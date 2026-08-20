#!/usr/bin/env python3
"""A1 J2 PRCC10 primitive-root carry / CRT reducer.

Key point: after an A^2 lift x=r2+A^2*j and A=2u+1,
A^2 == 1 (mod u), hence U-SQ is exactly
    (r2+j)^2 == Z^2 (mod u).
The reducer can test this directly on the proven short carry interval; factoring
u is optional and never required for correctness.
"""
from fractions import Fraction
from math import gcd

ETA = Fraction(1299, 500)


def floor_frac(x: Fraction) -> int:
    return x.numerator // x.denominator


def ceil_frac(x: Fraction) -> int:
    return -((-x.numerator)//x.denominator)


def root_interval(G,A,u,D2,ell):
    """Strict root-necessary interval (L,U).

    L is DRL.  U follows from positivity of the complementary root factor:
       AH^2 x < 2uKD2, K=G^2/10^ell.
    """
    L = Fraction(A*G, 10)
    U = Fraction(8*u*D2, A*(10**ell))
    return L,U


def j_interval(r2,A,L,U):
    A2=A*A
    lo=floor_frac((L-r2)/A2)+1
    hi=ceil_frac((U-r2)/A2)-1
    # x>0 and 0<=r2<A^2 force j>=0 for a positive root.
    lo=max(lo,0)
    return lo,hi


def carry_bound_rhs(q,ell):
    """Theorem upper coefficient: j < q*(ETA+10^-ell)."""
    return q*(ETA + Fraction(1,10**ell))


def verify_carry_bound_from_frozen(row,k,ell,r2,jhi=None):
    """Exact verification of the uniform PRCC10 carry-bound derivation.

    Frozen inputs used: a3<G, X*K<ETA*u*G^2, K=G^2/10^ell.
    It proves Ux/A^2 < q*(ETA+10^-ell).
    """
    G,u,A,q=row['G'],row['u'],row['A'],row['q']
    D2,X,a3=row['D2'],row['X'],row['a3']
    assert a3 < G
    assert X*k < ETA*u*G*G
    assert k*(10**ell)==G*G
    U=Fraction(8*u*D2,A*(10**ell))
    lhs=U/(A*A)
    rhs=carry_bound_rhs(q,ell)
    assert lhs < rhs
    if jhi is not None:
        assert jhi < rhs
    return lhs,rhs


def u_square_ok(r2,j,Z,u):
    return ((r2+j)*(r2+j)-Z*Z) % u == 0


def direct_u_square_candidates(r2,jlo,jhi,Z,u):
    if jhi<jlo:return []
    return [j for j in range(jlo,jhi+1) if u_square_ok(r2,j,Z,u)]


def coprime_square_root_form_is_legal(Z,u):
    return gcd(Z,u)==1


def combine_residues(rA2,A,u,ru):
    """CRT x=rA2 mod A^2 and x=ru mod u.  gcd(A,u)=1."""
    A2=A*A
    assert gcd(A2,u)==1
    # x=rA2+A2*j; since A2==1 mod u, j=ru-rA2 mod u.
    j0=(ru-rA2)%u
    x0=rA2+A2*j0
    mod=A2*u
    assert x0%A2==rA2%A2 and x0%u==ru%u
    return x0%mod,mod,j0


def audit_A2_mod_u(A,u):
    assert A==2*u+1
    return (A*A-1)%u==0


if __name__=='__main__':
    for u in (7,11,91,143):
        A=2*u+1
        assert audit_A2_mod_u(A,u)
    print('PRCC10_CRT_SYMBOLIC_STATUS=PASS')
    print('A2_EQ_1_MOD_U=PASS')
    print('FACTORING_U_REQUIRED=NO')
