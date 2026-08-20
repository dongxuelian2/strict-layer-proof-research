# 105-R33 — Prime-Branch Continuation

R33 does not claim that the prime branch is the unique frontier, because q=1 was not globally killed. It nevertheless pushes the same MASTER arithmetic into prescribed q.

For any prescribed q,

\[
m_2=\operatorname{dig}(A\Lambda q),\quad
m_3=\operatorname{dig}(W\Lambda q),\quad
g=m_3-n_3,\quad k=n_2-m_2-g.
\]

Define base coefficients

\[
\bar b_1=\frac{\Lambda u_0AW}{g_1^*},\qquad
\bar b_2=A\Lambda,\qquad \bar b_3=W\Lambda.
\]

For the actual q-blocks

\[
B_i=q\bar b_i.
\]

Multiplying MASTER by \(\Lambda q/g_1^*\), and using the actual denominator digit upper bounds \(B_2<10^m\), \(B_3<10^{n+g}\), gives

\[
\boxed{q\bar b_1D<Q_0.}
\]

Hence every admissible q satisfies the new exact MASTER cutoff

\[
\boxed{
q\le Q_{\rm master}:=
\left\lfloor\frac{Q_0-1}{\bar b_1D}\right\rfloor.
}
\tag{MASTER-Q-CUTOFF}
\]

Therefore the q-window can be replaced by

\[
Q_-\le q\le\min(Q_+,Q_{\rm master}),\qquad (q,FU)=1.
\]

For a minimal prime branch

\[
\boxed{
Q_-\le p\le\min(Q_+,Q_{\rm master}),\qquad p\nmid FU.
}
\]

This is a genuine R33 continuation: MASTER itself can delete an architecture before any prime-cover computation whenever \(Q_{\rm master}<Q_-\).

For the historical R29 full support-stack point

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*,\Lambda,D)=(1,20,1,80,4,1423),
\]

we have \(\bar b_1=1\) and

\[
Q_{\rm master}=\left\lfloor\frac{4976}{1423}\right\rfloor=3.
\]

Its frozen lower q-edge is \(Q_-=13\), so MASTER-Q-CUTOFF already places it below the admissible chamber. No global prime extinction follows.

```text
MASTER_Q_CUTOFF_THEOREM=PROVED
MINIMAL_PRIME_WINDOW_SHARPENED_BY_MASTER=YES
MINIMAL_PRIME_DENOMINATOR_EXTINCTION=NOT_PROVED
GENUINE_PRIME_Q_SURVIVOR_FOUND=NO
```
