#!/usr/bin/env python3
"""95-R8 g=0 C/I/P exact regression replay.

This is a regression/certificate helper, not a global H0 proof engine.
All arithmetic is exact (Fraction / integers).
"""
from fractions import Fraction
from math import gcd
from dataclasses import dataclass


def ceil_frac(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def smith_J(beta: int, v: int, m3: int) -> int:
    ten = 10**m3
    delta_beta = gcd(beta, ten)
    Lambda_beta = ten // delta_beta
    delta_v = gcd(v, Lambda_beta)
    return Lambda_beta // delta_v


def interval(C2: int, C3: int, n2: int, n3: int):
    L = max(Fraction(10**(n2-1), C2), Fraction(10**(n3-1), C3))
    R = min(Fraction(10**n2, C2), Fraction(10**n3, C3))
    return L, R


def classify(C2: int, C3: int, n2: int, n3: int):
    L, R = interval(C2, C3, n2, n3)
    if not L < R:
        return "C_FAIL", L, R, []
    U0 = max(1, ceil_frac(L))
    ints = list(range(U0, max(U0, ceil_frac(R))))
    ints = [u for u in ints if Fraction(u,1) < R]
    if not ints:
        return "I_FAIL", L, R, []
    return "I_SURVIVE", L, R, ints


@dataclass
class State:
    name: str
    b: tuple
    P: tuple
    Q: int
    gprofile: tuple
    n2: int
    n3: int
    beta: int
    v: int
    m3: int
    expected_J: int
    expected_class: str


states = [
    State("A", (1,6,8), (24,52,159), 169, (24,4,3), 2,1, 2,4,1, 5, "C_FAIL"),
    State("B", (1,6,8), (48,436,75), 445, (24,4,3), 2,1, 2,4,1, 5, "I_FAIL"),
    State("C", (1,6,8), (456,292,2907), 2957, (24,4,3), 2,1, 2,4,1, 5, "C_FAIL"),
    State("D", (1,6,8), (552,3796,2847), 4777, (24,4,3), 2,1, 2,4,1, 5, "C_FAIL"),
    State("E", (5,5,1), (298,2514,1485), 2935, (1,1,5), 2,1, 1,1,1, 10, "I_FAIL"),
]


print("95-R8 g=0 exact regression replay")
print("===================================")

for s in states:
    P1,P2,P3=s.P
    assert P1*P1 + P2*P2 + P3*P3 == s.Q*s.Q
    assert gcd(gcd(gcd(P1,P2),P3),s.Q)==1
    g1,g2,g3=s.gprofile
    assert P2 % g2 == 0 and P3 % g3 == 0
    C2=P2//g2
    C3=P3//g3
    J=smith_J(s.beta,s.v,s.m3)
    assert J==s.expected_J
    cls,L,R,ints=classify(C2,C3,s.n2,s.n3)
    assert cls==s.expected_class
    rho=Fraction(C2*10**s.n3, C3*10**s.n2)
    print(
        f"{s.name}: J={J}, C2={C2}, C3={C3}, rho={rho}, "
        f"I=[{L},{R}), class={cls}, integers={ints}"
    )

# Exact real-cone regression point.
C2,C3,n2,n3 = 17813,2633,2,1
cls,L,R,ints=classify(C2,C3,n2,n3)
assert cls=="I_FAIL"
assert 0 < L < R < 1
print(f"REAL_CONE: C2={C2}, C3={C3}, I=[{L},{R}), class={cls}")

# H0 cone formula verification on all recovered states.
for s in states:
    P1,P2,P3=s.P
    g1,g2,g3=s.gprofile
    C2=P2//g2; C3=P3//g3
    M=C2; N=C3  # all recovered rows here have u0=1
    rho=Fraction(M*10**s.n3, N*10**s.n2)
    cone = Fraction(1,10) < rho < 10
    L,R=interval(C2,C3,s.n2,s.n3)
    assert cone == (L<R)

# Plus-branch universal numerical constants used by symbolic proof.
c2 = Fraction(24,2525)
max_rhs = Fraction(50,1) * 4 / c2
assert max_rhs < 10**5 and max_rhs > 10**4
b1_ge3_rhs = Fraction(50,1) * Fraction(16,9) / c2
assert b1_ge3_rhs < 10**4
print(f"PLUS_K_BOUND_MAX_RHS={max_rhs} -> k<=4")
print(f"PLUS_K_BOUND_B1_GE_3_RHS={b1_ge3_rhs} -> k<=3")

print("CERTIFICATE_STATUS=PASS")
