#!/usr/bin/env python3
"""
Exact finite certificate for Second-85 Phase-II R3.

Responsibilities:
1) verify five g=5 source-lattice isotropic basepoints;
2) build source-adapted chord parameterizations;
3) exact scan reduced parameters |a|,|b|<=300 for positive decade-band rays;
4) exact necessary 2/5 primitive-content residue packets.

No floating point is used for PASS/FAIL decisions.
"""
from math import gcd
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

def vp(n,p):
    if n == 0:
        return 10**9
    n=abs(n); v=0
    while n%p==0:
        n//=p; v+=1
    return v

def setup(g,k,u,p0):
    G=10**g; K=10**k; H=G//2
    q=(G+1)//u
    assert u*q==G+1
    A=2*u+1; B=2*G+q; M=2*K

    def phi(v):
        c,z,l=v
        w=G*H*z-u*A*c
        T=G*z+u*l
        d2=u*c+G*w
        return (
            G*G*(B*z+A*l)**2
            +16*K*K*w*w
            -16*K*K*T*d2
        )

    def polar(x,y):
        return phi(tuple(x[i]+y[i] for i in range(3))) - phi(x)-phi(y)

    assert phi(p0)==0
    assert (B*p0[1]+A*p0[2])%M==0

    r0=(-B*pow(A,-1,M))%M
    assert gcd(r0,10)==1
    assert (p0[2]-r0*p0[1])%M==0
    p3=(p0[2]-r0*p0[1])//M
    assert p3!=0

    e1=(1,0,0)
    e2=(0,1,r0)

    q11=phi(e1)
    q22=phi(e2)
    q12=polar(e1,e2)
    l1=polar(p0,e1)
    l2=polar(p0,e2)

    # R(a,b)=Phi(y)p-B(p,y)y with y=a e1+b e2.
    coeffs=[]
    for j in range(3):
        coeffs.append((
            q11*p0[j]-l1*e1[j],
            q12*p0[j]-(l1*e2[j]+l2*e1[j]),
            q22*p0[j]-l2*e2[j],
        ))

    def ev(co,a,b):
        return co[0]*a*a+co[1]*a*b+co[2]*b*b

    # regression at several parameters
    for a,b in [(1,0),(0,1),(1,1),(2,3),(-2,3)]:
        v=tuple(ev(co,a,b) for co in coeffs)
        assert phi(v)==0
        assert (B*v[1]+A*v[2])%M==0

    return {
        "g":g,"k":k,"u":u,"q":q,"G":G,"K":K,"H":H,
        "A":A,"B":B,"M":M,"r0":r0,"phi":phi,
        "coeffs":coeffs,"ev":ev,
    }

def source_forms(F):
    X,Y,L=F["coeffs"]
    M=F["M"]; r0=F["r0"]
    N=tuple((L[i]-r0*Y[i])//M for i in range(3))
    C0=reduce(gcd,[abs(x) for co in (X,Y,N) for x in co])
    X=tuple(x//C0 for x in X)
    Y=tuple(x//C0 for x in Y)
    N=tuple(x//C0 for x in N)
    return X,Y,N,C0

def primitive_point(F,a,b):
    ev=F["ev"]
    c,z,l=(ev(co,a,b) for co in F["coeffs"])
    n=(l-F["r0"]*z)//F["M"]
    D=reduce(gcd,(abs(c),abs(z),abs(n)))
    assert D>0
    v=(c//D,z//D,l//D)
    if v[0]<0:
        v=tuple(-x for x in v)
    return v,D

def positive_band(F,v):
    c,z,l=v
    if min(v)<=0:
        return False
    G,K,H,u,q,A,B=(
        F["G"],F["K"],F["H"],F["u"],F["q"],F["A"],F["B"]
    )
    n=B*z+A*l
    if n%(2*K):
        return False
    C1=n//(2*K)
    C2=A*c+H*l
    T=G*z+u*l
    h=q*H*z-A*c
    m=A*h-G*z
    r=H*h-u*c
    w=G*H*z-u*A*c
    d2=u*c+G*w
    if min(C1,C2,T,h,m,r,w,d2)<=0:
        return False
    # 1/10 < rho=C2/(GKc) < 10
    return (10*C2>G*K*c) and (C2<10*G*K*c)

def necessary_residues(F,p):
    X,Y,N,C0=source_forms(F)
    e=min(vp(x,p) for x in X if x)
    mod=p**e
    reps=[(a,1) for a in range(mod)]
    reps += [(1,b) for b in range(0,mod,p)]
    sols=[]
    for a,b in reps:
        vals=[F["ev"](co,a,b) for co in (X,Y,N)]
        if all(v%mod==0 for v in vals):
            sols.append((a,b))
    return e,sols

def scan(F,B=300):
    count=0
    for b in range(0,B+1):
        for a in range(-B,B+1):
            if a==0 and b==0:
                continue
            if gcd(abs(a),abs(b))!=1:
                continue
            # quotient (a,b) ~ (-a,-b)
            if b==0 and a!=1:
                continue
            v,D=primitive_point(F,a,b)
            assert F["phi"](v)==0
            if positive_band(F,v):
                count+=1
    return count

print("R3_EXACT_CERTIFICATE")
print("====================")
print("FLOAT_GATE_DECISIONS=0")

for key,p0 in POINTS.items():
    F=setup(*key,p0)
    band=scan(F,300)
    e2,r2=necessary_residues(F,2)
    e5,r5=necessary_residues(F,5)
    g,k,u=key
    print()
    print(f"FIBRE=(g={g},k={k},u={u},q={F['q']})")
    print(f"r0={F['r0']}")
    print("ISOTROPIC_BASEPOINT=PASS")
    print("SOURCE_ADAPTED_PARAMETERIZATION=PASS")
    print(f"BAND_POSITIVE_SMALL_PARAMS_B300={band}")
    print(f"V2_X_COEFF_MIN={e2}")
    print(f"NECESSARY_MOD_2^{e2}_SLOPES={r2}")
    print(f"V5_X_COEFF_MIN={e5}")
    print(f"NECESSARY_MOD_5^{e5}_SLOPES={r5}")

print()
print("CERTIFICATE_STATUS=PASS")
print("FINITE_SCAN_ONLY=TRUE")
print("UNIFORM_HEIGHT_THEOREM_NOT_CLAIMED=TRUE")
