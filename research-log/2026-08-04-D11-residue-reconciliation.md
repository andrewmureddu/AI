# 2026-08-04 — D11: the residue reconciled, and why D3's counterexample was never a fluke

**Worked on:** [D11](../questions/UNKNOWN-LAWS.md), the question flagged in the
same session's branch-reconciliation pass —
[`SYNTHESIS.md`](../SYNTHESIS.md) §7.0(iii) named three independently-produced
accounts of "what the residue is in general"
([D7/D8](../derivations/D7-the-residue.md)'s projective/Grassmannian point,
[D10](../derivations/D10-composition-lens.md)'s composition-pinning criterion,
[D3-ladder-invariance](../experiments/D3-ladder-invariance/)'s "fixed point of
the description map, ratio as eigenvalue") as never checked against each
other.
**Change:** new derivation
[`derivations/D11-residue-reconciliation.md`](../derivations/D11-residue-reconciliation.md)
+ experiment
[`experiments/D11-residue-reconciliation/`](../experiments/D11-residue-reconciliation/);
the three accounts are shown to be one structure; `SYNTHESIS.md` §7.0's flagged
note is resolved; `FLOORS.md` §4 gets a matching note; the register's stone
count moves to 11.

## What I did

Read all three source documents closely before writing anything — D7's
derivation, D8's README, D10's derivation, D3-ladder-invariance's README — to
understand what each was actually claiming, not just the one-line summaries
already in `SYNTHESIS.md`.

D7/D8's construction (log-slopes of observables against a control, invariant
up to the diagonal/monomial reparameterization group) recognizably matched
textbook renormalization-group scaling theory: a critical exponent *is* an
eigenvalue of the linearized RG map at a fixed point, read against the map's
own rescaling factor. D3-ladder-invariance's "fixed point of the description
map" language, applied to an aggregation harness (sums of n increments), was
recognizably the same object probability theorists call the fixed point of a
renormalized-convolution operator — the modern RG treatment of the CLT and
stable laws. Checked both via `WebSearch` before writing a prior-art note,
per house discipline (the register's own rule against asserting a citation
that hasn't been checked): confirmed Jona-Lasinio's *Renormalization group and
probability theory* (Phys. Rep. 352, 2001) and its generalized-CLT
continuation (Calvo, Cuchí, Esteve & Falceto, J. Stat. Phys. 141, 2010,
arXiv:1009.2899) as the exact match; confirmed "critical exponents are
eigenvalues of the linearized RG transformation" as standard textbook content;
and searched for the closest known analogue to "a continuum of fixed points
sharing some invariant data while the theory genuinely differs" — found two,
neither exact (KT-type lines of fixed points, where exponents *do* vary along
the line; CFT conformal manifolds, where protected dimensions stay fixed
under a supersymmetry guarantee this construction doesn't have).

Pre-registered before any code, in a separate commit: the identity (C1/C2 —
proved analytically, not tested) and the at-risk numeric claims (C3/C4).

## What I found

**C1/C2 give a real proof, not an analogy.** For the dyadic renormalized-sum
map T: law(X) ↦ law((X₁+X₂)/√2) — the CLT's own RG, and literally what
D3-ladder-invariance's aggregation harness iterates without naming — *any* law
of a positive random variable U makes the scale mixture X = U·Z (Z ~ N(0,1)
independent of U) an **exact** fixed point: S_n =_d √n·X for every n and every
U-law, by nothing more than the self-similarity of the Gaussian under
convolution. This gives an explicit, infinite-dimensional continuum of
genuinely distinct laws that are all simultaneously exact fixed points sharing
one eigenvalue.

**The numbers came in essentially perfect.** Applying the exact same
log-log-regression estimator this arc has used since D1 — but to *exact*
quantiles (root-found on the closed-form mixture CDF, no Monte Carlo) instead
of sampled ones — recovered H = 0.500000000 with every deviation at the
machine-epsilon floor (≤1.7e-16) across 5 mixture configurations × 2
observables, against a registered tolerance of 1e-6. This wasn't the at-risk
part (the identity is proved), but it is a clean confirmation that the
earlier D3 run's 0.4923–0.4951 spread was sampling noise around the exact
value, not evidence of anything else — worth stating plainly since it hadn't
been checked.

**The falsifiable core passed too, and by a wide margin.** A scale-invariant
shape statistic (a ratio of quantile spreads — by construction exactly the
direction tangent to the fixed-point set, since it can't have any log-slope
against n at all) was registered to vary by at least 15% across the same five
configurations while H stayed flat. Measured: 208% spread, with the pure-
Gaussian configuration's value (2.9058) matching the textbook normal quantile
ratio as an independent sanity check on the whole pipeline, while the shape
statistic itself is exactly n-invariant (≤1.1e-14) — confirming it really is
tangent to the fixed-point set, not merely slow to converge to one.

**D10 turned out not to be a competing account at all.** It answers a
different question — which variables carry an eigenvalue structure to begin
with — and checking it on a variable the register hadn't used it on (the
aggregate count n) gave a clean, independent confirmation: n is additive under
concatenation, so its chart is pinned, matching what
[D3-ladder-as-quotient](../experiments/D3-ladder-as-quotient/) had already
found on the same harness from a different angle.

## Decisions

- **D11 registered as the reconciliation's own stone**, N1 (recombination of
  known results, correctly composed — every load-bearing piece is textbook,
  named in the prior-art note before any code). The one thing not previously
  stated, in this repo or in the literature search, is the specific
  cross-connection of these four independently-produced results, and the
  closed-form proof that the residue's blindness to fixed-point-tangent
  directions is general rather than a property of D3's one accidental
  counterexample — which is what keeps this above N0.
- **`SYNTHESIS.md` §7.0's flagged note is resolved**, not deleted — replaced
  with the reconciliation and its honest scope (checked in one setting;
  D8's m > 1 case and a genuinely nonlinear description map remain open).
- **`FLOORS.md` §4 gets a matching `⟳ RECONCILED` note** appended after the
  original D3 finding, per the register's append-only convention — the
  original text is kept, not rewritten.
- **Discovery-stone count moves 10 → 11**; experiment/derivation counts
  recounted directly against the tree (33/33, 10/10 — every directory and
  file has an index row).

## Next

- **D8's m > 1 case is untested here.** Does a multi-control description map
  (a genuine Grassmannian, not just a ray) have the same tangent-direction
  blindness, and does it admit as clean a closed-form example?
- **A genuinely nonlinear description map** — this stone's example is exactly
  solvable because the Gaussian's self-similarity under convolution is linear
  algebra in disguise. A real RG flow (an interacting model, not a
  renormalized sum) would test whether the identification survives when the
  fixed-point set's tangent directions aren't available in closed form.
- **The kink note in `FLOORS.md`** (D7's algebraic location of P-D's kink vs
  P-K's finite-size-rounding account) is a separate open reconciliation this
  pass did not touch — flagged there since 2026-07-28, still open.
