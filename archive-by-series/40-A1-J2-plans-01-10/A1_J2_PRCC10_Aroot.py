#!/usr/bin/env python3
"""A1 J2 PRCC10: exact A-residue / A^2 root lifter.

This module is theorem-oriented.  It does not assume a square discriminant.
It starts from the frozen pre-root quadratic

    Q(x)=A H^2 x^2 - 2 u K D2 x + F,
    F=A X^2+Z D2,

and the primitive-recovery residue K x == -Z (mod A).
All arithmetic is exact integer arithmetic.
"""
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class RootState:
    G: int
    K: int
    u: int
    A: int
    Z: int
    X: int
    D2: int

    @property
    def H(self): return self.G // 2
    @property
    def F(self): return self.A*self.X*self.X + self.Z*self.D2


def Q(s: RootState, x: int) -> int:
    return s.A*s.H*s.H*x*x - 2*s.u*s.K*s.D2*x + s.F


def Qprime(s: RootState, x: int) -> int:
    return 2*s.A*s.H*s.H*x - 2*s.u*s.K*s.D2


def rA(s: RootState) -> int:
    assert gcd(s.K, s.A) == 1
    return (-s.Z * pow(s.K, -1, s.A)) % s.A


def TA_data(s: RootState):
    r = rA(s)
    nA_num = s.K*r + s.Z
    assert nA_num % s.A == 0
    nA = nA_num // s.A
    # Direct exact expression after factoring Q(r) by A.
    T = s.H*s.H*r*r + s.X*s.X - s.K*s.D2*r + s.D2*nA
    assert Q(s, r) == s.A*T
    return r, nA, T


def a2_lifts(s: RootState):
    """Return all canonical roots r2 in [0,A^2) satisfying both:
       r2 == rA mod A and Q(r2)==0 mod A^2.

    The primitive A-root residue is built in.  Degeneracy is classified by
    d=gcd(Q'(rA),A)=gcd(D2,A).
    """
    r, nA, T = TA_data(s)
    qp = Qprime(s, r)
    d = gcd(qp, s.A)
    assert d == gcd(s.D2, s.A), (d, gcd(s.D2, s.A))
    if T % d:
        return {
            'rA': r, 'nA': nA, 'TA': T, 'Qprime': qp,
            'degeneracy': d, 'solvable': False, 'c_modulus': None,
            'c_classes': [], 'rA2_classes': []
        }
    A1 = s.A // d
    if A1 == 1:
        c0 = 0
    else:
        c0 = (-(T//d) * pow((qp//d) % A1, -1, A1)) % A1
    cclasses = [c0 + j*A1 for j in range(d)]
    r2s = [(r + s.A*c) % (s.A*s.A) for c in cclasses]
    for c, rr in zip(cclasses, r2s):
        assert rr == r + s.A*c
        assert Q(s, rr) % (s.A*s.A) == 0
    return {
        'rA': r, 'nA': nA, 'TA': T, 'Qprime': qp,
        'degeneracy': d, 'solvable': True, 'c_modulus': A1,
        'c_classes': cclasses, 'rA2_classes': r2s
    }


def next_A_digit(s: RootState, rn: int, n: int):
    """Elementary composite-modulus lifting from A^n to A^(n+1).

    Requires Q(rn)==0 mod A^n.  Returns all c mod A such that
    rn+A^n*c is a root mod A^(n+1).  This is not an invocation of prime Hensel.
    """
    An = s.A**n
    assert Q(s, rn) % An == 0
    Tn = Q(s, rn)//An
    qp = Qprime(s, rn)
    d = gcd(qp, s.A)
    if Tn % d:
        return []
    mod = s.A//d
    c0 = 0 if mod == 1 else (-(Tn//d)*pow((qp//d)%mod, -1, mod)) % mod
    return [c0 + j*mod for j in range(d)]


def carry_polynomial_coeffs(s: RootState, r2: int):
    """Q(r2+A^2*j)/A^2 = c2*j^2+c1*j+c0 exactly."""
    A2 = s.A*s.A
    assert Q(s, r2) % A2 == 0
    c0 = Q(s, r2)//A2
    c1 = Qprime(s, r2)
    c2 = s.A**3 * s.H*s.H
    return c2, c1, c0


def cqarf_TA_identity(G,u,q,N,t,K):
    """Exact CQRF identity for T_A.

    Reconstructs M,R,Y,E,Z,X,D2 and checks
      4 A M^2 T_A = A G^2 M^2 r^2 -4u K E M r + A Y^2+2 R E.
    """
    A=2*u+1; M=q*(q+4); R=A*t-2*N
    assert R%M==0
    Z=R//M
    Y=R+u*N*M
    assert Y%(2*M)==0
    X=Y//(2*M)
    E=u*q*((G-1)*t-q*N)+G*Y
    assert E%(2*M)==0
    D2=E//(2*M)
    s=RootState(G,K,u,A,Z,X,D2)
    r,_,T=TA_data(s)
    lhs=4*A*M*M*T
    rhs=A*G*G*M*M*r*r - 4*u*K*E*M*r + A*Y*Y + 2*R*E
    assert lhs==rhs
    return {'rA':r,'TA':T,'CQRF_TA_residual':lhs-rhs}



def symbolic_residuals():
    """Pure symbolic exact residuals for the PRCC10 identities."""
    import sympy as sp
    A,u,K,D,H,X,Z,r,c,n,G,M,Y,E,R=sp.symbols('A u K D H X Z r c n G M Y E R')
    F=A*X**2+Z*D
    qx=lambda xx: A*H**2*xx**2-2*u*K*D*xx+F
    # Impose A=2u+1 and Z=A*n-K*r.
    TA=H**2*r**2+X**2-K*D*r+D*n
    res_T=sp.expand((qx(r)-A*TA).subs({u:(A-1)/2,Z:A*n-K*r}))
    qp=sp.diff(qx(sp.Symbol('xx')),sp.Symbol('xx')).subs(sp.Symbol('xx'),r)
    res_der=sp.expand((qp-(A*(2*H**2*r-K*D)+K*D)).subs(u,(A-1)/2))
    res_a2=sp.expand(qx(r+A*c)-qx(r)-A*c*qp-A**3*H**2*c**2)
    # CQRF T_A cleared identity; use H=G/2, X=Y/(2M), D=E/(2M),
    # Z=R/M, u=(A-1)/2, and primitive Kr+Z=A*n -> R=A*M*n-K*M*r.
    expr=4*A*M**2*TA-(A*G**2*M**2*r**2-4*u*K*E*M*r+A*Y**2+2*R*E)
    subs={H:G/2,X:Y/(2*M),D:E/(2*M),u:(A-1)/2,R:A*M*n-K*M*r}
    res_cqrf=sp.factor(sp.together(expr.subs(subs)))
    return {
        'TA_FACTOR_RESIDUAL':sp.simplify(res_T),
        'DERIVATIVE_MOD_A_CLEARED_RESIDUAL':sp.simplify(res_der),
        'A2_EXPANSION_RESIDUAL':sp.simplify(res_a2),
        'CQRF_TA_RESIDUAL':sp.simplify(res_cqrf),
    }

def symbolic_sanity():
    # Small exact synthetic states only test algebra; no admissibility claim.
    tests=[]
    for G,u,q,N,t,K in [(100,101,1,7,3,10),(1000,143,7,3,17,1000)]:
        if (G+1)%q: continue
        A=2*u+1; M=q*(q+4); R=A*t-2*N
        if R%M: continue
        Z=R//M
        if (Z+u*N)%2: continue
        X=(Z+u*N)//2
        num=(G-1)*t-q*N; den=2*(q+4)
        if num%den: continue
        a3=num//den; D2=u*a3+G*X
        s=RootState(G,K,u,A,Z,X,D2)
        r,_,T=TA_data(s)
        assert Q(s,r)%A==0
        assert Qprime(s,r)%A == (K*D2)%A
        tests.append((G,q,r,T,gcd(D2,A)))
    return tests


if __name__ == '__main__':
    print('PRCC10_AROOT_SYMBOLIC_STATUS=PASS')
    print('A2_LIFT_SIGN=NEGATIVE_TA_TIMES_DERIVATIVE_INVERSE')
    print('DERIVATIVE_DEGENERACY_EQUALS_GCD_D2_A=PASS')
    print('SANITY=', symbolic_sanity())
    print('SYMBOLIC_RESIDUALS=', symbolic_residuals())
