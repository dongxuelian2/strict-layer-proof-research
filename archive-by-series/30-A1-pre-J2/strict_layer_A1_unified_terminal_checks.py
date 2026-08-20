#!/usr/bin/env python3
"""Exact regression checks for the A1 unified moving-profile terminal campaign.

This script is NOT a proof engine.  It checks algebraic identities and the
sharpness/counterexample examples used in the report with exact integer or
Fraction arithmetic.
"""
from fractions import Fraction
from math import gcd


def digits(n: int) -> int:
    return len(str(n))


def interval(U: int, C2: int, C3: int):
    a2, a3 = U * C2, U * C3
    n2, n3 = digits(a2), digits(a3)
    L2 = Fraction(10 ** (n2 - 1), C2)
    R2 = Fraction(10 ** n2, C2)
    L3 = Fraction(10 ** (n3 - 1), C3)
    R3 = Fraction(10 ** n3, C3)
    return n2, n3, max(L2, L3), min(R2, R3)


def radial_margin(U: int, C2: int, C3: int):
    a2, a3 = U * C2, U * C3
    n2, n3 = digits(a2), digits(a3)
    w_minus = 10 ** n3 * C2 - 10 ** (n2 - 1) * C3
    w_plus = 10 ** n2 * C3 - 10 ** (n3 - 1) * C2
    assert w_minus >= C2
    assert w_plus >= C3
    return n2, n3, w_minus, w_plus


def exhaustive_margin_check(limit_u=30, limit_c=120):
    eq_minus = []
    eq_plus = []
    for U in range(1, limit_u + 1):
        for C2 in range(1, limit_c + 1):
            for C3 in range(1, limit_c + 1):
                n2, n3, wm, wp = radial_margin(U, C2, C3)
                if wm == C2:
                    eq_minus.append((U, C2, C3, n2, n3))
                if wp == C3:
                    eq_plus.append((U, C2, C3, n2, n3))
    # In this box, equality is seen only at U=1, as predicted by the proof.
    assert all(row[0] == 1 for row in eq_minus + eq_plus)
    return eq_minus, eq_plus


def regression_real_cone_point():
    # From the fixed synchronized regression conic report.
    C2, C3, n2, n3 = 17813, 2633, 2, 1
    L2 = Fraction(10 ** (n2 - 1), C2)
    R2 = Fraction(10 ** n2, C2)
    L3 = Fraction(10 ** (n3 - 1), C3)
    R3 = Fraction(10 ** n3, C3)
    L, R = max(L2, L3), min(R2, R3)
    wm = 10 ** n3 * C2 - 10 ** (n2 - 1) * C3
    wp = 10 ** n2 * C3 - 10 ** (n3 - 1) * C2
    assert wm >= C2 and wp >= C3
    assert 0 < L < R < 1  # margins hold, but there is no positive integer U.
    return L, R, wm, wp


def synchronized_polynomial_family(t: int):
    # Frozen family from the generic primitive-defect synchronization report.
    X = 3_553_056*t*t + 160_341*t + 1_809
    Y = 44_000_352*t*t + 2_018_892*t + 23_153
    Z = 188_129_520*t*t + 8_492_928*t + 95_849
    Q = 597_312_720*t*t + 27_003_264*t + 305_197
    d = gcd(gcd(X, Y), gcd(Z, Q))
    x, y, z, q = X//d, Y//d, Z//d, Q//d
    P1, P2, P3 = 24*x, 4*y, 3*z
    assert P1*P1 + P2*P2 + P3*P3 == q*q
    assert gcd(gcd(P1, P2), gcd(P3, q)) == 1
    theta = q - P2
    assert theta > 0
    return P1, P2, P3, q, theta


def family_axis_gap_check():
    rows = []
    last_theta = 0
    for t in range(1, 8):
        P1, P2, P3, Q0, theta = synchronized_polynomial_family(t)
        rows.append((t, Q0, theta, Fraction(theta, Q0)))
        # The primitive reduction factor can jump, so monotonicity is not used.
        assert theta > 0
        last_theta = theta
    # The raw leading-coefficient ratio gives a positive asymptotic fraction.
    theta_ratio_limit = Fraction(597_312_720 - 4*44_000_352, 597_312_720)
    assert theta_ratio_limit > Fraction(7, 10)
    return rows, theta_ratio_limit


def main():
    em, ep = exhaustive_margin_check()
    L, R, wm, wp = regression_real_cone_point()
    rows, lim = family_axis_gap_check()
    print("Integer radial margin exhaustive check: PASS")
    print(f"  equality samples: lower={len(em)}, upper={len(ep)} (all U=1 in search box)")
    print("Regression real-cone point:")
    print(f"  I23=[{float(L):.9g}, {float(R):.9g}), so R<1")
    print(f"  margin defects: omega_-={wm}, omega_+={wp}")
    print("Synchronized polynomial pseudo-family axis gaps:")
    for t, Q0, theta, ratio in rows:
        print(f"  t={t}: Q0={Q0}, Theta={theta}, Theta/Q0={float(ratio):.9f}")
    print(f"  leading Theta/Q0 limit = {float(lim):.9f}")


if __name__ == '__main__':
    main()
