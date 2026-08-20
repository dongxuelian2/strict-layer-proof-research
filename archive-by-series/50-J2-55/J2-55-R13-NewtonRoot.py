#!/usr/bin/env python3
"""Generic lowest-coefficient and p-adic Newton-minimum checker."""
from math import inf

def vp(n,p):
    if n==0:return inf
    n=abs(int(n));v=0
    while n%p==0:v+=1;n//=p
    return v

def lowest_nonzero(coeffs):
    for j,c in enumerate(coeffs):
        if c:return j,c
    return None,None

def root_necessary(coeffs,m):
    j,c=lowest_nonzero(coeffs)
    if j is None:return {'identically_zero':True}
    T=10**m
    return {'jstar':j,'lowest_coeff':c,'T_divides_lowest':c%T==0}

def newton_unique_min(coeffs,m,p):
    vals=[vp(c,p)+j*m if c else inf for j,c in enumerate(coeffs)]
    mn=min(vals); idx=[j for j,v in enumerate(vals) if v==mn]
    return {'p':p,'valuations':vals,'minimum':mn,'min_indices':idx,'kill':len(idx)==1}

if __name__=='__main__':
    print('LCR-1: P(10^m)=0 => 10^m divides the lowest nonzero coefficient')
    print('NEWT-1: a unique p-adic minimum among v_p(Cj)+jm forbids P(10^m)=0')
