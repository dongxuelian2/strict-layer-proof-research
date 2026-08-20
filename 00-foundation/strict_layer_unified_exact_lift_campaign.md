# 三项十进制拼接平方和问题：Strict Layer Unified Exact Lift Campaign

**文件名：** `strict_layer_unified_exact_lift_campaign.md`  
**本轮等级：** **SGR-2B — UNIFICATION + NEW COUPLING**  
**范围：** 只统一 SGR-1 的 primitive-core / finite-fibre 框架与既有 Exact-Lift 框架；不单独深攻 \(A_2\)、DD、\(A_1\)，不启动新的 Pell / \(S\)-unit / Vieta jumping 路线。

---

# 0. Executive Summary

本轮得到的统一结论是：

\[
\boxed{
\text{Exact integer sphere + exact recovery}
\Longleftrightarrow
\text{primitive sphere core + coprime scale}.
}
\]

为避免 Exact-Lift 中前两分母拼接 \(Q\) 与 primitive sphere 的第四坐标冲突，全文把 primitive core 写成

\[
\mathcal P=(P_1,P_2,P_3,Q_0),
\]

而把 Exact-Lift 的前两分母拼接写成

\[
Q_{12}=b_1 10^{m_2}+b_2.
\]

两套主变量严格对应为

\[
\boxed{
q=V,\qquad y_i=UP_i,\qquad H=UQ_0.
}
\]

其中

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

\[
\gcd(U,V)=1,
\qquad
g_i=\gcd(V,P_i),
\qquad
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.
\]

Exact-Lift 的三个 carrier chamber

\[
A_2\text{-only},\qquad DD,\qquad A_1\text{-only}
\]

不是 primitive core 的三种算术类型，而是由

\[
s_i=n_i-m_i
\]

决定的真实 decimal carrier/profile 状态。完整 SGR state 决定 carrier chamber，但 chamber 不能反向恢复 primitive core、gcd profile、carry bits 或 decimal depth。

两套“二次门”也不是同一个方程：

- SGR 的二次式
  \[
  F_\Sigma(T)=0,\qquad T=10^{\ell(V)}
  \]
  控制 **decimal depth**；
- Exact-Lift 的统一 gap quadratic 控制 \([\mu:\nu]\)；
- Exact-Lift 的 primitive tail quadratic 控制第三尾有理根 \(z_3\)。

它们是对同一 exact candidate 的不同消元投影，因此属于：

\[
\boxed{
\text{compatible but nonredundant gates}.
}
\]

但二者可以进一步严格耦合。固定 primitive core 与完整 SGR state \(\Sigma\) 后，Exact-Lift 判别平方可化成

\[
\mathscr P_\Sigma(T)=Z^2,
\qquad
\deg_T\mathscr P_\Sigma\le6.
\]

将它模 SGR 二次式约化后，可写成

\[
Z_*^2=A_\Sigma T+B_\Sigma.
\]

若 SGR 二次式为

\[
f_2T^2+f_1T+f_0=0
\]

且 \(f_2A_\Sigma\neq0\)，消去 \(T\) 得

\[
\boxed{
f_2X^2+
(f_1A_\Sigma-2f_2B_\Sigma)X
+
\bigl(
f_2B_\Sigma^2-f_1A_\Sigma B_\Sigma+f_0A_\Sigma^2
\bigr)
=0,
\quad
X=Z_*^2.
}
\tag{UC}
\]

这是一条新的 **primitive-state resultant coupling**。它是“两旧门同时成立”的严格消元后果，不能夸大成比二者联立更强的新定理，但它把原来分散的两个约束压成了一个可直接研究 square-spacing、divisibility 与 moving-core growth 的对象。

SGR-1 的 fixed-core finite-fibre theorem 进一步说明：

\[
\boxed{
\text{固定 primitive core}
\Longrightarrow
\text{只有有限多个 strict decimal lifts}.
}
\]

故任何无穷 strict-layer 候选序列都必须满足

\[
\boxed{
Q_0\to\infty.
}
\]

这对 \(A_2\)、DD、\(A_1\) 同时成立。原来三个 chamber 中看似独立的“长尾逃逸”因此都不能发生在固定 primitive sphere direction 上；整个 strict layer 的真正无界源被统一为 **moving primitive core**。

本轮后的顶层 frontier 可以压成一个独立终端义务：

\[
\boxed{
\textbf{Moving Primitive-Core Uniform Termination}.
}
\]

其内部有两个必须同时满足、但不应误写为两个分别必须关闭的 terminal lemmas 的信息通道：

1. SGR depth + Exact discriminant 的 algebraic/square coupling；
2. Exact tail / gcd / \(2,5\)-adic actual-lift recovery。

因此本轮等级为

\[
\boxed{\textbf{SGR-2B — UNIFICATION + NEW COUPLING}.}
\]

本轮没有证明 strict layer empty，也没有关闭 \(A_2\)、DD、\(A_1\) 中任何一个旧局部分支。

---

# 1. 证据等级与来源审计

全文使用以下等级：

- **PROVED**：本文给出完整证明，或回查到已有严格证明正文；
- **DERIVED FROM PROVED RESULTS**：由已证结论直接推出；
- **COMPUTATIONAL EVIDENCE**：仅计算证据；
- **HEURISTIC**：结构性启发，不作为定理；
- **OPEN OBLIGATION**：仍需证明。

本轮实际使用的 Exact-Lift 关键链包括：

\[
q=\operatorname{lcm}(b_i),
\qquad
y_i=\frac{a_iq}{b_i},
\qquad
y_1^2+y_2^2+y_3^2=H^2,
\]

\[
\gcd(q,y_i)=\frac q{b_i},
\]

统一 gap quadratic、判别平方、primitive tail quadratic、以及

\[
10^\ell\mid\kappa^2(\kappa+2G).
\]

这些关键等价、整除与恢复步骤均沿既有 Exact-Lift 证明链回查，而不是仅把 synthesis 的摘要陈述当作证明。

primitive normalization 的关键恢复步骤也回查到早期 primitive-sphere 正文与审计后的基础定理：特别是

\[
V=\operatorname{lcm}(b_1,b_2,b_3)
\]

及最小公共分母的 primitive recovery。

### 关于 SGR-1 正文可见性的限制

本轮 File Library 检索没有重新暴露 `strict_layer_global_reduction_campaign.md` 的完整正文。项目当前冻结的 SGR-1 输入为：

\[
\boxed{
\text{fixed primitive core}\Longrightarrow\text{finite decimal fibre},
}
\]

以及每个完整 finite state 上的 exact depth gate

\[
\boxed{
F_{2,\Sigma}T^2+F_{1,\Sigma}T+F_{0,\Sigma}=0,
\qquad
T=10^{\ell(V)}.
}
\]

SGR-1 还给出了 core-height 对 \(\ell(U),\ell(V)\) 的显式线性界；这些常数不参与本轮新 coupling 的证明，因此本文不把它们作为新结果重新证明。

为了避免依赖不可见正文中的代数细节，第 4 节从已经回查到的 primitive-profile master equation 重新推导了 **固定完整 state 上的二次 depth gate**。需要区分：

- “每个固定 state 至多两个 depth roots”由本文重新推导；
- “固定 primitive core 只有有限多个完整 states”继承 SGR-1 的 finite-state theorem。

这一区分避免把 finite-fibre 结论循环地建立在未经证明的“\(r\) 只有有限种”上。

---

# 2. 精确变量字典

## 2.1 SGR primitive normalization

取

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\tag{2.1}
\]

令

\[
\boxed{\gcd(U,V)=1,}
\]

\[
\boxed{
g_i=\gcd(V,P_i),
\qquad
C_i=\frac{P_i}{g_i}.
}
\tag{2.2}
\]

则 strict candidate 的既约块恢复为

\[
\boxed{
a_i=UC_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.
}
\tag{2.3}
\]

---

## 2.2 SGR \(\Rightarrow\) Exact-Lift

### 定理 2.1 — \(V\) 恰为分母最小公倍数

**PROVED.**

\[
\boxed{
\operatorname{lcm}(b_1,b_2,b_3)=V.
}
\tag{2.4}
\]

### 证明

任取素数 \(p\) 且

\[
p^e\parallel V.
\]

若 \(p\mid P_1,P_2,P_3\)，则由

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

可得 \(p\mid Q_0\)，与 primitive 性矛盾。

故至少存在一个 \(j\) 使

\[
p\nmid P_j.
\]

于是

\[
v_p(g_j)=v_p(\gcd(V,P_j))=0,
\]

所以

\[
v_p(b_j)=v_p(V/g_j)=e.
\]

即 \(V\) 的每个完整素幂都出现在至少一个 \(b_j\) 中，而另一方面所有 \(b_i\mid V\)。因此

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

由 (2.4)，

\[
\boxed{q=V.}
\]

再由 (2.3)，

\[
y_i
=
\frac{(UP_i/g_i)V}{V/g_i}
=
UP_i.
\]

所以

\[
y_1^2+y_2^2+y_3^2
=
U^2(P_1^2+P_2^2+P_3^2)
=
(UQ_0)^2.
\]

取正根得到

\[
\boxed{
y_i=UP_i,
\qquad
H=UQ_0.
}
\tag{2.5}
\]

因此

\[
\boxed{
q=V,\qquad y_i=UP_i,\qquad H=UQ_0.
}
\tag{2.6}
\]

---

## 2.3 Exact-Lift \(\Rightarrow\) SGR

从 Exact-Lift 出发：

\[
q=\operatorname{lcm}(b_i),
\qquad
y_i=\frac{a_iq}{b_i},
\qquad
y_1^2+y_2^2+y_3^2=H^2.
\]

Exact primitive recovery 给出

\[
\boxed{
\gcd(q,y_i)=\frac q{b_i}.
}
\tag{2.7}
\]

定义

\[
\boxed{
U=\gcd(y_1,y_2,y_3,H),
}
\]

\[
P_i=\frac{y_i}{U},
\qquad
Q_0=\frac HU,
\qquad
V=q.
\tag{2.8}
\]

则显然

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

并且

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

还需证明 \(\gcd(U,V)=1\)。

假设某素数 \(p\mid U\) 且 \(p\mid q\)。令

\[
p^E\parallel q.
\]

因为 \(p\mid U\)，有 \(p\mid y_i\) 对所有 \(i\)。由 (2.7)，

\[
p\mid \frac q{b_i}
\]

对所有 \(i\) 成立，因此

\[
v_p(b_i)\le E-1
\]

对所有 \(i\) 成立。这与

\[
q=\operatorname{lcm}(b_i)
\]

要求至少一个 \(b_i\) 含完整 \(p^E\) 矛盾。

故

\[
\boxed{\gcd(U,V)=1.}
\tag{2.9}
\]

于是

\[
\gcd(V,P_i)
=
\gcd\!\left(q,\frac{y_i}{U}\right)
=
\gcd(q,y_i)
=
\frac q{b_i},
\]

其中使用了 \(\gcd(U,q)=1\)。所以定义

\[
g_i=\gcd(V,P_i)
\]

后有

\[
\boxed{
g_i=\frac V{b_i},
\qquad
b_i=\frac V{g_i}.
}
\tag{2.10}
\]

另一方面

\[
P_i=\frac{y_i}{U}
=
\frac{a_iq}{Ub_i}
=
\frac{a_iV}{Ub_i}
=
\frac{a_ig_i}{U},
\]

故

\[
\boxed{
a_i=\frac{UP_i}{g_i}.
}
\tag{2.11}
\]

因此两套 primitive normalization 完全双向一致。

---

## 2.4 完整变量对应表

| SGR 变量 | Exact-Lift 变量/表达式 | 对应关系 | 性质 |
|---|---|---|---|
| \((P_1,P_2,P_3,Q_0)\) | integer sphere 去 content 后的 primitive quadruple | \(P_i=y_i/U,\ Q_0=H/U\) | 精确双向 |
| \(U\) | sphere content | \(U=\gcd(y_1,y_2,y_3,H)\) | 精确双向 |
| \(V\) | \(q=\operatorname{lcm}(b_i)\) | \(V=q\) | 精确双向 |
| \(g_i\) | primitive recovery gcd | \(g_i=q/b_i=\gcd(q,y_i)\) | 精确双向 |
| \(C_i=P_i/g_i\) | \(a_i/U\) | \(a_i=UC_i\) | 精确双向 |
| \(a_i,b_i\) | \(a_i,b_i\) | 相同原始块 | 相同对象 |
| \(n_i=\ell(a_i)\) | \(n_i\) | 相同 | 相同对象 |
| \(m_i=\ell(b_i)\) | \(m_i\) | 相同 | 相同对象 |
| \(\delta_i=n_i-m_i\) | \(s_i\) | \(\delta_i=s_i\) | 精确 |
| \(T=10^{\ell(V)}\) | 无专门符号 | \(T=10^{\ell(q)}\) | SGR depth |
| gcd/carry state \(\Sigma\) | 无单一 Exact 变量 | 决定 digit/profile chamber | SGR 更上游 |
| \(Q_{12}\) | Exact 原记号 \(Q\) | \(b_1 10^{m_2}+b_2\) | Exact 下游 |
| \(G\) | \(G\) | \(b_1b_2\) | Exact 下游 |
| \(\mathcal N_{12}\) | \(\mathcal N_{12}\) | \((a_1b_2)^2+(a_2b_1)^2\) | Exact 下游 |
| \((C,D)\) | \((C,D)\) | branchwise coefficient pair | 无 primitive-core 单变量对应 |
| \(\kappa\) | \(\kappa\) | unified tail weight | Exact 下游 |
| \((\mu,\nu)\) | \((\mu,\nu)\) | gap ratio reduced pair | SGR 无天然变量 |
| \(K_{C,D}\) | 同名 | \(G^2C^2-D^2\mathcal N_{12}\) | Exact discriminant kernel |
| \(W\) | \(W\) | discriminant square root | SGR 无天然变量 |
| \(\delta_3,L,\tau,z_3\) | 同名 tail normalization | \(10^\ell=\delta_3L,\ b_3=\delta_3\tau,\ z_3=a_3/\delta_3\) | Exact tail arithmetic |
| \(G_0\) | \(G_0\) | tail primitive-recovery gcd | SGR 无天然变量 |

### 记号警告：\(Q_0\neq Q_{12}\)

全文固定：

\[
Q_0=\text{primitive sphere radius},
\]

\[
Q_{12}=b_1 10^{m_2}+b_2.
\]

这是两套旧文档最容易发生的记号冲突。

### 记号警告：\(z_3\) 一般不是整数

Exact-Lift 中

\[
z_3=\frac{a_3}{\delta_3}.
\]

由于

\[
\delta_3\mid b_3,
\qquad
\gcd(a_3,b_3)=1,
\]

有

\[
\gcd(a_3,\delta_3)=1.
\]

因此 \(z_3\) 是既约有理数，除非 \(\delta_3=1\)，否则不应称为整数变量。

---

# 3. 两套 reduction 的逻辑关系

## 3.1 SGR primitive-core reduction 能否从 Exact-Lift 直接推出？

答案必须分两层。

### primitive normalization：可以

第 2 节已经证明

\[
\boxed{
\text{Exact integer sphere + primitive recovery}
\Longleftrightarrow
\text{primitive core + coprime scale}.
}
\]

因此 SGR 的 primitive core 不是另一套独立假设，而是 Exact integer sphere 的 canonical content quotient。

### fixed-core finite fibre：不能仅由 integer sphere 自动推出

仅把

\[
y_1^2+y_2^2+y_3^2=H^2
\]

除去 content，只得到 primitive sphere direction。要得到

\[
\text{fixed core}\Longrightarrow\text{finite decimal fibre},
\]

还必须使用：

1. fixed core 的有限 gcd profiles；
2. multiplication carry states；
3. decimal concatenation master equation；
4. decimal depth gate；
5. SGR-1 对剩余 scale-gap state 的有限化。

所以

\[
\boxed{
\text{primitive normalization 是 Exact-Lift 的上游重写；}
}
\]

\[
\boxed{
\text{finite-fibre theorem 是 SGR-1 对该上游对象的额外全局压缩。}
}
\]

---

## 3.2 三个 carrier chamber 在 primitive-core 坐标下是什么？

Exact-Lift 使用

\[
s_i=n_i-m_i.
\]

SGR 使用同一个 quantity

\[
\delta_i=n_i-m_i.
\]

故

\[
\boxed{s_i=\delta_i.}
\]

三个 chamber 精确翻译为

\[
\boxed{
A_2\text{-only}:
\quad
\delta_3>0,\qquad
\delta_2+\delta_3\le0,
}
\tag{3.1}
\]

\[
\boxed{
DD:
\quad
\delta_3>0,\qquad
\delta_2+\delta_3>0,
}
\tag{3.2}
\]

\[
\boxed{
A_1\text{-only}:
\quad
\delta_3\le0,\qquad
\delta_2+\delta_3>0.
}
\tag{3.3}
\]

它们的身份是：

\[
\boxed{
\textbf{真实的 decimal carrier/profile states}.
}
\]

它们 **不是** primitive sphere core 的内在算术类型，因为 core 只记录球面方向：

\[
(P_1,P_2,P_3,Q_0).
\]

同一个 primitive core 原则上可以在不同 scale/gcd/carry 数据下产生不同 \(\delta\)-profile。

但三个 chamber 也不是后续消元“人为制造”的无意义分类。它们直接来自 Exact-Lift 的正权平均恒等式：

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

以及

\[
\mathcal R>r_i.
\]

所以 chamber 是真实十进制几何信息，只是比完整 SGR state 粗。

---

## 3.3 SGR profile/carry 与 carrier chamber 谁包含谁？

一个完整 SGR state \(\Sigma\) 至少固定：

- primitive core；
- gcd profile \(g_i\)；
- numerator/denominator multiplication carry bits；
- compatible digit differences；
- scale-gap state；
- decimal depth equation。

因此给定 \(\Sigma\)，\(\delta_2,\delta_3\) 已知，carrier chamber 唯一确定：

\[
\boxed{
\Sigma_{\mathrm{SGR}}
\longrightarrow
\text{carrier chamber}.
}
\tag{3.4}
\]

反向显然不成立。

仅知道 \(A_2/DD/A_1\) 的两个符号条件，不能恢复：

\[
(P_i,Q_0),\qquad
g_i,\qquad
U,V,\qquad
T,\qquad
\text{carry bits}.
\]

另一方面，进入 chamber 后 Exact-Lift 又定义了

\[
Q_{12},G,\mathcal N_{12},C,D,\kappa,\mu,\nu,\ldots
\]

这些是对具体 block values 与 tail arithmetic 的进一步信息，不能简单说“SGR 包含整个 Exact-Lift”。

正确层级为：

\[
\boxed{
\begin{array}{c}
\text{Original exact candidate}\\
\Updownarrow\\
\text{integer sphere + exact recovery}\\
\Updownarrow\\
\text{primitive core + coprime scale}\\
\Downarrow\\
\text{full SGR finite state }\Sigma\\
\Downarrow\\
\text{carrier label }(A_2,DD,A_1)
\end{array}
}
\tag{3.5}
\]

从同一个 full state 又分出两个非冗余下游通道：

\[
\boxed{
\Sigma
\longrightarrow
F_\Sigma(T)=0
}
\]

与

\[
\boxed{
\Sigma
\longrightarrow
(Q_{12},G,\mathcal N_{12},C,D,\kappa,\ldots).
}
\]

因此不能写成

\[
\text{SGR}>\text{Exact}
\]

或

\[
\text{Exact}>\text{SGR}.
\]

更准确的是：

\[
\boxed{
\text{primitive core 是共同上层；}
}
\]

\[
\boxed{
\text{SGR full state 比 carrier chamber 更细；}
}
\]

\[
\boxed{
\text{Exact block/tail arithmetic 是 chamber 后新增的信息通道；}
}
\]

\[
\boxed{
\text{SGR depth gate 与 Exact arithmetic gates 非冗余。}
}
\]

---

# 4. SGR depth quadratic 的自包含重推

本节只重新推导固定完整 state 上的 quadratic；fixed-core state set 的有限性继承 SGR-1。

## 4.1 固定 gcd profile

固定 primitive core。令

\[
L_g=\operatorname{lcm}(g_1,g_2,g_3),
\qquad
h_i=\frac{L_g}{g_i}.
\tag{4.1}
\]

从

\[
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i},
\]

以及 exact concatenation plane 消去公共尺度，可以得到 primitive-profile master equation：

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
\tag{4.2}
\]

---

## 4.2 multiplication carry bits

记

\[
u=\ell(U),
\qquad
v=\ell(V),
\qquad
T=10^v,
\]

\[
\lambda_i=\ell(C_i),
\qquad
\gamma_i=\ell(g_i).
\]

因为

\[
a_i=UC_i,
\]

两个正整数相乘的位数只有两种可能，所以存在

\[
\varepsilon_i\in\{0,1\}
\]

使

\[
\boxed{
n_i=u+\lambda_i-1+\varepsilon_i.
}
\tag{4.3}
\]

同理，因为

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
\tag{4.4}
\]

令

\[
r=u-v.
\]

则

\[
\boxed{
\delta_i
=
r+\lambda_i+\gamma_i-2+\varepsilon_i+\eta_i.
}
\tag{4.5}
\]

完整 SGR state \(\Sigma\) 中，core、gcd profile、carry bits 与 compatible \(r\)-state 均已固定。

---

## 4.3 抽出 \(T=10^v\)

由 (4.3)–(4.4)：

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

代入 (4.2)，得到

\[
\boxed{
F_{2,\Sigma}T^2+F_{1,\Sigma}T+F_{0,\Sigma}=0,
}
\tag{4.6}
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
\tag{4.7}
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
\tag{4.8}
\]

\[
\boxed{
F_{0,\Sigma}=h_3(P_3-Q_0).
}
\tag{4.9}
\]

因为 \(P_i>0\) 且

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

有

\[
P_3<Q_0,
\]

故

\[
\boxed{F_{0,\Sigma}<0.}
\tag{4.10}
\]

因此 quadratic 不可能恒等为零。

乘一个固定 \(10\)-幂清分母，可写成

\[
\boxed{
f_{2,\Sigma}T^2+f_{1,\Sigma}T+f_{0,\Sigma}=0,
\qquad
f_i\in\mathbb Z,
\qquad
f_0\neq0.
}
\tag{4.11}
\]

于是：

- 若 \(f_2\neq0\)，固定 state 至多有两个 \(T\)；
- 若 \(f_2=0,\ f_1\neq0\)，固定 state 至多有一个 \(T\)；
- 若 \(f_2=f_1=0\)，因 \(f_0\neq0\)，该 state 无候选。

### 结论等级

\[
\boxed{
\text{固定完整 SGR state}\Longrightarrow\text{至多两个 decimal depths}
}
\]

为 **PROVED**。

而

\[
\boxed{
\text{固定 primitive core}\Longrightarrow\text{完整 state 集有限}
}
\]

继承 SGR-1，故 fixed-core finite fibre 为 **DERIVED FROM PROVED RESULTS / SGR-1**。

---

# 5. 把 Exact-Lift 翻译到 primitive-profile 坐标

现在固定同一个 full state \(\Sigma\)。

## 5.1 抽出 denominator common scale

因为

\[
L_g=\operatorname{lcm}(g_i)\mid V,
\]

定义

\[
\boxed{
R=\frac{V}{L_g}.
}
\tag{5.1}
\]

则

\[
b_i=\frac V{g_i}
=
R\frac{L_g}{g_i}
=
Rh_i.
\tag{5.2}
\]

同时

\[
a_i=UC_i.
\]

定义

\[
\boxed{
\widehat Q=h_1 10^{m_2}+h_2,
}
\tag{5.3}
\]

\[
\boxed{
\widehat G=h_1h_2,
}
\tag{5.4}
\]

\[
\boxed{
\widehat{\mathcal N}
=
(C_1h_2)^2+(C_2h_1)^2.
}
\tag{5.5}
\]

则 Exact 的公共前两块对象满足

\[
\boxed{
Q_{12}=R\widehat Q,
}
\tag{5.6}
\]

\[
\boxed{
G=R^2\widehat G,
}
\tag{5.7}
\]

\[
\boxed{
\mathcal N_{12}
=
U^2R^2\widehat{\mathcal N}.
}
\tag{5.8}
\]

---

## 5.2 三个 carrier chamber 的 coefficient pair

### \(A_2\)-only

Exact-Lift 有

\[
C=a_1 10^{m_2}+10a_2,
\qquad
D=Q_{12}.
\]

定义

\[
\boxed{
\widehat C=C_1 10^{m_2}+10C_2,
\qquad
\widehat D=\widehat Q.
}
\tag{5.9}
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

Exact-Lift 有

\[
C
=
10^{m_2+k_{12}}a_1
+
10^{d_3}a_2,
\qquad
D=Q_{12}.
\]

定义

\[
\boxed{
\widehat C
=
10^{m_2+k_{12}}C_1
+
10^{d_3}C_2,
\qquad
\widehat D=\widehat Q.
}
\tag{5.10}
\]

仍有

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

Exact-Lift 有

\[
C
=
10^{g+k_{12}+m_2}a_1+a_2,
\]

\[
D=10^gQ_{12}.
\]

定义

\[
\boxed{
\widehat C
=
10^{g+k_{12}+m_2}C_1+C_2,
}
\]

\[
\boxed{
\widehat D
=
10^g\widehat Q.
}
\tag{5.11}
\]

仍有

\[
C=U\widehat C,
\qquad
D=R\widehat D.
\]

所以三 chamber 统一为

\[
\boxed{
C=U\widehat C,
\qquad
D=R\widehat D.
}
\tag{5.12}
\]

---

## 5.3 \(\kappa\) 的尺度分解

三个 branch 的 unified tail weight 可写成

\[
\boxed{
\kappa
=
\frac{10^{m_3}Q_{12}G}{b_3}.
}
\tag{5.13}
\]

因为

\[
b_3=Rh_3,
\]

定义整数量

\[
\boxed{
\widetilde\kappa
=
10^{m_3}\widehat Q\widehat G.
}
\tag{5.14}
\]

则

\[
\boxed{
\kappa
=
R^2\frac{\widetilde\kappa}{h_3}.
}
\tag{5.15}
\]

注意：\(\widetilde\kappa\in\mathbb Z\)，但不需要先验假设 \(h_3\mid\widetilde\kappa\)；实际 \(\kappa\in\mathbb Z\) 已由 Exact-Lift 的 tail construction 保证。

---

## 5.4 discriminant kernel 的尺度分解

Exact-Lift 定义

\[
K_{C,D}
=
G^2C^2-D^2\mathcal N_{12}.
\]

代入 (5.7)、(5.8)、(5.12)，定义

\[
\boxed{
\widehat K
=
\widehat G^2\widehat C^2
-
\widehat D^2\widehat{\mathcal N}.
}
\tag{5.16}
\]

得到

\[
\boxed{
K_{C,D}
=
U^2R^4\widehat K.
}
\tag{5.17}
\]

---

# 6. Exact-Lift 的两类二次门与统一判别平方

## 6.1 gap quadratic

Exact-Lift 的三个 chamber 统一满足

\[
\boxed{
D(\kappa+2G)\mu^2
-
2G\kappa C\,\mu\nu
+
\kappa D\mathcal N_{12}\nu^2
=0,
}
\tag{6.1}
\]

其中

\[
\gcd(\mu,\nu)=1.
\]

由本原性得到

\[
\boxed{
\nu\mid D(\kappa+2G),
}
\tag{6.2}
\]

\[
\boxed{
\mu\mid\kappa D\mathcal N_{12}.
}
\tag{6.3}
\]

其判别平方必要条件为

\[
\boxed{
\kappa
\left(
\kappa K_{C,D}
-
2GD^2\mathcal N_{12}
\right)
=
W^2
}
\tag{6.4}
\]

对某个整数 \(W\)。

这些均为 **PROVED / existing Exact-Lift**。

---

## 6.2 primitive tail quadratic

设

\[
10^\ell=\delta_3L,
\qquad
b_3=\delta_3\tau,
\qquad
z_3=\frac{a_3}{\delta_3}.
\]

则三个 branch 统一满足

\[
\boxed{
-\kappa(\kappa+2G)z_3^2
+
2G^2LC\,z_3
+
\mathcal C_3
=0,
}
\tag{6.5}
\]

其中

\[
\boxed{
\mathcal C_3
=
G^2L^2C^2
-
\mathcal N_{12}(LD+\tau)^2.
}
\tag{6.6}
\]

因为 \(z_3=a_3/\delta_3\) 已既约，有理根定理给出

\[
\boxed{
\delta_3\mid\kappa(\kappa+2G),
}
\tag{6.7}
\]

\[
\boxed{
a_3\mid\mathcal C_3.
}
\tag{6.8}
\]

再利用 \(L\mid\kappa\)，得到三 branch 的统一 tail certificate：

\[
\boxed{
10^\ell
\mid
\kappa^2(\kappa+2G).
}
\tag{6.9}
\]

这也是 **PROVED / existing Exact-Lift**。

---

# 7. 把 Exact discriminant square 化为 \(T\)-多项式平方门

把 (6.4) 代入第 5 节的尺度分解。

由

\[
\kappa
=
R^2\frac{\widetilde\kappa}{h_3},
\]

\[
K_{C,D}
=
U^2R^4\widehat K,
\]

\[
G=R^2\widehat G,
\qquad
D=R\widehat D,
\qquad
\mathcal N_{12}=U^2R^2\widehat{\mathcal N},
\]

得到

\[
W^2
=
U^2R^8
\frac{\widetilde\kappa}{h_3^2}
\left(
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right).
\tag{7.1}
\]

于是

\[
\left(
\frac{h_3W}{UR^4}
\right)^2
=
\widetilde\kappa
\left(
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right).
\tag{7.2}
\]

右端是整数。

若一个有理数的平方是整数，则该有理数本身是整数。因此存在

\[
Z\in\mathbb Z
\]

使

\[
\boxed{
Z^2
=
\widetilde\kappa
\left(
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right).
}
\tag{7.3}
\]

这一步严格消去了实际乘法尺度 \(U,R\)。

---

## 7.1 固定 state 后的 \(T\)-次数

固定 \(\Sigma\) 后，

\[
m_i=v-\gamma_i+1-\eta_i.
\]

故

\[
10^{m_i}
=
T\cdot
10^{-\gamma_i+1-\eta_i}.
\]

右侧系数是固定的 \(10\) 的整数次幂；若出现负指数，可在最后统一清分母。

于是：

\[
\widehat Q
=
h_1 10^{m_2}+h_2
\]

是 \(T\) 的一次式。

三 branch 中

\[
\widehat C,\widehat D
\]

也都是次数至多 \(1\) 的式子。

因此

\[
\widehat K
=
\widehat G^2\widehat C^2
-
\widehat D^2\widehat{\mathcal N}
\]

次数至多 \(2\)。

而

\[
\widetilde\kappa
=
10^{m_3}\widehat Q\widehat G
\]

次数至多 \(2\)。

所以 (7.3) 右侧是一个 \(T\) 次数至多 \(6\) 的有理系数多项式：

\[
\boxed{
\mathscr P_\Sigma(T)=Z^2,
\qquad
\deg\mathscr P_\Sigma\le6.
}
\tag{7.4}
\]

选固定正整数 \(d_\Sigma\) 清除全部系数分母，并故意乘平方 \(d_\Sigma^2\)，可等价改写为

\[
\boxed{
\mathscr P_\Sigma^*(T)=Z_*^2,
\qquad
\mathscr P_\Sigma^*\in\mathbb Z[T],
\qquad
\deg\mathscr P_\Sigma^*\le6.
}
\tag{7.5}
\]

### 结论等级

(7.3)–(7.5) 为 **PROVED**，只使用已经证明的 Exact discriminant square 与第 2–5 节的精确变量桥接。

---

# 8. 两套“二次门”的数学关系

## 8.1 不是同一个二次方程

SGR 的

\[
F_\Sigma(T)=0
\]

未知量是

\[
T=10^{\ell(V)}.
\]

Exact gap quadratic (6.1) 的未知对象是

\[
[\mu:\nu].
\]

Exact primitive tail quadratic (6.5) 的未知量是

\[
z_3=\frac{a_3}{\delta_3}.
\]

因此它们的“二次性”来自不同消元方向：

\[
\boxed{
\begin{array}{rcl}
\text{SGR} &:& \text{消去 scale mantissa，留下 decimal depth};\\
\text{Exact gap} &:& \text{消去 block balance，留下 gap slope};\\
\text{Exact tail} &:& \text{消去 tail gcd，留下 primitive rational root}.
\end{array}
}
\]

所以不能通过变量改名把三者识别成同一个方程。

---

## 8.2 也不存在一方整体严格包含另一方

SGR depth gate 本身看不到：

- \(\mathcal N_{12}\) 的二平方结构；
- \(\kappa\) 的素因子分配；
- gap ratio 的 \(\mu,\nu\) 整除；
- tail certificate
  \[
  10^\ell\mid\kappa^2(\kappa+2G);
  \]
- primitive recovery 的逐素数 gcd 数据。

反过来，Exact gap/tail quadratic 本身也没有推出：

\[
\boxed{
\text{fixed primitive core}
\Longrightarrow
\text{finite number of decimal lifts}.
}
\]

所以最准确的逻辑分类是：

\[
\boxed{
\textbf{两者是同一候选上的非冗余 gates。}
}
\tag{8.1}
\]

这对应题设的“情形 III”，但二者并非完全独立，因为它们共享同一个 primitive-state datum，可以进一步做 elimination。

---

# 9. 新 coupling：SGR depth quadratic × Exact square gate

这是本轮唯一新增的统一代数结构。

## 9.1 非退化情形

把 SGR equation 清分母、约去系数公因子后写成

\[
\boxed{
F(T)
=
f_2T^2+f_1T+f_0
=
0,
\qquad
f_i\in\mathbb Z,
\qquad
f_0\neq0.
}
\tag{9.1}
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
\tag{9.2}
\]

假设先有

\[
f_2\neq0.
\]

在 \(\mathbb Q[T]\) 中对 \(P\) 除以 \(F\)，存在

\[
Q_F(T)\in\mathbb Q[T],
\qquad
a,b\in\mathbb Q
\]

使

\[
P(T)=Q_F(T)F(T)+aT+b.
\]

对满足 \(F(T)=0\) 的候选，

\[
Z^2=aT+b.
\]

取固定正整数 \(d\) 清除 \(a,b\) 的分母，并乘平方 \(d^2\)，得到等价的

\[
\boxed{
Z_*^2=AT+B,
\qquad
A,B\in\mathbb Z.
}
\tag{9.3}
\]

令

\[
X=Z_*^2.
\]

若

\[
A\neq0,
\]

则

\[
T=\frac{X-B}{A}.
\]

代入 (9.1)，乘 \(A^2\)，得到

\[
\boxed{
\Phi_\Sigma(X)
:=
f_2X^2
+
(f_1A-2f_2B)X
+
\left(
f_2B^2-f_1AB+f_0A^2
\right)
=
0,
}
\tag{9.4}
\]

同时

\[
\boxed{X\in\mathbb Z_{\ge0}\text{ 必须是完全平方}.}
\tag{9.5}
\]

式 (9.4) 正是

\[
\boxed{
\operatorname{Res}_T
\left(
f_2T^2+f_1T+f_0,\,
X-AT-B
\right)
=0.
}
\tag{9.6}
\]

这就是本轮的 **primitive-state resultant coupling**。

---

## 9.2 退化情形必须保留

### 情形 D1：\(f_2=0,\ f_1\neq0\)

SGR depth gate 退化为线性：

\[
f_1T+f_0=0.
\]

所以

\[
\boxed{
T=-\frac{f_0}{f_1}
}
\]

被唯一确定。

此时不需要 resultant；只需检查：

1. \(T\) 是否为正整数 \(10\) 次幂；
2. \(P(T)\) 是否为整数平方；
3. actual-lift arithmetic recovery 是否成立。

这是比一般 resultant 更简单的 state check。

### 情形 D2：\(f_2=f_1=0\)

因

\[
f_0\neq0,
\]

SGR equation 无解，该 state 直接为空。

### 情形 D3：\(f_2\neq0\) 但 \(A=0\)

模 \(F\) 的 Exact square gate 退化为

\[
\boxed{
Z_*^2=B.
}
\tag{9.7}
\]

于是 \(B\) 必须是固定整数平方。

若不是，该 state 立即为空。

若是，Exact discriminant square 在“模 SGR quadratic”的 algebraic level 不再进一步限制 \(T\)，但 tail/gcd/valuation constraints 仍保留。

### 情形 D4：\(A=B=0\)

这意味着清分母后的 \(P(T)\) 被 \(F(T)\) 整除。

此时 Exact square polynomial 在 SGR root 上退化为

\[
Z_*^2=0.
\]

这并不表示整个 Exact-Lift 条件冗余；它只表示 **这一层 discriminant-square elimination** 没有提供额外状态约束。actual tail recovery、\(\mu,\nu\) divisibility、primitive gcd 与 digit windows 仍必须检查。

---

## 9.3 coupling 是否“严格更强”？

必须非常保守地区分两个概念。

式 (9.4) 是新的统一必要条件，但它是

\[
F(T)=0
\]

与

\[
P(T)=Z^2
\]

联立后消去 \(T\) 的后果。

因此它在逻辑上 **不比“两旧门同时成立”更强**。

它的推进价值是：

\[
\boxed{
\text{把两套框架中的约束压成一个只含 primitive-state 系数与平方变量 }X
\text{ 的对象。}
}
\]

这使下面几类统一攻击第一次可以直接作用在同一个式子上：

- square spacing；
- resultant divisibility；
- coefficient gcd；
- integer-gap inequalities；
- moving-core height comparison。

所以本轮有 “NEW COUPLING”，但没有产生新的 contradiction。

---

## 9.4 一个内部校验：不要把 resultant 判别式误当成新平方条件

(9.4) 作为关于 \(X\) 的二次式，其判别式为

\[
\boxed{
\operatorname{Disc}_X\Phi_\Sigma
=
A^2(f_1^2-4f_2f_0).
}
\tag{9.8}
\]

若 \(T\) 是 SGR quadratic 的根，则

\[
f_1^2-4f_2f_0
=
(2f_2T+f_1)^2.
\]

因此 resultant 的 **判别式为平方** 这一事实没有增加信息。

真正仍有内容的是：

\[
\boxed{
X\text{ 本身必须是整数完全平方}
}
\]

以及尚未被 algebraic elimination 吃掉的 actual-lift arithmetic recovery。

这一区分防止把一次形式消元误写成新的无解机制。

---

# 10. Exact tail divisibility 仍保留实际 scale 信息

虽然 normalized discriminant square (7.3) 消掉了 \(U,R\)，但 tail certificate

\[
10^\ell\mid\kappa^2(\kappa+2G)
\]

仍读取实际 denominator scale。

由

\[
\kappa
=
R^2\frac{\widetilde\kappa}{h_3},
\qquad
G=R^2\widehat G,
\]

有

\[
\boxed{
\kappa^2(\kappa+2G)
=
R^6
\frac{
\widetilde\kappa^2
\left(
\widetilde\kappa+2h_3\widehat G
\right)
}{
h_3^3
}.
}
\tag{10.1}
\]

所以对

\[
p\in\{2,5\}
\]

分别得到

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
\tag{10.2}
\]

其中

\[
R=\frac{V}{L_g}.
\]

这说明统一后至少存在两种性质不同的信息：

### Algebraic/state channel

\[
F_\Sigma(T)=0
\]

与

\[
P_\Sigma(T)=Z^2
\]

可通过 resultant 耦合。

### Actual-lift arithmetic channel

\[
10^\ell\mid\kappa^2(\kappa+2G),
\]

以及

\[
\nu\mid D(\kappa+2G),
\qquad
\mu\mid\kappa D\mathcal N_{12},
\]

primitive recovery gcd、digit windows、逐项既约等，仍保留实际 \(U,V,R\) 的算术。

因此不能把整个 Strict Layer 误压成“只研究一个 resultant polynomial”。

---

# 11. fixed primitive core finite fibre 对 Exact-Lift 的影响

SGR-1 的核心结论为：

\[
\boxed{
\text{固定 primitive sphere core}
\Longrightarrow
\text{strict decimal lift fibre 有限}.
}
\tag{11.1}
\]

结合第 4 节，可更具体地理解为：

\[
\text{fixed core}
\Longrightarrow
\text{finite full states}
\Longrightarrow
\text{每 state 至多两个 }T.
\]

---

## 11.1 无穷候选必迫使 \(Q_0\to\infty\)

假设存在无穷多个 strict-layer exact candidates。

若 primitive-core height \(Q_0\) 有界，则正整数 primitive quadruples

\[
(P_1,P_2,P_3,Q_0)
\]

只有有限多个。

每个固定 core 又只有有限多个 strict decimal lifts。

故总候选数只能有限，矛盾。

所以：

\[
\boxed{
\text{任何无穷 strict-layer exact-candidate sequence 必有 }
Q_0\to\infty.
}
\tag{11.2}
\]

这是 **DERIVED FROM PROVED RESULTS**。

---

## 11.2 对 DD 的意义

旧 Exact-Lift 把 DD 的无界危险压在顶部尖角：

\[
10S_{12}+11
\le
n_3
\le
11S_{12}+3,
\]

并伴随：

- extreme denominator asymmetry；
- \(2/5\)-adic double resonance；
- near-square；
- near-\(S\)-unit。

SGR finite fibre 排除了下面这种逃逸模型：

\[
\boxed{
\text{固定 primitive sphere direction}
+
\text{第三尾无限增长}.
}
\]

因此若 DD 真存在无穷候选序列，则必须同时发生

\[
\boxed{
Q_0\to\infty.
}
\]

所以 DD 的无界终止问题应重新理解为

\[
\boxed{
\text{moving primitive core}
+
\text{DD state constraints}
+
\text{coupled gates}.
}
\]

这没有关闭 DD，但严格删除了一个“固定 core、tail 自由逃逸”的无界自由度。

---

## 11.3 对 \(A_2\)-only 的意义

旧 \(A_2\) deep-even / double-Hensel 描述中，\(m_2\) 与 tail state 看起来可以无限增长。

统一后：

- 对固定 primitive core，\(m_2\)、\(m_3\)、\(\ell(V)\) 不可能产生无限 lift family；
- 任何 \(m_2\to\infty\) 的 exact candidate sequence 都必须伴随
  \[
  Q_0\to\infty.
  \]

因此 \(A_2\) 的真正全局难题不是“一个固定 core 上 Hensel 深度可否无限”，而是 moving core 时，Hensel contact、decimal window 与 unified gates 能否持续兼容。

---

## 11.4 对 \(A_1\)-only 的意义

旧 \(A_1\) saturated \(L=1\) 中最危险的是 decimal shift \(g\)。

SGR finite fibre 同样说明：

\[
\boxed{
\text{固定 primitive core 上 }g\text{ 不可能形成无穷 exact-lift tail}.
}
\]

如果存在 \(g\to\infty\) 的 exact candidate sequence，则必同时有

\[
Q_0\to\infty.
\]

因此 \(g\) 不再是一个可独立于 sphere core 漂移的 top-level infinity。

---

## 11.5 “只剩一个 moving core 参数”需要怎样理解？

不能把 (11.2) 夸大成：

> 整个问题只剩一个整数 \(Q_0\)。

因为当 \(Q_0\to\infty\) 时，

\[
P_i,\quad
g_i,\quad
\Sigma,\quad
U,V,\quad
\kappa,\ldots
\]

都可能协同变化。

严格成立的是：

\[
\boxed{
\text{固定 base core 的 fibre 已有限，因此 top-level 的无界性只能来自 base core 本身移动。}
}
\]

这是“无界自由度来源”的统一，而不是把所有坐标真正降成一个标量。

---

## 11.6 对旧 near-square / near-\(S\)-unit / square-spacing 语言的重新解释

**HEURISTIC.**

目前合理的统一理解是：

\[
\text{near-square},
\quad
\text{near-}S\text{-unit},
\quad
\text{double-Hensel},
\quad
\text{square-spacing}
\]

很可能不是四个彼此独立的 terminal phenomena，而是 moving primitive core 在不同 carrier states 下投影出的不同局部症状。

本轮没有证明它们可以被一个单独恒等式统一删除，因此这只作为研究解释，不升级为 theorem。

---

# 12. 重新定义 Strict-Layer Frontier

旧 strict-layer 讨论存在两套列表：

- SGR 侧的多个 \(O_i\) / terminal directions；
- Exact-Lift 侧的 \(A_2\)、DD、\(A_1\)。

统一后不应再把它们平铺成多个同等级 terminal obligations。

---

## 12.1 Unified Strict Exact Lift datum

定义

\[
\boxed{
\mathfrak L
=
\left(
\mathcal P,\Sigma,T,U,V;
Q_{12},G,\mathcal N_{12},C,D,\kappa,\mu,\nu,\ldots
\right),
}
\tag{12.1}
\]

其中

\[
\mathcal P=(P_1,P_2,P_3,Q_0)
\]

是 primitive core，

\[
\Sigma
\]

是 fixed-core finite gcd/carry/profile state。

一个真实 strict candidate 必须同时满足三组 **conjunctive gates**。

### G1 — SGR depth gate

\[
\boxed{
F_\Sigma(T)=0.
}
\tag{12.2}
\]

### G2 — Exact normalized square gate

\[
\boxed{
P_\Sigma(T)=Z^2.
}
\tag{12.3}
\]

等价地，在一般情形可用 coupling

\[
\boxed{
\Phi_\Sigma(Z_*^2)=0.
}
\tag{12.4}
\]

### G3 — actual-lift arithmetic recovery

至少包括：

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G),
}
\tag{12.5}
\]

\[
\boxed{
\nu\mid D(\kappa+2G),
\qquad
\mu\mid\kappa D\mathcal N_{12},
}
\tag{12.6}
\]

以及：

- primitive recovery gcd；
- digit windows；
- positivity；
-逐项既约；
- exact concatenation recovery。

这些条件是 **同时必须成立** 的。

但这不等于需要分别证明三个 lemma：

\[
G1\text{ 无解},\quad G2\text{ 无解},\quad G3\text{ 无解}.
\]

只要证明三者的交为空即可；一个成功的统一 argument 可能同时使用 G1+G2+G3，也可能仅由其中某一组在 moving-core regime 下直接产生 contradiction。

---

## 12.2 最小 dependency graph

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
\text{Primitive Core }\mathcal P
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
(\text{gcd/carry/profile; carrier is a coarse label})
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
\text{actual arithmetic recovery}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\textbf{Moving Primitive-Core Uniform Termination}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{Strict Layer Empty}.
}
\tag{12.7}
\]

---

## 12.3 真正的 terminal obligations 与 alternative attack routes

### 唯一顶层 conjunctive terminal obligation

\[
\boxed{
\textbf{T\(_{\rm move}\): Moving Primitive-Core Uniform Termination}.
}
\]

其精确定义是：

> 不存在一列 \(Q_0\to\infty\) 的 primitive cores 与相容 states \(\Sigma\)，使 SGR depth、Exact square、tail/gcd/\(2,5\)-adic recovery 和 exact reconstruction 同时成立。

这是本轮统一后的唯一顶层独立义务。

### 不是额外 obligations，而是 alternative attack routes

下面两条是不同证明路线，任何一条若能统一闭合即可完成 \(T_{\rm move}\)；它们不是必须依次完成的两个 lemmas：

1. **Resultant-square route**  
   从
   \[
   \Phi_\Sigma(X)=0,\qquad X=\square
   \]
   建立 uniform square-spacing / height / divisibility obstruction。

2. **Actual-recovery route**  
   把
   \[
   10^\ell\mid\kappa^2(\kappa+2G)
   \]
   的 \(2/5\)-进容量与 SGR depth root、primitive-core height 联立，得到统一不等式或容量矛盾。

二者可以最终合并，但当前不应把它们列成“必须全部证明”的两个独立 terminal targets。

---

# 13. 本轮结果分级

## PROVED

1. SGR primitive normalization 与 Exact integer sphere + primitive recovery 的双向变量桥；
2.
   \[
   q=V,\qquad y_i=UP_i,\qquad H=UQ_0;
   \]
3. carrier chamber 是 decimal profile 的真实粗投影，不是 primitive core 算术类型；
4. 固定完整 SGR state 上的 exact quadratic depth gate；
5. Exact discriminant square 在 primitive-profile 坐标中消除公共尺度 \(U,R\)；
6.
   \[
   P_\Sigma(T)=Z^2,\qquad \deg P_\Sigma\le6;
   \]
7. SGR quadratic 与 Exact square gate 的 resultant coupling (9.4)，含全部退化情形；
8. tail certificate 在 primitive-profile 坐标下的 \(2/5\)-adic capacity 式 (10.2)。

## DERIVED FROM PROVED RESULTS

1. fixed-core finite fibre 对 \(A_2\)、DD、\(A_1\) 同时成立；
2.
   \[
   \text{infinite strict candidates}\Longrightarrow Q_0\to\infty;
   \]
3. 旧三个 carrier frontier 的“固定 core 长尾逃逸”全部被排除；
4. strict-layer top-level unboundedness 可统一表述为 moving primitive core termination。

## COMPUTATIONAL EVIDENCE

本轮没有新增计算证据，也没有用有限搜索支持任何新全局结论。

## HEURISTIC

near-square、near-\(S\)-unit、double-Hensel、square-spacing 可能是 moving-core termination 的不同局部投影。

## OPEN OBLIGATION

\[
\boxed{
\textbf{Moving Primitive-Core Uniform Termination}.
}
\]

---

# 14. 下一轮只推荐两个 terminal targets

本轮不建议立刻恢复 \(A_2/DD/A_1\) 三个旧列表逐个深攻。更值得单独开 chat 的目标只有以下两个。

## Target 1 — Moving-Core Resultant Square Obstruction

研究统一 family

\[
\boxed{
\Phi_\Sigma(X)=0,
\qquad
X=Z^2,
\qquad
Q_0\to\infty,
}
\]

其中 \(\Sigma\) 遍历每个 core 的有限 state set。

目标不是再做固定模数搜索，而是寻找对所有 moving cores 有效的：

- square-spacing；
- coefficient gcd；
- root separation；
- height inequality；
- resultant divisibility；

最终得到一个 uniform obstruction 或 \(Q_0\) 上界。

这是本轮新 coupling 最自然的直接后续。

---

## Target 2 — Moving-Core \(2/5\)-Adic Capacity Coupling

把

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G)
}
\]

翻译成第 10 节的 primitive-profile valuation capacity，并与：

\[
F_\Sigma(T)=0,
\qquad
T=10^{\ell(V)},
\]

以及 primitive core height \(Q_0\) 联立。

目标是证明 moving core 无法同时提供：

- 正确 decimal depth；
- 足够 \(2\)-adic capacity；
- 足够 \(5\)-adic capacity；
- Exact discriminant square。

若成功，这一路可能一次覆盖 \(A_2\)、DD、\(A_1\)，而不需要重新逐 chamber 开局。

---

# 15. 最终裁决

\[
\boxed{
\textbf{SGR-2B — UNIFICATION + NEW COUPLING}.
}
\]

理由：

1. 两套变量已经严格双向对接；
2. primitive core、full SGR state、carrier chamber、Exact block arithmetic 的层级已经澄清；
3. SGR depth quadratic 与 Exact gap/tail quadratics 被证明是不同消元投影；
4. Exact discriminant square 已被翻译成同一 primitive-state 上的 \(T\)-polynomial square gate；
5. 两门联立得到新的 state-level resultant
   \[
   \boxed{\Phi_\Sigma(Z_*^2)=0};
   \]
6. resultant 的退化状态已经全部保留，没有偷偷假设 \(f_2A_\Sigma\neq0\)；
7. actual tail divisibility 被证明仍保存独立的 \(2/5\)-adic scale information，因此没有被错误地吸收到 resultant 中；
8. fixed-core finite fibre 把三个旧 carrier frontier 的共同无界源统一压成
   \[
   \boxed{Q_0\to\infty};
   \]
9. strict-layer top-level frontier 因而可压成一个真正独立的 terminal obligation：
   \[
   \boxed{
   \textbf{Moving Primitive-Core Uniform Termination}.
   }
   \]

本轮没有证明 Strict Layer Empty。

本轮也没有声称 resultant 比“两套旧条件联立”更强；其价值是消除重复框架，并把二者变成一个适合下一轮统一终止研究的共同代数对象。
