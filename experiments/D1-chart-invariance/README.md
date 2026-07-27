# D1 — the chart law: two integers classify floor 3 (result)

**Question ([D1](../../questions/UNKNOWN-LAWS.md)):** [S5](../S5-noise-thresholds/)
and [S7](../S7-critical-slowing/) each measured one relation that transferred
across domains and a set of exponents that did not, and both filed the exponent
spread as a negative result — "domain-specific." Is that reading right, or is a
bare exponent simply not a property of the singularity?

**Status: the chart claim holds, cleanly and in the strong form. The formula that
carries the classification is *not* new, and a third of the evidence for it is
identity rather than measurement — both declared in advance. One registered
direction was refuted, and the mechanism behind it survived quantitatively.**

Run it: `python3 run.py` (numpy only, ~9 min, deterministic — seed 20260726).
Raw output: [`verdict.json`](./verdict.json). Registered in advance:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## The claim

A floor-3 singularity is approached along whatever control parameter ε the domain
happens to supply. But ε is a coordinate choice — ε′ = ε^a describes the same
singularity — so every exponent measured against it divides by a. Write λ(ε) for
the softest Hessian eigenvalue, λ ~ ε^k. Then the singularity carries **two**
numbers:

```
   k = chart order       how fast it is approached in the domain's own coordinate  -> GAUGE
   p = degeneracy order  order of the first non-vanishing anharmonic term of Phi   -> INVARIANT
```

and the noise-rounding crossover, re-charted against λ, is
**λ_c ~ D^{(p−2)/p}** — no domain label, no free exponent.

## Design

Five systems, all one-dimensional gradient dynamics with additive noise, differing
in *k*, in *p*, in the anharmonic coefficient *g*, and in field.

| Leg | Field | Model | k | p | model class |
|---|---|---|:--:|:--:|---|
| A | ecology / dyn. sys. | saddle-node fold | ½ | 3 | exactly cubic |
| B | epidemiology | SIS at R₀ = 1 | 1 | 3 | exactly cubic |
| C | physics | mean-field Ising | 1 | 4 | **all orders** |
| D | physics | Blume–Capel, tricritical line | 1 | 6 | **all orders** |
| E | machine learning | least squares at the MP edge | 2 | ∞ | exactly quadratic |

Leg D runs along a ≡ 2e^{−Δ/T}/(1+2e^{−Δ/T}) = ⅓, where the quartic coefficient
vanishes identically. Confirmed numerically: c₄ = **1.0e-10** against c₆ =
**9.876e-3**, and the Ising leg's c₄ = **3.793e-2** matches 1/(12T³) exactly.

---

## Results

### The classification (P1)

| Leg | p | measured λ-chart exponent | predicted (p−2)/p | status |
|---|:--:|:--:|:--:|---|
| A fold | 3 | **0.33333** (resid 3e-15) | 0.3333 | identity — estimator check |
| B SIS | 3 | **0.33333** (resid 4e-15) | 0.3333 | identity — estimator check |
| **C Ising** | 4 | **0.4961** | 0.5000 | **at risk — passes** |
| **D Blume–Capel** | 6 | **0.6635** | 0.6667 | **at risk — passes** |

The two full models — carrying every higher order, where the dimensional argument
does *not* apply — land within 0.004 and 0.003 of a parameter-free prediction.
Both undershoot slightly (0.8% and 0.5%), consistently, which is what
higher-order contamination should do.

### *k* is removable — the result that matters (P2)

A and B are a fold in population dynamics and a threshold in epidemiology. Their
chart orders differ by 2× and their anharmonic coefficients by 3×:

```
   bare chart:   A = 0.6667      B = 0.3333      <- differ by exactly 2x
   lambda chart: A = 0.33333     B = 0.33333     <- identical to 5 decimals
```

And *g* enters where the claim says it should — the amplitude, not the exponent.
The measured prefactor ratio λ_c(B)/λ_c(A) = **2.0801 at every one of the nine
noise scales**, against (g_B/g_A)^{2/p} = 3^{2/3} = **2.0801**.

### The bare chart actively mis-classifies (P3)

Bare exponents: A = 0.667, B = 0.333, C = 0.499, D = 0.664.

> **In the domain's own coordinate, the fold (p = 3) and the tricritical point
> (p = 6) agree to three decimals, while the fold and the SIS epidemic — the same
> degeneracy — differ by a factor of two.** The bare chart does not merely lose
> the classification; it reports the exact opposite of it.

This is what S5 and S7 were doing when they concluded the exponents were
domain-specific. Identity-derived, so not evidence — but it is the point.

### Contour- and coordinate-independence (P4, P5)

Threshold spreads across |R−1| ∈ {0.05, 0.10, 0.20}: A **0.0000**, B **0.0000**,
C **0.0031**, D **0.0001** — all inside the registered 0.03, including the two
at-risk legs where different contours probe different amounts of contamination.

Under explicit reparameterization ε′ = ε^a for a ∈ {½, 2, 3}, the bare exponent
moves by exactly a (A: 0.333 → 1.333 → 2.000) while the **λ-chart exponent does
not move at all** — 0.3333 and 0.4961 unchanged to four decimals in every case.

### Controls (P6, P7)

The exactly quadratic well shows **max |R−1| = 4.4e-16** over 63 (λ, D) points:
the estimator does not manufacture crossovers. The MP-edge chart order fits
**k = 2.091** against a predicted 2.0 — inside the registered ±0.1, but only
just, and finite-N limited (measured λ_min tracks (1−√γ)² to ≤1% down to 0.0013).

τ·λ = **1.005 / 0.987 / 0.935 / 0.997** across the four legs, extending
[S7](../S7-critical-slowing/)'s three-domain collapse to epidemiology and to a
tricritical point it was never tested on.

### P8 — registered direction refuted, mechanism confirmed

Moving off the tricritical line by δa reinstates a quartic term and should produce
a crossover between p = 6 and p = 4 behaviour. It does, and the registered
*condition* — quartic wins once λ ≳ (c₆/c₄)·D — is correct. **The registered
translation of it into a direction is backwards.** I wrote that the p = 6 window
would be the small-D end; it is the large-D end:

| δa | slope at low D | slope at high D | D_crossover |
|---|:--:|:--:|:--:|
| 0 | 0.666 | 0.635 | — (sextic throughout) |
| 1e-4 | 0.606 | 0.633 | below range |
| 3e-4 | 0.553 | 0.630 | 1.61e-8 |
| 1e-3 | 0.514 | 0.620 | 6.44e-7 |
| 3e-3 | 0.503 | 0.596 | 2.63e-5 |
| 1e-2 | 0.500 | 0.543 | above range |

The error was in composing two correct facts: λ_c itself falls with D, and it
falls *more slowly* (λ_c ~ D^{2/3}) than D does, so λ_c/D **grows** as the noise
shrinks and the quartic takes over at *small* D. Substituting λ_c into the
registered condition gives a scaling the pre-registration did not contain:

```
        D_x  ~  c4^3 / c6^2   ~   delta_a^3
```

Measured: **D_× ~ δa^3.211** over two decades of δa and three of D_×.
**This is post-hoc — derived after the first run exposed the direction error, not
registered** — and it is reported as a consistency check, not as a confirmed
prediction. It does have out-of-sample content: the fit predicts the two missing
entries above should fall at 3.9e-10 and 1.1e-3, i.e. just outside the swept range
at each end, which is exactly where they are absent.

---

## Verdict

**On the chart claim: confirmed, in the strong form.** *k* is gauge — removable by
inference across two fields (P2), and removable by direct manipulation (P5). Two
full models with every higher order present follow the *p*-formula (P1). The
bare-chart mis-classification is exact and inverted (P3).

**On novelty — the part that must not be inflated.** Graded on the
[novelty ladder](../../questions/UNKNOWN-LAWS.md#2-the-novelty-ladder):

- **The formula λ_c ~ D^{(p−2)/p} is N0–N1.** The pre-registration flagged the
  Ginzburg criterion as the nearest miss and the flag was right: this is that
  calculation, done for general *p* instead of the quartic case. Worse, §4
  declared in advance that within a truncated normal form it is *forced* by
  dimensional analysis — legs A and B could not have come out otherwise, and are
  reported as estimator checks rather than evidence.
- **The two-integer classification of floor 3 is N2, at L2–L3.** What is not in
  the literature this borrows from is the cross-domain claim: that the exponent
  spreads S5 and S7 measured are a chart artifact, that floor 3 stratifies by *p*
  rather than by domain, and that one of the two numbers is removable. The
  fields these legs come from have no convention fixing the chart, which is
  precisely why they reported the coordinate as though it were the physics.

**What it does to three existing results.** S7's τ·λ = 1 is the statement that the
relaxation exponent is −1 in the λ chart in every domain — the domain-dependence
lived entirely in ε ↦ λ, and P7 extends it to two more fields. S5's "α = the order
of vanishing of χ²_sym" is the same re-charting move made in a different
coordinate. [P-A](../PA-spectral-gap/)'s directional finding is the statement that
λ must be taken from the trajectory free energy when the potential's Hessian is
the wrong chart. None of the three was built from D1, and D1 was built from the
residue of two of them.

**What it does to the fourth-floor question.** [FLOORS.md](../../invariants/FLOORS.md)
§4 found four things refusing the tower with one shared signature: a log-ratio,
log(multiplicity) over log(rescaling). The chart order is
k = d ln λ / d ln ε — that signature exactly. P5 shows *k* is removable by a
coordinate change. If the identification holds, the scheme layer is not a fourth
floor but the tower's **gauge group**, and the map's standing P0 dissolves rather
than resolves. That is [D2](../../questions/UNKNOWN-LAWS.md), unworked; this
experiment supplies the removability half only.

---

## Boundaries

- **One-dimensional gradient systems with additive noise.** Registered in advance
  and not exceeded. Multiplicative noise, state-dependent diffusion, spatial
  extension and genuine barrier crossing are all untested here.
- **Only degeneracy-type singularities.** Support-type (S5's type S) and essential
  singularities have no *p* at all and were excluded by construction — that is
  [D6](../../questions/UNKNOWN-LAWS.md), not this. So "floor 3 is classified by
  *p*" is established for the part of floor 3 where Φ has a Taylor expansion, which
  is not all of it.
- **Odd *p* never reaches a well-confined regime.** For p = 3 the anharmonic term
  *is* the barrier, so rounding and metastable escape are the same event and the
  well depth at crossover is a fixed multiple of D. Registered in advance; legs A
  and B agree with each other but do not probe a regime with a barrier.
- **Two of four P1 legs are identities**, by declaration. The at-risk evidence is
  two full models, both from physics. A full model from outside physics is the
  obvious next leg and is missing.
- **The p = ∞ control is trivially harmonic.** It shows the estimator is clean; it
  does not show anything about learning.
- **MP-edge k = 2.091** passes its registered tolerance by 0.009. Treat as
  consistent with 2, not as a precise measurement.
- **P8's δa³ law is post-hoc.** It has not been pre-registered and must be
  re-run against a registered prediction before it counts as anything.
