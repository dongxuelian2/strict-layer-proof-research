#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

states = [
('A',(1,6,8),(24,52,159),169,24,(24,4,3),1,1,2,1,3,4,13,53,2,1),
('B',(1,6,8),(48,436,75),445,24,(24,4,3),1,1,2,1,3,4,109,25,2,1),
('C',(1,6,8),(456,292,2907),2957,24,(24,4,3),1,1,2,1,3,4,73,969,2,1),
('E',(5,5,1),(298,2514,1485),2935,5,(1,1,5),1,5,1,1,1,1,2514,297,2,1),
]

def smooth25(n):
    x=n
    while x%2==0: x//=2
    while x%5==0: x//=5
    return x==1

def p5(n):
    x=n
    while x%5==0: x//=5
    return x==1

for name,b,P,Q,V,gs,s,alpha,beta,u0,t,v,M,N,n2,n3 in states:
    b1,b2,b3=b; P1,P2,P3=P; g1,g2,g3=gs
    assert P1*P1+P2*P2+P3*P3==Q*Q
    assert gcd(gcd(gcd(P1,P2),P3),Q)==1
    assert P2==v*M
    assert P3==alpha*t*N
    C2=M//u0
    C3=N//u0
    assert C2>0 and C3>0
    assert P2//g2==C2 and P3//g3==C3
    assert gcd(C2,b2)==1 and gcd(C3,b3)==1
    L=max(Fraction(10**(n2-1),C2),Fraction(10**(n3-1),C3))
    R=min(Fraction(10**n2,C2),Fraction(10**n3,C3))
    assert not any(L<=U<R for U in (1,2,3))
    if name=='B':
        assert C3==25 and Q%C3!=0
    assert not smooth25(C2)

print('R13 carrier-image exact census regression: PASS')
