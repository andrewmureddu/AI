# P-D — does the allometric exponent reduce to a partition function? (result)

**Prediction under test:** [`invariants/FLOORS.md`](../../invariants/FLOORS.md) §3's
only *negative*. The floor sort put [scaling & allometry](../../invariants/scaling-allometry.md)
(#9) outside the tower entirely — "the WBE exponent comes from branching geometry,
not a partition function" — about a **seed** entry with no evidence behind the
assignment. P-D is also the load bearer for the proposed **floor 4** (§4), where
allometry is listed only as a *candidate*.

**Status: P-D confirmed, and the exponent is now a written-down law rather than a
slogan.** The exponent is θ = min(1, ln n / −ln(β²γ)) — a ratio of logs of the
branching data, blind to every energy scale, non-analytic where dominance
switches. **The one genuine variational principle in the derivation produces the
wrong exponent:** no dissipation-minimizing network gives 3/4.

Run it: `python3 run.py` (numpy + scipy, deterministic, ~8 s). Predictions were
registered in [`PREREGISTRATION.md`](./PREREGISTRATION.md) before the run; raw
output in [`verdict.json`](./verdict.json).

## Design

The trap this experiment had to avoid: "allometry has no variational principle"
is a strawman, because **WBE's own derivation contains an optimization** — the
branching ratios are selected by minimizing dissipation and by matching
impedance. Optimization over a measure is floor 2 ([P-C](../../invariants/FLOORS.md)),
so the naive P-D is simply false.

The claim was therefore registered in the only form that can fail:

> the map (cost functional) → θ **factors through the two ratios (β, γ)**, and
> the second half of that map is a log-ratio with no cost, no energy scale and no
> conjugate variable in it.

Legs: **A** the law and its n-invariance; **B** what the optimizers actually
select, with radii left free; **C** mixed regions; **D** an independent
dimensional route; **E** the honest Φ attempt, with a control.

## Results

### A — the exponent is a log-ratio, exactly, and n cancels

    theta  =  ln n / ( -ln(beta^2 gamma) )        (star)

| Prediction | Result |
|---|---|
| **P1** (★) holds in its stated validity region (n β²γ < 1) | ✓ worst relative error **7.1e-11** over 22 (scheme, n) pairs |
| **P2** n-invariance under the WBE rules | ✓ θ = 3/4 for n = 2, 3, 4, 6, 10; spread **4.0e-15** |
| finite-N residual decays **exponentially**, not as 1/N | ✓ 5.1e-6 → 4.9e-10 → 0 (machine) at N = 20, 40, 80 |

Six ratio schemes were used, including two chosen to be off any biological
scheme and one whose ratios are *n-independent* (β = 0.6, γ = 0.7) so that the
cancellation cannot be an artifact of how β and γ were parameterized in n.

**Found, not registered: the law is kinked, and Murray's law sits exactly on the
kink.** (★) assumes the volume sum is dominated by the aorta end. When
n β²γ > 1 the sum is dominated by the *capillary* end instead and θ = 1. The
full law is

    theta  =  min( 1,  ln n / (-ln(beta^2 gamma)) )

verified across the switch (all 30 cases to 5.8e-3, the residual being the
marginal log correction). At exactly nβ²γ = 1 the geometric series degenerates
to N equal terms — and that marginal point *is* Murray's law. So the
dissipation-optimal network is not somewhere in the interior of the scheme
space; it is on the non-analytic boundary of it.

**A registered finite-size form failed as written, and the mechanism it named was
right.** I registered the marginal residual as θ_N = 1 − ln(N+1)/(N ln n). That
is the chord from the origin; θ is measured as a *local* slope, so the correct
comparison is the derivative of the same ln(N+1) term, 1/((N+3) ln n). Measured /
registered = 0.28→0.17 (wrong, and drifting); measured / corrected =
**0.972, 0.984, 0.992, 0.996, 0.998** at N = 20…320. Right mechanism, wrong
estimator.

### B — the magnitudes are invisible; only structural counts enter

Radii were left **free** (r₀…r₁₄, no geometric form assumed) and the ratios came
out of a constrained optimizer.

| Cost functional | selects β | n β²γ | θ |
|---|---:|---:|---:|
| dissipation @ fixed volume (**Murray's law**) | 0.629961 = n^(−1/3) | 1.0000 | **0.99711 → 1** |
| dissipation @ fixed **surface** (invented, no biological standing) | 0.574349 = n^(−2/5) | 0.8312 | **0.88235** |
| turbulent flow law (a = 4.75) @ fixed volume | 0.663150 | 1.1081 | **1.00000** |
| shallow flow law (a = 2) @ fixed volume | 0.500000 | 0.6300 | **0.75000** |
| impedance matching, area (Y ∼ r²) | 0.500000 | 0.6300 | **0.75000** |
| impedance matching, Womersley (Y ∼ r^5/2) | 0.574349 | 0.8312 | **0.88235** |

Every β is recovered from its analytic value to ≤ 4.9e-8, with bulk ratio spread
≤ 1.9e-6 (the optimizer really does produce a geometric network without being
told to).

**P5 ✓ — the cost never enters θ except through β.** Worst |measured − law| / law
across all six functionals: **2.9e-3**, and that single case is the marginal
Murray point with its known log correction; the other five agree to **≤ 1.5e-14**.
Six different functionals, six β, and in every case θ is recovered from (β, γ)
alone — with the viscosity, the flow rate, the pressure and the functional's own
form absent from the recovery.

**P3 ✓ — six decades on six dimensionful quantities move θ by 1.1e-8.**
`r_c, l_c, ρ, B_c` move it by ≤ 5.6e-16 (they are prefactors). `μ` and `Q₀` were
pushed *into the optimizer that selects β*, where they could in principle have
changed the selection: β moves by 1.3e-8 and θ by 9.7e-9 — optimizer tolerance,
not dependence.

**And the registered contrast holds: structure does move it.** Sweeping the flow
law's exponent a in R ∝ l/r^a:

| a | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 | 6.0 |
|---|---|---|---|---|---|---|---|---|
| θ | 0.750 | 0.818 | 0.882 | 0.943 | 0.997 | 1.000 | 1.000 | 1.000 |

each matching the law from the optimizer's own β. Magnitudes never matter;
integer and structural counts always do. That is the opposite of a Legendre
exchange rate, which is *set* by magnitudes.

**P4 ✓, and it is the sharpest negative here.** Dissipation minimization gives
θ = 1, not 3/4, for Poiseuille flow — and for **every** flow law at least as
steep as Poiseuille, since a ≥ 4 puts the network past the dominance switch.
Reading off the table: dissipation minimization reaches 3/4 only at **a = 2**, a
resistance law R ∝ l/r² that no viscous flow obeys. The one place a genuine
variational principle enters WBE's derivation produces the wrong exponent; 3/4
requires the non-variational ingredients (space-filling, impedance matching).

### C — mixed regions follow a parameter-free hyperbola

With a fraction f of levels on Murray ratios (capillary side) and 1 − f
area-preserving:

| f | 0 | 0.25 | 0.5 | 0.75 | 1.0 |
|---|---|---|---|---|---|
| measured θ | 0.75000 | 0.79999 | 0.85714 | 0.92307 | 0.99711 |
| 3/(4 − f) | 0.75000 | 0.80000 | 0.85714 | 0.92308 | 1.00000 |

**P6 ✓** — worst relative error over the registered set **1.1e-5** (registered
tolerance 2%), and n-independent: spread across n ∈ {2, 4, 10} is ≤ 2.9e-6 for
f ≤ 0.75. The residual at f = 1 is again the marginal log correction. No free
parameters were fitted anywhere in this table.

### D — an independent route reaches the same exponent with a different mechanism

Banavar-style efficient supply networks serving N sites at constant density in d
dimensions; total flow-volume C = Σ_links flow × length should scale as
N^((d+1)/d), giving θ = d/(d+1) with no energetics anywhere.

| d | predicted θ | Banavar lower bound | directed network | **MST (registered)** |
|---|---|---|---|---|
| 2 | 0.6667 | **0.6633** (0.5%) | **0.6680** (0.2%) | 0.6037 (9.4%) |
| 3 | 0.7500 | **0.7494** (0.08%) | **0.7337** (2.2%) | 0.6065 (19.1%) |
| 4 | 0.8000 | **0.8046** (0.6%) | **0.7969** (0.4%) | 0.6272 (21.6%) |

**P7 ✓ on two constructions, ✗ on the one I registered.** I registered the
minimum spanning tree, and the MST **fails**: its exponent is ~1.6 in every
dimension, barely moving with d. The diagnosis is that the MST minimizes total
*wire length*, which is a different functional from transport cost — its paths
wander, so path length does not track euclidean distance and the d-dependence is
destroyed. The claim is carried instead by (i) the Banavar lower bound
Σᵢ|xᵢ − x_source|, which is construction-free, and (ii) a directed network built
post-hoc, in which each site attaches to its nearest neighbour strictly closer to
the source (0 fallbacks at every N). The lower bound is the stronger evidence
precisely because it involves no network-building choice at all.

Either way the exponent is **(d+1)/d — a ratio of dimension counts**. So 3/4 has
two independent derivations, one through vessel geometry and one through
dimensional counting, sharing nothing but the log-ratio form.

### E — the Φ attempt, and what it fails on

The honest construction: the exponential family with sufficient statistics
x = (ln M, ln B) over the network family, natural parameters λ, and log Z(λ).

| | max(1 − corr) | conjugate ratio d⟨ln B⟩/d⟨ln M⟩ |
|---|---|---|
| allometric family (WBE) | **2.2e-16** | **0.750000**, varying by **1.1e-13** |
| allometric family (Murray, marginal) | 7.4e-7 | 0.9884–0.9955, varying by 7.2e-3 |
| control: 4×4 periodic 2D Ising, exact | max\|corr\| = **0.125** | varies by **151%** |

**P8 ✓.** Over four decades of λ and three directions in parameter space, the
covariance ∇² log Z is **rank 1 to machine precision** — the smaller eigenvalue is
exactly 0 in floating point — and the conjugate ratio is *constant*. The exponent
is not a derivative of a free energy with respect to anything; it is the slope of
a one-dimensional support, and the Φ machinery reproduces it without deriving it.
The control shows the test is not vacuous: a genuine two-statistic exponential
family has full-rank covariance and a conjugate ratio that swings by 151%.

**The control I registered failed, for the same structural reason the test
detects.** I registered mean-field Ising. Its |corr| runs from 0.469 to **0.9999**
— violating the registered "< 0.99" — because mean-field E and M are *both
functions of the single order parameter m*. It is a one-index family, exactly the
degeneracy under study, and I had proposed it as the non-degenerate control. It
is reported rather than dropped, and replaced by the 4×4 2D Ising enumeration
over all 65 536 configurations, where the two statistics are genuinely
independent.

## What this establishes

**P-D confirmed on every registered leg.** The allometric exponent is
θ = min(1, ln n / −ln(β²γ)): log(multiplicity per level) over log(rescaling per
level). That is *literally* the [floor-4 signature](../../invariants/FLOORS.md) §4
already measured elsewhere — S5's type-R threshold exponent ln n₀/ln(t+1) and the
deterministic fractal dimension ln N/ln b. Allometry moves from **candidate** to
**third measured exhibit** for the scheme layer.

**Optimization is present and does real work — as a selector, not as a source.**
This is the finding that keeps P-D from being a strawman. Six cost functionals
select six different β, and the exponent is then a log-ratio of the selected
geometry with the functional absent. The map really does factor, and it factors
through exactly two numbers.

**The variational route gives the wrong number.** Dissipation minimization yields
θ = 1 for Poiseuille and for anything steeper. If allometry were a floor-2 object
this is where 3/4 would have come from, and it does not.

**A small contribution to P-E, the map's live architectural question.** FLOORS §4
asks whether the scheme layer is floor 1 in disguise. This run shows the ratios
β and γ are selected by conditions that *are* floor-1-flavoured — impedance
matching is a reflectionless (flux-matching) condition, space-filling is a
geometric constraint. So the scheme layer **takes input from floor 1**. But the
exponent is not thereby a floor-1 object: floor 1's job is to choose Φ's
coordinates, and here there is no Φ downstream — the log-ratio is terminal. That
is evidence for *separateness* without settling it, and it is the first evidence
either way.

**A sharper floor-3 / floor-4 boundary, measured.** Floor 3's support facts are
singularities *located on a set*, with Φ regular elsewhere. P8's degeneracy is
rank deficiency **everywhere in parameter space**, for every λ — the signature of
one index pushed through two observables, i.e. of the description map itself.
That distinction is now a measurement (rank of ∇² log Z as a function of λ) and
not a matter of taste.

**Bonus structure: the exponent is non-analytic.** θ = min(1, ·) has a kink at
n β²γ = 1, and Murray's law sits exactly on it. A scheme exponent can be
non-analytic in a scheme parameter without any Φ being non-analytic in a
thermodynamic one — worth noting, because "non-analyticity ⇒ floor 3" is a rule
this repo has been using loosely.

## Honest limits

- **These are models of allometry, not organisms.** Nothing here tests whether
  real metabolic rates scale as M^(3/4); the Kozłowski–Konarzewski dispute is
  untouched and out of scope. The question answered is what *kind of object* the
  exponent is in the theories that produce it.
- **P8 is a measurement, not a non-existence proof.** Rank-1-everywhere and a
  constant conjugate ratio are strong evidence that no Φ-derivative is doing the
  work here; they do not prove no Φ exists.
- **The registered MST construction failed** (leg D) and the directed network
  replacing it was built after seeing that failure. The construction-free lower
  bound is the part that should be weighted.
- **The registered control failed** (leg E) and its replacement was chosen after
  the fact — though in the safest direction, since the replacement makes the
  discriminator harder to pass, not easier.
- **The a-sweep holds γ = n^(−1/3) fixed.** A joint optimization over both ratios
  is not done, so "dissipation minimization cannot give 3/4" is established for
  space-filling lengths, not in full generality.
- **Urban scaling** (#9's other instance, and the one where the mechanism is most
  contested) is untouched.
