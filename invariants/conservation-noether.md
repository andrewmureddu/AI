# Conservation laws & Noether's theorem

> **One-line claim:** Every differentiable symmetry of a system's action yields a
> conserved quantity; "conservation laws" elsewhere are conserved iff they trace
> to such a symmetry (or to an exact bookkeeping identity).
> **Headline correspondence level:** L4 within physics (Noether); L2–L3 for the
> economic/probabilistic analogues, sharply demarcated below.
> **Status:** developing
> **Floor:** **1** (symmetry-constituted) — charges are the natural parameters of long-time ensembles. *Bookkeeping identities are not floor 1* — see [FLOORS §4](./FLOORS.md)
> **⟳ Corrected 2026-07-29 ([D7](../derivations/D7-composition-lens.md)):** the rule
> is conservation **and additivity**, not conservation alone. A conserved but
> non-additive quantity cannot occupy a natural-parameter slot, because the
> ensemble family would not be closed under composition — L² is exactly as
> conserved as L_z and never carries a chemical potential. In statistics this is
> Koopman–Pitman–Darmois; measured in
> [D7 leg C](../experiments/D7-composition-lens/) at ≤3.2e-14 for additive
> statistics against ≥8.8e-4 for every non-additive one. The additivity half comes
> from **floor 0**, so this entry's floor sits on top of a composition law rather
> than at the bottom of the tower.

## Statement

Noether's theorem (1918): for a system with action S = ∫ L dt, every continuous
symmetry of L corresponds to a conserved current. Time-translation → energy;
space-translation → momentum; rotation → angular momentum; internal U(1) phase →
charge. The domain-neutral object is the pairing **symmetry ↔ conserved quantity**.

## Manifestations by domain

| Domain | "Conserved" quantity | Underlying symmetry? | Level | Ref |
|--------|----------------------|----------------------|:-----:|-----|
| Classical/quantum physics | Energy, momentum, charge | Yes — exact, by Noether | L4 | Noether 1918 |
| Probability | Total probability = 1 | Yes — unitarity / normalization is a symmetry of the evolution | L3 | — |
| Fluid/EM | Mass, charge continuity ∂ρ/∂t + ∇·J = 0 | Yes — same continuity structure | L3 | — |
| Accounting | Assets = Liabilities + Equity; double-entry | **No dynamical symmetry** — it's a *definitional identity* | L2 | Pacioli 1494 |
| Economics | "Conservation of value" in exchange | Contested / usually false | L1 | — |
| Ecology | Mass/energy budgets in food webs | Yes — physical conservation inherited | L3 | — |

## Shared mechanism

Two genuinely different things get called "conservation," and separating them is
the whole point of this entry:

1. **Symmetry-induced conservation (Noether).** A dynamical law with a continuous
   symmetry. This is the deep, L4 version. Its cross-domain reach is real but
   *only where an action principle and a symmetry actually exist* (physics, and
   by inheritance any physical subsystem — ecology's energy budgets, chemistry's
   mass balance).
2. **Bookkeeping identities.** Double-entry accounting, Kirchhoff's current law as
   a node constraint, "what goes in must come out" flow balance. These conserve by
   *definition/topology*, not by symmetry. That is an **L2** formal identity
   (the continuity-equation form) — powerful, but do not dress it in Noether's
   clothes.

The failure mode is treating (2) as if it were (1): claiming a conservation law
in economics *explains* something, when it is either a definitional identity or
simply false (value is created and destroyed).

## Quantitative signature

A conserved quantity Q with dQ/dt = 0 (closed system) or a continuity equation
∂ρ/∂t + ∇·J = 0 (local form). The signature of the *deep* version is that Q is
predicted by a specific symmetry group and its Noether current is computable.

## Boundary conditions / where it breaks

- Noether requires a differentiable action symmetry; dissipative/open systems
  break it (energy conservation fails locally, restored only globally).
- "Conservation of information" in black holes was an open problem precisely
  because the symmetry status was unclear.
- Economic "conservation" fails: value is not conserved under production or
  innovation.

## Evidence for

- Noether is a theorem, not an analogy — the strongest L4 anchor in the catalog.
- The continuity-equation form genuinely transfers technique across physics,
  chemistry, ecology, epidemiology (compartmental models are flow-balance).

## Evidence against / competing explanations

- The popular "conservation of X" in social science is usually an L1 metaphor or
  an L2 identity mislabeled as a physical law.

## Open questions

- Are there *bona fide* symmetry→conservation pairs outside physics? Candidate:
  gauge-theoretic formulations of economics (Malaney–Weinstein "gauge theory of
  economics"). Is that L2 formalism or does it yield a testable conserved current?
  (→ [`questions/OPEN-QUESTIONS.md`](../questions/OPEN-QUESTIONS.md) Q5)

## References

- Noether 1918 — Invariante Variationsprobleme
- Pacioli 1494 — *Summa de arithmetica* (double-entry)
- Baez & Fong 2013 — A Noether theorem for Markov processes
