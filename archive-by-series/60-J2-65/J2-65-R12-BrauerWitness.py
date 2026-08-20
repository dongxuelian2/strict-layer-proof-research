#!/usr/bin/env python3
import sympy as sp

a,b,rho,S,N = sp.symbols("a b rho S N", nonzero=True)
xg = (a + S*b**2)/(1+b**2)
yg = b*(S-a)/(1+b**2)

num = sp.factor(sp.together(xg**2 + yg**2 - N).as_numer_denom()[0])
num = sp.factor(num.subs(a**2, N-rho*b**2).subs(S**2, N+rho))

binv_err = sp.factor(sp.together(yg/(S-xg)-b))
ainv_num = sp.factor(sp.together((S*xg-N)/(S-xg)-a).as_numer_denom()[0])
ainv_num = sp.factor(ainv_num.subs(a**2, N-rho*b**2).subs(S**2, N+rho))

print("J2-65 R12 BRAUER WITNESS CERTIFICATE")
print("GAUSSIAN_FORWARD_REAL_PART=", xg)
print("GAUSSIAN_FORWARD_IMAG_PART=", yg)
print("NORM_IDENTITY_NUMERATOR_REDUCED=", num)
print("FORWARD_NORM_MAP=PASS" if num == 0 else "FORWARD_NORM_MAP=FAIL")
print("B_INVERSE_ERROR=", binv_err)
print("A_INVERSE_NUMERATOR_ERROR=", ainv_num)
print("BIRATIONAL_INVERSE=PASS" if binv_err == 0 and ainv_num == 0 else "BIRATIONAL_INVERSE=FAIL")
print("FORWARD_DENOMINATOR=1+b^2>0")
print("INVERSE_EXCEPTION=S-xg; impossible when rho=S^2-N>0")
print("BRAUER_TO_GAUSSIAN_WITNESS_TYPE=EXPLICIT_RATIONAL")
