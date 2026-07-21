# 2026-07-19 — Expansion: six fresh stones (S19–S24)

**Worked on:** new speculative questions, built on this session's scaffolding
**Change:** two new clusters in SPECULATIVE.md; synthesis stone-count updated

## Why now

These stones only became *articulable* after this session built the anchors: the
free-energy hub, the prediction-field frame, the validated ladder, and the
transfer-cliff finding ("transfer = shared-mechanism content"). Each new stone
attaches to one of those.

## Cluster I — Learning is the thermodynamics of prediction

- **S20 🟡 — inefficiency = non-predictive memory.** Building on Still et al.'s
  thermodynamics of prediction: a learner's regret/excess-loss may equal the
  information it keeps about the past that isn't predictive of the future
  ("nostalgia" as dissipation). *Tractable:* toy driven Markov model, numpy.
- **S21 🟡 — sloppiness = learnability = renormalizability.** One Fisher-spectrum
  fact (the hub's Hessian ∇²Φ is sloppy — few stiff directions) may explain
  learnability, renormalizability, and emergent simplicity together. Ladder level
  might = stiff-dimension count. *Tractable:* Fisher eigenvalue spectra, numpy;
  ties to S3.
- **S22 🟡 — the ladder is a renormalization scale.** Ladder level = renormalization
  depth (layers of irrelevant detail integrated out); L4 = RG fixed point, L2 =
  irrelevant operator that washes out (hence doesn't transfer). Self-referential
  like S18.

## Cluster J — The ladder as a dynamical process (climbing it is inference)

- **S19 🟡 — grokking is a climb up the ladder.** The memorization→generalization
  jump = an L2→L3 representation transition, which is *why* it's sudden (crossing
  the transfer cliff). Unifies grokking, S3, S13. *Test:* needs torch, but the
  invariance-across-subsets metric is cheap once a grokked model exists.
- **S23 🟡 — attention is the universal update.** Softmax attention = exp/Z = a
  Gibbs/Bayes reweighting = one step of entropic mirror descent; the transformer
  does amortized inference, attention-temperature = η. *Tractable:* show softmax
  attention ≡ Bayesian posterior over Gaussian memories, numpy.
- **S24 🔴 — the invariant is the minimal sufficient statistic** (and the rest is
  Landauer-erasable). Ties sufficiency, Landauer, and the prediction-field frame.

## Restraint owed

Three of these are numpy-cheap and would make good next restraint passes:
- **S23** (attention ≡ Bayesian reweighting) — a clean derivation+demo, like S1.
- **S21** (Fisher spectrum sloppiness vs. sample complexity) — extends the S3 tooling.
- **S20** (dissipation = non-predictive memory) — a toy Markov measurement.

The through-line getting stronger: **the hub (Φ) + the prediction field keep
generating the new stones**, which is itself weak evidence the center is real —
a productive center spawns questions, a decorative one doesn't.
