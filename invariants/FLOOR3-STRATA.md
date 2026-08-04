# Floor 3, sorted by stratum

*2026-07-28. The second sort. [`FLOORS.md`](./FLOORS.md) sorted the catalog into
the tower's three floors; this sorts **floor 3 into its three strata**, which
[`derivations/base-variable.md`](../derivations/base-variable.md) §4 showed are
forced rather than chosen.*

`FLOORS.md` §2 found that **floor 2 collapses and floor 3 stratifies**, listed the
strata — "non-analyticity, divergent moments, null Hessian directions, support
loss, soft modes" — and called classifying them open work. The base-variable
derivation closed that: writing every prediction field as Φ_Y(λ) = log E_P[e^(λ·Y)],
a log-Laplace transform has exactly three ways to fail to be nice, so the
stratification is a consequence.

Like the floor sort, **this is a test rather than bookkeeping**: it makes claims
about entries nobody has examined, and it emits a prediction that can come out
wrong. One already has — see §4.

---

## 1. The strata, as the experiment corrected them

The derivation stated the trichotomy as *domain boundary / limit / degeneracy*, and
[`experiments/F3-strata-rounding/`](../experiments/F3-strata-rounding/) was run to
test the sharpest thing that follows — "**only 3b rounds**". **That prediction was
wrong**, and the correction is worth more than the prediction was.

3a's boundary also appears only in a limit. At finite support Φ is entire — that is
the derivation's own F-fact — so "the domain boundary is stable in system size" was
not merely mis-measured, it was **not well posed**. What survives, and is cleaner,
is a classification by **what diverges**:

```
   3a   Phi ITSELF diverges, on a REGION of lambda      limit over SUPPORT
   3b   Phi finite; a DERIVATIVE diverges, at a POINT   limit over SIZE
   3c   Phi analytic; a derivative is exactly ZERO      EXACT at finite size
```

Measured, one instrument, one set of tolerances:

| stratum | exemplar | signature |
|---|---|---|
| **3a** | Exp(1) truncated at M | Φ(0.9) converges to **2.302585093** (= −log 0.1, increments **0**); Φ(1.1) grows as **M^0.981** — linearly, without bound |
| **3b** | two-state free energy | localised width **117×** the instrument floor, shrinking as **N^−1.001** |
| **3c** | functionally dependent statistics | **no localised feature** (width = **1.000×** the full window); smallest eigenvalue of the exact ∇²Φ at **8.9e-16**, the noise floor |
| *(type C — **not** floor 3)* | an argmin crossing | width pinned at the **resolution floor** at every size ([P-K](../experiments/PK-kink-taxonomy/)) |

Four distinguishable outputs, and the fourth is the useful boundary of the whole
scheme: a selector cell boundary is not a non-analyticity of any Φ_Y, which is why
it neither rounds nor lives on a floor.

---

## 2. The sort

| # | Entry | Stratum | Why | Basis |
|--:|-------|:-------:|-----|-------|
| 1 | [power laws](./power-laws.md) | **3a** | Heavy tails are exactly where the mgf's domain has a boundary. | the entry's own statement |
| 4 | [diffusion](./diffusion-random-walks.md) (tails) | **3a** | Lévy = divergent moments. **This is P-B's criterion restated** — see §3. | [P-B](./FLOORS.md) |
| 5 | [criticality & universality](./criticality-phase-transitions.md) | **3b** | Lee–Yang: the non-analyticity requires the thermodynamic limit. | textbook |
| 8 | [networks & percolation](./networks-percolation.md) | **3b** | The Potts q→1 non-analyticity is a limit fact. | [S27](../derivations/S27-control-split.md) |
| 9 | [scaling & allometry](./scaling-allometry.md) | **3b** | Measured: analytic at every finite depth, width ∝ N^−0.973. | [P-K](../experiments/PK-kink-taxonomy/) ✓ |
| 10 | [symmetry breaking](./symmetry-breaking.md) | **3b + 3c** | **Splits, and `FLOORS.md` already named both halves**: SSB needs the limit (3b); Goldstone modes are null ∇²Φ directions (3c). | [symmetry-sector](../derivations/symmetry-sector.md) |
| 11 | [fractals](./self-similarity-fractals.md) (statistical half) | **3b** | Self-affinity *at a critical point* inherits the critical point's stratum. | prediction |
| 6 | [feedback & control](./feedback-control.md) (floor-3 half) | **3a + 3c** | **Splits**: unreachable supports are 3a; null Fisher directions are 3c. | [S27](../derivations/S27-control-split.md) |
| 19 | [spectral gap](./spectral-gap.md) | **3c** | A null direction of the trajectory free energy's Hessian; Φ analytic. | [P-A](../experiments/PA-spectral-gap/) ✓ |
| 20 | [statistical geometry](./statistical-geometry.md) (floor-3 half) | **3c** | The metric degenerating *is* ∇²Φ losing rank. | the entry |
| 21 | [noise thresholds](./noise-thresholds.md) | **3a + 3c** | **Splits, and already measured as such**: type S (support loss) is 3a; type M (metric merge) is 3c. [D6](../experiments/D6-support-singularities/)'s q1 = 1 vs q1 = 2 is this distinction. | [S5](../experiments/S5-noise-thresholds/), [D6](../experiments/D6-support-singularities/) ✓ |
| 22 | [critical slowing down](./critical-slowing-down.md) | **3c** | The Hessian going soft — a degeneracy, not a non-analyticity. | [S7](../experiments/S7-critical-slowing/) ✓ |

**Basis column, honestly:** ✓ means an experiment measured it. The rest are the
sort's claims and can be wrong — the same status `FLOORS.md` §5 gives its `seed`
assignments.

**Two things the sort does not touch.** The scheme-layer refusers are gauge, not
floor 3 ([D2](../derivations/D2-gauge-of-the-tower.md)); and #7's readouts are
classified by response type, not stratum ([P-C](../experiments/PC-variational-kinds/)).

---

## 3. What the sort produces

A sort earns its keep by saying something about entries it had no hand in shaping.

**(a) P-B is subsumed, and its falsifier sharpens.** [P-B](./FLOORS.md) predicted
diffusion splits at finite-vs-infinite variance. That boundary **is** the 3a
criterion — the mgf's domain — so P-B is not an independent prediction but an
instance. Its untested half therefore gains a stronger form: a finite-variance
diffusion whose Φ misbehaves must be **3b or 3c, never 3a**. A finite-variance
process with a genuine domain boundary would break the trichotomy, not just P-B.

**(b) Critical slowing down is the 3c shadow of a 3b transition.** #22 is 3c, #5 is
3b, and they co-occur — the Hessian goes soft *on the approach to* a non-analyticity.
The sort predicts this is **one-directional**: every 3b transition carries a 3c
degeneracy on its approach, but 3c occurs without any 3b transition.
**Already confirmed, and it cost a result**: [P-A](../experiments/PA-spectral-gap/)
found a double well where the gap falls **3540×** while local curvature *rises* 6× —
a 3c fact with no transition anywhere — which is exactly why S7's τ·λ = 1 turned out
to be a **single-basin** law. The sort retrodicts the boundary condition that
experiment paid for.

**(c) A prediction about an unexamined repo result, registered and now tested.**
[S25](../experiments/S25-rlct-singularity/) measured λ(P) = min(P,D)/2 with a kink at
P = D and nobody classified it. The sort says **3c, not 3b** — a rank degeneracy,
exact at every finite D — against S25's own report of "a finite-size critical window
blurring λ̂ right at the singular point", which sounds like 3b rounding.
**Confirmed:** the (D+1)-th eigenvalue of the population Fisher matrix is
**≤ 3.11e-17** of the first at every D ∈ {4, 8, 16, 32}, with rank/2 = min(P,D)/2 to
**0.0e+00**. So the kink does not round, and **S25's blurring is a property of its
estimator at finite sample, not of the object** — a distinction S25 did not draw.

**(d) The strata have different repair routes**, which is the practical payoff:

- **3a** is fixed by **changing the base variable** — a bounded functional of a
  heavy-tailed Y has no domain boundary. This is why M11's exit-time reformulation
  worked where a state-space one would not have.
- **3b** cannot be fixed. It is the physics, and it is the only stratum where the
  singularity is the phenomenon rather than an artifact of description.
- **3c** is fixed by **dropping a coordinate** — a degenerate ∇²Φ means the base
  variable is over-parameterized, which is
  [`base-variable.md`](../derivations/base-variable.md) §5's rank reading.

---

## 4. What the sort's own test did to it

Registered: *only 3b rounds*. **Measured: 1 of 4 at-risk predictions passed.**

The one that passed is the one that mattered — (c) above, the prediction about an
entry the sort had no hand in shaping. The three that failed were all my criteria
rather than the sort's content, and two of them improved it:

- **3a's boundary is a limit too**, so "stable in system size" was not well posed.
  Repaired to "what diverges", which is sharper and is what §1 now states.
- **I asked the kink instrument for a *sharp* kink in a 3c object**, which has no
  kink at all — Φ is analytic and the degeneracy is in the eigenvalues. The
  instrument returned the full window, which is its correct way of saying "no
  localised feature", and that turned out to be the **fourth** output in §1's
  table. A category error caught by the instrument.
- A **power law fitted to values at the machine noise floor** (4.4e-17 … 8.9e-16),
  which measures nothing.

That is the fifth, sixth and seventh instance of
[`METHODOLOGY.md`](../METHODOLOGY.md)'s named anti-pattern, and the second pass in
a row where **every failure was a criterion and none was a claim**. The rate is not
falling; what has changed is that the repairs now arrive in the same run.

---

## 5. Boundaries of this sort

- **Most assignments are predictions.** Only #9, #19, #21, #22 and half of #10 rest
  on measurement; the rest are the sort's claims. Marked in the Basis column.
- **Splits are real and not a hedge.** #6, #10 and #21 genuinely occupy two strata,
  and in #21's case both halves were measured before this sort existed.
- **The exemplars are synthetic.** §1's table demonstrates the four signatures are
  distinguishable; it does not show every catalog entry sits where the sort puts it.
- **3a is exhibited by truncation**, a limit over support rather than over degrees
  of freedom. That the two limits behave differently is the claim, and it is the
  one this experiment's failure forced into the open.
- **Nothing here is new mathematics.** Finite-size rounding, the mgf's domain, and
  matrix rank are old; the claim is the exhaustiveness and the sorting, and if a
  reader thinks that is just finite-size scaling plus linear algebra, the
  prior-art note in the experiment agrees.
