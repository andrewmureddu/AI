# Does ladder level predict transfer? (result)

**Question (SYNTHESIS §6.1):** the prediction-field frame claims an invariant's
ladder *level* predicts how well it **transfers** across a boundary. S18 showed
this inside one constructed SCM (where invariance = transfer by design). This is the
honest step up: **genuinely different generative mechanisms**, with the transfer
outcome forced by probability theory rather than baked in.

**Status: confirmed, with a sharper finding than expected — the transfer *cliff*
sits at the L2/L3 boundary (appearance → mechanism).**

Run: `python3 run.py` (pure numpy, deterministic) → `python3 plot.py` →
[`ladder_transfer.png`](./ladder_transfer.png).

## Design (why it isn't S18 again)

We hold the **surface phenomenon fixed** — "a macroscopic quantity is the aggregate
of n = 200 microscopic contributions" — and learn the law in a reference domain A
(uniform increments): *the normalized aggregate is Gaussian*. Then we vary only how
deeply that Gaussian invariant **actually applies** in domain B — i.e. the
correspondence level — and measure whether A's law transfers:

| Level | Domain B | Why that level | Theory says |
|:-----:|----------|----------------|-------------|
| **L4** | exponential increments | finite variance ⇒ CLT is a **theorem** despite a totally different micro-law | Gaussian — transfers |
| **L3** | skewed finite-variance mixture | **same mechanism** (CLT), mild finite-n skew | Gaussian — transfers |
| **L2** | heavy-tailed increments (t, ν=1.5, **infinite variance**) | same "sum of many" *appearance*, but a **different universality class** (converges to a stable law) | not Gaussian — fails |
| **L1** | a single heavy draw (no aggregation) | shares only the **word** "combine" | irrelevant — fails |

The level labels are justified by real theory (finite/infinite variance; theorem vs
none), so a level⇒transfer relationship is a *consequence*, not a construction.
Metric: robustly-standardized shape distance (1-D Wasserstein over the [0.02, 0.98]
quantile band) between B's aggregate and A's Gaussian; skill = 1 − d/d_ref.

## Result (`verdict.json`)

| level | transfer skill | shape distance |
|:-----:|:--------------:|:--------------:|
| L1 | **0.03** | 0.209 |
| L2 | **0.48** | 0.111 |
| L3 | **0.92** | 0.018 |
| L4 | **0.89** | 0.023 |

Spearman(level, skill) = 0.80.

Two findings:

1. **A sharp cliff at L2/L3.** Transfer is near-useless at L1 (word only, 0.03) and
   only half-there at L2 (same *form*, wrong universality class, 0.48), then jumps to
   high at L3–L4 (0.9+). The cliff is exactly the **appearance → mechanism** boundary
   — the finite-vs-infinite-variance line. This is the [methodology's](../../METHODOLOGY.md)
   central claim (the L2/L3 line is the one that matters) **re-derived from a
   transfer measurement**, not assumed.

2. **L3 ≈ L4 — and that's correct.** A shared *mechanism* (L3) and a *theorem* (L4)
   transfer *equally well*; they differ in *why*, not *how well*. So "level predicts
   transfer" is real but **not strictly monotone at the top** — the honest shape is a
   **step** at the mechanism boundary, not a ramp. We report the step, not a forced
   monotonic story (`monotone_… = false` in the verdict, on purpose).

The left panel shows it directly: L3/L4 quantile curves hug A's Gaussian; L2 and L1
peel away in the tails (where the heavy-tailed universality class lives).

## Honest hedging

- **Controlled within one invariant family** (the CLT/Gaussian limit). It shows
  *depth of correspondence* controls transfer when the surface phenomenon is held
  fixed — the cleanest possible isolation — but it is not yet the cross-*invariant*,
  cross-*domain*, real-data test.
- **Still synthetic.** Genuinely different mechanisms (a real step past S18's single
  SCM), but generated, not observed. The remaining open version: measure A→B transfer
  for *different* catalog invariants on *real* datasets.
- The metric trims the extreme 2% tails (robustness for infinite-variance cases);
  the L2 skill would fall further with less trimming — i.e. we are being *generous*
  to L2, and the cliff is still sharp.

## What this does to the map

- Supports promoting the ladder from "a bookkeeping scale" to "an operational
  predictor of transfer," at least across mechanisms — and pinpoints that its
  **discriminating power is concentrated at the L2/L3 step**.
- Reinforces the [prediction-field frame](../../PREDICTION-FIELD.md): what transfers
  is the shared-mechanism (measurement-invariant) content, not the shared appearance.

## Next

- The real one: 3–4 *different* catalog invariants, real data, A→B transfer.
- Vary n (contributions per aggregate): the L2 skill should *fall* as n grows (the
  stable-law tails become more pronounced), sharpening the cliff — a clean follow-up.
