#!/usr/bin/env python3
"""A1 J2 TLRC7 exact diagnostic/certificate search.

Proves q=1,h>=1 tail closure by a complete residue-period check and performs a
small-q local-root census. Also verifies a low-k pre-DCDC pseudo-family that
falsifies k>g before the decimal-core gate. Exact integer/Fraction arithmetic.
"""
from fractions import Fraction
from math import gcd,isqrt
from collections import Counter
from pathlib import Path
import sympy as sp

OUT=Path('/mnt/data')
ETA=Fraction(1299,500)

def unit10(n): return gcd(abs(n),10)==1

def vp(n,p):
    n=abs(n); c=0
    if n==0:return 10**9
    while n%p==0:n//=p;c+=1
    return c

def ceil_div(a,b):return -((-a)//b)

def solve_signed_linear(a,b,m,M):
    """All x in [-M,M] with a*x=b mod m; x !=0."""
    if M<1:return []
    d=gcd(a,m)
    if b%d:return []
    aa,bb,mm=a//d,b//d,m//d
    r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
    lo=-M; hi=M
    first=r+ceil_div(lo-r,mm)*mm
    return [x for x in range(first,hi+1,mm) if x]

def tail_CB(q):
    C=q**4+10*q**3+12*q*q+8*q
    B=(q+2)*(q*q-4*q-4)
    return C,B

def reconstruct(G,q,N,t):
    if (G+1)%q:return None
    u=(G+1)//q; A=2*u+1; M=q*(q+4)
    R=A*t-2*N
    if R%M:return None
    Z=R//M
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
    return dict(G=G,q=q,u=u,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2,hlin=hlin,mlin=mlin,rlin=rlin)

def linear_gate(row,k):
    G,u,A=row['G'],row['u'],row['A'];K=10**k
    for z in ('a3','Z','X','D2','hlin','mlin','rlin'):
        if not(row[z]>0 and unit10(row[z])):return False,z
    if not(G//10<=row['a3']<G):return False,'DIG3'
    if not row['X']*K<ETA*u*G*G:return False,'X_RADIAL'
    if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False,'Z_RADIAL'
    return True,'PASS'

def F(row):return row['A']*row['X']**2+row['Z']*row['D2']

def psi_high(row,h):return 4*row['u']**2*10**(2*h)*row['D2']**2-row['A']*F(row)

def local_square_all(psi,n):
    for p in sp.factorint(n):
        if p in (2,5):continue
        r=psi%p
        if r and pow(r,(p-1)//2,p)!=1:return False,p,r
    return True,None,None

# ---- q=1 complete high-tail closure ----
def q1_complete_closure():
    # From N-strip + DIG3: t<=11. Safe alpha=m bounds for g>=h+6, ell>=6.
    mmax={1:161,2:16,3:1}
    raws=[]; stats={}
    for h in (1,2,3):
        st=Counter()
        Mloc=200*10**h
        for residue in range(15):
            g0=h+6
            g=g0+((residue-g0)%15)
            G=10**g; K=G*10**h
            u=G+1; A=2*u+1
            lo=-(2*ETA/K+Fraction(2*A,G)); hi=2*ETA*G*G/K
            for alpha in list(range(1,mmax[h]+1))+list(range(-1,-mmax[h]-1,-1)):
                for t in range(1,12):
                    num=alpha*(G//10)-21*t
                    if num%31:continue
                    N=num//31
                    if not(lo<Fraction(N,1)<hi):continue
                    st['tail_integral']+=1
                    if (N+t)%10:continue
                    q1=100*N*N+158*N*t+68*t*t
                    if (q1+alpha*((N+t)//10))%Mloc:continue
                    st['local_dcdc']+=1
                    row=reconstruct(G,1,N,t)
                    assert row is not None
                    # The local criterion is equivalent to exact DCDC in stabilized range.
                    assert F(row)%(2*10**(g+h))==0
                    ok,death=linear_gate(row,g+h)
                    st['linear_legal']+=int(ok)
                    raws.append(dict(h=h,residue=residue,g_rep=g,alpha=alpha,t=t,N=N,death=death))
        stats[h]=dict(st)
    # Exact complete residue census: three raw h=1 cells, no legal cells; h=2,3 empty.
    assert len(raws)==3
    assert all(x['h']==1 for x in raws)
    assert all(x['death']!='PASS' for x in raws)
    assert stats[2].get('local_dcdc',0)==0 and stats[3].get('local_dcdc',0)==0
    return stats,raws

# ---- fixed-small-q diagnostic ----
def small_q_census(gmax=1200):
    classes={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}
    H={7:4,11:6,17:6,19:6}
    rows=[]; totals={}
    for q in classes:
        b=vp(q+4,5); d=2*5**b; C,B=tail_CB(q); mod,rr=classes[q]
        for h in range(1,H[q]+1):
            mmax=(30*5**b*q**4-1)//10**h
            st=Counter()
            for g in range(h+6,gmax+1):
                if g%mod!=rr:continue
                G=10**g
                assert (G+1)%q==0
                D=G//d; k=g+h
                for t in range(1,3*q+8):
                    # alpha*D == -B*t mod C, |alpha|<=mmax
                    for alpha in solve_signed_linear(D,(-B*t)%C,C,mmax):
                        st['tail_integral']+=1
                        num=B*t+alpha*D
                        assert num%C==0
                        N=num//C
                        row=reconstruct(G,q,N,t)
                        if row is None:continue
                        st['reconstructed']+=1
                        ok,death=linear_gate(row,k)
                        if not ok:continue
                        st['linear_legal']+=1
                        if F(row)%(2*10**k):continue
                        st['dcdc']+=1
                        psi=psi_high(row,h)
                        qsq,pk,rk=local_square_all(psi,q)
                        if qsq:st['local_q_square']+=1
                        stack,ps,rs=local_square_all(psi,q*(q+4))
                        if stack:st['local_qq4_square']+=1
                        sq=False
                        if psi>=0:
                            z=isqrt(psi); sq=z*z==psi
                        st['global_square']+=int(sq)
                        rows.append(dict(q=q,h=h,g=g,alpha=alpha,t=t,N=N,psi_mod_q=psi%q,
                                         local_q_square=int(qsq),local_stack_square=int(stack),global_square=int(sq),
                                         first_nonresidue_prime=pk or ps or '',first_nonresidue_residue=rk or rs or ''))
            totals[(q,h)]=dict(st)
    return totals,rows

# ---- low-k pre-DCDC pseudo-family ----
def low_k_family_check():
    # q=1,N=7,t=3. This passes frozen RCE/digit/ten-unit/radial gates for sampled g,k<=g,
    # but F == 3 mod5, so it is always killed by DCDC. Closed-form identities are in report.
    for g in range(4,21):
        G=10**g; row=reconstruct(G,1,7,3); assert row is not None
        assert F(row)%5==3
        for k in range(1,g+1):
            ok,death=linear_gate(row,k)
            assert ok,(g,k,death)
            assert F(row)%(2*10**k)!=0
    return dict(g_sample='4..20',k_sample='1..g',pre_dcdc='PASS',F_mod_5=3,dcdc='FAIL')

def write_tsv(path,rows,fields):
    with path.open('w',encoding='utf-8') as f:
        f.write('\t'.join(fields)+'\n')
        for r in rows:f.write('\t'.join(str(r.get(x,'')) for x in fields)+'\n')

def main():
    q1stats,q1raw=q1_complete_closure()
    small,rows=small_q_census()
    low=low_k_family_check()
    surv=[]
    for r in q1raw:
        surv.append(dict(kind='q1_raw',q=1,h=r['h'],g=r['g_rep'],alpha=r['alpha'],t=r['t'],N=r['N'],death=r['death']))
    for r in rows:
        x=dict(kind='small_q_dcdc',q=r['q'],h=r['h'],g=r['g'],alpha=r['alpha'],t=r['t'],N=r['N'],death='LOCAL/ROOT')
        x.update({k:r[k] for k in ('psi_mod_q','local_q_square','local_stack_square','global_square','first_nonresidue_prime','first_nonresidue_residue')})
        surv.append(x)
    fields=['kind','q','h','g','alpha','t','N','death','psi_mod_q','local_q_square','local_stack_square','global_square','first_nonresidue_prime','first_nonresidue_residue']
    write_tsv(OUT/'A1_J2_TLRC7_survivors.tsv',surv,fields)
    lines=['A1 J2 TLRC7 search certificate','EXACT_ARITHMETIC=PASS','Q1_HIGH_TAIL=CLOSED']
    for h in (1,2,3):lines.append(f'Q1_h={h} {q1stats[h]}')
    lines.append('Q1_RAW_CELLS='+repr(q1raw))
    for key in sorted(small):lines.append(f'SMALL_Q_DIAG_{key}={small[key]}')
    lines.append('SMALL_Q_DCDC_ROWS='+str(len(rows)))
    lines.append('LOW_K_PRE_DCDC_FAMILY='+repr(low))
    lines.append('VERDICT_FULL_J2=OPEN')
    lines.append('SURVIVOR_FILE=A1_J2_TLRC7_survivors.tsv')
    (OUT/'A1_J2_TLRC7_search_certificate.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))

if __name__=='__main__':main()
