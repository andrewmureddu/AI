# Statistical geometry & curvature at criticality

> **One-line claim:** The Fisher information metric — natural gradient in ML,
> Ruppeiner metric in thermodynamics, Fubini–Study metric in quantum mechanics — is
> one geometry, and its scalar curvature diverges at phase transitions everywhere.
> **Headline correspondence level:** L3 candidate (the metric is genuinely shared;
> the curvature-at-criticality claim spans it). *(seed — speculative)*
> **Status:** developing — *first evidence in* ([experiment](../experiments/S3-fisher-geometry/))

## Statement

A family of probability distributions carries the Fisher information metric.
Domain-neutral object: this metric and its scalar curvature R, whose blow-up marks
loss of distinguishability / diverging correlation volume.

## Manifestations by domain (seed)

- Statistics/ML: Fisher metric = natural-gradient geometry (Amari). anchor.
- Thermodynamics: Ruppeiner metric; R diverges at critical points, R ~ correlation
  volume. L3.
- Quantum: Fubini–Study metric; fidelity susceptibility flags quantum phase
  transitions. L3.

## Why it's here / to develop

Speculative question **S3**: does curvature-blowup predict transitions in *learning
trajectories, fitness landscapes, and markets*, not just thermodynamics? Concrete
test: Fisher curvature should spike at an ML grokking/phase transition. Falsifier:
it doesn't. Refs: Amari 1985; Ruppeiner 1995; Provost–Vallee (quantum metric).

## Evidence so far (2026-07-19)

First test in [`../experiments/S3-fisher-geometry/`](../experiments/S3-fisher-geometry/)
(pure numpy, reproducible):

- **Physics leg confirmed exactly.** Mean-field Ising Fisher information
  (χ = Var(M)/T) diverges at T = 1.000 = T_c.
- **Learning leg confirmed on double descent.** In ridgeless random-feature
  regression the inverse-Fisher scale 1/σ_min² blows up at **the same** capacity
  P/N = 1.000 as the test-error peak — the generalization catastrophe *is* the
  Fisher matrix going singular.

This lifts the entry from `seed` to `developing`: same computable geometric object,
same signature, two domains. **Not yet L3** — this is coincidence with a shared
object (strong L2), not a proven common mechanism. Still open: the full Riemann
scalar-curvature version, and the *grokking*-specific transition (needs torch).
