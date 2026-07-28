# 2026-07-27 — P-D: the exponent that has no conjugate variable

**Worked on:** [`scaling-allometry.md`](../invariants/scaling-allometry.md) (#9),
[`FLOORS.md`](../invariants/FLOORS.md) P-D and P-E.
**Change:** new experiment
[`experiments/PD-allometry-reduction/`](../experiments/PD-allometry-reduction/);
#9 seed → developing ✓tested, its floor assignment moves from prediction to
evidence; floor 4 gains its second *measured* exhibit; first evidence on P-E's
live horn.

## What I did

Ran the [floor sort](../invariants/FLOORS.md)'s only **negative** — P-D, that
Kleiber's 3/4 is not derivable from a partition function — about an entry that,
like #19 before it, was a `seed` with nothing behind the assignment.

The design problem was that the obvious version of P-D is a strawman. WBE's own
derivation *contains* an optimization: the branching ratios come from minimizing
dissipation and from matching impedance, and optimization over a measure is floor
2 by P-C. Writing "allometry has no variational principle" would have been false
and would have made the experiment unlosable. So the claim was registered in the
only form that can fail:

> the map (cost functional) → θ **factors through the two ratios (β, γ)**, and the
> second half of that map is a log-ratio with no cost, no energy scale and no
> conjugate variable in it.

Radii were left free — r₀…r₁₄ with no geometric form assumed — so the ratios had
to come out of the optimizer rather than be handed to it.

## What I found

**The exponent is a law, not a slogan.**

    theta  =  min( 1,  ln n / ( -ln(beta^2 gamma) ) )

to 7.1e-11 over 22 (scheme, n) pairs, with n cancelling identically — θ = 3/4 for
n = 2, 3, 4, 6, 10 with spread **4.0e-15**. One of the six schemes was chosen with
n-independent ratios so the cancellation could not be an artifact of how β and γ
were parameterized.

**Magnitudes are invisible; structural counts are not.** Six decades on each of
r_c, l_c, ρ, μ, Q₀ and the per-capillary metabolic rate move θ by **1.1e-8** —
and μ and Q₀ were pushed *into the optimizer that selects β*, where they had a
route to matter. The flow law's structural exponent a, by contrast, walks θ from
0.750 to 1.000. That asymmetry is the whole finding in one line: a Legendre
exchange rate is *set* by magnitudes, and this is the opposite.

**Optimization is real here, and it is a selector rather than a source.** Six cost
functionals — dissipation at fixed volume (recovering Murray's law to 1.1e-8),
dissipation at fixed *surface* (an invented cost with no biological standing),
turbulent and shallow flow laws, and two impedance-matching conditions — select
six different β. θ is then recovered from (β, γ) alone, with the functional, the
viscosity and the flow rate absent, to **≤1.5e-14** in five of the six.

**The variational route gives the wrong number, and that is the sharpest result.**
Dissipation minimization yields θ = **1**, not 3/4, for Poiseuille flow — and for
*every* flow law at least as steep, since a ≥ 4 pushes the network past the
dominance switch. It reaches 3/4 only at R ∝ l/r², which no viscous flow obeys.
If allometry were a floor-2 object this is exactly where 3/4 would have come
from, and it does not.

**The Φ attempt fails in the registered way.** In the honest exponential family
with statistics (ln M, ln B), ∇²log Z is **rank 1 for every λ** — the smaller
eigenvalue is exactly zero in floating point — and the conjugate ratio is constant
to 1.1e-13 over four decades and three directions. The exponent is the slope of a
one-dimensional support; the Φ machinery reproduces it without deriving it. The
control (4×4 periodic 2D Ising, exact over 65 536 configurations) swings 151%, so
the test is not vacuous.

**A second, independent geometric route.** Efficient supply networks in d
dimensions give θ = d/(d+1): measured 0.663 / 0.749 / 0.805 against
0.667 / 0.750 / 0.800. No vessels, no energetics — a ratio of dimension counts.
Two derivations of 3/4 that share nothing but the log-ratio form.

**Two registered items failed, and both are on record.**

1. **The MST construction (leg D).** I registered the minimum spanning tree as the
   realization of an efficient network. Its exponent is ~1.6 in every dimension
   and barely moves with d — 9%, 19%, 22% errors. The diagnosis is that the MST
   minimizes total *wire length*, a different functional from transport cost; its
   paths wander, so path length stops tracking euclidean distance and the whole
   d-dependence is destroyed. The claim is carried by the construction-free
   Banavar lower bound, plus a directed network built after seeing the failure.
   The lower bound is what should be weighted, precisely because it involves no
   network-building choice.
2. **The control in leg E.** I registered mean-field Ising as the *non-degenerate*
   control. Its |corr| runs to **0.9999**, violating the registered <0.99 — because
   mean-field E and M are both functions of the single order parameter m. It is a
   one-index family: the exact degeneracy the test exists to detect, proposed by
   me as the thing that lacks it. Reported rather than dropped, and replaced with
   a genuine two-statistic family.

A registered finite-size *form* was also wrong while its mechanism was right: I
predicted the marginal residual as ln(N+1)/(N ln n), which is the chord from the
origin, whereas θ is measured as a local slope. The derivative of the same term,
1/((N+3) ln n), matches at 0.972 → 0.998 across N = 20…320.

**Found, not registered: the law is kinked, and Murray's law sits on the kink.**
(★) assumes the volume sum is dominated by the aorta end. Past nβ²γ = 1 it is
dominated by the capillary end and θ = 1 flat. At exactly nβ²γ = 1 the geometric
series degenerates to N equal terms — and that marginal point *is* the
dissipation optimum. So the dissipation-optimal network is not somewhere in the
interior of the scheme space; it is on the non-analytic boundary of it.

## Decisions

- **#9 moves from `seed` to `developing` ✓tested, and its floor assignment from
  prediction to evidence** — but only for the *type* of the exponent. Whether real
  metabolic rates scale as M^(3/4) is untouched and stays untouched; the
  Kozłowski–Konarzewski dispute is not what this measures.
- **Floor 4 gains its second measured exhibit, and this one was predicted.** S5's
  α = ln n₀/ln(t+1) was measured before the bin existed; P-D was run *because* the
  bin said allometry would land in it.
- **The floor-3 / floor-4 boundary stops being a matter of taste.** Floor 3's
  support facts are singularities located *on a set*, with Φ regular elsewhere.
  The scheme layer's degeneracy is rank deficiency **everywhere in parameter
  space**. That is now a measurement — the rank of ∇²log Z as a function of λ —
  and it is written into FLOORS §4.
- **First evidence on P-E's live horn, and it does not go the way the horn
  predicted.** Allometry's ratios really are selected by floor-1-flavoured
  conditions (impedance matching is flux-matching; space-filling is a geometric
  constraint), so the scheme layer *takes input from* floor 1. But floor 1's job
  is to choose Φ's coordinates, and here there is no Φ downstream — the log-ratio
  is terminal, and no conjugate pair exists for it to be an exchange rate between.
  *Takes input from*, not *is*. One instance; recorded as evidence, not a
  settlement.
- **P-C is now the most interesting remaining prediction, and P-D complicated it.**
  P-C says variational principles come in exactly two kinds: over a measure ⇒
  floor 2, over an action ⇒ floor 1. P-D exhibits a third case its binary has no
  slot for — a genuine optimization over a measure whose *exponent* is not a
  Φ-derivative, because the optimization selects a scheme and the scheme carries
  the exponent. P-C should be run with that case explicitly in its registration.

## Next

- **P-C**, with the selector/source distinction built into its registration from
  the start.
- **The base-variable derivation** flagged by [M3](./2026-07-25-M3-molloy-reed-rewiring.md)
  and [M11](./2026-07-25-M11-stochastic-resetting.md) is still unwritten and is
  now the oldest live debt. P-D adds a data point to it from the other end: here
  the question was not "Φ of what?" but "is there a Φ at all?", and the answer was
  no — which suggests the base-variable rule needs a null case.
- **Urban scaling** is #9's other instance and the discriminator is now concrete:
  it shares the mechanism iff its exponent is also a log-ratio of a scheme. 0.85
  and 1.15 are conspicuously *not* simple dimension ratios the way 3/4 and d/(d+1)
  are, and superlinear output has no transport route at all.
- **Neural scaling laws** are the entry's most interesting internal tension: loss
  ∝ compute^(−α) is the one instance where a Φ-route is live (via a spectrum, cf.
  [S25's RLCT result](../experiments/S25-rlct-singularity/)). If it reduces, #9
  splits — and it would be the first split with a floor-4 half.
- **M8** (extreme value / best-of-n) is still the register's next item, twice
  deferred now.
