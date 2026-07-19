# Invariants catalog

The master list of candidate cross-domain invariants. Each links to its own file.
"Level" is the **headline correspondence level** currently defended in the entry
(see [`../METHODOLOGY.md`](../METHODOLOGY.md) for the L0–L4 ladder). Levels and
statuses are provisional and change as entries are worked.

To add one: copy [`_TEMPLATE.md`](./_TEMPLATE.md), fill it in, add a row here and a
column in [`../domains/README.md`](../domains/README.md). See
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## Catalog

| # | Invariant | Core object | Level | Status | Notes |
|--:|-----------|-------------|:-----:|--------|-------|
| 1 | [Power laws / scale-free](./power-laws.md) | P(x) ∝ x^−α | L2 (L3 per-mechanism) | developing | Several mechanisms hide under one shape |
| 2 | [Conservation & Noether](./conservation-noether.md) | symmetry ↔ conserved current | L4 (phys) / L2 (else) | developing | Separates symmetry-laws from bookkeeping |
| 3 | [Entropy & information](./entropy-information.md) | −Σ p log p ; MaxEnt | L3 (L2 downstream) | developing | Predicts vs. re-describes |
| 4 | [Diffusion & random walks](./diffusion-random-walks.md) | ∂u/∂t = D∇²u ; CLT | L3–L4 | developing | CLT *forces* the class |
| 5 | [Criticality & universality](./criticality-phase-transitions.md) | RG fixed point; critical exponents | L4 (core) / L1–L2 (loose) | developing | The deepest genuine case |
| 6 | [Feedback & control](./feedback-control.md) | feedback loop; stability criterion | L2–L3 | seed | — |
| 7 | [Optimization & variational](./optimization-variational.md) | argmin of functional; EL/KKT | L1–L2 | seed | Teleology risk |
| 8 | [Networks & percolation](./networks-percolation.md) | giant-component transition | L3 / L2 | seed | Percolation = a universality class |
| 9 | [Scaling & allometry](./scaling-allometry.md) | Y ∝ M^b | L2 (L3 contested) | seed | Key open case (WBE) |
| 10 | [Symmetry breaking](./symmetry-breaking.md) | G → H, order parameter | L4 (phys) / L2–L3 | seed | — |
| 11 | [Fractals & self-similarity](./self-similarity-fractals.md) | fractal dim D ; Hurst H | L2 (L3 mechanistic) | seed | — |
| 12 | [Selection & replicator](./selection-replicator.md) | ẋ_i = x_i(f_i−f̄) ; Price eq. | L2–L3 | seed | Replicator ≡ mult.-weights |
| 13 | [Emergence & renormalization](./emergence-renormalization.md) | coarse-graining; relevant ops | L4 (RG) / L1 (loose) | seed | The meta-invariant |
| 14 | [Trade-offs & Pareto](./tradeoffs-pareto.md) | Pareto frontier | L1–L2 | seed | Maybe a corollary of #7 |
| 15 | [Duality & conjugates](./duality.md) | Fourier/Legendre transform | L2–L3 | seed | Legendre links thermo ↔ convex opt |
| 16 | [Information bottleneck](./information-bottleneck.md) | rate–distortion / IB curve | L2–L3 | seed | Related to #3, #14 |

## Reading the levels honestly

The interesting entries are the ones that span the ladder: **#2 (Noether)**,
**#4 (diffusion)**, and **#5 (criticality)** each have a genuine L4 core *and* a
soft L1–L2 fringe where the term gets over-applied. A large part of the research
is drawing that internal line correctly, not just assigning one number.
