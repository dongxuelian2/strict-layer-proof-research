#!/usr/bin/env python3
"""65-R1 exact symbolic audit: general-J provenance envelope and J=2 respecialization.

This script deliberately distinguishes:
  (i) source-proved general resonance data: J and u0 | G+1,
  (ii) the NEW canonical cyclotomic envelope built from q0=(G+1)/u0,
  (iii) the source-proved J=2 specialization u0=u, q=(G+1)/u.

It does NOT claim A_J=J*u+1 or B_J=J*G+q as a source-proved general-resonance theorem,
and it does NOT construct a general-J RCE.
"""
import sympy as sp

G,u0,q0,J = sp.symbols('G u0 q0 J', integer=True)
u,q = sp.symbols('u q', integer=True)
a3,Z,N,t = sp.symbols('a3 Z N t', integer=True)

# General source-proved cyclotomic relation, encoded as G = u0*q0 - 1.
Grel = u0*q0 - 1

Abar = J*u0 + 1
Bbar = J*G + q0

# Verify canonical envelope after substituting the exact complementary-divisor relation.
checks = {}
checks['q0_Abar_minus_Bbar_equals_J'] = sp.expand((q0*Abar-Bbar-J).subs(G,Grel))
checks['u0_Bbar_minus_G_Abar_equals_1'] = sp.expand((u0*Bbar-G*Abar-1).subs(G,Grel))

M = sp.Matrix([[G,u0],[Bbar,Abar]])
checks['det_plus_1_zero'] = sp.expand((M.det()+1).subs(G,Grel))

# For det=-1, inverse is [[-A,u0],[B,-G]].
Minv_candidate = sp.Matrix([[-Abar,u0],[Bbar,-G]])
I2 = sp.eye(2)
left = (M*Minv_candidate - I2).applyfunc(lambda x: sp.expand(x.subs(G,Grel)))
right = (Minv_candidate*M - I2).applyfunc(lambda x: sp.expand(x.subs(G,Grel)))
assert left == sp.zeros(2) and right == sp.zeros(2)

for name,val in checks.items():
    assert sp.simplify(val) == 0, (name,val)

# Primitive consequences of a Bezout identity.
# Symbolically we certify explicit Bezout representations of 1.
bezout_G_u0 = sp.expand((u0*Bbar-G*Abar).subs(G,Grel))
bezout_Abar_Bbar = sp.expand((u0*Bbar-G*Abar).subs(G,Grel))
assert bezout_G_u0 == 1 and bezout_Abar_Bbar == 1

# J=2 exact re-specialization to the source J2 chart, where u0=u and q0=q.
A2 = sp.expand(Abar.subs({J:2,u0:u,q0:q,G:u*q-1}))
B2 = sp.expand(Bbar.subs({J:2,u0:u,q0:q,G:u*q-1}))
assert A2 == 2*u+1
assert B2 == 2*(u*q-1)+q
assert sp.expand((q*A2-B2)-2) == 0
assert sp.expand(u*B2-(u*q-1)*A2-1) == 0

# J2 RCE provenance check only (NOT a general-J RCE).
G2 = u*q-1
A = 2*u+1
identity_Aq = sp.expand(2*A*q - (4*(G2-1)+2*(q+4)))
assert identity_Aq == 0

# RCE1: 2 A a3 = q(G-1)Z - N.
N_from_RCE1 = q*(G2-1)*Z - 2*A*a3
# t-definition in the recovered J2 CZ/RCE source.
t_def = q**2*Z - 4*a3
rce2_res = sp.expand((G2-1)*t_def - (2*(q+4)*a3 + q*N_from_RCE1))
rce3_res = sp.expand(q*(q+4)*Z - (A*t_def - 2*N_from_RCE1))
assert rce2_res == 0
assert rce3_res == 0

# Why full-u generalization is not automatic: if u = gamma*u0, then q=(G+1)/u=q0/gamma.
gamma = sp.symbols('gamma', integer=True, positive=True)
q_full = sp.cancel((Grel+1)/(gamma*u0))
assert sp.simplify(q_full-q0/gamma) == 0

print('J2-65 R1 UNIMODULAR SYMBOLIC CERTIFICATE')
print('STATUS=PASS')
print('SOURCE_GENERAL_RELATION=u0*q0=G+1')
print('CANONICAL_Abar=J*u0+1')
print('CANONICAL_Bbar=J*G+q0')
print('q0_Abar_MINUS_Bbar_EQUALS_J=PASS')
print('u0_Bbar_MINUS_G_Abar_EQUALS_1=PASS')
print('CANONICAL_DET_MINUS_1=PASS')
print('INVERSE=[[-Abar,u0],[Bbar,-G]]=PASS')
print('J2_A=2u+1 PASS')
print('J2_B=2G+q PASS')
print('J2_qA_MINUS_B=2 PASS')
print('J2_uB_MINUS_GA=1 PASS')
print('J2_RCE_INTERNAL_RESPECIALIZATION=PASS')
print('GENERAL_J_RCE=NOT_RECOVERED')
print('FULL_u_GENERALIZATION_WARNING=q_full=q0/gamma; source does not force gamma=1 in general resonance')
