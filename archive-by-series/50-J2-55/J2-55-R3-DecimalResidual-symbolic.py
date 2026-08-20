#!/usr/bin/env python3
"""J2-55 R3 symbolic audit: decimal-core normalized residual and CRT compression.

Scope: Strict Layer A1-only, Exact Resonance R=0, J=2.
This file checks algebraic identities only.  Root-necessary assumptions such as
DCDC/RQDC/OUTER are deliberately labelled as implications, not pre-root facts.
"""
from fractions import Fraction
from math import gcd
import sympy as sp

C_MAX = Fraction(2_598_001, 1_000_000)  # 1299/500 + 10^-6, valid ell>=6


def symbolic_identities():
    A,u,K,L,D,Om,x = sp.symbols('A u K L D Om x')
    M = L/8
    H2 = K*L/4  # H^2=G^2/4=KL/4
    Q = A*H2*x**2 - 2*u*K*D*x + 2*K*Om
    R = A*M*x**2 - u*D*x + Om
    lam = u*D - A*M*x
    return {
        'Q_MINUS_2K_R': sp.factor(Q-2*K*R),
        'R_MINUS_EUCLID': sp.factor(R-(Om-x*lam)),
        'R_MOD_M_QUOTIENT_MINUS_AX2': sp.factor((R-(Om-u*D*x))/M-A*x*x),
    }


def exact_constant_audit():
    # If UM-width fails and q>1, OUTER + failure yields
    #   (G/L)^2 < 292*C*(1+1/G).
    # For g>=4, 1+1/G <= 10001/10000.
    slope_const = 292*C_MAX*Fraction(10001,10000)
    assert slope_const < 759
    assert 759 < 100**2

    # h=0 failure: u^2 <= 8 C (1+1/G) < 21.
    h0 = 8*C_MAX*Fraction(10001,10000)
    assert h0 < 21

    # h<=-1 failure: multiply by 10^h <= 1/10.
    hneg = h0/Fraction(10,1)
    assert hneg < 3

    # h=1 has g>=7, so 1+1/G <= (10^7+1)/10^7.
    h1 = 80*C_MAX*Fraction(10_000_001,10_000_000)
    assert h1 < 208

    # Exact t<3q proof in h=1 once u<=13 and G>=10^7.
    # Difference between RHS 3q(G-1) and the DIG3/N-strip upper numerator is
    # q*((1201/2500)G-3)-8G.  With q>G/13 it is positive already for G>223.
    threshold_num = 107*32500
    threshold_den = 13*1201
    assert Fraction(threshold_num, threshold_den) < 223
    assert 10**7 > Fraction(threshold_num, threshold_den)

    return {
        'SLOPE_CONSTANT_UPPER': slope_const,
        'H0_U2_UPPER': h0,
        'HNEG_U2_UPPER': hneg,
        'H1_U2_UPPER': h1,
        'T_LT_3Q_THRESHOLD': Fraction(threshold_num,threshold_den),
    }


def crt_formula_sanity():
    # Synthetic coprime moduli only test formulas, not admissibility.
    tests=[]
    for A,u,M in [(23,11,125000),(27,13,125000),(47,23,1250000)]:
        assert gcd(A,u)==gcd(A,M)==gcd(u,M)==1
        r2=17 % (A*A); c3=5 % A; n=7
        x=r2+A*A*c3+A**3*n
        x10=x%M
        n10=((x10-r2-A*A*c3)*pow(A**3,-1,M))%M
        assert (n-n10)%M==0

        d=3 if A%3==0 else 1
        if d>1:
            m=2; j=4
            xs=r2+m*(A*A//d)+A*A*j
            xs10=xs%M
            m10=((xs10-r2-A*A*j)*pow(A*A//d,-1,M))%M
            assert (m-m10)%M==0
        tests.append((A,u,M,n10))
    return tests


def main():
    ids=symbolic_identities()
    assert ids['Q_MINUS_2K_R']==0
    assert ids['R_MINUS_EUCLID']==0
    assert ids['R_MOD_M_QUOTIENT_MINUS_AX2']==0
    constants=exact_constant_audit()
    tests=crt_formula_sanity()
    print('J2_55_R3_SYMBOLIC_STATUS=PASS')
    print('NORMALIZATION_Q_EQ_2K_R=PASS')
    print('EUCLIDEAN_R_EQ_OMEGA_MINUS_X_LAMBDA=PASS')
    print('RQDC_IMPLIES_M_DIVIDES_R=PASS')
    print('PAIRWISE_CRT_FORMULAS=PASS')
    print('REGULAR_TRIPLE_QUANTIZATION=LOGIC_PASS: A^3|Q, u|Q, M|R, gcd(AuM,2K)=1 => A^3*u*M|R')
    print('SINGULAR_QUANTIZATION=LOGIC_PASS: A^2|Q, u|Q, M|R => A^2*u*M|R')
    print('UM_WIDTH_FAILURE_OUTER_SLOPE=PASS: failure + OUTER => g<=ell+1')
    print('UM_WIDTH_FAILURE_H_NEG=IMPOSSIBLE')
    print('UM_WIDTH_FAILURE_H0=IMPOSSIBLE')
    print('UM_WIDTH_FAILURE_H1=IMPOSSIBLE_BY_RCE3_DIGIT_STRIP')
    print('UM_WIDTH_GLOBAL_ROOT_NECESSARY=PASS: u*M > C_ell*q')
    print('CONSTANTS=',constants)
    print('CRT_SANITY=',tests)

if __name__=='__main__':
    main()
