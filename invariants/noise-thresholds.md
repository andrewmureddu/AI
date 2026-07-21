# Noise thresholds (capacity, error catastrophe, fault tolerance)

> **One-line claim:** The sharp noise level above which information can no longer be
> recovered — Shannon capacity, Eigen's error catastrophe, the quantum
> fault-tolerance threshold — may be one redundancy-vs-noise transition.
> **Headline correspondence level:** L2–L3 candidate (each is a real sharp
> threshold; identity is the open question). *(seed — speculative)*
> **Status:** seed

## Statement

Domain-neutral object: a critical noise level p_c separating a recoverable
(information-preserving) phase from a lost phase, with a required-redundancy scaling
as p → p_c.

## Manifestations by domain (seed)

- CS coding theory: Shannon channel capacity; rate below capacity → recoverable.
  anchor.
- Biology: Eigen error catastrophe — above a mutation rate the genome's information
  dissolves (quasispecies). L3.
- Quantum computing: fault-tolerance threshold theorem — below an error rate,
  arbitrary computation survives. L3.
- Chemistry/development: kinetic proofreading error rates. L2.

## Why it's here / to develop

Speculative question **S5**. Test: does required redundancy scale with the same
exponent in (p_c − p) across domains? Falsifier: exponents differ. Cross-links
`entropy-information.md`, `criticality-phase-transitions.md`. Refs: Shannon 1948;
Eigen 1971; Aharonov–Ben-Or 1997.
