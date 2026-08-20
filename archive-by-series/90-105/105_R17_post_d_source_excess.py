#!/usr/bin/env python3
from math import gcd
def vp(n,p):
    e=0
    while n%p==0:
        n//=p;e+=1
    return e
def rad(n):
    r=1;d=2
    while d*d<=n:
        if n%d==0:
            r*=d
            while n%d==0:n//=d
        d=3 if d==2 else d+2
    if n>1:r*=n
    return r
def ceildiv(a,b): return (a+b-1)//b
def check(r):
    assert r["G"]==10**r["g"] and r["K"]==10**r["k"]
    assert r["X"]==10**r["m2"] and r["Y"]==10**r["n3"]
    assert r["P2"]==r["W"]*r["C2"] and r["P3"]==r["A"]*r["C3"]
    assert r["P1"]**2+r["P2"]**2+r["P3"]**2==r["Q0"]**2
    D=r["K"]*r["P1"]-r["Q0"]; assert D==r["D"]>0
    T3=r["Q0"]-r["P3"]; assert T3==r["T3"]>0
    Om=r["Q0"]*(r["W"]+r["A"]*r["Y"]*r["G"])-r["A"]*r["W"]*(r["C3"]+r["Y"]*r["C2"])
    assert Om==r["Omega"]>0
    L=r["U0"]*r["A"]*r["W"]*r["X"]*r["Y"]*r["G"]
    NM=L*D; assert NM==r["NM"] and NM%Om==0
    h=gcd(r["P1"],r["Q0"]); p=r["P1"]//h; delta=D//h
    assert gcd(p,delta)==1 and Om%delta==0
    OD=Om//delta; s=gcd(L,p); E=L//s
    g0=gcd(r["U0"]*r["A"]*r["W"],r["P1"]); RM=h*s//g0
    lower=(OD%E==0); ms=OD//E if lower else None
    upper=lower and RM%ms==0
    return dict(L=L,NM=NM,h=h,p=p,delta=delta,OmegaD=OD,Esrc=E,g0=g0,RM=RM,lower=lower,msrc=ms,upper=upper,gstar=NM//Om)
C5=dict(U0=1,C2=450,C3=7,n2=3,n3=1,g=1,k=1,m2=1,m3=2,G=10,K=10,X=10,Y=10,A=7,W=4,P1=420,P2=1800,P3=49,Q0=1849,D=2351,T3=1800,Omega=1175500,NM=65828000)
FULL=dict(U0=1,C2=60,C3=13683,n2=2,n3=5,g=0,k=1,m2=1,m3=5,G=1,K=10,X=10,Y=100000,A=1,W=35,P1=5600,P2=2100,P3=13683,Q0=14933,D=41067,T3=1250,Omega=1283343750,NM=1437345000000)
a=check(C5)
assert (a["Esrc"],a["OmegaD"],vp(a["Esrc"],5),vp(a["OmegaD"],5),vp(a["Esrc"],2),vp(a["OmegaD"],2))==(200,500,2,3,3,2)
b=check(FULL)
assert (b["Esrc"],b["OmegaD"],b["msrc"],b["RM"],b["upper"],b["gstar"],b["g0"])==(6250,31250,5,160,True,1120,35)
mu=b["gstar"]//b["g0"]; R1=FULL["P1"]//b["gstar"]
lambda_z=FULL["Y"]//gcd(FULL["Y"],FULL["W"]*FULL["T3"])
tau=lambda_z//gcd(lambda_z,mu); Lambda=mu*tau
F=rad(R1*FULL["C2"]*FULL["C3"])
ZL=max(ceildiv(10**(FULL["m2"]-1),FULL["A"]),ceildiv(10**(FULL["m3"]-1),FULL["W"]))
ZU=min((10**FULL["m2"]-1)//FULL["A"],(10**FULL["m3"]-1)//FULL["W"])
assert (mu,R1,lambda_z,tau,Lambda,F,gcd(Lambda,FULL["C2"]*FULL["C3"]),ZL,ZU)==(32,5,16,1,32,136830,4,286,9)
print("105-R17 exact witness verifier: PASS")
