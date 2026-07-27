"""
D1 - the chart law: two integers classify floor 3.

Tests whether the domain-dependence of floor-3 exponents lives entirely in the
chart map eps -> lambda (the chart order k, pure gauge) while the classification
is carried by the degeneracy order p (the order of the first non-vanishing
anharmonic term of Phi).

Registered prediction (see PREREGISTRATION.md):

        lambda_c ~ D^((p-2)/p)

for the noise-rounding crossover, measured in the *lambda chart*, with no domain
label and no free exponent.

Legs:
  A  fold / saddle-node          ecology, dynamical systems   k=1/2  p=3
  B  SIS at R0=1                 epidemiology                 k=1    p=3
  C  mean-field Ising            physics                      k=1    p=4   (all orders)
  D  Blume-Capel, tricritical    physics                      k=1    p=6   (all orders)
  E  least squares at MP edge    machine learning             k=2    p=inf (control)

Pure numpy, deterministic given the seed. ~2 minutes.
"""

import json
import numpy as np

SEED = 20260726
C_CUT = 45.0          # integrate the well out to Phi = C_CUT * D
DELTAS = [0.05, 0.10, 0.20]   # |R-1| thresholds; R* = 1 - delta as registered
D_GRID = np.logspace(-8.0, -4.0, 9)


# --------------------------------------------------------------------------
# quadrature over a well
# --------------------------------------------------------------------------

def _limit(phi, D, direction, width, bound):
    """Outer integration limit in `direction`: whichever of the potential
    reaching C_CUT*D or the supplied bound (barrier / state-space edge) comes
    first."""
    target = C_CUT * D
    if bound is not None and phi(bound) <= target:
        return bound
    hi = direction * width
    for _ in range(300):
        if bound is not None and abs(hi) >= abs(bound):
            hi = bound
            break
        if phi(hi) > target:
            break
        hi *= 2.0
    lo = 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if phi(mid) > target:
            hi = mid
        else:
            lo = mid
    return hi


def rounding_ratio(phi, lam, D, y_lo=None, y_hi=None):
    """R = Var * lambda / D for the stationary density rho ~ exp(-phi/D).

    phi must be shifted so the stable minimum sits at y = 0 with phi(0) = 0.
    y_lo / y_hi are hard bounds (barrier top or state-space edge), or None for
    a confining direction.
    """
    width = np.sqrt(D / lam)
    hi = _limit(phi, D, +1.0, width, y_hi)
    lo = _limit(phi, D, -1.0, width, y_lo)
    n = int(np.clip(60.0 * (hi - lo) / width, 20001, 600001))
    y = np.linspace(lo, hi, n)
    p = phi(y)
    w = np.exp(-(p - p.min()) / D)
    z = np.trapezoid(w, y)
    m1 = np.trapezoid(y * w, y) / z
    m2 = np.trapezoid(y * y * w, y) / z
    return (m2 - m1 * m1) * lam / D


# --------------------------------------------------------------------------
# the legs: each returns (phi_local, lam, y_lo, y_hi) for a given control eps
# --------------------------------------------------------------------------

def leg_fold(eps):
    """x' = -eps + x^2.  Phi(x) = eps*x - x^3/3.  Stable x* = -sqrt(eps)."""
    lam = 2.0 * np.sqrt(eps)
    phi = lambda y: 0.5 * lam * y**2 - y**3 / 3.0
    return phi, lam, None, lam          # barrier at y = lam (i.e. x = +sqrt(eps))


def leg_sis(eps, beta=3.0):
    """I' = beta*I*(1-I) - gamma*I, gamma = beta*(1-eps).  I* = eps."""
    lam = beta * eps
    phi = lambda y: 0.5 * lam * y**2 + beta * y**3 / 3.0
    return phi, lam, -eps, 1.0 - eps    # barrier at I=0; state space ends at I=1


def leg_ising(eps):
    """Mean-field Ising, T = 1 + eps.  Phi(m) = m^2/2 - T ln(2 cosh(m/T))."""
    T = 1.0 + eps
    lam = 1.0 - 1.0 / T
    # ln(2 cosh(x)) = logaddexp(x, -x); the constant makes phi(0) = 0
    phi = lambda m: 0.5 * m**2 - T * np.logaddexp(m / T, -m / T) + T * np.log(2.0)
    return phi, lam, None, None


def leg_blume_capel(T, a=1.0 / 3.0):
    """Mean-field Blume-Capel on the line a = 2 e^{-D/T}/(1 + 2 e^{-D/T}) = a.

    Phi(m) = m^2/2 - T ln(1 + A cosh(m/T)),  A = a/(1-a).
    On a = 1/3 the quartic coefficient vanishes identically -> leading term is
    sextic.  Critical at T = a.
    """
    A = a / (1.0 - a)
    lam = 1.0 - a / T
    lh = np.log(0.5 * A)
    base = np.log(1.0 + A)
    # log(1 + A cosh x) = logaddexp(logaddexp(0, lh+x), lh-x), overflow-safe
    phi = lambda m: 0.5 * m**2 - T * (
        np.logaddexp(np.logaddexp(0.0, lh + m / T), lh - m / T) - base)
    return phi, lam, None, None


def leg_quadratic(lam):
    """Exactly harmonic control (the MP-edge loss is quadratic in parameters)."""
    phi = lambda y: 0.5 * lam * y**2
    return phi, lam, None, None


# --------------------------------------------------------------------------
# crossover location and exponent fits
# --------------------------------------------------------------------------

def crossovers_for_D(make_leg, D, deltas, eps_hi, eps_lo=1e-10, n_scan=110):
    """Locate, for each threshold, the OUTERMOST control value at which the
    rounding ratio first departs from 1 by delta.

    A plain bisection on |R-1| - delta is wrong here: for odd p the well
    eventually dissolves, R turns over and comes back through 1, so the
    equation has several roots and bisection lands on different branches at
    different D.  Scanning inward from the harmonic end and bracketing the
    first crossing picks the same branch every time.
    """
    def dev(eps):
        phi, lam, ylo, yhi = make_leg(eps)
        return abs(rounding_ratio(phi, lam, D, ylo, yhi) - 1.0)

    grid = np.logspace(np.log10(eps_hi), np.log10(eps_lo), n_scan)
    devs = np.array([dev(e) for e in grid])
    out = {}
    for delta in deltas:
        idx = np.flatnonzero(devs >= delta)
        if idx.size == 0 or idx[0] == 0:
            out[delta] = (None, None)          # never departs / already departed
            continue
        i = idx[0]
        lo, hi = np.log(grid[i]), np.log(grid[i - 1])   # dev(lo) >= delta > dev(hi)
        for _ in range(45):
            mid = 0.5 * (lo + hi)
            if dev(np.exp(mid)) >= delta:
                lo = mid
            else:
                hi = mid
        eps_c = np.exp(0.5 * (lo + hi))
        _, lam_c, _, _ = make_leg(eps_c)
        out[delta] = (lam_c, eps_c)
    return out


def fit_slope(x, y):
    """least-squares slope of log y vs log x, plus max residual."""
    lx, ly = np.log(np.asarray(x)), np.log(np.asarray(y))
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    resid = ly - A @ coef
    return float(coef[0]), float(np.max(np.abs(resid)))


def sweep(name, make_leg, p, k, eps_hi, d_grid=D_GRID, deltas=DELTAS):
    """Fit the lambda-chart and bare-chart crossover exponents for one leg."""
    out = {"leg": name, "p": p, "k": k, "eps_hi": eps_hi,
           "predicted_lambda_exponent": None if p is None else (p - 2.0) / p,
           "by_threshold": {}}
    if p is not None:
        out["predicted_bare_exponent"] = (p - 2.0) / (p * k)
    per_D = {D: crossovers_for_D(make_leg, D, deltas, eps_hi) for D in d_grid}
    for delta in deltas:
        lams, epss, Ds = [], [], []
        for D in d_grid:
            lam_c, eps_c = per_D[D][delta]
            if lam_c is not None:
                lams.append(lam_c)
                epss.append(eps_c)
                Ds.append(D)
        if len(Ds) < 4:
            out["by_threshold"][f"{delta:.2f}"] = {"n": len(Ds), "status": "unbracketed"}
            continue
        s_lam, r_lam = fit_slope(Ds, lams)
        s_eps, r_eps = fit_slope(Ds, epss)
        out["by_threshold"][f"{delta:.2f}"] = {
            "n": len(Ds),
            "lambda_chart_exponent": s_lam,
            "lambda_chart_max_resid": r_lam,
            "bare_chart_exponent": s_eps,
            "bare_chart_max_resid": r_eps,
            "lambda_c": [float(v) for v in lams],
            "eps_c": [float(v) for v in epss],
            "D": [float(v) for v in Ds],
        }
    return out


# --------------------------------------------------------------------------
# tau * lambda (P7)
# --------------------------------------------------------------------------

def tau_lambda(drift, lam, D, rng, n_rep=64, n_step=60000, steps_per_tau=100):
    """Integrated autocorrelation time of the Langevin trajectory, times lam."""
    dt = 1.0 / (lam * steps_per_tau)
    y = np.zeros(n_rep)
    burn = 20 * steps_per_tau
    s = np.sqrt(2.0 * D * dt)
    for _ in range(burn):
        y = y + drift(y) * dt + s * rng.standard_normal(n_rep)
    traj = np.empty((n_step, n_rep))
    for i in range(n_step):
        y = y + drift(y) * dt + s * rng.standard_normal(n_rep)
        traj[i] = y
    traj -= traj.mean(axis=0, keepdims=True)
    nfft = 1 << (2 * n_step - 1).bit_length()
    F = np.fft.rfft(traj, n=nfft, axis=0)
    acf = np.fft.irfft(F * np.conj(F), n=nfft, axis=0)[:n_step].mean(axis=1)
    acf /= acf[0]
    zero = np.argmax(acf <= 0.0)
    zero = len(acf) if zero == 0 and acf[0] > 0 and np.all(acf > 0) else zero
    tau = (np.sum(acf[:zero]) - 0.5) * dt
    return float(tau * lam)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    rng = np.random.default_rng(SEED)
    res = {"seed": SEED, "C_cut": C_CUT, "thresholds": DELTAS}

    # ---- diagnostic: confirm p by numerical Taylor expansion --------------
    def taylor(phi, lam, order=8, h=None):
        h = h or 1e-2
        js = np.arange(-order, order + 1)
        ys = js * h
        vals = phi(ys)
        # solve Vandermonde for the Taylor coefficients
        V = np.vander(ys, order + 1, increasing=True)
        coef, *_ = np.linalg.lstsq(V, vals, rcond=None)
        return coef

    phi_c, lam_c_, _, _ = leg_ising(0.30)
    phi_d, lam_d_, _, _ = leg_blume_capel(0.50)
    tc, td = taylor(phi_c, lam_c_), taylor(phi_d, lam_d_)
    res["taylor_check"] = {
        "ising_T1.30": {"c2": float(tc[2]), "c4": float(tc[4]), "c6": float(tc[6]),
                        "lambda": float(lam_c_), "2c2_vs_lambda": float(2 * tc[2])},
        "blume_capel_T0.50": {"c2": float(td[2]), "c4": float(td[4]), "c6": float(td[6]),
                              "lambda": float(lam_d_), "2c2_vs_lambda": float(2 * td[2])},
    }

    # ---- P1 / P2 / P3 / P4: the crossover exponents -----------------------
    # eps_hi is the harmonic end of the scan; SIS needs 0.2 because its state
    # space is I in [0,1] and I* = eps, so eps -> 1 collapses the well's domain.
    legs = [
        ("A_fold",        lambda e: leg_fold(e),                    3, 0.5, 1.0),
        ("B_sis",         lambda e: leg_sis(e),                     3, 1.0, 0.2),
        ("C_ising",       lambda e: leg_ising(e),                   4, 1.0, 1.0),
        ("D_blume_capel", lambda e: leg_blume_capel(1.0 / 3.0 + e), 6, 1.0, 1.0),
    ]
    res["sweeps"] = [sweep(n, f, p, k, eh) for n, f, p, k, eh in legs]

    # ---- P6: null control, exactly quadratic ------------------------------
    Rs = []
    for D in D_GRID:
        for lam in np.logspace(-6, 0, 7):
            phi, l, ylo, yhi = leg_quadratic(lam)
            Rs.append(rounding_ratio(phi, l, D, ylo, yhi))
    Rs = np.array(Rs)
    res["null_control"] = {
        "n": int(Rs.size),
        "max_abs_dev_from_1": float(np.max(np.abs(Rs - 1.0))),
        "mean_R": float(Rs.mean()),
    }

    # ---- P6b: the MP-edge chart order k, measured on random matrices ------
    N = 4000
    eps_list = np.array([0.40, 0.30, 0.22, 0.16, 0.12, 0.09, 0.07])
    lam_min = []
    for e in eps_list:
        gam = 1.0 - e
        P = int(round(gam * N))
        vals = []
        for _ in range(3):
            X = rng.standard_normal((N, P))
            s = np.linalg.svd(X / np.sqrt(N), compute_uv=False)
            vals.append(s[-1] ** 2)
        lam_min.append(float(np.mean(vals)))
    k_mp, r_mp = fit_slope(eps_list, lam_min)
    res["mp_edge"] = {
        "N": N, "eps": eps_list.tolist(), "lambda_min": lam_min,
        "fitted_k": k_mp, "max_resid": r_mp, "predicted_k": 2.0,
        "theory_1_minus_sqrt_gamma_sq": [float((1 - np.sqrt(1 - e)) ** 2) for e in eps_list],
    }

    # ---- P5: explicit reparameterisation ----------------------------------
    repar = []
    for name, idx in [("A_fold", 0), ("C_ising", 2)]:
        nm, mk, p, k, eh = legs[idx]
        base = [s for s in res["sweeps"] if s["leg"] == nm][0]["by_threshold"]["0.10"]
        lam_list = np.array(base["lambda_c"])
        eps_list = np.array(base["eps_c"])
        Dl = np.array(base["D"])
        for a in [0.5, 2.0, 3.0]:
            # eps' = eps^a  =>  k' = k/a  =>  bare exponent (p-2)/(p k') = a*(p-2)/(p k)
            s_lam, _ = fit_slope(Dl, lam_list)
            s_eps, _ = fit_slope(Dl, eps_list ** a)
            repar.append({"leg": name, "a": a,
                          "lambda_chart_exponent": s_lam,
                          "lambda_chart_exponent_unreparameterised": base["lambda_chart_exponent"],
                          "bare_exponent_reparameterised": s_eps,
                          "bare_exponent_expected": base["bare_chart_exponent"] * a})
    res["reparameterisation"] = repar

    # ---- P7: tau * lambda -------------------------------------------------
    tl = {}
    # fold: eps=0.25 -> lam=1.0, barrier lam^3/6 = 0.167 >> D
    tl["A_fold"] = tau_lambda(lambda y: -(1.0 * y - y**2), 1.0, 5e-3, rng)
    # sis: beta=3, eps=0.3 -> lam=0.9, barrier 0.0135 >> D
    tl["B_sis"] = tau_lambda(lambda y: -(0.9 * y + 3.0 * y**2), 0.9, 5e-4, rng)
    # ising: T=1.3 -> lam=0.2308
    T = 1.3
    tl["C_ising"] = tau_lambda(lambda m: -(m - np.tanh(m / T)), 1.0 - 1.0 / T, 2e-3, rng)
    # blume-capel on the line: T=0.5 -> lam=1/3
    A_bc, Tb = 0.5, 0.5
    tl["D_blume_capel"] = tau_lambda(
        lambda m: -(m - A_bc * np.sinh(m / Tb) / (1.0 + A_bc * np.cosh(m / Tb))),
        1.0 - (1.0 / 3.0) / Tb, 2e-3, rng)
    res["tau_lambda"] = tl

    # ---- P8: off the tricritical line (exploratory) -----------------------
    #
    # Moving off the line by delta_a reinstates a quartic term with
    #     c4 = (a/8 - 1/24)*delta_a/T^3
    # while the sextic c6 stays put.  The quartic group reaches the rounding
    # threshold first when  D < c4^3/(c6^2 u*)  -- so the SMALL-D end is the
    # p=4 side and the LARGE-D end is the p=6 side, and the crossover noise
    # scale obeys  D_x  ~  c4^3  ~  delta_a^3.
    #
    D_FINE = np.logspace(-9.0, -3.0, 25)
    off, dx_da, dx_D = [], [], []
    for da in [0.0, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2]:
        a = 1.0 / 3.0 + da
        mk = lambda e, a=a: leg_blume_capel(a + e, a=a)
        s = sweep(f"bc_da={da}", mk, 6, 1.0, 1.0, d_grid=D_FINE, deltas=[0.10])
        b = s["by_threshold"].get("0.10", {})
        entry = {"delta_a": da}
        if "lambda_c" in b and len(b["D"]) > 6:
            lD, ll = np.log(np.array(b["D"])), np.log(np.array(b["lambda_c"]))
            slope = np.gradient(ll, lD)                    # local log-log slope
            mid = 0.5 * (0.5 + 2.0 / 3.0)                  # 0.5833
            entry["local_slopes"] = [float(v) for v in slope]
            entry["D"] = [float(v) for v in b["D"]]
            entry["exponent_lowD"] = float(np.mean(slope[:4]))
            entry["exponent_highD"] = float(np.mean(slope[-4:]))
            cross = np.flatnonzero((slope[:-1] < mid) & (slope[1:] >= mid))
            if cross.size and da > 0:
                i = cross[0]
                t = (mid - slope[i]) / (slope[i + 1] - slope[i])
                Dx = float(np.exp(lD[i] + t * (lD[i + 1] - lD[i])))
                entry["D_crossover"] = Dx
                dx_da.append(da)
                dx_D.append(Dx)
        off.append(entry)
    res["off_tricritical_line"] = off
    if len(dx_da) >= 3:
        s_dx, r_dx = fit_slope(dx_da, dx_D)
        res["off_line_crossover_scaling"] = {
            "delta_a": dx_da, "D_crossover": dx_D,
            "fitted_exponent": s_dx, "predicted_exponent": 3.0, "max_resid": r_dx}

    with open("verdict.json", "w") as fh:
        json.dump(res, fh, indent=2)

    # ---- report -----------------------------------------------------------
    print("=" * 74)
    print("D1 - the chart law")
    print("=" * 74)
    print("\nTaylor check (confirming p):")
    for kk, vv in res["taylor_check"].items():
        print(f"  {kk:22s} lambda={vv['lambda']:.6f}  2*c2={vv['2c2_vs_lambda']:.6f}"
              f"  c4={vv['c4']:+.3e}  c6={vv['c6']:+.3e}")

    print("\nP1/P2/P3 - crossover exponents (threshold |R-1| = 0.10):")
    print(f"  {'leg':16s} {'p':>3s} {'k':>5s} {'lam-chart':>10s} {'pred':>7s} "
          f"{'bare':>8s} {'pred':>7s}")
    for s in res["sweeps"]:
        b = s["by_threshold"].get("0.10", {})
        if "lambda_chart_exponent" not in b:
            print(f"  {s['leg']:16s} unbracketed")
            continue
        print(f"  {s['leg']:16s} {s['p']:3d} {s['k']:5.2f} "
              f"{b['lambda_chart_exponent']:10.4f} {s['predicted_lambda_exponent']:7.4f} "
              f"{b['bare_chart_exponent']:8.4f} {s['predicted_bare_exponent']:7.4f}")

    print("\nP4 - threshold independence (lambda chart):")
    for s in res["sweeps"]:
        vals = [s["by_threshold"].get(f"{d:.2f}", {}).get("lambda_chart_exponent")
                for d in DELTAS]
        vals = [v for v in vals if v is not None]
        if vals:
            print(f"  {s['leg']:16s} " + "  ".join(f"{v:.4f}" for v in vals)
                  + f"   spread={max(vals)-min(vals):.4f}")

    print("\nP5 - explicit reparameterisation eps' = eps^a:")
    for r in res["reparameterisation"]:
        print(f"  {r['leg']:10s} a={r['a']:.1f}  lam-chart={r['lambda_chart_exponent']:.4f}"
              f"   bare={r['bare_exponent_reparameterised']:.4f}"
              f" (expected {r['bare_exponent_expected']:.4f})")

    print("\nP6 - null control (exactly quadratic):")
    print(f"  max |R-1| over {res['null_control']['n']} (lambda,D) points = "
          f"{res['null_control']['max_abs_dev_from_1']:.3e}")
    print(f"  MP edge fitted k = {res['mp_edge']['fitted_k']:.4f} (predicted 2.0)")

    print("\nP7 - tau * lambda:")
    for kk, vv in res["tau_lambda"].items():
        print(f"  {kk:16s} {vv:.4f}")

    print("\nP8 - off the tricritical line (local lambda-chart slope):")
    print(f"  {'delta_a':>9s} {'low-D':>8s} {'high-D':>8s} {'D_crossover':>13s}")
    for o in res["off_tricritical_line"]:
        f = lambda k: f"{o[k]:8.4f}" if k in o else "     n/a"
        dx = f"{o['D_crossover']:13.3e}" if "D_crossover" in o else "          n/a"
        print(f"  {o['delta_a']:9.4f} {f('exponent_lowD')} {f('exponent_highD')} {dx}")
    if "off_line_crossover_scaling" in res:
        c = res["off_line_crossover_scaling"]
        print(f"  D_crossover ~ delta_a^{c['fitted_exponent']:.3f} "
              f"(predicted 3.000, max resid {c['max_resid']:.3f})")

    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
