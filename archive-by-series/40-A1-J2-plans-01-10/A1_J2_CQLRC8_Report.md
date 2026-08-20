# A1 J2 CQLRC8 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** Cyclotomic Quotient-Lift × Root Square-Class Compatibility × High/Low Tail Unification  
**Inherited source:** `A1_J2_TLRC7_Report.md`  
**Quotient symbolic certificate:** `A1_J2_CQLRC8_quotient.py`  
**Root symbolic certificate:** `A1_J2_CQLRC8_root.py`  
**Exact diagnostic computation:** `A1_J2_CQLRC8_search.py`  
**Diagnostic certificate:** `A1_J2_CQLRC8_search_certificate.txt`  
**Master certificate:** `A1_J2_CQLRC8_certificate.txt`  
**Survivor ledger:** `A1_J2_CQLRC8_survivors.tsv`

---

# Part I — Executive Status

\[
\boxed{\textbf{Full J2 OPEN}.}
\]

\[
\boxed{h\ge1\textbf{ OPEN globally}.}
\]

\[
\boxed{h=1\textbf{ OPEN globally}.}
\]

\[
\boxed{h=0\textbf{ OPEN globally}.}
\]

\[
\boxed{h<0\textbf{ / Reverse-CQRF OPEN globally}.}
\]

The frozen infinite closure

\[
\boxed{q=1,\ h\ge1\Longrightarrow\varnothing}
\]

remains valid.  No J2 Resonance Closure Certificate is issued this round.

This round nevertheless reaches the requested core structural target in a corrected form.  The decisive new theorem is not that the cyclotomic quotient residue \(u\bmod p\) is sparse.  Generically it is the opposite: along the allowed order class it runs through an affine progression and, when the first lifting coefficient is a unit, it runs through all of \(\mathbf F_p\).  What creates rigidity is the **simultaneous quotient ladder**:

\[
\boxed{
\text{tail quotient}
\Longrightarrow
\rho\text{-integrality fixes }n\bmod p^a
\Longrightarrow
\rho\bmod p\text{ is affine in the next digit }z
\Longrightarrow
\Psi_\delta\bmod p=F_{p,\delta,t}(z),
}
\]

where \(F_{p,\delta,t}\) has degree at most two.

Thus the three residues \((u,e,\rho)\) are indeed not independent.  More precisely, at a nondegenerate prime \(p^a\Vert q\), the RCE quotient consumes the first \(a\) base-\(p\) digits of the order-class index, and the root square class reads only the next digit.  This is the round's **Cyclotomic Quotient-Lift / Quotient-Root Compatibility Theorem**.

Where the frozen valuation-tail allocation is active, the same quotient-lift theorem applies on both sides of \(k=g\); the root-kernel unification itself is unconditional.  Introducing

\[
\delta:=k-g,
\qquad
\mathfrak a_\delta:=10^{\max(\delta,0)},
\qquad
\mathfrak b_\delta:=10^{\max(-\delta,0)},
\]

one obtains one unified root kernel

\[
\boxed{
\Psi_\delta
=4u^2\mathfrak a_\delta^2D_2^2
-A\mathfrak b_\delta^2\widetilde F,
}
\tag{U-RK}
\]

and

\[
\boxed{
\Delta_{\rm std}
=\left(\frac{G}{\mathfrak b_\delta}\right)^2\Psi_\delta.
}
\tag{U-DS}
\]

This specializes exactly to the frozen high-tail \(\Psi_h\), the boundary \(\Psi_0\), and the reverse-tail \(\Psi_r^-\).

Two strong candidate closure mechanisms are **disproved**:

1. a prime \(p\mid q\) is not automatically available for Layer-R root selection, because \(p\nmid AG\) in general;
2. even a complete structural local stack at the primes of \(q(q+4)c(q)B(q)\) does not always kill a fixed fibre.

The second failure is witnessed inside the same \(q=11,h=1,\alpha=152510,t=31\) fibre.  The inherited \(g=471\) state dies modulo \(11\), but at \(g=63501\) the root kernel is a residue or zero at **every odd structural prime**

\[
3,7,11,13,73,383,
\]

while it is still not a global integer square.  Hence a single-prime or fixed structural-prime Legendre obstruction cannot be the final globalization theorem.

The correct new frontier is lower-dimensional than CQRF:

\[
\boxed{
\text{one Hensel next-index digit }z_p
\quad+\quad
\text{one quadratic local square class }F_{p,\delta,t}(z_p).
}
\]

The remaining global problem is to synchronize these one-digit conditions across the prime powers of variable \(q\), or to connect them to a genuinely global square/root factor condition.

**Round verdict:** Success C2 and a strong corrected Success C3 are achieved; high/low quotient theory is unified (Success C4 at theorem level), but Success A/B/C1 are not achieved.

---

# Part II — Frozen Quotient Ledger

Throughout

\[
G=10^g,\qquad K=10^k,\qquad \ell=2g-k,
\qquad \delta:=k-g=g-\ell,
\]

\[
uq=G+1,\qquad A=2u+1.
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

Also

\[
\mathcal X=\frac{Z+uN}{2},
\qquad
D_2=ua_3+G\mathcal X,
\qquad
\widetilde F=A\mathcal X^2+ZD_2.
\]

Define

\[
c(q):=q^3+10q^2+12q+8,
\]

\[
C(q):=q\,c(q)=q^4+10q^3+12q^2+8q,
\]

\[
B(q):=(q+2)(q^2-4q-4).
\]

The frozen tail factor is

\[
G\mid(qN+t)(C(q)N-B(q)t),
\]

and

\[
\gcd(C(q),B(q))\mid7.
\]

For \(q>1\), let

\[
b:=v_5(q+4),\qquad d_0:=2\cdot5^b.
\]

For the unified exponent coordinate put

\[
\mathfrak a:=10^{\max(\delta,0)},
\qquad
\mathfrak b:=10^{\max(-\delta,0)},
\qquad
d_\delta:=d_0\mathfrak b.
\]

Then

\[
G=S\mathfrak b,
\qquad
K=S\mathfrak a,
\qquad
S:=\frac{G}{\mathfrak b}=\frac{K}{\mathfrak a}.
\]

### High tail \(\delta=h\ge1\)

In the frozen valuation-tail chamber \(b<g\), here \(\mathfrak a=10^h,\mathfrak b=1,d_\delta=d_0\), and the nonzero tail is

\[
C(q)N-B(q)t=\alpha\frac{G}{d_0},
\qquad \alpha=\sigma m\ne0,
\]

with

\[
0<m<30\cdot5^bq^4\,10^{-h},
\qquad
0<t<3q+8.
\]

### Boundary \(\delta=0\)

This is the \(r=0\) reverse-tail interface.  In the active reverse valuation-tail range \(k=g>b\), the reverse zero-tail ray would imply

\[
q^3<63,
\]

which is impossible for genuine \(q>1\), because then \(q\ge7\).  Hence every boundary state **inside this valuation-tail range** lies in the nonzero tail fibre

\[
C(q)N-B(q)t=\alpha\frac{G}{d_0},
\qquad \alpha\ne0.
\]

The safe reverse bound is

\[
0<|\alpha|<30\cdot5^bq^4,
\qquad
0<t<9q.
\]

### Low \(k\), \(\delta=-r<0\)

In the frozen eventual reverse-tail range \(k>b\), here \(\mathfrak a=1,\mathfrak b=10^r,d_\delta=d_r=d_0 10^r\).  Away from the separately bounded zero-tail ray,

\[
C(q)N-B(q)t
=\alpha\frac{G}{d_r},
\qquad \alpha\ne0,
\]

with

\[
0<|\alpha|<30\cdot5^bq^4\,10^{2r},
\qquad
t<9q10^r.
\]

In every nonzero branch the same quotient algebra holds:

\[
\boxed{
e:=\frac{d_\delta B(q)t-\alpha}{q}\in\mathbf Z,
}
\tag{Q-e}
\]

\[
\boxed{
d_\delta c(q)N=\alpha u+e.
}
\tag{Q-N}
\]

The actual RCE quotient is

\[
\boxed{
\rho:=\frac{At-2N}{q}=(q+4)Z\in\mathbf Z.
}
\tag{Q-rho}
\]

These are the only quotient variables needed below.

---

# Part III — Cyclotomic Quotient Lift

## 3.1 Prime-power next-digit theorem

Let

\[
p^a\Vert q,
\qquad p\ne2,5,
\]

and let

\[
r:=\operatorname{ord}_{p^a}(10).
\]

Because \(10^g\equiv-1\pmod{p^a}\), the order \(r\) is even and every allowed exponent is

\[
g=g_0+nr,
\qquad
g_0\equiv r/2\pmod r.
\]

Write the two one-step lifts

\[
10^r\equiv1+\mu p^a\pmod{p^{a+1}},
\]

\[
10^{g_0}\equiv-1+\chi_0p^a\pmod{p^{a+1}}.
\]

Then

\[
10^{g_0+nr}
\equiv(-1+\chi_0p^a)(1+n\mu p^a)
\equiv-1+(\chi_0-n\mu)p^a
\pmod{p^{a+1}}.
\]

Therefore

\[
\boxed{
\chi_{p,g}:=\frac{10^g+1}{p^a}\pmod p
\equiv \chi_0-n\mu\pmod p.
}
\tag{CQL-p}
\]

Squaring the half-order lift gives

\[
10^r=(10^{g_0})^2
\equiv1-2\chi_0p^a\pmod{p^{a+1}},
\]

so

\[
\boxed{\mu\equiv-2\chi_0\pmod p.}
\tag{half-lift}
\]

If \(\mu\not\equiv0\pmod p\), the quotient residue \(\chi_{p,g}\) runs affinely through all of \(\mathbf F_p\) as \(n\) runs through \(\mathbf F_p\).  Thus the next digit is **structured but not sparse**.

If \(\mu\equiv0\pmod p\), one is in the deeper lift / base-10 Wieferich-type exceptional chamber and must lift one level further.  No generic Wieferich theory is invoked here.

If

\[
q=p^aq',\qquad p\nmid q',
\]

then

\[
\boxed{
u=\frac{10^g+1}{q}
\equiv(q')^{-1}\chi_{p,g}\pmod p.
}
\tag{u-from-chi}
\]

This proves the requested prime-power cyclotomic quotient lift for arbitrary \(a\ge1\).

## 3.2 Composite-\(q\) order-class recurrence

For the actual fixed-\(q\) fibre it is cleaner to use the order modulo \(q\) itself.  Let

\[
T:=\operatorname{ord}_q(10),
\qquad g_0:=T/2,
\]

so every allowed exponent is

\[
g=g_0+nT.
\]

Set

\[
R:=10^T,
\qquad
L_q:=\frac{R-1}{q},
\qquad
u_n:=\frac{10^{g_0+nT}+1}{q}.
\]

Then the recurrence is exact over \(\mathbf Z\):

\[
\boxed{
u_{n+1}=Ru_n-L_q.
}
\tag{u-rec}
\]

Since \(R\equiv1\pmod q\), for every \(p\mid q\),

\[
\boxed{
u_n\equiv u_0-nL_q\pmod p.
}
\tag{u-aff}
\]

Define

\[
\lambda_p:=L_q\pmod p.
\]

If \(\lambda_p\ne0\), \(u\bmod p\) again runs through all residues as \(n\bmod p\) varies.

The exact regression table is:

| \(q\) | \(T\) | \(g_0\) | \(L_q\bmod q\) | \(u_0\bmod q\) |
|---:|---:|---:|---:|---:|
| 7 | 6 | 3 | 1 | 3 |
| 11 | 2 | 1 | 9 | 1 |
| 17 | 16 | 8 | 8 | 13 |
| 19 | 18 | 9 | 15 | 2 |

The non-squarefree checks

\[
q=49\quad(p=7,a=2),
\qquad
q=121\quad(p=11,a=2)
\]

also satisfy the same affine recurrence, with nonzero lifting coefficient.  Thus the mechanism is not an artifact of squarefree \(q\).

---

# Part IV — Quotient Relations

## 4.1 Opening congruences

For every odd prime \(p\mid q\),

\[
B(q)\equiv-8\pmod p,
\qquad
c(q)\equiv8\pmod p.
\]

Since

\[
q\mid d_\delta B(q)t-\alpha,
\]

we immediately obtain

\[
\boxed{
\alpha\equiv-8d_\delta t\pmod p.
}
\tag{Amodp}
\]

and from \(d_\delta cN=\alpha u+e\),

\[
8d_\delta N\equiv\alpha u+e\pmod p.
\]

Because \(\rho\in\mathbf Z\),

\[
2N\equiv At=(2u+1)t\pmod p.
\]

Substitution gives the stronger first quotient relation

\[
\boxed{
e\equiv4d_\delta t(4u+1)\pmod p.
}
\tag{QREL-1}
\]

This is the cheapest actual splice between the tail quotient and the cyclotomic quotient.

## 4.2 Exact affine numerator for \(\rho\)

Using

\[
N=\frac{\alpha u+e}{d_\delta c},
\qquad A=2u+1,
\]

we obtain

\[
\begin{aligned}
qd_\delta c\,\rho
&=d_\delta c(2u+1)t-2(\alpha u+e)\\
&=2(d_\delta ct-\alpha)u+d_\delta ct-2e.
\end{aligned}
\]

Thus define

\[
\boxed{
J(u):=2(d_\delta ct-\alpha)u+d_\delta ct-2e.
}
\]

Then

\[
\boxed{
qd_\delta c\,\rho=J(u).
}
\tag{QREL-exact}
\]

Since \(p\mid q\) implies \(c\equiv8\not\equiv0\pmod p\), and \(d_\delta\) is a power of \(2,5\),

\[
\gcd(q,d_\delta c)=1.
\]

Therefore

\[
\boxed{
\rho\in\mathbf Z
\iff q\mid J(u).
}
\tag{rho-int}
\]

inside an already tail-integral fibre.  This is the exact quotient equation that drives the Hensel ladder.

## 4.3 Hensel index-digit theorem

Fix \(p^a\Vert q\), put \(q=p^aq'\), and suppose

\[
p\nmid t,
\qquad
\lambda_p=L_q\not\equiv0\pmod p.
\]

Modulo \(p\), the coefficient of \(u\) in \(J\) is

\[
2(d_\delta ct-\alpha)
\equiv2(8d_\delta t+8d_\delta t)
=32d_\delta t,
\]

which is a unit.  Hence the congruence

\[
p^a\mid J(u_n)
\]

has a unique solution

\[
\boxed{n\equiv n_*\pmod{p^a}.}
\tag{n-star}
\]

The lift is explicit.  From the exact recurrence and \(R=1+qL_q\), for \(0\le j\le a\),

\[
\boxed{
 u_{n+p^j}-u_n
\equiv-p^jL_q\pmod{p^{j+1}}.
}
\tag{u-Hensel-step}
\]

Thus the first quotient/RCE integrality consumes one base-\(p\) digit of \(n\) at each stage.

Now write

\[
n=n_*+p^az.
\]

Then modulo \(p^{a+1}\),

\[
u_n\equiv u_*-zp^aL_q.
\]

Divide \(J(u_n)\) by \(q=p^aq'\) and by the unit \(d_\delta c\).  The next quotient residue is

\[
\boxed{
\rho\equiv\rho_*-4t\lambda_p(q')^{-1}z\pmod p.
}
\tag{rho-next}
\]

The striking point is that the tail scale \(d_\delta\), including all dependence on

\[
b=v_5(q+4)
\]

and on the reverse-tail factor \(10^r\), cancels from the slope.  Therefore the same Hensel quotient theorem works for high tail, boundary, and low tail.

### Degenerate chambers

The theorem above deliberately records its hypotheses.  Two residual local chambers remain:

1. \(p\mid t\), where the first derivative \(32d_\delta t\) vanishes;
2. \(\lambda_p\equiv0\pmod p\), where the cyclotomic order class has a deeper lift and \(u\bmod p\) is constant at first order.

Neither is silently discarded.

---
# Part V — Root Square-Class Reduction

## 5.1 High/low unification

Put

\[
\mathfrak a=10^{\max(\delta,0)},
\qquad
\mathfrak b=10^{\max(-\delta,0)},
\qquad
S=G/\mathfrak b=K/\mathfrak a.
\]

The standard discriminant is

\[
\begin{aligned}
\Delta_{\rm std}
&=(2uKD_2)^2-4A(G/2)^2\widetilde F\\
&=S^2\left(4u^2\mathfrak a^2D_2^2-A\mathfrak b^2\widetilde F\right).
\end{aligned}
\]

Hence

\[
\boxed{
\Psi_\delta
:=4u^2\mathfrak a^2D_2^2-A\mathfrak b^2\widetilde F,
}
\]

\[
\boxed{
\Delta_{\rm std}=S^2\Psi_\delta.
}
\]

Therefore Layer S is exactly

\[
\boxed{\Psi_\delta=s^2.}
\]

The quadratic root becomes

\[
\boxed{
a_1=\frac{2(2u\mathfrak aD_2\pm s)}{AG\mathfrak b},
}
\]

so Layer R is

\[
\boxed{
AG\mathfrak b\mid2(2u\mathfrak aD_2\pm s).
}
\tag{U-ROOT}
\]

For \(\delta=h>0\), this is the frozen high-tail kernel.  For \(\delta=-r<0\), multiplying by \(10^r\) gives exactly the frozen reverse kernel.  At \(\delta=0\) the two sides meet without a normalization jump.

## 5.2 Unified local formula at \(p\mid q\)

Let \(p\mid q\) be odd and define

\[
P_0:=\rho+A(A-1)t,
\qquad
Q_0:=\rho+(A^2-1)t.
\]

The frozen RCE local reduction gives

\[
\mathcal X\equiv\frac{P_0}{8},
\qquad
D_2\equiv-\frac{Q_0}{8}
\pmod p.
\]

Substitution into the unified kernel gives

\[
\boxed{
64\Psi_\delta\equiv
(A-1)^2\mathfrak a^2Q_0^2
-A^2\mathfrak b^2P_0^2
+2A\mathfrak b^2\rho Q_0
\pmod p.
}
\tag{LOCAL-DELTA}
\]

Because \(64=8^2\), this has the same nonzero quadratic character as \(\Psi_\delta\).

As a polynomial in \(\rho\), its degree is at most two.  The \(\rho^2\)-coefficient is

\[
\boxed{
\kappa_\delta
=(A-1)^2(\mathfrak a^2-\mathfrak b^2)+\mathfrak b^2.
}
\tag{rho2}
\]

The discriminant of the polynomial in \(\rho\) is

\[
\boxed{
4A^2\mathfrak b^2t^2(A-1)^2
\left(\kappa_\delta+\mathfrak b^2\right).
}
\tag{rho-disc}
\]

These identities are checked symbolically by `A1_J2_CQLRC8_root.py`.

## 5.3 Quotient-Root Compatibility Theorem

Under the nondegenerate hypotheses of Part IV, write

\[
n=n_*+p^az,
\]

so \(u\bmod p\) is already fixed and

\[
\rho\equiv\rho_*+\gamma_p z\pmod p,
\qquad
\gamma_p=-4t\lambda_p(q')^{-1}.
\]

Substitution into (LOCAL-DELTA) gives

\[
\boxed{
64\Psi_\delta\equiv F_{p,\delta,t}(z)\pmod p,
\qquad \deg F_{p,\delta,t}\le2.
}
\tag{QRC}
\]

Consequently

\[
\boxed{
\Psi_\delta\text{ square in }\mathbf Z
\Longrightarrow
F_{p,\delta,t}(z)\in(\mathbf F_p)^2\cup\{0\}.
}
\tag{QRC-square}
\]

This is the requested quotient-root compatibility result.  It is stronger than fixed-periodicity: the remaining local motion is literally one next Hensel digit and a quadratic polynomial.

It is also the precise sense in which the three quotient residues cannot move independently:

- \(e\) is fixed by the tail fibre;
- \(\rho\)-integrality fixes \(n\bmod p^a\);
- \(\rho\bmod p\) is affine in only the next digit \(z\);
- the root square class is a quadratic function of that same \(z\).

## 5.4 Why one prime cannot generically finish the proof

A tempting strengthening would be to show that the polynomial \(F(z)\) is a nonresidue for every \(z\in\mathbf F_p\).  This is false in general.

For a nonconstant quadratic over an odd finite field, the quadratic-character sum is too small for all nonzero values to be nonresidues; in the repeated-root case the polynomial has a zero.  A nonconstant linear polynomial also runs through every residue.  Thus a universal single-prime killer can occur only in degenerate constant situations, not as the generic consequence of quotient lifting.

Accordingly, (QRC) is a **dimension collapse and local filter**, not by itself a universal extinction theorem.

---

# Part VI — \(h=1\) Campaign

## 6.1 Exact \(q=11,g=471\) quotient-lift regression

Take

\[
q=11,\quad h=1,\quad g=471,\quad \alpha=152510,\quad t=31.
\]

For \(q=11\),

\[
T=\operatorname{ord}_{11}(10)=2,
\qquad
g_0=1,
\]

and

\[
L_q=\frac{10^2-1}{11}=9.
\]

Hence

\[
g=1+2n,
\qquad
n=235\equiv4\pmod{11},
\]

and

\[
u\equiv1-9n\equiv9\pmod{11}.
\]

Here \(b=v_5(15)=1\), so \(d=10\).  The exact tail quotient is

\[
e=\frac{10B(11)\cdot31-152510}{11}=12880,
\]

therefore

\[
e\equiv10\pmod{11}.
\]

The reconstructed residues are

\[
N\equiv3\pmod{11},
\qquad
\rho\equiv9\pmod{11}.
\]

All opening relations check:

\[
\alpha\equiv-8dt\equiv6\pmod{11},
\]

\[
e\equiv4dt(4u+1)\equiv10\pmod{11}.
\]

The first quotient integrality fixes

\[
\boxed{n\equiv4\pmod{11}.}
\]

Write

\[
n=4+11z.
\]

Then the Hensel next-digit theorem gives

\[
\boxed{
\rho\equiv4+6z\pmod{11}.
}
\tag{q11-rho}
\]

The local root polynomial produces the exact table:

| \(z\) | \(\rho\) | \(64\Psi_1\bmod11\) | class |
|---:|---:|---:|:---|
|0|4|4|residue|
|1|10|8|nonresidue|
|2|5|7|nonresidue|
|3|0|1|residue|
|4|6|1|residue|
|5|1|7|nonresidue|
|6|7|8|nonresidue|
|7|2|4|residue|
|8|8|6|nonresidue|
|9|3|3|residue|
|10|9|6|nonresidue|

For \(g=471\),

\[
z=21\equiv10\pmod{11},
\]

so

\[
64\Psi_1\equiv6\pmod{11},
\]

and equivalently

\[
\boxed{\Psi_1\equiv8\pmod{11},}
\]

which is a quadratic nonresidue.

This pinpoints the mechanism: **the nonresidue is not forced by \(u\bmod11\) alone.  It is produced by the next quotient digit \(z\) after RCE integrality has selected the first index class.**

## 6.2 Same-fibre counterexamples

The strong conjecture

\[
\text{“this fixed fibre is always killed modulo }11\text{”}
\]

is false.

Within the same fixed fibre

\[
(q,h,\alpha,t)=(11,1,152510,31),
\]

the exact shifted states include:

| \(g\) | \(\Psi_1\bmod11\) | \(\rho\bmod11\) | mod-11 status |
|---:|---:|---:|:---|
|471|8|9|nonresidue|
|13077|9|4|residue|
|50895|5|0|residue|
|63501|5|6|residue|
|101319|9|2|residue|
|126531|4|3|residue|

Therefore even a fixed \((q,h,\alpha,t)\) fibre is not uniformly killed by \(p\mid q\).

The most important state is \(g=63501\).  For the odd prime support of

\[
q(q+4)c(q)B(q),
\]

namely

\[
\{3,7,11,13,73,383\},
\]

its root residues are

\[
\begin{array}{c|cccccc}
p&3&7&11&13&73&383\\ \hline
\Psi_1\bmod p&1&2&5&0&72&331
\end{array}
\]

and every entry is a square or zero.  Yet exact integer arithmetic shows

\[
\boxed{\Psi_1\text{ is not an integer square}.}
\]

Hence the candidate “structural local obstruction stack always kills” is disproved.

## 6.3 Small-\(q\) exact diagnostic through \(g\le1200\)

The new script independently reproduces the previous \(h=1\) census:

| \(q\) | tail-integral | reconstructed | linear-legal | DCDC | local-\(q\) square | global square |
|---:|---:|---:|---:|---:|---:|---:|
|7|11144|142|29|0|0|0|
|11|355643|10760|1096|1|0|0|
|17|15198|43|3|0|0|0|
|19|15454|26|3|0|0|0|

The single DCDC cell is the known \(q=11,g=471\) state and dies locally.

This is diagnostic only.  Since the same fixed fibre has residue shifts at much larger \(g\), the finite \(g\le1200\) table cannot be promoted to an infinite \(h=1\) closure.

Therefore

\[
\boxed{h=1\textbf{ remains OPEN globally}.}
\]

---

# Part VII — \(h=0\) Campaign

## 7.1 Boundary quotient fibre

At \(h=0\),

\[
\delta=0,
\qquad
\mathfrak a=\mathfrak b=1.
\]

The reverse zero-tail condition would require \(q^3<63\), impossible for \(q\ge7\).  Hence the boundary is entirely in the nonzero quotient fibre.

The unified root kernel is

\[
\boxed{
\Psi_0=4u^2D_2^2-A\widetilde F.
}
\]

The local formula collapses dramatically:

\[
\boxed{
64\Psi_0
\equiv
\bigl(\rho+(A-1)t\bigr)^2
-2A^2(A-1)^2t^2
\pmod p.
}
\tag{BOUND-LOCAL}
\]

Thus the boundary root problem is a one-variable quadratic/norm-type condition after quotient lifting.

This simplification is genuine, but it does not itself imply extinction.

## 7.2 Exact diagnostic through \(g\le1200\)

Using the reverse-tail bound \(t<9q\), the exact boundary census gives:

| \(q\) | tail-integral | reconstructed | linear-legal | DCDC | local-\(q\) square | local \(q(q+4)\) square | global square |
|---:|---:|---:|---:|---:|---:|---:|---:|
|7|221288|2900|370|28|28|28|0|
|11|8713715|264156|10214|44|20|20|0|
|17|413750|1164|32|5|3|2|0|
|19|437896|969|21|2|0|0|0|

Therefore, in this diagnostic range,

\[
\boxed{79\text{ DCDC boundary pseudo-cells reach the root layer},}
\]

but

\[
\boxed{0\text{ have a global integer-square }\Psi_0.}
\]

The table is strong evidence that \(h=0\) may be close to closure, but it also gives explicit local-square survivors.  Consequently a proof of boundary extinction cannot simply assert a universal \(p\mid q\) or \(p\mid q(q+4)\) Legendre killer.

Thus

\[
\boxed{h=0\textbf{ remains OPEN globally}.}
\]

---
# Part VIII — Reverse-CQRF

The quotient-lift theorem itself does not distinguish high and low \(k\).

For \(r=g-k>0\), set

\[
\delta=-r,
\qquad
\mathfrak a=1,
\qquad
\mathfrak b=10^r,
\qquad
d_r=2\cdot5^b10^r.
\]

The frozen nonzero reverse tail is

\[
C(q)N-B(q)t=\alpha\frac{G}{d_r},
\]

with

\[
e_r=\frac{d_rB(q)t-\alpha}{q},
\qquad
d_rc(q)N=\alpha u+e_r.
\]

The exact same affine quotient numerator is

\[
\boxed{
qd_rc\,\rho
=2(d_rct-\alpha)u+d_rct-2e_r.
}
\tag{LOW-QREL}
\]

Since \(d_r\) remains a \(2,5\)-unit at every \(p\mid q\), all primewise opening congruences remain unchanged in form:

\[
\alpha\equiv-8d_rt\pmod p,
\]

\[
e_r\equiv4d_rt(4u+1)\pmod p.
\]

At a nondegenerate \(p^a\Vert q\), RCE integrality again determines a unique

\[
n\equiv n_*\pmod{p^a},
\]

and, after writing \(n=n_*+p^az\),

\[
\boxed{
\rho\equiv\rho_*-4t\lambda_p(q')^{-1}z\pmod p.
}
\]

The root kernel becomes

\[
\boxed{
\Psi_{-r}=4u^2D_2^2-A10^{2r}\widetilde F=\Psi_r^-.
}
\]

Hence the same one-digit quadratic compatibility theorem holds:

\[
64\Psi_r^-
\equiv F^-_{p,r,t}(z)\pmod p,
\qquad\deg F^-\le2.
\]

This is a genuine **Reverse-CQRF quotient-lift theorem**, not a separate ad hoc method.

What remains open is globalization over variable \(r,q\), plus the separately frozen zero-tail ray

\[
q^3<63\cdot10^r.
\]

Therefore

\[
\boxed{h<0\textbf{ remains OPEN, but the quotient theorem is unified}.}
\]

---

# Part IX — Variable-\(q\) Globalization

## 9.1 What primewise lifting actually gives

Suppose

\[
q=\prod_i p_i^{a_i}.
\]

At every nondegenerate prime power \(p_i^{a_i}\), the quotient equation gives a unique congruence

\[
n\equiv n_i^*\pmod{p_i^{a_i}}.
\]

If the local conditions are mutually compatible, CRT compresses the order-class index to at most one class modulo the corresponding product of prime powers.  The root square condition then constrains the **next** digits

\[
z_i=\frac{n-n_i^*}{p_i^{a_i}}\pmod{p_i}
\]

through quadratic conditions

\[
F_i(z_i)\in(\mathbf F_{p_i})^2\cup\{0\}.
\]

This is a strong reduction from a moving huge integer \(g\) to finitely many local next digits.

## 9.2 Why this is not yet a global contradiction

The primewise root filters generally retain roughly half of the possible next digits.  CRT alone therefore does not force emptiness.  The \(q=11\) shifted-fibre examples explicitly show that the allowed next digit can move from nonresidue to residue while all earlier quotient conditions remain legal.

Moreover the \(g=63501\) example shows that adding every odd structural prime dividing

\[
q(q+4)c(q)B(q)
\]

still need not kill the state locally.

Thus G1 in the prompt — a universal primewise nonresidue formula — is false in that strong form.

## 9.3 Product-of-primes amplification status

No theorem of the form

\[
\operatorname{rad}(q)\mid F(h,t,\alpha)
\]

has been proved from local square compatibility.  The local condition is a quadratic-character restriction rather than a divisibility restriction, so the hoped-for product amplification does not arise automatically.

A possible remaining route is to combine:

1. the CRT class forced by \(\rho\)-integrality;
2. the next-digit square-class sets for all \(p^a\Vert q\);
3. one genuinely global square condition or a prime supplied by the value of \(\Psi_\delta\), not merely by the fixed coefficient support.

That is a much narrower target than variable-\(q\) CQRF, but it is not closed here.

## 9.4 The role of \(b=v_5(q+4)\)

Whenever the frozen valuation-tail allocation is active, at every \(p\mid q\), \(p\ne2,5\), and therefore \(d_\delta=2\cdot5^b\mathfrak b\) is a unit.  The quotient-lift slope

\[
-4t\lambda_p(q')^{-1}
\]

contains no \(b\).  Thus \(b\) is not a hidden infinite local parameter in the quotient-root theorem.  It remains relevant only to the tail size bounds and decimal-depth allocation.

Both \(b=0\) and positive \(b\) are therefore covered by the same primewise quotient algebra **once the valuation-tail allocation applies**.  The deep branches \(b\ge g\) on the high side, or \(b\ge k\) on the reverse side, remain in the inherited outer-suppressed/finite-prefix treatment and are not silently promoted to CQRF.

---

# Part X — Layer-R Root Compatibility

## 10.1 Correction to the proposed \(p\mid q\) root selection

Layer R is

\[
AG\mathfrak b\mid2(2u\mathfrak aD_2\pm s).
\]

A prime \(p\mid q\) satisfies

\[
G\equiv-1\pmod p,
\]

so \(p\nmid G\).  Also \(p\nmid\mathfrak b\), because \(\mathfrak b\) is a power of \(10\).  Therefore

\[
p\mid q
\]

**does not imply**

\[
p\mid AG\mathfrak b.
\]

Consequently it is generally invalid to deduce

\[
s\equiv\pm2u\mathfrak aD_2\pmod p
\]

merely from \(p\mid q\).

The inherited \(q=11,g=471\) state gives an exact regression:

\[
A\equiv8\pmod{11},
\qquad
G\equiv10\pmod{11},
\]

hence

\[
\gcd(AG,11)=1.
\]

So mod-11 Layer R supplies **no** root-selection congruence there.

## 10.2 When a local Layer-R test is legitimate

If a prime \(p\mid A\), then Layer R genuinely constrains the square root modulo the appropriate power of \(p\).  The same is true at the decimal primes according to the exact valuation of \(AG\mathfrak b\).  Those are legitimate root-selection primes.

But they are a different support from the default \(p\mid q\) square-class primes.  The report therefore keeps:

- Layer S at \(p\mid q\) as the quotient-root quadratic-character test;
- Layer R only at primes actually dividing the root denominator.

No fake splice between the two is used.

## 10.3 Status

No global theorem that every local-square survivor is killed by Layer R has been proved.  The integral root-divisibility gate remains active after global square.

---

# Part XI — Computational Census

All decisions in the supplied scripts use exact integer arithmetic, exact modular arithmetic, `Fraction`, and integer square roots.  No floating-point decision is used.

## 11.1 Quotient symbolic regression

`A1_J2_CQLRC8_quotient.py` certifies:

- the exact recurrence \(u_{n+1}=10^T u_n-L_q\);
- the affine residue law \(u_n\equiv u_0-nL_q\pmod p\);
- the exact quotient relation \(qd_\delta c\rho=J(u)\);
- the \(q=11\) first/next-index digit regression;
- non-squarefree checks at \(q=49,121\).

Status:

```text
QUOTIENT_SYMBOLIC_STATUS=PASS
```

## 11.2 Root symbolic regression

`A1_J2_CQLRC8_root.py` certifies:

- high/boundary/low root-kernel unification;
- the unified local formula (LOCAL-DELTA);
- its \(\rho^2\)-coefficient and discriminant;
- the boundary norm form;
- the full \(q=11\) next-digit table;
- the invalidity of automatic Layer-R reduction mod \(p\mid q\);
- the shifted same-fibre counterexamples, including the all-structural-local-square \(g=63501\) state.

Status:

```text
ROOT_SYMBOLIC_STATUS=PASS
```

## 11.3 \(h=0,1\) exact census

`A1_J2_CQLRC8_search.py` is the reproducer for the exact small-\(q\) diagnostic through

\[
g\le1200,
\qquad
q\in\{7,11,17,19\}.
\]

The exact count ledger is saved in `A1_J2_CQLRC8_search_certificate.txt`; the 80 DCDC/root-layer rows are saved in `A1_J2_CQLRC8_survivors.tsv`.

Aggregate results:

```text
h=0: DCDC=79, global integer square=0
h=1: DCDC=1,  global integer square=0
```

The \(h=1\) DCDC row is exactly \(q=11,g=471\).

These counts are diagnostic and are not used as an infinite closure substitute.

---

# Part XII — Counterexample Ledger

## C1 — “\(u\bmod p\) is sparse along the allowed order class”

**DISPROVED generically.**  If the lift coefficient is nonzero, \(u\bmod p\) is affine with nonzero slope and runs through all of \(\mathbf F_p\).

## C2 — “\(e\bmod p\) is independent of RCE quotient legality”

**DISPROVED.**  On a legal \(\rho\)-quotient,

\[
e\equiv4d_\delta t(4u+1)\pmod p.
\]

## C3 — “\(\rho\bmod p\) is a free residue after fixing \(u\)”

**DISPROVED in the nondegenerate chamber.**  RCE integrality fixes \(n\bmod p^a\), and \(\rho\) is affine in the next digit \(z\).

## C4 — “\(h=1\) is uniformly dead at \(p\mid q\)”

**DISPROVED as a local theorem.**  The same \(q=11,h=1,\alpha,t\) fibre has both mod-11 nonresidue and residue lifts.

## C5 — “\(h=0\) is killed by the same local prime”

**DISPROVED in the tested local sense.**  There are many boundary DCDC cells that are local squares at all primes of \(q(q+4)\).

## C6 — “some prime \(p\mid q\) always gives a local nonresidue”

**DISPROVED.**  Boundary examples already violate this, and the shifted \(q=11\) high-tail fibre has mod-11 residue lifts.

## C7 — “Layer S survive implies Layer R can be tested mod the same \(p\mid q\)”

**DISPROVED as stated.**  A prime divisor of \(q\) need not divide the Layer-R modulus \(AG\mathfrak b\).

## C8 — “all structural primes \(q(q+4)cB\) suffice”

**DISPROVED.**  The exact \(q=11,g=63501\) state is square/zero at all odd structural primes but is not a global square.

## C9 — “high and reverse CQRF require different lifting theorems”

**DISPROVED.**  After \(d_\delta=d_0\mathfrak b\) and the unified root kernel, the quotient-lift theorem is identical on both sides.

---

# Part XIII — Closure Audit

The following audit is explicit.

### Frozen closures

- \(S_R>0\): **CLOSED**.
- \(S_R<0\): only the reduced negative frontier remains.
- \(k=2g+1\): **CLOSED**.
- \(k=2g\): **CLOSED**.
- \(\ell=1,2,3,4,5\): **CLOSED**.
- \(u=1\): **CLOSED**.
- \(g=2,3\): **CLOSED**.
- \(q=1,h\ge1\): **CLOSED**.

### Current live exponent chambers

- \(q>1,h\ge1\): **OPEN**, with quotient-root one-digit reduction.
- \(h=1\): **OPEN**.
- \(h=0\): **OPEN**, zero-tail excluded, nonzero quotient fibre only.
- \(h<0\): **OPEN**, Reverse-CQRF quotient theorem proved.

### Prime-power audit

- squarefree \(q\): covered by the quotient theorem;
- nonsquarefree \(q\): prime-power formula proved for arbitrary \(p^a\Vert q\), with explicit regressions \(q=49,121\);
- \(b=0\): covered in the valuation-tail quotient chamber;
- positive \(b\) with the valuation allocation active: covered by the same local theorem; \(b\) cancels from the next-digit slope;
- deep \(b\ge g\) (high) / \(b\ge k\) (reverse): retained under the inherited outer-suppressed or finite-prefix treatment;
- deeper \(\lambda_p=0\) lift: **OPEN exceptional chamber**;
- \(p\mid t\) derivative-degenerate chamber: **OPEN exceptional chamber**.

### Sign / tail audit

- \(\sigma=+1\): retained;
- \(\sigma=-1\): retained;
- tail zero in high \(h\ge1\): frozen impossible;
- boundary tail zero: impossible because \(q^3<63\) contradicts \(q\ge7\);
- low-tail zero ray: retained under \(q^3<63\cdot10^r\).

### Root audit

- local square at \(p\mid q\): reduced to degree-\(\le2\) one-digit polynomial;
- auxiliary structural local square: not sufficient globally;
- global integer square: still required and not claimed periodic;
- root divisibility: still required after square and not reduced mod \(p\mid q\) unless that prime actually divides \(A\);
- primitive gcd: retained after integral root reconstruction;
- common-\(U\) gate: retained after primitive reconstruction.

No later gate is silently removed.

---

# Part XIV — New Frontier

Full J2 is still open, but the frontier is strictly lower-dimensional than the inherited

\[
(q,h,\alpha,t;g)\text{ CQRF}.
\]

At a nondegenerate prime power \(p^a\Vert q\), the legal fibre now has the canonical local form

\[
\boxed{
\begin{array}{l}
 n\equiv n_*\pmod{p^a},\\[2mm]
 n=n_*+p^az,\\[2mm]
 \rho\equiv\rho_*+\gamma_pz\pmod p,\\[2mm]
 64\Psi_\delta\equiv F_{p,\delta,t}(z)\pmod p,\\[2mm]
 F_{p,\delta,t}(z)\in(\mathbf F_p)^2\cup\{0\}.
\end{array}}
\tag{NEW-FRONTIER}
\]

So the remaining obstruction is best stated as

\[
\boxed{
\textbf{one quotient index digit}
\;+
\textbf{one local quadratic square class}.
}
\]

The next theorem should not search for a new macroscopic coordinate.  It should attack one of the following precise gaps:

1. **cross-prime next-digit synchronization:** prove that the same global order-class index \(n\) cannot satisfy all prime-power quadratic square sets simultaneously once the exact \((\alpha,t)\) fibre restrictions are included;
2. **degenerate-prime closure:** control \(p\mid t\) and \(\lambda_p=0\) without losing the one-digit structure;
3. **global-square splice:** use the factorization/value structure of \(\Psi_\delta\) to introduce a prime depending on the value, not merely the fixed structural coefficient support, and combine it with the Hensel-index class.

For the boundary \(h=0\), the especially clean target is

\[
\boxed{
\bigl(\rho+(A-1)t\bigr)^2
-2A^2(A-1)^2t^2
\text{ is a global square kernel under the quotient class.}
}
\]

For \(h=1\), the \(q=11\) regression shows exactly why one more global synchronization ingredient is necessary.

Therefore:

\[
\boxed{\textbf{J2 Resonance remains OPEN}.}
\]

No false closure certificate is issued.

---

# File Audit

The round requires and generates:

```text
A1_J2_CQLRC8_Report.md
A1_J2_CQLRC8_quotient.py
A1_J2_CQLRC8_root.py
A1_J2_CQLRC8_search.py
A1_J2_CQLRC8_search_certificate.txt
A1_J2_CQLRC8_certificate.txt
A1_J2_CQLRC8_survivors.tsv
```

No `A1_J2_Resonance_Closure_Certificate.md` is generated because J2 is not closed.

The symbolic scripts certify exact identities; the census ledger is explicitly diagnostic; report and certificate use the same \(h=0,1\) counts.

FINAL_REPORT_FILE: A1_J2_CQLRC8_Report.md

QUOTIENT_SYMBOLIC_FILE: A1_J2_CQLRC8_quotient.py

ROOT_SYMBOLIC_FILE: A1_J2_CQLRC8_root.py

COMPUTATION_FILE: A1_J2_CQLRC8_search.py

CERTIFICATE_FILE: A1_J2_CQLRC8_certificate.txt

SURVIVOR_FILE: A1_J2_CQLRC8_survivors.tsv
