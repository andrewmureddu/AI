# 2026-07-28 — D3: the ladder is not a chart-invariance count

**Worked on:** [D3](../questions/UNKNOWN-LAWS.md), the discovery register's oldest
unworked stone, open since 2026-07-26 and flagged as "the cheapest thing left" in
three consecutive log entries without anyone running it.
**Change:** new experiment
[`D3-ladder-as-quotient/`](../experiments/D3-ladder-as-quotient/); **D3 falsified**
and marked so in the register. No other document's claims change — D3 was never
load-bearing for anything, which is part of why it kept getting deferred.

## What I did

D3 conjectured that a correspondence transfers **iff** it is chart-invariant, and
therefore that the ladder is not a scale of epistemic quality but *a count of how
many coordinate choices have been quotiented out*. Two things made it runnable now
and one made it weaker than when it was written.

- **"Count" acquired a referent.** [D7](../experiments/D7-residue-projective/) made
  it n − 1 and [D8](../experiments/D8-grassmannian-residue/) made it r(n−r), with an
  estimator validated across three classes.
- **The chart was already there.** The
  [ladder-vs-transfer harness](../experiments/ladder-vs-transfer/) varies *n*, the
  number of contributions in an aggregate. That is exactly a control parameter every
  observable varies along, so D7/D8 apply without adaptation.
- **Its supporting evidence had been retracted.** D3 leans on the transfer *cliff* —
  "the jump exactly at L2/L3", "a quotient is not a matter of degree". Paper 1
  [retracted the step reading](../paper/transfer-cliff.md) (L1→L2 = +0.451 ≈
  L2→L3 = +0.432). So the sharpness argument was dead before the run, and the
  registration recorded that this experiment did not get to use it.

The registration also names the failure mode that actually threatens a stone like
this. D3 is a claim about *the repo's own instrument*, so no field owns it and no
specialist will object; the risk is not rediscovery but **self-flattery**, since D3
surviving would upgrade the ladder from a convention to a measured structure. So the
primary prediction was registered as the outcome I expected — which falsifies D3 —
with the D3-saving outcome written down explicitly so it could not be waved away
afterwards.

## What I found

**D3 is false, on its own registered falsifier horn (i).**

| rung | transfer skill | residue distance from A | bare exponent distance |
|---|:--:|:--:|:--:|
| L1 | 0.033 | n/a — **rank 0**, no ray | 0.503 |
| L2 | 0.484 | 0.0327 | 0.181 |
| L3 | 0.916 | 0.0120 | 0.006 |
| L4 | 0.894 | 0.0081 | 0.005 |

The chart-free residue does not separate the domains that transfer from the one that
does not. **And the interesting part is how thoroughly it fails.** The main run's
distances *do* order the rungs, which is not what I predicted, so I checked what
carries that ordering before counting the leg. Re-measuring on a different n-window
at three sample sizes:

| M | L4 | L3 | L2 | ordering |
|:--:|:--:|:--:|:--:|---|
| 800 | 0.0014 | 0.0294 | 0.0268 | L4 < L2 < L3 |
| 3000 | 0.0310 | 0.0124 | 0.0202 | L3 < L2 < L4 |
| 9000 | 0.0189 | 0.0135 | **0.0097** | **L2 < L3 < L4** |

**The ordering scrambles completely, and at the best-estimated setting the domain
that fails to transfer is the closest to the reference.** Against that, transfer
skill spans a factor of 28 and is stable to ±0.02 over 8 seeds. So the residue
carries no information about transfer at all — reached more strongly than the flat
tie I had registered.

**The count reading fails separately.** L1's aggregate does not depend on *n*, so
its slope vector is the zero vector: rank 0, count 0. Every other domain has rank 1,
count n − 1 = 5. A quantity taking **two values across four rungs** cannot be a
four-valued ladder, and the one boundary it does place — L1 versus everything — is
the one that matters least.

**What does place the boundary is the bare exponent.** 1/α orders all four rungs
exactly as transfer does, with a 30× gap at L2/L3. That looks like a paradox given
D7 — the magnitude is supposed to be the gauge part — and the resolution is the leg
I am most glad I registered. **G_pow was never available here.** Aggregation
composes additively: n₁ contributions then n₂ is n₁ + n₂ of them, and under n ↦ n^a
that breaks, with defect **0** at a = 1 and **0.293 / 0.500 / 0.414** at 1.5 / 2 /
0.5. This is [P-D](../experiments/PD-allometry-reduction/)'s leg F with the count in
place of the mass. The chart is pinned to G_diff, and by
[D2](../derivations/D2-gauge-of-the-tower.md)'s rule (i) exponents are facts there.

**So D3 read the wrong half of a sentence the map already had.** D2 established:
*within a domain exponents are facts; across domains only ratios, signs and counts
are.* D3 assumed the ladder lives on the second clause. On this harness it lives on
the first, because additivity pins the chart.

## What replaces it

Smaller than D3, and measured: transfer here is predicted by **basin membership**,
and basin membership is a claim about magnitudes being *equal* — not about ratios.
That also explains something D3 could not. Paper 1 found the real structure is a
**ceiling**, not a step: L2 saturates at ~0.54 however much data it gets. A quotient
story predicts a step, because a quotient is not a matter of degree. A basin story
predicts a ceiling, because more data cannot move an exponent into another basin.
The ceiling is what was measured.

## Decisions

- **D3 marked falsified** in the register, with the replacement stated. Kept in
  full, per house style — knowing why a tempting stone fails is the point.
- **No other document changes.** D3 was cited as "the cheapest next thing" in three
  log entries and was load-bearing for nothing, so its death costs the map nothing
  and removes a standing invitation.
- **No registered tolerance was missed** — the first time in this arc, after D7's
  three and D8's one. The registration set them from the harness's published
  seed-to-seed spread and pre-checked the estimator's numerical resolution, which
  were exactly the two failure categories D7 and D8 logged. One unregistered
  separation constant in the code is disclosed in the write-up.

## Two process notes

**The dissolution pattern did not recur, and that is informative.** The previous
three registered questions all dissolved rather than resolving (D2's fourth floor,
D6's p = ∞, D8's coupling), and the last entry proposed writing down what a stone
presupposes as a cheap discipline. D3 **did not** dissolve — it was answered, and
the answer was no. Worth recording, because a pattern that predicts every outcome
predicts nothing; this one has now been checked against a case where it did not
apply.

**A self-inflicted error worth logging.** Mid-run I killed a slow background job
with `pkill -f "python3 -"`, and the pattern matched the shell running that very
command, killing the whole thing including the edit that had not been written yet.
No data was affected — the experiment is deterministic and was simply re-run — but
it cost a cycle. Broad process-pattern kills are not safe from inside the process
they might match.

## What this opens

- **The real test of a chart-invariance reading needs an unpinned chart.** This
  harness's chart is pinned by additivity, so it can only ever test the
  within-domain half of D2's rule. A transfer study whose control parameter is a
  genuine distance-to-threshold — where G_pow *is* available — would be the honest
  escalation, and no experiment in the repo currently has one.
- **Marginal directions** (weight exactly 0, hence logarithms) remain untested from
  D8, and are still cheap.
- **Is r forced to equal the codimension?** From D8, untested.
- **Essential singularities** remain the unclassified remainder, unchanged since D6.
