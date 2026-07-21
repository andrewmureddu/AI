# S25 — Channel-independence of the prediction field's singularities

**Status: RUN (2026-07-21). Verdict: the clean channel-independence claim
FAILS — but with structure. See Results at the bottom. Per the pre-registered
criteria, the 🔴 tier stays scaffolding-only.**

This is the first experiment that tests the 🔴 tier of
[PREDICTION-FIELD.md](../../PREDICTION-FIELD.md) rather than the 🟢 operational
core. Everything else we have run tests what the two tiers *share*.

## The claim under test

[S3](../S3-fisher-geometry/) established that the Fisher metric of the
prediction field degenerates at a phase transition (χ→∞ in Ising;
1/σ²min→∞ at the interpolation threshold). But S3 measured the field through
*one channel per system* (the field h; the feature Gram matrix).

The operational core (🟢) only licenses: "the metric, *as computed through the
channel we chose*, degenerates." The strong reading — the field is ontologically
real, prior to measurement — licenses more:

> **The singular structure belongs to the field, not the probe. Different
> measurement channels applied to the same system must agree on WHERE the
> metric degenerates**, even though they disagree wildly on how much
> information they carry.

If the location of the singularity moves when you change the channel, the
"field" is an artifact of measurement and the 🔴 reading fails by its own
standard (PREDICTION-FIELD.md: "If transfer is uncorrelated with level, the
reframing is decorative"). This is the analogous kill-switch for the
metaphysical tier.

## What makes the test non-trivial

The data-processing inequality for Fisher information guarantees
F_C(θ) ≤ F_full(θ) for any channel C: channels can only *lose* information.
So the **magnitude** of the Fisher curve is trivially channel-dependent. The
non-trivial question is whether the **argmax** (peak location) is invariant.
It is not guaranteed to be:

- A channel blind to the order parameter (e.g. one that measures a quantity
  independent of θ) has a flat-zero Fisher curve — no peak at all.
- An adversarial channel can in principle peak elsewhere (e.g. "sign of a
  single spin" fluctuates most *below* the pseudo-critical point).

So the sharpened, falsifiable prediction is:

> **Generic channels agree on the peak location; only channels that are
> (near-)blind to the transition deviate, and they deviate by carrying ~no
> information, not by carrying information about a *different* singularity.**

Under this reading, "the field is singular at θ*" means: the supremum of
channel Fisher curves is attained at θ*, and generically-chosen channels find
it. If generic random channels scatter their peaks across θ, the reading dies.

## Design

Two legs, mirroring S3. Both exact / deterministic, pure numpy, no fitting.

### Leg A — small 2D Ising, exact enumeration

System: 4×4 (or 5×4) periodic Ising lattice, 2^16 states, exact Boltzmann
p(s|T) by full enumeration. Small enough for exactness; large enough to have a
sharp finite-size pseudo-critical peak in the specific-heat/susceptibility.

A **channel** is a deterministic map c: states → outcomes. The induced
distribution p_c(y|T) = Σ_{s: c(s)=y} p(s|T) is exact by summation, and its
Fisher information w.r.t. T is exact:
F_c(T) = Σ_y p_c(y|T) (∂_T log p_c(y|T))², with ∂_T computed analytically from
the Boltzmann form (F_c(T) = Var over the induced distribution of the
conditional-expected energy — no finite differences needed).

Channel families:

1. **Natural channels** (the ones a physicist would pick):
   total magnetization |M|; total energy E; (|M|, E) jointly.
2. **Generic random channels** (the load-bearing family, ~20 draws):
   - magnetization of a random subset of k spins (k = 2, 4, 8);
   - sign of a random linear functional Σ a_i s_i, a_i ~ N(0,1);
   - random coarse-graining: majority vote on random blocks;
   - a random k-bit hash of a random subset of spins (deliberately unnatural).
3. **Degenerate / adversarial controls** (predicted to deviate, in the
   predicted *way*):
   - single-spin channel s_1 (nearly blind by symmetry: p(s_1|T) ≈ 1/2 at h=0
     → F ≈ 0 everywhere; run at small h > 0 to unpin it);
   - parity of all spins (exactly blind at h=0: energy is parity-even);
   - "sign of M" (a channel about symmetry breaking, not about T — its
     structure should differ, and that is *expected*, not a failure).

Measured quantities per channel: the full curve F_c(T) over T ∈ [1.5, 3.5]
(pseudo-T_c for 4×4 is near the infinite-lattice 2.269, shifted by finite
size), its argmax T*_c, and its total information ∫F_c (how much the channel
sees).

### Leg B — double descent, probe channels

System: the S3 random-feature ridgeless regressor, identical setup
(D=128, N=40, nested features, sweep P/N through 1).

A **channel** here is a way of probing the trained predictor:

1. **Natural**: test MSE on the training distribution (S3's channel).
2. **Generic random** (~20 draws): test MSE under probe distributions
   x ~ N(0, Σ_r) with random diagonal or random-rotation covariances Σ_r;
   random low-dimensional slices (probe inputs confined to a random
   d-dim subspace, d = 4, 16, 64).
3. **Adversarial control**: probe inputs confined to the span of the
   *training* inputs' feature directions — the one subspace where the
   interpolation singularity is invisible (predictions there are pinned to
   the training data). Predicted to *miss* the peak, and that is the point:
   it is the blind channel, the analogue of parity.

Measured: peak location in P/N of each channel's error/variance curve, vs. the
channel-independent 1/σ²min singularity at P/N = 1.

## Falsification criteria (fixed before running)

Let T*_full be the exact full-state Fisher peak (leg A) / P/N = 1 (leg B).

- **PASS (🔴 survives, promotes toward 🟡):** every generic random channel's
  peak lands within tolerance of T*_full (leg A: |ΔT*| < 0.15, roughly the
  finite-size scale; leg B: |Δ(P/N)| < 0.10, the S3 coincidence tolerance),
  AND the controls deviate only by being information-poor (∫F_c at least
  ~10× below natural channels), not by exhibiting a comparable-strength peak
  elsewhere.
- **FAIL (🔴 drops to scaffolding-only):** generic channels scatter — any
  substantial fraction (>2 of ~20) of *non-degenerate* random channels
  (∫F_c within 10× of natural) peak outside tolerance.
- **Interesting-either-way middle:** if peak location correlates with channel
  informativeness (weak channels drift, strong channels lock on), that is a
  quantitative statement about *how* measurement approximates the field —
  worth its own follow-up rather than a clean pass/fail.

One pre-registered caveat: on a finite lattice everything is analytic, so
"singularity" means "finite-size pseudo-critical peak." Channel-dependent
finite-size *shifts* are known physics (different observables have different
scaling corrections). The tolerance above is set wide enough to absorb that;
a scaling check (repeat at 3×3, 4×4, 4×5 and confirm per-channel peaks
converge toward each other as size grows) is the tie-breaker if results sit
near the boundary.

## Why this is the right next experiment

It is the only test on the table where the 🟢 and 🔴 tiers make different
predictions. 🟢 is agnostic about channel-independence; 🔴 requires it.
Cheap (exact enumeration + the existing S3 harness), deterministic, and the
outcome moves a tier boundary in either direction.

## Results (2026-07-21)

`run.py` (main experiment) + `scaling_check.py` (the pre-registered
tie-breaker). Outputs: `verdict.json`, `scaling_check.json`,
`legA_fisher_curves.csv`, `legB_mse_curves.csv`.

### Leg B — clean PASS

All 16 generic probe distributions (lognormal-diagonal covariances,
random-rotation power-law covariances, random low-dimensional slices down to
d=4) peak at **exactly P/N = 1.000**, deviation 0.000 against tolerance 0.10.
The adversarial train-span probe is blind exactly as predicted: peak MSE
0.96 vs. 753 for the natural probe (ratio 0.0013). For the learning system,
the interpolation singularity is visible through every generic channel and
invisible only through the one deliberately-constructed blind subspace.

### Leg A — fails the clean claim, in an instructive way

Full-state peak T* = 2.150 (4×4). Three findings:

1. **Unstructured generic channels lock on.** Subset magnetizations, random
   8-bit hashes, and |a·s| bins — 16 channels — all peak within 0.125 of
   T*, most within 0.075. For *random* measurement, channel-independence
   holds.
2. **Block-majority (coarse-graining) channels shift systematically UP**
   (+0.15 to +0.175 at 4×4), and the tie-breaker shows the shift does NOT
   vanish with size (mean dev 0.200 / 0.156 / 0.200 at 3×3 / 4×4 / 4×5).
   This is not noise and not a finite-size artifact within reach of our
   sizes: a channel that is itself a renormalization step measures the
   *coarse-grained* system's pseudo-critical point, i.e. the channel moves
   you along the RG flow. The field's geometry **composes with** structured
   channels rather than being invariant under them.
3. **The parity pre-registration was wrong physics, and the correction
   matters.** We pre-registered global parity as "exactly blind at h=0."
   That is true only for ODD site counts (global spin flip inverts parity →
   p(y)=1/2 identically; confirmed: integrated info ~1e-28 at 3×3). At even
   sizes parity is genuinely informative (~18–22% of full-state info) and
   peaks near T ≈ 1.6 — deviation ~0.5, persistent across 4×4 and 4×5. It
   peaks deep in the ordered phase, where single-flip excitations (which
   toggle parity) fluctuate most. So parity is not blind; it is an
   informative channel about a *different* structure than criticality.

### Verdict against the pre-registered criteria

The FAIL condition — non-degenerate channels exhibiting comparable-strength
peaks elsewhere — is met by the block-majority family (persistent under the
scaling tie-breaker) and by parity (misclassified as a control, but
non-degenerate by the stated 10× rule and peaked 0.5 away). **The strong
reading's clean prediction is falsified: peak location is invariant only
under UNSTRUCTURED channels.** Per PREDICTION-FIELD.md's own rule, 🔴 stays
scaffolding-only; it does not promote.

### What survives (the interesting middle, as pre-registered)

The result is exactly the flagged middle case, sharpened: **where a channel's
Fisher curve peaks tracks the channel's own structure, not its
informativeness.** Random channels — no structure of their own — inherit the
field's singularity. Channels with intrinsic structure (coarse-graining = an
RG step; parity = a topological/global statistic) locate *their own*
distinguishability peaks. A defensible weaker invariance survives:
*the singularity is invariant under generic (structure-free) measurement* —
true in both legs, and arguably the operationally relevant version, since a
measurement with its own dynamics is part system, part probe. Follow-up
question: is the block-majority shift quantitatively the first step of the
exact RG flow of pseudo-T_c? That would convert the failure into a
composition law for the field.

## See also

- [PREDICTION-FIELD.md](../../PREDICTION-FIELD.md) — the tiered claim; this
  tests the 🔴 tier.
- [S3](../S3-fisher-geometry/) — the single-channel result this generalizes.
