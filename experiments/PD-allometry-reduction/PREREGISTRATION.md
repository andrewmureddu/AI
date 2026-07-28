# P-D pre-registration — written before any measurement

Per the working rule used for [M3](../M3-molloy-reed-rewiring/PREREGISTRATION.md)
and [P-A](../PA-spectral-gap/predictions.json): *register the discriminator's
expected value before measuring it.* Nothing below is revised after the run;
results live in [`README.md`](./README.md).

**Prediction under test.** [`invariants/FLOORS.md`](../../invariants/FLOORS.md) §3:

> **P-D — allometry does not reduce (#9).** Kleiber's 3/4 should *not* be
> derivable from a partition function; it should come out of branching geometry,
> making it scheme structure. **Falsifier:** derive the 3/4 exponent from a Φ,
> which would put it on floor 2 and refute this line.

[`scaling-allometry.md`](../../invariants/scaling-allometry.md) is a **seed** entry
with no evidence behind its floor assignment, so this is a prediction about an
entry the sort had no hand in shaping — the same status P-A had.

**Why P-D and not P-B or P-C.** P-D is the sort's only *negative*: the only
prediction that says an entry will refuse all three floors. It is also the load
bearer for the proposed **floor 4** (§4), whose whole case is that some
invariants are log-ratios — log(multiplicity) / log(rescaling) — rather than
Φ-derivatives. Allometry is listed there as a *candidate* only. If the exponent
turns out to be a Legendre exchange rate, floor 4 loses its third exhibit and
P-D dies in the cleanest possible way.

---

## The theory (stated before the run)

### The object

A hierarchical branching network, levels `k = 0…N` (0 = aorta, N = capillary),
branching ratio `n`, radius ratio `β = r_{k+1}/r_k`, length ratio
`γ = l_{k+1}/l_k`. Counting from the capillary end (`j = N − k`):

    N_k = n^k,   r_k = r_c β^{−j},   l_k = l_c γ^{−j}

    B ∝ n^N                                  (metabolic rate ∝ terminal units)
    M ∝ V = Σ_k n^k · π r_k² l_k             (mass ∝ blood volume)

Substituting, `V = π r_c² l_c n^N Σ_{j=0}^{N} (n β² γ)^{−j}`. When `n β² γ < 1`
the sum is dominated by `j = N` and `V ∝ (β²γ)^{−N}`, so

    B ∝ M^θ    with    **θ = ln n / (−ln(β²γ))**                        (★)

This is exactly the floor-4 signature named in FLOORS.md §4 — log(multiplicity
per level) over log(rescaling per level), the same form as `ln N / ln b` and
S5's measured `ln n₀ / ln(t+1)`. With WBE's ratios (space-filling
`γ = n^{−1/3}`, area-preserving `β = n^{−1/2}`): `β²γ = n^{−4/3}` and θ = **3/4**,
with `n` cancelling identically.

### Where a Φ could enter, and the trap to avoid

The naive version of P-D is unfalsifiable, because *WBE's own derivation contains
an optimization* — the branching ratios are selected by minimizing dissipation /
matching impedance. Optimization over a measure is floor 2 ([P-C](../../invariants/FLOORS.md)),
so "there is no variational principle here" is simply false and would be a
strawman.

The claim is therefore stated in the only form that can fail:

> **The map (cost functional) → θ factors through the two ratios (β, γ), and the
> second half of that map — (β,γ) → θ — is (★), a log-ratio with no cost, no
> energy scale, and no conjugate variable in it.**

A floor-2 exponent is a *derivative of a free energy with respect to a natural
parameter*: it moves when the exchange rate moves, and its second derivative is a
variance. A floor-4 exponent is a ratio of two logs of integers. The legs below
separate these.

---

## Registered predictions

**P1 — the exponent is (★), exactly.** For `n ∈ {2,3,4,6,10}` and several ratio
schemes, the measured log-log slope of B vs M over `N ∈ [200,300]` matches (★)
within **0.5%**. Registered further: because the volume sum is *geometric*, the
finite-N residual decays **exponentially** in N, not as 1/N — except in the
marginal case `n β² γ = 1`, where it is exactly `ln(N+1)/(N ln n)`.

**P2 — n-invariance under the WBE rules.** With `β = n^{−1/2}`, `γ = n^{−1/3}`,
measured θ = 3/4 for every `n`, with spread across `n` below **0.005**.

**P3 — Φ-blindness of the magnitudes (the negative).** Scaling any of
`{r_c, l_c, blood density ρ, viscosity μ, pressure drop ΔP, per-capillary
metabolic rate B_c}` over **six decades** changes θ by **exactly 0** (relative
change < 1e-12), *including* when those quantities are fed to the optimizer that
selects β. Registered contrast: the *structural* exponent of the flow law (the
`a` in `R ∝ l/r^a`) **does** move θ, and moves it exactly through (★). Magnitudes
never matter; integer/structural counts always do — that is the scheme-layer
signature, and it is the opposite of a Legendre exchange rate, which is set by
magnitudes.

**P4 — the optimization route does not produce 3/4.** Minimizing Poiseuille
dissipation at fixed volume selects Murray's law `β = n^{−1/3}` (verified by
direct numerical optimization to <0.5%), which gives θ → **1**, not 3/4.
Registered finite-N form: θ_N = 1 − ln(N+1)/(N ln n), approached **from below**.
Impedance matching (`Y ∝ r²`) selects `β = n^{−1/2}` → θ = 3/4. So the exponent is
set by *which* ratio is selected; 3/4 requires the non-dissipative ingredient.

**P5 — cost-functional factoring (the sharp form of P-D).** For a third,
*invented* cost with no biological standing — minimize dissipation at fixed total
wall **surface area**, giving `β = n^{−2/5}` — the measured θ equals (★) evaluated
at the optimizer's own β within **0.5%**, i.e. **0.882**. Three costs, three β,
three θ, and in every case θ is recovered from (β,γ) alone with the cost, the
viscosity and the flow rate absent. Falsifier: a cost whose θ is *not* (★) at its
own optimizer's ratios — that would mean the functional enters the exponent
directly, which is what a floor-2 reduction would look like.

**P6 — mixed regions follow a parameter-free hyperbola.** With a fraction `f` of
levels (capillary side) on Murray ratios and `1 − f` area-preserving,
θ(f) = **3/(4 − f)**: no free parameters, n-independent, within **2%** for
f ∈ {0, 0.25, 0.5, 0.75} at N ∈ [200,300]. Registered because it is a shape a
log-ratio predicts and an exchange-rate account has no reason to produce.

**P7 — an independent geometric route reaches the same exponent with a different
mechanism.** Efficient directed supply networks (Banavar-style) serving N sites at
constant density in d dimensions have total flow-volume `C = Σ_links I ∝
N^{(d+1)/d}`, hence θ = d/(d+1) = **0.667 / 0.750 / 0.800** for d = 2, 3, 4 —
measured within **3%** by minimum-spanning-tree construction. No energetics, no
vessels, no Φ: the exponent is a ratio of *dimension counts*. If this holds, 3/4
has two independent derivations that share nothing but the log-ratio form.

**P8 — the Φ attempt fails in a specific, measurable way.** Build the honest
exponential family: statistics `x = (ln M, ln B)` over the network family,
natural parameters `λ`, `log Z(λ)`. Registered outcome:

- the covariance `∇² log Z` is **rank 1 for every λ** — correlation between
  ln M and ln B equal to 1 to < **1e-9** — over four decades of λ;
- the conjugate ratio `d⟨ln B⟩/d⟨ln M⟩` is **constant** in λ to < 1e-9;
- **control**: a genuine two-statistic exponential family (mean-field Ising with
  statistics (energy, magnetization), exact enumeration) shows correlation
  **< 0.99** and a conjugate ratio that moves by **> 10%** across its parameter
  range.

Reading registered in advance, so it cannot be chosen to fit: rank-deficiency
**everywhere** is a property of the description map (one index N pushed through
two observables), not a singularity of Φ located on a set. That is precisely what
distinguishes the proposed floor 4 from floor 3, whose support facts are
singularities *at a boundary* with Φ regular elsewhere. If instead the covariance
is full rank and the ratio moves, 3/4 is a Legendre exchange rate and **P-D is
dead**.

---

## What would kill P-D

- **P3 fails** — θ depends on an energy scale at fixed geometry. Then the
  exponent has an exchange rate and belongs on floor 2.
- **P5 fails** — some cost functional's exponent is not recovered by (★) from its
  own optimal ratios. Then the functional enters θ directly and allometry
  reduces.
- **P8 fails** — the covariance is full rank and the conjugate ratio moves with
  λ. Then 3/4 *is* a derivative of a log-partition function.
- **P7 fails** — if the dimensional route gives an exponent unrelated to d/(d+1),
  the "two independent geometric derivations" claim collapses and the case for
  the log-ratio signature rests on one model family.

## What this experiment cannot show

- It is a study of **models of allometry**, not of organisms. Nothing here tests
  whether real metabolic rates scale as 3/4 (that is the Kozłowski–Konarzewski
  dispute, and it is out of scope). The question is what *kind of object* the
  exponent is in the theories that produce it.
- Failure to find a Φ is not proof none exists. P8 is therefore stated as a
  measurement (rank, constancy) rather than as a non-existence claim.
- Urban scaling (#9's other instance) is untouched.
