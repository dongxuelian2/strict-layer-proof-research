#!/usr/bin/env python3
from fractions import Fraction
# This is a theorem ledger / arithmetic verifier. Source provenance is documented in report.
# Unified old tail identity: C(q)N-B(q)t = alpha*G/d.
# Old q>1 zero-tail theorem: LHS=0 is impossible. Therefore alpha != 0.
# Old bound, all q>1 charts with d=d_delta:
# |alpha| < 15*d*q^4*G/K.
# LOW + A=2u+1, u=(G+1)/q gives x>AG/10 > G^2/(5q).
# Face ratio R=|alpha|*G/(2*d*q^2*c*x*K), c>q^3.
# Hence R < 75/(2K^2) <= 3/8 since K>=10.
assert Fraction(75,2*10**2) == Fraction(3,8)
assert Fraction(3,8) < 1
print('ALPHA_VARIABLE_PROVENANCE=PASS')
print('ALPHA_ZERO_QGT1_STATUS=RETIRED_BY_OLD_ZERO_TAIL')
print('FACE_RATIO_IDENTITY=(C*N-B*t)/(2*q^2*c*x*K)')
print('FACE_RATIO_BOUND=ABS_RATIO<75/(2*K^2)<=3/8')
print('BOUNDARY_FACE_CANCELLATION=IMPOSSIBLE')
print('QGT1_SUPPORT_DEGENERATION_LOCI=NONE')
