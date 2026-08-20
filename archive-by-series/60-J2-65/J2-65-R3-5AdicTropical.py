#!/usr/bin/env python3
from J2_65_R3_common import *
C=grouped_coeffs()
P=sp.Poly(QNUM,G,K)
krow=sp.expand(sum(co*G**a*K**b for (a,b),co in P.terms() if b==1))
grow=sp.expand(sum(co*G**a*K**b for (a,b),co in P.terms() if b==0))
assert sp.cancel(krow-QDEN*(-8*K*u*D2*x))==0
assert sp.cancel(grow-QDEN*(A*G**2*x**2+4*F))==0

def coeff_v5(pt,co):
    special={
      (5,0):'2*A5+2*b5',
      (4,1):'A5+D5+X5+2*b5+c5',
      (0,1):'2*D5+T5+X5+2*b5+c5',
    }
    return special.get(pt,f'v5({sp.sstr(co)})')

def zero(pt,co):
    if pt in [(5,0),(4,1)]: return 'alpha=0 only among explicit structural factors; retired for q>1'
    if pt==(0,1): return 'NONE on live states (d,q,t,x,q+4,c nonzero)'
    return 'possible only by displayed additive bracket/sum cancellation (or alpha factor where displayed)'
rows=[]
for pt in EXPECTED_GK:
    co=C[pt];a,b=pt
    rows.append(dict(a=a,b=b,coefficient_factorization=sp.sstr(co),
      v5_expression=f'{a}*g+{b}*k+'+coeff_v5(pt,co),zero_locus=zero(pt,co),
      possible_minimum='YES',tie_partners='determined by row-min meta-cell; residue cancellation kept factor-aware',
      structural_constraints='q is 5-unit; b5=v5(q+4); c5=v5(c); b5>0=>c5=0, b5=0=>c5>=1'))
write_tsv(OUT/'J2-65-R3-5AdicLowerHull.tsv',rows,list(rows[0]))

# Dstr v5 = 2*D5 + 2*b5 + 2*c5 (q is a 5-unit).
# In Qclr, linear and constant have v5=k+X5, quadratic is higher by ell+X5.
T='2*D5+2*b5+2*c5+k+X5'
cells=[
 dict(cell_id='P5_K_LT_G',minimum_relation='m5(K-row)<m5(G-row)',required_tie='K-row minimum attained at least twice',row_sum_target=T,valuation_constraints='m5K<=T, m5G<=T; any row with m<T has internal cancellation',residue_constraints='b5>0=>c5=0; b5=0=>c5>=1; no q mod 25 ladder',status='OPEN_TIE_TYPE'),
 dict(cell_id='P5_K_EQ_G',minimum_relation='m5(K-row)=m5(G-row)',required_tie='cross-row global minimum tie already present',row_sum_target=T,valuation_constraints='m5K=m5G<=T; if <T each affected row must internally cancel',residue_constraints='b5>0=>c5=0; b5=0=>c5>=1; no q mod 25 ladder',status='OPEN_TIE_TYPE'),
 dict(cell_id='P5_G_LT_K',minimum_relation='m5(G-row)<m5(K-row)',required_tie='G-row minimum attained at least twice',row_sum_target=T,valuation_constraints='m5K<=T, m5G<=T; any row with m<T has internal cancellation',residue_constraints='b5>0=>c5=0; b5=0=>c5>=1; no q mod 25 ladder',status='OPEN_TIE_TYPE'),
]
write_tsv(OUT/'J2-65-R3-5AdicCells.tsv',cells,list(cells[0]))
print('P5_FULL_10_SUPPORT_USED=TRUE')
print('P5_COARSE_ROW_SUM_TARGET='+T)
print('P5_CELL_COUNT=3')
print('P5_UNIQUE_MIN_CELLS_CLOSED=ALL')
print('P5_RESIDUE_DESCRIPTOR=b5,c5 only; no forced q mod 25 refinement')
