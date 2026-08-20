#!/usr/bin/env python3
"""R8 reverse low-k DTF1 ledger.
Exact theorem-only output; no illegal use on deep-5 k=1 exceptions.
"""
from math import gcd
import csv
from pathlib import Path
OUT=Path(__file__).resolve().parent
K1_ACTIVE=[7,17,19,29,47,49,59,77,89,97,109]
K1_DEEP=[11,61,91,101]
K1_DEAD=[13,23,73,103,113]
K2=[7,11]
Q1=[1,2,3]

def vp(n,p):
 c=0
 while n and n%p==0:c+=1;n//=p
 return c

def cfun(q):return q**3+10*q*q+12*q+8

def row(k,q,scope):
 b=vp(q+4,5) if q>1 else None
 c=cfun(q) if q>1 else None
 v5c=vp(c,5) if q>1 else None
 forced='NONE'
 norm='NONE'
 status='OPEN_EXPLICIT_TYPE'
 if scope=='ACTIVE':
  e5=max(k-2*b,0);e2=max(k-2,0)
  if b==0 and e5>0:
   # 5^e5 | c*a3+q^2*t. If e5<=v5(c), force same 5^e5 into t.
   forced=f'5^{min(e5,v5c)}|t' if min(e5,v5c)>0 else 'NONE'
   if k==1:
    norm='lambda_R=(c*a3+q^2*t)/5; omega_R=2(q+4)lambda_R; lambda_R=4t mod q'
   elif k==2 and b==0:
    norm='lambda_R=(c*a3+q^2*t)/25; omega_R=(q+4)lambda_R; lambda_R=8t mod q'
  elif k>=2 and k>=2*b:
   norm='lambda_R=(c*a3+q^2*t)/(2^(k-2)5^(k-2b)); omega_R=((q+4)/5^b)lambda_R'
  if k==2 and q==7:
   assert v5c==2; forced='25|t'
  if k==2 and q==11:
   forced='NONE_FROM_R_DT5 (k-2b=0)'
 elif scope=='DEEP5':
  forced='ACTIVE_TAIL_DTF1_NOT_LEGAL; USE_PRE_VALUATION_RELATION'
  norm='NONE'
 elif scope=='A_TENUNIT_CLOSED':
  status='CLOSED_R7_A_TENUNIT'
 elif scope=='Q1':
  b=c=v5c=''
  forced='GENERIC_Q_TAIL_NOT_APPLICABLE'
  norm='Q1_FIXED_K_EUCLIDEAN/DCDC_ONLY'
 return dict(k=k,q=q,b=b,v5_c=v5c,DTF1_scope=scope,forced_v5_t=forced,normalized_tail=norm,status=status)

def main():
 rows=[]
 for q in K1_ACTIVE:rows.append(row(1,q,'ACTIVE'))
 for q in K1_DEEP:rows.append(row(1,q,'DEEP5'))
 for q in K1_DEAD:rows.append(row(1,q,'A_TENUNIT_CLOSED'))
 for q in K2:rows.append(row(2,q,'ACTIVE'))
 for k in Q1:rows.append(row(k,1,'Q1'))
 for x in rows:print(x)
 assert all('5^1|t' in x['forced_v5_t'] for x in rows if x['k']==1 and x['DTF1_scope']=='ACTIVE')
 q7=next(x for x in rows if x['k']==2 and x['q']==7); assert q7['forced_v5_t']=='25|t'
 path=OUT/'J2-55-R8-lowk-ledger.tsv'
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),delimiter='\t');w.writeheader();w.writerows(rows)
 print('ACTIVE_K1_B0_5_DIV_T=PROVED_FOR_11_TYPES')
 print('K2_Q7_25_DIV_T=PROVED')
 print('K2_Q11=NO_NEW_5_CONTENT_FROM_DTF1')
 print('DEEP5_K1=4_EXPLICIT_PREVALUATION_TYPES')
 print('Q1_REVERSE=3_EXPLICIT_TYPES')
 print('LEDGER_FILE='+path.name)
if __name__=='__main__':main()
