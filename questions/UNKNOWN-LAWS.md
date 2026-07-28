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
**Novelty: N2 claimed. Status: ⟳ RUN 2026-07-27, FALSIFIED as filed —
[`experiments/D3-chart-vs-ladder/`](../experiments/D3-chart-vs-ladder/).**

> **⟳ Restraint pass (2026-07-27): the biconditional dies, and so does the reading
> it was attacking.** Built both off-diagonal cells the falsifier below names, by
> crossing the [ladder-vs-transfer](../experiments/ladder-vs-transfer/) harness
> with a chart factor (B records on y ↦ sgn(y)|y|^a, D1/D2's G_pow on the
> measurement axis) and a statement factor (shape of Y, chart-dependent, vs shape
> of ln|Y|, chart-free).
> **The registered falsifier fired**: with the claim stated chart-freely the low
> rungs still fail — L2 = **0.373**, L1 = **0.037** against L3/L4 at 0.833/0.816 —
> so chart-invariance is **necessary but not sufficient**. **The rung-label reading
> fails too**: with the mechanism untouched but the claim chart-dependent, L3
> collapses 0.916 → 0.000 and at a = 0.7 the word-only L1 (0.723) **beats** the
> theorem-backed L4 (0.565).
> **Survivor — a two-factor claim:** transfer needs a shared mechanism **and** a
> chart-free statement of it; the ladder measures the first only. Sharper form:
> **chart-freedom is the precondition under which the ladder is predictive at
> all** — Spearman(rung, skill) is +0.80 in *every* chart under a chart-free claim,
> and runs +1.00 → −0.80 under a chart-dependent one. Note a = 0.85, where the
> ordering is nominally perfect while the **cliff vanishes** (0.756 vs 0.769
> against an undistorted 0.43): rank correlation alone would have missed it.
> **Revises an existing result:** [ladder-vs-transfer](../experiments/ladder-vs-transfer/)
> lives entirely in the shared-chart cell and never said so; its finding is
> conditional on a shared measurement chart. Also mostly retires
> [S22](./SPECULATIVE.md). Process deviation on record: **no PREREGISTRATION.md**
> — the design and opposing predictions were fixed before the run, but only the
> stone's own falsifier was formally registered, and backdating a file would be a
> fabrication.

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
