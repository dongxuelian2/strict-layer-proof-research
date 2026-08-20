#!/usr/bin/env python3
"""95-R3 exact symbolic/regression audit.

This script checks only the algebra stated in the R3 report.
It does NOT claim any pseudo-family is a source solution.
"""
import sympy as sp

# --------------------------------------------------------------------
# 1. General-J unimodular envelope and radial cross-product
# --------------------------------------------------------------------
G, u0, J, U = sp.symbols("G u0 J U", positive=True, integer=True)
q0 = sp.symbols("q0", positive=True, integer=True)

A = J*u0 + 1
B = J*G + q0

# impose G+1 = u0*q0
subs_cyc = {G: u0*q0 - 1}

assert sp.expand((u0*B - G*A - 1).subs(subs_cyc)) == 0

D_rad = sp.expand(A*U - u0*B)
D_expected = sp.expand(A*(U-G) - 1)
assert sp.expand((D_rad-D_expected).subs(subs_cyc)) == 0

# --------------------------------------------------------------------
# 2. H5.1 envelope
# --------------------------------------------------------------------
for u0v in (1, 11):
    Gv, Jv = 10, 5
    qv = (Gv+1)//u0v
    Av = Jv*u0v + 1
    Bv = Jv*Gv + qv
    assert u0v*Bv - Gv*Av == 1
    print("H5.1", {"u0":u0v, "q0":qv, "Abar":Av, "Bbar":Bv})

# --------------------------------------------------------------------
# 3. Negative RRGS/core/digit/SRUS pseudo-family.
#    It intentionally fails the primitive sphere.
# --------------------------------------------------------------------
t = sp.symbols("t", nonnegative=True, integer=True)

g = 1
Gv = 10
Jv = 10
u = u0v = dstar = beta0 = s = 1
n3 = 1
k = 1
n2 = 3
Uv = 1
C2 = 100
C3 = 1
a2 = Uv*C2
a3 = Uv*C3

w = 100*t + 99
W = -w
xi = Uv*W
d2 = 1000*t + 991
P2 = 1000
P3 = 1
Q0 = 1000*t + 1991
D1 = 110*t + 209
D = D1
P1 = 111*t + 220
Kstar = 10
q0v = 11
gamma = 1

checks = {
    "leading_defect": sp.expand(D - (10**k*P1-Q0)),
    "S_R": sp.expand((P2+P3-Q0) - Kstar*W),
    "core": sp.expand(u*Jv*D1 - (dstar*Q0-W)),
    "RRGS1": sp.expand(Uv*(Q0-P2) + Kstar*xi - u0v*a3),
    "RRGS2": sp.expand(
        dstar*(10**n3*a2+a3) -
        (q0v*xi + gamma*Jv*Uv*D1)
    ),
}
for name, expr in checks.items():
    assert expr == 0, (name, expr)

# SRUS interval here is [1,10)
assert 1 <= Uv/u0v < 10

sphere_defect = sp.expand(Q0**2 - (P1**2+P2**2+P3**2))
assert sp.factor(sphere_defect) == (
    987679*t**2 + 3933160*t + 2915680
)
print("negative witness sphere defect =", sphere_defect)
print("AUDIT_STATUS=PASS")
