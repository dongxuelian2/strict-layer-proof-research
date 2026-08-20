# J2-65-R11 — Gaussian Modular Reduction × Cusp Fundamental Domain × Continuant Encoding Report

**Scope:** Strict Layer — A1-only — Exact Resonance R=0 — J=2 — q>1 rational/Brauer layer  
**Round:** 65 第十一轮 / A1 统一终端线第三十六轮  
**Status:** **J2 OPEN**

## 1. Executive verdict

R11 closes the exact group-theoretic gap left by R10 and proves the requested one-step Gaussian Euclidean descent.

The central new results are:

1. The full automorphism group of
\[
H_{\rm can}=\begin{pmatrix}0&1+i\\1-i&1\end{pmatrix}
\]
is explicitly identified. Projectively,
\[
\boxed{\operatorname{PAut}(H_{\rm can})\cong C_4*C_4,}
\]
with one cusp and signature \((0;4,4,\infty)\). Including scalar Gaussian units,
\[
\boxed{\operatorname{Aut}(H_{\rm can})\cong \mu_4\times(C_4*C_4).}
\]

2. The R10 parabolic is the full cusp stabilizer up to scalar units:
\[
\boxed{\operatorname{Stab}([e_1])
=\{\varepsilon P_n:\varepsilon\in\mu_4,\ n\in\mathbb Z\}.}
\]

3. For every split actual power-ten matrix
\[
H=\begin{pmatrix}a&z\\\bar z&c\end{pmatrix},
\quad a=D_+,\ c=D_-,
\]
one has
\[
\boxed{\sqrt{5/7}<|z/a|<1.}
\]
The first nearest Gaussian digit is nonzero and belongs, modulo Gaussian units, to exactly two shells:
\[
\boxed{N(n)=1\quad\text{or}\quad N(n)=2.}
\]

4. The exact shear produces
\[
c'=\frac{|z-an|^2-2}{a},
\]
and for \(a>2\),
\[
\boxed{0\le c'<a/2.}
\]
Thus every actual split state enters the reduced cusp region in one step.

5. Iteration gives a strict halving Euclidean reduction. Every positive bulk step reduces the current positive pivot by more than a factor two; the number of bulk stages is logarithmic.

6. The reduction word has an exact continuant recurrence. If
\[
R(n)=\begin{pmatrix}-n&1\\1&0\end{pmatrix},
\]
then
\[
M_j=R(n_0)\cdots R(n_{j-1})
=\begin{pmatrix}P_j&P_{j-1}\\R_j&R_{j-1}\end{pmatrix},
\]
where
\[
X_{j+1}=-n_jX_j+X_{j-1}.
\]

7. The level-\(u\) “two isotropic columns” condition is automatic for every odd \(u\). For \(H_0\), the fixed basis
\[
V=\begin{pmatrix}i&-i\\1&1\end{pmatrix}
\]
has both column norms zero and determinant \(2i\), hence is unimodular modulo every odd \(u\). Therefore
\[
\boxed{\texttt{LEVEL_u_ISOTROPIC_BASIS_OBSTRUCTION=FALSE}.}
\]

R11 does **not** prove that every prescribed power-ten diagonal pair occurs. The rational/Brauer layer is therefore not retired and \(q>1\) is not closed.

---

## 2. R10 actual package reloaded

R10 proved:

\[
h_{\rm Herm}^{\rm primitive}(-2)=1,
\qquad
H_0=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
H_{\rm can}=\begin{pmatrix}0&1+i\\1-i&1\end{pmatrix},
\]
\[
\operatorname{SNF}_{\mathbb Z[i]}\sim\operatorname{diag}(1,2),
\]
and for actual split states
\[
H=\begin{pmatrix}D_+&z\\\bar z&D_-\end{pmatrix}
=U^*H_0U,\qquad U\in GL_2(\mathbb Z[i]).
\]

Also
\[
D_\pm=u(2KG\pm B),\qquad B=2G+q,\qquad uq=G+1,
\]
and
\[
0<\frac{D_+-D_-}{D_++D_-}
=\frac{B}{2KG}
\le \frac{31}{200}<\frac16.
\]

No class-number, Smith, inert-prime or composite norm-one layer is reopened.

---

## 3. Arithmetic quotient and one necessary correction

Let
\[
\Gamma=\operatorname{Aut}(H_0).
\]
Then
\[
\mathscr X=\Gamma\backslash GL_2(\mathbb Z[i])
\]
is exactly the set of matrices in the unique congruence orbit, with
\[
[U]\longmapsto U^*H_0U.
\]
Therefore
\[
\mathscr D([U])
=\bigl(H_0(v_1,v_1),H_0(v_2,v_2)\bigr)
\]
is well-defined and
\[
\boxed{\text{split locus}=\mathscr D(\mathscr X).}
\]

However, \(\mathscr X\) is a discrete coset space, **not** the Fuchsian modular surface
\(\Gamma\backslash\mathbb H\).
The hyperbolic fundamental domain of \(\Gamma\) controls left-stabilizer equivalence, but it does not by itself parameterize all points of \(\mathscr X\).
The right Gaussian reduction word is still required to coordinatize a coset.

This is why “one cusp fraction + finite datum” is too small as a literal global parameterization of all forms.

---

## 4. Exact automorphism group

Put
\[
D=\operatorname{diag}(1,-2),
\qquad
R=\begin{pmatrix}1-i&1\\-i&0\end{pmatrix}.
\]
Then
\[
\boxed{R^*DR=H_{\rm can}.}
\]

### 4.1 Complete algebraic parameterization over \(\mathbb Z[i]\)

For \(\delta\in\mu_4\), every automorphism of \(D\) with determinant \(\delta\) is uniquely
\[
A(a,c;\delta)=
\begin{pmatrix}
a&2\delta\bar c\\
c&\delta\bar a
\end{pmatrix},
\]
where
\[
a,c\in\mathbb Z[i],
\qquad
|a|^2-2|c|^2=1.
\]
Conversely every such matrix preserves \(D\).

Thus determinant gives a split exact sequence
\[
1\to SU(D,\mathbb Z[i])
\to U(D,\mathbb Z[i])
\to\mu_4\to1.
\]

### 4.2 Special unitary part as an explicit level-4 modular subgroup

Let
\[
C=
\begin{pmatrix}
1+i&-1+i\\
1&-i
\end{pmatrix}.
\]
Then
\[
C^*DC=4i
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

For
\[
g=\begin{pmatrix}p&q\\r&s\end{pmatrix}\in SL_2(\mathbb Q),
\]
the map
\[
\Phi(g)=CgC^{-1}
\]
lands in \(SU(D,\mathbb Q(i))\).

The integral image is exactly
\[
\Gamma_*=
\left\{
\begin{pmatrix}p&q\\r&s\end{pmatrix}\in SL_2(\mathbb Z):
\begin{array}{l}
p\equiv s\pmod2,\\
q\equiv r\pmod2,\\
p-s\equiv q+r\pmod4
\end{array}
\right\}.
\]

Conversely, if
\[
a=x+iy,\qquad c=m+in,
\]
then
\[
C^{-1}
\begin{pmatrix}a&2\bar c\\c&\bar a\end{pmatrix}
C
=
\begin{pmatrix}
m-n+x&-m-n-y\\
-m-n+y&-m+n+x
\end{pmatrix}\in SL_2(\mathbb Z).
\]

Reduction modulo \(4\) gives an image of size \(8\) inside
\(|SL_2(\mathbb Z/4)|=48\), hence
\[
\boxed{[SL_2(\mathbb Z):\Gamma_*]=6.}
\]

A Schreier generating set collapses to
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
\[
E=T^2ST^{-2}
=\begin{pmatrix}2&-5\\1&-2\end{pmatrix},
\]
\[
P=T^4
=\begin{pmatrix}1&4\\0&1\end{pmatrix}.
\]

Projectively,
\[
\boxed{\bar\Gamma_*\cong C_2*C_2*\mathbb Z.}
\]
Its two cusps have widths \(4\) and \(2\).

### 4.3 Full projective group

A determinant-\(i\) unitary element induces projectively
\[
K=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]
Set
\[
L=\begin{pmatrix}1&-5\\1&-3\end{pmatrix}.
\]
Then
\[
K^2=-2S,\qquad
L^2=-2E,\qquad
KL=2T^{-4}.
\]
Therefore \(K,L\) have projective order \(4\) and their product is parabolic.

In the original \(H_{\rm can}\) coordinates one may take the exact integral generators
\[
\boxed{
\kappa=
\begin{pmatrix}
i&0\\
-2i&1
\end{pmatrix},
\qquad
\lambda=
\begin{pmatrix}
1&-1+i\\
2i&-2-i
\end{pmatrix}.
}
\]
They satisfy
\[
\kappa^*H_{\rm can}\kappa=H_{\rm can},
\quad
\lambda^*H_{\rm can}\lambda=H_{\rm can},
\]
\[
\kappa^4=\lambda^4=I,
\]
and
\[
\boxed{
\kappa\lambda
=i
\begin{pmatrix}
1&-(1-i)\\
0&1
\end{pmatrix}
=iP_{-1}.
}
\]

Hence
\[
\boxed{
\operatorname{PAut}(H_{\rm can})
=\langle\bar\kappa,\bar\lambda
\mid \bar\kappa^4=\bar\lambda^4=1\rangle
\cong C_4*C_4.
}
\]

The scalar center \(\mu_4 I\) intersects this projective lift trivially, so
\[
\boxed{
\operatorname{Aut}(H_{\rm can})
\cong \mu_4\times(C_4*C_4).
}
\]

---

## 5. Fundamental domain and cusp count

The projective group has signature
\[
\boxed{(0;4,4,\infty)}.
\]
It has exactly one cusp.

In the upper-half-plane modular coordinate:

- \(K\) fixes \(i\);
- \(L\) fixes \(2+i\);
- \(KL\) fixes \(\infty\).

The Coxeter seed triangle has vertices
\[
\boxed{i,\quad 2+i,\quad\infty}
\]
and angles
\[
\pi/4,\quad\pi/4,\quad0.
\]
It is described exactly by
\[
0\le\Re z\le2,
\qquad
|z-1|\ge\sqrt2.
\]
The orientation-preserving fundamental region is two adjacent copies of this triangle.

Thus:

`CLASSICAL_MODULAR_GROUP_IDENTIFICATION=PROVED`

`NUMBER_OF_CUSPS=1`

`AUTOMORPHISM_PRESENTATION=PROVED`

---

## 6. Full cusp stabilizer

Directly in \(H_{\rm can}\) coordinates, an automorphism stabilizing the isotropic line \([e_1]\) must have the form
\[
\begin{pmatrix}
\varepsilon&b\\0&\varepsilon
\end{pmatrix},
\qquad \varepsilon\in\mu_4.
\]
The norm condition forces
\[
b=\varepsilon n(1-i),
\qquad n\in\mathbb Z.
\]
Therefore
\[
\boxed{
\operatorname{Stab}_\Gamma([e_1])
=
\{\varepsilon P_n:\varepsilon\in\mu_4,n\in\mathbb Z\}.
}
\]
So the R10 parabolic is not merely a subgroup: projectively it is the full cusp stabilizer.

---

## 7. Exact power-ten closeness and cusp annulus

Let
\[
a=D_+,\qquad c=D_-.
\]
Put
\[
\varepsilon=\frac{a-c}{a+c}
=\frac{B}{2KG}.
\]
R10 gives
\[
0<\varepsilon\le31/200<1/6.
\]
Hence
\[
\frac ca=\frac{1-\varepsilon}{1+\varepsilon}
\ge\frac{169}{231}
>\frac57.
\]

Since
\[
|z|^2=ac+2,
\]
we obtain
\[
\frac{|z|^2}{a^2}
=\frac ca+\frac2{a^2}
>\frac57,
\]
so
\[
|z/a|>\sqrt{5/7}.
\]

For the upper bound,
\[
|z|^2<a^2
\iff
a(a-c)>2.
\]
But
\[
a-c=2uB,
\qquad
a=uC_+,
\]
so
\[
a(a-c)=2u^2BC_+>2.
\]
Thus
\[
\boxed{\sqrt{5/7}<|z/a|<1.}
\]

---

## 8. First cusp digit theorem

Choose the canonical nearest Gaussian integer
\[
n\in\mathbb Z[i]
\]
to
\[
\tau=z/a.
\]
Because \(|\tau|<1\), each component of \(n\) lies in
\(\{-1,0,1\}\).

If \(n=0\), the centered-square Voronoi condition gives
\[
|\tau|\le1/\sqrt2,
\]
contradicting
\[
|\tau|>\sqrt{5/7}>1/\sqrt2.
\]
Therefore
\[
n\ne0.
\]

The eight raw possibilities are
\[
\pm1,\ \pm i,\ \pm1\pm i.
\]
Gaussian units act transitively on the four norm-one digits and separately on the four norm-two digits. Hence there are exactly two symmetry shells:
\[
\boxed{N(n)=1}
\qquad\text{or}\qquad
\boxed{N(n)=2}.
\]

No eight-way arithmetic branch is introduced.

---

## 9. Exact shear and One-Step Cusp Entrance Theorem

Set
\[
T_n=
\begin{pmatrix}1&-n\\0&1\end{pmatrix}.
\]
Then
\[
T_n^*
\begin{pmatrix}a&z\\\bar z&c\end{pmatrix}
T_n
=
\begin{pmatrix}
a&r\\
\bar r&c'
\end{pmatrix},
\]
where
\[
r=z-an,
\]
\[
c'=c-2\Re(\bar nz)+a|n|^2.
\]
Determinant \(-2\) gives the stronger formula
\[
\boxed{
c'=\frac{|r|^2-2}{a}.
}
\]

Nearest-Gaussian centering gives
\[
|r|^2\le a^2/2.
\]
If \(a>2\),
\[
c'>-1.
\]
Since \(c'\in\mathbb Z\),
\[
c'\ge0.
\]
Also
\[
c'\le a/2-2/a<a/2.
\]
Thus
\[
\boxed{0\le c'<a/2.}
\]

This proves the requested **One-Step Cusp Entrance Theorem**.

---

## 10. Iterated Gaussian Euclidean reduction

If \(c'>0\), swap coordinates. The new positive pivot is
\[
a_1=c'<a/2.
\]
Repeat.

Every nonterminal bulk step satisfies
\[
1\le a_{j+1}<a_j/2.
\]
Hence after \(m\) positive bulk transitions,
\[
a_m<a_0/2^m.
\]
Thus
\[
m<\log_2 a_0.
\]
Including the terminal small-pivot normalization gives the safe exact bound
\[
\boxed{\text{number of nearest/swap stages}\le\lceil\log_2 a_0\rceil.}
\]

### Terminal \(a=1\)

Since \(z\in\mathbb Z[i]\), choose \(n=z\). Then
\[
H\sim\operatorname{diag}(1,-2),
\]
which is carried to \(H_{\rm can}\) by the fixed R10 transporter.

### Terminal \(a=2\)

Centered \(r\) has \(|r|^2\le2\), while integrality of
\[
c'=(|r|^2-2)/2
\]
forces
\[
|r|^2\in\{0,2\}.
\]
Thus \(c'\in\{-1,0\}\).

If \(c'=-1\), the form is \(\operatorname{diag}(2,-1)\), and
\[
\begin{pmatrix}1&1\\1&2\end{pmatrix}^*
\operatorname{diag}(2,-1)
\begin{pmatrix}1&1\\1&2\end{pmatrix}
=
\operatorname{diag}(1,-2).
\]

If \(c'=0\), see the cusp terminal below.

### Terminal \(c'=0\)

Then
\[
|r|^2=2.
\]
Normalize \(r\) by a Gaussian unit to \(1+i\). Primitivity forces the remaining diagonal to be odd. A swap, a unit normalization and one integer parabolic shear reduce it to \(H_{\rm can}\).

Therefore the positive-pivot Euclidean algorithm terminates constructively at \(H_{\rm can}\). All actual power-ten split forms lie in this sector.

---

## 11. Cusp coordinate and what is / is not a standard Gaussian continued fraction

R10 gives an integral isotropic vector
\[
e=(1+i-z,a).
\]
Before primitive scaling define
\[
\boxed{
\xi(H)=\frac{1+i-z}{a}.
}
\]

For one shear+swap reduction matrix
\[
Q_n=T_nW=
\begin{pmatrix}-n&1\\1&0\end{pmatrix},
\]
the isotropic vector coordinates transform by \(Q_n^{-1}\), hence
\[
\boxed{
\xi_{j+1}=\frac1{\xi_j+n_j}.
}
\]

So the reduction word is exactly a continued-fraction-type Möbius expansion of one isotropic coordinate.

However the digit-selection rule is
\[
n_j=\operatorname{Near}(z_j/a_j)
=\operatorname{Near}\!\left(\frac{1+i}{a_j}-\xi_j\right),
\]
not the standard rule \(n_j=\operatorname{Near}(-\xi_j)\).

Therefore:

`GAUSSIAN_CF_MATCHES_REDUCTION=PROVED` **for the determinant-2 Hermitian continued fraction defined above**;

`STANDARD_NEAREST_GAUSSIAN_CF_MATCH=PARTIAL`.

This distinction is exact and prevents falsely identifying the reduction with a standard Hurwitz Gaussian CF without the height variable.

---

## 12. Gaussian continuants

Let
\[
R(n)=\begin{pmatrix}-n&1\\1&0\end{pmatrix}.
\]
Define
\[
M_j=R(n_0)\cdots R(n_{j-1}).
\]
Put
\[
P_{-1}=0,\quad P_0=1,
\]
\[
Q_{-1}=1,\quad Q_0=0,
\]
and for either sequence \(X=P,Q\),
\[
\boxed{
X_{j+1}=-n_jX_j+X_{j-1}.
}
\]
Then
\[
\boxed{
M_j=
\begin{pmatrix}
P_j&P_{j-1}\\
Q_j&Q_{j-1}
\end{pmatrix}.
}
\]

This is the exact Gaussian continuant encoding of the reduction word.

---

## 13. Diagonal map in continuant coordinates

Let the complete canonical reduction transformation, including the finite terminal normalization, be \(V\), so
\[
V^*HV=H_{\rm can}.
\]
Then
\[
H=(V^{-1})^*H_{\rm can}V^{-1}.
\]
Write
\[
V^{-1}=
\begin{pmatrix}p&q\\r&s\end{pmatrix}.
\]
Define
\[
\boxed{
\Phi(x,y)=|y|^2+
2\Re\!\bigl((1+i)\bar x\,y\bigr).
}
\]
Then
\[
\boxed{D_+=\Phi(p,r),}
\qquad
\boxed{D_-=\Phi(q,s).}
\]
The four entries \(p,q,r,s\) are explicit Gaussian continuants of the reduction word, modified only by the fixed/terminal normalization matrix.

Thus the power-ten intersection is exactly the pair of continuant-height equations
\[
\boxed{
\Phi(p,r)=u(2KG+B),
}
\]
\[
\boxed{
\Phi(q,s)=u(2KG-B).
}
\]
Equivalently,
\[
\Phi(p,r)+\Phi(q,s)=4uKG,
\]
\[
\Phi(p,r)-\Phi(q,s)=2uB.
\]

This is the new global frontier.

---

## 14. Level-u isotropic basis audit

Modulo \(u\), actual diagonals vanish:
\[
D_+\equiv D_-\equiv0\pmod u.
\]
For odd \(u\), take
\[
V=
\begin{pmatrix}
i&-i\\
1&1
\end{pmatrix}.
\]
Its two columns satisfy
\[
H_0((i,1),(i,1))=0,
\]
\[
H_0((-i,1),(-i,1))=0,
\]
and
\[
\det V=2i.
\]
Since \(u\) is odd, \(2i\) is a unit modulo \(u\).

Therefore every odd level has an explicit isotropic unimodular basis:
\[
\boxed{
\texttt{LEVEL_u_ISOTROPIC_BASIS_OBSTRUCTION=FALSE}.
}
\]
No Hecke restriction survives at this level.

---

## 15. First-shell parity refinement

Because actual \(a,c\) are odd,
\[
|z|^2=ac+2
\]
is odd, so \(z\not\equiv0\pmod{1+i}\).

If \(N(n)=1\), then \(n\) is a unit and
\[
r=z-an\equiv0\pmod{1+i},
\]
so \(|r|^2\) and hence \(c'\) are even.

If \(N(n)=2\), then \(n\equiv0\pmod{1+i}\), so
\[
r\equiv z\not\equiv0\pmod{1+i},
\]
and \(c'\) is odd.

Thus
\[
N(n)=1\Rightarrow c'\equiv0\pmod2,
\]
\[
N(n)=2\Rightarrow c'\equiv1\pmod2.
\]

Neither parity is contradictory. Both shells remain structural possibilities; no shell is falsely killed.

---

## 16. Fundamental-domain rigidity: exact status

The automorphism group itself is now completely controlled:

\[
\boxed{\operatorname{PAut}(H_{\rm can})\cong C_4*C_4}
\]
with one cusp.

The actual power-ten section enters the Euclidean reduction through only two unitary shells and after one step reaches
\[
0\le c'<a/2.
\]

What is **not** proved is that the subsequent reduction word lies in one parabolic family or one geodesic. The first-step closeness is consumed after the first halving; no invariant found in R11 forces all later digits to remain parabolic.

Therefore:

`FULL_ONE_PARAMETER_PARABOLIC_RIGIDITY=UNRESOLVED`

but

`ONE_CUSP_TWO_GATE_RIGIDITY=PROVED`.

The exact next object is no longer “unknown cusp rigidity”; it is:

\[
\boxed{
\textbf{one canonical determinant-2 Hermitian reduction word}
\times
\textbf{one pair of quadratic continuant-height equations}.
}
\]

---

## 17. Fifteen required answers

### Q1
Yes.
\[
\boxed{\text{split q>1 locus}
=\mathscr D(\Gamma\backslash GL_2(\mathbb Z[i])).}
\]

### Q2
Exactly:
\[
\boxed{
\operatorname{Aut}(H_{\rm can})
\cong\mu_4\times(C_4*C_4).
}
\]
Projectively it is the one-cusp \((4,4,\infty)\) group.

### Q3
Yes. An exact Coxeter seed has vertices
\[
i,\ 2+i,\ \infty
\]
with angles \(\pi/4,\pi/4,0\); the orientation-preserving domain is its double.

### Q4
Yes:
\[
\boxed{\sqrt{5/7}<|z/D_+|<1.}
\]

### Q5
Yes. Exactly two Gaussian-unit shells:
\[
\boxed{N(n)=1,\quad N(n)=2.}
\]

### Q6
Yes:
\[
\boxed{0\le c'<D_+/2.}
\]

### Q7
Yes for the positive-pivot sector, which contains every actual split power-ten state. Bulk height halves strictly; terminal pivots \(1,2\) and \(c'=0\) are exactly normalized.

### Q8
Yes in the precise determinant-2 Hermitian sense:
\[
\xi_{j+1}=1/(\xi_j+n_j).
\]
It is not literally the standard nearest-Gaussian CF because digit selection also uses the current height \(a_j\).

### Q9
Yes, up to scalar units:
\[
\boxed{\operatorname{Stab}([e_1])=\{\varepsilon P_n\}.}
\]

### Q10
The full projective group has
\[
\boxed{1\text{ cusp}}
\]
and two order-4 elliptic generators. Compact-core generators are necessary; the group is not purely parabolic.

### Q11
Yes. The level-\(u\) condition is automatic for every odd \(u\).

### Q12
Not applicable: no genuine Hecke restriction remains at this level.

### Q13
If
\[
V^{-1}=\begin{pmatrix}p&q\\r&s\end{pmatrix},
\]
with entries given by Gaussian continuants, then
\[
\boxed{
D_+=|r|^2+2\Re((1+i)\bar p r),
}
\]
\[
\boxed{
D_-=|s|^2+2\Re((1+i)\bar q s).
}
\]

### Q14
It is proved that all actual split states enter the **same unique cusp** through two fixed first-shell gates. A finite union of complete geodesic/parabolic families is not yet proved.

### Q15
Yes, at the required minimum compression level. The q>1 frontier is now
\[
\boxed{
\textbf{one canonical terminating Hermitian reduction word}
}
\]
subject to
\[
\boxed{
\textbf{two explicit quadratic continuant-height equations}
}
\]
and one two-shell boundary condition. It is strictly sharper than “one Hermitian orbit”.

---

## 18. Certificate summary

```text
GAUSSIAN_UNITARY_GROUP_IDENTIFICATION=PROVED
CLASSICAL_MODULAR_GROUP_IDENTIFICATION=PROVED
AUTOMORPHISM_PRESENTATION=PROVED
FULL_AUTOMORPHISM_GENERATORS=central iI + kappa + lambda
NUMBER_OF_CUSPS=1

ACTUAL_CLOSE_RATIO_GT_5_OVER_7=PASS
ACTUAL_CLOSE_RATIO_LT_1=PASS
CUSP_ANNULUS_LOWER=PASS
CUSP_ANNULUS_UPPER=PASS
NEAREST_GAUSSIAN_n_NONZERO=PASS
FIRST_DIGIT_EIGHT_SET=PASS
FIRST_DIGIT_SYMMETRY_TYPES=2
ONE_STEP_CUSP_ENTRANCE=PROVED

GAUSSIAN_EUCLIDEAN_REDUCTION=PROVED_FOR_ACTUAL_POSITIVE_SECTOR
REDUCTION_STRICTLY_DECREASING=TRUE
REDUCTION_TERMINATES=TRUE
REDUCTION_LENGTH_BOUND<=ceil(log2(DPLUS))
TERMINAL_FORMS=a=1; a=2; c'=0
TERMINAL_FORM_EQUALS_HCAN=PROVED

INTEGRAL_ISOTROPIC_VECTOR_FORMULA=PASS
CUSP_COORDINATE=(1+i-z)/a
HERMITIAN_CF_MATCHES_REDUCTION=PROVED
STANDARD_NEAREST_GAUSSIAN_CF_MATCH=PARTIAL
CUSP_STABILIZER={epsilon P_n}

LEVEL_u_ISOTROPIC_BASIS_CONDITION=PROVED
LEVEL_u_ISOTROPIC_BASIS_OBSTRUCTION=FALSE
HECKE_INTERPRETATION=NOT_APPLICABLE

POWER_TEN_SECTION_FIRST_SHELL_TYPES=2
NORM1_SHELL_STATUS=OPEN
NORM2_SHELL_STATUS=OPEN
EIGHT_RAW_DIGITS_USED_AS_BRANCHES=FALSE

DIAGONAL_MAP_IN_CONTINUANT_COORDINATES=PROVED
RATIONAL_CONIC_SOLUBILITY_AS_J2_KILLER=NOT_RETIRED
q_GT_1_CLOSED=FALSE
J2=OPEN
```

---

## 19. Next unique object

R11 has exhausted the class-number and automorphism-group questions. The next round should not further classify the group.

The unique global object is now:

\[
\boxed{
\textbf{Determinant-2 Hermitian Continuant Height Equation}
\times
\textbf{Power-of-Ten Toric Diagonal Section}.
}
\]

More explicitly:
\[
\boxed{
\Phi(p,r)+\Phi(q,s)=4uKG,
\qquad
\Phi(p,r)-\Phi(q,s)=2uB,
}
\]
where \((p,q,r,s)\) are constrained by one canonical terminating Gaussian reduction word whose first gate has norm \(1\) or \(2\).

No return to prime-by-prime sum-of-two-squares analysis is needed.

\[
\boxed{\textbf{J2 OPEN}.}
