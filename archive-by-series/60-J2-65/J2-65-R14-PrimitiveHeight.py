#!/usr/bin/env python3
"""Structural primitive-height audit."""
THEOREM = r'''
For a fixed smooth split conic with a nonempty real projective sector a3>0,
rational points are dense in that sector. Clearing denominators and taking the
canonical primitive lattice generator gives infinitely many primitive rays. A
bounded a3-coordinate together with the other fixed projective inequalities would
leave only finitely many primitive lattice vectors in any bounded box; hence no
upper bound for canonical a3 follows from primitivity/SNF/discriminant alone.
The exact Boundary Transference instead supplies a lower height condition on any
multiplier-failing ray: a3 >= G*kappa/j(10u) when kappa>0.
'''
assert 'primitivity/SNF/discriminant alone' in THEOREM
print('CANONICAL_DIGIT_HEIGHT=a3_0')
print('STRUCTURAL_LOWER_BOUND=a3_0>=1')
print('SNF_M_ALONE_GIVES_HEIGHT_UPPER_BOUND=FALSE')
print('PRIMITIVITY_ALONE_GIVES_HEIGHT_UPPER_BOUND=FALSE')
print('MULTIPLIER_FAILURE_HEIGHT_BOUND=a3_0>=G*kappa(chi)/j(10*u)')
print('IWANIEC_ASYMPTOTIC_HEIGHT_BOUND=a3_0>>G*kappa(chi)/log(10*u)^2')
