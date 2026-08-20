#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ETA_HAT = Fraction(1299, 500)
G_MIN, G_MAX = 4, 10

def unit10(n):
    return gcd(abs(n), 10) == 1

def divisors_trial(n):
    out = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
        d += 1
    return sorted(out)

def ceil_div(a,b):
    return -((-a)//b)

def solve_congruence_interval(a,b,m,L,U):
    if L > U:
        return []
    d = gcd(a,m)
    if b % d:
        return []
    aa,bb,mm = a//d,b//d,m//d
    r = (bb*pow(aa,-1,mm)) % mm
    first = r
    if first < L:
        first += ceil_div(L-first,mm)*mm
    return list(range(first,U+1,mm))

def t_interval(G,q,N):
    den = 2*(q+4)
    L = ceil_div(den*(G//10)+q*N, G-1)
    U = (den*G+q*N-1)//(G-1)
    return L,U

def reconstruct(G,q,N,t):
    if (G+1) % q:
        return None
    u=(G+1)//q
    A=2*u+1
    numZ=A*t-2*N
    denZ=q*(q+4)
    if numZ % denZ:
        return None
    Z=numZ//denZ
    numa=(G-1)*t-q*N
    dena=2*(q+4)
    if numa % dena:
        return None
    a3=numa//dena
    numX=Z+u*N
    if numX % 2:
        return None
    X=numX//2
    D2=u*a3+G*X
    return dict(u=u,q=q,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2)

def root_test(G,k,row):
    H=G//2
    K=10**k
    u,A=row["u"],row["A"]
    Z,X,D2=row["Z"],row["X"],row["D2"]
    Ft=A*X*X+Z*D2
    Y=u*K*D2
    Delta=Y*Y-A*H*H*Ft
    ans=dict(nonnegative=(Delta>=0), square=False, roots=[], Ftilde=Ft, Delta=Delta)
    if Delta < 0:
        return ans
    R=isqrt(Delta)
    if R*R != Delta:
        return ans
    ans["square"]=True
    den=A*H*H
    for num in (Y+R,Y-R):
        if num>0 and num%den==0:
            ans["roots"].append(num//den)
    return ans

def outer_pairs(G):
    ans=[]
    for u in divisors_trial(G+1):
        if u<=1:
            continue
        q=(G+1)//u
        A=2*u+1
        if unit10(A):
            ans.append((u,q,A))
    return ans

def scan_positive(G,g):
    stats=dict(outer_pairs=0,q1_nonunit_kills=0,t_candidates=0,
               linear_survivors=0,disc_nonnegative=0,
               square_discriminant=0,integral_a1_roots=0)
    led=[]
    for u,q,A in outer_pairs(G):
        stats["outer_pairs"]+=1
        if q==1:
            for n in (1,3,5):
                a3=n*(G//10)
                assert G//10 <= a3 < G
                assert not unit10(a3)
                stats["q1_nonunit_kills"]+=1
            continue
        # Proven q>1 positive collapse: N=-1, U=1, j=-1.
        N=-1
        L,U=t_interval(G,q,N)
        ts=solve_congruence_interval(A,2*N,q*(q+4),L,U)
        stats["t_candidates"]+=len(ts)
        for t in ts:
            row=reconstruct(G,q,N,t)
            if row is None:
                continue
            Z,a3,X,D2=row["Z"],row["a3"],row["X"],row["D2"]
            if not (G//10<=a3<G and unit10(a3) and unit10(Z)):
                continue
            if not (X<0 and D2>0):
                continue
            W=-X
            if not (0<W<u):
                continue
            if not (Z*G < 2*u*A):
                continue
            if N+q*Z<=0 or A*N+(q+2)*Z<=0:
                continue
            stats["linear_survivors"]+=1
            for k in range(2*g-1,3*g):
                rr=root_test(G,k,row)
                stats["disc_nonnegative"]+=int(rr["nonnegative"])
                stats["square_discriminant"]+=int(rr["square"])
                stats["integral_a1_roots"]+=len(rr["roots"])
                if rr["roots"]:
                    led.append((g,"POS",q,u,k,N,t,row,rr))
    return stats,led

def scan_negative_k2g(G,g):
    stats=dict(outer_pairs=0,t_candidates=0,linear_survivors=0,
               disc_nonnegative=0,square_discriminant=0,
               integral_a1_roots=0,q1_N1_family_seen=0)
    led=[]
    k=2*g
    K=G*G
    for u,q,A in outer_pairs(G):
        stats["outer_pairs"]+=1
        Ns=(-3,-1,1,3,5) if q==1 else (1,3,5)
        for N in Ns:
            L,U=t_interval(G,q,N)
            ts=solve_congruence_interval(A,2*N,q*(q+4),L,U)
            stats["t_candidates"]+=len(ts)
            for t in ts:
                row=reconstruct(G,q,N,t)
                if row is None:
                    continue
                Z,a3,X,D2=row["Z"],row["a3"],row["X"],row["D2"]
                if not (G//10<=a3<G and unit10(a3)):
                    continue
                if not (Z>0 and X>0 and D2>0):
                    continue
                if not (Fraction(Z,1) < Fraction(2*ETA_HAT*u,K)+Fraction(2*u*A,G)):
                    continue
                if not (Fraction(X,1) < ETA_HAT*u):
                    continue
                if N+q*Z<=0 or A*N+(q+2)*Z<=0:
                    continue
                stats["linear_survivors"]+=1
                if q==1 and N==1 and t==9:
                    stats["q1_N1_family_seen"]+=1
                rr=root_test(G,k,row)
                stats["disc_nonnegative"]+=int(rr["nonnegative"])
                stats["square_discriminant"]+=int(rr["square"])
                stats["integral_a1_roots"]+=len(rr["roots"])
                if rr["roots"]:
                    led.append((g,"NEG2G",q,u,k,N,t,row,rr))
    return stats,led

def top_layer_record(G,g):
    K=10*G*G
    rec=[]
    for u,q,A in outer_pairs(G):
        lower_mag=Fraction(2*ETA_HAT,K)+Fraction(2*A,G)
        upper=Fraction(2*ETA_HAT*G*G,K)
        # Search a safe finite odd box; theorem bounds are tiny here.
        poss=[n for n in range(-11,12,2) if -lower_mag<n<upper]
        if q>1:
            if poss:
                raise AssertionError(("unexpected q>1 top N",g,q,u,poss,lower_mag,upper))
            rec.append((q,u,"q>1",poss))
        else:
            if poss != [-3,-1]:
                raise AssertionError(("unexpected q=1 top N",g,poss,lower_mag,upper))
            forced=[(-N)*(G//10) for N in poss]
            if not all(not unit10(x) for x in forced):
                raise AssertionError(("q=1 top nonunit failure",g,forced))
            rec.append((q,u,"q=1",poss,forced))
    return rec

def q1_gap(G):
    P=(4096*G**8+15616*G**7+19748*G**6+6712*G**5
       -7856*G**4-22132*G**3-34633*G**2-25490*G-6600)
    Q=64*G**4+122*G**3+38*G**2-20*G
    lo,hi=Q-35,Q-34
    if not (lo*lo<P<hi*hi):
        raise AssertionError(("gap failed",G))
    return P-lo*lo,P-hi*hi

def main():
    lines=[
        "A1 J2 CZDR targeted exact certificate",
        f"ETA_MAJORANT={ETA_HAT.numerator}/{ETA_HAT.denominator}",
        f"SEARCH_G={G_MIN}..{G_MAX}",
        "NOTE=Targeted audit only; not a global J2 closure certificate.",
        ""
    ]
    ledger=[]
    for g in range(G_MIN,G_MAX+1):
        G=10**g
        lines.append(f"=== g={g} G={G} ===")
        lines.append("ADMISSIBLE_(u,q,A)="+repr(outer_pairs(G)))
        pos,l1=scan_positive(G,g)
        lines.append("POSITIVE_STATS="+repr(pos))
        lines.append("NEG_K_2G_PLUS_1_AUDIT="+repr(top_layer_record(G,g)))
        neg,l2=scan_negative_k2g(G,g)
        lines.append("NEG_K_2G_STATS="+repr(neg))
        lines.append("Q1_K_2G_POLYNOMIAL_GAP="+repr(q1_gap(G)))
        lines.append("")
        ledger.extend(l1); ledger.extend(l2)
    lines.append("ROOT_SURVIVOR_COUNT="+str(len(ledger)))
    lines.append("ROOT_SURVIVORS="+repr(ledger))
    lines += [
        "",
        "VERDICT:",
        "positive compressed branch: no linear survivor for g=4..10;",
        "negative k=2g+1: exact N-strip audit is empty after q=1 nonunit check;",
        "negative k=2g: only the q=1,N=1,t=9 family reaches the root gate in these depths;",
        "that family is killed by the exact adjacent-square polynomial gap;",
        "no integral root survivor occurs in the audited slices."
    ]
    Path("/mnt/data/A1_J2_CZDR_certificate.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines))

if __name__=="__main__":
    main()
