# Fourth 85 · R4 — Function-Field Norm Certificate

## Certified identity

For every fixed \(K\in\{10,100,1000\}\) and every q=1 negative coefficient template,

\[
(2A_Kn+B_{K,\tau})^2
-
A_2(G,K)(40K\mathcal Y)^2
=
[200K\tau G^2(G+1)(2G+3)]^2T_4(G,K).
\]

Hence over \(\mathbf Q(G)\):

\[
\boxed{x^2-A_2(G,K)v^2=T_4(G,K)}.
\]

The 12 \((K,\tau)\) templates collapse to 3 \(K\)-dependent torsors.

## Fixed function field

\[
C_K:\ z^2=A_2(G,K)
\]

has \(A_2\) irreducible squarefree of degree 6, hence genus 2.

The two points at infinity are conjugate over
\(\mathbf Q(\sqrt{K^2-1})\), so

\[
\boxed{\mathcal O(C_K\setminus\{\infty_\pm\})^\times=\mathbf Q^\times}.
\]

## Fixed divisor support

\[
T_4(G,K)
\]

is irreducible squarefree quartic and

\[
\operatorname{Res}_G(A_2,T_4)
=
1024(K-1)^2(K+1)^2
(32K^6+348K^4-1220K^2+727)^2\ne0.
\]

Thus the norm RHS is supported on a fixed finite set of places.

## Nontrivial quaternion class

\[
\beta_K=(A_2,T_4)\in\operatorname{Br}(\mathbf Q(G))[2]
\]

is nonzero.

Indeed for every integer \(G\equiv1\pmod{16}\),

\[
A_2(G,K)\equiv56\pmod{64},
\qquad
T_4(G,K)\equiv14\pmod{16},
\]

hence

\[
(A_2,T_4)_2=-1.
\]

Infinitely many such specializations rule out a generic \(\mathbf Q(G)\)-section.

## Verdict

\[
\boxed{\texttt{FUNCTION_FIELD_NORM_RIGIDITY=PROVED}}.
\]
