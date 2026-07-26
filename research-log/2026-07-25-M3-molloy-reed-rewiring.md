# 2026-07-25 — Restraint: the degree histogram does not determine connectivity

**Worked on:** [M3](../questions/L3-MECHANISMS.md) (Molloy–Reed branching), which
is [essay 04's falsifier 1](../essays/04-the-periphery-split.md) — named there
since 2026-07-22 and never run.
**Change:** new experiment
[`experiments/M3-molloy-reed-rewiring/`](../experiments/M3-molloy-reed-rewiring/);
M3 gains a ⟳ note; essay 04 gains a fourth restraint pass. No catalog level
changed.

## What I did

Degree-preserving rewiring. A double-edge swap holds every node's degree fixed,
so the degree histogram — the sufficient statistic of the degree-constrained
maximum-entropy graph ensemble, i.e. everything a Φ built on node degrees can
see — is bit-for-bit identical before and after. If p_c moves, connectivity is
not a Φ(degree)-derivative. Essay 04 demands that any Φ-reduction do
*predictive work* on exactly this shift.

## What I found

**Essay 04's factual claim holds, with room to spare.** At identical degree
sequences (checked per-node, not just as a histogram), rewiring moves the
threshold by **35% / 72% / 148%** on bimodal / trimodal / power-law graphs.
Random swaps move it <2.5%, so the swap machinery isn't the cause.

**But the pair statistic recovers it.** The leading eigenvalue of the edge-end
branching operator predicts the shifts to **≤4.6%** — a 41% shift predicted to
1.7%. So connectivity *is* log-partition machinery, built on the **edge-pair**
measure rather than the node measure. That is M11's "Φ of what?" lesson arriving
a second time, from the other side of the map. Two independent arrivals in two
days makes the base-variable question the sharpest thing on the board.

**P5 is the leg worth remembering, because the construction failed and the
question got answered anyway.** I wanted two graphs with identical degrees *and*
identical assortativity but different thresholds. Two rewiring attempts failed:
a tight constraint band gave matched r but only 3% λ separation; a loose band
gave 2.6% separation and let r drift apart. Rather than keep tuning an
optimiser, I computed the answer exactly — with three degree classes the
symmetric e_{jk} at fixed marginals has three free parameters, fixing r removes
one, and the remaining 2-D polytope can just be scanned. Result:

    lambda_max in [7.810, 8.730] at fixed degrees AND fixed r  -- an 11.8% range

So (degrees, r) provably does not determine the threshold, and my rewiring had
been a weak optimiser reaching 3% of an available 12%. The scan then *hands you
the target*: rewiring toward the polytope's maximiser reached **100.0% of the
analytic range**, giving two graphs with identical degrees, **Δr = 1×10⁻⁵**, and
thresholds **11.9% apart** — predicted ratio 0.895, measured 0.881.

Two smaller things fell out. The configuration-model graph sits exactly at the
**minimum** of the feasible λ range at its own r. And with only *two* degree
classes the test is impossible — fixed marginals plus r determine e_{jk}
completely — which is why my first attempt, on a bimodal graph, could never have
worked. Three classes is the minimum at which "degrees + assortativity" can fail.

**The boundary is signed and measured.** The branching argument assumes local
tree-likeness, and it fails in the registered direction when loops appear:
p_c sits *above* 1/λ_max by **+10.4%** at clustering 0.030 and **+124%** at 0.211.
The second of those was not designed as a clustering test — it is the strongly
assortative power-law variant that failed P4 — and its failure is explained by
the same mechanism, since assortative rewiring on a scale-free graph builds a
dense looped hub core. One boundary, two routes to it.

## Decisions

- **Comparisons are ratios at fixed N, not absolute thresholds.** The
  susceptibility-peak estimator is biased high at finite N; P1 handles that by
  finite-size extrapolation over N = 10k…80k, and every downstream leg uses
  ratios where the common offset cancels. The first version of this experiment
  compared absolute values and produced 160% "errors" that were nothing but that
  offset plus the power-law case's non-convergence.
- **Power-law graphs are reported but excluded from P1's pass/fail.** With
  α = 2.7 the threshold still drifts at N = 80k, so a fixed-exponent
  extrapolation isn't valid there. Saying so is better than quietly dropping the
  case or quietly counting it.
- **No catalog level moved.** Simulated graphs only; M3's claim is cross-domain
  identity (epidemics, gelation, robustness) and one percolation study is not
  that. What is established is that the discriminator fires.

## Next

- The base-variable question now has two independent arrivals (M11: exit times;
  M3: edge pairs) and deserves its own derivation rather than another
  experiment. The question to write down: **is there a rule for which base
  variable a given question needs?** Candidate answer to test — the base
  variable is fixed by what the question quantifies over (states, exit times,
  pairs), and the "tower" is a family indexed by that choice.
- `SYNTHESIS.md` is now three sessions out of date and this makes it worse: it
  still describes one hub with a periphery. Flagged again, not addressed.
- Register order: **M8** (extreme value / best-of-n) next, then **M10** (TUR).
