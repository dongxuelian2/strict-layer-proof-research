#!/usr/bin/env python3
"""R11 G-constant structural gate / pseudo-survivor audit.
This is NOT a replacement for the R10 79-state replay; those historical states
already die before THIRD_CORE.  It tests the new gate itself and falsifies an
over-strong small-cofactor conjecture under the currently frozen algebraic gates.
"""
from pathlib import Path
import csv
OUT=Path('/mnt/data')

def c(q): return q**3+10*q*q+12*q+8
def PB(q,f,e,ch,s,t):
    return (2*ch*q*q
      +e*(2*q**5+13*q**4+10*q**3+12*q**2+8*q)
      +s*(8*f*q**7+112*f*q**6+416*f*q**5+448*f*q**4+256*f*q**3)
      +t*(-4*f*q**7-8*f*q**6+104*f*q**5-80*f*q**4-864*f*q**3
          -256*f*q**2+512*f*q+256*f))
def CB(q,f,w,e,ch,s,t): return -4*f*f*w*PB(q,f,e,ch,s,t)

# q=19,g=9 is a legal cyclotomic exponent class: 19 | 10^9+1.
# b=0, v5(c)=1, t=5.  e=384 is the exact R10 e-CRT class mod c/5=2141.
row=dict(kind='BOUNDARY_PSEUDO',g=9,k=9,delta=0,q=19,b=0,t=5,e=86024,s=0,
         chi=19*24612650,rcenter='',Au='',A0='')
G=10**row['g']; f=1; w=5; ch=row['chi']//row['q']
C=CB(row['q'],f,w,row['e'],ch,row['s'],row['t'])
assert (G+1)%row['q']==0
assert (row['e']+8*f*row['t']*(3*row['q']+5))%(row['q']+4)==0
eta=(row['e']+8*f*row['t']*(3*row['q']+5))//(row['q']+4)
lam=8*f*f*row['t']+row['q']*eta
assert lam>0
assert row['e']%(c(row['q'])//5)==384
B=(row['q']+2)*(row['q']**2-4*row['q']-4)
alpha=2*f*B*row['t']-row['q']*row['e']
assert abs(alpha)<30*row['q']**4
assert C%G==0
Du=C//G
assert abs(Du)>row['q']
row.update(C=C,C_div_G='PASS',Du=Du,Du_mod_q=Du%row['q'],
           xi_reconstructed='',u=(G+1)//row['q'],G_candidate=G,
           root_status='PSEUDO_TQR_ECRT_GDIVC_NOT_FULL_RCE_DCDC',
           first_failure='SMALL_COFACTOR_LT_Q_FALSE')

fields=['kind','g','k','delta','q','b','t','e','s','chi','rcenter','Au','A0',
        'C','C_div_G','Du','Du_mod_q','xi_reconstructed','u','G_candidate',
        'root_status','first_failure','R','C_R_order','C_R_lowest','r_bound']
p=OUT/'J2-55-R11-survivors.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
    wri=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t',extrasaction='ignore')
    wri.writeheader();wri.writerow(row)

print('GATE_ORDER=INPUT,TAIL,RCE,DCDC,TQR,CARRY_CORE,THIRD_CORE,C_BUILD,G_DIV_C,D_COF,XI_RECON,ROOT_INTERVAL,LINEAR_ROOT,FULL_ROOT')
print('R10_HISTORICAL_79_REACH_THIRD_CORE=0 (frozen R10 result; not re-inferred here)')
print('CONSTANT_TERM_PSEUDO_SURVIVOR=',row)
print('UNIFORM_|Du|<q_FROM_CURRENT_CONSTANT_TERM_GATES=FALSE')
print('SURVIVOR_FILE=',p.name)
