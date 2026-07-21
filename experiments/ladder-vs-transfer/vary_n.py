"""
Follow-up to run.py: how does transfer skill scale with n, the number of
contributions per aggregate?

Prediction (generalized CLT): finite-variance levels (L3/L4) converge to Gaussian,
so skill → 1 as n grows; the infinite-variance level (L2) converges to an α-stable
law (α=1.5) that is *permanently* non-Gaussian, so its skill stays bounded away
from 1. Therefore the L2/L3 cliff should WIDEN with n. We also test the specific
earlier conjecture that L2 skill *falls* with n (vs. merely plateauing) — reported
honestly either way. L1 (a single heavy draw, no aggregation) is n-independent by
construction — the control.

Metric matches run.py: robustly-standardized shape distance (1-D Wasserstein over
the [0.02,0.98] quantile band) to the Gaussian invariant; skill = 1 − d/d_ref.
Pure numpy, deterministic.
"""
import numpy as np, json, os, csv as _csv

OUT = os.path.dirname(os.path.abspath(__file__))
M = 3000
SEEDS = 6
GRID = np.linspace(0.02, 0.98, 97)
NS = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


def robust_shape(x):
    med = np.median(x)
    q1, q3 = np.percentile(x, [25, 75])
    return np.quantile((x - med) / (q3 - q1 + 1e-12), GRID)


def w1(a, b):
    return float(np.mean(np.abs(a - b)))


def inc_exp(shape, r):  return r.exponential(1.0, shape) - 1.0
def inc_skew(shape, r):
    x = r.normal(0, 1, shape) + (r.random(shape) < 0.1) * r.normal(4.0, 1.0, shape)
    return x - x.mean()
def inc_heavy(shape, r): return r.standard_t(1.5, shape)

levels = {"L4": inc_exp, "L3": inc_skew, "L2": inc_heavy}

# Gaussian invariant reference shape + normalization scale
ref_gauss = robust_shape(np.random.default_rng(0).normal(0, 1, 400000))
d_ref = w1(ref_gauss, robust_shape(np.random.default_rng(1).standard_t(1.5, 400000)))

skill = {L: [] for L in ["L4", "L3", "L2", "L1"]}
for n in NS:
    acc = {L: [] for L in levels}
    l1 = []
    for s in range(SEEDS):
        r = np.random.default_rng(1000 + s + n)
        for L, fn in levels.items():
            agg = fn((M, n), r).sum(axis=1)
            acc[L].append(max(0.0, 1.0 - w1(robust_shape(agg), ref_gauss) / d_ref))
        l1.append(max(0.0, 1.0 - w1(robust_shape(r.standard_t(1.5, M)), ref_gauss) / d_ref))
    for L in levels:
        skill[L].append(float(np.mean(acc[L])))
    skill["L1"].append(float(np.mean(l1)))

gap = [skill["L3"][i] - skill["L2"][i] for i in range(len(NS))]   # cliff height
verdict = {
    "n_values": NS,
    "skill_L4": [round(v, 3) for v in skill["L4"]],
    "skill_L3": [round(v, 3) for v in skill["L3"]],
    "skill_L2": [round(v, 3) for v in skill["L2"]],
    "skill_L1": [round(v, 3) for v in skill["L1"]],
    "cliff_L3_minus_L2": [round(v, 3) for v in gap],
    "L3L4_rise_with_n": bool(skill["L3"][-1] > skill["L3"][0] and skill["L4"][-1] > skill["L4"][0]),
    "L2_falls_with_n": bool(skill["L2"][-1] < skill["L2"][0]),
    "cliff_widens_with_n": bool(gap[-1] > gap[0]),
}
with open(os.path.join(OUT, "vary_n.csv"), "w", newline="") as f:
    w = _csv.writer(f); w.writerow(["n", "skill_L1", "skill_L2", "skill_L3", "skill_L4", "cliff_L3_minus_L2"])
    for i, n in enumerate(NS):
        w.writerow([n, skill["L1"][i], skill["L2"][i], skill["L3"][i], skill["L4"][i], gap[i]])
with open(os.path.join(OUT, "vary_n_verdict.json"), "w") as f:
    json.dump(verdict, f, indent=2)

print("transfer skill vs n  (rows: n; L1 L2 L3 L4 | cliff=L3−L2)")
print("-" * 60)
for i, n in enumerate(NS):
    print(f"  n={n:>4}   {skill['L1'][i]:.2f}  {skill['L2'][i]:.2f}  "
          f"{skill['L3'][i]:.2f}  {skill['L4'][i]:.2f}   | cliff {gap[i]:.2f}")
print("-" * 60)
print("L3/L4 rise with n:", verdict["L3L4_rise_with_n"],
      "| L2 falls with n:", verdict["L2_falls_with_n"],
      "| cliff widens:", verdict["cliff_widens_with_n"])
