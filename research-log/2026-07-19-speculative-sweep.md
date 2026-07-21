# 2026-07-19 — Speculative sweep (AI-native bridges)

**Worked on:** new speculative question tier; 6 new candidate objects
**Change:** added `questions/SPECULATIVE.md` (12 questions) + invariants #17–22

## What I did

Ran a deliberately looser, exploratory pass to "map the environment" — generating
cross-domain questions organized by **shared mathematical object** rather than by
domain. Wrote [`../questions/SPECULATIVE.md`](../questions/SPECULATIVE.md): 12
questions (S1–S12) in six clusters, each tagged 🟢 established / 🟡 plausible /
🔴 wild, each with a concrete falsifier.

Six objects the sweep surfaced now have seed entries (#17–22): the universal update
(mirror descent), optimal transport (Wasserstein gradient flow), spectral gap,
statistical geometry (Fisher/Ruppeiner/Fubini–Study), noise thresholds, and
critical slowing down. Catalog and the domain matrix updated with a speculative
tier.

## What the "AI-native" framing actually bought us

The honest mechanism (documented in SPECULATIVE.md): the edge is not insight, it's
**breadth across notation barriers** — recognizing the *same* object under
different disciplinary names. The strongest catches:

- **S1 / #17** — replicator dynamics = multiplicative weights = Bayesian update =
  Boltzmann relaxation, all as entropic mirror descent. If true, learning-rate =
  temperature = mutation rate (S2). This is the highest-value new thread; the math
  bridge is established, only the *reach* is open.
- **S4 / #18** — JKO makes diffusion a gradient flow of entropy in Wasserstein
  space; possibly the one governing equation for "any evolving distribution"
  (markets, GANs, development).
- **S3 / #20** — one metric (Fisher) is natural gradient, Ruppeiner thermo metric,
  and quantum Fubini–Study; curvature-blowup as a universal transition detector.
  Has a crisp, cheap test: Fisher curvature should spike at an ML grokking event.

## Decisions / level changes

- New entries are `seed·spec` — speculative seeds. No promotions. Levels in the
  matrix's speculative rows are explicitly "hypotheses squared."
- Kept the rigorous tier (`OPEN-QUESTIONS.md`) and the speculative tier separate on
  purpose, with a stated graduation path: a stone that survives its falsifier moves
  up to the rigorous agenda and its object gets a full entry.

## Interpretation note

Read "map the environment" as *the intellectual terrain of cross-domain
invariants* (the knowledge landscape), not the runtime/sandbox. Flagged to the
user in case they meant otherwise.

## Next (cheapest high-signal tests)

- **S3**: instrument a small model through a known grokking transition; check
  whether Fisher-metric scalar curvature spikes. Cheap, decisive, and would anchor
  #20 immediately.
- **S1**: write the explicit dictionary mapping replicator ↔ MW ↔ Bayes ↔ Gibbs
  (the Bregman divergence + step size for each). Pure derivation, no data needed.
- **S7**: run lag-1 autocorrelation / variance on public training-loss curves
  before known collapses; test critical-slowing-down as an ML early warning.
