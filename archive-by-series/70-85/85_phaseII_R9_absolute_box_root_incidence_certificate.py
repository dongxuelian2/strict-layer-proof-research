#!/usr/bin/env python3
"""Exact arithmetic certificate for Second-85 Phase-II R9.

Responsibilities:
1. Implement the integer-cleared XY-adapted root residual.
2. Verify the R8 PLCF box point has the positive real root between Z=0 and Z=1
   by exact opposite residual signs.
3. Verify the new g=4 root-independent source-compatible pair has opposite
   residual signs while passing source lattice, positive words, common-V,
   primitive, regularity, and exact content U=1.
4. Run limited deterministic counterexample-guillotine scans. These scans are
   explicitly NOT completeness proofs for A9/B9/C9.

No floating-point value is used for any PASS/FAIL decision.
"""
from math import gcd, isqrt
from functools import reduce


def outer(g,k,u):
    G=10**g; K=10**k; H=G//2
    assert (G+1)%u==0
    q=(G+1)//u
    A=2*u+1; B=2*G+q
    assert gcd(A,2*K)==1
    r0=(-pow(A,-1,2*K)*B)%(2*K)
    return G,K,H,q,A,B,r0


def residual_int(g,k,u,X,Y,Z):
    """Returns Psi=16*G*K^2*F; sign equals exact root residual sign."""
    G,K,H,q,A,B,r0=outer(g,k,u)
    D=Y-A*X
    Lam=4*G*G*K*K-B*B
    assert Lam>0
    Pi=A*B*D-4*u*G*K*K*D-4*u*K*K*X
    C=4*A*A*G*D*D + 32*K*K*u*u*X*D*(A*G-1) + 16*G*K*K*u*u*A*A*X*X
    assert C>0
    return -G**3*Lam*Z*Z + 4*G*G*Pi*Z + C


def ledger(g,k,u,X,L,Z):
    G,K,H,q,A,B,r0=outer(g,k,u)
    assert (L-r0*Z)%(2*K)==0
    N=(L-r0*Z)//(2*K)
    Y=A*X+H*L
    Pnum=B*Z+A*L
    assert Pnum%(2*K)==0
    P=Pnum//(2*K)
    W=G*H*Z-u*A*X
    S=G*Z+u*L
    D2=u*X+G*W
    h=q*H*Z-A*X
    m=A*h-G*Z
    r=H*h-u*X
    U=reduce(gcd,(abs(X),abs(Z),abs(N)))
    P1=G*H*P; P2=u*G*Y; P3=u*X; Q0=P2+D2
    primitive=reduce(gcd,(P1,P2,P3,Q0))
    return dict(G=G,K=K,H=H,q=q,A=A,B=B,r0=r0,X=X,Y=Y,Z=Z,L=L,N=N,U=U,
                P=P,W=W,S=S,D2=D2,h=h,m=m,r=r,
                source_lattice=True,
                positive=min(P,W,S,D2,h,m,r)>0,
                tenunit=(gcd(X*Z*L,10)==1 and gcd(W*S*D2*h*m*r,10)==1),
                commonV=(gcd(P,u)==1 and gcd(Y,H)==1 and gcd(X,G*H)==1),
                primitive=primitive,
                regular=gcd(A,D2//U)==1,
                residual=residual_int(g,k,u,X,Y,Z))


def verify_plcf():
    g,k,u=5,1,11
    G,K,H,q,A,B,r0=outer(g,k,u)
    X=99999; Y=15002149977
    assert G//10<=X<G
    assert G*G*K//10<=Y<G*G*K
    r0v=residual_int(g,k,u,X,Y,0)
    r1v=residual_int(g,k,u,X,Y,1)
    assert r0v>0 and r1v<0
    print("PLCF_XY_ROOT_INTERVAL=(0,1) PASS")
    print("PLCF_PSI_0=",r0v)
    print("PLCF_PSI_1=",r1v)


def verify_spacing_pair():
    g,k,u=4,1,73
    X=1001; L=99969
    G,K,H,q,A,B,r0=outer(g,k,u)
    Y=A*X+H*L
    assert G//10<=X<G
    assert G*G*K//10<=Y<G*G*K
    assert gcd(X,10)==gcd(Y,10)==1

    a=ledger(g,k,u,X,L,1)
    b=ledger(g,k,u,X,L,61)
    for row in (a,b):
        assert row['positive']
        assert row['tenunit']
        assert row['commonV']
        assert row['primitive']==1
        assert row['regular']
        assert row['U']==1
    assert a['residual']>0
    assert b['residual']<0

    # The next source-lattice site after Z=1 is Z=21; exact sign proves unique
    # positive real root lies strictly between 1 and 21.
    r21=residual_int(g,k,u,X,Y,21)
    assert r21<0
    print("SPACING_PAIR_ALL_ROOT_INDEPENDENT_GATES=PASS")
    print("PSI_Z1=",a['residual'])
    print("PSI_Z21=",r21)
    print("PSI_Z61=",b['residual'])
    print("UNIQUE_POSITIVE_ROOT_INTERVAL=(1,21) BY SIGN+CONCAVITY")


def scan_D(g,k,u,zmax):
    """Limited A9 falsification probe: integer X,Y,Z, no source lattice required."""
    G,K,H,q,A,B,r0=outer(g,k,u)
    hits=0
    for X in range(G//10,G):
        for Z in range(1,zmax+1):
            # Equation in D=Y-AX after multiplying by 4 G K^2.
            aa=A*A*G
            bb=A*B*G*G*Z - 4*u*G**3*K*K*Z + 8*u*u*K*K*X*(A*G-1)
            cc=(4*G*K*K*u*u*A*A*X*X
                -4*u*G*G*K*K*X*Z
                +(G**3//4)*(B*B-4*G*G*K*K)*Z*Z)
            disc=bb*bb-4*aa*cc
            if disc<0: continue
            s=isqrt(disc)
            if s*s!=disc: continue
            den=2*aa
            for num in (-bb+s,-bb-s):
                if num%den: continue
                D=num//den
                Y=A*X+D
                if D>0 and G*G*K//10<=Y<G*G*K:
                    hits+=1
    return hits


if __name__ == '__main__':
    verify_plcf()
    verify_spacing_pair()
    h1=scan_D(4,1,73,100)
    assert h1==0
    print("LIMITED_A9_SCAN_(4,1,73)_X_FULL_Z1_100_HITS=0 PASS")
    h2=scan_D(5,1,11,5)
    assert h2==0
    print("LIMITED_A9_SCAN_(5,1,11)_X_FULL_Z1_5_HITS=0 PASS")
    print("CERTIFICATE_STATUS=PASS")
