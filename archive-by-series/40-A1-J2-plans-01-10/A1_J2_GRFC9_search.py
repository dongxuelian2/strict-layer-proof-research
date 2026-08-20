#!/usr/bin/env python3
"""A1 J2 GRFC9 exact targeted global-factor regression.

No expanded-g census is performed.  The script targets the two historical q=11
states that motivated the campaign and replays the inherited h=0 aggregate
counts.  All new arithmetic decisions are exact integer/modular decisions.
"""
from math import gcd, isqrt
from pathlib import Path

OUT = Path('/mnt/data')


def vp(n,p):
    n=abs(int(n)); c=0
    if n == 0: return 10**9
    while n%p==0:
        n//=p; c+=1
    return c


def unit10(n): return gcd(abs(int(n)),10)==1


def reconstruct(G,q,N,t):
    assert (G+1)%q==0
    u=(G+1)//q; A=2*u+1; M=q*(q+4)
    R=A*t-2*N
    assert R%M==0
    Z=R//M
    num=(G-1)*t-q*N; den=2*(q+4)
    assert num%den==0
    a3=num//den
    assert (Z+u*N)%2==0
    X=(Z+u*N)//2
    D2=u*a3+G*X
    return dict(G=G,q=q,u=u,A=A,N=N,t=t,M=M,R=R,Z=Z,a3=a3,X=X,D2=D2)


def ftilde(row):
    return row['A']*row['X']**2 + row['Z']*row['D2']


def psi_delta(row,delta):
    aa=10**max(delta,0); bb=10**max(-delta,0)
    return 4*row['u']**2*aa**2*row['D2']**2 - row['A']*bb**2*ftilde(row)


def q11_state(g):
    q=11; delta=1; alpha=152510; t=31
    b=vp(q+4,5); d=2*5**b
    c=q**3+10*q*q+12*q+8
    C=q*c; B=(q+2)*(q*q-4*q-4)
    G=10**g
    assert (G+1)%q==0
    num=B*t + alpha*(G//d)
    assert num%C==0
    N=num//C
    row=reconstruct(G,q,N,t)
    row.update(delta=delta,alpha=alpha,d=d,C=C,B=B,k=g+1,ell=g-1)
    return row


def legendre_status(n,p):
    r=n%p
    if r==0: return r,'ZERO'
    x=pow(r,(p-1)//2,p)
    return r, ('RESIDUE' if x==1 else 'NONRESIDUE')


def q11_regression(g, killer_prime):
    row=q11_state(g)
    F=ftilde(row); K=10**row['k']; ell=row['ell']
    psi=psi_delta(row,1)
    dcdc=(F%(2*K)==0)
    assert dcdc
    Omega=F//(2*K)
    assert unit10(row['u']) and unit10(row['D2'])
    rk,sk=legendre_status(psi,killer_prime)
    assert sk=='NONRESIDUE'

    # Exact square test for the smaller witness; for the huge witness modular NR
    # is already a proof of nonsquareness and avoids unnecessary isqrt work.
    if g <= 1000:
        global_square = psi>=0 and isqrt(psi)**2==psi
        assert not global_square
        square_certificate=f'isqrt exact; additionally mod {killer_prime}={rk} NONRESIDUE'
    else:
        global_square=False
        square_certificate=f'mod {killer_prime}={rk} NONRESIDUE (exact certificate of nonsquare)'

    structural=[3,7,11,13,73,383]
    structural_status=[(p,)+legendre_status(psi,p) for p in structural]
    if g==63501:
        assert all(st!='NONRESIDUE' for p,r,st in structural_status)

    # RQDC gives a unique residue class because u*D2 is a ten-unit.  Record a
    # 12-decimal-digit projection; the true modulus 10^ell/8 is enormous.
    mod10=10**12
    inv=pow((row['u']*row['D2'])%mod10,-1,mod10)
    kappa_suffix=(Omega%mod10)*inv%mod10

    # RCE-cleared P identity used by the new CQRF splice.
    M=row['M']; R=row['R']
    Y=R+row['u']*row['N']*M
    E=row['u']*row['q']*((row['G']-1)*row['t']-row['q']*row['N'])+row['G']*Y
    P=row['A']*Y*Y+2*R*E
    assert 4*M*M*F==P
    assert row['D2']==E//(2*M) and E%(2*M)==0

    return {
        'kind':'q11_fixed_fibre', 'g':g, 'q':11, 'delta':1, 'ell':ell,
        'k':row['k'], 'alpha':row['alpha'], 't':row['t'],
        'DCDC':'PASS', 'OMEGA_INTEGRAL':'PASS',
        'GLOBAL_SQUARE':'FAIL', 'LAYER_R':'NOT_REACHED',
        'KAPPA_INTEGER_COUNT':0, 'KDIV':'NOT_REACHED', 'RQDC':'NO_ROOT_KAPPA',
        'GRFQ':'NO_INTEGER_ROOT', 'FIRST_DEATH_GATE':'KAPPA_EXISTENCE/GLOBAL_ROOT',
        'KILLER_PRIME':killer_prime, 'PSI_MOD_KILLER':rk,
        'SQUARE_CERTIFICATE':square_certificate,
        'KAPPA_RQDC_SUFFIX_MOD_1E12':kappa_suffix,
        'STRUCTURAL_STATUS':';'.join(f'{p}:{r}:{st}' for p,r,st in structural_status),
        'CQRF_P_IDENTITY':'PASS',
    }


H0_COUNTS = {
    7:  dict(tail_integral=221288,reconstructed=2900,linear_legal=370,dcdc=28,global_square=0),
    11: dict(tail_integral=8713715,reconstructed=264156,linear_legal=10214,dcdc=44,global_square=0),
    17: dict(tail_integral=413750,reconstructed=1164,linear_legal=32,dcdc=5,global_square=0),
    19: dict(tail_integral=437896,reconstructed=969,linear_legal=21,dcdc=2,global_square=0),
}


def main():
    rows=[q11_regression(471,11), q11_regression(63501,17)]
    assert sum(v['dcdc'] for v in H0_COUNTS.values())==79
    assert sum(v['global_square'] for v in H0_COUNTS.values())==0

    tsv=OUT/'A1_J2_GRFC9_survivors.tsv'
    cols=['kind','g','q','delta','ell','k','alpha','t','DCDC','OMEGA_INTEGRAL','GLOBAL_SQUARE',
          'LAYER_R','KAPPA_INTEGER_COUNT','KDIV','RQDC','GRFQ','FIRST_DEATH_GATE','KILLER_PRIME',
          'PSI_MOD_KILLER','KAPPA_RQDC_SUFFIX_MOD_1E12','STRUCTURAL_STATUS','CQRF_P_IDENTITY']
    with tsv.open('w',encoding='utf-8') as f:
        f.write('\t'.join(cols)+'\n')
        for row in rows:
            f.write('\t'.join(str(row.get(c,'')) for c in cols)+'\n')
        for q,c in H0_COUNTS.items():
            r={
                'kind':'h0_round8_aggregate_replay','g':'<=1200','q':q,'delta':0,
                'DCDC':c['dcdc'],'GLOBAL_SQUARE':c['global_square'],
                'KAPPA_INTEGER_COUNT':0 if c['global_square']==0 else 'unknown',
                'GRFQ':'0 integer-root states in inherited exact census',
                'FIRST_DEATH_GATE':'KAPPA_EXISTENCE/GLOBAL_ROOT',
            }
            f.write('\t'.join(str(r.get(cn,'')) for cn in cols)+'\n')

    print('GRFC9_SEARCH_STATUS=PASS_EXACT_TARGETED')
    for row in rows:
        print('REGRESSION', row['g'], 'DCDC=',row['DCDC'],
              'GLOBAL_SQUARE=',row['GLOBAL_SQUARE'],
              'FIRST_DEATH_GATE=',row['FIRST_DEATH_GATE'],
              'KILLER=',row['KILLER_PRIME'],row['PSI_MOD_KILLER'])
        print('STRUCTURAL_STATUS',row['g'],row['STRUCTURAL_STATUS'])
        print('RQDC_SUFFIX_MOD_1E12',row['g'],f"{row['KAPPA_RQDC_SUFFIX_MOD_1E12']:012d}")
    print('H0_REPLAY_DCDC_TOTAL=',sum(v['dcdc'] for v in H0_COUNTS.values()))
    print('H0_REPLAY_GLOBAL_SQUARE_TOTAL=',sum(v['global_square'] for v in H0_COUNTS.values()))
    print('SURVIVOR_FILE=',tsv.name)

if __name__=='__main__':
    main()
