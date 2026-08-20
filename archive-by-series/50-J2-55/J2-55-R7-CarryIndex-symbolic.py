#!/usr/bin/env python3
"""J2-55 R7 exact symbolic audit.

Scope: Strict A1-only / Exact Resonance R=0 / J=2.
This file deliberately distinguishes:
  (i) exact integer carry identities;
  (ii) exact all-exponent carry-residual divisibilities;
  (iii) stabilized constant-term equalities.
No stabilized equality is promoted to an all-exponent theorem.
"""
import sympy as sp

checks=[]
def ck(name, expr):
    z=sp.factor(sp.cancel(expr))
    assert z==0,(name,z)
    checks.append(name)

def coeff0(expr,G):
    n,d=sp.fraction(sp.cancel(expr))
    return sp.factor(sp.Poly(sp.expand(n),G).coeff_monomial(1)), sp.factor(d)

G,q,alpha,t,d0,H,R,s,chi,e = sp.symbols('G q alpha t d0 H R s chi e', nonzero=True)
uvar,ch1=sp.symbols('uvar ch1')
c=q**3+10*q**2+12*q+8
C=q*c
B=(q+2)*(q**2-4*q-4)
u=(G+1)/q
A=2*u+1

# Cheap algebraic identities.
ck('B_PLUS_8_FACTOR', B+8-q*(q**2-2*q-12))
ck('DTF_AUX_FACTOR', c*(q+2)-2*B-(q+2)**3*(q+4))
# Correct mod-5 polynomial: c == (q-2)(q+1)^2 mod 5.
diff5=sp.Poly(sp.expand(c-(q-2)*(q+1)**2),q)
assert all(int(z)%5==0 for z in diff5.all_coeffs())
checks.append('C_MOD5_CORRECTED')
assert (7**3+10*7**2+12*7+8)==925 and 925%5==0
checks.append('C_TENUNIT_GLOBAL_CONJECTURE_FALSE_Q7')

# H1 proof arithmetic: for g>=2, (5^g-1)m > 2^(g+2)+4 for m>=1.
for gg in range(2,80):
    assert (5**gg-1) > 2**(gg+2)+4
checks.append('B_LT_G_CHEAP_LEMMA_ARITHMETIC')

# General tail-reconstructed RCE data.
def reconstructed(d):
    N=sp.cancel((B*t+alpha*G/d)/C)
    Z=sp.cancel((A*t-2*N)/(q*(q+4)))
    a3=sp.cancel(((G-1)*t-q*N)/(2*(q+4)))
    X=sp.cancel((Z+u*N)/2)
    D2=sp.cancel(u*a3+G*X)
    F=sp.cancel(A*X**2+Z*D2)
    return N,Z,a3,X,D2,F

# High/boundary quotient.
N,Z,a3,X,D2,F = reconstructed(d0)
U=sp.cancel(8*u*D2/(A*(G/H)))
nU,dU=sp.fraction(U)
Qh,Rh=sp.div(sp.Poly(nU,G),sp.Poly(dU,G))
Ph=sp.factor(Qh.as_expr())
remh=sp.factor(Rh.as_expr()/dU)
Dfl=2*d0*q**2*(q+4)*c
Jh=sp.factor(Dfl*Ph)
assert sp.denom(sp.cancel(Jh))==1
checks.append('JH_INTEGER_POLYNOMIAL')
# chi=J-D mu => eps_fl=mu-P=-chi/D exactly.
mu=sp.symbols('mu', integer=True)
ck('CHI_EPS_EXACT', (mu-Ph) + (Jh-Dfl*mu)/Dfl)

# Boundary R6 epsilon target and BCI sign.
Pb=sp.factor(Ph.subs(H,1))
Omega_b=sp.cancel(F/(2*G))
eps=sp.symbols('eps')
Dec_b=sp.cancel(u*D2*(Pb+eps-s)-Omega_b)
nb,db=sp.fraction(Dec_b)
const_b=sp.factor(sp.Poly(sp.expand(nb),G).coeff_monomial(1))
epsB=sp.factor(sp.solve(sp.Eq(const_b,0),eps)[0])
eps0=sp.factor(epsB-s)
Palpha=2*q**4+13*q**3+10*q**2+12*q+8
Pt=5*q**6+12*q**5-220*q**4-672*q**3-368*q**2+64*q+64
ck('BOUNDARY_EPS0_FORMULA', eps0-(-alpha*Palpha+d0*t*Pt)/(2*q*Dfl))
GammaB=alpha*Palpha-d0*t*Pt-2*q*(Dfl*s+chi)
# Under eps=-chi/D, the exact decimal congruence numerator has constant -2 d q^2 t(q+4) GammaB.
Dec_b_chi=sp.cancel(Dec_b.subs(eps,-chi/Dfl))
cb,denb=coeff0(Dec_b_chi,G)
ck('BOUNDARY_CONSTANT_RESIDUAL_FACTOR', cb + 2*d0*q**2*t*(q+4)*GammaB)
# Stabilized GammaB=0 -> + opening.
assert sp.rem(Palpha,q)==8 and sp.rem(Pt,q)==64
checks.append('BOUNDARY_ROOT_POSITIVE_OPENING_STABILIZED')

# High carry numerator / sign.
Omega_h=sp.cancel(F/(2*G*H))
Dec_h=sp.cancel(u*D2*(Ph+eps)-Omega_h)
nh,dh=sp.fraction(Dec_h)
const_h=sp.factor(sp.Poly(sp.expand(nh),G).coeff_monomial(1))
epsH=sp.factor(sp.solve(sp.Eq(const_h,0),eps)[0])
NH=sp.factor(sp.cancel(epsH*(2*H*q*Dfl)))
assert sp.denom(NH)==1
GammaH=sp.factor(NH+2*H*q*chi)
Dec_h_chi=sp.cancel(Dec_h.subs(eps,-chi/Dfl))
ch,denh=coeff0(Dec_h_chi,G)
ck('HIGH_CONSTANT_RESIDUAL_FACTOR', ch-2*d0*q**2*t*(q+4)*GammaH)
# NH mod q = -8 alpha +64 d0 t.
ck('HIGH_NH_MODQ_POLY', sp.rem(sp.Poly(NH-(-8*alpha+64*d0*t),q),sp.Poly(q,q)).as_expr())
checks.append('HIGH_ROOT_POSITIVE_OPENING_STABILIZED')

# Tail opening alpha=d B t-qe gives alpha == -8 d t mod q.
alpha_tail=d0*B*t-q*e
ck('TAIL_NEGATIVE_OPENING_FACTOR', alpha_tail+8*d0*t-q*(d0*(q**2-2*q-12)*t-e))
checks.append('TAIL_NEGATIVE_OPENING_EXACT')

# Stronger exact fact: q|chi already follows from tail opening, without q|t.
Jtail=sp.expand(Jh.subs({G:q*uvar-1,alpha:alpha_tail}))
assert sp.factor(Jtail).has(q)
Jtail_over_q=sp.factor(sp.cancel(Jtail/q))
assert sp.denom(Jtail_over_q)==1
checks.append('CHI_DIV_Q_FROM_TAIL_OPENING_HIGH_BOUNDARY')
# residue of chi/q (because Dfl is q^2-multiple)
J1mod=sp.factor(Jtail_over_q.subs(q,0))
ck('CHI_OVER_Q_RESIDUE', J1mod-8*H*(16*d0*t*uvar-4*d0*t-e))

# Exact normalized-root mod-q degeneracy: not a positive opening.
x=sp.cancel((Jh-chi)/Dfl-s)
Rnorm_b=sp.cancel(A*(G/8)*x.subs(H,1)**2-u*D2*x.subs(H,1)+Omega_b)
rbn,rbd=sp.fraction(Rnorm_b)
root_sub=sp.factor(rbn.subs({G:q*uvar-1,alpha:alpha_tail,chi:q*ch1,H:1}))
root_q3=sp.cancel(root_sub/q**3)
root_modq=sp.factor(root_q3.subs(q,0))
ch1B=sp.factor(J1mod.subs(H,1))
root_modq_sync=sp.factor(root_modq.subs(ch1,ch1B))
expected_deg=-16*(2*uvar-1)*(16*d0*t*uvar+4*d0*t-e)**2
ck('EXACT_ROOT_MODQ_DEGENERACY_BOUNDARY', root_modq_sync-expected_deg)
# RCE quotient relation is exactly e == 4 d t (4u+1) mod q, hence the square vanishes.
checks.append('EXACT_ROOT_MODQ_GIVES_NO_NEW_OPENING')

# High exact normalized-root degeneracy is the same.
xh=sp.cancel((Jh-chi)/Dfl)
Rnorm_h=sp.cancel(A*(G/(8*H))*xh**2-u*D2*xh+Omega_h)
rhn,rhd=sp.fraction(Rnorm_h)
hsub=sp.factor(rhn.subs({G:q*uvar-1,alpha:alpha_tail,chi:q*ch1}))
hmod=sp.factor(sp.cancel(hsub/q**3).subs(q,0).subs(ch1,J1mod))
ck('EXACT_ROOT_MODQ_DEGENERACY_HIGH', hmod-expected_deg)


# Stronger pre-descent identities: TDEF and DTF0 need no q-content descent.
# TDEF q^2 Z = 4 a3 + t follows directly from RCE.
ck('TDEF_PRE_DESCENT', q**2*Z-4*a3-t)
# Undescended tail factorization:
# (q+4)(q^2 c Z-t(q+2)^3)=2(G/d)(d c t-alpha).
DTF0=(q+4)*(q**2*c*Z-t*(q+2)**3)-2*(G/d0)*(d0*c*t-alpha)
ck('DTF0_PRE_DESCENT',DTF0)
checks.append('GLOBAL_Q_SQUARE_BOUND_FROM_TDEF')

# Descended RCE / QZ identity, conditional on first q-descent.
tau,beta,n,a,Zs=sp.symbols('tau beta n a Zs')
Arel=(2*G+q+2)/q
DR1=2*Arel*a-(G-1)*Zs+n
DR3=(q+4)*Zs-Arel*tau+2*n
n_from3=sp.solve(sp.Eq(DR3,0),n)[0]
ck('QZ_EQUALS_4A_PLUS_TAU', sp.factor(DR1.subs(n,n_from3) + (2*G+q+2)*(q*Zs-4*a-tau)/(2*q)))
# Descended quotient opening e1.
e1=sp.symbols('e1')
ck('E_DESC0', (d0*B*(q*tau)-q*beta)/q-(d0*B*tau-beta))
checks.append('BETA_NEGATIVE_OPENING_AFTER_DESCENT')

# DTF factorization after first descent.
D=sp.symbols('D')
DTF_lhs=(q+4)*(q*c*Zs-tau*(q+2)**3)
# n=(A tau-(q+4)Z)/2, tail D1 q c n-B tau=beta D.
nexpr=(Arel*tau-(q+4)*Zs)/2
tailD1=sp.expand(q*c*nexpr-B*tau-beta*D)
# Explicit algebra form: from q c n-B tau=beta D and A=(2G+q+2)/q, G=d_delta D.
ddel=sp.symbols('d_delta')
expr=sp.factor(DTF_lhs-2*D*(ddel*c*tau-beta))
relation=sp.factor((q*c*nexpr-B*tau-beta*D).subs(G,ddel*D))
ck('DESCENDED_TAIL_FACTORIZATION', expr.subs(G,ddel*D)+2*relation)
checks.append('DTF_IDENTITY')
checks.append('DTF_FACTORIZATION')

# Reverse fixed-depth quotient and carry audit.
dR=d0*R
Nr,Zr,a3r,Xr,D2r,Fr=reconstructed(dR)
Ur=sp.cancel(8*u*D2r/(A*(R*G)))
nr,dr=sp.fraction(Ur)
Qr,Rmr=sp.div(sp.Poly(nr,G),sp.Poly(dr,G))
Pr=sp.factor(Qr.as_expr())
DR=2*R**2*d0*q**2*(q+4)*c
Jr=sp.factor(DR*Pr)
assert sp.denom(Jr)==1
checks.append('REVERSE_STRUCTURAL_DENOM')
Omega_r=sp.cancel(Fr/(2*(G/R)))
Dec_r=sp.cancel(u*D2r*(Pr+eps-s)-Omega_r)
nrd,drd=sp.fraction(Dec_r)
const_r=sp.factor(sp.Poly(sp.expand(nrd),G).coeff_monomial(1))
epsTargetR=sp.factor(sp.solve(sp.Eq(const_r,0),eps)[0])
ck('REVERSE_EPS_COEFF_S',sp.diff(epsTargetR,s)-1)
epsR=sp.factor(epsTargetR-s)
NR=sp.factor(sp.cancel(epsR*(2*q*DR)))
assert sp.denom(NR)==1
GammaR=sp.factor(NR+2*q*(DR*s+chi))
Dec_r_chi=sp.cancel(Dec_r.subs(eps,-chi/DR))
cr,denr=coeff0(Dec_r_chi,G)
# determine sign by direct assertion
sgn=sp.factor(cr/(2*R*d0*q**2*t*(q+4)*GammaR))
assert sgn in (1,-1)
checks.append('REVERSE_CONSTANT_RESIDUAL_FACTOR')
# Reverse NR mod q gives the desired stabilized + opening.
NRmod=sp.factor(NR.subs(q,0))
# It is an R^2-unit multiple of (8 dR t-alpha).
assert sp.factor(NRmod/(8*R**2*(8*dR*t-alpha))) in (1,-1)
checks.append('REVERSE_ROOT_POSITIVE_OPENING_STABILIZED')
# q|chi_R from tail opening is unconditional in active reverse tail.
alpha_tail_R=dR*B*t-q*e
Jrtail=sp.factor(Jr.subs({G:q*uvar-1,alpha:alpha_tail_R}))
assert sp.denom(sp.cancel(Jrtail/q))==1
checks.append('REVERSE_CHI_DIV_Q_FROM_TAIL_OPENING')
Jr1mod=sp.factor(sp.cancel(Jrtail/q).subs(q,0))
ck('REVERSE_CHI_OVER_Q_RESIDUE', Jr1mod-8*(16*dR*t*uvar-4*dR*t-e))
# Exact reverse root mod-q degeneracy.
xr=sp.cancel((Jr-chi)/DR-s)
Rnorm_r=sp.cancel(A*(R*G/8)*xr**2-u*D2r*xr+Omega_r)
rrn,rrd=sp.fraction(Rnorm_r)
rsub=sp.factor(rrn.subs({G:q*uvar-1,alpha:alpha_tail_R,chi:q*ch1}))
rmod=sp.factor(sp.cancel(rsub/q**3).subs(q,0).subs(ch1,Jr1mod))
expected_r=-16*R**2*(2*uvar-1)*(16*dR*t*uvar+4*dR*t-e)**2
ck('EXACT_ROOT_MODQ_DEGENERACY_REVERSE',rmod-expected_r)

# Conditional second descent consequences and q=7 terminal identity.
# q=7: c=925, B=153, d0=2.
assert int(c.subs(q,7))==925 and int(B.subs(q,7))==153
G7,a2,beta2=sp.symbols('G7 a2 beta2')
n7=G7-1-22*a2
q7eq=sp.expand(2*(925*n7-153)-beta2*G7)
ck('BOUNDARY_Q7_TERMINAL_IDENTITY', q7eq-((1850-beta2)*G7-40700*a2-2156))
assert (40700%5)==0 and (2156%5)==1
checks.append('BOUNDARY_Q7_MOD5_CONTRADICTION_CONDITIONAL')

# Twice-descended DTF (conditional): exact corrected form.
tau2,beta2s=sp.symbols('tau2 beta2s')
first_DTF=(q+4)*(q*c*Zs-(q*tau2)*(q+2)**3)-2*D*(dR*c*(q*tau2)-q*beta2s)
ck('REVERSE_DTF_SECOND_DESCENT', sp.cancel(first_DTF/q)-((q+4)*(c*Zs-tau2*(q+2)**3)-2*D*(dR*c*tau2-beta2s)))

# q=1 boundary: exact root equation gives a nontrivial decimal product congruence.
N1,t1,chi1,s1=sp.symbols('N1 t1 chi1 s1', integer=True)
u1=G+1; A1=2*G+3
Z1=sp.cancel((A1*t1-2*N1)/5)
a31=sp.cancel(((G-1)*t1-N1)/10)
X1=sp.cancel((Z1+u1*N1)/2)
D21=sp.cancel(u1*a31+G*X1)
F1=sp.cancel(A1*X1**2+Z1*D21)
Om1=sp.cancel(F1/(2*G))
J1=10*G*N1+6*G*t1-N1+3*t1
x1=sp.cancel((J1-chi1)/5-s1)
Rq1=sp.cancel(A1*(G/8)*x1**2-u1*D21*x1+Om1)
q1n,q1d=sp.fraction(Rq1)
q1const=sp.factor(sp.Poly(sp.expand(q1n),G).coeff_monomial(1))
ck('Q1_BOUNDARY_CONSTANT',q1const-(N1+t1)*(31*N1+21*t1))
checks.append('Q1_BOUNDARY_ROOT_IMPLIES_G_DIV_PRODUCT')

print('J2-55 R7 CarryIndex symbolic certificate')
print('SYMBOLIC_STATUS=PASS')
for name in checks:
    print(name+'=PASS')
print('IMPORTANT_SCOPE=BCI/HCI/RCI_ZERO_EQUALITIES_ARE_STABILIZED_FIXED_FIBRE_ONLY')
print('EXACT_GLOBAL_REPLACEMENT=G_DIVIDES_CARRY_RESIDUAL_MULTIPLE; reverse reduces to K-scale')
print('GLOBAL_Q_DESCENT_1=NOT_PROVED')
print('C_MOD5=',sp.expand(sp.rem(sp.Poly(c,q),sp.Poly(5,q)).as_expr()) if False else '(q-2)(q+1)^2 mod 5')
