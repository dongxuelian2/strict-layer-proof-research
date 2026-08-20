# Fourth 85 · R5 — Local Cover Autopsy

## Verdict

\[
\boxed{\texttt{FINITE\_LOCAL\_COVER\_EXTRACTED=NO}}
\]

but R5 does **not** claim a theorem that no eventual finite cover can exist.

The reason to stop blind prime hunting is structural.

R5 proves

\[
(A_2,T_4)=(-1,T_4).
\]

Hence a local obstruction exists exactly at primes

\[
p\equiv3\pmod4
\]

with odd

\[
v_p(T_4(10^g,K)).
\]

There are exact live split fibres where no local place obstructs at all.

Examples:

- \(K=100\): \(g=5,9,10,11,14\);
- \(K=1000\): \(g=5,8,9\).

Therefore the conjecture

\[
\forall g\ \exists p:\ H_{K,p}(g)=-1
\]

is false.

A scan over all \(p<20000\), \(p\equiv3\bmod4\), gives:

- \(K=100,\ 4\le g\le200\): 129/197 survive all tested fixed primes;
- \(K=1000,\ 5\le g\le200\): 117/196 survive.

Thus marginal value from adding more unrelated fixed primes is low.

## What survives from local methods

Local/Brauer theory remains the exact classifier

\[
g\mapsto
\begin{cases}
\text{Brauer-obstructed},\\
\text{Gaussian-split}.
\end{cases}
\]

R6 should attack the source embedding only on Gaussian-split fibres.
