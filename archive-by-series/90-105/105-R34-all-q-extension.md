# 105-R34 — All-\(q\) Extension

For prescribed residual \(q\), R30/R33 give
\[
z=\Lambda q,\qquad
V(q)=qV_0,
\]
and actual denominator blocks
\[
B_1=q b_1,\qquad B_2=q b_2,\qquad B_3=q b_3,
\]
with deterministic exponents
\[
m_2=\operatorname{dig}(A\Lambda q),\quad
m_3=\operatorname{dig}(W\Lambda q),\quad
g=m_3-n_3,\quad
k=n_2-m_2-g.
\]

Because \(10^{n_3}\mid b_3T\), define
\[
J_3(q)=\frac{B_3T}{10^{n_3}}=qJ_3.
\]

For the semantic source words \(X_i=C_iU\),
\[
V(q)X_3-U B_3Q_0
=
-U B_3T
=
-10^{n_3}U J_3(q),
\]
and if
\[
A_2(q):=J_3(q)+Q_0(B_2 10^g+B_1 10^{m_2+g}),
\]
then, using \(n_2=m_2+g+k\),
\[
V(q)X_2-UA_2(q)
=
-B_1UP_1\,10^{n_2}.
\]

Thus the source-word congruences are identities for every prescribed q.

The important point is that one does not need to cancel q modulo a power of ten.
The q-factor disappears at the level of exact integer identities before reduction modulo \(10^{n_i}\).

Therefore
\[
\boxed{
\text{SOURCE-WORD CONGRUENCE INFORMATION GAIN}=0
\quad\text{for all }q.
}
\]

What remains q-dependent is exactly the already frozen structure:
- deterministic denominator digit jumps;
- MASTER cutoff
\[
q\le Q_{\rm master}=
\left\lfloor\frac{Q_0-1}{\bar b_1D}\right\rfloor;
\]
- primitive source coprimality
\[
(U,V_0q)=1\iff(U,V_0)=1\ \&\ (U,q)=1.
\]

Hence the minimal-prime branch remains
\[
\boxed{
Q_-\le p\le\min(Q_+,Q_{\rm master}),\qquad p\nmid FU.
}
\]
No new prime extinction follows from F2/F3.
