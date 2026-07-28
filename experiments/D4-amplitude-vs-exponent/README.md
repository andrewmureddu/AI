# D4 — do amplitudes transfer and bare exponents not? (result)

**Question ([D4](../../questions/UNKNOWN-LAWS.md)):** residue mining over this
repo's own reported numbers appeared to show dimensionless amplitudes transferring
across domains (spreads of a few percent, or exact) while exponents did not
(factors of 3), with *no counterexample in either direction recorded*. The stone
flagged its own weakness: that evidence is retrospective and selection-prone.

**Status: FALSIFIED. The amplitude/exponent axis is the wrong variable — it
separates nothing once chart-freedom is known. And the audit found counterexamples
in both directions already sitting in the record, one of them inside D4's own
evidence table.**

Run it: `python3 run.py` (numpy only, ~3 min, deterministic — seed 20260727).
Registered first: [`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## Part B — the prospective battery

Four systems, seven quantities, all chosen before measuring and **all reported**.
Each quantity carries two labels fixed in the pre-registration: its **kind**
(amplitude / exponent — D4's proposed variable) and its **chart** status
(free / dependent — [D2](../D2-gauge-group/)/[D3](../D3-chart-vs-ladder/)'s
variable). The battery deliberately contains chart-free *exponents* and a
chart-dependent *amplitude*, so the two axes predict different things.

| system | field | p | Q1 k | Q2 β | Q3 β/k | Q4 bare | Q5 λ-chart | Q6 prefactor | Q7 τ·λ |
|---|---|:--:|---|---|---|---|---|---|---|
| fold | ecology / dyn. sys. | 3 | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0.3333 | 3.8190 | 1.0184 |
| SIS | epidemiology | 3 | 1.0000 | 1.0000 | 1.0000 | 0.3333 | 0.3333 | 7.9439 | 1.0271 |
| Ising | physics | 4 | 1.0000 | 0.5000 | 0.5000 | 0.4985 | 0.4961 | 2.5912 | 0.9526 |
| Blume–Capel | physics | 6 | 0.9996 | 0.2502 | 0.2503 | 0.6641 | 0.6635 | 3.1720 | 0.9631 |

### The comparison pair: fold vs SIS (same p = 3, different fields and charts)

| quantity | kind | chart | fold | SIS | rel. spread |
|---|---|---|---|---|---|
| Q1 k | exponent | dependent | 0.5000 | 1.0000 | **66.7%** |
| Q2 β | exponent | dependent | 0.5000 | 1.0000 | **66.7%** |
| Q3 β/k | exponent | **free** | 1.0000 | 1.0000 | **0.0%** |
| Q4 bare crossover | exponent | dependent | 0.6667 | 0.3333 | **66.7%** |
| Q5 λ-chart crossover | exponent | **free** | 0.3333 | 0.3333 | **0.0%** |
| Q6 prefactor | **amplitude** | dependent | 3.8190 | 7.9439 | **70.1%** |
| Q7 τ·λ | **amplitude** | **free** | 1.0184 | 1.0271 | **0.8%** |

### P4 — which axis separates transfer from failure?

```
   by KIND:    exponent  n=5   spread   0.0% .. 66.7%     overlapping
               amplitude n=2   spread   0.8% .. 70.1%     -> separates: NO

   by CHART:   dependent n=4   spread  66.7% .. 70.1%
               free      n=3   spread   0.0% ..  0.8%     -> separates: YES
```

**Both classes of amplitude appear and both classes of exponent appear.** An
amplitude fails at 70.1% (Q6) while two exponents transfer exactly (Q3, Q5). Kind
explains nothing once chart is known; chart explains everything.

The decisive cell was registered with its value: Q6's prefactor should scale as
g^{2/p}, so with g = ⅓ and 1 the ratio should be 3^{2/3} = **2.0801**. Measured
7.9439 / 3.8190 = **2.0801**. So this is not a noisy amplitude — it is an amplitude
whose failure to transfer is *exactly predicted*, which is the sharpest possible
form of the counterexample.

**P5, non-vacuity.** On the control pair (Ising vs Blume–Capel, *different* p) the
chart-free quantities differ too — Q3 by 66.6%, Q5 by 28.9%. Chart-free quantities
are not constants that agree with everything; they agree when the underlying
object is the same and disagree when it is not.

---

## Part A — the selection audit

D4's evidence was a table of numbers the repo happened to report. The audit asks
what determined *which* numbers got reported. Two findings, and both go against
the stone.

**1. The sample was confounded.** Every amplitude D4 cited as transferring is a
dimensionless product of *conjugate* quantities — τ·λ, Λ''·gap, r·δ² — which is
exactly the chart-free construction. Every exponent it cited as failing is a
**bare** exponent against a domain-supplied control parameter. Nobody chose that;
it fell out of what each experiment happened to find quotable. So the retrospective
regularity is entailed by the confound, and carries no independent evidence for
the amplitude/exponent reading.

**2. The counterexamples were already recorded — including one inside D4's own
table.** P6 predicted the confound would be perfect. It is not:

- **[P-A](../PA-spectral-gap/)'s Kuramoto constant.** K_c·λ₂ is a dimensionless
  amplitude, and it spans **0.410–0.632** (1.54×) across graph families — an
  *amplitude that does not transfer*. D4's evidence table lists this number
  ("family constants 1.54×") **in the row supporting "amplitudes transfer."** It
  is a counterexample, filed as support.
- **[P-D](../PD-allometry-reduction/)'s allometric exponent**, which landed after
  D4 was filed. θ = min(1, ln n / −ln(β²γ)) holds with n cancelling identically
  (spread **4.0e-15**), and P-D's own summary is *"magnitudes invisible, counts
  not"* — an **exponent** transferring to fifteen digits while magnitudes are
  irrelevant. That is D4's claim with the sign reversed.

The Kuramoto case also fits the two-factor account from [D3](../D3-chart-vs-ladder/)
rather than breaking it: those families genuinely differ (size asymmetry), so it is
the *sameness* factor failing, not the chart factor. Chart-freedom is necessary,
not sufficient — which is exactly what D3 found.

---

## Verdict

**D4 is falsified as filed.** The amplitude/exponent distinction does not predict
transfer. It appeared to only because the repo's reported amplitudes were
chart-free by construction and its reported exponents were bare by convention.

**The replacement is not new — it is D2 and D3, and D4 collapses into them.**
Transfer requires (i) the underlying object to be the same and (ii) the claim to be
stated chart-freely. Amplitude-vs-exponent tracks neither reliably: amplitudes can
be chart-dependent (Q6, failing at exactly the predicted 2.0801×) and exponents can
be chart-free (Q3, Q5, both exact). **So D4 is not an independent law; it is a
proxy that happened to correlate on a confounded sample.**

**A note on the literature, which was flagged in the prior-art note and matters
here.** Physics holds the *opposite* contrast — critical exponents are universal
within a universality class, amplitudes are not, and only certain *amplitude
ratios* are universal (Privman–Hohenberg–Aharony). D4 was filed from a sample that
appeared to invert the textbook. It did not: the sample was confounded, and once
the confound is removed the surviving statement — *the transferable content is a
ratio* — is the same shape as the universal-amplitude-ratio result, and as D2's
chart-free residue. **Novelty: N0 for the surviving content.** Nothing here needed
to be new; the value was in killing a stone that would otherwise have propagated.

---

## Boundaries

- **Four systems, two of them sharing a normal form**, all 1-D gradient systems
  with additive noise. Inherited from D1 and, as registered, **not** extended —
  the legs were reused deliberately so the numbers are comparable with published
  ones. Two of four are physics; D6 closed that gap, this does not re-close it.
- **Q1, Q2 and Q5 are identities on the fold/SIS pair** (both models are exactly
  cubic), declared in the pre-registration. The at-risk content was Q6 and the
  audit, and both went against D4.
- **The audit covers this repo only.** It says nothing about the literature's
  amplitude/exponent contrast, which runs the other way and was not under test.
- **"Chart-free" is assigned by construction here, not measured.** A quantity is
  labelled free if it is invariant under G_pow by inspection. A measured
  chart-invariance score — as [D3](../D3-chart-vs-ladder/) used — would be
  stronger and is not done here.
- **One silent-failure bug found and fixed mid-run**, recorded because it would
  have corrupted the control pair: the Blume–Capel leg was being evaluated at
  T = ⅔ + ε instead of ⅓ + ε (the caller and the function each added ⅓), so no
  crossover was ever bracketed and the empty fit returned 0.0000 without
  complaint. The corrected leg reproduces D1's published 0.6635. An assertion now
  refuses to fit a degenerate set.
