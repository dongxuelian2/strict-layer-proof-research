# J2-55-R7 — Carry-Index Integerization × q-Content Dependency Audit × Pre-Descent Tail Factorization

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第七轮 / 统一终端线第十七轮  
**Primary inherited source:** `J2-55-R6-Euclidean-Quotient-Defect-Report.md`  
**Symbolic certificate:** `J2-55-R7-CarryIndex-symbolic.py`  
**Regression/search:** `J2-55-R7-QDescent-search.py`  
**Low-k ledger:** `J2-55-R7-lowk-descent.py`

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

\[
\boxed{\delta>0:\ \textbf{OPEN globally}}
\]

\[
\boxed{\delta=0,\ q>1:\ \textbf{OPEN globally}}
\]

\[
\boxed{\delta=0,\ q=1:\ \textbf{OPEN}}
\]

\[
\boxed{\delta<0,\ q>1:\ \textbf{OPEN}}
\]

\[
\boxed{\delta<0,\ q=1:\ \textbf{OPEN}}
\]

The inherited closures remain frozen, in particular

\[
q=1,\ \delta>0\Longrightarrow\varnothing,
\]

and the reverse zero-tail ray

\[
q>1,\qquad C(q)N-B(q)t=0
\Longrightarrow\varnothing.
\]

The principal R7 result is a **dependency correction**.  The proposed floor-carry integerization is valid, and every proposed stabilized sign computation is correct.  However, the R6 boundary/high/reverse carry-resonance equalities are **not all-exponent equalities**.  They are constant-term equalities valid only after the fixed-fibre finite prefix has been eliminated.  Therefore the hoped-for global implication

\[
\alpha\equiv+8d_\delta t\pmod q
\]

cannot presently be used on every structural fibre.

The exact all-exponent replacement is a carry-residual divisibility.  More strongly, reducing the **full exact root equation** modulo \(q\) does not recover the missing positive opening: it collapses to the already-known RCE quotient relation.  Thus the missing step is genuinely a globalization theorem for the unstable carry residual, not a missing easy mod-\(q\) manipulation.

At the same time R7 proves several new exact facts:

1. \(v_5(q+4)<g\) for every genuine \(q>1,g\ge2\);
2. the integer carry index \(\chi=J-D\mu\) is exact without stabilization;
3. on every active nonzero-tail \(q>1\) fibre, in fact \(q\mid\chi\) already follows from the **negative** tail opening;
4. an undescended exact factorization (DTF0) exists and is stronger in scope than the proposed DTF;
5. the old identity \(t=q^2Z-4a_3\) already gives a global near-\(\sqrt G\) outer bound without any q-descent;
6. the proposed global claim \(\gcd(c,10)=1\) is false; its exact mod-5 replacement is determined;
7. five low-\(k\) outer types die immediately from \(A\)-ten-unit compatibility;
8. the entire proposed double q-descent chain is symbolically valid **conditional on stabilized carry residual zero**, including the high contradiction and the boundary \(q=7\) mod-5 terminal contradiction.

No J2 resonance closure certificate is issued.

---

# Part II — Frozen notation

\[
G=10^g,\qquad K=10^k,\qquad L=10^\ell,
\]

\[
\ell=2g-k,\qquad \delta=k-g=g-\ell,
\]

\[
uq=G+1,\qquad A=2u+1.
\]

For \(q>1\),

\[
c=q^3+10q^2+12q+8,
\]

\[
C=qc,
\qquad
B=(q+2)(q^2-4q-4).
\]

The active nonzero tail is

\[
CN-Bt=\alpha\frac{G}{d_\delta},
\]

with quotient opening

\[
e:=\frac{d_\delta Bt-\alpha}{q}\in\mathbf Z,
\]

hence

\[
\boxed{\alpha\equiv-8d_\delta t\pmod q.}
\tag{TAIL-}
\]

The RCE system is

\[
2Aa_3=q(G-1)Z-N,
\]

\[
(G-1)t=2(q+4)a_3+qN,
\]

\[
q(q+4)Z=At-2N.
\]

---

# Part III — H1 proved: the \(b\ge g\) scope hole disappears

Let

\[
b=v_5(q+4).
\]

Assume \(b\ge g\).  Then

\[
q+4=5^g m,\qquad m\ge1.
\]

Since \(q\mid G+1\),

\[
G\equiv-1\pmod q.
\]

Also \(5^gm\equiv4\pmod q\).  Multiplying by \(2^g\),

\[
mG\equiv 2^{g+2}\pmod q,
\]

so

\[
q\mid m+2^{g+2}.
\]

But

\[
q=5^gm-4,
\]

and for every \(g\ge2\),

\[
5^gm-4>m+2^{g+2}>0.
\]

Contradiction.  Therefore

\[
\boxed{q>1,\ g\ge2\Longrightarrow v_5(q+4)<g.}
\tag{B<G}
\]

Since the live chamber has \(g\ge4\), high and boundary are always inside the active valuation-tail scope.

**Status: PROVED.**

---

# Part IV — Exact carry integerization succeeds

For high/boundary let

\[
d_0=2\cdot5^b,
\qquad
D_{\rm fl}=2d_0q^2(q+4)c.
\]

R6 gives

\[
\frac{uD_2}{\mathcal M}=P_H(G)+r_H(G),
\]

with

\[
J_H(G):=D_{\rm fl}P_H(G)\in\mathbf Z[G].
\]

Define

\[
\boxed{\chi:=J_H-D_{\rm fl}\mu.}
\]

Then for every exponent, without a one-grid assumption,

\[
\boxed{\chi\in\mathbf Z,}
\]

and exactly

\[
\boxed{\varepsilon_{\rm fl}=\mu-P_H=-\frac{\chi}{D_{\rm fl}}.}
\tag{CHI}
\]

Thus R7 Success A is achieved: the floor carry is an exact integer carry index.

The finite alphabet \(0\le\chi\le D_{\rm fl}\) remains only an eventual fixed-fibre statement; the integerization itself is exact.

---

# Part V — Dependency Audit: where the proposed q-descent breaks

R6 does not prove

\[
\varepsilon_{\rm fl}=s+\varepsilon_0
\]

as a raw all-exponent identity.  The logical route is:

1. start from the exact decimal-root congruence;
2. substitute \(\mu=P+\varepsilon_{\rm fl}\);
3. clear a structural denominator;
4. obtain an integer polynomial in \(G\) divisible by \(G\) (or by the reverse decimal scale);
5. for a **fixed fibre**, after the finite prefix, force its constant coefficient to vanish.

Only step 5 gives the displayed R6 carry-resonance equality.

Therefore the following distinction is mandatory:

\[
\boxed{\text{exact root congruence}}
\quad\neq\quad
\boxed{\text{constant coefficient }=0}.
\]

The second is a stabilized fixed-fibre consequence of the first.

This invalidates the proposed direct global chain

\[
\text{BCI/HCI}\Rightarrow +8dt\Rightarrow q\mid t
\]

unless the unstable carry residual is first globally killed.

---

# Part VI — Exact all-exponent Boundary Carry Residual

Define

\[
P_\alpha=2q^4+13q^3+10q^2+12q+8,
\]

\[
P_t=5q^6+12q^5-220q^4-672q^3-368q^2+64q+64.
\]

The proposed BCI is symbolically correct **when the stabilized carry equality is valid**:

\[
\boxed{
\alpha P_\alpha-d_0tP_t
=2q(D_{\rm fl}s+\chi).
}
\tag{BCI}
\]

Define its residual

\[
\boxed{
\Gamma_B:=
\alpha P_\alpha-d_0tP_t-2q(D_{\rm fl}s+\chi).
}
\]

The exact denominator-cleared decimal congruence has constant term

\[
\boxed{
-2d_0q^2t(q+4)\Gamma_B.
}
\]

Consequently every actual boundary root satisfies the exact all-exponent divisibility

\[
\boxed{
G\mid 2d_0q^2t(q+4)\Gamma_B.
}
\tag{B-UNSTABLE}
\]

Equivalently, there is an integer correction \(\Xi_B\) with

\[
\boxed{
2d_0q^2t(q+4)\Gamma_B=G\Xi_B.
}
\tag{B-PREFIX}
\]

The R6 stabilized branch is precisely \(\Xi_B=0\), hence \(\Gamma_B=0\).

This is the required **Unstable Prefix Equation**.  It is global and exact.  What is not yet proved is \(\Xi_B=0\) uniformly when \((q,\alpha,t)\) move with \(g\).

---

# Part VII — Exact High Carry Residual

Let \(H=10^\delta\), \(\delta>0\).  Write the R6 high carry target as

\[
\varepsilon_H=\frac{\mathscr N_H}{2HqD_{\rm fl}},
\]

where

\[
\begin{aligned}
\mathscr N_H={}&-2H^2\alpha q^4-12H^2\alpha q^3
+8H^2d_0q^6t+48H^2d_0q^5t-64H^2d_0q^4t\\
&-320H^2d_0q^3t-128H^2d_0q^2t
-\alpha q^3-10\alpha q^2-12\alpha q-8\alpha\\
&-3d_0q^6t-36d_0q^5t-156d_0q^4t-352d_0q^3t-240d_0q^2t
+64d_0qt+64d_0t.
\end{aligned}
\]

Define

\[
\boxed{\Gamma_H:=\mathscr N_H+2Hq\chi.}
\]

The exact denominator-cleared high decimal congruence has constant term

\[
\boxed{2d_0q^2t(q+4)\Gamma_H.}
\]

Thus every actual high root satisfies

\[
\boxed{
G\mid2d_0q^2t(q+4)\Gamma_H.
}
\tag{H-UNSTABLE}
\]

The stabilized high equality is

\[
\Gamma_H=0
\iff
\mathscr N_H=-2Hq\chi.
\]

Modulo \(q\),

\[
\mathscr N_H\equiv-8\alpha+64d_0t\pmod q,
\]

so **only in the stabilized branch** one obtains

\[
\alpha\equiv+8d_0t\pmod q.
\]

---

# Part VIII — Unexpected stronger theorem: \(q\mid\chi\) is already exact

Although the positive opening is not global, \(q\mid\chi\) actually is.

Substitute

\[
G=qu-1,
\qquad
\alpha=d_0Bt-qe
\]

into the exact integer polynomial \(J_H\).  Symbolic division gives

\[
q\mid J_H.
\]

Since

\[
q^2\mid D_{\rm fl},
\]

we obtain

\[
\boxed{q\mid\chi}
\tag{CHI-q}
\]

on every active high/boundary nonzero-tail fibre, **without** assuming \(q\mid t\) and without stabilization.

More precisely, if

\[
\chi=q\chi_1,
\]

then modulo \(q\),

\[
\boxed{
\chi_1\equiv
8H\bigl(16d_0tu-4d_0t-e\bigr)
\pmod q.
}
\tag{CHI1}
\]

Boundary is \(H=1\).

This supersedes the proposed proof of `CHIq`, which had placed it after first q-descent.

---

# Part IX — Exact root mod q is degenerate, not a source of the missing sign

One might hope to avoid stabilization by returning to the full normalized root equation.  R7 checks this exactly and finds that this does **not** work.

Use

\[
\alpha=d_0Bt-qe,
\qquad
G=qu-1,
\qquad
\chi=q\chi_1,
\]

and the exact residue (CHI1).  After removing the forced \(q^3\)-content from the cleared root numerator, the boundary and high root equations reduce modulo \(q\) to

\[
\boxed{
-16(2u-1)
\bigl(16d_0tu+4d_0t-e\bigr)^2
\equiv0\pmod q.
}
\tag{ROOT-q-DEG}
\]

But the frozen RCE quotient relation already gives

\[
\boxed{
e\equiv4d_0t(4u+1)
=16d_0tu+4d_0t
\pmod q.
}
\tag{QREL}
\]

Therefore (ROOT-q-DEG) is automatically satisfied.

This proves:

\[
\boxed{
\textbf{Exact Root mod-}q\textbf{ Degeneracy Theorem.}
}
\]

The full root equation does **not** supply the positive opening.  The positive sign appears specifically when the unstable carry correction is killed and the constant coefficient is forced to zero.

This is the central dependency result of R7.

---

# Part X — Conditional q-descent package: algebra correct, scope conditional

Assume now, only for this part, that the stabilized carry residual vanishes.

For boundary or high,

\[
\Gamma_{B/H}=0
\]

gives

\[
\alpha\equiv+8d_0t\pmod q.
\]

Together with the tail opening

\[
\alpha\equiv-8d_0t\pmod q,
\]

this gives

\[
q\mid t,\qquad q\mid\alpha.
\]

Then the RCE cascade gives

\[
q\mid N,
\qquad
q\mid a_3.
\]

Thus the proposed first descent is symbolically sound:

\[
\boxed{
\Gamma_{B/H}=0
\Longrightarrow
q\mid(t,\alpha,N,a_3).
}
\tag{QD1-COND}
\]

Write

\[
t=q\tau,\quad \alpha=q\beta,\quad N=qn,\quad a_3=qa.
\]

Then

\[
2Aa=(G-1)Z-n,
\]

\[
(G-1)\tau=2(q+4)a+qn,
\]

\[
(q+4)Z=A\tau-2n.
\]

Elimination gives

\[
\boxed{qZ=4a+\tau.}
\tag{QZ-COND}
\]

The descended quotient is

\[
e_1=\frac{d_0B\tau-\beta}{q}\in\mathbf Z,
\]

so

\[
\beta\equiv-8d_0\tau\pmod q.
\]

Because \(q\mid\chi\) is already global, the second stabilized carry reduction yields

\[
\beta\equiv+8d_0\tau\pmod q,
\]

and hence

\[
\boxed{q\mid\tau,\beta.}
\tag{QD2-COND}
\]

All signs in this conditional chain are certified.

---

# Part XI — Conditional high extinction is valid

The inherited high bound is

\[
0<t<3q+8.
\]

After first descent \(t=q\tau\), \(q\ge7\) gives

\[
0<\tau<3+\frac8q<5.
\]

From \(qZ=4a+\tau\), \(Z,a\) are odd ten-unit data, so \(\tau\) is odd:

\[
\tau\in\{1,3\}.
\]

Second descent gives \(q\mid\tau\), impossible for \(q\ge7\).

Therefore

\[
\boxed{
\Gamma_H=0
\Longrightarrow
\delta>0,\ q>1\Longrightarrow\varnothing.
}
\tag{HIGH-STAB-CLOSE}
\]

Together with the inherited \(q=1\) high closure, the **stabilized high branch** is empty.  This is not yet the full high chamber theorem because \(\Gamma_H=0\) is not globally proved.

---

# Part XII — Conditional boundary q=7 terminal contradiction is valid

Boundary gives

\[
0<t<9q,
\]

so after QD1

\[
\tau\in\{1,3,5,7\}.
\]

QD2 gives \(q\mid\tau\), hence the sole possible cell is

\[
q=7,\qquad \tau=7.
\]

Write

\[
\tau=q\tau_2,\qquad \beta=q\beta_2,
\qquad a=qa_2.
\]

Then

\[
\tau_2=1,
\qquad
Z=4a_2+1,
\qquad
a_3=49a_2.
\]

For \(q=7\),

\[
c=925,\qquad B=153,\qquad d_0=2.
\]

The twice-descended tail equation is

\[
925n-153=\frac{\beta_2G}{2},
\]

while RCE2 gives

\[
n=G-1-22a_2.
\]

Therefore

\[
\boxed{
(1850-\beta_2)G=40700a_2+2156.
}
\tag{Q7-KILL}
\]

Modulo 5 the left side is 0 and the right side is 1.  Contradiction.

Thus

\[
\boxed{
\Gamma_B=0
\Longrightarrow
\delta=0,\ q>1\Longrightarrow\varnothing.
}
\tag{BOUND-STAB-CLOSE}
\]

Again: the terminal algebra is correct; the missing theorem is uniform \(\Gamma_B=0\).

---

# Part XIII — Stronger pre-descent geometry already exists

The proposed identity \(qZ=4a+\tau\) is the descended form of an older exact identity that does **not** require q-descent:

\[
\boxed{q^2Z=4a_3+t.}
\tag{TDEF}
\]

This follows exactly from the RCE system and is symbolically re-certified in R7.

Using

\[
\frac G{10}\le a_3<G,
\]

we obtain globally

\[
\boxed{
\frac{2G}{5}+t\le q^2Z<4G+t.
}
\tag{Z-STRIP0}
\]

Hence \(Z\ge1\) gives

### High

\[
\boxed{q^2<4G+3q+8.}
\tag{H-Q2-GLOBAL}
\]

### Boundary

\[
\boxed{q^2<4G+9q.}
\tag{B-Q2-GLOBAL}
\]

These near-\(\sqrt G\) outer bounds do **not** depend on q-descent and should replace the conditional versions in subsequent work.

---

# Part XIV — New undescended tail factorization DTF0

Before any q-descent, substitute RCE3 into the original tail equation.  Using

\[
c(q+2)-2B=(q+2)^3(q+4),
\]

R7 proves the exact identity

\[
\boxed{
(q+4)\bigl(q^2cZ-t(q+2)^3\bigr)
=
2\frac{G}{d_\delta}\bigl(d_\delta ct-\alpha\bigr).
}
\tag{DTF0}
\]

This is stronger in scope than the proposed DTF because it requires no \(q\mid t\).

For high/boundary, \(d_\delta=d_0=2\cdot5^b\).  Therefore

\[
\boxed{2^g\mid q^2cZ-t(q+2)^3,}
\tag{DTF0-2}
\]

and if \(g\ge2b\),

\[
\boxed{5^{g-2b}\mid q^2cZ-t(q+2)^3.}
\tag{DTF0-5}
\]

So

\[
\boxed{
\frac{G}{5^{2b}}
\mid
q^2cZ-t(q+2)^3
}
\tag{DTF0-10}
\]

when \(g\ge2b\).

In reverse, since

\[
\frac{G}{d_r}=\frac{K}{d_0},
\]

DTF0 becomes an exact fixed-\(K\)-scale identity.  This is now the preferred reverse tail-factor interface, ahead of any conditional q-descent.

---

# Part XV — Correction: \(c\) is not globally a ten-unit

The prompt candidate

\[
c\equiv q^3+3\pmod5
\]

is incorrect.  The exact reduction is

\[
\boxed{
c\equiv q^3+2q+3
\equiv(q-2)(q+1)^2
\pmod5.
}
\tag{c5}
\]

The global ten-unit claim is false.  For example

\[
q=7\quad\Longrightarrow\quad c=925,
\qquad v_5(c)=2.
\]

There is, however, a clean live-chamber classification.  Since

\[
uq=G+1\equiv1\pmod5
\]

and \(A=2u+1\) is a ten-unit, \(q\equiv3\pmod5\) is impossible: it would give \(u\equiv2\pmod5\) and hence \(5\mid A\).

Thus live \(q\) lie in residues \(1,2,4\pmod5\).  Moreover

- \(b>0\iff q\equiv1\pmod5\), and then \(5\nmid c\);
- \(b=0\) forces \(q\equiv2\) or \(4\pmod5\), and then \(5\mid c\).

Therefore

\[
\boxed{
\text{on a legal }q>1\text{ fibre},\quad
\gcd(c,10)=1\iff b>0.
}
\tag{c-unit-split}
\]

Consequences:

1. DTF0-2 is global because \(c\) is odd;
2. the proposed inversion of \(qc\) or \(q^2c\) modulo a decimal modulus is valid only in the \(b>0\) chamber;
3. for \(b=0\), DTF0 instead immediately implies \(5\mid t\), because \(5\mid c\) while \(q+2\) is a 5-adic unit.

This replaces the proposed global `Z-DEC` theorem.

---

# Part XVI — Reverse carry: exact formula recovered

Let

\[
R=10^r,
\qquad d_r=d_0R,
\qquad L=RG.
\]

A structural denominator is

\[
\boxed{
D_R=2R^2d_0q^2(q+4)c.
}
\]

Define

\[
J_R=D_RP_R(G)\in\mathbf Z[G],
\qquad
\chi_R=J_R-D_R\mu.
\]

Then

\[
\varepsilon_{\rm fl}=-\frac{\chi_R}{D_R}.
\]

The reverse constant-term target is

\[
\varepsilon_{\rm fl}=s+\varepsilon_R,
\]

with

\[
\boxed{
\varepsilon_R=
-\frac{\mathscr B_R}
{4R^2d_0q^3(q+4)c},
}
\]

where

\[
\begin{aligned}
\mathscr B_R={}&
3R^3d_0q^6t+36R^3d_0q^5t+156R^3d_0q^4t+352R^3d_0q^3t+240R^3d_0q^2t\\
&-64R^3d_0qt-64R^3d_0t
+R^2\alpha q^3+10R^2\alpha q^2+12R^2\alpha q+8R^2\alpha\\
&-8Rd_0q^6t-48Rd_0q^5t+64Rd_0q^4t+320Rd_0q^3t+128Rd_0q^2t\\
&+2\alpha q^4+12\alpha q^3.
\end{aligned}
\]

If \(\mathscr N_R:=-\mathscr B_R\), define

\[
\Gamma_R:=\mathscr N_R+2q(D_Rs+\chi_R).
\]

The exact denominator-cleared reverse congruence has constant term

\[
\boxed{2Rd_0q^2t(q+4)\Gamma_R.}
\]

Thus every actual reverse root satisfies

\[
\boxed{
G\mid2Rd_0q^2t(q+4)\Gamma_R.
}
\]

Since \(G=RK\), this is exactly

\[
\boxed{
K\mid2d_0q^2t(q+4)\Gamma_R.
}
\tag{REV-UNSTABLE-K}
\]

This is the correct global reverse carry equation.  It naturally lives at the \(K\)-scale, exactly as the low-\(k\) architecture predicts.

---

# Part XVII — Reverse positive opening: conditionally correct, globally unavailable

Modulo \(q\), the reverse stabilized numerator satisfies

\[
\mathscr N_R
\sim
8R^2(8d_rt-\alpha)
\pmod q
\]

up to an invertible sign/unit.

Thus

\[
\Gamma_R=0
\Longrightarrow
\boxed{\alpha\equiv+8d_rt\pmod q.}
\]

Combined with the tail opening this produces the proposed first and second reverse q-descents.

However, the exact full reverse root equation again degenerates modulo \(q\).  After inserting the exact carry quotient residue it becomes

\[
\boxed{
-16R^2(2u-1)
\bigl(16d_rtu+4d_rt-e\bigr)^2
\equiv0\pmod q,
}
\]

and the square already vanishes by the inherited RCE quotient relation.

Therefore

\[
\boxed{
\textbf{REV-PLUS is PROVED only on }\Gamma_R=0\textbf{, not globally.}
}
\]

The correct reverse frontier is now (REV-UNSTABLE-K) + DTF0 + the exact root/defect equations.

---

# Part XVIII — Low-k ledger update

R6 listed 25 low-\(qK\) outer types.  R7 removes five \(k=1\) values immediately using the \(A\)-ten-unit condition:

\[
\boxed{q\in\{13,23,73,103,113\}\Longrightarrow\varnothing.}
\tag{A5-CLOSE}
\]

These are exactly the listed \(q\equiv3\pmod5\) types.

The four frozen deep-5 \(k=1\) exceptions remain

\[
\boxed{q\in\{11,61,91,101\}},
\]

where \(k>b\) fails.

The active \(k=1,b=0\) list is reduced to

\[
\boxed{
q\in\{7,17,19,29,47,49,59,77,89,97,109\}.
}
\]

There are 11 such types.  Every one lies in the \(5\mid c\) branch, so the proposed `c`-inverse decimal residue cannot be used there.

For \(k=2\), the frozen active types remain

\[
q=7\ (b=0,K/d_0=50),
\qquad
q=11\ (b=1,K/d_0=10).
\]

The old \(qK=1169\) bulk/exception split is **not yet retired**, because the global double q-descent that would supersede it has not been proved.

---

# Part XIX — q=1 boundary: one new exact congruence

For \(q=1\), R6 gives

\[
\frac{uD_2}{\mathcal M}
=
\frac{10GN+6Gt-N+3t}{5}
+
\frac{7GN-Gt-4N-4t}{5G(2G+3)}.
\]

Define

\[
J_1:=10GN+6Gt-N+3t,
\qquad
\chi_1:=J_1-5\mu.
\]

Then

\[
\varepsilon_{\rm fl}=-\frac{\chi_1}{5}
\]

exactly.

Substituting this into the **full boundary root equation**, clearing denominators, and reducing modulo \(G\) gives the exact necessary congruence

\[
\boxed{
G\mid(N+t)(31N+21t).
}
\tag{Q1-PROD}
\]

This is stronger than a finite \(s\)-scan and is the new q=1 boundary interface.  No uniform contradiction from (Q1-PROD) is proved in R7, so \(q=1,\delta=0\) remains open.

---

# Part XX — Historical regression

The exact R7 replay reproduces the R6/R3 boundary corpus for \(g\le1200\):

```text
q=7:  28 DCDC states
q=11: 44 DCDC states
q=17:  5 DCDC states
q=19:  2 DCDC states
TOTAL: 79
primitive-pass: 75
```

New q-content statistics:

```text
79 / 79 have q ∤ t
75 / 75 primitive-pass states have q ∤ t
79 / 79 have q | chi
0 / 79 hit Gamma_B=0 for any s in {0,...,20}
```

Thus the historical corpus does not produce a counterexample to the conditional descent.  Instead it shows that the stabilized carry target is never reached in this finite diagnostic corpus.

For the critical high fibre

\[
(q,\delta,\alpha,t)=(11,1,152510,31),
\]

\[
11\nmid31,
\qquad
11\mid\chi.
\]

So if a global first q-descent theorem were available, this fibre would die immediately at \(q\nmid t\).  It is **not** currently legitimate to move its first logical death there, because the fibre fails the high decimal carry target before the proposed stabilized opening is available.

---

# Part XXI — Conjecture ledger H1–H11

| ID | R7 status | Result |
|---|---|---|
| H1 \(b<g\) | **PROVED** | global for \(q>1,g\ge2\) |
| H2 boundary positive opening | **CONDITIONAL PROVED** | valid when \(\Gamma_B=0\); not all-exponent |
| H3 first q-descent | **CONDITIONAL PROVED** | follows from H2 + tail opening |
| H4 second q-descent | **CONDITIONAL PROVED** | signs and \(q\mid\chi\) certified |
| H5 boundary \(q>1\) extinction | **CONDITIONAL PROVED / GLOBAL OPEN** | stabilized branch closes via \(q=7\) mod 5 |
| H6 high extinction | **CONDITIONAL PROVED / GLOBAL OPEN** | stabilized \(q>1\) branch closes; \(q=1\) inherited closed |
| H7 reverse positive opening | **CONDITIONAL PROVED** | valid when \(\Gamma_R=0\) |
| H8 reverse double descent | **CONDITIONAL PROVED** | not global |
| H9 reverse \(q^2<G\) | **CONDITIONAL** | after double descent; global TDEF bound replaces it pre-descent |
| H10 reverse bulk extinction | **OPEN** | no global q-descent |
| H11 q=1 extinction | **OPEN** | new exact product congruence (Q1-PROD) |

---

# Part XXII — Scope / counterexample ledger

### C1 — BOUND-CARRY equality all-exponent exact?

\[
\boxed{\textbf{NO.}}
\]

Correct object: (B-UNSTABLE).  `BCI` is the \(\Gamma_B=0\) stabilized specialization.

### C2 — High numerator mod q wrong?

\[
\boxed{\textbf{NO.}}
\]

The predicted residue \(-8\alpha+64d_0t\) is correct.

### C3 — \(q\nmid\chi\) after descent?

\[
\boxed{\textbf{NO; stronger theorem proved.}}
\]

In fact \(q\mid\chi\) already follows from the tail opening, before first descent.

### C4 — Reverse carry lacks the + sign?

\[
\boxed{\textbf{NO.}}
\]

The + sign is correct on \(\Gamma_R=0\), but that equality is only stabilized.

### C5 — \(b<g\) false?

\[
\boxed{\textbf{NO. H1 proved.}}
\]

### C6 — q=7 terminal identity sign error?

\[
\boxed{\textbf{NO.}}
\]

`Q7-KILL` and the mod-5 contradiction are exact.

### C7 — \(c\) globally ten-unit?

\[
\boxed{\textbf{FALSE.}}
\]

Exact counterexample:

\[
q=7,\qquad c=925,\qquad v_5(c)=2.
\]

---

# Part XXIII — New exact frontier

R7 does **not** freeze the frontier as “21 defects + one periodic carry”.  The sharper exact interface is:

## High / boundary, \(q>1\)

\[
\boxed{q\mid\chi}
\]

plus

\[
\boxed{
G\mid2d_0q^2t(q+4)\Gamma_{H/B},
}
\]

plus the pre-descent identities

\[
\boxed{q^2Z=4a_3+t,}
\]

\[
\boxed{
(q+4)(q^2cZ-t(q+2)^3)
=2\frac{G}{d_0}(d_0ct-\alpha).
}
\]

The missing globalization target is:

\[
\boxed{
\textbf{force }\Gamma_H=0\textbf{ or }\Gamma_B=0
\textbf{ from these exact divisibilities/bounds.}
}
\]

Once that is achieved, the q-descent chain closes the stabilized high and boundary \(q>1\) chambers automatically.

## Reverse, \(q>1\)

The correct exact carry interface is

\[
\boxed{
K\mid2d_0q^2t(q+4)\Gamma_R,
}
\]

together with reverse DTF0 at the fixed \(K/d_0\) scale.  The old double-descent chart is retained only as a conditional terminal lemma.

## q=1 boundary

\[
\boxed{G\mid(N+t)(31N+21t).}
\]

This is now the first q=1 target.

---

# Part XXIV — Success audit

### Success A — carry integerization

\[
\boxed{\textbf{YES.}}
\]

### Success B — first q-descent globally

\[
\boxed{\textbf{NO. Conditional only.}}
\]

### Success C — double q-descent globally

\[
\boxed{\textbf{NO. Conditional only.}}
\]

### Success D — nonnegative tail closure

\[
\boxed{\textbf{NO.}}
\]

### Success E — full nonnegative tail closure

\[
\boxed{\textbf{NO.}}
\]

### Success F — reverse double descent globally

\[
\boxed{\textbf{NO.}}
\]

### Success G — reverse closure

\[
\boxed{\textbf{NO.}}
\]

### Success H — terminal J2 closure

\[
\boxed{\textbf{NO.}}
\]

Therefore

\[
\boxed{\textbf{J2 OPEN}.}
\]

No `J2-Resonance-Closure-Certificate.md` is generated.

---

# Part XXV — Next exact target

The next round should **not** repeat the q-descent algebra.  That algebra is already certified.

The precise missing theorem is one of the following two equivalent globalization routes:

1. **Carry-residual extinction:** use TDEF + DTF0 + DIG3 + the exact carry residual divisibility to prove \(\Gamma_{H/B/R}=0\) uniformly; or
2. **Nonzero unstable-correction exclusion:** assume \(\Gamma\ne0\), write the exact integer correction \(\Xi\ne0\), and prove its required size/divisibility contradicts the q-square/digit/tail bounds.

For high/boundary the newly global q-square bound and DTF0 should be used before any further floor-periodic analysis.

For reverse the natural modulus is \(K\), not \(G\); low-\(k\) should therefore be attacked through `REV-UNSTABLE-K + DTF0`, with the five \(q\equiv3\pmod5\) types permanently removed.

The full-root mod-\(q\) route is retired as a source of new information: R7 proves it is already the square of the inherited quotient relation.
