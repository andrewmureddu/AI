"""Render s25_result.png from curves.npz + verdict.json."""
import numpy as np, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
z = np.load(os.path.join(OUT, "curves.npz"))
v = json.load(open(os.path.join(OUT, "verdict.json")))
Ps, lam, th, Gs, T = z["Ps"], z["lambda_hat"], z["lambda_theory"], z["n_gen"], z["shift_T"]
D = 20

fig, ax = plt.subplots(1, 3, figsize=(14, 4.2))

# Leg A — estimated vs exact lambda
names = ["M1 y=wx\n(regular)", "M2 y=abx\n(singular)", "M3 y=w²x\n(singular)"]
est = [v["legA_estimator"][k]["lambda_hat"] for k in v["legA_estimator"]]
theo = [v["legA_estimator"][k]["lambda_theory"] for k in v["legA_estimator"]]
dh = [v["legA_estimator"][k]["d_half"] for k in v["legA_estimator"]]
xs = np.arange(3)
ax[0].bar(xs - 0.22, theo, 0.2, label="RLCT theory", color="#2a6f97")
ax[0].bar(xs, est, 0.2, label="estimated", color="#61a5c2")
ax[0].bar(xs + 0.22, dh, 0.2, label="naive d/2", color="#c9762b")
ax[0].set_xticks(xs, names, fontsize=8)
ax[0].set_ylabel("learning coefficient λ")
ax[0].set_title("Leg A — estimator vs exact RLCT")
ax[0].legend(fontsize=8)

# Leg B — lambda(P) kink
ax[1].plot(Ps, Ps / 2, "--", color="#c9762b", label="naive d/2 = P/2")
ax[1].plot(Ps, th, "-", color="#2a6f97", lw=2, label="RLCT: min(P,D)/2")
ax[1].plot(Ps, lam, "o", ms=4, color="#61a5c2", label="estimated λ̂(P)")
ax[1].axvline(D, color="gray", ls=":", lw=1)
ax[1].text(D + 0.5, 25, "P = D\n(Fisher metric\ndegenerates)", fontsize=8, color="gray")
ax[1].set_xlabel("feature count P (D = 20)")
ax[1].set_ylabel("λ")
ax[1].set_title("Leg B — λ kinks flat at the singular point")
ax[1].legend(fontsize=8)

# Leg C — generalization + transfer track lambda
ax[2].plot(Ps, Gs, "o-", ms=3, color="#2a6f97", label="n · Bayes excess risk (in-dist)")
ax2 = ax[2].twinx()
ax2.plot(Ps, T, "s-", ms=3, color="#7b9e3e", label="shift excess risk (transfer)")
ax[2].axvline(D, color="gray", ls=":", lw=1)
ax[2].set_xlabel("feature count P")
ax[2].set_ylabel("n · excess risk", color="#2a6f97")
ax2.set_ylabel("transfer excess risk", color="#7b9e3e")
ax[2].set_title("Leg C — both plateau with λ, not with P")
h1, l1 = ax[2].get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax[2].legend(h1 + h2, l1 + l2, fontsize=8, loc="lower right")

fig.suptitle("S25 — the learning coefficient (RLCT) charts the prediction field at its singularities", y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "s25_result.png"), dpi=150, bbox_inches="tight")
print("wrote s25_result.png")
