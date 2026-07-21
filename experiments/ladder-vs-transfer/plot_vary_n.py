"""Render transfer-skill-vs-n."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
v = json.load(open(os.path.join(OUT, "vary_n_verdict.json")))
n = np.array(v["n_values"])

# finite-sample ceiling: a fresh Gaussian sample vs the Gaussian reference
GRID = np.linspace(0.02, 0.98, 97)
def rshape(x):
    m = np.median(x); q1, q3 = np.percentile(x, [25, 75]); return np.quantile((x - m) / (q3 - q1), GRID)
ref = rshape(np.random.default_rng(0).normal(0, 1, 400000))
dref = float(np.mean(np.abs(ref - rshape(np.random.default_rng(1).standard_t(1.5, 400000)))))
ceiling = 1 - float(np.mean(np.abs(rshape(np.random.default_rng(5).normal(0, 1, 3000)) - ref))) / dref

fig, ax = plt.subplots(figsize=(8.2, 5.0))
colors = {"L4": "#2a9d8f", "L3": "#4c9f70", "L2": "#e9a13b", "L1": "#c1440e"}
for L in ["L4", "L3", "L2", "L1"]:
    ax.plot(n, v[f"skill_{L}"], "o-", color=colors[L], lw=2, ms=4, label=L)

ax.fill_between(n, v["skill_L2"], v["skill_L3"], color="#888", alpha=0.12)
ax.axhline(ceiling, ls="--", color="#555", lw=1)
ax.text(n[-1], ceiling + 0.01, f"finite-sample ceiling ≈ {ceiling:.2f} (= full transfer)",
        ha="right", va="bottom", fontsize=8, color="#555")
ax.text(n[3], 0.52, "L2 plateaus ~0.5\n(→ α-stable, never Gaussian)", fontsize=8, color="#9a6a1a")
ax.text(6, 0.44, "the cliff\n(L2/L3 gap)", fontsize=8, color="#444")

ax.set_xscale("log", base=2)
ax.set_xticks(n); ax.set_xticklabels(n)
ax.set_ylim(0, 1)
ax.set_xlabel("n  =  contributions per aggregate")
ax.set_ylabel("transfer skill  (1 = Gaussian invariant transfers)")
ax.set_title("Transfer skill vs n: finite-variance levels reach the ceiling,\n"
             "the infinite-variance level (L2) saturates far below it",
             fontsize=12, fontweight="bold")
ax.legend(title="level", fontsize=9)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "vary_n.png"), dpi=130)
print("wrote", os.path.join(OUT, "vary_n.png"), "| ceiling", round(ceiling, 3))
