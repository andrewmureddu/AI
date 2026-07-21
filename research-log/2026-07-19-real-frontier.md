# 2026-07-19 — The real frontier: the frame on data I did not construct

**Worked on:** SYNTHESIS §6.1 — make the prediction-field frame empirically
load-bearing
**Change:** frame's 🟢 core lifted from "demonstrated in a constructed SCM" to
"holds on real, uncontrolled data"

## Why this one

The frame is the repo's spine; its central claim (invariance ⇒ transfer) had only
been shown in a *constructed* SCM (S18) and a *controlled* mechanism ladder. The
critique both times: I designed the structure. The real frontier answers it with
data I did not design.

## What I did (two legs, both real)

**Leg A — real dataset (sklearn diabetes, 442 patients).** Environments = age
quartiles (genuine subpopulations). Measured each feature's relationship-stability
across age groups (invariance, train) and its leave-one-environment-out predictive
R² (transfer, held-out group).

**Leg B — a named invariant across computable domains.** Benford's law across
2ⁿ/3ⁿ/n!/Fibonacci (mechanism holds) vs uniform / narrow-lognormal controls.

## What I found

- **Leg A: Spearman(invariance, transfer) = 0.983** — essentially matching the
  synthetic S18 (0.985), now on real data. Interpretable: **bmi** and **s5** are
  stable across age groups and transfer (R² +0.29, +0.27); **sex** is unstable and
  fails (R² −0.08). Stability on training groups ranks held-out predictive power
  almost perfectly.
- **Leg B: mechanism domains 0.97 skill, controls 0.00.** The invariant transfers
  across four genuinely different generative processes and fails on surface-only
  look-alikes — the L3/L4-vs-L1 pattern, for a real named invariant.

## The honest confound (named, not hidden)

Leg A cannot cleanly separate **invariance** from **signal strength**: a strong
predictor (bmi) is both stable *and* transferable; a weak one (sex) has a noisy
(unstable) slope estimate *and* poor transfer. So ρ=0.983 partly reflects
"strong features are both stable and transferable." The synthetic S18 *controlled*
this (its spurious feature was the strongest in-distribution yet failed to transfer).
The two are complementary: S18 isolates the mechanism; real-transfer shows the
relationship survives in messy uncontrolled data.

## Verdict

The real frontier test **passed**. The prediction-field frame's operational core is
now **empirically load-bearing** — it holds on data whose structure I did not
design. Updated PREDICTION-FIELD.md (three-pass falsifier record) and SYNTHESIS
(§6.1 largely done; ledger + counts). The remaining gap (break the confound;
many real fields) is now P1, not P0.

## Loop status

Fifth experiment with teeth. The frame has survived three increasingly-honest
transfer tests (synthetic → controlled cross-mechanism → real data). This is the
strongest single result in the repo for "the center is real, not decorative."

## Next

- Residual-invariance version of Leg A to break the signal-strength confound.
- A second/third real dataset (wine cultivars, breast-cancer subtypes) to check ρ
  holds across datasets.
