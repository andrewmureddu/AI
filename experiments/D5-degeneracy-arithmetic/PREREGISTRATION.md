# D5 pre-registration — written before any code

Works [D5](../../questions/UNKNOWN-LAWS.md): *if floor 3 is classified by the
degeneracy order, does that order have arithmetic — is it conserved, additive, or
bounded along a sequence of transitions?*

---

## 0. Prior-art note (written first), and the stone's own warning

D5 was filed with the harshest prior-art warning in the register: *"this is the
stone most likely to be N0 — the potential case is Thom and Arnold, and anyone
claiming novelty here must first show their object is not a potential."*

**That warning is correct, and for one of the two readings the answer is already
known.** D5's literal question — a system passing through *two transitions in
succession* — is coalescence of critical points, and singularity theory answers
it: **codimension is additive**. Two folds (A₂, codim 1) colliding give a cusp
(A₃, codim 2). In the repo's notation codim = p − 2, so

```
        p_composite  =  p_1 + p_2 - 2                (3 + 3 -> 4, a cusp)
```

Degeneracy orders do **not** add and do **not** max; their codimensions add. This
is textbook and is graded **N0**. It is verified numerically in §4 as an estimator
check, not offered as a finding.

## 1. Restating the stone, because D6 moved the ground

D5 was filed when floor 3's classifier was believed to be a single integer *p*.
[D6](../D6-support-singularities/) has since shown *p* was the q₁ = 2 slice of a
**pair**: writing Φ's two leading terms as A|y|^{q₁} + B|y|^{q₂}, the crossover
locus is A_c ~ D^{1 − q₁/q₂} and the classifier is the ratio.

So the live version of "does the order have arithmetic" is: **what happens when Φ
carries more than two terms?** Per the register's working rule ("restate it as a
quantitative claim"), that is what is tested here.

With Φ = A|y|^{q₁} + Σ_j B_j |y|^{q_j}, each higher term j supplies its own
rounding scale, and whichever breaks the q₁ behaviour first governs. Since
1 − q₁/q_j increases with q_j, the *lowest* higher term governs at small D and
successively higher ones take over as D grows. So the prediction is a **staircase**:

```
        local exponent of A_c(D)   =   1 - q1/q_j     on the j-th plateau
```

**The arithmetic is enumeration, not addition.** Each term in Φ contributes one
plateau; the plateaus do not combine, they queue. Equivalently
**(1 − θ_j) = q₁/q_j**, so consecutive plateaus satisfy

```
        (1 - theta_j) / (1 - theta_{j+1})  =  q_{j+1} / q_j
```

recovering the ratios of the higher exponents from the staircase alone.

## 2. Identity vs. risk

**Identities — declared, and not evidence:**

- Each individual plateau value 1 − q₁/q_j is D6's formula applied to one pair.
- The ratio rule in §1 is those values divided. Both are algebra.
- The codimension additivity in §0 is Thom/Arnold.

**Genuinely at risk — and this is the experiment:**

- **P3, whether the intermediate plateaus exist at all.**
  [P8](../D1-chart-invariance/P8-REREGISTRATION.md) has just shown they need not:
  in Blume–Capel the sextic plateau **never established** — the local slope rose
  from 0.500, peaked at 0.5723, and turned back down without reaching 2/3, because
  higher terms took over before the sextic regime had room. So a staircase is
  *algebraically* forced and *observationally* contingent, and the registered
  question is when it survives.
- **P4, the squeeze condition** — a quantitative threshold on coefficient
  separation, predicted below and testable.

## 3. Registered predictions

**P1 — two-plateau staircases (three-term Φ).** With coefficients separated so each
regime has room, the local exponent of A_c(D) shows plateaus within **±0.04**:

| (q₁; q₂, q₃) | plateau 1 | plateau 2 |
|---|:--:|:--:|
| (2; 4, 6) | **0.5000** | **0.6667** |
| (2; 4, 8) | **0.5000** | **0.7500** |
| (2; 3, 6) | **0.3333** | **0.6667** |
| (1; 2, 4) | **0.5000** | **0.7500** |

**P2 — a three-plateau staircase (four-term Φ).** For (2; 4, 6, 8): plateaus at
**0.5000, 0.6667, 0.7500**, each within ±0.05 (looser — three plateaus in one
sweep leaves each less room).

**P3 — the ratio rule.** For every staircase above,
(1 − θ_j)/(1 − θ_{j+1}) reproduces q_{j+1}/q_j within **±0.08**.

**P4 — the squeeze condition (AT RISK, the real content).** A plateau needs its
regime to span enough decades in D to be visible. The j-th regime runs from where
term j overtakes term j−1 to where term j+1 overtakes term j. Registered
prediction: **the middle plateau of a (2; 4, 6) system is resolvable when the
coefficients are separated by more than ~3 decades in D, and is squeezed out
below ~1 decade** — measured by sweeping B₃/B₂ over several orders and recording
where the middle plateau's width falls below half a decade. Registered with the
direction: **increasing B₃ at fixed B₂ narrows the middle plateau.**

**P5 — codimension additivity (identity; estimator check).** Two folds brought
into coincidence give a cusp: the merged germ's leading anharmonic order is
**4**, i.e. p₁ + p₂ − 2 = 3 + 3 − 2, and the codimension is 2 = 1 + 1. Verified by
numerically expanding a two-fold family at coincidence.

## 4. What would kill the restated stone

- **No staircase at all** when the scales *are* separated — then higher terms do
  not queue and the enumeration picture is wrong.
- **Plateau values off** 1 − q₁/q_j by more than the tolerance — D6's formula does
  not extend past two terms.
- **P4's direction wrong** — if increasing B₃ *widens* the middle plateau, the
  squeeze mechanism is misunderstood.

## 5. Scope

One-dimensional gradient systems, additive noise, one control parameter —
inherited from D1/D6 and not exceeded. **Synthetic multi-term potentials by
construction**, because the point is to control the number and separation of
terms; the real-model counterpart is P8's Blume–Capel result, cited rather than
re-run. Support-type (q₁ = 1) appears in one leg only. Nothing here addresses
essential singularities, which remain floor 3's unclassified remainder.

**Novelty, stated in advance:** §0 is **N0**. The staircase's individual steps are
D6 applied repeatedly, so **N0–N1**. The only content that could reach N2 is P4 —
*when* an algebraically-forced regime fails to be observable — and even that is
close to standard crossover-scaling practice. This stone was always the register's
weakest; the honest outcome is most likely a confirmation of arithmetic that was
never in doubt, plus a boundary on when it can be seen.
