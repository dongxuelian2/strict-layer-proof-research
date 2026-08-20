#!/usr/bin/env python3
"""105-R11 exact quotient/threshold regression.

Purpose:
- verify B/E exact quotient and threshold values;
- verify the local p-power division firewall;
- keep computation as regression only, never as a nonexistence theorem.
"""
from math import gcd, floor

def positive_set(G, W, d, M, rho):
    out=[]
    for k in range(d):
        if rho == 0 and k == 0:
            delta=0
        else:
            r=rho+k*M
            delta=0 if r == 0 else d*M-r
        sigma=G-W*delta
        if sigma > 0:
            out.append(k)
    return out

def local_quotient(N, D, p, e):
    f=0
    z=D
    while z % p == 0:
        f += 1
        z //= p
    assert N % (p**f) == 0
    unit=D//(p**f)
    assert gcd(unit,p)==1
    mod=p**e
    return ((N//(p**f))*pow(unit,-1,mod)) % mod, f

def fixture_B():
    C2,C3,x,d,M,rho,G=109,25,10,1,109,10,840
    Q=(x-rho)//M
    assert Q==0 and Q%d==0
    assert positive_set(G,C3,d,M,rho)==[]
    sigma=G-C3*(d*M-rho)
    assert sigma==-1635
    D=10*1*48//d
    N=D*Q
    assert D==480 and N==0

def fixture_E():
    C2,C3,x,d,M,rho,G=2514,297,10,2,1257,10,22170
    Q=(x-rho)//M
    assert Q==0 and Q%d==0
    assert positive_set(G,C3,d,M,rho)==[]
    s0=G-C3*(d*M-rho)
    s1=G-C3*(d*M-rho-M)
    assert (s0,s1)==(-721518,-348189)
    D=10*5*298//d
    N=D*Q
    assert D==7450 and gcd(D,d)==2 and N==0
    qmod,f=local_quotient(N,D,2,1)
    assert f==1 and qmod==0

def fixture_B_faceB_transport():
    C3,d,M,rho,x=25,5,5,1,1
    K3,b3,Q0,V=296,8,445,24
    T=(b3*Q0-10*K3*rho)//C3
    D=10*K3//d
    N=T-V
    Q=N//D
    assert (T,D,N,Q,Q%d)==(24,592,0,0,0)

if __name__ == "__main__":
    fixture_B()
    fixture_E()
    fixture_B_faceB_transport()
    print("105-R11 exact regression: PASS")
