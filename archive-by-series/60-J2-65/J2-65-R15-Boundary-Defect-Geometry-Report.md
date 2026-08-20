# J2-65-R15 — LOW-Divisor Blow-Up × Boundary-Defect Discriminant Lift

**Scope:** Strict Layer — A1-only — Exact Resonance `R=0` — `J=2` — `q>1` only  
**Round:** 65 第十五轮 / A1 统一终端线第四十轮  
**Status:** **J2 OPEN**

## 1. Executive verdict

R15 achieves the requested source-preserving recompression.

The continuous LOW clearance is replaced exactly by the integer coordinate
\[
h=10x-Aa>0,
\]
with
\[
\kappa=\min\!\left(\frac9{10},\frac{h}{Aa+h}\right).
\]
Integrality gives
\[
\boxed{\kappa\ge\frac1{Aa+1}},
\qquad
\boxed{G\le j(10u)\,a(Aa+1)}
\]
for every multiplier-failing primitive ray.

The LOW map has determinant \(10\). If
\[
M=\frac{G}{\gcd(G,2d(q+4))},
\]
then the transformed lattice has
\[
\boxed{[\mathbb Z^3:\Lambda_\partial]=10M},
\]
with Smith factors
\[
\boxed{(1,\gcd(M,10),10M/\gcd(M,10))}.
\]
Thus the blow-up introduces only the fixed decimal index ten.

The source ternary cone becomes an exact primitive integral quadratic form
\[
Q_\partial(Z,a,h)=100F_{\rm src}\!\left(Z,a,\frac{Aa+h}{10}\right).
\]
Writing
\[
Q_\partial=\mathcal AZ^2+\mathcal B(a,h)Z+\mathcal C(a,h)
\]
gives
\[
\boxed{Y_\partial^2=\mathfrak D_\partial(a,h)
=d_0a^2+d_1ah+d_2h^2},
\qquad
Y_\partial=2\mathcal AZ+\mathcal B.
\]

At \(h=0\),
\[
\boxed{d_0=-400q^6\mathfrak D_{\rm LB}}.
\]
Hence the R14 LOW-boundary polynomial is not a separate terminal object; it is the boundary fibre of this binary discriminant form.

The binary-form discriminant satisfies
\[
\boxed{\Delta_\partial=-64\mathcal A\det\operatorname{Gram}(Q_\partial)}
\]
and, exactly,
\[
\boxed{
\Delta_\partial=
-256000000G^5q^{14}(G+1)^2(2G+q+2)
(2G^2+Gq+2G+2q)\Delta_{\rm fib}.
}
\]
Thus the R7 conic discriminant and the R14 LOW incidence are unified by one source-preserving Schur complement.

Completing the binary form yields
\[
\boxed{
R_\partial^2-4d_0Y_\partial^2
=\Delta_\partial h^2,
\qquad
R_\partial=2d_0a+d_1h.
}
\]
The \(h^2\) factor is deliberately retained.

The most important geometric verdict is negative but decisive:

\[
\boxed{\mathfrak D_{\rm LB}<0}
\]
on the entire actual power-of-ten base \(G\ge10,\ K\ge10,\ q\le G+1\). Therefore the LOW divisor has two distinct real intersections with the source conic. Moreover the upper intersection satisfies the inherited strict W inequalities, so

\[
\boxed{0\in\overline{\mathscr I_\eta}},
\qquad
\boxed{\text{UNIFORM PROJECTIVE CLEARANCE=FALSE}}.
\]

Thus pure real/source-quadric height geometry cannot close \(q>1\).

## 2. Integral clearance quantization

Since
\[
10x=Aa+h,
\qquad
\chi=\frac{x}{Aa}
=\frac1{10}+\frac{h}{10Aa},
\]
we have
\[
\frac1{10\chi}=\frac{Aa}{Aa+h}.
\]
Therefore
\[
\boxed{
\kappa
=\min\!\left(\frac9{10},\frac{h}{Aa+h}\right).
}
\]

For \(h\ge1\),
\[
\frac{h}{Aa+h}\ge\frac1{Aa+1},
\qquad
\frac9{10}\ge\frac1{Aa+1},
\]
so
\[
\boxed{\kappa\ge\frac1{Aa+1}}.
\]
Combining with R14 boundary transference,
\[
\frac Ga\kappa\le j(10u),
\]
gives
\[
\boxed{G\le j(10u)a(Aa+1)}.
\]

## 3. Boundary lattice

The coordinate change is
\[
T_\partial=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&-A&10
\end{pmatrix},
\qquad
\det T_\partial=10.
\]

R13 uses
\[
Z=Mw_1+\rho w_2,\qquad a=w_2,\qquad x=w_3.
\]
Thus a boundary basis is
\[
(M,0,0),\qquad(\rho,1,-A),\qquad(0,0,10).
\]

Equivalently,
\[
\Lambda_\partial=
\{(Z,a,h)\in\mathbb Z^3:
G\mid d(h_ZZ+h_aa),\quad Aa+h\in10\mathbb Z\}.
\]
The inverse is exactly
\[
x=\frac{Aa+h}{10}.
\]
Therefore the transformation preserves the source lattice integrally in both directions.

## 4. Binary discriminant lift and converse

The exact identity is
\[
Y_\partial^2-\mathfrak D_\partial
=4\mathcal A Q_\partial.
\]
So every source point gives a discriminant square.

The naked square equation is not falsely declared sufficient. The converse also requires
\[
Y_\partial-\mathcal B(a,h)\in2\mathcal A\mathbb Z
\]
and the reconstructed point to lie in \(\Lambda_\partial\). Hence
`BOUNDARY_DISCRIMINANT_CONVERSE=SQUARE_PLUS_FIXED_LATTICE_CONGRUENCE`.

The universal polynomial content of \(Y_\partial\) is exactly
\[
\boxed{40q^2}.
\]
No moving-prime split is introduced.

## 5. Schur complement and source-preserving norm

With the Gram convention \(\operatorname{Gram}(Q)=\operatorname{Hess}(Q)/2\),
\[
\det\operatorname{Gram}(Q_\partial)
=
40000G^2q^{10}(G+1)^2(2G+q+2)\Delta_{\rm fib}.
\]
Then
\[
\Delta_\partial=-64\mathcal A\det\operatorname{Gram}(Q_\partial).
\]

The completed-square identity
\[
R_\partial^2-4d_0Y_\partial^2=\Delta_\partial h^2
\]
is source-preserving because \(h\) is not divided out.

Since
\[
d_0=(20q^3)^2(-\mathfrak D_{\rm LB}),
\]
the associated quadratic square class is
\[
[d_0]=[-\mathfrak D_{\rm LB}].
\]
It is genuinely moving under specialization.

## 6. Power-of-ten LOW sign theorem

As a polynomial in \(K\),
\[
\mathfrak D_{\rm LB}
=
-4G^6(G+1)^2(2G+q+2)^2K^2
-80G^3q(G+1)^2(2G+q+2)K
+K_0(G,q).
\]
Thus it is strictly decreasing for \(K>0\).

On the actual base,
\[
G\ge10,\qquad K\ge10,\qquad q\le G+1\le\frac{11}{10}G.
\]
At \(K=10\), retain the negative monomial \(-1584G^{10}\) and discard all other negative monomials. Bounding every positive monomial by the two inequalities above gives total positive contribution at most
\[
\frac{9588271}{625000}G^{10}.
\]
Hence
\[
\mathfrak D_{\rm LB}(G,10,q)
\le
-\frac{980411729}{625000}G^{10}<0.
\]
Monotonicity gives
\[
\boxed{\mathfrak D_{\rm LB}<0}
\]
for every actual \(K\ge10\).

Therefore \(d_0>0\) and the LOW boundary has two distinct real projective source-conic intersections.

## 7. Exact projection to eta

Put
\[
\eta=\frac ha,\qquad z=\frac Za.
\]
Then
\[
\frac xa=\frac{A+\eta}{10}.
\]

The inherited projective W gates become three lower bounds:
\[
s>0\iff z>z_s,
\qquad
ct-s>0\iff z>z_{ct},
\qquad
UP\iff z>z_{UP}(\eta).
\]
Their exact rational expressions are in `J2-65-R15-WProjection.tsv`.

The source conic is
\[
\mathcal A z^2+B_\eta z+C_\eta=0
\]
with
\[
D_\eta=d_0+d_1\eta+d_2\eta^2.
\]
Since \(\mathcal A>0\), let
\[
z_+(\eta)=\frac{-B_\eta+\sqrt{D_\eta}}{2\mathcal A}.
\]
Then
\[
\boxed{
\mathscr I_\eta=
\{\eta>0:
D_\eta\ge0,\ 
z_+(\eta)>\max(z_s,z_{ct},z_{UP}(\eta))\}.
}
\]
This is a fixed-complexity semialgebraic set. A uniform crude component bound is at most 9.

## 8. eta=0 is in the admissible closure

First,
\[
z_s-z_{ct}
=
\frac{Gc^2}{q^4(Gc-2q^2(q+4))}>0.
\]

At \(\eta=0\), \(D_0=d_0>0\). For the two relevant W walls one obtains
\[
Q_z(z_s,0)<0,\qquad Q_z(z_{UP}(0),0)<0
\]
uniformly on the actual power-ten base.

The first sign follows because its positive \(K\)-coefficient makes the controlling expression minimal at \(K=10\), and the total normalized negative budget there is
\[
\frac{40313}{100000}<2.
\]
The second controlling polynomial is decreasing in \(K\); at \(K=10\), its positive budget is
\[
\frac{1331}{125}<1592.
\]

Hence both W walls lie strictly left of the conic vertex. The upper root lies strictly right of the vertex, so it satisfies all inherited strict W inequalities.

Thus
\[
\boxed{\eta=0\text{ is a genuine W-admissible real boundary point}}
\]
and
\[
\boxed{\text{UNIFORM PROJECTIVE CLEARANCE=FALSE}}.
\]

## 9. Real, rational, and primitive-lattice LOW incidence

**Real:** yes. There are two distinct real boundary points; the upper one is W-admissible.

**Rational:** a boundary ray is rational exactly when \(d_0\) is a rational square, equivalently when \(-\mathfrak D_{\rm LB}\) is a square at that specialization, with the W inequality selecting the admissible root.

**Primitive lattice:** any rational source ray can be multiplied into the finite-index source lattice and then divided to its canonical primitive lattice generator. Thus projective primitive-lattice equality is equivalent to rational boundary-ray existence. The moving square-value question remains unresolved; no prime-by-prime square test is used.

## 10. Thin-shell population

Condition on a rationally split fibre. Then the source conic is \(\mathbb P^1\) over \(\mathbb Q\), so rational points are dense on its real locus.

The W-admissible boundary point is smooth because \(d_0>0\). Therefore there are rational W-admissible points with
\[
\eta>0,\qquad \eta\to0.
\]
Scaling into the fixed source lattice and taking primitive generators yields infinitely many distinct primitive rays. Their height \(a\) must be unbounded.

Consequently the necessary shell
\[
G\le j(10u)a(Aa+1)
\]
is eventually satisfied along such a sequence.

This proves that the **necessary source/norm/height shell is genuinely populated** on split fibres. It does *not* prove actual multiplier failure, because boundary transference is necessary rather than sufficient.

Hence the correct negative strategic theorem is
\[
\boxed{
\text{pure source-quadric / real-height geometry cannot close }q>1.
}
\]

## 11. Answers to the fifteen required questions

1. **Q1:** Yes. \(h=10x-Aa\) exactly encodes LOW contact.
2. **Q2:** Yes. \(\kappa=\min(9/10,h/(Aa+h))\).
3. **Q3:** Yes. \(\kappa\ge1/(Aa+1)\).
4. **Q4:** Yes. \(G\le j(10u)a(Aa+1)\) for every multiplier-failing ray.
5. **Q5:** Index \(10M\), \(M=G/\gcd(G,2d(q+4))\); SNF \((1,\gcd(M,10),10M/\gcd(M,10))\).
6. **Q6:** Yes. The ternary quadric remains exactly integrally equivalent on \(\Lambda_\partial\).
7. **Q7:** Yes. Eliminating \(Z\) gives one binary homogeneous discriminant-square form; the converse needs the single source-lattice divisibility condition.
8. **Q8:** Yes, exactly: \(d_0=-400q^6\mathfrak D_{\rm LB}\).
9. **Q9:** \(\Delta_\partial=-64\mathcal A\det\operatorname{Gram}(Q_\partial)\), hence an explicit structural factor times R7's \(\Delta_{\rm fib}\).
10. **Q10:** Yes. \(R_\partial^2-4d_0Y_\partial^2=\Delta_\partial h^2\).
11. **Q11:** The W projection is exactly the fixed-complexity set \(\mathscr I_\eta\) above; uniform component bound \(\le9\).
12. **Q12:** **Yes.** \(\eta=0\) lies in the admissible projective closure.
13. **Q13:** Real LOW equality: **yes**, two points and one W-admissible. Rational/primitive equality is controlled by the moving square condition.
14. **Q14:** The necessary thin shell is genuinely populated on rationally split fibres; actual multiplier failure is not thereby proved.
15. **Q15:** Yes, the frontier compresses to
\[
\boxed{
\text{one primitive integral boundary-discriminant/norm cone}
\cap
\text{one quantized height shell}
\cap
\text{power-of-ten base}.
}
\]
It is not empty by pure source geometry.

## 12. Terminal verdict

\[
\boxed{\textbf{J2 OPEN}.}
\]

The next unique global object is
\[
\boxed{
\textbf{Integral Boundary Norm-Lattice Orbit}
\times
\textbf{Quantized Boundary Height}
\times
\textbf{Power-of-Ten Motion}.
}
\]

No ray enumeration, \(h\)-ladder, factorization of \(u\), q=1 reopening, Hermitian reopening, or old cell/tube replay was used.
