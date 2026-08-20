#!/usr/bin/env python3
"""J2-55 R4 exact Euclidean-defect replay/search.

Unified pipeline: no REGULAR/SINGULAR root-fibre enumeration.  d=gcd(A,D2) is
recorded only as structural polynomial content.  Every DCDC profile is sent to
one Euclidean division, one A+decimal CRT defect, and at most one candidate.

Computational scopes:
  * historical boundary q in {7,11,17,19}, g<=1200 (must reproduce 79 DCDC states);
  * high-tail delta=1 q in {7,11,17,19}, g<=1200;
  * reverse nonzero-tail r=1 q in {7,11,17,19}, g<=12 (targeted true post-DCDC diagnostic);
  * reverse zero-tail targeted at the minimal r allowed by q^3<63*10^r.
All arithmetic is exact Python integer/Fraction arithmetic.
"""
from fractions import Fraction
from math import gcd
from collections import Counter
import csv, sys
sys.set_int_max_str_digits(1_000_000)

ETA=Fraction(1299,500)
OUT_TSV='/mnt/data/J2-55-R4-EuclideanDefect-survivors.tsv'
OUT_CERT='/mnt/data/J2-55-R4-EuclideanDefect-search-certificate.txt'

ORDER_CLASSES={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}

def vp(n,p):
    n=abs(int(n)); c=0
    if n==0:return 10**9
    while n%p==0:n//=p;c+=1
    return c

def unit10(n): return gcd(abs(int(n)),10)==1

def ceil_div(a,b): return -((-a)//b)

def solve_signed_linear(a,b,m,M):
    """All nonzero z in [-M,M] with a*z=b mod m, exact arithmetic."""
    if M<1:return []
    d=gcd(a,m)
    if b%d:return []
    aa,bb,mm=a//d,b//d,m//d
    r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
    first=r+ceil_div(-M-r,mm)*mm
    if first==0:first=mm
    return range(first,M+1,mm)

def tail_CB(q):
    C=q**4+10*q**3+12*q*q+8*q
    B=(q+2)*(q*q-4*q-4)
    return C,B

def reconstruct(G,q,N,t):
    if (G+1)%q:return None
    u=(G+1)//q; A=2*u+1; Mq=q*(q+4)
    R=A*t-2*N
    if R%Mq:return None
    Z=R//Mq
    num=(G-1)*t-q*N; den=2*(q+4)
    if num%den:return None
    a3=num//den
    if (Z+u*N)%2:return None
    X=(Z+u*N)//2
    if (N+q*Z)%2:return None
    hlin=(N+q*Z)//2
    if (A*N+(q+2)*Z)%2:return None
    mlin=(A*N+(q+2)*Z)//2
    rlin=(G//2)*hlin-u*a3
    D2=u*a3+G*X
    return dict(G=G,q=q,u=u,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2,
                hlin=hlin,mlin=mlin,rlin=rlin)

def linear_gate(row,kexp):
    G,u,A=row['G'],row['u'],row['A']; K=10**kexp
    for z in ('a3','Z','X','D2','hlin','mlin','rlin'):
        if not(row[z]>0 and unit10(row[z])):return False,z
    if not(G//10<=row['a3']<G):return False,'DIG3'
    if not row['X']*K < ETA*u*G*G:return False,'X_RADIAL'
    if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False,'Z_RADIAL'
    return True,'PASS'

def F(row): return row['A']*row['X']**2+row['Z']*row['D2']

def Q(row,K,x):
    H=row['G']//2
    return row['A']*H*H*x*x-2*row['u']*K*row['D2']*x+F(row)

def root_interval(row,ell):
    return Fraction(row['A']*row['G'],10), Fraction(8*row['u']*row['D2'],row['A']*10**ell)

def crt2(a,m,b,n):
    assert gcd(m,n)==1
    return (a + m*(((b-a)*pow(m,-1,n))%n))%(m*n)

def euclidean_data(row,kexp,ell):
    G=row['G']; K=10**kexp; L=10**ell; M=L//8
    A,u,D2=row['A'],row['u'],row['D2']
    d=gcd(A,D2); e=A//d; Ds=D2//d
    assert gcd(e,Ds)==1
    f=F(row)
    assert f%d==0
    Fs=e*row['X']**2+row['Z']*Ds
    assert f==d*Fs
    if f%(2*K):
        return None,'DCDC_FAIL'
    # Content-deflated DCDC is forced by gcd(d,2K)=1.
    if gcd(d,2*K)!=1 or Fs%(2*K):
        return None,'CONTENT_DEFLATION_FAIL'
    Os=Fs//(2*K)
    assert f//(2*K)==d*Os
    a=e*M
    assert gcd(u*Ds,a)==1
    mu,rho=divmod(u*Ds,a)
    assert 1<=rho<a
    rA=(-row['Z']*pow(K,-1,A))%A
    x10=(Os*pow((u*Ds)%M,-1,M))%M
    sA=(mu-rA)%A; sM=(mu-x10)%M
    ss=crt2(sA,A,sM,M)
    Bnd=Fraction(292*L*L*u*u,A*G**3)
    return dict(d=d,e=e,Dsharp=Ds,OmegaSharp=Os,M=M,mu=mu,rho=rho,
                rA=rA,x10=x10,sA=sA,sM=sM,sstar=ss,B=Bnd), 'PASS'

def profile_pipeline(row,kexp,ell,kind,alpha=''):
    base=dict(kind=kind,g=len(str(row['G']))-1,k=kexp,ell=ell,
              delta=kexp-(len(str(row['G']))-1),q=row['q'],u=row['u'],A=row['A'],
              N=row['N'],t=row['t'],alpha=alpha,Z=row['Z'],D2=row['D2'])
    if gcd(row['Z'],row['u'])!=1:
        return {**base,'first_failure':'PRIMITIVE_GCD_FAIL'}
    ed,status=euclidean_data(row,kexp,ell)
    if status!='PASS': return {**base,'first_failure':status}
    rec={**base,**ed}
    s=ed['sstar']; Bnd=ed['B']
    rec['B_num']=Bnd.numerator; rec['B_den']=Bnd.denominator
    if Fraction(s,1)>=Bnd:
        rec['first_failure']='DEFECT_BOUND_FAIL'; return rec
    x=ed['mu']-s
    lam=ed['rho']+ed['e']*ed['M']*s
    phi=ed['OmegaSharp']-x*lam
    rec.update(x_candidate=x,lambdaSharp=lam,Phi=phi)
    lo,hi=root_interval(row,ell)
    if not(lo<x<hi):
        rec['first_failure']='ROOT_INTERVAL_FAIL'; return rec
    K=10**kexp; A=row['A']
    if Q(row,K,x)%(A*A):
        rec['first_failure']='A2_FAIL'; return rec
    if Q(row,K,x)%(A**3):
        rec['first_failure']='A3_FAIL'; return rec
    if (x*x-row['Z']*row['Z'])%row['u']:
        rec['first_failure']='U_SQUARE_FAIL'; return rec
    if phi:
        rec['first_failure']='PRODUCT_FAIL'; return rec
    # Q and deflated product are the same exact root equation; audit equality.
    assert Q(row,K,x)==0
    rec['first_failure']='FULL_ROOT_SURVIVE'
    return rec

def scan_tail(q,delta,gmax=1200):
    """Nonzero high/boundary/reverse tail for fixed q and delta."""
    mod,rr=ORDER_CLASSES[q]; b=vp(q+4,5); C,B=tail_CB(q); Mq=q*(q+4)
    r=max(-delta,0)
    ddel=2*5**b*10**r
    if delta>0:
        # |alpha| < 30*5^b*q^4*10^-delta; for our delta=1 exact integer bound.
        den=10**delta; numer=30*5**b*q**4
        mmax=(numer-1)//den
        tmax=3*q+7  # t < 3q+8
    elif delta==0:
        mmax=30*5**b*q**4-1
        tmax=9*q-1  # t < 9q
    else:
        mmax=30*5**b*q**4*10**(2*r)-1
        tmax=9*q*10**r-1
    rows=[]; st=Counter()
    for g in range(max(6,1-delta),gmax+1):
        if g%mod!=rr: continue
        k=g+delta; ell=g-delta
        if k<1 or ell<6:continue
        if delta<0 and k<=b:continue  # frozen reverse quotient scope
        G=10**g
        if G%ddel:continue
        u=(G+1)//q; A=2*u+1; D=G//ddel
        CM=C*Mq
        # Combine N-integrality + RCE3 into 2 D alpha = (C A-2B)t mod C*Mq.
        aa=2*D
        coeff=(C*A-2*B)
        for t in range(1,tmax+1):
            for alpha in solve_signed_linear(aa,(coeff*t)%CM,CM,mmax):
                st['tail_integral_rce']+=1
                num=B*t+alpha*D
                if num%C:continue
                N=num//C
                row=reconstruct(G,q,N,t)
                if row is None:continue
                st['reconstructed']+=1
                ok,_=linear_gate(row,k)
                if not ok:continue
                st['linear_legal']+=1
                if F(row)%(2*10**k):continue
                st['dcdc']+=1
                rows.append((g,k,ell,alpha,row))
    return dict(st),rows

def scan_boundary(gmax=1200):
    stats={}; rows=[]
    for q in ORDER_CLASSES:
        st,rr=scan_tail(q,0,gmax)
        stats[q]=st; rows.extend(rr)
    return stats,rows

def scan_high1(gmax=1200):
    stats={}; rows=[]
    for q in ORDER_CLASSES:
        st,rr=scan_tail(q,1,gmax)
        stats[q]=st; rows.extend(rr)
    return stats,rows

def scan_reverse_r1(gmax=1200):
    stats={}; rows=[]
    for q in ORDER_CLASSES:
        st,rr=scan_tail(q,-1,gmax)
        stats[q]=st; rows.extend(rr)
    return stats,rows

def scan_reverse_zero_tail():
    """Target the first r for each q where q^3<63*10^r; alpha=0."""
    out=[]; stats={}
    for q,(mod,rr) in ORDER_CLASSES.items():
        r=1
        while not q**3 < 63*10**r:r+=1
        b=vp(q+4,5); C,B=tail_CB(q); Mq=q*(q+4); st=Counter()
        # Search a few first admissible g classes above ell>=6 and k>b.
        admiss=[]
        for g in range(max(6,r+b+1), max(6,r+b+1)+10*mod+1):
            if g%mod==rr:admiss.append(g)
            if len(admiss)>=6:break
        gg=gcd(C,abs(B)); step=C//gg
        for g in admiss:
            k=g-r; ell=g+r; G=10**g
            u=(G+1)//q; A=2*u+1
            tmax=9*q*10**r-1
            # alpha=0 => C|B t.
            for t in range(step,tmax+1,step):
                st['tail_zero_t']+=1
                N=B*t//C
                row=reconstruct(G,q,N,t)
                if row is None:continue
                st['reconstructed']+=1
                ok,_=linear_gate(row,k)
                if not ok:continue
                st['linear_legal']+=1
                if F(row)%(2*10**k):continue
                st['dcdc']+=1
                out.append((q,r,g,k,ell,row))
        stats[q]=(r,dict(st))
    return stats,out

def specialized_high_s0(row,k,ell):
    """Death order after theorem B<1 forces s=0; primitive assumed separately."""
    if gcd(row['Z'],row['u'])!=1:return 'PRIMITIVE_GCD_FAIL'
    ed,status=euclidean_data(row,k,ell)
    if status!='PASS':return status
    assert ed['B']<1
    x=ed['mu']; A=row['A']; M=ed['M']
    if x%A!=ed['rA']:return 'S0_A_ROOT_FAIL'
    if x%M!=ed['x10']:return 'S0_DECIMAL_FAIL'
    K=10**k
    if Q(row,K,x)%(A*A):return 'S0_A2_FAIL'
    if Q(row,K,x)%(A**3):return 'S0_A3_FAIL'
    if (x*x-row['Z']**2)%row['u']:return 'S0_U_FAIL'
    if ed['OmegaSharp']-ed['mu']*ed['rho']:return 'S0_PRODUCT_FAIL'
    return 'FULL_ROOT_SURVIVE'

def normalize_record(rec):
    fields=['kind','g','k','ell','delta','q','u','A','N','t','alpha','Z','D2','d','e','Dsharp','OmegaSharp','mu','rho','B_num','B_den','sA','sM','sstar','rA','x10','x_candidate','lambdaSharp','Phi','first_failure']
    return {f:rec.get(f,'') for f in fields}

def main():
    allrecs=[]; lines=['J2-55 R4 EuclideanDefect exact search certificate','EXACT_ARITHMETIC=PASS']

    bstats,brows=scan_boundary(1200)
    lines.append(f'HISTORICAL_BOUNDARY_DCDC={len(brows)}')
    for q in ORDER_CLASSES: lines.append(f'H0_Q{q}={bstats[q]!r}')
    assert len(brows)==79, len(brows)
    bgate=Counter(); dcount=Counter()
    for g,k,ell,alpha,row in brows:
        rec=profile_pipeline(row,k,ell,'boundary',alpha); allrecs.append(rec)
        bgate[rec['first_failure']]+=1
        if 'd' in rec:dcount[rec['d']]+=1
    lines.append(f'H0_UNIFIED_FIRST_FAILURE={dict(bgate)!r}')
    lines.append(f'H0_CONTENT_DISTRIBUTION_AFTER_PRIMITIVE={dict(dcount)!r}')
    lines.append('H0_SINGULAR_OLD_G=259,359,435,481,669,1025')
    # Explicitly locate the six old singular profiles in the unified records.
    sing={259,359,435,481,669,1025}
    for rec in allrecs:
        if rec.get('kind')=='boundary' and rec.get('g') in sing and rec.get('q')==11 and rec.get('d')==3:
            Bv=Fraction(rec['B_num'],rec['B_den'])
            lines.append('H0_OLD_SINGULAR_UNIFIED '+repr({
                'g':rec['g'],'d':rec['d'],'e_digits':len(str(rec['e'])),
                'Dsharp_digits':len(str(rec['Dsharp'])),'mu_digits':len(str(rec['mu'])),
                'rho_digits':len(str(rec['rho'])),'sstar_digits':len(str(rec['sstar'])),
                'B_float':float(Bv),'first_failure':rec['first_failure']}))

    hstats,hrows=scan_high1(1200)
    lines.append(f'HIGH_DELTA1_DCDC={len(hrows)}')
    for q in ORDER_CLASSES: lines.append(f'H1_Q{q}={hstats[q]!r}')
    hdeath=Counter()
    for g,k,ell,alpha,row in hrows:
        rec=profile_pipeline(row,k,ell,'high_delta1',alpha); allrecs.append(rec)
        hdeath[specialized_high_s0(row,k,ell)]+=1
    lines.append(f'HIGH_DELTA1_S0_FIRST_DEATH={dict(hdeath)!r}')

    rstats,rrows=scan_reverse_r1(12)
    lines.append('REVERSE_R1_SCOPE=g<=12 (diagnostic, chosen to reach genuine post-DCDC states)')
    lines.append(f'REVERSE_R1_DCDC={len(rrows)}')
    for q in ORDER_CLASSES: lines.append(f'REVERSE_R1_Q{q}={rstats[q]!r}')
    rgate=Counter()
    for g,k,ell,alpha,row in rrows:
        rec=profile_pipeline(row,k,ell,'reverse_r1',alpha); allrecs.append(rec); rgate[rec['first_failure']]+=1
    lines.append(f'REVERSE_R1_UNIFIED_FIRST_FAILURE={dict(rgate)!r}')

    zstats,zrows=scan_reverse_zero_tail()
    lines.append(f'REVERSE_ZERO_TAIL_DCDC={len(zrows)}')
    for q in ORDER_CLASSES:lines.append(f'REVERSE_ZERO_Q{q}={zstats[q]!r}')
    zgate=Counter()
    for q,r,g,k,ell,row in zrows:
        rec=profile_pipeline(row,k,ell,f'reverse_zero_r{r}',0); allrecs.append(rec); zgate[rec['first_failure']]+=1
    lines.append(f'REVERSE_ZERO_UNIFIED_FIRST_FAILURE={dict(zgate)!r}')

    # Global diagnostics.
    lines.append('GLOBAL_ONE_S_IMPLEMENTATION=one CRT residue modulo A*M per profile; no A2 fibre enumeration')
    lines.append('FULL_ROOT_SURVIVE='+str(sum(r.get('first_failure')=='FULL_ROOT_SURVIVE' for r in allrecs)))

    fields=['kind','g','k','ell','delta','q','u','A','N','t','alpha','Z','D2','d','e','Dsharp','OmegaSharp','mu','rho','B_num','B_den','sA','sM','sstar','rA','x10','x_candidate','lambdaSharp','Phi','first_failure']
    with open(OUT_TSV,'w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
        for rec in allrecs:w.writerow(normalize_record(rec))
    with open(OUT_CERT,'w',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
    print('\n'.join(lines))

if __name__=='__main__':main()
