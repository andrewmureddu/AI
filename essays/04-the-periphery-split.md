# The Periphery Split

*On the invariants that resist Φ — and the conjecture that the resistance has
a shape.*

---

## 1. The residue is the test

The [second essay](./02-one-object-seen-sideways.md) ended by nominating the
independent periphery as the most important region of the map, and this essay
takes up the nomination. The argument there was conditional: *if* the collapse
onto Φ = ln Z reflects something real — that Φ is the normal form of
predictive structure for constraint-describable systems — then the invariants
that refuse to reduce to Φ are not loose ends. They are the experiment. A
thesis that explains everything it surveys is an instrument artifact; a thesis
with a principled residue is a claim about the world.

The [synthesis](../SYNTHESIS.md) lists the residue plainly: feedback/control,
networks/percolation, scaling/allometry, symmetry-breaking, fractals, spectral
gap, conservation/Noether, with diffusion, noise thresholds, and critical
slowing down parked in a "hub-adjacent, plausibly reducible" middle zone, and
power laws hanging strangely off the side. Ten-ish invariants outside the hub.

The lazy reading of that list is "work not yet done" — the periphery as
backlog. This essay argues for a stronger reading: the periphery is not a
backlog but a **taxonomy in disguise**. The invariants that resist Φ resist
for (at least) two different reasons, corresponding to two questions about a
system that are not the prediction question. If that's right, the map's deep
structure is not one hub with leftovers. It is a small number of primitive
questions, of which "what can be predicted?" is only the best-developed.

## 2. Three questions a system can be asked

Start from what Φ actually answers. For a system described by constraints,
Φ = ln Z generates every conditional expectation, every fluctuation, every
response coefficient. Packed into one convex function is the complete answer
to: **given what I know, what should I expect?** Call this the *prediction
question*. Essay 2's argument was that any inquirer bound to this question —
Bayesian, evolutionary, or gradient-descended — lands on Φ, which is why the
hub-core exists.

Now look at what the periphery entries are actually about, reading them
against their own files rather than from altitude.

**Networks, percolation, spectral gap** answer a different question: **what
can reach what, and how fast?** The
[percolation entry](../invariants/networks-percolation.md)'s domain-neutral
object is the giant-component transition — the threshold at which global
reachability appears. The [spectral gap](../invariants/spectral-gap.md)'s
one number governs mixing, consensus, synchronization, robustness to
disconnection: all rates and thresholds of *influence propagation*. Call this
the *connectivity question*. It is genuinely not the prediction question:
you can know the full degree distribution of two graphs (a distributional,
Φ-friendly fact) and still not know which one percolates, because
reachability depends on the wiring, not the histogram. Degree-preserving
rewiring — the exact quotient that distributional description takes — moves
p_c and λ₂. Connectivity lives in what the exponential-family description
throws away.

**Noether, symmetry-breaking, duality's deeper face** answer a third
question: **what is not allowed to change?** The
[conservation entry](../invariants/conservation-noether.md) is the purest
case, and its internal structure is telling: it spends most of its length
*separating* symmetry-induced conservation (Noether proper, L4) from
bookkeeping identities (double-entry accounting, Kirchhoff node laws, L2).
That split matters here because the bookkeeping half *is* Φ-flavored — a
normalization constraint, exactly the kind of thing partition functions
enforce — while the Noether half is not. A conserved charge is not an
expectation value you predict; it is a *constraint on which dynamics are
possible at all*, prior to any distribution over outcomes. Call this the
*invariance question* — with the uncomfortable note that the repo's own name,
"cross-domain invariants," uses the word in yet another sense, and Section 5
will have to pay for that pun.

So the conjecture, stated as a sorting rule:

> **The periphery split.** Periphery invariants resist Φ-reduction iff they
> answer the connectivity question or the invariance question rather than the
> prediction question. The hub-adjacent middle zone consists precisely of the
> entries that are secretly prediction-question entries in unfamiliar
> clothes, and those will eventually reduce.

## 3. Sorting the actual list

A sorting rule earns its keep by sorting, so run the whole periphery through
it and record the awkward cases — the awkward cases are the content.

**Cleanly connectivity:** networks/percolation, spectral gap. Both entries'
portable predictions are reachability thresholds and propagation rates.
Predicted to resist Φ permanently *as invariants*, even though (see §4) their
transitions borrow criticality's mathematics.

**Cleanly invariance:** conservation/Noether, symmetry-breaking. The
symmetry-breaking entry is the invariance question run in reverse — what
happens when a disallowed change happens anyway — and its order parameters
are defined relative to the broken symmetry, not to a predictive summary.

**Secretly prediction (the middle zone, predicted to reduce):**

- *Diffusion.* The Gaussian is the maximum-entropy distribution at fixed
  variance; the diffusion equation is the flow of that maxent structure over
  time. The synthesis already flags this. Reduction expected, and its failure
  would damage the split badly, since diffusion is the easiest case.
- *Noise thresholds.* Channel capacity is a free-energy-like object over
  codebooks; the entry is information theory, which is hub-native. Expected
  to reduce.
- *Critical slowing down.* The synthesis's own suggestion — softening of Φ's
  Hessian — makes this a corollary of S3's tested result, not a new invariant.
  Expected to reduce, and probably first.

**The genuinely awkward three:**

- *Feedback/control.* Control is about steering, which sounds like neither
  reachability nor conservation. But modern control theory keeps splitting
  along exactly our seam: controllability/observability are *reachability*
  properties (Kalman rank conditions — which states can be reached, which can
  be seen), while optimal control under noise dualizes to inference (the
  LQG/Kalman-filter duality, KL-control). Conjecture: the feedback entry is
  not one invariant but a connectivity half and a prediction half fused by
  historical accident, and Φ will absorb the second half only. This is the
  split's most specific prediction, and the most falsifiable.
- *Allometry.* Kleiber's 3/4-power scaling derives, on the West–Brown–Enquist
  account, from optimal transport through space-filling branching networks —
  which reads as connectivity (a network's delivery capacity) constrained by
  geometry. Sorted, tentatively, to connectivity; but the "optimal" in
  optimal transport smells of variational Φ-machinery, so this one straddles.
- *Fractals.* Self-similarity is scale-invariance — literally an invariance
  under the rescaling group. Sorted to invariance, with the consequence that
  fractals and Noether are relatives, which is either a nice unification or a
  sign the invariance bucket is too roomy.

Score so far: the rule sorts eight entries cleanly, makes one sharp testable
claim (control splits in two), and strains twice (allometry, fractals). A
sorting rule that never strained would be unfalsifiable; two strains in ten
is a real rule with real exposure.

## 4. Power laws, or: the boundary is in the picture

Power laws refuse all three buckets, and the synthesis's "tantalizing
secondary thread" says why: heavy tails live exactly where Φ or its moments
*diverge*. The [entry itself](../invariants/power-laws.md) adds the crucial
negative fact — there is no single power-law mechanism; the pattern is the
shared fingerprint of several distinct generators (preferential attachment,
SOC, multiplicative growth with reflection), which is why the entry caps at
L2 in general.

Put those together and power laws stop being an invariant *in* the taxonomy
and become the taxonomy's **boundary marker**: the scale-free world is the
complement of the well-behaved exponential-family world; a power law is what
the prediction question returns when asked past Φ's radius of convergence.
That would explain the no-single-mechanism finding structurally — there are
many ways to exit a domain, and the exits share only the property of being
exits. It also dissolves an old embarrassment: the decades-long fight over
whether given data are "really" power-law or lognormal is, on this reading,
a fight about how close to the boundary you are standing, which is why it is
interminable and why Clauset–Shalizi–Newman discipline (fit the
alternatives!) is the only honest tool.

And note what the boundary reading does for the split: it predicts that
connectivity and invariance invariants should *also* have their own boundary
phenomena — the analogues of heavy tails for the reachability and symmetry
questions. Percolation's scale-free cluster distribution *at* p_c is
plausibly the connectivity version, sitting exactly at the reachability
transition. If someone can name the invariance version — the characteristic
signature of a symmetry that is marginally, critically almost-broken — the
three-question picture gains a spine. Goldstone modes are the obvious
candidate. This is a question for [SPECULATIVE.md](../questions/SPECULATIVE.md),
not for an essay to settle.

## 5. The pun that has to be paid for 🟡

The repo is called cross-domain *invariants*, and Section 2 used "invariance
question" for one bucket among three. Either the name of the whole project
accidentally names one-third of it, or the buckets are not siblings — and
this is worth a register shift, because it decides what the split *is*.

Here is the debt paid, or at least restructured. The
[prediction-field frame](../PREDICTION-FIELD.md) defines an invariant as a
symmetry of the prediction field — a regularity in what-can-be-predicted that
survives changes of domain and measurement. On that definition, all three
buckets are invariances *of the map*: the percolation threshold's recurrence
across contact networks and power grids is a symmetry of the prediction field
just as much as the Fisher metric is. The three questions of Section 2 are
not three kinds of invariance. They are three kinds of *thing the invariance
is about*: distributions (prediction), wiring (connectivity), and dynamics'
symmetry groups (invariance-in-the-object-language).

So the split, stated carefully at last: **the prediction field has at least
three sectors that do not reduce to one another, because they are invariances
over different quotients** — Φ lives on the quotient by everything except
sufficient statistics; connectivity lives on the quotient by everything
except topology; Noether lives on the quotient by everything except the
symmetry group of the law. The hub thesis ("much of the map is one object")
is then true exactly of the first sector, and the map as a whole is not one
object but one *field* with a small number of sectors — which is a different,
more defensible, and honestly more beautiful claim than the monism the
collapse first suggested.

## 6. Falsifiers, filed 🔴

Per the ground rules, the conjectures above are only worth keeping if they
can die. The kill conditions, explicitly:

1. **A clean Φ-reduction of a connectivity invariant** — percolation
   thresholds or spectral gaps derived *through* log-partition structure
   rather than merely dressed in Gibbs notation. (The dressing exists — the
   Potts-model/random-cluster correspondence writes percolation as a q→1
   partition-function limit — so the falsifier must demand that the
   reduction do *predictive work*: recover p_c-shifts under rewiring from
   Φ-derivatives alone. If it can, the connectivity sector collapses into
   the hub and the split loses a leg.)
2. **Failure of the middle zone to reduce.** If diffusion — maxent's home
   game — cannot be cleanly folded into Φ, the sorting rule's easiest
   prediction fails and the rule is bookkeeping, not structure.
3. **Control refusing to split.** If feedback/control reduces *entirely* to
   Φ (via the inference-control dualities) with no irreducible reachability
   remainder, then the connectivity question is not primitive — Kalman rank
   conditions would have to be re-derivable as degenerate limits of a
   predictive object, which would be a spectacular result and a fatal one
   for this essay.
4. **No boundary signature outside the prediction sector.** If the
   heavy-tail-at-the-boundary pattern is unique to Φ — if percolation
   criticality and Goldstone phenomenology cannot be honestly read as the
   other sectors' boundary marks — then Section 4's symmetry among sectors
   is numerology.

Each of these is closer to an `experiments/` or `derivations/` task than to
further prose, which is where an essay in this repository is supposed to
end: not with a conclusion, but with a handoff. The periphery was the test
of the hub thesis. If the split survives its falsifiers, the periphery
becomes something better — the discovery that the map has more than one
cardinal direction, and that we had simply been walking the best-lit one
first.

> **⟳ Restraint pass (2026-07-22):** falsifiers 1 and 3 were run together, by
> derivation — [`derivations/S25-control-split.md`](../derivations/S25-control-split.md)
> — and **fired against this essay's geometry while confirming its taxonomy.**
> Control did not refuse to split (falsifier 3 survived on that side: the
> inference half is exact Φ-machinery). But the "irreducible" reachability half
> *reduced*: the controllability Gramian is the covariance of the noise-driven
> ensemble (∇²Φ), and minimum control energy is exactly the large-deviations
> rate function — Legendre dual of Φ, with predictive work done (falsifier 1's
> condition met). The saving structure: every binary reachability fact reduced
> only to Φ's **singular set** — supports, null Fisher directions, divergent
> rate functions — never to its regular derivatives. So §5's "three sectors
> over three quotients" is retired and replaced: the map is **two-layered, not
> three-sectored** — Φ's regular part (prediction), Φ's boundary (connectivity,
> power laws, percolation-via-Potts, and plausibly the spectral gap), and one
> remaining candidate for a genuine second axis: invariance/symmetry. Section
> 4's boundary-marker reading of power laws turns out to be the load-bearing
> idea of the essay, promoted from aside to architecture. The sharpest open
> question is now the one this essay filed under "too roomy": does the
> symmetry sector reduce too, or is it the map's one true second primitive?

> **⟳ Second restraint pass (2026-07-22, later):** answered — see
> [`derivations/symmetry-sector.md`](../derivations/symmetry-sector.md). The
> sector splits. Symmetry-*breaking* reduces completely, and to the boundary
> layer: SSB exists only at Φ's non-analyticities, and Goldstone modes are
> null directions of ∇²Φ — §4's hunch was not an analogue of the boundary
> signature but the boundary itself. Noether proper does **not** reduce — the
> obstruction is structural (Noether consumes a bracket, Φ consumes a measure)
> — but it isn't a parallel sector either: conserved charges turn out to be
> exactly the quantities that can, and at long times the only ones that do,
> serve as Φ's natural parameters (Gibbs/GGE). Symmetry sits *under* Φ,
> choosing its coordinates. Final architecture: **one tower, three floors** —
> symmetry picks the coordinates, Φ's regular part predicts, Φ's singular
> part ends prediction. Promoted to stone S26 with a runnable falsifier (the
> SGD stationary-sufficiency test).
