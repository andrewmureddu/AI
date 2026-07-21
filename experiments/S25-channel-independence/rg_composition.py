"""
S25 follow-up — is the structured-channel peak shift an RG composition law?

S25 found that block-majority channels shift the Fisher peak persistently
(+~0.2), falsifying clean channel-independence. Hypothesis promoted here to
a prediction: a structured channel c acts as a renormalization step, and its
Fisher curve is the EFFECTIVE system's curve pulled back through the RG map,

    F_c(T)  =  F_eff(T'(T)) * (dT'/dT)^2        (composition law)

so the shifted peak is not an anomaly of the field but the singular
structure of the renormalized field, composed with the channel.

  Leg 1 (exact anchor): 1D Ising ring N=16, channel = decimation (keep
     alternate spins). The RG map is exact: tanh K' = tanh^2 K, and the
     induced distribution IS the Boltzmann distribution of an 8-ring at K'.
     The composition law must hold to machine precision, peak shift
     predicted analytically. If it doesn't, the framework is wrong.

  Leg 2 (the real question): 4x4 -> 2x2 majority rule (geometric blocks,
     ties broken by the block's first spin). Fit T'(T) by minimum KL
     against an exact periodic 2x2 Ising; report the KL residual; check
     whether the composed prediction reproduces the measured peak of the
     channel Fisher curve. Control: random (non-geometric) 4-blocks, which
     are NOT an RG step — does the composition law degrade?

Everything exact enumeration, pure numpy.
"""
import numpy as np
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
Ts = np.linspace(1.05, 3.5, 246)  # step 0.01


# ---------------------------------------------------------------- shared
def enumerate_ring(N):
    idx = np.arange(2 ** N, dtype=np.uint32)
    spins = ((idx[:, None] >> np.arange(N)) & 1).astype(np.int8) * 2 - 1
    E = -np.sum(spins * np.roll(spins, -1, axis=1), axis=1).astype(np.float64)
    return spins, E


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


def channel_fisher_curve(labels, E, Ts):
    K = int(labels.max()) + 1
    F = np.zeros(len(Ts))
    for t, T in enumerate(Ts):
        w = boltzmann(E, T)
        p_y = np.bincount(labels, weights=w, minlength=K)
        Ey = np.bincount(labels, weights=w * E, minlength=K)
        mE = w @ E
        cond = np.divide(Ey, p_y, out=np.full(K, mE), where=p_y > 1e-300)
        F[t] = (p_y @ (cond - mE) ** 2) / T ** 4
    return F


def full_fisher_curve(E, Ts):
    return np.array([boltzmann(E, T) @ (E - boltzmann(E, T) @ E) ** 2 / T ** 4
                     for T in Ts])


def induced(labels, E, T, K):
    return np.bincount(labels, weights=boltzmann(E, T), minlength=K)


def kl(p, q):
    m = p > 1e-300
    return float(np.sum(p[m] * np.log(p[m] / np.maximum(q[m], 1e-300))))


def peak(Ts, F):
    return float(Ts[np.argmax(F)])


# ---------------------------------------------------------------- Leg 1
def leg1():
    print("=" * 70)
    print("LEG 1 — 1D ring N=16, decimation: the EXACT anchor")
    print("=" * 70)
    # 1D Fisher peaks at low T: use a grid that contains the peak interior
    Ts = np.linspace(0.3, 3.0, 271)
    spins16, E16 = enumerate_ring(16)
    spins8, E8 = enumerate_ring(8)
    keep = np.arange(0, 16, 2)
    bits = ((spins16[:, keep] + 1) // 2).astype(np.int64)
    labels = (bits * (2 ** np.arange(8))).sum(1)

    # exact RG map: K = 1/T, tanh K' = tanh^2 K — with ANALYTIC derivative
    K = 1.0 / Ts
    t = np.tanh(K)
    Kp = np.arctanh(t ** 2)
    Tp = 1.0 / Kp
    dKp_dK = 2.0 * t * (1.0 - t ** 2) / (1.0 - t ** 4)
    # dT'/dT = (dT'/dK')(dK'/dK)(dK/dT) = (-1/K'^2)(dK'/dK)(-1/T^2)
    dTp = dKp_dK / (Kp ** 2 * Ts ** 2)

    # check the induced distribution IS the 8-ring at T'
    kls = [kl(induced(labels, E16, T, 256), boltzmann(E8, tp))
           for T, tp in zip(Ts[::40], Tp[::40])]
    print(f"  KL(induced || 8-ring at exact T')  max over T grid: "
          f"{max(kls):.3e}   (should be ~0)")

    F_c = channel_fisher_curve(labels, E16, Ts)
    F8_at = np.array([boltzmann(E8, tp) @ (E8 - boltzmann(E8, tp) @ E8) ** 2
                      / tp ** 4 for tp in Tp])
    F_pred = F8_at * dTp ** 2
    err = np.max(np.abs(F_c - F_pred) / F_c.max())
    p_full = peak(Ts, full_fisher_curve(E16, Ts))
    p_c, p_pred = peak(Ts, F_c), peak(Ts, F_pred)
    print(f"  composition law max relative error: {err:.3e}")
    print(f"  full 16-ring Fisher peak T* = {p_full:.2f}")
    print(f"  decimation-channel peak     = {p_c:.2f}   "
          f"composed prediction = {p_pred:.2f}   shift = {p_c - p_full:+.2f}")
    return dict(kl_max=float(max(kls)), law_max_rel_err=float(err),
                full_peak=p_full, channel_peak=p_c, predicted_peak=p_pred)


# ---------------------------------------------------------------- Leg 2
def majority_labels(spins, blocks):
    votes = []
    for b in blocks:
        s = spins[:, b].sum(1)
        v = np.sign(s)
        v[s == 0] = spins[s == 0][:, b[0]]  # tie -> block's first spin
        votes.append(((v + 1) // 2).astype(np.int64))
    votes = np.stack(votes, 1)
    return (votes * (2 ** np.arange(len(blocks)))).sum(1)


def fit_Tprime(labels, E, K, E_eff, Ts):
    """For each T, the min-KL effective temperature. For a 1-parameter
    exponential family the min-KL fit is exact moment matching:
    <E_eff>_{q(T')} = <E_eff>_{induced}, solved by bisection (monotone in
    T'), giving T'(T) smooth to machine precision — no grid quantization."""
    def mean_E_eff(t):
        return boltzmann(E_eff, t) @ E_eff
    def solve(target):
        lo, hi = 1e-2, 500.0
        if target <= mean_E_eff(lo):
            return lo
        if target >= mean_E_eff(hi):
            return hi
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if mean_E_eff(mid) < target:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    Tp, res = np.zeros(len(Ts)), np.zeros(len(Ts))
    for i, T in enumerate(Ts):
        p = induced(labels, E, T, K)
        Tp[i] = solve(p @ E_eff)
        res[i] = kl(p, boltzmann(E_eff, Tp[i]))
    return Tp, res


def leg2():
    print("\n" + "=" * 70)
    print("LEG 2 — 4x4 -> 2x2 majority rule: fitted RG map vs measured peak")
    print("=" * 70)
    spins, E = enumerate_lattice(4, 4)
    spins_eff, E_eff = enumerate_lattice(2, 2)
    site = lambda r, c: (r % 4) * 4 + (c % 4)
    geo = [np.array([site(r, c), site(r, c + 1), site(r + 1, c),
                     site(r + 1, c + 1)]) for r in (0, 2) for c in (0, 2)]
    rng = np.random.default_rng(20260723)
    F_full = full_fisher_curve(E, Ts)
    p_full = peak(Ts, F_full)
    print(f"  full-state Fisher peak T* = {p_full:.2f}")
    out = {}
    for name, blocks in [("geometric_2x2", geo),
                         ("random_blocks", [b for b in
                          rng.permutation(16).reshape(4, 4)])]:
        labels = majority_labels(spins, blocks)
        F_c = channel_fisher_curve(labels, E, Ts)
        p_c = peak(Ts, F_c)
        Tp, res = fit_Tprime(labels, E, 16, E_eff, Ts)
        dTp = np.gradient(Tp, Ts)
        F_eff_at = np.array([boltzmann(E_eff, tp) @
                             (E_eff - boltzmann(E_eff, tp) @ E_eff) ** 2
                             / tp ** 4 for tp in Tp])
        F_pred = F_eff_at * dTp ** 2
        p_pred = peak(Ts, F_pred)
        # KL residual in bits, worst over T; and law quality near the peaks
        res_bits = res / np.log(2)
        corr = float(np.corrcoef(F_c, F_pred)[0, 1])
        print(f"\n  [{name}]")
        print(f"    measured channel peak       = {p_c:.2f}  "
              f"(shift vs full: {p_c - p_full:+.2f})")
        print(f"    composed prediction peak    = {p_pred:.2f}  "
              f"(pred shift:   {p_pred - p_full:+.2f})")
        print(f"    |measured - predicted| peak = {abs(p_c - p_pred):.3f}")
        print(f"    effective-Ising fit residual: max {res_bits.max():.4f} "
              f"bits, at measured peak {res_bits[np.argmax(F_c)]:.4f} bits")
        print(f"    corr(F_c, F_pred) over T    = {corr:.4f}")
        out[name] = dict(channel_peak=p_c, predicted_peak=p_pred,
                         peak_mismatch=float(abs(p_c - p_pred)),
                         shift_measured=float(p_c - p_full),
                         shift_predicted=float(p_pred - p_full),
                         fit_residual_bits_max=float(res_bits.max()),
                         fit_residual_bits_at_peak=float(
                             res_bits[np.argmax(F_c)]),
                         curve_correlation=corr)
        np.savetxt(os.path.join(OUT, f"rg_{name}.csv"),
                   np.column_stack([Ts, F_c, F_pred, Tp, res_bits]),
                   delimiter=",",
                   header="T,F_channel,F_composed,T_eff_fit,KL_bits",
                   comments="")
    out["full_peak"] = p_full
    return out


def main():
    r1 = leg1()
    r2 = leg2()
    verdict = {
        "leg1_exact_anchor": r1,
        "leg2_majority_rule": r2,
        "composition_law_exact_where_RG_exact":
            bool(r1["law_max_rel_err"] < 1e-6),
        "geometric_peak_predicted":
            bool(r2["geometric_2x2"]["peak_mismatch"] <= 0.05),
        "random_blocks_peak_predicted":
            bool(r2["random_blocks"]["peak_mismatch"] <= 0.05),
    }
    with open(os.path.join(OUT, "rg_composition_verdict.json"), "w") as f:
        json.dump(verdict, f, indent=2)
    print("\n" + "=" * 70)
    print("VERDICT:", json.dumps({k: v for k, v in verdict.items()
                                  if not isinstance(v, dict)}, indent=2))
    print("=" * 70)


if __name__ == "__main__":
    main()
