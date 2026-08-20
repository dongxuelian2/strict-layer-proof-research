#!/usr/bin/env python3
"""95-R9 reduced-information outer-plus projective cancellation regression.

This is NOT a proof engine and does NOT construct full original candidates.
It verifies the explicit Smith-radial witness used to falsify the standalone
deep-d projective/common-U closure architecture.
"""
from math import gcd


def witness(r: int):
    assert r >= 1
    d = -r
    g = r + 1
    k = 1

    m2 = g + d
    n2 = 2 * g + k + d
    n3 = n2
    m3 = n3 + g

    # Smith data: s=alpha=beta=t=u=u0=1.
    alpha = t = u0 = 1
    v = 10 ** (n3 - d)

    b2 = 1
    b3 = v
    M = N = 1

    g2 = u0 * v
    g3 = u0 * alpha * t
    P2 = v * M
    P3 = alpha * t * N
    C2 = M // u0
    C3 = N // u0

    V = v
    U = 10 ** (n2 - 1) + 1

    assert m2 == 1
    assert len(str(b2)) == m2
    assert len(str(b3)) == m3
    assert len(str(U * C2)) == n2
    assert len(str(U * C3)) == n3
    assert gcd(U, V) == 1

    # sigma=rho=1 exactly.
    assert v == 10 ** (n3 - d)
    assert M == N
    assert n2 == n3

    # Exact projective ratio.
    assert P2 == 10 ** (2 * g + k) * P3

    return {
        "r": r,
        "d": d,
        "g": g,
        "k": k,
        "m2": m2,
        "n2": n2,
        "n3": n3,
        "m3": m3,
        "P2_over_P3": 10 ** (2 * g + k),
        "U": U,
        "V": V,
    }


if __name__ == "__main__":
    for r in range(1, 9):
        row = witness(r)
        print(row)
