# 三项十进制拼接平方和问题：Strict Layer Unified Exact Lift Campaign

**文件名：** `strict_layer_unified_exact_lift_campaign.md`  
**本轮标签：** **SGR-2B — UNIFICATION + NEW COUPLING**  
**研究范围：** 仅统一 `strict_layer_global_reduction_campaign.md`（SGR-1）与 `exact_lift_research_synthesis_2026-08-10.md`（Exact-Lift），不单攻 \(A_2\)、DD、\(A_1\) 任一局部分支。

---

## 0. 结论摘要与证明等级

本轮得到的核心结论是：

\[
\boxed{
\text{Exact Lift}
\Longleftrightarrow
\text{primitive sphere core}
+
\text{coprime scale}
+
\text{exact decimal recovery}.
}
\]

在统一记号下，Exact-Lift 的整数球面

\[
q=\operatorname{lcm}(b_1,b_2,b_3),\qquad
y_i=\frac{a_iq}{b_i},\qquad
y_1^2+y_2^2+y_3^2=H^2
\]

与 SGR 的 primitive sphere core

\[
(P_1,P_2,P_3,Q_0),\qquad
P_1^2+P_2^2+P_3^2=Q_0^2,\qquad
\gcd(P_1,P_2,P_3,Q_0)=1
\]

严格对应为

\[
\boxed{
q=V,\qquad
y_i=UP_i,\qquad
H=UQ_0.
}
\]

这里特意把 primitive-core 的第四坐标写成 \(Q_0\)，以避免与 Exact-Lift 中前两分母拼接

\[
Q_{12}=b_1 10^{m_2}+b_2
\]

混淆。

进一步，本轮把两套所谓“二次门”放到同一 SGR 状态 \(\Sigma\) 上：

1. **SGR depth gate**
   \[
   \boxed{
   F_\Sigma(T)=F_2T^2+F_1T+F_0=0,
   \qquad
   T=10^{\ell(V)}.
   }
   \]

2. **Exact-Lift normalized discriminant gate**
   \[
   \boxed{
   \mathscr P_\Sigma(T)=Z^2,
   }
   \]
   其中 \(\mathscr P_\Sigma\) 在固定 primitive core / gcd profile / carry state 后是一个次数至多 \(6\) 的有理系数多项式；乘一个固定平方清分母后可取为整系数多项式。

它们**不是同一个二次方程**。SGR 的二次式以 decimal depth \(T\) 为未知量；Exact-Lift 的原始二次式以 gap ratio \(\mu/\nu\) 或第三尾有理根 \(z_3\) 为未知量。只有把 Exact-Lift 沿 primitive profile 消去公共尺度后，二者才共享同一变量 \(T\)。

此时可以严格做一次 Euclidean reduction / resultant。若

\[
\mathscr P_\Sigma^*(T)
\equiv
A_\Sigma T+B_\Sigma
\pmod{F_\Sigma(T)},
\]

其中 \(\mathscr P_\Sigma^*\) 已乘固定平方清分母，则任一候选都必须满足

\[
Z_*^2=A_\Sigma T+B_\Sigma.
\]

若 \(F_2\neq0\) 且 \(A_\Sigma\neq0\)，消去 \(T\) 得到新的统一耦合式

\[
\boxed{
F_2X^2+
(F_1A_\Sigma-2F_2B_\Sigma)X
+
\bigl(
F_2B_\Sigma^2
-F_1A_\Sigma B_\Sigma
+F_0A_\Sigma^2
\bigr)
=0,
\qquad
X=Z_*^2.
}
\tag{UC}
\]

这正是

\[
\operatorname{Res}_T
\left(
F_\Sigma(T),\,
X-A_\Sigma T-B_\Sigma
\right)=0.
\]

因此本轮确实得到一条此前两套框架分开书写时没有出现的 **primitive-state resultant coupling**。它不比“两门同时成立”在逻辑上更强，但它把两门压成一个只含 primitive-state 系数与平方变量 \(X\) 的严格必要方程，故本轮等级取 **SGR-2B**，而不是把它夸大成新的无解定理。

### 结论等级

- **PROVED**
  - Exact-Lift 与 primitive sphere normalization 的双向变量桥接；
  - \(q=V,\ y_i=UP_i,\ H=UQ_0\) 及其全部 gcd 条件；
  - carrier chamber 是 decimal profile 的粗投影，而不是 primitive core 的算术类型；
  - SGR depth quadratic 与 Exact-Lift gap/tail quadratic 不是同一方程；
  - Exact-Lift discriminant gate 的公共尺度消去；
  - resultant coupling (UC)。

- **DERIVED FROM PROVED RESULTS**
  - 固定 primitive core 的 finite-fibre 结论对三个 carrier chamber 同时成立；
  - 任意无穷 strict-layer 候选序列必有 \(Q_0\to\infty\)；
  - 旧 \(A_2/DD/A_1\) 三个开放列表可统一视为 moving-core termination 的状态标签，而不是三个逻辑独立的顶层 obligation。

- **COMPUTATIONAL EVIDENCE**
  - 本轮没有新增，也没有依赖任何新计算证据。

- **HEURISTIC**
  - near-square、near-\(S\)-unit、Hensel、square-spacing 等旧局部现象很可能是同一个 moving-core termination 的不同显影，而非独立终端问题；本轮不把这一判断升级为定理。

- **OPEN OBLIGATION**
  - 统一后的唯一顶层终端义务：
    \[
    \boxed{
    \text{Moving Primitive-Core Uniform Termination}.
    }
    \]

---

## 1. 来源审计说明

本轮重点使用并核对了：

- `exact_lift_research_synthesis_2026-08-10.md`；
- `proved_results_report_v3.md`；
- `strict_layer_final_campaign.md`；
- `final_results_index.md`；
- 早期 primitive sphere / scale-direction 正文
  `拼接平方和问题_推进整合证明.md`、
  `粘贴的 markdown (1)。md`、
  `three_term_decimal_concat_summary.md`。

其中，primitive sphere normalization、\(V=\operatorname{lcm}(b_i)\)、有限 gcd profile 等关键恢复步骤已经回查到证明正文，而不是只依赖 summary。

当前 File Library 检索没有重新暴露 `strict_layer_global_reduction_campaign.md` 的正文。因此本报告只继承本轮任务已经明确冻结的 SGR-1 核心结论：

\[
\boxed{
\text{fixed primitive core}\Longrightarrow\text{finite decimal fibre},
}
\]

以及其 depth gate

\[
F_2T^2+F_1T+F_0=0,\qquad T=10^{\ell(V)}.
\]

SGR-1 原报告还给过显式 height bounds，但本报告**不使用也不复述这些常数**，避免在正文不可重新打开时把 summary 中的数字当成重新审计过的证明。为了进一步降低依赖，本报告在第 4 节从已经回查到的 primitive-profile master equation **重新推导**了该 depth quadratic 的结构与系数形式。

Exact-Lift 的公共 \(\kappa\)、统一判别式、primitive tail quadratic 则在 `exact_lift_research_synthesis_2026-08-10.md` 中有完整统一推导链和明确的“已证/开放”区分；本轮另外独立复核了本报告实际使用的尺度消去、有理根整除和 resultant 代数。

---

# 2. 精确变量字典

## 2.1 SGR primitive normalization

取 primitive sphere core

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

令

\[
\gcd(U,V)=1,
\qquad
g_i=\gcd(V,P_i),
\qquad
C_i=\frac{P_i}{g_i}.
\]

SGR 恢复为

\[
\boxed{
a_i=UC_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.
}
\tag{2.1}
\]

---

## 2.2 从 SGR 到 Exact-Lift

### 定理 2.1

在 (2.1) 下，

\[
\boxed{
\operatorname{lcm}(b_1,b_2,b_3)=V.
}
\]

### 证明

任取素数 \(p\) 且

\[
p^e\parallel V.
\]

若三个 \(P_i\) 都被 \(p\) 整除，则由

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

可知 \(p\mid Q_0\)，与 primitive 性矛盾。因此至少存在一个 \(j\) 满足

\[
p\nmid P_j.
\]

于是

\[
v_p(g_j)=v_p(\gcd(V,P_j))=0,
\]

故

\[
v_p(b_j)
=
v_p(V/g_j)
=
e.
\]

所以每个 \(p^e\parallel V\) 的完整素幂都在至少一个 \(b_j\) 中出现。另一方面 \(b_i\mid V\)。因此

\[
\operatorname{lcm}(b_1,b_2,b_3)=V.
\]

证毕。

Exact-Lift 定义

\[
q=\operatorname{lcm}(b_1,b_2,b_3),
\qquad
y_i=\frac{a_iq}{b_i}.
\]

由上式，

\[
q=V,
\]

并且

\[
y_i
=
\frac{(UP_i/g_i)V}{V/g_i}
=
UP_i.
\]

因此

\[
y_1^2+y_2^2+y_3^2
=
U^2(P_1^2+P_2^2+P_3^2)
=
(UQ_0)^2.
\]

取正根，

\[
\boxed{
H=UQ_0.
}
\]

所以

\[
\boxed{
q=V,\qquad y_i=UP_i,\qquad H=UQ_0.
}
\tag{2.2}
\]

---

## 2.3 从 Exact-Lift 到 SGR

反过来，从 Exact-Lift 出发：

\[
q=\operatorname{lcm}(b_i),
\qquad
y_i=\frac{a_iq}{b_i},
\qquad
y_1^2+y_2^2+y_3^2=H^2.
\]

Exact-Lift 的 primitive recovery 给出

\[
\boxed{
\gcd(q,y_i)=\frac{q}{b_i}.
}
\tag{2.3}
\]

令

\[
\boxed{
U:=\gcd(y_1,y_2,y_3,H),
}
\]

\[
P_i:=\frac{y_i}{U},
\qquad
Q_0:=\frac HU,
\qquad
V:=q.
\]

则

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

且由 \(U\) 的定义，

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

还需要核查

\[
\gcd(U,V)=1.
\]

假设存在素数 \(p\mid U\) 且 \(p\mid V=q\)。因为 \(p\mid U\)，有

\[
p\mid y_i
\quad(i=1,2,3).
\]

于是由 (2.3)，

\[
p\mid \frac q{b_i}
\quad(i=1,2,3).
\]

设 \(p^E\parallel q\)。上式意味着对所有 \(i\),

\[
v_p(b_i)\le E-1,
\]

这与

\[
q=\operatorname{lcm}(b_1,b_2,b_3)
\]

要求至少一个 \(b_i\) 具有 \(p\)-进指数 \(E\) 矛盾。

故

\[
\boxed{\gcd(U,V)=1.}
\]

再令

\[
g_i=\gcd(V,P_i).
\]

由于 \(\gcd(U,V)=1\),

\[
\gcd(V,UP_i)=\gcd(V,P_i)=g_i.
\]

而 \(UP_i=y_i\)，由 (2.3)

\[
g_i
=
\gcd(q,y_i)
=
\frac q{b_i}
=
\frac V{b_i}.
\]

所以

\[
b_i=\frac V{g_i},
\]

且

\[
a_i
=
\frac{b_iy_i}{q}
=
\frac{(V/g_i)(UP_i)}V
=
\frac{UP_i}{g_i}.
\]

这完全恢复 SGR。

因此：

\[
\boxed{
\text{Exact-Lift integer sphere + primitive recovery}
\Longleftrightarrow
\text{SGR primitive core + coprime scale}.
}
\tag{2.4}
\]

---

## 2.4 完整变量对应表

为避免同名冲突，以下把 Exact-Lift 原来叫 \(Q\) 的前两分母拼接统一改记为 \(Q_{12}\)。

| SGR / bridge 变量 | Exact-Lift 变量 | 精确关系 | 性质 |
|---|---|---|---|
| \(Q_0\) | \(H\) | \(H=UQ_0\) | primitive core 第四坐标；**不是** Exact 的 \(Q_{12}\) |
| \(P_i\) | \(y_i\) | \(y_i=UP_i\) | primitive sphere 坐标 |
| \(U\) | integer sphere content | \(U=\gcd(y_1,y_2,y_3,H)\) | common content |
| \(V\) | \(q\) | \(q=V=\operatorname{lcm}(b_i)\) | common denominator scale |
| \(g_i\) | primitive recovery gcd | \(g_i=\gcd(V,P_i)=q/b_i=\gcd(q,y_i)\) | 精确对应 |
| \(C_i=P_i/g_i\) | \(a_i/U\) | \(a_i=UC_i\) | 精确对应 |
| \(b_i\) | \(b_i\) | \(b_i=V/g_i\) | 相同对象 |
| \(n_i=\ell(a_i)\) | \(n_i\) | 相同 | 分子位数 |
| \(m_i=\ell(b_i)\) | \(m_i\) | 相同 | 分母位数 |
| \(\delta_i=n_i-m_i\) | \(s_i\) | \(\delta_i=s_i\) | 精确对应 |
| \(T=10^{\ell(V)}\) | 无单独命名 | \(T=10^{\ell(q)}\) | SGR decimal-depth variable |
| gcd profile \(g_i\) / \(W_{\rm prof}\) | 无单一变量 | \(W_{\rm prof}=\gcd(V,\operatorname{lcm}(P_i))\) 决定 \(g_i\) | SGR 更上游 |
| \(Q_{12}\) | Exact 的 \(Q\) | \(Q_{12}=b_1 10^{m_2}+b_2\) | 由 scale/profile/decimal state 派生 |
| \(G\) | \(G\) | \(G=b_1b_2\) | Exact 下游块值对象 |
| \(\mathcal N_{12}\) | \(\mathcal N_{12}\) | \((a_1b_2)^2+(a_2b_1)^2\) | Exact 下游二平方型 |
| \((C,D)\) | \((C,D)\) | 见第 5 节三 chamber 定义 | 无 primitive-core 单变量对应 |
| \(\kappa\) | \(\kappa\) | \(10^{m_3}Q_{12}G/b_3\) | 下游尾权 |
| \((\mu,\nu)\) | \((\mu,\nu)\) | gap ratio 的既约分子分母 | SGR 无天然变量 |
| \(K_{C,D}\) | \(K_{C,D}\) | \(G^2C^2-D^2\mathcal N_{12}\) | Exact 判别核 |
| \(W\) | \(W\) | discriminant square root | SGR 无天然变量 |
| \(\delta_3,L,\tau,z_3\) | 同名尾正规化 | \(10^\ell=\delta_3L,\ b_3=\delta_3\tau,\ z_3=a_3/\delta_3\) | 下游 tail arithmetic |
| \(G_0\) | \(G_0\) | primitive recovery gcd | 无 primitive-core 单变量对应 |

### 一个必要的记号澄清

Exact-Lift 写

\[
z_3=\frac{a_3}{\delta_3}.
\]

因为 \(\delta_3\mid b_3\) 且 \(\gcd(a_3,b_3)=1\)，通常

\[
\gcd(a_3,\delta_3)=1
\]

且 \(z_3\) 是**既约有理数**，不应默认是整数。primitive tail quadratic 后使用的正是有理根定理：既约分母 \(\delta_3\) 整除首项系数，既约分子 \(a_3\) 整除常数项。

---

# 3. 两套 reduction 的逻辑关系

## 3.1 问题 A：SGR primitive-core reduction 能否从 Exact-Lift 直接推出？

答案分两层。

### 第一层：primitive normalization —— 可以

由第 2 节，

\[
\boxed{
\text{Exact integer sphere}
+
\gcd(q,y_i)=q/b_i
\Longrightarrow
(P_i,Q_0;U,V,g_i)
}
\]

完全可逆。

所以 SGR 的 primitive-core 坐标系不是另一套独立假设，而是 Exact-Lift integer sphere 的**canonical content quotient**。

### 第二层：SGR finite-fibre theorem —— 不能仅靠 Exact-Lift 的球面提升直接得到

从 Exact-Lift 的

\[
y_1^2+y_2^2+y_3^2=H^2
\]

除 content 只能得到 primitive core。要进一步得到

\[
\boxed{
\text{fixed core}
\Longrightarrow
\text{finite decimal fibre}
}
\]

还必须使用：

1. fixed core 的有限 gcd profile；
2. \(U,V\) 与 \(C_i,g_i\) 相乘时的有限 carry states；
3. decimal concatenation master equation；
4. 对 \(T=10^{\ell(V)}\) 的低次数代数门。

因此：

\[
\boxed{
\text{primitive normalization 可从 Exact-Lift 直接推出；}
}
\]

\[
\boxed{
\text{SGR-1 finite fibre 是对 Exact-Lift 的额外全局压缩。}
}
\]

---

## 3.2 问题 B：三个 carrier chamber 在 primitive-core 坐标下是什么？

Exact-Lift 定义

\[
s_i=n_i-m_i.
\]

而 SGR 中

\[
\delta_i=n_i-m_i.
\]

所以

\[
s_i=\delta_i.
\]

三个 chamber 精确变为：

\[
\boxed{
A_2\text{-only}:
\quad
\delta_3>0,\qquad
\delta_2+\delta_3\le0;
}
\]

\[
\boxed{
DD:
\quad
\delta_3>0,\qquad
\delta_2+\delta_3>0;
}
\]

\[
\boxed{
A_1\text{-only}:
\quad
\delta_3\le0,\qquad
\delta_2+\delta_3>0.
}
\]

这三类的数学身份是：

\[
\boxed{
\textbf{decimal profile / carrier state},
}
\]

不是 primitive sphere core 的内在算术类型。

同一个固定 primitive core

\[
(P_1,P_2,P_3,Q_0)
\]

原则上可以通过不同 gcd profile / scale / carry state 落入不同 chamber；core 本身并没有一个固有标签叫 \(A_2\)、DD 或 \(A_1\)。

但 carrier chamber 也不是“后续消元人为制造”的分类。它直接来自 exact weighted-average identity：

\[
\mathcal R
=
\frac{
w_1 10^{s_2+s_3}r_1
+w_2 10^{s_3}r_2
+w_3r_3
}{
w_1+w_2+w_3
},
\]

以及 \(\mathcal R>r_i\)。因此它是**真实的十进制几何状态**，只是比完整 SGR state 更粗。

---

## 3.3 问题 C：谁包含谁？

### carrier label 是 SGR full state 的粗投影

一个完整 SGR state 至少记录：

- primitive core；
- gcd profile \(g_i\)；
- numerator / denominator carry bits；
- digit differences / scale gap；
- decimal depth state。

给定这些量，\((\delta_2,\delta_3)\) 已知，所以 carrier chamber 唯一确定。

因此

\[
\boxed{
\text{SGR full state}
\longrightarrow
\text{carrier chamber}.
}
\]

反向不成立：只知道 \(A_2/DD/A_1\) 的两个符号条件，远不能恢复 gcd profile、carry、\(T\) 或 primitive core。

### 但 Exact-Lift 的下游算术不包含于 carrier label

进入 chamber 后，Exact-Lift 又定义：

\[
Q_{12},\ G,\ \mathcal N_{12},\ C,\ D,\ \kappa,\ \mu,\nu,\ldots
\]

这些包含具体 block value、二平方型、tail gcd、prime-flow 等新算术信息。

所以不能写成简单的一条

\[
\text{SGR}>\text{Exact}
\]

或

\[
\text{Exact}>\text{SGR}.
\]

正确层级是：

\[
\boxed{
\begin{array}{c}
\text{Original exact candidate}
\\
\Updownarrow
\\
\text{integer sphere + exact recovery}
\\
\Updownarrow
\\
\text{primitive core + coprime scale}
\\
\Downarrow
\\
\text{SGR finite gcd/carry/digit state}
\\
\Downarrow
\\
\text{carrier label }(A_2,DD,A_1)
\end{array}
}
\]

而从同一个 SGR state 还可以向下展开：

\[
\boxed{
\text{Exact-Lift block arithmetic}
:
Q_{12},G,\mathcal N_{12},C,D,\kappa,\ldots
}
\]

以及

\[
\boxed{
\text{SGR depth quadratic}
:
F_\Sigma(T)=0.
}
\]

这两个下游方向保存的是不同信息。

### 最终层级判断

\[
\boxed{
\text{primitive core 是共同上层；}
}
\]

\[
\boxed{
\text{SGR state 比 carrier chamber 更细；}
}
\]

\[
\boxed{
\text{Exact-Lift 的 }(\kappa,C,D,\mathcal N_{12},\ldots)
\text{ 是 chamber 后新增的算术层；}
}
\]

\[
\boxed{
\text{SGR depth gate 与 Exact arithmetic gate 彼此非冗余。}
}
\]

---

# 4. SGR depth quadratic 的自包含重推

这一节不依赖无法重新打开的 SGR-1 正文，而从已经回查到的 primitive-profile master equation 重推。

## 4.1 有限 gcd profile

固定 primitive core。令

\[
P_*=\operatorname{lcm}(P_1,P_2,P_3).
\]

由于

\[
g_i=\gcd(V,P_i),
\]

若令

\[
W_{\rm prof}=\gcd(V,P_*),
\]

则

\[
W_{\rm prof}\mid P_*,
\]

且

\[
g_i=\gcd(W_{\rm prof},P_i).
\]

所以固定 core 后 gcd profile 只有有限多个。

令

\[
L_g=\operatorname{lcm}(g_1,g_2,g_3),
\qquad
h_i=\frac{L_g}{g_i}.
\]

由拼接主方程可得：

\[
\boxed{
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
}
\tag{4.1}
\]

---

## 4.2 carry variables

记

\[
u=\ell(U),\qquad
v=\ell(V),\qquad
T=10^v.
\]

再记

\[
\lambda_i=\ell(C_i),
\qquad
\gamma_i=\ell(g_i).
\]

因为

\[
a_i=UC_i,
\]

存在

\[
\varepsilon_i\in\{0,1\}
\]

使

\[
\boxed{
n_i=u+\lambda_i-1+\varepsilon_i.
}
\tag{4.2}
\]

因为

\[
V=g_ib_i,
\]

存在

\[
\eta_i\in\{0,1\}
\]

使

\[
\boxed{
v=\gamma_i+m_i-1+\eta_i,
}
\]

即

\[
\boxed{
m_i=v-\gamma_i+1-\eta_i.
}
\tag{4.3}
\]

令

\[
r=u-v.
\]

则

\[
\delta_i=n_i-m_i
=
r+\lambda_i+\gamma_i-2+\varepsilon_i+\eta_i.
\tag{4.4}
\]

一个完整 SGR state \(\Sigma\) 固定 core、gcd profile、carry bits 与相容的 \(r\)。

---

## 4.3 抽出 \(T\)

由 (4.2)–(4.3),

\[
10^{n_2+n_3}
=
T^2
10^{
2r+\lambda_2+\lambda_3-2+\varepsilon_2+\varepsilon_3
},
\]

\[
10^{n_3}
=
T
10^{
r+\lambda_3-1+\varepsilon_3
},
\]

\[
10^{m_2+m_3}
=
T^2
10^{
-\gamma_2-\gamma_3+2-\eta_2-\eta_3
},
\]

\[
10^{m_3}
=
T
10^{
-\gamma_3+1-\eta_3
}.
\]

代入 (4.1)，得到

\[
\boxed{
F_{2,\Sigma}T^2
+
F_{1,\Sigma}T
+
F_{0,\Sigma}
=0,
}
\tag{4.5}
\]

其中

\[
\boxed{
F_{2,\Sigma}
=
h_1\left[
P_1
10^{
2r+\lambda_2+\lambda_3-2+\varepsilon_2+\varepsilon_3
}
-
Q_0
10^{
-\gamma_2-\gamma_3+2-\eta_2-\eta_3
}
\right],
}
\]

\[
\boxed{
F_{1,\Sigma}
=
h_2\left[
P_2
10^{
r+\lambda_3-1+\varepsilon_3
}
-
Q_0
10^{
-\gamma_3+1-\eta_3
}
\right],
}
\]

\[
\boxed{
F_{0,\Sigma}
=
h_3(P_3-Q_0).
}
\]

固定 \(\Sigma\) 后这些都是固定有理数；乘一个固定 \(10\)-幂即可化为整系数。

因为所有 \(P_i>0\) 且

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

必有

\[
P_3<Q_0.
\]

故

\[
\boxed{
F_{0,\Sigma}<0.
}
\]

因此 (4.5) 不可能恒等于零。

- 若 \(F_{2,\Sigma}\neq0\)，每个 state 至多有两个 \(T\)；
- 若 \(F_{2,\Sigma}=0\)，则因 \(F_0\neq0\)，方程至多线性，至多有一个 \(T\)。

这解释了 SGR-1 的有限 fibre 为什么本质上是一个低次数 decimal-depth gate，而不是某种数值搜索现象。

---

# 5. Exact-Lift gate 翻译到同一 primitive-profile 坐标

现在固定同一个 SGR state \(\Sigma\)。

## 5.1 把公共尺度从 \(b_i,a_i\) 中抽出

因为

\[
g_i\mid V,
\qquad
L_g=\operatorname{lcm}(g_i),
\]

有

\[
L_g\mid V.
\]

定义

\[
\boxed{
R:=\frac{V}{L_g}.
}
\]

则

\[
b_i
=
\frac V{g_i}
=
R\,\frac{L_g}{g_i}
=
Rh_i.
\tag{5.1}
\]

同时

\[
a_i=UC_i.
\]

因此前两块 Exact-Lift 对象可以全部写成“common scale × primitive-state object”。

定义

\[
\boxed{
\widehat Q
=
h_1 10^{m_2}+h_2,
}
\]

\[
\boxed{
\widehat G=h_1h_2,
}
\]

\[
\boxed{
\widehat{\mathcal N}
=
(C_1h_2)^2+(C_2h_1)^2.
}
\]

则

\[
\boxed{
Q_{12}=R\widehat Q,
}
\tag{5.2}
\]

\[
\boxed{
G=R^2\widehat G,
}
\tag{5.3}
\]

\[
\boxed{
\mathcal N_{12}
=
U^2R^2\widehat{\mathcal N}.
}
\tag{5.4}
\]

---

## 5.2 三 chamber 的 coefficient pair

定义 branchwise \((\widehat C,\widehat D)\)：

### \(A_2\)-only

\[
\widehat C
=
C_1 10^{m_2}+10C_2,
\qquad
\widehat D=\widehat Q.
\]

于是

\[
C=U\widehat C,
\qquad
D=R\widehat D.
\]

### DD

令

\[
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0.
\]

则

\[
\widehat C
=
10^{m_2+k_{12}}C_1
+
10^{d_3}C_2,
\qquad
\widehat D=\widehat Q,
\]

并仍有

\[
C=U\widehat C,
\qquad
D=R\widehat D.
\]

### \(A_1\)-only

令

\[
g=-s_3\ge0,
\qquad
k_{12}=s_2+s_3\ge1.
\]

则

\[
\widehat C
=
10^{g+k_{12}+m_2}C_1+C_2,
\]

\[
\widehat D
=
10^g\widehat Q,
\]

且

\[
C=U\widehat C,
\qquad
D=R\widehat D.
\]

所以三 chamber 的共同尺度规律是

\[
\boxed{
C=U\widehat C,
\qquad
D=R\widehat D.
}
\tag{5.5}
\]

---

## 5.3 \(\kappa\) 的公共尺度

三 branch 可统一写

\[
\boxed{
\kappa
=
\frac{10^{m_3}Q_{12}G}{b_3}.
}
\tag{5.6}
\]

因为

\[
b_3=Rh_3,
\]

由 (5.2)–(5.3)

\[
\kappa
=
\frac{
10^{m_3}(R\widehat Q)(R^2\widehat G)
}{
Rh_3
}
=
R^2
\frac{
10^{m_3}\widehat Q\widehat G
}{
h_3
}.
\]

定义整数量

\[
\boxed{
\widetilde\kappa
:=
10^{m_3}\widehat Q\widehat G.
}
\tag{5.7}
\]

于是

\[
\boxed{
\kappa
=
R^2\frac{\widetilde\kappa}{h_3}.
}
\tag{5.8}
\]

注意 \(\widetilde\kappa\) 显然是整数；\(\widetilde\kappa/h_3\) 不必单独是整数，\(\kappa\) 的整性还可利用 \(R^2\) 吸收 \(h_3\) 的因子。

---

## 5.4 判别核尺度消去

定义

\[
\widehat K
=
\widehat G^2\widehat C^2
-
\widehat D^2\widehat{\mathcal N}.
\]

由 (5.3)–(5.5),

\[
K_{C,D}
=
G^2C^2-D^2\mathcal N_{12}
\]

变成

\[
\boxed{
K_{C,D}
=
U^2R^4\widehat K.
}
\tag{5.9}
\]

Exact-Lift discriminant-square gate 是

\[
\kappa
\left(
\kappa K_{C,D}
-
2GD^2\mathcal N_{12}
\right)
=
W^2.
\tag{5.10}
\]

代入 (5.3)–(5.4)、(5.8)–(5.9)，得到

\[
W^2
=
U^2R^8
\frac{\widetilde\kappa}{h_3}
\left[
\frac{\widetilde\kappa}{h_3}\widehat K
-
2\widehat G\widehat D^2\widehat{\mathcal N}
\right].
\]

乘 \(h_3^2/(U^2R^8)\)：

\[
\left(
\frac{h_3W}{UR^4}
\right)^2
=
\widetilde\kappa
\left[
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right].
\tag{5.11}
\]

右端是整数。一个整数若是有理数平方，则它本身是整数平方。因此存在

\[
Z\in\mathbb Z
\]

使

\[
\boxed{
Z^2
=
\widetilde\kappa
\left[
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right].
}
\tag{5.12}
\]

这是本轮最重要的统一翻译之一：

\[
\boxed{
\text{Exact discriminant square 可以完全消去 }U,R
\text{ 的 common scale。}
}
\]

它剩下的只是 primitive core、gcd profile、decimal state 与 \(T\) 的条件。

---

## 5.5 在固定 state 下，它是 \(T\) 的次数至多六的 square gate

固定 \(\Sigma\) 后，由 (4.3)

\[
m_i=v+\text{constant},
\qquad
T=10^v.
\]

因此

\[
10^{m_2}=c_2T,
\qquad
10^{m_3}=c_3T
\]

其中 \(c_2,c_3\) 是固定的 \(10\) 的整数次幂（必要时允许负指数；最终可统一清分母）。

于是：

\[
\widehat Q
=
h_1c_2T+h_2
\]

是 \(T\) 的一次式；

\[
\widehat C,\widehat D
\]

在三个 chamber 中也都是 \(T\) 的次数至多一次的式子；

\[
\widehat K
=
\widehat G^2\widehat C^2
-
\widehat D^2\widehat{\mathcal N}
\]

次数至多 \(2\)；

而

\[
\widetilde\kappa
=
10^{m_3}\widehat Q\widehat G
\]

次数至多 \(2\)。

所以 (5.12) 右端是一个

\[
\boxed{
\deg_T\mathscr P_\Sigma\le6
}
\]

的有理系数多项式：

\[
\boxed{
\mathscr P_\Sigma(T)=Z^2.
}
\tag{5.13}
\]

取固定正整数 \(d_\Sigma\) 清除全部系数分母，并且故意乘平方 \(d_\Sigma^2\)，得到等价的整数平方门

\[
\boxed{
\mathscr P_\Sigma^*(T)=Z_*^2,
\qquad
\mathscr P_\Sigma^*\in\mathbb Z[T],
\qquad
\deg\mathscr P_\Sigma^*\le6.
}
\tag{5.14}
\]

---

# 6. 两套“二次门”究竟是什么关系？

## 6.1 它们不是同一个二次方程

SGR：

\[
F_\Sigma(T)=0
\]

的未知量是

\[
T=10^{\ell(V)}.
\]

Exact-Lift 的第一个统一二次式：

\[
D(\kappa+2G)\mu^2
-2G\kappa C\,\mu\nu
+\kappa D\mathcal N_{12}\nu^2
=0
\]

的未知对象是 projective gap ratio

\[
[\mu:\nu].
\]

Exact-Lift primitive tail quadratic：

\[
-\kappa(\kappa+2G)z_3^2
+2G^2LCz_3
+\mathcal C_3
=0
\]

的未知量则是

\[
z_3=a_3/\delta_3.
\]

所以三者的二次性来自**不同的消元方向**：

- SGR：消去实际 scale mantissa，只留 decimal depth；
- Exact gap quadratic：消去 sphere / block balance，只留 gap slope；
- Exact tail quadratic：消去第三块 gcd，只留 primitive tail rational root。

因此不可能把它们通过简单变量改名识别为同一个二次式。

---

## 6.2 也不存在“一个整体严格包含另一个”

SGR depth gate 看不到：

- \(\mathcal N_{12}\) 的平方分裂；
- \(\kappa\) 的 prime allocation；
- \(10^\ell\mid\kappa^2(\kappa+2G)\)；
- primitive recovery 的逐素数 gcd 信息。

反过来，Exact-Lift 的统一 gap / tail quadratic 本身也没有给出：

\[
\boxed{
\text{fixed primitive core}
\Longrightarrow
\text{finite number of decimal depths}.
}
\]

特别是它原来的三个 branch 仍允许前缀一起向无穷增长。

故正确分类是：

\[
\boxed{
\textbf{情形 III：二者是对同一候选施加的非冗余 gates。}
}
\]

更精确地说，它们在 primitive normalization 之上共享候选，但在不同消元坐标中施加约束。

---

# 7. 新 coupling：SGR quadratic × Exact square gate 的 resultant

这是本轮新增的严格耦合。

## 7.1 先模掉 SGR quadratic

固定一个 primitive core 与完整 state \(\Sigma\)。

把 SGR 方程清分母并约去系数公因子，写成

\[
\boxed{
F(T)=f_2T^2+f_1T+f_0=0,
\qquad
f_i\in\mathbb Z,
\qquad
f_0\neq0.
}
\tag{7.1}
\]

把 Exact square gate 写成

\[
\boxed{
P(T)=Z^2,
\qquad
P\in\mathbb Z[T],
\qquad
\deg P\le6.
}
\tag{7.2}
\]

对 \(P\) 除以 \(F\)。

若 \(f_2\neq0\)，存在

\[
Q_F(T)\in\mathbb Q[T],
\qquad
A,B\in\mathbb Q
\]

使

\[
P(T)=Q_F(T)F(T)+AT+B.
\]

再乘一个固定平方清除 \(A,B\) 的分母而不破坏 square condition，可无损地写成

\[
\boxed{
Z_*^2=AT+B,
\qquad
A,B\in\mathbb Z.
}
\tag{7.3}
\]

---

## 7.2 消去 \(T\)

令

\[
X=Z_*^2.
\]

若 \(A\neq0\)，则

\[
T=\frac{X-B}{A}.
\]

代入 (7.1)，乘 \(A^2\)，得到

\[
\boxed{
f_2X^2+
(f_1A-2f_2B)X
+
\left(
f_2B^2-f_1AB+f_0A^2
\right)
=0.
}
\tag{7.4}
\]

等价地，

\[
\boxed{
\operatorname{Res}_T
\bigl(
f_2T^2+f_1T+f_0,\,
X-AT-B
\bigr)=0.
}
\]

因此每个 strict-layer candidate 必须产生一个**整数平方**

\[
X=Z_*^2
\]

使一个 state-dependent 整系数二次多项式消失。

这是一个新的统一对象：

\[
\boxed{
\Phi_\Sigma(X)
=
f_2X^2+
(f_1A-2f_2B)X
+
f_2B^2-f_1AB+f_0A^2.
}
\tag{7.5}
\]

于是

\[
\boxed{
\Phi_\Sigma(Z_*^2)=0.
}
\tag{7.6}
\]

---

## 7.3 退化情形

### 若 \(A=0\)

则 Exact gate 在 SGR quadratic quotient 上退化为

\[
\boxed{
Z_*^2=B.
}
\]

也就是说整个 state 先接受一个**固定整数是否为平方**的测试。

### 若 \(f_2=0\)

由于 \(f_0\neq0\)，SGR depth gate 是真正线性方程：

\[
f_1T+f_0=0.
\]

于是 \(T\) 唯一确定，再直接代入 \(P(T)\) 检查平方即可；此时不需要 resultant。

---

## 7.4 这条 coupling 强到什么程度？

\(\Phi_\Sigma(Z_*^2)=0\) 是新的严格必要条件，但必须准确评价它的逻辑强度。

它：

- 比单独使用 SGR depth quadratic 更强；
- 比单独使用 Exact discriminant-square 更强；
- 把两套 gate 压到 primitive-state 系数上的一个方程；
- 消去了共同 decimal depth \(T\)。

但它**并不比“两套旧条件同时成立”更强**，因为它就是两者的消元后果。

所以本轮不能宣称：

\[
\text{resultant 已经制造了新的 contradiction}.
\]

真正的新价值是：

\[
\boxed{
\text{原来分散在两个框架中的约束，
第一次变成了一个可直接研究 square spacing / divisibility 的单一对象。}
}
\]

这足以构成 SGR-2B 的 “NEW COUPLING”，但不构成 strict layer closure。

---

## 7.5 一个有用的内部校验

(7.4) 作为关于 \(X\) 的二次式，其判别式为

\[
\boxed{
A^2(f_1^2-4f_2f_0).
}
\]

而若 \(T\) 本身是 SGR quadratic 的整数根，

\[
f_1^2-4f_2f_0
=
(2f_2T+f_1)^2.
\]

所以这部分判别平方没有凭空增加信息。这再次说明：真正还需要利用的是

\[
\boxed{
X\ \text{本身必须是整数平方},
}
\]

以及 Exact-Lift 另外保留下来的 tail / gcd / valuation constraints。

---

# 8. Exact tail divisibility 在 primitive-profile 坐标下仍保留独立信息

Exact-Lift 有

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G).
}
\tag{8.1}
\]

代入

\[
\kappa=R^2\frac{\widetilde\kappa}{h_3},
\qquad
G=R^2\widehat G,
\]

得到

\[
\kappa^2(\kappa+2G)
=
R^6
\frac{
\widetilde\kappa^2
(\widetilde\kappa+2h_3\widehat G)
}{
h_3^3
}.
\tag{8.2}
\]

因此对 \(p=2,5\) 分别有精确必要不等式

\[
\boxed{
\ell
\le
6v_p(R)
+
2v_p(\widetilde\kappa)
+
v_p(\widetilde\kappa+2h_3\widehat G)
-
3v_p(h_3).
}
\tag{8.3}
\]

这里

\[
R=\frac{V}{L_g}.
\]

这条式子非常重要，因为它指出：

- normalized discriminant square (5.12) 已经消掉实际尺度 \(U,R\)；
- 但 denominator-tail certificate 仍然读取 \(R\) 的真实 \(2\)-、\(5\)-进结构。

因此 Exact-Lift 中至少有两种不同性质的 gate：

1. **state/depth algebraic gate**：可以与 SGR quadratic 做 resultant；
2. **actual-lift arithmetic gate**：保留 scale mantissa 的 \(2/5\)-adic / gcd 信息。

这也是为什么不能把 O1/O2/O3 简单当作三个相同层级的“待证 lemma”。

---

# 9. Fixed primitive core finite fibre 对 Exact-Lift frontier 的影响

SGR-1 的核心全局结论是：

\[
\boxed{
\text{固定 primitive core 后，strict decimal lift 只有有限多个。}
}
\tag{9.1}
\]

继承的显式 height bound 是：若

\[
N=\ell(Q_0),
\]

则

\[
\boxed{
\ell(V)\le5N-1,
\qquad
\ell(U)\le5N,
}
\tag{9.2}
\]

并有对应 profile 深度上界。

本轮不使用这些常数的最优性；只使用其直接逻辑后果。

---

## 9.1 对全部三个 chamber 的统一推论

设存在无穷多个 strict-layer exact candidates。

若 primitive-core height \(Q_0\) 有界，则 primitive quadruple

\[
(P_1,P_2,P_3,Q_0)
\]

本身只有有限多个。

而每个固定 primitive core 的 exact lifts 又由 (9.1) 只有有限多个。

矛盾。

因此：

\[
\boxed{
\text{任何无穷 strict-layer candidate sequence 必有 }
Q_0\to\infty.
}
\tag{9.3}
\]

这个结论与 carrier chamber 无关，所以同时覆盖

\[
A_2,\qquad DD,\qquad A_1.
\]

---

## 9.2 DD 顶部尖角的重新解释

旧 Exact-Lift 语言把 DD 的最后困难写成：

\[
10S_{12}+11
\le n_3\le
11S_{12}+3
\]

并伴随：

- extreme denominator asymmetry；
- \(2/5\)-adic double resonance；
- near-square；
- near-\(S\)-unit。

SGR-1 告诉我们：这里不存在一个“固定球面方向但 decimal tail 无限增长”的逃逸机制。

所以如果 DD 顶部尖角真的存在无界候选族，它必然同时满足

\[
\boxed{
Q_0\to\infty.
}
\]

因此 DD 的真正无界问题应改写成：

\[
\boxed{
\text{moving primitive core}
+
\text{DD state constraints}
+
\text{coupled gates}
\Longrightarrow ?
}
\]

而不是单独追问“第三尾还能增长多长”。

这并没有关闭 DD，但它严格减少了无界自由度的解释空间。

---

## 9.3 \(A_2\)-only

旧 frontier 的 \(A_2\) deep-even / source-double-Hensel 系统看起来包含很长的尾参数。

统一后必须区分：

- **固定 core 内的 tail**：有限；
- **真正可能无界的序列**：只能由 core 本身移动而产生。

所以 \(m_2\ge11\)、deep-even、source Hensel 等不再是独立的“无界源”；它们是 moving-core sequence 上必须出现的 state features。

---

## 9.4 \(A_1\)-only

旧 frontier 中最危险的是 saturated \(L=1\) 下的 decimal shift \(g\)。

SGR finite fibre 立即排除：

\[
\boxed{
\text{固定 primitive core 上 }g\to\infty.
}
\]

如果存在 \(g\to\infty\) 的候选序列，则必伴随

\[
Q_0\to\infty.
\]

所以 saturated \(g\) 也应被重新定义为一个 moving-core height phenomenon，而不是“还有一个与 core 无关的自由十进制平移”。

---

## 9.5 near-\(S\)-unit / near-square / square-spacing 的统一定位

本轮不证明这些现象等价。

但从依赖图看，它们的角色已经改变：

旧解释：

\[
A_2\text{ 有 Hensel 障碍},
\quad
DD\text{ 有 near-square 障碍},
\quad
A_1\text{ 有 shift 障碍}.
\]

统一后的更准确解释是：

\[
\boxed{
\text{它们都是尝试阻止 }
Q_0\to\infty
\text{ 的不同局部机制。}
}
\]

即：

\[
\boxed{
\text{真正的无界变量不再是某个单独 tail，
而是 moving primitive core。}
}
\]

这是 SGR-1 对 Exact-Lift frontier 最实质的全局影响。

---

# 10. 重新定义 strict-layer frontier

旧列表有两套：

- SGR：O1 / O2 / O3；
- Exact-Lift：\(A_2\) / DD / \(A_1\)。

现在都不应继续当作顶层 dependency graph。

---

## 10.1 统一 exact-lift object

定义一个 **Unified Strict Exact Lift datum**

\[
\mathfrak L
=
\left(
\mathcal P,\Sigma,T,U,V;\,
Q_{12},G,\mathcal N_{12},C,D,\kappa,\ldots
\right),
\]

其中

\[
\mathcal P=(P_1,P_2,P_3,Q_0)
\]

是 primitive core，\(\Sigma\) 是 finite gcd/carry/carrier state。

一个真实候选必须**同时**满足：

### Gate G1：SGR depth

\[
\boxed{
F_\Sigma(T)=0.
}
\]

### Gate G2：normalized Exact discriminant

\[
\boxed{
P_\Sigma(T)=Z^2.
}
\]

等价地可以用新的 coupling

\[
\boxed{
\Phi_\Sigma(Z_*^2)=0.
}
\]

### Gate G3：exact arithmetic recovery

包括但不限于

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G),
}
\]

\[
\boxed{
\nu\mid D(\kappa+2G),
\qquad
\mu\mid\kappa D\mathcal N_{12},
}
\]

primitive recovery gcd、digit windows、逐项既约与 exact concatenation recovery。

这些是**候选必须同时满足的 conjunctive gates**。

但它们不是三个“必须分别证明一个无解 lemma”的 terminal obligations。要证明 strict layer empty，只要能证明这些 gate 的共同解不存在即可；某一个 gate 单独给出统一 contradiction 也足够。

---

## 10.2 最小 dependency graph

本轮建议把 strict layer 的主图冻结为：

\[
\boxed{
\text{Strict Exact Candidate}
}
\]

\[
\Updownarrow
\]

\[
\boxed{
\text{Primitive Core } \mathcal P
+
\text{Coprime Scale }(U,V)
+
\text{Exact Recovery}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{Finite State }\Sigma
\quad
(\text{gcd/carry/profile; carrier is a label})
}
\]

\[
\Downarrow
\]

\[
\boxed{
F_\Sigma(T)=0
}
\quad\land\quad
\boxed{
P_\Sigma(T)=Z^2
}
\quad\land\quad
\boxed{
\text{tail/gcd/valuation recovery}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\Phi_\Sigma(Z_*^2)=0
+
\text{arithmetic recovery}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{fixed-core finite fibre}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{any infinite family } \Longrightarrow Q_0\to\infty
}
\]

\[
\Downarrow
\]

\[
\boxed{
\mathbf{T1}:
\text{Moving Primitive-Core Uniform Termination}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{Strict Layer Empty}.
}
\]

因此顶层真正独立的 terminal obligation 数为

\[
\boxed{r=1.}
\]

---

## 10.3 唯一 terminal obligation 的精确表述

### T1 — Moving Primitive-Core Uniform Termination

证明不存在 primitive cores

\[
\mathcal P_j
=
(P_{1,j},P_{2,j},P_{3,j},Q_{0,j}),
\qquad
Q_{0,j}\to\infty,
\]

以及相应 finite states \(\Sigma_j\)、exact lifts，使：

\[
F_{\Sigma_j}(T_j)=0,
\]

\[
P_{\Sigma_j}(T_j)=Z_j^2,
\]

并同时满足全部 exact tail / gcd / valuation / digit recovery constraints。

换言之，真正剩余的是

\[
\boxed{
\text{一个 moving-core uniform incompatibility theorem}.
}
\]

\(A_2\)、DD、\(A_1\) 仍然可以作为证明时的 case labels，但它们不再是 dependency graph 上三个逻辑独立的终点。

---

## 10.4 哪些是 conjunctive obligations，哪些只是 alternative attack routes？

### 候选层面必须同时满足

这些是 **conjunctive conditions**：

1. primitive sphere + coprime scale recovery；
2. SGR depth gate；
3. Exact normalized discriminant square；
4. denominator-tail / gcd / valuation recovery；
5. digit windows / reducedness / original exact recovery。

### 证明层面不是必须全部单独完成

以下只是 **alternative attack routes**：

- resultant / square-spacing；
- pure-\(10\)-root / Vieta-style cross-ratio；
- \(2/5\)-adic tail valuation；
- near-square；
- near-\(S\)-unit；
- Hensel contact；
- Gaussian splitting；
- direct core-height inequality。

只要其中任一条对所有 moving cores 给出 uniform contradiction，就可直接闭合 T1。

因此旧 SGR 的

- O1 moving-core \(2/5\)-adic suffix；
- O2 pure-\(10\) quadratic-root / Vieta；
- O3 exact-lift gcd / interval obstruction

不应写成

\[
O1\to O2\to O3
\]

或

\[
O1\land O2\land O3
\]

三条必须逐项完成的 lemma。

它们只是攻击同一个 T1 的不同投影。

同理，旧 \(A_2/DD/A_1\) 是 T1 内部的 state partition，不是三个不同的全局研究项目。

---

# 11. 本轮得到的统一数学图景

可以把两套旧框架压成以下一句话：

\[
\boxed{
\text{primitive core 决定算术方向；}
\quad
\Sigma\text{ 决定 decimal profile；}
\quad
T\text{ 受 SGR 二次门控制；}
\quad
\text{Exact-Lift 再要求同一 }T\text{ 落在一个平方纤维中；}
\quad
\text{真实 }U,V\text{ 还必须通过 }2/5\text{-adic recovery。}
}
\]

所以严格层不是“两套不同方法并行”：

\[
\text{SGR}
\qquad\text{vs.}\qquad
\text{Exact-Lift},
\]

而应看成同一个纤维塔：

\[
\boxed{
\text{primitive core}
\longrightarrow
\text{finite decimal state}
\longrightarrow
\text{depth root}
\longrightarrow
\text{square lift}
\longrightarrow
\text{arithmetic recovery}.
}
\]

这才是本轮所要求的 **Unified Exact Lift**。

---

# 12. 对原有 terminal 状态的重新解释

## \(A_2\)

旧的

\[
m_2\ge11,\qquad
\text{deep-even},\qquad
\text{double Hensel}
\]

保留为 moving-core T1 中的一类 state geometry。

它不再被视为一个独立“必须完成的 \(A_2\) theorem”。

## DD

顶部尖角

\[
10S_{12}+11\le n_3\le11S_{12}+3
\]

仍是最锋利的局部 state，但其无界性必须伴随

\[
Q_0\to\infty.
\]

因此 near-square + discriminant square 应优先尝试作用于新的 \(\Phi_\Sigma(Z^2)=0\)，而不是再单独建立一套 DD 总框架。

## \(A_1\)

saturated \(L=1\) 与 decimal shift \(g\) 仍需保留，但

\[
g\to\infty
\]

只能发生在 moving core 上。

所以它也应并入 T1，而不是继续作为一个与 primitive core 无关的尾自由度。

---

# 13. 下一轮只建议两个 terminal targets

## Target 1 — Moving-core resultant / square-spacing theorem

直接研究本轮新对象

\[
\boxed{
\Phi_\Sigma(Z^2)=0
}
\]

在

\[
Q_0\to\infty
\]

下是否可能统一成立。

目标不是再按 \(A_2/DD/A_1\) 单独展开，而是寻找对所有有限 state templates 有效的：

- coefficient height relation；
- square-spacing inequality；
- resultant gcd；
- discriminant / determinant identity；
- \(0<|\Delta|<\) adjacent-square gap。

这是本轮之后最自然、信息耦合最充分的单一 target。

---

## Target 2 — Primitive-core \(2/5\)-adic recovery theorem

统一研究

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G)
}
\]

在

\[
R=V/L_g
\]

坐标下的

\[
\ell
\le
6v_p(R)
+
2v_p(\widetilde\kappa)
+
v_p(\widetilde\kappa+2h_3\widehat G)
-
3v_p(h_3),
\qquad
p=2,5,
\]

并把它与 SGR 已经给出的有限 depth root 同步。

目标是证明 moving core 无法长期同时提供：

- 正确 decimal depth；
- 正确 \(2\)-adic capacity；
- 正确 \(5\)-adic capacity；
- Exact discriminant square。

这是 arithmetic-recovery 侧唯一值得单开一轮的全局 target。

---

# 14. 最终等级

\[
\boxed{
\textbf{SGR-2B — UNIFICATION + NEW COUPLING}.
}
\]

理由：

1. 两套变量已经严格双向对接；
2. primitive-core / carrier / Exact arithmetic 的层级关系已经澄清；
3. SGR depth quadratic 与 Exact-Lift quadratics 被证明不是同一方程，而是非冗余 gates；
4. Exact discriminant square 已在 primitive-profile 坐标下消除公共尺度 \(U,R\)；
5. 两门联立后得到新的 state-level resultant
   \[
   \boxed{\Phi_\Sigma(Z^2)=0};
   \]
6. fixed-core finite fibre 将旧三个 carrier frontier 的共同无界源压成
   \[
   \boxed{Q_0\to\infty};
   \]
7. strict-layer 顶层 frontier 因而从“两套开放列表”压成一个真正独立的 terminal obligation：
   \[
   \boxed{
   \text{Moving Primitive-Core Uniform Termination}.
   }
   \]

本轮**没有**证明 strict layer empty，也没有关闭某个局部 carrier chamber；这正符合本轮只统一框架、不偏离去做局部 campaign 的范围限制。
