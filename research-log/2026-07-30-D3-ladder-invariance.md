# 2026-07-30 — D3: the ladder is not a chart-invariance count, and the residue is a fixed point

**Worked on:** [D3](../questions/UNKNOWN-LAWS.md#d3--the-ladder-is-a-chart-invariance-count),
the cheapest unworked discovery stone, flagged by both the
[D6](./2026-07-27-D6-support-singularities.md) and
[P-D/D2 reconciliation](./2026-07-27-PD-D2-reconciliation.md) passes; and, without
intending to, [`FLOORS.md`](../invariants/FLOORS.md) §4's live question about the
residue's general form.
**Change:** new experiment
[`D3-ladder-invariance/`](../experiments/D3-ladder-invariance/); D3 marked run and
**retired as stated**; `FLOORS.md` §4's live question **answered**; `SYNTHESIS.md`
§7.0's successor-to-the-P0 answered and replaced with a narrower one;
`METHODOLOGY.md` gains a failed-reduction note; **two corrections to paper 1**.

## What I did

D3 registered its own test: *add a chart-invariance measurement to each rung of
[`ladder-vs-transfer`](../experiments/ladder-vs-transfer/) and check it predicts the
transfer score better than the rung label does.* I did that, and then added two legs
D3 did not ask for, because the harness made them cheap and they were the only
genuinely at-risk parts. All five legs were pre-registered, including the disclosure
that the forward direction could not exceed N1 and that the attack leg was **expected
to fire**.

The measurement is the **aggregation chart order** H = d ln s(n)/d ln n, s(n) = IQR
of the n-aggregate. It is a log-response over a log-rescaling — §4's signature
exactly — and it is computed **inside one domain with no reference to any other
domain's samples**, which is what keeps it from being a restatement of the transfer
score. Cross-domain quantity: r = H_B/H_A, mismatch m = |r − 1|, per D2's rule that
bare exponents are gauge and ratios are not.

## What I found

**D3's own test passes.** H = 0.5006 (A), 0.5037 (L4), 0.4974 (L3), 0.6985 (L2),
−0.0011 (L1). The mismatch predicts the archival transfer skills at **R² = 0.998**
against **0.869** for the ordinal rung label, and it **ties L3 and L4** (0.006 vs
0.007) where the label predicts L4 > L3 and the measurement says −0.008. Under
φ_a(x) = sign(x)|x|^a the bare H spans **6.0×** with H/a pinned at 0.5006, while the
ratio is constant to **3.6e-4** — D2's rule reproduced in a system with **no
singularity and no Φ**, which is the class D2's own derivation cannot reach.
Re-charting B alone collapses skill from 0.894 to 0.239 / 0.091 / 0.000, so the
forward direction is interventional rather than observational.

Had I stopped where D3 asked, this would read as a promotion.

**The registered attack fires.** Increments X_i = U·z_i sharing one lognormal factor
U of coefficient of variation c: finite variance at every c, exchangeable but **not
independent**, assigned L2 before measurement by the harness's own criteria. The
common factor multiplies the sum, so it cannot touch how the sum's scale grows:

| c | 0.0 | 0.25 | 0.5 | 1.0 | 2.0 |
|---|:--:|:--:|:--:|:--:|:--:|
| mismatch m | 0.012 | 0.011 | 0.011 | 0.014 | 0.017 |
| transfer skill | 0.935 | 0.875 | **0.640** | **0.003** | **0.000** |

Below the L1 rung by c = 1.0, with the invariant pinned throughout. And it is not
slow convergence to A's law: shape distance between the n = 64 and n = 1024
aggregates is 0.006–0.025 — the sampling floor, the same order as the L4 rung's own
0.015 — while the distance *to* A's Gaussian is unchanged in n (0.073 → 0.075 at
c = 0.5). **The aggregation map has a one-parameter continuum of fixed points, all
carrying the eigenvalue H = ½.**

**Three things that costs.**

- **D3's biconditional is dead.** Chart-invariance in a ratio is *necessary, not
  sufficient*.
- **D3's explanation of the cliff's sharpness is dead too.** It argued the L2/L3 jump
  is sharp *because* a quotient is not a matter of degree. Here the quotient is fixed
  and transfer is continuous. (Paper 1 had independently retracted the cliff in
  favour of a ceiling; the two retractions agree, which is mild evidence both are
  right.)
- **The forward half that survives is N0–N1**, as the prior-art note said in advance:
  "an estimator generalizes iff it depends only on invariant structure" is IRM's
  thesis in this repo's vocabulary.

**The by-product is worth more than the stone was.** §4's live question — what the
residue is in general, given that D2's p − 2, D6's q1/q2 and P-D's θ are all ratios
reached by different routes — now has an answer, because this is the first measured
case where **the ratio is matched and the objects still differ**:

> **The residue is the fixed point of the description map. A ratio is only its
> eigenvalue.** Where the fixed-point set is a discrete list, the eigenvalue labels
> it and the residue *looks* like an integer — which is exactly the situation at a
> floor-3 germ, where normal-form theory supplies the list (the A_k series) that D2
> and D6 were in fact reading. Where the fixed-point set is a continuum, no finite
> collection of ratios classifies and the residue is a **shape**.

That explains why three independent routes all found ratios without licensing
"ratios are the general answer," which is what I would otherwise have been tempted
to write down. Three data points agreeing because they were all drawn from the same
special case is the failure mode this register was opened to avoid.

**A fourth result, and it is a caveat on the repo's own instrument.** P5's common-a
leg failed its registered threshold (deviation 0.551 against 0.05). The diagnosis is
a measurement, not a defence: skill is 1 − d/d_ref and d_ref is read *in the same
chart*, so **transfer skill is not a chart-invariant number** — the same preserved
correspondence reads 0.34 / 0.89 / 0.92 / 0.95 / 0.98 depending only on the chart.
Re-normalized by the in-chart sampling floor it is stable at 1.54–1.88× across a 6×
span of a, against 3.4–11.5× when only one domain is re-charted. So **D2's common-a
commitment holds outside physics** — but only once the normalizer is made
chart-internal, and every transfer number in the repo is chart-relative until then.

## Decisions

- **D3 retired as stated**, marked run with a restraint pass. It graduates nothing
  and earns no invariant entry. The forward direction is kept as a cheap *screening*
  test (measurable per-domain, before any joint modelling) and labelled N0–N1.
- **`FLOORS.md` §4's live question is answered** and replaced with a narrower one:
  a floor-3 object whose fixed-point set is a *continuum* should have a non-integer
  residue and should break the codimension count. Untested — D3's system has no
  floor-3 singularity to try it on — and logged as the cheapest next probe.
- **`METHODOLOGY.md` records the failed reduction.** The L3 mechanism criterion is
  not replaceable by an invariance count, and the reason is specific: what the
  counterexample breaks is *independence*, part of the mechanism and not a
  coordinate choice. This is the ladder being **vindicated by an attempt to
  eliminate it**, which is a better outcome than the promotion I was aiming at.
- **Paper 1 corrected twice.** L2's skill is **0.515 ± 0.050** at 32 seeds, not
  0.484 (an 8-seed low estimate; the independent-stream 8-seed value was 0.537), and
  the quoted "L2 max 0.538" is seed-limited — 0.629 at 32 seeds. Neither touches the
  paper's load-bearing claim (L2 is capped far below the 0.92 ceiling); the
  zero-overlap separation from L3 survives. The chart-relativity caveat is recorded
  in the same place.
- **A pre-registration error is on record, the fourth of its kind.** P2's threshold
  was set at 1e-6 relative, computed as if s(n) were an exact power law; the finite-n
  correction that also pushes L2's H off 2/3 makes the honest tolerance ~1e-3, and
  the measurement is 3.6e-4. `verdict.json` therefore reports `P2_holds: false` for a
  claim whose substance holds. Kept as written rather than revised.

## What this opens

- **The continuum test for the residue** (above). If it fails — if a continuum
  fixed-point set still yields an integer residue — then the fixed-point reading is
  wrong and the three ratios need three separate accounts after all.
- **The chart-internal normalizer should be retrofitted** to the `vary_n` sweep,
  whose ~0.5 plateau is quoted in chart-relative units. Cheap; changes no
  conclusion I expect, which is the reason to do it rather than assume it.
- **D4 is now the cheapest unworked D-stone** ("amplitudes transfer, exponents
  don't"), and D3 is a small piece of prospective evidence for it — but note that
  D4's registered caveat (its evidence is assembled from results kept *because* they
  held) is exactly the bias D3 just caught in the residue's three ratios. Worth
  running D4 with that specific worry in front of it.
- **P-C** remains unrun, still needing the selector/source distinction P-D found
  written into its registration.

## Next

- The continuum probe of the residue, on a floor-3 object.
- D4, run prospectively.
- The `vary_n` re-normalization.
