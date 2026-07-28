# 2026-07-28 — D9: an inconclusive experiment, and why the design failed

**Worked on:** [D9](../questions/UNKNOWN-LAWS.md), opened today as the half
[D3](../experiments/D3-ladder-as-quotient/) could not reach.
**Change:** new experiment
[`D9-unpinned-chart-transfer/`](../experiments/D9-unpinned-chart-transfer/), run and
**recorded as inconclusive**. No claim anywhere moves. `SYNTHESIS.md` §6 notes it;
the register carries the stone with its failure and the concrete fix.

## What I did

D3 refuted "the ladder is a chart-invariance count" on the CLT harness — but that
harness's chart is *n*, a **count**, which aggregation composes additively. The
pinning was measured, not assumed, and by [D2](../derivations/D2-gauge-of-the-tower.md)'s
rule (i) magnitudes are facts wherever it holds. So D3's refutation covers the
pinned regime and is silent about the one D1 and D7 were actually built in: a
distance-to-threshold, where G_pow is available and no coordinate is canonical.

D9 rebuilt D3's four rungs there — same rung logic, same robust-shape transfer
metric, same residue estimator — with **every domain supplying its own coordinate**
(ε = δ^c, c differing per domain), which is the variable D3's harness could not
move. Two guards went into the registration: transfer read from *distribution
shape* and the residue from *scaling exponents*, so the two readouts come from
different quantities; and the registered bar for the leg set as **stability of the
ordering across sampling settings**, since D3's residue produced an ordering in its
main run that dissolved on re-sampling.

## What I found

**The residue legs are clean.** Same-class domains sit at **0.0009** and **0.0020**
from the reference despite coefficients differing by up to 18× *and* different
charts; the different-class domain sits at **0.2606** against a predicted
0.214 ± 0.06. Stable to four decimals across three ε-windows and two quadrature
resolutions. The bare exponent behaves exactly as predicted too, spreading **3.33×**
across domains of the same class where D3's spread was **1.013×** — the mechanism is
real: on an unpinned chart each domain's coordinate choice multiplies the exponent,
so it is not shared even within a class.

**And none of that matters, because the transfer leg failed.**

| rung | transfer skill | registered |
|---|:--:|:--:|
| L4 | 0.988 | > 0.80 ✓ |
| L3 | 0.984 | > 0.80 ✓ |
| L2 | **0.938** | **< 0.40 ✗** |
| L1 | **0.664** | **< 0.40 ✗** |

The ordering clause passed and so did the stability clause I had registered as the
real bar. **Both are worthless here**, because the thing being ordered spans 0.938
to 0.988 among the rungs that matter. D3 had a factor of 28 to work with.

**Why, measured rather than asserted.** Excess kurtosis is the standardized shape
in one number: A (p = 4) −0.900, L4 −0.936, L3 −0.862, **L2 (p = 6) −1.036**, and
the metric's Laplace reference **+2.961**. So crossing the class boundary moves the
shape by 0.14 while the reference sits 2.96 away, and every singular rung normalizes
to a skill near 1. A far-tail readout does not rescue it: the q₉₉.₅/q₇₅ ratio
separates p = 4 from p = 6 by 0.154 against a within-class spread of 0.076 — 2:1,
where the residue's separation is 130:1.

**So the design error is structural.** The CLT harness works because crossing *its*
class boundary changes the law utterly — a Gaussian shape versus a stable one. Here
the two classes have nearly the same law. **I built a harness whose rungs differ in
the residue but not in the law**, which cannot test whether one predicts the other.
The registration checked that the two readouts came from different quantities, which
they did; it never checked that the readout had any **range** across the rungs. That
is a new entry on the list of things to verify before registering, and it is not the
same as any of the four tolerance failures D7, D8 and D3 logged.

## The by-product, which is worth more than the intended result

**The degeneracy order *p* is nearly invisible in the shape of the fluctuations.**
D1, D7 and D8 all establish it as the classifier of floor-3 singularities, and it
is — of the *scaling structure*. It is not a classifier of anything an observer sees
directly in the distribution. Two consequences the arc should carry:

- It explains why [D6](../experiments/D6-support-singularities/)'s kurtosis
  estimator worked: it spanned q = 0.5 to 8 (+22.2 to −1.08). Between **adjacent**
  degeneracies the same estimator is blunt, and anyone reusing it should expect that.
- It is mildly awkward for the arc's rhetoric. "The residue classifies floor 3" is
  true and has been measured four times; "the classification is what you would
  notice about the system" does not follow, and D9 is the first result that
  separates the two.

## Decisions

- **D9 recorded as inconclusive, not spun.** P2 failed, P4 missed its tolerance, P3
  is uninformative given P2, and only P1 carries weight — and P1 is a re-measurement
  of D7 in a new coordinate arrangement rather than a new result. The register entry
  says exactly that.
- **The no-tuning guard held.** The registration fixed the models and said that
  changing them after seeing the numbers voids the run. They were not changed.
  Fixing this experiment means building a *different* harness, and doing it inside
  this one would have made the registration meaningless.
- **The concrete fix is registered rather than executed**, so the next attempt
  starts from a stated design instead of an improvised one:
  [D6](../experiments/D6-support-singularities/) already has rungs whose *laws*
  differ — q₁ = 1 versus q₁ = 2 gives excess kurtosis +3.0000 versus 0.0000, a
  separation 20× larger than p = 4 versus p = 6. That harness, with each domain
  still supplying its own coordinate, has both the dynamic range D9 lacks and the
  unpinned chart D3 lacks.

## Process notes

**Two code faults, both mine, both cheap.** L1's residue came out as a `nan` because
an ordinary quadratic well has no third derivative, so one observable is identically
zero; fixed to report the degeneracy explicitly — and the fixed version is *sharper*
than what I registered, since "undefined" separates L1 more strongly than the zero
ray I predicted. Separately a patch script broke on an inserted docstring containing
a triple quote. Harmless, but the second scripting self-injury of the session after
the `pkill` incident, and both came from writing code that manipulates code rather
than from the physics.

**The failure rate is worth stating plainly.** Of the five stones worked in this
session, D7 and D8 produced results with tolerance misses, D3 produced a clean
falsification, and **D9 produced nothing usable**. That is roughly the rate the
register should expect, and it is the first session entry where the honest summary
of an experiment is "this did not work."

## What this opens

- **D3's open half is still open**, now with a stated design for the next attempt.
- **Marginal directions** (weight exactly 0, hence logarithms) from D8 — untested,
  still cheap.
- **Is r forced to equal the codimension?** From D8, untested.
- **Essential singularities** remain the unclassified remainder, unchanged since D6.
