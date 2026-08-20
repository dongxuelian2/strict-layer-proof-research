#!/usr/bin/env python3
"""Exact verification for the Phase-II R2 live deep countermodel.

Default: verify the displayed witness.
Optional --scan: reproduce the finite tangent-directed guillotine diagnostic.
No floating-point arithmetic is used.
"""
from math import gcd, isqrt
from functools import reduce
from itertools import product
import sys

g, k, u = 4, 1, 73
G, K = 10**g, 10**k
H = G // 2
q = (G + 1) // u
A = 2*u + 1
B = 2*G + q
V = u*G*H

c = 33924239254903883018463510772486609118378145469
z = 7320435422750314882891089365044594394569109
lam = 65244544113530337755581044004304642533979621

def ceil_div(a, b):
    return (a+b-1)//b

def phi(v):
    cc, zz, ll = v
    ww = G*H*zz - u*A*cc
    TT = G*zz + u*ll
    dd = u*cc + G*ww
    return G*G*(B*zz + A*ll)**2 + 16*K*K*ww*ww - 16*K*K*TT*dd

def polar(x, y):
    return phi(tuple(x[i]+y[i] for i in range(3))) - phi(x) - phi(y)

def ledger(v):
    cc, zz, ll = v
    if min(v) <= 0:
        return None
    n = B*zz + A*ll
    if n % (2*K):
        return None
    C1 = n // (2*K)
    C2 = A*cc + H*ll
    T = G*zz + u*ll
    h = q*H*zz - A*cc
    m = A*h - G*zz
    r = H*h - u*cc
    w = G*H*zz - u*A*cc
    d2 = u*cc + G*w
    if min(C1,C2,T,h,m,r,w,d2) <= 0:
        return None
    if gcd(cc*zz*ll,10) != 1:
        return None
    if gcd(h*m*r*w*T*d2,10) != 1:
        return None
    if gcd(A,d2) != 1:
        return None
    if gcd(C1,u) != 1 or gcd(C2,H) != 1 or gcd(cc,G*H) != 1:
        return None
    P1 = G*H*C1
    P2 = u*G*C2
    P3 = u*cc
    Q0 = P2 + d2
    primitive = reduce(gcd,[P1,P2,P3,Q0])
    Ulo = max(ceil_div(G*G*K,10*C2), ceil_div(G,10*cc), 1)
    Uhi = min((G*G*K-1)//C2, (G-1)//cc)
    return {
        "C1":C1,"C2":C2,"T":T,"h":h,"m":m,"r":r,"w":w,"d2":d2,
        "P1":P1,"P2":P2,"P3":P3,"Q0":Q0,
        "primitive":primitive,"Ulo":Ulo,"Uhi":Uhi
    }

def verify():
    assert u*q == G+1
    L = ledger((c,z,lam))
    assert L is not None
    assert L["primitive"] == 1
    assert phi((c,z,lam)) == 0

    W = G*G*z - 2*u*A*c
    D = G*W + 2*u*c
    N0 = 4*u*u*G*G*K*K - (G*A+1)**2 + 2
    alpha = 4*u*u*(4*K*K*u*u*(G*A-1)**2 - G*G*A**4)
    beta = -4*G*G*u*(A*N0 + G*A*A - 4*G*K*K*u*u)
    gamma = G**4*(N0-1)
    Q = alpha*c*c + beta*c*z + gamma*z*z
    Q2 = 4*u*u*K*K*D*D - A*G*G*(A*W*W + 2*z*D)
    assert Q == Q2
    Z = isqrt(Q)
    assert Z*Z == Q
    assert Z % 4 == 0
    Y0 = Z//4

    denom = A*H*H
    assert (u*K*L["d2"] + Y0) % denom == 0
    assert (u*K*L["d2"] + Y0)//denom == L["C1"]
    assert (2*K*L["C1"] - B*z) % A == 0
    assert (2*K*L["C1"] - B*z)//A == lam

    disc = beta*beta - 4*alpha*gamma
    assert disc == (4*G*G*u*A)**2 * N0

    assert L["Ulo"] == 1 and L["Uhi"] == 0
    assert gcd(c,z) == 1

    print("WITNESS_VERIFY=PASS")
    print("g,k,u,q =", g,k,u,q)
    print("N0 =", N0)
    print("Z =", Z)
    print("C1 =", L["C1"])
    print("C2 =", L["C2"])
    print("FULL_PRIMITIVE_GCD =", L["primitive"])
    print("Ulo,Uhi =", L["Ulo"],L["Uhi"])
    print("FIRST_FAILURE=COMMON_U_RADIAL_DIGIT_INTERVAL")

def scan():
    p = (
        44166648285459361797000000,
        9530621959721527629285,
        84945551173868016406925,
    )
    t0 = (
        23670799965621880000,
        5106933501050287,
        20440414109336223,
    )
    assert phi(p) == 0
    assert polar(p,t0) == 0
    assert (B*t0[1]+A*t0[2]) % (2*K) == 0

    seen=set()
    exact=deep=prim=commonU=0
    for M in range(1,81):
        for ec,ez,er in product(range(-5,6), repeat=3):
            if ec==ez==er==0:
                continue
            e=(ec,ez,9*ez+20*er)
            y=tuple(M*t0[i]+e[i] for i in range(3))
            py=phi(y)
            bpy=polar(p,y)
            P=tuple(py*p[i]-bpy*y[i] for i in range(3))
            if P==(0,0,0):
                continue
            d=reduce(gcd,map(abs,P))
            P=tuple(v//d for v in P)
            if P[0] < 0:
                P=tuple(-v for v in P)
            if P in seen:
                continue
            seen.add(P)
            assert phi(P)==0
            exact += 1
            L=ledger(P)
            if L is None:
                continue
            deep += 1
            if L["primitive"] != 1:
                continue
            prim += 1
            if L["Ulo"] <= L["Uhi"]:
                if any(gcd(U,V)==1 for U in range(L["Ulo"],L["Uhi"]+1)):
                    commonU += 1

    print("UNIQUE_EXACT_ROOT_POINTS =", exact)
    print("PASS_THROUGH_COMMON_V_TENUNIT_REGULAR =", deep)
    print("PASS_FULL_PRIMITIVE =", prim)
    print("PASS_COMMON_U =", commonU)

if __name__ == "__main__":
    verify()
    if "--scan" in sys.argv:
        scan()
