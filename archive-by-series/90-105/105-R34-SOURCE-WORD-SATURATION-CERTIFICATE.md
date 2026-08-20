# 105-R34 Source-Word Saturation Certificate

```text
R34_TERMINAL_ATTACK_FAILED
R34_SOURCE_WORD_SATURATION_CERTIFICATE=PROVED

STRICT_A1_UNLIFTABILITY_PROVED=NO
GLOBAL_N30_ZERO_THEOREM=NOT_PROVED
MASTER_SOURCE_WORD_ALLQ_EXTINCTION=NO
MASTER_SOURCE_WORD_UNIT_EXTINCTION=NO
DECIMAL_SOURCE_WORD_COLLISION=NO
FULL_STRICT_A1_WITNESS_FOUND=NO

F3_AUTHORITATIVE=V0*X3 == U*b3*Q0 (mod 10^n3)
F2_AUTHORITATIVE=V0*X2 == U*A2 (mod 10^n2)
F3_INFORMATION_GAIN=ZERO
F2_INFORMATION_GAIN=ZERO
U_ELIMINATION_INFORMATION_GAIN=ZERO
CROSS_REMAINDER_HAS_FULL_10_POWER_FACTOR=YES
REQUESTED_SIZE_GAP_STRUCTURALLY_IMPOSSIBLE=YES
R0_REDUCED_TO_OLD_CARRIER_EQUALITY=YES
ALLQ_SOURCE_WORD_CONGRUENCES_DEPENDENT=YES

UNIT_BRANCH_DEAD=NO
PRIME_BRANCH_DEAD=NO
```

## Certified dependency collapse

With
\[
A_3=b_3Q_0,\qquad
A_2=J_3+Q_0(b_2 10^g+b_1 10^{m+g}),
\]
the semantic source definitions imply
\[
V_0X_3-UA_3=-10^{n_3}UJ_3,
\]
\[
V_0X_2-UA_2=-10^{n_2}b_1UP_1.
\]

Thus both F2 and F3 are exact multiples of their moduli and add no restriction.

The proposed cross remainder satisfies
\[
R=U\left(10^{n_3}J_3C_2-10^{n_2}b_1P_1C_3\right),
\]
hence, for \(r=\min(n_2,n_3)\),
\[
10^r\mid R.
\]

Therefore if \(R\ne0\),
\[
|R|\ge10^r\ge M_r,
\]
which rules out the requested terminal pattern \(0<|R|<M_r\).

The zero branch is
\[
C_2T=10^{n_2}(P_1/g_1^*)P_3,
\]
an old carrier equality with no source-word variables.

## Saturation meaning

R34 has proved that "MASTER carry reads the full source words via F2/F3" is not an independent information class.
The low-decimal residues obtained in this way are already forced identities once the source words are defined as \(X_i=C_iU\).

Therefore further congruence bookkeeping on these same F2/F3 equations is retired.
