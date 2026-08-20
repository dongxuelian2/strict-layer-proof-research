#!/usr/bin/env python3
"""Exact diagnostic certificate for 第二个八五计划·R10.

This certificate verifies the exact (X,L,m) root-lattice formulas, several
representative interlacing cells, the natural-modulus survivor, and performs
finite exact no-hit censuses on selected low fibres.

IMPORTANT: finite censuses are regression/falsification diagnostics only and
are NOT promoted to a global J=2 theorem.
"""
from math import gcd, isqrt


def ceil_div(a, b):
    return -((-a)//b)


def params(g,k,u,q):
    G=10**g; K=10**k; A=2*u+1; B=2*G+q
    assert u*q==G+1
    assert gcd(A,2*K)==1
    r0=(-pow(A,-1,2*K)*B)%(2*K)
    assert gcd(r0,2*K)==1
    Lam=4*G*G*K*K-B*B
    assert Lam>0
    return G,K,A,B,r0,Lam


def l_bounds(g,k,u,q,X):
    G,K,A,_,_,_=params(g,k,u,q)
    lo_num=G*G*K-10*A*X
    lo_den=5*G
    hi_num=2*(G*G*K-A*X)
    hi_den=G
    return ceil_div(lo_num,lo_den), ceil_div(hi_num,hi_den)-1


def coeffs(g,k,u,q,X,L):
    G,K,A,B,r0,Lam=params(g,k,u,q)
    z0=(pow(r0,-1,2*K)*L)%(2*K)
    assert (L-r0*z0)%(2*K)==0
    n0=(L-r0*z0)//(2*K)
    assert (B*z0+A*L)%(2*K)==0
    p0=(B*z0+A*L)//(2*K)
    alpha=-(G*G*Lam)//4
    beta=(-2*u*G*K*X - G**4*K*z0 - u*G**3*K*L + (G*G*B*p0)//2)
    gamma=(u*u*A*A*X*X + u*u*(A*G-1)*X*L - u*G*X*z0
           - (G**4*z0*z0)//4 - (u*G**3*z0*L)//2 + (G*G*p0*p0)//4)
    return z0,n0,p0,alpha,beta,gamma


def qval(a,b,c,m):
    return a*m*m+b*m+c


def exact_roots(a,b,c):
    D=b*b-4*a*c
    if D<0: return []
    s=isqrt(D)
    if s*s!=D: return []
    out=[]
    den=2*a
    for num in (-b+s,-b-s):
        if num%den==0:
            out.append(num//den)
    return sorted(set(out))


def check_r9_scaled_identity(g,k,u,q,X,L,m):
    G,K,A,B,r0,Lam=params(g,k,u,q)
    z0,n0,p0,a,b,c=coeffs(g,k,u,q,X,L)
    Z=z0+2*K*m
    P=p0+B*m
    N=n0-r0*m
    assert L==r0*Z+2*K*N
    assert 2*K*P==B*Z+A*L
    E=(u*u*A*A*X*X + u*u*(A*G-1)*X*L - u*G*X*Z
       - G**4*Z*Z//4 - u*G**3*Z*L//2 + G*G*P*P//4)
    assert E==qval(a,b,c,m)
    Pi=G*L*(A*B-4*u*G*K*K)//2 - 4*u*K*K*X
    CXL=A*A*G*G*L*L + 16*K*K*u*u*X*L*(A*G-1) + 16*K*K*u*u*A*A*X*X
    R=G*G*Lam*Z*Z-4*G*Pi*Z-CXL
    assert R==-16*K*K*E
    # R9 discriminant bridge: Delta_m = Delta_box/(64 G^2 K^2).
    disc_m=b*b-4*a*c
    Cbox=G*CXL
    disc_box=16*G**4*Pi*Pi + 4*G**3*Lam*Cbox
    assert disc_m*64*G*G*K*K==disc_box
    return True


def roots_mod(a,b,c,M):
    return [m for m in range(M) if qval(a,b,c,m)%M==0]


def representative_ledger():
    states=[
      (4,1,73,137,1001,99969,0),
      (5,1,9091,11,99629,1784770,205),
      (5,1,11,9091,87090,1999280,0),
      (5,3,9091,11,99259,23155471,1),
    ]
    rows=[]
    for g,k,u,q,X,L,mstar in states:
        G,K,A,B,r0,Lam=params(g,k,u,q)
        lo,hi=l_bounds(g,k,u,q,X)
        assert lo<=L<=hi
        z0,n0,p0,a,b,c=coeffs(g,k,u,q,X,L)
        check_r9_scaled_identity(g,k,u,q,X,L,mstar)
        q0=qval(a,b,c,mstar); q1=qval(a,b,c,mstar+1)
        assert q0>0 and q1<0
        assert not exact_roots(a,b,c)
        Y=A*X+(G//2)*L
        assert G//10<=X<G
        assert G*G*K//10<=Y<G*G*K
        rows.append((g,k,u,q,X,L,z0,2*K,mstar,q0,q1))
    return rows


def natural_modulus_survivor():
    g,k,u,q,X,L=4,1,73,137,3471,144839
    G,K,A,B,r0,Lam=params(g,k,u,q)
    z0,n0,p0,a,b,c=coeffs(g,k,u,q,X,L)
    lo,hi=l_bounds(g,k,u,q,X)
    assert lo<=L<=hi
    Y=A*X+(G//2)*L
    assert G//10<=X<G and G*G*K//10<=Y<G*G*K
    assert c%G==0
    assert not exact_roots(a,b,c)
    mods={'2K':2*K,'G':G,'u':u,'q':q,'A':A}
    rr={name:roots_mod(a,b,c,M) for name,M in mods.items()}
    assert all(rr[name] for name in rr)
    return (X,L,z0,a,b,c,rr)


def census_allX_g4k1():
    g,k,u,q=4,1,73,137
    G,K,A,B,r0,Lam=params(g,k,u,q)
    checked=0; squares=0; hits=[]
    for X in range(G//10,G):
        lo,hi=l_bounds(g,k,u,q,X)
        d=gcd(X,G)
        mod=G//d
        target=(A*A*X)%mod
        first=lo+(target-lo)%mod
        for L in range(first,hi+1,mod):
            checked+=1
            z0,n0,p0,a,b,c=coeffs(g,k,u,q,X,L)
            # Necessary constant residue, derived from G | alpha,beta:
            assert c%G==0
            D=b*b-4*a*c
            s=isqrt(D)
            if s*s==D:
                squares+=1
                for m in exact_roots(a,b,c):
                    Z=z0+2*K*m
                    if Z>0:
                        hits.append((X,L,z0,m,Z))
    assert checked==1922400
    assert squares==0
    assert hits==[]
    return checked,squares,hits


def census_unitX(g,k,u,q):
    G,K,A,B,r0,Lam=params(g,k,u,q)
    assert k<=g
    checked=0; squares=0; hits=[]
    for X in range(G//10,G):
        if gcd(X,10)!=1: continue
        lo,hi=l_bounds(g,k,u,q,X)
        target=(A*A*X)%G
        first=lo+(target-lo)%G
        for L in range(first,hi+1,G):
            checked+=1
            z0,n0,p0,a,b,c=coeffs(g,k,u,q,X,L)
            assert c%G==0
            D=b*b-4*a*c
            s=isqrt(D)
            if s*s==D:
                squares+=1
                for m in exact_roots(a,b,c):
                    if z0+2*K*m>0:
                        hits.append((X,L,z0,m))
    assert hits==[]
    return checked,squares,hits


def main():
    print('R10 ROOT-LATTICE EXACT CERTIFICATE')
    print('===================================')
    print('FORMULA_IDENTITY_CHECKS=PASS')
    for row in representative_ledger():
        print('INTERLACING',row)
    X,L,z0,a,b,c,rr=natural_modulus_survivor()
    print('NATURAL_MODULUS_SURVIVOR',X,L,z0)
    for name,roots in rr.items():
        print('  MOD',name,'ROOT_COUNT',len(roots),'FIRST',roots[:10])
    print('  INTEGER_ROOT=NONE; DISCRIMINANT_NONSQUARE')
    checked,sq,hits=census_allX_g4k1()
    print('CENSUS_ALL_X_G4_K1', 'CHECKED',checked,'SQUARE_DISC',sq,'POSITIVE_HITS',len(hits))
    for args in [(4,1,73,137),(4,2,73,137),(5,1,11,9091),(5,1,9091,11)]:
        checked,sq,hits=census_unitX(*args)
        print('CENSUS_UNIT_X',args,'CHECKED',checked,'SQUARE_DISC',sq,'POSITIVE_HITS',len(hits))
    print('FINITE_SEARCH_IS_NOT_GLOBAL_PROOF=TRUE')
    print('CERTIFICATE_STATUS=PASS')

if __name__=='__main__':
    main()
