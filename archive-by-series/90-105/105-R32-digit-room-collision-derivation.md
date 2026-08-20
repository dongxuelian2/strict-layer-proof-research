# 105-R32 — Digit / Room Collision Derivation

## 1. Continuous denominator overlap

Let

\[
J_2=\left[\frac{10^{m_2-1}}A,\frac{10^{m_2}}A\right),\qquad
J_3=\left[\frac{10^{m_3-1}}W,\frac{10^{m_3}}W\right).
\]

Then \(J_2\cap J_3\ne\varnothing\) implies, and in the continuous decade model is
equivalent to,

\[
10^{m_3-m_2-1}<\frac WA<10^{m_3-m_2+1}. \tag{J}
\]

The actual q=1 problem uses the exact \(-1\) upper endpoints; this only tightens
the displayed open window.

## 2. Continuous source overlap

Similarly,

\[
I_2=\left[\frac{10^{n_2-1}}{C_2},\frac{10^{n_2}}{C_2}\right),\qquad
I_3=\left[\frac{10^{n_3-1}}{C_3},\frac{10^{n_3}}{C_3}\right)
\]

gives

\[
10^{n_2-n_3-1}<\frac{C_2}{C_3}<10^{n_2-n_3+1}. \tag{I}
\]

## 3. Eliminate A/W and C2/C3

Because

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3,
\]

\[
\frac{P_2}{P_3}=\frac WA\frac{C_2}{C_3}.
\]

Multiplying (J) and (I),

\[
10^{(m_3-m_2)+(n_2-n_3)-2}
<
\frac{P_2}{P_3}
<
10^{(m_3-m_2)+(n_2-n_3)+2}.
\]

But

\[
(m_3-m_2)+(n_2-n_3)=2g+k.
\]

Therefore simultaneous denominator/source decade overlap forces exactly the
packet-only factor-100 window

\[
\boxed{
10^{2g+k-2}<\frac{P_2}{P_3}<10^{2g+k+2}
}
\]

or

\[
\boxed{
10^{-2}<\mathfrak R<10^2,\qquad
\mathfrak R:=\frac{P_2}{10^{2g+k}P_3}.
}
\]

This is the lowest-complexity packet-only ratio produced by the four digit
inequalities.

## 4. Exact mantissa identity

For an actual common source integer U and q=1 define

\[
a_2=UC_2,\quad a_3=UC_3,\qquad
b_2=A\Lambda,\quad b_3=W\Lambda.
\]

Then exactly

\[
\frac{P_2}{P_3}=\frac{b_3}{b_2}\frac{a_2}{a_3}.
\]

Writing

\[
\alpha_i=\frac{a_i}{10^{n_i-1}},\qquad
\beta_i=\frac{b_i}{10^{m_i-1}},
\]

one gets the exact identity

\[
\boxed{
\frac{P_2}{10^{2g+k}P_3}
=
\frac{\beta_3}{\beta_2}\frac{\alpha_2}{\alpha_3}.
}
\]

Each mantissa is in its exact integer digit block, so the \(-1\) endpoints are
retained. But there is no algebraic reason for the product of these two
mantissa ratios to leave \((10^{-2},10^2)\).

## 5. Digit-only mutual-exclusion conjecture is not a formal consequence

The exact structural countermodel

\[
(P_1,P_2,P_3,Q_0)=(50,10,1,51)
\]

with

\[
A=W=u_0=g_1^*=1,\quad
(n_2,n_3,m_2,m_3,g,k)=(2,1,1,1,0,1)
\]

has

\[
(C_2,C_3)=(10,1),\quad \Lambda=1,\quad U=1,
\]

and passes:

- primitive sphere;
- both q=1 denominator digit blocks;
- both source digit blocks;
- shape gcd;
- \(\mu\)-Smith;
- tail-\(g_1\) and tail-Smith;
- \(T,H,D>0\).

Its source integer room is in fact \(1\le U\le9\).

But the exact TC1 equation has

\[
\text{LHS}=-5,\qquad \text{RHS}=4439,
\qquad \text{LHS}-\text{RHS}=-4444.
\]

So it dies **exactly at master/TC1**.

Consequently

```text
DENOMINATOR_INTERSECTION_IMPLIES_SOURCE_DISJOINT_BY_DIGITS_ALONE=FALSE
ROOM_KILL_REQUIRES_MASTER_OR_STRONGER_FROZEN_DATA=PROVED
```

The countermodel does **not** falsify global q=1 extinction because it is not a
TC1/master architecture.
