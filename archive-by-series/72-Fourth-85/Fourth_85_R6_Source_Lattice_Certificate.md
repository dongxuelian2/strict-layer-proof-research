# Fourth 85 · R6 — Source Lattice Certificate

The exact source completion square simplifies to

\[
x=\frac{2A_2a+B_1}{D},
\qquad
v=\frac{2Y_0}{D},
\qquad
D=\tau G^2(G+1)(2G+3).
\]

Using \(Y_0=2Ky\), define

\[
C=\frac{2A_2a+B_1}{4K},
\qquad
Y=y,
\qquad
Z=\frac{D}{4K}.
\]

Then

\[
C^2-A_2Y^2=T_4Z^2.
\]

Writing

\[
a=a_0+2Kn,
\qquad
a_0=\tau G/10+r_{K,\tau},
\]

gives

\[
C=c+A_2n,
\qquad
c=\frac{2A_2a_0+B_1}{4K}.
\]

Therefore the ambient source lattice is

\[
(c,0)+
\begin{pmatrix}
A_2&0\\
0&1
\end{pmatrix}
\mathbf Z^2,
\]

and

\[
\boxed{\operatorname{SNF}=\operatorname{diag}(1,A_2)}.
\]

However

\[
c^2-T_4Z^2
=
A_2\frac{A_2a_0^2+B_1a_0+C_0}{4K^2},
\]

so the induced congruence modulo \(A_2\) is automatically saturated.

```text
SOURCE_LATTICE_EXTRACTED = YES
SOURCE_LATTICE_SNF = (1,A2)
NEW_CODIMENSION_FROM_SNF = NO
```
