# Fourth 85 · R6 — Explicit Extension Gaussianization Certificate

Let \(A=A_2(G,K)\), \(T=T_4(G,K)\), and use the R5 identity

\[
A+S^2=TQ.
\]

Over \(E=\mathbf Q(G,\sqrt Q)\), define

\[
[U:W:Z_G]
=
[SX+\sqrt Q\,TZ:\,-AV:\,\sqrt Q\,X+SZ].
\]

Then the exact identity

\[
U^2+W^2-TZ_G^2
=
-A(X^2-AV^2-TZ^2)
\]

holds.

The matrix determinant is

\[
A^2,
\]

and an inverse up to scalar is

\[
[X:V:Z]
=
[SU-\sqrt Q\,TZ_G:\,W:\,SZ_G-\sqrt Q\,U].
\]

On affine charts:

\[
u=\frac{Sx+\sqrt Q\,T}{S+\sqrt Q\,x},
\qquad
w=\frac{-Av}{S+\sqrt Q\,x},
\]

\[
x=\frac{Su-\sqrt Q\,T}{S-\sqrt Q\,u},
\qquad
v=\frac{w}{S-\sqrt Q\,u}.
\]

Furthermore

\[
\operatorname{disc}_G(Q)=-20(8K^2-3)\ne0,
\]

so this explicit formula is genuinely quadratic over \(\mathbf Q(G)\).

Machine verification:
`Fourth_85_R6_computation/conic_maps/extension_gaussianization_certificate.py`.

Verdict:

```text
EXPLICIT_EXTENSION_GAUSSIANIZATION = PASS
BASE_FIELD_SOURCE_USEFUL_AFFINE_MAP = NOT_OBTAINED
```
