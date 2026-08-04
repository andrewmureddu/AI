# 2026-07-27 — The catalog tagged by chart: a third axis, and four predictions

**Worked on:** applying [D3](../experiments/D3-chart-vs-ladder/)'s finding to the
catalog — a debt logged in D3's own "next" list and repeated in D4's.
**Change:** new [`invariants/CHARTS.md`](../invariants/CHARTS.md), a third
orthogonal axis alongside level and floor. No level or floor moves; four new
falsifiable predictions are on record.

## What I did

D3 established that transfer needs two independent things — a shared mechanism
*and* a claim stated chart-freely — and that the ladder grades only the first. That
finding went into [`METHODOLOGY.md`](../METHODOLOGY.md) with the consequence
spelled out (*a high-rung entry with a chart-dependent statement is predicted not
to transfer, and that is the cheapest available falsifier for much of the
catalog*), and then sat there unapplied through two more cycles.

Applied it. Each entry tagged by whether its **core object** survives
reparameterizing the measurement axis — a ratio, a dimensionless product, a sign, a
count, an ordinal relation — or moves with it.

Count: **free 8 · dependent 6 · splits 8.**

## What I found

**Four entries were already confirmed by experiments in the repo**, which is what
makes the tag a test rather than a relabelling:

- **#22 critical slowing down** — free (τ·λ is a product of conjugates), and
  [S7](../experiments/S7-critical-slowing/) measured it transferring at 0.94 ± 0.13
  *while its exponents spanned −½/−1/−2*. The entry splits exactly along the tag.
- **#19 spectral gap** — dependent (a bare eigenvalue), and
  [P-A](../experiments/PA-spectral-gap/) measured family constants spanning 1.54×,
  filed at the time as a disappointment. The tag says that was the expected result.
- **#21 noise thresholds** — splits, and [S5](../experiments/S5-noise-thresholds/)
  measured both halves.
- **#9 allometry** — and this one is a *warning*, not a success. On its surface
  form (Y ∝ M^b) it is a bare exponent and the tag would predict failure.
  [P-D](../experiments/PD-allometry-reduction/) showed θ is a **log-ratio fixed by
  counts**, and it transferred at spread 4.0e-15. **The tag must be applied to the
  object after reduction, not to how the entry is written** — and I would have got
  this row wrong without P-D.

**The four predictions**, which is the point of the document:

1. **The catalog's strongest entry is predicted not to travel.** #5 criticality is
   the only unqualified **L4**, and critical exponents are chart-dependent. So its
   exponents should transfer *within* a universality class (shared chart, per
   [D2](../derivations/D2-gauge-of-the-tower.md) §7) and fail across fields sharing
   no chart convention, while its ratios, signs and relevant-direction counts
   transfer either way. A high rung does not protect it.
2. **Two low-rung entries are predicted to over-perform** — and this is where the
   tag and the ladder predict *opposite* orderings, so it is the sharpest test.
   **#14 Pareto (L1–L2)** is purely *ordinal*: dominance survives any monotone
   reparameterization of every axis independently, a stronger invariance than
   anything else in the catalog. **#16 information bottleneck (L2–L3)** rests on
   mutual information, invariant under any invertible reparameterization of either
   variable.
3. **#18 optimal transport is the weakest L3 candidate** — its core object needs a
   ground metric, which is a chart choice. [`FLOORS.md`](../invariants/FLOORS.md)
   already flagged it as fitting neither the three floors nor the proposed fourth;
   the tag says those are the same observation.
4. **The eight `splits` entries should split in measurement**, not just on paper —
   free half transfers, dependent half does not, on the same systems. Two already
   do (#21, #22); six are open.

## Decisions

- **Third axis added, nothing promoted or demoted.** Level, floor and chart are
  orthogonal; the catalog README now says so.
- **No entry files edited yet.** The tag lives in one document rather than being
  scattered across 23 entries, because it is a *claim* about each entry and should
  be reviewable in one read. If it survives, it belongs in the template.

## Honest limits

- **The tag is assigned by inspection, not measured.** D3 measured chart-invariance
  by applying an explicit group and watching transfer degrade. Nothing here does
  that, and #9 is the standing proof that inspection can be wrong.
- **One group only** (G_pow on the measurement axis).
- **Chart-freedom is necessary, not sufficient** (D3), and it **has a price** (D3
  again, against paper 1's ceiling: 0.833 vs 0.916). A `free` tag predicts an entry
  *can* travel, not that it does, and not that it travels best.

## Next

- **Measure the tag** on two or three entries rather than assigning it, using D3's
  method. That converts CHARTS.md from a claim into evidence.
- **Prediction 2 is cheap and decisive** — Pareto and the information bottleneck
  against a chart-dependent higher-rung entry, on the ladder-vs-transfer harness.
