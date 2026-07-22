"""S7 — critical slowing down as a universal early-warning signal.

Claim under test (S7, plus essay 4's middle-zone prediction): slowing down
near a transition is one mechanism across domains — the relevant curvature
(Hessian of the potential / free energy, i.e. a face of grad^2 Phi) softens,
and the relaxation time is its inverse:

        tau * lambda_min  =  1        (domain-neutral law)

while HOW lambda_min vanishes with the control parameter is domain-specific
(different exponents). Three domains, one collapse test:

  A. Ecology-style saddle-node:  dx = (r + x^2)dt + sigma dW,  r -> 0^-.
     Linearized recovery rate lambda = 2*sqrt(-r)   (exponent 1/2 in -r).
  B. Mean-field Ising (Glauber/Langevin), T -> Tc^+ = 1:
     dm = (-m + tanh(m/T))dt + sigma dW,  lambda = 1 - 1/T (exponent 1 in T-Tc).
  C. Learning: full-batch GD on least squares as P/N -> 1 (interpolation
     threshold): convergence rate lambda = lr * lambda_min(X^T X / N),
     Marchenko-Pastur edge (1 - sqrt(P/N))^2  (exponent 2 in 1 - sqrt(g)).

In each: measure tau empirically (autocorrelation time for A/B, convergence
time for C), measure lambda independently, test tau*lambda = 1.
Pure numpy, deterministic. ~10 s.
"""
import json
import numpy as np

rng = np.random.default_rng(1)
DT, SIGMA, STEPS, BURN = 0.01, 0.03, 400_000, 40_000

def ar1_tau(z, dt):
    z = z - z.mean()
    rho = float(np.dot(z[:-1], z[1:]) / np.dot(z[:-1], z[:-1]))
    return -dt / np.log(rho)

def simulate(drift, x0, steps=STEPS):
    x = np.empty(steps); x[0] = x0
    noise = rng.normal(size=steps - 1) * SIGMA * np.sqrt(DT)
    for i in range(steps - 1):
        x[i + 1] = x[i] + drift(x[i]) * DT + noise[i]
    return x[BURN:]

results = {"A_saddle_node": [], "B_ising": [], "C_learning": []}

# ---- Leg A: saddle-node ----
for r in (-0.25, -0.16, -0.09, -0.04, -0.02):
    xstar = -np.sqrt(-r)
    lam = 2 * np.sqrt(-r)
    x = simulate(lambda z: r + z * z, xstar)
    tau = ar1_tau(x, DT)
    results["A_saddle_node"].append(
        {"r": r, "lambda": lam, "tau": tau, "tau_x_lambda": tau * lam})

# ---- Leg B: mean-field Ising above Tc ----
for T in (2.0, 1.5, 1.25, 1.1, 1.05):
    lam = 1 - 1 / T
    m = simulate(lambda z: -z + np.tanh(z / T), 0.0)
    tau = ar1_tau(m, DT)
    results["B_ising"].append(
        {"T": T, "lambda": lam, "tau": tau, "tau_x_lambda": tau * lam})

# ---- Leg C: GD on least squares near interpolation ----
N, lr, tol = 400, 0.1, 1e-6
for gamma in (0.3, 0.5, 0.7, 0.8, 0.9):
    P = int(gamma * N)
    X = rng.normal(size=(N, P)) / np.sqrt(N)
    w_star = rng.normal(size=P)
    y = X @ w_star
    H = X.T @ X
    lam_min = float(np.linalg.eigvalsh(H)[0])
    w = np.zeros(P)
    e0 = np.linalg.norm(w - w_star)
    it = 0
    err = e0
    while err > tol * e0 and it < 2_000_000:
        w -= lr * (H @ w - X.T @ y)
        err = np.linalg.norm(w - w_star)
        it += 1
    # error ~ exp(-lr*lam_min*it): tau (in iterations) from the actual decay
    tau_iters = it / np.log(e0 / err)
    lam_gd = lr * lam_min
    results["C_learning"].append(
        {"P_over_N": gamma, "lambda": lam_gd, "tau_iters": tau_iters,
         "tau_x_lambda": tau_iters * lam_gd,
         "mp_edge_theory": float((1 - np.sqrt(gamma)) ** 2),
         "lam_min_measured": lam_min})

# ---- collapse test: tau * lambda == 1 across all three domains ----
products = ([d["tau_x_lambda"] for d in results["A_saddle_node"]]
            + [d["tau_x_lambda"] for d in results["B_ising"]]
            + [d["tau_x_lambda"] for d in results["C_learning"]])
collapse = {"mean": float(np.mean(products)), "std": float(np.std(products)),
            "min": float(min(products)), "max": float(max(products))}

# ---- exponents differ (the anti-universality half of the verdict) ----
def slope(xs, ys):
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0])
expA = slope([-d["r"] for d in results["A_saddle_node"]],
             [d["tau"] for d in results["A_saddle_node"]])
expB = slope([d["T"] - 1 for d in results["B_ising"]],
             [d["tau"] for d in results["B_ising"]])
expC = slope([1 - np.sqrt(d["P_over_N"]) for d in results["C_learning"]],
             [d["tau_iters"] for d in results["C_learning"]])

verdict = {
    "collapse_tau_x_lambda": collapse,
    "collapse_holds": bool(0.8 < collapse["mean"] < 1.25 and collapse["std"] < 0.3),
    "exponents": {"A_theory": -0.5, "A_fit": expA,
                  "B_theory": -1.0, "B_fit": expB,
                  "C_theory": -2.0, "C_fit": expC},
    "detail": results,
}
print(json.dumps({k: verdict[k] for k in
                  ("collapse_tau_x_lambda", "collapse_holds", "exponents")},
                 indent=2))
with open("verdict.json", "w") as f:
    json.dump(verdict, f, indent=2)
