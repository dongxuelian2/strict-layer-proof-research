from fractions import Fraction
from math import gcd, ceil
from itertools import product


def rad(n):
    r=1
    p=2
    x=n
    while p*p<=x:
        if x%p==0:
            r*=p
            while x%p==0: x//=p
        p+=1
    if x>1: r*=x
    return r


def mobius_squarefree(d):
    # called only on divisors of a radical
    if d==1: return 1
    k=0
    p=2
    x=d
    while p*p<=x:
        if x%p==0:
            k+=1; x//=p
            if x%p==0: return 0
        p+=1
    if x>1: k+=1
    return -1 if k%2 else 1


def divisors(n):
    out=[]
    for d in range(1,n+1):
        if n%d==0: out.append(d)
    return out


def coprime_count(V,L,R):
    rv=rad(V)
    return sum(mobius_squarefree(d)*(ceil(R/d)-ceil(L/d)) for d in divisors(rv))


def brute_coprime_count(V,L,R):
    lo=ceil(L)
    # n<R, so n <= ceil(R)-1
    hi=ceil(R)-1
    return sum(1 for n in range(max(1,lo),hi+1) if gcd(n,V)==1)


def check_rnf(C2,C3,n2,n3):
    tau=Fraction(10**n3,C3)
    rho=Fraction(C2*10**n3,C3*10**n2)
    L=max(Fraction(10**(n2-1),C2), Fraction(10**(n3-1),C3))
    R=min(Fraction(10**n2,C2), Fraction(10**n3,C3))
    Lj=tau*max(Fraction(1,10), Fraction(1,10)/rho)
    Rj=tau*min(Fraction(1,1), Fraction(1,1)/rho)
    assert L==Lj and R==Rj
    if Fraction(1,10)<rho<10:
        assert L<R
    else:
        assert L>=R
    return rho,tau,L,R


def b3_divisor_subsumption_regression(bound=7):
    # p=2 or 5 exponent audit. a=vp(s), b=vp(beta), c=vp(v), m=m3.
    for a,b,c,m in product(range(bound), repeat=4):
        if m==0: continue
        lhs=max(a+b+c-m,0)  # vp(B3^sharp)
        beta_sharp=max(b-m,0)
        lambda_exp=max(m-b,0)
        v_sharp=max(c-lambda_exp,0)
        rhs=a+beta_sharp+v_sharp
        assert lhs<=rhs, (a,b,c,m,lhs,rhs)


def duality_regression(limit=80):
    for V in range(1,limit+1):
        ds=[d for d in divisors(V)]
        for gi in ds:
            for gj in ds:
                bi,bj=V//gi,V//gj
                l=gi*gj//gcd(gi,gj)
                assert gcd(bi,bj)*l==V


def known_state_census():
    # fixed profile (b1,b2,b3)=(1,6,8), V=24, g2=4,g3=3, n2=2,n3=1
    states={
        'A':(24,52,159,169),
        'B':(48,436,75,445),
        'C':(456,292,2907,2957),
    }
    rows=[]
    for name,(P1,P2,P3,Q0) in states.items():
        assert P1*P1+P2*P2+P3*P3==Q0*Q0
        C2,C3=P2//4,P3//3
        rho,tau,L,R=check_rnf(C2,C3,2,1)
        if L>=R: layer='C'
        elif R<=1: layer='I'
        else:
            N=coprime_count(24,L,R)
            layer='P-survive' if N else 'P-dead'
        rows.append((name,C2,C3,rho,tau,L,R,layer))
    return rows


def synchronized_family(t):
    X=3_553_056*t*t+160_341*t+1_809
    Y=44_000_352*t*t+2_018_892*t+23_153
    Z=188_129_520*t*t+8_492_928*t+95_849
    Q=597_312_720*t*t+27_003_264*t+305_197
    d=gcd(gcd(X,Y),gcd(Z,Q))
    x,y,z,q=X//d,Y//d,Z//d,Q//d
    P1,P2,P3=24*x,4*y,3*z
    assert P1*P1+P2*P2+P3*P3==q*q
    assert z>y
    rho,tau,L,R=check_rnf(y,z,2,1)
    assert rho<Fraction(1,10) and L>=R
    return (t,y,z,rho)


def exact_count_regression():
    for V in range(1,35):
        for a in range(1,12):
            for b in range(a+1,a+8):
                # nonintegral endpoints too
                L=Fraction(2*a+1,2)
                R=Fraction(3*b+1,3)
                if L<R:
                    assert coprime_count(V,L,R)==brute_coprime_count(V,L,R)


def main():
    b3_divisor_subsumption_regression()
    duality_regression()
    exact_count_regression()
    rows=known_state_census()
    fam=[synchronized_family(t) for t in range(6)]
    print('B3 residual divisor subsumption: PASS')
    print('Smith/GCD duality regression: PASS')
    print('Exact coprime-count endpoint convention: PASS')
    print('Known synchronized state radial census:')
    for row in rows:
        print(row)
    print('g=0 infinite-family first six members: all continuous-dead, rho<0.1')
    for row in fam:
        print(row)

if __name__=='__main__':
    main()
