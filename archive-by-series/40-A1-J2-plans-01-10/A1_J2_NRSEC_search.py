#!/usr/bin/env python3
"""Exact targeted certificate for the J=2, g>=2, S_R<0 terminal system.

This script does NOT enumerate original concatenation states.  It uses the
proved negative-J2 c-z compression and the rigorous UZ bound.  For g=2,3 it
covers every admissible divisor u|(10^g+1), every sign/face-compatible k,
every actual third primitive digit 1<=C3<10^g, and every positive ten-unit z
allowed by the UZ theorem.  Each remaining cell is tested by the exact sphere
quadratic, integer-square discriminant, integral-root divisibility, primitive
reconstruction, and the actual common-U digit/coprimality gate.
"""
from fractions import Fraction
from math import gcd, isqrt

# Rigorous rational majorant:
# 2.532*sqrt(101/96) < 2.598 = 1299/500,
# because 2.598^2 - 2.532^2*(101/96) = 1869/400000 > 0.
ETA_HAT = Fraction(1299, 500)


def divisors(n: int):
    out = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
        d += 1
    return sorted(out)


def unit10(n: int) -> bool:
    return gcd(abs(n), 10) == 1


def strict_integer_ceiling_minus_one(x: Fraction) -> int:
    """Largest integer z with z < x."""
    return (x.numerator - 1) // x.denominator


def radial_units(G, K, u, C2, C3):
    # n2=2g+k and n3=g, so digit windows are exact.
    lo2, hi2 = G*G*K//10, G*G*K
    lo3, hi3 = G//10, G
    Ulo = max((lo2 + C2 - 1)//C2, (lo3 + C3 - 1)//C3, 1)
    Uhi = min((hi2 - 1)//C2, (hi3 - 1)//C3)
    if Ulo > Uhi:
        return []
    V = u * G * (G//2)
    return [U for U in range(Ulo, Uhi+1) if gcd(U, V) == 1]


def scan_g(g: int):
    G = 10**g
    H = G//2
    allowed = []
    stats = {
        "cz_cells": 0,
        "linear_positive": 0,
        "disc_nonnegative": 0,
        "square_discriminant": 0,
        "integral_C1_roots": 0,
        "exact_primitive_states": 0,
        "radial_U_survivors": 0,
    }
    per_uk = []
    survivor_ledger = []

    # S_R<0 is the old plus branch.  Frozen face bounds give
    # k-2g<=0 on Face A and <=1 on Face B, hence union: 1<=k<=2g+1.
    for u in divisors(G+1):
        q = (G+1)//u
        A = 2*u + 1
        B = 2*G + q
        # Exact J2.5 with m,C2 ten-units forces gcd(A,10)=1.
        if gcd(A, 10) != 1:
            continue
        allowed.append((u, q, A, B))
        for k in range(1, 2*g + 2):
            K = 10**k
            # Proven UZ bound, weakened only by U>=1 and eta<ETA_HAT:
            # z < 2*ETA_HAT*u/K + 2*u*A/G.
            z_bound = Fraction(2*ETA_HAT.numerator*u,
                               ETA_HAT.denominator*K) + Fraction(2*u*A, G)
            zmax = strict_integer_ceiling_minus_one(z_bound)
            local_cells = 0
            local_squares = 0
            local_roots = 0
            local_exact = 0
            local_radial = 0

            for z in range(1, zmax+1):
                if not unit10(z):
                    continue
                # Negative c-z normal form:
                # w = G*H*z-u*A*c >0 is the stronger linear positivity gate.
                # h=q*H*z-A*c>0 then follows automatically because G/u<q.
                cmax = min(G-1, (G*H*z - 1)//(u*A))
                for c in range(1, cmax+1):
                    if not unit10(c):
                        continue
                    local_cells += 1
                    stats["cz_cells"] += 1

                    h = q*H*z - A*c
                    w = G*H*z - u*A*c
                    m = A*h - G*z
                    r = H*h - u*c
                    d2 = u*c + G*w
                    if min(h, w, m, r, d2) <= 0:
                        continue
                    # These are automatic from the normal form when A,c,z are
                    # ten-units, but retain them as an implementation audit.
                    if not all(unit10(x) for x in (h, w, m, r, d2)):
                        raise AssertionError("ten-unit propagation failed")
                    stats["linear_positive"] += 1

                    # Eliminate T from 2uKC1 = A T + z and the sphere:
                    # A H^2 C1^2 - 2uK d2 C1 + A w^2 + z d2 = 0.
                    Delta0 = (u*u*K*K*d2*d2
                              - A*H*H*(A*w*w + z*d2))
                    if Delta0 < 0:
                        continue
                    stats["disc_nonnegative"] += 1
                    R = isqrt(Delta0)
                    if R*R != Delta0:
                        continue
                    stats["square_discriminant"] += 1
                    local_squares += 1

                    den = A*H*H
                    for num in (u*K*d2 + R, u*K*d2 - R):
                        if num <= 0 or num % den != 0:
                            continue
                        C1 = num//den
                        stats["integral_C1_roots"] += 1
                        local_roots += 1

                        numC2 = G*K*C1 - m
                        if numC2 % A:
                            continue
                        C2 = numC2//A
                        numT = u*C2 + w
                        if numT % H:
                            continue
                        T = numT//H
                        if C2 <= 0 or T <= 0:
                            continue
                        if gcd(C1, u) != 1 or gcd(C2, H) != 1 or gcd(c, G*H) != 1:
                            continue
                        if H*H*C1*C1 + w*w != T*d2:
                            continue

                        P1 = G*H*C1
                        P2 = u*G*C2
                        P3 = u*c
                        Q0 = P2 + d2
                        D = H*C2 + r
                        if P1*K - Q0 != D:
                            continue
                        if P1*P1 + P2*P2 + P3*P3 != Q0*Q0:
                            continue
                        if gcd(gcd(gcd(P1, P2), P3), Q0) != 1:
                            continue
                        if Q0 - P3 != G*H*T:
                            continue

                        stats["exact_primitive_states"] += 1
                        local_exact += 1
                        Us = radial_units(G, K, u, C2, c)
                        if Us:
                            stats["radial_U_survivors"] += len(Us)
                            local_radial += len(Us)
                            survivor_ledger.append({
                                "g": g, "u": u, "q": q, "k": k,
                                "C3": c, "z": z, "h": h, "w": w,
                                "m": m, "r": r, "d2": d2,
                                "C1": C1, "C2": C2, "T": T,
                                "Q0": Q0, "U": Us,
                            })

            per_uk.append({
                "u": u, "q": q, "k": k,
                "z_bound": str(z_bound), "zmax": zmax,
                "cz_cells": local_cells,
                "square_discriminant": local_squares,
                "integral_C1_roots": local_roots,
                "exact_primitive_states": local_exact,
                "radial_U_survivors": local_radial,
            })

    return allowed, per_uk, stats, survivor_ledger



def scan_g_positive(g: int):
    """Exact low-g audit for S_R>0 after the negative campaign succeeded.

    Uses the same c-z compression.  Here w=u*A*c-G*H*z>0 and inherited
    RRGS gives 0<U*w<u.  Since U*c<G, this implies the rigorous finite bound
    z < 2*u*A/G.  Frozen positive face bounds give 2g-1<=k<=3g-1.
    """
    G = 10**g
    H = G//2
    stats = {
        "cz_cells": 0,
        "linear_positive": 0,
        "square_discriminant": 0,
        "integral_C1_roots": 0,
        "exact_primitive_states": 0,
        "radial_U_survivors": 0,
    }
    per_uk = []
    survivor_ledger = []
    allowed = []
    for u in divisors(G+1):
        q = (G+1)//u
        A = 2*u+1
        B = 2*G+q
        if gcd(A,10) != 1:
            continue
        allowed.append((u,q,A,B))
        for k in range(max(1,2*g-1), 3*g):
            K=10**k
            z_bound=Fraction(2*u*A,G)
            zmax=strict_integer_ceiling_minus_one(z_bound)
            local_cells=local_linear=local_squares=local_roots=local_exact=local_radial=0
            for z in range(1,zmax+1):
                if not unit10(z):
                    continue
                # w=u*A*c-G*H*z>0 and h=q*H*z-A*c>0.
                cmin=(G*H*z)//(u*A)+1
                cmax=min(G-1,(q*H*z-1)//A)
                for c in range(cmin,cmax+1):
                    if not unit10(c):
                        continue
                    stats["cz_cells"]+=1; local_cells+=1
                    h=q*H*z-A*c
                    w=u*A*c-G*H*z
                    m=A*h-G*z
                    r=H*h-u*c
                    d2=u*c-G*w
                    if min(h,w,m,r,d2)<=0:
                        continue
                    if not all(unit10(x) for x in (h,w,m,r,d2)):
                        raise AssertionError("positive ten-unit propagation failed")
                    stats["linear_positive"]+=1; local_linear+=1
                    Delta0=(u*u*K*K*d2*d2-A*H*H*(A*w*w+z*d2))
                    if Delta0<0:
                        continue
                    R=isqrt(Delta0)
                    if R*R!=Delta0:
                        continue
                    stats["square_discriminant"]+=1; local_squares+=1
                    den=A*H*H
                    for num in (u*K*d2+R,u*K*d2-R):
                        if num<=0 or num%den:
                            continue
                        C1=num//den
                        stats["integral_C1_roots"]+=1; local_roots+=1
                        numC2=G*K*C1-m
                        if numC2%A:
                            continue
                        C2=numC2//A
                        if (u*C2-w)%H:
                            continue
                        T=(u*C2-w)//H
                        if C2<=0 or T<=0:
                            continue
                        if gcd(C1,u)!=1 or gcd(C2,H)!=1 or gcd(c,G*H)!=1:
                            continue
                        if H*H*C1*C1+w*w!=T*d2:
                            continue
                        P1=G*H*C1; P2=u*G*C2; P3=u*c; Q0=P2+d2
                        D=H*C2+r
                        if P1*K-Q0!=D:
                            continue
                        if P1*P1+P2*P2+P3*P3!=Q0*Q0:
                            continue
                        if gcd(gcd(gcd(P1,P2),P3),Q0)!=1:
                            continue
                        if Q0-P3!=G*H*T:
                            continue
                        stats["exact_primitive_states"]+=1; local_exact+=1
                        Us=[U for U in radial_units(G,K,u,C2,c) if U*w<u]
                        if Us:
                            stats["radial_U_survivors"]+=len(Us); local_radial+=len(Us)
                            survivor_ledger.append({"g":g,"u":u,"q":q,"k":k,"C3":c,"z":z,"U":Us})
            per_uk.append({"u":u,"q":q,"k":k,"z_bound":str(z_bound),"zmax":zmax,
                           "cz_cells":local_cells,"linear_positive":local_linear,
                           "square_discriminant":local_squares,"integral_C1_roots":local_roots,
                           "exact_primitive_states":local_exact,"radial_U_survivors":local_radial})
    return allowed,per_uk,stats,survivor_ledger

def main():
    print("A1 J2 NRSEC exact targeted certificate")
    print("ETA_MAJORANT=1299/500")
    print("ETA_SQUARE_MARGIN=1869/400000")
    print("SEARCH_G=2,3")
    all_survivors=[]
    for g in (2,3):
        allowed,per_uk,stats,survivors=scan_g(g)
        print(f"\nNEGATIVE_SECTION g={g} G={10**g}")
        print("ALLOWED_(u,q,A,B)=",allowed)
        print(f"K_RANGE=1..{2*g+1}")
        for row in per_uk:
            print("NEG_UK",row)
        print("NEG_TOTAL",stats)
        print("NEG_SURVIVOR_LEDGER",survivors)
        all_survivors.extend(survivors)

        allowed_p,per_uk_p,stats_p,survivors_p=scan_g_positive(g)
        print(f"\nPOSITIVE_SECTION g={g} G={10**g}")
        print("ALLOWED_(u,q,A,B)=",allowed_p)
        print(f"K_RANGE={max(1,2*g-1)}..{3*g-1}")
        for row in per_uk_p:
            print("POS_UK",row)
        print("POS_TOTAL",stats_p)
        print("POS_SURVIVOR_LEDGER",survivors_p)
        all_survivors.extend(survivors_p)

    print("\nGLOBAL_RADIAL_SURVIVOR_COUNT=",len(all_survivors))
    print("GLOBAL_SURVIVOR_LEDGER=",all_survivors)
    if all_survivors:
        raise SystemExit("NONZERO SURVIVORS")
    print("CERTIFICATE_STATUS=PASS")


if __name__ == "__main__":
    main()
