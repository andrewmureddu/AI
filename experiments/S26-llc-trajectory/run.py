"""
S26 test — is degeneracy an ATTRACTOR of learning dynamics? (the learning-domain
instance of S11, built on S25's chart)

S25 established that the learning coefficient lambda (RLCT) charts the prediction
field at its singular points. S11 conjectures criticality/degeneracy is an
attractor of optimization. Weld: estimate the LOCAL learning coefficient
lambda_hat(t) along an SGD trajectory of a small nonlinear network and see
whether the dynamics flow toward singular (low-lambda) regions.

Estimator: SGLD on the localized tempered posterior (Lau et al.-style local
learning coefficient),
    dw = -(eps/2) [ n*beta grad L_n(w) + gamma (w - w*) ] dt + N(0, eps),
    lambda_hat = n * beta * ( E_chain[L_n] - L_n(w*) ),  beta = 1/log n.

Registered predictions (written BEFORE running):

  Leg A (calibration, welded to S25's quadrature): the SGLD estimator targets
     the LOCALIZED tempered functional, whose exact value we can compute by
     S25-style quadrature for the same three models:
       A1  regular linear d=5:      asymptotic lambda = 2.5
       A2  y = ab x   (singular):   asymptotic lambda = 0.5   (d/2 = 1)
       A3  y = w^2 x  (singular):   asymptotic lambda = 0.25  (d/2 = 0.5)
     Prediction: SGLD matches the exact localized-functional value within 15%
     on all three. Known and reported honestly: at multiplicity>1 singularities
     the finite-n functional itself under-reads asymptotic lambda (the
     log log n effect S25 measured in M2's raw slope); regular points read
     accurately, so singular-vs-regular discrimination is conservative.

  Leg B (the trajectory). Student tanh net (1-8-1, d=16 params) learns a
     2-neuron teacher, mini-batch SGD, checkpoints across training:
       P1  the solution is singular: final lambda_hat < d/4 = 4
           (teacher needs only 2 of 8 units; 6 are excess degeneracy)
       P2  lambda_hat moves with structure: its largest rise falls in the same
           checkpoint window (+/- 1) as the largest training-loss drop
           (learning a feature buys effective dimensions)
       P3  the S11 direction: AFTER the loss has converged, lambda_hat keeps
           drifting DOWN — SGD noise moves along the loss level-set toward more
           singular points. Test: mean lambda_hat over the last quarter of the
           converged phase < mean over its first quarter.

Falsifier for S11-in-learning: lambda_hat(final) ~ d/2 (regular solution), or
lambda_hat drifting UP after convergence (dynamics repelled from degeneracy).

Pure numpy, deterministic (seeded). Outputs curves.npz + verdict.json + ASCII.
"""
import numpy as np
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
SIGMA = 0.1          # observation noise (model noise, known)
S2 = SIGMA ** 2


# ----------------------------------------------------------------------
# SGLD local learning coefficient estimator (shared by both legs)
# ----------------------------------------------------------------------
def llc_sgld(wstar, grad_L, L_full, n, rng,
             eps=1e-5, gamma=50.0, chains=2, steps=16000, burn=5000):
    """lambda_hat at wstar. grad_L/L_full take a flat parameter vector and
    return full-data gradient / loss (mean negative log-likelihood)."""
    beta = 1.0 / np.log(n)
    Lstar = L_full(wstar)
    acc = []
    for _ in range(chains):
        w = wstar.copy()
        tot, cnt = 0.0, 0
        for t in range(steps):
            g = n * beta * grad_L(w) + gamma * (w - wstar)
            w = w - 0.5 * eps * g + np.sqrt(eps) * rng.normal(size=w.shape)
            if t >= burn:
                tot += L_full(w); cnt += 1
        acc.append(tot / cnt)
    return float(n * beta * (np.mean(acc) - Lstar)), float(np.std(acc) * n * beta)


# ----------------------------------------------------------------------
# Leg A — calibration on models whose lambda S25 verified exactly
# ----------------------------------------------------------------------
def leg_A(n=1024, seeds=4):
    cases = {}
    rng0 = np.random.default_rng(11)

    # A1: regular linear, d=5, truth 0
    d = 5
    X = rng0.normal(size=(n, d)); y = SIGMA * rng0.normal(size=n)
    wstar = np.linalg.lstsq(X, y, rcond=None)[0]
    L1 = lambda w: float(np.mean((y - X @ w) ** 2) / (2 * S2))
    g1 = lambda w: -(X.T @ (y - X @ w)) / (n * S2)
    cases["A1 linear d=5 (regular)"] = (wstar, g1, L1, 2.5, 2.5)

    # A2: y = ab x, truth 0 -> lambda = 1/2 (d/2 = 1)
    x2 = rng0.normal(size=n); y2 = SIGMA * rng0.normal(size=n)
    Sxx, Sxy = float(x2 @ x2), float(x2 @ y2)
    def L2(w):
        u = w[0] * w[1]
        return float((y2 @ y2 - 2 * u * Sxy + u * u * Sxx) / (2 * n * S2))
    def g2(w):
        u = w[0] * w[1]
        du = (-Sxy + u * Sxx) / (n * S2)
        return np.array([du * w[1], du * w[0]])
    cases["A2 y=abx (singular)"] = (np.zeros(2), g2, L2, 0.5, 1.0)

    # A3: y = w^2 x, truth 0 -> lambda = 1/4 (d/2 = 0.5)
    def L3(w):
        u = w[0] ** 2
        return float((y2 @ y2 - 2 * u * Sxy + u * u * Sxx) / (2 * n * S2))
    def g3(w):
        u = w[0] ** 2
        return np.array([2 * w[0] * (-Sxy + u * Sxx) / (n * S2)])
    cases["A3 y=w^2x (singular)"] = (np.zeros(1), g3, L3, 0.25, 0.5)

    # exact values of the SAME localized tempered functional (quadrature, per
    # S25's analytic-in-b reduction), gamma matching the sampler's localizer
    gam = 50.0
    beta = 1.0 / np.log(n)
    h = beta * 1e-4

    H1 = X.T @ X / S2                                   # A1: quadratic, closed form
    exact1 = 0.5 * np.trace(np.linalg.solve(beta * H1 + gam * np.eye(d), beta * H1))

    def logZ2(b):
        a = np.linspace(-3, 3, 40001)
        c = gam + b * a * a * Sxx / S2
        e = -0.5 * gam * a * a - 0.5 * np.log(c / gam) + (b * a * Sxy / S2) ** 2 / (2 * c)
        m = e.max(); return m + np.log(np.trapezoid(np.exp(e - m), a))

    def logZ3(b):
        w = np.unique(np.concatenate([np.linspace(-3, 3, 40001),
                                      np.linspace(-0.3, 0.3, 40001)]))
        u = w * w
        e = -0.5 * gam * w * w + b * (2 * u * Sxy - u * u * Sxx) / (2 * S2)
        m = e.max(); return m + np.log(np.trapezoid(np.exp(e - m), w))

    exact2 = -beta * (logZ2(beta + h) - logZ2(beta - h)) / (2 * h)
    exact3 = -beta * (logZ3(beta + h) - logZ3(beta - h)) / (2 * h)
    exacts = {"A1 linear d=5 (regular)": float(exact1),
              "A2 y=abx (singular)": float(exact2),
              "A3 y=w^2x (singular)": float(exact3)}

    out = {}
    for name, (ws, g, L, lam_th, dhalf) in cases.items():
        ests = []
        for s in range(seeds):
            rng = np.random.default_rng(500 + s)
            lam, _ = llc_sgld(ws, g, L, n, rng)
            ests.append(lam)
        out[name] = {"lambda_hat": float(np.mean(ests)),
                     "sd": float(np.std(ests)),
                     "exact_localized": exacts[name],
                     "lambda_theory": lam_th, "d_half": dhalf}
    return out


# ----------------------------------------------------------------------
# Leg B — lambda_hat along a tanh-network SGD trajectory
# ----------------------------------------------------------------------
def make_net(n=1024, H=8):
    """Student 1-H-1 tanh net f(x) = a . tanh(b x); teacher uses 2 units."""
    rng = np.random.default_rng(21)
    x = rng.normal(size=n)
    a_t = np.array([1.5, -1.0]); b_t = np.array([0.7, 3.0])
    f_t = np.tanh(np.outer(x, b_t)) @ a_t
    y = f_t + SIGMA * rng.normal(size=n)
    return x, y, H

def unpack(w, H):
    return w[:H], w[H:]           # a (output), b (input)

def net_L(w, x, y, H):
    a, b = unpack(w, H)
    r = y - np.tanh(np.outer(x, b)) @ a
    return float(np.mean(r ** 2) / (2 * S2))

def net_grad(w, x, y, H, idx=None):
    if idx is not None:
        x, y = x[idx], y[idx]
    a, b = unpack(w, H)
    T = np.tanh(np.outer(x, b))                  # (m, H)
    r = y - T @ a                                # (m,)
    ga = -(T.T @ r) / (len(x) * S2)
    gb = -(((1 - T * T) * x[:, None]).T @ r) * a / (len(x) * S2)
    return np.concatenate([ga, gb])

def leg_B(n=1024, H=8, lr=0.05, batch=32, T_fit=20000, T_drift=120000,
          n_ckpt_fit=16, n_ckpt_drift=10, llc_seeds=2):
    x, y, H = make_net(n, H)
    d = 2 * H
    rng = np.random.default_rng(33)
    w = 0.4 * rng.normal(size=d)
    # checkpoints: log-spaced through fitting, linear through the drift phase
    ck_fit = np.unique(np.geomspace(1, T_fit, n_ckpt_fit).astype(int))
    ck_drift = np.linspace(T_fit + (T_drift - T_fit) / n_ckpt_drift, T_drift,
                           n_ckpt_drift).astype(int)
    ckpts = np.concatenate([[0], ck_fit, ck_drift])
    snaps, losses, steps_at = [], [], []
    nxt = 0
    for t in range(T_drift + 1):
        if nxt < len(ckpts) and t == ckpts[nxt]:
            snaps.append(w.copy())
            losses.append(net_L(w, x, y, H))
            steps_at.append(t)
            nxt += 1
        idx = rng.integers(0, n, batch)
        # SGD on the plain MSE (the likelihood 1/S2 scaling belongs to the
        # LLC functional, not to the optimizer's step size)
        w = w - lr * S2 * net_grad(w, x, y, H, idx)
    lam_t, lam_sd = [], []
    for w_ck in snaps:
        g = lambda ww: net_grad(ww, x, y, H)
        L = lambda ww: net_L(ww, x, y, H)
        ests = []
        for s in range(llc_seeds):
            rng2 = np.random.default_rng(900 + s)
            lam, _ = llc_sgld(w_ck, g, L, n, rng2)
            ests.append(lam)
        lam_t.append(float(np.mean(ests)))
        lam_sd.append(float(np.std(ests)))
    return (np.array(steps_at), np.array(losses), np.array(lam_t),
            np.array(lam_sd), d, T_fit)


def posthoc_full_batch(n=1024, H=8, lr=0.05, T=120000, llc_seeds=2):
    """POST-HOC CONTROL (added after seeing P3 fail; not a registered
    prediction). If SGD noise drives the parameters toward degeneracy, a
    noiseless full-batch run from the same init should end at HIGHER lambda_hat
    than the SGD run. If the two match, the endpoint's singularity is generic
    to the low-loss set, not noise-seeking."""
    x, y, H = make_net(n, H)
    rng = np.random.default_rng(33)
    w = 0.4 * rng.normal(size=2 * H)
    for _ in range(T):
        w = w - lr * S2 * net_grad(w, x, y, H)
    loss = net_L(w, x, y, H)
    g = lambda ww: net_grad(ww, x, y, H)
    L = lambda ww: net_L(ww, x, y, H)
    ests = [llc_sgld(w, g, L, n, np.random.default_rng(900 + s))[0]
            for s in range(llc_seeds)]
    return float(np.mean(ests)), float(loss)


def ascii_plot(x, y, label, width=64, height=12, logx=False):
    y = np.asarray(y, float)
    xx = np.log10(np.asarray(x, float) + 1) if logx else np.asarray(x, float)
    lo, hi = np.nanmin(y), np.nanmax(y)
    hi = hi if hi > lo else lo + 1
    grid = [[" "] * width for _ in range(height)]
    xi = ((xx - xx.min()) / (xx.max() - xx.min()) * (width - 1)).astype(int)
    yi = ((y - lo) / (hi - lo) * (height - 1)).astype(int)
    for a, b in zip(xi, yi):
        grid[height - 1 - b][a] = "*"
    return label + "\n" + "\n".join("".join(r) for r in grid) + \
        f"\ny: {lo:.2f} .. {hi:.2f}"


def main():
    print("=" * 68)
    print("LEG A — SGLD estimator vs S25's exact learning coefficients")
    print("=" * 68)
    resA = leg_A()
    okA = True
    for name, r in resA.items():
        rel = abs(r["lambda_hat"] - r["exact_localized"]) / r["exact_localized"]
        hit = rel <= 0.15
        okA &= hit
        print(f"  {name:26s} lambda_hat={r['lambda_hat']:.3f} (sd {r['sd']:.3f})  "
              f"exact-functional={r['exact_localized']:.3f}  asymptotic={r['lambda_theory']:.2f}  "
              f"d/2={r['d_half']:.2f}  {'OK' if hit else 'MISS'} ({100*rel:.0f}%)")

    print("\n" + "=" * 68)
    print("LEG B — lambda_hat along the SGD trajectory (1-8-1 tanh, d=16)")
    print("=" * 68)
    steps, losses, lam, lam_sd, d, T_fit = leg_B()
    print(ascii_plot(steps, np.log10(losses), "log10 train loss vs log10 step", logx=True))
    print()
    print(ascii_plot(steps, lam, "lambda_hat vs log10 step   [d/2 = 8]", logx=True))
    for t, l, lm, sd in zip(steps, losses, lam, lam_sd):
        print(f"  step {t:>7d}  loss={l:9.4f}  lambda_hat={lm:6.2f} +/- {sd:.2f}")

    # P1 — final solution singular
    lam_final = float(np.mean(lam[-3:]))
    p1 = lam_final < d / 4

    # P2 — NOT EVALUABLE as designed: mid-training checkpoints are not
    # critical points, so the localized chain flows downhill and lambda_hat
    # goes negative (it measures escape, not dimension). Recorded, not scored.
    fit = steps <= T_fit
    p2_evaluable = bool(np.all(lam[fit][1:] > 0))

    # P3 — post-convergence drift toward degeneracy
    drift = steps > T_fit
    lam_d = lam[drift]
    q = max(2, len(lam_d) // 4)
    early, late = float(np.mean(lam_d[:q])), float(np.mean(lam_d[-q:]))
    loss_flat = abs(np.log10(losses[drift][-1] / losses[drift][0])) < 0.3
    p3 = late < early

    print(f"\nP1 singular solution: lambda_final={lam_final:.2f} < d/4={d/4:.0f}?  {p1}")
    print(f"P2: evaluable={p2_evaluable} — mid-training lambda_hat is negative "
          f"(non-critical checkpoints); the test cannot be scored as designed")
    print(f"P3 post-convergence drift: early={early:.2f} -> late={late:.2f} "
          f"(loss flat by 0.3-dex criterion: {loss_flat})  {p3}")

    print("\nPOST-HOC CONTROL (unregistered): full-batch GD from the same init")
    lam_gd, loss_gd = posthoc_full_batch()
    print(f"  full-batch endpoint: loss={loss_gd:.4f}  lambda_hat={lam_gd:.2f}  "
          f"vs SGD lambda_final={lam_final:.2f}")

    verdict = {
        "legA_calibration": {k: {"lambda_hat": round(r["lambda_hat"], 3),
                                 "exact_localized": round(r["exact_localized"], 3),
                                 "lambda_theory": r["lambda_theory"],
                                 "d_half": r["d_half"]} for k, r in resA.items()},
        "legA_within_15pct_of_exact_functional": bool(okA),
        "P1_final_lambda": round(lam_final, 2),
        "P1_singular_solution": bool(p1),
        "P2_evaluable": p2_evaluable,
        "P2_note": "mid-training checkpoints are non-critical; lambda_hat<0 there measures escape, not dimension",
        "P3_lambda_early_converged": round(early, 2),
        "P3_lambda_late_converged": round(late, 2),
        "P3_loss_flat_during_drift": bool(loss_flat),
        "P3_drifts_toward_degeneracy": bool(p3),
        "posthoc_fullbatch_lambda": round(lam_gd, 2),
        "posthoc_fullbatch_loss": round(loss_gd, 4),
        "posthoc_sgd_noise_seeks_degeneracy": bool(lam_gd - lam_final > 0.5),
    }
    np.savez(os.path.join(OUT, "curves.npz"), steps=steps, losses=losses,
             lam=lam, lam_sd=lam_sd, d=d, T_fit=T_fit)
    with open(os.path.join(OUT, "verdict.json"), "w") as f:
        json.dump(verdict, f, indent=2)
    print("\n" + "=" * 68)
    print("VERDICT:", json.dumps(verdict, indent=2))


if __name__ == "__main__":
    main()
