# D10 — the lens under floor 1: composition, and what maintains it

*2026-07-29. Works [D10](../questions/UNKNOWN-LAWS.md#d10--is-there-a-floor-0-and-is-it-a-composition-law).
Experiment: [`experiments/D10-composition-lens/`](../experiments/D10-composition-lens/).
Prior-art note in the register, written first; the honest level is **N1**.*

**Result: floor 1 is not the bottom. It takes an input, and the input is a
composition law — a rule for putting two instances of a system side by side. That
law forces Φ's form, supplies the selection rule floor 1 was stated without,
decides which charts are pinned (and therefore what the tower's invariant residue
*is*, in general), and — because Φ is a cumulant generating function — must be
maintained order by order. The orders at which maintenance fails are the tower's
floors. So the layer under the tower and the layer on top of it are one condition
read at different orders.**

---

## 0. Verdict up front

```
  FLOOR 0  composition        ->  fixes what counts as two systems, hence Phi's form,
           (the lens)             the charge list, and which charts are pinned
  FLOOR 1  symmetry           ->  chooses Phi's coordinates from among the ADDITIVE
                                  conserved quantities
  FLOOR 2  Phi regular        ->  prediction        (fails at order 0: Phi* != s)
  FLOOR 3  Phi singular       ->  boundaries        (fails at order 2: criticality, SSB;
                                                     no order at all: heavy tails)
```

Four claims, in the order they are argued: **C1** the hub's form is forced by
composition (§2); **C2** floor 1's rule is conservation **and additivity**, which
corrects [`symmetry-sector.md`](./symmetry-sector.md) §2 (§3); **C3** the
composition law pins charts, which answers
[`FLOORS.md`](../invariants/FLOORS.md) §4's open question about the general
residue (§4); **C4** the tower's floors are the orders at which composition fails
(§5). C1 and C2 are textbook and are argued for placement, not for novelty. C4 is
the only part that could come out wrong, and §5 is where the measurements are.

---

## 1. The gap this fills

[`symmetry-sector.md`](./symmetry-sector.md) derived floor 1: conserved charges
are the natural parameters of long-time ensembles, so symmetry fixes *which
quantities exist* before Φ predicts with them. The derivation takes the group as
given.

That is fine for a physicist with a Hamiltonian in hand and fatal for this map,
because **there is no outside**. A cross-domain map has no privileged observer to
hand a group to a system, and neither does any of the systems it maps. If floor 1
is the base, then the base is a brute input and the tower is a description of
systems that have already been coordinatized by somebody.

Three of the repo's own results already reach past floor 1 for the missing thing,
and none of them names it:

- [P-D leg F](../experiments/PD-allometry-reduction/) killed `G_pow` for allometry
  because **mass is extensive** — under M → M^a masses stop adding.
- [D2 §7](./D2-gauge-of-the-tower.md) reconciled universality with chart-gauge
  because reduced temperature "enters the Hamiltonian linearly" — i.e. because
  **energy is additive**.
- `symmetry-sector.md` §2's charges — energy, particle number, momentum — are,
  without comment, **exactly the additive ones**. It says *conserved*, and every
  example it gives is additive too.

Three arrivals at one unnamed object. That is the shape the repo has learned to
take seriously: it is how the singular set of ∇²Φ announced itself five times
before anyone called it the top floor.

## 2. The composition law, and why Φ is a logarithm (C1)

**The object.** A composition law is a partial binary operation ⊎ on systems —
"A and B, side by side, are one system" — together with the decomposition of a
system into the parts ⊎ recombines. It requires no observer, no group, and no
dynamics. It requires only that the system can be next to a copy of itself.

**What it forces.** If the parts are independent, their states multiply and so do
their partition functions:

```
        Z(A + B)  =  Z(A) * Z(B)
```

Ask for a continuous real-valued summary F of a system that is **additive** under
⊎ — one number per system, and the number for the pair is the sum. Then F must
satisfy F = f(Z) with f(xy) = f(x) + f(y), which is Cauchy's exponential
functional equation; with continuity the solution is unique up to scale:

```
        F  =  c * ln Z
```

**So Φ = ln Z is not a convenient choice of scalar. It is the only additive
coordinate on a multiplicative composition.** Every place the repo has been
surprised to arrive at a logarithm — free energy, log-evidence, log-loss,
log-growth, all identified in [S1](./S1-universal-update.md) — is arriving at the
unique function that turns ⊎ into +.

This is Shannon–Khinchin–Rényi axiomatics and it is N0. It is recorded here
because it fixes the *direction of explanation*: the hub's form is downstream of
composition, not the other way round.

## 3. Additivity, not conservation (C2)

`symmetry-sector.md` §2 states floor 1's rule as: *a quantity Q can parameterize
an equilibrium ensemble iff it is conserved.* Conservation is necessary. It is not
sufficient, and the missing half is a composition fact.

**The argument.** For the family {p(x) ∝ e^{−μT(x)}} to be closed under ⊎ — for
two systems in the family to compose into a system in the family — the exponent
must split:

```
        e^{-mu T(A + B)}  =  e^{-mu T(A)} * e^{-mu T(B)}
        <=>   T(A + B) = T(A) + T(B)   (up to a constant)
```

A conserved quantity that is not additive cannot occupy the slot. Casimirs are the
standard witnesses: L² is exactly as conserved as L_z, and rotating equilibria are
written e^{−β(H−ω·L)} with the additive **L**, never with L². In statistics the
same fact is a theorem with a name — **Koopman–Pitman–Darmois**: a family whose
sufficient statistic has fixed dimension for all sample sizes is an exponential
family, and its statistic is a *sum* over the sample. Additivity is not a side
condition on exponential families; it is their defining property, read through
composition.

**Measured, and the discrimination is the point.**
[Leg C](../experiments/D10-composition-lens/) tilts six statistics of the same
underlying charge to the same informativeness and asks how far the product of two
tilted systems is from the composite's own family:

| T(Q) | additive | linear | monotone | convex | min KL from the family |
|---|:--:|:--:|:--:|:--:|---|
| Q | ✓ | ✓ | ✓ | ✓ | **≤ 3.2e-14** |
| 3Q − 7 | ✓ | ✗ | ✓ | ✓ | **≤ 2.6e-14** |
| Q² | ✗ | ✗ | ✓ | ✓ | 2.2e-2 → 2.4e-3 |
| √Q | ✗ | ✗ | ✓ | ✗ | 1.4e-1 → 8.8e-4 |
| ln(1+Q) | ✗ | ✗ | ✓ | ✗ | 2.3e-1 → 1.9e-3 |
| Q mod 2 | ✗ | ✗ | ✗ | ✗ | 6.44e-1 at every n |

Only the additive column matches the closure column. Linearity is refuted by
`3Q − 7`, which closes anyway because a constant offset is absorbed by
normalization — so the precise rule is **affine in an additive charge**.
Monotonicity is refuted by three rows that have it and fail. Convexity is refuted
by Q² and √Q, opposite curvature, identical failure.

**Why this establishes priority rather than restating floor 1.** The leg contains
no dynamics, no Hamiltonian and no group. Nothing in it can *be* a conservation
fact, because there is nothing for anything to be conserved under. The rule that
decides which statistics may sit in a natural-parameter slot is therefore not a
consequence of floor 1; floor 1 consumes it. That is the argument for a layer
underneath, and it is the one place where the priority claim is more than
suggestive.

## 4. What the composition law pins — and what the residue is (C3)

[`FLOORS.md`](../invariants/FLOORS.md) §4 closes on an explicitly open question:
the tower's chart-free residue has two known members reached by different routes —
the codimension p − 2 from a floor-3 germ ([D2](./D2-gauge-of-the-tower.md)) and
allometry's θ from a branching scheme ([P-D](../experiments/PD-allometry-reduction/))
— *"and no statement of what the general one is."*

Composition supplies the statement, because it is what decides which group is
available.

> **A chart is pinned to `G_diff` when its variable is additive under ⊎, or dual
> to a variable that is. It keeps the larger group `G_pow` when neither holds.**

The first clause is P-D leg F, measured: under M → M^a with a ≠ 1 two organisms
side by side stop having the mass of the pair (defect 0 at a = 1; 29% / 50% / 41%
at a = 1.5 / 2 / 0.5). The second clause is forced by
[the audit](../experiments/D10-composition-lens/#6-leg-e2--the-audit), which is
where this derivation nearly broke: reduced temperature is *intensive*, so by the
first clause alone its exponents should be gauge — and inside physics they are
facts. The resolution is D2 §7's own reason said in composition language. An
additive sufficient statistic induces an affine structure on the natural-parameter
space it is dual to; energy is additive, β is its conjugate, and that is what makes
the coupling's chart canonical. Cross-domain comparison loses the pinning because
an epidemic's R₀ and a decoder's recursion depth are dual to no additive charge —
which is exactly D1's measurement that a fold and an SIS epidemic, the *same*
degeneracy, differ 2× in the bare chart and agree to 0.33333 in the λ-chart.

**Hence the general residue:**

> **The tower's invariant residue is the invariant content of the largest group
> the system's composition law fails to pin.** Where composition pins the chart,
> that content includes the exponents themselves. Where it does not, it is ratios,
> signs and counts.

p − 2 and θ stop being two unrelated members of a list. They are the two branches
of one rule, and which branch a quantity is on is decided by a fact about ⊎ — not
by a fact about Φ, which is why no amount of staring at Φ produced the general
statement.

The audit that forced the correction also produced a confirmation it was not
designed for: the RLCT is read off the coefficient of ln n, **samples are
additive**, so the rule predicts λ is a fact rather than a chart artifact — which
is independently and famously true (it is a birational invariant). A row that
could have failed and did not.

## 5. Maintenance, and the failure orders (C4)

Here is the part that can be wrong, so here is where the numbers are.

Φ is the cumulant generating function. So **"Φ is additive under ⊎" is not one
condition but one per order**: every cumulant must be extensive. Write

```
        delta_k(N)  =  1  -  2 * kappa_k(N) / kappa_k(2N)
```

δ_k → 0 is "extensivity holds at order k." Maintenance is not free, and it fails
in distinguishable ways.

**Order 0 fails ⇒ floor 2 breaks.** When the parts interact strongly enough that
the extensive potential is not additive, the microcanonical entropy can be
non-concave — an additive system cannot manage this, because it can always realize
the two-copy mixture internally. Measured on the mean-field 3-state Potts: the
concavity defect is extensive, N^**1.0252** against a registered 1.00 ± 0.10, and
the microcanonical specific heat is **negative over 68.6%** of the accessible
energy range. The canonical ensemble sees only the concave hull, so **Φ\* is not
the entropy but its envelope** — floor 2's Legendre face, the identity that makes
free energy and entropy one object seen twice, fails precisely on the interval
where composition fails.

*A pre-registered hypothesis died here and the weaker one survived.* "Long-range ⇒
non-additive" is **false**: the mean-field q=2 model is exactly as long-range and
its defect is *exactly zero*, because its transition is continuous. Long range
opens the possibility; a first-order transition realizes it. The control was
added, before the run, specifically because q=3 confounds the two — and the
confound was real.

**Order 2 fails ⇒ floor 3, and by two mechanisms.** Var(M)/N is the
susceptibility. Its divergence, which is [S3](../experiments/S3-fisher-geometry/)'s
arrival and the most-arrived-at object in the repo, *is* the statement that the
second cumulant has stopped being extensive. Curie–Weiss, exact enumeration:

| | Var(M) | δ₂ measured | δ₂ predicted |
|---|---|--:|--:|
| above T_c | N^1.022 | 0.00240 | 0 |
| **at T_c** | N^**1.504** | **0.29364** | 1 − 2^{−1/2} = **0.29289** |
| below T_c | N^2.002 | 0.50010 | 0.5 |

The middle number is the load-bearing one. It is neither 0 nor ½; it is an
anomalous value inherited from a critical exponent, and nothing forces it if
criticality is not an order-2 extensivity failure. The bottom row reaches the
fully-correlated value ½ by a *different* mechanism — the symmetric ensemble below
T_c is a two-component mixture, i.e. symmetry breaking. Same order, two
mechanisms, two values. That separation is what the order-resolved defect buys
over the bare statement "χ diverges", which cannot tell them apart.

**No order exists ⇒ floor 3's heavy tails.** For α-stable summands with α = 1.5
the empirical δ₂ does not converge at all: centred at −0.39 … −2.93 with
across-seed spread 1.8 … 7.4, against a Gaussian control at 0.00 ± 0.03. There is
no order-2 statement to make. This retrodicts the sort's **P-B** — that diffusion
splits into floor 2 and floor 3 at exactly finite-vs-infinite variance — which
was written down before this derivation existed and is now not a separate
prediction but the order-2 clause of one condition.

**So the tower re-read:**

```
   order 0 fails            ->  Phi* = concave hull != s   ->  FLOOR 2's Legendre face
   order 2 fails, anomalous ->  Var/N -> infinity          ->  FLOOR 3, criticality
   order 2 fails, mixture   ->  delta_2 = 1/2              ->  FLOOR 3, symmetry breaking
   no order exists          ->  cumulants absent           ->  FLOOR 3, heavy tails
```

Floor 3 was a *classified set* with no principle behind the classification —
[FLOORS.md](../invariants/FLOORS.md) §2's "floor 2 collapses, floor 3 stratifies"
recorded the fact and could not explain it beyond D2's group argument. The
stratification now has a second reading with a different grain: floor 3's members
are the ways a composition law can lapse, indexed by the order at which it does.

This does not compete with [D6](../experiments/D6-support-singularities/)'s
classifier q1/q2. D6 classifies the *shape* of a singularity once you are at one;
C4 says what *kind of failure* being at one is. Whether the two indices are
related — whether q1/q2 is computable from the failing order — is not addressed
here and is the obvious next question.

## 6. Where the lens comes from, with no outside

C1–C4 all presuppose the decomposition into parts. Since there is no outside, that
decomposition cannot be handed over either. It has to be chosen from inside, and
there is a standard answer to how: **by the dynamics.** The decomposition that
makes ⊎ work is the one across which interaction is weakest, and finding it is a
minimization the system's own generator defines — the *quantum mereology* program
(Zanardi 2001; Tegmark 2015; Cotler–Penington–Ranard 2019; Carroll & Singh 2021),
where locality and the tensor-factorization into subsystems are *derived* from the
Hamiltonian's spectrum rather than assumed.

**This half is argued, not measured.** Nothing in the run touches it, and it is
recorded as untested. What it supplies is the answer to the question that opened
this derivation: *is there a point before the lens exists?* There is. Before a
decomposition is fixed there is no ⊎, hence no additive scalar, hence no Φ, hence
no floor 2 and nothing for floor 1 to coordinatize. Constructing the lens really
is the first task, and the system performs it on itself.

**And then the loop closes in a way worth stating plainly.** The cut that makes ⊎
additive is state-dependent, so it must be maintained; and the condition that
destroys it is not exotic. As the correlation length grows, the bipartition whose
halves are statistically independent gets harder to find, and at ξ → ∞ there is
none. That is §5's order-2 failure, and §5's order-2 failure is floor 3.

> **The lens is prior to the tower, and the tower's top floor is the lens
> breaking. Floor 0 and floor 3 are one condition read at different orders —
> which is why "there is a point before the lens exists" and "there is a point
> after it" have the same answer.**

## 7. What would kill this

1. **A natural parameter with a non-additive conjugate.** A genuine long-time
   ensemble parameterized by a conserved quantity that is neither additive nor
   affine in an additive one. Kills C2, and with it the argument that floor 1
   consumes an input rather than supplying one.
2. **A chart-invariant exponent in a variable that is neither additive nor dual to
   one, or a gauge exponent in one that is.** Kills C3 and returns
   FLOORS §4's residue question to open. The audit in §6 of the experiment is one
   pass over the repo's own ledger; it is small and a wider one could break it.
3. **Criticality without order-2 non-extensivity** — a divergence of ∇²Φ with
   Var(M)/N bounded, or an order-2 extensivity failure sitting at no floor-3
   object. Kills C4, the only at-risk claim.
4. **A system with no composition law that nonetheless has a Φ.** Kills the
   priority claim outright: floor 0 would be optional rather than prior. Driven
   non-stationary systems are the place to look, since the tower's own scope note
   already excludes them.
5. **The d ≥ 2 surface test coming out at exponent 1.** If an interacting
   short-range model with a first-order transition shows an *extensive* rather
   than surface-scaling defect, then "short-range ⇒ additive" is wrong and §5's
   order-0 clause loses its control.

## 8. Scope

- **Equilibrium / long-time (stationary) throughout**, inherited from the tower.
  The base-layer claim does not reach driven systems, and falsifier 4 lives there.
- **C1 and C2 are N0.** Cauchy's equation and Koopman–Pitman–Darmois are the
  content; the register's prior-art note names both. What is argued here is
  placement — that they sit *under* floor 1 — not that they are new.
- **C4's evidence is two mean-field models and one exactly solvable chain.** The
  order-0 clause has no interacting short-range control in d ≥ 2, which is the
  test with real teeth and is not run.
- **"Long-range" is one mean-field pair**, not a 1/r^σ family; where in σ the
  defect turns on is untouched.
- **The mereology half of §6 is untested**, and is the only part of the derivation
  that leans on literature the repo has not itself reproduced.
- **Two registered predictions failed** in the run — leg C's growth exponent and
  leg D3's discriminator — and are recorded in
  [the experiment](../experiments/D10-composition-lens/), not buried here.
- **The relation to D6's q1/q2 is open**, as §5 says: two indices on floor 3, no
  statement connecting them.
