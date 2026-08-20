#!/usr/bin/env python3
"""Exact verifier for 105-R3 S3-R3-VSCF.
This is a pseudo-source counterfamily: it verifies primitive/source/J/cell
conditions and then verifies that the full UDD/master row FAILS positively.
It is NOT a generator of original A1 solutions.
"""
from math import gcd

def verify(r: int):
    assert r >= 1
    G = 10 ** (r + 1)
    K = 10
    V = 10 ** (2*r + 3)
    assert V == 10 * G * G

    P2, P3 = V, 1
    P1 = V*V // 2
    Q0 = (V*V + 2) // 2
    assert P1*P1 + P2*P2 + P3*P3 == Q0*Q0
    assert gcd(gcd(P1,P2),gcd(P3,Q0)) == 1

    g1 = gcd(V,P1); g2 = gcd(V,P2); g3 = gcd(V,P3)
    assert (g1,g2,g3) == (V,V,1)
    C1,C2,C3 = P1//g1,P2//g2,P3//g3
    b1,b2,b3 = V//g1,V//g2,V//g3
    assert (C1,C2,C3) == (V//2,1,1)
    assert (b1,b2,b3) == (1,1,V)

    m1=m2=1
    m3=2*r+4
    n2=n3=r+3
    n1=3*r+5
    g=m3-n3
    k=1
    d=m2-g
    assert g == r+1 and d == -r and d <= -1
    assert n2 == m2+g+k
    assert m3 == n3+g

    U = 10**(r+2)+1
    L = 10**(r+2)
    Rsrc = 2*10**(r+2)
    assert L <= U < Rsrc
    assert gcd(U,V) == 1

    a1,a2,a3=U*C1,U*C2,U*C3
    assert 10**(n1-1) <= a1 < 10**n1
    assert 10**(n2-1) <= a2 < 10**n2
    assert 10**(n3-1) <= a3 < 10**n3
    assert 10**(m1-1) <= b1 < 10**m1
    assert 10**(m2-1) <= b2 < 10**m2
    assert 10**(m3-1) <= b3 < 10**m3

    beta=1
    Lambda_beta = 10**m3
    delta_v = gcd(V,Lambda_beta)
    J = Lambda_beta // delta_v
    assert J == 10

    D = K*P1-Q0
    H = b2*Q0-b1*(10**m2)*D
    Rden = b2*(10**n3)-b3
    assert D > 0 and H < 0 and Rden < 0

    T3 = Q0-P3
    assert (b3*T3) % (10**n3) == 0
    tau3=(b3*T3)//(10**n3)
    udd_residual = b2*P2 - tau3 - G*H
    expected = G*(4445*G**4 + 10*G - 11)
    assert udd_residual == expected and udd_residual > 0

    return {
        "r":r, "G":G, "V":V, "J":J, "d":d,
        "U":U, "D":D, "H":H, "R":Rden,
        "UDD_residual":udd_residual,
        "cell":"S3",
        "primitive":"PASS",
        "source_digit":"PASS",
        "coprime":"PASS",
        "full_master":"FAIL_AS_DESIGNED",
    }

if __name__ == "__main__":
    for r in [1,2,3,5,10]:
        row=verify(r)
        print("PASS", row)
    print("S3-R3-VSCF certificate: PASS")
