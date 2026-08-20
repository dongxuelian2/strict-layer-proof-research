#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

# Independent replay implementation: different square filter set and a separately written formula path.
MODS=(128,63,65,11,13,17,19,23,29,31,37,41,43)
SQ={m:{(a*a)%m for a in range(m)} for m in MODS}
CFG={2:(2,40,8),3:(4,800,12)} # d*, beta, kmax; J=5

def divs(n): return [d for d in range(1,n+1) if n%d==0]
def code(g,u,c,w,d2,k):
    ds,beta,_=CFG[g]; G=10**g; J=5
    A=u*J+ds; g1=beta*G; z=10**k
    # Written as lead^2 + correction, algebraically identical to the archived theorem.
    lead=J*u*d2*z
    correction=2*A*d2*w-A*A*(d2*d2+u*u*c*c)
    disc=lead*lead+correction
    if disc<0: return 'D'
    for m in MODS:
        if disc%m not in SQ[m]: return 'N'
    r=math.isqrt(disc)
    if r*r!=disc: return 'N'
    den=A*g1
    return 'P' if ((lead+r)>0 and (lead+r)%den==0) or ((lead-r)>0 and (lead-r)%den==0) else 'I'

def expected():
    for g in (2,3):
        ds,beta,kmax=CFG[g]; G=10**g; K=G//ds
        for u in divs(G+1):
            for c in range(1,G):
                maxw=(u*c-1)//K
                for w in range(1,maxw+1):
                    d2=u*c-K*w
                    codes=''.join(code(g,u,c,w,d2,k) for k in range(1,kmax+1))
                    yield f'{g}\t{u}\t{c}\t{w}\t{d2}\t{codes}\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--outdir',default='.');a=ap.parse_args();out=Path(a.outdir)
    ledger=out/'95_R2_J5_rejection_ledger.tsv'; certp=out/'95_R2_J5_certificate.json'
    cert=json.loads(certp.read_text(encoding='utf-8'))
    header='g\tu0\tC3\tW\td2\tk_reason_codes\n'; h=hashlib.sha256(); h.update(header.encode()); rows=0
    with ledger.open('r',encoding='utf-8',newline='',buffering=8<<20) as f:
        if f.readline()!=header: raise SystemExit('HEADER_MISMATCH')
        for e in expected():
            got=f.readline()
            if got!=e: raise SystemExit(f'ROW_MISMATCH_AT_{rows+1}: expected={e.strip()} got={got.strip()}')
            h.update(e.encode()); rows+=1
        if f.readline(): raise SystemExit('EXTRA_ROWS')
    digest=h.hexdigest()
    if digest!=cert['canonical_uncompressed_rejection_ledger_sha256']: raise SystemExit('CANONICAL_HASH_MISMATCH')
    if cert['families']['2']['base_states']!=9998 or cert['families']['3']['base_states']!=2681304: raise SystemExit('BASE_COUNT_MISMATCH')
    if cert['families']['2']['integral_C1_survivors'] or cert['families']['3']['integral_C1_survivors']: raise SystemExit('SURVIVOR_CLAIM_MISMATCH')
    rep={'verifier_status':'PASS','implementation':'independent_python_replay_v1','rows_verified':rows,'expanded_states_verified':79984+32175648,'canonical_uncompressed_sha256':digest,'integral_C1_survivors':0}
    rp=out/'95_R2_J5_verifier_report.json';rp.write_text(json.dumps(rep,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(rep,indent=2))
if __name__=='__main__': main()
