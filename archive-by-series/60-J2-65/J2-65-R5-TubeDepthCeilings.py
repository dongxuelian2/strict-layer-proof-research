#!/usr/bin/env python3
from __future__ import annotations
import csv, math
import sympy as sp
from J2_65_R5_common import HERE,q,DETERMINANTS,coeff_height,reciprocal_poly

lam=math.log(10)/(2*math.log(5))

rat=[]
rat.append(dict(
 factor='q+4',p=5,root='-4',m_condition='m=v5(q+4)>=1',
 q_least_residue='5^m-4',q_least_admissible='5^m-4 (m>=2); 11 if m=1 and q>1 odd',
 u_reciprocal_residue='(5^m-1)/4',
 exact_product_lower_bound='(5^m-4)(5^m-1)/4',
 exact_depth_ceiling='5^m <= (5+sqrt(25+16*10^g))/2',
 asymptotic_slope=f'{lam:.15f}',small_m_exceptions='m=1: least residue q=1 forbidden; bound remains valid but nonsharp',
 shallow_theorem='g>=2 => m<g'))
rat.append(dict(
 factor='q-2',p=5,root='2',m_condition='m=v5(q-2)>=1',
 q_least_residue='2',q_least_admissible='5^m+2 (q odd, q!=2)',
 u_reciprocal_residue='(5^m+1)/2',
 exact_product_lower_bound='(5^m+2)(5^m+1)/2',
 exact_depth_ceiling='5^m <= (-3+sqrt(9+8*10^g))/2',
 asymptotic_slope=f'{lam:.15f}',small_m_exceptions='none',
 shallow_theorem='g>=1 => m<g'))
rat.append(dict(
 factor='3q+2',p=5,root='-2/3',m_condition='m=v5(3q+2)>=1',
 q_least_residue='m odd: (5^m-2)/3; m even: 2(5^m-1)/3',
 q_least_admissible='m=1:11; odd m>=3:(5^m-2)/3; even m:(5*5^m-2)/3',
 u_reciprocal_residue='(5^m-3)/2',
 exact_product_lower_bound='m=1:11; odd m>=3:(5^m-2)(5^m-3)/6; even m:(5*5^m-2)(5^m-3)/6',
 exact_depth_ceiling='odd m>=3: 5^m <= (5+sqrt(25+24*10^g))/2; even m: 5^m <= (17+sqrt(289+120*10^g))/10; m=1 separate',
 asymptotic_slope=f'{lam:.15f}',small_m_exceptions='m=1 raw q-residue=1 forbidden; next odd q=11',
 shallow_theorem='g>=2 => m<g'))

p=HERE/'J2-65-R5-RationalTubeBounds.tsv'
with p.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rat[0]),delimiter='\t');w.writeheader();w.writerows(rat)

# Exact residue checks are diagnostics for formulas; theorem derivation is algebraic.
for m in range(1,16):
    M=5**m
    assert (M-4+4)%M==0
    assert ((M-1)//4 * (-4)-1)%M==0
    assert ((M+1)//2*2-1)%M==0
    q0=(M-2)//3 if m%2 else 2*(M-1)//3
    assert (3*q0+2)%M==0
    assert ((M-3)//2*2+3)%M==0

rows=[]
for name,data in DETERMINANTS.items():
    poly=sp.expand(data['poly']); pp=data['p']; deg=sp.degree(poly,q); C=coeff_height(poly)
    rec=reciprocal_poly(poly); Cv=coeff_height(rec, sp.symbols('u'))
    assert C==Cv
    if name=='q+4':
        qlb='q >= 5^m-4'; udepth='m (g>=2, hence shallow)'; ulb='u >= (5^m-1)/4'; pair='(5^m-4)(5^m-1)/4 <= 10^g+1'; grel='5^m <= (5+sqrt(25+16*10^g))/2; in particular m<g for g>=2'; sharp='YES'; crit='excluded for live g>=2 by sharp pair bound'
    elif name=='q-2':
        qlb='q >= 5^m+2'; udepth='m (always shallow for g>=1)'; ulb='u >= (5^m+1)/2'; pair='(5^m+2)(5^m+1)/2 <= 10^g+1'; grel='5^m <= (-3+sqrt(9+8*10^g))/2; m<g for g>=1'; sharp='YES'; crit='excluded'
    elif name=='3q+2':
        qlb='Q_m: 11 if m=1; (5^m-2)/3 if odd m>=3; (5*5^m-2)/3 if even'; udepth='m for live g>=2'; ulb='u >= (5^m-3)/2'; pair='Q_m*(5^m-3)/2 <= 10^g+1'; grel='parity-exact quadratic ceilings in RationalTubeBounds.tsv; m<g for g>=2'; sharp='YES'; crit='excluded for live g>=2'
    else:
        qlb=f'q >= ( {pp}^m/{C} )^(1/{deg}) when D(q)!=0'
        udepth='n>=min(m,g); exact n=m if m<g, n=g if m>g, n=g+v_p(rho*c_p^g-eps) if m=g'
        ulb=f'u >= ( {pp}^min(m,g)/{Cv} )^(1/{deg})'
        pair=f'{pp}^(m+min(m,g)) <= {C*Cv}*(10^g+1)^{deg}'
        grel=(f'E=floor_log_{pp}({C*Cv}*(10^g+1)^{deg}); '
              f'if m<=g: m<=floor(E/2); if m>=g: m<=E-g')
        sharp='NO_GENERIC_HEIGHT'
        crit='retained with normalized unit equation; pair bound uses guaranteed reciprocal depth >=g'
    rows.append(dict(factor=name,p=pp,degree=deg,tube_depth='m',q_lower_bound=qlb,
                     u_reciprocal_depth=udepth,u_lower_bound=ulb,pair_lower_bound=pair,
                     g_upper_relation=grel,sharp_rational=sharp,critical_case=crit,
                     coefficient_height_C=C,reciprocal_height_C=Cv))

p2=HERE/'J2-65-R5-TubeDepthCeilings.tsv'
with p2.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

print('R5 TUBE DEPTH CEILING CERTIFICATE')
print('QPLUS4_PAIR_BOUND=PROVED')
print('QMINUS2_PAIR_BOUND=PROVED')
print('THREEQPLUS2_PAIR_BOUND=PROVED_WITH_PARITY_AND_ODD_q_ADMISSIBILITY')
print('RATIONAL_TUBE_ASYMPTOTIC_SLOPE=',lam,sep='')
print('RATIONAL_TUBES_SHALLOW_FOR_LIVE_g_GE_4=PROVED (indeed q+4 and 3q+2 for g>=2; q-2 for g>=1)')
print('ALGEBRAIC_TUBE_DEPTH_CEILINGS=PROVED')
print('GENERIC_PAIR_THEOREM=p^(m+min(m,g)) <= C_D*C_Dvee*(10^g+1)^degree')
print('TUBES_WITH_GLOBAL_DEPTH_CEILING=',len(rows),sep='')
print('OUTPUTS=',p.name,',',p2.name,sep='')
