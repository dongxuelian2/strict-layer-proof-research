# 105-R37 — GCD-Normalized MASTER / Sphere System

Let
\[
X=10^m,\quad Y=10^n,\quad G=10^g,\quad K=10^k,
\]
\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3,
\]
and impose from birth
\[
u_0AW=g_0a,\qquad P_1=g_0\mu s,\qquad(a,\mu s)=1.
\]

## 1. Normalized MASTER
With \(\Lambda=\mu\ell\), \(\ell=\tau\), the base coefficient is
\[
\boxed{\bar b_1=\ell a.}
\]
The exact MASTER core is
\[
\boxed{a10^{m+n+g}D=\mu(WT+AYH)},
\]
where
\[
D=KP_1-Q_0=Kg_0\mu s-Q_0,
\]
\[
H=GQ_0-P_2,\qquad T=Q_0-P_3.
\]
The corrected MASTER cutoff is therefore
\[
Q_-\ell aD<Q_0.
\]

## 2. Normalized TC1 / F11 coefficients
The R31 coefficients factor as \(L=g_0L_N\), \(B=g_0B_N\), \(C=g_0C_N\), with
\[
\boxed{L_N=aXYGK,}
\]
\[
\boxed{B_N=\mu(W+AYG)+aXYG,}
\]
\[
\boxed{C_N=\mu(WP_3+AYP_2).}
\]
Equivalently, using the source carriers,
\[
C_N=\mu u_0AW(C_3+YC_2).
\]
The linear TC1 equation becomes
\[
\boxed{L_NP_1=B_NQ_0-C_N.}\tag{NTC1}
\]
Together with
\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]
eliminating \(P_1\) gives
\[
\boxed{(B_N^2-L_N^2)Q_0^2-2B_NC_NQ_0+C_N^2+L_N^2(P_2^2+P_3^2)=0.}\tag{NF11}
\]
No fake \(g_0\) remains in the quadratic coefficients.

## 3. Exact normalized discriminant
Set \(S_0=P_2^2+P_3^2\). Then
\[
\boxed{\Delta_{norm}=4L_N^2\delta_{norm}},
\]
where
\[
\boxed{\delta_{norm}=C_N^2+(L_N^2-B_N^2)S_0.}
\]
Hence, outside the linear exceptional case, a necessary square condition is \(\delta_{norm}=R^2\).

The exact roots are
\[
Q_0=\frac{B_NC_N\pm L_NR}{B_N^2-L_N^2},
\]
and, more importantly for selector consistency,
\[
\boxed{P_1=\frac{C_NL_N\pm B_NR}{B_N^2-L_N^2}.}\tag{P1-root}
\]

## 4. Selector-consistency root-numerator gate
Let
\[
\mathcal A_N=B_N^2-L_N^2,\qquad E_\pm=C_NL_N\pm B_NR.
\]
After integrality of the F11 root, the exact selector condition \(g_1^*=\mu g_0\mid P_1\) is equivalent to
\[
\boxed{\mu g_0\mathcal A_N\mid E_\pm.}\tag{NRDG}
\]
Then one must also have
\[
\boxed{\gcd\!\left(a,\frac{P_1}{g_0}\right)=1.}
\]
This `Normalized Root Divisibility Gate` is the exact global object left after R37. It is strictly sharper than asking only whether the discriminant is square.

The conjugate numerator product satisfies
\[
E_+E_-=(B_N^2-L_N^2)(B_N^2S_0-C_N^2),
\]
which is recorded for R38; R37 did not obtain a uniform prime-allocation contradiction from it.

## 5. Discriminant verdict
Square discriminant alone is not promoted to a selector theorem. R28 already identifies the square-discriminant construction as tautological on actual TC1+sphere incidence. R37's machine data show the same separation: square discriminants survive in every active cell, while selector-consistent integral roots do not.
