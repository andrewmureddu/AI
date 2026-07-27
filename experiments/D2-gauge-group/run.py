"""
D2 - the scheme layer is the tower's gauge group.

Tests derivations/D2-gauge-of-the-tower.md.  Two parts:

  Part A (theorem checks)  do RG eigenvalues behave as the derivation says --
                           invariant under G_diff (smooth conjugation), covariant
                           under G_pow (y -> a*y)?
  Part B (at risk)         is the chart-free residue the codimension?  Measures
                           beta/k on full models and predicts 1/(p-2).

Pure numpy, deterministic.  ~20 s.
"""

import json
import numpy as np

SEED = 20260726
rng = np.random.default_rng(SEED)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def bisect(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if (f(mid) < 0) == (flo < 0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fit_slope(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    return float(coef[0]), float(np.max(np.abs(ly - A @ coef)))


def multiplier(f, us=None):
    """f fixes 0; return f'(0) by extrapolating f(u)/u linearly to u -> 0.

    Plain f(u)/u at finite u carries an O(u) error from the map's quadratic
    term, which is what limited the first run to ~7 digits.  Fitting the ratio
    against u and taking the intercept removes it.
    """
    us = np.array([1e-7, 2e-7, 5e-7, 1e-6, 2e-6, 5e-6]) if us is None else us
    r = np.array([f(u) / u for u in us])
    A = np.vstack([us, np.ones_like(us)]).T
    coef, *_ = np.linalg.lstsq(A, r, rcond=None)
    return float(coef[1])


def power_conjugate_multiplier(f, a, u0=1e-6):
    """Multiplier of the G_pow-conjugated map v = u^a, i.e. F = (.)^a o f o (.)^(1/a).

    Anchored on u rather than v: fixing v and computing v^(1/a) drives the
    argument to ~1e-18 for a = 1/3, where f(K*+u) - K* is pure cancellation
    noise.  Anchoring on u keeps every evaluation in the well-conditioned range.
    """
    us = np.array([u0, 2 * u0, 5 * u0])
    r = []
    for u in us:
        v = u ** a
        F = f(v ** (1.0 / a)) ** a          # exercises the round trip explicitly
        r.append(F / v)
    A = np.vstack([us, np.ones_like(us)]).T
    coef, *_ = np.linalg.lstsq(A, np.array(r), rcond=None)
    return float(coef[1])


# --------------------------------------------------------------------------
# Part A - RG maps
# --------------------------------------------------------------------------

def rg_ising1d():
    """1D Ising decimation, x = tanh K, x' = x^2, critical at x = 1.
    In u = 1 - x:  u' = 2u - u^2.  Lambda = 2, b = 2, y = 1."""
    return (lambda u: 2.0 * u - u * u), 2.0, 1.0


def rg_diamond():
    """Diamond hierarchical lattice, b = 2:  K' = 2 artanh(tanh(K)^2)."""
    f = lambda K: 2.0 * np.arctanh(np.tanh(K) ** 2)
    Ks = bisect(lambda K: f(K) - K, 0.3, 1.5)
    g = lambda u: f(Ks + u) - Ks
    return g, 2.0, Ks


def logistic_superstable(nmax=11):
    """Superstable parameters r_n of the period-doubling cascade."""
    def orbit(r, m):
        x = 0.5
        for _ in range(m):
            x = r * x * (1.0 - x)
        return x - 0.5
    rs = [2.0, 1.0 + np.sqrt(5.0)]
    for n in range(2, nmax + 1):
        guess = rs[-1] + (rs[-1] - rs[-2]) / 4.6692016
        r = guess
        for _ in range(80):                       # Newton, numerical derivative
            m = 2 ** n
            h = 1e-11
            F = orbit(r, m)
            dF = (orbit(r + h, m) - orbit(r - h, m)) / (2 * h)
            if dF == 0 or not np.isfinite(dF):
                break
            step = F / dF
            step = np.clip(step, -abs(rs[-1] - rs[-2]), abs(rs[-1] - rs[-2]))
            r -= step
            if abs(step) < 1e-15:
                break
        rs.append(r)
    return np.array(rs)


def part_A():
    out = {}

    # --- recover the known eigenvalues -----------------------------------
    legs = {}
    f1, b1, y1 = rg_ising1d()
    L1 = multiplier(f1)
    legs["R1_ising1d"] = {"Lambda": L1, "b": b1, "y": float(np.log(L1) / np.log(b1)),
                          "y_known": y1}

    f2, b2, Ks = rg_diamond()
    L2 = multiplier(f2)
    y2 = float(np.log(L2) / np.log(b2))
    legs["R2_diamond"] = {"K_star": float(Ks), "Lambda": L2, "b": b2, "y": y2,
                          "nu": float(1.0 / y2), "nu_known": 1.338}

    rs = logistic_superstable()
    deltas = [(rs[n - 1] - rs[n - 2]) / (rs[n] - rs[n - 1]) for n in range(2, len(rs))]
    delta = float(deltas[-1])
    legs["R3_logistic"] = {"delta": delta, "delta_known": 4.6692016,
                           "deltas": [float(d) for d in deltas]}
    out["legs"] = legs

    # --- P2: power covariance  y -> a*y ----------------------------------
    # v = u^a  =>  v' = (f(v^(1/a)))^a  =>  multiplier Lambda^a
    pw = []
    for name, f, b, Lam in [("R1_ising1d", f1, b1, L1), ("R2_diamond", f2, b2, L2)]:
        y0 = np.log(Lam) / np.log(b)
        for a in [1 / 3, 0.5, 2.0, 3.0]:
            La = power_conjugate_multiplier(f, a)
            ya = float(np.log(La) / np.log(b))
            pw.append({"leg": name, "a": a, "y_measured": ya,
                       "y_predicted": float(a * y0),
                       "rel_err": float(abs(ya - a * y0) / (a * y0))})
    # logistic: r - r_inf ~ C delta^-n, so (r-r_inf)^a ~ C^a delta^(-na)
    r_inf = (rs[-1] * delta - rs[-2]) / (delta - 1.0)
    d = np.abs(r_inf - rs[:-1])
    for a in [1 / 3, 0.5, 2.0, 3.0]:
        da = d ** a
        ratio = float(da[-3] / da[-2])
        pw.append({"leg": "R3_logistic", "a": a,
                   "y_measured": float(np.log(ratio) / np.log(2.0)),
                   "y_predicted": float(a * np.log(delta) / np.log(2.0)),
                   "rel_err": float(abs(np.log(ratio) - a * np.log(delta))
                                    / (a * np.log(delta)))})
    out["P2_power_covariance"] = pw

    # --- P1 / P3: conjugation and the common-vs-independent power group ---
    # A 2x2 linear RG map with one relevant and one irrelevant direction.
    y_true = np.array([0.75, -1.30])
    b = 2.0
    Lam = b ** y_true
    P = rng.normal(size=(2, 2))
    while abs(np.linalg.det(P)) < 0.3:
        P = rng.normal(size=(2, 2))
    M = P @ np.diag(Lam) @ np.linalg.inv(P)

    conj = []
    for _ in range(6):
        Q = rng.normal(size=(2, 2))
        while abs(np.linalg.det(Q)) < 0.3:
            Q = rng.normal(size=(2, 2))
        Mc = Q @ M @ np.linalg.inv(Q)
        yc = np.sort(np.log(np.abs(np.linalg.eigvals(Mc))) / np.log(b))
        conj.append({"y": yc.tolist(),
                     "max_abs_err": float(np.max(np.abs(yc - np.sort(y_true))))})
    out["P1_conjugation"] = {"y_true": y_true.tolist(), "trials": conj,
                             "max_abs_err": float(max(c["max_abs_err"] for c in conj))}

    ratio0 = float(y_true[0] / y_true[1])
    common, indep = [], []
    for a in [0.4, 1.7, 3.0]:
        ya = a * y_true
        common.append({"a": a, "y": ya.tolist(),
                       "ratio": float(ya[0] / ya[1]),
                       "signs_preserved": bool(np.all(np.sign(ya) == np.sign(y_true))),
                       "n_relevant": int(np.sum(ya > 0))})
    for a1, a2 in [(0.5, 2.0), (3.0, 0.4), (1.0, 2.5)]:
        ya = np.array([a1, a2]) * y_true
        indep.append({"a": [a1, a2], "y": ya.tolist(),
                      "ratio": float(ya[0] / ya[1]),
                      "signs_preserved": bool(np.all(np.sign(ya) == np.sign(y_true))),
                      "n_relevant": int(np.sum(ya > 0))})
    out["P3_group_action"] = {"ratio_unreparameterised": ratio0,
                              "common_a": common, "independent_a": indep,
                              "n_relevant_unreparameterised": int(np.sum(y_true > 0))}
    return out


# --------------------------------------------------------------------------
# Part B - is the residue the codimension?   beta/k =?= 1/(p-2)
# --------------------------------------------------------------------------

def leg_fold(eps):
    """x' = -eps + x^2.  Fixed points +-sqrt(eps); Phi'' = 2 sqrt(eps)."""
    return np.sqrt(eps), 2.0 * np.sqrt(eps)


def leg_sis(eps, beta=3.0):
    """I* = eps,  lambda = beta*eps."""
    return eps, beta * eps


def leg_ising(eps):
    """Mean-field Ising below T_c = 1, full model:  Phi'(m) = m - tanh(m/T)."""
    T = 1.0 - eps
    dphi = lambda m: m - np.tanh(m / T)
    m = bisect(dphi, 1e-16, 4.0)
    lam = 1.0 - (1.0 / T) / np.cosh(m / T) ** 2
    return m, lam


def leg_blume_capel(eps, a=1.0 / 3.0):
    """Blume-Capel below T_t = a on the line, full model."""
    T = a - eps
    A = a / (1.0 - a)
    def dphi(m):
        return m - A * np.sinh(m / T) / (1.0 + A * np.cosh(m / T))
    m = bisect(dphi, 1e-16, 4.0)
    C, Dn = np.cosh(m / T), 1.0 + A * np.cosh(m / T)
    lam = 1.0 - (A / T) * (C + A) / Dn**2
    return m, lam


def part_B():
    legs = [
        ("fold",         leg_fold,         3, np.logspace(-10, -6, 13), "identity"),
        ("sis",          leg_sis,          3, np.logspace(-10, -6, 13), "identity"),
        ("ising",        leg_ising,        4, np.logspace(-9, -5, 13),  "AT RISK"),
        ("blume_capel",  leg_blume_capel,  6, np.logspace(-9, -5, 13),  "AT RISK"),
    ]
    out = []
    for name, fn, p, eps_grid, status in legs:
        ms, lams = [], []
        for e in eps_grid:
            m, lam = fn(e)
            ms.append(m)
            lams.append(lam)
        ms, lams = np.array(ms), np.array(lams)
        beta, rb = fit_slope(eps_grid, ms)
        k, rk = fit_slope(eps_grid, lams)
        # P5: the observable-observable relation, which never mentions eps
        obs, ro = fit_slope(lams, ms)
        entry = {"leg": name, "p": p, "status": status,
                 "beta": beta, "k": k, "ratio": beta / k,
                 "predicted_ratio": 1.0 / (p - 2),
                 "m_vs_lambda_exponent": obs,
                 "resid": {"beta": rb, "k": rk, "m_vs_lambda": ro},
                 "reparameterised": []}
        # P5: eps' = eps^a.  beta and k each divide by a and the ratio is fixed.
        # The m-vs-lambda fit is re-measured on a grid that is uniform in log
        # eps', i.e. at DIFFERENT eps points -- otherwise its invariance would be
        # definitional (the fit never mentions eps) rather than tested.
        for a in [0.5, 2.0, 3.0]:
            ba, _ = fit_slope(eps_grid ** a, ms)
            ka, _ = fit_slope(eps_grid ** a, lams)
            # linear-uniform in eps', which a power map does NOT send back to a
            # log-uniform grid in eps -- so these are genuinely different points.
            # (A log-uniform grid would map to a log-uniform grid and the "resample"
            # would be a no-op, which is what the first run silently did.)
            ep = np.linspace(eps_grid[0] ** a, eps_grid[-1] ** a, len(eps_grid))
            eb = ep ** (1.0 / a)
            m2, l2 = zip(*[fn(e) for e in eb])
            oa, roa = fit_slope(np.array(l2), np.array(m2))
            entry["reparameterised"].append(
                {"a": a, "beta": ba, "k": ka, "ratio": ba / ka,
                 "m_vs_lambda_exponent": oa, "m_vs_lambda_resid": roa,
                 "resampled": True})
        out.append(entry)
    return out


# --------------------------------------------------------------------------

def main():
    res = {"seed": SEED}
    res["part_A"] = part_A()
    res["part_B"] = part_B()

    # P6: the invariants of the common-a action are exactly the degree-0
    # functions of the exponent vector -- i.e. ratios and signs.  Demonstrated:
    # any candidate depending on magnitude fails.
    y = np.array([0.75, -1.30, 0.20])
    probe = []
    for a in [0.3, 1.0, 2.5, 7.0]:
        ya = a * y
        probe.append({"a": a,
                      "magnitude_candidate_sum": float(np.sum(np.abs(ya))),
                      "ratio_invariant": float(ya[0] / ya[1]),
                      "n_relevant": int(np.sum(ya > 0))})
    res["P6_invariant_search"] = {
        "probe": probe,
        "note": "sum|y| moves with a; ratios and counts do not"}

    with open("verdict.json", "w") as fh:
        json.dump(res, fh, indent=2)

    A, B = res["part_A"], res["part_B"]
    print("=" * 72)
    print("D2 - the gauge group of the tower")
    print("=" * 72)

    print("\nPart A / legs recovered:")
    L = A["legs"]
    print(f"  R1 1D Ising decimation : y     = {L['R1_ising1d']['y']:.10f}  (exact 1)")
    print(f"  R2 diamond lattice     : y     = {L['R2_diamond']['y']:.6f}"
          f"   nu = {L['R2_diamond']['nu']:.6f}  (lit. ~1.338)")
    print(f"  R3 logistic cascade    : delta = {L['R3_logistic']['delta']:.6f}"
          f"  (Feigenbaum 4.669202)")

    print("\nP1 - conjugation invariance (G_diff), 2x2 map, 6 random conjugations:")
    print(f"  max |y - y_true| = {A['P1_conjugation']['max_abs_err']:.3e}")

    print("\nP2 - power covariance (G_pow):  y -> a*y")
    print(f"  {'leg':14s} {'a':>6s} {'measured':>12s} {'predicted':>12s} {'rel err':>10s}")
    for r in A["P2_power_covariance"]:
        print(f"  {r['leg']:14s} {r['a']:6.3f} {r['y_measured']:12.6f} "
              f"{r['y_predicted']:12.6f} {r['rel_err']:10.2e}")

    print("\nP3 - what survives which group (2x2 map, y = [0.75, -1.30]):")
    g = A["P3_group_action"]
    print(f"  unreparameterised ratio = {g['ratio_unreparameterised']:.6f},"
          f" n_relevant = {g['n_relevant_unreparameterised']}")
    for c in g["common_a"]:
        print(f"    common a={c['a']:.2f}  y={np.round(c['y'],4).tolist()}"
              f"  ratio={c['ratio']:.6f}  signs={c['signs_preserved']}"
              f"  n_rel={c['n_relevant']}")
    for c in g["independent_a"]:
        print(f"    indep  a={c['a']}  y={np.round(c['y'],4).tolist()}"
              f"  ratio={c['ratio']:.6f}  signs={c['signs_preserved']}"
              f"  n_rel={c['n_relevant']}")

    print("\nP4 - is the residue the codimension?  beta/k =?= 1/(p-2)")
    print(f"  {'leg':14s} {'p':>2s} {'beta':>8s} {'k':>8s} {'ratio':>8s} "
          f"{'pred':>7s} {'status':>9s}")
    for e in B:
        print(f"  {e['leg']:14s} {e['p']:2d} {e['beta']:8.4f} {e['k']:8.4f} "
              f"{e['ratio']:8.4f} {e['predicted_ratio']:7.4f} {e['status']:>9s}")

    print("\nP5 - under eps' = eps^a: beta and k move, the ratio and the")
    print("     observable-observable exponent (m vs lambda) do not")
    for e in B:
        row = "  %-13s m~lam^%.4f (pred %.4f) |" % (
            e["leg"], e["m_vs_lambda_exponent"], e["predicted_ratio"])
        for r in e["reparameterised"]:
            row += "  a=%.1f: b=%.3f k=%.3f r=%.4f" % (r["a"], r["beta"],
                                                       r["k"], r["ratio"])
        print(row)

    print("\nP6 - invariant search under common-a:")
    for pr in res["P6_invariant_search"]["probe"]:
        print(f"    a={pr['a']:.1f}  sum|y|={pr['magnitude_candidate_sum']:8.4f}"
              f"   ratio={pr['ratio_invariant']:.6f}   n_rel={pr['n_relevant']}")

    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
