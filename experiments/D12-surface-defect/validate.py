"""
Code check for wl.c: Wang-Landau ln Omega against exact enumeration (enum.c) on
lattices small enough to enumerate, at the production setting ln f_final = 1e-6.
2-D windows run all the way to the ground state, so they exercise wl.c's
reachable-level rule; the 3-D lattice uses a bulk window (odd L = 3 is
frustrated below k = 27).  Carries no evidential weight for D12.

Run: python3 validate.py    (~2 min; writes validation.json)
"""
import json
import os
import subprocess
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = [  # q, d, L, kmin, kmax
    (2, 2, 4, 4, 32),       # k = 2 is unreachable (mirror of m = 2 at the AF end)
    (3, 2, 4, 0, 32),
    (4, 2, 4, 4, 32),
    (2, 3, 3, 33, 69),
]


def build():
    for src in ("wl", "enum"):
        subprocess.run(["gcc", "-O3", "-march=native", "-o", os.path.join(HERE, src),
                        os.path.join(HERE, src + ".c"), "-lm"], check=True)


def main():
    build()
    out = {}
    with tempfile.TemporaryDirectory() as tmp:
        procs = []
        for q, d, L, kmin, kmax in CASES:
            tag = f"q{q}_d{d}_L{L}"
            e, w = os.path.join(tmp, "e_" + tag), os.path.join(tmp, "w_" + tag)
            procs.append((tag, e, w, kmin, kmax,
                          subprocess.Popen([os.path.join(HERE, "enum"), str(q), str(d), str(L), e]),
                          subprocess.Popen([os.path.join(HERE, "wl"), str(q), str(d), str(L),
                                            str(kmin), str(kmax), "1", "1e-6", w])))
        for tag, e, w, kmin, kmax, pe, pw in procs:
            assert pe.wait() == 0 and pw.wait() == 0, tag
            ex = {int(r[0]): r[1] for r in np.atleast_2d(np.loadtxt(e))}
            wv = {int(r[0]): r[1] for r in np.loadtxt(w) if r[2] > 0}
            want = {k for k in ex if kmin <= k <= kmax}
            ks = sorted(wv)
            E = np.array([ex[k] for k in ks])
            W = np.array([wv[k] for k in ks])
            dev = (W - W.mean()) - (E - E.mean())
            out[tag] = dict(window=[kmin, kmax], levels=len(ks), levels_match=set(wv) == want,
                            max_abs_err=float(np.abs(dev).max()),
                            rms_err=float(np.sqrt((dev ** 2).mean())))
            print(tag, out[tag])
    with open(os.path.join(HERE, "validation.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
