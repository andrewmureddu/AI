"""
Numerical verification of derivations/S25-one-parameterness.md.

Three claims are checked, all exact-enumeration:

  1. Lemma 1 (exact characterization): a family is one-parameter iff the
     conditional mean energies mu_y(beta) are affine in one statistic
     across beta — i.e. the per-beta-centered matrix mu[beta, y] is
     rank 1. Exact for 1D decimation (known exponential family), near-1
     for majority rule, degraded for shell scrambling.

  2. Theorem 3 ordering: the measured rank defect tail3 = 1 - (s1^2+s2^2)/sum
     of the weighted centered log-prob matrix is controlled by
     rho^2, rho = Delta * sd_w(V_y) / (2 sd_w(mu_y)) — the dispersion of
     conditional VARIANCE across cells over the dispersion of conditional
     MEANS. Prediction: tail3 <= O(rho^2) and channels are ORDERED by rho.

  3. Scaling law: tail3 ~ Delta^2 as the window shrinks (log-log slope 2).
"""
import numpy as np
import json, os
from stress_channel import enumerate_lattice, make_stress_channels, boltzmann

OUT = os.path.dirname(os.path.abspath(__file__))
B0, DMAX = 0.4762, 0.1905          # window center/half-width in beta,
                                   # matching T in [1.5, 3.5]


def enumerate_ring(N):
    idx = np.arange(2 ** N, dtype=np.uint32)
    spins = ((idx[:, None] >> np.arange(N)) & 1).astype(np.int8) * 2 - 1
    E = -np.sum(spins * np.roll(spins, -1, axis=1), axis=1).astype(np.float64)
    return spins, E


def cond_moments(labels, E, beta, K):
    w = np.exp(-(E - E.min()) * beta)
    w /= w.sum()
    p_y = np.bincount(labels, weights=w, minlength=K)
    m1 = np.bincount(labels, weights=w * E, minlength=K)
    m2 = np.bincount(labels, weights=w * E * E, minlength=K)
    ok = p_y > 1e-300
    mu = np.where(ok, m1 / np.maximum(p_y, 1e-300), 0.0)
    V = np.where(ok, m2 / np.maximum(p_y, 1e-300) - mu ** 2, 0.0)
    return p_y, mu, V


def log_prob_matrix(labels, E, betas, K):
    P = np.zeros((len(betas), K))
    for t, b in enumerate(betas):
        w = np.exp(-(E - E.min()) * b)
        P[t] = np.bincount(labels, weights=w / w.sum(), minlength=K)
    return P


def spectrum_fracs(P):
    """Weighted, per-row-centered log matrix -> (frac1, frac2, tail3)."""
    wc = np.sqrt(np.maximum(P.mean(axis=0), 1e-300))
    L = np.log(np.maximum(P, 1e-300))
    mu_row = (L * wc ** 2).sum(1, keepdims=True) / (wc ** 2).sum()
    s = np.linalg.svd((L - mu_row) * wc, compute_uv=False)
    tot = np.sum(s ** 2)
    return (float(s[0] ** 2 / tot),
            float((s[0] ** 2 + s[1] ** 2) / tot),
            float(np.sum(s[2:] ** 2) / tot))


def mu_rank1_fraction(labels, E, betas, K):
    """Lemma-1 check: rank-1 fraction of the per-beta-centered,
    probability-weighted conditional-mean-energy matrix."""
    MU = np.zeros((len(betas), K))
    W = np.zeros(K)
    for t, b in enumerate(betas):
        p_y, mu, _ = cond_moments(labels, E, b, K)
        MU[t] = mu
        W += p_y / len(betas)
    wc = np.sqrt(np.maximum(W, 1e-300))
    m = (MU * wc ** 2).sum(1, keepdims=True) / (wc ** 2).sum()
    s = np.linalg.svd((MU - m) * wc, compute_uv=False)
    return float(s[0] ** 2 / np.sum(s ** 2))


def wsd(x, w):
    w = w / w.sum()
    m = w @ x
    return float(np.sqrt(w @ (x - m) ** 2))


def main():
    betas = np.linspace(B0 - DMAX, B0 + DMAX, 161)
    spins, E = enumerate_lattice(4, 4)
    channels = make_stress_channels(spins, E)

    # --- Claim 1: exact characterization on the known exponential family
    print("=" * 72)
    print("CLAIM 1 — Lemma 1: mu_y(beta) affine in one statistic iff 1-param")
    print("=" * 72)
    s16, E16 = enumerate_ring(16)
    bits = ((s16[:, ::2] + 1) // 2).astype(np.int64)
    dec_labels = (bits * (2 ** np.arange(8))).sum(1)
    f_dec = mu_rank1_fraction(dec_labels, E16, betas, 256)
    print(f"  1D decimation (exactly 1-param):   mu rank-1 fraction = "
          f"{f_dec:.12f}   (1 - {1 - f_dec:.2e})")
    mu_fracs = {}
    for name in ("geometric_majority", "shell_scramble_6"):
        labels, _ = channels[name]
        K = int(labels.max()) + 1
        mu_fracs[name] = mu_rank1_fraction(labels, E, betas, K)
        print(f"  {name:34s} mu rank-1 fraction = {mu_fracs[name]:.6f}")

    # --- Claim 2: defect ordered/bounded by rho^2
    print("\n" + "=" * 72)
    print("CLAIM 2 — Theorem 3: tail3 controlled by rho^2, "
          "rho = Delta sd_w(V)/(2 sd_w(mu))")
    print("=" * 72)
    print(f"{'channel':22s} {'sd_w(mu)':>9s} {'sd_w(V)':>9s} {'rho^2':>10s} "
          f"{'tail3':>10s} {'1-frac1':>9s} {'bound ok':>8s}")
    rows = {}
    for name, (labels, fam) in channels.items():
        K = int(labels.max()) + 1
        p_y, mu, _ = cond_moments(labels, E, B0, K)
        # Theorem 2 uses the WINDOW-MAX conditional variance per cell
        # (V*_y), not the center value — a channel's variance dispersion
        # can accidentally vanish at one beta (energy_mod_8 does).
        Vstar = np.max([cond_moments(labels, E, b, K)[2]
                        for b in np.linspace(B0 - DMAX, B0 + DMAX, 9)], axis=0)
        sd_mu, sd_V = wsd(mu, p_y), wsd(Vstar, p_y)
        rho2 = (DMAX * sd_V / (2 * sd_mu)) ** 2 if sd_mu > 0 else np.inf
        P = log_prob_matrix(labels, E, betas, K)
        f1, f2, tail3 = spectrum_fracs(P)
        rows[name] = dict(family=fam, sd_mu=sd_mu, sd_V=sd_V, rho2=rho2,
                          tail3=tail3, one_minus_frac1=1 - f1,
                          bound_ok=bool(tail3 <= rho2))
        print(f"{name:22s} {sd_mu:9.3f} {sd_V:9.3f} {rho2:10.2e} "
              f"{tail3:10.2e} {1-f1:9.2e} {str(tail3 <= rho2):>8s}")
    r2 = np.array([rows[n]["rho2"] for n in rows])
    t3 = np.array([rows[n]["tail3"] for n in rows])
    m = (r2 > 0) & (t3 > 0)
    corr = float(np.corrcoef(np.log(r2[m]), np.log(t3[m]))[0, 1])
    print(f"\n  log-log correlation(rho^2, tail3) across channels = {corr:.3f}")
    print(f"  bound tail3 <= rho^2 holds for {sum(r['bound_ok'] for r in rows.values())}"
          f"/{len(rows)} channels")

    # --- Claim 3: Delta^2 scaling of the defect
    print("\n" + "=" * 72)
    print("CLAIM 3 — scaling: tail3 ~ Delta^4 (norm is carrier-dominated; "
          "slope 4,\n          higher if leading cumulant dispersion cancels)")
    print("=" * 72)
    slopes = {}
    Deltas = np.array([0.05, 0.08, 0.12, 0.19])
    for name in ("geometric_majority", "abs_magnetization",
                 "shell_scramble_6", "crossover_pairs"):
        labels, _ = channels[name]
        K = int(labels.max()) + 1
        tails = []
        for D in Deltas:
            bg = np.linspace(B0 - D, B0 + D, 121)
            tails.append(spectrum_fracs(log_prob_matrix(labels, E, bg, K))[2])
        tails = np.array(tails)
        slope = float(np.polyfit(np.log(Deltas), np.log(tails), 1)[0])
        slopes[name] = slope
        print(f"  {name:22s} tail3(Delta): "
              + "  ".join(f"{t:.1e}" for t in tails)
              + f"   slope = {slope:.2f}")

    verdict = {
        "claim1_decimation_mu_rank1_defect": float(1 - f_dec),
        "claim1_mu_rank1": mu_fracs,
        "claim2_channels": rows,
        "claim2_loglog_correlation": corr,
        "claim2_bound_holds": int(sum(r["bound_ok"] for r in rows.values())),
        "claim2_n_channels": len(rows),
        "claim3_slopes": slopes,
    }
    with open(os.path.join(OUT, "theorem_verdict.json"), "w") as f:
        json.dump(verdict, f, indent=2)
    print("\nsaved theorem_verdict.json")


if __name__ == "__main__":
    main()
