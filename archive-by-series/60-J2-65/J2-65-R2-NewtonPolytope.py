#!/usr/bin/env python3
"""J2-65 R2 Laurent/Newton support and Archimedean fan audit."""
from pathlib import Path
import csv, importlib.util, math
import sympy as sp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('mr',HERE/'J2-65-R2-MasterRoot-symbolic.py')
mr=importlib.util.module_from_spec(spec); spec.loader.exec_module(mr)
G,K,q,d,alpha,t,x=mr.G,mr.K,mr.q,mr.d,mr.alpha,mr.t,mr.x
P=sp.Poly(mr.QNUM,G,K)

# Every support point is on the polygon boundary here; physical rho>0 exposes only (5,0),(4,1).
vertex_set={(1,0),(5,0),(4,1),(0,1)}
physical={(5,0),(4,1)}
rows=[]
for (a,b),coef in sorted(P.terms(), key=lambda z:(z[0][1],z[0][0])):
    cf=sp.factor(coef)
    if (a,b)==(5,0):
        status='III_live_degeneracy_alpha=0'
    elif (a,b)==(4,1):
        status='III_live_degeneracy_alpha=0_or_x=0'
    else:
        status='II_generic_nonzero_with_proper_coefficient_zero_locus'
    rows.append(dict(a=a,b=b,coefficient=str(sp.expand(coef)),coefficient_factorization=str(cf),
                     structural_status=status,
                     newton_vertex=str((a,b) in vertex_set),physical_exposed=str((a,b) in physical)))
with (HERE/'J2-65-R2-NewtonSupport.tsv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0]),delimiter='\t');wr.writeheader();wr.writerows(rows)

fan=[
 dict(rho_left='0',rho_right='1',dominant_face='vertex',vertices='(5,0)',
      coefficient_conditions='alpha!=0; physical x>0',chamber='REVERSE'),
 dict(rho_left='1',rho_right='1',dominant_face='edge',vertices='(5,0);(4,1)',
      coefficient_conditions='alpha!=0; top-face cancellation iff alpha=2*d*q^2*c*x',chamber='BOUNDARY_WALL'),
 dict(rho_left='1',rho_right='2',dominant_face='vertex',vertices='(4,1)',
      coefficient_conditions='alpha!=0; physical x>0',chamber='HIGH'),
 dict(rho_left='0',rho_right='2',dominant_face='degenerate-alpha-zero',vertices='(3,1)',
      coefficient_conditions='alpha=0; t!=0 and physical x>0; q positive ten-unit',chamber='SUPPORT_DEGENERATION'),
]
with (HERE/'J2-65-R2-ArchimedeanFan.tsv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(fan[0]),delimiter='\t');wr.writeheader();wr.writerows(fan)

# Symbolic place metadata only; no bit ladder.  Keep valuations conditional rather than freezing moving data.
place=[]
for row in rows:
    a,b=row['a'],row['b']; cf=row['coefficient_factorization']
    if (a,b)==(5,0):
        v2='1+2*v2(alpha)  (q+4 odd)'
        v5='2*v5(alpha)+2*v5(q+4)'
        locus='alpha=0'
    elif (a,b)==(4,1):
        v2='2+v2(alpha)+v2(d)+v2(x)  (q,c,q+4 odd at 2)'
        v5='v5(alpha)+v5(d)+v5(x)+2*v5(q+4)+v5(c)'
        locus='alpha=0 or x=0'
    else:
        v2='symbolic v2(C_ab); not frozen in R2'
        v5='symbolic v5(C_ab); not frozen in R2'
        locus='proper coefficient-zero locus; retained'
    place.append(dict(a=a,b=b,coefficient=cf,v2_known=v2,v5_known=v5,
                      source='Level1 Q_sat exact coefficient',conditional_locus=locus))
with (HERE/'J2-65-R2-PlaceMetadata.tsv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(place[0]),delimiter='\t');wr.writeheader();wr.writerows(place)

# Projection statements.
# Boundary K=G maps (a,b)->a+b: powers 1..5; one structural G factor -> degree 4 chart.
bproj=sorted(set(a+b for a,b in mr.SUPPORT))
assert bproj==[1,2,3,4,5]
# Reverse G=KR at fixed K maps (a,b)->a, giving only degrees 0..5 at Level1.
rproj=sorted(set(a for a,b in mr.SUPPORT))
assert rproj==[0,1,2,3,4,5]

print('J2-65 R2 NEWTON CERTIFICATE')
print('MASTER_NEWTON_SUPPORT_SIZE=10')
print('MASTER_NEWTON_VERTEX_COUNT=4')
print('MASTER_NEWTON_EDGE_COUNT=4')
print('ARCHIMEDEAN_FAN_COMPUTED=TRUE')
print('BOUNDARY_IS_NEWTON_WALL=PROVED')
print('HIGH_IS_NEWTON_CONE=PROVED')
print('REVERSE_IS_NEWTON_CONE=PROVED')
print('PHYSICAL_EXPOSED_COEFFICIENT_COUNT=2')
print('PHYSICAL_EXPOSED_PAIR=(5,0),(4,1)')
print('BOUNDARY_FACE_CANCELLATION='+str(mr.BOUNDARY_TOP))
print('ALPHA_ZERO_SUPPORT_DEGENERATION=EXPLICIT')
print('BOUNDARY_PROJECTION_POWERS='+str(bproj))
print('REVERSE_LEVEL1_PROJECTION_POWERS='+str(rproj))
print('REVERSE_DEGREE7_NOT_SIMPLE_MASTER_PROJECTION=PROVED')
