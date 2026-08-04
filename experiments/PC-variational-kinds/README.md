# P-C — variational principles come in exactly two kinds?

**Tests** [P-C](../../invariants/FLOORS.md#3-what-the-sort-predicts-the-part-that-makes-this-a-test),
the [floor sort](../../invariants/FLOORS.md)'s last unrun prediction, about
[#7](../../invariants/optimization-variational.md) — a `seed` entry whose floor
assignment ("**2 + 1**, splits by what the functional is over") had nothing behind
it.

**Registered in** [`PREREGISTRATION.md`](./PREREGISTRATION.md) — prior-art note
first, then the identity/risk split, then the numbers. Run with
`python3 run.py` (numpy + scipy, seed 20260727, 24 s).

---

## Verdict

> **P-C's registered falsifier fires, and the binary is replaced rather than
> patched.** A *genuine* variational law with no potential at all — predictive, in
> the sense that the dynamics reach the equilibrium it names — is not a curiosity
> at the edge of the classification: it is **12.2%** of a natural ensemble at
> n = 6, against the **0.000** the prediction requires. The reason is a counting
> fact. Requiring a potential imposes *n* conditions (S ≻ 0); rotation reduces them
> to **⌈n/2⌉**, one per invariant 2-plane of the antisymmetric part. Measured
> agreement between that criterion and actual convergence: **1.0000 / 0.9985 /
> 0.9985 / 0.9995** at n = 2, 4, 6, 8.
>
> What replaces the binary is not a third kind of *functional* but a **three-way
> classification of readouts**, mechanically decidable from the regularity of the
> optimal value: **smooth ⇒ floor 2, kinked ⇒ selector, jumping ⇒ a structural
> count** — and the count's response is *null*, which is floor 1's signature.
>
> **8 of 9 at-risk predictions passed; 4 of 5 declared identities.** The two
> failures are the same failure, are mine, and are the most useful thing here: I
> put a structural **count** (`n_base`) into my own list of *magnitudes*, and the
> instrument found it without being told — zero derivative on both sides and a
> discontinuous value. That is P-D's magnitude/count distinction reappearing
> inside my own parameter list, unplanted.

| | registered | measured | |
|---|---|---|---|
| **P1** two poles | identity | path-dep 6.8e-16, circulation 0.370, ΔE/E 1.3e-14 | ✓ |
| **P2** potential-free but predictive ≥ 0.10 | **AT RISK** | **0.1220** (null: 0.000) | ✓ |
| **P2b** not weighted-potential either | **AT RISK** | 200/200 residual > 0.1 (min **1.42**) | ✓ |
| **P3** plane-average mechanism ≥ 0.98 | **AT RISK** | **0.9985** min; n=2 stable **0.5084** vs 0.500 | ✓ |
| **P3b** condition count halves, ratio ≥ 10 | **AT RISK** | **2440** at n = 6 | ✓ |
| **P4** a_c = √(2 λ_max\|λ_min\|) | identity | 3.1e-15 max rel err, 73 cases | ✓ |
| **P5** nonlinear game still predicts | **AT RISK** | **100/100** converge, circulation **5.14** | ✓ |
| **P6** exponent magnitude-blind in a cell | identity | **400/400** exactly 0 | ✓ |
| **P7** ≥ 3 schemes, ≥ 3 exponents | **AT RISK** | 3 schemes (26.9 / 21.4 / 51.7%), 3 exponents | ✓ |
| **P8** one rank instrument: 0 / 6 / 5 | **AT RISK** | 0 / **4** / 5 | ✗ |
| **P9** Bertrand 1 and 2 | identity | **1.000000000** / **2.000000000** | ✓ |
| **P10** floor-1 readout magnitude-blind | **AT RISK** | spread **5.5e-10** / **4.0e-9** over 4 decades of k | ✓ |
| **P11** selector half: kink at the boundary | identity | ✗ as registered; **✓ on all 5 magnitude crossings** | ✗ |
| **P11** floor-1 half: value analytic | **AT RISK** | slopes agree **6.2e-6**; precession ∝ δ^**0.9760** | ✓ |

---

## 1. The claim, and why it was not run as written

P-C says variational principles come in exactly two kinds: over a measure ⇒
floor 2, over an action ⇒ floor 1. Running that as stated would have been a
strawman, and [P-D](../PD-allometry-reduction/) had already shown why — it
exhibited a genuine optimization *over a measure* whose readout is not a
Φ-derivative, because the optimization **selects a scheme** and the scheme carries
the law. The [research log](../../research-log/2026-07-27-PD-allometry.md) asked
that this be registered from the start, so the experiment tests the repair:

- **C1** — the floor is a property of the **readout**, not of the functional.
- **C2** — "measure" and "action" are the two **poles of a decomposition**
  (J = S + A at the equilibrium), not two boxes.
- **C3** — P-C's own falsifier fires: predictive variational laws exist with no
  potential.

---

## 2. C3 — the falsifier fires, and the reason is a count

**Setup.** Pseudo-gradient Jacobian J = S + a·A at an equilibrium, S symmetric
(GOE-like) and A antisymmetric, each Frobenius-normalised, a = 100. A potential
whose minimum sits at the equilibrium requires S ≻ 0. Gradient play converges iff
Re λ(J) > 0 for every eigenvalue. The two are not the same condition.

| n | P(S ≻ 0) | P(converges) | **P(no potential *and* converges)** | plane criterion |
|--:|--:|--:|--:|--:|
| 2 | 0.14575 | 0.5084 | **0.3626** | 1.0000 |
| 4 | 0.00337 | 0.2482 | **0.2449** | 0.9985 |
| 6 | 0.00005 | 0.1220 | **0.1220** | 0.9985 |
| 8 | 0.00000 | 0.0591 | **0.0591** | 0.9995 |

At n = 8, **not one draw in 8000 had a potential**, and 5.9% of them converge. The
region P-C's falsifier asks for is not a corner case; above n = 4 it is
*essentially all* of the convergent region.

**Why.** For J = S + aA at large a, each conjugate eigenvalue pair of A picks up a
real part equal to the average of S's quadratic form over A's invariant 2-plane:
Re λⱼ → ½(uⱼᵀSuⱼ + wⱼᵀSwⱼ). So stability stops being "*n* eigenvalues of S
positive" and becomes "**⌈n/2⌉ plane averages positive**". Rotation does not evade
the conditions; it **pairs them up**, and a pair survives when its two directions
cancel. At n = 2 the single plane average is tr(S)/2, so the criterion collapses to
tr S > 0 — symmetric under S → −S, hence the registered **0.500**, measured
**0.5084**.

The counting shows up directly: at n = 6 the convergent fraction is **2440×**
P(S ≻ 0).

**Not a weighted potential game either.** Games can have a potential after a
positive diagonal rescaling. Searching over D for min‖DJ − (DJ)ᵀ‖_F/‖J‖_F on 200
draws from the region: **every one** exceeds 0.1, the smallest residual is
**1.42**. There is no potential in the weighted sense either.

**And it is not an artifact of linearity.** A two-player game with quadratic +
quartic losses,

```
    L1 = ½x1² + (a/√2)·x1x2 + κx1⁴/4          L2 = -¼x2² - (a/√2)·x1x2 + κx2⁴/4
```

has symmetric part diag(**+1.000, −0.500**) at its equilibrium — indefinite, so no
potential has a minimum there — Re λ(J) = 0.250 for both eigenvalues, and
simultaneous gradient play converges from **100 of 100** random starts. The
pseudo-gradient's circulation around a loop enclosing the equilibrium is **5.14**,
so the field is not a gradient of anything. **A variational object with no
potential that nonetheless predicts where the system ends up is precisely what
P-C said should not exist.**

**Reading.** C2 is what survives: the antisymmetric part is not a *different kind*
of variational principle, it is the bracket content of the same one, and the
potential fraction π = ‖S‖²/(‖S‖² + ‖A‖²) is a continuous parameter running
between P-C's two "kinds". Floor 1 and floor 2 are its poles, and generic points
are mixtures. Prior art is explicit about the pieces — the Helmholtz split of a
game's pseudo-gradient is Balduzzi et al. 2018, gyroscopic stabilization is
Thomson–Tait — so what is claimed here is the tower placement, not the mathematics.

---

## 3. C1 — the selector, measured outside physics

Both at-risk legs of [D1](../D1-chart-invariance/) and
[D2](../D2-gauge-group/) were physics, which both passes recorded as a limitation.
This leg is computer science: integer multiplication, four **real** schemes
recursing to a base case — schoolbook (a=4, b=2), Karatsuba (3, 2), Toom-3 (5, 3),
Toom-4 (7, 4) — with a six-parameter cost model swept over ±2 decades, and the
variational problem "choose the scheme minimizing T(N) at N = 2¹⁴".

**Two readouts, one optimization.** The **exponent** log_b a of the winner, and the
**constant** T*(N)/N^exponent.

- The cells are real: over 4000 Latin-hypercube samples, three schemes win —
  Toom-4 **51.7%**, Karatsuba **26.9%**, Toom-3 **21.4%** — realizing three
  exponents (1.4037, 1.5850, 1.4650). *(Schoolbook never wins at N = 2¹⁴ anywhere
  in the box; the exponent 2 is not realized, and that is stated rather than
  papered over.)*
- Inside a cell the exponent's Jacobian with respect to every magnitude is
  **exactly zero at 400 of 400 interior points** — declared an identity in advance,
  since I chose a scheme set indexed by (a, b) and read log_b a off the winner. It
  checks the estimator and is not evidence.
- The constant's Jacobian is not zero. **One optimization emits a magnitude-blind
  readout and a magnitude-sensitive one at the same time**, which is C1.

### P8 failed, and the diagnosis is the finding

Registered: one rank test at one tolerance gives 0 for the exponent, **6** for the
constant, 5 for the floor-2 control (a Gibbs exchange rate ⟨x⟩ = ∇log Z). Measured:
0, **4**, 5 — with the smallest singular value of the constant's Jacobian exactly
**0.0**, so the deficiency is structural, not numerical. Post-hoc, both missing
directions are located:

- **`n_base` has derivative identically 0.0** — it is the recursion cutoff, a
  *count*, and perturbing it inside a level does nothing at all. I had listed it as
  a magnitude.
- **`c_add`, `c_mem`, `c_eval` enter only through α_s·c_add + γ_s·c_mem + δ_s·c_eval
  for the winning scheme**, so across the six operating sizes they span **2**
  directions, not 3.

2 + 1 + 1 = 4 exactly. Re-run on the identifiable coordinates
(c_mul, c_call, per-word scale) the rank is **3 of 3, full at 60 of 60 points**.

**So the instrument was right and the registered number was unattainable in the
cost model I wrote.** This is the fourth registration slip of this family in the
project ([P-A](../PA-spectral-gap/)'s threshold,
[P-D](../PD-allometry-reduction/)'s MST and control,
[D6](../D6-support-singularities/)'s P2) — but the first in the *opposite*
direction: not calling a construction-forced consequence a test, but registering a
number my own construction forbade. Same root cause: not auditing the construction
before registering a number about it.

### P11 failed for the same reason — and the failure adds a third class

Registered: at a cell boundary the optimal value V*(θ) is continuous with a
one-sided slope gap ≥ 10%. Reported as FAIL because I swept `n_base` as if it were
a magnitude. Split by what the swept parameter actually is:

| swept parameter | crossings | value jump | one-sided slope gap |
|---|--:|--:|--:|
| true magnitudes (c_mul, c_add, c_eval) | 5 | **exactly 0.0** | **0.204 – 1.000** |
| the count `n_base` | 6 | **8.3e-4 – 2.8e-2** | **exactly 0.0** |

On the five genuine magnitude crossings the registered claim holds **exactly** —
continuous value, kinked slope, every gap above the registered 10%. On the count,
the value itself jumps and there is no slope on either side.

**One instrument, three regularity classes, separated without being told apart:**

```
  magnitude, interior      value smooth              ->  floor 2  (source)
  magnitude, cell boundary value continuous, kinked  ->  SELECTOR
  structural count         value discontinuous       ->  a count, no derivative
```

---

## 4. Floor 1's response type, and what separates it from a selector

If both floor 1 and the selector produce magnitude-blind integers, the tower needs
something that tells them apart. Leg D measures it on planar central-force motion,
where the number of independent constants is read off the orbit
(ω_r/ω_θ rational ⇒ closed orbit ⇒ 3 constants; irrational ⇒ 2).

- **Bertrand, as a check on the quadrature:** ω_r/ω_θ = **1.000000000** for −k/r and
  **2.000000000** for ½kr².
- **Magnitude-blind:** across 4 decades of k × 3 decades of |E| × 3 eccentricities,
  the ratio moves by **5.5e-10** (Kepler) and **4.0e-9** (harmonic).
- **And blind to the orbit, which is the Bertrand-specific part.** For V = k·r^α
  the near-circular ratio is 1.7345 / 2.2323 / 1.2269 against √(α+2) =
  1.7321 / 2.2361 / 1.2247, k-invariant to **3.1e-10** — but it **moves with
  eccentricity** by 0.037–0.061. The Bertrand potentials' ratio does not move at
  all. Non-Bertrand ⇒ 2 constants, and it is the *rationality*, not the
  magnitude-blindness, that separates them.

**The discriminator.** Perturb inside the rotationally symmetric class:
V = −k/r + δ/r². The constant count **jumps from 3 to 2 the moment δ ≠ 0** — the
hidden SO(4) breaks — while:

- the circular orbit's energy E_circ(δ) is **analytic through δ = 0**: one-sided
  derivatives 2.44141 and 2.44140, agreeing to **6.2e-6**;
- the dynamical response is smooth and linear: precession per orbit ∝
  δ^**0.9760** over three decades (registered 1.00 ± 0.03).

Set against §3's table:

> **Discontinuous count + analytic value ⇒ floor 1.
> Discontinuous readout + kinked value ⇒ selector.**

Both are magnitude-blind integers; the optimal value's regularity is what tells
them apart, and it is measurable.

---

## 5. What this does to P-D's kink

> **⟳ RETRACTED 2026-07-28 by [P-K](../PK-kink-taxonomy/).** The account below is
> wrong, and the section is kept unedited because the way it is wrong is useful.
> The instinct was right — a min of two branches — but the mechanism is not an
> argmin crossing. Reading P-D's code, θ = min(1, ·) is the **tropical limit of a
> `logsumexp`**: a dominance switch between the two ends of a geometric sum. The
> two are distinguishable by **finite-size rounding**, which this section did not
> think to check: a selector boundary is non-analytic *already*, with zero width at
> every size, whereas P-D's θ is **analytic at every finite depth** and rounds as
> N^−0.9731. So the kink is a floor-3 non-analyticity of the
> **first-order-transition class**, not a selector cell boundary. The lesson for
> this experiment: the shape of a formula does not identify the operation that
> produced it, and I inferred the operation from the shape.

*The original section follows, unedited.*

[P-D](../PD-allometry-reduction/) measured θ = min(1, ln n/−ln β²γ), noted it is
**non-analytic at nβ²γ = 1 with Murray's law sitting exactly on the kink**, and
[FLOORS §4](../../invariants/FLOORS.md#4-what-refused-the-tower--and-the-shape-it-makes)
flagged the kink as unexplained — "whether that kink is a floor-3 degeneracy read
in a scheme variable, or a fact about the description map with no floor-3
counterpart, is untested."

Leg C measures the generic selector cell boundary and finds exactly that signature:
a readout that jumps, a value that stays continuous, and a slope that kinks —
because a min over branches is non-analytic where the branches cross. That makes
**"selector cell boundary" the leading account of P-D's kink**, and it names the
measurement that would settle it rather than settling it here: check whether
nβ²γ = 1 is where two branches exchange dominance *and* whether the cost
functional's optimal value kinks there. **Not measured in this run**, and recorded
that way so a later claim cannot be backdated.

If it holds, the kink is a floor-3 non-analyticity — but of the **optimal-value
function**, not of the system's own Φ. Which would be a small, precise addition to
the tower rather than a new floor: the argmin of a Φ is itself a Φ, with its own
singular part.

---

## 6. Honest limits

- **Leg B is linear-quadratic except P5.** What is measured is the local structure
  at an equilibrium, which is what a Jacobian classification is about, but the
  ensemble is synthetic and GOE-like. The one nonlinear instance is 2-D.
- **The ⌈n/2⌉ mechanism is verified, not derived here.** Agreement of 0.9985 at
  a = 100 is a large-a statement; the finite-a boundary is only pinned exactly at
  n = 2 (P4), where it is an identity.
- **P2b's search over D is a numerical minimum**, so "no weighted potential exists"
  is an empirical statement with residuals ≥ 1.42, not a proof.
- **Leg C tests a cost model, not a compiler** — the same restriction P-D carries
  about organisms. It establishes what kind of object the exponent is in the model
  that produces it. Schoolbook never winning is a fact about N = 2¹⁴ and the box.
- **P8's registered rank was wrong for a reason internal to my construction**, so
  the surviving claim is only the *ordering* 0 < 4 = full-on-identifiable-coords <
  5, not the exact numbers. A cleanly parameterized cost model would make this leg
  sharper and has not been run.
- **Leg D is 2-D and classical**, and the count is inferred from orbit closure
  rather than computed independently. The δ/r² perturbation is the easiest possible
  symmetry break; a shape change that also breaks rotational symmetry was not
  tried, and floor 3's whole content is that *some* symmetry changes produce
  non-analyticity (SSB) — so P11's floor-1 half is confirmed on one benign case,
  not in general.
- **Nothing here touches non-equilibrium variational principles** (Onsager, MaxEnt
  production). The tower is derived for stationary fields and this inherits that.
- **The three-way response classification may be N0.** Parametric programming's
  basis-change loci are the selector's cells and sensitivity analysis is the rank
  test; the prior-art note says so, and if that is the right reading then only the
  tower placement is new here.
