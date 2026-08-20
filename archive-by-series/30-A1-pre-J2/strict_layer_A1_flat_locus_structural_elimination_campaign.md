# 三项十进制拼接平方和问题：A1 Flat-Locus Structural Elimination Campaign

**文件名：** `strict_layer_A1_flat_locus_structural_elimination_campaign.md`  
**研究范围：** Strict Layer 正向线，仅研究当前唯一剩余 chamber：\(A_1\)-only。  
**本轮主目标：** 优先判定 \(\mathfrak a=0\) 是否可能；若排除，则立即转入 generic ten-free / valuation synchronization。  
**本轮最终裁决：**

\[
\boxed{\textbf{A1-FL1 — FLAT LOCUS CLOSED}}
\]

并进一步得到

\[
\boxed{\textbf{A1-GS1 — PRIMITIVE DEFECT SYNCHRONIZATION + IMPROVED HEIGHT BOUNDS}.}
\]

---

# 1. Executive Summary

本轮得到 Level 1 结果，而且闭合 flat locus 的机制比预期更短、更结构化。

上一轮冻结的 A1 primitive-profile translation equation 是

\[
\boxed{10^{m_3}\mathfrak a+\mathfrak b=0,}
\]

其中

\[
\mathfrak a
=
 h_1 10^{m_2}(P_1 10^k-Q_0)-Q_0h_2,
\]

\[
\mathfrak b
=
P_2h_2 10^{n_3}-h_3(Q_0-P_3),
\]

且

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

\[
g_i=\gcd(V,P_i),
\qquad
h_i=\frac{L_g}{g_i},
\qquad
L_g=\operatorname{lcm}(g_1,g_2,g_3).
\]

A1 中

\[
k\ge1,
\qquad
m_2\ge1,
\qquad
m_3=n_3+g.
\]

本轮严格证明：

\[
\boxed{\mathfrak a\neq0}
\]

对每一个 admissible A1 primitive state 都成立。

因此由 translation equation 自动有

\[
\boxed{\mathfrak b=-10^{m_3}\mathfrak a\neq0,}
\]

从而

\[
\boxed{\mathcal D_{\rm flat}=\{\mathfrak a=\mathfrak b=0\}=\varnothing.}
\]

这是完整的 flat-locus elimination；不需要 saturated \(L=1\)、tail certificate、square-spacing、旧 Gaussian descent、DD valuation overload 或任何 DD 专属结构。

决定性机制不是单独的 valuation，也不是单独的 \(p\equiv3\pmod4\)；而是一个 **coprime quotient + mod-4 orientation flip**：

1. 假设 \(\mathfrak a=0\)，得到
   \[
   g_2 10^{m_2}(P_1 10^k-Q_0)=g_1Q_0.
   \]
2. primitive sphere 先迫使 \(Q_0\) 为奇数。
3. 写
   \[
   g_1=ca,\qquad g_2=cb,\qquad \gcd(a,b)=1.
   \]
   则
   \[
   b10^{m_2}D=aQ_0,
   \qquad
   D:=P_1 10^k-Q_0>0.
   \]
4. 因 \(Q_0,D,b\) 都为奇数，精确得到
   \[
   v_2(a)=m_2.
   \]
   写
   \[
   a=2^{m_2}a_0,
   \qquad a_0\text{ odd}.
   \]
5. 所有奇素数 \(p\mid a_0\) 都必须满足
   \[
   p\equiv1\pmod4.
   \]
   因而
   \[
   a_0\equiv1\pmod4.
   \]
6. 将 flat equation 除去 \(2^{m_2}\)：
   \[
   b5^{m_2}D=a_0Q_0.
   \]
   又因 \(P_1\) 为偶数且 \(k\ge1\)，有
   \[
   D=P_1 10^k-Q_0\equiv-Q_0\pmod4.
   \]
   所以
   \[
   b\equiv-a_0\equiv3\pmod4.
   \]
7. 于是 \(b\) 必含某个 \(p\equiv3\pmod4\)。但
   \[
   b\mid Q_0,
   \qquad
   b\mid g_2\mid P_2.
   \]
   因而该 \(p\) 同时整除 \(Q_0,P_2\)。primitive sphere 模 \(p\) 给出
   \[
   P_1^2+P_3^2\equiv0\pmod p.
   \]
   因 \(-1\) 在 \(p\equiv3\pmod4\) 下不可为平方，得到
   \[
   p\mid P_1,P_3.
   \]
   于是 \(p\mid P_1,P_2,P_3,Q_0\)，与 primitive gcd 矛盾。

所以 flat locus 被彻底杀死。

更重要的是，flat elimination 后 generic translation 可以换成更干净的 primitive defect 坐标：

\[
\boxed{
\Delta_{12}
:=
g_2 10^{m_2}(P_1 10^k-Q_0)-g_1Q_0,
}
\]

\[
\boxed{
\Delta_3
:=
g_3P_2 10^{n_3}-g_2(Q_0-P_3).
}
\]

则完整 translation equation 精确等价于

\[
\boxed{
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}.}
\tag{GSYNC}
\]

由于 flat 已空：

\[
\boxed{\Delta_{12}\neq0,\qquad \Delta_3\neq0.}
\]

本轮还新证明：所有 exact A1 primitive state 必有

\[
\boxed{P_1 10^k>Q_0.}
\]

并且 universal tail divisibility

\[
\boxed{
10^{n_3}\mid g_1g_2(Q_0-P_3).
}
\]

对两个 defect-sign branch 分别得到：

### Plus-defect branch

若

\[
\Delta_{12}>0,
\qquad
\Delta_3<0,
\]

则

\[
\boxed{10^{n_3}<Q_0,}
\]

以及

\[
\boxed{10^{m_3}<\frac{Q_0^3}{2}.}
\]

### Minus-defect branch

若

\[
\Delta_{12}<0,
\qquad
\Delta_3>0,
\]

则

\[
\boxed{10^{m_2}<Q_0^2,}
\]

\[
\boxed{10^k<1.1Q_0,}
\]

以及

\[
\boxed{10^g<\frac{Q_0^2}{2}.}
\]

特别，所有 A1 exact states 统一满足

\[
\boxed{10^g<\frac{Q_0^3}{2},}
\]

从而上一轮 generic 粗界

\[
10^g<2Q_0^4
\]

被统一改善了一个 \(Q_0\) 次数；在 minus-defect branch 更改善为二次高度。

**本轮状态：Level 1 achieved；A1 尚未整体闭合，但唯一 primitive-profile flat degeneracy 已完全删除。**

---

# 2. Frozen Previous Results

本轮冻结上一轮 A1 moving-core 报告与统一 primitive normalization 中以下输入。

## 2.1 A1 chamber

\[
\boxed{s_3\le0,\qquad s_2+s_3>0.}
\]

定义

\[
g=-s_3=m_3-n_3\ge0,
\]

\[
k=s_2+s_3\ge1.
\]

于是

\[
\boxed{n_2=m_2+g+k,}
\]

\[
\boxed{m_3=n_3+g.}
\]

其中所有 \(m_i,n_i\) 都是正整数 digit lengths，所以特别

\[
\boxed{m_2\ge1,\qquad n_3\ge1.}
\]

## 2.2 Primitive normalization

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

\[
\gcd(U,V)=1,
\qquad
g_i=\gcd(V,P_i),
\qquad
C_i=\frac{P_i}{g_i}.
\]

所以

\[
\boxed{g_i\mid P_i.}
\]

恢复为

\[
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.
\]

本轮 flat proof 实际只用到

\[
g_1\mid P_1,
\qquad
g_2\mid P_2,
\]

而不需要更强的 common-\(V\) gcd-profile semantics。

## 2.3 Primitive-profile master equation

令

\[
L_g=\operatorname{lcm}(g_1,g_2,g_3),
\qquad
h_i=L_g/g_i.
\]

已有

\[
P_1h_1 10^{n_2+n_3}
+P_2h_2 10^{n_3}
+P_3h_3
=
Q_0\left(
 h_1 10^{m_2+m_3}
+h_2 10^{m_3}
+h_3
\right).
\tag{PM}
\]

代入 A1 digit relations 得 translation line。

---

# 3. Exact Definition of \(\mathfrak a,\mathfrak b\)

定义

\[
\boxed{
\mathfrak a
:=
h_1 10^{m_2}(P_1 10^k-Q_0)-Q_0h_2,
}
\tag{A}
\]

\[
\boxed{
\mathfrak b
:=
P_2h_2 10^{n_3}-h_3(Q_0-P_3).
}
\tag{B}
\]

则 (PM) 精确等价于

\[
\boxed{10^{m_3}\mathfrak a+\mathfrak b=0.}
\tag{TL}
\]

所有对象都是整数。

上一轮把

\[
\mathfrak a=\mathfrak b=0
\]

识别为唯一使 coarse primitive master equation 对 \(g\) 完全失明的 flat locus。

本轮证明更强结论：

\[
\boxed{\mathfrak a=0\text{ 本身即不可能}.}
\]

---

# 4. Flat Equation Derivation

从 \(\mathfrak a=0\) 出发：

\[
h_1 10^{m_2}(P_1 10^k-Q_0)=Q_0h_2.
\]

代入

\[
h_1=L_g/g_1,
\qquad
h_2=L_g/g_2
\]

并消去 \(L_g\)，得到

\[
\boxed{
g_2 10^{m_2}(P_1 10^k-Q_0)=g_1Q_0.
}
\tag{F0}
\]

右端为正，因此

\[
\boxed{D:=P_1 10^k-Q_0>0.}
\tag{D+}
\]

于是 flat equation 是

\[
\boxed{g_2 10^{m_2}D=g_1Q_0.}
\tag{F}
\]

**状态：PROVED.**

---

# 5. Equivalent Normal Forms

## 5.1 Ratio form

由 (F)：

\[
P_1 10^k
=
Q_0\left(1+\frac{g_1}{g_2 10^{m_2}}\right).
\]

故

\[
\boxed{
\frac{Q_0}{P_1}
=
\frac{10^k}
{1+\frac{g_1}{g_2 10^{m_2}}}.
}
\]

更有两个 exact gap：

\[
\boxed{
10^k-\frac{Q_0}{P_1}
=
\frac{g_1Q_0}{g_2 10^{m_2}P_1},
}
\]

以及尤其干净的

\[
\boxed{
\frac{P_1}{Q_0}-10^{-k}
=
\frac{g_1}{g_2 10^{m_2+k}}.
}
\tag{R-gap}
\]

所以 flat 并非“模糊接近” \(10^{-k}\)，而是一个完全精确的 rational displacement。

**状态：PROVED.**

## 5.2 Divisibility form

展开 (F)：

\[
\boxed{
g_2P_1 10^{m_2+k}
=
Q_0(g_2 10^{m_2}+g_1).
}
\tag{DIV}
\]

所以

\[
\boxed{Q_0\mid g_2P_1 10^{m_2+k}.}
\]

若记

\[
Q_0^{(10)}
=
\frac{Q_0}{2^{v_2(Q_0)}5^{v_5(Q_0)}},
\]

则

\[
\boxed{Q_0^{(10)}\mid g_2P_1.}
\]

该整除是正确的，但不是最终 decisive form。

**状态：PROVED BUT INSUFFICIENT ALONE.**

## 5.3 Coprime quotient form I: \(Q_0/P_1\)

写

\[
d=\gcd(Q_0,P_1),
\quad
Q_0=dq,
\quad
P_1=dp,
\quad
\gcd(p,q)=1.
\]

则

\[
\boxed{
g_2 10^{m_2}(p10^k-q)=g_1q.}
\tag{CQ1}
\]

从而至少有

\[
q^{(10)}\mid g_2.
\]

但这仍保留了 \(5\)-primary absorption，因此不是最自然的终端 quotient。

## 5.4 Coprime quotient form II: gcd-profile quotient — decisive form

令

\[
\boxed{c=\gcd(g_1,g_2),}
\]

\[
\boxed{g_1=ca,\qquad g_2=cb,\qquad \gcd(a,b)=1.}
\]

则 (F) 精确约成

\[
\boxed{b10^{m_2}D=aQ_0.}
\tag{RF}
\]

又因为

\[
a\mid g_1\mid P_1,
\qquad
b\mid g_2\mid P_2,
\]

得到

\[
\boxed{a\mid P_1,
\qquad
b\mid P_2.}
\tag{ALLOC}
\]

由于 \(\gcd(a,b)=1\)，(RF) 还立即给出

\[
\boxed{b\mid Q_0.}
\tag{BQ}
\]

这就是本轮真正的 decisive normal form：

\[
\boxed{
\text{flat}
\Longrightarrow
\begin{cases}
 b10^{m_2}D=aQ_0,\\
 \gcd(a,b)=1,\\
 a\mid P_1,\\
 b\mid P_2,Q_0.
\end{cases}
}
\]

**状态：NEW PROVED — DECISIVE NORMAL FORM.**

---

# 6. Prime Allocation Analysis

## 6.1 Primitive hypotenuse parity

### Lemma A1-FL-P1

\[
\boxed{Q_0\text{ is odd}.}
\]

### Proof

若 \(Q_0\) 为偶数，则模 \(4\)：

\[
P_1^2+P_2^2+P_3^2\equiv0\pmod4.
\]

平方模 \(4\) 只可能为 \(0,1\)。三个平方之和要为 \(0\pmod4\)，只能三个都为 \(0\)。因此

\[
2\mid P_1,P_2,P_3,Q_0,
\]

违反 primitive gcd。

证毕。

**状态：NEW PROVED in this campaign.**

事实上，进一步有恰好一个 \(P_i\) 为奇数；本轮 flat closure 只需前一结论。

---

## 6.2 Exact \(2\)-adic allocation in reduced flat quotient

由 \(Q_0\) 奇、\(k\ge1\)：

\[
P_1 10^k\text{ even},
\]

所以

\[
D=P_1 10^k-Q_0\text{ odd}.
\]

由 \(b\mid Q_0\)，\(b\) 也为奇数。

在

\[
b10^{m_2}D=aQ_0
\]

两边取 \(v_2\)：

\[
\boxed{v_2(a)=m_2.}
\tag{V2}
\]

故存在奇数 \(a_0\) 使

\[
\boxed{a=2^{m_2}a_0.}
\tag{A0}
\]

因 \(a\mid P_1\) 且 \(m_2\ge1\)，得到

\[
\boxed{2\mid P_1.}
\tag{P1-even}
\]

**状态：NEW PROVED.**

---

## 6.3 Odd-prime support of \(a_0\)

### Lemma A1-FL-P2 — Reduced numerator support

若奇素数

\[
p\mid a_0,
\]

则

\[
\boxed{p\equiv1\pmod4.}
\]

### Proof

若 \(p=5\)，结论显然。

以下设 \(p\ne5\)。

因为

\[
p\mid a,
\qquad
\gcd(a,b)=1,
\]

有 \(p\nmid b\)。又 \(p\ne2,5\)，故

\[
p\nmid b10^{m_2}.
\]

从

\[
b10^{m_2}D=aQ_0
\]

知左侧必须含 \(p\)，所以

\[
p\mid D.
\]

另一方面

\[
p\mid a\mid P_1.
\]

因此

\[
D=P_1 10^k-Q_0\equiv-Q_0\pmod p,
\]

故

\[
p\mid Q_0.
\]

primitive sphere 模 \(p\) 给出

\[
P_2^2+P_3^2\equiv0\pmod p.
\]

若 \(p\equiv3\pmod4\)，则 \(-1\) 是二次非剩余，故只能

\[
p\mid P_2,
\qquad
p\mid P_3.
\]

连同 \(p\mid P_1,Q_0\)，违反 primitive gcd。

所以

\[
p\not\equiv3\pmod4,
\]

而奇素数只有 \(1,3\pmod4\)，故

\[
\boxed{p\equiv1\pmod4.}
\]

证毕。

因此 \(a_0\) 的所有素因子都为 \(1\pmod4\)，从而

\[
\boxed{a_0\equiv1\pmod4.}
\tag{A0mod4}
\]

**状态：NEW PROVED.**

这一步实际上在整个 flat problem 中重新导出了一个全局的 non-decimal \(1\bmod4\) support restriction，而且不需要调用旧 saturated A1 theorem。

---

# 7. Primitive Sphere Interaction — Flat Locus Elimination

将

\[
b10^{m_2}D=aQ_0
\]

代入 \(a=2^{m_2}a_0\)，除以 \(2^{m_2}\)：

\[
\boxed{b5^{m_2}D=a_0Q_0.}
\tag{RF'}
\]

因为 \(P_1\) 已证为偶数，且 \(k\ge1\)，

\[
P_1 10^k
\]

至少含 \(2^2\)，所以

\[
P_1 10^k\equiv0\pmod4.
\]

因此

\[
\boxed{D\equiv-Q_0\pmod4.}
\tag{Dmod4}
\]

又

\[
5^{m_2}\equiv1\pmod4.
\]

将 (RF') 模 \(4\)：

\[
b(-Q_0)\equiv a_0Q_0\pmod4.
\]

因 \(Q_0\) 为奇数，可在模 \(4\) 中约掉：

\[
\boxed{b\equiv-a_0\pmod4.}
\]

由 \(a_0\equiv1\pmod4\)：

\[
\boxed{b\equiv3\pmod4.}
\tag{Bmod4}
\]

所以 \(b\) 的素因子分解中必存在至少一个

\[
\boxed{p\equiv3\pmod4}
\]

以奇指数出现。

但 (BQ)+(ALLOC) 给出

\[
p\mid b\mid Q_0,
\qquad
p\mid b\mid P_2.
\]

sphere 模 \(p\)：

\[
P_1^2+P_3^2\equiv0\pmod p.
\]

由于 \(p\equiv3\pmod4\)，再次由 \(-1\) 不可平方，得到

\[
p\mid P_1,
\qquad
p\mid P_3.
\]

于是

\[
p\mid P_1,P_2,P_3,Q_0,
\]

违反

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

因此假设 \(\mathfrak a=0\) 不可能。

---

## Theorem A1-FL — Flat Coefficient Elimination

对任意 admissible A1 primitive state，

\[
\boxed{\mathfrak a\neq0.}
\]

进而由

\[
10^{m_3}\mathfrak a+\mathfrak b=0
\]

有

\[
\boxed{\mathfrak b\neq0.}
\]

所以

\[
\boxed{
\mathcal D_{\rm flat}
=
\{\mathfrak a=\mathfrak b=0\}
=
\varnothing.
}
\]

**状态：NEW PROVED — LEVEL 1 ACHIEVED.**

---

# 8. What the Proof Actually Uses

flat elimination 的依赖极小。

真正使用的只有：

1. primitive sphere
   \[
   P_1^2+P_2^2+P_3^2=Q_0^2,
   \quad
   \gcd(P_1,P_2,P_3,Q_0)=1;
   \]
2. A1 中
   \[
   k\ge1,
   \quad
   m_2\ge1;
   \]
3. gcd-profile 的最弱后果
   \[
   g_1\mid P_1,
   \quad
   g_2\mid P_2;
   \]
4. flat equation本身。

没有使用：

- \(\mathfrak b=0\)；
- \(n_3,g,m_3\)；
- saturated / nonsaturated split；
- tail certificate；
- exact word cut；
- square gate；
- DD 的任何专属 theorem；
- 旧 saturated odd-prime support theorem。

因此本 theorem 比“完整 flat locus 不存在”更强：

\[
\boxed{
\text{primitive sphere 上连第一条 flat coefficient equation 都无法成立。}
}
\]

---

# 9. Archimedean Ratio Geometry

flat ratio identity

\[
\frac{P_1}{Q_0}
=
10^{-k}
+
\frac{g_1}{g_2 10^{m_2+k}}
\]

确实把 primitive sphere point 限制在靠近第一坐标轴的薄 slice 上。

但本轮证明显示：

\[
\boxed{
\text{真正 decisive 的不是 slice 的 Archimedean 薄度，而是其 reduced divisor orientation。}
}
\]

单纯比较

\[
\frac{Q_0}{P_1}
=
\sqrt{1+(P_2/P_1)^2+(P_3/P_1)^2}
\]

与 decimal rational family，并没有直接给出统一 gap lower bound；gcd profile 可以让 rational perturbation 很小。

因此：

\[
\boxed{\text{ratio approximation alone — INSUFFICIENT.}}
\]

但 exact ratio form 对发现 reduced quotient \((a,b)\) 有辅助价值。

---

# 10. \((2,5)\)-adic Budget

本轮 valuation 路线有一个明确结论：

\[
\boxed{v_2(a)=m_2.}
\]

这是 exact budget，不只是 inequality。

但若只停在

\[
m_2\le v_2(g_1Q_0)
\]

之类粗式，无法闭合 flat。

决定性升级是：

\[
\boxed{
\text{exact }2\text{-adic extraction}
+
\text{odd support }1\bmod4
+
\text{mod-}4\text{ orientation flip}
}
\]

共同给出

\[
b\equiv3\pmod4.
\]

所以本轮对 “pure valuation” 的裁决是：

\[
\boxed{\text{FAILED AS A STANDALONE ROUTE, SUCCESSFUL AS ONE COMPONENT OF THE MOD-4 PROOF}.}
\]

\(5\)-adic 深度在 flat closure 中完全不需要单独追逐；\(5\equiv1\pmod4\) 正好被吸收进 \(a_0\) 的 split-prime support。

---

# 11. A1 Decimal Inequalities

本轮最意外的结果之一是：完整 A1 digit inequalities 几乎没有被调用。

flat contradiction 只需要：

\[
\boxed{k\ge1,\qquad m_2\ge1.}
\]

也就是说，之前 flat locus 中已知的

\[
10^{m_2}<Q_0^2,
\quad
10^{n_3}<Q_0,
\quad
10^k\le1.1Q_0
\]

现在都不再是 flat closure 的必要输入；它们成为被更强 theorem supersede 的中间界。

**状态：SUPERSEDED FOR FLAT CLOSURE.**

---

# 12. Computational Experiments

本轮计算只用于结构发现与 falsification，不参与证明。

## 12.1 Restricted primitive scan

对所有正 ordered primitive sphere triples

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
Q_0\le300
\]

共枚举到

\[
\boxed{18270}
\]

个 ordered primitive directions。

对

\[
m_2,k\in\{1,2,3\}
\]

定义 flat 必需 ratio

\[
\frac ab
=
\frac{10^{m_2}(P_1 10^k-Q_0)}{Q_0}
\]

并约为最简分数。

必要条件是

\[
a\mid P_1,
\qquad
b\mid P_2.
\]

实验发现：

- 有 \(32\) 个 state 满足 numerator-side \(a\mid P_1\)；
- 这 \(32\) 个 state 全部满足
  \[
  b\equiv3\pmod4;
  \]
- 没有一个同时满足
  \[
  b\mid P_2.
  \]

即 restricted scan 中 flat hit 数为

\[
\boxed{0.}
\]

这正是后来 theorem 中

\[
a_0\equiv1\pmod4
\Longrightarrow
b\equiv3\pmod4
\]

的实验影子。

**状态：EXPERIMENTAL; not used in proof.**

## 12.2 Weakened nonprimitive toy counterexample

为了确认 primitive gcd 是真实关键，而不是 flat equation 在整数层面根本无解，可看弱化 toy system：

\[
(P_1,P_2,P_3,Q_0)=(30,42,219,225),
\]

满足

\[
30^2+42^2+219^2=225^2,
\]

但

\[
\gcd(30,42,219,225)=3.
\]

取

\[
m_2=k=1,
\qquad
D=30\cdot10-225=75,
\]

\[
g_1=10,
\qquad
g_2=3.
\]

则

\[
3\cdot10\cdot75
=
10\cdot225,
\]

并且

\[
g_1\mid P_1,
\qquad
g_2\mid P_2.
\]

所以在删除 primitive gcd、且只保留 divisibility semantics 的弱 toy model 中，flat equation 确实可以成立。

注意：这个 toy **没有**声称存在一个共同 \(V\) 使

\[
g_i=\gcd(V,P_i)
\]

同时成立；它只用于说明 primitive condition 不是装饰性假设。

**状态：PROVED WEAKENED-TOY COUNTEREXAMPLE.**

---

# 13. Split Resonance Analysis

上一轮若再加入 \(\mathfrak b=0\)，会得到 split resonance：

\[
a_1 10^{m_2+k}=\mathcal RQ_{12},
\]

\[
a_2 10^{n_3}+a_3=\mathcal Rb_3.
\]

本轮按照优先级先攻击 \(\mathfrak a=0\)。

由于已经严格证明

\[
\boxed{\mathfrak a=0\text{ impossible},}
\]

所以完整 split resonance 自动不存在。

因此本轮**没有继续浪费 token**研究 common rational scale / common slope / common norm 的双 resonance 解释。

**状态：OBSOLETE AFTER STRONGER THEOREM.**

---

# 14. New Proven Lemmas — Flat Phase

汇总本轮 flat phase 的新 theorem：

### A1-FL-P1 — Primitive hypotenuse oddness

\[
\boxed{Q_0\text{ odd}.}
\]

### A1-FL-P2 — Reduced flat divisor normal form

若 \(\mathfrak a=0\)，则存在 \(a,b,c\in\mathbf Z_{>0}\)：

\[
g_1=ca,
\quad
g_2=cb,
\quad
\gcd(a,b)=1,
\]

并且

\[
\boxed{b10^{m_2}D=aQ_0,}
\]

\[
\boxed{a\mid P_1,
\quad
b\mid P_2,Q_0.}
\]

### A1-FL-P3 — Exact two-adic numerator extraction

\[
\boxed{a=2^{m_2}a_0,
\quad
a_0\text{ odd}.}
\]

### A1-FL-P4 — Odd support theorem

\[
\boxed{p\mid a_0\Longrightarrow p\equiv1\pmod4.}
\]

因而

\[
\boxed{a_0\equiv1\pmod4.}
\]

### A1-FL-P5 — Reduced denominator orientation

\[
\boxed{b\equiv3\pmod4.}
\]

### A1-FL-P6 — Primitive contradiction

\[
\boxed{b\equiv3\pmod4,
\ b\mid Q_0,P_2
\Longrightarrow
\gcd(P_1,P_2,P_3,Q_0)>1.}
\]

### A1-FL — Flat coefficient elimination

\[
\boxed{\mathfrak a\neq0.}
\]

故

\[
\boxed{\mathcal D_{\rm flat}=\varnothing.}
\]

全部状态：**NEW PROVED.**

---

# 15. Generic Synchronization After Flat Elimination

flat locus 关闭后，整个 A1-only chamber 无条件进入

\[
\boxed{\mathfrak b=-10^{m_3}\mathfrak a,
\qquad
\mathfrak a\ne0.}
\]

本节把上一轮的 ten-free coefficient synchronization进一步压到 primitive integer defects。

## 15.1 Primitive defect coordinates

定义

\[
\boxed{
\Delta_{12}
:=
g_2 10^{m_2}(P_1 10^k-Q_0)-g_1Q_0,
}
\tag{Def12}
\]

\[
\boxed{
\Delta_3
:=
g_3P_2 10^{n_3}-g_2(Q_0-P_3).
}
\tag{Def3}
\]

因为

\[
\mathfrak a
=
\frac{L_g}{g_1g_2}\Delta_{12},
\]

\[
\mathfrak b
=
\frac{L_g}{g_2g_3}\Delta_3,
\]

translation equation 等价于

\[
\boxed{
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}.}
\tag{GSYNC}
\]

flat elimination 给出

\[
\boxed{\Delta_{12}\neq0,\qquad\Delta_3\neq0.}
\]

**状态：NEW PROVED NORMAL FORM.**

该形式比

\[
\operatorname{core}_{10}(\mathfrak a)
=
\operatorname{core}_{10}(\mathfrak b)
\]

更原始，因为 common \(L_g/g_2\) normalization 已被完全消掉。

---

## 15.2 Universal positive first defect geometry

定义

\[
D=P_1 10^k-Q_0.
\]

### Theorem A1-GS-P1

对每一个 exact A1 primitive state，

\[
\boxed{D>0.}
\]

### Proof

假设 \(D\le0\)。则

\[
\Delta_{12}
=
g_2 10^{m_2}D-g_1Q_0
\le
-g_1Q_0<0.
\]

由 (GSYNC)：

\[
g_1\Delta_3
=
-10^{m_3}g_3\Delta_{12}
\ge
10^{m_3}g_3g_1Q_0,
\]

所以

\[
\Delta_3\ge10^{m_3}g_3Q_0.
\]

另一方面

\[
\Delta_3
=
g_3P_2 10^{n_3}-g_2(Q_0-P_3)
<
g_3P_2 10^{n_3},
\]

因为 \(Q_0>P_3\)。

因此

\[
P_2 10^{n_3}
>
Q_0 10^{m_3}.
\]

又

\[
m_3=n_3+g,
\]

故

\[
P_2>Q_0 10^g\ge Q_0,
\]

与 \(P_2<Q_0\) 矛盾。

所以

\[
\boxed{P_1 10^k>Q_0.}
\]

证毕。

**状态：NEW PROVED.**

这说明上一轮 flat phase 中出现的“near-axis orientation”并不是 flat 专属，而是完整 A1 的 universal geometric orientation。

---

## 15.3 Universal tail divisibility

由 (GSYNC)：

\[
10^{m_3}\mid g_1\Delta_3.
\]

因为

\[
m_3=n_3+g\ge n_3,
\]

所以

\[
10^{n_3}\mid g_1\Delta_3.
\]

而

\[
g_1\Delta_3
=
g_1g_3P_2 10^{n_3}
-g_1g_2(Q_0-P_3).
\]

第一项已被 \(10^{n_3}\) 整除，因此

\[
\boxed{
10^{n_3}
\mid
g_1g_2(Q_0-P_3).
}
\tag{TAIL-P}
\]

**状态：NEW PROVED.**

从

\[
g_1g_2\le P_1P_2
\le
\frac{P_1^2+P_2^2}{2}
<
\frac{Q_0^2}{2}
\]

及

\[
Q_0-P_3<Q_0
\]

得

\[
\boxed{
10^{n_3}<\frac{Q_0^3}{2}.
}
\tag{n3-global}
\]

即

\[
\boxed{
n_3<3\log_{10}Q_0-\log_{10}2.
}
\]

这是一个不区分 saturated branch 的 primitive-profile tail capacity bound。

---

## 15.4 Defect sign dichotomy

因为

\[
D>0,
\qquad
\Delta_{12}\ne0,
\qquad
\Delta_3\ne0,
\]

由 (GSYNC) 只有两个 branch：

\[
\boxed{
\Delta_{12}>0
\iff
\Delta_3<0,
}
\]

或

\[
\boxed{
\Delta_{12}<0
\iff
\Delta_3>0.
}
\]

这给 A1 一个比 flat/generic 二分更细的 universal orientation。

---

# 16. Generic Height Compression by Defect Sign

## 16.1 Plus-defect branch

假设

\[
\Delta_{12}>0,
\qquad
\Delta_3<0.
\]

由

\[
-\Delta_3
=
g_2(Q_0-P_3)-g_3P_2 10^{n_3}>0
\]

先得到

\[
g_3P_2 10^{n_3}
<
g_2(Q_0-P_3).
\]

由于

\[
g_2\le P_2,
\qquad
g_3\ge1,
\]

有

\[
\boxed{10^{n_3}<Q_0-P_3<Q_0.}
\tag{PLUS-n}
\]

再由 (GSYNC)：

\[
10^{m_3}g_3\Delta_{12}
=
g_1(-\Delta_3)
<
g_1g_2(Q_0-P_3).
\]

因为 \(\Delta_{12}\ge1\)：

\[
10^{m_3}
<
\frac{g_1g_2(Q_0-P_3)}{g_3}
\le
P_1P_2(Q_0-P_3).
\]

而

\[
P_1P_2
\le
\frac{P_1^2+P_2^2}{2}
<
\frac{Q_0^2}{2},
\]

故

\[
\boxed{
10^{m_3}<\frac{Q_0^3}{2}.
}
\tag{PLUS-M}
\]

因此 plus branch 中整个 third-denominator length 已被三次 primitive height 控制。

**状态：NEW PROVED.**

---

## 16.2 Minus-defect branch

假设

\[
\Delta_{12}<0,
\qquad
\Delta_3>0.
\]

首先

\[
g_2 10^{m_2}D<g_1Q_0.
\]

因 \(D\ge1\)：

\[
10^{m_2}
<
\frac{g_1Q_0}{g_2}
\le
P_1Q_0
<
Q_0^2.
\]

所以

\[
\boxed{10^{m_2}<Q_0^2.}
\tag{MINUS-m2}
\]

进一步

\[
D
<
\frac{g_1Q_0}{g_2 10^{m_2}}
\le
\frac{P_1Q_0}{10^{m_2}}.
\]

由

\[
P_1 10^k=Q_0+D
\]

得

\[
10^k
<
\frac{Q_0}{P_1}
+
\frac{Q_0}{10^{m_2}}
\le
Q_0+\frac{Q_0}{10}
=1.1Q_0.
\]

即

\[
\boxed{10^k<1.1Q_0.}
\tag{MINUS-k}
\]

最后由 (GSYNC)：

\[
10^{m_3}g_3(-\Delta_{12})
=
g_1\Delta_3
<
g_1g_3P_2 10^{n_3}.
\]

约去 \(g_3 10^{n_3}\)，并用 \(-\Delta_{12}\ge1\)：

\[
\boxed{
10^g<g_1P_2\le P_1P_2<\frac{Q_0^2}{2}.
}
\tag{MINUS-g}
\]

**状态：NEW PROVED.**

这把上一轮统一 generic bound

\[
10^g<2Q_0^4
\]

在 minus branch 直接改善为

\[
\boxed{10^g<Q_0^2/2.}
\]

---

## 16.3 Universal improved \(g\)-bound

plus branch 中

\[
10^g<10^{m_3}<Q_0^3/2.
\]

minus branch 更有

\[
10^g<Q_0^2/2.
\]

所以所有 exact A1 primitive states 统一满足

\[
\boxed{
10^g<\frac{Q_0^3}{2}.
}
\]

即

\[
\boxed{
g<3\log_{10}Q_0-\log_{10}2.}
\tag{g-global-new}
\]

**状态：NEW PROVED.**

---

# 17. Generic Ten-Free Synchronization

从

\[
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}
\]

对任意素数 \(p\ne2,5\)：

\[
\boxed{
 v_p(g_1)+v_p(\Delta_3)
 =
 v_p(g_3)+v_p(\Delta_{12}).
}
\tag{TF-p}
\]

而对 \(p=2,5\)：

\[
\boxed{
 v_p(g_1)+v_p(\Delta_3)
 =
 m_3+v_p(g_3)+v_p(\Delta_{12}).
}
\tag{DEC-p}
\]

所以若定义

\[
\operatorname{core}_{10}(N)
=
\frac{|N|}{2^{v_2(N)}5^{v_5(N)}},
\]

则

\[
\boxed{
\operatorname{core}_{10}(g_1\Delta_3)
=
\operatorname{core}_{10}(g_3\Delta_{12}).
}
\tag{TF-core}
\]

并且 \(2\)-adic 与 \(5\)-adic 的 valuation gap 必须完全相同：

\[
\boxed{
\bigl[v_2(g_1\Delta_3)-v_2(g_3\Delta_{12})\bigr]
=
\bigl[v_5(g_1\Delta_3)-v_5(g_3\Delta_{12})\bigr]
=m_3.
}
\]

这就是 generic A1 的 primitive defect version of ten-free synchronization。

### Cross-defect allocation

再写

\[
d=\gcd(g_1,g_3),
\qquad
g_1=dr_1,
\qquad
g_3=dr_3,
\qquad
\gcd(r_1,r_3)=1.
\]

则

\[
\boxed{r_1\Delta_3=-10^{m_3}r_3\Delta_{12}.}
\]

因此：

- \(r_3\mid\Delta_3\)；
- \(r_1^{(10)}\mid\Delta_{12}\)，其中 \(r_1^{(10)}\) 是去掉 \(2,5\) 的部分；
- 任一 nondecimal prime 在 \(r_1,r_3\) 的不对称 support 必须跨越到另一侧 defect 中补偿。

**状态：NEW PROVED NECESSARY SYNCHRONIZATION; not yet a contradiction.**

---

# 18. Failed Routes

本轮实际尝试并裁决如下。

## 18.1 Pure \(p\equiv3\pmod4\)

**结论：INSUFFICIENT ALONE.**

仅说“出现 \(3\bmod4\) prime 会矛盾”是错的；必须先由 reduced quotient + exact \(2\)-adic extraction + mod-4 orientation **强迫** reduced denominator

\[
b\equiv3\pmod4.
\]

真正 decisive 的是“forced inert prime”，不是 inert-prime existence 本身。

## 18.2 Pure valuation

**结论：INSUFFICIENT ALONE.**

粗预算

\[
m_2\le v_2(g_1Q_0)
\]

之类不足。

有效的是 exact identity

\[
v_2(a)=m_2
\]

再与 odd-prime support 及模 \(4\) 联立。

## 18.3 Ratio approximation

**结论：INSUFFICIENT AS ARCHIMEDEAN CLOSURE.**

虽然 exact gap

\[
\frac{P_1}{Q_0}-10^{-k}
=
\frac{g_1}{g_2 10^{m_2+k}}
\]

非常干净，但单纯 rational approximation / spherical cap spacing 没有提供 uniform contradiction。

## 18.4 Sum of two squares

**结论：INSUFFICIENT STANDALONE; USED LOCALLY.**

\(P_2^2+P_3^2\equiv0\pmod p\) 只有在已经知道 \(p\equiv3\pmod4\) 且 \(p\mid Q_0,P_1\) 时才 decisive。

## 18.5 Sphere parametrization

**结论：NOT NEEDED FOR PROOF.**

参数化与 brute force 对发现 mod-4 pattern 有帮助，但最终 theorem 完全 elementary，不需要全参数化 primitive 3-sphere points。

## 18.6 Direct gcd / divisor allocation

**结论：STRONG BUT INSUFFICIENT UNTIL MOD-4 STEP.**

\[
Q_0^{(10)}\mid g_2P_1
\]

与逐 prime allocation 本身允许大量 \(1\bmod4\) prime。

真正强的 quotient 是

\[
g_1=ca,
\quad
g_2=cb,
\quad
\gcd(a,b)=1,
\quad
b\mid Q_0,P_2.
\]

## 18.7 Square-spacing

**结论：NOT NEEDED FOR FLAT CLOSURE.**

上一轮已经证明 bare \(g\)-large square-spacing 不足。flat elimination 完全绕开该路线；generic square gate 仍可保留为 auxiliary death test。

## 18.8 Old saturated support restriction

**结论：NOT NEEDED.**

旧 saturated theorem 中 nondecimal odd primes 的 \(1\bmod4\) restriction 与本轮机制方向一致，但本轮在 flat assumption 下自行从 primitive sphere 推出 \(a_0\) 的 \(1\bmod4\) support，而且适用范围不依赖 saturated \(L=1\)。

## 18.9 Brute force pattern

**结论：EXPERIMENTAL ONLY.**

零 hit 不作为 theorem。计算真正的价值是暴露了：

\[
\boxed{\text{numerator divisor test surviving时，reduced denominator 总落在 }3\bmod4.}
\]

随后该 pattern 被完全理论化。

---

# 19. False Conjectures vs Insufficient Theorems

必须区分两类失败。

## FALSE / TOO STRONG

以下形式不应再追：

\[
\boxed{
\mathfrak a=0
\Longrightarrow
Q_0^{(10)}\mid P_1,P_2
}
\]

过强。prime allocation 原则上可以在 \(P_1,P_2\) 间分裂；真正 contradiction 来自 reduced denominator 的 mod-4 class，而非把整个 \(Q_0^{(10)}\) 同时压进两个坐标。

同样，没有 theorem 说明 primitive sphere 上任意

\[
p\mid Q_0,P_i
\]

都会强迫全部坐标被 \(p\) 整除；这只在 \(p\equiv3\pmod4\) 且剩余两平方相加为零时成立。

## TRUE BUT INSUFFICIENT

以下均正确但单独不闭合：

\[
Q_0^{(10)}\mid g_2P_1,
\]

\[
q^{(10)}\mid g_2
\]

for \(q=Q_0/\gcd(Q_0,P_1)\)，以及各种粗 valuation budget、ratio closeness、spherical cap thinness。

---

# 20. Status of \(\mathfrak a=0\)

最终状态：

\[
\boxed{\textbf{PROVED IMPOSSIBLE}.}
\]

因此：

\[
\boxed{
\mathfrak a\neq0
\quad\text{for every admissible A1 primitive state}.
}
\]

以及

\[
\boxed{
\mathcal D_{\rm flat}=\varnothing.
}
\]

用户要求的 Level 1 已达到。

---

# 21. Generic Synchronization Work Reached

flat locus 删除以后，A1 frontier 不再需要“flat vs generic”二分。

新的统一状态是：

\[
\boxed{
\begin{gathered}
P_1 10^k>Q_0,\\
\Delta_{12}\neq0,\\
\Delta_3\neq0,\\
g_1\Delta_3=-10^{m_3}g_3\Delta_{12},\\
10^{n_3}\mid g_1g_2(Q_0-P_3).
\end{gathered}
}
\]

再按 defect sign 二分：

\[
\boxed{
\Delta_{12}>0
\Rightarrow
10^{n_3}<Q_0,
\quad
10^{m_3}<Q_0^3/2,
}
\]

\[
\boxed{
\Delta_{12}<0
\Rightarrow
10^{m_2}<Q_0^2,
\quad
10^k<1.1Q_0,
\quad
10^g<Q_0^2/2.
}
\]

以及统一

\[
\boxed{10^g<Q_0^3/2.}
\]

这已经比上一轮的 coarse generic translation line 明显更低维。

---

# 22. Remaining Frontier

flat degeneracy 已完全消失，所以 A1-only 的下一证明义务变成：

\[
\boxed{
\textbf{Generic Primitive-Defect Synchronization Termination}.}
\]

更具体地，需要解释为什么 moving primitive cores 无法长期满足

\[
\boxed{
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}}
\]

同时保持：

- primitive sphere；
- gcd-profile realizability；
- A1 digit relations；
- exact word realization / reducedness；
- tail divisibility；
- exact \(2\)-adic 与 \(5\)-adic equal-gap condition；
- nondecimal core equality。

现在最危险的已经不再是一个 coefficient vanishing locus，而是**两个非零 integer defects 必须以一个纯十进制幂精确相差**。

---

# 23. Recommended Next Campaign

下一轮只建议三个高价值方向。

## Priority 1 — Defect-Sign Branch Elimination

直接研究

\[
\Delta_{12}>0
\quad\text{vs}\quad
\Delta_{12}<0.
\]

plus branch 已有

\[
10^{n_3}<Q_0,
\quad
10^{m_3}<Q_0^3/2;
\]

minus branch 已有

\[
10^{m_2}<Q_0^2,
\quad
10^k<1.1Q_0,
\quad
10^g<Q_0^2/2.
\]

优先检查其中一个 sign 是否可由 exact word / reducedness 直接排除。

**成功收益：** A1 从两支压成单支，且另一支已经具有显式 logarithmic digit windows。

## Priority 2 — Equal \(2/5\)-adic Gap on Primitive Defects

研究

\[
 v_2(g_1\Delta_3)-v_2(g_3\Delta_{12})
=
 v_5(g_1\Delta_3)-v_5(g_3\Delta_{12})
=m_3.
\]

这比在 \(\mathfrak a,\mathfrak b\) 上研究更好，因为 common \(L_g\) 已消除。

重点不是单独做 valuation overload，而是问：

> 为什么两个来源完全不同的 defects，会同时给出完全相同的 2-adic 与 5-adic valuation gap？

**成功收益：** 可能统一终止整个 generic A1。

## Priority 3 — Primitive Defect × Actual Word Cut

若纯 primitive defect synchronization 仍存在 ambient pseudo-families，就把正向新正规形接到 backward A1-CGS 的 actual first-two cut：

\[
\Delta_{12},\Delta_3
\quad\longleftrightarrow\quad
(T,W,n)\text{ / actual decimal cut}.
\]

反向线已经证明：删除 actual cut 后 prime/Gaussian/valuation compatible pseudo-family 很多；因此下一步若需要更深语义，应只增加这个真正缺失的信息，而不是重新膨胀成旧 Exact-Lift 全变量系统。

**成功收益：** 正反两线第一次在一个非常小的 interface 上真正汇合。

---

# 24. Final Assessment

本轮最初的问题是：

\[
\boxed{\mathfrak a=0\text{ 究竟是否可能？}}
\]

现在答案已经严格确定：

\[
\boxed{\mathfrak a=0\text{ 不可能。}}
\]

其结构原因可以压缩成一句话：

\[
\boxed{
\textbf{flat equation 在 gcd-profile quotient 上强迫一个 }1\bmod4
\textbf{ numerator core 与一个 }3\bmod4
\textbf{ denominator core；}
}
\]

而后者又必须同时进入 primitive hypotenuse \(Q_0\) 与第二坐标 \(P_2\)，从而产生一个 \(3\bmod4\) inert prime，使 primitive sphere 被迫整体含同一素因子。

所以 flat locus 的真正 obstruction 不是“十进制比例太精确”，而是：

\[
\boxed{
\textbf{decimal }2\textbf{-adic mass extraction 改变了 reduced divisor 的 mod-4 orientation，}
}
\]

\[
\boxed{
\textbf{而 primitive three-square sphere 不允许这个 orientation 被分配到 }Q_0\cap P_2.
}
\]

flat degeneracy 删除后，A1 的主方程不再有任何 coefficient-vanishing escape：

\[
\boxed{
\mathfrak b=-10^{m_3}\mathfrak a,
\qquad
\mathfrak a\mathfrak b\ne0.
}
\]

并进一步被本轮压成 primitive defect synchronization：

\[
\boxed{
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}.}
\]

所以新的 A1 frontier 已经从

\[
\text{“generic vs flat translation”}
\]

推进到

\[
\boxed{
\textbf{“两个非零 primitive defects 为什么不可能保持 exact decimal-power synchronization？”}
}
\]

这应当是下一轮正向线的主战场。

---

# 25. Source / Provenance Ledger

本报告核对并使用以下当前文件：

1. `strict_layer_A1_moving_core_decimal_translation_global_campaign.md`
   - A1 translation equation；
   - \(\mathfrak a,\mathfrak b\) 精确定义；
   - flat equation；
   - 上一轮 generic \(10^g<2Q_0^4\)；
   - ten-free coefficient synchronization。

2. `strict_layer_unified_exact_lift_campaign.md` / `(1)`
   - primitive sphere normalization；
   - \(g_i=\gcd(V,P_i)\)；
   - \(g_i\mid P_i\)；
   - primitive-profile master equation；
   - SGR / Exact-Lift variable bridge。

3. `strict_layer_post_DD_consolidation_A1_frontier.md`
   - DD 已删除；
   - Strict frontier 只剩 A1；
   - A1 exact word / finite cut status。

4. `strict_layer_moving_core_square_spacing_campaign.md`
   - square-spacing 仍为 auxiliary；
   - bare \(g\)-large mechanism 不足。

5. `strict_layer_backward_A1_word_recovery_architecture_campaign.md`
   - actual cut 是不可删除的 semantic source information；
   - pure prime/Gaussian/valuation route 在脱离 actual cut 时存在 ambient pseudo-family；
   - 下一轮若 primitive-defect route不足，应在最小 interface 上与 A1-CGS 对接。

6. `exact_lift_research_synthesis_2026-08-10.md`
   - 仅用于历史 A1 saturated support / tail-bound provenance；
   - 本轮 flat closure 不依赖旧 synthesis 中任何已撤回 closure claim。

---

# 26. Claim Ledger

## PROVED

- \(Q_0\) odd for primitive sphere;
- flat gcd-profile reduced quotient \(b10^{m_2}D=aQ_0\);
- \(a\mid P_1\), \(b\mid P_2,Q_0\);
- \(v_2(a)=m_2\);
- odd core \(a_0\) only has primes \(1\bmod4\);
- \(a_0\equiv1\bmod4\);
- \(b\equiv3\bmod4\);
- flat contradiction;
- \(\mathfrak a\neq0\);
- flat locus empty;
- primitive defect synchronization (GSYNC);
- universal \(P_1 10^k>Q_0\);
- universal tail divisibility \(10^{n_3}\mid g_1g_2(Q_0-P_3)\);
- plus/minus defect sign dichotomy;
- plus branch \(10^{n_3}<Q_0\), \(10^{m_3}<Q_0^3/2\);
- minus branch \(10^{m_2}<Q_0^2\), \(10^k<1.1Q_0\), \(10^g<Q_0^2/2\);
- universal improved \(10^g<Q_0^3/2\);
- primitive-defect ten-free support synchronization and equal \(2/5\)-adic gap.

## EXPERIMENTAL

- restricted \(Q_0\le300\), \(m_2,k\le3\) scan: 18,270 primitive directions, 32 numerator-divisible states, all reduced denominator \(3\bmod4\), zero full divisibility hit.

## FAILED / INSUFFICIENT

- pure \(3\bmod4\) prime chase;
- pure valuation budget;
- ratio approximation alone;
- standalone sum-of-two-squares;
- sphere parametrization as proof engine;
- coarse divisor allocation alone;
- square-spacing for flat elimination;
- old saturated support as necessary input;
- brute-force no-hit as proof.

## OPEN

\[
\boxed{
\textbf{Generic Primitive-Defect Synchronization Termination}.}
\]

以及最终

\[
\boxed{A_1=\varnothing}
\]

仍未证明。
