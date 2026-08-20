#!/usr/bin/env python3
"""Finite exact reconnaissance for live J2 outer bases, 4 <= g <= 8.

This is NOT a global proof.  It factors N0 exactly and applies the
sum-of-two-squares parity criterion.
"""
from math import gcd, isqrt
from collections import Counter
from sympy import factorint

def divisors(n):
    out = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
        d += 1
    return sorted(out)

def n0(G, K, u):
    A = 2*u + 1
    return 4*u*u*G*G*K*K - (G*A + 1)**2 + 2

rows = []
for g in range(4, 9):
    G = 10**g
    for u in divisors(G + 1):
        q = (G + 1)//u
        if u <= 1 or q <= 1:
            continue
        A = 2*u + 1
        if gcd(A, 10) != 1:
            continue
        for ell in range(6, 2*g):
            k = 2*g - ell
            if k < 1:
                continue
            K = 10**k
            N0 = n0(G, K, u)
            fac = factorint(N0)
            split = all(e % 2 == 0 for p, e in fac.items() if p % 4 == 3)
            if split:
                rows.append((g, k, ell, u, q))

counts = Counter(g for g, *_ in rows)

expected = [
    (4,1,7,73,137),
    (5,4,6,11,9091),
    (5,3,7,11,9091),
    (5,1,9,11,9091),
    (5,3,7,9091,11),
    (5,1,9,9091,11),
    (6,2,10,101,9901),
    (6,4,8,9901,101),
    (6,3,9,9901,101),
    (6,2,10,9901,101),
    (6,1,11,9901,101),
    (7,6,8,11,909091),
    (7,3,11,11,909091),
    (7,7,7,909091,11),
    (8,10,6,5882353,17),
    (8,9,7,5882353,17),
    (8,8,8,5882353,17),
]
assert rows == expected

print("85-R6 live N0 split-base finite scan")
print("RANGE=4<=g<=8")
print("ROOT_FILTER_USED=NO")
for g in range(4,9):
    print(f"g={g} split_base_count={counts[g]}")
for row in rows:
    print("SPLIT_BASE", row)
print("FINITE_SCAN_ONLY=TRUE")
print("CERTIFICATE_STATUS=PASS")
