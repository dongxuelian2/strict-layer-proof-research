#!/usr/bin/env python3
from math import gcd, isqrt
from fractions import Fraction
from collections import Counter
import sympy as sp

# ---------- symbolic layer ----------
G,K,u,q,c,z,lam = sp.symbols('G K u q c z lam', integer=True, positive=True)
H=G/2
A=2*u+1
B=2*G+q
C1=(B*z+A*lam)/(2*K)
C2=A*c+H*lam
T=G*z+u*lam
h=q*H*z-A*c
m=A*h-G*z
r=H*h-u*c
w=G*H*z-u*A*c
d2=u*c+G*w
P1=G*H*C1
P2=u*G*C2
P3=u*c
Q0=P2+d2
V=u*G*H
D=H*C2+r

subs_res={q:(G+1)/u}
def ck(name, expr):
    e=sp.factor(sp.cancel(expr.subs(subs_res)))
    if e != 0:
        raise AssertionError((name,e))
    print(name+'=PASS')

print('85-R9 JOINT INCIDENCE CERTIFICATE')
ck('DET_qA_MINUS_B_EQUALS_2', q*A-B-2)
ck('DET_uB_MINUS_GA_EQUALS_1', u*B-G*A-1)
ck('PRE_c_ROW', c-(2*r-q*w))
ck('PRE_d2_ROW', d2-(2*u*r-w))
ck('PRE_Ar_ROW', A*r-w-m*H)
ck('PRE_GK_ROW', G*K*C1-A*C2-m)
ck('PRE_uC2_ROW', u*C2+w-H*T)
ck('PRE_THIRD_EUCLIDEAN', 2*u*K*C1-A*T-z)
ck('KP1_Q0_D', K*P1-Q0-D)
ck('Q0_P3_GHT', Q0-P3-G*H*T)

Ash=K*G**3*C1+G*C2+c
Bword=u*G**3+H*G**2+G*H
master_res=sp.factor(V*Ash-Q0*Bword)
print('SOURCE_MASTER_RAW_RESIDUAL=',master_res)
ck('SOURCE_MASTER_ON_uq_EQ_Gp1', master_res)
ck('BWORD_EQUALS_VB', Bword-V*B)
ck('ASH_EQUALS_BQ0', Ash-B*Q0)

F=sp.factor(H**2*C1**2+w**2-T*d2)
Phi=sp.factor(16*K**2*F)
Qprim=sp.factor(A*H**2*C1**2-2*u*K*d2*C1+A*w**2+z*d2)
ck('QPRIM_EQUALS_A_TIMES_F', Qprim-A*F)
ck('PRIMITIVE_SPHERE_RESIDUAL_EQUALS_G2F', P1**2+P2**2+P3**2-Q0**2-G**2*F)
print('PHI_COMPACT=G^2(Bz+A*lambda)^2+16K^2*w^2-16K^2*T*d2')
print('DEGREES_c_z_lambda=2,2,2; TOTAL_DEGREE=2')

aa=G**2*A**2/(16*K**2)
bb=G**2*A*B*z/(8*K**2)-u*d2
dd=G**2*B**2*z**2/(16*K**2)+w**2-G*z*d2
ck('LAMBDA_QUADRATIC_RECONSTRUCTION', F-(aa*lam**2+bb*lam+dd))
Delta_lam=sp.factor(bb**2-4*aa*dd)
Delta0=sp.factor(u**2*K**2*d2**2-A*H**2*(A*w**2+z*d2))
ck('DISCRIMINANT_BRIDGE_Dlambda_EQ_Delta0_OVER_K2', Delta_lam-Delta0/K**2)
print('LAMBDA_LEADING_COEFF=G^2*A^2/(16*K^2)>0')

# PLCF regression
Gp=sp.symbols('Gp', integer=True, positive=True)
up=sp.Integer(11); qp=(Gp+1)/11; Ap=sp.Integer(23); Kp=sp.Integer(10); Hp=Gp/2; Bp=2*Gp+qp
cp=zp=sp.Integer(1); lp=sp.Integer(3)
C1p=(Bp*zp+Ap*lp)/(2*Kp)
Tp=Gp*zp+up*lp
wp=Gp*Hp*zp-up*Ap*cp
d2p=up*cp+Gp*wp
Fp=sp.factor(Hp**2*C1p**2+wp**2-Tp*d2p)
Ppoly=47871*Gp**4+3159440*Gp**3-577600*Gp**2-1614236800*Gp-12321865600
if sp.factor(Fp+Ppoly/sp.Integer(193600)) != 0:
    raise AssertionError('PLCF regression')
print('PLCF_REGRESSION=PASS')
print('PLCF_F=-P(G)/193600')

# ---------- exact arithmetic source shell ----------
def unit10(n): return gcd(abs(int(n)),10)==1
def ceil_div(a,b): return (a+b-1)//b

def source_state(g,k,u0,c0,z0,l0, regular=True):
    GG=10**g; KK=10**k
    if (GG+1)%u0: return None
    qq=(GG+1)//u0
    if u0<=1 or qq<=1: return None
    AA=2*u0+1; BB=2*GG+qq; HH=GG//2; VV=u0*GG*HH
    if gcd(AA,10)!=1: return None
    if not (unit10(c0) and unit10(z0) and unit10(l0)): return None
    num=BB*z0+AA*l0
    if num%(2*KK): return None
    C10=num//(2*KK); C20=AA*c0+HH*l0; T0=GG*z0+u0*l0
    h0=qq*HH*z0-AA*c0; m0=AA*h0-GG*z0; r0=HH*h0-u0*c0
    w0=GG*HH*z0-u0*AA*c0; d20=u0*c0+GG*w0
    if min(C10,C20,T0,h0,m0,r0,w0,d20)<=0: return None
    if not all(unit10(v) for v in (h0,m0,r0,w0,d20,T0)): return None
    if regular and gcd(AA,d20)!=1: return None
    if gcd(C10,u0)!=1 or gcd(C20,HH)!=1 or gcd(c0,GG*HH)!=1: return None
    P10=GG*HH*C10; P20=u0*GG*C20; P30=u0*c0; Q00=P20+d20
    if gcd(VV,P10)!=GG*HH or gcd(VV,P20)!=u0*GG or gcd(VV,P30)!=u0: return None
    if gcd(gcd(gcd(P10,P20),P30),Q00)!=1: return None
    Ash0=KK*GG**3*C10+GG*C20+c0
    Bword0=u0*GG**3+HH*GG**2+GG*HH
    if VV*Ash0 != Q00*Bword0: return None
    x2=GG*GG*KK//10; x3=GG//10
    Ulo=max(ceil_div(x2,C20),ceil_div(x3,c0),1)
    Uhi=min((10*x2-1)//C20,(10*x3-1)//c0)
    if Ulo>Uhi: return None
    Uw=next((UU for UU in range(Ulo,Uhi+1) if gcd(UU,VV)==1),None)
    if Uw is None: return None
    F0=HH*HH*C10*C10+w0*w0-T0*d20
    return dict(g=g,k=k,G=GG,K=KK,u=u0,q=qq,A=AA,B=BB,H=HH,V=VV,
                c=c0,z=z0,lam=l0,C1=C10,C2=C20,T=T0,h=h0,m=m0,r=r0,w=w0,d2=d20,
                P1=P10,P2=P20,P3=P30,Q0=Q00,U=Uw,Ulo=Ulo,Uhi=Uhi,F=F0)

def assert_source_example(g,k,u0,c0,z0,l0, expected_sign):
    s=source_state(g,k,u0,c0,z0,l0)
    if s is None: raise AssertionError('source example failed')
    sign='N' if s['F']<0 else 'P' if s['F']>0 else 'Z'
    if sign!=expected_sign: raise AssertionError((sign,expected_sign))
    UU=s['U']
    a1,a2,a3=UU*s['C1'],UU*s['C2'],UU*s['c']
    b1,b2,b3=s['u'],s['H'],s['G']*s['H']
    if any(gcd(a,b)!=1 for a,b in [(a1,b1),(a2,b2),(a3,b3)]): raise AssertionError('reducedness')
    # current profile: n2=2g+k, n3=g; denominator shifts m2=g,m3=2g
    Ash_actual=a1*10**((2*g+k)+g)+a2*10**g+a3
    Bword_actual=b1*10**(g+2*g)+b2*10**(2*g)+b3
    if s['V']*Ash_actual != UU*s['Q0']*Bword_actual: raise AssertionError('actual master')
    return s,(a1,a2,a3),(b1,b2,b3),Ash_actual,Bword_actual

Nstate,Nab,Nbb,NAw,NBw=assert_source_example(4,1,73,147,1,25969,'N')
Pstate,Pab,Pbb,PAw,PBw=assert_source_example(4,1,73,147,1,25989,'P')
print('SIGN_CHANGE_N_STATE=', {k:Nstate[k] for k in ('c','z','lam','C1','C2','T','w','d2','U','F')})
print('SIGN_CHANGE_N_ACTUAL_BLOCKS=',Nab,Nbb)
print('SIGN_CHANGE_N_WORDS=',NAw,NBw)
print('SIGN_CHANGE_P_STATE=', {k:Pstate[k] for k in ('c','z','lam','C1','C2','T','w','d2','U','F')})
print('SIGN_CHANGE_P_ACTUAL_BLOCKS=',Pab,Pbb)
print('SIGN_CHANGE_P_WORDS=',PAw,PBw)
print('JOINT_SIGN=CHANGES_SIGN')

# Exact c=147,z=1 line census, lambda <= 40000
line=Counter(); line_states=[]
for lv in range(1,40001):
    s=source_state(4,1,73,147,1,lv)
    if s:
        sg='N' if s['F']<0 else 'P' if s['F']>0 else 'Z'
        line[sg]+=1; line_states.append(s)
print('LINE_C147_Z1_LAM_LE_40000=',dict(line),'TOTAL=',sum(line.values()))
for a0,b0 in zip(line_states,line_states[1:]):
    if a0['F']*b0['F']<0:
        print('ADJACENT_SOURCE_SIGN_TRANSITION=',(a0['lam'],a0['F']),(b0['lam'],b0['F']))
        break

# R7 original fixed box, now with full source-shell checks and F census
box=Counter(); modsets={M:set() for M in (5,8,16,20,25,40,80)}; modzero={}
for c0 in range(1,5001):
    if not unit10(c0): continue
    for l0 in range(1,2001):
        if not unit10(l0): continue
        s=source_state(4,1,73,c0,1,l0)
        if not s: continue
        box['SOURCE_SHELL']+=1
        sg='N' if s['F']<0 else 'P' if s['F']>0 else 'Z'
        box[sg]+=1
        for M in modsets:
            rr=s['F']%M; modsets[M].add(rr)
            if rr==0 and M not in modzero:
                modzero[M]=(c0,1,l0,s['U'],s['F'])
print('R7_BOX_FULL_SOURCE_CENSUS=',dict(box))
print('FIXED_MODULUS_ZERO_COMPATIBILITY=',modzero)

# Fixed-base Class-Z census using root-conditional NRSEC Uz bound.
def root_scan(g,k,u0):
    GG=10**g; KK=10**k; qq=(GG+1)//u0; AA=2*u0+1; BB=2*GG+qq; HH=GG//2
    eta=Fraction(1299,500)
    zbound=Fraction(2*1299*u0,500*KK)+Fraction(2*u0*AA,GG)  # z < bound, since U>=1
    zmax=(zbound.numerator-1)//zbound.denominator
    st=Counter(); squares=[]; zeros=[]
    for c0 in range(1,GG):
        if not unit10(c0): continue
        for z0 in range(1,zmax+1):
            if not unit10(z0): continue
            h0=qq*HH*z0-AA*c0; m0=AA*h0-GG*z0; r0=HH*h0-u0*c0
            w0=GG*HH*z0-u0*AA*c0; d20=u0*c0+GG*w0
            if min(h0,m0,r0,w0,d20)<=0: continue
            if not all(unit10(v) for v in (h0,m0,r0,w0,d20)): continue
            if gcd(AA,d20)!=1: continue
            st['LINEAR']+=1
            D0=u0*u0*KK*KK*d20*d20-AA*HH*HH*(AA*w0*w0+z0*d20)
            if D0<0:
                st['DISC_NEG']+=1; continue
            st['DISC_NONNEG']+=1
            rr=isqrt(D0)
            if rr*rr!=D0: continue
            st['DISC_SQUARE']+=1
            if len(squares)<5: squares.append((c0,z0,D0,rr))
            den=AA*HH*HH
            for sg in (-1,1):
                nn=u0*KK*d20+sg*rr
                if nn<=0 or nn%den: continue
                C10=nn//den; st['INTEGRAL_C1']+=1
                lnum=2*KK*C10-BB*z0
                if lnum<=0 or lnum%AA: continue
                l0=lnum//AA
                s=source_state(g,k,u0,c0,z0,l0)
                if s and s['F']==0:
                    zeros.append(s); st['SOURCE_Z']+=1
    return zbound,zmax,st,squares,zeros

for base in ((4,1,73),(4,2,73),(5,1,11)):
    zb,zm,st,sq,zs=root_scan(*base)
    print('ROOT_CENSUS_BASE=',base,'Z_BOUND=',zb,'ZMAX=',zm,'STATS=',dict(st),'SQUARE_EXAMPLES=',sq,'SOURCE_Z_COUNT=',len(zs))

print('JOINT_ROOT_SOURCE_INCIDENCE=UNKNOWN')
print('R9_SUCCESS_LEVEL=R9-S1_PLUS_EXPLICIT_DOMAIN_BELOW_S2')
print('R9_TERMINAL_VERDICT=OLD_NRSEC_INTERFACE_REAPPEARS')
print('CERTIFICATE_STATUS=PASS')
