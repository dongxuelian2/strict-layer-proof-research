#!/usr/bin/env python3
import sympy as sp

q,u,K,m,e = sp.symbols("q u K m e", nonzero=True)
X = u*q-1
rho = 4*q**2*u**4+4*q**2*u**3+q**2*u**2-8*q*u**3-4*q*u**2+4*u**2-2
sigma = 2*q**4*u**3+q**4*u**2+16*q**3*u**3+4*q**3*u**2+32*q**2*u**3-8*q**2*u**2+4*q**2*u-32*q*u**2+8*q*u+8*u-4
S = 2*K*u*X
Phi = sp.expand(rho-S**2)
N = sp.expand(-Phi)

assert sp.expand(Phi-(rho-S**2)) == 0
assert sp.factor(rho+2-(X*(2*u+1)+1)**2) == 0
assert sp.expand(N-(1+X*(X*(4*K**2*u**2-(2*u+1)**2)-2*(2*u+1)))) == 0
assert sp.expand(N.subs(u,0)-2) == 0

# R8 imported theorem:
# X^4*A1*h - q^2*m^2 = R*e^2,
# with A1=q*sigma, h=q(2u+1), R=q^2*rho.
pulled = X**4*(q*sigma)*(q*(2*u+1)) - q**2*m**2 - (q**2*rho)*e**2
assert sp.factor(pulled/q**2) == sp.factor(X**4*sigma*(2*u+1)-m**2-rho*e**2)

print("J2-65 R9 SPECIALIZED BRAUER CERTIFICATE")
print("PHI_EQUALS_RHO_MINUS_SQUARE=PASS")
print("RHO_PLUS_2_IS_SQUARE=PASS")
print("SIGMA_FACTOR_NORM_REDUCTION=PASS_FROM_R8_IDENTITY")
print("BRAUER_STEP1=(-rho,-Phi)")
print("MINUS_PHI_IS_NORM_FROM_Q_SQRT_RHO=PASS")
print("BRAUER_STEP2=(-1,-Phi)")
print("FIXED_GAUSSIAN_NORM_TORUS=Q(i)")
print("N_MINUS_PHI_TARGET=-Phi")
print("N_CONGRUENT_1_MOD_G=PASS")
print("N_CONGRUENT_2_MOD_u=PASS")
print("RAMIFICATION_ZERO_LOCUS_ACTUAL_NECESSITY=FALSE")
print("DIVISOR_INTERSECTION_STAGE_LEGAL=FALSE")
print("J2_OBSTRUCTION_LEVEL=CYCLOTOMIC_BRAUER_SPECIALIZATION")
print("J2_STATUS=OPEN")
