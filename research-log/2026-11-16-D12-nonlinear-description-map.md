# 2026-11-16 — D12: the residue under a nonlinear map, and a sentence in D11 that was too general

**Worked on:** [D12](../questions/UNKNOWN-LAWS.md) — the "genuinely nonlinear
description map" probe the [D11 entry](./2026-08-04-D11-residue-reconciliation.md)
listed under *Next*, together with D11's own local falsifier.
**Change:** new derivation
[`derivations/D12-nonlinear-description-map.md`](../derivations/D12-nonlinear-description-map.md)
and experiment
[`experiments/D12-nonlinear-description-map/`](../experiments/D12-nonlinear-description-map/).
D11's boundary statement is narrowed (append-only notes in the D11 derivation,
the register, `FLOORS.md` §4 and `SYNTHESIS.md` §7.0). Stone count 11 → 12;
experiments 33 → 34, derivations 10 → 11. No level changes.

## What I did

Chose the nonlinear probe over D8's m > 1 case because it could also fire
D11's falsifier, and chose period doubling because both sides of the
identification are independently computable: log-slopes from raw maps, and a
linearized operator from a functional equation.

Prior-art search first (Feigenbaum; van der Weele–Capel–Kluiving 1987; Briggs
1991; Jona-Lasinio's Hermite spectrum). All confirmed to exist; Briggs's table
was not retrievable, so the z ≠ 2 constants went into the registration marked
as unverified recall. Pre-registration committed with no code in the tree.
Tolerances for the raw-map route were derived from a stated convergence
assumption; the collocation route's gate was not, and that is where it failed.

While writing the registration I re-read D11 §3 and noticed its proof is for a
shared U while its map is defined with iid copies. That became a leg of its
own.

## What I found

- **The identification holds under a nonlinear map.** Seven critical orders,
  two routes with no shared code, agreement 2e-8 … 4e-5 in ln δ and ln α. A
  second microscopic family agrees to ≤ 6e-5.
- **D11's blindness sentence is false as stated.** Along the curve of
  period-doubling fixed points indexed by z — tangent to the fixed-point set —
  ln α/ln δ runs 0.914 → 0.128 monotonically. The residue is a coordinate
  there.
- **Why D11 saw blindness.** Maps commuting with T carry fixed points to
  fixed points with the same spectrum. The U-family is a mixture over the
  dilation orbit of the Gaussian, under shared-U aggregation. Under the iid
  map it is not fixed at all, and D11's own shape statistic decays as
  n^−1.000 with ratio −2.000 to the scale slope — the k = 4 Hermite
  eigenvalue.
- **Two registered items failed.** The collocation gate (N = 12 continuation
  left the branch; the method resolves δ to ~1e-6, the gate asked 1e-7), and
  δ(z = 3), which I registered from memory as 5.968 and both routes put at
  6.08469.
- **One budget assumption was wrong and it did not matter:** convergence per
  level is 2.3–2.9 at z = 6, 8, not ≥ 3.

## Decisions

- **D12 graded N0 / N1-at-most.** Nothing measured is new; what moves is this
  repo's statement of D11's boundary.
- **D11 is narrowed, not retracted.** Its numbers and its C1 stand. Its
  "tangent ⇒ blind" boundary is replaced by "blind to the level sets of the
  spectrum map; commuting orbits are always in them." Original text kept.
- **The failed gate is recorded as failed**, with the table reported anyway
  and the reason for reporting it stated as post hoc.
- **No recalled constant is to be cited from this repo as a literature
  value.** The recall leg exists to show why.

## Next

- **D8's m > 1 case under a literal description map** — now skipped by three
  stones in a row. A two-relevant-direction map (e.g. period doubling with a
  second control, or a hierarchical-lattice RG with field and temperature) is
  the obvious harness.
- **Is C1's criterion complete?** Find or rule out a fixed-point family that
  is not a commuting orbit but has constant spectrum.
- **The post-hoc rate observation** (convergence factor ≈ min(δ, 1/|λ|) with
  λ a sub-leading eigenvalue of the collocation spectrum) needs the
  coordinate-change eigenvalues separated from the genuine ones before it
  means anything; then it can be registered.
- **The `FLOORS.md` kink note** — still open since 2026-07-28.
