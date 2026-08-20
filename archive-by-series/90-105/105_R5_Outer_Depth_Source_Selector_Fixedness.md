# 105-R5 — Outer-Depth Arithmetic Source Selector × Power10 Half-Ray Compression × Fixed-Character Bridge × Source-Phase Rigidity × Repair-or-Kill

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R5  
**Main variable:** \(Z=X/G=10^d\)  
**Outer domain:** \(d\le-1\) or \(d\ge2\)

---

# 1. Executive Verdict

本轮不能签发

```text
S3_S4_EXTINCT
FINITE_OUTER_DEPTH_PROVED
ARITHMETIC_SOURCE_TO_CHARACTER_BRIDGE_PROVED
OUTER_FAMILY_COMPRESSED_TO_FINITE_PROPER_COMPONENTS
```

也**不能严格签发**

```text
OUTER_DEPTH_FIXEDNESS_ARCHITECTURE_FALSIFIED
```

因为当前尚未构造满足 full primitive sphere、full master、complete source completion 的
\(|d|\to\infty\) genuine source-completed counterfamily。

本轮可以严格签发：

```text
R5_TERMINAL_VERDICT=
CURRENT_THREE_LANE_OUTER_FIXEDNESS_ENGINE_FALSIFIED
__GLOBAL_OUTER_FIXEDNESS_UNRESOLVED
```

中央新 obstruction：

\[
\boxed{\texttt{CROSS\_BASE\_SOURCE\_PHASE\_COVARIANCE}}
\]

或等价地：

\[
\boxed{\texttt{MOVING\_BASE\_SOURCE\_PHASE\_ESCAPE}}.
\]

含义：

> R2 已经把 absolute common-\(U\) 与 actual cut 内化，所以问题不再是 source section loss。  
> 现在的问题是：\(\kappa_{\rm src}\) 的 absolute position 是 **fibrewise** canonical，
> 而 outer depth \(d\) 是 **basewise** moving digit-depth label。当前没有跨不同 moving bases
> 的 nonhomogeneous source phase 把 \(d\) 钉到同一个 fixed arithmetic lattice。

---

# 2. Frozen R1–R4 State

```text
COMMON_OBSTRUCTION_CERTIFIED=YES
COMMON_OBSTRUCTION=SOURCE_AFFINE_SECTION_LOSS
PRE_BRANCH_MASTER_OBJECT_RECOVERED=YES

SOURCE_SECTION_INTERNALIZATION_THEOREM_PROVED=YES
KAPPA_SRC_CANONICAL=YES_IN_SOURCE_COMPLETED_CATEGORY
ACTUAL_CUT_INTERNALIZED=YES
Q1_COMMON_U_GLUE=FINITE_INDEX_AFFINE_U_SUBLATTICE

FINITE_SOURCE_COMPLETED_VALUATION_ATLAS_PROVED=YES
CANONICAL_CELLS=S0,S1,S2,S3,S4
VALUATION_ATLAS_SEMANTICALLY_SATURATED=YES
NEW_SEMANTIC_DIMENSION_DROP_FROM_VALUATION=NO

R4_FIXED_INCIDENCE_OFF_EXCEPTIONAL_CELLS=YES
R4_EXCEPTIONAL_CELLS=S3,S4
R4_REMAINING_GAP=
ARITHMETIC_SOURCE_SELECTOR_TO_FIXED_CHARACTER_BRIDGE_MISSING
```

---

# 3. Unified Outer-Depth Variable \(Z=10^d\)

定义：

\[
\boxed{Z:=X/G=10^d.}
\]

outer family：

\[
\boxed{
d\in(-\infty,-1]\cup[2,\infty).
}
\]

S3 与 S4 不是两个 architecture，而是同一个 \(Z\)-line 的两个 real chambers。

进一步定义：

\[
D:=|d|,
\qquad
W:=10^{-D}.
\]

则：

\[
S3:\ Z=W,
\qquad
S4:\ Z=W^{-1}.
\]

---

# 4. S3/S4 Unification

令 chamber sign：

\[
\epsilon=-1\iff S3,\qquad
\epsilon=+1\iff S4.
\]

下文 outer master 可统一写成：

\[
\boxed{
A\,W^{(1-\epsilon)/2}
+
B\,W^{(1+\epsilon)/2}
=0.
}
\]

也就是：

\[
S3:\ AW+B=0,
\]

\[
S4:\ A+BW=0.
\]

所以两个 half-rays 已经统一成同一个 \(W\to0\) boundary degeneration。

但：

\[
\boxed{
\text{没有已知 source-preserving }Z\leftrightarrow Z^{-1}\text{ involution}.
}
\]

两边 boundary coefficient 的 source provenance 不对称。

---

# 5. Outer Master Equation Package

冻结 R4：

\[
D_{\rm lead}:=KP_1-Q_0,
\qquad
T_3:=Q_0-P_3,
\]

\[
H=b_2Q_0-b_1XD_{\rm lead},
\]

\[
R=b_2Y-b_3,
\]

\[
Y\tau_3=b_3T_3,
\]

\[
b_2P_2-\tau_3-GH=0.
\]

primitive-word master：

\[
b_1XYG(KP_1-Q_0)
+b_2Y(P_2-GQ_0)
-b_3(Q_0-P_3)=0.
\]

代入 \(X=GZ\)：

\[
\boxed{
H=b_2Q_0-b_1GZD_{\rm lead}.
}
\tag{OM1}
\]

以及：

\[
\boxed{
b_1YG^2D_{\rm lead}Z
+b_2Y(P_2-GQ_0)
-b_3T_3
=0.
}
\tag{OM2}
\]

定义：

\[
\boxed{
A:=b_1YG^2D_{\rm lead},
}
\]

\[
\boxed{
B:=b_2Y(P_2-GQ_0)-b_3T_3.
}
\]

则：

\[
\boxed{AZ+B=0.}
\tag{OM}
\]

这是 R5 的最小 \(Z\)-carrier。

## Equation ledger

```text
EQUATION_ID=OM1
Z_EXPONENTS={1}
Z_AS_COEFFICIENT=NO
Z_AS_MONOMIAL=YES
SOURCE_VARIABLE_COUPLING=INDIRECT_THROUGH_BASE_DIGIT_LABELS_AND_WORD
CAN_Z_BE_FACTORED=YES
CAN_Z_BE_NORMALIZED=YES
OUTER_ASYMPTOTIC_ROLE=PREFIX/BORROW_CARRIER

EQUATION_ID=OM2
Z_EXPONENTS={1}
Z_AS_COEFFICIENT=NO
Z_AS_MONOMIAL=YES
SOURCE_VARIABLE_COUPLING=NO_DIRECT_U_TERM
CAN_Z_BE_FACTORED=YES
CAN_Z_BE_NORMALIZED=YES_AS_AZ+B=0
OUTER_ASYMPTOTIC_ROLE=TWO_BOUNDARY_CHARTS
```

关键点：

\[
\boxed{U\text{ 不直接出现在 }AZ+B=0.}
\]

所以 \(d\) 与 \(\kappa_{\rm src}\) 的真正连接只能通过 digit chamber / actual word。

---

# 6. Outer-Depth Source Ledger

source：

\[
a_i=UC_i.
\]

定义：

\[
\boxed{
\mu_i:=\frac{UC_i}{10^{n_i-1}},
\qquad
1\le\mu_i<10.
}
\]

A1 exponent normal form：

\[
\boxed{
m_2=g+d,\qquad
n_2=2g+k+d,\qquad
m_3=n_3+g.
}
\]

| source quantity | exact dependence on \(d\) | monotone? | bounded ratio? | integral? | finite-state? |
|---|---|---|---|---|---|
| \(m_2\) | \(g+d\) | fixed \(g\) only | n/a | yes | no |
| \(n_2\) | \(2g+k+d\) | fixed \(g,k\) only | n/a | yes | no |
| \(U\) | \(10^{2g+k+d-1}\mu_2/C_2\) | no globally | after moving normalization | yes | no |
| \(C_3/C_2\) | moving base direction | no | decade-controlled jointly | rational | no |
| \(\Phi_{23}\) | \(10^{2g+k+d-n_3}C_3/C_2\) | no | \((0.1,10)\) | rational | not finite |
| \(\gcd(U,V)\) | no explicit \(d\) | no | n/a | yes | arithmetic |
| actual cut | through \(n_i,m_i,x,U\) | no | n/a | exact | no fixed automaton |
| DES/J | no cross-outer \(d\)-equation | no | finite schema only | yes | no |

---

# 7. \(d\)-to-\(U\) Exact Transport

第二 numerator block：

\[
10^{n_2-1}\le UC_2<10^{n_2}.
\]

代入：

\[
n_2=2g+k+d.
\]

得到：

\[
\boxed{
10^{2g+k+d-1}\le UC_2<10^{2g+k+d}.
}
\tag{DU1}
\]

等价：

\[
\boxed{
U=\frac{10^{2g+k+d-1}}{C_2}\mu_2,
\qquad 1\le\mu_2<10.
}
\tag{DU2}
\]

最精确的 source-native integer formula：

\[
\boxed{
d=
\lfloor\log_{10}(UC_2)\rfloor+1-2g-k.
}
\tag{DU3}
\]

所以：

\[
\boxed{
d\text{ 确实 exact 进入 }\kappa_{\rm src}.
}
\]

但读取它需要 moving \(C_2,g,k\)，不是 fixed \(U\)-phase。

---

# 8. \(d\)-to-Actual-Cut Transport

R2 已证明：

\[
\operatorname{Word}_x(U)
\]

deterministically 恢复 actual word/cut。

outer 中：

\[
m_2=g+d,\qquad
n_2=2g+k+d.
\]

因此 cut position确实读取 \(d\)。

但是对 moving family：

\[
d\mapsto(x_d,U_d),
\]

没有 canonical transition：

\[
\operatorname{Word}_{x_d}(U_d)
\to
\operatorname{Word}_{x_{d+1}}(U_{d+1}),
\]

因为：

\[
C_i,V,P_i,Q_0,g,k,n_3
\]

都可移动。

历史 S3 no-borrow theorem进一步给出严格反例机制：

\[
d=-r,\qquad g=r+1
\]

时：

\[
m_2=1.
\]

所以：

\[
\boxed{
-d\to\infty
\not\Rightarrow
m_2\to\infty.
}
\]

“deep negative \(d\) 自动制造越来越长 fixed prefix” 被处决。

S4 则有：

\[
\boxed{1\le c\le10^d,}
\]

carry alphabet本身随 \(d\) 增长。

---

# 9. Primitive / GCD Audit

canonical source gate：

\[
\boxed{\gcd(U,V)=1.}
\]

它没有显式 \(d\)-term。

要借它控制 \(d\)，必须先导出统一 identity，使同一 \(2^r5^s\) forced 同时进入 \(U,V\)。

当前没有。

历史任意深 S3 reduced witness可取：

\[
d=-r,\quad g=r+1,
\]

\[
V=10^{2r+3},
\]

\[
U=10^{r+2}+1.
\]

于是：

\[
\boxed{\gcd(U,V)=1}
\]

对所有 \(r\ge1\) 成立。

该 witness 不是 full source candidate，但足以证明：

\[
\boxed{
\text{gcd gate 本身不可能提供 deep-}d\text{ bound。}
}
\]

---

# 10. DES Audit

R3 已把 \(J\) 降为 saturation decoration。

outer depth变化时：

- source lattice rank仍为 1；
- \(J\) schema不变；
- saturation value可移动；
- 无 \(J=F(d)\) fixed relation。

q=1 finite-index \(U\)-sublattice属于 S1 specialization，不是 S3/S4 的 cross-outer carrier。

因此：

```text
D_TO_DES_RELATION=
NO_CROSS_OUTER_NONHOMOGENEOUS_RELATION
```

---

# 11. Outer Compactification

令：

\[
[Z_0:Z_1]\in\mathbf P^1,
\qquad
Z=Z_1/Z_0.
\]

\(AZ+B=0\) homogenize：

\[
\boxed{
AZ_1+BZ_0=0.
}
\tag{OC}
\]

## \(Z\to0\)

\[
Z_1=0
\Longrightarrow
\boxed{B=0.}
\]

## \(Z\to\infty\)

\[
Z_0=0
\Longrightarrow
\boxed{A=0.}
\]

而：

\[
A=b_1YG^2D_{\rm lead}.
\]

在 actual A1 source chamber中这些因子均非零，因此固定 base 上：

\[
\boxed{A\ne0.}
\]

所以 fixed base 不可向 \(Z=\infty\) lift。

但是这不是 S4 extinction，因为真正的 \(d\to\infty\) sequence可同时让 base \(x_d\) 移动；当前没有 compactness/height theorem控制 \(A_d,B_d\)。

---

# 12. Boundary Source-Liftability

固定 source-completed base \(x\) 时：

\[
AZ+B=0
\]

唯一给出：

\[
\boxed{Z=-B/A.}
\]

因此：

\[
\boxed{
\text{fixed source fibre 上 }d\text{ 至多有一个值。}
}
\tag{FBR}
\]

所以：

\[
\boxed{
\textbf{所有 unbounded outer-depth escape 必须是 moving-base escape。}
}
\tag{MBE}
\]

这是 R5 最重要的 architecture theorem。

新的问题已经变成：

> 是否存在一个在不同 moving bases \(x_d\) 之间 canonical transport 的
> nonhomogeneous source phase？

当前答案：未找到。

---

# 13. Source-Completed Asymptotic Expansion

令：

\[
W=10^{-|d|}.
\]

S3：

\[
\boxed{B+AW=0.}
\tag{AS-}
\]

S4：

\[
\boxed{A+BW=0.}
\tag{AS+}
\]

所以 expansion exact truncates at first order。

但 small parameter \(W\) 的 coefficient 会随 \(|d|\) 同步增长，故 first-order expansion没有给 integer quantum。

---

# 14. Lane A — Integer-Remainder Rigidity

## S3

令：

\[
d=-D,\qquad D\ge1.
\]

\[
A10^{-D}+B=0.
\]

乘 \(10^D\)：

\[
\boxed{A+10^DB=0.}
\tag{IR-}
\]

若把 \(A10^{-D}\) 当 small remainder，需要 \(A\) independent of \(D\)。

但：

\[
A=b_1YG^2D_{\rm lead}.
\]

且 S3 legality：

\[
m_2=g-D\ge1
\]

强迫：

\[
\boxed{g\ge D+1.}
\]

因此 \(G^2\) 已至少提供：

\[
10^{2D+2}.
\]

除以 \(10^D\) 后净 scale仍至少增长：

\[
10^{D+2}.
\]

所以不存在：

\[
0<|R_{\rm int}|<1.
\]

## S4

令：

\[
d=D,\qquad D\ge2.
\]

master：

\[
\boxed{A10^D+B=0.}
\tag{IR+}
\]

这里没有 small term，反而：

\[
|B|=|A|10^D.
\]

除非有 independent upper bound on \(B/A\)，否则无 rigidity。

而 S4 carry range：

\[
1\le c\le10^D
\]

正展示了 moving coefficient capacity。

## Lane A verdict

\[
\boxed{\texttt{INTEGER\_REMAINDER\_RIGIDITY=NO}.}
\]

失败机制：

\[
\boxed{
\texttt{DECAY\_ABSORBED\_BY\_MOVING\_POWER10\_COEFFICIENT\_GROWTH}.
}
\]

---

# 15. Denominator-Growth Audit

| observable | integral scale | moving coefficient | growth | decay | net | rigidity |
|---|---|---|---|---|---|---|
| S3 \(A10^{-D}+B\) | \(10^D\) | \(A\supset G^2\) | \(\ge10^{2D+2}\) | \(10^{-D}\) | grows \(\ge10^{D+2}\) | NO |
| S4 reciprocal \(A+B10^{-D}\) | \(10^D\) | \(B=-A10^D\) | \(10^D\) relative to \(A\) | \(10^{-D}\) | exact balance | NO |
| \(\Phi_{23}\) | none | \(C_3/C_2\) | compensating | bounded | bounded | NO |
| \(h/Q_0\) | \(Q_0\) | \(Q_0\) moving | uncontrolled | \(<1\) normalized | no uniform quantum | NO |

---

# 16. Lane B — Power-of-Ten Purity

OM1：

\[
H=b_2Q_0-b_1GZD_{\rm lead}.
\]

所以：

\[
\boxed{
Z=
\frac{b_2Q_0-H}{b_1GD_{\rm lead}}.
}
\tag{P10-1}
\]

这确实是：

\[
10^d=A/B
\]

型 identity。

但：

\[
GZ=X=10^{m_2}.
\]

故：

\[
b_2Q_0-H
=b_1D_{\rm lead}10^{m_2}.
\]

因此 P10-1 只是 \(H\)-defining decimal word equation 的重写。

master还给：

\[
\boxed{Z=-B/A.}
\tag{P10-2}
\]

但两侧 numerator/denominator 都 moving。

---

# 17. Non-\((2,5)\)-Prime Audit

对：

\[
10^d=\frac{b_2Q_0-H}{b_1GD_{\rm lead}},
\]

\(p\ne2,5\) 时：

\[
v_p(b_2Q_0-H)=v_p(b_1D_{\rm lead}).
\]

然而这不是新 restriction，因为 exact word equality已经逐素强迫它。

没有第二条 source theorem强迫同一 \(p\) 落到 incompatible location。

历史 S3 还证明：deep \(d\) 的大 transverse factor可以主要落入 decimal \(2,5\)-support，ten-free residual不必随 \(|d|\) 增长。

所以：

\[
\boxed{\texttt{NON\_25\_PRIME\_OBSTRUCTION=NOT\_FOUND}.}
\]

\[
\boxed{\texttt{PURITY\_RIGIDITY=NO}.}
\]

---

# 18. Lane C — Canonical Source Phase

定义：

\[
\mu_i=\frac{UC_i}{10^{n_i-1}}\in[1,10).
\]

则：

\[
\frac{\mu_3}{\mu_2}
=
10^{n_2-n_3}\frac{C_3}{C_2}.
\]

定义：

\[
\boxed{
\Phi_{23}:=
10^{n_2-n_3}\frac{C_3}{C_2}
=
\frac{\mu_3}{\mu_2}.
}
\tag{PHI}
\]

于是：

\[
\boxed{10^{-1}<\Phi_{23}<10.}
\]

又：

\[
n_2=2g+k+d.
\]

所以：

\[
\boxed{
\Phi_{23}
=
10^{2g+k+d-n_3}\frac{C_3}{C_2}.
}
\tag{PHI-d}
\]

这是 R5 真正找到的：

\[
\boxed{
d\mapsto\text{ bounded source phase}.
}
\]

但它不产生 rigidity，因为：

\[
\boxed{C_3/C_2}
\]

是 moving primitive/source direction。

历史 S3 Smith coordinates中：

\[
C_3/C_2=N/M,
\]

且：

\[
\frac{P_3}{P_2}
=
\frac{\alpha t}{v}\frac NM.
\]

\(\alpha t/v\) 以相反 decimal rate移动，精确吸收 \(d\)。

因此：

```text
SOURCE_PHASE_OBSERVABLE=Phi23
SOURCE_PHASE_FOUND=YES
SOURCE_PHASE_RIGIDITY=NO
```

---

# 19. Actual-Cut / Finite-State Audit

actual cut：

\[
\operatorname{Word}_x(U)
\]

是 exact source function。

但是没有：

\[
d\mapsto q_d
\]

落入 fixed finite state set。

原因：

1. base \(x_d\) moving；
2. raw long-division state模 \(Q_0\)，而 \(Q_0\) 可无界；
3. S4 carry alphabet \(1,\dots,10^d\) 自身增长。

因此：

```text
ACTUAL_CUT_RIGIDITY=NO
FINITE_STATE_ONLY=NO_FIXED_FINITE_AUTOMATON
```

仅得到 \(d\bmod m\) 也不会构成 R5 progress。

---

# 20. Character-Bridge Extraction

候选：

\[
Z^aG^bK^cY^e=c_0.
\]

当前所有 \(Z\)-relations 都含 moving coefficient：

\[
Z=10^d,
\]

\[
Z=-B/A,
\]

\[
Z=
\Phi_{23}\,
10^{n_3-2g-k}
\frac{C_2}{C_3}.
\]

所以：

\[
\boxed{\texttt{FIXED\_CHARACTER\_RELATION=NONE\_PROVED}.}
\]

---

# 21. Fixedness / Properness Proof

若能得到 fixed：

\[
Z^aG^bK^cY^e=c_0
\]

且 exponent vector非零，则自然定义 proper translated subtorus。

所以当前 bottleneck不是 properness，而是 source derivation。

R5 没有得到 fixed coefficient \(c_0\)。

---

# 22. Outer-Depth Boundedness Attempt

三种候选均失败：

### additive bounded observable

\(\Phi_{23}\) bounded，但 moving \(C_3/C_2\) 吸收 \(d\)。

### logarithmic observable

\[
\log\Phi_{23}
=
d\log10
+(2g+k-n_3)\log10
+\log(C_3/C_2).
\]

最后一项 moving，所以不是 fixed linear form in logs。

### congruence + magnitude

generic outer source fibre没有 fixed affine \(U\)-coset；moving modulus也没有 size collision。

故：

\[
\boxed{\texttt{OUTER\_DEPTH\_BOUNDED=NO\_PROOF}.}
\]

---

# 23. Source-Completed Counterfamily Search

必须区分：

\[
\text{reduced-information witness}
\]

与：

\[
\text{full source-completed counterfamily}.
\]

历史 S3 任意深 witness：

\[
d=-r,\quad
g=r+1,\quad
k=1,
\]

\[
m_2=1,\quad
n_2=n_3=r+3,\quad
m_3=2r+4,
\]

\[
s=\alpha=\beta=t=u=u_0=1,
\quad
v=10^{2r+3},
\]

\[
M=N=1,\quad
C_2=C_3=1,
\]

\[
U=10^{r+2}+1.
\]

它通过：

```text
OUTER_EXPONENT_PROFILE
DENOMINATOR_DIGIT_LENGTHS
SMITH_RADIAL_2_3_DICTIONARY
COMMON_U_INTERVAL
INTEGER_SUCCESSOR
GCD_GATE
PROJECTIVE_RATIO_WINDOW
```

但未通过/未施加：

```text
P1_Q0_LEADING_WORD
FULL_PRIMITIVE_SPHERE
FULL_MASTER
FULL_DES_J_SEMANTICS
```

所以：

\[
\boxed{\texttt{SOURCE\_COMPLETED\_COUNTERFAMILY=NO}.}
\]

---

# 24. Failure Frontier Table

| family | exact algebraic | primitive | source interval | gcd | actual cut | DES | outer | first failure |
|---|---|---|---|---|---|---|---|---|
| S3 arbitrary-depth Smith-radial witness | PARTIAL | 2/3 only | YES | YES | PARTIAL | NO | YES | full \(P_1/Q_0\) leading-word + sphere/master |
| R4 ambient torus section | YES ambient | normalized sphere | NO | NO | NO | NO | arbitrary | denominator/source realization |
| fixed-base source fibre | YES | YES | YES | YES | YES | YES | at most one \(d\) | cannot move \(d\) without moving base |
| S4 carry-capacity schema | PARTIAL historical | unknown full | schema compatible | unknown full | growing carry | generic schema | YES | no full moving family |

第一未解决 exact gate：

\[
\boxed{
\textbf{FULL LEADING-WORD/SPHERE/MASTER COUPLING ACROSS MOVING BASES}.
}
\]

---

# 25. Big-Theorem Eligibility Audit

```text
LAURENT_ELIGIBILITY=NO
ESS_ELIGIBILITY=NO
SUBSPACE_ELIGIBILITY=NO
BAKER_ELIGIBILITY=NO
```

理由：

- 无 fixed proper torus relation；
- 无 fixed sparse S-unit equation；
- 无 fixed coefficient linear form in logarithms。

---

# 26. Falsified Routes

```text
R5-F1=SMALL_REMAINDER_FROM_W_ALONE
CAUSE=MOVING_COEFFICIENT_GROWTH_DOMINATES_DECAY

R5-F2=POWER10_PURITY_FROM_H_DEFINITION
CAUSE=DEPENDENCY_REDUNDANT_WORD_IDENTITY

R5-F3=NON_25_PRIME_PURITY_WITHOUT_SECOND_DIVISOR_CHANNEL
CAUSE=PRIME_SUPPORT_EQUALITY_ALREADY_FORCED_BY_MASTER

R5-F4=BOUNDED_SOURCE_PHASE_IMPLIES_D_BOUND
CAUSE=MOVING_C3_OVER_C2_ABSORBS_D

R5-F5=ACTUAL_CUT_GIVES_FIXED_FINITE_AUTOMATON
CAUSE=MOVING_BASE_AND_UNBOUNDED_Q0_CARRY_STATE

R5-F6=Z_TO_1_OVER_Z_SOURCE_DUALITY
CAUSE=A_AND_B_HAVE_ASYMMETRIC_SOURCE_PROVENANCE

R5-F7=FIXED_BASE_BOUNDARY_NONLIFTABILITY_IMPLIES_GLOBAL_EXTINCTION
CAUSE=UNBOUNDED_ESCAPE_IS_NECESSARILY_MOVING_BASE
```

---

# 27. Exact Remaining Unknowns

## U1 — full moving-base counterfamily

能否把 arbitrary-depth S3 reduced witness升级到：

\[
P_1/Q_0\text{ leading word}
+\text{primitive sphere}
+\text{full master}
+\text{DES}
\]

并保持 \(d\to-\infty\)？

若 YES，Route D 才真正合法。

## U2 — cross-base nonhomogeneous source invariant

是否存在：

\[
\Psi(x,U)\in\mathbf Z/M\mathbf Z
\]

或 bounded integer observable，使：

\[
\Psi=A10^d+B
\]

且 \(A\) uniform nonzero，并能 canonical transport across moving bases？

## U3 — S4 carry quotient

能否把：

\[
1\le c\le10^d
\]

压成 source-preserving normalized observable，并与 master形成 independent equation？

---

# 28. R5 Terminal Verdict — Seven Highest Questions

## Q1

S3/S4 是否真正统一？

\[
\boxed{
\textbf{YES at }Z/\mathbf P^1/W\textbf{ level.}
}
\]

但没有 \(Z\leftrightarrow Z^{-1}\) source duality。

## Q2

\(d\) 如何 exact 进入 \(\kappa_{\rm src}\)？

\[
\boxed{
d=
\lfloor\log_{10}(UC_2)\rfloor+1-2g-k.
}
\]

以及：

\[
\boxed{
\Phi_{23}
=
10^{2g+k+d-n_3}C_3/C_2
\in(0.1,10).
}
\]

## Q3

source selector 是否迫使 \(|d|\) 有界？

\[
\boxed{\textbf{NOT PROVED}.}
\]

## Q4

是否至少产生 fixed character？

\[
\boxed{\textbf{NO FIXED CHARACTER PROVED}.}
\]

## Q5

power-of-ten purity 是否产生新 rigidity？

\[
\boxed{\textbf{NO}.}
\]

最自然 identity 是 old word/master relation重写。

## Q6

actual cut / source phase 是否贡献 rigidity？

\[
\boxed{
\text{source phase: YES observable / NO rigidity;}
}
\]

\[
\boxed{
\text{actual cut: exact fibrewise / no fixed cross-base state.}
}
\]

## Q7

第一个允许 unbounded outer-depth 的 exact mechanism 是什么？

\[
\boxed{\texttt{MOVING\_BASE\_SOURCE\_PHASE\_ESCAPE}.}
\]

具体地：

\[
\boxed{
\text{outer depth在 moving base 上；source }U
\text{的 absolute position只在每个 fibre 内 canonical；}
}
\]

\[
\boxed{
C_3/C_2,\ \alpha t/v,\ G,\ \text{carry state}
\text{ 都有 capacity 吸收 }10^d\text{ 的漂移。}
}
\]

---

# 29. R6 Single Attack Target

按本 prompt 自己规定的 strict routing：

- Route A：未证 finite depth；
- Route B：未证 fixed character；
- Route C：未证 finitely many liftable boundary classes；
- Route D：未构造 full source-completed unbounded counterfamily。

所以：

\[
\boxed{
\textbf{R6 尚未被严格授权。}
}
\]

若必须继续编号，建议不是伪装成 R6，而是：

\[
\boxed{
\textbf{105-R5C — Moving-Base Full-Source Counterfamily-or-Cross-Base-Phase Test}.
}
\]

唯一二分：

1. 升级 arbitrary-depth S3 witness 到 full master/source completion；
2. 或在其 first failure 提取 cross-base nonhomogeneous invariant。

完成后才合法进入 Route D 或返回 fixed-character/finiteness route。

---

# Machine-readable terminal block

```text
R5_TERMINAL_VERDICT=CURRENT_THREE_LANE_OUTER_FIXEDNESS_ENGINE_FALSIFIED__GLOBAL_OUTER_FIXEDNESS_UNRESOLVED

R1_R2_R3_R4_STATE_FROZEN=YES

OUTER_MASTER_VARIABLE=Z=X/G=10^d
OUTER_DOMAIN=d<=-1_OR_d>=2
S3_S4_UNIFIED=YES_AS_ONE_Z_FAMILY_AND_P1_COMPACTIFICATION__NO_SOURCE_DUALITY

SOURCE_SELECTOR_COMPONENTS_USED=ABSOLUTE_U;DIGIT_INTERVAL;ACTUAL_CUT;GCD_UV;PRIMITIVE_SOURCE_DIRECTION;POSITIONAL_INTEGER_STRUCTURE;DES_AUDIT
D_TO_U_EXACT_RELATION=d=floor(log10(U*C2))+1-2g-k
D_TO_CUT_RELATION=m2=g+d;n2=2g+k+d;Word_x(U)_DETERMINISTIC_BUT_BASE_MOVES
D_TO_GCD_RELATION=NO_EXPLICIT_D_TERM__GCD_GATE_ALONE_ALLOWS_ARBITRARY_DEEP_REDUCED_WITNESS
D_TO_DES_RELATION=NO_CROSS_OUTER_NONHOMOGENEOUS_RELATION

OUTER_COMPACTIFICATION=P1_Z_WITH_A*Z1+B*Z0=0
BOUNDARY_PARAMETER=W=10^(-abs(d))
BOUNDARY_SOURCE_LIFTABILITY=FIXED_BASE_UNIQUE_Z__UNBOUNDED_ESCAPE_REQUIRES_MOVING_BASE

INTEGER_REMAINDER_CANDIDATE=A*Z+B_WITH_A=b1*Y*G^2*Dlead
REMAINDER_INTEGRAL_SCALE=10^abs(d)
REMAINDER_DECAY=10^(-abs(d))_FORMALLY
DENOMINATOR_GROWTH=S3_A_CONTAINS_G^2_WITH_g>=abs(d)+1;S4_B=-A*10^d_ON_MASTER
INTEGER_REMAINDER_RIGIDITY=NO

POWER10_PURITY_IDENTITY=Z=(b2*Q0-H)/(b1*G*Dlead)=-B/A
NON_25_PRIME_OBSTRUCTION=NONE_INDEPENDENT_FOUND
PURITY_RIGIDITY=NO__IDENTITY_IS_WORD_MASTER_REDUNDANT

SOURCE_PHASE_OBSERVABLE=Phi23=10^(n2-n3)*(C3/C2)=mu3/mu2_IN_(0.1,10)
ACTUAL_CUT_RIGIDITY=NO_FIXED_CROSS_BASE_PHASE
FINITE_STATE_ONLY=NO_FIXED_FINITE_AUTOMATON__MOVING_Q0_AND_S4_CARRY_ALPHABET

FIXED_CHARACTER_RELATION=NONE_PROVED
CHARACTER_TARGET=(G_m)^4
CHARACTER_PROPER=NOT_REACHED
CHARACTER_SOURCE_DERIVED=NO

OUTER_DEPTH_BOUNDED=NO_PROOF
OUTER_DEPTH_BOUND=NONE
OUTER_DEPTH_FINITE_SET=NONE

S3_STATUS=OPEN__ARBITRARY_DEPTH_REDUCED_WITNESS_SURVIVES_SELECTOR_SUBSYSTEM__FULL_MASTER_NOT_REACHED
S4_STATUS=OPEN__MOVING_CARRY_CAPACITY_UNCONTROLLED

SOURCE_COMPLETED_COUNTERFAMILY=NO_FULL_COUNTERFAMILY_CONSTRUCTED
COUNTERFAMILY_FIRST_FAILURE=FULL_P1_Q0_LEADING_WORD_PLUS_PRIMITIVE_SPHERE_MASTER_DES_COUPLING

LAURENT_ELIGIBILITY=NO
ESS_ELIGIBILITY=NO
SUBSPACE_ELIGIBILITY=NO
BAKER_ELIGIBILITY=NO

NEW_GLOBAL_RIGIDITY_MECHANISM=NONE_PROVED__CANONICAL_BOUNDED_SOURCE_PHASE_EXTRACTED
NEW_COMMON_OBSTRUCTION=CROSS_BASE_SOURCE_PHASE_COVARIANCE__MOVING_BASE_SOURCE_PHASE_ESCAPE

RETIRED_AFTER_R5=SMALL_REMAINDER_FROM_W_ALONE;TAUTOLOGICAL_POWER10_PURITY;FIXED_FINITE_CUT_AUTOMATON;NAIVE_Z_INVERSION_DUALITY;FIXED_BASE_BOUNDARY_TO_GLOBAL_EXTINCTION

R6_ATTACK_TARGET=NOT_AUTHORIZED_UNDER_STRICT_ROUTING__RECOMMEND_105_R5C_MOVING_BASE_FULL_SOURCE_COUNTERFAMILY_OR_CROSS_BASE_NONHOMOGENEOUS_PHASE
```

---

# Provenance / Frozen Source-of-Truth

- `105_R2_Source_Section_Internalization.md`
- `105_R3_Source_Completed_Valuation_Atlas.md`
- `105_R4_Source_Completed_Fixed_Incidence_Extraction.md`
- `95_R9_Outer_Plus_No_Borrow_Projective_Smallness_Assault.md`
- `95_R10_Second_Architecture_Shock_Checkpoint_and_New_Invariant_Audit.md`

No finite computation is promoted to theorem in this report.
