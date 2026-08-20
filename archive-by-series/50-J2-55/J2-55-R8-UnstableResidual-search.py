#!/usr/bin/env python3
"""R8 exact unstable-residual diagnostic.

Replays the frozen R7 boundary generator (g<=1200) and the critical q=11 high fibre.
No finite census is promoted to a global theorem.
"""
from fractions import Fraction
from math import gcd
from collections import Counter
from pathlib import Path
import csv,sys
sys.set_int_max_str_digits(2_000_000)
OUT=Path(__file__).resolve().parent
ETA=Fraction(1299,500)
ORDER_CLASSES={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}

def vp(n,p):
 c=0;n=abs(n)
 if n==0:return 10**9
 while n%p==0:c+=1;n//=p
 return c

def unit10(n):return gcd(abs(n),10)==1
def ceil_div(a,b):return -((-a)//b)
def solve_signed_linear(a,b,m,M):
 if M<1:return ()
 d=gcd(a,m)
 if b%d:return ()
 aa,bb,mm=a//d,b//d,m//d
 rr=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
 first=rr+ceil_div(-M-rr,mm)*mm
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
  b=vp(q+4,5);d0=2*5**b;C,B,c=tail_CB(q)
  mmax=30*5**b*q**4-1;st=Counter()
  for g in range(6,gmax+1):
   if g%mod!=rr:continue
   G=10**g;D=G//d0;Mq=q*(q+4);CM=C*Mq;Dmod=D%CM;Amod=(2*((G+1)//q)+1)%Mq
   for tt in range(1,9*q):
    for al in solve_signed_linear(D,(-B*tt)%C,C,mmax):
     st['tail_integral']+=1
     nmod_num=(B*tt+al*Dmod)%CM
     assert nmod_num%C==0
     Nmod=nmod_num//C
     if (Amod*tt-2*Nmod)%Mq:continue
     num=B*tt+al*D
     assert num%C==0
     N=num//C;row=reconstruct(G,q,N,tt)
     if row is None:continue
     st['reconstructed']+=1
     if not linear_gate(row,g):continue
     st['linear_legal']+=1
     if Ftilde(row)%(2*G):continue
     st['dcdc']+=1;rows.append((q,g,al,tt,row))
  stats[q]=dict(st)
 return stats,rows

def high_critical(g):
 q=11;H=10;alpha=152510;t=31;b=1;d0=10;C,B,c=tail_CB(q);G=10**g
 N=(B*t+alpha*(G//d0))//C;row=reconstruct(G,q,N,t);assert row and linear_gate(row,g+1)
 M=(10**(g-1))//8;MB=row['A']*M;mu,rho=divmod(row['u']*row['D2'],MB)
 J0,D=boundary_J_D(G,q,alpha,t);J=H*J0;chi=J-D*mu
 NH=(-2*H**2*alpha*q**4-12*H**2*alpha*q**3+8*H**2*d0*q**6*t+48*H**2*d0*q**5*t
     -64*H**2*d0*q**4*t-320*H**2*d0*q**3*t-128*H**2*d0*q**2*t-alpha*q**3-10*alpha*q**2
     -12*alpha*q-8*alpha-3*d0*q**6*t-36*d0*q**5*t-156*d0*q**4*t-352*d0*q**3*t
     -240*d0*q**2*t+64*d0*q*t+64*d0*t)
 Gamma=NH+2*H*q*chi # high s=0
 digit=c*row['a3']+q*q*t
 omega=d0*c*t-alpha
 lam=digit//(G//(4*5**(2*b)))
 assert digit%(G//(4*5**(2*b)))==0
 assert omega==((q+4)//(5**b))*lam
 return dict(kind='HIGH_Q11_CRITICAL',q=q,g=g,alpha=alpha,t=t,a3=row['a3'],omega=omega,lambda_tail=lam,
             Gamma=Gamma,v2_Gamma=vp(Gamma,2),v5_Gamma=vp(Gamma,5),required_v2=g-2,required_v5=g-2*b,
             v2_digit=vp(digit,2),v5_digit=vp(digit,5),required_digit_v2=g-2,required_digit_v5=g-2*b,
             carry_core_pass=(vp(Gamma,2)>=g-2 and vp(Gamma,5)>=g-2*b),digit_core_pass=True)

def main():
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--full-boundary',action='store_true');args=ap.parse_args()
 out=[]
 if args.full_boundary:
  stats,rows=scan_boundary(1200)
  print('BOUNDARY_STATS=',stats)
  print('BOUNDARY_DCDC_TOTAL=',len(rows));assert len(rows)==79
  core_hits=0
  for q,g,al,tt,row in rows:
   G=10**g;b=vp(q+4,5);d0=2*5**b;c=q**3+10*q*q+12*q+8
   J,D=boundary_J_D(G,q,al,tt);dd=r6_data_boundary(row,g);assert dd
   chi=J-D*dd['mu']; digit=c*row['a3']+q*q*tt;omega=d0*c*tt-al
   req2=g-2;req5=max(g-2*b-vp(tt,5),0);reqdt5=max(g-2*b,0)
   best=None
   for ss in range(21):
    ga=gammaB(q,al,tt,ss,chi)
    ok=vp(ga,2)>=req2 and vp(ga,5)>=req5
    score=min(vp(ga,2)-req2,vp(ga,5)-req5)
    if best is None or score>best[0]:best=(score,ss,ga,vp(ga,2),vp(ga,5),ok)
    core_hits+=ok
   out.append(dict(kind='BOUNDARY_HISTORICAL',q=q,g=g,alpha=al,t=tt,a3=row['a3'],omega=omega,
                   Gamma=best[2],best_s=best[1],v2_Gamma=best[3],v5_Gamma=best[4],required_v2=req2,required_v5=req5,
                   v2_digit=vp(digit,2),v5_digit=vp(digit,5),required_digit_v2=g-2,required_digit_v5=reqdt5,
                   carry_core_pass=best[5],digit_core_pass=(vp(digit,2)>=g-2 and vp(digit,5)>=reqdt5)))
  print('BOUNDARY_ANY_S_CARRY_CORE_HITS=',core_hits)
 else:
  print('BOUNDARY_FULL_REPLAY=SKIPPED_BY_DEFAULT; use --full-boundary (expensive). R7 frozen corpus=79 states.')
 crit=[high_critical(471)]
 for x in crit:
  print('CRITICAL',x['g'],'omega',x['omega'],'lambda',x['lambda_tail'],'Gamma',x['Gamma'],
        'v2/v5',x['v2_Gamma'],x['v5_Gamma'],'required',x['required_v2'],x['required_v5'],'carrypass',x['carry_core_pass'])
  assert all(not x['carry_core_pass'] for x in crit)
 out.extend(crit)
 path=OUT/'J2-55-R8-UnstableResidual-diagnostics.tsv'
 fields=sorted({k for x in out for k in x})
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(out)
 print('CRITICAL_Q11_G471_CORE_KILL=YES')
 print('SURVIVOR_FILE='+path.name)

if __name__=='__main__':main()
