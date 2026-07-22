# 2026-07-21 — Restraint: the RLCT charts the field's singularities (S25)

**Worked on:** new stone S25 — singular learning theory as the chart of the
prediction field where S3's Fisher metric degenerates
**Change:** S25 added and immediately tested; confirmed with registered
quantitative predictions; graduates the "what math maps the field" question from
discussion to measurement

## Why this one

S3 measured that the Fisher metric degenerates at transitions, which left a hole:
where the metric is singular, "effective dimension d/2" is undefined, so what
prices generalization there? Watanabe's singular learning theory answers with the
learning coefficient λ (real log canonical threshold): F_n = nL_n(w0) + λ log n,
λ = d/2 only for regular models, λ < d/2 at singularities, and Bayes
generalization ≈ λ/n. The registered weld: estimate λ at a measured singular
point and check that it — not parameter count — predicts generalization *and*
transfer.

## What I did

Three legs ([`../experiments/S25-rlct-singularity/`](../experiments/S25-rlct-singularity/)),
pure numpy, all predictions registered in the docstring before running:

- **Leg A (anchor):** free-energy-slope estimator (deterministic quadrature,
  sufficient statistics, n → 10⁶) on three exactly-solved models: regular y=wx
  (λ=½), singular y=abx (λ=½, d/2=1, multiplicity 2), singular y=w²x (λ=¼).
- **Leg B (the singular point):** Bayesian random-feature regression, D=20,
  P=2..60. Population Fisher rank = min(P,D) ⇒ model turns singular at P=D.
  Registered: λ(P) = min(P,D)/2 with a kink at P=D.
- **Leg C (transfer):** excess risk under anisotropic covariate shift across the
  same sweep — does it plateau with λ or grow with parameter count?

## What I found

- **Leg A: λ̂ = 0.492 / 0.508 / 0.248 vs theory 0.5 / 0.5 / 0.25.** The estimator
  cleanly separates λ from d/2 on singular models (M2 has twice M1's parameters,
  same λ). M2's multiplicity-2 −log log n term is visible in the raw slope.
- **Leg B: the kink is real and exact.** λ̂ rises ≈ P/2, then plateaus at
  10.00 ± 0.08 = D/2 for P ≥ 26 while d/2 marches to 30. n·(Bayes excess risk)
  ratio at P=60 vs P=20 is 0.97 (d/2 predicts 3).
- **Leg C: transfer ratio 0.97** — shift error plateaus with λ too.
- **Bonus finding:** λ̂ overshoots its asymptote only in a narrow window around
  P=D (max dev 1.39 at P=18 → 0.08 by P=26): the Fisher matrix is full-rank but
  nearly degenerate there, so log n asymptotics set in slowly. A finite-size
  critical crossover at the singular point itself — the same phenomenology S3
  measured. The chart is exact away from the critical point, blurred on it.

## Decisions / level changes (with reasons)

- S25 added to SPECULATIVE.md at 🟡 and restraint-passed same day: registered
  predictions all confirmed. The Fisher-degeneracy ↔ RLCT correspondence is L2
  (formal identity: rank of the metric = 2λ in this model class) with an L4-grade
  theorem behind it (Watanabe) that we verified numerically rather than assumed.
- Not promoted further because the tested singularities are the *simplest kind*
  (quadratic/rank-deficient, plus two 1–2 parameter analytic toys). The claim
  that λ charts *neural-network* singularities is untested here.

## Honest limits

Leg C's covariate shift is within-space reweighting, not the ladder's
cross-domain transfer; the supported claim is narrow — λ, not d, is the
complexity that prices error under distribution change. And Leg B's P<D
(misspecified) slopes are noisy, consistent with Watanabe's fluctuation term.

## Next

- The real prize: estimate λ̂ locally along a *training trajectory* of a small
  nonlinear network (grokking-adjacent) and test S11 (criticality-as-attractor):
  does training flow toward low-λ (more singular) regions?
- Connect to S21 (sloppiness): is the sloppy Fisher spectrum's effective cutoff
  the same count as 2λ?
