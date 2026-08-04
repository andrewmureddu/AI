# D2 — the gauge group of the tower (result)

**Question ([D2](../../questions/UNKNOWN-LAWS.md), the map's standing P0):** four
things [refused the tower](../../invariants/FLOORS.md) with one shared signature —
a log-ratio. Are they a **fourth floor**, floor 1 in disguise, or coordinate
freedom? Tests
[`derivations/D2-gauge-of-the-tower.md`](../../derivations/D2-gauge-of-the-tower.md).

**Status: the derivation holds. There is no fourth floor — the scheme layer is
the tower's structure group, and its chart-free residue is the codimension, which
is [D1](../D1-chart-invariance/)'s *p* − 2. The counter-horn survives, in the
part the derivation predicted it would.**

Run it: `python3 run.py` (numpy only, ~20 s, deterministic — seed 20260726).
Registered first: [`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## What was tested

Two groups of reparameterizations ε ↦ φ(ε) fixing the singularity at 0:

```
   G_diff   phi'(0) exists and is nonzero        (smooth at the singular point)
   G_pow    phi(eps) ~ c eps^a,  a > 0           (smooth AWAY from it, not at it)
```

G_diff ⊊ G_pow, and the enlargement lives **entirely at the singular point** —
i.e. exactly on floor 3.

**Part A** asks how RG eigenvalues behave under each. **Part B** asks what is left
when the gauge is removed.

## Results

### Part A — the legs recover their known values

| Leg | Field | Measured | Known |
|---|---|---|---|
| R1 1D Ising decimation | statistical mechanics | y = **1.0000000000** | 1 exactly |
| R2 diamond hierarchical lattice | statistical mechanics | y = **0.747236**, ν = **1.338266** | ν ≈ 1.338 |
| R3 logistic period doubling | nonlinear dynamics | δ = **4.669201** | 4.6692016 |

### P1 — RG eigenvalues are G_diff-invariant (theorem check)

Six random conjugations of a 2×2 RG map: **max |y − y_true| = 5.3e-15**.
Eigenvalues are conjugation invariants, so this could not have come out
otherwise; it checks the code.

### P2 — RG eigenvalues are G_pow-covariant, y → a·y (theorem check)

| a | R1 | R2 | R3 |
|---|---|---|---|
| 1/3 | 0.333333 | 0.249079 | 0.741059 |
| 1/2 | 0.500000 | 0.373618 | 1.111588 |
| 2 | 2.000000 | 1.494471 | 4.446352 |
| 3 | 3.000000 | 2.241707 | 6.669527 |

Relative error ≤ **2.4e-12** (R1), **5.7e-10** (R2), **1.8e-8** (R3) against a·y.
Registered with the direction, and the direction is right: y **multiplies** by a,
because ν = 1/y divides by it. Also a theorem check.

**So an RG eigenvalue and D1's chart order have identical transformation
behaviour.** `FLOORS.md`'s log-ratio signature is not four unrelated quantities
happening to rhyme — it is the transformation datum of G_pow relative to G_diff.

### P3 — what survives which group

With y = [0.75, −1.30] (one relevant, one irrelevant direction):

| Action | magnitudes | ratio | signs | count of relevant |
|---|---|---|---|---|
| G_diff (conjugation) | invariant | invariant | invariant | invariant |
| G_pow, **common** a | **change** | **−0.576923 at every a** | invariant | invariant |
| G_pow, **independent** a | change | **−0.144 / −4.327 / −0.231** | invariant | invariant |

The independent-a row is the derivation's own caveat, made explicit rather than
argued away: if each eigendirection may be re-charted separately, ratios die too
and **only signs and counts survive**. The common-a commitment is what buys the
ratios, and it is a modelling commitment — a domain supplies one notion of
distance to threshold, not one per eigendirection.

### P4 — the residue is the codimension (AT RISK)

β/k measured on the models, against the derivation's 1/(p−2):

| Leg | p | β | k | β/k | predicted | status |
|---|:--:|:--:|:--:|:--:|:--:|---|
| fold | 3 | 0.5000 | 0.5000 | **1.0000** | 1.0000 | identity |
| SIS | 3 | 1.0000 | 1.0000 | **1.0000** | 1.0000 | identity |
| **mean-field Ising** | 4 | 0.5000 | 1.0000 | **0.5000** | 0.5000 | **at risk — passes** |
| **Blume–Capel (tricritical)** | 6 | 0.2502 | 0.9996 | **0.2503** | 0.2500 | **at risk — passes** |

β spans 4× (0.25 → 1.00) and k spans 2× (0.50 → 1.00) across the legs, so the
ratio's constancy is not vacuous. The two full models — carrying every higher
order — land within 0.0000 and 0.0003 of the reciprocal codimension.

### P5 — the gauge claim, operationally (AT RISK)

Under ε′ = ε^a the two exponents move exactly as they must (Ising: β = 0.500 →
1.000 / 0.250 / 0.167, k = 1.000 → 2.000 / 0.500 / 0.333), while the
**observable–observable** relation m ~ λ^{1/(p−2)}, which never mentions ε, does
not move:

| Leg | predicted | spread across four samplings |
|---|:--:|:--:|
| fold | 1.0000 | 1.8e-15 |
| SIS | 1.0000 | 8.9e-16 |
| Ising | 0.5000 | 7.7e-08 |
| Blume–Capel | 0.2500 | 6.5e-05 |

**A correction made mid-run, on the record.** The first implementation
"resampled" by building a log-uniform grid in ε′ — but a power map sends a
log-uniform grid to a log-uniform grid, so the ε points were *identical* and the
invariance was definitional rather than tested. The reported version samples
linearly in ε′, which maps back to genuinely different ε points. The exponents
above are stable across those, which is the honest version of the claim: the
relation is a real power law over the range, not an artifact of how it was
sampled.

Even so, **P5 is closer to a demonstration than a test**, and it is worth saying
why rather than banking it: the reason an observable–observable relation is
chart-free is that it does not contain the chart. That is the *content* of
"gauge," not evidence for it. The at-risk part of P5 is its *value* matching
1/(p−2) on full models — which is P4 again, viewed sideways.

### P6 — the falsifier hunt found nothing

The invariants of the common-a action θ ↦ θ/a on an exponent vector are exactly
the degree-zero functions — ratios and signs. Demonstrated: Σ|y| moves with a
(0.675 → 2.250 → 5.625 → 15.750) while ratios and counts do not. **No chart-free
quantity depending on an exponent's magnitude was found**, which is the registered
expectation and the thing that would have restored the fourth floor.

---

## Verdict

**The P0 is answered, and the answer is that the question presupposed too much.**
The scheme layer is neither a fourth floor nor floor 1 in disguise. It is the
**structure group** the tower was always implicitly defined up to: G_diff is what
its floors are defined modulo, G_pow is all that cross-domain comparison has, and
the scheme layer is the difference. That is why its members are all log-ratios,
why they refused floors 1–3 — a transformation parameter is not a fact on any
floor — and why four unrelated objects carried the *same* signature.

**The chart-free residue is one integer.** Signs, counts and ratios are not three
survivors but three faces of the codimension p − 2: the number of coefficients that
must be tuned to sit on the singularity, the number of relevant RG directions, and
the reciprocal of β/k. **So what was under the fourth floor was
[D1](../D1-chart-invariance/)'s *p*.**

> **⟳ Scoped 2026-07-27 by [D7](../D7-residue-projective/).** True as measured, and
> true of a **smooth floor-3 germ** — but "one integer" is the n = 2, integer-slope
> case. In general the residue is the log-slope vector modulo the diagonal ℝ⁺, with
> **n − 1** invariants (measured at n = 5), and it is not intrinsically discrete:
> incommensurable leading exponents give 0.68169 (= 1 − 1/π) and 0.70698 (= 1/√2).
> P3's common-*a* caveat is derived there rather than assumed.

**The counter-horn survives — where the derivation said it would.** "An RG
eigenvalue predicts which perturbations are relevant" is a claim about a *sign*,
and signs are G_pow-invariant (P3). The predictive work is real; it just lives in
the part that is not gauge. Quoting the *magnitude* 0.747 requires also quoting
the chart.

**And it explains an asymmetry the sort recorded without explaining.**
`FLOORS.md` found that floor 2 collapses while floor 3 stratifies. Away from the
singular point G_pow = G_diff, so floor-2 objects live under the ordinary smooth
group where tensorial quantities have genuine invariants — one convex function
seen from seven angles. At the singular point the group is strictly larger, eats
exponent magnitudes, and leaves a discrete residue. **The asymmetry is a statement
about which group acts where**, and it was not built from that observation.

**Exponents are not thereby meaningless**, which is the worry D1 left open.
Universality is a G_diff statement and under G_diff exponents are strictly
invariant (P1) — physics fixes the chart canonically because reduced temperature
enters the Hamiltonian linearly. **Within a domain, exponents are facts; across
domains, only ratios, signs and counts are.** S5 and S7 compared G_diff-facts
across a G_pow gap.

---

## Boundaries

- **Most of this experiment is a theorem check**, declared in advance. P1, P2, P3
  are linear algebra and one line of exponent arithmetic; they test the code and
  the setups, not the world. The at-risk content is P4/P5, and it is two legs.
- **Both at-risk legs are physics.** Identical to the gap D1 recorded and did not
  close. The fold and SIS legs are exactly-cubic and their β/k = 1 is closed-form
  — flagged in the pre-registration as a mid-writing correction, since the
  registered text had implied all four legs were full models.
- **The common-a commitment is load-bearing and is a commitment.** P3 shows
  explicitly that independent per-direction re-charting destroys the ratios. The
  argument for common-a is that a domain supplies one distance-to-threshold, which
  is a claim about scientific practice, not a theorem.
- **Degeneracy-type singularities only.** Support-type singularities (S5's type S)
  have no *p*, so the identification of the residue with the codimension does not
  reach them — though §2–§5 of the derivation, which never mentions *p*, does.
  What the residue is there is [D6](../../questions/UNKNOWN-LAWS.md), still open.
- **One control parameter.** A critical *surface* approached along a path raises
  the common-vs-independent question in a form the derivation settles by
  assumption.
- **Prior-art risk is real and partly realised.** The G_diff half is Wegner's
  nonlinear scaling fields in the RG literature's own language, and the
  smooth-vs-topological conjugacy distinction is standard in dynamical systems.
  The N2 claim is confined to the architectural reading — the scheme layer as this
  tower's structure group, and its residue as *p* − 2.
