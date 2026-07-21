"""Render the S3 results to a PNG from the saved CSVs."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
ising = np.loadtxt(os.path.join(OUT, "ising.csv"), delimiter=",", skiprows=1)
dd = np.loadtxt(os.path.join(OUT, "double_descent.csv"), delimiter=",", skiprows=1)

fig, ax = plt.subplots(1, 3, figsize=(13.5, 4.2))
fig.suptitle("S3 — a Fisher / statistical-curvature spike marks a phase transition, "
             "in physics and in learning", fontsize=12.5, fontweight="bold")

# Leg B: Ising susceptibility = Fisher info for the field
T, m, chi = ising[:, 0], ising[:, 1], ising[:, 2]
ax[0].semilogy(T, chi, color="#c1440e", lw=2)
ax[0].axvline(1.0, ls="--", color="#555", lw=1)
ax[0].set_title("Physics: mean-field Ising")
ax[0].set_xlabel("temperature  T")
ax[0].set_ylabel("Fisher info  χ = Var(M)/T   (log)")
ax[0].text(1.02, chi.max() * 0.3, "T_c", color="#555")

# Leg A: double descent test error
r, mse, invF = dd[:, 0], dd[:, 1], dd[:, 2]
ax[1].plot(r, mse, color="#1f6f8b", lw=2)
ax[1].axvline(1.0, ls="--", color="#555", lw=1)
ax[1].set_title("Learning: double descent")
ax[1].set_xlabel("capacity  P / N")
ax[1].set_ylabel("test error (MSE)")
ax[1].text(1.03, mse.max() * 0.9, "interpolation\nthreshold", color="#555", fontsize=8)

# Leg A: inverse-Fisher blow-up, same axis location
ax[2].semilogy(r, invF, color="#6a4c93", lw=2)
ax[2].axvline(1.0, ls="--", color="#555", lw=1)
ax[2].set_title("Learning: Fisher goes singular")
ax[2].set_xlabel("capacity  P / N")
ax[2].set_ylabel("inverse-Fisher  1/σ_min²   (log)")

for a in ax:
    a.grid(alpha=0.25)
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(os.path.join(OUT, "s3_result.png"), dpi=130)
print("wrote", os.path.join(OUT, "s3_result.png"))
