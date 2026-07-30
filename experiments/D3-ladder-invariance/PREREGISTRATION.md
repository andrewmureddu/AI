# D3 pre-registration — written before any measurement

Works [D3](../../questions/UNKNOWN-LAWS.md#d3--the-ladder-is-a-chart-invariance-count):
if [D1](../D1-chart-invariance/)/[D2](../D2-gauge-group/) are right, "does this
correspondence transfer?" has a mechanical answer — **it transfers iff it is
chart-invariant** — and the [ladder](../../METHODOLOGY.md) is not a scale of
epistemic quality but a count of how many coordinate choices have been quotiented
out.

D3's registered test: *"the ladder-vs-transfer harness already exists; add a
chart-invariance measurement to each rung and check it predicts the transfer score
better than the rung label does."* This pre-registration does that and adds two
legs the stone did not ask for, because the harness makes them cheap and they are
the only genuinely at-risk parts.

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers.

---

## 0. Prior-art note (written first)

**Old, and not marginally so.**

- **Domains of attraction and the index 1/α.** That the aggregate of n i.i.d.
  contributions has scale ∝ n^{1/α}, with α = 2 for finite variance and α < 2 in
  the heavy-tailed case, is Lévy / Gnedenko–Kolmogorov. Every number in P1 is a
  textbook consequence.
- **The CLT as an RG fixed point.** Jona-Lasinio (1975), Sinai, Bleher–Sinai: the
  aggregation-and-rescale map is a renormalization transformation, the Gaussian is
  its fixed point, and 1/α is the eigenvalue of the rescaling. So "chart order of
  the aggregation map" is, in this system, a known object under another name.
- **Normal variance mixtures and exchangeability.** X_i = U·z_i with a shared
  multiplier is a de Finetti-style exchangeable sequence; its aggregate is a normal
  variance mixture, non-Gaussian at every n, and this is the standard textbook
  counterexample to "finite variance ⇒ CLT."
- **Invariance ⇒ transfer** is the explicit thesis of invariant causal prediction
  (Peters–Bühlmann–Meinshausen) and invariant risk minimization (Arjovsky et al.),
  and the failure mode "invariance measured in the wrong statistic does not
  transfer" is well known there.

**Nearest miss, recorded so it cannot be relabelled.** If D3's forward direction
is read as "an estimator generalizes across environments iff it depends only on
invariant structure," it is **N0** — that is IRM's thesis in this repo's
vocabulary. The only thing here that is not covered is the *converse and its
failure*: whether the chart-invariant content is **exhaustible by a ratio**, which
is what [D2](../D2-gauge-group/)'s residue and [P-D](../PD-allometry-reduction/)'s
leg F would need in order to be a general statement rather than two instances.
That is the N2 claim, and it is a claim about **this repo's own residue question**,
not about probability theory.

**Consequence, registered up front: D3 cannot score above N1 on the forward
direction no matter how the numbers land.** What is being tested is whether the
biconditional holds, and the interesting outcome is a failure.

---

## 1. The claim, quantitatively

Domain A learns a law from the surface phenomenon "the macro quantity is the
aggregate of n micro contributions": *the standardized aggregate is Gaussian.* The
harness varies how deeply that law applies in a domain B and measures transfer
skill (1 = the law transfers, 0 = useless).

**The chart-invariance measurement.** For a domain D, define the **aggregation
chart order**

```
        H(D)  =  d ln s(n) / d ln n ,       s(n) = IQR of the n-aggregate
```

— log-response over log-rescaling, [`FLOORS.md`](../../invariants/FLOORS.md) §4's
signature exactly, and measurable **inside one domain with no reference to any
other**. This is the property that makes it a legitimate test rather than a
restatement of the transfer score: H(A) and H(B) never look at each other's
samples.

By D2's rule, a bare H is gauge and a **ratio** is the invariant, so the
cross-domain quantity is

```
        r  =  H(B) / H(A) ,        mismatch  m  =  | r - 1 | .
```

**D3, in this system:** transfer skill is a function of **m** and of nothing else.
In particular m, not the rung label, is what carries the prediction.

## 2. Identity vs. risk — the required disclosure

**Analytic identities. These cannot come out wrong and are not evidence for
anything; they check the estimator:**

- **P1**, every value of H. These are the domain-of-attraction indices.
- **P2's covariance law** H → a·H under the chart φ_a(x) = sign(x)|x|^a. If the
  aggregate is n^H·S for a fixed law S, then φ_a of it is n^{aH}·φ_a(S), so the
  fitted slope must scale by a exactly. Ratio invariance follows immediately. The
  measurement establishes that the estimator is not blind, not that ratios are
  special.
- **P4's H = 1/2 at every mixing strength.** The common factor multiplies the sum;
  it cannot change how the sum's scale grows with n.

**Partly confirmatory, and disclosed as such:**

- **P3.** The transfer numbers 0.033 / 0.484 / 0.916 / 0.894 were measured in
  2026-07-19 and re-analyzed in [`paper/transfer-cliff.md`](../../paper/transfer-cliff.md).
  They are known to me. P3 is therefore a check that a *blind-to-them* measurement
  reproduces their structure — worth doing, and not a prediction of unseen data.

**Genuinely at risk:**

- **P4 — the decoupling sweep.** The only leg that can kill the biconditional, and
  I expect it to.
- **P5 — the common-a half of the re-chart intervention.** D2 flagged the
  common-a commitment as load-bearing and physics-only; here it is tested in a
  system with no singularity and no Φ.

---

## 3. Registered predictions

**P1 — the aggregation chart orders (identity; estimator check).** Fitted slopes
over n = 2^4 … 2^12, each within **±0.03 absolute** (±0.05 for the
infinite-variance rung, whose IQR estimator is noisier):

| Rung | Domain B | H predicted | r = H_B/H_A | m |
|:--:|---|:--:|:--:|:--:|
| — | **A**: uniform increments | **0.5000** | 1 | 0 |
| L4 | exponential increments | **0.5000** | **1.000** | **0.000** |
| L3 | skewed finite-variance mixture | **0.5000** | **1.000** | **0.000** |
| L2 | Student-t, ν = 1.5 (infinite variance) | **0.6667** | **1.333** | **0.333** |
| L1 | single heavy draw (no aggregation) | **0.0000** | **0.000** | **1.000** |

**P2 — H is gauge, r is invariant (identity).** Under φ_a(x) = sign(x)|x|^a
applied to the macro observable, for a ∈ {0.5, 1, 1.5, 2, 3}: every H moves by the
factor **a** (relative error < 2%), while **r is invariant to < 1e-6 relative**
whenever the same a is applied to both domains. Registered because the same
estimator must *report movement where the gauge freedom is real* — D1's F3 lesson.

**P3 — m predicts transfer at least as well as the rung label (confirmatory).**
Two registered comparisons against the existing skills:

- **Ordering.** m must order the four rungs consistently with skill, including the
  fact that skill **ties** L3 and L4 (0.916 vs 0.894, a −0.022 step): m gives both
  exactly 0.000, whereas the label predicts L4 > L3. Registered as the one place
  the invariant does something the label cannot.
- **Fit.** Least-squares R² of skill against m (a single monotone fit) vs. skill
  against the ordinal label. Predict **R²(m) > R²(label)** by at least 0.10.

**P4 — the decoupling sweep (AT RISK; this is the leg that matters).** Add a fifth
domain, **B★**, with increments X_i = U·z_i: z_i ~ N(0,1) i.i.d., U > 0 a lognormal
common factor with coefficient of variation c, drawn once per aggregate.

*Level assignment, made now and not after:* B★ shares the surface phenomenon
(macro = sum of n micro contributions) and shares finite variance, but **not the
mechanism** — A's mechanism is *i.i.d.* aggregation, and independence fails. Its
limit is a normal variance mixture, a different universality class with the same
surface. By the harness's own criteria that is **L2**.

Registered predictions, for c ∈ {0, 0.25, 0.5, 1.0, 2.0}:

- **H(B★) = 0.5000 ± 0.03 at every c**, so **m = 0.000 at every c** (identity).
- **Transfer skill falls monotonically in c**, from the ceiling at c = 0 to below
  the L2 line (< 0.48) by c = 2.0.
- **B★'s standardized shape is a fixed point of aggregation, not slow
  convergence:** shape distance between the n = 64 and n = 1024 aggregates < 0.02,
  while each one's distance to A's Gaussian stays constant to within 0.02.

**If P4 lands as registered, D3's biconditional is dead in the ⟸ direction:** a
family that is chart-invariant *by the ratio measurement* and whose transfer skill
nonetheless sweeps continuously from the ceiling to below L2 — with no cliff, no
quotient, and one number's worth of invariant content held fixed at 1.000
throughout.

**P5 — the re-chart intervention (AT RISK in its second half).** Take the L4 rung
and apply φ_a to the macro observable:

- **B-only re-chart** (a applied to B, not A): m becomes |a − 1|, and transfer must
  **collapse** — skill < 0.60 at a = 2 and at a = 0.5, i.e. below the L2 line.
- **Common-a re-chart** (the same a applied to A and B): m stays 0.000 and transfer
  must be **preserved** — skill within **0.05** of the a = 1 value for every a.

The second half is D2's common-a commitment, tested outside physics. If it fails —
if re-charting both domains together still destroys transfer — then "a shared
chart is a symmetry" is false in a system with no singularity, and the ratios D2
and P-D rest on are not available in general.

---

## 4. What each outcome does

| Outcome | Reading |
|---|---|
| P3 holds, P4 and P5 hold as registered | D3 survives only in the **forward** direction (mismatch ⇒ no transfer), which is N0 by §0. The biconditional is false. |
| P3 holds, P4 fails (skill flat in c) | The biconditional survives a real attack; D3 promotes and the residue question gains "one ratio suffices" as evidence. |
| P3 fails | The chart-invariance reading has no purchase on the ladder at all and D3 dies on its own test. |
| P5's common-a half fails | Worse than D3 dying: it damages **D2** and **P-D**, whose invariant residues both require it. |

## 5. Scope, registered

- **One invariant family** (the CLT/stable limit), inherited from the harness. A
  claim about the ladder in general cannot be settled inside one family, and will
  not be made.
- **H is one chart-invariant, not the chart-free content.** The experiment can show
  a single ratio is insufficient; it cannot enumerate what would be sufficient.
- **Synthetic.** Same limitation the original harness carries.
- The "count of quotiented coordinate choices" half of D3 — that L2 vs L3 differ by
  *how many* group actions have been divided out — is **not tested here**. One
  ratio is one number; a count needs a group with more than one parameter.
  Recorded so a later claim to have tested it cannot be backdated.
