"""
P8, re-registered and re-run.  See P8-REREGISTRATION.md.

D1's P8 got its direction backwards, and the D_x ~ delta_a^3 law that replaced it
was derived AFTER the run -- post-hoc, and logged as a debt three cycles running.

This pays the debt and strengthens it.  The derivation actually gives a TWO-variable
law,

        D_x  =  c4^3 / (u* c6^2)

whose c6 exponent the post-hoc delta_a^3 result never tested (it is the
c6-constant slice).  Both coefficients are taken from the real Blume-Capel free
energy -- every order present, the model choosing c4 and c6, not the experimenter
-- by sweeping the crystal-field parameter a on the second-order side.

Pure numpy, deterministic.  ~6 min.
"""

import json

import numpy as np

C_CUT = 45.0
DELTA = 0.10
MID = 0.5 * (0.5 + 2.0 / 3.0)          # midpoint of the p=4 and p=6 exponents


# --- closed forms, verified against D1's numerical Taylor check ------------
def c4_of(a):
    return (a**2 / 8.0 - a / 24.0) / a**3


def c6_of(a):
    return (a**2 / 48.0 - a / 720.0 - a**3 / 24.0) / a**5


# --- Blume-Capel leg, T parameterised directly ----------------------------
def bc_leg(T, a):
    A = a / (1.0 - a)
    lh, base = np.log(0.5 * A), np.log(1.0 + A)
    phi = lambda m: 0.5 * m**2 - T * (
        np.logaddexp(np.logaddexp(0.0, lh + m / T), lh - m / T) - base)
    return phi, 1.0 - a / T


def _limit(phi, D, direction, width):
    target = C_CUT * D
    hi = direction * width
    for _ in range(300):
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


def rounding_ratio(phi, lam, D):
    width = np.sqrt(D / lam)
    hi = _limit(phi, D, +1.0, width)
    lo = _limit(phi, D, -1.0, width)
    n = int(np.clip(60.0 * (hi - lo) / width, 20001, 600001))
    y = np.linspace(lo, hi, n)
    p = phi(y)
    w = np.exp(-(p - p.min()) / D)
    z = np.trapezoid(w, y)
    m1 = np.trapezoid(y * w, y) / z
    m2 = np.trapezoid(y * y * w, y) / z
    return (m2 - m1 * m1) * lam / D


def crossover_lambda(a, D, eps_hi=1.0, eps_lo=1e-11, n_scan=90):
    """lambda at which |R-1| first reaches DELTA, scanning in from the harmonic end."""
    def dev(eps):
        phi, lam = bc_leg(a + eps, a)
        return abs(rounding_ratio(phi, lam, D) - 1.0)

    grid = np.logspace(np.log10(eps_hi), np.log10(eps_lo), n_scan)
    devs = np.array([dev(e) for e in grid])
    idx = np.flatnonzero(devs >= DELTA)
    if idx.size == 0 or idx[0] == 0:
        return None
    i = idx[0]
    lo, hi = np.log(grid[i]), np.log(grid[i - 1])
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if dev(np.exp(mid)) >= DELTA:
            lo = mid
        else:
            hi = mid
    _, lam = bc_leg(a + np.exp(0.5 * (lo + hi)), a)
    return lam


def D_crossover(a, d_grid):
    """Noise scale where the local log-log slope of lambda_c(D) crosses MID."""
    lam, Ds = [], []
    for D in d_grid:
        lc = crossover_lambda(a, D)
        if lc is not None:
            lam.append(lc)
            Ds.append(D)
    if len(Ds) < 8:
        return None, len(Ds)
    lD, ll = np.log(np.array(Ds)), np.log(np.array(lam))
    slope = np.gradient(ll, lD)
    # The slope RISES with D: small D is quartic-dominated (1/2), large D sextic
    # (2/3), per D1's P8 table.  An earlier version of this script looked for a
    # DOWNWARD crossing -- the same class of direction error P8 made the first
    # time -- and picked up spurious crossings in gradient noise, returning D_x
    # that FELL as c4 rose.  Left on record in the README.
    cross = np.flatnonzero((slope[:-1] < MID) & (slope[1:] >= MID))
    if cross.size == 0:
        return None, len(Ds)
    i = cross[0]
    t = (MID - slope[i]) / (slope[i + 1] - slope[i])
    return float(np.exp(lD[i] + t * (lD[i + 1] - lD[i]))), len(Ds)


def main():
    # capped at a = 0.36: D_x ~ c4^3/c6^2 grows ~7 decades across this window and
    # leaves the sweepable range above it.
    A_VALS = [0.3335, 0.3345, 0.3360, 0.3390, 0.3450, 0.3500, 0.3550, 0.3600]
    D_GRID = np.logspace(-11.0, -1.0, 41)

    rows = []
    for a in A_VALS:
        Dx, n = D_crossover(a, D_GRID)
        rows.append({"a": a, "delta_a": a - 1.0 / 3.0,
                     "c4": c4_of(a), "c6": c6_of(a),
                     "D_crossover": Dx, "n_points": n})
        tag = "n/a" if Dx is None else f"{Dx:.3e}"
        print(f"  a={a:.4f}  da={a-1/3:.2e}  c4={c4_of(a):.4e}  "
              f"c6={c6_of(a):.4e}  D_x={tag}")

    ok = [r for r in rows if r["D_crossover"] is not None]
    res = {"rows": rows, "n_usable": len(ok), "threshold": DELTA}

    if len(ok) >= 4:
        lc4 = np.log([r["c4"] for r in ok])
        lc6 = np.log([r["c6"] for r in ok])
        lDx = np.log([r["D_crossover"] for r in ok])
        M = np.vstack([lc4, lc6, np.ones_like(lc4)]).T
        coef, *_ = np.linalg.lstsq(M, lDx, rcond=None)
        resid = lDx - M @ coef
        res["two_variable_fit"] = {
            "alpha_on_c4": float(coef[0]), "predicted_alpha": 3.0,
            "beta_on_c6": float(coef[1]), "predicted_beta": -2.0,
            "const": float(coef[2]), "max_abs_log_resid": float(np.max(np.abs(resid))),
        }
        comp = np.array([r["D_crossover"] * r["c6"]**2 / r["c4"]**3 for r in ok])
        res["compensated"] = {
            "values": comp.tolist(),
            "ratio_max_over_min": float(comp.max() / comp.min()),
        }
        # P8R-3: the narrow window that reproduces the old one-variable result
        near = [r for r in ok if r["a"] <= 0.345]
        if len(near) >= 3:
            s = np.polyfit(np.log([r["delta_a"] for r in near]),
                           np.log([r["D_crossover"] for r in near]), 1)
            res["narrow_window_delta_a_exponent"] = float(s[0])
            res["narrow_window_n"] = len(near)

    with open("p8_verdict.json", "w") as f:
        json.dump(res, f, indent=2)

    print("\n" + "=" * 66)
    if "two_variable_fit" in res:
        t = res["two_variable_fit"]
        print(f"P8R-1  alpha on c4 = {t['alpha_on_c4']:+.3f}  (registered 3.00 +- 0.30)")
        print(f"       beta  on c6 = {t['beta_on_c6']:+.3f}  (registered -2.00 +- 0.40)")
        print(f"       max |log resid| = {t['max_abs_log_resid']:.3f}   n = {len(ok)}")
        print(f"P8R-2  D_x c6^2/c4^3 spans a factor of "
              f"{res['compensated']['ratio_max_over_min']:.2f}  (registered < 2.0)")
    if "narrow_window_delta_a_exponent" in res:
        print(f"P8R-3  narrow-window delta_a exponent = "
              f"{res['narrow_window_delta_a_exponent']:.3f}"
              f"  (registered 3.0 +- 0.4; post-hoc value was 3.211)")
    print("\nwrote p8_verdict.json")


if __name__ == "__main__":
    main()
