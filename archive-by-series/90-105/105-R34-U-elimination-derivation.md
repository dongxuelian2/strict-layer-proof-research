# 105-R34 — \(U\)-Elimination Derivation

Set
\[
A_3:=b_3Q_0,\qquad
A_2:=J_3+Q_0(b_2 10^g+b_1 10^{m+g}),
\]
and
\[
r:=\min(n_2,n_3).
\]

The two exact identities from the source-word system are
\[
V_0X_2-UA_2=-b_1UP_1\,10^{n_2},
\]
\[
V_0X_3-UA_3=-UJ_3\,10^{n_3}.
\]

Cross multiplication gives
\[
V_0(A_3X_2-A_2X_3)
=
U\left(A_2J_3\,10^{n_3}
-A_3b_1P_1\,10^{n_2}\right),
\]
so \(10^r\mid V_0R\), with
\[
R:=A_3X_2-A_2X_3.
\]

The stronger semantic simplification is immediate because \(X_i=C_iU\):
\[
R=U S,\qquad S:=A_3C_2-A_2C_3.
\]

Using
\[
A_3=V_0C_3+10^{n_3}J_3,\qquad
A_2=V_0C_2+10^{n_2}b_1P_1,
\]
the \(V_0C_2C_3\) terms cancel exactly:
\[
\boxed{
S=
10^{n_3}J_3C_2
-
10^{n_2}b_1P_1C_3.
}
\]

Therefore
\[
\boxed{10^r\mid S}
\]
before any division by \((V_0,10^r)\).

This is the key R34 dependency-collapse theorem.

If
\[
d_V=(V_0,10^r),\qquad M_r=\frac{10^r}{d_V},
\]
then the proposed
\[
M_r\mid R
\]
is true but strictly weaker than the already automatic
\[
10^r\mid S,\qquad 10^r\mid R.
\]

There is no useful \(U\)-elimination residue left: the cross remainder itself carries the full common decimal modulus.
