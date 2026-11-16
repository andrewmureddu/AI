# D13 — which part of an m-control residue is spectral

**Tests:** [D13](../questions/UNKNOWN-LAWS.md). [D11](./D11-residue-reconciliation.md)
§2 identified D7's ray with the projectivized eigenvalue vector and added that
D8's Gr(r, n) "is the same statement with r simultaneous controls." The
second half was never derived. Numerics:
[`experiments/D13-two-control-description-map/`](../experiments/D13-two-control-description-map/).

Standard scaling theory throughout; nothing here is new mathematics.

---

## 1. Euler

Let the description map have relevant eigenvalues λ₁…λ_r with linear scaling
fields ε₁…ε_r, and let observable O_i transform with weight μ_i:

```
        O_i(lambda_1^s eps_1, ..., lambda_r^s eps_r)  =  mu_i^s  O_i(eps)        (*)
```

If (\*) holds for all real s, differentiate at s = 0:

```
        sum_j  Y_ij ln lambda_j  =  ln mu_i ,      i.e.   Y · l  =  w .
```

So **w ∈ col(Y) at every base point.** One direction of D8's plane is
spectral: it is the vector of observable weights, and projectively it is
D7's ray for the one-parameter approach s ↦ (λ_j^s ε_j).

## 2. The other r − 1 directions

(\*) says O_i = ε₁^{w_i/ℓ₁} Φ_i(κ), where κ collects the r − 1 scale-invariant
ratios ε_j/ε₁^{ℓ_j/ℓ₁}. Then

```
        Y_i1 = w_i/l_1 - sum_j (l_j/l_1) d ln Phi_i / d ln kappa_j ,
        Y_ij = d ln Phi_i / d ln kappa_j        (j >= 2).
```

The columns j ≥ 2 are logarithmic derivatives of the scaling functions. They
depend on κ unless every Φ_i is a monomial, and they are not functions of the
spectrum. Hence

```
        col Y(kappa)  =  span{ w,  d ln Phi / d ln kappa_2, ... } ,
        intersection over kappa of col Y(kappa)  =  <w>      (generically).
```

**The spectral content of an m-control residue is one ray. The Grassmannian
point contains it and does not determine it;** two base rays do.

Counting, for n = 4, r = 2: the plane is 4 numbers, the ray is 3, and planes
through a fixed line form a 2-parameter family — so a plane is neither more
nor less than the ray, it is a different object that happens to contain it.

## 3. Discrete maps

If the map is iterated in whole steps, (\*) holds only for integer s. Then
O_i = ε₁^{w_i/ℓ₁} Φ_i(κ, ln ε₁ / ℓ₁) with Φ_i periodic of period 1 in its last
argument, and

```
        Y · l  =  w  +  d ln Phi / d(phase) .
```

The correction integrates to zero over a period and is otherwise
unconstrained. The exact statements are the per-step increment
ln O_i(λε) − ln O_i(ε) = w_i and the period mean Ȳ·ℓ = w. Measured: 4.9e-7
and 3.0e-7 respectively, against a pointwise residual of up to 6.7e-2.

## 4. What changes

- D11 §2, last sentence of the C1 paragraph: **withdrawn for m > 1.** D7's ray
  is the projectivized spectrum; D8's plane is the ray plus scaling-function
  directions.
- D8: its invariance statement (col(Y) fixed under Y ↦ YA⁻¹ at a base point)
  and its rank statement are untouched. Its implicit claim that col(Y) is
  *the* residue of the singularity needs "at this base ray."
- D7 §1's remark that a discrete chart uses per-level increments is promoted
  from a convention to a requirement.

**Scope.** One model, m = 2, no irrelevant direction, disordered side. "Only
one ray is spectral" is derived for linear scaling fields; nonlinear fields
change (\*) by analytic factors that vanish at the fixed point (measured:
below 5e-7 at t = 1e-6). Whether D8's own germs show the same κ-dependence is
predicted by §2 and not checked.
