# 2026-07-26 — D2: the P0 is answered, and there is no fourth floor

**Worked on:** [D2](../questions/UNKNOWN-LAWS.md) — the map's standing P0, open
since [the floor sort](../invariants/FLOORS.md) on 2026-07-25 and reprioritized to
P0 in three successive syntheses.
**Change:** the proposed fourth floor is **retired, not promoted**. The scheme
layer is reclassified as the tower's structure group; its chart-free residue is
identified with [D1](../experiments/D1-chart-invariance/)'s degeneracy order.
New derivation + experiment; `FLOORS.md` §4, SYNTHESIS §4/§6/§7 updated.

## What I did

[`FLOORS.md`](../invariants/FLOORS.md) §4 had found four things refusing floors
1–3 with one shared signature — a log-ratio, log(multiplicity) over
log(rescaling) — and proposed a fourth floor, naming "floor 1 in disguise" as the
live alternative. D1 added a third option by noticing its own chart order
k = d ln λ / d ln ε has that signature and is removable. The counter-horn was
recorded at the same time and was the thing to beat: **an RG eigenvalue predicts
which perturbations are relevant, and predictive work is not obviously gauge.**

Deciding it required stating something the repo never had: *which group* the
floors are defined up to. So D2 is primarily a
[derivation](../derivations/D2-gauge-of-the-tower.md), with an
[experiment](../experiments/D2-gauge-group/) whose honest job is checking the code
and testing the one numerical prediction the derivation makes about systems it
did not construct.

## What I found

**Two groups, and the enlargement is exactly floor 3.** For reparameterizations
φ of the approach to a singularity: **G_diff** (φ′(0) exists and is nonzero —
smooth *at* the singular point) and **G_pow** (φ ~ c·ε^a — a homeomorphism, smooth
*away* from the point, not at it). G_diff ⊊ G_pow, and the extra freedom lives
entirely at the singularity. That is already the structural fact: the group
enlarges precisely where Φ is non-smooth.

**RG eigenvalues are the same object as chart orders.** Under a smooth coordinate
change the linearized RG map transforms by conjugation, so eigenvalues are
invariant — verified to **5.3e-15** over six random conjugations of a 2×2 map.
Under u → u^a the map u′ = Λu becomes v′ = Λ^a v, so y → a·y — verified to
**≤2.4e-12** (1D Ising decimation), **5.7e-10** (diamond hierarchical lattice),
**1.8e-8** (Feigenbaum cascade), with the legs first recovering y = 1,
ν = 1.338266 and δ = 4.669201. Identical transformation behaviour to D1's chart
order. **So `FLOORS.md`'s four refusers are not four things that happen to rhyme —
they are the transformation data of G_pow modulo G_diff**, and a transformation
parameter is not a fact on any floor. That is *why* they refused.

**The residue is one integer.** Under common-a, what survives is signs, counts and
ratios — and those are three faces of the same thing. For a degeneracy Φ ~ y^p the
number of coefficients that must be tuned to sit on it is p − 2, which is also the
number of relevant RG directions, and also the reciprocal of β/k since
m ~ λ^{1/(p−2)}. Measured on **full** models: β/k = **0.5000** (mean-field Ising,
p = 4) and **0.2503** (Blume–Capel on its tricritical line, p = 6) against
1/(p−2), while β spans 4× and k spans 2× across the legs so the constancy is not
vacuous. **What was under the fourth floor was D1's *p*.**

**The counter-horn survives — in the part the derivation predicted.** "Which
perturbations are relevant" is a claim about the *sign* of y, and signs are
G_pow-invariant. The predictive work is real and it lives in the non-gauge part.
Quoting the magnitude 0.747 requires also quoting the chart. So the counter-horn
does not restore a floor; it identifies which piece is chart-free.

**Two things fell out that I was not looking for.**

1. **`FLOORS.md`'s asymmetry stops being an observation.** The sort had recorded,
   without explanation, that *floor 2 collapses and floor 3 stratifies*. Away from
   the singular point G_pow = G_diff, so floor-2 objects live under the ordinary
   smooth group where tensorial quantities have genuine invariants — one convex
   function seen from seven angles. At the singular point the group is strictly
   larger, eats exponent magnitudes, and leaves a discrete residue. **The
   asymmetry is a statement about which group acts where**, and nothing in the
   derivation was built from it.
2. **D1's loose end is closed.** D1 risked implying critical exponents are
   meaningless. They are not: universality is a **G_diff** statement, and under
   G_diff exponents are strictly invariant. Physics fixes the chart canonically
   because reduced temperature enters the Hamiltonian linearly. **Within a domain
   exponents are facts; across domains only ratios, signs and counts are.** S5 and
   S7 compared G_diff-facts across a G_pow gap.

## Decisions / level changes (with reasons)

- **The proposed fourth floor is retired.** Not promoted, not demoted to floor 1 —
  reclassified. `FLOORS.md` §4 keeps the original horn statement unedited above
  the resolution, per the repo's keep-don't-delete rule.
- **The tower stays at three floors**, now explicitly *defined up to G_diff*. The
  mermaid diagram's "outside the tower? / open: fourth floor?" node is relabelled
  as the structure group.
- **SYNTHESIS §7's P0 is closed** and replaced with what D2 leaves open: the
  residue for **support-type** singularities, which have no *p* at all (D6).
- **No new [`invariants/`](../invariants/) entry**, same reasoning as D1: this is
  architecture, and its home is `FLOORS.md` plus the derivation.
- **Novelty, honestly.** The group analysis is **N0–N1** — the G_diff half is
  Wegner's nonlinear scaling fields in the RG literature's own language, and
  smooth-vs-topological conjugacy is standard in dynamical systems. The
  pre-registration predicted this and it came true. The **N2** claim is confined
  to the architectural reading: the scheme layer as *this tower's* structure
  group, and its residue as p − 2.

## Honest limits

- **Most of the experiment is a theorem check**, declared in advance. P1/P2/P3 are
  linear algebra and one line of exponent arithmetic; they test the code, not the
  world. The at-risk content is two legs, and **both are physics** — the same gap
  D1 recorded and did not close.
- **The common-a commitment is load-bearing.** P3 shows explicitly that if each
  eigendirection may be re-charted separately, the ratios die and only signs and
  counts survive. The argument for common-a — a domain supplies one
  distance-to-threshold, not one per eigendirection — is a claim about scientific
  practice, not a theorem.
- **One mid-run correction on record.** P5's first implementation "resampled" onto
  a log-uniform grid in ε′, but a power map sends a log-uniform grid to a
  log-uniform grid, so the sample points were identical and the invariance was
  definitional. Fixed to sample linearly in ε′; exponents stable to 6.5e-5.
- **P5 remains closer to a demonstration than a test**, and the README says so: an
  observable–observable relation is chart-free *because* it contains no chart.
  That is the content of "gauge," not evidence for it.

## Next

1. **D6 — the singularities with no *p*.** This is what D2 leaves open and it is
   now the sharpest question: support-type singularities (S5's type S) have no
   Taylor expansion and no codimension, so the residue is unidentified there.
   M/M/1 at saturation is the cheap instance.
2. **A full at-risk leg from outside physics**, for both D1 and D2. Twice
   recorded, twice not closed.
3. **D3 — the ladder as a chart-invariance count.** D2 makes it sharper than when
   it was filed: if transfer is exactly chart-invariance, the L2/L3 cliff should
   be the G_pow quotient, and the existing ladder-vs-transfer harness can test it.
4. **Re-register P8's δa³ from D1**, still outstanding.
