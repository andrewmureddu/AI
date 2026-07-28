# 2026-07-28 — D8: the multi-parameter residue is a Grassmannian point, and its rank counts

**Worked on:** [D8](../questions/UNKNOWN-LAWS.md), opened today as the question
[D7](../experiments/D7-residue-projective/) left live and `SYNTHESIS.md` §7.0
carried as the successor to the successor of the P0.
**Change:** new experiment
[`D8-grassmannian-residue/`](../experiments/D8-grassmannian-residue/); D8 registered
and run. `SYNTHESIS.md` §6 and §7.0 updated. No earlier measurement changed, and
this time no earlier interpretation is corrected either — D8 *contains* D7 rather
than amending it.

## What I did

D7 closed with an admission in its own scope section: every germ it measured was
one-dimensional or a direct sum. So the count n − 1 was established only where the
directions do not talk to each other, and the obvious escalation was a genuinely
coupled multi-dimensional singularity.

Registered it that way, and the registration is where the interesting thing
happened: writing down the claim made it clear the question was pointed at the
wrong space. D7's lemma — every observable's log-slope picks up the same factor
when the control family is relabelled — never mentions the state space at all. A
coupled two-dimensional germ with **one** control must give n − 1 for reasons that
have nothing to do with whether the directions couple. What actually varies is how
many **controls** carry the approach, and a floor-3 singularity of codimension *c*
has *c* of them — so D7's one-parameter case is the exception, not the rule.

## What I found

**With m controls the residue is a point of the Grassmannian.** Write Y for the
n × m matrix of log-slopes, Y_{ij} = ∂ ln O_i/∂ ln ε_j. The multi-parameter form of
G_pow is the monomial group ln ε ↦ A ln ε, under which **Y ↦ Y·A^{-1}**. Right
multiplication by an invertible matrix preserves the column space and the rank and
nothing else, so

```
        residue = col(Y) ∈ Gr(r, n),     count = r(n − r),     r = rank Y
```

and D7 is the r = 1 slice, since Gr(1, n) = ℝP^{n−1} and n − 1 = 1·(n−1).

**The rank counts the relevant directions — at a rate, which is the part that could
have failed.** A cusp with a sixth-order coupling added has m = 3 controls, but the
coupling has weight −2 under the germ's own scaling. Measured rank: **2**. And the
discarded singular value does not merely go small, it goes small at the rate the
weight predicts:

| t | 1e-2 | 3e-3 | 1e-3 | 3e-4 | 1e-4 |
|---|:--:|:--:|:--:|:--:|:--:|
| σ₃/σ₁ | 3.66e-5 | 3.30e-6 | 3.66e-7 | 3.30e-8 | **3.94e-9** |

fitted **t^1.988** against a registered 2.00 ± 0.15, with σ₂/σ₁ pinned at 0.171
throughout. On the support-type class the same test gives **D^1.000** against 1.00.
*"Small" is cheap. The rate is the claim* — it is what separates "r counts relevant
directions" from "r counts whatever happens to be numerically negligible."

**The support-type leg is the one that carries the grade.** Relevant/irrelevant
classification by scaling dimension is textbook renormalization group, and the
prior-art note says so in the bluntest terms I could write. But the textbook
argument needs a fixed point to linearize about, and Φ = A|y| + B|y|² + C|y|⁴ has
none — no flow, no scaling field, no universality class. The rank counts the same
thing there anyway, at the same kind of rate.

**Orbit dimension came in exact.** Sampling 200 group elements and taking the SVD of
the vectorized orbit gives dim = r·m for every model — 4, 6, 2, 9 — so the counts
r(n−r) = 5 / 8 / 9 are measured rather than assumed. The arithmetic was declared an
identity in advance; its input was not.

**And one statement gets sharper than D2 could make it.** Individual entries of Y
span **106× to 450×** across the sampled group while the column space stays fixed.
At m = 1 the honest statement is "magnitudes are gauge, ratios survive"; at m > 1
**even the ratios move**, and what survives is a subspace. D2's common-*a*
discussion was the m = 1 shadow of this.

## Three errors, and one of them is a new category

**A fifth registration slip, and the fix I announced did not take.** D7 logged
setting tolerances from expectation rather than from the error budget, and D8's
registration claims they were derived in the scope section this time. Two of them
were — P4's and P8's rates, the legs that matter, which came in at 1.988 and 1.000.
**P1's was not**, and it failed in a category neither D7 nor the scope section had:
not the modelling budget (finite windows, finite N) but the **estimator's own
numerical resolution**. `arccos` of a principal cosine floors at √(machine eps)
≈ 1.5e-8 because cos θ = 1 − θ²/2 loses half the digits near zero, so a registered
1e-10 was unreachable whatever the model did. Measured the floor two ways to be sure
it was not the models: it is independent of step size (h = 1e-3…1e-5 all give
exactly 0.0 for a fixed group element) and independent of conditioning (best decile
cond 2.1 → 3.0e-8; worst decile cond 64.4 → 3.0e-8). Computing ‖(I − Q₁Q₁ᵀ)Q₂‖
instead — the same quantity, without the cancellation — gives 1e-13 to 1e-16.

**A vacuous control, declared only as forced.** P2 was labelled a control in
advance, which was right, but it is stronger than forced: an n × 1 matrix has rank 1
because of its shape. The register's §4 rule catches "this is a consequence of my
construction"; it did not catch "this has no content at all." The non-vacuous
version is post-hoc — stack the columns across four decades of ε and ask whether
coupling introduces a second scale, giving rank 1 and σ₂/σ₁ = 3.14e-12.

**A claim the registration should have made and didn't.** Two models — the ones with
an irrelevant column — kept a subspace distance of ~1e-7 even in the well-conditioned
estimator. That is not a failure: with σ_{r+1} ≠ 0 the rank-r subspace is only an
*asymptotic* invariant, because A^{-1} mixes the near-null column back in and tilts
it by ~σ_{r+1}/σ_r. If that is the cause, the tilt must vanish at the same rate as
the discarded singular value — and it does, **t^1.988**, matching σ₃/σ₁'s own
exponent. So the correct statement is that **the Grassmannian point is exact when
every direction is relevant and asymptotic when one is not**. P4 implies it; P1
should have anticipated it; neither said so.

## Decisions

- **D8 graded N1–N2, with the most deflationary prior-art note in the register.**
  The smooth half is RG bookkeeping and a specialist would likely call it a
  restatement; what is claimed is the count, the fact that r is measurable from
  observables without knowing the fixed point, and the support-type audit.
- **Nothing earlier is corrected.** D7's ℝP^{n−1} is exactly right at m = 1 and is
  now a named slice rather than the general case. This is the first pass in the arc
  that extends without amending.
- **`SYNTHESIS.md` §7.0's live question marked answered**, and §6's residue line
  carries both forms.

## The pattern this makes

**Three registered questions in a row have dissolved rather than resolved** — D2's
fourth floor ("neither a floor nor floor 1: the gauge group"), D6's p = ∞ ("neither
a separate class nor a point at infinity: a different slot"), and now D8's coupling
("neither yes nor no: the wrong space"). In every case the question presupposed a
distinction the answer removes, and in every case the dissolution was worth more
than either registered horn. That is frequent enough now to be a working
expectation rather than a run of luck, and it suggests a cheap discipline: **when
registering a stone, write down what the question presupposes, not just what it
asks.** Two of the three would have been visible before the run.

## What this opens

- **Marginal directions — weight exactly 0.** Untested and registered as such. They
  produce logarithms, and the rank statement becomes a claim about a column that
  vanishes like 1/ln t rather than a power. This is the natural next escalation and
  it is cheap.
- **Is r the codimension?** For every all-relevant germ here r = m, and m was chosen
  as the codimension. Whether r is *forced* to equal the codimension, or whether a
  singularity can have fewer independent scaling directions than tuned coefficients,
  is untested and is the sharper form of what [D5](../questions/UNKNOWN-LAWS.md)
  asks about arithmetic on *p*.
- **[D3](../questions/UNKNOWN-LAWS.md) is now the cheapest thing in the register**
  and has been for two passes. Its "count of coordinate choices quotiented out" now
  has two definite referents — n − 1, and r(n−r) — and the ladder-vs-transfer
  harness already exists.
- **Essential singularities remain outside**, unchanged since D6.
