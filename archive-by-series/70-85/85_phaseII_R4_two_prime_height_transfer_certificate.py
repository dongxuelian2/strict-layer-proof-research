#!/usr/bin/env python3
"""
Second-85 Phase-II R4 exact certificate.

Scope:
1) Rebuild the five g=5 source-adapted quadratic chord parameterizations from R3.
2) Upgrade R3's necessary 2/5 residue lists to exact PCS packets.
3) CRT-combine the exact affine packets.
4) Verify the exact radial-band boundary quadratics.
5) Prove by exact integer comparison the minimum reduced denominator in each
   PCS packet for the five representative g=5 fibres.
6) Verify the displayed near-countermodels and the displayed full-primitive
   packet survivor.
No floating-point number is used for any PASS/FAIL decision.
"""
from math import gcd, isqrt
from functools import reduce

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

EXPECTED_PACKETS = {
    (5,1,11):   (44707, 50000),
    (5,3,11):   (39227, 50000),
    (5,4,11):   (27227, 50000),
    (5,1,9091): (48227, 50000),
    (5,3,9091): (155347, 250000),
}

EXPECTED_FIRST = {
    (5,1,11):   (224277651577, 11411, 4475350),
    (5,3,11):   (5982784950483, 302729, 119418196),
    (5,4,11):   (20939904412893, 1059559, 418221116),
    (5,1,9091): (297757093, 9907159, -9549896),
    (5,3,9091): (538232869, 17795527, -11055774),
}

FULL_SURVIVOR = ((5,3,11), 6300650477551, 318813)

def vp(n,p):
    if n == 0:
        return 10**9
    n=abs(n); v=0
    while n%p == 0:
        n//=p; v+=1
    return v

def qeval(co,a,b):
    return co[0]*a*a + co[1]*a*b + co[2]*b*b

def qlin(terms):
    return tuple(sum(s*co[i] for co,s in terms) for i in range(3))

def primitive_coeff(co):
    d=reduce(gcd,[abs(x) for x in co])
    co=tuple(x//d for x in co)
    if co[0] < 0:
        co=tuple(-x for x in co)
    return co

def setup(key):
    g,k,u=key; p0=POINTS[key]
    G=10**g; K=10**k; H=G//2
    q=(G+1)//u
    assert u*q == G+1
    A=2*u+1; B=2*G+q; MM=2*K

    def phi(v):
        c,z,l=v
        w=G*H*z-u*A*c
        T=G*z+u*l
        d2=u*c+G*w
        return G*G*(B*z+A*l)**2 + 16*K*K*w*w - 16*K*K*T*d2

    def polar(x,y):
        return phi(tuple(x[i]+y[i] for i in range(3))) - phi(x) - phi(y)

    assert phi(p0) == 0
    assert (B*p0[1]+A*p0[2]) % MM == 0

    r0=(-B*pow(A,-1,MM)) % MM
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
    Lam=tuple(r0*Y[i]+MM*N[i] for i in range(3))
    return dict(
        key=key,g=g,k=k,u=u,q=q,G=G,K=K,H=H,A=A,B=B,MM=MM,r0=r0,
        phi=phi,forms=(X,Y,N,Lam),C0=C0
    )

def radial_polys(F):
    X,Y,N,Lam=F["forms"]
    G,K,H,A=F["G"],F["K"],F["H"],F["A"]
    C2=qlin([(X,A),(Lam,H)])
    # lower m-endpoint alpha is rho=10; upper endpoint beta is rho=1/10.
    alpha=primitive_coeff(qlin([(X,10*G*K),(C2,-1)]))
    beta =primitive_coeff(qlin([(C2,10),(X,-G*K)]))
    return alpha,beta

def floor_shift_root(poly,b,r,M):
    # Exact floor of b*(theta-r)/M where theta is the positive root
    # of A*x^2+B*x+C=0, A>0, C<0.
    A,B,C=poly
    D=B*B-4*A*C
    assert D > 0
    s=isqrt(D*b*b)  # floor(b*sqrt(D))
    assert s*s != D*b*b
    return (s - b*(B+2*A*r)) // (2*A*M)

def first_packet_rational(F,r,M,maxb):
    alpha,beta=radial_polys(F)
    for b in range(1,maxb+1):
        if gcd(b,M) != 1:
            continue
        lo=floor_shift_root(alpha,b,r,M)+1
        hi=floor_shift_root(beta,b,r,M)
        if lo <= hi:
            for ell in range(lo,hi+1):
                if gcd(ell,b)==1:
                    return r*b+M*ell, b, ell
    return None

def primitive_point(F,a,b):
    X,Y,N,Lam=F["forms"]
    xv,yv,nv=(qeval(co,a,b) for co in (X,Y,N))
    D=reduce(gcd,[abs(xv),abs(yv),abs(nv)])
    c=xv//D; z=yv//D; n=nv//D
    lam=F["r0"]*z+F["MM"]*n
    if c < 0:
        c,z,lam=-c,-z,-lam
    return (c,z,lam), D

def ledger(F,a,b):
    (c,z,lam),Dnorm=primitive_point(F,a,b)
    G,K,H,u,q,A,B=(F[x] for x in ("G","K","H","u","q","A","B"))
    assert c>0 and z>0 and lam>0
    num=B*z+A*lam
    assert num%(2*K)==0
    C1=num//(2*K)
    C2=A*c+H*lam
    T=G*z+u*lam
    h=q*H*z-A*c
    m=A*h-G*z
    r=H*h-u*c
    w=G*H*z-u*A*c
    d2=u*c+G*w
    assert min(C1,C2,T,h,m,r,w,d2)>0
    assert 10*C2>G*K*c and C2<10*G*K*c
    ten=(gcd(c*z*lam,10)==1 and gcd(h*m*r*w*T*d2,10)==1)
    regular=(gcd(A,d2)==1)
    commonV=(gcd(C1,u)==1 and gcd(C2,H)==1 and gcd(c,G*H)==1)
    P1=G*H*C1; P2=u*G*C2; P3=u*c; Q0=P2+d2
    prim=reduce(gcd,[P1,P2,P3,Q0])
    return dict(c=c,z=z,lam=lam,C1=C1,C2=C2,D=Dnorm*F["C0"],
                ten=ten,regular=regular,commonV=commonV,prim=prim,
                gC1u=gcd(C1,u))


def exact_pcs_residues(F,p):
    X,Y,N,Lam=F["forms"]
    e=min(vp(x,p) for x in X if x)
    mod=p**e
    reps=[(a,1) for a in range(mod)]
    reps += [(1,b) for b in range(0,mod,p)]
    necessary=[]
    exact=[]
    for a,b in reps:
        vals=[qeval(co,a,b) for co in (X,Y,N)]
        if all(v % mod == 0 for v in vals):
            necessary.append((a,b))
            vv=[vp(v,p) for v in vals]
            if vv[0] == vv[1] == min(vv):
                exact.append((a,b))
    return e,necessary,exact

def crt_pair(r2,m2,r5,m5):
    # coprime powers of 2 and 5
    return (r2 + m2*((r5-r2)*pow(m2,-1,m5) % m5)) % (m2*m5)

print("R4_EXACT_CERTIFICATE")
print("====================")
print("FLOAT_GATE_DECISIONS=0")

# Exact PCS packet upgrade, derived from the valuation equality itself.
for key in POINTS:
    F=setup(key)
    e2,n2,x2=exact_pcs_residues(F,2)
    e5,n5,x5=exact_pcs_residues(F,5)
    assert len(x2)==1 and x2[0][1]==1
    assert len(x5)==1 and x5[0][1]==1
    r2=x2[0][0]; m2=2**e2
    r5=x5[0][0]; m5=5**e5
    r=crt_pair(r2,m2,r5,m5)
    M=m2*m5
    assert (r,M)==EXPECTED_PACKETS[key]
    assert gcd(r,M)==1
    # No denominator-divisible projective branch survives full PCS.
    assert all(b==1 for a,b in x2+x5)
    print(f"PCS_LOCAL {key} : p2 e={e2} necessary={n2} exact={x2}; "
          f"p5 e={e5} necessary={n5} exact={x5}")
    print(f"PCS_PACKET {key} : a == {r} b (mod {M})")

# Exact minimum denominator in each representative packet.
for key,(ea,eb,eell) in EXPECTED_FIRST.items():
    F=setup(key)
    r,M=EXPECTED_PACKETS[key]
    got=first_packet_rational(F,r,M,eb)
    assert got == (ea,eb,eell), (key,got,(ea,eb,eell))
    L=ledger(F,ea,eb)
    assert L["ten"] and L["regular"]
    assert not L["commonV"]
    assert L["prim"] == F["u"]  # 11 or 9091 in all five first hits
    print(f"FIRST_PCS_BAND {key} : a={ea} b={eb} ell={eell} "
          f"D={L['D']} gcd(C1,u)={L['gC1u']} primitive_gcd={L['prim']}")

# Same exact PCS packet contains a genuine full-primitive survivor:
key,a,b=FULL_SURVIVOR
F=setup(key)
r,M=EXPECTED_PACKETS[key]
assert (a-r*b)%M==0
assert gcd(a,b)==1
L=ledger(F,a,b)
assert L["ten"] and L["regular"] and L["commonV"] and L["prim"]==1
print("FULL_PACKET_SURVIVOR=PASS")
print("FULL_PACKET_SURVIVOR_KEY=",key)
print("a,b=",a,b)
print("c=",L["c"])
print("C2=",L["C2"])
print("D_LAMBDA=",L["D"])

print("FULL_PRIMITIVE_PACKET_GUILLOTINE=FALSE")
print("CERTIFICATE_STATUS=PASS")
