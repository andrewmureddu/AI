# Scaling laws & allometry

> **One-line claim:** Many system properties scale as power laws of size with
> exponents that cluster around simple fractions, plausibly from transport-network
> geometry.
> **Headline correspondence level:** L2 broadly; L3 contested (WBE theory);
> a key open case.
> **Status:** developing ✓tested (the *exponent's type*, not the biology)
> **Floor:** **refuses the tower — measured, not asserted.** The exponent is a
> log-ratio of the branching data, not a Φ-derivative
> ([P-D, run](../experiments/PD-allometry-reduction/)). There is
> [no fourth floor](../derivations/D2-gauge-of-the-tower.md) to be an exhibit for:
> the scheme layer is the tower's **structure group**, and θ sits in its
> **invariant residue** — a *ratio*, invariant under scheme coarse-graining to
> 2.6e-15, measured against an extensive observable that admits no power
> re-charting. Alongside the codimension p − 2, and for the same reason.

## Statement

Allometric scaling: property Y ∝ M^b across sizes M. Domain-neutral object: the
scaling exponent b and its (claimed) derivation from fractal/hierarchical
transport networks. Distinct from within-domain criticality exponents.

## What the exponent *is* (tested)

For a hierarchical branching network with branching ratio n, radius ratio β and
length ratio γ, [P-D](../experiments/PD-allometry-reduction/) measured

    theta  =  min( 1,  ln n / ( -ln(beta^2 gamma) ) )

to 7.1e-11 across 22 (scheme, n) pairs — log(multiplicity per level) over
log(rescaling per level), with n cancelling identically (θ = 3/4 for
n = 2, 3, 4, 6, 10, spread 4.0e-15). Six decades on every dimensionful quantity
(r_c, l_c, ρ, μ, Q₀, per-capillary metabolic rate) move θ by **1.1e-8**; the
*structural* exponent of the flow law moves it a great deal. Magnitudes are
invisible, structural counts are not — the opposite of a Legendre exchange rate.

**Optimization is present, and it is a selector rather than a source.** Six cost
functionals (dissipation at fixed volume → Murray, dissipation at fixed surface,
turbulent and shallow flow laws, two impedance-matching conditions) select six
different β; θ is then recovered from (β, γ) alone with the functional absent, to
≤ 1.5e-14 in five of six cases. **The variational route gives the wrong number:**
dissipation minimization yields θ = **1**, not 3/4, for Poiseuille flow and for
every flow law at least as steep — it reaches 3/4 only at a resistance law
R ∝ l/r², which no viscous flow obeys.

Two further facts worth carrying:

- **Murray's law sits exactly on the law's kink.** θ = min(1, ·) is non-analytic
  where n β²γ = 1, the point at which the volume sum's dominance switches from
  the aorta end to the capillary end — and that marginal point *is* the
  dissipation optimum. A scheme exponent can be non-analytic in a scheme
  parameter with no Φ non-analytic in a thermodynamic one.
- **A second, independent geometric route gives the same exponent.** Efficient
  directed supply networks in d dimensions give θ = d/(d+1) — measured
  0.663/0.749/0.805 for d = 2, 3, 4 against 0.667/0.750/0.800. A ratio of
  dimension counts, with no energetics anywhere.

**What is *not* established:** whether real metabolic rates scale as M^(3/4).
P-D tests models of allometry, not organisms; the Kozłowski–Konarzewski dispute
is untouched. What is established is what *kind of object* the exponent is in the
theories that produce it.

## Manifestations by domain (seed)

- Biology: metabolic rate ∝ M^(3/4) (Kleiber's law); lifespan, heart rate — L2/L3.
- Urban: infrastructure ∝ N^~0.85 (sublinear), socioeconomic output ∝ N^~1.15
  (superlinear) (Bettencourt–West) — L2.
- ML: neural scaling laws, loss ∝ compute^(−α) — L2, mechanism debated.

## To develop

The big question (Q4/Q-urban in OPEN-QUESTIONS): do biological 3/4-power scaling
and urban scaling share the West–Brown–Enquist transport-network mechanism (→ L3),
or only the functional form (→ L2)? The 3/4 exponent's universality is itself
contested (Kozłowski–Konarzewski critique). Cross-link
`self-similarity-fractals.md`.

P-D sharpens that question rather than answering it. The discriminator is now
concrete: **urban scaling shares the mechanism iff its exponent is also a
log-ratio of a branching/embedding scheme** — and 0.85 / 1.15 are conspicuously
*not* simple dimension ratios the way 3/4 and d/(d+1) are. Sublinear
infrastructure at ~0.85 is close to neither 3/4 nor 5/6 within the data's spread,
and superlinear output has no transport-network route at all. Testing it needs
the same three legs P-D used: does the exponent move with a magnitude, does it
factor through a scheme, is the (log M, log Y) covariance rank-deficient
everywhere.

Also open, and cheaper: **neural scaling laws.** Loss ∝ compute^(−α) is the one
instance here where a Φ-route is live (the exponent is plausibly set by a
data/parameter spectrum, i.e. by an actual free energy — cf.
[S25's RLCT result](../experiments/S25-rlct-singularity/)), which would make it a
genuine floor-2 exponent sitting in an entry whose other instances are structure-group
residue. If so this entry splits — and it would be the first entry split across a
floor and the residue rather than across two floors.
