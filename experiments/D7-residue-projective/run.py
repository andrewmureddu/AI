"""D7 — the invariant residue is the log-slope vector modulo the diagonal R+.

Registered in PREREGISTRATION.md, committed before this file produced numbers.
Tests the four consequences of D7: weight-1 action, the count n-1, the loss of
integrality, and common-a as the group. Plus the unification leg (one estimator,
three classes) and the projective-wall reading of P-D's kink.

numpy + stdlib only. Deterministic; no sampling anywhere. ~1 min.
"""

import json
import math

import numpy as np

SEED = 20260727
OUT = {}

# ---------------------------------------------------------------- estimator


def log_slope(x, y):
    """d ln y / d ln x, least squares. The only estimator in this file."""
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y, float)))
    A = np.vstack([lx, np.ones_like(lx)]).T
    return float(np.linalg.lstsq(A, ly, rcond=None)[0][0])


def residue(o_a, o_b):
    """The chart-free slope: d ln O_a / d ln O_b. No chart appears."""
    return log_slope(o_b, o_a)


# ------------------------------------------------- M-A: the all-orders germ

C3, C4 = 0.2, 0.05


def _phi_coeffs(p, eps):
    """Phi(y) = y^p/p + C3 y^{p+1} + C4 y^{p+2} - eps*y, as {power: coeff}."""
    return {p: 1.0 / p, p + 1: C3, p + 2: C4, 1: -eps}


def _dphi(y, p, eps, m):
    """m-th derivative of Phi at y (m >= 0). Exact, all orders kept."""
    tot = 0.0
    for j, a in _phi_coeffs(p, eps).items():
        if j >= m:
            fall = 1.0
            for i in range(m):
                fall *= j - i
            tot += a * fall * y ** (j - m)
    return tot


def y_star(p, eps):
    """Root of the full Phi'(y) = 0, y > 0. Bisection in log y, then Newton."""
    lo, hi = math.log(eps ** (1.0 / (p - 1))) - 5.0, math.log(eps ** (1.0 / (p - 1))) + 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if _dphi(math.exp(mid), p, eps, 1) < 0.0:
            lo = mid
        else:
            hi = mid
    y = math.exp(0.5 * (lo + hi))
    for _ in range(60):
        f, fp = _dphi(y, p, eps, 1), _dphi(y, p, eps, 2)
        step = f / fp
        if not np.isfinite(step) or abs(step) > 0.5 * y:
            break
        y -= step
    return y


_GL = {}


def gl(n):
    if n not in _GL:
        _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]


def variance(p, eps, D, nodes=400):
    """Var of the exact stationary density ~ exp(-Phi/D), by quadrature.

    Phi(y*+d) - Phi(y*) is expanded exactly (Phi is a polynomial of degree p+2),
    which avoids differencing two numbers of size y*^p when Var ~ D/lambda is
    forty orders smaller.
    """
    ys = y_star(p, eps)
    lam = _dphi(ys, p, eps, 2)
    coef = [_dphi(ys, p, eps, m) / math.factorial(m) for m in range(1, p + 3)]
    w = 8.0 * math.sqrt(D / lam)
    x, wt = gl(nodes)
    d = w * x
    delta = np.zeros_like(d)
    for m, c in enumerate(coef, start=1):
        delta += c * d**m
    rho = np.exp(-(delta - delta.min()) / D) * wt
    z = rho.sum()
    m1 = (d * rho).sum() / z
    m2 = (d**2 * rho).sum() / z
    return m2 - m1**2


def germ_observables(p, eps_grid, D):
    """The five observables of M-A, all read off the full model."""
    ys = np.array([y_star(p, e) for e in eps_grid])
    lam = np.array([_dphi(y, p, e, 2) for y, e in zip(ys, eps_grid)])
    var = np.array([variance(p, e, D) for e in eps_grid])
    dphi = np.array([-_dphi(y, p, e, 0) for y, e in zip(ys, eps_grid)])
    d3 = np.array([_dphi(y, p, e, 3) for y, e in zip(ys, eps_grid)])
    return {"y_star": ys, "lambda": lam, "Var": var, "dPhi": dphi, "Phi3": d3}


OBS = ["y_star", "lambda", "Var", "dPhi", "Phi3"]
A_VALUES = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
EPSP = np.logspace(-8, -6, 25)  # window fixed in the *new* chart


def slopes_at(p, a, epsp=None):
    """Slope vector measured against the chart eps' , where eps = eps'^a.

    The window in eps' is held fixed, so different a interrogate different
    physical windows -- this is what puts P2 at risk.
    """
    epsp = EPSP if epsp is None else epsp
    eps = epsp**a
    D = 1e-8 * _dphi(y_star(p, eps[0]), p, eps[0], 2) * y_star(p, eps[0]) ** 2
    obs = germ_observables(p, eps, D)
    y = {k: log_slope(epsp, v) for k, v in obs.items()}
    # chart-derivative observable, excluded by the derivation's hypothesis
    lam = obs["lambda"]
    chi = a * epsp ** (a - 1.0) / lam
    y["chi"] = log_slope(epsp, chi)
    return y, D


# ------------------------------------------------------- P1 (identity)

def p1_exact_powers():
    exact = {"o1": 1 / 3, "o2": 2 / 3, "o3": -2 / 3, "o4": 4 / 3, "o5": 1 / 3}
    rows, ratio_dev = [], []
    for a in A_VALUES:
        eps = EPSP**a
        meas = {k: log_slope(EPSP, eps**v) for k, v in exact.items()}
        err = max(abs(meas[k] - a * v) for k, v in exact.items())
        r = meas["o2"] / meas["o1"]
        ratio_dev.append(abs(r - 2.0))
        rows.append({"a": a, "max_slope_err": err, "ratio_o2_o1": r})
    return {"rows": rows, "max_ratio_dev": max(ratio_dev),
            "max_slope_err": max(r["max_slope_err"] for r in rows)}


# --------------------------------------------- P2 / P2b / P3 (at risk)

def p2_p3(p):
    data = {a: slopes_at(p, a) for a in A_VALUES}
    y = {a: d[0] for a, d in data.items()}

    weights = {}
    for k in OBS + ["chi"]:
        av = np.array(A_VALUES)
        vv = np.array([y[a][k] for a in A_VALUES])
        weights[k] = log_slope(av, vv)

    ratio = {a: y[a]["lambda"] / y[a]["y_star"] for a in A_VALUES}
    bare = [y[a]["lambda"] for a in A_VALUES]
    bare_span = max(abs(b) for b in bare) / min(abs(b) for b in bare)

    # P3: do the slope vectors span a line?
    M = np.array([[y[a][k] for k in OBS] for a in A_VALUES])
    sv = np.linalg.svd(M, compute_uv=False)

    # P2b: affine law for the chart-derivative observable
    y_chi_1 = y[1.0]["chi"]
    affine = [{"a": a, "measured": y[a]["chi"], "affine_pred": a * y_chi_1 + (a - 1.0),
               "power_pred": a * y_chi_1} for a in A_VALUES]
    chi_ratio = [y[a]["chi"] / y[a]["y_star"] for a in A_VALUES]

    return {
        "p": p,
        "slopes": {str(a): {k: y[a][k] for k in OBS + ["chi"]} for a in A_VALUES},
        "chi_ratio_values": chi_ratio,
        "y_star_max_in_window": {
            str(a): y_star(p, (EPSP**a)[-1]) for a in A_VALUES},
        "D_used": {str(a): data[a][1] for a in A_VALUES},
        "weights": weights,
        "weight_max_dev": max(abs(weights[k] - 1.0) for k in OBS),
        "ratio_lambda_over_ystar": {str(a): ratio[a] for a in A_VALUES},
        "ratio_target_p_minus_2": p - 2,
        "ratio_max_rel_dev": max(abs(ratio[a] - (p - 2)) / (p - 2) for a in A_VALUES),
        "bare_slope_span": bare_span,
        "singular_values": sv.tolist(),
        "sigma2_over_sigma1": float(sv[1] / sv[0]),
        "n_observables": len(OBS),
        "independent_invariants": len(OBS) - 1,
        "chi_affine": affine,
        "chi_affine_max_err": max(abs(r["measured"] - r["affine_pred"]) for r in affine),
        "chi_power_max_err": max(abs(r["measured"] - r["power_pred"]) for r in affine),
        "chi_weight": weights["chi"],
        # range relative to the a = 1 value; max/min is meaningless here because
        # the ratio changes sign across the a-range
        "chi_ratio_rel_range": float(
            (max(chi_ratio) - min(chi_ratio)) / abs(chi_ratio[A_VALUES.index(1.0)])),
    }


# --------------------------------------------------------- P4 (control)

def p4_independent_charts():
    ps = [4, 6, 8]
    triples = [(0.7, 1.0, 1.6), (1.2, 0.8, 1.0), (1.0, 1.5, 0.6),
               (0.9, 1.1, 2.0), (1.4, 0.7, 0.9), (0.6, 1.3, 1.2)]

    def vec(a3):
        out = []
        for p, a in zip(ps, a3):
            eps = EPSP**a
            ys = np.array([y_star(p, e) for e in eps])
            out.append(log_slope(EPSP, ys))
        for p, a in zip(ps, a3):
            eps = EPSP**a
            lam = np.array([_dphi(y_star(p, e), p, e, 2) for e in eps])
            out.append(log_slope(EPSP, lam))
        return out

    M = np.array([vec(t) for t in triples])
    sv = np.linalg.svd(M, compute_uv=False)
    r21 = M[:, 4] / M[:, 3]  # lambda_2 slope over lambda_1 slope
    # the same three directions, now sharing one chart
    Mc = np.array([vec((a, a, a)) for a in A_VALUES])
    svc = np.linalg.svd(Mc, compute_uv=False)
    return {
        "independent": {
            "singular_values": sv.tolist(),
            "sigma2_over_sigma1": float(sv[1] / sv[0]),
            "ratio_lam2_over_lam1": r21.tolist(),
            "ratio_span": float(max(r21) / min(r21)),
            "all_signs_positive": bool(np.all(M > 0)),
        },
        "common_a": {
            "singular_values": svc.tolist(),
            "sigma2_over_sigma1": float(svc[1] / svc[0]),
        },
    }


# ------------------------------------------------ M-B: the two-term potential

def _kurt_pure(q):
    return math.gamma(5 / q) * math.gamma(1 / q) / math.gamma(3 / q) ** 2 - 3.0


def kurtosis_two_term(A, B, q1, q2, D, nodes=1200):
    s = min((D / A) ** (1.0 / q1), (D / B) ** (1.0 / q2))
    Y = 40.0 * s
    x, wt = gl(nodes)
    t = 0.5 * Y * (x + 1.0)
    w = 0.5 * Y * wt
    e = (A * t**q1 + B * t**q2) / D
    rho = np.exp(-(e - e.min())) * w
    z = rho.sum()
    m2 = (t**2 * rho).sum() / z
    m4 = (t**4 * rho).sum() / z
    return m4 / m2**2 - 3.0


def A_crit(q1, q2, D, B=1.0):
    target = 0.5 * (_kurt_pure(q1) + _kurt_pure(q2))
    lo, hi = -60.0, 20.0
    f = lambda la: kurtosis_two_term(math.exp(la), B, q1, q2, D) - target
    flo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (f(mid) < 0) == (flo < 0):
            lo = mid
        else:
            hi = mid
    return math.exp(0.5 * (lo + hi))


D_GRID = np.logspace(-8, -4, 9)


def support_residue(q1, q2):
    Ac = np.array([A_crit(q1, q2, D) for D in D_GRID])
    return residue(Ac, D_GRID), Ac


# ------------------------------------------------ M-C: the branching scheme

def scheme_obs(n, b2g, N):
    """ln B and ln V at level count N, V from the exact finite sum."""
    x = n * b2g
    N = np.asarray(N, float)
    lnB = N * math.log(n)
    if abs(x - 1.0) < 1e-12:
        lnS = np.log(N + 1.0)
    elif x < 1.0:
        lnS = np.log1p(-x ** (N + 1.0)) - math.log1p(-x)
    else:
        lnS = (N + 1.0) * math.log(x) + np.log1p(-x ** (-(N + 1.0))) - math.log(x - 1.0)
    lnV = -N * math.log(b2g) + lnS
    return lnB, lnV


def scheme_theta(n, b2g, N):
    lnB, lnV = scheme_obs(n, b2g, N)
    A = np.vstack([lnV, np.ones_like(lnV)]).T
    return float(np.linalg.lstsq(A, lnB, rcond=None)[0][0])


# ----------------------------------------------------------------- P5

def p5():
    out = {"a_germ": [], "b_support": [], "c_scheme": []}

    for p in (4, 6):
        eps = np.logspace(-10, -8, 25)
        ys = np.array([y_star(p, e) for e in eps])
        lam = np.array([_dphi(y, p, e, 2) for y, e in zip(ys, eps)])
        out["a_germ"].append({"p": p, "measured": residue(ys, lam),
                              "predicted": 1.0 / (p - 2)})

    for q1, q2 in [(2, 4), (1, 2), (2, 6), (1, 3)]:
        m, Ac = support_residue(q1, q2)
        out["b_support"].append({"q1": q1, "q2": q2, "measured": m,
                                 "predicted": 1.0 - q1 / q2,
                                 "A_c": Ac.tolist()})

    Ns = np.arange(20.0, 31.0)
    for n in range(2, 11):
        b2g = n ** (-1.0 / 2.0) ** 1 * 0  # placeholder replaced below
        b2g = (n ** -0.5) ** 2 * n ** (-1.0 / 3.0)
        out["c_scheme"].append({"n": n, "measured": scheme_theta(n, b2g, Ns),
                                "predicted": 0.75})

    # coarse-graining the scheme by a levels
    n0 = 4
    b2g0 = (n0**-0.5) ** 2 * n0 ** (-1.0 / 3.0)
    cg = []
    for a in range(1, 9):
        na, ba = n0**a, b2g0**a
        th = scheme_theta(na, ba, Ns / a)
        cg.append({"a": a, "theta": th, "per_level_slope": math.log(na)})
    out["c_coarse_grain"] = cg
    out["c_theta_spread"] = max(c["theta"] for c in cg) - min(c["theta"] for c in cg)
    out["c_bare_span"] = cg[-1]["per_level_slope"] / cg[0]["per_level_slope"]
    return out


# ----------------------------------------------------------------- P6

def p6():
    q1, q2 = 2.0, 2.0 * math.pi
    m_supp, _ = support_residue(q1, q2)
    p = 2.0 + math.sqrt(2.0)
    eps = np.logspace(-10, -8, 25)
    ys = np.array([y_star(p, e) for e in eps])
    lam = np.array([_dphi(y, p, e, 2) for y, e in zip(ys, eps)])
    return {
        "support": {"q1": q1, "q2": q2, "measured": m_supp,
                    "predicted": 1.0 - 1.0 / math.pi},
        "germ": {"p": p, "measured": residue(ys, lam),
                 "predicted": 1.0 / math.sqrt(2.0)},
    }


# ----------------------------------------------------------------- P7

def p7():
    n = 4
    Ns = np.arange(200.0, 401.0)
    lnx = np.linspace(-0.7, 0.55, 251)
    xs = np.exp(lnx)

    def theta_of_x(x, a=1):
        # beta = n^{-1/2} so b2g = gamma/n and x = gamma; coarse-grain by a
        b2g = x / n
        return scheme_theta(n**a, b2g**a, Ns / a)

    meas = np.array([theta_of_x(x) for x in xs])
    pred = np.array([min(1.0, math.log(n) / (-math.log(x / n))) for x in xs])
    far = np.abs(lnx) > 0.05
    rms = float(np.sqrt(np.mean((meas[far] - pred[far]) ** 2)))

    def kink(vals):
        # d2[j] is the curvature at lnx[j+1]; the parabolic refinement must be
        # centred on the argmax itself, not offset by the index shift.
        d2 = np.abs(np.diff(vals, 2))
        j = int(np.argmax(d2))
        j = min(max(j, 1), len(d2) - 2)
        y0, y1, y2 = d2[j - 1], d2[j], d2[j + 1]
        denom = y0 - 2 * y1 + y2
        shift = 0.5 * (y0 - y2) / denom if denom != 0 else 0.0
        h = lnx[1] - lnx[0]
        return float(lnx[j + 1] + shift * h)

    lnxc = kink(meas)
    cg = []
    for a in (1, 2, 4, 8):
        m = np.array([theta_of_x(x, a) for x in xs])
        lc = kink(m)
        cg.append({"a": a, "ln_x_c": lc, "x_c": math.exp(lc),
                   "per_level_slope": a * math.log(n)})
    return {
        "rms_vs_min_form": rms,
        "x_c": math.exp(lnxc),
        "theta_at_x_gt_1": float(np.mean(meas[lnx > 0.15])),
        "coarse_grain": cg,
        "x_c_spread": max(c["x_c"] for c in cg) - min(c["x_c"] for c in cg),
        "bare_span": cg[-1]["per_level_slope"] / cg[0]["per_level_slope"],
    }


# ------------------------------------------------- POST-HOC DIAGNOSTICS
#
# NOT registered. Three legs missed their registered tolerances (P2's ratio at
# p = 6, P5c's coarse-graining, P7's kink location). Each miss is either the
# claim failing or the finite-window / finite-grid error budget the
# registration named in section 5. Those are distinguishable, because the
# second one makes a prediction: the deviation must shrink at a stated rate as
# the window deepens or the grid refines. If it does not, the leg has failed
# for real. Reported separately and never counted as a pass.


def diag_window(p):
    """Does P2's ratio deviation track the window's distance from the point?

    Corrections to scaling enter Phi at relative order C3*y*, so the deviation
    should fall roughly in proportion to y* at the top of the window.
    """
    rows = []
    for top in (-4, -6, -8, -10, -12):
        epsp = np.logspace(top - 2, top, 25)
        y, _ = slopes_at(p, 1.0, epsp)
        r = y["lambda"] / y["y_star"]
        rows.append({"window_top_log10": top,
                     "y_star_max": y_star(p, epsp[-1]),
                     "ratio": r,
                     "rel_dev": abs(r - (p - 2)) / (p - 2)})
    return rows


def diag_scheme_N(n=4):
    """Does P5c's coarse-graining spread fall as the level window deepens?"""
    b2g = (n**-0.5) ** 2 * n ** (-1.0 / 3.0)
    x = n * b2g
    rows = []
    for lo in (20.0, 50.0, 100.0, 200.0, 400.0):
        Ns = np.arange(lo, lo + 11.0)
        th = [scheme_theta(n**a, b2g**a, Ns / a) for a in range(1, 9)]
        rows.append({"N_lo": lo, "spread": max(th) - min(th),
                     "x_pow_N": x**lo})
    return rows


def diag_kink_grid():
    """Does P7's kink locate at x = 1 once grid and level window are refined?

    The kink is intrinsically rounded over |ln x| ~ 1/N, so the locator cannot
    beat that; the prediction is that x_c -> 1 as N grows and the grid refines.
    """
    n = 4
    rows = []
    for npts, Nlo, Nhi in ((251, 200, 400), (501, 500, 1000),
                           (1001, 1500, 3000), (2001, 4000, 8000)):
        Ns = np.linspace(Nlo, Nhi, 60)
        lnx = np.linspace(-0.7, 0.55, npts)
        meas = np.array([scheme_theta(n, math.exp(v) / n, Ns) for v in lnx])
        d2 = np.abs(np.diff(meas, 2))
        j = int(np.argmax(d2))
        j = min(max(j, 1), len(d2) - 2)
        y0, y1, y2 = d2[j - 1], d2[j], d2[j + 1]
        den = y0 - 2 * y1 + y2
        h = lnx[1] - lnx[0]
        lc = lnx[j + 1] + (0.5 * (y0 - y2) / den if den != 0 else 0.0) * h
        rows.append({"n_grid": npts, "N_lo": Nlo, "grid_h": h,
                     "rounding_scale_1_over_N": 1.0 / Nlo,
                     "x_c": math.exp(lc), "abs_err": abs(math.exp(lc) - 1.0)})
    return rows


# ----------------------------------------------------------------- main

if __name__ == "__main__":
    np.random.seed(SEED)
    OUT["seed"] = SEED
    print("P1 ...", flush=True)
    OUT["P1_identity_exact_powers"] = p1_exact_powers()
    print("P2/P3 ...", flush=True)
    OUT["P2_P3_p4"] = p2_p3(4)
    OUT["P2_P3_p6"] = p2_p3(6)
    print("P4 ...", flush=True)
    OUT["P4_control_independent_charts"] = p4_independent_charts()
    print("P5 ...", flush=True)
    OUT["P5_one_estimator"] = p5()
    print("P6 ...", flush=True)
    OUT["P6_not_discrete"] = p6()
    print("P7 ...", flush=True)
    OUT["P7_kink"] = p7()
    print("diagnostics (post-hoc, not registered) ...", flush=True)
    OUT["POSTHOC_diagnostics"] = {
        "_note": "not registered; these exist only to separate a failed claim "
                 "from the finite-window error budget named in the "
                 "registration section 5. Never counted as a pass.",
        "window_dependence_p4": diag_window(4),
        "window_dependence_p6": diag_window(6),
        "scheme_N_dependence": diag_scheme_N(),
        "kink_grid_refinement": diag_kink_grid(),
    }

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2)

    r4, r6 = OUT["P2_P3_p4"], OUT["P2_P3_p6"]
    print("\n--- summary ---")
    print(f"P1  max slope err {OUT['P1_identity_exact_powers']['max_slope_err']:.2e}")
    for r in (r4, r6):
        print(f"P2  p={r['p']}: weights {[round(r['weights'][k], 4) for k in OBS]} "
              f"max|w-1|={r['weight_max_dev']:.4f}")
        print(f"    ratio -> {r['ratio_target_p_minus_2']}: "
              f"max rel dev {r['ratio_max_rel_dev']:.4%}, bare span {r['bare_slope_span']:.2f}x")
        print(f"P2b chi weight {r['chi_weight']:.4f}; affine err {r['chi_affine_max_err']:.2e}, "
              f"power err {r['chi_power_max_err']:.3f}, "
              f"ratio rel range {r['chi_ratio_rel_range']:.2f}")
        print(f"P3  sigma2/sigma1 = {r['sigma2_over_sigma1']:.2e} -> "
              f"{r['independent_invariants']} invariants from n={r['n_observables']}")
    p4o = OUT["P4_control_independent_charts"]
    print(f"P4  independent s2/s1 {p4o['independent']['sigma2_over_sigma1']:.3f}, "
          f"ratio span {p4o['independent']['ratio_span']:.2f}x | "
          f"common-a s2/s1 {p4o['common_a']['sigma2_over_sigma1']:.2e}")
    p5o = OUT["P5_one_estimator"]
    for r in p5o["a_germ"]:
        print(f"P5a p={r['p']}: {r['measured']:.4f} vs {r['predicted']:.4f}")
    for r in p5o["b_support"]:
        print(f"P5b ({r['q1']},{r['q2']}): {r['measured']:.4f} vs {r['predicted']:.4f}")
    print(f"P5c theta n=2..10: "
          f"{[round(r['measured'], 4) for r in p5o['c_scheme']]}")
    print(f"    coarse-grain spread {p5o['c_theta_spread']:.2e}, "
          f"bare span {p5o['c_bare_span']:.1f}x")
    print(f"P6  support {OUT['P6_not_discrete']['support']['measured']:.5f} vs "
          f"{OUT['P6_not_discrete']['support']['predicted']:.5f}; "
          f"germ {OUT['P6_not_discrete']['germ']['measured']:.5f} vs "
          f"{OUT['P6_not_discrete']['germ']['predicted']:.5f}")
    p7o = OUT["P7_kink"]
    print(f"P7  rms vs min-form {p7o['rms_vs_min_form']:.2e}, x_c {p7o['x_c']:.5f}, "
          f"theta(x>1) {p7o['theta_at_x_gt_1']:.5f}, x_c spread {p7o['x_c_spread']:.2e}, "
          f"bare span {p7o['bare_span']:.1f}x")
    dg = OUT["POSTHOC_diagnostics"]
    print("\n--- post-hoc diagnostics (not registered) ---")
    for tag in ("window_dependence_p4", "window_dependence_p6"):
        print(f"{tag}: " + ", ".join(
            f"y*max={r['y_star_max']:.1e}->{r['rel_dev']:.2%}" for r in dg[tag]))
    print("scheme N: " + ", ".join(
        f"N={int(r['N_lo'])}->{r['spread']:.1e}" for r in dg["scheme_N_dependence"]))
    print("kink grid: " + ", ".join(
        f"N={r['N_lo']}->x_c={r['x_c']:.5f}" for r in dg["kink_grid_refinement"]))
