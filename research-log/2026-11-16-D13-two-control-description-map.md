# 2026-11-16 — D13: at m = 2 the residue is still a ray; the plane belongs to the scaling function

**Worked on:** [D13](../questions/UNKNOWN-LAWS.md) — D8's m > 1 case under a
literal description map, listed under *Next* by D11 and D12.
**Change:** new derivation
[`derivations/D13-two-control-description-map.md`](../derivations/D13-two-control-description-map.md)
and experiment
[`experiments/D13-two-control-description-map/`](../experiments/D13-two-control-description-map/).
D11 §2's m > 1 clause withdrawn; D8's residue qualified as base-ray-dependent
(append-only notes in both, `FLOORS.md` §4, `SYNTHESIS.md` §7.0). Stones
12 → 13; experiments 34 → 35, derivations 11 → 12. No level changes.

## What I did

Needed a description map with two relevant directions and observables that
are smooth functions on the control plane. Period doubling's tricritical
point has the first and not the second (its natural observables live on
curves), so I used the Ising model on the diamond hierarchical lattice, where
the recursion in (K, h) and the free energy are exact. Derived the field
recursion by hand; λ_t reproduces the known ν ≈ 1.338.

Writing the registration, the Euler relation made the answer predictable in
outline: one direction of D8's plane is forced to be the weight vector, and
nothing forces the rest. The unknown was the map's log-periodic amplitude. I
registered a bound on it from memory of the literature's tone.

The natural scale of the base-ray label κ was also unknown, so the κ list was
fixed by a rule rather than by looking.

## What I found

- **col(Y) rotates by 1.155 rad** between 0.1κ\* and 10κ\*. Every entry of
  the slope matrix moves; several change sign.
- **The planes share one line**, within 4e-3 of the spectral weight vector on
  the far pair.
- **Per-step increments equal the weights to 4.9e-7.**
- **The log-periodic modulation is large at strong field**: the pointwise
  Euler residual reaches 6.7e-2 and slope entries swing by 0.12 over a
  period. My bound was 1e-2. That failed P2's bound outright and P4's third
  pair by 4%.
- Post hoc, phase-averaging removes the modulation and the shared line is
  good to 1e-7.

## Decisions

- **D11 §2's "same statement with r controls" is withdrawn.** D7's ray is the
  fixed point's residue at every m.
- **D8 is qualified, not retracted.** Its group-invariance and rank results
  stand; "the residue is col(Y)" needs "at this base ray."
- **P4 is recorded as failed as registered**, with the far-pair result and
  the post-hoc explanation alongside.
- **Three stones in a row (D8, D12, D13) have had a tolerance asserted
  instead of derived.** Next registration: every bound gets a line saying
  where its number comes from, or is registered as "report, no bound."

## Next

- **Re-measure D8's cusp at several base rays.** D13 §2 predicts its col(Y)
  moves and keeps the weight vector. Cheap, and it is D13's live falsifier.
- **Completeness of D12's commuting-orbit criterion.**
- **The `FLOORS.md` kink note** — open since 2026-07-28.
- **A two-field map with an irrelevant direction** (spin-1 on the same
  lattice), to give D8's rate leg a literal-map analogue.
