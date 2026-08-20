#!/usr/bin/env python3
from math import gcd
from fractions import Fraction
def verify_B():
    b1,b2,b3=1,6,8;P1,P2,P3,Q0=48,436,75,445;V=24;G=1;K=10;X=10;Y=10;m2=n3=1
    assert P1*P1+P2*P2+P3*P3==Q0*Q0
    assert gcd(gcd(gcd(P1,P2),P3),Q0)==1 and gcd(V,P1)==24
    A0=Y*G*(b1*X+b2)+b3;B0=b1*X*Y*G*K;C0=b2*Y*P2+b3*P3
    d=gcd(gcd(A0,B0),C0);Ahat,Bhat,c=A0//d,B0//d,C0//d
    a,b=Bhat-Ahat,Bhat+Ahat;g=gcd(a,b);ap,bp=a//g,b//g
    assert (A0,B0,C0,d,Ahat,Bhat,c,a,b,g,ap,bp)==(168,1000,26760,8,21,125,3345,104,146,2,52,73)
    h=gcd(P1,Q0);x=Q0+P1;y=Q0-P1;eps=gcd(x//h,y//h);X0=x//h//eps;Y0=y//h//eps
    M=X0*Y0;Delta=2*c//(g*eps*h)
    assert (h,eps,X0,Y0,M,Delta)==(1,1,493,397,195721,3345)
    assert gcd(X0,Y0)==1 and bp*Y0-ap*X0==Delta
    D=X0-Y0;Gdiff=48
    assert D==96 and P1==D//2 and gcd(M,D)==1 and D%Gdiff==0 and gcd(Gdiff,M)==1
    T=X0%Gdiff
    assert T==13 and (T*T-M)%Gdiff==0 and ((bp-ap)*T-Delta)%Gdiff==0
    W=Bhat*Q0-Ahat*P1
    assert W==54617 and W*W==c*c+a*b*(P2*P2+P3*P3)
    Dlead=K*P1-Q0;H=b2*Q0-b1*10**m2*Dlead;K3=b3*(Q0-P3)//10**n3
    assert (Dlead,H,K3)==(35,2320,296)
    assert b1*P1*100==Q0*16-H and b2*P2==H+K3
    C2=P2//gcd(V,P2);C3=P3//gcd(V,P3)
    L=max(Fraction(10,C2),Fraction(1,C3));R=min(Fraction(100,C2),Fraction(10,C3))
    assert (L,R)==(Fraction(10,109),Fraction(2,5)) and not any(L<=u<R for u in range(1,10))
    return "B PASS; first failure COMMON_U_INTEGER_SUCCESSOR"
def verify_E():
    b1,b2,b3=5,5,1;P1,P2,P3,Q0=298,2514,1485,2935;V=5;G=1;K=10;X=10;Y=10
    A0=Y*(b1*X+b2)+b3;B0=b1*X*Y*K;C0=b2*Y*P2+b3*P3
    d=gcd(gcd(A0,B0),C0);Ahat,Bhat,c=A0//d,B0//d,C0//d
    a,b=Bhat-Ahat,Bhat+Ahat;g=gcd(a,b);ap,bp=a//g,b//g
    h=gcd(P1,Q0);x=Q0+P1;y=Q0-P1;eps=gcd(x//h,y//h);X0=x//h//eps;Y0=y//h//eps
    Delta=2*c//(g*eps*h)
    assert (ap,bp,X0,Y0,Delta)==(4449,5551,3233,2637,254370)
    assert bp*Y0-ap*X0==Delta and X0%61==0 and Y0%9==0 and gcd(V,P1)==1
    return "E PASS; forced packets 61->X and 3^2->Y"
if __name__=="__main__":
    print(verify_B());print(verify_E())
