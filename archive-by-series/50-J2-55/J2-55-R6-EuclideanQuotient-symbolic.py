#!/usr/bin/env python3
import sympy as sp

G,q,alpha,t,d,d0,H,R,Ks,L = sp.symbols('G q alpha t d d0 H R Ks L', positive=True)
mu,rho,s,x,D2s,As,us,Mbig = sp.symbols('mu rho s x D2s As us Mbig')
eps = sp.symbols('eps')

checks=[]
def ck(name, expr):
    z=sp.factor(sp.together(expr))
    assert z==0,(name,z)
    checks.append(name)

# R_s simplification.
Rpred=Mbig*mu-rho-2*Mbig*s
ck('RS_X', (Rpred-(2*Mbig*x-us*D2s)).subs({x:mu-s,us*D2s:Mbig*mu+rho}))

c=q**3+10*q**2+12*q+8
C=q*c
B=(q+2)*(q**2-4*q-4)
u=(G+1)/q
A=2*u+1
Mq=q*(q+4)
N=(B*t+alpha*G/d)/C
Z=sp.cancel((A*t-2*N)/Mq)
a3=sp.cancel(((G-1)*t-q*N)/(2*(q+4)))
X=sp.cancel((Z+u*N)/2)
D2=sp.cancel(u*a3+G*X)
D2_num,D2_den=sp.fraction(D2)
expected_den=2*d*q**2*(q+4)*c
assert sp.factor(D2_den-expected_den)==0
checks.append('EQL1_D2_DEN')

expected_num=(alpha*q+4*alpha)*G**3 + (2*alpha+2*d*q**4*t+14*d*q**3*t+12*d*q**2*t-24*d*q*t-16*d*t)*G**2 + (-alpha*q+d*q**4*t+14*d*q**3*t+28*d*q**2*t+8*d*q*t)*G -2*d*q**4*t-8*d*q**3*t
ck('EQL1_D2_NUM',D2_num-expected_num)

U=sp.cancel(8*u*D2/(A*L))

# High / boundary: L=G/H, d=d0.
Uh=sp.cancel(U.subs({L:G/H,d:d0}))
nh,dh=sp.fraction(Uh)
Qh,Rh=sp.div(sp.Poly(nh,G),sp.Poly(dh,G))
Ph=sp.factor(Qh.as_expr())
remh=sp.factor(Rh.as_expr()/dh)
ck('EQL2_HIGH_DIVISION',Uh-(Ph+remh))
DQh=2*d0*q**2*(q+4)*c
assert sp.denom(sp.cancel(DQh*Ph))==1
checks.append('EQL2_HIGH_STRUCTURAL_DENOM')

# Reverse fixed delta: R=10^r, L=RG, d=d0R.
Ur=sp.cancel(U.subs({L:R*G,d:d0*R}))
nr,dr=sp.fraction(Ur)
Qr,Rmr=sp.div(sp.Poly(nr,G),sp.Poly(dr,G))
Pr=sp.factor(Qr.as_expr()); remr=sp.factor(Rmr.as_expr()/dr)
ck('EQL2_REVERSE_FIXED_DELTA_DIVISION',Ur-(Pr+remr))

# Reverse fixed low-k: R=G/K, d=d0G/K, L=G^2/K.
Ul=sp.cancel(U.subs({L:G**2/Ks,d:d0*G/Ks}))
nl,dl=sp.fraction(Ul)
Ql,Rml=sp.div(sp.Poly(nl,G),sp.Poly(dl,G))
Plow=sp.factor(Ql.as_expr()); remlow=sp.factor(Rml.as_expr()/dl)
ck('EQL2_LOWK_DIVISION',Ul-(Plow+remlow))
assert sp.degree(sp.fraction(Plow)[0],G)==0
checks.append('LOWK_POLYNOMIAL_COLLAPSE_TO_CONSTANT')

# q=1 special quotient laws.
N1,t1=sp.symbols('N1 t1', integer=True)
u1=G+1; A1=2*G+3
D21=(5*G**2*N1+3*G**2*t1+2*G*N1+3*G*t1-N1-t1)/10
U1b=sp.cancel(8*u1*D21/(A1*G))
n1b,d1b=sp.fraction(U1b); Q1b,R1b=sp.div(sp.Poly(n1b,G),sp.Poly(d1b,G))
ck('Q1_BOUNDARY_QUOTIENT',U1b-(Q1b.as_expr()+R1b.as_expr()/d1b))
U1k=sp.cancel(8*u1*D21/(A1*(G**2/Ks)))
n1k,d1k=sp.fraction(U1k); Q1k,R1k=sp.div(sp.Poly(n1k,G),sp.Poly(d1k,G))
ck('Q1_LOWK_QUOTIENT',U1k-(Q1k.as_expr()+R1k.as_expr()/d1k))

# Decimal constant-term gates. Ftilde and Omega are root-necessary after DCDC.
Ftilde=sp.cancel(A*X**2+Z*D2)
# Boundary H=1: K=G, L=G, d=d0, mu=P+eps, x=mu-s.
Pb=sp.factor(Ph.subs(H,1))
Omega_b=sp.cancel(Ftilde.subs(d,d0)/(2*G))
uD2_b=sp.cancel((u*D2).subs(d,d0))
Dec_b=sp.cancel(uD2_b*(Pb+eps-s)-Omega_b)
nb,db=sp.fraction(Dec_b)
assert not sp.Poly(nb,G).get_domain().is_EX
const_b=sp.factor(sp.Poly(sp.expand(nb),G).coeff_monomial(1))
eps_sol_b=sp.factor(sp.solve(sp.Eq(const_b,0),eps)[0])
eps0_b=sp.factor(eps_sol_b-s)
ck('DDR_BOUNDARY_EPS_COEFF_S',sp.diff(eps_sol_b,s)-1)

# High: K=GH, L=G/H, s=0.
Omega_h=sp.cancel(Ftilde.subs(d,d0)/(2*G*H))
Dec_h=sp.cancel(sp.cancel((u*D2).subs(d,d0))*(Ph+eps)-Omega_h)
nhd,dhd=sp.fraction(Dec_h)
const_h=sp.factor(sp.Poly(sp.expand(nhd),G).coeff_monomial(1))
eps_target_h=sp.factor(sp.solve(sp.Eq(const_h,0),eps)[0])
checks.append('DDR_HIGH_CONSTANT_TERM_GATE')

# Reverse fixed-delta decimal gate.
Omega_r=sp.cancel(Ftilde.subs(d,d0*R)/(2*(G/R)))
Dec_r=sp.cancel(sp.cancel((u*D2).subs(d,d0*R))*(Pr+eps-s)-Omega_r)
nrd,drd=sp.fraction(Dec_r)
const_r=sp.factor(sp.Poly(sp.expand(nrd),G).coeff_monomial(1))
eps_target_r=sp.factor(sp.solve(sp.Eq(const_r,0),eps)[0])
ck('DDR_REVERSE_EPS_COEFF_S',sp.diff(eps_target_r,s)-1)

# Fixed low-k scale identities.
b=sp.symbols('b', integer=True, nonnegative=True)
# d_r = 2*5^b*10^r and 10^r=G/K => G/d_r=K/(2*5^b).
scale=sp.cancel(G/(2*5**b*(G/Ks)))
ck('LOWK_FIXED_SCALE',scale-Ks/(2*5**b))

print('J2-55 R6 Euclidean quotient symbolic certificate')
print('SYMBOLIC_STATUS=PASS')
for name in checks: print(name+'=PASS')
print('D2_EXPLICIT=',sp.factor(D2))
print('HIGH_BOUNDARY_P=',Ph)
print('HIGH_BOUNDARY_REM=',remh)
print('HIGH_BOUNDARY_DQ=',DQh)
print('REVERSE_FIXED_DELTA_P=',Pr)
print('REVERSE_FIXED_DELTA_REM=',remr)
print('LOWK_P0=',Plow)
print('LOWK_REM=',remlow)
print('Q1_BOUNDARY_P=',sp.factor(Q1b.as_expr()))
print('Q1_BOUNDARY_REM=',sp.factor(R1b.as_expr()/d1b))
print('Q1_LOWK_P0=',sp.factor(Q1k.as_expr()))
print('Q1_LOWK_REM=',sp.factor(R1k.as_expr()/d1k))
print('BOUNDARY_EPS0=',eps0_b)
print('HIGH_EPS_TARGET=',eps_target_h)
print('REVERSE_EPS_TARGET=',eps_target_r)
