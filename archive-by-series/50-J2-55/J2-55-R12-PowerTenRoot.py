#!/usr/bin/env python3
"""J2-55 R12 power-of-ten integer-root descent utilities.

The key scope correction is explicit:
a R10 periodic residue cell does not by itself freeze e,t,gamma, so the
rational-root theorem gives a finite r-list only on a fixed coefficient fibre.
"""
from math import gcd
import sympy as sp
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    "rootcert", HERE/"J2-55-R12-RootSaturation-symbolic.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

R,G=m.R,m.G
q,K,e,f,w,t,gamma=m.q,m.K,m.e,m.f,m.w,m.t,m.gamma

def lowest_power(P,x):
    P=sp.Poly(sp.expand(P),x)
    return min(i for i in range(P.degree()+1) if P.nth(i)!=0)

def power_ten_bound_from_constant(C):
    """For an actual nonzero integer C, return max r with 10^r | C."""
    C=abs(int(C))
    if C==0:return None
    v2=v5=0
    z=C
    while z%2==0:v2+=1;z//=2
    z=C
    while z%5==0:v5+=1;z//=5
    return min(v2,v5)

def exact_possible_r(C, rmin=0):
    b=power_ten_bound_from_constant(C)
    if b is None:return None
    return list(range(rmin,b+1))

for name,P,x in [
    ("BOUNDARY",m.P_B,G),("HIGH",m.P_H,G),
    ("REVERSE_GENERIC",m.P_R,R),("REVERSE_K1",m.P_K1,R)]:
    poly=sp.Poly(P,x)
    print(name,"degree",poly.degree(),"lowest_power",lowest_power(P,x),
          "constant",sp.factor(poly.nth(0)))

Cg=sp.factor(sp.Poly(m.P_R,R).nth(0))
C1=sp.factor(sp.Poly(m.P_K1,R).nth(0))
assert sp.factor(Cg.subs(q,0) + 2*K**2*gamma**2)==0
assert sp.factor(C1.subs(q,0)-10*gamma**2)==0

print("REVERSE_GENERIC_C0_MOD_Q=-2*K^2*gamma^2")
print("REVERSE_K1_C0_MOD_Q=10*gamma^2")
print("THEREFORE_C0_ZERO_IMPLIES_q|gamma (q ten-unit, gcd(K,q)=1)")
print("INHERITED_R11_DU_MODQ=unit*t; hence q∤t => C0!=0 on legal normalized branch")
print("FIXED_COEFFICIENT_FIBRE_THEOREM=if C0!=0 and P(10^r)=0 then 10^r|C0")
print("PERIODIC_CELL_ALONE_FIXES_COEFFICIENTS=FALSE")
print("CELL_LEVEL_FINITE_R_BY_RATIONAL_ROOT=NOT_PROVED")
print("NO_FALSE_TYPE_CLOSURE=PASS")
