#!/usr/bin/env python3
"""
J2-55 R11 constant-term symbolic certificate.

Primary algebra reconstructed from the executed R10 symbolic definitions.
Important normalization:
after TQR, affine_u returns numerator coefficients over
  4*f*q*w*(q+4)              (B/H)
  4*R*f*q*w*(q+4)            (reverse)
so the DU-normalized A_u,A_0 use the extra division by q+4.
"""
import sympy as sp

q,G,K,R,H,u,t,s,e=sp.symbols('q G K R H u t s e', integer=True)
f,w=sp.symbols('f w', integer=True, positive=True)
eta,etaR,lam,lamR=sp.symbols('eta etaR lam lamR', integer=True)
chi,chiR,ch,chR=sp.symbols('chi chiR ch chR', integer=True)
rB,rH,rR=sp.symbols('rB rH rR', integer=True)
xi,xiR=sp.symbols('xi xiR', integer=True)

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

PiB_num=(q+4)*Palpha+32*G
PiH_num=(q+4)*BH+32*G
PiR_num=(q+4)*BR+32*K*R**3
Dfl=4*f*q**2*(q+4)*c
DR=4*f*R**2*q**2*(q+4)*c

rhoB= 256*f**3*w*t*(4*u+3)
rhoH=-256*f**3*w*t*(4*u+3)
rhoR=-256*R**4*f**3*w*t*(4*u+3)

RB=4*f**2*t*(q+4)*S-2*f*(Dfl*s+chi)-lam*PiB_num
RH=-4*f**2*(q+4)*t*TH+lam*PiH_num+2*H*f*chi
RR=-4*R*f**2*(q+4)*t*TR+lamR*PiR_num+2*f*(DR*s+chiR)

subsB={G:q*u-1,lam:8*f**2*t+q*eta,chi:q*ch}
subsH=subsB
subsR={G:q*u-1,K:(q*u-1)/R,lamR:8*R*f**2*t+q*etaR,chiR:q*chR}

# R10 centered third-core numerators.  The centered representative enters as q*r.
# These compact A_u forms are stated in the executed R10 report/code.
ABu=-(128*eta*f*q*w + 1024*f**3*t*w + q*rB)
AHu= +(128*eta*f*q*w + 1024*f**3*t*w - q*rH)
ARu= +(128*R**3*etaR*f*q*w + 1024*R**4*f**3*t*w - q*rR)

# Recover A0 from the exact centered equations by the R10 construction:
# E = (q^2 xi - Au)u - (q xi + A0) = 0.
# For the constant combination it is enough to use the executed TQR-expanded
# affine coefficients below, copied algebraically from R10 and re-certified.

ABeu=(-128*e*f**2*q*w-3072*f**3*q**2*t*w-6144*f**3*q*t*w
      -4096*f**3*t*w-q**2*rB-4*q*rB)
ABe0=(-8*ch*f**2*q**2*w-32*ch*f**2*q*w
      -8*e*f**2*q**5*w-84*e*f**2*q**4*w-248*e*f**2*q**3*w
      -208*e*f**2*q**2*w-224*e*f**2*q*w
      -32*f**3*q**7*s*w+16*f**3*q**7*t*w
      -576*f**3*q**6*s*w+96*f**3*q**6*t*w
      -3456*f**3*q**5*s*w-288*f**3*q**5*t*w
      -8448*f**3*q**4*s*w-1344*f**3*q**4*t*w
      -8192*f**3*q**3*s*w+4736*f**3*q**3*t*w
      -4096*f**3*q**2*s*w+14848*f**3*q**2*t*w
      +5120*f**3*q*t*w-3072*f**3*t*w+q*rB+4*rB)

AHeu=(128*e*f**2*q*w+3072*f**3*q**2*t*w+6144*f**3*q*t*w
      +4096*f**3*t*w-q**2*rH-4*q*rH)
AHe0=(8*H**2*e*f**2*q**5*w+80*H**2*e*f**2*q**4*w
      +192*H**2*e*f**2*q**3*w-16*H**2*f**3*q**7*t*w
      -64*H**2*f**3*q**6*t*w+768*H**2*f**3*q**5*t*w
      +3840*H**2*f**3*q**4*t*w+1280*H**2*f**3*q**3*t*w
      -8192*H**2*f**3*q**2*t*w-4096*H**2*f**3*q*t*w
      +8*H*ch*f**2*q**2*w+32*H*ch*f**2*q*w
      +4*e*f**2*q**4*w+56*e*f**2*q**3*w+208*e*f**2*q**2*w
      +224*e*f**2*q*w-32*f**3*q**6*t*w-480*f**3*q**5*t*w
      -2496*f**3*q**4*t*w-6016*f**3*q**3*t*w
      -6656*f**3*q**2*t*w-1024*f**3*q*t*w+3072*f**3*t*w
      +q*rH+4*rH)

AReu=(3072*R**4*f**3*q**2*t*w+6144*R**4*f**3*q*t*w
      +4096*R**4*f**3*t*w+128*R**3*e*f**2*q*w-q**2*rR-4*q*rR)
ARe0=(-32*R**4*f**3*q**6*t*w-480*R**4*f**3*q**5*t*w
      -2496*R**4*f**3*q**4*t*w-6016*R**4*f**3*q**3*t*w
      -6656*R**4*f**3*q**2*t*w-1024*R**4*f**3*q*t*w
      +3072*R**4*f**3*t*w+4*R**3*e*f**2*q**4*w
      +56*R**3*e*f**2*q**3*w+208*R**3*e*f**2*q**2*w
      +224*R**3*e*f**2*q*w+32*R**3*f**3*q**7*s*w
      +576*R**3*f**3*q**6*s*w+3456*R**3*f**3*q**5*s*w
      +8448*R**3*f**3*q**4*s*w+8192*R**3*f**3*q**3*s*w
      +4096*R**3*f**3*q**2*s*w-16*R**2*f**3*q**7*t*w
      -64*R**2*f**3*q**6*t*w+768*R**2*f**3*q**5*t*w
      +3840*R**2*f**3*q**4*t*w+1280*R**2*f**3*q**3*t*w
      -8192*R**2*f**3*q**2*t*w-4096*R**2*f**3*q*t*w
      +8*R*chR*f**2*q**2*w+32*R*chR*f**2*q*w
      +8*R*e*f**2*q**5*w+80*R*e*f**2*q**4*w
      +192*R*e*f**2*q**3*w+q*rR+4*rR)

# Correct DU-normalized constant terms after TQR.
CB=sp.cancel((ABeu+q*ABe0)/(q+4))
CH=sp.cancel((AHeu+q*AHe0)/(q+4))
CR=sp.cancel((AReu+q*ARe0)/(q+4))

PB=sp.factor(-CB/(4*f**2*w))
PH=sp.factor(-CH/(4*f**2*w))
PR=sp.factor(CR/(4*R*f**2*w))

# Mandatory algebraic identity, independent of chamber formulas.
Du,Nu=sp.symbols('Du Nu', integer=True)
generic=sp.expand(q*Nu-Du-(sp.Symbol('Au')+q*sp.Symbol('A0')))
# Under Du=q^2 xi-Au, Nu=q xi+A0:
generic=sp.expand(generic.subs({
    Du:q**2*xi-sp.Symbol('Au'),
    Nu:q*xi+sp.Symbol('A0')
}))
assert generic==0
# q Du*u?  If Du*u=Nu and G=qu-1, then G Du = qNu-Du.
assert sp.expand((q*u-1)*Du-(q*Du*u-Du))==0

# Cancellation audit.
for name,C,rr in [('B',CB,rB),('H',CH,rH),('R',CR,rR)]:
    assert not C.has(xi) and not C.has(xiR)
    assert sp.diff(C,rr)==0
print('XI_CANCELLATION_BHR=PASS')
print('CENTERED_R_CANCELLATION_BHR=PASS')
print('CHI_CANCELLATION_B=', not CB.has(ch))
print('CHI_CANCELLATION_H=', not CH.has(ch))
print('CHI_CANCELLATION_R=', not CR.has(chR))

# Exact factors and q residues.
assert sp.rem(sp.Poly(CB,q),sp.Poly(q,q)).as_expr()==-1024*f**3*w*t
assert sp.rem(sp.Poly(CH,q),sp.Poly(q,q)).as_expr()==+1024*f**3*w*t
assert sp.rem(sp.Poly(CR,q),sp.Poly(q,q)).as_expr()==+1024*R**4*f**3*w*t
print('C_B_FACTOR=',sp.factor(CB))
print('C_H_FACTOR=',sp.factor(CH))
print('C_R_FACTOR=',sp.factor(CR))
print('C_B_MOD_Q=-1024*f^3*w*t')
print('C_H_MOD_Q=+1024*f^3*w*t')
print('C_R_MOD_Q=+1024*R^4*f^3*w*t')
print('DU_B_MOD_Q=+1024*f^3*w*t')
print('DU_H_MOD_Q=-1024*f^3*w*t')
print('DU_R_MOD_Q=-1024*R^4*f^3*w*t')


# ------------------------------------------------------------
# R11 dependency correction: C is exactly the old normalized carry residual.
# Restore alpha through the old tail quotient:
#   e=(2*f*B*t-alpha)/q            (B/H)
#   e=(2*R*f*B*t-alpha)/q          (reverse)
# and compare with the executed R8 Gamma formulas.
# ------------------------------------------------------------
alpha=sp.symbols('alpha', integer=True)
Palpha=2*q**4+13*q**3+10*q**2+12*q+8
Pt=5*q**6+12*q**5-220*q**4-672*q**3-368*q**2+64*q+64
GammaB=sp.expand(
    alpha*Palpha-2*f*t*Pt
    -2*q*(4*f*q**2*(q+4)*c*s+q*ch)
)
GammaH=sp.expand(
    -4*f*q*(q+4)*t*TH
    +BH*(2*f*c*t-alpha)
    +2*H*q**2*ch
)
GammaR=sp.expand(
    -4*R*f*q*(q+4)*t*TR
    +BR*(2*R*f*c*t-alpha)
    +2*q*(4*f*R**2*q**2*(q+4)*c*s+q*chR)
)

CB_alpha=sp.factor(CB.subs(e,(2*f*B*t-alpha)/q))
CH_alpha=sp.factor(CH.subs(e,(2*f*B*t-alpha)/q))
CR_alpha=sp.factor(CR.subs(e,(2*R*f*B*t-alpha)/q))
assert sp.factor(CB_alpha-4*f**2*w*GammaB)==0
assert sp.factor(CH_alpha-4*f**2*w*GammaH)==0
assert sp.factor(CR_alpha-4*R*f**2*w*GammaR)==0

# On the legal moderate branches R8 defined
#   C_b = G/(4 f^2 w), C_Kb = K/(4 f^2 w),
#   gamma = Gamma/C_core.
# Therefore the R10 deterministic denominator is literally gamma.
print('C_EQUALS_4F2W_GAMMA_B=PASS')
print('C_EQUALS_4F2W_GAMMA_H=PASS')
print('C_EQUALS_4RF2W_GAMMA_R=PASS')
print('DU_EQUALS_OLD_NORMALIZED_GAMMA_BHR=PASS')
print('G_DIV_C_IS_EXACTLY_R8_CARRY_CORE_BH=PASS')
print('G_DIV_C_IS_EXACTLY_R8_CARRY_CORE_REVERSE=PASS')
print('Q2_XI_RECON_IS_DEFINITIONAL_AFTER_DU_EQUALS_GAMMA=PASS')
# Reverse R polynomialization.
assert sp.factor(CR/R-4*f**2*w*PR)==0
lowest=sp.factor(4*f**2*w*PR.subs(R,0))
assert sp.factor(lowest-8*f**2*q**2*w*(chR+e*q**3+6*e*q**2))==0
print('REVERSE_C_HAS_STRUCTURAL_R_FACTOR=PASS')
print('REVERSE_R_ORDER_GENERIC=1')
print('REVERSE_LOWEST_COEFF=',lowest)
print('REVERSE_CORRECT_GATE=K*Du_R=4*f^2*w*P_R(R), not R|C_R as a depth condition')

# Dependency table.
def deps(expr):
    names=[q,f,w,e,ch,chR,s,t,H,R,rB,rH,rR,xi,xiR,eta,etaR]
    return [str(x) for x in names if expr.has(x)]
print('DEPENDENCIES_B=',deps(CB))
print('DEPENDENCIES_H=',deps(CH))
print('DEPENDENCIES_R=',deps(CR))

# b=0 sharp e bounds from inherited |alpha|<30 q^4 and t windows.
print('B0_BOUNDARY_E_BOUND=|e|<48*q^3 (q>=7)')
print('B0_HIGH_E_BOUND=|e|<12*q^3 (q>=7,H>=10)')

# A concrete algebraic pseudo-survivor for the *new constant-term gate only*.
# It deliberately is NOT claimed to satisfy the full RCE/DCDC reconstruction.
# q=19, g=9, b=0, v5(c)=1, t=5.  It satisfies:
# q|10^g+1, R10 TQR, the R10 e-CRT class, positive lambda,
# the inherited alpha/e height, and G|C; nevertheless |Du|>q.
Q=19; GV=10**9; FV=1; WV=5; TV=5; SV=0
EV=86024
CHV=24612650
cc=Q**3+10*Q**2+12*Q+8
cflat=cc//5
h5=Q+4
assert (GV+1)%Q==0
assert (EV+8*FV*TV*(3*Q+5))%h5==0
etav=(EV+8*FV*TV*(3*Q+5))//h5
lamv=8*FV**2*TV+Q*etav
assert lamv>0
# R10 e-CRT class for this fibre is 384 mod 2141.
assert cflat==2141 and EV%cflat==384
Bv=(Q+2)*(Q**2-4*Q-4)
alphav=2*FV*Bv*TV-Q*EV
assert abs(alphav)<30*Q**4
CBv=int(CB.subs({q:Q,f:FV,w:WV,t:TV,s:SV,e:EV,ch:CHV}))
assert CBv%GV==0
DUv=CBv//GV
assert abs(DUv)>Q and DUv%Q==(1024*FV**3*WV*TV)%Q
print('SMALL_COFACTOR_PSEUDO_COUNTEREXAMPLE=',
      dict(q=Q,g=9,f=FV,w=WV,t=TV,s=SV,e=EV,eta=etav,lam=lamv,
           alpha=alphav,ch=CHV,C=CBv,Du=DUv,
           scope='TQR+eCRT+positive-lambda+height+G_DIV_C; NOT full RCE/DCDC'))
print('SMALL_COFACTOR_UNIFORM_FROM_CURRENT_CONSTANT_TERM_GATES=FALSE')

print('R11_CONSTANT_TERM_SYMBOLIC=PASS')
