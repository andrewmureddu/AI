"""
S25 stress test — a channel FAR from any one-parameter family.

The composition law F_c = F_eff(T') (dT'/dT)^2 is nearly automatic when the
induced family p_c(y|T) lies close to a one-parameter exponential family.
Every channel tested so far did (majority rule: <=0.01 bits from effective
Ising). This script (1) builds channels designed NOT to, (2) measures
one-parameterness intrinsically, (3) checks what happens to the law and to
the peak when one-parameterness fails.

Intrinsic measure: p_c is a 1-param exponential family in T iff
    log p_c(y|T) = -beta'(T) E_eff(y) + c(T),
i.e. the per-T-centered log-probability matrix L[t,y] has rank 1. The SVD
rank-1 energy fraction s1^2/sum(s^2) is the "one-parameterness"; the best
rank-1 approximation simultaneously yields the best-fit effective model
(E_eff from the right singular vector, beta'(T) from the left), from which
the composed/fitted Fisher prediction follows:
    F_fit(T) = (d beta'/dT)^2 Var_{q(T)}(E_eff),  q = softmax(-beta' E_eff).

Stress channels mix well-separated energy shells into the same cell, so
different cells freeze out at different rates and no single effective
temperature can track all of them:
  - energy_mod_m: label = (energy shell index) mod m
  - shell_scramble: label = random pairing that merges low- and high-energy
    shells into the same cell
  - EM_interleave: label = (E shell + |M| level) mod m

Reference channels (expected near rank-1): geometric 2x2 majority rule,
abs magnetization, one random 8-bucket hash.

Exact enumeration (4x4 Ising), pure numpy.
"""
import numpy as np
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
Ts = np.linspace(1.5, 3.5, 201)
RNG = np.random.default_rng(20260724)


def enumerate_lattice(Lr, Lc):
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


def boltzmann(E, T):
    w = np.exp(-(E - E.min()) / T)
    return w / w.sum()


def induced_matrix(labels, E, Ts, K):
    P = np.zeros((len(Ts), K))
    for t, T in enumerate(Ts):
        P[t] = np.bincount(labels, weights=boltzmann(E, T), minlength=K)
    return P


def fisher_from_probs(P, Ts):
    """Exact Fisher of a discrete family given on a fine T grid, via
    d/dT log p computed with np.gradient (grid is fine: dT=0.01)."""
    dlog = np.gradient(np.log(np.maximum(P, 1e-300)), Ts, axis=0)
    return np.sum(P * dlog ** 2, axis=1)


def full_fisher(E, Ts):
    return np.array([boltzmann(E, T) @ (E - boltzmann(E, T) @ E) ** 2 / T ** 4
                     for T in Ts])


def rank1_analysis(P, Ts):
    """Probability-weighted rank-1 test of the centered log-prob matrix.
    Weighting by each cell's mean probability keeps near-zero-probability
    cells (which barely affect KL or Fisher) from dominating the fit.
    Returns the one-parameterness fraction and the best-fit 1-param
    family's Fisher curve + KL residual."""
    w = np.sqrt(np.maximum(P.mean(axis=0), 1e-300))
    L = np.log(np.maximum(P, 1e-300))
    mu = (L * w ** 2).sum(1, keepdims=True) / (w ** 2).sum()
    Lc = (L - mu) * w                      # weighted, centered
    U, s, Vt = np.linalg.svd(Lc, full_matrices=False)
    frac = float(s[0] ** 2 / np.sum(s ** 2))
    beta = -U[:, 0] * s[0]                 # sign absorbed into E_eff
    E_eff = Vt[0] / w                      # undo column weighting
    logits = -np.outer(beta, E_eff)
    Q = np.exp(logits - logits.max(axis=1, keepdims=True))
    Q /= Q.sum(axis=1, keepdims=True)
    kl_bits = np.array([np.sum(p[p > 0] * np.log2(p[p > 0] / np.maximum(
        q[p > 0], 1e-300))) for p, q in zip(P, Q)])
    dbeta = np.gradient(beta, Ts)
    varE = np.sum(Q * E_eff ** 2, axis=1) - (Q @ E_eff) ** 2
    F_fit = dbeta ** 2 * varE
    return frac, F_fit, kl_bits


def make_stress_channels(spins, E):
    M = spins.sum(1)
    Evals, e_idx = np.unique(E, return_inverse=True)   # shell index per state
    nsh = len(Evals)
    ch = {}
    ch["energy_mod_5"] = (e_idx % 5, "stress")
    ch["energy_mod_8"] = (e_idx % 8, "stress")
    pair = RNG.permutation(nsh)                        # scramble shells
    ch["shell_scramble_6"] = (pair[e_idx] % 6, "stress")
    mlev = (np.abs(M) // 2).astype(int)
    ch["EM_interleave_7"] = ((e_idx + 3 * mlev) % 7, "stress")
    # crossover-pairs: merge shell pairs whose Boltzmann weights invert at
    # beta* = ln(g_i/g_j)/(E_i - E_j) INSIDE the window, at different
    # beta* per cell — the design a single effective temperature cannot
    # track. Greedy: pick disjoint pairs with in-window crossovers, spread.
    g = np.bincount(e_idx).astype(np.float64)
    blo, bhi = 1.0 / Ts.max(), 1.0 / Ts.min()
    cand = []
    for i in range(nsh):
        for j in range(i + 1, nsh):
            bstar = np.log(g[i] / g[j]) / (Evals[i] - Evals[j])
            if blo < bstar < bhi:
                cand.append((bstar, i, j))
    cand.sort()
    used, lab_of_shell, lab = set(), np.full(nsh, -1), 0
    for bstar, i, j in cand:               # sorted: crossovers spread
        if i not in used and j not in used:
            lab_of_shell[i] = lab_of_shell[j] = lab
            used.update((i, j))
            lab += 1
    for i in range(nsh):                   # unpaired shells: own labels
        if lab_of_shell[i] < 0:
            lab_of_shell[i] = lab
            lab += 1
    ch["crossover_pairs"] = (lab_of_shell[e_idx], "stress")
    # references
    site = lambda r, c: (r % 4) * 4 + (c % 4)
    geo = [np.array([site(r, c), site(r, c + 1), site(r + 1, c),
                     site(r + 1, c + 1)]) for r in (0, 2) for c in (0, 2)]
    votes = []
    for b in geo:
        s = spins[:, b].sum(1)
        v = np.sign(s)
        v[s == 0] = spins[s == 0][:, b[0]]
        votes.append(((v + 1) // 2).astype(np.int64))
    ch["geometric_majority"] = ((np.stack(votes, 1)
                                 * 2 ** np.arange(4)).sum(1), "reference")
    ch["abs_magnetization"] = (mlev, "reference")
    S = RNG.choice(16, size=8, replace=False)
    cfg = ((spins[:, S] + 1) // 2 * (2 ** np.arange(8))).sum(1)
    ch["hash8"] = (RNG.integers(0, 8, size=256)[cfg], "reference")
    return ch


def main():
    spins, E = enumerate_lattice(4, 4)
    F0 = full_fisher(E, Ts)
    p_full = float(Ts[np.argmax(F0)])
    print(f"full-state Fisher peak T* = {p_full:.2f}\n")
    print(f"{'channel':22s} {'family':9s} {'rank1':>6s} {'KLmax':>7s} "
          f"{'peak_meas':>9s} {'peak_fit':>8s} {'mismatch':>8s} "
          f"{'dev_full':>8s}")
    results = {}
    for name, (labels, fam) in make_stress_channels(spins, E).items():
        K = int(labels.max()) + 1
        P = induced_matrix(labels, E, Ts, K)
        F_c = fisher_from_probs(P, Ts)
        frac, F_fit, kl_bits = rank1_analysis(P, Ts)
        pm = float(Ts[np.argmax(F_c)])
        pf = float(Ts[np.argmax(F_fit)])
        results[name] = dict(family=fam, rank1_fraction=frac,
                             kl_bits_max=float(kl_bits.max()),
                             peak_measured=pm, peak_fitlaw=pf,
                             law_mismatch=float(abs(pm - pf)),
                             dev_from_full=float(abs(pm - p_full)))
        print(f"{name:22s} {fam:9s} {frac:6.4f} {kl_bits.max():7.4f} "
              f"{pm:9.2f} {pf:8.2f} {abs(pm-pf):8.3f} {abs(pm-p_full):8.3f}")
        np.savetxt(os.path.join(OUT, f"stress_{name}.csv"),
                   np.column_stack([Ts, F_c, F_fit]), delimiter=",",
                   header="T,F_channel,F_fitted_1param", comments="")
    results["full_peak"] = p_full
    with open(os.path.join(OUT, "stress_verdict.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("\nsaved stress_verdict.json + per-channel curves")


if __name__ == "__main__":
    main()
