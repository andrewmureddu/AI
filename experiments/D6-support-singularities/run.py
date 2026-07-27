"""
D6 - do support-type singularities have a classifier?

D1 classified degeneracy-type floor-3 singularities by p, the first non-vanishing
anharmonic term of Phi.  Support-type singularities (S5's type S) have no p.  This
tests whether the classifier is more general than D1 stated:

        Phi(y) = A|y|^q1 + B|y|^q2 + ...,   q1 < q2,   A -> 0

        A_c  ~  D^((q2-q1)/q2)  =  D^(1 - q1/q2)

with D1 the case q1 = 2 (smoothness pins the leading term to quadratic) and
support loss the case q1 = 1 (a kink or a boundary, where D1's formula is not
wrong but undefined).

Observable is SHAPE, not D1's rounding ratio: for a single-term Phi = A|y|^q the
standardized moments depend on q alone, so excess kurtosis reads q off directly --
and unlike Var*lambda/D it needs no curvature, which a kink does not have.

Pure numpy.  ~2 min.
"""

import json
from math import lgamma, exp

import numpy as np

SEED = 20260726
C_CUT = 45.0
D_GRID = np.logspace(-8.0, -4.0, 9)


def kurt_of_q(q):
    """Excess kurtosis of the generalized Gaussian exp(-c|y|^q)."""
    return exp(lgamma(5.0 / q) + lgamma(1.0 / q) - 2.0 * lgamma(3.0 / q)) - 3.0


def fit_slope(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    M = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(M, ly, rcond=None)
    return float(coef[0]), float(np.max(np.abs(ly - M @ coef)))


# --------------------------------------------------------------------------
# continuous legs: excess kurtosis of rho ~ exp(-Phi/D) by quadrature
# --------------------------------------------------------------------------

def _outer_limit(phi, D):
    """Where Phi reaches C_CUT * D, by geometric bracketing then bisection."""
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


def excess_kurtosis(phi, D, symmetric=True, n=200001):
    """Excess kurtosis of rho(y) ~ exp(-phi(y)/D)."""
    R = _outer_limit(phi, D)
    lo = -R if symmetric else 0.0
    y = np.linspace(lo, R, n)
    p = phi(y)
    w = np.exp(-(p - p.min()) / D)
    z = np.trapezoid(w, y)
    m1 = np.trapezoid(y * w, y) / z
    c = y - m1
    m2 = np.trapezoid(c**2 * w, y) / z
    m4 = np.trapezoid(c**4 * w, y) / z
    return m4 / (m2 * m2) - 3.0


def crossover_A(make_phi, D, target_kurt, A_hi, A_lo=1e-14, n_scan=90,
                symmetric=True, n_quad=200001):
    """Outermost A at which the shape statistic crosses its midpoint.

    Scanned inward from the q1-dominated (large A) end for the same reason D1
    had to: bisecting on a level set alone can land on different branches.
    """
    def kurt(A):
        return excess_kurtosis(make_phi(A), D, symmetric, n=n_quad)

    grid = np.logspace(np.log10(A_hi), np.log10(A_lo), n_scan)
    k_hi = kurt(grid[0])
    above = k_hi > target_kurt          # kurtosis falls as A falls (q1 -> q2)
    idx = None
    for i in range(1, n_scan):
        ki = kurt(grid[i])
        if (ki > target_kurt) != above:
            idx = i
            break
    if idx is None:
        return None
    lo, hi = np.log(grid[idx]), np.log(grid[idx - 1])
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        if (kurt(np.exp(mid)) > target_kurt) != above:
            lo = mid
        else:
            hi = mid
    return float(np.exp(0.5 * (lo + hi)))


def sweep_pair(q1, q2, B=1.0, d_grid=D_GRID):
    """Synthetic two-term model:  Phi = A|y|^q1 + B|y|^q2."""
    k1, k2 = kurt_of_q(q1), kurt_of_q(q2)
    target = 0.5 * (k1 + k2)
    make = lambda A: (lambda y: A * np.abs(y) ** q1 + B * np.abs(y) ** q2)
    As, Ds = [], []
    for D in d_grid:
        A = crossover_A(make, D, target, A_hi=1e4)
        if A is not None:
            As.append(A)
            Ds.append(D)
    out = {"q1": q1, "q2": q2, "ratio_q1_q2": q1 / q2,
           "predicted": (q2 - q1) / q2,
           "kurt_q1": k1, "kurt_q2": k2, "target_kurt": target, "n": len(Ds)}
    if len(Ds) >= 4:
        s, r = fit_slope(Ds, As)
        out["exponent"] = s
        out["max_resid"] = r
        out["A_c"] = As
        out["D"] = Ds
    return out


# --------------------------------------------------------------------------
# P3 - a real all-orders model with q1 = 1: L1-penalised logistic regression
# --------------------------------------------------------------------------

def logistic_nll_factory(rng, n=60):
    """1-D logistic negative log-likelihood, shifted to vanish at beta = 0.

    The design pairs each covariate with both labels, so the margins
    z_i = y_i x_i come in +-pairs and sum to zero -- which is what puts the
    UNPENALISED optimum at beta = 0, so the only non-smoothness at the origin is
    the L1 kink.  (An earlier version concatenated [x, -x] with labels [+1, -1],
    which duplicates the margins rather than balancing them and leaves the
    optimum away from zero.)

    With z = +-x0 the likelihood collapses to
        ell(b) = 2 sum_j log(2 cosh(x0_j b / 2)) - 2 n log 2
    which is even in b and carries every even order -- b^2, b^4, b^6, ...
    """
    x0 = rng.standard_normal(n)

    def ell(b):
        bb = np.asarray(b, float)
        u = np.abs(0.5 * np.multiply.outer(bb.ravel(), x0))
        # log(2 cosh u) = |u| + log1p(exp(-2|u|)), overflow-safe
        v = 2.0 * np.sum(u + np.log1p(np.exp(-2.0 * u)), axis=1)
        v = v - 2.0 * n * np.log(2.0)
        return float(v[0]) if bb.ndim == 0 else v.reshape(bb.shape)

    return ell


def leg_logistic(rng):
    ell = logistic_nll_factory(rng)
    scale = ell(1.0)                                # normalise the smooth part
    ell_n = lambda b: ell(b) / scale
    k1, k2 = kurt_of_q(1.0), kurt_of_q(2.0)
    target = 0.5 * (k1 + k2)
    make = lambda tau: (lambda b: tau * np.abs(b) + ell_n(b))
    taus, Ds = [], []
    for D in np.logspace(-7.0, -3.0, 9):
        # coarser quadrature here: each evaluation is a sum over the design, so
        # the 200k-point grid used for the closed-form legs costs ~100x more
        t = crossover_A(make, D, target, A_hi=1e2, n_quad=20001)
        if t is not None:
            taus.append(t)
            Ds.append(D)
    out = {"model": "L1-penalised logistic regression", "q1": 1, "q2": 2,
           "predicted": 0.5, "n": len(Ds), "target_kurt": target}
    if len(Ds) >= 4:
        s, r = fit_slope(Ds, taus)
        out["exponent"] = s
        out["max_resid"] = r
        out["tau_c"] = taus
        out["D"] = Ds
    return out


# --------------------------------------------------------------------------
# P4 / P5 - queues, exact discrete stationary laws
# --------------------------------------------------------------------------

def discrete_excess_kurtosis(p, n):
    m1 = np.sum(n * p)
    c = n - m1
    m2 = np.sum(c**2 * p)
    m4 = np.sum(c**4 * p)
    return m4 / (m2 * m2) - 3.0


def leg_mm1():
    """Infinite buffer: P(n) ~ rho^n.  q1 = 1, no second term -> no crossover."""
    rows = []
    for gap in np.logspace(-1, -5, 9):              # gap = 1 - rho
        rho = 1.0 - gap
        N = int(min(4e7, 80.0 / gap))
        n = np.arange(N + 1)
        logp = n * np.log(rho)
        p = np.exp(logp - logp.max())
        p /= p.sum()
        rows.append({"one_minus_rho": float(gap),
                     "excess_kurtosis": float(discrete_excess_kurtosis(p, n))})
    ks = [r["excess_kurtosis"] for r in rows]
    return {"model": "M/M/1, infinite buffer", "rows": rows,
            "kurt_exponential": 6.0,
            "mean": float(np.mean(ks)), "spread": float(max(ks) - min(ks)),
            "crossover_exists": False}


def leg_mm1k():
    """Finite buffer K: the wall is q2 -> infinity, so the predicted exponent
    is (q2-q1)/q2 -> 1, with 1/K playing the role of D."""
    k_geom, k_unif = 6.0, -6.0 / 5.0                # exponential vs uniform
    target = 0.5 * (k_geom + k_unif)
    Ks = np.array([100, 200, 400, 800, 1600, 3200, 6400])
    Ac = []
    for K in Ks:
        n = np.arange(K + 1)

        def kurt(A):
            logp = -A * n
            p = np.exp(logp - logp.max())
            p /= p.sum()
            return discrete_excess_kurtosis(p, n)

        lo, hi = np.log(1e-9), np.log(10.0)         # A = ln(1/rho)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if kurt(np.exp(mid)) > target:
                hi = mid                            # large A -> geometric shape
            else:
                lo = mid
        Ac.append(float(np.exp(0.5 * (lo + hi))))
    s, r = fit_slope(1.0 / Ks, Ac)
    return {"model": "M/M/1/K, finite buffer", "K": Ks.tolist(), "A_c": Ac,
            "target_kurt": target, "exponent_vs_inverse_K": s,
            "predicted": 1.0, "max_resid": r}


# --------------------------------------------------------------------------

def main():
    rng = np.random.default_rng(SEED)
    res = {"seed": SEED, "kurtosis_table": {str(q): kurt_of_q(q)
                                            for q in [0.5, 1, 2, 3, 4, 6, 8]}}

    pairs = [(2, 4), (1, 2), (2, 6), (1, 3), (1, 4), (0.5, 2), (2, 8), (3, 4), (1, 6)]
    res["synthetic"] = [sweep_pair(q1, q2) for q1, q2 in pairs]
    res["logistic"] = leg_logistic(rng)
    res["mm1"] = leg_mm1()
    res["mm1k"] = leg_mm1k()

    with open("verdict.json", "w") as fh:
        json.dump(res, fh, indent=2)

    print("=" * 76)
    print("D6 - do support-type singularities have a classifier?")
    print("=" * 76)

    print("\nP1/P2 - synthetic two-term models  Phi = A|y|^q1 + B|y|^q2")
    print(f"  {'(q1,q2)':>10s} {'q1/q2':>7s} {'measured':>10s} {'predicted':>10s} "
          f"{'err':>8s} {'resid':>9s}")
    for s in res["synthetic"]:
        if "exponent" not in s:
            print(f"  ({s['q1']},{s['q2']}) unbracketed")
            continue
        print(f"  {'(%g,%g)'%(s['q1'],s['q2']):>10s} {s['ratio_q1_q2']:7.3f} "
              f"{s['exponent']:10.4f} {s['predicted']:10.4f} "
              f"{abs(s['exponent']-s['predicted']):8.4f} {s['max_resid']:9.2e}")

    print("\nP2 - the ratio is the classifier: pairs sharing q1/q2 must agree")
    groups = {}
    for s in res["synthetic"]:
        if "exponent" in s:
            groups.setdefault(round(s["ratio_q1_q2"], 4), []).append(s)
    for r, g in sorted(groups.items()):
        if len(g) < 2:
            continue
        es = [x["exponent"] for x in g]
        tags = ", ".join("(%g,%g)" % (x["q1"], x["q2"]) for x in g)
        print(f"  ratio {r:.3f}: {tags:34s} exponents "
              + " ".join("%.4f" % e for e in es)
              + f"   spread={max(es)-min(es):.4f}")
    q2_4 = [s for s in res["synthetic"] if s["q2"] == 4 and "exponent" in s]
    if len(q2_4) >= 2:
        es = [s["exponent"] for s in q2_4]
        print(f"  control - same q2=4, different ratio: "
              + " ".join("(%g,%g)=%.4f" % (s["q1"], s["q2"], s["exponent"])
                         for s in q2_4)
              + f"   spread={max(es)-min(es):.4f} (must exceed 0.20)")

    print("\nP3 - real all-orders model with q1=1 (L1-penalised logistic):")
    L = res["logistic"]
    if "exponent" in L:
        print(f"  tau_c ~ D^{L['exponent']:.4f}   (predicted {L['predicted']:.4f},"
              f"  max resid {L['max_resid']:.2e})")

    print("\nP4 - M/M/1, infinite buffer: no second term -> no crossover")
    M = res["mm1"]
    for r in M["rows"]:
        print(f"    1-rho = {r['one_minus_rho']:.2e}   excess kurtosis = "
              f"{r['excess_kurtosis']:.4f}")
    print(f"  mean = {M['mean']:.4f} (exponential value 6.0), "
          f"spread = {M['spread']:.4f}")

    print("\nP5 - M/M/1/K, hard wall = the q2 -> infinity corner")
    Q = res["mm1k"]
    print(f"  A_c vs 1/K: exponent = {Q['exponent_vs_inverse_K']:.4f} "
          f"(predicted {Q['predicted']:.1f}, max resid {Q['max_resid']:.2e})")

    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
