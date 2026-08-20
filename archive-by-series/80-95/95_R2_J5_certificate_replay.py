#!/usr/bin/env python3
from __future__ import annotations
import argparse, gzip, hashlib, json, math
from collections import Counter
from pathlib import Path

MODS=(64,63,65,11,13,17,19,23,29,31)
SQRES={m:{x*x%m for x in range(m)} for m in MODS}
FAMILIES={2:dict(J=5,dstar=2,beta=40,kmax=8),3:dict(J=5,dstar=4,beta=800,kmax=12)}

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def square_status(n):
    if n<0: return 'D',None,'NEGATIVE_DISCRIMINANT'
    for m in MODS:
        if n%m not in SQRES[m]: return 'N',None,'NON_SQUARE_MODULAR_CERTIFICATE'
    r=math.isqrt(n)
    if r*r!=n: return 'N',None,'NON_SQUARE_EXACT_ISQRT'
    return 'S',r,'SQUARE'

def iter_base_states(g):
    cfg=FAMILIES[g]; G=10**g; Kstar=G//cfg['dstar']
    for u0 in divisors(G+1):
        A0=u0*cfg['J']+cfg['dstar']
        for C3 in range(1,G):
            for W in range(1,(u0*C3-1)//Kstar+1):
                d2=u0*C3-Kstar*W
                yield u0,C3,W,d2,A0

def classify(g,u0,C3,W,d2,A0,k):
    cfg=FAMILIES[g]; G=10**g; J=cfg['J']; g1=cfg['beta']*G; tenk=10**k
    x=d2*u0*J*tenk
    delta=x*x-A0*A0*(d2*d2+(u0*C3)**2)+2*A0*d2*W
    code,r,detail=square_status(delta)
    if code!='S': return code,detail,None
    denom=A0*g1; nums=(x+r,x-r); ok=tuple(n>0 and n%denom==0 for n in nums)
    if any(ok):
        roots=tuple(n//denom if good else None for n,good in zip(nums,ok))
        return 'P','INTEGRAL_C1_SURVIVOR',dict(delta=delta,sqrt=r,denom=denom,numerators=nums,roots=roots)
    return 'I','SQUARE_BUT_ROOT_DIVISIBILITY_FAIL',dict(delta=delta,sqrt=r,denom=denom,numerators=nums)

def sha256_file(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--outdir',default='.'); a=ap.parse_args(); out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True)
    ledger=out/'95_R2_J5_rejection_ledger.tsv'; near=out/'95_R2_J5_near_survivors.tsv'; cert=out/'95_R2_J5_certificate.json'
    uh=hashlib.sha256(); header='g\tu0\tC3\tW\td2\tk_reason_codes\n'; uh.update(header.encode()); results={}; near_rows=[]
    with ledger.open('wb', buffering=8<<20) as gz:
        gz.write(header.encode())
        for g in (2,3):
            cfg=FAMILIES[g]; base=expanded=surv=0; rc=Counter(); dc=Counter()
            for u0,C3,W,d2,A0 in iter_base_states(g):
                base+=1; codes=[]
                for k in range(1,cfg['kmax']+1):
                    code,detail,payload=classify(g,u0,C3,W,d2,A0,k); codes.append(code); expanded+=1; rc[code]+=1; dc[detail]+=1
                    if code in ('I','P'):
                        near_rows.append(dict(g=g,u0=u0,C3=C3,W=W,d2=d2,k=k,code=code,detail=detail,**payload))
                    if code=='P': surv+=1
                line=f"{g}\t{u0}\t{C3}\t{W}\t{d2}\t{''.join(codes)}\n".encode(); gz.write(line); uh.update(line)
            results[str(g)]={'G':10**g,'J':cfg['J'],'dstar':cfg['dstar'],'beta':cfg['beta'],'g1':cfg['beta']*(10**g),'u0_divisors':divisors(10**g+1),'C3_range':[1,10**g-1],'k_range':[1,cfg['kmax']],'base_states':base,'expanded_base_k_states':expanded,'reason_code_counts':dict(rc),'detail_counts':dict(dc),'integral_C1_survivors':surv}
    with near.open('w',encoding='utf-8',newline='\n') as f:
        f.write('g\tu0\tC3\tW\td2\tk\tcode\tdelta\tsqrt\tdenom\tnum_plus\tnum_minus\n')
        for r in near_rows:
            f.write(f"{r['g']}\t{r['u0']}\t{r['C3']}\t{r['W']}\t{r['d2']}\t{r['k']}\t{r['code']}\t{r['delta']}\t{r['sqrt']}\t{r['denom']}\t{r['numerators'][0]}\t{r['numerators'][1]}\n")
    certificate={
      'project':'三项十进制拼接平方和问题 / Strict Layer A1 / 95-R2',
      'scope':'J=5 positive exact-resonance residual families H_5,2 and H_5,3 only',
      'status_before_replay':'CLAIMED_BUT_CERTIFICATE_NOT_RECOVERED','status_after_replay':'REPLAY_CERTIFIED_CLOSED_POSITIVE_HALVES','arithmetic':'integer-only; no floating point',
      'coverage_basis':{
        'H_5,2':'g=n3=2, d*=2, beta=40, u=u0|101; C3 in [1,99]; d2=u0*C3-50W>0; inherited k<=8',
        'H_5,3':'g=n3=3, d*=4, beta=800, u=u0|1001; C3 in [1,999]; d2=u0*C3-250W>0; inherited k<=12',
        's_projection_note':'For H_5,2, s in {1,2} is absent from the primitive discriminant/root necessary gate; both source s-cases project to the same replay state space.',
        'g1_derivation':'resonance t=1; u=u0 and gcd(u0,10)=1 imply gamma=1, v0=10^g, hence g1=beta*10^g.'},
      'necessary_gate':{'A0':'u0*J+dstar','d2':'u0*C3-(10^g/dstar)*W > 0','DeltaPrime':'(d2*u0*J*10^k)^2 - A0^2*(d2^2+(u0*C3)^2) + 2*A0*d2*W','root':'C1=(d2*u0*J*10^k ± sqrt(DeltaPrime))/(A0*g1) must be a positive integer'},
      'reason_code_legend':{'D':'negative discriminant','N':'exactly certified non-square discriminant','I':'square discriminant but both C1 root numerators fail positive integrality/divisibility','P':'positive integral C1 survivor (must be replayed against original equation)'},
      'canonical_order':'g ascending; u0 ascending divisors of 10^g+1; C3 ascending; W ascending; k encoded left-to-right from 1 to kmax',
      'families':results,'near_survivors':near_rows,'original_equation_replay':'VACUOUS: zero positive integral C1 survivors reach the original-equation replay stage.',
      'conclusion':{'H_5,2_intersect_SR_positive':'EMPTY','H_5,3_intersect_SR_positive':'EMPTY'},'canonical_uncompressed_rejection_ledger_sha256':uh.hexdigest()}
    cert.write_text(json.dumps(certificate,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    manifest=out/'95_R2_J5_SHA256SUMS.txt'; files=[Path(__file__).resolve(),ledger,near,cert]; manifest.write_text(''.join(f"{sha256_file(p)}  {p.name}\n" for p in files),encoding='utf-8')
    print(json.dumps({'status':certificate['status_after_replay'],'families':{g:{'base_states':v['base_states'],'expanded':v['expanded_base_k_states'],'reasons':v['reason_code_counts'],'integral_C1_survivors':v['integral_C1_survivors']} for g,v in results.items()},'near_survivors':near_rows,'ledger_uncompressed_sha256':uh.hexdigest(),'ledger_file_sha256':sha256_file(ledger),'certificate_sha256':sha256_file(cert)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
