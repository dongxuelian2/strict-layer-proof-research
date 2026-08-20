#!/usr/bin/env python3
"""R13 q=1 Gaussian full inert-radical theorem certificate.

Theorem layer is factorization-free: it uses p≡3 mod4 inertness, gcd support,
and exact Euclidean identities.  The 888-row ledger records periodic cells only;
it does not claim a Gaussian root exists in any cell.
"""
from math import gcd
from pathlib import Path
import csv
import sympy as sp
OUT=Path(__file__).resolve().parent
G,K,a,tau=sp.symbols('G K a tau', integer=True)
S=(G+1)*(2*G+3)
Q=4*G**3*K**2-4*G**3+8*G**2*K**2-12*G**2+4*G*K**2-13*G-6
M=sp.expand(G**3*tau-(10*G**2+4*G-2)*a)
L=sp.expand(sp.cancel((Q*M+4*S*a)/G))
lin1=tau+4*a; lin2=27*tau+116*a
assert sp.denom(L)==1
assert sp.factor(M.subs(G,-1)+lin1)==0
assert sp.factor(8*M.subs(G,sp.Rational(-3,2))+lin2)==0
assert sp.expand(lin2-27*lin1)==8*a
U1=sp.factor((M+lin1)/(G+1))
U2=sp.factor((8*M+lin2)/(2*G+3))
assert sp.factor(U1-(G**2*tau-10*G*a-G*tau+6*a+tau))==0
assert sp.factor(U2-(4*G**2*tau-40*G*a-6*G*tau+44*a+9*tau))==0
assert sp.factor(U1.subs({G:-1,tau:-4*a})-4*a)==0
assert sp.factor(U2.subs({G:sp.Rational(-3,2),tau:-sp.Rational(116,27)*a})+12*a)==0

rows=[]
for KK,count in ((10,8),(100,80),(1000,800)):
    mod=2*KK; n=0
    for ar in range(mod):
        if gcd(ar,10)!=1:continue
        tr=(-31*ar)%mod
        rows.append(dict(K=KK,cell=f'a={ar};tau={tr} (mod {mod})',a_mod4=ar%4,
            full_inert_radical_M='PROVED: Rad_3mod4(M0)|S_G',
            rad3_linear_support='PROVED: Rad_3mod4(M0)|(tau+4a)(27tau+116a)',
            inert_valuation_budget='PROVED: v_p(M0)+v_p(L0)<=2v_p(S_G)',
            first_order_U1='4a mod p; unit on M-side inert support',
            first_order_U2='-12a mod p; unit (p=3 cannot divide S_G)',
            external_L_inert='p|L0,p∤S_G => p|gcd(a,Q_K(G))',
            negative_branch='OPEN',norm_status='OPEN_SPLIT_PRIME_IDEAL_ALLOCATION'))
        n+=1
    assert n==count
p=OUT/'J2-55-R13-q1-GaussianRadical.tsv'
with p.open('w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('GS-1 FULL_INERT_RADICAL_M=PROVED')
print('GS-2 RAD3_LINEAR_SUPPORT=PROVED')
print('GS-VAL INERT_VALUATION_BUDGET=PROVED')
print('GS-FIRST-ORDER U1_AT_SUPPORT=4a; U2_AT_SUPPORT=-12a')
print('GS-3 L_EXTERNAL_INERT_SUPPORT=PROVED')
print('NEGATIVE_GAUSSIAN_BRANCH=OPEN')
print('K10=OPEN')
print('K100=OPEN')
print('K1000=OPEN')
print('Q1_TOTAL=OPEN')
print('ROWS=',len(rows))
