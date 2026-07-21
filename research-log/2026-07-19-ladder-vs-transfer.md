# 2026-07-19 — Restraint: does ladder level predict transfer? (the cliff)

**Worked on:** SYNTHESIS §6.1 — the real transfer test; the ladder itself
**Change:** new experiment; methodology strengthened (L2/L3 line = transfer cliff)

## Why this one

The synthesis named "real cross-domain transfer" as the highest-stakes frontier —
the test that moves the prediction-field frame from self-consistent to load-bearing.
S18 proved invariance⇒transfer inside *one* SCM (invariance = transfer by design).
This is the honest step up: **genuinely different mechanisms**, transfer outcome
forced by probability theory.

## Design (the anti-tautology move)

Held the surface phenomenon fixed — "a macro quantity is the aggregate of n=200
micro contributions" — learned the law in reference domain A (uniform increments →
Gaussian aggregate), then varied only how deeply that Gaussian invariant applies in
B (= correspondence level):

- **L4** exponential increments (finite var → CLT theorem, different micro-law)
- **L3** skewed finite-var mixture (same CLT mechanism)
- **L2** heavy-tailed increments ν=1.5 (infinite var → stable law, NOT Gaussian)
- **L1** single heavy draw (not an aggregate; word only)

Levels justified by real theory (finite/infinite variance), so level⇒transfer is a
consequence, not a construction.

## Result

Transfer skill: **L1 0.03 · L2 0.48 · L3 0.92 · L4 0.89** (Spearman 0.80).

Two findings:
1. **A sharp cliff at L2/L3** — near-useless at L1–L2 (word / shared form), high at
   L3–L4 (shared mechanism / theorem). This *re-derives the methodology's central
   claim* (the L2/L3 line is the important one) from a transfer measurement, rather
   than assuming it. The cliff is the finite-vs-infinite-variance line = the
   appearance→mechanism boundary.
2. **L3 ≈ L4, honestly** — mechanism and theorem transfer *equally well*; they
   differ in the strength of the guarantee, not the transfer. So "level predicts
   transfer" is a **step at the mechanism boundary, not a ramp**. Did not force a
   monotonic story (`monotone_… = false`, on purpose).

## Honest limits

- Controlled within one invariant family (CLT/Gaussian) — cleanest isolation of
  "depth controls transfer," but not yet cross-invariant / real-data.
- Synthetic (different mechanisms, but generated). The remaining open version:
  *different* catalog invariants on *real* datasets, A→B.
- Metric trims extreme 2% tails (robustness for infinite variance) — generous to L2;
  the cliff is sharp anyway.

## Map updates

- Strengthened [`../METHODOLOGY.md`](../METHODOLOGY.md): the L2/L3 line is now
  documented as the empirical transfer cliff.
- SYNTHESIS §6.1 marked partially done; ledger row added.

## Follow-up (same day): varied n — and corrected a conjecture

Ran `vary_n.py` sweeping n = 2…1024. Findings:

- **L3/L4 climb to the finite-sample ceiling (~0.94)** as the CLT engages — more
  data makes genuine shared-mechanism invariants transfer *better*.
- **L2 does NOT fall (my conjecture was wrong).** I had predicted L2 skill would
  fall as n grows; it instead *rises then plateaus at ~0.5*. Reason: infinite-
  variance aggregates converge to a fixed α-stable law (permanently non-Gaussian),
  so skill saturates at a constant — **bounded away from 1, not declining.** The
  corrected invariant: "L2 is capped," not "L2 declines." (Restraint working as
  intended — the guess got pruned.)
- **The cliff opens fast (by n≈8) and persists** at ~0.4–0.5 because the two sides
  saturate at different ceilings (0.94 vs 0.5). Diagnostic sharpens with evidence:
  real invariants keep improving, appearance-only ones hit a wall.

## Next

- The real one still stands: real-data A→B transfer across different invariants.
- Metric sensitivity: repeat with less tail-trimming to show L2's ceiling drop.
