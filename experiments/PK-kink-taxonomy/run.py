#!/usr/bin/env python3
"""
P-K — three kinds of kink, and which one P-D's is.

Settles the item PC-variational-kinds left open (and FLOORS §4 flagged twice):
is P-D's non-analyticity at n*beta^2*gamma = 1 a selector cell boundary, or a
floor-3 non-analyticity?

  type L  limit kink     analytic at finite N; sharp only in a limit; width -> 0
  type C  crossing kink  non-analytic already; width exactly 0 at every size
  type X  branch point   one-sided slope diverges; exponent 1/2, not 1

Legs
  A  allometry: the exact finite-N law, the scaling collapse, the width    P1 P2 P3
  B  a two-state first-order transition -- independent type-L control      P4
  C  the divide-and-conquer selector boundary -- type C                    P5
  D  the P-C stability boundary -- type X                                  P6
  E  M/M/1 -- the null control, no kink to find                            P7
  F  the P-C P8 repair: a cleanly parameterised cost model                 P8

Pure numpy + scipy. Deterministic. Writes verdict.json.
"""

import json
import math
import time

import numpy as np
from scipy.optimize import brentq
from scipy.special import logsumexp

SEED = 20260728
OUT = {}
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def rec(k, v):
    OUT[k] = v


def fit_slope(x, y):
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


# ----------------------------------------------------------------------------
# the instrument: rounding width of a kink in a readout f(t)
# ----------------------------------------------------------------------------

def kink_width(f, t_c, half_span=2.0, m=4001):
    """FWHM of |f''| around t_c, plus the one-sided slopes.

    Returns None when |f''| has no interior peak -- i.e. no kink to fit.
    """
    t = np.linspace(t_c - half_span, t_c + half_span, m)
    y = np.array([f(v) for v in t])
    h = t[1] - t[0]
    d2 = np.abs(y[2:] - 2 * y[1:-1] + y[:-2]) / h ** 2
    tt = t[1:-1]
    i = int(np.argmax(d2))
    if i <= 1 or i >= len(d2) - 2:
        return None                                  # peak at the edge: no locus
    peak = d2[i]
    if not np.isfinite(peak) or peak <= 0:
        return None
    half = peak / 2.0
    above = np.where(d2 >= half)[0]
    if above.size == 0:
        return None
    w = float(tt[above[-1]] - tt[above[0]] + h)
    # one-sided slopes measured well outside the rounded region
    off = max(4 * w, 20 * h)
    sl = (f(t_c - off) - f(t_c - 2 * off)) / off
    sr = (f(t_c + 2 * off) - f(t_c + off)) / off
    return dict(width=w, peak_curvature=float(peak), peak_at=float(tt[i]),
                slope_left=float(sl), slope_right=float(sr),
                slope_gap_rel=float(abs(sl - sr) / max(abs(sl), abs(sr), 1e-300)))


# ============================================================================
# LEG A — allometry                                              P1 P2 P3
# ============================================================================

def theta_exact(N, n, beta, gamma):
    """Closed form for d ln B / d ln M at continuous depth N (derived in §2)."""
    y = 1.0 / (n * beta ** 2 * gamma)
    u = (N + 1) * math.log(y)
    g = 1.0 if abs(u) < 1e-9 else u / (1.0 - math.exp(-u))
    return math.log(n) / (math.log(n) + g / (N + 1))


def theta_logsumexp(N, n, beta, gamma):
    """d ln B / d ln M by central difference on a direct logsumexp of the sum."""
    def lnM(NN):
        j = np.arange(NN + 1)
        return logsumexp((NN - j) * math.log(n)
                         - 2 * j * math.log(beta) - j * math.log(gamma))
    return math.log(n) / ((lnM(N + 1) - lnM(N - 1)) / 2.0)


def theta_window(n, beta, gamma, Ns):
    """P-D's own estimator: polyfit of ln B on ln M over a window of depths."""
    def lnM(NN):
        j = np.arange(NN + 1)
        return logsumexp((NN - j) * math.log(n)
                         - 2 * j * math.log(beta) - j * math.log(gamma))
    lm = np.array([lnM(N) for N in Ns])
    lb = np.array([N * math.log(n) for N in Ns])
    return float(np.polyfit(lm, lb, 1)[0])


def g_scaling(u):
    return 1.0 if abs(u) < 1e-9 else u / (1.0 - math.exp(-u))


def leg_A():
    say("\n=== LEG A — allometry: is the kink rounded at finite N? ===")
    n = 4
    gamma = 4 ** (-1 / 3)
    out = {}

    def beta_of(x):                       # x = n*beta^2*gamma
        return math.sqrt(x / (n * gamma))

    # ---- P1 (identity): closed form vs direct logsumexp --------------------
    errs = []
    for N in (50, 200):
        for x in (0.7, 0.95, 1.0, 1.05, 1.4):
            b = beta_of(x)
            errs.append(abs(theta_exact(N, n, b, gamma) - theta_logsumexp(N, n, b, gamma)))
    out["P1"] = dict(max_abs_err=float(max(errs)), cases=len(errs))
    out["P1_pass"] = bool(max(errs) <= 1e-7)
    say(f"  P1 (identity) closed form vs logsumexp: max |err| = {max(errs):.2e}  "
        f"pass={out['P1_pass']}")

    # ---- P2 (AT RISK): does P-D's own window estimator collapse? -----------
    Ns = list(range(200, 301, 10))
    Nbar = float(np.mean(Ns))
    devs, pts = [], []
    for x in np.linspace(0.90, 1.12, 25):
        b = beta_of(x)
        th = theta_window(n, b, gamma, Ns)
        u = -(Nbar + 1) * math.log(x)
        lhs = (Nbar + 1) * math.log(n) * (1.0 / th - 1.0)
        devs.append(abs(lhs - g_scaling(u)))
        pts.append(dict(x=float(x), u=float(u), lhs=float(lhs), g=float(g_scaling(u))))
    out["P2"] = dict(max_dev=float(max(devs)), median_dev=float(np.median(devs)),
                     Nbar=Nbar, points=pts)
    out["P2_pass"] = bool(max(devs) <= 5e-3)
    say(f"  P2 (AT RISK) P-D's window estimator collapses onto g(u): max dev "
        f"{max(devs):.2e}  [registered <= 5e-3]  pass={out['P2_pass']}")

    # ---- P3 (identity): rounding width vs N --------------------------------
    Nlist = [20, 40, 80, 160, 320, 640, 1280, 2560, 5120]
    widths, curvs = [], []
    for N in Nlist:
        f = lambda t: theta_exact(N, n, beta_of(math.exp(t)), gamma)   # t = ln x
        k = kink_width(f, 0.0, half_span=min(2.0, 60.0 / N))
        widths.append(k["width"])
        curvs.append(k["peak_curvature"])
    slope = fit_slope(np.array(Nlist, float), np.array(widths))
    out["P3"] = dict(N=Nlist, widths=[float(w) for w in widths],
                     peak_curvatures=[float(c) for c in curvs],
                     width_exponent=slope,
                     curvature_exponent=fit_slope(np.array(Nlist, float), np.array(curvs)))
    out["P3_pass"] = bool(abs(slope + 1.0) <= 0.03)
    say(f"  P3 (identity) width ~ N^{slope:.4f}  [registered -1.00 +- 0.03]  "
        f"pass={out['P3_pass']}")

    # ---- interpretation check: Murray <=> equipartition of volume ----------
    lev = {}
    for label, x in (("Murray (n b^2 g = 1)", 1.0), ("off-Murray (0.8)", 0.8),
                     ("off-Murray (1.25)", 1.25)):
        b = beta_of(x)
        N = 12
        j = np.arange(N + 1)
        terms = (N - j) * math.log(n) - 2 * j * math.log(b) - j * math.log(gamma)
        terms = np.exp(terms - terms.max())
        lev[label] = dict(rel_spread=float(terms.max() / terms.min()))
    out["murray_equipartition"] = lev
    say(f"  [interp] volume across generations, max/min ratio: "
        f"Murray {lev['Murray (n b^2 g = 1)']['rel_spread']:.6f}, "
        f"off {lev['off-Murray (0.8)']['rel_spread']:.1f} / "
        f"{lev['off-Murray (1.25)']['rel_spread']:.1f}")

    # ---- POST-HOC (P1, P2 both failed as registered) -----------------------
    # P1: is the 1.8e-6 gap the closed form being wrong, or my checker's
    # truncation error? A 2-point central difference in N has O(h^2 f''') error
    # with h = 1. If the gap shrinks with stencil order, the checker was crude.
    def lnM(NN, b, g):
        j = np.arange(NN + 1)
        return logsumexp((NN - j) * math.log(n) - 2 * j * math.log(b) - j * math.log(g))

    e2, e5 = [], []
    for N in (50, 200):
        for x in (0.7, 0.95, 1.0, 1.05, 1.4):
            b = beta_of(x)
            d2 = (lnM(N + 1, b, gamma) - lnM(N - 1, b, gamma)) / 2.0
            d5 = (-lnM(N + 2, b, gamma) + 8 * lnM(N + 1, b, gamma)
                  - 8 * lnM(N - 1, b, gamma) + lnM(N - 2, b, gamma)) / 12.0
            th = theta_exact(N, n, b, gamma)
            e2.append(abs(th - math.log(n) / d2))
            e5.append(abs(th - math.log(n) / d5))
    # P2: does the deviation track the WIDTH of P-D's fitting window?
    win_sweep = []
    for half in (5, 10, 25, 50):
        Ns_w = list(range(250 - half, 251 + half, max(1, half // 5)))
        Nb = float(np.mean(Ns_w))
        dv = []
        for x in np.linspace(0.90, 1.12, 25):
            th = theta_window(n, beta_of(x), gamma, Ns_w)
            dv.append(abs((Nb + 1) * math.log(n) * (1 / th - 1)
                          - g_scaling(-(Nb + 1) * math.log(x))))
        win_sweep.append(dict(half_width=half, max_dev=float(max(dv))))

    out["posthoc"] = dict(
        P1_err_2point=float(max(e2)), P1_err_5point=float(max(e5)),
        P1_diagnosis=("the gap is the checker's finite-difference truncation error, "
                      "not the closed form: a 5-point stencil shrinks it by the "
                      "order the truncation predicts"),
        P2_window_sweep=win_sweep,
        P2_diagnosis=("P-D's estimator fits a slope over a window of depths, and u "
                      "depends on N, so the window smears the collapse; the "
                      "deviation tracks the window half-width"),
    )
    say(f"  [post-hoc] P1 err: 2-point {max(e2):.2e} -> 5-point {max(e5):.2e}")
    say(f"  [post-hoc] P2 deviation vs window half-width: "
        f"{[(w['half_width'], round(w['max_dev'], 5)) for w in win_sweep]}")

    rec("legA", out)
    return out


# ============================================================================
# LEG B — an independent type-L control                                   P4
# ============================================================================

def leg_B():
    say("\n=== LEG B — two-state first-order transition (independent type L) ===")
    # free energy per site: -(1/N) ln( e^{-N f1} + e^{-N f2} ),  f1 = 0, f2 = t
    out = {}
    Nlist = [20, 40, 80, 160, 320, 640, 1280, 2560, 5120]
    widths = []
    for N in Nlist:
        def f(t, N=N):
            return -(1.0 / N) * logsumexp([0.0, -N * t])
        k = kink_width(f, 0.0, half_span=min(2.0, 60.0 / N))
        widths.append(k["width"])
    slope = fit_slope(np.array(Nlist, float), np.array(widths))

    # normalised scaling functions, compared in sup-norm
    us = np.linspace(-8, 8, 801)
    g_norm = np.array([g_scaling(u) - max(u, 0.0) for u in us])      # allometry
    h_norm = np.array([math.log(1 + math.exp(-abs(u))) for u in us])  # two-state
    # both -> 0 at |u| -> inf; normalise to unit value at u = 0
    g_norm = g_norm / g_norm[len(us) // 2]
    h_norm = h_norm / h_norm[len(us) // 2]
    supdiff = float(np.max(np.abs(g_norm - h_norm)))

    out["P4"] = dict(N=Nlist, widths=[float(w) for w in widths],
                     width_exponent=slope, scaling_sup_diff=supdiff)
    out["P4a_pass"] = bool(abs(slope + 1.0) <= 0.03)
    out["P4b_pass"] = bool(supdiff >= 0.05)
    say(f"  P4a (identity) width ~ N^{slope:.4f}  pass={out['P4a_pass']}")
    say(f"  P4b (AT RISK) scaling functions differ in sup-norm by {supdiff:.4f}  "
        f"[registered >= 0.05]  pass={out['P4b_pass']}")
    rec("legB", out)
    return out


# ============================================================================
# LEG C — the selector boundary is type C                                 P5
# ============================================================================

SCHEMES = [("schoolbook", 4, 2, 3.0), ("karatsuba", 3, 2, 4.0),
           ("toom3", 5, 3, 8.0), ("toom4", 7, 4, 15.0)]


def dc_cost(scheme, N, c_lin, c_call, c_mul, n_base):
    _, a, b, alpha = scheme
    total, nn, mult = 0.0, float(N), 1.0
    for _ in range(200):
        if nn <= n_base:
            break
        total += mult * (c_lin * alpha * nn + c_call * a)
        mult *= a
        nn /= b
    return total + mult * c_mul * nn * nn


def leg_C():
    say("\n=== LEG C — the divide-and-conquer selector boundary (type C) ===")
    out = {"per_size": []}
    c_call, c_mul, n_base = 20.0, 1.0, 32.0
    for e in range(10, 19):
        N = 2 ** e

        def vstar(t):                      # t = ln c_lin
            c = math.exp(t)
            return math.log(min(dc_cost(s, N, c, c_call, c_mul, n_base) for s in SCHEMES))

        def winner(t):
            c = math.exp(t)
            return int(np.argmin([dc_cost(s, N, c, c_call, c_mul, n_base) for s in SCHEMES]))

        grid = np.linspace(-8, 6, 3001)
        w = np.array([winner(t) for t in grid])
        idx = np.where(np.diff(w) != 0)[0]
        if idx.size == 0:
            out["per_size"].append(dict(N=N, crossing=None))
            continue
        lo, hi = grid[idx[0]], grid[idx[0] + 1]
        w_lo = winner(lo)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if winner(mid) == w_lo:
                lo = mid
            else:
                hi = mid
        tc = 0.5 * (lo + hi)
        k = kink_width(vstar, tc, half_span=1.0)
        eps = 1e-4
        sl = (vstar(lo) - vstar(lo - eps)) / eps
        sr = (vstar(hi + eps) - vstar(hi)) / eps
        out["per_size"].append(dict(
            N=N, crossing=float(tc),
            value_jump=float(abs(vstar(hi) - vstar(lo))),
            slope_gap_rel=float(abs(sl - sr) / max(abs(sl), abs(sr))),
            instrument_width=(None if k is None else k["width"]),
        ))

    got = [r for r in out["per_size"] if r.get("crossing") is not None]
    gaps = [r["slope_gap_rel"] for r in got]
    jumps = [r["value_jump"] for r in got]
    Ns = np.array([r["N"] for r in got], float)
    gap_exp = fit_slope(Ns, np.array(gaps))
    out["P5"] = dict(sizes=len(got), slope_gap_min=float(min(gaps)),
                     slope_gap_exponent=gap_exp, value_jump_max=float(max(jumps)))
    out["P5_pass"] = bool(len(got) >= 8 and abs(gap_exp) <= 0.02
                          and max(jumps) <= 1e-12 and min(gaps) >= 0.05)
    say(f"  P5 (AT RISK) over {len(got)} operating sizes: slope gap does not shrink "
        f"(exponent {gap_exp:+.4f}, min gap {min(gaps):.3f}), value continuous to "
        f"{max(jumps):.1e}  pass={out['P5_pass']}")

    # ---- POST-HOC: I registered the wrong statistic ------------------------
    # Type L vs type C is a claim about the WIDTH, not about the slope gap.
    # The instrument's width here is pinned at its own grid resolution
    # (2*half_span/m), i.e. no intrinsic width at all, at every size.
    ws = [r["instrument_width"] for r in got if r["instrument_width"] is not None]
    floor = 2 * 1.0 / 4000
    out["posthoc"] = dict(
        instrument_widths=[float(w) for w in ws],
        resolution_floor=float(floor),
        widths_at_floor=bool(all(abs(w - floor) <= 1e-9 * max(1.0, abs(w)) for w in ws)),
        width_ratio_max_over_min=float(max(ws) / min(ws)) if ws else None,
        diagnosis=("the registered statistic was the slope gap, but type L vs "
                   "type C is a claim about the width: the width is pinned at "
                   "the instrument's own resolution floor at every operating "
                   "size, while legs A and B sit far above it and shrink"),
    )
    say(f"  [post-hoc] instrument width at every size = {ws[0]:.1e} = its own "
        f"resolution floor ({floor:.1e}); max/min = "
        f"{out['posthoc']['width_ratio_max_over_min']:.6f}")
    rec("legC", out)
    return out


# ============================================================================
# LEG D — the P-C stability boundary is type X                            P6
# ============================================================================

def leg_D():
    say("\n=== LEG D — the P-C stability boundary (type X: branch point) ===")
    rng = np.random.default_rng(SEED)
    out = {}
    for n in (2, 6):
        exps = []
        tried = 0
        while len(exps) < 40 and tried < 4000:
            tried += 1
            g = rng.normal(0, 1 / math.sqrt(n), (n, n))
            S = 0.5 * (g + g.T)
            S /= np.linalg.norm(S)
            h = rng.normal(0, 1 / math.sqrt(n), (n, n))
            A = 0.5 * (h - h.T)
            A /= np.linalg.norm(A)
            if np.linalg.eigvalsh(S).min() > 0:
                continue

            def minre(a):
                return np.linalg.eigvals(S + a * A).real.min()

            if minre(1e-6) > 0 or minre(1e4) < 0:
                continue
            a_c = brentq(minre, 1e-6, 1e4, xtol=1e-14, rtol=1e-15)
            ds = np.geomspace(1e-6, 1e-3, 25) * a_c
            ys = np.array([minre(a_c + d) for d in ds])
            if np.any(ys <= 0):
                continue
            exps.append(fit_slope(ds, ys))
        out[f"n={n}"] = dict(cases=len(exps), exponent_median=float(np.median(exps)),
                             exponent_iqr=float(np.subtract(*np.percentile(exps, [75, 25]))))
        say(f"  n={n}: min Re lambda ~ (a - a_c)^{np.median(exps):.4f}  "
            f"(IQR {out[f'n={n}']['exponent_iqr']:.4f}, {len(exps)} cases)")
    out["P6a_pass"] = bool(abs(out["n=2"]["exponent_median"] - 0.5) <= 0.02)
    out["P6b_pass"] = bool(abs(out["n=6"]["exponent_median"] - 0.5) <= 0.02)
    say(f"  P6a (identity) pass={out['P6a_pass']}   "
        f"P6b (AT RISK, 0.5 vs the alternative 1.0) pass={out['P6b_pass']}")

    # ---- POST-HOC: P6a was a WRONG identity, and type X is not exhibited ----
    # I registered 1/2 from "the quadratic formula", conflating the
    # DISCRIMINANT (eigenvalue collision, exponent 1/2) with the DETERMINANT
    # (which is what the stability boundary actually is). det J = 0 means one
    # real eigenvalue crossing zero transversally: exponent 1, and min Re lambda
    # is ANALYTIC there -- no kink of any kind.
    rng2 = np.random.default_rng(SEED + 99)
    checks = []
    while len(checks) < 20:
        g = rng2.normal(0, 1 / math.sqrt(2), (2, 2))
        S = 0.5 * (g + g.T)
        S /= np.linalg.norm(S)
        h = rng2.normal(0, 1 / math.sqrt(2), (2, 2))
        A = 0.5 * (h - h.T)
        A /= np.linalg.norm(A)
        if np.linalg.eigvalsh(S).min() > 0:
            continue

        def minre(a):
            return np.linalg.eigvals(S + a * A).real.min()

        if minre(1e-6) > 0 or minre(1e4) < 0:
            continue
        a_c = brentq(minre, 1e-6, 1e4, xtol=1e-14, rtol=1e-15)
        ev = np.linalg.eigvals(S + a_c * A)
        eps = 1e-5 * a_c
        dl = (minre(a_c) - minre(a_c - eps)) / eps
        dr = (minre(a_c + eps) - minre(a_c)) / eps
        checks.append(dict(
            max_abs_imag_at_ac=float(np.abs(ev.imag).max()),
            det_at_ac=float(abs(np.linalg.det(S + a_c * A))),
            slope_gap_rel=float(abs(dl - dr) / max(abs(dl), abs(dr))),
        ))
    out["posthoc"] = dict(
        eigenvalues_real_at_boundary=float(max(c["max_abs_imag_at_ac"] for c in checks)),
        det_at_boundary_max=float(max(c["det_at_ac"] for c in checks)),
        minre_slope_gap_max=float(max(c["slope_gap_rel"] for c in checks)),
        diagnosis=("P6a was a wrong identity, not a failed measurement: the "
                   "stability boundary is det J = 0 (a real eigenvalue crossing "
                   "zero, exponent 1) and not the discriminant (a collision, "
                   "exponent 1/2). min Re lambda is analytic through it, so the "
                   "P-C boundary is not a kink of any kind and type X is NOT "
                   "exhibited by this family."),
    )
    say(f"  [post-hoc] at a_c: max |Im lambda| = "
        f"{out['posthoc']['eigenvalues_real_at_boundary']:.2e}, |det J| = "
        f"{out['posthoc']['det_at_boundary_max']:.2e}, min-Re one-sided slope gap = "
        f"{out['posthoc']['minre_slope_gap_max']:.2e} -> analytic, no kink")
    rec("legD", out)
    return out


# ============================================================================
# LEG E — the null control                                                P7
# ============================================================================

def leg_E():
    say("\n=== LEG E — M/M/1, the null control (there is no kink) ===")
    # scaled queue length has the exponential shape at every rho: excess kurtosis 6.
    def kurt(t):                       # t = ln(1 - rho)
        rho = 1.0 - math.exp(t)
        # exact geometric moments about the mean, scaled -- shape only
        p = rho
        m1 = p / (1 - p)
        m2 = p * (1 + p) / (1 - p) ** 2
        m3 = p * (1 + 4 * p + p * p) / (1 - p) ** 3
        m4 = p * (1 + 11 * p + 11 * p * p + p ** 3) / (1 - p) ** 4
        c2 = m2 - m1 ** 2
        c3 = m3 - 3 * m1 * m2 + 2 * m1 ** 3
        c4 = m4 - 4 * m1 * m3 + 6 * m1 ** 2 * m2 - 3 * m1 ** 4
        return c4 / c2 ** 2 - 3.0

    ts = np.linspace(-10, -0.5, 400)
    vals = np.array([kurt(t) for t in ts])
    k = kink_width(kurt, -5.0, half_span=4.0)
    out = dict(kurtosis_min=float(vals.min()), kurtosis_max=float(vals.max()),
               kurtosis_spread=float(vals.max() - vals.min()),
               instrument_found_locus=bool(k is not None),
               instrument_detail=k)
    out["P7_pass"] = bool(k is None or k["slope_gap_rel"] < 1e-6)
    say(f"  excess kurtosis over 4 decades of (1-rho): {vals.min():.4f} .. "
        f"{vals.max():.4f}; instrument found a locus: {k is not None}  "
        f"pass={out['P7_pass']}")
    rec("legE", out)
    return out


# ============================================================================
# LEG F — the P-C P8 repair                                               P8
# ============================================================================

def leg_F():
    say("\n=== LEG F — the P-C rank test, cleanly parameterised (P8 repair) ===")
    rng = np.random.default_rng(SEED + 5)
    N_BASE = 32.0                       # a COUNT: excluded from the magnitudes
    MAGS = ["c_lin", "c_call", "c_fix", "c_log", "c_mul"]
    LO = np.array([3e-3, 0.2, 0.05, 0.02, 1e-2])
    HI = np.array([30.0, 2000.0, 500.0, 200.0, 1e2])
    sizes = [2 ** e for e in (10, 11, 12, 13, 14, 15)]

    def cost5(scheme, N, m):
        _, a, b, alpha = scheme
        c_lin, c_call, c_fix, c_log, c_mul = m
        total, nn, mult = 0.0, float(N), 1.0
        for _ in range(200):
            if nn <= N_BASE:
                break
            total += mult * (c_lin * alpha * nn + c_call * a + c_fix
                             + c_log * math.log(nn))
            mult *= a
            nn /= b
        return total + mult * c_mul * nn * nn

    def best(N, m):
        cs = [cost5(s, N, m) for s in SCHEMES]
        i = int(np.argmin(cs))
        return i, cs[i]

    def r_exp(m, szs):
        return np.array([math.log(SCHEMES[best(N, m)[0]][1])
                         / math.log(SCHEMES[best(N, m)[0]][2]) for N in szs])

    def r_const(m, szs):
        v = []
        for N in szs:
            i, c = best(N, m)
            v.append(math.log(c) - math.log(SCHEMES[i][1]) / math.log(SCHEMES[i][2])
                     * math.log(N))
        return np.array(v)

    def jac(fn, m, szs, h=1e-4):
        cols = []
        for j in range(len(m)):
            mp, mm = m.copy(), m.copy()
            mp[j] *= math.exp(h)
            mm[j] *= math.exp(-h)
            cols.append((fn(mp, szs) - fn(mm, szs)) / (2 * h))
        return np.stack(cols, axis=1)

    def rank(J, tol=1e-8):
        sv = np.linalg.svd(J, compute_uv=False)
        return (0 if sv[0] == 0 else int((sv > tol * sv[0]).sum())), sv

    u = (rng.permuted(np.tile(np.arange(2000)[:, None], (1, 5)), axis=0)
         + rng.uniform(size=(2000, 5))) / 2000
    pts = np.exp(np.log(LO) + u * (np.log(HI) - np.log(LO)))

    rc, re_, used = [], [], 0
    for m in pts:
        base = best(2 ** 14, m)[0]
        if not all(best(2 ** 14, np.where(np.arange(5) == j, m * math.exp(s * 1e-4), m))[0]
                   == base for j in range(5) for s in (+1, -1)):
            continue
        used += 1
        rc.append(rank(jac(r_const, m, sizes))[0])
        re_.append(rank(jac(r_exp, m, sizes))[0])
        if used >= 150:
            break

    d = 5
    states = rng.normal(size=(40, d))
    lam0 = rng.normal(scale=0.5, size=d)

    def gm(lam):
        lp = states.dot(lam)
        return states.T.dot(np.exp(lp - logsumexp(lp)))

    hh = 1e-5
    Jg = np.stack([(gm(lam0 + hh * np.eye(d)[j]) - gm(lam0 - hh * np.eye(d)[j])) / (2 * hh)
                   for j in range(d)], axis=1)
    rg = rank(Jg)[0]

    out = dict(magnitudes=MAGS, structural_count_excluded="n_base",
               interior_points=used,
               rank_constant_full_frac=float(np.mean([r == 5 for r in rc])),
               rank_constant_mode=int(np.bincount(rc).argmax()),
               rank_exponent_all_zero=bool(all(r == 0 for r in re_)),
               rank_gibbs=int(rg), tolerance=1e-8)
    out["P8_pass"] = bool(out["rank_constant_full_frac"] >= 0.95
                          and out["rank_exponent_all_zero"] and rg == 5)
    say(f"  ranks, one tolerance: exponent={set(re_)}  constant "
        f"{out['rank_constant_mode']}/5 (full in {out['rank_constant_full_frac']:.2f})  "
        f"gibbs={rg}/5")
    say(f"  P8 (AT RISK, the P-C repair) pass={out['P8_pass']}")

    # ---- POST-HOC: the repair failed the SAME way, and the rule is now clear -
    # c_call*a_s and c_fix are both per-level constants, so for a fixed winning
    # scheme they are collinear. The identifiable magnitude count is the number
    # of distinct n-dependences in the recurrence, NOT the number of named
    # constants. Audited model: n, sqrt(n), log n, const, base-case = 5.
    def cost5b(scheme, N, m):
        _, a, b, alpha = scheme
        c_lin, c_call, c_sqrt, c_log, c_mul = m
        total, nn, mult = 0.0, float(N), 1.0
        for _ in range(200):
            if nn <= N_BASE:
                break
            total += mult * (c_lin * alpha * nn + c_call * a
                             + c_sqrt * math.sqrt(nn) + c_log * math.log(nn))
            mult *= a
            nn /= b
        return total + mult * c_mul * nn * nn

    def best_b(N, m):
        cs = [cost5b(s, N, m) for s in SCHEMES]
        i = int(np.argmin(cs))
        return i, cs[i]

    def r_const_b(m, szs):
        v = []
        for N in szs:
            i, cst = best_b(N, m)
            v.append(math.log(cst) - math.log(SCHEMES[i][1]) / math.log(SCHEMES[i][2])
                     * math.log(N))
        return np.array(v)

    LO2 = np.array([3e-3, 0.2, 0.05, 0.02, 1e-2])
    HI2 = np.array([30.0, 2000.0, 500.0, 200.0, 1e2])
    u2 = (rng.permuted(np.tile(np.arange(2000)[:, None], (1, 5)), axis=0)
          + rng.uniform(size=(2000, 5))) / 2000
    pts2 = np.exp(np.log(LO2) + u2 * (np.log(HI2) - np.log(LO2)))
    rc2, used2 = [], 0
    for m in pts2:
        base = best_b(2 ** 14, m)[0]
        if not all(best_b(2 ** 14, np.where(np.arange(5) == j, m * math.exp(s * 1e-4), m))[0]
                   == base for j in range(5) for s in (+1, -1)):
            continue
        used2 += 1
        rc2.append(rank(jac(r_const_b, m, sizes))[0])
        if used2 >= 150:
            break

    out["posthoc"] = dict(
        registered_model_rank_mode=out["rank_constant_mode"],
        collinear_pair="c_call*a_s and c_fix are both per-level constants",
        audited_model_magnitudes=["c_lin (n)", "c_call (const)", "c_sqrt (sqrt n)",
                                  "c_log (log n)", "c_mul (base case)"],
        audited_rank_mode=int(np.bincount(rc2).argmax()) if rc2 else None,
        audited_full_frac=float(np.mean([r == 5 for r in rc2])) if rc2 else 0.0,
        audited_points=used2,
        rule=("the identifiable magnitude count is the number of distinct "
              "n-dependences in the recurrence, not the number of named constants"),
    )
    say(f"  [post-hoc] registered repair still collinear (c_call, c_fix); audited "
        f"model with distinct n-dependences: rank "
        f"{out['posthoc']['audited_rank_mode']}/5 (full in "
        f"{out['posthoc']['audited_full_frac']:.2f} of {used2} points)")
    rec("legF", out)
    return out


# ============================================================================

def main():
    say("P-K — three kinds of kink, and which one P-D's is.")
    a, b, c = leg_A(), leg_B(), leg_C()
    d, e, f = leg_D(), leg_E(), leg_F()

    verdict = {
        "P1_closed_form_identity": a["P1_pass"],
        "P2_PD_estimator_collapses": a["P2_pass"],
        "P3_allometry_width_identity": a["P3_pass"],
        "P4a_control_width_identity": b["P4a_pass"],
        "P4b_scaling_functions_differ": b["P4b_pass"],
        "P5_selector_boundary_is_sharp": c["P5_pass"],
        "P6a_branch_point_n2_identity": d["P6a_pass"],
        "P6b_branch_point_n6": d["P6b_pass"],
        "P7_null_control_no_kink": e["P7_pass"],
        "P8_rank_test_repaired": f["P8_pass"],
    }
    at_risk = ["P2_PD_estimator_collapses", "P4b_scaling_functions_differ",
               "P5_selector_boundary_is_sharp", "P6b_branch_point_n6",
               "P7_null_control_no_kink", "P8_rank_test_repaired"]
    ident = ["P1_closed_form_identity", "P3_allometry_width_identity",
             "P4a_control_width_identity", "P6a_branch_point_n2_identity"]

    OUT["verdict"] = verdict
    OUT["at_risk_predictions"] = at_risk
    OUT["declared_identities"] = ident
    OUT["at_risk_passed"] = sum(verdict[k] for k in at_risk)
    OUT["at_risk_total"] = len(at_risk)
    OUT["identities_passed"] = sum(verdict[k] for k in ident)
    OUT["seed"] = SEED
    OUT["runtime_s"] = round(time.time() - T0, 1)

    say("\n=== VERDICT ===")
    for k, v in verdict.items():
        say(f"  [{'AT RISK ' if k in at_risk else 'identity'}] {k}: "
            f"{'PASS' if v else 'FAIL'}")
    say(f"\n  at-risk passed: {OUT['at_risk_passed']}/{OUT['at_risk_total']}")
    say(f"  identities passed: {OUT['identities_passed']}/{len(ident)}")
    say(f"  runtime {OUT['runtime_s']}s")

    with open("verdict.json", "w") as fh:
        json.dump(OUT, fh, indent=2, sort_keys=True)
    say("\nwrote verdict.json")


if __name__ == "__main__":
    main()
