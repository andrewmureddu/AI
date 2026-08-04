# Invariants catalog

The master list of candidate cross-domain invariants. Each links to its own file.
"Level" is the **headline correspondence level** currently defended in the entry
(see [`../METHODOLOGY.md`](../METHODOLOGY.md) for the L0–L4 ladder). "Floor" is
where the entry sits in the map's architecture (see
[`../derivations/symmetry-sector.md`](../derivations/symmetry-sector.md) for the
derivation and [`FLOORS.md`](./FLOORS.md) for the full sort with reasons).
Levels and statuses are provisional and change as entries are worked.

**Three axes, all orthogonal.** *Level* (L0–L4) grades how well a correspondence
is established; *floor* ([`FLOORS.md`](./FLOORS.md)) says where it sits in the
tower; *chart* ([`CHARTS.md`](./CHARTS.md), added 2026-07-27) says whether its core
object survives reparameterizing the measurement axis. [D3](../experiments/D3-chart-vs-ladder/)
showed transfer needs a shared mechanism **and** a chart-free statement, and that
the level grades only the first — so a high-level entry with a chart-dependent core
is predicted *not* to travel.

To add one: copy [`_TEMPLATE.md`](./_TEMPLATE.md), fill it in, add a row here and a
column in [`../domains/README.md`](../domains/README.md). See
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## The floors, in one line each

| Floor | What it holds | Signature |
|:-----:|---------------|-----------|
| **1** | symmetry / conservation — *chooses Φ's coordinates* | a charge that can parameterize an invariant ensemble |
| **2** | Φ regular — *prediction* | ∇Φ, ∇²Φ, Φ*, −Φ of one convex function |
| **3** | Φ singular — *where prediction ends* | non-analyticity, null Hessian directions, lost supports |
| ~~4?~~ | *retired 2026-07-26* — not a floor but the tower's **structure group**: the floors are defined up to G_diff, cross-domain comparison has only G_pow, and the "scheme layer" is the difference ([D2](../derivations/D2-gauge-of-the-tower.md)) | a **log-ratio** exponent (ln N / ln b) — transformation data, not a fact; its chart-free residue is a **ratio** — the codimension p − 2 at a singularity ([D2](../derivations/D2-gauge-of-the-tower.md)), q1/q2 for support types ([D6](../experiments/D6-support-singularities/)), θ = ln n/−ln(β²γ) for a branching scheme ([P-D](../experiments/PD-allometry-reduction/)) |

Floors and ladder levels are **orthogonal**: a floor-3 entry can be L4 in physics
and L1 in finance. ▸facet marks entries that are *not independent invariants* —
derivative-faces of [#23](./free-energy-hub.md).

## Catalog

| # | Invariant | Core object | Level | Floor | Status | Notes |
|--:|-----------|-------------|:-----:|:-----:|--------|-------|
| 1 | [Power laws / scale-free](./power-laws.md) | P(x) ∝ x^−α | L2 (L3 per-mechanism) | **3** | developing | Where Z or its moments diverge |
| 2 | [Conservation & Noether](./conservation-noether.md) | symmetry ↔ conserved current | L4 (phys) / L2 (else) | **1** | developing | Bookkeeping half is *not* floor 1 |
| 3 | [Entropy & information](./entropy-information.md) | −Σ p log p ; MaxEnt | L3 (L2 downstream) | **2** ▸facet | developing | Φ*, the Legendre dual |
| 4 | [Diffusion & random walks](./diffusion-random-walks.md) | ∂u/∂t = D∇²u ; CLT | L3–L4 | **2** → 3 | developing | Splits at finite vs. infinite variance |
| 5 | [Criticality & universality](./criticality-phase-transitions.md) | RG fixed point; critical exponents | L4 (core) / L1–L2 (loose) | **3** | developing | Lee–Yang; the floor's L4 core |
| 6 | [Feedback & control](./feedback-control.md) | feedback loop; stability criterion | L2–L3 | **2 + 3** | seed | Splits, derived (S27) |
| 7 | [Optimization & variational](./optimization-variational.md) | argmin of functional; EL/KKT | L1–L2 | **2 + 1** | seed | Measure ⇒ 2, action ⇒ 1 |
| 8 | [Networks & percolation](./networks-percolation.md) | giant-component transition | L3 / L2 | **3** | seed | Connectivity = Φ-boundary |
| 9 | [Scaling & allometry](./scaling-allometry.md) | Y ∝ M^b | L2 (L3 contested) | **refuses** ✓tested | developing | θ = min(1, ln n/−ln(β²γ)) — not a Φ-derivative; the structure group's **invariant residue** ([P-D](../experiments/PD-allometry-reduction/) + [D2](../derivations/D2-gauge-of-the-tower.md)) |
| 10 | [Symmetry breaking](./symmetry-breaking.md) | G → H, order parameter | L4 (phys) / L2–L3 | **3** | seed | *Not* floor 1 — the sort's best case |
| 11 | [Fractals & self-similarity](./self-similarity-fractals.md) | fractal dim D ; Hurst H | L2 (L3 mechanistic) | **3 + 4?** | seed | D = ln N/ln b is a scheme signature |
| 12 | [Selection & replicator](./selection-replicator.md) | ẋ_i = x_i(f_i−f̄) ; Price eq. | L2–L3 | **2** ▸facet | seed | Same object as #17 |
| 13 | [Emergence & renormalization](./emergence-renormalization.md) | coarse-graining; relevant ops | L4 (RG) / L1 (loose) | **none** | seed | An *operation on* the tower |
| 14 | [Trade-offs & Pareto](./tradeoffs-pareto.md) | Pareto frontier | L1–L2 | **2** ▸facet | seed | A real frontier *is* a Legendre transform |
| 15 | [Duality & conjugates](./duality.md) | Fourier/Legendre transform | L2–L3 | **2 + 1** | seed | Legendre ⇒ 2, symplectic ⇒ 1 |
| 16 | [Information bottleneck](./information-bottleneck.md) | rate–distortion / IB curve | L2–L3 | **2** ▸facet | seed | Constrained-Φ object |

### Speculative tier (surfaced by [`../questions/SPECULATIVE.md`](../questions/SPECULATIVE.md))

These are "same object, different names" bridges. Treat every level as a hypothesis.

| # | Invariant | Core object | Level | Floor | Status | Bridges |
|--:|-----------|-------------|:-----:|:-----:|--------|---------|
| 17 | [Universal update (mirror descent)](./mirror-descent-update.md) | entropic mirror descent | **L3** (local; global≠shared) | **2** ▸facet | developing ✓derived | S1, S2 |
| 18 | [Optimal transport](./optimal-transport.md) | Wasserstein gradient flow (JKO) | L3? | **2** + open | seed·spec | S4 |
| 19 | [Spectral gap](./spectral-gap.md) | λ₂ of Markov/Laplacian | **L3** (one mechanism, family constants) | **3** ✓tested | developing ✓tested | mixing/sync/consensus |
| 20 | [Statistical geometry](./statistical-geometry.md) | Fisher/Ruppeiner/Fubini–Study metric | L3? | **2 ▸ 3** | seed·spec | S3 |
| 21 | [Noise thresholds](./noise-thresholds.md) | recoverability transition p_c | **L2–L3** (taxonomy) / L1 ("one threshold") | **3 + 4?** | developing ✓tested | S5 |
| 22 | [Critical slowing down](./critical-slowing-down.md) | autocorr→1, variance blow-up | L3–L4? | **3** | seed·spec | S6, S7 |

### Consolidations (a hub the other entries turn out to orbit)

Not a new bridge — a discovered *center*. Confirmed math, not speculative.

| # | Node | Core object | Level | Floor | Status | Absorbs |
|--:|------|-------------|:-----:|:-----:|--------|---------|
| 23 | [Free-energy hub](./free-energy-hub.md) | Φ = ln Z (log-partition) | **L3** (L4 via Lee–Yang) | **2 + 3** | developing | facets of #3, #12, #14, #15, #16, #17, #20 |

## Reading the levels honestly

The interesting entries are the ones that span the ladder: **#2 (Noether)**,
**#4 (diffusion)**, and **#5 (criticality)** each have a genuine L4 core *and* a
soft L1–L2 fringe where the term gets over-applied. A large part of the research
is drawing that internal line correctly, not just assigning one number.

## Reading the floors honestly

The [sort](./FLOORS.md) found an asymmetry worth stating here: **floor 2 collapses,
floor 3 stratifies.** Seven entries on floor 2 are one convex function
differentiated seven ways — genuine redundancy, marked ▸facet, and they should
stop being counted as independent evidence. The floor-3 entries are *not*
redundant with each other: they are different ways for a prediction field to end
(non-analyticity, divergent moments, null directions, lost supports), and
[S5](../experiments/S5-noise-thresholds/) showed they carry different exponents.
Six whole entries are deleted as independent, and #15 survives only in its
symplectic half — seven facet-faces in total. Effective independent count:
**23 entries → ~16**.

Three entries refused the tower altogether (#9, #13, and the type-R half of #21,
with #11's deterministic half joining them). They share a signature — a log-ratio
exponent rather than a Φ-derivative — which was read as evidence for a proposed
**fourth floor**, and equally as the tower's own falsifier.

**Resolved 2026-07-26 ([D2](../derivations/D2-gauge-of-the-tower.md)): there is no
fourth floor.** The floors are defined up to *G_diff* — reparameterizations smooth
at the singular point — while cross-domain comparison has only *G_pow* (φ ~ ε^a,
smooth away from the point but not at it). The shared log-ratio signature is the
**transformation data of one group relative to the other**, and a transformation
parameter is not a fact on any floor, which is why these entries refused. Their
chart-free residue is the **codimension p − 2**, i.e.
[D1](../experiments/D1-chart-invariance/)'s degeneracy order — floor-3 data. See
[`FLOORS.md`](./FLOORS.md) §4.
