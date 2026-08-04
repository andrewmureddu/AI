# D7 — What the invariant residue is

**Tests:** [D7](../questions/UNKNOWN-LAWS.md), the successor to the map's P0. D2,
D6 and P-D each reached "the chart-free residue" by a different route and produced
three objects that cannot state each other — a codimension, a ratio of leading
exponents, and an allometric exponent in a system with no potential at all. Is
there a general statement, or are the scheme layer's invariants heterogeneous?

**Result: one statement, and it is the Π-theorem with the chart as the single
dimension.** The residue is the log-slope vector modulo the diagonal ℝ⁺ — i.e. the
slopes of observables against *other observables*. The count is n − 1. The
discreteness D2 found is inherited from Taylor orders, not from the residue. And
the common-*a* commitment D2 flagged as load-bearing is not a stipulation: it is
the statement that the group is the diagonal, and it is forced as soon as the
singularity is approached along one family.

**Boundary, stated before the numbers:** the theorem is about observables, and a
*derivative with respect to the chart* is not one. Those transform affinely rather
than homogeneously, and including one in the slope vector destroys the ratios. §5.

Numerics: [`experiments/D7-residue-projective/`](../experiments/D7-residue-projective/).

---

## 1. Setup

A floor-3 singularity is approached along a one-parameter family. The domain
supplies a coordinate ε for that family — reduced temperature, mutation rate, load
gap, penalty strength, sample ratio — and [D1](../experiments/D1-chart-invariance/)'s
result is that ε is a *choice*. Write the admissible re-choices as

```
        G_pow :   ε  ↦  ε' = ε^{1/a},     a > 0
```

so that ε = ε'^a. [D2](./D2-gauge-of-the-tower.md) established that this is the
group available for cross-domain comparison, that it strictly contains G_diff, and
that the enlargement lives entirely on floor 3.

Let O₁,…,O_n be **observables**: quantities defined by the system, not by the
chart, each varying along the family. Their log-slopes are

```
        y_i  =  d ln O_i / d ln ε .
```

A *description scheme* — a branching network, a concatenated code, a
coarse-graining — is the same setup with a discrete chart. The level index N plays
the role of ln ε, the re-choice is coarse-graining by *a* levels, and log-slopes
are per-level log-increments. Nothing below distinguishes the two cases, which is
the point.

## 2. The action is by a common scalar

**Lemma.** For every observable, y_i ↦ a·y_i.

*Proof.* O_i is a function on the family; re-charting relabels the family and does
not change the function. So

```
        y_i'  =  d ln O_i / d ln ε'  =  (d ln O_i / d ln ε)·(d ln ε / d ln ε')
              =  y_i · a ,
```

and the factor `d ln ε/d ln ε' = a` carries no index *i*. ∎

The whole content is the last clause. Each observable is free to have any exponent;
what is not free is that they are all read against the same relabelling. **The
group acts on ℝⁿ as the diagonal ℝ⁺, not as (ℝ⁺)ⁿ.**

The lemma survives multiplicative log corrections, which is worth checking because
those are exactly where naive exponent bookkeeping fails. For
O ~ ε^y·(ln 1/ε)^m the slope is y − m/ln(1/ε), and re-charting gives
a·y − m/ln(1/ε'), which equals a·(y − m/ln(1/ε)) identically. Logs shift the slope
but do not spoil the weight.

## 3. The invariants, and the count

The orbits of the diagonal ℝ⁺ acting on ℝⁿ∖{0} are rays. So:

> **The chart-free content of the family is the ray through y — the point
> [y₁ : … : y_n] of ℝP^{n−1} — and nothing else.**

Two ways to say what that is concretely, and the second is the useful one:

- **As ratios.** y_i/y_j for any pair, of which n − 1 are independent.
- **As observable-against-observable slopes.** Because
  ```
        d ln O_i / d ln O_j  =  y_i / y_j ,
  ```
  the ratios are not derived quantities at all: they are the log-slopes one
  measures when no chart is used. *Eliminating the chart* and *taking the
  projective quotient* are the same operation performed in the two directions.

**The count is dimensional analysis.** n quantities, one "dimension" (the chart),
so n − r = n − 1 independent dimensionless combinations. This is the Buckingham Π
theorem transported from magnitudes to exponents, and it is the reason the count is
n − 1 for every n rather than being a fact about any particular singularity. It is
also the first statement in this arc that says anything at n > 2: all three known
members of the residue are n = 2 and therefore carry exactly one invariant, which
is why each of them looked like "the" residue rather than like a coordinate on a
space of them.

## 4. Two consequences that correct the existing statements

### 4.1 The residue is not intrinsically discrete

D2's residue is the integer p − 2 and the natural reading — the one `FLOORS.md`
carries — is that the chart-free content is a *codimension*. §3 says otherwise: the
residue is a point of ℝP^{n−1}, and a projective space has no distinguished
rational points. What produces D2's integer is the smooth case's arithmetic, where
the slopes are Taylor orders and Taylor orders are integers. Change the hypothesis
and the integrality goes:

```
        Phi(y) = |y|^{q1} + |y|^{q2},  q1/q2 irrational   ⇒   residue irrational
```

D6 already had the machinery for this and did not draw the consequence. So
"the residue is the codimension p − 2" is the smooth, integer-slope face of the
general statement, exactly as D6 showed *p* is the q1 = 2 face of the ratio.

### 4.2 Common-*a* is the group, not a caveat

D2 recorded this as its load-bearing stipulation: the ratios require "one
distance-to-threshold per singularity, not one per eigendirection," and under
independent per-direction re-charting only signs and counts survive. That is the
observation. Here is the derivation.

If each direction may be re-charted independently the group is (ℝ⁺)ⁿ acting
componentwise, y_i ↦ a_i·y_i. Its orbits on the open positive orthant are the
orthant itself, so **the only invariants are the signs**: the ratios all move, and
n − 1 collapses to 0. Conversely, the diagonal is forced whenever there is a single
one-parameter family — a single ε whose relabelling every observable is read
against. So:

> The common-*a* commitment is precisely the statement that the singularity is
> approached along one family. It is not an extra assumption bolted on to make the
> ratios work; it is what "one singularity" means, and D2's sign-only fallback is
> the correct answer to a *different* question — several independent approaches,
> hence several charts, hence no shared ray.

This also explains why signs are the survivors in D2's fallback rather than
something richer: sgn(y_i) is invariant under every a_i > 0, and it is the complete
invariant of the componentwise action.

## 5. Where it breaks — the observables hypothesis

§2 assumed O_i is a function *on the family*. A quantity built by differentiating
with respect to the chart is not, and it transforms differently. For
χ = dO/dε — the response, the susceptibility, the shape every domain reaches for
first —

```
        ln χ  =  ln O − ln ε + ln y      ⇒      y_χ  =  y − 1 + o(1),
```

and under re-charting

```
        y_χ(a)  =  a·y_χ(1)  +  (a − 1)         (affine, not homogeneous)
```

because a·(y − 1) ≠ a·y − 1. The inhomogeneous term is the chart's own Jacobian
showing through. Consequences, and they are restrictions on the claim rather than
decorations:

- **A chart-derivative observable has no weight**, so it does not belong in the
  slope vector; including one makes the ratios move under re-charting and would
  read as a falsification of §3 when it is a violation of its hypothesis.
- The affine law is itself exact and predicted, so the two cases are
  distinguishable by measurement rather than by taste: fit y(a) and see whether the
  intercept is 0.
- The repair is standard and is what the field already does without saying why:
  use the dimensionless log-slope d ln O/d ln ε in place of dO/dε. That quantity is
  an observable-vs-observable slope and lands back inside §3.

Three further boundaries, inherited rather than new:

- **Essential singularities** have no leading power, hence no finite log-slope, and
  are outside this as they were outside D6.
- **G_pow is the asymptotic group.** Over a finite window the admissible
  relabellings are only asymptotically ε ↦ ε^a; corrections to scaling contaminate
  measured slopes at the level of the window's distance from the singular point,
  and that error, not the group, is what limits the numbers in the experiment.
- **The count n − 1 is generic.** If the observables are algebraically dependent
  the measured slope vector lies on a subvariety and fewer than n − 1 invariants are
  *independently* measurable — the claim is about the dimension of the quotient, not
  about any particular observable list.

> **⟳ Generalized 2026-07-28 by [D8](../experiments/D8-grassmannian-residue/), which
> contains this rather than amending it.** Everything above is the **m = 1** case —
> one control carrying the approach. A floor-3 singularity of codimension *c* has
> *c* controls, so this is the exception rather than the rule. With m of them the
> log-slope **matrix** transforms as Y ↦ Y·A^{-1} under the monomial group, the
> residue is **col(Y) ∈ Gr(r, n)** with **r(n − r)** invariants, and §3's ℝP^{n−1}
> is the r = 1 slice. Two things that are invisible at m = 1: the rank **counts the
> relevant directions** (measured, at the rate their scaling dimension predicts),
> and **the ratios stop being invariants** — at m > 1 only the subspace survives, so
> §4.2's reading of common-*a* is itself the m = 1 shadow of a larger statement.

## 6. The three members, as instances

| Member | n | slope vector y | residue = [y] | chart eliminated by |
|---|:--:|---|---|---|
| [D2](./D2-gauge-of-the-tower.md), smooth germ | 2 | (β, k) = (1/(p−1), (p−2)/(p−1)) | β/k = 1/(p−2) | d ln y\*/d ln λ |
| [D6](../experiments/D6-support-singularities/), support type | 2 | leading exponents (q1, q2) of Φ | q1/q2 | d ln A_c/d ln D |
| [P-D](../experiments/PD-allometry-reduction/), branching scheme | 2 | (ln n, −ln β²γ) per level | θ = ln n/−ln(β²γ) | d ln B/d ln M |

All three are one observable differentiated against another; each domain's
"exponent" is that ratio read in the chart the domain happened to supply. The third
row is the one that decides whether this is a general statement or a physics
statement wearing one: allometry has no singularity, no Φ, no continuous chart and
no thermodynamic limit, and the construction still applies, because it only ever
used the fact that one relabelling is shared.

**And the kink falls out.** The reconciliation note left open whether P-D's
non-analyticity in θ = min(1, ln n/−ln(β²γ)) at nβ²γ = 1 is a floor-3 degeneracy
read in a scheme variable or something with no floor-3 counterpart. In §3's terms
the locus is where the two log-slopes are *equal* — the point [1 : 1] of ℝP¹ — so
it is a wall in the residue's own space, at a distinguished point of the projective
line, with no Φ anywhere in its statement. It is chart-invariant for the same
reason θ is, and that is a prediction rather than a reading: coarse-graining must
leave the kink's location fixed while the per-level slopes move.

## 7. Verdict

**The residue has a general form, and the three members are one invariant computed
on three slope vectors.** The mathematics is old in every component — projective
quotients, weight vectors defined up to scale, Π-groups — and the register's grade
should say so: N0 for §3's first sentence, N1 for the Π reading, **N2 only for the
cross-domain identification in §6 and for the consequences in §4 and §5**, none of
which the three members individually imply.

What it buys the map, concretely: a **count** (n − 1) that is testable and has never
been measured, since every known member has n = 2; the **removal** of the
integrality that `FLOORS.md` currently reads into the residue; a **derivation** of
D2's common-*a* caveat from the geometry instead of a stipulation; and a **scope
condition** (§5) that predicts exactly which observables will appear to falsify the
claim and by exactly how much.
