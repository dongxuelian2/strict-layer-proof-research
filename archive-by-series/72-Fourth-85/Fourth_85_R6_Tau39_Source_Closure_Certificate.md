# Fourth 85 · R6 — \(\tau=3,9\) Source Closure Certificate

For the q=1 negative source conic

\[
Y_0^2=A_2a^2+B_1a+C_0,
\]

assume \(K=100\) or \(1000\), \(G=10^g\), and \(3\mid\tau\).

Since powers of ten are \(1\bmod3\),

\[
G\equiv K\equiv1\pmod3.
\]

Direct reduction of \(A_2\) gives

\[
A_2(G,K)\equiv2\pmod3.
\]

Also

\[
B_1=-\tau G^2P\equiv0\pmod3,
\]

and

\[
C_0=\frac{\tau^2G^5}{4}Q_K\equiv0\pmod3.
\]

The source primitive condition contains

\[
\gcd(\rho,\tau)=1.
\]

Because

\[
a=\tau G/10+\rho,
\]

we get

\[
a\equiv\rho\not\equiv0\pmod3.
\]

Hence any source solution would imply

\[
Y_0^2
\equiv
2a^2
\equiv2
\pmod3,
\]

impossible.

Therefore, for both \(K=100\) and \(K=1000\),

\[
\boxed{
(d,\tau)=(1,3),(1,9),(3,3)
\Longrightarrow\varnothing.
}
\]

This closes six previously live historical source cases.

```text
TAU_DIVISIBLE_BY_3_SOURCE_FAMILIES_CLOSED = YES
NEW_HISTORICAL_CASES_CLOSED = 6
```
