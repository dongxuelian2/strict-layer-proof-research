#!/usr/bin/env python3
"""105-R7 exact verification / finite diagnostics.

This script distinguishes theorems (symbolic identities) from finite computational evidence.
It does NOT claim global source extinction from finite scans.
"""
from math import gcd, isqrt
import sympy as sp
from sympy.ntheory.residue_ntheory import is_quad_residue, sqrt_mod

# -----------------------------------------------------------------------------
# 1. Symbolic algebra: two factor-pair formulations and their exact bridge
# -----------------------------------------------------------------------------
A,B,C,Q,P,N,W=sp.symbols('A B C Q P N W')
Splus=Q+P
Sminus=Q-P
master=A*Q-B*P-C
comp=B*Q-A*P-W
sphere=Q**2-P**2-N

assert sp.expand((A-B)*Splus+(A+B)*Sminus-2*C).subs(C,A*Q-B*P) == 0
assert sp.expand(Splus*Sminus-N).subs(N,Q**2-P**2) == 0
assert sp.expand((W+C)-(A+B)*Sminus).subs({W:B*Q-A*P,C:A*Q-B*P}) == 0
assert sp.expand((W-C)-(B-A)*Splus).subs({W:B*Q-A*P,C:A*Q-B*P}) == 0
assert sp.simplify((W**2-C**2-(B**2-A**2)*N).subs({W:B*Q-A*P,C:A*Q-B*P,N:Q**2-P**2}, simultaneous=True)) == 0

print('SYMBOLIC_FACTOR_BRIDGE=PASS')
print('R_PLUS=(A+B)*S_MINUS')
print('R_MINUS=(B-A)*S_PLUS')

# -----------------------------------------------------------------------------
# 2. Fixed-character synchronized integral control (NOT an outer S3/S4 witness)
# -----------------------------------------------------------------------------
P1,P2,P3,Q0 = 24,52,159,169
A0,B0,C0 = 168,1000,60*P2+8*P3
row_gcd=gcd(gcd(A0,B0),C0)
Ah,Bh,Ch=A0//row_gcd,B0//row_gcd,C0//row_gcd
Nh=P2*P2+P3*P3
Wh=Bh*Q0-Ah*P1
assert P1*P1+Nh==Q0*Q0
assert Ah*Q0-Bh*P1==Ch
assert Wh*Wh==Ch*Ch+(Bh*Bh-Ah*Ah)*Nh
Sp,Sm=Q0+P1,Q0-P1
assert Sp*Sm==Nh
assert (Ch-Wh)%(Ah-Bh)==0 and (Ch+Wh)%(Ah+Bh)==0
assert (Ch-Wh)//(Ah-Bh)==Sp
assert (Ch+Wh)//(Ah+Bh)==Sm
print('FIXED_CHARACTER_CONTROL=PASS')
print(f'CONTROL_PRIMITIVE_ROW={Ah},{Bh},{Ch}')
print(f'CONTROL_W={Wh};S_PLUS={Sp};S_MINUS={Sm}')

# -----------------------------------------------------------------------------
# 3. Primitive-sphere gcd counterexample to the over-strong gcd(S-,S+) in {1,2}
# -----------------------------------------------------------------------------
cp=(60,7,24,65)
p,p2,p3,q=cp
assert p*p+p2*p2+p3*p3==q*q
assert gcd(gcd(gcd(p,p2),p3),q)==1
gs=gcd(q-p,q+p)
assert gs==5
print('PRIMITIVE_SPHERE_GCD_1_OR_2_CONJECTURE=FALSE')
print(f'COUNTEREXAMPLE={cp};GCD_S={gs}')

# -----------------------------------------------------------------------------
# 4. Canonical R5C moving-modulus audit: exact necessary residue is not universal killer
# -----------------------------------------------------------------------------
print('R5C_MOVING_MODULUS_AUDIT_BEGIN')
for g in range(1,13):
    G=10**g
    a,b,c=111,1000,100*G+1
    n=100*G**4+1
    m=(b*b-a*a)*n
    mod=2*c
    residue=m%mod
    qr=bool(is_quad_residue(residue,mod))
    root=''
    if qr:
        r=sqrt_mod(residue,mod,all_roots=False)
        assert r is not None and (r*r-residue)%mod==0
        root=str(int(r))
    print(f'R5C_G={g},C={c},MOD={mod},M_RES={residue},QR={qr},ROOT={root}')

# g=4 is a single exact falsifier for universal moving-modulus obstruction.
g=4;G=10**g;c=100*G+1;n=100*G**4+1;m=(1000**2-111**2)*n;mod=2*c
assert m%mod==c and (c*c-m)%mod==0
print('R5C_G4_EXACT_QR_FALSIFIER=PASS')

# Profile-specific gcd(C,M) bound for canonical R5C.
const1=1000**2-111**2
const2=1000001
assert const1==987679
assert sp.factorint(const1)=={7:1,11:1,101:1,127:1}
assert sp.factorint(const2)=={101:1,9901:1}
for g in range(1,20):
    G=10**g;c=100*G+1;n=100*G**4+1
    assert gcd(c,n) <= const2 and const2%gcd(c,n)==0
    assert (const1*const2)%gcd(c,const1*n)==0
print('R5C_PROFILE_SPECIFIC_GCD_BOUND=PASS')

# -----------------------------------------------------------------------------
# 5. Reduced-shell exact square search. Computational evidence only.
# Fixed b1=b2=C2=C3=P3=1 source shape; full m3 digit interval for listed (g,k).
# -----------------------------------------------------------------------------
def shell_scan(g,k):
    G=10**g;K=10**k
    n3=g+k+1
    Y=10**n3
    m3=n3+g
    lo,hi=10**(m3-1),10**m3
    hits=[]
    for V in range(lo,hi):
        A0=11*Y*G+V
        B0=10*Y*G*K
        C0=V*(Y+1)
        N=V*V+1
        D0=C0*C0+(B0*B0-A0*A0)*N
        if D0<0:
            continue
        w=isqrt(D0)
        if w*w==D0:
            den=B0*B0-A0*A0
            rec=[]
            for sgn in (1,-1):
                qnum=-A0*C0+sgn*B0*w
                pnum=-B0*C0+sgn*A0*w
                if den and qnum%den==0 and pnum%den==0:
                    Q=qnum//den;P=pnum//den
                    rec.append((sgn,P,Q,P%V==0))
            hits.append((V,w,rec))
    return lo,hi,hits

for g,k in [(1,1),(1,2),(1,3),(2,1)]:
    lo,hi,hits=shell_scan(g,k)
    print(f'SHELL_SCAN_g={g},k={k},V=[{lo},{hi}),COUNT={hi-lo},SQUARE_HITS={len(hits)}')
    if hits:
        print('SHELL_HITS=',hits[:20])
print('SHELL_SCAN_STATUS=FINITE_EVIDENCE_ONLY')
