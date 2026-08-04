# Does ladder level predict transfer? (result)

**Question (SYNTHESIS §6.1):** the prediction-field frame claims an invariant's
ladder *level* predicts how well it **transfers** across a boundary. S18 showed
this inside one constructed SCM (where invariance = transfer by design). This is the
honest step up: **genuinely different generative mechanisms**, with the transfer
outcome forced by probability theory rather than baked in.

**Status: confirmed — level orders transfer. The original "cliff at L2/L3"
reading is *partially retracted*; see the restraint pass at the bottom.**

> **⟳ Restraint pass (2026-07-26, [`paper/transfer-cliff.md`](../../paper/transfer-cliff.md)).**
> Re-analysis of this experiment's own output, with three additions the original
> run did not make.
> **(1) The step-size claim is wrong.** Adjacent steps are L1→L2 = **+0.451**,
> L2→L3 = **+0.432**, L3→L4 = **−0.022**. The L2/L3 step is *not* uniquely large
> — L1→L2 is the same size or larger. "Near-useless at L1–L2" is also wrong:
> 0.48 is roughly half the attainable skill. **Retracted.**
> **(2) What is real is a ceiling, not a step.** The `vary_n` sweep below is the
> load-bearing evidence: L3/L4 climb to the ceiling, L2 saturates at ~0.54
> permanently, L1 never moves. *More evidence redeems a shared mechanism and
> never redeems a shared form.*
> **(3) The ceiling is now measured** (it never was): scoring domain A against an
> **independent draw of A itself** gives **0.920 ± 0.023** over 8 seeds. L3 scores
> 0.916 — statistically indistinguishable from transferring the law to itself. So
> L3/L4 achieve *complete* transfer, and the ~0.08 shortfall in every L3/L4 number
> is metric noise, not a transfer deficit.
> Also: Spearman(level, skill) = 0.80 has n = 4, whose minimum two-sided p is
> 1/12 ≈ 0.083. It cannot reach significance and is reported for continuity only;
> the real statistics are the per-seed separation (L2 max 0.538 < L3 min 0.886,
> zero overlap in 8 seeds) and the divergent ceilings across 10 values of n.

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

> **⟳ Boundary condition added 2026-07-27 by [D3](../D3-chart-vs-ladder/), and it
> was invisible here.** This experiment compares A and B **in a shared measurement
> chart** — it never varies the convention on which B's aggregate is recorded, and
> never says that it doesn't. D3 crossed this harness with a chart factor
> (B records y ↦ sgn(y)|y|^a) and found the result is **conditional on that shared
> chart**: with the same generators and the same metric, a distortion of a = 0.7
> **inverts** the ordering (L1 0.723 and L2 0.773 beat L3 0.559 and L4 0.565), and
> a distortion of a = 0.85 leaves the ordering intact while **collapsing the L2/L3
> separation** to 0.013 (L2 0.756 vs L3 0.769) from 0.43 undistorted.
> Restating the claim chart-freely restores everything, at Spearman +0.80 in every
> chart. So "ladder level predicts transfer" holds **given a shared chart**, and
> transfer needs two factors — a shared mechanism *and* a chart-free statement of
> it. The ordering below is real; it is not unconditional.
> Read against the ceiling measured in the restraint pass above, chart-freedom
> also has a **price**: the chart-free claim tops out at 0.833 where this
> experiment's shared-chart claim reaches 0.916 ≈ complete transfer. Invariance
> buys robustness, not maximal skill.

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

## Follow-up: varying n (`vary_n.py`)

How does transfer skill scale with n, the number of contributions per aggregate?
Run `python3 vary_n.py` then `python3 plot_vary_n.py` → [`vary_n.png`](./vary_n.png).

| n | L1 | L2 | L3 | L4 | cliff (L3−L2) |
|---:|:--:|:--:|:--:|:--:|:--:|
| 2 | 0.03 | 0.12 | 0.36 | 0.30 | 0.23 |
| 8 | 0.04 | 0.31 | 0.75 | 0.67 | 0.44 |
| 64 | 0.01 | 0.44 | 0.89 | 0.90 | 0.45 |
| 1024 | 0.02 | **0.54** | **0.93** | **0.92** | 0.39 |

**Findings (one of which corrects a prior conjecture):**

1. **L3/L4 climb to the ceiling.** As n grows the CLT kicks in; finite-variance
   levels rise to the finite-sample ceiling (~0.94, = full transfer given metric
   noise). More data ⇒ genuine shared-mechanism invariants transfer *better*.
2. **L2 saturates far below — and my earlier guess was wrong.** I had conjectured
   "L2 skill *falls* as n grows." **It does not.** L2 *rises* then **plateaus at
   ~0.5**: the aggregate of infinite-variance increments converges to a fixed
   α-stable (α=1.5) law that is *permanently non-Gaussian*, so skill converges to a
   constant — bounded away from 1, never improving past it. The correct invariant
   here is **"L2 is capped," not "L2 declines."** Logged as a corrected prediction.
3. **The cliff opens fast and persists.** The L2/L3 gap is already wide by n≈8 and
   stays ~0.4–0.5; it does not close, because the two sides saturate at different
   ceilings (0.94 vs 0.5). *More evidence of the mechanism sharpens the diagnostic:
   real invariants keep improving, appearance-only ones hit a wall.*

**Caveat on the ~0.5 plateau:** the metric trims the extreme 2% tails, so it is
*generous* to L2 (the untrimmed heavy tails would push it lower). The robust,
metric-independent claim is *bounded away from the ceiling*, not the exact 0.5.

## Next

- The real one: 3–4 *different* catalog invariants, real data, A→B transfer.
- Repeat the plateau with less tail-trimming to show L2's ceiling drop (metric
  sensitivity check).
