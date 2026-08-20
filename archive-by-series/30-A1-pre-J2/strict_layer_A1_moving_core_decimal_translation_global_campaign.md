# 三项十进制拼接平方和问题：A1 Moving-Core / Decimal-Translation Global Campaign

**文件名：** `strict_layer_A1_moving_core_decimal_translation_global_campaign.md`  
**研究范围：** Strict Layer 正向线，仅研究 \(A_1\)-only；DD 已闭合，不迁移 DD 专属技术。  
**本轮目标：** 不要求 \(A_1=\varnothing\)，而是把 A1 压缩成尽可能低维的 moving-family / decimal-translation 终止问题。  
**本轮核心新结论：** A1 的 primitive-profile 主方程在 \(X=10^g\) 上不是一般二次/Pell 型，而是**线性 translation equation**；非退化状态统一满足 \(g=O(\log Q_0)\)。唯一使该主方程对 \(g\) 完全失明的，是一个明确的 **flat coefficient locus**。

---

# 1. Executive Summary

本轮最重要的结论不是一个新的局部 obstruction，而是 A1 的全局坐标发生了明显降维。

## 1.1 当前 Strict Layer 的唯一顶层无穷源不是 \((Q_0,g)\) 两轴

SGR-10B 已经冻结：

\[
\boxed{
\text{fixed primitive core}\Longrightarrow\text{finite A1 decimal fibre}.
}
\]

因此任意无限 A1 exact-candidate sequence 都必有

\[
\boxed{Q_0\to\infty.}
\]

反过来，每个固定高度壳 \(Q_0=H\) 上 primitive cores 有限，每个 core 的 decimal fibre 又有限，所以该高度壳中的 A1 candidates 有限。

因此，严格意义上的 top-level infinity source 只有：

\[
\boxed{\text{moving primitive-core height }Q_0.}
\]

这修正了旧 saturated A1 语言中“\(g\) 是第二个独立无穷方向”的表述。

**状态：PROVED / inherited from SGR-1 + SGR-10B.**

但是，这并不意味着 \(g,k_{12},m_i,n_i,U,V\) 是 \(Q_0\) 的函数；它只意味着这些量不能在固定 primitive core 上独立逃逸。

---

## 1.2 A1 的 decimal translation 实际上线性化

令

\[
k:=k_{12}=s_2+s_3\ge1,
\qquad
g:=-s_3=m_3-n_3\ge0.
\]

于是

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g.
\]

对 primitive core

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

与 gcd profile

\[
g_i=\gcd(V,P_i),
\qquad
L_g=\operatorname{lcm}(g_1,g_2,g_3),
\qquad
h_i=L_g/g_i,
\]

已有 primitive-profile master equation

\[
P_1h_1 10^{n_2+n_3}
+
P_2h_2 10^{n_3}
+
P_3h_3
=
Q_0\left(
h_1 10^{m_2+m_3}
+h_2 10^{m_3}
+h_3
\right).
\tag{1.1}
\]

代入 A1 位数关系，定义

\[
\boxed{
\mathfrak a
:=
h_1 10^{m_2}(P_1 10^k-Q_0)-Q_0h_2,
}
\tag{1.2}
\]

\[
\boxed{
\mathfrak b
:=
P_2h_2 10^{n_3}-h_3(Q_0-P_3),
}
\tag{1.3}
\]

则 (1.1) 精确化为

\[
\boxed{
10^{m_3}\mathfrak a+\mathfrak b=0.
}
\tag{TL}
\]

由于 \(m_3=n_3+g\)，若令

\[
X=10^g,
\qquad
S=10^{n_3},
\]

则

\[
\boxed{
S\,\mathfrak a\,X+\mathfrak b=0.
}
\tag{TL-X}
\]

所以对固定

\[
(P_i,Q_0;\ g_i;\ m_2,n_3,k)
\]

的 coefficient state，A1 的 translation variable \(X=10^g\) 落在一条**直线**上，而不是 Pell 曲线或一般 conic 上。

**状态：NEW PROVED.**

---

## 1.3 Generic A1 自动满足 logarithmic translation synchronization

若

\[
\mathfrak a\ne0,
\]

则 (TL) 给出

\[
\mathfrak b=-10^{m_3}\mathfrak a.
\]

因为 \(\mathfrak a\in\mathbf Z\setminus\{0\}\)，

\[
10^{m_3}\le|\mathfrak b|.
\]

另一方面 \(P_2<Q_0\)、\(P_3<Q_0\)，故

\[
|\mathfrak b|
<
Q_0\left(h_2 10^{n_3}+h_3\right).
\]

除以 \(10^{n_3}\)：

\[
\boxed{
10^g
<
Q_0\left(
h_2+\frac{h_3}{10^{n_3}}
\right).
}
\tag{1.4}
\]

又因为

\[
h_i\le L_g\le g_1g_2g_3\le P_1P_2P_3<Q_0^3,
\]

所以

\[
\boxed{
10^g<2Q_0^4,
}
\tag{1.5}
\]

即

\[
\boxed{
g<4\log_{10}Q_0+\log_{10}2.
}
\tag{1.6}
\]

这是一条不使用 DD、不使用 Hensel、不使用 square-spacing 的统一 A1 translation-height bound。

它没有关闭 A1，但已经证明：

> 在所有非退化 moving states 中，decimal translation 不可能比 primitive height 的对数尺度增长得更快。

**状态：NEW PROVED.**

---

## 1.4 唯一逃出上述同步的主退化：flat translation locus

如果

\[
\mathfrak a=0,
\]

则 (TL) 强制

\[
\mathfrak b=0.
\]

反过来若二者都为零，primitive-profile master equation 本身对 \(g\) 完全失去约束。

定义

\[
\boxed{
\mathcal D_{\rm flat}:
\qquad
\mathfrak a=\mathfrak b=0.
}
\]

这是本轮识别出的唯一真正的 **translation-flat locus**。

在该 locus 上：

\[
\boxed{
g_2 10^{m_2}(P_1 10^k-Q_0)=g_1Q_0,
}
\tag{1.7}
\]

\[
\boxed{
g_3P_2 10^{n_3}=g_2(Q_0-P_3).
}
\tag{1.8}
\]

因此虽然 \(g\) 在粗 master equation 中消失，但另外三个 decimal exponents 被强制压到 logarithmic height：

\[
\boxed{
10^{m_2}<Q_0^2,
}
\tag{1.9}
\]

\[
\boxed{
10^{n_3}<Q_0,
}
\tag{1.10}
\]

\[
\boxed{
10^k\le1.1\,Q_0.
}
\tag{1.11}
\]

即

\[
m_2<2\log_{10}Q_0,\qquad
n_3<\log_{10}Q_0,\qquad
k\le\log_{10}(1.1Q_0).
\]

**状态：NEW PROVED.**

所以 A1 的全局图景现在不是“两个自由高度 \(Q_0,g\)”；更准确的是：

\[
\boxed{
\begin{array}{c}
Q_0\to\infty
\\[1mm]
\Downarrow
\\[1mm]
\text{generic states: }g=O(\log Q_0)
\\[1mm]
\text{or}
\\[1mm]
\mathcal D_{\rm flat}:
\ m_2,n_3,k=O(\log Q_0),\
g\text{ 由更深 exact recovery 决定}.
\end{array}
}
\]

---

## 1.5 当前最值得研究的 invariant 已经出现

由

\[
\mathfrak b=-10^{m_3}\mathfrak a
\]

得到对所有 \(p\ne2,5\)

\[
\boxed{
v_p(\mathfrak a)=v_p(\mathfrak b),
}
\tag{1.12}
\]

而

\[
\boxed{
v_2(\mathfrak b)-v_2(\mathfrak a)
=
v_5(\mathfrak b)-v_5(\mathfrak a)
=
m_3.
}
\tag{1.13}
\]

若定义十进制自由核

\[
\operatorname{core}_{10}(n)
=
\frac{|n|}
{2^{v_2(n)}5^{v_5(n)}},
\]

则 generic exact A1 candidate 必满足

\[
\boxed{
\operatorname{core}_{10}(\mathfrak a)
=
\operatorname{core}_{10}(\mathfrak b).
}
\tag{1.14}
\]

这正是旧研究一直寻找的“decimal shift 一方面制造巨大 \(10\)-power，另一方面 non-decimal arithmetic 必须完全同步”的 coefficient-plane invariant。

**状态：NEW PROVED as a necessary invariant; its uniform obstruction power remains OPEN.**

---

# 2. Frozen Inputs

本轮冻结以下结果。

## 2.1 Strict scope

严格层只剩

\[
\boxed{A_1\text{-only}.}
\]

A1 cell 为

\[
\boxed{
s_3\le0,
\qquad
s_2+s_3>0.
}
\]

定义

\[
g=-s_3\ge0,
\qquad
k=k_{12}=s_2+s_3\ge1.
\]

所以

\[
s_2=g+k,
\qquad
n_2=m_2+g+k,
\qquad
m_3=n_3+g.
\]

DD 已由 SGR-9A 闭合；本报告不使用 DD orientation、double resonance、post-deflation、third-tail quotient difference 或其 source phase。

**状态：PROVED / FROZEN.**

主要来源：

- `strict_layer_post_DD_consolidation_A1_frontier.md`（SGR-10B）
- `strict_layer_DD_oriented_tail_window_campaign.md`（仅用于确认 DD 已闭合）

---

## 2.2 Primitive normalization

冻结

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

\[
\gcd(U,V)=1,
\qquad
g_i=\gcd(V,P_i),
\]

\[
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.
\]

Exact-Lift / SGR bridge：

\[
q=V,\qquad y_i=UP_i,\qquad H=UQ_0.
\]

**状态：PROVED / FROZEN.**

主要来源：

- `strict_layer_unified_exact_lift_campaign.md`

---

## 2.3 Fixed-core finite fibre

冻结：

\[
\boxed{
\text{fixed primitive core}
\Longrightarrow
\text{finite decimal fibre}.
}
\]

并且每个 fixed height shell \(Q_0=H\) 只有有限 A1 candidate states。

**状态：PROVED / DERIVED.**

主要来源：

- SGR-1（正文目前未重新暴露）
- `strict_layer_unified_exact_lift_campaign.md` 的自包含重推
- `strict_layer_post_DD_consolidation_A1_frontier.md`

注意：`strict_layer_global_reduction_campaign.md` 本轮再次按精确文件名与 SGR-1 关键词检索，仍未在 File Library 中重新暴露，因此本文不伪称重新读到了其正文；只使用后续统一报告已经自包含冻结的结论。

---

## 2.4 Current exact A1 terminal semantics

当前最短 exact recovery language 是：

\[
T=(b_1,b_2,b_3,S),
\qquad
S=10^{n_3},
\]

加 full numerator word \(\mathbf A\)，再加至多一个 binary prefix-cut choice。

fixed \((T,\mathbf A)\) 后合法 prefix fibre

\[
\boxed{\le2}.
\]

最终 exact gate 可以写成

\[
b_2^2a_1^2+b_1^2a_2^2
=
G^2
\left[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
-
\left(\frac{a_3}{b_3}\right)^2
\right].
\tag{A1-WR}
\]

**状态：PROVED / DERIVED.**

主要来源：

- `strict_layer_post_DD_consolidation_A1_frontier.md`
- `strict_layer_backward_exact_root_pair_fibre_campaign.md`

---

## 2.5 Tail normalization

A1 中 effective tail length 是

\[
\boxed{\ell=n_3.}
\]

令

\[
S=10^{n_3},
\qquad
\eta_3=\gcd(S,b_3),
\qquad
L=S/\eta_3,
\qquad
\tau=b_3/\eta_3.
\]

所以 \(L,\eta_3,\tau\) 都由 trace \((b_3,S)\) 决定，不是新的自由坐标。

**状态：PROVED / DERIVED.**

主要来源：

- `strict_layer_backward_denominator_decimal_interface.md`

saturated branch

\[
L=1
\]

等价于 \(S\mid b_3\)：有效 decimal tail 已完全被第三分母吸收。

旧 denominator-only theorem 在 saturated branch 给出

\[
\boxed{
\ell
\le
\left\lfloor
\log_5((10Q+2)G)
\right\rfloor
\le3(m_1+m_2)+1.
}
\tag{2.1}
\]

**状态：PROVED in the inherited A1 saturated theorem; scope is saturated \(L=1\), not all A1.**

主要来源：

- `exact_lift_research_synthesis_2026-08-10.md`, §§29–31.

---

## 2.6 Square gate status

A1 的 normalized square gate仍成立，但

\[
g\to\infty\not\Longrightarrow\rho\to0.
\]

已有

\[
\boxed{
\rho>\frac1{400}10^{-2k}.
}
\]

所以裸 \(g\)-large adjacent-square argument 不能终止 A1。

**状态：PROVED negative result.**

主要来源：

- `strict_layer_moving_core_square_spacing_campaign.md`

---

# 3. Canonical A1 State

这里必须区分“exact semantic minimality”与“moving-family asymptotic coordinates”。

## 3.1 Exact recovery chart

当前已经严格充分的 exact chart 是：

\[
\boxed{
\mathcal R_{\rm A1}
=
(T,\mathbf A,\omega_{12}),
}
\]

其中

\[
T=(b_1,b_2,b_3,10^{n_3}),
\qquad
\omega_{12}\in\{0,1\}
\]

仅在 two-cut collision 时需要。

由它恢复所有 \(a_i,b_i\)，再检查：

- digit legality；
- A1 cell；
- \(\gcd(a_i,b_i)=1\)；
- A1-WR。

**状态：PROVED sufficient semantic chart.**

---

## 3.2 Moving-family chart

为了研究 \(Q_0\to\infty\)，上述 chart 太“word-level”，不暴露 primitive height。

本轮建议使用：

\[
\boxed{
\mathcal M_{\rm A1}
=
\left(
\mathcal P,\mathbf g;
m_2,n_3,k;
g;
\mathfrak r
\right),
}
\tag{3.1}
\]

其中

\[
\mathcal P=(P_1,P_2,P_3,Q_0),
\qquad
\mathbf g=(g_1,g_2,g_3),
\]

而 \(\mathfrak r\) 表示 full recovery 所需的有限 realization data（scale mantissa / carry / exact word legality 等）。

在 primitive-profile 主方程层面，真正参与 translation 的只需要

\[
\boxed{
(\mathcal P,\mathbf g;m_2,n_3,k;g).
}
\]

因为：

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g
\]

自动恢复。

而：

- \(L,\eta_3,\tau,\ell\) 是 trace-derived；
- \(D=10^gQ\) 是 derived；
- gap root pair 已被 SGR-10B one-word collapse 消掉；
- discriminant/resultant 不是独立 candidate coordinate；
- prefix cut只通过 \(n_2\)、即这里的 \(k\) 与 finite \(\omega_{12}\) 进入。

**状态：NEW RECOMMENDED COORDINATE SYSTEM; sufficiency for full exact recovery is CONDITIONAL on retaining \(\mathfrak r\).**

---

## 3.3 为什么不能宣称一个 globally finite pattern alphabet

用户希望测试

\[
\mathscr A_1
=
\bigcup_{\sigma\in\Sigma_{\rm finite}}
\mathscr F_\sigma(Q_0,g).
\]

当前 proof library 只证明：

- fixed primitive core 的 state set finite；
- fixed \((T,\mathbf A)\) 的 prefix cut数 \(\le2\)。

它没有证明存在一个与 \(Q_0\) 无关的全局有限 alphabet \(\Sigma_{\rm finite}\)。

因此正确表述应是：

\[
\boxed{
\mathscr A_1
=
\bigcup_{H\ge1}
\ \bigcup_{\sigma\in\Sigma_H}
\mathscr F_\sigma,
\qquad
|\Sigma_H|<\infty.
}
\tag{3.2}
\]

而本轮新 translation-line theorem 进一步给出：

\[
\boxed{
\sigma\notin\mathcal D_{\rm flat}
\Longrightarrow
|\{g:\text{master equation holds}\}|\le1.
}
\tag{3.3}
\]

所以“无限 translation fibre”只可能发生在 flat locus。

**状态：PROVED modulo the inherited fixed-shell finiteness.**

---

# 4. Escape-Direction Audit

下面的“independent”指能否在 fixed primitive core 上单独趋于无穷。

| 参数 | 当前地位 | 结论 |
|---|---|---|
| \(Q_0\) | **genuinely top-level unbounded** | 任意无限 A1 family 必有 \(Q_0\to\infty\) |
| \(g\) | **dependent / projected** | fixed core 不可无界；generic 更有 \(g<4\log_{10}Q_0+\log_{10}2\) |
| \(k=k_{12}\) | **dependent / projected** | fixed core 不可无界；global uniform bound仍 OPEN；flat locus 上 \(10^k\le1.1Q_0\) |
| \(m_3\) | **dependent** | \(m_3=n_3+g\)，fixed core不可无界 |
| \(n_2\) | **dependent** | \(n_2=m_2+g+k\) |
| \(n_3=\ell\) | **dependent** | fixed core不可无界；saturated 时有 (2.1)；flat locus 上 \(10^{n_3}<Q_0\) |
| \(m_2\) | **dependent** | fixed core不可无界；flat locus 上 \(10^{m_2}<Q_0^2\) |
| \(m_1,n_1,U,V\) | **not independent infinity sources** | fixed core finite-fibre theorem排除 fixed-core runaway，但尚无统一显式 \(O(\log Q_0)\) bound |
| \(L,\eta_3,\tau\) | **derived** | 由 \((b_3,10^{n_3})\) 决定 |
| prefix cut | **uniformly finite after fixed word** | fixed \((T,\mathbf A)\) fibre \(\le2\) |
| gap/tail root | **redundant as A1 coordinate** | 已被 one-word exact recovery 消元 |

因此用户提出的候选 theorem

\[
\text{“任何无限 A1 family 都必须 }Q_0,g\to\infty\text{”}
\]

**不成立为当前可证陈述**：完全可能存在理论上的 sequence

\[
Q_0\to\infty,
\qquad
g=0\text{ 或 bounded}.
\]

目前没有 theorem 排除它。

正确修正版是：

\[
\boxed{
\text{任何无限 A1 family 都必须 }Q_0\to\infty,
}
\]

并且：

\[
\boxed{
\text{若该 family 避开 }\mathcal D_{\rm flat},
\quad
g=O(\log Q_0).
}
\tag{4.1}
\]

**状态：PROVED.**

---

# 5. Decimal Translation Normal Form

## 5.1 从 primitive-profile master equation 精确推导

已有

\[
P_1h_1 10^{n_2+n_3}
+
P_2h_2 10^{n_3}
+
P_3h_3
=
Q_0(
h_1 10^{m_2+m_3}
+h_2 10^{m_3}
+h_3).
\]

A1 中

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g.
\]

所以

\[
n_2+n_3=m_2+k+m_3.
\]

代入：

\[
P_1h_1 10^{m_2+k+m_3}
+
P_2h_2 10^{n_3}
+
P_3h_3
\]

\[
=
Q_0(
h_1 10^{m_2+m_3}
+h_2 10^{m_3}
+h_3).
\]

收集 \(10^{m_3}\)：

\[
10^{m_3}
\left[
h_1 10^{m_2}(P_1 10^k-Q_0)
-Q_0h_2
\right]
\]

\[
+
\left[
P_2h_2 10^{n_3}
-h_3(Q_0-P_3)
\right]
=0.
\]

即 (TL)。

**状态：NEW PROVED.**

---

## 5.2 Coefficient plane dimension

固定

\[
(\mathcal P,\mathbf g;m_2,n_3,k)
\]

后，

\[
(\mathfrak a,\mathfrak b)\in\mathbf Z^2
\]

被完全固定。

translation equation 只读取其 projective ratio：

\[
\boxed{
10^{m_3}=-\frac{\mathfrak b}{\mathfrak a},
\qquad
(\mathfrak a\ne0).
}
\tag{5.1}
\]

所以真正的 translation coefficient space 是：

- affine 上二维 pair \((\mathfrak a,\mathfrak b)\)；
- projectively 只剩一个 ratio；
- \(10^{m_3}\) 必须命中非常稀疏的集合 \(\{10,10^2,\dots\}\)。

若改用 \(X=10^g\)：

\[
\boxed{
X=-\frac{\mathfrak b}{10^{n_3}\mathfrak a}.
}
\tag{5.2}
\]

因此 generic state 对 \(g\) 至多有一个候选。

**状态：NEW PROVED.**

---

## 5.3 Digit legality 在新坐标中的位置

在 translation-line 层：

\[
m_2,n_3\ge1,
\qquad
k\ge1,
\qquad
g\ge0.
\]

并且

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g.
\]

这只编码 **digit lengths**，不编码 mantissa legality。

真正的：

\[
10^{n_i-1}\le a_i<10^{n_i},
\qquad
10^{m_i-1}\le b_i<10^{m_i}
\]

以及 \(\gcd(a_i,b_i)=1\)，仍在 realization layer \(\mathfrak r\) 中。

所以本轮没有把 digit legality 错误地等同于 exponent legality。

**状态：PROVED distinction.**

---

## 5.4 Translation divisibility invariant

generic case 中

\[
\mathfrak b=-10^{m_3}\mathfrak a.
\]

于是：

\[
10^{m_3}\mid\mathfrak b,
\]

且若

\[
0<|\mathfrak b|<10^{m_3}
\]

即可立即矛盾。

这正是旧 A1 coefficient-plane program 希望得到的形状，只不过现在不需要猜 determinant/resultant；primitive-profile master equation 自己已经给出 canonical integer pair。

**状态：NEW PROVED mechanism.**

---

# 6. Moving-Core Geometry

## 6.1 主几何不是 Pell，而是 translation line

对固定 coefficient state，主方程是

\[
S\mathfrak a X+\mathfrak b=0,
\qquad
X=10^g.
\]

所以：

\[
\boxed{
\text{generic A1 translation geometry = affine line.}
}
\]

并不存在固定 coefficient state 内部的 Pell orbit。

任何无限 A1 family 必须通过**移动 coefficients**，即 primitive core / gcd profile / exponent state 同时变化，而不是在同一曲线上反复产生 \(g\)。

**状态：NEW PROVED structural interpretation.**

---

## 6.2 Square gate 在 \(X=10^g\) 坐标中的几何

已有 A1 deflated square gate：

\[
\Psi
=
10^{m_3}\widehat K
-
2h_3X^2\widehat Q\widehat{\mathcal N}
=
\varepsilon Y^2,
\]

其中

\[
\widehat K
=
\widehat G^2\widehat C^2
-
X^2\widehat Q^2\widehat{\mathcal N}.
\]

A1 中

\[
\widehat C
=
C_1 10^{m_2+k}X+C_2.
\]

令

\[
\alpha=C_1 10^{m_2+k},
\qquad
R=10^{n_3},
\]

则

\[
\widehat C=\alpha X+C_2,
\qquad
10^{m_3}=RX.
\]

直接展开：

\[
\boxed{
\Psi_\sigma(X)
=
a_\sigma X^3+b_\sigma X^2+c_\sigma X,
}
\tag{6.1}
\]

其中

\[
\boxed{
a_\sigma
=
R\left(
\widehat G^2\alpha^2
-
\widehat Q^2\widehat{\mathcal N}
\right),
}
\tag{6.2}
\]

\[
\boxed{
b_\sigma
=
2R\widehat G^2\alpha C_2
-
2h_3\widehat Q\widehat{\mathcal N},
}
\tag{6.3}
\]

\[
\boxed{
c_\sigma
=
R\widehat G^2C_2^2>0.
}
\tag{6.4}
\]

因此 standalone square gate 的代数曲线是

\[
\boxed{
\varepsilon Y^2
=
X(a_\sigma X^2+b_\sigma X+c_\sigma).
}
\tag{6.5}
\]

固定 parity 后，generic 情形是一个 cubic double cover；若 cubic 无重根，则是 genus-one 型几何，而不是 Pell conic。

**状态：NEW PROVED algebraic rewrite; genus-one interpretation is STANDARD / CONDITIONAL on nonsingularity.**

---

## 6.3 Square-gate degeneracies

因为 \(c_\sigma>0\)，\(X=0\) 始终是 simple root。

square cubic 的自然退化包括：

1. **leading degeneration**
   \[
   a_\sigma=0,
   \]
   此时降为 quadratic/conic；

2. **singular quadratic-factor locus**
   \[
   b_\sigma^2-4a_\sigma c_\sigma=0,
   \]
   此时 cubic 有重根，变成 singular rational curve。

但是：

\[
\boxed{
\text{square-gate degeneration alone 不产生 translation freedom。}
}
\]

只要

\[
\mathfrak a\ne0,
\]

translation line 已经唯一固定 \(X\)。

所以 square cubic 的 Pell / elliptic / singular 分类只能作为**第二层 admissibility test**，不能作为顶层 moving-\(g\) 生成机制。

**状态：NEW PROVED hierarchy.**

---

## 6.4 真正的 translation-degenerate geometry

真正让 \(X\) 保持自由的是

\[
\boxed{
\mathfrak a=\mathfrak b=0.
}
\]

此时整条 \(X\)-axis 都被 coarse primitive-profile master equation 接受。

所以如果未来存在一个“Pell-like”或“elliptic-like” translation family，它必须首先落在

\[
\boxed{\mathcal D_{\rm flat}}
\]

上，然后由 square cubic / exact word / reducedness 等剩余条件继续切割。

这比先对所有 A1 做 Pell 分类小得多。

**状态：NEW PROVED reduction.**

---

# 7. The Flat Locus in More Detail

## 7.1 Primitive equations

\[
\mathfrak a=0
\]

等价于

\[
h_1 10^{m_2}(P_1 10^k-Q_0)
=
Q_0h_2.
\]

消去 \(L_g\)：

\[
\boxed{
g_2 10^{m_2}(P_1 10^k-Q_0)
=
g_1Q_0.
}
\tag{7.1}
\]

所以

\[
P_1 10^k>Q_0.
\]

而

\[
\mathfrak b=0
\]

等价于

\[
\boxed{
g_3P_2 10^{n_3}
=
g_2(Q_0-P_3).
}
\tag{7.2}
\]

**状态：NEW PROVED.**

---

## 7.2 Logarithmic compression inside the flat locus

从 (7.1)，因为

\[
P_1 10^k-Q_0\ge1,
\]

有

\[
10^{m_2}
\le
\frac{g_1Q_0}{g_2}
\le
P_1Q_0
<
Q_0^2.
\]

得到 (1.9)。

再由

\[
P_1 10^k
=
Q_0
\left(
1+\frac{g_1}{g_2 10^{m_2}}
\right),
\]

以及

\[
g_1\le P_1,\quad g_2\ge1,\quad10^{m_2}\ge10,
\]

得到

\[
10^k
\le
\frac{Q_0}{P_1}+\frac{Q_0}{10}
\le1.1Q_0.
\]

从 (7.2)：

\[
10^{n_3}
=
\frac{g_2(Q_0-P_3)}{g_3P_2}
\le
Q_0-P_3
<
Q_0.
\]

所以 flat locus 不是“所有 decimal lengths 都失控”；它只让 **translation gap \(g\)** 从该主方程中消失。

**状态：NEW PROVED.**

---

## 7.3 Semantic meaning of flatness

利用

\[
g_i=V/b_i,
\]

(7.1) 可化成

\[
\boxed{
P_1b_1 10^{m_2+k}
=
Q_0Q_{12},
}
\qquad
Q_{12}=b_1 10^{m_2}+b_2.
\tag{7.3}
\]

乘 \(U/V\)，因为

\[
r_i=\frac UVP_i,
\qquad
\mathcal R=\frac UVQ_0,
\]

得到

\[
\boxed{
a_1 10^{m_2+k}
=
\mathcal R\,Q_{12}.
}
\tag{7.4}
\]

同理 (7.2) 化成

\[
\boxed{
P_2b_2 10^{n_3}
=
(Q_0-P_3)b_3,
}
\tag{7.5}
\]

即

\[
\boxed{
a_2 10^{n_3}+a_3
=
\mathcal R\,b_3.
}
\tag{7.6}
\]

所以 flat locus 的真正含义是：

> 完整拼接 equality 不再依赖“prefix 与 tail 的相互补偿”；它分裂成两个子平衡，每一边都单独以同一个全局 norm \(\mathcal R\) 对齐。

这不是 presentation artifact，而是一个真正的 **split-resonance**。

**状态：NEW PROVED semantic interpretation.**

---

## 7.4 Flat locus 与 primitive norm

由 (7.2)：

\[
10^{n_3}\mid
\frac{g_2}{g_3}(Q_0-P_3)
\]

的精确整数版本为

\[
g_3P_2 10^{n_3}
=
g_2(Q_0-P_3).
\]

同时

\[
(Q_0-P_3)(Q_0+P_3)
=
P_1^2+P_2^2.
\]

所以 flat locus 把第三 tail 的整段 decimal depth 直接压入 primitive radial defect

\[
Q_0-P_3
\]

以及前两 primitive coordinates 的二平方 norm。

这是下一轮可能重新启用 Gaussian/norm arithmetic 的正确位置：**不是做 descent，而是研究 flat-locus norm divisibility。**

**状态：PROVED identity + HEURISTIC next-use.**

---

# 8. Candidate Global Invariants

本轮只保留三个。

## 8.1 Invariant I — Decimal Translation Defect Pair

定义

\[
\boxed{
\Delta_{\rm tr}
:=
(\mathfrak a,\mathfrak b).
}
\]

exact A1 必须满足

\[
\boxed{
\mathfrak b=-10^{m_3}\mathfrak a.
}
\]

它同时给出：

- Archimedean height relation；
- \(2\)-adic shift；
- \(5\)-adic shift；
- all non-decimal prime-support equality；
- flat degeneration \((0,0)\)。

因此它比 generic resultant 更直接地读取 decimal coefficient plane。

**当前强度：NEW PROVED necessary invariant.**

**下一步缺口：** 证明 moving primitive cores 中 \(\mathfrak a,\mathfrak b\) 的 prime-to-10 cores 很少能够完全一致，或证明 \(\mathfrak a\) 不能过小。

**优先级：最高。**

---

## 8.2 Invariant II — Ten-free Core / Mixed Valuation Profile

对 \(n\ne0\) 定义

\[
n^{\langle10\rangle}
=
\frac{|n|}
{2^{v_2(n)}5^{v_5(n)}}.
\]

generic A1 candidate 必须满足

\[
\boxed{
\mathfrak a^{\langle10\rangle}
=
\mathfrak b^{\langle10\rangle},
}
\tag{8.1}
\]

以及

\[
\boxed{
v_2(\mathfrak b)-v_2(\mathfrak a)
=
v_5(\mathfrak b)-v_5(\mathfrak a)
=
m_3.
}
\tag{8.2}
\]

等价地，十进制 valuation imbalance

\[
\omega_{10}(n):=v_2(n)-v_5(n)
\]

满足

\[
\boxed{
\omega_{10}(\mathfrak a)=\omega_{10}(\mathfrak b).
}
\tag{8.3}
\]

**当前强度：NEW PROVED necessary invariant.**

**为何有希望：** \(\mathfrak a\) 主要读取 first-carrier / prefix defect，\(\mathfrak b\) 主要读取 second-plus-third radial defect；二者来源不同，却必须拥有完全相同的 non-decimal part。

**风险：** moving core 可以不断提供新 primes，因此“prime support不同”不能靠有限素数集合直接结束；需要 coefficient gcd / norm identity / height coupling。

**优先级：高。**

---

## 8.3 Invariant III — Flat Radial Defect

在 \(\mathcal D_{\rm flat}\) 上：

\[
\boxed{
Q_0-P_3
=
\frac{g_3P_2}{g_2}10^{n_3}.
}
\]

结合

\[
P_1^2+P_2^2
=
(Q_0-P_3)(Q_0+P_3)
\]

定义 flat radial object

\[
\boxed{
\mathcal R_{\rm flat}
:=
\frac{P_1^2+P_2^2}{10^{n_3}}
=
\frac{g_3P_2}{g_2}(Q_0+P_3).
}
\tag{8.4}
\]

它把：

- decimal tail；
- primitive sphere radial gap；
- Gaussian norm \(P_1^2+P_2^2\)

放到一个整数对象中。

**当前强度：PROVED on \(\mathcal D_{\rm flat}\).**

**下一步缺口：** 与 reducedness、saturated \(L=1\)、A1-WR 或 square cubic 联立，证明该 norm allocation 不能长期支持 sliding \(g\)。

**优先级：仅在 flat campaign 中最高。**

---

# 9. Saturated \(L=1\) Reinterpretation

旧 A1 研究把 saturated

\[
L=1
\]

视为危险支，因为 Gaussian flip 在这里退化为 projective identity，而 \(g\) 看似仍可无界。

本轮需要修正其几何解释。

## 9.1 \(\ell\) 没有被绝对有界

旧 theorem 只有

\[
\ell=n_3
\le3(m_1+m_2)+1.
\]

所以它消除了“\(n_3\) 相对于 prefix denominator 完全自由”的情况，但没有给出绝对常数界。

因此：

\[
\boxed{
\text{“tail combinatorics 已全局有限化”是过强表述。}
}
\]

正确说法是：

\[
\boxed{
\text{saturated tail depth 被 prefix denominator height 线性控制。}
}
\]

**状态：AUDITED / PROVED correction.**

---

## 9.2 \(g\) 也不是独立 infinity

SGR-1 已经保证：

\[
g\to\infty
\Longrightarrow
Q_0\to\infty
\]

对 exact candidate sequence 成立。

本轮进一步得到：

\[
\boxed{
L=1,\ \mathfrak a\ne0
\Longrightarrow
g<4\log_{10}Q_0+\log_{10}2.
}
\]

所以 saturated A1 真正危险的部分进一步缩成：

\[
\boxed{
L=1\quad\cap\quad\mathcal D_{\rm flat},
}
\]

如果我们关心“\(g\) 在 coarse translation equation 中保持自由”的情形。

这不是说所有 non-flat saturated states 已经无解；它们仍可能随 \(Q_0\to\infty\) 形成 \(g=O(\log Q_0)\) 的 moving family。

**状态：NEW PROVED reduction / NOT closure.**

---

## 9.3 Saturated prime-support theorem 的地位

旧工作在 saturated A1 中定义 residual non-decimal factor \(h\)，证明：

\[
h\mid G,
\]

且 \(h\) 的奇素因子满足

\[
p\equiv1\pmod4.
\]

这仍是有效结构，但本轮不把它提升为 terminal obstruction：

- \(1\bmod4\) primes 无限多；
- moving \(Q_0\) 可以持续带入新 prime support；
- 只有与 \(\Delta_{\rm tr}\) 或 \(\mathcal R_{\rm flat}\) 结合时才可能产生 rigidity。

**状态：PROVED inherited constraint / insufficient alone.**

---

# 10. Experiments / Counterexamples

## 10.1 Symbolic verification of translation-line reduction

使用 symbolic expansion 将 A1 位数关系代入 primitive-profile master equation，精确得到：

\[
10^{m_3}\mathfrak a+\mathfrak b=0.
\]

无近似、无数值假设。

**状态：EXPERIMENTAL CHECK supporting an already hand-proved identity.**

---

## 10.2 Small ambient scan of the flat equation

为了测试 \(\mathcal D_{\rm flat}\) 是否非常常见，进行了一个**比 actual gcd-profile 条件更宽**的 ambient scan：

- \(2\le Q_0\le300\)；
- 所有正 primitive sphere cores
  \[
  P_1^2+P_2^2+P_3^2=Q_0^2;
  \]
- 共枚举 18,270 个有序 core records；
- 对每个 core 枚举所有 divisor triples
  \[
  g_i\mid P_i
  \]
  （未要求它们一定同时来自某个真实 \(V\)，因此搜索空间比真实 profile 更大）；
- 共检查 3,949,440 个 divisor-profile records；
- 检查
  \[
  k\in\{1,2\},
  \qquad
  m_2\in\{1,2\}.
  \]

结果：

\[
\boxed{
\mathfrak a=0
\text{ 的 ambient hit 数}=0.
}
\]

因此当然也没有 flat \((\mathfrak a,\mathfrak b)=(0,0)\) hit。

这不是证明，因为：

- \(Q_0\) 有界；
- \(k,m_2\) 有界；
- 没有建立一般不等式；
- 计算不能替代全局论证。

但它提示：

\[
\boxed{
\mathcal D_{\rm flat}
\text{ 可能比当前理论上允许的还要稀疏。}
}
\]

**状态：EXPERIMENTAL.**

---

## 10.3 Prefix-cut multiplicity counterexample

旧 exact-root-pair fibre 工作已经构造 repunit-style ambient examples，说明：

\[
\boxed{
\text{fixed word 的 cut fibre }\le2
\text{ 这个常数一般不能改成 }1.
}
\]

所以不应把 binary cut choice 当 presentation artifact 删除。

但它只是有限 bit，不是 infinity source。

**状态：PROVED ambient sharpness / inherited.**

---

# 11. Failed Routes Audit

## 11.1 “\(Q_0\) 与 \(g\) 是两个独立 infinity axes”

\[
\boxed{\text{FAILED.}}
\]

失败原因不是经验判断，而是 fixed-core finite fibre：

\[
g\to\infty\Longrightarrow Q_0\to\infty.
\]

本轮 generic log bound 更进一步否定了它们作为两个自由高度的图景。

---

## 11.2 “普通 square-spacing 单独靠 \(g\to\infty\) 足够”

\[
\boxed{\text{FAILED.}}
\]

已有

\[
\rho_{A_1}
=
10^{2g}
\frac{Q_{12}^2\mathcal N_{12}}{G^2A_{12}^2}
\left(
1+\frac{2b_3}{10^{m_3}Q_{12}}
\right)
\]

而 \(A_{12}\) 同步含 \(10^g\) growth，且

\[
\rho>\frac1{400}10^{-2k}.
\]

所以裸 \(g\)-large 不制造 near-square death。

失败类型：**fundamental for the bare \(g\)-large formulation**。

---

## 11.3 Naive Pell

\[
\boxed{\text{FAILED AS PRIMARY GEOMETRY.}}
\]

固定 moving coefficient state 后，真正的 translation equation 是 linear：

\[
S\mathfrak aX+\mathfrak b=0.
\]

standalone square gate是 cubic genus-one 型，而不是天然 Pell conic。

Pell 只可能在 square cubic 的特殊降阶/奇异 locus 上作为次级现象出现，而且还必须先落入 translation-flat state 才能保留 \(X\)-freedom。

失败类型：**previous formulation failure; possible resurrection only on a sharply defined degenerate locus.**

---

## 11.4 Generic resultant as terminal engine

\[
\boxed{\text{FAILED / REDUNDANT AS FRONTIER.}}
\]

已有 unified work 证明 resultant 只是两个必要 gate 的 elimination shadow；backward algebraic-denominator audit 还构造了 false-gluing，说明两个 quadratic/root conditions 可以同时成立而不对应同一合法 coefficient plane。

所以 resultant 适合压缩，不适合独立制造 terminal contradiction。

失败类型：**structural information-loss.**

---

## 11.5 Gaussian descent

\[
\boxed{\text{FAILED AS GLOBAL DESCENT.}}
\]

旧审计已明确：

- \(L>1\)：Gaussian flip 改变十进制 coefficient plane，离开原族；
- \(L=1\)：flip 退化为 projective identity，没有高度下降。

本轮的新结论不是复活 flip，而是把 Gaussian norm 只放到 flat radial defect

\[
P_1^2+P_2^2=(Q_0-P_3)(Q_0+P_3)
\]

上做**relative arithmetic analysis**。

失败类型：**fundamental for absolute descent; potentially recoverable as local norm invariant on \(\mathcal D_{\rm flat}\).**

---

## 11.6 Pure valuation / direct Hensel

\[
\boxed{\text{FAILED AS TOP-LEVEL STRATEGY SO FAR.}}
\]

现有 tail capacity 可以被 \(\widetilde\kappa\) 等项吸收，不能统一推出“模数大于 Archimedean 大小”。

而且 current A1 terminal language 已经把 root variables消掉。

但是在 \(\mathcal D_{\rm flat}\) 上，出现

\[
10^{m_2}\mid g_1Q_0,
\qquad
10^{n_3}\text{ 深入 }Q_0-P_3,
\]

因此 valuation 可能在**新坐标下**重新变得有效。

失败类型：**previous formulation failure, not a theorem that valuation can never work.**

---

## 11.7 Pure digit combinatorics

\[
\boxed{\text{FAILED AS GLOBAL TERMINATION ALONE.}}
\]

prefix convexity只给

\[
\le2
\]

而不是 zero；fixed-core finite fibre也只把问题推到 \(Q_0\to\infty\)。

失败类型：**uniqueness/finite-fibre is not emptiness.**

---

# 12. New Proven Statements

以下是本轮真正新增、可独立复核的命题。

## Theorem A1-TL — Translation-Line Theorem

对任意 A1 exact candidate，令

\[
\mathfrak a
=
h_1 10^{m_2}(P_1 10^k-Q_0)-Q_0h_2,
\]

\[
\mathfrak b
=
P_2h_2 10^{n_3}-h_3(Q_0-P_3).
\]

则

\[
\boxed{
10^{m_3}\mathfrak a+\mathfrak b=0.
}
\]

等价地，\(X=10^g\) 满足

\[
\boxed{
10^{n_3}\mathfrak a X+\mathfrak b=0.
}
\]

**状态：NEW PROVED.**

---

## Corollary A1-TL.1 — Generic uniqueness of decimal translation

若

\[
\mathfrak a\ne0,
\]

则固定

\[
(\mathcal P,\mathbf g;m_2,n_3,k)
\]

后，\(g\) 至多有一个可能值。

**状态：NEW PROVED.**

---

## Corollary A1-TL.2 — Exact ten-free synchronization

若 \(\mathfrak a\ne0\)，则

\[
\operatorname{core}_{10}(\mathfrak a)
=
\operatorname{core}_{10}(\mathfrak b),
\]

且

\[
v_2(\mathfrak b)-v_2(\mathfrak a)
=
v_5(\mathfrak b)-v_5(\mathfrak a)
=
m_3.
\]

**状态：NEW PROVED.**

---

## Theorem A1-LS — Generic Logarithmic Synchronization

若 \(\mathfrak a\ne0\)，则

\[
\boxed{
10^g
<
Q_0\left(
h_2+\frac{h_3}{10^{n_3}}
\right)
<
2Q_0^4.
}
\]

所以

\[
\boxed{
g<4\log_{10}Q_0+\log_{10}2.
}
\]

**状态：NEW PROVED.**

---

## Theorem A1-FL — Flat-Locus Double Decimal Absorption

若

\[
\mathfrak a=\mathfrak b=0,
\]

则

\[
g_2 10^{m_2}(P_1 10^k-Q_0)=g_1Q_0,
\]

\[
g_3P_2 10^{n_3}=g_2(Q_0-P_3),
\]

从而

\[
10^{m_2}<Q_0^2,
\qquad
10^{n_3}<Q_0,
\qquad
10^k\le1.1Q_0.
\]

**状态：NEW PROVED.**

---

## Corollary A1-FL.1 — Semantic Split-Resonance

flat locus 上：

\[
\boxed{
a_1 10^{m_2+k}=\mathcal R Q_{12},
}
\]

\[
\boxed{
a_2 10^{n_3}+a_3=\mathcal R b_3.
}
\]

因此完整 equality 分裂成 prefix 与 tail 两个独立 norm balances。

**状态：NEW PROVED.**

---

## Theorem A1-SQ — Translation-Square Geometry

固定

\[
(\mathcal P,\mathbf g;m_2,n_3,k)
\]

并令 \(X=10^g\)，则 deflated A1 square gate 可写成

\[
\boxed{
\varepsilon Y^2
=
X(a_\sigma X^2+b_\sigma X+c_\sigma),
\qquad
c_\sigma>0,
}
\]

其中系数由 (6.2)–(6.4) 显式给出。

generic nonsingular 情形是 genus-one cubic；但只要 \(\mathfrak a\ne0\)，translation line 已先固定 \(X\)。

**状态：NEW PROVED algebraic form + CONDITIONAL geometric classification.**

---

# 13. What This Does NOT Prove

本轮没有证明：

\[
A_1=\varnothing.
\]

没有证明：

\[
Q_0\gg1
\Longrightarrow
\text{A1 无候选}.
\]

没有证明：

\[
g\to\infty
\]

是每个 infinite A1 family 的必要条件。

没有证明 globally finite coefficient alphabet。

没有证明 \(\mathcal D_{\rm flat}\) 为空；小规模实验为零不能替代证明。

没有证明 generic \(g=O(\log Q_0)\) 本身足以造成 contradiction。

没有证明 square cubic 的 elliptic arithmetic 会自动关闭 flat locus。

---

# 14. Remaining Frontier

经过本轮后，A1 的 moving-family frontier 可以比原来更短地写成：

\[
\boxed{
\textbf{Moving primitive-core height }Q_0\to\infty
}
\]

下面只有两种宏观行为。

## Regime G — non-flat translation

\[
\mathfrak a\ne0.
\]

则

\[
\boxed{
\mathfrak b=-10^{m_3}\mathfrak a,
\qquad
g=O(\log Q_0).
}
\]

剩余问题不再是“控制任意大的 free \(g\)”；而是：

> moving primitive coefficients 能否长期制造两个来源不同的 integers \(\mathfrak a,\mathfrak b\)，使其 non-decimal core 完全相同，同时恰差一个巨大的 \(10\)-power？

这是一个明确的 coefficient synchronization problem。

---

## Regime F — flat translation

\[
\mathfrak a=\mathfrak b=0.
\]

则：

\[
m_2,n_3,k=O(\log Q_0),
\]

但 primitive-profile master equation 对 \(g\) 完全失明。

剩余问题变成：

> split-resonant prefix/tail balances 是否能与 exact word、reducedness、tail saturation、square cubic 和 primitive norm 同时成立？

这是真正适合集中攻击的 degenerate locus。

---

# 15. Recommended Next Campaign

只建议三个方向，按优先级排序。

## Priority 1 — Flat-Locus Elimination / Classification

目标：

\[
\boxed{\mathcal D_{\rm flat}}
\]

尤其研究

\[
g_2 10^{m_2}(P_1 10^k-Q_0)=g_1Q_0,
\]

\[
g_3P_2 10^{n_3}=g_2(Q_0-P_3),
\]

以及

\[
P_1^2+P_2^2=(Q_0-P_3)(Q_0+P_3).
\]

为什么优先：

- 它是唯一使 translation line 完全失去 \(g\) 控制的 locus；
- 小规模 ambient scan 未发现任何 \(\mathfrak a=0\)；
- 若证明 flat locus 空，则所有 A1 states 自动进入 \(g<4\log Q_0+O(1)\) 的 generic regime；
- 即使失败，也会得到 flat locus 的严格参数化，显著缩小后续 exact-recovery工作。

**成功收益：删除唯一真正的 translation-degenerate escape.**

---

## Priority 2 — Ten-Free Coefficient Synchronization

研究

\[
\boxed{
\mathfrak b=-10^{m_3}\mathfrak a
}
\]

的 prime-to-10 部分：

\[
\mathfrak a^{\langle10\rangle}
=
\mathfrak b^{\langle10\rangle}.
\]

尝试证明：

- \(\gcd(\mathfrak a,\mathfrak b)\) 有更小的 primitive-core 上界；
- 或二者的 non-decimal support 被不同 norm forms 控制；
- 或 normalized defects 的 projective separation 给出
  \[
  0<|\mathfrak b|<10^{m_3}
  \]
  型 contradiction；
- 或结合 reducedness 证明 \(v_2,v_5\) 的共同 jump 不可能等深。

为什么优先：

这是当前所有 non-flat A1 states 的统一必要条件，不需要按 cut、L、单个 prime 分支。

**成功收益：原则上可一次处理整个 generic A1 moving family.**

---

## Priority 3 — Flat Locus × Exact Word / Square Cubic Synchronization

若 Priority 1 不能直接杀死 flat locus，则只在 flat locus 内把：

\[
a_1 10^{m_2+k}=\mathcal R Q_{12},
\]

\[
a_2 10^{n_3}+a_3=\mathcal R b_3
\]

与：

- A1-WR；
- \(\gcd(a_i,b_i)=1\)；
- saturated \(L=1\) / nonsaturated \(L>1\)；
- square cubic
  \[
  \varepsilon Y^2=X(aX^2+bX+c)
  \]
  联立。

这里才值得检查：

- conic degeneration；
- elliptic/singular cubic；
- Gaussian norm；
- \(2,5\)-adic depth；
- relative descent。

为什么排第三：

在 translation line 尚未退化时，这些几何都只是 point test；只有 flat locus 里它们才真正承担控制 \(g\) 的职责。

**成功收益：关闭唯一仍可能拥有 genuine translation fibre 的状态。**

---

# 16. Final Assessment

本轮最初的问题是：

\[
\text{decimal translation }10^g
\text{ 与 primitive height }Q_0
\text{ 能否长期同步？}
\]

现在可以给出一个明显更精确的答案：

\[
\boxed{
\begin{gathered}
\textbf{A1 不是一个有两个独立高度 }(Q_0,g)\textbf{ 的问题。}\\[2mm]
\textbf{唯一 top-level infinity source 是 }Q_0\to\infty.\\[2mm]
\textbf{在所有非退化状态中，}
\quad
g<4\log_{10}Q_0+\log_{10}2.\\[2mm]
\textbf{decimal translation 因而被强制与 primitive height 对数同步。}\\[2mm]
\textbf{唯一使这种同步失效的粗代数 locus 是}\\
\mathfrak a=\mathfrak b=0,
\textbf{ 即 split-resonant flat locus。}
\end{gathered}
}
\]

所以 A1 的下一阶段不应继续问：

> “还能给 \(g\) 找什么局部同余？”

而应问：

\[
\boxed{
\textbf{为什么 moving primitive core 能或不能长期维持}
\quad
\mathfrak b=-10^{m_3}\mathfrak a?
}
\]

以及更尖锐地：

\[
\boxed{
\textbf{flat split-resonance }
\mathfrak a=\mathfrak b=0
\textbf{ 是否根本不可能？}
}
\]

这两个问题已经比原先的 A1 case tree 明显更小。

---

# 17. Source / Provenance Ledger

本报告主要依赖并审计以下文件：

1. `strict_layer_post_DD_consolidation_A1_frontier.md`
   - SGR-10B；
   - DD 已从 strict frontier 删除；
   - A1 exact word normal form；
   - fixed \((T,\mathbf A)\) cut fibre \(\le2\)；
   - fixed-core finite fibre 的 A1 interpretation；
   - \(g,k_{12}\) 不是独立 infinity source。

2. `strict_layer_unified_exact_lift_campaign.md`
   - primitive normalization；
   - \(q=V,\ y_i=UP_i,\ H=UQ_0\)；
   - primitive-profile master equation；
   - gcd profile / \(h_i\)；
   - SGR depth gate 与 Exact square gate 的统一坐标。

3. `strict_layer_moving_core_square_spacing_campaign.md`
   - A1 square / \(10\times\)square deflation；
   - \(\varepsilon M^2-E=\varepsilon Y^2\)；
   - \(g\to\infty\not\Rightarrow\rho\to0\)；
   - \(\rho>\frac1{400}10^{-2k_{12}}\)；
   - resultant root spacing不产生新信息。

4. `strict_layer_backward_denominator_decimal_interface.md`
   - A1 effective tail \(\ell=n_3\)；
   - \((b_3,S)\mapsto(\eta_3,L,\tau)\)；
   - tail normalization 是 derived trace。

5. `strict_layer_backward_exact_root_pair_fibre_campaign.md`
   - one-word collapse；
   - prefix weighted norm；
   - strict discrete convexity；
   - fixed word cut fibre \(\le2\)；
   - binary multiplicity 的 ambient sharpness。

6. `strict_layer_backward_algebraic_denominator_interface.md`
   - quadratic/root false-gluing；
   - coefficient plane 保留额外信息；
   - generic resultant 不应冒充 exact recovery。

7. `exact_lift_research_synthesis_2026-08-10.md`
   - 仅使用经后续审计仍有效的 A1 历史输入：
     - saturated \(L=1\) 的 denominator-only tail bound；
     - saturated residual odd-prime support restriction；
     - Gaussian flip 的 coefficient-plane failure；
     - naive local/Legendre/resultant 路线的失败原因。
   - 不使用其中已被撤回的旧 A1 closure。

8. `strict_layer_DD_oriented_tail_window_campaign.md`
   - 仅用于冻结
     \[
     DD=\varnothing.
     \]
   - 本报告没有迁移任何 DD closure 技术。

---

**本轮最终状态：**

- **NEW PROVED:** A1 translation-line theorem；
- **NEW PROVED:** generic \(g<4\log_{10}Q_0+\log_{10}2\)；
- **NEW PROVED:** ten-free coefficient synchronization；
- **NEW PROVED:** flat-locus double decimal absorption；
- **NEW PROVED:** flat semantic split-resonance；
- **NEW PROVED:** A1 square gate 的 \(X\)-cubic rewrite；
- **EXPERIMENTAL:** \(Q_0\le300\) ambient flat scan 无 hit；
- **FAILED:** \((Q_0,g)\) 两独立 infinity axes；
- **FAILED:** bare \(g\)-large square-spacing；
- **FAILED AS PRIMARY GEOMETRY:** naive Pell；
- **OPEN:** flat locus 是否为空；
- **OPEN:** generic ten-free synchronization 是否可 uniform contradiction；
- **OPEN:** A1 closure。
