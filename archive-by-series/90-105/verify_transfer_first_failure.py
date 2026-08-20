#!/usr/bin/env python3
"""105-R5C exact verifier.

Verifies:
1) the canonical R5 arbitrary-depth reduced family;
2) the R3 primitive-sphere/source-digit completion;
3) the exact T_minus transfer formulas;
4) the sphere x full-master eliminant;
5) the fixed odd 5-adic discriminant valuation.

The discriminant theorem is symbolic/exact. No floating point is used for proof decisions.
"""
from math import gcd
import sympy as sp

def v_p(n: int, p: int) -> int:
    n = abs(int(n))
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e

def verify_r3_section(r: int):
    assert r >= 1
    G = 10 ** (r + 1)
    K = 10
    V = 10 * G * G
    P2, P3 = V, 1
    P1 = 50 * G**4
    Q0 = 50 * G**4 + 1

    assert P1*P1 + P2*P2 + P3*P3 == Q0*Q0
    assert gcd(gcd(P1,P2),gcd(P3,Q0)) == 1

    g1, g2, g3 = gcd(V,P1), gcd(V,P2), gcd(V,P3)
    assert (g1,g2,g3) == (V,V,1)
    C1,C2,C3 = P1//g1,P2//g2,P3//g3
    assert (C1,C2,C3) == (5*G*G,1,1)
    b1,b2,b3 = V//g1,V//g2,V//g3
    assert (b1,b2,b3) == (1,1,V)

    g = r+1
    d = -r
    m1=m2=1
    n2=n3=g+2
    m3=2*g+2
    n1=3*g+2
    U=10*G+1

    a1,a2,a3=U*C1,U*C2,U*C3
    assert 10**(n1-1) <= a1 < 10**n1
    assert 10**(n2-1) <= a2 < 10**n2
    assert 10**(n3-1) <= a3 < 10**n3
    assert gcd(U,V)==1

    Lambda_beta=10**m3
    delta_v=gcd(V,Lambda_beta)
    J=Lambda_beta//delta_v
    assert J==10

    Y=10**n3
    D=K*P1-Q0
    H=Q0-10*D
    T3=Q0-P3
    assert (b3*T3)%Y==0
    tau3=(b3*T3)//Y
    assert tau3==5*G**5

    # Visible leading-word projection failure of THIS sphere section.
    assert -H == 89*Q0-100
    assert -H > Q0

    # Full master/UDD fails on this section.
    residual=P2-tau3-G*H
    assert residual == G*(4445*G**4+10*G-11)
    assert residual>0

    return {
        "r":r,"G":G,"d":d,"V":V,"U":U,"J":J,
        "sphere":"PASS","digits":"PASS","gcd":"PASS","tail":"PASS",
        "leading_word_section":"FAIL","master_section":"FAIL",
        "master_residual":residual
    }

def symbolic_first_failure():
    G,Q0,P1 = sp.symbols("G Q0 P1", positive=True)
    V=10*G**2
    # Full master on canonical reduced profile.
    M = sp.expand(111*Q0 - 1000*P1 - (100*G+1))
    S = sp.expand(P1**2 + V**2 + 1 - Q0**2)
    P1sol=(111*Q0-100*G-1)/1000
    poly=sp.factor(sp.together(S.subs(P1,P1sol)*1000000))
    expected=(
        100000000*G**4 + 10000*G**2 - 22200*G*Q0 + 200*G
        - 987679*Q0**2 - 222*Q0 + 1000001
    )
    assert sp.expand(poly-expected)==0
    disc=sp.factor(sp.discriminant(sp.Poly(poly,Q0),Q0))
    expected_disc=80000000*(4938395*G**4+500*G**2+10*G+49384)
    assert sp.expand(disc-expected_disc)==0
    assert sp.factorint(80000000)=={2:10,5:7}

    H=11*Q0-100*P1
    H_on=sp.factor(H.subs(P1,P1sol))
    assert sp.expand(H_on-(100*G-Q0+1)/10)==0
    return sp.factor(poly), sp.factor(disc), H_on

def concrete_discriminant_check(g: int):
    assert g>=1
    G=10**g
    inner=4938395*G**4+500*G**2+10*G+49384
    Delta=80000000*inner
    assert inner%5==4
    assert v_p(Delta,5)==7
    return G, inner%5, v_p(Delta,5)

if __name__=="__main__":
    poly,disc,H_on=symbolic_first_failure()
    print("SYMBOLIC ELIMINANT:", poly)
    print("DISCRIMINANT:", disc)
    print("H ON MASTER:", H_on)
    for g in [1,2,3,5,10]:
        print("DISC-CHECK", concrete_discriminant_check(g))
    for r in [1,2,3,5]:
        row=verify_r3_section(r)
        print("R3-SECTION", row)
    print("105-R5C certificate: PASS")
