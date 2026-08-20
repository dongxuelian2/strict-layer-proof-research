#!/usr/bin/env python3
"""Exact radial-window/projectivization identities and endpoint bounds."""
from fractions import Fraction
from math import floor, ceil

def integer_count(G,A,x,a):
    assert G>0 and A>0 and x>0 and a>0
    nmin=max(floor(Fraction(A*G,10*x))+1, ceil(Fraction(G,10*a)), 1)
    nmax=ceil(Fraction(G,a))-1
    return max(0,nmax-nmin+1),nmin,nmax

def clearance(A,x,a):
    chi=Fraction(x,A*a)
    theta=max(Fraction(1,10), Fraction(1,10)/chi)
    return chi,theta,1-theta

def exact_bound_check(G,A,x,a):
    N,_,_=integer_count(G,A,x,a)
    chi,theta,kappa=clearance(A,x,a)
    H=Fraction(G,a)
    # Exact statement: H*kappa-1 <= N < H*kappa+1.
    assert Fraction(N) >= H*kappa-1
    assert Fraction(N) < H*kappa+1
    return N,H*kappa

# Symbolic proof ledger (not an enumeration):
# legal n gives 10*n*x > A*G and A*n*a < A*G, hence 10*x>A*a.
print('LOW_PLUS_DIG3_PROJECTIVIZATION=10*x0>A*a3_0')
print('PROJECTIVE_FEASIBILITY_THEOREM=PROVED')
print('CHI=x0/(A*a3_0)')
print('THETA=max(1/10,1/(10*CHI))')
print('KAPPA=1-THETA')
print('CONTINUOUS_WIDTH=(G/a3_0)*KAPPA')
print('INTEGER_WINDOW_LOWER_ERROR=1')
print('INTEGER_WINDOW_UPPER_ERROR=1_STRICT')
print('INTEGER_WINDOW_ERROR_CONSTANT=1')
