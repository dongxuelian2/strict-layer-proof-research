#!/usr/bin/env python3
"""Finite-period Euclidean-quotient lift for J2-55 R6.

The theorem implemented here is deliberately weaker than an affine Hensel law:
after tail substitution the quotient is P(10^g)+r(10^g), with fixed structural
denominator D and r -> 0.  Hence mu modulo p is an exact finite-periodic
function of the exponent index once the finite prefix is removed.  The critical
q=11 fibre happens to collapse further to an affine mod-11 law.
"""
from math import gcd
from fractions import Fraction
from sympy.ntheory import n_order
import sys
sys.set_int_max_str_digits(1_000_000)

def vp(n,p):
 c=0
 while n%p==0:c+=1;n//=p
 return c

def split_10_part(D):
 a=b=0
 while D%2==0:a+=1;D//=2
 while D%5==0:b+=1;D//=5
 return a,b,D

def eventual_period_for_floor_polynomial(D,T,p):
 # To know floor(J/D) mod p it is enough to know J mod pD.
 M=p*D
 a,b,Mstar=split_10_part(M)
 if Mstar==1:return max(a,b),1
 base=pow(10,T,Mstar)
 return max(a,b),int(n_order(base,Mstar))

def fit_affine_mod_p(p,pairs):
 sols=[]
 for a in range(p):
  for b in range(p):
   if all((a*z+b)%p==m%p for z,m in pairs):sols.append((a,b))
 return sols

# Certified exact critical-fibre regression from the R6 exact search.
critical_g=[471,13077,50895,63501,101319,126531]
critical_mu_mod_11=[10,7,9,6,8,2]
n0=(critical_g[0]-1)//2
pairs=[]
for g,m in zip(critical_g,critical_mu_mod_11):
 n=(g-1)//2
 assert (n-n0)%11==0
 z=(n-n0)//11
 pairs.append((z%11,m))
sol=fit_affine_mod_p(11,pairs)
assert sol==[(8,10)],sol

# q=11,h=1 critical structural denominator.
q=11;d0=10;c=q**3+10*q*q+12*q+8
D=2*d0*q*q*(q+4)*c
prefix,period=eventual_period_for_floor_polynomial(D,T=2,p=11)

print('J2-55 R6 Quotient Lift')
print('GENERIC_MU_NEXT=FINITE_PERIODIC_AFTER_EXPLICIT_PREFIX')
print('GENERIC_STATE=(floor_residue_mod_D, remainder_sign)')
print('PREDICTED_ROOT_LIFT=FINITE_STATE_EXACT; GLOBAL_LOW_DEGREE_POLYNOMIAL_NOT_PROVED')
print('CRITICAL_Q11_PAIRS=',pairs)
print('CRITICAL_Q11_MU_MOD_11=10+8*z mod 11 [regression, six certified lifts]')
print('CRITICAL_Q11_AFFINE_FIT=PASS')
print('CRITICAL_Q11_STRUCTURAL_D=',D)
print('CRITICAL_Q11_EVENTUAL_PREFIX_BOUND_FROM_2_5_PART=',prefix)
print('CRITICAL_Q11_FLOOR_STATE_PERIOD_DIVIDES=',period)
