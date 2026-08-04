# D8 pre-registration — written before any measurement

Works [D8](../../questions/UNKNOWN-LAWS.md), the question
[D7](../D7-residue-projective/) left live: every germ D7 measured was
one-dimensional or a direct sum, so **does a genuinely coupled multi-dimensional
singularity still carry n − 1 invariants, or does coupling shrink the quotient?**

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers.

---

## 0. Prior-art note (written first)

**Old, and more of it than in D7.** Multi-parameter scaling near a critical point,
crossover exponents, and the classification of perturbations into **relevant,
marginal and irrelevant** by their scaling dimension are textbook renormalization
group — Wegner, Fisher, and every book on critical phenomena. Quasi-homogeneous
germs carry weight vectors defined up to overall scale (Arnold); the multi-variable
generalization of the Newton polygon is the Newton polyhedron; catastrophe theory
supplies the A_k unfoldings used below and their codimensions. That an irrelevant
coupling drops out of the leading asymptotics is the *content* of the word
"irrelevant" and is not a discovery in any form.

**The nearest miss, recorded so it cannot be relabelled.** If anyone has written
"the exponent data of an m-parameter approach is a point of the Grassmannian, and
its rank counts the relevant directions," then D8's geometry is **N0** and only the
cross-class audit survives. The construction is a short step from RG scaling
fields, and the honest prior expectation is that a specialist would call it a
restatement.

**What is claimed, and it is narrow.** (i) That the residue of an m-parameter
approach is the **column space** of the slope matrix — a point of Gr(r, n) — and
therefore carries **r(n − r)** invariants, with D7's ℝP^{n−1} the r = 1 slice. This
is a *count*, and counts are what this arc has been able to test. (ii) That r is
measurable from observables alone, without knowing the fixed point or the weights.
(iii) That both hold on the support-type class, where there is no RG, no fixed
point and no scaling field to appeal to — which is where a restatement of RG
bookkeeping would have nothing to say.

---

## 1. The claim

Let m controls ε₁,…,ε_m carry the approach and let O₁,…,O_n be observables. The
slope **matrix** is Y_{ij} = ∂ ln O_i/∂ ln ε_j. The multi-parameter form of G_pow
is the monomial group: ln ε ↦ A ln ε with A ∈ GL_m (entrywise non-negative, so the
approach is preserved). Then

```
        Y  ↦  Y·A^{-1}        ⇒   col(Y) is invariant,  rank r is invariant
                              ⇒   residue = col(Y) in Gr(r, n),  count r(n−r)
```

D7 is m = 1: Y is a column, r = 1, Gr(1, n) = ℝP^{n−1}, count n − 1. **The
individual exponents are not invariants once m > 1** — only the subspace they span
is — which is the m > 1 form of D2's common-*a* discussion.

**And r counts the relevant directions.** An irrelevant control's column vanishes
as the singularity is approached, at a rate set by its scaling dimension, so it does
not contribute to the rank. This is the part that is textbook RG in the smooth case
and is being tested outside it.

## 2. Identity vs. risk — the required disclosure

**Analytic identities. Not evidence:**

- **P1 — col(Y) invariant under Y ↦ YA^{-1}.** Linear algebra.
- **The arithmetic r(n−r).** Once the orbit dimension is r·m and the rank-r variety
  has dimension r(n+m−r), the count is subtraction. Only the *measured inputs*
  (r and the orbit dimension) are at risk, never the count derived from them.

**Controls, declared as such:**

- **P2 — the registered question itself.** A coupled 2-D state space with **one**
  control must give r = 1 and count n − 1, because D7's lemma never mentioned the
  state space. Its role is to answer the live question and to show the premise was
  wrong: what matters is control-space dimension, not state-space coupling. It is
  *forced*, and is reported as an answer rather than as evidence.
- **P7 — a rank-1-by-construction model.** Φ = x⁴/4 − (ε₁ε₂)x, where the controls
  enter through one product. Checks that the estimator can *see* r = 1 with m = 2,
  and that D7's estimator reproduces the projective class.

**Genuinely at risk:**

- **P3 — r = m for all-relevant germs.** The cusp (m = 2) and a codimension-3 germ
  (m = 3). Nothing guarantees the measured slope matrix attains full rank rather
  than degenerating.
- **P4 — the irrelevant direction, and its rate.** The leg. A cusp with a sixth-order
  coupling added: m = 3 controls, predicted r = **2**, with the discarded singular
  value vanishing at a *predicted exponent* rather than merely being small.
- **P5 — orbit dimension = r·m**, hence the counts, measured by sampling the group.
- **P6 — the individual exponents move while the subspace does not.**
- **P8 — the same on the support-type class**, where there is no RG to appeal to.

## 3. Models

| tag | Φ | controls | m | predicted r |
|---|---|---|:--:|:--:|
| M0 | x⁴/4 + 0.7·x²y²/2 + y⁴/4 − ε(x+y), **2-D state** | ε | 1 | 1 |
| M2 | x⁴/4 + a·x²/2 + b·x (the cusp, A₃) | a, b | 2 | 2 |
| M3 | M2 + c·x⁶/6 | a, b, c | 3 | **2** |
| M4 | x⁴/4 − (ε₁ε₂)·x | ε₁, ε₂ | 2 | 1 |
| M5 | x⁶/6 + a·x⁴/4 + b·x²/2 + c·x | a, b, c | 3 | 3 |
| M6 | A\|y\| + B\|y\|² + C\|y\|⁴ (support type) | A, B, C | 3 | **2** |

Each germ is approached along its own quasi-homogeneous ray in *t* — a = t², b = t³
for the cusp; a = t², b = t⁴, c = t⁵ for M5 — so that the approach respects the
germ's weights. Y is measured by central differences in ln ε_j at that base point,
with the whole matrix recomputed at several *t* to check it converges rather than
drifting. Observables (n = 6 for the germs): x\*, λ = Φ″(x\*), Var of the exact
stationary density by quadrature, ΔΦ, \|Φ‴\|, \|m₃\|. For M6, n = 4: the even
moments m₂, m₄, m₆, m₈ of the exact density.

## 4. Registered predictions

**P1 — subspace invariance (IDENTITY).** Over 200 random non-negative invertible A,
the largest principal angle between col(Y) and col(YA^{-1}) below **1e-10** for
every model.

**P2 — the registered question (CONTROL, forced).** M0: σ₂/σ₁ of Y below **1e-6**,
r = 1, count n − 1 = **5**. State-space coupling does not shrink the quotient.

**P3 — full rank when every control is relevant (AT RISK).** M2: σ₂/σ₁ > **0.05**
and σ₃ absent (m = 2), r = **2**. M5: σ₃/σ₁ > **0.02**, r = **3**. Failure is
either singular value collapsing below those thresholds.

**P4 — the irrelevant direction (AT RISK, the leg).** M3, with c₀ = 1 and the
approach a = t², b = t³:

- r = **2**, not 3: σ₃/σ₁ falls below **1e-3** by t = 1e-4 while σ₂/σ₁ stays above
  **0.05**;
- the discarded singular value carries the direction's scaling dimension:
  σ₃/σ₁ ∝ t^**2.00 ± 0.15**, since c has weight −2 under x ↦ sx, Φ ↦ s⁴Φ.

The exponent is the at-risk half. "Small" is cheap; a *predicted number* is not.

**P5 — orbit dimension and the counts (AT RISK).** Sampling A ∈ GL_m and taking the
SVD of the vectorized {YA^{-1}}, the number of singular values above 1e-8 of the
largest equals **r·m**. With n = 6 the resulting counts r(n−r) are **5 / 8 / 9** for
r = 1 / 2 / 3 — distinct, so the three models cannot be confused.

**P6 — exponents move, the subspace does not (AT RISK).** Over the same samples,
the entry Y₁₁ spans at least a factor of **2**, while P1's principal angle stays at
1e-10. Registered because it is the m > 1 statement of what D2 could only say for
m = 1.

**P7 — reduction to D7 (CONSTRUCTION CHECK).** M4: r = 1, and the projective class
of the single column agrees with D7's `residue` estimator applied to the same
observables to **1e-6**.

**P8 — the support-type class (AT RISK).** M6 with (q₁,q₂,q₃) = (1, 2, 4),
controls (A, B, C), approached by D → 0 at A ∝ √D:

- two-term (C = 0): r = **2**;
- single-term (A = C = 0, m = 1): r = **1**;
- three-term: r = **2**, with σ₃/σ₁ ∝ D^**1.00 ± 0.15**, since the C-term's
  relative size at the density's own scale is C·D/B².

This is the leg that separates D8 from RG bookkeeping: there is no fixed point, no
flow and no scaling field here, and the rank must still count relevant directions.

## 5. What would kill D8

- **P3 fails** — the slope matrix does not attain full rank when every control is
  relevant, so rank is not counting what the claim says it counts.
- **P4's exponent misses** — then the irrelevant column is merely small, the rate is
  not the scaling dimension, and "r counts the relevant directions" is a slogan
  rather than a measurement.
- **P5 fails** — the orbit dimension is not r·m, so the quotient is not Gr(r, n) and
  the count r(n−r) is wrong even if the rank statement survives.
- **P8 fails** — the geometry is RG bookkeeping in other notation and does not reach
  the class D6 opened, which is the only place D8 claims to add anything.
- **P6 fails in the direction of invariant exponents** — then the group is smaller
  than GL_m, the singularity supplies a canonical basis of control directions, and
  the residue is richer than a subspace. This would *not* kill the count so much as
  replace it, and it is the way of being wrong that would teach the most.

## 6. Scope, registered

- All germs are polynomial and 1-D in state space except M0. **"Coupled" is being
  tested in control space, not state space** — P2 is what establishes that this is
  the right reading, and if P2 came out otherwise the whole framing would be wrong.
- **Essential singularities remain outside**, unchanged since D6 and D7.
- The monomial group is restricted to entrywise non-negative invertible A so that
  ε_j → 0 is preserved. Whether the full GL_m is admissible is **not** tested.
- **Marginal directions are not tested.** Weight exactly 0 gives logarithms, the
  rank statement becomes a statement about a slowly-vanishing column, and nothing
  here addresses it. Recorded so a later claim cannot be backdated.
- P2 and P7 are forced; P1 is an identity; P5's *count* is arithmetic once its
  measured inputs are in. The at-risk content is P3, P4, P6, P8 and P5's inputs.
