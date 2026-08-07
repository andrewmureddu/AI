import math

def chi2_sym_bsc(p):
    p0 = (1-p, p)
    p1 = (p, 1-p)
    chi2_01 = sum((a-b)**2/b for a,b in zip(p0,p1))
    chi2_10 = sum((a-b)**2/b for a,b in zip(p1,p0))
    return 0.5*(chi2_01+chi2_10)

def N_bec(e):
    return 1.0/(1.0-e)

eps_list = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

def slope_against(f_of_eps, transform, eps_list):
    xs = [transform(e) for e in eps_list]
    ys = [f_of_eps(e) for e in eps_list]
    lx = [math.log(x) for x in xs]
    ly = [math.log(abs(y)) for y in ys]
    return (ly[-1]-ly[-2])/(lx[-1]-lx[-2])

ident = lambda e: e
sin_t = lambda e: math.sin(e)
aff_t = lambda e: 3*e + 7*e**2

print("=== Type M: BSC (threshold p_c=1/2) ===")
f_bsc = lambda e: chi2_sym_bsc(0.5-e)
print("raw alpha (against eps = p_c-p):", round(slope_against(f_bsc, ident, eps_list),4))
for a in [0.5,2.0,3.0]:
    t = lambda e,a=a: e**a
    s = slope_against(f_bsc, t, eps_list)
    print(f"  G_pow reparam a={a}: exponent -> {s:.4f}  (predicted 2/a = {2/a:.4f})")
for name,t in [("sin(eps)", sin_t), ("3eps+7eps^2", aff_t)]:
    s = slope_against(f_bsc, t, eps_list)
    print(f"  regular reparam {name}: exponent -> {s:.4f}  (predicted unchanged = 2.0000)")

print()
print("=== Type S: BEC (threshold e_c=1) ===")
f_bec = lambda e: N_bec(1-e)   # e here plays role of (1-e_c+e_c-e)... eps = e_c - e = 1-(1-eps)
print("raw alpha (against eps = e_c-e):", round(slope_against(f_bec, ident, eps_list),4))
for a in [0.5,2.0,3.0]:
    t = lambda e,a=a: e**a
    s = slope_against(f_bec, t, eps_list)
    print(f"  G_pow reparam a={a}: exponent -> {s:.4f}  (predicted 1/a = {1/a:.4f})")
for name,t in [("sin(eps)", sin_t), ("3eps+7eps^2", aff_t)]:
    s = slope_against(f_bec, t, eps_list)
    print(f"  regular reparam {name}: exponent -> {s:.4f}  (predicted unchanged = 1.0000)")
# Re-check: does alpha pass a CROSS-SYSTEM invariance test (D1's own P2 methodology)
# rather than just single-system reparametrization invariance?
# This uses S5's own already-published numbers (S5-noise-thresholds/README.md),
# just re-framed as a D1-style invariance test rather than re-measured.

print("Type M (claimed invariant p=2 candidate), three STRUCTURALLY unrelated systems:")
print("  BSC (discrete channel):                 alpha = 2.0000")
print("  BI-AWGN (continuous Gaussian channel):   alpha = 1.9985")
print("  quasispecies+majority-repair (biology):  alpha = 2.035")
print("  spread:", round(2.035-1.9985,4), " -- agree despite unrelated formulas (Bernoulli entropy vs Gaussian MI vs class-dynamics fitness recursion)")
print()
print("Type S (claimed invariant p=1 candidate), two structurally unrelated systems:")
print("  BEC (erasure channel):    alpha = 1.0000")
print("  Z-channel (asymmetric):   alpha = 1.0000")
print("  spread: 0.0000 -- exact agreement, unrelated channel laws")
print()
print("Type R (candidate NON-invariant / gauge, per D2's independent finding), four codes:")
vals = [2.2621, 2.3223, 2.8078, 3.1704]
print("  concatenated codes n0=23,7,9,5:", vals)
print("  spread:", round(max(vals)-min(vals),4), "-- varies freely with scheme, fails the cross-system test M and S pass")

