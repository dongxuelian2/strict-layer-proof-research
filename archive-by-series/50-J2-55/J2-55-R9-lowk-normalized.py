#!/usr/bin/env python3
"""R9 low-k normalized ledger after correcting the reverse R-factor."""
from math import gcd

def vp(n,p):
    c=0
    while n and n%p==0:c+=1;n//=p
    return c

def cfun(q): return q**3+10*q*q+12*q+8

def first_r(k,q,limit=5000):
    x=10**k % q
    ten=10%q
    for r in range(1,limit+1):
        x=x*ten%q
        if x==q-1:return r
    raise ValueError((k,q))

active_k1=[7,17,19,29,47,49,59,77,89,97,109]
deep5=[11,61,91,101]
print('kind\tk\tq\tb\tv5c\tvaluation\tlambda_residue\tgamma_sync\tstatus')
for q in active_k1:
    k=1;b=0;r=first_r(k,q);R=pow(10,r,q)
    lc=(4*R)%q
    # 5|t => carry normalization is trivial: gamma_R=Gamma_R.
    # Gamma_R=256 R^3 t; lambda_R=4R t => gamma=64R^2 lambda.
    gc=(64*R*R)%q
    assert lc==(-4*pow(10,-1,q))%q
    print(f'ACTIVE_K1\t1\t{q}\t0\t{vp(cfun(q),5)}\t5|t PROVED\t'
          f'lambda_R={lc}*t (mod q)\tgamma_R={gc}*lambda_R (mod q)\tOPEN_FIXED_TYPE')

# k=2,q=7
q=7;k=2;b=0;r=first_r(k,q);R=pow(10,r,q)
lc=(8*R)%q;gc=(32*R*R)%q
assert lc==3 and gc==1
print(f'ACTIVE_K2\t2\t7\t0\t{vp(cfun(7),5)}\t25|t PROVED\t'
      f'lambda_R={lc}*t (mod 7)\tgamma_R={gc}*lambda_R (mod 7)\tOPEN_FIXED_TYPE')

# k=2,q=11: moderate only when v5(t)=0; then M=C=1.
q=11;k=2;b=1;r=first_r(k,q);R=pow(10,r,q)
lc=(8*R*25)%q;gc=(-128*pow(R,3,q)*5)%q
assert lc==9 and gc==2
print(f'ACTIVE_K2\t2\t11\t1\t{vp(cfun(11),5)}\tno new 5-content; moderate iff v5(t)=0\t'
      f'lambda_R={lc}*t (mod 11)\tgamma_R={gc}*lambda_R (mod 11)\tOPEN_FIXED_TYPE')

for q in deep5:
    print(f'DEEP5_K1\t1\t{q}\t{vp(q+4,5)}\t{vp(cfun(q),5)}\tPRE-VALUATION ONLY\tN/A\tN/A\tOPEN_DEEP5_FIXED_TYPE')

print('R8_REVERSE_LOWK_RESIDUES=CORRECTED')
print('OLD_K1=lambda_R=4*t; NEW_K1=lambda_R=4*R*t=-4*10^{-1}*t (mod q)')
print('OLD_K2_Q7=lambda_R=8*t; NEW_K2_Q7=lambda_R=8*R*t=3*t (mod 7)')
print('K2_Q11_MODERATE=lambda_R=9*t (mod 11), gamma_R=2*lambda_R (mod 11)')
print('DEEP5_ACTIVE_TAIL_FORMULA=NOT_USED')
print('LOWK_STATUS=PASS_OPEN_TYPES_EXPLICIT')
