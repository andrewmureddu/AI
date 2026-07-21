"""
S23 — attention IS the universal update (one Bayesian step).

Claim: softmax attention output = the posterior-predictive mean of a Bayesian
retrieval over memories, i.e. one step of entropic mirror descent (S1's
x_i ∝ x_i·exp(−η g_i)) with:
    prior  x_i = 1/N (uniform),
    loss   g_i = ½‖q − k_i‖²   (squared distance = surprise),
    step   η   = 1/σ²           (= the attention temperature).

Derivation checked numerically in three parts:
  1. EXACT equivalence: with norm-equalized keys and σ²=√d, softmax-attention
     weights equal the Bayes posterior p(z=i|q) to machine precision, and the
     outputs coincide.
  2. TEMPERATURE = 1/σ²: sweeping the attention inverse-temperature β, prediction
     MSE is minimised at β = 1/σ0² (the true noise precision) — the Bayes-optimal
     value. So attention temperature is literally the update's η.
  3. KEY-NORM BIAS (honest nuance): with non-equalized keys, plain dot-product
     attention deviates from the exact posterior by exactly the ‖k_i‖²/2σ² term;
     adding that correction restores the exact match. (This is why architectures
     use QK-normalisation / cosine attention.)

Pure numpy, deterministic.
"""
import numpy as np, json, os

OUT = os.path.dirname(os.path.abspath(__file__))


def softmax(x):
    x = x - x.max()
    e = np.exp(x)
    return e / e.sum()


# ---------------------------------------------------------------- Part 1
d, N = 16, 200
r = np.random.default_rng(0)
dirs = r.normal(size=(N, d))
K = dirs / np.linalg.norm(dirs, axis=1, keepdims=True) * np.sqrt(d)   # norm-equalized keys
V = r.normal(size=(N, 3))                                            # vector values
q = r.normal(size=d) * 0.7

sigma2 = np.sqrt(d)                                # the exact-match temperature
w_attn = softmax(K @ q / np.sqrt(d))              # standard scaled dot-product attention
loglik = -0.5 * np.sum((q - K) ** 2, axis=1) / sigma2   # q|z=i ~ N(k_i, σ² I), uniform prior
w_bayes = softmax(loglik)

weight_max_absdiff = float(np.max(np.abs(w_attn - w_bayes)))
out_absdiff = float(np.max(np.abs(w_attn @ V - w_bayes @ V)))

# ---------------------------------------------------------------- Part 2
d2, N2, T = 8, 60, 20000
r2 = np.random.default_rng(1)
dirs = r2.normal(size=(N2, d2))
K2 = dirs / np.linalg.norm(dirs, axis=1, keepdims=True) * np.sqrt(d2)
w_true = r2.normal(size=d2)
Vt = K2 @ w_true                                  # deterministic value = f(k_i)
sigma0_2 = 2.0                                    # true query-noise variance
z = r2.integers(0, N2, size=T)
Q = K2[z] + r2.normal(scale=np.sqrt(sigma0_2), size=(T, d2))
y_true = Vt[z]                                    # target = source memory's value

betas = np.logspace(-1.0, 1.0, 41)                # attention inverse-temperature grid
# squared distances q to each key, for all queries: (T, N2)
D2 = ((Q[:, None, :] - K2[None, :, :]) ** 2).sum(-1)
mse = []
for b in betas:
    S = -0.5 * b * D2
    S -= S.max(1, keepdims=True)
    W = np.exp(S); W /= W.sum(1, keepdims=True)
    pred = W @ Vt
    mse.append(float(np.mean((pred - y_true) ** 2)))
mse = np.array(mse)
beta_star_empirical = float(betas[mse.argmin()])
beta_star_theory = 1.0 / sigma0_2                 # Bayes-optimal η

# ---------------------------------------------------------------- Part 3
r3 = np.random.default_rng(2)
dirs = r3.normal(size=(N, d))
norms = r3.uniform(0.5, 2.0, size=N)              # VARYING key norms
K3 = dirs / np.linalg.norm(dirs, axis=1, keepdims=True) * norms[:, None] * np.sqrt(d)
q3 = r3.normal(size=d) * 0.7
s2 = np.sqrt(d)
w_attn_plain = softmax(K3 @ q3 / np.sqrt(d))                       # plain: ignores ‖k_i‖²
w_bayes3 = softmax(-0.5 * np.sum((q3 - K3) ** 2, axis=1) / s2)     # true posterior
w_attn_corrected = softmax(K3 @ q3 / s2 - 0.5 * np.sum(K3 ** 2, axis=1) / s2)  # + norm term
plain_absdiff = float(np.max(np.abs(w_attn_plain - w_bayes3)))
corrected_absdiff = float(np.max(np.abs(w_attn_corrected - w_bayes3)))

np.savez(os.path.join(OUT, "curves.npz"), betas=betas, mse=mse,
         w_attn=w_attn, w_bayes=w_bayes,
         w_plain=w_attn_plain, w_bayes3=w_bayes3, w_corr=w_attn_corrected)

verdict = {
    "part1_exact_match": {
        "weight_max_abs_diff": weight_max_absdiff,
        "output_max_abs_diff": out_absdiff,
        "identical_to_machine_precision": bool(weight_max_absdiff < 1e-12),
    },
    "part2_temperature_is_eta": {
        "beta_star_empirical": round(beta_star_empirical, 3),
        "beta_star_theory_1_over_sigma0sq": round(beta_star_theory, 3),
        "match": bool(abs(beta_star_empirical - beta_star_theory) / beta_star_theory < 0.15),
    },
    "part3_key_norm_bias": {
        "plain_attention_max_abs_diff": round(plain_absdiff, 4),
        "corrected_attention_max_abs_diff": corrected_absdiff,
        "bias_is_exactly_key_norm_term": bool(corrected_absdiff < 1e-12 and plain_absdiff > 1e-3),
    },
}
with open(os.path.join(OUT, "verdict.json"), "w") as f:
    json.dump(verdict, f, indent=2)

print("S23 — attention as one Bayesian update")
print("-" * 60)
print(f"1. exact match (norm-eq keys, σ²=√d):")
print(f"     max |w_attn − w_bayes| = {weight_max_absdiff:.2e}   output diff = {out_absdiff:.2e}")
print(f"2. attention temperature = η = 1/σ²:")
print(f"     argmin-MSE β = {beta_star_empirical:.3f}   vs   1/σ0² = {beta_star_theory:.3f}")
print(f"3. key-norm bias (varying ‖k_i‖):")
print(f"     plain attn vs posterior:     max diff = {plain_absdiff:.4f}  (biased)")
print(f"     +‖k_i‖² correction:          max diff = {corrected_absdiff:.2e}  (exact)")
print("-" * 60)
print("VERDICT:", json.dumps(verdict))
