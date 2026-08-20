#!/usr/bin/env python3
"""R11 Hensel-root × cyclotomic-divisor collision audit."""
from pathlib import Path
import csv
OUT=Path('/mnt/data')

def c(q): return q**3+10*q*q+12*q+8
def cp(q): return 3*q*q+20*q+12

def lift(q,g):
    """q is root mod 5^g; return unique digit d and root mod 5^(g+1)."""
    M=5**g
    h=(c(q)//M)%5
    der=cp(q)%5
    d=(-h*pow(der,-1,5))%5
    qq=q+d*M
    assert c(qq)%(5*M)==0
    return d,qq

# Exact coupled recurrence for cyclotomic remainder:
# write 10^g+1=q_g*m_g+r_g. Then
# 10^(g+1)+1=q_{g+1}*(10m_g)
#                + [10r_g-9-10*d_g*5^g*m_g].
# The bracket must still be reduced modulo q_{g+1}.
# Hence (d_g,r_g) alone is NOT a closed finite state; m_g is required.

q=2
rows=[]
hits=[]
GMAX=600
for g in range(1,GMAX+1):
    if g>1:
        # q already lifted at end of previous iteration
        pass
    tenunit=(q%2==1 and q%5!=0)
    N=10**g+1
    rem=N%q if q else 0
    quot=N//q if q else 0
    if tenunit and rem==0:
        hits.append((g,q))
    h=c(q)//(5**g)
    # Exact collision consequence if rem=0:
    # h + 2^(g+3) == 0 mod q.
    collision=(h+2**(g+3))%q if q else 0
    d=''
    if g<GMAX:
        d,qn=lift(q,g)
    rows.append(dict(g=g,q_g=q,digit_to_next=d,ten_unit=tenunit,
                     cyclotomic_remainder=rem,
                     collision_h_plus_2g3_mod_q=collision,
                     status='HIT' if tenunit and rem==0 else 'NO_HIT_DIAGNOSTIC'))
    if g<GMAX:q=qn

p=OUT/'J2-55-R11-HenselCyclotomic-diagnostic.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
    fields=list(rows[0])
    wri=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t')
    wri.writeheader();wri.writerows(rows)

print('HENSEL_DIGIT_RECURRENCE=d_g=-[c(q_g)/5^g]*cprime(q_g)^(-1) mod 5')
print('CYCLOTOMIC_REMAINDER_RECURRENCE='
      'r_{g+1} == 10*r_g-9-10*d_g*5^g*m_g (mod q_{g+1})')
print('FINITE_STATE_ON_(d_g,r_g)_ALONE=CLOSED_FALSE; quotient m_g is necessary')
print('EXACT_ACCEPTING_STATE_CONSEQUENCE='
      'if q_g|(10^g+1), then c(q_g)/5^g + 2^(g+3) == 0 (mod q_g)')
print('DIAGNOSTIC_GMAX=',GMAX)
print('DIAGNOSTIC_HITS=',hits)
print('GLOBAL_EQUALITY_EDGE_CLOSURE=False')
print('DIAG=',p.name)
