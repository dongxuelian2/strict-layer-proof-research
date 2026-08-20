#!/usr/bin/env python3
"""R14 q=1 negative Gaussian branch: four-t theorem and finite cell audit."""
from math import gcd,isqrt
from pathlib import Path
import csv

HERE=Path(__file__).resolve().parent
Ks=(10,100,1000)
T4=(1,3,7,9)
pairs=((1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1))
assert sorted({d*tau for d,tau in pairs})==list(T4)
assert all(gcd(d,10)==gcd(tau,10)==1 for d,tau in pairs)

# DCDC cells in original variables 31*a3+t == 0 mod 2K.
rows=[]
for K in Ks:
    inv31=pow(31,-1,2*K)
    for tt in T4:
        a3=(-inv31*tt)%(2*K)
        assert (31*a3+tt)%(2*K)==0 and gcd(a3,10)==1
        fac=[f'({d},{tau})' for d,tau in pairs if d*tau==tt]
        rows.append(dict(K=K,t=tt,a3_mod_2K=a3,ten_unit_pass='PASS',
                         possible_d_tau_factorizations=','.join(fac),status='NEGATIVE_FIXED_CELL_OPEN'))
assert len(rows)==12
with (HERE/'J2-55-R14-q1-NegativeCells.tsv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0]),delimiter='\t');wr.writeheader();wr.writerows(rows)

# Exact theorem: M<0 and a3=d*a<G imply d*tau<10+4/G-2/G^2<11.
# Since d*tau=t is a positive ten-unit integer, t is one of 1,3,7,9.
def negative_four_t_check(G,d,tau,a):
    den=10*G*G+4*G-2
    assert d*a<G
    M=G**3*tau-den*a
    if M>=0:return True
    # Cross-multiplied exact inequality d*tau*G^2 < 10G^2+4G-2.
    assert d*tau*G*G < den
    assert den < 11*G*G
    return d*tau in T4
for G in (10**4,10**5):
    for d,tau in pairs:
        # sample a inside negative interval if present
        den=10*G*G+4*G-2
        lo=G**3*tau//den+1; hi=(G-1)//d
        if lo<=hi: assert negative_four_t_check(G,d,tau,lo)

# Active search for a negative actual pseudo-survivor through g<=7.
# This is diagnostic only, never promoted to an infinite-G proof.
def sq(n):
    if n<0:return False
    z=isqrt(n); return z*z==n
search=[]
for K in Ks:
    inv31=pow(31,-1,2*K)
    k=len(str(K))-1
    for d,tau in pairs:
        ar=(-inv31*tau)%(2*K)  # primitive relation 31a+tau ==0 mod2K
        total=primitive=Lneg=Dnonneg=squares=0; first=''
        for g in range(max(4,k+2),8):
            G=10**g; den=10*G*G+4*G-2
            lo=G**3*tau//den+1; hi=(G-1)//d
            a=lo+((ar-lo)%(2*K))
            while a<=hi:
                total+=1
                n=(31*a+tau)//(2*K)
                assert 2*K*n==31*a+tau
                if gcd(a,n)==1:
                    primitive+=1
                    M=G**3*tau-den*a
                    S=(G+1)*(2*G+3)
                    Q=4*G**3*K**2-4*G**3+8*G**2*K**2-12*G**2+4*G*K**2-13*G-6
                    num=Q*M+4*S*a
                    assert num%G==0
                    L=num//G
                    if L<0:
                        Lneg+=1
                        DD=M*L-(2*S*a)**2
                        if DD>=0:
                            Dnonneg+=1
                            if sq(DD):
                                squares+=1
                                if not first:first=f'g={g};a={a};n={n};M={M};L={L};Y={isqrt(DD)}'
                a+=2*K
        search.append(dict(K=K,d=d,tau=tau,t=d*tau,g_scope=f'{max(4,k+2)}..7',
                           raw=total,primitive=primitive,L_negative=Lneg,gaussian_D_nonnegative=Dnonneg,
                           gaussian_square=squares,first_square=first,status='NO_DIAGNOSTIC_SQUARE' if not squares else 'PSEUDO_SURVIVOR_FOUND'))
with (HERE/'J2-55-R14-q1-NegativeDiagnostic.tsv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(search[0]),delimiter='\t');wr.writeheader();wr.writerows(search)

print('PRIMITIVE_SCALE_PROVENANCE=a3=d*a,m=d*n,t=d*tau; gcd(a,n)=1; d,tau ten-units')
print('NEGATIVE_DT_BOUND=d*tau < 10+4/G-2/G^2 < 11')
print('NEGATIVE_FOUR_T_THEOREM=PASS:t in {1,3,7,9}')
print('NEGATIVE_EIGHT_PAIRS=PASS:'+str(pairs))
print('NEGATIVE_DCDC_CELLS=12')
for r in rows: print('CELL',r)
print('NEGATIVE_FIXED_CASES=24 (3 K values x 8 (d,tau) pairs)')
print('NEGATIVE_GAUSSIAN_DIAGNOSTIC_G_LE_7_SQUARES='+str(sum(x['gaussian_square'] for x in search)))
print('NEGATIVE_BRANCH_GLOBAL_CLOSURE=OPEN')
