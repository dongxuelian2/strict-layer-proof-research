# 105-R34 — Decimal Residue Collision Proof / Failure Certificate

The requested terminal pattern was
\[
M_r\mid R,\qquad 0<|R|<M_r.
\]

R34 proves that this pattern cannot arise from F2/F3.

Indeed,
\[
R=U S,\qquad
S=10^{n_3}J_3C_2-10^{n_2}b_1P_1C_3,
\]
and with \(r=\min(n_2,n_3)\),
\[
10^r\mid S.
\]

Hence either \(R=0\), or
\[
|R|=U|S|\ge U10^r\ge10^r.
\]

But
\[
M_r=\frac{10^r}{(V_0,10^r)}\le10^r.
\]

Therefore on every nonzero branch
\[
\boxed{|R|\ge10^r\ge M_r,}
\]
so the desired strict size inequality is structurally impossible.

This is stronger than a failed estimate: no refinement of decimal-box upper bounds can make
the same cross remainder satisfy \(0<|R|<M_r\).

## \(R=0\) branch

The zero branch is exactly
\[
10^{n_3}J_3C_2=10^{n_2}b_1P_1C_3.
\]
Since \(10^{n_3}J_3=b_3T\), \(P_1=g_1^*R_1\), and the carrier definitions hold,
this is equivalent to
\[
\boxed{
C_2T=10^{n_2}R_1P_3,
\qquad R_1:=\frac{P_1}{g_1^*}.
}
\]

Equivalently,
\[
g_1^*P_2T=u_0W\,10^{n_2}P_1P_3.
\]

This equality contains no \(U\), \(X_2\), or \(X_3\): the putative exceptional source-word branch collapses to an old packet/carrier equality.

R34 does not prove that this old equality is globally empty. It also does not need to:
the nonzero branch is already incapable of the requested size collision, while the zero branch produces no contradiction at all.
Thus \(R=0\) is not a remaining "source-word exceptional locus"; it is evidence that the entire F2/F3 cross-residue information class is dependent.
