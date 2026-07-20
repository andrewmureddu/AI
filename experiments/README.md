# Experiments

Runnable, reproducible tests of specific questions — the restraint stroke of the
[research rhythm](../METHODOLOGY.md). Each experiment is self-contained (prefer pure
numpy; state any install), deterministic where possible, and ends with an honest
verdict including what it does *not* show.

| Experiment | Tests | Result |
|------------|-------|--------|
| [`S3-fisher-geometry/`](./S3-fisher-geometry/) | [S3](../questions/SPECULATIVE.md): does a Fisher/statistical-curvature quantity spike at a phase transition, in physics *and* in learning? | **Partially confirmed** — χ→∞ at the Ising T_c; inverse-Fisher blows up exactly at the double-descent test-error peak (P/N=1). Grokking still open. |
| [`S18-invariance-transfer/`](./S18-invariance-transfer/) | [S18](../questions/SPECULATIVE.md) / the [prediction-field](../PREDICTION-FIELD.md) falsifier: does invariance-across-environments predict transfer? | **Falsifier survived** — train-measured coefficient instability ranks held-out transfer error at ρ=0.985; the most in-distribution-predictive feature is the worst-transferring. Confirmed in a constructed SCM; real cross-domain test still open. |

## Conventions

- Keep it cheap and deterministic; seed everything.
- Save raw outputs (CSV/JSON) next to the script so results are auditable.
- The `README.md` states the claim, the result, and the honest limits — a passing
  number is not a finding until its boundary conditions are written down.
- A surviving result graduates its object toward a full
  [`invariants/`](../invariants/) entry and gets a [research-log](../research-log/)
  note.
