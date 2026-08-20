# 105-R7D — Primitive Determinant–Packet Compatibility × Source-(g1) Firewall × Difference-GCD Collision

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — A1-only  
**Round:** 105-R7D  
**Terminal verdict:** **PSDG WITNESS CONSTRUCTED; first failure moves to common-U integer successor; R8 Route B authorized.**

## 1. Executive Verdict

R7D does **not** prove PSDG empty. The proposed universal Source-Support Collision fails.

Instead, an inherited exact synchronized H0 state supplies a genuine nontrivial PSDG witness:
\[
(b_1,b_2,b_3)=(1,6,8),\quad
(P_1,P_2,P_3,Q_0)=(48,436,75,445),\quad V=24.
\]

It satisfies the primitive sphere, correct signed master, reduced determinant equation, exact source \(g_1\)-firewall, Smith chart, and exact DES identities. Its residual difference modulus is
\[
G_{\rm diff}=48,
\]
while
\[
M=195721=17\cdot29\cdot397,\qquad \gcd(G_{\rm diff},M)=1.
\]

The witness then reaches the post-PSDG common-U source fibre and fails at Integer Successor:
\[
I_{23}=[10/109,2/5)\subset(0,1).
\]

Therefore
\[
\boxed{\texttt{PSDG\_WITNESS\_CONSTRUCTED=YES}}
\]
and
\[
\boxed{\texttt{NEW\_FIRST\_FAILURE\_GATE=POST\_PSDG\_COMMON\_U\_INTEGER\_SUCCESSOR}}.
\]

R7 is complete as a PSDG campaign. R8 is authorized only by Route B.

## 2. Frozen R1–R7C State

All R1–R7C architecture remains frozen:
\[
by-ax=2c,
\]
\[
\beta_0\mid h\mid H_{\max},\qquad \gcd(h,\alpha\gamma_0g_{23})=1,
\]
\[
X_0Y_0=M,\quad (X_0,Y_0)=1,\quad b'Y_0-a'X_0=\Delta.
\]
No old discriminant/orientation/valuation/divisor-spacing/Gaussian architecture is reopened.

## 3. Correct Signed Reduced Master

With
\[
x=Q_0+P_1,\qquad y=Q_0-P_1,
\]
the frozen equation is
\[
\boxed{by-ax=2c}.
\]
After
\[
x=h\varepsilon X_0,\quad y=h\varepsilon Y_0,\quad a=ga',\quad b=gb',
\]
\[
\boxed{b'Y_0-a'X_0=\Delta},\qquad
\Delta=\frac{2c}{g\varepsilon h}.
\]

## 4. Legal Shared-GCD \(h\) Selector

For each fixed source profile:
\[
\boxed{
\mathcal H_{\rm legal}=
\{h:\beta_0\mid h\mid H_{\max},\ \gcd(h,\alpha\gamma_0g_{23})=1\}.
}
\]
It is finite profilewise, not uniformly finite.

For B:
\[
g_{23}=1,\qquad H_{\max}=1,\qquad\beta_0=1,
\]
so
\[
\boxed{\mathcal H_{\rm legal}=\{1\}}.
\]

## 5. \(H_{\max}\) Compression

For B:
\[
436^2+75^2=195721=17\cdot29\cdot397.
\]
The \(1\bmod4\) square-root part is 1. Also
\[
(b_2Y)^2+b_3^2=60^2+8^2=3664,
\]
and \(c=3345\). Hence
\[
H_{\max}=\gcd(3345,3664,1)=1.
\]

## 6. Reduced Coprime Normal Form

For B:
\[
h=1,\quad\varepsilon=1,\quad x=493,\quad y=397,
\]
so
\[
X_0=493,\qquad Y_0=397,\qquad M=195721.
\]

The primitive master row is
\[
(A_0,B_0,C_0)=(168,1000,26760),\qquad d_{\rm row}=8,
\]
hence
\[
(\widehat A,\widehat B,c)=(21,125,3345),
\]
\[
a=104,\quad b=146,\quad g=2,\quad a'=52,\quad b'=73,
\]
\[
\Delta=3345.
\]
Indeed
\[
\boxed{73\cdot397-52\cdot493=3345}.
\]

## 7. Determinant–Packet Theorem Recap

Frozen:
\[
\gcd(X_0,\Delta)=\gcd(X_0,b'),\qquad
\gcd(Y_0,\Delta)=\gcd(Y_0,a'),
\]
so
\[
\gcd(M,\Delta)\mid a'b'.
\]

For B:
\[
\gcd(M,\Delta)=1,
\]
thus packets \(17,29,397\) are valuation-FREE.

## 8. Source \(g_1\) Firewall

The exact condition is
\[
\boxed{\gcd(V,P_1)=V/b_1}.
\]
Since
\[
P_1=\frac{h\varepsilon(X_0-Y_0)}2,
\]
the reduced firewall is
\[
\gcd\!\left(V,\frac{h\varepsilon(X_0-Y_0)}2\right)=V/b_1.
\]

For B:
\[
\boxed{\gcd(24,48)=24=V/b_1}.
\]

## 9. Primewise \(g_1\) Valuation Profile

Let
\[
S_p=v_p(V),\quad T_p=v_p(b_1),\quad\tau_p=S_p-T_p,
\]
and put
\[
D=X_0-Y_0,\qquad
\eta_p=v_p(h)+v_p(\varepsilon)-v_p(2).
\]
Then
\[
v_p(P_1)=\eta_p+v_p(D)
\]
and the firewall is exactly
\[
\min(S_p,\eta_p+v_p(D))=\tau_p.
\]

If \(T_p=0\):
\[
\boxed{\eta_p+v_p(D)\ge\tau_p}.
\]
This is a lower bound, not equality.

If \(T_p>0\):
\[
\boxed{\eta_p+v_p(D)=\tau_p}.
\]
This is exact.

## 10. Prefactor Oversupply Gate

The true cheap contradiction is
\[
\boxed{
T_p>0\ \text{and}\ \eta_p>\tau_p
\Longrightarrow\text{firewall impossible}.
}
\]

When \(T_p=0\), extra \(p\)-adic content is allowed because the gcd is already saturated at \(p^{S_p}\). Thus the blanket oversupply rule in the prompt requires this correction.

## 11. Residual Difference Modulus \(G_{\rm diff}\)

Define
\[
d_p=\max(0,\tau_p-\eta_p),\qquad
\boxed{G_{\rm diff}=\prod_{p\mid V}p^{d_p}}.
\]
Then
\[
G_{\rm diff}\mid D.
\]

Shell:
- \(p\mid b_1\): \(v_p(D)=d_p\) exactly;
- \(p\nmid b_1\): \(v_p(D)\ge d_p\).

For B:
\[
p=2:\ (S,T,\tau,\eta,d)=(3,0,3,-1,4),
\]
\[
p=3:\ (S,T,\tau,\eta,d)=(1,0,1,0,1),
\]
hence
\[
\boxed{G_{\rm diff}=48}.
\]
Actual \(D=96\), so the shell passes.

## 12. Coprime Product Difference Lemma

If \((X,Y)=1\), then
\[
\boxed{\gcd(XY,X-Y)=1}.
\]
Also
\[
\boxed{\gcd(XY,X+Y)=1}.
\]

Thus in R7D
\[
\boxed{\gcd(M,X_0-Y_0)=1}.
\]

This elementary fact strictly subsumes the forced-packet/difference-divisibility contradiction.

## 13. Source-Support Collision Criterion

Since \(G_{\rm diff}\mid X_0-Y_0\),
\[
\boxed{\gcd(G_{\rm diff},M)=1}
\]
is necessary.

## 14. \(\gcd(G_{\rm diff},M)\) Source Audit

For B:
\[
G_{\rm diff}=48,\qquad M=195721=17\cdot29\cdot397,
\]
so
\[
\boxed{\gcd(48,195721)=1}.
\]
Therefore universal Source-Support Collision is false.

## 15. Collision-Evasion Profile Conditions

A profile evades elementary collision iff
\[
\operatorname{rad}(G_{\rm diff})\cap\operatorname{rad}(M)=\varnothing.
\]
Mechanisms include prefactor absorption, Smith support separation, decimal support absent from reduced norm, and saturated \(T_p=0\) lower-bound cases.

B realizes this separation exactly.

## 16. Forced Packet Orientation Map

State E:
\[
(b_1,b_2,b_3)=(5,5,1),
\]
\[
(P_1,P_2,P_3,Q_0)=(298,2514,1485,2935),\quad V=5.
\]

Reduced:
\[
a'=4449=3\cdot1483,\qquad b'=5551=7\cdot13\cdot61,
\]
\[
X_0=3233=53\cdot61,\qquad Y_0=2637=3^2\cdot293,
\]
\[
M=3^2\cdot53\cdot61\cdot293,\qquad \Delta=254370.
\]

Hence:
\[
61\to X,\qquad 3^2\to Y,\qquad 53,293\to FREE.
\]
And indeed
\[
X_0=61\cdot53,\qquad Y_0=9\cdot293.
\]
So packet forcing is exact but not a universal killer.

## 17. Difference Residue Condition

If \(G_{\rm diff}\mid X_0-Y_0\), set
\[
X_0\equiv Y_0\equiv T\pmod{G_{\rm diff}}.
\]
Then
\[
\boxed{T^2\equiv M\pmod{G_{\rm diff}}}.
\]

For B:
\[
T\equiv13\pmod{48},
\]
and the square condition passes.

## 18. Determinant Residue Condition

The determinant yields
\[
\boxed{(b'-a')T\equiv\Delta\pmod{G_{\rm diff}}}.
\]
For B:
\[
21\cdot13\equiv3345\pmod{48}.
\]
PASS.

## 19. Elimination Modulo \(G_{\rm diff}\)

Exact identity:
\[
\boxed{
\Delta^2-(b'-a')^2M
=(X_0-Y_0)(a'^2X_0-b'^2Y_0).
}
\]
So the resultant congruence is automatic once product + determinant + difference divisibility are imposed:
\[
\boxed{\texttt{RESULTANT\_CONGRUENCE=TAUTOLOGICAL\_POST\_SOLUTION}}.
\]
It remains only a pre-solution sieve.

## 20. Exact Difference Valuation Shell

For \(p\mid b_1\), the difference exponent is exact.  
For \(p\nmid b_1\), it is only lower bounded.

B:
\[
v_2(D)=5\ge4,\qquad v_3(D)=1\ge1.
\]

## 21. Free-Packet Residue Gate

After
\[
X_0=M_XU,\quad Y_0=M_YV',\quad UV'=M_F,
\]
the source congruence becomes
\[
M_XU\equiv M_YV'\pmod G.
\]
This is a legitimate per-profile sieve, but not a universal architecture after B and E.

## 22. Source-Support Collision Theorem Attempt

**Refuted as universal.** B has \(G_{\rm diff}>1\) and \(\gcd(G_{\rm diff},M)=1\).

## 23. Determinant–Difference Obstruction Attempt

**Not universal.** B passes both canonical residue congruences modulo 48.

## 24. Packet-Residue Obstruction Attempt

**Not universal.** E realizes nontrivial forced packets exactly.

## 25. Difference-First Witness Construction

For B:
\[
D=96,\qquad M=195721,
\]
and
\[
D^2+4M=890^2.
\]
Therefore
\[
Y_0=(890-96)/2=397,\qquad X_0=493.
\]

## 26. Determinant-First Witness Construction

For B:
\[
73Y_0-52X_0=3345,\qquad X_0Y_0=195721
\]
selects
\[
(X_0,Y_0)=(493,397).
\]

## 27. Reduced PSDG Witness Audit

```text
H=1
EPSILON=1
M=195721
DELTA=3345
A_PRIME=52
B_PRIME=73
X0=493
Y0=397
G_DIFF=48
GCD_G_DIFF_M=1
```

All reduced PSDG checks pass.

## 28. \((P_1,Q_0)\) Recovery

\[
P_1=\frac{493-397}{2}=48,\qquad
Q_0=\frac{493+397}{2}=445.
\]

## 29. Primitive / \(g_1\) Verification

\[
48^2+436^2+75^2=445^2,
\]
\[
\gcd(48,436,75,445)=1,
\]
\[
\gcd(24,48)=24.
\]

Exceptional square:
\[
W=\widehat BQ_0-\widehat AP_1=54617,
\]
and
\[
W^2=c^2+abN.
\]
All pass.

## 30. Smith / DES / Source Downstream Audit

Use
\[
s=1,\ \alpha=1,\ \beta=2,\ t=3,\ u=1,\ v=4.
\]
Then
\[
V=24,\qquad(g_1,g_2,g_3)=(24,4,3).
\]

DES:
\[
D_{\rm lead}=35,\quad H=2320,\quad R=52,\quad K_3=296,
\]
with exact identities
\[
48\cdot100=445\cdot16-2320,
\]
\[
6\cdot436=2320+296.
\]
Smith and DES pass.

Common-U source fibre:
\[
C_2=109,\quad C_3=25,
\]
\[
I_{23}=\left[\frac{10}{109},\frac25\right).
\]
The real interval is nonempty but lies in \((0,1)\), hence contains no positive integer.

## 31. New First-Failure Gate

\[
\boxed{
\texttt{NEW\_FIRST\_FAILURE\_GATE}
=
\texttt{POST\_PSDG\_COMMON\_U\_INTEGER\_SUCCESSOR}
}
\]

This is specifically the integer radial/source-fibre layer, because the continuous interval already survives.

## 32. Architecture Shock Verdict

Q1 legal \(h\) finite per profile? **YES.**  
Q2 proposed oversupply universal? **NO; correct only in nonsaturated \(p\mid b_1\) case.**  
Q3 \(G_{\rm diff}\) canonical? **YES, with mixed exact/lower-bound shell.**  
Q4 \(\gcd(M,X_0-Y_0)=1\)? **YES.**  
Q5 \(\gcd(G_{\rm diff},M)=1\) necessary? **YES.**  
Q6 source universally violates it? **NO; B refutes.**  
Q7 determinant residue universal contradiction? **NO; B passes.**  
Q8 forced packets universal killer? **NO; E realizes them.**  
Q9 reduced PSDG witness? **YES.**  
Q10 \((P_1,Q_0)\) recovery? **YES.**  
Q11 PSDG empty? **NO; crossed by witness.**  
Q12 continue Web-side R7? **NO; first failure moved downstream.**

## 33. Continue-Web Decision

\[
\boxed{\texttt{CONTINUE\_WEB\_R7=NO}}.
\]
This is because R7 succeeded on its witness branch, not because of mere information exhaustion. No R7E should be manufactured.

## 34. R8 Authorization Decision

By strict Route B:
\[
\boxed{\texttt{R8\_AUTHORIZED=YES}}.
\]

\[
\boxed{\texttt{R8\_ARCHITECTURE=POST\_PSDG\_FIRST\_FAILURE\_ASSAULT}}
\]
with single target
\[
\boxed{\texttt{COMMON\_U\_INTEGER\_SUCCESSOR__SOURCE\_FIBRE\_INTEGER\_RADIAL\_GATE}}.
\]

R8 is not executed here.

# Machine-readable Terminal Block

```text
R7D_TERMINAL_VERDICT=PSDG_WITNESS_CONSTRUCTED__FIRST_FAILURE_MOVED_TO_COMMON_U_INTEGER_SUCCESSOR

R1_R2_R3_R4_R5_R5C_R6_R7_R7B_R7C_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=POST_PSDG_COMMON_U_INTEGER_SUCCESSOR

LEGAL_H_SET=PROFILEWISE_FINITE__B_WITNESS_HAS_H_SET_{1}
H_FINITE_PER_PROFILE=YES
H_UNIFORM_FINITE=NO

EPSILON_CASES={1,2}__B_WITNESS_EPSILON=1

M=195721
DELTA=3345
A_PRIME=52
B_PRIME=73

DETERMINANT_PACKET_THEOREM_FROZEN=YES

SOURCE_G1_FIREWALL=gcd(V,P1)=V/b1
V=24
B1=1

P1_REDUCED_FORM=h*epsilon*(X0-Y0)/2

G1_TARGET_VALUATIONS=p=2:tau=3;p=3:tau=1
PREFACTOR_VALUATIONS=p=2:eta=-1;p=3:eta=0
PREFACTOR_OVERSUPPLY=NO_FOR_B__GENERAL_GATE_ONLY_IF_vp(b1)>0_AND_eta>tau

G_DIFF=48
G_DIFF_EXACT=MINIMAL_DIVISIBILITY_MODULUS__EXACT_SHELL_IF_p|b1__LOWER_BOUND_IF_p_NOT_DIVIDE_b1
GCD_G_DIFF_M=1

COPRIME_PRODUCT_DIFFERENCE_LEMMA=PROVED
GCD_M_XMINUSY=1

SOURCE_SUPPORT_COLLISION=NOT_UNIVERSAL__EXACT_WITNESS_B_REFUTES

PACKET_ORIENTATION_MAP=B:ALL_FREE__E:61->X,3^2->Y,53_FREE,293_FREE
M_X=1_FOR_B__61_FOR_E
M_Y=1_FOR_B__9_FOR_E
M_FREE=195721_FOR_B__15529_FOR_E

DIFFERENCE_RESIDUE_CONDITION=T^2=M_mod_G_DIFF__B_PASS_T=13_mod_48
DETERMINANT_RESIDUE_CONDITION=(bprime-aprime)T=Delta_mod_G_DIFF__B_PASS

T_MOD_G_DIFF=13
T_SQUARE_CONDITION=PASS
RESULTANT_CONGRUENCE=PASS_BUT_TAUTOLOGICAL_AFTER_FULL_PRODUCT+DETERMINANT+DIFFERENCE

EXACT_DIFFERENCE_VALUATION_SHELL=MIXED__EXACT_WHEN_p|b1__LOWER_BOUND_WHEN_p_NOT_DIVIDE_b1

PACKET_RESIDUE_OBSTRUCTION=NOT_UNIVERSAL

REDUCED_PSDG_WITNESS=YES
H_WITNESS=1
EPSILON_WITNESS=1
X0_WITNESS=493
Y0_WITNESS=397

P1_RECOVERED=48
Q0_RECOVERED=445
SPHERE_VALID=YES
MASTER_VALID=YES
PRIMITIVE_VALID=YES
G1_FIREWALL_VALID=YES

SMITH_LIFT=YES
DES_LIFT=YES
SOURCE_FIBRE_LIFT=CONTINUOUS_PASS__INTEGER_FAIL
DIGIT_LIFT=NOT_REACHED_AFTER_INTEGER_SOURCE_FIBRE_FAILURE
ACTUAL_CUT_LIFT=NOT_REACHED
OUTER_LIFT=NO

PSDG_EMPTY_THEOREM=NO
PSDG_WITNESS_CONSTRUCTED=YES

NEW_FIRST_FAILURE_GATE=POST_PSDG_COMMON_U_INTEGER_SUCCESSOR

R7D_SINGLE_FINAL_ARITHMETIC_GATE=NO

CONTINUE_WEB_R7=NO

R8_AUTHORIZED=YES
R8_ARCHITECTURE=POST_PSDG_FIRST_FAILURE_ASSAULT
R8_SINGLE_ATTACK_TARGET=COMMON_U_INTEGER_SUCCESSOR__SOURCE_FIBRE_INTEGER_RADIAL_GATE
```

# Companion artifact verification

B PASS; first failure COMMON_U_INTEGER_SUCCESSOR
E PASS; forced packets 61->X and 3^2->Y
