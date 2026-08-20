# 三项十进制拼接平方和问题：A1 Unified Moving-Profile Terminal Campaign

**文件名：** `strict_layer_A1_unified_moving_profile_terminal_campaign.md`  
**研究范围：** Strict Layer，仅研究 `A1-only`；DD 保持 closed。  
**本轮最终状态：**

\[
\boxed{\textbf{A1 NOT CLOSED}}
\]

但本轮完成了 forward/backward 的正式语义合流，并得到五项新的统一终端结构：

1. **Full Interface Equivalence / Backward Redundancy Certificate**：A1 的 exact terminal witness 可以压成 primitive sphere + exact master + reduced common scale；backward WGF / phase / Gaussian 数据全部是派生视图。
2. **Exact Axis-Mantissa Quantization**：\(\Theta=Q_0-P_2\) 的真实尺度被压成一个固定 compact mantissa 乘 \(Q_0 10^{-2k}\)，并把 \(g\ge1\) 的旧 \(10^{2k}<5Q_0\) 改善到 \(<2.532Q_0\)。
3. **Sharp Integer Radial Margin Theorem**：common integer \(U\) 相比 continuous cone 确实增加一个精确的一格 lattice margin；但该 margin 被一个已知 synchronized real-cone state 压力测试后证明**不足以单独闭合**。
4. **Unified Decimal Defect Identity**：forward mantissa defect、GSYNC、backward primitive tail quotient 与 \(10^g\)-divisibility 可统一为一个普通整数 \(\Omega\) 的单一恒等式。
5. **Axis Small-Shift GCD Theorem**：\(d_Q:=\gcd(Q_0,V)\)、\(g_2\) 与 \(\Theta\) 满足
   \[
   \gcd(d_Q,g_2)\mid\Theta,
   \qquad
   d_Qg_2\le V\Theta,
   \qquad
   d_Q\le b_2\Theta.
   \]
   该结构在 bounded-\(\Theta\) 分支非常强，但当前缺少与之配对的 lower bound on \(d_Q/b_2\)。

本轮最重要的**负结论**同样明确：

\[
\boxed{
\text{现有 size geometry + exact master 不能推出 }\Theta=O(1).
}
\]

真正的缺口不是再找一个局部同余，而是把：

\[
\boxed{
\text{ordinary coprime radial successor}
\quad\text{与}\quad
\text{quantized decimal defect }\Omega
}
\]

做成一个 uniform exclusion theorem。

---

# 1. Executive Summary

## 1.1 FROZEN — Strict Layer 当前状态

\[
\boxed{DD=\varnothing.}
\]

DD 不再是开放 frontier。本轮不重新研究 DD orientation、double resonance、root-pair fibre 或 tail window。

Strict Layer 唯一剩余 chamber：

\[
\boxed{A_1\text{-only}.}
\]

---

## 1.2 FROZEN — forward/backward 已经语义会合

对一个 exact A1 witness，取 reduced common scale

\[
\lambda=\frac UV,
\qquad
U,V\in\mathbf Z_{>0},
\qquad
\gcd(U,V)=1,
\]

primitive sphere

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

定义

\[
g_i=\gcd(V,P_i),
\qquad
C_i=\frac{P_i}{g_i},
\]

\[
a_i=UC_i,
\qquad
b_i=\frac V{g_i}.
\]

则所有真实 blocks、digit lengths、A1 exponents 都唯一恢复。

因此 exact witness dimension 最小可写为：

\[
\boxed{
(P_1,P_2,P_3,Q_0;\lambda=U/V)
}
\]

外加“由这些数据恢复出的 blocks 满足 exact decimal master 与 A1 chamber”的谓词。

backward 中的

\[
N,\Delta,N^\sharp,\delta,Z_\pm,R_2,R_5,\varepsilon^\sharp
\]

不再增加 candidate semantics；它们只是在这个 terminal witness 上的派生 arithmetic views。

**状态：FROZEN / PROVENANCE-AUDITED.**

---

## 1.3 NEW PROVED — 本轮真正的新普通整数 normal form

定义

\[
D:=P_1 10^k-Q_0>0,
\]

\[
\boxed{
\Omega
:=
 b_2Q_0-b_1 10^{m_2}D.
}
\tag{UDD-0}
\]

flat locus 已删除，所以

\[
\boxed{\Omega\ne0.}
\]

再定义第三尾 ordinary integer

\[
\boxed{
\tau_3
:=
\frac{b_3(Q_0-P_3)}{10^{n_3}}.
}
\tag{UDD-T}
\]

exact master 自动给

\[
\tau_3\in\mathbf Z_{>0}.
\]

然后 GSYNC / master **完全等价地**压成：

\[
\boxed{
 b_2P_2-\tau_3
=
10^g\Omega.
}
\tag{UDD}
\]

这是本轮最重要的新统一恒等式之一。

它说明：

- forward 的 \(\varepsilon-\beta_2\) mantissa defect；
- primitive GSYNC；
- backward 的 third-tail quotient；
- decimal power \(10^g\)；

其实是同一个 ordinary-integer defect 的四种写法。

---

## 1.4 NEW PROVED — axis gap 的 exact compact mantissa

令

\[
\Theta:=Q_0-P_2>0,
\qquad
x:=\frac{P_2}{Q_0},
\qquad
 y:=\frac{P_3}{Q_0}.
\]

已有 exact leading defect

\[
\varepsilon
=
\frac{b_1D}{Q_0}\in(0,1),
\]

因此定义

\[
\boxed{
r_1:=10^k\frac{P_1}{Q_0}
=1+\frac{\varepsilon}{b_1}
\in(1,2).
}
\]

再定义

\[
\boxed{
r_3:=10^{2g+k}\frac{P_3}{Q_0}.
}
\]

则 sphere 精确给

\[
\boxed{
T_\Theta
:=
10^{2k}\frac{\Theta}{Q_0}
=
\frac{r_1^2+10^{-4g}r_3^2}{1+x}.
}
\tag{AX-M}
\]

对 \(g\ge1\)，已有

\[
x>\sqrt{96/101}>0.9749,
\]

并由 primitive ratio window 得 \(r_3<100\)。所以

\[
\boxed{
\frac12<T_\Theta
<
\frac5{1+\sqrt{96/101}}
<2.532.
}
\tag{AX-M1}
\]

若 \(g\ge2\)，更有

\[
\boxed{
\frac12<T_\Theta<2.026.
}
\tag{AX-M2}
\]

于是：

\[
\boxed{
\Theta
\asymp
Q_0 10^{-2k}
}
\]

不只是粗 \(\asymp\)，而是有 uniform compact mantissa。

由 \(\Theta\ge1\) 立即改善旧 height bound：

\[
\boxed{
10^{2k}
<
\frac5{1+\sqrt{96/101}}Q_0
<2.532Q_0
\qquad(g\ge1).
}
\tag{K-NEW}
\]

**状态：NEW PROVED.**

---

## 1.5 NEW PROVED — Sharp Integer Radial Margin

若同一个正整数 \(U\) 同时实现第二、三 numerator blocks：

\[
10^{n_2-1}\le UC_2<10^{n_2},
\]

\[
10^{n_3-1}\le UC_3<10^{n_3},
\]

则因为 \(UC_i\) 为整数，实际有

\[
10^{n_i-1}\le UC_i\le10^{n_i}-1.
\]

消去 \(U\) 得：

\[
\boxed{
\frac{10^{n_2-1}}{10^{n_3}-1}
\le
\frac{C_2}{C_3}
\le
\frac{10^{n_2}-1}{10^{n_3-1}}.
}
\tag{IRM-R}
\]

等价于两个 exact positive integer margins：

\[
\boxed{
10^{n_3}C_2-10^{n_2-1}C_3\ge C_2,
}
\tag{IRM-}
\]

\[
\boxed{
10^{n_2}C_3-10^{n_3-1}C_2\ge C_3.
}
\tag{IRM+}
\]

这就是本轮要求寻找的：

\[
\boxed{\textbf{Integer Radial Margin Theorem}.}
\]

它严格强于 continuous ratio cone，但后文证明它本身仍不足以闭 A1。

**状态：NEW PROVED / SHARP.**

---

# 2. Unified Dependency DAG

本轮以后依赖图统一如下。

## 2.1 Semantic / terminal layer

### Primitive arithmetic

\[
(P_1,P_2,P_3,Q_0),
\qquad
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

### Reduced radial scale

\[
\lambda=U/V,
\qquad
\gcd(U,V)=1.
\]

### Canonical gcd profile

\[
g_i=\gcd(V,P_i),
\qquad
C_i=P_i/g_i,
\]

\[
b_i=V/g_i,
\qquad
 a_i=UC_i.
\]

### Decimal semantics

\[
n_i=\ell(a_i),
\qquad
m_i=\ell(b_i),
\]

A1：

\[
s_3=n_3-m_3=-g\le0,
\]

\[
s_2+s_3=k\ge1.
\]

### Exact master

令

\[
\mathbf A^\sharp
=C_1 10^{n_2+n_3}+C_2 10^{n_3}+C_3,
\]

\[
\mathbf B
=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3.
\]

则

\[
\boxed{
V\mathbf A^\sharp=Q_0\mathbf B.
}
\tag{MASTER}
\]

这与当前 exact GSYNC presentation 等价。

---

## 2.2 Derived backward layer

从 semantic witness 派生：

\[
H=C_1 10^{n_2}+C_2,
\]

\[
\Pi=UH,
\]

\[
\mathbf A=U\mathbf A^\sharp,
\]

\[
N=U^2N^\sharp,
\]

\[
\Delta=U\delta.
\]

以及：

\[
Z_-=rac{Q_0-P_3}{\gcd(Q_0,P_3)},
\qquad
Z_+=\frac{Q_0+P_3}{\gcd(Q_0,P_3)}.
\]

partial \(2/5\)-phase、WGF、Gaussian factorization、norm resonance 全部从这些量派生。

因此依赖方向必须冻结为：

\[
\boxed{
\text{semantic terminal state}
\Longrightarrow
\text{backward toolkit},
}
\]

而不是反过来把 toolkit 当 candidate gate。

---

# 3. Full Interface Equivalence

## Theorem A1-UIE — Unified Interface Equivalence

以下两件事等价。

### (A) Original admissible A1 candidate

存在三组 reduced positive rational blocks

\[
\frac{a_i}{b_i}
\]

满足原三项平方和 = 拼接平方、真实 decimal block、Strict A1 inequalities。

### (B) Exact synchronized primitive state + legal common integer radial scale

存在：

\[
(P_1,P_2,P_3,Q_0),
\qquad
U,V,
\]

满足：

1. primitive sphere；
2. \(\gcd(U,V)=1\)；
3. \(g_i=\gcd(V,P_i)\)；
4. \(a_i=UP_i/g_i\)，\(b_i=V/g_i\)；
5. digit windows 与 A1 exponents；
6. exact master (MASTER)。

### Proof

(B) \(\Rightarrow\) (A)：

每个 block：

\[
\frac{a_i}{b_i}
=
\frac{UP_i/g_i}{V/g_i}
=
\frac UVP_i.
\]

所以 sphere 给

\[
\sum_i\left(\frac{a_i}{b_i}\right)^2
=\left(\frac UVQ_0\right)^2.
\]

另一方面

\[
\mathbf A=U\mathbf A^\sharp,
\]

MASTER 给

\[
\frac{\mathbf A}{\mathbf B}
=
\frac{UQ_0}{V}.
\]

故原平方和 equality 成立。

逐块 reducedness 自动成立，因为

\[
\gcd(C_i,b_i)=1,
\]

再结合 \(\gcd(U,V)=1\)。digit/A1 hypotheses 保证原 decimal semantics。

(A) \(\Rightarrow\) (B) 是 canonical primitive normalization。

\[
\boxed{\text{QED}.}
\]

因此 common-\(U\) 之后不存在一个独立的“backward norm gate”。

**状态：FROZEN + RECONSTRUCTED PROOF.**

---

# 4. Exponent Normal Form

统一记：

\[
g=m_3-n_3\ge0,
\]

\[
k=(n_2-m_2)+(n_3-m_3)\ge1.
\]

所以

\[
n_2-m_2=g+k.
\]

定义

\[
\boxed{d:=m_2-g.}
\]

则所有第二、三块 exponents 可写为：

\[
\boxed{
m_2=g+d,
}
\]

\[
\boxed{
n_2=2g+k+d,
}
\]

\[
\boxed{
m_3=n_3+g.
}
\]

因此 geometric moving exponents 只需：

\[
\boxed{(g,k,d)}
\]

而 \(n_3\) 是一个独立的 **decimal lattice-depth coordinate**，主要进入：

- common-\(U\) endpoint grid；
- third-tail divisibility；
- local \(2/5\)-phase visibility。

对于 \(g\ge1\)，已有：

\[
\text{plus}\Rightarrow d\le1,
\]

\[
\text{minus}\Rightarrow d\ge-1.
\]

故真正 sign-sensitive transition strip 只有：

\[
\boxed{d\in\{-1,0,1\}.}
\]

但两个 half-lines 不能因此删除；它们仍可能承载 exact states。

---

# 5. Minimal Moving Coordinates

必须区分两种“最小”。

## 5.1 Exact semantic minimum

\[
\boxed{
(P_1,P_2,P_3,Q_0;U,V)
}
\]

其中 \(U/V\) reduced。

因为这组数据唯一恢复：

\[
g_i,C_i,a_i,b_i,n_i,m_i,g,k,d.
\]

---

## 5.2 Analytic moving chart

对 \(P_2\)-axis analysis，最有用的 reduced chart 是：

\[
\boxed{
(Q_0;g,k,d;n_3;
\varepsilon,\beta_2,\beta_3;
\Theta;d_Q)
}
\]

其中

\[
\beta_i=b_i/10^{m_i}\in[0.1,1),
\]

\[
d_Q:=\gcd(Q_0,V).
\]

实际上 \(\Theta\) 由 sphere + \(P_1,P_3\) 决定，\(\varepsilon\) 决定 \(P_1/Q_0\)，所以 projective geometry 可以进一步压成：

\[
\boxed{
(g,k,d)
+
(\varepsilon,\beta_2,\beta_3,r_3)
+
Q_0.
}
\]

但如果要保留 integer/gcd semantics，不能把 \(V,d_Q,n_3\) 永久删除。

---

# 6. Common-\(U\) Radial Gate

定义：

\[
I_2=
\left[
\frac{10^{n_2-1}}{C_2},
\frac{10^{n_2}}{C_2}
\right),
\]

\[
I_3=
\left[
\frac{10^{n_3-1}}{C_3},
\frac{10^{n_3}}{C_3}
\right).
\]

\[
I_{23}=I_2\cap I_3=[L,R).
\]

exact terminal gate：

\[
\boxed{
N_V(L,R)>0,
}
\]

其中

\[
N_V(L,R)=
\#\{u\in\mathbf Z_{>0}\cap[L,R):\gcd(u,V)=1\}.
\]

---

## 6.1 NEW PROVED — only two active endpoint configurations

每个 interval 都是

\[
I_i=[L_i,10L_i).
\]

因此 lower endpoint 与 upper endpoint 的 ordering 相同。

若 \(L_2\ge L_3\)，则

\[
L=L_2,
\qquad
R=10L_3=R_3.
\]

若 \(L_3\ge L_2\)，则

\[
L=L_3,
\qquad
R=R_2.
\]

所以 prompt 中形式上的四种 active pairs 实际压成：

\[
\boxed{(L_2,R_3)\quad\text{或}\quad(L_3,R_2).}
\]

**状态：NEW PROVED.**

---

## 6.2 Canonical integer successor

忽略 coprime 时：

\[
I_{23}\cap\mathbf Z_{>0}\ne\varnothing
\iff
\boxed{\lceil L\rceil<R.}
\]

因此 integer feasibility 永远由 canonical least integer

\[
U_*=\lceil L\rceil
\]

见证。

带 coprime 时可定义：

\[
\operatorname{next}_V(L)
:=
\min\{u\in\mathbf Z_{>0}:u\ge L,\gcd(u,V)=1\}.
\]

则

\[
\boxed{
N_V(L,R)>0
\iff
\operatorname{next}_V(L)<R.
}
\tag{SUCCESSOR}
\]

这把最终 radial gate 压成一个一维 ordinary coprime-successor 问题。

---

# 7. Integer Radial Margin Theorem

## 7.1 Active-endpoint form

若存在 integer \(U\in[L,R)\)，且 active upper endpoint 为

\[
R=\frac{10^{n_j}}{C_j},
\]

则因为

\[
10^{n_j}-UC_j\in\mathbf Z_{\ge1},
\]

有

\[
\boxed{
R-U\ge\frac1{C_j}.
}
\]

所以

\[
\boxed{
R-L\ge\frac1{C_j}.
}
\tag{IRM-W}
\]

这就是最直接的 lattice-step lower bound。

---

## 7.2 Two-sided ratio form

更强的 projection 是 (IRM-) 与 (IRM+)：

\[
10^{n_3}C_2-10^{n_2-1}C_3\ge C_2,
\]

\[
10^{n_2}C_3-10^{n_3-1}C_2\ge C_3.
\]

令

\[
R_\alpha
:=
10^{n_3-n_2}\frac{C_2}{C_3}.
\]

因为

\[
R_\alpha=\frac{\alpha_2}{\alpha_3},
\qquad
\alpha_i:=a_i/10^{n_i}\in[0.1,1),
\]

可归一化成：

\[
\boxed{
\frac1{10(1-10^{-n_3})}
\le R_\alpha
\le
10(1-10^{-n_2}).
}
\tag{IRM-N}
\]

continuous cone 只有

\[
0.1<R_\alpha<10.
\]

所以 integer radial realization 确实把两侧边界向内推了一格。

---

## 7.3 Sharpness

下侧 equality 要求同时：

\[
a_2=10^{n_2-1},
\qquad
 a_3=10^{n_3}-1.
\]

由于

\[
U\mid a_2,
\qquad
U\mid a_3,
\]

而

\[
\gcd(10^{n_2-1},10^{n_3}-1)=1,
\]

故 equality 强迫：

\[
\boxed{U=1.}
\]

上侧同理。

因此：

- theorem 常数是 sharp；
- 若 \(U>1\)，两个 margin 至少严格多一单位 integer defect。

---

## 7.4 DISPROVED — margin alone closes A1

使用已知 synchronized real-cone point：

\[
(P_1,P_2,P_3,Q_0)
=(7776,71252,7899,72109),
\]

\[
V=24,
\quad
(g_1,g_2,g_3)=(24,4,3),
\]

故

\[
C_2=17813,
\qquad
C_3=2633,
\]

formal profile

\[
n_2=2,
\qquad n_3=1.
\]

两侧 integer-margin numerators 为：

\[
10C_2-10C_3=151800>C_2,
\]

\[
100C_3-C_2=245487>C_3.
\]

所以两个 sharp margin **都满足**。

但

\[
I_{23}
=
\left[
\frac{10}{17813},
\frac{10}{2633}
\right)
\subset(0,1).
\]

故没有 positive integer \(U\)。

因此：

\[
\boxed{
\textbf{Integer Radial Margin is true and sharp, but not a terminal killer.}
}
\]

它必须与 radial location / successor condition 一起使用。

**状态：NEW DISPROVED ROUTE.**

---

# 8. Exact \(P_2\)-Axis Geometry

sphere：

\[
\boxed{
\Theta(2Q_0-\Theta)=P_1^2+P_3^2.
}
\tag{AX}
\]

已有：

\[
10^{-k}
<\frac{P_1}{Q_0}
<2\cdot10^{-k},
\]

且

\[
\frac{P_3}{Q_0}
\asymp
10^{-(2g+k)}.
\]

所以 (AX-M) 给出了最精确的 uniform scale：

\[
\boxed{
\Theta
=
T_\Theta\frac{Q_0}{10^{2k}},
}
\]

其中 growing-\(g\) chamber 的 \(T_\Theta\) 落固定 compact interval。

---

## 8.1 Exact meaning of “critical \(k\)”

在 \(g\ge1\) 中，因为 \(T_\Theta\) bounded above and below：

\[
\boxed{
\Theta=O(1)
\iff
\frac{Q_0}{10^{2k}}=O(1).
}
\]

等价写成 additive criticality：

\[
\boxed{
\Theta=O(1)
\iff
k\ge\frac12\log_{10}Q_0-O(1).
}
\tag{CRIT}
\]

已有 theorem 只给反方向：

\[
k\le\frac12\log_{10}Q_0+O(1).
\]

所以 bounded-axis-gap 的真正缺口正是一个 lower critical bound on \(k\)。

---

## 8.2 Tropical scale of \(\Theta\)

若沿 infinite sequence：

\[
\kappa
:=
\lim\frac{k}{\log_{10}Q_0}
\]

存在，则 compact \(T_\Theta\) 给：

\[
\boxed{
\frac{\log\Theta}{\log Q_0}
=
1-2\kappa+o(1).
}
\tag{TH-SLOPE}
\]

因此：

- \(\kappa<1/2\)：\(\Theta\) 按正幂增长；
- \(\kappa=1/2\)：只知道 \(\Theta=Q_0^{o(1)}\)，**不等于 bounded**；
- bounded \(\Theta\) 需要 additive version (CRIT)。

---

# 9. Axis-Gap Boundedness Campaign

## 9.1 OPEN — uniform boundedness

本轮没有证明：

\[
\boxed{\Theta=O(1).}
\]

而且现有 size/tropical system 明确留下：

\[
0\le\kappa\le1/2,
\]

的整段 freedom。

所以不能把旧 \(k\)-upper bound误读成临界窗。

---

## 9.2 PROVED NEGATIVE — master alone cannot bound \(\Theta\)

此前 exact synchronized polynomial family 固定：

\[
g=0,
\qquad k=1,
\]

且满足 primitive sphere + exact GSYNC + fixed gcd profile，却死在 common-\(U\) gate。

其 primitive reductions 中：

\[
\frac{\Theta}{Q_0}
\to
\frac{597312720-4\cdot44000352}{597312720}
\approx0.7053446.
\]

所以沿该 synchronized family：

\[
\boxed{
\Theta\asymp Q_0\to\infty.
}
\]

因此任何 Axis-Gap Boundedness proof **必须真正使用 integer radial realization**；sphere + GSYNC/master 不够。

**状态：PROVED NEGATIVE THEOREM.**

---

# 10. Unified Decimal Defect Identity

现在正式推导 (UDD)。

由

\[
VC_i=b_iP_i,
\]

MASTER 等价于：

\[
 b_1P_1 10^{n_2+n_3}
+b_2P_2 10^{n_3}
+b_3P_3
\]

\[
=
Q_0
\left(
 b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3
\right).
\]

使用

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g,
\]

和

\[
D=P_1 10^k-Q_0,
\]

得到：

\[
 b_1D10^{m_2+m_3}
=
 b_2Q_0 10^{m_3}
-b_2P_2 10^{n_3}
+b_3(Q_0-P_3).
\]

右边前两项都显含 \(10^{n_3}\)，故：

\[
10^{n_3}\mid b_3(Q_0-P_3).
\]

定义 \(\tau_3\) 后除去 \(10^{n_3}\)：

\[
 b_1D10^{m_2+g}
=
 b_2Q_0 10^g
-b_2P_2
+\tau_3.
\]

重排即：

\[
\boxed{
 b_2P_2-\tau_3
=10^g
\left(
 b_2Q_0-b_1 10^{m_2}D
\right).
}
\]

即 (UDD)。

---

## 10.1 Relation to GSYNC

\[
\Delta_{12}
=
 g_2 10^{m_2}D-g_1Q_0.
\]

由

\[
g_i=V/b_i
\]

可得

\[
\boxed{
\Delta_{12}
=-\frac{V}{b_1b_2}\Omega.
}
\tag{OMEGA-DELTA}
\]

所以：

\[
\boxed{
\text{plus branch}
\iff\Omega<0,
}
\]

\[
\boxed{
\text{minus branch}
\iff\Omega>0.
}
\]

flat elimination 等价保证：

\[
\Omega\ne0.
\]

---

## 10.2 Exact decimal quantization

因为 \(\Omega\in\mathbf Z\setminus\{0\}\)：

\[
\boxed{
\left|b_2P_2-\tau_3\right|
\ge10^g.
}
\tag{QSP}
\]

这是真正的 ordinary-integer spacing，且 modulus 是 pure decimal power。

---

## 10.3 Mantissa normal form of \(\Omega\)

已有

\[
\beta_2=\frac{b_2}{10^{m_2}},
\qquad
\varepsilon=\frac{b_1D}{Q_0}.
\]

所以：

\[
\boxed{
\Omega
=Q_0 10^{m_2}(\beta_2-\varepsilon).
}
\tag{OM-1}
\]

代入 exact mantissa balance：

\[
\boxed{
\frac{\Omega}{Q_0}
=
\beta_2x10^d
-\beta_3(1-y).
}
\tag{OM-2}
\]

其中 \(d=m_2-g\)。

这给出一个重要 route verdict：

\[
\boxed{
\Omega\text{ 一般是 }Q_0\text{-scale integer，而不是 }O(1)\text{ defect。}
}
\]

所以此前“\(\beta_2-\varepsilon\ll10^{-g}\) + rational spacing”路线少了一个 \(Q_0\) 因子。

---

## 10.4 FAILED — pure mantissa rational spacing gives absolute \(g\)-bound

minus branch 中：

\[
\Omega>0,
\]

故

\[
\beta_2-\varepsilon
=
\frac{\Omega}{Q_0 10^{m_2}}
\ge
\frac1{Q_0 10^{m_2}}.
\]

而 MB 只给：

\[
\beta_2-\varepsilon<10^{-g}.
\]

合并只得到：

\[
10^{g-m_2}<Q_0.
\]

在 minus \(g\ge1\) 中已有 \(m_2\ge g-1\)，故这几乎是 tautology。

所以：

\[
\boxed{
\text{exact mantissa spacing alone does not produce an absolute }g\text{-bound.}
}
\]

**状态：FAILED AS STANDALONE ROUTE.**

---

# 11. Axis Form of the Master

用

\[
P_2=Q_0-\Theta
\]

代入 (UDD)：

\[
\boxed{
 b_2\Theta
=
 b_1 10^{m_2+g}D
-b_2Q_0(10^g-1)
-\tau_3.
}
\tag{AX-MASTER}
\]

这是 prompt 要求的 exact GSYNC/master axis expansion；没有 Taylor remainder。

它表明 \(\Theta\) 并不是一个独立小参数，而是：

\[
\boxed{
\text{leading word defect}
-
\text{dominant denominator correction}
-
\text{primitive tail integer}
}
\]

的 exact residual。

目前没有任何一项被证明与另外两项 cancellation 到 \(<b_2\) 的程度，所以还不能由 integrality 推出 \(\Theta=O(1)\)。

---

# 12. Backward Tail Quotient Reinterpreted

令

\[
\boxed{d_Q:=\gcd(Q_0,V).}
\]

backward pullback 已有：

\[
\varepsilon^\sharp
=
\frac{b_3(Q_0-P_3)}{10^{n_3}d_Q}
\in\mathbf Z_{>0}.
\]

所以：

\[
\boxed{\tau_3=d_Q\varepsilon^\sharp.}
\]

又

\[
b_3=\beta_3 10^{n_3+g},
\qquad
 y=P_3/Q_0,
\]

所以精确：

\[
\boxed{
\varepsilon^\sharp
=
10^g\frac{Q_0}{d_Q}\beta_3(1-y).
}
\tag{EPS-N}
\]

因此 prompt 中对旧“bounded \(\varepsilon^\sharp\)”预期的修正可以彻底冻结：

\[
\boxed{
\frac{\varepsilon^\sharp}
{10^g(Q_0/d_Q)}
=
\beta_3(1-y).
}
\]

若 \(g\ge1\)，则 \(y<0.1\)，故：

\[
\boxed{
0.09
<
\frac{\varepsilon^\sharp}
{10^g(Q_0/d_Q)}
<1.
}
\tag{EPS-COMPACT}
\]

所以真正 stable 的 backward quotient mantissa 已经找到。

**状态：NEW DERIVED / EXACT.**

---

# 13. Unified Axis–Tail Defect

设

\[
q:=Q_0/d_Q.
\]

由 (UDD)：

\[
10^g\Omega
=b_2(Q_0-\Theta)-d_Q\varepsilon^\sharp.
\]

所以：

\[
\boxed{
 d_Q(b_2q-\varepsilon^\sharp)
=
 b_2\Theta+10^g\Omega.
}
\tag{UAT}
\]

这是本轮 forward/backward 合流后最紧凑的 ordinary integer identity。

左边显含 \(d_Q\)；右边把：

- axis gap \(\Theta\)；
- decimal quantized defect \(\Omega\)；

放在同一个式子中。

从而：

\[
\boxed{
 d_Q\mid b_2\Theta+10^g\Omega.
}
\]

不过这仍是 master 的重写，不是独立 new gate；目前没有足够 size bound 把 RHS 压到 \(<d_Q\)。

**状态：NEW EXACT NORMAL FORM / NOT YET A CLOSURE.**

---

# 14. Small-Shift GCD Triad

令

\[
d_Q=\gcd(Q_0,V),
\]

\[
g_2=\gcd(P_2,V),
\]

\[
\Theta=Q_0-P_2.
\]

## Theorem A1-SSG — Small-Shift GCD

\[
\boxed{
\gcd(d_Q,g_2)\mid\Theta.
}
\tag{SSG1}
\]

### Proof

任何同时整除 \(d_Q\) 与 \(g_2\) 的整数都同时整除 \(Q_0\) 与 \(P_2\)，故整除其差 \(\Theta\)。

又因为 \(d_Q\mid V\)、\(g_2\mid V\)：

\[
\operatorname{lcm}(d_Q,g_2)\mid V.
\]

所以：

\[
\frac{d_Qg_2}{\gcd(d_Q,g_2)}\le V.
\]

由 (SSG1)：

\[
\boxed{
 d_Qg_2\le V\Theta.
}
\tag{SSG2}
\]

再用

\[
b_2=V/g_2
\]

得到更简洁版本：

\[
\boxed{
 d_Q\le b_2\Theta.
}
\tag{SSG3}
\]

或：

\[
\boxed{
 g_2\le\Theta\frac V{d_Q}.
}
\tag{SSG4}
\]

**状态：NEW PROVED.**

---

## 14.1 Prime allocation form

对任意 prime \(p\)：

\[
\boxed{
\min(v_p(d_Q),v_p(g_2))
\le v_p(\Theta).
}
\]

特别若 \(\Theta\le K\)，则所有 \(p>K\) 不可能同时进入 \(d_Q\) 与 \(g_2\)。

所以 bounded-axis-gap 会自动产生一个 strong large-prime support partition。

---

## 14.2 OPEN — closure power

当前只有：

\[
d_Q\le b_2\Theta.
\]

要得到 contradiction，需要另一边例如：

\[
d_Q>b_2\Theta
\]

或至少 \(d_Q/b_2\) 的 uniform lower bound。

现有 backward tail quotient只给 \(d_Q\) 的 divisibility / upper-side information；没有这样的 lower bound。

因此：

\[
\boxed{
\text{Small-shift gcd is a strong conditional amplifier, not yet a global killer.}
}
\]

---

# 15. Quantitative Fixed-Profile Audit

已有 fixed-profile radial bound：

\[
Q_0
<
\frac{
 g_2^2(10^{n_2}-1)^2
+g_3^2(10^{n_3}-1)^2
}{U^2}.
\tag{FPR}
\]

本轮追踪其 moving dependence。

因为：

\[
g_2/U=rac1{\lambda b_2},
\qquad
b_2=\beta_2 10^{m_2},
\]

且

\[
n_2=m_2+g+k,
\]

故：

\[
\frac{g_2 10^{n_2}}U
=
\frac{10^{g+k}}{\lambda\beta_2}.
\]

同理：

\[
\frac{g_3 10^{n_3}}U
=
\frac{10^{-g}}{\lambda\beta_3}.
\]

所以 moving version of (FPR) 至多变成：

\[
Q_0
<
\lambda^{-2}
\left(
\frac{10^{2g+2k}}{\beta_2^2}
+
\frac{10^{-2g}}{\beta_3^2}
\right).
\]

而由 actual block mantissas：

\[
\lambda P_2
=10^{g+k}\frac{\alpha_2}{\beta_2},
\]

\[
\lambda P_3
=10^{-g}\frac{\alpha_3}{\beta_3},
\]

右边本质就是：

\[
\frac{P_2^2}{\alpha_2^2}
+
\frac{P_3^2}{\alpha_3^2},
\]

它在 moving state 中是 \(Q_0^2\)-scale quantity。

因此：

\[
\boxed{
\textbf{fixed-profile finiteness 的显式 bound 已经定量化，}
}
\]

但：

\[
\boxed{
\textbf{直接代入 moving mantissas 后退化成 tautological }Q_0<O(Q_0^2).
}
\]

所以 fixed-profile theorem **不能靠简单 constant tracking 自动升级到 moving closure**。

**状态：NEW QUANTITATIVE NEGATIVE AUDIT.**

---

# 16. Regime Audit

## 16.1 \(\Theta\) bounded

若未来证明：

\[
1\le\Theta\le K,
\]

则立即得到：

1. critical \(k\) additive window；
2. fixed finite set of \(\Theta\)；
3. small-shift support partition；
4. axis equation
   \[
   P_1^2+P_3^2=2\Theta Q_0-\Theta^2;
   \]
5. bounded-source Gaussian factorization；
6. \(g\to\infty\) 时 \(P_3/P_1\to0\) 的 near-square branch。

这是一个极高 leverage reduction。

但它**不是本轮已证明 theorem**。

---

## 16.2 \(\Theta\to\infty\)

由 (AX-M)：

\[
\Theta
=T_\Theta Q_0 10^{-2k}.
\]

所以其 exact scale 已经完全确定到 compact mantissa。

如果 \(k/\log Q_0\to\kappa<1/2\)：

\[
\Theta=Q_0^{1-2\kappa+o(1)}.
\]

这不是一个模糊“可能增长”，而是明确的 axis-gap slope law。

---

## 16.3 \(g\to\infty\)

\[
P_3/P_2\to0.
\]

但若 \(k\) bounded：

\[
P_1/Q_0\asymp10^{-k}
\]

仍是固定正比例，所以 \(\Theta/Q_0\) 可保持常数级。

因此：

\[
\boxed{
g\to\infty\not\Rightarrow\Theta=O(1).}
\]

---

## 16.4 \(g\) bounded

fixed \(g\) 不等于 fixed profile。\(k,d,n_3,V,U,g_i\) 仍可移动。

现有 fixed-profile theorem不能直接使用。

---

## 16.5 \(k\) bounded

现有 geometry 完全允许：

\[
\Theta\asymp Q_0.
\]

没有证明 infinite exact A1 sequence 必须 \(k\to\infty\)。

---

## 16.6 bounded / unbounded \(U\)

本轮没有证明：

\[
U\le U_0\Rightarrow Q_0\le C(U_0).
\]

固定 \(U\) 仍允许 numerator digit lengths 与 primitive \(C_i\) 一起增长。

所以“bounded \(U\) finiteness”保持 OPEN。

同样没有证明任何 infinite sequence 必须 \(U\to\infty\)。

---

# 17. Integer Margin × Master Interaction

本轮最初希望：

\[
\text{master forces ratio near boundary}
+
\text{integer margin}
\Rightarrow\bot.
\]

压力测试结果是否定的。

原因有两层。

## 17.1 Master normal form does not force boundary approach

master 的最小 mantissa relation 是：

\[
\varepsilon
=
\beta_2(1-x10^{-g})
+
\beta_3(1-y)10^{-m_2}.
\]

它控制的是：

\[
\beta_2-\varepsilon
\]

而 common-\(U\) ratio boundary控制的是：

\[
R_\alpha
=
10^{n_3-n_2}\frac{C_2}{C_3}.
\]

当前不存在一条已证明 theorem 把 \(R_\alpha\) 强迫到 \(0.1\) 或 \(10\) 的 \(o(1/C)\) 邻域。

## 17.2 Known synchronized state satisfies margin but dies by location

第 7.4 节的 explicit state已经证明：

- sphere + master；
- real ratio cone；
- 两侧 integer margin；

仍可同时成立，而 interval 整体落在 \((0,1)\)。

所以：

\[
\boxed{
\text{the decisive integer information is not only boundary distance,}
}
\]

而是：

\[
\boxed{
\text{absolute radial location + integer/coprime successor.}
}
\]

---

# 18. Local \(2/5\)-Phase Quantitative Audit

backward pullback 已把 phase depth变成 primitive tail valuation：

\[
R_p^{\rm det}
=
\max\left(
0,
 v_p(Q_0-P_3)-n_3-v_p(g_3)
\right),
\]

在对应 cut-visible chamber 中使用。

partial-\(2\) actual-cut formula仍需保留 parity tax；不能为了对称删掉旧 \(-1\)。

但是在 unified semantics 中：

- phase depth完全由 primitive state决定；
- 它对 \(U\) radial scale homogeneous / blind；
- pure \(5\)-adic norm feedback存在 Hensel-compatible towers；
- \(2\)-adic companion能杀部分 projected local branches，但不 uniform；
- 没有一个 growing moving regime被 local phase 单独全局杀掉。

所以本轮裁决：

\[
\boxed{
\textbf{Backward phase remains a derived branch sieve, not the terminal engine.}
}
\]

---

# 19. Product Modulus Audit

若 \(R_2,R_5>0\)，当然可以把对应 decimal-prime powers放入：

\[
Q_0-P_3.
\]

但 phase exponent 本身就是这个 gap 的 valuation excess。

因此“product modulus \(>Q_0\)”若没有额外 independent lower bound on \(R_p\)，只是把 valuation definition重新写一遍。

当前 forward height bounds没有提供足够的 uniform phase lower bound。

所以：

\[
\boxed{
\text{product-modulus overload is not presently a global moving-profile route.}
}
\]

---

# 20. Pythagorean Axis / Gaussian Fallback Audit

定义 stereographic axis coordinates：

\[
r=\frac{P_1}{Q_0+P_2},
\qquad
s=\frac{P_3}{Q_0+P_2}.
\]

则 exact：

\[
\boxed{
r^2+s^2
=
\frac{Q_0-P_2}{Q_0+P_2}
=
\frac{\Theta}{2Q_0-\Theta}.
}
\]

同时：

\[
P_1^2+P_3^2
=
\Theta(Q_0+P_2).
\]

这是一个很干净的 axis Gaussian factorization入口。

但：

1. rational points在 sphere/conic 上本来就稠密；
2. 没有 common-\(U\) 信息进入上述 parametrization；
3. bounded \(\Theta\) 尚未证明；
4. generic Gaussian support此前已有 pseudo-family反例。

因此本轮没有把 Pythagorean quadruple parametrization升级为主路线。

**裁决：REDUNDANT AS STANDALONE / CONDITIONAL TOOL IF \(\Theta\) BOUNDED.**

---

# 21. Near-Square Branch

如果未来：

\[
\Theta\le K
\]

且 \(g\to\infty\)，则

\[
P_3/P_1\to0,
\]

而：

\[
P_1^2
=
2\Theta Q_0-\Theta^2-P_3^2.
\]

此时 square spacing 才真正重新成为合法工具。

当前却不能跳过 bounded-\(\Theta\) step。

所以：

\[
\boxed{
\text{square spacing is a post-criticality tool, not a current global tool.}
}
\]

---

# 22. Computation / Falsification

本轮 computation 只做 proof-audit 与 conjecture falsification。

保存脚本：

`strict_layer_A1_unified_terminal_checks.py`

它检查：

1. Integer Radial Margin 在小范围 exhaustive grid 上无反例；
2. equality samples只出现在 \(U=1\)；
3. explicit synchronized real-cone point满足 margin，但 \(R<1\)；
4. previous synchronized polynomial pseudo-family 的 \(\Theta/Q_0\) 趋近 \(0.7053446\)，显示 master-only axis gap可线性增长。

没有任何 nonexistence theorem 依赖有限搜索。

---

# 23. Route Scoreboard

| Route | Strongest result | Missing step | Verdict |
|---|---|---|---|
| Axis gap / critical \(k\) | exact compact \(T_\Theta\), improved \(k\)-upper | lower critical bound on \(k\) | **OPEN / high leverage** |
| Integer radial margin | sharp one-lattice-step theorem | radial location + coprime successor | **NEW PROVED but insufficient** |
| Small-shift gcd | \(d_Q\le b_2\Theta\) | lower bound on \(d_Q/b_2\) | **OPEN / conditional** |
| Mantissa spacing | exact integer \(\Omega\) | \(\Omega\) not forced \(O(1)\) | **FAILED standalone** |
| Unified \(\Omega\)-defect | \(b_2P_2-\tau_3=10^g\Omega\) | overload against radial successor | **NEW PROVED / strongest normal form** |
| Fixed-profile upgrade | explicit bound recovered | moving substitution becomes tautological | **FAILED direct upgrade** |
| Local \(2/5\) phase | real branch sieve | radial blindness / Hensel survivors | **derived toolkit only** |
| Pythagorean/Gaussian | exact axis factorization | no common-U input | **conditional fallback** |
| Coprime density | exact count/successor | U=1 and non-radical-rich V survive | **not global killer** |

---

# 24. Strongest New Theorems of This Campaign

## A1-U1 — Unified Interface Equivalence

Original A1 candidate iff exact synchronized primitive state + legal reduced common radial scale.

**FROZEN / RECONSTRUCTED.**

## A1-U2 — Exponent Normal Form

\[
(m_2,n_2,m_3)
=(g+d,2g+k+d,n_3+g).
\]

**NEW DERIVED.**

## A1-U3 — Axis Mantissa Quantization

\[
T_\Theta
=10^{2k}\Theta/Q_0
=
\frac{r_1^2+10^{-4g}r_3^2}{1+x}.
\]

For \(g\ge1\)：

\[
1/2<T_\Theta<2.532.
\]

**NEW PROVED.**

## A1-U4 — Sharp Integer Radial Margin

\[
10^{n_3}C_2-10^{n_2-1}C_3\ge C_2,
\]

\[
10^{n_2}C_3-10^{n_3-1}C_2\ge C_3.
\]

**NEW PROVED / SHARP.**

## A1-U5 — Unified Decimal Defect

\[
\Omega=b_2Q_0-b_1 10^{m_2}D\ne0,
\]

\[
\tau_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbf Z_{>0},
\]

\[
\boxed{b_2P_2-\tau_3=10^g\Omega.}
\]

**NEW PROVED.**

## A1-U6 — Backward Tail Natural Normalization

\[
\frac{\varepsilon^\sharp}{10^g(Q_0/d_Q)}
=\beta_3(1-y).
\]

**NEW DERIVED / EXACT.**

## A1-U7 — Small-Shift GCD

\[
\gcd(d_Q,g_2)\mid\Theta,
\qquad
 d_Qg_2\le V\Theta,
\qquad
 d_Q\le b_2\Theta.
\]

**NEW PROVED.**

---

# 25. Killed / Downgraded Conjectures

## DISPROVED / FAILED

1. master / GSYNC alone should force bounded \(\Theta\)；
2. integer radial margin alone should kill synchronized conic points；
3. moving fixed-profile theorem should close after simple constant tracking；
4. exact \(\varepsilon\) vs \(\beta_2\) rational spacing alone should bound \(g\)；
5. generic product modulus from \(R_2,R_5\) should overload \(Q_0-P_3\) without an independent phase-depth lower bound；
6. compact limit master alone should force a contradiction；
7. bare Pythagorean axis parametrization supplies the missing radial arithmetic。

## STILL OPEN

1. common-\(U\) forces critical lower \(k\)；
2. bounded \(\Theta\)；
3. transition-strip \(d\in\{-1,0,1\}\) exact overload；
4. a useful lower bound on \(d_Q/b_2\)；
5. global coprime successor exclusion；
6. full A1 closure。

---

# 26. Answers to Q1–Q12

## Q1 — A1 moving escape 的真正最小 coordinates 是什么？

### Exact semantic answer

\[
\boxed{
(P_1,P_2,P_3,Q_0;U,V),
\quad\gcd(U,V)=1,
}
\]

with sphere + recovered exact master/digit A1 predicate。

### Analytic moving answer

\[
\boxed{
(g,k,d;n_3)
+
(\varepsilon,\beta_2,\beta_3,r_3)
+
Q_0
}
\]

plus \(V,d_Q\) when gcd/coprime arithmetic is used。

---

## Q2 — 是否可以证明 \(Q_0-P_2\) uniformly bounded？

\[
\boxed{\textbf{NO — not with the current theorem set.}}
\]

现有 exact relation only gives：

\[
\Theta=T_\Theta Q_0 10^{-2k},
\]

with compact \(T_\Theta\)。

---

## Q3 — 若不能，它的 exact asymptotic scale是什么？

对 \(g\ge1\)：

\[
\boxed{
\frac12
<
10^{2k}\frac{\Theta}{Q_0}
<2.532.
}
\]

因此：

\[
\boxed{
\Theta\asymp Q_0 10^{-2k}.
}
\]

若 \(k/\log_{10}Q_0\to\kappa\)：

\[
\boxed{
\log\Theta/\log Q_0=1-2\kappa+o(1).
}
\]

---

## Q4 — common integer \(U\) 相比 continuous scale 增加了哪条最强 uniform inequality？

最干净的是 active upper endpoint lattice step：

\[
\boxed{R-L\ge1/C_j.}
\]

其 two-sided ratio projection 是：

\[
\boxed{
10^{n_3}C_2-10^{n_2-1}C_3\ge C_2,
}
\]

\[
\boxed{
10^{n_2}C_3-10^{n_3-1}C_2\ge C_3.
}
\]

但真正 exact integer gate仍是：

\[
\boxed{\lceil L\rceil<R}
\]

以及 coprime successor版本。

---

## Q5 — 能否建立 sharp Integer Radial Margin Theorem？

\[
\boxed{\textbf{YES.}}
\]

第 7 节已经证明，且 equality只可能出现在 \(U=1\) 的 endpoint-extreme configuration。

---

## Q6 — margin 能否与 GSYNC/master ratio defect直接冲突？

\[
\boxed{\textbf{NOT UNIFORMLY.}}
\]

已有 synchronized real-cone point同时满足两侧 margin，却因整个 interval 在 \((0,1)\) 而死亡。

所以 margin必须与 radial location / successor而非 master alone 联用。

---

## Q7 — small-shift gcd 是否有实质 closure power？

有结构力：

\[
\boxed{
\gcd(d_Q,g_2)\mid\Theta,
\qquad
 d_Q\le b_2\Theta.
}
\]

若 \(\Theta\) bounded，会强制 large-prime support partition。

但当前：

\[
\boxed{\textbf{no global closure yet}}
\]

因为缺少 \(d_Q/b_2\) 的 independent lower bound。

---

## Q8 — fixed-profile finiteness 能否定量化并升级到 moving profiles？

定量化：

\[
\boxed{\textbf{YES.}}
\]

直接 uniform upgrade：

\[
\boxed{\textbf{NO.}}
\]

把 bound 写成 moving mantissa 后退化为 \(Q_0<O(Q_0^2)\)-type inequality。

因此必须加入新的 moving correlation，而不是只追 constants。

---

## Q9 — backward-derived phase 工具是否真正杀掉任何 global moving regime？

\[
\boxed{\textbf{NO global regime so far.}}
\]

它们能杀具体 projected local branches，也能提供精确 tail valuation，但在 terminal forward state 后属于 derived toolkit，对 radial \(U\) homogeneous。

---

## Q10 — 是否所有 infinite escapes 都被压成 \(g,k,U\to\infty\)？

\[
\boxed{\textbf{NO — this has not been proved.}}
\]

当前甚至不能排除：

- bounded \(k\) + growing \(g\)；
- bounded \(g\) + moving gcd/digit profile；
- bounded \(U\) + growing primitive/digit state。

真正已证明的是 fixed full profile 不能无限逃逸。

---

## Q11 — 最终能否证明 \(A_1=\varnothing\)？

\[
\boxed{\textbf{NOT IN THIS CAMPAIGN.}}
\]

没有发现合法 Level-5 survivor，也没有发现 forward reconstruction bug；但也没有获得 uniform radial exclusion。

---

## Q12 — 如果不能，当前剩余最小 theorem是什么？

最精确的 terminal statement 可以写成：

### A1-TRX — Terminal Coprime-Radial Exclusion in Quantized-Defect Normal Form

对任意 positive primitive integer sphere state与 canonical denominator profile，若：

1. A1 exponent normal form
   \[
   m_2=g+d,
   \quad
   n_2=2g+k+d,
   \quad
   m_3=n_3+g;
   \]
2. \(D=P_1 10^k-Q_0>0\)；
3. \(\Omega\ne0\) 与 \(\tau_3\in\mathbf Z_{>0}\) 满足
   \[
   b_2P_2-\tau_3=10^g\Omega;
   \]
4. \(V=\operatorname{lcm}(b_1,b_2,b_3)\)，\(g_i=V/b_i=\gcd(V,P_i)\)，\(C_i=P_i/g_i\)；
5. denominator digits合法；

则定义

\[
I_{23}
=
\left[\frac{10^{n_2-1}}{C_2},\frac{10^{n_2}}{C_2}\right)
\cap
\left[\frac{10^{n_3-1}}{C_3},\frac{10^{n_3}}{C_3}\right).
\]

需要证明：

\[
\boxed{
\operatorname{next}_V(L)\ge R,
}
\]

即

\[
\boxed{N_V(I_{23})=0.}
\]

这是当前真正没有被派生 toolkit 代替的 single terminal theorem。

作为最高 leverage intermediate theorem，则是：

### A1-CRIT — Critical Radial Coupling

存在 absolute constant \(C\)，使任何满足上述 1–5 且 integer common-\(U\) feasible 的 state 均满足

\[
\boxed{
 k\ge\frac12\log_{10}Q_0-C.
}
\]

由 (AX-M) 它等价于：

\[
\boxed{\Theta=O(1).}
\]

本轮没有证明 A1-CRIT。

---

# 27. Fate of the Independent Backward Line

最终裁决：

\[
\boxed{
\textbf{ONLY AS DERIVED TOOLKIT.}
}
\]

理由不是 backward “没用”，而是：

1. common-\(U\) pullback后 raw WGF 对 \(U\) homogeneous；
2. full terminal forward state已经重建 original candidate；
3. phase / Gaussian / norm / determinant 都是 primitive master consequences；
4. pure \(5\)-adic loop存在 Hensel-compatible survivors；
5. \(2\)-adic companion不是 uniform radial killer；
6. 当前唯一 genuinely missing semantics 是 ordinary coprime integer radial realization。

因此不再建议维护独立 “Backward A1 program”。

应当把它作为：

\[
\boxed{
\text{tail valuation / branch sieve / divisibility toolkit}
}
\]

嵌入 unified terminal campaign。

---

# 28. PROVED / DISPROVED / OPEN Ledger

## FROZEN

- DD closed；
- Strict frontier = A1-only；
- flat locus empty；
- primitive sphere；
- exact GSYNC/master；
- common-\(U\) reconstruction theorem；
- fixed-profile radial termination；
- backward radial redundancy；
- local phase toolkit。

## NEW PROVED

1. full interface equivalence proof restated in minimal witness form；
2. exponent normal form \((g,k,d,n_3)\)；
3. only two active interval endpoint configurations；
4. sharp Integer Radial Margin；
5. margin equality \(\Rightarrow U=1\)；
6. exact axis mantissa identity (AX-M)；
7. improved \(10^{2k}<2.532Q_0\) for \(g\ge1\)；
8. Unified Decimal Defect (UDD)；
9. quantized spacing \(|b_2P_2-\tau_3|\ge10^g\)；
10. exact axis master (AX-MASTER)；
11. natural normalization of \(\varepsilon^\sharp\)；
12. unified axis-tail identity (UAT)；
13. small-shift gcd theorem；
14. fixed-profile quantitative non-upgrade audit。

## NEW DISPROVED / FAILED

1. integer margin alone closes synchronized conics；
2. master alone bounds \(\Theta\)；
3. pure rational spacing \(\varepsilon\) vs \(\beta_2\) gives absolute \(g\)；
4. direct fixed-profile constant tracking upgrades to moving profiles；
5. generic product phase modulus is terminal；
6. standalone Pythagorean axis parametrization supplies the missing radial gate。

## OPEN

1. A1-CRIT critical lower \(k\)；
2. bounded \(\Theta\)；
3. transition-strip \(d=-1,0,1\) overload；
4. useful lower bound on \(d_Q/b_2\)；
5. terminal coprime successor exclusion A1-TRX；
6. \(A_1=\varnothing\)；
7. Strict Layer closure。

---

# 29. Source / Provenance Audit

本轮没有调用任何外部 theorem 作为 A1 closure dependency；所有冻结输入均来自当前 Strict-Layer / A1 报告链，新增结论均在本文件中重新代数推导。

主要 provenance：

1. `strict_layer_A1_moving_profile_coprime_integer_scale_campaign.md`
   - exact leading-block sandwich；
   - \(\varepsilon\in(0,1)\)；
   - \(P_2\)-axis theorem；
   - \(\Theta\asymp Q_0 10^{-2k}\) 的旧粗 bound；
   - exact mantissa balance；
   - \(d=m_2-g\) sign classification；
   - tropical two-slope region。

2. `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`
   - common-\(U\) interval semantics；
   - fixed-profile radial termination；
   - exact coprime count；
   - full forward reconstruction theorem；
   - synchronized real-cone regression point used to falsify margin-only closure。

3. `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`
   - exact GSYNC；
   - primitive ratio window；
   - plus/minus defect language；
   - explicit infinite synchronized polynomial pseudo-family used to prove master-only \(\Theta\)-boundedness false。

4. `strict_layer_A1_flat_locus_structural_elimination_campaign.md`
   - flat locus empty；
   - \(D=P_1 10^k-Q_0>0\) and \(\Delta_{12}\ne0\) provenance。

5. `strict_layer_backward_A1_common_U_pullback_primitive_radial_gluing_campaign.md`
   - \(\Pi=UH\)、\(\mathbf A=U\mathbf A^\sharp\)、\(N=U^2N^\sharp\)、\(\Delta=U\delta\)；
   - backward-on-forward redundancy；
   - \(\varepsilon^\sharp\) 与 primitive tail factorization。

6. `strict_layer_backward_A1_2x5_decimal_synchronization_campaign.md`
   - general \(2\)-phase master / phase-to-cut；
   - partial-\(2\) parity tax；
   - CRT branch sieve limitations。

7. `strict_layer_backward_A1_5phase_cut_synchronization_campaign.md`
   - \(5\)-phase-to-cut theorem；
   - actual cut penetration bounds。

8. `strict_layer_backward_A1_same_cut_norm_excess_campaign.md`
   - pure \(5\)-adic same-cut feedback has Hensel-compatible survivors；
   - strict-cut shielding。

9. `strict_layer_backward_A1_word_recovery_architecture_campaign.md`
   - actual cut as irreducible semantic source before terminal merge；
   - detached-prefix / Gaussian anti-overclaim examples。

10. `strict_layer_DD_oriented_tail_window_campaign.md`
    - \(DD=\varnothing\) frozen Strict-Layer input。

本轮新增的 A1-U3 / U4 / U5 / U6 / U7 均只使用上述 frozen exact identities 加 elementary integer arithmetic；不依赖旧 External Exact-Lift closure claim。

---

# 30. At Most Three Next-Round Targets

## Target 1 — Quantized Defect × Coprime Successor

直接从：

\[
\boxed{b_2P_2-\tau_3=10^g\Omega}
\]

和：

\[
\boxed{\operatorname{next}_V(L)<R}
\]

出发，寻找一个 genuine modulus-vs-radial-location theorem。

不要重新回到 generic conic / prime audit。

**优先级：最高。**

---

## Target 2 — Critical Radial Coupling

攻击：

\[
\boxed{
U\in I_{23},\ \gcd(U,V)=1
\Longrightarrow
k\ge\frac12\log_{10}Q_0-C.
}
\]

即 bounded \(\Theta\)。

若成功，立即进入 finite-\(\Theta\) + small-shift gcd + axis Gaussian / square-spacing。

**优先级：高。**

---

## Target 3 — Transition Strip \(d\in\{-1,0,1\}\)

在此 strip 中 \(b_2P_2\) 与 \(\tau_3\) 同尺度，\(\Omega\) 是真正 cancellation quotient。

保留完整：

\[
\Omega/Q_0
=
\beta_2x10^d-\beta_3(1-y),
\]

\[
 d_Q(b_2q-\varepsilon^\sharp)
=b_2\Theta+10^g\Omega,
\]

再加入 radial successor / endpoint lattice。

这里最可能出现：

\[
0<|\Omega|<M,
\qquad M\mid\Omega
\]

型 overload。

**优先级：第三。**

---

# 31. Final Verdict

本轮没有达到：

\[
A_1=\varnothing.
\]

但 forward/backward 的组织方式已经可以正式结束：

\[
\boxed{
\text{Forward A1}
\quad\text{vs}\quad
\text{Backward A1}
}
\]

不再是正确的研究分割。

新的 unified terminal object 是：

\[
\boxed{
\text{primitive sphere}
+
\text{quantized decimal defect }\Omega
+
\text{common coprime radial successor}
}
\]

其中：

\[
\boxed{
\Theta
=
T_\Theta Q_0 10^{-2k}
}
\]

已经被精确量化；

\[
\boxed{
 b_2P_2-\tau_3=10^g\Omega
}
\]

已经把 master 与 backward tail 合成一个 ordinary integer equation；

而真正仍未跨越的障碍只剩：

\[
\boxed{
\textbf{为什么这个 quantized primitive state 永远无法让}
\operatorname{next}_V(L)<R.
}
\]

因此本轮最终等级最准确地写为：

\[
\boxed{
\textbf{LEVEL 3 ACHIEVED — SHARP INTEGER RADIAL MARGIN}
}
\]

\[
\boxed{
+
\textbf{NEW UNIFIED DECIMAL DEFECT NORMAL FORM}
+
\textbf{AXIS-GAP SCALE QUANTIZATION}
}
\]

并完成：

\[
\boxed{
\textbf{Backward A1 independent program }\to\textbf{ derived toolkit only.}
}
\]

A1 与 Strict Layer 均仍 **OPEN**。
