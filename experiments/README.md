# Experiments

Runnable, reproducible tests of specific questions — the restraint stroke of the
[research rhythm](../METHODOLOGY.md). Each experiment is self-contained (prefer pure
numpy; state any install), deterministic where possible, and ends with an honest
verdict including what it does *not* show.

| Experiment | Tests | Result |
|------------|-------|--------|
| [`S3-fisher-geometry/`](./S3-fisher-geometry/) | [S3](../questions/SPECULATIVE.md): does a Fisher/statistical-curvature quantity spike at a phase transition, in physics *and* in learning? | **Partially confirmed** — χ→∞ at the Ising T_c; inverse-Fisher blows up exactly at the double-descent test-error peak (P/N=1). Grokking still open. |
| [`S18-invariance-transfer/`](./S18-invariance-transfer/) | [S18](../questions/SPECULATIVE.md) / the [prediction-field](../PREDICTION-FIELD.md) falsifier: does invariance-across-environments predict transfer? | **Falsifier survived** — train-measured coefficient instability ranks held-out transfer error at ρ=0.985; the most in-distribution-predictive feature is the worst-transferring. Confirmed in a constructed SCM; real cross-domain test still open. |
| [`ladder-vs-transfer/`](./ladder-vs-transfer/) | [SYNTHESIS §6.1](../SYNTHESIS.md): does ladder *level* predict transfer across genuinely different mechanisms? | **Confirmed + sharpened** — transfer skill has a sharp *cliff at the L2/L3 boundary* (appearance→mechanism / finite-vs-∞ variance): L1 0.03, L2 0.48, L3 0.92, L4 0.89. L3≈L4 (mechanism and theorem transfer equally), so it's a step, not a ramp. Controlled/synthetic; real-data version still open. |
| [`S23-attention-bayes/`](./S23-attention-bayes/) | [S23](../questions/SPECULATIVE.md): is softmax attention one step of the [universal update](../invariants/mirror-descent-update.md)? | **Confirmed exactly** — attention weights = Bayes posterior over memories to 1.4e-17; attention temperature = the update's η = 1/σ²; plain dot-product attention is a biased posterior, exact once ‖k‖² is corrected (explains QK-norm). Attention is now a confirmed L3 instance of the universal update. |
| [`real-transfer/`](./real-transfer/) | [SYNTHESIS §6.1](../SYNTHESIS.md): does the [prediction-field frame](../PREDICTION-FIELD.md) hold on data I did **not** construct? | **Passed both legs** — Leg A: on the real diabetes dataset, invariance predicts transfer at ρ=0.983 (bmi/s5 stable+transfer, sex neither). Leg B: Benford transfers across 2ⁿ/3ⁿ/n!/Fibonacci (0.97) and fails on controls (0.00). Frame now empirically load-bearing. Honest confound: Leg A can't separate invariance from signal strength (S18 controls that; this doesn't). |
| [`S26-sgd-charges/`](./S26-sgd-charges/) | [S26(iii)](../questions/SPECULATIVE.md): is SGD's stationary law coordinatized by its conserved charges? | **Confirmed as a prethermalization plateau** — Q conserved in the flow limit (drift ∝ lr); weight-decay breaking follows dQ/dt=−4λQ to 1e-5; stationary norm = √(Q²+4w*²) predicted from the charge alone to 3e-4; charge quasi-conserved (erosion 5.6e-7/step, ~1.8M-step window) — the GGE logic transfers *with* its known failure mode. |
| [`S7-critical-slowing/`](./S7-critical-slowing/) | [S7](../questions/SPECULATIVE.md) + the middle-zone reduction: is slowing-down one signal, and is it Φ's Hessian softening? | **Mechanism confirmed, exponent refuted** — τ·λ_min = 0.94±0.13 across saddle-node, Ising, and GD-at-the-MP-edge (one relation, no tuning); divergence exponents are domain-specific (−½/−1/−2). Fourth arrival at the ∇²Φ singular-set object. Near-critical nonlinear bias documented (leg B). |

## Conventions

- Keep it cheap and deterministic; seed everything.
- Save raw outputs (CSV/JSON) next to the script so results are auditable.
- The `README.md` states the claim, the result, and the honest limits — a passing
  number is not a finding until its boundary conditions are written down.
- A surviving result graduates its object toward a full
  [`invariants/`](../invariants/) entry and gets a [research-log](../research-log/)
  note.
