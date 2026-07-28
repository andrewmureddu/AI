# The catalog, tagged by chart

*2026-07-27. The second axis [D3](../experiments/D3-chart-vs-ladder/) forced into
[`METHODOLOGY.md`](../METHODOLOGY.md), applied.*

[D3](../experiments/D3-chart-vs-ladder/) found that transfer needs **two**
independent things — a shared mechanism *and* a claim stated chart-freely — and
that the ladder grades only the first. It measured the consequence directly: with
the mechanism untouched but the claim chart-dependent, an L3 correspondence
transfers at 0.000, and a word-only L1 one can beat a theorem-backed L4 one.

So a level is not enough to say whether an entry will travel. This document
supplies the missing tag, and — like [`FLOORS.md`](./FLOORS.md) — it is a **test,
not bookkeeping**: it makes predictions about entries nobody has examined from
this angle.

**The tag.** Is the entry's *core object* invariant under reparameterizing the
measurement axis — a ratio, a dimensionless product, a sign, a count, an ordinal
relation — or does it move — a bare exponent, a magnitude in domain-specific units,
a coordinate-dependent value?

---

## 1. The tags

| # | Entry | Level | Core object | Chart | Why |
|--:|-------|:-----:|-------------|:-----:|-----|
| 1 | [power laws](./power-laws.md) | L2 | P(x) ∝ x^−α | **dependent** | α is a bare exponent; x → x^a rescales it |
| 2 | [conservation & Noether](./conservation-noether.md) | L4/L2 | dQ/dt = 0 | **free** | a zero is a zero under any monotone map; the charge's *value* is not |
| 3 | [entropy & information](./entropy-information.md) | L3 | −Σ p log p | **splits** | discrete entropy is a function of probabilities, not labels → free. Differential entropy shifts by the log-Jacobian → dependent |
| 4 | [diffusion & random walks](./diffusion-random-walks.md) | L3–L4 | CLT / ∂u/∂t = D∇²u | **dependent** | "the normalized sum is Gaussian" survives affine maps, not power maps — **this entry is literally D3's experiment** |
| 5 | [criticality & universality](./criticality-phase-transitions.md) | **L4** | critical exponents | **splits** | exponents are G_diff-invariant and G_pow-covariant ([D2](../derivations/D2-gauge-of-the-tower.md)); *ratios*, signs and the relevant-direction count are free |
| 6 | [feedback & control](./feedback-control.md) | L2–L3 | stability criterion | **splits** | "is stable" is a sign → free; gain and phase margins are magnitudes → dependent |
| 7 | [optimization & variational](./optimization-variational.md) | L1–L2 | argmin of a functional | **free** | being a stationary point is chart-free; its *location* and *value* are not |
| 8 | [networks & percolation](./networks-percolation.md) | L3/L2 | giant-component transition | **splits** | the transition's existence is free; p_c's value depends on how the edge measure is parameterized |
| 9 | [scaling & allometry](./scaling-allometry.md) | L2 | Y ∝ M^b | **free** ✓ | looks like a bare exponent, but [P-D](../experiments/PD-allometry-reduction/) showed θ = ln n/−ln(β²γ) is a **log-ratio fixed by counts** — and it transferred at spread 4.0e-15 |
| 10 | [symmetry breaking](./symmetry-breaking.md) | L4/L2–L3 | G → H | **splits** | the group quotient is a discrete structural fact → free; the order parameter's magnitude → dependent |
| 11 | [fractals & self-similarity](./self-similarity-fractals.md) | L2 | D = ln N/ln b | **dependent** | bi-Lipschitz invariant but not homeomorphism invariant; it is the chart order of a self-similar map (D2 §3) |
| 12 | [selection & replicator](./selection-replicator.md) | L2–L3 | ẋ_i = x_i(f_i − f̄) | **free** | relative growth rates — a ratio |
| 13 | [emergence & renormalization](./emergence-renormalization.md) | L4/L1 | relevant vs irrelevant | **splits** | the relevant/irrelevant *sign* is free (D2 §4); eigenvalue magnitudes are not |
| 14 | [trade-offs & Pareto](./tradeoffs-pareto.md) | **L1–L2** | Pareto frontier | **free** ★ | Pareto dominance is purely *ordinal* — invariant under any monotone reparameterization of every axis |
| 15 | [duality & conjugates](./duality.md) | L2–L3 | Legendre / Fourier | **free** | the duality relation is covariant; conjugate pairing survives re-charting |
| 16 | [information bottleneck](./information-bottleneck.md) | **L2–L3** | I(X;T), I(T;Y) | **free** ★ | mutual information is invariant under *any* invertible reparameterization of either variable |
| 17 | [universal update](./mirror-descent-update.md) | **L3** | x ∝ x·e^{−ηg} | **free** | a multiplicative ratio rule; η carries the units, the update does not |
| 18 | [optimal transport](./optimal-transport.md) | L3? | Wasserstein flow | **dependent** | W₂ is defined by a ground metric, and the ground metric is a chart choice |
| 19 | [spectral gap](./spectral-gap.md) | L3 | λ₂ | **dependent** ✓ | a bare eigenvalue magnitude — and [P-A](../experiments/PA-spectral-gap/) already measured family constants spanning **1.54×** |
| 20 | [statistical geometry](./statistical-geometry.md) | L3? | Fisher metric | **splits** | a metric is a *tensor*: scalar invariants built from it are free, components are not |
| 21 | [noise thresholds](./noise-thresholds.md) | L2–L3 | recoverability p_c | **splits** ✓ | [S5](../experiments/S5-noise-thresholds/)'s α spans 1.00→3.17 (dependent); its discriminator "α = order of vanishing of χ²_sym" is free |
| 22 | [critical slowing down](./critical-slowing-down.md) | L3–L4 | τ·λ = 1 | **free** ✓ | a dimensionless product of conjugates — and [S7](../experiments/S7-critical-slowing/) measured it transferring (0.94 ± 0.13) while its exponents did not |
| 23 | [free-energy hub](./free-energy-hub.md) | L3/L4 | Φ = ln Z | **splits** | Φ shifts by a log-Jacobian; its derivatives with respect to *natural* parameters are covariant |

✓ = the tag is confirmed by an experiment already in the repo, not just assigned.
★ = an entry whose chart status is **better than its rung**, which is where the
tag makes its most falsifiable claims (§3).

Count: **free 8 · dependent 6 · splits 8** (of 22 numbered entries plus the hub).

---

## 2. What the tag retrodicts

Four entries carry a ✓ because an experiment had already measured the thing the
tag predicts, before this document existed:

- **#22 critical slowing down** — free, and S7 measured τ·λ transferring across
  three domains at 0.94 ± 0.13 *while its exponents spanned −½/−1/−2*. The entry
  splits exactly along the tag.
- **#19 spectral gap** — dependent, and P-A measured family constants spanning
  1.54×, filed at the time as a disappointment ("one number demoted to one
  mechanism"). The tag says that was the expected outcome.
- **#21 noise thresholds** — splits, and S5 measured both halves: α varying
  1.00→3.17 against a discriminator that held to 0.0015.
- **#9 allometry** — the interesting one. It *looks* like a bare exponent, which
  would make it dependent and predict failure. P-D found θ is a **log-ratio fixed
  by counts** and it transferred at spread 4.0e-15. The tag is only correct here
  because P-D did the reduction; assigning it from the surface form would have got
  it wrong. **Recorded as a warning: the tag must be applied to the object after
  reduction, not to how the entry is written.**

---

## 3. What it predicts (the part that makes this a test)

**P-C1 — the catalog's strongest entry is predicted not to travel.**
[#5 criticality](./criticality-phase-transitions.md) is the map's only unqualified
**L4**, and its core object — critical exponents — is chart-dependent. So the tag
predicts that its exponents transfer *within* a universality class (a shared
chart, per D2 §7) and **fail across fields that share no chart convention**, while
its *ratios*, signs and relevant-direction counts transfer in both cases. A high
rung does not protect it. **Falsifier:** a bare critical exponent agreeing across
two fields with no shared chart convention.

**P-C2 — two low-rung entries are predicted to over-perform.** ★-marked above:

- **#14 Pareto (L1–L2)** is *ordinally* invariant — Pareto dominance survives any
  monotone reparameterization of every axis independently, which is a stronger
  invariance than anything else in the catalog. Predict it transfers better than
  its rung implies.
- **#16 information bottleneck (L2–L3)** rests on mutual information, invariant
  under any invertible reparameterization of either variable. Same prediction.

These are the tag's most falsifiable claims, because the ladder predicts the
opposite ordering. **Falsifier:** either fails to transfer where a chart-dependent
higher-rung entry succeeds.

**P-C3 — #18 optimal transport is predicted to be the weakest L3 candidate.** Its
core object depends on a ground metric, which is a chart choice, and
[`FLOORS.md`](./FLOORS.md) already flags it as fitting neither the three floors
nor the proposed fourth. The tag says those are the same observation.

**P-C4 — the `splits` entries should split *in measurement*, not just on paper.**
Eight entries are tagged splits. For each, the free half should transfer and the
dependent half should not, measured on the same systems. #21 and #22 already show
this. The other six are open.

---

## 4. Boundaries of this tag

- **The tag is assigned by inspection, not measured.** [D3](../experiments/D3-chart-vs-ladder/)
  measured chart-invariance by applying an explicit group and watching transfer
  degrade; nothing here does that. Every row is a *claim* about the entry's core
  object, and #9 is the standing proof that inspection can get it wrong.
- **Only one group.** "Chart" throughout means G_pow acting on the measurement
  axis, as in [D1](../experiments/D1-chart-invariance/)/[D2](../derivations/D2-gauge-of-the-tower.md).
  Richer re-measurement groups are untested.
- **Chart-freedom is necessary, not sufficient.** D3 established this and D4
  confirmed it from the other side: a chart-free amplitude still fails when the
  underlying systems genuinely differ (P-A's Kuramoto families). A `free` tag
  predicts an entry *can* travel, not that it does.
- **Chart-freedom has a price.** Measured in D3 against paper 1's ceiling: the
  chart-free statement tops out at 0.833 where a shared-chart statement reaches
  0.916 ≈ complete transfer. Invariance buys robustness, not maximal skill, so a
  `free` tag is not straightforwardly better.
- **Levels and floors are unaffected.** This is a third axis, orthogonal to both
  ([`FLOORS.md`](./FLOORS.md) is the second). Nothing here promotes or demotes.
