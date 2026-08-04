#!/usr/bin/env python3
"""
F3 — only 3b rounds.

Tests the sharpest prediction of invariants/FLOOR3-STRATA.md, the sort of floor 3
against the trichotomy derivations/base-variable.md §4 forced:

  3a  DOMAIN BOUNDARY   Phi = +inf beyond a boundary; lambda_c STABLE in size
  3b  LIMIT             Phi analytic at finite size; ROUNDS, width -> 0
  3c  DEGENERACY        Phi analytic and finite; the degeneracy is EXACT, no rounding

One instrument, one set of tolerances, three exemplars. Every tolerance is
registered against a stated noise floor (METHODOLOGY audit item (iii), rewritten
after BV violated the checklist version three times in one run).

Pure numpy + scipy. Deterministic. Writes verdict.json.
"""

import json
import math
import time

import numpy as np
from scipy.optimize import brentq
from scipy.special import logsumexp

SEED = 20260728
OUT = {}
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def rec(k, v):
    OUT[k] = v


def fit_slope(x, y):
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


# ----------------------------------------------------------------------------
# the one instrument, with its noise floor reported alongside every answer
# ----------------------------------------------------------------------------

def kink_width(f, t_c, half_span, m=4001):
    """FWHM of |f''| around t_c. Returns the resolution floor with the width, so
    'a width' and 'no width' are distinguishable rather than a judgement call."""
    floor = 2.0 * half_span / (m - 1)
    t = np.linspace(t_c - half_span, t_c + half_span, m)
    y = np.array([f(v) for v in t])
    if not np.all(np.isfinite(y)):
        return dict(width=None, floor=floor, reason="f not finite on the window")
    h = t[1] - t[0]
    d2 = np.abs(y[2:] - 2 * y[1:-1] + y[:-2]) / h ** 2
    tt = t[1:-1]
    i = int(np.argmax(d2))
    if i <= 1 or i >= len(d2) - 2 or not np.isfinite(d2[i]) or d2[i] <= 0:
        return dict(width=None, floor=floor, reason="no interior peak")
    above = np.where(d2 >= d2[i] / 2.0)[0]
    w = float(tt[above[-1]] - tt[above[0]] + h)
    return dict(width=w, floor=floor, ratio=w / floor,
                peak_curvature=float(d2[i]), peak_at=float(tt[i]))


# ============================================================================
# 3b — the limit stratum: the only one that should round            P1
# ============================================================================

def leg_3b():
    say("\n=== 3b — LIMIT: does it round? (calibration; identity) ===")
    Nlist = [20, 40, 80, 160, 320, 640, 1280, 2560, 5120]
    rows = []
    for N in Nlist:
        def f(t, N=N):
            return -(1.0 / N) * logsumexp([0.0, -N * t])
        k = kink_width(f, 0.0, half_span=min(2.0, 60.0 / N))
        rows.append(dict(N=N, **{kk: vv for kk, vv in k.items() if kk != "reason"}))
    widths = np.array([r["width"] for r in rows])
    slope = fit_slope(np.array(Nlist, float), widths)
    min_ratio = float(min(r["ratio"] for r in rows))
    out = dict(rows=rows, width_exponent=slope, min_width_over_floor=min_ratio)
    out["P1_pass"] = bool(abs(slope + 1.0) <= 0.03 and min_ratio >= 20.0)
    say(f"  widths {[round(w, 5) for w in widths]}")
    say(f"  P1 (identity) width ~ N^{slope:.4f}, every width >= "
        f"{min_ratio:.0f}x the instrument floor  pass={out['P1_pass']}")
    rec("stratum_3b", out)
    return out


# ============================================================================
# 3a — the domain boundary: stable, and a divergence not a width    P2
# ============================================================================

def leg_3a():
    say("\n=== 3a — DOMAIN BOUNDARY: stable in size, diverges (AT RISK) ===")
    # Y ~ Exponential(1) truncated at M. Phi_M(lam) = log((1-e^{-(1-lam)M})/(1-lam)),
    # entire for finite M; -> -log(1-lam) with a pole at lam = 1 as M -> oo.
    def phi(lam, M, n=400_000):
        y = (np.arange(n) + 0.5) / n * M
        w = np.exp(-y)
        w = w / w.sum()
        return float(logsumexp(np.log(w) + lam * y))

    rows = []
    for M in (10.0, 1e2, 1e3, 1e4):
        # locate the boundary as the lambda where Phi first exceeds a large level
        LEVEL = 50.0

        def g(lam):
            return phi(lam, M) - LEVEL

        lo, hi = 0.0, 5.0
        lam_c = brentq(g, lo, hi, xtol=1e-12) if g(lo) * g(hi) < 0 else None
        beyond = phi(1.1, M)
        rows.append(dict(M=float(M), lambda_c=(None if lam_c is None else float(lam_c)),
                         phi_beyond_boundary=float(beyond)))
        say(f"  M={M:>8.0f}  lambda_c={lam_c if lam_c is None else round(lam_c, 9)}"
            f"   Phi(1.1)={beyond:.4f}")

    lcs = [r["lambda_c"] for r in rows if r["lambda_c"] is not None]
    drift = float(max(lcs) - min(lcs)) if len(lcs) > 1 else None
    beyonds = [r["phi_beyond_boundary"] for r in rows]
    growth = [beyonds[i + 1] - beyonds[i] for i in range(len(beyonds) - 1)]
    # Phi(1.1) ~ 0.1*M for large M, so it grows additively by ~log-decade; register
    # growth as a ratio of the *value*, which is what "grows without bound" means
    ratios = [beyonds[i + 1] / max(beyonds[i], 1e-12) for i in range(len(beyonds) - 1)]

    out = dict(rows=rows, lambda_c_drift=drift, growth_ratios=[float(r) for r in ratios])
    out["P2_pass"] = bool(drift is not None and drift <= 1e-6
                          and min(ratios) >= 10.0)
    say(f"  P2 (AT RISK) lambda_c drift over 4 decades of M: {drift:.2e} "
        f"[registered <= 1e-6, bisection floor 1e-12]; Phi beyond it grows by "
        f"{[round(r, 1) for r in ratios]}x per decade  pass={out['P2_pass']}")

    # ---- POST-HOC: P2 was wrong in principle, not mis-measured -------------
    # Two faults, and the second is the interesting one.
    # (1) INSTRUMENT: the quadrature underflows -- exp(-y) is 0 beyond y ~ 745,
    #     so Phi saturates at ~0.1*745 = 74.5 and M = 1e3 and 1e4 return the same
    #     number. Redone below with the exact closed form.
    # (2) PRINCIPLE: at FINITE M there is no boundary at all -- Phi_M is entire,
    #     which is the derivation's own F-fact. "lambda_c stable in system size"
    #     is not merely mis-operationalised, it is not well posed. 3a's boundary
    #     appears only in the M -> oo limit, exactly as 3b's kink appears only in
    #     the N -> oo limit.
    # So the surviving distinction is not limit-vs-no-limit. It is WHAT diverges:
    #     3a  Phi ITSELF diverges, on a REGION of lambda
    #     3b  Phi stays finite; a DERIVATIVE diverges, at a POINT
    #     3c  nothing diverges; a derivative is exactly ZERO at finite size
    def phi_exact(lam, M):
        """log E[e^{lam Y}] for Y ~ Exp(1) truncated to [0, M]. Stable."""
        den = math.log(-math.expm1(-M))
        if abs(lam - 1.0) < 1e-12:
            return math.log(M) - den
        if lam < 1.0:
            return math.log(-math.expm1(-(1 - lam) * M)) - math.log(1 - lam) - den
        a = lam - 1.0
        aM = a * M
        num = (aM + math.log(-math.expm1(-aM))) if aM > 30 else math.log(math.expm1(aM))
        return num - math.log(a) - den

    Ms = [1e2, 1e3, 1e4, 1e5, 1e6]
    below = [phi_exact(0.9, M) for M in Ms]          # lambda < 1: converges
    above = [phi_exact(1.1, M) for M in Ms]          # lambda > 1: diverges
    below_incr = [abs(below[i + 1] - below[i]) for i in range(len(Ms) - 1)]
    above_slope = fit_slope(np.array(Ms), np.array(above))
    # and Phi is FINITE at 3b's kink at every N, for contrast
    kink_vals = [-(1.0 / N) * logsumexp([0.0, 0.0]) for N in (20, 320, 5120)]

    out["posthoc"] = dict(
        phi_below_boundary=[float(v) for v in below],
        phi_below_increments=[float(v) for v in below_incr],
        phi_above_boundary=[float(v) for v in above],
        phi_above_growth_exponent_in_M=above_slope,
        exact_limit_below=-math.log(1 - 0.9),
        phi_finite_at_3b_kink=[float(v) for v in kink_vals],
        repaired_claim=("3a is a limit phenomenon too; the distinction that "
                        "survives is WHAT diverges -- Phi itself on a region (3a) "
                        "vs a derivative at a point (3b) vs nothing (3c)"),
        registered_claim_was="lambda_c stable in system size -- not well posed",
    )
    out["posthoc_repaired_pass"] = bool(below_incr[-1] <= 1e-9
                                        and abs(above_slope - 1.0) <= 0.02)
    say(f"  [post-hoc] exact closed form: Phi(0.9) converges to "
        f"{below[-1]:.9f} (exact {-math.log(0.1):.9f}), increments "
        f"{below_incr[-1]:.1e}; Phi(1.1) grows as M^{above_slope:.4f} (linear)")
    say(f"  [post-hoc] so 3a's boundary IS a limit, like 3b's kink; what separates "
        f"them is that Phi itself diverges (3a) vs stays finite while a derivative "
        f"diverges (3b). Repaired claim pass={out['posthoc_repaired_pass']}")
    rec("stratum_3a", out)
    return out


# ============================================================================
# 3c — the degeneracy: exact at every size, no rounding             P3
# ============================================================================

def leg_3c():
    say("\n=== 3c — DEGENERACY: exact at every size, no rounding (AT RISK) ===")
    rng = np.random.default_rng(SEED)
    rows = []
    for n in (10, 100, 1000, 10_000):
        z = rng.normal(size=n)
        Y = np.stack([z, 2.5 * z - 1.0], axis=1)      # functionally dependent
        w = np.full(n, 1.0 / n)
        lam = np.array([0.2, -0.1])
        lp = np.log(w) + Y.dot(lam)
        q = np.exp(lp - logsumexp(lp))
        mu = Y.T.dot(q)
        C = (Y - mu).T.dot((Y - mu) * q[:, None])      # exact grad^2 Phi
        ev = np.sort(np.abs(np.linalg.eigvalsh(C)))[::-1]
        rows.append(dict(n=n, eigen_ratio=float(ev[-1] / ev[0])))
        say(f"  n={n:>6}  smallest/largest eigenvalue of grad^2 Phi = "
            f"{ev[-1] / ev[0]:.2e}")

    ratios = np.array([r["eigen_ratio"] for r in rows])
    trend = fit_slope(np.array([r["n"] for r in rows], float),
                      np.maximum(ratios, 1e-18))

    # the same kink instrument, on the same object: is there a locus at all?
    n = 2000
    z = rng.normal(size=n)
    Y = np.stack([z, 2.5 * z - 1.0], axis=1)
    w = np.full(n, 1.0 / n)

    def phi_along(t):
        lam = np.array([t, -t])
        return float(logsumexp(np.log(w) + Y.dot(lam)))

    k = kink_width(phi_along, 0.0, half_span=1.0)

    out = dict(rows=rows, max_eigen_ratio=float(ratios.max()), trend_exponent=trend,
               instrument=k)
    no_rounding = (k["width"] is None) or (k.get("ratio", 0) <= 1.01)
    out["P3_pass"] = bool(ratios.max() <= 1e-14 and abs(trend) <= 0.05 and no_rounding)
    inst = ("no locus" if k["width"] is None
            else f"width/floor={k['ratio']:.3f}")
    say(f"  P3 (AT RISK) max eigen ratio {ratios.max():.2e} "
        f"[registered <= 1e-14, exact-covariance floor ~1e-16], trend in n "
        f"{trend:+.4f}; kink instrument: {inst}  pass={out['P3_pass']}")

    # ---- POST-HOC: two mis-specified criteria, and the second is a category
    # error that the instrument caught for me.
    # (1) The trend was fitted through values spanning 4.4e-17 .. 8.9e-16 with a
    #     noise floor of ~1e-16 -- a power law fitted to noise. No trend is
    #     measurable there and none should have been registered.
    # (2) I asked the kink instrument for a width "at the resolution floor",
    #     i.e. a SHARP kink. But 3c has no kink at all: Phi is analytic, and the
    #     degeneracy is in the EIGENVALUES of grad^2 Phi, not in any
    #     non-analyticity. The instrument returned the whole window, which is
    #     its correct way of saying "no localised feature" -- and that is a
    #     fourth distinguishable output, not a failure.
    window = 2.0 * 1.0
    out["posthoc"] = dict(
        eigen_ratios=[float(r) for r in ratios],
        noise_floor=1e-16,
        all_within_10x_of_floor=bool(ratios.max() <= 1e-14),
        trend_fitted_to_noise=True,
        instrument_width=(None if k["width"] is None else float(k["width"])),
        instrument_window=window,
        width_over_window=(None if k["width"] is None else float(k["width"] / window)),
        diagnosis=("(1) a power law fitted to values at the machine noise floor; "
                   "(2) I registered 'width at the resolution floor' (a SHARP "
                   "kink) for an object that has no kink at all -- 3c is analytic "
                   "and its degeneracy lives in the eigenvalues. The instrument "
                   "returned the full window, which is 'no localised feature'."),
    )
    say(f"  [post-hoc] eigen ratios {[f'{r:.1e}' for r in ratios]} are all at the "
        f"~1e-16 noise floor, so the registered trend was fitted to noise")
    say(f"  [post-hoc] instrument width / full window = "
        f"{out['posthoc']['width_over_window']:.4f} -> 'no localised feature', "
        f"a fourth output I failed to register as the right one for 3c")
    rec("stratum_3c", out)
    return out


# ============================================================================
# S25's kink — the sort's prediction about an unexamined repo result  P4 P5
# ============================================================================

def leg_S25():
    say("\n=== S25's lambda(P) = min(P,D)/2 kink — predicted 3c, not 3b ===")
    rng = np.random.default_rng(SEED + 1)
    rows = []
    for D in (4, 8, 16, 32):
        ranks, gaps = [], []
        for P in range(1, 2 * D + 1):
            A = rng.normal(size=(D, P))
            F = A.T.dot(A)                      # population Fisher, Sigma_x = I
            ev = np.sort(np.abs(np.linalg.eigvalsh(F)))[::-1]
            r = int((ev > 1e-14 * ev[0]).sum())
            ranks.append(r)
            if P == D + 1:
                gaps.append(float(ev[D] / ev[0]))
        lam = [min(P, D) / 2 for P in range(1, 2 * D + 1)]
        measured = [r / 2 for r in ranks]
        rows.append(dict(D=D, max_abs_err=float(max(abs(a - b) for a, b in
                                                    zip(lam, measured))),
                         eigen_gap_at_P_eq_D_plus_1=gaps[0] if gaps else None))
        say(f"  D={D:>3}: |rank/2 - min(P,D)/2| max = {rows[-1]['max_abs_err']:.1e}; "
            f"(D+1)-th eigenvalue / 1st at P=D+1 = "
            f"{rows[-1]['eigen_gap_at_P_eq_D_plus_1']:.2e}")

    out = dict(rows=rows,
               max_err=float(max(r["max_abs_err"] for r in rows)),
               max_gap=float(max(r["eigen_gap_at_P_eq_D_plus_1"] for r in rows)))
    out["P4_pass"] = bool(out["max_err"] == 0.0)
    out["P5_pass"] = bool(out["max_gap"] <= 1e-14)
    say(f"  P4 (identity) rank is an integer, so the kink is sharp by "
        f"construction: err {out['max_err']:.1e}  pass={out['P4_pass']}")
    say(f"  P5 (AT RISK) and sharp NUMERICALLY: worst eigenvalue gap "
        f"{out['max_gap']:.2e} [registered <= 1e-14, exact-Gram floor ~1e-16]  "
        f"pass={out['P5_pass']}")
    rec("S25_kink", out)
    return out


# ============================================================================

def main():
    say("F3 — only 3b rounds.")
    b, a, c, s = leg_3b(), leg_3a(), leg_3c(), leg_S25()

    # P6: the cross-cutting claim, one instrument
    rounded = {"3b": b["min_width_over_floor"] >= 20.0,
               "3c": not ((c["instrument"]["width"] is not None)
                          and c["instrument"].get("ratio", 0) > 1.01)}
    p6 = bool(rounded["3b"] and rounded["3c"] and a["P2_pass"])
    say(f"\n  P6 (AT RISK) one instrument, three behaviours: 3b rounds "
        f"({b['min_width_over_floor']:.0f}x floor), 3c does not, 3a gives a stable "
        f"boundary instead of a width  pass={p6}")

    # ---- POST-HOC: P6 as it should have been registered -------------------
    # P2 and P3 each failed on their criterion rather than their content, and
    # repairing both gives a SHARPER classification than the one registered:
    # the instrument has four outputs, and the fourth is P-K's selector, which
    # is not a Phi object at all.
    repaired = {
        "3a  Phi diverges on a region (limit over support)":
            f"Phi(0.9) converges to {a['posthoc']['phi_below_boundary'][-1]:.9f} "
            f"(increments {a['posthoc']['phi_below_increments'][-1]:.0e}); "
            f"Phi(1.1) grows as M^{a['posthoc']['phi_above_growth_exponent_in_M']:.3f}",
        "3b  Phi finite, a derivative diverges at a point (limit over size)":
            f"localised width, {b['min_width_over_floor']:.0f}x floor, "
            f"shrinking as N^{b['width_exponent']:.3f}",
        "3c  Phi analytic, an eigenvalue exactly zero (exact at finite size)":
            f"no localised feature (width/window = "
            f"{c['posthoc']['width_over_window']:.3f}); eigen ratio "
            f"{c['max_eigen_ratio']:.1e} at the noise floor",
        "(type C, NOT floor 3) an argmin crossing":
            "width pinned at the resolution floor at every size (P-K)",
    }
    p6r = bool(
        abs(a["posthoc"]["phi_above_growth_exponent_in_M"] - 1.0) <= 0.02
        and a["posthoc"]["phi_below_increments"][-1] <= 1e-9
        and b["min_width_over_floor"] >= 20.0
        and abs(b["width_exponent"] + 1.0) <= 0.03
        and c["posthoc"]["width_over_window"] >= 0.95
        and c["max_eigen_ratio"] <= 1e-14)
    OUT["P6_repaired"] = dict(table=repaired, pass_=p6r)
    say("\n  [post-hoc] P6 repaired — one instrument, FOUR distinguishable outputs:")
    for kk, vv in repaired.items():
        say(f"    {kk}\n        {vv}")
    say(f"  repaired P6 pass={p6r}")

    verdict = {
        "P1_3b_rounds_identity": b["P1_pass"],
        "P2_3a_boundary_stable": a["P2_pass"],
        "P3_3c_does_not_round": c["P3_pass"],
        "P4_S25_sharp_by_construction": s["P4_pass"],
        "P5_S25_sharp_numerically": s["P5_pass"],
        "P6_one_instrument_three_behaviours": p6,
    }
    at_risk = ["P2_3a_boundary_stable", "P3_3c_does_not_round",
               "P5_S25_sharp_numerically", "P6_one_instrument_three_behaviours"]
    ident = ["P1_3b_rounds_identity", "P4_S25_sharp_by_construction"]

    OUT["verdict"] = verdict
    OUT["at_risk_predictions"] = at_risk
    OUT["declared_identities"] = ident
    OUT["at_risk_passed"] = sum(verdict[k] for k in at_risk)
    OUT["at_risk_total"] = len(at_risk)
    OUT["identities_passed"] = sum(verdict[k] for k in ident)
    OUT["seed"] = SEED
    OUT["runtime_s"] = round(time.time() - T0, 1)

    say("\n=== VERDICT ===")
    for k, v in verdict.items():
        say(f"  [{'AT RISK ' if k in at_risk else 'identity'}] {k}: "
            f"{'PASS' if v else 'FAIL'}")
    say(f"\n  at-risk passed: {OUT['at_risk_passed']}/{OUT['at_risk_total']}")
    say(f"  identities passed: {OUT['identities_passed']}/{len(ident)}")
    say(f"  runtime {OUT['runtime_s']}s")

    with open("verdict.json", "w") as fh:
        json.dump(OUT, fh, indent=2, sort_keys=True)
    say("\nwrote verdict.json")


if __name__ == "__main__":
    main()
