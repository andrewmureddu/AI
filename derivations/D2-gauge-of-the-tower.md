# D2 — the scheme layer is the tower's gauge group

*2026-07-26. Works [D2](../questions/UNKNOWN-LAWS.md), which was opened by
[D1](../experiments/D1-chart-invariance/) and inherits the map's standing P0:
[is there a fourth floor?](../invariants/FLOORS.md)*

**Result: no fourth floor. The scheme layer is the transformation data of a group
— the difference between the group the tower's floors are defined up to and the
weaker group available for cross-domain comparison. Its chart-free residue is a
single integer, the codimension of the singularity, which is
[D1](../experiments/D1-chart-invariance/)'s *p* − 2 and therefore floor-3 data.**

The resolution also settles a question D1 left dangerously open — whether critical
exponents are "meaningless" — and the answer is no, in a way that turns out to be
the whole point: **within a domain, exponents are facts; across domains, only their
ratios are.**

---

## 1. What has to be decided

[`FLOORS.md`](../invariants/FLOORS.md) §4 found four things refusing floors 1–3
with one shared signature: their invariant is a **log-ratio**, log(multiplicity)
over log(rescaling) — S5's concatenation exponent ln n₀/ln(t+1), a fractal
dimension ln N/ln b, RG eigenvalues, and (degenerately) bookkeeping identities.
It proposed a fourth floor and named the live alternative as floor 1 in disguise.

[D1](../experiments/D1-chart-invariance/) added a third option by noticing that
its own chart order is

```
        k  =  d ln λ / d ln ε
```

— the same signature — and by showing *k* is removable: under ε′ = ε^a the chart
order changes while every λ-chart exponent is unmoved. That suggests the refusers
are not facts on any floor but coordinate freedom.

The counter-horn was recorded at the same time and is the thing to beat: **an RG
eigenvalue predicts which perturbations are relevant.** That is predictive work,
and predictive work is not obviously gauge.

Deciding this requires being explicit about something the repo has never stated:
*which group* the tower's floors are defined up to.

## 2. Two groups

Let ε ≥ 0 parameterize the approach to a singularity at ε = 0, and let φ be a
reparameterization: an increasing homeomorphism of a neighbourhood of 0 fixing 0.

- **G_diff** — φ is a diffeomorphism *including at the endpoint*: φ′(0) exists and
  φ′(0) ≠ 0. Near 0, φ(ε) = cε + O(ε²) with c ≠ 0.
- **G_pow** — φ(ε) = c·ε^a·(1 + o(1)) for some a > 0. A homeomorphism, and a
  diffeomorphism *away from* 0, but at 0 its derivative is 0 (a > 1) or ∞ (a < 1).

**G_diff ⊊ G_pow**, with equality only at a = 1. The enlargement lives entirely at
the singular point — which is already the first structural fact worth having,
because it says the extra freedom exists **exactly on floor 3** and nowhere else.

Two elementary consequences, stated so the rest can lean on them:

> **(i) Exponents are G_diff-invariant.** If X ~ ε^θ and φ ∈ G_diff, then
> ε ≈ ε′/c and X ~ (ε′/c)^θ: **θ is unchanged**, only the amplitude moves.
>
> **(ii) Exponents are G_pow-covariant.** Under ε′ = ε^a, ε = ε′^{1/a} and
> X ~ ε′^{θ/a}: **θ → θ/a**.

So an exponent is a *fact* under G_diff and a *coordinate* under G_pow. Everything
below is a consequence of which group is available.

## 3. RG eigenvalues are the same object as chart orders

Let R be a coarse-graining map on couplings with fixed point g\*, rescaling factor
b, and linearization M = DR(g\*), eigenvalues Λ_i, RG exponents y_i = ln Λ_i / ln b.

**Under G_diff: invariant.** A smooth coordinate change h with Dh invertible sends
R ↦ h∘R∘h⁻¹ and therefore M ↦ (Dh) M (Dh)⁻¹. Eigenvalues are conjugation
invariants, so **every y_i is unchanged**. This is why universality classes are
well defined and why quoting ν = 1.338 for the diamond hierarchical lattice is
meaningful: it is an invariant of an equivalence class under smooth
reparameterization.

**Under G_pow: covariant.** In an eigencoordinate the map is u′ = Λu. Put
v = u^a. Then v′ = (u′)^a = (Λu)^a = Λ^a v, so

```
        Λ  →  Λ^a  ,        y  →  a · y
```

which is exactly rule (ii) applied to the inverse exponent (ν = 1/y_t transforms as
ν → ν/a, as an exponent must).

**Therefore an RG eigenvalue and a chart order have identical transformation
behaviour: G_diff-invariant, G_pow-covariant.** They are the same kind of object.
FLOORS.md's log-ratio signature is not a coincidence of four unrelated quantities;
it is the statement that all four are **transformation data of G_pow relative to
G_diff.** A fractal dimension is the chart order of a self-similar map (and
correspondingly is a bi-Lipschitz invariant but not a homeomorphism invariant);
an RG eigenvalue is the chart order of the coarse-graining map; S5's type-R
exponent is the chart order of a decoder recursion; double-entry accounting is the
degenerate case, conserving because its chart is constant.

## 4. What survives G_pow

Under a **common** reparameterization (one a for the singularity):

| Quantity | G_diff | G_pow |
|---|:--:|:--:|
| an exponent's magnitude θ | invariant | **θ/a — gauge** |
| the sign of θ (relevant / irrelevant) | invariant | **invariant** |
| the number of relevant directions | invariant | **invariant** |
| a ratio θ₁/θ₂ at the same singularity | invariant | **invariant** |

A single exponent can be set to any positive value — in particular to 1 — by
choosing a. Its numerical value therefore carries no information without a stated
chart. Signs survive because a > 0. Ratios survive because both exponents are
divided by the same a.

**The counter-horn, answered.** "An RG eigenvalue predicts which perturbations are
relevant" is a claim about the **sign** of y, and signs are G_pow-invariant. So the
predictive work is real and it survives — but it survives *precisely in the part
that is not gauge*, and that part is a sign and a count, not a log-ratio. The
counter-horn does not restore a fourth floor; it identifies which piece of the
scheme layer is chart-free.

**A caveat kept rather than buried.** If one allows *independent* power maps per
eigendirection — v_i = u_i^{a_i}, still a legitimate homeomorphism, still
diagonalizing to eigenvalues Λ_i^{a_i} — then ratios die too and only signs
survive. The common-a group is the operative one for the question this repo asks,
and the reason is not aesthetic: a domain supplies **one** notion of distance to
threshold, and the reparameterization freedom D1 identified is the freedom in that
one choice. Nothing in cross-domain practice exercises a separate arbitrary
distance scale per eigendirection. This is a modelling commitment and it is stated
as one; the results below hold under it and weaken to sign-only without it.

## 5. The resolution

Putting §2–§4 together:

> **The tower's floors are defined up to G_diff. Cross-domain comparison has only
> G_pow. The scheme layer is exactly the difference — the transformation data of
> G_pow modulo G_diff.** That is why its members are all log-ratios, why they
> refused floors 1–3 (a transformation parameter is not a fact on any floor), and
> why four unrelated objects carried the *same* signature, which a genuine new
> floor would have had no reason to produce.

So the answer to the P0 is **not** "there is a fourth floor" and **not** "the
scheme layer is floor 1 in disguise." It is that the scheme layer is not a layer
of facts at all — it is the tower's **structure group**, and the tower was always
implicitly defined up to it.

**And it explains the asymmetry the sort could not.**
[`FLOORS.md`](../invariants/FLOORS.md) found, without explanation, that *floor 2
collapses and floor 3 stratifies*. The group makes it a theorem-shape rather than
an observation: away from the singular point G_pow = G_diff, so floor-2 objects
live under the ordinary smooth group where tensorial quantities have genuine
invariants — hence one convex function seen from seven angles. At the singular
point the group is strictly larger, and the enlargement eats exponent magnitudes
while leaving a discrete residue — hence a classified set rather than a collapse.
**The asymmetry is a statement about which group acts where.**

## 6. The residue is the codimension — and it is D1's *p*

> **⟳ Scoped 2026-07-27 by [D7](./D7-the-residue.md), which generalizes this
> section rather than contradicting it.** Everything below is correct **for a
> smooth floor-3 germ**, and that is how the heading should be read. What does not
> generalize is the *integrality*: the residue is the log-slope vector modulo the
> diagonal ℝ⁺, i.e. a point of ℝP^{n−1}, and a projective space has no
> distinguished rational points. The integer here is inherited from Taylor orders
> being integers once smoothness pins the leading exponent to 2 — with
> incommensurable leading exponents the residue is irrational (measured: 1 − 1/π
> and 1/√2). Two further amendments in D7's favour: "the residue is **one**
> integer" is the n = 2 case of a count that reads **n − 1**, and §7's common-*a*
> commitment below is *derived* there rather than stipulated — it is the statement
> that the action is the diagonal, which is what approaching one singularity along
> one family means.

What is left of the scheme layer after the gauge is removed? Signs, counts, and
ratios. These are not three things.

For a degeneracy-type floor-3 singularity with leading anharmonicity Φ ~ y^p, the
number of coefficients that must be tuned to sit exactly on it — a₂ through
a_{p−1} — is **p − 2**. That is the codimension of the A_{p−1} germ, and it is the
number of relevant directions the RG sees at the corresponding fixed point.

The ratios say the same thing. Minimising Φ = λy²/2 + g y^p gives
m ~ λ^{1/(p−2)}, so with λ ~ ε^k the order-parameter and chart exponents obey

```
        beta / k  =  1 / (p - 2)
```

a **chart-free ratio equal to the reciprocal codimension**. Predictions:
1 for the fold and the SIS epidemic (p = 3), ½ for mean-field Ising (p = 4),
¼ for a tricritical point (p = 6) — while β and k separately vary with the chart.
This is the derivation's one genuinely at-risk output and it is what
[`experiments/D2-gauge-group/`](../experiments/D2-gauge-group/) tests on full
models.

> **So the chart-free residue of the scheme layer is a single integer, the
> codimension p − 2 — which is [D1](../experiments/D1-chart-invariance/)'s
> degeneracy order. The fourth floor dissolves into gauge plus floor 3, and what
> was underneath it all along was *p*.**

## 7. Why exponents are not thereby meaningless

D1 left an obvious worry: physics measures critical exponents, they are universal,
they are checked against experiment. If exponent magnitudes are gauge, what is
being measured?

The answer is §3's first half. **Universality is a G_diff statement**, and under
G_diff exponents are strictly invariant. A universality class is an equivalence
class of systems under smooth reparameterization, and physics fixes the chart
canonically: the reduced temperature is the coupling that enters the Hamiltonian
*linearly*, so the space of couplings carries a linear structure and G_diff is the
group that respects it. Within that structure, ν = 1.338 is a fact.

What D1 discovered is that **cross-domain comparison is not a G_diff comparison.**
A decoder recursion, a queue at saturation, an epidemic at R₀ = 1 and a
least-squares fit at the interpolation threshold do not share a linear structure on
their control spaces — they share only a topological one. Comparing their exponents
is quotienting by G_pow whether or not anyone says so, and under G_pow the
magnitudes are not comparable.

> **Within a domain, exponents are facts. Across domains, only ratios, signs and
> counts are.** S5 and S7 reported "domain-specific exponents"; the correct
> statement is that they compared G_diff-facts across a G_pow gap.

## 8. What would kill this

- **A scheme-layer quantity whose magnitude does chart-free predictive work.**
  Exhibit a prediction that (a) depends on the numerical value of a log-ratio
  exponent, and (b) is unchanged under ε′ = ε^a. §4 says this is impossible under
  common-a; a counterexample kills the derivation outright and restores the fourth
  floor.
- **An invariant of a description map whose signature is not a log-ratio.** Breaks
  the identification from the other side — the scheme layer would then be larger
  than the group's transformation data.
- **β/k ≠ 1/(p−2)** in full models. Kills §6's identification of the residue with
  the codimension, leaving the group analysis intact but the residue unidentified.
- **A domain pair with a genuinely shared linear structure whose exponents still
  fail to transfer.** Would show G_diff is not what makes exponents comparable, and
  §7's reconciliation is wrong.

## 9. Scope

- **Degeneracy-type singularities only**, inherited from D1. Support-type
  singularities (S5's type S) have no *p*, so §6's identification of the residue
  does not reach them; §2–§5's group analysis does, since it never mentions *p*.
  What the residue *is* for a support-type singularity is open
  ([D6](../questions/UNKNOWN-LAWS.md)).
- **One control parameter.** Multi-parameter approaches (a critical *surface*
  reached along a path) raise the independent-vs-common question of §4 in a form
  this derivation settles by assumption rather than by argument.
- **The common-a commitment is a commitment**, restated here so it is not lost:
  under independent per-direction power maps the ratio results fail and only signs
  survive.
- **"Gauge" is used in the precise sense of §4** — a quantity whose value can be
  changed by a coordinate choice with no observable consequence — not by analogy
  to gauge field theory. Whether the analogy is more than terminological is
  [S10](../questions/SPECULATIVE.md), and is not claimed here.
