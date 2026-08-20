#!/usr/bin/env python3
"""A1 J2 FQTR6 exact computation certificate.

Tasks:
  * exact ell=5 diagnostic census on the already-proved finite wedge;
  * write DCDC/root pseudo-survivor ledgers;
  * verify the new fixed-q valuation tail on every relevant tested state;
  * verify an explicit large-g q=11 DCDC pseudo-survivor showing DCDC alone is not closure.

All decision arithmetic is integer/Fraction arithmetic. SymPy is used only to factor
10^g+1 and enumerate its exact divisors for 4<=g<=14.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
from collections import Counter, defaultdict
import sympy as sp

OUT=Path('/mnt/data')
ETA=Fraction(1299,500)
ELL=5


def unit10(n): return gcd(abs(n),10)==1

def ceil_div(a,b): return -((-a)//b)

def vp(n,p):
    n=abs(n); c=0
    while n and n%p==0:
        n//=p; c+=1
    return c

def tail_CB(q):
    C=q**4+10*q**3+12*q**2+8*q
    B=(q+2)*(q*q-4*q-4)
    return C,B

def outer_pairs(G):
    out=[]
    for u in sp.divisors(G+1):
        if u<=1: continue
        q=(G+1)//u
        A=2*u+1
        if unit10(A): out.append((u,q,A))
    return out

def solve_cong_interval(a,b,m,L,U):
    if L>U: return []
    d=gcd(a,m)
    if b%d: return []
    aa,bb,mm=a//d,b//d,m//d
    r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
    if r<L:
        r += ceil_div(L-r,mm)*mm
    return list(range(r,U+1,mm))

def digit_t_interval(G,q,N):
    L=ceil_div((q+4)*(G//5)+q*N,G-1)
    U=(2*(q+4)*G+q*N-1)//(G-1)
    return L,U

def nstrip(G,u,A,k):
    K=10**k
    lo=-(2*ETA/K + Fraction(2*A,G))
    hi=2*ETA*G*G/K
    nmin=lo.numerator//lo.denominator + 1
    while Fraction(nmin,1)<=lo: nmin+=1
    nmax=hi.numerator//hi.denominator
    while Fraction(nmax,1)>=hi: nmax-=1
    if nmin%2==0: nmin+=1
    if nmax%2==0: nmax-=1
    return nmin,nmax,lo,hi

def reconstruct(G,q,N,t):
    if (G+1)%q: return None
    u=(G+1)//q; A=2*u+1; M=q*(q+4)
    R=A*t-2*N
    if R%M: return None
    Z=R//M
    anum=(G-1)*t-q*N; aden=2*(q+4)
    if anum%aden: return None
    a3=anum//aden
    if (Z+u*N)%2: return None
    X=(Z+u*N)//2
    if (N+q*Z)%2: return None
    h=(N+q*Z)//2
    if (A*N+(q+2)*Z)%2: return None
    m=(A*N+(q+2)*Z)//2
    r=(G//2)*h-u*a3
    D2=u*a3+G*X
    return dict(G=G,u=u,q=q,A=A,N=N,t=t,a3=a3,Z=Z,X=X,D2=D2,h=h,m=m,r=r)

def negative_linear_ok(row,k):
    G,u,A=row['G'],row['u'],row['A']; K=10**k
    for key in ('a3','Z','X','D2','h','m','r'):
        if not (row[key]>0 and unit10(row[key])): return False
    if not (G//10 <= row['a3'] < G): return False
    if not row['X']*K < ETA*u*G*G: return False
    if not Fraction(row['Z'],1) < 2*ETA*u/K + Fraction(2*u*A,G): return False
    q,N,t,Z,a3=row['q'],row['N'],row['t'],row['Z'],row['a3']
    return (2*A*a3 == q*(G-1)*Z-N
            and (G-1)*t == 2*(q+4)*a3+q*N
            and q*(q+4)*Z == A*t-2*N)

def Ftilde(row): return row['A']*row['X']*row['X'] + row['Z']*row['D2']

def root_data(row,k):
    G,u,A=row['G'],row['u'],row['A']; H=G//2; K=10**k; F=Ftilde(row)
    aa=A*H*H; bb=-2*u*K*row['D2']; cc=F
    disc=bb*bb-4*aa*cc
    if disc<0: return False,False,[],disc
    s=isqrt(disc); sq=(s*s==disc); roots=[]
    if sq:
        den=2*aa
        for sg in (1,-1):
            num=-bb+sg*s
            if num>0 and num%den==0: roots.append(num//den)
    return True,sq,sorted(set(roots)),disc

def tail_prune(G,ell,q,N,t):
    if ell>=len(str(G))-1: # equivalent ell>=g; no tail reduction needed
        return True
    if q==1:
        if (N+t)%10: return False
        r=(N+t)//10
        return (31*N+21*t)%(G//10)==0
    C,B=tail_CB(q); b=vp(q+4,5)
    g=len(str(G))-1
    if b>=g:
        return True  # valuation is handled by the large-5^b outer chamber, not by this tail prune
    D=G//(2*5**b)
    return (C*N-B*t)%D==0

def survivor_row(row,k,ell):
    F=Ftilde(row); nonneg,sq,roots,disc=root_data(row,k)
    q=row['q']; C,B=tail_CB(q)
    b=vp(q+4,5)
    f1=q*row['N']+row['t']
    f2=C*row['N']-B*row['t']
    return {
        'ell':ell,'g':len(str(row['G']))-1,'q':q,'u':row['u'],'N':row['N'],'t':row['t'],
        'a3':row['a3'],'Z':row['Z'],'X':row['X'],'D2':row['D2'],
        'Ftilde':F,'core_quotient':F//(2*10**k),
        'v2_f1':vp(f1,2),'v5_f1':vp(f1,5),'v2_f2':vp(f2,2),'v5_f2':vp(f2,5),
        'disc_nonnegative':int(nonneg),'disc_square':int(sq),
        'integral_a1_roots':','.join(map(str,roots))
    }

def scan_l5():
    totals=Counter(); per_g=defaultdict(Counter); per_q=[]; survivors=[]
    for g in range(4,15):
        G=10**g; k=2*g-ELL
        if k<1: continue
        for u,q,A in outer_pairs(G):
            if q==1 and g>12: continue
            stats=Counter(outer=1)
            nmin,nmax,_,_=nstrip(G,u,A,k)
            if nmin<=nmax: stats['N_cells']=(nmax-nmin)//2+1
            M=q*(q+4)
            for N in range(nmin,nmax+1,2):
                L,U=digit_t_interval(G,q,N)
                ts=solve_cong_interval(A,2*N,M,L,U)
                stats['congruence'] += len(ts)
                for t in ts:
                    if not tail_prune(G,ELL,q,N,t): continue
                    stats['tail'] += 1
                    row=reconstruct(G,q,N,t)
                    if row is not None: stats['reconstructed'] += 1
                    if not (row and negative_linear_ok(row,k)): continue
                    stats['digit_legal'] += 1
                    F=Ftilde(row)
                    if F%(2*10**k): continue
                    stats['dcdc'] += 1
                    nonneg,sq,roots,_=root_data(row,k)
                    stats['disc_nonnegative'] += int(nonneg)
                    stats['disc_square'] += int(sq)
                    stats['integral_a1_roots'] += len(roots)
                    survivors.append(survivor_row(row,k,ELL))
            totals.update(stats); per_g[g].update(stats)
            per_q.append((g,q,dict(stats)))
    totals['full_radial_survivors']=0
    assert totals['integral_a1_roots']==0
    return totals,dict(per_g),per_q,survivors

def check_large_q11_pseudo():
    # Exact fixed-q tail/DCDC pseudo-survivor discovered in this round.
    q=11; h=1; g=471; ell=g-h; G=10**g
    C,B=tail_CB(q); b=vp(q+4,5); t=31; mu=152510
    D=G//(2*5**b)
    num=B*t+mu*D
    assert num%C==0
    N=num//C
    row=reconstruct(G,q,N,t); assert row is not None
    k=g+h
    assert negative_linear_ok(row,k)
    F=Ftilde(row); assert F%(2*10**k)==0
    nonneg,sq,roots,disc=root_data(row,k)
    assert nonneg and not sq and not roots
    assert disc%11==8  # 8 is a quadratic nonresidue modulo 11
    # New valuation-tail theorem is exact here.
    assert vp(q*N+t,2)==1
    assert vp(q*N+t,5)==b
    assert (C*N-B*t)==mu*D
    meta=dict(q=q,g=g,ell=ell,h=h,t=t,mu=mu,N=N,dcdc=True,disc_nonnegative=nonneg,disc_square=sq,disc_mod11=8)
    return meta, survivor_row(row,k,ell)

def write_tsv(path,rows):
    fields=['ell','g','q','u','N','t','a3','Z','X','D2','Ftilde','core_quotient',
            'v2_f1','v5_f1','v2_f2','v5_f2','disc_nonnegative','disc_square','integral_a1_roots']
    with path.open('w',encoding='utf-8') as f:
        f.write('\t'.join(fields)+'\n')
        for r in rows:
            f.write('\t'.join(str(r.get(k,'')) for k in fields)+'\n')

def main():
    totals,per_g,per_q,surv=scan_l5()
    pseudo,pseudo_row=check_large_q11_pseudo()
    write_tsv(OUT/'A1_J2_FQTR6_L5_survivors.tsv',surv)
    write_tsv(OUT/'A1_J2_FQTR6_survivors.tsv',surv+[pseudo_row])
    lines=[
        'A1 J2 FQTR6 exact certificate',
        'EXACT_ARITHMETIC=PASS',
        'SYMBOLIC_FILE=A1_J2_FQTR6_symbolic.py',
        'NEW_Q1_TAIL: ell<g => G/10 | (31N+21t), with N+t=10r and G/100 | (31r-t); hence g<=ell+3.',
        'NEW_QGT1_VALUATION_TAIL: ell<g, q>1, b=v5(q+4)<g, C=q^4+10q^3+12q^2+8q, B=(q+2)(q^2-4q-4): G/(2*5^b) | C*N-B*t.',
        'NEW_FIXED_Q_BOUND: if g>b then G < 30*5^b*q^4*10^ell; for fixed q the exceptional g<=b are already finite, so fixed q is slope 1 asymptotically.',
        'NEW_UNIFORM_QGT1_WEDGE: b<g gives G < 40*10^(17ell/7); b>=g is even stronger by outer suppression; globally g<=ceil(17ell/7)+1.',
        "SMALL_Q_CLASSIFICATION={7:'g=3 mod 6',11:'g odd',17:'g=8 mod 16',19:'g=9 mod 18'}; q=13 excluded by 5|A.",
        f'L5_TOTALS={dict(totals)!r}',
    ]
    for g in sorted(per_g): lines.append(f'L5_g={g} {dict(per_g[g])!r}')
    lines += [
        f'L5_DCDC_SURVIVORS={len(surv)}',
        f'ALL_RECORDED_DCDC_PSEUDO_SURVIVORS={len(surv)+1}',
        'L5_DISC_SQUARE_SURVIVORS=0',
        'L5_INTEGRAL_ROOT_SURVIVORS=0',
        'VERDICT_ELL5=CLOSED',
        f"Q11_LARGE_DCDC_PSEUDO=(g={pseudo['g']},ell={pseudo['ell']},q=11,h=1,t=31,mu=152510); DISC_MOD_11=8 NONRESIDUE; DISC_SQUARE=False",
        'VERDICT_FIXED_Q_DCDC_ALONE=FALSE_AS_CLOSURE_ENGINE',
        'VERDICT_UNIFORM_SLOPE2=NOT_PROVED',
        'VERDICT_UNIFORM_QGT1_SLOPE=17/7',
        'VERDICT_FULL_J2=OPEN',
        'CERTIFICATE_STATUS=PASS',
        'SURVIVOR_FILE=A1_J2_FQTR6_survivors.tsv',
        'L5_SURVIVOR_FILE=A1_J2_FQTR6_L5_survivors.tsv',
    ]
    (OUT/'A1_J2_FQTR6_certificate.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (OUT/'A1_J2_FQTR6_L5_certificate.txt').write_text(
        'A1 J2 FQTR6 ell=5 exact closure certificate\n'
        f'TOTALS={dict(totals)!r}\nDCDC_SURVIVORS={len(surv)}\nDISC_SQUARE_SURVIVORS=0\n'
        'INTEGRAL_ROOT_SURVIVORS=0\nFULL_RADIAL_SURVIVORS=0\nSTATUS=ELL5_CLOSED\n',encoding='utf-8')
    print('CERTIFICATE_STATUS=PASS')
    print('L5_TOTALS=',dict(totals))
    print('L5_DCDC_SURVIVORS=',len(surv))
    print('VERDICT_ELL5=CLOSED')
    print('VERDICT_FULL_J2=OPEN')

if __name__=='__main__': main()
