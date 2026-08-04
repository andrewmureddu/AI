# D8 — the residue of a multi-parameter approach (result)

**Question ([D8](../../questions/UNKNOWN-LAWS.md)):** the question
[D7](../D7-residue-projective/) left live. Every germ D7 measured was
one-dimensional or a direct sum, so **does a genuinely coupled multi-dimensional
singularity still carry n − 1 invariants, or does coupling shrink the quotient?**

**Status: the question's premise was about the wrong space — and the answer
generalizes D7 rather than qualifying it.** State-space coupling changes nothing;
what matters is how many *controls* carry the approach. With m of them the slope
matrix Y transforms as Y ↦ Y·A^{-1}, so the residue is the **column space** of Y —
a point of the Grassmannian Gr(r, n) carrying **r(n − r)** invariants — and D7's
ℝP^{n−1} is the r = 1 slice. **The rank r counts the relevant directions**, and it
does so at a *predicted rate*: the irrelevant column vanishes as t^1.988 against a
registered 2.00. All four at-risk legs pass, including on the support-type class
where there is no fixed point and no scaling field to appeal to.

**This is the third time in this arc that a registered question dissolved instead
of resolving** — after D2's fourth floor and D6's p = ∞. The pattern is now worth
treating as an expectation rather than a surprise; §5.

Run it: `python3 run.py` (numpy only, ~3 min, deterministic — seed 20260728).
Registered first and committed before this file existed:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## The claim

m controls ε₁…ε_m, n observables, slope **matrix** Y_{ij} = ∂ ln O_i/∂ ln ε_j. The
multi-parameter form of G_pow is the monomial group ln ε ↦ A ln ε, A ∈ GL_m:

```
        Y ↦ Y·A^{-1}     ⇒    col(Y) and rank(Y) are the invariants
                         ⇒    residue ∈ Gr(r, n),  count r(n − r)
```

m = 1 gives back D7 exactly: Y is a column, r = 1, Gr(1, n) = ℝP^{n−1}, count
n − 1. **The individual exponents stop being invariants once m > 1** — only the
subspace they span survives — which is the m > 1 form of D2's common-*a* discussion.

## Results

### P2 — the registered question (CONTROL; and the registered form was vacuous)

A coupled 2-D state space (Φ = x⁴/4 + 0.7·x²y²/2 + y⁴/4 − ε(x+y)) with one control:
rank **1**, count n − 1 = **5**. State-space coupling does not shrink the quotient.

> **The registered form of this test is not merely forced, it is vacuous**, and the
> registration should have said so: an n × 1 matrix has rank 1 whatever the model
> does. The question is answered by the *shape* of the object, which is itself the
> finding — D7's lemma never mentioned the state space — but no measurement was
> involved. The non-vacuous version, run post-hoc: coupling could introduce a
> second scale, which would make the column drift with ε. Stacking columns across
> four decades of ε gives rank **1**, σ₂/σ₁ = **3.14e-12**. It does not drift.

### P3 — full rank when every control is relevant (AT RISK — passes)

| model | Φ | m | σ-ratios | rank | count r(n−r) |
|---|---|:--:|---|:--:|:--:|
| M2 (cusp A₃) | x⁴/4 + a·x²/2 + b·x | 2 | 1, **0.171** | **2** | 8 |
| M5 (codim 3) | x⁶/6 + a·x⁴/4 + b·x²/2 + c·x | 3 | 1, 0.175, **0.0823** | **3** | 9 |

Registered σ₂/σ₁ > 0.05 and σ₃/σ₁ > 0.02: met.

### P4 — the irrelevant direction, and its rate (AT RISK — the leg, passes)

M3 is the cusp with a sixth-order coupling added, so m = 3 controls but c has weight
−2 under x ↦ sx, Φ ↦ s⁴Φ. Predicted r = **2**, not 3:

| t | 1e-2 | 3e-3 | 1e-3 | 3e-4 | 1e-4 |
|---|:--:|:--:|:--:|:--:|:--:|
| σ₃/σ₁ | 3.66e-5 | 3.30e-6 | 3.66e-7 | 3.30e-8 | **3.94e-9** |

with σ₂/σ₁ pinned at 0.171 throughout. Registered: σ₃/σ₁ below 1e-3 by t = 1e-4
(met by six orders), σ₂/σ₁ above 0.05 (met), and — the at-risk half — the discarded
singular value carrying the direction's scaling dimension:

```
        sigma_3 / sigma_1  ~  t^1.988          registered  2.00 +- 0.15
```

**"Small" is cheap; the rate is the claim.** The rank does not merely drop, it drops
at the rate the direction's weight predicts, so r is counting relevant directions
rather than counting whatever happens to be numerically negligible.

### P5 — orbit dimension, hence the counts (AT RISK — passes)

Sampling 200 non-negative invertible A and taking the SVD of the vectorized
{Y·A^{-1}}:

| model | m | r | orbit dim | predicted r·m | count r(n−r), n = 6 |
|---|:--:|:--:|:--:|:--:|:--:|
| M2 | 2 | 2 | **4** | 4 | 8 |
| M3 | 3 | 2 | **6** | 6 | 8 |
| M4 | 2 | 1 | **2** | 2 | 5 |
| M5 | 3 | 3 | **9** | 9 | 9 |

Exact in every case. The counts 5 / 8 / 9 are distinct, so the three ranks cannot be
confused by the measurement. The *arithmetic* r(n−r) was declared an identity in
advance; what is at risk and passes is the orbit dimension it is computed from.

### P6 — the exponents move, the subspace does not (AT RISK — passes)

The entry Y₁₁ spans **106.5× / 340.8× / 105.7× / 450.3×** across the sampled group
for M2 / M3 / M4 / M5, against a registered ≥2×, while the column space is fixed to
the precision recorded in P1. **Individual exponents are not invariants of a
multi-parameter approach.** D2 could only say this for m = 1, where it reads "ratios
survive"; at m > 1 even the ratios move, and what survives is a subspace.

### P7 — reduction to D7 (CONSTRUCTION CHECK — passes)

M4 = x⁴/4 − (ε₁ε₂)·x, where two controls enter through one product: rank **1**, and
the normalized column agrees with D7's own `residue` estimator applied to the same
observables to **6.68e-8** (registered 1e-6). Declared in advance as a construction
check — its job is to confirm the estimator can see r = 1 at m = 2 and that the
r = 1 slice really is D7.

### P8 — the support-type class (AT RISK — passes)

Φ = A|y| + B|y|² + C|y|⁴, controls (A, B, C), approached by D → 0 at A ∝ √D. No
fixed point, no flow, no scaling field — the class D6 opened.

| model | m | σ-ratios | rank | count, n = 4 |
|---|:--:|---|:--:|:--:|
| single term (B only) | 1 | 1 | **1** | 3 |
| two terms (A, B) | 2 | 1, **0.0458** | **2** | 4 |
| three terms (A, B, C) | 3 | 1, 0.0458, **~1e-8** | **2** | 4 |

and the discarded singular value again carries a *predicted* rate — the C-term's
relative size at the density's own scale is C·D/B², so

```
        sigma_3 / sigma_1  ~  D^1.000          registered  1.00 +- 0.15
```

Orbit dimension **6** = r·m = 2×3, exact. **This is the leg that separates D8 from
RG bookkeeping**: relevant/irrelevant classification is textbook where there is a
fixed point to linearize about, and here there is none, yet the rank counts the same
thing at the same kind of rate.

### P1 — subspace invariance (IDENTITY — missed as registered, for two reasons)

Registered: largest principal angle below **1e-10** for every model. Measured with
the estimator the registration named, and then with a better-conditioned one:

| model | arccos form | sine form | registered 1e-10 |
|---|:--:|:--:|:--:|
| M2 | 3.33e-8 | **1.22e-13** | met in the sine form |
| M5 | 4.47e-8 | **3.28e-13** | met in the sine form |
| M4 | 2.58e-8 | **5.03e-16** | met in the sine form |
| M3 | 1.34e-7 | 1.39e-7 | **not met, and correctly so** |
| M6, three-term | 7.74e-8 | 7.30e-8 | **not met, and correctly so** |

Two distinct causes, separated by diagnostics rather than assertion:

1. **The estimator's resolution, not the claim.** `arccos` of a principal cosine
   floors at √(machine eps) ≈ 1.5e-8, because cos θ = 1 − θ²/2 loses half the
   digits near θ = 0. Measured: the floor sits at 3.3e-8 *regardless of step size*
   (h = 1e-3…1e-5 all give 0.0 for a fixed A) and *regardless of conditioning*
   (best decile cond 2.1 → 3.0e-8; worst decile cond 64.4 → 3.0e-8). Computing
   ‖(I − Q₁Q₁ᵀ)Q₂‖ instead — the same quantity for small angles, without the
   cancellation — gives 1e-13 to 1e-16. **The registered tolerance was below what
   the registered estimator can represent**, whatever the model does.
2. **The remaining two are the asymptotics, and they are supposed to be there.**
   M3 and M6's three-term case are exactly the models with an irrelevant column.
   With σ_{r+1} ≠ 0 the rank-r subspace is only an *asymptotic* invariant: A^{-1}
   mixes the near-null column back in and tilts it by ~σ_{r+1}/σ_r. If that is the
   cause, the tilt must vanish at the same rate as the discarded singular value —
   and it does, at **t^1.988** against σ₃/σ₁'s own t^1.988:

   | t | 1e-2 | 3e-3 | 1e-3 | 3e-4 | 1e-4 |
   |---|:--:|:--:|:--:|:--:|:--:|
   | subspace sine | 1.5e-4 | 1.3e-5 | 1.5e-6 | 1.3e-7 | **1.6e-8** |

   So the correct statement, which the registration did not make, is: **the
   Grassmannian point is exact when every direction is relevant and asymptotic when
   one is not**, with the error at the irrelevant direction's own rate. That is a
   sharper claim than the one registered, and it is not a repair — it is what P4's
   result implies and P1 should have anticipated.

## 5. What this cost, and what it is worth

> **A fifth registration slip, and the fix I announced did not take.** D7 logged
> setting tolerances from expectation rather than from the error budget, and D8's
> registration says in its commit message that this time they were derived in the
> scope section. Two of them were — P4's and P8's rates, which are the legs that
> matter and which came in at 1.988 and 1.000. **P1's was not**, and it failed in a
> category neither D7 nor the scope section had: not the *modelling* budget
> (finite windows, finite N) but the **estimator's own numerical resolution**. A
> tolerance can be below what double precision can express in the chosen formula
> while the claim is exact to machine precision in another. Added to the list of
> things to check before registering a number.
>
> **And the vacuous control (P2).** Declared as forced, which was right, but it is
> stronger than forced: an n × 1 matrix's rank is fixed by its shape. Declaring a
> test "forced" is not the same as noticing it has no content, and the register's
> §4 rule catches the first but did not catch the second.

**What survives.** The residue of an m-parameter approach is the column space of
the slope matrix, with r(n−r) invariants and D7 as the r = 1 slice; r counts the
relevant directions and does so at the rate their scaling dimension predicts, on
smooth germs and on the support-type class alike; individual exponents are not
invariants once m > 1.

**Honest limits.**

- Every germ is polynomial and 1-D in state space except M0, and M0 is the control.
  **"Coupled" was tested in control space** — P2 is what licenses that reading, and
  P2 is vacuous as registered.
- The prior-art note is deflationary and stands: relevant/irrelevant classification
  is textbook RG, and if the Grassmannian reading is written down anywhere, D8's
  geometry is N0 and only the support-type audit survives.
- **Marginal directions — weight exactly 0 — are untested**, as registered. They
  produce logarithms and the rank statement becomes a statement about a
  slowly-vanishing column.
- The monomial group was restricted to entrywise non-negative A so the approach is
  preserved; whether full GL_m is admissible is untested.
- **Essential singularities remain outside**, unchanged since D6. The remainder does
  not narrow.
