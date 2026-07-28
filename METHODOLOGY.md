# Methodology

This document is the spine of the project. It defines *what counts* as a
cross-domain invariant and how we grade the evidence for one. If an entry in
[`invariants/`](./invariants/) cannot be located on the ladder below with a
stated reason, it is not finished.

## The correspondence ladder

Every claimed correspondence between two (or more) domains is assigned a level.
Higher is stronger. An invariant's headline level is the **highest level that is
actually defended in its entry**, not the highest level someone has ever asserted
in a TED talk.

| Level | Name | What is shared | What it buys you | Typical failure |
|------|------|----------------|------------------|-----------------|
| **L0** | Metaphor | A word | Nothing predictive | "Momentum" of a sales team |
| **L1** | Structural analogy | A relational/topological structure (objects and relations map over, but no quantitative law) | Hypothesis generation | Mistaking the map for the territory |
| **L2** | Formal identity | The same mathematical object governs both (same distribution, same PDE, same functional form) | Quantitative transfer of technique | Same form, unrelated mechanism, different constants |
| **L3** | Mechanistic identity | The *same generative process* produces the pattern in each domain | Genuine explanation + intervention | Convergent-but-distinct mechanisms mistaken for one |
| **L4** | Universality | A rigorous argument (renormalization group, a central-limit-type theorem, a symmetry principle) shows a whole class of microscopically different systems must share the invariant, and predicts its quantitative signature | Prediction of new systems + exponents | "Universality inflation" — the word without the proof |

**Convergence vs. identity.** L3 requires the *same* mechanism. If two domains
arrive at the same pattern by *different* mechanisms (convergent evolution of
form), that is a real and interesting finding, but it is a **separate claim** —
label it "convergent (distinct mechanisms)" and do not silently promote it to
L3/L4.

**The L2/L3 line is the one that matters — and it is empirically where the
transfer ceiling becomes attainable.** A controlled experiment
([`experiments/ladder-vs-transfer/`](./experiments/ladder-vs-transfer/)) held a
surface phenomenon fixed and varied only correspondence depth. Transfer skill ran
0.03 / 0.48 / 0.92 / 0.89 across L1 / L2 / L3 / L4 — level orders transfer. The
operative difference is **asymptotic**: as evidence grows, L3 and L4 rise to the
metric's measured ceiling (0.920 ± 0.023, i.e. *complete* transfer) while L2
saturates at ~0.54 and stays there. **More evidence redeems a shared mechanism and
never redeems a shared form.** So the appearance→mechanism line isn't just a
bookkeeping distinction — it is where a correspondence starts to carry predictions
across the boundary *without a ceiling*. Notably L3 ≈ L4 in transfer skill
(mechanism and theorem transfer equally well); they differ in the *strength of the
guarantee*, not the transfer.

> **⟳ Correction (2026-07-26, [`paper/transfer-cliff.md`](./paper/transfer-cliff.md) §3.3).**
> This paragraph previously said transfer was "near-useless at L1–L2" with "the
> cliff exactly at the L2/L3 boundary." Decomposing the adjacent steps refutes
> that: L1→L2 = +0.451 and L2→L3 = +0.432 are the same size, and L2 at 0.48 is
> about half the attainable skill, not near-useless. The *step*-size reading is
> **retracted**; the *ceiling* reading above replaces it and is what the `vary_n`
> sweep actually supports.

## Evidence standards

To move a candidate *up* the ladder, an entry must supply the relevant evidence:

- **Quantitative match (for L2+).** Do the *numbers* agree — exponents,
  dimensionless ratios, scaling collapses — not merely the qualitative shape? A
  shared "roughly straight line on log-log axes" is not a shared law.
- **Mechanism check (for L3+).** Is there one identified generative process, and
  does perturbing it move both domains the predicted way? Name the mechanism.
- **Predictive transfer.** Does knowing the invariant in domain A yield a
  *nontrivial, correct, previously-unmade* prediction in domain B? Record the
  prediction, not just the retrodiction.
- **Boundary conditions.** A real invariant has known limits. State where it
  breaks. An invariant that "always holds" usually hasn't been tested.
- **Statistical rigor.** Fit candidate laws against alternatives (lognormal,
  stretched exponential, truncated power law) with a principled criterion, not by
  eyeballing. See the power-law caution below.

## Anti-patterns (things that masquerade as invariants)

- **The power-law trap.** A noisy straight-ish line on log-log axes is weak
  evidence. Lognormal and stretched-exponential distributions imitate power laws
  over 1–2 decades. Require several decades and a proper model comparison
  (Clauset–Shalizi–Newman style) before claiming a power law at all.
- **Reification of metaphor.** Treating a suggestive word ("energy," "entropy,"
  "selection") as if naming it explained a mechanism.
- **Universality inflation.** Calling any recurrence "universal." Universality
  (L4) is a technical claim with a technical burden of proof.
- **Cherry-picked domains.** Listing the three fields where it works and omitting
  the ten where it doesn't. Entries should record where the invariant *fails* to
  appear when you'd expect it.
- **Dimensional sleight of hand.** "Conservation of X" claims that don't specify
  the conserved quantity's units or the symmetry it follows from.
- **Curve-fitting freedom.** Enough free parameters fit anything. Count them.
- **Registering a number without auditing the construction.** *The house
  speciality.* You build a model, then register a prediction about it — and the
  number is unreachable, or forced, or measured by a checker cruder than the
  tolerance you asked for. Six instances on record and counting:
  [P-A](./experiments/PA-spectral-gap/)'s spread threshold,
  [P-D](./experiments/PD-allometry-reduction/)'s MST construction and its
  mean-field control (degenerate for the exact reason under study),
  [D6](./experiments/D6-support-singularities/)'s P2 (an identity registered as
  at-risk), [P-C](./experiments/PC-variational-kinds/)'s P8 (a rank its own cost
  model forbade) and P4 (a normalization slip), and
  [P-K](./experiments/PK-kink-taxonomy/)'s P1, P5 and P6a (a stencil cruder than
  its tolerance, the wrong statistic, and one piece of wrong algebra labelled an
  identity). **Pre-registration has caught every one of these and prevented none
  of them**, which is exactly what you would expect — it is a detector, not a
  brake. So before writing any number down, audit the construction itself:

  > **The pre-registration audit.** (i) *Rank* — how many of the parameters you
  > are about to vary are genuinely independent in the object? Count the distinct
  > functional dependences, not the named constants. (ii) *Identity* — can this
  > prediction come out any other way, given what you built? If not, label it.
  > (iii) *Instrument* — is the estimator's own precision (stencil order, grid
  > resolution, window width) better than the tolerance you are registering?
  > (iv) *Algebra* — re-derive the "obvious" closed forms. Three of the six were
  > wrong arithmetic, not wrong science.

## Statuses

Each invariant entry carries one status:

- `seed` — placeholder with a claim and a rough level; not yet worked.
- `developing` — actively being filled in and argued.
- `vetted` — evidence reviewed, level defended, boundary conditions stated.
- `contested` — a serious challenge is on record; level in dispute.
- `retired` — investigated and found to be ≤ L1 despite common claims. **Kept,
  not deleted** — the reason it fails is a result.

## The research rhythm: expansion ⇄ restraint

The project runs on a two-stroke engine, and both strokes are load-bearing:

- **Expansion.** Make conceptual leaps — spot that the same object wears different
  disciplinary costumes, connect distant fields, generate candidates. This is the
  generative stroke, and it is *supposed* to overreach. Its home is
  [`questions/SPECULATIVE.md`](./questions/SPECULATIVE.md), where hops are tagged by
  boldness (🟢/🟡/🔴), not yet defended.
- **Restraint.** Test, prune, refine. Take one leap, restate it quantitatively, try
  hardest to *falsify* it, and record what survived. Its home is
  [`questions/OPEN-QUESTIONS.md`](./questions/OPEN-QUESTIONS.md) and
  [`experiments/`](./experiments/).

Expansion without restraint is confabulation; restraint without expansion is
bookkeeping. The map advances only by alternating them. A leap that survives its
falsifier **graduates** from the speculative tier to the rigorous tier and its
object earns a full entry in [`invariants/`](./invariants/); a leap that dies is
logged and its correspondence marked L1. Either way the environment gets mapped.

This is also the honest reading of the "AI-native" advantage: the breadth that
powers the expansion stroke is exactly what makes fake unifications cheap, so it
must be paired with a disciplined restraint stroke. Do what breadth is good at —
*with explicit hedging.*

## The second axis: novelty

The ladder above grades how well a correspondence is *established*. It says
nothing about whether the claim is *new*, because for the project's first seven
cycles every claim was, by construction, old — each stone asked whether a law
already known in field A is the same object as the thing that resembles it in
field B. That is **recognition**, and its ceiling is the union of the textbooks.

[`questions/UNKNOWN-LAWS.md`](./questions/UNKNOWN-LAWS.md) opens the other
operation — **discovery** — and grades it on an orthogonal ladder: **N0**
restatement · **N1** recombination of known parts · **N2** a relation between
standard quantities that no single field states · **N3** a new object that does
predictive work. Levels **multiply**: an N3 claim at L1 is a fantasy, an N0 claim
at L4 is a textbook.

Two rules carry over into that register with extra force, because in discovery
there is no field expert to object:

- **Assume N0 until a prior-art search has failed.** Every N2+ claim carries a
  written prior-art note naming where the result would already live if it were
  old, including the near-misses it did turn up.
- **Separate identities from risks before running.** A pre-registration must mark
  which of its predictions are analytic identities — forced by the construction
  and therefore incapable of coming out wrong — and which are genuinely at risk.
  A stone whose predictions are all identities has not been tested no matter how
  well the numbers agree. This rule exists because
  [P-A](./experiments/PA-spectral-gap/) discovered mid-run that three of its four
  readouts were one number by construction.

## The unit of work

One research increment = take one candidate, gather its manifestations, assign a
defensible level per domain with a quantitative signature, identify the
mechanism (or note that it's convergent/unknown), state where it breaks, and log
the decision in [`research-log/`](./research-log/). Small, rigorous, cumulative.
