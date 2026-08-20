#!/usr/bin/env python3
"""J2-65 R2: branch-independent pre-floor bivariate master-root certificate.

Source reconstruction only.  No R12 frozen polynomial is imported.
The full-root normalization is
    R(x)=A*(L/8)*x^2-u*D2*x+Omega,
and source recovery gives Omega=F/(2K), F=A*X^2+Z*D2.
With KL=G^2, clearing the structural Laurent monomial K gives
    Qclr=A*G^2*x^2-8*K*u*D2*x+4*F.
All structural-definitional variables are then substituted exactly.
"""
from pathlib import Path
import csv, hashlib
import sympy as sp

HERE=Path(__file__).resolve().parent
G,K,L,q,d,alpha,t,x=sp.symbols('G K L q d alpha t x', integer=True)
u,A,B,c,N,Z,a3,X,D2,F,Omega=sp.symbols('u A B c N Z a3 X D2 F Omega')

c0=q**3+10*q**2+12*q+8
B0=(q+2)*(q**2-4*q-4)
u0=(G+1)/q
A0=2*u0+1
N0=sp.cancel((B0*t+alpha*G/d)/(q*c0))
Z0=sp.cancel((A0*t-2*N0)/(q*(q+4)))
a30=sp.cancel(((G-1)*t-q*N0)/(2*(q+4)))
X0=sp.cancel((Z0+u0*N0)/2)
D20=sp.cancel(u0*a30+G*X0)
F0=sp.cancel(A0*X0**2+Z0*D20)
Omega0=sp.cancel(F0/(2*K))
L0=G**2/K
ROOT0=sp.cancel(A0*(L0/8)*x**2-u0*D20*x+Omega0)
QCLR=sp.cancel(8*K*ROOT0)
QCLR_EXPECTED=sp.cancel(A0*G**2*x**2-8*K*u0*D20*x+4*F0)
assert sp.cancel(QCLR-QCLR_EXPECTED)==0
QNUM,QDEN=map(sp.factor,sp.fraction(QCLR))
DEN_EXPECTED=d**2*q**5*(q+4)**2*c0**2
assert sp.factor(QDEN-DEN_EXPECTED)==0
QNUM=sp.expand(QNUM)
P=sp.Poly(QNUM,G,K)
SUPPORT=sorted([m for m,cx in P.terms() if cx!=0], key=lambda z:(z[1],z[0]))
EXPECTED=[(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(3,1),(4,1)]
assert SUPPORT==EXPECTED
assert sp.Poly(QNUM,x).degree()==2

# Convex hull for these integer support points.
def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    pts=sorted(set(points))
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
HULL=hull(SUPPORT)
assert set(HULL)=={(1,0),(5,0),(4,1),(0,1)} and len(HULL)==4

C50=sp.factor(P.coeff_monomial(G**5))
C41=sp.factor(P.coeff_monomial(G**4*K))
assert sp.factor(C50-2*alpha**2*(q+4)**2)==0
assert sp.factor(C41+4*alpha*d*q**2*x*(q+4)**2*c0)==0
BOUNDARY_TOP=sp.factor(C50+C41)
assert sp.factor(BOUNDARY_TOP-2*alpha*(q+4)**2*(alpha-2*d*q**2*c0*x))==0

# alpha=0 is the first support-degeneration locus.
P0=sp.Poly(sp.expand(QNUM.subs(alpha,0)),G,K)
SUPPORT_ALPHA0=sorted([m for m,cx in P0.terms() if cx!=0], key=lambda z:(z[1],z[0]))
assert SUPPORT_ALPHA0==[(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1)]
C31_A0=sp.factor(P0.coeff_monomial(G**3*K))

# q=1 is algebraically defined; denominator remains nonzero as formal positive structural data.
Q1DEN=sp.factor(QDEN.subs(q,1))
assert Q1DEN==25*d**2*31**2

# emit compact master expression rather than a reverse-engineered chart polynomial.
master_txt=HERE/'J2-65-R2-Level1MasterRoot.txt'
master_txt.write_text(
    'LEVEL0_ROOT = A*(G^2/(8K))*x^2-u*D2*x+F/(2K)\n'
    'CLEARING_MONOMIAL = 8*K\n'
    'LEVEL1_QCLR = A*G^2*x^2-8*K*u*D2*x+4*F\n'
    'DEFINITIONAL_SUBSTITUTION = u=(G+1)/q; A=2u+1; B=(q+2)(q^2-4q-4); '
    'c=q^3+10q^2+12q+8; N=(Bt+alpha*G/d)/(qc); Z=(At-2N)/(q(q+4)); '
    'a3=((G-1)t-qN)/(2(q+4)); X=(Z+uN)/2; D2=u*a3+GX; F=A*X^2+ZD2\n'
    f'QDEN = {sp.factor(QDEN)}\n'
    f'QNUM_SHA256 = {hashlib.sha256(str(QNUM).encode()).hexdigest()}\n',encoding='utf-8')

print('J2-65 R2 MASTER ROOT CERTIFICATE')
print('LEVEL0_UNIVERSAL_ROOT=PROVED')
print('OMEGA_EQUALS_F_OVER_2K=PROVED')
print('MONOMIAL_RELATION_KL_EQUALS_G2=PROVED')
print('CLEARING_MONOMIAL=8*K')
print('LEVEL1_STRUCTURAL_SATURATED_ROOT=PROVED')
print('QDEN='+str(QDEN))
print('QNUM_DEG_G='+str(sp.Poly(QNUM,G).degree()))
print('QNUM_DEG_K='+str(sp.Poly(QNUM,K).degree()))
print('QNUM_DEG_X='+str(sp.Poly(QNUM,x).degree()))
print('SUPPORT='+str(SUPPORT))
print('NEWTON_VERTICES='+str(HULL))
print('EXPOSED_PHYSICAL_PAIR=[(5,0),(4,1)]')
print('C_5_0='+str(C50))
print('C_4_1='+str(C41))
print('BOUNDARY_TOP_FACE='+str(BOUNDARY_TOP))
print('ALPHA_ZERO_SUPPORT='+str(SUPPORT_ALPHA0))
print('ALPHA_ZERO_DOMINANT_C_3_1='+str(C31_A0))
print('Q1_MASTER_DEGENERATION=NONE')
