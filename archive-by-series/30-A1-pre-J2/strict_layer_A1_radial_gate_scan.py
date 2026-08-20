from fractions import Fraction
from math import gcd
from functools import reduce


def lcm(a, b):
    return a // gcd(a, b) * b


def lcmm(*xs):
    return reduce(lcm, xs, 1)


def ceil_frac(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)


def check_state(b, P, *, n2, n3, m2, m3, k, g):
    b1, b2, b3 = b
    p1, p2, p3, q = P
    V = lcmm(b1, b2, b3)
    g1, g2, g3 = (V // b1, V // b2, V // b3)

    # exact master in block form
    lhs = (
        b1 * p1 * 10 ** (n2 + n3)
        + b2 * p2 * 10 ** n3
        + b3 * p3
    )
    B = b1 * 10 ** (m2 + m3) + b2 * 10 ** m3 + b3
    rhs = q * B

    sphere = p1 * p1 + p2 * p2 + p3 * p3 == q * q
    primitive = gcd(gcd(gcd(p1, p2), p3), q) == 1
    gcd_profile = [gcd(V, x) for x in (p1, p2, p3)] == [g1, g2, g3]

    D = p1 * 10 ** k - q
    H = b2 * q - b1 * 10 ** m2 * D
    K3 = Fraction(b3 * (q - p3), 10 ** n3)
    tail = K3.denominator == 1 and b2 * p2 == 10 ** g * H + K3

    C1, C2, C3 = p1 // g1, p2 // g2, p3 // g3
    L2 = Fraction(10 ** (n2 - 1), C2)
    L3 = Fraction(10 ** (n3 - 1), C3)
    L = max(L2, L3)
    R23 = min(10 * L2, 10 * L3)

    raw = []
    if L < R23:
        for u in range(max(1, ceil_frac(L)), ceil_frac(R23)):
            if Fraction(u, 1) >= L and Fraction(u, 1) < R23:
                raw.append((u, gcd(u, V)))

    RU = C2 * 10 ** (n3 - 1) - C3 * 10 ** (n2 - 1)
    AU = C3 * 10 ** (n2 - 1)
    BU = C2 * 10 ** (n3 - 1)
    GU = 10 * min(AU, BU) - max(AU, BU)

    # Verify new bridges.
    ru_bridge = (
        10 * V * RU
        == 10 ** m3 * H + b3 * (q - p3 * (1 + 10 ** n2))
    )

    if L2 >= L3:
        face = "A"
        gap_bridge = (
            V * GU
            == 10 ** m3 * H
            + b3 * (q - p3 * (1 + 10 ** (n2 - 1)))
        )
    else:
        face = "B"
        gap_bridge = (
            10 * V * GU
            == -10 ** m3 * H
            + b3 * (p3 * (10 ** (n2 + 1) + 1) - q)
        )

    return {
        "master": lhs == rhs,
        "sphere": sphere,
        "primitive": primitive,
        "gcd_profile": gcd_profile,
        "tail": tail,
        "V": V,
        "g": (g1, g2, g3),
        "C": (C1, C2, C3),
        "D": D,
        "H": H,
        "K3": K3,
        "L2": L2,
        "L3": L3,
        "I23": (L, R23),
        "face": face,
        "RU": RU,
        "GU": GU,
        "raw": raw,
        "N_raw": len(raw),
        "N_V": sum(1 for u, guv in raw if guv == 1),
        "RU_bridge": ru_bridge,
        "gap_bridge": gap_bridge,
    }


REGRESSION = [
    # b, P=(P1,P2,P3,Q0), profile
    ((1, 6, 8), (24, 52, 159, 169), dict(n2=2, n3=1, m2=1, m3=1, k=1, g=0)),
    ((1, 6, 8), (48, 436, 75, 445), dict(n2=2, n3=1, m2=1, m3=1, k=1, g=0)),
    ((1, 6, 8), (456, 292, 2907, 2957), dict(n2=2, n3=1, m2=1, m3=1, k=1, g=0)),
    ((1, 6, 8), (552, 3796, 2847, 4777), dict(n2=2, n3=1, m2=1, m3=1, k=1, g=0)),
    ((5, 5, 1), (298, 2514, 1485, 2935), dict(n2=2, n3=1, m2=1, m3=1, k=1, g=0)),
    ((5, 5, 10), (32, 264, 123, 293), dict(n2=3, n3=1, m2=1, m3=2, k=1, g=1)),
    ((7, 7, 14), (32, 264, 123, 293), dict(n2=3, n3=1, m2=1, m3=2, k=1, g=1)),
]


if __name__ == "__main__":
    for idx, (b, P, prof) in enumerate(REGRESSION, 1):
        out = check_state(b, P, **prof)
        print(f"State {idx}: b={b}, P={P}")
        for key in (
            "master", "sphere", "primitive", "gcd_profile", "tail",
            "V", "g", "C", "D", "H", "K3", "face", "RU", "GU",
            "I23", "raw", "N_raw", "N_V", "RU_bridge", "gap_bridge"
        ):
            print(f"  {key}: {out[key]}")
        print()
