#!/usr/bin/env python3
"""85-R6 exact diagnostics.

No floating-point decision is used.
This script certifies:
1) the live g=4 N0-split base;
2) one regular J2 linear pre-radial no-common-U pseudo-state;
3) one same-base regular J2 linear state with a legal common-U;
4) the historical exact primitive radial pseudo-state with I23 subset (0,1).

It does NOT claim either J2 linear state satisfies the sphere/root gate.
"""

from math import gcd

def n0(G, K, u):
    A = 2*u + 1
    return 4*u*u*G*G*K*K - (G*A + 1)**2 + 2

def j2_u_interval(G, K, C2, C3):
    lo2, hi2 = G*G*K//10, G*G*K
    lo3, hi3 = G//10, G
    umin = max((lo2 + C2 - 1)//C2,
               (lo3 + C3 - 1)//C3,
               1)
    umax = min((hi2 - 1)//C2,
               (hi3 - 1)//C3)
    return umin, umax

# ---- live split base ----
g, k, ell = 4, 1, 7
G, K = 10**g, 10**k
u, q = 73, 137
A, H = 2*u + 1, G//2
assert u*q == G + 1
assert k == 2*g - ell

N0 = n0(G, K, u)
assert N0 == 210999097060001
assert 14449385**2 + 1488076**2 == N0

B = 2*G + q
Cm, Cp = 2*G*K - B, 2*G*K + B
assert N0 == 2 + u*u*Cm*Cp

# ---- no-lift linear state ----
c, z = 3, 1
h, w, m = 684559, 49967807, 100620173
r, d2 = 3422794781, 499678070219
C1, C2, T = 5483, 3045441, 54457

assert c == 2*r - q*w
assert d2 == 2*u*r - w
assert A*r - w == m*H
assert G*K*C1 == A*C2 + m
assert u*C2 + w == H*T
assert 2*u*K*C1 == A*T + z
assert gcd(A, d2) == 1
assert gcd(C1, u) == 1
assert gcd(C2, H) == 1
assert gcd(c, G*H) == 1

umin, umax = j2_u_interval(G, K, C2, c)
assert (umin, umax) == (334, 328)
assert umin > umax

sphere_residual_no_lift = H*H*C1*C1 + w*w - T*d2
assert sphere_residual_no_lift == -23962604708526834

# ---- same-base linear lift ----
C1b, C2b, Tb = 1073, 45441, 10657
assert G*K*C1b == A*C2b + m
assert u*C2b + w == H*Tb
assert 2*u*K*C1b == A*Tb + z
assert gcd(C1b, u) == 1
assert gcd(C2b, H) == 1

umin_b, umax_b = j2_u_interval(G, K, C2b, c)
U = 2201
V = u*G*H
assert umin_b <= U <= umax_b
assert gcd(U, V) == 1
assert G*G*K//10 <= U*C2b < G*G*K
assert G//10 <= U*c < G

sphere_residual_lift = H*H*C1b*C1b + w*w - Tb*d2
assert sphere_residual_lift == -2799504232934634

# ---- exact primitive A1 radial pseudo-state ----
P1, P2, P3, Q0 = 7776, 71252, 7899, 72109
assert P1*P1 + P2*P2 + P3*P3 == Q0*Q0
assert gcd(gcd(P1, P2), gcd(P3, Q0)) == 1
V0 = 24
g2, g3 = 4, 3
C2p, C3p = P2//g2, P3//g3
assert (C2p, C3p) == (17813, 2633)
# n2=2,n3=1: upper endpoint is 10/C3 < 1
assert 10 < C3p

print("85-R6 N0/full-word projection diagnostic")
print("FLOAT_GATE_DECISIONS=0")
print("LIVE_SPLIT_BASE=(g,k,ell,u,q)=(4,1,7,73,137)")
print("N0=", N0)
print("N0_SUM2SQ=(14449385,1488076)")
print("NO_LIFT_U_RANGE=[334,328]=EMPTY")
print("NO_LIFT_REGULAR_gcd(A,d2)=1")
print("NO_LIFT_SPHERE_RESIDUAL=", sphere_residual_no_lift)
print("SAME_BASE_LIFT_U=2201")
print("SAME_BASE_LIFT_U_RANGE=", (umin_b, umax_b))
print("SAME_BASE_LIFT_gcd(U,V)=", gcd(U,V))
print("SAME_BASE_LIFT_SPHERE_RESIDUAL=", sphere_residual_lift)
print("GENERIC_PRIMITIVE_PSEUDO_STATE=(7776,71252,7899,72109)")
print("GENERIC_PRIMITIVE_I23_SUBSET_0_1=TRUE")
print("ROOT_FILTER_USED=NO")
print("CERTIFICATE_STATUS=PASS")
