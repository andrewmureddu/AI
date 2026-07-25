# Spectral gap (mixing, robustness, synchronization, consensus)

> **One-line claim:** The second eigenvalue of a system's operator governs how fast
> it mixes, how robustly it stays connected, how quickly it reaches consensus, and
> whether it synchronizes — the same number across all four.
> **Headline correspondence level:** L3 candidate (one operator invariant, many
> readouts). *(seed — speculative)*
> **Status:** seed
> **Floor:** **3** (Φ-singular) — **predicted, never tested**: gap-closure *is* the ∇²Φ degeneracy ([P-A](./FLOORS.md))

## Statement

For a Markov/Laplacian operator, the spectral gap (1 − second eigenvalue, or the
Fiedler value λ₂ of the graph Laplacian) sets the slowest relaxation mode.
Domain-neutral object: the spectral gap and the time/threshold scales it controls.

## Manifestations by domain (seed)

- CS: MCMC mixing time ~ 1/gap; expander graphs; PageRank convergence. L3.
- Physics: relaxation time to equilibrium ~ 1/gap. L3.
- Networks: algebraic connectivity (Fiedler) = robustness to disconnection. L3.
- Multi-agent/social: consensus convergence rate = λ₂. L2–L3.
- Neuro/physics: Kuramoto synchronization threshold tied to spectrum. L2.

## Why it's here / to develop

Underlies robustness/mixing/consensus/sync questions. The portable prediction: one
measured gap predicts mixing time, consensus speed, and sync threshold together.
Falsifier: a system where these decouple from the gap. Cross-links
`networks-percolation.md`. Refs: Fiedler 1973; Levin–Peres; Chung (spectral graph).
