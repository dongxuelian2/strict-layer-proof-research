# 105-R38 — Factor Allocation Derivation


Let \(B=B_N,\ L=L_N,\ C=C_N,\ \mathcal A_N=B^2-L^2\), and
\(S_0=P_2^2+P_3^2\). For \(\mathcal A_N\ne0\), choose
\(R\ge0\) with \(R^2=C^2-\mathcal A_NS_0\) and a root sign
\(\varepsilon\in\{\pm1\}\):
\[
Q=\frac{BC+\varepsilon LR}{\mathcal A_N},\qquad
P=\frac{CL+\varepsilon BR}{\mathcal A_N}.
\]
Then
\[
\boxed{C+\varepsilon R=(B-L)(Q+P)},\qquad
\boxed{C-\varepsilon R=(B+L)(Q-P)}. \tag{FA}
\]
Their product is exactly
\[
(C+\varepsilon R)(C-\varepsilon R)
=\mathcal A_N(Q^2-P^2)=\mathcal A_NS_0.
\]

Write \(d=(B,L)\), \(B=d\beta,L=d\lambda\), \((\beta,\lambda)=1\),
\(m_-=\beta-\lambda,m_+=\beta+\lambda\). Then
\[
\mathcal A_N=d^2m_-m_+,\qquad (m_-,m_+)\mid2.
\]
For
\[
X_{\rm alloc}=\frac{C+\varepsilon R}{m_-},\qquad
Y_{\rm alloc}=\frac{C-\varepsilon R}{m_+},
\]
one has
\[
\boxed{X_{\rm alloc}=d(Q+P),\qquad Y_{\rm alloc}=d(Q-P)},
\]
so \(X_{\rm alloc}Y_{\rm alloc}=d^2S_0\). These are sphere radial
factors in disguise.

The exact integer-root criterion is:
\[
B-L\mid C+\varepsilon R,\qquad B+L\mid C-\varepsilon R,
\]
and, for the resulting quotients \(U,V\), \(U\equiv V\pmod2\).
Then \(Q=(U+V)/2,\ P=(U-V)/2\).
Selector divisibility is exactly \(2\mu g_0\mid U-V\), followed by
\(\gcd(a,(U-V)/(2g_0))=1\).
