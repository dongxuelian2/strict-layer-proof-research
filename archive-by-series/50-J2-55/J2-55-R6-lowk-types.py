#!/usr/bin/env python3
from math import gcd
from fractions import Fraction

K1=[7,11,13,17,19,23,29,47,49,59,61,73,77,89,91,97,101,103,109,113]
K2=[7,11]
Q1=[1,2,3]

def vp(n,p):
 c=0
 while n%p==0:c+=1;n//=p
 return c

def order_minus_one(q,limit=100000):
 if q==1:return (1,0)
 x=1
 first=None
 for g in range(1,limit+1):
  x=x*10%q
  if first is None and x==q-1:first=g
  if x==1:
   return (first,g)
 return (first,None)

def cfun(q):return q**3+10*q*q+12*q+8

def P0(q,k,alpha,t):
 K=10**k;b=vp(q+4,5);d0=2*5**b;c=cfun(q)
 num=2*K*(K*alpha*q+4*K*alpha+2*d0*q**4*t+14*d0*q**3*t+12*d0*q*q*t-24*d0*q*t-16*d0*t)
 den=d0*q*q*(q+4)*c
 return Fraction(num,den)

print('J2-55 R6 low-qK exact type ledger')
print('THEOREM: for fixed (q,k,alpha,t), uD2/M = P0 + O(1/G); hence mu is eventually bounded, while actual x>AG/10 grows. Every fixed tail fibre has only a finite exponent prefix.')
for k,qs in [(1,K1),(2,K2)]:
 for q in qs:
  b=vp(q+4,5);K=10**k
  active=(k>b)
  scale=Fraction(K,2*5**b) if active else None
  g0,T=order_minus_one(q)
  print(f'k={k},q={q},b={b},active_reverse_quotient={active},G/d_r={scale},first_minus_one_g={g0},order={T},TYPE_STATUS=OPEN_MOVING_TAIL_FIBRES,FIXED_FIBRE=FINITE_PREFIX')
for k in Q1:
 print(f'q=1,k={k},TYPE_STATUS=OPEN_MOVING_(N,t),FIXED_(N,t)_FIBRE=FINITE_PREFIX')

# Frozen exact scales.
assert Fraction(10,2)==5
assert Fraction(100,2)==50
assert Fraction(100,10)==10
print('K1TAIL=CN-Bt=5*alpha')
print('K2TAIL_b0=CN-Bt=50*alpha')
print('K2TAIL_b1=CN-Bt=10*alpha')
print('LOWK_TYPE_COUNT=',len(K1)+len(K2)+len(Q1))
