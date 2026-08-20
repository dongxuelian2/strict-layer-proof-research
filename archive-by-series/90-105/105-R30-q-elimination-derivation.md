# 105-R30 — Residual \(q\)-Elimination Derivation

**Status:** new R30 theorem; exact algebraic elimination of the R15 residual denominator integer as an independent search coordinate.

---

## 1. Starting point

Fix one R26 finite architecture

\[
\mathfrak a=(\pi,\sigma,n,\delta,\rho,m)
\]

that has reached the TC3/TC4 interface and passed every fixed compatibility condition needed to activate the R15 shell.

TC3 gives

\[
z=\Lambda q,
\qquad
Q_-\le q\le Q_+,
\qquad
\gcd(q,F)=1.
\]

Let

\[
\boxed{V_0:=\Lambda u_0AW.}
\]

R14's exact variable graph gives

\[
V=z\,u_0AW,
\qquad
b_2=zA,
\qquad
b_3=zW,
\]

and the frozen \(g_1\)-shell fixes \(g_1=g_1^*\). Hence on the residual \(q\)-fibre,

\[
\boxed{V(q)=qV_0.}
\]

All raw denominator rows that are homogeneous in \(V,b_1,b_2,b_3\) acquire the same common factor \(q\).

---

## 2. Radial coefficients do not move with TC3-admissible \(q\)

R15's canonical forbidden factor contains

\[
F=\operatorname{rad}(R_1C_2C_3).
\]

Therefore every TC3-admissible residual \(q\) satisfies

\[
\gcd(q,C_2C_3)=1.
\]

Since

\[
P_2=u_0WC_2,
\qquad
P_3=u_0AC_3,
\]

and the fixed R15 shape checks contain

\[
\gcd(A,C_2)=1,
\qquad
\gcd(W,C_3)=1,
\]

the new prime support contributed by \(q\) cannot increase \(\gcd(V,P_2)\) or \(\gcd(V,P_3)\) beyond the already frozen values. More invariantly, the R15 theorem was obtained precisely by separating the forced denominator content \(\Lambda\) from a residual factor avoiding \(C_2C_3\); hence the decontented radial coefficients \(C_2,C_3\) are fixed on the residual \(q\)-fibre.

The \(g_1\)-coordinate is fixed by the exact shell

\[
\gcd(u_0AWz,P_1)=g_1^*,
\]

and \((q,R_1)=1\) is exactly what prevents the residual factor from changing it.

Thus

\[
\boxed{g_i,\ C_i\text{ are fixed across every TC3-admissible residual }q.}
\]

---

## 3. Common-dilation invariance of the source geometry

R7's normalized source row has the form

\[
\widehat{\mathcal A}
=\frac{XYG}{g_1}+\frac{YG}{g_2}+\frac1{g_3},
\]

\[
\widehat{\mathcal B}=\frac{XYGK}{g_1},
\qquad
\widehat{\mathcal C}=YC_2+C_3.
\]

The raw row is obtained by multiplying by the common denominator content \(V\). Since \(V,b_i\) all acquire the same residual factor \(q\), decontenting removes that factor exactly.

The R30 regression script checks this on ten exact common dilations of the frozen R7D witness B and recovers the same normalized row

\[
(\widehat{\mathcal A},\widehat{\mathcal B},\widehat{\mathcal C})=(21,125,3345)
\]

in every case. This computation is a regression of the algebraic homogeneity theorem, not a claim that those ten dilations are ten legal 105 architectures.

Consequently the post-PSDG/source-completed *geometric* profile, the block-2/3 interval endpoints, and every fixed source-native affine condition remain fixed when only the R15 residual \(q\) changes.

---

## 4. The only residual \(q\)-dependence in TC4

TC4's primitive source condition is

\[
\gcd(U,V)=1.
\]

Because \(V(q)=V_0q\),

\[
\boxed{
\gcd(U,V_0q)=1
\iff
\gcd(U,V_0)=1\quad\text{and}\quad\gcd(U,q)=1.
}
\tag{split}
\]

All other source-completed conditions can be frozen into a q-independent finite set of candidate source integers.

Define

\[
\boxed{
\mathcal U_0(\mathfrak a)
}
\]

to be the set of positive integers \(U\) satisfying:

1. the exact decorated R8 source interval, including strict endpoint flags;
2. the fixed source-native affine/periodic selector of the frozen source chart;
3. every fixed source-completed predicate independent of the R15 residual \(q\);
4. \(\gcd(U,V_0)=1\).

Because \(U<R_{\rm src}<\infty\), \(\mathcal U_0(\mathfrak a)\) is finite.

Then for fixed \(U\in\mathcal U_0(\mathfrak a)\), the residual \(q\) must satisfy simultaneously

\[
\gcd(q,F)=1,
\qquad
\gcd(q,U)=1.
\]

These fuse exactly into

\[
\boxed{\gcd(q,FU)=1.}
\]

Therefore

\[
\boxed{
TC3(\mathfrak a)+TC4(\mathfrak a)
\iff
\exists U\in\mathcal U_0(\mathfrak a)
\ \exists q\in[Q_-,Q_+]\cap\mathbb Z_{>0}:
\gcd(q,FU)=1.
}
\tag{R30-QF-1}
\]

This is the exact integer fusion.

---

## 5. Möbius elimination of \(q\)

For a fixed positive integer \(U\), define

\[
\boxed{
\Phi_{\mathfrak a}(U)
:=
\sum_{d\mid\operatorname{rad}(FU)}
\mu(d)
\left(
\left\lfloor\frac{Q_+}{d}\right\rfloor
-
\left\lfloor\frac{Q_--1}{d}\right\rfloor
\right).
}
\tag{Phi}
\]

By ordinary inclusion-exclusion, \(\Phi_{\mathfrak a}(U)\) is exactly

\[
\#\{q\in[Q_-,Q_+]\cap\mathbb Z_{>0}:\gcd(q,FU)=1\}.
\]

No asymptotic density and no Jacobsthal bound is used.

Define the terminal q-free architecture count

\[
\boxed{
N_{30}(\mathfrak a)
:=
\sum_{U\in\mathcal U_0(\mathfrak a)}
\Phi_{\mathfrak a}(U).
}
\tag{N30}
\]

Then

\[
\boxed{
TC3(\mathfrak a)+TC4(\mathfrak a)
\iff
N_{30}(\mathfrak a)>0.
}
\tag{R30-QF-2}
\]

This formula contains **no free residual denominator integer \(q\)**.

The exact execution script checks the Möbius formula against direct gcd enumeration in

\[
\boxed{540000}
\]

small exact test cases.

It also checks the coprimality splitting identity (split) in

\[
\boxed{117649}
\]

exact triples \((V_0,q,U)\).

---

## 6. Prime-cover form

For fixed \(U\in\mathcal U_0\),

\[
\Phi_{\mathfrak a}(U)=0
\]

if and only if every integer in the residual \(q\)-window is covered by a forbidden prime:

\[
\boxed{
[Q_-,Q_+]\cap\mathbb Z
\subseteq
\bigcup_{p\mid FU}p\mathbb Z.
}
\tag{cover}
\]

Thus the exact R30 replacement for a generic Jacobsthal argument is a finite **architecture-specific prime-cover certificate**.

The union of TC3's prime set and TC4's primitive source prime set is literally

\[
\operatorname{supp}(FU).
\]

---

## 7. Exact special branches

### Empty window

If

\[
Q_->Q_+,
\]

then

\[
N_{30}(\mathfrak a)=0
\]

without evaluating the source successor.

### Singleton window

If

\[
Q_-=Q_+=q^*,
\]

then joint TC3/TC4 feasibility is equivalent to the existence of

\[
U\in\mathcal U_0
\]

with

\[
\boxed{\gcd(q^*,FU)=1.}
\]

Since a TC3 singleton already requires \(\gcd(q^*,F)=1\), the genuinely new TC4 coupling is simply

\[
\boxed{\gcd(q^*,U)=1.}
\]

### Multi-integer window

No new existential integer is needed: compute \(\Phi_{\mathfrak a}(U)\) exactly for each q-independent source candidate \(U\), or equivalently compute the prime cover (cover).

---

## 8. What this theorem does not prove

R30 does **not** prove

\[
N_{30}(\mathfrak a)=0
\]

for every legal post-support architecture \(\mathfrak a\).

It also does not prove a universal constant bound such as

\[
Q_+-Q_-<1
\]

or

\[
\#\{q\text{ satisfying TC3}\}\le1
\]

across the entire primitive-sphere locus.

Therefore the correct status is:

```text
Q_VARIABLE_ELIMINATION_EQUIVALENCE=PROVED
TC3_TC4_Q_FREE_COUNT_EQUIVALENCE=YES
GLOBAL_TC3_TC4_INCOMPATIBILITY=NOT_PROVED
STRICT_A1_UNLIFTABILITY=NOT_PROVED
```

The minimal missing theorem is no longer “control the denominator integer.” It is the q-free statement

\[
\boxed{
N_{30}(\mathfrak a)=0
\quad\text{for every legal post-support architecture }\mathfrak a,
}
\]

or a single exact counterexample with \(N_{30}(\mathfrak a)>0\).
