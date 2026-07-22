"""
S25 test — channel-independence of the prediction field's singularities.

Do different measurement channels on the same system agree on WHERE the
Fisher metric degenerates? The data-processing inequality forces channel
Fisher curves to differ in MAGNITUDE (F_c <= F_full); the strong reading
of PREDICTION-FIELD.md predicts the PEAK LOCATION is invariant for
generic channels, with blind channels deviating only by carrying ~zero
information.

  Leg A: 4x4 periodic Ising, exact enumeration (2^16 states). A channel
     is a deterministic map c on states; the induced Fisher w.r.t. T is
     exact: for Boltzmann p(s|T), d/dT log p_c(y|T) = (E[E|y] - <E>)/T^2,
     so F_c(T) = Var_y( E[energy | c(s)=y] ) / T^4.  No sampling, no
     finite differences.

  Leg B: the S3 ridgeless random-feature regressor. A channel is a probe
     distribution over inputs; measured curve = test MSE under that probe
     as P/N sweeps through the interpolation threshold.

Pure numpy, deterministic (seeded). Outputs CSVs + verdict.json.
Pass/fail criteria are fixed in README.md (written before this file).
"""
import numpy as np
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20260721)

# ----------------------------------------------------------------------
# Leg A: exact Ising enumeration
# ----------------------------------------------------------------------
def enumerate_ising(L=4):
    """All 2^(L*L) states of a periodic LxL Ising lattice: spins (S, n)
    in {-1,+1} and energies E = -sum_<ij> s_i s_j."""
    n = L * L
    idx = np.arange(2 ** n, dtype=np.uint32)
    spins = ((idx[:, None] >> np.arange(n)) & 1).astype(np.int8) * 2 - 1
    site = lambda r, c: (r % L) * L + (c % L)
    E = np.zeros(2 ** n, dtype=np.int32)
    for r in range(L):
        for c in range(L):
            i = site(r, c)
            E -= spins[:, i].astype(np.int32) * (
                spins[:, site(r, c + 1)] + spins[:, site(r + 1, c)]
            )
    return spins, E.astype(np.float64)


def channel_fisher(labels, E, Ts):
    """Exact Fisher info of the induced distribution p_c(y|T) w.r.t. T.
    labels: integer channel output per state. Returns F_c(T) and the
    total information integral sum_T F_c dT (crude trapezoid)."""
    labels = np.asarray(labels)
    K = labels.max() + 1
    F = np.zeros(len(Ts))
    for t, T in enumerate(Ts):
        w = np.exp(-(E - E.min()) / T)
        w /= w.sum()
        p_y = np.bincount(labels, weights=w, minlength=K)
        Ey = np.bincount(labels, weights=w * E, minlength=K)
        mean_E = w @ E
        cond = np.divide(Ey, p_y, out=np.full(K, mean_E), where=p_y > 1e-300)
        F[t] = (p_y @ (cond - mean_E) ** 2) / T ** 4
    total = np.trapezoid(F, Ts)
    return F, total


def make_channels(spins, rng):
    """Return dict name -> (labels, family). family in
    {'full','natural','generic','control'}."""
    n = spins.shape[1]
    ch = {}
    M = spins.sum(1)
    ch["full_state"] = (np.arange(len(spins)), "full")
    ch["abs_magnetization"] = ((np.abs(M) // 2).astype(int), "natural")
    # energy channel: label = rank of distinct energy value
    ch["energy"] = (None, "natural")  # filled by caller with E
    # generic: subset magnetization (value of sum over k random spins)
    for k in (2, 4, 8):
        for j in range(2):
            S = rng.choice(n, size=k, replace=False)
            ch[f"subset_mag_k{k}_{j}"] = (((spins[:, S].sum(1) + k) // 2), "generic")
    # generic: random k-bucket hash of a random 8-spin subset
    for j in range(6):
        S = rng.choice(n, size=8, replace=False)
        cfg = ((spins[:, S] + 1) // 2 * (2 ** np.arange(8))).sum(1)
        table = rng.integers(0, 8, size=256)
        ch[f"hash8_{j}"] = (table[cfg], "generic")
    # generic: majority vote on a random partition into 4 blocks of 4
    for j in range(4):
        perm = rng.permutation(n).reshape(4, 4)
        votes = np.stack([np.sign(spins[:, b].sum(1)) for b in perm], 1) + 1
        ch[f"block_majority_{j}"] = ((votes * 3 ** np.arange(4)).sum(1), "generic")
    # generic: |a . s| quantile-binned into 8 bins (even channel)
    for j in range(4):
        a = rng.normal(size=n)
        v = np.abs(spins @ a)
        edges = np.quantile(v, np.linspace(0, 1, 9)[1:-1])
        ch[f"abs_linear_{j}"] = (np.searchsorted(edges, v), "generic")
    # controls: blind by symmetry at h=0
    ch["single_spin"] = (((spins[:, 0] + 1) // 2), "control")
    ch["parity"] = ((((spins + 1) // 2).sum(1) % 2), "control")
    ch["sign_M"] = ((np.sign(M) > 0).astype(int), "control")
    return ch


def leg_A(L=4, Ts=np.linspace(1.5, 3.5, 81)):
    spins, E = enumerate_ising(L)
    ch = make_channels(spins, RNG)
    # energy channel labels from distinct energy values
    _, e_labels = np.unique(E, return_inverse=True)
    ch["energy"] = (e_labels, "natural")
    results = {}
    for name, (labels, family) in ch.items():
        F, total = channel_fisher(labels, E, Ts)
        peak_T = float(Ts[np.argmax(F)]) if F.max() > 1e-12 else float("nan")
        results[name] = dict(family=family, peak_T=peak_T,
                             total_info=float(total), Fmax=float(F.max()))
        print(f"  {name:22s} [{family:7s}]  peak T* = "
              f"{('%.3f' % peak_T) if peak_T == peak_T else '  --  '}   "
              f"integrated info = {total:10.4f}")
    curves = {name: channel_fisher(labels, E, Ts)[0]
              for name, (labels, family) in ch.items()}
    header = "T," + ",".join(curves)
    np.savetxt(os.path.join(OUT, "legA_fisher_curves.csv"),
               np.column_stack([Ts] + list(curves.values())),
               delimiter=",", header=header, comments="")
    return results, Ts


# ----------------------------------------------------------------------
# Leg B: double descent probed through different channels
# ----------------------------------------------------------------------
def leg_B(D=128, N=40, Nprobe=600, noise=0.15, Pmax=140, seeds=10):
    Ps = np.arange(2, Pmax + 1, 2)
    ratio = Ps / N
    # channel = probe input distribution; T-independent, fixed up front
    probes = {"iid_natural": ("natural", np.eye(D))}
    for j in range(6):
        s = np.exp(RNG.normal(0, 1, size=D))
        probes[f"diag_lognormal_{j}"] = ("generic", np.diag(s / s.mean()))
    for j in range(4):
        Q = np.linalg.qr(RNG.normal(size=(D, D)))[0]
        spec = np.arange(1, D + 1) ** -1.0
        probes[f"rot_powerlaw_{j}"] = ("generic", Q @ np.diag(spec / spec.mean()) @ Q.T)
    for d in (4, 16, 64):
        for j in range(2):
            U = np.linalg.qr(RNG.normal(size=(D, d)))[0]
            probes[f"slice_d{d}_{j}"] = ("generic", U @ U.T * (D / d))
    mse = {k: np.zeros((seeds, len(Ps))) for k in probes}
    mse["train_span"] = np.zeros((seeds, len(Ps)))  # adversarial control
    for s in range(seeds):
        rng = np.random.default_rng(1000 + s)
        beta = rng.normal(size=D) / np.sqrt(D)
        X = rng.normal(size=(N, D))
        y = X @ beta + noise * rng.normal(size=N)
        R = rng.normal(size=(D, Pmax)) / np.sqrt(D)
        probe_X = {}
        for name, (fam, C) in probes.items():
            Lc = np.linalg.cholesky(C + 1e-10 * np.eye(D))
            probe_X[name] = rng.normal(size=(Nprobe, D)) @ Lc.T
        # adversarial: probes confined to the span of the training inputs
        A = rng.normal(size=(Nprobe, N)) / np.sqrt(N)
        probe_X["train_span"] = A @ X
        for j, P in enumerate(Ps):
            Phi = X @ R[:, :P]
            w, *_ = np.linalg.lstsq(Phi, y, rcond=None)
            for name, Xp in probe_X.items():
                pred = (Xp @ R[:, :P]) @ w
                mse[name][s, j] = np.mean((pred - Xp @ beta) ** 2)
    results = {}
    for name in mse:
        fam = "control" if name == "train_span" else probes[name][0]
        curve = mse[name].mean(0)
        pk = float(ratio[np.argmax(curve)])
        results[name] = dict(family=fam, peak_ratio=pk,
                             peak_mse=float(curve.max()))
        print(f"  {name:22s} [{fam:7s}]  peak at P/N = {pk:.3f}   "
              f"peak MSE = {curve.max():9.3f}")
    header = "P_over_N," + ",".join(mse)
    np.savetxt(os.path.join(OUT, "legB_mse_curves.csv"),
               np.column_stack([ratio] + [mse[k].mean(0) for k in mse]),
               delimiter=",", header=header, comments="")
    return results


# ----------------------------------------------------------------------
def main():
    print("=" * 70)
    print("LEG A — exact 4x4 Ising: channel Fisher curves F_c(T)")
    print("=" * 70)
    resA, Ts = leg_A()
    full_peak = resA["full_state"]["peak_T"]
    nat_info = np.median([r["total_info"] for r in resA.values()
                          if r["family"] == "natural"])
    gen = {k: r for k, r in resA.items() if r["family"] == "generic"}
    # a generic channel counts as non-degenerate if within 10x of natural info
    live = {k: r for k, r in gen.items() if r["total_info"] > nat_info / 10}
    devs = {k: abs(r["peak_T"] - full_peak) for k, r in live.items()}
    ctrl_max_info = max(r["total_info"] for r in resA.values()
                       if r["family"] == "control")
    print(f"\n  full-state peak T* = {full_peak:.3f}")
    print(f"  generic channels: {len(gen)} total, {len(live)} non-degenerate "
          f"(info within 10x of natural median {nat_info:.3f})")
    print(f"  max |peak deviation| among non-degenerate generics = "
          f"{max(devs.values()):.3f}  (tolerance 0.15)")
    print(f"  worst offender: {max(devs, key=devs.get)}")
    print(f"  control channels' max integrated info = {ctrl_max_info:.2e} "
          f"(natural median {nat_info:.3f})")

    print("\n" + "=" * 70)
    print("LEG B — double descent probed through channels")
    print("=" * 70)
    resB = leg_B()
    genB = {k: r for k, r in resB.items() if r["family"] == "generic"}
    devB = {k: abs(r["peak_ratio"] - 1.0) for k, r in genB.items()}
    print(f"\n  max |P/N peak - 1| among generic probes = {max(devB.values()):.3f}"
          f"  (tolerance 0.10)")
    print(f"  adversarial train-span probe peak: "
          f"{resB['train_span']['peak_ratio']:.3f}, "
          f"peak MSE {resB['train_span']['peak_mse']:.3f} vs natural "
          f"{resB['iid_natural']['peak_mse']:.3f}")

    n_out_A = sum(d > 0.15 for d in devs.values())
    n_out_B = sum(d > 0.10 for d in devB.values())
    verdict = {
        "legA_full_state_peak_T": full_peak,
        "legA_n_generic": len(gen),
        "legA_n_nondegenerate": len(live),
        "legA_max_peak_deviation": float(max(devs.values())),
        "legA_generics_outside_tolerance": int(n_out_A),
        "legA_controls_info_ratio_vs_natural": float(ctrl_max_info / nat_info),
        "legB_max_peak_deviation": float(max(devB.values())),
        "legB_generics_outside_tolerance": int(n_out_B),
        "legB_trainspan_peak_mse_ratio": float(
            resB["train_span"]["peak_mse"] / resB["iid_natural"]["peak_mse"]),
        "PASS": bool(n_out_A <= 2 and n_out_B <= 2
                     and ctrl_max_info / nat_info < 0.1),
        "channels": {"legA": resA, "legB": resB},
    }
    with open(os.path.join(OUT, "verdict.json"), "w") as f:
        json.dump(verdict, f, indent=2)
    print("\n" + "=" * 70)
    print("VERDICT:", json.dumps({k: v for k, v in verdict.items()
                                  if k != "channels"}, indent=2))
    print("=" * 70)


if __name__ == "__main__":
    main()
