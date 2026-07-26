# D1 pre-registration — written before any measurement

Per [`questions/UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: the
prior-art note comes first, then the registered numbers, and **§4 marks which
predictions are analytic identities and which can actually come out wrong** — the
discipline [P-A](../PA-spectral-gap/) had to learn mid-flight when three of its
four readouts turned out to be one number by construction.

Nothing here is revised after the run. Results live in [`README.md`](./README.md).

---

## 0. Prior-art note (written first)

**What is old.** That critical exponents depend on the coordinate used to approach
the critical point is elementary. Physics fixes it by convention — exponents are
quoted against the reduced temperature t = (T−T_c)/T_c, and everyone knows quoting
them against T or 1/T would change them. Scaling relations (Rushbrooke, Widom,
Fisher, Josephson) are exactly the statement that certain exponent *combinations*
are convention-free. Catastrophe theory (Thom, Arnold) classifies degeneracies of
gradient systems by codimension; the A_k normal forms are the finite-*p* case of
this document's *p*. Noise-rounding of a mean-field transition is standard
(Ginzburg-criterion-adjacent). **None of that is claimed as new**, and §4 records
that within a *truncated* normal form the headline exponent is not merely known
but forced.

**What the above does not cover.** The systems this repo compares mostly have no
such convention, because they have no thermodynamic limit and no universality class
to hang one on: a decoder recursion, a queue at saturation, a least-squares fit at
the interpolation threshold, an SIS epidemic at R₀ = 1. In those fields the
exponent is quoted against whatever knob the discipline happens to turn, and is
then compared *across* disciplines as though it were intrinsic.
[S5](../S5-noise-thresholds/) and [S7](../S7-critical-slowing/) both did this and
both concluded "the exponents are domain-specific." The claim under test is that
this conclusion is an artifact of charts.

**Nearest miss found.** The Ginzburg criterion is this calculation for the Ising
case specifically, expressed as a condition on dimensionality rather than as a
chart-free exponent. If the general (p−2)/p statement is a known result in that
language, D1 drops to **N0 for the formula** and retains at most N1 for the
cross-domain reading. Recorded now so the outcome cannot be relabelled later.

---

## 1. The setup

A system relaxes in an effective potential Φ near a floor-3 singularity, driven by
noise of scale D:

```
        dy = −Φ'(y) dt + √(2D) dW ,      stationary density  ρ(y) ∝ e^{−Φ(y)/D}
```

Near the singular point, with y measured from the stable fixed point:

```
        Φ(y)  =  (λ/2) y²  +  g·y^p  +  (higher orders)
```

- **λ** — softest Hessian eigenvalue, vanishing at the singularity.
- **p** — the **degeneracy order**: order of the first non-vanishing anharmonic
  term. Read off the model's Taylor expansion; no measurement involved.
- **ε** — whatever control parameter the *domain* supplies; defines the **chart
  order** *k* via λ ~ ε^k.

Define the **rounding ratio** R(λ,D) = Var_measured·λ/D, which → 1 in the harmonic
limit, and locate λ_c(D) as the λ at which R falls to a threshold R\*.

## 2. The prediction

Balancing the anharmonic term against the noise at the thermal width √(D/λ):

```
        g·y_th^p / D  =  g·D^{p/2−1}·λ^{−p/2}  =  O(1)
    ⟹   λ_c  ~  D^{(p−2)/p}          ← no domain label, no free exponent
```

In the domain's own chart the same locus reads ε_c ~ D^{(p−2)/(pk)} — an exponent
that moves with the chart while the singularity does not.

## 3. The legs

| Leg | Field | Model | ε | **k** | **p** | model class |
|---|---|---|---|:--:|:--:|---|
| **A** | ecology / dyn. sys. | saddle-node fold, ẋ = −ε + x² | ε | **½** | **3** | exactly cubic |
| **B** | epidemiology | SIS, İ = βI(1−I) − γI on [0,1] | 1−γ/β | **1** | **3** | exactly cubic |
| **C** | physics | mean-field Ising, Φ(m) = m²/2 − T ln(2 cosh(m/T)) | T−T_c | **1** | **4** | **all orders** |
| **D** | physics | mean-field Blume–Capel on the tricritical line | T−T_t | **1** | **6** | **all orders** |
| **E** | machine learning | least-squares at the Marchenko–Pastur edge | 1−γ | **2** | **∞** | exactly quadratic |

Leg D runs along the line a ≡ 2e^{−Δ/T}/(1+2e^{−Δ/T}) = ⅓, on which the quartic
coefficient (a²/8 − a/24)/T³ vanishes **identically**, leaving the sextic as the
leading anharmonicity. Tricritical point: T_t = ⅓, Δ_t = ⅓·ln 4. The sextic
coefficient there is predicted to be 0.0750.

---

## 4. Identity vs. risk — the required disclosure

**This section exists because the headline scaling is, in part, forced.** Rescaling
y = √(D/λ)·ŷ in the *truncated* form Φ = λy²/2 + g y^p gives

```
        Φ/D  =  ŷ²/2 + u·ŷ^p ,      u ≡ g·D^{p/2−1}·λ^{−p/2}
```

so R depends on **u alone**, hence R = R\* fixes u, hence λ_c ∝ D^{(p−2)/p}
*exactly and for any threshold*. Therefore:

**Analytic identities. These cannot come out wrong and are NOT evidence:**

- λ_c ~ D^{(p−2)/p} **for legs A and B**, whose potentials are exactly cubic. They
  are included to verify the estimator and to demonstrate the chart effect — not to
  support the formula.
- Threshold-independence for A, B, E — changing R\* changes u\*, not the exponent.
- ε_c exponent = (λ_c exponent)/k. Arithmetic, given the chart map. **The
  bare-chart numbers in P3 are illustration, not evidence.**
- τ·λ = 1 for a purely harmonic well (leg E) — the OU solution.

**Genuinely at risk. These are the experiment:**

- **P1 (C and D only)** — whether **full** models, carrying every higher order,
  follow (p−2)/p at all. The u-scaling argument does not apply to them: leg C has
  m⁶, m⁸, … terms and leg D has m⁸, … , each contributing its own dimensionless
  group. Contamination could bend the exponent, and for leg D the quartic
  coefficient vanishes only *on* the line, so any numerical drift off it reintroduces
  p = 4.
- **P2** — whether *k* is removable across genuinely different models, tested where
  it can fail: A and B have different *k* (½ vs 1) *and* different anharmonic
  coefficients *g*.
- **P5** — reparameterization invariance under an explicit coordinate change
  applied to a full model (C), where λ(ε) is not an exact power law.
- **P6** — the null control. A purely quadratic well must show no crossover. If one
  appears, the estimator manufactures crossovers and nothing above is interpretable.
- **P8** — the off-line crossover prediction for leg D. Fully out-of-sample.

---

## 5. Registered predictions

**P1 — the classification (headline).** Fitted λ-chart crossover exponents within
**±0.05 absolute** of the parameter-free prediction:

| Leg | p | predicted (p−2)/p | status |
|---|:--:|:--:|---|
| A | 3 | **0.3333** | identity (estimator check) |
| B | 3 | **0.3333** | identity (estimator check) |
| C | 4 | **0.5000** | **at risk** — full model |
| D | 6 | **0.6667** | **at risk** — full model, c₄ = 0 only on the line |

**P2 — *k* is removable.** A (k = ½) and B (k = 1) agree in the λ chart within
**0.03 absolute** despite bare exponents differing by 2×, and despite different
anharmonic coefficients. Their λ_c *prefactors* differ as g^{2/p} = g^{2/3} —
registered as a check that g enters the amplitude and not the exponent.

**P3 — the bare chart mis-classifies (illustrative, identity-derived).**
ε_c ~ D^{(p−2)/(pk)} gives A = 0.667, B = 0.333, C = 0.500, D = 0.667. So **in the
bare chart A and D agree exactly (0.667) while A and B differ by 2×** — precisely
inverting the true classification (A = B ≠ D). Registered as the sharpest available
statement of what a chart does to a cross-domain exponent comparison. *Not
evidence*: it follows from P1 by division. Reported because it is what S5 and S7
actually did.

**P4 — threshold-independence.** Repeating with R\* ∈ {0.95, 0.90, 0.80} moves each
fitted exponent by **< 0.03**. Identity for A, B, E; **at risk for C and D**, where
different thresholds probe different distances from the singularity and therefore
different amounts of higher-order contamination.

**P5 — explicit reparameterization.** Re-chart legs A and C with ε′ = ε^a for
a ∈ {½, 2, 3}: bare exponent scales as (bare)/a to within **1%**; **λ-chart
exponent unchanged to within 0.01**.

> **Pre-run correction (caught at implementation, before any measurement, left
> on record rather than silently edited).** The direction above is wrong. Under
> ε′ = ε^a we have ε = ε′^{1/a}, so λ ~ ε′^{k/a} and k′ = k/a; the bare exponent
> (p−2)/(p k′) therefore **multiplies by a**, it does not divide. The code tests
> the corrected form. The substance of P5 is unaffected — the bare exponent moves
> by the factor a in some direction, the λ-chart exponent does not move at all —
> but the registered direction was stated backwards and that is now on the record
> alongside [S5](../S5-noise-thresholds/)'s.

**P6 — null control (leg E).** For the exactly quadratic well, R stays within
**1%** of 1 across the entire λ range at every D; no crossover exists to fit. The
MP-edge chart order is separately confirmed: fitted k = **2.0 ± 0.1** for
λ_min = (1−√γ)² against ε = 1−γ.

**P7 — τ·λ = 1 extends to two new fields.** Langevin autocorrelation times in the
harmonic regime give τ·λ = **1.0 ± 0.15** for A, B, C, D — extending
[S7](../S7-critical-slowing/)'s three-domain collapse to epidemiology and to a
tricritical (p = 6) point it was never tested on. Confirmatory, not new.

**P8 — the off-line crossover (exploratory, fully out-of-sample).** Moving off the
tricritical line by δa reintroduces a quartic term with coefficient
c₄ ≈ (a/8 − 1/24)·δa/T³ ≈ 0.9·δa. Predict the measured exponent crosses over from
**2/3 back to 1/2** once the quartic group exceeds the sextic one, i.e. once
c₄·D/λ² ≳ c₆·D²/λ³, i.e. **λ ≳ (c₆/c₄)·D**. At D = 10⁻⁴ and δa = 10⁻², that is
λ ≳ 8×10⁻³. Registered with the sign: **the exponent should fall, not rise**, and
the p = 6 window should be the *small*-λ end.

---

## 6. What would kill D1

- **P2 fails** — A and B disagree in the λ chart. The chart is not gauge, *k*
  carries information, and S5/S7's "domain-specific" reading was right.
- **P1 fails for C or D while holding for A and B** — the formula governs truncated
  normal forms only, so *p* classifies nothing about real models. This is the most
  likely partial outcome and would still be a result: it locates the classifier's
  absence.
- **P5 fails** — the λ-chart exponent moves under explicit reparameterization; the
  invariance claim is false as stated.
- **P4 fails for C or D** — the exponent depends on the contour, so there is no
  crossover exponent to classify with.
- **P6 fails** — the estimator manufactures crossovers; nothing is interpretable.

## 7. Registered scope

All legs are one-dimensional gradient systems with additive noise. D1 is being
tested where Φ has a Taylor expansion and the singularity is a **degeneracy**.
**Support-type singularities (S5's type S) and essential singularities have no *p*
and are excluded by construction** — they are
[D6](../../questions/UNKNOWN-LAWS.md), not this experiment. Multiplicative noise,
state-dependent diffusion, spatially extended systems, and genuine barrier crossing
(where [P-A](../PA-spectral-gap/) showed the potential's Hessian is the wrong
chart) are all outside. A result here says nothing about any of them.

One further scope note recorded in advance: for **odd *p*** the anharmonic term
*is* the barrier, so noise-rounding and metastable escape are the same event. At
the crossover the well depth is a fixed multiple of D regardless of *g*. Legs A and
B are therefore measuring a rounding scale that coincides with well-dissolution;
that is a property of odd degeneracies, not an artifact, but it means A and B do
not probe a well-confined regime and their agreement should not be read as evidence
that the formula holds where a barrier is absent.
