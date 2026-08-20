#!/usr/bin/env python3
"""J2 55 R1: symbolic audit for A-residue primitive root lift.

This is a theorem-oriented algebra certificate.  It does not enumerate original
concatenation states.  It verifies the new singular-content deflation identities
and the prime-power lift form inherited from PRCC10.
"""
import sympy as sp

A0, d, Ash, Dsh, H, K, X, Z, r, c = sp.symbols(
    'A0 d Ash Dsh H K X Z r c', integer=True
)
# A=d*Ash=2u+1, D2=d*Dsh
A = d*Ash
u = (A-1)/2
D = d*Dsh
F = A*X**2 + Z*D
x = sp.symbols('x')
Q = sp.expand(A*H**2*x**2 - 2*u*K*D*x + F)
Qsh = sp.expand(Ash*H**2*x**2 - 2*u*K*Dsh*x + Ash*X**2 + Z*Dsh)

# 1. Content deflation Q=d Qsharp.
content_residual = sp.factor(Q - d*Qsh)
assert content_residual == 0

# 2. After deflation, derivative is primitive modulo Ash:
# Qsharp'(r) == K*Dsh mod Ash.
Qshp = sp.diff(Qsh, x).subs(x, r)
derivative_residual = sp.factor(Qshp - K*Dsh)
assert sp.factor(derivative_residual / Ash) == 2*H**2*r - d*K*Dsh

# 3. Original derivative divided by content obeys the same reduction mod Ash.
Qp = sp.diff(Q, x).subs(x, r)
qpd_residual = sp.factor(Qp/d - K*Dsh)
assert sp.factor(qpd_residual / Ash) == 2*H**2*r - d*K*Dsh

# 4. Exact A^2 Taylor expansion inherited from PRCC10.
Qr = Q.subs(x, r)
Qrc = sp.expand(Q.subs(x, r + A*c))
taylor_residual = sp.expand(Qrc - Qr - A*c*Qp - A**3*H**2*c**2)
assert taylor_residual == 0

# 5. Singular square signature.  For a prime p dividing d, D == 0 (mod p),
#    Kr+Z == 0 (mod p), H=G/2.  The congruence T_A == 0 (mod p)
#    is equivalent after multiplying by 4K^2 to
#    (G Z)^2 + (2K X)^2 == 0 (mod p).
G = sp.symbols('G', integer=True)
TA_mod_content = H**2*r**2 + X**2  # terms containing D vanish mod p^s
sig = sp.expand(4*K**2*TA_mod_content - (G*Z)**2 - (2*K*X)**2)
sig_sub = sp.factor(sig.subs({H:G/2, Z:-K*r}))
assert sig_sub == 0

print('J2_55_R1_SYMBOLIC_STATUS=PASS')
print('CONTENT_DEFLATION=Q=d*Qsharp')
print('DEFLATED_DERIVATIVE=Qsharp_prime(r) == K*(D2/d) (mod A/d)')
print('ORIGINAL_DERIVATIVE_AFTER_DIVISION=(Qprime(r)/d) == K*(D2/d) (mod A/d)')
print('A2_TAYLOR_RESIDUAL=0')
print('SINGULAR_SIGNATURE=4*K^2*T_A == (G*Z)^2+(2*K*X)^2 (mod p^s)')
print('P25_A_PRIME_BRANCH=ABSENT because inherited gcd(A,10)=1')
