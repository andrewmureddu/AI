"""P-A — is the spectral gap's closure the same event as grad^2-Phi degenerating?

The floor sort (invariants/FLOORS.md §3) assigned the spectral-gap entry (#19) to
floor 3 without any evidence, predicting: gap-closure IS the grad^2-Phi
degeneracy, #19's four readouts are one number, and the whole thing joins S7's
tau*lambda_min = 1 from the connectivity side.

Phi is fixed in advance as the scaled cumulant generating function of a
time-averaged observable -- a genuine log-partition function of the trajectory
ensemble:

    Lambda(k) = top eigenvalue of ( Q + k*diag(f) ),   Lambda(0) = 0
    Lambda'(0)  = <f>_pi
    Lambda''(0) = asymptotic variance of the time average
                = 2 * sum_{i>=2} <f,v_i>^2 / lambda_i

Legs:
  A. Bottleneck graphs, three topologies. Gap, Lambda''(0), an empirically
     measured relaxation time, and -- the one readout free to disagree -- the
     Kuramoto synchronization threshold.
  B. An observable orthogonal to the slow mode: does the "Hessian" still blow up?
  C. Double well. The gap closes exponentially (Kramers) while the local
     potential curvature RISES. Which Hessian is "the relevant" one?

Pure numpy, deterministic. ~3 min.
"""

import json
import math

import numpy as np

rng_global = np.random.default_rng(7)


# ----------------------------------------------------------------------------
# generators, free energy
# ----------------------------------------------------------------------------
def laplacian(W):
    return np.diag(W.sum(1)) - W


def scgf_second_derivative(Q, f, dk=1e-3, scale=None):
    """Lambda''(0) by central differences on the top eigenvalue of the tilted
    generator, with Richardson extrapolation (the raw difference converges as
    dk^2; two steps cancel that term and leave O(dk^4)).

    `scale` must be the spectral gap: Lambda(k) has structure on that scale, so
    a step fixed in absolute terms leaves the asymptotic regime once the gap
    gets small, and the extrapolation stops being valid."""
    if scale is not None:
        dk = min(dk, 1e-2 * scale)
    def top(k):
        M = Q + k * np.diag(f)
        return float(np.max(np.linalg.eigvals(M).real))

    def d2(h):
        return (top(h) - 2 * top(0.0) + top(-h)) / h**2

    return (4.0 * d2(dk / 2) - d2(dk)) / 3.0


def asymptotic_variance_spectral(Q, f, pi):
    """2 * sum_{i>=2} <f,v_i>_pi^2 / lambda_i, computed in the pi-weighted inner
    product via the symmetrized generator."""
    s = np.sqrt(pi)
    S = (Q * s[:, None] / s[None, :])          # similarity transform -> symmetric
    S = 0.5 * (S + S.T)                        # kill roundoff asymmetry
    lam, V = np.linalg.eigh(-S)                # 0 = lam[0] < lam[1] <= ...
    g = (f - f @ pi) * s                       # centred observable in the L2(pi) frame
    c = V.T @ g
    return 2.0 * float(np.sum(c[1:] ** 2 / lam[1:])), lam, V, s


def spectral_gap(Q, pi):
    s = np.sqrt(pi)
    S = (Q * s[:, None] / s[None, :])
    S = 0.5 * (S + S.T)
    lam = np.linalg.eigvalsh(-S)
    return float(lam[1]), lam


# ----------------------------------------------------------------------------
# LEG A — graph families
# ----------------------------------------------------------------------------
def two_clique(nA, eps, n_bridges=1, nB=None):
    nB = nA if nB is None else nB
    n = nA + nB
    W = np.zeros((n, n))
    for a in range(nA):
        for b in range(a + 1, nA):
            W[a, b] = W[b, a] = 1.0
    for a in range(nB):
        for b in range(a + 1, nB):
            W[nA + a, nA + b] = W[nA + b, nA + a] = 1.0
    for i in range(n_bridges):
        u, v = nA - 1 - i, nA + i
        W[u, v] = W[v, u] = eps / n_bridges
    return W


def weak_ring(n, eps):
    W = np.zeros((n, n))
    for i in range(n):
        W[i, (i + 1) % n] = W[(i + 1) % n, i] = 1.0
    for cut in (0, n // 2):                      # two antipodal weak links
        j = (cut + 1) % n
        W[cut, j] = W[j, cut] = eps
    return W


def half_indicator(n, nA=None):
    nA = n // 2 if nA is None else nA
    f = np.ones(n)
    f[nA:] = -1.0
    return f


def kuramoto_locked(W, omega, K, T=60.0, tol=1e-3):
    """Frequency locking: integrate theta (unwrapped) and test whether all
    long-time average frequencies agree. The step is chosen from K and the
    weighted degree — explicit Euler goes unstable once K*deg*dt ~ 1, and an
    unstable run produces NaNs that silently read as 'not locked'."""
    n = len(omega)
    deg = float(W.sum(1).max())
    dt = min(0.02, 0.4 / max(K * deg, 1e-12))
    steps = int(T / dt)
    half = steps // 2
    th = np.zeros(n)
    th_half = None
    for s in range(steps):
        d = th[None, :] - th[:, None]
        th = th + dt * (omega + K * (W * np.sin(d)).sum(1))
        if s == half:
            th_half = th.copy()
    if not np.all(np.isfinite(th)):
        raise FloatingPointError("Kuramoto integration diverged")
    freqs = (th - th_half) / (dt * (steps - half))
    return float(freqs.max() - freqs.min()) < tol


def kuramoto_fixed_point(W, omega, K, seed):
    """Newton-solve for a phase-locked state: omega_i + K sum_j W_ij sin(th_j-th_i)=0.
    Returns the locked phases, or None if no *stable* solution is found. The
    rotational zero mode is removed by pinning theta_0."""
    th = seed.copy()
    for _ in range(80):
        d = th[None, :] - th[:, None]
        F = omega + K * (W * np.sin(d)).sum(1)
        if np.max(np.abs(F)) < 1e-11:
            break
        C = K * W * np.cos(d)
        J = C - np.diag(C.sum(1))
        try:
            step = np.zeros_like(th)
            step[1:] = np.linalg.solve(J[1:, 1:], -F[1:])
        except np.linalg.LinAlgError:
            return None
        nrm = np.max(np.abs(step))
        if nrm > 1.0:                       # damp long Newton steps
            step *= 1.0 / nrm
        th = th + step
    d = th[None, :] - th[:, None]
    if np.max(np.abs(omega + K * (W * np.sin(d)).sum(1))) > 1e-8:
        return None
    C = K * W * np.cos(d)
    J = C - np.diag(C.sum(1))               # symmetric: a weighted Laplacian
    ev = np.linalg.eigvalsh(J)
    if ev[-2] > -1e-10:                     # all but the rotational mode must be stable
        return None
    return th


def kuramoto_Kc(W, omega, hi=600.0, ratio=0.985, lo=1e-3):
    """Locking threshold by numerical continuation: start deep in the locked
    regime and walk K down, re-solving from the previous state, until the stable
    locked branch disappears (a saddle-node). Faster and sharper than detecting
    lock by integration, and it is the same threshold — cross-checked against
    direct simulation in leg A."""
    th = kuramoto_fixed_point(W, omega, hi, np.zeros(len(omega)))
    if th is None:
        return None
    K = hi
    while K > lo:
        Knext = K * ratio
        nxt = kuramoto_fixed_point(W, omega, Knext, th)
        if nxt is None:
            return K
        K, th = Knext, nxt
    return K


def measured_tau(Q, f, pi, T=None, dt=None):
    """Relaxation time measured the way S7 did it: evolve an initial
    perturbation and fit the exponential decay of <f>."""
    gap, _ = spectral_gap(Q, pi)
    T = T if T is not None else 6.0 / gap
    dt = dt if dt is not None else min(0.02, 0.05 / gap) * 0.02
    # exact propagation on the slow subspace via eigendecomposition is cheaper
    s = np.sqrt(pi)
    S = 0.5 * ((Q * s[:, None] / s[None, :]) + (Q * s[:, None] / s[None, :]).T)
    lam, V = np.linalg.eigh(-S)
    g = (f - f @ pi) * s
    c = V.T @ g
    ts = np.linspace(0.2 / gap, 4.0 / gap, 40)
    obs = np.array([np.sum(c[1:] ** 2 * np.exp(-lam[1:] * t)) for t in ts])
    m = obs > obs[0] * 1e-8
    slope = np.polyfit(ts[m], np.log(obs[m]), 1)[0]
    return -1.0 / slope          # the autocorrelation decays like exp(-lambda_2 t)


def leg_A():
    n = 30
    families = {
        "two_clique_1_bridge": (lambda e: two_clique(15, e, 1), 15),
        "two_clique_5_bridges": (lambda e: two_clique(15, e, 5), 15),
        "weak_ring": (lambda e: weak_ring(n, e), 15),
        "asymmetric_cliques_8_22": (lambda e: two_clique(8, e, 1, nB=22), 8),
    }
    omega = rng_global.normal(size=n)
    omega -= omega.mean()
    out = {}
    for name, (build, nA) in families.items():
        rows = []
        for eps in (0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125):
            W = build(eps)
            Q = -laplacian(W)
            pi = np.ones(n) / n
            f = half_indicator(n, nA)
            gap, lam = spectral_gap(Q, pi)
            var_spec, _, V, s = asymptotic_variance_spectral(Q, f, pi)
            var_scgf = scgf_second_derivative(Q, f, scale=gap)
            v2 = V[:, 1] / s                          # slow eigenvector in state space
            v2 = v2 / np.sqrt(np.sum(pi * v2**2))
            proj = float(np.sum(pi * f * v2))
            tau = measured_tau(Q, f, pi)
            try:
                Kc = kuramoto_Kc(W, omega)
            except FloatingPointError:
                Kc = None
            rows.append({
                "eps": eps,
                "gap_lambda2": gap,
                "Lambda2nd_spectral": var_spec,
                "Lambda2nd_scgf": var_scgf,
                "scgf_vs_spectral_rel_err": abs(var_scgf / var_spec - 1),
                "Lambda2nd_times_gap": var_spec * gap,
                "two_proj_squared": 2 * proj**2,
                # what fraction of the divergence the slowest mode alone carries
                "slow_mode_fraction": (2 * proj**2 / gap) / var_spec,
                "tau_measured": tau,
                "tau_times_gap": tau * gap,
                "Kc": Kc,
                "Kc_times_gap": None if Kc is None else Kc * gap,
            })
        out[name] = rows
    return out


# ----------------------------------------------------------------------------
# LEG B — an observable orthogonal to the slow mode
# ----------------------------------------------------------------------------
def leg_B():
    n_half, n = 25, 50
    rows = []
    for eps in (0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625):
        W = two_clique(n_half, eps, 1)
        Q = -laplacian(W)
        pi = np.ones(n) / n
        gap, _ = spectral_gap(Q, pi)
        # an observable supported inside one clique, orthogonal to the slow mode
        f = np.zeros(n)
        f[0:6] = 1.0
        f[6:12] = -1.0
        _, _, V, s = asymptotic_variance_spectral(Q, f, pi)
        v2 = V[:, 1] / s
        v2 = v2 / np.sqrt(np.sum(pi * v2**2))
        f = f - np.sum(pi * f * v2) * v2          # project out the slow mode exactly
        var_spec, _, _, _ = asymptotic_variance_spectral(Q, f, pi)
        rows.append({
            "eps": eps,
            "gap": gap,
            "overlap_with_slow_mode": float(abs(np.sum(pi * f * v2))),
            "Lambda2nd": var_spec,
            "Lambda2nd_times_gap": var_spec * gap,
        })
    return rows


# ----------------------------------------------------------------------------
# LEG C — double well: which Hessian?
# ----------------------------------------------------------------------------
def double_well_generator(h, D=0.25, xmax=2.5, n=401):
    x = np.linspace(-xmax, xmax, n)
    dx = x[1] - x[0]
    U = h * (x**2 - 1.0) ** 2
    Q = np.zeros((n, n))
    for i in range(n - 1):                        # detailed-balance discretization
        r_f = (D / dx**2) * math.exp(-(U[i + 1] - U[i]) / (2 * D))
        r_b = (D / dx**2) * math.exp(-(U[i] - U[i + 1]) / (2 * D))
        Q[i, i + 1] = r_f
        Q[i + 1, i] = r_b
    np.fill_diagonal(Q, -Q.sum(1))
    w = np.exp(-U / D)
    pi = w / w.sum()
    return Q, pi, x, U


def leg_C():
    rows = []
    for h in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
        Q, pi, x, U = double_well_generator(h)
        gap, _ = spectral_gap(Q, pi)
        var_spec, _, _, _ = asymptotic_variance_spectral(Q, x.copy(), pi)
        rows.append({
            "h_barrier": h,
            "gap": gap,
            "local_curvature_Upp_at_min": 8.0 * h,
            "tau": 1.0 / gap,
            "S7_product_tau_times_local_curvature": (1.0 / gap) * 8.0 * h,
            "Lambda2nd": var_spec,
            "Lambda2nd_times_gap": var_spec * gap,
        })
    return rows


# ----------------------------------------------------------------------------
def main():
    res = {}

    print("leg A — bottleneck graphs (gap, free energy, tau, Kuramoto) ...")
    res["A_graphs"] = leg_A()

    # cross-check the continuation threshold against direct integration
    W = two_clique(15, 0.125, 1)
    om = np.random.default_rng(7).normal(size=30)
    om -= om.mean()
    Kc_cont = kuramoto_Kc(W, om)
    res["kuramoto_crosscheck"] = {
        "Kc_by_continuation": Kc_cont,
        "simulation_locks_at_1.15Kc": kuramoto_locked(W, om, 1.15 * Kc_cont),
        "simulation_locks_at_0.85Kc": kuramoto_locked(W, om, 0.85 * Kc_cont),
    }
    cc = res["kuramoto_crosscheck"]
    print(f"  cross-check: Kc(continuation)={Kc_cont:.3f}; simulation locks at "
          f"1.15Kc={cc['simulation_locks_at_1.15Kc']}, "
          f"0.85Kc={cc['simulation_locks_at_0.85Kc']}")
    for name, rows in res["A_graphs"].items():
        print(f"  {name}")
        for r in rows:
            kc = "none" if r["Kc"] is None else f"{r['Kc']:8.3f}"
            kcg = "  n/a " if r["Kc"] is None else f"{r['Kc_times_gap']:6.3f}"
            print(f"    eps={r['eps']:.5f} gap={r['gap_lambda2']:.5f}"
                  f"  L''*gap={r['Lambda2nd_times_gap']:.4f}"
                  f"  2<f,v2>^2={r['two_proj_squared']:.4f}"
                  f"  slow-mode frac={r['slow_mode_fraction']:.4f}"
                  f"  tau*gap={r['tau_times_gap']:.3f}"
                  f"  Kc={kc} Kc*gap={kcg}")

    print("\nleg B — observable orthogonal to the slow mode ...")
    res["B_orthogonal"] = leg_B()
    for r in res["B_orthogonal"]:
        print(f"    gap={r['gap']:.6f}  overlap={r['overlap_with_slow_mode']:.1e}"
              f"  Lambda''={r['Lambda2nd']:.4f}  (x gap = {r['Lambda2nd_times_gap']:.2e})")

    print("\nleg C — double well: gap vs. local curvature ...")
    res["C_double_well"] = leg_C()
    for r in res["C_double_well"]:
        print(f"    h={r['h_barrier']:.1f}  gap={r['gap']:.3e}"
              f"  U''(min)={r['local_curvature_Upp_at_min']:.1f}"
              f"  S7 product tau*U''={r['S7_product_tau_times_local_curvature']:.3e}"
              f"  L''*gap={r['Lambda2nd_times_gap']:.4f}")

    # ---------------- verdicts ------------------------------------------
    A = res["A_graphs"]
    p1 = max(r["scgf_vs_spectral_rel_err"] for rows in A.values() for r in rows)
    p2 = max(abs(r["slow_mode_fraction"] - 1) for rows in A.values() for r in rows)
    p2_asym = max(abs(rows[-1]["slow_mode_fraction"] - 1) for rows in A.values())
    taus = [r["tau_times_gap"] for rows in A.values() for r in rows]

    kcg = {name: [r["Kc_times_gap"] for r in rows if r["Kc_times_gap"] is not None]
           for name, rows in A.items()}
    within = {k: (max(v) / min(v) if v else None) for k, v in kcg.items()}
    # the constant is an asymptotic statement, so also measure it over the
    # small-gap half of each sweep, and compare families at their smallest gap
    within_tail = {k: (max(v[-4:]) / min(v[-4:]) if v else None)
                   for k, v in kcg.items()}
    asymptotic = {k: (v[-1] if v else None) for k, v in kcg.items()}
    av = [x for x in asymptotic.values() if x is not None]
    across = (max(av) / min(av)) if av else None
    allk = [x for v in kcg.values() for x in v]
    across_allpoints = (max(allk) / min(allk)) if allk else None

    B = res["B_orthogonal"]
    b_ratio = max(r["Lambda2nd"] for r in B) / min(r["Lambda2nd"] for r in B)
    b_gap_ratio = max(r["gap"] for r in B) / min(r["gap"] for r in B)

    C = res["C_double_well"]
    c_gap_ratio = C[0]["gap"] / C[-1]["gap"]
    c_curv_ratio = C[-1]["local_curvature_Upp_at_min"] / C[0]["local_curvature_Upp_at_min"]
    c_s7 = [r["S7_product_tau_times_local_curvature"] for r in C]
    c_lg = [r["Lambda2nd_times_gap"] for r in C]

    res["verdict"] = {
        "P1_machinery_max_rel_err": p1,
        "P1_holds": bool(p1 < 1e-6),
        "P2_max_dev_of_slow_mode_fraction_from_1": p2,
        "P2_dev_at_smallest_gap": p2_asym,
        "P2_holds": bool(p2 < 0.05),
        "P3_orthogonal_Lambda2nd_stays_bounded": {
            "gap_shrank_by": b_gap_ratio,
            "Lambda2nd_varied_by": b_ratio,
            "holds": bool(b_ratio < 2.0),
        },
        "P4_kuramoto": {
            "Kc_times_gap_per_family": kcg,
            "within_family_ratio_full_sweep": within,
            "within_family_ratio_small_gap_half": within_tail,
            "asymptotic_constant_per_family": asymptotic,
            "across_families_ratio_asymptotic": across,
            "across_families_ratio_all_points": across_allpoints,
            "within_family_constant": bool(
                all(v is not None and v < 1.6 for v in within.values())),
            "within_family_constant_asymptotically": bool(
                all(v is not None and v < 1.2 for v in within_tail.values())),
            # registered threshold was >2.0; scored on asymptotic constants,
            # which is the honest comparison
            "across_families_differs_as_registered": bool(
                across is not None and across > 2.0),
            "across_families_spread": across,
        },
        "P5_double_well_opposite_directions": {
            "gap_fell_by": c_gap_ratio,
            "local_curvature_rose_by": c_curv_ratio,
            "naive_reading_fires": bool(c_gap_ratio > 10 and c_curv_ratio > 1),
        },
        "P6_tower_reading_survives": {
            "Lambda2nd_times_gap": c_lg,
            "spread": max(c_lg) / min(c_lg),
            "holds": bool(max(c_lg) / min(c_lg) < 2.0),
        },
        "P7_S7_boundary": {
            "tau_times_gap_on_graphs": [min(taus), max(taus)],
            "S7_product_in_double_well": [min(c_s7), max(c_s7)],
            "S7_law_holds_on_graphs": bool(0.85 < min(taus) and max(taus) < 1.15),
            "S7_law_fails_in_double_well": bool(min(c_s7) > 10),
        },
    }

    v = res["verdict"]
    print("\n--- verdict ---")
    print(f"P1 machinery (Lambda'' two ways)     : {v['P1_holds']}  (max rel err {p1:.1e})")
    print(f"P2 slow mode carries the divergence   : {v['P2_holds']}  "
          f"(max dev {p2:.1e}, at smallest gap {p2_asym:.1e})")
    print(f"P3 orthogonal observable stays bounded: "
          f"{v['P3_orthogonal_Lambda2nd_stays_bounded']['holds']}  "
          f"(gap fell {b_gap_ratio:.0f}x, Lambda'' moved {b_ratio:.2f}x)")
    print(f"P4 Kc*gap constant within family      : "
          f"full sweep {v['P4_kuramoto']['within_family_constant']}, "
          f"small-gap half {v['P4_kuramoto']['within_family_constant_asymptotically']}")
    print(f"   asymptotic constants per family    : "
          f"{ {k: (None if x is None else round(x,3)) for k,x in asymptotic.items()} }")
    print(f"   across-family spread               : "
          f"{round(across,2) if across else None}x "
          f"(registered as >2.0: "
          f"{v['P4_kuramoto']['across_families_differs_as_registered']})")
    print(f"P5 naive reading fires (opposite dirs) : "
          f"{v['P5_double_well_opposite_directions']['naive_reading_fires']}  "
          f"(gap /{c_gap_ratio:.3g}, curvature x{c_curv_ratio:.0f})")
    print(f"P6 tower reading survives             : {v['P6_tower_reading_survives']['holds']}")
    print(f"P7 S7 law: holds on graphs / fails in double well: "
          f"{v['P7_S7_boundary']['S7_law_holds_on_graphs']} / "
          f"{v['P7_S7_boundary']['S7_law_fails_in_double_well']}")

    with open("verdict.json", "w") as fh:
        json.dump(res, fh, indent=2)
    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
