# 105-R4 — Source-Completed Power10 Fixed-Incidence Extraction × Moving-Coefficient Elimination × Primitive/Smith Semantic Descent × Proper-Component Certification × Global Arithmetic Eligibility

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R4  
**Date:** 2026-08-19  
**Nature:** global-rigidity entry / fixed-incidence extraction audit; **not** an extinction round.

---

# 1. Executive Verdict

本轮得到一个**严格的部分成功 + 一个新的全局瓶颈定位**：

\[
\boxed{
\texttt{R4\_TERMINAL\_VERDICT
=
FIXED\_INCIDENCE\_EXTRACTED\_OFF\_EXCEPTIONAL\_CELLS}
}
\]

更具体地，R3 的四个 decimal torus coordinates

\[
(G,K,X,Y)
=
(10^g,10^k,10^{m_2},10^{n_3})
\]

必须一起保留。令

\[
T_4=(\mathbf G_m)^4.
\]

则五个 canonical cells 中：

\[
S0:\quad G=1,
\]

\[
S1:\quad X=G,
\]

\[
S2:\quad X=G\quad\text{or}\quad X=10G.
\]

因此：

\[
\boxed{
S0\cup S1\cup S2
\subset
V_{\rm pre}
:=
V\!\left((G-1)(X-G)(X-10G)\right)
\subsetneq T_4.
}
\tag{R4-PARTIAL}
\]

这是：

- fixed；
- explicit；
- proper；
- finite-character；
- cross-cell；

的 incidence。

但是：

\[
\boxed{
E_{\rm exc}=\{S3,S4\}.
}
\]

在 outer cells：

\[
d=m_2-g
\]

沿半直线无界，而

\[
\boxed{
Z_{\rm out}:=\frac XG=10^d
}
\]

只给：

\[
S3:\ d\le-1,
\qquad
S4:\ d\ge2.
\]

因此当前没有证明 \(Z_{\rm out}\) 落入有限 coefficient family，也没有得到对全部 \(A_1\) 的 fixed proper incidence。

更重要的是，本轮证明了 ordinary algebraic elimination 为什么会失效。对 normalized primitive ray

\[
p_i=P_i/Q_0,\qquad p_1^2+p_2^2+p_3^2=1
\]

和 denominator projective class \([b_1:b_2:b_3]\)，master 可写为

\[
b_1XYG(Kp_1-1)
+b_2Y(p_2-G)
-b_3(1-p_3)=0.
\tag{NM}
\]

在 open set \(1-p_3\ne0\) 上，\(b_3\) 可吸收任意 power-torus state。事实上固定 primitive point

\[
(p_1,p_2,p_3)=\left(\frac27,\frac37,\frac67\right),
\qquad
b_1=b_2=1
\]

后取

\[
\boxed{
b_3=
XYG(2K-7)+Y(3-7G)
}
\tag{SEC}
\]

即可使 (NM) 恒等成立。

因此 relaxed algebraic master envelope 对 \(T_4\) 的 projection 是 dominant；其 Laurent elimination ideal 在 power variables 上为零。这个结果是 **K2 — AMBIENT-ONLY**，不是 source theorem。

真正的 source section

\[
\kappa_{\rm src}
\]

主要通过：

- \(U\in\mathbf Z_{>0}\)；
- digit interval；
- \(\gcd(U,V)=1\)；
- q=1 affine congruence；
- exact actual-cut semantics；

进入，而这些数据不能由 ordinary polynomial ideal 无损表示。

所以本轮不能安全 eliminate \(U\)。

最终新的唯一缺口被命名为：

\[
\boxed{
\texttt{ARITHMETIC\_SOURCE\_SELECTOR\_TO\_FIXED\_CHARACTER\_BRIDGE\_MISSING}.
}
\]

R5 因而唯一进入：

\[
\boxed{
\textbf{Route C — Exceptional Fixedness Repair}
}
\]

并统一攻击：

\[
\boxed{
S3/S4
\quad\text{via}\quad
Z_{\rm out}=X/G=10^d.
}
\]

---

# 2. Frozen R1–R3 Architecture

以下全部冻结：

```text
COMMON_OBSTRUCTION_CERTIFIED=YES
COMMON_OBSTRUCTION=SOURCE_AFFINE_SECTION_LOSS
PRE_BRANCH_MASTER_OBJECT_RECOVERED=YES

SOURCE_SECTION_INTERNALIZATION_THEOREM_PROVED=YES
KAPPA_SRC=CANONICAL_IN_SOURCE_COMPLETED_CATEGORY
J_SATURATION_FUNCTORIALITY_PROVED=YES
Q1_COMMON_U_GLUE=FINITE_INDEX_AFFINE_U_SUBLATTICE

FINITE_SOURCE_COMPLETED_VALUATION_ATLAS_PROVED=YES
CANONICAL_PRIMARY_CELLS=S0,S1,S2,S3,S4
VALUATION_ATLAS_SEMANTICALLY_SATURATED=YES
NEW_SEMANTIC_DIMENSION_DROP_FROM_VALUATION=NO
```

R4 不重新打开 \(J\)-branching、valuation refinement、Gaussian orientation、conductor、raw SNF、resonance endpoint、transition headroom、outer-plus inequality、common-\(U\) 单独攻击等退休路线。

---

# 3. Master Source-Completed Incidence

R3 的 fixed-support algebraic core：

\[
F_{\rm sph}
=
P_1^2+P_2^2+P_3^2-Q_0^2=0,
\]

\[
D=KP_1-Q_0,
\qquad
T_3=Q_0-P_3,
\]

\[
H=b_2Q_0-b_1XD,
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

等价 primitive-word master：

\[
\boxed{
b_1XYG(KP_1-Q_0)
+b_2Y(P_2-GQ_0)
-b_3(Q_0-P_3)=0.
}
\tag{M}
\]

source completion：

\[
C_i=P_i/\gcd(V,P_i),
\qquad
\gcd(C_1,C_2,C_3)=1,
\]

\[
a_i=UC_i,
\qquad
U=\gcd(a_1,a_2,a_3),
\]

\[
10^{n_i-1}\le UC_i<10^{n_i},
\qquad
\gcd(U,V)=1.
\]

q=1 decorated source还要求：

\[
31C_3U+d_q\tau\equiv0\pmod{2Kd_q}.
\]

因此 master 是：

\[
\boxed{
\mathscr Z_{\rm sem}^{\rm src}
=
(\text{fixed algebraic equalities})
\times
(\text{primitive/Smith arithmetic})
\times
\kappa_{\rm src}.
}
\]

它不是一个可以无损缩成单个 ordinary finite-type scheme 的对象。

---

# 4. Projection Ledger

核心 projection 结论：

| Projection | Target | Source loss | Generic relaxed fibre | Fixed target | Result |
|---|---|---:|---:|---:|---|
| \(\pi_{GK}^{\rm amb}\) | \((\mathbf G_m)^2\) | severe | 5 | yes | dominant ambient envelope |
| \(\pi_{T4}^{\rm amb}\) | \(T_4\) | severe | 3 | yes | dominant ambient envelope |
| \(\pi_{GK}^{\rm src}\) | \((\mathbf G_m)^2\) | none at source | unknown | yes | actual closure **OPEN** |
| \(\pi_{T4}^{\rm src}\) | \(T_4\) | none at source | mixed arithmetic | yes | proper on S0–S2 only |
| \(\pi_{GKU}\) | \((\mathbf G_m)^2\times\mathbf A^1\) | less | positive | yes | source-safe carrier, no proper global image yet |
| \(\pi_{\rm mod}\) | \(T_4\times Q_{\rm sph}\times\mathbf P^2_b\) | loses absolute source scale | 0 inside incidence | yes | fixed moduli incidence, not rigidity projection |

`105_R4_Projection_Ledger.csv` gives the full ledger.

---

# 5. Dimension/Fibre Audit

## 5.1 Algebraic normalized envelope

在 \(Q_0\ne0\) chart，令：

\[
p_i=P_i/Q_0.
\]

primitive sphere quotient：

\[
Q_{\rm sph}:\quad p_1^2+p_2^2+p_3^2=1
\]

维数为 2。

master 对 denominator variables \(b_i\) 齐次，因此 algebraic presentation quotient 给：

\[
[b_1:b_2:b_3]\in\mathbf P^2,
\]

维数为 2。

加上：

\[
T_4,\quad \dim=4,
\]

再减去 master 的一个 equation：

\[
\boxed{
d_{\rm alg}=4+2+2-1=7.
}
\]

由于 \(\pi_{T4}^{\rm amb}\) dominant：

\[
\boxed{
d_{\rm fibre}^{T4}=7-4=3
}
\]

on a generic open set.

再 forget \(X,Y\)：

\[
\boxed{
d_{\rm fibre}^{GK}=5
}
\]

for the relaxed envelope.

## 5.2 Semantic dimensions

这里不能伪造一个单一 scheme dimension。

严格区分：

```text
d_torus=4
d_primitive_algebraic=2
d_denominator_projective_algebraic=2
d_relaxed_master=7
d_generic_relaxed_fibre_over_T4=3
d_generic_relaxed_fibre_over_GK=5
source_radial_rank=1
q1_source_radial_rank=1_on_finite_index_affine_sublattice
d_actual_source_mixed=NOT_A_PURE_SCHEME_DIMENSION
```

因此 generic positive-dimensional moving fibre 已经解释：

\[
\boxed{
\text{plain elimination 不应被期待自动产生 }F(G,K)=0.
}
\]

---

# 6. Moving-Data Classification

## D1 — Gauge / presentation data

可 quotient：

- arbitrary Smith/Hermite basis；
- Gaussian orientation；
- historical chart basis；
- derived coordinates \(D,T_3,H,R,\tau_3,\Delta_{12},\Delta_3\)（保留 defining equations 后）；
- denominator common scalar **仅在 algebraic envelope 中**可 projectivize。

注意：denominator absolute scale在 source category 中影响 digit lengths，所以不能全局作为 source gauge 删除。

## D2 — Genuine primitive direction

\[
[P_1:P_2:P_3:Q_0]
\]

是 dimension-2 genuine algebraic freedom；不是有限类型 coefficient label。

## D3 — Smith / denominator arithmetic data

raw basis可 quotient 到：

- pairwise gcd；
- canonical Smith divisors；
- DES saturation index \(J\)。

但：

\[
[b_1:b_2:b_3]
\]

及 absolute denominator scale \(V\) 仍是真正 moving arithmetic data。

\(J\) 的 construction schema finite，不意味着 \(J\) value 或 denominator moduli finite。

## D4 — Radial source data

\[
\boxed{U}
\]

是真正 source-semantic coordinate，必须保留。

## D5 — Power/cut data

\[
G,K,X,Y
\]

全部是 torus coordinates，不是 moving coefficients。

numerical digit depths可无界；active-face combinatorics finite。

---

# 7. Canonical Quotient Search

定义 algebraic moduli envelope：

\[
\boxed{
\mathcal M_{\rm alg}
=
Q_{\rm sph}\times\mathbf P^2_b.
}
\]

并有 fixed map：

\[
\Theta_{\rm alg}:
\mathscr Z_{\rm alg}
\to
T_4\times\mathcal M_{\rm alg}.
\]

master 变为：

\[
b_1A_1+b_2A_2+b_3A_3=0,
\]

其中

\[
A_1=XYG(Kp_1-1),
\quad
A_2=Y(p_2-G),
\quad
A_3=-(1-p_3).
\]

这个 quotient：

- quotient 掉 primitive common scale；
- quotient 掉 denominator algebraic common scale；
- 不依赖 arbitrary basis；
- target fixed。

但：

\[
\boxed{
\kappa_{\rm src}\text{ 不可从 }\Theta_{\rm alg}\text{ 读取。}
}
\]

所以：

\[
\boxed{
\Theta_{\rm alg}
\text{ 是 canonical algebraic envelope，不是 source-complete quotient。}
}
\]

---

# 8. \(U\)-Eliminate-or-Retain Decision

正式选择：

\[
\boxed{
\texttt{U\_POLICY=RETAIN}.
}
\]

理由：

1. \(U\) 是 numerator triple 的 intrinsic common content；
2. algebraic master 在 radial cancellation 后本来就不含 \(U\)；
3. 如果再从 source object中删除 \(U\)，digit interval和 coprime selector不会留下 ordinary polynomial trace；
4. q=1 的 congruence仅是特殊 decorated cell，不提供 cross-cell uniform replacement；
5. 当前没有证明一个 fixed discriminant/resultant/character 可以完整编码 \(U\)-selector。

所以：

\[
\boxed{
\texttt{U\_ELIMINATION\_SOURCE\_SAFE=NO\_GLOBAL}.
}
\]

Route U-E 未达到证明标准；采用 Route U-R。

---

# 9. Source-Semantic Elimination Setup

定义 Laurent base ring：

\[
R_T
=
\mathbf Q[G^{\pm1},K^{\pm1},X^{\pm1},Y^{\pm1}].
\]

normalized ambient variables：

\[
p_1,p_2,p_3,b_1,b_2,b_3.
\]

algebraic relaxation ideal：

\[
I_{\rm amb}
=
\langle
p_1^2+p_2^2+p_3^2-1,
\;
b_1XYG(Kp_1-1)+b_2Y(p_2-G)-b_3(1-p_3)
\rangle.
\]

source-semantic object不能写成：

\[
I_{\rm sem}=I_{\rm amb}+\langle\text{几个 polynomials}\rangle
\]

而保持 exact equivalence，因为：

- gcd；
- positivity；
- digit intervals；
- \(U\in\mathbf Z\)；
- finite-index affine congruence；

属于 mixed arithmetic annotation。

因此 R4 **拒绝伪造**：

\[
\operatorname{Spec}(R/I_{\rm sem})
\cong
\mathscr Z_{\rm sem}^{\rm src}.
\]

---

# 10. Ambient vs Source Elimination Comparison

## Ambient

在：

\[
p=(2/7,3/7,6/7),
\qquad
b_1=b_2=1
\]

上：

\[
p_1^2+p_2^2+p_3^2=1.
\]

取：

\[
b_3=XYG(2K-7)+Y(3-7G),
\]

直接代回 normalized master 得恒等 0。

因此有一个显式 rational/algebraic section over a nonempty open subset of \(T_4\)。

所以：

\[
\boxed{
\overline{\pi_{T4}(V(I_{\rm amb}))}^{\,\rm Zar}
=
T_4.
}
\]

于是：

\[
\boxed{
I_{\rm amb}\cap R_T=(0).
}
\tag{ELIM-0}
\]

进一步：

\[
\boxed{
I_{\rm amb}\cap\mathbf Q[G^{\pm1},K^{\pm1}]
=(0).
}
\]

分类：

\[
\boxed{\texttt{K2 — AMBIENT-ONLY / WHOLE-TORUS}.}
\]

## Source

对 actual source image：

\[
\overline{
\pi_{GK}
(
\mathscr Z_{\rm sem}^{\rm src}
)
}^{\,\rm Zar}
\]

本轮**没有证明**是整个 \((\mathbf G_m)^2\)，也没有证明 proper。

因此：

\[
\boxed{
\texttt{DIRECT\_GK\_ZARISKI\_CLOSURE
=
UNKNOWN\_FOR\_ACTUAL\_SOURCE\_IMAGE}.
}
\]

这一区分是 R4 的核心 firewall。

---

# 11. Direct \((G,K)\) Projection

结论：

\[
\boxed{
\text{ambient equality envelope 的 }(G,K)\text{ projection 是 dense}.
}
\]

但不能升级为：

\[
\boxed{
\texttt{DIRECT\_POWER10\_PROJECTION\_DENSE}
}
\]

for the actual source-completed integer image。

原因：source selector可能在 integer points 上产生 algebraic sparsity，而这不由 ambient ideal检测。

所以 direct \((G,K)\) fixed-incidence architecture 的状态是：

```text
AMBIENT_DIRECT_GK_RELATION=NONE
ACTUAL_SOURCE_DIRECT_GK_RELATION=NOT_EXTRACTED
ACTUAL_SOURCE_DIRECT_GK_DENSITY=NOT_PROVED
```

---

# 12. Zariski-Closure Audit

三个层次必须严格区分：

### Z1 — relaxed algebraic total space

\[
\overline{\pi_{T4}(\mathscr Z_{\rm alg})}=T_4.
\]

**PROVED.**

### Z2 — source-completed mixed object

\[
\overline{\pi_{T4}(\mathscr Z_{\rm sem}^{\rm src})}
\]

globally **UNKNOWN**。

### Z3 — cellwise power support

S0–S2 落入 fixed proper character union。

S3/S4 的 raw exponent support：

\[
(G,K,X,Y)
=
(10^g,10^k,10^{g+d},10^{n_3})
\]

的 exponent map具有 full rank 4：

\[
(g,k,d,n_3)
\mapsto
(g,k,g+d,n_3)
\]

对应 matrix determinant \(1\)。

因此 outer **exponent geometry itself** 不产生 Laurent codimension。

这不是 actual solution-density theorem；它只是证明：

\[
\boxed{
\text{S3/S4 的 fixedness 必须来自 master+source arithmetic，
不能来自 exponent bookkeeping alone.}
}
\]

---

# 13. Character-Elimination Attempt

定义 characters：

\[
\chi_{a,b,c,e}
=
G^aK^bX^cY^e.
\]

最重要的 hidden character：

\[
\boxed{
Z_{\rm out}=X/G.
}
\]

cellwise：

\[
S0:\quad G=1,
\]

\[
S1:\quad Z_{\rm out}=1,
\]

\[
S2:\quad Z_{\rm out}\in\{1,10\},
\]

\[
S3:\quad Z_{\rm out}=10^d,\ d\le-1,
\]

\[
S4:\quad Z_{\rm out}=10^d,\ d\ge2.
\]

得到：

\[
\boxed{
(G-1)(X-G)(X-10G)=0
}
\]

on S0–S2。

但 S3/S4 coefficient alphabet：

\[
\{10^d:d\le-1\}\cup\{10^d:d\ge2\}
\]

无限。

因此 Candidate A：

```text
OFF_EXCEPTIONAL_CELLS=SUCCESS
GLOBAL=FAIL_AT_S3_S4
```

---

# 14. Finite-Coefficient Reduction

已证 finite family：

\[
\boxed{
\{G=1,\ X/G=1,\ X/G=10\}
}
\]

cover S0–S2。

global finite coefficient reduction 未证明。

特别：

\[
d\to-\infty
\]

或：

\[
d\to+\infty
\]

不能被 valuation atlas 的 “finite combinatorial type” 错误解释成 finite coefficient value。

所以：

\[
\boxed{
\texttt{FINITE\_COEFFICIENT\_FAMILY
=
YES\_OFF\_S3S4;\ NO\_GLOBAL}.
}
\]

---

# 15. Determinantal Route

把 normalized master 写成：

\[
\begin{pmatrix}
A_1&A_2&A_3
\end{pmatrix}
\begin{pmatrix}
b_1\\b_2\\b_3
\end{pmatrix}=0.
\]

对 generic nonzero row \(A\)，kernel 在 \(\mathbf P^2_b\) 中是：

\[
\mathbf P^1.
\]

所以 existence of a projective denominator vector并不要求 row rank drop。

真正可能产生 rank rigidity 的必须是：

- denominator arithmetic image；
- Smith restrictions；
- source \(U\)-selector；

与这个 kernel 的 intersection。

单独 determinant/rank：

\[
\boxed{
\texttt{DETERMINANTAL\_ROUTE=K2/K4,\ NOT\ A\ FIXED\ RIGIDITY\ CONDITION}.
}
\]

---

# 16. Fixed-Moduli Route

fixed moduli incidence：

\[
\mathcal V_{\rm mod}
\subset
T_4\times Q_{\rm sph}\times\mathbf P^2_b
\]

由 one master equation定义，因此本身 proper。

但是 projection：

\[
\mathcal V_{\rm mod}\to T_4
\]

dominant，generic fibre dimension 3。

所以“fixed moduli variety存在”本身不等于 “power orbit落入 proper subvariety”。

Candidate B verdict：

```text
FIXED_TARGET=YES
FIXED_INCIDENCE=YES
PROPER_IN_FULL_MODULI_TARGET=YES
POWER_TORUS_PROJECTION_PROPER=NO
SOURCE_SECTION_READABLE=NO
VERDICT=INSUFFICIENT
```

---

# 17. Norm/Discriminant Quotient Route

历史 norm/Gaussian对象仍有局部价值，但 R4 只问 canonical fixedness。

审计结果：

1. q=1 norm chart只有在 source completion 后才 source-compatible；
2. q=1 是 S1 的 decoration，不是 cross-cell carrier；
3. norm coefficients仍读 \(G,K\) 及 source-specialized moving data；
4. Gaussian orientation不是 canonical source invariant；
5. 当前没有证明 discriminant/norm class只取有限 coefficient types across S0–S4。

所以 Candidate D：

\[
\boxed{
\texttt{NORM\_DISCRIMINANT\_GLOBAL\_FIXEDNESS=NO}.
}
\]

不复活 prime orientation / conductor。

---

# 18. Cross-Cell Invariant Test

统一 target：

\[
T_4=(\mathbf G_m)^4.
\]

| CELL | INVARIANT | FIXED TARGET | SOURCE ESSENTIAL? | PROPER RELATION | FINITE COEFF | VERDICT |
|---|---|---|---|---|---|---|
| S0 | \(G\) | yes | no | \(G=1\) | yes | fixed ambient cell relation |
| S1 | \(X/G\) | yes | no | \(X/G=1\) | yes | fixed ambient cell relation |
| S2 | \(X/G\) | yes | no | \(X/G\in\{1,10\}\) | yes | fixed finite union |
| S3 | \(X/G\) | yes | not yet | none fixed | no | exceptional |
| S4 | \(X/G\) | yes | not yet | none fixed | no | exceptional |

统一 invariant language已经找到：

\[
\boxed{
G,\quad Z_{\rm out}=X/G.
}
\]

但 source-essential properness仅在 S3/S4 才是未决核心。

---

# 19. Exceptional-Cell Audit

\[
\boxed{
E_{\rm exc}=\{S3,S4\}.
}
\]

它们不是两个未来独立 architecture。

统一写：

\[
\boxed{
\mathcal E_{\rm outer}
=
\left\{
Z_{\rm out}=10^d:
d\in(-\infty,-1]\cup[2,\infty)
\right\}.
}
\]

R5 必须对同一个 outer-depth character：

\[
Z_{\rm out}=X/G
\]

寻找：

- finite source-selected values；
- fixed character relation with \(G,K,Y\)；
- 或 source-semantic arithmetic obstruction。

---

# 20. Properness Proofs

\(V_{\rm pre}\) 由 nonzero Laurent polynomial：

\[
F_{\rm pre}
=
(G-1)(X-G)(X-10G)
\]

定义。

\(F_{\rm pre}\) 显然不是 Laurent ring 中的零元，例如：

\[
(G,X)=(2,3)
\]

给非零值。

所以：

\[
\boxed{
V_{\rm pre}\subsetneq T_4.
}
\]

三个 components：

\[
G=1,
\qquad
X/G=1,
\qquad
X/G=10
\]

都是 proper character cosets。

---

# 21. Fixedness Proofs

\(F_{\rm pre}\) 的 coefficients：

\[
1,\ 10
\]

均 independent of：

- \(g,k,m_2,n_3\)；
- primitive ray；
- Smith basis；
- \(U\)；
- \(J\)；
- q；
- historical chart。

所以：

\[
\boxed{
V_{\rm pre}
\text{ is genuinely fixed.}
}
\]

但它只 cover S0–S2。

outer relation：

\[
X=10^dG
\]

的 coefficient \(10^d\) 无界 moving，因此不能称 fixed finite family。

---

# 22. Source-Preservation Proofs

这里得到一个重要的**negative firewall result**。

对 partial relation：

\[
F_{\rm pre}=0,
\]

删除 \(\kappa_{\rm src}\) 后关系仍成立，因为它只来自 exponent/cell definition。

因此：

\[
\boxed{
\texttt{SOURCE\_COMPLETION\_CAUSES\_PROPERNESS
=
NO\_FOR\_THE\_PARTIAL\_CARRIER}.
}
\]

这正是为什么不能签：

\[
\texttt{SOURCE\_COMPLETED\_FIXED\_PROPER\_INCIDENCE\_EXTRACTED}.
\]

对 S3/S4，source completion是否能把 image从 dense envelope切成 proper仍是 OPEN。

---

# 23. Whole-Torus Component Autopsy

为什么 resultant / Groebner elimination反复会给 whole torus？

不是计算失败，而是 structural freedom：

1. primitive sphere有 2 algebraic dimensions；
2. denominator projective class有 2 dimensions；
3. master只给 1 equation；
4. fixed primitive point后，\(b_3\) 甚至可线性吸收任意 torus state；
5. \(U\) 已从 homogeneous algebraic master中 radial-cancel；
6. 真正 source-selecting conditions是 arithmetic/Archimedean，而不是 ordinary equality rows。

所以：

\[
\boxed{
\texttt{WHOLE\_TORUS\_CAUSE
=
POSITIVE\_DIMENSIONAL\_PRIMITIVE/DENOMINATOR\_MODULI
+
SOURCE\_SELECTOR\_NONALGEBRAICITY}.
}
\]

继续换 resultant 不会改变这一信息类。

---

# 24. Hidden-Fixedness Audit

本轮真正发现的 hidden fixedness不是 norm field，而是：

\[
\boxed{
Z_{\rm out}=X/G.
}
\]

它把五 cells 放进一个统一 character language：

- \(G=1\)；
- \(Z_{\rm out}=1\)；
- \(Z_{\rm out}=10\)；
- \(Z_{\rm out}=10^d\) outer half-lines。

因此历史 “moving coefficient” \(X=10^{m_2}\) 应重新理解为：

\[
\boxed{
X=G\,Z_{\rm out}.
}
\]

R5 的任务不是再消去 \(X\)，而是把 outer \(Z_{\rm out}\) 的无限 semigroup freedom与 source selector collision。

---

# 25. \(\Gamma_{10}\) Eligibility Ladder

全局：

\[
\boxed{
\texttt{GLOBAL\_ARITHMETIC\_ENTRY\_LEVEL=E0}.
}
\]

原因：全部 actual source candidates尚未被压进 fixed proper incidence。

局部 S0–S2：

- fixed proper character cosets已显式得到；
- 形式上达到 E5-type character description；
- 但这些 relation只是 cell/exponent identities，本身容纳无限 powers-of-ten points；
- 不产生 extinction，也不激活新的 global theorem。

因此记录：

```text
GLOBAL=E0
OFF_EXCEPTIONAL_CELLS=EXPLICIT_CHARACTER_COSETS_BUT_TAUTOLOGICAL/NONEXTINGUISHING
```

---

# 26. Laurent Audit

全局不执行 theorem invocation：

```text
FIXED_GLOBAL_V=NO
PROPER_GLOBAL_V=NO
LAURENT_ELIGIBILITY=NO
```

S0–S2 components 已经显式是 translated character subtori/cosets，使用任何一般 torus-intersection theorem都只会重新陈述已经可见的无限 exponent relations。

因此：

\[
\boxed{
\text{R4 不调用 Laurent。}
}
\]

---

# 27. ESS/Subspace Audit

未得到全局 fixed sparse Laurent equation：

\[
\sum_i a_iG^{r_i}K^{s_i}X^{u_i}Y^{v_i}=0
\]

cover S3/S4，且 fixed coefficients finite。

所以：

```text
ESS_ELIGIBILITY=NO
SUBSPACE_THEOREM_ELIGIBILITY=NO
```

partial polynomial \(F_{\rm pre}\) 是完全因式分解的 character-coset equation，且对应 infinite degenerate families，不是 ESS extinction interface。

---

# 28. Unlikely-Intersection Audit

当前 higher-dimensional moduli incidence：

\[
\mathcal V_{\rm mod}
\subset T_4\times\mathcal M_{\rm alg}
\]

对 \(T_4\) dominant，expected codimension并没有投射成 power orbit的 unlikely condition。

所以：

```text
UNLIKELY_INTERSECTION_ELIGIBILITY=NO
ANOMALOUS_ANALYSIS=NOT_REACHED
```

不为了“高级”强行调用该语言。

---

# 29. Translated-Subtorus Search

找到三个 explicit character components：

\[
\boxed{G=1,}
\]

\[
\boxed{X/G=1,}
\]

\[
\boxed{X/G=10.}
\]

其中前两个是 subtori / identity-character fibres，第三个是 translated coset。

对 actual power coordinates：

\[
G=10^g,\quad X=10^{m_2},
\]

它们分别等价于：

\[
g=0,
\qquad
m_2=g,
\qquad
m_2=g+1.
\]

它们完全解释 S0–S2 的 exponent fixedness。

没有在 S3/S4 找到新的 translated-subtorus component。

---

# 30. Failed/Falsified Routes

## F1 — Direct \(G,K\) resultant

ambient elimination ideal为零。

**Verdict:** retired as a source-blind route.

## F2 — Eliminate \(X,Y\) first

会删除真正的 decimal torus coordinates，制造 moving coefficients。

**Verdict:** illegal architecture.

## F3 — Projectivize all denominator data

algebraically legal，但 source absolute denominator scale/digit semantics丢失。

**Verdict:** algebraic envelope only.

## F4 — Eliminate \(U\)

master本来不含 \(U\)；删除后 source selector不留 ordinary polynomial trace。

**Verdict:** source-unsafe.

## F5 — Determinantal rank drop

1×3 master row generic kernel已有 dimension 1。

**Verdict:** no rank rigidity.

## F6 — Finite coefficients from finite atlas

finite combinatorial cell type \(\not\Rightarrow\) finite numerical \(10^d\) coefficient。

**Verdict:** falsified for S3/S4 architecture.

## F7 — q=1 norm as global carrier

只属于 S1 decoration。

**Verdict:** non-global.

---

# 31. Exact Remaining Unknowns

R4 后真正只剩以下 interface：

1. actual source-completed \(\pi_{GK}\) Zariski closure究竟是 whole torus还是 proper？
2. S3/S4 中 source selector是否迫使
   \[
   Z_{\rm out}=X/G
   \]
   进入 finite set？
3. 若不 finite，是否存在 fixed character relation
   \[
   Z_{\rm out}^aG^bK^cY^e=c_0
   \]
   或 fixed sparse Laurent relation？
4. primitive/denominator moduli与 \(\kappa_{\rm src}\) 的 intersection能否产生一个 canonical arithmetic invariant carrier？
5. q=1 congruence能否被解释为一个更一般 outer/source selector mechanism的 specialization？当前没有证据。

最准确的缺口名称：

\[
\boxed{
\texttt{ARITHMETIC\_SOURCE\_SELECTOR\_TO\_FIXED\_CHARACTER\_BRIDGE\_MISSING}.
}
\]

它同时解释：

- 为什么 fixedness只做到 S0–S2；
- 为什么 properness不能 global；
- 为什么 ordinary source-preserving elimination尚未完成。

---

# 32. R4 Terminal Verdict

六个最高问题：

## Q1 — \(\pi_{GK}\) 的 Zariski closure？

\[
\boxed{
\textbf{actual source image: UNKNOWN.}
}
\]

但：

\[
\boxed{
\textbf{ambient algebraic equality envelope: }
(\mathbf G_m)^2.
}
\]

所以 direct resultant不能回答 actual source问题。

## Q2 — moving primitive / Smith data能否 canonical quotient？

\[
\boxed{
\textbf{presentation/gauge 部分可以；genuine primitive ray、denominator arithmetic moduli 不可以有限化。}
}
\]

## Q3 — \(U\) eliminate还是 retain？

\[
\boxed{\textbf{RETAIN}.}
\]

## Q4 — 是否存在 fixed proper rigidity carrier？

\[
\boxed{
\textbf{YES on }S0\cup S1\cup S2,\quad
\textbf{NO GLOBAL CARRIER YET}.
}
\]

## Q5 — \(\Gamma_{10}\) 是否真正进入 arithmetic-geometry regime？

\[
\boxed{
\textbf{GLOBAL: NO (E0).}
}
\]

partial character cosets只重述 cell exponent structure。

## Q6 — 真正缺什么？

\[
\boxed{
\textbf{source-preserving arithmetic elimination from }
\kappa_{\rm src}
\textbf{ to a fixed outer-depth character condition.}
}
\]

即：

\[
\boxed{
\texttt{ARITHMETIC\_SOURCE\_SELECTOR\_TO\_FIXED\_CHARACTER\_BRIDGE\_MISSING}.
}
\]

---

# Machine-readable terminal block

```text
R4_TERMINAL_VERDICT=FIXED_INCIDENCE_EXTRACTED_OFF_EXCEPTIONAL_CELLS

R1_R2_R3_STATE_FROZEN=YES
VALUATION_LAYER_STATUS=SEMANTICALLY_SATURATED_AND_RETIRED

MASTER_SOURCE_OBJECT=CANONICAL_SOURCE_COMPLETED_PRE_J_MASTER_X_KAPPA_SRC
SOURCE_SECTION_STATUS=CANONICAL_RANK_ONE_ARITHMETIC_SELECTOR
CANONICAL_CELL_ATLAS=S0,S1,S2,S3,S4

DIRECT_GK_PROJECTION=AMBIENT_DOMINANT__ACTUAL_SOURCE_UNRESOLVED
DIRECT_GK_ZARISKI_CLOSURE=UNKNOWN_FOR_ACTUAL_SOURCE_IMAGE__GM2_FOR_AMBIENT_EQUALITY_ENVELOPE
DIRECT_GK_PROPER=NOT_PROVED

MOVING_DATA_CLASSES=GAUGE_PRESENTATION;PRIMITIVE_DIRECTION;DENOMINATOR_SMITH_ARITHMETIC;RADIAL_SOURCE_U;POWER_CUT_DEPTH;DERIVED_HISTORICAL
QUOTIENTABLE_DATA=ARBITRARY_BASES;GAUSSIAN_ORIENTATION;DERIVED_COORDINATES;PRIMITIVE_COMMON_SCALE_ALGEBRAICALLY;DENOMINATOR_COMMON_SCALE_ONLY_IN_ALGEBRAIC_ENVELOPE
GENUINE_MOVING_DATA=PRIMITIVE_SPHERE_DIRECTION;DENOMINATOR_PROJECTIVE_ARITHMETIC_CLASS;ABSOLUTE_DENOMINATOR_SCALE;U;OUTER_DEPTH_d;Y_DEPTH

U_POLICY=RETAIN
U_ELIMINATION_SOURCE_SAFE=NO_GLOBAL

CANONICAL_RIGIDITY_CARRIER=T4_POWER_TORUS_WITH_PARTIAL_CHARACTER_COSET_UNION
RIGIDITY_TARGET=T4=(GM)^4_COORDS(G,K,X,Y)
TARGET_DIMENSION=4
TARGET_FIXED=YES
TARGET_PROPER=YES_OFF_S3_S4__NO_GLOBAL_COVER

FIXED_RELATIONS=(G-1)(X-G)(X-10G)=0_ON_S0_S1_S2
CHARACTER_RELATIONS=G=1;X/G=1;X/G=10
FINITE_COEFFICIENT_FAMILY=YES_OFF_S3_S4_{1,10};NO_GLOBAL

SOURCE_COMPLETION_CAUSES_PROPERNESS=NO_FOR_EXTRACTED_PARTIAL_RELATION__OPEN_ON_S3_S4
AMBIENT_COMPARISON=RELAXED_ALGEBRAIC_MASTER_DOMINATES_T4;SOURCE_SELECTOR_NOT_CAPTURED_BY_ORDINARY_EQUALITY_IDEAL

CELL_UNIFORMITY=UNIFIED_T4_CHARACTER_LANGUAGE_ALL_CELLS__PROPER_FINITE_RELATION_ONLY_S0_S1_S2
EXCEPTIONAL_CELLS=S3,S4

LAURENT_ELIGIBILITY=NO_GLOBAL
ESS_ELIGIBILITY=NO
SUBSPACE_THEOREM_ELIGIBILITY=NO
UNLIKELY_INTERSECTION_ELIGIBILITY=NO

TRANSLATED_SUBTORUS_COMPONENTS=G=1;X/G=1;X/G=10
GLOBAL_ARITHMETIC_ENTRY_LEVEL=E0_GLOBAL__EXPLICIT_NONEXTINGUISHING_CHARACTER_COSETS_OFF_EXCEPTIONS

FAILED_EXTRACTION_ROUTES=DIRECT_GK_RESULTANT;ELIMINATE_XY;FULL_DENOMINATOR_PROJECTIVIZATION;U_ELIMINATION;DETERMINANTAL_RANK;GLOBAL_NORM_DISCRIMINANT
RETIRED_AFTER_R4=BRUTE_RESULTANT_ON_GK;SOURCE_BLIND_MODULI_PROJECTION;FINITE_COEFFICIENT_FROM_FINITE_ATLAS;PROJECTIVIZE_U;THEOREM_INVOCATION_BEFORE_GLOBAL_E2

NEW_COMMON_OBSTRUCTION=ARITHMETIC_SOURCE_SELECTOR_TO_FIXED_CHARACTER_BRIDGE_MISSING

R5_ATTACK_TARGET=ROUTE_C_EXCEPTIONAL_FIXEDNESS_REPAIR__UNIFIED_S3_S4_OUTER_DEPTH_CHARACTER_Z=X/G=10^d
```

---

# 33. R5 Single Attack Target

R5 **唯一**允许进入：

\[
\boxed{
\textbf{Route C — Exceptional Fixedness Repair}.
}
\]

不要分成 “S3 战争 / S4 战争”。

统一变量：

\[
\boxed{
Z:=X/G=10^d.
}
\]

唯一目标：

> 从 full master + primitive/Smith canonical quotient + retained \(U\)-source selector 中，证明 outer source candidates 的 \(Z\) 不能沿两条无界 half-rays 自由移动；必须得到 finite \(Z\)-types、fixed character relation，或一个明确证明该 fixedness 不可能的 family-level theorem。

R5 的 success gate应写成：

\[
\boxed{
\texttt{OUTER\_DEPTH\_FIXEDNESS\_REPAIRED}
}
\]

或若严格失败：

\[
\boxed{
\texttt{OUTER\_DEPTH\_FIXEDNESS\_ARCHITECTURE\_FALSIFIED}.
}
\]

只有后者被证明，才允许进入 moving-family arithmetic rigidity。

---

# Global Rigidity Candidate Register

本轮正式审计四个 genuinely different mechanisms：

### Candidate A — Character elimination

- **Success:** S0–S2。
- **Failure:** S3/S4 coefficient \(10^d\) infinite。
- **Verdict:** PARTIAL PROMOTION。

### Candidate B — Fixed moduli

- fixed proper total incidence exists；
- projection to power torus dominant；
- source section unreadable。
- **Verdict:** INSUFFICIENT。

### Candidate C — Determinantal rank

- master row always has projective kernel；
- no generic rank drop。
- **Verdict:** KILLED AS STANDALONE。

### Candidate D — Norm/discriminant quotient

- q=1 source-completed use remains valid；
- no cross-cell finite fixed invariant。
- **Verdict:** LOCAL ONLY / NOT PROMOTED。

---

# Fixedness Shock Checkpoint

```text
Q1_PI_GK_DENSE=AMBIENT_YES__ACTUAL_SOURCE_UNKNOWN
Q2_HIGHER_FIXED_TARGET_FOUND=YES_T4
Q3_QUOTIENTABLE_MOVING_DATA=PRESENTATION_ONLY_PLUS_ALGEBRAIC_SCALES
Q4_U_SAFE_ELIMINATION=NO
Q5_NONZERO_FIXED_LAURENT_RELATION=YES_ONLY_S0_S1_S2
Q6_FINITE_COEFFICIENT_FAMILY=YES_ONLY_S0_S1_S2
Q7_SOURCE_COMPLETION_CAUSES_PROPERNESS=NO_FOR_PARTIAL_RELATION__OPEN_OUTER
Q8_TRANSLATED_SUBTORUS_SIGNAL=YES_G=1_X/G=1_X/G=10
```

---

# Provenance / Status Discipline

Main inherited sources:

- `105_R1_Common_Obstruction_Reconstruction.md`
- `105_R2_Source_Section_Internalization.md`
- `105_R3_Source_Completed_Valuation_Atlas.md`
- `strict_layer_A1_double_euclidean_smith_gcd_terminal_campaign.md`
- `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`
- `strict_layer_unified_exact_lift_campaign(1).md`

External standard algebraic-geometry language used only for the projection/dimension audit:

- Stacks Project, Morphisms of Schemes, dominant morphisms / density;
- Stacks Project, Dimension of fibres, generic fibre dimension on an open set.

The decisive dominance certificate in this report is nevertheless **explicit** (equation (SEC)); it does not depend on a black-box theorem computation.

---

# Computational companion

`105_R4_scripts/verify_r4_fixed_incidence.py` verifies exactly:

1. the primitive point \((2,3,6,7)\) lies on the integer sphere;
2. the normalized section (SEC) annihilates the master identically;
3. the outer exponent map has determinant \(1\);
4. the S0/S1/S2 fixed character relations are algebraically nonzero/proper.

The script is a verification aid. The semantic conclusions about \(\kappa_{\rm src}\), mixed arithmetic, and R5 architecture are not inferred from finite computation.
