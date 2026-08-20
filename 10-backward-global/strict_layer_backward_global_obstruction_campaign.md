# 三项十进制拼接平方和问题：Backward Strict Layer 全局恢复障碍框架

**文件名：** `strict_layer_backward_global_obstruction_campaign.md`  
**轮次：** Backward Strict Layer — Round 1  
**研究目标：** 从“一个 strict-layer state 必须能够被 Exact-Lift 完整恢复成原题候选”这一终端出发，建立全局、反向、非分支化的 obstruction calculus。  
**责任边界：** 本报告不推进 SGR primitive-core 正向归约、不研究 fixed-core finite fibre、不研究 SGR depth quadratic、不研究 resultant / square-spacing coupling、不研究 moving primitive-core termination，也不单攻 \(A_2\)、DD、\(A_1\) 任一 chamber。

---

# 0. Executive summary

本轮最重要的结论不是新的局部分支无解，而是把“反方向”严格化为一个**完成纤维（completion fibre）**问题。

给定一个抽象 strict-layer state \(\xi\)，不把它预先当作原题候选。令

\[
\mathfrak C_{\mathrm{full}}(\xi)
\]

表示所有与 \(\xi\) 相容、并能恢复出六个正整数块

\[
(a_i,b_i)_{i=1}^3
\]

且满足原题全部条件的完整 witness 集合。定义

\[
\boxed{
\xi\ \text{Liftable}
\iff
\mathfrak C_{\mathrm{full}}(\xi)\neq\varnothing.
}
\]

于是 backward strict layer 的基本对象不是“把一个必要条件倒过来”，而是寻找可检验条件 \(B\)，使

\[
\boxed{
B(\xi)\Longrightarrow
\mathfrak C_{\mathrm{full}}(\xi)=\varnothing.
}
\]

这就是严格意义上的 obstruction。

本轮得到以下全局框架。

## 0.1 核心结构

恢复逻辑应分成两层：

### A. Exact recovery spine

这是由原题本身和审计后的双向恢复定理定义的真正恢复主干：

\[
\boxed{
\text{integer sphere witness}
\to
\text{canonical denominator recovery}
\to
\text{reduced decimal blocks}
\to
\text{digit-cell realization}
\to
\text{exact concatenation plane}.
}
\]

其中最关键的终端事实是 T3：若

\[
x_1^2+x_2^2+x_3^2=t^2,
\qquad
d_i=\gcd(x_i,L),
\]

\[
a_i=\frac{x_i}{d_i},
\qquad
b_i=\frac{L}{d_i},
\]

并满足规范化条件

\[
\gcd(x_1,x_2,x_3,L)=1
\]

以及精确拼接恒等式

\[
\boxed{
L\,\operatorname{concat}(a_1,a_2,a_3)
=
t\,\operatorname{concat}(b_1,b_2,b_3),
}
\]

则恢复出的 \((a_i,b_i)\) 是原题完整候选；反向亦成立。  
因此“完整可提升性”有一个真正的全局等价终端，而不只是若干必要条件的并列。

### B. Derived obstruction certificates

Exact-Lift 后续得到的

- primitive recovery gcd；
- denominator prime graph；
- gap quadratic；
- discriminant square；
- rational-root divisibility；
- primitive tail quadratic；
- \(10^\ell\mid\kappa^2(\kappa+2G)\)；
- \(2\)-adic / \(5\)-adic capacity；
- digit window；
- Gaussian prime allocation；

都应理解为从完整恢复主干投影出的**必要证书**。

它们非常适合反向使用其逆否命题：

\[
\boxed{
\text{必要证书不可能实现}
\Longrightarrow
\text{not liftable}.
}
\]

但它们一般不能反过来作为完整恢复的充分条件。

---

## 0.2 本轮新的逻辑原则

### NEW PROVED — Completion-fibre obstruction principle

若已经严格证明

\[
\operatorname{Liftable}(\xi)
\Longrightarrow
\exists c\in\mathcal C(\xi)\quad P(c),
\]

那么严格 obstruction 是

\[
\boxed{
\{c\in\mathcal C(\xi):P(c)\}=\varnothing
\Longrightarrow
\text{not liftable}.
}
\]

**只排除某一个辅助根、某一个符号选择、某一个局部 prime allocation，不足以推出 non-liftability。**

这条量词纪律是 backward strict layer 的基本安全规则。

### NEW PROVED — “最弱 obstruction”不存在非平凡规范最小元

若

\[
B_1\Longrightarrow\text{not liftable},
\qquad
B_2\Longrightarrow\text{not liftable},
\]

则

\[
B_1\lor B_2
\Longrightarrow
\text{not liftable},
\]

而 \(B_1\lor B_2\) 比 \(B_1,B_2\) 都更弱。继续取并可以不断扩大死亡区域。

因此，除非直接取

\[
\boxed{\text{not liftable}}
\]

本身，否则“最弱充分 obstruction”没有天然唯一答案。

所以本报告把“minimal obstruction basis”解释为：

> **相对于当前恢复塔与当前已证证书，寻找不被其他已知 obstruction 家族吸收的少数生成机制。**

---

## 0.3 当前建议的 minimal obstruction basis

当前最可信的全局 basis 不是 near-square / near-\(S\)-unit / Hensel 等局部现象，而是三个更深的恢复失败家族：

\[
\boxed{
\mathfrak B_{\mathrm{back}}
=
\left\{
B_{\mathrm{arith}},
B_{\mathrm{root}},
B_{\mathrm{dec}}
\right\}.
}
\]

其中：

1. \(\boxed{B_{\mathrm{arith}}}\)：**canonical arithmetic recovery failure**  
   公共分母、逐坐标 gcd、最小公分母、prime-power allocation、denominator core / prime graph 无法同时实现。

2. \(\boxed{B_{\mathrm{root}}}\)：**admissible algebraic-root failure**  
   Exact-Lift 消元后的恢复二次式不存在符合有理性、符号、约分分子/分母要求的 admissible rational root。

3. \(\boxed{B_{\mathrm{dec}}}\)：**decimal synchronization failure**  
   即使 arithmetic skeleton 与 algebraic root 各自存在，也不存在同一个 witness 同时满足十进制 tail、\(2/5\)-adic capacity、digit window、逐项既约和原始 coefficient plane / concatenation identity。

这是**相对当前证明库的 basis**，不是宣称三者在更深理论上绝对独立。

---

## 0.4 Backward interface

未来正向线若想把 reachable state 撞入反向死亡区域，不需要把整套 SGR 变量全部传入本体系。

本报告建议的最小接口是 recovery signature

\[
\boxed{
\Xi_{\mathrm{back}}
=
\left(
\Gamma_{\mathrm{arith}},
\mathscr Q_{\mathrm{rec}},
\mathcal A_{\mathrm{root}},
\Theta_{10},
\Pi_{\mathrm{dec}}
\right).
}
\]

其中：

- \(\Gamma_{\mathrm{arith}}\)：公共分母 / gcd / prime-support / valuation profile；
- \(\mathscr Q_{\mathrm{rec}}\)：实际 Exact-Lift recovery polynomial（允许二次式退化为一次式）；
- \(\mathcal A_{\mathrm{root}}\)：根必须满足的正性、约分分子分母、区间与符号 admissibility；
- \(\Theta_{10}\)：十进制 tail demand 与 \(2,5\)-adic supply；
- \(\Pi_{\mathrm{dec}}\)：digit-cell 与 exact concatenation coefficient-plane 数据。

该接口不含 SGR depth quadratic、resultant、moving-core height，因而与正向工作区严格去重。

---

# 1. 来源审计与责任边界

## 1.1 实际核对的来源

本轮重点读取并交叉检查：

- `exact_lift_research_synthesis_2026-08-10.md`；
- `strict_layer_final_campaign.md`；
- `proved_results_report_v3.md`；
- `final_results_index.md`；
- `strict_layer_unified_exact_lift_campaign.md`，仅用于划定 anti-duplication boundary。

对恢复逻辑，本报告优先使用审计后的全局基础 T1–T4，尤其是 T3 的双向公共分母重构，而不是把 Exact-Lift synthesis 中所有“recovery”字样都自动视为 equivalence。

## 1.2 已明确排除的旧错误

`exact_lift_research_synthesis_2026-08-10.md` 已明确撤回早期预印本中若干“完整关闭”论证，包括：

- 完全共享分母结构 \(\not\Rightarrow\) 自动矛盾；
- 有限证书 \(\not\Rightarrow\) 无界下降；
- “素数同时进入 gap 与二平方和” \(\not\Rightarrow\) 自动矛盾；
- 旧 \(A_1\) “两个 gap 尺度不相容”缺乏逐行可核验矛盾；
- Gaussian flip 不保持原十进制 coefficient plane，因此不能作为合法全局下降。

这些旧路线**不进入**本报告 obstruction ledger。

## 1.3 与正向 SGR 线的硬边界

本报告不使用下列内容制造新证明：

- primitive-core 全局归约；
- \(q=V,\ y_i=UP_i,\ H=UQ_0\) 的变量字典；
- fixed primitive core finite fibre；
- SGR depth quadratic；
- SGR gate × Exact discriminant 的 resultant；
- moving primitive-core uniform termination。

本轮唯一允许引用 `strict_layer_unified_exact_lift_campaign.md` 的目的，是确认这些已经属于另一条研究线。

---

# 2. Complete liftability 的严格定义

## 2.1 Canonical complete witness

定义一个 canonical complete witness

\[
\mathcal W
=
(x_1,x_2,x_3,t,L)
\in\mathbf Z_{>0}^5
\]

满足

\[
\boxed{
x_1^2+x_2^2+x_3^2=t^2.
}
\tag{2.1}
\]

令

\[
d_i=\gcd(x_i,L),
\]

并恢复

\[
\boxed{
a_i=\frac{x_i}{d_i},
\qquad
b_i=\frac{L}{d_i}.
}
\tag{2.2}
\]

要求 canonical minimality

\[
\boxed{
\gcd(x_1,x_2,x_3,L)=1.
}
\tag{2.3}
\]

由 T3，(2.3) 等价于恢复后的

\[
L=\operatorname{lcm}(b_1,b_2,b_3).
\]

并且 (2.2) 自动给出

\[
\gcd(a_i,b_i)=1.
\]

最后令

\[
A=\operatorname{concat}(a_1,a_2,a_3),
\qquad
B=\operatorname{concat}(b_1,b_2,b_3).
\]

要求 exact decimal balance

\[
\boxed{
LA=tB.
}
\tag{2.4}
\]

### PROVED — T3 terminal equivalence

(2.1)–(2.4) 与正整数块条件一起，构成原题解存在性的双向恢复判别。

因此它是 backward framework 的真正终端，不需要借助 \(A_2/DD/A_1\) 才成立。

---

## 2.2 Partial strict state

一个 abstract strict-layer state \(\xi\) 可以只固定上述 witness 的一部分信息，例如：

- 某些 \(x_i,t,L\)；
- gcd / valuation profile；
- 已恢复的部分 \(a_i,b_i\)；
- 位数向量；
- Exact-Lift recovery polynomial；
- tail demand；
- prime-support data。

记

\[
\mathfrak W(\xi)
\]

为所有与 \(\xi\) 相容的正整数扩张 witness。

定义

\[
\boxed{
\operatorname{Liftable}(\xi)
\iff
\exists\mathcal W\in\mathfrak W(\xi)
\text{ 满足 (2.1)--(2.4) 及 strict-layer digit cell}.
}
\tag{2.5}
\]

定义

\[
\boxed{
\operatorname{NonLiftable}(\xi)
\iff
\mathfrak C_{\mathrm{full}}(\xi)=\varnothing.
}
\tag{2.6}
\]

这一定义故意不依赖任何特定 carrier chamber。

---

# 3. Recovery gate DAG：主干与投影必须分开

恢复系统有两种不同意义的“gate”。

## 3.1 Exact spine gates

### \(\mathcal G_{\mathrm{Sph}}\) — integer sphere gate

\[
x_1^2+x_2^2+x_3^2=t^2.
\]

- **性质：** 原题必要；作为 canonical witness 定义的一部分。
- **全局性：** genuinely global。
- **失败：** 立即 non-liftable。

### \(\mathcal G_{\mathrm{Can}}\) — canonical denominator recovery

\[
d_i=\gcd(x_i,L),
\quad
a_i=x_i/d_i,
\quad
b_i=L/d_i,
\]

并要求

\[
\gcd(x_1,x_2,x_3,L)=1.
\]

- **性质：** T3 中的 exact recovery。
- **全局性：** genuinely global。
- **作用：** 自动恢复逐项既约性与最小公共分母。
- **失败：** canonical lift 不存在。

### \(\mathcal G_{\mathrm{Dig}}\) — decimal cell realization

恢复的 \(a_i,b_i\) 必须属于 state 指定的十进制位数格：

\[
10^{n_i-1}\le a_i<10^{n_i},
\qquad
10^{m_i-1}\le b_i<10^{m_i}.
\]

- **性质：** 原题定义性要求；单独既非充分也非深层算术定理。
- **全局性：** global，具体窗口参数可依 state。

### \(\mathcal G_{\mathrm{Bal}}\) — exact concatenation plane

\[
\boxed{
L\,\operatorname{concat}(a_1,a_2,a_3)
=
t\,\operatorname{concat}(b_1,b_2,b_3).
}
\]

- **性质：** 与 \(\mathcal G_{\mathrm{Sph}}+\mathcal G_{\mathrm{Can}}\) 联立时构成 T3 的终端双向恢复。
- **全局性：** genuinely global。
- **重要性：** 这是“coefficient plane compatibility”的最终准确版本，而不是某个近似平面或变换后的平面。

---

## 3.2 Derived certificate gates

这些不是恢复主干的等价层，而是完整候选必须通过的投影测试。

### \(\mathcal C_{\mathrm{gcd}}\) — primitive recovery gcd

Exact-Lift 中

\[
\boxed{
\gcd(q,y_i)=\frac{q}{b_i}.
}
\]

- **性质：** 精确恢复恒等式。
- **单独强度：** 不足以恢复原题。
- **失败：** non-liftable。

### \(\mathcal C_{\mathrm{prime}}\) — denominator core / prime graph

已证全局必要结构包括：

- \(2\)-进最大赋值位置受严格限制；
- denominator core \(N_L\) 为奇数；
- \(p\mid N_L\Rightarrow p\equiv1\pmod4\)；
- 核素数最大赋值按特定 pair-max 模式出现；
- Exact-Lift 的 denominator prime graph 对 unique-max / pair-max 给出进一步必要结构。

- **性质：** necessary only。
- **失败：** non-liftable。
- **通过：** 绝不代表可恢复。

### \(\mathcal C_{\mathrm{root}}\) — exact rational-root gate

三个 Exact-Lift chamber 在统一正规化后都产生 recovery quadratic。典型 gap quadratic 为

\[
D(\kappa+2G)\mu^2
-2G\kappa C\,\mu\nu
+\kappa D\mathcal N_{12}\nu^2
=0,
\qquad
\gcd(\mu,\nu)=1.
\tag{3.1}
\]

以及 primitive tail quadratic

\[
-\kappa(\kappa+2G)z_3^2
+
2G^2LC\,z_3
+
\mathcal C_3
=0.
\tag{3.2}
\]

这里

\[
z_3=\frac{a_3}{\delta_3}
\]

一般是既约有理数，不应默认为整数。

- **性质：** 对完整候选是必要。
- **全局性：** 三 chamber 共有同一 schema，但具体 \((C,D,\ell)\) 的定义带 branch normalization。
- **失败：** non-liftable。

### \(\mathcal C_{\square}\) — discriminant square

对非退化二次式

\[
AX^2+BX+C=0,
\qquad A,B,C\in\mathbf Z,\ A\ne0,
\]

有

\[
\boxed{
\exists X\in\mathbf Q
\iff
B^2-4AC
\text{ 是整数平方}.
}
\tag{3.3}
\]

因此在“只问是否存在某个有理根”的层次，discriminant-square 与 rational-root existence 是等价的。

但 Exact-Lift 还要求根满足：

- 正性；
- 指定 reduced denominator；
- 指定 numerator / denominator divisibility；
- digit / tail admissibility。

故

\[
\boxed{
\text{discriminant square}
\not\Rightarrow
\text{complete recovery}.
}
\]

### \(\mathcal C_{\mathrm{RRT}}\) — rational-root divisibility

由 (3.1) 的本原性：

\[
\boxed{
\nu\mid D(\kappa+2G),
\qquad
\mu\mid\kappa D\mathcal N_{12}.
}
\tag{3.4}
\]

由 (3.2) 与

\[
z_3=a_3/\delta_3
\]

既约，得到

\[
\boxed{
\delta_3\mid\kappa(\kappa+2G),
\qquad
a_3\mid\mathcal C_3.
}
\tag{3.5}
\]

- **性质：** necessary only。
- **失败：** algebraic-root recovery 失败。
- **通过：** 不保证判别式平方，也不保证存在 admissible root。

### \(\mathcal C_{10}\) — denominator-tail certificate

利用

\[
10^\ell=\delta_3L,
\qquad
L\mid\kappa,
\]

以及 (3.5)，得到

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G).
}
\tag{3.6}
\]

这是一条非常干净的全局 tail certificate。

- **性质：** necessary only。
- **逻辑来源：** rational-root denominator recovery + decimal tail decomposition 的投影。
- **因此：** 它不是一个与 root / decimal recovery 完全独立的基本机制。

---

# 4. 一个严格的 nested completion-fibre calculus

为避免把“gate”误写成一串单向蕴含，定义嵌套完成纤维。

\[
\mathfrak C_0(\xi)=\mathfrak W(\xi).
\]

\[
\mathfrak C_{\mathrm{Sph}}(\xi)
=
\{
\mathcal W\in\mathfrak C_0(\xi):
\mathcal G_{\mathrm{Sph}}
\}.
\]

\[
\mathfrak C_{\mathrm{Can}}(\xi)
=
\{
\mathcal W\in\mathfrak C_{\mathrm{Sph}}(\xi):
\mathcal G_{\mathrm{Can}}
\}.
\]

\[
\mathfrak C_{\mathrm{Dig}}(\xi)
=
\{
\mathcal W\in\mathfrak C_{\mathrm{Can}}(\xi):
\mathcal G_{\mathrm{Dig}}
\}.
\]

\[
\mathfrak C_{\mathrm{Bal}}(\xi)
=
\{
\mathcal W\in\mathfrak C_{\mathrm{Dig}}(\xi):
\mathcal G_{\mathrm{Bal}}
\}.
\]

于是

\[
\boxed{
\mathfrak C_{\mathrm{Bal}}
\subseteq
\mathfrak C_{\mathrm{Dig}}
\subseteq
\mathfrak C_{\mathrm{Can}}
\subseteq
\mathfrak C_{\mathrm{Sph}}
\subseteq
\mathfrak C_0.
}
\tag{4.1}
\]

并由 T3：

\[
\boxed{
\operatorname{Liftable}(\xi)
\iff
\mathfrak C_{\mathrm{Bal}}(\xi)\ne\varnothing.
}
\tag{4.2}
\]

因此任意一层出现空纤维：

\[
\boxed{
\mathfrak C_j(\xi)=\varnothing
\Longrightarrow
\operatorname{NonLiftable}(\xi).
}
\tag{4.3}
\]

这就是 backward obstruction calculus 的主骨架。

---

# 5. Backward obstruction DAG

下面只记录**严格可用的死亡箭头**。

\[
\boxed{
\begin{array}{ccccc}
\text{canonical gcd impossible}
&\Longrightarrow&
B_{\mathrm{arith}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
\text{prime graph/core violated}
&\Longrightarrow&
B_{\mathrm{arith}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
\Delta_{\mathrm{rec}}\ \text{not square}
&\Longrightarrow&
B_{\mathrm{root}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
\text{all rational roots violate admissibility}
&\Longrightarrow&
B_{\mathrm{root}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
\text{RRT numerator/denominator capacity fails}
&\Longrightarrow&
B_{\mathrm{root}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
10^\ell\nmid\kappa^2(\kappa+2G)
&\Longrightarrow&
B_{\mathrm{dec}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
\text{digit cell empty}
&\Longrightarrow&
B_{\mathrm{dec}}
&\Longrightarrow&
\text{not liftable}
\\[1mm]
\text{no single witness satisfies exact coefficient plane}
&\Longrightarrow&
B_{\mathrm{dec}}
&\Longrightarrow&
\text{not liftable}.
\end{array}
}
\tag{5.1}
\]

---

## 5.1 \(2/5\)-adic capacity 与 tail divisibility 是同一 obstruction 的坐标形式

令

\[
K_{\mathrm{tail}}
=
\kappa^2(\kappa+2G).
\]

则

\[
10^\ell\mid K_{\mathrm{tail}}
\]

等价于同时满足

\[
v_2(K_{\mathrm{tail}})\ge\ell,
\qquad
v_5(K_{\mathrm{tail}})\ge\ell.
\tag{5.2}
\]

因此

\[
\boxed{
10^\ell\nmid K_{\mathrm{tail}}
\iff
\left[v_2(K_{\mathrm{tail}})<\ell\right]
\lor
\left[v_5(K_{\mathrm{tail}})<\ell\right].
}
\tag{5.3}
\]

### NEW PROVED

所谓“\(2\)-adic capacity obstruction”和“\(5\)-adic capacity obstruction”不是两个独立 obstruction basis 元素；它们只是同一十进制 tail-divisibility obstruction 的两个坐标投影。

---

## 5.2 discriminant square 与 rational-root gate 的压缩

对于非退化整系数二次式，

\[
\boxed{
\Delta\text{ 非平方}
\iff
\text{不存在任何有理根}.
}
\]

因此在纯 algebraic-root existence 层：

\[
\boxed{
\text{discriminant-square}
\quad\text{与}\quad
\text{rational-root existence}
}
\]

应合并为同一个 gate。

但以下条件仍然额外存在：

\[
\text{root exists}
\not\Rightarrow
\text{root has required reduced denominator / sign / digit window}.
\]

所以 rational-root theorem 的 divisibility 与 decimal admissibility 不能被判别平方吸收。

---

## 5.3 denominator-tail obstruction 不是新的独立本体

(3.6) 的证明链是：

\[
\text{admissible reduced tail root}
\]

\[
\Longrightarrow
\delta_3\mid\kappa(\kappa+2G)
\]

再与

\[
10^\ell=\delta_3L,
\qquad
L\mid\kappa
\]

合并得到

\[
10^\ell\mid\kappa^2(\kappa+2G).
\]

因此 tail obstruction 的位置应画成

\[
\boxed{
B_{\mathrm{root}}
+
\text{decimal tail realization}
\Longrightarrow
\mathcal C_{10}.
}
\]

其失败是非常有效的死亡证书，但它在结构上是 root recovery 与 decimal embedding 的交叉投影，而不是第四个独立 basis。

---

# 6. obstruction dominance / redundancy

## 6.1 已严格确认的冗余

### R1. discriminant square 与“存在某个有理根”

非退化二次式层面等价，可合并。

### R2. \(2\)-adic / \(5\)-adic tail capacity

由 (5.3) 精确合并为一个 \(10^\ell\)-divisibility obstruction。

### R3. rational-root divisibility

是 admissible root existence 的必要投影，不应独立提升为“完整恢复 gate”。

### R4. near-\(S\)-unit

目前只有在它进一步推出：

- tail divisibility failure；
- prime-allocation impossibility；
- 或精确 spacing contradiction

时才成为 obstruction。

“接近 \(S\)-unit”本身不是死亡条件。

### R5. near-square

同理，只有当它严格推出

\[
\Delta_{\mathrm{rec}}\ \text{不是平方}
\]

或其他 exact root impossibility 时，才进入 \(B_{\mathrm{root}}\)。

near-square 本身不是 basis 元素。

---

## 6.2 不能升级为 state obstruction 的“方法失败”

### Gaussian flip 离开 coefficient plane

已证事实是：flip 通常不保持原十进制 coefficient plane。

严格结论是：

\[
\boxed{
\text{该 flip 不能作为合法 descent map}.
}
\]

不能写成：

\[
\boxed{
\text{原 state 因此 not liftable}.
}
\]

除非未来证明：

> 原 state 的**所有**恢复 witness 都必然落在错误 coefficient plane。

### “模数大于区间”

已知

\[
M>|I|
\]

只能推出某 congruence class 在区间中至多有一个代表。

它只给

\[
\boxed{\text{uniqueness}}
\]

而不自动给

\[
\boxed{\text{emptiness}}.
\]

因此它是未来 synchronization obstruction 的组件，不是现成死亡证书。

---

## 6.3 当前仍无法证明的 dominance

目前没有严格定理证明：

\[
B_{\mathrm{arith}}
\Longrightarrow
B_{\mathrm{root}},
\]

或

\[
B_{\mathrm{root}}
\Longrightarrow
B_{\mathrm{dec}},
\]

或任意反向包含。

`strict_layer_final_campaign.md` 的 N2–N3 已证明：仅靠现有位数尺度 / 连续 Archimedean gap 无法形成统一正间隙。

同一报告的 N4–N5 又证明：当前 denominator-core 的局部 prime-position 条件对所有位置模式仍可相容。

因此至少就**当前已知工具**而言：

- 纯 decimal/Archimedean geometry 不能吞掉 arithmetic obstruction；
- 纯局部 valuation-position geometry 也不能吞掉 decimal/global synchronization obstruction。

这支持保留至少两个不同信息通道。

至于 \(B_{\mathrm{root}}\) 是否最终能被某个更深的 arithmetic-decimal synchronization theorem 吸收，目前是 **OPEN**。

---

# 7. Minimal obstruction basis

## 7.1 相对当前证明库的 basis

定义：

\[
\boxed{
\mathfrak B_{\mathrm{back}}
=
\{
B_{\mathrm{arith}},
B_{\mathrm{root}},
B_{\mathrm{dec}}
\}.
}
\tag{7.1}
\]

### \(B_{\mathrm{arith}}\)：canonical arithmetic recovery failure

包括：

- canonical common denominator 不存在；
- \(\gcd(x_1,x_2,x_3,L)=1\) 不能实现；
- primitive recovery gcd 不一致；
- denominator core 必要结构失败；
- prime graph / prime-power allocation 失败；
- Gaussian-active prime allocation 与 reducedness 冲突。

其统一语义不是某一条同余，而是：

\[
\boxed{
\text{不存在满足全部 canonical denominator / prime-demand 条件的 arithmetic witness}.
}
\]

### \(B_{\mathrm{root}}\)：admissible algebraic-root failure

包括：

- nondegenerate recovery quadratic 判别式非平方；
- 退化一次式无 admissible root；
- 有理根存在但所有根都违反正性 / sign；
- 所有根都违反 reduced numerator / denominator requirements；
- rational-root theorem capacity 不足。

统一语义：

\[
\boxed{
\mathscr R_{\mathrm{alg}}(\xi)=\varnothing,
}
\]

其中 \(\mathscr R_{\mathrm{alg}}(\xi)\) 是所有 algebraically admissible recovery roots。

### \(B_{\mathrm{dec}}\)：decimal synchronization failure

包括：

- \(10^\ell\) tail demand 超过 \(2/5\)-adic supply；
- root denominator 无法与 decimal tail split 对接；
- digit window 无交；
- local congruence roots 无法由同一个全局整数 / 有理数实现；
- 唯一 CRT representative 不在真实 digit interval；
- recovered root 无法满足 exact coefficient plane；
- 原始 concatenation identity 失败。

统一语义：

\[
\boxed{
\mathscr R_{\mathrm{alg}}(\xi)
\cap
\mathscr R_{\mathrm{decimal}}(\xi)
=
\varnothing.
}
\]

---

## 7.2 为什么暂不进一步压成两个 basis 元素？

最诱人的压缩是：

\[
B_{\mathrm{root}}+B_{\mathrm{dec}}
\rightsquigarrow
B_{\mathrm{sync}}.
\]

从语义上当然可以定义

\[
B_{\mathrm{sync}}
=
\{
\text{no root survives all decimal recovery}
\}.
\]

但这样只是把两个问题换了名字，没有得到可计算的新定理。

当前仍有实质不同的信息：

- discriminant square / rational root 是 algebraic existence；
- tail / digit / exact coefficient plane 是 decimal embedding。

因此本轮不把它们虚假统一。

---

# 8. Backward interface state \(\Xi_{\mathrm{back}}\)

未来正向线不需要把完整内部状态复制给反向线。只需提供足够判断死亡证书的 recovery signature。

定义

\[
\boxed{
\Xi_{\mathrm{back}}
=
\left(
\Gamma_{\mathrm{arith}},
\mathscr Q_{\mathrm{rec}},
\mathcal A_{\mathrm{root}},
\Theta_{10},
\Pi_{\mathrm{dec}}
\right).
}
\tag{8.1}
\]

## 8.1 \(\Gamma_{\mathrm{arith}}\)

记录：

- canonical common denominator candidate；
- 逐坐标 gcd profile；
- 对每个相关素数 \(p\) 的
  \[
  (v_p(b_1),v_p(b_2),v_p(b_3));
  \]
- denominator-core support；
- 必要的 Gaussian / norm allocation labels。

它只服务于 arithmetic recoverability，不需要 primitive-core height。

## 8.2 \(\mathscr Q_{\mathrm{rec}}\)

记录实际恢复所需的有限个一元 polynomial：

\[
\mathscr Q_{\mathrm{rec}}
=
\{
Q_{\mathrm{gap}},
Q_{\mathrm{tail}},
\ldots
\}.
\]

对二次式只需保存：

\[
(A,B,C)
\]

及退化标志。

这样可以直接判断：

- discriminant square；
- rational roots；
- reduced denominator capacity。

## 8.3 \(\mathcal A_{\mathrm{root}}\)

记录 root admissibility：

- \(X>0\) 或其他 sign；
- admissible interval；
- reduced numerator/denominator demand；
- root 与原 block variable 的恢复公式。

这一步防止把“存在某个有理根”误写成“存在原题 root”。

## 8.4 \(\Theta_{10}\)

建议压缩成

\[
\boxed{
\Theta_{10}
=
(\ell,c_2,c_5,\text{tail-split data}),
}
\]

其中

\[
c_p
=
v_p\!\left(\kappa^2(\kappa+2G)\right),
\qquad
p=2,5.
\]

于是 tail death test 只需读：

\[
\boxed{
\ell>\min(c_2,c_5)
\Longrightarrow
\text{not liftable}.
}
\tag{8.2}
\]

## 8.5 \(\Pi_{\mathrm{dec}}\)

记录：

- \((n_i,m_i)\) digit cell；
- block recovery affine/rational maps；
- exact coefficient-plane residual所需数据；
- 必要的 global congruence / CRT class；
- original concatenation check。

它的终端任务是判断：

\[
\boxed{
\exists r\in\mathscr R_{\mathrm{alg}}
\text{ simultaneously satisfying every decimal condition?}
}
\]

---

# 9. Death region \(\mathcal D\)

定义：

\[
\boxed{
\mathcal D
=
\mathcal D_{\mathrm{arith}}
\cup
\mathcal D_{\mathrm{root}}
\cup
\mathcal D_{\mathrm{dec}}.
}
\tag{9.1}
\]

其中：

\[
\mathcal D_{\mathrm{arith}}
=
\{
\Xi:
\text{canonical arithmetic witness set empty}
\},
\]

\[
\mathcal D_{\mathrm{root}}
=
\{
\Xi:
\mathscr R_{\mathrm{alg}}=\varnothing
\},
\]

\[
\mathcal D_{\mathrm{dec}}
=
\{
\Xi:
\mathscr R_{\mathrm{alg}}
\cap
\mathscr R_{\mathrm{decimal}}
=\varnothing
\}.
\]

于是严格有：

\[
\boxed{
\Xi_{\mathrm{back}}\in\mathcal D
\Longrightarrow
\text{not liftable}.
}
\tag{9.2}
\]

---

## 9.1 当前可显式写出的 proven 子死亡区

### \(\mathcal D_{\mathrm{prime}}\subseteq\mathcal D_{\mathrm{arith}}\)

任何违反 T8/T9 或 denominator prime graph 已证必要结构的 state。

### \(\mathcal D_{\square}\subseteq\mathcal D_{\mathrm{root}}\)

任一必需 nondegenerate recovery quadratic 判别式不是整数平方，并且不存在其他 auxiliary root branch。

### \(\mathcal D_{\mathrm{RRT}}\subseteq\mathcal D_{\mathrm{root}}\)

所有可能 reduced rational roots 都违反 numerator / denominator divisibility。

### \(\mathcal D_{10}\subseteq\mathcal D_{\mathrm{dec}}\)

\[
v_2(K_{\mathrm{tail}})<\ell
\quad\text{或}\quad
v_5(K_{\mathrm{tail}})<\ell.
\]

### \(\mathcal D_{\mathrm{digit}}\subseteq\mathcal D_{\mathrm{dec}}\)

所有 algebraically admissible roots 都落在真实 digit window 外。

### \(\mathcal D_{\mathrm{plane}}\subseteq\mathcal D_{\mathrm{dec}}\)

所有剩余 roots 恢复后都违反

\[
L A=t B.
\]

---

# 10. “最弱但足以推出 non-liftability”的正确解释

如果允许任意逻辑组合，则

\[
\mathcal D_1,\mathcal D_2
\]

都是死亡区时，

\[
\mathcal D_1\cup\mathcal D_2
\]

仍是更大的死亡区。

所以 backward 研究真正应该优化的量不是“寻找唯一最弱 obstruction”，而是：

\[
\boxed{
\text{在保持可判定性的前提下，尽可能扩大 }\mathcal D.
}
\]

等价地，要把当前死亡证书的前提不断削弱：

\[
B_{\mathrm{strong}}
\Longrightarrow
B_{\mathrm{weak}}
\Longrightarrow
\text{not liftable}.
\]

这比追求形式上的“唯一最弱条件”更稳定。

---

# 11. 当前 backward frontier

当前反向体系真正缺少的不是更多必要条件，而是三类**existential synchronization theorem**。

现有材料已经有大量局部证书，但仍常出现：

\[
\forall p,\quad
\exists \text{ local admissible choice}
\]

却无法推出或否定

\[
\exists \text{ one global witness compatible with all }p
\]

以及真实 digit interval、exact coefficient plane。

`proved_results_report_v3.md` 已明确指出：逐素数局部吸收条件可以分别相容，但仍需由**同一个具有正确实数大小的整数根**实现。

这正是 backward strict layer 当前最核心的缺口。

因此本轮建议把真正 frontier 写成：

\[
\boxed{
\textbf{Global Recovery-Witness Synchronization}.
}
\tag{11.1}
\]

这与正向线的 Moving Primitive-Core Uniform Termination 不同：

- 正向线问 reachable states 如何终止；
- 反向线问一个给定 recovery signature 是否存在**单一完整 witness**穿过全部恢复门。

---

# 12. 下一轮最多三个全局 theorem targets

## Target B1 — Global Admissible-Root Capacity Theorem

### 目标

为任意 strict Exact-Lift recovery polynomial

\[
AX^2+BX+C
\]

建立一个 chamber-independent 的 admissible-root capacity bound。

理想形式是：

\[
\boxed{
\operatorname{Liftable}(\Xi)
\Longrightarrow
\ell
\le
\mathsf{Cap}_{10}
(A,B,C;\Gamma_{\mathrm{arith}},\mathcal A_{\mathrm{root}})
}
\tag{B1}
\]

其中 \(\mathsf{Cap}_{10}\) 只读取 \(\Xi_{\mathrm{back}}\)，并比当前单纯

\[
10^\ell\mid\kappa^2(\kappa+2G)
\]

更容易在粗状态上失败。

### 它将吞掉

- discriminant square；
- rational-root theorem divisibility；
- \(2/5\)-adic tail capacity；
- 一部分 Hensel / resonance 现象；
- 一部分 near-\(S\)-unit 现象。

### 要求

不能只证明某 chamber 的某个 root branch；必须对所有非退化 / 退化 recovery polynomials 给统一 admissibility 处理。

---

## Target B2 — Global Prime-Demand Matching Theorem

### 目标

把 denominator recovery 看成 prime-power demand / supply matching。

对每个素数 \(p\)，需求由：

- 三个 denominator exponent；
- canonical gcd；
- tail denominator；
- reducedness

产生；供给由：

- recovery coefficients；
- norm factors；
- common scale；
-允许的 Gaussian splitting

产生。

建立一个全局 feasibility criterion，例如 Hall-type capacity condition：

\[
\boxed{
\operatorname{Liftable}
\Longrightarrow
\forall S\subseteq\mathcal P,\quad
\mathrm{Demand}(S)\le\mathrm{Supply}(S).
}
\tag{B2}
\]

然后寻找其反面作为

\[
\mathcal D_{\mathrm{arith}}
\]

的大规模可判定子区。

### 它将吞掉

- T8/T9 的位置限制；
- denominator prime graph；
- unique-max / pair-max；
- Gaussian prime allocation；
- “局部位置均相容但总容量可能不相容”的剩余问题。

### 重要警告

`strict_layer_final_campaign.md` 的 N5 已证明“只看 prime 最大位置”不足，所以 B2 必须是**capacity theorem**，不能退化为位置枚举。

---

## Target B3 — One-Witness Decimal Synchronization Theorem

### 目标

假设 arithmetic gate 与 algebraic-root gate 都通过，直接研究最终交集：

\[
\mathscr R_{\mathrm{alg}}
\cap
\mathscr R_{\mathrm{prime}}
\cap
\mathscr R_{\mathrm{digit}}
\cap
\mathscr R_{\mathrm{plane}}.
\]

希望证明一个只读取 \(\Xi_{\mathrm{back}}\) 的充分死亡条件：

\[
\boxed{
B_{\mathrm{sync}}(\Xi)
\Longrightarrow
\mathscr R_{\mathrm{alg}}
\cap
\mathscr R_{\mathrm{decimal}}
=\varnothing.
}
\tag{B3}
\]

最值得发展的版本是：

1. local congruence / Hensel 数据把 root 压到一个或极少数 global residue classes；
2. digit window 给出真实区间；
3. exact coefficient plane 再提供一个非恒等 residual；
4. 证明唯一可能代表不落在 plane 上。

### 它将吞掉

- “模数大于区间只给唯一性”的最后一步缺口；
- local-root sign synchronization；
- Hensel contact；
- coefficient-plane incompatibility；
- 一部分 near-square / near-\(S\)-unit 的终端用途。

B3 是当前最可能直接扩大

\[
\mathcal D_{\mathrm{dec}}
\]

的顶层 target。

---

# 13. Proved / derived / heuristic / open ledger

## PROVED

1. T3 提供 canonical common-denominator reconstruction 的双向判别：
   sphere + canonical gcd recovery + exact concatenation identity 可完整恢复原题。
2. Exact-Lift primitive recovery：
   \[
   \gcd(q,y_i)=q/b_i.
   \]
3. denominator core / prime graph 的既有全局必要结构。
4. gap quadratic 与 primitive tail quadratic 为完整候选的必要恢复方程。
5. 非退化整系数二次式：
   \[
   \mathbf Q\text{-root}
   \iff
   \text{integer-square discriminant}.
   \]
6. rational-root divisibility：
   \[
   \nu\mid D(\kappa+2G),\quad
   \mu\mid\kappa D\mathcal N_{12},
   \]
   \[
   \delta_3\mid\kappa(\kappa+2G),\quad
   a_3\mid\mathcal C_3.
   \]
7. denominator-tail certificate：
   \[
   10^\ell\mid\kappa^2(\kappa+2G).
   \]
8. strict-layer 旧冲刺已经证明：单纯连续尺度 gap 与单纯 prime-position incompatibility 均不足以形成全局终止。

## DERIVED FROM PROVED RESULTS

1. 任一已证必要 certificate 的失败都可通过逆否命题作为 non-liftability obstruction。
2. \(2\)-adic / \(5\)-adic capacity failure 精确等价于 \(10^\ell\)-divisibility failure 的两个坐标。
3. discriminant-square 与“存在某个有理根”在非退化二次式层面可合并。
4. tail certificate 是 algebraic root denominator recovery 与 decimal tail realization 的交叉投影，不应视作独立第四 basis。
5. coefficient-plane mismatch of a particular flip 只杀死该变换，不自动杀死原 state。

## NEW PROVED

1. Completion-fibre obstruction calculus：
   \[
   \mathfrak C_j(\xi)=\varnothing
   \Longrightarrow
   \text{not liftable}.
   \]
2. Existential-gate quantifier discipline：若完整恢复只保证“存在某 auxiliary certificate”，则必须排空全部 certificate 才能宣称 obstruction。
3. 不存在天然唯一的非平凡“最弱 obstruction”：充分死亡条件对析取闭合。
4. 相对当前 proof library，可把大量旧终端现象压入
   \[
   B_{\mathrm{arith}},\quad
   B_{\mathrm{root}},\quad
   B_{\mathrm{dec}}
   \]
   三个恢复失败家族，而无需把 near-square / near-\(S\)-unit / Hensel 当作独立本体。

## HEURISTIC

1. 三个 basis 家族可能最终被更深的“global witness synchronization”统一。
2. Gaussian allocation、Hensel、near-square、near-\(S\)-unit 很可能只是不同坐标下对“单一恢复 witness 无法同步”的显影。
3. Prime-demand matching 可能存在 Hall-type 或 max-flow/min-cut 风格的严格算术版本；目前尚无此定理。

## OPEN

1. 是否存在一个跨所有 strict chambers 的 admissible-root capacity theorem。
2. 是否存在一个全局 prime-power demand/supply matching theorem。
3. 是否能把 local congruence roots + digit interval + coefficient plane 压成统一 one-witness synchronization contradiction。
4. 三个 obstruction basis 是否能严格再降为两个甚至一个真正的深层 obstruction。
5. 当前 \(\mathcal D\) 是否足够大到能与正向 reachable set 发生全局包含关系——本轮按责任边界不研究该包含。

---

# 14. 最终结论

Backward Strict Layer 的第一轮得到的不是某个新的窄分支矛盾，而是一套独立于正向 SGR termination 的研究语言：

\[
\boxed{
\text{strict state}
\longmapsto
\text{completion fibre}
\longmapsto
\text{recovery certificates}
\longmapsto
\text{death region}.
}
\]

其核心原则是：

\[
\boxed{
\text{不是把必要条件反过来使用，}
\quad
\text{而是严格使用必要条件的逆否命题，
并对 auxiliary witnesses 保持正确的存在量词。}
}
\]

当前最小可信恢复障碍结构为

\[
\boxed{
\mathfrak B_{\mathrm{back}}
=
\{
B_{\mathrm{arith}},
B_{\mathrm{root}},
B_{\mathrm{dec}}
\},
}
\]

接口为

\[
\boxed{
\Xi_{\mathrm{back}}
=
(
\Gamma_{\mathrm{arith}},
\mathscr Q_{\mathrm{rec}},
\mathcal A_{\mathrm{root}},
\Theta_{10},
\Pi_{\mathrm{dec}}
),
}
\]

死亡区为

\[
\boxed{
\mathcal D
=
\mathcal D_{\mathrm{arith}}
\cup
\mathcal D_{\mathrm{root}}
\cup
\mathcal D_{\mathrm{dec}}.
}
\]

未来正向研究线不需要采用本报告的内部推理，只需输出足够的 \(\Xi_{\mathrm{back}}\)。Backward 线的任务则是继续扩大 \(\mathcal D\)，最终争取得到

\[
\boxed{
\Xi_{\mathrm{back}}\in\mathcal D
\Longrightarrow
\text{not liftable}
}
\]

覆盖越来越弱、越来越全局的 strict-layer states。

本轮没有证明 strict layer empty，没有关闭 \(A_2\)、DD、\(A_1\) 中任何局部分支，也没有推进 moving primitive-core termination。责任边界保持完整。
