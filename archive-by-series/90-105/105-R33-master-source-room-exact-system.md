# 105-R33 — MASTER × Source Integer Room Exact System

## 1. Frozen variables

Use the R28/R32 authoritative notation

\[
T=Q_0-P_3>0,\qquad H=10^gQ_0-P_2>0,\qquad D=10^kP_1-Q_0>0,
\]

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3,
\]

and

\[
m_2=m,\quad m_3=n+g,\quad n_2=m+g+k,\quad n_3=n.
\]

The authoritative positive MASTER is

\[
\boxed{g_1^*\bigl(WT+A10^nH\bigr)=AWu_0\,10^{m+n+g}D.}
\tag{M}
\]

For q=1,

\[
\Lambda=\operatorname{lcm}\!\left(
\frac{g_1^*}{(u_0AW,P_1)},
\frac{10^n}{(10^n,W T)}
\right),
\]

and the denominator digit conditions are exact:

\[
10^{m-1}\le A\Lambda\le10^m-1,\qquad
10^{n+g-1}\le W\Lambda\le10^{n+g}-1.
\]

## 2. q1 denominator-block normal form

Define

\[
\boxed{b_2=A\Lambda,\qquad b_3=W\Lambda,\qquad
b_1=\frac{\Lambda u_0AW}{g_1^*}.}
\]

The last quantity is an integer because if
\(g_0=(u_0AW,P_1)\), then \(g_1^*=g_0\mu\), \(\mu\mid\Lambda\), and
\(g_0\mid u_0AW\).

Multiplying (M) by \(\Lambda/g_1^*\) gives the lowest-complexity q1 MASTER:

\[
\boxed{b_1 10^{m+n+g}D=b_3T+b_2 10^nH.}
\tag{DM}
\]

This is not a second TC1 equation; it is exactly MASTER in q1 block coordinates.

## 3. Exact MASTER remainder

Set upper denominator deficits

\[
e_2=10^m-b_2\ge1,\qquad e_3=10^{n+g}-b_3\ge1.
\]

Expanding (DM) yields

\[
\boxed{
10^{m+n+g}(Q_0-b_1D)
=Q_0(e_3+e_2 10^{n+g})+b_3P_3+b_2 10^nP_2.
}
\tag{REM}
\]

Every term on the right is positive. Hence

\[
\boxed{0<b_1D<Q_0.}
\tag{DEFECT}
\]

This is the q1/block-coordinate recovery of the earlier leading-defect fact.

## 4. Tail carry extraction

The frozen definition

\[
\lambda_z=\frac{10^n}{(10^n,WT)},\qquad \lambda_z\mid\Lambda
\]

implies

\[
10^n\mid W\Lambda T=b_3T.
\]

Thus

\[
\boxed{J_3:=\frac{b_3T}{10^n}\in\mathbb Z_{>0}}
\]

and division of (DM) by \(10^n\) gives the exact decimal carry equation

\[
\boxed{J_3+b_2H=b_1 10^{m+g}D.}
\tag{CARRY}
\]

In particular

\[
J_3+b_2H\equiv0\pmod{10^m}.
\]

This is stronger than a raw interval statement, but it controls the MASTER carry rather than the Euclidean remainders of \(10^{n_i-1}\) modulo \(C_i\).

## 5. Put MASTER inside an integer source room

Assume a coarse source integer \(U\ge1\) exists and set

\[
X_2=C_2U,\qquad X_3=C_3U.
\]

Then

\[
10^{n_2-1}\le X_2\le10^{n_2}-1,\qquad
10^{n-1}\le X_3\le10^n-1.
\]

Set source upper deficits

\[
f_2=10^{n_2}-X_2\ge1,\qquad f_3=10^n-X_3\ge1.
\]

Because \(b_3P_3=\Lambda u_0AW C_3\) and
\(b_2P_2=\Lambda u_0AW C_2\), multiplying (REM) by U gives

\[
\boxed{
10^{m+n+g}U(Q_0-b_1D)
=UQ_0(e_3+e_2 10^{n+g})
+V_0\bigl[(10^n-f_3)+10^n(10^{n_2}-f_2)\bigr],
}
\tag{BOX-REM}
\]

where \(V_0=\Lambda u_0AW\).

This is the requested MASTER-inside-source-box identity. It has no cancellation.
