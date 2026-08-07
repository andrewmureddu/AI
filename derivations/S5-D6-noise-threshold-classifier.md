# S5 × D1/D6 — is the noise-threshold taxonomy gauge, or a real classification?

**Tests:** [S5](../questions/SPECULATIVE.md#cluster-c--is-there-only-one-threshold)
(retired 2026-07-25) against [D1](../questions/UNKNOWN-LAWS.md#d1--the-chart-law-two-integers-classify-floor-3)
and [D6](../questions/UNKNOWN-LAWS.md#d6--is-there-a-singularity-with-no-p)
(both 2026-07-26/27, never cross-referenced back to S5 or to
[`noise-thresholds.md`](../invariants/noise-thresholds.md) until this pass).
Prompted by pushback on the essay-intake session's annotation ("these are all
shadows of the same operator") — reopened rather than defended as-is, per
[`research-log/2026-08-07-essay-intake-theory-of-everything.md`](../research-log/2026-08-07-essay-intake-theory-of-everything.md).

**Result: type S was never comparable to type M in the first place — D1
excludes it from *p* by construction, and D6 already generalized the
classifier to include it, without anyone connecting this back to S5. Once
reframed as D1's own cross-system test (not a new one), S5's published numbers
already show type M and type S are each internally invariant across
structurally unrelated systems, and type R is not — exactly matching type R's
independent demotion to gauge in [D2](./D2-gauge-of-the-tower.md). So: not one
law (confirmed again), but a real two-point classification, not noise.**

---

## 1. What was actually still open

The 2026-08-07 annotation on S5 asked: are type M's α = 2 and type S's α = 1
two different values of a real invariant (D1's degeneracy order *p*), or is
one of them a chart artifact (D1's chart order *k*) that a different
parametrization of "distance to threshold" would remove?

That framing turns out to be slightly wrong on both horns, and reading D1's
own scope note first would have caught it.

## 2. Type S was never in scope for *p* — this is already on record

[D1's pre-registration](../experiments/D1-chart-invariance/PREREGISTRATION.md)
§7, written 2026-07-26: *"Support-type singularities (S5's type S) and
essential singularities have no p and are excluded by construction — they are
D6, not this experiment."* This is not a gap this pass discovered; it was
declared before D1 was even run, one day after S5 shipped, and it names S5's
type S explicitly. Neither `noise-thresholds.md` nor the S5 stone ever linked
to it.

[D6](../questions/UNKNOWN-LAWS.md#d6--is-there-a-singularity-with-no-p)
(2026-07-27) is the follow-up that was written to close exactly this gap, and
its restraint pass generalizes D1's single integer *p* to a ratio of two:
write Φ's two leading terms as A|y|^q1 + B|y|^q2 with A → 0. **q1 = 2 is what
smoothness forces** (D1's case, with q2 = p); **support loss is q1 = 1** — a
kink or boundary, where D1's formula is undefined rather than wrong. D6 names
S5's type S as its own motivating example of the q1 = 1 case, in the same
document that defines q1 = 2 as "what smoothness forces" — the same words S5
uses for type M ("the first-order term... cancels identically... quadratic is
forced, not fitted"). D6 was almost certainly written with S5's type S in
mind and simply never looped back.

**So the qualitative question is already settled, by material already in the
repo:** type M and type S are not comparable via D1's *p* (S has none), but
they are exactly the two named examples (q1 = 2, q1 = 1) of D6's generalized
classifier, tested and confirmed elsewhere (L1-penalized logistic regression,
M/M/1, a hard-wall corner). That is real support for "one classifier, two
points on it" — not "one law," and not "unrelated." [`SYNTHESIS.md`](../SYNTHESIS.md)
§4 already states this pairing (q1=1 ↔ "support loss (S5's type S)") — the gap
was never that the connection was unknown anywhere in the repo, only that it
never reached `noise-thresholds.md` or the S5 stone themselves, and that
`SYNTHESIS.md`'s own text still called S5's exponent spread "largely a chart
artifact," which §3 below shows is too pessimistic.

## 3. Is S5's own α the same invariant D6 is talking about? — checked, not just argued

The remaining question: does S5's *own* published number (α, defined as the
order of vanishing of N or χ²_sym against the raw channel parameter) actually
track D6's q1, or is it a chart-order artifact that happens to coincide with
q1 for these two examples by construction? D1's own methodology for
certifying an invariant is not "does it survive reparametrization" alone —
it's **P2: does it agree across structurally unrelated systems that share the
same mechanism**, the test that separated the fold and the SIS epidemic's real
k = ½ vs 1 from their shared p = 3. That test was never run on S5's numbers
before now, and it is the decisive one, not the reparametrization check below
(which is included because it was cheap and rules out one specific failure
mode, but it is the weaker of the two).

### 3a. Regular-reparametrization check (cheap, single-system, weaker evidence)

Closed-form, verified numerically
([`experiments/S5-D6-reconciliation/run.py`](../experiments/S5-D6-reconciliation/)):

- **BSC** (type M): χ²_sym(p) = (2p−1)²·[1/p + 1/(1−p)], exactly. Near p = ½,
  χ²_sym ~ 16(p−½)² — the measured α = 2 is exact algebra, not a fit artifact.
- **BEC** (type S): N(e) = 1/(1−e), exactly. α = 1 is exact algebra.
- Under a **regular** reparametrization of the distance-to-threshold variable
  (v = sin(ε), v = 3ε+7ε²  — smooth, finite nonzero derivative at ε = 0): the
  fitted exponent is unchanged to 4 decimals for both channels (2.0000 and
  1.0000 respectively).
- Under the **singular** G_pow group (u = ε^a, a ∈ {0.5, 2, 3}): the exponent
  divides by a exactly, as D1's own formalism predicts for any k-type
  quantity (BSC: 4.0000 / 1.0000 / 0.6667 against predicted 2/a; BEC:
  −2.0000 / −0.5000 / −0.3333 against predicted 1/a).

This shows α is not fragile to *ordinary* choices of how you'd naturally
measure noise (crossover probability vs. SNR vs. log-odds are all regular
reparametrizations of each other) — but it is, formally, still a *k*-shaped
object in D1's strict sense (moves under G_pow). This much is true of D1's own
worked examples too, so on its own it settles nothing: **the order of a zero
of a smooth function is always regular-reparametrization-invariant** — that's
elementary calculus, not evidence of a deep invariant. It rules out one
failure mode (that α is fragile to which "reasonable" noise parametrization a
field happens to use) without answering the real question.

### 3b. Cross-system check (D1's actual test, applied for the first time)

D1 certified *p* as real specifically by showing it agrees across systems
whose *k* differs and whose governing equations share nothing (a saddle-node
fold and an SIS epidemic). The equivalent test for S5's α was sitting in
[S5's own published table](../experiments/S5-noise-thresholds/README.md) the
entire time, uninterpreted:

| Claimed type | Systems compared | Governing math | α values | Spread |
|---|---|---|---|---|
| M | BSC, BI-AWGN, quasispecies+repair | discrete Bernoulli / continuous Gaussian MI / population-genetics class recursion | 2.0000, 1.9985, 2.035 | **0.037** |
| S | BEC, Z-channel | erasure / asymmetric bit-flip | 1.0000, 1.0000 | **0.000** |
| R | 4 concatenated codes (n₀ = 5,7,9,23) | same recursion class, different code | 2.2621, 2.3223, 2.8078, 3.1704 | **0.908** |

Type M and type S each pass exactly the invariance test that matters — three
and two structurally unconnected systems, sharing nothing but the claimed
mechanism, land on the same number to 2–4 significant figures. Type R fails
it outright, varying by an order of magnitude more than M or S even *within*
one mechanism class, purely as a function of which code you pick — which is
precisely [D2](./D2-gauge-of-the-tower.md)'s independent verdict on type R
(gauge, dissolves into G_pow), reached from a completely different direction
(the log-ratio-signature argument in [FLOORS.md](../invariants/FLOORS.md) §4)
and now agreeing with this one.

## 4. Verdict

- **Type S was never a fair comparison to type M under D1's original *p*** —
  it has none, by construction, and this was on record one day after S5
  shipped.
- **D6 already supplies the classifier that includes both** — q1 = 2 (smooth,
  type M) and q1 = 1 (kink/boundary, type S) — tested and passing on three
  other domains, never linked to S5 until this pass.
- **S5's own α, re-examined by D1's real test (cross-system agreement, not
  reparametrization robustness), behaves exactly like an invariant for types M
  and S, and exactly like gauge for type R.** This is now three independent
  lines of evidence (D2's derivation, D1's log-ratio signature, and this
  cross-system check) agreeing that type R is gauge, and the first direct
  evidence that types M and S are not.
- **What this does and does not resurrect.** It does not resurrect "one
  threshold" — M ≠ S, confirmed twice over now. It replaces "three unrelated
  exponents" with a sharper claim: **a real two-point classification (smooth
  merge vs. boundary loss), with type R now understood as a gauge readout of
  the same floor-3 structure rather than a third kind of thing.** That is a
  meaningfully stronger and more precise statement than either "one law" (the
  essay's claim, still wrong) or "three unrelated laws" (this repo's original
  verdict, now understood to be one invariant class, one gauge artifact, and
  one napkin comparison — 2 and 1 — that was never actually tested until now).

## 5. What is still genuinely open

Whether S5's α is *literally* D6's q1 (i.e., whether running D6's own
apparatus — the noise-rounding crossover exponent 1−q1/q2, or the
excess-kurtosis diagnostic — on a properly constructed continuous analogue of
these channels reproduces 2 and 1) has **not** been checked, and should not be
claimed. D6's apparatus assumes a stochastic process with an explicit noise
scale D rounding a potential's degeneracy; S5's channels are static
probability models with no such second noise axis, so building that analogue
is a real, nontrivial modeling choice (what plays the role of D for a
channel?) and deserves its own pre-registration rather than an ad hoc
construction here. The cross-system check in §3b is strong indirect evidence
for treating M and S as real classes, but it is a different (weaker in form,
though decisive in the way D1 itself used it) test than actually measuring
q1 directly.

**Falsifier for the open piece:** construct a genuine third member of type M
or type S from a domain with no discrete/continuous-channel structure at all
(the boundary conditions section of `noise-thresholds.md` already flags
chemistry/kinetic-proofreading as L2, untested) and check whether its α
matches its claimed type to the same precision as the table in §3b. A miss
would mean the two-point classification is real only within
coding-theory-adjacent systems, not the general floor-3 fact D6 claims.

## 6. Corrections made as part of this pass

- [`noise-thresholds.md`](../invariants/noise-thresholds.md): mechanism
  section no longer claims type R is excluded from Φ; now cites D2's
  resolution.
- [S5 stone](../questions/SPECULATIVE.md#cluster-c--is-there-only-one-threshold):
  annotated with this result and a link here.
