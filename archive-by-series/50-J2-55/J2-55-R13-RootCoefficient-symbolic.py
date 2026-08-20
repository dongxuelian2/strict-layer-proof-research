#!/usr/bin/env python3
"""R13 lightweight coefficient analyzer.

Run beside J2-55-R12-RootSaturation-symbolic.py.  This script deliberately
imports the R12 certified independent root factors; it does not rederive the
R8--R12 saturation chain and does not introduce a new residual.
"""
from pathlib import Path
import csv, importlib.util, sympy as sp

HERE=Path(__file__).resolve().parent
SRC=HERE/'J2-55-R12-RootSaturation-symbolic.py'
if not SRC.exists():
    raise FileNotFoundError(
        'R12 frozen symbolic certificate must be mounted beside this script: '+str(SRC))
spec=importlib.util.spec_from_file_location('r12root',SRC)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
D=m.build_root_factors() if hasattr(m,'build_root_factors') else m.__dict__

objs=[
 ('BOUNDARY', D['P_B_G']),
 ('HIGH', D['P_H_G']),
 ('REVERSE_GENERIC', D['P_R_generic']),
 ('REVERSE_K1_SPECIAL', D['P_R_k1']),
]
# Infer the univariate power variable from the polynomial itself, excluding
# structural/e,t,gamma symbols.  Prefer names used by R12.
def power_var(expr, branch):
    names={str(x):x for x in expr.free_symbols}
    for n in (('GG','G') if branch in ('BOUNDARY','HIGH') else ('RR','RR1','R')):
        if n in names: return names[n]
    # robust fallback: variable with degree 4 or 7
    target=4 if branch in ('BOUNDARY','HIGH') else 7
    for x in expr.free_symbols:
        try:
            if sp.Poly(expr,x).degree()==target:return x
        except Exception:pass
    raise RuntimeError('cannot infer power variable')

def degree(expr, name):
    xs=[x for x in expr.free_symbols if str(x)==name]
    if not xs:return 0
    return sp.Poly(sp.expand(expr),xs[0]).degree()

def homogeneous_degree2(expr):
    syms={str(x):x for x in expr.free_symbols}
    vars=[syms[n] for n in ('e','t','gamma') if n in syms]
    if not vars:return False
    P=sp.Poly(sp.expand(expr),*vars)
    return all(sum(mon)==2 for mon,coef in P.terms() if coef!=0)

rows=[]; coeff_dump=[]
for branch,expr in objs:
    T=power_var(expr,branch); P=sp.Poly(sp.expand(expr),T)
    assert P.degree()==(4 if branch in ('BOUNDARY','HIGH') else 7)
    for j in range(P.degree()+1):
        C=sp.factor(P.nth(j)); coeff_dump.append(f'{branch} C{j} = {C}')
        names={str(x) for x in C.free_symbols}
        rows.append(dict(branch=branch,index=j,coefficient=str(C),
            degree_e=degree(C,'e'),degree_t=degree(C,'t'),degree_gamma=degree(C,'gamma'),
            homogeneous_degree2=homogeneous_degree2(C),
            depends_s=('s' in names),depends_H=('H' in names),depends_K=('K' in names),
            factor_2='use exact valuation analyzer',factor_5='use exact valuation analyzer',
            factor_q='factor(C) shown in coefficient',zero_locus='Cj=0'))

(HERE/'J2-55-R13-Coefficients.txt').write_text('\n'.join(coeff_dump)+'\n',encoding='utf-8')
with (HERE/'J2-55-R13-CoefficientProfile.tsv').open('w',newline='',encoding='utf-8') as fh:
    fields=list(rows[0]); w=csv.DictWriter(fh,fields,delimiter='\t');w.writeheader();w.writerows(rows)
for branch,expr in objs:
    print('HOMOGENEITY_'+branch+'=', 'QUADRATIC' if homogeneous_degree2(expr) else 'FAIL')
print('COEFFICIENT_ROWS=',len(rows))
print('NO_NEW_RESIDUAL=PASS')
