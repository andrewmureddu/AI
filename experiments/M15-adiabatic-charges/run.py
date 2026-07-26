"""M15 — is SGD's quasi-conserved charge an adiabatic invariant?

S26 found the balancedness charge Q = u^2 - v^2 quasi-conserved under
label-noise SGD (erosion ~5.6e-7/step) and called the result a
"prethermalization plateau."  That is a description.  M15 asks whether the
AVERAGING MECHANISM is running, which is a question about how the erosion
rate scales with the slowness parameter (here the learning rate eta):

    ordinary averaging   ->  k ~ eta^p, power law
    Nekhoroshev regime   ->  k ~ exp(-c/eta), exponentially protected

Predictions are registered in PREREGISTRATION.md BEFORE this was run:
  P1 exact per-step law Q' = Q(1 - eta^2 m^2)      (machine precision)
  P2 k ~ eta^2 sigma^2 / B                          (p=2, q=2, s=-1)
  P3 power law beats exp(-c/eta) decisively         (the discriminator)
  P4 absolute k = eta^2 sigma^2 E[x^2] / B within 10%, no fitting
  P5 S26's 5.6e-7 revises to ~7.8e-7
  P6 scaling survives in a wide two-layer net where the exact algebra does not
  P7 breakdown when timescale separation R -> O(1)   (exploratory)

Pure numpy, deterministic seeds, ~1 minute.  Seeds are vectorized: u, v are
arrays over seeds so the python loop runs once per STEP, not per seed.
"""
import json
import math

import numpy as np

# ----------------------------------------------------------------------------
# shared data (same generator/settings as S26 so numbers are comparable)
# ----------------------------------------------------------------------------
rng = np.random.default_rng(0)
w_true = 1.5
N = 200
x = rng.normal(size=N)
y_clean = w_true * x
Ex2 = float(np.mean(x**2))          # E[x^2] under the sampling distribution
w_hat = float(np.sum(x * y_clean) / np.sum(x * x))   # empirical LS optimum

S = 16          # seeds, vectorized
BURN = 4000     # steps to reach the plateau before measuring
MEASURE = 20000  # measurement window (relative estimator: precision ~ 1/sqrt(2T))


def sgd_charge_decay(eta, sigma, B, u0=1.7, v0=0.4, seed0=0,
                     burn=BURN, measure=MEASURE, instrument=False):
    """Label-noise SGD on f(x)=u*v*x.  Returns per-step charge decay rate k.

    Estimator: k = -mean_seeds( log Q(T) - log Q(0) ) / T over the plateau.
    Unbiased in the multiplicative-decay model regardless of total decay, with
    relative precision ~ 1/sqrt(2*T*S).
    """
    r = np.random.default_rng(1000 + seed0)
    u = np.full(S, float(u0))
    v = np.full(S, float(v0))
    logQ0 = None
    m2_acc = 0.0
    exact_err = 0.0
    uv_acc = 0.0

    for step in range(burn + measure):
        idx = r.integers(0, N, size=(S, B))
        xb = x[idx]                                   # (S,B)
        yb = y_clean[idx] + sigma * r.normal(size=(S, B))
        rb = (u * v)[:, None] * xb - yb               # residuals
        m = np.mean(rb * xb, axis=1)                  # the scalar the grads factor through
        gu = v * m
        gv = u * m
        if instrument and step == burn:
            Q_before = u * u - v * v
            u_next = u - eta * gu
            v_next = v - eta * gv
            Q_after = u_next * u_next - v_next * v_next
            pred = Q_before * (1.0 - eta**2 * m**2)
            exact_err = float(np.max(np.abs(Q_after - pred) / np.abs(Q_after)))
        u = u - eta * gu
        v = v - eta * gv
        if step == burn - 1:
            logQ0 = np.log(u * u - v * v)
        if step >= burn:
            m2_acc += float(np.mean(m**2))
            uv_acc += float(np.mean(u * v))

    logQT = np.log(u * u - v * v)
    k = float(-np.mean(logQT - logQ0) / measure)
    return {
        "k": k,
        "k_pred": eta**2 * sigma**2 * Ex2 / B,
        "m2_measured": m2_acc / measure,
        "m2_pred": sigma**2 * Ex2 / B,
        "uv_mean": uv_acc / measure,
        "exact_rel_err": exact_err,
        "Q_final": float(np.mean(np.exp(logQT))),
    }


def loglog_slope(xs, ys):
    """Least-squares slope of log y vs log x, plus R^2."""
    lx, ly = np.log(np.array(xs)), np.log(np.array(ys))
    p = np.polyfit(lx, ly, 1)
    resid = ly - np.polyval(p, lx)
    r2 = 1.0 - np.sum(resid**2) / np.sum((ly - ly.mean()) ** 2)
    return float(p[0]), float(r2), float(np.sum(resid**2))


def aic(sse, n, n_params):
    return n * math.log(sse / n) + 2 * n_params


out = {"setup": {"Ex2": Ex2, "w_hat": w_hat, "seeds": S,
                 "burn": BURN, "measure": MEASURE}}

# ---------------------------------------------------------------- P1: exactness
p1 = sgd_charge_decay(5e-3, 0.5, 8, instrument=True, burn=200, measure=200)
out["P1_exact_per_step_law"] = {
    "max_rel_err_vs_Q(1-eta^2 m^2)": p1["exact_rel_err"],
    "confirmed": bool(p1["exact_rel_err"] < 1e-12),
}

# ------------------------------------------------- P2/P3: the eta sweep (core)
etas = [1e-3, 2e-3, 4e-3, 7e-3, 1.2e-2, 2e-2, 3.2e-2, 5e-2]
eta_rows = []
for eta in etas:
    res = sgd_charge_decay(eta, 0.5, 8)
    eta_rows.append({"eta": eta, **res, "ratio": res["k"] / res["k_pred"]})
p_eta, r2_eta, sse_pow = loglog_slope([r["eta"] for r in eta_rows],
                                      [r["k"] for r in eta_rows])

# discriminator: power law  vs  Nekhoroshev-type log k = a - c/eta
inv_eta = np.array([1.0 / r["eta"] for r in eta_rows])
lk = np.log(np.array([r["k"] for r in eta_rows]))
p_nek = np.polyfit(inv_eta, lk, 1)
resid_nek = lk - np.polyval(p_nek, inv_eta)
sse_nek = float(np.sum(resid_nek**2))
r2_nek = 1.0 - sse_nek / float(np.sum((lk - lk.mean()) ** 2))
n = len(etas)
aic_pow, aic_nek = aic(sse_pow, n, 2), aic(sse_nek, n, 2)

out["P2P3_eta_sweep"] = {
    "rows": eta_rows,
    "power_law_exponent_p": p_eta,
    "power_law_R2": r2_eta,
    "nekhoroshev_R2": r2_nek,
    "AIC_power": aic_pow,
    "AIC_nekhoroshev": aic_nek,
    "delta_AIC_favouring_power": aic_nek - aic_pow,
    "p_in_registered_CI": bool(abs(p_eta - 2.0) < 0.05),
    "power_law_decisively_favoured": bool(aic_nek - aic_pow >= 10),
}

# --------------------------------------------------------- P2: sigma and B sweeps
sigmas = [0.25, 0.5, 1.0, 2.0]
sig_rows = [{"sigma": s, **sgd_charge_decay(8e-3, s, 8)} for s in sigmas]
q_sig, r2_sig, _ = loglog_slope([r["sigma"] for r in sig_rows],
                                [r["k"] for r in sig_rows])

batches = [1, 2, 4, 8, 16, 32]
b_rows = [{"B": b, **sgd_charge_decay(8e-3, 0.5, b)} for b in batches]
s_b, r2_b, _ = loglog_slope([r["B"] for r in b_rows], [r["k"] for r in b_rows])

out["P2_sigma_sweep"] = {"rows": sig_rows, "exponent_q": q_sig, "R2": r2_sig,
                         "q_in_registered_CI": bool(abs(q_sig - 2.0) < 0.05)}
out["P2_batch_sweep"] = {"rows": b_rows, "exponent_s": s_b, "R2": r2_b,
                         "s_in_registered_CI": bool(abs(s_b + 1.0) < 0.05)}

# ------------------------------------------- P4: absolute, parameter-free check
all_rows = eta_rows + sig_rows + b_rows
ratios = [r["k"] / r["k_pred"] for r in all_rows]
out["P4_absolute_no_fit"] = {
    "grid_points": len(ratios),
    "ratio_measured_over_predicted_min": float(min(ratios)),
    "ratio_max": float(max(ratios)),
    "ratio_median": float(np.median(ratios)),
    "all_within_10pct": bool(all(abs(r - 1.0) < 0.10 for r in ratios)),
}

# the residual is not noise: the plateau's own O(eta) fluctuation adds an
# O(eta) correction to E[m^2].  Fit ratio = 1 + c*eta and check it explains
# why the measured exponent sits slightly above 2.
c_fit = float(np.polyfit([r["eta"] for r in eta_rows],
                         [r["ratio"] - 1.0 for r in eta_rows], 1)[0])
eta_gm = float(np.exp(np.mean(np.log([r["eta"] for r in eta_rows]))))
out["P4_residual_is_lawful"] = {
    "ratio_model": "k_measured / k_predicted = 1 + c*eta",
    "c_fit": c_fit,
    "predicted_exponent_excess_at_geometric_mean_eta":
        c_fit * eta_gm / (1 + c_fit * eta_gm),
    "measured_exponent_excess": p_eta - 2.0,
}

# ------------------------------------------------------- P5: S26's number redone
s26 = sgd_charge_decay(5e-3, 0.5, 8)
out["P5_S26_revision"] = {
    "S26_reported_k": 5.6e-7,
    "S26_window_steps": 1.8e6,
    "M15_measured_k": s26["k"],
    "M15_predicted_k": s26["k_pred"],
    "M15_window_steps": 1.0 / s26["k"],
}

# ------------------------------------------- P6: wide net, exact algebra broken
def wide_net_drift(eta, sigma, B, d=6, h=4, steps=6000, seed=7):
    """f(x) = v^T W x.  Per-unit charges Q_j = ||W_j||^2 - v_j^2.

    Second-order term is eta^2 (v_j^2 ||m||^2 - <W_j,m>^2): NOT the scalar
    law, but predicted to keep the same eta^2 sigma^2 / B scaling.

    TWO estimators are reported, because the pre-registered one turned out to
    be wrong on its face:
      (a) net_displacement_per_step -- the PRE-REGISTERED estimator:
          |Q(T) - Q(0)| / T.  This measures DISPLACEMENT, not rate, and
          saturates once the charge reaches its eta-dependent quasi-equilibrium
          inside the window.  Kept because it is what was registered.
      (b) instantaneous_rate -- mean over steps of |Q(t+1) - Q(t)|, which
          cannot saturate.  This is the correct analogue of the scalar k.
    Also returns exact_rel_err: a P1-style check that the per-step change equals
    eta^2 (v_j^2||m||^2 - <W_j,m>^2) with no first-order term.
    """
    r = np.random.default_rng(seed)
    X = r.normal(size=(N, d))
    w_star = r.normal(size=d)
    Y = X @ w_star
    W = r.normal(size=(h, d)) * 0.6
    v = r.normal(size=h) * 0.6
    Qs = None
    inst_acc, cnt = 0.0, 0
    for phase in ("burn", "measure"):
        if phase == "measure":
            Qs = np.sum(W**2, axis=1) - v**2
        for step in range(steps):
            idx = r.integers(0, N, size=B)
            xb, yb = X[idx], Y[idx] + sigma * r.normal(size=B)
            rb = (W @ xb.T).T @ v - yb                 # (B,)
            m = (rb[:, None] * xb).mean(axis=0)        # (d,)
            gW = np.outer(v, m)
            gv = W @ m
            Q_before = np.sum(W**2, axis=1) - v**2
            W = W - eta * gW
            v = v - eta * gv
            Q_after = np.sum(W**2, axis=1) - v**2
            if phase == "measure":
                inst_acc += float(np.mean(np.abs(Q_after - Q_before)))
                cnt += 1
    Qe = np.sum(W**2, axis=1) - v**2
    return {"net_displacement_per_step": float(np.sqrt(np.mean((Qe - Qs) ** 2)) / steps),
            "instantaneous_rate": inst_acc / cnt,
            "Q_end": Qe.tolist()}


def wide_net_exactness(eta=8e-3, sigma=0.5, B=8, d=6, h=4, burn=2000, seed=7):
    """P1-analogue for the wide net: is the per-step change exactly second order?"""
    r = np.random.default_rng(seed)
    X = r.normal(size=(N, d))
    Y = X @ r.normal(size=d)
    W = r.normal(size=(h, d)) * 0.6
    v = r.normal(size=h) * 0.6
    worst = 0.0
    for step in range(burn + 50):
        idx = r.integers(0, N, size=B)
        xb, yb = X[idx], Y[idx] + sigma * r.normal(size=B)
        rb = (W @ xb.T).T @ v - yb
        m = (rb[:, None] * xb).mean(axis=0)
        gW, gv = np.outer(v, m), W @ m
        Q_before = np.sum(W**2, axis=1) - v**2
        pred = Q_before + eta**2 * (v**2 * float(m @ m) - (W @ m) ** 2)
        W, v = W - eta * gW, v - eta * gv
        Q_after = np.sum(W**2, axis=1) - v**2
        if step >= burn:
            worst = max(worst, float(np.max(np.abs(Q_after - pred)
                                            / np.maximum(np.abs(Q_after), 1e-12))))
    return worst


wide_rows = [{"eta": e, **wide_net_drift(e, 0.5, 8)}
             for e in (2e-3, 4e-3, 8e-3, 1.6e-2, 3.2e-2)]
p_wide_disp, r2_disp, _ = loglog_slope([r["eta"] for r in wide_rows],
                                       [r["net_displacement_per_step"] for r in wide_rows])
p_wide_inst, r2_inst, _ = loglog_slope([r["eta"] for r in wide_rows],
                                       [r["instantaneous_rate"] for r in wide_rows])
wide_sig = [{"sigma": s, **wide_net_drift(8e-3, s, 8)} for s in (0.25, 0.5, 1.0, 2.0)]
q_wide_disp, _, _ = loglog_slope([r["sigma"] for r in wide_sig],
                                 [r["net_displacement_per_step"] for r in wide_sig])
q_wide_inst, r2_qi, _ = loglog_slope([r["sigma"] for r in wide_sig],
                                     [r["instantaneous_rate"] for r in wide_sig])

# saturation diagnosis: if net displacement measures a RATE it grows ~ linearly
# with window length; if the charge has saturated it stops growing.
sat = []
for T in (750, 1500, 3000, 6000, 12000):
    lo = wide_net_drift(3.2e-2, 0.5, 8, steps=T)
    sat.append({"window": T,
                "net_displacement_total": lo["net_displacement_per_step"] * T,
                "instantaneous_rate": lo["instantaneous_rate"]})
sat_slope, sat_r2, _ = loglog_slope([s["window"] for s in sat],
                                    [s["net_displacement_total"] for s in sat])

def wide_net_relaxation(eta, sigma=0.5, B=8, d=6, h=4, seed=7,
                        burn_eta=1e-3, burn_steps=40000, T=None):
    """The non-tautological wide-net test: the charge RELAXATION TIME.

    In the scalar model ΔQ = -eta^2 m^2 Q drives Q -> 0 monotonically.  In the
    wide model ΔQ_j = eta^2 (v_j^2||m||^2 - <W_j,m>^2) has EITHER sign (it is
    positive when W_j is orthogonal to the noise direction m), so charges
    relax to an alignment-dependent quasi-equilibrium instead of to zero --
    which is why the displacement estimator saturated.

    So measure the approach: rms|Q(t)-Q(0)| = A(1-exp(-t/tau)), and test
    tau ~ eta^-2.  All runs start from a COMMON state (burn-in at fixed
    burn_eta) so the eta-dependence is not confounded by the state.
    """
    r = np.random.default_rng(seed)
    X = r.normal(size=(N, d))
    Y = X @ r.normal(size=d)
    W = r.normal(size=(h, d)) * 0.6
    v = r.normal(size=h) * 0.6

    def step(W, v, lr):
        idx = r.integers(0, N, size=B)
        xb, yb = X[idx], Y[idx] + sigma * r.normal(size=B)
        rb = (W @ xb.T).T @ v - yb
        m = (rb[:, None] * xb).mean(axis=0)
        return W - lr * np.outer(v, m), v - lr * (W @ m)

    for _ in range(burn_steps):          # common starting state for every eta
        W, v = step(W, v, burn_eta)
    Q0 = np.sum(W**2, axis=1) - v**2
    T = T if T is not None else int(3e5 * (8e-3 / eta) ** 2)
    T = int(min(max(T, 4000), 1_000_000))
    n_probe = 40
    probe = np.unique(np.linspace(T // n_probe, T, n_probe).astype(int))
    disp, pi = [], 0
    for t in range(1, T + 1):
        W, v = step(W, v, eta)
        if pi < len(probe) and t == probe[pi]:
            Q = np.sum(W**2, axis=1) - v**2
            disp.append(float(np.sqrt(np.mean((Q - Q0) ** 2))))
            pi += 1
    disp = np.array(disp)
    A = float(disp[-3:].mean())          # saturation amplitude, this run
    # a run counts as saturated only if the curve has actually flattened
    flat = bool(disp[-1] / max(disp[-6], 1e-30) < 1.15)
    return {"eta": eta, "T": T, "A_this_run": A, "flattened": flat,
            "probe": probe.tolist(), "disp": disp.tolist()}


def tau_from_curve(row, A):
    """First crossing of A*(1-1/e), linearly interpolated. None if never reached."""
    probe, disp = row["probe"], row["disp"]
    thresh = A * (1 - 1 / math.e)
    for i, dv in enumerate(disp):
        if dv >= thresh:
            if i == 0:
                return float(probe[0])
            f = (thresh - disp[i - 1]) / max(disp[i] - disp[i - 1], 1e-30)
            return float(probe[i - 1] + f * (probe[i] - probe[i - 1]))
    return None


# The saturation amplitude A is a property of the alignment quasi-equilibrium,
# NOT of eta -- so it is estimated once from the runs that actually flattened
# and applied as a common threshold to all of them.  (A per-run A biases tau
# downward for any run that hit its step cap before saturating.)
relax_raw = [wide_net_relaxation(e, T=int(min(1e6, 3e5 * (8e-3 / e) ** 2)))
             for e in (4e-3, 8e-3, 1.6e-2, 3.2e-2)]
A_vals = [r["A_this_run"] for r in relax_raw if r["flattened"]]
A_common = float(np.median(A_vals))
A_spread = float((max(A_vals) - min(A_vals)) / A_common) if len(A_vals) > 1 else None
relax = []
for r in relax_raw:
    tau = tau_from_curve(r, A_common)
    relax.append({"eta": r["eta"], "T": r["T"], "A_this_run": r["A_this_run"],
                  "flattened": r["flattened"], "tau_steps": tau,
                  "reached_common_threshold": tau is not None})
relax_ok = [r for r in relax if r["reached_common_threshold"]]
tau_slope, tau_r2, _ = (loglog_slope([r["eta"] for r in relax_ok],
                                     [r["tau_steps"] for r in relax_ok])
                        if len(relax_ok) >= 3 else (float("nan"),) * 3)

out["P6_wide_net"] = {
    "eta_rows": [{k: v for k, v in r.items() if k != "Q_end"} for r in wide_rows],
    "PREREGISTERED_estimator_net_displacement": {
        "exponent_p": p_wide_disp, "R2": r2_disp,
        "p_in_registered_CI": bool(abs(p_wide_disp - 2.0) < 0.10),
        "sigma_exponent_q": q_wide_disp,
    },
    "saturation_diagnosis": {
        "rows": sat,
        "displacement_vs_window_slope": sat_slope,
        "note": "slope 1 => estimator tracks a rate; slope < 1 => saturating",
        "instantaneous_rate_stable_across_windows": bool(
            max(s["instantaneous_rate"] for s in sat)
            / min(s["instantaneous_rate"] for s in sat) < 1.15),
    },
    "CORRECTED_estimator_instantaneous_rate": {
        "exponent_p": p_wide_inst, "R2": r2_inst,
        "sigma_exponent_q": q_wide_inst, "sigma_R2": r2_qi,
        "p_in_registered_CI": bool(abs(p_wide_inst - 2.0) < 0.10),
        "q_in_registered_CI": bool(abs(q_wide_inst - 2.0) < 0.10),
    },
    "exactness_second_order_only_max_rel_err": wide_net_exactness(),
    "DECISIVE_relaxation_time": {
        "rows": relax,
        "A_common_threshold_amplitude": A_common,
        "A_n_saturated_runs": len(A_vals),
        "A_relative_spread_across_eta": A_spread,
        "tau_vs_eta_exponent": tau_slope,
        "R2": tau_r2,
        "registered_prediction": -2.0,
        "in_CI": bool(abs(tau_slope + 2.0) < 0.10) if tau_slope == tau_slope else False,
        "note": ("charges relax to an alignment-dependent quasi-equilibrium, not "
                 "to zero; the relaxation RATE is the eta^2 quantity"),
    },
}

# ------------------------------------------------- P7: breakdown (exploratory)
def sufficiency_error(eta, sigma, B, steps=20000, seed0=3):
    """Does Q still coordinatize the plateau?  ||(u,v)||^2 =? sqrt(Q^2+4w^2)."""
    r = np.random.default_rng(500 + seed0)
    u = np.full(S, 1.7)
    v = np.full(S, 0.4)
    norm_acc, Q_acc, cnt = 0.0, 0.0, 0
    diverged = False
    for step in range(steps):
        idx = r.integers(0, N, size=(S, B))
        xb = x[idx]
        yb = y_clean[idx] + sigma * r.normal(size=(S, B))
        rb = (u * v)[:, None] * xb - yb
        m = np.mean(rb * xb, axis=1)
        gu, gv = v * m, u * m              # both from PRE-update u, v
        u = u - eta * gu
        v = v - eta * gv
        if not np.all(np.isfinite(u)) or np.max(u * u + v * v) > 1e6:
            diverged = True
            break
        if step >= steps // 2:
            norm_acc += float(np.mean(u * u + v * v))
            Q_acc += float(np.mean(u * u - v * v))
            cnt += 1
    if diverged or cnt == 0:
        return {"eta": eta, "sigma": sigma, "B": B, "diverged": True}
    Qm, nm = Q_acc / cnt, norm_acc / cnt
    pred = math.sqrt(Qm**2 + 4 * w_hat**2)
    lam = nm * Ex2                                  # stiff curvature estimate
    R = B * lam / (eta * sigma**2 * Ex2)            # timescale separation
    return {"eta": eta, "sigma": sigma, "B": B, "R": R, "diverged": False,
            "norm_observed": nm, "norm_predicted_from_charge": pred,
            "suff_rel_err": abs(pred - nm) / nm,
            "stability_margin_eta_lambda": eta * lam,
            "R_lower_bound_from_stability": B * lam**2 / (2 * sigma**2 * Ex2)}


grid = []
for eta in (5e-3, 1e-2, 2e-2, 4e-2, 8e-2, 1.6e-1):
    for sigma in (0.5, 1.0, 2.0, 4.0):
        for B in (1, 8):
            grid.append(sufficiency_error(eta, sigma, B, steps=8000))
ok = [g for g in grid if not g.get("diverged")]
# Does the coordinatization degrade with the timescale separation, and where is
# the knee?  Fit suff_err ~ C * R^-a above the measurement floor.
floor = 1e-3
fit_pts = [g for g in ok if g["suff_rel_err"] > floor]
a_R, r2_R, _ = (loglog_slope([g["R"] for g in fit_pts],
                             [g["suff_rel_err"] for g in fit_pts])
                if len(fit_pts) >= 3 else (float("nan"),) * 3)
C_R = (float(np.exp(np.mean([math.log(g["suff_rel_err"]) - a_R * math.log(g["R"])
                             for g in fit_pts]))) if fit_pts else float("nan"))
out["P7_breakdown"] = {
    "grid": sorted(ok, key=lambda g: g["R"]) + [g for g in grid if g.get("diverged")],
    "n_stable": len(ok),
    "n_diverged": len(grid) - len(ok),
    "min_R_among_stable": min((g["R"] for g in ok), default=None),
    "max_suff_err_among_stable": max((g["suff_rel_err"] for g in ok), default=None),
    "worst_config": max(ok, key=lambda g: g["suff_rel_err"]) if ok else None,
    "suff_err_vs_R_exponent": a_R,
    "suff_err_vs_R_R2": r2_R,
    "suff_err_prefactor_C": C_R,
    "R_at_which_err_reaches_unity": (C_R ** (-1.0 / a_R)) if a_R == a_R else None,
    "n_points_above_floor": len(fit_pts),
}

# ------------------------------------------------------------------- verdict
out["VERDICT"] = {
    "P1_exact_law": out["P1_exact_per_step_law"]["confirmed"],
    "P2_exponents": {"p_eta": p_eta, "q_sigma": q_sig, "s_batch": s_b},
    "P3_regime": ("ordinary averaging (power law)"
                  if aic_nek - aic_pow >= 10 else "INCONCLUSIVE / exponential"),
    "P4_absolute_within_10pct": out["P4_absolute_no_fit"]["all_within_10pct"],
    "P6_preregistered_displacement_estimator": out["P6_wide_net"][
        "PREREGISTERED_estimator_net_displacement"]["p_in_registered_CI"],
    "P6_instantaneous_rate_estimator": out["P6_wide_net"][
        "CORRECTED_estimator_instantaneous_rate"]["p_in_registered_CI"],
    "P6_first_order_cancels_exactly_in_wide_net": bool(
        out["P6_wide_net"]["exactness_second_order_only_max_rel_err"] < 1e-12),
    "P6_DECISIVE_tau_scaling": {
        "exponent": tau_slope, "registered": -2.0,
        "confirmed": out["P6_wide_net"]["DECISIVE_relaxation_time"]["in_CI"]},
    "P7_suff_err_vs_R": {
        "exponent": a_R, "breakdown_R_at_err_unity":
            out["P7_breakdown"]["R_at_which_err_reaches_unity"]},
}

print(json.dumps(out, indent=2, default=float))
with open("verdict.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
