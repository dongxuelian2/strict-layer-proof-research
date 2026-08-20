#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path

ROOT = Path('/mnt/data')


def ceildiv(a:int,b:int)->int:
    return (a+b-1)//b


def vp(n:int,p:int)->int:
    if n == 0:
        raise ValueError('vp(0,p) is not used in this archive')
    e=0
    while n%p==0:
        n//=p; e+=1
    return e


def factorint(n:int)->dict[int,int]:
    n=abs(n)
    if n==0: raise ValueError('factorint(0)')
    out={}
    for p in (2,3,5):
        while n%p==0:
            out[p]=out.get(p,0)+1; n//=p
    d=7
    step=4
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d += step
        step = 6-step
    if n>1: out[n]=out.get(n,0)+1
    return out


def facstr(n:int)->str:
    if n==1: return '1'
    f=factorint(n)
    return '*'.join(str(p) if e==1 else f'{p}^{e}' for p,e in sorted(f.items()))


def divisors_from_factor(f:dict[int,int])->list[int]:
    ds=[1]
    for p,e in sorted(f.items()):
        old=ds[:]
        mult=1
        new=[]
        for k in range(e+1):
            if k: mult*=p
            new.extend(d*mult for d in old)
        ds=new
    return sorted(ds)


def divisors(n:int)->list[int]:
    return divisors_from_factor(factorint(n))


@lru_cache(None)
def cf_factorizations(n:int):
    """Exact CF factorizations c^2 X0 Y0=n with X0>Y0, gcd=1, P1,Q0 integral."""
    f=factorint(n)
    # c has exponent 0..floor(e/2) at each prime.
    cf={p:e//2 for p,e in f.items() if e//2}
    cands=divisors_from_factor(cf) if cf else [1]
    rows=[]
    for c in cands:
        m=n//(c*c)
        for y0 in divisors(m):
            x0=m//y0
            if x0<=y0 or gcd(x0,y0)!=1: continue
            if (c*(x0-y0))%2: continue
            p1=c*(x0-y0)//2
            q0=c*(x0+y0)//2
            rows.append((c,x0,y0,p1,q0))
    return tuple(rows)


def enrich(row:dict)->dict:
    r=dict(row)
    N=r['NM']; om=r['Omega']; p1=r['P1']; q0=r['Q0']; D=r['D']
    u0=r.get('U0',1); A=r['A']; W=r['W']; X=r.get('X',10); Y=r.get('Y',10); G=r.get('G',1)
    h=gcd(p1,q0)
    assert gcd(D,p1)==h
    delta=D//h
    d=gcd(N,p1)
    E=N//d
    g0=gcd(u0*A*W,p1)
    assert d%g0==0
    Rm=d//g0
    L=u0*A*W*X*Y*G
    p=p1//h
    assert gcd(p,delta)==1
    s=gcd(L,p)
    Esrc=L//s
    assert E==delta*Esrc
    assert d==h*s
    assert N//(g0*E)==Rm
    gs=N//om
    assert N%om==0
    lower=(om%E==0)
    upper=((N//g0)%om==0)
    corridor=lower and upper
    # Equivalent original corridor.
    assert corridor == (gs%g0==0 and p1%gs==0)
    gr=gcd(om,E)
    momega_rat=f'{om//gr}/{E//gr}' if E//gr!=1 else str(om//gr)
    if lower:
        momega=om//E
        assert corridor == (Rm%momega==0)
    else:
        momega=''
    bad=[]
    primes=sorted(set(factorint(E))|set(factorint(om)))
    for prime in primes:
        ee=vp(E,prime) if E%prime==0 else 0
        eo=vp(om,prime) if om%prime==0 else 0
        if ee>eo:
            bad.append((prime,ee,eo))
    pbad=bad[0][0] if bad else ''
    e2=max(vp(X*Y*G,2)-vp(p1,2),0)
    e5=max(vp(X*Y*G,5)-vp(p1,5),0)
    vo2=vp(om,2) if om%2==0 else 0
    vo5=vp(om,5) if om%5==0 else 0
    B=W+A*Y*G
    S=r.get('NR',r.get('C3'))+Y*r.get('MR',r.get('C2'))
    # residue modulo delta; for delta=1 it is 0 by definition.
    residue=(h*(r.get('K',10))*p*B-A*W*S)%delta if delta>1 else 0
    assert om%delta == residue
    out={
        'H':h,'D_OVER_H':delta,'GCD_NM_P1':d,'EM':E,'RM':Rm,
        'L_SOURCE':L,'P1_REDUCED':p,'ABSORBED_SOURCE_GCD':s,'E_SRC':Esrc,
        'LOWER_EM_DIVIDES_OMEGA':int(lower),'UPPER_OMEGA_DIVIDES_NM_OVER_G0':int(upper),
        'OMEGA_CORRIDOR_PASS':int(corridor),'M_OMEGA':momega,'M_OMEGA_RATIONAL':momega_rat,
        'EM_GT_OMEGA':int(E>om),'EM_MOD_OMEGA':E%om,'OMEGA_MOD_EM':om%E,
        'D_OVER_H_DIVIDES_OMEGA':int(om%delta==0), 'D_RESIDUE':residue,
        'DECIMAL_EXCESS_2':e2,'DECIMAL_EXCESS_5':e5,'VP2_OMEGA':vo2,'VP5_OMEGA':vo5,
        'DEC2_LOCAL_FAIL':int(vo2<e2),'DEC5_LOCAL_FAIL':int(vo5<e5),
        'FIRST_BAD_PRIME':pbad,
        'BAD_PRIME_LEDGER':';'.join(f'{p0}:{ee}>{eo}' for p0,ee,eo in bad),
        'FAC_NM':facstr(N),'FAC_P1':facstr(p1),'FAC_OMEGA':facstr(om),'FAC_EM':facstr(E),'FAC_D_OVER_H':facstr(delta),
    }
    # Exact post-D quotient gate when delta passes.
    if om%delta==0:
        od=om//delta
        out['OMEGA_D']=od
        out['POST_D_E_SRC_DIVIDES_OMEGA_D']=int(od%Esrc==0)
        out['OMEGA_D_MOD_E_SRC']=od%Esrc
    else:
        out['OMEGA_D']=''; out['POST_D_E_SRC_DIVIDES_OMEGA_D']=''; out['OMEGA_D_MOD_E_SRC']=''
    r.update(out)
    return r


def enumerate_core(u:int,c2:int,c3:int):
    cnt=Counter(); masters=[]
    for b2 in range(1,10):
        if gcd(b2,c2)!=1: continue
        for b3 in range(1,10):
            if gcd(b3,c3)!=1: continue
            for z in divisors(gcd(b2,b3)):
                A=b2//z; W=b3//z
                p2=W*c2; p3=A*c3
                for c,x0,y0,p1,q0 in cf_factorizations(p2*p2+p3*p3):
                    cnt['CF']+=1
                    if gcd(gcd(gcd(p1,p2),p3),q0)!=1: continue
                    cnt['PRIMITIVE']+=1
                    D=10*p1-q0; t3=q0-p3
                    if D<=0 or t3<=0: continue
                    cnt['D_RATIO']+=1
                    if (z*W*t3)%10!=0: continue
                    cnt['TAIL']+=1
                    omega=W*t3-A*10*(p2-q0)
                    # OMEGA2 exact identity for g=0,k=1,X=Y=10,G=1.
                    omega2=q0*(W+A*10)-A*W*(c3+10*c2)
                    assert omega==omega2
                    nm=A*W*100*D
                    if omega<=0 or nm%omega:
                        cnt['MASTER_NONINTEGER_ROWS']+=1; continue
                    gs=nm//omega
                    if gs<=0:
                        cnt['MASTER_NONINTEGER_ROWS']+=1; continue
                    cnt['MASTER_INTEGER_ROWS']+=1
                    g0=gcd(A*W,p1)
                    cor=(gs%g0==0 and p1%gs==0)
                    cnt['CORRIDOR_PASS_ROWS' if cor else 'CORRIDOR_FAIL_ROWS']+=1
                    row={
                        'U':u,'U0':1,'MR':c2,'NR':c3,'N2':2,'N3':1,'C2':c2,'C3':c3,
                        'g':0,'k':1,'m2':1,'m3':1,'G':1,'K':10,'X':10,'Y':10,
                        'b2':b2,'b3':b3,'z_R14':z,'A':A,'W':W,'c':c,'X0':x0,'Y0':y0,
                        'P1':p1,'P2':p2,'P3':p3,'Q0':q0,'D':D,'T3':t3,'Omega':omega,'NM':nm,
                        'G1_STAR':gs,'M0':A*W,'G0':g0,'OLD_G1_STAR_DIVIDES_P1':int(p1%gs==0),
                    }
                    masters.append(enrich(row))
    if cnt['CF']==0: first='FAIL_CF'
    elif cnt['PRIMITIVE']==0: first='FAIL_PRIMITIVE'
    elif cnt['D_RATIO']==0: first='FAIL_D_RATIO'
    elif cnt['TAIL']==0: first='FAIL_TAIL'
    elif cnt['MASTER_INTEGER_ROWS']==0: first='FAIL_MASTER_NONINTEGER'
    elif cnt['CORRIDOR_PASS_ROWS']==0: first='FAIL_G1_CORRIDOR'
    else: first='POST_CORRIDOR'
    return cnt,masters,first


def enumerate_u1_u9():
    registry=[]; masters=[]; by_u=defaultdict(Counter)
    for u in range(1,10):
        for c2 in range(ceildiv(10,u),99//u+1):
            for c3 in range(1,9//u+1):
                cnt,rows,first=enumerate_core(u,c2,c3)
                masters.extend(rows); by_u[u][first]+=1
                registry.append({
                    'U':u,'U0':1,'MR':c2,'NR':c3,'N2':2,'N3':1,'C2':c2,'C3':c3,
                    'CF_FACTOR_ROWS':cnt['CF'],'PRIMITIVE_PASS_ROWS':cnt['PRIMITIVE'],'D_T3_PASS_ROWS':cnt['D_RATIO'],
                    'TAIL_PASS_ROWS':cnt['TAIL'],'MASTER_INTEGER_ROWS':cnt['MASTER_INTEGER_ROWS'],
                    'OMEGA_CORRIDOR_PASS_ROWS':cnt['CORRIDOR_PASS_ROWS'],'FIRST_FAILURE':first,
                    'R16_CERTIFICATION':'EXACT_EMPTY_BY_NECESSARY_GATE' if first!='POST_CORRIDOR' else 'POST_CORRIDOR_REQUIRES_Z',
                })
    return registry,masters,by_u


def write_csv(path:Path, rows:list[dict], fields:list[str]|None=None):
    if fields is None:
        fields=[]
        seen=set()
        for r in rows:
            for k in r:
                if k not in seen:
                    seen.add(k); fields.append(k)
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore')
        w.writeheader()
        for r in rows:w.writerow(r)


def verify_construct(row:dict)->dict:
    r=dict(row)
    u0=1
    assert r['g']>=0 and r['k']>=1 and r['g']+r['k']<=r['n2']-1
    assert r['m2']==r['n2']-r['g']-r['k'] and r['m3']==r['n3']+r['g']
    assert r['G']==10**r['g'] and r['K']==10**r['k'] and r['X']==10**r['m2'] and r['Y']==10**r['n3']
    assert gcd(r['A'],r['C2'])==1 and gcd(r['W'],r['C3'])==1 and gcd(r['A'],r['W'])==1
    assert r['P2']==r['W']*r['C2'] and r['P3']==r['A']*r['C3']
    assert r['c']**2*r['X0']*r['Y0']==r['P2']**2+r['P3']**2
    assert gcd(r['X0'],r['Y0'])==1
    assert r['P1']==r['c']*(r['X0']-r['Y0'])//2 and r['Q0']==r['c']*(r['X0']+r['Y0'])//2
    assert gcd(gcd(gcd(r['P1'],r['P2']),r['P3']),r['Q0'])==1
    assert r['D']==r['K']*r['P1']-r['Q0']>0
    assert r['T3']==r['Q0']-r['P3']>0
    om1=r['W']*r['T3']-r['A']*r['Y']*(r['P2']-r['G']*r['Q0'])
    om2=r['Q0']*(r['W']+r['A']*r['Y']*r['G'])-r['A']*r['W']*(r['C3']+r['Y']*r['C2'])
    assert om1==om2==r['Omega']>0
    nm=u0*r['A']*r['W']*r['X']*r['Y']*r['G']*r['D']
    assert nm==r['NM'] and nm%r['Omega']==0
    assert nm//r['Omega']==r['G1_STAR']
    r.update({'U':1,'U0':1,'MR':r['C2'],'NR':r['C3'],'M0':r['A']*r['W'],'G0':gcd(r['A']*r['W'],r['P1']),
              'OLD_G1_STAR_DIVIDES_P1':int(r['P1']%r['G1_STAR']==0)})
    return enrich(r)


def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
    return h.hexdigest()


def main():
    core_registry, masters19, by_u = enumerate_u1_u9()
    assert len(core_registry)==1191
    assert len(masters19)==163
    assert all(r['OMEGA_CORRIDOR_PASS']==0 for r in masters19)
    assert all(r['EM_GT_OMEGA']==1 for r in masters19)
    assert all(r['UPPER_OMEGA_DIVIDES_NM_OVER_G0']==1 for r in masters19)

    m132=[r for r in masters19 if r['U']<=3]
    assert len(m132)==132
    for i,r in enumerate(m132): r['R15_ROW_ID']=i
    old_size=[r for r in m132 if r['G1_STAR']>r['P1']]
    old_six=[r for r in m132 if r['G1_STAR']<=r['P1']]
    assert len(old_size)==126 and len(old_six)==6
    assert all(r['EM_GT_OMEGA']==1 for r in m132)
    assert [(r['R15_ROW_ID'],r['U']) for r in old_six]==[(35,1),(36,1),(37,1),(94,2),(95,2),(96,2)]

    # Two exact non-size survivors found in the R16 construct campaign. They are not corridor passes.
    NS1=verify_construct({
        'C2':289,'C3':59,'n2':3,'n3':2,'g':1,'k':1,'m2':1,'m3':3,'G':10,'K':10,'X':10,'Y':100,
        'A':9,'W':8,'c':197,'X0':145,'Y0':1,'P1':14184,'P2':2312,'P3':531,'Q0':14381,
        'D':127459,'T3':13850,'Omega':127459000,'NM':91770480000,'G1_STAR':720,
    })
    NS2=verify_construct({
        'C2':388,'C3':31,'n2':3,'n3':2,'g':1,'k':1,'m2':1,'m3':3,'G':10,'K':10,'X':10,'Y':100,
        'A':3,'W':5,'c':13,'X0':221,'Y0':101,'P1':780,'P2':1940,'P3':93,'Q0':2093,
        'D':5707,'T3':2000,'Omega':5707000,'NM':856050000,'G1_STAR':150,
    })
    construct_rows=[NS1,NS2]
    assert all(r['EM_GT_OMEGA']==0 and r['OMEGA_CORRIDOR_PASS']==0 for r in construct_rows)
    assert all(r['D_OVER_H_DIVIDES_OMEGA']==1 for r in construct_rows)
    assert NS1['FIRST_BAD_PRIME']==2 and NS2['FIRST_BAD_PRIME']==5
    assert NS1['E_SRC']==10000 and NS1['OMEGA_D']==197000
    assert NS2['E_SRC']==2500 and NS2['OMEGA_D']==13000

    # Minimal failure certificate: S=size, P=prime excess, U=upper corridor.
    for r in masters19+construct_rows:
        if r['EM_GT_OMEGA']:
            r['CERTIFICATE_TYPE']='S'; r['CERTIFICATE']='EM>Omega'
        elif not r['LOWER_EM_DIVIDES_OMEGA']:
            r['CERTIFICATE_TYPE']='P'; r['CERTIFICATE']=f"p={r['FIRST_BAD_PRIME']}: v_p(Omega)<v_p(EM)"
        elif not r['UPPER_OMEGA_DIVIDES_NM_OVER_G0']:
            r['CERTIFICATE_TYPE']='U'; r['CERTIFICATE']='Omega !| NM/g0'
        else:
            r['CERTIFICATE_TYPE']='PASS'; r['CERTIFICATE']='FULL_OMEGA_CORRIDOR_PASS'

    # Main corridor registry: all complete U1-U9 master rows + the two non-size construct survivors.
    omega_rows=[]
    for r in masters19:
        x=dict(r); x['SCOPE']='R15_COMPLETE_U1_U9'; omega_rows.append(x)
    for j,r in enumerate(construct_rows,1):
        x=dict(r); x['SCOPE']=f'R16_CONSTRUCT_NON_SIZE_{j}'; omega_rows.append(x)
    write_csv(ROOT/'105_R16_Omega_Corridor_Registry.csv',omega_rows)
    write_csv(ROOT/'105_R16_R15_132_Reclassification.csv',m132)

    six_rows=[]
    for r in old_six:
        x=dict(r)
        x['ROW_ID']=r['R15_ROW_ID']
        x['WHY_OLD_SIZE_FAILS']='G1_STAR<=P1'
        x['WHY_COMPLEMENT_SIZE_KILLS']='gcd(NM,P1)=2 << P1; EM=90*Omega'
        x['COMMON_D_CHANNEL']='D/h=3^4*37 but v3(Omega)=2<4'
        x['CANONICAL_BAD_PRIME']='2'
        six_rows.append(x)
    write_csv(ROOT/'105_R16_R15_Six_Exceptional_Autopsy.csv',six_rows)

    # D/h audit, including two non-size construct rows and an exact D=h tail-stage witness.
    drows=[]
    for x in omega_rows:
        rr={k:x.get(k,'') for k in [
            'SCOPE','U','C2','C3','A','W','P1','Q0','D','H','D_OVER_H','FAC_D_OVER_H','Omega','D_OVER_H_DIVIDES_OMEGA',
            'D_RESIDUE','OMEGA_D','E_SRC','POST_D_E_SRC_DIVIDES_OMEGA_D','OMEGA_D_MOD_E_SRC','OMEGA_CORRIDOR_PASS']}
        rr['MASTER_INTEGRAL']=1; rr['STAGE']='MASTER_INTEGRAL'
        drows.append(rr)
    # Exact source-possible D=h branch witness: passes CF/primitive/D,T3/tail but master is nonintegral.
    d1={'SCOPE':'D_EQ_H_PREMASTER_TAIL_WITNESS','U':1,'C2':19,'C3':7,'A':2,'W':3,'P1':6,'Q0':59,
        'D':1,'H':1,'D_OVER_H':1,'FAC_D_OVER_H':'1','Omega':175,'D_OVER_H_DIVIDES_OMEGA':1,'D_RESIDUE':0,
        'OMEGA_D':'','E_SRC':'','POST_D_E_SRC_DIVIDES_OMEGA_D':'','OMEGA_D_MOD_E_SRC':'','OMEGA_CORRIDOR_PASS':'',
        'MASTER_INTEGRAL':0,'STAGE':'CF_PRIMITIVE_D_T3_TAIL_PASS__MASTER_NONINTEGRAL',
        'EXACT_WITNESS_DATA':'b2=4;b3=6;z=2;c=1;X0=65;Y0=53;P2=57;P3=14;T3=45;NM=600;NM%Omega=75'}
    assert d1['D']==d1['H'] and d1['D_OVER_H']==1 and d1['Omega']>0 and 600%175!=0
    drows.append(d1)
    write_csv(ROOT/'105_R16_D_Over_H_Audit.csv',drows)

    decrows=[]
    for x in omega_rows:
        decrows.append({k:x.get(k,'') for k in [
            'SCOPE','U','C2','C3','g','k','X','Y','G','A','W','P1','Omega','EM','DECIMAL_EXCESS_2','DECIMAL_EXCESS_5',
            'VP2_OMEGA','VP5_OMEGA','DEC2_LOCAL_FAIL','DEC5_LOCAL_FAIL','FIRST_BAD_PRIME','E_SRC','OMEGA_D','POST_D_E_SRC_DIVIDES_OMEGA_D']})
    write_csv(ROOT/'105_R16_Decimal_Excess_Audit.csv',decrows)

    write_csv(ROOT/'105_R16_U1_U9_Corridor_Certification.csv',core_registry)

    # Prime atlas: row-level complement prime ledger + aggregate counts.
    atlas=[]
    scoped=[('R15_132',m132),('R15_U1_U9_MASTER_163',masters19),('R16_NON_SIZE_2',construct_rows)]
    for scope,rows in scoped:
        first=Counter(r['FIRST_BAD_PRIME'] for r in rows if r['FIRST_BAD_PRIME']!='')
        allbad=Counter()
        for idx,r in enumerate(rows):
            N=r['NM']; p1=r['P1']; om=r['Omega']; E=r['EM']; delta=r['D_OVER_H']; Esrc=r['E_SRC']
            U0=r.get('U0',1)
            components={'u0':U0,'A':r['A'],'W':r['W'],'X':r['X'],'Y':r['Y'],'G':r['G']}
            for p0 in sorted(factorint(E)):
                vN=vp(N,p0); vP=vp(p1,p0) if p1%p0==0 else 0
                Delta=max(vN-vP,0)
                if Delta<=0: continue
                vE=vp(E,p0); vO=vp(om,p0) if om%p0==0 else 0
                vDel=vp(delta,p0) if delta%p0==0 else 0
                vSrc=vp(Esrc,p0) if Esrc%p0==0 else 0
                raw=[f'{name}:{vp(val,p0)}' for name,val in components.items() if val%p0==0]
                origin=[]
                if vDel: origin.append(f'D_OVER_H:{vDel}')
                if vSrc: origin.append(f'REDUCED_SOURCE_EXCESS:{vSrc}[raw '+','.join(raw)+']')
                local=int(vO>=vE)
                if not local: allbad[p0]+=1
                atlas.append({
                    'RECORD_TYPE':'PRIME_LEDGER','SCOPE':scope,'ROW_KEY':r.get('R15_ROW_ID',idx),
                    'U':r.get('U',''),'C2':r['C2'],'C3':r['C3'],'A':r['A'],'W':r['W'],'P':p0,
                    'VP_NM':vN,'VP_P1':vP,'DELTA_P':vN-vP,'VP_EM':vE,'VP_OMEGA':vO,
                    'VP_D_OVER_H':vDel,'VP_E_SRC':vSrc,'SOURCE_OF_EXCESS':';'.join(origin),
                    'CORRIDOR_LOCAL_PASS':local,'IS_CANONICAL_FIRST_BAD':int(r['FIRST_BAD_PRIME']==p0),
                    'CERTIFICATE_TYPE':r.get('CERTIFICATE_TYPE',''),'OMEGA_CORRIDOR_PASS':r['OMEGA_CORRIDOR_PASS']})
        primes=sorted(set(first)|set(allbad))
        for p0 in primes:
            atlas.append({'RECORD_TYPE':'AGGREGATE','SCOPE':scope,'P':p0,'FIRST_BAD_COUNT':first[p0],'ANY_DEFICIT_COUNT':allbad[p0]})
    write_csv(ROOT/'105_R16_Master_Complement_Prime_Atlas.csv',atlas)

    # Construct-search registry. These are exact batches executed in R16; counts are audit records.
    search_summaries=[
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'B0_R15_CANONICAL_REPLAY','SCOPE':'u0=U=1; C2=10..120; C3=1..40; all legal exponent charts; A,W<=12','CF_FACTOR_ROWS':519323,'MASTER_INTEGRAL_SHAPES':103,'EM_LE_OMEGA':0,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'B1_EXPAND','SCOPE':'u0=U=1; C2=10..200; C3=1..60; all legal exponent charts; A,W<=20','CF_FACTOR_ROWS':4658455,'MASTER_INTEGRAL_SHAPES':268,'EM_LE_OMEGA':0,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'B2_EXPAND','SCOPE':'u0=U=1; C2=201..300; C3=1..80; all legal exponent charts; A,W<=20','CF_FACTOR_ROWS':5572543,'MASTER_INTEGRAL_SHAPES':117,'EM_LE_OMEGA':1,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'B3_EXPAND','SCOPE':'u0=U=1; C2=301..400; C3=1..100; all legal exponent charts; A,W<=20','CF_FACTOR_ROWS':7317851,'MASTER_INTEGRAL_SHAPES':106,'EM_LE_OMEGA':1,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'B4_EXPAND','SCOPE':'u0=U=1; C2=401..500; C3=10..99; all legal exponent charts; A,W<=20','CF_FACTOR_ROWS':7012701,'MASTER_INTEGRAL_SHAPES':89,'EM_LE_OMEGA':0,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'F1_G1K1','SCOPE':'n2=3,n3=2,g=k=1; C2=100..250; C3=10..99; A<=9,W<=40','CF_FACTOR_ROWS':4768162,'MASTER_INTEGRAL_SHAPES':4,'EM_LE_OMEGA':0,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'F2_G1K1','SCOPE':'n2=3,n3=2,g=k=1; C2=251..450; C3=10..99; A<=9,W<=40','CF_FACTOR_ROWS':6781051,'MASTER_INTEGRAL_SHAPES':10,'EM_LE_OMEGA':2,'OMEGA_CORRIDOR_PASS':0},
        {'RECORD_TYPE':'SEARCH_BATCH','BATCH_ID':'F3_G1K1','SCOPE':'n2=3,n3=2,g=k=1; C2=451..600; C3=10..99; A<=9,W<=40','CF_FACTOR_ROWS':5301916,'MASTER_INTEGRAL_SHAPES':1,'EM_LE_OMEGA':0,'OMEGA_CORRIDOR_PASS':0},
    ]
    for j,r in enumerate(construct_rows,1):
        search_summaries.append({
            'RECORD_TYPE':'NON_SIZE_SURVIVOR','BATCH_ID':f'NS{j}','SCOPE':'exact finite shape',
            'C2':r['C2'],'C3':r['C3'],'A':r['A'],'W':r['W'],'c':r['c'],'X0':r['X0'],'Y0':r['Y0'],
            'P1':r['P1'],'Q0':r['Q0'],'D':r['D'],'H':r['H'],'D_OVER_H':r['D_OVER_H'],'Omega':r['Omega'],'NM':r['NM'],
            'G1_STAR':r['G1_STAR'],'G0':r['G0'],'EM':r['EM'],'RM':r['RM'],'M_OMEGA':r['M_OMEGA'],'M_OMEGA_RATIONAL':r['M_OMEGA_RATIONAL'],
            'E_SRC':r['E_SRC'],'OMEGA_D':r['OMEGA_D'],'FIRST_BAD_PRIME':r['FIRST_BAD_PRIME'],
            'OMEGA_CORRIDOR_PASS':r['OMEGA_CORRIDOR_PASS'],
        })
    write_csv(ROOT/'105_R16_Corridor_Construct_Search.csv',search_summaries)

    # First-failure registry.
    ff=[
        {'ORDER':1,'GATE':'MASTER_INTEGRALITY','EXACT_TEST':'Omega>0 and Omega|NM','STATUS':'FROZEN_FROM_R15'},
        {'ORDER':2,'GATE':'COMPLEMENT_SIZE','EXACT_TEST':'EM<=Omega','STATUS':'R15_132: 0/132 survive; R15_U1_U9 master 163: 0/163 survive; NOT universal (NS1,NS2 survive)'},
        {'ORDER':3,'GATE':'D_OVER_H_CHANNEL','EXACT_TEST':'delta_D=D/h divides Omega','STATUS':'necessary, not universal obstruction; NS1,NS2 pass'},
        {'ORDER':4,'GATE':'POST_D_REDUCED_SOURCE_EXCESS','EXACT_TEST':'E_SRC=L/gcd(L,P1/h) divides Omega_D=Omega/(D/h)','STATUS':'CURRENT_FIRST_FAILURE; NS1,NS2 both fail'},
        {'ORDER':5,'GATE':'ABSORPTION_DIVISOR_MEMBERSHIP','EXACT_TEST':'m_Omega=Omega/EM in Div((NM,P1)/g0)','STATUS':'exact full corridor theorem; no hit found'},
        {'ORDER':6,'GATE':'R15_Z_SHELL','EXACT_TEST':'z=Lambda*q, gcd(q,F)=1, q in exact interval','STATUS':'NOT_ACTIVATED'},
    ]
    write_csv(ROOT/'105_R16_First_Failure_Registry.csv',ff)

    # Reclassification stats.
    pbad132=Counter(r['FIRST_BAD_PRIME'] for r in m132)
    pbad163=Counter(r['FIRST_BAD_PRIME'] for r in masters19)
    d_fail132=sum(1 for r in m132 if not r['D_OVER_H_DIVIDES_OMEGA'])
    d_fail163=sum(1 for r in masters19 if not r['D_OVER_H_DIVIDES_OMEGA'])
    dec2_132=sum(r['DEC2_LOCAL_FAIL'] for r in m132); dec5_132=sum(r['DEC5_LOCAL_FAIL'] for r in m132)
    dec2_163=sum(r['DEC2_LOCAL_FAIL'] for r in masters19); dec5_163=sum(r['DEC5_LOCAL_FAIL'] for r in masters19)

    # D=h branch audit within complete master rows.
    d_eq_h_master=sum(1 for r in masters19 if r['D_OVER_H']==1)
    assert d_eq_h_master==0

    # Main report.
    report=r'''# 105-R16 — Master Complement Divisor × Ω-Divisor Corridor × Decimal/D-Excess Content × Corridor-Empty-or-First-Pass

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — A1-only  
**Round:** 105-R16  
**Arithmetic:** exact integers only  
**Terminal class:** **STRUCTURAL REDUCTION; COMPLETE R15 CHAMBER RECLASSIFIED; TWO NON-SIZE SURVIVORS FOUND AND KILLED; NO CORRIDOR PASS**

## 1. Executive Verdict

R16 严格证明了 master complement dualization，并把 R15 的 corridor

\[
 g_0\mid g_1^*\mid P_1
\]

等价改写为

\[
\boxed{E_M\mid\Omega\mid N_M/g_0},\qquad
E_M=\frac{{N_M}}{{(N_M,P_1)}}.
\]

这不是单纯换名：进一步令

\[
L=u_0AWXYG,\quad P_1=hp,\quad D=h\delta,\quad h=(P_1,Q_0),
\]

则得到 exact factorization

\[
\boxed{E_M=\delta\,E_{{\rm src}},\qquad
E_{{\rm src}}=\frac{{L}}{{(L,p)}}.}
\]

所以 \(D/h=\delta\) 是 **整块强制因子**，而在 \(\delta\mid\Omega\) 之后，lower corridor 精确降为新的 source-specific 单门：

\[
\boxed{E_{{\rm src}}\mid\Omega_D,\qquad \Omega_D:=\Omega/\delta.}
\]

R15 的 132 个 master-integral rows 被全部重放。旧语言中 126 个由 \(g_1^*>P_1\) 杀死、6 个只由非整除杀死；R16 发现 **132/132 全部由更强的 complement size \(E_M>\Omega\) 杀死**。完整 U=1,...,9 chamber 的 163 个 master-integral rows 也全部满足 \(E_M>\Omega\)。

但 complement size **不是 universal theorem**。R16 的扩展 exact construct search 找到两个 genuine positive finite master-integral shapes 满足 \(E_M<\Omega\)。它们都先通过 \(D/h\mid\Omega\)，随后死在 \(E_{{\rm src}}\nmid\Omega_D\)：第一个同时缺 2/5-adic 一层，第二个只缺 5-adic 一层。仍然没有发现 corridor pass。

因此本轮不签 universal extinction，也不签 interface saturation。合法 terminal 是：

```text
R16_REDUCED_TO_SINGLE_MASTER_DIVISOR_GATE
```

当前 first failure 是 **post-D normalized source-excess divisibility**，不是 generic divisor spacing，更不是 q-successor。

## 2. Frozen R1–R15 State

R1–R15 全部冻结。R16 不重开 endpoint、DES、carrier image、generic PSDG、packet、generic divisor spacing、broad valuation，也不在 corridor pass 前启动 z/q。

R15 已冻结的 master/tail/Smith z-shell 只作为 downstream theorem 保存；本轮 0 个 shape 到达该层。

## 3. R15 Architecture Review

R15 的实际 first failure 是 master 强制出的 \(g_1^*\) 是否有资格作为 \(P_1\) 的 divisor。R16 的目标是把“资格”转成 \(N_M\) 中未被 \(P_1\) 吸收的 content 是否能进入 additive \(\Omega\)。

## 4. Definition of \(N_M\)

\[
\boxed{N_M=u_0AWXYGD.}
\]

master-integral branch 定义为

\[
\Omega>0,\qquad \Omega\mid N_M,
\]

并强制

\[
\boxed{g_1^*=N_M/\Omega.}
\]

## 5. Definition of \(E_M\)

令

\[
d_M=(N_M,P_1),\qquad
\boxed{E_M=N_M/d_M}.
\]

primewise：

\[
\boxed{v_p(E_M)=\max(v_p(N_M)-v_p(P_1),0).}
\]

## 6. Proof of \(g_1^*\mid P_1\iff E_M\mid\Omega\)

固定 prime \(p\)，令

\[
a=v_p(N_M),\quad b=v_p(P_1),\quad w=v_p(\Omega),\qquad 0\le w\le a.
\]

则

\[
g_1^*\mid P_1
\iff a-w\le b
\iff w\ge\max(a-b,0)
\iff v_p(\Omega)\ge v_p(E_M).
\]

对全部 prime 合并即得

\[
\boxed{g_1^*\mid P_1\iff E_M\mid\Omega.}
\]

## 7. Proof of the Lower/Upper Corridor Equivalence

\(g_0=(u_0AW,P_1)\) 且 \(u_0AW\mid N_M\)，故 \(g_0\mid N_M\)。于是

\[
g_0\mid\frac{{N_M}}{{\Omega}}
\iff g_0\Omega\mid N_M
\iff \Omega\mid\frac{{N_M}}{{g_0}}.
\]

所以

\[
\boxed{g_0\mid g_1^*\iff\Omega\mid N_M/g_0.}
\]

## 8. Exact Ω-Corridor Theorem

综合 §§6–7：

\[
\boxed{
g_0\mid g_1^*\mid P_1
\iff
E_M\mid\Omega\mid N_M/g_0.
}
\]

更进一步，因为 \(g_0\mid d_M\)，

\[
\boxed{E_M\mid N_M/g_0\ \text{自动成立}.}
\]

定义

\[
R_M:=\frac{{N_M}}{{g_0E_M}}=\frac{{d_M}}{{g_0}}\in\mathbf Z_{{>0}}.
\]

则完整 corridor 的单式为

\[
\boxed{
\frac{{\Omega}}{{E_M}}\in\operatorname{{Div}}\!\left(\frac{{(N_M,P_1)}}{{g_0}}\right).
}
\]

这里不调用任何 generic divisor-spacing theorem；右侧是 exact absorbed-content divisor set。

## 9. Primewise Excess Formula

对每个 prime，定义

\[
\Delta_p=v_p(N_M)-v_p(P_1).
\]

只有 \(\Delta_p>0\) 需要检查；local failure certificate 是

\[
\boxed{v_p(\Omega)<\Delta_p.}
\]

这给出 machine-checkable Type-P certificate。

## 10. Exact \(D/h\mid E_M\) Theorem — Strong Form

由

\[
D=KP_1-Q_0,\qquad h=(P_1,Q_0)
\]

立即得

\[
\boxed{(D,P_1)=h.}
\]

写

\[
P_1=hp,\qquad D=h\delta.
\]

则 \((p,\delta)=1\)。再令

\[
L=u_0AWXYG.
\]

因为 \(N_M=LD=Lh\delta\)，

\[
(N_M,P_1)=h(L,p).
\]

因此得到比“\(D/h\mid E_M\)”更强的 exact factorization：

\[
\boxed{
E_M=\delta\frac{{L}}{{(L,p)}}
=\frac{{D}}{{h}}\,E_{{\rm src}},
\qquad
E_{{\rm src}}:=\frac{{u_0AWXYG}}{{(u_0AWXYG,P_1/h)}}.
}
\]

## 11. \(D/h\mid\Omega\) Consequence

由上式和 \(E_M\mid\Omega\)，

\[
\boxed{D/h\mid\Omega.}
\]

但 R16 **没有**证明它 universal impossible；两个新的 non-size survivor 都通过这条门。

### 11.1 Exceptional branch \(D=h\)

该 branch **source-possible**，不能从代数上删除。R16 恢复了一个 exact tail-stage witness：

```text
U=1, C2=19, C3=7, b2=4, b3=6, z=2
A=2, W=3, c=1, X0=65, Y0=53
P1=6, Q0=59, P2=57, P3=14
D=h=1, T3=45, Omega=175, NM=600
TAIL=PASS, MASTER_INTEGRAL=NO (600 mod 175 = 75)
```

所以 \(D=h\) 不是 source-empty；但在 complete U1–U9 chamber 的 163 个 master-integral rows 中，\(D/h=1\) 的数量是 **0**。R16 没有把这条有限数据冒充 universal theorem。

## 12. \(\Omega\bmod D/h\) Audit

令 \(B=W+AYG\)、\(S=N_r+YM_r\)。由

\[
Q_0=h(Kp-\delta)
\]

及

\[
\Omega=Q_0B-AWS
\]

得到

\[
\boxed{
\Omega\equiv hKp(W+AYG)-AW(N_r+YM_r)\pmod\delta.
}
\]

因此 \(\delta\mid\Omega\) 的 source residue 是 explicit；未得到 universal \(0<|R_D|<\delta\) theorem。

## 13. Decimal Excess 2-adic Audit

定义

\[
e_2^{{\rm dec}}=\max(v_2(XYG)-v_2(P_1),0).
\]

则 \(2^{{e_2^{{\rm dec}}}}\mid E_M\)，故 corridor 必须满足 \(v_2(\Omega)\ge e_2^{{\rm dec}}\)。

该条件是 exact necessary channel，但不 universal。所有 \(v_2(\Omega),v_5(\Omega)\) 均在 **先精确计算完整差值 \(\Omega\)** 后再取 valuation；R16 从未用“两项 valuation 的最小值”代替差值，因此 equal-valuation cancellation 没有被 handwave。

## 14. Decimal Excess 5-adic Audit

同理

\[
e_5^{{\rm dec}}=\max(v_5(XYG)-v_5(P_1),0)
\]

且 \(v_5(\Omega)\ge e_5^{{\rm dec}}\) 是必要条件。

重要的是：第二个 non-size survivor 满足 raw \(e_5^{{\rm dec}}\) 门，却仍在 normalized \(E_{{\rm src}}\) 的 5-adic exponent 上失败。这证明 post-D source excess 严格强于 prompt 中单独的 raw decimal lower bound。

## 15. \(u_0AW\)-Excess Audit

\(u_0AW\) 的 prime content 不应与 \(XYG,D\) 人工分割；最安全的 exact object 是

\[
E_{{\rm src}}=L/(L,P_1/h).
\]

它自动处理 AW/decimal prime overlap。R16 因而不签独立 universal AW obstruction。

## 16. Master Size Obstruction

由 \(d_M\le P_1\)：

\[
g_1^*>P_1
\Longrightarrow
\frac{{N_M}}{{d_M}}>\frac{{N_M}}{{P_1}}>\Omega,
\]

即

\[
\boxed{g_1^*>P_1\Rightarrow E_M>\Omega.}
\]

converse **不成立**。R15 六个 exceptional rows 正是反例：\(g_1^*=180<P_1=334\)，但 \(E_M=299700>3330=\Omega\)。

更精确地，在 master-integral branch 上：

\[
\boxed{E_M>\Omega\iff g_1^*>(N_M,P_1).}
\]

这解释了 complement size 为什么比旧 \(g_1^*>P_1\) 更锐。

## 17. First-Bad-Prime Certificate Theory

定义

\[
p_{{\rm bad}}=\min\{{p:v_p(\Omega)<v_p(E_M)}\}.
\]

R15-132 的 canonical first-bad-prime counts 为：

```text
__PBAD132__
```

完整 U1–U9 master-163 为：

```text
__PBAD163__
```

完整 prime atlas 见 companion CSV。

结合 R14 已冻结的 fixed-core finite-fibre theorem，这同时给出 R16 的 **Master Corridor Finite Shape Certificate Theorem**：对 fixed positive core 的每个 legal finite shape，master-integral 后可用 Type S（\(E_M>\Omega\)）、Type P（单 prime exponent deficit）或 Type U（upper corridor）给出 exact finite certificate；若三类都不触发，才形成 corridor pass。

## 18. R15 132-Survivor Reclassification

exact replay：

```text
MASTER_INTEGRAL=132
OLD_G1STAR_GT_P1=126
OLD_G1STAR_LE_P1_BUT_NONDIVISOR=6
R16_EM_GT_OMEGA=132
R16_OMEGA_CORRIDOR_PASS=0
D_OVER_H_LOCAL_FAIL=__D_FAIL132__
RAW_DEC2_LOCAL_FAIL=__DEC2_132__
RAW_DEC5_LOCAL_FAIL=__DEC5_132__
```

所以 R16 把旧 126+6 两类统一成 132/132 Type-S complement-size certificates。

## 19. Six Exceptional Rows Exact Autopsy

六行共享 geometry：

\[
(P_1,Q_0,D,\Omega,N_M,g_1^*)=(334,343,2997,3330,599400,180).
\]

并有

\[
h=1,\quad g_0=2,\quad (N_M,P_1)=2,
\]

\[
\boxed{E_M=299700=90\Omega.}
\]

factorization：

\[
N_M=2^3\,3^4\,5^2\,37,
\]

\[
P_1=2\cdot167,
\]

\[
E_M=2^2\,3^4\,5^2\,37,
\qquad
\Omega=2\,3^2\,5\,37.
\]

所以 canonical first bad prime 为 \(2\)。同时更 source-native 的 \(D/h\) channel 已经失败：

\[
D/h=2997=3^4\cdot37,
\qquad v_3(\Omega)=2<4.
\]

这六行的共同机制不是偶然 nondivisor，而是 **\((N_M,P_1)=2\) 极小，导致几乎全部 master multiplicative content 留在 complement 中**。

## 20. Complete \(U\le9\) Ω-Corridor Certification

1191 个 positive cores 完整重放；master-integral rows 为 163，且：

```text
MASTER_INTEGRAL_SHAPES=163
FAIL_EM_GT_OMEGA=163
OMEGA_CORRIDOR_PASS=0
D_OVER_H_LOCAL_FAIL=__D_FAIL163__
RAW_DEC2_LOCAL_FAIL=__DEC2_163__
RAW_DEC5_LOCAL_FAIL=__DEC5_163__
```

因此 R15 的 U1–U9 exact emptiness 被 R16 corridor language 完整 reproduce；没有任何旧 failure 丢失。

## 21. Dominant Bad-Prime Analysis

bounded master rows 的 first bad prime 以 2、3、5 为主，但并不只来自 decimal source；\(D/h\) 的 3-adic content 是大量失败的重要来源。精确计数见 `105_R16_Master_Complement_Prime_Atlas.csv`。

## 22. Infinite-Family Theorem Attempt

未证明一个 actual infinite positive source family universally corridor-empty，因此：

```text
INFINITE_POSITIVE_SHAPE_CORRIDOR_EXTINCTION=NO
```

但在特殊 alignment locus

\[
\Omega=DYG
\]

上，master 强制简化为

\[
g_1^*=u_0AWX.
\]

又因 \(\Omega_D=hYG\)，lower corridor 精确等价于

\[
\boxed{
u_0AWX\mid h\,(u_0AWXYG,P_1/h).
}
\]

R16 的两个 non-size survivors 都落在此 locus，并分别失败。当前没有证明该 locus 本身形成 infinite legal source family，所以不越权签 infinite-family theorem。

## 23. \(E_M=1\) Construct Route

在所有 exact completed/search master-integral shapes 中没有 \(E_M=1\) hit。未证明 universal \(E_M>1\)。

## 24. \(E_M=\Omega\) Construct Route

注意：\(E_M=\Omega\) 意味着 \(m_\Omega=1\)。因为 \(1\mid R_M\)，这将自动成为完整 corridor pass。R16 搜索未找到任何此类 shape。

## 25. Small \(\Omega/E_M\) Construction

完整 corridor 精确要求

\[
m_\Omega=\Omega/E_M\in\operatorname{{Div}}(R_M).
\]

R16 主动检查了 small-ratio regime。两个真正突破 complement-size 的 shapes 分别有

\[
m_\Omega=197/10,
\qquad
m_\Omega=26/5,
\]

均非整数，所以还没资格进入 finite divisor set。

## 26. First Corridor Pass — Search Result

R16 exact construct campaign 包括原 R15 canonical search 的 replay、扩大矩形、以及集中到 \(n_2=3,n_3=2,g=k=1\) 的 focused chart。各批 exact counts 保存于 `105_R16_Corridor_Construct_Search.csv`。

结果：

```text
OMEGA_CORRIDOR_PASS_FOUND=NO
```

但发现两个 genuine non-size survivors，证明 size obstruction 不 universal。

### NS1

\[
(C_2,C_3,A,W)=(289,59,9,8),
\]

\[
(P_1,Q_0,D,h)=(14184,14381,127459,197),
\]

\[
(E_M,\Omega)=(6470000,127459000).
\]

这里 \(D/h=647\mid\Omega\)，但

\[
E_{{\rm src}}=10000\nmid \Omega_D=197000.
\]

local deficits：\(v_2:4>3\)、\(v_5:4>3\)。

### NS2

\[
(C_2,C_3,A,W)=(388,31,3,5),
\]

\[
(P_1,Q_0,D,h)=(780,2093,5707,13),
\]

\[
(E_M,\Omega)=(1097500,5707000).
\]

这里 \(D/h=439\mid\Omega\)，但

\[
E_{{\rm src}}=2500\nmid\Omega_D=13000,
\]

且唯一 local deficit 是 \(v_5:4>3\)。

## 27. R15 z-Shell Reactivation

没有 corridor pass，因此按照 R16 firewall：

```text
R15_Z_SHELL_REACTIVATED=NO
```

## 28. First z-Selector Pass

未激活；不计算 \(\Lambda,F,Q_-,Q_+\)。

## 29. Full Source Reconstruction

未激活。

## 30. Exact U Recovery

未激活。

## 31. Downstream Word/Cut Audit

未激活。

## 32. Interface Saturation Audit

不签 saturation。原因是 R16 已经找到突破 complement-size 的真实 finite shapes，而且它们在 \(D/h\) 之后暴露出一个更窄的 source-specific quotient gate：

\[
\boxed{
E_{{\rm src}}=\frac{{u_0AWXYG}}{{(u_0AWXYG,P_1/h)}}
\mid
\Omega_D=\frac{{\Omega}}{{D/h}}.
}
\]

这个 gate 同时耦合 AW、decimal scales、reduced \(P_1/h\) 和 additive \(\Omega_D\)；它没有退化成 arbitrary divisor problem。

## 33. Information-Gain Certificate

```text
OLD_GATE=E_M|Omega|NM/g0 (proposed R16 corridor)
EXACT_CORRIDOR_EQUIVALENCE=PROVED
AUTOMATIC_EM_DIVIDES_NM_OVER_G0=PROVED
FULL_CORRIDOR_SINGLE_MEMBERSHIP=Omega/EM in Div(gcd(NM,P1)/g0)
D_OVER_H_EXACT_FACTOR=PROVED
EXACT_COMPLEMENT_FACTORIZATION=EM=(D/h)*E_SRC
POST_D_NORMALIZED_GATE=E_SRC|Omega_D
R15_132_COMPLEMENT_SIZE_RECLASSIFICATION=132/132
R15_SIX_EXCEPTIONAL_UNIFIED_BY_COMPLEMENT_SIZE=YES
COMPLEMENT_SIZE_UNIVERSAL=DISPROVED_BY_2_EXACT_SHAPES
FIRST_NON_SIZE_SHAPES=2
FIRST_NON_SIZE_SHAPES_D_OVER_H_PASS=2/2
FIRST_NON_SIZE_SHAPES_POST_D_GATE_PASS=0/2
CORRIDOR_PASS_FOUND=NO
NEW_GATE_SOURCE_SPECIFIC=YES
USES_POSITIVE_RADIAL_CORE_INFORMATION=YES_FOR_CERTIFICATION_AND_CONSTRUCT_SEARCH;NO_FOR_PURE_ALGEBRA_THEOREMS
```

## 34. R16 Terminal Verdict

```text
R16_TERMINAL_VERDICT=R16_REDUCED_TO_SINGLE_MASTER_DIVISOR_GATE

R1_TO_R15_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=POST_D_REDUCED_SOURCE_EXCESS_DIVISIBILITY

NM=u0*A*W*X*Y*G*D
OMEGA=W*(Q0-P3)-A*Y*(P2-G*Q0)=Q0*(W+A*Y*G)-A*W*(Nr+Y*Mr)
G0=gcd(u0*A*W,P1)
G1_STAR=NM/OMEGA
P1=c*(X0-Y0)/2

EM=NM/gcd(NM,P1)
EM_DEFINITION_VALID=YES

G1_DIVIDES_P1_EQUIV_EM_DIVIDES_OMEGA=YES
G0_DIVIDES_G1_EQUIV_OMEGA_DIVIDES_NM_OVER_G0=YES

OMEGA_CORRIDOR_EQUIVALENCE_PROVED=YES

D_GCD_P1=h
D_OVER_H=delta_D
D_OVER_H_DIVIDES_EM=YES
D_OVER_H_DIVIDES_OMEGA_REQUIRED=YES

DECIMAL_EXCESS_2=max(v2(XYG)-v2(P1),0)
DECIMAL_EXCESS_5=max(v5(XYG)-v5(P1),0)
VP2_OMEGA=SHAPE_DEPENDENT_EXACT
VP5_OMEGA=SHAPE_DEPENDENT_EXACT

MASTER_SIZE_OBSTRUCTION=PROVED_AS_NECESSARY_KILLER__NOT_UNIVERSAL
MASTER_D_OVER_H_OBSTRUCTION=NECESSARY_CHANNEL_PROVED__NOT_UNIVERSAL
MASTER_DECIMAL_EXCESS_OBSTRUCTION=NECESSARY_LOCAL_CHANNEL_PROVED__NOT_UNIVERSAL
MASTER_AW_EXCESS_OBSTRUCTION=ABSORBED_IN_EXACT_E_SRC__NO_UNIVERSAL_SEPARATE_THEOREM

R15_132_RECLASSIFIED=YES
R15_126_SIZE_FAILURES_REPRODUCED=126/126__AND_STRENGTHENED_TO_132/132_EM_GT_OMEGA
R15_6_EXCEPTIONAL_FAILURES_EXPLAINED=YES

R15_6_COMMON_BAD_PRIME=2
R15_6_COMMON_BAD_MECHANISM=GCD_NM_P1_EQUALS_2_CAUSING_EM_EQUALS_90*OMEGA;_ALSO_D_OVER_H_HAS_3^4_WHILE_OMEGA_HAS_3^2

FIRST_BAD_PRIME_ATLAS=105_R16_Master_Complement_Prime_Atlas.csv

U1_TO_9_OMEGA_CORRIDOR_CERTIFICATION=1191_CORES_EXACT;_163_MASTER_INTEGRAL;_0_CORRIDOR_PASS

INFINITE_POSITIVE_SHAPE_CORRIDOR_EXTINCTION=NO
INFINITE_FAMILY_DESCRIPTION=NO_ACTUAL_INFINITE_FAMILY_THEOREM;_CONDITIONAL_OMEGA_EQUALS_DYG_LOCUS_REDUCED_EXACTLY

OMEGA_CORRIDOR_PASS_FOUND=NO
CORRIDOR_PASS_SHAPE=NONE
CORRIDOR_PASS_RADIAL_CORE=NONE

G1_CORRIDOR_PASS=NO

LAMBDA=NOT_ACTIVATED
FORBIDDEN_FACTOR=NOT_ACTIVATED
Q_LOWER=NOT_ACTIVATED
Q_UPPER=NOT_ACTIVATED
Q_SUCCESSOR_PASS=NOT_ACTIVATED

Z_SELECTOR_PASS=NO_NOT_ACTIVATED
Z=NONE

FULL_POST_PSDG_LIFT=NO
FULL_LIFT_DATA=NONE

PLAIN_U=NOT_ACTIVATED
SOURCE_SELECTOR_PASS=NOT_ACTIVATED
SOURCE_INTEGER_U_FOUND=NO

COMMON_U_INTEGER_SUCCESSOR_GATE=NOT_ACTIVATED

DIGIT_SYNCHRONIZATION=NOT_ACTIVATED
ACTUAL_CUT=NOT_ACTIVATED
FULL_WORD=NOT_ACTIVATED
OUTER_COMPLETION=NOT_ACTIVATED

MASTER_COMPLEMENT_DIVISOR_OBSTRUCTION_PROVED=NO

POSITIVE_RADIAL_CORE_UNLIFTABILITY_PROVED=NO
POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NO_GLOBAL_THEOREM

MASTER_COMPLEMENT_DIVISOR_INTERFACE_SATURATED=NO

NEW_FIRST_FAILURE_GATE=E_SRC_DIVIDES_OMEGA_D_ON_DELTA_D_PASSING_POSITIVE_FINITE_SHAPES

R16_INFORMATION_GAIN_CERTIFICATE=PASS__EXACT_DUALITY_PLUS_EM_FACTOR_SPLIT_PLUS_AUTOMATIC_RM_PLUS_132_RECLASSIFICATION_PLUS_2_NON_SIZE_SURVIVORS

R17_AUTHORIZED=YES
R17_ARCHITECTURE=POST_D_NORMALIZED_SOURCE_EXCESS_ONLY__NO_GENERIC_DIVISOR_SPACING__NO_Q_SUCCESSOR
R17_SINGLE_ATTACK_TARGET=DECIDE_E_SRC_DIVIDES_OMEGA_D_ON_DELTA_D_PASSING_POSITIVE_LEGAL_FINITE_SHAPES;_FIRST_PASS_MUST_IMMEDIATELY_CHECK_mOmega_DIVIDES_RM_AND_THEN_REACTIVATE_R15_Z_SHELL
```

## 35. R17 Authorization Decision

R16 属于 Route D：没有 universal extinction，没有 corridor pass，但留下了一个真正新的 source-specific quotient gate，而不是把 \(E_M\mid\Omega\) 原样换名。

R17 只允许攻击：

\[
\boxed{
\frac{{u_0AWXYG}}{{(u_0AWXYG,P_1/h)}}
\mid
\frac{{\Omega}}{{D/h}}
}
\]

**且仅在 \(D/h\mid\Omega\) 的 branch 上。** 一旦命中，必须立即验证

\[
\Omega/E_M\mid (N_M,P_1)/g_0
\]

从而确认完整 corridor；只有这时才重新激活 R15 的 z/\(\Lambda\)/F/q machinery。

---

## Artifact Index

- `105_R16_Omega_Corridor_Registry.csv`
- `105_R16_Master_Complement_Prime_Atlas.csv`
- `105_R16_R15_132_Reclassification.csv`
- `105_R16_R15_Six_Exceptional_Autopsy.csv`
- `105_R16_D_Over_H_Audit.csv`
- `105_R16_Decimal_Excess_Audit.csv`
- `105_R16_U1_U9_Corridor_Certification.csv`
- `105_R16_Corridor_Construct_Search.csv`
- `105_R16_First_Failure_Registry.csv`
- `105_R16_execution.log`
- `105_R16_SHA256_Manifest.csv`
- `105_R16_scripts/105_R16_master_complement.py`

All divisibility, gcd, valuation, CF, master-integrality, and corridor decisions in the generated registries use exact integer arithmetic. No floating-point value is used as a theorem/certificate predicate.
'''
    report=(report
        .replace('__PBAD132__',str(dict(sorted(pbad132.items()))))
        .replace('__PBAD163__',str(dict(sorted(pbad163.items()))))
        .replace('__D_FAIL132__',str(d_fail132))
        .replace('__DEC2_132__',str(dec2_132))
        .replace('__DEC5_132__',str(dec5_132))
        .replace('__D_FAIL163__',str(d_fail163))
        .replace('__DEC2_163__',str(dec2_163))
        .replace('__DEC5_163__',str(dec5_163))
        .replace('{{','{').replace('}}','}'))
    report_path=ROOT/'105_R16_Master_Complement_Divisor_Omega_Corridor.md'
    report_path.write_text(report,encoding='utf-8')

    # Execution log.
    with (ROOT/'105_R16_execution.log').open('w',encoding='utf-8') as f:
        f.write('105-R16 exact master-complement execution\n')
        f.write(f'U1_U9_CORES={len(core_registry)}\n')
        f.write(f'U1_U9_MASTER_INTEGRAL={len(masters19)}\n')
        f.write(f'U1_U9_CORRIDOR_PASS={sum(r["OMEGA_CORRIDOR_PASS"] for r in masters19)}\n')
        f.write(f'U1_U9_EM_GT_OMEGA={sum(r["EM_GT_OMEGA"] for r in masters19)}\n')
        f.write(f'R15_132={len(m132)} OLD_SIZE_126={len(old_size)} OLD_SIX={len(old_six)} NEW_EM_GT={sum(r["EM_GT_OMEGA"] for r in m132)}\n')
        f.write(f'R15_132_FIRST_BAD={dict(sorted(pbad132.items()))}\n')
        f.write(f'U1_U9_FIRST_BAD={dict(sorted(pbad163.items()))}\n')
        f.write(f'D_EQUALS_H_MASTER_INTEGRAL_U1_U9={d_eq_h_master}\n')
        f.write('R16_CONSTRUCT_NON_SIZE=2\nR16_CONSTRUCT_CORRIDOR_PASS=0\n')
        f.write('NS1=EM<OMEGA; D/h PASS; E_SRC=10000 !| OMEGA_D=197000; bad p=2,5\n')
        f.write('NS2=EM<OMEGA; D/h PASS; E_SRC=2500 !| OMEGA_D=13000; bad p=5\n')
        f.write('ALL_ASSERTIONS=PASS\n')

    # Manifest last (excluding itself, then append self hash is impossible without recursion).
    files=[
        report_path,
        ROOT/'105_R16_Omega_Corridor_Registry.csv',ROOT/'105_R16_Master_Complement_Prime_Atlas.csv',
        ROOT/'105_R16_R15_132_Reclassification.csv',ROOT/'105_R16_R15_Six_Exceptional_Autopsy.csv',
        ROOT/'105_R16_D_Over_H_Audit.csv',ROOT/'105_R16_Decimal_Excess_Audit.csv',
        ROOT/'105_R16_U1_U9_Corridor_Certification.csv',ROOT/'105_R16_Corridor_Construct_Search.csv',
        ROOT/'105_R16_First_Failure_Registry.csv',ROOT/'105_R16_execution.log',Path(__file__),
    ]
    manifest=[]
    for pth in files:
        manifest.append({'FILE':str(pth.relative_to(ROOT)),'BYTES':pth.stat().st_size,'SHA256':sha256(pth)})
    write_csv(ROOT/'105_R16_SHA256_Manifest.csv',manifest,['FILE','BYTES','SHA256'])

    print('R16 exact archive: PASS')
    print('U1-U9 cores:',len(core_registry),'master:',len(masters19),'corridor pass:',sum(r['OMEGA_CORRIDOR_PASS'] for r in masters19))
    print('R15 132 complement-size deaths:',sum(r['EM_GT_OMEGA'] for r in m132))
    print('Construct non-size survivors:',[(r['C2'],r['C3'],r['EM'],r['Omega'],r['FIRST_BAD_PRIME']) for r in construct_rows])


if __name__=='__main__':
    main()
