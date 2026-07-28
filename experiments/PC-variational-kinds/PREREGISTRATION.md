# P-C pre-registration — written before any measurement

Works [P-C](../../invariants/FLOORS.md#3-what-the-sort-predicts-the-part-that-makes-this-a-test),
the [floor sort](../../invariants/FLOORS.md)'s remaining unrun prediction about
[#7](../../invariants/optimization-variational.md), a `seed` entry:

> **P-C — variational principles come in exactly two kinds.** Over a measure
> (free energy) ⇒ floor 2; over an action (bracket) ⇒ floor 1. **Falsifier:** a
> genuine variational law — one that predicts, rather than re-describes — whose
> functional is over neither.

[P-D](../PD-allometry-reduction/) complicated it before it was run, and the
[research log](../../research-log/2026-07-27-PD-allometry.md) asked that the
complication be registered from the start rather than discovered mid-run:

> P-C says variational principles come in exactly two kinds. P-D exhibits a third
> case its binary has no slot for — a genuine optimization over a measure whose
> *exponent* is not a Φ-derivative, because the optimization **selects a scheme**
> and the scheme carries the exponent. P-C should be run with that case explicitly
> in its registration.

So this is not a test of the binary as written. The binary is already known to be
inadequate; running it as stated would be the strawman
[P-D warned about](../PD-allometry-reduction/PREREGISTRATION.md). The registered
claim is the repair, and the repair has to be able to fail.

---

## 0. Prior-art note (written first)

This is a floor-sort prediction, not a discovery-register stone, so the novelty
burden is lower — but three of the four legs use machinery with owners, and saying
so in advance is what stops the write-up from laundering them.

**Old, and load-bearing.**

- The **Helmholtz decomposition of a game's pseudo-gradient** into symmetric
  (potential) and antisymmetric (Hamiltonian) parts is Balduzzi et al. 2018
  ("The Mechanics of n-Player Differentiable Games"). Potential games are
  Monderer–Shapley 1996; the symmetry criterion (∂ᵢuⱼ = ∂ⱼuᵢ) is theirs.
- **Rotation can stabilize** is not new either: it is gyroscopic stabilization,
  known since Thomson–Tait, and the modern statement (a gyroscopic term can
  stabilize a statically unstable equilibrium, subject to a parity condition on the
  number of unstable directions) is standard in mechanics. Also known in the
  learning-dynamics literature as the reason adversarial games converge in
  directions no potential explains.
- **Bertrand's theorem** (1873): the only central potentials with all bounded
  orbits closed are −k/r and ½kr². The 2D Kepler and harmonic problems are
  maximally superintegrable (2n − 1 = 3 independent constants); a generic central
  potential has 2.
- **The Master theorem** and the Karatsuba/Toom-Cook crossover ladder are textbook;
  that GMP switches algorithm at size thresholds set by machine constants is
  engineering practice, not a finding.

**Not covered, and what is actually claimed.** That these are **one classification
of readouts**, mechanically decidable by the response of a readout to the
functional's parameters, with **three** types rather than two:

| type | response of the readout to the functional's magnitudes | jump locus |
|---|---|---|
| **floor 2** — source, measure-type | smooth, full-rank | — |
| **floor 1** — source, action-type | **null** | where the invariance group changes |
| **selector** — the case P-D found | **null a.e., jumps** | where two argmin branches cross |

and that the third type's jump locus is a **kink in the optimal-value function** —
which, if it holds, identifies the non-analyticity
[P-D flagged and left open](../../invariants/FLOORS.md#4-what-refused-the-tower--and-the-shape-it-makes)
(θ = min(1, ln n/−ln β²γ) is non-analytic at nβ²γ = 1, and nobody knew what floor
that kink was on).

**Nearest miss, recorded so it cannot be relabelled.** If the three-way response
classification is a restatement of the standard distinction between *smooth* and
*combinatorial* optimization — parametric programming's basis-change loci are
exactly the selector's cells, and sensitivity analysis is exactly the rank test —
then the mechanical content here is **N0** and only the tower placement survives.
That is a live possibility and I expect the write-up to have to concede it.

---

## 1. The claim, in three separable propositions

**C1 — the floor is a property of the readout, not of the functional.**
One variational problem can emit a floor-2 readout and a selector readout at once.
Operationally: for readout R and functional parameters θ, the discriminator is the
Jacobian ∂R/∂θ. Full rank ⇒ source. Rank 0 with jumps ⇒ selector.

**C2 — "over a measure" vs "over an action" is a decomposition, not a partition.**
At an equilibrium with pseudo-gradient Jacobian J, write J = S + A (symmetric +
antisymmetric). S is the potential content, A is the bracket content, and the
potential fraction π = ‖S‖²_F/(‖S‖²_F + ‖A‖²_F) is a continuous mixture parameter
the binary has no slot for. The two "kinds" are its two poles.

**C3 — P-C's registered falsifier fires.** There exist predictive variational laws
with no potential: the region {S ⊁ 0} ∩ {Re λ(J) > 0} — no potential has a minimum
here, yet gradient play converges — is **nonempty and not small**. The mechanism is
that rotation replaces S ≻ 0's *n* conditions with **⌈n/2⌉** conditions, one per
invariant 2-plane of A.

If C3's region is empty, P-C survives in a stronger form than it was written
("prediction requires a potential") and C2 is decorative.

---

## 2. Identity vs. risk — the required disclosure

[`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §4 names
tautology-by-construction as the failure this project keeps committing —
three times so far, most recently
[D6's P2](../D6-support-singularities/README.md), each time by calling a
consequence of my own construction a test of it. So, explicitly:

**Analytic identities. These cannot come out wrong and are not evidence.**

- **P1** — the two poles. A = 0 gives an exact potential; S = 0 conserves ½|x|²
  exactly. Both are definitions differentiated.
- **P4** — the n = 2 stabilization threshold a_c = √(2·λ_max·|λ_min|). Two lines of
  algebra from trace and determinant. *(Normalization slip corrected here before
  any code was run: with ‖A‖_F = 1 the 2×2 generator is A = 2^(−½)·[[0,1],[−1,0]],
  so det J = λ₁λ₂ + a²/2 and the factor 2 belongs inside the root. Recorded rather
  than silently fixed, per the register's rule about the identity/risk split.)*
- **P6** — the divide-and-conquer exponent equals log_b a within a selection cell,
  and is magnitude-blind there. **This is true by construction** — I am choosing a
  scheme set indexed by (a, b) and reading log_b a off the winner. It verifies the
  estimator and nothing else. The selector claim rests on P7/P8, not on this.
- **P9** — Bertrand: ω_r/ω_θ = 1 for −k/r and 2 for ½kr². A theorem check on the
  integrator.
- **P11, selector half** — a min of two smooth branches kinks at the crossing.
  Structurally forced. The at-risk half is the floor-1 side (below).

**Genuinely at risk.**

- **P2 / P3 / P5** — everything about C3. The perturbation argument behind the
  ⌈n/2⌉ count is mine and could be wrong; the region could be empty or negligible;
  the nonlinear instance could fail to converge.
- **P7 / P8** — that the cost model's magnitudes actually flip the winner over the
  registered box (if one scheme always wins, "selector" is an empty word here), and
  that **one** rank instrument with **one** tolerance separates all three response
  types without hand-tuning.
- **P10** — that the charge count is blind to magnitude across the registered
  sweep, measured through an integrator that can fail.
- **P11, floor-1 half** — that the symmetry-change locus carries **no** kink.
  Nothing guarantees this: floor 3's whole content is that symmetry changes
  *do* produce non-analyticities (SSB), so predicting analyticity here is a real
  bet against the tower's own best-known behaviour.

---

## 3. Registered predictions

### Leg A — the two poles (identity; estimator check)

**P1.** For n = 6, over 200 draws:
(a) with A = 0, gradient play converges iff S ≻ 0, and the line integral of the
pseudo-gradient around 50 random closed loops is path-independent to **≤ 1e-12**;
(b) with S = 0, ½|x|² is conserved along the flow to **≤ 1e-10** over 10⁴ steps,
and the same loop integral has circulation **≥ 0.1** (a potential does not exist).
The potential fraction π reads 1.000 and 0.000 respectively.

### Leg B — C3: potential-free but predictive (AT RISK; the central measurement)

Ensemble: S = (G + Gᵀ)/2, A = (H − Hᵀ)/2 with G, H entries i.i.d. N(0, 1/n), each
normalized to ‖·‖_F = 1; J = S + a·A. Gradient play ẋ = −Jx.

**P2 (AT RISK).** At n = 6, a = 100, over 20 000 draws, the fraction with
**S ⊁ 0 and Re λ(J) > 0** is **≥ 0.10**. The null hypothesis this experiment is
run against — P-C as written, "prediction requires a potential" — predicts
**0.000**.

**P2b (AT RISK).** These are not weighted potential games either: for ≥ 99% of the
draws in that region, no positive diagonal D makes DJ symmetric, measured as
min_D ‖DJ − (DJ)ᵀ‖_F/‖J‖_F > **0.1** over D in a log-parameterized search.

**P3 (AT RISK — the mechanism).** In the large-a limit the stability criterion is
that all **⌈n/2⌉** two-plane averages ½(uⱼᵀSuⱼ + wⱼᵀSwⱼ) are positive, where
(uⱼ, wⱼ) are A's real Schur 2-planes. Predict agreement between this criterion and
the measured sign of min Re λ(J) at a = 100 of **≥ 0.98** for n = 2, 4, 6, 8.
Predict at n = 2 the stable fraction is **0.500 ± 0.02** (the criterion collapses to
tr S > 0, which is symmetric under S → −S).

**P3b (AT RISK — the counting).** The number of binding conditions halves.
Operationally: at n = 6, fraction stable at a = 100 divided by P(S ≻ 0) is
**≥ 10**. Both numbers reported.

**P4 (identity).** n = 2, S indefinite: measured a_c matches √(2·λ_max|λ_min|) to
**≤ 1e-6 relative** (see §2 for the normalization correction).

**P5 (AT RISK — nonlinear, and the "does it predict" half).** A two-player game
with quadratic-plus-cubic payoffs constructed to have S indefinite at its interior
equilibrium. Predict simultaneous gradient play from 100 random starts in a
registered basin converges to that equilibrium (‖x − x*‖ < **1e-8**) in ≥ 95 of
100 runs, while the pseudo-gradient's circulation around a loop enclosing the
equilibrium is **≥ 0.01** so no potential exists. A variational object with no
potential that nonetheless predicts where the system ends up is exactly P-C's
registered falsifier.

### Leg C — C1: the selector, in a domain that is not physics (AT RISK)

Integer multiplication. Four **real** schemes, each recursing to a base case:
schoolbook (a=4, b=2), Karatsuba (3, 2), Toom-3 (5, 3), Toom-4 (7, 4). Six
magnitudes θ_m = (c_mul, c_add, c_call, c_mem, c_eval, n_base), swept over a
registered box of ±2 decades around a machine-plausible centre. The variational
problem: choose the scheme minimizing T_s(N) at a fixed operating size N = 2¹⁴
words. Readouts: **R_exp** = log_b a of the winner; **R_const** = T*(N)/N^R_exp.

**P6 (identity, declared).** Within a cell, ∂R_exp/∂ln θ_m = **0** to machine
precision and R_exp ∈ {2, 1.5850, 1.4650, 1.4037}. Not evidence.

**P7 (AT RISK).** Over 4000 Latin-hypercube samples of the box, **≥ 3** distinct
schemes win somewhere and **≥ 3** distinct exponents are realized, each with
frequency **≥ 2%**. If one scheme always wins, this leg is void and says so.

**P8 (AT RISK — the instrument).** One rank test, one tolerance (singular values
below 1e-8 × the largest are zero), applied to ∂R/∂ln θ for three readouts:

| readout | predicted rank |
|---|---|
| D&C exponent R_exp | **0** |
| D&C constant R_const | **6** (full) |
| Gibbs exchange rate ⟨x⟩ = ∇log Z, floor-2 control | **full** (= dim λ = 5) |

Three answers from one instrument. Failure mode that would count against: needing
a different tolerance per readout, or the constant coming out rank-deficient
(which would mean the selector swallowed the magnitudes too and C1's "two readouts,
two floors" is wrong).

### Leg D — floor 1's response type (AT RISK)

Planar central-force motion, symplectic integrator. Count of independent constants
read off the orbit: ω_r/ω_θ rational ⇒ closed orbit ⇒ 3 constants; irrational ⇒
2 (invariant 2-torus).

**P9 (identity/theorem).** ω_r/ω_θ = **1.000000** for V = −k/r and **2.000000** for
V = ½kr², to ≤ 1e-5.

**P10 (AT RISK).** That ratio is invariant across **4 decades of k** and **3 decades
of |E|** to **≤ 1e-5** — the floor-1 readout is magnitude-blind. For V = k·r^α with
α ∈ {1, 3, −0.5} the ratio is irrational (no rational p/q with q ≤ 12 within 1e-4)
so the count is 2, and it too is k-invariant.

**P11 (the discriminator; selector half is an identity, floor-1 half is AT RISK).**
Perturb *within* the rotationally symmetric class: V = −k/r + δ/r².

- Floor-1 side (AT RISK): the count jumps from 3 to 2 at δ = 0, while the circular
  orbit's energy E_circ(δ) is **analytic through δ = 0** — left and right numerical
  derivatives agreeing to **≤ 1e-4 relative** — and the dynamical response is
  smooth: precession per orbit ∝ δ^**1.00 ± 0.03** over three decades of δ.
- Selector side (identity): at each Leg-C cell boundary, V*(θ) = min_s T_s is
  continuous while its one-sided slopes differ by **≥ 10%**.

**Discontinuous count + analytic value ⇒ floor 1. Discontinuous readout + kinked
value ⇒ selector.** That is the whole discriminator, and it is what P-D's
unexplained kink is being tested against.

---

## 4. What would kill this

- **P2 fails** (region empty) — P-C survives in a *stronger* form than written and
  C2/C3 are wrong. This is the outcome that would most change my mind.
- **P3 fails** — the region exists but my mechanism for it does not, so C3's
  explanatory half is unearned and only the bare existence claim survives.
- **P7 fails** — no cross-domain selector instance outside P-D's allometry, so C1
  rests on one case and the "new domain" claim is void.
- **P8 fails** — the response classification is not mechanically decidable with one
  instrument, which was its main advantage over the taxonomy it replaces.
- **P11's floor-1 half fails** (a kink at δ = 0) — then kinked-value does not
  separate selector from floor 1, and P-D's kink stays unexplained.

## 5. Scope, registered

- **Linear-quadratic games in Leg B, except P5.** Real games are not quadratic;
  what is measured is the local structure at an equilibrium, which is what the
  Jacobian classification is about, but the ensemble is synthetic.
- **Leg C tests a cost model, not a compiler.** As with
  [P-D and organisms](../PD-allometry-reduction/README.md), this establishes what
  kind of object the exponent is in the model that produces it, and says nothing
  about which algorithm is actually fastest on any machine.
- **Leg D is 2-D and classical**, and "count" is read from orbit closure rather
  than from an independent computation of the constants.
- **No claim about non-equilibrium or dissipative variational principles**
  (Onsager, MaxEnt production). The tower is derived for stationary fields and this
  inherits that.
- **The floor-2 control is an exponential family**, i.e. the easiest possible case;
  a harder floor-2 control could blur P8.
