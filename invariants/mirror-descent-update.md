# The universal update (mirror descent / entropic ascent)

> **One-line claim:** Replicator dynamics, multiplicative-weights, exponentiated
> gradient, Bayesian updating, and relaxation to Boltzmann–Gibbs are all mirror
> descent on a KL/entropy regularizer — one update rule wearing many names.
> **Headline correspondence level:** L3 candidate (shared formal update) — the
> strongest speculative bridge in the catalog. *(seed — speculative)*
> **Status:** seed

## Statement

Mirror descent minimizes a loss plus a Bregman-divergence regularizer; with the
(negative) entropy as mirror map it becomes the exponential/multiplicative update
x_i ← x_i · exp(η · reward_i) / Z. Domain-neutral object: **entropic mirror
descent** and its continuous-time limit (a replicator/Fokker–Planck flow).

## Manifestations by domain (seed)

- Biology: replicator dynamics ẋ_i = x_i(f_i − f̄) — continuous-time MW. L3.
- CS/ML: multiplicative weights, Hedge, exponentiated gradient — anchor.
- Inference: Bayesian update is a multiplicative reweighting by likelihood. L3.
- Physics: relaxation to Boltzmann–Gibbs = entropy-regularized equilibrium. L3.
- Economics: fictitious play / evolutionary game dynamics. L2–L3.

## Why it's here / to develop

This is the spine of speculative question **S1** (`../questions/SPECULATIVE.md`).
If it holds, "adaptation" everywhere is one descent on a free energy, and the
learning rate = temperature = mutation rate (S2). Falsifier: an adaptive update
provably not expressible as mirror descent on any Bregman divergence. Refs:
Beck–Teboulle 2003; Nemirovski–Yudin; Hofbauer–Sigmund; Amari (natural gradient).
