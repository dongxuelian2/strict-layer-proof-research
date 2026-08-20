#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from functools import reduce

# First live audited outer base.
g,k,u=4,1,73
G,K=10**g,10**k
H=G//2
q=(G+1)//u
A=2*u+1
B=2*G+q
V=u*G*H

# R1 isotropic basepoint and the R2 targeted chord direction.
p0=(44166648285459361797000000,
    9530621959721527629285,
    84945551173868016406925)
y=(9,75934,2036559106)
expected=(55572391133361773812119871611530969901,
          18294059737282238636057102641763401,
          169133142022529638483244734153511450709)

def phi(v, K0=K):
    c,z,lam=v
    w=G*H*z-u*A*c
    T=G*z+u*lam
    d2=u*c+G*w
    return G*G*(B*z+A*lam)**2+16*K0*K0*w*w-16*K0*K0*T*d2

def polar(x,y,K0=K):
    return phi(tuple(x[i]+y[i] for i in range(3)),K0)-phi(x,K0)-phi(y,K0)

def ceil_div(a,b):
    return (a+b-1)//b

def reconstruct(v,K0=K):
    c,z,lam=v
    n=B*z+A*lam
    assert n%(2*K0)==0
    C1=n//(2*K0)
    C2=A*c+H*lam
    T=G*z+u*lam
    h=q*H*z-A*c
    m=A*h-G*z
    r=H*h-u*c
    w=G*H*z-u*A*c
    d2=u*c+G*w
    P1=G*H*C1; P2=u*G*C2; P3=u*c; Q0=P2+d2
    return locals()

def verify_ratio_band_witness():
    assert u*q==G+1
    assert phi(p0)==0
    assert (B*y[1]+A*y[2])%(2*K)==0
    py=phi(y); bpy=polar(p0,y)
    raw=tuple(py*p0[i]-bpy*y[i] for i in range(3))
    d=reduce(gcd,map(abs,raw))
    assert d==2920000
    P=tuple(x//d for x in raw)
    if P[0]<0: P=tuple(-x for x in P)
    assert P==expected
    assert phi(P)==0
    R=reconstruct(P)
    c,z,lam=P
    for key in ('C1','C2','T','h','m','r','w','d2'):
        assert R[key]>0
    assert gcd(c*z*lam,10)==1
    assert gcd(R['h']*R['m']*R['r']*R['w']*R['T']*R['d2'],10)==1
    assert gcd(A,R['d2'])==1
    assert gcd(R['C1'],u)==1
    assert gcd(R['C2'],H)==1
    assert gcd(c,G*H)==1
    assert reduce(gcd,[R['P1'],R['P2'],R['P3'],R['Q0']])==1
    assert gcd(V,R['P1'])==G*H
    assert gcd(V,R['P2'])==u*G
    assert gcd(V,R['P3'])==u
    Ash=K*G**3*R['C1']+G*R['C2']+c
    Bword=u*G**3+H*G**2+G*H
    assert V*Ash==R['Q0']*Bword
    # root -> square witness
    Y0=abs(A*H*H*R['C1']-u*K*R['d2'])
    Z=4*Y0
    W=G*G*z-2*u*A*c
    D=G*W+2*u*c
    Q=4*u*u*K*K*D*D-A*G*G*(A*W*W+2*z*D)
    assert Q==Z*Z
    rho=Fraction(R['C2'],G*K*c)
    assert Fraction(1,10)<rho<10
    I2=(Fraction(G*G*K,10*R['C2']),Fraction(G*G*K,R['C2']))
    I3=(Fraction(G,10*c),Fraction(G,c))
    assert max(I2[0],I3[0])<min(I2[1],I3[1])
    # Yet the witness is killed already by absolute oversize.
    assert c>=G and R['C2']>=G*G*K
    assert min(I2[1],I3[1])<1
    print('RATIO_BAND_WITNESS=PASS')
    print('CHORD_PHI_Y=',py)
    print('CHORD_POLAR=',bpy)
    print('CHORD_RAW_GCD=',d)
    print('c=',c); print('z=',z); print('lambda=',lam)
    for key in ('C1','C2','T','h','m','r','w','d2'):
        print(key+'=',R[key])
    print('rho=',rho)
    print('rho_decimal=',float(rho))
    print('SQUARE_Z=',Z)
    print('FULL_PRIMITIVE_GCD=1')
    print('REAL_INTERVAL_OVERLAP=PASS')
    print('ABSOLUTE_OVERSIZE=PASS')
    print('FIRST_SOURCE_FAILURE=ABSOLUTE_RADIAL_SCALE')

# Exact fixed-base Level-I guillotine audit.
# In the g=4 audited central regular scope, ell=2g-k>=6 gives k=1,2.
# u=137 is excluded by gcd(2u+1,10)>1, while u=1 or q=1 are outside the live q,u>1 scope.
def root_poly(k0,c,z,lam):
    # H^2*C1^2+w^2-T*d2, expanded exactly for this base.
    if k0==1:
        return (115154361*c*c + 7833624671*c*lam - 730000*c*z
                +1350562500*lam*lam -36129982625000*lam*z
                -2474656326937500*z*z)
    if k0==2:
        return (115154361*c*c + 7833624671*c*lam - 730000*c*z
                +13505625*lam*lam -36496299826250*lam*z
                -2499746563269375*z*z)
    raise ValueError

def fixed_base_level1_audit(k0):
    K0=10**k0
    lmax=(G*G*K0-1-A)//H  # safe rectangle, attained at c=1
    Z=10 if k0==1 else 3
    # -root_poly(Z,c,lambda) is separately concave in c and lambda;
    # hence its minimum on the rectangle occurs at a corner.
    corners=[-root_poly(k0,c,Z,l) for c in (1,G-1) for l in (1,lmax)]
    assert min(corners)>0
    zmax=Z-1
    tested=0; sqdisc=0; roots=[]
    # Solve the integer quadratic in lambda for every remaining (c,z).
    # These coefficients come directly from root_poly.
    if k0==1:
        aa=1350562500; blz=36129982625000; z2=2474656326937500
    else:
        aa=13505625; blz=36496299826250; z2=2499746563269375
    for c in range(1,G):
        for z in range(1,zmax+1):
            tested+=1
            bb=7833624671*c-blz*z
            cc=115154361*c*c-730000*c*z-z2*z*z
            disc=bb*bb-4*aa*cc
            if disc<0: continue
            s=isqrt(disc)
            if s*s!=disc: continue
            sqdisc+=1
            for num in (-bb+s,-bb-s):
                den=2*aa
                if num>0 and num%den==0:
                    lam=num//den
                    if A*c+H*lam<G*G*K0:
                        roots.append((c,z,lam))
    assert sqdisc==0 and roots==[]
    print(f'FIXED_BASE_K{k0}_LEVEL1_AUDIT=PASS')
    print('lambda_rectangle_max=',lmax)
    print('z_strict_upper=',Z)
    print('corner_margin_min=',min(corners))
    print('cells_tested=',tested)
    print('square_discriminants=',sqdisc)
    print('level1_countermodels=0')

if __name__=='__main__':
    verify_ratio_band_witness()
    fixed_base_level1_audit(1)
    fixed_base_level1_audit(2)
    print('CERTIFICATE_STATUS=PASS')
