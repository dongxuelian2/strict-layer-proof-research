#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from collections import Counter
import sys
sys.set_int_max_str_digits(1_000_000)

ETA=Fraction(1299,500)
ORDER_CLASSES={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}

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
    h=(N+q*Z)//2
    if (A*N+(q+2)*Z)%2:return None
    mu=(A*N+(q+2)*Z)//2
    r=(G//2)*h-u*a3
    D2=u*a3+G*X
    return dict(G=G,q=q,u=u,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2,h=h,mu=mu,r=r)

def linear_gate(row,k):
    G,u,A=row['G'],row['u'],row['A']; K=10**k
    for z in ('a3','Z','X','D2','h','mu','r'):
        if not(row[z]>0 and unit10(row[z])): return False
    if not(G//10<=row['a3']<G):return False
    if not row['X']*K < ETA*u*G*G:return False
    if not Fraction(row['Z'],1)<2*ETA*u/K+Fraction(2*u*A,G):return False
    return True

def F(row): return row['A']*row['X']**2+row['Z']*row['D2']

def Q_scaled_at_y(row,k,y):
    # (GK)^2 Q(y/(GK)), exact integer when y is integral.
    G=row['G'];K=10**k;H=G//2;A=row['A'];u=row['u'];D2=row['D2']
    GK=G*K
    return A*H*H*y*y-2*u*K*D2*y*GK+F(row)*GK*GK

def classify(row,k):
    G=row['G'];K=10**k;A=row['A'];u=row['u'];H=G//2;D2=row['D2'];mu=row['mu']
    # y=GK*x; exact affine digit endpoints.
    yL=A*G*G*K//10+mu
    yU=A*G*G*K+mu
    eL=Q_scaled_at_y(row,k,yL); eU=Q_scaled_at_y(row,k,yU)
    a=A*H*H; b=u*K*D2
    disc=b*b-a*F(row)
    if disc<0:return 'NO_REAL_ROOT', eL, eU, disc
    if eL==0 or eU==0:return 'BOUNDARY_TOUCH',eL,eU,disc
    if eL*eU<0:return 'ONE_ROOT_INSIDE',eL,eU,disc
    if eL<0 and eU<0:return 'WINDOW_BETWEEN_ROOTS',eL,eU,disc
    # both positive: decide side by derivative at endpoints
    # sign Q'(x) equals sign(a*y-b*GK)
    GK=G*K
    dL=a*yL-b*GK; dU=a*yU-b*GK
    if dL>0:return 'WINDOW_RIGHT_BOTH_ROOTS',eL,eU,disc
    if dU<0:return 'WINDOW_LEFT_BOTH_ROOTS',eL,eU,disc
    return 'WINDOW_CONTAINS_BOTH_ROOTS',eL,eU,disc

def tail_rows(q,delta,gmax,require_dcdc=False):
    mod,rr=ORDER_CLASSES[q]; b=vp(q+4,5); C,B=tail_CB(q); Mq=q*(q+4)
    r=max(-delta,0); ddel=2*5**b*10**r
    if delta>0:
        mmax=(30*5**b*q**4-1)//(10**delta); tmax=3*q+7
    elif delta==0:
        mmax=30*5**b*q**4-1; tmax=9*q-1
    else:
        mmax=30*5**b*q**4*10**(2*r)-1; tmax=9*q*10**r-1
    out=[]
    for g in range(max(6,1-delta),gmax+1):
        if g%mod!=rr:continue
        k=g+delta; ell=g-delta
        if k<1 or ell<6 or (delta<0 and k<=b):continue
        G=10**g
        if G%ddel:continue
        u=(G+1)//q; A=2*u+1; D=G//ddel; CM=C*Mq
        aa=2*D; coeff=C*A-2*B
        for t in range(1,tmax+1):
            for alpha in solve_signed_linear(aa,(coeff*t)%CM,CM,mmax):
                num=B*t+alpha*D
                if num%C:continue
                N=num//C
                row=reconstruct(G,q,N,t)
                if not row or not linear_gate(row,k):continue
                if require_dcdc and F(row)%(2*10**k):continue
                out.append((g,k,ell,alpha,t,row))
    return out

def census(delta,gmax,require_dcdc=False):
    C=Counter()
    for q in ORDER_CLASSES:
        for g,k,ell,alpha,t,row in tail_rows(q,delta,gmax,require_dcdc):
            if gcd(row['A'],row['D2'])!=1:continue
            if gcd(row['Z'],row['u'])!=1:continue
            cls,_,_,_=classify(row,k)
            C[cls]+=1
    return C

def make_example(q,g,delta,alpha,t):
    b=vp(q+4,5); C,B=tail_CB(q); r=max(-delta,0); ddel=2*5**b*10**r
    G=10**g; D=G//ddel
    num=B*t+alpha*D
    assert num%C==0
    N=num//C
    row=reconstruct(G,q,N,t); assert row and linear_gate(row,g+delta)
    k=g+delta;ell=g-delta
    cls,eL,eU,disc=classify(row,k)
    assert gcd(row['A'],row['D2'])==1 and gcd(row['Z'],row['u'])==1
    return dict(q=q,g=g,k=k,ell=ell,alpha=alpha,t=t,N=N,
                u=row['u'],A=row['A'],mu=row['mu'],Z=row['Z'],a3=row['a3'],
                D2=row['D2'],DCDC=(F(row)%(2*10**k)==0),
                class_=cls,Q_L_sign=(eL>0)-(eL<0),Q_U_sign=(eU>0)-(eU<0),
                disc_square=(disc>=0 and isqrt(disc)**2==disc))

def main():
    results={}
    results['high_pre_g100']=dict(census(1,100,False))
    results['boundary_pre_g100']=dict(census(0,100,False))
    results['reverse_pre_g20']=dict(census(-1,20,False))
    results['boundary_postDCDC_g1200']=dict(census(0,1200,True))
    results['reverse_postDCDC_g12']=dict(census(-1,12,True))
    examples={
      'high_pre':make_example(11,9,1,17260,29),
      'boundary_pre':make_example(7,9,0,5781,25),
      'reverse_pre':make_example(7,9,-1,137582,25),
      'reverse_postDCDC':make_example(7,9,-1,337012,25),
      'boundary_postDCDC':make_example(11,359,0,228530,13),
    }
    assert examples['high_pre']['class_']=='ONE_ROOT_INSIDE'
    assert examples['boundary_pre']['class_']=='ONE_ROOT_INSIDE'
    assert examples['reverse_pre']['class_']=='ONE_ROOT_INSIDE'
    assert examples['reverse_postDCDC']['DCDC'] and examples['reverse_postDCDC']['class_']=='ONE_ROOT_INSIDE'
    assert examples['boundary_postDCDC']['DCDC'] and examples['boundary_postDCDC']['class_']=='ONE_ROOT_INSIDE'
    print('85-R5 exact order diagnostic certificate')
    print('FLOAT_GATE_DECISIONS=0')
    for k,v in results.items(): print(k,'=',v)
    for k,v in examples.items():
        print('EXAMPLE',k,'=',v)
    print('UNIFORM_PRE_ROOT_ORDER_DISJOINTNESS=FALSE')
    print('BOUNDARY_ORDER_DISJOINTNESS_EVEN_AFTER_DCDC=FALSE')
    print('REVERSE_NONZERO_TAIL_ORDER_DISJOINTNESS_EVEN_AFTER_DCDC=FALSE')
    print('CERTIFICATE_STATUS=PASS')

if __name__=='__main__':
    main()
