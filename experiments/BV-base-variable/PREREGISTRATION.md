# BV pre-registration — written before any measurement

Numerical companion to [`derivations/base-variable.md`](../../derivations/base-variable.md),
which pays the debt [M11](../M11-stochastic-resetting/) opened and four later
passes kept flagging. The derivation's claims, in the order they can fail:

- **F1/F2** — the log-Laplace *form* is portable to every base variable; the
  *geometry* is not, because ∇²Φ_Y = Cov(Y).
- **§3, the rule** — an invariant is a Φ-fact on Y iff Y is **sufficient** for it.
- **§4, the trichotomy** — floor 3 has exactly three strata (domain boundary /
  limit / degeneracy) because those are the only ways a log-Laplace transform
  fails to be nice; in particular **a singular density is not a singular Φ**.
- **§5** — P-D's "no Φ at all" is a Φ on a **rank-one** base variable, and
  rank(∇²Φ_Y) is the effective dimension of Y.

---

## 0. Prior-art note

All of the machinery is old and named in the derivation's §0: sufficiency and
Fisher–Neyman, exponential families, analyticity of the mgf inside its domain,
Lee–Yang, caustics, Donsker–Varadhan. This experiment checks a stitching job, not
a discovery, and the write-up should not claim otherwise. What can genuinely come
out wrong is whether the repo's own objects behave as the stitching says.

---

## 1. The pre-registration audit

First pass to run [`METHODOLOGY.md`](../../METHODOLOGY.md)'s new standing audit,
added after six instances of registering a number without auditing the
construction. Applying it here, in order:

**(i) Rank.** Leg D varies a 2-parameter family whose statistics are functionally
dependent by construction, so its Jacobian *cannot* have rank 2 — that is the
point, and it means **P8 below is an identity, not a test.** The at-risk half is
whether the rank is restored by an independent third statistic, and that is a
different claim about a different family.

**(ii) Identity.** P1 (∇Φ = mean, ∇²Φ = Cov), P3 (the caustic exponent −½ is the
Jacobian of y = x²), P4 (Φ entire for a bounded observable), and P8 (rank 1 by
construction) are all identities. Marked as such below, and they are **not
evidence**.

**(iii) Instrument.** P1 is registered at 1e-8 and measured with a **5-point**
stencil at h = 1e-3, whose truncation is O(h⁴) ≈ 1e-12 — four orders below the
tolerance. This is the check [P-K's P1](../PK-kink-taxonomy/README.md) failed by
using a 2-point stencil against a 1e-7 tolerance.

**(iv) Algebra.** Re-derived rather than recalled: for a doubly stochastic chain
π is uniform (each column sums to 1, so uniform is a left eigenvector); the
uniform-jump chain's mean first-passage time to any state is exactly n; the
cycle's is k(n−k). Three of P-K's failures were arithmetic.

---

## 2. Identity vs. risk

**Identities. Not evidence.** P1, P3, P4, P8.

**Genuinely at risk.**

- **P2** — that three base variables over *one* master measure give
  substantially different geometries. They could come out similar, which would
  make F2 true but empty.
- **P5, P6** — the sufficiency failure. I must construct two chains with
  bit-identical stationary laws whose trajectory-level quantities differ a lot.
  Both the construction and the size of the gap can fail.
- **P7** — that the *state* base variable is blind to the difference while the
  *trajectory* one sees it. This is the rule's content and is the leg most able to
  embarrass it.
- **P9** — rank restored by an independent statistic, on a family not built to be
  degenerate.
- **P10** — the trichotomy guard: 3a, 3b and 3c each exhibited, and **no** interior
  non-analyticity at finite size anywhere in the battery.

---

## 3. Registered predictions

**P1 (identity).** For three base variables over one master measure,
‖∇Φ_Y − E[Y]‖ and ‖∇²Φ_Y − Cov(Y)‖ ≤ **1e-8** (5-point stencil, h = 1e-3).

**P2 (AT RISK).** The three ∇²Φ_Y at matched tilt differ substantially: the
largest pairwise ratio of their spectral norms is **≥ 10**.

**P3 (identity).** Pushing uniform-on-[−1,1] through Y = x² gives a density
diverging as y^α with α = **−0.500 ± 0.01**.

**P4 (identity).** For that same Y, Φ_Y is **entire**: a degree-20 Taylor series
about 0 reproduces Φ_Y to **≤ 1e-8** over |λ| ≤ 3. *The contrast between P3 and P4
is the claim — a singular density is not a singular Φ — and neither half is
evidence on its own.*

**P5 (AT RISK).** Two doubly stochastic chains on n = 20 states — a nearest-
neighbour cycle walk and uniform jumps — have stationary laws agreeing to
**≤ 1e-15** in total variation.

**P6 (AT RISK).** Their mean first-passage times differ by a factor **≥ 2**
(predicted: 100 vs 20 for the antipode, from k(n−k) and n).

**P7 (AT RISK — the rule).** For an observable f with equal stationary mean under
both chains, the **state** base variable's Φ is identical (≤ 1e-14) while the
**trajectory** base variable's curvature Λ''(0) differs by a factor **≥ 2**. So
the state statistic is *not sufficient* and the trajectory statistic is, exactly
as §3 requires.

**P8 (identity).** For the allometry family with statistics (ln M, ln B),
rank(∇²Φ) = **1** at every λ on a 5-decade grid, with the smaller eigenvalue below
**1e-12** of the larger — reproducing [P-D](../PD-allometry-reduction/)'s result
from the definition rather than from its code.

**P9 (AT RISK).** Adding a genuinely independent third statistic restores rank
**2** (and 3 where the family supports it) with the smallest eigenvalue above
**1e-6** of the largest — so rank tracks the effective dimension of the base
variable and is not an artifact of the estimator.

**P10 (AT RISK — the trichotomy guard).** Across a battery of six base variables:
**3a** exhibited (a heavy-tailed Y with Φ finite for λ < 0 and infinite for
λ > 0 — a domain boundary); **3b** exhibited (analytic at every finite N,
non-analytic in the limit); **3c** exhibited (Φ analytic, ∇²Φ degenerate); and
**zero** cases of a non-analyticity in the *interior* at finite size, which §4
forbids.

---

## 4. What would kill this

- **P7 fails** — sufficiency is not what picks the base variable, and §3's rule is
  decoration.
- **P2 fails** — the geometry is portable too, and F2 has no content.
- **P10 finds an interior non-analyticity at finite size** — §2's construction is
  wrong, not just the classification.
- **P9 fails** — rank does not track base-variable dimension, so §5's reading of
  P-D is unearned and P-D's "no Φ at all" stands as written.

## 5. Scope

- **Finite discrete state spaces throughout**, so every Φ here is entire by
  construction and P10's guard is a check on the *battery*, not a general proof.
- **The chains are synthetic and chosen** to have identical stationary laws; this
  demonstrates the sufficiency failure, it does not measure how common it is.
- **Leg D reproduces P-D's rank-1 result but not its physics** — the family is the
  honest exponential family in (ln M, ln B), as P-D built it.
- **Nothing here tests the rule prospectively.** Every arrival it explains was
  measured first. The derivation's §7 says so and this does not change it.
