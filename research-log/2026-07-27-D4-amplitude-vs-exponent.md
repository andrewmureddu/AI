# 2026-07-27 — D4 falsified: the amplitude/exponent axis was a confound

**Worked on:** [D4](../questions/UNKNOWN-LAWS.md) — do dimensionless amplitudes
transfer across domains while bare exponents do not?
**Change:** D4 **retired**, collapsing into [D2](../derivations/D2-gauge-of-the-tower.md)
and [D3](../experiments/D3-chart-vs-ladder/) rather than standing beside them. The
discovery register's first six stones are now all worked. One counterexample is
identified *inside D4's own evidence table*, and a silent-failure bug is on record.

## What I did

D4 was the register's weakest stone by its own admission: its evidence was a
retrospective table of numbers this repo happened to report, and the stone itself
said it "should be tested prospectively before being believed at all." Two parts,
both registered before the code — the first time in this arc that the
pre-registration genuinely preceded the implementation.

**Part A, a selection audit.** Ask what determined *which* quantities got
reported, and specifically whether the amplitudes we published were
disproportionately chart-free and the exponents disproportionately bare.

**Part B, a prospective battery.** Four systems, seven quantities, all fixed
before measuring and **all reported**, each labelled on two axes at once — kind
(amplitude / exponent, D4's variable) and chart (free / dependent, D2/D3's
variable). The battery deliberately contains chart-free *exponents* and a
chart-dependent *amplitude*, so exactly one axis can survive.

## What I found

**The kind axis separates nothing.** On the comparison pair (fold vs SIS — same
degeneracy order p = 3, different fields, charts differing 2×):

```
   by KIND     exponent  n=5   spread  0.0% .. 66.7%    overlapping
               amplitude n=2   spread  0.8% .. 70.1%    -> separates: NO

   by CHART    dependent n=4   spread 66.7% .. 70.1%
               free      n=3   spread  0.0% ..  0.8%    -> separates: YES
```

An **amplitude** fails at 70.1% while two **exponents** transfer exactly. And the
failing amplitude is not noisy — its prefactor ratio was registered in advance as
g^{2/p} = 3^{2/3} = 2.0801 and measured **2.0801**. An amplitude whose failure to
transfer is exactly predicted is the sharpest available counterexample.

The non-vacuity control holds: on the Ising/Blume–Capel pair (different p) the
chart-free quantities differ too (66.6%, 28.9%), so they are not constants that
agree with everything — they agree when the underlying object is the same.

**The audit found the confound, and then found counterexamples already in the
record.** Every amplitude D4 cited as transferring is a dimensionless product of
*conjugate* quantities — τ·λ, Λ''·gap, r·δ² — which is precisely the chart-free
construction; every exponent it cited as failing is a *bare* exponent against a
domain-supplied control. Nobody chose that. So the regularity is entailed by the
confound.

P6 predicted the confound would be perfect. **It is not, and that is the sharper
result:**

- **[P-A](../experiments/PA-spectral-gap/)'s Kuramoto constant** K_c·λ₂ spans
  0.410–0.632 (1.54×) across graph families — a dimensionless amplitude that does
  *not* transfer. **D4's own evidence table lists this number in the row
  supporting "amplitudes transfer."** The stone cited its own counterexample as
  support.
- **[P-D](../experiments/PD-allometry-reduction/)'s allometric exponent**, which
  landed after D4 was filed: θ holds with n cancelling identically (spread
  4.0e-15), and P-D's own summary is *"magnitudes invisible, counts not"* — an
  exponent transferring to fifteen digits while magnitudes are irrelevant. D4's
  claim with the sign reversed.

The Kuramoto case fits D3's two-factor account rather than breaking it: those
families genuinely differ, so it is the *sameness* factor failing, not the chart
factor. Chart-freedom is necessary, not sufficient.

## Decisions / level changes (with reasons)

- **D4 retired**, and it does not leave a replacement of its own — it collapses
  into D2 and D3. Transfer needs the object to be the same *and* the claim stated
  chart-freely; amplitude-vs-exponent tracks neither reliably.
- **Novelty of the survivor: N0.** The prior-art note flagged that physics holds
  the *opposite* contrast (exponents universal within a class, amplitudes not,
  only certain amplitude *ratios* universal — Privman–Hohenberg–Aharony). D4
  looked like an inversion of the textbook; it was a confounded sample, and the
  surviving statement — *the transferable content is a ratio* — is the same shape
  as the universal-amplitude-ratio result and as D2's chart-free residue. Nothing
  here needed to be new. The value was in killing a stone that would otherwise
  have propagated into the map as an independent law.
- **A methodological point worth keeping.** D4 is the register's first stone whose
  evidence was *assembled from our own published summaries* rather than measured.
  It failed exactly where that method is weakest — the summaries were selected on
  a property nobody was tracking. Engine 1 (residue mining) produced D1, which was
  excellent, and D4, which was a confound; the difference is that D1 mined
  *unexplained numbers* and D4 mined *numbers that already agreed*.

## Honest limits

- **Four systems, two sharing a normal form**, 1-D gradient with additive noise.
  Registered as a deliberate reuse of D1's legs so the numbers stay comparable;
  it does *not* re-close the outside-physics gap that D6 closed.
- **Q1, Q2, Q5 are identities on the comparison pair** (both models exactly cubic),
  declared in advance. The at-risk content was Q6 and the audit.
- **"Chart-free" is assigned by inspection, not measured.** D3 measured it; this
  does not.
- **Silent-failure bug, found and fixed mid-run, on record.** The Blume–Capel leg
  was evaluated at T = ⅔ + ε instead of ⅓ + ε — the caller and the function each
  added ⅓ — so no crossover was bracketed and the empty fit returned 0.0000
  without complaint, which would have corrupted the control pair. The corrected
  leg reproduces D1's published 0.6635. An assertion now refuses to fit a
  degenerate set. This is the second silent-zero in the register (D3 had a
  tie-broken spurious +1.00) and both were caught only by noticing a number that
  was *too round*.

## Next

The register's six filed stones are worked: D1 (confirmed, formula deflated), D2
(P0 answered), D3 (falsified, two-factor replacement), D4 (falsified, confound),
D6 (D1 generalized). **D5 (does *p* obey a sum rule?) is the only one left**, and
its own prior-art warning stands — the potential case is Thom and Arnold, so
anyone working it must first show the object is not a potential.

Standing debts, now three cycles old: **re-register D1's P8 δa³**; a **real ratio
test** for D6 (two domains sharing q1/q2 but not q1 or q2); and the chart tag that
[D3 put into METHODOLOGY](../METHODOLOGY.md) has not yet been applied to any
catalog entry.
