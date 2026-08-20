# 105-R39 — Production-Native Root System

## 1. GCD-normalized selector semantics

\[
u_0AW=g_0a,\qquad P_1=g_0\mu s,\qquad (a,\mu s)=1,
\]

with

\[
g_0=(u_0AW,P_1),\qquad g_1^*=\mu g_0.
\]

Also

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3.
\]

## 2. Source-native coefficients

After exponent synchronization,

\[
XYGK=10^{n_2+n_3},\quad
YG=10^{m_3},\quad
XYG=10^{m_2+m_3}=10^{n_2+n_3-k}.
\]

Hence

\[
\boxed{L_{\rm src}=a10^{n_2+n_3}=a10^{m_2+m_3+k}},
\]

\[
\boxed{B_{\rm src}=\mu(W+A10^{m_3})+a10^{m_2+m_3}},
\]

and, since \(u_0AW=g_0a\),

\[
\boxed{C_{\rm src}=\mu g_0a(C_3+10^{n_3}C_2)}.
\]

No ambient \(X,Y,G,K\) remain.

## 3. Exact incidence

\[
\boxed{L_{\rm src}P_1=B_{\rm src}Q_0-C_{\rm src}},
\]

\[
P_1^2+P_2^2+P_3^2=Q_0^2.
\]

Substituting \(P_1=g_0\mu s\) gives

\[
\boxed{
B_{\rm src}Q_0
=
g_0\mu a
\left(
s10^{n_2+n_3}+C_3+10^{n_3}C_2
\right).
}
\]

## 4. Quadratic form

\[
(B_{\rm src}^2-L_{\rm src}^2)Q_0^2
-2B_{\rm src}C_{\rm src}Q_0
+C_{\rm src}^2
+L_{\rm src}^2(P_2^2+P_3^2)=0.
\]

R39 proves \(B_{\rm src}<L_{\rm src}\), hence

\[
\boxed{\mathcal A_N=B_{\rm src}^2-L_{\rm src}^2<0}.
\]

The linear degenerate branch is globally absent.
