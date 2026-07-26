# 2026-07-25 — S5 run, and the synthesis brought up to the tower

## What happened

Two pieces of work, both queued by the 2026-07-22 entry: the cheapest unworked
stone (S5), and the SYNTHESIS refresh that entry deferred as "its own piece of
work, not a drive-by edit."

### 1. S5 — three noise thresholds ([`experiments/S5-noise-thresholds/`](../experiments/S5-noise-thresholds/))

**Falsifier fires.** Under one resource definition applied identically in every
leg (N(p) = minimum resource per protected bit, N ~ (p_c − p)^(−α)), the exponents
span **1.00 → 3.17**. Predictions were registered in `predictions.json` before
the run; all of them held.

The decisive detail is not that they differ but *how*: the variation is **within**
domains, not across them. Coding theory alone supplies both α = 1 (BEC,
Z-channel) and α = 2 (BSC, BI-AWGN); concatenated fault tolerance supplies four
values determined only by which code you concatenate. So "one threshold per
domain, three domains, three exponents" is not the story, and no re-labelling
rescues the stone.

**Replacement claim — α is a degeneracy order:**

- **type M**, α = 2, where the two conditional laws merge smoothly. This is
  *forced*, not fitted: the first-order term of any divergence between two
  normalized laws cancels identically, so the leading term is the Fisher
  quadratic form. Members: BSC, BI-AWGN, majority-repair quasispecies.
- **type S**, α = 1, where the informative support loses mass. Mass is a linear
  functional. Members: BEC, Z-channel.
- **type R**, α = ln n₀/ln(t+1), where the threshold is not a capacity zero but
  the unstable fixed point of a decoder recursion — an RG eigenvalue ratio.
  Verified for four codes to 1.6e-4.

**Discriminator, verified:** α equals the order of vanishing of the symmetrized
χ² between the conditional laws, to 0.0015 across four channels. The exponent is
therefore readable off local geometry at the threshold, with no capacity
computation.

**A registered diagnostic had to be replaced (on record).** The pre-registration
said "infinite χ² ⇒ α = 1." That rule is direction-dependent and hence ill-posed,
as the Z-channel showed: χ²(P₀‖P₁) = 1e-4 but χ²(P₁‖P₀) = ∞. The *prediction* it
was registered to support (α = 1 for the Z-channel, against the naive reading that
its laws merge) was correct. The rule was rewritten as the quantitative version
above and then tested. Worth naming the pattern: the pre-registration was useful
precisely because it failed in a way that a post-hoc rule would have hidden.

**The biology leg produced the structural finding.** Eigen's bare model has **no
redundancy knob** — every site is functional, so the stone's "required redundancy
vs. gap" question is *malformed* there, and the threshold sits at ln σ/L, moving
with genome length instead of at a fixed p_c. Exact class dynamics recovers
L·μ_c = ln σ (relative error 0.0093 → 0.0023 as L: 50 → 400, falling like 1/L).
Add a decoder and the threshold moves to μ = ½ with r_min·δ² = 1.32 — constant to
0.5% over an 8× range of gaps, and to 10% over the full 33× range (the expected
log correction). So **the error catastrophe is the zero-redundancy corner of
Shannon's picture**, and the gap between the crudest code and the optimal one is a
*constant* (≈3.8), not an exponent — exponent = geometry, code quality =
prefactor.

**Fifth arrival at ∇²Φ's singular set**, and the first to measure its *order*.
Both of S25(K)'s named singular faces — null Fisher directions and supports — turn
up in one experiment carrying different exponents, which is the reason a
single-exponent premise had to fail.

### 2. SYNTHESIS refreshed ([`SYNTHESIS.md`](../SYNTHESIS.md))

The 2026-07-19 snapshot was two architectures out of date. Rewritten around the
tower, with:

- the full ledger, grouped by what each result bears on (frame · hub · architecture
  · "one law" claims) rather than as a flat list;
- a new §5 promoting the repo's strongest empirical regularity to its own
  section: **five independent arrivals at the singular set of ∇²Φ** (S3
  divergence, S25(K) null spaces, Goldstone flat directions, S7 slow mode, S5
  degeneracy order), with the RLCT read as the *quantification* of the same
  object rather than a sixth arrival;
- a reprioritized frontier;
- §8 on what the process is showing.

## Decisions

- **The frontier gained a genuinely new P0 from S5.** Type-R thresholds are
  properties of a *decoder's* RG flow — not facts about Φ, and not obviously
  facts about symmetry either. That is a live candidate for the tower's
  falsifier #4 (an invariant reducible to none of the three floors). Either
  scheme/algorithm-level structure is a **fourth floor**, or a code belongs under
  the symmetry floor (a code *is* a redundancy chosen to be invariant under the
  noise). Deciding this is now the map's sharpest architectural question.
- **Numbering collision fixed forward, not retroactively.** S25 and S26 each name
  two different stones (Cluster J and Cluster K). `SPECULATIVE.md` now carries a
  disambiguation note and S25(K)/S26(K) headers; SYNTHESIS uses the (J)/(K)
  suffixes throughout. Dated log entries and directory names are left as written
  — they are a historical record, not an index. Renaming them would edit history
  to fix an index, which is the wrong trade.
- The `domains/` matrix is left unchanged: the per-domain cells (physics L3,
  biology L3, CS anchor) remain defensible — each domain really does have a sharp
  threshold with a mechanism. What was demoted is the cross-domain *identity*,
  which the matrix does not encode.

## Open

- Unworked stones after today: S2, S4, S6, S8, S10, S12–S17, S19–S22, S24.
  Cheapest next: **S15** (FDT in learning — a cheap numpy test, still untouched
  after being listed as P1 in two consecutive syntheses) and **S22** (the ladder
  as an RG scale).
- The P0 that has now survived three syntheses without being done: **re-sort the
  catalog by floor.** The tower makes it mechanical; nobody has done it. It is
  also the sharpest test of the through-line, because the sorting rule makes
  falsifiable claims about entries no one has examined.
- S5's type-M/S taxonomy is verified at orders 1 and 2 only. A family whose
  Fisher form also vanishes would give α = 4 — an exhibit worth constructing,
  since it would turn the taxonomy from a two-point fit into a series.
