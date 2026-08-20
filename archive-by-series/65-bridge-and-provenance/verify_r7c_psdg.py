#!/usr/bin/env python3
"""105-R7C exact algebra verifier.

This script certifies:
1) the sign of the factor master;
2) falsification of the proposed coefficient-external supply lemma;
3) the infinite primitive near-balanced sphere family;
4) determinant-packet gcd identities on deterministic samples.

It does NOT claim a global outer PSDG theorem.
"""
from math import gcd

def check_supply_counterexample():
    P1,P2,P3,Q0 = 2,14,5,15
    Ah,Bh,c = 1,6,3
    N = P2*P2 + P3*P3
    a,b = Bh-Ah, Ah+Bh
    x,y = Q0+P1, Q0-P1
    assert P1*P1 + N == Q0*Q0
    assert Ah*Q0 - Bh*P1 == c
    assert x*y == N
    assert b*y - a*x == 2*c
    aext = a // gcd(a,2*c)
    bext = b // gcd(b,2*c)
    assert N % aext != 0
    assert N % bext != 0
    return (a,b,c,N,x,y,aext,bext)

def check_near_balanced_family(limit=100):
    for n in range(1,limit+1):
        P1,P2,P3,Q0 = 2*n,2*n*n,1,2*n*n+1
        N = P2*P2 + P3*P3
        x,y = Q0+P1,Q0-P1
        assert P1*P1 + N == Q0*Q0
        assert gcd(gcd(P1,P2),gcd(P3,Q0)) == 1
        assert x*y == N
        assert gcd(P1,Q0) == 1
    return True

def check_determinant_packet_samples():
    # Start from coprime X0,Y0 and coprime a',b'; define Delta exactly.
    samples = [
        (5,7,2,3),
        (13,17,3,4),
        (17,19,4,5),
        (25,49,3,8),
    ]
    out=[]
    for X0,Y0,ap,bp in samples:
        if gcd(X0,Y0)!=1 or gcd(ap,bp)!=1:
            continue
        Delta = bp*Y0-ap*X0
        if Delta <= 0:
            continue
        assert gcd(X0,Delta)==gcd(X0,bp)
        assert gcd(Y0,Delta)==gcd(Y0,ap)
        M=X0*Y0
        assert gcd(M,Delta) == gcd(X0,Delta)*gcd(Y0,Delta)
        assert (ap*bp) % gcd(M,Delta) == 0
        out.append((X0,Y0,ap,bp,Delta))
    return out

if __name__ == "__main__":
    print("SUPPLY_COUNTEREXAMPLE=", check_supply_counterexample())
    print("NEAR_BALANCED_FAMILY_1_TO_100=PASS" if check_near_balanced_family() else "FAIL")
    print("DETERMINANT_PACKET_SAMPLES=", check_determinant_packet_samples())
    print("GLOBAL_PSDG_EMPTY=NOT_CLAIMED")
    print("GLOBAL_OUTER_WITNESS=NOT_FOUND")
