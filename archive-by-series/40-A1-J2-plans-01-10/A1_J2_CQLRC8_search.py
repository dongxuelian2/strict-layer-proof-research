#!/usr/bin/env python3
"""A1 J2 CQLRC8 exact h=0,1 diagnostic census.

This is diagnostic, not a global closure certificate. It scans q=7,11,17,19
through g<=1200 using tail congruence solving rather than raw alpha iteration.
All decisions are exact integer/Fraction arithmetic.
"""
from fractions import Fraction
from math import gcd,isqrt
from collections import Counter
from pathlib import Path
import sympy as sp

OUT=Path('/mnt/data')
ETA=Fraction(1299,500)


def vp(n,p):
    n=abs(int(n)); c=0
    if n==0:return 10**9
    while n%p==0:n//=p;c+=1
    return c

def unit10(n):return gcd(abs(int(n)),10)==1
def ceil_div(a,b):return -((-a)//b)

def solve_signed_linear(a,b,m,M):
    if M<1:return []
    d=gcd(a,m)
    if b%d:return []
    aa,bb,mm=a//d,b//d,m//d
    r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
    first=r+ceil_div(-M-r,mm)*mm
    return [x for x in range(first,M+1,mm) if x]

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
    num=(G-1)*t-q*N;den=2*(q+4)
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
def psi_delta(row,delta):
    aa=10**max(delta,0);bb=10**max(-delta,0)
    return 4*row['u']**2*aa**2*row['D2']**2-row['A']*bb**2*F(row)

def local_square_all(psi,n):
    for p in sp.factorint(n):
        if p in (2,5):continue
        r=psi%p
        if r and pow(r,(p-1)//2,p)!=1:return False,p,r
    return True,None,None


def scan_delta(delta,gmax=1200):
    assert delta in (0,1)
    classes={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}
    totals={};rows=[]
    for q,(mod,rr) in classes.items():
        b=vp(q+4,5);d=2*5**b;C,B=tail_CB(q)
        mmax=(30*5**b*q**4-1)//(10**delta)
        # h=1 uses the sharp high-tail t<3q+8; boundary h=0 uses reverse-tail t<9q.
        tmax=(3*q+7) if delta==1 else (9*q-1)
        st=Counter()
        gmin=max(6+delta,1)
        for g in range(gmin,gmax+1):
            if g%mod!=rr:continue
            G=10**g;D=G//d;k=g+delta
            for t in range(1,tmax+1):
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
                    ff=F(row)
                    if ff%(2*10**k):continue
                    st['dcdc']+=1
                    psi=psi_delta(row,delta)
                    qsq,pk,rk=local_square_all(psi,q)
                    stack,ps,rs=local_square_all(psi,q*(q+4))
                    st['local_q_square']+=int(qsq)
                    st['local_qq4_square']+=int(stack)
                    sq=psi>=0 and isqrt(psi)**2==psi
                    st['global_square']+=int(sq)
                    rows.append(dict(delta=delta,q=q,g=g,alpha=alpha,t=t,N=N,psi_mod_q=psi%q,
                                     local_q_square=int(qsq),local_stack_square=int(stack),global_square=int(sq),
                                     first_nonresidue_prime=pk or ps or '',first_nonresidue_residue=rk or rs or ''))
        totals[q]=dict(st)
    return totals,rows


def write_tsv(path,rows):
    fields=['delta','q','g','alpha','t','N','psi_mod_q','local_q_square','local_stack_square','global_square','first_nonresidue_prime','first_nonresidue_residue']
    with path.open('w',encoding='utf-8') as f:
        f.write('\t'.join(fields)+'\n')
        for r in rows:
            f.write('\t'.join(str(r.get(k,'')) for k in fields)+'\n')


def main():
    h0,r0=scan_delta(0)
    h1,r1=scan_delta(1)
    # Exact regression totals from this script.
    assert sum(x.get('dcdc',0) for x in h0.values())==79
    assert sum(x.get('global_square',0) for x in h0.values())==0
    assert sum(x.get('dcdc',0) for x in h1.values())==1
    assert len(r1)==1 and r1[0]['q']==11 and r1[0]['g']==471 and r1[0]['psi_mod_q']==8
    write_tsv(OUT/'A1_J2_CQLRC8_survivors.tsv',r0+r1)
    lines=['A1 J2 CQLRC8 h01 diagnostic','EXACT_ARITHMETIC=PASS','GMAX=1200']
    for q in (7,11,17,19):lines.append(f'H0_Q{q}={h0[q]}')
    for q in (7,11,17,19):lines.append(f'H1_Q{q}={h1[q]}')
    lines.append('H0_DCDC_TOTAL=79')
    lines.append('H0_GLOBAL_SQUARE=0')
    lines.append('H1_DCDC_TOTAL=1')
    lines.append('H1_Q11_G471_PSI_MOD11=8')
    lines.append('DIAGNOSTIC_ONLY=YES')
    lines.append('SURVIVOR_FILE=A1_J2_CQLRC8_survivors.tsv')
    (OUT/'A1_J2_CQLRC8_search_certificate.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))

if __name__=='__main__':main()
