# 2026-07-28 — D5 confirms arithmetic nobody doubted, and closes the discovery register

**Worked on:** [D5](../questions/UNKNOWN-LAWS.md), the register's last unworked
stone.
**Change:** D5 confirmed and graded **N0–N1**; the discovery register's six filed
stones are all worked. A fifth process failure is on record, and this one was mine
rather than the code's.

## What I did

D5 asked whether the degeneracy order has arithmetic. Its own prior-art warning
was the harshest in the register — *"most likely to be N0; the potential case is
Thom and Arnold"* — and that warning was right about the literal reading.

**The literal reading is coalescence, and it is answered.** Codimension is
additive: two folds give a cusp, so p_composite = p₁ + p₂ − 2. Degeneracy orders
neither add nor max; their codimensions do. Textbook, graded N0 in the
registration, and the numerical check verifies essentially nothing beyond
self-consistency.

**The live reading exists only because [D6](../experiments/D6-support-singularities/)
moved the ground after D5 was filed.** D5 assumed the classifier was a single
integer *p*; D6 showed *p* was the q₁ = 2 slice of a pair. So the open question
became what happens when Φ carries more than two terms — and the prediction is a
**staircase**, each higher term contributing a plateau at 1 − q₁/q_j.

## What I found

**The arithmetic is enumeration.** Terms queue rather than combine. Eleven
plateaus across five systems land within **0.0068** of prediction, including a
genuine **three-step staircase** for a four-term potential (0.5068 / 0.6645 /
0.7452 against 0.5 / 0.6667 / 0.75). The ratio rule
(1 − θ_j)/(1 − θ_{j+1}) = q_{j+1}/q_j holds in all six comparisons, worst error
0.033. So the staircase alone recovers the higher exponents, and the terms do not
interact.

**And almost none of that was in doubt** — which the registration said in advance.
Each plateau value is D6's formula applied to one pair; the ratio rule is those
values divided. Declared identities before the run.

**The one measured thing is the squeeze.** Raising B₃ narrows the lower plateau,
direction registered and confirmed, and the useful number falls out of the last
two rows: **a regime must exceed its visible plateau by ≈ 2.25 decades**,
consistently (6 → 3.75, 10 → 7.75). Below ~2.25 decades a plateau is invisible at
±0.04 tolerance.

Registered as *"squeezed out below ~1 decade."* Measured **~2.25**. The direction
and the existence of a threshold hold; **the registered threshold was optimistic
by about a factor of two**, and that is the registration being wrong rather than
the claim.

That number does real work: it converts
[P8](../experiments/D1-chart-invariance/P8-REREGISTRATION.md)'s failure into a
condition. P8's Blume–Capel sextic plateau never established because its regime
did not span 2.25 decades — not because the two-regime picture was wrong.

## Decisions

- **D5 confirmed, graded N0–N1.** It closes the register without adding a law.
  That is a legitimate outcome for a stone whose own registration predicted
  exactly it, and the staircase picture is now checked rather than assumed.
- **No catalog or floor change.** Nothing here promotes or demotes anything.

## The register, closed

Six stones filed, six worked:

| | outcome | novelty |
|---|---|---|
| **D1** | chart claim confirmed in the strong form | N2 for the classification, N0–N1 for the formula |
| **D2** | the P0 answered — no fourth floor, the scheme layer is the gauge group | N2 architectural, N0–N1 for the group analysis |
| **D6** | D1's *p* generalized; floor 3's classifier is a ratio | N2 for "one classifier", N0–N1 for the formula |
| **D3** | **falsified** — transfer needs mechanism *and* chart-freedom | replacement is N1–N2 |
| **D4** | **falsified** — the amplitude/exponent axis was a confound | survivor N0 |
| **D5** | confirmed, but confirms the undoubted | N0–N1 |

**Two killed by their own registered falsifiers, one dissolved a standing P0, one
generalized another, one confirmed nothing new.** The register's opening section
set the base rate — *"the base rate for 'an AI noticed a new universal law' is
dominated by rediscovery"* — and the outcome is consistent with it. The single
most valuable output was not a law but a **correction to how the repo reads its
own results**: S5's and S7's "domain-specific exponents" were a chart artifact,
and `ladder-vs-transfer`'s finding was conditional on a shared chart in a way
nobody had noticed.

## The process record, which is now the more instructive half

Five failures, and a pattern:

1. **D1 P5** — direction stated backwards (÷a for ×a).
2. **D1 P8** — direction backwards again, in the same experiment.
3. **P8 re-run** — direction backwards a *third* time (crossing sought downward
   when the slope rises).
4. **D3** — a tie-broken Spearman manufacturing a spurious +1.00 from clipped
   zeros; **D4** — an empty fit returning 0.0000 in silence.
5. **D5** — a `pkill` returning exit 144 killed the *shell*, not the process, so a
   superseded run finished afterwards and **overwrote the verdict with
   stale-coefficient results**. Those numbers were read and nearly written up.

Every one was caught by a number looking wrong — too round, or moving the wrong
way, or two computations of the same thing disagreeing. **None was caught by the
pre-registration.** The registration catches conceptual errors (what counts as
evidence); it is blind to implementation errors, and blind to the environment.

The D5 case is the sharpest: P1 and P4 computed the *same system* and reported
0.00 and 3.75 decades for the same plateau. Two numbers that cannot both be right
for one computation. **The habit that caught it — checking that independent paths
to the same quantity agree — is worth more than any single result in this
register**, and it should be a standing rule: every experiment that computes a
quantity twice should be made to say so.

## Next

- **The register is closed but not finished.** Two debts remain, both logged twice:
  a **real ratio test** for D6 (two domains sharing q₁/q₂ but not q₁ or q₂), and
  **measuring** the chart tags in [`CHARTS.md`](../invariants/CHARTS.md) rather
  than assigning them by inspection.
- **[`CHARTS.md`](../invariants/CHARTS.md)'s prediction 2 is the cheapest open
  test in the repo** — Pareto and the information bottleneck are predicted to
  out-transfer higher-rung chart-dependent entries, which is the one place the
  chart axis and the ladder predict opposite orderings.
- **New stones need a new engine.** Residue mining is close to exhausted: it
  produced D1 (excellent) and D4 (a confound), and the difference was that D1
  mined *unexplained* numbers while D4 mined numbers that already agreed. The
  repo's remaining unexplained residues should be inventoried before more stones
  are filed.
