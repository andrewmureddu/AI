# D7 pre-registration — written before any measurement

Works [D7](../../questions/UNKNOWN-LAWS.md#d7--is-there-a-floor-0-and-is-it-a-composition-law):
is there a layer under floor 1, and is it a composition law?

The prior-art note is in the register entry and was written first, per
[`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6. It concludes **N1 by
default** — Koopman–Pitman–Darmois already *is* claim C2 — with one N2 candidate,
C4. This document does the second half of §6: state the claims quantitatively and
mark, **before the run**, which are analytic identities and which can come out
wrong.

The register has now been burned three times by predictions that were identities
dressed as risk ([D6](../D6-support-singularities/)'s P2 was the third). So this
pre-registration is deliberately lopsided: **two of the five legs are declared
identities up front and carry zero evidential weight.** The stone lives or dies on
legs B, C and D.

---

## 0. The one definition everything uses

For an observable whose cumulants are κ_k, define the **order-k additivity defect**
of a system of size N:

```
        Delta_k(N)  =  kappa_k(2N)  -  2 * kappa_k(N)
        delta_k(N)  =  Delta_k(N) / kappa_k(2N)          (the ratio actually reported)
```

δ_k → 0 is "extensivity holds at order k." This is the model-independent form; it
never requires a spatial cut, which matters because long-range models do not have
one.

Φ = ln Z is the cumulant generating function, so **"Φ is additive under
composition" is exactly "δ_k → 0 for every k"** — one condition per order. C4 says
the tower's floors are the orders at which it fails.

---

## 1. Leg A — the order-resolved defect spectrum · **DECLARED IDENTITY**

Exact 1D Ising chain, open boundary, h = 0, u = tanh(βJ), ξ = −1/ln u.

```
        Var(M_N)  =  N + 2 * sum_{d=1}^{N-1} (N - d) u^d          (exact)
```

Report δ₀ (free energy) and δ₂ (magnetization variance) against N/ξ.

**Everything in this leg is closed form**: δ₀ = O(1/N) at every temperature because
splitting a chain removes one bond, and δ₂ → ½ as ξ/N → ∞ because Var → N², →0 as
ξ/N → 0 because Var → N(1+u)/(1−u). **No evidential weight.** It is here to show
that the orders separate — order 0 extensive while order 2 is not, at the same
point — because that separation is what C4 needs to be meaningful, and a reader
should be able to see it in closed form before being asked to believe anything.

---

## 2. Leg B — long-range breaks order 0, short-range does not · **AT-RISK**

Two microcanonical entropies, both computed by exact counting, no sampling.

- **Long-range:** mean-field 3-state Potts, H = −(1/2N)·Σ_a n_a², all-to-all.
- **Short-range control:** 1-D 3-state Potts chain, nearest-neighbour, exact
  transfer-matrix DP over the energy lattice.

Composite of two half-systems at total energy E:
Ω^comp(E) = Σ_{E'} Ω(E')·Ω(E−E'), and the total defect is
D(E) = ln Ω^comp(E) − ln Ω(E).

**B1 — at-risk, but the answer is in the literature; graded as a check.**
s(e) for the mean-field 3-state Potts is **non-concave on a nonempty interval**
(Ispolatov & Cohen 2001). If my counting disagrees with that, the leg is broken,
not the claim.

**B2 — DECLARED IDENTITY.** The two-copy maximum entropy at fixed total energy is
the concave hull of s, and the concave hull is s** = the double Legendre
transform. Used only to validate the code: predicted agreement to grid resolution.

**B3 — at-risk, the leg's real content.** The defect's **scaling exponent**:

```
        long-range  :  max_E D(E)  ~  N^1     registered 1.00 +/- 0.10
        short-range :  max_E D(E)  ~  N^0     registered bounded by 2*ln 3 = 2.20
                                              for every N up to 512 and every E
```

Can come out wrong in both directions: the short-range chain could show growth
(logarithmic or otherwise), and the long-range defect could be sub-extensive.

**B4 — at-risk.** The microcanonical specific heat
c(e) = −(ds/de)² / (d²s/de²) is **negative on a nonempty subinterval** of the
long-range model and **nowhere negative** for the short-range control.
(That the *canonical* heat capacity β²Φ'' ≥ 0 everywhere is a variance and is an
identity — reported, not counted.)

---

## 3. Leg C — what closes the ensemble family under composition · **AT-RISK**

N iid sites, q_i ∈ {0,1,2}, uniform base measure, Q = Σ q_i. For a statistic T,
the family on a size-n system is p_n(x; μ) ∝ e^{−μ T(Q_n(x))}.

Take two independent size-n systems, each at μ. Their product is a distribution on
the composite. Ask how far it is from the *composite's own family*:

```
        KL_min(T, n)  =  min over mu'  of  KL( p_n(mu) (x) p_n(mu)  ||  p_2n(mu') )
```

evaluated exactly on the (Q_A, Q_B) lattice.

**Tilt normalization, fixed in advance to remove the free knob:** for each T and n,
μ is chosen by solving KL(p_n(·; μ) ‖ p_n(·; 0)) = 1 nat. Every statistic is
therefore tilted by the same amount, and μ is not available for tuning.

Six statistics, chosen so that **four nearby rules make different predictions**:

| T(Q) | additive | linear | monotone | convex |
|---|:--:|:--:|:--:|:--:|
| Q | ✓ | ✓ | ✓ | ✓ |
| 3Q − 7 | ✓ | ✗ | ✓ | ✓ |
| Q² | ✗ | ✗ | ✓ | ✓ |
| √Q | ✗ | ✗ | ✓ | ✗ |
| ln(1+Q) | ✗ | ✗ | ✓ | ✗ |
| Q mod 2 | ✗ | ✗ | ✗ | ✗ |

**C1 — at-risk.** KL_min = 0 (≤ 1e-12) for **exactly** the additive rows — Q and
3Q − 7 — and > 1e-6 for **every** other row. If the discriminator were linearity,
3Q − 7 fails; if monotonicity, Q² and √Q pass; if convexity, √Q and Q² split. Only
one of the four rules survives all six rows, and the run decides which.

**C2 — at-risk.** For the non-additive rows KL_min grows **linearly in n**,
registered exponent 1.00 ± 0.15 over n = 8…128. Could saturate; could be n².

**Not claimed:** that additivity is *sufficient* for anything beyond closure, or
that this is new — it is Koopman–Pitman–Darmois, and the register says so.

---

## 4. Leg D — order 2, and the three values · **AT-RISK, the sharpest leg**

Curie–Weiss (mean-field Ising), exact enumeration over total magnetization M.
Report δ₂(N) = 1 − 2·Var(M_N)/Var(M_{2N}) at three temperatures.

At T_c the magnetization density has the quartic law p(m) ∝ e^{−N m⁴/12}, so
Var(M) ~ N^{3/2} rather than N — and the defect ratio inherits the anomaly:

```
        T > T_c   Var ~ N        ->   delta_2  ->  0
        T = T_c   Var ~ N^{3/2}  ->   delta_2  ->  1 - 2^{-1/2}  =  0.29289
        T < T_c   Var ~ N^2      ->   delta_2  ->  1/2
```

**D1 — at-risk.** Those three values, registered to 2 decimals, tolerance ±0.03 at
N = 4096. The middle one is the load-bearing number: it is not 0 and not ½, it
comes from a critical exponent, and nothing forces it if C4 is wrong about
criticality being an order-2 extensivity failure.

**D2 — at-risk.** The T < T_c value of ½ is the *symmetry-broken* case (the
unrestricted symmetric ensemble is a two-component mixture). Registered as a
distinct mechanism reaching the same order — if it instead reads 0.29 or 0, the
reading "SSB is also an order-2 failure" is wrong.

**D3 — at-risk.** Heavy tails, the "no order exists" case: for iid α-stable
summands with α = 1.5 the empirical δ₂ **does not converge** — registered as
across-seed spread that fails to shrink by more than 2× as N goes 10³ → 10⁵,
against a Gaussian control whose spread shrinks like N^{−1/2}.

---

## 5. Leg E — chart pinning · **IDENTITY (table) + AT-RISK (audit)**

**E1 — DECLARED IDENTITY.** The additivity defect of x → x^a for equal parts,
|(x_A + x_B)^a − (x_A^a + x_B^a)| / (x_A + x_B)^a = |1 − 2^{1−a}|. Reproduces
[P-D leg F](../PD-allometry-reduction/)'s 29% / 50% / 41% at a = 1.5 / 2 / 0.5.
Arithmetic. Zero weight.

**E2 — at-risk audit.** C3 predicts a clean sort over the repo's own ledger:
**every exponent recorded as gauge is measured in a variable with no additive
composition law, and every exponent recorded as a fact is measured in an additive
one.** The audit is run over D1's chart order *k*, D2's RG eigenvalues, P-D's θ,
S5's α, D6's q1/q2, and the critical exponents of
[S3](../S3-fisher-geometry/)/[S7](../S7-critical-slowing/). **A single
counterexample kills C3** and is the outcome I am looking for.

---

## 6. What would make me report a failure

- Leg B's short-range defect grows with N, or the long-range one does not.
- Any additive statistic in leg C giving KL_min > 0, or any non-additive one
  giving 0.
- Leg D's middle value landing at 0 or ½ rather than near 0.293.
- Leg E's audit turning up an exponent on the wrong side.

Legs A, B2 and E1 are identities and are reported with that label attached; if the
write-up ever cites them as evidence, that is the failure mode §4 of the register
names, and it should be called.

## 7. Scope, fixed now

- Everything is equilibrium / stationary, inheriting the tower's own restriction.
- Classical throughout. The quantum-mereology half of the claim — that the
  decomposition into parts is selected by the dynamics — is **argued in the
  derivation and not tested here**. Recorded as untested, not as supported.
- "Long-range" is represented by one mean-field model, not by a 1/r^a family. The
  exponent-1 defect is therefore established for the extreme case only.
- Leg C's construction has iid sites and no interaction; it tests closure of the
  family, not thermalization onto it.
