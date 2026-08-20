#!/usr/bin/env python3
"""Exact R7 regression/search for q-content descent gates.

This replays the frozen g<=1200 boundary corpus and the critical high q=11 fibre.
It does NOT treat the stabilized constant-term carry equality as an all-exponent theorem.
"""
from fractions import Fraction
from math import gcd
from collections import Counter
from pathlib import Path
import csv,sys
sys.set_int_max_str_digits(2_000_000)
ETA=Fraction(1299,500)
ORDER_CLASSES={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}
OUT=Path(__file__).resolve().parent

def vp(n,p):
 c=0;n=abs(n)
 while n and n%p==0:c+=1;n//=p
 return c

def unit10(n):return gcd(abs(n),10)==1
def ceil_div(a,b):return -((-a)//b)
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
 u=(G+1)//q;A=2*u+1;Mq=q*(q+4)
 rr=A*t-2*N
 if rr%Mq:return None
 Z=rr//Mq
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
  if not(row[z]>0 and unit10(row[z])):return False
 if not(G//10<=row['a3']<G):return False
 if not row['X']*K<ETA*u*G*G:return False
 if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False
 return True

def Ftilde(row):return row['A']*row['X']**2+row['Z']*row['D2']

def r6_data_boundary(row,g):
 G=10**g;M=G//8;MB=row['A']*M
 f=Ftilde(row)
 if f%(2*G):return None
 Omega=f//(2*G)
 mu,rho=divmod(row['u']*row['D2'],MB)
 if not 0<rho<MB:return None
 if gcd(row['u']*row['D2'],M)!=1:return None
 x10=(Omega*pow((row['u']*row['D2'])%M,-1,M))%M
 sM=(mu-x10)%M
 Bdef=Fraction(292*G*G*row['u']*row['u'],row['A']*G**3)
 return dict(mu=mu,rho=rho,sM=sM,B=Bdef)

def boundary_J_D(G,q,alpha,t):
 b=vp(q+4,5);d0=2*5**b;c=q**3+10*q*q+12*q+8
 br=(-4*G*G*alpha*q-16*G*G*alpha+2*G*alpha*q*q+8*G*alpha*q-8*G*alpha
     -8*G*d0*q**4*t-56*G*d0*q**3*t-48*G*d0*q*q*t+96*G*d0*q*t+64*G*d0*t
     -alpha*q**3-6*alpha*q*q+4*d0*q**5*t+24*d0*q**4*t-32*d0*q**3*t-160*d0*q*q*t-64*d0*q*t)
 return -br,2*d0*q*q*(q+4)*c

def gammaB(q,alpha,t,s,chi):
 b=vp(q+4,5);d0=2*5**b;c=q**3+10*q*q+12*q+8;D=2*d0*q*q*(q+4)*c
 Pa=2*q**4+13*q**3+10*q**2+12*q+8
 Pt=5*q**6+12*q**5-220*q**4-672*q**3-368*q**2+64*q+64
 return alpha*Pa-d0*t*Pt-2*q*(D*s+chi)

def scan_boundary(gmax=1200):
 rows=[];stats={}
 for q,(mod,rr) in ORDER_CLASSES.items():
  b=vp(q+4,5);d0=2*5**b;C,B,c=tail_CB(q);Mq=q*(q+4);CM=C*Mq
  mmax=30*5**b*q**4-1;st=Counter()
  for g in range(6,gmax+1):
   if g%mod!=rr:continue
   G=10**g;D=G//d0;A=2*((G+1)//q)+1
   aa=2*D;coeff=C*A-2*B
   for tt in range(1,9*q):
    for al in solve_signed_linear(aa,(coeff*tt)%CM,CM,mmax):
     st['tail_integral']+=1
     num=B*tt+al*D
     if num%C:continue
     N=num//C;row=reconstruct(G,q,N,tt)
     if row is None:continue
     st['reconstructed']+=1
     if not linear_gate(row,g):continue
     st['linear_legal']+=1
     if Ftilde(row)%(2*G):continue
     st['dcdc']+=1;rows.append((q,g,al,tt,row))
  stats[q]=dict(st)
 return stats,rows

def high_critical_rows():
 q=11;H=10;alpha=152510;t=31;d0=10;C,B,c=tail_CB(q)
 out=[]
 for g in [471,13077,50895,63501,101319,126531]:
  G=10**g;N=(B*t+alpha*(G//d0))//C;row=reconstruct(G,q,N,t)
  assert row and linear_gate(row,g+1)
  M=(10**(g-1))//8;MB=row['A']*M;mu,rho=divmod(row['u']*row['D2'],MB)
  # H-high J has an extra H factor.
  J0,D=boundary_J_D(G,q,alpha,t);J=H*J0
  chi=J-D*mu
  out.append((q,g,g+1,g-1,alpha,t,row,mu,rho,J,D,chi))
 return out

FIELDS=['kind','g','k','ell','delta','q','b','d_delta','alpha','t','N','a3','Jcarry','Dcarry','chi','carry_target','root_plus_opening','tail_minus_opening','q_div_t','beta','tau','e','e1','q_div_chi','q_div_tau','beta2','tau2','a2','n','Z','first_failure']

def main():
 stats,rows=scan_boundary(1200)
 print('BOUNDARY_STATS=',stats)
 print('BOUNDARY_DCDC_TOTAL=',len(rows))
 primitive=[r for r in rows if gcd(r[4]['Z'],r[4]['u'])==1]
 print('BOUNDARY_PRIMITIVE_PASS=',len(primitive))
 print('BOUNDARY_Q_DIV_T=',sum(1 for q,g,a,t,row in rows if t%q==0))
 print('BOUNDARY_PRIMITIVE_Q_DIV_T=',sum(1 for q,g,a,t,row in primitive if t%q==0))
 resonance=0;chiq=0
 ledger=[]
 for q,g,al,tt,row in rows:
  G=10**g;J,D=boundary_J_D(G,q,al,tt);d=r6_data_boundary(row,g);assert d
  chi=J-D*d['mu'];chiq+=(chi%q==0)
  ss=[s for s in range(21) if gammaB(q,al,tt,s,chi)==0]
  resonance+=bool(ss)
  first='PRIMITIVE_GCD_FAIL' if gcd(row['Z'],row['u'])!=1 else ('SINGLE_MODULUS_DEFECT_BOUND_FAIL' if Fraction(d['sM'],1)>=d['B'] else 'SMALL_DEFECT')
  b=vp(q+4,5);d0=2*5**b
  ledger.append(dict(kind='BOUNDARY_HISTORICAL',g=g,k=g,ell=g,delta=0,q=q,b=b,d_delta=d0,alpha=al,t=tt,N=row['N'],a3=row['a3'],Jcarry=J,Dcarry=D,chi=chi,carry_target=('GAMMA_B_ZERO_s='+','.join(map(str,ss)) if ss else 'STABILIZED_TARGET_FAIL'),root_plus_opening='NOT_ACTIVATED',tail_minus_opening='PASS',q_div_t=str(tt%q==0),beta='',tau='',e=(d0*((q+2)*(q*q-4*q-4))*tt-al)//q,e1='',q_div_chi=str(chi%q==0),q_div_tau='',beta2='',tau2='',a2='',n='',Z=row['Z'],first_failure=first))
 print('BOUNDARY_STABILIZED_CARRY_TARGET_HITS=',resonance)
 print('BOUNDARY_CHI_DIV_Q=',chiq,'/',len(rows))
 # Critical high q11 sanity: q∤t but q|chi; not a counterexample because carry equality does not hold globally.
 for q,g,k,ell,al,tt,row,mu,rho,J,D,chi in high_critical_rows():
  ledger.append(dict(kind='HIGH_Q11_CRITICAL',g=g,k=k,ell=ell,delta=1,q=q,b=1,d_delta=10,alpha=al,t=tt,N=row['N'],a3=row['a3'],Jcarry=J,Dcarry=D,chi=chi,carry_target='R6_HIGH_TARGET_FAIL',root_plus_opening='NOT_ACTIVATED',tail_minus_opening='PASS',q_div_t=str(tt%q==0),beta='',tau='',e=(10*((q+2)*(q*q-4*q-4))*tt-al)//q,e1='',q_div_chi=str(chi%q==0),q_div_tau='',beta2='',tau2='',a2='',n='',Z=row['Z'],first_failure='HIGH_DECIMAL_ZERO_DEFECT_FAIL'))
 print('CRITICAL_Q11_Q_DIV_T=',31%11==0)
 print('CRITICAL_Q11_CHI_DIV_Q=',all(r[-1]%11==0 for r in high_critical_rows()))
 path=OUT/'J2-55-R7-CarryIndex-survivors.tsv'
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader();w.writerows(ledger)
 print('LEDGER_ROWS=',len(ledger))
 print('LEDGER_FILE=',path.name)
 print('GLOBAL_Q_DESCENT_STATUS=NOT_PROVED; stabilized-target implication only')

if __name__=='__main__':main()
