#!/usr/bin/env python3
"""Exact algebraic intersection of the LOW boundary 10x=Aa with the source conic core."""
import sympy as sp
G,q,K,z=sp.symbols('G q K z')
# From R14 ModU audit: integer source-core after removing the global rational scalar.
Z,a,x=sp.symbols('Z a x')
F=(2*G**5*Z**2*q**4-16*G**5*Z*a*q**2+32*G**5*a**2-4*G**4*K*Z*q**4*x+16*G**4*K*a*q**2*x+G**4*Z**2*q**5+2*G**4*Z**2*q**4-16*G**4*Z*a*q**3-48*G**4*Z*a*q**2+48*G**4*a**2*q+160*G**4*a**2-4*G**3*K*Z*q**4*x+8*G**3*K*a*q**3*x+48*G**3*K*a*q**2*x+2*G**3*Z**2*q**5-4*G**3*Z*a*q**4-40*G**3*Z*a*q**3-48*G**3*Z*a*q**2+24*G**3*a**2*q**2+192*G**3*a**2*q+320*G**3*a**2+2*G**3*q**4*x**2+8*G**2*K*a*q**3*x+48*G**2*K*a*q**2*x-8*G**2*Z*a*q**4-32*G**2*Z*a*q**3-16*G**2*Z*a*q**2+4*G**2*a**2*q**3+72*G**2*a**2*q**2+288*G**2*a**2*q+320*G**2*a**2+G**2*q**5*x**2+2*G**2*q**4*x**2-8*G*K*a*q**3*x+16*G*K*a*q**2*x-8*G*Z*a*q**3+8*G*a**2*q**3+72*G*a**2*q**2+192*G*a**2*q+160*G*a**2-8*K*a*q**3*x+4*Z*a*q**4+4*a**2*q**3+24*a**2*q**2+48*a**2*q+32*a**2)
A=(2*G+q+2)/q
P=sp.Poly(sp.together(F.subs({Z:z,a:1,x:A/10}))*100*q**2,z)
# remove harmless denominator/scalar content automatically
content,primitive=sp.Poly(sp.expand(P.as_expr()),z).primitive()
primitive=sp.Poly(primitive,z)
assert primitive.degree()==2
disc=sp.factor(sp.discriminant(primitive.as_expr(),z))
# Normalize the discriminant to a named exact polynomial; sign is not fixed by the global base identities alone.
print('LOW_PROJECTIVE_BOUNDARY=10*x=A*a3')
print('BOUNDARY_INTERSECTION_POLYNOMIAL_DEGREE=2')
print('BOUNDARY_POLYNOMIAL_LEADING_COEFF='+str(sp.factor(primitive.all_coeffs()[0])))
print('BOUNDARY_DISCRIMINANT='+str(disc))
print('LOW_BOUNDARY_CONIC_INTERSECTION=OPEN')
print('UNIFORM_PROJECTIVE_CLEARANCE=UNRESOLVED')
