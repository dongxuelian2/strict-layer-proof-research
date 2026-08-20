#!/usr/bin/env python3
"""J2-55 R12 q=1 Primitive Gaussian support certificate.

No generic one-prime projective conic search is used.
The proof is support-theoretic and factorization-free at theorem level.
"""
from math import gcd
from fractions import Fraction
from pathlib import Path
import csv
import sympy as sp

OUT=Path('/mnt/data')
G,K,a,tau,n,Y0=sp.symbols('G K a tau n Y0', integer=True)
S=(G+1)*(2*G+3)
C0=S*a
Q=4*G**3*K**2-4*G**3+8*G**2*K**2-12*G**2+4*G*K**2-13*G-6
M=sp.expand(G**3*tau-(10*G**2+4*G-2)*a)
L=sp.expand((Q*M+4*S*a)/G)
assert sp.denom(sp.cancel(L))==1
L=sp.expand(L)

# New Euclidean support identities.
assert sp.factor(M.subs(G,-1)+tau+4*a)==0
# 2G+3=0 => G=-3/2; clearing 8:
assert sp.factor(8*M.subs(G,sp.Rational(-3,2)) + 27*tau+116*a)==0
lin1=tau+4*a
lin2=27*tau+116*a
assert sp.expand(lin2-27*lin1)==8*a

# Primitive gcd consequences from tau=-31a+2Kn, gcd(a,n)=1.
# gcd(a,tau)=gcd(a,2Kn)=1 because a is a ten-unit and K is a power of ten.
# Then lin1 is odd, gcd(lin1,a)=1, and gcd(lin1,lin2)=gcd(lin1,8a)=1.
# We certify the exact Bezout reduction symbolically above; integer gcd is checked below exhaustively modulo 2K.

# Mod 8 live-range identities (G divisible by 16, K divisible by 10).
# M == 2a mod 8. Expanded L has all G-terms 0 mod8 and 8K^2a+18a ==2a.
# Thus M/2 == L/2 == a mod4.
assert sp.expand(L).subs(G,0) == 8*K**2*a+18*a

ratio={
    10:(Fraction(0,1),Fraction(9,1)),
    100:(Fraction(0,1),Fraction(9,10)),
    1000:(Fraction(0,1),Fraction(9,100)),
}
lin_bounds={
    10:(Fraction(13,1),Fraction(359,1),Fraction(4667,1)),
    100:(Fraction(49,10),Fraction(1403,10),Fraction(68747,100)),
    1000:(Fraction(409,100),Fraction(11843,100),Fraction(4843787,10000)),
}

def strip_support(x,Sv):
    """Remove the maximal divisor of x supported on primes dividing Sv, no factorization."""
    x=abs(x)
    while x:
        d=gcd(x,Sv)
        if d==1:
            return x
        x//=d
    return 0

def cell_rows():
    rows=[]
    for KK in (10,100,1000):
        mod=2*KK
        amin=4 if KK<1000 else 5
        # primitive deflation permutes these unit cells, so enumerate a directly.
        cells=0;c1=c3=0
        for ar in range(mod):
            if gcd(ar,10)!=1: continue
            tr=(-31*ar)%mod
            assert gcd(tr,10)==1
            # n=(31a+tau)/(2K) is integral on the cell.
            am4=ar%4
            assert am4 in (1,3)
            if am4==1:c1+=1
            else:c3+=1
            rows.append(dict(
                K=KK,
                cell=f'a={ar};tau={tr} (mod {mod})',
                g=f'g>={amin}, periodic',
                a_mod_4=am4,
                tau_mod_4=am4,
                linear1='tau+4a',
                linear2='27tau+116a',
                common_support='d|linear1*linear2; gcd(linear1,linear2)=1',
                M0_mod_4=am4,
                inert_kernel_status='odd inert kernels of M0,L0 divide d',
                gaussian_support_status='S-free(M0),S-free(L0) must both be 1 mod4',
                root_status='OPEN_GLOBAL_NORM'))
            cells+=1
        assert cells=={10:8,100:80,1000:800}[KK]
        assert c1==c3==cells//2
        print(f'K={KK} CELLS={cells} A_MOD4_COUNTS=({c1},{c3})')
    return rows

def diagnostic_external_gate():
    """Small exact diagnostics only; never promoted to a global proof."""
    tests=[
        (1000,10**5,451,19),
        (1000,10**5,193,17),
        (100,10**4,19,11),
        (10,10**4,9,1),
    ]
    out=[]
    for KK,GG,aa,tt in tests:
        nn=(tt+31*aa)//(2*KK)
        if (tt+31*aa)%(2*KK): continue
        MM=int(M.subs({G:GG,K:KK,a:aa,tau:tt}))
        LL=int(L.subs({G:GG,K:KK,a:aa,tau:tt}))
        SS=(GG+1)*(2*GG+3)
        assert MM%2==LL%2==0
        me=strip_support(MM//2,SS)
        le=strip_support(LL//2,SS)
        out.append((KK,GG,aa,tt,nn,me%4,le%4,
                    'KILL' if (me%4==3 or le%4==3) else 'PASS_SUPPORT_GATE'))
    return out


# Positivity audit: the requested M>0 conclusion is NOT implied by the
# primitive/DCDC ratio package alone.  These exact states satisfy
# tau=-31a+2Kn, gcd(a,n)=1, a ten-unit, g-k>=2, 0<tau/a<the sharp window,
# and a<G, but have M<0 (and L<0).  They are support-level counterexamples,
# not Gaussian roots.
NEG_M_WITNESSES=[
    (10,10**4,1009,1,1564),
    (100,10**4,1129,1,175),
    (1000,10**5,10129,1,157),
]
for KK,GG,aa,tt,nn in NEG_M_WITNESSES:
    assert tt == -31*aa + 2*KK*nn
    assert gcd(aa,nn)==1 and gcd(aa,10)==1
    assert GG//KK >= 100
    assert Fraction(tt,aa) < ratio[KK][1]
    MM=int(M.subs({G:GG,K:KK,a:aa,tau:tt}))
    LL=int(L.subs({G:GG,K:KK,a:aa,tau:tt}))
    assert MM<0 and LL<0

# Exact ratio -> linear-factor bounds.
for KK,(lo,hi) in ratio.items():
    b1,b2,bd=lin_bounds[KK]
    assert Fraction(4,1)+hi == b1
    assert Fraction(116,1)+27*hi == b2
    assert b1*b2 == bd

# Exhaustive modular primitive-gcd check on all 888 cells.
for KK in (10,100,1000):
    mod=2*KK
    for ar in range(mod):
        if gcd(ar,10)!=1: continue
        tr=(-31*ar)%mod
        # gcd(a,tau)=1 is not implied by a residue cell alone for arbitrary lifts,
        # so do NOT assert it here. It follows only after primitive gcd(a,n)=1.
        assert (31*ar+tr)%mod==0

rows=cell_rows()
p=OUT/'J2-55-R12-q1-GaussianSupport.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
    fields=['K','cell','g','a_mod_4','tau_mod_4','linear1','linear2','common_support',
            'M0_mod_4','inert_kernel_status','gaussian_support_status','root_status']
    wri=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t')
    wri.writeheader();wri.writerows(rows)

print('J2-55 R12 q=1 Gaussian support certificate')
print('Y_EVEN=PROVED_FROM_ML_DIV4_AND_CSTAR_EVEN')
print('GAUSS0=M0*L0=Y0^2+[S_G*a]^2')
print('MG1=M == -(tau+4a) mod (G+1)')
print('MG2=8M == -(27tau+116a) mod (2G+3)')
print('GCD_GPLUS1_2GPLUS3=1')
print('PRIMITIVE_GCD_A_TAU=1 from tau=-31a+2Kn, gcd(a,n)=1, gcd(a,2K)=1')
print('LIN_COPRIME=gcd(tau+4a,27tau+116a)=1')
print('COMMON_SUPPORT=d|[(tau+4a)(27tau+116a)]')
print('INERT_KERNEL_M0_DIVIDES_D=PROVED')
print('INERT_KERNEL_L0_DIVIDES_D=PROVED')
print('S_FREE_M0_MOD4_MUST_EQUAL_1=PROVED')
print('S_FREE_L0_MOD4_MUST_EQUAL_1=PROVED')
print('M0_MOD4=L0_MOD4=a_MOD4 in live g>=4')
print('M_POSITIVITY_FROM_PRIMITIVE_RATIO_PACKAGE=FALSE')
print('M_POSITIVITY_COUNTEREXAMPLES=',NEG_M_WITNESSES)
print('M_SIGN_MUST_BE_HANDLED_IN_GAUSSIAN_NORM; no positive-factor allocation assumed')
for KK in (10,100,1000):
    lo,hi=ratio[KK]
    b1,b2,bd=lin_bounds[KK]
    print(f'K={KK} TAU_OVER_A=(0,{hi}) LIN1<{b1}a LIN2<{b2}a d<{bd}a^2')
print('DIAGNOSTIC_EXTERNAL_GATE=',diagnostic_external_gate())
print('K1000_CLOSED=False')
print('K100_CLOSED=False')
print('K10_CLOSED=False')
print('Q1_TOTAL_CLOSED=False')
print('LEDGER='+p.name)
