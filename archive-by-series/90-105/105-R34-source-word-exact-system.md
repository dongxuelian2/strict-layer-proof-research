# 105-R34 — Source-Word Exact System

## Frozen authoritative coordinates

\[
T=Q_0-P_3>0,\quad H=10^gQ_0-P_2>0,\quad D=10^kP_1-Q_0>0,
\]
\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3,
\]
\[
m_2=m,\quad m_3=n+g,\quad n_2=m+g+k,\quad n_3=n.
\]

For \(q=1\),
\[
b_2=A\Lambda,\quad b_3=W\Lambda,\quad
b_1=\frac{\Lambda u_0AW}{g_1^*},\quad
V_0=\Lambda u_0AW.
\]

R33 gives
\[
b_1 10^{m+n+g}D=b_3T+b_2 10^nH,
\]
\[
J_3:=\frac{b_3T}{10^n}\in\mathbb Z_{>0},\qquad
J_3+b_2H=b_1 10^{m+g}D.
\]

For a source integer \(U\),
\[
X_2=C_2U,\qquad X_3=C_3U,
\]
with
\[
10^{n_2-1}\le X_2<10^{n_2},\qquad
10^{n_3-1}\le X_3<10^{n_3},
\]
and the frozen primitive condition \((U,V_0)=1\).

## Face 3

Because
\[
V_0C_3=(\Lambda u_0AW)C_3=(W\Lambda)(u_0AC_3)=b_3P_3,
\]
we have the exact identity
\[
V_0X_3-b_3UQ_0
=
U(V_0C_3-b_3Q_0)
=
-U b_3T
=
-10^{n_3}UJ_3.
\]

Hence the requested congruence is authoritative:
\[
\boxed{V_0X_3\equiv b_3UQ_0\pmod{10^{n_3}}}.
\]

But it is not new information: after the semantic definition \(X_3=C_3U\), it is identically the already-frozen tail divisibility \(10^{n_3}\mid b_3T\).

## Face 2

Define
\[
A_2:=J_3+Q_0\left(b_2 10^g+b_1 10^{m+g}\right).
\]

Using \(V_0C_2=b_2P_2\), \(H=10^gQ_0-P_2\), CARRY, and \(D+Q_0=10^kP_1\),
\[
\begin{aligned}
A_2-V_0C_2
&=J_3+b_2H+b_1 10^{m+g}Q_0\\
&=b_1 10^{m+g}(D+Q_0)\\
&=b_1 10^{m+g+k}P_1\\
&=b_1 10^{n_2}P_1.
\end{aligned}
\]

Therefore
\[
V_0X_2-UA_2
=
-b_1UP_1\,10^{n_2},
\]
and hence
\[
\boxed{
V_0X_2\equiv
U\left[J_3+Q_0(b_2 10^g+b_1 10^{m+g})\right]
\pmod{10^{n_2}}.
}
\]

Again this is an exact identity once \(X_2=C_2U\) is imposed. It contains no new source-word restriction.

## Dependency theorem

For every frozen q1 MASTER/tail architecture and every integer \(U\),
\[
X_i=C_iU
\quad\Longrightarrow\quad
(F2)\wedge(F3).
\]

Consequently
\[
\boxed{
\mathrm{MASTER+TAIL+SEMANTIC\ SOURCE}
\Rightarrow
\mathrm{F2+F3}
}
\]
with no use of BOX2/BOX3 or \((U,V_0)=1\).

Thus
\[
\boxed{
\{U:\mathrm{BOX+primitive+SrcComp+F2+F3}\}
=
\{U:\mathrm{BOX+primitive+SrcComp}\}
}
\]
on every fixed q1 MASTER/tail architecture.
