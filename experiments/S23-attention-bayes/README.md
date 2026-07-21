# S23 — attention is the universal update (result)

**Question ([S23](../../questions/SPECULATIVE.md)):** is softmax attention one step of
the [universal update](../../invariants/mirror-descent-update.md) — a Bayesian
reweighting over memories?

**Status: confirmed exactly (to machine precision), plus an honest nuance about
plain dot-product attention.**

Run: `python3 run.py` (pure numpy, deterministic) → `python3 plot.py` →
[`s23_result.png`](./s23_result.png).

## The derivation

Softmax attention over memories (kᵢ, vᵢ) for a query q:

```
   wᵢ = softmax(q·kᵢ / √d),      output = Σᵢ wᵢ vᵢ .
```

Bayesian retrieval: a latent "which memory" z with uniform prior, and
`q | z=i ~ N(kᵢ, σ² I)`. The posterior is

```
   p(z=i | q) ∝ exp(−‖q − kᵢ‖² / 2σ²)
              ∝ exp( q·kᵢ/σ²  −  ‖kᵢ‖²/2σ² )      (the ‖q‖² term cancels in softmax)
```

This is **exactly** S1's universal update `xᵢ ∝ xᵢ · exp(−η gᵢ)` applied once, from
the uniform prior, with **loss gᵢ = ½‖q−kᵢ‖²** (squared distance = surprise) and
**step η = 1/σ²**. And the two coincide with attention when

- **keys are norm-equalized** (‖kᵢ‖ = const, so the ‖kᵢ‖² term drops), and
- **σ² = √d** (so q·kᵢ/σ² = q·kᵢ/√d).

Then the attention output = Σᵢ p(z=i|q) vᵢ = the **posterior-predictive mean**.
Reading: **a transformer layer does amortized Bayesian inference in its forward
pass; in-context learning is the universal update executed at run time.**

## Results (`verdict.json`)

| # | Test | Result |
|---|------|--------|
| 1 | Exact match (norm-eq keys, σ²=√d) | `max |w_attn − w_bayes| = 1.4e-17`, outputs `6e-17` → **identical to machine precision** |
| 2 | Attention temperature = η | argmin-MSE `β = 0.501` vs theory `1/σ0² = 0.500` → **the temperature is the noise precision** |
| 3 | Key-norm bias | plain attention differs by `0.029`; adding `‖kᵢ‖²/2σ²` → `1e-17` → **bias is exactly the key-norm term** |

Panel 2 is the load-bearing one: sweeping attention's inverse-temperature β, the
prediction MSE bottoms out precisely at β = 1/σ0² — the Bayes-optimal step size.
Attention temperature is not a free knob; it is the update's η = the inverse noise
variance.

## The honest nuance (a genuine, useful finding)

**Plain dot-product attention is a *biased* Bayesian retrieval.** It omits the
`−‖kᵢ‖²/2σ²` term, so it implicitly boosts high-norm keys by a prior factor
`exp(‖kᵢ‖²/2σ²)`. Panel 3 shows the deviation (0.029) and that the `‖kᵢ‖²`
correction removes it exactly. This is *why* architectures adopt QK-normalization
and cosine attention: they restore the exact posterior by equalizing key norms.
The stone didn't just confirm — it explained an existing engineering practice.

## Scope / limits

- Exact for the **single-head, single-step** case with a Gaussian memory model.
  Multi-head attention = a mixture of such updates; multi-layer = iterated updates
  (a chain of Bayesian filters) — plausible but not shown here.
- The Gaussian likelihood is a modeling choice; other kernels give other
  exponential-family updates (still the universal update, different gᵢ).
- Shows attention *equals* one Bayesian update; it does not claim trained networks
  *use* it optimally (β is learned, not set to 1/σ²).

## What it does to the map

- **Promotes a manifestation:** attention/transformers is now a confirmed L3 instance
  of [the universal update](../../invariants/mirror-descent-update.md) — the same
  object as replicator / MW / Bayes / Gibbs, now including modern deep learning.
- Reinforces the [prediction-field](../../PREDICTION-FIELD.md) reading: attention
  computes a posterior over which memory predicts the query — inference on the field.

## Next

- Iterate: does stacking these updates (multi-layer) behave like a Bayesian
  filter / particle filter? (numpy-feasible)
- Multi-head as a mixture-of-experts update.
