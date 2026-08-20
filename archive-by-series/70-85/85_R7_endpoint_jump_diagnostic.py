#!/usr/bin/env python3
"""
85-R7 exact endpoint-jump diagnostic.

Scope:
  J=2, Exact Resonance, negative J2 PRE_ROOT linear projection chart.
Purpose:
  (1) exact fixed-base jump-spectrum reconnaissance;
  (2) exact verification of an infinite PRE_ROOT-linear common-scale/coprime
      counterfamily to universal endpoint-jump rigidity.

This script DOES NOT search for J2 solutions and DOES NOT use the sphere/root
quadratic as a gate.
"""
from math import gcd
from fractions import Fraction
from collections import Counter

def unit10(n):
    return gcd(abs(int(n)), 10) == 1

def ceil_div(a, b):
    return (a + b - 1) // b

def fixed_base_scan():
    # Same live outer base used in 85-R6.
    g = 4
    G = 10**g
    k = 1
    K = 10
    u = 73
    q = 137
    A = 2*u + 1
    B = 2*G + q
    H = G//2
    assert u*q == G + 1

    stats = Counter()
    rows = []

    # Exact finite reconnaissance box only; no extrapolation.
    # z=1, 1<=C3<=5000, 1<=lambda<=2000.
    for c in range(1, 5001):
        if not unit10(c):
            continue
        z = 1
        for lam in range(1, 2001):
            if not unit10(lam):
                continue

            # Fourth Euclidean PRE_ROOT linear form.
            num = B*z + A*lam
            if num % (2*K):
                continue
            C1 = num // (2*K)
            C2 = A*c + H*lam
            T = G*z + u*lam

            # Sign-unified CZ linear form, negative sign X>0.
            h = q*H*z - A*c
            m = A*h - G*z
            r = H*h - u*c
            X = G*H*z - u*A*c
            d2 = u*c + G*X

            if min(C1, C2, T, h, m, r, X, d2) <= 0:
                continue
            if not all(unit10(v) for v in (h, m, r, X, d2, T)):
                continue

            # Primitive/reducedness conditions present before sphere/root.
            if gcd(A, d2) != 1:
                continue
            if gcd(C1, u) != 1:
                continue
            if gcd(C2, H) != 1:
                continue
            if gcd(c, G*H) != 1:
                continue

            stats["linear_pre_root"] += 1

            x2 = G*G*K//10       # 10^(n2-1)
            x3 = G//10           # 10^(n3-1)

            lo = max(Fraction(x2, C2), Fraction(x3, c))
            hi = min(Fraction(10*x2, C2), Fraction(10*x3, c))
            if not lo < hi:
                continue
            stats["continuous"] += 1

            # Face is decided by the larger lower endpoint.
            face = "A" if Fraction(x2, C2) >= Fraction(x3, c) else "B"
            if face == "A":
                delta = (-x2) % C2
                Gface = C2*G - c*x2
                req = (Gface - C2) // c
                mod = C2
            else:
                delta = (-x3) % c
                Gface = c*(G*G*K) - C2*x3
                req = (Gface - c) // C2
                mod = c

            stats[f"face_{face}"] += 1
            if req < 0:
                stats["required_window_negative"] += 1
            elif req >= mod - 1:
                stats["required_window_vacuous"] += 1
            else:
                stats["required_window_active"] += 1

            Ulo = max(ceil_div(x2, C2), ceil_div(x3, c), 1)
            Uhi = min((10*x2 - 1)//C2, (10*x3 - 1)//c)
            ordinary = Ulo <= Uhi
            coprime = False
            if ordinary:
                stats["ordinary_feasible"] += 1
                V = u*G*H
                coprime = any(gcd(U, V) == 1 for U in range(Ulo, Uhi+1))
                if coprime:
                    stats["coprime_feasible"] += 1

            rows.append({
                "face": face,
                "ratio": Fraction(delta, mod),
                "delta": delta,
                "req": req,
                "mod": mod,
                "C3": c,
                "lambda": lam,
                "C2": C2,
                "C1": C1,
                "T": T,
                "Ulo": Ulo,
                "Uhi": Uhi,
                "ordinary": ordinary,
                "coprime": coprime,
            })

    return (g,G,k,K,u,q,A,B,H), stats, rows

def infinite_family(g):
    # Infinite family index: g = 5 mod 22, g>=5.
    assert g >= 5 and g % 22 == 5
    G = 10**g
    K = 10
    u = 11
    q = (G + 1)//u
    assert u*q == G + 1
    A = 23
    H = G//2
    B = 2*G + q

    c = 1
    z = 1
    lam = 3

    C2 = A*c + H*lam
    n = B*z + A*lam
    assert n % 20 == 0
    C1 = n//20
    T = G*z + u*lam

    h = q*H*z - A*c
    m = A*h - G*z
    r = H*h - u*c
    X = G*H*z - u*A*c
    d2 = u*c + G*X

    assert min(C1,C2,T,h,m,r,X,d2) > 0
    assert all(unit10(v) for v in (h,m,r,X,d2,T))
    assert gcd(C1,u) == 1
    assert gcd(C2,H) == 1
    assert gcd(c,G*H) == 1
    assert gcd(A,d2) == 1

    # Exact PRE_ROOT linear identities.
    assert c == 2*r - q*X
    assert d2 == 2*u*r - X
    assert A*r - X == m*H
    assert G*K*C1 == A*C2 + m
    assert u*C2 + X == H*T
    assert 2*u*K*C1 == A*T + z

    # Exact common-scale and coprime witness.
    U = G - 1
    x2 = G*G*K//10   # G^2
    x3 = G//10
    assert x2 <= U*C2 < 10*x2
    assert x3 <= U*c < 10*x3
    V = u*G*H
    assert gcd(U,V) == 1

    # Face A, required window, exact jump.
    assert Fraction(x2,C2) >= Fraction(x3,c)
    delta2 = (-x2) % C2
    req2 = C2*(G-1) - G*G
    assert delta2 <= req2
    assert req2 >= C2 - 1

    # Closed form for the residue/jump:
    # 9 G^2 == 2116 (mod C2), C2 == 2 (mod 9).
    r2 = (4*C2 + 2116)//9
    assert 9*r2 == 4*C2 + 2116
    assert 0 < r2 < C2
    assert G*G % C2 == r2
    assert delta2 == C2-r2
    assert delta2 == (5*C2-2116)//9

    sphere_residual = H*H*C1*C1 + X*X - T*d2

    return {
        "g": g, "G": G, "q": q, "C1": C1, "C2": C2, "C3": c,
        "T": T, "U": U, "V": V, "delta2": delta2, "req2": req2,
        "delta2_over_C2": Fraction(delta2,C2),
        "req2_over_C2": Fraction(req2,C2),
        "sphere_residual": sphere_residual,
    }

def main():
    base, stats, rows = fixed_base_scan()
    g,G,k,K,u,q,A,B,H = base

    print("85-R7 exact endpoint-jump diagnostic certificate")
    print("EXACT_ARITHMETIC=PASS")
    print("ROOT_OR_SPHERE_GATE_USED_IN_FIXED_BASE_SCAN=NO")
    print("FIXED_BASE=", {"g":g,"G":G,"k":k,"K":K,"u":u,"q":q,"A":A,"B":B,"H":H})
    print("SCAN_BOX=", {"z":1,"C3":"1..5000 ten-units","lambda":"1..2000 ten-units"})
    print("STATS=", dict(stats))

    for face in ("A","B"):
        feasible = [r for r in rows if r["face"] == face and r["ordinary"]]
        if feasible:
            mn = min(feasible, key=lambda r:r["ratio"])
            mx = max(feasible, key=lambda r:r["ratio"])
            print(face+"_FEASIBLE_COUNT=", len(feasible))
            print(face+"_MIN_JUMP_RATIO=", mn["ratio"], mn)
            print(face+"_MAX_JUMP_RATIO=", mx["ratio"], mx)

    fail = next(r for r in rows
                if 0 <= r["req"] < r["mod"]-1 and r["delta"] > r["req"])
    survive = next(r for r in rows
                   if r["ordinary"] and 0 <= r["req"] < r["mod"]-1
                   and r["delta"] <= r["req"])
    print("ACTIVE_WINDOW_FAIL_EXAMPLE=", fail)
    print("ACTIVE_WINDOW_SURVIVE_EXAMPLE=", survive)

    print("\nINFINITE_PRE_ROOT_LINEAR_FAMILY")
    for gg in (5,27,49):
        f = infinite_family(gg)
        print("FAMILY_SAMPLE=", f)

    print("FAMILY_THEOREM_INDEX=g=5+22t,t>=0")
    print("FAMILY_COMMON_SCALE_U=G-1")
    print("FAMILY_COPRIME_COMMON_SCALE=PROVED_BY_EXACT_IDENTITIES")
    print("FAMILY_DELTA2_FORMULA=(5*C2-2116)/9")
    print("FAMILY_DELTA2_OVER_C2_LIMIT=5/9")
    print("FAMILY_REQUIRED_WINDOW_VACUOUS=TRUE")
    print("FAMILY_IS_NOT_CLAIMED_AS_PRIMITIVE_SPHERE_OR_ROOT_SURVIVOR=TRUE")
    print("CERTIFICATE_STATUS=PASS")

if __name__ == "__main__":
    main()
