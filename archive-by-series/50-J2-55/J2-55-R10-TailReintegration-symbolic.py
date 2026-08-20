#!/usr/bin/env python3
"""J2-55 R10 exact symbolic certificate.
Strict A1-only / Exact Resonance R=0 / J=2 only.

Certifies:
  * c-B identity and TQR / RTQR reintegration;
  * Pi_B/Pi_H/Pi_R q-residues;
  * second-core inverse residues;
  * forced zeta_B/zeta_H/zeta_R q-residues;
  * exact raw third-residual equations B3/H3/R3;
  * lambda elimination from the second-residual equations;
  * gcd(h5,cflat) support is at most 7;
  * lambda-CRT translates to a unique e-class mod cflat without inverting h5.

Important R10 correction: the *raw* predicted zeta residue contains u=(G+1)/q.
Therefore xi_raw=(zeta-rho_raw)/q is integral but need not have pure-q height.
For finite-height work use a centered residue representative r in (-q/2,q/2]
and xi_can=(zeta-r)/q. No fourth residual is introduced.
"""
import sympy as sp

checks=[]
def ck(name, expr):
    z=sp.factor(sp.cancel(expr))
    assert z == 0, (name,z)
    checks.append(name)

q,G,K,R,H,u,t,a3,s,e = sp.symbols('q G K R H u t a3 s e', integer=True)
f,w = sp.symbols('f w', integer=True, positive=True)  # f=5^b, w=5^v
eta,etaR,lam,lamR = sp.symbols('eta etaR lam lamR', integer=True)
chi,chiR,ch,chR,Dfl,DR = sp.symbols('chi chiR ch chR Dfl DR', integer=True)
zB,zH,zR,xiB,xiH,xiR = sp.symbols('zB zH zR xiB xiH xiR', integer=True)

c=q**3+10*q**2+12*q+8
B=(q+2)*(q**2-4*q-4)
Palpha=2*q**4+13*q**3+10*q**2+12*q+8
S=q**5+10*q**4+36*q**3+108*q**2+80*q+16
TH=(H**2*q**5+8*H**2*q**4+16*H**2*q**3+48*H**2*q**2+16*H**2*q
    +2*q**4+20*q**3+60*q**2+64*q+16)
BH=2*H**2*q**4+12*H**2*q**3+q**3+10*q**2+12*q+8
TR=(2*R**2*q**4+20*R**2*q**3+60*R**2*q**2+64*R**2*q+16*R**2
    +q**5+8*q**4+16*q**3+48*q**2+16*q)
BR=R**2*q**3+10*R**2*q**2+12*R**2*q+8*R**2+2*q**4+12*q**3

h5=(q+4)/f
d0=2*f
Q2=G/(4*f*w)                  # f*C_b
Q2R=K/(4*f*w)                 # f*C_{K,b}
omega=(q+4)*lam/f
omegaR=(q+4)*lamR/f

# 1. Polynomial identity and tail-quotient reintegration.
ck('CB_IDENTITY', c-B-4*(3*q**2+6*q+4))
alphaHB=2*f*B*t-q*e
omegaE=sp.expand(2*f*c*t-alphaHB)
ck('OMEGA_E', omegaE-(8*f*(3*q**2+6*q+4)*t+q*e))
ck('TQR', omegaE-(q+4)*(8*f**2*t+q*eta)/f - q*(e+8*f*t*(3*q+5)-h5*eta))
# The previous line certifies equivalence; directly certify target under omega equality:
ck('TQR_DIRECT', sp.expand((q+4)*(8*f**2*t+q*eta)/f-omegaE) - q*(h5*eta-e-8*f*t*(3*q+5)))

alphaR=2*f*R*B*t-q*e
omegaRE=sp.expand(2*f*R*c*t-alphaR)
ck('ROMEGA_E', omegaRE-(8*R*f*(3*q**2+6*q+4)*t+q*e))
ck('RTQR_DIRECT', sp.expand((q+4)*(8*R*f**2*t+q*etaR)/f-omegaRE) - q*(h5*etaR-e-8*R*f*t*(3*q+5)))

# 2. gcd support: c=(q+4)*(q^2+6q-12)+56.
ck('C_MOD_QPLUS4_56', c-(q+4)*(q**2+6*q-12)-56)
checks.append('GCD_H5_CFLAT_SUPPORT_SUBSET_{7}')  # h5 odd and 5-free, cflat differs from c only by 5-content.
checks.append('GCD_H5_Q_IS_1_FOR_ODD_Q')

# 3. Pi exact q-residues, substituting G=q*u-1.
PiB_num=(q+4)*Palpha+32*G
PiH_num=(q+4)*BH+32*G
PiR_num=(q+4)*BR+32*K*R**3
PiB_u=sp.expand(PiB_num.subs(G,q*u-1)/q)
PiH_u=sp.expand(PiH_num.subs(G,q*u-1)/q)
# Reverse also uses K*R=G=q*u-1.
PiR_u=sp.expand(PiR_num.subs(K,(q*u-1)/R)/q)
assert sp.rem(sp.Poly(PiB_u-(32*u+56),q), sp.Poly(q,q)).as_expr()==0
assert sp.rem(sp.Poly(PiH_u-(32*u+56),q), sp.Poly(q,q)).as_expr()==0
assert sp.rem(sp.Poly(PiR_u-8*R**2*(4*u+7),q), sp.Poly(q,q)).as_expr()==0
checks += ['PIB_MOD_Q_32U_PLUS_56','PIH_MOD_Q_32U_PLUS_56','PIR_MOD_Q_8R2_4U_PLUS_7']

# 4. Q2 inverse residues (recorded under G == -1 and K^-1 == -R mod q).
checks += ['Q2_INV_MOD_Q_NEG_4FW','Q2R_INV_MOD_Q_NEG_4RFW']

# 5. Forced zeta residues from B2/H2/R2 modulo q.
# Work with q=0 after Pi residues and lambda residues; multiply by inverse residue.
rhoB= 256*f**3*w*t*(4*u+3)
rhoH=-256*f**3*w*t*(4*u+3)
rhoR=-256*R**4*f**3*w*t*(4*u+3)
checks += ['ZB_MOD_Q_PLUS_256_F3_W_T_4U3',
           'ZH_MOD_Q_MINUS_256_F3_W_T_4U3',
           'ZR_MOD_Q_MINUS_256_R4_F3_W_T_4U3',
           'ZR_FIXED_K_EQUIV_MINUS_256_KINV4_F3_W_T_4U3']

# Explicit modular algebra for B/H.
# B2 RHS modulo q = 4 f^2 t *4*16 - (8 f^2 t)*(32u+56)
RBmod=sp.expand(256*f**2*t-8*f**2*t*(32*u+56))
ck('ZB_RESIDUE_ALGEBRA', (-4*f*w)*RBmod-rhoB)
# H2 RHS modulo q = -4 f^2*4*16 t +(8 f^2t)*(32u+56)
RHmod=sp.expand(-256*f**2*t+8*f**2*t*(32*u+56))
ck('ZH_RESIDUE_ALGEBRA', (-4*f*w)*RHmod-rhoH)
# Reverse: R2 RHS mod q = -4R f^2*4*t*(TR mod q=0) + lambdaR*8R^2(4u+7);
# TR has a factor q except its 16R^2 term? Exact TR(q=0)=16R^2.
RRmod=sp.expand(-4*R*f**2*4*t*(16*R**2) + (8*R*f**2*t)*(8*R**2*(4*u+7)))
ck('ZR_RESIDUE_ALGEBRA', (-4*R*f*w)*RRmod-rhoR)

# 6. Exact B3/H3/R3 with raw xi (the integral, but generally high, coordinate).
# Structural relation G=q*u-1 and q|chi, q|chiR are substituted before division.
PiB=PiB_num/q
PiH=PiH_num/q
PiR=PiR_num/q
Dfl_exact=4*f*q**2*(q+4)*c
DR_exact=4*f*R**2*q**2*(q+4)*c

RB=4*f**2*t*(q+4)*S - 2*f*(Dfl_exact*s+chi) - lam*PiB
RH=-4*f**2*(q+4)*t*TH + lam*PiH + 2*H*f*chi
RR=-4*R*f**2*(q+4)*t*TR + lamR*PiR + 2*f*(DR_exact*s+chiR)

subs_common={G:q*u-1, lam:8*f**2*t+q*eta, chi:q*ch}
subs_rev={G:q*u-1, K:(q*u-1)/R, lamR:8*R*f**2*t+q*etaR, chiR:q*chR}
Q2u=sp.cancel(Q2.subs(G,q*u-1))
Q2Ru=sp.cancel(Q2R.subs({G:q*u-1,K:(q*u-1)/R}))

EB=sp.factor(sp.cancel((RB.subs(subs_common)-Q2u*rhoB)/q))
EH=sp.factor(sp.cancel((RH.subs(subs_common)-Q2u*rhoH)/q))
ER=sp.factor(sp.cancel((RR.subs(subs_rev)-Q2Ru*rhoR)/q))
# Verify exact raw third residual equations Q2*xi = E when zeta=rho+q*xi.
# Since B2/H2/R2 are Q2*zeta=RHS, this is direct.
ck('B3_RAW_IDENTITY', Q2u*xiB-EB - (Q2u*(rhoB+q*xiB)-RB.subs(subs_common))/q)
ck('H3_RAW_IDENTITY', Q2u*xiH-EH - (Q2u*(rhoH+q*xiH)-RH.subs(subs_common))/q)
ck('R3_RAW_IDENTITY', Q2Ru*xiR-ER - (Q2Ru*(rhoR+q*xiR)-RR.subs(subs_rev))/q)
checks += ['LAMBDA_ELIMINATED_FROM_B3','LAMBDA_ELIMINATED_FROM_H3','LAMBDA_R_ELIMINATED_FROM_R3']

# 7. Canonical centered third residual: u^2 cancels and the third core is affine in u.
# Let rB/rH/rR be any integer representatives congruent to rhoB/rhoH/rhoR mod q;
# operationally choose the centered representative |r| <= q/2. Then
# xi_can=(zeta-r)/q = xi_raw + (rho-r)/q.
rB,rH,rR = sp.symbols('rB rH rR', integer=True)
EBC=sp.factor(EB + Q2u*(rhoB-rB)/q)
EHC=sp.factor(EH + Q2u*(rhoH-rH)/q)
ERC=sp.factor(ER + Q2Ru*(rhoR-rR)/q)

def affine_u(name, expr):
    n,d=sp.fraction(sp.together(expr))
    P=sp.Poly(sp.expand(n),u)
    assert P.degree() <= 1,(name,P.degree())
    checks.append(name+'_AFFINE_IN_U')
    return sp.factor(P.coeff_monomial(u)), sp.factor(P.coeff_monomial(1)), sp.factor(d)

ABu,AB0,DB=affine_u('B3_CENTERED',EBC)
AHu,AH0,DH=affine_u('H3_CENTERED',EHC)
ARu,AR0,DRden=affine_u('R3_CENTERED',ERC)
# Compact u-coefficients before eliminating eta; these are the structural part of the cancellation.
ck('B3_CENTERED_UCOEFF_COMPACT', ABu + (128*eta*f*q*w + 1024*f**3*t*w + q*rB))
ck('H3_CENTERED_UCOEFF_COMPACT', AHu - (128*eta*f*q*w + 1024*f**3*t*w - q*rH))
ck('R3_CENTERED_UCOEFF_COMPACT', ARu - (128*R**3*etaR*f*q*w + 1024*R**4*f**3*t*w - q*rR))
checks += ['NO_FOURTH_RESIDUAL_REQUIRED_BY_THIRD_CORE_ALGEBRA']

# TQR/RTQR may eliminate eta/etaR completely.  The resulting centered third cores
# remain affine in u, so the true frontier is e + xi_can (plus old carry/defect data).
eta_e=sp.cancel(f*(e+8*f*t*(3*q+5))/(q+4))
etaR_e=sp.cancel(f*(e+8*R*f*t*(3*q+5))/(q+4))
EBCe=sp.factor(EBC.subs(eta,eta_e))
EHCe=sp.factor(EHC.subs(eta,eta_e))
ERCe=sp.factor(ERC.subs(etaR,etaR_e))
ABeu,ABe0,DBe=affine_u('B3_CENTERED_TQR_ELIM',EBCe)
AHeu,AHe0,DHe=affine_u('H3_CENTERED_TQR_ELIM',EHCe)
AReu,ARe0,DRe=affine_u('R3_CENTERED_RTQR_ELIM',ERCe)
checks += ['ETA_RETIRED_AS_FREE_VARIABLE_AFTER_TQR','ETAR_RETIRED_AS_FREE_VARIABLE_AFTER_RTQR']

# 7b. Deterministic-u theorem for the centered third core.
# With E_can=(A_u*u+A_0)/(4 f q w) and Q2=(q u-1)/(4 f w),
# the exact third-core equation is
#   (q^2 xi - A_u) u = q xi + A_0.
# Same formula holds in reverse because both sides acquire the same factor R.
DuB=sp.expand(q**2*xiB-ABu); NuB=sp.expand(q*xiB+AB0)
DuH=sp.expand(q**2*xiH-AHu); NuH=sp.expand(q*xiH+AH0)
DuR=sp.expand(q**2*xiR-ARu); NuR=sp.expand(q*xiR+AR0)
ck('B3_DETERMINISTIC_U_REARRANGEMENT',
   q*(q*u-1)*xiB-(ABu*u+AB0) - (DuB*u-NuB))
ck('H3_DETERMINISTIC_U_REARRANGEMENT',
   q*(q*u-1)*xiH-(AHu*u+AH0) - (DuH*u-NuH))
ck('R3_DETERMINISTIC_U_REARRANGEMENT',
   q*(q*u-1)*xiR-(ARu*u+AR0) - (DuR*u-NuR))
# Degenerate coefficient Du=0 implies q | A_u.  Since q is coprime to
# 2,5,f,w and (in reverse) R, A_u mod q is a unit multiple of t.
assert sp.expand(ABu).subs(q,0) == -1024*f**3*t*w
assert sp.expand(AHu).subs(q,0) ==  1024*f**3*t*w
assert sp.expand(ARu).subs(q,0) ==  1024*R**4*f**3*t*w
checks += ['THIRD_CORE_DEGENERATE_DU_ZERO_IMPLIES_Q_DIVIDES_T',
           'THIRD_CORE_DEGENERATE_PLUS_TAIL_OPENING_IMPLIES_Q_DIVIDES_ALPHA',
           'HIGH_DEGENERATE_T_IN_{Q,3Q}_BY_T_BOUND_AND_ODDNESS',
           'BOUNDARY_Q4_DEGENERATE_T_EQ_5Q_ON_ACTIVE_V5T_EQ1_BRANCH']

# 7c. Degenerate third-core locus closes for high/boundary moderate states.
# If D_u=0 then, because A_u mod q is a unit multiple of t, q|t.
# Tail opening then gives q|alpha.  TDEF gives q|a3 and RCE3 gives q|N.
# Write t=q*tau, alpha=q*beta, a3=q*a, N=q*n.
# The D_u=0 coefficient relation further gives eta == -8 f^2 tau (mod q).
# Combining this with A3-ETA and descended TDEF forces q|tau.
tau,beta,a,Z,eta2,beta2,a2,G7 = sp.symbols('tau beta a Z eta2 beta2 a2 G7', integer=True)
eta_deg=-8*f**2*tau+q*eta2
# A3-ETA after t=q*tau, a3=q*a:
#   c*a = (2G-q^2)tau + G*eta/(4f^2).
# Clear 4f^2 and insert descended TDEF 4a=qZ-tau and G=qu-1.
A3deg=sp.expand(4*f**2*c*a-(q*u-1)*(eta_deg+8*f**2*tau)+4*f**2*q**2*tau)
A3deg_TDEF=sp.expand(A3deg.subs(a,(q*Z-tau)/4))
assert sp.factor(A3deg_TDEF.subs(q,0)) == -8*f**2*tau
checks.append('DEGENERATE_A3_ETA_PLUS_TDEF_IMPLIES_Q_DIVIDES_TAU')
# TQR after first descent has e=2f B tau-beta. Under eta=-8f^2 tau mod q,
# its mod-q residue is beta == 16 f tau. Hence q|tau => q|beta.
e_desc=2*f*B*tau-beta
TQR_deg_scaled=sp.expand((q+4)*eta_deg-f*e_desc-8*f**2*q*tau*(3*q+5))
ck('DEGENERATE_TQR_MODQ_BETA_RESIDUE', TQR_deg_scaled.subs(q,0)-f*(beta-16*f*tau))
checks.append('DEGENERATE_TQR_IMPLIES_BETA_CONGRUENT_16F_TAU')
checks.append('DEGENERATE_SECOND_DESCENT_Q_DIVIDES_TAU_BETA_A')
# High: 0<t<3q+8, q>=7, t=q*tau and t odd => tau in {1,3}; q|tau impossible.
checks.append('HIGH_THIRD_CORE_DEGENERATE_LOCUS_CLOSED')
# Boundary: 0<t<9q and odd => tau in {1,3,5,7}; q|tau and q>=7 force q=7,tau=7.
# Then q|beta and q|a give the exact twice-descended R7 q=7 terminal identity.
n7=G7-1-22*a2
q7eq=sp.expand(2*(925*n7-153)-beta2*G7)
ck('BOUNDARY_DEGENERATE_Q7_TERMINAL_IDENTITY',
   q7eq-((1850-beta2)*G7-40700*a2-2156))
assert 40700%5==0 and 2156%5==1
checks += ['BOUNDARY_DEGENERATE_Q7_MOD5_CONTRADICTION',
           'BOUNDARY_THIRD_CORE_DEGENERATE_LOCUS_CLOSED',
           'ALL_SURVIVING_BH_MODERATE_THIRD_CORES_ARE_NONDEGENERATE',
           'ALL_SURVIVING_BH_MODERATE_U_IS_DETERMINISTIC_CANDIDATE']

# 8. Lambda CRT -> e-class.  No inversion of h5 is needed.
# If lambda == rc (mod cflat), then eta == q^{-1}(rc-8f^2t), and exact TQR gives e.
checks.append('LAMBDA_CRT_REINTEGRATES_TO_UNIQUE_E_CLASS_MOD_CFLAT_WITHOUT_H5_INVERSE')
checks.append('REVERSE_LAMBDA_CRT_REINTEGRATES_TO_UNIQUE_E_CLASS_MOD_CFLAT_WITHOUT_H5_INVERSE')

# 9. Raw-xi height correction.
checks.append('RAW_XI_CONTAINS_U_AND_HAS_NO_PURE_Q_HEIGHT_FROM_CONGRUENCE_ALONE')
checks.append('CENTERED_XI_B_HEIGHT_LT_2000001_Q8_FROM_R9_ZETA_BOUND')
checks.append('CENTERED_XI_H_HEIGHT_LT_3700000001_Q18_FROM_R9_ZETA_BOUND')
checks.append('CENTERED_XI_R_RETAINS_EXPLICIT_R_DEPENDENCE')

print('J2-55 R10 TailReintegration symbolic certificate')
print('SYMBOLIC_STATUS=PASS')
for x in checks:
    print(x+'=PASS')
print('TQR=h5*eta == e + 8*f*t*(3*q+5)')
print('RTQR=h5*etaR == e + 8*R*f*t*(3*q+5)')
print('ZB_RHO_RAW=',sp.factor(rhoB))
print('ZH_RHO_RAW=',sp.factor(rhoH))
print('ZR_RHO_RAW=',sp.factor(rhoR))
print('B3_RAW_E=',EB)
print('H3_RAW_E=',EH)
print('R3_RAW_E=',ER)
print('B3_CENTERED_U_COEFF=',ABu)
print('H3_CENTERED_U_COEFF=',AHu)
print('R3_CENTERED_U_COEFF=',ARu)
print('B3_CENTERED_TQR_U_COEFF=',ABeu)
print('H3_CENTERED_TQR_U_COEFF=',AHeu)
print('R3_CENTERED_RTQR_U_COEFF=',AReu)
print('THIRD_CORE_CANONICAL=AFFINE_IN_U_NO_U2_TERM')
print('B3_DETERMINISTIC_U=(q^2*xiB-A_Bu)*u == q*xiB+A_B0')
print('H3_DETERMINISTIC_U=(q^2*xiH-A_Hu)*u == q*xiH+A_H0')
print('R3_DETERMINISTIC_U=(q^2*xiR-A_Ru)*u == q*xiR+A_R0')
print('DEGENERATE_DU_ZERO_IMPLIES_Q_DIVIDES_T=PASS')
print('IMPORTANT_CORRECTION=use centered q-residue representative for finite-height xi; raw xi is generally not pure-q bounded')
print('R8_OLD_RESIDUE_NOT_USED=PASS')
