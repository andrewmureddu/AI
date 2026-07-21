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

## Conventions

- Keep it cheap and deterministic; seed everything.
- Save raw outputs (CSV/JSON) next to the script so results are auditable.
- The `README.md` states the claim, the result, and the honest limits — a passing
  number is not a finding until its boundary conditions are written down.
- A surviving result graduates its object toward a full
  [`invariants/`](../invariants/) entry and gets a [research-log](../research-log/)
  note.
