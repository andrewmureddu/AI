# F3 pre-registration — written before any measurement

Tests the sharpest prediction of [`invariants/FLOOR3-STRATA.md`](../../invariants/FLOOR3-STRATA.md),
the sort of floor 3 against the trichotomy
[`derivations/base-variable.md`](../../derivations/base-variable.md) §4 forced:

```
   3a  DOMAIN BOUNDARY   Phi = +inf beyond a boundary in lambda-space
   3b  LIMIT             Phi analytic at finite size, non-analytic in the limit
   3c  DEGENERACY        Phi analytic and finite; a DERIVATIVE degenerates
```

A sort is only a test if it predicts something about entries it had no hand in
shaping. This is the prediction: **the three strata have three different
finite-size signatures, and one instrument separates them.**

---

## 0. Prior-art note

Finite-size rounding of a first-order transition (Imry–Wortis; Fisher–Berker),
the analyticity of the mgf inside its domain, and the fact that a matrix rank is
an integer are all old and were named in the derivation's §0. What is claimed here
is that these three known behaviours are **the** three, and that they sort the
repo's own floor-3 entries. If the answer is "this is just the difference between
a divergence, a limit and a degeneracy", that is correct and is the point — the
claim is the exhaustiveness and the sorting, not the phenomena.

---

## 1. The claim

| stratum | Φ at the locus | finite-size behaviour | signature |
|---|---|---|---|
| **3a** | **divergent** | λ_c is **stable** in system size; Φ beyond it grows without bound | a *boundary*, not a kink |
| **3b** | finite | **rounds**; width → 0 | the only stratum that rounds |
| **3c** | finite and smooth | **does not round**; the degeneracy is exact at every size | an integer, not a limit |

> **Only 3b rounds.** That is the whole prediction, and it is what makes the
> trichotomy a classification rather than three words.

It also supplies a prediction about an existing repo result that was never
classified: [S25](../S25-rlct-singularity/)'s λ(P) = min(P,D)/2 with its kink at
P = D. **Predicted 3c, not 3b** — sharp at every finite D, with the finite-sample
blurring S25 reported being a property of the *estimator* rather than of the
object.

---

## 2. Instrument noise floors

First pass under [`METHODOLOGY.md`](../../METHODOLOGY.md)'s **rewritten audit item
(iii)**: *state the instrument's noise floor next to every registered tolerance.*
[BV](../BV-base-variable/) violated the checklist version three times in one run.

| instrument | noise floor | tolerance registered against it |
|---|---|---|
| kink-width (FWHM of \|f″\| on a grid of m points over 2·half_span) | **2·half_span/m**, reported explicitly per call | widths are compared *to this floor*, never to 0 |
| second difference of Φ at step h = 1e-3 | ε/h² ≈ **1e-10** | curvatures registered ≥ 1.0, eight orders above |
| eigenvalues of an **exactly computed** Gram/covariance matrix | **≈1e-16 relative** | rank thresholds at 1e-14, two orders above |
| bisection for λ_c | **1e-12** absolute | λ_c stability registered at 1e-6, six orders above |

No finite-difference stencil is used where an exact expression exists — the BV
lesson.

---

## 3. Identity vs. risk

**Identities. Not evidence.**

- **P1** — 3b rounds as N^(−1). Already measured by [P-K](../PK-kink-taxonomy/) and
  derivable; included as a *calibration* of the instrument, so the other two
  strata are measured against a known scale.
- **P4** — the rank of a Gram matrix is an integer, so S25's kink is sharp *by
  construction*. The at-risk half is the numerical one (P5).

**Genuinely at risk.**

- **P2** — that 3a's λ_c is **stable** in system size. Nothing forces it; the
  boundary could drift as the support grows, which would make 3a a limit
  phenomenon and collapse it into 3b.
- **P3** — that 3c does **not** round under the same instrument that measures a
  1/N width for 3b.
- **P5** — that the eigenvalue gap at S25's kink is at machine zero rather than
  merely small, at every D. Numerical rank deficiency is often approximate.
- **P6** — the cross-cutting claim: **one instrument, three behaviours**, with no
  per-stratum tuning.

---

## 4. Registered predictions

**P1 (identity; calibration).** 3b exemplar (two-state free energy,
−N^(−1)·log(e^(−N f₁) + e^(−N f₂))): kink width ∝ N^**−1.00 ± 0.03** over
N = 20…5120, and every width at least **20×** the instrument's resolution floor.

**P2 (AT RISK).** 3a exemplar (exponential tail truncated at M, so
Φ_M(λ) → −log(1−λ)): the domain boundary λ_c sits at **1.000000** and moves by
**≤ 1e-6** across M = 10 … 10⁴ (four decades), while Φ_M(λ_c + 0.1) grows by
**≥ 10× per decade of M**. Divergence, not rounding.

**P3 (AT RISK).** 3c exemplar (a base variable with two functionally dependent
statistics): the smallest eigenvalue of the *exact* ∇²Φ is **≤ 1e-14** relative at
every system size 10 … 10⁴, with **no** trend in system size (fitted exponent
|α| ≤ 0.05), and the kink instrument applied to the same object returns **no
locus** or a width at its resolution floor.

**P4 (identity).** S25's random-feature Fisher matrix A^TΣA with A ∈ R^(D×P) has
rank exactly min(P, D), so λ = min(P,D)/2 with a sharp kink. By construction.

**P5 (AT RISK).** That sharpness is *numerical*, not just formal: at P = D + 1 the
(D+1)-th eigenvalue is **≤ 1e-14** of the first, for D = 4, 8, 16, 32 — so the kink
does not round at any D and S25's blurring is the estimator, not the object.

**P6 (AT RISK — the classification).** One instrument, one set of tolerances,
applied to all three exemplars: rounding observed for **3b only**. Specifically,
width/floor ratio ≥ 20 for 3b and ≤ 1.01 for 3c, with 3a producing a stable
boundary rather than a width at all.

---

## 5. What would kill this

- **P2 fails** (λ_c drifts) — 3a is a limit phenomenon and the trichotomy has two
  strata, not three.
- **P3 fails** (3c rounds) — the degeneracy is not exact at finite size and the
  3b/3c distinction is a matter of degree.
- **P5 fails** — S25's kink does round, so the sort's one prediction about an
  unexamined repo result is wrong, and the sort's generative claim is unearned.
- **P6 fails** — the strata are not separable by one instrument, which is what a
  classification has to mean here.

## 6. Scope

- **Exemplars, not the catalog.** This tests that the three signatures are
  distinguishable, not that every catalog entry sits where the sort puts it. Those
  assignments are predictions and are labelled as such in `FLOOR3-STRATA.md`.
- **3a is exhibited by truncation**, which is a limit over *support*, not over
  degrees of freedom. That the two limits behave differently is the claim; a reader
  who thinks all limits are one thing should read P2 as the test of that.
- **S25's leg uses the population Fisher matrix**, so it says nothing about the
  finite-sample estimator S25 actually ran — which is the point being made, but it
  means the two are not compared head to head here.
