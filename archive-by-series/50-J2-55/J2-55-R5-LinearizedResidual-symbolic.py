#!/usr/bin/env python3
"""Exact symbolic certificate for J2-55 R5.

Scope: Strict A1-only, Exact Resonance R=0, J=2.
No floating-point arithmetic is used.  SymPy is used only for exact polynomial
identities; inequality certificates are reduced to manifestly positive gaps.
"""
import sympy as sp

# Positive structural symbols (positivity is used only in printed inequality gaps).
u,G,K,L,q,A,D2,Omega,mu,rho,s,x = sp.symbols(
    'u G K L q A D2 Omega mu rho s x', positive=True)
Mq,t,N,E,Fnum,sigma = sp.symbols('Mq t N E Fnum sigma', positive=True)
a,b,S,Ftilde = sp.symbols('a b S Ftilde', positive=True)
Mdec = L/8
Mbig = A*Mdec
Theta = sp.symbols('Theta')

checks=[]
def ck(name, expr):
    z=sp.factor(sp.together(expr))
    assert z==0, (name,z)
    checks.append(name)

# 1. Big modulus.
ck('1_MBIG_EQUALS_A_MDEC', Mbig-A*Mdec)

# Euclidean and defect substitutions.
subs_eucl={rho:u*D2-Mbig*mu, x:mu-s}

# 3. Linearized residual.
Rscr=Mbig*x**2-u*D2*x+Omega
Theta_def=(Omega-x*rho)/Mbig
ck('3_LINEARIZED_RESIDUAL', (Rscr-Mbig*(Theta_def-s*x)).subs(u*D2,Mbig*mu+rho).subs(x,mu-s))

# 4. Theta=sx iff raw product equality; identity of the two residuals.
raw_product_residual=Omega-(mu-s)*(rho+Mbig*s)
ck('4_THETA_PRODUCT_EQUIVALENCE', (Mbig*(Theta_def-s*x)-raw_product_residual).subs(x,mu-s))

# 5. Predicted discriminant root identity.
DiscNorm=u**2*D2**2-4*Mbig*Omega
Rpred=Mbig*mu-rho-2*Mbig*s
expr5=(DiscNorm-Rpred**2 + 4*Mbig**2*(Theta_def-s*x))
expr5=expr5.subs(x,mu-s).subs(u*D2,Mbig*mu+rho)
# Need replace u^2 D2^2 by (uD2)^2 after substitution.
expr5=sp.expand(expr5).subs(u**2*D2**2,(Mbig*mu+rho)**2)
ck('5_DISC_MINUS_PREDICTED_SQUARE',expr5)

# 6. Standard discriminant scale.
H=G/2
DeltaStd=(2*u*K*D2)**2-4*A*H**2*Ftilde
expr6=DeltaStd-4*K**2*DiscNorm
expr6=expr6.subs(Ftilde,2*K*Omega).subs(G**2,K*L)
ck('6_STANDARD_DISC_SCALE',expr6)

# 7. CQLRC kernel scale.  G=S*b, K=S*a.
Psi=4*u**2*a**2*D2**2-A*b**2*Ftilde
expr7=Psi-4*a**2*DiscNorm
expr7=expr7.subs(Ftilde,2*K*Omega).subs(K,S*a).subs(G,S*b)
# Mbig=A L/8 and L=G*b/a follows G*b/a=10^ell; equivalently K*L=G^2.
# Use L = S*b**2/a after G=S*b,K=S*a.
expr7=expr7.subs(L,S*b**2/a)
ck('7_PSI_NORMALIZED_DISC_SCALE',expr7)

# 8. Under root DeltaLin=0, Psi equals predicted exact square.
# This is just 7 + 5; verify directly after imposing Euclidean/root product.
expr8=(Psi-(2*a*Rpred)**2)
expr8=expr8.subs({Ftilde:2*K*Omega,K:S*a,G:S*b,L:S*b**2/a})
expr8=expr8.subs(Omega,(mu-s)*(rho+Mbig*s)).subs(L,S*b**2/a)
expr8=expr8.subs(u*D2,Mbig*mu+rho).subs(L,S*b**2/a)
expr8=sp.expand(expr8).subs(u**2*D2**2,(Mbig*mu+rho)**2)
ck('8_PSI_PREDICTED_ROOT_UNDER_ROOT',expr8)

# 9. Outer Euclidean division from D2=E/(2Mq), rho=sigma/(8Mq).
expr9=4*u*E-A*L*Mq*mu-sigma
expr9=expr9.subs(E,2*Mq*D2).subs(sigma,8*Mq*rho).subs(u*D2,Mbig*mu+rho)
ck('9_OUTER_EUCLIDEAN_DIVISION',expr9)

# 10. Outer product from Fnum=8 K Mq^2 Omega and root product.
expr10=Fnum-K*Mq*(mu-s)*(sigma+A*L*Mq*s)
expr10=expr10.subs(Fnum,8*K*Mq**2*Omega).subs(sigma,8*Mq*rho)
expr10=expr10.subs(Omega,(mu-s)*(rho+Mbig*s))
ck('10_OUTER_EXACT_PRODUCT',expr10)

# 11. Outer Theta identity using K L=G^2.
expr11=A*G**2*Mq**2*Theta_def-(Fnum-K*Mq*x*sigma)
expr11=expr11.subs(Fnum,8*K*Mq**2*Omega).subs(sigma,8*Mq*rho).subs(G**2,K*L)
ck('11_OUTER_THETA',expr11)

# 2. Euclidean identity is definitional; verify rho substitution exactly.
ck('2_EUCLIDEAN_DEFINITION', (u*D2-Mbig*mu-rho).subs(rho,u*D2-Mbig*mu))

# 12. s/x bound.  The exact upper ratio from s<B and x>AG/10 is
# 2920 L^2 u^2/(A^2 G^4). With KL=G^2 it is
# 2920 u^2/(A^2 K^2). Compare to 730/K^2.
gap12=sp.factor(730/K**2-2920*u**2/(A**2*K**2))
gap12_A=sp.factor(gap12.subs(A,2*u+1))
assert sp.simplify(gap12_A-730*(4*u+1)/(K**2*(2*u+1)**2))==0
checks.append('12_S_OVER_X_GAP_POSITIVE')

# 13. B/Mdec bound.  After u=(G+1)/q and L=G^2/K,
# RHS-LHS is exactly 1168*u/(A*G*K)>0.
Bnd=292*L**2*u**2/(A*G**3)
ratioBM=sp.simplify(Bnd/Mdec)
RHS13=1168/(q*K)*(1+1/G)
expr13=sp.factor((RHS13-ratioBM).subs(q,(G+1)/u).subs(L,G**2/K).subs(A,2*u+1))
assert sp.simplify(expr13-1168*u/(G*K*(2*u+1)))==0
checks.append('13_B_OVER_MDEC_GAP_POSITIVE')

# 14. B/A bound: RHS-LHS positive by A^2-4u^2=4u+1.
RHS14=73*G/K**2
expr14=sp.factor((RHS14-Bnd/A).subs(L,G**2/K).subs(A,2*u+1))
assert sp.simplify(expr14-73*G*(4*u+1)/(K**2*(2*u+1)**2))==0
checks.append('14_B_OVER_A_GAP_POSITIVE')

# Additional R5 identities.
E0=Omega-mu*rho
ck('E0_ROOT_FORM', (E0-s*(Mbig*x-rho)).subs(x,mu-s).subs(Omega,(mu-s)*(rho+Mbig*s)))

# Rpred alternative form, removes mu if desired.
ck('RPRED_ALTERNATIVE', (Rpred-(u*D2-2*rho-2*Mbig*s)).subs(u*D2,Mbig*mu+rho))

# Outer DeltaLin identity.
DeltaLin=Theta_def-s*x
exprD=A*G**2*Mq**2*DeltaLin-(Fnum-K*Mq*x*(sigma+A*L*Mq*s))
exprD=exprD.subs(Fnum,8*K*Mq**2*Omega).subs(sigma,8*Mq*rho).subs(G**2,K*L)
ck('OUTER_DELTALIN',exprD)

# Zero-tail DIG3 algebra pieces.
qq=sp.symbols('qq', positive=True, integer=True)
c=qq**3+10*qq**2+12*qq+8
B=sp.expand((qq+2)*(qq**2-4*qq-4))
assert sp.expand(c-B)==12*qq**2+24*qq+16
checks.append('ZERO_TAIL_c_MINUS_B_POSITIVE')

print('J2-55 R5 symbolic exact certificate')
print('SYMBOLIC_STATUS=PASS')
for name in checks:
    print(name+'=PASS')
print('INEQUALITY_12_GAP=',gap12_A)
print('INEQUALITY_13_GAP=',expr13)
print('INEQUALITY_14_GAP=',expr14)
print('ZERO_TAIL_IDENTITY_c_minus_B=',sp.expand(c-B))
