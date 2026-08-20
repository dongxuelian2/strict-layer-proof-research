# 105-R33 — Quotient / Remainder Analysis

## MASTER modulo C2

Using \(P_2=u_0WC_2\), hence \(H\equiv10^gQ_0\pmod{C_2}\), the exact MASTER gives

\[
\boxed{
g_1^*\bigl[W(Q_0-u_0AC_3)+A10^{n+g}Q_0\bigr]
\equiv AWu_0 10^{m+n+g}D\pmod{C_2}.
}
\tag{MC2}
\]

Equivalently, from R28 (3.1),

\[
g_1^*Q_0(W+A10^{n+g})
\equiv AWu_0\bigl(g_1^*C_3+10^{m+n+g}D\bigr)\pmod{C_2}.
\]

## MASTER modulo C3

Using \(P_3=u_0AC_3\),

\[
\boxed{
g_1^*\bigl[WQ_0+A10^n(10^gQ_0-u_0WC_2)\bigr]
\equiv AWu_0 10^{m+n+g}D\pmod{C_3}.
}
\tag{MC3}
\]

Equivalently,

\[
g_1^*Q_0(W+A10^{n+g})
\equiv AWu_0\bigl(g_1^*10^nC_2+10^{m+n+g}D\bigr)\pmod{C_3}.
\]

## What these congruences do and do not determine

The source-room remainders are

\[
10^{n_i-1}\bmod C_i.
\]

Neither MC2 nor MC3 contains an endpoint power \(10^{n_i-1}\) as an isolated invertible term, and the frozen shape/support conditions do not make every remaining coefficient invertible modulo \(C_i\). Consequently raw reduction modulo \(C_2\) or \(C_3\) does not, by itself, determine \(r_2\) or \(r_3\).

The genuinely stronger exact quotient extraction is instead the tail carry

\[
10^n\mid b_3T,
\qquad
J_3=\frac{b_3T}{10^n},
\qquad
J_3+b_2H=b_1 10^{m+g}D.
\]

This is the new useful remainder object of R33. It has not been converted into a universal source-room contradiction.
