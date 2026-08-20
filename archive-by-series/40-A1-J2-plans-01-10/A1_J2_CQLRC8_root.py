#!/usr/bin/env python3
"""A1 J2 CQLRC8 root-compatibility certificate.

Exact symbolic reduction of the high/boundary/low root kernels to one unified
formula, plus q=11 quotient-lift regression and counterexamples to overly strong
single-prime/root-divisibility claims.
"""
from math import gcd,isqrt
import sympy as sp


def vp(n,p):
    n=abs(int(n)); c=0
    if n==0:return 10**9
    while n%p==0:n//=p;c+=1
    return c


def unit10(n): return gcd(abs(int(n)),10)==1


def tail_data(q,delta=0):
    b=vp(q+4,5); d0=2*5**b
    beta=10**max(-delta,0); d=d0*beta
    c=q**3+10*q*q+12*q+8
    C=q*c; B=(q+2)*(q*q-4*q-4)
    return b,d0,beta,d,c,C,B


def reconstruct(G,q,N,t):
    if (G+1)%q:return None
    u=(G+1)//q; A=2*u+1; M=q*(q+4)
    R=A*t-2*N
    if R%M:return None
    Z=R//M
    num=(G-1)*t-q*N; den=2*(q+4)
    if num%den:return None
    a3=num//den
    if (Z+u*N)%2:return None
    X=(Z+u*N)//2
    D2=u*a3+G*X
    return dict(G=G,q=q,u=u,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2)


def F(row): return row['A']*row['X']**2+row['Z']*row['D2']


def psi_delta(row,delta):
    aa=10**max(delta,0); bb=10**max(-delta,0)
    return 4*row['u']**2*aa**2*row['D2']**2-row['A']*bb**2*F(row)


def local64(row,delta,p):
    q=row['q']; assert q%p==0
    A=row['A']%p; t=row['t']%p
    rho=((row['A']*row['t']-2*row['N'])//q)%p
    aa=pow(10,max(delta,0),p); bb=pow(10,max(-delta,0),p)
    P0=(rho+A*(A-1)*t)%p
    Q0=(rho+(A*A-1)*t)%p
    v=((A-1)**2*aa*aa*Q0*Q0-A*A*bb*bb*P0*P0+2*A*bb*bb*rho*Q0)%p
    return rho,v


def symbolic_unification():
    G,K,u,A,H,D2,Fv=sp.symbols('G K u A H D2 Fv', nonzero=True)
    ap,bp=sp.symbols('ap bp', positive=True, integer=True)
    S=sp.symbols('S', positive=True)
    # unified parameterization G=S*b, K=S*a
    disc=sp.expand((2*u*(S*ap)*D2)**2-4*A*(S*bp/2)**2*Fv)
    psi=4*u**2*ap**2*D2**2-A*bp**2*Fv
    assert sp.simplify(disc-S**2*psi)==0
    # Formal root a1 = 2(2u*a*D2 +/- s)/(A*G*b), since G=S*b.

    rho,t,Aloc,a,b=sp.symbols('rho t Aloc a b')
    P0=rho+Aloc*(Aloc-1)*t
    Q0=rho+(Aloc**2-1)*t
    L=sp.expand((Aloc-1)**2*a**2*Q0**2-Aloc**2*b**2*P0**2+2*Aloc*b**2*rho*Q0)
    poly=sp.Poly(L,rho)
    lead=sp.factor(poly.LC())
    expected=(Aloc-1)**2*(a**2-b**2)+b**2
    assert sp.simplify(lead-expected)==0
    # boundary a=b=1 has a very clean norm form
    L0=sp.factor(L.subs({a:1,b:1}))
    norm=(rho+(Aloc-1)*t)**2-2*Aloc**2*(Aloc-1)**2*t**2
    assert sp.simplify(L0-norm)==0
    discr=sp.factor(sp.discriminant(poly.as_expr(),rho))
    return sp.factor(lead),sp.factor(discr),sp.factor(L0)


def q11_state(g):
    q=11; delta=1; alpha=152510; t=31
    b,d0,beta,d,c,C,B=tail_data(q,delta)
    G=10**g
    assert (G+1)%q==0
    num=B*t+alpha*(G//d)
    assert num%C==0
    N=num//C
    row=reconstruct(G,q,N,t); assert row is not None
    psi=psi_delta(row,delta)
    rho,l64=local64(row,delta,11)
    assert l64==(64*psi)%11
    return row,psi,rho,l64


def q11_regression():
    row,psi,rho,l64=q11_state(471)
    assert psi%11==8 and rho==9 and l64==6
    assert pow(psi%11,5,11)==10
    # Crucial audit: p|q does NOT divide AG here, so Layer-R divisibility modulo p is unavailable.
    assert row['A']%11==8 and row['G']%11==10 and gcd(row['A']*row['G'],11)==1

    # From quotient script: on legal first lift n=4+11*z, rho=4+6z (mod11).
    vals=[]
    for z in range(11):
        rr=(4+6*z)%11
        A=8; t=31%11; aa=10%11; bb=1
        P0=(rr+A*(A-1)*t)%11
        Q0=(rr+(A*A-1)*t)%11
        v=((A-1)**2*aa*aa*Q0*Q0-A*A*P0*P0+2*A*rr*Q0)%11
        ch='ZERO' if v==0 else ('RESIDUE' if pow(v,5,11)==1 else 'NONRESIDUE')
        vals.append((z,rr,v,ch))
    assert any(x[3]=='RESIDUE' for x in vals) and any(x[3]=='NONRESIDUE' for x in vals)
    assert vals[10][1]==9 and vals[10][2]==6 and vals[10][3]=='NONRESIDUE'
    return vals


def shifted_fibre_counterexamples():
    # Same fixed fibre (q,h,alpha,t) as g=471, shifted by the exact quotient-integrality
    # period 12606.  These states pass tail reconstruction and show mod-11 root class changes.
    out=[]
    for g in (471,13077,50895,63501,101319,126531):
        row,psi,rho,l64=q11_state(g)
        chars=[]
        c=11**3+10*11**2+12*11+8
        B=(11+2)*(11**2-4*11-4)
        for p in sorted(sp.factorint(11*(11+4)*c*B)):
            if p in (2,5):continue
            r=psi%p
            leg=0 if r==0 else pow(r,(p-1)//2,p)
            chars.append((p,r,'ZERO' if leg==0 else ('RESIDUE' if leg==1 else 'NONRESIDUE')))
        sq=psi>=0 and isqrt(psi)**2==psi
        out.append((g,psi%11,rho,chars,sq))
    # g=63501 survives every structural prime in q(q+4)c(q)B(q), but is not a global square.
    target=[x for x in out if x[0]==63501][0]
    assert all(ch!='NONRESIDUE' for _,_,ch in target[3])
    assert target[4] is False
    # g=13077 already disproves 'same fixed fibre is always killed mod q'.
    x=[x for x in out if x[0]==13077][0]
    assert x[1]==9 and all(not(p==11 and ch=='NONRESIDUE') for p,r,ch in x[3])
    return out


if __name__=='__main__':
    lead,discr,bound=symbolic_unification()
    vals=q11_regression()
    shifted=shifted_fibre_counterexamples()
    print('ROOT_SYMBOLIC_STATUS=PASS')
    print('LOCAL_RHO2_LEADING_COEFF=',lead)
    print('LOCAL_RHO_DISCRIMINANT=',discr)
    print('BOUNDARY_LOCAL_FORM=',bound)
    print('Q11_Z_TABLE=',vals)
    print('SHIFTED_FIXED_FIBRE=',shifted)
