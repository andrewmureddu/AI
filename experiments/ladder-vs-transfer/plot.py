"""Render the ladder-vs-transfer result."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
c = np.load(os.path.join(OUT, "curves.npz"))
grid = c["grid"]
skill = json.load(open(os.path.join(OUT, "verdict.json")))["transfer_skill_by_level"]

fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.4))
fig.suptitle("Does ladder level predict transfer?  A controlled cross-mechanism test",
             fontsize=12.5, fontweight="bold")

# Panel 1: standardized quantile curves — do B's aggregates match A's Gaussian shape?
colors = {"L4": "#2a9d8f", "L3": "#4c9f70", "L2": "#e9a13b", "L1": "#c1440e"}
ax[0].plot(grid, c["A(learned_Gaussian)"], "k--", lw=2, label="A: learned Gaussian law")
for name in ["L4", "L3", "L2", "L1"]:
    ax[0].plot(grid, c[name], color=colors[name], lw=2, label=f"{name} (skill {skill[name]:.2f})")
ax[0].set_title("Does B's aggregate collapse onto A's Gaussian?")
ax[0].set_xlabel("quantile")
ax[0].set_ylabel("robustly-standardized value")
ax[0].legend(fontsize=8, loc="upper left")
ax[0].text(0.02, -0.30, "L3/L4 hug the Gaussian (shared mechanism); L2/L1 peel off in the tails",
           transform=ax[0].transAxes, fontsize=8, color="#555")

# Panel 2: skill by level, cliff annotated
names = ["L1", "L2", "L3", "L4"]
vals = [skill[n] for n in names]
bars = ax[1].bar(names, vals, color=[colors[n] for n in names])
ax[1].axhline(0.5, ls=":", color="#888", lw=1)
ax[1].set_ylim(0, 1)
ax[1].set_title("Transfer skill by correspondence level")
ax[1].set_ylabel("transfer skill  (1 = A's law transfers)")
for n, v in zip(names, vals):
    ax[1].text(n, v, f"{v:.2f}", ha="center", va="bottom", fontsize=9)
# cliff marker between L2 and L3
ax[1].annotate("the cliff:\nappearance → mechanism\n(finite vs ∞ variance)",
               xy=(1.5, 0.5), xytext=(1.5, 0.20), ha="center", fontsize=8, color="#444",
               arrowprops=dict(arrowstyle="-|>", color="#444"))

for a in ax:
    a.grid(alpha=0.25)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(os.path.join(OUT, "ladder_transfer.png"), dpi=130)
print("wrote", os.path.join(OUT, "ladder_transfer.png"))
