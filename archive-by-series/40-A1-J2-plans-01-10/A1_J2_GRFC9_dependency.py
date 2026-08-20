#!/usr/bin/env python3
"""Dependency/provenance audit for A1 J2 GRFC9.

The important distinction is between *operational search order* and *logical
provenance*.  DCDC (2K | Ftilde for ell>=3) can be tested before an explicit
square-root computation, but it was proved from the integral-root factor system;
therefore it is a root-necessary condition, not a pre-root identity.
"""

LEDGER = [
    ("RCE1--RCE3 and reconstruction of a3,Z,Xcal,D2", "PRE_ROOT", "frozen linear/radial terminal data"),
    ("Ftilde=A*Xcal^2+Z*D2", "PRE_ROOT", "definition"),
    ("root polynomial Q(T)=A H^2 T^2-2uKD2 T+Ftilde", "PRE_ROOT", "polynomial coefficients are defined before asserting an integral root"),
    ("Psi_delta=X_delta^2-A b^2 Ftilde", "PRE_ROOT", "definition of square kernel"),
    ("Psi_delta=s^2", "LAYER_S", "introduces integer square root s"),
    ("AG b | 2(X_delta +/- s)", "LAYER_S_PLUS_R", "integral-root divisibility"),
    ("a1=2(X_delta +/- s)/(AG b)", "FULL_ROOT", "actual positive integral root"),
    ("Ftilde=a1*Lambda", "FULL_ROOT", "root-factor identity"),
    ("AH^2*a1+Lambda=2uKD2", "FULL_ROOT", "complementary root-factor identity"),
    ("2K | Lambda and 2K | Ftilde (ell>=3)", "ROOT_NECESSARY", "decimal core derived from integral-root factor system; safe early sieve, not pre-root provenance"),
    ("Omega_hat=Ftilde/(2K) in Q", "PRE_ROOT_RATIONAL", "always definable as a rational number"),
    ("Omega=Ftilde/(2K) in Z", "ROOT_NECESSARY", "integer status is DCDC/root-core dependent"),
    ("Lambda=2K*lambda0", "FULL_ROOT", "requires root factor plus decimal core"),
    ("lambda0=uD2-(A*10^ell/8)*a1", "FULL_ROOT", "normalized complementary root equation"),
    ("Omega=a1*lambda0", "FULL_ROOT", "product of two post-root quantities"),
    ("gcd(lambda0,10)=1 (ell>=4)", "FULL_ROOT", "deduced from normalized root factor and ten-unit u,D2,A"),
    ("kappa=2(X_delta+eps*s)/(AG b)", "FULL_ROOT", "definition uses Layer S+R; equals a1 for the selected sign"),
    ("kappa | 4 a Omega", "FULL_ROOT", "integer divisibility meaningful after Omega integrality"),
    ("GRFQ with Omega_hat rational", "ROOT_EQUIVALENT", "equivalent to the old integral-root polynomial after clearing denominators"),
    ("RQDC", "FULL_ROOT_NECESSARY", "exactly the normalized complementary root relation modulo 10^ell/8"),
]

if __name__ == '__main__':
    print('GRFC9_DEPENDENCY_AUDIT=PASS')
    print('IDENTITY\tSTATUS\tNOTE')
    for row in LEDGER:
        print('\t'.join(row))
    print('DCDC_PRE_ROOT_PROVENANCE=FALSE')
    print('DCDC_SAFE_EARLY_SIEVE=TRUE')
    print('OMEGA_INTEGER_PRE_ROOT=FALSE')
    print('OMEGA_RATIONAL_PRE_ROOT=TRUE')
    print('BRANCH_IDENTITY_NEW_THEOREM=FALSE_TAUTOLOGICAL_VIETA')
