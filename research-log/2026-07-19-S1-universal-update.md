# 2026-07-19 — S1 derived: the universal update

**Worked on:** S1 (mirror-descent unification); invariant #17
**Change:** new `derivations/` tier + full derivation; #17 seed → developing (L3)

## Restraint stroke (analytical) — S1 tested by derivation

Pure derivation, no compute:
[`../derivations/S1-universal-update.md`](../derivations/S1-universal-update.md).

Derived once that entropic mirror descent on the simplex is
`x_{t+1,i} ∝ x_{t,i} exp(−η g_i)`, then specialized it four ways:

- **Multiplicative weights** — g_i = expert loss ℓ_i (definitional).
- **Bayes** — g_i = log-loss −ln L_i, η = 1 (tempering → η ≠ 1).
- **Replicator** — the continuous-time limit (η→0) of the update *is* ẋ_i =
  x_i(f_i − f̄), exactly.
- **Gibbs** — energy g_i = E_i, η = β; the free-energy minimizer / fixed point.

**Two L3 findings:**
1. The local update + its geometry are genuinely one object — Fisher/Shahshahani
   natural-gradient descent (ties to S3 and the prediction-field metric).
2. The normalizer is one object too: **free energy = −log evidence = cumulative
   log-loss = −log-growth** (Jaynes / Bayes evidence / online-learning regret /
   Kelly log-growth). Possibly the deeper unification than (★) itself.

## What restraint bought — the sharp boundary

The valuable part is the *demotion*: **global dynamics are NOT shared.** Same local
update, but a fixed loss concentrates (Bayes, Gibbs) while a game-coupled loss
cycles forever (replicator/MWU in zero-sum games — Poincaré recurrence,
Mertikopoulos et al. 2018). So "they all converge alike" is **retired to L1** with a
concrete counterexample. Also logged: vanilla Bayes locks η = 1; discrete-replicator
vs. MWU agree only to O(η) / in continuous time; physical relaxation shares the
Lyapunov/fixed-point structure but not the trajectory.

Net: **S1 confirmed, sharpened, bounded.** #17 promoted seed → developing, L3 for
the local update (global-convergence claim explicitly rejected). S2 (η = learning
rate = temperature = selection intensity) falls out for free.

## Method note

Added a `derivations/` tier alongside `experiments/` — analytical vs. numerical
restraint. Same discipline: not done until the boundary condition is written.

## Next

- **Cheap numpy follow-up:** exhibit the concentrate-vs-cycle split directly — the
  *same* update converging on a fixed loss vs. Poincaré-recurring on Matching
  Pennies. Turns the §5 boundary into a picture.
- **Promote the §3 identity** (free energy = −log evidence = log-loss = log-growth)
  to its own entry; it likely subsumes parts of `entropy-information.md` and
  `information-bottleneck.md`.
