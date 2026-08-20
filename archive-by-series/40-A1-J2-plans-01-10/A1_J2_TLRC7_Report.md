# A1 J2 TLRC7 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Campaign:** Tail-Parametrized Local Root Obstruction × Fixed-Modulus Periodicity × Low-\(k\) Chamber  
**Inherited source:** `A1_J2_FQTR6_Report.md`  
**Symbolic certificate:** `A1_J2_TLRC7_symbolic.py`  
**Local checker:** `A1_J2_TLRC7_local.py`  
**Exact diagnostic computation:** `A1_J2_TLRC7_search.py`  
**Certificate:** `A1_J2_TLRC7_certificate.txt`  
**Survivor ledger:** `A1_J2_TLRC7_survivors.tsv`

---

# Part I — Executive Status

\[
\boxed{\textbf{Full J2 OPEN}.}
\]

\[
\boxed{h\ge1\textbf{ tail chamber OPEN globally}.}
\]

but a new infinite subchamber is closed:

\[
\boxed{q=1,\ h\ge1\Longrightarrow\varnothing.}
\tag{Q1-HIGH-CLOSE}
\]

The first deficiency edge is therefore

\[
\boxed{h=1\textbf{ OPEN globally},}
\]

with the entire \(q=1\) component closed and, in the exact small-\(q\) diagnostic range \(g\le1200\), only the inherited \(q=11,g=471\) DCDC pseudo-survivor reaching the root gate; it dies modulo \(11\).

The low-\(k\) chamber remains

\[
\boxed{\ell\ge g\quad(k\le g)\quad\textbf{OPEN}.}
\]

However it is no longer an unstructured remainder.  This round proves a **reverse tail allocation** and a separate low-\(k\) root kernel, reducing every fixed \((q,r)\) fibre, \(r=g-k=\ell-g\ge0\), to the same type of one-dimensional cyclotomic lift problem as the high-tail side.

The main new rigorous results are:

1. **Tail-root square-kernel theorem.**  In \(h=g-\ell=k-g\ge1\), the huge quadratic discriminant has the exact square factor \(G^2\):
   \[
   \boxed{\Delta_{\rm std}=G^2\Psi_h,\qquad
   \Psi_h=4u^2 10^{2h}D_2^2-A\widetilde F.}
   \tag{RK-H}
   \]
   Hence discriminant-square is exactly \(\Psi_h\)-square, while root divisibility remains a separate gate.

2. **Tail flattening.**  After the valuation-tail parametrization, \(\Psi_h\) is a rational polynomial in \(G\) with an **exact square denominator** and degree-eight numerator.  Thus all odd-prime local square classes can be computed without the original nested root variables.

3. **Cyclotomic quotient-tail theorem.**  The tail equation admits a second Euclidean quotient
   \[
   \boxed{e=\frac{dB(q)t-\alpha}{q}\in\mathbb Z,\qquad
   d\,c(q)N=\alpha u+e,}
   \tag{CQ}
   \]
   where \(\alpha=\sigma m\), \(d=2\cdot5^b\), \(c(q)=C(q)/q\).  Thus \(N\) is affine in the cyclotomic quotient \(u=(G+1)/q\).

4. **Explicit local root formula at every prime \(p\mid q\).**  The local square class is reduced to a quartic-looking quotient expression in \(A\), a new Euclidean quotient \(\rho\), \(t\), and \(10^h\); see Part IV.

5. **Fixed-fibre periodic/stabilization theorem.**  For fixed \((q,h,\sigma,m,t)\), every denominator/reconstruction/local-DCDC/local-root-residue gate is eventually constant at the decimal primes and periodic at every nondecimal prime.  An explicit safe period and decimal stabilization threshold are given in Part VII.  Global integer-square is *not* claimed periodic.

6. **Complete \(q=1\), high-tail closure.**  The previous \(q=1\) slope gives \(h\le3\).  Fixed-modulus DCDC plus the exact mod-31 period leaves exactly three raw cells at \(h=1\), all killed by the actual \(a_3\) digit/ten-unit gate; \(h=2,3\) have no local-DCDC cells.

7. **Low-\(k\) reverse-tail theorem.**  When \(k\le g\), DCDC forces the complementary tail factor to absorb decimal depth \(K=10^k\).  Apart from a separately controlled zero-tail ray, fixed \((q,r)\) again has finite \((\alpha,t)\) fibres.

Therefore this round achieves a strong form of **Success C3**, plus a new infinite closure \((q=1,h\ge1)\), but not Success A/B/C1 globally.

---

# Part II — Frozen Tail Ledger

Write

\[
G=10^g,\qquad H=\frac G2,\qquad K=10^k,
\]

\[
\ell=2g-k,\qquad h=g-\ell=k-g\quad(h\ge1\text{ in the high-tail chamber}),
\]

\[
uq=G+1,\qquad A=2u+1,\qquad M=q(q+4).
\]

The frozen RCE system is

\[
2Aa_3=q(G-1)Z-N,
\tag{RCE1}
\]

\[
(G-1)t=2(q+4)a_3+qN,
\tag{RCE2}
\]

\[
q(q+4)Z=At-2N.
\tag{RCE3}
\]

The actual radial reconstruction is

\[
\mathcal X=\frac{Z+uN}{2},\qquad D_2=ua_3+G\mathcal X,
\]

and

\[
\widetilde F=A\mathcal X^2+ZD_2.
\]

The root quadratic is

\[
AH^2a_1^2-2uKD_2a_1+\widetilde F=0.
\tag{ROOT-Q}
\]

For \(\ell\ge5\), the decimal core is

\[
2K\mid\widetilde F.
\tag{DCDC}
\]

With

\[
R:=At-2N,
\]

\[
Y:=R+uNM,
\]

\[
E:=uq((G-1)t-qN)+GY,
\]

we have

\[
Z=\frac RM,\qquad \mathcal X=\frac{Y}{2M},\qquad D_2=\frac{E}{2M},
\]

and

\[
\boxed{4M^2\widetilde F=P:=AY^2+2RE.}
\tag{NT}
\]

The previous symbolic polynomial is

\[
q^3P=C_3G^3+C_2G^2+C_1G+C_0,
\]

with

\[
C_0=(qN+t)(C(q)N-B(q)t),
\]

\[
C(q)=q^4+10q^3+12q^2+8q,
\]

\[
B(q)=(q+2)(q^2-4q-4),
\]

and

\[
\gcd(C(q),B(q))\mid7.
\]

For \(q>1\), put

\[
b=v_5(q+4),\qquad d=2\cdot5^b.
\]

In the high-tail chamber \(h\ge1\), the frozen valuation theorem is

\[
v_2(qN+t)=1,\qquad v_5(qN+t)=b,
\]

and

\[
\boxed{\frac Gd\mid C(q)N-B(q)t.}
\tag{VT}
\]

The complementary tail is nonzero there, so write

\[
\boxed{C(q)N-B(q)t=\alpha\frac Gd,\qquad \alpha=\sigma m\ne0.}
\tag{TP1}
\]

Thus

\[
\boxed{N=\frac{B(q)t+\alpha G/d}{C(q)}.}
\tag{TP2}
\]

The exact safe size theorem is

\[
\boxed{0<m<30\cdot5^bq^4\,10^{-h}.}
\tag{MBOUND}
\]

Consequently

\[
\boxed{10^h<30\cdot5^bq^4.}
\tag{HBOUND}
\]

For fixed \(q\), this makes \(h\) finite.

---

# Part III — Tail-Parametrized Root Discriminant

## 3.1 Exact square-kernel reduction

Let \(T=10^h\), so \(K=GT\).  The standard discriminant of (ROOT-Q) is

\[
\begin{aligned}
\Delta_{\rm std}
&=(2uKD_2)^2-4AH^2\widetilde F\\
&=4u^2G^2T^2D_2^2-AG^2\widetilde F.
\end{aligned}
\]

Therefore

\[
\boxed{
\Delta_{\rm std}=G^2\Psi_h,
\qquad
\Psi_h:=4u^2T^2D_2^2-A\widetilde F.
}
\tag{3.1}
\]

Since \(G^2\) is an integer square,

\[
\boxed{\Delta_{\rm std}\text{ is a square}\iff\Psi_h\text{ is a square}.}
\tag{3.2}
\]

This is the correct Layer S object for the remainder of J2.

If \(\Psi_h=s^2\), the two formal roots are

\[
\boxed{
a_1=\frac{2(2uTD_2\pm s)}{AG}.
}
\tag{3.3}
\]

Hence Layer R is the separate divisibility condition

\[
\boxed{AG\mid2(2uTD_2\pm s),}
\tag{3.4}
\]

with positive numerator.  No square test in this report is allowed to absorb (3.4).

## 3.2 Complete tail substitution

Define

\[
c(q):=q^3+10q^2+12q+8,
\qquad C(q)=q\,c(q),
\]

and \(\alpha=\sigma m\).  Then

\[
N_T(G;q,h,\alpha,t)
:=\frac{dB(q)t+\alpha G}{dq\,c(q)}.
\]

Set

\[
u_T=\frac{G+1}{q},\qquad A_T=2u_T+1,
\]

\[
Z_T=\frac{A_Tt-2N_T}{q(q+4)},
\]

\[
a_{3,T}=\frac{(G-1)t-qN_T}{2(q+4)},
\]

\[
X_T=\frac{Z_T+u_TN_T}{2},
\qquad
D_{2,T}=u_Ta_{3,T}+GX_T,
\]

\[
F_T=A_TX_T^2+Z_TD_{2,T}.
\]

Then the desired tail-parametrized discriminant is exactly

\[
\boxed{
\Delta_{\rm std}(G,q,h,\sigma,m,t)
=G^2\left(4u_T^2 10^{2h}D_{2,T}^2-A_TF_T\right).
}
\tag{TRD}
\]

No \(N,Z,\mathcal X,D_2,C_1\) remains free in (TRD); each is a displayed deterministic rational function of \((G,q,h,\sigma,m,t)\), integral on a legal tail cell.

## 3.3 Square-denominator flattening

The symbolic certificate performs the complete substitution and proves

\[
\boxed{
\Psi_h
=\frac{\mathscr D_{q,h,\alpha,t}(G)}
{\left(2dq^3(q+4)c(q)\right)^2},
}
\tag{FLAT-PSI}
\]

where

\[
\boxed{\deg_G\mathscr D_{q,h,\alpha,t}=8.}
\]

The denominator is itself a perfect square.  Thus for every odd prime not lost to the denominator, the local square class can be read from the normalized numerator after the exact denominator valuation is removed.  The expanded degree-eight polynomial is produced deterministically by `A1_J2_TLRC7_symbolic.py`; the factorized form (TRD)+(FLAT-PSI) is retained in the report because it exposes the arithmetic structure much more clearly than several pages of expanded coefficients.

---

# Part IV — mod-\(q\) Square-Class Reduction

The naive hope

\[
G\equiv-1\pmod q
\quad\Longrightarrow\quad
\Psi_h\bmod q\text{ depends only on }(h,\alpha,t)
\]

is **false as a structural simplification**.  Division by \(q\) creates cyclotomic quotient data that survives modulo primes dividing \(q\).

## 4.1 First quotient: tail quotient \(e\)

Starting from

\[
dq\,c(q)N-dB(q)t=\alpha G
\]

and using \(G=qu-1\), we get

\[
q\bigl(dc(q)N-\alpha u\bigr)=dB(q)t-\alpha.
\]

Hence every legal tail cell satisfies

\[
\boxed{q\mid dB(q)t-\alpha,}
\tag{E-CONG}
\]

and the integer

\[
\boxed{e:=\frac{dB(q)t-\alpha}{q}}
\]

satisfies

\[
\boxed{dc(q)N=\alpha u+e.}
\tag{E-N}
\]

This is a genuine dimensional collapse: for fixed \((q,h,\alpha,t)\), \(e\) is fixed, and \(N\) is affine in the single cyclotomic quotient \(u=(10^g+1)/q\).

## 4.2 Second quotient: \(\rho\)

RCE3 gives

\[
\boxed{
\rho:=\frac{At-2N}{q}=(q+4)Z\in\mathbb Z.
}
\tag{RHO}
\]

Thus the correct local state at a prime \(p\mid q\) is not merely \(G=-1\), but the pair of quotient residues

\[
(u\bmod p,\ \rho\bmod p).
\]

## 4.3 Exact local square-class kernel

Let \(p\mid q\) be odd.  Since \(q\) is a ten-unit, \(p\ne2,5\).  Modulo \(p\),

\[
G\equiv-1,
\qquad A=2u+1.
\]

From \(At-2N=q\rho\),

\[
N\equiv\frac{At}{2}.
\]

RCE2 and RCE3 give

\[
a_3\equiv-\frac t4,
\qquad
Z\equiv\frac\rho4.
\]

Define

\[
P_0:=\rho+A(A-1)t,
\]

\[
Q_0:=\rho+(A^2-1)t.
\]

Then

\[
\mathcal X\equiv\frac{P_0}{8},
\qquad
D_2\equiv-\frac{Q_0}{8},
\]

and

\[
64\widetilde F
\equiv
AP_0^2-2\rho Q_0.
\]

Therefore the root square kernel satisfies

\[
\boxed{
64\Psi_h\equiv
(A-1)^2 10^{2h}Q_0^2
-A^2P_0^2
+2A\rho Q_0
\pmod p.
}
\tag{LOCAL-q}
\]

Because \(64=8^2\), (LOCAL-q) has exactly the same nonzero quadratic character as \(\Psi_h\).

This is the main local-root theorem of the round.

## 4.4 The inherited \(q=11\) pseudo-survivor

For

\[
(q,h,g,t,\alpha)=(11,1,471,31,152510),
\]

all RCE, digit, ten-unit, radial, tail, valuation-tail, and DCDC gates pass.  The new kernel gives

\[
\boxed{\Psi_h\equiv8\pmod{11}.}
\]

Since \(8\) is a quadratic nonresidue modulo \(11\), Layer S dies immediately.

The quotient form gives

\[
\rho\equiv9\pmod{11},
\]

and (LOCAL-q) returns

\[
64\Psi_h\equiv6\pmod{11},
\]

which is consistent because \(64\cdot8\equiv6\pmod{11}\).

At the auxiliary primes,

\[
\Psi_h\equiv1\pmod3,
\qquad
\Psi_h\equiv2\pmod7,
\]

both quadratic residues.  Hence the prime \(7\) is **not** a universal root killer; the special \(\gcd(B,C)\mid7\) collision does not by itself close the root gate.

---

# Part V — mod-\((q+4)\) and Auxiliary Local Obstructions

The same principle applies to any odd prime

\[
p\mid q+4.
\]

Here \(q\equiv-4\pmod p\) and

\[
G=uq-1\equiv-4u-1\pmod p.
\]

Unlike the \(p\mid q\) chart, no universal simplification removes \(u\).  The exact checker therefore evaluates \(\Psi_h\) after the tail reconstruction and tests every odd prime divisor of

\[
q(q+4).
\]

For the \(q=11\) pseudo-survivor, the only new odd prime from \(q+4=15\) is \(3\), and

\[
\Psi_h\equiv1\pmod3.
\]

So the \((q+4)\) stack is a genuine supplement, not a universal replacement for the \(q\)-prime obstruction.

The report therefore does **not** assert LRT-B.  The proved object is the local obstruction stack plus explicit periodicity, not a claim that one of \(q\) or \(q+4\) always supplies a nonresidue.

---

# Part VI — \(h=1\) Campaign

## 6.1 Global status

\[
\boxed{h=1\textbf{ remains OPEN globally for variable }q.}
\]

No uniform theorem

\[
\forall\text{ legal }h=1\text{ cell}\ \exists p\mid q:\ (\Psi_h/p)=-1
\]

has been proved.

## 6.2 Complete \(q=1\) high-tail closure

For \(q=1\), the previous slope theorem gives

\[
g\le\ell+3.
\]

Hence in the high-tail chamber

\[
h=g-\ell\in\{1,2,3\}.
\]

The \(q=1\) polynomial is

\[
\begin{aligned}
100\widetilde F={}&
G^3(50N^2+60Nt+20t^2)\\
&+G^2(115N^2+170Nt+66t^2)\\
&+G(100N^2+158Nt+68t^2)\\
&+(N+t)(31N+21t).
\end{aligned}
\tag{Q1-POLY}
\]

The first tail factor obeys

\[
v_2(N+t)=v_5(N+t)=1,
\]

and the previous \(q=1\) tail gives

\[
31N+21t=\alpha\frac G{10},\qquad\alpha\ne0.
\tag{Q1-TAIL}
\]

Since \(2K=2G10^h\mid\widetilde F\), division of (Q1-POLY) by \(G\) gives, once \(g\ge h+4\), the exact fixed local condition

\[
\boxed{
200\cdot10^h
\mid
100N^2+158Nt+68t^2
+\alpha\frac{N+t}{10}.
}
\tag{Q1-LOCAL}
\]

Current frontier \(\ell\ge6\) gives \(g\ge h+6\), so the stabilization hypothesis is automatic.

The N-strip and DIG3 yield the safe bounds

\[
1\le t\le11,
\]

and

\[
|\alpha|\le
\begin{cases}
161,&h=1,\\
16,&h=2,\\
1,&h=3.
\end{cases}
\tag{Q1-ABOUND}
\]

Because

\[
N=\frac{\alpha10^{g-1}-21t}{31},
\]

all integrality and (Q1-LOCAL) data depend only on

\[
g\pmod{15},
\]

since \(\operatorname{ord}_{31}(10)=15\), after the already satisfied decimal stabilization threshold.

The complete exact one-period census is:

| \(h\) | tail-integral cells | local-DCDC cells | legal linear cells |
|---:|---:|---:|---:|
| 1 | 853 | 3 | 0 |
| 2 | 78 | 0 | 0 |
| 3 | 3 | 0 | 0 |

The three \(h=1\) raw cells are represented by

\[
(g\bmod15,\alpha,t)=(0,130,8),(2,150,5),(9,110,1).
\]

They die uniformly as follows.

### Cell A: \((\alpha,t)=(110,1)\)

\[
N=\frac{11G-21}{31}>0.
\]

But

\[
a_3=\frac{G-1-N}{10}<\frac G{10},
\]

so DIG3 fails for every member of the residue class.

### Cell B: \((\alpha,t)=(130,8)\), \(g\equiv0\pmod{15}\)

\[
a_3=\frac{47G-16}{62}.
\]

For \(g\equiv0\pmod{15}\),

\[
G\equiv32\pmod{124},
\]

hence \(47G-16\equiv0\pmod{124}\), so

\[
2\mid a_3.
\]

Thus the required ten-unit condition fails.

### Cell C: \((\alpha,t)=(150,5)\)

\[
a_3=\frac{14G-5}{31}.
\]

Since \(31\equiv1\pmod5\) and \(14G-5\equiv0\pmod5\),

\[
5\mid a_3.
\]

Again the ten-unit gate fails.

Therefore

\[
\boxed{q=1,\ h\ge1\Longrightarrow\varnothing.}
\]

This is a new infinite closure, not a bounded-\(g\) computation.

## 6.3 Fixed-small-\(q\) diagnostic

For the actual small fixed divisors

\[
q\in\{7,11,17,19\},
\]

HBOUND gives

\[
\boxed{H_7=4,\qquad H_{11}=6,\qquad H_{17}=6,\qquad H_{19}=6.}
\]

The exact diagnostic census through \(g\le1200\), respecting the order classes and full tail integrality, gives:

- \(q=7\): no legal DCDC cell for \(1\le h\le4\);
- \(q=11\): exactly one legal DCDC cell, at \(h=1,g=471\); it is the known mod-11 nonresidue pseudo-survivor;
- \(q=17\): no legal DCDC cell for \(1\le h\le6\);
- \(q=19\): no legal DCDC cell for \(1\le h\le6\).

This is **diagnostic only**.  It is not promoted to an infinite fixed-small-\(q\) closure, because reconstruction/root data retain nondecimal periodic lifts beyond this finite range.

---

# Part VII — Fixed-Fibre Periodicity / Stabilization

This round proves the requested theorem in a corrected form: **decimal stabilization + nondecimal periodicity**.

Fix

\[
(q,h,\alpha,t),\qquad \alpha=\sigma m\ne0.
\]

Define

\[
S_f:=2dq^3(q+4)c(q).
\]

From (FLAT-PSI),

\[
\Psi_h=\frac{\mathscr D(G)}{S_f^2}.
\]

## 7.1 Nondecimal local period

Let \(p\ne2,5\) be any prime used by a denominator, reconstruction gate, or local-root test, and put

\[
s_p=v_p(S_f).
\]

To recover the normalized value of \(\Psi_h\bmod p\), it is enough to know

\[
\mathscr D(G)\pmod{p^{2s_p+1}}.
\]

Since \(G=10^g\), this depends only on

\[
g\pmod{\operatorname{ord}_{p^{2s_p+1}}(10)}.
\]

Thus for any finite local prime stack \(\mathcal P\), one explicit period is

\[
\boxed{
T_{q,\mathcal P}
=\operatorname{lcm}_{p\in\mathcal P\cup\mathcal P_{\rm den}}
\operatorname{ord}_{p^{2s_p+1}}(10),
}
\tag{PER}
\]

where \(\mathcal P_{\rm den}\) is the set of nondecimal primes appearing in the fixed denominators.  Equivalently, a conservative one-modulus implementation can use the nondecimal part of \(S_f^3\).

The order condition \(q\mid10^g+1\) is simply intersected with this period.

## 7.2 Decimal stabilization

At the high-tail local-DCDC depth

\[
2^{h+3}5^{h+2b},
\]

and with the square denominator \(S_f^2\), a safe stabilization threshold is

\[
\boxed{
g_{\rm dec}
=\max\bigl(h+3+2v_2(S_f),\ h+2b+2v_5(S_f)\bigr).
}
\tag{GSTAB}
\]

For \(g\ge g_{\rm dec}\), every required power of \(10^g\) vanishes modulo the lifted 2/5 modulus, so the decimal local data are constant on the fixed fibre.

## 7.3 Inequality gates

After tail substitution, every digit/sign/radial inequality is a rational polynomial inequality in \(G\) with fixed denominator.  Clear the positive denominator.  For a nonzero polynomial

\[
f(G)=a_dG^d+\cdots+a_0,
\]

one explicit Cauchy threshold is

\[
R_f=1+\max_{j<d}\left|\frac{a_j}{a_d}\right|.
\]

For \(G>R_f\), the sign equals the sign of \(a_d\).  Hence each inequality is eventually constant, with an explicit finite prefix.

## 7.4 What the theorem does and does not prove

Therefore:

> **Fixed-Fibre Local Periodicity Lemma.**  For fixed \((q,h,\sigma,m,t)\), RCE integrality, local-DCDC, all chosen local root square tests, and all digit/sign/radial inequalities are determined by a finite prefix plus finitely many residue classes modulo an explicit period.

This is stronger than a vague “finite-checkable” claim and supplies the explicit period/stabilization mechanism requested in the prompt.

However:

\[
\boxed{\text{the global condition }\Psi_h=s^2\text{ is not claimed periodic}.}
\]

A fixed fibre is completely closed by one period only when the local obstruction stack kills every allowed residue class.  Local-square residue classes that survive still require a global square/root-divisibility argument.

For the known \(q=11,h=1\) fibre, the conservative implementation returns a finite safe period and

\[
g_{\rm dec}=8.
\]

The period is intentionally conservative; optimization is irrelevant to the theorem.

---

# Part VIII — Variable-\(q\) Globalization

## 8.1 Formal \(h\)-ceiling

From MBOUND and \(m\ge1\),

\[
\boxed{10^h<30\cdot5^bq^4.}
\]

Thus fixed \(q\) has a finite \(h\)-list.

## 8.2 Tail-coordinate outer splice

The inherited outer wedge is

\[
q^2<\frac{73}{2}\left(1+\frac1G\right)^2 10^{2\ell-h}.
\]

HBOUND gives

\[
q^2>\frac{10^{h/2}}{\sqrt{30\cdot5^b}}.
\]

Combining,

\[
\boxed{
10^{3h/2}
<\frac{73}{2}\sqrt{30\cdot5^b}
\left(1+\frac1G\right)^2 10^{2\ell}.
}
\tag{H-OUT}
\]

Therefore

\[
\boxed{
h<\frac43\ell
+\frac23\log_{10}\!\left[
\frac{73}{2}\sqrt{30\cdot5^b}\left(1+\frac1G\right)^2
\right].}
\tag{H-WEDGE}
\]

For the ordinary chamber \(b=0\), the additive constant is about \(1.54\), recovering the \(7/3\)-type slope directly in the new \((\ell,h,q)\) chart.

This is the correct globalization interface for the tail coordinates, but it does not by itself close variable \(q\): the exceptional \(5\)-adic depth \(b=v_5(q+4)\) and the cyclotomic quotient residues remain live.

## 8.3 Why fixed fibre is not global closure

Even though fixed \(q\) gives finite \(h,m,t\), the pair \((q,h)\) is globally unbounded.  The local formula (LOCAL-q) therefore identifies the new missing theorem precisely:

\[
\boxed{
\text{control the cyclotomic quotient residues }(u,\rho)
\text{ across variable }q.
}
\]

This is lower-dimensional than the old \((g,\ell,q,N,t)\) frontier and more precise than “continue local roots.”

---

# Part IX — Low-\(k\) Chamber

Put

\[
\boxed{r:=g-k=\ell-g\ge0,\qquad K=\frac G{10^r}.}
\]

The low-\(k\) chamber is **not closed** this round, but it receives an independent tail/root reduction.

## 9.1 The cheap theorem \(k>g\) does not follow from the frozen pre-DCDC package

There is an exact \(q=1\) pre-DCDC family

\[
N=7,\qquad t=3,
\]

with

\[
Z=\frac{6G}{5}-1,
\]

\[
a_3=\frac{3G}{10}-1,
\]

\[
\mathcal X=\frac{41G}{10}+3,
\]

\[
D_2=\frac{44G^2+23G-10}{10}.
\]

For every sampled \(g\ge4\) and every \(1\le k\le g\), it passes the exact RCE, positivity, ten-unit, DIG3, and inherited radial inequalities.  Analytically, these formulas have the correct signs and leading coefficients throughout the same range.

But

\[
\widetilde F\equiv3\pmod5,
\]

so DCDC fails for every \(k\ge1\).

Thus a proof of \(k>g\), if true for full J2 states, **must use the decimal/root package**; it cannot be extracted from the already-frozen linear/digit/radial gates alone.

## 9.2 Reverse valuation-tail allocation

For \(q>1\), DCDC gives

\[
8KM^2\mid P.
\]

Because \(K\mid G\), reducing the cubic polynomial \(q^3P\) modulo \(K\) leaves only the constant tail:

\[
\boxed{K\mid(qN+t)(C(q)N-B(q)t).}
\tag{LOW-PROD}
\]

Using

\[
v_2(qN+t)=1,\qquad v_5(qN+t)=b
\]

when \(b<g\), we obtain

\[
\boxed{
2^{k-1}5^{\max(k-b,0)}
\mid C(q)N-B(q)t.
}
\tag{LOW-VT}
\]

In the eventual fixed-\((q,r)\) range \(k>b\), this is

\[
\boxed{
\frac{G}{2\cdot5^b10^r}
\mid C(q)N-B(q)t.
}
\tag{LOW-VT2}
\]

There are two branches.

### Zero-tail ray

If

\[
C(q)N-B(q)t=0,
\]

then \(\gcd(B,C)\mid7\) forces

\[
t\ge\frac{C(q)}7>\frac{q^4}{7}.
\]

The low-\(k\) digit/N-strip gives the safe bound

\[
t<9q10^r.
\]

Hence a zero-tail state must satisfy

\[
\boxed{q^3<63\cdot10^r.}
\tag{ZERO-RAY}
\]

So the zero ray is itself confined to a diagonal \((q,r)\)-wedge.

### Nonzero reverse tail

Otherwise write

\[
\boxed{
C(q)N-B(q)t
=\alpha\frac{G}{2\cdot5^b10^r},
\qquad \alpha\ne0.
}
\tag{LOW-TP}
\]

The N-strip and \(t<9q10^r\) give the safe size bound

\[
\boxed{
0<|\alpha|<30\cdot5^bq^4\,10^{2r}.
}
\tag{LOW-M}
\]

Thus **fixed \((q,r)\)** again has finite \((\alpha,t)\) fibres.

With

\[
d_r:=2\cdot5^b10^r,
\]

the same quotient-tail identity becomes

\[
\boxed{
e_r:=\frac{d_rB(q)t-\alpha}{q}\in\mathbb Z,
\qquad
d_rc(q)N=\alpha u+e_r.
}
\tag{LOW-CQ}
\]

This is the low-\(k\) analogue of (CQ).

## 9.3 Low-\(k\) root square kernel

Since

\[
K=\frac G{10^r},
\]

the standard discriminant factors instead as

\[
\boxed{
\Delta_{\rm std}=K^2\Psi_r^{-},
\qquad
\Psi_r^{-}:=4u^2D_2^2-A10^{2r}\widetilde F.
}
\tag{RK-L}
\]

Hence Layer S is

\[
\Psi_r^{-}=s^2,
\]

and Layer R is

\[
\boxed{
AG10^r\mid2(2uD_2\pm s).
}
\tag{ROOT-L}
\]

This is the promised independent Low-\(k\) Chamber Ledger.  The chamber is no longer hidden in global OPEN: it is a reverse-tail cyclotomic fibre plus a separate root-square/root-divisibility gate.

---

# Part X — \(\ell=6\) Diagnostic Certificate

No independent \(\ell=6\) exhaustive search is used in this round.  This is deliberate: the round obtained infinite theorems (root-kernel reduction, fixed-fibre local periodicity, complete \(q=1\) high-tail closure, and low-\(k\) reverse-tail compression) that strictly dominate a single-layer certificate as a research target.

Accordingly no `A1_J2_TLRC7_L6_certificate.txt` is generated, and no \(\ell=6\) closure is claimed.

---

# Part XI — Counterexample / Survivor Ledger

The actual ledger is `A1_J2_TLRC7_survivors.tsv`.

## 11.1 Genuine DCDC/root pseudo-survivor

\[
(q,h,g,t,\alpha)=(11,1,471,31,152510)
\]

passes the full pre-root package and DCDC, then dies at

\[
\Psi_h\equiv8\pmod{11}.
\]

This continues to falsify DCDC-only closure.

## 11.2 \(q=1,h=1\) local-DCDC raw cells

Exactly three periodic raw cells survive the fixed local congruence, but each dies at DIG3/ten-unit before becoming a legal tail state.  They certify that the \(q=1\) proof genuinely needs the actual digit legality after the periodic local filter.

## 11.3 Low-\(k\) pre-DCDC family

The \((q,N,t)=(1,7,3)\) family shows that low-\(k\) RCE/digit/radial pseudo-states exist for \(k\le g\).  It is killed uniformly by \(\widetilde F\equiv3\pmod5\).

## 11.4 Conjecture audit

- **C1 \(h=1\Rightarrow\varnothing\): OPEN globally.**  Closed for \(q=1\); small-\(q\) diagnostics strongly support it but do not prove variable \(q\).
- **C2 mod-\(q\) always gives a nonresidue: OPEN.**  No legal DCDC counterexample was found in the reported small-\(q\) diagnostic, but no universal proof exists.
- **C3 \(q+4\) always补杀 mod-\(q\) survivor: OPEN.**
- **C4 fixed \((q,h)\) conditions eventually stabilize: REFINED/PROVED.**  Decimal data stabilize; nondecimal data are periodic rather than generally constant.
- **C5 \(k>g\) uniformly: OPEN as a full-state theorem.**  The proposed cheap derivation from frozen linear/digit/radial gates is falsified by the explicit low-\(k\) family.
- **C6 \(\ell\ge g\) empty: OPEN.**
- **C7 all genuine local-square states have \(m=1\): OPEN.**
- **C8 prime 7 is a universal root obstruction: FALSE.**  The \(q=11\) DCDC pseudo-survivor has \(\Psi_h\equiv2\pmod7\), a quadratic residue; the actual killer is \(11\).

---

# Part XII — Closure Audit

## 12.1 Positive resonance

Frozen closed; not reopened.

## 12.2 \(k=2g+1\), \(k=2g\), \(\ell=1,\ldots,5\)

Frozen closed; not reopened.

## 12.3 \(g=2,3\), \(u=1\)

Frozen closed; not reopened.

## 12.4 \(q=1\)

High-tail \(h\ge1\) is newly closed by the period-15 fixed-modulus argument.  Low-\(k\) \(q=1\) remains part of the reverse-tail chamber.

## 12.5 \(q>1\), \(b=0\) and \(b>0\)

Both are retained through \(d=2\cdot5^b\).  All valuation allocations state the needed hypothesis \(b<g\); fixed \(q\) has only a finite exceptional prefix if this fails.

## 12.6 \(\sigma=\pm1\)

Both signs are retained in \(\alpha=\sigma m\).  The small-\(q\) diagnostic solves the signed congruence on the full symmetric interval \([-m_{\max},m_{\max}]\setminus\{0\}\).

## 12.7 Local square versus global square

Separated.  A local nonresidue kills Layer S.  Local residue does not imply global square.

## 12.8 Root divisibility

Kept separate as (3.4) in high-tail and (ROOT-L) in low-\(k\).

## 12.9 Primitive gcd / common-\(U\)

Neither is discarded.  No state is declared a full survivor merely by passing the local root screen.  Since the full J2 closure is not claimed, later primitive/common-\(U\) gates remain active on any future global-square/root-divisible survivor.

## 12.10 Exact arithmetic

All square tests use `math.isqrt`; all congruences, valuations and rational inequalities use Python integers / `Fraction` / exact SymPy integer algebra.  No floating-point decision is used in any certificate.

---

# Part XIII — New Frontier

\[
\boxed{\textbf{J2 remains OPEN}.}
\]

But the old terminal chart

\[
(q,h,\sigma,m,t;g)
\]

can now be sharpened further.

## 13.1 High-tail frontier: Cyclotomic Quotient-Root Fibre (CQRF)

For \(q>1,h\ge1\), fix

\[
(q,h,\alpha,t),
\]

with

\[
0<|\alpha|<30\cdot5^bq^4 10^{-h}.
\]

Then define deterministically

\[
e=\frac{dBt-\alpha}{q},
\]

\[
N=\frac{\alpha u+e}{dc},
\qquad
\rho=\frac{At-2N}{q},
\qquad
u=\frac{10^g+1}{q}.
\]

The remaining obstruction is

\[
\boxed{
\textbf{CQRF}:
\begin{cases}
q\mid10^g+1,\\
N,\rho\in\mathbb Z,\\
\text{fixed local-DCDC},\\
\text{(LOCAL-q) square class at }p\mid q,\\
\text{auxiliary local stack},\\
\Psi_h=s^2,\\
AG\mid2(2u10^hD_2\pm s).
\end{cases}}
\]

The key new fact is that the local motion in \(g\) occurs only through **cyclotomic quotient residues** \((u,\rho)\), and those residues are periodic at fixed nondecimal modulus.

The next highest-value theorem is therefore not another wedge improvement.  It is a **quotient-residue compatibility theorem** coupling

\[
10^g\equiv-1\pmod q
\]

with the square class in (LOCAL-q), ideally eliminating all local-period classes for variable \(q\).

## 13.2 Low-\(k\) frontier: Reverse CQRF

For \(r=g-k\ge0\), either the zero-tail ray satisfies

\[
q^3<63\cdot10^r,
\]

or the nonzero branch has

\[
C N-Bt=\alpha\frac{G}{2\cdot5^b10^r},
\]

with finite \((\alpha,t)\) for fixed \((q,r)\), quotient-tail identity (LOW-CQ), and root kernel (RK-L).

Thus the low-\(k\) chamber has also been reduced to a **reverse cyclotomic quotient-root fibre**, not left as a raw open wedge.

## 13.3 Status summary

\[
\boxed{q=1,\ h\ge1\textbf{ CLOSED}}
\]

\[
\boxed{q>1,\ h\ge1\textbf{ OPEN at CQRF}}
\]

\[
\boxed{h=1\textbf{ OPEN globally, locally highly compressed}}
\]

\[
\boxed{\ell\ge g\textbf{ OPEN at reverse CQRF}}
\]

No J2 Resonance Closure Certificate is issued.

---

# File Audit

Generated and checked:

```text
A1_J2_TLRC7_Report.md
A1_J2_TLRC7_symbolic.py
A1_J2_TLRC7_local.py
A1_J2_TLRC7_search.py
A1_J2_TLRC7_certificate.txt
A1_J2_TLRC7_search_certificate.txt
A1_J2_TLRC7_survivors.tsv
```

Not generated because no independent \(\ell=6\) search was used:

```text
A1_J2_TLRC7_L6_certificate.txt
```

Final verdict:

```text
VERDICT_FULL_J2=OPEN
VERDICT_HIGH_TAIL=OPEN_GLOBALLY
VERDICT_Q1_HIGH_TAIL=CLOSED
VERDICT_H1=OPEN_GLOBALLY
VERDICT_LOW_K=OPEN_COMPRESSED
FIXED_FIBRE_LOCAL_PERIODICITY=PROVED
ROOT_KERNEL_REDUCTION=PROVED
LOW_K_REVERSE_TAIL=PROVED
```

FINAL_REPORT_FILE: A1_J2_TLRC7_Report.md

SYMBOLIC_FILE: A1_J2_TLRC7_symbolic.py

LOCAL_CHECK_FILE: A1_J2_TLRC7_local.py

COMPUTATION_FILE: A1_J2_TLRC7_search.py

CERTIFICATE_FILE: A1_J2_TLRC7_certificate.txt

SURVIVOR_FILE: A1_J2_TLRC7_survivors.tsv
