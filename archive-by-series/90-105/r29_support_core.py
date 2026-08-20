#!/usr/bin/env python3
from math import gcd, ceil, floor
from fractions import Fraction
from pathlib import Path
import csv, hashlib, json

ROOT = Path('/mnt/data/105-R29')
ROOT.mkdir(parents=True, exist_ok=True)

def vp(n,p):
    if n == 0:
        return None
    n=abs(n); e=0
    while n%p==0:
        e+=1; n//=p
    return e

def eval_point(name,P1,P2,P3,Q0,A,W,u0,g1,n,m,k,g, shape_expected=True):
    C2=P2//(u0*W)
    C3=P3//(u0*A)
    T=Q0-P3
    H=(10**g)*Q0-P2
    D=(10**k)*P1-Q0
    r=m+n+g
    g0=gcd(A*W,P1)
    mu=g1//g0
    a0=A*W//g0
    ell=(W+A*10**(n+g))//u0
    Xi=Q0*ell-A*W*(C3+(10**n)*C2)
    Omega=W*T+A*(10**n)*H
    tc1_lhs=g1*Omega
    tc1_rhs=A*W*u0*(10**r)*D
    core_lhs=mu*Xi
    core_rhs=a0*(10**r)*D
    sphere=P1*P1+P2*P2+P3*P3==Q0*Q0
    shape=(gcd(A,C2)==1 and gcd(W,C3)==1 and gcd(A,W)==1)
    n2=m+g+k
    ur_lo=max(ceil(10**(n2-1)/C2),ceil(10**(n-1)/C3))
    ur_hi=min(floor((10**n2-1)/C2),floor((10**n-1)/C3))
    d=n+g-m
    theta=Fraction(W, A*(10**d))
    return {
        'name':name,'P1':P1,'P2':P2,'P3':P3,'Q0':Q0,'A':A,'W':W,'u0':u0,'g1star':g1,
        'n':n,'m':m,'k':k,'g':g,'C2':C2,'C3':C3,'T':T,'H':H,'D':D,'r':r,'g0':g0,'mu':mu,'a0':a0,
        'ell':ell,'Xi':Xi,'Omega':Omega,'sphere':sphere,'shape':shape,'radial_lo':ur_lo,'radial_hi':ur_hi,
        'radial_pass':ur_lo<=ur_hi,'smith_gcd_C2':gcd(mu,C2),'smith_gcd_C3':gcd(mu,C3),
        'smith_gcd_total':gcd(mu,C2*C3),'tc1_lhs':tc1_lhs,'tc1_rhs':tc1_rhs,'tc1_pass':tc1_lhs==tc1_rhs,
        'core_lhs':core_lhs,'core_rhs':core_rhs,'core_pass':core_lhs==core_rhs,
        'v2_mu':vp(mu,2),'v5_mu':vp(mu,5),'v2_C2':vp(C2,2),'v5_C2':vp(C2,5),
        'v2_C3':vp(C3,2),'v5_C3':vp(C3,5),'v2_Xi':vp(Xi,2),'v5_Xi':vp(Xi,5),
        'v2_a0':vp(a0,2),'v5_a0':vp(a0,5),'v2_D':vp(D,2),'v5_D':vp(D,5),
        'd':d,'theta_num':theta.numerator,'theta_den':theta.denominator,
        'ratio_pass':Fraction(1,10)<theta<10,
    }

# R28 global positive-radial conic points, recovered from frozen registry + exact packets.
r28_points=[
    eval_point('ARCH_07',240,1155,56,1181,1,1,7,80,2,1,1,1),
    eval_point('ARCH_08',240,1155,56,1181,7,7,1,80,2,1,1,1),
    eval_point('ARCH_24',480,1040,2499,2749,3,2,1,240,3,2,1,0),
    eval_point('ARCH_30',200,365,104,429,13,1,1,40,1,1,1,1),
]

# Genuine R20/R21 support-stack point; crucial R29 counterexample.
cex=eval_point('R29_CEX_R20',640,1420,4727,4977,1,20,1,80,4,1,1,0)

# exact assertions
assert cex['sphere'] and cex['shape'] and cex['radial_pass'] and cex['tc1_pass'] and cex['core_pass']
assert cex['smith_gcd_total']==1
assert cex['C2']==71 and cex['C3']==4727 and cex['mu']==4
assert cex['Xi']==35575000 and cex['r']==5
assert not cex['ratio_pass'] and Fraction(cex['theta_num'],cex['theta_den'])==Fraction(1,50)
assert cex['Xi'] > 10**cex['r'] and cex['Xi'] > min(cex['C2'],cex['C3'])
assert all(p['sphere'] and p['tc1_pass'] and p['core_pass'] for p in r28_points)
assert [p['smith_gcd_total'] for p in r28_points]==[40,40,40,40]
assert r28_points[1]['shape'] is False

# R26 denominator continuation for cex packet
m2=1; m3=4
z_lower=max(ceil(10**(m2-1)/cex['A']), ceil(10**(m3-1)/cex['W']))
z_upper=min(floor((10**m2-1)/cex['A']), floor((10**m3-1)/cex['W']))
assert (z_lower,z_upper)==(50,9)

# autopsy CSV
fields=['name','P1','P2','P3','Q0','A','W','u0','g1star','n','m','k','g','C2','C3','mu','Xi','a0','D','r','radial_lo','radial_hi','shape','smith_gcd_C2','smith_gcd_C3','smith_gcd_total','v2_mu','v2_C2','v2_C3','v2_Xi','v2_a0','v2_D','v5_mu','v5_C2','v5_C3','v5_Xi','v5_a0','v5_D','d','theta_num','theta_den','ratio_pass']
with open(ROOT/'105-R29-R28-positive-radial-autopsy.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader();
    for p in r28_points: w.writerow({k:p[k] for k in fields})

# gcd valuation registry including counterexample
with open(ROOT/'105-R29-gcd-valuation-registry.csv','w',newline='',encoding='utf-8') as f:
    fs=['name','mu','C2','C3','gcd_mu_C2','gcd_mu_C3','gcd_mu_C2C3','v2_mu','v2_C2','v2_C3','v2_Xi','v5_mu','v5_C2','v5_C3','v5_Xi','structural_note']
    w=csv.DictWriter(f,fieldnames=fs); w.writeheader()
    for p in r28_points+[cex]:
        note='R28 observed positive-radial point; gcd=40 is sample-specific' if p['name'].startswith('ARCH') else 'Genuine TC1+shape+positive-radial+Smith+tail support counterexample; gcd=1'
        w.writerow({'name':p['name'],'mu':p['mu'],'C2':p['C2'],'C3':p['C3'],'gcd_mu_C2':p['smith_gcd_C2'],'gcd_mu_C3':p['smith_gcd_C3'],'gcd_mu_C2C3':p['smith_gcd_total'],'v2_mu':p['v2_mu'],'v2_C2':p['v2_C2'],'v2_C3':p['v2_C3'],'v2_Xi':p['v2_Xi'],'v5_mu':p['v5_mu'],'v5_C2':p['v5_C2'],'v5_C3':p['v5_C3'],'v5_Xi':p['v5_Xi'],'structural_note':note})

# architecture-free certificate
cert_rows=[
 ('MU_A0_COPRIME','PROVED','g0=gcd(AW,P1), mu|P1/g0, a0=AW/g0 => gcd(mu,a0)=1'),
 ('MU_DIVIDES_10R_D','PROVED','mu*Xi=a0*10^r*D and gcd(mu,a0)=1'),
 ('MU_DIVIDES_10R_Q0','PROVED','D=10^k P1-Q0 and mu|P1'),
 ('NONDECIMAL_COMMON_SUPPORT','EXTINCT','p!=2,5, p|mu and p|C2 or C3 forces p|P1,P2,P3,Q0, contradicting primitive sphere'),
 ('DECIMAL_ONLY_COLLISION_REDUCTION','PROVED','supp(mu) intersect supp(C2*C3) subset {2,5}'),
 ('C3_EVEN_SMITH_BRANCH','EXTINCT_IN_R28','R28 exact 2-adic theorem; under TC1+shape+Smith, C3 is odd'),
 ('UNIVERSAL_2_DIVIDES_C2','FALSE','R29_CEX_R20 has C2=71'),
 ('UNIVERSAL_2_DIVIDES_C2C3','FALSE','R29_CEX_R20 has C2=71,C3=4727 both odd'),
 ('UNIVERSAL_5_DIVIDES_MU','FALSE','R29_CEX_R20 has mu=4'),
 ('UNIVERSAL_5_DIVIDES_C2C3','FALSE','R29_CEX_R20 has C2*C3 coprime to 5'),
 ('UNIVERSAL_MU_SMITH_COLLISION','FALSE','R29_CEX_R20 has gcd(mu,C2*C3)=1 and passes TC1+shape+positive radial'),
 ('XI_LT_10R_RADIAL_BOUND','FALSE','R29_CEX_R20: Xi=35575000 > 10^5'),
 ('XI_LT_MIN_C2_C3_BOUND','FALSE','R29_CEX_R20: Xi=35575000 > 71'),
 ('HISTORICAL_GCD40_UNIVERSAL_DIVISOR','FALSE','R29_CEX_R20 has gcd=1; no nontrivial divisor common to all legal post-radial examples'),
 ('TC1_EQUALS_DIRECT_W_MASTER','PROVED','W[u0 A X Y G D-g1*T]=g1*A*Y*H iff g1[W*T+A*Y*H]=A*W*u0*X*Y*G*D'),
 ('TC1_CONDITIONED_RATIO_NEW_INFORMATION','ZERO','TC1 is exactly the Direct-W/master equation already present on R20-R25 support-stack locus'),
 ('COUNTEREXAMPLE_NEXT_FIRST_FAILURE','DENOMINATOR_RATIO','theta=1/50; R26 complete packet replay gives Z_-=50>Z_+=9'),
 ('STRICT_A1_UNLIFTABILITY','NOT_PROVED','R29 disproves Smith killer but does not globally eliminate all primitive carriers'),
]
with open(ROOT/'105-R29-architecture-free-certificate.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['claim','status','certificate']); w.writerows(cert_rows)

# exceptional branch registry
branches=[
 ('NONDECIMAL_OVERLAP','p!=2,5 divides mu and C2*C3','EXTINCT','primitive sphere contradiction'),
 ('C3_EVEN_UNDER_SMITH','2|C3 and gcd(mu,C2*C3)=1','EXTINCT','R28 2-adic mu-core theorem'),
 ('DECIMAL_COLLISION_R28_SAMPLE','2 or 5 shared between mu and C2*C3','REAL_BUT_NOT_UNIVERSAL','ARCH_07/24/30 give gcd 40'),
 ('TEN_UNIT_RADIAL_SUPPORT','gcd(C2*C3,10)=1','LIVE','R29_CEX_R20: C2=71,C3=4727,mu=4'),
 ('SMITH_PASS_TAIL_PASS_RATIO_FAIL','TC1+shape+radial+Smith+tail','LIVE_TO_RATIO','R29_CEX_R20, theta=1/50'),
 ('RATIO_WINDOW_FOR_CEX_PACKET','Z_-<=Z_+','EXTINCT_FOR_PACKET','R26 complete enumeration: unique candidate gives 50>9'),
]
with open(ROOT/'105-R29-exceptional-branch-registry.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['branch','condition','status','evidence']); w.writerows(branches)

# survivor registry
surv_fields=['id','P1','P2','P3','Q0','A','W','u0','g1star','n','m','k','g','C2','C3','g0','mu','a0','ell','Xi','D','r','tc1','shape','radial','smith_gcd','tail_support','theta','ratio','Z_lower','Z_upper','terminal_status']
with open(ROOT/'105-R29-survivor-registry.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=surv_fields); w.writeheader();
    w.writerow({'id':'R29_CEX_R20','P1':cex['P1'],'P2':cex['P2'],'P3':cex['P3'],'Q0':cex['Q0'],'A':cex['A'],'W':cex['W'],'u0':cex['u0'],'g1star':cex['g1star'],'n':cex['n'],'m':cex['m'],'k':cex['k'],'g':cex['g'],'C2':cex['C2'],'C3':cex['C3'],'g0':cex['g0'],'mu':cex['mu'],'a0':cex['a0'],'ell':cex['ell'],'Xi':cex['Xi'],'D':cex['D'],'r':cex['r'],'tc1':'PASS','shape':'PASS','radial':'PASS_[1,1]','smith_gcd':cex['smith_gcd_total'],'tail_support':'PASS_lambda_z=2_tau=1_Lambda=4','theta':'1/50','ratio':'FAIL','Z_lower':z_lower,'Z_upper':z_upper,'terminal_status':'PACKET_UNLIFTABLE_BY_R26_DENOMINATOR_CHAMBER'})

# resultant registry: no new resultant information
with open(ROOT/'105-R29-resultant-registry.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['object','operation','status','information_gain','note'])
    w.writerow(['support-core_vs_TC1','symbolic identity comparison','COMPLETED','0','support-core is algebraic consequence/reparameterization of TC1 after g1=g0*mu and AW=g0*a0'])
    w.writerow(['TC1_vs_Direct-W','exact expansion','IDENTICAL','0_NEW_CONSTRAINT','same equation, opposite rearrangement'])
    w.writerow(['R28_TC1_sphere_resultant','inherited R28 audit','INHERITED','0','R28 resultant produced no new factor'])

# symbolic factorization text
symtxt=f'''105-R29 symbolic factorization / exact elimination ledger\n\n1. Xi exact expansion\n\nu0*Xi = W*(Q0-P3) + A*10^n*(10^g*Q0-P2)\n      = W*Q0 - W*P3 + A*10^(n+g)*Q0 - A*10^n*P2.\n\nWith P2=u0*W*C2 and P3=u0*A*C3:\n\nu0*Xi = Q0*(W+A*10^(n+g)) - u0*A*W*(C3+10^n*C2).\n\n2. Fully expanded support-core normal form\n\nF_support_core = mu*Q0*W + mu*A*10^(n+g)*Q0\n                 - mu*u0*A*W*C3 - mu*u0*A*W*10^n*C2\n                 - u0*a0*10^(r+k)*P1 + u0*a0*10^r*Q0 = 0,\nwhere r=m+n+g.\n\nEquivalently:\nmu*[Q0*ell-AW(C3+10^n*C2)] = a0*10^r*(10^k P1-Q0).\n\n3. TC1 / Direct-W identity\n\nDirect-W: W*(u0*A*X*Y*G*D-g1*T)=g1*A*Y*H.\nMove g1*W*T to the right:\nA*W*u0*X*Y*G*D = g1*(W*T+A*Y*H),\nwhich is exactly R28-PF TC1.\nThus TC1_CONDITIONED_DENOMINATOR_RATIO_INFORMATION_GAIN = 0 on the post-support/master locus.\n\n4. R29 exact counterexample\nP=(640,1420,4727), Q0=4977; A=1,W=20,u0=1,g1=80; n=4,m=1,k=1,g=0.\nT=250,H=3557,D=1423,C2=71,C3=4727,g0=20,mu=4,a0=1,ell=10020,Xi=35575000,r=5.\nTC1 LHS = {cex['tc1_lhs']}\nTC1 RHS = {cex['tc1_rhs']}\nmu-core LHS = {cex['core_lhs']}\nmu-core RHS = {cex['core_rhs']}\ngcd(mu,C2*C3)=1.\nXi/10^r = {Fraction(cex['Xi'],10**cex['r'])}.\nTheta = 1/50.\n'''
(ROOT/'105-R29-symbolic-factorization.txt').write_text(symtxt,encoding='utf-8')

# execution log
log={
 'R28_INPUT_MODE':'FILE_LIBRARY_PARSED_REFERENCE',
 'R28_BYTEWISE_SHA256_RECOMPUTATION':'UNAVAILABLE_IN_ACTIVE_RUNTIME',
 'R28_FROZEN_MANIFEST_LEDGER_CROSSCHECK':'YES',
 'R29_EXACT_ARITHMETIC':'PYTHON_INTEGERS_FRACTION',
 'R28_POSITIVE_RADIAL_POINTS_AUTOPSIED':4,
 'R28_AUTOPSY_GCDS':[p['smith_gcd_total'] for p in r28_points],
 'R29_COUNTEREXAMPLE_FOUND':'YES_R20_FROZEN_SUPPORT_STACK_WITNESS',
 'R29_COUNTEREXAMPLE_TC1':cex['tc1_pass'],
 'R29_COUNTEREXAMPLE_SMITH_GCD':cex['smith_gcd_total'],
 'R29_COUNTEREXAMPLE_TAIL_SUPPORT':'PASS_FROZEN_R20_R21',
 'R29_COUNTEREXAMPLE_THETA':'1/50',
 'R29_COUNTEREXAMPLE_Z_WINDOW':[z_lower,z_upper],
 'MU_SMITH_UNIVERSAL_COLLISION':'FALSE',
 'TC1_EQUALS_DIRECT_W_MASTER':'YES',
 'TC1_CONDITIONED_RATIO_INFORMATION_GAIN':0,
 'STRICT_A1_UNLIFTABILITY_PROVED':'NO',
}
(ROOT/'105-R29-execution.log').write_text('\n'.join(f'{k}={v}' for k,v in log.items())+'\n',encoding='utf-8')

print(json.dumps({'counterexample':cex,'z_window':[z_lower,z_upper]},ensure_ascii=False,indent=2,default=str))
