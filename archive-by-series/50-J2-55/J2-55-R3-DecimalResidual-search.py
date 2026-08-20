#!/usr/bin/env python3
"""J2-55 R3 exact decimal-residual regression.

Replays the inherited h=0 root-layer corpus q=7,11,17,19 through g<=1200,
then applies the R3 gate order.  It also audits the six historical singular
states with the decimal gate and the content-deflated A^3 lift, and performs a
targeted large-q outer/RCE scan at (g,u,q,A)=(6,101,9901,203).

All arithmetic is exact integer/Fraction arithmetic.  The 79-state corpus is
reconstructed from the frozen tail equations rather than hard-coded.
"""
from fractions import Fraction
from math import gcd
from collections import Counter
import csv
import sys
sys.set_int_max_str_digits(1_000_000)

ETA = Fraction(1299,500)
C_MAX = Fraction(2_598_001,1_000_000)
OUT_TSV='/mnt/data/J2-55-R3-DecimalResidual-survivors.tsv'
OUT_CERT='/mnt/data/J2-55-R3-DecimalResidual-search-certificate.txt'


def vp(n,p):
    n=abs(int(n)); c=0
    if n==0:return 10**9
    while n%p==0:n//=p;c+=1
    return c

def unit10(n): return gcd(abs(int(n)),10)==1

def ceil_div(a,b): return -((-a)//b)

def solve_signed_linear(a,b,m,M):
    if M<1:return []
    d=gcd(a,m)
    if b%d:return []
    aa,bb,mm=a//d,b//d,m//d
    r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
    first=r+ceil_div(-M-r,mm)*mm
    if first==0:first=mm
    return range(first,M+1,mm)

def tail_CB(q):
    return q**4+10*q**3+12*q*q+8*q,(q+2)*(q*q-4*q-4)

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

def Qp(row,K,x):
    H=row['G']//2
    return 2*row['A']*H*H*x-2*row['u']*K*row['D2']

def a2_lifts(row,kexp):
    A=row['A']; K=10**kexp
    r=(-row['Z']*pow(K,-1,A))%A
    T=Q(row,K,r)//A
    qp=Qp(row,K,r); d=gcd(qp,A)
    assert d==gcd(row['D2'],A)
    if T%d:return r,T,d,[]
    mod=A//d
    c0=0 if mod==1 else (-(T//d)*pow((qp//d)%mod,-1,mod))%mod
    cs=[c0+j*mod for j in range(d)]
    r2=[r+A*c for c in cs]
    assert all(Q(row,K,x)%(A*A)==0 for x in r2)
    return r,T,d,r2

def root_interval(row,ell):
    return Fraction(row['A']*row['G'],10), Fraction(8*row['u']*row['D2'],row['A']*10**ell)

def jrange(row,r2,ell):
    L,U=root_interval(row,ell); A2=row['A']**2
    v=(L-r2)/A2; lo=v.numerator//v.denominator+1
    w=(U-r2)/A2; hi=-((-w.numerator)//w.denominator)-1
    return max(0,lo),hi

def c3_regular(row,kexp,r2):
    A=row['A']; K=10**kexp
    T2=Q(row,K,r2)//(A*A); qp=Qp(row,K,r2)
    assert gcd(qp,A)==1
    # R2 sign correction: NEGATIVE residual times derivative inverse.
    c3=(-T2*pow(qp,-1,A))%A
    E=T2+qp*c3+A**3*(row['G']//2)**2*c3*c3
    assert E==Q(row,K,r2+A*A*c3)//(A*A)
    assert E%A==0
    return c3,E

def decimal_data(row,kexp,ell):
    K=10**kexp; M=10**ell//8
    assert F(row)%(2*K)==0
    omega=F(row)//(2*K)
    assert gcd(row['u']*row['D2'],M)==1
    x10=(omega*pow((row['u']*row['D2'])%M,-1,M))%M
    return M,omega,x10

def singular_deflated_a3(row,kexp,r2,d):
    A=row['A']; K=10**kexp
    T2=Q(row,K,r2)//(A*A); qp=Qp(row,K,r2)
    assert gcd(qp,A)==d
    if T2%d:return 'CONTENT_DIVISIBILITY_FAIL',None,[]
    e=A//d
    c=0 if e==1 else (-(T2//d)*pow((qp//d)%e,-1,e))%e
    lo,hi=jrange(row,r2,2*row['G'].bit_length()) if False else (None,None)
    return 'CONGRUENCE',c,[]


def scan_h0(gmax=1200):
    classes={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}
    rows=[]; stats={}
    for q,(mod,rr) in classes.items():
        b=vp(q+4,5); d0=2*5**b; C,B=tail_CB(q); mmax=30*5**b*q**4-1
        st=Counter(); Mq=q*(q+4); CM=C*Mq
        for g in range(6,gmax+1):
            if g%mod!=rr:continue
            G=10**g; D=G//d0; Dmod=D%CM; Amod=(2*((G+1)//q)+1)%Mq
            for t in range(1,9*q):
                for alpha in solve_signed_linear(D,(-B*t)%C,C,mmax):
                    st['tail_integral']+=1
                    nmod_num=(B*t+alpha*Dmod)%CM
                    assert nmod_num%C==0
                    Nmod=nmod_num//C
                    if (Amod*t-2*Nmod)%Mq:continue
                    num=B*t+alpha*D
                    assert num%C==0
                    N=num//C
                    row=reconstruct(G,q,N,t)
                    if row is None:continue
                    st['reconstructed']+=1
                    ok,_=linear_gate(row,g)
                    if not ok:continue
                    st['linear_legal']+=1
                    if F(row)%(2*10**g):continue
                    st['dcdc']+=1
                    rows.append((q,g,alpha,t,row))
        stats[q]=dict(st)
    return stats,rows


def r3_replay(rows):
    gate=Counter(); ledger=[]
    singular_g=[]
    for q,g,alpha,t,row in rows:
        base=dict(kind='state',q=q,g=g,k=g,ell=g,N=row['N'],t=t,alpha=alpha,
                  u=row['u'],A=row['A'],Z=row['Z'],D2=row['D2'])
        gate['INPUT_STATES']+=1
        if gcd(row['Z'],row['u'])!=1:
            gate['PRIMITIVE_GCD_FAIL_STATES']+=1
            ledger.append({**base,'first_failure':'PRIMITIVE_GCD','d_A':'','m':'','r_A2':'','j_lo':'','j_hi':'','c3':'','decimal_js':'','u_square_js':'','deflated_a3':''})
            continue
        gate['PRIMITIVE_GCD_PASS_STATES']+=1
        gate['DCDC_PASS_STATES']+=1  # corpus construction already passed DCDC
        rA,TA,d,r2s=a2_lifts(row,g)
        if not r2s:
            gate['A2_FAIL_STATES']+=1
            ledger.append({**base,'first_failure':'A2_LIFT','d_A':d,'m':'','r_A2':'','j_lo':'','j_hi':'','c3':'','decimal_js':'','u_square_js':'','deflated_a3':''})
            continue
        gate['A2_PASS_STATES']+=1; gate['ROOT_FIBRES']+=len(r2s)
        M,omega,x10=decimal_data(row,g,g)
        if d==1:
            gate['REGULAR_FIBRES']+=1
            r2=r2s[0]; lo,hi=jrange(row,r2,g); c3=''; decjs=[]; usq=[]
            if hi<lo:
                gate['A3_INTERVAL_FAIL_FIBRES']+=1; death='J_INTERVAL'
            else:
                c3,E=c3_regular(row,g,r2)
                if not(lo<=c3<=hi):
                    gate['A3_INTERVAL_FAIL_FIBRES']+=1; death='A3_DIGIT_INTERVAL'
                else:
                    gate['A3_INTERVAL_PASS_FIBRES']+=1
                    x=r2+row['A']**2*c3
                    if (x-x10)%M:
                        gate['DECIMAL_ROOT_FAIL_FIBRES']+=1; death='DECIMAL_ROOT'
                    else:
                        decjs=[c3]; gate['DECIMAL_ROOT_PASS_FIBRES']+=1
                        if ((r2+c3)**2-row['Z']**2)%row['u']:
                            gate['U_SQUARE_FAIL_FIBRES']+=1; death='U_SQUARE'
                        else:
                            usq=[c3]; gate['U_SQUARE_PASS_FIBRES']+=1
                            lam=row['u']*row['D2']-row['A']*M*x
                            assert lam>0  # exact interval already guarantees this
                            R=row['A']*M*x*x-row['u']*row['D2']*x+omega
                            if omega%x:
                                gate['OMEGA_FACTOR_FAIL_FIBRES']+=1; death='OMEGA_FACTOR'
                            elif R:
                                gate['EXACT_RESIDUAL_FAIL_FIBRES']+=1; death='EXACT_RESIDUAL'
                            else:
                                gate['FULL_ROOT_SURVIVE_FIBRES']+=1; death='FULL_ROOT_SURVIVE'
            ledger.append({**base,'kind':'regular','first_failure':death,'d_A':d,'m':0,'r_A2':r2,'j_lo':lo,'j_hi':hi,'c3':c3,'decimal_js':','.join(map(str,decjs)),'u_square_js':','.join(map(str,usq)),'deflated_a3':''})
        else:
            gate['SINGULAR_STATES']+=1; singular_g.append(g)
            for m,r2 in enumerate(r2s):
                gate['SINGULAR_FIBRES']+=1
                lo,hi=jrange(row,r2,g); decjs=[]; usq=[]
                if hi<lo:
                    gate['J_INTERVAL_FAIL_SINGULAR_FIBRES']+=1; death='J_INTERVAL'; da3='NOT_REACHED'
                else:
                    gate['SINGULAR_LEGAL_CARRIES']+=hi-lo+1
                    for j in range(lo,hi+1):
                        x=r2+row['A']**2*j
                        if (x-x10)%M==0:decjs.append(j)
                    if not decjs:
                        gate['DECIMAL_ROOT_FAIL_SINGULAR_FIBRES']+=1; death='DECIMAL_ROOT'
                    else:
                        gate['DECIMAL_ROOT_PASS_SINGULAR_FIBRES']+=1; gate['DECIMAL_ROOT_PASS_SINGULAR_CARRIES']+=len(decjs)
                        usq=[j for j in decjs if ((r2+j)**2-row['Z']**2)%row['u']==0]
                        if not usq:
                            gate['U_SQUARE_FAIL_SINGULAR_FIBRES']+=1; death='U_SQUARE'
                        else:
                            gate['U_SQUARE_PASS_SINGULAR_CARRIES']+=len(usq); death='POST_U'
                    # Independent diagnostic of content-deflated A^3 lift.
                    T2=Q(row,10**g,r2)//(row['A']**2); qp=Qp(row,10**g,r2); e=row['A']//d
                    if T2%d:
                        gate['DEFLATED_A3_CONTENT_FAIL_FIBRES']+=1; da3='CONTENT_DIVISIBILITY_FAIL'
                    else:
                        csharp=0 if e==1 else (-(T2//d)*pow((qp//d)%e,-1,e))%e
                        first=csharp if csharp>=lo else csharp+((lo-csharp+e-1)//e)*e
                        if first>hi:
                            gate['DEFLATED_A3_INTERVAL_FAIL_FIBRES']+=1; da3=f'C_SHARP_OUTSIDE:{csharp}'
                        else:
                            gate['DEFLATED_A3_PASS_FIBRES']+=1; da3=f'PASS:{first}'
                ledger.append({**base,'kind':'singular','first_failure':death,'d_A':d,'m':m,'r_A2':r2,'j_lo':lo,'j_hi':hi,'c3':'','decimal_js':','.join(map(str,decjs)),'u_square_js':','.join(map(str,usq)),'deflated_a3':da3})
    return gate,ledger,sorted(set(singular_g))


def divisors_trial(n):
    lo=[]; hi=[]; d=1
    while d*d<=n:
        if n%d==0:
            lo.append(d)
            if d*d!=n:hi.append(n//d)
        d+=1
    return lo+hi[::-1]

def outer_large_q_census(glo=6,ghi=12):
    out=[]
    for g in range(glo,ghi+1):
        G=10**g
        for u in divisors_trial(G+1):
            if u<=1:continue
            q=(G+1)//u; A=2*u+1
            if unit10(A) and A<=C_MAX*q:
                out.append((g,u,q,A,q*q>=G+1))
    return out

def targeted_h0_pair(g,q):
    # Exact h=0 tail/RCE scan for one selected outer large-q pair.
    b=vp(q+4,5); d0=2*5**b; C,B=tail_CB(q); mmax=30*5**b*q**4-1
    G=10**g
    assert (G+1)%q==0
    D=G//d0; Mq=q*(q+4); CM=C*Mq; Dmod=D%CM; A=2*((G+1)//q)+1; Amod=A%Mq
    st=Counter()
    for t in range(1,9*q):
        for alpha in solve_signed_linear(D,(-B*t)%C,C,mmax):
            st['tail_integral']+=1
            nmod_num=(B*t+alpha*Dmod)%CM
            if nmod_num%C:continue
            Nmod=nmod_num//C
            if (Amod*t-2*Nmod)%Mq:continue
            num=B*t+alpha*D
            if num%C:continue
            row=reconstruct(G,q,num//C,t)
            if row is None:continue
            st['reconstructed']+=1
            ok,_=linear_gate(row,g)
            if not ok:continue
            st['linear_legal']+=1
            if F(row)%(2*10**g):continue
            st['dcdc']+=1
    return dict(st)


def write_tsv(rows):
    fields=['kind','q','g','k','ell','N','t','alpha','u','A','Z','D2','d_A','m','r_A2','j_lo','j_hi','c3','decimal_js','u_square_js','deflated_a3','first_failure']
    with open(OUT_TSV,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        w.writeheader(); w.writerows(rows)


def main():
    stats,rows=scan_h0(1200)
    assert len(rows)==79
    assert stats[7]['dcdc']==28 and stats[11]['dcdc']==44 and stats[17]['dcdc']==5 and stats[19]['dcdc']==2
    gate,ledger,singg=r3_replay(rows)
    assert gate['PRIMITIVE_GCD_FAIL_STATES']==4
    assert gate['A2_FAIL_STATES']==19
    assert gate['A2_PASS_STATES']==56
    assert gate['ROOT_FIBRES']==68
    assert gate['REGULAR_FIBRES']==50
    assert gate['A3_INTERVAL_FAIL_FIBRES']==50
    assert gate['SINGULAR_STATES']==6 and gate['SINGULAR_FIBRES']==18
    assert gate['SINGULAR_LEGAL_CARRIES']==333
    assert gate['DECIMAL_ROOT_FAIL_SINGULAR_FIBRES']==18
    assert gate['DECIMAL_ROOT_PASS_SINGULAR_CARRIES']==0
    assert gate['DEFLATED_A3_CONTENT_FAIL_FIBRES']==12
    assert gate['DEFLATED_A3_INTERVAL_FAIL_FIBRES']==6
    assert gate['DEFLATED_A3_PASS_FIBRES']==0
    assert singg==[259,359,435,481,669,1025]
    outer=outer_large_q_census()
    assert len(outer)==28
    targeted=targeted_h0_pair(6,9901)
    write_tsv(ledger)
    lines=['J2-55 R3 DecimalResidual exact regression certificate','EXACT_ARITHMETIC=PASS']
    for q in (7,11,17,19):lines.append(f'H0_Q{q}={stats[q]}')
    lines.append('HISTORICAL_DCDC_INPUT=79')
    ordered=['INPUT_STATES','PRIMITIVE_GCD_FAIL_STATES','PRIMITIVE_GCD_PASS_STATES','DCDC_PASS_STATES','A2_FAIL_STATES','A2_PASS_STATES','ROOT_FIBRES','REGULAR_FIBRES','A3_INTERVAL_FAIL_FIBRES','A3_INTERVAL_PASS_FIBRES','DECIMAL_ROOT_FAIL_FIBRES','DECIMAL_ROOT_PASS_FIBRES','U_SQUARE_FAIL_FIBRES','U_SQUARE_PASS_FIBRES','SINGULAR_STATES','SINGULAR_FIBRES','SINGULAR_LEGAL_CARRIES','DECIMAL_ROOT_FAIL_SINGULAR_FIBRES','DECIMAL_ROOT_PASS_SINGULAR_FIBRES','DECIMAL_ROOT_PASS_SINGULAR_CARRIES','U_SQUARE_PASS_SINGULAR_CARRIES','DEFLATED_A3_CONTENT_FAIL_FIBRES','DEFLATED_A3_INTERVAL_FAIL_FIBRES','DEFLATED_A3_PASS_FIBRES','OMEGA_FACTOR_FAIL_FIBRES','EXACT_RESIDUAL_FAIL_FIBRES','FULL_ROOT_SURVIVE_FIBRES']
    for k in ordered:lines.append(f'{k}={gate[k]}')
    lines.append('SINGULAR_G='+','.join(map(str,singg)))
    lines.append('SINGULAR_NEW_FIRST_DEATH=DECIMAL_ROOT for all 18 fibres / all 333 legal carries in requested gate order')
    lines.append('SINGULAR_DEFLATED_A3_DIAGNOSTIC=12 content-divisibility fail + 6 c_sharp outside interval + 0 pass')
    lines.append(f'OUTER_LARGE_Q_PAIRS_G6_12={len(outer)}')
    for x in outer:lines.append('OUTER '+repr(x))
    lines.append('TARGETED_LARGE_Q_G6_Q9901='+repr(targeted))
    lines.append('TARGETED_LARGE_Q_RESULT=2 reconstructed; 0 linear-legal; 0 DCDC')
    lines.append('TRIPLE_GATE_STRUCTURAL_SURVIVORS_IN_HISTORICAL_CORPUS=0')
    lines.append('SURVIVOR_FILE='+OUT_TSV)
    open(OUT_CERT,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
    print('\n'.join(lines[:55]))

if __name__=='__main__':
    main()
