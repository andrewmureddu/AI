"""D12 -- the residue under a genuinely nonlinear description map.

Registered in PREREGISTRATION.md before this file existed.

Leg 1 (P1-P2): the iid CLT map on D11's U-family. Exact CDF of the iid sum
               (binomial mixture of Gaussians), exact quantiles.
Leg 2 (P3-P6): period doubling. Route A measures log-slopes on raw maps
               (mpmath, 80 digits). Route B solves T g = g by collocation and
               takes the leading eigenvalue of DT(g). The routes share no code.

Deterministic. numpy + scipy + mpmath.
"""
import json
import time

import mpmath as mp
import numpy as np
from scipy.optimize import brentq, fsolve
from scipy.special import ndtr
from scipy.stats import binom

mp.mp.dps = 80
T0 = time.time()

# --------------------------------------------------------------------------
# Leg 1: iid CLT map on the U-family
# --------------------------------------------------------------------------
CONFIGS = {
    "gaussian": (1.0, 1.0, 1.0),
    "mild": (1.0, 2.0, 0.5),
    "strong": (1.0, 5.0, 0.5),
    "rare_extreme": (1.0, 10.0, 0.9),
    "asymmetric": (0.5, 3.0, 0.3),
}
QS = (0.025, 0.25, 0.75, 0.975)
SR_GAUSS = None


def iid_sum_quantiles(n, u1, u2, p):
    """Exact quantiles of S_n = sum of n iid U_i Z_i, U in {u1,u2} w.p. {p,1-p}.

    S_n | K=k ~ N(0, k u1^2 + (n-k) u2^2), K ~ Binomial(n, p).
    """
    n = int(n)
    if p >= 1.0:
        ks = np.array([n])
        w = np.array([1.0])
    else:
        m, s = n * p, np.sqrt(n * p * (1 - p))
        lo, hi = max(0, int(m - 14 * s) - 2), min(n, int(m + 14 * s) + 2)
        ks = np.arange(lo, hi + 1)
        w = binom.pmf(ks, n, p)
        w = w / w.sum()
    sd = np.sqrt(ks * u1**2 + (n - ks) * u2**2)
    scale = sd.max()

    def cdf(x):
        return float(np.dot(w, ndtr(x / sd)))

    return [brentq(lambda x: cdf(x) - q, -12 * scale, 12 * scale,
                   xtol=1e-13 * scale, rtol=1e-15) for q in QS]


def leg1():
    global SR_GAUSS
    from scipy.special import ndtri
    SR_GAUSS = ndtri(0.975) / ndtri(0.75)
    ns = np.unique(np.round(np.logspace(3, 5, 15)).astype(int))
    out = {}
    for name, (u1, u2, p) in CONFIGS.items():
        iqr, delta = [], []
        for n in ns:
            q = iid_sum_quantiles(n, u1, u2, p)
            iqr.append(q[2] - q[1])
            delta.append((q[3] - q[0]) / (q[2] - q[1]) - SR_GAUSS)
        iqr, delta = np.array(iqr), np.array(delta)
        H = np.polyfit(np.log(ns), np.log(iqr), 1)[0]
        rec = {"H_iqr": H, "max_abs_delta": float(np.abs(delta).max()),
               "delta_first": float(delta[0]), "delta_last": float(delta[-1])}
        if name == "gaussian":
            rec["P1_ok"] = bool(np.abs(delta).max() < 1e-9)
            rec["P2_ok"] = bool(abs(H - 0.5) < 5e-3)
        else:
            sl = np.polyfit(np.log(ns), np.log(np.abs(delta)), 1)[0]
            # exact cumulant identity for reference: excess kurtosis * n
            m2 = p * u1**2 + (1 - p) * u2**2
            m4 = p * u1**4 + (1 - p) * u2**4
            rec.update({"slope_shape": sl, "ratio": sl / H,
                        "excess_kurtosis_n1": 3 * m4 / m2**2 - 3,
                        "P1_ok": bool(abs(sl + 1.0) < 0.05),
                        "P2_ok": bool(abs(H - 0.5) < 5e-3
                                      and abs(sl / H + 2.0) < 0.12)})
        out[name] = rec
    return out, [int(n) for n in ns]


# --------------------------------------------------------------------------
# Leg 2, route A: raw maps, superstable cascade (mpmath)
# --------------------------------------------------------------------------
def make_family(kind, z, c=None):
    z = mp.mpf(z)
    if kind == "A":       # 1 - a |x|^z
        def f(x, a):
            return 1 - a * abs(x) ** z
        a1 = mp.mpf(1)
    elif kind == "B":     # 1 - a |sin x|^z
        def f(x, a):
            return 1 - a * abs(mp.sin(x)) ** z
        a1 = mp.sin(1) ** (-z)
    elif kind == "dil":   # c * fA(x / c)
        c = mp.mpf(c)

        def f(x, a):
            return c * (1 - a * abs(x / c) ** z)
        a1 = mp.mpf(1)
    else:
        raise ValueError(kind)
    return f, a1


def iterate(f, a, k):
    x = mp.mpf(0)
    for _ in range(k):
        x = f(x, a)
    return x


def superstable(f, a1, nmax):
    """a_n with f_a^{2^n}(0) = 0 (a_0 = 0, a_1 given), and nearest returns d_n."""
    a = [mp.mpf(0), a1]
    for n in range(2, nmax + 1):
        k = 2 ** n
        gap = a[-1] - a[-2]
        F = lambda t: iterate(f, t, k)  # noqa: E731
        # first sign change above a_{n-1}: scan, then bisect, then secant
        step = gap / 60
        lo = a[-1] + step / 8
        flo = F(lo)
        hi, fhi = None, None
        t = lo
        for _ in range(600):
            t = t + step
            ft = F(t)
            if ft * flo < 0:
                hi, fhi = t, ft
                break
            lo, flo = t, ft
        if hi is None:
            raise RuntimeError(f"no bracket at level {n}")
        for _ in range(12):
            mid = (lo + hi) / 2
            fm = F(mid)
            if fm * flo < 0:
                hi, fhi = mid, fm
            else:
                lo, flo = mid, fm
        root = mp.findroot(F, (lo, hi), solver="secant", tol=mp.mpf(10) ** (-70),
                           maxsteps=60)
        if not (lo <= root <= hi):
            raise RuntimeError(f"root left its bracket at level {n}")
        a.append(root)
    d = [None] + [iterate(f, a[n], 2 ** (n - 1)) for n in range(1, nmax + 1)]
    return a, d


def route_A(kind, z, nmax=12, c=None):
    f, a1 = make_family(kind, z, c)
    a, d = superstable(f, a1, nmax)
    gaps = [None] + [a[n] - a[n - 1] for n in range(1, nmax + 1)]
    delta_n = [float(gaps[n] / gaps[n + 1]) for n in range(1, nmax)]
    alpha_n = [float(abs(d[n] / d[n + 1])) for n in range(1, nmax)]
    lvl = np.arange(6, nmax + 1)
    lg = np.array([float(mp.log(gaps[n])) for n in lvl])
    ld = np.array([float(mp.log(abs(d[n]))) for n in lvl])
    return {
        "ln_delta_last": float(mp.log(gaps[nmax - 1] / gaps[nmax])),
        "ln_alpha_last": float(mp.log(abs(d[nmax - 1] / d[nmax]))),
        "ln_delta_reg": -np.polyfit(lvl, lg, 1)[0],
        "ln_alpha_reg": -np.polyfit(lvl, ld, 1)[0],
        "delta_n": delta_n, "alpha_n": alpha_n,
        "a_inf_est": float(a[nmax] + gaps[nmax] / (gaps[nmax - 1] / gaps[nmax] - 1)),
        "_a": a, "_d": d,
    }


# --------------------------------------------------------------------------
# Leg 2, route B: fixed point of T and its linearization (collocation)
# --------------------------------------------------------------------------
def cheb_nodes(N):
    k = np.arange(N)
    return 0.5 * (1 - np.cos(np.pi * (2 * k + 1) / (2 * N)))  # in (0,1)


def g_eval(c, x, z):
    """g(x) = 1 + sum_{k>=1} c_k |x|^{zk}."""
    t = np.abs(x) ** z
    return 1 + sum(ck * t ** (k + 1) for k, ck in enumerate(c))


def gprime_eval(c, x, z):
    ax = np.abs(x)
    t = ax ** z
    Fp = sum((k + 1) * ck * t ** k for k, ck in enumerate(c))
    return Fp * z * ax ** (z - 1) * np.sign(x)


def solve_fixed_point(z, N, c0):
    tn = cheb_nodes(N)
    xn = tn ** (1.0 / z)

    def resid(c):
        alpha = -1.0 / g_eval(c, 1.0, z)
        return g_eval(c, xn, z) + alpha * g_eval(c, g_eval(c, xn / alpha, z), z)

    c, info, ier, msg = fsolve(resid, c0, xtol=1e-14, full_output=True)
    return c, float(np.abs(resid(c)).max()), ier


def spectrum(c, z, N):
    """Eigenvalues of (L h)(x) = -alpha [ h(g(x/a)) + g'(g(x/a)) h(x/a) ]
    on h in span{ |x|^{zk}, k = 0..N-1 }."""
    alpha = -1.0 / g_eval(c, 1.0, z)
    tn = cheb_nodes(N)
    xn = tn ** (1.0 / z)
    y = g_eval(c, xn / alpha, z)
    gp = gprime_eval(c, y, z)
    B = np.empty((N, N))
    R = np.empty((N, N))
    for k in range(N):
        B[:, k] = tn ** k
        R[:, k] = -alpha * (np.abs(y) ** (z * k) + gp * (tn / alpha ** z) ** k)
    ev = np.linalg.eigvals(np.linalg.solve(B, R))
    ev = ev[np.argsort(-np.abs(ev))]
    return alpha, ev


def route_B(zs, Ns=(12, 16), dz=0.25):
    """Continuation in z from the classical z = 2 fixed point."""
    out = {}
    for N in Ns:
        c = np.zeros(N)
        c[:3] = [-1.5276, 0.1048, 0.0267]
        path = sorted(set(list(zs) + [round(v, 6) for v in np.arange(1.5, 8.0001, dz)]))
        start = path.index(2.0)
        sols = {}
        cc = c.copy()
        for zz in path[start:]:
            cc, res, ier = solve_fixed_point(zz, N, cc)
            sols[zz] = (cc.copy(), res, ier)
        cc = sols[2.0][0].copy()
        for zz in path[:start][::-1]:
            cc, res, ier = solve_fixed_point(zz, N, cc)
            sols[zz] = (cc.copy(), res, ier)
        for zz in zs:
            cz, res, ier = sols[zz]
            alpha, ev = spectrum(cz, zz, N)
            out.setdefault(zz, {})[N] = {
                "alpha": float(alpha), "delta": float(ev[0].real),
                "delta_imag": float(ev[0].imag), "resid": res, "ier": int(ier),
                "next_eigs": [complex(e) for e in ev[1:6]],
            }
    return out


# --------------------------------------------------------------------------
def main():
    verdict = {"stone": "D12"}

    # ---- Leg 1
    l1, ns = leg1()
    verdict["leg1_iid_clt"] = {"n_grid": ns, "SR_gauss": float(SR_GAUSS),
                               "configs": l1}
    verdict["P1_shape_slope_minus_one"] = all(r["P1_ok"] for r in l1.values())
    verdict["P2_scale_half_and_ratio_minus_two"] = all(r["P2_ok"] for r in l1.values())
    print("Leg 1 (iid CLT map on the U-family)")
    for k, r in l1.items():
        print(f"  {k:13s} H={r['H_iqr']:.6f}  slope_shape="
              f"{r.get('slope_shape', float('nan')):+.4f}  ratio="
              f"{r.get('ratio', float('nan')):+.4f}  P1={r['P1_ok']} P2={r['P2_ok']}")

    # ---- Leg 2
    ZS = [1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0]
    B = route_B(ZS)
    A = {z: route_A("A", z) for z in ZS}
    Bf = {z: route_A("B", z) for z in (2.0, 3.0, 4.0)}

    rows, p3_last, p3_reg, conv = {}, True, True, {}
    for z in ZS:
        b12, b16 = B[z][12], B[z][16]
        gate = (abs(b12["alpha"] - b16["alpha"]) < 1e-7
                and abs(b12["delta"] - b16["delta"]) < 1e-7)
        conv[z] = gate
        lnd, lna = np.log(b16["delta"]), np.log(b16["alpha"])
        a = A[z]
        r = {
            "routeB_delta": b16["delta"], "routeB_alpha": b16["alpha"],
            "routeB_gate_N12_vs_N16": bool(gate),
            "routeB_dalpha": abs(b12["alpha"] - b16["alpha"]),
            "routeB_ddelta": abs(b12["delta"] - b16["delta"]),
            "routeB_resid": b16["resid"],
            "routeB_next_eigs": [[e.real, e.imag] for e in b16["next_eigs"]],
            "routeA_delta_last": float(np.exp(a["ln_delta_last"])),
            "routeA_alpha_last": float(np.exp(a["ln_alpha_last"])),
            "dln_delta_last": abs(a["ln_delta_last"] - lnd),
            "dln_alpha_last": abs(a["ln_alpha_last"] - lna),
            "dln_delta_reg": abs(a["ln_delta_reg"] - lnd),
            "dln_alpha_reg": abs(a["ln_alpha_reg"] - lna),
            "rho_B": lna / lnd,
            "rho_A": a["ln_alpha_last"] / a["ln_delta_last"],
            "a_inf_est": a["a_inf_est"],
            "delta_n": a["delta_n"], "alpha_n": a["alpha_n"],
        }
        r["P3_last_ok"] = bool(r["dln_delta_last"] < 1e-4 and r["dln_alpha_last"] < 1e-4)
        r["P3_reg_ok"] = bool(r["dln_delta_reg"] < 2e-3 and r["dln_alpha_reg"] < 2e-3)
        # post hoc: per-level convergence factor of delta_n, alpha_n
        dn, an = np.array(a["delta_n"]), np.array(a["alpha_n"])
        ed, ea = np.abs(dn - b16["delta"]), np.abs(an - b16["alpha"])
        r["posthoc_conv_factor_delta"] = [float(x) for x in ed[2:7] / ed[3:8]]
        r["posthoc_conv_factor_alpha"] = [float(x) for x in ea[2:7] / ea[3:8]]
        p3_last &= r["P3_last_ok"]
        p3_reg &= r["P3_reg_ok"]
        rows[str(z)] = r
    verdict["leg2_period_doubling"] = rows
    verdict["routeB_all_converged"] = all(conv.values())
    verdict["P3_last_pair_within_1e-4"] = bool(p3_last)
    verdict["P3_house_regression_within_2e-3"] = bool(p3_reg)

    rhoB = [rows[str(z)]["rho_B"] for z in ZS]
    rhoA = [rows[str(z)]["rho_A"] for z in ZS]
    verdict["rho_B"] = rhoB
    verdict["rho_A"] = rhoA
    verdict["P4_rho_strictly_decreasing_and_spread"] = bool(
        all(np.diff(rhoB) < 0) and all(np.diff(rhoA) < 0)
        and rhoB[0] / rhoB[-1] - 1 >= 1.0)
    verdict["rho_spread"] = rhoB[0] / rhoB[-1] - 1

    recall = {2.0: (4.6692016, 2.5029079), 3.0: (5.9679687, 1.9276910),
              4.0: (7.2846862, 1.6903030), 6.0: (9.2962468, 1.4677425)}
    p5 = {}
    for z, (d, al) in recall.items():
        p5[str(z)] = {"ddelta": abs(B[z][16]["delta"] - d),
                      "dalpha": abs(B[z][16]["alpha"] - al)}
        p5[str(z)]["ok"] = bool(p5[str(z)]["ddelta"] < 1e-6 and p5[str(z)]["dalpha"] < 1e-6)
    verdict["P5_recall"] = p5
    verdict["P5_recall_all_ok"] = all(v["ok"] for v in p5.values())

    p6 = {}
    for z, b in Bf.items():
        lnd, lna = np.log(B[z][16]["delta"]), np.log(B[z][16]["alpha"])
        p6[str(z)] = {"dln_delta_reg": abs(b["ln_delta_reg"] - lnd),
                      "dln_alpha_reg": abs(b["ln_alpha_reg"] - lna),
                      "dln_delta_last": abs(b["ln_delta_last"] - lnd),
                      "dln_alpha_last": abs(b["ln_alpha_last"] - lna)}
        p6[str(z)]["ok"] = bool(p6[str(z)]["dln_delta_reg"] < 2e-3
                                and p6[str(z)]["dln_alpha_reg"] < 2e-3)
    verdict["P6_family_B"] = p6
    verdict["P6_family_B_all_ok"] = all(v["ok"] for v in p6.values())

    # ---- POST HOC (not registered): the registered N=12 vs N=16 gate failed
    # because the N=12 continuation left the solution branch. Re-check route B's
    # own convergence with a finer continuation step and N = 16, 18, 20.
    Bp = route_B(ZS, Ns=(16, 18, 20), dz=0.125)
    ph = {}
    for z in ZS:
        d = [Bp[z][N]["delta"] for N in (16, 18, 20)]
        al = [Bp[z][N]["alpha"] for N in (16, 18, 20)]
        ph[str(z)] = {"delta_N16_18_20": d, "alpha_N16_18_20": al,
                      "ier": [Bp[z][N]["ier"] for N in (16, 18, 20)],
                      "spread_delta": max(d) - min(d), "spread_alpha": max(al) - min(al),
                      "inv_abs_second_nontrivial_eig": float(
                          1 / abs(B[z][16]["next_eigs"][1]))}
    verdict["posthoc_routeB_convergence"] = ph
    print("  post hoc route-B spread (N=16,18,20):",
          {z: (f"{r['spread_delta']:.1e}", f"{r['spread_alpha']:.1e}") for z, r in ph.items()})

    cdil = 0.37
    D = route_A("dil", 2.0, c=cdil)
    a_dev = max(abs(D["_a"][n] - A[2.0]["_a"][n]) for n in range(1, 13))
    d_dev = max(abs(D["_d"][n] / A[2.0]["_d"][n] - mp.mpf(cdil)) for n in range(1, 13))
    verdict["C5_dilation"] = {"max_a_dev": float(a_dev), "max_d_ratio_dev": float(d_dev),
                              "ok": bool(a_dev < mp.mpf(10) ** -60 and d_dev < mp.mpf(10) ** -60)}

    print("\nLeg 2 (period doubling)")
    print("   z   delta_B      alpha_B     gate  dlnd_last dlna_last dlnd_reg  dlna_reg  rho_B")
    for z in ZS:
        r = rows[str(z)]
        print(f"  {z:3.1f} {r['routeB_delta']:.7f} {r['routeB_alpha']:.7f} "
              f"{str(r['routeB_gate_N12_vs_N16']):5s} {r['dln_delta_last']:.1e}  "
              f"{r['dln_alpha_last']:.1e}  {r['dln_delta_reg']:.1e}  "
              f"{r['dln_alpha_reg']:.1e}  {r['rho_B']:.5f}")
    for key in ("routeB_all_converged", "P1_shape_slope_minus_one",
                "P2_scale_half_and_ratio_minus_two", "P3_last_pair_within_1e-4",
                "P3_house_regression_within_2e-3",
                "P4_rho_strictly_decreasing_and_spread", "P5_recall_all_ok",
                "P6_family_B_all_ok"):
        print(f"  {key}: {verdict[key]}")
    print("  P5:", json.dumps(p5))
    print("  P6:", json.dumps(p6))
    print("  C5:", verdict["C5_dilation"])

    verdict["runtime_s"] = round(time.time() - T0, 1)
    with open(__file__.replace("run.py", "verdict.json"), "w") as fh:
        json.dump(verdict, fh, indent=2)
    print(f"\nruntime {verdict['runtime_s']} s")


if __name__ == "__main__":
    main()
