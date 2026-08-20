#!/usr/bin/env python3
"""J2-55 R8 q=1 boundary finite multiplier + periodic root certificate.

All arithmetic is exact.  The final closure is periodic in g; it is NOT a finite-g scan.
"""
from math import gcd, lcm
from fractions import Fraction
import csv
from pathlib import Path

OUT=Path(__file__).resolve().parent
ETA=Fraction(1299,500)
TSET=(3,7,9,11,13)

# Dnum = 38440000 * discriminant of AM x^2-uD2 x+Omega after q=1 multiplier reconstruction.
def dnum_mod(G,m,t,p):
    G%=p; m%=p; t%=p
    return (
      100*pow(G,8,p)*m*m +280*pow(G,7,p)*m*m -4800*pow(G,7,p)*m*t
      +136*pow(G,6,p)*m*m +8880*pow(G,6,p)*m*t +57600*pow(G,6,p)*t*t
      -364*pow(G,5,p)*m*m +42080*pow(G,5,p)*m*t -374400*pow(G,5,p)*t*t
      -597*pow(G,4,p)*m*m +21440*pow(G,4,p)*m*t -227200*pow(G,4,p)*t*t
      -370*pow(G,3,p)*m*m -32600*pow(G,3,p)*m*t +18000*pow(G,3,p)*t*t
      -89*pow(G,2,p)*m*m -31220*pow(G,2,p)*m*t -1998900*pow(G,2,p)*t*t
      -8500*G*m*t -2305000*G*t*t +40000*t*t
    )%p

DEN=38440000

def legendre_square_rational(num,p):
    assert DEN%p
    v=num*pow(DEN,-1,p)%p
    if v==0:return True
    return pow(v,(p-1)//2,p)==1

def ord_mod(a,p):
    assert gcd(a,p)==1
    x=1
    for n in range(1,p+1):
        x=x*a%p
        if x==1:return n
    raise AssertionError

def local200_residue(t):
    # for live g>=6: G/100 ==0 mod200, so 31r == t mod200.
    inv31=pow(31,-1,200)
    rr=t*inv31%200
    N=(10*rr-t)%200
    # 100N^2+158Nt+68t^2 + m r ==0 mod200; r is a unit mod200.
    base=(100*N*N+158*N*t+68*t*t)%200
    mm=(-base*pow(rr,-1,200))%200
    return rr,N,mm

def generate_multiplier_candidates():
    out=[]
    for t in TSET:
        rr,Nmod,mres=local200_residue(t)
        for m in range(mres if mres else 200,1612,200):
            if m<1 or m>1611:continue
            zeta=310*t-m
            if not (311<=zeta<=3100):continue
            out.append((t,m,zeta,rr,Nmod,mres))
    return out

def gclasses_mod31(t,m):
    # m*10^(g-1) ==21t mod31; ord=15.
    ans=[]
    for g in range(1,16):
        if (m*pow(10,g-1,31)-21*t)%31==0:
            ans.append(g%15)
    return ans

PRIMES=[3,7,11,13,17,19,23,29,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443]

def find_killer(t,m,g15):
    for p in PRIMES:
        if p in (2,5,31) or DEN%p==0 or gcd(10,p)!=1: continue
        o=ord_mod(10,p)
        P=lcm(15,o)
        residues=[g for g in range(1,P+1) if g%15==g15%15]
        if not residues:continue
        vals=[]; ok=True
        for g in residues:
            G=pow(10,g,p)
            num=dnum_mod(G,m,t,p)
            sq=legendre_square_rational(num,p)
            vals.append((g,num,sq))
            if sq:
                ok=False;break
        if ok:
            return p,o,P,vals
    return None

def main():
    assert ord_mod(10,31)==15
    # t-bound: a3<G gives r>G(t-10)/10; N<2*ETA*G gives r<(2*ETA*G+t)/10.
    # Hence t(G-1)<(10+2*ETA)G.  At G>=10^4 the RHS ratio is <16, so t<=15.
    Gmin=10**4
    assert (Fraction(10)+2*ETA)*Gmin/Fraction(Gmin-1) < 16
    assert tuple(n for n in range(2,16) if n%2 and n%5) == TSET
    # Exact constant improvements used by theorem.
    # From r < (2 eta G+t)/10, m=100(31r-t)/G <620 eta + (310t-100t)/G.
    # For G>=10^4,t<=15: RHS < 1610.76+0.315=1611.075, hence m<=1611.
    assert Fraction(620)*ETA + Fraction(210*15,10**4) < Fraction(1612)
    assert Fraction(620)*ETA + Fraction(210*15,10**4) == Fraction(1611075,1000)

    table=[]
    for t in TSET:
        rr,Nmod,mres=local200_residue(t)
        table.append((t,rr,Nmod,mres))
    print('LOCAL200_TABLE=t,r_mod200,N_mod200,m_mod200')
    for row in table: print(*row,sep='\t')
    expected={3:(13,127,130),7:(97,163,170),9:(39,181,190),11:(181,199,10),13:(123,17,30)}
    assert {t:(r,n,m) for t,r,n,m in table}==expected

    cand=generate_multiplier_candidates()
    print('MULTIPLIER_CANDIDATES_BEFORE_MOD31=',len(cand))
    assert len(cand)==29
    cells=[]
    killed_mod31=0
    for t,m,zeta,rr,Nmod,mres in cand:
        gs=gclasses_mod31(t,m)
        if not gs:
            killed_mod31+=1;continue
        assert len(gs)==1
        g15=gs[0]
        killer=find_killer(t,m,g15)
        assert killer is not None,(t,m,g15)
        p,o,P,vals=killer
        cells.append(dict(t=t,m1=m,zeta=zeta,g_mod15=g15,killer_prime=p,ord10=o,period=P,
                          checked_g_residues=','.join(str(v[0]) for v in vals),
                          disc_num_mod_p=','.join(str(v[1]) for v in vals)))
    print('MOD31_DEAD=',killed_mod31)
    print('PERIODIC_CELLS=',len(cells))
    assert killed_mod31==12 and len(cells)==17

    expected_cells=[
      (3,330,600,9),(7,170,2000,10),(7,370,1800,13),(7,570,1600,8),
      (7,770,1400,9),(7,1170,1000,1),(7,1370,800,14),(9,790,2000,6),
      (9,990,1800,9),(9,1190,1600,4),(9,1390,1400,5),(11,410,3000,7),
      (11,810,2600,12),(11,1010,2400,5),(11,1210,2200,9),(13,1030,3000,4),
      (13,1430,2600,9)]
    assert [(x['t'],x['m1'],x['zeta'],x['g_mod15']) for x in cells]==expected_cells

    for x in cells:
        print('CELL',x['t'],x['m1'],x['zeta'],'gmod15='+str(x['g_mod15']),
              'KILL_p='+str(x['killer_prime']),'ord='+str(x['ord10']),'period='+str(x['period']),
              'gres='+x['checked_g_residues'])

    path=OUT/'J2-55-R8-q1-boundary-cells.tsv'
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(cells[0].keys()),delimiter='\t')
        w.writeheader();w.writerows(cells)
    print('Q1_BOUNDARY_PERIODIC_DISCRIMINANT_KILL=17/17')
    print('Q1_BOUNDARY_STATUS=CLOSED')
    print('CELL_FILE='+path.name)

if __name__=='__main__':main()
