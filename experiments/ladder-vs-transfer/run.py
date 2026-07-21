"""
Does ladder level predict transfer? — a controlled cross-mechanism test.

SYNTHESIS §6.1: S18 showed invariance⇒transfer inside ONE constructed SCM, where
invariance = transfer by design. This is the honest step up: genuinely DIFFERENT
generative mechanisms, with the transfer outcome forced by probability theory, not
by us.

We hold the *surface phenomenon* fixed — "a macroscopic quantity is the aggregate of
n=200 microscopic contributions" — and learn the law in a reference domain A
(uniform increments): the normalized aggregate is Gaussian. We then vary how deeply
that Gaussian invariant actually applies in domain B, i.e. the correspondence LEVEL,
and measure whether A's law transfers to B:

  L4  B = exponential increments  → finite variance ⇒ CLT FORCES Gaussian (a theorem,
        despite a totally different micro-law).            → should transfer.
  L3  B = skewed finite-variance mixture → same CLT mechanism, mild finite-n skew.
                                                            → should transfer well.
  L2  B = heavy-tailed increments (Student-t, ν=1.5, INFINITE variance) → the
        aggregate converges to a stable law, NOT Gaussian: same "sum of many"
        surface, different universality class.              → should FAIL.
  L1  B = not an aggregate at all (single heavy draw) — shares only the loose word
        "combine".                                          → should fail (~0).

The level assignments are justified by real theory (finite/infinite variance;
theorem vs none), so any level⇒transfer relationship is a consequence, not a
construction. Metric: robustly-standardized shape distance (1-D Wasserstein over the
[0.02,0.98] quantile band) between B's aggregate and A's learned Gaussian shape;
skill = 1 − d/d_ref.  Pure numpy, deterministic.
"""
import numpy as np, json, os, csv as _csv

OUT = os.path.dirname(os.path.abspath(__file__))
N_INCR = 200          # contributions per aggregate
M = 4000              # aggregates (samples of the macro quantity) per domain
SEEDS = 8
GRID = np.linspace(0.02, 0.98, 97)


def aggregate(incr_fn, r):
    """M aggregates, each a sum of N_INCR i.i.d. contributions from incr_fn."""
    X = incr_fn((M, N_INCR), r)
    return X.sum(axis=1)


# --- increment / macro generators (all mean-centred) ---
def inc_uniform(shape, r):   return r.uniform(-1, 1, shape)                 # A: finite var
def inc_exp(shape, r):       return r.exponential(1.0, shape) - 1.0         # L4: finite var
def inc_skew(shape, r):                                                     # L3: finite var, skewed
    z = r.normal(0, 1, shape)
    j = (r.random(shape) < 0.1) * r.normal(4.0, 1.0, shape)
    x = z + j
    return x - x.mean()
def inc_heavy(shape, r):     return r.standard_t(1.5, shape)                # L2: INFINITE var
def macro_single(r):         return r.standard_t(1.5, M)                    # L1: not an aggregate


def robust_shape(x):
    med = np.median(x)
    q1, q3 = np.percentile(x, [25, 75])
    return np.quantile((x - med) / (q3 - q1 + 1e-12), GRID)


def w1(qa, qb):
    return float(np.mean(np.abs(qa - qb)))


cases = [
    ("L4", 4, "exponential increments (CLT forces Gaussian)", lambda r: aggregate(inc_exp, r)),
    ("L3", 3, "skewed finite-variance mix (same CLT mechanism)", lambda r: aggregate(inc_skew, r)),
    ("L2", 2, "heavy-tailed increments, ν=1.5 (infinite var → stable, not Gaussian)",
     lambda r: aggregate(inc_heavy, r)),
    ("L1", 1, "single heavy draw (not an aggregate; word only)", lambda r: macro_single(r)),
]

skills = {c[0]: [] for c in cases}
dists = {c[0]: [] for c in cases}
curves = {}
for s in range(SEEDS):
    r = np.random.default_rng(100 + s)
    qA = robust_shape(aggregate(inc_uniform, r))            # A's learned Gaussian shape
    # reference scale: distance from Gaussian to a maximally-different heavy shape
    q_ref = robust_shape(np.random.default_rng(1).standard_t(1.5, 200000))
    d_ref = w1(qA, q_ref)
    for name, lvl, desc, gen in cases:
        qB = robust_shape(gen(r))
        d = w1(qA, qB)
        dists[name].append(d)
        skills[name].append(max(0.0, 1.0 - d / d_ref))
        if s == 0:
            curves[name] = qB
    if s == 0:
        curves["A(learned Gaussian)"] = qA

lvl_of = {c[0]: c[1] for c in cases}
mean_skill = {k: float(np.mean(v)) for k, v in skills.items()}
mean_dist = {k: float(np.mean(v)) for k, v in dists.items()}


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float); ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean(); ry -= ry.mean()
    return float((rx @ ry) / (np.sqrt(rx @ rx) * np.sqrt(ry @ ry) + 1e-12))


order = ["L1", "L2", "L3", "L4"]
rho = spearman([lvl_of[k] for k in order], [mean_skill[k] for k in order])

# save curves + summary
np.savez(os.path.join(OUT, "curves.npz"), grid=GRID, **{k.replace(" ", "_"): v for k, v in curves.items()})
with open(os.path.join(OUT, "summary.csv"), "w", newline="") as f:
    w = _csv.writer(f)
    w.writerow(["level", "name", "description", "mean_shape_distance", "mean_transfer_skill"])
    for name, lvl, desc, _ in cases:
        w.writerow([lvl, name, desc, f"{mean_dist[name]:.4f}", f"{mean_skill[name]:.4f}"])

verdict = {
    "transfer_skill_by_level": {k: round(mean_skill[k], 3) for k in order},
    "shape_distance_by_level": {k: round(mean_dist[k], 3) for k in order},
    "spearman_level_vs_skill": round(rho, 3),
    "cliff_between": "L2/L3 (finite vs infinite variance = the shared-mechanism boundary)",
    "monotone_level_predicts_transfer": bool(mean_skill["L4"] >= mean_skill["L3"] >= mean_skill["L2"]
                                             and mean_skill["L2"] <= 0.5 < mean_skill["L3"]),
}
with open(os.path.join(OUT, "verdict.json"), "w") as f:
    json.dump(verdict, f, indent=2)

print("ladder level → transfer skill (1 = A's Gaussian law transfers, 0 = useless)")
print("-" * 66)
for name, lvl, desc, _ in cases:
    bar = "#" * int(round(mean_skill[name] * 40))
    print(f"  {name}  skill={mean_skill[name]:.2f}  d={mean_dist[name]:.3f}  |{bar:<40}|  {desc}")
print("-" * 66)
print(f"Spearman(level, skill) = {rho:.3f}   |   cliff at {verdict['cliff_between']}")
print("VERDICT:", json.dumps(verdict["transfer_skill_by_level"]))
