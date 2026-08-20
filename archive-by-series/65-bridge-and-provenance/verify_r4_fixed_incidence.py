#!/usr/bin/env python3
from sympy import symbols, Rational, simplify, factor, Matrix

G,K,X,Y = symbols("G K X Y", nonzero=True)

# 1. Fixed primitive sphere point.
p1,p2,p3 = Rational(2,7),Rational(3,7),Rational(6,7)
sphere = simplify(p1**2+p2**2+p3**2-1)
assert sphere == 0

# 2. Explicit ambient section of the normalized master.
# Master:
# b1*X*Y*G*(K*p1-1)+b2*Y*(p2-G)-b3*(1-p3)=0
b1=b2=1
b3 = X*Y*G*(2*K-7) + Y*(3-7*G)
master = simplify(
    b1*X*Y*G*(K*p1-1)
    + b2*Y*(p2-G)
    - b3*(1-p3)
)
assert master == 0

# 3. Outer exponent map:
# (g,k,d,n3) -> (g,k,m2=g+d,n3)
M = Matrix([
    [1,0,0,0],
    [0,1,0,0],
    [1,0,1,0],
    [0,0,0,1],
])
det = M.det()
assert det == 1

# 4. Partial fixed-incidence polynomial is nonzero.
Fpre = (G-1)*(X-G)*(X-10*G)
assert factor(Fpre) != 0
assert simplify(Fpre.subs({G:2,X:3})) != 0

print("SPHERE_SECTION=PASS")
print("AMBIENT_MASTER_SECTION=PASS")
print("OUTER_EXPONENT_LATTICE_DET=", det)
print("PARTIAL_FIXED_INCIDENCE_PROPERNESS_WITNESS=PASS")
print("AMBIENT_SECTION_B3=", factor(b3))
