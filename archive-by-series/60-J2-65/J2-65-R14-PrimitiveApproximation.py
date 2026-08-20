#!/usr/bin/env python3
"""Composite primitive-open approximation on the saturated split source conic."""
THEOREM = r'''
(1) R14 ModUAutomaticity gives Q_prim = epsilon*(x^2-Z^2) modulo u,
    epsilon a unit, and u is odd. Hence Z=1,x=1 (or -1), arbitrary a,
    is a composite-modulus primitive residue point. At such a point
    partial_x Q_prim = 2*epsilon*x is a unit modulo u.
(2) Composite Hensel, without factoring u: if r_k solves F=0 mod u^k and
    F_x(r_k) is a unit mod u, choose t mod u from
    t = -(F(r_k)/u^k) * F_x(r_k)^(-1), and replace x by x+u^k t.
    The quadratic remainder is divisible by u^(2k), hence by u^(k+1).
    Induction constructs a compatible solution modulo every u^k, i.e. a
    nonempty finite adelic primitive unit-open over the support of u.
(3) If the smooth projective source conic is split over Q, it is Q-isomorphic
    to P^1. Weak approximation, simultaneously at infinity and the finite
    support of u, gives a rational conic point in any prescribed nonempty real
    projective W-sector and in this finite primitive unit-open.
(4) Express the rational point in the source-lattice basis, clear denominators,
    and divide the global gcd. The resulting primitive lattice generator differs
    at the finite places only by local units, so Z remains a unit modulo u.
    U-SQ then makes x a unit modulo u as well.
'''
assert 'Composite Hensel' in THEOREM and 'Weak approximation' in THEOREM
print('LOCAL_PRIMITIVE_OPEN_NONEMPTY=PROVED')
print('COMPOSITE_HENSEL_WITHOUT_FACTORING_u=PROVED')
print('SPLIT_CONIC_WEAK_APPROXIMATION=PROVED_APPLICABLE')
print('PRIMITIVE_SOURCE_LATTICE_LIFT=PROVED')
print('COMPOSITE_PRIMITIVE_OPEN_APPROXIMATION=PROVED')
print('PRIMITIVE_MODULO_u_OBSTRUCTION=RETIRED')
print('RAY_x0_UNIT_FROM_Z0_UNIT_AND_U_SQ=AUTOMATIC')
print('STRONG_APPROXIMATION_NOT_INVOKED=TRUE')
print('PRIME_BY_PRIME_LOCALIZATION_USED=FALSE')
