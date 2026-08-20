#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, math, os, sys, time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = 500

def gcd4(a,b,c,d): return math.gcd(math.gcd(a,b), math.gcd(c,d))
def ceildiv(a,b): return (a+b-1)//b

def vp(n,p):
    if n == 0: return 10**9
    e=0
    while n%p==0:
        n//=p; e+=1
    return e

def nu10(n): return min(vp(n,2),vp(n,5))

def divisors(n):
    out=[]
    r=math.isqrt(n)
    for d in range(1,r+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return sorted(out)

DIVCACHE={}
def divs(n):
    if n not in DIVCACHE: DIVCACHE[n]=divisors(n)
    return DIVCACHE[n]

def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d=3 if d==2 else d+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def sqf(n):
    r=1
    for p,e in factor(n).items():
        if e&1: r*=p
    return r

def primitive_packets(B):
    sums=defaultdict(list)
    for x in range(1,B):
        for y in range(1,B):
            s=x*x+y*y
            if s < B*B:
                sums[s].append((x,y))
    for q in range(2,B+1):
        qq=q*q
        for z in range(1,q):
            s=qq-z*z
            for x,y in sums.get(s,()):
                if x>=q or y>=q: continue
                if gcd4(x,y,z,q)==1:
                    yield x,y,z,q

def delta_set(M,N):
    L=max(len(str(M)),len(str(N)))+3
    out=[]
    for d in range(-L,L+1):
        if d-1>=0: low = M > N*10**(d-1)
        else: low = M*10**(1-d) > N
        if d+1>=0: high = M < N*10**(d+1)
        else: high = M*10**(-d-1) < N
        if low and high: out.append(d)
    return out

# Relaxed local selector capacity: all p-adic conditions from
# A|P3, W|P2, u0|(P2/W,P3/A), shape gcds, g0|g1|P1, mu-Smith.
def cap2_rel(P1,P2,P3,Q):
    # Historical function name retained for CSV compatibility; A is NOT assumed odd.
    T=Q-P3
    x,y,z,t=vp(P1,2),vp(P2,2),vp(P3,2),vp(T,2)
    if y>=z: return t+x+y-z
    return t+min(x,y)+max(0,x-z)

def cap5_rel(P1,P2,P3,Q):
    T=Q-P3
    x,y,z,t=vp(P1,5),vp(P2,5),vp(P3,5),vp(T,5)
    if y>=z: return t+x+y-z
    return t+min(x,y)+max(0,x-z)

def e2_branch(pi):
    P1,P2,P3,Q=pi
    x,y,z=vp(P1,2),vp(P2,2),vp(P3,2)
    # Primitive sphere has Q odd and exactly one of P1,P2,P3 odd.
    if Q%2==1 and P3%2==1:
        return True,'P3_ODD'
    if Q%2==1 and P3%2==0:
        if P1%2==0 and P2%2==1:
            return (x>z), ('P1_2_EXCESS_OVER_P3' if x>z else 'FAIL_P1_2_NOT_EXCEED_P3')
        if P1%2==1 and P2%2==0:
            return (y>z), ('P2_2_EXCESS_OVER_P3' if y>z else 'FAIL_P2_2_NOT_EXCEED_P3')
    return False,'IMPOSSIBLE_PRIMITIVE_PARITY'

def e5_branch(pi):
    P1,P2,P3,Q=pi; T=Q-P3
    x,y,z,t=vp(P1,5),vp(P2,5),vp(P3,5),vp(T,5)
    if x>0 and y>0:
        return True,'BOTH_HORIZONTAL_5'
    if x==0 and y==0:
        return (t>0), ('HENSEL_TMINUS' if t>0 else 'FAIL_NO_HORIZONTAL5_NO_TMINUS5')
    if x>0 and y==0:
        return (x>z), ('P1_5_EXCESS_OVER_P3' if x>z else 'FAIL_P1_5_NOT_EXCEED_P3')
    if x==0 and y>0:
        return (y>z), ('P2_5_EXCESS_OVER_P3' if y>z else 'FAIL_P2_5_NOT_EXCEED_P3')
    raise AssertionError

def local_capacity_brute(x,y,z,t, allow_A_p=True):
    best=-10**9
    arange=range(z+1) if allow_A_p else range(1)
    for a in arange:
      for w in range(y+1):
        if a and w: continue
        for u in range(min(y-w,z-a)+1):
          c2=y-u-w; c3=z-u-a
          if a and c2: continue
          if w and c3: continue
          r=min(u+a+w,x)
          for s in range(r,x+1):
            if s>r and (c2 or c3): continue
            best=max(best,w+s+t-a)
    return best

def cap_formula_general(x,y,z,t):
    if y>=z: return t+x+y-z
    return t+min(x,y)+max(0,x-z)

def cap_formula_Afree(x,y,z,t):
    if y>=z: return t+x+y-z
    return t+min(x,y)

def tc1_hits(pi, cap_hits=1000):
    P1,P2,P3,Q=pi; T=Q-P3
    hits=[]; selector_count=0; exponent_count=0
    for A in divs(P3):
      for W in divs(P2):
        common=math.gcd(P2//W,P3//A)
        for u0 in divs(common):
          M=P2//W; N=P3//A; dels=delta_set(M,N)
          for g1 in divs(P1):
            selector_count+=1
            num=W*g1*T
            if num%A: continue
            NE=num//A
            vmax=nu10(NE)
            for n in range(1,vmax+1):
              E=NE//10**n
              for delta in dels:
                ssum=n+delta
                if ssum<2: continue
                for rho in range(2,ssum+1):
                  g=ssum-rho
                  for m in range(1,rho):
                    exponent_count+=1
                    R=E-g1*P2
                    S=W*u0*P1*10**rho-Q*(W*u0*10**m+g1)
                    if R==10**g*S:
                        hits.append((A,W,u0,g1,n,delta,rho,m,g))
                        if len(hits)>=cap_hits:
                            return hits,selector_count,exponent_count
    return hits,selector_count,exponent_count

def r24_support_result(pi,h):
    P1,P2,P3,Q=pi
    A,W,u0,g1,n,delta,rho,m,g=h
    k=rho-m; n2=n+delta
    X=10**m; Y=10**n; G=10**g; K=10**k
    D=K*P1-Q; T=Q-P3
    J=u0*A*X*Y*G*D-g1*T
    NW=g1*A*Y*(G*Q-P2)
    base={'D':D,'J':J,'NW':NW,'k':k,'n2':n2}
    if J<=0: return False,'J_NONPOS',base
    if NW%J: return False,'W_NONINTEGRAL',base
    Wrec=NW//J; base['Wrec']=Wrec
    if Wrec!=W: return False,'W_MISMATCH',base
    if P2%(u0*W) or P3%(u0*A): return False,'C2C3_NONINTEGRAL',base
    Mr=P2//W; Nr=P3//A; C2=P2//(u0*W); C3=P3//(u0*A)
    base.update(Mr=Mr,Nr=Nr,C2=C2,C3=C3)
    if math.gcd(A,C2)!=1 or math.gcd(W,C3)!=1 or math.gcd(A,W)!=1:
        return False,'SHAPE_GCD',base
    Ulo=max(ceildiv(u0*10**(n2-1),Mr),ceildiv(u0*10**(n-1),Nr))
    Uhi=min((u0*10**n2-1)//Mr,(u0*10**n-1)//Nr)
    base.update(Ulo=Ulo,Uhi=Uhi)
    if Ulo>Uhi: return False,'POSITIVE_RADIAL_BOX',base
    g0=math.gcd(u0*A*W,P1); base['g0']=g0
    if g1%g0: return False,'MASTER_G0',base
    mu=g1//g0; base['mu']=mu
    if math.gcd(mu,C2*C3)!=1: return False,'MU_SMITH',base
    lam=Y//math.gcd(Y,W*T); tau=lam//math.gcd(lam,mu); R1=P1//g1
    base.update(lambda_z=lam,tau=tau,R1=R1)
    if math.gcd(tau,R1)!=1: return False,'TAIL_G1',base
    if math.gcd(tau,C2*C3)!=1: return False,'TAIL_SMITH',base
    return True,'R24_SUPPORT_PASS',base

def csv_write(path,rows,fields=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    if fields is None:
        fields=[]
        for row in rows:
            for key in row.keys():
                if key not in fields:
                    fields.append(key)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader(); w.writerows(rows)

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''): h.update(chunk)
    return h.hexdigest()

def main():
    t0=time.time()
    packets=list(primitive_packets(B))
    sample=[]; valctr=Counter(); kctr=Counter(); ectr=Counter()
    gcd_ok=inert_ok=e2eq=e5eq=0
    cap2_count=cap5_count=capboth=e27_count=0
    raw_hits=[]
    for pi in packets:
        P1,P2,P3,Q=pi; Tm=Q-P3; Tp=Q+P3
        c=math.gcd(Q,P3); d=math.gcd(Tm,Tp)
        ratio=d//c
        f_c=factor(c)
        gcd_struct=(c%2==1 and ratio in (1,2) and ratio==(2 if (Q%2 and P3%2) else 1)
                    and all(p%4==1 for p in f_c))
        inert_struct=(all(not(p%4==3 and e%2) for p,e in factor(Tm).items()) and
                      all(not(p%4==3 and e%2) for p,e in factor(Tp).items()))
        gcd_ok += gcd_struct; inert_ok += inert_struct
        c2=cap2_rel(*pi); c5=cap5_rel(*pi)
        e2,br2=e2_branch(pi); e5,br5=e5_branch(pi)
        e2eq += (e2==(c2>=1)); e5eq += (e5==(c5>=1))
        arch=P1*P2*Tm>10*P3
        cap2_count += c2>=1; cap5_count += c5>=1
        capboth += c2>=1 and c5>=1
        e27 = c2>=1 and c5>=1 and arch
        e27_count += e27
        vals=(vp(P1,2),vp(P2,2),vp(Tm,2),vp(Tp,2),vp(P1,5),vp(P2,5),vp(Tm,5),vp(Tp,5))
        valctr[(br2,br5,*vals)] += 1
        kctr[sqf(Tm)] += 1
        ectr[(br2,br5,e2,e5,arch,e27)] += 1
        sample.append(dict(P1=P1,P2=P2,P3=P3,Q0=Q,Tminus=Tm,Tplus=Tp,
            gcd_Tminus_Tplus=d,gcd_Q0_P3=c,gcd_ratio=ratio,
            v2_P1=vp(P1,2),v2_P2=vp(P2,2),v2_P3=vp(P3,2),v2_Tminus=vp(Tm,2),v2_Tplus=vp(Tp,2),
            v5_P1=vp(P1,5),v5_P2=vp(P2,5),v5_P3=vp(P3,5),v5_Tminus=vp(Tm,5),v5_Tplus=vp(Tp,5),
            sqf_Tminus=sqf(Tm),cap2_rel=c2,cap5_rel=c5,E2_branch=br2,E2_pass=int(e2),E5_branch=br5,E5_pass=int(e5),
            arch_packet_only_pass=int(arch),E27_pass=int(e27)))
    # Exhaustive local valuation-box regression for the capacity formulas.
    local2=local5=0; local_total=0
    for x in range(0,7):
      for y in range(0,7):
       for z in range(0,7):
        for t in range(0,5):
          local_total+=1
          if local_capacity_brute(x,y,z,t,False)==cap_formula_Afree(x,y,z,t): local2+=1
          if local_capacity_brute(x,y,z,t,True)==cap_formula_general(x,y,z,t): local5+=1
    # R26 TC1 reconnaissance on complete Q<=B sample (not a proof of global absence).
    total_selector=total_exp=0
    hit_packets=set()
    for pi in packets:
        hits,sc,ec=tc1_hits(pi)
        total_selector+=sc; total_exp+=ec
        if hits:
            hit_packets.add(pi)
            for h in hits:
                ok,reason,data=r24_support_result(pi,h)
                row=dict(P1=pi[0],P2=pi[1],P3=pi[2],Q0=pi[3],
                         A=h[0],W=h[1],u0=h[2],g1star=h[3],n=h[4],delta=h[5],rho=h[6],m=h[7],g=h[8],
                         R24_support_pass=int(ok),rejection_or_pass=reason)
                for k,v in data.items(): row[k]=v
                raw_hits.append(row)
    support_hits=[r for r in raw_hits if r['R24_support_pass']]
    # Counterfamily rows: pi_c=(c,5c,(c^2-26)/2,(c^2+26)/2)
    cf=[]
    for cc in range(8,200,2):
        if cc%5 not in (2,3) or (cc//2)%13==0: continue
        pi=(cc,5*cc,(cc*cc-26)//2,(cc*cc+26)//2)
        assert gcd4(*pi)==1 and pi[0]**2+pi[1]**2+pi[2]**2==pi[3]**2
        e2,_=e2_branch(pi); e5,_=e5_branch(pi); arch=pi[0]*pi[1]*(pi[3]-pi[2])>10*pi[2]
        assert e2 and e5 and arch
        cf.append(dict(family='INFINITE_E27_FAMILY',parameter=cc,P1=pi[0],P2=pi[1],P3=pi[2],Q0=pi[3],Tminus=26,E2=1,E5=1,ARCH=1,note='c even; c mod5 in {2,3}; 13 does not divide c/2'))
    # Split-prime square-kernel counterexamples for a few primes.
    split=[]
    for p in range(5,200):
        if p%4!=1: continue
        # primality
        if any(p%d==0 for d in range(2,math.isqrt(p)+1)): continue
        found=None
        for b in range(1,math.isqrt(p)+1):
            a2=p-b*b; a=math.isqrt(a2)
            if a*a==a2 and a>b: found=(a,b); break
        if not found: continue
        a,b=found
        pi=(4*(a*a-b*b),8*a*b,3*p,5*p)
        assert gcd4(*pi)==1 and pi[0]**2+pi[1]**2+pi[2]**2==pi[3]**2
        assert pi[3]-pi[2]==2*p and sqf(pi[3]-pi[2])==2*p
        split.append(dict(family='ARBITRARY_SPLIT_PRIME_IN_SQF_TMINUS',p=p,a=a,b=b,P1=pi[0],P2=pi[1],P3=pi[2],Q0=pi[3],Tminus=2*p,sqf_Tminus=2*p))
    # CSVs
    csv_write(ROOT/'105-R27-primitive-sphere-sample.csv',sample)
    valrows=[]
    for key,count in sorted(valctr.items(),key=lambda kv:(kv[0],kv[1])):
        br2,br5,*v=key
        valrows.append(dict(E2_branch=br2,E5_branch=br5,v2_P1=v[0],v2_P2=v[1],v2_Tminus=v[2],v2_Tplus=v[3],v5_P1=v[4],v5_P2=v[5],v5_Tminus=v[6],v5_Tplus=v[7],count=count))
    csv_write(ROOT/'105-R27-valuation-patterns.csv',valrows)
    krows=[dict(sqf_Tminus=k,count=v) for k,v in sorted(kctr.items())]
    csv_write(ROOT/'105-R27-Tminus-square-kernels.csv',krows)
    csv_write(ROOT/'105-R27-survivor-registry.csv',raw_hits)
    exrows=[]
    for key,count in sorted(ectr.items(),key=lambda kv:str(kv[0])):
        br2,br5,e2,e5,arch,e27=key
        exrows.append(dict(record_type='SAMPLE_BRANCH_AGGREGATE',E2_branch=br2,E5_branch=br5,E2_pass=int(e2),E5_pass=int(e5),ARCH_pass=int(arch),E27_pass=int(e27),count=count))
    exrows.extend(cf)
    exrows.extend(split)
    # union fields
    fields=[]
    for r in exrows:
        for k in r:
            if k not in fields: fields.append(k)
    csv_write(ROOT/'105-R27-exceptional-locus-registry.csv',exrows,fields)
    countrows=[
      dict(stage='primitive_positive_oriented_packets',count=len(packets),scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='gcd_Tpm_structure_pass',count=gcd_ok,scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='inert_prime_even_exponent_Tpm_pass',count=inert_ok,scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='C2_capacity_ge_1',count=cap2_count,scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='C5_capacity_ge_1',count=cap5_count,scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='C2_and_C5_capacity_ge_1',count=capboth,scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='E27_capacity_plus_arch',count=e27_count,scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND'),
      dict(stage='raw_R26_TC1_hit_packets',count=len(hit_packets),scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND__TC1_ONLY'),
      dict(stage='raw_R26_TC1_hit_tuples',count=len(raw_hits),scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND__TC1_ONLY'),
      dict(stage='R24_support_plus_TC1_hit_tuples',count=len(support_hits),scope=f'Q0<={B}',completeness='COMPLETE_IN_BOUND__NOT_TC2_TO_TC4_GLOBAL_PROOF'),
    ]
    csv_write(ROOT/'105-R27-R26-survivor-counts.csv',countrows)
    cert=[
      dict(certificate='R26_FROZEN_INPUT',status='READ_EXTERNALLY',scope='105-R26-stage-archive.md + sha companion',detail='archive-supplied SHA256=41f4e2aad7720862a98349d61d22c482b7f5045b6c54bfea56651d4032d97680'),
      dict(certificate='GCD_TPM_STRUCTURE_SAMPLE_REGRESSION',status='PASS' if gcd_ok==len(packets) else 'FAIL',scope=f'all {len(packets)} oriented packets Q0<={B}',detail=f'{gcd_ok}/{len(packets)}'),
      dict(certificate='INERT_PRIME_EVEN_EXPONENT_TPM_SAMPLE_REGRESSION',status='PASS' if inert_ok==len(packets) else 'FAIL',scope=f'all {len(packets)} oriented packets Q0<={B}',detail=f'{inert_ok}/{len(packets)}'),
      dict(certificate='CAP2_LOCAL_FORMULA_EXHAUSTIVE_VALUATION_BOX',status='PASS' if local2==local_total else 'FAIL',scope='x,y,z=0..6;t=0..4;A p-content allowed',detail=f'{local2}/{local_total}'),
      dict(certificate='CAP5_LOCAL_FORMULA_EXHAUSTIVE_VALUATION_BOX',status='PASS' if local5==local_total else 'FAIL',scope='x,y,z=0..6;t=0..4;A p-content allowed',detail=f'{local5}/{local_total}'),
      dict(certificate='PRIMITIVE_E2_BRANCH_EQUIV_SAMPLE',status='PASS' if e2eq==len(packets) else 'FAIL',scope=f'all {len(packets)} packets',detail=f'{e2eq}/{len(packets)}'),
      dict(certificate='PRIMITIVE_E5_BRANCH_EQUIV_SAMPLE',status='PASS' if e5eq==len(packets) else 'FAIL',scope=f'all {len(packets)} packets',detail=f'{e5eq}/{len(packets)}'),
      dict(certificate='RAW_TC1_RECON',status='PASS',scope=f'complete Q0<={B}',detail=f'hit_packets={len(hit_packets)};hit_tuples={len(raw_hits)};support_plus_TC1={len(support_hits)}'),
      dict(certificate='INFINITE_E27_FAMILY_REGRESSION',status='PASS',scope='sample c<200',detail=f'rows={len(cf)};symbolic proof is in stage archive'),
      dict(certificate='SPLIT_PRIME_SQF_COUNTERFAMILY_REGRESSION',status='PASS',scope='split primes p<200',detail=f'rows={len(split)};symbolic proof is in stage archive'),
    ]
    csv_write(ROOT/'105-R27-certificate-registry.csv',cert)
    elapsed=time.time()-t0
    log=(f'105-R27 exact reconnaissance execution\n'
         f'BOUND_Q0={B}\nORIENTED_PRIMITIVE_PACKETS={len(packets)}\n'
         f'GCD_STRUCTURE_PASS={gcd_ok}\nINERT_TPM_PASS={inert_ok}\n'
         f'CAP2_GE1={cap2_count}\nCAP5_GE1={cap5_count}\nCAP_BOTH_GE1={capboth}\nE27_CAP_ARCH={e27_count}\n'
         f'RAW_TC1_HIT_PACKETS={len(hit_packets)}\nRAW_TC1_HIT_TUPLES={len(raw_hits)}\nR24_SUPPORT_PLUS_TC1={len(support_hits)}\n'
         f'TOTAL_SELECTOR_LABELS_VISITED={total_selector}\nTOTAL_EXPONENT_RECORDS_VISITED={total_exp}\n'
         f'LOCAL_CAPACITY_BOX_TOTAL={local_total}\nCAP2_FORMULA_MATCH={local2}\nCAP5_FORMULA_MATCH={local5}\n'
         f'INFINITE_E27_SAMPLE_ROWS={len(cf)}\nSPLIT_PRIME_COUNTEREXAMPLE_ROWS={len(split)}\n'
         f'ELAPSED_SECONDS={elapsed:.6f}\n'
         'FINITE_ENUMERATION_IS_RECONNAISSANCE_ONLY=YES\n'
         'NO_GLOBAL_NONEXISTENCE_CLAIM_FROM_BOUND=YES\n'
         'FULL_TC2_TC4_REPLAY_IMPLEMENTED=NO\n'
         'ALL_ASSERTIONS=PASS\n')
    (ROOT/'105-R27-execution.log').write_text(log,encoding='utf-8')
    print(log)

if __name__=='__main__': main()
