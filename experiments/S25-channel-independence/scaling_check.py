"""
S25 tie-breaker — pre-registered finite-size scaling check.

Two boundary cases from run.py need adjudication:
  1. block-majority channels peak ~0.15-0.175 ABOVE the full-state peak.
     If this shrinks with lattice size it is a finite-size coarse-graining
     shift (known physics), not a channel-dependent singularity.
  2. parity was pre-registered as an exactly-blind control; that claim was
     WRONG (energy being flip-even does not make it independent of up-spin
     parity). Parity carries real information and peaks near T=1.65.
     Track its peak and info share vs size: does it stay an off-peak
     informative channel, or wash out?

Lattices: 3x3 (512 states), 4x4 (65536), 4x5 (1048576). Exact enumeration.
"""
import numpy as np
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20260722)
Ts = np.linspace(1.5, 3.5, 81)


def enumerate_ising(Lr, Lc):
    n = Lr * Lc
    idx = np.arange(2 ** n, dtype=np.uint32)
    spins = ((idx[:, None] >> np.arange(n)) & 1).astype(np.int8) * 2 - 1
    site = lambda r, c: (r % Lr) * Lc + (c % Lc)
    E = np.zeros(2 ** n, dtype=np.float64)
    for r in range(Lr):
        for c in range(Lc):
            i = site(r, c)
            E -= spins[:, i] * (spins[:, site(r, c + 1)].astype(np.float64)
                                + spins[:, site(r + 1, c)])
    return spins, E


def channel_fisher(labels, E, Ts):
    K = int(labels.max()) + 1
    F = np.zeros(len(Ts))
    for t, T in enumerate(Ts):
        w = np.exp(-(E - E.min()) / T)
        w /= w.sum()
        p_y = np.bincount(labels, weights=w, minlength=K)
        Ey = np.bincount(labels, weights=w * E, minlength=K)
        mean_E = w @ E
        cond = np.divide(Ey, p_y, out=np.full(K, mean_E), where=p_y > 1e-300)
        F[t] = (p_y @ (cond - mean_E) ** 2) / T ** 4
    return F, float(np.trapezoid(F, Ts))


def peaks_for(Lr, Lc, n_blocks):
    spins, E = enumerate_ising(Lr, Lc)
    n = Lr * Lc
    out = {}
    F, info = channel_fisher(np.arange(len(spins)), E, Ts)
    out["full_state"] = (float(Ts[np.argmax(F)]), info)
    bp = []
    bsize = n // n_blocks
    for j in range(4):
        perm = RNG.permutation(n)[: n_blocks * bsize].reshape(n_blocks, bsize)
        votes = np.stack([np.sign(spins[:, b].sum(1)) for b in perm], 1) + 1
        lab = (votes * 3 ** np.arange(n_blocks)).sum(1)
        F, info = channel_fisher(lab, E, Ts)
        bp.append((float(Ts[np.argmax(F)]), info))
    out["block_majority"] = bp
    lab = (((spins + 1) // 2).sum(1) % 2).astype(int)
    F, info = channel_fisher(lab, E, Ts)
    out["parity"] = (float(Ts[np.argmax(F)]), info)
    return out


def main():
    res = {}
    for name, (Lr, Lc, nb) in {"3x3": (3, 3, 3), "4x4": (4, 4, 4),
                               "4x5": (4, 5, 4)}.items():
        print(f"--- {name} ({2**(Lr*Lc)} states) ---")
        r = peaks_for(Lr, Lc, nb)
        full_T, full_I = r["full_state"]
        bm_devs = [abs(p - full_T) for p, _ in r["block_majority"]]
        par_T, par_I = r["parity"]
        print(f"  full-state peak T* = {full_T:.3f}   info = {full_I:.3f}")
        print(f"  block-majority peak deviations: "
              + ", ".join(f"{d:.3f}" for d in bm_devs)
              + f"   (mean {np.mean(bm_devs):.3f})")
        print(f"  parity: peak T* = {par_T:.3f}  dev = {abs(par_T-full_T):.3f}"
              f"   info = {par_I:.4f}  ({par_I/full_I:.1%} of full)")
        res[name] = {"full_peak": full_T,
                     "block_majority_mean_dev": float(np.mean(bm_devs)),
                     "parity_peak": par_T, "parity_dev": abs(par_T - full_T),
                     "parity_info_share": par_I / full_I}
    with open(os.path.join(OUT, "scaling_check.json"), "w") as f:
        json.dump(res, f, indent=2)
    print("\nSCALING:", json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
