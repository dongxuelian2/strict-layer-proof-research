#!/usr/bin/env python3
"""R14 q=1 equal-valuation Gaussian support second-lift certificate."""
import csv
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
G,a,tau=sp.symbols('G a tau', integer=True)
M=G**3*tau-(10*G**2+4*G-2)*a
lin1=tau+4*a
lin2=27*tau+116*a
U1=sp.cancel((M+lin1)/(G+1))
U2=sp.cancel((8*M+lin2)/(2*G+3))
assert sp.denom(U1)==1 and sp.denom(U2)==1
assert sp.expand(M+lin1-(G+1)*U1)==0
assert sp.expand(8*M+lin2-(2*G+3)*U2)==0
# First-order support residues.
assert sp.expand(U1.subs(G,-1)-4*a-3*lin1)==0
# Polynomial remainder: U2+12a reduces exactly to lin2 modulo 2G+3.
assert sp.rem(sp.expand(U2+12*a-lin2),2*G+3,G)==0

# Equal valuation second lifts, written without introducing quotient variables:
# l1 == 4a*g1 (mod p) <=> lin1 == 4a(G+1) (mod p^{h+1}).
raw1=sp.expand(lin1-4*a*(G+1))
assert raw1==tau-4*a*G
# l2 == -12a*g2 (mod p) <=> lin2 == -12a(2G+3) mod p^{h+1}.
raw2=sp.expand(lin2+12*a*(2*G+3))
assert raw2==27*tau+24*a*G+152*a

rows=[
 dict(support='G+1',p_class='3 mod 4',equal_valuation_h='h>=1',first_order_unit='U1 == 4a (mod p)',
      second_lift_condition='tau-4aG == 0 (mod p^(h+1))',higher_cancellation_possible='YES iff second-lift congruence',
      Gaussian_budget='v_p(M)<=2h',status='SECOND_LIFT_PROVED; GLOBAL_ALLOCATION_OPEN'),
 dict(support='2G+3',p_class='3 mod 4',equal_valuation_h='h>=1',first_order_unit='U2 == -12a (mod p)',
      second_lift_condition='27tau+24aG+152a == 0 (mod p^(h+1))',higher_cancellation_possible='YES iff second-lift congruence',
      Gaussian_budget='v_p(M)<=2h',status='SECOND_LIFT_PROVED; GLOBAL_ALLOCATION_OPEN')]
out=HERE/'J2-55-R14-q1-SecondSupportLift.tsv'
with out.open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0]),delimiter='\t');wr.writeheader();wr.writerows(rows)
print('U1='+str(sp.factor(U1)))
print('U2='+str(sp.factor(U2)))
print('FIRST_SUPPORT_U1_MOD_P=4a PASS')
print('SECOND_SUPPORT_U2_MOD_P=-12a PASS')
print('EQ1_LIFT= v_p(M)>h iff tau-4aG == 0 mod p^(h+1) PASS')
print('EQ2_LIFT= v_p(M)>h iff 27tau+24aG+152a == 0 mod p^(h+1) PASS')
print('GAUSSIAN_EXPONENT_BUDGET=v_p(M)<=2h')
print('EQUAL_VALUATION_SECOND_LIFT=PASS')
print('GLOBAL_EQUAL_VALUATION_CLOSURE=OPEN')
print('LEDGER='+out.name)
