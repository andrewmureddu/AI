# 2026-07-21 — S25: the 🔴 tier meets its first falsifier, and loses cleanly

## The setup

The session sharpened "prediction exists before measurement, ontologically"
into a testable form. Two moves made it non-vacuous:

1. **Distributions, not values.** A field of pre-existing *outcomes* is dead
   on arrival (Bell / Kochen–Specker). The survivable version: what exists
   prior to measurement is probabilistic structure. Conveniently, this is the
   only version the repo's machinery parses — the Fisher metric is a geometry
   on distributions.
2. **De-agented via causal states.** "Whose prediction?" forks the claim into
   agent-indexed (QBism/Kant) or intrinsic (ε-machine causal-state structure).
   The repo's 🟡 tier had already picked the second.

From the sharpened claim, one consequence discriminates 🔴 from 🟢:
**channel-independence of the field's singularities.** The data-processing
inequality makes Fisher *magnitude* trivially channel-dependent; the strong
reading predicts the *peak location* is invariant for generic channels. 🟢 is
agnostic about this. First experiment on the table that tests the tiers apart.

## The result ([S25](../experiments/S25-channel-independence/))

Criteria pre-registered before running. Two legs:

- **Learning system (double descent): clean pass.** 16/16 generic probe
  distributions peak at exactly P/N = 1.000; the adversarial train-span probe
  is blind (peak MSE ratio 0.0013). 
- **Exact Ising (2^16–2^20 states, everything closed-form): fails the clean
  claim.** Unstructured channels (random subsets, random hashes, random
  linear bins — 16 of them) lock onto the full-state peak. But
  block-majority coarse-graining shifts the peak up persistently (~0.2,
  non-vanishing across 3×3/4×4/4×5 — the pre-registered tie-breaker), and
  parity turns out to be informative (~20% of full-state info) with a peak
  ~0.5 away, deep in the ordered phase.

**Verdict: 🔴 does not promote.** By the repo's own rule it stays
scaffolding-only.

## Two honest errors on record

- Parity was pre-registered as "exactly blind at h=0." Wrong: that holds only
  for odd site counts (global flip inverts parity). At even sizes parity
  tracks single-flip excitations. The 3×3 run confirms the odd-n version
  exactly (info ~1e-28), which is how we know the reasoning error was about
  evenness, not about the formalism.
- "Blind or agreeing" was a false dichotomy. The third possibility —
  informative about a *different* structure — is what parity and
  coarse-graining actually do, and it is the finding.

## What survives, sharpened

**Peak location tracks channel structure, not informativeness.** Random,
structure-free channels inherit the field's singularity — in both a physical
and a learning system, with zero exceptions across 32 channels. Channels
that carry structure of their own (an RG step; a global topological
statistic) locate their *own* distinguishability peaks. So the defensible
invariance is: *singular structure is invariant under generic measurement,
and composes with structured measurement.* The block-majority shift looks
like the first step of an RG flow of the pseudo-critical point — if that is
quantitative, the "failure" becomes a composition law for the field.

## Same-day follow-up: the failure promoted to a law

The first P2 was run immediately (`rg_composition.py`). Claim: a structured
channel renormalizes the field, so F_c(T) = F_eff(T′(T)) · (dT′/dT)².

- 1D decimation (exact RG known): law holds to 7×10⁻¹⁴. Anchor confirmed.
- 4×4 → 2×2 majority rule: induced distribution is near-perfect effective
  Ising (≤0.01 bits); moment-matched T′(T) predicts the measured peak shift
  to grid resolution (+0.15 predicted vs +0.14 measured, corr 0.9998).
- Random blocks, expected to be the negative control, also obey the law
  (peak predicted to 0.01) — their induced family is still near-Ising.

So the corrected statement of channel-independence, now with empirical
teeth on both sides: **the field's singular structure is invariant under
generic channels and covariant under structured ones** — the peak moves
exactly as far as the channel's induced RG map says it must. Nothing about
the singularity is channel-created; channels either preserve it (T′≈T) or
transport it. Caveat on record: the law is automatic when the induced
family is near a one-parameter exponential family; the finding is that it
IS near one, and that the transported peak lands where measured. The next
real stress test is a channel whose induced family is far from any
one-parameter model.

Methodological note: the first run of the follow-up "refuted" the law
(peak mismatch 0.27) purely through numerics — a finite-difference
derivative of a grid-quantized fit, and a temperature grid that clipped
the 1D peak. Exact ingredients deserve exact numerics; with an analytic
derivative and moment-matched fit the mismatch fell from 0.27 to 0.01.
Worth remembering which side of that experience to trust first.

## Follow-ups

- **P2:** check whether the block-majority peak shift matches the exact
  decimation/majority-rule RG map for small lattices (turning the deviation
  into a prediction).
- **P2:** is there a clean statement of "structure-free channel" (random
  functions concentrate? a measure-zero exception set?) that would make the
  weaker invariance a theorem rather than an observation?
- The learning-system leg passed with suspicious perfection — worth one
  adversarial-generic hybrid (probes correlated with training data but not
  confined to its span) to see where its structured-channel deviations begin.
