#!/usr/bin/env python3
"""
BV — the base variable: one tower, seen through observables.

Numerical companion to derivations/base-variable.md. Checks, in order:

  F1/F2  the log-Laplace FORM is portable; the GEOMETRY is not      P1 P2
  §4     a singular density is not a singular Phi                   P3 P4
  §3     the rule: an invariant is a Phi-fact on Y iff Y is
         SUFFICIENT for it -- shown by a sufficiency failure        P5 P6 P7
  §5     rank(grad^2 Phi_Y) is the effective dimension of Y;
         P-D's "no Phi at all" is a rank-one base variable          P8 P9
  §4     the trichotomy guard: 3a/3b/3c exhibited, and no interior
         non-analyticity at finite size                             P10

Pure numpy + scipy. Deterministic. Writes verdict.json.
"""

import json
import math
import time

import numpy as np
from scipy.special import logsumexp

SEED = 20260728
OUT = {}
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def rec(k, v):
    OUT[k] = v


# ----------------------------------------------------------------------------
# Phi_Y for a finite measure, and a 5-point derivative stencil
# (instrument precision O(h^4) ~ 1e-12 at h = 1e-3, four orders below the
#  1e-8 tolerance P1 registers -- the audit item P-K's P1 failed)
# ----------------------------------------------------------------------------

def make_phi(weights, Y):
    """Phi_Y(lam) = log sum_i w_i exp(lam . Y_i), for a finite base measure."""
    logw = np.log(weights)

    def phi(lam):
        return logsumexp(logw + Y.dot(np.asarray(lam, float)))
    return phi


def tilted(weights, Y, lam):
    lp = np.log(weights) + Y.dot(np.asarray(lam, float))
    return np.exp(lp - logsumexp(lp))


def grad5(phi, lam, h=1e-3):
    d = len(lam)
    g = np.zeros(d)
    for j in range(d):
        e = np.eye(d)[j] * h
        g[j] = (-phi(lam + 2 * e) + 8 * phi(lam + e)
                - 8 * phi(lam - e) + phi(lam - 2 * e)) / (12 * h)
    return g


def hess5(phi, lam, h=1e-3):
    d = len(lam)
    H = np.zeros((d, d))
    for j in range(d):
        e = np.eye(d)[j] * h
        col = (-grad5(phi, lam + 2 * e, h) + 8 * grad5(phi, lam + e, h)
               - 8 * grad5(phi, lam - e, h) + grad5(phi, lam - 2 * e, h)) / (12 * h)
        H[:, j] = col
    return 0.5 * (H + H.T)


# ============================================================================
# LEG A — F1/F2: one master measure, three base variables          P1 P2
# ============================================================================

def leg_A():
    say("\n=== LEG A — form portable, geometry not (F1/F2) ===")
    rng = np.random.default_rng(SEED)
    n_paths, T = 4000, 12
    # master measure: paths of a 3-state chain, weighted by their probability
    P = np.array([[0.6, 0.3, 0.1], [0.2, 0.5, 0.3], [0.3, 0.2, 0.5]])
    p0 = np.array([1.0, 0.0, 0.0])
    paths = np.empty((n_paths, T), dtype=int)
    logw = np.zeros(n_paths)
    for i in range(n_paths):
        s = rng.choice(3, p=p0)
        paths[i, 0] = s
        for t in range(1, T):
            nxt = rng.choice(3, p=P[s])
            logw[i] += math.log(P[s, nxt])
            s = nxt
            paths[i, t] = s
    w = np.exp(logw - logsumexp(logw))

    # three base variables over the SAME master measure
    Y_state = np.stack([(paths[:, -1] == k).astype(float) for k in (0, 1)], axis=1)
    Y_occ = np.stack([(paths == k).mean(axis=1) for k in (0, 1)], axis=1)
    first2 = np.array([np.argmax(p == 2) if (p == 2).any() else T for p in paths],
                      dtype=float)
    Y_exit = np.stack([first2, first2 ** 2 / T], axis=1)

    res, hess = {}, {}
    for name, Y in (("state (final)", Y_state), ("occupancy (time average)", Y_occ),
                    ("exit time", Y_exit)):
        phi = make_phi(w, Y)
        lam = np.array([0.3, -0.2])
        q = tilted(w, Y, lam)
        g_true = Y.T.dot(q)
        C_true = (Y - g_true).T.dot((Y - g_true) * q[:, None])
        g_num, H_num = grad5(phi, lam), hess5(phi, lam)
        res[name] = dict(
            grad_err=float(np.abs(g_num - g_true).max()),
            hess_err=float(np.abs(H_num - C_true).max()),
            spectral_norm=float(np.linalg.norm(C_true, 2)),
            convex=bool(np.linalg.eigvalsh(C_true).min() >= -1e-12),
        )
        hess[name] = C_true

    max_err = max(max(v["grad_err"], v["hess_err"]) for v in res.values())
    norms = [v["spectral_norm"] for v in res.values()]
    ratio = max(norms) / min(norms)
    out = dict(per_base_variable=res, max_identity_err=float(max_err),
               spectral_norm_ratio=float(ratio),
               all_convex=bool(all(v["convex"] for v in res.values())))
    out["P1_pass"] = bool(max_err <= 1e-8 and out["all_convex"])
    out["P2_pass"] = bool(ratio >= 10.0)
    for k, v in res.items():
        say(f"  {k:26s} |grad-mean| {v['grad_err']:.2e}  |hess-cov| {v['hess_err']:.2e}"
            f"  ||C||={v['spectral_norm']:.4g}")
    say(f"  P1 (identity) form portable to all three: max err {max_err:.2e}  "
        f"pass={out['P1_pass']}")
    say(f"  P2 (AT RISK) geometry NOT portable: spectral-norm ratio {ratio:.1f}  "
        f"[registered >= 10]  pass={out['P2_pass']}")
    rec("legA", out)
    return out


# ============================================================================
# LEG B — a singular density is not a singular Phi                 P3 P4
# ============================================================================

def leg_B():
    say("\n=== LEG B — the caustic: singular density, entire Phi ===")
    rng = np.random.default_rng(SEED + 1)
    m = 2_000_000
    x = rng.uniform(-1, 1, m)
    y = x ** 2

    # P3: density exponent near 0 (identity: the Jacobian of y = x^2)
    edges = np.exp(np.linspace(math.log(1e-6), math.log(1e-2), 25))
    cnt, _ = np.histogram(y, bins=edges)
    ctr = np.sqrt(edges[:-1] * edges[1:])
    dens = cnt / (np.diff(edges) * m)
    ok = cnt > 50
    alpha = float(np.polyfit(np.log(ctr[ok]), np.log(dens[ok]), 1)[0])

    # P4: Phi_Y on a fine deterministic grid (Y bounded => mgf entire)
    grid = (np.arange(200_000) + 0.5) / 200_000 * 2 - 1
    Yg = (grid ** 2).reshape(-1, 1)
    wg = np.full(len(grid), 1.0 / len(grid))
    phi = make_phi(wg, Yg)

    # degree-20 Taylor about 0 from cumulants, via finite differences of Phi
    def d_n(k, h=0.05):
        # central difference of order k for Phi at 0
        c = np.array([(-1) ** i * math.comb(k, i) for i in range(k + 1)])
        pts = np.array([phi([(k / 2 - i) * h]) for i in range(k + 1)])
        return float(c.dot(pts) / h ** k)

    K = 20
    cum = [d_n(k) for k in range(1, K + 1)]
    lams = np.linspace(-3, 3, 61)
    taylor = np.array([sum(cum[k - 1] * L ** k / math.factorial(k)
                           for k in range(1, K + 1)) for L in lams])
    exact = np.array([phi([L]) for L in lams])
    taylor_err = float(np.abs(taylor - exact).max())
    finite_everywhere = bool(np.all(np.isfinite([phi([L]) for L in
                                                 np.linspace(-200, 200, 401)])))

    out = dict(density_exponent=alpha, taylor_max_err=taylor_err,
               phi_finite_over_pm200=finite_everywhere, taylor_degree=K)
    out["P3_pass"] = bool(abs(alpha + 0.5) <= 0.01)
    out["P4_pass"] = bool(taylor_err <= 1e-8 and finite_everywhere)
    say(f"  P3 (identity) density ~ y^{alpha:.4f}  [registered -0.500 +- 0.01]  "
        f"pass={out['P3_pass']}")
    say(f"  P4 (identity) Phi entire: degree-20 Taylor err {taylor_err:.2e} over "
        f"|lam|<=3, finite over |lam|<=200: {finite_everywhere}  pass={out['P4_pass']}")
    say("  -> the density diverges; Phi does not. A singular density is not a "
        "singular Phi.")

    # ---- POST-HOC: P4's instrument was the failure, not the claim ----------
    # A k-th order central difference at h = 0.05 divides by h^k = 1e-26 at
    # k = 20: the estimator is pure rounding noise well before that. This is
    # METHODOLOGY's audit item (iii) -- instrument precision -- violated in the
    # first pass after writing it. Exact cumulants instead: for Y = x^2 with x
    # uniform on [-1,1], m_k = E[x^2k] = 1/(2k+1), and the standard recursion
    # kappa_n = m_n - sum_{k<n} C(n-1,k-1) kappa_k m_{n-k} gives Phi's Taylor
    # coefficients exactly.
    mom = [1.0 / (2 * k + 1) for k in range(0, K + 1)]
    kap = []
    for nn in range(1, K + 1):
        s = mom[nn]
        for k in range(1, nn):
            s -= math.comb(nn - 1, k - 1) * kap[k - 1] * mom[nn - k]
        kap.append(s)
    taylor_x = np.array([sum(kap[k - 1] * L ** k / math.factorial(k)
                             for k in range(1, K + 1)) for L in lams])
    err_x = float(np.abs(taylor_x - exact).max())
    out["posthoc"] = dict(
        taylor_err_finite_difference=taylor_err,
        taylor_err_exact_cumulants=err_x,
        diagnosis=("the registered Taylor check divided by h^20 = 1e-26; the "
                   "estimator was noise long before the claim was tested. With "
                   "exact cumulants the same claim holds to "
                   f"{err_x:.1e}. Audit item (iii), violated one pass after "
                   "being written."),
    )
    say(f"  [post-hoc] Taylor err: finite differences {taylor_err:.2e} -> exact "
        f"cumulants {err_x:.2e} (Phi IS entire; the checker was not)")
    rec("legB", out)
    return out


# ============================================================================
# LEG C — the rule: a sufficiency failure                       P5 P6 P7
# ============================================================================

def mfpt(P, target):
    """Mean first-passage time to `target` from every state."""
    n = P.shape[0]
    idx = [i for i in range(n) if i != target]
    A = np.eye(len(idx)) - P[np.ix_(idx, idx)]
    t = np.linalg.solve(A, np.ones(len(idx)))
    out = np.zeros(n)
    out[idx] = t
    return out


def scgf_curvature(P, f, h=1e-4):
    """Lambda''(0) for the time average of f: the trajectory base variable."""
    def lam(k):
        M = P * np.exp(k * f)[None, :]
        return math.log(max(abs(np.linalg.eigvals(M))))
    return (lam(h) - 2 * lam(0.0) + lam(-h)) / h ** 2


def leg_C():
    say("\n=== LEG C — sufficiency: the state statistic cannot see it ===")
    n = 20
    cyc = np.zeros((n, n))
    for i in range(n):
        cyc[i, (i + 1) % n] = 0.5
        cyc[i, (i - 1) % n] = 0.5
    unif = np.full((n, n), 1.0 / n)

    def stat(P):
        v, V = np.linalg.eig(P.T)
        k = int(np.argmin(np.abs(v - 1.0)))
        p = np.real(V[:, k])
        return p / p.sum()

    pc, pu = stat(cyc), stat(unif)
    tv = 0.5 * float(np.abs(pc - pu).sum())

    m_cyc = mfpt(cyc, 0)[n // 2]
    m_unif = mfpt(unif, 0)[n // 2]

    # an observable with equal stationary mean under both
    f = np.cos(2 * math.pi * np.arange(n) / n)
    mean_c = float(pc.dot(f))
    mean_u = float(pu.dot(f))
    k_cyc = scgf_curvature(cyc, f)
    k_unif = scgf_curvature(unif, f)

    # state base variable: Phi over the stationary law of f -- identical by
    # construction if the stationary laws are identical
    phi_c = make_phi(pc, f.reshape(-1, 1))
    phi_u = make_phi(pu, f.reshape(-1, 1))
    state_gap = max(abs(phi_c([L]) - phi_u([L])) for L in np.linspace(-3, 3, 61))

    out = dict(
        n=n, stationary_tv_distance=tv,
        mfpt_cycle=float(m_cyc), mfpt_uniform=float(m_unif),
        mfpt_ratio=float(m_cyc / m_unif),
        mfpt_cycle_predicted=float((n // 2) * (n - n // 2)),
        mfpt_uniform_predicted=float(n),
        stationary_mean_gap=abs(mean_c - mean_u),
        state_phi_max_gap=float(state_gap),
        scgf_curvature_cycle=float(k_cyc), scgf_curvature_uniform=float(k_unif),
        scgf_ratio=float(max(k_cyc, k_unif) / min(k_cyc, k_unif)),
    )
    out["P5_pass"] = bool(tv <= 1e-15)
    out["P6_pass"] = bool(out["mfpt_ratio"] >= 2.0)
    out["P7_pass"] = bool(state_gap <= 1e-14 and out["scgf_ratio"] >= 2.0)
    say(f"  P5 (AT RISK) stationary laws identical: TV = {tv:.2e}  pass={out['P5_pass']}")
    say(f"  P6 (AT RISK) MFPT to the antipode: cycle {m_cyc:.1f} (predicted "
        f"{out['mfpt_cycle_predicted']:.0f}) vs uniform {m_unif:.1f} (predicted "
        f"{out['mfpt_uniform_predicted']:.0f}), ratio {out['mfpt_ratio']:.2f}  "
        f"pass={out['P6_pass']}")
    say(f"  P7 (AT RISK) STATE base variable blind: Phi gap {state_gap:.2e}; "
        f"TRAJECTORY base variable sees it: Lambda''(0) {k_cyc:.4f} vs {k_unif:.4f}, "
        f"ratio {out['scgf_ratio']:.2f}  pass={out['P7_pass']}")
    say("  -> the state statistic is NOT sufficient for either readout; the "
        "trajectory statistic is.")

    # ---- POST-HOC: P5's tolerance was below the eigensolver's noise floor ---
    # Both chains are doubly stochastic, so pi = uniform EXACTLY. Comparing two
    # numerically-computed eigenvectors measures the solver; comparing each to
    # the exact uniform vector measures the claim.
    exact_pi = np.full(n, 1.0 / n)
    out["posthoc"] = dict(
        tv_between_computed_eigenvectors=tv,
        max_dev_from_exact_uniform_cycle=float(np.abs(pc - exact_pi).max()),
        max_dev_from_exact_uniform_unifjump=float(np.abs(pu - exact_pi).max()),
        column_sums_cycle=float(np.abs(cyc.sum(axis=0) - 1).max()),
        column_sums_uniform=float(np.abs(unif.sum(axis=0) - 1).max()),
        diagnosis=("both chains are doubly stochastic, so the stationary law is "
                   "uniform by construction; 1.7e-15 is the 20x20 eigensolver's "
                   "noise, not a difference. The registered 1e-15 was below the "
                   "instrument's floor -- audit item (iii) again."),
    )
    say(f"  [post-hoc] doubly stochastic (column sums off by "
        f"{out['posthoc']['column_sums_cycle']:.1e} / "
        f"{out['posthoc']['column_sums_uniform']:.1e}), so pi = uniform exactly; "
        f"deviation from exact uniform "
        f"{out['posthoc']['max_dev_from_exact_uniform_cycle']:.1e} / "
        f"{out['posthoc']['max_dev_from_exact_uniform_unifjump']:.1e}")
    rec("legC", out)
    return out


# ============================================================================
# LEG D — rank(grad^2 Phi) is the base variable's dimension       P8 P9
# ============================================================================

def leg_D():
    say("\n=== LEG D — rank is the effective dimension of the base variable ===")
    rng = np.random.default_rng(SEED + 3)
    # P-D's honest exponential family: statistics (ln M, ln B) over network depths
    n_br, beta, gamma = 4, 4 ** -0.5, 4 ** (-1 / 3)
    Ns = np.arange(40, 140)
    lnB = Ns * math.log(n_br)
    lnM = np.array([logsumexp((N - np.arange(N + 1)) * math.log(n_br)
                              - 2 * np.arange(N + 1) * math.log(beta)
                              - np.arange(N + 1) * math.log(gamma)) for N in Ns])
    Y2 = np.stack([lnM, lnB], axis=1)
    w = np.full(len(Ns), 1.0 / len(Ns))
    phi2 = make_phi(w, Y2)

    ranks, small = [], []
    for a in np.linspace(-2, 2, 9):
        for b in np.linspace(-2, 2, 9):
            H = hess5(phi2, np.array([a * 1e-3, b * 1e-3]), h=1e-3)
            ev = np.sort(np.abs(np.linalg.eigvalsh(H)))[::-1]
            ranks.append(int((ev > 1e-12 * ev[0]).sum()))
            small.append(float(ev[-1] / ev[0]))

    # P9: add a genuinely independent third statistic
    extra = rng.normal(size=len(Ns))
    Y3 = np.concatenate([Y2, extra[:, None]], axis=1)
    phi3 = make_phi(w, Y3)
    ranks3, small3 = [], []
    for a in np.linspace(-1, 1, 5):
        H = hess5(phi3, np.array([a * 1e-3, -a * 1e-3, 0.1]), h=1e-3)
        ev = np.sort(np.abs(np.linalg.eigvalsh(H)))[::-1]
        ranks3.append(int((ev > 1e-12 * ev[0]).sum()))
        small3.append(float(ev[-1] / ev[0]))

    out = dict(
        rank2_modes=sorted(set(ranks)), rank2_max_smallest_ratio=float(max(small)),
        rank3_modes=sorted(set(ranks3)), rank3_min_smallest_ratio=float(min(small3)),
        grid_points=len(ranks),
    )
    out["P8_pass"] = bool(all(r == 1 for r in ranks) and max(small) <= 1e-12)
    out["P9_pass"] = bool(all(r >= 2 for r in ranks3) and min(small3) >= 1e-6)
    say(f"  P8 (identity) (lnM, lnB): rank {out['rank2_modes']} over "
        f"{len(ranks)} lambda, smallest/largest eigenvalue <= "
        f"{max(small):.2e}  pass={out['P8_pass']}")
    say(f"  P9 (AT RISK) + one independent statistic: rank {out['rank3_modes']}, "
        f"smallest/largest >= {min(small3):.2e}  pass={out['P9_pass']}")

    # ---- POST-HOC: the Hessian estimator, not the rank, was the problem ----
    # hess5 nests two 5-point stencils, so its floor is ~eps/h^2 ~ 1e-10 -- and
    # leg A already measured |hess - cov| up to 3.7e-9. A 1e-12 rank threshold
    # was never reachable with it. grad^2 Phi_Y IS the tilted covariance, which
    # is computable exactly; use that.
    def exact_hess(Yv, wv, lam):
        q = tilted(wv, Yv, lam)
        mu = Yv.T.dot(q)
        return (Yv - mu).T.dot((Yv - mu) * q[:, None])

    r2e, s2e = [], []
    for a in np.linspace(-2, 2, 9):
        for b in np.linspace(-2, 2, 9):
            H = exact_hess(Y2, w, np.array([a * 1e-3, b * 1e-3]))
            ev = np.sort(np.abs(np.linalg.eigvalsh(H)))[::-1]
            r2e.append(int((ev > 1e-12 * ev[0]).sum()))
            s2e.append(float(ev[-1] / ev[0]))
    r3e, s3e = [], []
    for a in np.linspace(-1, 1, 5):
        H = exact_hess(Y3, w, np.array([a * 1e-3, -a * 1e-3, 0.1]))
        ev = np.sort(np.abs(np.linalg.eigvalsh(H)))[::-1]
        r3e.append(int((ev > 1e-12 * ev[0]).sum()))
        s3e.append(float(ev[-1] / ev[0]))

    out["posthoc"] = dict(
        stencil_rank2=sorted(set(ranks)), stencil_smallest_ratio=float(max(small)),
        exact_rank2=sorted(set(r2e)), exact_smallest_ratio_2=float(max(s2e)),
        exact_rank3=sorted(set(r3e)), exact_smallest_ratio_3=float(min(s3e)),
        hess5_floor_from_legA=3.74e-9,
        diagnosis=("hess5 nests two 5-point stencils, floor ~eps/h^2 ~ 1e-10, and "
                   "leg A measured 3.7e-9; the registered 1e-12 rank threshold was "
                   "below the instrument. grad^2 Phi is the tilted covariance and "
                   "is exact -- audit item (iii), a third time in one pass."),
    )
    say(f"  [post-hoc] exact tilted covariance instead of the stencil: "
        f"(lnM,lnB) rank {out['posthoc']['exact_rank2']} with smallest/largest "
        f"<= {max(s2e):.2e}; +1 independent statistic rank "
        f"{out['posthoc']['exact_rank3']} with smallest/largest >= {min(s3e):.2e}")
    rec("legD", out)
    return out


# ============================================================================
# LEG E — the trichotomy guard                                        P10
# ============================================================================

def leg_E():
    say("\n=== LEG E — trichotomy guard: 3a / 3b / 3c, and nothing else ===")
    battery = {}

    # 3a: domain boundary -- a heavy tail. Phi finite for lam<0, infinite for lam>0.
    rng = np.random.default_rng(SEED + 4)
    pareto = (1 - rng.uniform(size=400_000)) ** (-1 / 1.5)
    def phi_pareto(L):
        return logsumexp(L * pareto) - math.log(len(pareto))
    finite_neg = np.isfinite(phi_pareto(-1.0))
    # exact statement: E[e^{lam Y}] = infinity for lam>0 with a Pareto tail
    grows = [phi_pareto(L) for L in (0.5, 1.0, 2.0, 4.0)]
    battery["3a_domain_boundary"] = dict(
        finite_for_negative_lambda=bool(finite_neg),
        phi_at_positive_lambda=[float(g) for g in grows],
        divergent_in_lambda=bool(grows[-1] > grows[0] * 3),
        exhibited=bool(finite_neg and grows[-1] > grows[0] * 3))

    # 3b: limit -- analytic at every finite N, non-analytic in the limit
    def free(N, t):
        return -(1.0 / N) * logsumexp([0.0, -N * t])
    curvs = []
    for N in (20, 80, 320, 1280):
        h = 1e-3
        curvs.append(abs(free(N, h) - 2 * free(N, 0.0) + free(N, -h)) / h ** 2)
    battery["3b_limit"] = dict(
        curvature_at_kink=[float(c) for c in curvs],
        grows_without_bound=bool(curvs[-1] > 10 * curvs[0]),
        finite_at_every_N=bool(all(np.isfinite(curvs))),
        exhibited=bool(all(np.isfinite(curvs)) and curvs[-1] > 10 * curvs[0]))

    # 3c: degeneracy -- Phi analytic, grad^2 Phi degenerate
    Y = np.array([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0], [0.5, 0.5]])   # rank-1 stats
    w = np.full(4, 0.25)
    phi = make_phi(w, Y)
    H = hess5(phi, np.array([0.1, -0.1]))
    ev = np.sort(np.abs(np.linalg.eigvalsh(H)))[::-1]
    battery["3c_degeneracy"] = dict(
        phi_finite_wide=bool(np.all(np.isfinite([phi([a, -a]) for a in
                                                 np.linspace(-50, 50, 101)]))),
        eigen_ratio=float(ev[-1] / ev[0]),
        exhibited=bool(ev[-1] / ev[0] < 1e-12))

    # the forbidden case: an interior non-analyticity at finite size.
    # Test six finite base variables by Taylor-remainder over their domain.
    rng2 = np.random.default_rng(SEED + 5)
    violations = []
    for trial in range(6):
        k = rng2.integers(4, 40)
        Yb = rng2.normal(size=(int(k), 2))
        wb = rng2.dirichlet(np.ones(int(k)))
        ph = make_phi(wb, Yb)
        lam0 = rng2.normal(scale=0.5, size=2)
        H = hess5(ph, lam0)
        # analytic <=> Hessian equals the tilted covariance exactly
        q = tilted(wb, Yb, lam0)
        mu = Yb.T.dot(q)
        C = (Yb - mu).T.dot((Yb - mu) * q[:, None])
        err = float(np.abs(H - C).max())
        finite = bool(np.all(np.isfinite([ph(l) for l in
                                          rng2.normal(scale=5, size=(40, 2))])))
        if err > 1e-7 or not finite:
            violations.append(dict(trial=trial, hess_err=err, finite=finite))
    battery["forbidden_interior_nonanalyticity"] = dict(
        trials=6, violations=len(violations), detail=violations)

    out = dict(battery=battery)
    out["P10_pass"] = bool(battery["3a_domain_boundary"]["exhibited"]
                           and battery["3b_limit"]["exhibited"]
                           and battery["3c_degeneracy"]["exhibited"]
                           and len(violations) == 0)
    say(f"  3a domain boundary exhibited: {battery['3a_domain_boundary']['exhibited']}")
    say(f"  3b limit exhibited:           {battery['3b_limit']['exhibited']} "
        f"(curvature {[round(c, 1) for c in battery['3b_limit']['curvature_at_kink']]})")
    say(f"  3c degeneracy exhibited:      {battery['3c_degeneracy']['exhibited']} "
        f"(eigen ratio {battery['3c_degeneracy']['eigen_ratio']:.1e})")
    say(f"  forbidden interior non-analyticity: {len(violations)} of 6 trials")
    say(f"  P10 (AT RISK) pass={out['P10_pass']}")
    rec("legE", out)
    return out


# ============================================================================

def main():
    say("BV — the base variable: one tower, seen through observables.")
    a, b, c, d, e = leg_A(), leg_B(), leg_C(), leg_D(), leg_E()

    verdict = {
        "P1_form_portable_identity": a["P1_pass"],
        "P2_geometry_not_portable": a["P2_pass"],
        "P3_caustic_exponent_identity": b["P3_pass"],
        "P4_phi_entire_identity": b["P4_pass"],
        "P5_stationary_laws_identical": c["P5_pass"],
        "P6_mfpt_differs": c["P6_pass"],
        "P7_sufficiency_failure": c["P7_pass"],
        "P8_rank_one_identity": d["P8_pass"],
        "P9_rank_restored": d["P9_pass"],
        "P10_trichotomy_guard": e["P10_pass"],
    }
    at_risk = ["P2_geometry_not_portable", "P5_stationary_laws_identical",
               "P6_mfpt_differs", "P7_sufficiency_failure", "P9_rank_restored",
               "P10_trichotomy_guard"]
    ident = ["P1_form_portable_identity", "P3_caustic_exponent_identity",
             "P4_phi_entire_identity", "P8_rank_one_identity"]

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
