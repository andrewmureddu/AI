"""
D3 - is the ladder a chart-invariance count?

D3 (questions/UNKNOWN-LAWS.md) conjectured that if D1 is right, "does this
correspondence transfer?" has a mechanical answer -- it transfers IFF it is
chart-invariant -- so the ladder would be a count of how many coordinate choices
have been quotiented out rather than a scale of epistemic quality.

The registered falsifier names two off-diagonal cells, and this experiment builds
both, because they are where the rung-label theory and D3 predict OPPOSITE things:

  (b)  a shared-MECHANISM correspondence stated chart-DEPENDENTLY
       -> rung says transfer, D3 says fail
  (a)  a different-mechanism correspondence stated chart-FREELY
       -> rung says fail, D3 says transfer

Design: the ladder-vs-transfer harness, crossed with two new factors.

  rung       L1..L4, exactly the original generators (mechanism depth)
  chart      domain B records on y -> sgn(y)|y|^a, a in {1, 0.5, 2, 3}
             (the G_pow group of D1/D2, acting on the measurement axis)
  statement  raw  : compare the standardized shape of Y        (chart-DEPENDENT)
             log  : compare the standardized shape of ln|Y|    (chart-FREE, since
                    ln|y|^a = a ln|y| and standardizing kills the factor a)

Pure numpy, deterministic.  ~1 min.
"""

import json
import os

import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
N_INCR = 200
M = 4000
SEEDS = 8
GRID = np.linspace(0.02, 0.98, 97)
# Milder distortions than a first pass used: at a >= 2 every cell clips at the
# skill floor, which hides the gradient and makes the columns uninformative.
CHARTS = [1.0, 0.85, 0.7, 0.5, 1.5, 2.0]


# --- generators: identical to experiments/ladder-vs-transfer/run.py -------
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


def aggregate(incr_fn, r):
    return incr_fn((M, N_INCR), r).sum(axis=1)


def macro_single(r):
    return r.standard_t(1.5, M)


CASES = [
    ("L4", 4, 1, "exponential increments (CLT is a theorem)", lambda r: aggregate(inc_exp, r)),
    ("L3", 3, 1, "skewed finite-variance mix (same CLT mechanism)", lambda r: aggregate(inc_skew, r)),
    ("L2", 2, 0, "heavy-tailed nu=1.5 (infinite variance -> stable law)", lambda r: aggregate(inc_heavy, r)),
    ("L1", 1, 0, "single heavy draw (not an aggregate)", macro_single),
]


# --- charts and statement forms -------------------------------------------

def apply_chart(y, a):
    """G_pow acting on the measurement axis, applied to the CENTRED reading.

    Centring first is what makes the chart a clean power map: real measurement
    charts of this kind (log-returns, decibels, magnitude scales) are all defined
    relative to a reference level.
    """
    y0 = y - np.median(y)
    return np.sign(y0) * np.abs(y0) ** a


def robust_shape(x):
    med = np.median(x)
    q1, q3 = np.percentile(x, [25, 75])
    return np.quantile((x - med) / (q3 - q1 + 1e-12), GRID)


def statistic(y, form):
    if form == "raw":
        return robust_shape(y)
    return robust_shape(np.log(np.maximum(np.abs(y), 1e-30)))


def w1(qa, qb):
    return float(np.mean(np.abs(qa - qb)))


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean()
    ry -= ry.mean()
    return float((rx @ ry) / (np.sqrt(rx @ rx) * np.sqrt(ry @ ry) + 1e-12))


# --------------------------------------------------------------------------

def main():
    skills = {}
    for s in range(SEEDS):
        r = np.random.default_rng(100 + s)
        A = aggregate(inc_uniform, r)                       # reference domain
        ref = np.random.default_rng(1).standard_t(1.5, 200000)
        for form in ("raw", "log"):
            qA = statistic(apply_chart(A, 1.0), form)
            d_ref = w1(qA, statistic(apply_chart(ref, 1.0), form))
            for name, rung, mech, _desc, gen in CASES:
                B = gen(r)
                for a in CHARTS:
                    qB = statistic(apply_chart(B, a), form)
                    raw_sk = 1.0 - w1(qA, qB) / d_ref
                    skills.setdefault((name, a, form), []).append(
                        (max(0.0, raw_sk), raw_sk))

    cells = []
    for (name, a, form), v in skills.items():
        rung = dict((c[0], c[1]) for c in CASES)[name]
        mech = dict((c[0], c[2]) for c in CASES)[name]
        chart_free = 1 if form == "log" else 0
        undistorted = 1 if a == 1.0 else 0
        cells.append({
            "rung_name": name, "rung": rung, "mechanism_shared": mech,
            "chart_a": a, "statement": form, "claim_chart_free": chart_free,
            "chart_undistorted": undistorted,
            # the registered two-factor model
            "conjunction": int(mech == 1 and (chart_free == 1 or undistorted == 1)),
            "skill": float(np.mean([x[0] for x in v])),
            "skill_unclipped": float(np.mean([x[1] for x in v])),
            "sd": float(np.std([x[0] for x in v])),
        })

    sk = [c["skill"] for c in cells]
    res = {
        "n_cells": len(cells), "cells": cells,
        "predictors": {
            "rung_alone": spearman([c["rung"] for c in cells], sk),
            "claim_chart_free_alone": spearman([c["claim_chart_free"] for c in cells], sk),
            "mechanism_alone": spearman([c["mechanism_shared"] for c in cells], sk),
            "conjunction": spearman([c["conjunction"] for c in cells], sk),
        },
    }

    def grab(name, a, form):
        return [c for c in cells if c["rung_name"] == name and c["chart_a"] == a
                and c["statement"] == form][0]["skill"]

    def grab_u(name, a, form):
        return [c for c in cells if c["rung_name"] == name and c["chart_a"] == a
                and c["statement"] == form][0]["skill_unclipped"]

    # Added AFTER seeing the table: Spearman(rung, skill) computed WITHIN each
    # (chart, statement) column.  This is a better reading of the registered
    # quantities than the pooled horse race in P5 -- it asks directly whether the
    # ladder orders transfer, separately under each measurement convention.
    #
    # Ranked on the UNCLIPPED skill: skill is floored at 0, and under the harsher
    # charts every raw cell clips, so ranking the clipped values ranks a column of
    # ties and the tie-breaking manufactures a spurious +1.00.
    order = ["L1", "L2", "L3", "L4"]
    per_column = {}
    for form in ("raw", "log"):
        for a in CHARTS:
            per_column[f"{form}_a={a:g}"] = spearman(
                [1, 2, 3, 4], [grab_u(n, a, form) for n in order])
    res["spearman_rung_vs_skill_per_column"] = per_column
    res["unclipped_table"] = {
        form: {f"a={a:g}": {n: round(grab_u(n, a, form), 3) for n in order}
               for a in CHARTS} for form in ("raw", "log")}

    # P1 reproduction; P2 collapse; P3 restoration; P4 the D3 falsifier
    res["P1_raw_identity"] = {n: grab(n, 1.0, "raw") for n in ["L1", "L2", "L3", "L4"]}
    res["P2_raw_distorted"] = {
        n: {"a=1": grab(n, 1.0, "raw"),
            "worst_distorted": min(grab(n, a, "raw") for a in CHARTS if a != 1.0),
            "drop": grab(n, 1.0, "raw") - min(grab(n, a, "raw") for a in CHARTS if a != 1.0)}
        for n in ["L3", "L4"]}
    res["P3_log_any_chart"] = {
        n: {"by_a": {str(a): grab(n, a, "log") for a in CHARTS},
            "spread": max(grab(n, a, "log") for a in CHARTS)
                      - min(grab(n, a, "log") for a in CHARTS)}
        for n in ["L3", "L4"]}
    res["P4_chart_free_low_rungs"] = {
        n: {"by_a": {str(a): grab(n, a, "log") for a in CHARTS},
            "max": max(grab(n, a, "log") for a in CHARTS)}
        for n in ["L1", "L2"]}

    with open(os.path.join(OUT, "verdict.json"), "w") as f:
        json.dump(res, f, indent=2)

    # ---- report ----------------------------------------------------------
    print("=" * 78)
    print("D3 - is the ladder a chart-invariance count?")
    print("=" * 78)
    print("\ntransfer skill  (1 = A's law transfers, 0 = useless)")
    for form in ("raw", "log"):
        tag = "chart-DEPENDENT claim" if form == "raw" else "chart-FREE claim"
        print(f"\n  statement = {form:3s}  ({tag})")
        print("      " + "".join(f"   a={a:<6g}" for a in CHARTS))
        for n in ["L4", "L3", "L2", "L1"]:
            row = "".join(f"   {grab(n, a, form):<8.3f}" for a in CHARTS)
            print(f"   {n} {row}")

    print("\nP1 - raw statement, undistorted chart: reproduces the original cliff")
    print("   " + "  ".join(f"{k}={v:.2f}" for k, v in res["P1_raw_identity"].items()))

    print("\nP2 - raw statement, distorted chart: shared mechanism, transfer LOST")
    for n, d in res["P2_raw_distorted"].items():
        print(f"   {n}: a=1 -> {d['a=1']:.3f}   worst distorted -> "
              f"{d['worst_distorted']:.3f}   drop = {d['drop']:.3f}")

    print("\nP3 - chart-free statement: transfer restored AND immune to the chart")
    for n, d in res["P3_log_any_chart"].items():
        print(f"   {n}: " + "  ".join(f"a={a}:{v:.3f}" for a, v in d["by_a"].items())
              + f"   spread = {d['spread']:.4f}")

    print("\nP4 - chart-free statement at the LOW rungs (D3's own falsifier)")
    for n, d in res["P4_chart_free_low_rungs"].items():
        print(f"   {n}: " + "  ".join(f"a={a}:{v:.3f}" for a, v in d["by_a"].items())
              + f"   max = {d['max']:.3f}")

    print("\nP5 - which predictor tracks transfer?  Spearman over all "
          f"{len(cells)} cells")
    for k, v in res["predictors"].items():
        print(f"   {k:26s} {v:+.3f}")

    print("\nDoes the LADDER order transfer?  Spearman(rung, skill) within each"
          " column\n   (added after seeing the table; see README)")
    for form in ("raw", "log"):
        row = "  ".join(f"a={a:g}:{res['spearman_rung_vs_skill_per_column'][f'{form}_a={a:g}']:+.2f}"
                        for a in CHARTS)
        print(f"   {form:3s}  {row}")

    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
