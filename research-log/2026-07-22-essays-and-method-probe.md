# 2026-07-22 — Essays, the periphery split, and probing the method's self-description

## What happened

1. **`essays/` opened** (four essays + ground rules): the ladder as an
   epistemology; the Φ-collapse as localized Wigner; expansion⇄restraint as
   error dynamics; the periphery split. Essays cite the ledger, tag registers,
   and never carry ladder levels.

2. **S25 promoted** from essay 4 into
   [`SPECULATIVE.md`](../questions/SPECULATIVE.md) (new Cluster K): feedback/
   control should split into a Φ-reducible inference half (LQG↔Kalman,
   KL-control) and an irreducible reachability half (Gramian rank conditions),
   with a two-sided falsifier. Cheaper siblings queued behind it: diffusion
   must reduce (kills the sorting rule if it doesn't); percolation must resist
   even through the Potts q→1 dressing.

3. **Essay 3's L3 suspicion probed and settled** —
   [`derivations/essay3-method-as-update.md`](../derivations/essay3-method-as-update.md).
   Claim was: the expansion⇄restraint method is itself an instance of S1's
   universal update (★). Result: **retired as stated.**
   - Level assignment = per-entry Bayes over {L0…L4}: exactly (★), L3, trivially.
   - Attention allocation: the only real population-level candidate; mechanism
     unwritten, one log epoch → L1–L2, currently unfalsifiable.
   - Expansion: provably outside (★) — multiplicative updates preserve zeros;
     support growth is impossible for mirror descent. **The method is a
     replicator–mutator with a zero-sum attention budget**, not the universal
     update; only its selection term is S1's object.
   - Consequence: essay 3 §5's self-licensing worry downgraded 🔴 → 🟡. The
     loop isn't closed if the generative half lies outside the object studied.

## Decisions

- Restraint notes go *into* the essays (⟳ blockquotes) rather than silently
  editing them — essays keep their dead, same as the catalog.
- The revival condition for the attention face is now a designed experiment:
  define g_i = −log falsifier-survival likelihood, η = session expansion/
  restraint ratio; run ≥3 epochs at deliberately different tempos; check the
  mirror-descent regret prediction. Needs epochs we don't have yet — the log
  gains value for this test simply by accumulating dated sessions at varied
  tempo.

## Open

- S25 (control split) is the sharpest periphery test — next restraint target.
- Meta-observation worth one line: the probe found the boundary by lemma while
  *preparing* the listed empirical falsifier. Falsifiers earn their keep even
  when the kill arrives from elsewhere.
