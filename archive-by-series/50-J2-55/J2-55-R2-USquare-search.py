from fractions import Fraction
from math import gcd
from collections import Counter
import sys,time
sys.set_int_max_str_digits(1000000)
ETA=Fraction(1299,500)

def vp(n,p):
 c=0
 while n and n%p==0:n//=p;c+=1
 return c

def unit10(n): return gcd(abs(n),10)==1

def ceil_div(a,b): return -((-a)//b)

def solve_signed_linear(a,b,m,M):
 d=gcd(a,m)
 if b%d:return []
 aa,bb,mm=a//d,b//d,m//d
 r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
 first=r+ceil_div(-M-r,mm)*mm
 return range(first,M+1,mm)

def tail_CB(q): return q**4+10*q**3+12*q*q+8*q,(q+2)*(q*q-4*q-4)

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
  if not(row[z]>0 and unit10(row[z])):return False
 if not(G//10<=row['a3']<G):return False
 if not row['X']*K < ETA*u*G*G:return False
 if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False
 return True

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
 G,A,u,D2=row['G'],row['A'],row['u'],row['D2']
 return Fraction(A*G,10), Fraction(8*u*D2,A*10**ell)

def jrange(row,r2,ell):
 L,U=root_interval(row,ell); A2=row['A']**2
 lo=(L.numerator*A2 and (L-r2)//A2) # unused
 # exact open endpoints
 flo=(L-r2).numerator//(L-r2).denominator
 lo=flo//A2 if False else 0
 # use Fraction division
 v=(L-r2)/A2
 lo=v.numerator//v.denominator+1
 w=(U-r2)/A2
 hi=-((-w.numerator)//w.denominator)-1
 return max(0,lo),hi

def proc(row,kexp,ell):
 r,T,d,r2s=a2_lifts(row,kexp)
 out={'d':d,'r':r,'T':T,'r2s':r2s,'usq':[],'jr':[]}
 for i,r2 in enumerate(r2s):
  lo,hi=jrange(row,r2,ell)
  if hi>=lo:
   out['jr'].append((i,lo,hi))
   for j in range(lo,hi+1):
    if ((r2+j)**2-row['Z']**2)%row['u']==0:
     out['usq'].append((i,j))
 return out

def scan(qs=(7,11,17,19),gmax=1200, stop_sing=None):
 classes={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}
 allrows=[];stats={}; sing=[]
 for q in qs:
  mod,rr=classes[q]; b=vp(q+4,5); d0=2*5**b; C,B=tail_CB(q); mmax=30*5**b*q**4-1; st=Counter()
  for g in range(6,gmax+1):
   if g%mod!=rr: continue
   G=10**g; D=G//d0; kexp=g; ell=g; Mq=q*(q+4); CM=C*Mq; Dmod=D%CM; u=(G+1)//q; A=2*u+1; Amod=A%Mq
   for t in range(1,9*q):
    for alpha in solve_signed_linear(D,(-B*t)%C,C,mmax):
     if alpha==0: continue
     st['tail']+=1
     nmod_num=(B*t+alpha*Dmod)%CM
     assert nmod_num%C==0
     Nmod=nmod_num//C
     if (Amod*t-2*Nmod)%Mq:continue
     num=B*t+alpha*D
     assert num%C==0
     N=num//C; row=reconstruct(G,q,N,t)
     if row is None:continue
     st['recon']+=1
     if not linear_gate(row,kexp):continue
     st['linear']+=1
     if F(row)%(2*10**kexp):continue
     st['dcdc']+=1
     pr=proc(row,kexp,ell); st['a2']+=bool(pr['r2s']);st['deg']+=pr['d']>1;st['j']+=sum(b-a+1 for _,a,b in pr['jr']);st['usq']+=len(pr['usq'])
     rec={**row,'g':g,'k':kexp,'ell':ell,'alpha':alpha,**pr}
     allrows.append(rec)
     if pr['d']==3 and pr['r2s']:
      sing.append(rec)
      if stop_sing and len(sing)>=stop_sing:return stats,allrows,sing
  stats[q]=dict(st)
 return stats,allrows,sing



def q11_state(g):
    q=11; alpha=152510; t=31
    b=vp(q+4,5); d0=2*5**b
    C,B=tail_CB(q); G=10**g
    assert (G+1)%q==0
    num=B*t+alpha*(G//d0); assert num%C==0
    N=num//C
    row=reconstruct(G,q,N,t); assert row is not None
    assert linear_gate(row,g+1)
    assert F(row)%(2*10**(g+1))==0
    row.update(g=g,k=g+1,ell=g-1,alpha=alpha)
    return row


def c3_for_regular(z):
    A=z['A']; K=10**z['k']; r2=z['r2s'][0]
    T2=Q(z,K,r2)//(A*A); qp=Qp(z,K,r2)
    assert gcd(qp,A)==1
    c3=(-T2*pow(qp,-1,A))%A
    assert Q(z,K,r2+A*A*c3)%(A**3)==0
    E=Q(z,K,r2+A*A*c3)//(A*A)
    return r2,c3,E


def divisors_trial(n):
    lo=[];hi=[];d=1
    while d*d<=n:
        if n%d==0:
            lo.append(d)
            if d*d!=n: hi.append(n//d)
        d+=1
    return lo+hi[::-1]


def large_q_outer_diagnostic(glo=6,ghi=12):
    rows=[]
    Cmax=Fraction(2598001,1000000)
    for g in range(glo,ghi+1):
        G=10**g
        for u in divisors_trial(G+1):
            if u<=1: continue
            q=(G+1)//u; A=2*u+1
            if not unit10(A): continue
            if A<=Cmax*q:
                rows.append((g,u,q,A,q*q>=G+1))
    return rows


def r2_full_analysis():
    stats,rows,sing=scan(qs=(7,11,17,19),gmax=1200)
    gate=Counter()
    fibre_rows=[]
    reg_examples=[]
    singular_rows=[]
    Cmax=Fraction(2598001,1000000)

    for z in rows:
        gate['INPUT_STATES']+=1
        if gcd(z['Z'],z['u'])!=1:
            gate['PRIMITIVE_GCD_FAIL_STATES']+=1
            fibre_rows.append(dict(kind='state',q=z['q'],g=z['g'],k=z['k'],ell=z['ell'],N=z['N'],t=z['t'],alpha=z['alpha'],u=z['u'],A=z['A'],Z=z['Z'],D2=z['D2'],d_A=z['d'],e='',m='',r_A2='',r_A2_mod_u='',bridge_delta_mod_u='',j_lo='',j_hi='',c3='',u_square_js='',unitary_sign_cell='NONE',first_failure='PRIMITIVE_GCD'))
            continue
        gate['PRIMITIVE_GCD_PASS_STATES']+=1
        if not z['r2s']:
            gate['A2_LIFT_FAIL_STATES']+=1
            fibre_rows.append(dict(kind='state',q=z['q'],g=z['g'],k=z['k'],ell=z['ell'],N=z['N'],t=z['t'],alpha=z['alpha'],u=z['u'],A=z['A'],Z=z['Z'],D2=z['D2'],d_A=z['d'],e='',m='',r_A2='',r_A2_mod_u='',bridge_delta_mod_u='',j_lo='',j_hi='',c3='',u_square_js='',unitary_sign_cell='NONE',first_failure='A2_LIFT'))
            continue
        gate['A2_SOLVABLE_STATES']+=1
        gate['INPUT_ROOT_FIBRES']+=len(z['r2s'])
        if z['d']==1:
            gate['REGULAR_FIBRES']+=1
            r2,c3,E=c3_for_regular(z)
            lo,hi=jrange(z,r2,z['ell'])
            singleton = z['A']>Cmax*z['q']
            gate['REGULAR_SINGLETON_FIBRES']+=int(singleton)
            if hi<lo:
                gate['J_INTERVAL_FAIL_FIBRES']+=1
                failure='J_INTERVAL'
            elif singleton and not (lo<=c3<=hi):
                gate['A3_DIGIT_FAIL_FIBRES']+=1
                failure='A3_DIGIT'
            else:
                # This branch is not reached in the inherited 79-cell ledger,
                # but keep the exact pipeline for future/replayed data.
                js=[j for j in range(lo,hi+1) if ((r2+j)**2-z['Z']**2)%z['u']==0]
                if not js:
                    gate['U_SQUARE_FAIL_FIBRES']+=1; failure='U_SQUARE'
                else:
                    gate['U_SQUARE_SURVIVE_FIBRES']+=1
                    exact=[]
                    for j in js:
                        if Q(z,10**z['k'],r2+z['A']**2*j)==0: exact.append(j)
                    if exact:
                        gate['EXACT_ROOT_SURVIVE_FIBRES']+=1;failure='EXACT_ROOT_SURVIVOR'
                    else:
                        gate['EXACT_CARRY_FAIL_FIBRES']+=1;failure='EXACT_CARRY'
                fibre_rows.append(dict(kind='regular',q=z['q'],g=z['g'],k=z['k'],ell=z['ell'],N=z['N'],t=z['t'],alpha=z['alpha'],u=z['u'],A=z['A'],Z=z['Z'],D2=z['D2'],d_A=1,e=z['A'],m=0,r_A2=r2,r_A2_mod_u=r2%z['u'],bridge_delta_mod_u=0,j_lo=lo,j_hi=hi,c3=c3,u_square_js=','.join(map(str,js)),unitary_sign_cell=('PRESENT' if js else 'NONE'),first_failure=failure))
                continue
            fibre_rows.append(dict(kind='regular',q=z['q'],g=z['g'],k=z['k'],ell=z['ell'],N=z['N'],t=z['t'],alpha=z['alpha'],u=z['u'],A=z['A'],Z=z['Z'],D2=z['D2'],d_A=1,e=z['A'],m=0,r_A2=r2,r_A2_mod_u=r2%z['u'],bridge_delta_mod_u=0,j_lo=lo,j_hi=hi,c3=c3,u_square_js='',unitary_sign_cell='NONE',first_failure=failure))
            if len(reg_examples)<12:
                reg_examples.append((z['q'],z['g'],lo,hi,c3,((r2+c3)**2-z['Z']**2)%z['u'],E))
        else:
            d=z['d'];e=z['A']//d;r0=z['r2s'][0]
            gate['SINGULAR_SOLVABLE_STATES']+=1
            for m,r2 in enumerate(z['r2s']):
                assert (r2-r0-m*e)%z['u']==0
                lo,hi=jrange(z,r2,z['ell'])
                if hi<lo:
                    gate['J_INTERVAL_FAIL_FIBRES']+=1;js=[];failure='J_INTERVAL'
                else:
                    js=[j for j in range(lo,hi+1) if ((r2+j)**2-z['Z']**2)%z['u']==0]
                    if js:
                        gate['U_SQUARE_SURVIVE_FIBRES']+=1
                        exact=[j for j in js if Q(z,10**z['k'],r2+z['A']**2*j)==0]
                        if exact:
                            gate['EXACT_ROOT_SURVIVE_FIBRES']+=1;failure='EXACT_ROOT_SURVIVOR'
                        else:
                            gate['EXACT_CARRY_FAIL_FIBRES']+=1;failure='EXACT_CARRY'
                    else:
                        gate['U_SQUARE_FAIL_FIBRES']+=1;failure='U_SQUARE'
                rec=dict(kind='singular',q=z['q'],g=z['g'],k=z['k'],ell=z['ell'],N=z['N'],t=z['t'],alpha=z['alpha'],u=z['u'],A=z['A'],Z=z['Z'],D2=z['D2'],d_A=d,e=e,m=m,r_A2=r2,r_A2_mod_u=r2%z['u'],bridge_delta_mod_u=(r2-r0)%z['u'],j_lo=lo,j_hi=hi,c3='',u_square_js=','.join(map(str,js)),unitary_sign_cell=('PRESENT' if js else 'NONE'),first_failure=failure)
                fibre_rows.append(rec);singular_rows.append(rec)

    # Targeted pseudo states: they must die before coprime unitary allocation.
    q11=[]
    for g in (471,63501):
        z=q11_state(g); pr=proc(z,z['k'],z['ell'])
        q11.append((g,gcd(z['Z'],z['u']),pr['jr'],pr['usq']))
        assert gcd(z['Z'],z['u'])==13 and not pr['usq']

    # The inherited diagnostic has only small q, so R5 has no true large-q root
    # fibre.  We nevertheless enumerate outer pairs with A<=Cq to certify that
    # the large-q chamber itself is structurally nonempty and must be handled
    # by the uniform theorem rather than by this regression.
    outer_large=large_q_outer_diagnostic()

    fields=['kind','q','g','k','ell','N','t','alpha','u','A','Z','D2','d_A','e','m','r_A2','r_A2_mod_u','bridge_delta_mod_u','j_lo','j_hi','c3','u_square_js','unitary_sign_cell','first_failure']
    out='/mnt/data/J2-55-R2-USquare-survivors.tsv'
    with open(out,'w',encoding='utf-8',newline='') as f:
        import csv
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(fibre_rows)

    # Assertions pin down the exact R2 regression claimed in the report.
    assert gate['INPUT_STATES']==79
    assert gate['PRIMITIVE_GCD_FAIL_STATES']==4
    assert gate['A2_LIFT_FAIL_STATES']==19
    assert gate['A2_SOLVABLE_STATES']==56
    assert gate['INPUT_ROOT_FIBRES']==68
    assert gate['REGULAR_FIBRES']==50
    assert gate['SINGULAR_SOLVABLE_STATES']==6
    assert gate['REGULAR_SINGLETON_FIBRES']==50
    assert gate['J_INTERVAL_FAIL_FIBRES']==1
    assert gate['A3_DIGIT_FAIL_FIBRES']==49
    assert gate['U_SQUARE_FAIL_FIBRES']==18
    assert gate['U_SQUARE_SURVIVE_FIBRES']==0
    assert gate['EXACT_ROOT_SURVIVE_FIBRES']==0
    assert len(singular_rows)==18
    assert all(x['d_A']==3 for x in singular_rows)
    assert all(x['first_failure']=='U_SQUARE' for x in singular_rows)

    lines=['J2-55 R2 exact regression certificate','EXACT_ARITHMETIC=PASS']
    ordered_keys=['INPUT_STATES','PRIMITIVE_GCD_FAIL_STATES','PRIMITIVE_GCD_PASS_STATES','A2_LIFT_FAIL_STATES','A2_SOLVABLE_STATES','INPUT_ROOT_FIBRES','REGULAR_FIBRES','REGULAR_SINGLETON_FIBRES','SINGULAR_SOLVABLE_STATES','J_INTERVAL_FAIL_FIBRES','A3_DIGIT_FAIL_FIBRES','U_SQUARE_FAIL_FIBRES','U_SQUARE_SURVIVE_FIBRES','EXACT_CARRY_FAIL_FIBRES','EXACT_ROOT_SURVIVE_FIBRES']
    for k in ordered_keys: lines.append(f'{k}={gate[k]}')
    lines.append('SINGULAR_SOLVABLE_G=' + ','.join(str(x) for x in sorted({r['g'] for r in singular_rows})))
    lines.append('SINGULAR_CONTENT_BRIDGE_ALL_18=PASS')
    lines.append('SINGULAR_ALL_USQ_FAIL=PASS')
    for g,gzu,jr,usq in q11:
        lines.append(f'Q11_G{g}_GCD_Z_U={gzu};J_RANGES={jr};USQ={usq};FIRST_DEATH=PRIMITIVE_GCD')
    lines.append(f'R5_TRUE_LARGE_Q_ROOT_FIBRES_IN_INHERITED_79=0')
    lines.append(f'R5_OUTER_LARGE_Q_PAIRS_g6_12={len(outer_large)}')
    for g,u,q,A,uqflag in outer_large[:20]: lines.append(f'R5_OUTER g={g} u={u} q={q} A={A} q2_ge_G1={uqflag}')
    lines.append('REGULAR_EXAMPLES=(q,g,jlo,jhi,c3,USQ_residual,E)')
    for x in reg_examples: lines.append(repr(x))
    lines.append('SURVIVOR_FILE=J2-55-R2-USquare-survivors.tsv')
    cert='/mnt/data/J2-55-R2-USquare-search-certificate.txt'
    open(cert,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
    print('\n'.join(lines[:40]))
    return gate,fibre_rows,singular_rows,outer_large

if __name__=='__main__':
    r2_full_analysis()
