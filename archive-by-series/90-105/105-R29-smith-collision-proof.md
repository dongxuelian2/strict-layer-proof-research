# 105-R29 — μ-Smith Collision Attempt: Exact Falsification Certificate

## 1. Proposed theorem

R29 attempted to prove

\[
\text{TC1 + legal shape + positive radial}
\Longrightarrow
(\mu,C_2C_3)>1.
\tag{S}
\]

This theorem is false.

## 2. Genuine counterexample

Use the frozen R20/R21 full-support-stack witness

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*;n,m,k,g)=(1,20,1,80;4,1,1,0).
\]

It has

\[
C_2=71,\qquad C_3=4727,
\]

\[
g_0=20,\qquad \mu=4,
\]

and

\[
\boxed{\gcd(\mu,C_2C_3)=1.}
\]

The primitive sphere equation is exact:

\[
640^2+1420^2+4727^2=4977^2.
\]

Shape gcds are

\[
(1,71)=(20,4727)=(1,20)=1.
\]

Positive radial has the unique integer

\[
U=1:
\quad 10\le71<100,
\qquad 1000\le4727<10000.
\]

The R28 TC1 is exact:

\[
80[20(4977-4727)+10^4(4977-1420)]
=20\cdot10^5(10\cdot640-4977).
\]

Both sides equal

\[
2,846,000,000.
\]

The frozen R20/R21 tail support also passes:

\[
\lambda_z=2,\qquad \tau=1,\qquad \Lambda=4,
\]

\[
R_1=P_1/g_1^*=8,
\qquad
(\tau,R_1)=(\tau,C_2C_3)=1.
\]

Thus this is not a raw/relaxed counterexample. It reaches the full post-master support-stack locus.

## 3. Why the observed gcd 40 is not structural

R28's four globally completed positive-radial conic points were:

| Architecture | C2 | C3 | μ | gcd(μ,C2) | gcd(μ,C3) | total gcd | shape |
|---|---:|---:|---:|---:|---:|---:|---|
| ARCH_07 | 165 | 8 | 80 | 5 | 8 | 40 | pass |
| ARCH_08 | 165 | 8 | 80 | 5 | 8 | 40 | fail (`(A,W)=7`) |
| ARCH_24 | 520 | 833 | 40 | 40 | 1 | 40 | pass |
| ARCH_30 | 365 | 8 | 40 | 5 | 8 | 40 | pass |

The prime allocation is already different inside these samples: ARCH_07/30 place `2^3` in `C3` and `5` in `C2`, while ARCH_24 places the entire `2^3*5` in `C2`.

The genuine R20/R21 point instead has

\[
(C_2,C_3,\mu)=(71,4727,4),
\]

so

\[
\gcd(4,71)=\gcd(4,4727)=1.
\]

Therefore no divisor `d>1` can be extracted from the historical 40 as a universal Smith divisor. The universal common divisor supported by actual legal post-radial data is only

\[
\boxed{d_{\rm forced}=1.}
\]

## 4. Universal decimal-prime subclaims

The counterexample gives:

\[
2\mid\mu\quad\text{but}\quad 2\nmid C_2C_3,
\]

so `2|C2` and `2|C2C3` are not universal.

It also gives

\[
5\nmid\mu,
\qquad
5\nmid C_2C_3,
\]

so neither `5|mu` nor `5|C2C3` is universal.

R29 does **not** prove or disprove the isolated statement `2|mu` on every TC1+radial+shape point. That statement is insufficient for Smith extinction anyway, because the counterexample shows the radial support can be completely odd.

## 5. Xi absorption mechanism in the counterexample

Here

\[
r=5,
\quad
v_2(\mu)=2,
\quad
v_2(\Xi)=3,
\]

so the full `2^5` decimal budget splits between `mu` and `Xi` while `C2*C3` stays odd.

At 5,

\[
v_5(\mu)=0,
\quad
v_5(\Xi)=5,
\]

so `Xi` absorbs the entire decimal `5^5` budget.

This is the exact mechanism that kills the hoped-for universal decimal-prime support collision.

## 6. Continuation to the next frozen gate

The counterexample does not become a full Strict-A1 witness. Its denominator ratio is

\[
d=m_3-m_2=(n+g)-m=3,
\]

\[
\Theta=10^{-d}W/A=1/50,
\]

so

\[
\frac1{10}<\Theta<10
\]

fails.

Equivalently, the exact integer denominator window is

\[
Z_-=50,
\qquad
Z_+=9.
\]

R26 completely enumerated every selector/exponent tuple for this primitive packet and certified that this is the unique dual-collision candidate and that the packet is globally unliftable.

Hence the ordered first failure after the Smith/tail pass is

\[
\boxed{\texttt{DENOMINATOR\_RATIO\_CHAMBER}.}
\]

## 7. Verdict

```text
MU_SMITH_UNIVERSAL_COLLISION=FALSE
ARCHITECTURE_FREE_MU_SMITH_EXTINCTION=NO
UNIVERSAL_DECIMAL_PRIME_SUPPORT_COLLISION=NO
R29_COUNTEREXAMPLE_IS_GENUINE_POST_RADIAL_SUPPORT_PASS=YES
R29_COUNTEREXAMPLE_NEXT_FIRST_FAILURE=DENOMINATOR_RATIO_CHAMBER
R29_COUNTEREXAMPLE_PACKET_UNLIFTABLE_BY_R26=YES
```
