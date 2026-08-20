#!/usr/bin/env python3
"""A1 J2 PRCC10 exact primitive-root/carry regression.

Replays the inherited h=0 exact diagnostic (q=7,11,17,19,g<=1200),
processes its 79 DCDC root-layer pseudo-cells through the A^2 lift, exact root
interval and U-square carry sieve, and separately audits q=11,g=471 and 63501.
Also records a reverse pre-DCDC regression (q=1,N=7,t=3) to check scope.
All decisions are exact integer/Fraction arithmetic.
"""
from fractions import Fraction
from math import gcd
from collections import Counter
from pathlib import Path
import sys
sys.set_int_max_str_digits(1000000)
sys.path.insert(0,'/mnt/data')
from A1_J2_PRCC10_Aroot import RootState,Q,a2_lifts,carry_polynomial_coeffs
from A1_J2_PRCC10_CRT import ETA,root_interval,j_interval,direct_u_square_candidates,carry_bound_rhs

OUT=Path('/mnt/data')


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
    return q**4+10*q**3+12*q*q+8*q,(q+2)*(q*q-4*q-4)

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

def linear_gate(row,kexp):
    G,u,A=row['G'],row['u'],row['A']; K=10**kexp
    for z in ('a3','Z','X','D2','hlin','mlin','rlin'):
        if not(row[z]>0 and unit10(row[z])):return False,z
    if not(G//10<=row['a3']<G):return False,'DIG3'
    if not row['X']*K<ETA*u*G*G:return False,'X_RADIAL'
    if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False,'Z_RADIAL'
    return True,'PASS'

def F(row):return row['A']*row['X']**2+row['Z']*row['D2']

def root_state(row,kexp):
    return RootState(row['G'],10**kexp,row['u'],row['A'],row['Z'],row['X'],row['D2'])

def suffix(n,d=12):
    return f'{n%(10**d):0{d}d}'

def process_root_cell(row,kexp,ell,kind,meta=None):
    s=root_state(row,kexp); A=row['A']; A2=A*A
    lift=a2_lifts(s)
    L,U=root_interval(row['G'],A,row['u'],row['D2'],ell)
    out={
        'kind':kind,'q':row['q'],'g':len(str(row['G']))-1,'k':kexp,'ell':ell,
        'N':row['N'],'t':row['t'],'alpha':(meta or {}).get('alpha',''),
        'gcd_D2_A':gcd(row['D2'],A),'gcd_Z_u':gcd(row['Z'],row['u']),
        'A2_SOLVABLE':int(lift['solvable']),'A2_CLASS_COUNT':len(lift['rA2_classes']),
        'rA_suffix':suffix(lift['rA']),'TA_suffix':suffix(lift['TA']),
        'rA2_suffixes':','.join(suffix(x) for x in lift['rA2_classes'][:20]),
        'J_RANGE_COUNT':0,'U_SQUARE_CANDIDATE_COUNT':0,'EXACT_ROOT_COUNT':0,
        'FIRST_DEATH_GATE':'', 'J_RANGES':'', 'U_SQUARE_JS':'',
        'ROOT_LOWER_NUM':L.numerator,'ROOT_LOWER_DEN':L.denominator,
        'ROOT_UPPER_NUM':U.numerator,'ROOT_UPPER_DEN':U.denominator,
    }
    if not lift['solvable']:
        out['FIRST_DEATH_GATE']='A2_LIFT'
        return out
    jranges=[]; usq=[]; exact=[]
    for idx,r2 in enumerate(lift['rA2_classes']):
        jlo,jhi=j_interval(r2,A,L,U)
        if jhi>=jlo:
            # Exact universal theorem check, not a heuristic.
            assert Fraction(jhi,1) < carry_bound_rhs(row['q'],ell)
            jranges.append((idx,jlo,jhi))
            out['J_RANGE_COUNT'] += jhi-jlo+1
            js=direct_u_square_candidates(r2,jlo,jhi,row['Z'],row['u'])
            for j in js:
                usq.append((idx,j))
                x=r2+A2*j
                if Q(s,x)==0:
                    exact.append((idx,j,x))
    out['U_SQUARE_CANDIDATE_COUNT']=len(usq)
    out['EXACT_ROOT_COUNT']=len(exact)
    out['J_RANGES']=';'.join(f'{i}:{lo}..{hi}' for i,lo,hi in jranges)
    out['U_SQUARE_JS']=';'.join(f'{i}:{j}' for i,j in usq)
    if gcd(row['Z'],row['u'])!=1:
        out['FIRST_DEATH_GATE']='PRIMITIVE_GCD(Z,u)'
    elif not jranges:
        out['FIRST_DEATH_GATE']='J_INTERVAL'
    elif not usq:
        out['FIRST_DEATH_GATE']='U_SQUARE'
    elif not exact:
        out['FIRST_DEATH_GATE']='EXACT_CARRY_POLYNOMIAL'
    else:
        out['FIRST_DEATH_GATE']='EXACT_ROOT_SURVIVOR'
    return out


def scan_h0(gmax=1200):
    classes={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}
    rows=[]; stats={}
    for q,(mod,rr) in classes.items():
        b=vp(q+4,5); d=2*5**b; C,B=tail_CB(q)
        mmax=30*5**b*q**4-1
        st=Counter()
        for g in range(6,gmax+1):
            if g%mod!=rr:continue
            G=10**g; D=G//d; kexp=g; ell=g
            for t in range(1,9*q):
                # alpha integrality first; before constructing the huge N, use the
                # exact quotient modulo C*M to test the RCE3 Z-integrality gate.
                Mq=q*(q+4); CM=C*Mq; Dmod=D%CM; Amod=(2*((G+1)//q)+1)%Mq
                for alpha in solve_signed_linear(D,(-B*t)%C,C,mmax):
                    st['tail_integral']+=1
                    nmod_num=(B*t + alpha*Dmod) % CM
                    assert nmod_num%C==0
                    Nmod=nmod_num//C
                    if (Amod*t-2*Nmod)%Mq: continue
                    num=B*t+alpha*D
                    assert num%C==0
                    N=num//C
                    row=reconstruct(G,q,N,t)
                    if row is None:continue
                    st['reconstructed']+=1
                    ok,_=linear_gate(row,kexp)
                    if not ok:continue
                    st['linear_legal']+=1
                    if F(row)%(2*10**kexp):continue
                    st['dcdc']+=1
                    pr=process_root_cell(row,kexp,ell,'h0_boundary',{'alpha':alpha})
                    rows.append(pr)
                    st['a2_solvable']+=pr['A2_SOLVABLE']
                    st['degenerate']+=int(pr['gcd_D2_A']>1)
                    st['primitive_gcd_pass']+=int(pr['gcd_Z_u']==1)
                    st['j_candidates']+=pr['J_RANGE_COUNT']
                    st['u_square_candidates']+=pr['U_SQUARE_CANDIDATE_COUNT']
                    st['exact_roots']+=pr['EXACT_ROOT_COUNT']
        stats[q]=dict(st)
    assert sum(s.get('dcdc',0) for s in stats.values())==79,stats
    return stats,rows


def q11_state(g):
    q=11; delta=1; alpha=152510; t=31
    b=vp(q+4,5); d=2*5**b
    c=q**3+10*q*q+12*q+8; C=q*c
    B=(q+2)*(q*q-4*q-4)
    G=10**g; assert (G+1)%q==0
    num=B*t+alpha*(G//d); assert num%C==0
    N=num//C
    row=reconstruct(G,q,N,t); assert row is not None
    ok,death=linear_gate(row,g+1); assert ok,death
    assert F(row)%(2*10**(g+1))==0
    return row,alpha


def reverse_pre_dcdc_regression(g=12,kexp=6):
    # Frozen TLRC7 low-k family q=1,N=7,t=3: legal before DCDC and F==3 mod 5.
    G=10**g; row=reconstruct(G,1,7,3); assert row is not None
    ok,death=linear_gate(row,kexp); assert ok,death
    assert F(row)%5==3
    return {
        'kind':'reverse_pre_dcdc','q':1,'g':g,'k':kexp,'ell':2*g-kexp,'N':7,'t':3,
        'DCDC':'FAIL_F_MOD_5_EQ_3','A_ROOT_SCOPE':'FORMULA_DEFINED_BUT_ROOT_LAYER_NOT_REACHED',
        'FIRST_DEATH_GATE':'DCDC'
    }


def write_tsv(path,rows):
    fields=['kind','q','g','k','ell','N','t','alpha','gcd_D2_A','gcd_Z_u','A2_SOLVABLE','A2_CLASS_COUNT',
            'rA_suffix','TA_suffix','rA2_suffixes','J_RANGE_COUNT','J_RANGES','U_SQUARE_CANDIDATE_COUNT','U_SQUARE_JS',
            'EXACT_ROOT_COUNT','FIRST_DEATH_GATE']
    with path.open('w',encoding='utf-8') as f:
        f.write('\t'.join(fields)+'\n')
        for r in rows:
            f.write('\t'.join(str(r.get(k,'')) for k in fields)+'\n')


def main():
    stats,h0rows=scan_h0(1200)
    targeted=[]
    for g in (471,63501):
        row,alpha=q11_state(g)
        targeted.append(process_root_cell(row,g+1,g-1,'q11_fixed_fibre',{'alpha':alpha}))
    reverse=reverse_pre_dcdc_regression()
    allrows=h0rows+targeted
    write_tsv(OUT/'A1_J2_PRCC10_survivors.tsv',allrows)

    h0=Counter()
    for r in h0rows:
        h0['DCDC']+=1; h0['A2_SOLVABLE']+=r['A2_SOLVABLE']; h0['DERIVATIVE_DEGENERATE']+=int(r['gcd_D2_A']>1)
        h0['PRIMITIVE_GCD_PASS']+=int(r['gcd_Z_u']==1); h0['J_CANDIDATES']+=r['J_RANGE_COUNT']
        h0['U_SQUARE_CANDIDATES']+=r['U_SQUARE_CANDIDATE_COUNT']; h0['EXACT_ROOTS']+=r['EXACT_ROOT_COUNT']
    lines=['A1 J2 PRCC10 exact root-carry regression','EXACT_ARITHMETIC=PASS','H0_GMAX=1200']
    for q in (7,11,17,19): lines.append(f'H0_Q{q}={stats[q]}')
    for k,v in h0.items(): lines.append(f'H0_{k}={v}')
    for r in targeted:
        lines += [
            f"Q11_G{r['g']}_GCD_D2_A={r['gcd_D2_A']}",
            f"Q11_G{r['g']}_GCD_Z_U={r['gcd_Z_u']}",
            f"Q11_G{r['g']}_RA_SUFFIX={r['rA_suffix']}",
            f"Q11_G{r['g']}_RA2_SUFFIXES={r['rA2_suffixes']}",
            f"Q11_G{r['g']}_J_RANGES={r['J_RANGES']}",
            f"Q11_G{r['g']}_U_SQUARE_CANDIDATES={r['U_SQUARE_CANDIDATE_COUNT']}",
            f"Q11_G{r['g']}_EXACT_ROOTS={r['EXACT_ROOT_COUNT']}",
            f"Q11_G{r['g']}_FIRST_DEATH={r['FIRST_DEATH_GATE']}",
        ]
    lines += [f'REVERSE_REGRESSION={reverse}', 'SURVIVOR_FILE=A1_J2_PRCC10_survivors.tsv']
    (OUT/'A1_J2_PRCC10_search_certificate.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))

if __name__=='__main__': main()
