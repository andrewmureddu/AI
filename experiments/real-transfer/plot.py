"""Render the real-frontier result (both legs)."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
c = np.load(os.path.join(OUT, "curves.npz"), allow_pickle=True)
v = json.load(open(os.path.join(OUT, "verdict.json")))

fig, ax = plt.subplots(1, 3, figsize=(14, 4.4))
fig.suptitle("The real frontier — the prediction-field frame on data I did not construct",
             fontsize=12.5, fontweight="bold")

# Panel 1 — Leg A: invariance vs transfer on REAL diabetes data
inv, tr, nm = c["invA"], c["trA"], c["namesA"]
ax[0].scatter(inv, tr, s=40, color="#1f6f8b", zorder=3)
for i, name in enumerate(nm):
    ax[0].annotate(str(name), (inv[i], tr[i]), fontsize=8,
                   xytext=(4, 3), textcoords="offset points")
ax[0].axhline(0, color="#aaa", lw=1)
rho = v["legA_real_dataset"]["spearman_invariance_vs_transfer"]
ax[0].set_title(f"Leg A · REAL data (diabetes)\ninvariance ⇒ transfer,  ρ = {rho}")
ax[0].set_xlabel("invariance across age groups (train)")
ax[0].set_ylabel("transfer R² to held-out age group")

# Panel 2 — Leg B: first-digit distributions vs Benford
benford = c["benford"]
digits = np.arange(1, 10)
ax[1].plot(digits, benford, "k--o", lw=2, ms=5, label="Benford's law", zorder=5)
mech = ["2^n", "n!", "Fibonacci"]
ctrl = ["uniform[100,999]", "narrow lognormal"]
for m, col in zip(mech, ["#2a9d8f", "#4c9f70", "#3d8c68"]):
    ax[1].plot(digits, c[f"fd_{m}"], "-", color=col, alpha=0.9, label=m)
for m, col in zip(ctrl, ["#e9a13b", "#c1440e"]):
    ax[1].plot(digits, c[f"fd_{m}"], ":", color=col, lw=2, label=m)
ax[1].set_title("Leg B · Benford across computable domains")
ax[1].set_xlabel("leading digit")
ax[1].set_ylabel("frequency")
ax[1].set_xticks(digits)
ax[1].legend(fontsize=7.5)

# Panel 3 — Leg B: transfer skill per domain
per = v["legB_benford"]["per_domain"]
order = ["2^n", "3^n", "n!", "Fibonacci", "uniform[100,999]", "narrow lognormal"]
skills = [per[k]["transfer_skill"] for k in order]
cols = ["#2a9d8f" if per[k]["benford_mechanism"] else "#c1440e" for k in order]
ax[2].bar(range(len(order)), skills, color=cols)
ax[2].set_xticks(range(len(order)))
ax[2].set_xticklabels(order, rotation=40, ha="right", fontsize=7.5)
ax[2].set_ylim(0, 1.05)
ax[2].set_title("Leg B · transfer skill of the invariant\n(green = shares mechanism, red = control)")
ax[2].set_ylabel("Benford transfer skill")

for a in ax:
    a.grid(alpha=0.25)
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUT, "real_transfer.png"), dpi=130)
print("wrote", os.path.join(OUT, "real_transfer.png"))
