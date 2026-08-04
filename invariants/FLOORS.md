# The catalog, sorted by floor

*2026-07-25. The P0 that outlived three syntheses.*

[`derivations/symmetry-sector.md`](../derivations/symmetry-sector.md) derived the
map's architecture: not sectors side by side but **one tower, three floors**.

```
  FLOOR 1  symmetry / conservation  →  chooses Φ's coordinates (which quantities exist)
  FLOOR 2  Φ, regular part          →  prediction (∇Φ, ∇²Φ, Φ*, −Φ)
  FLOOR 3  Φ, singular part         →  boundaries (non-analyticity, degeneracy, supports)
```

> **⟳ 2026-07-29 — the tower gained a floor at the *bottom*, and it reorganizes
> this document twice.** [D10](../derivations/D10-composition-lens.md) found that
> floor 1 takes an input it never names — the symmetry group is *given*, and there
> is no outside to give it. Under it sits a **composition law** ⊎:
>
> ```
>   FLOOR 0  composition (the lens)  →  fixes what counts as two systems, hence Φ's
>                                        form, the charge list, and which charts pin
> ```
>
> Two consequences land in this file specifically. **(a) §4's live question is
> answered** — the general residue is the invariant content of the largest group ⊎
> fails to pin (see the note at the end of §4). **(b) §2's asymmetry gets a second
> reading**: since Φ is a cumulant generating function, "Φ is additive under ⊎" is
> one condition *per order*, and the orders at which it fails are the floors —
> order 0 → floor 2's Legendre face (Φ\* = concave hull ≠ s), order 2 → criticality
> and SSB, no order at all → heavy tails. Floor 3 stratifies because there is more
> than one way for a composition law to lapse. This does **not** replace D2's group
> argument or D6's q1/q2 classifier; whether the two indices are related is open.

Sorting the catalog against that architecture is a **test**, not bookkeeping: the
rule makes claims about entries nobody has examined, and an entry that refuses all
three floors is the tower's own falsifier #4. This document records the sort, what
it deletes, what it predicts, and what refused.

---

## 1. The sort

| # | Entry | Floor | Why |
|--:|-------|:-----:|-----|
| 23 | [free-energy hub](./free-energy-hub.md) | **2 + 3** | Not *on* a floor — it is the object the floors are floors of. Regular part = floor 2, singular part = floor 3. |
| 2 | [conservation & Noether](./conservation-noether.md) | **1** | Derived: charges are the natural parameters of long-time ensembles. The entry's own split holds — symmetry-induced conservation is floor 1; *bookkeeping identities* (double-entry) are **not floor 1 and not a Φ fact**, see §4. |
| 3 | [entropy & information](./entropy-information.md) | **2** ▸facet | Φ* — the Legendre dual. Literally a derivative-face of the hub. |
| 20 | [statistical geometry](./statistical-geometry.md) | **2**▸3 | ∇²Φ. The entry *spans* the 2/3 boundary: the metric is floor 2, its degeneration is floor 3. The bridge entry. |
| 15 | [duality & conjugates](./duality.md) | **2 + 1** | **Splits.** Legendre duality = Φ* = floor 2 (facet). Fourier / canonical conjugacy (position–momentum) is *symplectic* — a bracket, which Φ does not have — so it belongs to floor 1. |
| 17 | [universal update](./mirror-descent-update.md) | **2** ▸facet | −Φ is its Lyapunov function (S1, derived). |
| 12 | [selection & replicator](./selection-replicator.md) | **2** ▸facet | Same object as #17 (S1: replicator = MW = Bayes = Gibbs). |
| 16 | [information bottleneck](./information-bottleneck.md) | **2** ▸facet | Rate–distortion is a constrained-Φ / Legendre object. |
| 14 | [trade-offs & Pareto](./tradeoffs-pareto.md) | **2** ▸facet, partial | Where a trade-off has a real exchange rate, its frontier *is* a Legendre transform (rate–distortion). Where it doesn't, it is not an invariant at all (L1). |
| 4 | [diffusion & random walks](./diffusion-random-walks.md) | **2** (→3 in the tails) | Reduction demonstrated: CLT forces the Gaussian, the Gaussian is the max-entropy exponential family, and by JKO diffusion is gradient flow of that free energy. **Heavy-tailed/Lévy instances move to floor 3** — see prediction P-B. |
| 18 | [optimal transport](./optimal-transport.md) | **2** (+ open) | The *flow* is Φ-driven (JKO). But the Wasserstein *metric* is not ∇²Φ — a second geometry on the same space, not derived from Φ. Flagged, §4. |
| 6 | [feedback & control](./feedback-control.md) | **2 + 3** | **Splits, derived** ([S27](../derivations/S27-control-split.md)): inference half (LQG↔Kalman, KL-control, min control energy = Φ*) is floor 2; binary reachability is floor 3 (supports, null Fisher). |
| 7 | [optimization & variational](./optimization-variational.md) | **2 + 1** | **Splits by what the functional is over.** Objective = a free energy ⇒ floor 2. Objective = an *action* (least action) ⇒ floor 1, since that is the bracket structure Noether consumes. "As-if" optimization (adaptationism, utility) is neither — L1. |
| 5 | [criticality & universality](./criticality-phase-transitions.md) | **3** | Lee–Yang: transition ⇔ non-analyticity of Φ. The floor's L4 core. |
| 10 | [symmetry breaking](./symmetry-breaking.md) | **3** | Derived, and the sort's best non-trivial case: an entry *named* for symmetry lands on floor 3, because SSB requires a non-analyticity of Φ and Goldstone modes are null directions of ∇²Φ. |
| 1 | [power laws](./power-laws.md) | **3** | Heavy tails are where Z or its moments diverge — the complement of the well-behaved exponential-family world. |
| 8 | [networks & percolation](./networks-percolation.md) | **3** | Connectivity facts are Φ-boundary facts (S27); the Potts q→1 non-analyticity is systematic, not dressing. |
| 22 | [critical slowing down](./critical-slowing-down.md) | **3** | Tested ([S7](../experiments/S7-critical-slowing/)): τ·λ_min = 0.94±0.13 — the Hessian going soft, i.e. the *approach* to the singular set. |
| 21 | [noise thresholds](./noise-thresholds.md) | **3 + 4?** | **Splits, tested** ([S5](../experiments/S5-noise-thresholds/)): type M (metric merge) and type S (support loss) are floor 3; **type R (decoder RG fixed point) is not a Φ fact at all** — see §4. |
| 19 | [spectral gap](./spectral-gap.md) | **3** ✓tested | The sort's prediction, [run and confirmed](../experiments/PA-spectral-gap/) — but in the *directional* form: gap-closure is a **null direction** of the trajectory free energy's Hessian, not a scalar divergence. See P-A below. |
| 13 | [emergence & renormalization](./emergence-renormalization.md) | **none — an operation** | RG is not a fact *inside* Φ; it is a map that carries Φ at one scale to Φ at another. [S25's channel law](../experiments/S25-channel-independence/) measured exactly this: F_c(T) = F_eff(T′)·(dT′/dT)². See §4. |
| 9 | [scaling & allometry](./scaling-allometry.md) | **refuses** ✓tested | The exponent is θ = min(1, ln n/−ln(β²γ)) — a log-ratio of the branching data, blind to every energy scale. [Run and confirmed](../experiments/PD-allometry-reduction/); see P-D below. |
| 11 | [fractals & self-similarity](./self-similarity-fractals.md) | **3 + 4?** | **Splits.** Statistical self-affinity at a critical point is floor 3. *Deterministic* self-similarity of a constructed hierarchy is scheme structure — and its dimension has the same form as the type-R exponent, §4. |

**Legend.** ▸facet = not an independent invariant; a derivative-face of #23.

---

## 2. What the sort deletes — and what it doesn't

**On floor 2, redundancy deletion succeeds.** Seven entries (#3, #12, #14, #15
Legendre half, #16, #17, #20) are ∇Φ, ∇²Φ, Φ*, or −Φ of *one convex function*.
They are not seven invariants that happen to agree; they are one function
differentiated seven ways. The catalog should stop counting them separately, and
the domain matrix should stop treating their per-domain cells as independent
evidence.

**On floor 3, redundancy deletion fails — and that is the more interesting
result.** Criticality, power laws, percolation, SSB, critical slowing down and the
noise thresholds are *all* "Φ goes singular," but they are **different
singularities**: non-analyticity, divergent moments, null Hessian directions,
support loss, soft modes. [S5](../experiments/S5-noise-thresholds/) showed these
carry *different exponents* — metric merge gives 2, support loss gives 1 — so they
cannot be collapsed into each other.

> **⟳ Update (2026-07-26, [D1](../experiments/D1-chart-invariance/)).** The
> classification this section called open work now has a partial answer, and a
> correction to how the exponents were being read. A degeneracy-type floor-3
> singularity carries **two** numbers: the **chart order** *k* (λ ~ ε^k in
> whatever coordinate the domain supplies) and the **degeneracy order** *p* (first
> non-vanishing anharmonic term of Φ). ***k* is gauge** — removed by inference
> across two fields and by explicit reparameterization — and ***p* classifies**,
> via λ_c ~ D^{(p−2)/p} on the noise-rounding crossover. So the exponent spreads
> S5 and S7 reported as "domain-specific" are largely a **chart artifact**: in the
> bare chart a fold (p = 3) and a tricritical point (p = 6) agree to three decimals
> while a fold and an SIS epidemic — the same degeneracy — differ by 2×.
> **Scope, and it matters here:** this classifies the part of floor 3 where Φ has a
> Taylor expansion. **Support loss has no *p*** — S5's type S is precisely a
> boundary rather than a degeneracy — so the stratification of floor 3 is now
> "degeneracy-type, indexed by *p*" plus "everything else, still unclassified"
> ([D6](../questions/UNKNOWN-LAWS.md)). Redundancy deletion still fails on floor 3;
> it is now failing in a countable way.
>
> **⟳ Extended (2026-07-27, [D6](../experiments/D6-support-singularities/)): *p*
> was a special case, and the "everything else" above is now nearly empty.**
> Writing Φ's two leading terms at the singular point as A|y|^{q1} + B|y|^{q2}
> with A → 0, the crossover locus is **A_c ~ D^{1 − q1/q2}**, and:
>
> ```
>    q1 = 2      what SMOOTHNESS forces   ->  D1's degeneracy order, exponent (p-2)/p
>    q1 = 1      a kink or a boundary     ->  support loss (S5's type S)
>    q2 -> oo    a hard wall              ->  exponent 1  (measured 0.9979)
> ```
>
> So support loss is not p = ∞ — that would be a value in the q2 slot — but a
> different value in the *q1* slot, and M/M/1 with an infinite buffer has **no
> second term and therefore no crossover at all** (kurtosis pinned at 6.0000 over
> four decades). **Floor 3's classifier is the ratio q1/q2**, which is exactly the
> form [D2](../derivations/D2-gauge-of-the-tower.md) derived the chart-free
> residue must take; D2's "residue = codimension p − 2" is its smooth-case face.
> The unclassified remainder is now **essential singularities only** — Φ with no
> leading power at all.

So the asymmetry, which the original "one object seen sideways" slogan could not
express:

> **Floor 2 collapses. Floor 3 stratifies.**

The regular part of Φ is one function seen from several angles. The singular part
is a *classified set* of ways for a prediction field to end, and classifying them
is open work rather than deletion.

**Net effect on the count.** The bins, non-overlapping, summing to 23:

| Bin | Entries | n |
|-----|---------|--:|
| the hub itself | #23 | 1 |
| floor 1 only | #2 | 1 |
| floor 2, ▸facet | #3, #12, #14, #16, #17, #20 | 6 |
| floor 2, not a facet | #4, #18 | 2 |
| floor 3 only | #1, #5, #8, #10, #19, #22 | 6 |
| splits across floors | #6, #7, #11, #15, #21 | 5 |
| refuses the tower (§4) | #9, #13 | 2 |

Six whole entries are deleted as independent, and #15 survives only in its
symplectic half — **seven facet-faces of Φ in total**. Effective independent count:
**23 → ~16**. A real simplification, and a smaller one than "much of the map is
one object" implied: the deletion is confined to floor 2, which is exactly the
asymmetry above.

---

## 3. What the sort predicts (the part that makes this a test)

Each prediction is about an entry the sort had no hand in shaping.

**P-A — spectral gap (#19) — ✓ RUN, [`experiments/PA-spectral-gap/`](../experiments/PA-spectral-gap/).**
*Predicted:* gap-closure is the ∇²Φ degeneracy; the entry's four readouts are one
number because they are the softest direction of one Hessian; joins S7's
τ·λ_min = 1 from the connectivity side.
*Found:* the floor assignment holds with Φ fixed in advance — the slow mode comes
to carry the entire divergence of Λ''(0) (Λ''·gap = 2⟨f,v₂⟩² = 2.0000) — **but the
scalar reading is wrong**: for an observable orthogonal to the slow mode Λ'' is
unchanged (1.00×) while the gap falls 31×. Gap-closure is a **null-direction**
fact, filing #19 with S27's unreachable null spaces rather than with S3's
scalar blow-up. Three of the four readouts turned out to be one number *by
construction* and tested nothing; the fourth (Kuramoto) gives one mechanism with
**family-specific constants** (0.410–0.632) — the S7/S5 shape again. And the
listed falsifier **fired** against the naive reading: in a double well the gap
falls 3540× while the local curvature *rises* 6×, which cost S7 a boundary
condition (**its law is single-basin**). One registered threshold failed as
written: I predicted >2× across-family spread; it is 1.54×.

**P-B — diffusion splits at finite variance (#4).** Normal diffusion is floor 2
(Gaussian = max-entropy exponential family); Lévy/anomalous diffusion is floor 3
(divergent moments = Φ misbehaving). The boundary is exactly finite-vs-infinite
variance. **This retrodicts a result already in the repo**: the
[transfer cliff](../experiments/ladder-vs-transfer/) sits at precisely that line,
measured before the tower existed. **Falsifier:** a finite-variance diffusion whose
Φ is non-analytic in the relevant variable, or a heavy-tailed one whose moments
behave.
*(⟳ 2026-07-29: P-B is no longer a separate prediction. Under
[D10](../derivations/D10-composition-lens.md)'s reading it is the **order-2 clause**
of one condition — finite variance is "the second cumulant is extensive," and
infinite variance is "there is no order-2 statement to make." Measured: an
α = 1.5 stable sum has δ₂ wandering over −0.39…−2.93 with across-seed spread
1.8…7.4, against a Gaussian control at 0.00 ± 0.03. The untested half of P-B — a
finite-variance diffusion with non-analytic Φ — stays untested.)*

**P-C — variational principles come in exactly two kinds (#7).** Over a measure
(free energy) ⇒ floor 2; over an action (bracket) ⇒ floor 1. **Falsifier:** a
genuine variational law — one that predicts, rather than re-describes — whose
functional is over neither.

**P-D — allometry does not reduce (#9) — ✓ RUN, [`experiments/PD-allometry-reduction/`](../experiments/PD-allometry-reduction/).**
*Predicted:* Kleiber's 3/4 should *not* be derivable from a partition function; it
should come out of branching geometry, making it scheme structure. *Falsifier
registered:* derive the 3/4 exponent from a Φ.
*Found:* **confirmed on every registered leg, and the exponent is now a law rather
than a slogan** —

    theta  =  min( 1,  ln n / ( -ln(beta^2 gamma) ) )

to 7.1e-11 over 22 (scheme, n) pairs, with n cancelling identically (spread
4.0e-15 across n = 2…10). Six decades on every dimensionful quantity move θ by
**1.1e-8**; the flow law's *structural* exponent moves it a lot. The strawman was
avoided by registering the claim in factoring form, since WBE's derivation does
contain an optimization: six cost functionals select six different β, and θ is
recovered from (β, γ) alone with the functional absent (≤1.5e-14 in five of six).
**The variational route gives the wrong number** — dissipation minimization yields
θ = 1 for Poiseuille and for every steeper flow law, reaching 3/4 only at
R ∝ l/r², which no viscous flow obeys. The Φ attempt fails in the registered way:
∇²log Z is **rank 1 for every λ** and the conjugate ratio is constant to 1.1e-13,
against a control that swings 151%. Independent second route: efficient supply
networks in d dimensions give θ = d/(d+1) (0.663/0.749/0.805 vs 0.667/0.750/0.800)
— a ratio of dimension counts. Two registered items failed and are on record: the
MST construction in leg D (its exponent barely depends on d; it minimizes wire
length, not transport cost) and the mean-field-Ising control in leg E, which is
itself degenerate for exactly the reason under study. Bonus: θ = min(1, ·) is
**non-analytic** at nβ²γ = 1, and Murray's law sits exactly on that kink.

**P-E — the fourth floor has a signature (§4).** See below.

---

## 4. What refused the tower — and the shape it makes

Five things refused floors 1–3, and they refuse it *the same way*:

| What | Where it came from | Its exponent |
|------|--------------------|--------------|
| Type-R noise thresholds | [S5](../experiments/S5-noise-thresholds/), measured | α = **ln n₀ / ln(t+1)** |
| Deterministic fractals (#11) | catalog | D = **ln N / ln b** |
| RG / coarse-graining (#13) | catalog + [S25 channel law](../experiments/S25-channel-independence/) | eigenvalues of the flow map |
| Bookkeeping identities (#2's second half) | catalog | — (conserved by construction) |
| Allometry (#9) | [P-D](../experiments/PD-allometry-reduction/), measured | θ = **min(1, ln n / −ln(β²γ))**; independently **d/(d+1)** |

**They share a signature: their invariant is a log-ratio — log(multiplicity) over
log(rescaling) — not a derivative of Φ.** The concatenated code's α = ln n₀/ln(t+1)
is *literally of the same form* as a fractal dimension ln N/ln b: multiplicity per
level over rescaling per level. This was not designed; S5 measured that exponent
before the sort noticed what it was.

**Two of the five are now measured rather than asserted, and the second was a
prediction.** S5's α was measured before the bin existed; [P-D](../experiments/PD-allometry-reduction/)
was run *because* the bin predicted allometry would land in it, and allometry's
θ = ln n/−ln(β²γ) is the same form again. Three things separate that from a
Φ-derivative, all of them now measurements rather than intuitions: the exponent
is **blind to magnitudes** (1.1e-8 over six decades of six quantities) while
responding to structural counts; a cost functional enters it only by *selecting*
the scheme, never directly (six functionals, ≤1.5e-14 residual); and the honest
exponential family's ∇²log Z is **rank 1 for every parameter value**, so there is
no conjugate pair for the exponent to be an exchange rate between.

That last point also sharpens the **floor-3 / floor-4 boundary**, which had been
a matter of taste. Floor 3's support facts are singularities *located on a set*,
with Φ regular elsewhere. The scheme layer's degeneracy is rank deficiency
**everywhere in parameter space** — the signature of one index pushed through two
observables, i.e. of the description map itself. That is a measurement (rank of
∇²log Z as a function of λ), not a preference.

What unites them conceptually is that each is a fact about **the map between
descriptions** — the encoding, the coarse-graining, the recursion — rather than
about the system's prediction field. RG is the general form of such a map; a code
is a designed one; a deterministic fractal is one's fixed point; double-entry
accounting is a trivial one, conserving *because of the representation*, exactly
as a code's redundancy does. That is why the catalog's oldest embarrassment
(accounting "conservation" that isn't Noether) and the newest result (S5's type R)
land in the same bin.

**Proposed floor 4 — the scheme layer:** invariants of the description map, whose
signature is a log-ratio exponent rather than a Φ-derivative. This is a
**proposal, not a result.** It is exactly the tower's falsifier #4 (an invariant
reducible to none of the three floors), so if it stands the tower gains a floor.
*(⟳ Retired 2026-07-26 by [D2](../derivations/D2-gauge-of-the-tower.md) — kept as
written because the reason it fails is the result. Read the resolution below.)*

**P-E, its falsifier, two-sided:** (kills the floor) reduce a log-ratio exponent to
a Φ-derivative, or exhibit a scheme-layer invariant whose signature is a
Φ-derivative; (kills the *separateness*) show the scheme layer is floor 1 in
disguise — a code *is* a redundancy chosen to be invariant under the noise, and
"invariance selects the coordinates" is precisely floor 1's job. **The second
horn is the live one**, and deciding it is now the map's sharpest architectural
question. *(⟳ Both horns are now answered — the second by
[P-D](../experiments/PD-allometry-reduction/), the floor itself by a third horn
neither anticipated. Below.)*

**First evidence on the live horn, from P-D — and it points to *takes input from*
rather than *is*.** Allometry's two ratios are selected by conditions that are
plainly floor-1-flavoured: impedance matching is a reflectionless (flux-matching)
condition, and space-filling is a geometric constraint. So the scheme layer does
draw its parameters from invariance arguments, which is what the second horn
predicted. But floor 1's job is to choose *Φ's coordinates*, and here there is no
Φ downstream at all — the log-ratio is terminal, and the run showed no conjugate
pair exists for it to be an exchange rate between. Evidence for separateness, not
a settlement: one instance, and the argument that floor 1 must terminate in a Φ
is a claim about the tower rather than a measurement.

> **⟳ RESOLVED 2026-07-26 — the third horn is the right one.** Worked in
> [`derivations/D2-gauge-of-the-tower.md`](../derivations/D2-gauge-of-the-tower.md)
> and [`experiments/D2-gauge-group/`](../experiments/D2-gauge-group/).
> **There is no fourth floor.** Writing **G_diff** for reparameterizations smooth
> *at* the singular point and **G_pow** for φ(ε) ~ ε^a (smooth away from it, not
> at it), the floors are defined up to G_diff while cross-domain comparison has
> only G_pow — and **the scheme layer is the difference between the two.** RG
> eigenvalues are G_diff-invariant by conjugation (5.3e-15) and G_pow-covariant
> as y → a·y (≤2.4e-12): identical behaviour to D1's chart order, so all five
> rows of the table above are one object, the transformation datum of G_pow
> modulo G_diff. A transformation parameter is not a fact on any floor, which is
> why they refused, and why five unrelated things shared one signature.
> **The chart-free residue is the codimension p − 2** — signs, counts and ratios
> being three faces of it — measured as β/k = 0.5000 (p = 4) and 0.2503 (p = 6)
> against 1/(p−2). So the refusers dissolve into gauge plus floor 3, and what was
> under them was [D1](../experiments/D1-chart-invariance/)'s degeneracy order.
> **This section's asymmetry (§2) also stops being a bare observation:** away from
> the singular point G_pow = G_diff, so floor 2 lives under the smooth group where
> tensors have real invariants and collapses; at the singular point the group
> enlarges, eats exponent magnitudes, and leaves a discrete residue — so floor 3
> stratifies. Load-bearing caveat: the ratios require the **common-a** commitment
> (one distance-to-threshold per singularity, not one per eigendirection); under
> independent re-charting only signs and counts survive.
>
> *The original statement of the horn follows, unedited.*
>
> **⟳ A third horn, opened 2026-07-26 ([D2](../questions/UNKNOWN-LAWS.md)).**
> Neither a floor nor floor 1: **the gauge group.** D1's chart order is
>
> ```
>         k  =  d ln λ / d ln ε
> ```
>
> log-response over log-rescaling — *the signature in the table above, exactly*.
> On that reading a fractal dimension is the chart order of a self-similar map, an
> RG eigenvalue the chart order of the coarse-graining map, S5's type-R exponent
> the chart order of a decoder recursion, and double-entry accounting the
> degenerate case k = 0, conserving because the chart is constant. That would
> explain both facts this section found puzzling: why they refused floors 1–3 (a
> gauge parameter is not a fact on any floor) and why four unrelated objects
> carried the *same* signature, which a genuine new floor has no reason to
> produce.
> **[D1](../experiments/D1-chart-invariance/) supplies the removability half**:
> under an explicit reparameterization ε′ = ε^a the chart order changes while every
> λ-chart exponent is unmoved to four decimals. **It does not supply the rest**,
> and the counter-horn is real: an RG eigenvalue *predicts which perturbations are
> relevant*, and it is not obvious that predictive work survives being called
> gauge. If it does, the P0 **dissolves** rather than resolving — there is no fourth
> floor, only a coordinate freedom the first three were always defined up to.
> Unworked; now the map's most valuable question.

> **⟳ Reconciliation (2026-07-27) — how P-D and D2 fit.** They were run on
> parallel branches and neither pass saw the other, so this note states the
> relation rather than adding a result.
> **They agree on the negative and differ only on what to call the remainder.**
> P-D killed the *second* horn from the measurement side (the scheme layer takes
> input from floor 1 without being it); D2 retired the *fourth floor* from the
> structural side. So "evidence for separateness" above should be read as
> **separate from floors 1–3** — which both passes support — and not as "is a
> fourth floor", which D2 retires. The "Proposed floor 4" paragraph and P-E's
> two-sided falsifier are superseded in that order.
> **The fit is closer than bare compatibility:** P-D's three negatives are the
> signature D2's reading predicts. An exponent **blind to magnitudes** (1.1e-8
> over six decades), reached through a cost functional that only *selects* the
> scheme, with **∇²log Z rank 1 for every λ** so that no conjugate pair exists,
> is what a transformation parameter looks like — a quantity with no conjugate is
> not an exchange rate on any floor. What P-D measured as *terminal*, D2 derived
> as *gauge*.
> **Left open, and not claimed by either pass:** P-D's θ = min(1, ln n/−ln(β²γ))
> is non-analytic at nβ²γ = 1, while D2's chart-free residue is a discrete
> codimension. Whether that kink is a floor-3 degeneracy read in a scheme
> variable, or a fact about the description map with no floor-3 counterpart, is
> untested — flagged here for whoever takes the next pass.
>
> **⟳ Leg F (2026-07-27, later the same day) — the reconciliation above is right
> except in one sentence, and the correction is a measurement.** The note says
> *"what P-D measured as terminal, D2 derived as gauge."* Measured, θ is **not**
> gauge. D2's own §4 table puts an exponent's *magnitude* in the gauge column and
> a **ratio** of exponents in the invariant one — and θ is a ratio of two
> per-level log-quantities, so the table already predicts which column it lands
> in. The rest of that note stands: P-D's three negatives really are the
> signature D2's reading predicts, and "separate from floors 1–3, not a fourth
> floor" is the right reading of the negative.
>
> **What leg F measured.** θ is a **ratio** of two per-level
> log-quantities, and D2's own §4 table puts ratios in the invariant column.
> Coarse-graining the scheme by `a` levels (n → nᵃ, β → βᵃ, γ → γᵃ) raises
> numerator and denominator to the same power and leaves θ **invariant to
> 2.6e-15** across a = 1…8, while the bare per-level chart ln n moves **8×**. The
> same estimator on a genuine floor-3 chart reports k moving **3.0×**, tracking
> 1/a — so the invariance is a fact about θ, not a blind estimator.
> **And G_pow is not available here in the first place.** D2's freedom exists
> because a distance-to-threshold carries no canonical scale. Mass does: it is
> **extensive**, and under M → M^a with a ≠ 1 masses stop adding (additivity
> defect 0 at a = 1; 29% / 50% / 41% at a = 1.5 / 2 / 0.5 for equal-depth
> sub-networks). Extensivity pins the chart to G_diff, where by D2's rule (i)
> exponents are invariant.
> **Net: the two results compose.** The scheme layer is the structure group, as
> D2 says; allometry's 3/4 is in its **invariant residue**, not its gauge part —
> alongside the codimension p − 2, and for the same reason (both are ratios).
> What P-D called "the floor-4 signature" should be read as *the residue*, and
> the entry is corrected accordingly. One thing P-D observed survives the
> reframing intact: allometry's ratios are selected by floor-1-flavoured
> conditions (impedance matching is flux-matching, space-filling is geometric),
> which is now unsurprising — selecting a scheme is exactly what a structure
> group's parameters get chosen by.
> **Still open:** the residue has two known members (p − 2 from a singularity,
> θ from a branching scheme) and no statement of what the general one is. D2
> derived its residue for floor-3 germs; allometry has no singularity and no Φ at
> all, so "the residue is the codimension" does not cover it. That gap is now the
> live question in this section.
>
> **⟳ ANSWERED 2026-07-29 by [D10](../derivations/D10-composition-lens.md) — and the
> answer is not in Φ, which is why staring at Φ never produced it.** What decides
> the group is a fact about **composition**, not about the singularity:
>
> > **A chart is pinned to G_diff when its variable is additive under system
> > composition, or dual to one. It keeps G_pow when neither holds. The residue is
> > the invariant content of the largest group the composition law fails to pin.**
>
> On that rule the two members stop being a list: where composition pins the chart
> the exponents *themselves* are facts (allometry's θ — mass is additive, leg F's
> defect 0 at a=1 and 29–50% otherwise); where it does not, only ratios, signs and
> counts survive (p − 2, and D6's q1/q2). **Two branches of one rule, and which
> branch you are on is a floor-0 question.**
> The audit that established this
> ([D10 §6](../experiments/D10-composition-lens/)) **forced a correction to the rule
> as first written** — reduced temperature is intensive, so by additivity alone its
> exponents should be gauge, and inside physics they are facts; the "or dual to
> one" clause is D2 §7's own reason ("enters the Hamiltonian linearly") restated,
> since energy is additive and β is its conjugate. It also passed a row it was not
> designed for: the RLCT is read off the coefficient of ln n, **samples are
> additive**, so λ should be a fact — and it independently is one (a birational
> invariant).

> **⟳ CLOSED 2026-07-27 by [D7](../questions/UNKNOWN-LAWS.md) — and it corrects
> one sentence above.** Derivation:
> [`derivations/D7-the-residue.md`](../derivations/D7-the-residue.md); numerics:
> [`experiments/D7-residue-projective/`](../experiments/D7-residue-projective/).
>
> **The residue is the log-slope vector modulo the *diagonal* ℝ⁺.** Write
> y_i = d ln O_i/d ln ε for the log-slopes of observables along the one control
> family. Relabelling the family multiplies **every** component by the **same**
> scalar, so the chart-free content is the ray through y — the point of ℝP^{n−1} —
> and concretely it is the set of slopes of observables against *other*
> observables, d ln O_i/d ln O_j, in which no chart appears. Eliminating the chart
> and taking the projective quotient are one operation done in the two directions.
> **All three members are that invariant on three slope vectors:** D2's
> β/k = 1/(p−2), D6's q1/q2 fixed by d ln A_c/d ln D, and P-D's θ = d ln B/d ln M.
> One estimator, unmodified, returns 0.4996 / 0.2483 on smooth germs, D6's table
> exactly on support-type potentials, and 0.7495–0.7500 on the branching scheme —
> the case with no singularity, no Φ and a discrete chart, which is the one that
> decides whether this is a general statement or a physics statement wearing one.
>
> **The correction: "the chart-free residue is the codimension p − 2" is the
> smooth case's arithmetic, not the residue's.** A projective space has no
> distinguished rational points; D2's integer comes from Taylor orders being
> integers once smoothness forces q1 = 2. Measured counterexamples:
> Φ = A|y|² + |y|^{2π} gives **0.68169** (= 1 − 1/π) and a germ with p = 2 + √2
> gives **0.70698** (= 1/√2). Read the D2 block above as *the residue of a smooth
> floor-3 germ is p − 2*, which is true, and not as *the residue is an integer*,
> which is not.
>
> **Two things the general form buys that no member did.** (i) A **count**:
> n observables give exactly n − 1 independent invariants, the Π-theorem with the
> chart as the single dimension. Measured at n = 5 for the first time — the slope
> vectors span a line, σ₂/σ₁ = 2.96e-3 — where every previously known member has
> n = 2 and therefore exactly one invariant. (ii) D2's **common-*a*** commitment
> stops being a stipulation: it says the action is the diagonal, which is what "one
> singularity, one family" means, and under the product group the orbits are the
> whole orthant so only signs survive. Exhibited on the same observables with the
> same estimator: σ₂/σ₁ = 2.19e-3 diagonal vs 0.227 product, signs unchanged in
> both.
>
> **And P-D's kink resolves.** The reconciliation left open whether the
> non-analyticity of θ = min(1, ln n/−ln(β²γ)) at nβ²γ = 1 is a floor-3 degeneracy
> read in a scheme variable. It is not: it is where the two log-slopes are *equal*,
> the point [1 : 1] of ℝP¹ — a wall in the residue's own space. The min emerges
> from the exact finite sum rather than being imposed (RMS 5.6e-9 against the
> min-form), the wall locates at x = 1.00012, and it is chart-invariant.
> **Scope, unchanged:** essential singularities remain outside, every model is 1-D
> or separable, and three registered tolerances were missed to the finite-window
> error budget — all logged in the experiment's §4.

One more honest flag: **optimal transport (#18)** puts a *metric* on distribution
space that is not the Fisher metric and is not derived from Φ. It is not a
log-ratio object either, so it fits neither the three floors nor the proposed
fourth. Either it reduces (Otto calculus relates the two geometries) or it is a
second, unrelated exhibit against monism. Unresolved, and recorded as such.

---

## 5. Boundaries of this sort

- The tower is derived for **equilibrium / long-time (stationary)** prediction
  fields. Every floor-1 assignment inherits that restriction.
- Assignments for `seed`-status entries are *predictions*, not findings. Only
  #6, #9, #10, #19, #21, #22 and the #4 reduction rest on a derivation or an
  experiment; the rest are the sort's claims and can be wrong. Two of those —
  #19 ([P-A](../experiments/PA-spectral-gap/)) and #9
  ([P-D](../experiments/PD-allometry-reduction/)) — were `seed` entries the sort
  made claims about and have since been run, so the sort has now been graded
  twice: once on a positive (confirmed, in a corrected form) and once on its only
  negative (confirmed).
- P-D tests **models** of allometry, not organisms. It establishes what kind of
  object the exponent is in the theories that produce it, and says nothing about
  whether real metabolic rates scale as M^(3/4).
- "Refuses the tower" is a statement about the reductions **attempted here**. A
  successful reduction of allometry or OT would move them, and that is a cheaper
  result than a new floor.
- The sort does not touch per-domain levels in
  [`../domains/README.md`](../domains/README.md); floors and ladder levels are
  orthogonal axes (a floor-3 entry can be L4 in physics and L1 in finance).
