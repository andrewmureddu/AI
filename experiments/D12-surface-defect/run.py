"""
D12 -- does the order-0 (concavity) defect scale as the surface in short-range
models with a first-order transition?

Pre-registration: PREREGISTRATION.md (committed before any production run).

  P1  AT-RISK  2-D Potts q=20: D ~ N^b, b = 0.50 +/- 0.08, excluding 0 and 1 by >3 sd
  P2  AT-RISK  3-D Potts q=10: b = 0.667 +/- 0.10, excluding 0.5 and 1 by >3 sd
  P3  AT-RISK  2-D q=20: D/L at the largest L within 10% of 2 sigma_od = 0.370988
  P4  AT-RISK  2-D q=10 (crossover): b in [0.35, 0.85]; D/L within 25% of 0.094701;
               largest-pair local slope closer to 0.5 than smallest-pair
  P5  AT-RISK  2-D Ising (continuous) control: D < 0.25 at every L, or b < 0.15
  I1  IDENTITY max N(s_hat - s) == ln(P_max/P_min) at beta = bitangent slope
  I2  CHECK    bitangent slope at the largest 2-D L within 2% of ln(1 + sqrt q)

The defect is D10's: D = N * max_e [s_hat(e) - s(e)], s = ln Omega / N, s_hat the
exact upper concave envelope (D10's monotone-chain hull, copied verbatim).
Omega from Wang-Landau (wl.c, 1/t schedule), validated against exact enumeration.

Run: python3 run.py            (compiles wl.c, runs missing jobs on all cores,
                                 caches raw/ ; ~1-2 h on 4 cores from scratch)
     python3 run.py --analyze   (analysis only, from raw/)
"""

import json
import math
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
WL = os.path.join(HERE, "wl")
LNF_FINAL = 1e-6

SIGMA2 = {20: 0.370988, 10: 0.094701}      # exact 2*sigma_od, Borgs-Janke

SYSTEMS = {
    "potts2d_q20": dict(q=20, d=2, Ls=[12, 16, 24, 32, 48], window=(-1.99, -0.30), seeds=[1, 2, 3, 4]),
    "potts2d_q10": dict(q=10, d=2, Ls=[16, 24, 32, 48, 64], window=(-1.97, -0.55), seeds=[1, 2, 3, 4]),
    "potts3d_q10": dict(q=10, d=3, Ls=[8, 10, 12, 14], window=(-2.90, -0.45), seeds=[1, 2, 3]),
    "ising2d":     dict(q=2, d=2, Ls=[8, 12, 16, 24, 32], window=(-1.98, -1.30), seeds=[1, 2, 3, 4]),
}


# ---------------------------------------------------------------------------
# jobs
# ---------------------------------------------------------------------------

def kwindow(sysd, L):
    N = L ** sysd["d"]
    lo, hi = sysd["window"]                  # in e = -k/N
    d = sysd["d"]
    # 3-D: keep clear of the sparse levels next to the ground state (wl.c
    # enumerates them exactly only in 2-D).  Never binding for the registered
    # 3-D window, which stops 0.1 N below the ground state.
    kmax = int(math.floor(-lo * N))
    if d == 3:
        kmax = min(kmax, d * N - 14)
    return N, int(math.ceil(-hi * N)), kmax


def outpath(name, L, seed):
    return os.path.join(RAW, f"{name}_L{L}_s{seed}.txt")


def jobs():
    out = []
    for name, sd in SYSTEMS.items():
        for L in sd["Ls"]:
            N, kmin, kmax = kwindow(sd, L)
            for seed in sd["seeds"]:
                out.append((N * (kmax - kmin), name, sd, L, seed, kmin, kmax))
    out.sort(key=lambda j: -j[0])            # largest first
    return out


def run_job(j):
    _, name, sd, L, seed, kmin, kmax = j
    p = outpath(name, L, seed)
    if os.path.exists(p):
        return p, 0.0
    t0 = time.time()
    tmp = p + ".tmp"
    subprocess.run([WL, str(sd["q"]), str(sd["d"]), str(L), str(kmin), str(kmax),
                    str(seed), str(LNF_FINAL), tmp], check=True)
    os.replace(tmp, p)
    dt = time.time() - t0
    print(f"  done {name} L={L} seed={seed} in {dt:.0f}s", flush=True)
    return p, dt


def run_all():
    os.makedirs(RAW, exist_ok=True)
    if not os.path.exists(WL) or os.path.getmtime(WL) < os.path.getmtime(WL + ".c"):
        subprocess.run(["gcc", "-O3", "-march=native", "-o", WL, WL + ".c", "-lm"], check=True)
    todo = [j for j in jobs() if not os.path.exists(outpath(j[1], j[3], j[4]))]
    print(f"{len(todo)} jobs to run", flush=True)
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        list(ex.map(run_job, todo))


# ---------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------

def concave_hull(e, s):
    """Exact upper concave envelope by monotone chain -- verbatim from D10."""
    order = np.argsort(e)
    ex, sx = e[order], s[order]
    hull = []
    for i in range(len(ex)):
        while len(hull) >= 2:
            a, b = hull[-2], hull[-1]
            cross = ((ex[b] - ex[a]) * (sx[i] - sx[a])
                     - (sx[b] - sx[a]) * (ex[i] - ex[a]))
            if cross >= 0:
                hull.pop()
            else:
                break
        hull.append(i)
    hx, hy = ex[hull], sx[hull]
    out = np.empty_like(s)
    out[order] = np.interp(ex, hx, hy)
    return out, hx


def load(name, L, seed):
    a = np.loadtxt(outpath(name, L, seed))
    return a[:, 0].astype(int), a[:, 1], a[:, 2] > 0


def defect_of(k, lng, N, window):
    """D10's defect plus the diagnostics the pre-registration needs."""
    e = -k / N
    s = lng / N
    shat, hx = concave_hull(e, s)
    gap = shat - s
    i = int(np.argmax(gap))
    D = float(N * gap[i])
    # widest hull edge = the bitangent
    j = int(np.argmax(np.diff(hx)))
    ea, eb = float(hx[j]), float(hx[j + 1])
    ia, ib = int(np.argmin(np.abs(e - ea))), int(np.argmin(np.abs(e - eb)))
    slope = float((s[ib] - s[ia]) / (e[ib] - e[ia]))         # = beta at coexistence
    # window rule: both bitangent vertices >= 2% of the window width from the ends
    lo, hi = window
    w = hi - lo
    inside = (ea - lo > 0.02 * w) and (hi - eb > 0.02 * w)
    # I1: ln P(E) = ln Omega(E) - beta E, E = N e ; ratio of max to min between peaks
    lnP = lng - slope * N * e
    between = (e >= min(ea, eb)) & (e <= max(ea, eb))
    lnratio = float(lnP[between].max() - lnP[between].min()) if D > 0 else 0.0
    return dict(D=D, e_at_max=float(e[i]), bitangent=(ea, eb), beta=slope,
                window_ok=bool(inside), I1_lnPratio=lnratio)


def averaged(name, L, seeds):
    curves = []
    for sd in seeds:
        k, g, v = load(name, L, sd)
        curves.append((k, g, v))
    k = curves[0][0]
    vis = np.logical_and.reduce([c[2] for c in curves])
    G = np.array([c[1][vis] - c[1][vis].mean() for c in curves])
    return k[vis], G.mean(axis=0), [(k[vis], g) for g in G]


def fit_slope(x, y):
    A = np.vstack([np.log(x), np.ones_like(x)]).T
    return float(np.linalg.lstsq(A, np.log(y), rcond=None)[0][0])


def analyze():
    res = {}
    for name, sd in SYSTEMS.items():
        rows, per_seed = [], {s: [] for s in sd["seeds"]}
        for L in sd["Ls"]:
            N = L ** sd["d"]
            k, gbar, gs = averaged(name, L, sd["seeds"])
            r = defect_of(k, gbar, N, sd["window"])
            seedD = []
            for s, (kk, g) in zip(sd["seeds"], gs):
                rs = defect_of(kk, g, N, sd["window"])
                seedD.append(rs["D"])
                per_seed[s].append(rs["D"])
            r.update(L=L, N=N, D_seed=seedD,
                     D_err=float(np.std(seedD, ddof=1) / math.sqrt(len(seedD))),
                     D_over_L=r["D"] / L, D_per_site=r["D"] / N,
                     D_over_surface=r["D"] / L ** (sd["d"] - 1))
            rows.append(r)
        Ns = np.array([r["N"] for r in rows], float)
        Ds = np.array([r["D"] for r in rows])
        out = dict(rows=rows, q=sd["q"], d=sd["d"])
        if np.all(Ds > 1e-9):
            b = fit_slope(Ns, Ds)
            bs = [fit_slope(Ns, np.array(per_seed[s])) for s in sd["seeds"]
                  if np.all(np.array(per_seed[s]) > 1e-9)]
            berr = float(np.std(bs, ddof=1) / math.sqrt(len(bs))) if len(bs) > 1 else float("nan")
            loc = [float(math.log(Ds[i + 1] / Ds[i]) / math.log(Ns[i + 1] / Ns[i]))
                   for i in range(len(Ds) - 1)]
            out.update(b=b, b_err=berr, b_per_seed=bs, local_slopes=loc)
            # secondary, NOT registered: D = a L^{d-1} + c ln L + e
            Ls = np.array([r["L"] for r in rows], float)
            A = np.vstack([Ls ** (sd["d"] - 1), np.log(Ls), np.ones_like(Ls)]).T
            out["secondary_fit_a_c_e"] = [float(x) for x in np.linalg.lstsq(A, Ds, rcond=None)[0]]
        res[name] = out
    return res


def verdict(res):
    v = {}
    q20, q10, d3, ising = (res[k] for k in ("potts2d_q20", "potts2d_q10", "potts3d_q10", "ising2d"))

    def disc(r, alts):
        return all(abs(r["b"] - a) > 3 * r["b_err"] for a in alts)

    v["P1"] = dict(b=q20["b"], b_err=q20["b_err"], band=[0.42, 0.58],
                   in_band=0.42 <= q20["b"] <= 0.58, discriminates_0_and_1=disc(q20, [0, 1]))
    v["P1"]["pass"] = v["P1"]["in_band"] and v["P1"]["discriminates_0_and_1"]
    v["P2"] = dict(b=d3["b"], b_err=d3["b_err"], band=[0.567, 0.767],
                   in_band=0.567 <= d3["b"] <= 0.767, discriminates_half_and_1=disc(d3, [0.5, 1]))
    v["P2"]["pass"] = v["P2"]["in_band"] and v["P2"]["discriminates_half_and_1"]
    last = q20["rows"][-1]
    rel = last["D_over_L"] / SIGMA2[20] - 1
    v["P3"] = dict(L=last["L"], D_over_L=last["D_over_L"], exact=SIGMA2[20], rel_dev=rel,
                   **{"pass": abs(rel) <= 0.10})
    last10 = q10["rows"][-1]
    rel10 = last10["D_over_L"] / SIGMA2[10] - 1
    loc = q10["local_slopes"]
    v["P4"] = dict(b=q10["b"], b_err=q10["b_err"], b_in_band=0.35 <= q10["b"] <= 0.85,
                   D_over_L=last10["D_over_L"], rel_dev=rel10, mag_ok=abs(rel10) <= 0.25,
                   local_first=loc[0], local_last=loc[-1],
                   approaches_half=abs(loc[-1] - 0.5) < abs(loc[0] - 0.5))
    v["P4"]["pass"] = v["P4"]["b_in_band"] and v["P4"]["mag_ok"] and v["P4"]["approaches_half"]
    Dmax = max(r["D"] for r in ising["rows"])
    v["P5"] = dict(D_values=[r["D"] for r in ising["rows"]], D_max=Dmax, b=ising.get("b"),
                   **{"pass": Dmax < 0.25 or (ising.get("b") is not None and ising["b"] < 0.15)})
    i1 = [abs(r["D"] - r["I1_lnPratio"]) for k in ("potts2d_q20", "potts2d_q10", "potts3d_q10")
          for r in res[k]["rows"]]
    v["I1_identity_max_abs_diff"] = max(i1)
    v["I2"] = {}
    for k, q in (("potts2d_q20", 20), ("potts2d_q10", 10)):
        bt = math.log(1 + math.sqrt(q))
        bl = res[k]["rows"][-1]["beta"]
        v["I2"][k] = dict(beta_bitangent=bl, beta_t=bt, rel=bl / bt - 1, ok=abs(bl / bt - 1) <= 0.02)
    v["window_rule_all_ok"] = all(r["window_ok"] for k in ("potts2d_q20", "potts2d_q10", "potts3d_q10")
                                  for r in res[k]["rows"])
    return v


def main():
    t0 = time.time()
    if "--analyze" not in sys.argv:
        run_all()
    res = analyze()
    v = verdict(res)
    for name, r in res.items():
        print(f"--- {name}  b={r.get('b', float('nan')):+.4f} +/- {r.get('b_err', float('nan')):.4f}"
              f"  local={[round(x, 3) for x in r.get('local_slopes', [])]}")
        for row in r["rows"]:
            print(f"    L={row['L']:3d} N={row['N']:6d}  D={row['D']:9.4f} +/- {row['D_err']:.4f}"
                  f"  D/L^(d-1)={row['D_over_surface']:.5f}  beta={row['beta']:.4f}"
                  f"  bitangent={row['bitangent'][0]:+.3f}..{row['bitangent'][1]:+.3f}"
                  f"  win_ok={row['window_ok']}  |D-I1|={abs(row['D'] - row['I1_lnPratio']):.1e}")
        if "secondary_fit_a_c_e" in r:
            print(f"    secondary (unregistered) D = a L^(d-1) + c ln L + e : {r['secondary_fit_a_c_e']}")
    print(json.dumps(v, indent=1))
    with open(os.path.join(HERE, "verdict.json"), "w") as f:
        json.dump(dict(stone="D12", verdict=v, results=res, lnf_final=LNF_FINAL,
                       analysis_runtime_s=round(time.time() - t0, 1)), f, indent=1)


if __name__ == "__main__":
    main()
