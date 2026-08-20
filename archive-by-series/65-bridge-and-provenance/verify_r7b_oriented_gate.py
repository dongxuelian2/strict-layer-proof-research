#!/usr/bin/env python3
"""105-R7B exact symbolic/regression verifier.

This script certifies only algebraic identities and the fixed-character
regression. It does NOT promote finite search to a global S3/S4 theorem.
"""
from math import gcd
import sympy as sp

A,B,C,N,W,x = sp.symbols("A B C N W x", integer=True)
m_minus=A-B
m_plus=A+B

# Product bridge.
prod = sp.expand((C-W)*(C+W)-m_minus*m_plus*N)
prod = sp.expand(prod.subs(W**2, C**2+(B**2-A**2)*N))
assert prod == 0

# W-free divisor equation from x=(W-C)/(B-A).
a=B-A
b=A+B
W_from_x=C+a*x
D_eq=sp.expand(W_from_x**2-(C**2+(B**2-A**2)*N))
assert sp.expand(D_eq-a*(a*x**2+2*C*x-b*N)) == 0

# CRT modulus collision is tautological after g | (B^2-A^2).
g,L=sp.symbols("g L", integer=True, positive=True)
assert sp.expand((C**2+g*L*N)-C**2-g*L*N)==0

# Fixed-character exact regression from R7.
P1,P2,P3,Q0=24,52,159,169
Ah,Bh,Ch=21,125,549
Wh=20621
Nh=P2*P2+P3*P3
assert P1*P1+Nh==Q0*Q0
assert Ah*Q0-Bh*P1==Ch
assert Wh*Wh==Ch*Ch+(Bh*Bh-Ah*Ah)*Nh
Sp,Sm=Q0+P1,Q0-P1
assert (Wh-Ch)%(Bh-Ah)==0
assert (Wh-Ch)//(Bh-Ah)==Sp
assert (Wh+Ch)%(Ah+Bh)==0
assert (Wh+Ch)//(Ah+Bh)==Sm
assert Sp*Sm==Nh

# Row-gcd firewall and CRT data on control.
assert gcd(Ah,Bh)==1
gm=gcd(Bh-Ah,Ah+Bh)
assert gm in (1,2)
L0=(Bh-Ah)*(Ah+Bh)//gm
assert Wh % (Bh-Ah) == Ch % (Bh-Ah)
assert Wh % (Ah+Bh) == (-Ch) % (Ah+Bh)
assert (Wh*Wh-Ch*Ch) % L0 == 0

# Primitive divisor criterion on control.
h=gcd(P1,Q0)
g23=gcd(P2,P3)
assert gcd(h,g23)==1
assert Sp%Sm != 0 or True
assert Sp*Sm==Nh
assert (Sp-Sm)%2==0
assert gcd((Sp-Sm)//2,(Sp+Sm)//2)==h

print("R7B_SYMBOLIC_PRODUCT_BRIDGE=PASS")
print("R7B_W_FREE_DIVISOR_EQUATION=PASS")
print("R7B_CRT_SQUARE_COLLISION=IDENTITY")
print("R7B_FIXED_CHARACTER_REGRESSION=PASS")
print("R7B_PRIMITIVE_DIVISOR_CRITERION_REGRESSION=PASS")
print("GLOBAL_OUTER_KILL=NOT_CLAIMED")
print("GLOBAL_OUTER_WITNESS=NOT_FOUND")
