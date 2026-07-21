"""Render the S23 result."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
c = np.load(os.path.join(OUT, "curves.npz"))
v = json.load(open(os.path.join(OUT, "verdict.json")))

fig, ax = plt.subplots(1, 3, figsize=(13.5, 4.3))
fig.suptitle("S23 — softmax attention IS one Bayesian update (a step of the universal update)",
             fontsize=12.5, fontweight="bold")

# Panel 1: exact weight match
ax[0].scatter(c["w_bayes"], c["w_attn"], s=14, color="#2a9d8f")
lim = max(c["w_bayes"].max(), c["w_attn"].max()) * 1.05
ax[0].plot([0, lim], [0, lim], "k--", lw=1)
ax[0].set_title("1. Exact match (norm-eq keys, σ²=√d)")
ax[0].set_xlabel("Bayes posterior weight  p(z=i|q)")
ax[0].set_ylabel("softmax attention weight")
ax[0].text(0.05, 0.92, f"max |Δ| = {v['part1_exact_match']['weight_max_abs_diff']:.1e}",
           transform=ax[0].transAxes, fontsize=9, color="#555")

# Panel 2: temperature = 1/sigma0^2
b, mse = c["betas"], c["mse"]
ax[1].semilogx(b, mse, "o-", color="#1f6f8b", ms=3, lw=1.6)
bstar = v["part2_temperature_is_eta"]["beta_star_theory_1_over_sigma0sq"]
ax[1].axvline(bstar, ls="--", color="#c1440e", lw=1.5)
ax[1].set_title("2. Attention temperature = η = 1/σ²")
ax[1].set_xlabel("attention inverse-temperature β")
ax[1].set_ylabel("prediction MSE")
ax[1].text(bstar * 1.1, mse.max() * 0.85, f"Bayes-optimal\nβ = 1/σ0² = {bstar}",
           color="#c1440e", fontsize=8)

# Panel 3: key-norm bias
ax[2].scatter(c["w_bayes3"], c["w_plain"], s=14, color="#e9a13b", label="plain attention (biased)")
ax[2].scatter(c["w_bayes3"], c["w_corr"], s=14, color="#2a9d8f", label="+ ‖k‖² correction (exact)")
lim3 = max(c["w_bayes3"].max(), c["w_plain"].max()) * 1.05
ax[2].plot([0, lim3], [0, lim3], "k--", lw=1)
ax[2].set_title("3. Key-norm bias (varying ‖k_i‖)")
ax[2].set_xlabel("Bayes posterior weight")
ax[2].set_ylabel("attention weight")
ax[2].legend(fontsize=8, loc="upper left")

for a in ax:
    a.grid(alpha=0.25)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(os.path.join(OUT, "s23_result.png"), dpi=130)
print("wrote", os.path.join(OUT, "s23_result.png"))
