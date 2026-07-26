# M3 pre-registration — written before any measurement

Per [`questions/L3-MECHANISMS.md`](../../questions/L3-MECHANISMS.md)'s working
rule: *register the discriminator's expected value before measuring it.* Nothing
below is revised after the run; results live in [`README.md`](./README.md).

**Mechanism under test (M3).** Local branching on a locally tree-like graph: a
giant component exists iff the expected number of *new* nodes reached per node
reached exceeds 1. Claimed to be the same process behind random-graph
percolation, epidemic thresholds (R₀), polymer gelation, and network robustness.

**Why this one.** It is [essay 04's falsifier 1](../../essays/04-the-periphery-split.md),
which names the degree-preserving rewiring test and has never been run. The
essay's demand is precise: a Φ-reduction of connectivity must do **predictive
work** — recover p_c-shifts under rewiring from Φ-derivatives alone.

---

## The theory (stated before the run)

For a configuration-model graph with degree distribution p_k, write
κ = ⟨k²⟩/⟨k⟩. Bond percolation has

    p_c = ⟨k⟩/(⟨k²⟩ − ⟨k⟩) = 1/(κ − 1)

With degree **correlations** this generalises. Let e_{jk} be the probability
that a random edge joins nodes of excess degrees j and k, and q_j = Σ_k e_{jk}.
The branching operator on edge-ends is

    T_{kj} = j · e_{jk} / q_j ,        p_c = 1 / λ_max(T)

and when e_{jk} = q_j q_k this collapses to λ_max = Σ_j j q_j = κ − 1, recovering
the uncorrelated result.

**The two facts that make this the sharp test of the map's architecture:**

1. A double-edge swap (a,b),(c,d) → (a,d),(c,b) preserves **every node's
   degree exactly**. So ⟨k⟩, ⟨k²⟩, κ and the whole degree histogram are
   invariant — and the degree histogram is precisely the sufficient statistic
   of the maximum-entropy graph ensemble with degree constraints, i.e.
   everything a Φ built on node degrees can see.
2. Newman's assortativity r is, at fixed degree sequence, a monotone function of
   S₁ = Σ_edges k_u k_v alone; and a swap changes it by
   **ΔS₁ = (k_a − k_c)(k_d − k_b)**. So r is controllable in O(1) per swap, and
   swaps with k_a = k_c preserve it *exactly*.

## Registered predictions

**P1 — Molloy–Reed on uncorrelated graphs.** For ≥3 degree distributions
(Poisson, power-law with cutoff, bimodal), the measured threshold — located as
the peak of the finite-cluster susceptibility χ(p) = Σ'_c s_c²/Σ'_c s_c — matches
1/(κ−1) computed from the realised degree sequence within **5%**.

**P2 — rewiring control.** Random double-edge swaps preserve degrees and leave
the graph uncorrelated: p_c unchanged within **3%**, λ_max unchanged within 3%.
This shows the swap machinery is not itself the cause of any shift below.

**P3 — the discriminator.** Assortative and disassortative rewiring, with the
degree sequence asserted **bit-for-bit identical** throughout, move p_c: the
assortative graph has the *lower* threshold, the disassortative the higher, and
the extremes differ by **≥15%** for the heavy-tailed degree distribution. Sign
registered explicitly: assortative mixing raises λ_max, hence lowers p_c.

**P4 — the corrected criterion transfers.** p_c = 1/λ_max(T) predicts the
measured threshold for *every* rewired variant within **8%** — i.e. the pair
statistic e_{jk} recovers what the degree histogram lost.

**P5 — (degrees, r) is still not enough.** Construct two graphs with identical
degree sequence and matched assortativity, |r_X − r_Y| < 0.01, whose λ_max differ
by ≥5% (assortativity concentrated among hubs versus spread across the bulk).
Predict their measured p_c differ by **≥5%**, each predicted by 1/λ_max. If this
holds, the exponential family with degree *and* assortativity constraints is
still insufficient for connectivity.

**P6 — where the tree-like assumption breaks (exploratory).** Triangle-enriched
rewiring at fixed degrees. Clustering creates redundant paths that the branching
argument double-counts, so predict measured p_c sits **above** 1/λ_max by ≥5% at
high clustering — i.e. e_{jk} is sufficient for locally tree-like graphs and
insufficient once clustering is real.

## The Φ question, stated so it cannot come out vacuous

M11's lesson was that "does X reduce to Φ?" is under-specified until the base
variable is named, and that a check comparing an object to a rewriting of itself
proves nothing. So the claim here is stated as a **hierarchy of ensembles**, each
with named sufficient statistics, and the experiment decides where connectivity
first becomes recoverable:

| Ensemble | Sufficient statistics | Predicts p_c? |
|---|---|---|
| degree-constrained (configuration model) | p_k, i.e. ⟨k⟩, ⟨k²⟩ | P1 yes / P3 **no** |
| degree + assortativity | p_k and r | P5 **no** |
| edge-pair ensemble | e_{jk} | P4 yes / P6 no at high clustering |

The outcome is informative whichever way it falls: if p_c is a Φ-derivative of
the *pair* measure but not of the node measure, then connectivity does not need a
separate axis — it needs the base variable moved, exactly as
[M11](../M11-stochastic-resetting/) found for exit times. If even e_{jk} fails,
connectivity carries structure no fixed-order ensemble captures.

## What would kill M3

- Rewiring leaves p_c unchanged (P3) — the degree histogram *does* determine
  connectivity and essay 04's premise was wrong.
- 1/λ_max fails to predict the rewired thresholds (P4) — the branching mechanism
  is not what sets p_c in correlated graphs.
- The measured uncorrelated thresholds miss 1/(κ−1) (P1) — the estimator or the
  graph construction is broken, and nothing downstream is interpretable.
