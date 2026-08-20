#!/usr/bin/env python3
"""R9 q=1 reverse fixed-K periodic reduction and k=3,g=4 exception closure."""
from math import gcd,isqrt
from pathlib import Path
import csv
OUT=Path('/mnt/data')

# Exact source regression where 4K|G.
for k in (1,2,3):
    K=10**k
    for g in (max(4,k+2), max(5,k+3)):
        G=10**g;u=G+1;A=2*G+3
        assert G%(4*K)==0
        for a3 in (1,3,7,9,11,13,17,19):
            for t in (1,3,7,9,11,13,17,19):
                N=(G-1)*t-10*a3
                Z=4*a3+t
                assert (Z+u*N)%2==0
                X=(Z+u*N)//2
                D2=u*a3+G*X
                F=A*X*X+Z*D2
                assert (F-a3*(31*a3+t))%(2*K)==0
print('Q1_FIXED_K_SOURCE_REGRESSION=PASS')

# The only live reverse case where 4K does NOT divide G is (k,g)=(3,4).
# Exhaust it exactly using inherited t<9G/K, linear ten-unit gates, DCDC, and the exact root discriminant.
def close_k3_g4():
    G=10_000;k=3;K=1000;L=G*G//K;u=G+1;A=2*u+1;M=L//8
    counts=dict(linear=0,dcdc=0,disc_nonnegative=0,disc_square=0,integral_root=0)
    survivors=[]
    for t in range(1,9*G//K):
        if t%2==0: continue
        for a3 in range(G//10,G):
            if gcd(a3,10)!=1: continue
            N=(G-1)*t-10*a3
            if N<=0 or gcd(N,10)!=1: continue
            Z=4*a3+t
            if gcd(Z,10)!=1 or (Z+u*N)%2: continue
            X=(Z+u*N)//2
            if X<=0 or gcd(X,10)!=1: continue
            D2=u*a3+G*X
            if gcd(D2,10)!=1 or (N+Z)%2 or (A*N+3*Z)%2: continue
            h=(N+Z)//2; m=(A*N+3*Z)//2; r=G//2*h-u*a3
            if min(h,m,r)<=0 or any(gcd(z,10)!=1 for z in (h,m,r)): continue
            counts['linear']+=1
            F=A*X*X+Z*D2
            if F%(2*K): continue
            counts['dcdc']+=1
            Om=F//(2*K)
            disc=(u*D2)**2-4*A*M*Om
            if disc<0: continue
            counts['disc_nonnegative']+=1
            y=isqrt(disc)
            if y*y!=disc: continue
            counts['disc_square']+=1
            den=2*A*M
            for sg in (1,-1):
                num=u*D2+sg*y
                if num%den: continue
                x=num//den
                counts['integral_root']+=1
                survivors.append((t,a3,N,x))
    assert counts=={'linear':91200,'dcdc':152,'disc_nonnegative':152,'disc_square':0,'integral_root':0},counts
    assert not survivors
    return counts

exc=close_k3_g4()
print('Q1_K3_G4_EXCEPTION_COUNTS=',exc)
print('Q1_K3_G4_EXCEPTION_STATUS=CLOSED_BY_NONSQUARE_DISCRIMINANT')

allrows=[]
for k in (1,2,3):
    K=10**k;m=2*K;inv31=pow(31,-1,m)
    cells=[]
    for t in range(m):
        a3=(-inv31*t)%m
        assert (31*a3+t)%m==0
        if gcd(a3,10)!=1: continue
        assert gcd(t,10)==1
        cells.append((t,a3))
        allrows.append(dict(k=k,K=K,valid_g=('g>=4' if k<=2 else 'g>=5'),modulus=m,t_mod=t,a3_mod=a3,
                            dcdc='PASS',digit_unit='PASS',discriminant='UNRESOLVED_PERIODIC',full_root='UNRESOLVED_PERIODIC'))
    phi=sum(1 for x in range(m) if gcd(x,m)==1)
    assert len(cells)==phi
    print(f'K={K}')
    print('structural_cells=',m)
    print('DCDC_cells=',len(cells))
    print('multiplier_cells=',len(cells))
    print('periodic_cells=',len(cells))
    print('discriminant_survivors=',len(cells),'(unresolved periodic cells; k=3,g=4 already separately closed)')
    print('full_root_survivors=',len(cells),'(unresolved periodic cells, not actual roots)')
    print('sample_cells=',cells[:min(12,len(cells))])
    print()

p=OUT/'J2-55-R9-q1-reverse-cells.tsv'
with p.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(allrows[0]),delimiter='\t');w.writeheader();w.writerows(allrows)
print('Q1_REVERSE_NEW_THEOREM=31*a3+t == 0 (mod 2K), whenever 4K|G')
print('Q1_REVERSE_T_TENUNIT=PROVED_FROM_DCDC_AND_A3_TENUNIT')
print('Q1_REVERSE_CELL_COUNTS=8,80,800')
print('Q1_REVERSE_STATUS=OPEN_AT_FINITE_EXPLICIT_PERIODIC_CELLS')
print('CELL_FILE='+p.name)
