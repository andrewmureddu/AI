"""
D11 -- the residue reconciled: one structure, three descriptions.

Tests whether D7/D8's projective/Grassmannian residue, D10's composition-
pinning criterion, and D3-ladder-invariance's "fixed point of the description
map, ratio as eigenvalue" reconcile as one structure (a description map's
linearization at a fixed point).

C2 (identity, proved in the derivation): for the dyadic renormalized-sum map
T: law(X) -> law((X_1+X_2)/sqrt(2)), any scale mixture X = U*Z (U > 0 indep
of Z ~ N(0,1)) is an exact fixed point, with scale eigenvalue H = 1/2 for
every n and every law of U.

C3 (at risk): the log-log regression estimator this repo already uses,
applied to EXACT quantiles (root-finding on the closed-form mixture CDF, no
Monte Carlo), recovers H = 0.5 to near machine precision.

C4 (at risk, the falsifiable core): a scale-invariant shape statistic varies
substantially across the same U-mixture family while H stays flat -- the
same phenomenon D3-ladder-invariance found by accident (with MC noise), now
targeted in advance and computed exactly.

Deterministic. No random sampling: every quantity is either a closed-form
formula or a root-find on one. Pure numpy + scipy.
"""

import json
import time

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

T0 = time.time()

# ---------------------------------------------------------------------------
# Exact quantiles of S_n = U * (Z_1 + ... + Z_n), U a two-point mixture
# {u1 w.p. p, u2 w.p. 1-p}, independent of iid Z_i ~ N(0,1).
#
# S_n | U=u  ~  N(0, n * u^2),   so
#   CDF_{S_n}(x) = p * Phi(x / (u1*sqrt(n))) + (1-p) * Phi(x / (u2*sqrt(n)))
# ---------------------------------------------------------------------------


def mixture_cdf(x, n, u1, u2, p):
    sqn = np.sqrt(n)
    return p * norm.cdf(x / (u1 * sqn)) + (1 - p) * norm.cdf(x / (u2 * sqn))


def mixture_quantile(q, n, u1, u2, p, bracket=None):
    """Exact quantile via root-finding on the closed-form mixture CDF."""
    if bracket is None:
        # generous bracket: scale grows like sqrt(n)*max(u1,u2)
        scale = np.sqrt(n) * max(u1, u2)
        bracket = (-50 * scale - 10, 50 * scale + 10)
    lo, hi = bracket
    f = lambda x: mixture_cdf(x, n, u1, u2, p) - q
    return brentq(f, lo, hi, xtol=1e-13, rtol=1e-14, maxiter=200)


def scale_stat(n, u1, u2, p, q_lo, q_hi):
    """Quantile spread Q_{q_hi} - Q_{q_lo} of S_n, exact."""
    lo = mixture_quantile(q_lo, n, u1, u2, p)
    hi = mixture_quantile(q_hi, n, u1, u2, p)
    return hi - lo


def log_log_slope(ns, ys):
    """Least-squares slope of ln(ys) vs ln(ns); returns (slope, r2)."""
    x = np.log(ns)
    y = np.log(ys)
    A = np.vstack([x, np.ones_like(x)]).T
    coef, res, _, _ = np.linalg.lstsq(A, y, rcond=None)
    slope, intercept = coef
    yhat = A @ coef
    ss_res = np.sum((y - yhat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return float(slope), float(r2)


# ---------------------------------------------------------------------------
# Registered mixture configurations: U in {u1, u2} w.p. {p, 1-p}
# ---------------------------------------------------------------------------

CONFIGS = [
    {"name": "config0_gaussian", "u1": 1.0, "u2": 1.0, "p": 1.0},
    {"name": "config1_mild", "u1": 1.0, "u2": 2.0, "p": 0.5},
    {"name": "config2_strong", "u1": 1.0, "u2": 5.0, "p": 0.5},
    {"name": "config3_rare_extreme", "u1": 1.0, "u2": 10.0, "p": 0.9},
    {"name": "config4_asymmetric", "u1": 0.5, "u2": 3.0, "p": 0.3},
]

N_GRID = np.logspace(1, 4, 20)  # n in [10, 10000], 20 log-spaced points

print("D11 -- residue reconciliation")
print("=" * 70)

# ---------------------------------------------------------------------------
# P1/P2 (C3): H_IQR and H_1090 for each config, via exact quantiles.
# ---------------------------------------------------------------------------

results = {}
p1_pass = True
p2_pass = True

print("\nP1/P2 -- exact log-log regression H for two observables, 5 configs")
print("-" * 70)
for cfg in CONFIGS:
    u1, u2, p = cfg["u1"], cfg["u2"], cfg["p"]

    iqr_vals = np.array([scale_stat(n, u1, u2, p, 0.25, 0.75) for n in N_GRID])
    r1090_vals = np.array([scale_stat(n, u1, u2, p, 0.10, 0.90) for n in N_GRID])

    H_iqr, r2_iqr = log_log_slope(N_GRID, iqr_vals)
    H_1090, r2_1090 = log_log_slope(N_GRID, r1090_vals)

    dev_iqr = abs(H_iqr - 0.5)
    dev_1090 = abs(H_1090 - 0.5)
    ray_gap = abs(H_iqr - H_1090)

    p1_ok = dev_iqr < 1e-6 and dev_1090 < 1e-6 and r2_iqr > 1 - 1e-10 and r2_1090 > 1 - 1e-10
    p2_ok = ray_gap < 1e-6
    p1_pass &= p1_ok
    p2_pass &= p2_ok

    results[cfg["name"]] = {
        "u1": u1, "u2": u2, "p": p,
        "H_iqr": H_iqr, "r2_iqr": r2_iqr,
        "H_1090": H_1090, "r2_1090": r2_1090,
        "dev_iqr": dev_iqr, "dev_1090": dev_1090, "ray_gap": ray_gap,
        "P1_ok": p1_ok, "P2_ok": p2_ok,
    }

    print(f"  {cfg['name']:22s}  H_iqr={H_iqr:.9f} (dev {dev_iqr:.2e}, R2 dev {1-r2_iqr:.2e})"
          f"  H_1090={H_1090:.9f} (dev {dev_1090:.2e})  ray_gap={ray_gap:.2e}")

print(f"\nP1 (H within 1e-6 of 0.5, both observables, all configs): {'PASS' if p1_pass else 'FAIL'}")
print(f"P2 (ray [H_iqr:H_1090] = [1:1] within 1e-6, all configs):  {'PASS' if p2_pass else 'FAIL'}")

# ---------------------------------------------------------------------------
# P3/P4 (C4): scale-invariant shape ratio SR(n) = (Q97.5-Q2.5)/(Q75-Q25)
# ---------------------------------------------------------------------------

print("\nP3/P4 -- shape ratio SR(n) = (Q97.5-Q2.5)/(Q75-Q25): varies vs n-invariant")
print("-" * 70)

SR_at_100 = {}
sr_tangent_pass = True
for cfg in CONFIGS:
    u1, u2, p = cfg["u1"], cfg["u2"], cfg["p"]

    def SR(n):
        wide = scale_stat(n, u1, u2, p, 0.025, 0.975)
        iqr = scale_stat(n, u1, u2, p, 0.25, 0.75)
        return wide / iqr

    sr_100 = SR(100)
    sr_10 = SR(10)
    sr_10000 = SR(10000)
    tangent_dev = abs(sr_10 - sr_10000)
    tangent_ok = tangent_dev < 1e-6
    sr_tangent_pass &= tangent_ok

    SR_at_100[cfg["name"]] = sr_100
    results[cfg["name"]]["SR_100"] = sr_100
    results[cfg["name"]]["SR_10"] = sr_10
    results[cfg["name"]]["SR_10000"] = sr_10000
    results[cfg["name"]]["SR_tangent_dev"] = tangent_dev
    results[cfg["name"]]["P4_ok"] = tangent_ok

    print(f"  {cfg['name']:22s}  SR(n=10)={sr_10:.9f}  SR(n=100)={sr_100:.9f}"
          f"  SR(n=10000)={sr_10000:.9f}  |SR(10)-SR(10000)|={tangent_dev:.2e}")

sr_values = np.array(list(SR_at_100.values()))
sr_spread = sr_values.max() / sr_values.min() - 1
p3_pass = sr_spread >= 0.15

print(f"\nSR(n=100) across configs: min={sr_values.min():.6f} max={sr_values.max():.6f}"
      f"  spread(max/min - 1)={sr_spread:.4f}")
print(f"P3 (SR spread >= 0.15 across configs, H flat throughout): {'PASS' if (p3_pass and p1_pass) else 'FAIL'}")
print(f"P4 (SR exactly n-invariant, |SR(10)-SR(10000)| < 1e-6):    {'PASS' if sr_tangent_pass else 'FAIL'}")

# ---------------------------------------------------------------------------
# Post-hoc diagnostic (not registered): compare to the earlier MC-noise
# version of this same finding (D3-ladder-invariance), for context only.
# ---------------------------------------------------------------------------

print("\n--- post-hoc diagnostic (not registered) ---")
print("Earlier D3-ladder-invariance run measured H in [0.4923, 0.4951] via Monte")
print("Carlo sampling (finite aggregates, seeded RNG). This run's exact H values:")
for cfg in CONFIGS:
    r = results[cfg["name"]]
    print(f"  {cfg['name']:22s}  H_iqr={r['H_iqr']:.9f}")
print("consistent with the MC estimates being noisy measurements of the same")
print("exact 1/2, not evidence of a different true value.")

# ---------------------------------------------------------------------------
# Verdict assembly
# ---------------------------------------------------------------------------

verdict = {
    "stone": "D11",
    "P1_exact_H_within_1e-6_of_half": bool(p1_pass),
    "P2_ray_degenerate_within_1e-6": bool(p2_pass),
    "P3_shape_ratio_spread_geq_0.15": bool(p3_pass),
    "P4_shape_ratio_exactly_n_invariant": bool(sr_tangent_pass),
    "n_grid_min": float(N_GRID.min()),
    "n_grid_max": float(N_GRID.max()),
    "n_grid_points": int(len(N_GRID)),
    "configs": results,
    "runtime_s": round(time.time() - T0, 1),
}

with open("verdict.json", "w") as f:
    json.dump(verdict, f, indent=2)

print("\n" + "=" * 70)
print("--- summary ---")
print(f"P1 (exact H = 0.5 to 1e-6, 2 observables x 5 configs): {'PASS' if p1_pass else 'FAIL'}")
print(f"P2 (ray degenerate to 1e-6, 5 configs):                {'PASS' if p2_pass else 'FAIL'}")
print(f"P3 (shape ratio spread >= 15% across configs):         {'PASS' if p3_pass else 'FAIL'}")
print(f"P4 (shape ratio exactly n-invariant, all configs):     {'PASS' if sr_tangent_pass else 'FAIL'}")
print(f"\nwritten verdict.json  (runtime {verdict['runtime_s']}s)")
