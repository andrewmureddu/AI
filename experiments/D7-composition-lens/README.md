# D7 — the composition law is floor 0

*2026-07-29. Works [D7](../../questions/UNKNOWN-LAWS.md#d7--is-there-a-floor-0-and-is-it-a-composition-law).
Pre-registration: [`PREREGISTRATION.md`](./PREREGISTRATION.md), written before any
measurement, with the q=2 control added in a separate commit still before the run.
Derivation: [`derivations/D7-composition-lens.md`](../../derivations/D7-composition-lens.md).*

**Result: floor 1 takes an input, and the input is a composition law. Additivity —
not conservation, not linearity, not monotonicity, not convexity — is what lets a
statistic occupy a natural-parameter slot (leg C, ≤3.2e-14 vs ≥8.8e-4). The
order-2 defect takes the three registered values 0.0024 / 0.29364 / 0.50010 at the
three temperatures, so criticality and symmetry-breaking are the same
extensivity failure at the same order by two mechanisms (leg D). Two registered
predictions failed and are on record.**

**And one pre-registered hypothesis was killed by its own control.** "Long-range ⇒
non-additive" is **false**: mean-field q=2 is exactly as long-range as mean-field
q=3 and its defect is *exactly zero*. The surviving claim is the weaker one the
pre-registration named in advance as the alternative — **long-range interaction
opens the possibility of non-additivity; a first-order transition realizes it.**

Run: `python3 run.py` (~45 s, pure numpy). Numbers: [`verdict.json`](./verdict.json).

---

## 1. The one definition

For a system of size N with observable cumulants κ_k,

```
        delta_k(N)  =  1  -  2 * kappa_k(N) / kappa_k(2N)
```

δ_k → 0 is "extensivity holds at order k." Φ = ln Z is the cumulant generating
function, so **"Φ is additive under composition" is one condition per order**, and
D7's claim C4 is that the tower's floors are the orders at which it fails.

The form never requires a spatial cut, which matters: long-range models do not
have one.

---

## 2. Leg B — the concavity defect and how it scales · **AT-RISK**

Exact counting, no sampling. Defect = N · max_e [ŝ(e) − s(e)], where ŝ is the
upper concave envelope: the entropy a *composite* reaches by letting its parts sit
at different energy densities, which an additive system can always do internally
and a non-additive one cannot.

| model | what it is | defect at N = 64 … 1024 | slope | c < 0 on |
|---|---|---|--:|--:|
| mean-field q=3 | long-range, **1st order** | 10.29 · 21.11 · 43.07 · 87.47 · 176.41 | **+1.0252** | **68.6%** of e |
| mean-field q=2 | long-range, 2nd order | 0 · 0 · 0 · 0 · 0 | **0** | 0% |
| 1-D chain q=3 | short-range, no transition | 0 · 0 · 0 · 0 · 0 | **0** | 0% |

- **B1 ✓ (check against literature).** The mean-field 3-state Potts entropy is
  non-concave on e ∈ [−0.4981, −0.1667], as Ispolatov & Cohen 2001 report.
- **B3 ✓.** Registered 1.00 ± 0.10 long-range, bounded short-range. Measured
  **1.0252** and **exactly 0** — the defect per site converges to a constant
  (0.1607 → 0.1723 over the size range) and the total is N times it.
- **B3b — the control fires, and it kills the strong reading.** This was added
  before the run precisely because q=3 confounds "long-range" with "first-order",
  and the confound was real. Long range is **necessary and not sufficient**.
- **B4 ✓.** Microcanonical specific heat is negative over 68.6% of the accessible
  energy range for q=3 and nowhere for either control. *(The magnitude of min c is
  set by where s″ → 0 and is not a physical number; only the sign and the measure
  of the region are reported as findings.)*
- **B2 — declared identity, used as a code check.** The two-copy maximum and the
  concave envelope, computed by independent routes, agree to 2.2e-16 and 3.4e-16
  for the concave models and to 1.45e-2 → 5.59e-3 (improving with grid resolution)
  for q=3. Carries no evidential weight; it is here to show the hull code is not
  the two-copy code wearing a hat.

**What this buys.** The canonical ensemble sees only ŝ. Where ŝ ≠ s the two
ensembles are inequivalent and **Φ\* is not s but its concave hull** — floor 2's
Legendre face, the one that makes entropy and free energy the same object seen
twice, fails exactly on the interval where composition fails. That is C4's order-0
prediction, and it is a *floor-2* breakdown caused by a *floor-0* condition.

---

## 3. Leg C — what closes an ensemble family under composition · **AT-RISK**

Two independent size-n systems at tilt μ; their product is a distribution on the
composite. How far is it from the composite's *own* family? KL minimized over the
family parameter, exactly, on the (Q_A, Q_B) lattice. Tilt strength is normalized
so μ is not a free knob: each statistic is tilted to the same KL from untilted.

| T(Q) | additive | linear | monotone | convex | KL_min, n = 8 … 128 | closes? |
|---|:--:|:--:|:--:|:--:|---|:--:|
| Q | ✓ | ✓ | ✓ | ✓ | 0 · 0 · 0 · 6.9e-16 · 3.2e-14 | **yes** |
| 3Q − 7 | ✓ | ✗ | ✓ | ✓ | 2.6e-16 · 0 · 4.0e-15 · 2.6e-14 · 0 | **yes** |
| Q² | ✗ | ✗ | ✓ | ✓ | 2.2e-2 · 2.2e-2 · 8.3e-3 · 4.5e-3 · 2.4e-3 | no |
| √Q | ✗ | ✗ | ✓ | ✗ | 1.4e-1 · 2.7e-3 · 5.1e-3 · 2.0e-3 · 8.8e-4 | no |
| ln(1+Q) | ✗ | ✗ | ✓ | ✗ | 2.3e-1 · 1.8e-1 · 3.3e-2 · 9.1e-3 · 1.9e-3 | no |
| Q mod 2 | ✗ | ✗ | ✗ | ✗ | 6.44e-1 at every n | no |

**C1 ✓, and the discrimination is the point.** The additive column is the only one
that matches the closure column. Each of the three nearby rules is refuted by a
specific row:

- **linearity** — refuted by `3Q − 7`, which is not linear and closes anyway (the
  offset is absorbed by normalization, so the rule is *affine in an additive
  charge*);
- **monotonicity** — refuted by Q², √Q and ln(1+Q), all monotone, none closing;
- **convexity** — refuted by Q² and √Q, opposite curvature, identical failure.

This is the measured face of **Koopman–Pitman–Darmois**, which the register's
prior-art note names as already being this claim. Nothing here is new physics;
what is new is where it sits — it is the rule floor 1 was stated without.

**C2 ✗ — a registered prediction failed.** I registered KL_min growing linearly in
n (1.00 ± 0.15); measured **−0.87, −1.51, −1.82** and **0.00** for the parity
statistic. The diagnosis is in the design: normalizing every tilt to the same KL
was introduced to remove a free knob, and it removes the growth along with it —
holding informativeness fixed as n grows shrinks μ, and the composition mismatch
shrinks with it. The quantity was ill-posed, not the claim; but the claim as
registered is refuted and stays refuted.

---

## 4. Leg D — order 2, and the three values · **AT-RISK, the sharpest leg**

Curie–Weiss, exact enumeration over total magnetization.

| | βJ | Var(M) scaling | δ₂ measured | δ₂ registered | error |
|---|--:|---|--:|--:|--:|
| above T_c | 0.8 | N^**1.022** | **0.00240** | 0 | 0.0024 |
| **at T_c** | 1.0 | N^**1.504** | **0.29364** | 1 − 2^{−1/2} = 0.29289 | **0.00075** |
| below T_c | 1.5 | N^**2.002** | **0.50010** | 0.5 | 0.00010 |

**D1 ✓.** The middle value is the load-bearing one. It is not 0 and not ½; it is
an *anomalous* value inherited from a critical exponent (Var ~ N^{3/2} because the
magnetization law at T_c is quartic, not Gaussian), and it is the direct
measurement that **criticality is an order-2 extensivity failure**. The five
arrivals at the singular set of ∇²Φ that
[SYNTHESIS §5](../../SYNTHESIS.md) records are arrivals at a broken composition
law, read at order 2.

**D2 ✓.** Below T_c the ratio is ½ — the fully-correlated value — reached by a
different mechanism (the symmetric ensemble is a two-component mixture, i.e.
symmetry breaking). Same order, two mechanisms, two different values. That
distinction is what the order-resolved defect buys over "χ diverges".

**D3 — mis-registered, reported as such.** Heavy tails, the "no order exists"
case: for α = 1.5 the empirical δ₂ is centred at −0.39 … −2.93 with across-seed
spread 1.8 … 7.4, against a Gaussian control at 0.00 ± 0.03. The *result* is what
C4 predicts — there is no order-2 statement to make, and the scale-based value
(1 − 2^{1−2/α} = 0.2063) is not what the variance estimator converges to, because
it does not converge. But my registered **discriminator** was wrong: I wrote that
the Gaussian control's spread would shrink like N^{−1/2}, and it does not — that
spread is set by the number of realizations, not by N. The working discriminator
is the centre and the magnitude, not the shrinkage.

---

## 5. Legs A and E — **DECLARED IDENTITIES**

Reported with the label attached; they carry no evidential weight and the write-up
does not lean on them.

**Leg A**, exact 1-D Ising: δ₀ ≤ 0.121 and falling as 1/N at every temperature,
while δ₂ → 0.499 for N/ξ = 0.006 and → 0.0166 for N/ξ = 22.5. The orders separate:
order 0 extensive at the same point where order 2 is not. Closed form throughout.

**Leg E1**, chart arithmetic: |1 − 2^{1−a}| = 0.4142 / 0 / 0.2929 / 0.5 at
a = 0.5 / 1 / 1.5 / 2, reproducing [P-D leg F](../PD-allometry-reduction/).

---

## 6. Leg E2 — the audit · **AT-RISK, and it forced a correction**

C3 predicted a clean sort: every exponent the repo files as gauge should live in a
variable with no additive composition law, every exponent filed as a fact in one
that has it. **No counterexample was found, but the rule as stated does not cover
the most important case and had to be widened.**

| exponent | its control variable | additive? | filed as | consistent |
|---|---|:--:|---|:--:|
| [D1](../D1-chart-invariance/)'s chart order *k* | ε, distance to threshold | no | gauge | ✓ |
| [D2](../D2-gauge-group/)'s RG eigenvalues *y* | coupling-space distance | no | gauge | ✓ |
| [S5](../S5-noise-thresholds/)'s type-R α | concatenation level *t* | no (a construction index, not a composite) | gauge | ✓ |
| [P-D](../PD-allometry-reduction/)'s θ | mass M | **yes** | fact | ✓ |
| [S25](../S25-rlct-singularity/)'s RLCT λ | sample count *n* | **yes** | fact | ✓ *(not designed for)* |
| [S28](../S28-sgd-charges/)'s decay rate | training time | **yes** | fact | ✓ |
| [S3](../S3-fisher-geometry/)/[S7](../S7-critical-slowing/) critical exponents | reduced temperature | **no** — and yet facts within physics | fact in-domain, gauge across | **forced the correction** |

**The correction.** Reduced temperature is intensive; by the rule as written its
exponents should be gauge, and inside physics they are not.
[D2 §7](../../derivations/D2-gauge-of-the-tower.md) already knew why without
saying it this way: the chart is pinned because the coupling "enters the
Hamiltonian linearly" — that is, because its **conjugate**, the energy, is
additive. An additive sufficient statistic induces an affine structure on the
natural-parameter space it is dual to. So:

> **C3, corrected: a chart is pinned to G_diff when its variable is additive under
> composition *or dual to one*. It keeps the larger group G_pow when neither
> holds, and then only ratios, signs and counts survive.**

Cross-domain comparison loses the pinning because the epidemic's R₀ and the
decoder's recursion depth are dual to no additive charge, which is exactly D1's
measurement that a fold and an SIS epidemic — the same degeneracy — differ 2× in
the bare chart.

**One confirmation the audit did not design for.** The RLCT is read off the
coefficient of ln n, and *n is additive*: samples compose. The rule therefore
predicts λ is a fact, not a chart artifact — which is independently true and
famously so (it is a birational invariant). A row the audit could have failed on,
that it passes.

---

## 7. Boundaries

- **Equilibrium / stationary throughout**, inheriting the tower's own restriction.
- **"Long-range" is one mean-field pair**, not a 1/r^σ family. The exponent-1
  defect is established for the extreme case; where the crossover sits in σ is
  untouched.
- **The forceful short-range control is missing.** The 1-D chain's entropy is
  log-binomial and therefore *exactly* concave, so its zero is close to an
  identity — registered as a weakness in advance (B3c). The version with teeth is
  an interacting model in d ≥ 2 with a first-order transition, where the defect
  should scale as the surface, N^{(d−1)/d} — neither 0 nor 1. That needs a density
  of states this run does not compute, and it is the cheapest next test.
- **Leg C has iid sites and no interaction.** It tests closure of a family under
  composition, not thermalization onto one.
- **Two registered items failed** (C2's growth exponent; D3's discriminator) and
  one pre-registered hypothesis was killed by its own control (B3b).
- **The quantum-mereology half is untested here.** That the decomposition into
  parts is selected by the dynamics rather than given is argued in the derivation
  and measured nowhere in this run.
- **Novelty stays N1.** Every mechanism above is somebody's textbook; the register
  entry lists whose. What the run establishes is *placement* — that one condition
  sits under floor 1 and that the tower's floors are its orders.
