"""D9 — does chart-invariance predict transfer when the chart is UNPINNED?

Registered in PREREGISTRATION.md, committed before this file produced numbers.
D3 answered no on a harness whose chart is a count, pinned by additivity. This
asks the same question where the control is a distance-to-threshold, so that
G_pow is genuinely available and every domain supplies its own coordinate.

Transfer is read from distribution SHAPE; the residue from scaling EXPONENTS.
Different quantities, so the comparison is not circular.

numpy + stdlib only. Deterministic, quadrature only -- no sampling. ~1 min.
"""

import json
import math

import numpy as np

SEED = 20260728
OUT = {}

# Domains, fixed in the registration section 3 and NOT tuned.
DOMAINS = {
    "A":  dict(p=4, ap=1.0, c3=0.20, c4=0.05, chart=1.0),
    "L4": dict(p=4, ap=3.0, c3=-0.40, c4=0.90, chart=2.0),
    "L3": dict(p=4, ap=1.5, c3=0.10, c4=0.02, chart=0.6),
    "L2": dict(p=6, ap=1.0, c3=0.20, c4=0.05, chart=1.3),
    "L1": dict(p=None, ap=1.0, c3=0.0, c4=0.0, chart=1.0),   # no singularity
}
RUNGS = ["L4", "L3", "L2", "L1"]
GRID = np.linspace(0.02, 0.98, 97)

_GL = {}


def gl(k):
    if k not in _GL:
        _GL[k] = np.polynomial.legendre.leggauss(k)
    return _GL[k]


# ------------------------------------------------------------ potentials

def phi_sym(y, d):
    """Symmetric potential, eps = 0: the shape at the singularity."""
    if d["p"] is None:                       # L1: an ordinary quadratic well
        return 0.5 * d["ap"] * y**2
    a = np.abs(y)
    return (d["ap"] * a ** d["p"] / d["p"]
            + d["c3"] * a ** (d["p"] + 1)
            + d["c4"] * a ** (d["p"] + 2))


def dphi(y, d, eps, m):
    """m-th derivative of the one-sided potential with the control term."""
    if d["p"] is None:
        terms = {2: 0.5 * d["ap"], 1: -eps}
    else:
        terms = {d["p"]: d["ap"] / d["p"], d["p"] + 1: d["c3"],
                 d["p"] + 2: d["c4"], 1: -eps}
    tot = 0.0
    for j, c in terms.items():
        if j >= m:
            f = 1.0
            for i in range(m):
                f *= j - i
            tot += c * f * y ** (j - m)
    return tot


def y_star(d, eps):
    lo, hi = -40.0, 20.0
    f = lambda u: dphi(math.exp(u), d, eps, 1)
    flo = f(lo)
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if (f(mid) < 0) == (flo < 0):
            lo = mid
        else:
            hi = mid
    return math.exp(0.5 * (lo + hi))


# ----------------------------------------------- transfer: the law's SHAPE

def shape_curve(d, nodes=4000, reach=12.0):
    """Standardized quantile curve of the fluctuation density at eps = 0.

    Same robust standardization (median, IQR) and same quantile band as the
    ladder-vs-transfer harness, so the numbers are comparable to D3's.
    """
    # scale at which Phi/D is order 1
    if d["p"] is None:
        s = 1.0
    else:
        s = (d["p"] / d["ap"]) ** (1.0 / d["p"])
    x, w = gl(nodes)
    y = reach * s * x
    jac = reach * s * w
    e = phi_sym(y, d)
    rho = np.exp(-(e - e.min())) * jac
    cdf = np.cumsum(rho)
    cdf /= cdf[-1]
    qs = np.interp([0.25, 0.5, 0.75], cdf, y)
    iqr = qs[2] - qs[0]
    return (np.interp(GRID, cdf, y) - qs[1]) / (iqr + 1e-300)


def w1(a, b):
    return float(np.mean(np.abs(a - b)))


# ------------------------------------------- residue: the SCALING exponents

OBS = ["y_star", "lambda", "Var", "dPhi", "Phi3"]


def observables(d, eps):
    ys = y_star(d, eps)
    lam = dphi(ys, d, eps, 2)
    D = 1e-9 * lam * ys**2
    top = (d["p"] + 3) if d["p"] else 3
    dv = [dphi(ys, d, eps, m) / math.factorial(m) for m in range(1, top)]
    wdt = 8.0 * math.sqrt(D / lam)
    x, wq = gl(400)
    dl = wdt * x
    delta = np.zeros_like(dl)
    for m, c in enumerate(dv, start=1):
        delta += c * dl**m
    rho = np.exp(-(delta - delta.min()) / D) * wq
    z = rho.sum()
    m1 = (dl * rho).sum() / z
    var = (dl**2 * rho).sum() / z - m1**2
    return np.array([ys, lam, var, abs(dphi(ys, d, eps, 0)),
                     abs(dphi(ys, d, eps, 3))])


def slope_vector(d, window, nodes=25, rechart=1.0):
    """y_i = d ln O_i / d ln delta, where delta is the DOMAIN'S OWN chart.

    eps = delta^(c*rechart): c is the domain's coordinate choice, rechart is
    the extra G_pow relabelling used by P4.
    """
    delta = np.logspace(window[0], window[1], nodes)
    eps = delta ** (d["chart"] * rechart)
    O = np.array([observables(d, e) for e in eps])
    ld = np.log(delta)
    A = np.vstack([ld, np.ones_like(ld)]).T
    return np.array([np.linalg.lstsq(A, np.log(O[:, k]), rcond=None)[0][0]
                     for k in range(O.shape[1])])


def subspace_sine(a, b):
    """sin of the angle between two rays. Never arccos -- see D8's P1."""
    u = a / np.linalg.norm(a)
    v = b / np.linalg.norm(b)
    return float(np.linalg.norm(v - u * (u @ v)))


def is_zero_ray(y, tol=0.02):
    return bool(np.max(np.abs(y)) < tol)

def degenerate_observables(d, eps=1e-8):
    """Observables that are identically zero, whose log-slope is undefined.

    L1 has no anharmonicity at all, so its third derivative is exactly 0 --
    which is the signature of "no singularity" rather than a numerical
    problem, and is reported instead of a nan.
    """
    O = observables(d, eps)
    return [OBS[i] for i in range(len(OBS)) if abs(O[i]) < 1e-300]


# ----------------------------------------------------------------- main

WINDOWS = [(-9, -7), (-11, -9), (-8, -6)]

if __name__ == "__main__":
    OUT["seed"] = SEED

    # ---- P2 (first half): transfer from distribution shape
    print("shape / transfer ...", flush=True)
    qA = shape_curve(DOMAINS["A"])
    q_ref = shape_curve(dict(p=1, ap=1.0, c3=0.0, c4=0.0, chart=1.0))  # Laplace
    d_ref = w1(qA, q_ref)
    skill = {}
    for r in RUNGS:
        skill[r] = max(0.0, 1.0 - w1(qA, shape_curve(DOMAINS[r])) / d_ref)
    OUT["P2_transfer"] = {"skill": skill, "reference_distance": d_ref}

    # ---- P1: residue distances, across every window and both resolutions
    print("residue ...", flush=True)
    per_setting = []
    for wi, win in enumerate(WINDOWS):
        for nodes in (25, 41):
            deg = {k: degenerate_observables(DOMAINS[k]) for k in DOMAINS}
            ys = {k: slope_vector(DOMAINS[k], win, nodes) for k in DOMAINS}
            row = {"window": f"1e{win[0]}..1e{win[1]}", "nodes": nodes,
                   "dist": {}, "zero_ray": {}, "degenerate": deg}
            for r in RUNGS:
                row["zero_ray"][r] = is_zero_ray(ys[r])
                if deg[r] or row["zero_ray"][r]:
                    row["dist"][r] = None          # undefined, not zero
                else:
                    row["dist"][r] = subspace_sine(ys["A"], ys[r])
            row["slopes"] = {k: ys[k].tolist() for k in DOMAINS}
            per_setting.append(row)
    base = per_setting[0]
    OUT["P1_residue"] = {
        "observables": OBS,
        "settings": per_setting,
        "base_distances": base["dist"],
        "zero_ray": base["zero_ray"],
    }

    # ---- P2 (second half): is the ordering STABLE? -- the registered bar
    def ordered(row):
        """Same-class rungs closer to A than the different-class one.

        L1 is excluded: its residue is UNDEFINED (one observable is
        identically zero), which is a stronger separation than any distance
        and is reported on its own rather than folded into an ordering.
        """
        d = row["dist"]
        if d["L2"] is None or d["L4"] is None or d["L3"] is None:
            return False
        return bool(max(d["L4"], d["L3"]) < d["L2"])

    stable = [ordered(r) for r in per_setting]
    OUT["P2_transfer"]["residue_orders_transfer"] = ordered(base)
    OUT["P2_transfer"]["ordering_stable_across_settings"] = bool(all(stable))
    OUT["P2_transfer"]["per_setting_ordered"] = stable

    # ---- P3: the contrast with D3 -- does the bare exponent order transfer?
    bare_k = {k: base["slopes"][k][1] for k in DOMAINS}      # lambda's slope
    same_class = ["A", "L4", "L3"]
    kk = [abs(bare_k[k]) for k in same_class]
    bare_dist = {r: abs(abs(bare_k[r]) - abs(bare_k["A"])) for r in RUNGS}
    OUT["P3_contrast"] = {
        "bare_k": bare_k,
        "same_class_spread_factor": max(kk) / min(kk),
        "bare_exponent_distance_from_A": bare_dist,
        "bare_orders_transfer": bool(
            max(bare_dist["L4"], bare_dist["L3"]) < bare_dist["L2"]),
        "d3_same_class_spread_factor": 0.5023 / 0.4960,
        "d3_bare_ordered_transfer": True,
        "d3_residue_ordering_stable": False,
    }

    # ---- P4: re-charting invariance (DECLARED, not evidence)
    print("re-charting ...", flush=True)
    rec = []
    for a in (0.5, 1.0, 2.0, 3.0):
        yA = slope_vector(DOMAINS["A"], WINDOWS[0], 25, rechart=a)
        rec.append({"a": a, "bare_k": yA[1],
                    "residue_shift": subspace_sine(
                        slope_vector(DOMAINS["A"], WINDOWS[0], 25), yA)})
    OUT["P4_recharting_declared"] = {
        "_note": "declared not evidence; D7 established this and D1 measured it",
        "rows": rec,
        "max_residue_shift": max(r["residue_shift"] for r in rec),
        "bare_k_span": max(abs(r["bare_k"]) for r in rec)
        / min(abs(r["bare_k"]) for r in rec),
    }

    # ---- POST-HOC DIAGNOSTIC (not registered)
    # The registered transfer thresholds (L2 and L1 below 0.40) were missed
    # badly. Either the claim is wrong or the readout has no dynamic range in
    # this family. Excess kurtosis decides it: it is the standardized shape in
    # one number, so if p = 4 and p = 6 differ by very little then the "law"
    # barely depends on the class and the transfer test cannot carry a claim.
    print("diagnostic (post-hoc) ...", flush=True)

    def excess_kurtosis(d, nodes=4000, reach=12.0):
        s_ = 1.0 if d["p"] is None else (d["p"] / d["ap"]) ** (1.0 / d["p"])
        x, w = gl(nodes)
        y = reach * s_ * x
        jac = reach * s_ * w
        e = phi_sym(y, d)
        rho = np.exp(-(e - e.min())) * jac
        z = rho.sum()
        m2 = (y**2 * rho).sum() / z
        m4 = (y**4 * rho).sum() / z
        return m4 / m2**2 - 3.0

    kurt = {k: excess_kurtosis(DOMAINS[k]) for k in DOMAINS}
    kurt["ref_Laplace"] = excess_kurtosis(
        dict(p=1, ap=1.0, c3=0.0, c4=0.0, chart=1.0))
    raw = {r: w1(qA, shape_curve(DOMAINS[r])) for r in RUNGS}
    OUT["POSTHOC_readout_dynamic_range"] = {
        "_note": "not registered; asks whether the missed transfer thresholds "
                 "mean the claim is wrong or the readout has no dynamic range "
                 "in this family. Never counted as a pass.",
        "excess_kurtosis": kurt,
        "raw_shape_distance_from_A": raw,
        "reference_distance": d_ref,
        "spread_among_singular_rungs":
            max(raw[r] for r in ("L4", "L3", "L2"))
            - min(raw[r] for r in ("L4", "L3", "L2")),
    }

    # What readout WOULD separate adjacent degeneracies? The class lives in
    # the tail exponent of exp(-a|y|^p/pD), so a far-quantile ratio should see
    # it where a kurtosis does not. Measured to make the next registration
    # concrete; explicitly NOT a result of this experiment.
    def tail_ratio(d, hi=0.995, lo=0.75):
        c = shape_curve(d, nodes=8000, reach=16.0)
        return float(np.interp(hi, GRID, c) / np.interp(lo, GRID, c))

    tr = {k: tail_ratio(DOMAINS[k]) for k in DOMAINS}
    OUT["POSTHOC_readout_dynamic_range"]["tail_ratio_q995_over_q75"] = tr
    OUT["POSTHOC_readout_dynamic_range"]["tail_ratio_separation_p4_vs_p6"] = {
        "p4_spread": max(tr[k] for k in ("A", "L4", "L3"))
                     - min(tr[k] for k in ("A", "L4", "L3")),
        "p4_to_p6_gap": abs(np.mean([tr[k] for k in ("A", "L4", "L3")]) - tr["L2"]),
    }

    with open("verdict.json", "w") as f:
        json.dump(OUT, f, indent=2)

    print("\n--- summary ---")
    print(f"P2  transfer skill: " + ", ".join(
        f"{r}={skill[r]:.3f}" for r in RUNGS))
    def fmt(row, r):
        if row["degenerate"][r]:
            return f"{r}=UNDEFINED({','.join(row['degenerate'][r])}=0)"
        if row["dist"][r] is None:
            return f"{r}=ZERO RAY"
        return f"{r}={row['dist'][r]:.4f}"

    print("P1  residue distance from A: " + ", ".join(
        fmt(base, r) for r in RUNGS))
    print("    across settings:")
    for row in per_setting:
        print(f"      {row['window']} nodes={row['nodes']}: " + ", ".join(
            fmt(row, r) for r in RUNGS) + f"   ordered={ordered(row)}")
    print(f"P2  ordering stable across all settings? "
          f"{OUT['P2_transfer']['ordering_stable_across_settings']}")
    p3 = OUT["P3_contrast"]
    print(f"P3  bare k: " + ", ".join(f"{k}={v:.4f}" for k, v in bare_k.items()))
    print(f"    same-class spread {p3['same_class_spread_factor']:.2f}x "
          f"(D3's was {p3['d3_same_class_spread_factor']:.4f}x)")
    print(f"    bare exponent orders transfer here? {p3['bare_orders_transfer']} "
          f"(in D3: {p3['d3_bare_ordered_transfer']})")
    dg = OUT["POSTHOC_readout_dynamic_range"]
    print("\n--- post-hoc diagnostic (not registered) ---")
    print("  excess kurtosis: " + ", ".join(
        f"{k}={v:.4f}" for k, v in dg["excess_kurtosis"].items()))
    print("  raw shape dist from A: " + ", ".join(
        f"{k}={v:.4f}" for k, v in dg["raw_shape_distance_from_A"].items())
        + f"   (reference {dg['reference_distance']:.4f})")
    print("  tail ratio q99.5/q75: " + ", ".join(
        f"{k}={v:.4f}" for k, v in dg["tail_ratio_q995_over_q75"].items()))
    ts = dg["tail_ratio_separation_p4_vs_p6"]
    print(f"    within-p4 spread {ts['p4_spread']:.4f} vs p4->p6 gap "
          f"{ts['p4_to_p6_gap']:.4f}")
    p4 = OUT["P4_recharting_declared"]
    print(f"P4  residue shift under re-charting {p4['max_residue_shift']:.2e}, "
          f"bare k span {p4['bare_k_span']:.2f}x  (declared, not evidence)")
