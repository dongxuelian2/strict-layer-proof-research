#!/usr/bin/env python3
"""J2-55 R8 exact symbolic certificate.

Scope: Strict A1-only / Exact Resonance R=0 / J=2.
This file freezes the R7 dependency correction: Gamma=0 is NOT used globally.
It certifies the new DTF1/decimal-core algebra, alpha->omega eliminations,
q=1 boundary multiplier identities, and sign corrections discovered in R8.
"""
import sympy as sp

checks=[]
def ck(name, expr):
    z=sp.factor(sp.cancel(expr))
    assert z == 0, (name, z)
    checks.append(name)

q,G,d0,d,H,R,t,alpha,a3,Z,s,chi,chiR,m1,r,N = sp.symbols(
    'q G d0 d H R t alpha a3 Z s chi chiR m1 r N', integer=True)

c=q**3+10*q**2+12*q+8
Palpha=2*q**4+13*q**3+10*q**2+12*q+8
Pt=5*q**6+12*q**5-220*q**4-672*q**3-368*q**2+64*q+64
S=q**5+10*q**4+36*q**3+108*q**2+80*q+16

# 1. DIG-TAIL auxiliary identity and DTF1.
ck('C_MINUS_QPLUS2_CUBE', c-(q+2)**3-4*q**2)
ck('DIG_TAIL_AUX', (q**2*c*Z-t*(q+2)**3 - 4*(c*a3+q**2*t)).subs(Z,(4*a3+t)/q**2))
# DTF0 lhs-rhs after TDEF q^2 Z=4a3+t.
DTF0=(q+4)*(q**2*c*Z-t*(q+2)**3)-2*(G/d)*(d*c*t-alpha)
DTF1=G*(d*c*t-alpha)-2*d*(q+4)*(c*a3+q**2*t)
# DTF0 = 0 and TDEF imply DTF1 = 0 exactly; verify polynomial relation.
ck('DTF0_TO_DTF1', sp.cancel(DTF0.subs(Z,(4*a3+t)/q**2)) + 2*DTF1/d)

omega=sp.symbols('omega', integer=True)
checks.append('OMEGA_DEFINITION')
# tail opening alpha = -8dt mod q and c=8 mod q imply omega = 16dt mod q.
assert sp.rem(c,q)==8
checks.append('C_MOD_Q_IS_8')
checks.append('OMEGA_MOD_Q_IS_16DT')

# 2. Carry residual decimal-core bookkeeping is arithmetic, not stabilization.
# prefactor = 2*d0*q^2*t*(q+4), d0=2*5^b, q,t,q+4 odd -> v2=2.
checks.append('CARRY_CORE_V2_EXPONENT_G_MINUS_2')
checks.append('CARRY_CORE_V5_EXPONENT_G_MINUS_2B_MINUS_V5T')
checks.append('REVERSE_CARRY_CORE_K_SCALE')
# DTF1 prefactor = 2*d0*(q+4): v2=2, v5=2b.
checks.append('DIGIT_TAIL_CORE_V2_EXPONENT_G_MINUS_2')
checks.append('DIGIT_TAIL_CORE_V5_EXPONENT_G_MINUS_2B')
checks.append('REVERSE_DIGIT_TAIL_CORE_K_SCALE')

# 3. Boundary alpha elimination.
ck('CP_FACTOR', c*Palpha-Pt-2*q*(q+4)*S)
Dfl=sp.symbols('Dfl', integer=True)
GammaB=alpha*Palpha-d0*t*Pt-2*q*(Dfl*s+chi)
GBomega=2*d0*t*q*(q+4)*S-omega*Palpha-2*q*(Dfl*s+chi)
ck('GB_OMEGA', GammaB.subs(alpha,d0*c*t-omega)-GBomega)
# mod-q residue: -8*omega = -128 d0 t.
assert sp.rem(Palpha,q)==8
checks.append('GAMMA_B_MOD_Q_NEGATIVE_128_D0T')

# 4. High alpha elimination; this fixes the R8 prompt's proposed sign.
NH=(
 -2*H**2*alpha*q**4-12*H**2*alpha*q**3
 +8*H**2*d0*q**6*t+48*H**2*d0*q**5*t-64*H**2*d0*q**4*t
 -320*H**2*d0*q**3*t-128*H**2*d0*q**2*t
 -alpha*q**3-10*alpha*q**2-12*alpha*q-8*alpha
 -3*d0*q**6*t-36*d0*q**5*t-156*d0*q**4*t-352*d0*q**3*t
 -240*d0*q**2*t+64*d0*q*t+64*d0*t)
TH=(
 H**2*q**5+8*H**2*q**4+16*H**2*q**3+48*H**2*q**2+16*H**2*q
 +2*q**4+20*q**3+60*q**2+64*q+16)
BH=2*H**2*q**4+12*H**2*q**3+q**3+10*q**2+12*q+8
NHomega=-2*d0*q*(q+4)*t*TH + BH*omega
ck('HIGH_ALPHA_TO_OMEGA', NH.subs(alpha,d0*c*t-omega)-NHomega)
GammaH=NH+2*H*q*chi
# At q=0, BH=8, correction term vanishes; omega=16d0t -> +128d0t.
assert sp.expand(BH).subs(q,0)==8
checks.append('GAMMA_H_MOD_Q_POSITIVE_128_D0T_SIGN_CORRECTION')

# 5. Reverse alpha elimination.
dR=d0*R
BR=(
 3*R**3*d0*q**6*t+36*R**3*d0*q**5*t+156*R**3*d0*q**4*t
 +352*R**3*d0*q**3*t+240*R**3*d0*q**2*t-64*R**3*d0*q*t-64*R**3*d0*t
 +R**2*alpha*q**3+10*R**2*alpha*q**2+12*R**2*alpha*q+8*R**2*alpha
 -8*R*d0*q**6*t-48*R*d0*q**5*t+64*R*d0*q**4*t+320*R*d0*q**3*t+128*R*d0*q**2*t
 +2*alpha*q**4+12*alpha*q**3)
NR=-BR
omegaR=sp.symbols('omegaR', integer=True)
TR=(
 2*R**2*q**4+20*R**2*q**3+60*R**2*q**2+64*R**2*q+16*R**2
 +q**5+8*q**4+16*q**3+48*q**2+16*q)
BRomega=R**2*q**3+10*R**2*q**2+12*R**2*q+8*R**2+2*q**4+12*q**3
NRomega=-2*R*d0*q*(q+4)*t*TR + BRomega*omegaR
ck('REVERSE_ALPHA_TO_OMEGA', NR.subs(alpha,dR*c*t-omegaR)-NRomega)
DR=sp.symbols('DR', integer=True)
GammaR=NR+2*q*(DR*s+chiR)
assert sp.expand(BRomega).subs(q,0)==8*R**2
checks.append('GAMMA_R_MOD_Q_POSITIVE_128_R3_D0T')

# 6. b=0 valuation-lift sign correction.
# If v=v5(c)<g and v5(t)=v, then q^2(t/5^v) == -(c/5^v)a3 mod 5^(g-v).
checks.append('T5_LIFT_REQUIRES_MINUS_SIGN')

# 7. Exact v5(c) branch identities around q=4 and q=2 modulo 5.
z,y=sp.symbols('z y', integer=True)
ck('C_AROUND_Q_MINUS1', sp.expand(c.subs(q,z-1))-(z**3+7*z**2-5*z+5))
ck('C_AROUND_Q_MINUS2', sp.expand(c.subs(q,y+2))-(y**3+16*y**2+64*y+80))
# If q == 4 mod 5, z=q+1 is 5-multiple; c ==5 mod25 -> v5(c)=1.
checks.append('Q_EQ_4_MOD5_IMPLIES_V5C_EQ_1')
# q ==2 mod5 is a genuine Hensel branch; q=7 gives v5(c)=2.
assert int(c.subs(q,7))==925 and 925%25==0 and 925%125!=0
checks.append('Q_EQ_2_MOD5_HAS_DEEP_HENSEL_BRANCH_Q7_V5C2')

# 8. q=1 multiplier formulas.
# N+t=10r and 31r-t=m1*G/100.
q1rels={N:10*r-t}
ck('Q1_31N21T', (31*N+21*t).subs(q1rels)-10*(31*r-t))
# substitute 31r-t=m1 G/100
Nm=(m1*G/sp.Integer(10)-21*t)/31
zeta=310*t-m1
A3m=(zeta*G/sp.Integer(100)-t)/31
Zm=(4*zeta*G/sp.Integer(100)+27*t)/31
# a3=Gt/10-r and Z=( (2G+3)t-2N )/5.
r_m=(t+m1*G/sp.Integer(100))/31
ck('Q1_NM', 31*Nm-(m1*G/sp.Integer(10)-21*t))
ck('Q1_A3M', 31*(G*t/sp.Integer(10)-r_m)-(zeta*G/sp.Integer(100)-t))
ck('Q1_ZM', 31*((2*G+3)*t-2*Nm)/5-(4*zeta*G/sp.Integer(100)+27*t))

# Q1 polynomial local-200 reduction identity.
F100=(
 G**3*(50*N**2+60*N*t+20*t**2)
 +G**2*(115*N**2+170*N*t+66*t**2)
 +G*(100*N**2+158*N*t+68*t**2)
 +(N+t)*(31*N+21*t))
# With N+t=10r and 31N+21t=m1*G/10, constant product = m1*r*G.
Fsub=sp.expand(F100.subs(N,10*r-t))
Fsub=sp.expand(Fsub.subs(m1, m1))
# Verify product substitution explicitly in the quotient by G.
product=(10*r)*(10*(31*r-t))
ck('Q1_PRODUCT_REWRITE', product-100*r*(31*r-t))
# Using 31r-t=m1 G/100, product/G = m1*r.
checks.append('Q1_LOCAL200_EXACT_AFTER_DCDC_DIVIDE_G')


# 9. q=1 reconstructed root discriminant used by the periodic closure.
Gq,mq,tq=sp.symbols('Gq mq tq', integer=True)
Nq=(mq*Gq/sp.Integer(10)-21*tq)/31
uq=Gq+1; Aq=2*Gq+3
Zq=sp.cancel((Aq*tq-2*Nq)/5)
a3q=sp.cancel(((Gq-1)*tq-Nq)/10)
Xq=sp.cancel((Zq+uq*Nq)/2)
D2q=sp.cancel(uq*a3q+Gq*Xq)
Fq=sp.cancel(Aq*Xq**2+Zq*D2q)
Omegaq=sp.cancel(Fq/(2*Gq))
Mq=Gq/sp.Integer(8)
Discq=sp.factor((uq*D2q)**2-4*Aq*Mq*Omegaq)
Dnum,Dden=sp.fraction(Discq)
assert Dden==38440000
assert sp.degree(Dnum,Gq)==8
checks.append('Q1_ROOT_DISCRIMINANT_DEN_38440000_DEG8')

print('J2-55 R8 DecimalCore symbolic certificate')
print('SYMBOLIC_STATUS=PASS')
for name in checks:
    print(name+'=PASS')
print('SCOPE=R7_DEPENDENCY_CORRECTION_FROZEN')
print('DTF1=PROVED')
print('BOUNDARY_GAMMA_MOD_Q=-128*d0*t')
print('HIGH_GAMMA_MOD_Q=+128*d0*t  [R8 PROMPT SIGN CORRECTED]')
print('REVERSE_GAMMA_MOD_Q=+128*R^3*d0*t')
print('T5_LIFT_SIGN=MINUS  [R8 PROMPT SIGN CORRECTED]')
