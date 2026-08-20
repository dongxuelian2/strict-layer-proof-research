#!/usr/bin/env python3
import sympy as sp

G,K,u,q,m,c,z,Y=sp.symbols('G K u q m c z Y', integer=True)
A=2*u+1
B=2*G+q
H=G/2
N0=4*u**2*G**2*K**2-(G*A+1)**2+2

# J2 determinant package.
# qA-B=2 and uB-GA=1 follow from uq=G+1.
q_sub=(G+1)/u
assert sp.factor((q*A-B).subs(q,q_sub)-2)==0
assert sp.factor((u*B-G*A).subs(q,q_sub)-1)==0

# PRE_ROOT negative-chart compression: m=Ah-Gz, h=qHz-Ac.
h=q*H*z-A*c
m_expr=sp.expand(A*h-G*z)
assert sp.factor((m_expr-(B*H*z-A**2*c)).subs(q,q_sub))==0

# Inverse formulas, valid on the J2 determinant locus.
z_inv=2*(m+A**2*c)/(B*G)
w_inv=(G*m-A*c)/B
d2_inv=(G**2*m+c)/B

# Verify these against the old c,z chart w=G H z-u A c, d2=u c+G w.
w_old=G*H*z-u*A*c
d2_old=u*c+G*w_old
subs_m={m:B*H*z-A**2*c}
assert sp.factor((w_inv.subs(subs_m)-w_old).subs(q,q_sub))==0
assert sp.factor((d2_inv.subs(subs_m)-d2_old).subs(q,q_sub))==0
assert sp.factor((z_inv.subs(subs_m)-z).subs(q,q_sub))==0

# Moving square discriminant Delta0 in (m,c), clearing the B denominator.
Delta=u**2*K**2*d2_inv**2-A*H**2*(A*w_inv**2+z_inv*d2_inv)
Qmc=sp.factor(4*B**2*Delta)
Qmc_expected=(
    G**2*(N0-1)*m**2
    +2*G*(4*G*K**2*u**2-A)*m*c
    +(4*K**2*u**2-G*A**3*(G*A+2))*c**2
)
assert sp.factor(Qmc-Qmc_expected)==0

P=sp.Poly(Qmc_expected,m,c)
a=P.coeff_monomial(m**2)
b=P.coeff_monomial(m*c)
cc=P.coeff_monomial(c**2)
disc=sp.factor(b**2-4*a*cc)
disc_expected=(2*G*A*(G*A+1))**2*N0
assert sp.factor(disc-disc_expected)==0

print('QGT1_SPARSE_ELIMINATION=PASS')
print('M_IDENTITY=m=B*H*z-A^2*c')
print('INVERSE_z=2(m+A^2c)/(BG)')
print('INVERSE_w=(Gm-Ac)/B')
print('INVERSE_d2=(G^2m+c)/B')
print('QMC=G^2(N0-1)m^2+2G(4GK^2u^2-A)mc+(4K^2u^2-GA^3(GA+2))c^2')
print('ROOT_SQUARE=QMC=(2BY)^2')
print('DISC_QMC=(2GA(GA+1))^2*N0')
print('VERDICT=REPRESENTATIONAL_COMPRESSION_ONLY__OLD_N0_SQUARECLASS_RETURNS')
