"""P-D — does the allometric exponent reduce to a partition function?

Tests invariants/FLOORS.md §3's only *negative* prediction: Kleiber's 3/4 should
not be derivable from a Phi; it should be a log-ratio of the branching geometry
(the proposed floor-4 signature).

Predictions registered in PREREGISTRATION.md before this ran.
Pure numpy/scipy, deterministic, ~40 s.
"""

import json
import math

import numpy as np
from scipy.optimize import minimize
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components, dijkstra, minimum_spanning_tree
from scipy.spatial import cKDTree
from scipy.special import gammaln, logsumexp

RNG_SEED = 20260727
OUT = {}


# --------------------------------------------------------------------------
# The network model.  Levels j = 0 (capillary) .. N (aorta), counted from the
# terminal units so that the capillary is the invariant unit (WBE's own
# convention).  A level-j vessel has n^(N-j) copies.
# --------------------------------------------------------------------------

def log_volume(N, n, betas, gamma, r_c=1.0, l_c=1.0):
    """log of V = sum_j n^(N-j) * pi * r_j^2 * l_j, in logs throughout.

    `betas` is either a scalar radius ratio or an array of length N giving the
    ratio used on each step upward from the capillary.
    """
    betas = np.broadcast_to(np.asarray(betas, dtype=float), (N,))
    j = np.arange(N + 1)
    log_r = np.log(r_c) + np.concatenate([[0.0], np.cumsum(-np.log(betas))])
    log_l = np.log(l_c) - j * np.log(gamma)
    log_terms = (N - j) * np.log(n) + np.log(np.pi) + 2 * log_r + log_l
    return logsumexp(log_terms)


def log_mass(N, n, betas, gamma, r_c=1.0, l_c=1.0, rho=1.0):
    return np.log(rho) + log_volume(N, n, betas, gamma, r_c, l_c)


def log_metabolism(N, n, B_c=1.0):
    """Metabolic rate = (per-capillary rate) x (number of capillaries)."""
    return np.log(B_c) + N * np.log(n)


def measured_theta(n, betas_fn, gamma, Ns, r_c=1.0, l_c=1.0, rho=1.0, B_c=1.0):
    """Log-log slope of B against M over a window of network depths."""
    lm = np.array([log_mass(N, n, betas_fn(N), gamma, r_c, l_c, rho) for N in Ns])
    lb = np.array([log_metabolism(N, n, B_c) for N in Ns])
    return float(np.polyfit(lm, lb, 1)[0])


def theta_star(n, beta, gamma):
    """(star): ln(multiplicity per level) / ln(rescaling per level).

    Valid where the volume sum is dominated by the aorta end, n*beta^2*gamma < 1.
    """
    return math.log(n) / (-math.log(beta ** 2 * gamma))


def theta_general(n, beta, gamma):
    """The full law, both dominance regimes:  theta = min(1, (star))."""
    return min(1.0, theta_star(n, beta, gamma))


WINDOW = list(range(200, 301, 10))


# ==========================================================================
# Leg A -- P1, P2: the exponent is the log-ratio, and n cancels
# ==========================================================================

def leg_A():
    res = {"P1_schemes": [], "regime_scan": []}
    ns = [2, 3, 4, 6, 10]

    schemes = [
        ("WBE: area-preserving + space-filling", lambda n: n ** -0.5, lambda n: n ** (-1 / 3)),
        ("Murray: area-increasing + space-filling", lambda n: n ** (-1 / 3), lambda n: n ** (-1 / 3)),
        ("minimum-surface: beta=n^-2/5", lambda n: n ** -0.4, lambda n: n ** (-1 / 3)),
        ("off-scheme A: beta=n^-0.45, gamma=n^-0.30", lambda n: n ** -0.45, lambda n: n ** -0.30),
        ("off-scheme B: beta=n^-0.60, gamma=n^-0.25", lambda n: n ** -0.60, lambda n: n ** -0.25),
        ("non-power: beta=0.6, gamma=0.7 (n-independent)", lambda n: 0.6, lambda n: 0.7),
    ]

    for label, bf, gf in schemes:
        for n in ns:
            beta, gamma = bf(n), gf(n)
            if beta ** 2 * gamma >= 1.0:
                continue
            nbg = n * beta ** 2 * gamma
            th_meas = measured_theta(n, lambda N: beta, gamma, WINDOW)
            res["P1_schemes"].append({
                "scheme": label, "n": n, "beta": beta, "gamma": gamma,
                "n_beta2_gamma": nbg,
                "regime": ("aorta-dominated" if nbg < 1 - 1e-9 else
                           "marginal" if nbg < 1 + 1e-9 else "capillary-dominated"),
                "theta_star": theta_star(n, beta, gamma),
                "theta_general": theta_general(n, beta, gamma),
                "theta_measured": th_meas,
                "rel_err_vs_star": abs(th_meas - theta_star(n, beta, gamma)) / theta_star(n, beta, gamma),
                "rel_err_vs_general": abs(th_meas - theta_general(n, beta, gamma)) / theta_general(n, beta, gamma),
            })

    # P1 as registered: (star) applies where its stated validity condition holds.
    valid = [r for r in res["P1_schemes"] if r["regime"] == "aorta-dominated"]
    res["P1_worst_rel_err_in_validity_region"] = max(r["rel_err_vs_star"] for r in valid)
    res["P1_n_in_validity_region"] = len(valid)
    res["P1_worst_rel_err_general_law"] = max(r["rel_err_vs_general"] for r in res["P1_schemes"])
    res["P1_n_total"] = len(res["P1_schemes"])

    # P2: n-invariance under the WBE rules
    wbe = [r for r in res["P1_schemes"] if r["scheme"].startswith("WBE")]
    thetas = [r["theta_measured"] for r in wbe]
    res["P2_wbe_by_n"] = [{"n": r["n"], "theta": r["theta_measured"]} for r in wbe]
    res["P2_spread"] = float(max(thetas) - min(thetas))
    res["P2_max_dev_from_0.75"] = float(max(abs(t - 0.75) for t in thetas))

    # Not registered: sweep beta through the dominance switch at n*beta^2*gamma = 1.
    n, gamma = 4, 4 ** (-1 / 3)
    beta_marginal = (1.0 / (n * gamma)) ** 0.5
    for x in np.linspace(0.75, 1.35, 25):
        beta = beta_marginal * x
        if beta ** 2 * gamma >= 1.0:
            continue
        res["regime_scan"].append({
            "beta_over_beta_marginal": float(x), "beta": float(beta),
            "n_beta2_gamma": float(n * beta ** 2 * gamma),
            "theta_measured": measured_theta(n, lambda N: beta, gamma, WINDOW),
            "theta_star": theta_star(n, beta, gamma),
            "theta_general": theta_general(n, beta, gamma),
        })

    # Registered: geometric (non-marginal) residuals decay exponentially in N;
    # the marginal case n*beta^2*gamma = 1 decays as ln(N+1)/(N ln n).
    conv = {"non_marginal": [], "marginal": []}
    n = 4
    for label, beta, gamma_, key in [
        ("WBE", n ** -0.5, n ** (-1 / 3), "non_marginal"),
        ("Murray", n ** (-1 / 3), n ** (-1 / 3), "marginal"),
    ]:
        th_pred = theta_general(n, beta, gamma_)
        for N in [20, 40, 80, 160, 320]:
            th = measured_theta(n, lambda M: beta, gamma_, [N, N + 1, N + 2, N + 3, N + 4])
            entry = {"label": label, "N": N, "theta": th, "residual": abs(th - th_pred)}
            if key == "marginal":
                # Registered form: theta_N = 1 - ln(N+1)/(N ln n).  That is the
                # chord from the origin; theta is measured as a *local* slope, so
                # the right comparison is the derivative of the same ln(N+1) term.
                entry["registered_residual_chord"] = math.log(N + 1) / (N * math.log(n))
                entry["local_slope_residual"] = 1.0 / ((N + 3) * math.log(n))
                entry["ratio_vs_registered"] = entry["residual"] / entry["registered_residual_chord"]
                entry["ratio_vs_local_slope"] = entry["residual"] / entry["local_slope_residual"]
                entry["from_below"] = bool(th < th_pred)
            conv[key].append(entry)
    res["convergence"] = conv
    return res


# ==========================================================================
# Leg B -- P3, P4, P5: what the optimizer actually selects
# ==========================================================================

def optimal_radius_ratio(n, gamma, N, flow_exponent=4.0, constraint="volume",
                         mu=1.0, Q0=1.0, seed=0):
    """Minimize hydrodynamic dissipation over *free* radii r_0..r_N.

    W = sum_k N_k R_k Q_k^2,  R_k = 8 mu l_k / (pi r_k^a),  Q_k = Q0 / n^k.
    Constraint is total volume or total wall surface area, held fixed.

    Nothing is assumed geometric: the ratios r_{k+1}/r_k come out of the
    optimizer.  Returns (median ratio in the bulk, spread across the bulk, sol).
    """
    k = np.arange(N + 1)
    l = gamma ** k                                   # l_k = l_c gamma^k
    Nk = n ** k.astype(float)
    Q = Q0 / Nk

    def log_dissipation(u):
        r = np.exp(u)
        w = Nk * (8 * mu * l / (np.pi * r ** flow_exponent)) * Q ** 2
        return logsumexp(np.log(w))

    def log_constraint(u):
        r = np.exp(u)
        c = Nk * np.pi * r ** 2 * l if constraint == "volume" else Nk * 2 * np.pi * r * l
        return logsumexp(np.log(c))

    target = log_constraint(np.zeros(N + 1))
    rng = np.random.default_rng(seed)
    u0 = rng.normal(0, 0.05, N + 1)
    sol = minimize(log_dissipation, u0, method="SLSQP",
                   constraints=[{"type": "eq", "fun": lambda u: log_constraint(u) - target}],
                   options={"maxiter": 3000, "ftol": 1e-14})
    ratios = np.exp(sol.x[1:] - sol.x[:-1])          # r_{k+1}/r_k = beta
    bulk = ratios[2:-2]                              # drop ends: boundary effects
    return float(np.median(bulk)), float(bulk.max() - bulk.min()), sol


def impedance_beta(n, m):
    """Radius ratio that cancels junction reflection for admittance Y ~ r^m.

    Root of g(b) = 1 - n b^m (parent admittance minus n child admittances),
    found by bisection rather than assumed.  g is decreasing in b.
    """
    lo, hi = 1e-12, 1.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if 1.0 - n * mid ** m > 0:
            lo = mid          # still under-matched: root lies above
        else:
            hi = mid
    return 0.5 * (lo + hi)


def leg_B():
    res = {"optimizers": [], "P3_magnitudes": [], "P3_structural": []}
    n, N = 4, 14
    gamma = n ** (-1 / 3)

    cases = [
        ("dissipation @ fixed volume (Murray)", 4.0, "volume", n ** (-1 / 3)),
        ("dissipation @ fixed surface", 4.0, "surface", n ** (-2 / 5)),
        ("turbulent (a=4.75) @ fixed volume", 4.75, "volume", n ** (-2 / 6.75)),
        ("shallow flow law (a=2) @ fixed volume", 2.0, "volume", n ** (-2 / 4)),
    ]
    for label, a, cons, beta_analytic in cases:
        beta_num, spread, sol = optimal_radius_ratio(n, gamma, N, a, cons)
        res["optimizers"].append({
            "cost": label, "flow_exponent": a, "constraint": cons,
            "beta_numeric": beta_num, "beta_analytic": beta_analytic,
            "beta_rel_err": abs(beta_num - beta_analytic) / beta_analytic,
            "bulk_ratio_spread": spread, "converged": bool(sol.success),
            "n_beta2_gamma": n * beta_num ** 2 * gamma,
            "theta_from_law": theta_general(n, beta_num, gamma),
            "theta_measured": measured_theta(n, lambda M: beta_num, gamma, WINDOW),
        })

    for m, name in [(2.0, "impedance matching, area (Y ~ r^2)"),
                    (2.5, "impedance matching, Womersley (Y ~ r^5/2)")]:
        beta_num = impedance_beta(n, m)
        res["optimizers"].append({
            "cost": name, "flow_exponent": None, "constraint": "zero reflection",
            "beta_numeric": beta_num, "beta_analytic": n ** (-1 / m),
            "beta_rel_err": abs(beta_num - n ** (-1 / m)) / n ** (-1 / m),
            "bulk_ratio_spread": 0.0, "converged": True,
            "n_beta2_gamma": n * beta_num ** 2 * gamma,
            "theta_from_law": theta_general(n, beta_num, gamma),
            "theta_measured": measured_theta(n, lambda M: beta_num, gamma, WINDOW),
        })

    for r in res["optimizers"]:
        r["law_vs_measured_rel_err"] = abs(r["theta_measured"] - r["theta_from_law"]) / r["theta_from_law"]
    res["P5_worst_rel_err"] = max(r["law_vs_measured_rel_err"] for r in res["optimizers"])

    # -- P3a: magnitudes.  Six decades on every dimensionful quantity, including
    #    the ones fed to the optimizer that selects beta.
    base_beta, _, _ = optimal_radius_ratio(n, gamma, N, 4.0, "volume", mu=1.0, Q0=1.0)
    base_theta = measured_theta(n, lambda M: base_beta, gamma, WINDOW)
    for label, kw, optkw in [
        ("r_c x 1e3", {"r_c": 1e3}, {}),
        ("l_c x 1e-3", {"l_c": 1e-3}, {}),
        ("rho x 1e6", {"rho": 1e6}, {}),
        ("B_c x 1e-6", {"B_c": 1e-6}, {}),
        ("viscosity mu x 1e6 (into optimizer)", {}, {"mu": 1e6}),
        ("flow Q0 x 1e-3 (into optimizer)", {}, {"Q0": 1e-3}),
        ("all of the above", {"r_c": 1e3, "l_c": 1e-3, "rho": 1e6, "B_c": 1e-6},
         {"mu": 1e6, "Q0": 1e-3}),
    ]:
        beta, _, _ = optimal_radius_ratio(n, gamma, N, 4.0, "volume", **optkw)
        th = measured_theta(n, lambda M: beta, gamma, WINDOW, **kw)
        res["P3_magnitudes"].append({
            "perturbation": label, "beta": beta, "theta": th,
            "beta_rel_change": abs(beta - base_beta) / base_beta,
            "rel_change_vs_base": abs(th - base_theta) / base_theta,
        })
    res["P3_base_theta"] = base_theta
    res["P3_max_theta_change"] = max(r["rel_change_vs_base"] for r in res["P3_magnitudes"])

    # -- P3b: the *structural* exponent of the flow law does move theta, and
    #    moves it exactly through the law.
    for a in [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0]:
        beta, _, _ = optimal_radius_ratio(n, gamma, N, a, "volume")
        res["P3_structural"].append({
            "flow_exponent_a": a, "beta_numeric": beta,
            "beta_analytic": n ** (-2 / (a + 2)),
            "theta_from_law": theta_general(n, beta, gamma),
            "theta_measured": measured_theta(n, lambda M: beta, gamma, WINDOW),
        })
    for r in res["P3_structural"]:
        r["rel_err"] = abs(r["theta_measured"] - r["theta_from_law"]) / r["theta_from_law"]
    return res


# ==========================================================================
# Leg C -- P6: mixed regions follow theta(f) = 3/(4-f)
# ==========================================================================

def leg_C():
    rows = []
    for n in [2, 4, 10]:
        gamma = n ** (-1 / 3)
        b_murray, b_area = n ** (-1 / 3), n ** (-0.5)
        for f in [0.0, 0.25, 0.5, 0.75, 1.0]:
            def betas_fn(N, f=f, b_m=b_murray, b_a=b_area):
                n_m = int(round(f * N))
                return np.concatenate([np.full(n_m, b_m), np.full(N - n_m, b_a)])
            th = measured_theta(n, betas_fn, gamma, WINDOW)
            th_pred = 3.0 / (4.0 - f)
            rows.append({"n": n, "f": f, "theta_measured": th,
                         "theta_predicted_3_over_4_minus_f": th_pred,
                         "rel_err": abs(th - th_pred) / th_pred})
    spread = {}
    for f in [0.0, 0.25, 0.5, 0.75, 1.0]:
        ths = [r["theta_measured"] for r in rows if r["f"] == f]
        spread[str(f)] = float(max(ths) - min(ths))
    return {"rows": rows, "spread_across_n": spread,
            "worst_rel_err": max(r["rel_err"] for r in rows)}


# ==========================================================================
# Leg D -- P7: the independent dimensional route, theta = d/(d+1)
# ==========================================================================

def directed_supply_cost(pts, src, k=64):
    """Banavar-style *directed* efficient network: every link carries flow
    monotonically away from the source.  Each site attaches to its nearest
    neighbour that is strictly closer to the source, so path length tracks
    euclidean distance rather than wandering.

    Returns (total flow-volume C = sum_links flow*length, fallback count)."""
    N = len(pts)
    r = np.sqrt(((pts - pts[src]) ** 2).sum(1))
    order = np.argsort(r, kind="stable")
    rank = np.empty(N, dtype=np.int64)
    rank[order] = np.arange(N)

    kk = min(N, k)
    dist, idx = cKDTree(pts).query(pts, k=kk)
    pathlen = np.zeros(N)
    fallback = 0
    for i in order:
        if i == src:
            continue
        for m in range(1, kk):
            j = idx[i, m]
            if rank[j] < rank[i]:
                pathlen[i] = pathlen[j] + dist[i, m]
                break
        else:
            pathlen[i] = r[i]          # attach straight to the source
            fallback += 1
    return float(pathlen.sum()), fallback


def mst_supply_cost(pts, src, k=24):
    """Minimum spanning tree: the *registered* construction.  Minimizes total
    wire length, which is not the transport functional -- kept as a control."""
    N = len(pts)
    kk = min(N - 1, k)
    dist, idx = cKDTree(pts).query(pts, k=kk + 1)
    rows = np.repeat(np.arange(N), kk)
    cols = idx[:, 1:].ravel()
    vals = dist[:, 1:].ravel()
    mst = minimum_spanning_tree(coo_matrix((vals, (rows, cols)), shape=(N, N)))
    sym = mst + mst.T
    ncomp, _ = connected_components(sym, directed=False)
    if ncomp != 1:
        return None, ncomp
    return float(dijkstra(sym, directed=False, indices=src).sum()), 1


def leg_D():
    rng = np.random.default_rng(RNG_SEED)
    out = {"rows": [], "fits": []}
    sizes = [500, 1000, 2000, 4000, 8000, 16000]
    for d in [2, 3, 4]:
        rec = {"N": [], "lower": [], "directed": [], "mst": []}
        for N in sizes:
            L = N ** (1.0 / d)                  # constant density
            pts = rng.random((N, d)) * L
            src = int(np.argmin(((pts - pts.mean(0)) ** 2).sum(1)))
            lower = float(np.sqrt(((pts - pts[src]) ** 2).sum(1)).sum())
            directed, fallback = directed_supply_cost(pts, src)
            mst, ncomp = mst_supply_cost(pts, src)
            out["rows"].append({"d": d, "N": N, "C_lower_bound": lower,
                                "C_directed": directed, "C_mst": mst,
                                "directed_fallbacks": fallback, "mst_components": ncomp})
            rec["N"].append(N); rec["lower"].append(lower)
            rec["directed"].append(directed); rec["mst"].append(mst)
        ln = np.log(rec["N"])
        fit = {"d": d, "C_exponent_predicted": (d + 1) / d,
               "theta_predicted_d_over_d_plus_1": d / (d + 1.0)}
        for key in ("lower", "directed", "mst"):
            if any(v is None for v in rec[key]):
                continue
            e = float(np.polyfit(ln, np.log(rec[key]), 1)[0])
            fit[f"C_exponent_{key}"] = e
            fit[f"theta_{key}"] = 1.0 / e
            fit[f"rel_err_{key}"] = abs(1 / e - d / (d + 1.0)) / (d / (d + 1.0))
        out["fits"].append(fit)
    return out


# ==========================================================================
# Leg E -- P8: the honest Phi attempt, and a genuine floor-2 control
# ==========================================================================

def exp_family(x1, x2, lam1, lam2, log_base=None):
    """means and covariance for p(i) ~ mult_i * exp(lam1 x1_i + lam2 x2_i)."""
    lw = lam1 * x1 + lam2 * x2
    if log_base is not None:
        lw = lw + log_base
    lw -= lw.max()
    w = np.exp(lw)
    w /= w.sum()
    m1, m2 = float(w @ x1), float(w @ x2)
    c11 = float(w @ (x1 - m1) ** 2)
    c22 = float(w @ (x2 - m2) ** 2)
    c12 = float(w @ ((x1 - m1) * (x2 - m2)))
    return m1, m2, np.array([[c11, c12], [c12, c22]])


def ising2d_enumeration(L=4):
    """Exact enumeration of the periodic LxL Ising model: energy and magnetization
    over all 2^(L*L) configurations.  Two statistics that are genuinely not
    functions of one another."""
    n_sites = L * L
    states = np.arange(2 ** n_sites, dtype=np.int64)
    bits = ((states[:, None] >> np.arange(n_sites)[None, :]) & 1).astype(np.int8)
    s = (2 * bits - 1).astype(np.int8).reshape(-1, L, L)
    E = -(s * np.roll(s, 1, axis=1)).sum((1, 2)) - (s * np.roll(s, 1, axis=2)).sum((1, 2))
    M = s.sum((1, 2))
    return E.astype(float), M.astype(float)


def leg_E():
    out = {}
    n, N_lo, N_hi = 4, 60, 300
    gamma = n ** (-1 / 3)
    Ns = np.arange(N_lo, N_hi + 1)
    for label, beta in [("allometric family, WBE (beta = n^-1/2)", n ** -0.5),
                        ("allometric family, Murray (marginal)", n ** (-1 / 3))]:
        x1 = np.array([log_mass(int(N), n, beta, gamma) for N in Ns])   # ln M
        x2 = np.array([log_metabolism(int(N), n) for N in Ns])          # ln B
        rows = []
        for lam in [1e-3, 1e-2, 1e-1, 1e0, 1e1]:
            for direction in [(-1.0, 0.0), (0.0, -1.0), (-0.7, -0.7)]:
                m1, m2, C = exp_family(x1, x2, lam * direction[0], lam * direction[1])
                corr = C[0, 1] / math.sqrt(C[0, 0] * C[1, 1])
                ev = np.linalg.eigvalsh(C)
                rows.append({
                    "lambda": lam, "direction": list(direction),
                    "mean_lnM": m1, "mean_lnB": m2,
                    "corr": float(corr), "one_minus_corr": float(1.0 - corr),
                    "conjugate_ratio_dlnB_dlnM": float(C[0, 1] / C[0, 0]),
                    "cov_eig_ratio_small_over_large": float(abs(ev[0]) / abs(ev[1])),
                })
        ratios = [r["conjugate_ratio_dlnB_dlnM"] for r in rows]
        out[label] = {
            "rows": rows, "ratio_min": min(ratios), "ratio_max": max(ratios),
            "ratio_rel_variation": float((max(ratios) - min(ratios)) / abs(np.mean(ratios))),
            "max_one_minus_corr": max(r["one_minus_corr"] for r in rows),
            "max_cov_eig_ratio": max(r["cov_eig_ratio_small_over_large"] for r in rows),
        }

    # --- registered control: mean-field Ising.  Recorded even though it turns
    #     out to be degenerate for the same structural reason (E and M are both
    #     functions of the single order parameter m), which is itself the point.
    n_spins = 400
    k = np.arange(n_spins + 1)
    m = (2.0 * k - n_spins) / n_spins
    log_mult = gammaln(n_spins + 1) - gammaln(k + 1) - gammaln(n_spins - k + 1)
    E_mf = -0.5 * n_spins * m ** 2
    M_mf = n_spins * m
    rows = []
    h = 0.02
    for bT in [0.6, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.3, 1.6, 2.0]:
        mE, mM, C = exp_family(E_mf, M_mf, -bT, bT * h, log_base=log_mult)
        corr = C[0, 1] / math.sqrt(C[0, 0] * C[1, 1])
        rows.append({"beta": bT, "mean_E": mE, "mean_M": mM, "corr": float(corr),
                     "abs_corr": float(abs(corr)),
                     "conjugate_ratio_dM_dE": float(C[0, 1] / C[0, 0])})
    ratios = [r["conjugate_ratio_dM_dE"] for r in rows]
    out["control_registered_mean_field_ising"] = {
        "rows": rows,
        "min_abs_corr": min(r["abs_corr"] for r in rows),
        "max_abs_corr": max(r["abs_corr"] for r in rows),
        "ratio_rel_variation": float((max(ratios) - min(ratios)) / abs(np.mean(ratios))),
        "note": ("registered control, and it fails its own registered threshold: "
                 "E and M are both functions of the single order parameter m, so "
                 "(E,M) traces a curve and |corr| reaches ~1 over part of the range"),
    }

    # --- replacement control: 4x4 periodic 2D Ising, exact enumeration.
    E2, M2 = ising2d_enumeration(4)
    rows = []
    h = 0.05
    for bT in [0.10, 0.20, 0.30, 0.40, 0.44, 0.50, 0.60, 0.80, 1.00]:
        mE, mM, C = exp_family(E2, M2, -bT, bT * h)
        corr = C[0, 1] / math.sqrt(C[0, 0] * C[1, 1])
        ev = np.linalg.eigvalsh(C)
        rows.append({"beta": bT, "mean_E": mE, "mean_M": mM, "corr": float(corr),
                     "abs_corr": float(abs(corr)),
                     "cov_eig_ratio_small_over_large": float(abs(ev[0]) / abs(ev[1])),
                     "conjugate_ratio_dM_dE": float(C[0, 1] / C[0, 0])})
    ratios = [r["conjugate_ratio_dM_dE"] for r in rows]
    out["control_2d_ising_4x4"] = {
        "rows": rows, "max_abs_corr": max(r["abs_corr"] for r in rows),
        "min_cov_eig_ratio": min(r["cov_eig_ratio_small_over_large"] for r in rows),
        "ratio_min": min(ratios), "ratio_max": max(ratios),
        "ratio_rel_variation": float((max(ratios) - min(ratios)) / abs(np.mean(ratios))),
    }
    return out


# ==========================================================================

def main():
    print("Leg A: the log-ratio law ...")
    OUT["legA"] = leg_A()
    a = OUT["legA"]
    print(f"  P1 worst rel err, {a['P1_n_in_validity_region']} cases in (star)'s "
          f"validity region: {a['P1_worst_rel_err_in_validity_region']:.3e}")
    print(f"  P1 worst rel err, all {a['P1_n_total']} cases vs min(1,(star)): "
          f"{a['P1_worst_rel_err_general_law']:.3e}")
    print(f"  P2 WBE spread across n: {a['P2_spread']:.3e}; "
          f"max |theta-3/4| = {a['P2_max_dev_from_0.75']:.3e}")

    print("Leg B: what the optimizer selects ...")
    OUT["legB"] = leg_B()
    for r in OUT["legB"]["optimizers"]:
        print(f"  {r['cost']:42s} beta={r['beta_numeric']:.5f} "
              f"(analytic {r['beta_analytic']:.5f}, err {r['beta_rel_err']:.1e})  "
              f"theta={r['theta_measured']:.5f}  law={r['theta_from_law']:.5f}")
    print(f"  P5 worst |measured-law|/law: {OUT['legB']['P5_worst_rel_err']:.3e}")
    print(f"  P3 max relative theta change over 6 decades of magnitudes: "
          f"{OUT['legB']['P3_max_theta_change']:.3e}")
    for r in OUT["legB"]["P3_structural"]:
        print(f"    a={r['flow_exponent_a']:.1f}  beta={r['beta_numeric']:.5f}  "
              f"theta={r['theta_measured']:.5f}")

    print("Leg C: mixed regions ...")
    OUT["legC"] = leg_C()
    for r in OUT["legC"]["rows"]:
        if r["n"] == 4:
            print(f"  f={r['f']:.2f}  theta={r['theta_measured']:.5f}  "
                  f"3/(4-f)={r['theta_predicted_3_over_4_minus_f']:.5f}  "
                  f"err={r['rel_err']:.2e}")

    print("Leg D: the dimensional route ...")
    OUT["legD"] = leg_D()
    for r in OUT["legD"]["fits"]:
        print(f"  d={r['d']}  predicted {r['theta_predicted_d_over_d_plus_1']:.4f}  |  "
              f"lower bound {r['theta_lower']:.4f}  directed {r['theta_directed']:.4f}  "
              f"MST {r['theta_mst']:.4f}")

    print("Leg E: the Phi attempt ...")
    OUT["legE"] = leg_E()
    for key, v in OUT["legE"].items():
        if key.startswith("control"):
            corr = v.get("min_abs_corr", v.get("max_abs_corr"))
            print(f"  CONTROL {key}: |corr| {corr:.4f}, "
                  f"conjugate ratio varies {100*v['ratio_rel_variation']:.1f}%")
        else:
            print(f"  {key}: max(1-corr) {v['max_one_minus_corr']:.2e}, "
                  f"ratio varies {v['ratio_rel_variation']:.2e}")

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2)
    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
