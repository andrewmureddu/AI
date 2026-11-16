# D12 — what the residue's blindness actually is

**Tests:** [D12](../questions/UNKNOWN-LAWS.md). [D11](./D11-residue-reconciliation.md)
concluded that the residue "is exactly blind to whatever is tangent to the
fixed-point set" and named two untested cases. This takes the nonlinear one,
and finds the sentence needs a qualifier that changes its meaning.

**Result.** On the fixed-point set, the residue is the **spectrum map**
σ : Fix(T) → {projectivized spectra}. It is blind to exactly ker dσ. Orbits of
maps that commute with T lie in ker dσ (§1); a general tangent direction does
not (§3). D11's family was the first kind, and only for a map other than the
one D11 named (§2). Numerics:
[`experiments/D12-nonlinear-description-map/`](../experiments/D12-nonlinear-description-map/).

Nothing below is new mathematics. §1 is linear algebra, §2 is cumulant
additivity plus Jona-Lasinio's spectrum, §3 is Feigenbaum theory.

---

## 1. C1 — intertwining gives isospectral fixed points

**Lemma.** Let M∘T = T∘M and T x\* = x\*. Then T(M x\*) = M x\*, and

```
        DT(M x*) · DM(x*)  =  DM(x*) · DT(x*).
```

*Proof.* T(Mx\*) = M(Tx\*) = Mx\*. Differentiate M∘T = T∘M at x\* by the
chain rule and use T x\* = x\*. ∎

So if DT(x\*) v = λ v and DM(x\*) v ≠ 0, then DM(x\*) v is an eigenvector of
DT(M x\*) with the same λ. Along a family of fixed points that is an orbit
{M_s x\*} of commuting maps, every eigenvalue not killed by DM persists, and
the log-slope vector D7 builds from them is the same at every point. **A
symmetry orbit is a blind direction, exactly and at every finite n**, not only
asymptotically. M need not be invertible; an intertwiner is enough for this
direction of the statement.

The converse is not claimed. Differentiating T(x_s) = x_s along *any* curve of
fixed points gives DT(x_s) ẋ_s = ẋ_s — the tangent is a marginal direction —
and says nothing about the rest of the spectrum. Whether the spectrum moves is
dσ, and it is a fact about the family, not about tangency.

## 2. C2 — D11's family, under the map D11 named

D11 §3 defines T: law(X) ↦ law((X₁+X₂)/√2) with X₁, X₂ **iid**, then proves
the fixed-point property for S_n = U·(Z₁+…+Z_n), one U shared by the whole
aggregate. These are different maps.

**Shared U.** Conditional on U = u the aggregate is the Gaussian law(uZ),
which is a fixed point of T, and {law(uZ)}_u is the orbit of the dilations
D_u, which commute with T. Shared-U aggregation is T applied fibre by fibre
with U conserved, extended to mixtures by linearity. The U-family is a set of
mixtures over a C1 symmetry orbit; §1 gives constancy of the scale eigenvalue
on each fibre and linearity carries it to the mixture. **That is the whole
reason D11's residue was blind.**

**Iid.** Cumulants add under independent sums, so for S_n = ΣU_iZ_i

```
        kappa_4(S_n / sqrt(n))  =  kappa_4(X) / n,      exactly, every n.
```

X = U·Z has κ₄ = 3·Var(U²) > 0 unless U is constant, so the U-family is not
fixed: it flows to the Gaussian. The linearized map at the Gaussian has
Hermite eigenfunctions with λ_k = 2^{1−k/2} (Jona-Lasinio 2001); the leading
deviation of a symmetric law is k = 4, λ₄ = 1/2 per doubling, i.e. n⁻¹. Any
shape statistic that is a smooth functional of the law inherits it at leading
order. Against the scale spread's √2 per doubling, the residue ray is

```
        [ ln sqrt(2) : ln (1/2) ]  =  [ 1/2 : -1 ],      ratio -2.
```

Measured on D11's own quantile statistic: −2.0002 … −2.0021.

**So the same direction has two roles.** Under the shared-U map it is tangent
to a fixed-point set and invisible. Under the iid map it is irrelevant and
plainly visible. "Tangent" is a property of the pair (direction, map), and
D11's conclusion was stated for the wrong member of the pair.

## 3. C4 — a tangent direction the residue sees

The doubling operator T f(x) = −α f(f(−x/α)) acts on unimodal maps of any
critical order. For each z > 1 it has a fixed point g_z(x) = G_z(|x|^z), and T
preserves z, so z ↦ g_z is a curve in Fix(T) with ∂_z g_z a DT-eigenvector of
eigenvalue 1 (§1's last paragraph).

It is not an orbit of the commuting maps in hand: the conjugacies that
commute with T's rescaling are dilations, and dilations preserve z. (I have
not proved that *no* commuting map carries g₂ to g₃; the measurement below
shows none can, since by §1 it would force equal spectra.) §1 therefore predicts nothing about σ along it, and the measured
answer is that σ is injective on the tested range:

```
        z      1.5      2        3        4        8
        rho    0.914    0.595    0.363    0.264    0.128       (rho = ln alpha / ln delta)
```

Within this family the residue *determines* the fixed point. That is the
opposite of D11's "necessary but never sufficient."

## 4. Three kinds of direction, one construction

| direction at a fixed point | what the log-slope residue does | instance |
|---|---|---|
| irrelevant | blind **asymptotically**, at the direction's own rate | D8 P4; families A vs B here; the U-direction under the iid CLT map |
| tangent, along a commuting orbit | blind **exactly**, at every n | dilations; D11's U-family under shared-U |
| tangent, not along a commuting orbit | **not blind in general** — σ may vary | z ↦ g_z |

D11 merged the second and third rows.

## 5. Corrected statement

> The residue is the projectivized spectrum of DT at a fixed point. On Fix(T)
> it is a function, σ, and it is blind to ker dσ and nothing else. Symmetry
> orbits of T are always in ker dσ. Where σ is locally injective the residue
> is a coordinate on the fixed-point set; where σ is constant it carries no
> information about which fixed point one is at.

"Necessary but not sufficient" survives as a statement about D11's family and
about any symmetry orbit. "Never sufficient wherever the fixed-point set has
tangent directions" does not survive.

**Scope.** One nonlinear map with one relevant direction (m = 1). C1 is
sufficient, not necessary: a non-orbit family with constant σ is not excluded.
The eigenvalue-1 claim for ∂_z g_z is derived, not measured. D8's m > 1 case
under a literal description map remains open.
