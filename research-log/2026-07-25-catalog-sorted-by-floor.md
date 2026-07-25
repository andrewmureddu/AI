# 2026-07-25 (second entry) — the catalog sorted by floor

**Worked on:** all 23 invariant entries; the tower architecture.
**Change:** every entry now carries a `**Floor:**` line; 7 entries marked ▸facet
(no longer independent invariants); #21 and #9 and #13 recorded as refusing the
tower; new [`invariants/FLOORS.md`](../invariants/FLOORS.md); catalog index gains
a Floor column.

## What I did

Ran every catalog entry against the architecture derived in
[`symmetry-sector.md`](../derivations/symmetry-sector.md) — floor 1
(symmetry-constituted), floor 2 (Φ-regular), floor 3 (Φ-singular) — and recorded
the assignment, the reason, and, for entries with no evidence behind them, the
falsifiable prediction the assignment amounts to.

This was the P0 that survived three consecutive syntheses without being done. It
was worth doing, and not for the reason it was queued: the value was not tidiness
but the two things the sort refused to do cleanly.

## What I found

**1. Redundancy deletion works — but only on floor 2.** Seven entries (#3 entropy,
#12 replicator, #14 Pareto, #15's Legendre half, #16 bottleneck, #17 universal
update, #20 statistical geometry) are ∇Φ, ∇²Φ, Φ* or −Φ of *one convex function*.
They are not seven invariants that agree; they are one function differentiated
seven ways, and the catalog now says so. Six of those are whole entries; #15
survives only in its symplectic half. Effective independent count: 23 → ~16 —
a real simplification, and a smaller one than "much of the map is one object"
implied, because the deletion is confined to floor 2.

**2. Floor 3 does not collapse — it stratifies.** Criticality, power laws,
percolation, SSB, critical slowing down and the noise thresholds are all "Φ goes
singular," but they are *different* singularities: non-analyticity, divergent
moments, null Hessian directions, lost supports, soft modes. S5 had already
measured that these carry different exponents (2 for a metric merge, 1 for support
loss), so they provably cannot be collapsed into one another. The slogan that
needed replacing —

> **Floor 2 collapses. Floor 3 stratifies.**

— is the honest version of "one object seen sideways," and explains why that
slogan always felt simultaneously right and overstated.

**3. Three entries refused the tower, and refused it the same way.** Scaling/
allometry (#9), emergence/RG (#13), and the type-R half of noise thresholds (#21)
would not reduce to any floor, with #11's deterministic half and #2's bookkeeping
half joining them. The signature they share was the surprise: **their invariant is
a log-ratio — log(multiplicity) over log(rescaling) — not a derivative of Φ.**

S5's concatenation exponent α = ln n₀/ln(t+1) is *literally of the same form* as a
fractal dimension ln N/ln b. That was measured before the sort noticed what it
was, which is the only reason I trust it. RG eigenvalues are the general case; a
code is a designed one; a deterministic fractal is one's fixed point; double-entry
accounting is a trivial one, conserving *because of the representation* exactly as
a code's redundancy does. So the catalog's oldest embarrassment (accounting
"conservation" that isn't Noether, on record since the kickoff) and its newest
result (S5's type R, from three days ago) land in the same bin.

**4. Two non-trivial assignments worth naming.** Symmetry breaking (#10) is *not*
floor 1 despite its name — SSB requires a non-analyticity of Φ, so it is floor 3.
And emergence/RG (#13) is not on a floor at all: it is an **operation on the
tower**, carrying Φ at one scale to Φ at another — which the
[S25 channel experiment](../experiments/S25-channel-independence/) had already
measured as F_c(T) = F_eff(T′)·(dT′/dT)².

## Predictions the sort makes (the part that makes it a test)

Recorded in [FLOORS §3](../invariants/FLOORS.md) with falsifiers. The two worth
running:

- **P-A, spectral gap (#19, never tested):** gap-closure *is* the ∇²Φ degeneracy,
  so the entry's four readouts (mixing, connectivity, consensus, sync) are one
  number because they are the softest direction of one Hessian. Joins S7's
  τ·λ_min = 1 from the connectivity side.
- **P-D, allometry (#9):** Kleiber's 3/4 should *not* be derivable from a
  partition function. The sort's most falsifiable negative.

**P-B is a retrodiction and it landed.** The sort says diffusion splits at
finite-vs-infinite variance (floor 2 for normal, floor 3 for Lévy, since divergent
moments are exactly Φ misbehaving). The
[transfer-cliff experiment](../experiments/ladder-vs-transfer/) measured the L2/L3
cliff at *precisely that line* — months before the tower existed and with no
connection to it. Consistency check I did not construct.

## Decisions

- **The fourth-floor question is now the map's P0**, and the sort changed what the
  question is. It is no longer "is there a candidate" — there is a cluster with a
  shared signature. It is **"does the scheme layer collapse into floor 1?"** A
  code *is* a redundancy chosen to be invariant under the noise, and "invariance
  chooses the coordinates" is exactly floor 1's job. That horn is live and cheap
  to attack.
- **Seed-entry assignments are labelled as predictions, not findings.** Only #6,
  #10, #21, #22 and #4's reduction rest on a derivation or an experiment. The rest
  are the sort's claims and can be wrong; FLOORS.md says so per entry.
- Optimal transport (#18) is flagged **unresolved** rather than forced: the JKO
  flow is Φ-driven (floor 2), but the Wasserstein metric is not ∇²Φ and is not a
  log-ratio object either. It fits neither the three floors nor the proposed
  fourth. Either Otto calculus reduces it, or it is a second exhibit against
  monism.
- `domains/README.md` left unchanged: floors and ladder levels are orthogonal
  axes, and the matrix encodes the latter.

## Next

- Attack the live horn of the fourth-floor question (does the scheme layer reduce
  to floor 1?).
- P-A (spectral gap) is the cheapest unrun prediction with teeth.
- Still-unworked stones: S2, S4, S6, S8, S10, S12–S17, S19–S22, S24.
