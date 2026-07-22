"""Render s26_result.png from curves.npz + verdict.json."""
import numpy as np, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
z = np.load(os.path.join(OUT, "curves.npz"))
v = json.load(open(os.path.join(OUT, "verdict.json")))
steps, losses, lam, lam_sd = z["steps"], z["losses"], z["lam"], z["lam_sd"]
d, T_fit = int(z["d"]), int(z["T_fit"])

fig, ax = plt.subplots(1, 3, figsize=(14, 4.2))

# Leg A — SGLD vs exact localized functional vs asymptotic lambda
names = ["A1 linear d=5\n(regular)", "A2 y=abx\n(singular)", "A3 y=w²x\n(singular)"]
keys = list(v["legA_calibration"])
est = [v["legA_calibration"][k]["lambda_hat"] for k in keys]
exa = [v["legA_calibration"][k]["exact_localized"] for k in keys]
asy = [v["legA_calibration"][k]["lambda_theory"] for k in keys]
xs = np.arange(3)
ax[0].bar(xs - 0.22, exa, 0.2, label="exact functional (quadrature)", color="#2a6f97")
ax[0].bar(xs, est, 0.2, label="SGLD estimate", color="#61a5c2")
ax[0].bar(xs + 0.22, asy, 0.2, label="asymptotic λ", color="#c9762b")
ax[0].set_xticks(xs, names, fontsize=8)
ax[0].set_yscale("log")
ax[0].set_ylabel("λ")
ax[0].set_title("Leg A — sampler validated against S25 quadrature")
ax[0].legend(fontsize=8)

# Leg B — trajectory: loss and lambda_hat
mask = steps > 0
ax[1].plot(steps[mask], losses[mask], "o-", ms=3, color="#7b9e3e")
ax[1].set_xscale("log"); ax[1].set_yscale("log")
ax[1].set_xlabel("SGD step"); ax[1].set_ylabel("train loss (NLL/sample)")
ax[1].axvline(T_fit, color="gray", ls=":", lw=1)
ax[1].set_title("training loss (noise floor ≈ 0.5)")

good = lam > 0
ax[2].errorbar(steps[good & mask], lam[good & mask], yerr=lam_sd[good & mask],
               fmt="o-", ms=3, color="#2a6f97", label="local λ̂ (where valid)")
ax[2].axhline(d / 2, color="#c9762b", ls="--", label=f"regular d/2 = {d//2}")
ax[2].axhline(v["posthoc_fullbatch_lambda"], color="#61a5c2", ls=":",
              label=f"full-batch control λ̂ = {v['posthoc_fullbatch_lambda']}")
ax[2].axvline(T_fit, color="gray", ls=":", lw=1)
ax[2].set_xscale("log")
ax[2].set_xlabel("SGD step"); ax[2].set_ylabel("λ̂")
ax[2].set_title("λ̂ ≪ d/2 (P1 ✓) but drifts UP late (P3 ✗)")
ax[2].legend(fontsize=8)

fig.suptitle("S26 — the solution is singular, but SGD does not *seek* singularity", y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "s26_result.png"), dpi=150, bbox_inches="tight")
print("wrote s26_result.png")
