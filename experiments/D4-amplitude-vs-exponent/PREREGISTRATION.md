# D4 pre-registration — written before any measurement

Works [D4](../../questions/UNKNOWN-LAWS.md): *dimensionless amplitudes transfer
across domains, bare exponents do not, and no counterexample in either direction
has been recorded.*

**Written before the code this time.** The register has now recorded three
misclassifications ([D1](../D1-chart-invariance/)'s P5 direction,
[D2](../D2-gauge-group/)'s resampling no-op, [D6](../D6-support-singularities/)'s
P2) and one outright omission ([D3](../D3-chart-vs-ladder/) had no
pre-registration at all). The D6 log's correction — *apply the identity/risk
split after the code exists, not only before* — is honoured by §3 being revisited
once the script is written, with any change recorded in place rather than
silently applied.

---

## 0. Prior-art note (written first)

**Old.** That dimensionless groups are the transferable content of a physical
relation is the whole of dimensional analysis and the Buckingham π theorem —
roughly a century old, and the reason engineering correlations are written in π
groups. That critical exponents are universal within a universality class while
amplitudes are not is standard critical phenomena; in fact the *textbook* form of
the amplitude/exponent contrast runs **opposite to D4's claim** — physics holds
that exponents are universal and amplitudes are not, with only certain *amplitude
ratios* universal.

**That opposition is the reason to run this.** D4 was filed from residue mining
over this repo's own results, which appeared to show the reverse. Either the repo
has found a real regime where the textbook contrast inverts, or D4's sample was
selected. The stone itself flags the second possibility and says it "should be
tested prospectively before being believed at all."

**Nearest miss.** Privman–Hohenberg–Aharony universal amplitude ratios are
precisely the statement that the transferable amplitude content is a *ratio*.
That is the same shape as [D2](../../derivations/D2-gauge-of-the-tower.md)'s
finding that the chart-free residue is a ratio, and if D4 reduces to it, D4 is
**N0** and only the audit is new.

---

## 1. Two parts

**Part A — the selection audit.** D4's evidence is retrospective: a table of
numbers this repo happened to report. The audit asks *what determined which
quantities got reported*, and specifically whether the amplitudes we published
were disproportionately chart-free and the exponents disproportionately bare. If
so, the sample was selected on chart-freedom without anyone intending it, and the
apparent amplitude/exponent law is a confound.

**Part B — a prospective battery.** A fixed set of systems, a fixed set of
quantities, chosen before measuring, **all reported**. Each quantity is
pre-labelled on *two* axes:

- **kind**: amplitude or exponent (D4's proposed variable)
- **chart**: chart-free or chart-dependent ([D2](../D2-gauge-group/)/[D3](../D3-chart-vs-ladder/)'s variable)

Because the battery deliberately contains **chart-free exponents** and
**chart-dependent amplitudes**, the two axes make different predictions and
exactly one can survive.

## 2. The battery

Systems (all already in the repo, all with published verdicts):

| System | Field | p | k |
|---|---|:--:|:--:|
| saddle-node fold | ecology / dynamical systems | 3 | ½ |
| SIS at R₀ = 1 | epidemiology | 3 | 1 |
| mean-field Ising | physics | 4 | 1 |
| Blume–Capel, tricritical line | physics | 6 | 1 |

Quantities, with both labels fixed in advance:

| # | Quantity | kind | chart |
|---|---|---|---|
| Q1 | k — exponent of λ vs ε | exponent | **dependent** |
| Q2 | β — exponent of the order parameter vs ε | exponent | **dependent** |
| Q3 | β/k | exponent | **free** |
| Q4 | crossover exponent, bare chart | exponent | **dependent** |
| Q5 | crossover exponent, λ chart | exponent | **free** |
| Q6 | C — prefactor of λ_c = C·D^θ | **amplitude** | **dependent** |
| Q7 | τ·λ | **amplitude** | **free** |

**The comparison group is the fold/SIS pair**: same degeneracy order p = 3, so
the same underlying singularity, but different fields, different charts (k = ½ vs
1) and different anharmonic coefficients. Anything genuinely transferable must
agree there.

**The control group is Ising/Blume–Capel**: different p, so even the chart-free
quantities should differ — which is what shows they are not vacuously constant.

## 3. Identity vs. risk

**Identities / already measured, and therefore not evidence for D4 either way:**

- Q1 and Q2 for the fold and SIS are closed-form (both models are exactly cubic),
  as [D1](../D1-chart-invariance/) and [D6](../D6-support-singularities/) both
  declared for these legs.
- Q5's equality across the fold/SIS pair follows from the u-rescaling argument,
  declared in D1 §4.
- Q3 = 1/(p−2) is derived in [D2](../../derivations/D2-gauge-of-the-tower.md) §6.

**Genuinely at risk — and note that the at-risk content here is D4's claim, not
the machinery:**

- **Whether Q6 transfers.** D4 says amplitudes transfer. Q6 is an amplitude. If
  it fails to transfer while Q3 and Q5 — both *exponents* — succeed, D4's axis is
  refuted by construction-free measurement.
- **Whether the audit finds selection.** Part A could come out either way.

## 4. Registered predictions

**P1 — the fold/SIS pair, chart-free quantities agree.** Relative spread of Q3,
Q5, Q7 across the two systems is **< 5%** each.

**P2 — the fold/SIS pair, chart-dependent quantities disagree.** Relative spread
of Q1, Q2, Q4 is **> 50%** each (all three differ by a factor of ~2 on theory).

**P3 — the decisive cell.** **Q6, an amplitude, fails to transfer**: relative
spread **> 50%** across the fold/SIS pair. Registered with the predicted value —
the crossover prefactor scales as g^{2/p}, so with g = ⅓ and 1 the ratio should be
3^{2/3} = **2.0801**, i.e. a spread of 108%.

**P4 — the axes are separated, and only one survives.** Grouping the seven
quantities by **chart** gives clean separation (all chart-free below 5%, all
chart-dependent above 50%). Grouping the same seven by **kind** gives **no
separation** — amplitudes split across both outcomes (Q7 transfers, Q6 does not)
and so do exponents (Q3, Q5 transfer; Q1, Q2, Q4 do not). Registered as the
headline: **kind explains nothing once chart is known.**

**P5 — non-vacuity control.** On the Ising/Blume–Capel pair (different p), the
chart-free quantities Q3 and Q5 **differ** by > 20%, confirming they are not
constants that agree with everything.

**P6 — the audit.** Predict that of the cross-domain quantities this repo has
reported as transferring, **all** are chart-free, and of those reported as failing
to transfer, **all** are chart-dependent — i.e. the retrospective sample is
perfectly confounded, and D4's regularity is entailed by the confound rather than
evidence for the amplitude/exponent axis.

## 5. What would kill the replacement

- **Q6 transfers** (spread < 5%) — then amplitudes really do transfer as a class,
  D4 survives, and the chart account is incomplete.
- **Q3 or Q5 fails on the fold/SIS pair** — then chart-freedom does not confer
  transfer either, and neither axis works.
- **The audit finds reported counterexamples** — a chart-free quantity that failed
  or a chart-dependent one that transferred, already in the record — which would
  break P6's confound story.

## 6. Scope

Four systems, two of them sharing a normal form, all one-dimensional gradient
systems with additive noise; inherited from D1 and not exceeded. Two of the four
are physics, the recorded gap D1 and D2 both left open and D6 closed — **not
closed again here**, since this battery reuses D1's legs deliberately so that the
numbers are comparable with the published ones. The audit covers only this repo's
own results and says nothing about the literature's amplitude/exponent contrast,
which runs the other way and is not under test.
