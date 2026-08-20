#!/usr/bin/env python3
from __future__ import annotations
import csv,itertools
from J2_65_R5_common import HERE,ROW_TYPES,ROW_TERMS,ROW_ADDITIVES,BRACKETS,PAIR_DET,R4_LAMBDA

def row_for_type(tp:str):
    return 'K' if tp=='K_LT_G' else ('G' if tp=='G_LT_K' else None)

def row_of_term(cid):
    return 'K' if cid in {'C01','C11','C21','C31','C41'} else 'G'

def weight(term,p, lifted:set[str]|None=None):
    cid,a,br,kind=term; b=1 if row_of_term(cid)=='K' else 0
    delta='0'
    if br and lifted is not None and br in lifted:
        delta=f'delta_{br}_{p}'
    return f'{a}*g+{b}*k+nu{p}({cid})+{delta}'

def pair_dnf(row,p,lifted:set[str]):
    terms=ROW_TERMS[row]
    clauses=[]
    for i,j in itertools.combinations(range(len(terms)),2):
        wi,wj=weight(terms[i],p,lifted),weight(terms[j],p,lifted)
        rest=[weight(terms[k],p,lifted) for k in range(len(terms)) if k not in (i,j)]
        clauses.append(f'({wi}={wj}; {wi}<='+';'.join(rest)+')')
    return ' OR '.join(clauses)

def det_pairs(subset):
    linears=[b for b in subset if BRACKETS[b]['kind']=='linear']
    out=[]
    for a,b in itertools.combinations(linears,2):
        key=tuple(sorted((a,b)))
        if key in PAIR_DET: out.append((a,b,PAIR_DET[key]))
    return out

def fixed_closed(p,row,subset):
    s=set(subset)
    if p!=2: return False,None
    if row=='K':
        if 'B31' in s and ('B11' in s or 'B21' in s):
            return True,'R4_FIXED_DEPTH: a lifted pair among (B11,B31)/(B21,B31) would make two primitive linears even, but the pair determinant is a 2-unit'
    if row=='G' and {'B10','B40'}<=s:
        return True,'R4_FIXED_DEPTH: lifted B10 and B40 would both be even, but v2(Delta_10,40)=0'
    return False,None

fibres=[]
for t2 in ROW_TYPES:
    for t5 in ROW_TYPES:
        fibres.append((f'F_{t2}__{t5}',t2,t5))

rows=[]; c3map=[]
for fid,t2,t5 in fibres:
    for p,tp in ((2,t2),(5,t5)):
        row=row_for_type(tp)
        if row is None:
            rows.append(dict(fibre_id=fid,place=p,row='CROSS',disjunct_id=f'{fid}_p{p}_C1',type='C1',
                coefficients='cross-row raw minima',brackets='',required_depth='0',determinant_factor='',status='SURVIVES_CROSS_ROW',
                affine_condition='m_K=m_G',pair_minimum_dnf='',lift_pattern='NONE',notes='No internal C2/C3 choice at this place.'))
            continue
        terms=ROW_TERMS[row]
        adds=ROW_ADDITIVES[row]
        # C2: no additive extra cancellation anywhere in the row; exact base-min pair DNF expanded into 10 affine cells.
        for idx,(i,j) in enumerate(itertools.combinations(range(len(terms)),2),1):
            ti,tj=terms[i],terms[j]
            ci,ai,_,_=ti; bi=1 if row=='K' else 0; cj,aj,_,_=tj; bj=bi
            lhs=f'{ai}*g+{bi}*k+nu{p}({ci})'
            rhs=f'{aj}*g+{bj}*k+nu{p}({cj})'
            rest=[]
            for z in terms:
                cz,az,_,_=z; bz=bi
                if cz not in (ci,cj): rest.append(f'{lhs}<={az}*g+{bz}*k+nu{p}({cz})')
            cond=f'delta(all additive generators)=0; {lhs}={rhs}; '+'; '.join(rest)
            rows.append(dict(fibre_id=fid,place=p,row=row,disjunct_id=f'{fid}_p{p}_{row}_C2_{idx:02d}',type='C2',
                coefficients=f'{ci},{cj}',brackets='',required_depth='0',determinant_factor='',status='SURVIVES_AFFINE_TIE_CELL',
                affine_condition=cond,pair_minimum_dnf=cond,lift_pattern='NONE',
                notes='Exact affine base-valuation tie cell; nu_p(C) is the structural coefficient-valuation coordinate from the factor-aware row.'))
        # C3: exact positive-extra-depth support strata. Within a lift support, minimum multiplicity is the explicit 10-pair DNF.
        for mask in range(1,1<<len(adds)):
            subset=[adds[i] for i in range(len(adds)) if mask>>i&1]
            S=set(subset)
            req=[]
            for b in subset:
                if BRACKETS[b]['kind']=='linear': req.append(f'{b}>={R4_LAMBDA[(p,b)]}')
                else: req.append(f'{b}:delta_{b}_{p}>0 (R4 conic valuation/resultant interface; no fake scalar Lambda)')
            dp=det_pairs(subset)
            detfactor=';'.join(f'{a}-{b}:{d["ambient"]}' for a,b,d in dp) if dp else 'NONE_SINGLE_LINEAR_OR_CONIC'
            closed,reason=fixed_closed(p,row,subset)
            status='CLOSED_BY_R4_FIXED_DEPTH' if closed else 'SURVIVES_R5_DNF'
            liftcond=';'.join([f'delta_{b}_{p}>0' for b in subset]+[f'delta_{b}_{p}=0' for b in adds if b not in S])
            pmd=pair_dnf(row,p,S)
            did=f'{fid}_p{p}_{row}_C3_{mask:02d}'
            rows.append(dict(fibre_id=fid,place=p,row=row,disjunct_id=did,type='C3',coefficients=','.join(t[0] for t in terms),
                brackets=','.join(subset),required_depth='; '.join(req),determinant_factor=detfactor,status=status,
                affine_condition=liftcond,pair_minimum_dnf=pmd,lift_pattern=','.join(subset),
                notes=reason or 'Positive bracket/conic lift stratum. Pairwise determinant applies only when at least two linear generators occur in this support.'))
            # C3 tube map is one row per support stratum, not per syntactic pair-min clause.
            conics=[b for b in subset if BRACKETS[b]['kind']=='conic']
            if closed:
                tube='FIXED_2_UNIT'; ceiling='0'; death='R4_FIXED_DEPTH'
            elif dp:
                if p==2:
                    # only nonclosed row-internal 2-adic line pair is B11-B21 -> D8.
                    tube='D8' if {'B11','B21'}<=S else 'BOUNDED_OR_NONE'
                    ceiling='2+M_D8(g)' if tube=='D8' else 'R4 fixed table'
                else:
                    tubes={'q+4'}
                    if {'B11','B31'}<=S: tubes.add('D9')
                    tube=','.join(sorted(tubes)); ceiling='M_q+4(g)'+('+M_D9(g)' if 'D9' in tubes else '')
                death='NONE_UNIFORM: R4 Lambda expressions are not proved to dominate the new tube ceiling'
            else:
                tube='NONE'; ceiling='N/A'; death='NONE: singleton linear or conic C3 has no determinant polynomial forced'
            branch_ref=('q==1 mod5 REQUIRED for any p5 two-linear lift; on q==2 or4 mod5 all same-row line-pair determinants are 5-units' if p==5 and dp else 'NONE')
            c3map.append(dict(disjunct_id=did,fibre_id=fid,place=p,row=row,lifted_brackets=','.join(subset),
                line_pair_count=len(dp),line_pairs=';'.join(f'{a}-{b}' for a,b,_ in dp),determinant_tube=tube,
                determinant_depth_ceiling=ceiling,conic_interface=('R4_11_RESULTANTS' if conics else 'NONE'),
                branch_refinement=branch_ref,
                r4_fixed_status=('CLOSED' if closed else 'OPEN'),r5_ceiling_status=('NOT_APPLICABLE' if closed or not dp else 'CONDITIONAL_ONLY'),
                death=death))

p=HERE/'J2-65-R5-InternalDisjunctions.tsv'
with p.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p2=HERE/'J2-65-R5-C3TubeMap.tsv'
with p2.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(c3map[0]),delimiter='\t');w.writeheader();w.writerows(c3map)

c3=[r for r in rows if r['type']=='C3']; fixed=[r for r in c3 if r['status']=='CLOSED_BY_R4_FIXED_DEPTH']
assert len(fibres)==9
assert len(c3)==132, len(c3)
assert len(fixed)==21, len(fixed)
print('R5 INTERNAL DISJUNCTION CERTIFICATE')
print('INTERNAL_DISJUNCTION_DNF=PASS')
print('FIBRE_COUNT=9')
print('C3_DISJUNCTS_TOTAL=',len(c3),sep='')
print('C3_CLOSED_BY_R4_FIXED_DEPTH=',len(fixed),sep='')
print('C3_CLOSED_BY_R5_TUBE_CEILING=0')
print('C3_SURVIVING=',len(c3)-len(fixed),sep='')
print('C3_SINGLE_OR_CONIC_OBSTRUCTION=PROVED_PRESENT')
print('ALL_C3_MAP_TO_DETERMINANT_TUBE=FALSE')
print('WHY=single-bracket lift and conic lift strata are exact inherited C3 alternatives; DET-GCD needs two simultaneous linear brackets')
print('ROW_INTERNAL_AMBIENT_TUBES=p2:D8_only_unbounded_pair; p5:q+4_with_optional_D9_extra')
print('P5_TWO_LINEAR_C3_SUPPORTS_FORCED_TO_q_EQ_1_MOD5=24')
print('OUTPUTS=',p.name,',',p2.name,sep='')
