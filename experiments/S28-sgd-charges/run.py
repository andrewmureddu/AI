"""S28(iii) — are conserved charges the coordinates of SGD's stationary law?

Setup: two-layer linear network f(x) = v^T (W x) ... reduced here to the
scalar deep-linear case f(x) = u*v*x (the standard minimal model for scale
symmetry). The loss L(u,v) = E[(uvx - y)^2]/2 is invariant under
(u,v) -> (au, v/a): a continuous symmetry whose gradient-flow charge is
    Q = u^2 - v^2      (balancedness; Kunin et al. 2021).

Three legs:
  A. Gradient flow (tiny-lr full-batch GD): Q conserved?  Prediction: drift
     O(lr) per unit time -> ~machine-level for lr -> 0. (Conservation.)
  B. GD + weight decay lambda: broken conservation with EXACT predicted law
     dQ/dt = -4*lambda*Q  =>  Q(t) = Q0 * exp(-4*lambda*t).  (Predictive work.)
  C. SGD with label noise, no decay: is Q conserved under the ACTUAL noisy
     dynamics, and is the stationary law parameterized by the initial Q?
     Tower/GGE logic says: only charges of the actual dynamics survive; if
     noise breaks Q, the stationary law must FORGET initial Q (Q relaxes,
     thermalization), and naive S28(iii) sufficiency fails.

Pure numpy, deterministic seeds. ~seconds.
"""
import json
import numpy as np

rng = np.random.default_rng(0)

# data: y = w_true * x + noise at train time (label noise re-drawn per step in leg C)
w_true = 1.5
N = 200
x = rng.normal(size=N)
y_clean = w_true * x

def grad(u, v, xb, yb):
    r = u * v * xb - yb
    gu = np.mean(r * v * xb)
    gv = np.mean(r * u * xb)
    return gu, gv

# ---------------- Leg A: gradient flow conservation ----------------
def run_gd(u0, v0, lr, steps, lam=0.0):
    u, v = u0, v0
    Qs = [u * u - v * v]
    for _ in range(steps):
        gu, gv = grad(u, v, x, y_clean)
        u -= lr * (gu + 2 * lam * u)
        v -= lr * (gv + 2 * lam * v)
        Qs.append(u * u - v * v)
    return u, v, np.array(Qs)

legA = {}
for lr in (1e-2, 1e-3, 1e-4):
    T = 5.0                       # fixed physical time
    steps = int(T / lr)
    _, _, Qs = run_gd(1.7, 0.4, lr, steps)
    drift = float(abs(Qs[-1] - Qs[0]) / abs(Qs[0]))
    legA[f"lr={lr:g}"] = drift
# conservation confirmed if drift scales ~ linearly with lr (first-order breaking)
drifts = list(legA.values())
legA_ratio_1 = drifts[0] / drifts[1] if drifts[1] else float("inf")
legA_ratio_2 = drifts[1] / drifts[2] if drifts[2] else float("inf")

# ---------------- Leg B: broken conservation, exact law ----------------
lam = 0.05
lr = 1e-4
T = 20.0
_, _, Qs = run_gd(1.7, 0.4, lr, int(T / lr), lam=lam)
t = np.arange(len(Qs)) * lr
# fit exponent: Q(t) = Q0 exp(-k t)
mask = Qs > 0
k_fit = float(np.polyfit(t[mask], np.log(Qs[mask]), 1)[0] * -1)
k_theory = 4 * lam
legB = {"k_fit": k_fit, "k_theory": k_theory,
        "rel_err": float(abs(k_fit - k_theory) / k_theory)}

# ---------------- Leg C: SGD with label noise ----------------
def run_sgd(u0, v0, lr, steps, noise, batch, seed):
    r = np.random.default_rng(seed)
    u, v = u0, v0
    Qtrace, obs = [], []
    for s in range(steps):
        idx = r.integers(0, N, size=batch)
        yb = y_clean[idx] + noise * r.normal(size=batch)
        gu, gv = grad(u, v, x[idx], yb)
        u -= lr * gu
        v -= lr * gv
        if s >= steps // 2:                     # stationary half
            Qtrace.append(u * u - v * v)
            obs.append((u * v, u * u + v * v))  # product (function fit) and norm
    return np.array(Qtrace), np.array(obs)

# inits: same product uv (same function), very different initial Q
inits = {"Q0=+2.73": (1.7, 0.4), "Q0=0.00": (np.sqrt(0.68), np.sqrt(0.68)),
         "Q0=-2.73": (0.4, 1.7)}
lr, steps, noise, batch = 5e-3, 40000, 0.5, 8
legC = {}
for name, (u0, v0) in inits.items():
    Qt, obs = [], []
    for seed in range(8):
        q, o = run_sgd(u0, v0, lr, steps, noise, batch, seed)
        Qt.append(q); obs.append(o)
    Qt = np.concatenate(Qt); obs = np.concatenate(obs)
    legC[name] = {"Q0": float(u0**2 - v0**2),
                  "Q_stationary_mean": float(Qt.mean()),
                  "Q_stationary_std": float(Qt.std()),
                  "norm_stationary_mean": float(obs[:, 1].mean())}

# does the stationary law remember init Q?  compare stationary Q means across
# init groups relative to their spread
means = [legC[k]["Q_stationary_mean"] for k in legC]
stds = [legC[k]["Q_stationary_std"] for k in legC]
separation = float((max(means) - min(means)) / np.mean(stds))
forgets_Q0 = bool(separation < 0.5)   # groups indistinguishable => forgot Q0
relaxed_to_balanced = bool(all(abs(m) < 0.2 * 2.73 for m in means))

# sufficiency check: on the minimum manifold uv = w_true, the stationary norm
# is DETERMINED by the charge:  u^2+v^2 = sqrt(Q^2 + 4 w_true^2).
suff = {}
for name in legC:
    Qm = legC[name]["Q_stationary_mean"]
    pred = float(np.sqrt(Qm**2 + 4 * w_true**2))
    obs_ = legC[name]["norm_stationary_mean"]
    suff[name] = {"predicted_norm_from_charge": pred, "observed_norm": obs_,
                  "rel_err": float(abs(pred - obs_) / obs_)}
suff_ok = bool(all(v["rel_err"] < 0.01 for v in suff.values()))

# slow drift: rate at which SGD discretization/label noise erodes the charge
q0, qT = 2.73, legC["Q0=+2.73"]["Q_stationary_mean"]
k_sgd = float(-np.log(qT / q0) / steps)          # per-step decay rate
quasi_window = float(1.0 / k_sgd)                # steps until O(1) erosion

verdict = {
    "sufficiency_norm_eq_f_of_charge": suff,
    "sufficiency_confirmed": suff_ok,
    "sgd_charge_decay_per_step": k_sgd,
    "quasi_conservation_window_steps": quasi_window,
    "legA_drift_by_lr": legA,
    "legA_drift_ratio_lr10x": [legA_ratio_1, legA_ratio_2],
    "legA_conserved_in_flow_limit": bool(legA_ratio_1 > 5 and legA_ratio_2 > 5),
    "legB_broken_conservation_law": legB,
    "legB_exact_law_confirmed": bool(legB["rel_err"] < 0.05),
    "legC_stationary_by_init": legC,
    "legC_separation_over_spread": separation,
    "legC_stationary_law_forgets_Q0": forgets_Q0,
    "legC_Q_relaxes_toward_balance": relaxed_to_balanced,
}
print(json.dumps(verdict, indent=2))
with open("verdict.json", "w") as f:
    json.dump(verdict, f, indent=2)
