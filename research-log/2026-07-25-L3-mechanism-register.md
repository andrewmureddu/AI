# 2026-07-25 — Expansion: the L3 mechanism register (M1–M17)

**Worked on:** the L3 rung generally; the periphery (connectivity), the symmetry
floor, and the power-law mechanism partition.
**Change:** new register [`questions/L3-MECHANISMS.md`](../questions/L3-MECHANISMS.md);
pointers added from `README.md` and `SPECULATIVE.md`. No level or status changes
to any existing entry.

## What I did

An expansion stroke, deliberately scoped to a unit the repo did not have. The
[stones](../questions/SPECULATIVE.md) are *questions* ("are these the same
object?"). What L3 actually requires is a **named generative process**, and the
repo had been carrying those implicitly — `power-laws.md` names four mechanism
families in prose and tests none of them; `networks-percolation.md` is a seed
with no mechanism; the symmetry floor established in
[`symmetry-sector.md`](../derivations/symmetry-sector.md) has a result and no
mechanisms at all.

So: seventeen candidate mechanisms, grouped by which floor of the tower they
probe, each with a five-part admission test.

## What I found

**The admission test is the content, not the list.** The five conditions —
named process, role assignment, parameter transfer, convergence discriminator,
intervention — are just the methodology's L3 bar written operationally, but
writing them out sharpens one thing considerably. The L2/L3 line in practice is
*whether the signature is fitted or predicted*: L2 fits the pattern, L3 predicts
it from mechanism parameters measured somewhere the pattern is not. And the
discriminator has to be an **off-pattern observable**, because identity and
convergence are by construction indistinguishable in the pattern itself. M12
(CTRW vs fractional Brownian motion — identical MSD exponent, separated only by
ergodicity) is kept in the register mainly as the standard case of this.

**The distribution of candidates is a finding about the map.** Eleven of the
seventeen sit at Φ's boundary or below it. That is not a sampling choice; it is
where mechanisms are missing. Every confirmed L3 in the
[ledger](../SYNTHESIS.md) — S1, S23, S7, S25a — is a face of the hub, so the
tower's completeness has never been tested by a mechanism selected from outside
it. The register is built to make either outcome informative: survivors are
non-Φ L3s, uniform reduction is a much stronger monism claim than the collapse
argument has produced, and deaths are L1/L2 demotions of correspondences that
currently circulate as mechanism.

**Three entries attach to existing unrun work and sharpen its instrument:**

- **M15 (adiabatic invariance)** re-reads [S26](../experiments/S28-sgd-charges/)'s
  "prethermalization plateau" as an averaging-theorem claim, testable by
  sweeping the learning rate: does charge erosion scale as a power of lr or as
  exp(−c/lr)? Existing code, one sweep, and it converts a phenomenological label
  into a mechanism with a number. Best effort-to-information ratio on the list.
- **M10 (TUR)** replaces S15's fluctuation–dissipation framing with the correct
  out-of-equilibrium instrument. FDT is an equilibrium identity whose failure
  gets absorbed by a fitted effective temperature; the thermodynamic uncertainty
  relation is an inequality and cannot be fitted away.
- **M2 (critical branching)** gives [Q2](../questions/OPEN-QUESTIONS.md) a
  stronger test than exponent comparison: the exponent *relation* plus avalanche
  shape collapse. Mean-field exponents are generic, so agreement on τ ≈ 3/2 is
  weak evidence — which is exactly the failure mode Q2 was written to catch.

**M3 (Molloy–Reed + degree-preserving rewiring)** is essay 04's falsifier 1,
which the essay names and nobody has run. Rewiring holds the degree histogram —
the exponential-family sufficient statistic, i.e. all Φ can see — fixed while
moving p_c. It is the sharpest cheap probe of whether connectivity is really
Φ's boundary layer.

**M11 (stochastic resetting)** is the one candidate for a genuine second axis
that is *not* symmetry. First-passage structure is not obviously a Φ-derivative,
and the CV > 1 criterion is parameter-free and does predictive work in CS
(Luby restarts), biochemistry (Michaelis–Menten), and search. Since S25 collapsed
connectivity into Φ's boundary, this is the first fresh candidate for an
irreducible direction.

## Decisions

- Numbered `M#`, not `S#`. **Bookkeeping flag:** the stones already use **S25
  and S26 twice each** (Cluster J and Cluster K), so `S#` is no longer a unique
  key across `SPECULATIVE.md`. Flagged, not renumbered — renumbering rewrites
  cross-references in six files and should be its own deliberate change.
- Register entries carry no ladder level. They are *candidates for* L3; a level
  would be the conclusion of the work, not its filing.
- One added working rule: **register the discriminator's expected value before
  measuring it.** A discriminator chosen after seeing the data is a fit. This is
  the pre-registration discipline S25 already learned the hard way (the parity
  channel declared blind, true only at odd site counts).

## Next

Priority order, with the first concrete step in each:
1. **M15** — lr sweep on the existing S26 script; fit erosion vs lr.
2. **M11** — one script, three domains, one CV criterion.
3. **M3** — rewiring at fixed degree sequence; predicted vs measured p_c shift.
4. **M8** — reward tail index → best-of-n growth curve.
5. **M10** — construct σ from SGD's stationary current; check the bound.

Unrelated but noted while reading: `SYNTHESIS.md` is still the 2026-07-19
snapshot and predates the tower architecture, the prethermalization plateau, and
the fourth ∇²Φ arrival. The 07-22 log entry already flagged this; it remains
pending and is not addressed here.
