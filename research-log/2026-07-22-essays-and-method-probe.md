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

## Addendum (same day) — S25 run

[`derivations/S25-control-split.md`](../derivations/S25-control-split.md):
attacked the "irreducible" reachability half as the stone instructed, and it
reduced. Controllability Gramian ≡ covariance of the noise-driven ensemble
(∇²Φ); minimum control energy = large-deviations rate function (Legendre dual
of Φ; exact linear-Gaussian, Freidlin–Wentzell small-noise beyond). Predictive
work: Gramian eigenvalue → 0 forecasts controllability loss (balanced
truncation already exploits this). But all *binary* reachability facts landed
in Φ's singular set (supports, null Fisher, I = ∞), never its regular part.

**Stone retired as stated; replacement claim: connectivity facts are
Φ-boundary facts.** The periphery split's geometry corrected: two layers
(regular Φ = prediction; singular Φ = connectivity, power laws,
percolation-via-Potts) plus at most one true second axis — invariance/
symmetry. Percolation's q→1 non-analyticity re-read from "dressing" to
systematic. Queued: spectral gap as Φ-degeneracy (gap-closing = critical
slowing down from the connectivity side); the symmetry-sector question is now
the map's sharpest open problem. Restraint notes placed in S25 and essay 4;
feedback-control entry flagged for promotion from seed.

## Second addendum (same day) — the symmetry sector

[`derivations/symmetry-sector.md`](../derivations/symmetry-sector.md): ran the
question S25 left open. **Monism fails, but so does "second sector."**

- Symmetry-*breaking* reduces to Φ-singular, fully: no SSB without a
  non-analyticity of Φ (finite-N Gibbs measures keep the full symmetry;
  Lee–Yang); Goldstone modes = null directions of ∇²Φ — third independent
  arrival at the same signature class (after S3's divergences and S25's
  unreachable null spaces).
- Noether proper does **not** reduce (structural obstruction: Noether needs a
  bracket, Φ has only a measure) — but inverts: a quantity can be a natural
  parameter of an invariant ensemble iff conserved, and long-time ensembles
  are parameterized by nothing but their charges (Gibbs / GGE, Jaynes read in
  reverse). Symmetry *constitutes* Φ's coordinates rather than reducing to Φ.
- Architecture correction: **one tower, three floors** — symmetry chooses the
  coordinates; Φ-regular predicts; Φ-singular ends prediction. Slogan
  candidate for the next synthesis pass: "one object, three floors: chosen by
  symmetry, read by prediction, ended by breakdown."
- Bookkeeping: S26 filed (charges = sufficient statistics of stationary
  prediction fields; three-sided falsifier, side (iii) runnable: SGD
  stationary-sufficiency on Kunin invariants). S9 sharpened to L2-with-L3-
  route (momentum maps over symplectic vs. metric structure). Echo noted:
  S1's cycling boundary is Hamiltonian and conserves a KL — the base layer
  showing through at the prediction layer's edge.

**SYNTHESIS.md is now materially out of date** (through-line changed twice
today: three sectors → two layers → tower). Needs a refresh pass as its own
piece of work, not a drive-by edit.

## Third addendum (same day) — two experiments: S26(iii) and S7

Unworked-stone audit: S2, S4–S8, S10–S17, S19–S22, S24 had never had a
restraint pass. Ran two that today's tower made most informative.

**S26(iii)** ([`experiments/S26-sgd-charges/`](../experiments/S26-sgd-charges/)):
falsifier did not fire, and the structure is better than the claim. Minimal
scale-symmetric model: charge conserved in the flow limit (drift ∝ lr);
weight-decay breaking follows dQ/dt = −4λQ to 1e-5 (the broken law is a law);
stationary norm predicted from the charge alone to 3e-4; charge erosion
5.6e-7/step ⇒ ~1.8M-step quasi-conservation window. SGD's stationary law is a
**prethermalization plateau coordinatized by quasi-charges** — GGE
phenomenology transferring with its known failure mode intact.

**S7** ([`experiments/S7-critical-slowing/`](../experiments/S7-critical-slowing/)):
split verdict, and a middle-zone reduction confirmed. τ·λ_min = 0.94±0.13
across saddle-node / mean-field Ising / GD at the MP edge — one mechanism
(curvature softening), L3 on-model. Universal-exponent reading retired to L1
(−½/−1/−2 by domain). Critical slowing down = Φ's Hessian going soft: fourth
independent arrival at the ∇²Φ singular-set object (S3 divergence, S25 null
spaces, Goldstone flat directions, now the slow mode). Boundary observed on
schedule: quartic dominance nearest T_c degrades the linear law.

Still unworked: S2, S4–S6, S8, S10–S17, S19–S22, S24. Cheapest next: S5
(three thresholds), S22 (ladder as RG scale). SYNTHESIS refresh still pending
— today added: tower architecture, prethermalization plateau, fourth ∇²Φ
arrival.
