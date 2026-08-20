#!/usr/bin/env python3
"""A1 J2 CQLRC8 quotient-lift certificate.

Exact arithmetic only.  Establishes the cyclotomic quotient recurrence,
the first quotient relation, and the p-adic Hensel ladder used in the report.
"""
from math import gcd
import sympy as sp


def vp(n,p):
    n=abs(int(n)); c=0
    if n==0: return 10**9
    while n%p==0:
        n//=p; c+=1
    return c


def tail_data(q,delta=0):
    b=vp(q+4,5)
    d0=2*5**b
    beta=10**max(-delta,0)
    d=d0*beta
    c=q**3+10*q*q+12*q+8
    B=(q+2)*(q*q-4*q-4)
    C=q*c
    return b,d0,beta,d,c,B,C


def order_class(q):
    T=int(sp.n_order(10,q))
    assert T%2==0 and pow(10,T//2,q)==q-1
    g0=T//2
    R=10**T
    L=(R-1)//q
    u0=(10**g0+1)//q
    return T,g0,R,L,u0


def u_mod(q,g,mod):
    """Return ((10^g+1)/q) mod mod, assuming q | 10^g+1."""
    z=pow(10,g,q*mod)+1
    # z is 0 or a positive multiple of q modulo q*mod.
    if z==q*mod: z=0
    assert z%q==0
    return (z//q)%mod


def prime_lift_formula(q,p,n):
    """Check u_n == u0 - n L (mod p), where g=g0+n*T."""
    T,g0,R,L,u0=order_class(q)
    g=g0+n*T
    lhs=u_mod(q,g,p)
    rhs=(u0-n*L)%p
    assert lhs==rhs
    return lhs


def fibre_data(q,delta,alpha,t):
    b,d0,beta,d,c,B,C=tail_data(q,delta)
    assert (d*B*t-alpha)%q==0
    e=(d*B*t-alpha)//q
    # q*d*c*rho = J(u)
    L0=2*(d*c*t-alpha)
    C0=d*c*t-2*e
    return dict(b=b,d0=d0,beta=beta,d=d,c=c,B=B,C=C,e=e,L0=L0,C0=C0)


def first_qrel(q,p,delta,alpha,t,u,N,e):
    """Verify e = 4*d*t*(4u+1) (mod p), p|q, on a legal rho quotient."""
    b,d0,beta,d,c,B,C=tail_data(q,delta)
    assert q%p==0
    assert alpha%p==(-8*d*t)%p
    assert c%p==8%p
    assert (d*c*N-alpha*u-e)%p==0
    # N == A t/2 mod p when rho is integral.
    A=2*u+1
    assert (2*N-A*t)%p==0
    lhs=e%p
    rhs=(4*d*t*(4*u+1))%p
    assert lhs==rhs
    return lhs


def q11_regression():
    q=11; p=11; delta=1; alpha=152510; t=31; g=471
    fd=fibre_data(q,delta,alpha,t)
    T,g0,R,L,u0=order_class(q)
    assert (T,g0,L%p,u0%p)==(2,1,9,1)
    n=(g-g0)//T
    u=(10**g+1)//q
    N=(alpha*u+fd['e'])//(fd['d']*fd['c'])
    A=2*u+1
    rho=(A*t-2*N)//q
    assert n%11==4 and u%11==9 and N%11==3 and rho%11==9
    first_qrel(q,p,delta,alpha,t,u,N,fd['e'])

    # Hensel next-digit regression: n = 4 + 11*z.  rho is affine in z mod 11.
    seq=[]
    dc=fd['d']*fd['c']
    for z in range(11):
        nn=4+11*z
        gg=g0+T*nn
        uu=u_mod(q,gg,121)
        J=fd['L0']*uu+fd['C0']
        assert J%11==0
        rr=((J//11)*pow(dc%11,-1,11))%11
        seq.append(rr)
    assert seq==[(4+6*z)%11 for z in range(11)]
    # Universal slope -4*t*L/q' (q'=1) mod p.
    assert (-4*(t%11)*(L%11))%11==6
    return dict(T=T,g0=g0,L_mod_p=L%p,n_mod_p=n%p,u_mod_p=u%p,e=fd['e'],e_mod_p=fd['e']%p,
                N_mod_p=N%p,rho_mod_p=rho%p,rho_affine=seq)


def nonsquarefree_regression():
    rows=[]
    for q in (49,121):
        T,g0,R,L,u0=order_class(q)
        p=7 if q==49 else 11
        a=vp(q,p)
        assert a==2 and L%p!=0
        for n in range(p):
            prime_lift_formula(q,p,n)
        rows.append((q,p,a,T,g0,L%p,u0%p))
    return rows


def symbolic_identities():
    q,d,c,B,t,alpha,u,e,N,rho=sp.symbols('q d c B t alpha u e N rho')
    A=2*u+1
    # Given d*c*N=alpha*u+e, multiply rho=(At-2N)/q by d*c.
    J=2*(d*c*t-alpha)*u+d*c*t-2*e
    assert sp.simplify(sp.expand(q*d*c*rho-J).subs(rho,(A*t-2*N)/q).subs(N,(alpha*u+e)/(d*c)))==0

    # The concrete polynomial identity c-B = 4(3q^2+6q+4), hence mod q =16.
    qq=sp.symbols('qq')
    cc=qq**3+10*qq**2+12*qq+8
    BB=(qq+2)*(qq**2-4*qq-4)
    assert sp.simplify((cc-BB)-4*(3*qq**2+6*qq+4))==0
    assert sp.rem(cc,qq)==8
    assert sp.rem(BB,qq)==-8 or sp.rem(BB,qq)==qq-8


if __name__=='__main__':
    symbolic_identities()
    small=[]
    for q in (7,11,17,19):
        T,g0,R,L,u0=order_class(q)
        p=q
        for n in range(p): prime_lift_formula(q,p,n)
        small.append((q,T,g0,L%p,u0%p))
    reg=q11_regression()
    ns=nonsquarefree_regression()
    print('QUOTIENT_SYMBOLIC_STATUS=PASS')
    print('SMALL_Q_ORDER_TABLE=',small)
    print('Q11_REGRESSION=',reg)
    print('NONSQUAREFREE_REGRESSION=',ns)
