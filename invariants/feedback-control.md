# Feedback, homeostasis & control

> **One-line claim:** Negative feedback stabilizes and positive feedback amplifies,
> and the same control-theoretic structure governs regulation across engineered,
> biological, economic, and computational systems.
> **Headline correspondence level:** L2–L3 (shared control equations; sometimes
> shared mechanism). *(provisional — seed)*
> **Status:** seed
> **Floor:** **2 + 3** — splits (derived, [S25(K)](../derivations/S25-control-split.md)): inference half floor 2, binary reachability floor 3

## Statement

A controlled system compares an output to a setpoint and acts on the error.
Negative feedback (error-correcting) → stability, homeostasis; positive feedback
(error-amplifying) → runaway, switches, network effects. The domain-neutral object
is the feedback loop / transfer function and its stability criterion.

## Manifestations by domain (seed)

- Engineering: PID controllers, thermostats — L3 (same equations, designed in).
- Biology: homeostasis (glucose, temperature), gene regulation — L3.
- Economics: automatic stabilizers, central-bank rules (Taylor rule) — L2.
- Ecology: predator–prey oscillations (Lotka–Volterra) — L2/L3.
- ML: no direct analogue for feedback control, but see RL / control duality.

## To develop

Copy structure from a full entry (e.g. `diffusion-random-walks.md`). Key questions:
does the *stability criterion* (loop gain, phase margin) transfer quantitatively?
Where is it L3 (same mechanism) vs. L2 (borrowed equations)? See Cybernetics
(Wiener 1948), control theory. Boundary: delays and nonlinearity break linear
stability results.
