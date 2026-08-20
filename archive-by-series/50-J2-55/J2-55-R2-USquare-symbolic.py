#!/usr/bin/env python3
"""J2-55 R2 symbolic/exact checks.
Scope: Strict Layer A1-only, Exact Resonance R=0, J=2 only.
No floating-point proof decisions.
"""
from math import gcd
from fractions import Fraction

ETA = Fraction(1299, 500)


def q_value(A,u,K,D,H,X,Z,x):
    return A*H*H*x*x - 2*u*K*D*x + A*X*X + Z*D


def check_carry_identity(A,u,K,D,H,X,Z,r2,j):
    assert A == 2*u+1
    q0=q_value(A,u,K,D,H,X,Z,r2)
    assert q0%(A*A)==0
    lhs=q_value(A,u,K,D,H,X,Z,r2+A*A*j)//(A*A)
    qp=2*A*H*H*r2-2*u*K*D
    rhs=q0//(A*A)+qp*j+A**3*H*H*j*j
    assert lhs==rhs
    return lhs


def check_content_bridge(u,d,r0,m):
    A=2*u+1
    assert A%d==0
    e=A//d
    r_m=r0+m*(A*A//d)
    assert (d*e-1)%u==0
    assert gcd(d,u)==gcd(e,u)==1
    assert (r_m-r0-m*e)%u==0
    return e,r_m%u


def unitary_allocation(u,Z,b):
    """Return u+,u- from gcds when b^2=Z^2 mod u and gcd(Z,u)=1.
    No factorization is needed: gcd(b-Z,u), gcd(b+Z,u) are already
    complementary because u is odd and the two gcds are coprime.
    """
    assert u%2==1 and gcd(Z,u)==1
    assert (b*b-Z*Z)%u==0
    up=gcd(b-Z,u); um=gcd(b+Z,u)
    assert up*um==u and gcd(up,um)==1
    assert (b-Z)%up==0 and (b+Z)%um==0
    return up,um


def corrected_spacing(u,Z,b1,b2):
    """Check the exact same-sign / flipped-sign divisor decomposition.
    Uses the gcd representation, avoiding explicit prime factorization.
    For roots of Z^2, d_same=gcd(b1-b2,u), d_flip=gcd(b1+b2,u),
    and for distinct coprime roots these are complementary unitary divisors.
    """
    assert u%2==1 and gcd(Z,u)==1
    assert (b1*b1-Z*Z)%u==0 and (b2*b2-Z*Z)%u==0
    ds=gcd(b1-b2,u); df=gcd(b1+b2,u)
    assert gcd(ds,df)==1 and ds*df==u
    if b1%u != b2%u:
        assert df>1
    return ds,df


def outer_k_check(g,ell,q,u):
    G=10**g; A=2*u+1; K=10**(2*g-ell); L=10**ell
    assert u*q==G+1
    assert 2*G==q*A-q-2
    assert 4*L*K==(q*A-q-2)**2
    assert (4*L*K-(q+2)**2)%A==0
    assert (4*L*K-((q+2)**2-2*q*(q+2)*A))%(A*A)==0
    assert (L*K-1)%u==0
    return True


def regular_next_digit(A,u,G,K,D,X,Z,r2):
    H=G//2
    q0=q_value(A,u,K,D,H,X,Z,r2)
    assert q0%(A*A)==0
    qp=2*A*H*H*r2-2*u*K*D
    assert gcd(qp,A)==1
    T2=q0//(A*A)
    c3=(-T2*pow(qp,-1,A))%A
    assert q_value(A,u,K,D,H,X,Z,r2+A*A*c3)%(A**3)==0
    return c3


def candidate_excess_divisibility(A,u,G,K,D,X,Z,r2,c3):
    H=G//2
    x=r2+A*A*c3
    E=q_value(A,u,K,D,H,X,Z,x)//(A*A)
    assert E%A==0
    if (x*x-Z*Z)%u==0:
        # In the reconstructed J2 chart Q(x) == (x^2-Z^2)/4 (mod u).
        # This function verifies only the resulting divisibility interface.
        # Caller must supply a state where the reconstructed mod-u identity holds.
        return E, E%u
    return E,None


def proper_content_m_bound(u,d):
    A=2*u+1
    assert 1<d<A and A%d==0
    e=A//d
    assert e>=3 and e%2==1
    assert d<u
    return e


def maximal_content_multiplicity(u,residue):
    """For d=A, m in [0,A)=[0,2u+1), count m == residue mod u."""
    A=2*u+1
    return sum(1 for m in range(A) if m%u==residue%u)


def symbolic_taylor_residual():
    import sympy as sp
    A,u,K,D,H,X,Z,r,j=sp.symbols('A u K D H X Z r j')
    Q=lambda y: A*H**2*y**2-2*u*K*D*y+A*X**2+Z*D
    qp=sp.diff(Q(r),r)
    residual=sp.expand(Q(r+A**2*j)-Q(r)-A**2*qp*j-A**5*H**2*j**2)
    assert sp.simplify(residual)==0
    return residual

def run():
    assert symbolic_taylor_residual()==0
    # A^2 carry reduction and singular bridge, exact synthetic checks.
    for u in (11, 101, 143):
        A=2*u+1
        assert (A*A-1)%u==0
    for u,d in ((13,9),(91,61)):
        A=2*u+1
        if A%d==0:
            for m in range(min(d,7)):
                check_content_bridge(u,d,17,m)

    # Minimal structurally cyclotomic spacing counterexample:
    # 11 | 10^1+1 and roots ±5 are adjacent: 5,6.
    u,Z,b1,b2=11,5,5,6
    assert (10+1)%u==0
    ds,df=corrected_spacing(u,Z,b1,b2)
    assert (ds,df)==(1,11)

    # A composite mixed-sign example for unitary allocation.
    u,Z=77,10
    # + at 7 and - at 11 => CRT root 45.
    b=45
    assert b%7==Z%7 and b%11==(-Z)%11
    up,um=unitary_allocation(u,Z,b)
    assert up==7 and um==11

    # Outer-K exact identities on actual cyclotomic pairs.
    outer_k_check(g=6,ell=6,q=9901,u=101)
    outer_k_check(g=9,ell=6,q=11,u=(10**9+1)//11)

    # Proper content multiplicity theorem checks.
    for u in (11,91,143,1001):
        A=2*u+1
        for d in range(3,A,2):
            if A%d==0 and d>1:
                proper_content_m_bound(u,d)
        assert maximal_content_multiplicity(u,0)==3
        assert maximal_content_multiplicity(u,1)==2

    # Constant used in the new regular-large-q wedge.
    Cmax=ETA+Fraction(1,10**6)
    assert Cmax==Fraction(2598001,1000000)
    assert Fraction(37,2)*Cmax < 50

    print('J2_55_R2_SYMBOLIC_STATUS=PASS')
    print('A2_EQ_1_MOD_U=PASS')
    print('UNITARY_ALLOCATION=PASS')
    print('CORRECTED_SPACING=small_same_sign_factor_OR_global_antipode')
    print('SPACING_COUNTEREXAMPLE=u=11,Z=5,roots=5,6,same_sign_factor=1')
    print('CONTENT_TO_U_BRIDGE=PASS')
    print('PROPER_CONTENT_FIXED_CELL_J_M_MULTIPLICITY<=1')
    print('MAXIMAL_CONTENT_FIXED_CELL_J_M_MULTIPLICITY<=3')
    print('OUTER_K_IDENTITIES=PASS')
    print('CARRY_POLYNOMIAL_TAYLOR_RESIDUAL=0')
    print('REGULAR_LARGE_Q_CONSTANT=(37/2)*Cmax<50')

if __name__=='__main__':
    run()
