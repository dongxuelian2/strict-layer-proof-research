#!/usr/bin/env python3
"""J2-55 R12 Hensel equality-edge dependency audit and root-splice scaffold."""
from math import gcd
from pathlib import Path
import csv

OUT=Path('/mnt/data')
def c(q): return q**3+10*q*q+12*q+8

# R11-HC is an exact recombination:
# c(q)=5^g h, c(q)==8 mod q, and 10^g==-1 mod q
# => 5^g h==8 mod q
# => 10^g h==2^(g+3) mod q
# => h+2^(g+3)==0 mod q.
def hc_check(g,q):
    cg=c(q)
    if cg%(5**g):return None
    h=cg//(5**g)
    if gcd(q,10)!=1 or pow(10,g,q)!=(q-1)%q:return None
    return (h+2**(g+3))%q==0

def hensel_qs(gmax):
    qv=2
    rows=[]
    for g in range(1,gmax+1):
        assert c(qv)%5**g==0
        cyc=(gcd(qv,10)==1 and pow(10,g,qv)==(qv-1)%qv)
        hc=hc_check(g,qv) if cyc else ''
        rows.append(dict(g=g,q_g=qv,ten_unit=(gcd(qv,10)==1),
                         cyclotomic_divisor=cyc,R11_HC=(hc if cyc else ''),
                         full_root_splice='REQUIRES_E_T_GAMMA_ROOTNF'))
        if g<gmax:
            base=5**g;mod=5**(g+1)
            ds=[d for d in range(5) if c(qv+d*base)%mod==0]
            assert len(ds)==1
            qv+=ds[0]*base
    return rows

rows=hensel_qs(1000)
hits=[r for r in rows if r['cyclotomic_divisor']]
p=OUT/'J2-55-R12-HenselRootSplice-diagnostic.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
    fields=list(rows[0])
    wr=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(rows)

print('J2-55 R12 Hensel root-splice certificate')
print('R11_HC_DEPENDENCY=DERIVED_ONLY_FROM_[5^g|c(q), q|10^g+1]')
print('R11_HC_INDEPENDENT_OBSTRUCTION=FALSE')
print('R11_HC_STATUS=RETIRED_AS_INDEPENDENT; retained only as cheap consequence filter')
print('HENSEL_UNIQUE_Q_G=PASS')
print('DIAGNOSTIC_GMAX=1000')
print('DIAGNOSTIC_CYCLOTOMIC_HITS=',len(hits))
print('FULL_ROOT_SPLICE_OBJECT=E_ind(q_g,u,e,t,gamma,...)')
print('FULL_ROOT_SPLICE_GLOBAL_CLOSURE=False')
print('DIAGNOSTIC='+p.name)
