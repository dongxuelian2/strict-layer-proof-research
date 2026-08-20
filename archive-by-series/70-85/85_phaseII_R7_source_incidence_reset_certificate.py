#!/usr/bin/env python3
from math import gcd


def vp(n,p):
    n=abs(n)
    if n==0: return 10**9
    v=0
    while n%p==0:
        n//=p; v+=1
    return v


def fibre_data(g,k,u,q):
    G=10**g; K=10**k
    A=2*u+1; B=2*G+q
    assert u*q==G+1
    assert u*B-G*A==1
    r0=(-pow(A,-1,2*K)*B)%(2*K)
    assert gcd(r0,10)==1
    s0=(B+A*r0)//(2*K)
    t0=G+u*r0
    assert A*t0==2*u*K*s0-1
    D=2**min(k+1,2*g-2)*5**min(k,2*g)
    assert D==gcd(2*K,G*G//4)
    a=u*u*A*A
    b=u*(-A*G*G+A*G*t0-t0)
    Rsrc=(-b*pow(a,-1,D))%D
    Rdeep=(pow(A*A,-1,D)*(pow(u,-1,D)*G-(A*G-1)*r0))%D
    assert Rsrc==Rdeep
    # PCS-substitution saturation: coefficient of tau*z after dividing D.
    coeff_tau_z=(2*a*Rsrc+b)
    assert gcd(coeff_tau_z,10)==1
    return dict(g=g,k=k,u=u,q=q,G=G,K=K,A=A,B=B,r0=r0,s0=s0,t0=t0,D=D,Rsrc=Rsrc,
                coeff_tau_z=coeff_tau_z)

fibres=[
    (5,1,11,9091),
    (5,3,11,9091),
    (5,4,11,9091),
    (5,1,9091,11),
    (5,3,9091,11),
]

print('FIBRE_PROJECTION_CHECKS')
for f in fibres:
    d=fibre_data(*f)
    print((d['g'],d['k'],d['u'],d['q']), 'D=',d['D'],'Rsrc=',d['Rsrc'],
          'gcd(tau_z_coeff,10)=',gcd(d['coeff_tau_z'],10))

# Deepest inherited R4/R5/R6 source witness.
g,k,u,q=5,3,11,9091
d=fibre_data(g,k,u,q)
G,K,A,B,r0,s0,t0,D,R=d['G'],d['K'],d['A'],d['B'],d['r0'],d['s0'],d['t0'],d['D'],d['Rsrc']
c=2844241425759278313791310157183552723
z=209677679429991676302394167849
n=546955596371187859561484885716881905
lam=1093911419823302541803955206926647590467

assert lam==r0*z+2*K*n
assert gcd(c,z,n)==1
assert gcd(c,10)==gcd(z,10)==gcd(lam,10)==1
assert (c-R*z)%D==0

# Primitive source conic E(c,z,n).
E=(
    u*u*A*A*c*c
    +u*(-A*G*G+A*G*t0-t0)*c*z
    +2*K*u*u*(A*G-1)*c*n
    +(G*G//4)*(G*G-2*G*t0+s0*s0)*z*z
    +(G*G//2)*(A*s0-2*G*K*u)*z*n
    +(G*G*A*A//4)*n*n
)
assert E==0

C1=(B*z+A*lam)//(2*K)
C2=A*c+(G//2)*lam
w=(G*G//2)*z-u*A*c
T=G*z+u*lam
d2=u*c+G*w
assert (G*G//4)*C1*C1+w*w==T*d2

# Exact deep decimal section.
Msec=u*A*A*c+u*(A*G-1)*lam-G*z
assert Msec%(G*G//4)==0
Theta=Msec//(G*G//4)
Rsec=C1*C1-G*G*z*z-2*u*G*z*lam
assert Rsec==-u*c*Theta

# First G-adic quotient consequence.
assert (lam-A*A*c)%G==0
y=(lam-A*A*c)//G
assert (u*y+z-u*A**3*c)%G==0

# Radial band and integer common-U failure.
rho_num=C2
rho_den=G*K*c
assert 10*rho_num>rho_den and rho_num<10*rho_den
Ulo=max((G*G*K + 10*C2-1)//(10*C2), (G + 10*c-1)//(10*c), 1)
Uhi=min((G*G*K-1)//C2, (G-1)//c)
assert Ulo>Uhi

print('\nDEEPEST_WITNESS')
print('SOURCE_LATTICE=PASS')
print('PRIMITIVE_SOURCE_CONIC=PASS')
print('INTRINSIC_PCS=PASS')
print('PURE_10_POWER_G=PASS')
print('uq=G+1=PASS')
print('RADIAL_BAND=PASS')
print('POWER_OF_TEN_SECTION=PASS')
print('D=',D,'Rsrc=',R)
print('Theta=',Theta)
print('v2(Msec)=',vp(Msec,2),'v5(Msec)=',vp(Msec,5),
      'required=',(2*g-2,2*g))
print('INTEGER_COMMON_U=FAIL interval=',(Ulo,Uhi))
print('FULL_SOURCE_LIFT=FAIL (inherited first failing layer)')
