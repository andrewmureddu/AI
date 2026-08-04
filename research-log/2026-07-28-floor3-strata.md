# 2026-07-28 — The second sort: floor 3 into its strata, and what it costs S25

**Worked on:** [`FLOORS.md`](../invariants/FLOORS.md) §2's "floor 3 stratifies —
open work", now closed by [`base-variable.md`](../derivations/base-variable.md) §4.
**Change:** new sort [`invariants/FLOOR3-STRATA.md`](../invariants/FLOOR3-STRATA.md)
+ test [`experiments/F3-strata-rounding/`](../experiments/F3-strata-rounding/);
the trichotomy is **restated** by its own failed prediction; **P-B is subsumed**;
**S25's kink is classified and its blurring reassigned to the estimator**.

## What I did

The last log named this as "cheap, mechanical, and would grade the classification
the way the floor sort graded the tower." That is the right reason to do it: a sort
makes claims about entries nobody has examined, so it is a test rather than
bookkeeping — and the floor sort is what produced P-A, P-D and P-C.

Sorted every floor-3 entry into 3a/3b/3c, then ran the sharpest thing that follows.

## What I found

**The sort's own sharpest prediction is wrong, and the correction is worth more.**
I registered *only 3b rounds*, with 3a distinguished as the stratum that does not
need a limit. It does. At finite support Φ is entire — the derivation's own F-fact,
which I had written a week's worth of passes ago and did not apply to my own
registration — so 3a's boundary appears only as M → ∞, exactly as 3b's kink appears
only as N → ∞. "λ_c stable in system size" was **not well posed**.

**What survives is cleaner: classify by what diverges.**

    3a   Phi ITSELF diverges, on a REGION of lambda      limit over SUPPORT
    3b   Phi finite; a DERIVATIVE diverges, at a POINT   limit over SIZE
    3c   Phi analytic; a derivative is exactly ZERO      EXACT at finite size

Measured, one instrument: Φ(0.9) converges to **2.302585093** (= −log 0.1,
increments exactly 0 by M = 10⁶) while Φ(1.1) grows as **M^0.981** — Φ itself
diverging on a region; 3b gives a **localised** width **117×** the resolution
floor, shrinking as **N^−1.001**; 3c gives **no localised feature at all** (width =
1.000× the full window) with the smallest eigenvalue of the exact ∇²Φ at 8.9e-16.

**And a fourth output, which is the scheme's useful boundary.** [P-K](./2026-07-28-PK-kink-taxonomy.md)'s
selector cell boundary returns a width pinned at the *resolution floor* at every
size. It is not a floor-3 stratum — a selector boundary is not a non-analyticity of
any Φ_Y — and the instrument separates it from all three without being told.

**The one prediction that could have embarrassed the sort passed.** A sort earns
its keep on entries it had no hand in shaping, and this one had exactly one:
[S25](../experiments/S25-rlct-singularity/)'s λ(P) = min(P,D)/2 kink, never
classified. Predicted **3c, not 3b** — against S25's own report of "a finite-size
critical window blurring λ̂ right at the singular point", which sounds like 3b.
Measured: rank/2 = min(P,D)/2 to **0.0e+00** and the (D+1)-th eigenvalue at
**≤ 3.11e-17** of the first, for D = 4, 8, 16, 32. **The kink does not round.** So
S25's blurring is a property of its finite-sample *estimator*, not of the object —
a distinction S25 did not draw and this forces.

**Three further things the sort produces.**

1. **P-B is subsumed.** Its finite-vs-infinite-variance split *is* the 3a criterion
   (the mgf's domain), so P-B is an instance rather than an independent prediction,
   and its untested half sharpens: a finite-variance diffusion whose Φ misbehaves
   must be 3b or 3c, **never** 3a.
2. **Critical slowing down is the 3c shadow of a 3b transition** — #22 is 3c, #5 is
   3b, and the sort predicts the relation is one-directional. **Already confirmed
   and it cost a result**: [P-A](../experiments/PA-spectral-gap/) found a double
   well with the gap falling 3540× while curvature *rises* — 3c with no transition
   — which is exactly why S7's τ·λ = 1 turned out to be single-basin. The sort
   retrodicts the boundary condition that experiment paid for.
3. **The strata have different repair routes**: 3a is fixed by changing the base
   variable (why M11's exit-time reformulation worked), 3b cannot be fixed (it is
   the physics), 3c is fixed by dropping a coordinate (the base variable is
   over-parameterized).

**1 of 4 at-risk, 2 of 2 identities — and all three failures are criteria, not
claims.** Besides P2 above: I fitted a power law to eigenvalue ratios sitting at
the 1e-16 machine floor, and I asked a **kink-finder to find a kink in a 3c
object**, which has none — Φ is analytic and the degeneracy is in the eigenvalues.
The instrument returned the full window, its correct way of saying *no localised
feature*, and that turned out to be the fourth signature I had failed to register
as the right answer. A category error caught by the instrument rather than by me.

## Decisions

- **`FLOORS.md` §2's open work is closed and the closure is restated.** Not
  "domain boundary / limit / degeneracy" but **what diverges** — Φ on a region, a
  derivative at a point, or nothing. The experiment's failure forced the better
  form.
- **S25's entry gains a classification and loses an implication.** The kink is 3c;
  the blurring it reported is estimator-side. Recorded in the sort, not as a level
  change — no ladder position moves.
- **P-B is retired as an independent prediction** and folded into 3a as an
  instance, with a sharper falsifier than it had.
- **No catalog level moved.** Same standard as the last three passes.
- **Fifth, sixth and seventh instance of the same anti-pattern**, and the second
  consecutive pass where every failure was a criterion and none a claim. The rate
  is not falling. What has changed is that the repairs now arrive in the same run
  rather than the next one, which is worth something but is not the fix.

## Next

- **Use the base-variable rule prospectively** — still the honest test of the
  derivation, still unrun. [Q6](../questions/OPEN-QUESTIONS.md) (urban scaling) is
  the candidate, and the reason it was skipped this pass is worth recording: the
  models I would need are ones I can only reconstruct from memory, and the repo's
  own rules say not to assert a citation I cannot check.
- **M8** (extreme value / best-of-n) — deferred six times now, which is itself
  evidence about how this agenda actually selects work.
- **The sort's unmeasured assignments.** Eight of the twelve rows are predictions.
  #1 (power laws → 3a) and #5 (criticality → 3b) are the cheapest to cash.
- **Continuous-transition rounding** ([P-K](./2026-07-28-PK-kink-taxonomy.md)'s
  extension): 3b was measured only on min-of-two-branches exemplars, where the
  width goes as N^−1. A continuous transition should give L^(−1/ν), and if it does
  not, 3b is narrower than the sort claims.
