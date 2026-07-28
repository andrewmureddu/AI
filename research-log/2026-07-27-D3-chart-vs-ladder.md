# 2026-07-27 — D3: the ladder is one factor of two, and the transfer cliff needs a shared chart

**Worked on:** [D3](../questions/UNKNOWN-LAWS.md) — is the ladder a chart-invariance
count?
**Change:** D3 falsified as filed (its own registered falsifier fired); the
rung-label reading it attacked is falsified too; replacement is a two-factor
statement. A **boundary condition is added to
[`ladder-vs-transfer`](../experiments/ladder-vs-transfer/)**, an existing repo
result: its finding holds only when the two domains share a measurement chart, a
condition the original run never stated. S22 sharpened and mostly retired.

## What I did

D3 conjectured that if [D1](../experiments/D1-chart-invariance/) is right, transfer
has a mechanical answer — a correspondence transfers **iff** it is chart-invariant
— making the ladder a count of quotiented-out coordinate choices rather than a
scale of epistemic quality.

The stone came with a two-sided falsifier naming the exact off-diagonal cells, so I
built both, because that is where D3 and the rung-label reading predict *opposite*
outcomes: a shared-**mechanism** correspondence stated chart-**dependently**, and a
different-mechanism one stated chart-**freely**. Design: the existing
ladder-vs-transfer harness (same generators, same metric) crossed with a chart
factor (B records on y ↦ sgn(y)|y|^a, the G_pow group of D1/D2 acting on the
measurement axis) and a statement factor (compare the shape of Y, chart-dependent,
versus the shape of ln|Y|, chart-free since standardizing kills the factor a).

## What I found

**Both readings fail, in opposite directions.**

- **P2 kills the rung-label reading.** Under a chart distortion the CLT still
  genuinely holds in B — the mechanism is untouched — yet L3 collapses from 0.916
  to 0.000 and L4 from 0.894 to 0.000. At a = 0.7 and a = 0.5 the ladder does not
  merely weaken, it **inverts**: the word-only L1 correspondence (0.723, 0.562)
  beats the theorem-backed L4 one (0.565, 0.286).
- **P4 kills D3.** With the claim stated chart-freely the low rungs still fail:
  L2 = 0.373, L1 = 0.037, against L3/L4 at 0.833/0.816. The stone's registered
  falsifier was *"an L2 correspondence that is chart-invariant and still fails to
  transfer."* That is this cell. **Chart-invariance is necessary, not sufficient.**

**The survivor is a two-factor statement**: transfer needs a shared mechanism *and*
a chart-free statement of it. The ladder measures the first. D3 proposed it was
secretly measuring the second; it is not.

**The sharper and more useful form** came out of a per-column analysis I added
after seeing the table: Spearman(rung, skill) *within* each measurement
convention. Under a chart-free claim it is **+0.80 in every column** — and +0.80
is exactly what the original ladder-vs-transfer experiment reported. Under a
chart-dependent claim it runs +0.80 / +1.00 / −0.60 / −0.80 / +0.80 / +0.80. So
**chart-freedom is the precondition under which the ladder is predictive at all.**

Note the a = 0.85 column especially: Spearman is nominally *perfect* (+1.00) while
the **cliff has vanished** — L2 = 0.756 against L3 = 0.769, a gap of 0.013 where
the undistorted cliff is 0.43. A mild chart distortion destroys the ladder's
discriminating power while preserving its order; a stronger one inverts the order.
Rank correlation alone would have missed this.

## Decisions / level changes (with reasons)

- **D3 retired as filed**, replaced by the two-factor claim. Logged in
  [`UNKNOWN-LAWS.md`](../questions/UNKNOWN-LAWS.md).
- **A boundary condition is added to
  [`ladder-vs-transfer`](../experiments/ladder-vs-transfer/)** — a result already
  in the ledger. That experiment lives entirely in the `raw, a=1` cell: it
  compared two domains sharing a chart by construction and never said so. Its
  finding is real but **conditional on a shared measurement chart**, and the
  conditional was invisible until the chart was varied. This is the first time in
  this arc that a D-stone has revised an existing experiment rather than adding to
  the architecture.
- **S22 ("the ladder is a renormalization scale") is mostly retired.** D3 was filed
  as its sharper version; the identification form is dead. What survives is that
  the ladder is one factor of two and the other is a quotient.
- **It explains a pattern the repo kept recording.** S5 and S7 each found a
  mechanism that transferred while its exponents did not, and filed the exponents
  as "domain-specific." D1 showed that was a chart artifact; D3 shows the same
  thing one level up, at the level of the method — those were correspondences with
  a shared mechanism and a chart-dependent statement, i.e. the P2 cell in the wild.

## Honest limits, including a process failure

- **This experiment has no `PREREGISTRATION.md`, and I am not going to write one
  now.** The design and the opposing predictions were fixed before the run (module
  docstring, and the README's design section), but no numerical thresholds were
  registered. What *was* registered — on 2026-07-26, when the stone was filed — is
  the falsifier that decided it, and it fired. Backdating a pre-registration file
  would be a fabrication. Recorded as a process deviation, the fourth in this
  register's short life and the first that is an omission rather than a
  misclassification.
- **Identity/risk split, done after the code** per the correction logged in D6:
  P3's chart-immunity is an **identity** (standardizing ln|y| removes the factor a
  by construction); P2's collapse is **forced in direction** but not in magnitude,
  and the inversion was not forced; **P4 is the genuinely at-risk result** — a
  chart-free statistic could have discriminated nothing, making the framing
  vacuous, and instead it preserves the full cliff.
- **Skill is floored at 0** and every raw cell clips at a ≥ 1.5, so the per-column
  Spearman is computed on unclipped skill. Ranking the clipped values ranks a
  column of ties and the tie-break manufactures a spurious +1.00 — caught and
  fixed mid-analysis.
- **One invariant family, synthetic, one chart group.** Inherited from the original
  harness. The real version is still what that experiment already named: several
  *different* catalog invariants, real data.

## Next

1. **The chart-freedom axis deserves a place in the methodology.** If transfer
   needs two factors and we only grade one, entries should carry a second tag:
   *is this correspondence stated in chart-free terms?* Cheap to add, and it
   predicts which catalog entries will fail to transfer despite a high rung.
2. **Re-run the original ladder-vs-transfer with the boundary stated**, or simply
   annotate it — done here, but the experiment's own README should carry it.
3. **D4** (amplitudes transfer, exponents don't) is now the last unworked stone
   besides D5, and D3 supplies its mechanism: an amplitude can be made chart-free,
   a bare exponent cannot.
4. Still outstanding from D1: **re-register P8's δa³**. Third time logged.
