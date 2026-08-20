#!/usr/bin/env python3
"""R7 low-k ledger after the carry-index dependency audit.

Double q-descent is recorded only conditionally on the stabilized reverse carry residual Gamma_R=0.
"""
from math import gcd
K1=[7,11,13,17,19,23,29,47,49,59,61,73,77,89,91,97,101,103,109,113]
K2=[7,11]
Q1=[1,2,3]

def vp(n,p):
 c=0
 while n%p==0:c+=1;n//=p
 return c

def cfun(q):return q**3+10*q*q+12*q+8

def row(k,q):
 b=vp(q+4,5);d0=2*5**b;c=cfun(q)
 a_unit_ok=(q%5)!=3
 active=(k>b) and a_unit_ok
 scale=(10**k)//d0 if active else None
 status=('CLOSED_A_TENUNIT' if not a_unit_ok else ('OPEN_EXACT_CARRY_RESIDUAL_K_SCALE' if active else 'OPEN_DEEP5_PREPROCESSING'))
 return dict(k=k,q=q,b=b,active_tail_scope=active,v5_c=vp(c,5),tail_scale=scale,
             q_descent_1='CONDITIONAL_GAMMA_R_ZERO' if active else 'N/A',
             q_descent_2='CONDITIONAL_AFTER_QD1' if active else 'N/A',
             status=status)

print('k\tq\tb\tactive_tail_scope\tv5(c)\ttail_scale(K/d0)\tq_descent_1\tq_descent_2\tstatus')
for k,qs in [(1,K1),(2,K2)]:
 for q in qs:
  r=row(k,q)
  print('{k}\t{q}\t{b}\t{active_tail_scope}\t{v5_c}\t{tail_scale}\t{q_descent_1}\t{q_descent_2}\t{status}'.format(**r))
for k in Q1:
 print(f'{k}\t1\t-\tQ1_SPECIAL\t-\t-\tN/A\tN/A\tOPEN_Q1_EXACT_ROOT_CONGRUENCE')

# Frozen deep-5 exceptions for k=1.
deep=[q for q in K1 if vp(q+4,5)>=1]
assert deep==[11,61,91,101],deep
print('DEEP5_K1=',deep)
closed_a=[q for q in K1 if q%5==3]
assert closed_a==[13,23,73,103,113],closed_a
print('A_TENUNIT_CLOSED_K1=',closed_a)
active_k1=[q for q in K1 if q%5!=3 and vp(q+4,5)==0]
print('ACTIVE_K1_AFTER_SCOPE=',active_k1,'COUNT=',len(active_k1))
# Correct c-unit audit: global c-ten-unit is false.
assert cfun(7)==925 and vp(cfun(7),5)==2
print('C_TENUNIT_GLOBAL=FALSE; q=7 gives c=925, v5(c)=2')
print('REVERSE_EXACT_FRONTIER: K divides 2*d0*q^2*t*(q+4)*Gamma_R')
print('DOUBLE_DESCENT: VALID ONLY IF Gamma_R=0 (stabilized fixed-depth branch)')
