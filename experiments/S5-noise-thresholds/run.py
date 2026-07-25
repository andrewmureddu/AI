"""S5 — "is there only one threshold?" — Shannon capacity vs. Eigen's error
catastrophe vs. the quantum fault-tolerance threshold.

The stone (questions/SPECULATIVE.md, Cluster C) asks whether these three are one
redundancy-vs-noise transition, and offers a falsifier: *the redundancy-vs-gap
scaling exponents differ across the three*.

Common resource definition, applied identically in every leg:

    N(p) = minimum physical resource per protected bit required to keep the
           information recoverable indefinitely, at noise level p

    N(p) ~ (p_c - p)^(-alpha)   as p -> p_c from the recoverable side.

Legs (all exact or exactly-converged; pure numpy, deterministic, ~30 s):

  A. Coding theory, four channels — BSC, BEC, Z-channel, binary-input AWGN.
     N = 1/C with C computed by direct maximization of I(X;Y) over the input
     distribution (no capacity formulas assumed except as a cross-check).
     Also computes the directed chi-square between the two conditional laws,
     the proposed discriminator between exponent classes.

  B. Biology — Eigen's quasispecies, exact deterministic dynamics in the
     Hamming-class representation (exact for a single-peak landscape, since
     fitness depends only on the class).
       B1 bare model: locate the error catastrophe, test L*mu_c = ln(sigma).
       B2 with a decoder: majority repair across r copies per functional site,
          then find the minimum redundancy r_min(mu) from the same exact
          dynamics, and fit its divergence.

  C. Quantum fault tolerance — concatenated distance-(2t+1) codes: resource
     n0^L per logical qubit against the level-L error recursion.

Predictions were registered in predictions.json before this was run.
"""

import json
import math

import numpy as np

LN2 = math.log(2.0)


# ----------------------------------------------------------------------------
# generic helpers
# ----------------------------------------------------------------------------
def h2(p):
    """Binary entropy in bits."""
    p = np.clip(np.asarray(p, dtype=float), 0.0, 1.0)
    out = np.zeros_like(p)
    m = (p > 0) & (p < 1)
    out[m] = -p[m] * np.log2(p[m]) - (1 - p[m]) * np.log2(1 - p[m])
    return out if out.shape else float(out)


def entropy_bits(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def loglog_slope(gap, N, last_decade=True):
    """Fit N ~ gap^slope. If last_decade, use only the smallest-gap decade
    (the asymptotic regime)."""
    gap = np.asarray(gap, float)
    N = np.asarray(N, float)
    if last_decade:
        keep = gap <= gap.min() * 10.0
        if keep.sum() >= 3:
            gap, N = gap[keep], N[keep]
    A = np.vstack([np.log(gap), np.ones_like(gap)]).T
    slope, _ = np.linalg.lstsq(A, np.log(N), rcond=None)[0]
    return float(slope)


# ----------------------------------------------------------------------------
# LEG A — coding-theory channels
# ----------------------------------------------------------------------------
def capacity_binary_input(P0, P1, n_grid=20001):
    """C = max_pi I(X;Y) for a binary-input discrete channel, by direct
    maximization over Pr[X=1] = pi. Returns bits/use."""
    P0 = np.asarray(P0, float)
    P1 = np.asarray(P1, float)
    pis = np.linspace(0.0, 1.0, n_grid)
    HY = np.empty_like(pis)
    for i, pi in enumerate(pis):
        HY[i] = entropy_bits((1 - pi) * P0 + pi * P1)
    HYX = (1 - pis) * entropy_bits(P0) + pis * entropy_bits(P1)
    return float(np.max(HY - HYX))


def chi2_directed(P0, P1):
    """chi^2(P0 || P1) = sum (P0-P1)^2 / P1 — infinite if P0 is not absolutely
    continuous w.r.t. P1."""
    P0 = np.asarray(P0, float)
    P1 = np.asarray(P1, float)
    if np.any((P1 <= 0) & (P0 > 0)):
        return float("inf")
    m = P1 > 0
    return float(((P0[m] - P1[m]) ** 2 / P1[m]).sum())


def chi2_sym(P0, P1):
    """Symmetrized chi-square (triangular discrimination), sum (P0-P1)^2/mean.
    Always finite, and — the sharpened discriminator — its ORDER OF VANISHING
    in the gap is the exponent alpha. Second order iff the two conditional
    laws merge smoothly (the first-order term cancels identically, leaving the
    Fisher quadratic form); first order iff mass sits on a support mismatch."""
    P0 = np.asarray(P0, float)
    P1 = np.asarray(P1, float)
    mix = 0.5 * (P0 + P1)
    m = mix > 0
    return float(((P0[m] - P1[m]) ** 2 / mix[m]).sum())


def biawgn_capacity(a, n_nodes=80):
    """Binary-input AWGN, inputs +/-a, unit-variance noise, uniform input.
    I = 1 - E_{y~N(a,1)}[ log2(1 + exp(-2 a y)) ]  (bits). Gauss-Hermite.
    (n_nodes 40..200 agree to 7 digits; above ~300 the weights overflow.)"""
    x, w = np.polynomial.hermite_e.hermegauss(n_nodes)
    w = w / w.sum()
    y = a + x
    return float(1.0 - (w * np.logaddexp(0.0, -2.0 * a * y) / LN2).sum())


# Each channel: gap -> (P0, P1) conditional laws, plus a closed-form capacity
# for cross-checking the numerical maximization. "gap" is always the distance
# to the zero-capacity point, so alpha is directly comparable across channels.
CHANNELS = {
    # binary symmetric, p = 1/2 - gap: the two laws merge smoothly
    "BSC": (lambda g: ([1 - (0.5 - g), 0.5 - g], [0.5 - g, 1 - (0.5 - g)]),
            lambda g: 1.0 - float(h2(np.array([0.5 - g]))[0])),
    # binary erasure, e = 1 - gap: laws stay disjoint, informative mass -> 0
    "BEC": (lambda g: ([g, 0.0, 1 - g], [0.0, g, 1 - g]),
            lambda g: g),
    # Z-channel, q = 1 - gap: laws merge in total variation, but P1 puts mass
    # on a symbol P0 never emits -> one-sided support mismatch
    "Zchannel": (lambda g: ([1.0, 0.0], [1 - g, g]), None),
    # binary-input AWGN, amplitude a = gap: a second smooth merge
    "BIAWGN": (lambda g: _biawgn_discretized(g), lambda g: biawgn_capacity(g)),
}


def leg_A(gaps=np.logspace(-6, -2, 25)):
    out = {}
    for name, (law, formula) in CHANNELS.items():
        g = gaps if name != "BIAWGN" else np.logspace(-2, -0.6, 20)
        if name == "BIAWGN":
            C = np.array([biawgn_capacity(x) for x in g])
        else:
            C = np.array([capacity_binary_input(*law(x)) for x in g])
        x2 = np.array([chi2_sym(*law(x)) for x in g])
        rec = {
            "alpha_capacity": abs(loglog_slope(g, 1.0 / C)),
            "chi2_sym_vanishing_order": loglog_slope(g, x2),
            "C_over_chi2_sym": [float(v) for v in (C / x2)[[0, len(g) // 2, -1]]],
            "chi2_directed_01": chi2_directed(*law(g[len(g) // 2])),
            "chi2_directed_10": chi2_directed(*law(g[len(g) // 2])[::-1]),
            "total_variation": float(
                0.5 * np.abs(np.subtract(*[np.asarray(q, float)
                                           for q in law(g[len(g) // 2])])).sum()
            ),
        }
        if formula is not None:
            rec["max_rel_err_vs_formula"] = float(
                np.max(np.abs(C / np.array([formula(x) for x in g]) - 1))
            )
        out[name] = rec
    return out


def _biawgn_discretized(a, lo=-9.0, hi=9.0, n=40001):
    """Fine discretization of the two conditional Gaussians, for chi^2."""
    y = np.linspace(lo, hi, n)
    p0 = np.exp(-0.5 * (y - a) ** 2)
    p1 = np.exp(-0.5 * (y + a) ** 2)
    return p0 / p0.sum(), p1 / p1.sum()


# ----------------------------------------------------------------------------
# LEG B — Eigen's quasispecies (exact Hamming-class dynamics)
# ----------------------------------------------------------------------------
def log_binom_pmf(n, mu):
    k = np.arange(n + 1)
    if mu <= 0:
        out = np.full(n + 1, -np.inf)
        out[0] = 0.0
        return out
    logc = np.concatenate(
        [[0.0], np.cumsum(np.log(np.arange(n, 0, -1)) - np.log(np.arange(1, n + 1)))]
    )
    return logc + k * np.log(mu) + (n - k) * np.log1p(-mu)


def mutation_matrix(L, mu):
    """M[d', d] = P(Hamming distance d -> d') under independent per-site
    flipping with probability mu. Exact."""
    M = np.zeros((L + 1, L + 1))
    for d in range(L + 1):
        back = np.exp(log_binom_pmf(d, mu))          # j of the d wrong sites flip back
        fwd = np.exp(log_binom_pmf(L - d, mu))       # i of the L-d right sites flip
        M[:, d] = np.convolve(fwd, back[::-1])       # index n  <->  d' = d - j + i
    return M


def master_frequency(L, mu, sigma, tol=1e-13, max_iter=20000):
    """Stationary master-class frequency of the single-peak quasispecies
    (selection then mutation), by power iteration on M @ diag(w)."""
    M = mutation_matrix(L, mu)
    w = np.ones(L + 1)
    w[0] = sigma
    x = np.zeros(L + 1)
    x[0] = 1.0
    prev = -1.0
    for _ in range(max_iter):
        x = M @ (w * x)
        x /= x.sum()
        if abs(x[0] - prev) < tol:
            break
        prev = x[0]
    return float(x[0])


def majority_error(r, mu):
    """P(Bin(r, mu) > r/2) — per-functional-bit error after majority repair
    across r copies. r odd."""
    lp = log_binom_pmf(r, mu)
    tail = lp[(r + 1) // 2:]
    m = tail.max()
    return float(np.exp(m) * np.exp(tail - m).sum())


def leg_B1(sigma_list=(2.0, 10.0), L_list=(50, 100, 200, 400), floor=1e-10):
    """Bare quasispecies: locate the error catastrophe (the master frequency
    vanishes there — it is a transcritical crossing, not an inflection) by
    bisecting x0 > floor, and test L*mu_c = ln(sigma)."""
    rows = []
    for sigma in sigma_list:
        for L in L_list:
            lo, hi = 1e-9, min(0.5, 4 * math.log(sigma) / L)
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if master_frequency(L, mid, sigma) > floor:
                    lo = mid
                else:
                    hi = mid
            mu_c = 0.5 * (lo + hi)
            exact = 1 - sigma ** (-1.0 / L)   # root of sigma*(1-mu)^L = 1
            rows.append(
                {
                    "sigma": sigma,
                    "L": L,
                    "mu_c_numeric": mu_c,
                    "L_mu_c": L * mu_c,
                    "ln_sigma": math.log(sigma),
                    "rel_err_vs_ln_sigma": abs(L * mu_c / math.log(sigma) - 1),
                    "mu_c_analytic_1_minus_sigma_pow": exact,
                    "rel_err_vs_analytic": abs(mu_c / exact - 1),
                }
            )
    return rows


def leg_B2(k=64, sigma=2.0, crit=0.01, n_deltas=12):
    """Quasispecies + majority repair: minimum redundancy r_min(mu), from the
    same exact dynamics applied to the decoded genome."""

    def viable(r, mu):
        e = majority_error(r, mu)
        # an effective per-site error >= 1/2 carries no information at all; it
        # also puts the class dynamics into the degenerate inversion regime
        # (mu_eff -> 1 is deterministic bit-flipping, a 2-cycle, not noise)
        if e >= 0.5:
            return False
        return master_frequency(k, e, sigma) >= crit

    def r_min(mu):
        lo, hi = 1, 3
        while not viable(hi, mu):
            lo, hi = hi, (hi * 2) | 1
            if hi > 400001:
                return None
        while hi - lo > 2:
            mid = ((lo + hi) // 2) | 1
            if viable(mid, mu):
                hi = mid
            else:
                lo = mid
        return hi

    deltas = np.logspace(math.log10(0.02), math.log10(0.25), n_deltas)
    rows = []
    for d in deltas:
        mu = 0.5 - d
        r = r_min(mu)
        rows.append({"delta": float(d), "mu": float(mu), "r_min": r})
    gaps = np.array([q["delta"] for q in rows])
    rs = np.array([q["r_min"] for q in rows], float)
    # the coding gap, as a constant: repetition r_min vs. optimal 1/C, both * d^2
    N_opt = 1.0 / (1.0 - h2(0.5 - gaps))
    return {
        "k": k,
        "sigma": sigma,
        "criterion_master_freq": crit,
        # the threshold really is at 1/2: no redundancy suffices there, while
        # any mu < 1/2 is rescuable, at a cost that keeps growing like d^-2.
        # (mu > 1/2 is outside the model: that is deterministic inversion, i.e.
        # signal, not noise — the standard quasispecies restriction mu <= 1/2.)
        "r_min_at_mu_0.50": r_min(0.50),
        "r_min_deeper_gaps": {
            str(d): r_min(0.5 - d) for d in (0.015, 0.01, 0.0075)
        },
        "alpha": loglog_slope(gaps, rs, last_decade=False),
        "alpha_smallest_half": loglog_slope(
            gaps[: max(3, n_deltas // 2)], rs[: max(3, n_deltas // 2)], last_decade=False
        ),
        "r_min_times_delta2": [float(v) for v in rs * gaps ** 2],
        "coding_gap_ratio": [float(v) for v in rs / N_opt],
        "rows": rows,
    }


def leg_B2_robustness(k=64, sigma=2.0):
    """Same exponent under a 100x change of the survival criterion?"""
    out = {}
    for crit in (0.001, 0.1):
        res = leg_B2(k=k, sigma=sigma, crit=crit, n_deltas=6)
        out[str(crit)] = res["alpha"]
    return out


# ----------------------------------------------------------------------------
# LEG C — concatenated fault tolerance
# ----------------------------------------------------------------------------
def ft_overhead(p, p_th, n0, t, eps):
    """Physical qubits per logical qubit for a concatenated distance-(2t+1)
    code: level-L error is p_th*(p/p_th)^((t+1)^L), resource is n0^L."""
    need = math.log(p_th / eps) / math.log(p_th / p)      # required (t+1)^L
    L_real = math.log(need) / math.log(t + 1)             # smooth envelope
    return n0 ** L_real, n0 ** math.ceil(L_real)


def leg_C(p_th=1e-4, eps=1e-12):
    rows = []
    for n0, t in ((5, 1), (7, 1), (9, 1), (23, 3)):
        gaps = np.logspace(-4, -1, 25) * p_th            # p_th - p
        p = p_th - gaps
        N = np.array([ft_overhead(x, p_th, n0, t, eps)[0] for x in p])
        N_stair = np.array([ft_overhead(x, p_th, n0, t, eps)[1] for x in p])
        theory = math.log(n0) / math.log(t + 1)
        fit = -loglog_slope(gaps, N)
        rows.append(
            {
                "n0": n0,
                "t": t,
                "alpha_theory_log_n0_over_log_t1": theory,
                "alpha_fit": fit,
                "rel_err": abs(fit / theory - 1),
                "alpha_fit_staircase": -loglog_slope(gaps, N_stair),
            }
        )
    return rows


# ----------------------------------------------------------------------------
def main():
    res = {}
    print("leg A — coding-theory channels ...")
    res["A_channels"] = leg_A()
    for name, r in res["A_channels"].items():
        print(f"   {name:10s} alpha = {r['alpha_capacity']:.4f}"
              f"   chi2_sym order = {r['chi2_sym_vanishing_order']:.4f}"
              f"   chi2 directed = {r['chi2_directed_01']:.3g} / "
              f"{r['chi2_directed_10']:.3g}")

    print("leg B1 — bare quasispecies (error catastrophe) ...")
    res["B1_eigen_bare"] = leg_B1()
    for r in res["B1_eigen_bare"]:
        print(f"   sigma={r['sigma']:>4} L={r['L']:>3}  L*mu_c = {r['L_mu_c']:.4f}"
              f"   ln sigma = {r['ln_sigma']:.4f}"
              f"   rel err vs ln sigma {r['rel_err_vs_ln_sigma']:.4f}"
              f"   vs finite-L root {r['rel_err_vs_analytic']:.2e}")

    print("leg B2 — quasispecies + majority repair ...")
    res["B2_eigen_repair"] = leg_B2()
    b2 = res["B2_eigen_repair"]
    print(f"   alpha = {b2['alpha']:+.4f} (smallest half: {b2['alpha_smallest_half']:+.4f})")
    print(f"   r_min*delta^2 = {[round(v, 2) for v in b2['r_min_times_delta2']]}")
    print(f"   coding-gap ratio r_min/(1/C) = "
          f"{[round(v, 2) for v in b2['coding_gap_ratio']]}")
    res["B2_robustness_alpha_by_criterion"] = leg_B2_robustness()
    print(f"   robustness (crit 0.001 / 0.1): {res['B2_robustness_alpha_by_criterion']}")

    print("leg C — concatenated fault tolerance ...")
    res["C_fault_tolerance"] = leg_C()
    for r in res["C_fault_tolerance"]:
        print(f"   n0={r['n0']:>3} t={r['t']}  alpha_fit = {r['alpha_fit']:.4f}"
              f"   theory log_{r['t']+1}({r['n0']}) = "
              f"{r['alpha_theory_log_n0_over_log_t1']:.4f}"
              f"   rel err {r['rel_err']:.2e}")

    # ---- the falsifier, evaluated ----------------------------------------
    alphas = {
        **{k: v["alpha_capacity"] for k, v in res["A_channels"].items()},
        "eigen_majority_repair": -res["B2_eigen_repair"]["alpha"],
        **{f"FT_n0={r['n0']}_t={r['t']}": r["alpha_fit"] for r in res["C_fault_tolerance"]},
    }
    alphas = {k: abs(v) for k, v in alphas.items()}
    res["alphas"] = alphas
    spread = max(alphas.values()) - min(alphas.values())
    res["falsifier"] = {
        "statement": "the redundancy-vs-gap scaling exponents differ across the three",
        "spread": spread,
        "fires": bool(spread > 0.1),
    }

    # ---- the replacement taxonomy, evaluated ------------------------------
    merge = ["BSC", "BIAWGN", "eigen_majority_repair"]
    support = ["BEC", "Zchannel"]
    rg = [k for k in alphas if k.startswith("FT_")]
    res["taxonomy"] = {
        "type_M_smooth_merge_predict_2": {k: alphas[k] for k in merge},
        "type_S_support_mismatch_predict_1": {k: alphas[k] for k in support},
        "type_R_decoder_RG_fixed_point_predict_log_n0_over_log_t1": {
            k: alphas[k] for k in rg
        },
        "type_M_max_dev_from_2": max(abs(alphas[k] - 2) for k in merge),
        "type_S_max_dev_from_1": max(abs(alphas[k] - 1) for k in support),
        "type_R_max_rel_dev": max(r["rel_err"] for r in res["C_fault_tolerance"]),
    }

    # ---- the sharpened discriminator, tested -----------------------------
    # Registered version ("chi2 infinite => alpha=1") turned out to be
    # direction-dependent, so it is replaced by a quantitative rule and tested
    # here: alpha equals the ORDER OF VANISHING of the symmetrized chi-square
    # between the two conditional laws.
    disc = {
        name: {
            "alpha_capacity": r["alpha_capacity"],
            "chi2_sym_order": r["chi2_sym_vanishing_order"],
            "abs_diff": abs(r["alpha_capacity"] - r["chi2_sym_vanishing_order"]),
        }
        for name, r in res["A_channels"].items()
    }
    res["discriminator_alpha_equals_chi2_order"] = {
        "per_channel": disc,
        "max_abs_diff": max(v["abs_diff"] for v in disc.values()),
        "holds": bool(max(v["abs_diff"] for v in disc.values()) < 0.05),
    }

    print("\n--- verdict ---")
    print(f"falsifier fires: {res['falsifier']['fires']}  (spread {spread:.3f})")
    print(f"type-M (smooth merge) max deviation from 2:      "
          f"{res['taxonomy']['type_M_max_dev_from_2']:.4f}")
    print(f"type-S (support mismatch) max deviation from 1:  "
          f"{res['taxonomy']['type_S_max_dev_from_1']:.4f}")
    print(f"type-R (decoder RG) max relative deviation:      "
          f"{res['taxonomy']['type_R_max_rel_dev']:.2e}")
    print(f"alpha == order of vanishing of chi2_sym:         "
          f"{res['discriminator_alpha_equals_chi2_order']['holds']}"
          f"  (max |diff| "
          f"{res['discriminator_alpha_equals_chi2_order']['max_abs_diff']:.4f})")

    with open("verdict.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
