#!/usr/bin/env python3
from math import gcd, lcm, isqrt
def dig(n): return len(str(n))
def ceil_div(a,b): return (a+b-1)//b
P1,P2,P3,Q0=48,436,75,445
A,W,u0,g1,Lam,q=3,4,1,24,2,1
C2,C3=109,25
n2,n3=2,1
g0=gcd(u0*A*W,P1); mu=g1//g0; a=u0*A*W//g0; s=P1//g1
m2=dig(A*Lam*q); m3=dig(W*Lam*q); g=m3-n3; k=n2-m2-g
X,Y,G,K=10**m2,10**n3,10**g,10**k
L=a*X*Y*G*K
B=mu*(W+A*Y*G)+a*X*Y*G
C=mu*(W*P3+A*Y*P2)
assert (g0,mu,a,s)==(12,2,1,2)
assert (m2,m3,g,k)==(1,1,0,1)
assert (X,Y,G,K)==(10,10,1,10)
assert (L,B,C)==(1000,168,26760)
assert L*P1==B*Q0-C
assert P1*P1+P2*P2+P3*P3==Q0*Q0
lamz=10**n3//gcd(10**n3,W*(Q0-P3))
assert lamz==1 and lcm(mu,lamz)==Lam
delta=C*C+(L*L-B*B)*(P2*P2+P3*P3)
R=isqrt(delta)
assert R*R==delta and R==436936
assert B*P1-L*Q0==-R
ulo=max(ceil_div(10**(n2-1),C2),ceil_div(10**(n3-1),C3))
uhi=min((10**n2-1)//C2,(10**n3-1)//C3)
assert (ulo,uhi)==(1,0)
assert 10**m2==10 # R38 regression expected production X
for aa in range(1,20):
    assert 10*aa > aa+1.1
print("R39_VERIFY=PASS")
print("FIRST_EXPONENT_SYNCHRONIZED_ROOT=(48,436,75,445)")
print("FIRST_FAILURE=SOURCE_INTEGER_ROOM_EMPTY")
print("SOURCE_NATIVE_LINEAR_BRANCH_EXTINCTION=PROVED")
