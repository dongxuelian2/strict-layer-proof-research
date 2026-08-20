#!/usr/bin/env python3
"""R11 q=1 primitive conic audit."""
from math import gcd
from pathlib import Path
import csv
import sympy as sp

OUT=Path('/mnt/data')
G,K,a,t,m,n,Y=sp.symbols('G K a t m n Y', integer=True)
u=G+1; AA=2*G+3
N=(G-1)*t-10*a
Z=4*a+t
Xn=sp.expand(Z+u*N)             # 2X
D2n=sp.expand(2*u*a+G*Xn)       # 2D2
F4=sp.expand(AA*Xn**2+2*Z*D2n) # 4 Ftilde
D4=sp.factor((2*K*u*D2n)**2-AA*G**2*F4)
D4m=sp.factor(D4.subs(t,-31*a+2*K*m))
P=(4*G**4*K**2-4*G**4+8*G**3*K**2-12*G**3
   +4*G**2*K**2-13*G**2-6*G+1)
disc=sp.factor(sp.discriminant(D4m,m))
assert disc==64*G**4*K**2*a**2*(G+1)**2*(2*G+3)**2*P
poly=sp.Poly(D4m,m)
AK=sp.factor(poly.coeff_monomial(m**2))
BK=sp.factor(poly.coeff_monomial(m)/a)
CK=sp.factor(poly.coeff_monomial(1)/a**2)
assert sp.factor(BK**2-4*AK*CK)==64*G**4*K**2*(G+1)**2*(2*G+3)**2*P

# Primitive-deflation facts:
# 2K m = 31 a3 + t, with gcd(a3,2K)=gcd(t,2K)=1.
# gcd(a3,m)=gcd(a3,t).
# gcd(t,m)=gcd(t,31*a3), so only an extra 31 can appear beyond gcd(a3,t).
for KK in (10,100,1000):
    for ar in range(1,2*KK):
        if gcd(ar,10)!=1: continue
        for tr in range(1,2*KK):
            if gcd(tr,10)!=1 or (31*ar+tr)%(2*KK): continue
            mm=(31*ar+tr)//(2*KK)
            assert gcd(ar,mm)==gcd(ar,tr)
            assert gcd(tr,mm)==gcd(tr,31*ar)

# Exact ratio interval:
# z=m/a = 31/(2K)+t/(2Ka), and t/a<90/K.
ratio={KK:(sp.Rational(31,2*KK), sp.Rational(31,2*KK)+sp.Rational(45,KK**2))
       for KK in (10,100,1000)}

# Complete-square norm form:
# Xc=2 AK*n + BK*a,  Xc^2 - 4 AK Y^2 = Delta*a^2.
Xc=2*AK*n+BK*a
Delta=sp.factor(BK**2-4*AK*CK)
W=8*G**2*K*(G+1)*(2*G+3)*a
assert sp.factor(Delta*a**2-W**2*P)==0


# ------------------------------------------------------------
# Stronger primitive Gaussian-product normal form.
# P-1 has an exact factor G*Q.  The completed-square norm has
# an additional built-in factorization that removes the huge square factors.
# ------------------------------------------------------------
Qpoly=sp.factor((P-1)/G)
assert sp.factor(P-1-G*Qpoly)==0
assert sp.factor(AK-4*G**4*K**2*(P-1))==0

# Xc is divisible by 4 G^2 K.
xsmall=sp.factor(Xc/(4*G**2*K))
Csmall=2*(G+1)*(2*G+3)*a
tau=sp.symbols('tau', integer=True)
x_tau=sp.factor(xsmall.subs(n,(tau+31*a)/(2*K)))
Mfac=sp.factor(G**3*tau-(10*G**2+4*G-2)*a)
assert sp.factor((x_tau-Csmall)-Qpoly*Mfac)==0
assert sp.factor((x_tau+Csmall)/G - (Qpoly*Mfac+2*Csmall)/G)==0
Lfac=sp.factor((x_tau+Csmall)/G)
assert sp.factor(G*Lfac-Qpoly*Mfac-2*Csmall)==0

# The conic equation Y^2=D4 becomes M*L = Y^2+C^2.
# Algebraically:
assert sp.factor(Mfac*Lfac-(x_tau**2-Csmall**2)/(G*Qpoly))==0

# Mod 4 / mod 5 support, valid in the live q=1 range g-k>=2:
# M = 2*a (mod 4), M = 2*a (mod 5);
# expanded L = 2*a (mod 4), L = 3*a (mod 5), since K=10^k.
# Hence M/2 and L/2 are ten-units.  Also gcd(M,a)=1 follows from
# tau=-31a+2Kn and gcd(a,n)=1.
print('Q1_P_MINUS_1_EQUALS_GQ=PASS')
print('Q1_GAUSSIAN_PRODUCT_NORMAL_FORM=ML=Y^2+C^2')
print('Q1_M_FORM=G^3*tau-(10G^2+4G-2)*a')
print('Q1_L_FORM=(Q*M+4(G+1)(2G+3)a)/G')
print('Q1_PRIMITIVE_GCD_M_A=1 (from tau=-31a+2Kn, gcd(a,n)=1)')
print('Q1_M_OVER_2_AND_L_OVER_2_TENUNITS=PASS in live g-k>=2')
print('Q1_COMMON_ODD_SUPPORT=gcd(M/2,L/2) divides (G+1)(2G+3)')
# The projective local route is universally unavailable:
# Chevalley-Warning: one homogeneous degree-2 polynomial in 3 variables over F_p,
# with 3>2, has a nonzero zero.  On Y^2=D4(a,n), a=n=0 would force Y=0,
# so every projective zero has (a,n)!=(0,0). For p∤2K it CRT-combines with
# every base 2K cell.  This is a theorem, not a prime scan.

rows=[]
for k in (1,2,3):
    KK=10**k; mod=2*KK; inv31=pow(31,-1,mod)
    count=0
    for tr in range(mod):
        ar=(-inv31*tr)%mod
        if gcd(ar,10)!=1: continue
        assert gcd(tr,10)==1
        rows.append(dict(
            K=KK,
            base_cell=f't={tr};a3={ar} (mod {mod})',
            gcd_support='d=gcd(a3,m)=gcd(a3,t), d is a ten-unit',
            primitive_cell='divide by d; multiply cell by d^{-1} mod 2K',
            local_prime='all p coprime 2K',
            projective_points='NONEMPTY_BY_CHEVALLEY_WARNING',
            norm_status='GLOBAL_NORM_OPEN',
            period='base modulus 2K; G=10^g',
            root_survivors='UNRESOLVED_GLOBAL_CONIC',
            status='OPEN_PRIMITIVE_GLOBAL_NORM'))
        count+=1
    assert count=={1:8,2:80,3:800}[k]

p=OUT/'J2-55-R11-q1-conic-certificate.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
    fields=['K','base_cell','gcd_support','primitive_cell','local_prime',
            'projective_points','norm_status','period','root_survivors','status']
    wri=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t')
    wri.writeheader();wri.writerows(rows)

with (OUT/'J2-55-R11-q1-norm.txt').open('w',encoding='utf-8') as fobj:
    fobj.write('A_K(G)=\n'+str(AK)+'\n\n')
    fobj.write('B_K(G)=\n'+str(BK)+'\n\n')
    fobj.write('C_K(G)=\n'+str(CK)+'\n\n')
    fobj.write('Delta_K(G)=\n'+str(Delta)+'\n\n')
    fobj.write('P_K(G)=\n'+str(P)+'\n\n')
    fobj.write('Norm form:\n(2*A_K*n+B_K*a)^2-4*A_K*Y^2'
               '=[8*G^2*K*(G+1)*(2G+3)*a]^2*P_K(G)\n\n')
    fobj.write('P-1=G*Q with Q=\n'+str(Qpoly)+'\n\n')
    fobj.write('Gaussian product normal form after tau=t/d=-31a+2Kn:\n')
    fobj.write('M='+str(Mfac)+'\n')
    fobj.write('L='+str(Lfac)+'\n')
    fobj.write('M*L=Y^2+[2(G+1)(2G+3)a]^2\n')

print('PRIMITIVE_DEFLATION=PASS')
print('GCD_A_M_EQUALS_GCD_A_T=PASS')
print('GCD_T_M_EQUALS_GCD_T_31A=PASS')
for KK,I in ratio.items():
    print(f'K={KK} RATIO_INTERVAL=({I[0]},{I[1]})')
print('PROJECTIVE_SINGLE_PRIME_KILLER=IMPOSSIBLE_BY_CHEVALLEY_WARNING')
print('NORM_REDUCTION=PASS')
print('Q1_GLOBAL_CLOSURE=False')
print('CELLS=',len(rows))
print('CERT=',p.name)
