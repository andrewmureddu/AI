# Candidate L3 mechanisms — the mechanism register

An expansion-stroke register, and a **different unit of work** from
[`SPECULATIVE.md`](./SPECULATIVE.md). A stone there is a *question* ("are these
two things the same object?"). An entry here is a **named generative process**
proposed to run identically in two or more domains — the thing
[`METHODOLOGY.md`](../METHODOLOGY.md) requires before anything is allowed onto
L3.

The reason to keep the register separately is the ladder's own asymmetry. L2 is
a claim about a *pattern* (same equation, same distribution), so you can check
it by looking at the pattern. L3 is a claim about a *process*, and processes are
mostly invisible in the pattern they produce — [power
laws](../invariants/power-laws.md) already record the canonical case: one shape,
at least four unrelated generators. So an L3 candidate has to be stated as a
rule you could run, and it has to come with an observable that is **not** the
pattern — otherwise identity and convergence are indistinguishable and the
entry cannot be graded.

---

## The admission test

An entry earns a place here only if all five are answerable. Where one is
missing, it is marked ✗ in the entry.

1. **Named process.** Stated as a rule or dynamics, not a pattern or an
   attitude. "Preferential attachment" passes; "self-organization" does not.
2. **Role assignment.** For each domain, what plays each variable in the rule.
3. **Parameter transfer.** The mechanism's parameters are measurable
   *independently of the pattern*, and predict the pattern's quantitative
   signature without fitting it. This is the L2/L3 line in operational form:
   L2 fits the signature, L3 predicts it from mechanism parameters measured
   elsewhere.
4. **Convergence discriminator.** An observable that differs between "same
   mechanism" and "different mechanism, same shape." Almost always an
   *off-pattern* quantity: a kernel, a shape collapse, an ergodicity test, a
   sign flip under intervention.
5. **Intervention.** Perturbing the mechanism moves both domains the predicted
   way (the [methodology](../METHODOLOGY.md)'s mechanism check).

Tiers follow [`SPECULATIVE.md`](./SPECULATIVE.md): 🟢 the mechanism is real and
published in ≥2 domains — the open question is whether it is *the same one*;
🟡 genuine formal resemblance, identity unproven; 🔴 a hunch filed to be killed.

Numbering is `M#` to stay clear of the `S#` stones. (Bookkeeping note: the
stones currently use **S25 and S26 twice each** — Cluster J and Cluster K — so
`S#` is no longer a unique key. Not renumbered here.)

---

## The register at a glance

| # | Mechanism | Tier | Tower floor it probes | Discriminator | Cost |
|--:|-----------|:----:|----------------------|---------------|------|
| [M1](#m1--preferential-attachment-) | Preferential attachment | 🟢 | Φ-boundary (tails) | measured attachment kernel Π(k) | data-bound |
| [M2](#m2--critical-branching--soc-) | Critical branching / SOC | 🟢 | Φ-boundary (criticality) | avalanche shape collapse + exponent relation | cheap sim |
| [M3](#m3--molloyreed-giant-component-) | Molloy–Reed giant component | 🟢 | Φ-boundary (connectivity) | degree-preserving rewiring | **cheap** |
| [M4](#m4--k-core--bootstrap-percolation-) | k-core / bootstrap percolation | 🟡 | Φ-boundary (connectivity) | hybrid transition: jump **and** β=½ | cheap sim |
| [M5](#m5--complex-contagion-) | Complex contagion | 🟡 | Φ-boundary (connectivity) | clustering **sign flip** | cheap sim |
| [M6](#m6--kesten-multiplicative-growth-) | Kesten multiplicative growth | 🟢 | Φ-boundary (tails) | E[A^α]=1 from shock data | **cheap** |
| [M7](#m7--neutral-drift--innovation-) | Neutral drift + innovation | 🟢 | Φ-regular | one θ must fit spectrum *and* turnover | cheap |
| [M8](#m8--extreme-value--weakest-link-) | Extreme value / weakest link | 🟢 | off-Φ (max-stable fixed point) | tail index → max-over-n curve | **cheap** |
| [M9](#m9--kinetic-proofreading-) | Kinetic proofreading | 🟡 | Φ-regular, driven | cost–speed–accuracy surface | mid |
| [M10](#m10--detailed-balance-breaking--tur-) | Detailed-balance breaking (TUR) | 🟡 | Φ-regular, driven | precision–dissipation inequality | cheap |
| [M11](#m11--stochastic-resetting-) | Stochastic resetting | 🟢 | off-tower candidate | CV > 1 criterion | **cheapest** |
| [M12](#m12--heavy-tailed-waiting-times-ctrw-) | Heavy-tailed waiting times (CTRW) | 🟡 | Φ-boundary (ergodicity) | weak ergodicity breaking | cheap |
| [M13](#m13--equivariant-bifurcation-) | Equivariant bifurcation | 🟢 | **symmetry floor** | isotropy-lattice inventory | mid |
| [M14](#m14--turing--scale-dependent-feedback-) | Turing / scale-dependent feedback | 🟡 | **symmetry floor** | predicted (not fitted) wavelength | mid |
| [M15](#m15--adiabatic-invariance-under-slow-drive-) | Adiabatic invariance | 🟡 | **symmetry floor** | drift scaling in ε | **cheap, reuses S26** |
| [M16](#m16--frustration--quenched-disorder-rsb-) | Frustration + quenched disorder | 🟡 | Φ-boundary (landscape) | overlap distribution P(q) | mid |
| [M17](#m17--record-dynamics--extremal-driving-) | Record dynamics | 🔴 | off-tower candidate | t/t_w aging collapse | cheap |

The distribution is itself a finding: **eleven of seventeen sit at Φ's boundary
or below it.** The prediction floor is where the confirmed L3s already are
(S1, S23, S7, S25a); mechanisms are what the *other* floors are missing.

---

## A — Connectivity mechanisms (Φ's boundary layer)

Per [`derivations/S25-control-split.md`](../derivations/S25-control-split.md),
connectivity facts land in Φ's singular set, not its regular part. These are the
processes that put them there.

### M1 — Preferential attachment 🟢

**Process.** A population grows by adding units; each new unit attaches to an
existing one with probability Π(k) ∝ k. Growth + linear attachment, nothing else.

**Roles.** Citation networks (Price 1976): units = papers, k = citations · WWW
(Barabási–Albert 1999): pages, in-links · species-per-genus (Yule 1925) · firm
and city sizes (Simon 1955, Gabaix 1999): k = size, "attachment" = growth
proportional to size · package/model-hub ecosystems: downloads, dependents.

**Parameter transfer.** γ = 3 for pure BA; γ = 2 + m₀/m with initial
attractiveness. The kernel *shape* sets the outcome class: sublinear Π ∝ k^α
(α<1) gives a stretched exponential, superlinear gives condensation onto a
single hub (Krapivsky–Redner 2000). So γ is a function of an independently
measurable object.

**Discriminator.** Measure Π(k) directly from time-resolved growth: for each new
link, histogram the target's degree against availability (Jeong–Néda–Barabási
2003). Identity requires matching kernels *and* γ matching the kernel's
prediction. A matching γ over a non-linear kernel is convergence.

**Falsifier.** A canonical "scale-free by preferential attachment" system whose
measured kernel is significantly sublinear while γ sits at the linear
prediction — the pattern is then made by something else.

**First test.** Two time-stamped growth datasets; kernel estimate + CSN tail fit.
Compute-cheap, data-bound. Formalizes a mechanism family already named in
[`power-laws.md`](../invariants/power-laws.md) but never tested here.

### M2 — Critical branching / SOC 🟢

**Process.** Slow external drive, fast threshold-triggered relaxation that
transports the driven quantity, dissipation only at boundaries. The steady state
self-tunes the branching ratio σ (descendants per event) to 1.

**Roles.** Sandpiles (BTW) · earthquakes (Olami–Feder–Christensen) · neuronal
avalanches (Beggs–Plenz 2003) · solar flares · forest fires.

**Parameter transfer.** σ = 1 is measurable directly from event cascades, before
any exponent is fit. Mean field then gives τ = 3/2 (size), α = 2 (duration).

**Discriminator.** Two off-pattern observables: (i) the **exponent relation**
(α−1)/(τ−1) = γ, where γ is the independently measured size–duration scaling;
(ii) **avalanche shape collapse** — average temporal profiles of avalanches of
duration T fall on one curve when rescaled by T^(γ−1) (Sethna–Dahmen–Myers 2001;
Friedman et al. 2012 for cortex). Exponent agreement alone is weak evidence
because mean-field values are generic.

**Falsifier.** τ ≈ 3/2 with the exponent relation violated or no shape collapse →
convergent look-alike, not the branching mechanism. Also: measured σ ≠ 1 in a
claimed SOC steady state.

**First test.** This is the right instrument for **[Q2](./OPEN-QUESTIONS.md)**,
which currently proposes comparing exponents — the weaker test. Cheap in
simulation; public avalanche datasets exist.

### M3 — Molloy–Reed giant component 🟢

**Process.** A local rule spreads independently across edges of a locally
tree-like graph. A giant component / epidemic exists iff the expected number of
*new* reached nodes per reached node exceeds 1, i.e. ⟨k²⟩/⟨k⟩ > 2.

**Roles.** Random graphs · epidemics (R₀) · polymer gelation
(Flory–Stockmayer) · infrastructure robustness under node removal · forest fires.

**Parameter transfer.** p_c = ⟨k⟩/(⟨k²⟩−⟨k⟩), predicted from two moments of the
degree distribution alone; β = 1 for the giant component's growth.

**Discriminator.** **Degree-preserving rewiring.** Rewiring holds the degree
histogram fixed — that histogram *is* the exponential-family sufficient
statistic, i.e. everything Φ can see — while changing clustering and degree
correlations, and it moves p_c. Identity requires the shift to be predicted by
the assortativity-corrected criterion.

**Why it matters here.** This is the sharpest available probe of whether
connectivity is genuinely Φ's boundary or a second axis, and it is *exactly*
[essay 04's falsifier 1](../essays/04-the-periphery-split.md), which names the
rewiring test and has never been run. The demand there is that a Φ-reduction do
**predictive work**: recover p_c-shifts under rewiring from Φ-derivatives alone.

**Falsifier.** Rewiring-induced p_c shifts recovered from Φ-derivatives (the
connectivity sector collapses into the hub), or shifts that neither Φ nor the
corrected Molloy–Reed criterion predicts (a third thing is at work).

**First test.** Pure numpy, hours. **Top-3 pick.**

### M4 — k-core / bootstrap percolation 🟡

**Process.** A node remains (or activates) only if at least k of its neighbours
do; iterate to a fixed point.

**Roles.** Jamming and rigidity in granular/glassy systems · k-SAT's frozen
variables · cascading failure in power grids and exposure networks · Watts
threshold contagion · **iterative magnitude pruning in networks**, whose update
has exactly this form.

**Parameter transfer.** k and the degree distribution predict the transition
point and the size of the surviving core.

**Discriminator.** The **hybrid transition**: a discontinuous jump *plus* a
square-root singularity, β = 1/2 above the jump (Dorogovtsev–Goltsev–Mendes
2006), together with the divergence of the "corona" (nodes with exactly k active
neighbours). The joint fingerprint is rare and hard to counterfeit.

**Falsifier.** A claimed k-core system with a continuous β = 1 transition —
ordinary percolation misidentified.

**First test.** Cheap simulation. Original leg worth running: does iterative
magnitude pruning show the jump-plus-√ signature at the lottery-ticket
threshold? If so, pruning collapse is a k-core transition, not a heuristic
cliff.

### M5 — Complex contagion 🟡

**Process.** Adoption requires ≥ θ *distinct* exposures rather than one.

**Roles.** Health behaviours, social movements, hashtag adoption (Centola–Macy
2007) · technology diffusion · financial contagion · 🔴 sub-hop: in-context
learning, where a behaviour may need multiple demonstrations to "take."

**Parameter transfer.** θ, measurable from individual-level adoption records,
predicts the direction and size of the clustering effect.

**Discriminator.** The **sign flip**: clustering and wide bridges *speed* complex
contagion and *slow* simple contagion; long-range ties help simple, hurt
complex. Run the spread on rewired graphs at matched degree, varied clustering,
and check the sign — an intervention, not a fit.

**Falsifier.** A documented complex contagion that spreads faster on a random
rewire than on the clustered original.

**First test.** Cheap. Pairs naturally with M3 (same rewiring machinery).

---

## B — Heavy tails off the critical path

The [power-law entry](../invariants/power-laws.md) says the shape partitions
into mechanism families; [Q1](./OPEN-QUESTIONS.md) asks whether the shapes
survive CSN model comparison. These two answer the next question — *which
generator* — and each makes a parameter-free numerical prediction.

### M6 — Kesten multiplicative growth 🟢

**Process.** X_{t+1} = A_t X_t + B_t with random multiplicative shocks A,
additive floor B (or a reflecting lower barrier), and E[log A] < 0.

**Roles.** Wealth (Levy–Solomon) · firm and city sizes · ARCH/GARCH volatility ·
products of random matrices · importance-sampling weights · activation and
weight tails under depth.

**Parameter transfer.** The tail exponent α solves **E[A^α] = 1** — computed
from the *shock* distribution, with no tail fitting whatsoever.

**Discriminator.** Measure the distribution of multiplicative shocks directly
(returns, growth rates, per-step gains), solve the Kesten equation, compare
predicted α against measured tail exponent. Two domains share the mechanism iff
both parameter-free predictions land. This is the cleanest test in the
heavy-tail zoo precisely because the prediction uses no information from the
tail.

**Falsifier.** A system with well-measured shocks whose Kesten α misses the
measured tail exponent outside CI → a different generator.

**First test.** Numerically trivial; the work is finding two domains with clean
shock data. Arms Q1 from the mechanism side: CSN says *whether* it's a power
law, Kesten says *why* and predicts the number.

### M7 — Neutral drift + innovation 🟢

**Process.** Fixed-size population; variants copied at random with **no fitness
differences**, innovation at rate μ; frequencies random-walk to fixation
(Moran / Wright–Fisher, infinite alleles).

**Roles.** Molecular evolution (Kimura) · ecology (Hubbell's neutral
biodiversity) · cultural transmission — first names, pottery motifs, dog breeds,
citations (Bentley et al. 2004) · plausibly model and method adoption in
research communities.

**Parameter transfer.** The **Ewens sampling formula** with a single parameter
θ = 2Nμ fixes the whole frequency spectrum, and separately predicts turnover —
the churn rate in a top-y list.

**Discriminator.** **One parameter, two observables.** Fit θ to the frequency
spectrum; predict the turnover rate; check. Neutrality tests (Ewens' allele-count
distribution, Tajima's-D-style statistics) transfer verbatim between domains.

**Falsifier.** A dataset where θ fitted from the spectrum mispredicts turnover —
reported for some name data, which is a boundary condition worth having.

**Why it matters here.** The catalog's cleanest available L3 with *nothing* to do
with Φ or with optimization: a null-model mechanism. It also pressures
[selection/replicator](../invariants/selection-replicator.md) from below — how
much apparent selection is drift?

### M8 — Extreme value / weakest link 🟢

**Process.** The observable is a max (or min) over many quasi-independent draws.
Max-stability forces one of three limit laws (Fisher–Tippett–Gnedenko) — an RG
fixed point of the *max* operation rather than the sum, which is why this sits
off Φ rather than under it.

**Roles.** Floods and records · material failure (weakest link → Weibull) ·
sporting records · tail risk · **best-of-n sampling** · max-pooling and top-k
routing.

**Parameter transfer.** The parent's tail fixes the domain of attraction and
therefore the growth of the max: Gumbel (exponential-ish tail) → E[max] ~ ln n;
Fréchet (tail index α) → ~ n^{1/α}; Weibull (bounded) → saturates. The
weakest-link **size effect** adds strength ∝ V^{−1/m} with the same m as the
Weibull shape parameter.

**Discriminator.** **Parameter transfer between two different observables.** Fit
the tail index on single draws; *predict* the max-over-n growth curve. Agreement
means the max is doing the work.

**AI-native leg 🟡.** Best-of-n reward gain should be an EVT curve whose shape
reveals the reward model's tail class — and the familiar
KL(best-of-n) = log n − (n−1)/n is the same computation from the other side. A
measured ln n gain says Gumbel; a power-law gain says the reward distribution is
heavy-tailed, which makes reward hacking a Fréchet statement with an exponent
rather than a vibe.

**Falsifier.** Measured tail index predicting the wrong max-over-n growth class.

**First test.** Very cheap on any sampled-reward data. **Top-5 pick.**

---

## C — Driven mechanisms (Φ's regular part, out of equilibrium)

### M9 — Kinetic proofreading 🟡

**Process.** Discrimination is amplified by an energy-consuming *irreversible*
discard branch off the binding pathway: the system re-tests from an
out-of-equilibrium intermediate, so equilibrium error ε becomes ε^(n+1) for n
proofreading steps, paid in free energy and in speed.

**Roles.** DNA replication · tRNA selection · T-cell receptor discrimination ·
🔴 speculative decoding, rejection sampling, and verifier-reranked generation —
an accept/reject branch fed by a cheap proposal.

**Parameter transfer.** The error exponent equals the number of irreversible
steps; the achievable cost–speed–accuracy surface is bounded (Murugan–Huse–
Leibler 2012).

**Discriminator.** Identity requires the same **cycle topology** — an
irreversible branch that consumes free energy and returns the system to its
start — not merely "checking twice." The test is the tradeoff surface: a genuine
proofreader trades accuracy against dissipation *and* throughput along a
specific curve, while an equilibrium two-step filter cannot beat ε at any speed.

**Falsifier.** A claimed proofreader improving accuracy without dissipation (an
equilibrium filter mislabelled), or an error exponent that doesn't count its
irreversible steps.

**Note.** Sharpens [S8](./SPECULATIVE.md) (universal thermodynamic cost of
computation) by giving it a specific cycle instead of a ratio, and
[`noise-thresholds.md`](../invariants/noise-thresholds.md) already gestures at
proofreading without naming the topology.

### M10 — Detailed-balance breaking (TUR) 🟡

**Process.** Any system holding a nonequilibrium steady state carries cyclic
probability currents, and the precision of any current-like output is bounded by
its entropy production: Var(J)/⟨J⟩² ≥ 2/σ (Barato–Seifert 2015).

**Roles.** Molecular motors · sensory adaptation in chemotaxis · circadian clocks
(the cost of a reliable period) · **SGD's stationary state**, known to break
detailed balance and cycle (Chaudhari–Soatto 2018).

**Parameter transfer.** A single inequality, no fitted parameters, linking a
measurable output variance to a measurable dissipation.

**Discriminator.** Identity requires the *same* inequality binding with the
*same* construction of entropy production. For SGD, build σ from the stationary
probability current and check; near-saturation would mean the learner is
thermodynamically efficient at its precision.

**Why it matters here.** This is the correct instrument for the repo's unrun
**[S15](./SPECULATIVE.md)** (FDT in learning). FDT is an *equilibrium* identity;
out of equilibrium it fails, and the fitted "effective temperature" absorbs the
failure. The TUR is an inequality — it cannot be fitted away.

**Falsifier.** A TUR violation in a system meeting its Markov assumptions (the
mechanism is not a Markov current), or a bound so loose it is vacuous at these
scales.

**First test.** Numpy-feasible on a small model; reuses
[S26](../experiments/S26-sgd-charges/) machinery.

### M11 — Stochastic resetting 🟢

**Process.** A search or first-passage process restarts from its initial
condition at rate r. Restarting truncates the heavy-tailed unlucky trajectories
that dominate the mean completion time.

**Roles.** Foraging and animal search · enzymatic turnover — Michaelis–Menten
*is* a resetting process (Reuveni–Urbakh–Klafter 2014) · RNA polymerase
backtracking recovery · **randomized restarts in SAT/CSP solvers**, where
heavy-tailed runtimes (Gomes–Selman–Kautz 1998) motivate Luby's universal restart
schedule · MCMC restarts · retry loops and best-of-n in agent systems.

**Parameter transfer.** The **CV criterion**: resetting reduces mean completion
time iff the coefficient of variation of the un-reset completion time exceeds 1
(Reuveni 2016; Pal–Reuveni 2017), and at the optimal rate CV = 1 exactly. Both
the *whether* and the *where* come from the un-reset distribution alone.

**Discriminator.** The criterion is parameter-free and cross-domain by
construction: measure the completion-time distribution in domain A, predict
whether restarting helps and by how much, verify. Identity holds iff the optimal
rate satisfies CV = 1 in each domain.

**Why it matters here.** It probes something the tower does not currently
answer. First-passage and completion structure are not obviously Φ-derivatives,
and the criterion does real predictive work. Either outcome is informative: a
Φ-expression is a win for the hub; a resistance makes this a candidate second
axis that is *not* symmetry — the first such candidate since S25 collapsed
connectivity into Φ's boundary.

**Falsifier.** A domain with CV > 1 (assumptions met) whose optimal restart rate
is 0.

**First test.** **Cheapest strong candidate on the list.** One numpy script can
run a diffusive search, a Michaelis–Menten cycle, and a backtracking SAT solver
through the same CV analysis. **Top-2 pick.**

> **⟳ Restraint pass (2026-07-25):** *run — the mechanism confirms, the framing
> above does not* — see
> [`../experiments/M11-stochastic-resetting/`](../experiments/M11-stochastic-resetting/).
> **The identity test passes.** At the optimal rate the restarted process has
> CV = 0.998 / 1.001 / 1.028 in diffusive search, enzymatic turnover and
> randomized backtracking — three processes with nothing in common (one with an
> *infinite* un-reset mean) landing on the same universal constant. The criterion
> predicts whether restarting helps (0/10 misclassified), where the optimum sits
> (diffusion: 2.62 vs the analytic 2.5396), and the entire restart curve from the
> un-reset distribution alone (≤2.9%) — including where ⟨T⟩ = ∞, because the
> Laplace transform exists when the moments do not. Two sign flips *within*
> single domains are the sharpest part: one enzyme scheme goes from "unbinding
> hurts" (multi-step, CV 0.50) to "unbinding helps 25×" (dynamic disorder,
> CV 1.71), and one search paradigm from no help (3-SAT, CV 0.73) to 19.4×
> (quasigroup-with-holes, CV 2.71).
> **But "candidate second axis" is retired.** The registered Φ-check was
> *vacuous* — Φ_T(−r) ≡ log T̃(r), so it verified algebra, not nature. The
> substantive fact is better: the exponential is the **maximum-entropy** law on
> [0,∞) at fixed mean and has CV exactly 1, so the criterion reads *restart helps
> iff the completion time is more dispersed than MaxEnt at the same mean.*
> First-passage structure is therefore not a new primitive — it is the hub's own
> log-partition form on a different **base variable** (an exit time, not a
> state). Consequence for the map: **what is portable is Φ's form, not Φ's
> variable**, and "does X reduce to Φ?" is under-specified until the base
> variable is named. Filed, not settled.
> **Scope:** restart is instantaneous and Poissonian throughout; all three
> domains are simulated. Three estimator failures were diagnosed en route (see
> the experiment README) — none changed a conclusion, all changed a verdict.

### M12 — Heavy-tailed waiting times (CTRW) 🟡

**Process.** Motion is jumps separated by waiting times drawn from
ψ(t) ~ t^−(1+α) with α < 1 (no mean) — traps of random depth.

**Roles.** Charge transport in amorphous semiconductors · intracellular
transport · human mobility and inter-event times · glassy relaxation · possibly
long plateaus in training curves.

**Parameter transfer.** MSD ~ t^α with the *same* α as the waiting-time exponent,
measured independently from dwell times.

**Discriminator.** **Weak ergodicity breaking** — time averages stay random and
differ from ensemble averages, the time-averaged MSD is *linear* in lag while
the ensemble MSD is sublinear, and both age with t_w. This separates CTRW
subdiffusion from fractional-Brownian subdiffusion, which has an **identical**
MSD exponent and is ergodic.

**Why it is in the register.** It is the cleanest teaching case for rule 4: two
mechanisms with the same L2 signature (t^α) separated entirely by an off-pattern
observable. Use it as the standard against which the other discriminators are
judged.

**Falsifier.** Ergodic time-averages with α < 1 → fBm, not CTRW.

---

## D — Symmetry-floor mechanisms

[`derivations/symmetry-sector.md`](../derivations/symmetry-sector.md) put
symmetry *under* Φ — it chooses the coordinates. That floor currently holds one
result and no mechanisms. These three live there.

### M13 — Equivariant bifurcation 🟢

**Process.** As a parameter crosses a stability threshold, the dynamics on the
center manifold reduce to a normal form dictated by the system's symmetry group;
the **equivariant branching lemma** says the branches that appear are those with
axial isotropy subgroups. The symmetry group, not the microscopic detail,
selects the inventory.

**Roles.** Convection patterns · lasers · buckling · **animal gaits** — the
symmetry of the CPG network predicts which gaits exist and the order of
transitions (Golubitsky–Stewart–Buono–Collins 1998) · visual hallucination form
constants (Bressloff–Cowan) · order parameters at phase transitions.

**Parameter transfer.** β = 1/2 at a pitchfork, but the real content is
**combinatorial**: the number, symmetry type, and stability ordering of emerging
states, read off the isotropy lattice before any simulation.

**Discriminator.** A combinatorial prediction is far harder to counterfeit than
an exponent. Identity holds iff the *same* isotropy lattice predicts *both*
domains' observed inventory of patterns and their transition order.

**Falsifier.** A symmetric system whose pattern inventory at onset contains
non-axial states, or omits predicted axial ones, with no imperfection to blame.

**First test.** A symmetric CPG ODE network — verify the gait inventory — then
the interesting leg: does a network with a known weight-space symmetry show the
*same* branch inventory at its own instability? That would put a mechanism on
the symmetry floor rather than a correspondence.

### M14 — Turing / scale-dependent feedback 🟡

**Process.** Local self-activation plus longer-ranged inhibition destabilizes
the homogeneous state over a band of wavenumbers, selecting a wavelength.
Requires the inhibitor's transport to substantially outrange the activator's.

**Roles.** Chemistry (CIMA, BZ) · digit patterning (Raspopovic et al. 2014) ·
**dryland vegetation stripes**, where the "diffusion" is advective water
redistribution (Klausmeier; Rietkerk) · pigment patterns · predator–prey spatial
structure.

**Parameter transfer.** The dispersion relation predicts the wavelength from
independently measured transport constants and kinetics.

**Discriminator.** Measure the two transport constants and the kinetics
independently, then **predict** the wavelength rather than fitting it. The
vegetation case is the sharp one precisely because its transport is hydrological,
not molecular: if the same dispersion relation with measured hydrology gets the
observed stripe spacing, that is mechanism identity across chemistry and ecology.
Post-hoc wavelength fits are convergence.

**Falsifier.** A canonical Turing pattern whose measured transport ratio is ≈ 1
(so the instability is mechanical or otherwise non-Turing), or a
predicted-vs-observed wavelength mismatch beyond uncertainty.

**Cost.** Mid — literature parameter-gathering dominates the work.

### M15 — Adiabatic invariance under slow drive 🟡

**Process.** With a fast near-periodic (or fast-mixing) motion and a slowly
varying parameter, ratio ε, the action variables of the fast motion are
conserved to high order. Drift is bounded by an averaging theorem, can be
exponentially small in 1/ε, and fails abruptly at resonance crossings.

**Roles.** Classical mechanics and plasma confinement · the quantum adiabatic
theorem · **prethermalization in near-integrable systems** · slow–fast ecology
and climate · **SGD's quasi-conserved charges** — this repo's own
[S26 result](../experiments/S26-sgd-charges/): erosion 5.6e-7/step, a
~1.8M-step conservation window, described there as a "prethermalization
plateau."

**Parameter transfer.** The **scaling of the drift rate in ε** — power-law
(ordinary averaging) versus exponentially small (Neishtadt/Nekhoroshev regime) —
plus the resonance-crossing failure mode.

**Discriminator.** Measure the scaling by varying ε. In S26's setup ε *is* the
learning rate: re-run the charge-erosion measurement across a decade of learning
rates and test whether erosion scales as a power of lr or as exp(−c/lr). That
single sweep converts "prethermalization plateau" from a phenomenological label
into a mechanism claim with a number, and it says which averaging regime the
learner is in.

**Falsifier.** An erosion rate independent of ε, or one matching neither scaling
form.

**First test.** **Existing S26 code plus a sweep — the best
information-per-effort ratio on the list. Top-1 pick.**

> **⟳ Restraint pass (2026-07-25):** *run — the ML leg confirms the mechanism* —
> see [`../experiments/M15-adiabatic-charges/`](../experiments/M15-adiabatic-charges/).
> The averaging structure is exact, not approximate: the symmetry generator is
> orthogonal to the *stochastic* gradient for every noise realization, so the
> first-order term vanishes identically and the drift is purely second order
> (verified to 1.6e-16 scalar, 1.0e-15 in a wide two-layer net). Registered
> scaling confirmed: k ∝ η^2.021 σ^1.999 B^−1.003, with the parameter-free
> absolute rate k = η²σ²E[x²]/B good to 2% across 18 grid points. **The
> discriminator answers "ordinary averaging"**: the power law beats the
> Nekhoroshev form exp(−c/η) by ΔAIC = 73.6 — the plateau is long because η is
> small, not because anything protects it, which is the expected consequence of
> a *stochastic, broadband* perturbation. Breakdown (registered as exploratory)
> is the sharpest secondary result: coordinatization degrades as
> suff_err = 1.12·R^−0.97 in the timescale-separation ratio R, reaching unity at
> **R = 1.13** — O(1), where an adiabatic argument says it must.
> Two honest marks on the record: (a) the pre-registered wide-net estimator
> **failed** (p = 1.64) and was diagnosed rather than swapped — it measured
> displacement, not rate, and saturated (displacement-vs-window slope 0.39
> instead of 1), because in the wide net ΔQ_j can be *positive* and charges
> relax to an alignment-dependent quasi-equilibrium rather than to zero; the
> corrected observable (relaxation time) gives τ ∝ η^−2.038 at R² = 0.99994.
> (b) S26's erosion rate is corrected from 5.6e-7 to **7.30e-7/step** (window
> 1.37M, not 1.8M) — its estimator mixed in the burn-in.
> **Scope:** this establishes the mechanism's fingerprint in the ML instance
> only. The cross-domain identity claim — same averaging mechanism as plasma
> confinement, the quantum adiabatic theorem, near-integrable prethermalization
> — is untouched and is what a second leg would have to test.

---

## E — Landscape and search mechanisms

### M16 — Frustration + quenched disorder (RSB) 🟡

**Process.** Competing constraints that cannot be simultaneously satisfied, with
disorder frozen on the dynamics' timescale; the solution space fragments into
exponentially many clusters separated by extensive barriers.

**Roles.** Spin glasses · random k-SAT and CSPs — the clustering/condensation
transition (Krzakala et al. 2007) · protein folding (funnel vs glass) ·
combinatorial optimization · **neural network loss landscapes**.

**Parameter transfer.** The clustering threshold is predicted from the constraint
density, and algorithmic hardness is predicted to onset there — *before* the
satisfiability threshold.

**Discriminator.** The **overlap distribution P(q)**: trivial (single delta) in
the replica-symmetric phase, multi-peaked or continuous under 1RSB/full RSB.
Identity requires the same qualitative RSB structure at the corresponding point
— a structural match, not an exponent match.

**Connection.** This is the mechanism *behind* [S6](./SPECULATIVE.md) (SAT
hardness ↔ physical transition); naming it converts S6 from "is this a
coincidence?" into a mechanism-identity test. It also gives S3/S25's singular
*geometry* a landscape-side counterpart: measure P(q) across SGD solutions from
different seeds, alongside λ̂.

**Falsifier.** A hardness peak with trivial P(q), or clustering with no hardness
onset.

**First test.** Mid overall; the ML leg (P(q) across seeds) is cheap and, as far
as I know, rarely measured next to a learning-coefficient estimate.

### M17 — Record dynamics / extremal driving 🔴

**Process.** Evolution is punctuated: nothing happens until a *record*
fluctuation occurs; the extremal element is then replaced and the local
configuration resets. Because records in a stationary series occur at times ~ ln
t, activity is Poisson in **log** time.

**Roles.** Punctuated equilibrium (Bak–Sneppen) · spin-glass and colloidal aging ·
crackling in disordered materials · evolutionary computation and hill climbing ·
**learning plateaus and grokking**.

**Parameter transfer.** Log-Poisson event statistics: event count ∝ ln t, waiting
times ∝ 1/t — no fitted exponent.

**Discriminator.** **Aging collapse**: two-time correlations depend on t/t_w
rather than t − t_w. This fails for ordinary stationary dynamics and for simple
exponential relaxation, so it is a strong test that costs nothing to run.

**Why 🔴.** The ML leg is a hunch. But it is a cheap one, and it would give the
repo's grokking thread ([S19](./SPECULATIVE.md); S26's call for "plateau-rich
tasks") a *mechanism* hypothesis rather than a description: if plateau escapes
are log-Poisson and learning curves age on t/t_w, grokking is record dynamics
and the plateau is a waiting-time law, not a mystery.

**Falsifier.** Plateau-escape times exponentially rather than 1/t distributed, or
correlations collapsing on t − t_w.

---

## What to run first

Ranked by (what it moves on the map) × (cheapness), with the first concrete step:

1. ~~**M15 adiabatic invariance**~~ — **done 2026-07-25**, see
   [`experiments/M15-adiabatic-charges/`](../experiments/M15-adiabatic-charges/).
   Ordinary averaging, exact first-order cancellation, breakdown at R ≈ 1. The
   ML leg only; a second domain is what would make it cross-domain.
2. ~~**M11 stochastic resetting**~~ — **done 2026-07-25**, see
   [`experiments/M11-stochastic-resetting/`](../experiments/M11-stochastic-resetting/).
   Identity test passed (CV → 1 at the optimum in all three domains); the
   "second axis" framing retired — it is Φ's form on a different base variable.
3. **M3 Molloy–Reed + rewiring** — runs
   [essay 04's falsifier 1](../essays/04-the-periphery-split.md) with the
   predictive-work condition it demands. Settles whether connectivity is Φ's
   boundary or something else.
4. **M8 extreme value / best-of-n** — fit a reward tail index, predict the
   max-over-n curve. Cheapest AI-native parameter transfer available.
5. **M10 TUR in learning** — the unrun S15 with the right instrument (an
   inequality instead of a fitted effective temperature).
6. **M6 Kesten** — arms [Q1](./OPEN-QUESTIONS.md) from the mechanism side:
   predict the tail exponent from shock data with zero tail fitting.

## What would make the register earn its keep

The register is built so that either outcome is informative, which is the only
honest way to file seventeen guesses at once:

- **If several survive their discriminators**, the catalog gains L3 entries that
  are *not* Φ-facets. Every confirmed L3 in the [ledger](../SYNTHESIS.md) today
  (S1, S23, S7, S25a) is a face of the hub, so the tower's completeness has never
  actually been tested by a mechanism from outside it.
- **If they all reduce to Φ**, that is a far stronger monism result than the
  collapse argument has produced so far — because these were selected to sit at
  the boundary and below it, not chosen for reducibility.
- **If they die on their discriminators** — same shape, different generator —
  each death is a mapped L1/L2 demotion of a correspondence that currently
  circulates as mechanism, which is the [methodology](../METHODOLOGY.md)'s stated
  reason for keeping the dead.

## How to work an entry

Same as a stone, with one addition: **write down the discriminator's expected
value before measuring it.** A discriminator chosen after seeing the data is a
fit. If an entry survives, its mechanism gets a proper file in
[`../invariants/`](../invariants/) and the domains it links get their cells
updated in [`../domains/README.md`](../domains/README.md); if it dies, the
correspondence it was supposed to support drops a level and the entry keeps its
⟳ restraint note here.
