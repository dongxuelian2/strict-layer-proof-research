#!/usr/bin/env python3
from math import gcd
from functools import reduce
import sympy as sp

print("SECOND_85_PHASEII_R5_CERTIFICATE")
print("FLOAT_GATE_DECISIONS=0")

# ------------------------------------------------------------------
# I. Symbolic source-form determinant
# ------------------------------------------------------------------
G,K,u,A,s,t = sp.symbols("G K u A s t", nonzero=True)
c,z,n = sp.symbols("c z n")
H = G/2

# Source coordinates:
# lambda = r0*z + 2K*n
# B + A*r0 = 2K*s
# t = G + u*r0
# hence A*t = 2uK*s - 1
C1 = s*z + A*n
w  = G*H*z - u*A*c
T  = t*z + 2*u*K*n
d2 = u*c + G*w
E  = sp.expand(H**2*C1**2 + w**2 - T*d2)

P = sp.Poly(E,c,z,n)
coef = {m: sp.factor(v) for m,v in P.terms()}
assert coef[(2,0,0)] == A**2*u**2
assert coef[(1,1,0)] == u*(-A*G**2 + A*G*t - t)
assert coef[(1,0,1)] == 2*K*u**2*(A*G-1)
assert coef[(0,2,0)] == G**2*(G**2-2*G*t+s**2)/4
assert coef[(0,1,1)] == G**2*(A*s-2*G*K*u)/2
assert coef[(0,0,2)] == A**2*G**2/4

S = sp.Matrix([
    [coef[(2,0,0)], coef[(1,1,0)]/2, coef[(1,0,1)]/2],
    [coef[(1,1,0)]/2, coef[(0,2,0)], coef[(0,1,1)]/2],
    [coef[(1,0,1)]/2, coef[(0,1,1)]/2, coef[(0,0,2)]],
])
N0 = 4*u**2*G**2*K**2 - (G*A+1)**2 + 2
s_sub = (A*t+1)/(2*u*K)
det_reduced = sp.factor(S.det().subs(s,s_sub))
assert sp.simplify(det_reduced + G**2*u**2*N0/16) == 0
print("SOURCE_FORM_DETERMINANT_IDENTITY=PASS")
print("det(S_E)=-G^2*u^2*N0/16")

# ------------------------------------------------------------------
# II. Generic ternary-quadric chord resultant identity
# ------------------------------------------------------------------
s11,s12,s22,s13,s23,s33 = sp.symbols("s11 s12 s22 s13 s23 s33")
p1,p2,p3,a,b = sp.symbols("p1 p2 p3 a b")
Sg = sp.Matrix([[s11,s12,s13],[s12,s22,s23],[s13,s23,s33]])
pg = sp.Matrix([p1,p2,p3])
Q = s11*a*a + 2*s12*a*b + s22*b*b
l1 = 2*(s11*p1+s12*p2+s13*p3)
l2 = 2*(s12*p1+s22*p2+s23*p3)
L = l1*a+l2*b
res = sp.factor(sp.resultant(Q,L,a)/b**2)
iso = (pg.T*Sg*pg)[0]
s33_iso = sp.solve(sp.Eq(iso,0),s33)[0]
assert sp.factor((res + 4*p3**2*Sg.det()).subs(s33,s33_iso)) == 0
print("CHORD_RESULTANT_IDENTITY=PASS")
print("Res(Q,L)=-4*p3^2*det(S) on Q(p)=0")

# ------------------------------------------------------------------
# III. Representative live g=5 fibres
# ------------------------------------------------------------------
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
PACKETS = {
    (5,1,11):(44707,50000),
    (5,3,11):(39227,50000),
    (5,4,11):(27227,50000),
    (5,1,9091):(48227,50000),
    (5,3,9091):(155347,250000),
}
FIRST = {
    (5,1,11):(224277651577,11411,80000000),
    (5,3,11):(5982784950483,302729,800000000000),
    (5,4,11):(20939904412893,1059559,80000000000000),
    (5,1,9091):(297757093,9907159,80000000),
    (5,3,9091):(538232869,17795527,4000000000000),
}

for key,p0 in POINTS.items():
    g,k,uu = key
    GG=10**g; KK=10**k; HH=GG//2
    qq=(GG+1)//uu; AA=2*uu+1; BB=2*GG+qq
    assert uu*qq == GG+1
    assert gcd(AA,10)==1
    r0=(-BB*pow(AA,-1,2*KK))%(2*KK)
    ss=(BB+AA*r0)//(2*KK)
    tt=GG+uu*r0
    assert AA*tt == 2*uu*KK*ss-1

    # Exact integral source-form coefficients.
    co = [
        uu*uu*AA*AA,
        uu*(-AA*GG*GG+AA*GG*tt-tt),
        2*KK*uu*uu*(GG*AA-1),
        GG*GG*(GG*GG-2*GG*tt+ss*ss)//4,
        GG*GG*(AA*ss-2*GG*KK*uu)//2,
        GG*GG*AA*AA//4,
    ]
    assert reduce(gcd,[abs(x) for x in co]) == 1

    NN=4*uu*uu*GG*GG*KK*KK-(GG*AA+1)**2+2
    assert NN > 0 and NN%2==1 and NN%5==1
    assert gcd(NN,uu)==1
    Csrc=GG*GG*uu*uu*NN//4

    # Old source-basis p3 for the R4 basepoint.
    p3old=(p0[2]-r0*p0[1])//(2*KK)
    # Phi_R4 = 16 K^2 E, hence:
    # det S_Phi = -256 K^6 G^2 u^2 N0
    # |Res_Phi| = 1024 K^6 G^2 u^2 N0 p3^2
    Rraw=1024*KK**6*GG**2*uu**2*NN*p3old**2
    Capraw=abs(p3old)*Rraw

    print("FIBRE", (g,k,uu,qq))
    print(" r0,s,t=",r0,ss,tt)
    print(" packet=",PACKETS[key])
    print(" first_H,D=",FIRST[key][0],FIRST[key][2])
    print(" N0=",NN)
    print(" old_p3=",p3old)
    print(" canonical_p3=1")
    print(" canonical_resultant_capacity=",Csrc)
    print(" old_raw_resultant_digits=",len(str(Rraw)))
    print(" old_raw_capacity_digits=",len(str(Capraw)))

# SNF is immediate because the source reconstruction matrix contains a 2x2 identity:
# [[1,0,0],[0,1,0],[0,r0,2K]].
print("SOURCE_RECONSTRUCTION_SNF=diag(1,1,2K)")
print("ODD_SOURCE_LATTICE_INVARIANT_FACTOR=NONE")

# Content split:
# Csrc=(G^2/4)*u^2*N0; u,N0 are ten-units.
print("CANONICAL_D_25_DIVIDES=G^2/4")
print("CANONICAL_D_ODD_DIVIDES=u^2*N0")

print("CERTIFICATE_STATUS=PASS")
