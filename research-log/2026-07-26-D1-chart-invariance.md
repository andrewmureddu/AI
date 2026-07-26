# 2026-07-26 — Turning to discovery: the chart law (D1), and what it does to floor 3

**Worked on:** a new register ([`questions/UNKNOWN-LAWS.md`](../questions/UNKNOWN-LAWS.md)),
its first stone D1 ([`experiments/D1-chart-invariance/`](../experiments/D1-chart-invariance/)),
and the standing P0 about a fourth floor.
**Change:** new register + novelty ladder in [`METHODOLOGY.md`](../METHODOLOGY.md);
floor 3's classification moves from "open" to "two integers, one of them gauge";
the fourth-floor question is reframed (not answered) by D2.

## What I did

The brief was to look for *new, unknown* universal laws. So the first thing was to
be honest about what the project had been doing instead.

Every stone in [`SPECULATIVE.md`](../questions/SPECULATIVE.md) has one shape: take
a law already known in field A, ask whether the look-alike in field B is the same
object. S1 asks whether the replicator equation is Bayes; S5 whether Shannon
capacity is Eigen's threshold; S13 whether grokking is Lee–Yang. That is
**recognition**. It has been productive — it produced the hub, the tower, the
transfer cliff — but its ceiling is the union of the textbooks, and no amount of
it will return a law nobody has written down.

So I opened a third register for **discovery**, with the machinery the operation
actually needs and that the rigor ladder does not supply:

- a **novelty ladder** (N0 restatement → N1 recombination → N2 new relation → N3
  new object), orthogonal to L0–L4 and *multiplying* with it: N3×L1 is a fantasy,
  N0×L4 is a textbook;
- **three engines** — residue mining (explain the numbers our own experiments
  produced and never accounted for), gap prediction (a classification with a hole
  is an instruction), negative space (what never recurs despite the opportunity);
- **two anti-patterns the rigor ladder does not cover**: rediscovery in unfamiliar
  notation, answered by a prior-art note written *first*; and
  tautology-by-construction, answered by a pre-registration that marks which
  predictions are analytic identities before the run. The second rule exists
  because [P-A](../experiments/PA-spectral-gap/) found mid-run that three of its
  four readouts were one number by construction.

Then I worked the first stone, using engine 1 on the repo's own discards.

## What I found

**The residue.** [S7](../experiments/S7-critical-slowing/) measured one relation
that transferred (τ·λ = 0.94 ± 0.13, three domains) and three exponents that did
not (−½/−1/−2), and filed the second half as a negative result.
[S5](../experiments/S5-noise-thresholds/) produced the identical shape: one
discriminator that held, exponents spanning 1.00 → 3.17.
[P-A](../experiments/PA-spectral-gap/) made it three. **Three independent passes
produced the same asymmetry and none of them asked why.**

**D1's answer: the exponent spread was never a fact about domains.** A control
parameter ε is a coordinate choice — ε′ = ε^a describes the same singularity and
divides every exponent by a. So a floor-3 singularity carries two numbers: the
chart order *k* (λ ~ ε^k), which is gauge, and the degeneracy order *p*, which
classifies. Registered form: λ_c ~ D^{(p−2)/p}.

**Result: the chart claim holds in the strong form.**

- *k* is removable **by inference**: a fold in population dynamics (k = ½) and an
  SIS epidemic (k = 1), with anharmonic coefficients differing 3×, give bare
  exponents 0.667 vs 0.333 — differing by exactly 2× — and λ-chart exponents
  0.33333 vs 0.33333, identical to five decimals. *g* lands exactly where the
  claim puts it, in the amplitude: prefactor ratio **2.0801** measured at every
  one of nine noise scales against 3^{2/3} = **2.0801** predicted.
- *k* is removable **by manipulation**: under explicit ε′ = ε^a the bare exponent
  moves by exactly a (0.333 → 1.333 → 2.000) while the λ-chart exponent does not
  move at all.
- The two **at-risk** legs pass. Full models carrying every higher order — mean-field
  Ising (p = 4) and Blume–Capel on its tricritical line (p = 6, quartic coefficient
  verified at 1.0e-10) — give 0.4961 and 0.6635 against 0.5000 and 0.6667.
- The bare chart **inverts** the classification: the fold (p = 3) and the
  tricritical point (p = 6) agree to three decimals, while the fold and the
  epidemic — the *same* degeneracy — differ by 2×. That is the shape of the
  comparison S5 and S7 actually made.

**And the honest deflation, declared before the run rather than after.** The
formula itself is **N0–N1**: it is the Ginzburg calculation for general *p*, and
the pre-registration's §4 stated in advance that inside a truncated normal form it
is *forced* by dimensional analysis — legs A and B could not have come out
otherwise and are reported as estimator checks, not evidence. What is N2 is the
cross-domain claim: that S5's and S7's exponent spreads are a chart artifact, that
floor 3 stratifies by *p* rather than by domain, and that one of the two numbers
is gauge. Fields with no convention fixing the chart reported the coordinate as
though it were the physics.

**One registered direction refuted, its mechanism confirmed.** P8 predicted that
moving off the tricritical line reinstates a quartic and produces a p=6 → p=4
crossover. It does, and the registered *condition* (λ ≳ (c₆/c₄)·D) is right, but
I wrote that the sextic window would be the small-D end and it is the large-D end
— because λ_c ~ D^{2/3} falls more slowly than D, so λ_c/D grows as noise shrinks.
Substituting gives D_× ~ c₄³/c₆² ~ δa³; measured **δa^3.211** over two decades.
That scaling is **post-hoc** and is logged as a consistency check, not a result.

## Decisions / level changes (with reasons)

- **New register + novelty ladder.** [`METHODOLOGY.md`](../METHODOLOGY.md) gains
  the second axis. Recognition and discovery fail differently and need different
  guards.
- **Floor 3's classification moves from "open work" to a stated answer with a
  scope.** [`FLOORS.md`](../invariants/FLOORS.md) said floor 3 stratifies and that
  classifying it was open. It is classified by *p* — **on the part of floor 3
  where Φ has a Taylor expansion.** Support-type and essential singularities have
  no *p* and are explicitly outside; that is now D6.
- **S7's law is re-read, not re-tested.** τ·λ = 1 *is* the statement that the
  relaxation exponent is −1 in the λ chart. Its "domain-specific exponents" clause
  should be read as a statement about coordinates, not domains. P7 extends the
  collapse to epidemiology and a tricritical point (1.005 / 0.987 / 0.935 / 0.997).
- **The fourth-floor P0 is reframed, not resolved.** k = d ln λ / d ln ε is a
  log-ratio — [`FLOORS.md`](../invariants/FLOORS.md) §4's signature exactly — and
  P5 shows *k* is removable by a coordinate change. If that identification holds,
  the scheme layer is the tower's **gauge group**, not a floor, and the P0
  dissolves. Logged as D2, **unworked**; D1 supplies only the removability half.
  The counter-horn is on record: an RG eigenvalue predicts which perturbations are
  relevant, and it is not obvious that survives being called gauge.
- **No new [`invariants/`](../invariants/) entry.** D1 classifies an existing floor
  rather than adding an invariant; its home is
  [`FLOORS.md`](../invariants/FLOORS.md). Revisit if D2 lands.

## Next

1. **D2 (P0).** Decide whether the scheme layer is gauge. The sharp test is the
   counter-horn: is an RG eigenvalue removable by re-charting, or does it do
   predictive work that survives? This is now the map's most valuable question.
2. **A full model from outside physics.** Both at-risk P1 legs are physics. The
   classification needs one all-orders model from biology, information theory or
   ML before "cross-domain" is earned.
3. **D6 — the singularities with no *p*.** M/M/1 at saturation is the cheap
   instance: exponential stationary law, linear potential, relaxation vanishing
   quadratically in the load gap. Is p = ∞ the right label, or a separate class?
4. **Re-register P8's δa³.** It was derived after seeing the direction error and
   does not count until it is predicted in advance and re-run.
5. **D4, cheaply.** Tabulate every cross-domain number in the repo and check
   prospectively whether amplitudes really do transfer where exponents don't — the
   current evidence is retrospective and selection-prone.
