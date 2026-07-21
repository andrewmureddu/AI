# S26 — is degeneracy an *attractor* of learning dynamics? (mixed: state yes, dynamics no)

**Question.** [S25](../S25-rlct-singularity/) established that the learning
coefficient λ (RLCT) charts the prediction field at its singularities.
[S11](../../questions/SPECULATIVE.md) conjectures criticality/degeneracy is an
*attractor of optimization*. This experiment tests the learning-domain instance:
estimate the **local** λ̂ along an SGD trajectory of a small tanh network
(SGLD estimator, Lau-et-al style) and ask whether the dynamics flow toward
singular (low-λ) regions.

## Registered predictions and outcomes

| | Prediction (registered before running) | Outcome |
|---|---|---|
| **Leg A** | SGLD λ̂ matches the exact localized-functional value (S25-style quadrature, same γ) within 15% on three solved models | **Confirmed** — 4.6% / 11% / 1% error; regular case reads d/2 accurately, singular cases read below d/2 |
| **P1** | final solution is singular: λ̂ < d/4 = 4 | **Confirmed, strongly** — λ̂_final = 1.38 vs d/2 = 8 (teacher needs 2 of 8 units) |
| **P2** | λ̂'s largest rise aligns with the largest loss drop | **Not evaluable** — mid-training checkpoints are not critical points; the localized chain flows downhill and λ̂ goes (hugely) negative there, measuring *escape rate*, not dimension. Recorded, not scored. |
| **P3** | after loss convergence, λ̂ drifts *down* (SGD noise moves along the level set toward degeneracy) | **Falsified** — λ̂ drifts *up* (1.16 → 1.38) while loss still creeps down (0.473 → 0.467); the drift tracks residual fitting, not degeneracy-seeking |

**Post-hoc control (unregistered, added after P3 failed):** if SGD noise sought
degeneracy, noiseless full-batch GD from the same init should end at higher λ̂.
It doesn't: full-batch λ̂ = 1.40 vs SGD 1.38 — indistinguishable.

## What this means

- **The solution *state* is exactly as singular as S25's chart predicts**: the
  8-unit student fitting a 2-unit teacher lands at λ̂ ≈ 1.4, far below the
  regular d/2 = 8. Overparameterized solutions live deep in the singular part
  of the field. (Leg A's calibration shows the estimator under-reads singular
  points and reads regular points accurately, so this gap is conservative.)
- **But we found no *dynamical attraction* to singularity.** λ̂ rises during
  late training (structure formation costs effective dimensions — consistent
  with the developmental-interpretability literature), and SGD noise adds
  nothing degeneracy-seeking over full-batch GD here. The honest reading:
  **the low-loss set is generically singular, and dynamics just descend loss**
  — degeneracy is where you *end up*, not what you're *pulled toward*.
- For S11 this is a partial falsification of the strong ("attractor") form in
  the learning domain, while the weak form ("optimized systems sit at singular
  points") survives — for the deflationary reason that almost all good
  solutions are singular.

## Honest limits

- One architecture (1-8-1 tanh, d=16), one task, one init seed for the
  trajectory. A grokking-style task with genuine plateaus could make P2
  evaluable (checkpoints near critical points) and might show different drift.
- λ̂ at non-critical points is not meaningful with this estimator; the
  trajectory's early values are reported for completeness only.
- "Loss flat" in P3 is a 0.3-dex criterion; the loss was still creeping down,
  which is exactly why the P3 failure is attributed to residual fitting rather
  than level-set drift. A cleaner P3 needs a truly converged plateau.
- The full-batch control shares the trajectory's init; different inits could
  break the tie.

## Files

- `run.py` — the experiment (pure numpy; ~5 min; predictions in the docstring)
- `plot.py` — renders `s26_result.png` from `curves.npz`
- `verdict.json` — machine-readable outcome
