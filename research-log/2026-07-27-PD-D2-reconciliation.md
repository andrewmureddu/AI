# 2026-07-27 — Reconciling P-D with D2: the residue is a ratio, twice over

**Worked on:** [P-D](../experiments/PD-allometry-reduction/) and
[D2](../derivations/D2-gauge-of-the-tower.md), which were run in parallel on
different branches and reached apparently opposite conclusions about the map's P0.
**Change:** P-D gains a post-hoc leg F; #9's floor line corrected from "floor-4
exhibit" to "the structure group's invariant residue";
[`FLOORS.md`](../invariants/FLOORS.md) §4 and `SYNTHESIS.md` §7.0 carry the
reconciliation. No experiment's numbers changed.

## The collision

Two sessions worked the same question at the same time and did not see each other.

- **P-D** (this branch) ran the floor sort's only negative and reported allometry
  as the **third measured exhibit for floor 4**, on the strength of its log-ratio
  form and the measurement that ∇²log Z is rank 1 everywhere.
- **D2** (the discovery-register branch) derived that there **is no fourth
  floor**: the log-ratio signature is the transformation data of `G_pow` relative
  to `G_diff`, and a transformation parameter is not a fact on any floor.

Both edit `FLOORS.md` §4. Merging either one last would have silently overwritten
the other's conclusion, which is the failure mode worth naming: **a merge is not
an adjudication**, and the branch that lands second is not thereby right.

## What I did

Rather than arbitrate in prose, I looked for the measurement that separates them,
and D2's own §4 table supplies it. D2 says an exponent's *magnitude* is gauge but
a **ratio** of exponents at the same singularity is invariant. θ is built as a
ratio of two per-level log-quantities. So the question is decidable: is θ in the
gauge part or the residue?

Added leg F to P-D (labelled post-hoc, since it is not in the pre-registration).

## What I found

**θ is in the invariant residue, and it is not close.**

| Test | Result |
|---|---|
| F1 — θ under coarse-graining the scheme by `a` levels (n → nᵃ, β → βᵃ, γ → γᵃ) | invariant to **2.6e-15** across a = 1…8, while the bare per-level chart ln n moves **8×** |
| F2 — is `G_pow` available at all? mass is extensive | additivity defect **0** at a = 1; **29% / 50% / 41%** at a = 1.5 / 2 / 0.5 |
| F3 — same estimator on a genuine floor-3 chart (λ ~ εᵏ, ε′ = εᵃ) | k moves **3.0×**, tracking 1/a exactly |

F1 is the direct test — coarse-graining is the legitimate reparameterization of a
branching scheme, and it raises numerator and denominator to the same power, so a
ratio survives. F3 is what makes F1 mean something: the identical estimator *does*
report a moving exponent where gauge freedom is real, so the invariance is a fact
about θ rather than a blind fit.

**F2 is the one I did not anticipate, and it is the more interesting half.** D2's
freedom exists because a distance-to-threshold has no canonical scale — ε′ = ε^a
is an equally good distance. Mass is not like that: it is **extensive**, and under
M → M^a with a ≠ 1 masses stop adding, so two organisms side by side no longer
have the mass of the pair. Extensivity *pins the chart* to `G_diff`, where by D2's
own rule (i) exponents are invariant. So `G_pow` was never available for
allometry, and the question of whether θ is gauge under it is moot.

**The two results compose, and the composition is sharper than either.** D2 is
right that the log-ratio *signature* is transformation data — that is what
dissolves the fourth floor. P-D is right that θ is a fact — because it is a
*ratio* of two such quantities, measured against an extensive observable. What
P-D called "the floor-4 signature" is better named the structure group's
**invariant residue**, and it sits alongside D2's codimension p − 2 and
[D6](../experiments/D6-support-singularities/)'s q1/q2 for the same reason: all
three are ratios.

**A first-draft F2 was wrong and is worth recording.** I compared networks at
depths 40 and 55, whose volumes differ by ~10¹¹, so (V₁+V₂)^a ≈ V₂^a ≈ V₁^a + V₂^a
for any a and the additivity defect read 0.03 — which I would have reported as
"extensivity survives re-charting," the opposite of the truth. Comparable
subsystems are required for an additivity test; the equal-depth numbers are the
ones above.

## Decisions

- **#9's floor line corrected.** "Third exhibit for the proposed floor 4" → "the
  structure group's invariant residue." The measurement did not change; its
  interpretation did, and the entry says so rather than quietly restating.
- **P-D's README keeps its original claim with the correction after it**, per
  house style, instead of being rewritten to look like it always said this.
- **The merged §4 keeps D2's resolution as authoritative** and adds P-D's leg F as
  a follow-on, because D2 answers the architectural question and P-D answers where
  one entry lands inside the answer. Those are different questions and the merge
  should not flatten them.

## What this opens

**The residue now has three members derived by three routes, and no general
statement of what it is.** D2 derived p − 2 as the codimension of a floor-3 germ;
D6 generalized it to q1/q2, still at a singularity; P-D's θ is a ratio in a system
with **no singularity and no Φ at all**. "The residue is the codimension" does not
cover the third case. Either there is a common statement — *the residue is the
ratio structure that survives the group*, which is suggestive and currently
contentless — or the scheme layer's invariants are heterogeneous and the three
need separate accounts. This is now the live question in `FLOORS.md` §4, and it is
sharper than the P0 it replaces.

## Next

- **The residue's general form** (above) — the successor to the P0.
- **D3**, the ladder as a chart-invariance count, which the D-branch flagged as
  cheapest and which is sharper now that three independent routes say the
  invariant content is a ratio.
- **P-C**, still unrun, and still needing the selector/source distinction P-D
  found written into its registration.
- The **S25→S27 / S26→S28 renumbering** is still unapplied; `SYNTHESIS.md` §6
  continues to advertise two number collisions.
