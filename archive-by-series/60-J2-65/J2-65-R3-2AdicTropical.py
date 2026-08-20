#!/usr/bin/env python3
from J2_65_R3_common import *
C=grouped_coeffs()
P=sp.Poly(QNUM,G,K)
krow=sp.expand(sum(co*G**a*K**b for (a,b),co in P.terms() if b==1))
grow=sp.expand(sum(co*G**a*K**b for (a,b),co in P.terms() if b==0))
assert sp.cancel(krow-QDEN*(-8*K*u*D2*x))==0
assert sp.cancel(grow-QDEN*(A*G**2*x**2+4*F))==0

def coeff_v2(pt,co):
    a,b=pt
    s=sp.sstr(co)
    special={
      (5,0):'1+2*A2',
      (4,1):'2+A2+D2v+X2',
      (0,1):'3+2*D2v+X2',
    }
    return special.get(pt,f'v2({s})')

def zero(pt,co):
    if pt in [(5,0),(4,1)]: return 'alpha=0 only among explicit structural factors; retired for q>1'
    if pt==(0,1): return 'NONE on live states (d,q,t,x,q+4,c nonzero)'
    return 'possible only by displayed additive bracket/sum cancellation (or alpha factor where displayed)'
rows=[]
for pt in EXPECTED_GK:
    co=C[pt];a,b=pt
    rows.append(dict(a=a,b=b,coefficient_factorization=sp.sstr(co),
      v2_expression=f'{a}*g+{b}*k+'+coeff_v2(pt,co),zero_locus=zero(pt,co),
      possible_minimum='YES',tie_partners='determined by row-min meta-cell; no bit ladder',
      structural_constraints='q,q+4,c,t are 2-units; v2(d)=1 for rho>=1, =1+g-k for rho<1'))
write_tsv(OUT/'J2-65-R3-2AdicLowerHull.tsv',rows,list(rows[0]))

# Exact full-root row-sum target after the common Qsat clearing factor Dstr.
# Qclr: quadratic A G^2 x^2 has v2=2g+2X2;
# linear -8K uD2 x and constant 4F=8K x lambda0 both have k+3+X2,
# because u,D2,lambda0 are 2-units. ell>=6 => quadratic is strictly higher.
# Dstr contributes 2*v2(d).
T='2*D2v+k+3+X2'
cells=[
 dict(cell_id='P2_K_LT_G',minimum_relation='m2(K-row)<m2(G-row)',required_tie='K-row minimum attained at least twice',row_sum_target=T,valuation_constraints='m2K<=T, m2G<=T; any row with m<T has internal cancellation',structural_constraints='ell>=6; u,D2,lambda0 are 2-units',status='OPEN_TIE_TYPE'),
 dict(cell_id='P2_K_EQ_G',minimum_relation='m2(K-row)=m2(G-row)',required_tie='cross-row global minimum tie already present',row_sum_target=T,valuation_constraints='m2K=m2G<=T; if <T each affected row must internally cancel',structural_constraints='ell>=6; u,D2,lambda0 are 2-units',status='OPEN_TIE_TYPE'),
 dict(cell_id='P2_G_LT_K',minimum_relation='m2(G-row)<m2(K-row)',required_tie='G-row minimum attained at least twice',row_sum_target=T,valuation_constraints='m2K<=T, m2G<=T; any row with m<T has internal cancellation',structural_constraints='ell>=6; u,D2,lambda0 are 2-units',status='OPEN_TIE_TYPE'),
]
write_tsv(OUT/'J2-65-R3-2AdicCells.tsv',cells,list(cells[0]))
print('P2_FULL_10_SUPPORT_USED=TRUE')
print('P2_COARSE_ROW_SUM_TARGET='+T)
print('P2_CELL_COUNT=3')
print('P2_UNIQUE_MIN_CELLS_CLOSED=ALL')
print('P2_BIT_LADDER_USED=FALSE')
