#!/usr/bin/env python3
"""R10 Hensel equality-edge / deep-core audit.
No finite-g scan is promoted to a theorem.
"""
from math import gcd
from pathlib import Path
import csv
OUT=Path('/mnt/data')

def c(q): return q**3+10*q*q+12*q+8
def cp(q): return 3*q*q+20*q+12

def lift(root,w):
 """root mod 5^w -> unique root mod 5^(w+1), w>=1."""
 M=5**w
 assert c(root)%M==0 and cp(root)%5!=0
 a=(c(root)//M)%5
 inv=pow(cp(root)%5,-1,5)
 digit=(-a*inv)%5
 nr=root+digit*M
 assert c(nr)%(5*M)==0
 return nr,digit

def roots(n):
 r=2; out=[(1,r,None)]
 for w in range(1,n):
  r,d=lift(r,w);out.append((w+1,r,d))
 return out

# Equality edge g=w. R7 gives q^2<4G+3q+8 (high) and
# q^2<4G+9q (boundary).  If q>=5^g, then q<=G+1 and for g>=3:
# q^2-9q >=25^g-9(G+1) >=4G, contradicting the boundary bound.
# (High is stronger.) Hence q<5^g, so the Hensel class forces q=q_g exactly.
for g in range(3,100):
 G0=10**g
 assert 25**g >= 13*G0+9

rows=[];hits=[]
for g,r,d in roots(300):
 edge_div=(pow(10,g,r)==(r-1)%r) if r>1 else False
 tenunit=gcd(r,10)==1
 # If edge_div, u=(10^g+1)/r; test inherited A=2u+1 ten-unit.
 Aten=''
 if edge_div:
  u=(10**g+1)//r;Aten=(gcd(2*u+1,10)==1)
  if tenunit and Aten:hits.append((g,r))
 rows.append(dict(g=g,hensel_root=r,lift_digit='' if d is None else d,tenunit=tenunit,
                  divides_10g_plus_1=edge_div,A_tenunit=Aten,
                  theorem_scope=('FINITE_EDGE' if g<3 else 'UNIQUE_Q_CANDIDATE_BY_Q_SQUARE_BOUND')))

p=OUT/'J2-55-R10-HenselEdge-diagnostic.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
 w=csv.DictWriter(fobj,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

print('HENSEL_DERIVATIVE_UNIT_AT_Q_EQ_2_MOD5=PASS')
print('HENSEL_RECURRENCE=q_{w+1}=q_w+d_w*5^w with unique d_w in {0,1,2,3,4}')
print('EQUALITY_EDGE_G_GE_3_ONE_Q_CANDIDATE=q_g=PASS')
print('EQUALITY_EDGE_DIAGNOSTIC_G_LE_300_VALID_HITS=',hits)
print('DIAGNOSTIC_NOT_GLOBAL_THEOREM=PASS')
print('EQUALITY_EDGE_STATUS=OPEN_AT_ONE_HENSEL_CANDIDATE_PER_EXPONENT')
print('DEEP_CORE_SIZE_THEOREM=5^g < 5^(2b+v) <= (q+4)^2 * t; hence high <(q+4)^2(3q+8), boundary <9q(q+4)^2')
print('DEEP_CORE_FIXED_OFFSET_NOT_PROVED=PASS')
print('DIAGNOSTIC_FILE='+p.name)
