"""
S3 test — does a Fisher / statistical-curvature quantity spike at a phase
transition, in BOTH a thermodynamic system and a learning system?

We test the claim on two exactly-computable phase transitions (grokking itself
needs GPU-scale compute and is left open; see README):

  Leg B (physics anchor): mean-field Ising. The Fisher information for the
     external field h equals the magnetic susceptibility chi = dm/dh, which
     equals Var(magnetization)/T. Prediction: chi -> infinity at T_c = 1.

  Leg A (learning, the novel claim): ridgeless random-feature regression.
     For a linear model y = Phi w + noise, the Fisher information matrix is
     F = Phi^T Phi / sigma^2. At the interpolation threshold P = N the Gram
     matrix goes singular, so the worst-direction inverse-Fisher variance
     1/sigma_min^2 blows up. Prediction: this blow-up coincides exactly with
     the double-descent test-error peak.

Pure numpy, deterministic (seeded). Outputs CSVs + an ASCII summary.
"""
import numpy as np
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------------
# Leg B: mean-field Ising -- Fisher info for the field = susceptibility
# ----------------------------------------------------------------------
def ising_susceptibility(Ts):
    """Solve m = tanh(m/T) (J=1, T_c=1); return magnetization m and
    susceptibility chi = beta(1-m^2)/(1 - beta(1-m^2)) = Fisher info for h."""
    ms, chis = [], []
    for T in Ts:
        beta = 1.0 / T
        # fixed-point iterate; start off-zero so the ordered branch is found for T<1
        m = 0.9
        for _ in range(20000):
            m_new = np.tanh(m / T)
            if abs(m_new - m) < 1e-14:
                m = m_new
                break
            m = m_new
        denom = 1.0 - beta * (1.0 - m * m)
        chi = beta * (1.0 - m * m) / denom if abs(denom) > 1e-12 else np.inf
        ms.append(m)
        chis.append(abs(chi))
    return np.array(ms), np.array(chis)


# ----------------------------------------------------------------------
# Leg A: double descent + Fisher singularity
# ----------------------------------------------------------------------
def double_descent(D=128, N=40, Ntest=1000, noise=0.15, Pmax=140, seeds=25):
    Ps = np.arange(2, Pmax + 1, 2)
    test_mse = np.zeros((seeds, len(Ps)))
    inv_fisher = np.zeros((seeds, len(Ps)))  # 1/sigma_min^2 of normalized features
    for s in range(seeds):
        rng = np.random.default_rng(1000 + s)
        beta = rng.normal(size=D) / np.sqrt(D)          # teacher
        X = rng.normal(size=(N, D))
        Xt = rng.normal(size=(Ntest, D))
        y = X @ beta + noise * rng.normal(size=N)
        yt = Xt @ beta                                   # clean test target
        R = rng.normal(size=(D, Pmax)) / np.sqrt(D)      # nested random features
        for j, P in enumerate(Ps):
            Phi = X @ R[:, :P]                           # (N, P)
            Phit = Xt @ R[:, :P]
            # min-norm / least-squares solution (handles both P<N and P>N)
            w, *_ = np.linalg.lstsq(Phi, y, rcond=None)
            pred = Phit @ w
            test_mse[s, j] = np.mean((pred - yt) ** 2)
            # Fisher geometry: singular values of features scaled by 1/sqrt(N)
            sv = np.linalg.svd(Phi / np.sqrt(N), compute_uv=False)
            smin = sv.min()
            inv_fisher[s, j] = 1.0 / (smin ** 2 + 1e-30)
    return Ps / N, test_mse.mean(0), np.median(inv_fisher, 0)


# ----------------------------------------------------------------------
# tiny ASCII plot
# ----------------------------------------------------------------------
def ascii_plot(x, y, label, width=60, height=12, logy=False):
    y = np.asarray(y, float)
    yy = np.log10(y + 1e-30) if logy else y.copy()
    lo, hi = np.nanmin(yy), np.nanmax(yy)
    hi = hi if hi > lo else lo + 1
    grid = [[" "] * width for _ in range(height)]
    xi = ((x - x.min()) / (x.max() - x.min()) * (width - 1)).astype(int)
    yi = ((yy - lo) / (hi - lo) * (height - 1)).astype(int)
    for a, b in zip(xi, yi):
        grid[height - 1 - b][a] = "*"
    peak = int(np.nanargmax(y))
    px = int((x[peak] - x.min()) / (x.max() - x.min()) * (width - 1))
    for r in range(height):
        if grid[r][px] == " ":
            grid[r][px] = "|"
    top = f"{'log10 ' if logy else ''}{label}  (peak at x={x[peak]:.3f})"
    body = "\n".join("".join(r) for r in grid)
    axis = f"x: {x.min():.2f} .. {x.max():.2f}   (| marks peak)"
    return f"{top}\n{body}\n{axis}"


def main():
    print("=" * 68)
    print("LEG B — mean-field Ising: Fisher info for field h (= susceptibility)")
    print("=" * 68)
    Ts = np.linspace(0.30, 2.0, 120)
    m, chi = ising_susceptibility(Ts)
    ic = int(np.argmax(chi))
    print(ascii_plot(Ts, chi, "Fisher info chi(T)", logy=True))
    print(f"Peak susceptibility at T = {Ts[ic]:.3f}  (theory: T_c = 1.000)")
    print(f"chi rises from ~{chi[0]:.2f} (T={Ts[0]:.2f}) to {chi[ic]:.1f} near T_c\n")
    np.savetxt(os.path.join(OUT, "ising.csv"),
               np.column_stack([Ts, m, chi]), delimiter=",",
               header="T,magnetization,fisher_info_chi", comments="")

    print("=" * 68)
    print("LEG A — double descent: Fisher singularity vs generalization")
    print("=" * 68)
    ratio, mse, invF = double_descent()
    pk_mse = int(np.argmax(mse))
    pk_F = int(np.argmax(invF))
    print(ascii_plot(ratio, mse, "test MSE"))
    print()
    print(ascii_plot(ratio, invF, "inverse-Fisher scale 1/sigma_min^2", logy=True))
    print(f"\ntest-error peak at P/N = {ratio[pk_mse]:.3f}")
    print(f"inverse-Fisher peak at P/N = {ratio[pk_F]:.3f}   (theory: 1.000)")
    np.savetxt(os.path.join(OUT, "double_descent.csv"),
               np.column_stack([ratio, mse, invF]), delimiter=",",
               header="P_over_N,test_mse,inverse_fisher_scale", comments="")

    verdict = {
        "ising_chi_peak_T": float(Ts[ic]),
        "ising_Tc_theory": 1.0,
        "dd_testerr_peak_ratio": float(ratio[pk_mse]),
        "dd_fisher_peak_ratio": float(ratio[pk_F]),
        "dd_peaks_coincide": bool(abs(ratio[pk_mse] - ratio[pk_F]) <= 0.10),
    }
    with open(os.path.join(OUT, "verdict.json"), "w") as f:
        json.dump(verdict, f, indent=2)
    print("\n" + "=" * 68)
    print("VERDICT:", json.dumps(verdict))
    print("=" * 68)


if __name__ == "__main__":
    main()
