# The universal update (mirror descent / entropic ascent)

> **One-line claim:** Replicator dynamics, multiplicative-weights, exponentiated
> gradient, Bayesian updating, and relaxation to Boltzmann–Gibbs are all mirror
> descent on a KL/entropy regularizer — one update rule wearing many names.
> **Headline correspondence level:** **L3** for the local update + its geometry
> (derived, exact); global convergence is explicitly *not* shared.
> **Status:** developing — *derived* ([derivation](../derivations/S1-universal-update.md))

## Statement

Mirror descent minimizes a loss plus a Bregman-divergence regularizer; with the
(negative) entropy as mirror map it becomes the exponential/multiplicative update
x_i ← x_i · exp(η · reward_i) / Z. Domain-neutral object: **entropic mirror
descent** and its continuous-time limit (a replicator/Fokker–Planck flow).

## Manifestations by domain (seed)

- Biology: replicator dynamics ẋ_i = x_i(f_i − f̄) — continuous-time MW. L3.
- CS/ML: multiplicative weights, Hedge, exponentiated gradient — anchor.
- Inference: Bayesian update is a multiplicative reweighting by likelihood. L3.
- Physics: relaxation to Boltzmann–Gibbs = entropy-regularized equilibrium. L3.
- Economics: fictitious play / evolutionary game dynamics. L2–L3.
- Deep learning: **softmax attention** = one Bayesian update over memories, exactly
  (loss ½‖q−k‖², η = 1/σ²). **L3, verified** —
  [`../experiments/S23-attention-bayes/`](../experiments/S23-attention-bayes/).

## Result (2026-07-19) — derived, sharpened, bounded

Full derivation: [`../derivations/S1-universal-update.md`](../derivations/S1-universal-update.md).
All four are the same update `x_i ∝ x_i·exp(−η g_i)` (entropic mirror descent),
differing only in the loss g_i and the step η:

| update | g_i | η |
|--------|-----|---|
| multiplicative weights | expert loss ℓ_i | free |
| Bayes | log-loss −ln L_i | 1 (temper → free) |
| replicator (cts) | −fitness | →0 limit = ẋ_i=x_i(f_i−f̄) |
| Gibbs | energy E_i | β = 1/T |

**Confirmed L3** for the local update and its geometry (it is Fisher/Shahshahani
natural-gradient descent; ties to [S3](../experiments/S3-fisher-geometry/) and the
[prediction field](../PREDICTION-FIELD.md)). Bonus L3: the normalizer is one object
— **free energy = −log evidence = cumulative log-loss = −log-growth**.

**Boundary (the sharp line):** global dynamics are *not* shared — with a fixed loss
the update concentrates (Bayes, Gibbs); with a game-coupled loss it can cycle
forever (replicator in zero-sum games, Poincaré recurrence). "They all converge
alike" is **retired to L1**. Vanilla Bayes also locks η = 1.

**S2 corollary:** the shared η is learning rate = inverse temperature = selection
intensity (given the tempered-Bayes bridge).

**Next:** numerically exhibit the concentrate-vs-cycle split (§5 of the derivation).
Refs: Nemirovski–Yudin; Beck–Teboulle 2003; Shahshahani 1979; Harper 2009;
Mertikopoulos–Papadimitriou–Piliouras 2018; Jaynes 1957; Khan–Rue 2023.
