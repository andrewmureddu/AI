"""
D3 — is transfer a chart-invariance count?

Tests the claim registered in PREREGISTRATION.md: if D1/D2 are right, a
correspondence transfers *iff* it is chart-invariant, and the ladder is a count of
quotiented coordinate choices rather than a scale of epistemic quality.

The chart-invariance measurement is the **aggregation chart order**

    H(D) = d ln s(n) / d ln n,      s(n) = IQR of the n-aggregate,

log-response over log-rescaling (FLOORS.md §4's signature), measured inside one
domain with no reference to any other domain's samples. By D2's rule the bare H is
gauge and the ratio r = H_B/H_A is the invariant; mismatch m = |r - 1|.

Legs (see PREREGISTRATION.md for the registered numbers):
  P1  H for A and each ladder rung.
  P2  gauge check: H -> a*H under phi_a(x) = sign(x)|x|^a; r invariant.
  P3  does m predict the archival transfer skills better than the rung label?
  P4  the decoupling sweep: a chart-invariant family (common-factor increments,
      H = 1/2 at every mixing strength) whose transfer skill is swept continuously.
  P5  re-chart intervention on the L4 rung: B-only vs common-a.

Metric and generators are copied verbatim from ../ladder-vs-transfer/run.py so the
skills are comparable to the archival numbers. Pure numpy, deterministic.
"""
import numpy as np, json, os, csv as _csv

OUT = os.path.dirname(os.path.abspath(__file__))

# --- harness constants, identical to ladder-vs-transfer -----------------------
N_INCR = 200
M = 4000
SEEDS = 8
GRID = np.linspace(0.02, 0.98, 97)

# --- H-fit constants ---------------------------------------------------------
N_MAX = 4096                                  # 2^12
N_GRID = 2 ** np.arange(4, 13)                # 2^4 .. 2^12
M_H = 4000
SEEDS_H = 3
CHART_A = [0.5, 1.0, 1.5, 2.0, 3.0]


# ---------------------------------------------------------------- generators --
def inc_uniform(shape, r):   return r.uniform(-1, 1, shape)
def inc_exp(shape, r):       return r.exponential(1.0, shape) - 1.0
def inc_skew(shape, r):
    z = r.normal(0, 1, shape)
    j = (r.random(shape) < 0.1) * r.normal(4.0, 1.0, shape)
    x = z + j
    return x - x.mean()
def inc_heavy(shape, r):     return r.standard_t(1.5, shape)


def inc_common_factor(c):
    """X_i = U * z_i, z i.i.d. N(0,1), U lognormal with coefficient of variation c,
    drawn once per aggregate (shared across the row => exchangeable, not i.i.d.)."""
    sig = np.sqrt(np.log1p(c * c))

    def f(shape, r):
        rows = shape[0]
        z = r.normal(0, 1, shape)
        U = np.exp(sig * r.normal(0, 1, (rows, 1)) - 0.5 * sig * sig)
        return U * z
    return f


def aggregate(incr_fn, r, n=N_INCR, m=M):
    return incr_fn((m, n), r).sum(axis=1)


def macro_single(r, m=M):    return r.standard_t(1.5, m)


# -------------------------------------------------------------------- metric --
def robust_shape(x):
    med = np.median(x)
    q1, q3 = np.percentile(x, [25, 75])
    return np.quantile((x - med) / (q3 - q1 + 1e-12), GRID)


def w1(qa, qb):
    return float(np.mean(np.abs(qa - qb)))


def chart(x, a):
    """phi_a(x) = sign(x)|x|^a — the power re-charting of D1/D2, applied to the
    macro observable. a = 1 is the identity."""
    return x if a == 1.0 else np.sign(x) * np.abs(x) ** a


def iqr(x):
    q1, q3 = np.percentile(x, [25, 75])
    return float(q3 - q1)


# ------------------------------------------------- P1/P2: aggregation order H --
def fit_H(incr_fn, seed, a=1.0, single=False):
    """Slope of ln IQR(n-aggregate) against ln n. Nested partial sums: one draw of
    (M_H, N_MAX) increments, cumulative-summed at the n grid."""
    r = np.random.default_rng(seed)
    if single:                                       # L1: no aggregation at all
        s = [iqr(chart(macro_single(r, M_H), a)) for _ in N_GRID]
    else:
        X = incr_fn((M_H, N_MAX), r)
        cs = np.cumsum(X, axis=1)
        s = [iqr(chart(cs[:, n - 1], a)) for n in N_GRID]
    return float(np.polyfit(np.log(N_GRID), np.log(np.array(s)), 1)[0])


def H_of(incr_fn, a=1.0, single=False):
    v = [fit_H(incr_fn, 700 + s, a=a, single=single) for s in range(SEEDS_H)]
    return float(np.mean(v)), float(np.std(v))


DOMAINS = [
    ("A",  None, inc_uniform, False, "uniform increments (reference domain)"),
    ("L4", 4, inc_exp,   False, "exponential increments (CLT forces Gaussian)"),
    ("L3", 3, inc_skew,  False, "skewed finite-variance mixture (same CLT mechanism)"),
    ("L2", 2, inc_heavy, False, "Student-t nu=1.5 (infinite variance -> stable law)"),
    ("L1", 1, None,      True,  "single heavy draw (not an aggregate)"),
]

H1 = {}
for name, lvl, fn, single, desc in DOMAINS:
    h, sd = H_of(fn, single=single)
    H1[name] = {"H": h, "sd": sd, "level": lvl, "desc": desc}

HA = H1["A"]["H"]
for name in H1:
    H1[name]["r"] = H1[name]["H"] / HA
    H1[name]["m"] = abs(H1[name]["r"] - 1.0)

# P2 — gauge behaviour of H, invariance of the ratio
P2 = []
for a in CHART_A:
    hA = H_of(inc_uniform, a=a)[0]
    hB = H_of(inc_heavy, a=a)[0]          # the rung whose H differs from A's
    P2.append({
        "a": a,
        "H_A": hA, "H_A_over_a": hA / a,
        "H_L2": hB, "H_L2_over_a": hB / a,
        "r_L2": hB / hA,
    })
r_span = max(p["r_L2"] for p in P2) - min(p["r_L2"] for p in P2)
H_span = max(p["H_A"] for p in P2) / min(p["H_A"] for p in P2)

# ------------------------------------------------- P3: skills, and the ceiling --
CASES = [
    ("L4", 4, lambda r: aggregate(inc_exp, r)),
    ("L3", 3, lambda r: aggregate(inc_skew, r)),
    ("L2", 2, lambda r: aggregate(inc_heavy, r)),
    ("L1", 1, lambda r: macro_single(r)),
]


def skill_of(gen, a_B=1.0, a_A=1.0, seeds=SEEDS):
    """Transfer skill of A's learned Gaussian shape onto domain B. a_A / a_B are the
    charts the two macro observables are read in; the reference scale is read in A's
    chart, since it calibrates A's law."""
    sk, ds = [], []
    for s in range(seeds):
        r = np.random.default_rng(100 + s)
        qA = robust_shape(chart(aggregate(inc_uniform, r), a_A))
        q_ref = robust_shape(chart(np.random.default_rng(1).standard_t(1.5, 200000), a_A))
        d_ref = w1(qA, q_ref)
        d = w1(qA, robust_shape(chart(gen(r), a_B)))
        ds.append(d)
        sk.append(max(0.0, 1.0 - d / d_ref))
    return float(np.mean(sk)), float(np.std(sk)), float(np.mean(ds))


def ceiling_distance(a=1.0, seeds=SEEDS):
    """A scored against an independent draw of A itself, read in chart a. This is the
    chart's own irreducible sampling floor: the smallest distance any domain can
    achieve in that chart."""
    ds = []
    for s in range(seeds):
        q1 = robust_shape(chart(aggregate(inc_uniform, np.random.default_rng(100 + s)), a))
        q2 = robust_shape(chart(aggregate(inc_uniform, np.random.default_rng(500 + s)), a))
        ds.append(w1(q1, q2))
    return float(np.mean(ds))


skills = {}
for name, lvl, gen in CASES:
    mu, sd, d = skill_of(gen)
    skills[name] = {"skill": mu, "sd": sd, "d": d, "level": lvl}

# ceiling: A scored against an independent draw of A itself
ceil = []
for s in range(SEEDS):
    r1 = np.random.default_rng(100 + s)
    r2 = np.random.default_rng(500 + s)
    qA = robust_shape(aggregate(inc_uniform, r1))
    q_ref = robust_shape(np.random.default_rng(1).standard_t(1.5, 200000))
    ceil.append(max(0.0, 1.0 - w1(qA, robust_shape(aggregate(inc_uniform, r2))) / w1(qA, q_ref)))
CEILING = float(np.mean(ceil))


def r2_of(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    b, a0 = np.polyfit(x, y, 1)
    yh = b * x + a0
    ss = float(np.sum((y - yh) ** 2)); tt = float(np.sum((y - y.mean()) ** 2))
    return 1.0 - ss / tt


order = ["L1", "L2", "L3", "L4"]
sk_vec = [skills[k]["skill"] for k in order]
m_vec = [H1[k]["m"] for k in order]
lvl_vec = [float(H1[k]["level"]) for k in order]
P3 = {
    "R2_skill_vs_mismatch": r2_of(m_vec, sk_vec),
    "R2_skill_vs_level": r2_of(lvl_vec, sk_vec),
    "mismatch_ties_L3_L4": bool(abs(H1["L3"]["m"] - H1["L4"]["m"]) < 0.02),
    "label_predicts_L4_above_L3": True,
    "skill_L4_minus_L3": skills["L4"]["skill"] - skills["L3"]["skill"],
}

# --------------------------------------------------------- P4: the decoupling --
CVS = [0.0, 0.25, 0.5, 1.0, 2.0]
P4 = []
for c in CVS:
    fn = inc_common_factor(c)
    h, hsd = H_of(fn)
    mu, sd, d = skill_of(lambda r, f=fn: aggregate(f, r))
    # fixed point of aggregation? standardized shape at n = 64 vs n = 1024
    r = np.random.default_rng(4242)
    q64 = robust_shape(aggregate(fn, r, n=64, m=20000))
    q1024 = robust_shape(aggregate(fn, r, n=1024, m=20000))
    qG = robust_shape(np.random.default_rng(7).normal(0, 1, 200000))
    P4.append({
        "cv": c, "H": h, "H_sd": hsd, "r": h / HA, "m": abs(h / HA - 1.0),
        "skill": mu, "skill_sd": sd, "d": d,
        "self_distance_n64_n1024": w1(q64, q1024),
        "d_to_gaussian_n64": w1(q64, qG), "d_to_gaussian_n1024": w1(q1024, qG),
    })

# the same fixed-point diagnostic on the archival rungs, for comparison
FP = {}
for nm, fn in [("L4", inc_exp), ("L3", inc_skew), ("L2", inc_heavy)]:
    r = np.random.default_rng(4242)
    q64 = robust_shape(aggregate(fn, r, n=64, m=20000))
    q1024 = robust_shape(aggregate(fn, r, n=1024, m=20000))
    qG = robust_shape(np.random.default_rng(7).normal(0, 1, 200000))
    FP[nm] = {"self_distance_n64_n1024": w1(q64, q1024),
              "d_to_gaussian_n64": w1(q64, qG), "d_to_gaussian_n1024": w1(q1024, qG)}

# ------------------------------------------------ P5: the re-chart intervention --
P5 = []
for a in CHART_A:
    b_only = skill_of(lambda r: aggregate(inc_exp, r), a_B=a, a_A=1.0)
    common = skill_of(lambda r: aggregate(inc_exp, r), a_B=a, a_A=a)
    P5.append({"a": a,
               "skill_B_only": b_only[0], "d_B_only": b_only[2],
               "skill_common_a": common[0], "d_common_a": common[2],
               "m_B_only": abs(a - 1.0), "m_common_a": 0.0})
base_common = [p for p in P5 if p["a"] == 1.0][0]["skill_common_a"]
common_dev = max(abs(p["skill_common_a"] - base_common) for p in P5)
b_only_worst = min(p["skill_B_only"] for p in P5 if p["a"] != 1.0)

# P5b (POST-HOC, not registered) — skill's normalizer is itself chart-dependent, so
# P5's registered threshold may be measuring the metric rather than the claim.
# Re-normalize every distance by the *same chart's* sampling floor (A vs A).
for p in P5:
    dc = ceiling_distance(a=p["a"])
    p["d_ceiling_in_chart"] = dc
    p["ratio_common_a"] = p["d_common_a"] / dc
    p["ratio_B_only"] = p["d_B_only"] / dc
common_ratio_span = (max(p["ratio_common_a"] for p in P5),
                     min(p["ratio_common_a"] for p in P5))
b_only_ratio_worst = max(p["ratio_B_only"] for p in P5 if p["a"] != 1.0)

# Bookkeeping check: the archival L2 skill (0.484) rests on 8 seeds, and this run's
# independent-stream version read 0.537. Which is it?
L2_32 = skill_of(lambda r: aggregate(inc_heavy, r), seeds=32)

# ------------------------------------------------------------------- verdicts --
verdict = {
    "P1_aggregation_chart_order": {k: {"H": round(v["H"], 4), "sd": round(v["sd"], 4),
                                       "r": round(v["r"], 4), "m": round(v["m"], 4)}
                                   for k, v in H1.items()},
    "P1_holds": bool(abs(H1["A"]["H"] - 0.5) < 0.03 and abs(H1["L4"]["H"] - 0.5) < 0.03
                     and abs(H1["L3"]["H"] - 0.5) < 0.03
                     and abs(H1["L2"]["H"] - 2.0 / 3.0) < 0.05
                     and abs(H1["L1"]["H"]) < 0.03),
    "P2_gauge": P2,
    "P2_holds": bool(r_span < 1e-6 and H_span > 5.0),
    "P2_ratio_span": r_span, "P2_H_A_span_factor": H_span,
    "P3": P3,
    "P3_holds": bool(P3["R2_skill_vs_mismatch"] > P3["R2_skill_vs_level"] + 0.10
                     and P3["mismatch_ties_L3_L4"]),
    "archival_skills": {k: round(v["skill"], 3) for k, v in skills.items()},
    "ceiling_A_vs_A": round(CEILING, 3),
    "P4_decoupling": P4,
    "P4_falsifier_fired": bool(all(abs(p["m"]) < 0.06 for p in P4)
                               and P4[-1]["skill"] < skills["L2"]["skill"]
                               and all(P4[i + 1]["skill"] <= P4[i]["skill"] + 1e-9
                                       for i in range(len(P4) - 1))),
    "P4_fixed_point_comparison": FP,
    "P5_recharting": P5,
    "P5_common_a_max_deviation": common_dev,
    "P5_B_only_worst_skill": b_only_worst,
    "P5_holds": bool(common_dev < 0.05 and b_only_worst < 0.60),
    "P5b_posthoc_chart_internal_normalizer": {
        "ratio_common_a_max": common_ratio_span[0],
        "ratio_common_a_min": common_ratio_span[1],
        "ratio_B_only_worst": b_only_ratio_worst,
        "common_a_preserved": bool(common_ratio_span[0] < 1.6),
    },
    "L2_skill_32_seeds": {"mean": L2_32[0], "sd": L2_32[1],
                          "archival_8_seed_value": 0.484},
}
with open(os.path.join(OUT, "verdict.json"), "w") as f:
    json.dump(verdict, f, indent=2)

with open(os.path.join(OUT, "summary.csv"), "w", newline="") as f:
    w = _csv.writer(f)
    w.writerow(["rung", "H", "r=H/H_A", "m=|r-1|", "transfer_skill", "shape_distance"])
    for k in order:
        w.writerow([k, f"{H1[k]['H']:.4f}", f"{H1[k]['r']:.4f}", f"{H1[k]['m']:.4f}",
                    f"{skills[k]['skill']:.4f}", f"{skills[k]['d']:.4f}"])
    w.writerow([])
    w.writerow(["common-factor cv", "H", "m", "transfer_skill", "shape_distance",
                "shape n64 vs n1024", "shape vs Gaussian (n1024)"])
    for p in P4:
        w.writerow([p["cv"], f"{p['H']:.4f}", f"{p['m']:.4f}", f"{p['skill']:.4f}",
                    f"{p['d']:.4f}", f"{p['self_distance_n64_n1024']:.4f}",
                    f"{p['d_to_gaussian_n1024']:.4f}"])

# --------------------------------------------------------------------- report --
print("P1 — aggregation chart order H = dln IQR / dln n   (H_A = %.4f)" % HA)
print("-" * 74)
for k in ["A"] + order[::-1]:
    v = H1[k]
    sk = "" if k == "A" else "   skill=%.3f" % skills[k]["skill"]
    print(f"  {k:<3} H={v['H']:+.4f}±{v['sd']:.4f}   r={v['r']:+.4f}   m={v['m']:.4f}{sk}")
print("\nP2 — H is gauge, r is invariant")
print("-" * 74)
for p in P2:
    print(f"  a={p['a']:<4} H_A={p['H_A']:.4f}  H_A/a={p['H_A_over_a']:.4f}   "
          f"H_L2={p['H_L2']:.4f}  H_L2/a={p['H_L2_over_a']:.4f}   r={p['r_L2']:.10f}")
print(f"  ratio span over a = {r_span:.2e}   bare H_A spans {H_span:.1f}x")
print("\nP3 — predictor comparison (ceiling = %.3f)" % CEILING)
print("-" * 74)
print(f"  R2(skill | mismatch m) = {P3['R2_skill_vs_mismatch']:.3f}    "
      f"R2(skill | rung label) = {P3['R2_skill_vs_level']:.3f}")
print(f"  m ties L3/L4: {P3['mismatch_ties_L3_L4']}   measured skill L4-L3 = "
      f"{P3['skill_L4_minus_L3']:+.3f}")
print("\nP4 — the decoupling sweep: common-factor increments, m held at 0")
print("-" * 74)
for p in P4:
    bar = "#" * int(round(p["skill"] * 40))
    print(f"  cv={p['cv']:<5} H={p['H']:.4f}  m={p['m']:.4f}  skill={p['skill']:.3f} "
          f"|{bar:<40}|  n64-vs-n1024={p['self_distance_n64_n1024']:.4f}")
print("  fixed-point diagnostic on the archival rungs:")
for k, v in FP.items():
    print(f"    {k}: n64-vs-n1024={v['self_distance_n64_n1024']:.4f}   "
          f"to-Gaussian n64={v['d_to_gaussian_n64']:.4f} n1024={v['d_to_gaussian_n1024']:.4f}")
print("\nP5 — re-chart intervention on the L4 rung")
print("-" * 74)
for p in P5:
    print(f"  a={p['a']:<4} B-only: m={p['m_B_only']:.2f} skill={p['skill_B_only']:.3f}   "
          f"common-a: m=0 skill={p['skill_common_a']:.3f}")
print(f"  common-a max deviation = {common_dev:.3f}   B-only worst = {b_only_worst:.3f}")
print("\nP5b (post-hoc) — distances re-normalized by the same chart's sampling floor")
print("-" * 74)
for p in P5:
    print(f"  a={p['a']:<4} floor={p['d_ceiling_in_chart']:.4f}   "
          f"d_common/floor={p['ratio_common_a']:.3f}   d_Bonly/floor={p['ratio_B_only']:.3f}")
print(f"  common-a ratio range = [{common_ratio_span[1]:.2f}, {common_ratio_span[0]:.2f}]   "
      f"B-only worst ratio = {b_only_ratio_worst:.1f}")
print(f"\nBookkeeping: L2 skill at 32 seeds = {L2_32[0]:.3f} ± {L2_32[1]:.3f} "
      f"(archival 8-seed value 0.484)")
print("\nVERDICT:", json.dumps({k: verdict[k] for k in
      ["P1_holds", "P2_holds", "P3_holds", "P4_falsifier_fired", "P5_holds"]}))
