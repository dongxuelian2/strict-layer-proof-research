# 105-R32 — q=1 Extinction Assault / Proof Audit

## Claimed target

\[
q=1+\text{all frozen preconditions}\Longrightarrow\mathcal U_0=\varnothing.
\]

## What is proved

1. q=1 is exactly the two forced denominator digit conditions.
2. Coarse source-room nonemptiness is exactly \(U_{\rm lo}\le U_{\rm hi}\).
3. The exponent gap is exactly
   \[
   (m_3-m_2)-(n_3-n_2)=2g+k.
   \]
4. q=1 deletes the independent exponent search:
   \[
   m_2=\operatorname{dig}(A\Lambda),\
   m_3=\operatorname{dig}(W\Lambda),\
   g=m_3-n_3,\
   k=n_2-m_2-g.
   \]
5. The four digit inequalities alone reduce only to
   \[
   10^{-2}<P_2/(10^{2g+k}P_3)<10^2,
   \]
   not to a contradiction.
6. There is an exact primitive/support/source-room structural countermodel which
   fails only at TC1/master. Hence master is essential to any global q1 kill.

## Complete R28 Q0<=3000 q1 autopsy

The seven raw-TC1 q1 forced-scale hits are exactly replayed in
`105-R32-q1-seven-hit-autopsy.csv`.

Machine assertions:

```text
SEVEN_Q1_HITS=7
Ulo=1,Uhi=0 for 7/7
FACE3_ROOM_KILL=7/7
FACE2_ROOM_KILL=5/7
g=0,k=1,lambda_z=tau=1 for 7/7
Delta_U=1 for 7/7
```

Thus the bounded empirical/theorem-discovery signature is strikingly Face-3:
every historical q1 raw-TC1 hit already has

\[
C_3\ge10^{n_3}.
\]

This **cannot** be promoted to a global theorem from these seven rows.

## Infinite fixed-architecture stress test

R28 already proves an infinite primitive raw-TC1 conic family on the fixed
architecture

\[
1000P_1+50P_2+P_3=151Q_0,
\]

\[
(A,W,u_0,g_1^*,n,\delta,m,k,g)=(1,2,1,10,2,0,1,1,0),
\]

and proves the positive radial box globally empty on that fixed architecture.
Therefore q1/raw-TC1 geometry is not merely a seven-point finite accident; at
least one infinite fixed architecture is killed globally by the source room.

This still does not classify every moving architecture.

## New exact bounded falsification lane

R32 additionally exhausts

```text
A=W=u0=g1*=Lambda=1
U=1
n3=m2=m3=1
g=0
k=1..4
C3=1..9
C2 has exactly k+1 digits
```

Under TC1+primitive sphere the equation reduces to

\[
10^{k+2}P_1+10C_2+C_3=111Q_0.
\]

Exactly 899,910 \((k,C_2,C_3)\) configurations were checked.
The induced quadratic in \(P_1\) had **zero square discriminants** and hence zero
integer conic roots.

This is a complete theorem only for the stated lane, not global q1 extinction.

## Global status

No genuine TC1/master q1 architecture with \(U_{\rm lo}\le U_{\rm hi}\) was
found, but no architecture-uniform proof excluding one was obtained.

Therefore the only honest verdict is

```text
UNIT_CHAMBER_SOURCE_ROOM_EXTINCTION=NOT_PROVED_NOT_FALSIFIED
Q1_ROOM_KILL_FACE3_GLOBAL=NOT_PROVED
Q1_ROOM_KILL_FACE2_GLOBAL=FALSE_AS_A_SEVEN_HIT_PATTERN
Q1_DIGIT_ONLY_MUTUAL_EXCLUSION=FALSE_AS_A_FORMAL_IMPLICATION
MASTER_CONDITIONED_UNIT_SOURCE_ROOM_COLLISION=OPEN
```

No q1 extinction certificate is issued.
