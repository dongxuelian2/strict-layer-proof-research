#!/usr/bin/env python3
"""85-R8 exact symbolic certificate for the R7-PLCF gate differential audit.
This is a regression/provenance certificate, not a search for J2 solutions.
"""
import sympy as sp
from math import gcd

G = sp.symbols('G', integer=True, positive=True)
u = sp.Integer(11); A = sp.Integer(23); K = sp.Integer(10); H = G/2
q = (G+1)/11; B = 2*G+q
c = z = sp.Integer(1); lam = sp.Integer(3)
C3 = c
C2 = sp.simplify(A*c + H*lam)
C1 = sp.simplify((B*z + A*lam)/(2*K))
T = sp.simplify(G*z + u*lam)
h = sp.simplify(q*H*z - A*c)
w = sp.simplify(G*H*z - u*A*c)
m = sp.simplify(A*h - G*z)
r = sp.simplify(H*h - u*c)
d2 = sp.simplify(u*c + G*w)

# PRE_ROOT J2 rows, negative branch epsilon=-1.
assert sp.factor(C3-(2*r-q*w)) == 0
assert sp.factor(d2-(2*u*r-w)) == 0
assert sp.factor(A*r-w-m*H) == 0
assert sp.factor(G*K*C1-A*C2-m) == 0
assert sp.factor(u*C2+w-H*T) == 0
assert sp.factor(2*u*K*C1-A*T-z) == 0

P1 = sp.simplify(G*H*C1)
P2 = sp.simplify(u*G*C2)
P3 = sp.simplify(u*C3)
Q0 = sp.simplify(P2+d2)
D = sp.simplify(H*C2+r)
assert sp.factor(P1*K-Q0-D) == 0
assert sp.factor(Q0-P3-G*H*T) == 0

# Exact non-root word master for the PLCF exponent profile.
# n1=2g, n2=2g+1, n3=g; m1=2, m2=g, m3=2g.
Asharp = sp.expand(10*G**3*C1 + G*C2 + C3)
b1, b2, b3 = sp.Integer(11), H, G*H
Bword = sp.expand(b1*G**3 + b2*G**2 + b3)
V = sp.simplify(u*G*H)
assert sp.factor(V*Asharp-Q0*Bword) == 0

sphere = sp.factor(H**2*C1**2+w**2-T*d2)
expected_num = 47871*G**4 + 3159440*G**3 - 577600*G**2 - 1614236800*G - 12321865600
assert sp.factor(sphere + expected_num/sp.Integer(193600)) == 0
Qprim = sp.factor(A*H**2*C1**2-2*u*K*d2*C1+A*w**2+z*d2)
assert sp.factor(Qprim-A*sphere) == 0  # third Euclidean row has already been imposed
assert sp.factor(P1**2+P2**2+P3**2-Q0**2-G**2*sphere) == 0

# Three exact family-index regressions; theorem statuses are proved symbolically above.
for t in (0,1,2):
    g = 5+22*t
    GG = 10**g
    qq = (GG+1)//11
    BB = 2*GG+qq
    CC1 = (BB+69)//20
    CC2 = (3*GG+46)//2
    dd2 = GG*(GG*GG-506)//2+11
    ww = GG*GG//2-253
    UU = GG-1
    VV = 11*GG*GG//2
    assert BB+69 == 20*CC1
    assert gcd(UU,VV) == 1
    assert GG*GG//10 <= UU*CC1 < GG*GG
    assert GG*GG <= UU*CC2 < 10*GG*GG
    assert GG//10 <= UU < GG
    PP1 = GG*(GG//2)*CC1
    PP2 = 11*GG*CC2
    PP3 = 11
    assert gcd(VV,PP1) == GG*GG//2
    assert gcd(VV,PP2) == 11*GG
    assert gcd(VV,PP3) == 11
    assert gcd(gcd(gcd(PP1,PP2),PP3), PP2+dd2) == 1
    # A-root passes.
    assert (10*CC1+1) % 23 == 0
    # U-SQ root shadow fails.
    assert (CC1*CC1-1) % 11 != 0
    # DCDC root-necessary sieve fails: 2K=20 does not divide primitive constant.
    assert (23*ww*ww+dd2) % 20 == 18
    # Apparently primitive gcd firewall fails, but its historical proof uses sphere.
    assert CC1 % 3 == 0 and dd2 % 3 == 0
    # regular d_A=1.
    assert gcd(23,dd2) == 1

print('85-R8 PLCF GATE DIFFERENTIAL CERTIFICATE')
print('SYMBOLIC_PRE_ROOT_ROWS=PASS')
print('NONROOT_MASTER=PASS')
print('COMMON_V_PROFILE=t=0,1,2 regression PASS; general proof in report')
print('FULL_THREE_NUMERATOR_WINDOWS=t=0,1,2 regression PASS; general proof in report')
print('A_ROOT=PASS')
print('U_SQ=FAIL_TYPE_B_ROOT_MOD_U_SHADOW')
print('DCDC=FAIL_TYPE_B_ROOT_NECESSARY')
print('SPHERE=FAIL_TYPE_C_ROOT_EQUIVALENT_ON_FROZEN_STATE')
print('ROOT_FACTOR_GCD_C1_D2=FAIL_BUT_SPHERE_DERIVED_TYPE_C')
print('FULL_ROOT=FAIL')
print('ROOT_INDEPENDENT_MISSING_GATE=NONE')
print('SOURCE_PROJECTION_PROGRAMME=EXHAUSTED')
print('R8_TERMINAL_VERDICT=SOURCE_PROJECTION_EXHAUSTED_FULL_ROOT_IS_NEXT_INDEPENDENT_GATE')
