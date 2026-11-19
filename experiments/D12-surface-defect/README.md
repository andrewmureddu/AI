# D12 — the order-0 defect in short-range models: surface, not volume

*2026-11-19. Works [D12](../../questions/UNKNOWN-LAWS.md#d12--does-the-order-0-defect-scale-as-the-surface-in-short-range-models),
the P0 that [D10](../D10-composition-lens/) left open
([`SYNTHESIS.md`](../../SYNTHESIS.md) §7.0'(a)). Pre-registration:
[`PREREGISTRATION.md`](./PREREGISTRATION.md), committed before any production run,
with one machinery amendment (Amendment A), also committed before any defect was
computed. Numbers: [`verdict.json`](./verdict.json).*

**Result: 3 of 5 registered predictions pass, and the one with the most teeth is
the cleanest.** For a short-range model with a first-order transition, D10's
order-0 defect scales as the **surface**. In 2-D q=20 Potts, D ~ N^**0.509 ± 0.011**
(registered 0.50 ± 0.08; 0 and 1 both excluded by > 40 error bars), and its
prefactor is the interface free energy: D/L = **0.376** at L = 48 against the exact
2σ_od = **0.370988** (Borgs–Janke), a 1.3% difference. The continuous-transition
control (2-D Ising) has no growing defect. So order 0 is a classifier with at
least three values: **0** (no coexistence), **(d−1)/d** (short-range coexistence),
**1** (long-range coexistence, D10).

**Two registered predictions failed, for two different reasons, both on record.**
3-D q=10 measured b = **0.778** against a registered band of [0.567, 0.767]. The
local slopes fall at every step, and a post-hoc extension to L = 20 continues the
trend to **0.695**, but the registered statistic failed. 2-D q=10 measured
b = **0.20** because of something I did not anticipate: **D10's definition (a max
over the whole energy axis) picks up lattice discreteness at the bottom of the
band**, and at L = 16 that beats the coexistence gap. That is a finding about the
definition, not about the physics, and it is the most useful thing this run turned
up for the map.

Run: `python3 validate.py` (code check, ~2 min), `python3 run.py` (the registered
run, ~1 h on 4 cores), `python3 run.py --extend` (the post-hoc 3-D sizes, ~1 h).
The code is C (`wl.c`, `enum.c`, compiled by the scripts with `gcc`) plus numpy.

---

## 1. Method

**Definition (D10's, unchanged).** s(e) = ln Ω(E)/N on a periodic L^d lattice,
E = −(number of satisfied bonds). ŝ is the exact upper concave envelope (D10's
monotone-chain hull, copied verbatim). The defect is **D = N · max_e [ŝ(e) − s(e)]**.

**Density of states.** Wang–Landau with the Belardinelli–Pereyra 1/t schedule,
confined to an energy window that contains the coexistence region; ln f_final =
1e-6; 4 seeds in 2-D, 3 in 3-D; the seeds' ln Ω curves are averaged.
**Validated against exact enumeration** on four lattices (2-D q = 2, 3, 4 at
L = 4, with windows running to the ground state; 3-D q = 2 at L = 3). The level sets
match exactly and max |Δ ln Ω| ≤ **0.0098** (`validation.json`).

**Amendment A** (before results): the registered flatness-0.8 schedule stalled on
the largest window, and a first replacement converged on a sub-window (447 of
1,731 bins) without crossing the barrier. Both were caught before any defect was
computed. The fix requires every *reachable* level, which `wl.c` enumerates
exactly. Machinery only; nothing registered changed.

---

## 2. The registered verdict

| | system | registered | measured | |
|---|---|---|---|:--:|
| **P1** | 2-D Potts q=20 | b = 0.50 ± 0.08, excluding 0 and 1 by > 3σ | **b = 0.509 ± 0.011** | ✓ |
| **P2** | 3-D Potts q=10 | b = 0.667 ± 0.10, excluding ½ and 1 by > 3σ | **b = 0.778 ± 0.0005** | ✗ |
| **P3** | 2-D q=20, L = 48 | D/L within 10% of 2σ_od = 0.370988 | **0.376 (+1.3%)** | ✓ |
| **P4** | 2-D Potts q=10 | b ∈ [0.35, 0.85]; D/L within 25% of 0.094701; slope → ½ | b = **0.20** ✗ · D/L = 0.1007 (+6.4%) ✓ · local slope −0.55 → 0.51 ✓ | ✗ |
| **P5** | 2-D Ising (continuous) | D < 0.25 at every L, **or** b < 0.15 | D = 1.10 → 0.27, **b = −0.48** | ✓ |
| I1 | identity | max N(ŝ − s) = ln(P_max/P_min) | ≤ 5e-13 wherever the max is the coexistence gap; fails exactly where it is not (§4) | code check |
| I2 | check | bitangent slope within 2% of β_t = ln(1+√q) | −0.05% (q=20), −0.06% (q=10) | ✓ |

### P1 and P3: the surface, and it is the interface

| L | 12 | 16 | 24 | 32 | 48 |
|---|--:|--:|--:|--:|--:|
| D (q=20) | 4.54 | 5.79 | 8.61 | 12.55 | 18.05 |
| ± (seed sd/√4) | 0.03 | 0.08 | 0.05 | 0.28 | 0.53 |
| **D / L** | 0.378 | 0.362 | 0.359 | 0.392 | **0.376** |

D/L is flat to within the seed scatter from L = 12 (≈ 4.5 ξ_d) on. The number it is
flat at is not a fit parameter: it is the exact order–disorder interface tension
times two, for the two interfaces a periodic slab carries. The unregistered
three-parameter fit D = aL + c ln L + e gives a = 0.383. The bitangent's slope is
the transition temperature to 0.05% (I2). That is what makes this an *interface*
measurement rather than "some exponent near ½": the defect D10 defined in a
composition-law vocabulary is, number for number, the surface free energy that
Binder and Lee–Kosterlitz measure in a canonical one.

### P5: the control is clean, but not in the way I registered it

D does not grow (b = −0.48), so P5 passes on its second branch. Its first branch,
D < 0.25, fails at every size: D = 1.10, 1.48, 0.90, 0.78, 0.27. **Every one of
those maxima sits at the low-energy edge of the window** (e = −1.91 … −1.97, a few
dozen broken bonds above the ground state). More than 0.1 away from that edge the
Ising defect is **0.0022, 0.0024, 0.0126** at L = 16, 24, 32 (post hoc): the WL
noise floor. A continuous transition has no intruder, and there is none.

---

## 3. The two failures

### P2: three dimensions, still in the crossover

| L | 8 | 10 | 12 | 14 | *16* | *18* | *20* |
|---|--:|--:|--:|--:|--:|--:|--:|
| D | 13.42 | 22.96 | 35.17 | 49.46 | *66.09* | *84.73* | *105.53* |
| D / L² | 0.210 | 0.230 | 0.244 | 0.252 | *0.258* | *0.262* | *0.264* |
| local slope (to next) | 0.802 | 0.779 | 0.737 | 0.724 | *0.703* | *0.695* | |

*Italic: post hoc (`--extend`), added after the verdict because P2 failed. Same
window, settings, and seeds 1–3.*

The registered fit over L = 8–14 gives **0.778**, 0.011 above the band's upper
edge. P2 fails. What the failure looks like matters for reading it:

- The local slope **falls monotonically at every step**, 0.80 → 0.695, and D/L²
  rises toward a plateau (0.210 → 0.264, with increments shrinking 0.020 → 0.002).
  That is a surface term approached from below, with a negative subleading
  correction. The unregistered fit D = aL² + c ln L + e has c = −2.8. The same
  shape would make the apparent exponent overshoot at small L.
- A fit over the last three post-hoc sizes gives **0.699**. That is inside the
  registered band, but a post-hoc number cannot rescue a registered prediction,
  so it is not used.
- **What does survive, from the registered data alone:** b = 0.778 excludes both ½
  and 1 by hundreds of (statistical) error bars. **The 3-D exponent is not the 2-D
  one and not the long-range one.** "The dimension enters" is established;
  "(d−1)/d exactly" in 3-D is not.

The registered error bar (±0.0005) is a seed scatter and is far smaller than the
finite-size systematic. That was flagged as a weakness in the pre-registration
(§4) and is why I report the slope sequence and not the error bar.

### P4: the definition picks up the bottom of the band

q=10's registered fit gives **b = 0.20**, outside [0.35, 0.85]. The whole failure
is one point. At L = 16, D = **4.18**, and it sits at e = −1.965, about 9 broken
bonds above the ground state. The coexistence gap at the same size is 1.75. The
lump is real and exact: it is the same in all four seeds (4.10, 4.26, 4.23, 4.14),
and it is the combinatorics of the lowest excitations (one flipped spin costs 4
bonds, a flipped pair 6 or 7, a bent triple 8 or 9, …). Those level counts are not
concave at small N. The registered window reached m ≥ 8 broken bonds at L = 16 and
m ≥ 18 at L = 24, so the lump is in the window at one size only, and the fit
inherits a fake drop of D between L = 16 and 24.

The intruder alone (the gap under the bitangent, post hoc) behaves exactly as
q=10 should in a crossover:

| L | 16 | 24 | 32 | 48 | 64 |
|---|--:|--:|--:|--:|--:|
| D, intruder only | 1.75 | 2.68 | 3.43 | 4.80 | 6.45 |
| D / L | 0.109 | 0.112 | 0.107 | 0.0999 | **0.1007** |

The exponent is 0.46, and D/L ends 6.4% above the exact 0.094701 with L/ξ_d ≈ 6.
The pre-registration's own reading was "q=10 is not yet asymptotic", but that
reading was attached to a *crossover* failure, and this failure is not one. It is
a failure of the statistic, and I report it as that.

**Why it matters beyond this run.** D10 defines the order-0 defect as a max over
the whole energy axis. On any lattice model whose window reaches the bottom of the
band, the definition picks up discreteness lumps that are no part of the
thermodynamics. For Ising the lowest one (m = 6 against m = 4 and 8) has depth
≈ ½ ln N − 1, which **grows logarithmically**. D10's own models (mean-field
multinomials, a log-binomial chain) have no lumps, so D10's numbers stand. But the
definition needs one clause it never had:

> **The order-0 defect is the max of N(ŝ − s) over a fixed interior fraction of the
> energy band, or equivalently the depth of the intruder under the hull's
> bitangent. It is not the max over every level.** Excitation combinatorics at the
> band edge are O(ln N) and vanish per site; they would make every lattice model
> look "non-additive at order 0" with exponent 0⁺.

---

## 4. Code checks

- **I1** (declared identity): where the maximum is the coexistence gap, D equals
  ln(P_max/P_min) of the canonical histogram at the bitangent's temperature to
  ≤ 5.2e-13. That holds at every q=20 and 3-D size and at q=10 for L ≥ 24. I1 fails
  at q=10 L = 16 (by 2.43) and at Ising L = 24, 32. Those are exactly the cases
  where the maximum is a band-edge lump, which is how the P4 diagnosis was found.
  The identity is fine; it was never about the lumps.
- **Window rule**: every Potts run has both bitangent vertices inside the window
  with the registered margin.
- **Cost**: about an hour on 4 cores for each of the registered run and the
  extension. The largest single jobs were 2-D q=10 L = 64 (7–8 min) and 3-D L = 20
  (20–32 min).

---

## 5. What this does and does not establish

- **Established (d = 2):** a short-range first-order transition violates order 0 at
  N^{1/2}, with the interface tension as prefactor (1.3%), and a continuous
  transition does not. D10's B3b sentence ("long range opens the possibility, a
  first-order transition realizes it") is wrong in its first half and should read:
  **a first-order transition always violates order 0; the range sets the exponent**
  (1 long-range, (d−1)/d short-range). The violation is **sub-extensive** for short
  range (D/N → 0, so ensembles are equivalent in the limit), and that qualifier is
  part of the claim.
- **Not established:** the exact 3-D value. The registered fit failed; the
  post-hoc trend points at 2/3 and is not a test.
- **Corrected:** D10's definition needs the interior/intruder clause above.
- **Novelty N0**, as declared before the work. Every number here is in Binder
  (1982), Lee–Kosterlitz (1990) and Borgs–Janke (1992) in canonical language. What
  the run adds to the map is placement: the ensemble-inequivalence result D10
  measured and the interface-tension literature are the same floor-0 quantity at
  two ranges.
- **Boundaries:** periodic boundaries only (they select the slab geometry and the
  factor 2 in 2σ); Potts and Ising only; equilibrium only; one 3-D system; WL
  systematic error is estimated only by seed scatter on the big windows.
