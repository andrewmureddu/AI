# Papers

Longer-form write-ups that assemble several of the repo's results into a single
argument with its own methods, statistics and limitations sections. A paper is
not a new claim — everything in one traces to an experiment, a derivation, or a
catalog entry — but it is allowed to *re-analyze* what is already here, and a
re-analysis can correct the source.

| Paper | Subject | Status |
|-------|---------|--------|
| [`transfer-cliff.md`](./transfer-cliff.md) | What makes a cross-domain correspondence transfer. Assembles [S18](../experiments/S18-invariance-transfer/), [ladder-vs-transfer](../experiments/ladder-vs-transfer/) and [real-transfer](../experiments/real-transfer/); tests whether the [ladder](../METHODOLOGY.md) predicts transfer. | complete — carries one **retraction** and two new measurements |

## What paper 1 changed in the map

Three things, all in [`transfer-cliff.md`](./transfer-cliff.md):

1. **Retraction (§3.3).** The repo's "cliff at the L2/L3 boundary, transfer
   near-useless at L1–L2" reading is not supported by its own data. The adjacent
   steps are L1→L2 = 0.451 and L2→L3 = 0.432 — the same size. Corrected in
   [`METHODOLOGY.md`](../METHODOLOGY.md) and the
   [source README](../experiments/ladder-vs-transfer/).
2. **Replacement (§3.4).** What is real about the L2/L3 boundary is a **ceiling,
   not a step**: L3/L4 rise to full transfer as evidence grows, L2 saturates at
   ~59% of it permanently. *More evidence redeems a shared mechanism and never
   redeems a shared form.*
3. **New measurement (§3.4).** The transfer metric's own ceiling, never
   previously measured: 0.920 ± 0.023 (a domain scored against an independent
   draw of itself). L3 scores 0.916 — shared-mechanism correspondences transfer
   as well as a law transfers to itself, which is stronger than "high transfer."

New statistics are in [`analysis/robustness.py`](./analysis/robustness.py) →
[`analysis/robustness.json`](./analysis/robustness.json): per-seed spreads, the
adjacent-step decomposition, the self-transfer baseline, and a permutation test
for the real-data leg (p = 6 × 10⁻⁵).

## Conventions

- Every number must be reproducible from a script in the repo, and the paper
  states when it was last regenerated.
- Limitations are sections, not asides. A paper that re-analyzes a result
  inherits the duty to state limits the source did not.
- A paper may retract a repo claim. It must then correct the claim at its
  source and log it in [`research-log/`](../research-log/), per
  [`CONTRIBUTING.md`](../CONTRIBUTING.md).
