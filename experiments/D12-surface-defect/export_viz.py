"""
Export D12's results as small JSON files for the visual page (the "D12" Data
artifact). Reads raw/ (the Wang-Landau densities of states) and verdict.json,
recomputing every number with run.py's own functions. Writes viz/*.json, each
{rows, meta}, where meta carries this script's text so a reader can check it.

Run: python3 export_viz.py      (after run.py and run.py --extend)
"""
import json
import math
import os

import numpy as np

import run

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "viz")
SRC = open(os.path.abspath(__file__)).read()
LABEL = {"potts2d_q20": "2-D Potts q=20", "potts2d_q10": "2-D Potts q=10",
         "potts3d_q10": "3-D Potts q=10", "ising2d": "2-D Ising (control)"}
EXACT = {"potts2d_q20": 0.370988, "potts2d_q10": 0.094701}   # 2 sigma_od, Borgs-Janke


def meta(extra):
    return [{"label": "export_viz.py", "value": SRC, "type": "code", "lang": "python"},
            {"label": "Input", "value": extra}]


def r6(x):
    return None if x is None or (isinstance(x, float) and not math.isfinite(x)) else round(float(x), 6)


def system_rows(name, sd, L, stage):
    N = L ** sd["d"]
    k, g, gs = run.averaged(name, L, sd["seeds"])
    r = run.defect_of(k, g, N, sd["window"])
    seedD = [run.defect_of(kk, gg, N, sd["window"])["D"] for kk, gg in gs]
    lo = sd["window"][0]
    base = name.replace("_ext", "")
    intr = run.intruder_defect(k, g, N) if base != "ising2d" else None
    surf = L ** (sd["d"] - 1)
    return dict(system=LABEL[base], key=base, d=sd["d"], q=sd["q"], L=L, N=N,
                D=r6(r["D"]), D_err=r6(np.std(seedD, ddof=1) / math.sqrt(len(seedD))),
                D_over_surface=r6(r["D"] / surf),
                D_intruder=r6(intr), intruder_over_surface=r6(intr / surf) if intr is not None else None,
                e_at_max=r6(r["e_at_max"]), max_at_band_edge=bool(r["e_at_max"] < lo + 0.10),
                stage=stage)


def main():
    os.makedirs(OUT, exist_ok=True)
    v = json.load(open(os.path.join(HERE, "verdict.json")))
    defects = []
    for name, sd in run.SYSTEMS.items():
        for L in sd["Ls"]:
            defects.append(system_rows(name, sd, L, "registered"))
    ext = run.EXTENSION["potts3d_q10_ext"]
    for L in ext["Ls"]:
        defects.append(system_rows("potts3d_q10_ext", ext, L, "post hoc"))

    slopes = []
    for key in LABEL:
        rows = [r for r in defects if r["key"] == key]
        for stat in ("D", "D_intruder"):
            if rows[0][stat] is None:
                continue
            for a, b in zip(rows, rows[1:]):
                slopes.append(dict(system=LABEL[key], key=key, statistic="D10 defect" if stat == "D" else "intruder only",
                                   L_from=a["L"], L_to=b["L"],
                                   local_slope=r6(math.log(b[stat] / a[stat]) / math.log(b["N"] / a["N"])),
                                   stage="post hoc" if (b["stage"] == "post hoc" or stat != "D") else "registered"))

    res, ver = v["results"], v["verdict"]
    bands = {"potts2d_q20": [0.42, 0.58], "potts3d_q10": [0.567, 0.767], "potts2d_q10": [0.35, 0.85],
             "ising2d": [None, 0.15]}
    summary = []
    for key in LABEL:
        r = res[key]
        last = r["rows"][-1]
        summary.append(dict(system=LABEL[key], key=key, d=r["d"], q=r["q"], b=r6(r.get("b")), b_err=r6(r.get("b_err")),
                            band_lo=bands[key][0], band_hi=bands[key][1], surface_exponent=(r["d"] - 1) / r["d"],
                            L_last=last["L"], D_over_surface_last=r6(last["D_over_surface"]),
                            exact_2sigma=EXACT.get(key)))

    verdict = [
        dict(id="P1", system=LABEL["potts2d_q20"], registered="b = 0.50 ± 0.08, excluding 0 and 1 by > 3σ",
             measured=f"b = {ver['P1']['b']:.3f} ± {ver['P1']['b_err']:.3f}", result="pass" if ver["P1"]["pass"] else "fail"),
        dict(id="P2", system=LABEL["potts3d_q10"], registered="b = 0.667 ± 0.10, excluding ½ and 1 by > 3σ",
             measured=f"b = {ver['P2']['b']:.3f} ± {ver['P2']['b_err']:.4f}", result="pass" if ver["P2"]["pass"] else "fail"),
        dict(id="P3", system=LABEL["potts2d_q20"], registered="D/L at L = 48 within 10% of 2σ_od = 0.370988",
             measured=f"{ver['P3']['D_over_L']:.3f} ({ver['P3']['rel_dev']:+.1%})", result="pass" if ver["P3"]["pass"] else "fail"),
        dict(id="P4", system=LABEL["potts2d_q10"], registered="b in [0.35, 0.85]; D/L within 25% of 0.094701; slope → ½",
             measured=f"b = {ver['P4']['b']:.3f}; D/L = {ver['P4']['D_over_L']:.4f} ({ver['P4']['rel_dev']:+.1%})",
             result="pass" if ver["P4"]["pass"] else "fail"),
        dict(id="P5", system=LABEL["ising2d"], registered="D < 0.25 at every L, or b < 0.15",
             measured=f"b = {ver['P5']['b']:.2f}; max D = {ver['P5']['D_max']:.2f}", result="pass" if ver["P5"]["pass"] else "fail"),
    ]

    gap = []
    for name, L, step in (("potts2d_q10", 16, 1), ("potts2d_q10", 64, 8)):
        sd = run.SYSTEMS[name]
        N = L ** sd["d"]
        k, g, _ = run.averaged(name, L, sd["seeds"])
        e = -k / N
        shat, _ = run.concave_hull(e, g / N)
        gp = N * (shat - g / N)
        o = np.argsort(e)
        for i in o[::step]:
            gap.append(dict(system=LABEL[name], L=L, e=r6(e[i]), gap=r6(max(gp[i], 0.0))))

    inp = "raw/ (Wang-Landau ln Omega, seeds averaged) and verdict.json, experiments/D12-surface-defect"
    for fn, rows in (("defects", defects), ("slopes", slopes), ("summary", summary),
                     ("verdict", verdict), ("gap_profile", gap)):
        with open(os.path.join(OUT, fn + ".json"), "w") as f:
            json.dump({"rows": rows, "meta": meta(inp)}, f)
        print(fn, len(rows))


if __name__ == "__main__":
    main()
