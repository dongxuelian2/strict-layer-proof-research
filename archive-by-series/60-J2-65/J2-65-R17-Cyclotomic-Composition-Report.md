# J2-65-R17 — Cyclotomic q-Elimination × q-Free Near-Square Core × Orthogonal Composition × Infrastructure Unwrapping

**Scope:** Strict Layer — A1-only — Exact Resonance \(R=0\) — \(J=2\) — \(q>1\)  
**Round:** 65 第十七轮 / A1 统一终端线第四十二轮  
**Status:** \(\boxed{\textbf{J2 OPEN}}\)

## 0. Executive verdict

R17 produces a genuine global recompression, but it does not close \(q>1\).

The three previously separated objects

\[
\text{R7 fibre discriminant},\qquad
\text{R9 Gaussian target},\qquad
\text{R16 boundary radicand}
\]

are linked by the exact identities

\[
\boxed{-\Delta_{\rm fib}=q^2N_0},
\]

\[
\boxed{D=q^4D_0},
\]

and

\[
\boxed{D_0+J_0^2=W_0N_0}.
\]

Moreover \(N_0\) is exactly the R9 Gaussian target \(N\). Thus the scalar/arithmetic core is one **cyclotomic orthogonal-composition geometry**.

The \(q\)-dependence of the normalized near-square packet is spurious at field/square-class level: after \(uq=G+1\), all of

\[
F_0,W_0,S_0,J_0,D_0,N_0
\]

depend only on \((G,u,K)\), with \(A=2u+1\). Hence \(q\) is no longer an independent normalized arithmetic coordinate.

The strongest negative theorem of the round is the infrastructure result. For every \(g\ge2\),

\[
\boxed{0<S_0<R_0},
\qquad R_0=F_0W_0,
\]

and the only \(g=1\), \(q>1\) exact-resonance case is also no-wrap. Therefore

\[
\boxed{S_0\bmod R_0=S_0}
\]

throughout the actual base, and the R16 “composite infrastructure phase” is not a periodic arithmetic object at all. It is an ordinary deterministic algebraic height coordinate. Multiplicative-order and phase-orbit analysis are permanently retired.

However, field-level square descent does **not** automatically descend the integral source norm lattice. On the nonsplit locus

\[
\mathbf Z[\sqrt D]
=
\mathbf Z[q^2\sqrt{D_0}]
\subset
\mathbf Z[\sqrt{D_0}]
\]

with index \(q^2\). R16's source multiplier order and its composite \(C_{\rm extra}\) must be recomputed after saturation; there is no legal theorem permitting the remaining norm coordinates to be divided by the full visible \(q\)-square scale. Thus the exact verdict is

\[
\boxed{\text{field/core q-elimination = TRUE}},
\qquad
\boxed{\text{order/source-lattice q-elimination = PARTIAL}}.
\]

Finally, the orthogonal composition is an exact Euclidean similitude on the parameter vector \((T_0,1)\), but no source-preserving map from the R16 coordinates \((r_N,v_N,h)\) is obtained. Therefore the R9→R16 bridge is **not** upgraded to a source-lattice isometry/similitude; its honest verdict is `FORMAL_IDENTITY_ONLY` at the source-lattice level.

The terminal frontier is therefore:

\[
\boxed{
\text{one q-free scalar composition core in }(G,u,K)
}
\]

together with

\[
\boxed{
\text{one source-lattice/index/conductor packet}
\times
\text{the original digit-height shell}
\times
\mathscr T_{10}.
}
\]

The R16 unit/Pell/infrastructure-phase campaign is no longer a justified next layer.

---

## 1. Exact cyclotomic elimination

Freeze

\[
A=2u+1,\quad B=2G+q,\quad uq=G+1,
\quad qA-B=2,\quad uB-GA=1.
\]

Put

\[
C=2G+q+2.
\]

Then

\[
qA=2uq+q=2(G+1)+q=C,
\]

so

\[
\boxed{C=qA}.
\]

Likewise

\[
2G^2+Gq+2G+2q
=
GC+2q
=
q(GA+2).
\]

Set

\[
L_0=GA+1=uB,\qquad
F_0=L_0^2-1=GA(GA+2).
\]

Exact symbolic substitution into the R16 fibre defect gives

\[
\boxed{\mathcal R_F=q^2(L_0^2-2)}.
\]

Since

\[
T=2KG(G+1)=q(2KGu),
\]

define

\[
T_0=2KGu.
\]

Then

\[
-\Delta_{\rm fib}
=
T^2-\mathcal R_F
=
q^2(T_0^2-L_0^2+2).
\]

Thus

\[
\boxed{N_0=T_0^2-L_0^2+2},
\qquad
\boxed{-\Delta_{\rm fib}=q^2N_0}.
\]

R9's target is

\[
N=2+u^2(4K^2G^2-B^2).
\]

Since \(uB=L_0\),

\[
N=2+T_0^2-L_0^2=N_0.
\]

Therefore

\[
\boxed{-\Delta_{\rm fib}=q^2N_{\rm R9}}.
\]

This is a direct invariant bridge from the R7 fibre discriminant to the R9 Gaussian target.

---

## 2. q-free boundary near-square packet

Define

\[
U_0=G^2A,\qquad V_0=20u,
\qquad W_0=U_0^2+V_0^2.
\]

Using \(C=qA\) and \(G+1=uq\),

\[
G^4C^2+400(G+1)^2
=
q^2(G^4A^2+400u^2)
=
q^2W_0.
\]

The R16 boundary defect therefore becomes

\[
\begin{aligned}
\mathcal R_D
&=
G\,(qA)\,q(GA+2)\,q^2W_0\\
&=
q^4\,GA(GA+2)W_0,
\end{aligned}
\]

hence

\[
\boxed{\mathcal R_D=q^4F_0W_0}.
\]

Next,

\[
S_D
=
2KG^3(G+1)C+20q(G+1)
=
q^2(2KGuG^2A+20u).
\]

Define

\[
\boxed{S_0=U_0T_0+V_0}.
\]

Then

\[
\boxed{S_D=q^2S_0}.
\]

With

\[
R_0:=F_0W_0,
\qquad
D_0:=S_0^2-R_0,
\]

the R16 radicand satisfies

\[
\boxed{D=q^4D_0}.
\]

Similarly,

\[
E_\partial
=
-GC(2G^2+Gq+2G+2q)\Delta_{\rm fib}
=
\boxed{q^4F_0N_0}.
\]

This proves that the complete scalar quadratic-étale packet carries a common cyclotomic square scale.

---

## 3. Field, coordinate order, source order

Because

\[
D=q^4D_0,
\qquad
\sqrt D=q^2\sqrt{D_0},
\]

the nonsplit fields are equal:

\[
\boxed{\mathbf Q(\sqrt D)=\mathbf Q(\sqrt{D_0})}.
\]

The split locus is also unchanged.

But the coordinate orders are not equal in general:

\[
\mathbf Z[\sqrt D]
=
\mathbf Z[q^2\sqrt{D_0}]
\subset
\mathbf Z[\sqrt{D_0}],
\]

and on a nonsplit specialization the inclusion has index

\[
\boxed{q^2}.
\]

Equivalently, their coordinate-order discriminants differ by \(q^4\).

R16's actual source order is not merely the coordinate order; it is the multiplier ring of the source lattice/coset packet. Therefore the field descent does not determine the new conductor or multiplier ring.

Verdict:

```text
CYCLOTOMIC_Q4_FIELD_DESCENT=PROVED
CYCLOTOMIC_Q4_ORDER_DESCENT=PARTIAL
```

For the defect ideal,

\[
\mathfrak I_D
=
(q^4R_0,q^2(S_0+\sqrt{D_0}))
=
q^2(q^2R_0,S_0+\sqrt{D_0}).
\]

The outer \(q^2\) is principal scaling, but the inner generator \(q^2R_0\) and the order change remain. Hence

```text
R16_DEFECT_PACKET_TO_qFREE_PACKET=PARTIAL
```

rather than `EQUIVALENT`.

---

## 4. Cyclotomic Orthogonal-Composition Theorem

Define

\[
\boxed{J_0=U_0-V_0T_0}.
\]

Then

\[
(U_0-iV_0)(T_0+i)
=
(U_0T_0+V_0)+i(U_0-V_0T_0),
\]

so

\[
\boxed{
(U_0-iV_0)(T_0+i)=S_0+iJ_0.
}
\]

Taking Gaussian norms,

\[
\boxed{
S_0^2+J_0^2=W_0(T_0^2+1).
}
\]

Since

\[
F_0=L_0^2-1
\]

and

\[
N_0=T_0^2-L_0^2+2,
\]

we have

\[
T_0^2+1-F_0=N_0.
\]

Thus

\[
\begin{aligned}
D_0+J_0^2
&=
S_0^2-F_0W_0+J_0^2\\
&=
W_0(T_0^2+1-F_0)\\
&=
W_0N_0.
\end{aligned}
\]

Therefore

\[
\boxed{
D_0+J_0^2=W_0N_0
}
\]

or

\[
\boxed{
D_0=W_0N_{\rm R9}-J_0^2.
}
\]

This is the **Cyclotomic Orthogonal-Composition Theorem**.

In matrix form,

\[
M_0=
\begin{pmatrix}
U_0&V_0\\
-V_0&U_0
\end{pmatrix},
\qquad
M_0^TM_0=W_0I,
\]

and

\[
M_0
\binom{T_0}{1}
=
\binom{S_0}{J_0}.
\]

It is exactly an integral Euclidean similitude.

### General tool: Orthogonal-Composition Schur Lemma

If \(M^TM=WI\), \(Mv=w\), then for any scalar \(F\),

\[
w_1^2-FW
=
W(|v|^2-F)-w_2^2.
\]

R17 is the specialization

\[
v=(T_0,1),\quad
w=(S_0,J_0),\quad
F=F_0.
\]

---

## 5. What the composition does not prove

The matrix \(M_0\) acts on the two-dimensional parameter vector

\[
(T_0,1),
\]

not on R16's source norm coordinates

\[
(r_N,v_N,h).
\]

No integral map has been produced that simultaneously preserves:

- the R16 source lattice/coset;
- the \(h\)-coordinate;
- the discriminant-converse congruence;
- the digit-height strip;
- the multiplier ring/order.

Therefore the correct certificate is

```text
R9_TO_R16_SOURCE_NORM_BRIDGE=FORMAL_IDENTITY_ONLY
```

at the **source-lattice** level, even though the scalar identity and the Euclidean similitude are exact.

The important structural conclusion is narrower:

\[
\boxed{
\text{the R16 radicand is not an independent scalar polynomial invariant.}
}
\]

The remaining source-attached integral incidence may still be genuinely additional.

---

## 6. Source norm lattice q-descent

R16 gives before the moving \(C_{\rm extra}\) division

\[
r_0^2-Dv_0^2
=
(20G^2q^2(G+1))^2E_\partial h^2.
\]

Substituting the R17 identities yields

\[
r_0^2-q^4D_0v_0^2
=
(20G^2q^4(G+1))^2F_0N_0h^2.
\]

The integral substitution

\[
v_\circ=q^2v_0
\]

is legal and gives

\[
\boxed{
r_0^2-D_0v_\circ^2
=
(20G^2q^4(G+1))^2F_0N_0h^2.
}
\]

At the final R16 normalization,

\[
\boxed{
r_N^2-D_0(q^2v_N)^2
=
\left(
\frac{20G^2q^4(G+1)}{C_{\rm extra}}
\right)^2
F_0N_0h^2.
}
\]

This removes \(q\) from the radicand, but not from the integral scalar/lattice package.

R16 already stopped after the maximal universal coordinate descent and retained \(C_{\rm extra}\) precisely because further specialization-dependent divisibility was not universal. R17 has no source-row theorem proving that the displayed \(q^4\) can now be divided from both norm coordinates. Doing so would be an illegal rational simplification.

Hence

```text
q_ELIMINATION_FIELD_LEVEL=TRUE
q_ELIMINATION_ORDER_LEVEL=PARTIAL
q_ELIMINATION_SOURCE_LATTICE_LEVEL=PARTIAL
q_ELIMINATION_DIGIT_SHELL_LEVEL=PARTIAL
Q_FREE_SOURCE_NORM_CORE=PARTIAL
```

The residual \(q\) is nevertheless **not an independent base variable**: it is always recoverable as \((G+1)/u\). What survives is deterministic integral scale/index/conductor data.

---

## 7. Infrastructure phase normalization

Write

\[
S_0=P_0K+Q_0,
\]

with

\[
P_0=2uG^3A,\qquad Q_0=20u.
\]

For \(g\ge2\), the exact whole-modulus gcd is

\[
\boxed{\gcd(P_0,R_0)=800GA}.
\]

### Proof without factoring \(u\) or \(R_0\)

Since \(uq=G+1\),

\[
\gcd(G,u)=1,
\qquad
G\equiv-1\pmod u.
\]

Also \(\gcd(A,u)=1\), because \(A=2u+1\). Hence

\[
GA+2\equiv1\pmod u,
\]

and

\[
W_0=G^4A^2+400u^2
\equiv G^4A^2\pmod u,
\]

so both \(GA+2\) and \(W_0\) are coprime to \(u\).

Thus

\[
\gcd(P_0,R_0)
=
GA\gcd(2G^2,(GA+2)W_0).
\]

For \(G=10^g,\ g\ge2\),

\[
v_2(GA+2)=1,\qquad v_5(GA+2)=0.
\]

Since \(u,A\) are ten-units,

\[
v_2(W_0)=4,\qquad v_5(W_0)=2.
\]

No prime outside \(2,5\) divides \(2G^2\). Therefore

\[
\gcd(2G^2,(GA+2)W_0)=2^5 5^2=800.
\]

No factorization of \(u\) or \(R_0\) is used.

Define

\[
m_{\rm ph}
=
\frac{R_0}{800GA}
=
\boxed{
\frac{GA+2}{2}
\left[
u^2+
\left(\frac{G^2A}{20}\right)^2
\right]
},
\]

and

\[
c_{\rm ph}
=
\frac{P_0}{800GA}
=
\boxed{\frac{uG^2}{400}}.
\]

Then

\[
\psi_k
=
\frac{S_0-Q_0}{800GA}
=
c_{\rm ph}10^k.
\]

Consequently

\[
\boxed{
\psi_k\equiv c_{\rm ph}10^k\pmod{m_{\rm ph}}.
}
\]

Moreover

\[
\gcd(m_{\rm ph},10)
=
\gcd(m_{\rm ph},u)
=
\gcd(c_{\rm ph},m_{\rm ph})
=
1.
\]

Thus if wrapping existed, it would indeed be one cyclic ten-unit orbit. R17 next proves that wrapping does not occur.

---

## 8. Infrastructure Phase Unwrapping Theorem

Exact resonance gives

\[
k=2g-\ell,\qquad \ell>0,
\]

hence

\[
\boxed{k<2g},
\qquad
\boxed{K<G^2}.
\]

For \(g\ge2\),

\[
c_{\rm ph}K
<
\frac{uG^4}{400}.
\]

But

\[
m_{\rm ph}
>
\frac{G^4A^2(GA+2)}{800}.
\]

Since \(A=2u+1\),

\[
A^2(GA+2)>2u,
\]

so

\[
\boxed{
0<c_{\rm ph}K<m_{\rm ph}.
}
\]

Hence the normalized orbit never wraps.

More strongly,

\[
S_0
=
2uG^3AK+20u
<
2uG^5A+20u,
\]

whereas

\[
R_0
=
GA(GA+2)(G^4A^2+400u^2)
>
G^6A^4.
\]

For \(G\ge100\), \(A\ge3\),

\[
2uG^5A<\frac12G^6A^4,
\qquad
20u<\frac12G^6A^4,
\]

so

\[
\boxed{0<S_0<R_0}.
\]

Therefore

\[
\boxed{S_0\bmod R_0=S_0}.
\]

### The fixed \(g=1\) audit

If \(G=10\), then \(G+1=11\). With \(q>1\),

\[
u=1,\qquad q=11.
\]

Exact resonance gives \(k<2\), hence \(k=1,\ K=10\). Then

\[
A=3,\quad
S_0=60020,\quad
R_0=86784000,
\]

so no wrapping occurs.

Thus throughout the actual q>1 base:

```text
INFRASTRUCTURE_PHASE_PERIODICITY=RETIRED
INFRASTRUCTURE_PHASE_WRAP_AROUND=IMPOSSIBLE
POWER_TEN_MULTIPLICATIVE_ORDER_STAGE=NOT_APPLICABLE
```

This does **not** make \(K\) disappear. It remains in \(T_0,S_0,J_0,N_0,D_0\), but only as deterministic algebraic motion.

### General tool: Infrastructure Phase Unwrapping

If a near-square packet depends on \(S\bmod R\) and source height proves

\[
0<S<R,
\]

then the infrastructure “phase” is exactly the ordinary coordinate \(S\). Any multiplicative-order or phase-dynamics stage is inapplicable.

---

## 9. q elimination as a base-dimension theorem

All normalized scalar invariants are now functions of

\[
(G,u,K)
\]

with

\[
A=2u+1.
\]

Explicitly,

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
S_0=2uG^3AK+20u,
\]

\[
J_0=G^2A-40u^2GK,
\]

\[
N_0=4u^2G^2K^2-(GA+1)^2+2,
\]

\[
D_0=S_0^2-F_0W_0.
\]

The original \(q\) is merely

\[
\boxed{q=(G+1)/u}.
\]

Therefore

\[
\boxed{
q\text{ is not an independent arithmetic coordinate of the normalized near-square/composition core.}
}
\]

---

## 10. Split étale locus

Because

\[
D=q^4D_0,
\]

and \(q^2\in\mathbf Z\),

\[
\boxed{D\text{ is a square}\iff D_0\text{ is a square}}.
\]

Thus the split locus is the q-free hypersurface

\[
\boxed{
\mathscr S_{\rm split}:D_0(G,u,K)=Y^2.
}
\]

Since

\[
D_0=(P_0K+Q_0)^2-R_0,
\]

it is quadratic in \(K\), and its \(K\)-discriminant is

\[
\boxed{4P_0^2R_0}.
\]

Over \(\mathbf Q(G,u)\), the curve is a genus-zero conic and can be written

\[
\boxed{
(S_0-Y)(S_0+Y)=R_0.
}
\]

It is therefore a global conic/toric incidence, not a fixed-field Pell problem.

The composition theorem gives

\[
\boxed{
Y^2+J_0^2=W_0N_0.
}
\]

Since \(W_0=U_0^2+V_0^2\), if \(N_0\) is a Gaussian norm then \(W_0N_0\) is automatically a Gaussian norm. But the split condition requires a Gaussian representation whose one coordinate is the **prescribed** value \(J_0\). That is not automatic.

Therefore the R16 square-locus gap becomes a genuinely source-attached **fixed-coordinate Gaussian norm incidence**, but it is now q-free.

---

## 11. Power-of-ten toric section

Define

\[
\mathscr T_{10}
=
\{(G,K):G=10^g,\ K=10^k,\ 0<k<2g\}.
\]

The normalized core is sparse in \(G,K\):

\[
N_0=4u^2G^2K^2-(GA+1)^2+2,
\]

\[
S_0=2uG^3AK+20u,
\]

\[
J_0=G^2A-40u^2GK,
\]

and \(D_0\) is quadratic in \(K\).

No exact algebraic zero locus is currently forced by the source shell, so no speculative S-unit theorem is triggered.

---

## 12. New reusable tools

### Tool 1 — Cyclotomic Square-Descent Lemma

If a structural relation forces a centre and radicand to acquire scales

\[
S=q^mS_0,\qquad D=q^{2m}D_0,
\]

then the field/square-class layer descends to \(D_0\). Integral order/lattice descent is a separate index/conductor audit and cannot be inferred from the field equality.

### Tool 2 — Orthogonal-Composition Schur Lemma

If

\[
M^TM=WI,\qquad Mv=w,
\]

then

\[
w_1^2-FW=W(|v|^2-F)-w_2^2.
\]

This compresses a large Schur-complement radicand into one norm product minus one explicit square.

### Tool 3 — Infrastructure Phase Unwrapping

If a defect packet is formally controlled by \(S\bmod R\) but source inequalities imply

\[
0<S<R,
\]

then the phase is not a periodic arithmetic variable.

### Tool 4 — Affine Power-Orbit Normalization

Before unwrapping, R17 also proves the fallback normalization

\[
\psi_k=c_{\rm ph}10^k\pmod{m_{\rm ph}},
\qquad
\gcd(10c_{\rm ph},m_{\rm ph})=1.
\]

In this problem the stronger unwrapping theorem makes the fallback orbit unnecessary.

---

## 13. Direct answers to Q1–Q16

### Q1
Yes:
\[
\boxed{2G+q+2=qA}.
\]

### Q2
Yes:
\[
\boxed{\mathcal R_F=q^2[(GA+1)^2-2]}.
\]

### Q3
Yes:
\[
\boxed{-\Delta_{\rm fib}=q^2N_{\rm R9}}.
\]

### Q4
Yes:
\[
\boxed{\mathcal R_D=q^4F_0W_0}.
\]

### Q5
Yes:
\[
\boxed{S_D=q^2S_0,\qquad D=q^4D_0}.
\]

### Q6
Yes at the normalized scalar/field level: \(q\) is not independent. At the integral source-lattice/order level the descent is only partial because a deterministic q-scale/index/conductor remains.

### Q7
Yes:
\[
\boxed{(U_0-iV_0)(T_0+i)=S_0+iJ_0}.
\]

### Q8
Yes:
\[
\boxed{D_0+J_0^2=W_0N}.
\]

### Q9
It gives an exact integral Euclidean similitude on \((T_0,1)\), but **not** a proved source-norm similitude on \((r_N,v_N,h)\). Source-level verdict: `FORMAL_IDENTITY_ONLY`.

### Q10
Field: TRUE. Coordinate/source order: PARTIAL. Source lattice: PARTIAL. The radicand can be q-free; the full integral norm scale cannot yet be legally divided away.

### Q11
Yes for \(g\ge2\):
\[
\boxed{\psi_k\equiv c_{\rm ph}10^k\pmod{m_{\rm ph}}}
\]
with ten-unit composite modulus.

### Q12
Yes, more strongly:
\[
\boxed{0<S_0<R_0}
\]
throughout the actual q>1 base, including the one fixed \(g=1\) audit.

### Q13
Yes. R16 composite infrastructure phase should be permanently retired. \(K\) remains only as deterministic algebraic motion.

### Q14
Yes:
\[
\boxed{D_0(G,u,K)=Y^2}
\]
is the exact q-free split locus.

### Q15
At scalar near-square/infrastructure level, **no**: the R16 radicand is a composition shadow of R9 \(N\), and its phase is unwrapped. But the source integral norm lattice/coset remains an additional unresolved incidence. So the whole source norm layer is not retired, while the unit/infrastructure machinery is.

### Q16
Almost, but not completely in the strongest integral sense. R17 reaches

\[
\boxed{
\text{one q-free scalar composition core in }(G,u,K)
}
\]

plus

\[
\boxed{
\text{one source-lattice/index/conductor packet}
\times
\text{one original digit-height shell}.
}
\]

There is no longer an independent infrastructure phase, no reason to continue unit-orbit enumeration, and no independent \(q\)-coordinate. The only caveat is that the source norm lattice itself is not yet proven q-free after integral saturation.

---

## 14. Strategic verdict for R18

The unit/Pell route is finished as a productive frontier. The phase does not wrap, so multiplicative-order analysis is inapplicable.

The next round should work directly on

\[
\boxed{
D_0+J_0^2=W_0N_0
}
\]

over

\[
\boxed{
G=10^g,\quad K=10^k,\quad 0<k<2g,\quad u\mid G+1
}
\]

and intersect this q-free scalar composition core with the actual source lattice/digit shell.

The most precise next target is therefore:

\[
\boxed{
\textbf{q-Free Composition Core}
\times
\textbf{Source-Lattice Saturation/Incidence}
\times
\textbf{Power-of-Ten Toric Section}
\times
\textbf{Digit Shell}.
}
\]

A particularly valuable R18 objective would be to decide whether the remaining source lattice can be saturated in coordinates adapted to the similitude \(M_0\) so that the fixed-coordinate Gaussian incidence and the original digit shell meet in one source-preserving object.

No return to Pell indices, unit powers, regulator bounds, ideal-class tables, or multiplicative-order computation is justified.

\[
\boxed{\textbf{J2 OPEN}.}
\]
