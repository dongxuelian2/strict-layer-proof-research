#!/usr/bin/env python3
"""Whole-modulus reduced-residue covering object. No factorisation of u."""
THEOREM_SOURCE = 'H. Iwaniec, On the problem of Jacobsthal, Demonstratio Math. 11 (1978), 225-231'
CONVENTION = 'j(m)=min J such that every block of J consecutive integers contains an integer coprime to m'
# Iwaniec proves C(r) << r^2 log^2 r for the maximum bad run covered by r arbitrary primes.
# Since coprimality depends only on rad(m), j(m)=C(supp(m))+1; standard primorial growth
# r log r << log m converts this to j(m) << (log m)^2 with an absolute, non-explicit constant.
print('MULTIPLIER_MODULUS=10*u')
print('COVERING_RADIUS_OBJECT=Jacobsthal_j')
print('JACOBSTHAL_CONVENTION='+CONVENTION)
print('JACOBSTHAL_GLOBAL_BOUND=PROVED_FROM_SOURCE:j(m)<<log(m)^2')
print('BOUND_CONSTANT=ABSOLUTE_NONEXPLICIT')
print('SQUAREFREE_RESTRICTION=NONE; j(m)=j(rad(m))')
print('FACTOR_u_USED=FALSE')
print('PRIME_RESIDUE_CASES_USED=FALSE')
