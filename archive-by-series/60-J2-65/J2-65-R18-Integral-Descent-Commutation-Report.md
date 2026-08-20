# J2-65-R18 — Cyclotomic Integral Saturation × Saturation–Schur Commutation × q-Free Ambient Source Quadric

**Scope:** Strict Layer — A1-only — Exact Resonance \(R=0\) — \(J=2\) — \(q>1\)  
**Round:** 65 第十八轮 / A1 统一终端线第四十三轮  
**Final status:** \(\boxed{\mathbf{J2\ OPEN}}\)

## 0. Executive verdict

R18 identifies where the residual \(q\)-information actually lives.

The pre-Schur source lattice itself does **not** carry a genuine \(q\)-dependent congruence after the cyclotomic relation is used integrally. Starting from the actual R13/R15 boundary lattice and using \(uq=G+1\), its moving congruence is exactly equivalent to

\[
\boxed{
G\mid 2d(1+4u)\bigl(Z+u(1+2u)^3a\bigr).
}
\]

Hence, with

\[
\delta_0=\gcd(G,2d(1+4u)),\qquad M_0=G/\delta_0,
\qquad \beta_0=u(1+2u)^3,
\]

the pre-Schur source lattice is

\[
\boxed{
\Lambda_{\partial,0}
=
\{(Z,a,h)\in\mathbf Z^3:
M_0\mid Z+\beta_0a,\quad Aa+h\equiv0\pmod{10}\}.
}
\]

This is not an enlargement: it is exactly the old lattice. Therefore the source-first cyclotomic saturation quotient is trivial:

\[
\boxed{\mathcal C_{\rm cyc}=0.}
\]

The residual \(q\)-phenomenon appears only **after** Schur/norm completion. The R17 order inclusion

\[
\mathbf Z[q^2\sqrt{D_0}]\subset\mathbf Z[\sqrt{D_0}]
\]

has index \(q^2\), and the source norm coordinate lands in the same index-\(q^2\) sublattice. Consequently Saturation and Schur do not commute integrally, but they fail by exactly one cyclic finite module:

\[
\boxed{
\mathcal C_{\rm SS}\simeq\mathbf Z/q^2\mathbf Z.
}
\]

Thus the R17 “order conductor” and the universal \(q\)-part of the source norm-lattice defect are the **same cokernel phenomenon**.

Using R16's pre-\(C_{\rm extra}\) coordinates \((r_0,v_0)\), define

\[
R=r_0,\qquad V=q^2v_0,\qquad
H=\mu_0h,\qquad
\mu_0=20G^2q^4(G+1).
\]

Then the exact source norm equation becomes

\[
\boxed{
R^2-D_0V^2=F_0N_0H^2.
}
\tag{Q0}
\]

The quadratic form itself is completely \(q\)-free: its coefficients depend only on \((G,u,K)\). \(C_{\rm extra}\) is not needed in this canonical ambient model and is therefore absorbed rather than promoted to a new parameter.

Combining (Q0) with R17's
\[
D_0+J_0^2=W_0N_0
\]
gives the exact source-variable identity

\[
\boxed{
R^2+(J_0V)^2
=
N_0\bigl(W_0V^2+F_0H^2\bigr).
}
\tag{CAS}
\]

This genuinely upgrades the R17 scalar composition to a **source-attached identity**, but it still does not construct an integral similitude of the full source lattice. Hence `COMPOSITION_ADAPTED_SOURCE_COORDINATES=NOT_FOUND`.

After retaining the fixed decimal chart and contact-height semantic line as part of the ambient integral structure, the remaining moving source packet is

\[
\boxed{
\mathbf Z/M_0\mathbf Z\oplus\mathbf Z/q^2\mathbf Z.
}
\]

Since \(M_0\mid G\) and \(\gcd(q,G)=1\),

\[
\boxed{
\mathbf Z/M_0\mathbf Z\oplus\mathbf Z/q^2\mathbf Z
\simeq
\mathbf Z/(M_0q^2)\mathbf Z.
}
\]

So R18 attains the requested recompression to **one explicit finite source module**.

What R18 does **not** prove is that this finite packet is automatic on the ambient isotropic/digit locus. The digit-height functional also retains a recovered \(q\)-scale, although \(q\) is no longer an independent base coordinate. Therefore \(q>1\) is not closed.

The terminal frontier is

\[
\boxed{
\mathscr X_0(G,u,K)
\cap
\Gamma_{\rm src}^{\rm full}
\cap
\Omega_{\rm digit,0}
}
\]

with

\[
\boxed{
\mathscr X_0:\ R^2-D_0V^2-F_0N_0H^2=0,
}
\]

one finite cyclic moving source packet
\[
\boxed{\mathbf Z/(M_0q^2)\mathbf Z,}
\]
one exact digit shell, and the power-of-ten toric base.

The R16 unit/Pell/infrastructure layer is no longer independent arithmetic and remains permanently retired.

---

## 1. Reloaded actual source packet

R13 reduces source integrality to the single composite congruence

\[
G\mid d(h_ZZ+h_aa)
\]

in \((Z,a,x)\), with

\[
h_Z\equiv-2q^4(q+4)\pmod G,
\qquad
h_a\equiv-2(q+2)^3(q+4)\pmod G.
\]

R15 changes \(x\) to \(h=10x-Aa\) with determinant \(10\) and gives

\[
\Lambda_\partial
=
\{(Z,a,h)\in\mathbf Z^3:
G\mid d(h_ZZ+h_aa),\quad Aa+h\equiv0\pmod{10}\}.
\]

The second condition is a fixed decimal chart condition. The moving arithmetic is entirely in the first row.

The independent source parameter \(d\) survives only through the whole-modulus index. \(C_{\rm extra}\) is later normalization content of the norm-coordinate image and is not an original source coordinate.

---

## 2. Integral cyclotomic row reduction

On Exact Resonance,

\[
uq=G+1,
\]

so modulo \(G\),

\[
uq\equiv1.
\]

Since \(\gcd(u,G)=1\), multiplying a congruence row by \(u^5\) is an integral automorphism of the quotient modulo \(G\).

Two exact polynomial identities are

\[
u^5q^4(q+4)-(1+4u)
=
(uq-1)P_1(u,q),
\]

and

\[
u^5(q+2)^3(q+4)-u(1+2u)^3(1+4u)
=
u(uq-1)P_2(u,q),
\]

with \(P_1,P_2\in\mathbf Z[u,q]\). Since \(uq-1=G\), they give

\[
u^5q^4(q+4)\equiv1+4u\pmod G,
\]

\[
u^5(q+2)^3(q+4)
\equiv
u(1+2u)^3(1+4u)\pmod G.
\]

Therefore the R13 congruence is equivalent to

\[
\boxed{
G\mid2d(1+4u)\left(Z+u(1+2u)^3a\right).
}
\tag{SRC0}
\]

No rational substitution and no division by \(u\) occurred: only multiplication by a unit modulo \(G\).

Furthermore,

\[
u(q+4)=G+1+4u,
\]

hence, again because \(u\) is a unit modulo \(G\),

\[
\gcd(G,2d(q+4))
=
\gcd(G,2d(1+4u)).
\]

Thus

\[
\boxed{
\delta_0=\gcd(G,2d(1+4u)),
\qquad
M_0=G/\delta_0
}
\]

is exactly the old R13 index, rewritten without \(q\).

This proves

\[
\boxed{\mathcal C_{\rm cyc}=0.}
\]

The pre-Schur residual \(q\)-dependence was a choice of row representative, not a genuine source-lattice invariant.

---

## 3. q-free pre-Schur basis and fixed decimal index

Let

\[
\beta_0=u(1+2u)^3
\]

and choose

\[
\rho_0\equiv-\beta_0\pmod{M_0}.
\]

Then an exact basis is

\[
\boxed{
(M_0,0,0),\quad
(\rho_0,1,-A),\quad
(0,0,10).
}
\]

The determinant remains \(10M_0\). Relative to raw \(\mathbf Z^3\) its Smith factors are

\[
\boxed{
\left(
1,\ g_{10},\ \frac{10M_0}{g_{10}}
\right),
\qquad
g_{10}:=\gcd(M_0,10).
}
\]

Thus the fixed decimal index \(10\) is retained exactly. It is not confused with the moving cyclotomic/conductor packet.

---

## 4. q-free ambient source quadric

R16's pre-extra normalized norm equation is

\[
r_0^2-Dv_0^2
=
\left(20G^2q^2(G+1)\right)^2E_\partial h^2.
\]

R17 proves

\[
D=q^4D_0,
\qquad
E_\partial=q^4F_0N_0.
\]

Therefore

\[
r_0^2-D_0(q^2v_0)^2
=
\left(20G^2q^4(G+1)h\right)^2F_0N_0.
\]

Define

\[
\boxed{
R=r_0,\quad
V=q^2v_0,\quad
H=\mu_0h,\quad
\mu_0=20G^2q^4(G+1).
}
\]

All three are integral on actual source states. Hence

\[
\boxed{
Q_0(R,V,H)
=
R^2-D_0V^2-F_0N_0H^2=0.
}
\]

The coefficients \(D_0,F_0,N_0\) depend only on \((G,u,K)\):

\[
A=2u+1,
\]

\[
F_0=GA(GA+2),
\]

\[
W_0=G^4A^2+400u^2,
\]

\[
T_0=2KGu,
\]

\[
N_0=T_0^2-(GA+1)^2+2,
\]

\[
S_0=G^2AT_0+20u,
\]

\[
D_0=S_0^2-F_0W_0.
\]

Thus `Success A` is achieved exactly.

### Why \(C_{\rm extra}\) disappears from the canonical model

R16 introduced \(C_{\rm extra}\) only to make a further specialization-dependent primitive descent of both norm-coordinate rows. It is unnecessary for the existence of the integral q-free ambient form. Working with \((r_0,v_0)\) retains every actual source point and avoids making a normalization gcd into a base parameter.

If one insists on R17's post-\(C_{\rm extra}\) coordinates, then

\[
\mu_q=
\frac{20G^2q^4(G+1)}{C_{\rm extra}}
=
q^2\frac{20G^2q^2(G+1)}{C_{\rm extra}}
\in\mathbf Z
\]

by the defining divisibility of \(C_{\rm extra}\). So the prompt's candidate is also integral. The pre-extra chart is simply cleaner.

---

## 5. The correct ambient lattice

It would be misleading to take the ambient lattice to be raw \(\mathbf Z^3_{R,V,H}\) and then interpret every determinant factor as a source obstruction. The Schur coordinate map itself has non-unimodular geometric content, and \(H=\mu_0h\) is a semantic contact-height line that must remain fixed.

Accordingly, the canonical q-free ambient integral structure is defined by:

1. retaining the fixed decimal chart \(Aa+h\equiv0\pmod{10}\);
2. transporting that chart through the exact source-preserving Schur map;
3. retaining the contact-height line \(H\in\mu_0\mathbf Z\);
4. saturating only the quadratic-order \(\sqrt{D_0}\)-coordinate that R17 showed to differ by \(q^2\).

With this choice the finite quotient measures source arithmetic, not coordinate-Jacobian artifacts.

---

## 6. Saturation–Schur commutation

There are now two distinct saturation operations, and confusing them was exactly the R17 ambiguity.

### Source-first

At pre-Schur level the cyclotomic source saturation is trivial:

\[
\Lambda_\partial^{\rm cyc,sat}
=
\Lambda_{\partial,0}
=
\Lambda_\partial.
\]

After Schur completion the source image has

\[
V=q^2v_0.
\]

### Norm-first

Schur first gives the order

\[
\mathbf Z[q^2\sqrt{D_0}],
\]

while q-free order saturation gives

\[
\mathbf Z[\sqrt{D_0}].
\]

Their quotient is cyclic of order \(q^2\).

Hence

\[
\boxed{
\operatorname{Schur}(\operatorname{Sat}_{\rm src}\Lambda_\partial)
\neq
\operatorname{Sat}_{\rm ord}(\operatorname{Schur}\Lambda_\partial)
}
\]

integrally, but

\[
\boxed{
\mathcal C_{\rm SS}
\simeq
\mathbf Z/q^2\mathbf Z.
}
\]

Therefore

```text
SATURATION_SCHUR_COMMUTATION=FINITE_INDEX
COMMUTATION_DEFECT_MODULE=Z/q^2Z
```

They are rationally identical, and the failure of integral commutation is rank-zero and one-generator.

This answers the central R18 question: the R17 source/order residual is **not** a large hidden lattice. It is one cyclic conductor direction created by Schur completion.

---

## 7. Index–conductor correspondence

The order defect is

\[
\mathbf Z[q^2\sqrt{D_0}]
\subset
\mathbf Z[\sqrt{D_0}]
\]

with quotient generated by the class of \(\sqrt{D_0}\) modulo \(q^2\sqrt{D_0}\).

The source q-free norm embedding has exactly the same coordinate condition

\[
V=q^2v_0.
\]

Thus the universal \(q\)-part of its saturation quotient is generated by the same missing \(\sqrt{D_0}\)-coordinate.

Consequently

\[
\boxed{
\texttt{INDEX_CONDUCTOR_CORRESPONDENCE
=PROVED\_FOR\_THE\_UNIVERSAL\_q\_PART}.
}
\]

The \(d\)-dependent source index \(M_0\) is not part of this quadratic-order conductor; it comes from the original source congruence. The point of R18 is that these two pieces can nevertheless be stored in one finite module.

---

## 8. One finite source module

Work relative to the fixed decimal/contact ambient lattice. The source congruence contributes

\[
\mathbf Z/M_0\mathbf Z.
\]

The Schur/order commutation defect contributes

\[
\mathbf Z/q^2\mathbf Z.
\]

Since \(M_0\mid G\) and \(uq=G+1\),

\[
\gcd(q,G)=1,
\]

hence

\[
\gcd(M_0,q)=1.
\]

Therefore CRT gives

\[
\boxed{
\mathfrak C_{\rm src}
=
\mathbf Z/M_0\mathbf Z
\oplus
\mathbf Z/q^2\mathbf Z
\simeq
\mathbf Z/(M_0q^2)\mathbf Z.
}
\tag{FP}
\]

This is the requested single finite moving source packet.

If one wants the full raw-coordinate ledger including the fixed decimal index, combine R15's SNF with the coprime \(q^2\) factor:

\[
\boxed{
\operatorname{SNF}_{\rm raw}
=
\left(
1,\ g_{10},\
q^2\frac{10M_0}{g_{10}}
\right).
}
\]

Its order is \(10M_0q^2\).

Thus `Success B` is achieved: the vague “index/conductor/coset packet” has been replaced by one explicit finite abelian module.

---

## 9. Composition-Adapted Source Norm Identity

R17 gives

\[
D_0+J_0^2=W_0N_0.
\]

The ambient source equation is

\[
R^2-D_0V^2=F_0N_0H^2.
\]

Add \(J_0^2V^2\) to both sides:

\[
R^2+J_0^2V^2
=
(D_0+J_0^2)V^2+F_0N_0H^2.
\]

Hence

\[
\boxed{
R^2+(J_0V)^2
=
N_0(W_0V^2+F_0H^2).
}
\]

Define

\[
\boxed{
Q_{\rm aux}(V,H)=W_0V^2+F_0H^2.
}
\]

Then

\[
\operatorname{content}(Q_{\rm aux})
=
\boxed{\gcd(W_0,F_0)}
\]

and, with the ordinary binary-form convention,

\[
\operatorname{disc}(Q_{\rm aux})
=
\boxed{-4W_0F_0}.
\]

Since \(W_0>0\) and \(F_0>0\), \(Q_{\rm aux}\) is positive definite.

This proves `Success F`.

What it does not prove is an integral source similitude. R17's \(2\times2\) orthogonal matrix still acts canonically on \((T_0,1)\), not on a source basis of \((R,V,H)\). No block-Smith coordinate system adapted to that matrix is forced. Therefore:

```text
COMPOSITION_ADAPTED_SOURCE_COORDINATES=NOT_FOUND
```

The upgrade over R17 is real but narrower: `FORMAL_IDENTITY_ONLY` is upgraded to an exact **source-variable norm identity**, not to a source-lattice isometry.

---

## 10. R16 layer after CAS

The R16 unit/orbit/order machinery no longer represents an independent infinite arithmetic layer.

After R18, every source point is governed by:

\[
Q_0=0,
\]

the finite module \(\mathfrak C_{\rm src}\), and the digit shell.

Therefore

```text
R16_SOURCE_NORM_LAYER_AFTER_CAS=FINITE_LATTICE_PACKET_ONLY
R16_SOURCE_NORM_LAYER_INDEPENDENT=FALSE
```

The source norm *equation* survives, but its Pell/unit interpretation is retired.

This achieves the structural content of `Success G`.

---

## 11. Exact digit-height pullback

R15 gives

\[
R_\partial=2d_0a+d_1h.
\]

R16 divides the first norm coordinate by \(800q^5\), so

\[
R=r_0=\frac{R_\partial}{800q^5}.
\]

R17 gives

\[
d_0=400q^{10}D_0.
\]

Define the exact R16 normalized h-row coefficient

\[
\lambda_h:=\frac{d_1}{800q^5}.
\]

Then

\[
\boxed{
R=q^5D_0\,a+\lambda_h h.
}
\]

Since

\[
H=\mu_0h,
\]

we obtain

\[
\boxed{
h=\frac{H}{\mu_0},
}
\]

and

\[
\boxed{
a=
\frac{R-\lambda_h H/\mu_0}{q^5D_0}.
}
\]

These are exact functionals on the source image.

The original source semantics become

\[
1\le a<G,\qquad
H\in\mu_0\mathbf Z_{>0},\qquad
\frac{H/\mu_0}{a}\in\mathscr I_\eta,
\]

together with the inherited whole-modulus thin-shell condition

\[
G\le j(10u)a(Aa+1).
\]

No primitive-mod-\(u\) gate and no Jacobsthal campaign is reopened.

The important negative verdict is

```text
DIGIT_HEIGHT_FUNCTIONAL_q_DEPENDENCE=SCALAR_ONLY
Q_FREE_DIGIT_SHELL=PARTIAL
```

because the quadratic **ambient form** is q-free, but the exact integral height section still contains the recovered integer \(q=(G+1)/u\). There is no legal source theorem dividing \(R\) by \(q^5\) uniformly.

Thus q is retired as an independent base coordinate, but not from every integral scale in the digit embedding.

---

## 12. Digit shell as one affine cone slice

Define \(\Omega_{\rm digit,0}\) to be the set of ambient triples satisfying simultaneously:

\[
H\in\mu_0\mathbf Z_{>0},
\]

\[
a(R,H)=
\frac{R-\lambda_hH/\mu_0}{q^5D_0}
\in\mathbf Z,
\]

\[
1\le a(R,H)<G,
\]

\[
\frac{H/\mu_0}{a(R,H)}\in\mathscr I_\eta,
\]

and

\[
G\le j(10u)a(R,H)\left(Aa(R,H)+1\right).
\]

This is retained as one semialgebraic/arithmetic shell; no W-sector components are reopened.

---

## 13. Finite-packet automaticity

R18 does **not** prove that every integral point of the q-free ambient quadric in the real digit shell lands in the required class modulo \(M_0q^2\).

Nor is it legitimate to call the packet false merely because it is nontrivial: automaticity is an incidence statement requiring an action or approximation theorem on the actual integral quadric with the digit section.

Therefore

```text
FINITE_PACKET_AUTOMATIC_ON_AMBIENT_ISOTROPIC_LOCUS=UNRESOLVED
SOURCE_PACKET_IS_CURRENT_J2_OBSTRUCTION=TRUE
```

This is now the unique residual arithmetic gate attached to the R15–R18 boundary route.

No residue enumeration is opened.

---

## 14. Split specialization

On

\[
D_0=Y^2,
\]

the q-free ambient equation factors:

\[
\boxed{
(R-YV)(R+YV)=F_0N_0H^2.
}
\]

The source lattice remains rank three and the finite module specializes without a rank jump. The factorization itself does not force the required class modulo \(M_0q^2\).

Hence

```text
SPLIT_SOURCE_PACKET=SPECIAL
```

rather than `AUTOMATIC` or `EMPTY`.

No factor allocation is performed.

---

## 15. Power-of-ten primitive ambient form

On

\[
G=10^g,\qquad K=10^k,\qquad0<k<2g,
\]

the q-free scalar coefficients have degrees

\[
\deg_G F_0=2,\quad
\deg_G N_0=2,\quad
\deg_G W_0=4,\quad
\deg_G D_0=6,
\]

and

\[
\deg_K N_0=2,\qquad
\deg_KD_0=2.
\]

The ambient form is

\[
Q_0=R^2-D_0V^2-F_0N_0H^2.
\]

Because the coefficient of \(R^2\) is \(1\),

\[
\boxed{\operatorname{content}(Q_0)=1.}
\]

Therefore

\[
\boxed{
Q_{10}^{\rm prim}=Q_0.
}
\]

There is no universally certified ten-square content left in the scalar form. Any further ten-power division would have to act on the source lattice and is not currently legal.

No exact algebraic zero locus \(F(G,u,K)=0\) is forced, so no S-unit stage is triggered.

---

## 16. New reusable principles

### Integral Descent Commutation Principle

For an integral quadratic lattice, field-level square descent and Schur complement need not commute in the integral category. The failure is measured by the finite cokernel between the source-first Schur image and the post-Schur saturated order.

Here:

\[
\boxed{\mathcal C_{\rm SS}\simeq\mathbf Z/q^2\mathbf Z.}
\]

### q-Free Ambient Form + Integral Packet Principle

Move removable square factors out of the quadratic coefficients and into the source embedding:

\[
\boxed{
Q_0(R,V,H)=0
}
\]

plus one finite source packet.

Here the moving packet is

\[
\boxed{
\mathbf Z/(M_0q^2)\mathbf Z.
}
\]

### Composition-Adapted Source Identity

The R17 scalar orthogonal composition pulls back to

\[
\boxed{
R^2+(J_0V)^2=N_0Q_{\rm aux}(V,H)
}
\]

on the actual source image, with

\[
Q_{\rm aux}=W_0V^2+F_0H^2.
\]

---

## 17. Direct answers to Q1–Q16

### Q1. What exactly is the R17 residual q-dependence?

It consists of one universal post-Schur conductor/index direction of order \(q^2\). The original pre-Schur source congruence is q-free after legal row reduction. \(d\) survives separately only through \(M_0\). \(C_{\rm extra}\) is absorbed by the pre-extra norm chart.

### Q2. Can cyclotomic relation give stronger legal pre-Schur saturation?

Yes. In fact it gives exact q-free row equivalence:
\[
G\mid2d(1+4u)(Z+u(1+2u)^3a).
\]

### Q3. What is the source-first saturation quotient?

\[
\boxed{\mathcal C_{\rm cyc}=0,\quad |\mathcal C_{\rm cyc}|=1.}
\]

### Q4. Can one construct the exact q-free ambient source quadric?

Yes:
\[
\boxed{R^2-D_0V^2=F_0N_0H^2.}
\]

### Q5. Which sublattice/coset do actual source states form?

In the fixed decimal/contact ambient, they are the kernel of one combined finite class in
\[
\boxed{\mathbf Z/(M_0q^2)\mathbf Z.}
\]
Equivalently the two transparent factors are source congruence \(M_0\) and Schur conductor \(q^2\).

### Q6. What is the embedded-lattice saturation quotient?

Canonically,
\[
\boxed{\mathfrak C_{\rm src}\simeq\mathbf Z/(M_0q^2)\mathbf Z.}
\]
Relative to raw \(\mathbf Z^3\), retaining the fixed decimal index:
\[
\boxed{
(1,g_{10},q^2\,10M_0/g_{10}).
}
\]

### Q7. Is R17's order index \(q^2\) the same conductor phenomenon as the source quotient?

For the universal \(q\)-part, yes:
\[
\boxed{\mathbf Z/q^2\mathbf Z.}
\]
The \(M_0\) factor is original source congruence data, not quadratic-order conductor.

### Q8. Do saturation-before-Schur and Schur-before-saturation commute?

Not integrally. They are finite-index equivalent:
\[
\boxed{\texttt{SATURATION\_SCHUR\_COMMUTATION=FINITE\_INDEX}.}
\]

### Q9. What is the unique commutation defect?

\[
\boxed{\mathcal C_{\rm SS}\simeq\mathbf Z/q^2\mathbf Z.}
\]

### Q10. Is the composition-adapted source identity exact?

Yes:
\[
\boxed{
R^2+(J_0V)^2
=
N_0(W_0V^2+F_0H^2).
}
\]

### Q11. Does this upgrade R17 `FORMAL_IDENTITY_ONLY`?

It upgrades it to an exact identity on source variables, but **not** to an integral source-lattice similitude. No composition-adapted integral source basis was found.

### Q12. What are digit height and contact height?

\[
\boxed{h=H/\mu_0,}
\]
\[
\boxed{
a=(R-\lambda_hH/\mu_0)/(q^5D_0),
\quad
\lambda_h=d_1/(800q^5).
}
\]

### Q13. Can q retire completely from the digit shell?

No. It retires as an independent base variable, but the exact height section retains recovered q-scales:
\[
\boxed{\texttt{DIGIT\_HEIGHT\_FUNCTIONAL\_q\_DEPENDENCE=SCALAR\_ONLY}.}
\]

### Q14. Is the remaining finite source packet automatic?

\[
\boxed{\texttt{UNRESOLVED}.}
\]
No transitivity/strong-approximation theorem has yet been proved with the digit shell attached.

### Q15. Is the R16 source norm layer still genuinely independent?

No:
\[
\boxed{
\texttt{R16\_SOURCE\_NORM\_LAYER\_AFTER\_CAS
=FINITE\_LATTICE\_PACKET\_ONLY}.
}
\]
Its unit/Pell/order dynamics are not an independent frontier.

### Q16. What is the R18 terminal q>1 frontier?

Yes, it has the requested form:

\[
\boxed{
\text{one q-free integral ambient quadric/composition core}
}
\]

times

\[
\boxed{
\text{one finite source saturation/conductor module }
\mathbf Z/(M_0q^2)\mathbf Z
}
\]

times

\[
\boxed{
\text{one digit shell}
}
\]

times

\[
\boxed{
\text{the power-of-ten toric base}.
}
\]

It cannot yet be reduced further because finite-packet automaticity and complete q-retirement from the digit-height functional are not proved.

---

## 18. Strategic verdict for R19

\[
\boxed{\mathbf{J2\ OPEN}.}
\]

The next round must **not** return to units, Pell equations, regulators, infrastructure phase, multiplicative order, prime decomposition of \(q\), or prime decomposition of \(d\).

The unique justified next object is

\[
\boxed{
\textbf{finite cyclic source module }
\mathbf Z/(M_0q^2)\mathbf Z
\textbf{ acting/inciding on the q-free ambient quadric}
}
\]

together with the already-defined digit shell.

The target is to decide finite-module orbit/transitivity/automaticity globally, without splitting the modulus into primes. If that packet proves automatic, the entire R15–R18 boundary/source-integral route ceases to be a J2 obstruction and a fresh independent-obstruction audit is required.

No exact toric zero locus has emerged, so an S-unit campaign is still unjustified.
