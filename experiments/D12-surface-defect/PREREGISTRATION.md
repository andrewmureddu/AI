# D12 pre-registration — written before any production measurement

Works [D12](../../questions/UNKNOWN-LAWS.md#d12--does-the-order-0-defect-scale-as-the-surface-in-short-range-models):
[`SYNTHESIS.md`](../../SYNTHESIS.md) §7.0'(a), the P0 that
[D10](../D10-composition-lens/) left open. D10 measured the order-0 (concavity)
defect at **N^1.0252** for long-range first-order and **exactly 0** for a 1-D
chain whose entropy is log-binomial — so the zero was nearly an identity. The
version with teeth is a short-range interacting model in d ≥ 2 with a
first-order transition, where the defect should scale as the **surface**,
N^{(d−1)/d}. A third value would make D10's order-0 clause a classifier; an
exponent of 1 would break it.

The prior-art note is in the register entry and was written first. It
concludes **N0 for the scaling itself** — the convex intruder of a finite
short-range s(e) being set by the interface free energy is Binder (1982) and
Lee–Kosterlitz (1990) in canonical language, and Gross / Janke in
microcanonical language. The stone's only claim to content is *placement*:
whether D10's order-0 defect, with D10's exact definition and D10's hull code,
takes the value (d−1)/d, so that order 0 sorts systems into three classes.

**What was done before this file was written** (and nothing else):
1. `wl.c` (Wang–Landau) and `enum.c` (exact enumeration) written and compiled.
2. **Code validation** against exact enumeration on three small lattices
   (2-D q=3 L=4, 2-D q=2 L=5, 3-D q=2 L=3): same set of populated levels in
   all three, max |Δ ln Ω| = 0.0047 / 0.0025 / 0.0026. No defect was
   computed.
3. **Pilots** at sizes excluded from every fit (2-D L=8, 3-D L=6), used only
   to place energy windows: the bitangent of the hull runs over
   e = −1.94 → −0.52 (q=20), −1.88 → −0.77 (q=10), −2.50 → −0.69 (3-D q=10).
   The pilots' defect values were not computed or looked at.

---

## 0. The definition (D10's, unchanged)

s(e) = ln Ω(E)/N with e = E/N, E = −(number of satisfied bonds), periodic
hypercubic lattice, J = 1. ŝ = exact upper concave envelope (D10's
monotone-chain hull, copied verbatim). **Defect D(N) = N · max_e [ŝ(e) − s(e)].**
The exponent b is the slope of ln D against ln N.

Ω comes from Wang–Landau (1/t schedule, Belardinelli–Pereyra), restricted to an
energy window that contains the bitangent. **Window rule:** the window is valid
only if both hull vertices bounding the widest hull edge lie strictly inside it,
at least 2% of the window width from either end; if a production run violates
this, the window is widened and the run repeated, and the violation is reported.

Settings, fixed now: ln f_final = 1e-6; flatness 0.8; seeds 1–4 (2-D) and 1–3
(3-D). Point estimate = defect from the seed-averaged ln Ω (the mean of the
seeds' ln Ω curves after aligning each to zero mean over the window). Error =
standard deviation across seeds' individual defects / √n_seeds. Exponent b from
an unweighted least-squares fit of ln D on ln N over the registered sizes; its
error = sd across seeds of the per-seed slopes / √n_seeds.

| system | transition | sizes (fit set) | window e = −k/N |
|---|---|---|---|
| 2-D Potts q=20 | strong 1st order, ξ_d = 2.70 | L = 12, 16, 24, 32, 48 | [−1.99, −0.30] |
| 2-D Potts q=10 | 1st order, ξ_d = 10.56 | L = 16, 24, 32, 48, 64 | [−1.97, −0.55] |
| 3-D Potts q=10 | strong 1st order | L = 8, 10, 12, 14 | [−2.90, −0.45] |
| 2-D Ising (q=2) | **continuous** — the control | L = 8, 12, 16, 24, 32 | [−1.98, −1.30] |

---

## 1. At-risk predictions

**P1 — the core (2-D q=20).** b = **0.50 ± 0.08**. Fails if b lies outside
[0.42, 0.58]. The two named alternatives, 0 (short-range first-order does not
violate order 0 at all) and 1 (short-range is indistinguishable from
long-range), must each be excluded by more than 3 error bars — otherwise the
leg is recorded as *not discriminating*, whatever the central value.

**P2 — the dimension enters (3-D q=10).** b = **0.667 ± 0.10**, i.e. in
[0.567, 0.767]. This is the leg that makes "(d−1)/d" more than "something
between 0 and 1": the formula has d in it, so it needs two d. Same
3-error-bar discrimination requirement, against both 0.5 and 1.

**P3 — the magnitude (2-D q=20).** At the largest size, D/L lies within
**10%** of the exact interface free energy **2σ_od = 0.370988** (Borgs–Janke;
Billoire–Neuhaus–Berg tabulate it; the periodic box carries two interfaces of
length L, so D → 2σ_od·L). This is what turns "an exponent near ½" into "the
defect *is* the interface". Expected to be approached from below; the
direction is not registered.

**P4 — q=10 is in the crossover, and says so.** The largest L is ≈ 6 ξ_d, so I
do not register b = ½ for q=10. Registered: b in **[0.35, 0.85]**, D/L at the
largest size within **25%** of 2σ_od = 0.094701, and the local slope between
the two largest sizes **closer to 0.5 than** the local slope between the two
smallest. A failure here with P1 passing is read as "q=10 is not yet
asymptotic", not as a failure of the claim — and that reading is registered
now, not chosen afterwards.

**P5 — the control (2-D Ising, continuous transition).** The defect does not
grow with the surface: **either D < 0.25 at every size, or b < 0.15**. A
continuous transition has no coexistence and so no interface; if the Ising
defect grows like L, the "surface" in P1 is not an interface at all and the
stone fails regardless of P1.

## 2. Declared identities and code checks (no evidential weight)

**I1.** max_E [N(ŝ − s)] equals ln(P_max/P_min) of the canonical energy
histogram at the inverse temperature equal to the bitangent's slope — the
quantity Binder and Lee–Kosterlitz measure. This is an identity (a Legendre
shift of a straight line), so P3 is a comparison with *their* number, not an
independent measurement of mine. Checked to round-off as a code check.

**I2.** The bitangent's slope at the largest 2-D size lies within 2% of the
exact β_t = ln(1+√q) (1.6997 for q=20, 1.4261 for q=10). Finite-size shifts are
O(1/N)-ish; this is a check that the WL density of states is the right one, not
evidence for the claim.

## 3. What each outcome would mean

- **P1 ∧ P2 ∧ P5 pass:** order 0 is a three-valued classifier — 0 (no
  coexistence, or no interaction), (d−1)/d (short-range coexistence), 1
  (long-range coexistence) — and D10's "long range opens the possibility, a
  first-order transition realizes it" is refined to: *a first-order
  transition always violates order 0; range sets the exponent.* The defect per
  site still vanishes for short range (ensemble equivalence holds in the limit),
  so this is a **sub-extensive** order-0 failure, and that qualifier is part of
  the claim.
- **b ≈ 1 in 2-D:** the order-0 clause cannot tell short from long range and
  D10's B3 conclusion that range matters is wrong.
- **b ≈ 0 in 2-D:** short-range first-order transitions do not violate order 0;
  D10's B3b alternative ("first-order realizes non-additivity") must be
  restricted to long range.
- **P2 fails with P1 passing:** the exponent is ½ for some other reason, and
  "surface" is unproven.

## 4. Known weaknesses, registered now

- **The answer is in the literature** (prior-art note). The risk is in whether
  *this* repository's definition and code reproduce it, not in the physics.
- **Finite sizes are modest**, especially 3-D (L ≤ 14) and q=10 (L ≤ 6ξ_d).
  Corrections to D = 2σL are known to include ln L and constant terms; a
  two-parameter fit would absorb them but is **not** the registered statistic.
- **Wang–Landau has a systematic error** that seed scatter does not fully
  capture. The validation (§0, item 2) bounds it at ≈ 0.005 per level on tiny
  lattices; on large windows it is larger and unquantified beyond the seed
  spread.
- **Periodic boundaries** select the slab (two-interface) geometry at the
  defect's maximum. Free boundaries would change the prefactor, not the
  exponent; not tested.

---

## Amendment A — 2026-11-19, before any production defect was computed

The first production launch ran 30 minutes without completing a job and was
killed; no output from it was kept or analyzed. Two changes to the Wang–Landau
*machinery* followed. The definition, the systems, sizes, windows, seeds,
ln f_final, the statistics and every registered band are unchanged.

1. **Schedule.** "Flatness 0.8" (§0) is replaced by Belardinelli–Pereyra's own
   initial-phase rule: halve ln f each time every reachable bin in the window
   has been visited since the last halving, then switch to 1/t. The flatness
   rule stalled on a 5,816-bin window that spans a first-order intruder.
2. **Reachable levels.** A first attempt at (1) counted only bins visited *so
   far*, and a timing probe (q=20, L=32) showed the walker converging on 447 of
   1,731 bins without crossing to the disordered side. The rule now requires
   every *reachable* level, enumerated exactly in `wl.c` (2-D q ≥ 3: m = 1, 2,
   3, 5 unsatisfied bonds are impossible; q = 2: m even and m ≠ 2; 3-D windows
   are kept below 3N − 14, which never binds for the registered window). A run
   that cannot finish now aborts instead of hanging.

Re-validated against exact enumeration at the production ln f_final = 1e-6,
with 2-D windows running to the ground state: levels match exactly on all four
lattices, max |Δ ln Ω| ≤ 0.0098 (`validate.py`, `validation.json`). The timing
probe was a code check at a registered size; its defect was not computed.
