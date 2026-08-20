#!/usr/bin/env python3
from math import gcd, isqrt
from functools import reduce
from fractions import Fraction
import sympy as sp

# ------------------------------------------------------------
# R6 exact certificate
# ------------------------------------------------------------

POINTS = {
    (5,1,11): (
        1491459664733466585956240803634050000,
        75467853474355231420281803580,
        -686071388003955444976305309500000,
    ),
    (5,3,11): (
        13181522546463675594173650000,
        666984812505721578000,
        -6063494450950787414300000,
    ),
    (5,4,11): (
        9214727133067217111520972650000,
        466265117663257878240000,
        -4238773594884971124185500000,
    ),
    (5,1,9091): (
        2652710889697407681836610881735456320850000,
        87699498978743438609861631221925832864020,
        -964684841823690106852729032282709382700000,
    ),
    (5,3,9091): (
        103795578925497542415930652290517454210000,
        3431516152362614455194820774241073138000,
        -37746300106092409262517254288837766060000,
    ),
}

OLD_PACKETS = {
    (5,1,11):   (44707, 50000),
    (5,3,11):   (39227, 50000),
    (5,4,11):   (27227, 50000),
    (5,1,9091): (48227, 50000),
    (5,3,9091): (155347, 250000),
}

FIRST = {
    (5,1,11):   (224277651577, 11411),
    (5,3,11):   (5982784950483, 302729),
    (5,4,11):   (20939904412893, 1059559),
    (5,1,9091): (297757093, 9907159),
    (5,3,9091): (538232869, 17795527),
}

FULL_SURVIVOR = ((5,3,11), 6300650477551, 318813)

def qeval(co,a,b):
    return co[0]*a*a + co[1]*a*b + co[2]*b*b

def setup_old(key):
    g,k,u=key
    p0=POINTS[key]
    G=10**g; K=10**k; H=G//2
    q=(G+1)//u
    A=2*u+1; B=2*G+q; MM=2*K
    assert u*q == G+1
    def phi(v):
        c,z,l=v
        w=G*H*z-u*A*c
        T=G*z+u*l
        d2=u*c+G*w
        return G*G*(B*z+A*l)**2 + 16*K*K*w*w - 16*K*K*T*d2
    def polar(x,y):
        return phi(tuple(x[i]+y[i] for i in range(3))) - phi(x) - phi(y)
    assert phi(p0)==0
    r0=(-B*pow(A,-1,MM))%MM
    assert gcd(r0,10)==1
    e1=(1,0,0); e2=(0,1,r0)
    q11=phi(e1); q22=phi(e2); q12=polar(e1,e2)
    l1=polar(p0,e1); l2=polar(p0,e2)
    coeffs=[]
    for j in range(3):
        coeffs.append((
            q11*p0[j]-l1*e1[j],
            q12*p0[j]-(l1*e2[j]+l2*e1[j]),
            q22*p0[j]-l2*e2[j],
        ))
    X,Y,L=coeffs
    N=tuple((L[i]-r0*Y[i])//MM for i in range(3))
    C0=reduce(gcd,[abs(x) for co in (X,Y,N) for x in co])
    X=tuple(x//C0 for x in X)
    Y=tuple(x//C0 for x in Y)
    N=tuple(x//C0 for x in N)
    return dict(g=g,k=k,u=u,q=q,G=G,K=K,H=H,A=A,B=B,MM=MM,r0=r0,
                forms=(X,Y,N),C0=C0)

def primitive_from_old(key,a,b):
    F=setup_old(key)
    X,Y,N=F["forms"]
    vals=[qeval(co,a,b) for co in (X,Y,N)]
    D=reduce(gcd,[abs(v) for v in vals])
    c,z,n=[v//D for v in vals]
    if c<0:
        c,z,n=-c,-z,-n
    lam=F["r0"]*z+F["MM"]*n
    C2=F["A"]*c+F["H"]*lam
    Hproj=max(abs(c),abs(z),abs(n))
    Hrad=max(Fraction(c,F["G"]), Fraction(C2,F["G"]**2*F["K"]))
    return dict(c=c,z=z,n=n,lam=lam,C2=C2,Hproj=Hproj,Hrad=Hrad,
                Draw=D*F["C0"])

def source_data(g,k,u):
    G=10**g; K=10**k; H=G//2
    q=(G+1)//u
    A=2*u+1; B=2*G+q; M=2*K
    r0=(-B*pow(A,-1,M))%M
    s0=(B+A*r0)//M
    t0=G+u*r0
    assert A*t0 == 2*u*K*s0-1
    co=dict(
        cc=u*u*A*A,
        cz=u*(-A*G*G+A*G*t0-t0),
        cn=2*K*u*u*(A*G-1),
        zz=G*G*(G*G-2*G*t0+s0*s0)//4,
        zn=G*G*(A*s0-2*G*K*u)//2,
        nn=G*G*A*A//4,
    )
    return dict(g=g,k=k,u=u,q=q,G=G,K=K,H=H,A=A,B=B,M=M,
                r0=r0,s0=s0,t0=t0,co=co)

def intrinsic_packet(g,k,u):
    F=source_data(g,k,u)
    G,K,u,A=F["G"],F["K"],F["u"],F["A"]
    mp2=min(k+1,2*g-2)
    mp5=min(k,2*g)
    D=(2**mp2)*(5**mp5)
    cc=F["co"]["cc"]; cz=F["co"]["cz"]
    assert gcd(cc,D)==1
    R=(-cz*pow(cc,-1,D))%D
    # All n^2, zn, z^2 and cn terms vanish modulo D.
    assert F["co"]["cn"]%D==0
    assert F["co"]["zz"]%D==0
    assert F["co"]["zn"]%D==0
    assert F["co"]["nn"]%D==0
    # cc and cz are decimal units.
    assert gcd(cc,10)==1 and gcd(cz,10)==1
    return D,R

# I. symbolic physical-height baseline identity
G,K,u,A,B,t,s=sp.symbols("G K u A B t s", nonzero=True)
H=G/2
C1=(B*s+A*t)/(2*K)
w=G*H*s-u*A
T=G*s+u*t
d2=u+G*w
raw=sp.expand((H**2*C1**2+w**2-T*d2)*16*K**2/G**2)
P=sp.Poly(raw,s)
aa,bb,cc=P.all_coeffs()
assert sp.factor(aa-(B**2-4*G**2*K**2))==0
assert sp.factor(bb-(2*A*B*t-8*G*K**2*u*t-16*K**2*u/G))==0
assert sp.factor(cc-(A**2*t**2+16*A**2*K**2*u**2/G**2
                     +16*A*K**2*t*u**2/G-16*K**2*t*u**2/G**2))==0
print("SOURCE_PHYSICAL_BASELINE_POLYNOMIAL=PASS")

# II. exact intrinsic PCS packet on the five representative fibres
for key in POINTS:
    D,R=intrinsic_packet(*key)
    oldr,oldM=OLD_PACKETS[key]
    print("INTRINSIC_PACKET", key, "c ==",R,"z (mod",D,")",
          "OLD_CHORD_MODULUS=",oldM)

# III. exact deepest survivor reconstruction
key,a,b=FULL_SURVIVOR
S=primitive_from_old(key,a,b)
assert S["c"]==2844241425759278313791310157183552723
assert S["z"]==209677679429991676302394167849
assert S["n"]==546955596371187859561484885716881905
assert S["lam"]==1093911419823302541803955206926647590467
assert S["C2"]==54695636408717919553598977546465994745062629
assert S["Hproj"]==S["c"]
assert S["Hrad"]==Fraction(S["c"],100000)
print("DEEPEST_SURVIVOR_INTRINSIC_RECONSTRUCTION=PASS")
print("DEEPEST_H_P2=",S["Hproj"])
print("DEEPEST_H_RAD=",S["Hrad"])

# IV. exact finite intrinsic-low search H_P2 <= 2000
def low_search(key,Hmax=2000):
    F=source_data(*key)
    co=F["co"]; an=co["nn"]
    D,R=intrinsic_packet(*key)
    found=[]
    checked=0
    for z in range(1,Hmax+1):
        if gcd(z,10)!=1:
            continue
        c0=(R*z)%D
        if c0==0:
            c0=D
        for c in range(c0,Hmax+1,D):
            if gcd(c,10)!=1:
                continue
            checked += 1
            bn=co["cn"]*c+co["zn"]*z
            cn0=co["cc"]*c*c+co["cz"]*c*z+co["zz"]*z*z
            disc=bn*bn-4*an*cn0
            if disc<0:
                continue
            rr=isqrt(disc)
            if rr*rr!=disc:
                continue
            for num in (-bn+rr,-bn-rr):
                den=2*an
                if num%den:
                    continue
                n=num//den
                if abs(n)>Hmax:
                    continue
                if gcd(gcd(c,z),abs(n))!=1:
                    continue
                lam=F["r0"]*z+F["M"]*n
                if lam<=0:
                    continue
                C2=F["A"]*c+F["H"]*lam
                if not (10*C2>F["G"]*F["K"]*c and C2<10*F["G"]*F["K"]*c):
                    continue
                found.append((c,z,n))
    return checked,found

for key in POINTS:
    checked,found=low_search(key,2000)
    assert not found
    print("INTRINSIC_LOW_SEARCH",key,"H_P2<=2000","checked=",checked,"survivors=0")

print("FLOAT_GATE_DECISIONS=0")
print("CERTIFICATE_STATUS=PASS")
