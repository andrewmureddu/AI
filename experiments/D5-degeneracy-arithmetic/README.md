# D5 — does the degeneracy order have arithmetic? (result)

**Question ([D5](../../questions/UNKNOWN-LAWS.md)):** if floor 3 is classified by
the degeneracy order, is that order conserved, additive, or bounded along a
sequence of transitions?

**Status: confirmed, and it confirms something that was never in doubt — exactly
as the pre-registration predicted it would. The arithmetic is *enumeration*:
terms in Φ queue rather than combine. The only measured content is the boundary
on when the arithmetic is *visible*, and the registered threshold for that was
optimistic by about a factor of two.**

Run it: `python3 run.py` (numpy only, ~8 min, deterministic — seed 20260727).
Registered first, and committed before any output existed:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## Two readings, and only one of them was open

**The literal reading — two transitions in succession — is coalescence, and
singularity theory already answers it.** Codimension is additive: two folds (A₂,
codim 1) colliding give a cusp (A₃, codim 2), so with codim = p − 2,

```
        p_composite  =  p_1 + p_2 - 2        (3 + 3 -> 4)
```

Degeneracy orders neither add nor max; their codimensions add. That is Thom and
Arnold, it was graded **N0** in the registration, and the numerical check (P5,
confirming the merged germ's leading order is 4) verifies essentially nothing
beyond the arithmetic being self-consistent. **The content of that section is the
citation, not the computation.** D5's own prior-art warning called this.

**The live reading exists only because [D6](../D6-support-singularities/) moved
the ground.** D5 was filed when the classifier was believed to be a single integer
*p*; D6 showed *p* was the q₁ = 2 slice of a pair. So the open question became:
what happens when Φ carries more than two terms?

Each higher term supplies its own rounding scale, the lowest governs first, and
the prediction is a **staircase** with the j-th plateau at 1 − q₁/q_j.

## Results

### P1/P2 — the staircase exists, with every plateau where predicted

Plateau width = decades of D over which the local slope sits within ±0.04.

| (q₁; higher terms) | plateau 1 | plateau 2 | plateau 3 |
|---|---|---|---|
| (2; 4, 6) | **0.5007** (3.75 dec) | **0.6662** (5.75 dec) | — |
| (2; 4, 8) | **0.5000** (4.25 dec) | **0.7500** (5.75 dec) | — |
| (2; 3, 6) | **0.3333** (3.75 dec) | **0.6666** (6.00 dec) | — |
| (1; 2, 4) | **0.5000** (4.25 dec) | **0.7500** (6.00 dec) | — |
| (2; 4, 6, 8) | **0.5068** (1.75 dec) | **0.6645** (3.25 dec) | **0.7452** (4.25 dec) |

Predicted: 0.5000 / 0.6667 / 0.7500 / 0.3333 as appropriate. Worst error across
all eleven plateaus is **0.0068**. The four-term system produces a genuine
**three-step staircase**, all within the registered ±0.05.

### P3 — the ratio rule

(1 − θ_j)/(1 − θ_{j+1}) should recover q_{j+1}/q_j:

| case | measured | predicted |
|---|---|---|
| (2; 4, 6) | 1.496 | 1.500 |
| (2; 4, 8) | 2.000 | 2.000 |
| (2; 3, 6) | 2.000 | 2.000 |
| (1; 2, 4) | 2.000 | 2.000 |
| (2; 4, 6, 8) | 1.470 / 1.317 | 1.500 / 1.333 |

All six inside the registered ±0.08. **So the staircase alone recovers the ratios
of the higher exponents** — the arithmetic is enumeration, and the terms do not
interact.

### P4 — the squeeze, and the one number that was actually measured

Raising B₃ at fixed B₂ moves the plateau switch (D_switch = B₂³/B₃² for this
family) and should narrow the lower plateau. Direction registered in advance, and
confirmed:

| B₃ | D_switch | regime width | lower plateau |
|---|---|---|---|
| 10⁸ | 10⁻¹⁶ | 0 dec (below grid) | **0.00 dec** |
| 10⁶ | 10⁻¹² | 0 dec (below grid) | **0.00 dec** |
| 10⁴ | 10⁻⁸ | 2 dec | **0.00 dec** |
| 10² | 10⁻⁴ | 6 dec | **3.75 dec** |
| 10⁰ | 10⁰ | 10 dec | **7.75 dec** |

The last two rows give the useful number: **a regime must exceed its visible
plateau by ≈ 2.25 decades**, consistently (6 → 3.75 and 10 → 7.75). So a plateau
is resolvable to ±0.04 only when its regime spans more than about 2.25 decades in
D, and is invisible below that.

**Registered as "squeezed out below ~1 decade" — the measured squeeze-out is
~2.25 decades.** The direction and the existence of a threshold are confirmed; the
threshold itself was optimistic by roughly a factor of two, and that is the
registration being wrong rather than the claim.

---

## Verdict

**The arithmetic is enumeration.** Terms in Φ queue rather than combine: each
contributes one plateau at 1 − q₁/q_j, the plateaus are independent, and their
ratios recover the higher exponents. Degeneracy orders do not add; along a
*coalescence* it is the codimension that adds.

**And this confirms almost nothing that was in doubt**, which the pre-registration
said in advance:

- §0's codimension additivity is **N0** — Thom and Arnold.
- Each plateau value is [D6](../D6-support-singularities/)'s formula applied to
  one pair, and the ratio rule is those values divided. **N0–N1**, declared as
  identities before the run.
- The only genuinely measured content is P4's ≈2.25-decade overhead, and even that
  is as much a property of the ±0.04 tolerance as of the physics.

**Honest grade: N0–N1 overall.** D5 closes the discovery register without adding a
law. That is a legitimate outcome for a stone whose registration predicted exactly
it, and it is worth more than the alternative — the staircase picture is now
*checked* rather than assumed, and P4 converts [P8](../D1-chart-invariance/P8-REREGISTRATION.md)'s
failure into a quantitative condition: P8's Blume–Capel sextic plateau never
established because its regime did not span 2.25 decades.

---

## Boundaries, including a process failure

- **Synthetic multi-term potentials by construction**, because the point was to
  control the number and separation of terms. The real-model counterpart is P8's
  Blume–Capel result, cited rather than re-run — and P4 now explains it.
- **One-dimensional gradient systems, additive noise, one control parameter.**
  Inherited from D1/D6 and not exceeded. Support-type (q₁ = 1) appears in one leg.
  Essential singularities remain floor 3's unclassified remainder, untouched.
- **P5 is near-vacuous as implemented**, and is labelled so above rather than
  presented as a check that carried weight.
- **A design error caught before any output existed.** The first coefficient set
  used B₃ = 10⁶ throughout, which puts the (2;4,6) switch at D = 10⁻¹² — below the
  swept grid, so only one plateau could ever have appeared. That is arithmetic
  from the registered formula, not a result, so the correction is recorded in the
  code rather than treated as tuning.
- **A process failure, and the fifth of its kind in this register.** A `pkill`
  returned exit 144 and killed the *shell* rather than the Python process, so the
  superseded run finished afterwards and **overwrote `verdict.json` with
  stale-coefficient results**. Those numbers were read and nearly written up. The
  tell was an internal contradiction: P1 and P4 compute the same system at
  B₃ = 10², and reported 0.00 and 3.75 decades for the same plateau — two numbers
  that cannot both be right for one computation. Caught by the arithmetic not
  closing, not by the pre-registration. Every result above is from the run whose
  stored `terms` field reads 10², verified before use.
