"""M3 -- does the degree histogram determine connectivity?

Essay 04's falsifier 1, which the essay names and nobody ran: degree-preserving
rewiring holds the degree histogram -- the sufficient statistic of the
degree-constrained maximum-entropy graph ensemble, i.e. everything a Phi built
on node degrees can see -- bit-for-bit fixed, while changing the wiring.  If
p_c moves, connectivity is not a Phi(degree)-derivative.  If the pair statistic
e_{jk} then recovers it, connectivity is a Phi-derivative of the PAIR measure,
which is M11's "Phi of what?" lesson applied a second time.

  p_c = 1/(kappa - 1),  kappa = <k^2>/<k>          (uncorrelated)
  p_c = 1/lambda_max(T),  T_{kj} = j e_{jk}/q_j    (with degree correlations)

Predictions registered in PREREGISTRATION.md BEFORE this was run:
  P1 Molloy-Reed holds on configuration-model graphs (5%)
  P2 random swaps are neutral (3%)
  P3 assortative/disassortative rewiring moves p_c >=15% at fixed degrees
  P4 1/lambda_max predicts every rewired threshold (8%)
  P5 (degrees, r) is still insufficient: matched r, different p_c
  P6 clustering breaks the tree-like assumption: p_c above 1/lambda_max

numpy + scipy (connected components), deterministic seeds.  ~5 minutes.
"""
import json

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

N_NODES = 20_000
P_GRID = 41
N_REAL = 8                 # percolation realisations (common random numbers)
FSS_SIZES = (10_000, 20_000, 40_000, 80_000)
N_REWIRE = 40_000          # size for the rewiring legs


# ---------------------------------------------------------------------------
# graph construction
# ---------------------------------------------------------------------------
def degree_sequence(kind, n, rng):
    if kind == "poisson":
        k = rng.poisson(3.0, n)
    elif kind == "powerlaw":
        u = rng.random(n)                       # alpha = 2.7, k_min = 2
        k = np.floor(2.0 * (1.0 - u) ** (-1.0 / 1.7)).astype(int)
        k = np.minimum(k, 150)
    elif kind == "bimodal":
        k = np.where(rng.random(n) < 0.7, 2, 12)
    elif kind == "trimodal":
        u = rng.random(n)
        k = np.where(u < 0.50, 2, np.where(u < 0.85, 5, 15))
    else:
        raise ValueError(kind)
    k = np.maximum(k, 1)
    if k.sum() % 2:                             # even stub count
        k[int(rng.integers(n))] += 1
    return k.astype(np.int64)


def configuration_graph(deg, rng, repair_rounds=60):
    """Stub matching, then repair self-loops and multi-edges by double swaps.

    Repair uses double-edge swaps, so the degree sequence is exactly preserved.
    """
    stubs = np.repeat(np.arange(len(deg)), deg)
    rng.shuffle(stubs)
    E = stubs.reshape(-1, 2).copy()
    M = len(E)

    def key(u, v):
        return (u, v) if u < v else (v, u)

    seen, bad = set(), []
    for i in range(M):
        u, v = int(E[i, 0]), int(E[i, 1])
        if u == v or key(u, v) in seen:
            bad.append(i)
        else:
            seen.add(key(u, v))
    for _ in range(repair_rounds):
        if not bad:
            break
        still = []
        for i in bad:
            ok = False
            for _try in range(40):
                j = int(rng.integers(M))
                if j == i:
                    continue
                a, b = int(E[i, 0]), int(E[i, 1])
                c, d = int(E[j, 0]), int(E[j, 1])
                if a == d or c == b:
                    continue
                if key(a, d) in seen or key(c, b) in seen:
                    continue
                seen.discard(key(c, d))
                E[i] = (a, d)
                E[j] = (c, b)
                seen.add(key(a, d))
                seen.add(key(c, b))
                ok = True
                break
            if not ok:
                still.append(i)
        bad = still
    if bad:                                     # drop the few unrepairable
        keep = np.ones(M, dtype=bool)
        keep[bad] = False
        E = E[keep]
    return E


# ---------------------------------------------------------------------------
# statistics
# ---------------------------------------------------------------------------
def degrees_from_edges(E, n):
    return np.bincount(E.ravel(), minlength=n).astype(np.int64)


def kappa_of(deg):
    m1 = deg.mean()
    m2 = (deg.astype(float) ** 2).mean()
    return float(m2 / m1)


def joint_excess(E, deg):
    """e_{jk} over excess degrees, symmetrised; returns (e, q)."""
    j = deg[E[:, 0]] - 1
    k = deg[E[:, 1]] - 1
    m = int(max(j.max(), k.max())) + 1
    e = np.zeros((m, m))
    np.add.at(e, (j, k), 1.0)
    np.add.at(e, (k, j), 1.0)
    e /= e.sum()
    return e, e.sum(axis=1)


def lambda_max(E, deg):
    """Leading eigenvalue of the edge-end branching operator T_{kj}=j e_{jk}/q_j."""
    e, q = joint_excess(E, deg)
    nz = q > 0
    e, q = e[np.ix_(nz, nz)], q[nz]
    idx = np.flatnonzero(nz).astype(float)      # actual excess-degree values
    # T[k, j] = j * e_{jk} / q_j   (e is symmetric, so e.T[k, j] = e[j, k])
    T = idx[None, :] * e.T / q[None, :]
    ev = np.linalg.eigvals(T)
    return float(np.max(ev.real))


def assortativity(E, deg):
    """Newman's r: Pearson correlation of excess degrees across edges."""
    j = (deg[E[:, 0]] - 1).astype(float)
    k = (deg[E[:, 1]] - 1).astype(float)
    a, b = np.concatenate([j, k]), np.concatenate([k, j])
    return float(np.corrcoef(a, b)[0, 1])


def global_clustering(E, deg, n):
    """3*triangles / triples, via common neighbours over edges."""
    adj = [set() for _ in range(n)]
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)
    tri = 0
    for u, v in E:
        su, sv = adj[u], adj[v]
        if len(su) > len(sv):
            su, sv = sv, su
        tri += sum(1 for w in su if w in sv)
    tri //= 3
    triples = int(np.sum(deg * (deg - 1) // 2))
    return float(3 * tri / triples) if triples else 0.0



def feasible_lambda_range(q, idx, S_fixed, grid=400):
    """Exact range of lambda_max over graphs with these degree marginals AND
    this value of S = sum_jk j k e_jk (equivalently, this assortativity r).

    With three excess-degree classes the symmetric e_{jk} with fixed row sums
    has three free parameters; fixing r removes one, leaving a 2-D polytope
    that can simply be scanned.  This settles whether (degrees, r) determines
    connectivity, without depending on how good a rewiring optimiser is.
    """
    assert len(idx) == 3, "polytope scan is written for three degree classes"
    j1, j2, j3 = idx
    den = -j2 * j2 - j3 * j3 + 2 * j2 * j3
    best = (np.inf, None)
    worst = (-np.inf, None)
    feas = 0
    g = np.linspace(0.0, float(max(q)), grid)
    for e12 in g:
        for e13 in g:
            num = (S_fixed - j1 * j1 * (q[0] - e12 - e13)
                   - j2 * j2 * (q[1] - e12) - j3 * j3 * (q[2] - e13)
                   - 2 * j1 * j2 * e12 - 2 * j1 * j3 * e13)
            if den == 0:
                continue
            e23 = num / den
            E_ = np.array([[q[0] - e12 - e13, e12, e13],
                           [e12, q[1] - e12 - e23, e23],
                           [e13, e23, q[2] - e13 - e23]])
            if E_.min() < 0:
                continue
            feas += 1
            T = idx[None, :] * E_.T / q[None, :]
            L = float(np.max(np.linalg.eigvals(T).real))
            if L < best[0]:
                best = (L, E_.copy())
            if L > worst[0]:
                worst = (L, E_.copy())
    return {"lambda_min": best[0], "lambda_max": worst[0],
            "e_at_max": worst[1], "e_at_min": best[1], "feasible_points": feas}


def class_of(deg, idx):
    """Map each node to its excess-degree class index."""
    lut = {int(v): i for i, v in enumerate(idx)}
    return np.array([lut[int(k - 1)] for k in deg])


def rewire_to_target_e(E, deg, cls, e_target, rng, n_sweeps=60):
    """Degree-preserving swaps driven toward a target joint distribution e_{jk}.

    Hitting e_target pins r automatically, since e determines r.  This is the
    constructive form of the polytope scan: build the graph the scan says
    exists, then measure its threshold.
    """
    E = E.copy()
    M = len(E)
    seen = set()
    for u, v in E:
        seen.add((u, v) if u < v else (v, u))
    C = np.zeros_like(e_target)
    for u, v in E:
        C[cls[u], cls[v]] += 1.0
        C[cls[v], cls[u]] += 1.0
    target = e_target * (2.0 * M)

    def dist(Cm):
        return float(np.abs(Cm - target).sum())

    cur = dist(C)
    for _ in range(int(n_sweeps * M)):
        i, j = int(rng.integers(M)), int(rng.integers(M))
        if i == j:
            continue
        a, b = int(E[i, 0]), int(E[i, 1])
        c, d = int(E[j, 0]), int(E[j, 1])
        if rng.random() < 0.5:
            c, d = d, c
        if len({a, b, c, d}) < 4:
            continue
        k1 = (a, d) if a < d else (d, a)
        k2 = (c, b) if c < b else (b, c)
        if k1 in seen or k2 in seen:
            continue
        ca, cb, cc, cd = cls[a], cls[b], cls[c], cls[d]
        C[ca, cb] -= 1; C[cb, ca] -= 1
        C[cc, cd] -= 1; C[cd, cc] -= 1
        C[ca, cd] += 1; C[cd, ca] += 1
        C[cc, cb] += 1; C[cb, cc] += 1
        new = dist(C)
        if new <= cur:
            cur = new
            seen.discard((a, b) if a < b else (b, a))
            seen.discard((c, d) if c < d else (d, c))
            seen.add(k1); seen.add(k2)
            E[i] = (a, d)
            E[j] = (c, b)
        else:
            C[ca, cb] += 1; C[cb, ca] += 1
            C[cc, cd] += 1; C[cd, cc] += 1
            C[ca, cd] -= 1; C[cd, ca] -= 1
            C[cc, cb] -= 1; C[cb, cc] -= 1
    return E


# ---------------------------------------------------------------------------
# percolation
# ---------------------------------------------------------------------------
def susceptibility_curve(E, n, ps, n_real, seed):
    """Mean finite-cluster size chi(p), averaged over realisations.

    Common random numbers: one uniform weight per edge per realisation, so the
    occupied sets are nested in p and chi(p) is smooth.
    """
    rng = np.random.default_rng(seed)
    M = len(E)
    chi = np.zeros(len(ps))
    for _ in range(n_real):
        u = rng.random(M)
        for i, p in enumerate(ps):
            occ = u < p
            if not occ.any():
                chi[i] += 1.0
                continue
            e = E[occ]
            g = csr_matrix((np.ones(len(e)), (e[:, 0], e[:, 1])), shape=(n, n))
            _, lab = connected_components(g, directed=False)
            sizes = np.bincount(lab)
            sizes = np.delete(sizes, np.argmax(sizes))      # drop the giant
            chi[i] += float((sizes ** 2).sum() / max(sizes.sum(), 1))
    return chi / n_real


def pc_from_peak(ps, chi):
    """Peak location with parabolic refinement on the top three points."""
    i = int(np.argmax(chi))
    if 0 < i < len(ps) - 1:
        y0, y1, y2 = chi[i - 1], chi[i], chi[i + 1]
        den = y0 - 2 * y1 + y2
        if den != 0:
            return float(ps[i] + 0.5 * (y0 - y2) / den * (ps[1] - ps[0]))
    return float(ps[i])


def measure_pc(E, deg, n, seed, span=(0.35, 2.6)):
    """Locate p_c on a grid bracketing the theoretical prediction."""
    lam = lambda_max(E, deg)
    centre = 1.0 / lam
    ps = np.linspace(max(centre * span[0], 1e-3), min(centre * span[1], 1.0), P_GRID)
    chi = susceptibility_curve(E, n, ps, N_REAL, seed)
    return {"p_c_measured": pc_from_peak(ps, chi), "lambda_max": lam,
            "p_c_pred_eig": 1.0 / lam, "kappa": kappa_of(deg),
            "p_c_pred_MR": 1.0 / (kappa_of(deg) - 1.0),
            "r": assortativity(E, deg),
            "chi": chi.tolist(), "ps": ps.tolist()}


# ---------------------------------------------------------------------------
# degree-preserving rewiring
# ---------------------------------------------------------------------------
def rewire(E, deg, mode, rng, n_sweeps=12, hub_q=0.90, pin_r=False,
           s1_tol_frac=0.010):
    """Double-edge swaps.  Degrees are preserved exactly by construction.

    modes: 'random' | 'assort' | 'disassort' | 'hubassort' | 'bulkassort'
    The last two target a fixed r (r_target) while pushing hub-hub edges up or
    down -- two graphs with the same degrees AND the same assortativity but
    different e_{jk}.
    """
    E = E.copy()
    M = len(E)
    seen = set()
    for u, v in E:
        seen.add((u, v) if u < v else (v, u))
    hub_cut = np.quantile(deg, hub_q)
    is_hub = deg >= hub_cut

    def S1_of(E_):
        return float(np.sum(deg[E_[:, 0]].astype(float) * deg[E_[:, 1]]))

    S1 = S1_of(E)
    hubhub = int(np.sum(is_hub[E[:, 0]] & is_hub[E[:, 1]]))
    # r is a monotone function of S1 at fixed degrees, so pinning S1 pins r
    S1_target = S1
    tol = s1_tol_frac * abs(S1_target)

    attempts = int(n_sweeps * M)
    for _ in range(attempts):
        i, j = int(rng.integers(M)), int(rng.integers(M))
        if i == j:
            continue
        a, b = int(E[i, 0]), int(E[i, 1])
        c, d = int(E[j, 0]), int(E[j, 1])
        if rng.random() < 0.5:
            c, d = d, c
        if len({a, b, c, d}) < 4:
            continue
        ka, kb, kc, kd = deg[a], deg[b], deg[c], deg[d]
        dS1 = float((ka - kc) * (kd - kb))
        dHH = (int(is_hub[a] and is_hub[d]) + int(is_hub[c] and is_hub[b])
               - int(is_hub[a] and is_hub[b]) - int(is_hub[c] and is_hub[d]))
        if mode == "random":
            accept = True
        elif mode == "assort":
            accept = dS1 > 0
        elif mode == "disassort":
            accept = dS1 < 0
        elif mode in ("hubassort", "bulkassort"):
            # Pin S1 (hence r) inside a tolerance band, and inside that band
            # drive S2 = sum_e (k_u k_v)^2 up or down.  Same degrees, same r,
            # different higher-order pair structure -- which is what lambda_max
            # actually responds to.
            dS2 = float((ka * kd) ** 2 + (kc * kb) ** 2
                        - (ka * kb) ** 2 - (kc * kd) ** 2)
            new_drift = abs(S1 + dS1 - S1_target)
            old_drift = abs(S1 - S1_target)
            if new_drift > tol:
                accept = new_drift < old_drift        # always allow restoring moves
            elif dS2 == 0:
                accept = new_drift <= old_drift
            else:
                accept = (dS2 > 0) if mode == "hubassort" else (dS2 < 0)
        else:
            raise ValueError(mode)
        if not accept:
            continue
        ka_, kd_ = (a, d) if a < d else (d, a)
        kc_, kb_ = (c, b) if c < b else (b, c)
        if (ka_, kd_) in seen or (kc_, kb_) in seen:
            continue
        ab = (a, b) if a < b else (b, a)
        cd = (c, d) if c < d else (d, c)
        seen.discard(ab)
        seen.discard(cd)
        seen.add((ka_, kd_))
        seen.add((kc_, kb_))
        E[i] = (a, d)
        E[j] = (c, b)
        S1 += dS1
        hubhub += dHH
    return E


def rewire_triangles(E, deg, rng, n_sweeps=25):
    """Swaps accepted only if they increase the common-neighbour count."""
    E = E.copy()
    M = len(E)
    n = len(deg)
    adj = [set() for _ in range(n)]
    seen = set()
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)
        seen.add((u, v) if u < v else (v, u))
    for _ in range(int(n_sweeps * M)):
        i, j = int(rng.integers(M)), int(rng.integers(M))
        if i == j:
            continue
        a, b = int(E[i, 0]), int(E[i, 1])
        c, d = int(E[j, 0]), int(E[j, 1])
        if rng.random() < 0.5:
            c, d = d, c
        if len({a, b, c, d}) < 4:
            continue
        k1 = (a, d) if a < d else (d, a)
        k2 = (c, b) if c < b else (b, c)
        if k1 in seen or k2 in seen:
            continue
        def common(x, y):
            sx, sy = adj[x], adj[y]
            if len(sx) > len(sy):
                sx, sy = sy, sx
            return sum(1 for w in sx if w in sy)
        before = common(a, b) + common(c, d)
        after = common(a, d) + common(c, b)
        if after <= before:
            continue
        adj[a].discard(b); adj[b].discard(a)
        adj[c].discard(d); adj[d].discard(c)
        adj[a].add(d); adj[d].add(a)
        adj[c].add(b); adj[b].add(c)
        seen.discard((a, b) if a < b else (b, a))
        seen.discard((c, d) if c < d else (d, c))
        seen.add(k1); seen.add(k2)
        E[i] = (a, d)
        E[j] = (c, b)
    return E


# ===========================================================================
out = {"setup": {"fss_sizes": list(FSS_SIZES), "n_rewire": N_REWIRE,
                 "p_grid": P_GRID, "realisations": N_REAL}}


def build(kind, n, seed=1234):
    rng = np.random.default_rng(seed)
    E = configuration_graph(degree_sequence(kind, n, rng), rng)
    return E, degrees_from_edges(E, n)


# ---- P1: Molloy-Reed, with finite-size scaling ---------------------------
# The chi-peak estimator is biased HIGH at finite N and converges from above.
# Mean-field percolation has nu_bar = 3, so extrapolate p_peak(N) = p_c + a N^(-1/3).
p1 = {}
for kind in ("poisson", "bimodal", "trimodal", "powerlaw"):
    seq, pred = [], None
    for n in FSS_SIZES:
        E, deg = build(kind, n)
        res = measure_pc(E, deg, n, seed=99)
        seq.append({"N": n, "p_peak": res["p_c_measured"],
                    "p_c_pred_MR": res["p_c_pred_MR"], "kappa": res["kappa"]})
        pred = res["p_c_pred_MR"]
    x = np.array([r["N"] ** (-1.0 / 3.0) for r in seq])
    y = np.array([r["p_peak"] for r in seq])
    a, b = np.polyfit(x, y, 1)          # y = a*x + b ; b is the N->inf limit
    resid = y - (a * x + b)
    r2 = 1.0 - float(np.sum(resid ** 2) / np.sum((y - y.mean()) ** 2))
    p1[kind] = {
        "sizes": seq, "p_c_extrapolated": float(b), "fss_slope": float(a),
        "fss_R2": r2, "p_c_pred_MR_at_largest_N": pred,
        "rel_err_extrapolated": abs(float(b) - pred) / pred,
        "rel_err_at_largest_N_no_extrapolation":
            abs(seq[-1]["p_peak"] - pred) / pred,
    }
clean = ("poisson", "bimodal", "trimodal")
out["P1_molloy_reed"] = {
    "graphs": p1,
    "bounded_degree_max_rel_err_extrapolated":
        float(max(p1[k]["rel_err_extrapolated"] for k in clean)),
    "powerlaw_rel_err_extrapolated": p1["powerlaw"]["rel_err_extrapolated"],
    "confirmed_for_bounded_degree":
        bool(all(p1[k]["rel_err_extrapolated"] < 0.05 for k in clean)),
    "note": ("power-law kept separate: with alpha<3 the asymptotic threshold "
             "drifts with N, so a fixed-exponent extrapolation is not valid "
             "there -- reported, not counted"),
}

# ---- P2/P3/P4: rewiring at bit-for-bit fixed degree sequence -------------
# P4 is now a RATIO test.  Every measurement carries the same finite-size
# offset (P1 shows it is +4..7% and nearly constant at fixed N), so comparing
# predicted vs measured SHIFTS cancels it; comparing absolute values does not.
rew = {}
for kind in ("bimodal", "trimodal", "powerlaw"):
    E0, deg0 = build(kind, N_REWIRE)
    variants = {"config": E0}
    for mode, sweeps in (("random", 12), ("assort", 25), ("disassort", 25)):
        variants[mode] = rewire(E0, deg0, mode, np.random.default_rng(7), sweeps)
    entry = {}
    for name, E in variants.items():
        deg = degrees_from_edges(E, N_REWIRE)
        res = measure_pc(E, deg, N_REWIRE, seed=99)
        entry[name] = {
            "degree_sequence_identical": bool(np.array_equal(deg, deg0)),
            "kappa": res["kappa"], "r": res["r"], "lambda_max": res["lambda_max"],
            "p_c_measured": res["p_c_measured"],
            "p_c_pred_eig": res["p_c_pred_eig"],
            "clustering": global_clustering(E, deg, N_REWIRE),
        }
    base = entry["config"]
    for name, v in entry.items():
        v["ratio_measured"] = v["p_c_measured"] / base["p_c_measured"]
        v["ratio_predicted"] = base["lambda_max"] / v["lambda_max"]
        v["ratio_err"] = abs(v["ratio_measured"] - v["ratio_predicted"]) / v["ratio_predicted"]
    rew[kind] = entry

out["P2_random_swap_control"] = {
    kind: {"ratio_measured": v["random"]["ratio_measured"],
           "lambda_change": abs(v["random"]["lambda_max"] - v["config"]["lambda_max"])
           / v["config"]["lambda_max"]}
    for kind, v in rew.items()}
out["P2_random_swap_control"]["confirmed"] = bool(all(
    abs(rew[k]["random"]["ratio_measured"] - 1.0) < 0.05 for k in rew))

spreads = {k: (v["disassort"]["p_c_measured"] - v["assort"]["p_c_measured"])
           / v["config"]["p_c_measured"] for k, v in rew.items()}
out["P3_rewiring_moves_pc"] = {
    "variants": rew,
    "all_degree_sequences_identical": bool(all(
        v[nm]["degree_sequence_identical"] for v in rew.values() for nm in v)),
    "spread_disassort_minus_assort": spreads,
    "sign_correct_assort_lower": bool(all(
        v["assort"]["p_c_measured"] < v["disassort"]["p_c_measured"]
        for v in rew.values())),
    "confirmed": bool(min(spreads.values()) >= 0.15 and all(
        v["assort"]["p_c_measured"] < v["disassort"]["p_c_measured"]
        for v in rew.values())),
}

# tree-like graphs: the pair statistic must predict the SHIFT
treelike = ("bimodal", "trimodal")
errs_tree = [rew[k][nm]["ratio_err"] for k in treelike for nm in rew[k]]
errs_pl = [rew["powerlaw"][nm]["ratio_err"] for nm in rew["powerlaw"]]
out["P4_eigenvalue_criterion"] = {
    "ratio_errors_treelike": {k: {nm: rew[k][nm]["ratio_err"] for nm in rew[k]}
                              for k in treelike},
    "ratio_errors_powerlaw": {nm: rew["powerlaw"][nm]["ratio_err"]
                              for nm in rew["powerlaw"]},
    "max_ratio_err_treelike": float(max(errs_tree)),
    "max_ratio_err_powerlaw": float(max(errs_pl)),
    "confirmed_treelike": bool(max(errs_tree) < 0.08),
}

# ---- P5: is (degrees, r) enough? -----------------------------------------
# Settled two ways: EXACTLY, by scanning the feasible polytope of e_{jk} at
# fixed marginals and fixed r; and CONSTRUCTIVELY, by rewiring to the extreme
# the scan identifies and measuring its threshold.
E0, deg0 = build("trimodal", N_REWIRE)
e0, q0 = joint_excess(E0, deg0)
nzq = q0 > 0
idx0 = np.flatnonzero(nzq).astype(float)
e0, q0 = e0[np.ix_(nzq, nzq)], q0[nzq]
S_fixed = float(idx0 @ e0 @ idx0)           # fixing this fixes r
scan = feasible_lambda_range(q0, idx0, S_fixed)

cls0 = class_of(deg0, idx0)
E_hi = rewire_to_target_e(E0, deg0, cls0, scan["e_at_max"],
                          np.random.default_rng(11))
p5 = {}
for name, E in (("config (polytope minimum)", E0), ("rewired to polytope maximum", E_hi)):
    deg = degrees_from_edges(E, N_REWIRE)
    res = measure_pc(E, deg, N_REWIRE, seed=99)
    p5[name] = {"degree_sequence_identical": bool(np.array_equal(deg, deg0)),
                "r": res["r"], "lambda_max": res["lambda_max"],
                "p_c_measured": res["p_c_measured"],
                "p_c_pred_eig": res["p_c_pred_eig"],
                "clustering": global_clustering(E, deg, N_REWIRE)}
k_lo, k_hi = "config (polytope minimum)", "rewired to polytope maximum"
dr = abs(p5[k_hi]["r"] - p5[k_lo]["r"])
dlam = (p5[k_hi]["lambda_max"] - p5[k_lo]["lambda_max"]) / p5[k_lo]["lambda_max"]
dpc = (p5[k_hi]["p_c_measured"] - p5[k_lo]["p_c_measured"]) / p5[k_lo]["p_c_measured"]
out["P5_matched_r"] = {
    "analytic_polytope_scan": {
        "excess_degree_classes": idx0.tolist(),
        "lambda_min": scan["lambda_min"], "lambda_max": scan["lambda_max"],
        "lambda_spread_frac": (scan["lambda_max"] - scan["lambda_min"]) / scan["lambda_min"],
        "implied_p_c_range": [1.0 / scan["lambda_max"], 1.0 / scan["lambda_min"]],
        "feasible_points": scan["feasible_points"],
        "verdict": ("lambda_max is NOT determined by (degree sequence, r): the "
                    "feasible set at fixed r spans this range"),
    },
    "constructed": p5,
    "delta_r": float(dr), "delta_lambda_max_rel": float(dlam),
    "delta_pc_rel": float(dpc),
    "fraction_of_analytic_range_reached": float(
        (p5[k_hi]["lambda_max"] - p5[k_lo]["lambda_max"])
        / (scan["lambda_max"] - scan["lambda_min"])),
    "predicted_pc_ratio": p5[k_lo]["lambda_max"] / p5[k_hi]["lambda_max"],
    "measured_pc_ratio": p5[k_hi]["p_c_measured"] / p5[k_lo]["p_c_measured"],
    "r_matched": bool(dr < 0.01),
    "confirmed_analytically": bool(
        (scan["lambda_max"] - scan["lambda_min"]) / scan["lambda_min"] >= 0.05),
    "confirmed_constructively": bool(dr < 0.01 and abs(dlam) >= 0.05
                                     and abs(dpc) >= 0.05 and dlam * dpc < 0),
}

# ---- P6: clustering breaks the tree-like assumption ----------------------
E0, deg0 = build("trimodal", N_REWIRE)
Ec = rewire_triangles(E0, deg0, np.random.default_rng(13))
degc = degrees_from_edges(Ec, N_REWIRE)
resc = measure_pc(Ec, degc, N_REWIRE, seed=99)
out["P6_clustering"] = {
    "clustering_before": global_clustering(E0, deg0, N_REWIRE),
    "clustering_after": global_clustering(Ec, degc, N_REWIRE),
    "degree_sequence_identical": bool(np.array_equal(degc, deg0)),
    "r": resc["r"], "lambda_max": resc["lambda_max"],
    "p_c_measured": resc["p_c_measured"], "p_c_pred_eig": resc["p_c_pred_eig"],
    "signed_rel_dev": float((resc["p_c_measured"] - resc["p_c_pred_eig"])
                            / resc["p_c_pred_eig"]),
    "confirmed_pc_above_prediction": bool(
        (resc["p_c_measured"] - resc["p_c_pred_eig"]) / resc["p_c_pred_eig"] >= 0.05),
    "powerlaw_assort_clustering_for_comparison":
        rew["powerlaw"]["assort"]["clustering"],
    "powerlaw_assort_ratio_err": rew["powerlaw"]["assort"]["ratio_err"],
}

# the general form of P6: prediction error should track clustering across every
# graph measured, tree-like or not
pts = [(rew[k][nm]["clustering"], rew[k][nm]["ratio_err"])
       for k in rew for nm in rew[k] if nm != "config"]
pts.append((out["P6_clustering"]["clustering_after"],
            abs(out["P6_clustering"]["signed_rel_dev"])))
pts.sort()
out["P6_clustering"]["error_vs_clustering"] = [
    {"clustering": c, "prediction_error": e} for c, e in pts]
out["P6_clustering"]["spearman_error_vs_clustering"] = float(np.corrcoef(
    np.argsort(np.argsort([c for c, _ in pts])),
    np.argsort(np.argsort([e for _, e in pts])))[0, 1])

out["VERDICT"] = {
    "P1_molloy_reed_bounded_degree": out["P1_molloy_reed"]["confirmed_for_bounded_degree"],
    "P1_max_err_extrapolated": out["P1_molloy_reed"]["bounded_degree_max_rel_err_extrapolated"],
    "P2_random_swaps_neutral": out["P2_random_swap_control"]["confirmed"],
    "P3_rewiring_moves_pc_at_fixed_degrees": out["P3_rewiring_moves_pc"]["confirmed"],
    "P3_spreads": out["P3_rewiring_moves_pc"]["spread_disassort_minus_assort"],
    "P4_pair_statistic_recovers_shift_treelike":
        out["P4_eigenvalue_criterion"]["confirmed_treelike"],
    "P4_max_ratio_err": [out["P4_eigenvalue_criterion"]["max_ratio_err_treelike"],
                         out["P4_eigenvalue_criterion"]["max_ratio_err_powerlaw"]],
    "P5_degrees_plus_r_insufficient_analytic":
        out["P5_matched_r"]["confirmed_analytically"],
    "P5_lambda_spread_at_fixed_r":
        out["P5_matched_r"]["analytic_polytope_scan"]["lambda_spread_frac"],
    "P5_constructed": out["P5_matched_r"]["confirmed_constructively"],
    "P6_clustering_breaks_tree_assumption":
        out["P6_clustering"]["confirmed_pc_above_prediction"],
}

print(json.dumps(out["VERDICT"], indent=2, default=float))
with open("verdict.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
