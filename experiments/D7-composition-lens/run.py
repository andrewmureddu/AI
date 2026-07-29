"""
D7 - is there a floor 0, and is it a composition law?

Tests the four consequences of "floor 0 = a composition law" laid out in
questions/UNKNOWN-LAWS.md, on the split fixed by PREREGISTRATION.md:

  leg A  DECLARED IDENTITY - the order-resolved defect spectrum (1-D Ising, exact)
  leg B  AT-RISK  - the concavity defect scales as N^1 long-range, N^0 short-range,
                    with a q=2 control separating "long-range" from "first-order"
  leg C  AT-RISK  - additivity (not linearity, monotonicity or convexity) is what
                    closes an ensemble family under composition
  leg D  AT-RISK  - the order-2 defect takes three values: 0 / 1-2^-0.5 / 0.5
  leg E  IDENTITY - chart pinning arithmetic

Everything is exact enumeration or closed form except leg D3 (heavy tails), which
samples.  Pure numpy.  ~2 min.
"""

import json
from math import lgamma, log, sqrt

import numpy as np

SEED = 20260729
OUT = {}


def logsumexp(a, axis=None):
    a = np.asarray(a, float)
    m = np.max(a, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)
    return np.squeeze(m, axis=axis) + np.log(np.sum(np.exp(a - m), axis=axis))


def fit_slope(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    M = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(M, ly, rcond=None)
    return float(coef[0]), float(np.max(np.abs(ly - M @ coef)))


def lchoose(n, k):
    return lgamma(n + 1.0) - lgamma(k + 1.0) - lgamma(n - k + 1.0)


# ==========================================================================
# leg A - DECLARED IDENTITY.  1-D Ising, exact.  Order 0 vs order 2.
# ==========================================================================

def leg_A():
    """delta_0 and delta_2 for the open 1-D Ising chain, in closed form.

    Var(M_N) = N + 2 sum_{d=1}^{N-1} (N-d) u^d   with u = tanh(beta J).
    Phi_N    = ln 2 + (N-1) ln(2 cosh beta J).
    """
    def var_M(N, u):
        d = np.arange(1, N)
        return float(N + 2.0 * np.sum((N - d) * u ** d))

    def phi(N, bJ):
        return log(2.0) + (N - 1) * log(2.0 * np.cosh(bJ))

    rows = []
    for bJ in [0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]:
        u = float(np.tanh(bJ))
        xi = -1.0 / log(u)
        for N in [4, 16, 64, 256, 1024]:
            v1, v2 = var_M(N, u), var_M(2 * N, u)
            p1, p2 = phi(N, bJ), phi(2 * N, bJ)
            rows.append({
                "beta_J": bJ, "N": N, "xi": xi, "N_over_xi": N / xi,
                "delta_0": 1.0 - 2.0 * p1 / p2,
                "delta_2": 1.0 - 2.0 * v1 / v2,
            })

    # the two closed-form limits
    lim_corr = max(r["delta_2"] for r in rows if r["N_over_xi"] < 0.05)
    lim_indep = max(abs(r["delta_2"]) for r in rows if r["N_over_xi"] > 20)
    return {
        "label": "DECLARED IDENTITY - closed form, zero evidential weight",
        "rows": rows,
        "delta_2_correlated_limit": lim_corr,   # -> 1/2
        "delta_2_independent_limit": lim_indep,  # -> 0
        "max_abs_delta_0": max(abs(r["delta_0"]) for r in rows),
    }


# ==========================================================================
# leg B - AT-RISK.  The concavity defect and how it scales.
# ==========================================================================

def _group_logsumexp(key, lnW):
    """Exact (unique key, logsumexp of lnW within key), sorted by key.

    Energies are aggregated on their *exact integer* key rather than binned.  An
    earlier version binned onto a uniform e-grid and stored the bin centre, which
    misaligns the abscissa from the value it was computed at and destroys
    concavity — enough to make the exactly-log-binomial control look non-concave.
    """
    order = np.argsort(key, kind="stable")
    k, w = key[order], lnW[order]
    starts = np.flatnonzero(np.r_[True, k[1:] != k[:-1]])
    gmax = np.maximum.reduceat(w, starts)
    tot = np.add.reduceat(np.exp(w - np.repeat(gmax, np.diff(np.r_[starts, len(k)]))),
                          starts)
    return k[starts], gmax + np.log(tot)


def mf_potts_entropy(N, q):
    """Exact microcanonical entropy density of the mean-field q-state Potts model.

    H = -(1/2N) sum_a n_a^2,  so  e = E/N = -(1/2) sum_a x_a^2  with x_a = n_a/N.
    Multiplicity is the multinomial N!/(prod n_a!).  The energy key sum_a n_a^2 is
    an integer, so grouping is exact.
    """
    lg = np.array([lgamma(k + 1.0) for k in range(N + 1)])
    if q == 2:
        n1 = np.arange(N + 1, dtype=np.int64)
        n2 = N - n1
        lnW = lgamma(N + 1.0) - lg[n1] - lg[n2]
        key = n1 ** 2 + n2 ** 2
    elif q == 3:
        a, b = np.meshgrid(np.arange(N + 1, dtype=np.int64),
                           np.arange(N + 1, dtype=np.int64), indexing="ij")
        ok = (a + b) <= N
        n1, n2 = a[ok], b[ok]
        n3 = N - n1 - n2
        lnW = lgamma(N + 1.0) - lg[n1] - lg[n2] - lg[n3]
        key = n1 ** 2 + n2 ** 2 + n3 ** 2
    else:
        raise ValueError(q)
    k, w = _group_logsumexp(key, lnW)
    return -k / (2.0 * N * N), w / N


def chain_potts_entropy(N, q=3):
    """Exact microcanonical entropy density of the open 1-D q-state Potts chain.

    Sequences of N spins with exactly k agreeing neighbour pairs number
    q * C(N-1, k) * (q-1)^(N-1-k).   e = -k/N.  Log-binomial, hence exactly
    concave — which is the point of the control.
    """
    k = np.arange(N)
    lnW = np.array([log(q) + lchoose(N - 1, int(j)) + (N - 1 - j) * log(q - 1.0)
                    for j in k])
    return -k / N, lnW / N


def concave_hull(e, s):
    """Exact upper concave envelope of the point set, by monotone chain.

    An earlier version did this with a double Legendre transform on a fixed beta
    grid.  That is wrong at the ends: where |ds/de| exceeds the grid's range the
    transform cannot represent the tangent, so s** comes out too large and every
    model acquires a spurious gap that grows with N.  It made the *short-range
    control* the steepest riser in the table, which is what exposed it.  A hull is
    a hull; compute it exactly.
    """
    order = np.argsort(e)
    ex, sx = e[order], s[order]
    hull = []          # indices of upper-hull vertices
    for i in range(len(ex)):
        while len(hull) >= 2:
            a, b = hull[-2], hull[-1]
            # drop b if it lies on or below the chord a->i
            cross = ((ex[b] - ex[a]) * (sx[i] - sx[a])
                     - (sx[b] - sx[a]) * (ex[i] - ex[a]))
            if cross >= 0:
                hull.pop()
            else:
                break
        hull.append(i)
    hx, hy = ex[hull], sx[hull]
    out = np.empty_like(s)
    out[order] = np.interp(ex, hx, hy)
    return out


def two_copy_entropy(e, s, ngrid=1200):
    """max over splits of 1/2 (s(e1)+s(e2)) with (e1+e2)/2 = e.

    Computed on a uniform grid so the max-plus convolution is well defined; the
    point of B2 is that this independently reproduces the hull, so it must not be
    computed *from* the hull.  Returns (grid, two_copy, s_on_grid).
    """
    order = np.argsort(e)
    ex, sx = e[order], s[order]
    g = np.linspace(ex[0], ex[-1], ngrid)
    sg = np.interp(g, ex, sx)
    de = g[1] - g[0]
    out = np.full(ngrid, -np.inf)
    idx = np.arange(ngrid)
    for i in range(ngrid):
        j2 = 2 * i - idx          # e2 = 2 g[i] - g[j]  <=>  index 2i - j
        ok = (j2 >= 0) & (j2 < ngrid)
        if np.any(ok):
            out[i] = np.max(0.5 * (sg[ok] + sg[j2[ok]]))
    return g, out, sg


def specific_heat(e, s, trim=0.05):
    """c(e) = -(ds/de)^2 / (d^2 s/de^2), interior only.

    The endpoints of a microcanonical entropy have divergent slope, so finite
    differences there report nothing about the physics; trim them.
    """
    order = np.argsort(e)
    ex, sx = e[order], s[order]
    n = len(ex)
    lo, hi = int(trim * n) + 1, n - int(trim * n) - 1
    if hi - lo < 8:
        return np.array([])
    d1 = np.gradient(sx, ex)
    d2 = np.gradient(d1, ex)
    with np.errstate(divide="ignore", invalid="ignore"):
        c = -(d1 ** 2) / d2
    c, d2i, exi = c[lo:hi], d2[lo:hi], ex[lo:hi]
    ok = np.isfinite(c) & (np.abs(d2i) > 1e-6)
    return c[ok], exi[ok]


def leg_B():
    sizes = [64, 128, 256, 512, 1024]
    families = {
        "mean_field_q3": ("long-range, 1st order", lambda N: mf_potts_entropy(N, 3)),
        "mean_field_q2": ("long-range, 2nd order", lambda N: mf_potts_entropy(N, 2)),
        "chain_q3": ("short-range, no transition", lambda N: chain_potts_entropy(N, 3)),
    }

    res = {}
    for name, (desc, fn) in families.items():
        defects, gaps, hull_vs_twocopy, cmin, cneg = [], [], [], [], []
        for N in sizes:
            e, s = fn(N)
            hull = concave_hull(e, s)
            gap = np.maximum(hull - s, 0.0)
            gaps.append(float(np.max(gap)))            # the Legendre gap, per site
            defects.append(float(N * np.max(gap)))     # total
            g, twoc, sg = two_copy_entropy(e, s)
            hull_g = concave_hull(g, sg)
            fin = np.isfinite(twoc)
            fin[:3] = fin[-3:] = False
            hull_vs_twocopy.append(float(np.max(np.abs(hull_g[fin] - twoc[fin]))))
            c, ce = specific_heat(e, s)
            if len(c):
                cmin.append(float(np.min(c)))
                span = float(e.max() - e.min())
                neg = ce[c < 0]
                cneg.append(float(neg.max() - neg.min()) / span if len(neg) else 0.0)
            else:
                cmin.append(float("nan"))
                cneg.append(float("nan"))
        d = np.array(defects)
        slope, resid = fit_slope(sizes, np.maximum(d, 1e-16))
        res[name] = {
            "description": desc,
            "N": sizes,
            "legendre_gap_per_site": gaps,
            "defect_N_times_max_gap": defects,
            "defect_slope": slope if d.max() > 1e-8 else 0.0,
            "defect_slope_raw": slope,
            "fit_max_resid": resid,
            "hull_vs_twocopy_max_abs_diff": hull_vs_twocopy,   # B2 identity check
            "min_specific_heat": cmin,
            "negative_c_energy_fraction": cneg,
            "nonconcave": bool(d.max() > 1e-6),
        }

    # the non-concave window and where the canonical ensemble cannot follow
    e, s = mf_potts_entropy(1024, 3)
    hull = concave_hull(e, s)
    gap = hull - s
    win = e[gap > 1e-6]
    res["nonconcave_window_q3"] = ([float(win.min()), float(win.max())]
                                   if len(win) else None)
    res["label"] = "AT-RISK (B1, B3, B3b, B4); B2 is a declared identity check"
    return res


# ==========================================================================
# leg C - AT-RISK.  What closes an ensemble family under composition.
# ==========================================================================

STATS = {
    "Q":          (lambda Q: Q.astype(float),                 True,  "additive, linear"),
    "3Q_minus_7": (lambda Q: 3.0 * Q - 7.0,                   True,  "additive, affine"),
    "Q_squared":  (lambda Q: Q.astype(float) ** 2,            False, "monotone, convex"),
    "sqrt_Q":     (lambda Q: np.sqrt(Q.astype(float)),        False, "monotone, concave"),
    "log1p_Q":    (lambda Q: np.log1p(Q.astype(float)),       False, "monotone, concave"),
    "Q_mod_2":    (lambda Q: (Q % 2).astype(float),           False, "neither"),
}


def base_counts(n):
    """log multiplicities of Q = sum of n iid sites with q_i in {0,1,2}."""
    w = np.array([1.0, 1.0, 1.0])
    acc = np.array([1.0])
    for _ in range(n):
        acc = np.convolve(acc, w)
    return np.log(acc)          # index = Q, 0 .. 2n


def tilt(lnW, T, mu):
    lp = lnW - mu * T
    return lp - logsumexp(lp)


def kl(lp, lq):
    p = np.exp(lp)
    return float(np.sum(p * (lp - lq)))


def max_tilt_kl(lnW, T):
    """Largest KL(p(mu) || p(0)) any tilt of T can reach."""
    best = 0.0
    lp0 = tilt(lnW, T, 0.0)
    for mu in np.concatenate([-np.logspace(-3, 4, 80)[::-1], np.logspace(-3, 4, 80)]):
        v = kl(tilt(lnW, T, float(mu)), lp0)
        if np.isfinite(v):
            best = max(best, v)
    return best


def solve_mu(lnW, T, target=1.0):
    """mu with KL(p(mu) || p(0)) = target nat.  Search both signs.

    A bounded statistic cannot reach an arbitrary target: tilting Q mod 2 can at
    most push all mass onto one parity class, so its KL saturates near ln 2.  The
    caller lowers the target in that case and records what it used.
    """
    lp0 = tilt(lnW, T, 0.0)
    best = None
    for sign in (+1.0, -1.0):
        lo, hi = 0.0, sign * 1e-6
        for _ in range(200):
            if kl(tilt(lnW, T, hi), lp0) > target:
                break
            hi *= 2.0
            if abs(hi) > 1e8:
                hi = None
                break
        if hi is None:
            continue
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if kl(tilt(lnW, T, mid), lp0) > target:
                hi = mid
            else:
                lo = mid
        cand = 0.5 * (lo + hi)
        err = abs(kl(tilt(lnW, T, cand), lp0) - target)
        if best is None or err < best[1]:
            best = (cand, err)
    return best


def leg_C():
    ns = [8, 16, 32, 64, 128]
    res = {}
    for name, (fn, additive, shape) in STATS.items():
        kls, mus, targets = [], [], []
        for n in ns:
            lnW = base_counts(n)
            Q = np.arange(len(lnW))
            T1 = fn(Q)
            target = min(1.0, 0.8 * max_tilt_kl(lnW, T1))
            targets.append(target)
            got = solve_mu(lnW, T1, target)
            if got is None:
                kls.append(float("nan"))
                mus.append(float("nan"))
                continue
            mu, _ = got
            mus.append(mu)

            lp = tilt(lnW, T1, mu)                     # p_n(.; mu)
            LP = lp[:, None] + lp[None, :]             # the product measure
            P = np.exp(LP)

            A, B = np.meshgrid(Q, Q, indexing="ij")
            lnWW = lnW[:, None] + lnW[None, :]
            Tsum = fn(A + B)                           # the composite's statistic

            # min over mu' of KL(P || R(mu')); convex in mu', so golden-section
            def obj(m):
                lr = lnWW - m * Tsum
                lr = lr - logsumexp(lr.ravel())
                return float(np.sum(P * (LP - lr)))

            # coarse grid then ternary refinement; obj is convex in mu'
            grid = np.linspace(-50.0, 50.0, 2001)
            vals = np.array([obj(m) for m in grid])
            j = int(np.argmin(vals))
            lo = grid[max(j - 1, 0)]
            hi = grid[min(j + 1, len(grid) - 1)]
            for _ in range(80):
                m1 = lo + (hi - lo) / 3.0
                m2 = hi - (hi - lo) / 3.0
                if obj(m1) < obj(m2):
                    hi = m2
                else:
                    lo = m1
            kls.append(max(obj(0.5 * (lo + hi)), 0.0))

        arr = np.array(kls)
        slope = (fit_slope(ns, np.maximum(arr, 1e-18))[0]
                 if np.nanmax(arr) > 1e-9 else 0.0)
        res[name] = {
            "shape": shape,
            "additive": additive,
            "n": ns,
            "mu": mus,
            "tilt_target_nats": targets,
            "kl_min": kls,
            "kl_growth_slope": slope,
            "closes_family": bool(np.nanmax(arr) < 1e-12),
        }
    res["label"] = "AT-RISK (C1 the rule, C2 the growth exponent)"
    return res


# ==========================================================================
# leg D - AT-RISK.  Order 2, and the three values.
# ==========================================================================

def cw_var(N, bJ):
    """Var(M) for Curie-Weiss, exact: p(M) ~ C(N,(N+M)/2) exp(beta J M^2 / 2N)."""
    k = np.arange(N + 1)
    M = 2.0 * k - N
    lnp = np.array([lchoose(N, int(j)) for j in k]) + bJ * M ** 2 / (2.0 * N)
    lnp -= logsumexp(lnp)
    p = np.exp(lnp)
    m1 = float(np.sum(p * M))
    m2 = float(np.sum(p * M ** 2))
    return m2 - m1 ** 2


def leg_D():
    Ns = [256, 512, 1024, 2048, 4096]
    out = {}
    for label, bJ, pred in [("above_Tc", 0.8, 0.0),
                            ("at_Tc", 1.0, 1.0 - 2.0 ** -0.5),
                            ("below_Tc", 1.5, 0.5)]:
        d2, var_slope = [], []
        for N in Ns:
            v1, v2 = cw_var(N, bJ), cw_var(2 * N, bJ)
            d2.append(1.0 - 2.0 * v1 / v2)
        vs = [cw_var(N, bJ) for N in Ns]
        var_slope = fit_slope(Ns, vs)[0]
        out[label] = {
            "beta_J": bJ,
            "N": Ns,
            "delta_2": d2,
            "delta_2_final": d2[-1],
            "predicted": pred,
            "abs_error": abs(d2[-1] - pred),
            "var_scaling_exponent": var_slope,
        }

    # D3 - heavy tails: no order exists
    rng = np.random.default_rng(SEED)

    def stable(alpha, size):
        """Chambers-Mallows-Stuck, symmetric alpha-stable."""
        U = rng.uniform(-np.pi / 2, np.pi / 2, size)
        W = rng.exponential(1.0, size)
        return (np.sin(alpha * U) / np.cos(U) ** (1.0 / alpha)
                * (np.cos(U - alpha * U) / W) ** ((1.0 - alpha) / alpha))

    K, seeds = 4000, 12
    Ns_h = [100, 200, 400, 800, 1600, 3200]
    heavy = {}
    for tag, draw, alpha in [("alpha_stable_1.5", lambda s: stable(1.5, s), 1.5),
                             ("gaussian_control", lambda s: rng.normal(size=s), 2.0)]:
        per_seed = []
        for _ in range(seeds):
            V = [float(np.var(draw((K, N)).sum(axis=1))) for N in Ns_h]
            per_seed.append([1.0 - 2.0 * V[i] / V[i + 1] for i in range(len(V) - 1)])
        per_seed = np.array(per_seed)
        heavy[tag] = {
            "N_pairs": [[Ns_h[i], Ns_h[i + 1]] for i in range(len(Ns_h) - 1)],
            "delta_2_mean": per_seed.mean(axis=0).tolist(),
            "delta_2_std": per_seed.std(axis=0).tolist(),
            "scale_based_prediction": 1.0 - 2.0 ** (1.0 - 2.0 / alpha),
            "spread_first": float(per_seed.std(axis=0)[0]),
            "spread_last": float(per_seed.std(axis=0)[-1]),
        }
    out["heavy_tails"] = heavy
    out["label"] = "AT-RISK (D1 the three values, D2 the SSB reading, D3 heavy tails)"
    return out


# ==========================================================================
# leg E - DECLARED IDENTITY.  Chart pinning arithmetic.
# ==========================================================================

def leg_E():
    rows = []
    for a in [0.5, 1.0, 1.5, 2.0]:
        rows.append({
            "a": a,
            "additivity_defect_equal_parts": abs(1.0 - 2.0 ** (1.0 - a)),
        })
    return {
        "label": "DECLARED IDENTITY - arithmetic, zero evidential weight",
        "formula": "|1 - 2^(1-a)| for two equal additive parts under x -> x^a",
        "rows": rows,
        "reproduces_PD_legF": {"a=1.5": 0.2929, "a=2": 0.5, "a=0.5": 0.4142},
    }


# ==========================================================================

if __name__ == "__main__":
    OUT["seed"] = SEED
    print("leg A (identity) ...");  OUT["leg_A"] = leg_A()
    print("leg B (at-risk)  ...");  OUT["leg_B"] = leg_B()
    print("leg C (at-risk)  ...");  OUT["leg_C"] = leg_C()
    print("leg D (at-risk)  ...");  OUT["leg_D"] = leg_D()
    print("leg E (identity) ...");  OUT["leg_E"] = leg_E()

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2)

    print("\n--- A (identity) delta_2 limits:",
          round(OUT["leg_A"]["delta_2_correlated_limit"], 4), "/",
          round(OUT["leg_A"]["delta_2_independent_limit"], 6),
          "| max |delta_0| =", round(OUT["leg_A"]["max_abs_delta_0"], 5))
    print("--- B defect slopes:")
    for k in ["mean_field_q3", "mean_field_q2", "chain_q3"]:
        b = OUT["leg_B"][k]
        print(f"      {k:16s} {b['description']:28s} slope={b['defect_slope']:+.4f} "
              f"defects={[round(x, 4) for x in b['defect_N_times_max_gap']]} "
              f"c<0 on {round(max(b['negative_c_energy_fraction']) * 100, 1)}% of e "
              f"| B2 |hull-2copy|={max(b['hull_vs_twocopy_max_abs_diff']):.2e}")
    print("      nonconcave window (q3):", OUT["leg_B"]["nonconcave_window_q3"])
    print("--- C:")
    for k, v in OUT["leg_C"].items():
        if k == "label":
            continue
        print(f"      {k:12s} additive={str(v['additive']):5s} "
              f"kl_min={['%.3e' % x for x in v['kl_min']]} slope={v['kl_growth_slope']:+.3f}")
    print("--- D:")
    for k in ["above_Tc", "at_Tc", "below_Tc"]:
        v = OUT["leg_D"][k]
        print(f"      {k:9s} delta_2={v['delta_2_final']:.5f} "
              f"predicted={v['predicted']:.5f} err={v['abs_error']:.5f} "
              f"Var~N^{v['var_scaling_exponent']:.3f}")
    for k, v in OUT["leg_D"]["heavy_tails"].items():
        print(f"      {k:18s} delta_2={[round(x, 3) for x in v['delta_2_mean']]} "
              f"std={[round(x, 3) for x in v['delta_2_std']]} "
              f"scale-pred={v['scale_based_prediction']:.4f}")
