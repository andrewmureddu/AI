# Optimal transport & Wasserstein gradient flow

> **One-line claim:** "How a distribution evolves" — in diffusion, matching
> markets, generative models, and development — may all be steepest descent of a
> free energy in the Wasserstein geometry of distributions.
> **Headline correspondence level:** L3 candidate (JKO is a theorem; cross-domain
> reach is the open part). *(seed — speculative)*
> **Status:** seed

## Statement

Optimal transport equips the space of probability distributions with the
Wasserstein metric. The Jordan–Kinderlehrer–Otto (JKO) theorem: the heat/diffusion
equation is the **gradient flow of entropy** in this metric. Domain-neutral object:
∂ρ/∂t = −∇_W F[ρ] — distributional dynamics as gradient descent of a functional F.

## Manifestations by domain (seed)

- Physics: diffusion / Fokker–Planck as Wasserstein gradient flow (JKO). anchor.
- Economics: Monge–Kantorovich optimal matching / assignment. L3.
- ML: Wasserstein GANs, diffusion models, distributional RL. L3.
- Biology: developmental / cell-fate trajectories as transport (Waddington). L2.

## Why it's here / to develop

Speculative question **S4**. The unifying claim: every "evolving distribution" is a
Wasserstein gradient flow of some free energy F; the domains differ only in F.
Falsifier: a genuinely non-gradient (curl-dominated) distributional flow. Cross-
links `diffusion-random-walks.md`. Refs: JKO 1998; Villani 2009; Otto 2001.
