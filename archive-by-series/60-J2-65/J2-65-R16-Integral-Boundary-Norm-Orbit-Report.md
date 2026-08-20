# J2-65-R16 — Integral Boundary Norm Orbit Report

**Scope:** Strict Layer — A1-only — Exact Resonance \(R=0\) — \(J=2\) — \(q>1\) only  
**Round:** 65 第十六轮 / A1 统一终端线第四十一轮  
**Status:** **J2 OPEN**

## 0. Executive verdict

R16 achieves the intended arithmetic recompression but does **not** close \(q>1\).

The R15 source-preserving boundary discriminant is converted into one integral quadratic-étale norm lattice. The largest universal polynomial common divisor of the two norm coordinates is exactly

\[
\boxed{C_0=800q^5}.
\]

After this legal descent,

\[
\boxed{
r_0^2-Dv_0^2
=
\bigl(20G^2q^2(G+1)\bigr)^2E_\partial h^2,
}
\]

where

\[
D=-\mathfrak D_{\rm LB}>0,
\qquad
E_\partial=
-G(2G+q+2)(2G^2+Gq+2G+2q)\Delta_{\rm fib}>0.
\]

Any further source-lattice divisibility is retained as one composite gcd \(C_{\rm extra}\); it is not decomposed.

The strongest positive structural theorem of the round is the **double near-square theorem**:

\[
\boxed{-\Delta_{\rm fib}=T^2-\mathcal R_F},
\qquad
T=2KG(G+1),
\]

and

\[
\boxed{D=S_D^2-\mathcal R_D},
\]

with

\[
S_D=
2KG^3(G+1)(2G+q+2)+20q(G+1),
\]

and the exact \(K\)-independent defect

\[
\boxed{
\mathcal R_D=
G(2G+q+2)(2G^2+Gq+2G+2q)
\left(
G^4(2G+q+2)^2+400(G+1)^2
\right).
}
\]

Thus all \(K\)-motion of \(D\) enters through the square centre \(S_D\). Moreover

\[
\boxed{
S_D=G^2(2G+q+2)T+20q(G+1).
}
\]

However the two defects are not the same hidden invariant:

\[
\boxed{\gcd_{\mathbf Q[G,q]}(\mathcal R_D,\mathcal R_F)=1},
\]

and both one-variable resultants are nonzero. Hence the correct verdict is

\[
\boxed{\text{DOUBLE NEAR-SQUARE = TRUE, COMMON DEFECT = FALSE}.}
\]

A second important correction is that \(D>0\) does **not** imply that every specialization defines a real quadratic field. R15 already leaves open the locus where \(D\) is an integer square. The unified arithmetic object is therefore

\[
\boxed{
\mathscr A_D=\mathbf Q[T]/(T^2-D),
}
\]

a quadratic étale algebra: it is a real quadratic field on the nonsquare locus and a split algebra on the square locus.

On nonsplit fibres, the totally positive norm-one unit group has rank one; the subgroup preserving the full source lattice/coset data has finite index, expressed as the kernel of one action on a finite quotient. For fixed base and fixed \(h\), integral source solutions break into finitely many such source-unit orbits. At the ideal-class level the factor \(h^2\) disappears because \((h)^2\) is a principal square, although \(h\) remains essential at the element, lattice, and digit-height levels.

The attempted one-hit theorem does **not** become unconditional. The abstract spacing lemma is proved, but the actual inequality

\[
\Lambda_U>\mathfrak W_{\rm mult}
\]

cannot be derived uniformly. The obstruction is structural: the universal lower bound for units depends on the squarefree field radicand \(D_{\rm sf}\), not on the huge displayed integer \(D\); the split \(D=\square\) locus is not excluded; and R15 proved \(0\in\overline{\mathscr I_\eta}\), so the source shell has no uniform projective clearance that would bound its multiplicative diameter.

Therefore R16 compresses the infinite Pell-type picture to a finite source-unit orbit packet for each fixed base/height, but it does **not** reduce every orbit to one canonical digit representative.

The next global work should not enumerate Pell indices. The surviving object is

\[
\boxed{
\text{K-independent near-square defect packet}
\times
\text{one composite infrastructure phase }S_D\bmod\mathcal R_D
\times
\text{source congruence / digit-height section}
\times
\text{power-of-ten relation }uq=G+1.
}
\]

---

## 1. Exact R15 reload and sign package

R16 uses the R15 identities

\[
Y_\partial^2=d_0a^2+d_1ah+d_2h^2,
\]

\[
R_\partial^2-4d_0Y_\partial^2=\Delta_\partial h^2,
\qquad
R_\partial=2d_0a+d_1h,
\]

with

\[
d_0=-400q^6\mathfrak D_{\rm LB},
\]

and

\[
\Delta_\partial=
-256000000G^5q^{14}(G+1)^2
(2G+q+2)(2G^2+Gq+2G+2q)\Delta_{\rm fib}.
\]

Set

\[
D=-\mathfrak D_{\rm LB}>0.
\]

Then

\[
d_0=(20q^3)^2D,
\qquad
4d_0=(40q^3)^2D.
\]

Define

\[
V=40q^3Y_\partial.
\]

Hence

\[
\boxed{R_\partial^2-DV^2=\Delta_\partial h^2.}
\]

For the RHS set

\[
S_\Delta=16000G^2q^7(G+1)
\]

and

\[
E_\partial=
-G(2G+q+2)(2G^2+Gq+2G+2q)\Delta_{\rm fib}.
\]

Then

\[
\boxed{\Delta_\partial=S_\Delta^2E_\partial.}
\]

### Sign of \(E_\partial\)

Let

\[
\mathcal R_F=
4G^4+4G^3q+8G^3+G^2q^2+8G^2q+4G^2+2Gq^2+4Gq-q^2.
\]

Since \(0<q\le G+1\),

\[
\mathcal R_F
<
3G(G+1)^2(3G+2).
\]

For \(K\ge10\),

\[
T^2=4K^2G^2(G+1)^2\ge400G^2(G+1)^2.
\]

The gap between this lower bound and the displayed upper bound is

\[
G(G+1)^2(391G-6)>0
\qquad(G\ge10).
\]

Thus

\[
-\Delta_{\rm fib}=T^2-\mathcal R_F>0,
\]

so

\[
\boxed{E_\partial>0.}
\]

---

## 2. Maximal universal source-preserving square descent

The norm-coordinate coefficient rows satisfy the exact polynomial-content identities

\[
\gcd_{\rm poly}(\text{coefficients of }R_\partial)=800q^6,
\]

\[
\gcd_{\rm poly}(\text{coefficients of }V)=1600q^5,
\]

and jointly

\[
\boxed{
\gcd_{\rm poly}(\text{coefficients of }R_\partial,V)=800q^5.
}
\]

Therefore the maximal **universal polynomial** common divisor is

\[
\boxed{C_0=800q^5.}
\]

Define

\[
r_0=\frac{R_\partial}{800q^5},
\qquad
v_0=\frac{V}{800q^5}.
\]

Then

\[
\boxed{
r_0^2-Dv_0^2
=
\left(20G^2q^2(G+1)\right)^2E_\partial h^2.
}
\tag{PN0}
\]

No further universal polynomial common divisor remains between the two coordinate rows.

The source lattice can impose extra specialization-dependent divisibility. Let \(B_{N,0}\) be the normalized source norm-lattice basis and let

\[
C_{\rm lat}
=
\gcd(\text{all first/second-coordinate entries of }B_{N,0}).
\]

To avoid any illegal use of accidental square factors in \(E_\partial\), R16 removes only the part certified by the explicit remaining structural square:

\[
\boxed{
C_{\rm extra}
=
\gcd\!\left(C_{\rm lat},\,20G^2q^2(G+1)\right).
}
\]

Then

\[
C_N=800q^5C_{\rm extra},
\qquad
r_N=r_0/C_{\rm extra},
\qquad
v_N=v_0/C_{\rm extra},
\]

and

\[
\boxed{
r_N^2-Dv_N^2
=
E_Nh^2,
}
\]

where

\[
\boxed{
E_N=
\left(
\frac{20G^2q^2(G+1)}{C_{\rm extra}}
\right)^2E_\partial.
}
\]

This is the maximal source-preserving descent certified by the explicit structural square package. No factorization of \(D,E_\partial,h\) is used.

---

## 3. Source norm lattice

R15 gives

\[
\Lambda_\partial=
\{(Z,a,h)\in\mathbf Z^3:
G\mid d(h_ZZ+h_aa),\
Aa+h\equiv0\pmod{10}\}.
\]

Using the R13 basis

\[
Z=Mw_1+\rho w_2,\qquad a=w_2,\qquad x=w_3,
\]

the boundary basis is

\[
(M,0,0),\qquad(\rho,1,-A),\qquad(0,0,10),
\]

where

\[
M=\frac{G}{\gcd(G,2d(q+4))}
\]

and \(\rho\) is the canonical whole-modulus source-basis residue.

After the universal \(800q^5\) descent write

\[
r_0=r_a a+r_hh,
\qquad
v_0=v_ZZ+v_aa+v_hh.
\]

Then an exact basis matrix is

\[
B_{N,0}=
\begin{pmatrix}
0&r_a-Ar_h&10r_h\\
v_ZM&v_Z\rho+v_a-Av_h&10v_h\\
0&-A&10
\end{pmatrix}.
\]

Its determinant is

\[
\boxed{
\det B_{N,0}
=
-100G^3Mq^3(2G^2+Gq+2G+2q)D,
}
\]

so

\[
\boxed{\operatorname{rank}\Lambda_N=3.}
\]

The moving composite gcd loci prevent one polynomial SNF tuple from being valid without forbidden gcd branching. R16 therefore records the exact whole-object SNF by determinantal divisors:

\[
D_1=\gcd(\text{entries}),
\]

\[
D_2=\gcd(\text{all }2\times2\text{ minors}),
\]

\[
D_3=|\det B_{N,0}|,
\]

so

\[
\boxed{
\operatorname{SNF}(\Lambda_N)
=
\left(
D_1,\frac{D_2}{D_1},\frac{D_3}{D_2}
\right).
}
\]

This is exact and avoids a residue/gcd case tree. The HNF is retained as the single whole-object operation \(\operatorname{HNF}(B_{N,0})\).

---

## 4. Double near-square theorem

### Fibre

With

\[
T=2KG(G+1),
\]

R7 gives

\[
\boxed{
-\Delta_{\rm fib}=T^2-\mathcal R_F,
}
\]

where \(\mathcal R_F\) is independent of \(K\).

### Boundary norm radicand

Set

\[
P_D=2G^3(G+1)(2G+q+2),
\qquad
Q_D=20q(G+1),
\]

\[
S_D=P_DK+Q_D.
\]

Exact completion of the \(K\)-square gives

\[
\boxed{
D=S_D^2-\mathcal R_D,
}
\]

with

\[
\boxed{
\mathcal R_D=
G(2G+q+2)(2G^2+Gq+2G+2q)
\left[
G^4(2G+q+2)^2+400(G+1)^2
\right].
}
\]

In particular

\[
\boxed{\partial_K\mathcal R_D=0.}
\]

The centres satisfy

\[
\boxed{
S_D=G^2(2G+q+2)T+20q(G+1).
}
\]

### Defect relation audit

The polynomial gcd is

\[
\boxed{\gcd(\mathcal R_D,\mathcal R_F)=1.}
\]

The resultant with respect to \(q\) is

\[
256G^4(G+1)^8
\left(
G^8+600G^6-400G^5+10200G^4+40000G^3
+20000G^2-40000G+10000
\right),
\]

which is nonzero.

The resultant with respect to \(G\) is

\[
65536q^{12}
\left(
q^8+29600q^6+99200q^5+66134400q^4+3840000q^3
+5876480000q^2-11269120000q+105474560000
\right),
\]

also nonzero.

A Bézout combination \(s\mathcal R_D+t\mathcal R_F=1\) over \(\mathbf Q(G)[q]\) is generated in `NearSquareDefects.tsv`.

Therefore

\[
\boxed{
\texttt{NEAR\_SQUARE\_DEFECT\_RELATION=NONE\_COMMON\_FACTOR}.
}
\]

No global square-class identification between the two defects is obtained.

---

## 5. Quadratic étale algebra and source order

Because \(D>0\) but \(D=\square\) has not been excluded, the correct whole-family object is

\[
\boxed{
\mathscr A_D=\mathbf Q[T]/(T^2-D).
}
\]

- If \(D\notin\mathbf Q^{\times2}\), then \(\mathscr A_D=\mathbf Q(\sqrt{D_{\rm sf}})\) is a real quadratic field.
- If \(D\in\mathbf Q^{\times2}\), then \(\mathscr A_D\simeq\mathbf Q\times\mathbf Q\).

The ambient coordinate order is

\[
\mathbf Z[\sqrt D],
\qquad
\operatorname{disc}=4D.
\]

It is **not** automatically the maximal order.

The actual source order is defined intrinsically by

\[
\boxed{
\mathcal O_\partial
=
\operatorname{Mult}(\mathfrak L_\partial^{\rm src})
=
\{\alpha\in\mathscr A_D:
\alpha\mathfrak L_\partial^{\rm src}
\subseteq
\mathfrak L_\partial^{\rm src}\}.
}
\]

On the nonsplit locus this is a finite-index order in the maximal real-quadratic order. Its conductor is kept as one composite conductor \(f_\partial\) satisfying

\[
\operatorname{disc}(\mathcal O_\partial)
=
f_\partial^2\operatorname{disc}(\mathcal O_{K_D}).
\]

No numerical squarefree factorization of \(D\) is used.

---

## 6. Source-attached norm elements and finite orbit packets

Define

\[
\xi=r_N+v_N\sqrt D.
\]

Then

\[
\boxed{
N(\xi)=E_Nh^2.
}
\]

The symbol \(\xi\) alone is not the full source condition. It must belong to the source lattice/coset packet carrying:

- the image of \(\Lambda_\partial\);
- \(Aa+h\equiv0\pmod{10}\);
- the discriminant-converse divisibility;
- positivity/W-sector conditions.

Call this packet

\[
\mathfrak L_\partial^{\rm src}.
\]

### Nonsplit unit group

For a real quadratic order,

\[
U_\partial^+
=
\{\varepsilon\in\mathcal O_\partial^\times:
N(\varepsilon)=1,\ \varepsilon,\bar\varepsilon>0\}
\]

is infinite cyclic.

The subgroup preserving all source data is

\[
\boxed{
U_{\rm src}
=
\{\varepsilon\in U_\partial^+:
\varepsilon\mathfrak L_\partial^{\rm src}
=
\mathfrak L_\partial^{\rm src}\}.
}
\]

The source data reduce modulo a finite-index lattice/coset quotient, so the action of \(U_\partial^+\cong\mathbf Z\) has finite image. Hence

\[
\boxed{[U_\partial^+:U_{\rm src}]<\infty.}
\]

If \(\varepsilon_\partial\) generates \(U_\partial^+\), then

\[
[U_\partial^+:U_{\rm src}]
\]

is exactly the order of its image in this one finite automorphism quotient. No modulus factorization or residue tree is required.

### Finiteness of orbit packets

Fix the base and \(h\), and set \(n=E_Nh^2\ne0\). For an integral norm element,

\[
n\mathcal O_\partial\subseteq(\xi)\subseteq\mathcal O_\partial.
\]

Such intermediate ideals correspond to submodule data of the finite module

\[
\mathcal O_\partial/n\mathcal O_\partial,
\]

so there are finitely many possibilities. Generators of the same principal ideal differ by units, and passing from all units to \(U_{\rm src}\) only splits each unit orbit into finitely many suborbits.

Therefore

\[
\boxed{
\text{for fixed base and }h,\text{ source norm solutions form finitely many }U_{\rm src}\text{-orbits}.
}
\]

No Pell recurrence or prime-ideal allocation is used.

On the split étale locus, there is no rank-one Pell dynamics; the fixed-target integral packet is already finite.

---

## 7. Ideal-class core and disappearance of \(h\)

At the ideal level,

\[
(\xi)\overline{(\xi)}
=
(E_N)(h)^2.
\]

The factor \((h)^2\) is a principal square. Consequently it is invisible in the ordinary class group and in the corresponding narrow-class obstruction:

\[
\boxed{
\texttt{h\_CLASS\_GROUP\_DEPENDENCE=NONE}.
}
\]

This does **not** justify dividing \(\xi\) by \(h\). The contact height remains in:

- element integrality;
- source coset;
- digit height;
- W-sector;
- the actual norm target.

Across the power-of-ten family the field/order and \(E_N\) move, so R16 does not obtain a universal nonprincipal core class:

\[
\boxed{
\texttt{BOUNDARY\_NORM\_IDEAL\_CLASS\_OBSTRUCTION=GENUINELY\_MOVING}.
}
\]

Thus ideal classes do not close \(q>1\) in this round.

---

## 8. Near-square infrastructure reduction

The exact identity

\[
\boxed{
(S_D+\sqrt D)(S_D-\sqrt D)=\mathcal R_D
}
\]

gives the canonical near-square infrastructure element. It is not called a fundamental unit because its norm is \(\mathcal R_D\), not \(\pm1\).

Also

\[
\boxed{
S_D-\sqrt D
=
\frac{\mathcal R_D}{S_D+\sqrt D}.
}
\]

For nonsquare \(D\),

\[
\boxed{
\lfloor\sqrt D\rfloor
=
S_D-
\left\lceil
\frac{\mathcal R_D}{S_D+\sqrt D}
\right\rceil.
}
\]

R16 does **not** obtain the stronger adjacent-square identity
\(\lfloor\sqrt D\rfloor=S_D-1\); the defect is relatively small but can be arithmetically much larger than \(S_D\) in absolute size.

The canonical defect ideal/form packet is represented by

\[
\boxed{
\mathfrak I_D=(\mathcal R_D,S_D+\sqrt D).
}
\]

Its dependence on \(K\) is only through

\[
\boxed{S_D\bmod\mathcal R_D}.
\]

Therefore

\[
\boxed{
\texttt{K\_DEPENDENCE\_AFTER\_FIRST\_NEARSQUARE\_REDUCTION=REDUCED}.
}
\]

It is **not** removed: no theorem shows that the power-of-ten update \(K\mapsto10K\) fixes this composite phase.

So there is no Power-of-Ten Infrastructure Stability Theorem yet; there is a weaker but exact **Infrastructure Phase Compression Theorem**.

---

## 9. Unit lower bounds

Let \(d=D_{\rm sf}\) be the squarefree field radicand on a nonsplit specialization. Any nontrivial totally positive norm-one algebraic unit can be written in the maximal order as

\[
\varepsilon=\frac{m+n\sqrt d}{2},
\qquad
n\ne0.
\]

Because \(\bar\varepsilon=\varepsilon^{-1}\),

\[
\varepsilon-\varepsilon^{-1}=n\sqrt d\ge\sqrt d.
\]

Solving the quadratic inequality gives

\[
\boxed{
\varepsilon
\ge
\frac{\sqrt d+\sqrt{d+4}}2
>
\sqrt d.
}
\]

If one separately proves that the relevant unit lies in a full integral \(\mathbf Z[\sqrt d]\) coordinate order, the stronger \(>2\sqrt d\) type bound is available, but R16 does not assume that.

Crucially, without a square-content theorem controlling \(D/D_{\rm sf}\), this does **not** become a lower bound of size \(\sqrt D\).

Hence

\[
\boxed{
\texttt{NEAR\_SQUARE\_REGULATOR\_BOUND=NOT\_OBTAINED}.
}
\]

---

## 10. Digit height as an exact Minkowski shell

R15 gives

\[
a=\frac{R_\partial-d_1h}{2d_0}.
\]

Since \(d_0>0\), the primitive range

\[
1\le a<G
\]

is exactly

\[
\boxed{
2d_0+d_1h
\le
R_\partial
<
2d_0G+d_1h.
}
\]

After division by \(C_N\), this becomes the corresponding interval for \(r_N\).

Let

\[
X=\sigma_+(\xi),
\qquad
Y=\sigma_-(\xi).
\]

Then

\[
XY=E_Nh^2
\]

and

\[
r_N=\frac{X+Y}{2}.
\]

Thus the digit shell is a finite union of monotone arcs of the hyperbola

\[
XY=E_Nh^2
\]

cut by the affine real-part interval, the thin Jacobsthal condition

\[
G\le j(10u)a(Aa+1),
\]

and the inherited W-sector

\[
h/a\in\mathscr I_\eta.
\]

For a positive component \(X,Y>0\), writing \(N_h=E_Nh^2\), the outer real-part cutoff \(r_N<U\) gives the exact multiplicative envelope

\[
U-\sqrt{U^2-N_h}
<
X
<
U+\sqrt{U^2-N_h}
\]

whenever \(U^2>N_h\). Its multiplicative diameter is bounded by

\[
\boxed{
\mathfrak W_{\rm mult}
\le
\frac{U+\sqrt{U^2-N_h}}
{U-\sqrt{U^2-N_h}}.
}
\]

W-sector information may only shrink this shell.

---

## 11. Abstract orbit-spacing theorem and actual failure of comparison

Let a generator of the source stabilizer satisfy

\[
\Lambda_U=\sigma_+(\varepsilon_{\rm src})>1.
\]

Along one orbit,

\[
X_m=\Lambda_U^mX_0.
\]

Therefore:

> **Source Unit-Orbit Height-Section Spacing Lemma.**  
> On any connected monotone shell arc of multiplicative diameter
> \(\mathfrak W_{\rm mult}\), if
> \[
> \Lambda_U>\mathfrak W_{\rm mult},
> \]
> then that source-unit orbit intersects the arc at most once.

This is exact and uses no numerical logarithms.

More generally, define

\[
H_{\rm mult}
=
\max\{m\ge0:\Lambda_U^m\le\mathfrak W_{\rm mult}\}.
\]

Then one monotone arc contains at most \(H_{\rm mult}+1\) points of one orbit. The full positive hyperbola cut by one real-part interval has at most two such monotone arcs, hence a safe fixed-base bound is

\[
\boxed{
\#(\mathcal O\cap\mathscr H)
\le
2(H_{\rm mult}+1).
}
\]

This is finite for each fixed base, but no absolute constant is obtained.

### Why the desired one-hit comparison does not close

R16 cannot prove

\[
\Lambda_U>\mathfrak W_{\rm mult}
\]

uniformly because:

1. \(D\) may be a square, so there may be no real-quadratic rank-one unit dynamics at all;
2. on nonsplit fibres the universal unit lower bound sees \(D_{\rm sf}\), not \(D\);
3. no symbolic theorem bounds the square factor \(D/D_{\rm sf}\);
4. R15 proved \(0\in\overline{\mathscr I_\eta}\), so the W-sector has no uniform clearance that would bound the shell diameter away from the cusp;
5. the source stabilizer has finite but not uniformly bounded index by current data.

Thus

\[
\boxed{
\texttt{ONE\_HIT\_PER\_UNIT\_ORBIT=PARTIAL}.
}
\]

The unique terminal failure category is

\[
\boxed{
\textbf{unit spacing cannot yet control the actual digit-height strip}.
}
\]

---

## 12. Power-of-ten scale audit

The exact degree table is recorded in `J2-65-R16-NearSquareScale.tsv`. The key scales are:

\[
T\sim 2KG^2,
\]

\[
S_D\sim4KG^5,
\]

\[
\mathcal R_D\sim16G^{10},
\]

\[
D\sim16K^2G^{10}
\]

in the \(G\)-leading sense with the other formal variables held.

Thus the near-square defect is \(K\)-independent, while the centre grows linearly with \(K\). This is a genuine large-\(K\) cusp translation phenomenon at the level of the first defect packet.

However it cannot be upgraded to “large \(D\) implies huge source unit spacing”, because the unit group is controlled by the squarefree field radicand/order, not the raw integer \(D\).

---

## 13. General tools extracted

### Tool A — K-Independent Near-Square Defect Lemma

If

\[
D(K)=a^2K^2+2abK+c
\]

and

\[
D(K)=(aK+b)^2-\mathcal R
\]

with \(\partial_K\mathcal R=0\), then the moving parameter enters only through the square centre. The canonical defect ideal

\[
(\mathcal R,aK+b+\sqrt D)
\]

depends on the moving parameter only through the composite phase
\((aK+b)\bmod\mathcal R\).

R16 realizes this exactly with \(a=P_D,b=Q_D,\mathcal R=\mathcal R_D\).

### Tool B — Source-Preserving Norm-Lattice Orbit Lemma

A source-preserving Schur complement
\[
R^2-DV^2=Nh^2
\]
together with a finite-index integral source lattice defines a rank-two norm lattice in a quadratic étale order. For fixed target, solutions split into finitely many orbits under the subgroup of norm-one units stabilizing the source lattice/coset data. Finiteness follows from the finite module \(\mathcal O/n\mathcal O\), not from enumerating Pell recurrences.

### Tool C — Unit-Orbit Height-Section Spacing Lemma

If one embedding of a source-unit orbit is multiplied by \(\Lambda>1\) and the relevant source height section has multiplicative diameter \(W\), then \(\Lambda>W\) implies one hit per connected monotone shell arc. More generally, hit count is bounded by the largest \(m\) with \(\Lambda^m\le W\).

---

# 14. Direct answers to Q1–Q16

## Q1. Primitive integral model

\[
\boxed{
r_N^2-Dv_N^2=E_Nh^2
}
\]

with

\[
D=-\mathfrak D_{\rm LB}
=
S_D^2-\mathcal R_D,
\]

\[
C_0=800q^5,
\]

and \(C_{\rm extra}\) retained as one whole source-lattice gcd against the residual structural square scale. This is the maximal certified source-preserving square descent; no illegal division is used.

## Q2. Norm-coordinate source lattice

Rank \(3\). A full basis is written in `NormLatticeBasis.txt`. Its determinant after universal descent is

\[
100G^3Mq^3(2G^2+Gq+2G+2q)D
\]

in absolute value. Exact SNF is represented by its three determinantal divisors; a single polynomial SNF/HNF tuple would require forbidden branching over moving composite gcd loci.

## Q3. Fibre near-square

Yes:

\[
\boxed{-\Delta_{\rm fib}=T^2-\mathcal R_F},
\qquad
T=2KG(G+1),
\]

and \(\mathcal R_F\) is \(K\)-independent.

## Q4. Boundary near-square

Yes:

\[
\boxed{D=S_D^2-\mathcal R_D},
\]

with the explicit positive factorization

\[
\boxed{
\mathcal R_D=
G(2G+q+2)(2G^2+Gq+2G+2q)
\left[G^4(2G+q+2)^2+400(G+1)^2\right],
}
\]

independent of \(K\).

## Q5. Relation between defects

No common polynomial factor:

\[
\boxed{\gcd(\mathcal R_D,\mathcal R_F)=1}.
\]

Both \(q\)- and \(G\)-resultants are nonzero. A Bézout identity exists and is recorded. No useful global square-class relation was found.

## Q6. Correct arithmetic model

The whole-family object is the quadratic étale algebra

\[
\mathbf Q[T]/(T^2-D),
\]

not unconditionally a field. On nonsquare specializations it is a real quadratic field. The source order is the multiplier ring of the source norm lattice/coset, not automatically the maximal order nor automatically \(\mathbf Z[\sqrt D]\).

## Q7. Source unit subgroup

On nonsplit fibres,

\[
U_{\rm src}
=
\ker\bigl(
U_\partial^+\to
\operatorname{Aut}(\text{finite source quotient/coset datum})
\bigr).
\]

Its index is finite and equals the order of the image of one generator in that finite quotient. No residue enumeration is required.

## Q8. Finite source-unit orbits

Yes, for each fixed base and fixed \(h\). This follows from the finite ideal/submodule packet between \(n\mathcal O\) and \(\mathcal O\), then quotienting generators by the finite-index source-unit stabilizer.

## Q9. Does \(h^2\) disappear in ideal class?

Yes:

\[
\boxed{\texttt{h\_CLASS\_GROUP\_DEPENDENCE=NONE}.}
\]

But \(h\) remains in element integrality, source lattice, W-sector, and digit height.

## Q10. First near-square reduction and \(K\)

\(K\)-dependence is **reduced**, not removed. The defect packet is \(K\)-independent and the canonical defect ideal depends on \(K\) only through

\[
S_D\bmod\mathcal R_D.
\]

The exact first floor still depends on \(K\):

\[
\lfloor\sqrt D\rfloor
=
S_D-\left\lceil\frac{\mathcal R_D}{S_D+\sqrt D}\right\rceil.
\]

## Q11. Uniform unit/regulator bound

A universal nonsplit bound is

\[
\varepsilon\ge
\frac{\sqrt{D_{\rm sf}}+\sqrt{D_{\rm sf}+4}}2
>
\sqrt{D_{\rm sf}}.
\]

No stronger near-square regulator bound in terms of the raw \(D\) is proved.

## Q12. Digit height in Minkowski space

It is the affine real-part strip

\[
2d_0+d_1h\le R_\partial<2d_0G+d_1h,
\]

or its scaled version for \(r_N\), intersected with

\[
XY=E_Nh^2,
\qquad
h/a\in\mathscr I_\eta,
\qquad
G\le j(10u)a(Aa+1).
\]

## Q13. Unit spacing versus strip width

The exact comparison theorem is available, but the actual inequality is unresolved:

\[
\Lambda_U>\mathfrak W_{\rm mult}
\quad\Longrightarrow\quad
\text{one hit per monotone arc}.
\]

Current data do not prove this inequality uniformly.

## Q14. Maximum hits per orbit

For a fixed base,

\[
\boxed{
\#(\mathcal O\cap\mathscr H)
\le
2(H_{\rm mult}+1),
\quad
H_{\rm mult}=
\max\{m:\Lambda_U^m\le\mathfrak W_{\rm mult}\}.
}
\]

No absolute constant, and in particular no global one-hit theorem, is proved.

## Q15. Does the norm orbit close \(q>1\)?

No. It is a successful **recompression mechanism**, not a closing obstruction. As a standalone terminal route it should not be pushed into Pell-index enumeration. The unresolved point is exactly the lack of a uniform source-unit-spacing versus digit-shell comparison.

## Q16. Final R16 frontier

The stronger desired compression

\[
\text{one reduced norm core}
\times
\text{one canonical digit representative}
\times
\text{base}
\]

is **not** proved because one-hit fails globally.

The honest terminal frontier is

\[
\boxed{
\text{one }K\text{-independent boundary defect packet}
\times
\text{one composite phase }S_D\bmod\mathcal R_D
\times
\text{finite source-unit orbit packet}
\times
\text{quantized digit-height shell}
\times
\text{power-of-ten base}.
}
\]

Hence

\[
\boxed{\textbf{J2 OPEN}.}
\]

---

# 15. Next-round discipline

R16 gives no justification for Pell-index enumeration or continued-fraction digit ladders.

Because the ideal-class \(h\)-dependence has disappeared but unit spacing does not close, the strongest unused global interaction is now between:

\[
\boxed{
\mathcal R_D(G,q),\quad
S_D\bmod\mathcal R_D,\quad
uq=G+1,\quad
\text{source congruence / digit shell}.
}
\]

A next round should therefore test whether the cyclotomic relation \(uq=G+1\) collapses the single infrastructure phase or the reduced defect packet. It should not continue deeper into individual unit powers.

---

## 16. Discipline audit

- Pell orbit enumeration: **FALSE**
- full continued-fraction digit enumeration: **FALSE**
- numerical factorization of \(D,E,h\): **FALSE**
- prime-ideal allocation: **FALSE**
- fixed \(q,g,k\) campaign: **FALSE**
- ray enumeration: **FALSE**
- multiplier enumeration: **FALSE**
- Gaussian/Hermitian reopening: **FALSE**
- q=1 reopening: **FALSE**
- general J reopening: **FALSE**

\[
\boxed{\textbf{J2 OPEN}.}
\]
