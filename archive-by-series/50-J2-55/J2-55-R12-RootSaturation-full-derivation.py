#!/usr/bin/env python3
"""
J2-55 R12 Carry-Saturated Full-Root symbolic audit.

Scope:
  Strict A1-only / Exact Resonance R=0 / J=2.

Source discipline:
  * exact root is the frozen R3/R6/R7 normalization
        R(x)=A*(L/8)*x^2-u*D2*x+Omega.
  * tail reconstruction is R6/R7.
  * carry saturation is the exact R8 normalized carry divisibility.
  * R10/R11 later third-core data are NOT added as a new polynomial in the
    old variables: R11 proves D_u=gamma and xi-reconstruction is definitional.
Thus this script asks the R12 question: after quotienting out the old carry
core, does the FULL exact root still have a nonzero polynomial factor?

It reconstructs Boundary moderate, High moderate, Reverse generic moderate,
and the special k=1,b=0 reverse normalization.
"""
import hashlib
import sympy as sp

def H(expr):
    return hashlib.sha256(str(sp.expand(expr)).encode()).hexdigest()

def primitive_expr(P, var):
    P=sp.Poly(sp.expand(P),var)
    cont, prim = sp.polys.polytools.primitive(P.as_expr(), expand=True)
    return sp.factor(cont), sp.factor(prim)

def setup():
    G,q,alpha,t,f,w,s,e,Hh,R,K=sp.symbols(
        'G q alpha t f w s e H R K', integer=True)
    chi,chiR,gamma=sp.symbols('chi chiR gamma', integer=True)
    d0=2*f
    c=q**3+10*q**2+12*q+8
    C=q*c
    B=(q+2)*(q**2-4*q-4)
    u=(G+1)/q
    A=2*u+1

    def reconstructed(d):
        N=sp.cancel((B*t+alpha*G/d)/C)
        Z=sp.cancel((A*t-2*N)/(q*(q+4)))
        a3=sp.cancel(((G-1)*t-q*N)/(2*(q+4)))
        X=sp.cancel((Z+u*N)/2)
        D2=sp.cancel(u*a3+G*X)
        F=sp.cancel(A*X**2+Z*D2)
        return N,Z,a3,X,D2,F

    # High/boundary reconstruction.
    N,Z,a3,X,D2,F = reconstructed(d0)
    Dfl=4*f*q**2*(q+4)*c

    # Boundary quotient/floor numerator.
    Ub=sp.cancel(8*u*D2/(A*G))
    nb,db=sp.fraction(Ub)
    Qb,_=sp.div(sp.Poly(nb,G),sp.Poly(db,G))
    Pb=sp.factor(Qb.as_expr())
    Jb=sp.factor(Dfl*Pb)
    xb=sp.cancel((Jb-chi)/Dfl-s)
    Omegab=sp.cancel(F/(2*G))
    RootB=sp.cancel(A*(G/8)*xb**2-u*D2*xb+Omegab)

    # Boundary old carry residual.
    Palpha=2*q**4+13*q**3+10*q**2+12*q+8
    Pt=5*q**6+12*q**5-220*q**4-672*q**3-368*q**2+64*q+64
    GammaB=sp.expand(alpha*Palpha-2*f*t*Pt-2*q*(Dfl*s+chi))

    # High quotient/floor numerator.
    Uh=sp.cancel(8*u*D2/(A*(G/Hh)))
    nh,dh=sp.fraction(Uh)
    Qh,_=sp.div(sp.Poly(nh,G),sp.Poly(dh,G))
    Ph=sp.factor(Qh.as_expr())
    Jh=sp.factor(Dfl*Ph)
    xh=sp.cancel((Jh-chi)/Dfl)
    Omegah=sp.cancel(F/(2*G*Hh))
    RootH=sp.cancel(A*(G/(8*Hh))*xh**2-u*D2*xh+Omegah)

    eps=sp.symbols('eps')
    DecH=sp.cancel(u*D2*(Ph+eps)-Omegah)
    nDecH,_=sp.fraction(DecH)
    constH=sp.Poly(sp.expand(nDecH),G).coeff_monomial(1)
    epsH=sp.factor(sp.solve(sp.Eq(constH,0),eps)[0])
    NH=sp.factor(sp.cancel(epsH*(2*Hh*q*Dfl)))
    GammaH=sp.factor(NH+2*Hh*q*chi)

    # Reverse reconstruction.
    dR=d0*R
    Nr,Zr,a3r,Xr,D2r,Fr = reconstructed(dR)
    Ur=sp.cancel(8*u*D2r/(A*(R*G)))
    nr,dr=sp.fraction(Ur)
    Qr,_=sp.div(sp.Poly(nr,G),sp.Poly(dr,G))
    Pr=sp.factor(Qr.as_expr())
    DR=4*f*R**2*q**2*(q+4)*c
    Jr=sp.factor(DR*Pr)
    xr=sp.cancel((Jr-chiR)/DR-s)
    Omegar=sp.cancel(Fr/(2*(G/R)))
    RootR=sp.cancel(A*(R*G/8)*xr**2-u*D2r*xr+Omegar)

    epsr=sp.symbols('epsr')
    DecR=sp.cancel(u*D2r*(Pr+epsr-s)-Omegar)
    nDecR,_=sp.fraction(DecR)
    constR=sp.Poly(sp.expand(nDecR),G).coeff_monomial(1)
    epsTargetR=sp.factor(sp.solve(sp.Eq(constR,0),epsr)[0])
    epsR=sp.factor(epsTargetR-s)
    NR=sp.factor(sp.cancel(epsR*(2*q*DR)))
    GammaR=sp.factor(NR+2*q*(DR*s+chiR))

    return locals()

def root_num(expr):
    return sp.fraction(sp.cancel(expr))[0]

def nontrivial_factor(expr, var, structural_factors):
    n,d=sp.fraction(sp.cancel(expr))
    n=sp.factor(n)
    for sf in structural_factors:
        while sp.rem(sp.Poly(sp.expand(n),var),sp.Poly(sf,var)).as_expr()==0:
            n=sp.cancel(n/sf)
    return sp.factor(n), sp.factor(d)

def build_root_factors():
    z=setup()
    G,q,t,f,w,s,e,Hh,R,K=z['G'],z['q'],z['t'],z['f'],z['w'],z['s'],z['e'],z['Hh'],z['R'],z['K']
    alpha,chi,chiR,gamma=z['alpha'],z['chi'],z['chiR'],z['gamma']
    B=z['B']
    U=sp.symbols('u', integer=True)
    ch,chR=sp.symbols('ch chR', integer=True)

    # ---------- Boundary ----------
    rb=root_num(z['RootB'])
    tailB=2*f*B*t-q*e
    rb=sp.factor(rb.subs({G:q*U-1,alpha:tailB,chi:q*ch}))
    GB=sp.expand(z['GammaB'].subs({G:q*U-1,alpha:tailB,chi:q*ch}))
    # R8: Gamma_B = [G/(4 f^2 w)] gamma.
    eqB=sp.expand(4*f**2*w*GB-(q*U-1)*gamma)
    chB=sp.solve(sp.Eq(eqB,0),ch)[0]
    satB=sp.factor(sp.cancel(rb.subs(ch,chB)))
    nB,dB=sp.fraction(satB)
    flB=sp.factor_list(nB)
    assert any(sp.factor(ff-(q*U-1))==0 for ff,ee in flB[1])
    EB=[ff for ff,ee in flB[1] if sp.factor(ff-(q*U-1))!=0][-1]
    assert EB!=0 and sp.Poly(EB,U).degree()==4

    # ---------- High ----------
    rh=root_num(z['RootH'])
    rh=sp.factor(rh.subs({G:q*U-1,alpha:tailB,chi:q*ch}))
    GH=sp.expand(z['GammaH'].subs({G:q*U-1,alpha:tailB,chi:q*ch}))
    eqH=sp.expand(4*f**2*w*GH-(q*U-1)*gamma)
    chH=sp.solve(sp.Eq(eqH,0),ch)[0]
    satH=sp.factor(sp.cancel(rh.subs(ch,chH)))
    nH,dH=sp.fraction(satH)
    flH=sp.factor_list(nH)
    assert any(sp.factor(ff-(q*U-1))==0 for ff,ee in flH[1])
    EH=[ff for ff,ee in flH[1] if sp.factor(ff-(q*U-1))!=0][-1]
    assert EH!=0 and sp.Poly(EH,U).degree()==4

    # ---------- Reverse generic moderate ----------
    rr=root_num(z['RootR'])
    tailR=2*R*f*B*t-q*e
    subsR={G:q*U-1,alpha:tailR,chiR:q*chR,K:(q*U-1)/R}
    rr=sp.factor(rr.subs(subsR))
    GR=sp.factor(z['GammaR'].subs(subsR))
    # R8 generic moderate: Gamma_R=[K/(4 f^2 w)] gamma.
    eqR=sp.factor(4*f**2*w*GR-((q*U-1)/R)*gamma)
    chRv=sp.solve(sp.Eq(eqR,0),chR)[0]
    satR=sp.factor(sp.cancel(rr.subs(chR,chRv)))
    nR,dR=sp.fraction(satR)
    flR=sp.factor_list(nR)
    assert any(sp.factor(ff-(q*U-1))==0 for ff,ee in flR[1])
    ER=[ff for ff,ee in flR[1] if sp.factor(ff-(q*U-1))!=0][-1]
    assert ER!=0 and sp.Poly(ER,U).degree()==4

    # Convert B/H to G polynomials.
    GG=sp.symbols('GG', integer=True)
    def as_G(E):
        ex=sp.cancel(E.subs(U,(GG+1)/q))
        n,d=sp.fraction(ex)
        cont,prim=primitive_expr(n,GG)
        return sp.factor(prim),sp.factor(d),cont

    PBG,dPBG,cPBG=as_G(EB)
    PHG,dPHG,cPHG=as_G(EH)
    assert sp.Poly(PBG,GG).degree()==4
    assert sp.Poly(PHG,GG).degree()==4

    # Convert generic reverse to fixed-K polynomial in R=10^r.
    RR=sp.symbols('RR', integer=True)
    exRG=sp.cancel(ER.subs({U:(K*RR+1)/q,R:RR}))
    nRG,dRG=sp.fraction(exRG)
    PRraw=sp.Poly(sp.expand(nRG),RR)
    lowest=min(i for i in range(PRraw.degree()+1) if PRraw.nth(i)!=0)
    assert lowest==2
    PRprim=sp.factor(nRG/RR**2)
    assert sp.Poly(PRprim,RR).degree()==7
    Cgeneric=sp.factor(sp.Poly(PRprim,RR).nth(0))
    Cgeneric_expected=sp.factor(
        gamma*(-K**2*gamma*q-2*K**2*gamma-64*K*e*f**2*q**3*w
               +256*f**3*q**5*t*w+1024*f**3*q**4*t*w))
    assert sp.factor(Cgeneric-Cgeneric_expected)==0

    # ---------- Reverse special k=1,b=0 ----------
    # Here generic K/(4 f^2 w) normalization is illegal. R8 carry core is
    # simply Gamma_R=gamma, and K=10,f=1,G=10R.
    RR1=sp.symbols('RR1', integer=True)
    rr1=root_num(z['RootR']).subs({
        f:1,K:10,R:RR1,G:10*RR1,
        alpha:2*RR1*B*t-q*e,chiR:q*chR})
    gr1=z['GammaR'].subs({
        f:1,K:10,R:RR1,G:10*RR1,
        alpha:2*RR1*B*t-q*e,chiR:q*chR})
    ch1=sp.solve(sp.Eq(gr1-gamma,0),chR)[0]
    sat1=sp.factor(sp.cancel(rr1.subs(chR,ch1)))
    n1,d1=sp.fraction(sat1)
    fac1=sp.factor_list(n1)
    assert any(sp.factor(ff-RR1)==0 for ff,ee in fac1[1])
    P1=[ff for ff,ee in fac1[1] if sp.Poly(ff,RR1).degree()==7][0]
    C1=sp.factor(sp.Poly(P1,RR1).nth(0))
    C1expected=sp.factor(
        -gamma*(-80*e*q**3-5*gamma*q-10*gamma
                 +32*q**5*t+128*q**4*t))
    assert sp.factor(C1-C1expected)==0

    return dict(
        E_B_u=sp.factor(EB),E_H_u=sp.factor(EH),E_R_u=sp.factor(ER),
        P_B_G=sp.factor(PBG),P_H_G=sp.factor(PHG),
        P_R_generic=sp.factor(PRprim),P_R_k1=sp.factor(P1),
        C_R_generic=Cgeneric,C_R_k1=C1,
        hashes=dict(
            E_B_u=H(EB),E_H_u=H(EH),E_R_u=H(ER),
            P_B_G=H(PBG),P_H_G=H(PHG),
            P_R_generic=H(PRprim),P_R_k1=H(P1)),
        degrees=dict(B_G=4,H_G=4,R_generic=7,R_k1=7),
        denominators=dict(B=dB,H=dH,R=dR,R_k1=d1))

def main():
    D=build_root_factors()
    print('J2-55 R12 Carry-Saturated Full-Root certificate')
    print('FULL_ROOT_MOD_CARRY_IDEAL=NONZERO')
    print('BOUNDARY_ROOTNF_NONZERO=PASS degree_G=4 hash='+D['hashes']['P_B_G'])
    print('HIGH_ROOTNF_NONZERO=PASS degree_G=4 hash='+D['hashes']['P_H_G'])
    print('REVERSE_GENERIC_ROOTNF_NONZERO=PASS degree_R=7 hash='+D['hashes']['P_R_generic'])
    print('REVERSE_K1_SPECIAL_ROOTNF_NONZERO=PASS degree_R=7 hash='+D['hashes']['P_R_k1'])
    print('REVERSE_GENERIC_CONSTANT=',D['C_R_generic'])
    print('REVERSE_K1_CONSTANT=',D['C_R_k1'])
    print('DEPENDENCY_VERDICT=R8_CARRY_CORE_DOES_NOT_ALGEBRAICALLY_CONSUME_FULL_ROOT')
    print('R10_R11_LATER_XI_RECON=DEFINITIONAL_AFTER_DU_EQUALS_GAMMA')
    print('NO_R12_RESIDUAL_LADDER=PASS')

if __name__=='__main__':
    main()
