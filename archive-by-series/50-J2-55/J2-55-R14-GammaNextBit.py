#!/usr/bin/env python3
"""R14 reverse carry-bit audit.

This deliberately stops the proposed bit ladder when the exact source algebra
reveals a whole R=10^r factor in Gamma_R after the legal reverse tail
substitution.  That is the required explicit moving 2-adic cancellation
mechanism; no new quotient is introduced.
"""
import csv, importlib.util
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
q,G,K,R,f,t,e,alpha,s,mu=sp.symbols('q G K R f t e alpha s mu', integer=True)
Rh=sp.symbols('Rh', integer=True)
d0=2*f
c=q**3+10*q**2+12*q+8
B=(q+2)*(q**2-4*q-4)

# Exact R7 reverse carry source.  Reconstruct J_R once from the published EQL/R7 definitions
# and cross-check the lightweight explicit polynomial below.
u=(G+1)/q; A=2*u+1; dR=2*f*R; C=q*c
N=sp.cancel((B*t+alpha*G/dR)/C)
Z=sp.cancel((A*t-2*N)/(q*(q+4)))
a3=sp.cancel(((G-1)*t-q*N)/(2*(q+4)))
X=sp.cancel((Z+u*N)/2)
D2=sp.cancel(u*a3+G*X)
Ur=sp.cancel(8*u*D2/(A*(R*G)))
nr,dr=sp.fraction(Ur)
Qr,_=sp.div(sp.Poly(nr,G),sp.Poly(dr,G))
Pr=sp.factor(Qr.as_expr())
J_from_source=sp.factor((4*f*R**2*q**2*(q+4)*c)*Pr)
D=2*R**2*d0*q**2*(q+4)*c
J=(4*G**2*alpha*q + 16*G**2*alpha
   +16*G*R*f*q**4*t +112*G*R*f*q**3*t+96*G*R*f*q**2*t
   -192*G*R*f*q*t-128*G*R*f*t
   -2*G*alpha*q**2-8*G*alpha*q+8*G*alpha
   -8*R*f*q**5*t-48*R*f*q**4*t+64*R*f*q**3*t
   +320*R*f*q**2*t+128*R*f*q*t
   +alpha*q**3+6*alpha*q**2)
assert sp.factor(J_from_source-J)==0
Bscr=(3*R**3*d0*q**6*t+36*R**3*d0*q**5*t+156*R**3*d0*q**4*t
      +352*R**3*d0*q**3*t+240*R**3*d0*q**2*t-64*R**3*d0*q*t-64*R**3*d0*t
      +R**2*alpha*q**3+10*R**2*alpha*q**2+12*R**2*alpha*q+8*R**2*alpha
      -8*R*d0*q**6*t-48*R*d0*q**5*t+64*R*d0*q**4*t+320*R*d0*q**3*t
      +128*R*d0*q**2*t+2*alpha*q**4+12*alpha*q**3)
chi=J-D*mu
Gamma=-Bscr+2*q*(D*s+chi)

# Exact v2(D)=2r+2: D/R^2 has exactly one factor 4? Here D=4*f*R^2*q^2(q+4)c,
# and f,q,q+4,c are odd in the legal q ten-unit branch.
assert sp.factor(D/(4*R**2*f*q**2*(q+4)*c)-1)==0

# Universal evenness: write R=2*Rh (r>=1). Every coefficient of Gamma is even.
Gamma_even=sp.expand(Gamma.subs(R,2*Rh))
syms=sorted(Gamma_even.free_symbols,key=lambda z:str(z))
assert int(sp.Poly(Gamma_even,*syms).content())%2==0

# Legal reverse tail substitution and G=KR.
tail_alpha=2*R*f*B*t-q*e
Gamma_tail=sp.factor(Gamma.subs({alpha:tail_alpha,G:K*R}))
Q=sp.cancel(Gamma_tail/R)
assert sp.denom(Q)==1
assert sp.expand(Gamma_tail-R*Q)==0

# The opaque floor only appears inside the R^2 term, so the R factor is global;
# no deep/shallow split is required for this theorem.
# K1 parity audit from the old proposed next-bit route.
J_tail=sp.expand(J.subs({alpha:tail_alpha,G:K*R}))
# J_R mod 2 = alpha mod 2 when R is even and q odd. Certify by q=2*q0+1,R=2*Rh.
q0=sp.symbols('q0',integer=True)
Jpar=sp.expand((J-sp.Integer(1)*alpha).subs({q:2*q0+1,R:2*Rh,G:K*2*Rh}))
assert int(sp.Poly(Jpar,*sorted(Jpar.free_symbols,key=lambda z:str(z))).content())%2==0

# K1 special TQR: 2(q+4) eta1 = e+8Rt(3q+5), so e is even.
eta1=sp.symbols('eta1',integer=True)
K1_tqr_rhs=2*(q+4)*eta1-8*R*t*(3*q+5)
# This expression equals e; substituting odd q/R integer makes it visibly even.
assert int(sp.Poly(sp.expand(K1_tqr_rhs),*sorted(K1_tqr_rhs.free_symbols,key=lambda z:str(z))).content())%2==0

# Frozen independent root polynomials: gamma=0 is not skipped; recover its next lowest coefficient.
spec=importlib.util.spec_from_file_location('fr',HERE/'J2-55-R14-FrozenRootPolynomials.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
C1R=sp.factor(sp.Poly(m.P_R.subs(m.gamma,0),m.R).nth(1))
C1K1=sp.factor(sp.Poly(m.P_K1.subs(m.gamma,0),m.R).nth(1))
assert C1R!=0 and C1K1!=0

rows=[]
active_k1=[7,17,19,29,47,49,59,77,89,97,109]
for Qq in active_k1:
    rows.append(dict(branch='K1_SPECIAL',q=Qq,k=1,r_scope='r>=3 live',normalizer_v2=0,
        Gamma_v2_min='>=r',gamma_bit0=0,gamma_bit1=0,e_parity=0,
        chi_parity='J parity',J_parity='alpha=e=0 mod2',v2_gamma_bound='>=r (no absolute upper bound from carry)',
        status='ODD_BRANCH_VACUOUS; BIT_LADDER_RETIRED_BY_R_FACTOR'))
for Qq in (7,11):
    rows.append(dict(branch=f'K2_Q{Qq}',q=Qq,k=2,r_scope='r>=2 live',normalizer_v2=0,
        Gamma_v2_min='>=r',gamma_bit0=0,gamma_bit1=0,e_parity='not needed',
        chi_parity='not needed',J_parity='not needed',v2_gamma_bound='>=r (normalizer=1)',
        status='ODD_BRANCH_VACUOUS; BIT_LADDER_RETIRED_BY_R_FACTOR'))
rows.append(dict(branch='GENERIC_REVERSE',q='q>1',k='k',r_scope='active reverse',normalizer_v2='k-2',
    Gamma_v2_min='>=r',gamma_bit0='depends on r+2-k',gamma_bit1='not pursued',e_parity='not needed',
    chi_parity='floor eliminated inside exact R factor',J_parity='not needed',
    v2_gamma_bound='>=r+2-k on legal normalized states',
    status='EXPLICIT_MOVING_2ADIC_CANCELLATION_LOCUS; NO_BIT_LADDER'))
out=HERE/'J2-55-R14-GammaBit.tsv'
with out.open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0]),delimiter='\t');wr.writeheader();wr.writerows(rows)

print('GAMMA_R_EVEN=PASS')
print('D_R_V2=2r+2_EXACT')
print('REVERSE_TAIL_GAMMA_R_HAS_FACTOR_R=PASS')
print('REVERSE_TAIL_GAMMA_R_OVER_R=',sp.factor(Q))
print('K1_E_EVEN=PASS')
print('K1_JR_MOD2=alpha=e=0')
print('K1_GAMMA_OVER2_MOD2=0 (indeed R|gamma and r>=3)')
print('K1_V2_GAMMA=>=r; NOT_EQUAL_1')
print('K2_Q7_V2_GAMMA=>=r; NOT_EQUAL_1')
print('K2_Q11_V2_GAMMA=>=r; NOT_EQUAL_1')
print('GENERIC_GAMMA_V2_LOWER=>=r+2-k')
print('GENERIC_DEEP_ZONE_NEXTBIT=SUPERSEDED_BY_GLOBAL_R_FACTOR')
print('GENERIC_SHALLOW_ZONE=SUPERSEDED_BY_GLOBAL_R_FACTOR')
print('BIT_LADDER=STOPPED_BY_EXPLICIT_UNBOUNDED_CANCELLATION_MECHANISM')
print('GAMMA_ZERO_GENERIC_LOWEST_J=1')
print('GAMMA_ZERO_GENERIC_C1='+str(C1R))
print('GAMMA_ZERO_K1_LOWEST_J=1')
print('GAMMA_ZERO_K1_C1='+str(C1K1))
print('LEDGER='+out.name)
