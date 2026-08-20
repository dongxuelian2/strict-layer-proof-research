#!/usr/bin/env python3
"""A1 J2 TLRC7 exact local/root checker.

Checks a fixed tail fibre (q,h,sigma,m,t,g), reconstructs the RCE state,
computes the scaled root kernel, local square data, and a conservative explicit
fixed-fibre period/stabilization certificate. Exact integer arithmetic only.
"""
from math import gcd,isqrt,lcm
from fractions import Fraction
import sympy as sp

ETA=Fraction(1299,500)

def vp(n,p):
    n=abs(int(n)); c=0
    if n==0: return 10**9
    while n%p==0: n//=p; c+=1
    return c

def unit10(n): return gcd(abs(int(n)),10)==1

def odd10_part(n):
    n=abs(int(n))
    while n%2==0: n//=2
    while n%5==0: n//=5
    return n

def tail_data(q):
    b=vp(q+4,5); d=2*5**b
    c=q**3+10*q*q+12*q+8
    C=q*c
    B=(q+2)*(q*q-4*q-4)
    return b,d,c,C,B

def reconstruct(G,q,N,t):
    if (G+1)%q: return None
    u=(G+1)//q; A=2*u+1; M=q*(q+4)
    R=A*t-2*N
    if R%M: return None
    Z=R//M
    anum=(G-1)*t-q*N; aden=2*(q+4)
    if anum%aden: return None
    a3=anum//aden
    if (Z+u*N)%2: return None
    X=(Z+u*N)//2
    if (N+q*Z)%2: return None
    hlin=(N+q*Z)//2
    if (A*N+(q+2)*Z)%2: return None
    mlin=(A*N+(q+2)*Z)//2
    rlin=(G//2)*hlin-u*a3
    D2=u*a3+G*X
    return dict(G=G,q=q,u=u,A=A,N=N,t=t,Z=Z,a3=a3,X=X,D2=D2,hlin=hlin,mlin=mlin,rlin=rlin)

def linear_gate(row,k):
    G,u,A=row['G'],row['u'],row['A']; K=10**k
    for z in ('a3','Z','X','D2','hlin','mlin','rlin'):
        if not(row[z]>0 and unit10(row[z])): return False,z
    if not (G//10<=row['a3']<G): return False,'DIG3'
    if not row['X']*K < ETA*u*G*G: return False,'X_RADIAL'
    if not Fraction(row['Z'],1) < 2*ETA*u/K + Fraction(2*u*A,G): return False,'Z_RADIAL'
    return True,'PASS'

def Ftilde(row): return row['A']*row['X']**2+row['Z']*row['D2']

def high_root_kernel(row,h):
    T=10**h; A=row['A']; u=row['u']; D2=row['D2']; F=Ftilde(row)
    psi=4*u*u*T*T*D2*D2-A*F
    return psi

def root_layer(row,h):
    G=row['G']; A=row['A']; u=row['u']; D2=row['D2']
    psi=high_root_kernel(row,h)
    out={'psi':psi,'nonnegative':psi>=0,'square':False,'roots':[]}
    if psi<0:return out
    s=isqrt(psi); out['square']=s*s==psi
    if out['square']:
        den=A*G
        for sg in (1,-1):
            num=2*(2*u*(10**h)*D2+sg*s)
            if num>0 and num%den==0: out['roots'].append(num//den)
    return out

def prime_factors(n): return sorted(sp.factorint(abs(int(n))).keys())

def local_square_status(psi,mods):
    ans=[]
    for p in mods:
        if p in (2,5):continue
        r=psi%p
        if r==0: ch='ZERO'
        else: ch='RESIDUE' if pow(r,(p-1)//2,p)==1 else 'NONRESIDUE'
        ans.append((p,r,ch))
    return ans

def local_p_div_q_formula(row,h,p):
    # 64 Psi mod p formula in quotient coordinates rho=(At-2N)/q=(q+4)Z.
    q=row['q']; assert q%p==0
    A=row['A']%p; T=pow(10,h,p); t=row['t']%p
    rho=((row['A']*row['t']-2*row['N'])//q)%p
    P0=(rho+A*(A-1)*t)%p
    Q0=(rho+(A*A-1)*t)%p
    val=((A-1)**2*T*T*Q0*Q0 - A*A*P0*P0 + 2*A*rho*Q0)%p
    return rho,val

def fixed_fibre_period(q,h):
    b,d,c,C,B=tail_data(q)
    S=2*d*q**3*(q+4)*c
    # S^3 has p-exponent >= 2 v_p(S)+1 for every nondecimal p|S.
    Mper=odd10_part(S**3)
    period=1 if Mper==1 else int(sp.n_order(10,Mper))
    # Safe decimal stabilization for quotient data after a square denominator S^2,
    # at LOCAL-DCDC depth 2^(h+3) 5^(h+2b).
    gst=max(h+3+2*vp(S,2), h+2*b+2*vp(S,5))
    return dict(S=S,Mper=Mper,period=period,g_stabilize=gst)

def check_fibre(q,h,sigma,m,t,g):
    G=10**g
    b,d,c,C,B=tail_data(q); alpha=sigma*m
    if (G+1)%q: return {'status':'ORDER_FAIL'}
    if (d*B*t-alpha)%q: return {'status':'E_QUOTIENT_FAIL'}
    e=(d*B*t-alpha)//q
    u=(G+1)//q
    num=alpha*u+e
    if num%(d*c): return {'status':'N_INTEGRAL_FAIL','e':e}
    N=num//(d*c)
    # equivalent raw TP2 check
    assert C*N-B*t==alpha*(G//d)
    row=reconstruct(G,q,N,t)
    if row is None:return {'status':'RCE_RECON_FAIL','N':N,'e':e}
    ok,gate=linear_gate(row,g+h)
    F=Ftilde(row); dcdc=(F%(2*10**(g+h))==0)
    root=root_layer(row,h)
    ps=prime_factors(q*(q+4))
    loc=local_square_status(root['psi'],ps)
    local_formula=[]
    for p in prime_factors(q):
        if p not in (2,5):
            rho,v=local_p_div_q_formula(row,h,p)
            assert v==(64*root['psi'])%p
            local_formula.append((p,rho,v))
    return dict(status='PASS_RECON',N=N,e=e,row=row,linear_ok=ok,linear_gate=gate,dcdc=dcdc,root=root,local=loc,local_formula=local_formula)

def known_q11_pseudo():
    out=check_fibre(11,1,+1,152510,31,471)
    assert out['status']=='PASS_RECON' and out['linear_ok'] and out['dcdc']
    assert out['root']['psi']%11==8
    assert not out['root']['square']
    assert any(p==11 and ch=='NONRESIDUE' for p,r,ch in out['local'])
    return out

if __name__=='__main__':
    p=known_q11_pseudo()
    per=fixed_fibre_period(11,1)
    print('LOCAL_STATUS=PASS')
    print('Q11_PSEUDO_N=',p['N'])
    print('Q11_PSEUDO_PSI_MOD_11=',p['root']['psi']%11)
    print('Q11_LOCAL_FORMULA=',p['local_formula'])
    print('Q11_LOCAL_STACK=',p['local'])
    print('Q11_FIXED_FIBRE_PERIOD_SAFE=',per['period'])
    print('Q11_FIXED_FIBRE_G_STABILIZE_SAFE=',per['g_stabilize'])
