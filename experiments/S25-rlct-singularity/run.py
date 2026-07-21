"""
S25 test — does the learning coefficient (RLCT) chart the prediction field at
its singular points, where the Fisher metric (S3) degenerates and d/2 fails?

Watanabe's singular learning theory: the Bayesian free energy obeys
    F_n = n L_n(w0) + lambda log n - (m-1) log log n + O_p(1),
where lambda is the real log canonical threshold (RLCT) of the loss's zero set
and m its multiplicity. For regular models lambda = d/2; at singularities
lambda < d/2, and lambda — not d/2 — controls Bayes generalization (~ lambda/n).

Registered predictions (written BEFORE running):

  Leg A (theory anchor, exactly known lambdas). Three 1-2 parameter models,
     truth = 0, posterior integrals by quadrature (no MCMC):
       M1  y = w x        regular    lambda = 1/2, m = 1   (d/2 = 1/2)
       M2  y = (a b) x    singular   lambda = 1/2, m = 2   (d/2 = 1)
       M3  y = w^2 x      singular   lambda = 1/4, m = 1   (d/2 = 1/2)
     Prediction: free-energy slopes recover these lambdas; d/2 fails on M2, M3.

  Leg B (the repo's singular point). Bayesian random-feature regression,
     input dim D = 20, feature count P swept 2..60. The population Fisher
     matrix R^T E[xx^T] R has rank min(P, D) — the model becomes SINGULAR at
     P = D (this is the population analogue of S3's finite-sample degeneracy
     at P = N). Prediction: lambda_hat(P) = min(P, D)/2 — rises like P/2,
     then KINKS FLAT at P = D — and n * (Bayes generalization error) tracks
     lambda_hat(P), not P/2, in the overparameterized regime.

  Leg C (transfer). Under covariate shift (anisotropic test inputs), excess
     transfer risk at P >= D should PLATEAU with lambda (ratio T(P=60)/T(P=D)
     near 1) rather than grow with parameter count (naive d-scaling: ~3x).

Pure numpy, deterministic (seeded). Outputs curves.npz + verdict.json + ASCII.
"""
import numpy as np
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
SIGMA = 0.5          # observation noise (known to the model)
S2 = SIGMA ** 2


# ----------------------------------------------------------------------
# Leg A — free-energy slopes for models with exactly known RLCT
# ----------------------------------------------------------------------
# All three models have mean u(theta) * x with u = w, ab, w^2. With truth
# u0 = 0, the normalized free energy is
#   Ftilde_n = -log Int prior(theta) exp[(2 u Sxy - u^2 Sxx)/(2 s^2)] dtheta,
# needing only the sufficient statistics Sxx = sum x^2, Sxy = sum x y.

def ftilde_M1(Sxx, Sxy):
    # regular: Gaussian x Gaussian, closed form
    q = Sxx / S2
    return 0.5 * np.log1p(q) - (Sxy / S2) ** 2 / (2.0 * (1.0 + q))

def ftilde_M2(Sxx, Sxy):
    # y = ab x: integrate b analytically (Gaussian in b for fixed a),
    # then quadrature over a. Integrand is O(1)-smooth in a (the fine
    # posterior scale lives in b and is handled exactly).
    a = np.linspace(-8, 8, 4001)
    qa = a * a * Sxx / S2
    g = -0.5 * np.log1p(qa) + (a * Sxy / S2) ** 2 / (2.0 * (1.0 + qa))
    logint = _logtrapz(-0.5 * a * a + g, a) - 0.5 * np.log(2 * np.pi)
    return -logint

def ftilde_M3(Sxx, Sxy):
    # y = w^2 x: 1D quadrature; two-scale grid (posterior width ~ n^-1/4)
    w = np.unique(np.concatenate([np.linspace(-6, 6, 4001),
                                  np.linspace(-0.5, 0.5, 8001)]))
    u = w * w
    e = -0.5 * w * w + (2 * u * Sxy - u * u * Sxx) / (2 * S2)
    logint = _logtrapz(e, w) - 0.5 * np.log(2 * np.pi)
    return -logint

def _logtrapz(loga, x):
    m = loga.max()
    return m + np.log(np.trapezoid(np.exp(loga - m), x))

def leg_A(n_list=(100, 1000, 10000, 100000, 1000000), seeds=20):
    models = {
        "M1 y=wx (regular)":   (ftilde_M1, 0.50, 1, 0.5),
        "M2 y=abx (singular)": (ftilde_M2, 0.50, 2, 1.0),
        "M3 y=w^2x (singular)": (ftilde_M3, 0.25, 1, 0.5),
    }
    n_arr = np.array(n_list, float)
    res = {}
    for name, (ft, lam_th, mult, dhalf) in models.items():
        F = np.zeros((seeds, len(n_list)))
        for s in range(seeds):
            rng = np.random.default_rng(3000 + s)
            x = rng.normal(size=n_list[-1])
            eps = SIGMA * rng.normal(size=n_list[-1])   # truth: y = 0 + noise
            for j, n in enumerate(n_list):
                Sxx = float(x[:n] @ x[:n]); Sxy = float(x[:n] @ eps[:n])
                F[s, j] = ft(Sxx, Sxy)
        Fbar = F.mean(0)
        # fit registered form: Ftilde = lambda log n - (m-1) log log n + c
        target = Fbar + (mult - 1) * np.log(np.log(n_arr))
        lam_hat = np.polyfit(np.log(n_arr), target, 1)[0]
        raw_slope = np.polyfit(np.log(n_arr), Fbar, 1)[0]
        res[name] = {"lambda_hat": float(lam_hat), "lambda_theory": lam_th,
                     "raw_slope": float(raw_slope), "d_half": dhalf,
                     "multiplicity": mult, "Fbar": Fbar.tolist()}
    return res, n_arr


# ----------------------------------------------------------------------
# Leg B — lambda(P) across the random-feature sweep + Bayes gen error
# ----------------------------------------------------------------------
def free_energy_lin(Phi, y, alpha2=1.0):
    """Exact -log marginal likelihood of y ~ N(0, S2 I + alpha2 Phi Phi^T),
    via the P x P Woodbury forms."""
    n, P = Phi.shape
    G = Phi.T @ Phi
    A = (S2 / alpha2) * np.eye(P) + G
    b = Phi.T @ y
    quad = (y @ y - b @ np.linalg.solve(A, b)) / S2
    logdet = n * np.log(S2) + np.linalg.slogdet(np.eye(P) + (alpha2 / S2) * G)[1]
    return 0.5 * (quad + logdet + n * np.log(2 * np.pi))

def leg_BC(D=20, Pmax=60, n_list=(200, 400, 800, 1600, 3200), seeds=24):
    Ps = np.arange(2, Pmax + 1, 2)
    n_arr = np.array(n_list, float)
    n_big = n_list[-1]
    rng0 = np.random.default_rng(7)
    beta = rng0.normal(size=D); beta /= np.linalg.norm(beta)   # teacher
    R = rng0.normal(size=(D, Pmax)) / np.sqrt(D)               # nested features
    # anisotropic covariate shift for Leg C
    shift_var = np.concatenate([np.full(D // 2, 4.0), np.full(D - D // 2, 0.25)])

    Ft = np.zeros((seeds, len(n_list), len(Ps)))
    excess = np.zeros((seeds, len(Ps)))       # in-dist Bayes excess risk, n=n_big
    shift_T = np.zeros((seeds, len(Ps)))      # covariate-shift excess risk
    for s in range(seeds):
        rng = np.random.default_rng(4000 + s)
        X = rng.normal(size=(n_big, D))
        y = X @ beta + SIGMA * rng.normal(size=n_big)
        for k, P in enumerate(Ps):
            RP = R[:, :P]
            w0 = np.linalg.pinv(RP) @ beta               # population-best params
            for j, n in enumerate(n_list):
                Phi = X[:n] @ RP
                nL0 = float(np.sum((y[:n] - Phi @ w0) ** 2)) / (2 * S2) \
                      + n / 2 * np.log(2 * np.pi * S2)
                Ft[s, j, k] = free_energy_lin(Phi, y[:n]) - nL0
            # posterior mean at n = n_big (alpha2 = 1)
            Phi = X @ RP
            A = S2 * np.eye(P) + Phi.T @ Phi
            wbar = np.linalg.solve(A, Phi.T @ y)
            r = RP @ wbar - beta                          # error in input space
            r0 = RP @ w0 - beta                           # best-in-class error
            excess[s, k] = (r @ r - r0 @ r0) / (2 * S2)   # E_x isotropic => norms
            rs = r * np.sqrt(shift_var)
            r0s = r0 * np.sqrt(shift_var)
            shift_T[s, k] = rs @ rs - r0s @ r0s
    lam_hat = np.array([np.polyfit(np.log(n_arr), Ft[:, :, k].mean(0), 1)[0]
                        for k in range(len(Ps))])
    G_scaled = n_big * excess.mean(0)                     # n * Bayes excess
    T = shift_T.mean(0)
    return Ps, lam_hat, G_scaled, T, D


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean(); ry -= ry.mean()
    return float((rx @ ry) / (np.sqrt(rx @ rx) * np.sqrt(ry @ ry) + 1e-12))


def ascii_plot(x, y, label, width=60, height=12):
    y = np.asarray(y, float)
    lo, hi = np.nanmin(y), np.nanmax(y)
    hi = hi if hi > lo else lo + 1
    grid = [[" "] * width for _ in range(height)]
    xi = ((x - x.min()) / (x.max() - x.min()) * (width - 1)).astype(int)
    yi = ((y - lo) / (hi - lo) * (height - 1)).astype(int)
    for a, b in zip(xi, yi):
        grid[height - 1 - b][a] = "*"
    return label + "\n" + "\n".join("".join(r) for r in grid) + \
        f"\nx: {x.min():.0f} .. {x.max():.0f}   y: {lo:.2f} .. {hi:.2f}"


def main():
    print("=" * 68)
    print("LEG A — RLCT estimator vs exact theory (regular vs singular)")
    print("=" * 68)
    resA, nA = leg_A()
    okA = True
    for name, r in resA.items():
        hit = abs(r["lambda_hat"] - r["lambda_theory"]) <= 0.06
        beats = abs(r["lambda_hat"] - r["lambda_theory"]) < abs(r["lambda_hat"] - r["d_half"]) \
                or abs(r["lambda_theory"] - r["d_half"]) < 1e-9
        okA &= hit
        print(f"  {name:24s} lambda_hat={r['lambda_hat']:.3f} "
              f"theory={r['lambda_theory']:.2f}  d/2={r['d_half']:.2f}  "
              f"raw_slope={r['raw_slope']:.3f}  {'OK' if hit else 'MISS'}")

    print("\n" + "=" * 68)
    print("LEG B — lambda(P) across the random-feature sweep (D=20)")
    print("=" * 68)
    Ps, lam, Gs, T, D = leg_BC()
    theory = np.minimum(Ps, D) / 2.0
    print(ascii_plot(Ps, lam, "lambda_hat(P)  [prediction: min(P,20)/2 — kink at P=20]"))
    dev = lam - theory
    rise = Ps <= D - 4            # misspecified regular regime (lambda = P/2)
    crit = (Ps > D - 4) & (Ps < D + 6)   # window around the singular point
    plat = Ps >= D + 6            # singular regime (lambda = D/2 exactly)
    rise_dev = float(np.mean(np.abs(dev[rise])))
    crit_dev = float(np.max(np.abs(dev[crit])))
    plat_dev = float(np.max(np.abs(dev[plat])))
    over = Ps >= D
    lam_end = float(lam[-1])
    print(f"\n|lambda_hat - min(P,D)/2|: rise(P<=16) mean={rise_dev:.3f}   "
          f"critical window(P=18..24) max={crit_dev:.3f}   plateau(P>=26) max={plat_dev:.3f}")
    print(f"lambda_hat(P=60) = {lam_end:.2f}   [singular theory: {D/2:.1f} | d/2: {Ps[-1]/2:.1f}]")
    rho_lam = spearman(Gs[over], lam[over]); rho_d = spearman(Gs[over], Ps[over] / 2.0)
    gs_ratio = float(Gs[-1] / Gs[np.searchsorted(Ps, D)])
    print(f"n*BayesExcess at P=60 / at P=20 = {gs_ratio:.2f}  (lambda predicts ~1, d/2 predicts ~3)")

    print("\n" + "=" * 68)
    print("LEG C — transfer under covariate shift: lambda or parameter count?")
    print("=" * 68)
    print(ascii_plot(Ps, T, "shift excess risk T(P)"))
    t_ratio = float(T[-1] / T[np.searchsorted(Ps, D)])
    print(f"\nT(P=60)/T(P=20) = {t_ratio:.2f}  (lambda-plateau predicts ~1, d-scaling ~3)")

    verdict = {
        "legA_estimator": {
            k: {"lambda_hat": round(r["lambda_hat"], 3),
                "lambda_theory": r["lambda_theory"], "d_half": r["d_half"]}
            for k, r in resA.items()},
        "legA_all_within_0.06": bool(okA),
        "legB_rise_mean_dev": round(rise_dev, 3),
        "legB_critical_window_max_dev": round(crit_dev, 3),
        "legB_plateau_max_dev": round(plat_dev, 3),
        "legB_kink_confirmed": bool(plat_dev < 0.1 and rise_dev < 1.0
                                    and abs(lam_end - D / 2) < 0.1),
        "legB_n_gen_ratio_60_vs_20": round(gs_ratio, 2),
        "legB_gen_tracks_lambda_not_d": bool(gs_ratio < 1.5),
        "legC_transfer_ratio_60_vs_20": round(t_ratio, 2),
        "legC_transfer_plateaus_with_lambda": bool(t_ratio < 1.5),
    }
    np.savez(os.path.join(OUT, "curves.npz"),
             Ps=Ps, lambda_hat=lam, lambda_theory=theory, n_gen=Gs, shift_T=T,
             legA_n=nA, **{f"legA_F_{i}": np.array(r["Fbar"])
                           for i, r in enumerate(resA.values())})
    with open(os.path.join(OUT, "verdict.json"), "w") as f:
        json.dump(verdict, f, indent=2)
    print("\n" + "=" * 68)
    print("VERDICT:", json.dumps(verdict, indent=2))


if __name__ == "__main__":
    main()
