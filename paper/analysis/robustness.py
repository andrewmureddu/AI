"""
Robustness numbers for the transfer-cliff paper.

The source experiments report seed-*means* only. A paper needs the spread, and
it needs to say plainly which statistic is load-bearing. Two checks:

  (1) Per-seed spread of the ladder-vs-transfer skills, and whether the L3-L2
      cliff is positive in EVERY seed (the claim is a step, not a correlation:
      Spearman over 4 levels has n=4 and cannot carry significance).
  (2) A permutation test for the real-data Leg A rank correlation (n=9
      features), which is the only leg with enough independent units to test.

Pure numpy + sklearn, deterministic. Mirrors the source runners exactly.
"""
import numpy as np, json, math, os
from sklearn.datasets import load_diabetes

OUT = os.path.dirname(os.path.abspath(__file__))
GRID = np.linspace(0.02, 0.98, 97)
N_INCR, M, SEEDS = 200, 4000, 8


def aggregate(f, r): return f((M, N_INCR), r).sum(axis=1)
def inc_uniform(s, r): return r.uniform(-1, 1, s)
def inc_exp(s, r): return r.exponential(1.0, s) - 1.0
def inc_skew(s, r):
    x = r.normal(0, 1, s) + (r.random(s) < 0.1) * r.normal(4.0, 1.0, s)
    return x - x.mean()
def inc_heavy(s, r): return r.standard_t(1.5, s)


def robust_shape(x):
    med = np.median(x); q1, q3 = np.percentile(x, [25, 75])
    return np.quantile((x - med) / (q3 - q1 + 1e-12), GRID)


def w1(a, b): return float(np.mean(np.abs(a - b)))


# ---- (1) per-seed ladder skills -------------------------------------------
cases = [("L4", lambda r: aggregate(inc_exp, r)),
         ("L3", lambda r: aggregate(inc_skew, r)),
         ("L2", lambda r: aggregate(inc_heavy, r)),
         ("L1", lambda r: r.standard_t(1.5, M))]
per_seed = {k: [] for k, _ in cases}
q_ref = robust_shape(np.random.default_rng(1).standard_t(1.5, 200000))
for s in range(SEEDS):
    r = np.random.default_rng(100 + s)
    qA = robust_shape(aggregate(inc_uniform, r))
    d_ref = w1(qA, q_ref)
    for name, gen in cases:
        per_seed[name].append(max(0.0, 1.0 - w1(qA, robust_shape(gen(r))) / d_ref))

skills = {k: np.array(v) for k, v in per_seed.items()}
gap = skills["L3"] - skills["L2"]
ladder = {k: {"mean": round(float(v.mean()), 3), "sd": round(float(v.std(ddof=1)), 3),
              "min": round(float(v.min()), 3), "max": round(float(v.max()), 3)}
          for k, v in skills.items()}
cliff = {"L3_minus_L2_mean": round(float(gap.mean()), 3),
         "L3_minus_L2_sd": round(float(gap.std(ddof=1)), 3),
         "L3_minus_L2_min": round(float(gap.min()), 3),
         "positive_in_all_seeds": bool((gap > 0).all()),
         "n_seeds": SEEDS,
         # separation in pooled-sd units; the two sides never overlap
         "seed_wise_overlap": bool(skills["L2"].max() >= skills["L3"].min())}

# adjacent-step decomposition: is the L2/L3 step uniquely large? (it is not)
step_12 = skills["L2"] - skills["L1"]
step_34 = skills["L4"] - skills["L3"]
diff = step_12 - gap                       # paired, same seeds
t_stat = float(diff.mean() / (diff.std(ddof=1) / np.sqrt(len(diff))))
steps = {"L1_to_L2": [round(float(step_12.mean()), 3), round(float(step_12.std(ddof=1)), 3)],
         "L2_to_L3": [round(float(gap.mean()), 3), round(float(gap.std(ddof=1)), 3)],
         "L3_to_L4": [round(float(step_34.mean()), 3), round(float(step_34.std(ddof=1)), 3)],
         "note": "[mean, sd] over seeds",
         "paired_diff_L1L2_minus_L2L3": round(float(diff.mean()), 3),
         "paired_t_df7": round(t_stat, 3),
         "steps_differ_significantly": bool(abs(t_stat) > 2.365)}   # t_.05,7 = 2.365

# ---- (2) permutation test for real-data Leg A ------------------------------
def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float); ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean(); ry -= ry.mean()
    return float((rx @ ry) / (math.sqrt(rx @ rx) * math.sqrt(ry @ ry) + 1e-12))


d = load_diabetes(); X, y, names = d.data, d.target, list(d.feature_names)
qs = np.quantile(X[:, 0], [0.25, 0.50, 0.75]); env = np.digitize(X[:, 0], qs)
def slope(xj, yy):
    A = np.column_stack([np.ones_like(xj), xj])
    w, *_ = np.linalg.lstsq(A, yy, rcond=None); return w

inv, tr = [], []
for j in [k for k in range(X.shape[1]) if names[k] != "age"]:
    sl = np.array([slope(X[env == e, j], y[env == e])[1] for e in range(4)])
    inv.append(1.0 / (1.0 + float(np.std(sl) / (abs(np.mean(sl)) + 1e-9))))
    sk = []
    for te in range(4):
        w = slope(X[env != te, j], y[env != te])
        yt = y[env == te]
        sk.append(1.0 - np.mean((w[0] + w[1] * X[env == te, j] - yt) ** 2) / np.var(yt))
    tr.append(float(np.mean(sk)))

rho_obs = spearman(inv, tr)
rng = np.random.default_rng(0)
null = np.array([spearman(inv, rng.permutation(tr)) for _ in range(200000)])
p_two = float((np.abs(null) >= abs(rho_obs) - 1e-12).mean())
legA = {"n_features": len(inv), "rho": round(rho_obs, 3),
        "permutation_p_two_sided": p_two,
        "n_permutations": int(null.size),
        "exact_min_p_for_n9_two_sided": round(2 / math.factorial(9), 8)}

res = {"ladder_per_seed_skill": ladder, "ladder_cliff": cliff,
       "ladder_adjacent_steps": steps, "real_legA_permutation": legA}
with open(os.path.join(OUT, "robustness.json"), "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))


# ---- (3) self-transfer baseline: what IS the metric's ceiling? --------------
# The paper claims L3/L4 saturate at the metric's finite-sample ceiling rather
# than at a real transfer deficit. That is testable directly: score domain A
# against an INDEPENDENT draw of domain A itself. Any shortfall from 1.0 is pure
# estimation noise in the quantile comparison, since the law is identical.
def self_skill(n_incr, seed_a, seed_b):
    ra, rb = np.random.default_rng(seed_a), np.random.default_rng(seed_b)
    qa = robust_shape(ra.uniform(-1, 1, (M, n_incr)).sum(axis=1))
    qb = robust_shape(rb.uniform(-1, 1, (M, n_incr)).sum(axis=1))
    return max(0.0, 1.0 - w1(qa, qb) / w1(qa, q_ref))

base = {}
for n_incr in (200, 1024):
    vals = np.array([self_skill(n_incr, 100 + s, 900 + s) for s in range(SEEDS)])
    base[f"n={n_incr}"] = {"mean": round(float(vals.mean()), 3),
                           "sd": round(float(vals.std(ddof=1)), 3),
                           "min": round(float(vals.min()), 3)}
res["metric_ceiling_self_transfer"] = base
with open(os.path.join(OUT, "robustness.json"), "w") as f:
    json.dump(res, f, indent=2)
print("\nmetric ceiling (A vs independent A):", json.dumps(base, indent=2))
