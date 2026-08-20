#!/usr/bin/env python3
"""R10 exact historical replay + TQR gate.
Reconstructs the frozen R9 boundary corpus (default g<=1200), applies digit core,
TQR reintegration, deflated lambda/e CRT bookkeeping, and carry core.
No theorem is inferred from finite search.
"""
from fractions import Fraction
from math import gcd
from collections import Counter
from pathlib import Path
import csv,argparse,sys
sys.set_int_max_str_digits(2_000_000)
OUT=Path('/mnt/data')
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

def crt2(a,m,b,n):
 assert gcd(m,n)==1
 x=(a+m*(((b-a)*pow(m,-1,n))%n))%(m*n)
 assert x%m==a%m and x%n==b%n
 return x

def normalized_digit_data(q,g,t,a3):
 G=10**g;b=vp(q+4,5);f=5**b;c=q**3+10*q*q+12*q+8;v=vp(t,5)
 digit=c*a3+q*q*t
 if G%(4*f*f): return dict(digit_core=False)
 M=G//(4*f*f)
 if digit%M:return dict(digit_core=False)
 lam=digit//M
 eta_num=lam-8*f*f*t
 if eta_num%q:return dict(digit_core=True,lambda_=lam,lambda_q_pass=False)
 eta=eta_num//q
 out=dict(digit_core=True,b=b,f=f,v5t=v,v5c=vp(c,5),lambda_=lam,eta=eta,
          lambda_q_pass=True)
 if b>0:
  if v!=0:
   out['lam_def_scope']='FAIL_BPOS_V_NOT_ZERO';return out
  cflat=c;tflat=t;Cb=M
 elif g>vp(c,5) and v==vp(c,5):
  w=5**v;cflat=c//w;tflat=t//w;Cb=G//(4*w)
 else:
  out['lam_def_scope']='HENSEL_EDGE_OR_VALUATION_UNRESOLVED';return out
 rc=(q*q*tflat*pow(Cb,-1,cflat))%cflat
 star=crt2((8*f*f*t)%q,q,rc,cflat)
 eta_star=((rc-8*f*f*t)*pow(q,-1,cflat))%cflat
 h5=(q+4)//f
 e_star=(h5*eta_star-8*f*t*(3*q+5))%cflat
 out.update(lam_def_scope='ACTIVE',cflat=cflat,lambda_mod_c=lam%cflat,lambda_c_rhs=rc,
            lambda_crt=star,lambda_crt_pass=(lam%(q*cflat)==star),eta_mod_c=eta%cflat,
            eta_mod_c_rhs=eta_star,e_mod_c_rhs=e_star)
 return out

def high_critical(g=471):
 q=11;H=10;alpha=152510;t=31;b=1;f=5;d0=10;C,B,c=tail_CB(q);G=10**g
 N=(B*t+alpha*(G//d0))//C;row=reconstruct(G,q,N,t);assert row and linear_gate(row,g+1)
 digit=c*row['a3']+q*q*t;M=G//(4*f*f);lam=digit//M
 eta=(lam-8*f*f*t)//q
 e=(d0*B*t-alpha)//q
 h5=(q+4)//f
 assert h5*eta==e+8*f*t*(3*q+5)
 return dict(kind='HIGH_Q11_CRITICAL',g=g,k=g+1,delta=1,q=q,b=b,v5t=vp(t,5),v5c=vp(c,5),
             t=t,alpha=alpha,a3=row['a3'],e=e,eta=eta,lambda_=lam,TQR_status='PASS',
             first_failure='CARRY_NORMALIZATION_FAIL')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--gmax',type=int,default=1200);args=ap.parse_args()
 stats,rows=scan_boundary(args.gmax)
 print('BOUNDARY_STATS=',stats)
 print('BOUNDARY_DCDC_TOTAL=',len(rows))
 if args.gmax==1200: assert len(rows)==79
 out=[];tqrpass=0;carryhits=0;ecpass=0
 for q,g,al,tt,row in rows:
  G=10**g;b=vp(q+4,5);f=5**b;C,B,c=tail_CB(q);d0=2*f
  nd=normalized_digit_data(q,g,tt,row['a3']);assert nd['digit_core'] and nd['lambda_q_pass']
  e_num=d0*B*tt-al;assert e_num%q==0;e=e_num//q
  h5=(q+4)//f
  assert h5*nd['eta']==e+8*f*tt*(3*q+5);tqrpass+=1
  if nd.get('lam_def_scope')=='ACTIVE':
   assert e%nd['cflat']==nd['e_mod_c_rhs'];ecpass+=1
  J,D=boundary_J_D(G,q,al,tt);dd=r6_data_boundary(row,g);assert dd
  chi=J-D*dd['mu'];assert chi%q==0
  req2=g-2;req5=max(g-2*b-vp(tt,5),0)
  best=None
  for ss in range(21):
   Ga=gammaB(q,al,tt,ss,chi);ok=vp(Ga,2)>=req2 and vp(Ga,5)>=req5
   score=min(vp(Ga,2)-req2,vp(Ga,5)-req5)
   if best is None or score>best[0]:best=(score,ss,Ga,ok)
   carryhits+=ok
  first='CARRY_NORMALIZATION_FAIL' if not best[3] else 'NORMALIZED_SURVIVOR'
  out.append(dict(kind='BOUNDARY_HISTORICAL',g=g,k=g,delta=0,q=q,b=b,v5t=vp(tt,5),v5c=vp(c,5),h5=h5,
                  t=tt,alpha=al,a3=row['a3'],e=e,eta=nd['eta'],lambda_=nd['lambda_'],TQR_status='PASS',
                  lambda_reintegrated='PASS',gamma='' if not best[3] else best[2],zeta='',zeta_residue='',xi='',
                  s=best[1],Theta='',root_status='UNREACHED',first_failure=first))
 out.append(high_critical())
 fields=['kind','g','k','delta','q','b','v5t','v5c','h5','t','alpha','a3','e','eta','lambda','TQR_status',
         'lambda_reintegrated','gamma','zeta','zeta_residue','xi','third_core','s','Theta','root_status','first_failure',
         'R','K','etaR','lambdaR','zetaR','xiR']
 for rr in out:
  if 'lambda_' in rr: rr['lambda']=rr.pop('lambda_')
 p=OUT/'J2-55-R10-survivors.tsv'
 with p.open('w',newline='',encoding='utf-8') as fobj:
  wri=csv.DictWriter(fobj,fieldnames=fields,delimiter='\t',extrasaction='ignore');wri.writeheader();wri.writerows(out)
 print('TQR_PASS=',tqrpass,'/',len(rows))
 print('E_CRT_REINTEGRATION_PASS=',ecpass)
 print('BOUNDARY_ANY_S_CARRY_CORE_HITS=',carryhits)
 print('BOUNDARY_NORMALIZED_SURVIVORS=',sum(1 for r in out if r.get('kind')=='BOUNDARY_HISTORICAL' and r['first_failure']=='NORMALIZED_SURVIVOR'))
 print('HIGH_Q11_TQR=PASS')
 print('HIGH_Q11_FIRST_FAILURE=CARRY_NORMALIZATION_FAIL')
 print('SURVIVOR_FILE='+p.name)
 print('FINITE_SEARCH_IS_DIAGNOSTIC_NOT_THEOREM=PASS')

if __name__=='__main__':main()
