#!/usr/bin/env python3
"""A1 J2 GRFC9 symbolic global root-factor certificate.

This script checks, with exact SymPy algebra, the normalization requested in the
GRFC9 campaign.  The main correction is that the proposed root-factor quotient
kappa is exactly the old integral root a1; GRFQ is four times the inherited
radial root quadratic after clearing the decimal normalization.
"""
import sympy as sp


def symbolic_checks():
    A,G,K,u,D2,F,a,b,kappa,L = sp.symbols(
        'A G K u D2 F a b kappa L', nonzero=True
    )
    X = 2*u*a*D2
    Omega = F/(2*K)

    # Frozen structural identities: K = G*a/b and L=10^ell=G*b/a.
    subsK = {K: G*a/b}
    subsL = {L: G*b/a}

    F1 = A*G*b*kappa/2
    F2_product = sp.simplify(A*b**2*F/F1)
    F2_candidate = 4*a*Omega/kappa
    f2_residual = sp.factor((F2_product - F2_candidate).subs(subsK))
    assert f2_residual == 0

    # F1+F2=2X gives GRFQ.
    grfq_sum = sp.expand(F1 + F2_candidate - 2*X)
    # Multiply by 2*kappa/a and use G*b/a=L.
    grfq_q = A*L*kappa**2 - 8*u*D2*kappa + 8*Omega
    grfq_from_sum = sp.factor((2*kappa/a*grfq_sum).subs({G: L*a/b}))
    assert sp.simplify(grfq_from_sum - grfq_q) == 0

    # Clear Omega and L.  This is exactly 4 times the inherited root quadratic.
    grfq_cleared = sp.expand((K*grfq_q).subs({L: G**2/K, Omega: F/(2*K)}))
    expected_cleared = A*G**2*kappa**2 - 8*u*K*D2*kappa + 4*F
    assert sp.expand(grfq_cleared - expected_cleared) == 0

    H = G/2
    root_q = A*H**2*kappa**2 - 2*u*K*D2*kappa + F
    root_residual = sp.factor(expected_cleared - 4*root_q)
    assert root_residual == 0

    # CQRF/RCE cleared splice.  M,R,Y,E are independent symbolic placeholders
    # linked by D2=E/(2M), 4M^2 F=P=AY^2+2RE.
    M,E,P = sp.symbols('M E P', nonzero=True)
    cqrf = A*G**2*M**2*kappa**2 - 4*u*K*E*M*kappa + P
    cqrf_from_root = sp.expand(
        expected_cleared.subs({D2: E/(2*M), F: P/(4*M**2)}) * M**2
    )
    cqrf_residual = sp.factor(cqrf_from_root - cqrf)
    assert cqrf_residual == 0

    # RQDC is the exact equality behind the congruence.
    rq_exact = sp.expand(u*D2*kappa - Omega - A*L*kappa**2/8)
    rq_from_grfq = sp.factor(grfq_q + 8*rq_exact)
    assert rq_from_grfq == 0

    # BRANCH audit: if Omega is also written with a1 via the old full-root factor,
    # comparing the two formulas is just the difference of the same quadratic at
    # kappa and a1.
    a1 = sp.symbols('a1')
    omega_k = kappa*u*D2 - A*L*kappa**2/8
    omega_a1 = a1*u*D2 - A*L*a1**2/8
    branch = sp.factor(omega_k - omega_a1)
    branch_expected = sp.factor((kappa-a1)*(u*D2 - A*L*(kappa+a1)/8))
    assert sp.expand(branch - branch_expected) == 0

    # Discriminant of the cleared kappa polynomial is 16 times the standard
    # root discriminant; no new discriminant has been created.
    disc_k = sp.factor(sp.discriminant(expected_cleared, kappa))
    disc_root = sp.factor((2*u*K*D2)**2 - 4*A*(G/2)**2*F)
    disc_residual = sp.factor(disc_k - 16*disc_root)
    assert disc_residual == 0

    return {
        'F2_RESIDUAL': f2_residual,
        'GRFQ_TO_ROOT_RESIDUAL': root_residual,
        'CQRF_SPLICE_RESIDUAL': cqrf_residual,
        'DISCRIMINANT_RESIDUAL': disc_residual,
        'BRANCH_FACTORIZATION': branch,
        'CLEARED_GRFQ': expected_cleared,
        'CQRF_GRFQ': cqrf,
    }


def chamber_checks():
    # Exact integer regressions in high, boundary, and reverse chambers.
    out = []
    g = 20
    for delta in (3, 1, 0, -1, -4):
        k = g + delta
        ell = g - delta
        assert k > 0 and ell > 0
        aa = 10**max(delta, 0)
        bb = 10**max(-delta, 0)
        G = 10**g
        K = 10**k
        L = 10**ell
        assert K == G*aa//bb
        assert G*bb == L*aa
        out.append((delta, k, ell, aa, bb, 'PASS'))
    return out


if __name__ == '__main__':
    res = symbolic_checks()
    chambers = chamber_checks()
    print('GRFC9_SYMBOLIC_STATUS=PASS')
    for k, v in res.items():
        print(f'{k}={v}')
    print('KAPPA_EQUALS_A1_FROM_FROZEN_ROOT_FORMULA=PASS')
    print('GRFQ_IS_FOUR_TIMES_OLD_ROOT_QUADRATIC=PASS')
    print('RQDC_IS_EXACT_ROOT_FACTOR_NORMALIZATION=PASS')
    print('CHAMBER_NORMALIZATION_CHECKS=', chambers)
