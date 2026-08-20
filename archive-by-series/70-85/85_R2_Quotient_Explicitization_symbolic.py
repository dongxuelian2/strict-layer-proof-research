#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from collections import Counter, defaultdict
import csv
import sympy as sp

# 85-R2 exact symbolic quotient/carry audit.
# This script re-derives the R6 EQL-1 -> high/boundary/reverse exact division,
# then replays the frozen boundary historical corpus through g<=1200.

G,q,alpha,t,d0,H,R = sp.symbols('G q alpha t d0 H R', nonzero=True)
c = q**3 + 10*q**2 + 12*q + 8
u = (G+1)/q
A = 2*u+1

def D2_master(d):
    D3 = alpha*(q+4)
    D2 = 2*alpha + 2*d*q**4*t + 14*d*q**3*t + 12*d*q**2*t - 24*d*q*t - 16*d*t
    D1 = -alpha*q + d*q**4*t + 14*d*q**3*t + 28*d*q**2*t + 8*d*q*t
    D0 = -2*d*q**4*t - 8*d*q**3*t
    return sp.cancel((D3*G**3 + D2*G**2 + D1*G + D0)/(2*d*q**2*(q+4)*c))

def divide_exact(U):
    num, den = sp.fraction(sp.cancel(U))
    Q, Rem = sp.div(sp.Poly(num,G), sp.Poly(den,G))
    P = sp.factor(Q.as_expr())
    r = sp.factor(Rem.as_expr()/den)
    assert sp.factor(U-P-r) == 0
    return P,r

D2H = D2_master(d0)
UH = sp.cancel(8*u*D2H/(A*(G/H)))
PH,rH = divide_exact(UH)
Dfl = 2*d0*q**2*(q+4)*c
JH = sp.expand(sp.factor(Dfl*PH))

D2R = D2_master(d0*R)
UR = sp.cancel(8*u*D2R/(A*(R*G)))
PR,rR = divide_exact(UR)
DR = 2*R**2*d0*q**2*(q+4)*c
JR = sp.expand(sp.factor(DR*PR))

print('SYMBOLIC_HIGH_DIVISION=PASS')
print('SYMBOLIC_REVERSE_DIVISION=PASS')
print('D_FL=', sp.factor(Dfl))
print('D_R=', sp.factor(DR))
print('P_H=', PH)
print('r_H=', rH)
print('P_R=', PR)
print('r_R=', rR)

# ---------- historical boundary replay ----------
ETA=Fraction(1299,500)
ORDER_CLASSES={7:(6,3),11:(2,1),17:(16,8),19:(18,9)}

def vp(n,p):
    c0=0;n=abs(int(n))
    while n and n%p==0:c0+=1;n//=p
    return c0

def unit10(n): return gcd(abs(int(n)),10)==1

def ceil_div(a,b): return -((-a)//b)

def solve_signed_linear(a,b,m,M):
    if M<1:return ()
    dd=gcd(a,m)
    if b%dd:return ()
    aa,bb,mm=a//dd,b//dd,m//dd
    rr=0 if mm==1 else (bb*pow(aa,-1,mm))%mm
    first=rr+ceil_div(-M-rr,mm)*mm
    if first==0:first=mm
    return range(first,M+1,mm)

def tail_CB(qv):
    cv=qv**3+10*qv*qv+12*qv+8
    return qv*cv,(qv+2)*(qv*qv-4*qv-4),cv

def reconstruct(Gv,qv,N,tv):
    if (Gv+1)%qv:return None
    uv=(Gv+1)//qv; Av=2*uv+1; Mq=qv*(qv+4)
    rr=Av*tv-2*N
    if rr%Mq:return None
    Z=rr//Mq
    num=(Gv-1)*tv-qv*N; den=2*(qv+4)
    if num%den:return None
    a3=num//den
    if (Z+uv*N)%2:return None
    X=(Z+uv*N)//2
    if (N+qv*Z)%2:return None
    hlin=(N+qv*Z)//2
    if (Av*N+(qv+2)*Z)%2:return None
    mlin=(Av*N+(qv+2)*Z)//2
    rlin=(Gv//2)*hlin-uv*a3
    D2=uv*a3+Gv*X
    return dict(G=Gv,q=qv,u=uv,A=Av,N=N,t=tv,Z=Z,a3=a3,X=X,D2=D2,hlin=hlin,mlin=mlin,rlin=rlin)

def linear_gate(row,k):
    Gv,uv,Av=row['G'],row['u'],row['A']; Kv=10**k
    for z in ('a3','Z','X','D2','hlin','mlin','rlin'):
        if not(row[z]>0 and unit10(row[z])):return False
    if not(Gv//10<=row['a3']<Gv):return False
    if not row['X']*Kv<ETA*uv*Gv*Gv:return False
    if not Fraction(row['Z'],1)<2*ETA*uv/Kv+Fraction(2*uv*Av,Gv):return False
    return True

def Ftilde(row): return row['A']*row['X']**2+row['Z']*row['D2']

def r6_data_boundary(row,g):
    Gv=10**g; m=Gv//8; Mbig=row['A']*m
    f=Ftilde(row)
    if f%(2*Gv):return None
    Omega=f//(2*Gv)
    mu,rho=divmod(row['u']*row['D2'],Mbig)
    if not 0<rho<Mbig:return None
    if gcd(row['u']*row['D2'],m)!=1:return None
    x10=(Omega*pow((row['u']*row['D2'])%m,-1,m))%m
    return dict(mu=mu,rho=rho,x10=x10)

def boundary_J_D(Gv,qv,av,tv):
    b=vp(qv+4,5); d=2*5**b; cv=qv**3+10*qv*qv+12*qv+8
    br=(-4*Gv*Gv*av*qv-16*Gv*Gv*av+2*Gv*av*qv*qv+8*Gv*av*qv-8*Gv*av
        -8*Gv*d*qv**4*tv-56*Gv*d*qv**3*tv-48*Gv*d*qv*qv*tv+96*Gv*d*qv*tv+64*Gv*d*tv
        -av*qv**3-6*av*qv*qv+4*d*qv**5*tv+24*d*qv**4*tv-32*d*qv**3*tv-160*d*qv*qv*tv-64*d*qv*tv)
    return -br,2*d*qv*qv*(qv+4)*cv

def scan_boundary(gmax=1200):
    rows=[]; stats={}
    for qv,(mod,rr) in ORDER_CLASSES.items():
        b=vp(qv+4,5); d=2*5**b; C,B,cv=tail_CB(qv); Mq=qv*(qv+4); CM=C*Mq
        mmax=30*5**b*qv**4-1; st=Counter()
        for g in range(6,gmax+1):
            if g%mod!=rr:continue
            Gv=10**g; D=Gv//d; Av=2*((Gv+1)//qv)+1
            aa=2*D; coeff=C*Av-2*B
            for tv in range(1,9*qv):
                for av in solve_signed_linear(aa,(coeff*tv)%CM,CM,mmax):
                    st['tail_integral']+=1
                    num=B*tv+av*D
                    if num%C:continue
                    N=num//C; row=reconstruct(Gv,qv,N,tv)
                    if row is None:continue
                    st['reconstructed']+=1
                    if not linear_gate(row,g):continue
                    st['linear_legal']+=1
                    if Ftilde(row)%(2*Gv):continue
                    st['dcdc']+=1; rows.append((qv,g,av,tv,row))
        stats[qv]=dict(st)
    return stats,rows

stats, rows = scan_boundary(1200)
assert len(rows)==79
byq=defaultdict(list)
for qv,g,av,tv,row in rows:
    dd=r6_data_boundary(row,g); assert dd
    J,D=boundary_J_D(10**g,qv,av,tv)
    chi=J-D*dd['mu']
    eps=Fraction(-chi,D)
    assert chi%qv==0
    assert -1 < eps < 0
    byq[qv].append((g,av,tv,chi,D,eps))

with open('/mnt/data/85_R2_CarrySpectrum.tsv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['q','g','alpha','t','chi','D','mu_minus_P_num','mu_minus_P_den'])
    for qv in sorted(byq):
        for g,av,tv,chi,D,eps in byq[qv]:
            w.writerow([qv,g,av,tv,chi,D,eps.numerator,eps.denominator])

print('BOUNDARY_DCDC_TOTAL=',len(rows))
print('BOUNDARY_CHI_DIV_Q=79/79')
all_eps=set()
for qv in sorted(byq):
    vals={x[-1] for x in byq[qv]}; all_eps |= vals
    print('Q',qv,'STATES',len(byq[qv]),'DISTINCT_EPS',len(vals),'EPS_MIN',min(vals),'EPS_MAX',max(vals))
print('BOUNDARY_DISTINCT_EPS_TOTAL=',len(all_eps))
print('CARRY_SPECTRUM_FILE=/mnt/data/85_R2_CarrySpectrum.tsv')
