# D7 pre-registration — written before any measurement

Works [D7](../../questions/UNKNOWN-LAWS.md), the successor to the map's P0: the
invariant residue has three members found by three routes
([D2](../../derivations/D2-gauge-of-the-tower.md)'s codimension p − 2,
[D6](../D6-support-singularities/)'s q1/q2, [P-D](../PD-allometry-reduction/)'s
θ) and no general statement. Derivation:
[`derivations/D7-the-residue.md`](../../derivations/D7-the-residue.md).

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers. The prior-art note is in the register entry and
is unusually deflationary — every piece of the mathematics is old.

---

## 0. What is at stake

The claim is that the residue is the log-slope vector modulo the **diagonal** ℝ⁺,
i.e. the slopes of observables against other observables, with **n − 1**
independent invariants. Everything measured here is in the service of four
consequences, three of which are corrections to statements the map currently
carries:

1. every observable's log-slope has **weight exactly 1** under ε ↦ ε^a;
2. the count of independent invariants is **n − 1**, tested at n > 2 for the first
   time;
3. the residue is **not intrinsically discrete** — `FLOORS.md` reads D2's integer
   as a codimension;
4. **common-*a* is the group**, so independent per-direction re-charting must kill
   every ratio and leave only signs.

## 1. Identity vs. risk — the required disclosure

The register's §4 names tautology-by-construction as this project's recurring
failure, and [D6](../D6-support-singularities/) recorded it happening for the third
time. This section is written to be checkable against the results afterwards.

**Analytic identities. These cannot come out wrong and are not evidence:**

- **P1 — exact-power models.** For O = c·ε^y with y exact, every ratio is invariant
  under ε ↦ ε^a by one line of algebra. P1 exists to check the estimator over the
  range of slopes used later, nothing more.
- **P6 — irrational residues.** That q1/q2 is irrational when q1/q2 is irrational
  is not a discovery. What is substantive is only that it contradicts "the residue
  is the codimension," which is a claim in the map and not an identity. Graded as
  an identity; its weight is in the interpretation, and that is declared here so it
  cannot be upgraded later.

**Control, not a test. Declared as such in advance:**

- **P4 — independent per-direction re-charting.** Given P2, the fact that
  componentwise rescaling moves the ratios is forced. Its role is to show that the
  invariance measured in P2/P3 is a property of the group and not something the
  estimator manufactures — i.e. it is the negative control that D6's P2 lacked.

**Genuinely at risk:**

- **P2 — weight 1 on an all-orders model.** The slopes are measured from a full
  potential with every order present, over a **window fixed in the new chart**, so
  different *a* interrogate different physical windows and corrections to scaling
  are free to break the uniform weight. This is the leg that can fail.
- **P2b — the observables hypothesis.** The derivation predicts that a
  chart-derivative observable transforms **affinely**, y_χ(a) = a·y_χ(1) + (a − 1),
  and therefore breaks the ratios. A specific competing formula with no free
  parameter, on a quantity the derivation says must be excluded. It can come out
  wrong in either direction: weight 1 would mean the scope condition is spurious,
  and neither law fitting would mean the framework is incomplete.
- **P3 — the count n − 1 at n = 5.** No member of the residue has been measured at
  n > 2. Nothing outside the derivation guarantees the measured slope vectors span
  a line rather than a plane.
- **P5 — one estimator, three classes.** The unification claim, and the only leg
  that carries the N2 grade. A single function, applied to a smooth germ, a
  support-type singularity and a branching scheme, must return D2's, D6's and
  P-D's numbers with nothing fitted. The scheme leg is where it should fail if it
  is going to: discrete chart, no Φ, no singularity.
- **P7 — the kink.** Whether P-D's non-analyticity is chart-invariant, which the
  D2/P-D reconciliation explicitly left open. The two branches could carry
  different weights, in which case the kink moves under coarse-graining and the
  projective-wall reading is wrong.

## 2. Models

**M-A, the all-orders germ (P1–P4).** One-dimensional gradient system

```
        Phi(y; eps) = y^p/p + c3·y^{p+1} + c4·y^{p+2} − eps·y ,   c3 = 0.2, c4 = 0.05
```

with y\* the root of Φ′ found numerically from the **full** Φ′ (not a truncation),
λ = Φ″(y\*), and Var, ⟨y⟩ from Gauss–Legendre quadrature of the exact stationary
density ∝ exp(−Φ/D) on a window around y\*. Asymptotically β = 1/(p−1) and
k = (p−2)/(p−1); the measured slopes will differ from these by the
corrections-to-scaling the c-terms generate, and that difference is the experiment's
error budget rather than a result.

**M-B, the two-term potential (P5b, P6).** Φ = A|y|^{q1} + B|y|^{q2}, exactly
[D6](../D6-support-singularities/)'s model, with A_c(D) located by excess kurtosis
crossing the midpoint of its two limiting values — D6's own estimator, reused
unchanged so that agreement with D6 is a check and not a re-fit.

**M-C, the branching scheme (P5c, P7).** [P-D](../PD-allometry-reduction/)'s
network: branching ratio n, radius ratio β, length ratio γ, capillary invariance, so
that at level count N

```
        B(N) = n^N ,      V(N) = (beta^2 gamma)^{-N} · sum_{k=0}^{N} (n beta^2 gamma)^k
```

with V evaluated as the **exact finite sum**, not its asymptotic form, so finite-N
corrections are present.

## 3. Registered predictions

**P1 — estimator check on exact powers (IDENTITY).** For O_i = ε^{y_i} with
y = (1/3, 2/3, −2/3, 4/3, 1/3), recovered slopes within **1e-10** and ratios
invariant under a ∈ {0.5, 1, 2, 3} to **1e-10**.

**P2 — weight 1 on M-A (AT RISK).** For p = 4 and p = 6, with the five observables
O = (y\*, λ, Var, ΔΦ = Φ(0) − Φ(y\*), Φ‴(y\*)) measured over the window
ε′ ∈ [1e-8, 1e-6] for each a ∈ {0.5, 0.75, 1, 1.5, 2, 3}:

- fitted weights w_i in y_i(a) = c_i·a^{w_i} equal to **1 within ±0.05** for all
  five observables and both p;
- the ratio y_λ/y_{y\*} equal to **p − 2 within ±5%** at every a, while the bare
  slopes move by the full factor **6×** across the a-range.

The 100:1 gap between "moves by 6×" and "stable to 5%" is the discrimination; the
5% is set by the corrections to scaling the c-terms generate over the widest
window, not chosen to be safe.

**P2b — the chart-derivative exception (AT RISK).** Add χ = dy\*/dε to the
observable set. Predict its measured slope follows

```
        y_chi(a) = a·y_chi(1) + (a − 1)     to within ±0.05 absolute,
```

that a pure-weight fit gives w ≠ 1 by **at least 0.1**, and that ratios formed with
χ move by at least **20%** across the a-range — i.e. the derivation's excluded case
misbehaves exactly as predicted rather than merely misbehaving.

**P3 — the count is n − 1 (AT RISK).** Assemble the 6 × 5 matrix of slope vectors
y(a) for M-A. Predict **σ₂/σ₁ < 0.05** (the vectors span a line), hence rank 1 and
**5 − 1 = 4** independent invariants. Reported alongside the same statistic for P4.

**P4 — independent re-charting kills the ratios (CONTROL).** Three-direction
anisotropic germ Φ = Σ_i y_i^{p_i}/p_i − Σ_i ε_i·y_i with p = (4, 6, 8) and
ε_i = ε^{a_i}, a = (0.7, 1.0, 1.6). Predict σ₂/σ₁ **> 0.2** (no shared ray), the
ratio y₂/y₁ moving by at least **1.5×**, and the sign vector unchanged in every
case.

**P5 — one estimator, three classes (AT RISK).** A single function
`residue(O_a, O_b) = d ln O_a / d ln O_b`, applied without modification:

| leg | system | quantities | predicted |
|---|---|---|:--:|
| P5a | M-A germ, p = 4 | y\* vs λ | **0.5000** |
| P5a | M-A germ, p = 6 | y\* vs λ | **0.2500** |
| P5b | M-B, (q1,q2) = (2,4) | A_c vs D | **0.5000** |
| P5b | M-B, (q1,q2) = (1,2) | A_c vs D | **0.5000** |
| P5b | M-B, (q1,q2) = (2,6) | A_c vs D | **0.6667** |
| P5b | M-B, (q1,q2) = (1,3) | A_c vs D | **0.6667** |
| P5c | M-C, n = 2…10, β = n^{−1/2}, γ = n^{−1/3} | B vs V | **0.7500** |

Tolerances **±0.01** for P5a/P5c and **±0.04** for P5b (D6's own). P5a must
reproduce D2's 0.5000 / 0.2503 and P5b must reproduce D6's table; P5c must
reproduce P-D's 3/4 — with the same code path, which is the whole claim.
Additionally, P5c under coarse-graining by a ∈ {1,…,8} levels: θ invariant to
**1e-10** while the per-level slope ln n moves by **8×**.

**P6 — the residue is not discrete (IDENTITY; decisive against a map claim).**
M-B with (q1, q2) = (2, 2π) gives crossover exponent 1 − 1/π = **0.68169**, and an
M-A germ with p = 2 + √2 gives β/k = 1/√2 = **0.70711**, both within their leg's
tolerance. If either is a rational with small denominator to the measured
precision, consequence 3 is wrong.

**P7 — the kink is a projective wall (AT RISK).** In M-C hold β = n^{−1/2} and
sweep γ so that x = nβ²γ crosses 1. Predict:

- the measured θ(γ) tracks **min(1, ln n/(−ln β²γ))** to **±0.01** outside a 5%
  neighbourhood of the crossing, with the min emerging from the exact sum rather
  than being imposed;
- the crossing located from the two branches sits at **x = 1.000 ± 0.005**;
- under coarse-graining by *a* levels the located crossing stays at x = 1 to
  **1e-6** while the per-level slope moves by *a* — the kink is chart-invariant.

## 4. What would kill D7

- **P2 fails** (any weight ≠ 1 for a genuine observable) — the action is not by a
  common scalar, the residue is weighted-projective at best, and the ratios are not
  the invariants. This is the cleanest kill.
- **P3 fails** (σ₂/σ₁ not small) — the slope vectors do not span a ray, so there is
  no projective quotient and the count is wrong.
- **P5c fails** — the unification does not reach the case with no Φ, and the honest
  conclusion is D6's ratio plus a separate account for schemes, i.e. the
  heterogeneity the live question feared.
- **P7 fails** (the kink moves) — the non-analyticity is chart data, and the
  reconciliation's open item resolves the other way.
- **P2b fails in the direction of weight 1** — then §5's scope condition is
  spurious. Recorded as a way to be wrong that would *simplify* the claim, which is
  the kind this register is most likely to miss.

## 5. Scope, registered

- One control family per singularity throughout, except in P4 where violating that
  is the point.
- **Essential singularities remain outside**, as after D6 — no leading power, no
  finite log-slope, nothing here applies. The remainder does not narrow.
- **Finite-window contamination is the error budget.** G_pow is the asymptotic
  group; over a finite window corrections to scaling shift measured slopes by
  roughly the window's distance from the singular point. Every tolerance above is
  set by that and not by a target.
- The n − 1 count is claimed **generically**. M-A's five observables are
  algebraically related through the germ, so P3 tests that the measured vectors span
  a line — the dimension of the quotient — and not that five unrelated quantities
  were found.
- **Not tested here, and recorded so it cannot be backdated:** whether the residue's
  projective coordinates obey any *arithmetic* across composed singularities. That
  is [D5](../../questions/UNKNOWN-LAWS.md)'s question, it is now sharper (D5 asks for
  a sum rule on p; D7 says the object with the arithmetic would be a point of
  ℝP^{n−1}), and it is untouched by this experiment.
