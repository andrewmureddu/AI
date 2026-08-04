# The base variable — one tower, seen through observables

*2026-07-28. Pays the debt [M11](../research-log/2026-07-25-M11-stochastic-resetting.md)
opened and [M3](../research-log/2026-07-25-M3-molloy-reed-rewiring.md),
[P-D](../research-log/2026-07-27-PD-allometry.md),
[P-C](../research-log/2026-07-28-PC-variational-kinds.md) and
[P-K](../research-log/2026-07-28-PK-kink-taxonomy.md) kept flagging as the oldest
live item on the board.*

**Result: one tower, not a family. Base variables are pushforwards of a single
master measure, ordered by refinement, and the right one for an invariant is the
coarsest statistic it is measurable with respect to — so "does X reduce to Φ?" is
a sufficiency question with a decidable answer.** Two things fall out that were not
sought. **Floor 3's stratification is forced**, and into exactly three kinds,
because those are the only three ways a family of log-Laplace transforms can fail
to be nice. And **P-D's "no Φ at all" is not a null case** — it is a Φ on a
rank-one base variable, which is what P-D actually measured.

Numerical companion: [`experiments/BV-base-variable/`](../experiments/BV-base-variable/).

---

## 0. Prior-art note

Everything mechanical here is old, and the derivation is a stitching job.
**Sufficiency and the Fisher–Neyman factorization** are 1920s–30s statistics.
**Exponential families**, their log-partition function's convexity, and
∇Φ = mean / ∇²Φ = covariance are textbook. **Analyticity of the moment generating
function in the interior of its domain of finiteness** is standard complex
analysis. **Lee–Yang** is why a non-analyticity needs a limit.
**Caustics of a pushforward** are Thom and Arnold. **Donsker–Varadhan** supplies
the trajectory-level Φ.

What is claimed is the **application**: that the tower's base-variable question is
a sufficiency question, and that floor 3's stratification — which
[`FLOORS.md`](../invariants/FLOORS.md) §2 recorded as an observation and called
open work — is *forced* by the analyticity structure of the log-Laplace transform.
If a reader's reaction is "this is just sufficiency plus the analyticity of the
mgf", that reaction is correct and is the point: the map's open question turns out
to have been answered before it was asked, and the work is the identification.

---

## 1. What has to be decided

[M11](../experiments/M11-stochastic-resetting/) found that first-passage structure
is not a new primitive — it is the hub's own log-partition form on **an exit time
rather than a state** — and drew the conclusion that made it the oldest debt:

> **Φ's form is portable; Φ's variable is not.** "Does X reduce to Φ?" is
> under-specified until one says *Φ of what*.
>
> The tower may be a family of towers indexed by base variable rather than one
> tower.

Five arrivals now, from five directions, none of them looking for this:

| arrival | the base variable it needed | how it showed up |
|---|---|---|
| [M11](../experiments/M11-stochastic-resetting/) | exit time | the exponential is MaxEnt on [0,∞) at fixed mean; CV = 1 is its knife edge |
| [M3](../experiments/M3-molloy-reed-rewiring/) | **edge pairs**, not node degrees | identical degree sequences move p_c by 35–148% |
| [P-A](../experiments/PA-spectral-gap/) | trajectory (the SCGF of a time average) | the potential's Hessian is the wrong chart; the gap is a null direction of the *trajectory* free energy |
| [S5](../experiments/S5-noise-thresholds/) | codebooks | the entry says so outright |
| [P-D](../experiments/PD-allometry-reduction/) | *none?* | ∇²log Z **rank 1 for every λ**, no conjugate pair, exponent terminal |

The question is whether these are five towers or one, and whether anything picks
the variable other than taste.

---

## 2. The construction

Let **P** be a master measure on a space Ω — for a stochastic process, the path
measure; for a random graph, the measure on labelled graphs. A **base variable** is
a measurable map

```
        Y : Omega -> R^d
```

and its prediction field is the log-Laplace transform of the pushforward,

```
        Phi_Y(lambda)  =  log E_P[ exp(lambda . Y) ]  =  log integral e^{lambda.y} d(P o Y^-1)(y).
```

**(F1) The form is portable, and this is two lines.** Φ_Y is convex (Hölder) and
lower semicontinuous for *every* Y. So convexity, Legendre duality, ∇Φ_Y = the
mean of Y, ∇²Φ_Y = the covariance of Y under the tilted law — the entire floor-2
apparatus — holds for every base variable whatsoever. **The form is a property of
the transform, not of the physics.** That is exactly M11's first clause, and it is
why the hub keeps reappearing in unrelated fields: it is not a discovery about the
world, it is a property of taking a log-Laplace transform of anything.

**(F2) The variable is not portable, and this is one line.** ∇²Φ_Y = Cov(Y). The
geometry is the covariance *of the chosen observable*. Two observables of the same
system give two different metrics on it. Hence M11's second clause: the question is
under-specified without Y.

**(F3) Base variables are ordered, so there is one tower.** If Y = f(Z) for
measurable f, then P∘Y^(−1) = (P∘Z^(−1))∘f^(−1): the coarser field is a pushforward
of the finer. Base variables therefore form a lattice under refinement, with the
master measure at the top and every Φ_Y a pushforward of it.

> **So it is one tower, seen through observables — not a family of towers.**
> M11's conjecture is answered in the deflationary direction.

The rest of this derivation is what F3 costs, because a pushforward is not a
harmless change of view.

---

## 3. The base-variable rule

If base variables are ordered, "which one?" has a candidate answer, and it is the
oldest answer in statistics.

> **The rule.** An invariant X is a Φ-fact on base variable Y **iff X is
> measurable with respect to P∘Y^(−1)** — i.e. iff Y is *sufficient* for X. The
> right base variable is the **coarsest sufficient** one.

This makes the map's question decidable rather than a matter of taste: *"does X
reduce to Φ?"* becomes *"what is the coarsest sufficient statistic for X?"*, and
that has a standard machinery behind it.

**It is not vacuous, because sufficiency fails informatively.** M3 is the rule
being measured without knowing it. Percolation threshold p_c, base variable = node
degrees: at **bit-for-bit identical** degree sequences, rewiring moves p_c by
35 / 72 / 148%. Degrees are **not sufficient** for p_c, so p_c is not a Φ-fact on
the node measure — which is precisely why the Molloy–Reed criterion needs more than
the histogram. Refine to edge pairs and the shifts are predicted to **≤ 4.6%**;
refine no further and clustering breaks it (+10.4% at C = 0.030, **+124%** at
C = 0.211), because triangles are not measurable with respect to pairs. **The rule
predicts M3's exact failure ladder**: sufficiency is achieved level by level, and
each unmeasurable feature is a boundary condition.

**And it retro-explains the other arrivals.** M11: mean completion time is not
measurable w.r.t. the state marginal — you cannot read a first-passage time off an
equilibrium histogram — so the base variable must be refined to exit times. P-A:
the relaxation rate is a functional of the *trajectory*, not of the stationary
state, which is why the potential's Hessian was the wrong chart and the SCGF was
the right one. S5: a code's threshold is not measurable w.r.t. the channel's
one-symbol law.

**Honest status:** F1–F3 are proofs, and the rule is a *definition plus a claim
that it is the operative one*. Its evidence is retrodictive — four arrivals it
explains, one it was fitted to — so §6 registers what would break it.

---

## 4. What this forces about floor 3

Here the derivation pays more than it was asked for.

[`FLOORS.md`](../invariants/FLOORS.md) §2 observed that **floor 2 collapses and
floor 3 stratifies**, listed the strata — "non-analyticity, divergent moments, null
Hessian directions, support loss, soft modes" — and called classifying them open
work. Given §2's construction, the stratification is not open and not a taxonomy.
It is forced, and there are exactly three strata, because a family of log-Laplace
transforms has exactly three ways to fail to be nice.

**On a finite system, Φ_Y(λ) is real-analytic on the interior of its domain of
finiteness.** (The mgf of any random variable is analytic there; log of a
non-vanishing analytic function is analytic.) So *every* floor-3 phenomenon must be
one of:

```
   3a  DOMAIN BOUNDARY   Phi_Y = +infinity beyond a boundary in lambda-space.
                         The tail of Y is too heavy for the transform to exist.
                         -> divergent moments, heavy tails, support loss

   3b  LIMIT             Phi_Y is analytic at every finite size; analyticity is
                         not preserved by the limit.
                         -> Lee-Yang, SSB, percolation, P-D's kink

   3c  DEGENERACY        Phi_Y is perfectly analytic; a DERIVATIVE degenerates.
                         -> null Hessian directions, soft modes, D1's p,
                            D6's q1/q2
```

There is no fourth option, because analytic / not-defined / defined-but-degenerate
exhausts the cases.

**This unifies four of the repo's own results as one statement.**
[D1](../experiments/D1-chart-invariance/)'s degeneracy order *p* and
[D6](../experiments/D6-support-singularities/)'s ratio q1/q2 classify **3c** — and
D6's finding that support loss is q1 = 1 rather than p = ∞ is the statement that
support loss is not in 3c at all, it is **3a**, which is why D1's formula was
*undefined* there rather than wrong. [P-K](../experiments/PK-kink-taxonomy/) just
established that P-D's kink is **3b** by measuring exactly the property that
defines 3b: analytic at every finite depth, non-analytic only in the limit, width
∝ N^(−0.973). And [P-K](../experiments/PK-kink-taxonomy/)'s type L / type C
distinction *is* 3b versus a non-Φ object — a selector boundary is not a
non-analyticity of any Φ_Y, which is why it has no rounding.

**A consequence worth stating separately, because it is a common confusion and the
companion experiment tests it:** a singularity of the *density* is not a
singularity of *Φ*. Push a uniform measure through Y = x² and the density diverges
as y^(−1/2) — a caustic, a genuine floor-3-looking object — while Φ_Y(λ) remains
entire. **Caustics are 3a/3c facts about the pushforward's support and derivatives,
never 3b facts about Φ.** Any claim that "the distribution goes singular, therefore
the free energy does" is unlicensed.

---

## 5. P-D's null case, resolved

[P-D](../experiments/PD-allometry-reduction/) asked for the rule's null case: it
found allometry's exponent has **no conjugate variable** and measured ∇²log Z as
**rank 1 for every λ** against a control swinging 151%. The research log recorded
this as "the question was not *Φ of what?* but *is there a Φ at all?*, and the
answer was no."

**Under §2 the answer is sharper and less dramatic: there is a Φ, and its base
variable has rank one.** ∇²Φ_Y = Cov(Y), so rank-1 covariance *everywhere in
parameter space* says exactly that the two components of Y are functionally
dependent — the honest exponential family with statistics (ln M, ln B) is a
one-parameter family wearing two labels. A rank-one base variable has no conjugate
*pair*, so it supports no exchange rate, so nothing on it can be a Legendre
derivative. **That is not the absence of a prediction field; it is a prediction
field with no room in it**, and it is what P-D's own measurement says.

Two things follow that P-D and [D2](./D2-gauge-of-the-tower.md) left as separate
observations.

- P-D's diagnostic — *is ∇²log Z rank-deficient everywhere?* — is exactly a test of
  whether the proposed base variable is degenerate. It generalizes: **rank(∇²Φ_Y)
  is the effective dimension of the base variable**, and `FLOORS.md` §4's
  floor-3/floor-4 boundary ("singular on a set" versus "rank-deficient everywhere")
  is the difference between a degeneracy *of* a base variable and a degeneracy *in*
  one.
- It explains why the log-ratio refusers were terminal. A rank-one Y admits no
  Legendre dual, so the chain stops; D2 reached the same place by calling them
  transformation data, which is the same fact from the group side.

---

## 6. Falsifiers

- **F1–F3 are theorems** and are falsifiable only by arithmetic.
- **The rule (§3) fails** if some invariant is a genuine Φ-fact on a base variable
  it is *not* measurable with respect to — a quantity predicted correctly by a
  statistic that provably does not determine it. That would make sufficiency the
  wrong criterion and leave the choice of variable arbitrary again.
- **The trichotomy (§4) fails** if a floor-3 object is exhibited that is none of
  3a/3b/3c — in particular a Φ_Y non-analytic *in the interior of its domain at
  finite size*, which the analyticity of the mgf forbids. Finding one would break
  §2's construction, not just the classification.
- **The rank reading (§5) fails** if a rank-one base variable is exhibited whose Φ
  nonetheless supports a genuine exchange rate.
- **The whole framing fails** if the master measure is not well-defined for some
  domain in the catalog — i.e. if some invariant's "Φ" cannot be written as a
  log-Laplace transform of any observable of any measure. Economics' utility and
  biology's fitness are the candidates, and both are already L1 in the catalog for
  related reasons.

## 7. Boundaries

- **Finite systems.** §4's trichotomy is a statement about finite systems plus
  limits of them. It says nothing about objects defined only in a continuum.
- **The rule is a definition with retrodictive evidence.** Four arrivals explained,
  one (M3) that it was read off. It has not yet been used to *predict* a base
  variable in advance of a measurement, which is the honest next step and is what
  §6's first falsifier is for.
- **"Coarsest sufficient" need not be unique or attainable** — minimal sufficient
  statistics exist under regularity conditions that a general graph or path measure
  need not satisfy. M3's clustering breakdown is what non-attainment looks like in
  practice.
- **Nothing here touches floor 1.** The base variable question is about Φ; which
  coordinates Φ is written in is the floor-1 question and is untouched.
