# 2026-07-26 — Paper 1: the transfer result re-analyzed, and the "cliff" retracted

**Worked on:** [`experiments/ladder-vs-transfer/`](../experiments/ladder-vs-transfer/),
[`experiments/S18-invariance-transfer/`](../experiments/S18-invariance-transfer/),
[`experiments/real-transfer/`](../experiments/real-transfer/), and the ladder
claim in [`METHODOLOGY.md`](../METHODOLOGY.md).
**Change:** new [`paper/`](../paper/) directory with paper 1; the "cliff at the
L2/L3 boundary" step-reading **retracted** and replaced by a ceiling reading,
corrected at four sites; two new measurements added.

## What I did

Assembled the project's three transfer experiments into one argument with its own
methods and limitations sections ([`paper/transfer-cliff.md`](../paper/transfer-cliff.md)),
rather than adding a new experiment. The point of a paper here is that a
re-analysis is allowed to correct its sources — and this one did.

First, reproduction. All three experiments were re-run from scratch
(numpy 2.4.6, scikit-learn 1.9.0) and reproduce their committed verdicts
bit-for-bit: ladder skills 0.033/0.484/0.916/0.894, S18 ρ = 0.985, real-transfer
ρ = 0.983 with Benford 0.97 vs 0.00.

Then three analyses the source runs did not do, in
[`paper/analysis/robustness.py`](../paper/analysis/robustness.py).

## What I found

**The headline reading was wrong, and it was wrong in a checkable way.** Every
write-up of the ladder experiment — the experiment README, `METHODOLOGY.md`,
`SYNTHESIS.md`, essay 1 — described a *cliff at the L2/L3 boundary*, with
transfer "near-useless at L1–L2." Nobody had decomposed the adjacent steps:

```
   L1 → L2   +0.451
   L2 → L3   +0.432        <- claimed to be the cliff
   L3 → L4   −0.022
```

The L2/L3 step is not uniquely large: paired across the 8 seeds the two steps
differ by 0.019 ± 0.098, **t(7) = 0.56**. And L2 at
0.484 is roughly half the attainable skill, not near-useless. The step reading is
**retracted**. This is a case of a slogan outrunning its data and then being
copied forward through four documents, which is the specific failure mode the
[methodology](../METHODOLOGY.md) exists to catch — caught here only because a
paper forced a second look at numbers that had been treated as settled.

**What replaces it is better, and it was already in the repo.** The `vary_n`
sweep — run at the time, never made load-bearing — shows the real structure. As n
goes 2 → 1024: L1 never moves (~0.03), L3/L4 climb to ~0.93, **L2 rises and then
stops at ~0.54.** The distinction is a *ceiling*, not a step:

> More evidence redeems a shared mechanism and never redeems a shared form.

That is a claim about the limit of a correspondence's usefulness, it is what the
data support without adjudication, and it survives the objection that L1 was
never a real rung.

**The ceiling is now measured, and it changes the reading of L3.** The claim that
L3/L4 saturate at the *metric's* ceiling rather than at a real deficit had never
been tested. Scoring domain A against an **independent draw of A itself** — same
law, so any shortfall is pure estimation noise — gives **0.920 ± 0.023** over 8
seeds. L3 scores **0.916**. So shared-mechanism correspondences do not merely
transfer well; they transfer *as well as a law transfers to itself*, and the ~0.08
shortfall in every L3/L4 number is metric noise that should never have been
interpreted.

**A statistic that was carrying weight it cannot carry.** Spearman(level, skill)
= 0.80 has n = 4; its minimum attainable two-sided p is 1/12 ≈ 0.083, so it cannot
reach significance regardless of the data. Demoted to "reported for continuity."
The load-bearing statistics are the per-seed separation (L2 max 0.538 < L3 min
0.886 — zero overlap in 8 seeds) and the divergent ceilings across 10 values of n.
Conversely, the real-data leg has 9 independent features and *can* be tested:
a 200k-draw permutation test gives **p = 6 × 10⁻⁵**.

**One limitation the sources do not state.** The ladder experiment's L3 and L4
conditions both have finite variance and are both covered by the CLT; the labels
encode whether we *treat* the limit as an invoked theorem or a shared mechanism.
So "L3 ≈ L4 in transfer" cannot be separated from "L3 and L4 were never two
conditions." The L3≈L4 finding is downgraded to suggestive.

## Decisions

- Retraction recorded at all four sites that carried the claim
  (`METHODOLOGY.md`, `SYNTHESIS.md`, the experiment README, essay 1), each
  pointing at paper 1 §3.3. Nothing rewritten to hide the error — the essay in
  particular is left as written with a correction note, per the repo's rule that
  superseded work is corrected in place.
- The paper grades its own claims on the ladder, and grades the ceiling result
  **L2 with a mechanism proposed** — a candidate, not a finding. It rests on one
  sweep in one invariant family.
- Papers get a stated convention ([`paper/README.md`](../paper/README.md)): every
  number reproducible from a script, limitations as sections, and a paper that
  retracts a repo claim must correct it at the source and log it.

## Next

- **Break the signal-strength confound** in real-transfer leg A (§8 falsifier 5).
  It is now the paper's live falsifier: if a residual-invariance version destroys
  ρ = 0.983, the real-data leg reduces to "strong features transfer" and only the
  synthetic legs support the frame.
- **Separate L3 from L4 properly** — a condition where the mechanism is shared but
  no theorem covers it, versus one where the theorem is available. Only then does
  "L3 ≈ L4" mean anything.
- **A second invariant family.** Every transfer number in the repo lives in the
  CLT/stable-law universe. The ceiling claim is one family wide.
- The paper's §6.3 conjecture (levels differ in what they *compress*) predicts
  **no L2/L3 cap for non-modal tasks** — in-distribution fit, retrodiction,
  interpolation. Untested, and a clean experiment.
