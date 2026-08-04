"""D8 — the residue of an m-parameter approach is a point of the Grassmannian.

Registered in PREREGISTRATION.md, committed before this file produced numbers.
Y_{ij} = d ln O_i / d ln eps_j transforms as Y -> Y A^{-1} under monomial
re-charting, so col(Y) and rank(Y) are the invariants and the count is r(n-r).
D7 is the m = 1, r = 1 slice.

numpy + stdlib only. Deterministic; no sampling of models, only of the group.
"""

import json
import math

import numpy as np

SEED = 20260728
OUT = {}

_GL = {}


def gl(k):
    if k not in _GL:
        _GL[k] = np.polynomial.legendre.leggauss(k)
    return _GL[k]


# ------------------------------------------------------------ 1-D germs
#
# A germ is a dict {power: coefficient-callable(params)}; params is the vector
# of controls. Everything below reads the FULL polynomial, never a truncation.


def poly_derivs(coeffs, x, m):
    tot = 0.0
    for j, c in coeffs.items():
        if j >= m:
            fall = 1.0
            for i in range(m):
                fall *= j - i
            tot += c * fall * x ** (j - m)
    return tot


def minimize_1d(coeffs, lo=-50.0, hi=50.0):
    """Root of Phi' with Phi'' > 0, by bisection on the increasing branch."""
    f = lambda x: poly_derivs(coeffs, x, 1)
    a, b = lo, hi
    fa = f(a)
    for _ in range(300):
        mid = 0.5 * (a + b)
        if (f(mid) < 0) == (fa < 0):
            a = mid
        else:
            b = mid
    return 0.5 * (a + b)


def germ_observables(coeffs):
    """The six observables, all read off the full germ."""
    xs = minimize_1d(coeffs)
    lam = poly_derivs(coeffs, xs, 2)
    d3 = poly_derivs(coeffs, xs, 3)
    phi_min = poly_derivs(coeffs, xs, 0)
    D = 1e-9 * lam * xs**2 if xs != 0 else 1e-30
    top = max(coeffs) + 1
    dv = [poly_derivs(coeffs, xs, mm) / math.factorial(mm) for mm in range(1, top)]
    w = 8.0 * math.sqrt(D / lam)
    u, wt = gl(400)
    d = w * u
    delta = np.zeros_like(d)
    for mm, c in enumerate(dv, start=1):
        delta += c * d**mm
    rho = np.exp(-(delta - delta.min()) / D) * wt
    z = rho.sum()
    m1 = (d * rho).sum() / z
    m2 = (d**2 * rho).sum() / z - m1**2
    m3 = (d**3 * rho).sum() / z - 3 * m1 * (d**2 * rho).sum() / z + 2 * m1**3
    return np.array([abs(xs), lam, m2, abs(phi_min), abs(d3), abs(m3)])


# model builders: params -> coeffs

def M2(p):  # cusp A3
    a, b = p
    return {4: 0.25, 2: 0.5 * a, 1: b}


def M3(p):  # cusp + an irrelevant sixth-order coupling
    a, b, c = p
    return {6: c / 6.0, 4: 0.25, 2: 0.5 * a, 1: b}


def M4(p):  # rank 1 by construction: the controls enter as one product
    e1, e2 = p
    return {4: 0.25, 1: -(e1 * e2)}


def M5(p):  # codimension-3 germ, every control relevant
    a, b, c = p
    return {6: 1 / 6.0, 4: 0.25 * a, 2: 0.5 * b, 1: c}


RAYS = {
    "M2": lambda t: np.array([t**2, t**3]),
    "M3": lambda t: np.array([t**2, t**3, 1.0]),
    "M4": lambda t: np.array([t**1.5, t**1.5]),
    "M5": lambda t: np.array([t**2, t**4, t**5]),
}
MODELS = {"M2": M2, "M3": M3, "M4": M4, "M5": M5}


def slope_matrix(fn, params, obs_fn, h=1e-4):
    """Y_ij = d ln O_i / d ln eps_j by central differences in log parameter."""
    params = np.asarray(params, float)
    cols = []
    for j in range(len(params)):
        pp, pm = params.copy(), params.copy()
        pp[j] *= math.exp(h)
        pm[j] *= math.exp(-h)
        lp = np.log(obs_fn(fn(pp)))
        lm = np.log(obs_fn(fn(pm)))
        cols.append((lp - lm) / (2 * h))
    return np.column_stack(cols)


# ------------------------------------------------- M0: coupled 2-D state

KAPPA = 0.7


def M0_observables(eps):
    """x*=y*=u by symmetry; six deterministic observables of the 2-D germ."""
    u = (eps / (1.0 + KAPPA)) ** (1.0 / 3.0)
    hxx = 3 * u**2 + KAPPA * u**2
    hxy = 2 * KAPPA * u**2
    lam_min, lam_max = hxx - hxy, hxx + hxy
    det = lam_min * lam_max
    phi = 2 * (u**4 / 4.0) + KAPPA * u**4 / 2.0 - eps * 2 * u
    d3 = 6 * u  # d^3 Phi / dx^3 at the minimum
    return np.array([u, lam_min, lam_max, det, abs(phi), d3])


# --------------------------------------------- M6: support-type moments

def M6_moments(A, B, C, D, nodes=1600):
    q = (1.0, 2.0, 4.0)
    co = (A, B, C)
    s = min((D / c) ** (1.0 / qq) for c, qq in zip(co, q) if c > 0)
    Y = 45.0 * s
    x, wt = gl(nodes)
    t = 0.5 * Y * (x + 1.0)
    w = 0.5 * Y * wt
    e = sum(c * t**qq for c, qq in zip(co, q)) / D
    rho = np.exp(-(e - e.min())) * w
    z = rho.sum()
    return np.array([(t**k * rho).sum() / z for k in (2, 4, 6, 8)])


def M6_slope_matrix(D, which, h=1e-4):
    """which selects the active controls; A ~ sqrt(D) keeps A relevant."""
    base = {"three": [math.sqrt(D), 1.0, 1.0],
            "two": [math.sqrt(D), 1.0, 0.0],
            "one": [0.0, 1.0, 0.0]}[which]
    active = [i for i, v in enumerate(base) if v > 0]
    cols = []
    for j in active:
        pp, pm = list(base), list(base)
        pp[j] *= math.exp(h)
        pm[j] *= math.exp(-h)
        lp = np.log(M6_moments(*pp, D))
        lm = np.log(M6_moments(*pm, D))
        cols.append((lp - lm) / (2 * h))
    return np.column_stack(cols)


# ------------------------------------------------------- the group, GL_m

def sample_A(m, rng, n=200):
    out = []
    while len(out) < n:
        A = rng.uniform(0.2, 2.5, size=(m, m))
        if abs(np.linalg.det(A)) > 0.05:
            out.append(A)
    return out


def col_space(Y, r):
    """Orthonormal basis of the rank-r column space.

    QR is wrong here: for a rank-deficient Y its range includes directions the
    columns do not span, so the comparison below would report pi/2 for exactly
    the models where the claim is most interesting.
    """
    U, _, _ = np.linalg.svd(Y, full_matrices=False)
    return U[:, :r]


def principal_angle(Y1, Y2, r):
    """arccos of the smallest principal cosine. Kept because it is what the
    registration named -- but note it floors at sqrt(machine eps) ~ 1.5e-8,
    since cos t = 1 - t^2/2 loses half the digits near t = 0."""
    s = np.linalg.svd(col_space(Y1, r).T @ col_space(Y2, r), compute_uv=False)
    return float(np.arccos(np.clip(s.min(), -1.0, 1.0)))


def subspace_sine(Y1, Y2, r):
    """sin of the largest principal angle, computed without arccos.

    ||(I - Q1 Q1^T) Q2||_2 is accurate to machine precision where the arccos
    form is not, and it is the same quantity for small angles.
    """
    q1, q2 = col_space(Y1, r), col_space(Y2, r)
    return float(np.linalg.svd(q2 - q1 @ (q1.T @ q2), compute_uv=False)[0])


def group_analysis(Y, rng, r):
    m = Y.shape[1]
    As = sample_A(m, rng)
    angles, sines, y11, vecs = [], [], [], []
    for A in As:
        Yp = Y @ np.linalg.inv(A)
        angles.append(principal_angle(Y, Yp, r))
        sines.append(subspace_sine(Y, Yp, r))
        y11.append(Yp[0, 0])
        vecs.append(Yp.ravel())
    V = np.array(vecs)
    sv = np.linalg.svd(V - V.mean(0), compute_uv=False)
    orbit_dim = int((sv > 1e-8 * sv[0]).sum())
    conds = np.array([np.linalg.cond(A) for A in As])
    ang = np.array(angles)
    order = np.argsort(conds)
    best = order[: max(1, len(order) // 10)]
    worst = order[-max(1, len(order) // 10):]
    return {
        "max_principal_angle": float(max(angles)),
        "max_subspace_sine": float(max(sines)),
        "cond_vs_angle": {
            "best_decile_cond_median": float(np.median(conds[best])),
            "best_decile_angle_max": float(ang[best].max()),
            "worst_decile_cond_median": float(np.median(conds[worst])),
            "worst_decile_angle_max": float(ang[worst].max()),
        },
        "Y11_span": float(max(y11) / min(y11)) if min(y11) > 0 else
                    float((max(y11) - min(y11)) / abs(np.median(y11))),
        "orbit_singular_values": sv[: m * m + 2].tolist(),
        "orbit_dim": orbit_dim,
    }


def rank_report(Y, tol=1e-3):
    sv = np.linalg.svd(Y, compute_uv=False)
    ratios = (sv / sv[0]).tolist()
    r = int((sv > tol * sv[0]).sum())
    return sv.tolist(), ratios, r


# ----------------------------------------------------------------- main

if __name__ == "__main__":
    rng = np.random.default_rng(SEED)
    OUT["seed"] = SEED

    # ---- P2 (control, forced): coupled 2-D state, one control
    print("P2 ...", flush=True)
    eg = np.logspace(-9, -7, 25)
    Y0 = np.column_stack([
        (np.log(M0_observables(eg[-1] * math.exp(1e-4)))
         - np.log(M0_observables(eg[-1] * math.exp(-1e-4)))) / 2e-4])
    sv0, rat0, r0 = rank_report(Y0)
    # The registered form is VACUOUS: an n x 1 matrix has rank 1 whatever the
    # model does. The non-vacuous question is whether coupling introduces a
    # second scale, which would make the column drift with eps. Stack columns
    # measured across four decades and look at the rank of the stack.
    stack = np.column_stack([
        (np.log(M0_observables(e * math.exp(1e-4)))
         - np.log(M0_observables(e * math.exp(-1e-4)))) / 2e-4 for e in eg])
    sv_st, rat_st, r_st = rank_report(stack)
    OUT["P2_control_coupled_state"] = {
        "m": 1, "n": 6, "singular_ratios": rat0, "rank": r0,
        "count_r_times_n_minus_r": r0 * (6 - r0),
        "registered_form_is_vacuous": True,
        "stacked_across_eps": {
            "n_eps": len(eg), "singular_ratios": rat_st[:3], "rank": r_st,
            "sigma2_over_sigma1": rat_st[1],
        },
        "note": "forced AND vacuous as registered; the stacked form is the "
                "non-vacuous version and is post-hoc",
    }

    # ---- P3 / P4 / P7: the germs
    print("P3/P4/P7 ...", flush=True)
    germ = {}
    for tag in ("M2", "M3", "M4", "M5"):
        rows = []
        for t in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4):
            Y = slope_matrix(MODELS[tag], RAYS[tag](t), germ_observables)
            sv, rat, r = rank_report(Y)
            rows.append({"t": t, "singular_ratios": rat, "rank": r,
                         "Y": Y.tolist()})
        last = rows[-1]
        n = 6
        germ[tag] = {
            "m": len(RAYS[tag](1e-3)), "n": n, "by_t": rows,
            "rank": last["rank"],
            "count_r_times_n_minus_r": last["rank"] * (n - last["rank"]),
            "group": group_analysis(np.array(last["Y"]), rng, last["rank"]),
        }
    # P4's predicted rate for the discarded singular value
    ts = np.array([row["t"] for row in germ["M3"]["by_t"]])
    s3 = np.array([row["singular_ratios"][2] for row in germ["M3"]["by_t"]])
    A = np.vstack([np.log(ts), np.ones_like(ts)]).T
    germ["M3"]["sigma3_rate_exponent"] = float(
        np.linalg.lstsq(A, np.log(s3), rcond=None)[0][0])
    germ["M3"]["sigma3_over_sigma1_by_t"] = s3.tolist()
    OUT["P3_P4_P7_germs"] = germ

    # P7: does D7's estimator reproduce M4's projective class?
    m4 = np.array(germ["M4"]["by_t"][-1]["Y"])
    col = m4[:, 0] / m4[0, 0]
    e1 = np.logspace(-6, -5, 25)
    obs = np.array([germ_observables(M4([e, e])) for e in e1])
    d7 = np.array([np.polyfit(np.log(obs[:, 0]), np.log(obs[:, k]), 1)[0]
                   for k in range(6)])
    OUT["P7_reduction_to_D7"] = {
        "column_normalized": col.tolist(),
        "D7_estimator": d7.tolist(),
        "max_abs_diff": float(np.max(np.abs(col - d7))),
    }

    # ---- P8: the support-type class
    print("P8 ...", flush=True)
    supp = {}
    for which in ("one", "two", "three"):
        rows = []
        for D in (1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
            Y = M6_slope_matrix(D, which)
            sv, rat, r = rank_report(Y)
            rows.append({"D": D, "singular_ratios": rat, "rank": r,
                         "Y": Y.tolist()})
        n = 4
        supp[which] = {"by_D": rows, "rank": rows[-1]["rank"], "n": n,
                       "count_r_times_n_minus_r":
                           rows[-1]["rank"] * (n - rows[-1]["rank"])}
    Ds = np.array([row["D"] for row in supp["three"]["by_D"]])
    s3s = np.array([row["singular_ratios"][2] for row in supp["three"]["by_D"]])
    A = np.vstack([np.log(Ds), np.ones_like(Ds)]).T
    supp["three"]["sigma3_rate_exponent"] = float(
        np.linalg.lstsq(A, np.log(s3s), rcond=None)[0][0])
    supp["three"]["group"] = group_analysis(
        np.array(supp["three"]["by_D"][-1]["Y"]), rng,
        supp["three"]["by_D"][-1]["rank"])
    OUT["P8_support_type"] = supp

    # ---- POST-HOC DIAGNOSTIC (not registered)
    # P1's angle came in at ~1e-8 against a registered 1e-10. Y is built from
    # central differences, whose error is O(h^2) with an O(eps/h) roundoff
    # floor, so the subspace it spans cannot be more accurate than that. If the
    # claim is exact and the budget is the cause, the angle must track that
    # curve and bottom out near h ~ 1e-5; if it plateaus, the claim is off.
    print("diagnostic (post-hoc) ...", flush=True)
    hrows = []
    for h in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
        Y = slope_matrix(M5, RAYS["M5"](1e-4), germ_observables, h=h)
        _, _, r = rank_report(Y)
        A = np.array([[1.3, 0.4, 0.7], [0.5, 1.9, 0.3], [0.8, 0.6, 2.1]])
        hrows.append({"h": h, "rank": r,
                      "angle": principal_angle(Y, Y @ np.linalg.inv(A), r),
                      "fd_budget": h**2 + 1e-16 / h})
    # Where an irrelevant column is present the rank-r subspace is only an
    # ASYMPTOTIC invariant: mixing the near-null column back in with A^{-1}
    # tilts it by ~sigma_{r+1}/sigma_r. If that is the cause, the subspace
    # distance must vanish at the same rate as the discarded singular value.
    Am3 = np.array([[1.3, 0.4, 0.7], [0.5, 1.9, 0.3], [0.8, 0.6, 2.1]])
    tilt = []
    for row in germ["M3"]["by_t"]:
        Y = np.array(row["Y"])
        tilt.append({"t": row["t"],
                     "sine": subspace_sine(Y, Y @ np.linalg.inv(Am3), 2),
                     "sigma3_over_sigma1": row["singular_ratios"][2]})
    tt = np.array([r["t"] for r in tilt])
    ss = np.array([r["sine"] for r in tilt])
    Am = np.vstack([np.log(tt), np.ones_like(tt)]).T
    OUT["POSTHOC_asymptotic_subspace"] = {
        "_note": "not registered; tests whether P1's residual on the models "
                 "with an irrelevant column is the asymptotics rather than a "
                 "failure. Never counted as a pass.",
        "rows": tilt,
        "sine_rate_exponent": float(np.linalg.lstsq(Am, np.log(ss), rcond=None)[0][0]),
    }

    OUT["POSTHOC_step_size"] = {
        "_note": "not registered; separates a failed claim from the "
                 "finite-difference budget. Never counted as a pass.",
        "rows": hrows}

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2)

    print("\n--- summary ---")
    p2 = OUT["P2_control_coupled_state"]
    print(f"P2  coupled 2-D state, m=1: rank {p2['rank']}, "
          f"count {p2['count_r_times_n_minus_r']}  (forced AND vacuous); "
          f"stacked across eps: rank {p2['stacked_across_eps']['rank']}, "
          f"s2/s1 {p2['stacked_across_eps']['sigma2_over_sigma1']:.2e}")
    for tag in ("M2", "M3", "M4", "M5"):
        g = germ[tag]
        last = g["by_t"][-1]
        print(f"P3  {tag}: m={g['m']} rank={g['rank']} count={g['count_r_times_n_minus_r']} "
              f"ratios={[round(v, 5) for v in last['singular_ratios']]}")
        gr = g["group"]
        print(f"    group: angle {gr['max_principal_angle']:.2e} "
              f"(sine form {gr['max_subspace_sine']:.2e}), "
              f"orbit_dim {gr['orbit_dim']} (predict r*m={g['rank']*g['m']}), "
              f"Y11 span {gr['Y11_span']:.2f}x")
    print(f"P4  M3 sigma3/sigma1 by t: "
          f"{[f'{v:.2e}' for v in germ['M3']['sigma3_over_sigma1_by_t']]}")
    print(f"    fitted rate exponent {germ['M3']['sigma3_rate_exponent']:.3f} "
          f"(predict 2.00 +- 0.15)")
    print(f"P7  reduction to D7: max diff {OUT['P7_reduction_to_D7']['max_abs_diff']:.2e}")
    for which in ("one", "two", "three"):
        s = supp[which]
        print(f"P8  M6 {which}-term: rank {s['rank']} count {s['count_r_times_n_minus_r']} "
              f"ratios={[round(v, 5) for v in s['by_D'][-1]['singular_ratios']]}")
    print(f"    three-term sigma3 rate {supp['three']['sigma3_rate_exponent']:.3f} "
          f"(predict 1.00 +- 0.15); group angle "
          f"{supp['three']['group']['max_principal_angle']:.2e} "
          f"(sine {supp['three']['group']['max_subspace_sine']:.2e}), "
          f"orbit_dim {supp['three']['group']['orbit_dim']}")
    print("\n--- post-hoc diagnostic (not registered) ---")
    for tag in ("M2", "M5"):
        cv = germ[tag]["group"]["cond_vs_angle"]
        print(f"angle vs cond(A) [{tag}]: best decile cond "
              f"{cv['best_decile_cond_median']:.1f} -> {cv['best_decile_angle_max']:.1e}; "
              f"worst decile cond {cv['worst_decile_cond_median']:.1f} -> "
              f"{cv['worst_decile_angle_max']:.1e}")
    pa = OUT["POSTHOC_asymptotic_subspace"]
    print("M3 subspace sine by t: " + ", ".join(
        f"{r['t']:.0e}->{r['sine']:.1e}" for r in pa["rows"])
        + f"  rate {pa['sine_rate_exponent']:.3f}")
    print("angle vs step size: " + ", ".join(
        f"h={r['h']:.0e}->{r['angle']:.1e} (budget {r['fd_budget']:.1e})"
        for r in OUT["POSTHOC_step_size"]["rows"]))
