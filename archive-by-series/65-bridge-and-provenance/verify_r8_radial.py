#!/usr/bin/env python3
"""105-R8 exact radial verifier.

Scope:
- Does NOT reopen PSDG / discriminant / packet allocation.
- Treats the four R7D reduced-witness registry entries A,B,C,E as frozen PSDG PASS inputs.
- Re-verifies only downstream frozen sphere/master/g1/Smith/DES data and the R8 radial successor layer.
- Uses exact integer/Fraction arithmetic only.
"""
from fractions import Fraction
from math import gcd, ceil

PROFILES = [
    ("A",(1,6,8),(24,52,159,169),24,2,1,1,1,1,0,(1,1,2,3,1,4)),
    ("B",(1,6,8),(48,436,75,445),24,2,1,1,1,1,0,(1,1,2,3,1,4)),
    ("C",(1,6,8),(456,292,2907,2957),24,2,1,1,1,1,0,(1,1,2,3,1,4)),
    ("E",(5,5,1),(298,2514,1485,2935),5,2,1,1,1,1,0,(1,5,1,1,1,1)),
]

def check(item):
    name,b,P,V,n2,n3,m2,m3,k,g,smith=item
    b1,b2,b3=b; P1,P2,P3,Q0=P
    G,K,X,Y=10**g,10**k,10**m2,10**n3
    assert P1*P1+P2*P2+P3*P3==Q0*Q0
    assert gcd(gcd(P1,P2),gcd(P3,Q0))==1
    gs=(gcd(V,P1),gcd(V,P2),gcd(V,P3))
    assert tuple(V//x for x in gs)==b
    assert gcd(V,P1)==V//b1
    C=(P1//gs[0],P2//gs[1],P3//gs[2])
    D=K*P1-Q0
    assert b1*X*Y*G*D+b2*Y*(P2-G*Q0)-b3*(Q0-P3)==0
    H=b2*Q0-b1*X*D
    K3=Fraction(b3*(Q0-P3),Y)
    assert K3.denominator==1 and b2*P2==G*H+K3
    s,a,beta,t,u,v=smith
    assert (b1,b2,b3)==(s*a*u,s*a*beta*t,s*beta*v)
    assert gcd(a,beta)==gcd(u,beta*t)==gcd(a*t,v)==1

    C1,C2,C3=C
    L2=Fraction(10**(n2-1),C2); L3=Fraction(10**(n3-1),C3)
    L=max(L2,L3); R=min(10*L2,10*L3)
    uz=max(1,ceil(L))
    us=uz
    while gcd(us,V)!=1: us+=1
    if L2>=L3:
        Gface=C2*10**n3-C3*10**(n2-1)
        jump=C2*us-10**(n2-1)
        exact=(us<R)==(C3*jump<Gface)
    else:
        Gface=C3*10**n2-C2*10**(n3-1)
        jump=C3*us-10**(n3-1)
        exact=(us<R)==(C2*jump<Gface)
    assert exact
    return name,L,R,uz,us,R-us

if __name__=="__main__":
    for p in PROFILES:
        print(check(p))
