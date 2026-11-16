"""D13 -- D8's m = 2 residue under a literal description map.

Ising on the diamond hierarchical lattice, exact recursion in (K, h).
Registered in PREREGISTRATION.md before this file existed.
Deterministic. mpmath + numpy.
"""
import json
import time

import mpmath as mp
import numpy as np

mp.mp.dps = 30
T0 = time.time()


def lse(a, b):
    """ln(e^a + e^b), stable."""
    return (a if a > b else b) + mp.log1p(mp.exp(-abs(a - b)))


def step(K, h):
    lpp = lse(2 * K + 2 * h, -2 * K)
    lmm = lse(2 * K - 2 * h, -2 * K)
    lpm = lse(h, -h)
    return (lpp + lmm) / 2 - lpm, lpp - lmm, (lpp + lmm) / 2 + lpm


def free_energy(K, h):
    """f = sum_n 4^-(n+1) g(K_n, h_n), truncated below working precision."""
    tol = mp.mpf(2) ** (-mp.mp.prec - 12)
    f, wgt = mp.mpf(0), mp.mpf(1) / 4
    for _ in range(4000):
        K, h, g = step(K, h)
        f += wgt * g
        wgt /= 4
        if wgt * (abs(K) + abs(h) + 1) < tol:
            return f
    raise RuntimeError("free energy did not converge")


Kc = mp.findroot(lambda K: K - mp.log(mp.cosh(2 * K)), 0.6)
lam_t = 2 * mp.tanh(2 * Kc)
lam_h = 2 * (1 + mp.tanh(2 * Kc))
Lt, Lh, L4 = mp.log(lam_t), mp.log(lam_h), mp.log(4)
DELTA = Lh / Lt
OBS = [(0, 1), (0, 2), (0, 3), (1, 1)]            # (l, k): d_t^l d_h^k f
NAMES = ["m", "chi", "-M3", "-dm/dt"]
W = np.array([float(L4 - k * Lh - l * Lt) for l, k in OBS])
ELL = np.array([float(Lt), float(Lh)])


def partials(t, h, orders):
    """F_{lk} = d_a^l d_b^k f(Kc - t a, h b) at (1,1) = t^l h^k (d_t^l d_h^k f)."""
    F = lambda a, b: free_energy(Kc - t * a, h * b)  # noqa: E731
    return {o: mp.diff(F, (1, 1), o) for o in orders}


def slope_matrix(t, h):
    need = set(OBS) | {(l + 1, k) for l, k in OBS} | {(l, k + 1) for l, k in OBS}
    P = partials(t, h, need)
    Y = np.array([[float(P[(l + 1, k)] / P[(l, k)]), float(P[(l, k + 1)] / P[(l, k)])]
                  for l, k in OBS])
    signs = [int(mp.sign(P[o])) for o in OBS]
    logabs = [mp.log(abs(P[(l, k)])) - l * mp.log(t) - k * mp.log(h) for l, k in OBS]
    return Y, signs, logabs


def log_obs(t, h):
    P = partials(t, h, set(OBS))
    return ([mp.log(abs(P[(l, k)])) - l * mp.log(t) - k * mp.log(h) for l, k in OBS],
            [int(mp.sign(P[o])) for o in OBS])


def angles(Y1, Y2):
    Q1, _ = np.linalg.qr(Y1)
    Q2, _ = np.linalg.qr(Y2)
    U, c, Vt = np.linalg.svd(Q1.T @ Q2)
    s = np.linalg.svd(Q2 - Q1 @ (Q1.T @ Q2), compute_uv=False)   # sines
    s = np.sort(np.clip(s, 0, 1))
    common = Q2 @ Vt[0]                    # direction of the largest cosine
    wn = W / np.linalg.norm(W)
    ang_w = float(np.arcsin(min(1.0, np.linalg.norm(common - wn * (wn @ common)))))
    return float(np.arcsin(s[-1])), float(np.arcsin(s[0])), ang_w


def main():
    t0 = mp.mpf("1e-6")
    delta_sf = Lh / (L4 - Lh)
    target = (1 + 1 / delta_sf) / 2

    def dlnm(lnk):
        h = mp.exp(lnk) * t0 ** DELTA
        P = partials(t0, h, {(0, 1), (0, 2)})
        return P[(0, 2)] / P[(0, 1)] - target

    lo, hi = mp.mpf(-25), mp.mpf(25)
    flo, fhi = dlnm(lo), dlnm(hi)
    assert flo > 0 > fhi, (flo, fhi)
    for _ in range(40):
        mid = (lo + hi) / 2
        if dlnm(mid) > 0:
            lo = mid
        else:
            hi = mid
    kstar = mp.exp((lo + hi) / 2)

    verdict = {"stone": "D13", "Kc": float(Kc), "lambda_t": float(lam_t),
               "lambda_h": float(lam_h), "Delta": float(DELTA),
               "delta_strong_field": float(delta_sf), "kappa_star": float(kstar),
               "w": W.tolist(), "ell": ELL.tolist(), "observables": NAMES}
    print(f"Kc={float(Kc):.10f} lam_t={float(lam_t):.8f} lam_h={float(lam_h):.8f} "
          f"Delta={float(DELTA):.6f} kappa*={float(kstar):.6g}")
    print("w =", np.round(W, 6))

    kappas = {"0.1k*": kstar / 10, "k*": kstar, "10k*": kstar * 10}
    res, Ys = {}, {}
    p1 = p2a = p3 = True
    all_signs = set()
    for name, kap in kappas.items():
        rows = []
        for j in range(8):
            t = t0 * lam_t ** (-mp.mpf(j) / 8)
            h = kap * t ** DELTA
            Y, signs, lo0 = slope_matrix(t, h)
            lo1, signs1 = log_obs(lam_t * t, lam_h * h)
            disc = np.array([float(a - b) for a, b in zip(lo1, lo0)]) - W
            e = Y @ ELL - W
            sv = np.linalg.svd(Y, compute_uv=False)
            all_signs.add(tuple(signs))
            all_signs.add(tuple(signs1))
            rows.append({"phase": j, "Y": Y.tolist(), "euler_resid": e.tolist(),
                         "discrete_resid": disc.tolist(),
                         "sigma_ratio": float(sv[1] / sv[0]), "signs": signs})
            Ys[(name, j)] = Y
        E = np.array([r["euler_resid"] for r in rows])
        D = np.array([r["discrete_resid"] for r in rows])
        sr = min(r["sigma_ratio"] for r in rows)
        res[name] = {"kappa": float(kap), "phases": rows,
                     "max_abs_euler": float(np.abs(E).max()),
                     "phase_mean_euler": E.mean(axis=0).tolist(),
                     "max_abs_phase_mean_euler": float(np.abs(E.mean(axis=0)).max()),
                     "max_abs_discrete": float(np.abs(D).max()),
                     "min_sigma_ratio": sr,
                     "Y_phase0": rows[0]["Y"],
                     "Y_phase_spread": float(np.ptp(np.array([r["Y"] for r in rows]),
                                                    axis=0).max())}
        p1 &= res[name]["max_abs_discrete"] < 1e-4
        p2a &= (res[name]["max_abs_euler"] < 1e-2
                and res[name]["max_abs_phase_mean_euler"] < 1e-4)
        p3 &= sr > 0.05
        print(f"  {name:6s} kappa={float(kap):.4g}  max|disc|={res[name]['max_abs_discrete']:.2e}"
              f"  max|euler|={res[name]['max_abs_euler']:.2e}"
              f"  |mean euler|={res[name]['max_abs_phase_mean_euler']:.2e}"
              f"  min s2/s1={sr:.4f}  Y spread over phase={res[name]['Y_phase_spread']:.2e}")
        print("     Y(phase 0) =", np.round(Ys[(name, 0)], 5).tolist())
    verdict["rays"] = res
    verdict["sign_patterns_seen"] = [list(s) for s in all_signs]
    verdict["guard_signs_constant"] = len(all_signs) == 1

    pairs = {"far": ("0.1k*", "10k*", 0.05), "low": ("0.1k*", "k*", 0.02),
             "high": ("k*", "10k*", 0.02)}
    p4, ang = True, {}
    for nm, (a, b, bar) in pairs.items():
        big, small, aw = angles(Ys[(a, 0)], Ys[(b, 0)])
        ok = big >= bar and small <= 1e-2 and aw <= 1e-2
        ang[nm] = {"pair": [a, b], "largest_angle": big, "smallest_angle": small,
                   "common_dir_angle_to_w": aw, "bar": bar, "ok": bool(ok)}
        p4 &= ok
        print(f"  angles {a} vs {b}: largest={big:.4f}  smallest={small:.2e}  "
              f"common-to-w={aw:.2e}  ok={ok}")
    verdict["angles"] = ang

    # ---- POST HOC (not registered): the registered angles use one phase, and
    # the log-periodic modulation turned out larger than budgeted. Repeat with
    # the phase-averaged slope matrix, for which Y.ell = w holds to ~1e-7.
    Ybar = {nm: np.mean([Ys[(nm, j)] for j in range(8)], axis=0) for nm in kappas}
    ph = {}
    for nm, (a, b, bar) in pairs.items():
        big, small, aw = angles(Ybar[a], Ybar[b])
        ph[nm] = {"pair": [a, b], "largest_angle": big, "smallest_angle": small,
                  "common_dir_angle_to_w": aw}
        print(f"  post hoc, phase-averaged {a} vs {b}: largest={big:.4f}  "
              f"smallest={small:.2e}  common-to-w={aw:.2e}")
    verdict["posthoc_phase_averaged_angles"] = ph
    verdict["posthoc_Ybar"] = {nm: Ybar[nm].tolist() for nm in kappas}
    verdict["P1_discrete_relation_1e-4"] = bool(p1)
    verdict["P2_euler_bounded_and_mean_zero"] = bool(p2a)
    verdict["P3_rank_two"] = bool(p3)
    verdict["P4_plane_moves_line_stays"] = bool(p4)
    for k in ("P1_discrete_relation_1e-4", "P2_euler_bounded_and_mean_zero",
              "P3_rank_two", "P4_plane_moves_line_stays", "guard_signs_constant"):
        print(f"  {k}: {verdict[k]}")
    verdict["runtime_s"] = round(time.time() - T0, 1)
    with open(__file__.replace("run.py", "verdict.json"), "w") as fh:
        json.dump(verdict, fh, indent=2)
    print(f"runtime {verdict['runtime_s']} s")


if __name__ == "__main__":
    main()
