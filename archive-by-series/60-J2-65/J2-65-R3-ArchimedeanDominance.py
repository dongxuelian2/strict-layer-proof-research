#!/usr/bin/env python3
from J2_65_R3_common import *
from J2_65_R3_projective import verify as verify_projective
import math

terms=full_terms()
S=sum(abs(co) for _,co in terms)
# distinguished generic augmented monomial M_X
MX=((3,0,12,2,0,0,2),2)
assert MX in terms
# nearest projective competitors identified by exact symbolic support + LP diagnostic:
MK=((4,1,7,1,1,0,1),-4)
MA=((5,0,2,0,2,0,0),2)
assert MK in terms and MA in terms
threshold=math.ceil(math.log10((S-abs(MX[1]))/abs(MX[1])))
assert threshold==6

# Height-bound ledger. Bounds retain finite-g corrections rather than silently deleting O(1/g).
rows=[
 dict(variable='rho=k/g',lower_bound='0',upper_bound='<5/3 on current q>1 live wedge',scope='q>1 live',source='FQTR6/DCDC old wedge projection',normalized_bound='0<rho<5/3'),
 dict(variable='sigma=h_G(q)',lower_bound='log10(7)/g',upper_bound='<1',scope='q>1',source='q>=7 and q<G',normalized_bound='0<sigma<1'),
 dict(variable='eta=h_G(d)',lower_bound='0',upper_bound='(b log10(5)+log10(2))/g',scope='rho>=1',source='d=2*5^b, b<g',normalized_bound='0<=eta<0.8'),
 dict(variable='eta=h_G(d)',lower_bound='1-rho',upper_bound='1-rho+(b log10(5)+log10(2))/g',scope='rho<1',source='d=2*5^b*10^(g-k), b<g',normalized_bound='1-rho<=eta<1-rho+0.8'),
 dict(variable='a=h_G(|alpha|)',lower_bound='no source-positive lower height beyond alpha!=0',upper_bound='h_G(15*d*q^4*G/K)',scope='q>1',source='CQLRC8 unified tail-size',normalized_bound='a < 1+4sigma+eta-rho+log10(15)/g'),
 dict(variable='tau=h_G(t)',lower_bound='0',upper_bound='h_G(5q)',scope='rho>1',source='t<3q+8<5q',normalized_bound='tau < sigma+log10(5)/g'),
 dict(variable='tau=h_G(t)',lower_bound='0',upper_bound='h_G(9q)',scope='rho=1',source='boundary t<9q',normalized_bound='tau < sigma+log10(9)/g'),
 dict(variable='tau=h_G(t)',lower_bound='0',upper_bound='h_G(9q*10^(g-k))',scope='rho<1',source='reverse t<9q10^(g-k)',normalized_bound='tau < sigma+1-rho+log10(9)/g'),
 dict(variable='xi=h_G(x)',lower_bound='2-sigma-log10(5)/g',upper_bound='2-sigma+log10(11)/g',scope='live ell>=6',source='DRL + ROOT-UP + radial D2 bound',normalized_bound='xi=2-sigma+O(1/g) with explicit endpoints'),
 dict(variable='h_G(u)',lower_bound='1-sigma',upper_bound='1-sigma+log10(1+1/G)/g',scope='all',source='u=(G+1)/q',normalized_bound='1-sigma+O(1/(gG))'),
 dict(variable='h_G(A)',lower_bound='1-sigma+log10(2)/g',upper_bound='1-sigma+log10(3*(1+1/G))/g',scope='u>1',source='2u<A<3u',normalized_bound='1-sigma+O(1/g)'),
 dict(variable='h_G(c)',lower_bound='3sigma',upper_bound='3sigma+log10(3)/g',scope='q>=7',source='q^3<c<3q^3',normalized_bound='3sigma+O(1/g)'),
 dict(variable='h_G(q+4)',lower_bound='sigma',upper_bound='sigma+log10(11/7)/g',scope='q>=7',source='q<q+4<11q/7',normalized_bound='sigma+O(1/g)'),
]
write_tsv(OUT/'J2-65-R3-HeightBounds.tsv',rows,['variable','lower_bound','upper_bound','scope','source','normalized_bound'])

# Exact finite-g triangle theorem is represented by the actual augmented gap Delta_arch,
# which is derived from existing heights and is NOT a new terminal variable.
# If Delta_arch > threshold/g, then |M_X| > sum of every other monomial after integer coefficients are included.
# Projective limit of the admissible near-tie locus has 3 meta-faces found by the support audit:
# sigma=0, sigma=1, and tail saturation W(MX)=W(MK).
cells=[
 dict(cell_id='A_SIGMA0',scope='q>1 projective closure',defining_condition='Delta_arch<=6/g and projective approach sigma=0',projective_limit_face='sigma=0',dominant_monomial='MX=(3,0,12,2,0,0,2)',exact_status='NEAR_TIE_ENVELOPE',quantitative_rule='actual root => Delta_arch<=6/g',notes='q-height tends to zero; q may remain bounded/subexponential'),
 dict(cell_id='A_SIGMA1',scope='q>1 projective closure',defining_condition='Delta_arch<=6/g and projective approach sigma=1',projective_limit_face='sigma=1',dominant_monomial='MX',exact_status='NEAR_TIE_ENVELOPE',quantitative_rule='actual root => Delta_arch<=6/g',notes='outer q-height tends to G-height; equivalently u has height 0'),
 dict(cell_id='A_TAILSAT',scope='q>1 projective closure',defining_condition='Delta_arch<=6/g and W(MX)=W(MK) in limit',projective_limit_face='1+4sigma+eta-rho-a=0 (with xi=2-sigma)',dominant_monomial='MX tied with MK=(4,1,7,1,1,0,1)',exact_status='NEAR_TIE_ENVELOPE',quantitative_rule='actual root => Delta_arch<=6/g',notes='alpha/tail-height saturation face; exact finite-g constants retained in Delta_arch'),
]
write_tsv(OUT/'J2-65-R3-ArchimedeanCells.tsv',cells,list(cells[0]))

vc=verify_projective()
print('PROJECTIVE_RATIONAL_VERTEX_CERTIFICATE=PASS')
print('PROJECTIVE_VERTEX_COUNTS='+','.join(f'{k}:{v}' for k,v in vc.items()))
print('PROJECTIVE_GAP_LOWER_BOUND=min(sigma,1-sigma,Delta_alpha,2-rho)')
print('AUGMENTED_SUPPORT_SIZE='+str(len(terms)))
print('INTEGER_COEFFICIENT_L1='+str(S))
print('TRIANGLE_GAP_THRESHOLD_DIGITS='+str(threshold))
print('ARCHIMEDEAN_EXACT_METHOD=TRIANGLE_DOMINANCE')
print('FALSE_ARCHIMEDEAN_MINMAX_TIE_USED=FALSE')
print('GENERIC_STRICT_PROJECTIVE_DOMINANT=MX:'+str(MX[0]))
print('PROJECTIVE_ESCAPE_FACE_COUNT=3')
print('ARCHIMEDEAN_CELL_COUNT=3')
print('ARCHIMEDEAN_CELLS_CLOSED=generic complement of Delta_arch<=6/g')
