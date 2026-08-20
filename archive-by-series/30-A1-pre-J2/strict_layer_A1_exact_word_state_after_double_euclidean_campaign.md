# A1 Exact-Word State After Double-Euclidean Campaign

## Current status

\[
\boxed{DD=\varnothing,\qquad A_1\text{ OPEN}.}
\]

## Frozen exact system

\[
D=P_1 10^k-Q_0>0,
\qquad
H=b_2Q_0-b_1 10^{m_2}D\ne0,
\]

\[
Q_{12}=b_1 10^{m_2}+b_2,
\]

\[
b_1P_1 10^{m_2+k}=Q_0Q_{12}-H,
\]

\[
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbb Z_{>0},
\]

\[
b_2P_2=10^gH+K_3.
\]

## Double Euclidean theorem

\[
c_{\rm pref}=\lceil H/Q_0\rceil,
\]

\[
q_{\rm pref}=Q_{12}-c_{\rm pref},
\qquad
r_{\rm pref}=c_{\rm pref}Q_0-H,
\]

\[
q_2-q_3=H,
\qquad
K_3\equiv b_2P_2\pmod{10^g}.
\]

## New Smith divisor

For

\[
b_1=s\alpha u,
\quad
b_2=s\alpha\beta t,
\quad
b_3=s\beta v,
\]

let

\[
\delta_\beta=\gcd(\beta,10^{m_3}),
\qquad
\beta^\sharp=\beta/\delta_\beta.
\]

Then

\[
\boxed{M_H=s\alpha\beta^\sharp\mid H}.
\]

Define

\[
q_H=H/M_H.
\]

The reduced equations are

\[
\boxed{q_H=\delta_\beta tQ_0-uD^\sharp},
\]

\[
\boxed{
\frac{10^{m_3}}{\delta_\beta}q_H
=tP_2 10^{n_3}-vA_3.
}
\]

## Borrow theorem

\[
\boxed{g\ge1,\ \text{minus}\Longrightarrow c\le b_2}.
\]

Hence no cross-block borrow for \(g\ge1\). Cross-block borrow can occur only for \(g=0\), and then by at most one block.

## Resonance

\[
R=b_2 10^{n_3}-b_3.
\]

If \(R=0\):

\[
\alpha=t=1,
\quad
m_2=g,
\quad
b_3=b_2 10^{n_3},
\]

and with

\[
S_R=P_2+P_3-Q_0\ne0,
\]

\[
\boxed{
\frac{10^g}{\gcd(10^g,\delta_\beta)}\mid S_R,
}
\]

with a nontrivial divisor \(>1\).

## Transition state

For \(g\ge1\):

\[
d\le-1\Rightarrow\text{plus},
\qquad
d=0,1\text{ dual-sign},
\qquad
d\ge2\Rightarrow\text{minus}.
\]

New constraints:

\[
d=0,\text{ plus},R>0\Rightarrow m_3\ge2k,
\]

\[
d=0,\text{ minus},R<0\Rightarrow m_3\ge2g+k-1,
\]

\[
d=1,\text{ plus}\Rightarrow m_3\ge2k.
\]

## Killed conjectures

- uniform \(|q_H|\le C\): false;
- uniform \(M_H\gg Q_0\): false;
- generic \(|R|\) growing: false;
- pure exact-word + Smith suffices for closure: false.

The fixed \((b_1,b_2,b_3)=(1,6,8)\) infinite synchronized family has \(M_H=1\), \(q_H\to\infty\), and dies only at common-\(U\).

## Exact frontier

Prove the Smith-reduced common-\(U\) exclusion:

\[
\boxed{
\operatorname{next}_V(L_{23})\ge R_{23}
}
\]

for every DES+Smith synchronized primitive A1 state.

This would imply

\[
\boxed{A_1=\varnothing}.
\]
