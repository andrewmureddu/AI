# Speculative bridges — the AI-native question set

A separate, deliberately looser tier from [`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md).
Those are P0-rigorous cleanups. These are **speculative stepping stones**: hops
that lean on non-obvious formal bridges between distant fields, taken to map the
terrain rather than to prove a point.

## What "a question only an AI could ask" actually means

Not mystical insight. The concrete edge is this: the same mathematical object
recurs across fields under *different names*, and a specialist in field A usually
doesn't recognize it in field B because they never learned B's vocabulary. Holding
many formalisms at once makes those collisions visible. So the AI-native move is
**organize by the shared object, not by the domain** — and then ask what travels.

That edge cuts both ways: breadth makes it trivially easy to generate
impressive-sounding fake unifications (exactly the "universality inflation" the
[methodology](../METHODOLOGY.md) warns against). So every hop below is tagged:

- 🟢 **Established bridge** — the shared object is real, published math. The
  question is how *far* it travels, not whether it exists.
- 🟡 **Plausible** — a genuine formal resemblance; the identity is unproven and
  might be convergence, not identity.
- 🔴 **Wild** — a hunch worth recording precisely so we can try to kill it.

Each carries a **falsifier**: the concrete observation that would confirm or sink it.

---

## Cluster A — "Is there only one update rule?"

### S1 🟢 — Replicator = multiplicative weights = Bayes = Gibbs, one algorithm?
**Bridge:** entropic mirror descent / exponential-family update.
**Connects:** evolutionary biology · online learning (CS) · Bayesian inference ·
statistical mechanics.
Evolutionary **replicator dynamics**, the **multiplicative-weights** update,
**exponentiated gradient**, **Bayesian posterior updating**, and relaxation to the
**Boltzmann–Gibbs** distribution are all, in the right limit, mirror descent with
a KL/entropy regularizer. Question: is "adaptation" in *every* domain literally the
same descent on a free energy, with only the regularizer's geometry changing?
**Falsifier:** find an adaptive system whose update provably cannot be written as
mirror descent on *any* Bregman divergence — that bounds the invariant's reach.
(Promotes/kills the new entry [`mirror-descent-update.md`](../invariants/mirror-descent-update.md).)
> **⟳ Restraint pass (2026-07-19):** *derived and confirmed* — see
> [`../derivations/S1-universal-update.md`](../derivations/S1-universal-update.md).
> All four are `x_i ∝ x_i·exp(−η g_i)` with the loss and step size as the only
> free choices; the normalizer unifies as free energy = −log evidence = cumulative
> log-loss = −log-growth. **L3 for the local update + geometry.** Sharp boundary
> found: *global* dynamics are not shared (fixed loss concentrates; game-coupled
> loss cycles — Poincaré recurrence), so "they converge alike" is retired to L1.
> S2's shared η (learning rate = temperature = selection) falls out. Object
> promoted to `developing`.

### S2 🟡 — Is a "learning rate" the same object as a "temperature" and a "mutation rate"?
**Bridge:** the coefficient on the entropy term in S1.
**Connects:** ML · thermodynamics · population genetics.
If S1 holds, the step size (ML), temperature (physics), and mutation/selection
ratio (biology) are the *same* knob — the weight on exploration vs. exploitation.
Question: do the well-known *phase transitions in that knob* (learning-rate
"edge of stability," the melting temperature, Eigen's error threshold) map to each
other quantitatively? **Falsifier:** the critical values, once nondimensionalized,
don't line up across two of the three domains.

---

## Cluster B — "Is there only one geometry?"

### S3 🟢 — Fisher = Ruppeiner = Fubini–Study: does statistical curvature mark every phase transition?
**Bridge:** the Fisher information metric and its scalar curvature.
**Connects:** statistics/ML (natural gradient) · thermodynamics (Ruppeiner metric)
· quantum mechanics (Fubini–Study metric).
The same metric on a space of distributions appears as the natural-gradient metric
(ML), the thermodynamic metric whose **scalar curvature diverges at critical
points** (physics), and the quantum state metric (whose divergence flags quantum
phase transitions). Question: does statistical **curvature** flag "critical points"
in *learning trajectories, evolutionary fitness landscapes, and markets* the way it
does in thermodynamics — i.e., is curvature-blowup a universal early-warning of a
transition? **Falsifier:** train a model through a known grokking/phase transition
and show the Fisher curvature does *not* spike there.
> **⟳ Restraint pass (2026-07-19):** tested and *partially confirmed* — see
> [`../experiments/S3-fisher-geometry/`](../experiments/S3-fisher-geometry/). The
> Fisher signal spikes at both the Ising critical point (χ→∞ at T_c) *and* the
> double-descent interpolation threshold (inverse-Fisher blow-up coincides exactly
> with the test-error peak, P/N=1). Grokking specifically remains untested (needs
> torch); the full Riemann-curvature version remains open. Object promoted to
> `developing`: [`statistical-geometry.md`](../invariants/statistical-geometry.md).

### S4 🟢 — Is every "evolving distribution" a gradient flow in Wasserstein space?
**Bridge:** optimal transport; the JKO theorem (the heat equation *is* the gradient
flow of entropy in the Wasserstein metric).
**Connects:** PDE/diffusion (physics) · economics (Monge–Kantorovich matching) ·
generative ML (Wasserstein GANs, diffusion models) · developmental biology.
Question: are diffusion, price-equilibrium matching, GAN training, and
developmental trajectories all *the same* object — steepest descent of a free
energy in the geometry of distributions? If so, "how a population/price/pixel-
distribution/cell-fate moves" has one governing equation. **Falsifier:** a
domain instance whose dynamics are provably not a Wasserstein gradient flow of any
functional (e.g., genuinely non-gradient, curl-dominated flow).
(New entry [`optimal-transport.md`](../invariants/optimal-transport.md).)

---

## Cluster C — "Is there only one threshold?"

### S5 🟡 — Shannon capacity = Eigen's error catastrophe = the quantum fault-tolerance threshold?
**Bridge:** the noise level at which information stops being recoverable.
**Connects:** coding theory (CS) · molecular evolution (biology) · quantum
computing (physics).
Shannon's **channel capacity**, Eigen's **error catastrophe** (above a mutation
rate a genome's information dissolves), and the **fault-tolerance threshold
theorem** (below an error rate, arbitrarily long quantum computation is possible)
are all sharp "how much noise before the signal is lost" thresholds. Question: are
these one invariant — a redundancy-vs-noise transition — with a shared scaling of
required redundancy in the noise gap? **Falsifier:** the redundancy-vs-(threshold−p)
scaling exponents differ across the three. (New entry
[`noise-thresholds.md`](../invariants/noise-thresholds.md).)

### S6 🟢 — Is the SAT solvability transition the same phase transition as a physical one?
**Bridge:** the replica/cavity method; computational phase transitions.
**Connects:** CS (k-SAT, constraint satisfaction) · statistical physics (spin
glasses).
Already established that random k-SAT has a sharp satisfiability threshold analyzed
by spin-glass methods. Question (the AI-native extension): does the **hardness
peak** at the threshold correspond to **critical slowing down** — i.e., is
algorithmic hardness the computational face of a diverging relaxation time? Links
directly to S8. **Falsifier:** a solver whose runtime does *not* diverge at the
threshold despite the transition being present.

---

## Cluster D — "Is 'about to break' one signal?"

### S7 🟢 — Critical slowing down as a universal early-warning signal
**Bridge:** rising autocorrelation & variance as a system approaches a tipping point.
**Connects:** ecology & climate (regime shifts) · neuroscience (seizure onset) ·
finance (crashes) · physics (critical points) · CS (S6 hardness).
Critical slowing down is an *established* early-warning signal in ecosystems and
climate. Question: is the **same statistic** (lag-1 autocorrelation → 1, variance
blow-up) a domain-neutral predictor of *any* impending transition — and does it
work on training-loss curves before a model collapses or groks? **Falsifier:** a
well-characterized tipping point in one domain that arrives with *no* rise in
autocorrelation/variance. (New entry
[`critical-slowing-down.md`](../invariants/critical-slowing-down.md).)

---

## Cluster E — "Is there one price for a bit?"

### S8 🟡 — A universal thermodynamic cost of computation across brains, cells, and chips
**Bridge:** Landauer's bound (kT ln2 per erased bit) + thermodynamic length
(minimum dissipation).
**Connects:** physics/computation · neuroscience (metabolic cost of spikes) · cell
biology (proofreading energetics) · CS (chip energy).
Question: do brains (Attwell–Laughlin spike energetics), kinetic-proofreading
molecular machines, and processors sit at a *common multiple* of the Landauer
bound — is there an invariant "efficiency ratio" (actual / thermodynamic-minimum
cost) that biology and engineering both converge to? **Falsifier:** the ratios
differ by orders of magnitude with no shared explanation. (Cross-links
[`entropy-information.md`](../invariants/entropy-information.md).)

---

## Cluster F — Wild stones (recorded to be knocked down)

### S9 🟡 — A Noether theorem for learning
**Bridge:** symmetry → conserved quantity, applied to gradient-flow training.
**Connects:** physics (Noether) · ML (training dynamics).
There is real work showing that symmetries of a loss landscape induce **conserved
quantities in gradient-flow training** (analogous to Noether currents). Question:
is this the *same* theorem as physics' Noether, and does every invariance we build
into a model (translation, scale, permutation equivariance) leave a measurable
conserved quantity during training? Bridges
[`conservation-noether.md`](../invariants/conservation-noether.md) ↔
[`optimization-variational.md`](../invariants/optimization-variational.md).
**Falsifier:** a continuous loss symmetry with demonstrably no conserved quantity
under gradient flow.

### S10 🔴 — Is gauge symmetry just "redundancy of description," and does fixing it always cost something?
**Bridge:** gauge freedom / reparameterization invariance.
**Connects:** physics (gauge theory) · ML (over-parameterized weight-space
symmetries) · economics (utility defined only up to monotone transform) ·
measurement theory.
Question: is "gauge symmetry" a universal signature of *redundant coordinates*, and
does gauge-fixing have a universal pathology (the physics **Gribov ambiguity** ↔
optimization getting stuck in a bad coordinate patch ↔ index-number problems in
economics)? **Falsifier:** the redundancies are structurally different (e.g., one
is a Lie group, another isn't) with no shared consequence — likely demotes this to
L1 metaphor.

### S11 🔴 — Is criticality an *attractor of optimization*, not a coincidence?
**Bridge:** near-critical dynamics maximize dynamic range / information transmission
/ memory.
**Connects:** neuroscience (critical brain) · evolution · ML · economics.
Reframe: instead of asking "why do so many systems sit near a critical point?", ask
whether **any process that optimizes information-processing capacity is *driven*
toward criticality** — so selection, learning, and markets independently discover
the same edge. That would make criticality's recurrence a *consequence* of
optimization, unifying [`criticality-phase-transitions.md`](../invariants/criticality-phase-transitions.md)
with [`optimization-variational.md`](../invariants/optimization-variational.md).
**Falsifier:** an optimizing system that maximizes a capacity measure and provably
sits *away* from criticality.

### S12 🔴 — Predictive information as the single axis that "interesting" systems share
**Bridge:** excess entropy / predictive information (mutual information between past
and future).
**Connects:** linguistics · neural spike trains · financial series · music.
Question: do the time series humans find "meaningful" across every domain sit in a
narrow band of predictive-information scaling — neither periodic (too predictable)
nor random (unpredictable) — and is *that band* itself the invariant? **Falsifier:**
measure predictive-information scaling across domains and find no common band.

---

## Cluster G — Stones off the free-energy hub (added 2026-07-19)

These use the [free-energy hub](../invariants/free-energy-hub.md) Φ = ln Z: its
gradient (observables), Hessian (Fisher/fluctuations), and singularities.

### S13 🟡 — Is every phase transition a non-analyticity of the prediction field's free energy?
**Bridge:** Lee–Yang — a transition is a singularity of Φ = ln Z.
**Connects:** physics · CS (SAT) · ML (grokking, double descent) · reasoning.
Given the hub, is *every* sharp transition — thermodynamic, computational, learning
— a non-analyticity of the appropriate log-partition function (Lee–Yang zeros
pinching the real axis)? Double descent already fits: the inverse-Fisher = ∂²Φ that
blew up in [S3](../experiments/S3-fisher-geometry/) is exactly the hub's Hessian
diverging. **Falsifier:** a genuine transition whose free energy stays analytic.
**Tractable next step:** locate partition-function zeros for a small grokking model.

### S15 🟡 — Does the fluctuation–dissipation theorem hold in learning and markets?
**Bridge:** response = fluctuation, because both are ∂²Φ (the hub's Hessian).
**Connects:** physics · ML (SGD noise) · finance.
FDT: a system's linear response to a perturbation equals the autocorrelation of its
spontaneous fluctuations. Does a learner's response to a data/parameter perturbation
equal the covariance of its SGD fluctuations? Do market impact responses equal
fluctuation autocorrelations? **Out of equilibrium**, is the FDT-violation ratio —
an *effective temperature* — itself the invariant? **Falsifier:** measure both sides
in a trained model and find no relation even after fitting one effective temperature.

### S16 🔴 — Is there a universal speed limit on changing your predictions?
**Bridge:** information-geometric / thermodynamic speed limits (Fisher length ≥
distance ÷ time).
**Connects:** physics (thermalization) · ML (learning curves) · evolution.
The rate at which any system can move its distribution is bounded by its integrated
Fisher information (a "statistical speed"). Are learning speed, evolutionary rate,
and thermalization time all bounded by the *same* Fisher-length inequality?
**Falsifier:** a system that shifts its distribution faster than its integrated
Fisher information permits.

## Cluster H — Compression, symmetry, and what survives

### S14 🟡 — Renormalization = the information bottleneck = diffusion-model denoising?
**Bridge:** scale-by-scale compression that preserves predictive information.
**Connects:** physics (RG) · ML (info bottleneck, diffusion models) · neuro
(predictive coding).
RG keeps "relevant" operators and discards "irrelevant" ones; the IB keeps
predictive information and discards the rest; diffusion models and network depth
coarse-grain scale by scale. Are **RG-relevant = IB-predictive = coarse-to-fine-
preserved** the same partition of information? **Falsifier:** exhibit relevant-
operator content that is provably *not* the predictive-information content. Upgrades
[`emergence-renormalization.md`](../invariants/emergence-renormalization.md).

### S17 🔴 — Are flat minima (ML generalization) the same as gauge / Goldstone zero-modes (physics)?
**Bridge:** flat directions = symmetry orbits.
**Connects:** physics (gauge, Goldstone modes) · ML (flat minima).
Flat minima generalize; broken-symmetry zero-modes (Goldstone) are flat directions
with physical meaning. Is "generalization = living on a flat / gauge orbit" the same
statement as "physical observables are gauge-invariant"? **Falsifier:** flat minima
that correspond to no symmetry of the loss. (Sharpens S10.)

### S18 🟢 — Causation = invariance across environments = this project's own method, turned inward
**Bridge:** intervention-invariant prediction.
**Connects:** causal inference (Pearl do-calculus) · ML (invariant causal
prediction / IRM) · **the methodology of this repo itself**.
Modern ML *defines* causal mechanisms as precisely the relationships that stay
invariant across environments (Peters et al.'s ICP; Arjovsky's IRM). That is our
[cross-domain-invariant](../METHODOLOGY.md) criterion applied to one system's
environments: **causation is a prediction-field invariant under the group of
interventions.** So "map cross-domain invariants" and "find causal structure" are
the *same operation at different scopes* — the project is self-similar with its own
method. **Tier 🟢** because invariance⇒causation is already established; the open
part is whether the "same operation, different scope" reading yields a real transfer
(e.g., does ladder level predict causal robustness?). This is also the concrete
falsifier for the [prediction-field frame](../PREDICTION-FIELD.md). **Falsifier:** a
mechanism causally stable but *not* environment-invariant, or vice versa.
> **⟳ Restraint pass (2026-07-19):** *tested — falsifier survived* — see
> [`../experiments/S18-invariance-transfer/`](../experiments/S18-invariance-transfer/).
> In a linear SCM, coefficient instability measured on training environments ranks
> transfer error on a *held-out* environment at Spearman ρ = 0.985, and the most
> in-distribution-predictive (spurious) feature is the worst-transferring (8×). The
> prediction-field claim "invariance predicts transfer" holds and has teeth. Honest
> limit: invariance = causation *by construction* in the SCM; the real test is the
> same measurement on genuine catalog invariants across genuinely different domains.

---

## Cluster I — Learning is the thermodynamics of prediction (added 2026-07-19)

These use the [free-energy hub](../invariants/free-energy-hub.md), Landauer's bound,
and the Fisher spectrum. If the universal update descends −Φ, then *inefficient*
learning should dissipate, and the thing dissipated should be information.

### S20 🟡 — Is a learner's inefficiency exactly its non-predictive memory?
**Bridge:** Still–Sivak–Bell–Crooks "thermodynamics of prediction" — a driven
system's dissipation is bounded below by the *nonpredictive* information it retains
about its past.
**Connects:** stochastic thermodynamics · online learning (regret) · Bayesian
sufficiency.
Conjecture: every learner's excess loss / regret equals the information it keeps
about the training past that is *not* predictive of the future — "nostalgia" as
dissipation. A perfectly efficient learner retains only predictive information (a
sufficient statistic) and dissipates nothing. **Falsifier:** a maximally efficient
predictor that provably retains non-predictive information, or a dissipative one
that retains none. **Tractable next step:** a toy driven 2-state Markov model —
measure dissipation vs. retained-nonpredictive-info directly (numpy-feasible).

### S21 🟡 — Sloppiness = learnability = renormalizability (one Fisher-spectrum fact)
**Bridge:** the eigenvalue spectrum of the Fisher metric (= the hub's Hessian ∇²Φ)
spans many decades — a few "stiff" directions, many "sloppy" ones.
**Connects:** systems biology / physics ("sloppy models," Sethna) · statistical
learning (sample complexity) · renormalization (parameter-space compression).
Conjecture: a model is *learnable* from few samples, a theory is *renormalizable*,
and a system shows *emergent simplicity* for the **same** reason — the Fisher
spectrum is sloppy, so only a low-dimensional stiff subspace matters. Ladder level
may equal the number of stiff directions. **Falsifier:** a learnable model with a
flat (non-sloppy) Fisher spectrum, or a sloppy one that resists compression.
**Tractable next step:** compute Fisher eigenvalue spectra for a few small models
and correlate stiff-dimension count with sample complexity (numpy-feasible; ties to
[S3](../experiments/S3-fisher-geometry/)).

### S22 🟡 — The ladder is a renormalization scale
**Bridge:** coarse-graining keeps "relevant" operators and discards "irrelevant"
ones — exactly what climbing L2→L3→L4 does to spurious detail.
**Connects:** RG (physics) · causal abstraction (CS) · **this repo's own ladder**.
Conjecture: an invariant's ladder level = its *renormalization depth* — how many
layers of irrelevant/measurement-specific detail have been integrated out. L4
invariants are RG fixed points; L2 correspondences are irrelevant operators that
wash out under coarse-graining (which is *why* they don't transfer — see the
[transfer cliff](../experiments/ladder-vs-transfer/)). Self-referential like S18:
the methodology is itself an RG flow. **Falsifier:** an L4 invariant that is *not*
stable under coarse-graining, or an L2 one that is.

## Cluster J — The ladder as a dynamical process (climbing it is inference)

### S19 🟡 — Grokking is a climb up the ladder
**Bridge:** the memorization→generalization transition as an L2→L3 jump in the
learned representation.
**Connects:** ML (grokking) · the ladder · the [transfer cliff](../experiments/ladder-vs-transfer/).
Conjecture: grokking is the moment a model stops using L2 memorized correlations and
finds the L3 *mechanism* (the actual algorithm), which is exactly why generalization
appears *suddenly* — it's a discrete jump across the L2/L3 cliff, not a smooth ramp.
Unifies [S3](../experiments/S3-fisher-geometry/) (a transition), S13 (Lee–Yang),
and the ladder. **Falsifier:** a grokking event whose post-grok solution is *not*
more mechanism-invariant (across data subsets) than the pre-grok one. **Test:** needs
torch, but the invariance-across-subsets metric is cheap once a grokked model exists.

### S23 🟡 — Attention is the universal update (amortized Bayesian filtering)
**Bridge:** softmax attention = exp(scores)/Z — a Gibbs/Bayes reweighting, i.e. one
step of [entropic mirror descent](../invariants/mirror-descent-update.md).
**Connects:** transformers (ML) · Bayesian filtering · the universal update · the hub.
Conjecture: a transformer layer performs the *same* reweighting as Bayesian updating
over its key–value memories — the model does amortized inference at run time, and
"attention temperature" is the update's η (= inverse temperature). If so, in-context
learning is literally the universal update executed in the forward pass. **Falsifier:**
an attention mechanism not expressible as an entropic reweighting over a memory.
**Tractable next step:** show softmax attention and a Bayesian posterior over
Gaussian memories coincide numerically (numpy-feasible).

### S24 🔴 — The invariant is the minimal sufficient statistic (and the rest is Landauer-erasable)
**Bridge:** a minimal sufficient statistic keeps all predictive information and
discards the rest; the discarded remainder is erasable at Landauer cost.
**Connects:** statistics (sufficiency) · thermodynamics (Landauer) · our invariants ·
the info bottleneck.
Conjecture: a domain-pair's invariant *is* the minimal sufficient statistic of one
domain for predicting the other; everything non-invariant is thermodynamically
erasable, and the cost of erasing it is the "price" of abstraction. Ties sufficiency,
Landauer, and the [prediction-field](../PREDICTION-FIELD.md) frame. **Falsifier:** an
invariant that is provably *not* a minimal sufficient statistic of its domain-pair.

---

## How to work a speculative stone

1. Pick one. Restate it as a **quantitative** claim (an exponent, a ratio, a
   scaling — never just "they're similar").
2. Try hardest to **falsify** it via the listed test. A killed stone is a mapped
   stone — log it and mark the connection L1.
3. If it survives, it graduates to [`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md) with a
   real evidence plan, and its object gets a proper entry in
   [`../invariants/`](../invariants/).
