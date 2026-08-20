#!/usr/bin/env python3
from J2_65_R3_common import *
import hashlib

assert QDEN == d**2*q**5*(q+4)**2*c**2
P=sp.Poly(QNUM,G,K)
support=sorted([m for m,co in P.terms() if co!=0], key=lambda z:(z[1],z[0]))
assert support==EXPECTED_GK
assert sp.Poly(QNUM,x).degree()==2
C=grouped_coeffs()
assert sp.factor(C[(5,0)]-2*alpha**2*(q+4)**2)==0
assert sp.factor(C[(4,1)]+4*alpha*d*q**2*x*(q+4)**2*c)==0
assert sp.factor(C[(5,0)]+C[(4,1)]-2*alpha*(q+4)**2*(alpha-2*d*q**2*c*x))==0

rows=[]
for exps,coef in full_terms():
    rows.append(dict(G_exp=exps[0],K_exp=exps[1],q_exp=exps[2],d_exp=exps[3],
                     alpha_exp=exps[4],t_exp=exps[5],x_exp=exps[6],
                     integer_coefficient=coef,sign=('+' if coef>0 else '-')))
write_tsv(OUT/'J2-65-R3-AugmentedSupport.tsv',rows,list(rows[0]))

# q=1 specialization audit
Q1=sp.expand(QNUM.subs(q,1))
q1terms=len(sp.Poly(Q1,G,K,d,alpha,t,x).terms())
q1support=sorted([m for m,co in sp.Poly(Q1,G,K).terms() if co!=0],key=lambda z:(z[1],z[0]))
assert q1support==EXPECTED_GK

h=hashlib.sha256(sp.sstr(QNUM).encode()).hexdigest()
print('R2_LEVEL1_MASTER_HASH_RECOMPUTED='+h)
print('R2_SUPPORT_REGRESSION=PASS')
print('AUGMENTED_SUPPORT_SIZE='+str(len(rows)))
print('Q1_AUGMENTED_SUPPORT_SIZE='+str(q1terms))
Q10=sp.expand(Q1.subs(alpha,0))
q10terms=len(sp.Poly(Q10,G,K,d,t,x).terms())
q10support=sorted([m for m,co in sp.Poly(Q10,G,K).terms() if co!=0],key=lambda z:(z[1],z[0]))
assert q10support==[(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1)]
print('Q1_GK_SUPPORT_UNCHANGED=PASS')
print('Q1_ALPHA0_AUGMENTED_SUPPORT_SIZE='+str(q10terms))
print('Q1_ALPHA0_GK_SUPPORT_SIZE='+str(len(q10support)))
