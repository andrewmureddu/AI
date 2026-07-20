"""Render the S18 result from sweep.csv + verdict.json."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
d = np.loadtxt(os.path.join(OUT, "sweep.csv"), delimiter=",", skiprows=1)
v = json.load(open(os.path.join(OUT, "verdict.json")))
al, inm, trm, inst = d[:, 0], d[:, 1], d[:, 2], d[:, 3]

fig, ax = plt.subplots(1, 3, figsize=(13.5, 4.2))
fig.suptitle("S18 — invariance measured on training environments predicts transfer "
             "to an unseen one", fontsize=12.5, fontweight="bold")

# Panel 1: the in-distribution vs transfer inversion
ax[0].plot(al, inm, color="#1f6f8b", lw=2, label="in-distribution error")
ax[0].plot(al, trm, color="#c1440e", lw=2, label="transfer error (unseen env)")
ax[0].set_title("The inversion")
ax[0].set_xlabel("predictor:  causal  →  spurious  (α)")
ax[0].set_ylabel("MSE")
ax[0].legend(fontsize=8, loc="upper left")
ax[0].text(0.02, -0.28, "spurious feature: best in-distribution, worst on transfer",
           transform=ax[0].transAxes, fontsize=8, color="#555")

# Panel 2: invariance (train-only) predicts transfer (test-only)
ax[1].scatter(inst, trm, c=al, cmap="viridis", s=28)
ax[1].set_title(f"Invariance ⇒ transfer   (Spearman ρ = {v['spearman_instability_vs_transfer']})")
ax[1].set_xlabel("coefficient instability across TRAIN envs")
ax[1].set_ylabel("transfer error on HELD-OUT env")

# Panel 3: ERM vs invariant-only vs spurious-only, on transfer
names = ["causal only\n(invariant)", "ERM\n(both)", "spurious\nonly"]
vals = [v["transfer_MSE_causal_only"], v["transfer_MSE_ERM_both"], v["transfer_MSE_spurious_only"]]
ax[2].bar(names, vals, color=["#2a9d8f", "#e9c46a", "#c1440e"])
ax[2].set_title("Transfer error by strategy")
ax[2].set_ylabel("transfer MSE (unseen env)")
for i, val in enumerate(vals):
    ax[2].text(i, val, f"{val:.2f}", ha="center", va="bottom", fontsize=9)

for a in ax:
    a.grid(alpha=0.25)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(os.path.join(OUT, "s18_result.png"), dpi=130)
print("wrote", os.path.join(OUT, "s18_result.png"))
