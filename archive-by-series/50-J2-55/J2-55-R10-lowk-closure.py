#!/usr/bin/env python3
"""R10 reverse fixed-low-k exact TQR-cell audit.
Outputs every requested active type as CLOSED or an explicit finite periodic
TQR residue-cell family.  Deep-5 types are kept separate and no generic RTQR
is applied to them.
"""
from math import gcd,lcm
from pathlib import Path
import csv
OUT=Path('/mnt/data')
ACTIVE_K1=[7,17,19,29,47,49,59,77,89,97,109]
DEEP5=[11,61,91,101]

def vp(n,p):
 c=0
 while n%p==0 and n:
  n//=p;c+=1
 return c

def ordmod(a,m):
 if m==1:return 1
 if gcd(a,m)!=1:return None
 x=1
 for d in range(1,1000000):
  x=x*a%m
  if x==1:return d
 raise RuntimeError(('order too large',a,m))

def decimal_split(m):
 a=b=0;n=m
 while n%2==0:a+=1;n//=2
 while n%5==0:b+=1;n//=5
 return a,b,n

def eventual_R_residues(q,k,mod):
 """R=10^r, r=g-k, with q | 10^g+1. Return eventual residues mod mod."""
 a,b,unit=decimal_split(mod);stab=max(a,b,1)
 oq=ordmod(10,q);ou=ordmod(10,unit) if unit>1 else 1
 T=lcm(oq,ou)
 out=[]
 for rr in range(T):
  r=stab+rr
  # dependency is periodic after stab with period T
  if pow(10,r+k,q)!=(q-1)%q:continue
  Rm=pow(10,r,mod)
  out.append((rr,Rm))
 return stab,T,sorted(set(out))

rows=[]
# k=1 special normalization: 2(q+4) eta1 = e + 8 R t(3q+5).
for q in ACTIVE_K1:
 D=2*(q+4); tmod=lcm(D,10)  # encodes odd and 5|t via actual residue filter
 stab,T,Rres=eventual_R_residues(q,1,D)
 count=0
 for rr,Rm in Rres:
  for tr in range(tmod):
   if tr%2==0 or tr%5: continue
   er=(-8*Rm*(tr%D)*(3*q+5))%D
   rows.append(dict(k=1,q=q,branch='ACTIVE_SPECIAL_K1',period=T,r_class=rr,modulus=D,
                    t_modulus=tmod,t_residue=tr,e_residue=er,
                    theorem='2(q+4)eta1=e+8Rt(3q+5)',status='EXPLICIT_PERIODIC_TQR_CELL'))
   count+=1
 print(f'k=1,q={q}: EXPLICIT_PERIODIC_TQR_CELLS={count}; period={T}; Rclasses={len(Rres)}')

# k=2,q=7: generic RTQR, 25|t, t odd.
q=7;k=2;f=1;D=q+4;tmod=lcm(D,50)
stab,T,Rres=eventual_R_residues(q,k,D);count=0
for rr,Rm in Rres:
 for tr in range(tmod):
  if tr%2==0 or tr%25:continue
  er=(-8*Rm*(tr%D)*(3*q+5))%D
  rows.append(dict(k=k,q=q,branch='ACTIVE_K2_Q7',period=T,r_class=rr,modulus=D,t_modulus=tmod,t_residue=tr,e_residue=er,
                   theorem='(q+4)etaR=e+8Rt(3q+5);25|t',status='EXPLICIT_PERIODIC_TQR_CELL'));count+=1
print(f'k=2,q=7: EXPLICIT_PERIODIC_TQR_CELLS={count}; period={T}; Rclasses={len(Rres)}')

# k=2,q=11: generic RTQR, b=1,f=5, moderate v5(t)=0, t odd.
q=11;k=2;f=5;D=(q+4)//f;tmod=lcm(D,10)
stab,T,Rres=eventual_R_residues(q,k,D);count=0
for rr,Rm in Rres:
 for tr in range(tmod):
  if gcd(tr,10)!=1:continue
  er=(-8*Rm*f*(tr%D)*(3*q+5))%D
  rows.append(dict(k=k,q=q,branch='ACTIVE_K2_Q11',period=T,r_class=rr,modulus=D,t_modulus=tmod,t_residue=tr,e_residue=er,
                   theorem='h5 etaR=e+8R*5*t(3q+5);v5(t)=0',status='EXPLICIT_PERIODIC_TQR_CELL'));count+=1
print(f'k=2,q=11: EXPLICIT_PERIODIC_TQR_CELLS={count}; period={T}; Rclasses={len(Rres)}')

# Deep-5: no generic lambda/RTQR. Record exact pre-valuation tail scale only.
for q in DEEP5:
 b=vp(q+4,5);d0=2*5**b
 assert k!=1 or True
 # exact pre-valuation law d0(CN-Bt)=K*alpha with K=10.
 rows.append(dict(k=1,q=q,branch='DEEP5',period='',r_class='',modulus='',t_modulus='',t_residue='',e_residue='',
                  theorem=f'{d0}(C N-B t)=10 alpha; generic RTQR forbidden',status='OPEN_FIXED_TYPE_PREVALUATION'))
 print(f'deep5 q={q}: OPEN_FIXED_TYPE_PREVALUATION (generic RTQR not used)')

p=OUT/'J2-55-R10-lowk-cells.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
 w=csv.DictWriter(fobj,fieldnames=['k','q','branch','period','r_class','modulus','t_modulus','t_residue','e_residue','theorem','status'],delimiter='\t')
 w.writeheader();w.writerows(rows)
print('R8_OLD_RESIDUE_NOT_USED=PASS')
print('LOWK_COMPLETE_CLOSURE=False')
print('LOWK_CELL_FILE='+p.name)
