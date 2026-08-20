#!/usr/bin/env python3
from math import gcd
from pathlib import Path
import csv
import sympy as sp

OUT=Path('/mnt/data/Fourth_85_R2_computation')

PAIRS=[(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)]
KS=[10,100,1000]


def vp(n,p):
    if n==0: return 10**9
    n=abs(n); e=0
    while n%p==0:
        n//=p; e+=1
    return e


def pos_residue(a,m):
    a%=m
    return a if a else m


def source_rho(K,d,tau,g):
    G=10**g
    inv31=pow(31,-1,2*K)
    rho0=pos_residue(-tau*inv31,2*K)
    upper=(10-d*tau)*G/(10*d)
    # primitive source also requires gcd(rho,tau)=1; scan the fixed residue lattice.
    x=rho0
    while x<upper:
        if gcd(x,10*tau)==1:
            return x
        x+=2*K
    return None


def crt_pair(a,m,b,n):
    assert gcd(m,n)==1
    return (a + ((b-a)*pow(m,-1,n)%n)*m)%(m*n)


def positive_lift(a,m,minimum=1):
    a%=m
    if a<minimum:
        a += ((minimum-a + m-1)//m)*m
    return a


def make_orientation(g,k,rho,tau,ori):
    G=10**g
    P=2**(g-2)
    Q=5**(g-1)
    H=10**(g-1)
    e2=g-k-1
    e5=g-k+min(k,2)-1
    m2=2**e2; m5=5**e5
    bnd=tau-10*rho
    if ori=='A':
        # Deep eta congruence + gap imply ell == tau-10rho mod both deep prime powers.
        ell0=crt_pair(bnd%m2,m2,bnd%m5,m5)
        ell=positive_lift(ell0,m2*m5,1)
        while gcd(ell,rho)!=1:
            ell+=m2*m5
        rr=G//20*ell + rho
        L=H*ell; R=2*rr
    elif ori=='D':
        # Deep eta congruence + gap imply r == 10rho-tau mod both deep prime powers.
        rt=-bnd
        r0=crt_pair(rt%m2,m2,rt%m5,m5)
        rr=positive_lift(r0,m2*m5,1)
        while H*rr<=2*rho or gcd(rr,rho)!=1:
            rr+=m2*m5
        ell=G//20*rr-rho
        L=2*ell; R=H*rr
    elif ori=='B':
        # Q*r - P*ell = rho. General solution ell=ell0+Q*t, r=r0+P*t.
        ell0=(-rho*pow(P,-1,Q))%Q
        if ell0==0: ell0=Q
        r0=(rho+P*ell0)//Q
        # Mod 2^e2: r is fixed by the gap, tune ell.
        target_ell2=(bnd*Q)%m2
        t2=((target_ell2-ell0)*pow(Q,-1,m2))%m2
        # Mod 5^e5: ell is fixed by the gap, tune r.
        target_r5=(-bnd*P)%m5
        t5=((target_r5-r0)*pow(P,-1,m5))%m5
        t0=crt_pair(t2,m2,t5,m5)
        t=positive_lift(t0,m2*m5,1)
        while True:
            ell=ell0+Q*t; rr=r0+P*t
            if ell>0 and rr>0 and gcd(ell,rr)==1:
                break
            t+=m2*m5
        L=2**(g-1)*ell; R=2*Q*rr
    elif ori=='C':
        # P*r - Q*ell = rho. General solution r=r0+Q*t, ell=ell0+P*t.
        r0=(rho*pow(P,-1,Q))%Q
        if r0==0: r0=Q
        ell0=(P*r0-rho)//Q
        # Mod 2^e2: ell fixed by gap, tune r.
        target_r2=(-bnd*Q)%m2
        t2=((target_r2-r0)*pow(Q,-1,m2))%m2
        # Mod 5^e5: r fixed by gap, tune ell.
        target_ell5=(bnd*P)%m5
        t5=((target_ell5-ell0)*pow(P,-1,m5))%m5
        t0=crt_pair(t2,m2,t5,m5)
        t=positive_lift(t0,m2*m5,1)
        while True:
            rr=r0+Q*t; ell=ell0+P*t
            if rr>0 and ell>0 and gcd(ell,rr)==1:
                break
            t+=m2*m5
        L=2*Q*ell; R=2**(g-1)*rr
    else: raise ValueError(ori)
    assert R-L==2*rho
    y=(L+R)//2
    assert L>0 and R>0 and y>rho>0
    assert gcd(y,10)==1 and gcd(rho,10)==1
    eta=L*R//(2**g*5**(g-1))
    assert L*R==2**g*5**(g-1)*eta
    assert gcd(eta,10)==1
    assert (eta-rho*bnd)%m2==0
    assert (eta-rho*bnd)%m5==0
    assert eta%10==(rho*tau)%10
    vals=(vp(L,2),vp(L,5),vp(R,2),vp(R,5))
    expected={
        'A':(g-1,g-1,1,0),
        'B':(g-1,0,1,g-1),
        'C':(1,g-1,g-1,0),
        'D':(1,0,g-1,g-1),
    }[ori]
    assert vals==expected,(ori,g,rho,vals,expected,L,R,ell,rr)
    h=gcd(y,rho)
    assert gcd(L,R)==2*h
    assert gcd(ell,rr)==h
    assert eta==ell*rr
    return dict(orientation=ori,g=g,G=G,rho=rho,tau=tau,L=L,R=R,y=y,ell=ell,r=rr,eta=eta,
                e2=e2,e5=e5,v2L=vals[0],v5L=vals[1],v2R=vals[2],v5R=vals[3],h=h,gcdLR=gcd(L,R))

# Symbolic conic defect and odd-prime destination polynomial.
G,K,rho,tau=sp.symbols('G K rho tau', integer=True, positive=True)
A2=(100*G**6*K**2-100*G**6+280*G**5*K**2-380*G**5+236*G**4*K**2-545*G**4
    +16*G**3*K**2-362*G**3-52*G**2*K**2-93*G**2-8*G*K**2+4*K**2)
B1=-G**2*tau*(20*G**5*K**2-20*G**5+48*G**4*K**2-68*G**4+32*G**3*K**2-85*G**3-46*G**2-4*G*K**2-4*G+3)
PK=4*G**4*K**2-4*G**4+8*G**3*K**2-12*G**3+4*G**2*K**2-13*G**2-6*G+1
QK=sp.cancel((PK-1)/G)
C0=G**5*tau**2*QK/4
a=tau*G/10+rho
rhs=sp.expand(A2*a**2+B1*a+C0)
diff=sp.factor(rhs-(2*K*rho)**2)
pr=sp.Poly(sp.expand(diff),rho)
cr2=sp.factor(pr.coeff_monomial(rho**2))
cr1=sp.factor(pr.coeff_monomial(rho))
cr0=sp.factor(pr.coeff_monomial(1))
Psi=sp.factor(100*cr0/(G**2*tau**2))
Psi_expected=16*G**4*K**2-20*G**4+16*G**3*K**2-52*G**3-12*G**2*K**2-53*G**2-8*G*K**2-30*G+4*K**2
assert sp.expand(Psi-Psi_expected)==0

# Build 24x4 necessary-skeleton witnesses at the earliest g where source rho class meets the window.
rows=[]
for KK in KS:
    k=len(str(KK))-1
    for d,tt in PAIRS:
        found=None
        for g in range(k+2,k+9):
            rr=source_rho(KK,d,tt,g)
            if rr is not None:
                found=(g,rr); break
        assert found is not None
        g,rrho=found
        G0=10**g
        assert (31*rrho+tt)%(2*KK)==0
        assert gcd(rrho,10*tt)==1
        assert 0<rrho<(10-d*tt)*G0/(10*d)
        for ori in 'ABCD':
            z=make_orientation(g,k,rrho,tt,ori)
            z.update(K=KK,k=k,d=d,case=f'K{KK}_d{d}_tau{tt}',scope='NECESSARY_SKELETON_PLUS_DEEP_ETA')
            rows.append(z)

fields=['case','K','k','d','tau','g','G','orientation','rho','L','R','y','ell','r','eta','e2','e5','v2L','v5L','v2R','v5R','h','gcdLR','scope']
with (OUT/'counterexample_skeleton_witnesses.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t'); w.writeheader(); w.writerows(rows)
assert len(rows)==96

# Universal orientation table.
orient=[
    dict(orientation='A',L='10^(g-1)*ell',R='2*r',gap='r=(G/20)*ell+rho',last_digit='ell=tau (mod 10); r=rho (mod 10)'),
    dict(orientation='B',L='2^(g-1)*ell',R='2*5^(g-1)*r',gap='5^(g-1)r-2^(g-2)ell=rho',last_digit='r=-tau*2^(g-2) (mod 5); ell=-rho*2^(-(g-2)) (mod 5)'),
    dict(orientation='C',L='2*5^(g-1)*ell',R='2^(g-1)*r',gap='2^(g-2)r-5^(g-1)ell=rho',last_digit='r=rho*2^(-(g-2)) (mod 5); ell=tau*2^(g-2) (mod 5)'),
    dict(orientation='D',L='2*ell',R='10^(g-1)*r',gap='ell=(G/20)*r-rho',last_digit='ell=-rho (mod 10); r=-tau (mod 10)'),
]
with (OUT/'orientation_table.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['orientation','L','R','gap','last_digit'],delimiter='\t');w.writeheader();w.writerows(orient)

# Targeted modular compatibility: every fixed case/orientation has a witness; summarize by case.
with (OUT/'modular_orientation_compatibility.tsv').open('w',newline='',encoding='utf-8') as f:
    fw=csv.writer(f,delimiter='\t'); fw.writerow(['K','d','tau','orientations_realized','status'])
    for KK in KS:
        for d,tt in PAIRS:
            os=sorted({r['orientation'] for r in rows if r['K']==KK and r['d']==d and r['tau']==tt})
            fw.writerow([KK,d,tt,','.join(os),'ALL_4_NECESSARY_SKELETON_COMPATIBLE'])

with (OUT/'symbolic_factorizations.txt').open('w',encoding='utf-8') as f:
    f.write('DEFECT_RHO2_COEFF = '+str(cr2)+'\n\n')
    f.write('DEFECT_RHO1_COEFF = '+str(cr1)+'\n\n')
    f.write('DEFECT_RHO0_COEFF = '+str(cr0)+'\n\n')
    f.write('PSI_K_G = '+str(Psi)+'\n')
    for KK in KS:
        f.write(f'PSI_K{KK} = {sp.expand(Psi.subs(K,KK))}\n')

with (OUT/'modular_search_summary.txt').open('w',encoding='utf-8') as f:
    f.write('TARGET=valuation-template/factor-gap quotient residue compatibility\n')
    f.write('FIXED_CASES=24\nORIENTATIONS_PER_CASE=4\n')
    f.write('NECESSARY_SKELETON_WITNESSES=96\n')
    f.write('ALL_24x4_COMPATIBLE=TRUE\n')
    f.write('INTERPRETATION=No immediate local/source death follows from exact 2/5 cores + gap + deep eta congruences + DCDC rho residue/window alone.\n')
    f.write('NOT_A_SOURCE_SOLUTION_SEARCH=TRUE\n')

# Compress the 24 source cases at coefficient level: d occurs only in the source window.
with (OUT/'fixed_case_compression.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['K','tau','d_values','coefficient_template_count','orientation_templates','note'])
    for KK in KS:
        for tt in [1,3,7,9]:
            ds=[d for d,t0 in PAIRS if t0==tt]
            w.writerow([KK,tt,','.join(map(str,ds)),1,4,'d appears only in source upper window; conic/factor coefficients depend on (K,tau)'])

with (OUT/'deep_eta_congruence.txt').open('w',encoding='utf-8') as f:
    f.write('e2 = g-k-1 >= 1\n')
    f.write('e5 = g-k+min(k,2)-1 >= 2\n')
    f.write('eta == rho*(tau-10*rho) mod 2^e2\n')
    f.write('eta == rho*(tau-10*rho) mod 5^e5\n')
    f.write('A: ell == tau-10*rho modulo both deep prime powers\n')
    f.write('D: r == 10*rho-tau modulo both deep prime powers\n')
    f.write('B/C: compatible via the one-parameter exact gap solution and CRT lifting\n')

with (OUT/'r2_certificate.txt').open('w',encoding='utf-8') as f:
    f.write('FOURTH_85_R2_FACTOR_GAP_AUDIT=PASS\n')
    f.write('LIVE_G_MIN=3 (historical g>=k+2, k>=1)\n')
    f.write('ORIENTATION_COUNT_BEFORE=4\nORIENTATION_COUNT_AFTER=4\n')
    f.write('EXACT_GCD=gcd(L,R)=2*gcd(y,rho)\n')
    f.write('ODD_COMMON_DESTINATION=gcd(y,rho) divides Psi_K(G)\n')
    f.write('FIXED_S_SUPPORT=NOT_PROVED\n')
    f.write('FULL_ETA_PARAMETERIZATION=ORIGINAL_SQUARE_CONDITION_RETURN\n')
    f.write('COEFFICIENT_TEMPLATES_AFTER_d_COMPRESSION=12\n')
    f.write('COUNTEREXAMPLE_GUILLOTINE=ALL_24x4_DEEP_ETA_SKELETON_COMPATIBLE_WITH_h_EQ_1\n')
    f.write('Q1_BRANCH_CLOSED=NO\n')
    f.write('FINAL_VERDICT=FACTOR_GAP_ARCHITECTURE_DEAD\n')

print('R2_AUDIT_PASS')
print('WITNESSES',len(rows))
print('PSI',Psi)
