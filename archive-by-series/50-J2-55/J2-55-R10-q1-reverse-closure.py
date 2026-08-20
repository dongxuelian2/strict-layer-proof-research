#!/usr/bin/env python3
"""R10 q=1 reverse exact finite-state/root-conic audit.

This script does NOT truncate g.  It reproduces the 8/80/800 DCDC cells and
then derives an exact scaled discriminant polynomial.  It also certifies why a
'one killer prime per base cell' strategy cannot work without further root/
defect information: for every odd p not dividing 10K the base cell admits the
CRT refinement a3 == t == 0 (mod p), making the homogeneous scaled
discriminant 0 (a square) mod p.

Thus no false q=1 closure is claimed.  The new frontier is each periodic DCDC
cell plus one exact homogeneous binary-quadratic square equation after
 t = -31*a3 + 2K*m.
"""
from math import gcd
from pathlib import Path
import csv
import sympy as sp

OUT=Path('/mnt/data')
G,K,a,t,m=sp.symbols('G K a t m', integer=True)
u=G+1; A=2*G+3
N=(G-1)*t-10*a
Z=4*a+t
Xn=sp.expand(Z+u*N)          # 2X
D2n=sp.expand(2*u*a+G*Xn)   # 2D2
F4=sp.expand(A*Xn**2+2*Z*D2n) # 4 Ftilde
# D4=(4K)^2 * standard root discriminant; square-discriminant => D4 is a square.
D4=sp.factor((2*K*u*D2n)**2-A*G**2*F4)
D4m=sp.factor(D4.subs(t,-31*a+2*K*m))
assert sp.Poly(D4m,a,m).total_degree()==2
assert all(sum(mon)==2 for mon,_ in sp.Poly(D4m,a,m).terms())
# Discriminant of the binary quadratic viewed as quadratic in m.
disc_m=sp.factor(sp.discriminant(D4m,m))
P=(4*G**4*K**2-4*G**4+8*G**3*K**2-12*G**3+4*G**2*K**2-13*G**2-6*G+1)
expected=64*G**4*K**2*a**2*(G+1)**2*(2*G+3)**2*P
assert sp.factor(disc_m-expected)==0

# Homogeneity implies zero refinement at every auxiliary odd prime.
assert sp.expand(D4m.subs({a:0,m:0}))==0

rows=[]
for k in (1,2,3):
 KK=10**k; mod=2*KK; inv31=pow(31,-1,mod)
 cells=[]
 for tr in range(mod):
  ar=(-inv31*tr)%mod
  if gcd(ar,10)!=1: continue
  assert gcd(tr,10)==1 and (31*ar+tr)%mod==0
  cells.append((tr,ar))
  rows.append(dict(K=KK,base_cell=f't={tr};a3={ar} (mod {mod})',aux_modulus='generic p coprime 10K',
                   g_period='ord_p(10)',killer_prime='',compatible_residue_count='>=1 for every such p (zero refinement)',
                   root_survivor_count='UNRESOLVED_BINARY_QUADRATIC',status='OPEN_EXACT_ROOT_CONIC'))
 assert len(cells)=={1:8,2:80,3:800}[k]
 print(f'K{KK}_CELLS={len(cells)}')
 print(f'K{KK}_KILLER_PRIME_BASE_CELL_METHOD=PROVED_INSUFFICIENT_BY_ZERO_REFINEMENT')

p=OUT/'J2-55-R10-q1-periodic-certificate.tsv'
with p.open('w',newline='',encoding='utf-8') as fobj:
 wri=csv.DictWriter(fobj,fieldnames=['K','base_cell','aux_modulus','g_period','killer_prime','compatible_residue_count','root_survivor_count','status'],delimiter='\t')
 wri.writeheader();wri.writerows(rows)

# Save exact root-conic data compactly.
with (OUT/'J2-55-R10-q1-root-conic.txt').open('w',encoding='utf-8') as fobj:
 fobj.write('D4=(4K)^2*Delta_std =\n'+str(D4)+'\n\n')
 fobj.write('After t=-31*a3+2K*m:\n'+str(D4m)+'\n\n')
 fobj.write('disc_m(D4m)=\n'+str(disc_m)+'\n\n')
 fobj.write('P_K(G)=\n'+str(P)+'\n')

print('Q1_D4_HOMOGENEOUS_BINARY_QUADRATIC=PASS')
print('Q1_D4_M_DISCRIMINANT_FACTOR=PASS')
print('Q1_NO_SINGLE_AUX_PRIME_CAN_KILL_A_BASE_CELL_WITHOUT_EXTRA_ROOT_DEFECT_REFINEMENT=PASS')
print('K10_CLOSED=False')
print('K100_CLOSED=False')
print('K1000_CLOSED=False')
print('Q1_ALL_CLOSED=False')
print('Q1_STATUS=OPEN_AT_888_PERIODIC_CELLS_PLUS_EXACT_BINARY_QUADRATIC_ROOT_CONIC')
print('PERIODIC_CERTIFICATE='+p.name)
