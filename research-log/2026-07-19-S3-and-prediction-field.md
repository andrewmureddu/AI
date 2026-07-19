# 2026-07-19 — S3 tested + the prediction-field reframing

**Worked on:** S3 (statistical geometry); the expansion⇄restraint rhythm; the
"environment = prediction field" reframing
**Change:** first experiment added; #20 promoted seed→developing; METHODOLOGY +
new PREDICTION-FIELD.md

## Restraint stroke — S3 tested

Ran the first real experiment ([`../experiments/S3-fisher-geometry/`](../experiments/S3-fisher-geometry/),
pure numpy, deterministic, ~1.4 s). Could not run *grokking* (needs torch /
GPU-scale compute; a failed-to-grok CPU run would be a fake null), so tested the
**same claim** on two exactly-computable transitions.

- **Physics leg (exact):** mean-field Ising Fisher information χ = Var(M)/T
  diverges at **T = 1.000 = T_c**.
- **Learning leg (novel):** ridgeless random-feature regression — the inverse-Fisher
  scale 1/σ_min² blows up at **the same P/N = 1.000** as the double-descent
  test-error peak. `dd_peaks_coincide = true`. The generalization catastrophe *is*
  the Fisher matrix going singular.

**Verdict:** S3 partially confirmed. Same computable geometric signature marks a
transition in both a thermodynamic and a learning system. Honest limits: it's a
Fisher-magnitude/singularity proxy, not the full Riemann scalar curvature; it shows
coincidence-with-a-shared-object (strong L2), not proven mechanism-identity; and
double descent ≠ grokking (still open). Promoted
[`statistical-geometry.md`](../invariants/statistical-geometry.md) seed→developing.

## Method stroke — named the rhythm

Wrote the expansion⇄restraint loop into [`../METHODOLOGY.md`](../METHODOLOGY.md) as
a first-class idea (the user's framing): expansion = leaps (home: SPECULATIVE.md),
restraint = test/prune (home: OPEN-QUESTIONS.md + experiments/), with a stated
graduation path between the tiers. This cycle IS an instance of it: S1/S3 were
expansion; today's experiment was restraint; S3's object graduated.

## Expansion stroke — the prediction-field reframing

New doc [`../PREDICTION-FIELD.md`](../PREDICTION-FIELD.md). Reframes the target:
we're mapping not "recurrences" but the **measurement-invariant predictive
structure** — the prediction field. An invariant = a symmetry of that field.
Tiered honestly: 🟢 operational core (invariant ≡ prediction that transfers —
true almost by definition, and it reorganizes the repo), 🟡 formal support
(Bayesian priors, Crutchfield predictive/causal states, predictive information,
predictive processing, Pearl's SCMs all put a predictive object before the datum),
🔴 the strong "ontologically prior" reading (Wheeler/QBism — generative, not
provable).

Nice tie-in: the Fisher metric *is* the geometry of distinguishability of
predictions, so today's S3 result reads as "the prediction field goes singular at a
transition" — already measured. And it gave the frame a falsifier: ladder level
should predict cross-domain *transfer performance*; if it doesn't, the reframing is
decorative and drops to 🔴-only.

## Next

- **S3 strengthen:** show the inverse-Fisher peak *leads* the error peak in
  training time (early warning), not just coincides in capacity.
- **S1 (pure derivation, no compute):** write the explicit replicator ↔ MW ↔ Bayes
  ↔ Gibbs dictionary (Bregman divergence + step size each). Next expansion-tier
  item ripe for a restraint pass.
- **Prediction-field falsifier:** design the level-vs-transfer test on 3–4
  invariants.
