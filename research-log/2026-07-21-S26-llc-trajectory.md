# 2026-07-21 — Restraint: degeneracy is where you end up, not what pulls you (S26)

**Worked on:** S26 (new) — the learning-domain instance of S11
(criticality-as-attractor), built directly on S25's chart
**Change:** S26 added and tested same day; **mixed verdict** — the singular-state
claim confirmed, the attractor-dynamics claim falsified in this setup. S11's
strong form takes its first real hit.

## Why this one

S25 ended with "the real prize": track the local learning coefficient λ̂ along a
training trajectory and test whether optimization *flows toward* singular
regions (S11's claim, instantiated in learning). If true, criticality's
recurrence would be a consequence of optimization; if false, singular endpoints
need a different explanation.

## What I did

([`../experiments/S26-llc-trajectory/`](../experiments/S26-llc-trajectory/), predictions registered in the docstring first.)

- **Leg A:** validated an SGLD local-λ̂ estimator against the *exact* value of
  the same localized tempered functional, computed by S25's quadrature
  machinery on the same three solved models — a deliberate weld: the new
  instrument is calibrated against the old one. Passed (≤11% error). Key
  calibration fact: regular points read accurately; multiplicity>1 singular
  points under-read (the log log n effect S25 measured) — so singular-vs-regular
  calls are conservative.
- **Leg B:** 1-8-1 tanh student (d=16) learns a 2-unit teacher by mini-batch
  SGD; λ̂ estimated at 27 checkpoints through fitting and a long post-convergence
  phase. Registered: P1 (final λ̂ < d/4 — singular solution), P2 (λ̂ steps align
  with loss drops), P3 (post-convergence λ̂ drifts *down* — the S11 direction).

## What I found

- **P1 confirmed strongly:** λ̂_final = 1.38 vs d/2 = 8. The solution sits deep
  in the singular part of the field, as S25's chart predicts for an
  overparameterized fit.
- **P2 not evaluable — and that's a finding about the instrument:** at
  non-critical mid-training points the localized chain runs downhill and λ̂
  goes hugely negative (−1557 at init). λ̂ is a *dimension* only at (near-)
  critical points; elsewhere it measures escape. Logged rather than scored.
- **P3 falsified:** λ̂ rose 1.16 → 1.38 during the "converged" phase — but the
  loss was still creeping down (0.473 → 0.467), so the rise tracks residual
  structure formation (consistent with developmental-interpretability reports
  of LLC increasing through stages), not level-set drift.
- **Post-hoc control (unregistered, labeled as such):** full-batch (noiseless)
  GD from the same init ends at λ̂ = 1.40 ≈ SGD's 1.38. SGD noise adds nothing
  degeneracy-seeking here.

## Decisions / level changes (with reasons)

- **S11's strong form ("optimization is *driven* toward criticality") is
  contested in the learning domain:** the endpoint is singular, but noiseless
  descent gets exactly as singular — the deflationary explanation ("almost all
  low-loss solutions are singular; dynamics just descend loss") fully accounts
  for the data. S11 stays 🔴 with this counter-evidence on record; its weak
  form (optimized systems *sit at* singular points) is what P1 supports.
- A failed registered prediction is kept as-is in verdict.json — the repo's
  rule that a killed conjecture is a mapped region.

## Honest limits

One architecture/task/init; no truly flat plateau (which is what a clean P3
needs); early-trajectory λ̂ meaningless by construction. A grokking-style task
with genuine developmental plateaus is the right escalation — it would make P2
evaluable and give P3 a real level set to drift on.

## Next

- Grokking-adjacent task (modular arithmetic in a tiny net, or a task with
  forced plateaus) → re-run P2/P3 where checkpoints are near-critical.
- Multi-init version of the full-batch control (the tie could be init-specific).
- S21 connection unchanged from S25's log: sloppy-spectrum cutoff vs 2λ.
