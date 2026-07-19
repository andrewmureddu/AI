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

## Statuses

Each invariant entry carries one status:

- `seed` — placeholder with a claim and a rough level; not yet worked.
- `developing` — actively being filled in and argued.
- `vetted` — evidence reviewed, level defended, boundary conditions stated.
- `contested` — a serious challenge is on record; level in dispute.
- `retired` — investigated and found to be ≤ L1 despite common claims. **Kept,
  not deleted** — the reason it fails is a result.

## The unit of work

One research increment = take one candidate, gather its manifestations, assign a
defensible level per domain with a quantitative signature, identify the
mechanism (or note that it's convergent/unknown), state where it breaks, and log
the decision in [`research-log/`](./research-log/). Small, rigorous, cumulative.
