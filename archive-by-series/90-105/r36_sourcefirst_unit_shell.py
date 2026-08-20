#!/usr/bin/env python3
from math import gcd, isqrt, lcm
from csv import DictWriter
from json import dump
from pathlib import Path

OUT=Path('/mnt/data/105-R36')
ROOTS=OUT/'105-R36-sourcefirst-unit-F11-root-registry.csv'
SUMMARY=OUT/'105-R36-sourcefirst-unit-search-summary.json'

def divisors(n):
    ds=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ds.append(d)
            if d*d!=n: ds.append(n//d)
    return sorted(ds)

def ceil_div(a,b): return (a+b-1)//b

def first_coprime(lo,hi,m):
    for u in range(lo,hi+1):
        if gcd(u,m)==1: return u
    return None

fields=['u0','Lambda','A','W','C2','C3','Ulo','Uhi','Umin','V0','mu','g0_selector','g1star','P1','P2','P3','Q0','D','H','T3','lambda_z','actual_g0','g0_match','g1_div_P1','primitive','Lambda_recovered','post_basic_pass','first_failure']
rows=[]
counts=dict(source_arch_configs=0,f11_configs=0,disc_sq=0,int_roots=0,post_basic=0)

# Exact source-first bounded shell:
# residual q=1; regular generic source superset; n2=2,n3=1;
# exponent skeleton gives m2=m3=1,g=0,k=1.
for u0 in range(1,21):
  for Lam in range(1,10):
    maxaw=9//Lam
    for A in range(1,maxaw+1):
      for W in range(1,maxaw+1):
        M0=u0*A*W
        g0ds=divisors(M0)
        muds=divisors(Lam)
        X=10; Y=10; G=1; K=10
        for C2 in range(2,100):
          if gcd(Lam*A,C2)!=1: continue
          ulo2=ceil_div(10,C2); uhi2=99//C2
          if ulo2>uhi2: continue
          for C3 in range(1,10):
            if gcd(Lam*W,C3)!=1: continue
            ulo=max(1,ulo2,ceil_div(1,C3))
            uhi=min(uhi2,9//C3)
            if ulo>uhi: continue
            V0=Lam*M0
            umin=first_coprime(ulo,uhi,V0)
            if umin is None: continue
            counts['source_arch_configs']+=1
            P2=u0*W*C2
            P3=u0*A*C3
            # source-first F11 generator, all exact integer arithmetic
            Lc=A*W*u0*X*Y*G*K
            Bbase=A*W*u0*X*Y*G
            for mu in muds:
              for g0sel in g0ds:
                g1=mu*g0sel
                counts['f11_configs']+=1
                B=g1*(W+A*Y*G)+Bbase
                C=g1*(W*P3+A*Y*P2)
                aa=B*B-Lc*Lc
                bb=-2*B*C
                cc=C*C+Lc*Lc*(P2*P2+P3*P3)
                roots=[]
                if aa==0:
                    if bb!=0 and (-cc)%bb==0:
                        roots=[(-cc)//bb]
                else:
                    disc=bb*bb-4*aa*cc
                    if disc<0: continue
                    sd=isqrt(disc)
                    if sd*sd!=disc: continue
                    counts['disc_sq']+=1
                    den=2*aa
                    for num in (-bb+sd,-bb-sd):
                        if den and num%den==0:
                            q0=num//den
                            if q0>0: roots.append(q0)
                for Q0 in sorted(set(roots)):
                    num=B*Q0-C
                    if num%Lc!=0: continue
                    P1=num//Lc
                    if P1<=0: continue
                    # verify sphere exactly; F11 should imply, but retain explicit check
                    if P1*P1+P2*P2+P3*P3!=Q0*Q0: continue
                    counts['int_roots']+=1
                    D=10*P1-Q0
                    H=Q0-P2
                    T3=Q0-P3
                    actual_g0=gcd(M0,P1)
                    g0match=(actual_g0==g0sel)
                    g1div=(P1%g1==0)
                    prim=(gcd(gcd(gcd(P1,P2),P3),Q0)==1)
                    lamz=10//gcd(10,W*T3) if T3>0 else 0
                    lrec=(T3>0 and lcm(mu,lamz)==Lam)
                    post=(D>0 and H>0 and T3>0 and g0match and g1div and prim and lrec)
                    if post: counts['post_basic']+=1
                    if not g0match: ff='G0_SELECTOR_MISMATCH'
                    elif not g1div: ff='G1STAR_NOT_DIVIDING_P1'
                    elif not prim: ff='NONPRIMITIVE_SPHERE'
                    elif D<=0: ff='D_NONPOSITIVE'
                    elif H<=0: ff='H_NONPOSITIVE'
                    elif T3<=0: ff='T3_NONPOSITIVE'
                    elif not lrec: ff='LAMBDA_RECOVERY_MISMATCH'
                    else: ff='POST_BASIC_PASS'
                    rows.append(dict(u0=u0,Lambda=Lam,A=A,W=W,C2=C2,C3=C3,Ulo=ulo,Uhi=uhi,Umin=umin,V0=V0,mu=mu,g0_selector=g0sel,g1star=g1,P1=P1,P2=P2,P3=P3,Q0=Q0,D=D,H=H,T3=T3,lambda_z=lamz,actual_g0=actual_g0,g0_match=int(g0match),g1_div_P1=int(g1div),primitive=int(prim),Lambda_recovered=int(lrec),post_basic_pass=int(post),first_failure=ff))

with ROOTS.open('w',newline='') as f:
    w=DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
with SUMMARY.open('w') as f:
    dump({'scope':{'residual_q':1,'source_chart':'regular generic superset; native selector forgotten, gcd(U,V0) retained','n2':2,'n3':1,'m2':1,'m3':1,'g':0,'k':1,'u0_max':20,'Lambda_max':9,'C2':'2..99','C3':'1..9'},'counts':counts,'root_rows':len(rows),'global_inference':False},f,indent=2)
print(counts)
print('root_rows',len(rows))
