from __future__ import annotations
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
q = sp.symbols('q', integer=True)

DETERMINANTS = {
    'q+4': dict(p=5, poly=q+4, root='rho_qp4=-4', root_mod=1, r4='v5(q+4)=b5'),
    'D7': dict(p=2, poly=q**3+5*q**2-4*q-4, root='rho_D7_2', root_mod=1, r4='v2(D7(q))=v2(q-rho_D7_2)'),
    'D8': dict(p=2, poly=q**2+q+2, root='rho_D8_2', root_mod=1, r4='v2(D8(q))=v2(q-rho_D8_2)'),
    '3q+2': dict(p=5, poly=3*q+2, root='rho_3q2=-2/3', root_mod=1, r4='v5(3q+2)=v5(q-rho_3q2)'),
    'D4': dict(p=5, poly=q**6+16*q**5+132*q**4+480*q**3+432*q**2-64, root='rho_D4_5', root_mod=4, r4='v5(D4(q))=v5(q-rho_D4_5)'),
    'q-2': dict(p=5, poly=q-2, root='rho_qm2=2', root_mod=2, r4='v5(q-2)=v5(q-2)'),
    'D9': dict(p=5, poly=q**3+10*q**2+36*q+8, root='rho_D9_5', root_mod=1, r4='v5(D9(q))=v5(q-rho_D9_5)'),
}

BRACKETS = {
    'B10': {'row':'G','kind':'linear'},
    'H20': {'row':'G','kind':'conic'},
    'H30': {'row':'G','kind':'conic'},
    'B40': {'row':'G','kind':'linear'},
    'B11': {'row':'K','kind':'linear'},
    'B21': {'row':'K','kind':'linear'},
    'B31': {'row':'K','kind':'linear'},
}
ROW_TERMS = {
    'K': [('C01',0,None,'monomial'),('C11',1,'B11','linear'),('C21',2,'B21','linear'),('C31',3,'B31','linear'),('C41',4,None,'monomial')],
    'G': [('C10',1,'B10','linear'),('C20',2,'H20','conic'),('C30',3,'H30','conic'),('C40',4,'B40','linear'),('C50',5,None,'monomial')],
}
ROW_ADDITIVES = {
    'K':['B11','B21','B31'],
    'G':['B10','H20','H30','B40'],
}

# Full line-line determinant factorizations from R4. Only row-internal pairs are used in the DNF audit.
PAIR_DET = {
    tuple(sorted(('B10','B40'))): {'poly':'-(q+4)*D1', 'p2':'0', 'p5':'b5 (D1 is live 5-unit)', 'ambient':'q+4'},
    tuple(sorted(('B11','B21'))): {'poly':'4*q*(q+4)*D8', 'p2':'2+v2(D8)', 'p5':'b5 (D8 is 5-unit)', 'ambient':'D8@2;q+4@5'},
    tuple(sorted(('B11','B31'))): {'poly':'(q+4)*D9', 'p2':'0', 'p5':'b5+v5(D9)', 'ambient':'q+4,D9'},
    tuple(sorted(('B21','B31'))): {'poly':'-(q+2)*(q+4)*D10', 'p2':'0', 'p5':'b5 (D10 is live 5-unit)', 'ambient':'q+4'},
}

R4_LAMBDA = {
    (2,'B10'):'max(0, v2(d)+k+2+v2(x)-g-v2(h))',
    (2,'B40'):'max(0, 2*v2(d)+k+3+v2(x)-4*g-v2(alpha)-v2(h))',
    (2,'B11'):'max(0, v2(d)+1-g-v2(h))',
    (2,'B21'):'max(0, v2(d)+1-g-v2(h))',
    (2,'B31'):'max(0, v2(d)+1-g-v2(h))',
    (5,'B10'):'max(0, v5(d)+b5+2*c5+k+v5(x)-g-v5(t)-v5(h))',
    (5,'B40'):'max(0, 2*v5(d)+b5+2*c5+k+v5(x)-4*g-v5(alpha)-v5(h))',
    (5,'B11'):'max(0, v5(d)+b5+c5-g-v5(h))',
    (5,'B21'):'max(0, v5(d)+b5+c5-g-v5(h))',
    (5,'B31'):'max(0, v5(d)+b5+c5-g-v5(h))',
}

HEIGHTS = {
 'B10':'8280*d*q^7*M/h',
 'B40':'372*d*q^6*M/h',
 'B11':'42*d*q^4*M/h',
 'B21':'96*d*q^5*M/h',
 'B31':'84*d*q^5*M/h',
}

ROW_TYPES=['K_LT_G','K_EQ_G','G_LT_K']

def reciprocal_poly(poly: sp.Expr) -> sp.Expr:
    P=sp.Poly(poly,q)
    u=sp.symbols('u')
    return sp.expand(u**P.degree()*poly.subs(q,1/u))

def coeff_height(poly: sp.Expr, var=None) -> int:
    if var is None:
        syms=sorted(poly.free_symbols, key=lambda z:z.name)
        var=q if q in syms else syms[0]
    return sum(abs(int(c)) for c in sp.Poly(poly,var).all_coeffs())

def v_int(n:int,p:int)->int:
    if n==0: raise ValueError('v(0)')
    n=abs(n); e=0
    while n%p==0:
        n//=p;e+=1
    return e

def floor_log_p(n:int,p:int)->int:
    if n<1: raise ValueError
    e=0
    while n>=p:
        n//=p;e+=1
    return e
