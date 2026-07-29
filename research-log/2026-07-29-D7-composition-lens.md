# 2026-07-29 — D7: the lens under floor 1, and what maintains it

**Worked on:** [D7](../questions/UNKNOWN-LAWS.md) (new stone) ·
[`derivations/D7-composition-lens.md`](../derivations/D7-composition-lens.md) ·
[`experiments/D7-composition-lens/`](../experiments/D7-composition-lens/)
**Change:** the tower gains a **floor 0**; `symmetry-sector.md` §2's selection rule
**corrected**; [`FLOORS.md`](../invariants/FLOORS.md) §4's live question
**answered**; P-B folded into it; the synthesis through-line rewritten from three
floors to four.

## What I did

Started from a gap rather than a result, which is the register's engine 2. Floor 1
says symmetry chooses Φ's coordinates. The derivation takes the group as **given**
— and this map has no outside to give it. So either the base is a brute input, or
something sits under it.

Three of the repo's own results already reached past floor 1 for the same unnamed
thing: P-D leg F killed `G_pow` because *mass is extensive*; D2 §7 reconciled
universality because *energy is additive*; symmetry-sector's charges are, without
comment, exactly the additive ones. Three arrivals, one object — the shape the
singular set of ∇²Φ made five times before it was called the top floor.

Then the register's protocol, in order and in separate commits so the ordering is
checkable: prior-art note first (it came back **N1** — Cauchy, Koopman–Pitman–
Darmois, Ispolatov–Cohen, Touchette, quantum mereology; every ingredient is
somebody's textbook), then the identity/at-risk split, then the run.

## What I found

**The claim survives, at exactly the level the prior-art note predicted before the
work.** Floor 0 is a composition law ⊎ — a rule for putting two instances of a
system side by side. No observer, no group, no dynamics required.

**The one that establishes priority (leg C).** Six statistics of one charge, each
tilted to the *same* informativeness so μ is not a free knob. The ensemble family
closes for **exactly** the additive ones (≤3.2e-14) and none of the others
(≥8.8e-4). Three nearby rules each die on a specific row: linearity on `3Q−7`
(closes anyway — the rule is *affine in an additive charge*), monotonicity on three
rows that have it and fail, convexity on Q² and √Q failing identically at opposite
curvature. **The leg contains no dynamics and no group**, so the rule cannot be a
consequence of floor 1. That, not the arithmetic, is the argument for a layer
underneath, and it is the only place the priority claim is more than suggestive.

**The one that could have been wrong (leg D).** Φ is a cumulant generating
function, so "Φ is additive under ⊎" is one condition **per order**. Curie–Weiss,
exact enumeration, δ₂ = 1 − 2Var(N)/Var(2N):

```
   above T_c   Var ~ N^1.022    delta_2 = 0.00240    predicted 0
   at    T_c   Var ~ N^1.504    delta_2 = 0.29364    predicted 1 - 2^-0.5 = 0.29289
   below T_c   Var ~ N^2.002    delta_2 = 0.50010    predicted 0.5
```

The middle value is the load-bearing one: neither 0 nor ½, inherited from a
critical exponent, and nothing forces it if criticality is not an order-2
extensivity failure. The bottom row reaches ½ by a *different* mechanism (the
symmetric ensemble is a mixture — symmetry breaking). Same order, two mechanisms,
two numbers — a separation "χ diverges" cannot make.

**Order 0 breaks floor 2's Legendre face.** Mean-field 3-state Potts: concavity
defect ~N^1.0252 (registered 1.00±0.10), microcanonical c<0 over 68.6% of the
energy range, so Φ\* is the concave hull rather than s. The identity that makes
free energy and entropy one object seen twice fails exactly on the interval where
composition does.

**Heavy tails have no order at all** — δ₂ centred −0.39…−2.93 with spread 1.8…7.4
against a Gaussian control at 0.00±0.03. Which means the sort's **P-B** (diffusion
splits at finite variance) stops being a separate prediction: it is this
condition's order-2 clause.

**And C3 answers FLOORS §4.** The residue is *the invariant content of the largest
group the composition law fails to pin* — where the chart is pinned the exponents
themselves are facts (allometry's θ, the RLCT), where it is not only ratios survive
(p−2, q1/q2). Two branches of one rule rather than two unrelated members.

## What died, and what I got wrong

**A pre-registered hypothesis, killed by its own control.** "Long-range ⇒
non-additive" is **false**: mean-field q=2 is exactly as long-range as q=3 and its
defect is *exactly zero*. I added that control before the run specifically because
q=3 confounds long-range with first-order, and wrote down in advance which weaker
claim I would have to report. The confound was real, so the weaker claim is what
stands: long range opens the possibility, a first-order transition realizes it.
This is the first time the pre-registration's "here is the alternative I would have
to report" clause has actually fired, and it worked.

**Two registered items failed.** Leg C's growth exponent (+1.00 registered, −0.87 /
−1.51 / −1.82 measured) — killed by my own tilt normalization: holding
informativeness fixed as n grows shrinks μ and the mismatch with it, so the
quantity was ill-posed. Leg D3's discriminator was mis-stated — I claimed a
Gaussian control's spread would shrink like N^{−1/2}, and that spread is set by the
number of realizations, not by N.

**The audit nearly broke C3 and forced a correction.** Reduced temperature is
intensive, so by "additive pins the chart" its exponents should be gauge, and
inside physics they are facts. The fix is D2 §7's own reason said differently —
the chart is pinned because the *conjugate* (energy) is additive — so the rule
needs "or dual to one". Not an epicycle: an additive sufficient statistic is
exactly what induces an affine structure on the natural-parameter space. The same
audit passed a row it was not designed for: the RLCT is read off ln n, samples are
additive, so λ should be a fact — and it independently is one.

**Three code bugs, all found before the numbers were trusted**, all recorded in the
source: a truncated β grid in the Legendre hull; binning that stored bin *centres*
against values computed elsewhere; an off-by-`g[0]/de` index in the max-plus
convolution. The first two made the **short-range control the steepest riser in the
table**, which is what exposed them — the control earned its keep by being
obviously wrong rather than by being right.

## Decisions / level changes

- **New floor.** The tower is now 0–3. This is the first correction to arrive from
  *below* the architecture; D2's was about whether anything sat on top.
- **`symmetry-sector.md` §2 corrected** — "iff it is conserved" is wrong in the
  *if* direction. Its examples were all additive, which is why nothing had broken.
- **`FLOORS.md` §4's live question answered**; P-B demoted from a standing
  prediction to a clause.
- **D7 stays N1.** The prior-art note's default was right and the run does not move
  it. The N2 candidate (floor 3's members indexed by the failing order) is
  *supported* but I have not established it is unstated elsewhere, and the
  large-deviation literature is close enough that the nearest-miss warning stands.
- Legs A and E1 declared identities **before** the run and cited nowhere as
  evidence.

## Next

1. **The d ≥ 2 surface test — the cheapest thing with real teeth.** D7's
   short-range control is a 1-D chain whose entropy is exactly log-binomial, so its
   zero is nearly an identity. An interacting model in d ≥ 2 with a first-order
   transition should give a **third** value, N^{(d−1)/d}. Needs a Wang–Landau
   density of states. A third value makes the order-0 clause a classifier; an
   exponent of 1 breaks it.
2. **Two indices on floor 3, no relation.** D6's q1/q2 classifies a singularity's
   shape; D7's failing order says what kind of failure being at one is. Is q1/q2
   computable from the order?
3. **The mereology half is borrowed.** That the decomposition into parts is
   selected by the dynamics is argued from the literature and measured nowhere. It
   is the part of "the system builds its own lens" the repo has not earned.
