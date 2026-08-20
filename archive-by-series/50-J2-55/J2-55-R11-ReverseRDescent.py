#!/usr/bin/env python3
"""R11 reverse R-descent audit: exposes the structural R factor and low-k scope."""
from math import gcd,lcm
from pathlib import Path
import csv
import sympy as sp

OUT=Path('/mnt/data')
q,R,f,w,e,chR,s,t=sp.symbols('q R f w e chR s t', integer=True)
PR=(2*chR*q**2
+e*(R**2*q**4+10*R**2*q**3+12*R**2*q**2+8*R**2*q+2*q**5+12*q**4)
+s*(8*R**2*f*q**7+112*R**2*f*q**6+416*R**2*f*q**5+448*R**2*f*q**4+256*R**2*f*q**3)
+t*(-8*R**3*f*q**6-88*R**3*f*q**5-272*R**3*f*q**4-416*R**3*f*q**3
   +512*R**3*f*q+256*R**3*f-4*R*f*q**7+192*R*f*q**5+192*R*f*q**4
   -448*R*f*q**3-256*R*f*q**2))
CR=4*R*f**2*w*PR
low=sp.factor(4*f**2*w*PR.subs(R,0))
assert low==8*f**2*q**2*w*(chR+e*q**3+6*e*q**2)

def vp(n,p):
    v=0
    while n and n%p==0:v+=1;n//=p
    return v
def ordmod(a,m):
    if m==1:return 1
    x=1
    for d in range(1,1000000):
        x=x*a%m
        if x==1:return d
    raise RuntimeError
def split10(m):
    a=b=0
    while m%2==0:a+=1;m//=2
    while m%5==0:b+=1;m//=5
    return a,b,m
def eventual(qv,k,mod):
    a,b,unit=split10(mod); stab=max(a,b,1)
    T=lcm(ordmod(10,qv),ordmod(10,unit) if unit>1 else 1)
    out=[]
    for rr in range(T):
        rv=stab+rr
        if pow(10,rv+k,qv)==qv-1:
            out.append((rr,pow(10,rv,mod)))
    return stab,T,out

rows=[]
ACTIVE=[7,17,19,29,47,49,59,77,89,97,109]
# k=1,b=0 has the special R10 normalization 2(q+4)eta1=...
# The generic reverse third core used to derive CR is not legal here.
for qv in ACTIVE:
    D=2*(qv+4); tm=lcm(D,10)
    stab,T,Rs=eventual(qv,1,D)
    cell=0
    for rr,Rm in Rs:
        for tr in range(tm):
            if tr%2==0 or tr%5: continue
            er=(-8*Rm*(tr%D)*(3*qv+5))%D
            rows.append(dict(type='ACTIVE_SPECIAL_K1',q=qv,k=1,cell=cell,
                R_degree='',R_order='',lowest_R_coefficient='',
                R_divisibility='GENERIC_CR_NOT_LEGAL',
                r_bound='',status='OPEN_SPECIAL_THIRD_CORE_REQUIRED'))
            cell+=1

# k=2 legal generic RTQR types.
for qv,fv,wv,label in [(7,1,25,'ACTIVE_K2_Q7'),(11,5,1,'ACTIVE_K2_Q11')]:
    # K/(4 f^2 w)=1 in both cases: constant-term gate is tautologically Du=PR.
    K=100
    assert K==4*fv*fv*wv
    D=(qv+4)//fv
    tm=lcm(D,50 if qv==7 else 10)
    stab,T,Rs=eventual(qv,2,D)
    cell=0
    for rr,Rm in Rs:
        for tr in range(tm):
            if qv==7 and (tr%2==0 or tr%25): continue
            if qv==11 and gcd(tr,10)!=1: continue
            rows.append(dict(type=label,q=qv,k=2,cell=cell,
                R_degree=4,R_order=1,
                lowest_R_coefficient=str(low.subs({q:qv,f:fv,w:wv})),
                R_divisibility='STRUCTURAL_R_CANCELS; K/(4f^2w)=1',
                r_bound='',status='OPEN_CONSTANT_TERM_GATE_TAUTOLOGICAL'))
            cell+=1

for qv in [11,61,91,101]:
    rows.append(dict(type='DEEP5',q=qv,k=1,cell='',
        R_degree='',R_order='',lowest_R_coefficient='',
        R_divisibility='GENERIC_RTQR/THIRD_CORE_FORBIDDEN',
        r_bound='',status='OPEN_PREVALUATION'))

p=OUT/'J2-55-R11-reverse-r-certificate.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
    fields=['type','q','k','cell','R_degree','R_order','lowest_R_coefficient',
            'R_divisibility','r_bound','status']
    wri=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t')
    wri.writeheader();wri.writerows(rows)

print('GENERIC_REVERSE_C_R_ORDER=1')
print('GENERIC_LOWEST=',low)
print('R_DIV_C_DEPTH_KILLER=FALSE_STRUCTURALLY')
print('CORRECT_NORMALIZED_GATE=K*Du_R=4*f^2*w*P_R(R)')
print('K2_Q7_COFactor=1')
print('K2_Q11_COFactor=1')
print('K1_SPECIAL_GENERIC_CR_SCOPE=FORBIDDEN')
print('ROWS=',len(rows))
print('CERT=',p.name)
