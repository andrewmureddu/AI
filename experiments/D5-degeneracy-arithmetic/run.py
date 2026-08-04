"""
D5 - does the degeneracy order have arithmetic?

D5 asked whether the degeneracy order is conserved, additive or bounded along a
sequence of transitions.  Two readings, and D6 moved the ground under both:

  (a) coalescence -- two transitions in succession.  Singularity theory answers
      it: CODIMENSION adds, so p_composite = p1 + p2 - 2 (two folds -> a cusp).
      Textbook, graded N0, verified here as an estimator check only.

  (b) multi-term Phi -- the live version, since D6 showed p was the q1 = 2 slice
      of a PAIR.  With Phi = A|y|^q1 + sum_j B_j |y|^q_j, each higher term supplies
      its own rounding scale and the lowest one governs first, so the prediction
      is a STAIRCASE with the j-th plateau at 1 - q1/q_j.  The arithmetic is
      ENUMERATION, not addition: terms queue, they do not combine.

The at-risk content is not the staircase's values (D6 applied repeatedly) but
whether the intermediate plateaus EXIST -- P8 has just shown they need not.

Pure numpy, deterministic.  ~8 min.
"""

import json
from math import exp, lgamma

import numpy as np

SEED = 20260727
C_CUT = 45.0


def kurt_of_q(q):
    return exp(lgamma(5.0 / q) + lgamma(1.0 / q) - 2.0 * lgamma(3.0 / q)) - 3.0


def _outer(phi, D):
    target = C_CUT * D
    hi = 1e-9
    for _ in range(400):
        if phi(hi) > target:
            break
        hi *= 2.0
    lo = 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if phi(mid) > target:
            hi = mid
        else:
            lo = mid
    return hi


def excess_kurtosis(phi, D, n=120001):
    R = _outer(phi, D)
    y = np.linspace(-R, R, n)
    p = phi(y)
    w = np.exp(-(p - p.min()) / D)
    z = np.trapezoid(w, y)
    m1 = np.trapezoid(y * w, y) / z
    c = y - m1
    m2 = np.trapezoid(c**2 * w, y) / z
    m4 = np.trapezoid(c**4 * w, y) / z
    return m4 / (m2 * m2) - 3.0


def make_phi(q1, terms):
    """Phi = A|y|^q1 + sum B_j |y|^q_j ; returns a function of A."""
    def f(A):
        def phi(y):
            ay = np.abs(y)
            out = A * ay ** q1
            for q, B in terms:
                out = out + B * ay ** q
            return out
        return phi
    return f


def crossover_A(fac, D, target, A_hi=1e6, A_lo=1e-16, n_scan=95):
    """Outermost A at which the shape statistic leaves the q1 value.

    Scanned inward from the q1-dominated (large A) end, as in D6 -- bisecting on
    a level set alone can land on a different branch when several terms compete,
    which is exactly the regime this experiment is about.
    """
    def k(A):
        return excess_kurtosis(fac(A), D)

    grid = np.logspace(np.log10(A_hi), np.log10(A_lo), n_scan)
    k0 = k(grid[0])
    above = k0 > target
    idx = None
    for i in range(1, n_scan):
        if (k(grid[i]) > target) != above:
            idx = i
            break
    if idx is None:
        return None
    lo, hi = np.log(grid[idx]), np.log(grid[idx - 1])
    for _ in range(42):
        mid = 0.5 * (lo + hi)
        if (k(np.exp(mid)) > target) != above:
            lo = mid
        else:
            hi = mid
    return float(np.exp(0.5 * (lo + hi)))


def staircase(q1, terms, d_grid):
    """Local log-log slope of A_c(D); the plateaus are the staircase."""
    fac = make_phi(q1, terms)
    # leave the q1 shape: threshold midway to the NEAREST higher term's shape
    target = 0.5 * (kurt_of_q(q1) + kurt_of_q(terms[0][0]))
    A, Ds = [], []
    for D in d_grid:
        a = crossover_A(fac, D, target)
        if a is not None:
            A.append(a)
            Ds.append(D)
    if len(Ds) < 8:
        return None
    lD, lA = np.log(np.array(Ds)), np.log(np.array(A))
    return {"D": Ds, "A_c": A, "slope": np.gradient(lA, lD).tolist()}


def plateaus(slope, D, predicted, tol=0.04):
    """Width in decades over which the slope sits within tol of each prediction."""
    s = np.array(slope)
    lD = np.log10(np.array(D))
    out = []
    for p in predicted:
        m = np.abs(s - p) < tol
        width = 0.0
        if m.any():
            # widest contiguous run
            best = run = 0
            start = None
            for i, v in enumerate(m):
                if v:
                    if start is None:
                        start = i
                    run = lD[i] - lD[start]
                    best = max(best, run)
                else:
                    start = None
            width = best
        out.append({"predicted": p, "decades_within_tol": float(width),
                    "closest_slope": float(s[np.argmin(np.abs(s - p))])})
    return out


def main():
    res = {"seed": SEED}

    # ---- P5: codimension additivity (identity / estimator check) ----------
    # Two folds at +-d merging: V'(x) = (x^2 - d^2) -> V = x^3/3 - d^2 x.
    # At coincidence (d=0) the germ is x^3 (a fold, p=3).  Bringing two FOLDS of a
    # one-parameter family together needs the next unfolding: V' = x^3 - e x,
    # whose germ at e=0 is x^4 -> p=4 = 3+3-2, codim 2 = 1+1.
    x = np.linspace(-0.4, 0.4, 40001)
    V = x**4 / 4.0                                   # merged germ
    c = np.polyfit(x, V, 6)[::-1]
    res["P5_coalescence"] = {
        "merged_leading_order": int(np.argmax(np.abs(c[2:]) > 1e-9) + 2),
        "p_composite_predicted": 4, "p1_plus_p2_minus_2": 3 + 3 - 2,
        "codim_predicted": 2, "note": "textbook (Thom/Arnold); N0, estimator check",
    }

    # ---- P1/P2/P3: the staircases ----------------------------------------
    # Coefficients chosen so the plateau SWITCH lands mid-sweep.  Equating the two
    # rounding scales A_c,j = (B_j/u*)^(q1/q_j) D^(1-q1/q_j) gives the switch:
    #     (2;4,6):  D_switch = B2^3 / B3^2        (2;4,8) & (1;2,4): B2^2 / B3
    #     (2;3,6):  D_switch = B2^2 / B3
    # A first version used B3 = 1e6 throughout, which puts (2;4,6)'s switch at
    # 1e-12 -- BELOW the swept grid, so only one plateau could ever appear.  That
    # is arithmetic from the registered formula, not a result, so it is corrected
    # here before any output existed; recorded in the README.
    cases = [
        ("q1=2; 4,6",   2.0, [(4.0, 1.0), (6.0, 1e2)],  [0.5, 2.0 / 3.0]),
        ("q1=2; 4,8",   2.0, [(4.0, 1.0), (8.0, 1e4)],  [0.5, 0.75]),
        ("q1=2; 3,6",   2.0, [(3.0, 1.0), (6.0, 1e4)],  [1.0 / 3.0, 2.0 / 3.0]),
        ("q1=1; 2,4",   1.0, [(2.0, 1.0), (4.0, 1e4)],  [0.5, 0.75]),
        # two switches, at ~1e-6 (4->6) and ~1e-2 (6->8)
        ("q1=2; 4,6,8", 2.0, [(4.0, 1.0), (6.0, 1e3), (8.0, 5e4)],
         [0.5, 2.0 / 3.0, 0.75]),
    ]
    D_GRID = np.logspace(-10.0, 2.0, 49)
    res["staircases"] = []
    for name, q1, terms, pred in cases:
        st = staircase(q1, terms, D_GRID)
        entry = {"case": name, "q1": q1,
                 "terms": [[q, B] for q, B in terms], "predicted": pred}
        if st is None:
            entry["status"] = "unbracketed"
        else:
            entry["plateaus"] = plateaus(st["slope"], st["D"], pred)
            entry["slope_min"] = float(min(st["slope"]))
            entry["slope_max"] = float(max(st["slope"]))
            # P3: ratio rule (1-th_j)/(1-th_{j+1}) = q_{j+1}/q_j
            obs = [p["closest_slope"] for p in entry["plateaus"]]
            qs = [q for q, _ in terms]
            entry["ratio_rule"] = [
                {"measured": float((1 - obs[j]) / (1 - obs[j + 1])),
                 "predicted": float(qs[j + 1] / qs[j])}
                for j in range(len(obs) - 1)]
        res["staircases"].append(entry)

    # ---- P4: the squeeze condition (the at-risk leg) ----------------------
    squeeze = []
    for B3 in [1e8, 1e6, 1e4, 1e2, 1e0]:
        st = staircase(2.0, [(4.0, 1.0), (6.0, B3)], D_GRID)
        if st is None:
            squeeze.append({"B3": B3, "status": "unbracketed"})
            continue
        pl = plateaus(st["slope"], st["D"], [0.5, 2.0 / 3.0])
        squeeze.append({"B3": B3,
                        "middle_plateau_decades": pl[0]["decades_within_tol"],
                        "upper_plateau_decades": pl[1]["decades_within_tol"],
                        "slope_max": float(max(st["slope"]))})
    res["P4_squeeze"] = squeeze

    with open("verdict.json", "w") as f:
        json.dump(res, f, indent=2)

    print("=" * 74)
    print("D5 - does the degeneracy order have arithmetic?")
    print("=" * 74)
    p5 = res["P5_coalescence"]
    print(f"\nP5 (identity): merged germ leading order = "
          f"{p5['merged_leading_order']}  = p1+p2-2 = {p5['p1_plus_p2_minus_2']}")

    print("\nP1/P2 - staircase plateaus (width = decades of D within +-0.04)")
    for e in res["staircases"]:
        if "plateaus" not in e:
            print(f"  {e['case']:14s} UNBRACKETED")
            continue
        print(f"  {e['case']:14s} slope range "
              f"{e['slope_min']:.3f} .. {e['slope_max']:.3f}")
        for p in e["plateaus"]:
            print(f"      predicted {p['predicted']:.4f}   closest "
                  f"{p['closest_slope']:.4f}   width {p['decades_within_tol']:.2f} dec")

    print("\nP3 - ratio rule (1-th_j)/(1-th_j+1) = q_j+1/q_j")
    for e in res["staircases"]:
        if "ratio_rule" not in e:
            continue
        for r in e["ratio_rule"]:
            print(f"  {e['case']:14s} measured {r['measured']:.3f}   "
                  f"predicted {r['predicted']:.3f}")

    print("\nP4 - squeeze: raising B3 at fixed B2 should narrow the MIDDLE plateau")
    for s in res["P4_squeeze"]:
        if "status" in s:
            print(f"  B3={s['B3']:.0e}  unbracketed")
            continue
        print(f"  B3={s['B3']:.0e}   middle {s['middle_plateau_decades']:5.2f} dec"
              f"   upper {s['upper_plateau_decades']:5.2f} dec"
              f"   slope_max {s['slope_max']:.3f}")

    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
