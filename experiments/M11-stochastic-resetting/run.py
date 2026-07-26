"""M11 -- is stochastic resetting one mechanism across three fields?

Diffusive search (Evans-Majumdar 2011), enzymatic turnover (Reuveni-Urbakh-
Klafter 2014: substrate unbinding IS restart), and randomized backtracking
search (Luby et al. 1993; Gomes-Selman-Kautz 1998) each independently
discovered that restarting a stalled search helps.  M11 asks whether it is the
SAME mechanism, which is a question about whether one parameter-free criterion
governs all three:

    restart helps  <=>  CV = sigma_T / <T>  >  1
    and at the optimum,  CV(T_r*) = 1  exactly, whatever the process.

Predictions registered in PREREGISTRATION.md BEFORE this was run:
  P1 sign flip at CV=1, crossing located at lognormal sigma*=sqrt(ln2)
  P2 exponential knife edge: <T_r> independent of r
  P3 diffusion: r* x0^2/D = 2.5396
  P4 parameter transfer: curve predicted from un-reset distribution alone, 3%
  P5 CV(T_r*) = 1 in all three domains          <- the identity test
  P6 Michaelis-Menten sign flip within one scheme
  P7 SAT: CV>1 and predicted speedup
  P8 the whole theory is the CGF of the completion time  (the Phi question)

Pure numpy, deterministic seeds.  ~3 minutes (the SAT pool dominates).
"""
import json
import math
import zlib

import numpy as np

MASTER = np.random.default_rng(11)
NTRIAL = 100_000          # trajectories per restart-rate evaluation (main domains)
NBATT = 60_000            # trajectories for the wide battery
NSIG = 4.0                # sigmas of improvement required to call 'restart helps'
RGRID = 21                # points per restart-rate sweep
GUARD = 4000              # max restart rounds before a rate is marked uncomputable
LMIN = 0.02               # only simulate rates where P(finish before reset) >= this


# ---------------------------------------------------------------------------
# theory harness
# ---------------------------------------------------------------------------
def cv_of(T):
    T = np.asarray(T, dtype=float)
    return float(T.std() / T.mean())


def predicted_curve(T_samples, rs):
    """<T_r> = (1 - Ltilde(r)) / (r Ltilde(r)), Ltilde from the UN-RESET samples.

    Uses only the un-reset completion-time distribution -- no information from
    the restarted process.  Works even when <T> = inf, since Ltilde exists when
    moments do not.
    """
    T = np.asarray(T_samples, dtype=float)
    out = []
    for r in rs:
        if r <= 0:
            out.append(float(T.mean()))
            continue
        L = float(np.mean(np.exp(-r * T)))
        out.append((1.0 - L) / (r * L) if L > 0 else float("inf"))
    return np.array(out)


def simulate_restart(sampler, r, n, rng):
    """Actually run the restart protocol.  Returns completion times.

    Restart returns the process to its initial condition, so each attempt is a
    fresh draw -- this is the definition of the protocol, not an approximation.
    """
    if r <= 0:
        return sampler(n, rng)
    total = np.zeros(n)
    active = np.ones(n, dtype=bool)
    guard = 0
    while active.any() and guard < GUARD:
        k = int(active.sum())
        T = sampler(k, rng)
        R = rng.exponential(1.0 / r, size=k)
        done = T < R
        idx = np.flatnonzero(active)
        total[idx] += np.where(done, T, R)
        active[idx[done]] = False
        guard += 1
    if active.any():          # rate too high to complete -- not a usable point
        return None
    return total


def rate_grid(T_samples, n_points=RGRID, lmin=LMIN):
    """Log grid of restart rates, bounded above by where the protocol still
    completes: keep only r with Ltilde(r) = E[e^{-rT}] >= lmin, so the expected
    number of restarts stays ~1/lmin.  Uses the un-reset samples only."""
    T = np.asarray(T_samples, dtype=float)
    scale = float(np.median(T))
    probe = np.logspace(-4, 3, 200) / scale
    ok = [r for r in probe if float(np.mean(np.exp(-r * T))) >= lmin]
    r_max = max(ok) if ok else 1.0 / scale
    return np.concatenate([[0.0], np.logspace(math.log10(r_max) - 3.0,
                                              math.log10(r_max), n_points - 1)])


def bootstrap_ratio_lo(a, b, seed, B=300, pct=1.0):
    """Lower percentile of the bootstrap distribution of mean(a)/mean(b).

    Robust where a normal standard error is not: it needs no finite variance,
    only that resampling reproduces the sampling distribution of the mean.
    """
    rng = np.random.default_rng(seed + 555)
    na, nb = len(a), len(b)
    ratios = np.empty(B)
    for t in range(B):
        ratios[t] = (a[rng.integers(0, na, na)].mean()
                     / b[rng.integers(0, nb, nb)].mean())
    return float(np.percentile(ratios, pct))


def initial_slope_norm(rs, means):
    """d<T_r>/dr at r=0, normalised by <T>^2.

    Theory: the slope is <T>^2 - <T^2>/2 = <T>^2 (1 - CV^2)/2, so the
    normalised slope should equal (1 - CV^2)/2 -- a SIGNED, quantitative
    prediction spanning both sides of the criterion, far stronger than a
    sign test and not limited by the power of a significance threshold.
    Meaningless where <T> = inf; the caller filters those.
    """
    rs = np.asarray(rs, dtype=float)
    m = np.asarray(means, dtype=float)
    ok = np.isfinite(m) & (rs <= rs[np.isfinite(m)].max() * 1e-2)
    if ok.sum() < 3 or not np.isfinite(m[0]) or m[0] <= 0:
        return float("nan")
    slope = float(np.polyfit(rs[ok], m[ok], 1)[0])
    return slope / (m[0] ** 2)


def sweep(sampler, rs, n, seed, label=""):
    """Simulate the restarted process across a grid of rates; find the optimum.

    Two things matter for the decision rule and both were got wrong first time:

    * COMMON RANDOM NUMBERS -- every rate is simulated from the same seed, so
      the first attempt of every trajectory is the *same* draw across rates.
      Noise is then shared and differences between rates are far sharper than
      the individual means.
    * SIGNIFICANCE -- taking argmin over a grid of noisy means is BIASED toward
      "restart helps": the minimum of k noisy values sits ~2 standard errors
      low even when the true curve is flat.  So "helps" requires the best rate
      to beat r=0 by NSIG combined standard errors, not merely to be lower.
    """
    means, sems, cvs, samples = [], [], [], {}
    for j, r in enumerate(rs):
        Tr = simulate_restart(sampler, r, n, np.random.default_rng(seed))
        if Tr is None:
            means.append(float("nan"))
            sems.append(float("nan"))
            cvs.append(float("nan"))
            continue
        means.append(float(Tr.mean()))
        sems.append(float(Tr.std() / math.sqrt(len(Tr))))
        cvs.append(float(Tr.std() / Tr.mean()))
        samples[j] = Tr
    means, sems, cvs = np.array(means), np.array(sems), np.array(cvs)
    valid = np.isfinite(means)
    i = int(np.flatnonzero(valid)[np.argmin(means[valid])])
    # A normal standard error is meaningless when the baseline has infinite
    # variance (the Levy case: a 5985x speedup scored 3.8 sigma).  Bootstrap
    # the RATIO instead and require its lower percentile to exceed 1.
    lo_ratio = bootstrap_ratio_lo(samples[0], samples[i], seed)
    helps = bool(i > 0 and lo_ratio > 1.0)
    gap = means[0] - means[i]
    return {"label": label, "rs": rs.tolist(), "means": means.tolist(),
            "sems": sems.tolist(), "cvs": cvs.tolist(),
            "i_opt": i if helps else 0,
            "r_opt": float(rs[i]) if helps else 0.0,
            "mean_at_opt": float(means[i]), "cv_at_opt": float(cvs[i]),
            "mean_at_r0": float(means[0]),
            "speedup": float(means[0] / means[i]),
            "bootstrap_ratio_lo": float(lo_ratio),
            "improvement_over_sigma": float(
                gap / max(math.sqrt(sems[0] ** 2 + sems[i] ** 2), 1e-300)),
            "initial_slope_norm": initial_slope_norm(rs, means),
            "n_rates_uncomputable": int((~valid).sum()),
            "helps": helps}


# ---------------------------------------------------------------------------
# samplers -- each returns n iid un-reset completion times
# ---------------------------------------------------------------------------
def s_exponential(n, rng, rate=1.0):
    return rng.exponential(1.0 / rate, size=n)


def s_erlang(k):
    def f(n, rng):                      # mean 1, CV = 1/sqrt(k)
        return rng.gamma(shape=k, scale=1.0 / k, size=n)
    return f


def s_uniform(n, rng):                  # CV = 1/sqrt(3)
    return rng.uniform(0.0, 2.0, size=n)


def s_lognormal(sig):
    def f(n, rng):                      # CV = sqrt(exp(sig^2)-1)
        return rng.lognormal(mean=0.0, sigma=sig, size=n)
    return f


def s_pareto(alpha):
    def f(n, rng):                      # CV finite for alpha > 2
        return (1.0 + rng.pareto(alpha, size=n))
    return f


def s_levy(x0=1.0, D=1.0):
    """1D diffusion first passage: T = x0^2 / (2 D Z^2), Z ~ N(0,1).  <T> = inf."""
    def f(n, rng):
        z = rng.normal(size=n)
        z = np.where(np.abs(z) < 1e-8, 1e-8, z)
        return x0 * x0 / (2.0 * D * z * z)
    return f


def s_mm_multistep(k=4, kcat=1.0):
    """Catalysis through k sequential sub-steps: Erlang, CV = 1/sqrt(k) < 1."""
    def f(n, rng):
        return rng.gamma(shape=k, scale=1.0 / (k * kcat), size=n)
    return f


def s_mm_disorder(p=0.5, k_fast=10.0, k_slow=0.1):
    """Dynamic disorder: conformer drawn at binding.  Broad => CV > 1."""
    def f(n, rng):
        fast = rng.random(n) < p
        rates = np.where(fast, k_fast, k_slow)
        return rng.exponential(1.0, size=n) / rates
    return f


def pool_sampler(pool):
    def f(n, rng):
        return pool[rng.integers(0, len(pool), size=n)].astype(float)
    return f


out = {}

# ---------------------------------------------------------------------------
# P1 -- the sign flip, and where it sits
# ---------------------------------------------------------------------------
battery = [
    ("erlang k=16", s_erlang(16)), ("erlang k=8", s_erlang(8)),
    ("erlang k=4", s_erlang(4)), ("uniform", s_uniform),
    ("erlang k=2", s_erlang(2)), ("lognormal s=0.5", s_lognormal(0.5)),
    ("exponential", s_exponential), ("lognormal s=1.0", s_lognormal(1.0)),
    ("pareto a=2.5", s_pareto(2.5)), ("lognormal s=1.5", s_lognormal(1.5)),
    ("levy (diffusion)", s_levy()),
]
rows = []
for name, samp in battery:
    rng = np.random.default_rng(zlib.crc32(name.encode()))
    base = samp(NBATT * 5, rng)
    c = cv_of(base)
    rs = rate_grid(base)
    sw = sweep(samp, rs, NBATT, 7, label=name)
    rows.append({"process": name, "CV": c, "r_opt": sw["r_opt"],
                 "helps": sw["helps"], "speedup": sw["speedup"],
                 "improvement_over_sigma": sw["improvement_over_sigma"],
                 "bootstrap_ratio_lo": sw["bootstrap_ratio_lo"],
                 "slope_measured": sw["initial_slope_norm"],
                 "slope_predicted_(1-CV^2)/2": (1.0 - c * c) / 2.0,
                 "cv_at_opt": sw["cv_at_opt"],
                 "criterion_says_helps": bool(c > 1.0),
                 "agrees": bool(sw["helps"] == (c > 1.0))})
slope_ok = [r for r in rows if np.isfinite(r["slope_measured"]) and r["CV"] < 10]
slope_err = [abs(r["slope_measured"] - r["slope_predicted_(1-CV^2)/2"])
             for r in slope_ok]
near_edge = [r for r in rows if abs(r["CV"] - 1.0) < 0.06]
away = [r for r in rows if abs(r["CV"] - 1.0) >= 0.06]
out["P1_sign_flip"] = {
    "rows": rows,
    "misclassifications_away_from_edge": int(sum(not r["agrees"] for r in away)),
    "n_away_from_edge": len(away),
    "n_near_edge_excluded": len(near_edge),
    "confirmed": bool(sum(not r["agrees"] for r in away) == 0),
    "slope_test": {
        "n_processes": len(slope_ok),
        "median_abs_err": float(np.median(slope_err)) if slope_err else None,
        "max_abs_err_vs_(1-CV^2)/2": float(max(slope_err)) if slope_err else None,
        "resolvable_CV<=1.35": {
            "n": len([r for r in slope_ok if r["CV"] <= 1.35]),
            "max_abs_err": float(max(
                [abs(r["slope_measured"] - r["slope_predicted_(1-CV^2)/2"])
                 for r in slope_ok if r["CV"] <= 1.35])),
        },
        "broad_CV>1.35": {
            "n": len([r for r in slope_ok if r["CV"] > 1.35]),
            "note": ("the linear regime narrows as higher moments grow -- the "
                     "r^2 term carries <T^3> -- so a finite-r fit understates "
                     "|slope| for broad distributions.  Sign stays correct."),
        },
        "signs_all_correct": bool(all(
            (r["slope_measured"] < 0) == (r["CV"] > 1.0)
            for r in slope_ok if abs(r["CV"] - 1.0) >= 0.06)),
        "note": ("signed quantitative form of the criterion; excludes "
                 "infinite-variance processes where <T>^2 does not normalise"),
    },
}

# Locate the crossing by scanning lognormal width.  Thresholding SIGNIFICANCE
# finds where the effect becomes DETECTABLE, not where it changes sign, and so
# is biased late (it put the crossing at sigma=0.925 vs the predicted 0.833).
# The signed initial slope of the restart curve changes sign exactly at CV=1,
# so interpolate ITS zero instead -- more powerful and unbiased.
sig_scan = []
for sig in np.linspace(0.60, 1.10, 11):
    samp = s_lognormal(float(sig))
    base = samp(NBATT * 5, np.random.default_rng(4242))
    c = cv_of(base)
    rs = rate_grid(base, n_points=15)
    sw = sweep(samp, rs, NBATT, 99)
    sig_scan.append({"sigma": float(sig), "CV": c, "helps": sw["helps"],
                     "speedup": sw["speedup"],
                     "slope_measured": sw["initial_slope_norm"],
                     "slope_predicted": (1.0 - c * c) / 2.0})

sl = np.array([r["slope_measured"] for r in sig_scan])
sg = np.array([r["sigma"] for r in sig_scan])
cross = float("nan")
for i in range(len(sl) - 1):
    if np.isfinite(sl[i]) and np.isfinite(sl[i + 1]) and sl[i] > 0 >= sl[i + 1]:
        cross = float(sg[i] + (sg[i + 1] - sg[i]) * sl[i] / (sl[i] - sl[i + 1]))
        break
sig_star = math.sqrt(math.log(2))
# where the significance threshold would have put it, for comparison
helped = [r["sigma"] for r in sig_scan if r["helps"]]
not_helped = [r["sigma"] for r in sig_scan if not r["helps"]]
naive = ((max(not_helped) + min(helped)) / 2
         if helped and not_helped else float("nan"))
out["P1_crossing_location"] = {
    "scan": sig_scan,
    "crossing_from_slope_sign_change": cross,
    "crossing_from_significance_threshold_biased_late": naive,
    "predicted_sigma_star_sqrt_ln2": sig_star,
    "rel_err": abs(cross - sig_star) / sig_star,
    "confirmed": bool(abs(cross - sig_star) / sig_star < 0.05),
}

# ---------------------------------------------------------------------------
# P2 -- the exponential knife edge
# ---------------------------------------------------------------------------
rs = np.logspace(-1, 1, 9)
means = [float(simulate_restart(s_exponential, float(r), NTRIAL,
                                np.random.default_rng(5)).mean()) for r in rs]  # noqa
out["P2_exponential_knife_edge"] = {
    "rs": rs.tolist(), "means": means,
    "relative_spread": float((max(means) - min(means)) / np.mean(means)),
    "confirmed": bool((max(means) - min(means)) / np.mean(means) < 0.02),
}

# ---------------------------------------------------------------------------
# P3 -- diffusive search against its analytic optimum
# ---------------------------------------------------------------------------
x0, D = 1.0, 1.0
z_star = 1.5936                                   # root of z/2 = 1 - exp(-z)
r_star_theory = D * z_star**2 / x0**2
rs = np.linspace(0.3 * r_star_theory, 3.0 * r_star_theory, 60)
sw_diff = sweep(s_levy(x0, D), rs, NTRIAL, 21, "diffusion")
# parabolic refinement around the grid minimum
i = sw_diff["i_opt"]
if 0 < i < len(rs) - 1:
    y0_, y1_, y2_ = sw_diff["means"][i - 1:i + 2]
    denom = (y0_ - 2 * y1_ + y2_)
    shift = 0.5 * (y0_ - y2_) / denom if denom != 0 else 0.0
    r_star_sim = float(rs[i] + shift * (rs[1] - rs[0]))
else:
    r_star_sim = sw_diff["r_opt"]
out["P3_diffusion"] = {
    "r_star_theory_x0^2_over_D": r_star_theory,
    "r_star_simulated": r_star_sim,
    "rel_err": abs(r_star_sim - r_star_theory) / r_star_theory,
    "cv_at_opt": sw_diff["cv_at_opt"],
    "confirmed": bool(abs(r_star_sim - r_star_theory) / r_star_theory < 0.05),
}

# ---------------------------------------------------------------------------
# P6 -- Michaelis-Menten: same scheme, two regimes, opposite conclusions
# ---------------------------------------------------------------------------
mm = {}
for name, samp in (("multistep k=4", s_mm_multistep(4)),
                   ("dynamic disorder", s_mm_disorder())):
    rng = np.random.default_rng(31)
    base = samp(NTRIAL, rng)
    rs = rate_grid(base)
    sw = sweep(samp, rs, NTRIAL, 32, name)
    pred = predicted_curve(base, np.array(rs))
    finite = np.isfinite(pred) & (np.array(sw["means"]) > 0)
    mm[name] = {
        "CV": cv_of(base), "r_opt": sw["r_opt"], "helps": sw["helps"],
        "speedup": sw["speedup"], "cv_at_opt": sw["cv_at_opt"],
        "transfer_max_rel_err": float(np.max(np.abs(
            pred[finite] - np.array(sw["means"])[finite])
            / np.array(sw["means"])[finite])),
        "sweep": sw,
    }
out["P6_michaelis_menten"] = {
    "regimes": {k: {kk: vv for kk, vv in v.items() if kk != "sweep"}
                for k, v in mm.items()},
    "sign_flip_within_one_scheme": bool(
        mm["multistep k=4"]["helps"] is False
        and mm["dynamic disorder"]["helps"] is True),
}

# ---------------------------------------------------------------------------
# P7 -- randomized DPLL on a fixed satisfiable 3-SAT instance
# ---------------------------------------------------------------------------
def make_3sat(n, m, rng):
    cl = np.zeros((m, 3), dtype=np.int64)
    for i in range(m):
        v = rng.choice(n, size=3, replace=False) + 1
        s = rng.choice(np.array([-1, 1]), size=3)
        cl[i] = v * s
    return cl


def dpll(clauses, n, rng, max_nodes):
    """Backtracking search with unit propagation, random var/value order.

    Returns (sat, nodes).  `nodes` = decisions taken; the Las Vegas runtime.
    """
    assign = np.zeros(n + 1, dtype=np.int64)
    absl, sgn = np.abs(clauses), np.sign(clauses)
    nodes = [0]

    def propagate(trail):
        while True:
            vals = assign[absl] * sgn
            sat = (vals == 1).any(axis=1)
            nun = (vals == 0).sum(axis=1)
            if np.any((~sat) & (nun == 0)):
                return False
            unit = np.flatnonzero((~sat) & (nun == 1))
            if unit.size == 0:
                return True
            c = unit[0]
            j = int(np.flatnonzero(vals[c] == 0)[0])
            lit = int(clauses[c, j])
            assign[abs(lit)] = 1 if lit > 0 else -1
            trail.append(abs(lit))

    def search():
        if nodes[0] >= max_nodes:
            return None                      # censored
        trail = []
        if not propagate(trail):
            for v in trail:
                assign[v] = 0
            return False
        free = np.flatnonzero(assign[1:] == 0) + 1
        if free.size == 0:
            return True
        nodes[0] += 1
        var = int(rng.choice(free))
        first = int(rng.choice(np.array([1, -1])))
        for val in (first, -first):
            assign[var] = val
            res = search()
            if res is True:
                return True
            if res is None:
                return None
            assign[var] = 0
        for v in trail:
            assign[v] = 0
        return False

    res = search()
    return res, nodes[0]


def run_pool(solver, n_runs, cap, seed0=10_000):
    pool, censored = [], 0
    for k in range(n_runs):
        res, nd = solver(np.random.default_rng(seed0 + k), cap)
        if res is None:
            censored += 1
            nd = cap
        pool.append(max(nd, 1))
    return np.array(pool, dtype=float), censored


# --- (a) random 3-SAT at the phase transition: the EASY control -------------
N_VARS, RATIO = 50, 4.26
M_CL = int(RATIO * N_VARS)
gen = np.random.default_rng(2024)
instance, tries = None, 0
while instance is None and tries < 60:
    cand = make_3sat(N_VARS, M_CL, gen)
    sat, _ = dpll(cand, N_VARS, np.random.default_rng(1), 60_000)
    tries += 1
    if sat is True:
        instance = cand
pool_sat, cens_sat = run_pool(
    lambda rg, cap: dpll(instance, N_VARS, rg, cap), 150, 60_000)

samp_3sat = pool_sampler(pool_sat)
rs = rate_grid(pool_sat)
sw_3sat = sweep(samp_3sat, rs, NTRIAL // 2, 77, "3sat")

# --- (b) quasigroup-with-holes: the canonical HEAVY-TAILED benchmark --------
# Gomes-Selman 1997: randomized backtracking with MRV + random tie-breaking on
# QWH is where heavy-tailed runtime distributions were first characterised.
import sys
sys.setrecursionlimit(20_000)


def random_latin(N, rng):
    L = [[(i + j) % N for j in range(N)] for i in range(N)]
    rp, cp, sp = rng.permutation(N), rng.permutation(N), rng.permutation(N)
    return [[int(sp[L[int(rp[i])][int(cp[j])]]) for j in range(N)]
            for i in range(N)]


def make_qwh(N, holes_frac, rng):
    """A Latin square with holes punched -- satisfiable by construction."""
    grid = [r[:] for r in random_latin(N, rng)]
    cells = [(i, j) for i in range(N) for j in range(N)]
    rng.shuffle(cells)
    for (i, j) in cells[:int(holes_frac * N * N)]:
        grid[i][j] = -1
    return grid


def solve_qwh(grid, N, rng, max_nodes):
    """Backtracking, most-constrained-variable with RANDOMISED tie-breaking."""
    row, col, full, empt = [0] * N, [0] * N, (1 << N) - 1, []
    for i in range(N):
        for j in range(N):
            v = grid[i][j]
            if v >= 0:
                row[i] |= 1 << v
                col[j] |= 1 << v
            else:
                empt.append((i, j))
    empt, nodes = set(empt), [0]

    def rec():
        if not empt:
            return True
        if nodes[0] >= max_nodes:
            return None
        bestn, ties = 99, []
        for (i, j) in empt:
            c = full & ~(row[i] | col[j])
            n = bin(c).count("1")
            if n == 0:
                return False
            if n < bestn:
                bestn, ties = n, [(i, j)]
            elif n == bestn:
                ties.append((i, j))
        cell = ties[int(rng.integers(len(ties)))]
        i, j = cell
        vals = [v for v in range(N) if (full & ~(row[i] | col[j])) >> v & 1]
        rng.shuffle(vals)
        nodes[0] += 1
        empt.discard(cell)
        for v in vals:
            b = 1 << v
            row[i] |= b
            col[j] |= b
            r = rec()
            if r is True:
                return True
            if r is None:
                return None
            row[i] &= ~b
            col[j] &= ~b
        empt.add(cell)
        return False

    return rec(), nodes[0]


QN, QHOLES, QCAP = 14, 0.55, 100_000
qgrid = make_qwh(QN, QHOLES, np.random.default_rng(5))
pool_qwh, cens_qwh = run_pool(
    lambda rg, cap: solve_qwh(qgrid, QN, rg, cap), 500, QCAP, seed0=9_000)

samp_qwh = pool_sampler(pool_qwh)
rs_q = rate_grid(pool_qwh)
sw_qwh = sweep(samp_qwh, rs_q, NTRIAL, 78, "qwh")


def pool_report(pool, censored, cap):
    return {"n": len(pool), "cap": cap, "censored": int(censored),
            "censored_frac": float(censored / len(pool)),
            "median": float(np.median(pool)), "mean": float(pool.mean()),
            "p90": float(np.percentile(pool, 90)), "max": float(pool.max())}


out["P7_combinatorial_search"] = {
    "note": ("censoring truncates the tail, which biases CV DOWN and the "
             "no-restart baseline DOWN -- both make the test conservative"),
    "a_random_3sat_easy_control": {
        "instance": {"n_vars": N_VARS, "n_clauses": M_CL, "ratio": RATIO,
                     "instances_tried": tries},
        "pool": pool_report(pool_sat, cens_sat, 60_000),
        "CV": cv_of(pool_sat),
        "criterion_says_helps": bool(cv_of(pool_sat) > 1.0),
        "helps": sw_3sat["helps"], "r_opt": sw_3sat["r_opt"],
        "speedup": sw_3sat["speedup"], "cv_at_opt": sw_3sat["cv_at_opt"],
        "agrees": bool(sw_3sat["helps"] == (cv_of(pool_sat) > 1.0)),
    },
    "b_qwh_heavy_tailed": {
        "instance": {"order": QN, "holes_frac": QHOLES},
        "pool": pool_report(pool_qwh, cens_qwh, QCAP),
        "CV": cv_of(pool_qwh),
        "criterion_says_helps": bool(cv_of(pool_qwh) > 1.0),
        "helps": sw_qwh["helps"], "r_opt": sw_qwh["r_opt"],
        "speedup": sw_qwh["speedup"], "cv_at_opt": sw_qwh["cv_at_opt"],
        "agrees": bool(sw_qwh["helps"] == (cv_of(pool_qwh) > 1.0)),
    },
    "sign_flip_within_combinatorial_search": bool(
        (not sw_3sat["helps"]) and sw_qwh["helps"]),
}

# ---------------------------------------------------------------------------
# P4 -- parameter transfer, and P5 -- the identity test, across the three domains
# ---------------------------------------------------------------------------
domains = {
    "diffusive search": (s_levy(x0, D), sw_diff, None),
    "enzymatic turnover": (s_mm_disorder(), mm["dynamic disorder"]["sweep"], None),
    "randomized backtracking search": (samp_qwh, sw_qwh, pool_qwh),
}
transfer, identity = {}, {}
for name, (samp, sw, fixed_pool) in domains.items():
    base = fixed_pool if fixed_pool is not None else samp(NTRIAL,
                                                          np.random.default_rng(3))
    rs_d = np.array(sw["rs"])
    pred = predicted_curve(base, rs_d)
    obs = np.array(sw["means"])
    fin = np.isfinite(pred) & np.isfinite(obs) & (obs > 0) & (rs_d > 0)
    transfer[name] = {
        "max_rel_err_over_r_grid": float(np.max(np.abs(pred[fin] - obs[fin]) / obs[fin])),
        "median_rel_err": float(np.median(np.abs(pred[fin] - obs[fin]) / obs[fin])),
        "n_r_points": int(fin.sum()),
    }
    identity[name] = {"CV_unreset": cv_of(base), "r_opt": sw["r_opt"],
                      "CV_at_optimum": sw["cv_at_opt"],
                      "deviation_from_unity": abs(sw["cv_at_opt"] - 1.0)}
out["P4_parameter_transfer"] = {
    "domains": transfer,
    "all_within_3pct": bool(all(v["max_rel_err_over_r_grid"] < 0.03
                                for v in transfer.values())),
}
out["P5_identity_CV_at_optimum_equals_one"] = {
    "domains": identity,
    "max_deviation": float(max(v["deviation_from_unity"] for v in identity.values())),
    "all_within_0.05": bool(all(v["deviation_from_unity"] < 0.05
                                for v in identity.values())),
}

# ---------------------------------------------------------------------------
# P8 -- the Phi question: is this log-partition machinery on the exit time?
# ---------------------------------------------------------------------------
phi_check = {}
for name, (samp, sw, fixed_pool) in domains.items():
    base = fixed_pool if fixed_pool is not None else samp(NTRIAL,
                                                          np.random.default_rng(3))
    rs_d = np.array([r for r in sw["rs"] if r > 0])[:15]
    # Phi_T(s) = log E[e^{sT}] evaluated at s = -r; <T_r> = (e^{-Phi(-r)} - 1)/r
    viaPhi, viaL = [], []
    for r in rs_d:
        PhiT = float(np.log(np.mean(np.exp(-r * base))))     # Phi_T(-r)
        viaPhi.append((math.exp(-PhiT) - 1.0) / r)
        L = float(np.mean(np.exp(-r * base)))
        viaL.append((1.0 - L) / (r * L))
    viaPhi, viaL = np.array(viaPhi), np.array(viaL)
    # and the criterion as a cumulant condition:  Phi''(0) > Phi'(0)^2
    m1, m2 = float(base.mean()), float((base**2).mean())
    phi_check[name] = {
        "max_rel_err_CGF_vs_Laplace": float(np.max(np.abs(viaPhi - viaL)
                                                   / np.abs(viaL))),
        "Phi''(0)=Var": m2 - m1**2, "Phi'(0)^2=<T>^2": m1**2,
        "cumulant_criterion_says_helps": bool((m2 - m1**2) > m1**2),
        "simulation_says_helps": bool(sw["helps"]),
    }
out["P8_phi_form_on_exit_time"] = {
    "domains": phi_check,
    "identity_holds": bool(all(v["max_rel_err_CGF_vs_Laplace"] < 1e-6
                               for v in phi_check.values())),
    "reading": ("the restart theory is log-partition machinery built on the "
                "COMPLETION TIME, not on the state distribution"),
}

out["VERDICT"] = {
    "P1_sign_flip": out["P1_sign_flip"]["confirmed"],
    "P1_crossing": {k: out["P1_crossing_location"][k] for k in
                    ("crossing_from_slope_sign_change",
                     "crossing_from_significance_threshold_biased_late",
                     "predicted_sigma_star_sqrt_ln2", "rel_err", "confirmed")},
    "P2_knife_edge": out["P2_exponential_knife_edge"]["confirmed"],
    "P3_diffusion_optimum": out["P3_diffusion"]["confirmed"],
    "P4_transfer_within_3pct": out["P4_parameter_transfer"]["all_within_3pct"],
    "P5_CV_at_opt_equals_1": out["P5_identity_CV_at_optimum_equals_one"],
    "P6_mm_sign_flip": out["P6_michaelis_menten"]["sign_flip_within_one_scheme"],
    "P7_3sat_CV_and_helps": [out["P7_combinatorial_search"]
                             ["a_random_3sat_easy_control"]["CV"],
                             out["P7_combinatorial_search"]
                             ["a_random_3sat_easy_control"]["helps"]],
    "P7_qwh_CV_and_helps": [out["P7_combinatorial_search"]
                            ["b_qwh_heavy_tailed"]["CV"],
                            out["P7_combinatorial_search"]
                            ["b_qwh_heavy_tailed"]["helps"]],
    "P7_sign_flip": out["P7_combinatorial_search"]
                       ["sign_flip_within_combinatorial_search"],
    "P8_phi_identity": out["P8_phi_form_on_exit_time"]["identity_holds"],
}

print(json.dumps(out["VERDICT"], indent=2, default=float))
with open("verdict.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
