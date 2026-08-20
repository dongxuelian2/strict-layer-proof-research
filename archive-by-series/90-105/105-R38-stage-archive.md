
# 105-R38 Stage Archive

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — (A1)-only  
**Round:** 105-R38  
**Arithmetic:** exact integers only

## Part I — FILE / HASH AUDIT

R37's authoritative SHA-256 ledger was read. Historical File Library objects
are references rather than mounted raw bytes in this runtime, so R37 inputs
are recorded as `LEDGER-CROSSCHECK`. R38 outputs are bytewise SHA-256 hashed.

## Part II — NORMALIZED ROOT GATE

The authoritative R37 coefficients are
\[
L_N=aXYGK,\quad B_N=\mu(W+AYG)+aXYG,\quad
C_N=\mu(WP_3+AYP_2).
\]
The exact linear root relation is
\[
L_NP_1=B_NQ_0-C_N
\]
with \(P_1^2+P_2^2+P_3^2=Q_0^2\).


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


## Part III — FACTORIZATION / PARITY

Since \((\beta,\lambda)=1\),
\[
\gcd(\beta-\lambda,\beta+\lambda)\mid2.
\]
If \(\beta,\lambda\) have opposite parity the gcd is \(1\). If both are
odd the gcd is \(2\); both \(m_\pm\) are even, exactly one has \(v_2=1\),
and the other has \(v_2\ge2\).

Also
\[
B_N-L_N=\mu(W+AYG)-aXYG(K-1),
\]
\[
B_N+L_N=\mu(W+AYG)+aXYG(K+1).
\]
These are sums, so no universal \(K\pm1\) factor can be extracted.

## Part IV — INFORMATION-GAIN AUDIT

```text
FACTOR_ALLOCATION_INFORMATION_GAIN=0
PRIME_ALLOCATION_INTO_Q0_PLUS_MINUS_P1=FALSE
ROUTE_TERMINATED
```

The proposed stronger allocation is not merely unproved; the exact normalized
root below falsifies it:
\[
29\nmid37=Q_0+P_1,\qquad71\nmid25=Q_0-P_1.
\]

## Part V — DIRECT NRDG ARITHMETIC


On an actual NTC1+sphere incidence,
\[
C=BQ-LP,\qquad S_0=Q^2-P^2.
\]
Hence
\[
\delta_{\rm norm}
=(BQ-LP)^2-(B^2-L^2)(Q^2-P^2)
=\boxed{(BP-LQ)^2}.
\]
Choose the matching sign by \(\varepsilon R=BP-LQ\). Then
\[
\boxed{BC+\varepsilon LR=\mathcal A_NQ},\qquad
\boxed{CL+\varepsilon BR=\mathcal A_NP}. \tag{RI}
\]
Thus \(E_\varepsilon=\mathcal A_NP_1\). Under production normalization
\(P_1=g_0\mu s\),
\[
\boxed{E_\varepsilon=\mu g_0\mathcal A_Ns}.
\]
Therefore NRDG is exactly \(\mu g_0\mid P_1\), its quotient is exactly
\(s\), and COP is exactly the already-imposed \((a,\mu s)=1\).
For every prime \(p\),
\[
v_p(E_\varepsilon)=v_p(\mathcal A_N)+v_p(g_0)+v_p(\mu)+v_p(s).
\]
So no universal \(p\)-adic deficit, size gap, or extra factor allocation
can be extracted from NRDG alone on the production-normalized exact root locus.


## Part VI — ZERO / DEGENERATE BRANCHES

### \(\mathcal A_N=0\)
Because \(B_N,L_N>0\), this is exactly \(B_N=L_N\), i.e.
\[
\mu(W+AYG)=aXYG(K-1).
\]
NF11 becomes
\[
-2B_NC_NQ_0+C_N^2+B_N^2S_0=0.
\]
NRDG division by \(\mathcal A_N\) is invalid and cannot delete this branch.
An exact primitive selector-normalized NTC1+sphere row exists:
\[
(u_0,A,W,g_0,a,\mu,s;X,Y,G,K;C_2,C_3)
=(3,1,8,8,3,25,10;1,10,10,10;16,45),
\]
\[
(P_1,P_2,P_3,Q_0)=(2000,384,135,2041),\quad
B_N=L_N=3000,\ C_N=123000.
\]
It is not a full-support witness: \(\gcd(\mu,C_2C_3)=5\).

### \(R=0\)
For a nondegenerate exact root:
\[
R=0\iff B_NP_1=L_NQ_0.
\]
Because \(Q_0>P_1>0\), this forces \(B_N>L_N\), hence \(\mathcal A_N>0\).
The two root signs merge and NRDG again reduces to \(\mu g_0\mid P_1\).

### \(C_N=\pm R\)
Since \(C_N^2-R^2=\mathcal A_NS_0\) and \(S_0>0\),
\(C_N=R\) forces \(\mathcal A_N=0\).  \(C_N=-R\) is impossible in the
positive branch.

## Part VII — ACTIVE FALSIFICATION

The first exact normalized selector-consistent root found is
\[
(u_0,A,W,g_0,a,\mu,s)=(1,3,2,6,1,1,1),
\]
\[
(X,Y,G,K,C_2,C_3)=(1,10,1,10,11,7),
\]
\[
(P_1,P_2,P_3,Q_0)=(6,22,21,31).
\]
It has
\[
(L_N,B_N,C_N)=(100,42,702),\quad \mathcal A_N=-8236,
\]
\[
\delta_{\rm norm}=8\,111\,104=2848^2.
\]
The matching sign is \(\varepsilon=-1\), and
\[
E_-=-49\,416=\mathcal A_NP_1
=(\mu g_0\mathcal A_N)\cdot1.
\]
Hence NRDG and COP pass exactly.

For this root,
\[
d=2,\quad(\beta,\lambda)=(21,50),\quad(m_-,m_+)=(-29,71),
\]
\[
X_{\rm alloc}=74=2(31+6),\quad
Y_{\rm alloc}=50=2(31-6).
\]

```text
NORMALIZED_ROOT_DIVISIBILITY_EXTINCTION=FALSE
GENUINE_NORMALIZED_SELECTOR_CONSISTENT_ROOT=YES
```

## Part VIII — DOWNSTREAM REPLAY

\(C_2=11\) forces \(n_2=2\); \(G=1\) gives \(g=0\); \(K=10\) gives
\(k=1\). The frozen exponent relation is
\[
m_2=n_2-g-k=1,\qquad X=10^{m_2}=10.
\]
But the root requires \(X=1\). Therefore its first downstream failure is
\[
\boxed{\texttt{SOURCE_EXPONENT_SYNCHRONIZATION}}.
\]
It does not reach the corrected simultaneous locus or a terminal pair.

## Part IX — FULL RECONSTRUCTION

Not triggered: no terminal pair is produced.

## Part X — TERMINAL VERDICT

```text
FACTOR_ALLOCATION_INFORMATION_GAIN=0
PRIME_ALLOCATION_INTO_RADIAL_FACTORS=FALSIFIED
NRDG_INFORMATION_GAIN_ON_PRODUCTION_EXACT_ROOT=0
NORMALIZED_ROOT_DIVISIBILITY_EXTINCTION=FALSE
GENUINE_NORMALIZED_SELECTOR_CONSISTENT_ROOT=YES
SOURCE_COMPLETE_SELECTOR_CONSISTENT_ROOT=NOT_FOUND
GCD_NORMALIZED_SIMULTANEOUS_LOCUS_EXTINCTION=NOT_PROVED
MASTER_REFINED_TERMINAL_POSITIVE=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
R38_NRDG_SATURATION_CERTIFICATE=YES
```

### Unique R39 object

R39 is not authorized to revisit factor allocation, prime allocation, raw
discriminants, or NRDG valuations. The surviving independent object is
\[
\boxed{\textbf{production-normalized NTC1+sphere root}
\cap\textbf{frozen source-exponent image}}
\]
with
\[
X=10^{n_2-g-k},\quad Y=10^{n_3},\quad
P_2=u_0WC_2,\quad P_3=u_0AC_3,
\]
followed immediately by normalized MASTER / corrected-simultaneous replay.
