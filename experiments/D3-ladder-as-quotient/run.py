"""D3 — is the ladder a chart-invariance count?

Registered in PREREGISTRATION.md, committed before this file produced numbers.
The chart is n, the number of contributions. D7/D8 apply directly: measure each
domain's log-slope vector against ln n and ask whether the chart-free residue
tracks transfer skill.

The primary registered prediction falsifies D3.

numpy + stdlib only. Deterministic. ~3 min.
"""

import json
import math

import numpy as np

SEED = 20260728
OUT = {}

N_VALUES = [50, 100, 200, 500, 1000, 2000]
M = 1500          # aggregates per (domain, n)
SEEDS = 4
GRID = np.linspace(0.02, 0.98, 97)


# ------------------------------------------------------------- domains

def inc_uniform(shape, r):
    return r.uniform(-1, 1, shape)


def inc_exp(shape, r):
    return r.exponential(1.0, shape) - 1.0


def inc_skew(shape, r):
    z = r.normal(0, 1, shape)
    j = (r.random(shape) < 0.1) * r.normal(4.0, 1.0, shape)
    x = z + j
    return x - x.mean()


def inc_heavy(shape, r):
    return r.standard_t(1.5, shape)


INCR = {"A": inc_uniform, "L4": inc_exp, "L3": inc_skew, "L2": inc_heavy}


def sample(domain, n, r):
    """M aggregates of n contributions. L1 does not aggregate at all."""
    if domain == "L1":
        return r.standard_t(1.5, M)
    return INCR[domain]((M, n), r).sum(axis=1)


# --------------------------------------------------------- observables

def observables(x):
    """Four scale-like spreads and two dimensionless shape ratios."""
    q = np.percentile(x, [0.5, 2, 10, 25, 75, 90, 98, 99.5])
    s1 = q[4] - q[3]
    s2 = q[5] - q[2]
    s3 = q[6] - q[1]
    s4 = q[7] - q[0]
    return np.array([s1, s2, s3, s4, s2 / s1, s3 / s1])


OBS_NAMES = ["iqr", "p90_10", "p98_02", "p99.5_0.5", "shape_90/iqr", "shape_98/iqr"]
SCALE_IDX = [0, 1, 2, 3]
SHAPE_IDX = [4, 5]


def slope_vector(domain):
    """y_i = d ln O_i / d ln n, averaged over seeds."""
    per_seed = []
    for s in range(SEEDS):
        rows = []
        for n in N_VALUES:
            r = np.random.default_rng(10_000 * s + n)
            rows.append(observables(sample(domain, n, r)))
        Ov = np.array(rows)
        ln_n = np.log(np.array(N_VALUES, float))
        A = np.vstack([ln_n, np.ones_like(ln_n)]).T
        per_seed.append(np.array([
            np.linalg.lstsq(A, np.log(Ov[:, k]), rcond=None)[0][0]
            for k in range(Ov.shape[1])]))
    P = np.array(per_seed)
    return P.mean(0), P.std(0)


# ------------------------------------------------ residue and distance

def projective_class(y, tol=0.02):
    """y normalized by its first component; the chart-free content (D7)."""
    if np.max(np.abs(y)) < tol:
        return None            # zero vector: no ray, rank 0
    return y / y[0]


def subspace_sine(y1, y2):
    """sin of the angle between the two rays. Never arccos -- see D8's P1."""
    u = y1 / np.linalg.norm(y1)
    v = y2 / np.linalg.norm(y2)
    return float(np.linalg.norm(v - u * (u @ v)))


# ---------------------------------------- P5: is n a legitimate chart?

def additivity_defect(a, n1=400, n2=400):
    """Aggregation composes: n1 then n2 contributions is n1 + n2 of them.

    Under the relabelling n -> n^a that composition must survive if G_pow is
    available. Defect = |(n1^a + n2^a) - (n1+n2)^a| / (n1+n2)^a, which is
    P-D's extensivity test with the count in place of the mass.
    """
    lhs = n1**a + n2**a
    rhs = (n1 + n2) ** a
    return abs(lhs - rhs) / rhs


# --------------------------------------- P6: reproduce the harness

def transfer_skills():
    def robust_shape(x):
        med = np.median(x)
        q1, q3 = np.percentile(x, [25, 75])
        return np.quantile((x - med) / (q3 - q1 + 1e-12), GRID)

    def w1(qa, qb):
        return float(np.mean(np.abs(qa - qb)))

    MM = 4000
    q_ref = robust_shape(np.random.default_rng(1).standard_t(1.5, 200000))
    out = {k: [] for k in ("L4", "L3", "L2", "L1")}
    for s in range(8):
        r = np.random.default_rng(100 + s)
        qA = robust_shape(INCR["A"]((MM, 200), r).sum(axis=1))
        d_ref = w1(qA, q_ref)
        for name in ("L4", "L3", "L2", "L1"):
            xb = (r.standard_t(1.5, MM) if name == "L1"
                  else INCR[name]((MM, 200), r).sum(axis=1))
            out[name].append(max(0.0, 1.0 - w1(qA, robust_shape(xb)) / d_ref))
    return {k: float(np.mean(v)) for k, v in out.items()}


# ----------------------------------------------------------------- main

if __name__ == "__main__":
    OUT["seed"] = SEED
    print("P1 slope vectors ...", flush=True)

    slopes, sds = {}, {}
    for dom in ("A", "L4", "L3", "L2", "L1"):
        y, sd = slope_vector(dom)
        slopes[dom], sds[dom] = y, sd
        print(f"  {dom}: {[round(v, 4) for v in y]}", flush=True)

    OUT["P1_slopes"] = {
        d: {"observables": OBS_NAMES,
            "slopes": slopes[d].tolist(),
            "seed_sd": sds[d].tolist(),
            "scale_mean": float(np.mean(slopes[d][SCALE_IDX])),
            "shape_max_abs": float(np.max(np.abs(slopes[d][SHAPE_IDX])))}
        for d in slopes}

    # ---- P2 / P3: the residue, its rank, and the distances
    cls, ranks = {}, {}
    for d, y in slopes.items():
        c = projective_class(y)
        cls[d] = None if c is None else c.tolist()
        ranks[d] = 0 if c is None else 1

    dists = {}
    for d in ("L4", "L3", "L2", "L1"):
        if cls[d] is None:
            dists[d] = None
        else:
            dists[d] = subspace_sine(slopes["A"], slopes[d])

    OUT["P2_residue"] = {
        "projective_classes": cls,
        "residue_distance_from_A": dists,
        "d3_saving_criterion": "A-L2 distance > 3x both A-L3 and A-L4",
        "d3_saved": bool(
            dists["L2"] is not None and dists["L3"] is not None
            and dists["L4"] is not None
            and dists["L2"] > 3 * max(dists["L3"], dists["L4"])),
    }
    OUT["P3_rank"] = {
        "rank_by_domain": ranks,
        "count_r_times_n_minus_r": {d: r * (6 - r) for d, r in ranks.items()},
        "distinct_counts": sorted({r * (6 - r) for r in ranks.values()}),
    }

    # ---- P4: which predictor places which boundary
    print("P4/P6 transfer ...", flush=True)
    skill = transfer_skills()
    alpha_inv = {d: float(np.mean(slopes[d][SCALE_IDX])) for d in slopes}
    bare = {d: abs(alpha_inv[d] - alpha_inv["A"]) for d in ("L4", "L3", "L2", "L1")}

    def places_boundary(vals, lo=("L1", "L2"), hi=("L3", "L4"), sep=0.05):
        """Does this predictor separate {L1,L2} from {L3,L4}?"""
        v = {k: (1e9 if vals[k] is None else vals[k]) for k in vals}
        return bool(min(v[k] for k in lo) > max(v[k] for k in hi) + sep)

    OUT["P4_comparison"] = {
        "transfer_skill": skill,
        "residue_distance": dists,
        "bare_exponent_distance": bare,
        "rung_label": {"L1": 1, "L2": 2, "L3": 3, "L4": 4},
        "residue_places_transfer_boundary": places_boundary(dists),
        "bare_exponent_places_transfer_boundary": places_boundary(bare),
        "residue_ties": [d for d in ("L2", "L3", "L4")
                         if dists[d] is not None and dists[d] < 0.05],
    }

    # ---- P5: is n a legitimate G_pow chart?
    OUT["P5_chart_pinned"] = {
        "additivity_defect": {str(a): additivity_defect(a)
                              for a in (1.0, 1.5, 2.0, 0.5)},
        "reading": "0 at a=1 and large otherwise means aggregation stops "
                   "composing under n -> n^a, so G_pow is unavailable and the "
                   "magnitudes are facts (D2 rule i) -- P-D's leg F argument "
                   "with the count in place of the mass",
    }
    OUT["P6_harness_reproduction"] = {
        "measured": skill,
        "published": {"L1": 0.033, "L2": 0.484, "L3": 0.916, "L4": 0.894},
        "max_abs_diff": max(abs(skill[k] - v) for k, v in
                            {"L1": 0.033, "L2": 0.484,
                             "L3": 0.916, "L4": 0.894}.items()),
    }

    # ---- POST-HOC DIAGNOSTIC (not registered)
    # The primary prediction said the residue would TIE across L2/L3/L4. It
    # did not -- it ordered them, with L2 furthest from A. Before crediting
    # that as chart-free content, check what carries it. L2's tilt sits in the
    # q99.5-q0.5 observable, which is estimated from ~M/200 samples beyond it
    # and is therefore worst exactly where the tails are heaviest. Two ways to
    # tell a real signal from an estimator artifact: drop that observable, and
    # raise M. A real signal survives both.
    print("diagnostic (post-hoc) ...", flush=True)

    def slopes_md(dom, ns, m, seeds):
        per = []
        for s in range(seeds):
            rows = []
            for n in ns:
                r = np.random.default_rng(555_000 + 1000 * s + n)
                g = (r.standard_t(1.5, m) if dom == "L1"
                     else INCR[dom]((m, n), r).sum(axis=1))
                rows.append(observables(g))
            Ov = np.array(rows)
            ln = np.log(np.array(ns, float))
            A_ = np.vstack([ln, np.ones_like(ln)]).T
            per.append(np.array([
                np.linalg.lstsq(A_, np.log(Ov[:, k]), rcond=None)[0][0]
                for k in range(Ov.shape[1])]))
        return np.array(per).mean(0)

    ns_d = [500, 1000, 2000, 5000]
    keep = [0, 1, 2, 4, 5]        # every observable except the extreme spread
    drows = []
    for m in (800, 3000, 9000):
        yA = slopes_md("A", ns_d, m, 3)
        row = {"M": m,
               "L2_scale_slopes": slopes_md("L2", ns_d, m, 3)[SCALE_IDX].tolist()}
        for d in ("L4", "L3", "L2"):
            yd = slopes_md(d, ns_d, m, 3)
            row[f"{d}_all"] = subspace_sine(yA, yd)
            row[f"{d}_drop_extreme"] = subspace_sine(yA[keep], yd[keep])
        drows.append(row)
    OUT["POSTHOC_what_carries_the_residue"] = {
        "_note": "not registered; the primary prediction said the residue "
                 "would tie across L2/L3/L4 and it ordered them instead. This "
                 "asks whether that ordering is scaling structure or "
                 "extreme-quantile estimation error. Never counted as a pass.",
        "rows": drows,
    }

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2)

    print("\n--- summary ---")
    for d in ("A", "L4", "L3", "L2", "L1"):
        p = OUT["P1_slopes"][d]
        print(f"P1  {d}: scale slope {p['scale_mean']:.4f} "
              f"(sd {max(sds[d][SCALE_IDX]):.4f}), "
              f"shape |max| {p['shape_max_abs']:.4f}")
    print(f"P2  projective classes: " + "; ".join(
        f"{d}=" + ("ZERO VECTOR" if cls[d] is None
                   else str([round(v, 3) for v in cls[d]]))
        for d in ("A", "L4", "L3", "L2", "L1")))
    print(f"    residue distance from A: " + ", ".join(
        f"{d}={'n/a' if dists[d] is None else format(dists[d], '.4f')}"
        for d in ("L4", "L3", "L2", "L1")))
    print(f"    D3 saved by this leg? {OUT['P2_residue']['d3_saved']}")
    print(f"P3  ranks {ranks}, counts {OUT['P3_rank']['count_r_times_n_minus_r']}, "
          f"distinct counts {OUT['P3_rank']['distinct_counts']}")
    print(f"P4  transfer   {({k: round(v,3) for k,v in skill.items()})}")
    print(f"    bare expo  {({k: round(v,3) for k,v in bare.items()})}")
    print(f"    residue places the transfer boundary? "
          f"{OUT['P4_comparison']['residue_places_transfer_boundary']}; "
          f"bare exponent does? "
          f"{OUT['P4_comparison']['bare_exponent_places_transfer_boundary']}")
    print(f"P5  additivity defect "
          f"{ {k: round(v,4) for k,v in OUT['P5_chart_pinned']['additivity_defect'].items()} }")
    print("\n--- post-hoc diagnostic (not registered) ---")
    for r in OUT["POSTHOC_what_carries_the_residue"]["rows"]:
        print(f"  M={r['M']:>5}  ALL obs: L4={r['L4_all']:.4f} "
              f"L3={r['L3_all']:.4f} L2={r['L2_all']:.4f}   |   "
              f"drop extreme: L4={r['L4_drop_extreme']:.4f} "
              f"L3={r['L3_drop_extreme']:.4f} L2={r['L2_drop_extreme']:.4f}")
        print(f"         L2 scale slopes {[round(v,4) for v in r['L2_scale_slopes']]}")
    print(f"P6  max diff vs published {OUT['P6_harness_reproduction']['max_abs_diff']:.4f}")
