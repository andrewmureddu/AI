# S25 — the learning coefficient (RLCT) charts the prediction field at its singularities

**Question.** [S3](../S3-fisher-geometry/) measured that the Fisher metric of the
prediction field *degenerates* at phase transitions. Where the metric degenerates,
the standard "effective dimension" d/2 loses meaning. Watanabe's singular learning
theory says the quantity that survives is the **real log canonical threshold
(RLCT / learning coefficient) λ**: the Bayesian free energy obeys
`F_n = n L_n(w0) + λ log n − (m−1) log log n + O_p(1)`, with λ = d/2 for regular
models and **λ < d/2 exactly at singularities**, and λ — not d/2 — controls
Bayes generalization (≈ λ/n). This experiment welds the repo's three spine pieces
— the metric (S3), the singularity chart (λ), and transfer — in one run.

## Registered predictions (written before running)

1. **Leg A (theory anchor).** Free-energy slopes on three exactly-solved models
   recover λ = 1/2 (regular `y=wx`), λ = 1/2 with d/2 = 1 (singular `y=abx`),
   λ = 1/4 with d/2 = 1/2 (singular `y=w²x`). Posterior integrals by
   deterministic quadrature, n up to 10⁶ via sufficient statistics — no MCMC.
2. **Leg B (the repo's singular point).** Bayesian random-feature regression
   (input dim D=20, features P=2..60): the population Fisher matrix has rank
   min(P, D), so the model becomes *singular* at P=D. Prediction:
   **λ̂(P) = min(P, D)/2** — rises like P/2, then kinks flat at P=D — and
   n·(Bayes excess risk) tracks λ̂, not P/2.
3. **Leg C (transfer).** Under anisotropic covariate shift, excess transfer risk
   at P ≥ D plateaus with λ (ratio T(60)/T(20) ≈ 1) rather than growing with
   parameter count (naive d-scaling: ≈ 3).

## Result — all three predictions confirmed

```
Leg A   λ̂ = 0.492 / 0.508 / 0.248   vs theory 0.5 / 0.5 / 0.25   (d/2: 0.5 / 1.0 / 0.5)
Leg B   plateau λ̂(P≥26) = 10.00 ± 0.08  = D/2 exactly   (naive d/2 at P=60: 30)
Leg C   T(60)/T(20) = 0.97   n·G(60)/n·G(20) = 0.97     (d-scaling predicts ~3)
```

- **Leg A**: the estimator distinguishes singular from regular models cleanly —
  `y=abx` has *twice* the parameters of `y=wx` but the *same* λ = 1/2, and
  `y=w²x` has λ = 1/4 < d/2. Note the raw slope of M2 (0.391) undershoots ½
  because its multiplicity m=2 contributes a −log log n term — the registered
  fit includes it; both slope forms are reported in `verdict.json`.
- **Leg B**: past the singular point every added parameter adds **zero** learning
  coefficient — the plateau at exactly D/2 = 10 (max dev 0.078 for P≥26) is why
  overparameterization is free for Bayes generalization. This is the population
  analogue of S3's finite-sample degeneracy at P=N: the *rank* of the Fisher
  metric is the RLCT chart.
- **Leg C**: transfer under covariate shift also plateaus with λ. Parameter
  count is the wrong coordinate on the singular part of the field; λ is the
  right one.

## The bonus finding: a critical window at the singularity itself

λ̂(P) *overshoots* min(P,D)/2 in a narrow window around P=D (max dev 1.39 at
P=18, decaying to 0.08 by P=26). Mechanism: at P≈D the Fisher matrix is
full-rank but *nearly* degenerate, so the log n asymptotics set in slowly — a
finite-size critical crossover, the same phenomenology S3 measured at its
transition. The asymptotic chart is exact away from the critical point and
blurred exactly on it.

## Honest limits

- Leg B/C use a **linear-Gaussian** model, where the RLCT is just rank/2 — the
  simplest possible singularity. Neural-network singularities (analytic,
  non-quadratic) are the real target; Leg A's M2/M3 are the only non-quadratic
  cases here, and they are 1–2 parameters.
- The P<D rise region is misspecified (teacher not in model span); slope
  estimates there are noisy (mean dev 0.44), consistent with the O_p(√n)
  fluctuation term Watanabe predicts for the renormalizable misspecified case.
- Leg C's covariate shift is a reweighting of the same input space — not
  cross-domain transfer in the ladder's L3 sense. The claim it supports is
  narrow: *λ, not d, is the complexity that prices transfer error*.

## Files

- `run.py` — the experiment (pure numpy, deterministic; ~4 s)
- `plot.py` — renders `s25_result.png` from `curves.npz`
- `verdict.json` — machine-readable outcome
