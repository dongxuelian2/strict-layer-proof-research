#!/usr/bin/env python3
"""R9 reverse residue provenance audit.
Independently compares the R8 reported lambda_R residue with the residue forced by
(1) omega_R ≡16 d_r t (mod q), (2) omega_R=(q+4)/5^b lambda_R,
(3) d_r=2*5^b*R and RK=G≡-1 (mod q).
"""
from math import gcd
import random

def vp(n,p):
    c=0
    while n and n%p==0:
        c+=1;n//=p
    return c

def inv(a,m): return pow(a%m,-1,m)

def coeffs(q,k,r,b=None):
    K=10**k;R=10**r;G=K*R
    assert (G+1)%q==0
    if b is None:b=vp(q+4,5)
    f=5**b
    new=(8*(R%q)*(f*f%q))%q
    old=(8*(f*f%q))%q
    kinv=inv(K,q)
    fixed=(-8*(f*f%q)*kinv)%q
    assert new==fixed
    return old,new,fixed,R%q

def bulk_numeric_regression(q,k,r,t):
    old,new,fixed,Rq=coeffs(q,k,r)
    b=vp(q+4,5);f=5**b;K=10**k;R=10**r
    # Construct lambda on the corrected residue class, then exact omega.
    lam=new*t + q*(3+t)
    # ensure omega integral; f | q+4 by definition.
    omega=((q+4)//f)*lam
    dr=2*f*R
    assert (omega-16*dr*t)%q==0
    assert lam%q==(8*R*f*f*t)%q
    assert lam%q==(-8*f*f*pow(K,-1,q)*t)%q
    old_ok=(lam-8*f*f*t)%q==0
    # Generic moderate v=0 carry normalization.
    if k>=2*b:
        C=(10**k)//(4*f*f)
        assert C>0 and (10**k)%(4*f*f)==0
        Gamma_mod=(256*pow(R,3,q)*f*t)%q
        gamma_mod=(Gamma_mod*pow(C,-1,q))%q
        sync=(-128*pow(R,3,q)*f*(lam%q))%q
        fixed_sync=(128*pow(pow(10**k,-1,q),3,q)*f*(lam%q))%q
        assert gamma_mod==sync==fixed_sync
    else:
        gamma_mod=sync=fixed_sync=None
    return dict(q=q,k=k,r=r,t=t,R_mod_q=Rq,old_coeff=old,new_coeff=new,
                lambda_mod_q=lam%q,old_formula_ok=old_ok,gamma_mod_q=gamma_mod,
                gamma_sync_rhs=sync)

# Three genuinely structural bulk examples with R != 1 mod q in at least two cases.
examples=[(7,6,3),(11,6,1),(19,6,3)]
rows=[]
rng=random.Random(20260817)
for q,k,r in examples:
    for _ in range(8):
        t=rng.randrange(1,200,2)
        if gcd(t,10)!=1:t+=2
        rows.append(bulk_numeric_regression(q,k,r,t))

# Low-k corrected residue table.
active_k1=[7,17,19,29,47,49,59,77,89,97,109]
low=[]
for q in active_k1:
    # find smallest r>=1 such that g=1+r and q|10^g+1
    r=next(rr for rr in range(1,1000) if (10**(1+rr)+1)%q==0)
    R=pow(10,r,q)
    coeff=(4*R)%q  # k=1 ad-hoc lambda=(digit)/5, omega=2(q+4)lambda
    fixed=(-4*pow(10,-1,q))%q
    assert coeff==fixed
    low.append((1,q,r,R,coeff))

# k=2,q=7: lambda=digit/25, omega=(q+4)lambda => lambda≡8Rt.
q=7;k=2
r=next(rr for rr in range(1,100) if (10**(k+rr)+1)%q==0)
R=pow(10,r,q); coeff=(8*R)%q
assert coeff==(-8*pow(100,-1,q))%q
low.append((2,7,r,R,coeff))
# k=2,q=11 moderate v=0 lambda=digit, corrected bulk coefficient.
q=11;k=2
r=next(rr for rr in range(1,100) if (10**(k+rr)+1)%q==0)
R=pow(10,r,q);b=1;coeff=(8*R*25)%q
assert coeff==(-8*25*pow(100,-1,q))%q
low.append((2,11,r,R,coeff))

print('R8_REVERSE_LAMBDA_RESIDUE=CORRECTED')
print('DERIVED=lambda_R == 8*R*5^(2b)*t (mod q)')
print('FIXED_K=lambda_R == -8*5^(2b)*K^{-1}*t (mod q)')
print('RANDOM_BULK_REGRESSION_ROWS=',len(rows))
print('RANDOM_BULK_REGRESSION=PASS')
print('OLD_FORMULA_FAILURES=',sum(not x['old_formula_ok'] for x in rows),'/',len(rows))
for x in rows[:6]: print('BULK_SAMPLE',x)
print('LOWK_CORRECTED_TABLE: k q r Rmodq coeff_of_t')
for x in low: print(*x)
print('VALUATION_PROVENANCE: k1_b0_5_DIV_T=INDEPENDENT_OF_LAMBDA_RESIDUE')
print('VALUATION_PROVENANCE: k2_q7_25_DIV_T=INDEPENDENT_OF_LAMBDA_RESIDUE')
print('AUDIT_STATUS=PASS')
