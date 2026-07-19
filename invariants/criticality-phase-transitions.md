# Criticality, phase transitions & universality

> **One-line claim:** Near a critical point, microscopically different systems
> share the *same* critical exponents; this "universality" is the deepest genuine
> cross-domain invariant we have.
> **Headline correspondence level:** L4 where the renormalization group applies;
> L1–L2 where "criticality" is invoked loosely (markets, cities, "edge of chaos").
> **Status:** developing

## Statement

At a continuous phase transition an order parameter vanishes and correlation
length ξ diverges as ξ ∝ |t|^−ν (t = reduced distance to the critical point).
Observables follow power laws with **critical exponents** (α, β, γ, δ, ν, η). The
renormalization group (RG) shows these exponents depend only on a few gross
features — dimensionality and symmetry of the order parameter — not on microscopic
details. Systems sharing those features form a **universality class** with
*identical* exponents.

## Manifestations by domain

| Domain | Critical phenomenon | Level | Quantitative signature | Ref |
|--------|---------------------|:-----:|------------------------|-----|
| Magnetism | Ising ferromagnet at T_c | anchor | 3D Ising: β ≈ 0.326, ν ≈ 0.630 | Onsager 1944 |
| Fluids | Liquid–gas critical point | L4 | *Same* exponents as 3D Ising | — |
| Percolation | Connectivity threshold | L4 | Percolation universality class | Stauffer 1979 |
| Epidemiology | Epidemic threshold R₀ = 1 | L3 | Percolation-like transition | — |
| Neuroscience | "Critical brain" / avalanches | L2–L3 | Branching σ ≈ 1; exponents debated | Beggs–Plenz 2003 |
| Finance | Market crashes as critical points | L1–L2 | Claimed log-periodic precursors; contested | Sornette 2003 |

## Shared mechanism

**The RG is the mechanism, and it is a genuine L4 story where it applies.** The
liquid–gas critical point and the 3D Ising magnet share critical exponents *to
measured precision* despite having nothing microscopically in common — because RG
flow carries both to the same fixed point. This is arguably the single strongest
demonstration that a cross-domain invariant can be *real and provable* rather than
metaphorical: the coincidence of exponents is predicted, then measured, then
confirmed.

The danger is **universality inflation**: applying the word to systems where no
RG argument exists. "The brain operates at criticality" and "markets are critical"
are *hypotheses at L2 at best* — sometimes with suggestive exponents, rarely with
a demonstrated universality class. Keep the L4 core (equilibrium critical
phenomena) sharply separated from the L1–L2 borrowings.

## Quantitative signature

The critical exponents and, decisively, **data collapse**: rescaling different
systems' data by powers of |t| should collapse them onto one universal curve.
Shared exponents *and* shared scaling function = same class. Shared qualitative
"tipping-point" behavior with unmatched exponents = not (yet) the same class.

## Boundary conditions / where it breaks

- Below the upper critical dimension, mean-field exponents fail; above it, they
  hold. Dimension matters.
- Finite systems round off the divergence — real "criticality" is approximate.
- Self-organized criticality (SOC) claims that some systems *tune themselves* to
  the critical point; whether SOC exponents form true universality classes across
  sandpiles/avalanches/earthquakes is genuinely open.

## Evidence for

- Liquid–gas ≡ Ising exponents: independent systems, identical numbers.
- Data collapse works quantitatively in equilibrium critical phenomena.

## Evidence against / competing explanations

- Neuronal-avalanche and market "criticality" often lack the exponent agreement
  and the RG argument; subsampling artifacts can fake criticality signatures.

## Open questions

- Is SOC (sandpiles, neuronal avalanches, earthquakes, forest fires) one
  universality class or several convergent mechanisms?
  (→ [`questions/OPEN-QUESTIONS.md`](../questions/OPEN-QUESTIONS.md) Q2)
- Do ML "neural scaling laws" reflect a statistical-physics criticality, or a
  different (approximation-theoretic) origin?
  (→ Q4; cross-link [`scaling-allometry.md`](./scaling-allometry.md))

## References

- Onsager 1944 — Crystal statistics (exact 2D Ising)
- Wilson 1971 — Renormalization group and critical phenomena
- Stanley 1971 — *Introduction to Phase Transitions and Critical Phenomena*
- Sornette 2003 — *Why Stock Markets Crash* (contested application)
