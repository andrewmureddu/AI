# 2026-07-24 — Synthesis refresh, and a numbering collision fixed

> **⟳ Recovered 2026-07-27.** This entry sat on an unmerged branch
> (`claude/continuation-k0958d`) for three days and is added here so the record
> is complete. Read it with two corrections:
> **§1 stands** — the renumbering it argues for is the one the repo now uses, but
> it was applied as a [fresh commit on 2026-07-27](./2026-07-27-PD-D2-reconciliation.md),
> not from this branch, because by then a dozen files merged after it referenced
> the old directory names. Its choice to leave pre-dated log prose untouched was
> kept.
> **§2 is superseded.** The synthesis refresh described here was overtaken by the
> [2026-07-25 refresh](./2026-07-25-S5-and-synthesis-refresh.md) and then twice
> more; the §3 ledger it describes no longer resembles the current one. It is
> kept as a record of what was true on 2026-07-24, which is what a dated log is
> for.

Bookkeeping session, no new claims. Two jobs, both flagged as pending by the
2026-07-22 log.

## 1. Cluster K renumbered: S25/S26 → S27/S28

The periphery-split cluster was filed on 2026-07-22 reusing stone numbers
Cluster G already held (S25 = RLCT chart, S26 = degeneracy-as-attractor). With
four experiment directories and two derivations referencing them, "S26" had
become ambiguous in exactly the documents whose job is to be unambiguous —
and the synthesis ledger could not be written without resolving it.

- S25 (feedback/control splits in two) → **S27**;
  `derivations/S25-control-split.md` → `derivations/S27-control-split.md`.
- S26 (conserved charges are the coordinates) → **S28**;
  `experiments/S26-sgd-charges/` → `experiments/S28-sgd-charges/`.
- Cluster G's S25/S26 untouched. Cross-references updated in `SPECULATIVE.md`,
  both derivations, `derivations/README.md`, `experiments/README.md`,
  `experiments/S7-critical-slowing/README.md`, and `essays/04`.
- **Research-log entries dated before today were left as written** — the log is
  a dated record, not a live index. The renumber is noted at the head of
  Cluster K and in `SYNTHESIS.md` §5.

Stones are now S1–S28 with no collisions; 11 have had a restraint pass.

## 2. SYNTHESIS.md refreshed (was 2026-07-19, two architectures out of date)

The through-line had changed twice since the last snapshot (three sectors → two
layers → one tower) and the ledger was missing five restraint passes. What
changed in the document:

- **§1 / §4 rewritten around the tower.** "Core + independent periphery"
  replaced by *one object, three floors — chosen by symmetry, read by
  prediction, ended by breakdown*. The old snapshot's "tantalizing secondary
  thread" (power laws live where Φ misbehaves) is now the load-bearing floor,
  not a conjecture in a footnote.
- **§3 ledger extended** from 6 rows to 13: S25, S26, S27, S28(iii), S7, and
  the symmetry-sector and method-as-update derivations. Split and falsified
  verdicts (S26's attractor claim, S7's exponent reading, essay 3's
  self-description) sit in the same table as the confirmations, since they cost
  the same to earn.
- **§2 gained the method-is-not-its-own-subject result** — the self-licensing
  worry is closed by a lemma, and that belongs in the method summary rather
  than buried in a derivation.
- **New row in the Φ table for the singular set of ∇²Φ**, with the count made
  explicit: four independent arrivals (S3 divergences, S27 null spaces,
  Goldstone flat directions, S7's slow mode) by four unrelated routes.
- **§6 reprioritized.** The old #1 (real cross-domain transfer) is demoted from
  P0 — three passes made the frame load-bearing. The new #1 is the **unworked
  backlog**: 17 stones have never had a restraint pass, and they are where a
  quiet counterexample would sit precisely because they weren't chosen for
  being interesting. Added: sort every catalog entry into a floor and see what
  refuses.
- **§7** names the pattern the last two sessions showed: the restraint passes
  have been more generative than the expansions — the tower arrived via three
  stones dying usefully — with the matching warning that an architecture that
  moved twice in a week is not yet one to trust.

## Open

- Cheapest next restraint targets unchanged: **S5** (three thresholds), **S22**
  (ladder as RG scale).
- The floor-sort of §6.2 is now the sharpest structural test of the tower, and
  it is cheap: it needs a pass over `invariants/`, not an experiment.
- `invariants/feedback-control.md` still awaiting promotion from seed (flagged
  2026-07-22, not done today).
