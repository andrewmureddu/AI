"""
D4 - do amplitudes transfer and bare exponents not?

D4 was filed from residue mining over this repo's own reported numbers, which
appeared to show dimensionless amplitudes transferring across domains (spreads of
a few percent, or exact) while exponents did not (factors of 3).  The stone flags
its own weakness: that evidence is retrospective and selection-prone.

This is the prospective version.  A fixed set of systems, a fixed set of
quantities, chosen before measuring, ALL reported -- and each quantity labelled on
two axes at once:

    kind   amplitude / exponent          <- D4's proposed variable
    chart  chart-free / chart-dependent  <- D2/D3's variable

The battery deliberately contains chart-free EXPONENTS and a chart-dependent
AMPLITUDE, so the two axes predict different things and exactly one can survive.

Comparison group: fold vs SIS -- same degeneracy order p=3 (same singularity),
different fields, different charts (k = 1/2 vs 1), different anharmonic
coefficients.  Control group: Ising vs Blume-Capel -- different p, where even the
chart-free quantities should differ.

Pure numpy, deterministic.  ~3 min.
"""

import json

import numpy as np

SEED = 20260727
C_CUT = 45.0
DELTA = 0.10


# --------------------------------------------------------------------------
# shared machinery (same forms as D1 / D2 / D6, so numbers are comparable)
# --------------------------------------------------------------------------

def fit_loglog(x, y):
    """slope and intercept of log y vs log x."""
    lx, ly = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    M = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(M, ly, rcond=None)
    return float(coef[0]), float(np.exp(coef[1]))


def bisect(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if (f(mid) < 0) == (flo < 0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _limit(phi, D, direction, width, bound):
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


def crossover(make_leg, D, eps_hi, eps_lo=1e-10, n_scan=110):
    def dev(e):
        phi, lam, ylo, yhi = make_leg(e)
        return abs(rounding_ratio(phi, lam, D, ylo, yhi) - 1.0)

    grid = np.logspace(np.log10(eps_hi), np.log10(eps_lo), n_scan)
    devs = np.array([dev(e) for e in grid])
    idx = np.flatnonzero(devs >= DELTA)
    if idx.size == 0 or idx[0] == 0:
        return None, None
    i = idx[0]
    lo, hi = np.log(grid[i]), np.log(grid[i - 1])
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        if dev(np.exp(mid)) >= DELTA:
            lo = mid
        else:
            hi = mid
    e = np.exp(0.5 * (lo + hi))
    _, lam, _, _ = make_leg(e)
    return lam, e


def tau_lambda(drift, lam, D, rng, n_rep=64, n_step=60000, steps_per_tau=100):
    dt = 1.0 / (lam * steps_per_tau)
    y = np.zeros(n_rep)
    s = np.sqrt(2.0 * D * dt)
    for _ in range(20 * steps_per_tau):
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
    nz = np.flatnonzero(acf <= 0.0)
    zero = nz[0] if nz.size else len(acf)
    return float((np.sum(acf[:zero]) - 0.5) * dt * lam)


# --------------------------------------------------------------------------
# the four systems
# --------------------------------------------------------------------------

def fold_leg(eps):
    lam = 2.0 * np.sqrt(eps)
    return (lambda y: 0.5 * lam * y**2 - y**3 / 3.0), lam, None, lam


def sis_leg(eps, beta=3.0):
    lam = beta * eps
    return (lambda y: 0.5 * lam * y**2 + beta * y**3 / 3.0), lam, -eps, 1.0 - eps


def ising_leg(eps):
    T = 1.0 + eps
    lam = 1.0 - 1.0 / T
    return (lambda m: 0.5 * m**2 - T * np.logaddexp(m / T, -m / T)
            + T * np.log(2.0)), lam, None, None


def bc_leg(T, a=1.0 / 3.0):
    # takes T directly, as in D1/D2/D6.  An earlier version took eps and added a
    # internally while the caller ALSO added 1/3, putting the leg at T = 2/3 + eps
    # -- far from the tricritical point, so no crossover was ever bracketed and
    # the empty fit silently returned 0.  The assert in measure() now catches it.
    A = a / (1.0 - a)
    lh, base = np.log(0.5 * A), np.log(1.0 + A)
    return (lambda m: 0.5 * m**2 - T * (
        np.logaddexp(np.logaddexp(0.0, lh + m / T), lh - m / T) - base)), \
        1.0 - a / T, None, None


# order parameter (below the transition) and curvature there
def fold_order(eps):
    return np.sqrt(eps), 2.0 * np.sqrt(eps)


def sis_order(eps, beta=3.0):
    return eps, beta * eps


def ising_order(eps):
    T = 1.0 - eps
    m = bisect(lambda x: x - np.tanh(x / T), 1e-16, 4.0)
    return m, 1.0 - (1.0 / T) / np.cosh(m / T) ** 2


def bc_order(eps, a=1.0 / 3.0):
    T = a - eps
    A = a / (1.0 - a)
    dphi = lambda m: m - A * np.sinh(m / T) / (1.0 + A * np.cosh(m / T))
    m = bisect(dphi, 1e-16, 4.0)
    C, Dn = np.cosh(m / T), 1.0 + A * np.cosh(m / T)
    return m, 1.0 - (A / T) * (C + A) / Dn**2


SYSTEMS = [
    dict(name="fold", field="ecology / dyn. sys.", p=3,
         leg=fold_leg, order=fold_order, eps_hi=1.0,
         eps_ord=np.logspace(-10, -6, 13),
         drift=lambda y: -(1.0 * y - y**2), tau_lam=1.0, tau_D=5e-3),
    dict(name="sis", field="epidemiology", p=3,
         leg=sis_leg, order=sis_order, eps_hi=0.2,
         eps_ord=np.logspace(-10, -6, 13),
         drift=lambda y: -(0.9 * y + 3.0 * y**2), tau_lam=0.9, tau_D=5e-4),
    dict(name="ising", field="physics", p=4,
         leg=ising_leg, order=ising_order, eps_hi=1.0,
         eps_ord=np.logspace(-9, -5, 13),
         drift=lambda m: -(m - np.tanh(m / 1.3)), tau_lam=1.0 - 1.0 / 1.3,
         tau_D=2e-3),
    dict(name="blume_capel", field="physics", p=6,
         leg=lambda e: bc_leg(1.0 / 3.0 + e), order=bc_order, eps_hi=1.0,
         eps_ord=np.logspace(-9, -5, 13),
         drift=lambda m: -(m - 0.5 * np.sinh(m / 0.5)
                           / (1.0 + 0.5 * np.cosh(m / 0.5))),
         tau_lam=1.0 - (1.0 / 3.0) / 0.5, tau_D=2e-3),
]

# label fixed in PREREGISTRATION.md, before any measurement
LABELS = {
    "Q1_k":            ("exponent",  "dependent"),
    "Q2_beta":         ("exponent",  "dependent"),
    "Q3_beta_over_k":  ("exponent",  "free"),
    "Q4_bare_cross":   ("exponent",  "dependent"),
    "Q5_lam_cross":    ("exponent",  "free"),
    "Q6_prefactor":    ("amplitude", "dependent"),
    "Q7_tau_lambda":   ("amplitude", "free"),
}

D_GRID = np.logspace(-8.0, -4.0, 9)


def measure(sysd, rng):
    out = {"system": sysd["name"], "field": sysd["field"], "p": sysd["p"]}

    eps = sysd["eps_ord"]
    ms, lams = zip(*[sysd["order"](e) for e in eps])
    beta, _ = fit_loglog(eps, np.array(ms))
    k, _ = fit_loglog(eps, np.array(lams))
    out["Q1_k"] = k
    out["Q2_beta"] = beta
    out["Q3_beta_over_k"] = beta / k

    lam_c, eps_c, Ds = [], [], []
    for D in D_GRID:
        lc, ec = crossover(sysd["leg"], D, sysd["eps_hi"])
        if lc is not None:
            lam_c.append(lc)
            eps_c.append(ec)
            Ds.append(D)
    assert len(Ds) >= 5, (f"{sysd['name']}: only {len(Ds)}/{len(D_GRID)} crossovers "
                          "bracketed — refusing to fit a degenerate set")
    th_lam, C = fit_loglog(Ds, lam_c)
    th_eps, _ = fit_loglog(Ds, eps_c)
    out["Q4_bare_cross"] = th_eps
    out["Q5_lam_cross"] = th_lam
    out["Q6_prefactor"] = C
    out["Q7_tau_lambda"] = tau_lambda(sysd["drift"], sysd["tau_lam"],
                                      sysd["tau_D"], rng)
    return out


def rel_spread(a, b):
    return abs(a - b) / (0.5 * (abs(a) + abs(b)) + 1e-300)


def main():
    rng = np.random.default_rng(SEED)
    rows = [measure(s, rng) for s in SYSTEMS]
    res = {"seed": SEED, "labels": {k: {"kind": v[0], "chart": v[1]}
                                    for k, v in LABELS.items()},
           "systems": rows}

    by = {r["system"]: r for r in rows}
    pairs = {
        "comparison_fold_vs_sis": ("fold", "sis"),
        "control_ising_vs_blume_capel": ("ising", "blume_capel"),
    }
    for pname, (a, b) in pairs.items():
        res[pname] = {q: {"a": by[a][q], "b": by[b][q],
                          "rel_spread": rel_spread(by[a][q], by[b][q]),
                          "kind": LABELS[q][0], "chart": LABELS[q][1]}
                      for q in LABELS}

    # P4: does either axis separate transfer from failure?
    cmp_ = res["comparison_fold_vs_sis"]
    grp = {}
    for axis in ("kind", "chart"):
        vals = {}
        for q, d in cmp_.items():
            vals.setdefault(d[axis], []).append(d["rel_spread"])
        grp[axis] = {g: {"n": len(v), "min": min(v), "max": max(v)}
                     for g, v in vals.items()}
        # separation = does every member of one group beat every member of the other?
        gs = list(vals)
        if len(gs) == 2:
            lo, hi = sorted(gs, key=lambda g: max(vals[g]))
            grp[axis]["separates"] = bool(max(vals[lo]) < min(vals[hi]))
            grp[axis]["gap"] = float(min(vals[hi]) - max(vals[lo]))
    res["separation"] = grp

    with open("verdict.json", "w") as f:
        json.dump(res, f, indent=2)

    print("=" * 78)
    print("D4 - do amplitudes transfer and bare exponents not?")
    print("=" * 78)
    print(f"\n{'system':14s} {'field':22s} {'p':>2s}  " +
          "  ".join(f"{q.split('_',1)[0]:>8s}" for q in LABELS))
    for r in rows:
        print(f"{r['system']:14s} {r['field']:22s} {r['p']:2d}  " +
              "  ".join(f"{r[q]:8.4f}" for q in LABELS))

    for pname, (a, b) in pairs.items():
        print(f"\n{pname}  ({a} vs {b})")
        print(f"  {'quantity':18s} {'kind':10s} {'chart':10s} "
              f"{a:>10s} {b:>10s} {'rel spread':>11s}")
        for q, d in res[pname].items():
            print(f"  {q:18s} {d['kind']:10s} {d['chart']:10s} "
                  f"{d['a']:10.4f} {d['b']:10.4f} {d['rel_spread']*100:10.1f}%")

    print("\nP4 - which axis separates transfer from failure? (comparison pair)")
    for axis, g in res["separation"].items():
        print(f"  by {axis}:")
        for name, v in g.items():
            if isinstance(v, dict):
                print(f"     {name:10s} n={v['n']}  spread range "
                      f"{v['min']*100:6.1f}% .. {v['max']*100:7.1f}%")
        print(f"     -> separates cleanly: {g.get('separates')}")

    print("\nwrote verdict.json")


if __name__ == "__main__":
    main()
