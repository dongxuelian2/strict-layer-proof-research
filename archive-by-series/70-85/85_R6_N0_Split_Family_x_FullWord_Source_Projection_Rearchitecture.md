# 85 第六轮阶段报告：Actual \(N_0\) Split-Family × Pre-Radial Full-Word/Common-Scale Source Projection

**文件名：** `85_R6_N0_Split_Family_x_FullWord_Source_Projection_Rearchitecture.md`  
**Scope：** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**主分支：** \(S_R<0,\ g\ge4,\ u>1,\ \ell\ge6,\ q>1\)；regular \(d_A=1\) 为主  
**本轮任务：** 攻击
\[
\mathcal S_{\rm word}^{\rm pre}\longrightarrow \mathfrak P_{\rm pre}
\]
的 source projection，并与 actual \(N_0\)-split outer family 做第一次严格交叉审计。

---

## 0. Executive Summary

R1–R5 的冻结判决保持不变：

```text
R1_R5_CAMPAIGN_VERDICT=
CURRENT_REGULAR_INTERFACE_EXHAUSTED_REARCHITECTURE_REQUIRED
```

本轮没有关闭 J2，也没有关闭新的 regular tail chamber。

但 R6 得到一个明确而重要的 **projection-level result**：

\[
\boxed{
\textbf{最早可证的 genuine source-information loss 是 common radial scale }
\mathcal U
\textbf{ 的整数/coprime incidence，}
}
\]

而不是 R18/R20 的 saturation / conductor / ruling packet。

更精确地，若 primitive/radial state 为 \(\xi\)，其 genuine full-word lift 所需的最后 radial 条件是

\[
\boxed{
\mathcal U_{\rm src}(\xi)
=
\left\{
\mathcal U\in\mathbf Z_{>0}:
\gcd(\mathcal U,V)=1,\;
10^{n_i-1}\le \mathcal U C_i<10^{n_i}
\right\},
}
\]

在 A1 terminal reduction 中最小地可只保留 block \(2,3\)：

\[
\boxed{
\mathcal U\in I_{23}(\xi),\qquad
\gcd(\mathcal U,V)=1.
}
\]

这是一个 genuine arithmetic image condition；ambient radial state 可以满足全部连续 ratio/margin 条件而 \(\mathcal U_{\rm src}(\xi)=\varnothing\)。

与此同时，本轮把 actual \(N_0\) 精确拉回 pre-root base：

\[
\boxed{
N_0
=
4u^2G^2K^2-(GA+1)^2+2
=
2+u^2(2GK-B)(2GK+B),
}
\]

其中

\[
A=2u+1,\qquad B=2G+q,\qquad uq=G+1.
\]

因此：

\[
\boxed{
N_0=N_0(G,K,u,q)
}
\]

完全不读取：

\[
\mathcal U,\quad
C_1,C_2,C_3,\quad
\text{radial content},\quad
\text{full-word lift choice}.
\]

这给出本轮最关键的新定理。

### R6 Fibrewise Orthogonality Theorem

设 \(b=(G,K,u,q)\) 为 outer base，\(\mathcal I_{{\rm pre},b}\) 为该 base 上的 genuine pre-root full-word image fibre。则

\[
\boxed{
(\mathcal F_{\rm split}\cap\mathcal I_{\rm pre})_b
=
\begin{cases}
\mathcal I_{{\rm pre},b},&N_0(b)\text{ split},\\[2mm]
\varnothing,&N_0(b)\text{ nonsplit}.
\end{cases}
}
\]

所以：

\[
\boxed{
\textbf{\(N_0\)-split 对固定 split base 内的 source fibre 没有任何额外 codimension。}
}
\]

它只筛 outer base，不会在一个已经 split 的 fibre 内再筛掉某个 \(\mathcal U\)、某个 primitive ray 或某个 common-scale lift。

这意味着本轮原本希望出现的：

\[
\boxed{
N_0\text{-split}
\Longrightarrow
\mathcal U\equiv b\pmod m
}
\]

或：

\[
\boxed{
N_0\text{-split}
\Longrightarrow
\mathcal U\notin I_{23}
}
\]

在当前 exact pullback 上根本没有变量接口。

因此 R6 的 set-theoretic intersection 不能合法宣布 EMPTY、THIN 或 LARGE：

```text
INTERSECTION_STATUS=UNKNOWN
```

但 architecture 可以合法判死：

```text
N0_SPLIT_FULLWORD_INTERFACE=
INSUFFICIENT_NO_FIBREWISE_COUPLING
```

本轮同时得到一个 live split base：

\[
\boxed{
(g,k,\ell,u,q)=(4,1,7,73,137)
}
\]

且

\[
\boxed{
N_0
=
210999097060001
=
14449385^2+1488076^2.
}
\]

在这个 **同一个 actual split base** 上，可以精确构造：

- 一个通过 regular J2 linear pre-radial source rows、且有合法 common-\(\mathcal U\) 的 state；
- 一个通过同样的 linear rows、但第二/第三 digit windows 对 \(\mathcal U\) 精确不相交的 pseudo-state。

所以 \(N_0\)-split 既不自动制造 common-scale lift，也不自动排除它。

最终：

```text
SOURCE_PROJECTION_REARCHITECTURE=
PARTIAL_SUCCESS_GENUINE_COMMON_SCALE_LOSS_IDENTIFIED

N0_SPLIT_FULLWORD_INTERFACE=
INSUFFICIENT_NO_FIBREWISE_COUPLING

OLD_INTERFACE_REAPPEARED=
NO

R6_SUCCESS_LEVEL=
S2

R6_TERMINAL_VERDICT=
N0_FULLWORD_INTERFACE_INSUFFICIENT
```

J2 仍 OPEN。

---

# 1. R1–R5 Frozen Campaign Verdict

必须继续冻结：

```text
R1_R5_CAMPAIGN_VERDICT=
CURRENT_REGULAR_INTERFACE_EXHAUSTED_REARCHITECTURE_REQUIRED
```

R1–R5 没有产生新的 regular chamber closure。

已退休的 information classes：

1. Euclidean floor/carry；
2. carry alphabet refinement；
3. source-cut as second residual；
4. \(2/5\)-capacity overload；
5. primitive odd-prime allocation；
6. root-factor support allocation；
7. full root-containing sphere algebra as independent second gate；
8. uniform pre-root real-root order collision；
9. signed affine remainder as a new compression mechanism。

R6 不重新使用这些作为 closure engine。

当前 live regular profile 仍为：

\[
\boxed{
J=2,\quad S_R<0,\quad g\ge4,\quad u>1,\quad
\ell\ge6,\quad q>1,\quad d_A=1.
}
\]

---

# 2. Why Root-Local Interface Is Retired

R5 已给出 exact counterexamples，使：

\[
I_{\rm root}\cap I_{\rm src}=\varnothing
\]

不可能成为 uniform theorem。

因此 R6 不对：

\[
Q_{\rm pre}(C_1)=0
\]

继续做：

- root order；
- root factor；
- carry；
- source-cut residual；
- \(2/5\) load；
- odd-prime allocation。

本轮所有 source constraints 必须在 **不假设 exact root** 的情况下定义。

---

# 3. Semantic Firewall：什么叫 “Full-Word Source”？

这里必须先防止一个 semantic loop。

如果把

\[
\mathcal S_{\rm word}
\]

定义成“已经满足 primitive sphere + exact master + all reconstruction + final norm/root compatibility 的完整 original solution”，那么

\[
\mathcal S_{\rm word}\to\mathfrak P_{\rm pre}
\]

的 image characterization 本身就等价于重新解原题。

这会触发：

```text
FULLWORD_IMAGE=SEMANTIC_LOOP
```

因此 R6 合法使用的是：

\[
\boxed{
\mathcal S_{\rm word}^{\rm pre}
}
\]

即 **pre-root word-semantic shell**：

- exact decimal blocks；
- exact concatenation layout；
- common reduced scale；
- block lengths；
- positivity / ordering；
- individual reducedness；
- common-\(V\) gcd profile；
- common-\(\mathcal U\) numerator realization；
- exact master / word synchronization中不使用 final root 的部分；
- J2 exponent relations；

但不把：

\[
Q_{\rm pre}(C_1)=0
\]

或任何已经证明等价于它的 \(C_1\)-containing dependency package 当作 source-image definition 的一部分。

这正是 R5 Pre-Root Independence Firewall 的延续。

---

# 4. Source Projection Graph

本轮最终采用：

\[
\boxed{
\mathcal S_{\rm word}^{\rm pre}
\overset{\sim}{\longrightarrow}
\mathcal S_{\rm common}
\longrightarrow
\mathcal S_{\rm radial}
\longrightarrow
\mathfrak P_{\rm pre}^{\rm sem}
\longrightarrow
\mathfrak P_{\rm pre}^{\rm amb}.
}
\]

其中用户要求的主图是：

\[
\boxed{
\mathcal S_{\rm word}^{\rm pre}
\to
\mathcal S_{\rm common}
\to
\mathcal S_{\rm radial}
\to
\mathfrak P_{\rm pre}.
}
\]

额外写出 semantic/ambient 两层只是为了说明 R18/R20 的 packet 不应被误认成新的 source loss。

---

# 5. Full-Word Source State

采用统一 terminal dictionary：

\[
(P_1,P_2,P_3,Q_0;\mathcal U,V),
\qquad
\gcd(\mathcal U,V)=1.
\]

定义：

\[
g_i:=\gcd(V,P_i),
\qquad
C_i:=\frac{P_i}{g_i},
\qquad
b_i:=\frac{V}{g_i},
\]

于是：

\[
\boxed{
a_i=\mathcal U C_i,
\qquad
b_i=\frac V{g_i}.
}
\]

由 \(g_i=\gcd(V,P_i)\) 得：

\[
\gcd(C_i,b_i)=1.
\]

再由：

\[
\gcd(\mathcal U,V)=1
\]

可得：

\[
\boxed{
\gcd(a_i,b_i)=1.
}
\]

因此 individual reducedness 并不要求新增一个 radial prime-allocation theorem。

对 exact digit lengths \(n_i\)：

\[
\boxed{
10^{n_i-1}\le\mathcal U C_i<10^{n_i}.
}
\]

这是 genuine full-word source image 中真正读取 \(\mathcal U\) 的地方。

---

# 6. Common-Scale Reconstruction Theorem

## Theorem R6-CSRT — Pre-Root Common-Scale Reconstruction

给定一个 primitive/radial pre-root state \(\xi\)，并假设：

1. common-\(V\) gcd profile 已固定；
2. denominator blocks \(b_i=V/g_i\) 具有合法 digit lengths；
3. primitive word/master identities中不使用 final root 的部分成立；
4. \(C_i=P_i/g_i>0\)；
5. ordering / chamber / exponent relations成立。

定义：

\[
U_{\min}(\xi)
=
\max_i
\left\lceil
\frac{10^{n_i-1}}{C_i}
\right\rceil,
\]

\[
U_{\max}(\xi)
=
\min_i
\left\lfloor
\frac{10^{n_i}-1}{C_i}
\right\rfloor.
\]

则 \(\xi\) 有 genuine common-scale full-word lift，当且仅当：

\[
\boxed{
\exists\mathcal U\in
[U_{\min},U_{\max}]\cap\mathbf Z_{>0}
\quad\text{且}\quad
\gcd(\mathcal U,V)=1.
}
\tag{CSRT}
\]

重构为：

\[
\boxed{
a_i=\mathcal U C_i,\qquad b_i=V/g_i.
}
\]

### A1 terminal minimal form

既有 forward reconstruction 已经证明 \(n_1\) 不必作为 terminal radial gate 的独立输入；最小 numerator incidence 可以只读 block \(2,3\)。

定义：

\[
I_{23}(\xi)
=
\left[
\max\left(
\frac{10^{n_2-1}}{C_2},
\frac{10^{n_3-1}}{C_3}
\right),
\;
\min\left(
\frac{10^{n_2}}{C_2},
\frac{10^{n_3}}{C_3}
\right)
\right).
\]

则：

\[
\boxed{
\mathcal U_{\rm src}^{23}(\xi)
=
\{
\mathcal U\in I_{23}\cap\mathbf Z_{>0}:
\gcd(\mathcal U,V)=1
\}.
}
\]

J2 中：

\[
\boxed{
n_2=2g+k,\qquad n_3=g,
}
\]

所以：

\[
\boxed{
\frac{G^2K}{10}\le \mathcal U C_2<G^2K,
\qquad
\frac G{10}\le \mathcal U C_3<G.
}
\tag{J2-U23}
\]

这是真正 root-independent 的 exact source-image test。

---

# 7. Radialization / Saturation Audit

## 7.1 Word \(\to\) Common

在固定 gcd/digit profile 下，full blocks 与：

\[
(P_i,Q_0;\mathcal U,V;g_i)
\]

之间是 exact reconstruction。

本轮没有找到这里的 information loss。

```text
WORD_TO_COMMON=
REVERSIBLE_ON_FIXED_PROFILE
```

## 7.2 Common \(\to\) Radial

当 \(\mathcal U\) 被忘掉，只保留 primitive ray / normalized data 时，合法 source fibre 变成：

\[
\mathcal U_{\rm src}(\xi).
\]

该 fibre 可能为空。

因此：

\[
\boxed{
\textbf{这是本轮第一个被 exact certificate 证明的 genuine source loss。}
}
\]

它不是“大小信息”而是：

\[
\boxed{
\textbf{bounded interval 内存在一个与 \(V\) 互素的正整数。}
}
\]

## 7.3 Radial \(\to\) R18 semantic lattice

65-R18 在 pre-Schur contact coordinates 已经得到 exact source row：

\[
M_0\mid Z+\beta_0 a,
\]

并证明 source-first cyclotomic saturation quotient 为 \(0\)。

所以这里没有一个此前被 saturation 偷掉、现在可以重新发现的 independent congruence。

## 7.4 R18 \(\to\) R20 semantic model

R20 证明：

- semantic row 可以 exact transport；
- integral graph/dilatation model 的整数点恰好是 source packet kernel；
- R15 source model 与 R20 semantic model 之间为 integral isomorphism；
- split rational fibre 上 finite semantic admissibility automatic；
- moving packet \(\mathbf Z/(M_0q^2)\) 是 model-change cokernel，而不是新的 Diophantine obstruction。

因此：

```text
SATURATION_MISSING_CONGRUENCE=
NO_NEW_GENUINE_INVARIANT_FOUND

CONDUCTOR_PACKET_AS_SOURCE_LOSS=
RETIRED
```

---

# 8. Projection Loss Ledger

| Projection | 输入保留 | 输出保留 | 真正忘掉 | Reversible? | fibre | 首次 pseudo-state |
|---|---|---|---|---|---|---|
| \(\mathcal S_{\rm word}^{pre}\to\mathcal S_{\rm common}\) | exact blocks, scale, digit lengths | primitive/common-scale dictionary | 无（固定 profile） | YES | 1 | NO |
| \(\mathcal S_{\rm common}\to\mathcal S_{\rm radial}\) | \(\mathcal U,V,C_i\) | primitive ray, \(V\), gcd profile | **integer \(\mathcal U\), exact location, coprimality** | only if CSRT passes | finite bounded | **YES** |
| \(\mathcal S_{\rm radial}\to\mathfrak P_{\rm pre}^{sem}\) | primitive source data | RCE/lattice/pre-root semantic coords | coordinate content / basis data | semantic model: YES modulo recorded rows | finite/model-change | no new genuine class |
| \(\mathfrak P_{\rm pre}^{sem}\to\mathfrak P_{\rm pre}^{amb}\) | semantic source row | raw ambient state | source row / packet label | NO | ambient enlargement | YES, but **old retired artifact** |

结论：

\[
\boxed{
\text{earliest new actionable loss}
=
\text{common-scale integer/coprime incidence}.
}
\]

---

# 9. Pseudo-State Construction

本轮给出两个层次的 certificate。

## 9.1 Exact primitive A1 radial pseudo-state — PROVED

已有 synchronized primitive state：

\[
(P_1,P_2,P_3,Q_0)
=
(7776,71252,7899,72109)
\]

满足：

\[
7776^2+71252^2+7899^2=72109^2,
\]

且 primitive gcd 为 \(1\)。

取：

\[
V=24,
\qquad
(g_1,g_2,g_3)=(24,4,3),
\]

则：

\[
C_2=17813,\qquad C_3=2633.
\]

formal digit profile：

\[
n_2=2,\qquad n_3=1.
\]

于是：

\[
I_{23}
=
\left[
\frac{10}{17813},
\frac{10}{2633}
\right)
\subset(0,1).
\]

所以：

\[
\boxed{
\mathcal U_{\rm src}^{23}(\xi)=\varnothing.
}
\]

这严格证明：

\[
\boxed{
\mathcal S_{\rm radial}^{\rm ambient}
\supsetneq
\pi(\mathcal S_{\rm common}).
}
\]

它还满足两侧 sharp integer radial margin，但仍没有正整数 \(\mathcal U\)，说明真正的 source invariant 是 exact successor/incidence，而不仅是 margin inequality。

## 9.2 New live-J2 split linear pseudo-state — NEW COMPUTATIONAL/EXACT CERTIFICATE

取：

\[
\boxed{
g=4,\quad G=10000,\quad
k=1,\quad K=10,\quad
\ell=7,
}
\]

\[
\boxed{
u=73,\quad q=137,\quad uq=10001,
\quad A=147,\quad H=5000.
}
\]

此 base 满足当前 live outer restrictions：

\[
g\ge4,\quad u>1,\quad q>1,\quad \ell\ge6.
\]

其：

\[
B=2G+q=20137,
\]

\[
C_-=179863,\qquad C_+=220137,
\]

并且：

\[
\boxed{
N_0
=
2+73^2\cdot179863\cdot220137
=
210999097060001.
}
\]

精确表示：

\[
\boxed{
N_0
=
14449385^2+1488076^2.
}
\]

所以这是一个 **live actual \(N_0\)-split base**。

现在取 negative-J2 linear pre-radial state：

\[
C_3=c=3,\qquad z=1,
\]

\[
h=684559,
\quad
w=49967807,
\quad
m=100620173,
\]

\[
r=3422794781,
\quad
d_2=499678070219,
\]

\[
C_1=5483,
\quad
C_2=3045441,
\quad
T=54457.
\]

exact identities：

\[
C_3=2r-qw=3,
\]

\[
d_2=2ur-w=499678070219,
\]

\[
Ar-w=mH,
\]

\[
GKC_1=AC_2+m=548300000,
\]

\[
uC_2+w=HT=272285000,
\]

\[
2uKC_1=AT+z=8005180.
\]

并且：

\[
\gcd(A,d_2)=1,
\]

所以它位于 regular linear chart。

但 J2 block-2 window 给：

\[
10^8\le\mathcal U\cdot3045441<10^9
\]

即：

\[
33\le\mathcal U\le328.
\]

而 block-3 window 给：

\[
1000\le3\mathcal U<10000
\]

即：

\[
334\le\mathcal U\le3333.
\]

因此：

\[
\boxed{
[33,328]\cap[334,3333]=\varnothing.
}
\]

故：

\[
\boxed{
\mathcal U_{\rm src}^{23}=\varnothing.
}
\]

### Scope firewall

这个 state **没有**被宣称为 exact primitive/sphere survivor。

事实上：

\[
H^2C_1^2+w^2-Td_2
=
-23962604708526834\ne0.
\]

这正是本轮不使用 root/sphere 预筛的纪律。

因此它的合法用途是：

> 证明在一个 actual live \(N_0\)-split base 上，regular J2 linear pre-radial source chart 仍然包含被 common-scale exact image 排除的 pseudo-state。

它不是 J2 solution，也不是 post-sphere Type-II certificate。

---

# 10. Actual \(N_0\)-Split Criterion

## 10.1 Provenance

使用 65-R17 / 85-R1 的 exact \(N_0\)：

\[
N_0
=
4u^2G^2K^2-(GA+1)^2+2.
\]

使用 75-R8 标准化并经 7.15 审计保留的 Gaussian norm criterion：

\[
\boxed{
N_0\text{ split}
\iff
N_0=X^2+Y^2
}
\]

等价于：

\[
\boxed{
v_p(N_0)\equiv0\pmod2
\quad
\forall p\equiv3\pmod4.
}
\]

本轮没有新增外部 theorem。

```text
75_MIGRATION_USED=
GAUSSIAN_NORM_PARITY_DICTIONARY

7_15_AUDITED=
YES

BAD_PRIME_STATUS=
R8 already proves gcd(N0,10*G*u)=1 on the live family

INTEGRAL_COMPATIBILITY=
YES
```

## 10.2 Necessity firewall

85-R1 已把 \(N_0\) Gaussian split 分类为：

```text
TYPE_III_NECESSARY
```

所以：

```text
N0_SPLIT_STATUS=
NECESSARY
```

但它仍只是 source solution 的必要投影，不是 complete state。

---

# 11. \(N_0\) Pullback to Source Variables

由：

\[
A=2u+1,\qquad uq=G+1,
\]

有：

\[
GA+1
=
G(2u+1)+1
=
2Gu+(G+1)
=
u(2G+q).
\]

令：

\[
B:=2G+q.
\]

于是：

\[
\begin{aligned}
N_0
&=
4u^2G^2K^2-u^2B^2+2\\
&=
2+u^2(2GK-B)(2GK+B).
\end{aligned}
\]

即：

\[
\boxed{
N_0
=
\mathcal N(G,K,u,q).
}
\tag{N0-PB}
\]

进一步用：

\[
u=\frac{G+1}{q}
\]

可写成：

\[
\boxed{
\mathcal N(g,k,q)
=
2+
\left(\frac{10^g+1}{q}\right)^2
\Bigl(2\cdot10^{g+k}-(2\cdot10^g+q)\Bigr)
\Bigl(2\cdot10^{g+k}+(2\cdot10^g+q)\Bigr).
}
\]

split pullback 为：

\[
\boxed{
X^2+Y^2=\mathcal N(g,k,q).
}
\tag{SPLIT-PB}
\]

最重要的是：

\[
\boxed{
\frac{\partial\mathcal N}{\partial\mathcal U}
\text{ 在离散语义上根本不存在：
\(\mathcal N\) 不读取 \(\mathcal U\)。}
}
\]

同样它不读取：

\[
C_1,\ C_2,\ C_3,\ T,\ w,\ m,\ r,\ d_2.
\]

因此：

```text
N0_PULLBACK_PROVENANCE=
PRE_ROOT

ROOT_DERIVED=
NO
```

---

# 12. Split × Full-Word Intersection Theorem

令 outer-base projection：

\[
\beta:\mathfrak P_{\rm pre}\to\mathcal B,
\qquad
\beta(\xi)=b=(G,K,u,q).
\]

定义：

\[
s(b)=
\begin{cases}
1,&N_0(b)\text{ split},\\
0,&\text{otherwise}.
\end{cases}
\]

因为：

\[
N_0=N_0\circ\beta,
\]

有：

\[
\mathcal F_{\rm split}
=
\beta^{-1}(\mathcal B_{\rm split}).
\]

于是对每个 fixed base \(b\)：

\[
\boxed{
(\mathcal F_{\rm split}\cap\mathcal I_{\rm pre})_b
=
s(b)\cdot\mathcal I_{{\rm pre},b}.
}
\]

集合语言即：

\[
\boxed{
(\mathcal F_{\rm split}\cap\mathcal I_{\rm pre})_b
=
\begin{cases}
\mathcal I_{{\rm pre},b},
&
b\in\mathcal B_{\rm split},\\[2mm]
\varnothing,
&
b\notin\mathcal B_{\rm split}.
\end{cases}
}
\tag{FIBRE}
\]

### Consequence

在一个已经 split 的 base 上：

\[
\boxed{
\text{split 条件不会删掉任何一个 fibre coordinate。}
}
\]

所以：

\[
\boxed{
\operatorname{codim}_{\rm fibre}
(\text{split}\cap\text{full-word})
-
\operatorname{codim}_{\rm fibre}
(\text{full-word})
=
0.
}
\]

这就是 R6 最重要的 architecture falsification。

---

# 13. Congruence / Divisibility Collision Audit

本轮重点检查了可能的：

\[
\mathcal U\equiv a\pmod m
\]

versus：

\[
N_0\text{-split}
\Longrightarrow
\mathcal U\equiv b\pmod m.
\]

exact pullback 直接表明 split equation：

\[
X^2+Y^2=\mathcal N(g,k,q)
\]

中没有：

\[
\mathcal U.
\]

因此不存在一个从 **split criterion 本身**推出的 common-scale residue。

任何未来若得到：

\[
\mathcal U\bmod m
\]

必须来自另一个 source theorem，而不是 \(N_0\)-split。

所以：

```text
DIRECT_U_CONGRUENCE_COLLISION=
IMPOSSIBLE_AT_CURRENT_PULLBACK

MISSING_CONGRUENCE_FROM_SATURATION=
NOT_FOUND_AND_R18_R20_RETIRE_THIS_ROUTE
```

本轮找到的 lost invariant 是：

\[
\boxed{
\operatorname{next}_V(L)<R
}
\]

型 exact integer/coprime incidence，而不是 residue class。

---

# 14. Source Codimension Ledger

这里同时记录 algebraic freedom 与 arithmetic incidence；两者不能混为一谈。

| Stage | ambient freedoms | source constraints | remaining freedom | codimension gain |
|---|---|---|---|---|
| raw pre-root | outer base \(b=(g,k,q)\) + primitive/source fibre | live J2 restrictions | moving base + moving fibre | baseline |
| \(N_0\)-split | same | one Gaussian-norm predicate on **base only** | split bases + unchanged fibre | base-arithmetic only |
| full-word image | same | common-\(\mathcal U\) integer/coprime incidence + exact word semantics | source-realizable subfibre | genuine arithmetic fibre restriction |
| split \(\cap\) full-word | split base + source fibre | both | **same source fibre as full-word on each split base** | **no extra fibre codim** |
| plus root | not executed | \(Q_{\rm pre}=0\) | — | NOT AUDITED |

因此：

\[
\boxed{
\text{split 与 full-word 的“碰撞收益”在 fixed fibre 上等于 0。}
}
\]

这不等于说 full-word source image 没有 codimension；它有。

它只说明：

\[
\boxed{
N_0\text{-split 没有利用这个 codimension。}
}
\]

---

# 15. Exact Computational Reconnaissance

所有 R6 新计算使用 exact integer arithmetic。

## 15.1 Live split-base scan

在：

\[
4\le g\le8,
\qquad
u>1,\ q>1,
\qquad
\ell\ge6,
\qquad
k=2g-\ell\ge1,
\]

上按 exact factor parity 测试 \(N_0\)-split。

得到 split base 数：

```text
g=4 : 1
g=5 : 5
g=6 : 5
g=7 : 3
g=8 : 3
```

对应 \((g,k,\ell,u,q)\)：

```text
(4,1,7,73,137)

(5,4,6,11,9091)
(5,3,7,11,9091)
(5,1,9,11,9091)
(5,3,7,9091,11)
(5,1,9,9091,11)

(6,2,10,101,9901)
(6,4,8,9901,101)
(6,3,9,9901,101)
(6,2,10,9901,101)
(6,1,11,9901,101)

(7,6,8,11,909091)
(7,3,11,11,909091)
(7,7,7,909091,11)

(8,10,6,5882353,17)
(8,9,7,5882353,17)
(8,8,8,5882353,17)
```

这只是 finite reconnaissance，不是 infinite theorem。

但它有一个明确用途：

\[
\boxed{
\text{actual split 并不只发生在 75 的 \(u=1\) witness；
它已经进入 current live outer base。}
}
\]

## 15.2 Root filter

本轮计算：

```text
ROOT_FILTER_USED=NO
```

没有要求：

\[
Q_{\rm pre}(C_1)=0.
\]

## 15.3 Split test before source lift

pipeline：

```text
outer/pre-radial state
-> N0 exact
-> split test
-> common-scale lift test
-> root NOT USED
```

符合 R6 discipline。

---

# 16. Type-I / II / III / IV Classification

由于本轮禁止 root screening，而 exact full primitive J2 source fibre 没有被全局枚举，因此必须区分 **official type** 与 **linear reconnaissance type**。

## 16.1 Official Type I

\[
\text{split + full pre-root word lift}.
\]

本轮没有证明一个 infinite official Type-I family，也没有证明 official Type I 为空。

```text
OFFICIAL_TYPE_I_STATUS=
UNKNOWN
```

## 16.2 Type II

\[
\text{split + no full-word lift}.
\]

本轮在 generic exact primitive A1 projection 上有严格 pseudo-state；在 live J2 split base 上有 regular **linear pre-radial** Type-II witness。

但因为该 J2 witness 未通过 sphere/root-dependent package，不把它升级成 post-sphere official Type II。

```text
TYPE_II_LINEAR_J2=
EXPLICIT

TYPE_II_POST_SPHERE_J2=
NOT_CLAIMED
```

## 16.3 Type III

\[
\text{nonsplit + full-word lift}.
\]

不是 R6 主目标，未系统分类。

## 16.4 Type IV

\[
\text{neither}.
\]

不是 R6 主目标，未系统分类。

## 16.5 Same-base split independence experiment

在同一个 split base：

\[
(g,k,\ell,u,q)=(4,1,7,73,137)
\]

同一个：

\[
C_3=3,\ z=1,\ h,w,m,r,d_2
\]

下，另取：

\[
C_1=1073,\qquad
C_2=45441,\qquad
T=10657.
\]

此时 common-scale interval 非空；例如：

\[
\boxed{\mathcal U=2201}
\]

满足：

\[
\gcd(2201,V)=1,
\qquad
V=uG(G/2)=3650000000,
\]

且：

\[
a_2=2201\cdot45441=100015641
\]

满足 9-digit window，

\[
a_3=2201\cdot3=6603
\]

满足 4-digit window。

所以在同一个 split base 上：

- 有 linear common-scale lift；
- 也有 linear no-lift pseudo-state。

这对 “split 偏爱 pseudo-state / split 自动排除 source scale” 都构成直接反例。

同样，此 state 也未被宣称为 sphere/root survivor。

---

# 17. Counterexamples and What They Kill

## CE-1 — Ambient radial \(\not\Rightarrow\) common-\(\mathcal U\)

exact synchronized primitive state：

\[
(7776,71252,7899,72109)
\]

有：

\[
I_{23}\subset(0,1).
\]

杀死：

```text
PROJECTION_ALMOST_TRIVIALLY_SURJECTIVE=
FALSE
```

## CE-2 — \(N_0\)-split \(\not\Rightarrow\) common-\(\mathcal U\)

live split base：

\[
(4,1,7,73,137)
\]

上的 linear pseudo-state要求：

\[
\mathcal U\le328
\]

同时：

\[
\mathcal U\ge334.
\]

杀死：

```text
N0_SPLIT_IMPLIES_COMMON_SCALE=
FALSE_AT_LINEAR_PRE_RADIAL_LEVEL
```

## CE-3 — \(N_0\)-split \(\not\Rightarrow\) no common-\(\mathcal U\)

同一 split base 存在：

\[
\mathcal U=2201
\]

的 linear source-scale lift。

杀死：

```text
ALL_SPLIT_LINEAR_STATES_ARE_PSEUDO=
FALSE
```

因此 split 对 common scale 的最准确关系是：

\[
\boxed{
\textbf{fibrewise blind}.
}
\]

---

# 18. Old-Interface Resurrection Audit

## USSPAL

未使用 transverse splitting height chart。

```text
USSPAL_REAPPEARED=
NO
```

## N4-A reverse semantics

未使用 current N4-A coefficient reverse map。

```text
N4A_REAPPEARED=
NO
```

## R18/R20 conductor packet

只用于证明“这里没有新的 lost congruence”，没有把 packet 重新当 obstruction。

```text
CONDUCTOR_PACKET_REACTIVATED=
NO
```

## 65-R19 finite packet automaticity

未把 generic ambient isotropic abundance当 source realization。

```text
FINITE_PACKET_ROUTE_REOPENED=
NO
```

总 verdict：

```text
OLD_INTERFACE_REAPPEARED=
NO
```

---

# 19. Proven vs Computational Claims

## PROVED / FROZEN

1. R1–R5 architecture exhaustion verdict。
2. exact common-\(\mathcal U\) dictionary：
   \[
   a_i=\mathcal U C_i,\quad b_i=V/g_i.
   \]
3. common-scale exact interval/coprime criterion。
4. generic synchronized primitive pseudo-state with \(I_{23}\subset(0,1)\)。
5. R18 source-first saturation has no extra cyclotomic quotient。
6. R20 semantic packet is model-change cokernel / integral semantic model。
7. exact \(N_0(G,K,u,q)\) formula。
8. \(N_0\)-split Gaussian norm criterion from audited 75-R8。
9. \(N_0\)-split is Type-III necessary for source solution。
10. **Fibrewise Orthogonality Theorem**。

## NEW EXACT COMPUTATIONAL CERTIFICATES

1. live split base：
   \[
   (g,k,\ell,u,q)=(4,1,7,73,137).
   \]
2. exact representation：
   \[
   210999097060001=14449385^2+1488076^2.
   \]
3. live split regular linear pseudo-state with disjoint \(\mathcal U\) windows。
4. same-base linear state with legal \(\mathcal U=2201\)。
5. split-base census \(4\le g\le8\)。

## NOT PROVED / NOT CLAIMED

1. \(\mathcal F_{\rm split}\cap\mathcal I_{\rm pre}=\varnothing\)。
2. intersection is thin。
3. intersection is large。
4. infinite official Type-I family。
5. all split witnesses are pseudo-states。
6. J2 closure。
7. regular closure。
8. singular \(d_A>1\) closure。

---

# 20. Intersection Status: EMPTY / THIN / LARGE / UNKNOWN

必须严格区分 **set-theoretic status** 与 **architecture status**。

## Set-theoretic status

本轮没有证明：

\[
\mathcal F_{\rm split}\cap\mathcal I_{\rm pre}
\]

为空、thin 或 large。

所以：

\[
\boxed{
\texttt{INTERSECTION\_STATUS=UNKNOWN}.
}
\]

这不是含糊处理，而是因为：

- split 只筛 base；
- full-word lift筛 fibre；
- 尚未证明所有 split bases 的 fibre 都空；
- 也尚未证明无限多个 split bases 有 genuine full-word fibres。

## Architecture status

但本轮已经证明：

\[
\boxed{
\text{在 fixed split fibre 内没有 split × full-word 的新增 codimension。}
}
\]

因此当前 proposed collision interface 已经失去继续五轮的理由。

```text
N0_SPLIT_FULLWORD_COLLISION=
FAILED_NO_FIBREWISE_COUPLING
```

---

# 21. R6 Terminal Verdict

最终最准确的状态是：

```text
J2_STATUS=
OPEN

REGULAR_J2_STATUS=
OPEN

N0_SPLIT_STATUS=
NECESSARY

SOURCE_PROJECTION_LOSS=
GENUINE_COMMON_SCALE_INTEGER_COPRIME_INCIDENCE

EARLIEST_CERTIFIED_LOSS_POINT=
COMMON_TO_RADIAL_FORGETTING_OF_MATHCAL_U

SATURATION_LOST_CONGRUENCE=
NO_NEW_INVARIANT

N0_PULLBACK=
PRE_ROOT_BASE_ONLY

N0_SPLIT_FULLWORD_INTERFACE=
INSUFFICIENT_NO_FIBREWISE_COUPLING

INTERSECTION_STATUS=
UNKNOWN

SOURCE_PROJECTION_REARCHITECTURE=
PARTIAL_SUCCESS_GENUINE_LOST_SOURCE_INVARIANT_IDENTIFIED

R6_SUCCESS_LEVEL=
S2

OLD_INTERFACE_REAPPEARED=
NO

ROOT_REINSERTION=
NOT_AUTHORIZED

SINGULAR_dA_GT_1=
UNTOUCHED

R6_TERMINAL_VERDICT=
N0_FULLWORD_INTERFACE_INSUFFICIENT
```

这里 S2 的含义是：

\[
\boxed{
\text{建立了 explicit、root-independent 的 full-word/common-scale image criterion。}
}
\]

但没有达到 S3，因为没有把 actual intersection 压成 thin family。

---

# 22. R7 Attack Target

由于：

```text
N0_FULLWORD_INTERFACE_INSUFFICIENT
```

R7 必须禁止继续：

\[
N_0\text{-split}
+
\text{common-}\mathcal U
+
\text{radial source image}
\]

这一组合。

R7 也不得重新回到 R1–R5 的 root-local residual/carry/factor/order classes。

新的 information class 必须满足：

\[
\boxed{
\textbf{它同时读取 outer base 与 primitive/source fibre，}
}
\]

而不是像：

- \(N_0\)：只读 base；
- common-\(\mathcal U\)：主要读 fibre；

这样彼此正交。

建议把 R7 的唯一 acceptance criterion 写成：

> 寻找一个 **pre-root mixed base–primitive invariant**
> \[
> \mathfrak I(G,K,u,q;\xi)
> \]
> 它在 fixed base 上不是常数，且能从 exact full-word/source semantics 独立推出一个 finite/fixed image；再证明 current pre-root survivor落在不相交 image 中。

优先信息来源应是：

- full denominator-word / prefix structure；
- primitive gcd-profile 与 outer decimal base 的 mixed incidence；
- 在 radial decontenting 之前仍然同时含 base 与 primitive coordinate 的 determinant / residue；
- 但不得退化成 \(N_V(I_{23})\)、R18 packet、USSPAL、N4-A 或 root residual。

因此：

```text
R7_ATTACK_TARGET=
PRE_ROOT_MIXED_BASE_PRIMITIVE_SOURCE_INVARIANT

R7_FORBIDDEN=
N0_SPLIT_X_COMMON_U_CONTINUATION;
ROOT_LOCAL_RESIDUAL_REPACKAGING;
USSPAL;
CURRENT_N4A;
CONDUCTOR_PACKET
```

---

# Appendix A — Exact Common-\(\mathcal U\) Formula

对任意两个 terminal numerator blocks \(i,j\)：

\[
I_{ij}
=
\left[
\max\left(
\frac{10^{n_i-1}}{C_i},
\frac{10^{n_j-1}}{C_j}
\right),
\min\left(
\frac{10^{n_i}}{C_i},
\frac{10^{n_j}}{C_j}
\right)
\right).
\]

整数形式：

\[
U_{\min}^{ij}
=
\max\left(
\left\lceil\frac{10^{n_i-1}}{C_i}\right\rceil,
\left\lceil\frac{10^{n_j-1}}{C_j}\right\rceil
\right),
\]

\[
U_{\max}^{ij}
=
\min\left(
\left\lfloor\frac{10^{n_i}-1}{C_i}\right\rfloor,
\left\lfloor\frac{10^{n_j}-1}{C_j}\right\rfloor
\right).
\]

genuine radial lift要求：

\[
U_{\min}^{ij}\le U_{\max}^{ij}
\]

且区间中至少有一个：

\[
\gcd(\mathcal U,V)=1.
\]

这是 exact finite arithmetic predicate。

---

# Appendix B — Projection Loss Is Not a Congruence

R6 原计划优先寻找：

\[
\mathcal U\equiv a\pmod m.
\]

审计结果说明，当前最早的 lost invariant 不是这种形式，而是：

\[
\boxed{
\exists \mathcal U\in[L,R)\cap\mathbf Z_{>0},
\quad
\gcd(\mathcal U,V)=1.
}
\]

它可以进一步写成 coprime successor：

\[
\boxed{
\operatorname{next}_V(L)<R.
}
\]

因此 projection loss 是：

\[
\boxed{
\text{integer incidence / successor condition},
}
\]

而不是 single residue class。

---

# Appendix C — Why No Root Reinsertion

R6 的规则要求：

\[
\mathcal F_{\rm split}\cap\mathcal I_{\rm pre}
\]

先被证明 thin，才能重新加入：

\[
Q_{\rm pre}(C_1)=0.
\]

本轮没有达到 THIN。

所以：

```text
ROOT_REINSERTION_AUDIT=
SKIPPED_BY_RULE

ROOT_USED_AS_FILTER=
NO
```

这保证 R6 没有偷偷退回 R1–R5。

---

# Appendix D — Provenance Anchors

本轮只继承以下已经冻结/审计的结构：

- `85_R1_R5_First_Five_Round_Closure_Checkpoint.md`
- `85_R1_J2_Terminal_Recompression_and_Minimal_Survivor.md`
- `strict_layer_A1_unified_moving_profile_terminal_campaign.md`
- `strict_layer_backward_A1_common_U_pullback_primitive_radial_gluing_campaign.md`
- `A1_J2_NRSEC_Report.md`
- `A1_J2_NRSEC_search.py`
- `J2-65-R17-Cyclotomic-Composition-Report.md`
- `J2-65-R18-Integral-Descent-Commutation-Report.md`
- `J2-65-R20-Semantic-Conductor-Ruling-Report.md`
- `13_R8_terminal_verdict.md`
- `7_15_Audit_Report.md`

没有新 literature migration。

---

# Final One-Line Verdict

\[
\boxed{
\textbf{R6 找到了 genuine full-word projection loss，
但证明了 \(N_0\)-split 在 fixed source fibre 上完全看不见它；
因此当前 \(N_0\)-split × common-scale collision interface 应立即退休。}
}
\]
