# D2 pre-registration — written before any measurement

Tests [`derivations/D2-gauge-of-the-tower.md`](../../derivations/D2-gauge-of-the-tower.md).
Per [`questions/UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art
note first, then the identity/risk split, then the numbers.

**Most of this experiment is a theorem check.** That is stated up front because
the derivation's core — conjugation invariance of eigenvalues, power covariance of
exponents — is mathematics, and running it proves nothing about the world. It is
worth running anyway for one reason: it is a check on *the code and the claimed
setups*, and D1 established that this register's failures are estimator failures
as often as they are claim failures. The genuinely at-risk content is §5's T4 and
T5, and they are the reason this is an experiment rather than a footnote.

---

## 0. Prior-art note (written first)

**Old.** Conjugation invariance of eigenvalues is linear algebra. That RG
eigenvalues are invariants of the linearized flow, and that critical exponents are
quoted against a canonically chosen scaling field, is textbook RG (Wilson, Kadanoff;
Wegner's treatment of nonlinear scaling fields is exactly the statement that a
smooth change of scaling fields leaves the exponents alone). That Hausdorff
dimension is a bi-Lipschitz invariant but not a homeomorphism invariant is
textbook fractal geometry. Scaling relations among exponents are old. **None of
this is claimed as new**, and the derivation says so in §3 and §7.

**Not covered.** The identification of `FLOORS.md`'s log-ratio signature with the
transformation data of G_pow modulo G_diff; the consequent claim that the
scheme layer is the tower's **structure group** rather than a layer of facts; the
identification of its chart-free residue with the codimension p − 2; and the
resulting explanation of why floor 2 collapses while floor 3 stratifies. Those are
claims about **this repo's architecture**, and the N2 claim is confined to them.

**Nearest miss, recorded so it cannot be relabelled later.** Wegner's nonlinear
scaling fields are the G_diff half of §3 stated in the RG literature's own
language. If the G_pow half also turns out to be standard somewhere — most likely
in the singularity-theory or the dynamical-systems-conjugacy literature, where
topological vs smooth conjugacy is exactly this distinction — then D2's group
analysis is **N0–N1** and only the architectural reading survives at N2. I expect
this to be at least partly true: topological conjugacy famously does not preserve
eigenvalues, and that is §4 in other words.

---

## 1. Legs

**Part A — RG maps** (does an eigenvalue behave as the derivation says?)

| Leg | Field | Map | Known value |
|---|---|---|---|
| **R1** | statistical mechanics | 1D Ising decimation, x = tanh K, x′ = x², at x = 1 | y = 1 exactly |
| **R2** | statistical mechanics | diamond hierarchical lattice, K′ = 2·artanh(tanh²K) | y ≈ 0.747, ν ≈ 1.338 |
| **R3** | nonlinear dynamics | logistic-map period doubling | δ = 4.66920 |

**Part B — D1's legs re-used** (is the residue the codimension?)

The fold (p = 3), SIS (p = 3), mean-field Ising (p = 4) and Blume–Capel on its
tricritical line (p = 6), with β measured from the order parameter and k from the
chart map, both by numerical fit on the **full** models.

---

## 2. Identity vs. risk — the required disclosure

**Theorem checks. These cannot come out wrong; they test the code, not the claim:**

- **T1** conjugation invariance under G_diff. Linear algebra.
- **T2** power covariance y → a·y under G_pow. One line of algebra (§3).
- **T3** sign and count invariance under a > 0. Immediate.
- The three RG legs' *known values* (y = 1, ν ≈ 1.338, δ ≈ 4.669) are literature
  numbers; recovering them checks the implementation.

**Genuinely at risk:**

- **T4 — β/k = 1/(p−2) on full models.** The derivation gets this from a truncated
  Landau form; the legs carry every higher order. This is the one place the
  derivation makes a numerical prediction about a system it did not construct.

  > **Pre-run correction (caught while writing the code, before any measurement;
  > left on record rather than silently edited, as D1's P5 was).** "The legs carry
  > every higher order" is true of only two of the four. The fold and SIS have
  > *exactly* cubic potentials, so their β and k are closed-form and β/k = 1 is an
  > identity there, exactly as those two legs were identities in D1. **The at-risk
  > half of P4 is mean-field Ising and Blume–Capel only** — and both are physics,
  > which is the same gap D1 recorded and did not close.
- **T5 — the observable–observable invariance.** The operational meaning of
  "gauge" is that no measurable prediction changes. T5 tests it directly rather
  than asserting it, and it can fail: if a relation between two *observables*
  (no control parameter appearing) moves under ε′ = ε^a, the gauge claim is
  simply false and §5 of the derivation collapses.
- **T6 — the falsifier hunt.** An explicit search for a chart-free prediction that
  depends on an exponent's *magnitude*. §4 says there is none under common-a.

---

## 3. Registered predictions

**P1 (T1, theorem check).** For R1–R3, applying smooth conjugations
h(u) = c₁u + c₂u² + c₃u³ with c₁ ∈ {0.4, 1, 2.5} and c₂, c₃ random, leaves the
eigenvalue unchanged to **≤ 1e-6 relative** (finite-difference limited).

**P2 (T2, theorem check).** Under u → u^a for a ∈ {1/3, 1/2, 2, 3}, the measured
RG exponent equals **a·y** to **≤ 1e-6 relative**, for all three legs.
Registered with the direction: **y multiplies by a**, because y is an inverse
exponent (ν = 1/y divides by a). Getting this backwards is the error D1's P5 made
and it is written out here to avoid repeating it.

**P3 (T3, theorem check).** On a 2×2 RG map with one relevant and one irrelevant
direction, both G_diff and G_pow leave (i) the sign of each y_i and (ii) the count
of relevant directions unchanged, for every a and every conjugation tested.
Additionally: the **ratio** y₁/y₂ is unchanged under common-a and **does** change
under independent-a — the caveat in derivation §4, made explicit rather than
argued.

**P4 (T4, AT RISK).** Measured β/k on the full models, each within **±0.03
absolute** of 1/(p−2):

| Leg | p | predicted β/k |
|---|:--:|:--:|
| fold | 3 | **1.000** |
| SIS | 3 | **1.000** |
| mean-field Ising | 4 | **0.500** |
| Blume–Capel (tricritical) | 6 | **0.250** |

Registered alongside: the bare exponents β and k separately must **not** be
constant across the legs — otherwise the ratio's invariance is vacuous. Predict
β ∈ {0.5, 1, 0.5, 0.25} and k ∈ {0.5, 1, 1, 1}, so β spans 4× and k spans 2×
while β/k lands on 1/(p−2).

**P5 (T5, AT RISK).** Construct an observable–observable relation containing no
control parameter — the order parameter as a function of the softest eigenvalue,
m ~ λ^{1/(p−2)}. Under ε′ = ε^a for a ∈ {1/2, 2, 3}: β and k each change by the
factor 1/a, and the **fitted exponent of m vs λ is unchanged to ≤ 0.01 absolute**.
This is the gauge claim in its operational form.

**P6 (T6, AT RISK — the falsifier hunt).** Search for a quantity that is (a) a
function of an exponent's magnitude and (b) invariant under common-a
reparameterization. Registered expectation: **none exists**, i.e. every invariant
found is expressible in signs, counts, and ratios. Reported honestly if one is
found, since that restores the fourth floor and kills the derivation.

---

## 4. What would kill D2

- **P5 fails** — an observable–observable relation moves under reparameterization.
  Then exponent magnitudes are *not* gauge, the scheme layer is not a structure
  group, and the fourth floor is back.
- **P4 fails** — the residue is not the codimension. The group analysis survives
  (it never mentions *p*) but the identification of what the scheme layer leaves
  behind is wrong, and the P0 is only half answered.
- **P2 fails** — the derivation's central algebra is wrong.
- **P6 finds something** — a chart-free magnitude. Strongest possible refutation.

## 5. Scope, registered

Everything inherits D1's scope: one-dimensional gradient systems, additive noise,
degeneracy-type singularities, one control parameter. The RG legs are
one-dimensional coupling spaces except for the constructed 2×2 map in P3, which is
a demonstration of the group action rather than a physical model and is labelled as
such. **Support-type singularities are excluded**: they have no *p*, so P4 does not
apply to them, and what the residue is there stays open ([D6](../../questions/UNKNOWN-LAWS.md)).
