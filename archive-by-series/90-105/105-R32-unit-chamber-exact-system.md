# 105-R32 — Unit-Chamber Exact System

## 1. Frozen variables

For a legal post-support architecture,

\[
C_2=\frac{P_2}{u_0W},\qquad C_3=\frac{P_3}{u_0A},
\]

\[
g_0=(u_0AW,P_1),\quad \mu=g_1^*/g_0,
\]

\[
\lambda_z=\frac{10^{n_3}}{(10^{n_3},W(Q_0-P_3))},
\qquad \Lambda=\operatorname{lcm}(\mu,\lambda_z).
\]

The primitive carrier obeys

\[
P_1^2+P_2^2+P_3^2=Q_0^2,\qquad
(P_1,P_2,P_3,Q_0)=1.
\]

Shape/support conditions remain frozen:

\[
(A,C_2)=(W,C_3)=(A,W)=1,
\]

\[
g_0\mid g_1^*\mid P_1,\quad
(\mu,C_2C_3)=1,
\]

and the inherited tail-\(g_1\)/tail-Smith conditions.

## 2. q=1 denominator system

Residual \(q=1\) is exactly

\[
Z_-\le \Lambda\le Z_+,
\]

equivalently

\[
10^{m_2-1}\le A\Lambda\le10^{m_2}-1 \tag{D2}
\]

and

\[
10^{m_3-1}\le W\Lambda\le10^{m_3}-1. \tag{D3}
\]

Thus, once \(\Lambda\) is known,

\[
\boxed{m_2=\operatorname{dig}(A\Lambda),\qquad
m_3=\operatorname{dig}(W\Lambda).}
\]

No denominator prime-cover arithmetic survives in the unit chamber.

## 3. Exact coarse source room

The two source digit conditions are

\[
10^{n_2-1}\le C_2U\le10^{n_2}-1,\tag{S2}
\]

\[
10^{n_3-1}\le C_3U\le10^{n_3}-1.\tag{S3}
\]

Equivalently,

\[
U_{\rm lo}=
\max\!\left(
\left\lceil\frac{10^{n_2-1}}{C_2}\right\rceil,
\left\lceil\frac{10^{n_3-1}}{C_3}\right\rceil
\right),
\]

\[
U_{\rm hi}=
\min\!\left(
\left\lfloor\frac{10^{n_2}-1}{C_2}\right\rfloor,
\left\lfloor\frac{10^{n_3}-1}{C_3}\right\rfloor
\right).
\]

Therefore, **before** native source residue/completed-source restrictions,

\[
\boxed{\exists U\in\mathbb Z_{>0}\text{ satisfying S2,S3}
\iff U_{\rm lo}\le U_{\rm hi}.}
\]

The full \(\mathcal U_0\) additionally requires the frozen residue selector,
\((U,\Lambda u_0AW)=1\), and source-completed predicates.

## 4. Exact exponent collapse

R26 gives

\[
n_3=n,\qquad n_2=n+\delta,\qquad m_2=m,
\]

\[
k=\rho-m,\qquad g=n+\delta-\rho,\qquad m_3=n+g.
\]

Hence

\[
\boxed{n_2=m_2+g+k,\qquad m_3=n_3+g}
\]

and

\[
\boxed{(m_3-m_2)-(n_3-n_2)=2g+k.}
\]

Since \(k\ge1\), this difference is always positive.

## 5. Unit-chamber digit determinization theorem

Fix a primitive packet and selectors \(A,W,u_0,g_1^*\), and fix a source digit pair
\((n_2,n_3)\) for which the source room is nonempty. Compute

\[
\Lambda=\operatorname{lcm}\!\left(
\frac{g_1^*}{(u_0AW,P_1)},
\frac{10^{n_3}}{(10^{n_3},W(Q_0-P_3))}
\right).
\]

Then q=1 forces

\[
m_2=\operatorname{dig}(A\Lambda),\quad
m_3=\operatorname{dig}(W\Lambda),
\]

and therefore forces

\[
\boxed{g=m_3-n_3,\qquad
k=n_2-m_2-g.}
\]

Thus the unit branch has no independent \((m_2,m_3,g,k)\) search once the source
digit pair is fixed. Legality requires \(g\ge0,\ k\ge1\), after which TC1/master
and the frozen completed-source gates are replayed.

```text
UNIT_CHAMBER_DIGIT_DETERMINIZATION_THEOREM=PROVED
```

The same statement holds for prescribed general q after replacing
\(A\Lambda,W\Lambda\) by \(A\Lambda q,W\Lambda q\).
