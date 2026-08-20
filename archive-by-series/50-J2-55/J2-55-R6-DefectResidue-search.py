#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from collections import Counter
from pathlib import Path
import csv, sys, argparse
sys.set_int_max_str_digits(2_000_000)
OUT=Path('/mnt/data/r6')
ETA=Fraction(1299,500)
ORDER_CLASSES={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}

def vp(n,p):
 c=0;n=abs(n)
 while n and n%p==0:c+=1;n//=p
 return c

def unit10(n): return gcd(abs(n),10)==1

def ceil_div(a,b): return -((-a)//b)

def solve_signed_linear(a,b,m,M):
 if M<1:return ()
 d=gcd(a,m)
 if b%d:return ()
 aa,bb,mm=a//d,b//d,m//d
 r=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
 first=r+ceil_div(-M-r,mm)*mm
 if first==0:first=mm
 return range(first,M+1,mm)

def tail_CB(q):
 c=q**3+10*q*q+12*q+8
 return q*c,(q+2)*(q*q-4*q-4),c

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
 return dict(G=G,q=q,u=u,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2,hlin=hlin,mlin=mlin,rlin=rlin)

def linear_gate(row,k):
 G,u,A=row['G'],row['u'],row['A']; K=10**k
 for z in ('a3','Z','X','D2','hlin','mlin','rlin'):
  if not(row[z]>0 and unit10(row[z])):return False
 if not(G//10<=row['a3']<G):return False
 if not row['X']*K < ETA*u*G*G:return False
 if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False
 return True

def Ftilde(row):return row['A']*row['X']**2+row['Z']*row['D2']

def crt2(a,m,b,n):
 return (a+m*(((b-a)*pow(m,-1,n))%n))%(m*n)

def r6_data(row,k,ell):
 G=row['G'];K=10**k;L=10**ell; M=L//8; A=row['A'];u=row['u'];D2=row['D2']; MB=A*M
 f=Ftilde(row)
 if f%(2*K):return None
 Omega=f//(2*K)
 mu,rho=divmod(u*D2,MB)
 if not 0<rho<MB:return None
 rA=(-row['Z']*pow(K,-1,A))%A
 if gcd(u*D2,M)!=1:return None
 x10=(Omega*pow((u*D2)%M,-1,M))%M
 sA=(mu-rA)%A;sM=(mu-x10)%M;sstar=crt2(sA,A,sM,M)
 Bd=Fraction(292*L*L*u*u,A*G**3)
 return dict(Mdec=M,Mbig=MB,Omega=Omega,mu=mu,varrho=rho,rA=rA,x10=x10,sA=sA,sM=sM,sstar=sstar,B=Bd)

def scan_tail(q,delta,gmax=1200):
 mod,rr=ORDER_CLASSES[q]; b=vp(q+4,5); C,B,c=tail_CB(q); Mq=q*(q+4); r=max(-delta,0); ddel=2*5**b*10**r
 if delta>0:
  mmax=(30*5**b*q**4-1)//10**delta;tmax=3*q+7
 elif delta==0:
  mmax=30*5**b*q**4-1;tmax=9*q-1
 else:
  mmax=30*5**b*q**4*10**(2*r)-1;tmax=9*q*10**r-1
 rows=[];st=Counter()
 for g in range(max(6,1-delta),gmax+1):
  if g%mod!=rr:continue
  k=g+delta;ell=g-delta
  if k<1 or ell<6:continue
  if delta<0 and k<=b:continue
  G=10**g
  if G%ddel:continue
  u=(G+1)//q;A=2*u+1;D=G//ddel;CM=C*Mq; aa=2*D; coeff=C*A-2*B
  for tt in range(1,tmax+1):
   for al in solve_signed_linear(aa,(coeff*tt)%CM,CM,mmax):
    st['tail_integral']+=1; num=B*tt+al*D
    if num%C:continue
    N=num//C; row=reconstruct(G,q,N,tt)
    if row is None:continue
    st['reconstructed']+=1
    if not linear_gate(row,k):continue
    st['linear_legal']+=1
    if Ftilde(row)%(2*10**k):continue
    st['dcdc']+=1; rows.append((g,k,ell,al,row))
 return st,rows

def high_P_fraction(G,q,H,alpha,t,d0):
 c=q**3+10*q*q+12*q+8
 num=-H*(-4*G*G*alpha*q-16*G*G*alpha+2*G*alpha*q*q+8*G*alpha*q-8*G*alpha-8*G*d0*q**4*t-56*G*d0*q**3*t-48*G*d0*q*q*t+96*G*d0*q*t+64*G*d0*t-alpha*q**3-6*alpha*q*q+4*d0*q**5*t+24*d0*q**4*t-32*d0*q**3*t-160*d0*q*q*t-64*d0*q*t)
 den=2*d0*q*q*(q+4)*c
 return Fraction(num,den)

def high_rem_fraction(G,q,H,alpha,t,d0):
 c=q**3+10*q*q+12*q+8
 num=H*(-G*alpha*q**3-8*G*alpha*q*q-12*G*alpha*q-8*G*alpha+4*G*d0*q**5*t+32*G*d0*q**4*t+8*G*d0*q**3*t-176*G*d0*q*q*t-160*G*d0*q*t-64*G*d0*t-16*d0*q**3*t-64*d0*q*q*t)
 den=2*G*d0*q*(q+4)*(2*G+q+2)*c
 return Fraction(num,den)

def high_eps_target(q,H,alpha,t,d0):
 c=q**3+10*q*q+12*q+8
 num=(-2*H*H*alpha*q**4-12*H*H*alpha*q**3+8*H*H*d0*q**6*t+48*H*H*d0*q**5*t-64*H*H*d0*q**4*t-320*H*H*d0*q**3*t-128*H*H*d0*q*q*t-alpha*q**3-10*alpha*q*q-12*alpha*q-8*alpha-3*d0*q**6*t-36*d0*q**5*t-156*d0*q**4*t-352*d0*q**3*t-240*d0*q*q*t+64*d0*q*t+64*d0*t)
 den=4*H*d0*q**3*(q+4)*c
 return Fraction(num,den)

def critical_q11_rows():
 q=11;H=10;delta=1;alpha=152510;t=31;d0=10;C,B,c=tail_CB(q)
 target=high_eps_target(q,H,alpha,t,d0); DQ=2*d0*q*q*(q+4)*c
 gs=[471,13077,50895,63501,101319,126531]
 out=[]
 for g in gs:
  G=10**g; num=B*t+alpha*(G//d0); assert num%C==0; N=num//C
  row=reconstruct(G,q,N,t);assert row and linear_gate(row,g+1)
  d=r6_data(row,g+1,g-1); assert d
  P=high_P_fraction(G,q,H,alpha,t,d0); rem=high_rem_fraction(G,q,H,alpha,t,d0)
  assert Fraction(row['u']*row['D2'],d['Mbig'])==P+rem
  eps=Fraction(d['mu'],1)-P
  first='HIGH_DECIMAL_ZERO_DEFECT_FAIL' if d['sM']!=0 else ('HIGH_A_ZERO_DEFECT_FAIL' if d['sA']!=0 else 'DUAL_ZERO_DEFECT')
  secondary='PRIMITIVE_GCD_FAIL' if gcd(row['Z'],row['u'])!=1 else ''
  out.append((g,row,d,P,rem,eps,target,first,secondary))
 return DQ,target,out

def critical_period_audit():
 # Exact period for the q=11 critical fibre: order modulo C*33 = 12606.
 q=11;alpha=152510;t=31;d0=10;C,B,c=tail_CB(q);Mq=q*(q+4);period=12606
 valid=[]
 G=10
 for g in range(1,period+1):
  if (G+1)%q==0:
   num=B*t+alpha*(G//d0)
   if num%C==0:
    N=num//C
    row=reconstruct(G,q,N,t)
    if row is not None: valid.append(g)
  G*=10
 assert valid==[471],valid[:10]
 return period,valid

FIELDS=['kind','g','k','ell','delta','q','u','A','alpha','t','N','mu','varrho','B_num','B_den','sA','sM','sstar','x','Theta','DeltaLin','p','z','mu_mod_p','H_degree','H_value','first_failure','secondary_failure','rA','x10','floor_eps_num','floor_eps_den','eps_target_num','eps_target_den']

def write_tsv(critical, historical_rows):
 path=OUT/'J2-55-R6-survivors.tsv'
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader()
  for g,row,d,P,rem,eps,target,first,secondary in critical:
   n=(g-1)//2; z=(n-235)//11 # nstar representative from g=471
   rec={k:'' for k in FIELDS}; rec.update(kind='HIGH_Q11_CRITICAL',g=g,k=g+1,ell=g-1,delta=1,q=11,u=row['u'],A=row['A'],alpha=152510,t=31,N=row['N'],mu=d['mu'],varrho=d['varrho'],B_num=d['B'].numerator,B_den=d['B'].denominator,sA=d['sA'],sM=d['sM'],sstar=0,x=d['mu'],p=11,z=z,mu_mod_p=d['mu']%11,H_degree='FINITE_STATE/REGRESSION_LINEAR',first_failure=first,secondary_failure=secondary,rA=d['rA'],x10=d['x10'],floor_eps_num=eps.numerator,floor_eps_den=eps.denominator,eps_target_num=target.numerator,eps_target_den=target.denominator)
   w.writerow(rec)
  for kind,g,k,ell,alpha,row,d in historical_rows:
   rec={k0:'' for k0 in FIELDS};rec.update(kind=kind,g=g,k=k,ell=ell,delta=k-g,q=row['q'],u=row['u'],A=row['A'],alpha=alpha,t=row['t'],N=row['N'],mu=d['mu'],varrho=d['varrho'],B_num=d['B'].numerator,B_den=d['B'].denominator,sA=d['sA'],sM=d['sM'],sstar=d['sstar'],rA=d['rA'],x10=d['x10'])
   if gcd(row['Z'],row['u'])!=1:rec['first_failure']='PRIMITIVE_GCD_FAIL'
   else:rec['first_failure']='SINGLE_MODULUS_DEFECT_BOUND_FAIL' if (Fraction(d['sA'],1)>=d['B'] and Fraction(d['sM'],1)>=d['B']) else 'SMALL_DEFECT'
   w.writerow(rec)
 return path

def main(full=False):
 DQ,target,critical=critical_q11_rows(); period,valid=critical_period_audit()
 # exact carry-small threshold by direct test; g=10 works and remainder decreases thereafter because numerator is affine and denominator quadratic-positive.
 threshold=None
 for g in range(1,30):
  if abs(high_rem_fraction(10**g,11,10,152510,31,10)) < Fraction(1,DQ):threshold=g;break
 assert threshold==10
 hist=[]; summary={}
 if full:
  for delta,label,gmax in [(0,'BOUNDARY',1200),(-1,'REVERSE_R1',12)]:
   for q in (7,11,17,19):
    st,rows=scan_tail(q,delta,gmax);summary[(label,q)]=dict(st)
    for g,k,ell,al,row in rows:
     d=r6_data(row,k,ell);assert d
     hist.append((label,g,k,ell,al,row,d))
  bc=[r for r in hist if r[0]=='BOUNDARY'];rv=[r for r in hist if r[0]=='REVERSE_R1']
  assert len(bc)==79 and len(rv)==50,(len(bc),len(rv))
  bp=[r for r in bc if gcd(r[5]['Z'],r[5]['u'])==1];rp=[r for r in rv if gcd(r[5]['Z'],r[5]['u'])==1]
  assert len(bp)==75 and all(Fraction(r[6]['sA'],1)>=r[6]['B'] and Fraction(r[6]['sM'],1)>=r[6]['B'] for r in bp)
  assert len(rp)==44 and all(Fraction(r[6]['sA'],1)>=r[6]['B'] and Fraction(r[6]['sM'],1)>=r[6]['B'] for r in rp)
 path=write_tsv(critical,hist)
 print('R6_DEFECT_SEARCH=PASS')
 print('CRITICAL_PERIOD=',period,'VALID_CLASSES=',valid)
 print('CRITICAL_CARRY_THRESHOLD_G=',threshold)
 print('CRITICAL_EPS_TARGET=',target)
 print('CRITICAL_EPS_TARGET_IN_STABLE_INTERVAL=',-1<=target<=0)
 for g,row,d,P,rem,eps,target,first,secondary in critical:
  print('CRIT',g,'mu_mod_11',d['mu']%11,'sA_nonzero',d['sA']!=0,'sM_nonzero',d['sM']!=0,'eps_in_stable',-1<=eps<=0,'first',first,'secondary',secondary)
 if full:
  print('BOUNDARY_DCDC=79 PRIMITIVE_PASS=75 BOTH_SINGLE_MOD_DEAD=75')
  print('REVERSE_R1_DCDC=50 PRIMITIVE_PASS=44 BOTH_SINGLE_MOD_DEAD=44')
 print('SURVIVOR_FILE=',path)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--historical-full',action='store_true');args=ap.parse_args();main(args.historical_full)
