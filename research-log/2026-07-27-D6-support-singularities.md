# 2026-07-27 — D6: D1 was a special case, and floor 3's classifier is a ratio

**Worked on:** [D6](../questions/UNKNOWN-LAWS.md) — the remainder
[D2](../derivations/D2-gauge-of-the-tower.md) left when it answered the P0 for
degeneracy-type singularities only.
**Change:** floor 3's classification extends to support-type singularities;
[D1](../experiments/D1-chart-invariance/)'s *p* is reclassified as a special case;
the unclassified remainder narrows from "all of support-type" to "essential
singularities only." A third pre-registration slip goes on record, and the pattern
across all three is now nameable.

## What I did

D2 closed the fourth-floor P0 but explicitly did not reach support-type
singularities (S5's type S): they have no Taylor expansion, hence no degeneracy
order *p*, hence no codimension, so the residue D2 identified had nothing to
attach to there. D6 asks whether they are a separate class, whether p = ∞ is the
right label, or whether D1's classifier was narrower than it looked.

The productive move was to stop treating *p* as the primitive. Writing the two
leading terms of Φ at the singular point as A|y|^{q1} + B|y|^{q2} with A → 0 the
control, the same rescaling argument that made D1's formula an identity gives

```
        A_c ~ D^{(q2−q1)/q2} = D^{1 − q1/q2}
```

D1 is the case **q1 = 2** — which is what *smoothness forces*, with q2 = p.
Support loss is **q1 = 1**, a kink or a boundary, where D1's formula is not wrong
but undefined.

**The observable had to change**, and that is the part I would have missed by
reasoning verbally. D1's R = Var·λ/D needs a curvature λ, and a kink does not have
one. Distribution *shape* works instead: for a single-term Φ = A|y|^q the
standardized moments depend on q alone, so excess kurtosis reads q off directly and
is defined at q = 1 (Laplace, +3.0000) and q = 2 (Gaussian, 0.0000) alike.

## What I found

**All three at-risk legs pass.**

- **P3, L1-penalized logistic regression** (statistics/ML), a genuinely
  all-orders smooth part plus an L1 kink: τ_c ~ D^**0.5000** against 0.5000
  predicted, max residual 1.6e-4.
- **P4, M/M/1** (operations research): the registered prediction was that **no
  crossover exists** — infinite buffer means q1 = 1 with the q2 slot empty. Excess
  kurtosis pinned at the exponential value across four decades of 1 − ρ (mean
  6.0014, spread 0.0111), with no locus to fit.
- **P5, M/M/1/K**: a hard wall is the q2 → ∞ corner, predicted exponent 1.
  Measured **0.9979**, residual 2.9e-3 — so the limit is continuous and boundaries
  are not a separate class either.

**The synthetic grid confirms the functional form** across nine (q1, q2) pairs to
1e-14, including q = 0.5 (excess kurtosis +22.2) and q = 8, which is the range D1's
observable could not cover.

**So the answer is that D6's question presupposed too much, the same way D2's
did.** Support loss is neither a separate class nor p = ∞ — p = ∞ would be a value
in the q2 slot, and support loss is a different value in the *q1* slot. Floor 3's
classifier is a pair, and what classifies is the **ratio** q1/q2.

**That lands exactly where D2 said it had to.** D2 derived that the chart-free
residue on floor 3 must be a ratio rather than a magnitude, because magnitudes are
gauge under G_pow. It reached that conclusion through codimension — a smooth-germ
notion that cannot be defined for a kink. D6 finds the classifier is q1/q2 on
precisely the class D2's argument could not reach, so **D2's "the residue is the
codimension p − 2" is the smooth-case face of a more general ratio.**

**The physics gap is closed.** D1 and D2 each recorded, and neither closed, that
every at-risk leg was physics. D6's three are statistics/ML and operations research.

## Decisions / level changes (with reasons)

- **D1's *p* is reclassified, not retired.** It remains correct and remains the
  generic case — if Φ has a Taylor expansion then q1 = 2 and only q2 varies. It is
  now stated as the q1 = 2 slice rather than as the classifier.
- **The remainder narrows to essential singularities.** If Φ has no leading power
  at all (Φ ~ exp(−1/y)), there is no q1 and nothing here applies. That is
  strictly smaller than the gap D2 left.
- **Third pre-registration slip, and the pattern is now nameable.** P2 was
  registered "AT RISK, structural." It is an identity: once A_c ∝ D^{1−q1/q2} is
  forced, equal ratios giving equal exponents follows immediately. Together with
  [D1's P5 direction](../experiments/D1-chart-invariance/PREREGISTRATION.md) and
  [D2's resampling no-op](../experiments/D2-gauge-group/README.md), the recurring
  failure is **misclassifying a consequence of my own construction as a test of
  it** — which is exactly the anti-pattern
  [`UNKNOWN-LAWS.md`](../questions/UNKNOWN-LAWS.md) §4 was written to catch, and
  it has now caught the same author three times. The register's identity/risk
  rule is doing its job; my first pass at applying it is not reliable, and the
  honest reading is that the rule needs to be applied *after* the code exists, not
  only before.
- **No new [`invariants/`](../invariants/) entry**, same reasoning as D1 and D2:
  this is floor-3 architecture and its home is
  [`FLOORS.md`](../invariants/FLOORS.md).

## Honest limits

- **P1 and P2 are identities.** The evidence is P3–P5, three legs.
- **The ratio claim is not tested on real models.** Establishing it honestly needs
  real systems with *different* (q1, q2) sharing a ratio; the synthetic grid cannot
  do it because the agreement is forced.
- **M/M/1's "no crossover" is a fact about that model**, not a theorem that
  support singularities never acquire a second term. A queue with state-dependent
  service would have one.
- **Prior-art risk unresolved.** Two-term crossover scaling is the Ginzburg
  balancing argument again. If the general form is standard in the multicritical
  crossover literature, the formula is N0–N1 and only the "one classifier across
  all of floor 3" reading is N2.

## Next

1. **The logarithmic corner q1 → 0**, where exp(−Φ/D) becomes a power law. It was
   registered as noted-not-tested precisely so it could not be backdated, and it
   would connect this classifier to the catalog's heavy-tail entry (#1) — the
   floor-3 member neither D1 nor D6 has touched.
2. **A real ratio test** — two genuinely different domains whose singularities
   share q1/q2 but not q1 or q2.
3. **Essential singularities**, the whole remaining gap.
4. **D3** (the ladder as a chart-invariance count), still the cheapest unworked
   stone, and sharper now that D2 and D6 both say the invariant content is a ratio.
5. Still outstanding from D1: **re-register P8's δa³**.
