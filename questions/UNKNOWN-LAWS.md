# Unknown laws — the discovery register

*Opened 2026-07-26. A third register, alongside
[`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md) (rigorous cleanups),
[`SPECULATIVE.md`](./SPECULATIVE.md) (cross-domain stones) and
[`L3-MECHANISMS.md`](./L3-MECHANISMS.md) (candidate shared mechanisms).*

---

## 1. Why a third register

Seven cycles in, it is worth naming what this project has actually been doing.

Every stone in [`SPECULATIVE.md`](./SPECULATIVE.md) has the same shape: **take a
law that is already known in field A, and ask whether the thing that looks like it
in field B is the same object.** S1 asks whether the replicator equation is Bayes.
S3 asks whether the Fisher metric is the Ruppeiner metric. S5 asks whether Shannon
capacity is Eigen's error threshold. S13 asks whether grokking is Lee–Yang. Even
the architecture results — the tower, the floors — are a *sorting* of known
invariants into a structure.

That is **recognition**, and it has been productive: it produced the hub, the
tower, the transfer cliff, and five arrivals at the singular set of ∇²Φ. But
recognition can only ever return laws that someone already wrote down. Its
ceiling is the union of the textbooks.

This register is for the other operation: **discovery** — finding a law that is
not in any of the textbooks, in any field, because nobody has stated it.

The distinction is not about difficulty or grandeur. It is about where the
candidate comes from:

| | Recognition | Discovery |
|---|---|---|
| Candidate source | a named law in some field | an unexplained residue in our own measurements |
| The question | "are A and B the same object?" | "what is this number?" |
| Success looks like | a level on the ladder | a relation nobody has written |
| Failure mode | universality inflation | rediscovery, and tautology-by-construction |
| Register | [`SPECULATIVE.md`](./SPECULATIVE.md) | here |

**Both strokes stay.** Discovery without recognition is crankery — you cannot know
your law is new if you do not know the literature. The two registers are the same
expansion⇄restraint engine pointed at different targets.

---

## 2. The novelty ladder

The [rigor ladder](../METHODOLOGY.md) grades how well a correspondence is
established. It says nothing about whether the claim is *new*, because until now
every claim here was, by construction, old. A discovery register needs the second
axis, and it needs it to be as unforgiving as the first, because "nobody has said
this" is exactly the kind of assertion that breadth makes cheap and dangerous.

| Level | Name | What it means | The burden |
|---|---|---|---|
| **N0** | Restatement | The claim is a known law in different words. | — |
| **N1** | Recombination | Known laws from ≥2 fields, correctly composed. The composition is new; every part is old. | Name the parts. |
| **N2** | New relation | A relation between measured quantities that is not derivable from any single field's standard results, though each quantity is standard. | Show the quantities are standard *and* the relation is not in the field that owns either one. |
| **N3** | New object | A quantity nobody measures, which does predictive work. | The quantity must be operationally defined and independently measurable. |

**Levels multiply, they do not add.** An N3 claim at L1 is a fantasy; an N0 claim
at L4 is a textbook. The target region is **N2–N3 × L2–L3**: a relation nobody has
written, established well enough to transfer. Anything claiming N2+ must carry an
explicit **prior-art note** naming where it would already live if it were old.

**Honest default: assume N0.** The base rate for "an AI noticed a new universal
law" is dominated by rediscovery. A candidate is N0 until someone has actively
tried to find it in the literature and failed. Record that search, including what
it *did* turn up — near-misses are the most useful thing a prior-art note contains,
because they usually reveal the special case that is known and locate exactly which
generalization is not.

---

## 3. Three discovery engines

Where do N2+ candidates actually come from? Not from staring at the catalog. From
three specific places, all of which this project has already stumbled into by
accident.

### Engine 1 — Residue mining

**Look at the numbers our own experiments produced that we did not predict and
have not explained.** Every experiment in this repo emits constants; most are
recorded and never revisited. An unexplained constant is a law with its statement
missing.

Precedent, all accidental:

- [S5](../experiments/S5-noise-thresholds/) measured the concatenation exponent
  ln n₀/ln(t+1) *before* anyone noticed it has the form of a fractal dimension.
  That observation is the whole of the [proposed fourth floor](../invariants/FLOORS.md) §4.
- [P-A](../experiments/PA-spectral-gap/) measured Λ''·gap → 2.0000. The 2 was not
  predicted; it turned out to be 2⟨f,v₂⟩².
- [S7](../experiments/S7-critical-slowing/) measured τ·λ = 0.94 ± 0.13 across three
  domains *and* three exponents that did not transfer. The repo filed the exponent
  spread as a negative result. **It is the positive result of [D1](#d1--the-chart-law-two-integers-classify-floor-3) below.**

**The protocol.** Sweep the repo's own `verdict.json` files for (a) constants that
were measured but not derived, (b) exponents recorded as "domain-specific" — that
phrase is where explanations go to die, and (c) quantities that were controlled
away rather than understood.

### Engine 2 — Gap prediction

**Ask the structure where it says something must exist, then go look.** A
classification with a hole in it is a prediction. The [tower](../SYNTHESIS.md) says
floor 2 collapses and floor 3 stratifies — so floor 3 has a classification and we
do not have it. That hole is an instruction.

This is the engine that is strongest here, because the tower was *derived* rather
than assembled, and derived structures have holes with shapes.

### Engine 3 — Negative space

**Catalog what is systematically absent.** The catalog records what recurs.
Nothing records what *never* recurs despite the opportunity — and a forbidden
region is as much a law as a populated one. Candidate absences worth checking:
no cross-domain relation in the repo has survived as a bare exponent; no invariant
in the catalog involves a third derivative of Φ; no floor-3 entry has a
domain-invariant amplitude *and* a domain-invariant exponent at once.

---

## 4. Anti-patterns specific to discovery

The [methodology's list](../METHODOLOGY.md) covers recognition's failure modes.
Discovery has its own, and they are worse, because there is no field-expert to
object.

- **Rediscovery in unfamiliar notation.** The single most likely outcome. The
  antidote is the prior-art note, written *before* the excitement.
- **Tautology by construction.** Building the systems that exhibit the law, then
  reporting that they exhibit it. [P-A](../experiments/PA-spectral-gap/) caught
  this in-flight — three of #19's four readouts were one number *by construction*
  and tested nothing. **Every D-stone must mark which of its predictions are
  analytic identities and which can actually come out wrong**, in the
  pre-registration, before the run.
- **Exponent fitting.** Two decades of range and a free exponent will fit
  anything. Same standard as the power-law trap: the exponent must be *predicted*,
  not fitted, and the prediction must be a number rather than a sign.
- **Grandeur inflation.** "A new universal law" is a sentence that should
  embarrass its author. State the law as the narrowest thing that is true —
  its domain of validity is part of the claim, not a caveat appended after.
- **Novelty laundering by generalization.** Taking a known special case and
  stating it with the constants removed. If the general form's only content is the
  known case, that is N0 with extra steps.

---

## 5. The register

Each stone: the claim, the novelty level with its prior-art note, the falsifier,
and the engine that produced it.

---

### D1 — The chart law: two integers classify floor 3

**Engine:** residue mining ([S7](../experiments/S7-critical-slowing/)'s discarded
exponents) + gap prediction (floor 3's missing classification).
**Novelty: N2 claimed; N0–N1 for the formula, N2 survives for the classification.**
**Status: ⟳ RUN 2026-07-26 — [`experiments/D1-chart-invariance/`](../experiments/D1-chart-invariance/).**

> **⟳ Restraint pass (2026-07-26):** *chart claim confirmed in the strong form;
> the formula deflated to N0–N1 exactly as the prior-art note warned.*
> *k* is removable **by inference** — a fold in population dynamics (k = ½) and an
> SIS epidemic (k = 1), anharmonic coefficients differing 3×, give bare exponents
> 0.667 vs 0.333 and λ-chart exponents **0.33333 vs 0.33333**; *g* enters the
> amplitude exactly as claimed (prefactor ratio 2.0801 measured at all nine noise
> scales vs 3^{2/3} = 2.0801 predicted) — and **by manipulation**: under ε′ = ε^a
> the bare exponent moves by exactly a while the λ-chart exponent does not move at
> all. Both **at-risk** legs pass: full all-orders models give 0.4961 (p = 4) and
> 0.6635 (p = 6) against 0.5000 and 0.6667. The bare chart **inverts** the
> classification — fold (p = 3) and tricritical point (p = 6) agree to three
> decimals while fold and epidemic, the *same* degeneracy, differ by 2×.
> **Deflation, declared in advance:** legs A and B are analytic identities inside
> a truncated normal form and are not evidence; the formula is the Ginzburg
> calculation for general *p*. What survives at N2 is the cross-domain
> classification and the removability of *k*. **One registered direction refuted**
> (P8's crossover is the large-D end, not the small-D end); its mechanism survived
> and gave a post-hoc D_× ~ δa³ law, measured at δa^3.211 — logged as a
> consistency check, not a result. Scope: 1-D gradient systems, additive noise,
> degeneracy-type singularities only; both at-risk legs are physics.

**The residue.** S7 measured one relation that transferred across three domains
(τ·λ_min = 0.94 ± 0.13) and three exponents that did not (−½ / −1 / −2). The repo
recorded the second half as a negative result — "critical slowing down is not one
scaling law" — and moved on. S5 produced the identical shape: one discriminator
that held (α = order of vanishing of χ²_sym) and exponents spanning 1.00 → 3.17.
P-A made it three: one mechanism, family-specific constants. **Three independent
passes produced the same asymmetry and none of them asked why.**

**The claim.** Because the exponent asymmetry is not a fact about domains. It is a
fact about *charts*.

A floor-3 singularity is approached along some control parameter ε that the domain
happens to supply — temperature, mutation rate, load factor, sample ratio. But ε
is a **coordinate choice**, and nothing in the physics picks it: ε' = ε^a describes
the same singularity for any a > 0. Under that reparameterization every exponent
measured against ε is divided by a. **A bare exponent is therefore not an
invariant of the singularity at all — it is a property of the chart.** What is
invariant is anything that survives reparameterization.

Write λ(ε) for the softest Fisher/Hessian eigenvalue, vanishing as λ ~ ε^k. Then:

> **D1.** A floor-3 singularity carries exactly two numbers. The **chart order**
> *k* — how fast the singularity is approached in whatever coordinate the domain
> supplies — is pure gauge and carries no cross-domain information. The
> **degeneracy order** *p* — the order of the first non-vanishing anharmonic term
> of Φ at the singular point — is the invariant, and it classifies. Every
> cross-domain relation that has survived in this repo is a *p*-statement; every
> one that died was a *k*-statement wearing a domain label.

Concretely, re-charting all observables against λ instead of ε removes *k*
identically, and what remains is a function of *p* alone. The registered
quantitative form is the noise-rounding crossover
**λ_c ~ D^(p−2)/p**, where D is the noise scale — a formula containing no free
parameter and no domain label, predicting 1/3, 1/2 and 2/3 for cubic, quartic and
sextic degeneracies respectively.

**What it retrodicts (built from none of these).** S7's τ·λ = 1 is the statement
that in the λ chart the relaxation exponent is exactly −1 in every domain — the
domain-dependence lived entirely in ε ↦ λ. S5's "α = the order of vanishing of
χ²_sym" is the same move made in a different chart: α varies against the bare noise
parameter and stops varying once referred to the χ² degeneracy. P-A's directional
finding is the statement that λ must be taken from the trajectory free energy when
the potential's Hessian is the wrong chart.

**Prior-art note.** Reparameterization-covariance of critical exponents is not new
in itself — it is why physics quotes exponents against the *reduced* temperature
and not against T, and scaling relations (Rushbrooke, Widom, Fisher) are exactly
statements that certain exponent combinations are chart-free. The claim here is
narrower in one direction and wider in another: *narrower*, because it asserts only
that the classification needs two integers and that one is gauge; *wider*, because
it applies to singularities with no thermodynamic limit, no order parameter and no
universality class — a decoder recursion, a queue at saturation, a least-squares fit
at the interpolation threshold — where the discipline that supplies the exponent has
no convention about which chart is canonical, and therefore reports the chart as if
it were the physics. What is claimed as N2 is the *cross-domain* statement plus the
λ-chart's canonical status; what is emphatically not claimed is that critical
exponents transform under reparameterization, which is elementary.

**Falsifier — three-sided.** (i) Two systems with the same *p* and different *k*
whose λ-chart exponents disagree — then the chart is not removable and *k* carries
real information. (ii) A measured λ-chart crossover exponent that misses
(p−2)/p — then *p* is not the classifying integer, whatever else is true.
(iii) The λ-chart exponent moving under an explicit reparameterization of ε —
then the invariance claim is simply false.

---

### D2 — Floor 4 is not a floor, it is the gauge group

**Engine:** gap prediction — the map's [sharpest open question](../SYNTHESIS.md) §7.1.
**Novelty: N2 for the architectural reading; N0–N1 for the group analysis, as its
prior-art note warned. Status: ⟳ WORKED 2026-07-26 —
[`derivations/D2-gauge-of-the-tower.md`](../derivations/D2-gauge-of-the-tower.md)
+ [`experiments/D2-gauge-group/`](../experiments/D2-gauge-group/).**

> **⟳ Restraint pass (2026-07-26): the P0 is answered, and the answer is that
> the question presupposed too much.** Neither a fourth floor nor floor 1 in
> disguise: the scheme layer is the tower's **structure group**. Make the two
> groups explicit — **G_diff** (reparameterizations smooth *at* the singular
> point) and **G_pow** (φ ~ ε^a: smooth away from it, not at it, so
> G_diff ⊊ G_pow with the enlargement living entirely on floor 3). Then RG
> eigenvalues are G_diff-invariant by conjugation (verified to 5.3e-15) and
> G_pow-covariant as y → a·y (verified to ≤2.4e-12), which is **exactly D1's
> chart order's behaviour** — so the log-ratio signature is the transformation
> datum of G_pow modulo G_diff, and a transformation parameter is not a fact on
> any floor. **The chart-free residue is one integer**: signs, counts and ratios
> are three faces of the codimension p − 2 — the coefficients that must be tuned
> to sit on the singularity, the relevant RG directions, and the reciprocal of
> β/k. Measured on full models: β/k = **0.5000** (p = 4) and **0.2503** (p = 6)
> against 1/(p−2), while β spans 4× and k spans 2×. **So what was under the
> fourth floor was D1's *p*.** The counter-horn survives where the derivation
> said it would — "which perturbations are relevant" is a claim about a *sign*,
> and signs are G_pow-invariant, so the predictive work is real and lives in the
> non-gauge part. Bonus: it explains `FLOORS.md`'s unexplained asymmetry —
> **floor 2 collapses because G_pow = G_diff away from the singularity; floor 3
> stratifies because the group enlarges exactly there.** And it settles the worry
> D1 left open: **within a domain exponents are facts (universality is a G_diff
> statement); across domains only ratios, signs and counts are.** Honest limits:
> most of the experiment is a theorem check, both at-risk legs are physics, the
> common-a commitment is load-bearing (independent per-direction re-charting kills
> the ratios and leaves only signs), and the G_diff half is Wegner's nonlinear
> scaling fields in other words.

[`FLOORS.md`](../invariants/FLOORS.md) §4 found that four things refused the tower
and refused it *the same way*: their invariant is a **log-ratio** —
log(multiplicity) over log(rescaling) — rather than a derivative of Φ. S5's
ln n₀/ln(t+1), a fractal's ln N/ln b, RG eigenvalues, and bookkeeping identities.
The repo proposed these constitute a fourth floor, the "scheme layer," and named
the live question as whether they instead collapse into floor 1.

**The claim: neither. They are the chart order *k* of D1.**

Note what *k* actually is:

```
        k  =  d ln λ / d ln ε
```

log-response over log-rescaling — **the floor-4 signature exactly**. A fractal
dimension is the chart order of a self-similar map; an RG eigenvalue is the chart
order of the coarse-graining map; S5's type-R exponent is the chart order of a
decoder recursion; double-entry accounting is the degenerate case k = 0, conserving
because the chart is constant. If D1 holds, these are not a *layer of the tower* at
all — they are the **reparameterization data relating one description of the tower
to another**, i.e. its gauge group. That is why they refused floors 1–3: a gauge
parameter is not a fact on any floor. It is also why they all had the same
signature, which a genuine new floor would have no reason to produce.

This dissolves the P0 rather than answering it, and it makes a commitment the
"fourth floor" reading does not: **scheme-layer quantities must be removable.**
A floor is a place where facts live; a gauge is something you can chart away.

**Falsifier — two-sided.** (i) A scheme-layer invariant that does *predictive work
which survives re-charting* — a log-ratio quantity that cannot be absorbed into a
coordinate choice — restores the fourth floor and kills this. (ii) Conversely, an
invariant of the description map whose signature is *not* a log-ratio breaks the
identification in the other direction. Note that horn (i) is a real risk: an RG
eigenvalue predicts which perturbations are relevant, and it is not obvious that
survives being called gauge.

---

### D3 — The ladder is a chart-invariance count

**Engine:** negative space — no cross-domain relation in this repo has ever
survived as a bare exponent.
**Novelty: N2 claimed. Status: ⟳ RUN 2026-07-28 — FALSIFIED.
[`experiments/D3-ladder-as-quotient/`](../experiments/D3-ladder-as-quotient/).**

> **⟳ Restraint pass (2026-07-28): falsified on its own registered falsifier, and
> the replacement is smaller but measured.** The chart is *n*, the number of
> contributions, so D7/D8 apply directly to the
> [ladder-vs-transfer harness](../experiments/ladder-vs-transfer/). **The chart-free
> residue does not separate the domains that transfer from the one that does not.**
> Its distances from the reference are 0.0081 / 0.0120 / 0.0327 for L4 / L3 / L2 —
> all the size of the seed spread — and their **ordering scrambles across every
> sampling setting tried**, with L2, the domain that fails, coming out *closest* at
> the best-estimated one. Transfer skill over the same rungs is 0.033 / 0.484 /
> 0.916 / 0.894: a factor of 28, stable to ±0.02 over 8 seeds. That is horn (i)
> exactly — **an L2 correspondence that is chart-invariant and still fails to
> transfer.** The *count* reading fails too: rank is 1 for every aggregating domain
> and **0** for the non-aggregating one, so it takes two values across four rungs
> and separates the boundary that matters least.
> **What does place the boundary is the bare exponent 1/α**, which orders all four
> rungs exactly as transfer does with a 30× gap at L2/L3. Not a paradox: aggregation
> composes additively, so n ↦ n^a breaks it (defect **0** at a = 1;
> **0.293 / 0.500 / 0.414** at 1.5 / 2 / 0.5 — [P-D](../experiments/PD-allometry-reduction/)'s
> leg F with the count in place of the mass). **G_pow was never available, the chart
> is pinned, and by [D2](../derivations/D2-gauge-of-the-tower.md)'s rule (i) the
> magnitudes are facts.** So D3 assumed the ladder lives on the *across-domains*
> half of D2's sentence; on this harness it lives on the *within-domain* half.
> **The replacement:** transfer here is predicted by **basin membership**, which is
> a claim about magnitudes being *equal*, not about ratios — and that fits what
> [paper 1](../paper/transfer-cliff.md) found and D3 could not explain. A quotient
> story predicts a step; a basin story predicts a **ceiling**; the ceiling is what
> was measured, because more data cannot move an exponent into another basin.
> **Honest:** one harness and one family, so this refutes D3 as stated and does not
> show that no chart-invariance reading works — the real test is a family whose
> chart is *not* pinned, and this experiment does not contain one. Four rungs cannot
> support a coefficient, so the argument is the pattern of ties plus the
> 30×-versus-scrambling-noise contrast. **No registered tolerance was missed, the
> first time in this arc**; one unregistered separation constant in the code is
> disclosed in the write-up.
>
> **Note on what this stone could still use.** D3's own statement leans on the
> transfer *cliff* — "the jump exactly at L2/L3", "a quotient is not a matter of
> degree". Paper 1 had already **retracted** that step reading (L1→L2 = +0.451 ≈
> L2→L3 = +0.432), so the sharpness argument was dead before the run and the
> registration recorded that it did not get to use it.

If D1 is right, "does this correspondence transfer?" has a mechanical answer:
**it transfers iff it is chart-invariant.** Which would mean the
[ladder](../METHODOLOGY.md) is not a scale of epistemic quality but a count of how
many coordinate choices have been quotiented out — L2 (same form) is a statement in
some chart; L3 (same mechanism) is a statement about the chart-free content.

This makes the [transfer cliff](../experiments/ladder-vs-transfer/) — measured at
0.03/0.48/0.92/0.89, with the jump exactly at L2/L3 — not a curiosity but the
signature of a quotient: nothing transfers until the gauge is removed, and then
everything does. It also predicts the cliff's *sharpness*, which the original
experiment observed and did not explain: a quotient is not a matter of degree.
Compare [S22](./SPECULATIVE.md), which conjectured the ladder is a
renormalization scale; D3 is the sharper version, since RG flow is a chart change.

**Falsifier:** an L2 correspondence that is chart-invariant and still fails to
transfer, or an L3 one that transfers while remaining chart-dependent. Either
breaks the identification. **Test:** the ladder-vs-transfer harness already exists;
add a chart-invariance measurement to each rung and check it predicts the transfer
score better than the rung label does.

---

### D4 — Amplitudes transfer, exponents don't, and the asymmetry is one-directional

**Engine:** residue mining across every experiment in the repo.
**Novelty: N1–N2. Status: unworked; cheap.**

Tabulate everything this repo has measured across ≥2 domains:

| Quantity | Spread across domains |
|---|---|
| τ·λ_min (S7) | 0.94 ± 0.13 — 14% |
| Λ''·gap (P-A) | 2.0000 — exact; family constants 1.54× |
| r_min·δ² (S5) | 1.32, constant to 0.5% over an 8× gap range |
| channel law F_c/F_eff (S25) | exact to 1e-14 |
| attention = Bayes (S23) | exact to 1.4e-17 |
| **exponents** (S5) | **1.00 → 3.17** |
| **exponents** (S7) | **−½ / −1 / −2** |

Dimensionless products come in at O(1) with single-digit-percent spread or exactly;
exponents span factors of 3. **No counterexample in either direction has been
recorded.** D1 explains why — products of conjugate quantities are
reparameterization-invariant, bare exponents are not — but the regularity is
independently checkable and is currently supported by selection-prone evidence: we
kept the relations that worked.

**Falsifier:** a cross-domain bare exponent that transfers tighter than the products
do — for instance a genuinely domain-free critical exponent measured in two fields
with no shared universality class. **Honest caveat:** this stone's evidence is
assembled retrospectively from results that were kept *because* they held, so it
should be tested prospectively before being believed at all.

---

### D5 — Does *p* obey a sum rule?

**Engine:** gap prediction — if *p* classifies, it should have arithmetic.
**Novelty: N3 if it holds. Status: unworked, speculative.**

If floor 3 is classified by the degeneracy order *p*, the natural next question is
whether *p* is conserved, additive, or bounded along a sequence of transitions.
Catastrophe theory gives the finite-codimension answer for gradient systems (the
A_k series, with codimension k−1), which is a strong hint that the arithmetic
exists — but it is stated for potentials, and floor 3's objects include supports,
null Fisher directions and non-analyticities of Φ that are not potentials.
Concretely: when a system passes through two transitions in succession, is the
composite degeneracy order p₁ + p₂, max(p₁, p₂), or unconstrained?

**Falsifier:** measure composite degeneracies and find no relation. **Prior-art
warning:** this is the stone most likely to be N0 — the potential case is Thom and
Arnold, and anyone claiming novelty here must first show their object is not a
potential.

---

### D6 — Is there a singularity with no *p*?

**Engine:** negative space.
**Novelty: N2 for the "one classifier" reading; N0–N1 for the formula.
Status: ⟳ RUN 2026-07-27 —
[`experiments/D6-support-singularities/`](../experiments/D6-support-singularities/).**

> **⟳ Restraint pass (2026-07-27): the question presupposed too much, the same
> way D2's did. Support loss is neither a separate class nor p = ∞ — D1 was a
> special case.** Write Φ's two leading terms as A|y|^{q1} + B|y|^{q2} with
> A → 0; the crossover locus is **A_c ~ D^{1 − q1/q2}**. **q1 = 2 is what
> *smoothness* forces**, giving D1's (p−2)/p with q2 = p; **support loss is
> q1 = 1** — a kink or a boundary — where D1's formula is undefined rather than
> wrong. p = ∞ would be a value in the q2 slot; support loss is a different value
> in the *q1* slot. The observable had to change with it: D1's Var·λ/D needs a
> curvature a kink does not have, so distribution *shape* is used instead (excess
> kurtosis, defined at q = 1 → +3.0000 and q = 2 → 0.0000 alike).
> **Three at-risk legs, all passing, and none of them physics** — closing a gap
> D1 and D2 both recorded and neither closed: L1-penalized logistic regression
> (all orders) gives τ_c ~ D^**0.5000** against 0.5000; **M/M/1 has no crossover
> at all**, as registered — kurtosis pinned at 6.0000 across four decades of
> 1 − ρ, spread 0.0111, no locus to fit; and the hard-wall corner q2 → ∞ gives
> **0.9979** against 1, so a boundary is a continuous corner of the same
> classifier rather than a separate class.
> **The classifier is the ratio q1/q2** — precisely the form
> [D2](../derivations/D2-gauge-of-the-tower.md) derived the chart-free residue
> must take, now established on the class D2's codimension argument could not
> reach, so D2's "residue = codimension p − 2" is the smooth-case face of it.
> Honest: P1/P2 are identities and **P2 was mis-registered as at-risk** — the
> third such slip, all the same failure (§4's tautology-by-construction, caught
> by the rule and missed by me three times); the ratio claim is untested on real
> models; the remainder narrows from "all of support-type" to **essential
> singularities only**; the q1 → 0 logarithmic corner (where the density becomes
> a power law) was registered as noted-not-tested and remains so.

D1's classification presumes Φ has a Taylor expansion at the singular point, with
some first non-vanishing anharmonic term. Floor 3 contains objects for which that
is false by construction: support loss (S5's type S), where the singularity is a
boundary rather than a degeneracy, and essential singularities, where every
derivative vanishes. **These have no *p*.** Are they a separate class, or is
p = ∞ the right label and the classification survives with a point at infinity?

M/M/1 at saturation is the cheapest instance: its stationary law is exponential,
its "potential" is linear, and its relaxation rate vanishes quadratically in the
load gap — a floor-3 singularity from operations research with no anharmonic term
to expand. **Falsifier:** exhibit a boundary-type singularity whose observables
follow (p−2)/p for some finite effective p, collapsing the distinction.

---

### D7 — What the residue *is*: eliminate the chart, and the count is n − 1

**Engine:** gap prediction — the successor to the P0, named as the live question in
[`SYNTHESIS.md`](../SYNTHESIS.md) §7.0 and [`FLOORS.md`](../invariants/FLOORS.md) §4.
**Novelty: N1–N2 claimed, and the split is declared up front — N0 for
projectivization, N1 for the Π-theorem reading, N2 only for the cross-domain
identification and the count. Status: ⟳ RUN 2026-07-27 —
[`derivations/D7-the-residue.md`](../derivations/D7-the-residue.md) +
[`experiments/D7-residue-projective/`](../experiments/D7-residue-projective/).**

> **⟳ Restraint pass (2026-07-27): the residue has a general form, and one of the
> map's standing statements is wrong.** The residue is the log-slope vector modulo
> the **diagonal** ℝ⁺ — equivalently the slopes of observables against other
> observables, in which no chart appears. All five at-risk legs pass on substance.
> **The leg that carries the claim** is one estimator, `d ln O_a/d ln O_b`, handed
> three different pairs of measured quantities without modification: it returns
> **0.4996 / 0.2483** against D2's 1/(p−2) on a smooth germ, **0.5000 / 0.5000 /
> 0.6667 / 0.6667** reproducing D6's table on support-type potentials, and
> **0.7495–0.7500** against P-D's 3/4 on a branching scheme with no singularity, no
> Φ and a discrete chart. **The count is measured at n > 2 for the first time**:
> five slope vectors of a full all-orders germ span a *line* (σ₂/σ₁ = 2.96e-3 and
> 3.45e-3), so the quotient is ℝP⁴ and the invariants number n − 1 = 4 — every
> previously known member has n = 2, which is why each looked like *the* residue
> rather than one coordinate among several. **What it corrects:** "the chart-free
> residue is one integer, the codimension p − 2" is the smooth case's arithmetic,
> not the residue's — Φ = A|y|² + |y|^{2π} gives **0.68169** against 1 − 1/π and a
> germ with p = 2 + √2 gives **0.70698** against 1/√2, and a projective space has
> no distinguished rational points. **D2's common-*a* caveat is derived rather than
> stipulated** and exhibited: the same observables and the same estimator give
> σ₂/σ₁ = 2.19e-3 under the diagonal and 0.227 under the product group, where only
> the signs survive. **The scope condition the derivation had to state holds
> sharply** — a chart-derivative is not an observable, transforms affinely, and its
> slope *changes sign* at a = 1/(1 − k) (predicted 3.010, measured −0.0000 at
> a = 3), which a weight-1 quantity cannot do. **And P-D's kink is settled**: the
> min emerges from the exact sum rather than being imposed, the wall sits at
> x = 1.00012, and it is the point [1 : 1] of ℝP¹ — a wall in the residue's own
> space, chart-invariant, with no Φ in its statement.
> **Honest: three registered tolerances were missed** (P2's ratio at p = 6, 6.73%
> vs 5%; P5c's coarse-graining, 1.96e-6 vs 1e-10; P7's kink spread, 4.7e-6 vs
> 1e-6), all three to the finite-window budget §5 of the registration had named one
> section earlier — **a fourth registration slip, and a new kind**: not
> tautology-by-construction but tolerances set from expectation instead of from the
> scope section. A code bug in the kink locator is also on record, caught by a
> diagnostic that got *worse* under refinement. P1/P6 are identities, P4 is a
> control, P5b reuses D6's estimator so it checks the unification rather than the
> ratio, every model is 1-D or separable, and **essential singularities remain
> outside** — the remainder does not narrow.

**The residue.** Three passes reached the invariant residue by three routes and
none of them can state the other two:

| Route | The residue it found | The object it lives on |
|---|---|---|
| [D2](../derivations/D2-gauge-of-the-tower.md) | codimension **p − 2**, measured as β/k | a smooth floor-3 germ |
| [D6](../experiments/D6-support-singularities/) | **q1/q2**, the two leading exponents of Φ | a support-type singularity |
| [P-D](../experiments/PD-allometry-reduction/) | **θ = ln n / −ln(β²γ)** | a branching scheme with *no singularity and no Φ at all* |

"The residue is the codimension" does not cover the third; "the residue is a ratio"
covers all three and says nothing. The register's own §4 warns that stating a known
special case with the constants removed is N0 with extra steps, so a general
statement has to earn its keep by predicting something the three members do not.

**The claim.** Let a singularity — or a description scheme — supply observables
O₁,…,O_n that vary along one control family carried by a chart ε, and write
y_i = d ln O_i / d ln ε for their log-slopes. G_pow acts by ε ↦ ε^a, and it acts on
the whole slope vector by **one common scalar**:

```
        y  ↦  a · y          (every component, the same a)
```

> **D7.** The chart-free content of a floor-3 singularity or a description scheme
> is exactly the image of its log-slope vector in projective space — the ratios
> y_i/y_j and nothing else. Equivalently and more usefully: **the residue is the
> set of log-slopes of observables taken against other observables**,
> d ln O_i / d ln O_j, in which no chart appears. Four consequences, and the last
> three are the content:
>
> 1. **Ratios are the only invariants** (this is the part that is not new).
> 2. **Counting: exactly n − 1 functionally independent invariants**, for any n.
>    This is the Π-theorem with the chart as the single "dimension" — r = 1, so
>    n − r. No member of the residue has ever been measured at n > 2, so the count
>    has never been tested.
> 3. **The residue is not intrinsically discrete.** D2's integer is inherited from
>    Taylor orders being integers in the smooth case, not from the residue. A
>    singularity with incommensurable leading exponents has an irrational residue,
>    which "the residue is the codimension" forbids.
> 4. **The common-*a* commitment is the group, not a caveat.** D2 flagged it as
>    load-bearing and left it as a stipulation. It is the statement that the action
>    is the *diagonal* ℝ⁺; under independent per-direction re-charting the group is
>    (ℝ⁺)ⁿ, every ratio moves, and the residue collapses from n − 1 invariants to
>    the sign vector — which is exactly what D2 observed and could not derive.

The reason the three members look heterogeneous is that each was read in the chart
its own domain supplies. β/k is d ln y\* / d ln λ; q1/q2 is fixed by
d ln A_c / d ln D; θ is d ln B / d ln M. All three are one observable differentiated
against another, and that is what "eliminating the chart" means.

**Prior-art note (written first).** *Old, and squarely so.* That a set of exponents
defined against an arbitrary scale is meaningful only up to overall rescaling is
elementary; quasi-homogeneous singularities have weight vectors normalized by
convention exactly because they live in weighted projective space (Arnold), the
slope of a Newton-polygon edge is q1/q2 by construction, scaling relations
(Rushbrooke, Widom, Fisher) are the statement that certain exponent combinations
are chart-free, and "two independent exponents" is the standard count in critical
phenomena. The Π-theorem is 1914. **Nothing in the mathematics here is new, and
claiming otherwise would be the register's §4 anti-pattern in its purest form.**
*The nearest miss, recorded so it cannot be relabelled later:* dimensional analysis
already gives n − r invariants from n quantities and r dimensions; D7's counting law
is that arithmetic with r = 1, and if anyone has written "the chart is a dimension
and exponents are its Π-groups", D7 is **N0** and only the cross-domain audit
survives.
*What is claimed at N2, and it is narrow:* that D2's codimension, D6's ratio and
P-D's allometric exponent are **the same invariant computed on different slope
vectors** — including in a system with no potential, no singularity and a discrete
chart, where none of the classical statements apply — plus consequences 2–4, which
the three members individually do not imply.

**Falsifier — four-sided, one per consequence.** (i) An observable at a floor-3
singularity whose log-slope transforms with weight ≠ 1 under ε ↦ ε^a — then the
action is not by a common scalar, the residue is *weighted* projective, and the
ratios are not the invariants. (ii) A singularity with n independent measured
slopes carrying more or fewer than n − 1 independent chart-free combinations.
(iii) A demonstration that the residue must be discrete after all — which would
make consequence 3 false and D2's codimension the general statement. (iv) Ratios
surviving independent per-direction re-charting, which would mean the invariance
is an artifact of the estimator rather than of the group.

---

### D8 — The multi-parameter residue is a Grassmannian point, and its rank counts

**Engine:** gap prediction — the question [D7](#d7--what-the-residue-is-eliminate-the-chart-and-the-count-is-n--1) left live.
**Novelty: N1–N2, and the prior-art note is the most deflationary in the register.
Status: ⟳ RUN 2026-07-28 —
[`experiments/D8-grassmannian-residue/`](../experiments/D8-grassmannian-residue/).**

> **⟳ Restraint pass (2026-07-28): the question's premise was about the wrong
> space, and the answer generalizes D7 rather than qualifying it.** *State-space*
> coupling changes nothing — D7's lemma never mentioned the state space. What
> matters is how many **controls** carry the approach. With m of them the slope
> **matrix** Y_{ij} = ∂ ln O_i/∂ ln ε_j transforms as **Y ↦ Y·A^{-1}** under the
> monomial group ln ε ↦ A ln ε, so the residue is the **column space** of Y — a
> point of **Gr(r, n)** carrying **r(n − r)** invariants — and D7's ℝP^{n−1} is the
> **r = 1 slice**. All four at-risk legs pass. **The rank counts the *relevant*
> directions, at a predicted rate**: a cusp with an added sixth-order coupling has
> m = 3 controls and rank **2**, with the discarded singular value vanishing as
> **t^1.988** against the 2.00 its scaling dimension forces — and on the
> support-type class as **D^1.000** against 1.00. *Small is cheap; the rate is the
> claim.* **Orbit dimension = r·m exactly** (4 / 6 / 2 / 9 measured), so the counts
> 5 / 8 / 9 are measured rather than assumed. **Individual exponents span
> 106×–450×** under the group while the column space is fixed — so at m > 1 even
> the *ratios* move and only a subspace survives, which is the m > 1 form of a
> statement [D2](../derivations/D2-gauge-of-the-tower.md) could make only at m = 1.
> The leg that carries the grade is the **support-type** one: relevant/irrelevant
> classification is textbook wherever there is a fixed point to linearize about,
> and there is none there.
> **Honest, and it is a fifth registration slip in a third category.** P1's
> tolerance was set below what its own estimator can express — `arccos` of a
> principal cosine floors at √(machine eps) ≈ 1.5e-8 — so it was unreachable
> whatever the model did; in the sine form the same models give 1e-13 to 1e-16.
> D7 logged setting tolerances from expectation instead of the modelling budget and
> D8 announced a fix; the fix covered the modelling budget and not the
> **estimator's numerical resolution**. Separately the P2 control is not merely
> forced but **vacuous** — an n × 1 matrix's rank is fixed by its shape — and
> "declared forced" is not the same as "has no content". One thing the registration
> failed to anticipate and P4 implies: **the Grassmannian point is exact when every
> direction is relevant and only asymptotic when one is not**, the tilt vanishing at
> the irrelevant direction's own rate (measured t^1.988, matching). Marginal
> directions (weight 0, hence logarithms) untested; **essential singularities remain
> outside** and the remainder does not narrow.

**The residue's third form.** D7 established that with one control the chart-free
content is the log-slope *vector* modulo the diagonal ℝ⁺. But a floor-3 singularity
of codimension c has c control directions, so the one-parameter case is the
exception rather than the rule, and D7's own scope section admitted every germ it
measured was 1-D or a direct sum.

Write Y for the n × m matrix of log-slopes. The multi-parameter form of G_pow is
the monomial group — ε′_k = Π_j ε_j^{A_{kj}}, i.e. ln ε ↦ A ln ε — under which
Y ↦ Y·A^{-1}. Right multiplication by an invertible matrix preserves the column
space and the rank, and nothing else.

> **D8.** The residue of an m-parameter approach is **col(Y) ∈ Gr(r, n)** with
> r = rank Y, carrying **r(n − r)** invariants. Three consequences:
>
> 1. **D7 is the r = 1 slice**, since Gr(1, n) = ℝP^{n−1} and n − 1 = 1·(n−1).
> 2. **r counts the relevant directions.** An irrelevant control's column vanishes
>    as the singularity is approached, at the rate its scaling dimension sets, so it
>    contributes nothing to the rank.
> 3. **Individual exponents are not invariants once m > 1.** Only the subspace is.
>    At m = 1 this reads "the ratios survive"; at m > 1 the ratios move too.

**Prior-art note (written first, and it is the most deflationary here).** Relevant,
marginal and irrelevant perturbations classified by scaling dimension is textbook
renormalization group — Wegner, Fisher, every book on critical phenomena — and that
an irrelevant coupling drops out of the leading asymptotics is the *content* of the
word. Quasi-homogeneous weight vectors, Newton polyhedra and the A_k unfoldings used
here are all classical. **The nearest miss, recorded so it cannot be relabelled:**
if anyone has written "the exponent data of an m-parameter approach is a point of
the Grassmannian and its rank counts the relevant directions," D8's geometry is
**N0** and only the cross-class audit survives. The honest prior is that a
specialist would call the smooth half a restatement. What is claimed: the *count*
r(n−r); that r is measurable from observables alone without knowing the fixed point;
and that both hold on the support-type class, where there is no fixed point, no flow
and no scaling field for the textbook argument to use.

**Falsifier — four-sided.** (i) The slope matrix failing full rank when every
control is relevant. (ii) The irrelevant column vanishing at a rate that is *not*
its scaling dimension — then r counts numerical negligibility, not relevance.
(iii) Orbit dimension ≠ r·m, which breaks the quotient and the count together.
(iv) Individual exponents surviving the group — then the group is smaller than
GL_m, the singularity supplies a canonical basis of control directions, and the
residue is richer than a subspace. Horn (iv) would replace the count rather than
merely kill it, and is the most informative way for this to be wrong.

---

## 6. Working a D-stone

Same rhythm as a speculative stone, with two additions, both aimed at the two
failure modes that are specific to this register:

1. **Write the prior-art note first**, before the pre-registration. If the search
   turns it up, the stone is N0 and the work is done — cheaply, which is the point.
2. Restate as a quantitative claim, and **pre-register which predictions are
   analytic identities and which can come out wrong.** A stone whose predictions
   are all identities has not been tested no matter how well the numbers agree.
3. Try hardest to falsify. Log it either way.
4. A surviving stone graduates to [`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md) and
   its object earns an entry in [`../invariants/`](../invariants/) — *and* a
   prior-art note that a specialist could check.
