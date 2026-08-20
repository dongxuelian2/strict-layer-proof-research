#!/usr/bin/env python3
"""J2-55 R12 reverse full-root polynomial / low-k audit.

Uses the genuinely new carry-saturated FULL-root degree-7 polynomial.
It deliberately distinguishes:
  * exact new gate R | C0(e,t,gamma);
  * fixed-coefficient rational-root finiteness;
  * R10 periodic residue cells, which do NOT freeze e,t,gamma.
"""
from math import gcd,lcm
from pathlib import Path
import csv, importlib.util
import sympy as sp

OUT=Path('/mnt/data')
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    "rootcert", HERE/"J2-55-R12-RootSaturation-symbolic.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def ordmod(a,m):
    if m==1:return 1
    if gcd(a,m)!=1:return None
    x=1
    for d in range(1,1000000):
        x=x*a%m
        if x==1:return d
    raise RuntimeError

def decimal_split(m):
    a=b=0;n=m
    while n%2==0:a+=1;n//=2
    while n%5==0:b+=1;n//=5
    return a,b,n

def eventual_R_residues(q,k,mod):
    a,b,unit=decimal_split(mod); stab=max(a,b,1)
    T=lcm(ordmod(10,q),ordmod(10,unit) if unit>1 else 1)
    out=[]
    for rr in range(T):
        r=stab+rr
        if pow(10,r+k,q)!=(q-1)%q:continue
        out.append((rr,pow(10,r,mod)))
    return stab,T,sorted(set(out))

R,q,K,e,f,w,t,gamma=m.R,m.q,m.K,m.e,m.f,m.w,m.t,m.gamma
Cgen=sp.factor(sp.Poly(m.P_R,R).nth(0))
Ck1=sp.factor(sp.Poly(m.P_K1,R).nth(0))
assert sp.factor(Cgen.subs(q,0)+2*K**2*gamma**2)==0
assert sp.factor(Ck1.subs(q,0)-10*gamma**2)==0

rows=[]
def add_k1_q7():
    Q=7;k=1;D=2*(Q+4); base_tmod=lcm(D,10); tref=lcm(base_tmod,Q)
    stab,T,Rres=eventual_R_residues(Q,k,D)
    for rr,Rm in Rres:
        for tr in range(tref):
            if tr%2==0 or tr%5:continue
            er=(-8*Rm*(tr%D)*(3*Q+5))%D
            rows.append(dict(k=k,q=Q,branch='K1_SPECIAL',period=T,r_class=rr,
                modulus=D,t_modulus=tref,t_residue=tr,e_residue=er,
                degree=7,content='primitive_after_structural_R',
                lowest_power=0,
                constant_term='gamma*(80e q^3+5gamma(q+2)-32q^4(q+4)t)',
                constant_mod_q='10 gamma^2',
                q_div_t='YES' if tr%Q==0 else 'NO',
                possible_r='FIXED_(e,t,gamma)_FIBRE_ONLY',
                exact_root_survivors='UNRESOLVED',
                status='OPEN_MOVING_COEFFICIENTS'))
def add_k2(Q):
    k=2
    if Q==7:
        ff=1;D=Q+4;base_tmod=lcm(D,50)
        condition=lambda tr: tr%2==1 and tr%25==0
    else:
        ff=5;D=(Q+4)//ff;base_tmod=lcm(D,10)
        condition=lambda tr: gcd(tr,10)==1
    tref=lcm(base_tmod,Q)
    stab,T,Rres=eventual_R_residues(Q,k,D)
    for rr,Rm in Rres:
        for tr in range(tref):
            if not condition(tr):continue
            er=(-8*Rm*ff*(tr%D)*(3*Q+5))%D
            rows.append(dict(k=k,q=Q,branch=f'K2_Q{Q}_GENERIC',period=T,r_class=rr,
                modulus=D,t_modulus=tref,t_residue=tr,e_residue=er,
                degree=7,content='primitive_after_structural_R^2',
                lowest_power=0,
                constant_term='gamma*(-K^2 gamma(q+2)-64K e f^2 q^3 w+256f^3 q^4(q+4)tw)',
                constant_mod_q='-2K^2 gamma^2',
                q_div_t='YES' if tr%Q==0 else 'NO',
                possible_r='FIXED_(e,t,gamma)_FIBRE_ONLY',
                exact_root_survivors='UNRESOLVED',
                status='OPEN_MOVING_COEFFICIENTS'))

add_k1_q7();add_k2(7);add_k2(11)

p=OUT/'J2-55-R12-ReverseRootPolynomial.tsv'
fields=['k','q','branch','period','r_class','modulus','t_modulus','t_residue','e_residue',
        'degree','content','lowest_power','constant_term','constant_mod_q','q_div_t',
        'possible_r','exact_root_survivors','status']
with p.open('w',newline='',encoding='utf-8') as fobj:
    wr=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(rows)

for typ in [(1,7),(2,7),(2,11)]:
    rr=[x for x in rows if (x['k'],x['q'])==typ]
    qnot=sum(x['q_div_t']=='NO' for x in rr)
    qyes=len(rr)-qnot
    print(f'k={typ[0]},q={typ[1]} REFINED_CELLS={len(rr)} q∤t={qnot} q|t={qyes}')
print('NEW_EXACT_GATE=actual full root => R divides carry-saturated primitive constant coefficient C0')
print('C0_ZERO_ON_q_NOT_DIV_t=IMPOSSIBLE by C0 mod q and inherited gamma mod q = unit*t')
print('FIXED_COEFFICIENT_FIBRE=FINITE_R via 10^r|C0 when C0!=0')
print('R10_PERIODIC_CELL_FREEZES_e_t_gamma=FALSE')
print('K1_Q7_CLOSED=False')
print('K2_Q7_CLOSED=False')
print('K2_Q11_CLOSED=False')
print('LOWK_TYPE_CLOSURE_NOT_CLAIMED=PASS')
print('LEDGER='+p.name)
