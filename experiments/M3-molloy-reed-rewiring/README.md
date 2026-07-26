# M3 — does the degree histogram determine connectivity? (result)

**Question ([M3](../../questions/L3-MECHANISMS.md)):** local branching on a
locally tree-like graph — the mechanism claimed to be shared by random-graph
percolation, epidemic thresholds, gelation and network robustness. The
discriminator is **degree-preserving rewiring**, which is
[essay 04's falsifier 1](../../essays/04-the-periphery-split.md): the essay names
this test and nobody ran it.

Why it bites: a double-edge swap holds every node's degree fixed, so the degree
histogram — the sufficient statistic of the degree-constrained maximum-entropy
graph ensemble, i.e. **everything a Φ built on node degrees can see** — is
bit-for-bit identical before and after. If p_c moves, connectivity is not a
Φ(degree)-derivative.

**Status: confirmed on every registered prediction. The degree histogram does
not determine connectivity; the pair statistic e_{jk} does, up to the point
where local loops appear.**

Run it: `python3 run.py` (numpy + scipy, ~6 min, verified identical across runs).
Predictions registered in [`PREREGISTRATION.md`](./PREREGISTRATION.md) before any
measurement; that file is unedited.

## Results

| # | Prediction | Result | |
|---|-----------|--------|---|
| **P1** | Molloy–Reed within 5% | **3.7%** max (bounded degree, finite-size extrapolated) | ✓ |
| **P2** | random swaps neutral | ratios **0.977 / 0.982 / 0.991** | ✓ |
| **P3** | rewiring moves p_c ≥15% at fixed degrees | **35% / 72% / 148%** | ✓ |
| **P4** | 1/λ_max predicts the shift within 8% | **≤4.6%** (tree-like) | ✓ |
| **P5** | (degrees, r) still insufficient | **11.8%** range, constructed at **Δr = 1e-5** | ✓ |
| **P6** | clustering pushes p_c above prediction | **+10.4%** at C=0.030, **+124%** at C=0.211 | ✓ |

### P3 — the discriminator

Degree sequences asserted **bit-for-bit identical** across all variants (not just
the histogram — the per-node array). Same degrees, different wiring:

| graph | r | λ_max | p_c measured |
|---|---:|---:|---:|
| trimodal, assortative | +0.936 | 13.43 | **0.0800** |
| trimodal, unrewired | −0.004 | 7.81 | 0.1352 |
| trimodal, disassortative | −0.849 | 5.75 | **0.1777** |

A **72% spread in the percolation threshold** with the degree histogram frozen.
Bimodal gives 35%, power-law 148%. Random swaps move it by <2.5%, so the swap
machinery is not the cause.

### P4 — the pair statistic recovers what the histogram lost

Compared as **ratios** to the unrewired graph, which cancels the finite-size
offset (P1 shows that offset is ~+2% and common to all measurements at fixed N;
comparing absolute values would not cancel it):

| variant | measured ratio | predicted λ_config/λ_variant | error |
|---|---:|---:|---:|
| trimodal assortative | 0.5918 | 0.5816 | **1.7%** |
| trimodal disassortative | 1.3148 | 1.3589 | 3.3% |
| bimodal assortative | 0.7281 | 0.7632 | 4.6% |
| bimodal disassortative | 1.0776 | 1.1254 | 4.2% |

A 41% shift predicted to 1.7% from a statistic the degree histogram does not
contain.

### P5 — (degrees + assortativity) is still not enough

Settled two ways, because the first attempt at a construction failed.

**Exactly.** With three degree classes the symmetric e_{jk} with fixed marginals
has three free parameters; fixing r removes one, leaving a 2-D polytope that can
simply be scanned. Over 12995 feasible points at **fixed degrees and fixed r**:

    λ_max ∈ [7.810, 8.730]   — an 11.8% range   ⇒   p_c ∈ [0.1145, 0.1280]

So λ_max is provably not a function of (degree sequence, r). Worth noting: the
configuration-model graph sits exactly at the **minimum** of that range.

**Constructively.** Rewiring toward the polytope's λ-maximising e_{jk} reaches
**100.0% of the analytic range**:

| | r | λ_max | p_c measured |
|---|---:|---:|---:|
| unrewired (polytope minimum) | −0.003870 | 7.810 | 0.1352 |
| rewired (polytope maximum) | −0.003860 | 8.730 | 0.1191 |

**Assortativity matched to 1×10⁻⁵**, degree sequence identical, and the
thresholds differ by **11.9%** — predicted ratio 0.8946, measured 0.8808, agreeing
to 1.5%.

A separate observation: with only **two** degree classes this test is impossible,
because fixed marginals plus r determine e_{jk} completely. Three classes is the
minimum at which "degrees + assortativity" can fail — which is why the first
attempt, run on a bimodal graph, could never have worked.

### P6 — where the mechanism's own assumption breaks

The branching argument assumes local tree-likeness. Enrich triangles at fixed
degrees and the prediction fails in the registered direction — measured p_c
*above* 1/λ_max, because loops make the branching process double-count paths:

| graph | clustering C | prediction error |
|---|---:|---:|
| all tree-like variants | ≤0.0015 | ≤4.6% |
| triangle-rewired trimodal | 0.0301 | **+10.4%** |
| power-law, strongly assortative | 0.2110 | **+124%** |

The power-law assortative case was *not* designed as a clustering test — it is
the P3 variant that failed P4 — and its failure is explained by the same
mechanism: assortative rewiring on a scale-free graph builds a dense, heavily
looped hub core (C = 0.21). One boundary, two routes to it.

## Verdict

Reading the legs as a hierarchy of ensembles, which is how the prereg framed it
so the Φ question could not come out vacuous:

| Ensemble | Sufficient statistics | Predicts p_c? |
|---|---|---|
| degree-constrained (configuration model) | ⟨k⟩, ⟨k²⟩ | **no** — 72% spread at fixed degrees (P3) |
| degree + assortativity | p_k and r | **no** — 11.9% spread at Δr = 1e-5 (P5) |
| edge-pair ensemble | e_{jk} | **yes**, to ≤4.6% (P4) — until loops (P6) |

So connectivity is **not** a Φ-derivative of the node-degree measure, and essay
04's premise survives its own falsifier: the histogram genuinely does not
determine the threshold. But it *is* recovered by a log-partition-style object on
the **edge-pair** measure — which is [M11](../M11-stochastic-resetting/)'s
"Φ of what?" lesson arriving a second time, now from the connectivity side rather
than the exit-time side. The base variable moves from node to edge-pair; the form
does not change.

The residue is real and small: e_{jk} is sufficient only while the graph is
locally tree-like, and clustering breaks it in a specific, signed, measurable way.

**No catalog level moved.** These are simulated graphs, and the claim M3 makes is
cross-domain identity (epidemics, gelation, robustness), which one percolation
study does not establish. What is established is that the *discriminator* fires.

## Boundaries

- All graphs simulated; no empirical network. The cross-domain legs (epidemic
  thresholds on real contact networks, gelation) are untouched.
- p_c is located as the peak of the finite-cluster susceptibility, which is
  biased high at finite N. P1 handles this by finite-size extrapolation over
  N = 10k…80k; everything downstream uses **ratios at fixed N**, where the bias
  cancels. Absolute thresholds in the rewiring tables should not be read as
  asymptotic values.
- The finite-size fits are noisy for bounded-degree graphs (R² = 0.45–0.86)
  because the drift is small relative to realisation noise; for those, the
  un-extrapolated value at the largest N is within 2.2% anyway.
- **Power-law graphs never reach the asymptotic regime here.** With α = 2.7 the
  threshold drifts with N (0.0854 → 0.0737 from 10k to 80k) and a
  fixed-exponent extrapolation is not valid. Power-law results are reported and
  excluded from the P1 pass/fail.
- P5's polytope scan is written for exactly three degree classes; the general
  statement (that e_{jk} has slack at fixed r whenever there are ≥3 classes) is
  argued, not scanned, beyond that case.
- Bond percolation only, on undirected simple graphs. Site percolation and
  directed/weighted variants untested.
