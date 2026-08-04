# D3 — is the ladder a chart-invariance count? (result)

**Question ([D3](../../questions/UNKNOWN-LAWS.md)):** if [D1](../D1-chart-invariance/)
is right, "does this correspondence transfer?" might have a mechanical answer —
**it transfers iff it is chart-invariant** — which would make the
[ladder](../../METHODOLOGY.md) not a scale of epistemic quality but a count of how
many coordinate choices have been quotiented out.

**Status: D3's biconditional is FALSIFIED — its own registered falsifier fired.
But so is the rung-label reading it was attacking. The replacement is a two-factor
statement, and it adds a boundary condition to
[`ladder-vs-transfer`](../ladder-vs-transfer/) that the original run never stated.**

Run it: `python3 run.py` (numpy only, ~1 min, deterministic).
Raw output: [`verdict.json`](./verdict.json).

---

## Design

The [ladder-vs-transfer](../ladder-vs-transfer/) harness — same generators, same
metric — crossed with two new factors:

| Factor | Values |
|---|---|
| **rung** | L1–L4, the original generators (depth of shared mechanism) |
| **chart** | domain B records on y ↦ sgn(y)·\|y\|^a, a ∈ {1, 0.85, 0.7, 0.5, 1.5, 2} — the **G_pow** group of [D1](../D1-chart-invariance/)/[D2](../D2-gauge-group/), now acting on the measurement axis |
| **statement** | **raw**: compare the standardized shape of Y (chart-**dependent**) · **log**: compare the standardized shape of ln\|Y\| (chart-**free**, since ln\|y\|^a = a·ln\|y\| and standardizing kills the factor a) |

The point of the design is to **break the correlation between rung and
chart-freedom**, by building the two off-diagonal cells D3's falsifier names —
a shared-mechanism correspondence stated chart-dependently, and a
different-mechanism one stated chart-freely. In those cells the rung-label theory
and D3 predict *opposite* outcomes.

## Results

Transfer skill (1 = A's law transfers, 0 = useless):

**Chart-dependent claim (raw)**

| | a=1 | a=0.85 | a=0.7 | a=0.5 | a=1.5 | a=2 |
|---|---|---|---|---|---|---|
| L4 | 0.894 | 0.775 | 0.565 | 0.286 | 0.090 | 0.000 |
| L3 | **0.916** | 0.769 | 0.559 | 0.282 | 0.129 | 0.000 |
| L2 | 0.484 | 0.756 | **0.773** | 0.438 | 0.000 | 0.000 |
| L1 | 0.033 | 0.467 | **0.723** | **0.562** | 0.000 | 0.000 |

**Chart-free claim (log)** — identical in every column:

| | every a |
|---|---|
| L4 | 0.816 |
| L3 | 0.833 |
| L2 | 0.373 |
| L1 | 0.037 |

### P1 — the harness is faithful

Raw statement, undistorted chart reproduces the original result exactly:
**0.03 / 0.48 / 0.92 / 0.89**.

### P2 — shared mechanism, transfer lost (kills the rung-label reading)

Under a chart distortion the CLT still genuinely holds in domain B — the mechanism
is untouched — yet the correspondence collapses: L3 from 0.916 to 0.000, L4 from
0.894 to 0.000. And at a = 0.7 and a = 0.5 the ladder does not merely weaken, it
**inverts**: the word-only L1 correspondence (0.723, 0.562) *beats* the
theorem-backed L4 one (0.565, 0.286).

### P3 — a chart-free restatement restores transfer and is immune

Spread across all six charts: **0.0000**. Declared below as an identity.

### P4 — the registered falsifier fires

With the claim stated chart-freely, the low rungs **still fail**: L2 = 0.373,
L1 = 0.037, against L3/L4 at 0.833/0.816. D3's registered falsifier was *"an L2
correspondence that is chart-invariant and still fails to transfer."* That is
exactly this cell. **Chart-invariance is necessary for transfer; it is not
sufficient.**

### P5 — does the ladder order transfer?

Spearman(rung, skill) computed **within** each column, ranked on unclipped skill:

| statement | a=1 | a=0.85 | a=0.7 | a=0.5 | a=1.5 | a=2 |
|---|---|---|---|---|---|---|
| raw | +0.80 | +1.00 | **−0.60** | **−0.80** | +0.80 | +0.80 |
| **log** | **+0.80** | **+0.80** | **+0.80** | **+0.80** | **+0.80** | **+0.80** |

Two things this shows that the raw skills alone do not:

- Under a **chart-free** claim the ladder orders transfer at **+0.80 in every
  chart** — and +0.80 is exactly the Spearman the
  [original experiment](../ladder-vs-transfer/) reported.
- Under a **chart-dependent** claim the ordering is unstable in both directions.
  At a = 0.85 it is nominally perfect (+1.00) but the **L2/L3 separation has
  collapsed** — L2 = 0.756 against L3 = 0.769, a gap of 0.013 where the
  undistorted gap is 0.43. So a mild chart distortion destroys the ladder's
  *discriminating power* while preserving its order; a stronger one inverts the
  order outright.

> **Terminology, corrected after a concurrent retraction.** An earlier draft of
> this README called the L2/L3 gap "the cliff." While this was being written,
> [paper 1](../../paper/transfer-cliff.md) §3.3 **retracted** that reading of the
> source experiment: the adjacent steps are L1→L2 = 0.451 and L2→L3 = 0.432, the
> same size, so the L2/L3 step is not uniquely large. Nothing measured here
> depends on it — the numbers above are gaps and orderings, not step
> comparisons — but the word is wrong and has been removed.

### The price of chart-freedom (added post-merge)

Paper 1 also measured something this experiment needed and did not have: **the
metric's own ceiling, 0.920 ± 0.023**, obtained by scoring a domain against an
independent draw of itself. That makes the chart-free column readable in absolute
terms for the first time:

| | L3 | L4 | vs ceiling 0.920 |
|---|---|---|---|
| shared chart, chart-**dependent** claim | 0.916 | 0.894 | **complete transfer** |
| any chart, chart-**free** claim | 0.833 | 0.816 | ~0.09 **short** |

So chart-freedom is **not free**. Stating the correspondence invariantly buys
immunity to the measurement convention — the whole point — but costs about 0.09
of transfer skill against a ceiling that the chart-dependent statement *reaches*
when the two domains happen to share a chart. The invariant statement discards
real information (here, everything the sign and scale of Y carried). That is a
genuine trade-off the stone did not anticipate, and it sharpens the replacement
claim: chart-freedom is what makes transfer *robust*, not what makes it *maximal*.

The pooled predictor comparison over all 48 cells (rung alone +0.481, claim
chart-free alone −0.078, mechanism alone +0.492, registered conjunction +0.525) is
reported in `verdict.json` but is the **weaker** analysis: the binary conjunction
mispredicts the mild-distortion cells, because chart-dependence degrades transfer
*continuously* with distortion size rather than as a step.

---

## Verdict

**Both readings are wrong, and they fail in opposite directions.**

- **D3 as filed ("transfers iff chart-invariant") is falsified** by its own
  registered falsifier: a chart-invariantly-stated L2 correspondence still fails
  (0.373). Chart-freedom does not manufacture a shared mechanism.
- **The rung-label reading is also insufficient**: a genuinely shared mechanism,
  stated chart-dependently, transfers at 0.000 — and can be beaten by a word-only
  correspondence.

**Replacement (the survivor).** Transfer requires **two independent things**:

```
   transfer  <=  (mechanism is shared)  AND  (the claim is stated chart-freely)
```

The ladder measures the first. D3 proposed it was secretly measuring the second;
it is not. Chart-freedom is a genuinely separate axis that the ladder does not
capture — which is *why* it took a designed experiment to see it, since in
ordinary practice the two are confounded (people usually state a correspondence in
whatever chart both domains happen to share).

**Sharper form, and the useful one:** chart-freedom is **the precondition under
which the ladder is predictive at all.** Rung predicts transfer at +0.80
regardless of measurement convention when the claim is chart-free, and predicts it
unstably — including backwards — when it is not.

**This adds a boundary condition to an existing repo result.** The
[original ladder-vs-transfer experiment](../ladder-vs-transfer/) lives entirely in
the `raw, a=1` cell: it compared two domains that shared a chart by construction,
and never said so. Its finding — *ladder level predicts transfer* — is real but
**conditional on a shared measurement chart**, and the conditional was invisible
until the chart was varied.

**It also explains a pattern the repo kept recording.** [S5](../S5-noise-thresholds/)
and [S7](../S7-critical-slowing/) both found mechanisms that transferred while
their exponents did not, and filed the exponents as "domain-specific."
[D1](../D1-chart-invariance/) showed that was a chart artifact. D3 shows the same
thing at the level of the *method*: those were correspondences whose mechanism was
shared but whose statement was chart-dependent — the P2 cell, in the wild.

**Relation to [S22](../../questions/SPECULATIVE.md).** S22 conjectured the ladder
is a renormalization scale; D3 was filed as the sharper version of it. The
identification form is dead. What survives is weaker and more useful: the ladder is
one factor of two, and the other factor is a quotient.

---

## Boundaries and process notes

- **Process deviation, stated plainly: this experiment has no
  `PREREGISTRATION.md`.** The design and the opposing predictions were fixed
  before the run (they are in the module docstring and in the design section
  above), but no numerical thresholds were registered. What *was* registered, on
  2026-07-26 when the stone was filed, is the falsifier that decided it — *"an L2
  correspondence that is chart-invariant and still fails to transfer"* — and that
  is the result. Writing a pre-registration file now and dating it before the run
  would be a fabrication, so there isn't one.
- **Identity/risk split, done after the code** — per the correction logged in
  [D6](../D6-support-singularities/) after three registration slips:
  - **Identity:** P3's chart-immunity. Standardizing ln|y| removes the factor a by
    construction; the 0.0000 spread could not have come out otherwise.
  - **Forced in direction, not in magnitude:** P2's collapse. A nonlinear map on
    one side of a shape comparison must degrade it. The *inversion* at a ∈ {0.5,
    0.7} was not forced.
  - **Genuinely at risk, and the decisive result:** P4. A chart-free statistic
    could have been so weak that it discriminated nothing, making the whole
    framing vacuous. It is not: the chart-free claim preserves the full L1→L4
    separation (0.037 / 0.373 / 0.833 / 0.816).
- **The chart is applied to the centred reading**, which is what makes it a clean
  power map. Real charts of this kind (log-returns, decibels, magnitude scales)
  are all defined relative to a reference level, so this is not a contrivance —
  but it is an assumption.
- **Skill is floored at 0**, and under the expansive charts (a ≥ 1.5) every raw
  cell clips. The per-column Spearman is therefore computed on **unclipped**
  skill; ranking the clipped values ranks a column of ties and the tie-breaking
  manufactures a spurious +1.00. The unclipped table is in `verdict.json`.
- **One invariant family, synthetic.** Inherited from the original harness: this
  is the CLT/Gaussian limit only, with generated rather than observed data. The
  real version remains what the original experiment already named — several
  *different* catalog invariants, real data.
- **Only one chart group tested (G_pow).** Whether the same two-factor structure
  holds under richer re-measurement groups is untested.
