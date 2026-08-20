#!/usr/bin/env python3
"""A1 J2 FQTR6 symbolic certificate.

Exact symbolic expansion and tail-factor identities for the Strict Layer A1-only,
Exact Resonance R=0, J=2 negative deficiency frontier.
All theorem checks are exact (SymPy integers/rationals only).
"""
from fractions import Fraction
from math import gcd
import sympy as sp

q,G,N,t = sp.symbols('q G N t', integer=True)
u = (G+1)/q
A = 2*u + 1
M = q*(q+4)
R = A*t - 2*N
Y = R + u*N*M
E = u*q*((G-1)*t-q*N) + G*Y
P = sp.expand(A*Y**2 + 2*R*E)
Q = sp.expand(q**3 * P)
poly = sp.Poly(Q, G)
assert poly.degree() == 3
C3,C2,C1,C0 = poly.all_coeffs()

C = q**4 + 10*q**3 + 12*q**2 + 8*q
B = (q+2)*(q**2-4*q-4)
assert sp.expand(C0 - (q*N+t)*(C*N-B*t)) == 0

# Explicit coefficient certificates.
E3 = 2*(N**2*q**4 + 8*N**2*q**3 + 16*N**2*q**2
        + 2*N*q**3*t + 12*N*q**2*t + 16*N*q*t
        + 2*q**2*t**2 + 4*q*t**2 + 4*t**2)
E2 = (N**2*q**5 + 10*N**2*q**4 + 40*N**2*q**3 + 64*N**2*q**2
      +2*N*q**4*t + 16*N*q**3*t + 72*N*q**2*t + 80*N*q*t
      +2*q**3*t**2 + 12*q**2*t**2 + 28*q*t**2 + 24*t**2)
E1 = 2*(N**2*q**5 + 9*N**2*q**4 + 20*N**2*q**3 + 20*N**2*q**2
        +N*q**4*t + 10*N*q**3*t + 36*N*q**2*t + 32*N*q*t
        +q**3*t**2 + 5*q**2*t**2 + 16*q*t**2 + 12*t**2)
assert sp.expand(C3-E3)==0
assert sp.expand(C2-E2)==0
assert sp.expand(C1-E1)==0

# Bezout certificate used to show gcd(C,B)|7 (for odd q).
Cbar = q**3 + 10*q**2 + 12*q + 8
bez = sp.expand((-6*q**2+15*q+68)*Cbar + (6*q**2+57*q+40)*B)
assert bez == 224

# q=1 specialization recovers the previous polynomial and exposes the stronger tail.
q1 = [sp.expand(x.subs(q,1)) for x in (C3,C2,C1,C0)]
assert sp.expand(q1[3] - (N+t)*(31*N+21*t)) == 0
r = sp.symbols('r', integer=True)
assert sp.expand((31*N+21*t).subs(N,-t+10*r)) == 10*(31*r-t)

# Small-q classification (<23): q must be a ten-unit divisor of 10^g+1 and A a ten-unit.
def order10_mod(n:int):
    if gcd(n,10)!=1:
        return None
    return int(sp.n_order(10,n))

def minus_one_classes(n:int):
    o=order10_mod(n)
    if o is None:
        return []
    return [j for j in range(1,o+1) if pow(10,j,n)==n-1]

small=[]
for qq in range(2,23):
    if gcd(qq,10)!=1:
        continue
    cls=minus_one_classes(qq)
    if not cls:
        continue
    # A=2u+1, u=(G+1)/q. Mod 5, G+1 == 1 and therefore u == q^{-1}.
    A_mod5=(2*pow(qq,-1,5)+1)%5
    if A_mod5==0:
        continue
    small.append((qq,order10_mod(qq),cls))
assert [x[0] for x in small] == [7,11,17,19]
assert small == [(7,6,[3]),(11,2,[1]),(17,16,[8]),(19,18,[9])]

# Uniform wedge arithmetic checks.
# For q>=7, q+4 <= 11q/7.  For ell<g, g>=6, so the outer coefficient is <37.
assert Fraction(73,2)*Fraction(1000001,1000000)**2 < 37
assert Fraction(330,7)**2 * 37**5 < 40**7

print('SYMBOLIC_STATUS=PASS')
print('DEGREE_G=3')
print('Q3P_COEFF_G3=', sp.factor(C3))
print('Q3P_COEFF_G2=', sp.factor(C2))
print('Q3P_COEFF_G1=', sp.factor(C1))
print('Q3P_CONST=', sp.factor(C0))
print('TAIL_C(q)=', C)
print('TAIL_B(q)=', B)
print('BEZOUT_IDENTITY=', bez)
print('SMALL_Q=', small)
print('Q1_CONST=', q1[3])
print('UNIFORM_COMBINATION_CHECK=PASS')
