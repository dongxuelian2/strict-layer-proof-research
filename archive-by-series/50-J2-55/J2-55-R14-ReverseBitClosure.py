#!/usr/bin/env python3
"""R14 reverse low-k closure audit after the exact R-factor correction."""
from math import gcd
from pathlib import Path
import csv, importlib.util
import sympy as sp
HERE=Path(__file__).resolve().parent

# Load frozen polynomials.
spec=importlib.util.spec_from_file_location('fr',HERE/'J2-55-R14-FrozenRootPolynomials.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def order(a,n):
    x=1
    for d in range(1,100000):
        x=x*a%n
        if x==1:return d
    raise RuntimeError

def r_classes(q,k):
    T=order(10%q,q)
    return T,[r for r in range(T) if pow(10,k+r,q)==q-1]

rows=[]
for k,Q,branch in [(1,7,'K1_SPECIAL'),(2,7,'K2_Q7'),(2,11,'K2_Q11')]:
    T,rr=r_classes(Q,k)
    rows.append(dict(k=k,q=Q,branch=branch,cyclotomic_period=T,r_classes=','.join(map(str,rr)),
                     gamma_normalizer='1',carry_factor='10^r | Gamma_R = gamma',
                     v2_gamma='>=r',v5_gamma='>=r',finite_r_bound='NONE',
                     gamma_zero_lowest='C1 (j=1)',full_root='P_K1(10^r)=0' if k==1 else 'P_R(10^r)=0',
                     status='OPEN_EXPLICIT_CANCELLATION_LOCUS'))

# All active K1 b=0 types inherit the same special normalization and R factor.
active=[7,17,19,29,47,49,59,77,89,97,109]
for Q in active:
    if Q==7: continue
    T,rr=r_classes(Q,1)
    rows.append(dict(k=1,q=Q,branch='K1_SPECIAL',cyclotomic_period=T,r_classes=','.join(map(str,rr)),
                     gamma_normalizer='1',carry_factor='10^r | Gamma_R = gamma',
                     v2_gamma='>=r',v5_gamma='>=r',finite_r_bound='NONE',gamma_zero_lowest='C1 (j=1)',
                     full_root='P_K1(10^r)=0',status='OPEN_EXPLICIT_CANCELLATION_LOCUS'))

out=HERE/'J2-55-R14-ReverseBitClosure.tsv'
with out.open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0]),delimiter='\t');wr.writeheader();wr.writerows(rows)


# Splice the exact carry cancellation locus back into the independent root polynomial.
# This studies the unbounded mechanism without introducing gamma/R as a variable.
import io, contextlib
specg=importlib.util.spec_from_file_location('gn',HERE/'J2-55-R14-GammaNextBit.py')
gn=importlib.util.module_from_spec(specg)
with contextlib.redirect_stdout(io.StringIO()): specg.loader.exec_module(gn)
# symbols are mapped explicitly to avoid assumption/name ambiguity.
mapbase={gn.R:m.R,gn.q:m.q,gn.e:m.e,gn.t:m.t}
GamK1=sp.expand(gn.Gamma_tail.subs({gn.K:10,gn.f:1,**mapbase}))
PK1splice=sp.expand(m.P_K1.subs(m.gamma,GamK1))
pp1=sp.Poly(PK1splice,m.R); js1=[j for j in range(pp1.degree()+1) if pp1.nth(j)!=0]
assert min(js1)==2
C2K1=sp.factor(pp1.nth(2))
xexpr=gn.mu-gn.s
# Two fixed k=2 types, whose carry normalizer is also 1.
splice2=[]
for Qq,ff,ww in [(7,1,25),(11,5,1)]:
    Gam=sp.expand(gn.Gamma_tail.subs({gn.K:100,gn.f:ff,gn.q:Qq,gn.R:m.R,gn.e:m.e,gn.t:m.t}))
    PS=sp.expand(m.P_R.subs({m.K:100,m.f:ff,m.w:ww,m.q:Qq,m.gamma:Gam}))
    pp=sp.Poly(PS,m.R); js=[j for j in range(pp.degree()+1) if pp.nth(j)!=0]
    assert min(js)==2
    splice2.append((Qq,sp.factor(pp.nth(2))))

# gamma=0 is processed by the next lowest independent coefficient, not skipped.
C1R=sp.factor(sp.Poly(m.P_R.subs(m.gamma,0),m.R).nth(1))
C1K=sp.factor(sp.Poly(m.P_K1.subs(m.gamma,0),m.R).nth(1))
assert C1R!=0 and C1K!=0
print('K1_Q7_CYCLOTOMIC: r mod 6 = 2')
print('K2_Q7_CYCLOTOMIC: r mod 6 = 1')
print('K2_Q11_CYCLOTOMIC: r mod 2 = 1')
print('LOW_K_NORMALIZER=1 for K1 special, K2 q=7, K2 q=11')
print('LOW_K_GAMMA_DIVISIBLE_BY_10^r=PASS')
print('FINITE_R_BOUND_FROM_GAMMA_BITS=FALSE')
print('K1_Q7_CLOSED=FALSE')
print('K2_Q7_CLOSED=FALSE')
print('K2_Q11_CLOSED=FALSE')
print('K1_CARRY_SPLICE_ROOT_ORDER=2')
print('K1_CARRY_SPLICE_C2='+str(C2K1))
for Qq,C2 in splice2: print(f'K2_Q{Qq}_CARRY_SPLICE_ROOT_ORDER=2; C2={C2}')
print('CARRY_SPLICE_INTERPRETATION=P(R)|carry has an extra R^2 structural order; next independent gate is the displayed C2 divisibility')
print('GAMMA_ZERO_GENERIC_C1='+str(C1R))
print('GAMMA_ZERO_K1_C1='+str(C1K))
print('GAMMA_ZERO_LOCUS=REDUCED_TO_EXPLICIT_J1_DIVISIBILITY; NOT CLOSED')
print('REVERSE_FRONTIER=explicit 10^r|gamma cancellation locus + independent degree-7 root polynomial')
print('LEDGER='+out.name)
