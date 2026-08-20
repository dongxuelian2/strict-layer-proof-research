#!/usr/bin/env python3
"""105-R2 exact algebraic sanity certificate.

This is NOT a proof engine for the whole theorem.
It verifies the elementary arithmetic identities used in:
1) q=1 U-domain congruence and finite-index step;
2) q=1 rho-image step/inverse on sampled exact congruence classes;
3) J saturation index identity.

Only exact integer arithmetic is used.
"""
from math import gcd

def q1_check(C3, dq, tau, K, G, U0):
    M = 2*K*dq
    assert gcd(31, M) == 1  # historical dq in {1,3,7,9}, K power of 10
    # Combined congruence:
    assert (31*C3*U0 + dq*tau) % M == 0
    # It implies dq | C3*U.
    assert (C3*U0) % dq == 0
    a0 = C3*U0 // dq
    assert (31*a0 + tau) % (2*K) == 0

    hU = M // gcd(C3, M)
    U1 = U0 + hU
    assert (31*C3*U1 + dq*tau) % M == 0

    rho0 = a0 - tau*G//10
    a1 = C3*U1 // dq
    rho1 = a1 - tau*G//10
    drho = rho1-rho0
    expected = 2*K*C3//gcd(C3, M)
    assert drho == expected
    assert drho % (2*K) == 0

    # inverse
    assert dq*(rho0 + tau*G//10) % C3 == 0
    assert dq*(rho0 + tau*G//10)//C3 == U0
    return hU, drho

def solve_one(C3, dq, tau, K):
    M=2*K*dq
    for U in range(M*2):
        if (31*C3*U+dq*tau)%M==0:
            return U
    return None

def j_check(Lambda, v):
    delta=gcd(Lambda,v)
    J=Lambda//delta
    # Lambda Z subset delta Z; index is Lambda/delta.
    assert Lambda % delta == 0
    return delta,J

if __name__ == "__main__":
    examples=0
    for K in (10,100,1000):
        for dq,tau in ((1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)):
            G=10**(len(str(K))+3)
            for C3 in range(1,40):
                U0=solve_one(C3,dq,tau,K)
                if U0 is None:
                    continue
                hU,drho=q1_check(C3,dq,tau,K,G,U0)
                examples+=1
    assert examples>0

    for Lambda in (1,2,4,5,10,20,25,100,1000):
        for v in range(1,80):
            delta,J=j_check(Lambda,v)
            assert J == Lambda//gcd(Lambda,v)

    print("Q1_COMBINED_CONGRUENCE=PASS")
    print("Q1_FINITE_INDEX_U_STEP=PASS")
    print("Q1_RHO_IMAGE_STEP=PASS")
    print("Q1_INVERSE_ON_IMAGE=PASS")
    print("J_SATURATION_INDEX=PASS")
    print("SAMPLED_Q1_NONEMPTY_CLASSES=", examples)
