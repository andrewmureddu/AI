#!/usr/bin/env python3
"""
P-C — variational principles come in exactly two kinds?

Tests the floor sort's last unrun prediction (invariants/FLOORS.md §3) about
entry #7, in the repaired form registered in PREREGISTRATION.md:

  C1  the floor is a property of the READOUT, not of the functional
  C2  "over a measure" vs "over an action" is a DECOMPOSITION, not a partition
  C3  P-C's registered falsifier fires: predictive variational laws exist with
      no potential at all, because rotation replaces S > 0's n conditions with
      ceil(n/2) conditions.

Legs
  A  the two poles                     (identity / estimator check)   P1
  B  potential-free but predictive     (AT RISK, central)        P2 P2b P3 P3b P4 P5
  C  the selector, in CS not physics   (AT RISK)                 P6 P7 P8 P11s
  D  floor 1's response type           (AT RISK)                 P9 P10 P11f

Pure numpy + scipy. Deterministic (single seed). Writes verdict.json.
"""

import json
import math
import time

import numpy as np
from scipy.linalg import schur
from scipy.optimize import brentq, minimize
from scipy.special import logsumexp

SEED = 20260727
OUT = {}
T0 = time.time()


def rec(section, key, value):
    OUT.setdefault(section, {})[key] = value


def say(*a):
    print(*a, flush=True)


# ----------------------------------------------------------------------------
# shared machinery
# ----------------------------------------------------------------------------

def goe(rng, n, size=None):
    """Symmetric GOE-like draw, Frobenius-normalised to 1."""
    shape = (n, n) if size is None else (size, n, n)
    g = rng.normal(0.0, 1.0 / math.sqrt(n), shape)
    s = 0.5 * (g + np.swapaxes(g, -1, -2))
    nrm = np.linalg.norm(s, axis=(-2, -1), keepdims=True)
    return s / nrm


def antisym(rng, n, size=None):
    """Antisymmetric draw, Frobenius-normalised to 1."""
    shape = (n, n) if size is None else (size, n, n)
    h = rng.normal(0.0, 1.0 / math.sqrt(n), shape)
    a = 0.5 * (h - np.swapaxes(h, -1, -2))
    nrm = np.linalg.norm(a, axis=(-2, -1), keepdims=True)
    return a / nrm


def loop_integral_linear(J, loop):
    """Exact line integral of g(x) = J x around a closed polygon.

    For a segment p->q,  int g.dx = (Jp).(q-p) + 1/2 (J(q-p)).(q-p).
    Zero for symmetric J (exact differential); the circulation for antisymmetric J.
    """
    total = 0.0
    m = len(loop)
    for i in range(m):
        p = loop[i]
        q = loop[(i + 1) % m]
        d = q - p
        total += J.dot(p).dot(d) + 0.5 * J.dot(d).dot(d)
    return total


def loop_integral_field(g, loop, nq=2000):
    """Line integral of a general field g around a closed polygon (quadrature)."""
    total = 0.0
    m = len(loop)
    ts = (np.arange(nq) + 0.5) / nq
    for i in range(m):
        p = loop[i]
        q = loop[(i + 1) % m]
        d = q - p
        pts = p[None, :] + ts[:, None] * d[None, :]
        vals = np.array([g(x) for x in pts])
        total += float(vals.dot(d).mean())
    return total


def random_loop(rng, n, radius=1.0, verts=7):
    """A closed polygon in a random 2-plane of R^n."""
    q, _ = np.linalg.qr(rng.normal(size=(n, 2)))
    ang = np.sort(rng.uniform(0, 2 * math.pi, verts))
    rad = radius * rng.uniform(0.5, 1.5, verts)
    pts2 = np.stack([rad * np.cos(ang), rad * np.sin(ang)], axis=1)
    return pts2.dot(q.T)


def rk4(f, x, dt, steps):
    for _ in range(steps):
        k1 = f(x)
        k2 = f(x + 0.5 * dt * k1)
        k3 = f(x + 0.5 * dt * k2)
        k4 = f(x + dt * k3)
        x = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x


# ============================================================================
# LEG A — the two poles (identity; estimator check)                        P1
# ============================================================================

def leg_A():
    say("\n=== LEG A — the two poles (identity) ===")
    rng = np.random.default_rng(SEED)
    n, draws, loops = 6, 200, 50

    pot_frac_S, pot_frac_A = [], []
    path_dep_S, circ_A = [], []
    stable_matches = 0
    energy_drift = []

    for _ in range(draws):
        S = goe(rng, n)
        A = antisym(rng, n)

        # (a) pure potential: A = 0
        JS = S
        piS = np.linalg.norm(S) ** 2 / (np.linalg.norm(S) ** 2 + 0.0)
        pot_frac_S.append(piS)
        d = max(abs(loop_integral_linear(JS, random_loop(rng, n)))
                for _ in range(loops // 10))
        path_dep_S.append(d)
        conv = np.all(np.linalg.eigvals(JS).real > 0)
        pos_def = np.linalg.eigvalsh(S).min() > 0
        stable_matches += int(conv == pos_def)

        # (b) pure rotation: S = 0
        JA = A
        piA = 0.0 / (0.0 + np.linalg.norm(A) ** 2)
        pot_frac_A.append(piA)
        c = max(abs(loop_integral_linear(JA, random_loop(rng, n)))
                for _ in range(loops // 10))
        circ_A.append(c)

    # energy conservation under xdot = -A x
    for _ in range(20):
        A = antisym(rng, n)
        x0 = rng.normal(size=n)
        x0 /= np.linalg.norm(x0)
        e0 = 0.5 * x0.dot(x0)
        xT = rk4(lambda x: -A.dot(x), x0, 1e-3, 10_000)
        energy_drift.append(abs(0.5 * xT.dot(xT) - e0) / e0)

    res = dict(
        n=n, draws=draws,
        pi_pure_potential=float(np.mean(pot_frac_S)),
        pi_pure_rotation=float(np.mean(pot_frac_A)),
        path_dependence_potential_max=float(np.max(path_dep_S)),
        circulation_rotation_min=float(np.min(circ_A)),
        energy_drift_max=float(np.max(energy_drift)),
        convergence_iff_posdef_rate=stable_matches / draws,
    )
    res["P1_pass"] = bool(
        res["path_dependence_potential_max"] <= 1e-12
        and res["circulation_rotation_min"] >= 0.1
        and res["energy_drift_max"] <= 1e-10
        and res["convergence_iff_posdef_rate"] == 1.0
    )
    say(f"  path-dependence (potential pole, max) = {res['path_dependence_potential_max']:.3e}"
        "   [registered <= 1e-12]")
    say(f"  circulation (rotation pole, min)      = {res['circulation_rotation_min']:.4f}"
        "   [registered >= 0.1]")
    say(f"  |dE|/E under pure rotation (max)      = {res['energy_drift_max']:.3e}"
        "   [registered <= 1e-10]")
    say(f"  converge <=> S>0 at A=0               = {res['convergence_iff_posdef_rate']:.3f}")
    say(f"  P1 (identity) pass = {res['P1_pass']}")
    rec("legA", "P1", res)
    return res


# ============================================================================
# LEG B — potential-free but predictive                    P2 P2b P3 P3b P4 P5
# ============================================================================

def plane_averages(S, A):
    """ceil(n/2) two-plane averages of S in A's real Schur basis.

    Large-a perturbation theory: for J = S + aA with A antisymmetric (normal,
    eigenvalues +-i*mu_j), the real part of each eigenvalue pair converges to
    1/2 (u^T S u + w^T S w) over A's invariant 2-plane (u, w).
    """
    n = S.shape[0]
    T, Q = schur(A, output="real")
    vals = []
    i = 0
    while i < n:
        if i + 1 < n and abs(T[i + 1, i]) > 1e-12:
            u, w = Q[:, i], Q[:, i + 1]
            vals.append(0.5 * (u.dot(S).dot(u) + w.dot(S).dot(w)))
            i += 2
        else:
            z = Q[:, i]
            vals.append(z.dot(S).dot(z))
            i += 1
    return np.array(vals)


def weighted_potential_residual(J, rng, restarts=4):
    """min over positive diagonal D of ||DJ - (DJ)^T||_F / ||J||_F.

    A weighted potential game requires this to be 0.
    """
    n = J.shape[0]
    nrm = np.linalg.norm(J)

    def obj(t):
        d = np.exp(t - t.mean())          # scale-free: D and cD are equivalent
        M = d[:, None] * J
        return np.linalg.norm(M - M.T) / nrm

    best = obj(np.zeros(n))
    for _ in range(restarts):
        t0 = rng.normal(scale=1.0, size=n)
        r = minimize(obj, t0, method="L-BFGS-B",
                     options=dict(maxiter=2000, ftol=1e-14, gtol=1e-12))
        best = min(best, float(r.fun))
    return best


def leg_B():
    say("\n=== LEG B — potential-free but predictive (AT RISK) ===")
    rng = np.random.default_rng(SEED + 1)
    out = {}

    # ---- P2 / P3 / P3b : the region and its mechanism -----------------------
    a_big = 100.0
    per_n = {}
    for n in (2, 4, 6, 8):
        draws = 20_000 if n == 6 else 8_000
        S = goe(rng, n, draws)
        A = antisym(rng, n, draws)
        J = S + a_big * A

        ev_S = np.linalg.eigvalsh(S)
        posdef = ev_S.min(axis=1) > 0
        min_re = np.linalg.eigvals(J).real.min(axis=1)
        stable = min_re > 0

        # plane-average criterion (the registered mechanism)
        crit = np.empty(draws, dtype=bool)
        sub = min(draws, 4000)
        for i in range(sub):
            crit[i] = plane_averages(S[i], A[i]).min() > 0
        agree = float(np.mean(crit[:sub] == stable[:sub]))

        region = (~posdef) & stable
        per_n[n] = dict(
            draws=int(draws),
            frac_posdef=float(posdef.mean()),
            frac_stable_large_a=float(stable.mean()),
            frac_potential_free_but_predictive=float(region.mean()),
            plane_criterion_agreement=agree,
            plane_criterion_draws=int(sub),
            ratio_stable_over_posdef=(float(stable.mean() / posdef.mean())
                                      if posdef.mean() > 0 else float("inf")),
        )
        say(f"  n={n}: P(S>0)={posdef.mean():.5f}  P(stable @a=100)={stable.mean():.4f}  "
            f"P(no potential & predictive)={region.mean():.4f}  "
            f"plane-criterion agreement={agree:.4f}")

    out["per_n"] = per_n
    out["P2_fraction_n6"] = per_n[6]["frac_potential_free_but_predictive"]
    out["P2_pass"] = bool(out["P2_fraction_n6"] >= 0.10)
    out["P3_agreements"] = {str(k): v["plane_criterion_agreement"] for k, v in per_n.items()}
    out["P3_min_agreement"] = float(min(v["plane_criterion_agreement"] for v in per_n.values()))
    out["P3_n2_stable_fraction"] = per_n[2]["frac_stable_large_a"]
    out["P3_pass"] = bool(out["P3_min_agreement"] >= 0.98
                          and abs(out["P3_n2_stable_fraction"] - 0.5) <= 0.02)
    out["P3b_ratio_n6"] = per_n[6]["ratio_stable_over_posdef"]
    out["P3b_pass"] = bool(out["P3b_ratio_n6"] >= 10.0)
    say(f"  P2  pass = {out['P2_pass']}  (fraction {out['P2_fraction_n6']:.4f}, "
        f"null predicts 0.000)")
    say(f"  P3  pass = {out['P3_pass']}  (min agreement {out['P3_min_agreement']:.4f}, "
        f"n=2 stable {out['P3_n2_stable_fraction']:.4f})")
    say(f"  P3b pass = {out['P3b_pass']}  (ratio {out['P3b_ratio_n6']:.1f})")

    # ---- P2b : not weighted potential games either --------------------------
    n = 6
    hits, resids = 0, []
    tries = 0
    while hits < 200 and tries < 20_000:
        tries += 1
        S = goe(rng, n)
        A = antisym(rng, n)
        J = S + a_big * A
        if np.linalg.eigvalsh(S).min() > 0:
            continue
        if np.linalg.eigvals(J).real.min() <= 0:
            continue
        hits += 1
        resids.append(weighted_potential_residual(J, rng))
    resids = np.array(resids)
    out["P2b"] = dict(
        sampled=int(hits),
        residual_min=float(resids.min()),
        residual_median=float(np.median(resids)),
        frac_above_0p1=float((resids > 0.1).mean()),
    )
    out["P2b_pass"] = bool(out["P2b"]["frac_above_0p1"] >= 0.99)
    say(f"  P2b pass = {out['P2b_pass']}  (frac with weighted-potential residual > 0.1 = "
        f"{out['P2b']['frac_above_0p1']:.4f}, min residual {resids.min():.4f})")

    # ---- P4 : the n=2 threshold (identity) ----------------------------------
    errs = []
    for _ in range(200):
        S = goe(rng, 2)
        ev = np.linalg.eigvalsh(S)
        if ev.min() >= 0 or ev.sum() <= 0:      # need indefinite S with tr S > 0
            continue
        A = antisym(rng, 2)
        pred = math.sqrt(2.0 * ev.max() * abs(ev.min()))

        def unstable(a):
            return -np.linalg.eigvals(S + a * A).real.min()

        lo, hi = 1e-6, 1e4
        if unstable(lo) < 0 or unstable(hi) > 0:
            continue
        a_c = brentq(unstable, lo, hi, xtol=1e-14, rtol=1e-15)
        errs.append(abs(a_c - pred) / pred)
    errs = np.array(errs)
    out["P4"] = dict(cases=int(errs.size), rel_err_max=float(errs.max()),
                     rel_err_median=float(np.median(errs)))
    out["P4_pass"] = bool(errs.max() <= 1e-6)
    say(f"  P4  pass = {out['P4_pass']}  (a_c vs sqrt(2*lmax*|lmin|), max rel err "
        f"{errs.max():.2e} over {errs.size} cases)")

    # ---- P5 : a nonlinear two-player game, no potential, still predicts -----
    # L1 = 1/2 x1^2 + (a/sqrt2) x1 x2 + k x1^4/4
    # L2 = -1/4 x2^2 - (a/sqrt2) x1 x2 + k x2^4/4
    # pseudo-gradient g = (dL1/dx1, dL2/dx2); symmetric part of its Jacobian at 0
    # is diag(1, -1/2) -- indefinite, so no potential has a minimum there.
    a_g, kap = 3.0, 0.5
    c = a_g / math.sqrt(2.0)

    def g_game(x):
        return np.array([x[0] + c * x[1] + kap * x[0] ** 3,
                         -c * x[0] - 0.5 * x[1] + kap * x[1] ** 3])

    J0 = np.array([[1.0, c], [-c, -0.5]])
    S0 = 0.5 * (J0 + J0.T)
    X = rng.uniform(-1, 1, (100, 2))                 # 100 starts, run together
    for _ in range(400_000):
        gx = np.stack([X[:, 0] + c * X[:, 1] + kap * X[:, 0] ** 3,
                       -c * X[:, 0] - 0.5 * X[:, 1] + kap * X[:, 1] ** 3], axis=1)
        X = X - 1e-3 * gx
        if not np.all(np.isfinite(X)):
            break
    norms = np.linalg.norm(X, axis=1)
    norms = np.where(np.isfinite(norms), norms, np.inf)
    final = norms.tolist()
    conv = int((norms < 1e-8).sum())
    loop = random_loop(np.random.default_rng(7), 2, radius=0.6, verts=40)
    circ = abs(loop_integral_field(g_game, loop))
    out["P5"] = dict(
        S_eigs=[float(v) for v in np.linalg.eigvalsh(S0)],
        J_eig_real=[float(v) for v in np.linalg.eigvals(J0).real],
        runs=100, converged=int(conv),
        max_final_norm=float(np.max(final)),
        circulation=float(circ),
        exact_gradient_field=bool(abs(J0[0, 1] - J0[1, 0]) < 1e-15),
    )
    out["P5_pass"] = bool(conv >= 95 and circ >= 0.01)
    say(f"  P5  pass = {out['P5_pass']}  (converged {conv}/100, circulation {circ:.4f}, "
        f"sym-part eigs {out['P5']['S_eigs'][0]:.3f}/{out['P5']['S_eigs'][1]:.3f})")

    rec("legB", "results", out)
    return out


# ============================================================================
# LEG C — the selector, in CS not physics              P6 P7 P8 P11-selector
# ============================================================================
#
# Integer multiplication. Four real schemes, each recursing to a base case.
# Structural constants (a, b, adds, temps, evals) are properties of the
# algorithm; the six magnitudes are the cost model.

SCHEMES = [
    # name          a  b  alpha(adds/word) gamma(temps) delta(eval divisions)
    ("schoolbook",  4, 2, 3.0,  2.0,  0.0),
    ("karatsuba",   3, 2, 4.0,  2.0,  0.0),
    ("toom3",       5, 3, 8.0,  3.0,  5.0),
    ("toom4",       7, 4, 15.0, 4.0, 12.0),
]
MAG_NAMES = ["c_mul", "c_add", "c_call", "c_mem", "c_eval", "n_base"]
MAG_CENTRE = np.array([1.0, 0.3, 20.0, 0.5, 2.0, 32.0])
MAG_LO = np.array([1e-2, 3e-3, 0.2, 5e-3, 2e-2, 2.0])
MAG_HI = np.array([1e2, 30.0, 2000.0, 50.0, 200.0, 512.0])


def cost(scheme, N, mags):
    """T_s(N) for one scheme, recursing to the base case."""
    _, a, b, alpha, gamma, delta = scheme
    c_mul, c_add, c_call, c_mem, c_eval, n_base = mags
    per_word = alpha * c_add + gamma * c_mem + delta * c_eval
    total, n, mult = 0.0, float(N), 1.0
    for _ in range(200):
        if n <= n_base:
            break
        total += mult * (per_word * n + c_call * a)
        mult *= a
        n /= b
    return total + mult * c_mul * n * n


def exponent(scheme):
    _, a, b, *_ = scheme
    return math.log(a) / math.log(b)


def best_scheme(N, mags):
    costs = [cost(s, N, mags) for s in SCHEMES]
    i = int(np.argmin(costs))
    return i, costs[i]


def readout_exp(mags, sizes):
    return np.array([exponent(SCHEMES[best_scheme(N, mags)[0]]) for N in sizes])


def readout_const(mags, sizes):
    out = []
    for N in sizes:
        i, c = best_scheme(N, mags)
        out.append(math.log(c) - exponent(SCHEMES[i]) * math.log(N))
    return np.array(out)


def jacobian_log(fn, mags, sizes, h=1e-4):
    """d readout / d ln(magnitude), central differences in log space."""
    k = len(mags)
    cols = []
    for j in range(k):
        mp, mm = mags.copy(), mags.copy()
        mp[j] *= math.exp(h)
        mm[j] *= math.exp(-h)
        cols.append((fn(mp, sizes) - fn(mm, sizes)) / (2 * h))
    return np.stack(cols, axis=1)


def numeric_rank(J, tol=1e-8):
    sv = np.linalg.svd(J, compute_uv=False)
    if sv[0] == 0:
        return 0, sv
    return int((sv > tol * sv[0]).sum()), sv


def leg_C():
    say("\n=== LEG C — the selector, in CS not physics (AT RISK) ===")
    rng = np.random.default_rng(SEED + 2)
    out = {}
    N_op = 2 ** 14
    sizes = [2 ** e for e in (10, 11, 12, 13, 14, 15)]

    # ---- P7 : do the magnitudes actually flip the winner? -------------------
    n_samp = 4000
    # Latin hypercube in log space
    u = (rng.permuted(np.tile(np.arange(n_samp)[:, None], (1, 6)), axis=0)
         + rng.uniform(size=(n_samp, 6))) / n_samp
    mags = np.exp(np.log(MAG_LO) + u * (np.log(MAG_HI) - np.log(MAG_LO)))

    winners = np.array([best_scheme(N_op, m)[0] for m in mags])
    exps = np.array([exponent(SCHEMES[i]) for i in winners])
    counts = {SCHEMES[i][0]: int((winners == i).sum()) for i in range(len(SCHEMES))}
    freqs = {k: v / n_samp for k, v in counts.items()}
    n_schemes = sum(1 for v in freqs.values() if v >= 0.02)
    uniq_exp = sorted({round(float(e), 6) for e, i in zip(exps, winners)
                       if freqs[SCHEMES[i][0]] >= 0.02})
    out["P7"] = dict(samples=n_samp, N=N_op, winner_counts=counts,
                     winner_freqs=freqs, schemes_above_2pct=n_schemes,
                     distinct_exponents=uniq_exp)
    out["P7_pass"] = bool(n_schemes >= 3 and len(uniq_exp) >= 3)
    say(f"  winners over the box: {counts}")
    say(f"  P7  pass = {out['P7_pass']}  ({n_schemes} schemes >=2%, exponents {uniq_exp})")

    # ---- P6 : exponent is magnitude-blind inside a cell (identity) ----------
    interior, blind = 0, 0
    checked = 0
    for m in mags[:400]:
        base = best_scheme(N_op, m)[0]
        pert_ok = True
        for j in range(6):
            for s in (+1, -1):
                mm = m.copy()
                mm[j] *= math.exp(s * 1e-4)
                if best_scheme(N_op, mm)[0] != base:
                    pert_ok = False
        checked += 1
        if pert_ok:
            interior += 1
            Je = jacobian_log(readout_exp, m, sizes)
            if np.abs(Je).max() == 0.0:
                blind += 1
    out["P6"] = dict(checked=checked, interior=interior, exactly_blind=blind)
    out["P6_pass"] = bool(interior > 0 and blind == interior)
    say(f"  P6  pass = {out['P6_pass']}  (identity: {blind}/{interior} interior points "
        f"have dR_exp/dln(theta) == 0 exactly)")

    # ---- P8 : one rank instrument, three readouts ---------------------------
    ranks_exp, ranks_const, svs_e, svs_c = [], [], [], []
    used = 0
    for m in mags[:400]:
        base = best_scheme(N_op, m)[0]
        ok = True
        for j in range(6):
            for s in (+1, -1):
                mm = m.copy()
                mm[j] *= math.exp(s * 1e-4)
                if best_scheme(N_op, mm)[0] != base:
                    ok = False
        if not ok:
            continue
        used += 1
        Je = jacobian_log(readout_exp, m, sizes)
        Jc = jacobian_log(readout_const, m, sizes)
        re, se = numeric_rank(Je)
        rc, sc = numeric_rank(Jc)
        ranks_exp.append(re)
        ranks_const.append(rc)
        svs_e.append(se)
        svs_c.append(sc)
        if used >= 120:
            break

    # floor-2 control: Gibbs exchange rate, <x> = grad log Z, on an exponential family
    d = 5
    states = rng.normal(size=(40, d))
    lam0 = rng.normal(scale=0.5, size=d)

    def gibbs_mean(lam):
        lp = states.dot(lam)
        w = np.exp(lp - logsumexp(lp))
        return states.T.dot(w)

    hcd = 1e-5
    Jg = np.stack([(gibbs_mean(lam0 + hcd * np.eye(d)[j])
                    - gibbs_mean(lam0 - hcd * np.eye(d)[j])) / (2 * hcd)
                   for j in range(d)], axis=1)
    rg, sg = numeric_rank(Jg)

    out["P8"] = dict(
        base_points=used,
        rank_exponent_mode=int(np.bincount(ranks_exp).argmax()) if ranks_exp else None,
        rank_exponent_all_zero=bool(all(r == 0 for r in ranks_exp)),
        rank_constant_mode=int(np.bincount(ranks_const).argmax()) if ranks_const else None,
        rank_constant_full_frac=float(np.mean([r == 6 for r in ranks_const])) if ranks_const else 0.0,
        constant_sv_ratio_median=float(np.median([s[-1] / s[0] for s in svs_c])) if svs_c else None,
        rank_gibbs=int(rg),
        gibbs_sv_ratio=float(sg[-1] / sg[0]),
        tolerance=1e-8,
    )
    out["P8_pass"] = bool(out["P8"]["rank_exponent_all_zero"]
                          and out["P8"]["rank_constant_full_frac"] >= 0.95
                          and rg == d)
    say(f"  ranks with ONE tolerance 1e-8: exponent={set(ranks_exp)}  "
        f"constant mode={out['P8']['rank_constant_mode']} "
        f"(full in {out['P8']['rank_constant_full_frac']:.2f})  gibbs={rg}/{d}")
    say(f"  P8  pass = {out['P8_pass']}")

    # ---- P11 selector half : the cell boundary carries a kink ---------------
    kinks = []
    base = MAG_CENTRE.copy()
    for j, name in enumerate(MAG_NAMES):
        grid = np.exp(np.linspace(np.log(MAG_LO[j]), np.log(MAG_HI[j]), 4001))
        wins = []
        for v in grid:
            m = base.copy()
            m[j] = v
            wins.append(best_scheme(N_op, m)[0])
        wins = np.array(wins)
        for idx in np.where(np.diff(wins) != 0)[0]:
            lo, hi = grid[idx], grid[idx + 1]

            def winner_at(v):
                m = base.copy()
                m[j] = v
                return best_scheme(N_op, m)[0]

            def vstar(v):
                m = base.copy()
                m[j] = v
                return math.log(best_scheme(N_op, m)[1])

            w_lo = winner_at(lo)
            for _ in range(80):                      # bisect to the crossing
                mid = math.sqrt(lo * hi)
                if winner_at(mid) == w_lo:
                    lo = mid
                else:
                    hi = mid
            xc = math.sqrt(lo * hi)
            eps = 1e-3
            sl = (vstar(lo) - vstar(lo * math.exp(-eps))) / eps
            sr = (vstar(hi * math.exp(eps)) - vstar(hi)) / eps
            gap = abs(sl - sr) / max(abs(sl), abs(sr), 1e-300)
            v_lo, v_hi = vstar(lo), vstar(hi)
            kinks.append(dict(magnitude=name, crossing=float(xc),
                              slope_left=float(sl), slope_right=float(sr),
                              slope_gap_rel=float(gap),
                              value_jump_rel=float(abs(v_hi - v_lo) / max(abs(v_lo), 1e-300))))
    out["P11_selector"] = dict(
        crossings=len(kinks),
        detail=kinks,
        min_slope_gap_rel=float(min(k["slope_gap_rel"] for k in kinks)) if kinks else None,
        max_value_jump_rel=float(max(k["value_jump_rel"] for k in kinks)) if kinks else None,
    )
    out["P11_selector_pass"] = bool(
        kinks and min(k["slope_gap_rel"] for k in kinks) >= 0.10
        and max(k["value_jump_rel"] for k in kinks) <= 1e-6)
    say(f"  P11-selector pass = {out['P11_selector_pass']}  "
        f"({len(kinks)} cell crossings, min one-sided slope gap "
        f"{out['P11_selector']['min_slope_gap_rel']:.3f}, value continuous to "
        f"{out['P11_selector']['max_value_jump_rel']:.2e})")

    # ---- POST-HOC diagnostics (not registered; run after P8/P11 failed) ----
    # P8 came back rank 4, not the registered 6, with the smallest singular value
    # exactly 0 -- so the deficiency is structural, not numerical. Two candidate
    # causes, both testable: (i) n_base is a *count*, not a magnitude, so it has
    # no derivative at all; (ii) c_add, c_mem and c_eval enter the cost only
    # through the single combination alpha*c_add + gamma*c_mem + delta*c_eval.
    diag = {}
    interior_pts = []
    for m in mags[:400]:
        base = best_scheme(N_op, m)[0]
        if all(best_scheme(N_op, np.where(np.arange(6) == j, m * math.exp(s * 1e-4), m))[0]
               == base for j in range(6) for s in (+1, -1)):
            interior_pts.append(m)
        if len(interior_pts) >= 60:
            break

    dn, cols3, ident_ranks = [], [], []
    for m in interior_pts:
        Jc = jacobian_log(readout_const, m, sizes)
        dn.append(float(np.abs(Jc[:, 5]).max()))               # d/dln n_base
        cols3.append(numeric_rank(Jc[:, [1, 3, 4]])[0])         # c_add, c_mem, c_eval

        # rank on the identifiable coordinates: (c_mul, c_call, per-word scale)
        def readout_ident(theta, szs):
            mm = m.copy()
            mm[0] *= theta[0]
            mm[2] *= theta[1]
            mm[1] *= theta[2]
            mm[3] *= theta[2]
            mm[4] *= theta[2]
            return readout_const(mm, szs)

        Ji = jacobian_log(readout_ident, np.ones(3), sizes)
        ident_ranks.append(numeric_rank(Ji)[0])

    diag["n_base_derivative_max"] = float(np.max(dn))
    diag["rank_of_three_per_word_columns"] = dict(
        mode=int(np.bincount(cols3).argmax()), values=sorted(set(int(v) for v in cols3)))
    diag["rank_on_identifiable_coordinates"] = dict(
        mode=int(np.bincount(ident_ranks).argmax()),
        full_frac=float(np.mean([r == 3 for r in ident_ranks])), dim=3)
    diag["diagnosis"] = (
        "n_base is a structural count with identically zero derivative, and the "
        "three per-word magnitudes enter only through one linear functional per "
        "scheme; the registered rank 6 was unattainable in the cost model I wrote."
    )

    # P11: split the crossings into magnitude crossings and count crossings
    mag_k = [k for k in kinks if k["magnitude"] != "n_base"]
    cnt_k = [k for k in kinks if k["magnitude"] == "n_base"]
    diag["P11_split"] = dict(
        magnitude_crossings=len(mag_k),
        magnitude_min_slope_gap=float(min(k["slope_gap_rel"] for k in mag_k)) if mag_k else None,
        magnitude_max_value_jump=float(max(k["value_jump_rel"] for k in mag_k)) if mag_k else None,
        count_crossings=len(cnt_k),
        count_max_slope_gap=float(max(k["slope_gap_rel"] for k in cnt_k)) if cnt_k else None,
        count_min_value_jump=float(min(k["value_jump_rel"] for k in cnt_k)) if cnt_k else None,
        reading=("three regularity classes, separated without being told apart: a "
                 "magnitude gives a smooth value; a selector cell boundary gives a "
                 "continuous value with a kinked slope; a structural count gives a "
                 "discontinuous value with no slope on either side."),
    )
    out["posthoc"] = diag
    say(f"  [post-hoc] d(const)/d ln n_base max = {diag['n_base_derivative_max']:.3e} "
        f"(a count, not a magnitude)")
    say(f"  [post-hoc] rank of the 3 per-word columns = "
        f"{diag['rank_of_three_per_word_columns']['mode']} of 3")
    say(f"  [post-hoc] rank on identifiable coordinates = "
        f"{diag['rank_on_identifiable_coordinates']['mode']}/3 "
        f"(full in {diag['rank_on_identifiable_coordinates']['full_frac']:.2f})")
    say(f"  [post-hoc] P11 split: {len(mag_k)} magnitude crossings "
        f"(min slope gap {diag['P11_split']['magnitude_min_slope_gap']:.3f}, value jump "
        f"<= {diag['P11_split']['magnitude_max_value_jump']:.1e}); "
        f"{len(cnt_k)} count crossings (slope gap <= "
        f"{diag['P11_split']['count_max_slope_gap']:.3f}, value jump >= "
        f"{diag['P11_split']['count_min_value_jump']:.1e})")

    rec("legC", "results", out)
    return out


# ============================================================================
# LEG D — floor 1's response type                        P9 P10 P11-floor1
# ============================================================================

def turning_points(V, E, L, rlo=1e-6, rhi=1e6, npts=4000):
    """Bracket and solve f(r) = 2(E - V(r)) - L^2/r^2 = 0 (m = 1)."""
    def f(r):
        return 2.0 * (E - V(r)) - L * L / (r * r)

    grid = np.exp(np.linspace(math.log(rlo), math.log(rhi), npts))
    vals = np.array([f(r) for r in grid])
    sign_changes = np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0]
    if len(sign_changes) < 2:
        return None
    i, j = sign_changes[0], sign_changes[-1]
    r1 = brentq(f, grid[i], grid[i + 1], xtol=1e-15, rtol=8.9e-16)
    r2 = brentq(f, grid[j], grid[j + 1], xtol=1e-15, rtol=8.9e-16)
    if r2 <= r1 * (1 + 1e-9):
        return None
    return r1, r2


def apsidal_ratio(V, E, L, order=400):
    """omega_r / omega_theta = 2*pi / delta_theta, by Gauss-Legendre after the
    r = c + h sin(u) substitution that removes the turning-point singularities."""
    tp = turning_points(V, E, L)
    if tp is None:
        return None
    r1, r2 = tp
    c, h = 0.5 * (r1 + r2), 0.5 * (r2 - r1)
    u, w = np.polynomial.legendre.leggauss(order)
    u = u * (math.pi / 2)
    w = w * (math.pi / 2)
    r = c + h * np.sin(u)
    f = np.array([2.0 * (E - V(x)) - L * L / (x * x) for x in r])
    g = f / ((r - r1) * (r2 - r))
    g = np.maximum(g, 1e-300)
    dtheta = 2.0 * np.sum(w * (L / (r * r)) / np.sqrt(g))
    return 2.0 * math.pi / dtheta


def L_max_sq(V, E, rlo=1e-4, rhi=1e4):
    """max over r of 2 r^2 (E - V(r)) -- the circular-orbit angular momentum."""
    grid = np.exp(np.linspace(math.log(rlo), math.log(rhi), 20000))
    vals = np.array([2.0 * r * r * (E - V(r)) for r in grid])
    return float(vals.max())


def leg_D():
    say("\n=== LEG D — floor 1's response type (AT RISK) ===")
    out = {}

    # ---- P9 : Bertrand (theorem check on the quadrature) --------------------
    kep = lambda k: (lambda r: -k / r)
    har = lambda k: (lambda r: 0.5 * k * r * r)

    r_kep = apsidal_ratio(kep(1.0), -0.5, 0.8)
    r_har = apsidal_ratio(har(1.0), 1.0, 0.5)
    out["P9"] = dict(kepler_ratio=float(r_kep), harmonic_ratio=float(r_har),
                     kepler_err=abs(r_kep - 1.0), harmonic_err=abs(r_har - 2.0))
    out["P9_pass"] = bool(abs(r_kep - 1.0) <= 1e-5 and abs(r_har - 2.0) <= 1e-5)
    say(f"  P9  pass = {out['P9_pass']}  (Kepler {r_kep:.9f} vs 1, harmonic "
        f"{r_har:.9f} vs 2)")

    # ---- P10 : magnitude-blindness, and the eccentricity discriminator ------
    sweeps = {}
    for name, Vk, Esign in (("kepler", kep, -1.0), ("harmonic", har, +1.0)):
        vals = []
        for k in (1e-2, 1e-1, 1e0, 1e1, 1e2):
            for scale in (1e-1, 1e0, 1e1):
                E = Esign * scale * (k if name == "kepler" else 1.0)
                Lm2 = L_max_sq(Vk(k), E)
                if Lm2 <= 0:
                    continue
                for rho in (0.95, 0.7, 0.4):
                    r = apsidal_ratio(Vk(k), E, math.sqrt(rho * Lm2))
                    if r is not None:
                        vals.append(r)
        vals = np.array(vals)
        target = 1.0 if name == "kepler" else 2.0
        sweeps[name] = dict(n=int(vals.size), mean=float(vals.mean()),
                            spread=float(vals.max() - vals.min()),
                            max_err=float(np.abs(vals - target).max()),
                            target=target, constants_of_motion=3)
        say(f"  {name}: ratio over 4 decades of k x 3 of |E| x 3 eccentricities -> "
            f"spread {sweeps[name]['spread']:.2e}, max err {sweeps[name]['max_err']:.2e}")

    powers = {}
    for alpha, k, E in ((1.0, 1.0, 1.0), (3.0, 1.0, 1.0), (-0.5, -1.0, -0.2)):
        Vp = (lambda kk, aa: (lambda r: kk * r ** aa))(k, alpha)
        vals = []
        for kscale in (1e-2, 1e-1, 1e0, 1e1, 1e2):
            Vs = (lambda kk, aa: (lambda r: kk * r ** aa))(k * kscale, alpha)
            Es = E * (kscale if alpha > 0 else kscale)
            Lm2 = L_max_sq(Vs, Es)
            if Lm2 <= 0:
                continue
            for rho in (0.95, 0.7, 0.4):
                r = apsidal_ratio(Vs, Es, math.sqrt(rho * Lm2))
                if r is not None:
                    vals.append((kscale, rho, r))
        arr = np.array([v[2] for v in vals])
        # k-invariance at matched eccentricity
        by_rho = {}
        for ks, rho, r in vals:
            by_rho.setdefault(rho, []).append(r)
        k_spread = max(max(v) - min(v) for v in by_rho.values())
        ecc_spread = float(arr.max() - arr.min())
        near_circ = float(np.mean([r for ks, rho, r in vals if rho == 0.95]))
        # rational within 1e-4 with denominator <= 12?
        rational = any(abs(near_circ - p / q) < 1e-4
                       for q in range(1, 13) for p in range(1, 5 * q))
        powers[f"alpha={alpha}"] = dict(
            near_circular_ratio=near_circ,
            predicted_near_circular=(math.sqrt(alpha + 2.0) if alpha + 2 > 0 else None),
            k_invariance_spread=float(k_spread),
            eccentricity_spread=ecc_spread,
            rational_p_over_q=bool(rational),
        )
        say(f"  V=k r^{alpha}: near-circular ratio {near_circ:.6f} "
            f"(sqrt(alpha+2)={math.sqrt(alpha + 2):.6f}), k-spread {k_spread:.2e}, "
            f"eccentricity spread {ecc_spread:.4f}, rational={rational}")

    out["P10"] = dict(bertrand=sweeps, power_law=powers)
    out["P10_pass"] = bool(
        all(s["max_err"] <= 1e-5 for s in sweeps.values())
        and all(p["k_invariance_spread"] <= 1e-5 for p in powers.values())
        and all(not p["rational_p_over_q"] for p in powers.values())
        and all(p["eccentricity_spread"] > 1e-3 for p in powers.values())
    )
    say(f"  P10 pass = {out['P10_pass']}")

    # ---- P11 floor-1 half : count jumps, value analytic --------------------
    k, L = 1.0, 0.8

    def V_delta(delta):
        return lambda r: -k / r + delta / (r * r)

    def E_circ(delta):
        rc = 2.0 * (delta + 0.5 * L * L) / k
        return V_delta(delta)(rc) + 0.5 * L * L / (rc * rc)

    hd = 1e-6
    dl = (E_circ(0.0) - E_circ(-hd)) / hd
    dr = (E_circ(hd) - E_circ(0.0)) / hd
    slope_gap = abs(dl - dr) / max(abs(dl), abs(dr))

    prec = []
    for delta in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1):
        r = apsidal_ratio(V_delta(delta), -0.5, L)
        if r is None:
            continue
        dtheta = 2 * math.pi / r
        prec.append((delta, abs(dtheta - 2 * math.pi)))
    xs = np.log(np.array([p[0] for p in prec]))
    ys = np.log(np.array([p[1] for p in prec]))
    slope = float(np.polyfit(xs, ys, 1)[0])

    # count: rational (closed orbit) at delta = 0, irrational for delta != 0
    r0 = apsidal_ratio(V_delta(0.0), -0.5, L)
    rp = apsidal_ratio(V_delta(1e-2), -0.5, L)
    count0 = 3 if abs(r0 - round(r0)) < 1e-6 else 2
    countp = 3 if abs(rp - round(rp)) < 1e-6 else 2

    out["P11_floor1"] = dict(
        E_circ_slope_left=float(dl), E_circ_slope_right=float(dr),
        E_circ_slope_gap_rel=float(slope_gap),
        precession_exponent=slope,
        ratio_at_delta_0=float(r0), ratio_at_delta_1e_2=float(rp),
        count_at_delta_0=count0, count_at_delta_1e_2=countp,
        precession_points=[[float(a), float(b)] for a, b in prec],
    )
    out["P11_floor1_pass"] = bool(slope_gap <= 1e-4
                                  and abs(slope - 1.0) <= 0.03
                                  and count0 == 3 and countp == 2)
    say(f"  P11-floor1 pass = {out['P11_floor1_pass']}  "
        f"(count 3 -> 2 at delta=0; E_circ one-sided slopes agree to "
        f"{slope_gap:.2e}; precession ~ delta^{slope:.4f})")

    rec("legD", "results", out)
    return out


# ============================================================================

def main():
    say("P-C — variational principles come in exactly two kinds?")
    say(f"seed = {SEED}")
    a = leg_A()
    b = leg_B()
    c = leg_C()
    d = leg_D()

    verdict = {
        "P1_two_poles_identity": a["P1_pass"],
        "P2_potential_free_but_predictive": b["P2_pass"],
        "P2b_not_weighted_potential": b["P2b_pass"],
        "P3_plane_average_mechanism": b["P3_pass"],
        "P3b_condition_count_halves": b["P3b_pass"],
        "P4_n2_threshold_identity": b["P4_pass"],
        "P5_nonlinear_game_predicts": b["P5_pass"],
        "P6_exponent_blind_identity": c["P6_pass"],
        "P7_selector_cells_nontrivial": c["P7_pass"],
        "P8_one_rank_instrument": c["P8_pass"],
        "P11_selector_kink": c["P11_selector_pass"],
        "P9_bertrand_identity": d["P9_pass"],
        "P10_floor1_magnitude_blind": d["P10_pass"],
        "P11_floor1_analytic_value": d["P11_floor1_pass"],
    }
    at_risk = ["P2_potential_free_but_predictive", "P2b_not_weighted_potential",
               "P3_plane_average_mechanism", "P3b_condition_count_halves",
               "P5_nonlinear_game_predicts", "P7_selector_cells_nontrivial",
               "P8_one_rank_instrument", "P10_floor1_magnitude_blind",
               "P11_floor1_analytic_value"]
    identities = ["P1_two_poles_identity", "P4_n2_threshold_identity",
                  "P6_exponent_blind_identity", "P9_bertrand_identity",
                  "P11_selector_kink"]

    OUT["verdict"] = verdict
    OUT["at_risk_predictions"] = at_risk
    OUT["declared_identities"] = identities
    OUT["at_risk_passed"] = sum(verdict[k] for k in at_risk)
    OUT["at_risk_total"] = len(at_risk)
    OUT["identities_passed"] = sum(verdict[k] for k in identities)
    OUT["seed"] = SEED
    OUT["runtime_s"] = round(time.time() - T0, 1)

    say("\n=== VERDICT ===")
    for k, v in verdict.items():
        tag = "AT RISK " if k in at_risk else "identity"
        say(f"  [{tag}] {k}: {'PASS' if v else 'FAIL'}")
    say(f"\n  at-risk passed: {OUT['at_risk_passed']}/{OUT['at_risk_total']}")
    say(f"  identities passed: {OUT['identities_passed']}/{len(identities)}")
    say(f"  runtime {OUT['runtime_s']}s")

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2, sort_keys=True)
    say("\nwrote verdict.json")


if __name__ == "__main__":
    main()
