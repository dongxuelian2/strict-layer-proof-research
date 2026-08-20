# A1 J2 CZDR Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** J2 \(C_3\)-\(z\) Discriminant-Root × Near-Square Factor Allocation × Cyclotomic Outer-\(g\) Closure  
**Status date:** 2026-08-16  
**Main inherited source:** `A1_J2_NRSEC_Report.md`  
**Computation:** `A1_J2_CZDR_search.py`  
**Certificate:** `A1_J2_CZDR_certificate.txt`

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

and, more specifically,

\[
\boxed{
g\ge4,\quad u>1
\quad\textbf{is not fully extinct.}
}
\]

Therefore this round does **not** issue a J2 Resonance Closure Certificate.

However, the old frontier

\[
(g,u,k,c,z)
\]

has been materially reduced.  The round attains **Success C** in a stronger-than-minimal form.

The new results are:

1. the square-discriminant/root-divisibility gate is replaced exactly by a root-factor system
   \[
   C_1\lambda=F,\qquad
   AH^2C_1+\lambda=2uKd_2;
   \]

2. every root survivor has a large forced decimal core
   \[
   \boxed{
   2^{\min(k+1,\,2g-2)}
   5^{\min(k,\,2g)}
   \mid \lambda,\ F;
   }
   \]

3. the prompt's nominal chamber \(5\mid A\) is not live:
   \[
   \boxed{\gcd(A,10)=1}
   \]
   was already forced by the inherited J2 equations, hence
   \[
   \boxed{\gcd(A,H)=1;}
   \]

4. the cyclotomic relation \(uq=G+1\) yields a new exact signed coordinate
   \[
   \boxed{
   j:=q(G-1)z-2Ac=\frac{2X-z}{u},
   }
   \]
   which linearizes \(c,h,m,X\);

5. after multiplying by the actual common radial scale \(U\), the terminal chart becomes a new **radial cyclotomic Euclidean chart**
   in the two integer variables
   \[
   \boxed{N:=Uj,\qquad t:=q^2Z-4a_3,\qquad Z:=Uz,}
   \]
   with
   \[
   \boxed{
   \begin{aligned}
   2Aa_3&=q(G-1)Z-N,\\
   (G-1)t&=2(q+4)a_3+qN,\\
   q(q+4)Z&=At-2N.
   \end{aligned}}
   \tag{RCE}
   \]

6. in the entire \(S_R>0\) branch the radial signed index collapses to
   \[
   q=1:\quad -N\in\{1,3,5\},
   \]
   and
   \[
   q>1:\quad
   \boxed{U=1,\ j=-1,\ N=-1.}
   \]
   The extreme \(q=1\) branch is then killed uniformly.

7. every surviving positive branch must satisfy
   \[
   \boxed{
   7\le q<6G^{1/3}.
   }
   \]
   For each such outer divisor \(q\), the whole old \((c,z,U)\) fibre contains **at most one**
   cyclotomic candidate \(t\) before the root gate.

8. in the negative branch,
   \[
   \boxed{k=2g+1\Longrightarrow\varnothing}
   \]
   uniformly.

9. in the negative boundary layer \(k=2g\),
   \[
   q=1\Longrightarrow\varnothing
   \]
   uniformly; for any remaining survivor,
   \[
   \boxed{
   7\le q<6G^{1/3},
   \qquad
   N\in\{1,3,5\}.
   }
   \]
   For fixed \(q\), there are at most \(9\) cyclotomic \((N,t)\) cells before the root gate.

Hence the strongest new global compression is

\[
\boxed{
\begin{array}{ll}
S_R>0:&
q=1\text{ dead};\quad
q>1\Rightarrow
7\le q<6G^{1/3},\
N=-1,\
\#t\le1;
\\[1mm]
S_R<0,\ k=2g+1:&
\varnothing;
\\[1mm]
S_R<0,\ k=2g:&
q=1\text{ dead};\quad
q>1\Rightarrow
7\le q<6G^{1/3},\
N\in\{1,3,5\},\
\#t\le9.
\end{array}}
\tag{EXEC}
\]

The still-open portion is therefore concentrated in

\[
\boxed{
S_R<0,\quad
1\le k\le2g-1
}
\]

together with the already strongly compressed positive cyclotomic/root cells.

This is a genuine reduction of the old \(C_3\)-\(z\) frontier: on the full positive branch \(c,z,U\) are no longer free search coordinates at all.

---

# Part II — Frozen \(C_3\)-\(z\) Ledger

## 2.1 Frozen outer notation

\[
G=10^g,\qquad
H=\frac G2,\qquad
K=10^k,
\]

\[
u\mid G+1,\qquad
q=\frac{G+1}{u},\qquad
uq=G+1,
\]

\[
A=2u+1,\qquad
B=2G+q.
\]

The inherited determinant identities are

\[
\boxed{qA-B=2,}
\tag{DET2}
\]

\[
\boxed{uB-GA=1.}
\tag{DET1}
\]

Also

\[
u,q\ \text{are odd ten-units},\qquad
\gcd(u,H)=1.
\]

## 2.2 The \(5\mid A\) audit

The previous J2 normal form contains

\[
GKC_1=AC_2+m,
\]

with \(C_2,m\) ten-units.  The left side is divisible by \(5\).  If \(5\mid A\), then the right side is congruent to \(m\not\equiv0\pmod5\), contradiction.

Since \(A=2u+1\) is odd,

\[
\boxed{\gcd(A,10)=1.}
\tag{A10}
\]

Therefore the prompt's requested split is resolved as

\[
\boxed{5\mid A\Longrightarrow\varnothing,}
\]

and throughout every admissible J2 cell,

\[
\boxed{\gcd(A,H)=1.}
\tag{AH}
\]

This is important: \(A,u,H\) are pairwise coprime.

## 2.3 Frozen \(C_3\)-\(z\) chart

Write

\[
c:=C_3.
\]

Every remaining J2 state has a positive ten-unit \(z\) with

\[
\boxed{
h=qHz-Ac,
}
\tag{CZ1}
\]

\[
\boxed{
m=Ah-Gz,
}
\tag{CZ2}
\]

\[
\boxed{
r=Hh-uc,
}
\tag{CZ3}
\]

\[
\boxed{
X=GHz-uAc,
}
\tag{CZ4}
\]

\[
\boxed{
d_2=uc+GX.
}
\tag{CZ5}
\]

The sign is

\[
\boxed{
X>0\iff S_R<0,
\qquad
X<0\iff S_R>0.
}
\]

The frozen positivity conditions include

\[
h,m,r,d_2>0,\qquad X\ne0,
\]

and \(h,m,r,|X|,d_2,z,c\) are ten-units where inherited.

The primitive coordinates are

\[
P_1=GHC_1,\qquad
P_2=uGC_2,\qquad
P_3=uc,
\]

\[
Q_0=P_2+d_2.
\]

The actual common radial scale satisfies

\[
a_i=UC_i,\qquad
V=uGH,\qquad
\gcd(U,V)=1.
\]

Hence \(U\) is a ten-unit.

The exact third and second numerator windows used in this round are

\[
\boxed{
\frac{G}{10}\le Uc<G,
}
\tag{DIG3}
\]

\[
\boxed{
\frac{G^2K}{10}\le UC_2<G^2K.
}
\tag{DIG2}
\]

The inherited positive-branch RRGS estimate is

\[
\boxed{0<U|X|<u\qquad(S_R>0).}
\tag{RRGS+}
\]

For the negative branch, with

\[
\eta:=2.532\sqrt{\frac{101}{96}}<\frac{1299}{500}=2.598,
\]

the inherited bounds are

\[
\boxed{
U X<\eta\,\frac{uG^2}{K}
\qquad(S_R<0),
}
\tag{UW-}
\]

\[
\boxed{
Uz<
\frac{2\eta u}{K}
+\frac{2uA}{G}.
}
\tag{UZ-}
\]

For \(S_R>0\),

\[
\boxed{
Uz<\frac{2uA}{G}.
}
\tag{UZ+}
\]

The frozen sign/face exponent bands are

\[
S_R<0:\qquad1\le k\le2g+1,
\]

\[
S_R>0:\qquad2g-1\le k\le3g-1.
\]

Finally, the inherited low-depth and \(u=1\) closures are

\[
\boxed{
g=2\Longrightarrow\varnothing,
\qquad
g=3\Longrightarrow\varnothing,
}
\]

and

\[
\boxed{
u=1\Longrightarrow\varnothing.
}
\]

Therefore this round only concerns

\[
g\ge4,\qquad u>1.
\]

---

# Part III — Near-Square Factorization

The frozen quadratic is

\[
\boxed{
AH^2C_1^2-2uKd_2C_1+AX^2+zd_2=0.
}
\tag{Q}
\]

Define

\[
Y:=uKd_2,
\qquad
F:=AX^2+zd_2.
\]

Then

\[
AH^2C_1^2-2YC_1+F=0.
\]

The reduced discriminant is

\[
\Delta_0=Y^2-AH^2F.
\]

A root survivor must have

\[
\Delta_0=R_0^2,
\]

and

\[
AH^2\mid Y\pm R_0.
\]

Set

\[
L:=Y-R_0,\qquad M:=Y+R_0.
\]

Then

\[
\boxed{
LM=AH^2F,
}
\tag{NF1}
\]

\[
L+M=2Y.
\]

The integral root condition says that one of \(L,M\) equals \(AH^2C_1\).  The other factor is therefore

\[
\frac{F}{C_1}.
\]

This motivates the exact root-factor quotient

\[
\boxed{
\lambda:=\frac{F}{C_1}.
}
\]

Then every integral root satisfies

\[
\boxed{
C_1\lambda=F,
}
\tag{LR2}
\]

\[
\boxed{
AH^2C_1+\lambda=2Y=2uKd_2.
}
\tag{LR1}
\]

Conversely, positive integers \((C_1,\lambda)\) satisfying LR1–LR2 automatically give

\[
\Delta_0
=
\left(
\frac{AH^2C_1-\lambda}{2}
\right)^2.
\]

Thus, at the exact integer level,

\[
\boxed{
\text{square discriminant + root divisibility}
\Longleftrightarrow
\text{positive factor system LR1--LR2}.
}
\tag{RF-EQ}
\]

This is the preferred language for the rest of the report.

It exposes two facts that the bare discriminant hides:

* \(C_1\mid F\);
* the complementary root factor \(\lambda\) is arithmetically constrained by the common decimal powers in \(2uKd_2\) and \(AH^2C_1\).

---

# Part IV — Root-Factor Arithmetic

## 4.1 Decimal-core divisor theorem

Because \(u,d_2,A\) are ten-units,

\[
v_2(2uKd_2)=k+1,
\qquad
v_5(2uKd_2)=k.
\]

Also

\[
H^2=2^{2g-2}5^{2g},
\]

and \(A\) is a ten-unit.

From

\[
\lambda
=
2uKd_2-AH^2C_1,
\]

both summands are divisible by

\[
\boxed{
D_{g,k}
:=
2^{\min(k+1,\,2g-2)}
5^{\min(k,\,2g)}.
}
\]

Hence

\[
\boxed{
D_{g,k}\mid\lambda.
}
\tag{DCF1}
\]

Since \(F=C_1\lambda\),

\[
\boxed{
D_{g,k}\mid F.
}
\tag{DCF2}
\]

This is the main new root-factor allocation theorem.

Important specializations are

\[
k\ge2g
\Longrightarrow
\boxed{H^2\mid\lambda,\ F,}
\tag{DCF-H2}
\]

and

\[
k=2g-1
\Longrightarrow
\boxed{\frac{H^2}{5}\mid\lambda,\ F.}
\tag{DCF-H25}
\]

Therefore the positive branch, whose frozen range starts at \(k=2g-1\), always satisfies

\[
\boxed{\frac{H^2}{5}\mid F.}
\tag{POS-DCF}
\]

This already falsifies the tempting conjecture that a near-survivor should have \(\lambda=1\):

\[
\boxed{
S_R>0\Longrightarrow
\lambda\ge H^2/5.
}
\]

So the correct "small factor" is not a constant-size factor.  The useful statement is that it contains a **forced decimal core**.

## 4.2 Two root residues

The fourth Euclidean identity inherited from the previous round is

\[
2KC_1=Bz+A\ell.
\]

Since \(B=qA-2\),

\[
2KC_1\equiv-2z\pmod A.
\]

As \(A\) is odd,

\[
\boxed{
KC_1\equiv-z\pmod A.
}
\tag{RA}
\]

A second residue comes directly from the quadratic modulo \(u\).

Because

\[
G\equiv-1\pmod u,
\qquad
2H=G,
\]

we have

\[
H\equiv-\frac12\pmod u.
\]

From CZ4 and CZ5,

\[
X\equiv\frac z2\pmod u,
\qquad
d_2\equiv-\frac z2\pmod u,
\]

and \(A\equiv1\pmod u\).

Reducing Q modulo \(u\) gives

\[
\frac{C_1^2-z^2}{4}\equiv0\pmod u.
\]

Thus

\[
\boxed{
C_1^2\equiv z^2\pmod u.
}
\tag{RU}
\]

Primitive gcd gives \(\gcd(C_1,u)=1\): if a prime divided both \(C_1\) and \(u\), it would divide \(P_1,P_2,P_3\), hence \(Q_0\), contradicting primitiveness.

Therefore RU forces

\[
\boxed{\gcd(z,u)=1.}
\tag{ZU}
\]

Moreover,

\[
F
\equiv
-\frac{z^2}{4}
\pmod u,
\]

so

\[
\boxed{\gcd(F,u)=1.}
\tag{FU}
\]

Since \(F=C_1\lambda\),

\[
\boxed{\gcd(\lambda,u)=1.}
\tag{LU}
\]

This is a genuine prime-allocation statement for the complementary root factor: the large decimal core \(D_{g,k}\) lies in \(\lambda\), while no prime of \(u\) may lie in \(\lambda\).

## 4.3 Radialized root-factor system

The preceding factor system becomes cleaner after multiplying by the actual scale.

Define

\[
a_1:=UC_1,\qquad
Z:=Uz,\qquad
\mathcal X:=UX,\qquad
D_2:=Ud_2,
\]

and

\[
\widetilde F
:=
U^2F
=
A\mathcal X^2+ZD_2.
\]

Then the quadratic is

\[
\boxed{
AH^2a_1^2
-
2uKD_2a_1
+
\widetilde F
=0.
}
\tag{RQ}
\]

Define

\[
\Lambda:=U\lambda.
\]

Because \(U\) is a ten-unit, the decimal-core theorem is unchanged:

\[
\boxed{
D_{g,k}\mid\Lambda,\ \widetilde F.
}
\tag{RDCF}
\]

The exact factor system is

\[
\boxed{
a_1\Lambda=\widetilde F,
}
\tag{RLR2}
\]

\[
\boxed{
AH^2a_1+\Lambda=2uKD_2.
}
\tag{RLR1}
\]

The root residues become

\[
\boxed{
a_1^2\equiv Z^2\pmod u,
}
\tag{RRU}
\]

\[
\boxed{
Ka_1\equiv-Z\pmod A.
}
\tag{RRA}
\]

This radialization is useful because the common scale \(U\) disappears from the quadratic itself.

---

# Part V — Cyclotomic Outer-\(g\) Splice

## 5.1 The signed cyclotomic coordinate \(j\)

Use

\[
uq=G+1
\]

inside CZ4:

\[
2X-z
=
(G^2-1)z-2uAc
=
u\bigl(q(G-1)z-2Ac\bigr).
\]

Define

\[
\boxed{
j:=q(G-1)z-2Ac.
}
\tag{JDEF}
\]

Then

\[
\boxed{
2X-z=uj,
}
\tag{J1}
\]

hence

\[
\boxed{
X=\frac{z+uj}{2}.
}
\tag{JX}
\]

Solving for \(c\),

\[
\boxed{
c=\frac{q(G-1)z-j}{2A}.
}
\tag{JC}
\]

Substitution into CZ1–CZ2 gives

\[
\boxed{
h=\frac{j+qz}{2},
}
\tag{JH}
\]

\[
\boxed{
m=\frac{Aj+(q+2)z}{2}.
}
\tag{JM}
\]

Also

\[
\boxed{
d_2
=
\frac{
u(AG-1)j+[G(G+A)-1]z
}{2A}.
}
\tag{JD}
\]

Since \(q,G-1,z\) are odd and \(2Ac\) is even,

\[
\boxed{j\ \text{is odd}.}
\]

This is the first cyclotomic compression.

## 5.2 Actual radial variables \(N,Z,a_3\)

Set

\[
\boxed{
N:=Uj,
\qquad
Z:=Uz,
\qquad
a_3:=Uc.
}
\]

Since \(U\) is a ten-unit, \(N\) is odd.

Multiplying JC by \(U\),

\[
\boxed{
2Aa_3=q(G-1)Z-N.
}
\tag{RCE1}
\]

Now define the second Euclidean remainder

\[
\boxed{
t:=q^2Z-4a_3.
}
\tag{TDEF}
\]

Multiply RCE1 by \(q\).  Since

\[
2Aq
=
4(G-1)+2(q+4),
\]

one gets

\[
\boxed{
(G-1)t
=
2(q+4)a_3+qN.
}
\tag{RCE2}
\]

Eliminating \(a_3\) gives

\[
\boxed{
q(q+4)Z
=
At-2N.
}
\tag{RCE3}
\]

Hence

\[
\boxed{
a_3
=
\frac{(G-1)t-qN}{2(q+4)},
}
\tag{RA3}
\]

\[
\boxed{
Z
=
\frac{At-2N}{q(q+4)}.
}
\tag{RZ}
\]

Finally,

\[
\boxed{
\mathcal X=UX=\frac{Z+uN}{2},
}
\tag{RX}
\]

and

\[
\boxed{
D_2=u a_3+G\mathcal X.
}
\tag{RD2}
\]

Thus, before solving the root quadratic, the old actual variables \((U,c,z)\) are replaced by \((N,t)\), with \(a_3,Z,\mathcal X,D_2\) deterministic.

This is the second and more important cyclotomic compression.

---

# Part VI — \((2/5)\)-Valuation of Root Factors

This round does not return to the old primitive phase campaign.  The only valuations used are the valuations of the root factors.

## 6.1 General root-factor valuation floor

From DCF1,

\[
v_2(\lambda)\ge\min(k+1,2g-2),
\]

\[
v_5(\lambda)\ge\min(k,2g).
\]

The same lower bounds hold for \(F\).

Therefore:

* for \(k\le2g-3\),
  \[
  2\cdot10^k\mid\lambda,F;
  \]

* for \(k=2g-2\),
  \[
  10^{2g-2}\mid\lambda,F;
  \]

* for \(k=2g-1\),
  \[
  H^2/5\mid\lambda,F;
  \]

* for \(k\ge2g\),
  \[
  H^2\mid\lambda,F.
  \]

The key point is not a local Hensel phase: it is that **one root factor must absorb an explicit decimal prime-power block whose depth grows linearly with \(g\)**.

## 6.2 GCD of the two near-square factors

Let

\[
L=Y-R_0,\qquad M=Y+R_0.
\]

Then

\[
\gcd(L,M)\mid2Y.
\]

Root divisibility says one factor is \(AH^2C_1\), and the other is \(\lambda\).

Because

\[
\gcd(AH^2,u)=1
\]

and LU gives

\[
\gcd(\lambda,u)=1,
\]

no prime of \(u\) can be "hidden" in the complementary small root factor.  The cyclotomic divisor \(u\) and the decimal core \(H^2\) therefore occupy genuinely different support channels.

This is the useful allocation statement obtained in this round.

---

# Part VII — Uniform Large-\(g\) Theorems

No theorem of the form

\[
g\ge g_0\Longrightarrow\varnothing
\]

was proved.

So **Success B is not attained**.

What is proved instead is a collection of uniform outer-\(g\) compression theorems.

## 7.1 Positive branch: finite signed index

Assume

\[
S_R>0.
\]

Then \(X<0\).  Write

\[
s:=-j>0.
\]

Let

\[
n:=Us=-N>0.
\]

From J1,

\[
2U|X|+Z=un.
\]

Using RRGS+ and UZ+,

\[
un
<
2u+\frac{2uA}{G}.
\]

Thus

\[
\boxed{
n<2+\frac{2A}{G}.
}
\tag{PN}
\]

### Case \(q=1\)

Then \(u=G+1\), \(A=2G+3\), so

\[
n<6+\frac6G.
\]

For \(g\ge4\), \(n\) is a positive odd integer, hence

\[
\boxed{
n\in\{1,3,5\}.
}
\tag{PN1}
\]

### Case \(q>1\)

Because \(q\mid G+1\), \(q\) is odd and coprime to \(5\).  Also

\[
G+1\equiv2\pmod3,
\]

so \(3\nmid q\).  Hence

\[
q>1\Longrightarrow q\ge7.
\]

Then for \(G\ge10^4\),

\[
2+\frac{2A}{G}
=
2+
\frac{4(G+1)}{qG}
+\frac2G
<3.
\]

Therefore

\[
\boxed{n=1.}
\]

Since \(n=Us\) with positive integers \(U,s\),

\[
\boxed{
U=1,\qquad s=1,\qquad j=-1,\qquad N=-1.
}
\tag{POS-COLLAPSE}
\]

This is a complete radial collapse of the non-extreme positive branch.

## 7.2 Positive \(q=1\) is uniformly impossible

In the \(q=1\) chamber, radialized RCE1 is

\[
2Aa_3=(G-1)Z+n.
\]

Here

\[
A=2G+3,
\qquad
2A\equiv10\pmod{G-1}.
\]

Hence

\[
10a_3\equiv n\pmod{G-1}.
\]

Since

\[
10\cdot\frac G{10}=G\equiv1\pmod{G-1},
\]

the inverse of \(10\) modulo \(G-1\) is \(G/10\).  Therefore

\[
a_3
\equiv
n\frac G{10}
\pmod{G-1}.
\]

For

\[
n\in\{1,3,5\}
\]

the representative \(nG/10\) already lies in the legal digit interval

\[
[G/10,G),
\]

and adding \(G-1\) exits the interval.  Hence

\[
a_3=nG/10.
\]

But \(g\ge4\), so \(a_3\) is divisible by \(10\).  On the other hand

\[
a_3=Uc
\]

is a product of ten-units.

Contradiction.

Thus

\[
\boxed{
S_R>0,\ q=1
\Longrightarrow
\varnothing.
}
\tag{POS-Q1}
\]

## 7.3 Positive \(q>1\): exact Bézout gate

By POS-COLLAPSE,

\[
U=1,\qquad j=-1.
\]

Therefore RCE1 becomes

\[
\boxed{
2Ac-q(G-1)z=1.
}
\tag{BEZ}
\]

Equivalently,

\[
\boxed{
(G-1)t=2(q+4)c-q,
}
\tag{BEZ2}
\]

\[
\boxed{
q(q+4)z=At+2.
}
\tag{BEZ3}
\]

Hence

\[
At\equiv-2\pmod{q(q+4)}.
\tag{BEZ-CONG}
\]

Any solution forces

\[
\gcd(A,q(q+4))=1.
\]

The digit window \(G/10\le c<G\) gives

\[
0<t<
\frac{2(q+4)G}{G-1}.
\]

For \(q\ge7\),

\[
\frac{2(q+4)G}{G-1}
<
q(q+4).
\]

Therefore BEZ-CONG has **at most one** admissible \(t\).

Thus:

\[
\boxed{
\text{for fixed }(g,q),\ S_R>0,\ q>1,
\text{ there is at most one pre-root cyclotomic cell.}
}
\tag{POS-ONE}
\]

The old \((c,z,U)\) fibre has disappeared.

## 7.4 Positive root factor gives \(q<6G^{1/3}\)

Use the radialized factor

\[
\widetilde F=A W^2+ZD_2,
\]

where \(W=U|X|\).

In the positive branch,

\[
W<u,
\qquad
Z<\frac{2uA}{G},
\]

and

\[
D_2=u a_3-GW<u a_3<uG.
\]

Therefore

\[
\widetilde F
<
Au^2
+
\frac{2uA}{G}\cdot uG
=
3Au^2.
\]

But \(k\ge2g-1\), so RDCF gives

\[
\frac{H^2}{5}
=
\frac{G^2}{20}
\mid
\widetilde F.
\]

Hence

\[
\frac{G^2}{20}
<
3Au^2.
\]

Since \(A=2u+1\le3u\),

\[
G^2<180u^3.
\]

With \(u=(G+1)/q\),

\[
q^3
<
180G\left(1+\frac1G\right)^3
<
216G
\qquad(G\ge10^4).
\]

Thus

\[
\boxed{
q<6G^{1/3}.
}
\tag{POS-QBOUND}
\]

Combining with \(q>1\Rightarrow q\ge7\),

\[
\boxed{
S_R>0
\Longrightarrow
7\le q<6G^{1/3},
\quad
N=-1,
\quad
\#t\le1.
}
\tag{POS-FRONT}
\]

This is the strongest uniform positive-branch theorem of the round.

## 7.5 Negative signed-index strip

Now assume

\[
S_R<0,
\qquad
X>0.
\]

Let

\[
W:=UX>0.
\]

From J1,

\[
uN=2W-Z.
\]

Using UW- and UZ-,

\[
\boxed{
-\left(
\frac{2\eta}{K}
+
\frac{2A}{G}
\right)
<
N
<
\frac{2\eta G^2}{K}.
}
\tag{NSTRIP}
\]

Recall that \(N\) is odd.

### Top layer \(k=2g+1\)

Here \(K=10G^2\).  Thus

\[
N<\frac{\eta}{5}<1.
\]

If \(q>1\), then \(q\ge7\) and, for \(G\ge10^4\),

\[
\frac{2\eta}{K}+\frac{2A}{G}<1.
\]

So

\[
-1<N<1,
\]

which contains no odd integer.

If \(q=1\), the strip gives

\[
N\in\{-3,-1\}.
\]

RCE1 modulo \(G-1\) gives

\[
10a_3\equiv-N\pmod{G-1}.
\]

Hence

\[
N=-1\Rightarrow a_3=G/10,
\]

\[
N=-3\Rightarrow a_3=3G/10,
\]

both non-ten-units.

Therefore

\[
\boxed{
S_R<0,\ k=2g+1
\Longrightarrow
\varnothing.
}
\tag{NEG-TOP}
\]

The inherited negative exponent ceiling improves from \(2g+1\) to

\[
\boxed{k\le2g.}
\]

### Boundary layer \(k=2g\)

Now

\[
N<2\eta<5.196.
\]

For \(q>1\), the lower side is \(>-1\), hence

\[
\boxed{
N\in\{1,3,5\}.
}
\tag{NEG-N}
\]

For \(q=1\),

\[
N\in\{-3,-1,1,3,5\}.
\]

## 7.6 Negative \(q=1,k=2g\) is uniformly impossible

For \(q=1\), RCE1 modulo \(G-1\) gives

\[
10a_3\equiv-N\pmod{G-1}.
\]

For \(N=-3,-1\), this forces

\[
a_3=3G/10,\quad G/10,
\]

hence non-ten-units.

For \(N=3\),

\[
a_3=\frac{7G}{10}-1,
\qquad
Z=\frac{14G+15}{5},
\]

so

\[
W=\frac{29G+30}{10}.
\]

Since

\[
\frac{29G+30}{10}
>
2.9G
>
2.598(G+1)
>
\eta u
\]

for \(G\ge10^4\), UW- is violated.

For \(N=5\),

\[
a_3=\frac G2-1,
\qquad
Z=2G+1,
\]

\[
W=\frac{7G+6}{2}
>
3.5G
>
\eta u.
\]

Thus \(N=3,5\) are impossible.

The only linear survivor is

\[
\boxed{
N=1,\qquad t=9.
}
\]

It reconstructs

\[
\boxed{
a_3=\frac{9G-10}{10},
}
\]

\[
\boxed{
Z=\frac{18G+25}{5},
}
\]

\[
\boxed{
W=\frac{23G+30}{10},
}
\]

\[
\boxed{
D_2=\frac{32G^2+29G-10}{10}.
}
\]

At \(k=2g\), \(K=G^2\).  The reduced radialized discriminant is

\[
\widetilde\Delta
=
\frac{G^2}{400}P(G),
\]

where

\[
\begin{aligned}
P(G)=\;&
4096G^8
+15616G^7
+19748G^6
+6712G^5\\
&-7856G^4
-22132G^3
-34633G^2
-25490G
-6600.
\end{aligned}
\]

Set

\[
Q(G)=64G^4+122G^3+38G^2-20G.
\]

Direct expansion gives

\[
P-(Q-35)^2
=
60G^4
-12072G^3
-32373G^2
-26890G
-7825.
\]

For \(G\ge10^4\),

\[
32373G^2+26890G+7825<4G^3,
\]

so

\[
P-(Q-35)^2
>
G^3(60G-12076)>0.
\]

Also

\[
P-(Q-34)^2
=
-68G^4
-12316G^3
-32449G^2
-26850G
-7756
<0.
\]

Hence

\[
\boxed{
(Q-35)^2<P<(Q-34)^2.
}
\]

Thus \(P\) is not a square, and therefore \(\widetilde\Delta\) is not a square.

So

\[
\boxed{
S_R<0,\ q=1,\ k=2g
\Longrightarrow
\varnothing.
}
\tag{NEG-Q1-2G}
\]

## 7.7 Negative \(k=2g,q>1\): outer divisor compression

At \(k=2g\),

\[
H^2\mid\widetilde F.
\]

The negative bounds give

\[
W<\eta u,
\]

\[
Z<
\frac{2\eta u}{G^2}
+
\frac{2uA}{G},
\]

\[
D_2=u a_3+GW<(1+\eta)uG.
\]

Hence

\[
\begin{aligned}
\widetilde F
&=
AW^2+ZD_2\\
&<
A\eta^2u^2
+
\left(
\frac{2\eta u}{G^2}
+
\frac{2uA}{G}
\right)
(1+\eta)uG\\
&<
14Au^2
\qquad(G\ge10^4,\ \eta<2.598).
\end{aligned}
\]

Since \(H^2=G^2/4\) divides the positive integer \(\widetilde F\),

\[
\frac{G^2}{4}<14Au^2.
\]

Thus

\[
G^2<56Au^2\le168u^3.
\]

Therefore

\[
q^3
<
168G\left(1+\frac1G\right)^3
<
216G,
\]

and

\[
\boxed{
q<6G^{1/3}.
}
\tag{NEG-QBOUND}
\]

Combining this with NEG-N and the cyclotomic congruence

\[
At\equiv2N\pmod{q(q+4)},
\]

one obtains a constant fibre bound.

Let

\[
d=\gcd(A,q(q+4)).
\]

The congruence requires \(d\mid2N\).  Since \(d\) is odd,

\[
d\mid N.
\]

For \(N=1,3,5\), the number of residue classes for \(t\) modulo \(q(q+4)\) is at most \(1,3,5\), respectively.

The digit interval keeps \(t\) inside a range shorter than one full modulus once
\(q<6G^{1/3}\) and \(G\ge10^4\).  Hence the total number of pre-root \((N,t)\) cells for each outer divisor \(q\) is at most

\[
1+3+5=9.
\]

Therefore

\[
\boxed{
S_R<0,\ k=2g
\Longrightarrow
\begin{cases}
q=1:&\varnothing,\\
q>1:&
7\le q<6G^{1/3},\
N\in\{1,3,5\},\
\#(N,t)\le9.
\end{cases}
}
\tag{NEG-2G-FRONT}
\]

---

# Part VIII — Finite Residual Certificate

No finite certificate is claimed to close all

\[
4\le g<g_0
\]

because no large-\(g\) extinction theorem \(g\ge g_0\) was proved.

The computation in this round is therefore a **targeted exact audit**, not a closure substitute.

The executable file is

```text
A1_J2_CZDR_search.py
```

and the output is

```text
A1_J2_CZDR_certificate.txt
```

The audited depths are

\[
g=4,5,\ldots,10.
\]

For each audited \(g\), the program:

1. generates every divisor \(u\mid G+1\) by exact trial division;
2. sets \(q=(G+1)/u\);
3. removes only the rigorously impossible \(A\)-non-ten-unit cells;
4. applies the proved positive \(N=-1\) collapse;
5. solves the exact linear congruence for \(t\);
6. reconstructs \(Z,a_3,\mathcal X,D_2\) using RCE;
7. tests exact digit, sign, ten-unit and RRGS/UZ bounds;
8. evaluates the radialized quadratic with integer arithmetic;
9. tests discriminants with `isqrt`;
10. tests the exact root divisibility.

It separately audits the negative \(k=2g+1\) and \(k=2g\) layers.

The observed totals are:

\[
\boxed{
\text{positive linear survivors for }4\le g\le10: 0,
}
\]

\[
\boxed{
\text{negative }k=2g+1\text{ survivors: }0,
}
\]

and, for every audited depth, the only negative \(k=2g\) linear survivor is the already proved symbolic family

\[
q=1,\quad N=1,\quad t=9,
\]

which has non-square discriminant.

The certificate ends with

```text
ROOT_SURVIVOR_COUNT=0
```

for the audited slices.

This is consistent with the analytic theorems but is not promoted to a statement beyond the audited range.

---

# Part IX — Closure Audit

## 9.1 \(u=1\)

Inherited closure:

\[
\boxed{u=1\Longrightarrow\varnothing.}
\]

No reopening occurred.

## 9.2 \(u>1\)

This is the only live outer chamber.

The present round compresses, but does not fully kill, it.

## 9.3 \(q=1\)

Positive branch:

\[
\boxed{q=1\Longrightarrow\varnothing.}
\]

Negative branch:

\[
k=2g+1\Longrightarrow\varnothing,
\]

\[
k=2g\Longrightarrow\varnothing.
\]

The low-\(k\) negative \(q=1\) cells remain part of the open frontier.

## 9.4 \(u=q\)

If \(u=q\), then

\[
u^2=G+1.
\]

But

\[
G+1=10^g+1\equiv2\pmod3,
\]

while a square modulo \(3\) is \(0\) or \(1\).  Hence

\[
\boxed{u=q\ \text{is impossible}.}
\]

## 9.5 \(u<q\) and \(u>q\)

Neither chamber is silently dropped.

The new \(q\)-bound is written in the complementary factor \(q\), so it applies uniformly to both orderings whenever the corresponding sign/\(k\) theorem applies.

## 9.6 \(5\mid A\)

Empty:

\[
\boxed{5\mid A\Longrightarrow\varnothing.}
\]

## 9.7 \(5\nmid A\)

This is the only admissible chamber.

Thus

\[
\gcd(A,H)=1
\]

is now safe to use.

## 9.8 \(X>0\)

This is \(S_R<0\).

The top layer \(k=2g+1\) is closed.

The \(k=2g,q=1\) cell is closed.

The \(k=2g,q>1\) cell is compressed to

\[
7\le q<6G^{1/3},
\qquad
N\in\{1,3,5\},
\qquad
\#(N,t)\le9.
\]

The main unresolved negative mass is

\[
1\le k\le2g-1.
\]

## 9.9 \(X<0\)

This is \(S_R>0\).

The \(q=1\) chamber is closed.

For \(q>1\),

\[
U=1,\quad j=-1,\quad N=-1,
\]

\[
7\le q<6G^{1/3},
\]

and for every \((g,q)\) there is at most one \(t\) before the root gate.

## 9.10 Small \(k\) / large \(k\)

Large negative \(k\) was materially improved:

\[
k=2g+1\ \text{is gone},
\]

and \(k=2g\) is almost completely finite-fibred in the outer divisor.

Small negative \(k\),

\[
1\le k\le2g-1,
\]

remains the dominant open sector.

Positive \(k\) is always large,

\[
2g-1\le k\le3g-1,
\]

which is exactly why the universal \(H^2/5\) root core becomes available.

## 9.11 Root sign \(\pm\)

No root sign is dropped.

The \((C_1,\lambda)\) factor language is sign-unified: one root sign corresponds to

\[
Y+R_0=AH^2C_1,
\]

the other to

\[
Y-R_0=AH^2C_1.
\]

In both cases the complementary factor is \(\lambda\).

## 9.12 Square discriminant

Still required.

The factor system is exactly equivalent to square discriminant plus integral-root divisibility, so no square condition has been weakened.

## 9.13 Integral root divisibility

Not ignored; it is the source of the new decimal-core divisor theorem.

## 9.14 Primitive gcd

The new residue

\[
C_1^2\equiv z^2\pmod u
\]

is combined with primitive gcd to obtain

\[
\gcd(z,u)=1,
\qquad
\gcd(F,u)=\gcd(\lambda,u)=1.
\]

Thus primitive gcd remains active.

## 9.15 Common-\(U\) reconstruction

The radial chart does not discard \(U\).  It packages the actual scale into

\[
a_1=UC_1,\quad
a_3=Uc,\quad
Z=Uz,\quad
N=Uj.
\]

The radialized quadratic is exactly the original quadratic multiplied by \(U^2\).

## 9.16 Face A / Face B

No face-specific theorem was used to exclude a face.

The only inherited face information used is the already audited union of the exact \(k\)-ranges.  Thus both faces remain covered.

## 9.17 Near-square conjectures audit

### C1: \(\Delta_0\) is always nonsquare

Not proved.

The targeted certificate found no square in the audited compressed slices, but no global statement is made.

### C2: square discriminant may fail root divisibility

Still plausible and now represented exactly by the factor system.

### C3: \(C_1>F\)

Not proved and not used.

### C4: \(F/C_1=1\)

False as a possible uniform closure principle in the positive branch, because

\[
H^2/5\mid\lambda=F/C_1.
\]

### C5: \(AH^2F<2Y-1\) uniformly

Not proved.

Generic adjacent-square spacing is not the new terminal mechanism.

### C6: large-\(g\) magnitude closure plus finite residual certificate

Not achieved.

The replacement result is the uniform complementary-divisor ceiling

\[
q<6G^{1/3}
\]

on the positive branch and on the negative \(k=2g\) boundary.

---

# Part X — New Frontier

## 10.1 J2 status

\[
\boxed{\textbf{J2 remains OPEN}.}
\]

Therefore Exact Resonance remains OPEN.

But the old J2-CZDR frontier

\[
(g,u,k,c,z)
\]

should no longer be used as the preferred terminal chart.

## 10.2 New terminal obstruction

The recommended new obstruction is:

\[
\boxed{
\textbf{J2-RCRF}
=
\textbf{Radial Cyclotomic Root-Factor Exclusion}.
}
\]

Fix

\[
g\ge4,
\qquad
G=10^g,
\]

choose a nontrivial complementary divisor

\[
q\mid G+1,
\qquad
u=\frac{G+1}{q},
\]

with

\[
u>1,
\qquad
\gcd(2u+1,10)=1.
\]

Choose \(k\) in the surviving sign band.

Then choose an odd signed cyclotomic radial index \(N\) in the exact strip

\[
-\left(
\frac{2\eta}{K}
+
\frac{2A}{G}
\right)
<
N
<
\frac{2\eta G^2}{K}
\]

for the negative branch, or use the positive theorem

\[
N=-1.
\]

Choose \(t\) satisfying

\[
\boxed{
At\equiv2N\pmod{q(q+4)},
}
\]

and reconstruct

\[
\boxed{
a_3=
\frac{(G-1)t-qN}{2(q+4)},
}
\]

\[
\boxed{
Z=
\frac{At-2N}{q(q+4)},
}
\]

\[
\boxed{
\mathcal X=\frac{Z+uN}{2},
}
\]

\[
\boxed{
D_2=u a_3+G\mathcal X.
}
\]

Require the exact digit/sign/ten-unit/RRGS conditions.

Then rule out every positive integer \(a_1\) satisfying

\[
\boxed{
AH^2a_1^2
-
2uKD_2a_1
+
A\mathcal X^2+ZD_2
=0,
}
\tag{RCRF-Q}
\]

equivalently every positive factor pair

\[
\boxed{
a_1\Lambda
=
A\mathcal X^2+ZD_2,
}
\]

\[
\boxed{
AH^2a_1+\Lambda
=
2uKD_2,
}
\]

with

\[
\boxed{
D_{g,k}\mid\Lambda,
}
\]

\[
\boxed{
a_1^2\equiv Z^2\pmod u,
}
\]

\[
\boxed{
Ka_1\equiv-Z\pmod A.
}
\]

This chart is strictly more rigid than the previous \(C_3\)-\(z\) discriminant chart.

### Positive branch specialization

\[
\boxed{
7\le q<6G^{1/3},
\qquad
N=-1,
\qquad
\#t\le1.
}
\]

So for fixed \((g,q,k)\), there is at most one pre-root terminal cell.

### Negative boundary specialization

\[
k=2g+1:\quad\varnothing,
\]

\[
k=2g,\ q=1:\quad\varnothing,
\]

\[
k=2g,\ q>1:
\quad
\boxed{
7\le q<6G^{1/3},
\quad
N\in\{1,3,5\},
\quad
\#(N,t)\le9.
}
\]

### Main remaining open mass

The next attack should focus on

\[
\boxed{
S_R<0,\qquad
1\le k\le2g-1,
}
\]

and should use the new \((N,t)\) cyclotomic chart together with the decimal-core root factor

\[
D_{g,k}\mid\Lambda.
\]

The immediate next question is no longer whether a broad \((c,z)\) box contains a square root.  It is:

\[
\boxed{
\textbf{Can the signed radial index }N
\textbf{ and the second Euclidean remainder }t
\textbf{ simultaneously satisfy the cyclotomic congruence and the forced root-factor core?}
}
\]

That is the new lowest-dimensional exact J2 obstruction produced by this round.

---

# Final Status Ledger

## NEW PROVED

1. \(5\mid A\) is impossible; hence \(\gcd(A,H)=1\).
2. Exact root-factor equivalence LR1–LR2.
3. Decimal-core divisor
   \[
   D_{g,k}\mid\lambda,F.
   \]
4. Root residues
   \[
   C_1^2\equiv z^2\pmod u,
   \qquad
   KC_1\equiv-z\pmod A.
   \]
5. Root-factor coprimality
   \[
   \gcd(z,u)=\gcd(F,u)=\gcd(\lambda,u)=1.
   \]
6. Cyclotomic signed coordinate
   \[
   j=q(G-1)z-2Ac=(2X-z)/u.
   \]
7. Radial cyclotomic Euclidean system RCE1–RCE3.
8. Positive signed-index collapse:
   \[
   q>1\Rightarrow U=1,\ j=-1.
   \]
9. Positive \(q=1\) uniform extinction.
10. Positive outer bound
    \[
    q<6G^{1/3}.
    \]
11. Positive at-most-one-\(t\) theorem.
12. Negative signed-index strip NSTRIP.
13. Negative top-layer extinction
    \[
    k=2g+1\Rightarrow\varnothing.
    \]
14. Negative \(q=1,k=2g\) extinction, including the exact adjacent-square polynomial kill.
15. Negative \(k=2g,q>1\) outer bound
    \[
    q<6G^{1/3}.
    \]
16. Negative \(k=2g\) finite signed index
    \[
    N\in\{1,3,5\}
    \]
    and at-most-nine-\((N,t)\)-cells per outer divisor.

## COMPUTATIONAL EVIDENCE

Exact targeted audit for

\[
4\le g\le10
\]

finds no positive compressed linear survivor, no negative \(k=2g+1\) survivor, and no integral root survivor in the negative \(k=2g\) slice.

## OPEN

1. Full positive J2 extinction for all \(g\), despite the \((g,q,k)\)-level compression.
2. Negative
   \[
   1\le k\le2g-1.
   \]
3. Full
   \[
   J=2,\quad g\ge4,\quad u>1
   \Longrightarrow\varnothing.
   \]
4. J2 Resonance Closure Certificate.

---

# File Audit

The task is intentionally concluded only after the following files are written:

```text
A1_J2_CZDR_Report.md
A1_J2_CZDR_search.py
A1_J2_CZDR_certificate.txt
```

No survivor ledger file is referenced because the targeted certificate has

```text
ROOT_SURVIVOR_COUNT=0
```

in the audited slices.

FINAL_REPORT_FILE: A1_J2_CZDR_Report.md

COMPUTATION_FILE: A1_J2_CZDR_search.py

CERTIFICATE_FILE: A1_J2_CZDR_certificate.txt
