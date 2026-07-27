# 2026-07-27 — D7: the residue is the log-slope vector modulo the diagonal, and it has a count

**Worked on:** [D7](../questions/UNKNOWN-LAWS.md), opened today as the successor to
the map's P0 — the live question that the P-D/D2 reconciliation left in
[`FLOORS.md`](../invariants/FLOORS.md) §4 and [`SYNTHESIS.md`](../SYNTHESIS.md)
§7.0.
**Change:** new derivation [`D7-the-residue.md`](../derivations/D7-the-residue.md),
new experiment [`D7-residue-projective/`](../experiments/D7-residue-projective/),
D7 registered and run. **One standing statement in the map is corrected**: the
chart-free residue is not intrinsically an integer. §4 of `FLOORS.md` and §7.0 of
`SYNTHESIS.md` updated; no earlier measurement changed.

## What I did

The reconciliation two entries ago ended with a gap rather than a result: the
invariant residue had three members found by three routes — D2's codimension
p − 2 on a smooth germ, D6's q1/q2 on a support-type singularity, P-D's
θ = ln n/−ln(β²γ) on a branching scheme with no singularity and no Φ at all — and
"the residue is the ratio structure that survives the group" was, in that entry's
own words, *suggestive and currently contentless*.

So the question was whether a general statement exists that predicts something the
three members do not. Register rules: prior-art note first, then the identity/risk
split, then numbers. The prior-art note came out deflationary enough that I nearly
stopped — projectivization, weight vectors defined up to scale, Newton-polygon
slopes, scaling relations, the Π-theorem — all old, and §4's "novelty laundering by
generalization" anti-pattern is exactly the trap of restating a known special case
with the constants removed. What kept it alive was that the general form makes
three commitments the members individually do not, and two of them contradict what
the map currently says.

## What I found

**The residue is the log-slope vector modulo the *diagonal* ℝ⁺.** Relabelling the
control family, ε ↦ ε^a, multiplies **every** observable's log-slope by the **same**
scalar — the factor carries no observable index. So the orbits are rays, the
chart-free content is a point of ℝP^{n−1}, and concretely it is the set of slopes
of observables against *other* observables, d ln O_i/d ln O_j, in which no chart
appears. Eliminating the chart and taking the projective quotient are one operation
performed from the two ends.

**The unification leg is the one that carries the claim, and it is one estimator
handed three different pairs of measured quantities**, with nothing fitted:

| system | quantities | measured | must reproduce |
|---|---|:--:|---|
| smooth germ, p = 4 / 6 | y\* vs λ | 0.4996 / 0.2483 | D2's 0.5000 / 0.2503 |
| Φ = A\|y\|^q1 + \|y\|^q2, four pairs | A_c vs D | 0.5000, 0.5000, 0.6667, 0.6667 | D6's table |
| branching scheme, n = 2…10 | B vs V | 0.7495–0.7500 | P-D's 3/4 |

The third row is the one that decides it. Allometry has no singularity, no Φ, no
continuous chart and no thermodynamic limit, and the estimator that produced D2's
codimension returns P-D's 3/4 there unmodified.

**The count is the genuinely new part, and it is the Π-theorem.** n quantities and
one "dimension" — the chart — give n − 1 independent invariants. Every previously
known member of the residue has n = 2 and therefore exactly one invariant, which is
precisely why each looked like *the* residue rather than one coordinate among
several. Measured at n = 5 on a full all-orders germ: the six slope vectors span a
**line**, σ₂/σ₁ = 2.96e-3, so the quotient is ℝP⁴ and the count is 4.

**Two corrections to what the map says.**

- **The residue is not intrinsically discrete.** `FLOORS.md` and `SYNTHESIS.md`
  both read D2's result as "the chart-free residue is one integer, the codimension
  p − 2." A projective space has no distinguished rational points. D2's integer is
  inherited from Taylor orders being integers once smoothness pins q1 = 2 — change
  that hypothesis and it goes: Φ = A|y|² + |y|^{2π} measures **0.68169** (1 − 1/π),
  a germ with p = 2 + √2 measures **0.70698** (1/√2). *A smooth germ's residue is
  p − 2* stands; *the residue is an integer* does not.
- **D2's common-*a* commitment is derived, not stipulated.** D2 flagged it as
  load-bearing and left it as a condition one has to assume. It is the statement
  that the action is the *diagonal* ℝ⁺, and that is what "one singularity,
  approached along one family" means. Under the product group (ℝ⁺)ⁿ the orbits fill
  the orthant, so only the sign vector survives — which is exactly the fallback D2
  observed. Exhibited on the same observables with the same estimator:
  σ₂/σ₁ = 2.19e-3 under the diagonal, 0.227 under the product group, signs
  unchanged in both.

**A boundary the derivation had to state, and it held sharply.** The theorem is
about observables, and a *derivative with respect to the chart* is not one: it
transforms affinely, y_χ(a) = a·y_χ(1) + (a − 1), and including it destroys the
ratios. Measured against that formula with no free parameter: max error 6.4e-3,
against 2.003 for a pure weight. The cleanest form of it was not the statistic I
registered — the affine law predicts y_χ vanishes at a = 1/(1 − k), i.e. a = 3.010
for p = 4, and the measured value at a = 3 is **−0.0000**. *A weight-1 quantity
cannot change sign as the chart is relabelled.* This is why "susceptibility
exponents" need a convention and log-slopes do not.

**P-D's kink resolves, and the reconciliation's open item closes.** That note
flagged θ = min(1, ln n/−ln(β²γ))'s non-analyticity at nβ²γ = 1 as untested:
floor-3 degeneracy read in a scheme variable, or something with no floor-3
counterpart? It is where the two log-slopes are **equal** — the point [1 : 1] of
ℝP¹ — a wall in the residue's own space. The min *emerges* from the exact finite
sum rather than being imposed (RMS 5.6e-9), the wall locates at x = 1.00012, and it
is chart-invariant under coarse-graining.

## Two errors, both on record

**Three registered tolerances were missed** — P2's ratio at p = 6 (6.73% vs 5%),
P5c's coarse-graining (1.96e-6 vs 1e-10), P7's kink spread (4.7e-6 vs 1e-6). All
three to the same mechanism, and it is the one §5 of my own registration named:
G_pow is the *asymptotic* group, so finite windows carry corrections to scaling and
finite level counts carry x^N. Post-hoc diagnostics confirm the deviations shrink
at the predicted rates (the p = 6 window series runs 3.78% → 1.62% → 0.67% → 0.27%
→ 0.11% in proportion to y\* at the top of the window), but the registered numbers
stand as missed and the diagnostics are not counted as passes.

**This is the register's fourth slip and the first of a new kind.** The previous
three — D1's P5 direction, D2's resampling no-op, D6's P2 — were all the same
failure: calling a consequence of my own construction a test of it. This one is
different. The identity/risk split was right; the *tolerances* were wrong, set from
what I expected rather than from the error budget I had written one section
earlier. That is the more dangerous kind, because it can convert a passing claim
into a failing one or the reverse without touching any reasoning. The mechanical
fix: derive each tolerance from the scope section, inside the scope section.

**And a code bug, caught by disbelieving a diagnostic.** The kink locator's
parabolic refinement read an off-centre triple of the curvature array. The
registered P7 first reported x_c = 0.99220 — a miss — and the refinement series
read 0.99219, 0.99439, **1.10974**, 1.00153. The 1.11 is what exposed it: a locator
that is merely grid-limited does not get *worse* by a factor of 40 when the grid is
refined. Centred, the same code gives 1.00012 and a monotone series. Worth
recording because the wrong number was the *registered* one, and because nothing I
had planned would have caught it.

## Decisions

- **D7 graded N1–N2, with the split declared before the work**, not after: N0 for
  the projective quotient, N1 for the Π-theorem reading, N2 only for the
  cross-domain identification and for the three consequences. The mathematics is
  old in every component and the register entry says so in its own words.
- **`FLOORS.md` §4 and `SYNTHESIS.md` §7.0 corrected in place, additively.** The
  D2 blocks keep their original text and gain a correction after them, per house
  style — "the residue of a smooth floor-3 germ is p − 2" is what those passages
  should be read as saying.
- **The live question in `FLOORS.md` §4 is marked closed**, and the frontier's item
  0 with it. No measurement anywhere changed; one interpretation did.

## What this opens

- **The count at n − 1 is measured on separable models only.** Every germ here is
  one-dimensional or a direct sum. A genuinely *coupled* multi-dimensional
  singularity is the obvious escalation: does coupling preserve the count, or does
  it reduce the quotient's dimension below n − 1?
- **[D3](../questions/UNKNOWN-LAWS.md) is now much sharper and is the cheapest
  thing left.** It conjectured the ladder is "a count of how many coordinate
  choices have been quotiented out." That phrase had no definite referent when it
  was written; it does now — n − 1 — and the ladder-vs-transfer harness already
  exists.
- **[D5](../questions/UNKNOWN-LAWS.md)'s arithmetic question inherits an object.**
  It asked whether *p* obeys a sum rule; the thing that would carry the arithmetic
  is a point of ℝP^{n−1}, which is a sharper question than the one D5 states.
- **Essential singularities remain the unclassified remainder**, unchanged since
  D6. No leading power, no finite log-slope, nothing in D7 reaches them.
- **P-C** is still unrun, and still needs the selector/source distinction P-D found
  written into its registration.
