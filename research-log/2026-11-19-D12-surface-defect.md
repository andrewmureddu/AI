# 2026-11-19 — D12: the order-0 defect is the surface in 2-D, and D10's definition needed a clause

**Worked:** [D12](../questions/UNKNOWN-LAWS.md#d12--does-the-order-0-defect-scale-as-the-surface-in-short-range-models),
the P0 that [D10](../experiments/D10-composition-lens/) left open
([`SYNTHESIS.md`](../SYNTHESIS.md) §7.0'(a)). Experiment:
[`experiments/D12-surface-defect/`](../experiments/D12-surface-defect/).

**Order of work.**
1. The prior-art note went first and concluded **N0**: Binder 1982,
   Lee–Kosterlitz 1990 and Borgs–Janke 1992 already contain the scaling and the
   exact prefactor.
2. Then the code (Wang–Landau and exact enumeration, in C), validated before any
   defect was computed, then pilots at excluded sizes to place the windows.
3. The pre-registration was committed next.
4. The first production launch stalled. Two schedule bugs were caught before any
   defect was computed, and both are recorded as Amendment A.
5. Then the registered run. Last came a post-hoc 3-D extension, which is labelled
   as such everywhere.

**What changed in the map.**
- **Order 0 is a classifier, in d = 2:** 0 (no coexistence) / (d−1)/d
  (short-range coexistence) / 1 (long-range coexistence). The evidence is 2-D
  q=20, b = 0.509 ± 0.011, with D/L = 0.376 against the exact interface tension
  0.371, and an Ising control that does not grow.
- **D10's B3b is rewritten:** "a first-order transition always violates order 0;
  range sets the exponent". For short range this is sub-extensive, so ensemble
  equivalence still holds per site.
- **D10's definition gains a clause.** A max of N(ŝ − s) over every level picks up
  the non-concave combinatorics of the lowest excitations. Those lumps are exact,
  not noise, grow as ln N, and carry no thermodynamics. The statistic is the
  intruder's depth. D10's own numbers are unaffected.

**What failed, and stays failed.**
- **P2:** the 3-D exponent is 0.778 against a band topping out at 0.767. Its
  slopes fall monotonically, and the post-hoc fit reaches 0.695 at L = 20. That is
  "the dimension enters", not "(d−1)/d confirmed".
- **P4:** the q=10 fit is 0.20, an artifact of the statistic at one size. That
  failure is what exposed the clause above.

**Next.** The 3-D value at larger L, or by a method with smaller finite-size
corrections (multicanonical with an interface-geometry fit). Separately, whether
the long-range/short-range crossover in the exponent can be tracked continuously
in a 1/r^σ family, which D10 also listed as untouched.
