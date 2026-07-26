# Noise thresholds (capacity, error catastrophe, fault tolerance)

> **One-line claim:** The sharp noise level above which information can no longer be
> recovered — Shannon capacity, Eigen's error catastrophe, the quantum
> fault-tolerance threshold — is **one kind of object with three degeneracy
> orders**, not one law. Each domain has a genuine sharp threshold with a named
> mechanism (L3 within domain); the cross-domain *identity* is L1, because the
> required-redundancy exponent varies **within** domains as much as across them.
> **Headline correspondence level:** L2–L3 for the taxonomy; **L1 for "one
> threshold"** (retired).
> **Status:** developing ✓tested ([S5](../experiments/S5-noise-thresholds/))
> **Floor:** **3 + 4?** — splits (tested, [S5](../experiments/S5-noise-thresholds/)): types M and S are floor 3; **type R is not a Φ fact at all** — the scheme-layer candidate ([FLOORS §4](./FLOORS.md))

## Statement

Domain-neutral object: a critical noise level p_c separating a recoverable
(information-preserving) phase from a lost phase, with required resource per
protected bit N(p) ~ (p_c − p)^(−α) as p → p_c.

**The exponent α is not a property of the domain. It is the order at which the
prediction field degenerates at the threshold** — measurable, before any capacity
is computed, as the order of vanishing of the χ²-divergence between the two
conditional output laws (verified to 0.0015 across four channels).

| Type | Degeneracy at p_c | α | Instances |
|------|-------------------|---|-----------|
| **M** | the two conditional laws **merge smoothly** — first order cancels identically, leaving the Fisher quadratic form, so α = 2 is *forced* | **2** | BSC (2.0000), binary-input AWGN (1.9985), quasispecies + majority repair (2.035) |
| **S** | the laws stay distinguishable but the **informative support loses mass**; mass is a linear functional | **1** | BEC (1.0000), Z-channel (1.0000) |
| **R** | not a capacity zero at all — an **unstable fixed point of a decoder recursion** p → A·p^(t+1); α is an RG eigenvalue ratio | **ln n₀ / ln(t+1)** | concatenated codes: 2.2621 (n₀=23,t=3), 2.3223 (5,1), 2.8078 (7,1), 3.1704 (9,1) — all to 1.6e-4 |

Type M members also share the *constant*: C/χ²_sym = 1/(8 ln 2) for both BSC and
BI-AWGN.

## Manifestations by domain

- **CS, coding theory** — Shannon channel capacity; rate below capacity ⇒
  recoverable. **Anchor.** Supplies *both* type M (BSC, BI-AWGN) and type S (BEC,
  Z-channel), which is the single fact that kills the one-exponent reading.
- **Biology, molecular evolution** — Eigen's error catastrophe. L3 within domain.
  But the bare quasispecies has **no redundancy knob**: every site is functional,
  so N per protected bit ≡ 1 and the threshold sits at ln σ/L, moving with genome
  length rather than at a fixed p_c. Verified from exact class dynamics:
  L·μ_c = ln σ to within 0.25% at L = 400. **The error catastrophe is the zero-redundancy
  corner of the coding picture**, not a separate law. Add a decoder (majority
  repair across r copies — gene conversion / polyploid repair) and the threshold
  moves to μ = ½ with r_min ∝ δ^(−2): type M.
- **Quantum computing** — the fault-tolerance threshold theorem. L3 within domain,
  but type R: the exponent describes the *concatenation scheme*, not fault
  tolerance as such (constant-overhead LDPC constructions achieve O(1) overhead
  below threshold).
- **Chemistry/development** — kinetic proofreading error rates. L2, untested here.

## Mechanism

For types M and S the threshold is a **singularity of the prediction field**: the
point where the Fisher information the channel carries about the message develops a
null direction (M) or where the informative event's probability vanishes (S). Both
are faces of Φ's singular set already identified by
[S25(K)](../derivations/S25-control-split.md) — null Fisher directions and
supports — and they carry different exponents, which is exactly why they cannot be
one law. Type R is **not** a Φ-fact: it is a property of a decoder's flow, and is
the leading candidate for a fourth floor of the
[tower](../derivations/symmetry-sector.md).

## Boundary conditions

- Verified at degeneracy orders 1 and 2 only. A family whose Fisher form *also*
  vanishes at the threshold would give α = 4; no such case exhibited.
- All channels tested are binary-input and memoryless.
- The biology leg's decoder is a repetition code with majority repair — the crudest
  code available — in a deterministic (infinite-population), single-peak,
  no-epistasis, no-recombination model. μ > ½ is outside the model.
- The fault-tolerance leg is arithmetic on the standard concatenation recursion,
  not a simulated noisy circuit.

## Where the coding gap went

Near a type-M threshold the crudest code (repetition + majority) and the optimal
code share the exponent and differ by a **constant** (r_min/(1/C) ≈ 3.8, flat in
the gap), because both are governed by the same Chernoff/KL quadratic.
**Exponent = geometry of the threshold; code quality = prefactor.**

## Why it's here

Speculative question **S5**, run 2026-07-25. Cross-links
[`entropy-information.md`](./entropy-information.md),
[`criticality-phase-transitions.md`](./criticality-phase-transitions.md),
[`statistical-geometry.md`](./statistical-geometry.md). Refs: Shannon 1948;
Eigen 1971; Aharonov–Ben-Or 1997; Gottesman 2013.
