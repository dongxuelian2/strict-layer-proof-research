# 三项十进制拼接平方和问题：Backward Strict Layer — A1 Same-Cut Norm-Excess Feedback Campaign

**文件名：** `strict_layer_backward_A1_same_cut_norm_excess_campaign.md`  
**日期：** 2026-08-16  
**研究范围：** Strict Layer，仅研究 \(A_1\)-only 的 backward exact recovery；本轮集中于 partial \(5\)-saturation 中
\[
\boxed{\text{Same Actual Cut}\times\text{Norm Excess}\times\text{Residual }5\text{-Phase}}.
\]

**最终状态：**

\[
\boxed{\textbf{A1 PARTIAL-5 NOT CLOSED}}
\]

但本轮得到的不是“又一个局部 congruence”，而是对当前 partial-\(5\) 机制的一次实质性判型：

1. 完整算清了 \(\nu=v_5(N)\) 的 valuation tree 与全部 denominator support pattern；
2. 找到了真正的 norm resonance phase，并将其 canonical 地写成 ratio Hensel branch；
3. 将 norm phase 与 word phase 合成了同一个 actual cut 上的一元 \(5\)-adic fixed-point congruence；
4. 证明该 fixed point 在真正 resonance chambers 中是 **transverse** 的，且 strict decimal cut 对 norm-leading-error 存在一个不可跨越的 **shielding margin**；
5. 因而系统性否定了“norm-excess self-amplification”作为当前机制的 closure route；
6. 更强地，构造了一个 **unequal denominator support 的完整 raw A1-WR \(\mathbf Z_5\)-Hensel tower**，证明纯 \(5\)-adic same-cut algebra 本身并不会强迫 \(r_1=r_2\)；
7. 因此 partial-\(5\) 的下一条真正独立 relation 已被压缩为：**同一个 word determinant 的 \(2\)-adic companion phase**，而不是继续堆叠新的 \(5\)-adic valuation lemma。

本轮最重要的新结构可以压成：

\[
\boxed{
\text{high norm resonance}
\Longrightarrow
\text{two Hensel ratio branches}
\Longrightarrow
\text{one-variable same-cut fixed point}
}
\]

但紧接着：

\[
\boxed{
R_5< n+\lambda_N
}
\]

在真正 resonance chambers 中被 strict cut 自动强迫，所以 word phase 永远读不到决定 \(\lambda_N\) 的下一位 Hensel error。换言之，当前 loop **闭合了，但不是以 contradiction 闭合，而是以 transverse compatibility 闭合**。

---

# 1. Executive summary

## 1.1 FROZEN — phase-to-cut theorem

沿上一轮记号：

\[
P=a_1 10^n+a_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
G=b_1b_2,
\qquad
\nu=v_5(N),
\qquad
\gamma=v_5(G),
\]

partial \(5\)-saturation：

\[
0<s:=v_5(b_3)<n_3.
\]

上一轮已经严格建立：

\[
\Delta:=b_3P-a_3D,
\qquad
v_5(\Delta)=e,
\]

\[
\boxed{e=\nu+3s-2\gamma-n_3},
\]

以及 cut-visible depth

\[
\boxed{
R:=R_5^{\rm cut}
=
\max\{0,\nu+2s-2\gamma-n_3\}.
}
\]

当 \(R>0\) 时：

\[
\boxed{
P\equiv
C_5
:=
a_3\frac D{5^s}
\left(\frac{b_3}{5^s}\right)^{-1}
\pmod{5^R}.
}
\]

本轮不重证 phase-to-cut transfer；只在使用时重新审计其 valuation domain。

## 1.2 NEW PROVED — exact norm valuation tree

令

\[
r_i=v_5(b_i),
\qquad
\alpha_i=v_5(a_i),
\]

\[
x=\alpha_1+r_2,
\qquad
y=\alpha_2+r_1.
\]

则：

- \(x<y\Rightarrow \nu=2x\)；
- \(y<x\Rightarrow \nu=2y\)；
- \(x=y=t\Rightarrow\nu=2t+\lambda_N\)，其中
  \[
  \lambda_N=v_5(X_0^2+Y_0^2),
  \quad
  X=5^tX_0,
  \quad
  Y=5^tY_0.
  \]

因此真正不可控的额外 norm depth 确实只出现在 equal-support resonance；但在 no-denominator-support chamber 中，base support \(t\) 本身仍来自 numerator，所以不能把整个 \(\nu\) 说成仅由 \(\lambda_N\) 决定。

## 1.3 NEW PROVED — unequal denominator supports 并不自动消失

若 \(r_1\ne r_2\)，包括 one-sided support，则 reducedness 直接给出统一公式

\[
\boxed{
\nu=2\min(r_1,r_2),
\qquad
R=2s-n_3-2\max(r_1,r_2).
}
\]

因此

\[
\boxed{
R>0
\Longrightarrow
2s>n_3+2\max(r_1,r_2),
}
\]

但这 **不推出** \(r_1=r_2\)。

更强地，本轮给出一个 Pattern II trace，在完整 raw A1-WR 的 \(\mathbf Z_5\)-completion 中存在 simple Hensel root，且保持

\[
r_1=0,
\qquad r_2=1,
\qquad R=1.
\]

所以 Candidate A

\[
R>0\Longrightarrow r_1=r_2
\]

至少不能由当前纯 \(5\)-adic same-cut / raw-WGF algebra 推出。

## 1.4 NEW PROVED — norm resonance phase

固定 canonical \(\iota\in\mathbf Z_5\) 满足

\[
\iota^2=-1,
\qquad
\iota\equiv2\pmod5.
\]

若 \(X_0,Y_0\) 为 \(5\)-adic units 且 \(\lambda_N\ge1\)，则唯一存在

\[
\sigma\in\{\pm1\}
\]

使

\[
\boxed{
\lambda_N
=
v_5(X_0-\sigma\iota Y_0),
}
\]

而另一 factor 为 unit。

因此 norm excess 自带一个 canonical sign phase。

## 1.5 NEW PROVED — same-cut fixed-point equation

在 equal denominator support \(r_1=r_2=r>0\) 中：

\[
\frac{a_1}{a_2}
\equiv
K_\sigma
:=
\sigma\iota\frac{\beta_1}{\beta_2}
\pmod{5^{\lambda_N}},
\]

其中

\[
b_i=5^r\beta_i,
\qquad 5\nmid\beta_1\beta_2.
\]

写成 exact Hensel error：

\[
a_1=K_\sigma a_2+5^{\lambda_N}z,
\qquad z\in\mathbf Z_5^\times.
\]

代入 actual cut：

\[
P
=
(1+10^nK_\sigma)a_2
+
10^n5^{\lambda_N}z.
\]

如果

\[
R<n+\lambda_N,
\]

则最后一项在 phase modulus 内不可见，所以

\[
\boxed{
P\equiv C_5\pmod{5^R}
\iff
(1+10^nK_\sigma)a_2\equiv C_5\pmod{5^R}.
}
\]

而

\[
1+10^nK_\sigma\equiv1\pmod5
\]

是 unit，所以每个 sign branch 对 \(a_2\) 都只有唯一 Hensel residue，而不是 contradiction。

## 1.6 NEW PROVED — Strict-Cut Shielding

本轮最关键的正结果是：在真正的两个 resonance chamber 中，恰好总有

\[
\boxed{R<n+\lambda_N.}
\]

而且存在显式 margin。

### Equal denominator support \(r_1=r_2=r>0\)

若 \(R>0\)，则 prefix valuation lock 强迫

\[
v_5(D)=s.
\]

又该 chamber 中

\[
v_5(Q)=r,
\]

故

\[
\boxed{s=g+r.}
\]

同时

\[
R=\lambda_N+2g-n_3.
\]

于是

\[
\boxed{
(n+\lambda_N)-R
=m_2+k_{12}+n_3-g
\ge4.
}
\]

### No denominator support + numerator resonance

若

\[
r_1=r_2=0,
\qquad
\alpha_1=\alpha_2=t,
\]

则

\[
p:=v_5(P)=t.
\]

在真正能读到 normalized prefix unit 的 subchamber \(R>t\) 中，prefix lock 强迫

\[
\boxed{g=s+t.}
\]

除去共同 \(5^t\) 后的 phase depth为

\[
R_0=R-t.
\]

此时

\[
\boxed{
(n+\lambda_N)-R_0
=m_2+k_{12}+n_3-s
\ge3.
}
\]

因此 word phase 仍然读不到决定 exact \(\lambda_N\) 的 Hensel error。

这直接否定了本轮最诱人的 self-amplification 猜想：

\[
\lambda_N\ge k
\Longrightarrow
\lambda_N\ge k+1
\]

不会由当前 same-cut phase mechanism 自动产生。

## 1.7 NEW PROVED — 真正的“双 phase synchronization”是 leading-unit 同步，不是 valuation ascent

完整 raw WGF 的 unit part 给出：

\[
\boxed{
\widehat N\,\widehat{\mathbf B}^{\,2}\widehat b_3^{\,2}
=
\widehat G^{\,2}
2^{n_3}
\widehat\Delta\,
\widehat C_+,
}
\]

其中

\[
C_+:=b_3\mathbf A+a_3\mathbf B,
\]

所有带帽量均为 \(5\)-adic units。

在 resonance branch 中，若

\[
X_0-\sigma\iota Y_0=5^{\lambda_N}z_N,
\]

则

\[
\widehat N
=z_N(X_0+\sigma\iota Y_0).
\]

另一方面

\[
\widehat\Delta=\Delta/5^e
\]

是 word-phase 的 leading unit。

于是 raw WGF 给出 exact multiplicative unit balance

\[
\boxed{
\widehat\Delta=U_5\,z_N,
\qquad U_5\in\mathbf Z_5^\times.
}
\]

这里 \(U_5\) 是由同一个完整 state 的其余 unit parts 显式组成的 unit；**一般不能把它误当成只由 denominator trace 预先决定的外部 target**。因此这条式子的严格含义是：两个 phase 的 leading nonzero units 被同一 exact WGF 约束，但它本身不会自动再制造一位 \(5\)-divisibility。

## 1.8 Final verdict

所以本轮并未关闭

\[
0<v_5(b_3)<n_3.
\]

更准确地说：

\[
\boxed{
\textbf{当前纯 }5\textbf{-adic same-cut loop 已经被研究到“局部闭合但可相容”的程度。}
}
\]

真正缺少的单一独立 relation 不再是另一个 \(5\)-adic norm lemma，而是同一个 determinant

\[
\Delta=b_3P-a_3D
\]

上的 companion decimal-prime phase，例如：

\[
\boxed{
P\equiv C_2(T,a_3)
\pmod{2^{R_2}}
}
\]

与现有

\[
P\equiv C_5(T,a_3)
\pmod{5^{R_5}}
\]

同步，从而真正通过 CRT 读取同一 actual decimal suffix。

---

# 2. Frozen phase-to-cut theorem

本轮沿用：

\[
S=10^{n_3},
\qquad
D=10^gQ,
\qquad
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\]

\[
n=m_2+g+k_{12},
\qquad
k_{12}\ge1,
\]

\[
\mathbf A=SP+a_3,
\qquad
P=a_1 10^n+a_2,
\]

\[
\mathbf B=SD+b_3.
\]

partial \(5\)-saturation：

\[
0<s=v_5(b_3)<n_3,
\qquad
5\nmid a_3.
\]

上一轮已证明：

\[
\Delta=b_3P-a_3D,
\]

\[
\boxed{v_5(\Delta)=e=\nu+3s-2\gamma-n_3.}
\]

若 \(R=e-s>0\)，则

\[
\boxed{
R=\nu+2s-2\gamma-n_3,
}
\]

并有

\[
\boxed{
P\equiv C_5\pmod{5^R}.
}
\]

所有本轮结论都在此 frozen theorem 之上推进。

---

# 3. Exact scope / anti-duplication

本轮只研究 fixed-candidate / fixed-trace 的局部 arithmetic self-consistency。

明确不使用正向线的：

- \(Q_0\to\infty\)；
- primitive moving-core termination；
- generic primitive-defect height bound；
- square-spacing；
- large-height projective compactness；
- asymptotic decimal translation。

最新正向报告已经关闭 primitive coefficient flat locus，并把 forward frontier 压到 generic primitive-defect synchronization；该结果在本轮只作为 anti-duplication boundary，不进入任何新 backward theorem 的证明。

---

# 4. Norm valuation tree

定义

\[
X=a_1b_2,
\qquad
Y=a_2b_1,
\qquad
N=X^2+Y^2.
\]

记

\[
x=v_5(X)=\alpha_1+r_2,
\qquad
y=v_5(Y)=\alpha_2+r_1.
\]

## Theorem NVT — Exact Norm-Valuation Tree

### Case A: \(x<y\)

写

\[
X=5^xX_0,
\qquad
Y=5^yY_0,
\qquad
5\nmid X_0Y_0.
\]

则

\[
N
=5^{2x}
\left(
X_0^2+5^{2(y-x)}Y_0^2
\right).
\]

括号模 \(5\) 等于 \(X_0^2\ne0\)，故

\[
\boxed{\nu=2x.}
\]

### Case B: \(y<x\)

同理：

\[
\boxed{\nu=2y.}
\]

### Case C: \(x=y=t\)

写

\[
X=5^tX_0,
\qquad
Y=5^tY_0,
\qquad
5\nmid X_0Y_0.
\]

则

\[
N=5^{2t}(X_0^2+Y_0^2).
\]

定义

\[
\boxed{
\lambda_N:=v_5(X_0^2+Y_0^2).
}
\]

于是

\[
\boxed{\nu=2t+\lambda_N.}
\]

**状态：NEW PROVED.**

---

# 5. Denominator \(5\)-support compression

先补一个本轮反复需要的 denominator-prefix valuation。令

\[
q:=v_5(Q),
\qquad
Q=b_1 10^{m_2}+b_2.
\]

写

\[
b_1=5^{r_1}\beta_1,
\qquad
b_2=5^{r_2}\beta_2,
\qquad
5\nmid\beta_1\beta_2.
\]

则

\[
Q
=5^{r_1+m_2}2^{m_2}\beta_1
+5^{r_2}\beta_2.
\]

因此得到 exact denominator-prefix valuation tree：

\[
\boxed{
q=
\begin{cases}
\min(r_1+m_2,r_2),&r_1+m_2\ne r_2,\\
r_2+\lambda_Q,&r_1+m_2=r_2,
\end{cases}
}
\]

其中 resonance 时

\[
\boxed{
\lambda_Q
:=v_5(2^{m_2}\beta_1+\beta_2).
}
\]

这说明 prefix denominator 自己也只有一个真正的 \(5\)-adic cancellation chamber：

\[
\boxed{r_2=r_1+m_2.}
\]

特别在 equal support \(r_1=r_2=r>0\) 中，因为 \(m_2\ge1\)，绝不处于该 resonance，且

\[
\boxed{q=r.}
\]

**状态：NEW PROVED — Prefix Denominator Valuation Tree.**

逐块 reducedness 给：

\[
r_1>0\Rightarrow\alpha_1=0,
\qquad
r_2>0\Rightarrow\alpha_2=0.
\]

## Pattern I — \(r_1>0,r_2=0\)

\[
x=0,
\qquad
y=\alpha_2+r_1>0.
\]

故

\[
\boxed{\nu=0.}
\]

\[
\boxed{
R=2s-2r_1-n_3.
}
\]

并且

\[
Q=b_1 10^{m_2}+b_2\equiv b_2\not\equiv0\pmod5,
\]

所以

\[
\boxed{v_5(Q)=0,\qquad v_5(D)=g.}
\]

## Pattern II — \(r_1=0,r_2>0\)

\[
y=0,
\qquad x=\alpha_1+r_2>0.
\]

故

\[
\boxed{\nu=0,}
\qquad
\boxed{R=2s-2r_2-n_3.}
\]

且 \(a_2\) 为 unit，因此

\[
\boxed{v_5(P)=0.}
\]

若 \(R>0\)，后文 Prefix-Valuation Trichotomy 将强迫

\[
\boxed{v_5(D)=s.}
\]

## Pattern III — \(r_1,r_2>0,\ r_1\ne r_2\)

\[
\alpha_1=\alpha_2=0,
\]

\[
x=r_2,
\qquad y=r_1.
\]

故

\[
\boxed{\nu=2\min(r_1,r_2).}
\]

\[
\boxed{
R
=2s-n_3-2\max(r_1,r_2).
}
\]

又 \(P\) 为 unit，所以 \(R>0\Rightarrow v_5(D)=s\)。

## Unified unequal-support formula

Patterns I–III 可统一写成：

\[
\boxed{
 r_1\ne r_2
\Longrightarrow
\nu=2\min(r_1,r_2),
}
\]

\[
\boxed{
R=2s-n_3-2\max(r_1,r_2).
}
\]

因此真正能推出的 compression 是：

\[
\boxed{
R>0
\Longrightarrow
2s>n_3+2\max(r_1,r_2).
}
\]

而不是 \(r_1=r_2\)。

## Pattern IV — \(r_1=r_2=r>0\)

\[
x=y=r,
\]

\[
\boxed{
u=2r+\lambda_N.}
\]

\[
\boxed{
R=\lambda_N+2s-2r-n_3.
}
\]

这是 denominator-driven resonance chamber。

## Pattern V — \(r_1=r_2=0\)

\[
\gamma=0,
\qquad
x=\alpha_1,
\qquad
y=\alpha_2.
\]

全部额外 norm depth 来自 numerator。

**状态：NEW PROVED classification.**

---

# 6. Unequal-support elimination attempt

Theorem Candidate A 希望证明：

\[
R>0\Longrightarrow r_1=r_2.
\]

本轮结论是：

\[
\boxed{\textbf{FAILED AS A PURE }5\textbf{-ADIC / VALUATION COMPRESSION.}}
\]

原因分两层。

第一层，exact formula 已经表明 \(r_1\ne r_2\) 与 \(R>0\) 在 valuation algebra 上完全兼容，只需

\[
2s>n_3+2\max(r_1,r_2).
\]

第二层，第 25 节将给出一个 Pattern II trace，使完整 raw A1-WR 在 \(\mathbf Z_5\) 中具有 simple Hensel branch，同时保持

\[
r_1=0,
\quad r_2=1,
\quad R=1.
\]

因此若全局 exact integer candidate 最终确实满足 \(r_1=r_2\)，证明必须读取一个 **不包含在当前 \(5\)-adic completion 中的独立 relation**。

---

# 7. Equal-support resonance

重点 chamber：

\[
r_1=r_2=r>0.
\]

写

\[
b_1=5^r\beta_1,
\qquad
b_2=5^r\beta_2,
\qquad
5\nmid\beta_1\beta_2.
\]

reducedness 给

\[
5\nmid a_1a_2.
\]

于是

\[
X=5^r a_1\beta_2,
\qquad
Y=5^r a_2\beta_1,
\]

\[
\lambda_N
=v_5(a_1^2\beta_2^2+a_2^2\beta_1^2).
\]

该 chamber 的整个非平凡 norm information 正好压在 \(\lambda_N\) 与一个 sign phase 上。

---

# 8. \(5\)-adic roots of \(-1\)

选择 canonical root

\[
\boxed{
\iota^2=-1,
\qquad
\iota\equiv2\pmod5.
}
\]

由于

\[
f(x)=x^2+1,
\qquad
f'(x)=2x,
\]

且根模 \(5\) 为 \(2,3\)，两根处 derivative 都是 unit，所以每一支唯一 Hensel lift。

前几级为：

\[
\begin{array}{c|c}
\text{modulus}&\text{roots of }x^2+1\\
\hline
5&2,3\\
25&7,18\\
125&57,68\\
625&182,443\\
3125&1068,2057
\end{array}
\]

若 \(U,V\in\mathbf Z_5^\times\)，则

\[
U^2+V^2=(U-\iota V)(U+\iota V).
\]

两个 factors 的差为

\[
2\iota V\in\mathbf Z_5^\times,
\]

所以它们不可能同时被 \(5\) 整除。

因此若

\[
\lambda=v_5(U^2+V^2)\ge1,
\]

存在唯一 \(\sigma\in\{\pm1\}\) 使

\[
\boxed{
\lambda=v_5(U-\sigma\iota V),
}
\]

且

\[
U+\sigma\iota V
\]

为 unit。

**状态：NEW PROVED / standard Hensel argument reconstructed here.**

---

# 9. Norm-phase parameterization

## Equal denominator support

令

\[
U=a_1\beta_2,
\qquad
V=a_2\beta_1.
\]

若 \(\lambda_N\ge1\)，则唯一 \(\sigma\) 满足

\[
U\equiv\sigma\iota V\pmod{5^{\lambda_N}}.
\]

故

\[
\boxed{
\frac{a_1}{a_2}
\equiv
K_\sigma
:=
\sigma\iota\frac{\beta_1}{\beta_2}
\pmod{5^{\lambda_N}}.
}
\]

更精确地：

\[
\boxed{
 a_1-K_\sigma a_2=5^{\lambda_N}z_N,
\qquad
z_N\in\mathbf Z_5^\times.
}
\]

## No denominator support + equal numerator support

若

\[
r_1=r_2=0,
\qquad
\alpha_1=\alpha_2=t,
\]

写

\[
a_i=5^tA_i,
\qquad
5\nmid A_1A_2.
\]

则

\[
X_0=A_1b_2,
\qquad
Y_0=A_2b_1.
\]

所以

\[
\boxed{
\frac{A_1}{A_2}
\equiv
K_\sigma
:=
\sigma\iota\frac{b_1}{b_2}
\pmod{5^{\lambda_N}}.
}
\]

同样可写

\[
A_1-K_\sigma A_2=5^{\lambda_N}z_N,
\qquad z_N\in\mathbf Z_5^\times.
\]

这回答 Q4：**YES，resonance 可以 canonical 地写成 ratio phase，而且 sign 唯一。**

---

# 10. Word-phase residue \(C_5\)

上一轮可用形式：

\[
C_5
=
a_3\frac D{5^s}
\left(\frac{b_3}{5^s}\right)^{-1}.
\]

本轮重新核验其 domain。

设

\[
d:=v_5(D).
\]

只要 \(R>0\)，由

\[
v_5(\Delta)=s+R>s
\]

和

\[
\Delta=b_3P-a_3D
\]

立刻有

\[
\boxed{d\ge s.}
\]

否则第二项具有严格更小 valuation，不可能使 \(\Delta\) 达到 \(s+R\)。

所以在真正使用 \(C_5\) 的所有 \(R>0\) states 中，\(D/5^s\) 自动为整数。

并且

\[
5\nmid a_3,
\qquad
5\nmid b_3/5^s,
\]

故

\[
\boxed{
 v_5(C_5)=d-s.
}
\]

若 \(R=0\)，则 phase theorem没有要求把上述 expression 当成 residue class；此时不应把可能的“负 valuation”强行解释成 integral residue。

**状态：NEW PROVED domain cleanup.**

---

# 11. Prefix-Valuation Lock

记

\[
p:=v_5(P),
\qquad
d:=v_5(D).
\]

因为

\[
\Delta=b_3P-a_3D,
\]

两项 valuation 分别为

\[
s+p,
\qquad d.
\]

而 \(R>0\) 时

\[
v_5(\Delta)=e=s+R.
\]

于是得到三分支。

## Theorem PVL — Prefix-Valuation Trichotomy

### I. \(R<p\)

此时

\[
s+p>s+R=e.
\]

为了使 difference 恰好有 valuation \(e\)，必须

\[
\boxed{d=e=s+R.}
\]

故

\[
\boxed{v_5(C_5)=R.}
\]

### II. \(R>p\)

此时

\[
s+p<e.
\]

若要 difference 的 valuation从 \(s+p\) 提升到 \(e\)，必须两项先具有同样 valuation：

\[
\boxed{d=s+p,}
\]

并发生 exact unit cancellation 到深度 \(e\)。

所以

\[
\boxed{v_5(C_5)=p<R,}
\]

且 phase congruence真正锁定

\[
\boxed{v_5(P)=v_5(C_5)=p.}
\]

### III. \(R=p\)

此时第一项 valuation已经等于 \(e\)。若 \(d<e\) 则不可能；故

\[
\boxed{d\ge s+R.}
\]

从而

\[
\boxed{v_5(C_5)\ge R.}
\]

该 congruence在 valuation 层只表现为 \(0\equiv0\pmod{5^R}\)，未必产生 unit lock。

**状态：NEW PROVED.**

特别，若 \(5\mid b_2\)，则 reducedness 给 \(p=0\)，所以任意 \(R>0\) 自动落在 Case II：

\[
\boxed{d=s.}
\]

这重新统一解释了上一轮的 derived result。

---

# 12. Same-cut feedback equations

假设 resonance branch 已写成

\[
a_1=K_\sigma a_2+5^Lz,
\qquad L=\lambda_N,
\qquad z\in\mathbf Z_5^\times.
\]

actual cut：

\[
P=a_1 10^n+a_2.
\]

代入：

\[
\boxed{
P
=(1+10^nK_\sigma)a_2
+10^n5^Lz.
}
\tag{SCF}
\]

## Same-Cut Transversality Lemma

若

\[
R<n+L,
\]

则

\[
10^n5^Lz\equiv0\pmod{5^R},
\]

所以

\[
\boxed{
P\equiv C_5\pmod{5^R}
\iff
(1+10^nK_\sigma)a_2\equiv C_5\pmod{5^R}.
}
\]

而

\[
\boxed{
1+10^nK_\sigma\in\mathbf Z_5^\times.
}
\]

因此：

\[
\boxed{
 a_2
\equiv
C_5(1+10^nK_\sigma)^{-1}
\pmod{5^R}
}
\]

是每个 sign branch 上的唯一 solution。

若把 self-consistency 写成

\[
F_\sigma(a_2)
=(1+10^nK_\sigma)a_2-C_5,
\]

则

\[
\boxed{
F_\sigma'(a_2)
=1+10^nK_\sigma
\in\mathbf Z_5^\times.
}
\]

所以 Hensel geometry 是 **simple / transverse root**，不是 singular tower。

**状态：NEW PROVED.**

这回答 Q5：可以合成一元 fixed-point congruence；但其 natural outcome 是唯一兼容 lift，而不是 contradiction。

---

# 13. Equal denominator support chamber

令

\[
r_1=r_2=r>0.
\]

此时 \(a_1,a_2\) 都是 units，故

\[
p=v_5(P)=0.
\]

若 \(R>0\)，PVL Case II 给

\[
\boxed{d=s.}
\]

另一方面：

\[
Q
=5^r
\left(
\beta_1 10^{m_2}+\beta_2
\right).
\]

括号内第一项被 \(5\) 整除，第二项为 unit，所以

\[
\boxed{v_5(Q)=r.}
\]

因为

\[
D=10^gQ,
\]

故

\[
d=g+r.
\]

于是

\[
\boxed{s=g+r.}
\tag{EDS}
\]

将其代入

\[
R=\lambda_N+2s-2r-n_3
\]

得到

\[
\boxed{
R=\lambda_N+2g-n_3.
}
\tag{EDR}
\]

现在计算 feedback penetration：

\[
\begin{aligned}
(n+\lambda_N)-R
&=(m_2+g+k_{12})+\lambda_N
-(\lambda_N+2g-n_3)\\
&=m_2+k_{12}+n_3-g.
\end{aligned}
\]

而 partial saturation 与 \(s=g+r<n_3\) 给

\[
n_3-g\ge r+1\ge2.
\]

又

\[
m_2\ge1,
\qquad
k_{12}\ge1.
\]

因此

\[
\boxed{
(n+\lambda_N)-R\ge4.
}
\tag{SH-ED}
\]

## Theorem SH-ED — Equal-Denominator Strict-Cut Shielding

任何 partial-\(5\), equal-denominator-support, \(R>0\) state 都满足

\[
\boxed{
R\le n+\lambda_N-4.
}
\]

所以 word phase 至少提前四个 \(5\)-adic digits 停止，永远碰不到 norm-excess leading error \(z_N\)。

**状态：NEW PROVED.**

这是一项比“\(R\le n\)”更精确的 threshold theorem：

- \(R\le n\)：连 norm sign \(K_\sigma\) 都看不到；
- \(n<R<n+\lambda_N\)：可以看到 norm branch center / sign；
- \(R\ge n+\lambda_N\)：才真正开始读取 exact norm Hensel error。

而最后一种情况在此 chamber **不可能发生**。

---

# 14. No denominator support chamber

令

\[
r_1=r_2=0.
\]

则

\[
\gamma=0.
\]

并且

\[
Q=b_1 10^{m_2}+b_2\equiv b_2\not\equiv0\pmod5,
\]

所以

\[
\boxed{v_5(Q)=0,\qquad d=v_5(D)=g.}
\]

## 14.1 Prefix valuation \(p=v_5(P)\) 的 exact piecewise formula

两项

\[
a_1 10^n,
\qquad a_2
\]

的 valuations 为

\[
A=n+\alpha_1,
\qquad B=\alpha_2.
\]

故：

- \(B<A\Rightarrow p=B\)；
- \(A<B\Rightarrow p=A\)；
- \(A=B\Rightarrow p=A+\lambda_P\)，其中 \(\lambda_P\) 是对应 unit cancellation depth。

这是 exact prefix valuation tree。

## 14.2 Unequal numerator supports

若

\[
\alpha_1<\alpha_2,
\]

则

\[
\nu=2\alpha_1,
\]

且必有

\[
p>\alpha_1.
\]

若

\[
\alpha_2<\alpha_1,
\]

则

\[
\nu=2\alpha_2,
\qquad
p=\alpha_2.
\]

这些是 nonresonant numerator states；不存在 \(\lambda_N\)。

## 14.3 Equal numerator support

若

\[
\alpha_1=\alpha_2=t,
\]

则

\[
\boxed{p=t}
\]

因为 \(a_2\) 项 valuation \(t\) 严格小于 \(a_1 10^n\) 的 \(n+t\)。

同时

\[
\boxed{
\nu=2t+\lambda_N,
}
\]

\[
\boxed{
R=\lambda_N+2t+2s-n_3.
}
\]

### Subchamber A: \(R<t\)

PVL 给

\[
g=s+R.
\]

但 phase modulus 不足以穿过 \(P\) 自身的 \(5^t\) content；没有 unit-level norm feedback。

### Subchamber B: \(R=t\)

PVL 只给

\[
g\ge s+t.
\]

phase 仍未得到 normalized unit lock。

### Subchamber C: \(R>t\)

PVL 给

\[
\boxed{g=s+t.}
\tag{NDS}
\]

写

\[
a_i=5^tA_i,
\qquad
P=5^tP_0,
\]

其中

\[
P_0=A_2+10^nA_1.
\]

此时 normalized phase depth

\[
\boxed{
R_0:=R-t
=\lambda_N+t+2s-n_3.
}
\]

而

\[
C_5
=5^t C_0,
\]

其中

\[
\boxed{
C_0
=a_3 2^gQ
\left(\frac{b_3}{5^s}\right)^{-1}
\in\mathbf Z_5^\times.
}
\]

norm ratio 写成

\[
A_1=K_\sigma A_2+5^{\lambda_N}z_N.
\]

于是

\[
P_0
=(1+10^nK_\sigma)A_2
+10^n5^{\lambda_N}z_N.
\]

计算 shielding margin：

\[
\begin{aligned}
(n+\lambda_N)-R_0
&=(m_2+g+k_{12})+\lambda_N
-(\lambda_N+t+2s-n_3)\\
&=m_2+k_{12}+n_3-s.
\end{aligned}
\]

由于 partial saturation

\[
n_3-s\ge1,
\]

故

\[
\boxed{
(n+\lambda_N)-R_0\ge3.
}
\tag{SH-ND}
\]

## Theorem SH-ND — Numerator-Resonance Strict-Cut Shielding

在 no-denominator-support、equal-numerator-resonance 且真正进入 unit phase 的 \(R>t\) subchamber 中：

\[
\boxed{
R_0\le n+\lambda_N-3.
}
\]

所以 normalized word phase 仍然读不到 norm leading error。

**状态：NEW PROVED.**

值得强调：这里 \(k_{12}\ge1\) 的作用与此前猜测相反。它不是增加 phase penetration，而是直接增加 shielding margin。

---

# 15. Mod \(5\) classification

由于

\[
n=m_2+g+k_{12}
\]

且

\[
m_2\ge1,
\qquad
k_{12}\ge1,
\]

有

\[
\boxed{n\ge2.}
\]

所以在模 \(5\) 上：

\[
P\equiv a_2\pmod5.
\]

在 resonance chamber 中 norm ratio为

\[
a_1\equiv K_\sigma a_2\pmod5.
\]

但 \(a_1\) 被乘上 \(10^n\)，整个 norm sign 对 \(P\bmod5\) 完全不可见。

因此 low-level same-cut system 只读：

\[
\boxed{a_2\equiv C_5\pmod5,}
\]

且只要 target valuation与 reducedness兼容，就没有 sign elimination。

**状态：NEW PROVED complete low-level observation.**

---

# 16. Mod \(25/125\) lifting

因为 \(n\ge2\)，同样有

\[
P\equiv a_2\pmod{25}.
\]

所以即使 norm branch 已经在 mod \(25\) 唯一提升为

\[
\iota\equiv7\pmod{25}
\]

或

\[
-\iota\equiv18\pmod{25},
\]

word phase 在 depth \(R\le2\) 时仍然完全看不见 branch sign。

只有当

\[
R>n
\]

时，\(10^nK_\sigma\) 才开始进入 fixed-point coefficient。

但 Strict-Cut Shielding 证明：即使进入这一层，仍有

\[
R<n+\lambda_N,
\]

所以只读取 branch center，不读取 branch error。

因此 mod \(25/125\) 没有出现 finite-level sign contradiction。

**状态：FAILED AS BRANCH ELIMINATION.**

---

# 17. Hensel branch analysis

本轮 Hensel picture 可以精确分成两种。

## Norm Hensel branch

\[
X_0-\sigma\iota Y_0=5^{\lambda_N}z_N,
\qquad
z_N\in\mathbf Z_5^\times.
\]

这里 \(\sigma\) 是唯一 sign，\(z_N\) 是 exact leading error。

## Word fixed-point Hensel branch

\[
F_\sigma(a_2)
=(1+10^nK_\sigma)a_2-C_5.
\]

因为

\[
F_\sigma'(a_2)\in\mathbf Z_5^\times,
\]

每个 sign branch 都有唯一 compatible residue lift。

因此这两个 Hensel structures 并没有形成“singular meets singular”的 collision；而是：

\[
\boxed{
\text{norm branch supplies a center }K_\sigma,
\quad
\text{word phase transverse 地选择同一 branch 上的 }a_2.
}
\]

这解释了为什么低阶 enumeration 很可能稳定成少数 branches，而不是突然空掉。

---

# 18. Fixed-point formulation

在 equal denominator support chamber：

\[
\boxed{
 a_2
\equiv
\frac{C_5}{1+10^nK_\sigma}
\pmod{5^R}.
}
\tag{FP-ED}
\]

在 no-denominator-support equal-numerator resonance 的 unit subchamber：

\[
\boxed{
 A_2
\equiv
\frac{C_0}{1+10^nK_\sigma}
\pmod{5^{R_0}}.
}
\tag{FP-ND}
\]

二者都具有 unit derivative。

所以本轮确实实现了用户要求的闭环：

\[
(a_1,a_2)
\to
N
\to
\nu
\to
R
\to
P\bmod5^R
\to
(a_1,a_2),
\]

但闭环的数学形状是一个 regular fixed point，而不是无 fixed point state machine。

---

# 19. Norm-excess ceiling attempts

## 19.1 Denominator-tail certificate 给出的 ceiling

A1 tail weight：

\[
\kappa=\frac{10^{m_3}QG}{b_3},
\qquad
m_3=n_3+g.
\]

记

\[
q=v_5(Q).
\]

则 partial chamber 中

\[
v_5(\kappa)
=n_3+g+q+\gamma-s.
\]

由于 \(n_3-s>0\)，有

\[
v_5(\kappa)>\gamma.
\]

因此

\[
\boxed{
v_5(\kappa+2G)=\gamma.
}
\]

尾 certificate

\[
10^{n_3}\mid\kappa^2(\kappa+2G)
\]

在 \(5\)-adic side 给

\[
2(n_3+g+q+\gamma-s)+\gamma\ge n_3.
\]

即

\[
\boxed{
2s\le n_3+2g+2q+3\gamma.
}
\tag{TC5}
\]

这是一个真实 denominator-only ceiling。

但代回

\[
R=\nu+2s-2\gamma-n_3
\]

只得到例如

\[
R\le\nu+2g+2q+\gamma,
\]

并不能压掉 resonance \(\lambda_N\)。

## 19.2 Archimedean trivial ceiling

固定一个具体整数 state，自然有

\[
5^{\lambda_N}
\le X_0^2+Y_0^2.
\]

因此 \(\lambda_N\) 被该 state 的 actual integer height 控制。

但这不是 uniform backward ceiling；随着 actual blocks 移动，右侧也移动。

## 19.3 Verdict

\[
\boxed{
\textbf{NO uniform Norm-Excess Ceiling found from current same-cut data.}
}
\]

第 26 节还会给出 arbitrary-\(\lambda_N\) 的 projected pseudo-family，直接攻击所有过强 ceiling conjectures。

---

# 20. Self-amplification attempts

候选机制：

\[
\lambda_N\ge k
\Longrightarrow
R\text{ deep}
\Longrightarrow
\text{cut fixes more digits}
\Longrightarrow
\lambda_N\ge k+1.
\]

本轮证明该路线在当前结构中失败有两个独立原因。

### 原因 1 — Strict-Cut Shielding

真正进入 resonance error 需要

\[
R\ge n+\lambda_N
\]

或 normalized 版本。

但 equal-denominator chamber 至少差 4 位；no-denominator resonance 至少差 3 位。

所以 phase 永远碰不到 \(z_N\)。

### 原因 2 — unit-part synchronization preserves exact valuation

第 21 节将证明 raw WGF 只把 norm leading error \(z_N\) 乘一个 unit 映射到 word leading error \(\widehat\Delta\)。

因此若 \(z_N\) 是 unit，word side 也只得到 unit，不会无条件多出一个 factor \(5\)。

故：

\[
\boxed{
\textbf{Norm-Excess Self-Amplification FAILED structurally.}
}
\]

---

# 21. True double-phase synchronization

raw A1-WR / word-gap factorization 可写为

\[
N\mathbf B^2b_3^2
=
G^2
(b_3\mathbf A-a_3\mathbf B)
(b_3\mathbf A+a_3\mathbf B).
\]

令

\[
C_+:=b_3\mathbf A+a_3\mathbf B.
\]

又

\[
b_3\mathbf A-a_3\mathbf B
=S\Delta.
\]

partial chamber 中：

\[
v_5(\mathbf B)=s,
\qquad
v_5(b_3)=s.
\]

并且

\[
C_+
=S(b_3P+a_3D)+2a_3b_3.
\]

第一部分 valuation 至少 \(n_3>s\)，第二部分 valuation 恰为 \(s\)，所以

\[
\boxed{v_5(C_+)=s.}
\]

定义 unit parts：

\[
\widehat N=N/5^\nu,
\quad
\widehat{\mathbf B}=\mathbf B/5^s,
\quad
\widehat b_3=b_3/5^s,
\]

\[
\widehat G=G/5^\gamma,
\quad
\widehat\Delta=\Delta/5^e,
\quad
\widehat C_+=C_+/5^s.
\]

利用

\[
e=\nu+3s-2\gamma-n_3
\]

精确消掉 \(5\)-powers，得到：

\[
\boxed{
\widehat N\,
\widehat{\mathbf B}^{\,2}
\widehat b_3^{\,2}
=
\widehat G^{\,2}
2^{n_3}
\widehat\Delta
\widehat C_+.
}
\tag{UNIT-SYNC}
\]

现在进入 norm resonance。

若

\[
X_0-\sigma\iota Y_0
=5^{\lambda_N}z_N,
\quad z_N\in\mathbf Z_5^\times,
\]

则

\[
\frac{X_0^2+Y_0^2}{5^{\lambda_N}}
=z_N(X_0+\sigma\iota Y_0).
\]

因此 \(\widehat N\) 是 \(z_N\) 乘一个 unit。

代回 UNIT-SYNC：

\[
\boxed{
\widehat\Delta
=U_5 z_N,
\qquad
U_5\in\mathbf Z_5^\times.
}
\]

## Theorem DPS — Double Phase Leading-Unit Synchronization

norm phase 与 word-gap phase 确实同步，但同步对象是

\[
\boxed{
\text{leading nonzero }5\text{-adic unit},
}
\]

不是额外 valuation。

**状态：NEW PROVED.**

这是本轮对“双 phase synchronization”最精确的最终表述。

---

# 22. Reducedness interaction

reducedness 在本轮主要做三件事：

1. denominator support一旦出现，立即删除同块 numerator 的 \(5\)-support；
2. Patterns II–IV 中 \(a_2\) 为 unit，从而 \(P\) 为 unit，并借 PVL 强迫 \(v_5(D)=s\)；
3. equal denominator support 中同时保证 norm ratio variables 为 units，允许直接进入 \(\mathbf Z_5^\times\) Hensel root of \(-1\)。

但 reducedness 并不排斥两个 norm sign，也不排斥 transverse fixed point。

特别：

\[
\boxed{
\text{reducedness 不会把 }1+10^nK_\sigma\text{ 变成 non-unit.}
}
\]

因此它不会制造 derivative degeneracy。

**状态：PROVED useful but insufficient.**

---

# 23. Digit-window interaction

若 fixed-point congruence给

\[
a_2\equiv a_2^*\pmod{5^R}
\]

且

\[
10^{n-1}\le a_2<10^n,
\]

那么仅当 \(5^R\) 超过该 interval length 时，才可能压成至多一个 integer representative。

但在 resonance chambers，当前没有 uniform theorem 强迫

\[
5^R>10^n.
\]

更重要的是，即使 \(R>n\)，这也不意味着 norm error被读到；真正 threshold 是

\[
R\ge n+\lambda_N.
\]

Strict-Cut Shielding 正好排除了后者。

所以 digit interval 在本轮最多是 eventual exact-rejection 工具，不是 uniform closure engine。

**状态：OPEN / not activated as proof.**

---

# 24. \(k_{12}\ge1\) interaction

上一轮已经否定：\(k_{12}\ge1\) 自动增加一位 phase penetration。

本轮得到更精确的新角色：

在两个 resonance shielding margins 中，\(k_{12}\) 以正号出现：

\[
(n+\lambda_N)-R
=m_2+k_{12}+n_3-g,
\]

以及

\[
(n+\lambda_N)-R_0
=m_2+k_{12}+n_3-s.
\]

因此：

\[
\boxed{
\textbf{strict excess }k_{12}\ge1
\textbf{ 是 shielding multiplier，而不是 phase amplifier.}
}
\]

这也是本轮对 strict cut 真正算术作用的一项新解释。

**状态：NEW PROVED.**

---

# 25. Computational stress tests / unequal-support local Hensel tower

本节只用计算先发现结构；下面给出可符号验证的 exact local theorem。

取 Pattern II trace：

\[
b_1=1,
\qquad b_2=5,
\]

\[
n_3=5,
\quad g=3,
\quad m_2=1,
\quad k_{12}=1,
\quad n=5,
\]

\[
b_3=10\,000\,625
=5^4\cdot16001,
\qquad s=4.
\]

于是

\[
Q=15,
\qquad
D=15000,
\qquad
G=5.
\]

固定

\[
a_1=a_3=1.
\]

令

\[
a_2=4+5t,
\qquad t\in\mathbf Z_5.
\]

则 \(a_2\) 始终为 unit，因此

\[
N=25+a_2^2
\]

为 unit：

\[
\nu=0.
\]

故

\[
R=0+8-2-5=1,
\]

\[
e=s+R=5.
\]

记

\[
S=10^5,
\quad
P=10^5+a_2,
\quad
\mathbf A=SP+1,
\quad
\mathbf B=SD+b_3.
\]

定义 raw A1-WR residual：

\[
F(t)
:=
N\mathbf B^2b_3^2
-G^2
(b_3\mathbf A-a_3\mathbf B)
(b_3\mathbf A+a_3\mathbf B).
\]

直接展开可验证：\(F(t)\) 的所有系数都被 \(5^{16}\) 整除。令

\[
H(t):=F(t)/5^{16}\in\mathbf Z_5[t].
\]

其模 \(5\) 恰为

\[
\boxed{
H(t)\equiv t+2\pmod5.
}
\]

所以

\[
t\equiv3\pmod5
\]

是 simple root，且

\[
H'(3)\equiv1\pmod5.
\]

由 Hensel：

\[
\boxed{
\exists!\ t_*\in\mathbf Z_5,
\quad
 t_*\equiv3\pmod5,
\quad
 H(t_*)=0.
}
\]

并且在该 root 上，\(\Delta\) 的 normalized leading unit保持非零，所以仍有 exact

\[
v_5(\Delta)=5,
\quad R=1.
\]

## Theorem UHL — Unequal-Support Local Hensel Survival

raw A1-WR 的 \(5\)-adic completion 中存在 partial-\(5\) exact branch 满足

\[
\boxed{
 r_1=0,
\quad r_2=1,
\quad R=1.
}
\]

**状态：NEW PROVED over \(\mathbf Z_5\), NOT an original integer candidate.**

特别说明：这里的 \(t_*\) 是一个 genuine \(5\)-adic integer，不能自动解释成满足固定 Archimedean digit interval 的 ordinary integer \(a_2\)。因此 UHL 只否定“纯 local \(5\)-adic algebra 自身足以杀掉 unequal support”，不否定未来由 exact digit window / integer realization 排除此 branch 的可能性。

该 theorem 的逻辑意义非常重要：

\[
\boxed{
\text{任何希望从纯 }5\text{-adic same-cut raw-WGF 推出 }
R>0\Rightarrow r_1=r_2
\text{ 的证明都不可能成立。}
}
\]

要排除此 branch，必须使用 \(\mathbf Z_5\)-completion 看不到的独立信息。

附带 finite stress tests 还在 Patterns I、III 中找到 analogous simple local roots；它们仅记为 **COMPUTATIONAL EVIDENCE**，不升级为 theorem。

---

# 26. Counterexamples / pseudo-families

本节构造一个任意深 \(\lambda_N\) 的 projected same-cut family，用来主动杀死过强 conjecture。

固定：

\[
b_1=b_2=5,
\qquad
b_3=1025=5^2\cdot41,
\]

\[
n_3=3,
\qquad
m_3=4,
\qquad
g=1,
\qquad s=2,
\]

\[
m_2=1,
\qquad
Q=55,
\qquad
D=550,
\qquad
G=25.
\]

取

\[
a_3=101.
\]

对任意

\[
\lambda\ge2,
\]

令

\[
n=\lambda+2,
\qquad
k_{12}=n-m_2-g=\lambda.
\]

则

\[
R=\lambda-1,
\qquad
e=\lambda+1
\]

是目标 valuation。

## 26.1 phase condition

因为

\[
\Delta
=1025P-101\cdot550
=25(41P-2222),
\]

且 \(n>\lambda\)，有

\[
P\equiv a_2\pmod{5^\lambda}.
\]

选一个合法 \(n\)-digit unit \(a_2\) 使

\[
\boxed{
41a_2-2222
\equiv
5^{\lambda-1}
\pmod{5^\lambda}.
}
\]

则

\[
\boxed{v_5(\Delta)=\lambda+1=e.}
\]

## 26.2 exact norm resonance

取任一 Hensel root

\[
\rho_\sigma^{(\lambda+1)}{}^2
\equiv-1
\pmod{5^{\lambda+1}}.
\]

要求

\[
\boxed{
 a_1-
ho_\sigma^{(\lambda+1)}a_2
\equiv
5^\lambda
\pmod{5^{\lambda+1}}.
}
\]

则展开

\[
a_1^2+a_2^2
\]

可见 cross term 在 \(5^\lambda\) 处为 unit，而 root error 已至少到 \(5^{\lambda+1}\)，所以

\[
\boxed{
v_5(a_1^2+a_2^2)=\lambda.
}
\]

因此

\[
N=25(a_1^2+a_2^2)
\]

满足

\[
\boxed{
\nu=2+\lambda.
}
\]

于是 phase formula 确实反馈回

\[
R
=\nu+2s-2\gamma-n_3
=(\lambda+2)+4-4-3
=\lambda-1.
\]

## 26.3 canonical word quotient也可同时保留

该 trace 有

\[
\mathbf B=551025,
\qquad
\Lambda=1025,
\qquad
\Gamma=25,
\]

\[
\boxed{E=22041,\qquad\gcd(E,10)=1.}
\]

canonical word forcing要求

\[
E\mid\mathbf A,
\qquad
\mathbf A=1000P+101.
\]

固定前述 \(a_2\) 后，这是关于 \(a_1\) 的一个 mod \(E\) 线性 congruence；其系数含 \(10^n\)，而 \(E\) 与 \(10\) 互素。

与此同时 norm resonance只固定 \(a_1\bmod5^{\lambda+1}\)。

由于

\[
\gcd(E,5)=1,
\]

CRT 可同时选取正整数 \(a_1\) 满足两者。

于是该 family 可同时保持：

- actual WORD；
- actual CUT；
- individual RED；
- canonical \(E\mid\mathbf A\)；
- exact norm valuation \(\nu\)；
- exact norm Hensel sign；
- exact determinant phase depth；
- arbitrarily large \(\lambda_N\)。

它**不声称**完整 BR-WGF equality 成立，因此不是 original candidate。

## Theorem PPF — Arbitrarily Deep Projected Same-Cut Pseudo-Family

上述条件对所有 \(\lambda\ge2\) 可同时实现。

**状态：NEW PROVED PROJECTED PSEUDO-FAMILY.**

它严格反驳以下过强 conjectures 作为当前 projected loop 的结论：

- high norm resonance impossible；
- \(\lambda_N\) 有 uniform local ceiling；
- phase congruence自动使 norm resonance collapse；
- \(\lambda_N\ge k\Rightarrow\lambda_N\ge k+1\)。

---

# 27. Partial-(5) closure attempt

本轮现在可以对 partial chamber 作比上一轮更细的全局 ledger。

## Closed by valuation deficit

仍有：

\[
\nu+3s<2\gamma+n_3
\Longrightarrow
\varnothing.
\]

## Cut-invisible phase

\[
0\le e\le s
\Longleftrightarrow
R=0
\]

仍是 open escape；same-cut feedback没有 modulus可读。

## Nonresonant cut-visible states

Patterns I–III 与 no-denominator unequal-numerator states 中，\(\nu\) 已 exact determined；但没有 universal contradiction。

尤其 UHL theorem 表明 unequal denominator support 在 full local \(\mathbf Z_5\)-A1-WR 中可以 survive。

## Resonant cut-visible states

equal denominator support 与 no-denominator equal-numerator support 均可压成 canonical norm sign + one-variable fixed point。

但 Strict-Cut Shielding 保证 phase 无法读取 norm leading error，fixed-point derivative 又是 unit，所以不出现 self-amplification。

故：

\[
\boxed{
0<v_5(b_3)<n_3
\quad\textbf{NOT CLOSED}.
}
\]

**状态：OPEN.**

---

# 28. Surviving Hensel towers

不能把整个 partial chamber 压成单一 \((\sigma,\lambda_N)\) tower，因为：

- unequal support Patterns I–III 本身没有 \(\lambda_N\) resonance；
- UHL 给出一个 genuine local unequal-support tower；
- no-denominator unequal-numerator support 也属于 nonresonant states。

但是 resonance subchambers 已经可以 canonical 地写成：

\[
\boxed{
(\sigma,\lambda_N,z_N)
}
\]

其中

- \(\sigma\) 是唯一 norm Hensel sign；
- \(\lambda_N\) 是 exact contact order；
- \(z_N\in\mathbf Z_5^\times\) 是 leading error。

word phase在当前 depth只读取 \((\sigma,\lambda_N)\) 给出的 branch center，而由 shielding 看不到 \(z_N\)。

因此更精确的 survivor picture 是：

\[
\boxed{
\text{nonresonant local branches}
\ \sqcup\ 
\text{two-sign resonance towers with hidden leading error}.
}
\]

---

# 29. Exact remaining theorem

本轮最重要的“缺什么”答案已经比上一轮更具体。

因为 UHL 证明：

\[
\boxed{
\text{完整 pure-}5\text{-adic raw A1-WR itself has surviving unequal-support branches.}
}
\]

所以继续添加只由同一 \(\mathbf Z_5\)-equation 推出的 \(5\)-adic congruence，不可能从原则上清空全部 survivors。

下一条真正独立 relation 应作用于同一个 source determinant：

\[
\Delta=b_3P-a_3D.
\]

最自然的 precise target 是：

## Backward A1 Same-Determinant \(2\)-Phase Companion Theorem

对 surviving partial-\(5\) state，重新从同一个 exact determinant / normalized word-gap 推导

\[
\boxed{
P\equiv C_2(T,a_3)
\pmod{2^{R_2}},
}
\]

并明确保存与 \(5\)-adic phase 相同的 source labels。

然后与

\[
P\equiv C_5(T,a_3)
\pmod{5^{R_5}}
\]

CRT 同步，得到真正的

\[
\boxed{
P\bmod10^j,
\qquad
j\le\min(R_2,R_5).
}
\]

只有到这一步，actual decimal suffix 才真正被 source phase 固定。

**状态：OPEN NEXT THEOREM.**

注意：本报告不声称 companion \(2\)-phase 一定足以关闭 A1；只证明它是当前 \(5\)-adic completion 中不存在的、最小且具体的独立同步信息。

---

# 30. Next chamber migration

由于 partial-\(5\) 未闭合，本轮不把精力迁移到：

\[
v_5(b_3)=0
\]

或 full absorption

\[
v_5(b_3)\ge n_3.
\]

但已明确：partial mechanism 中真正可迁移的不是“高 \(5\)-depth本身”，而是：

\[
\boxed{
\text{source-labelled determinant}
+
\text{actual cut}
+
\text{local phase companion}.
}
\]

若以后 partial chamber 被 companion-prime synchronization 关闭，再迁移到 full/no-absorption 才有意义。

---

# 31. Q1–Q9 final answers + PROVED / FAILED / OPEN ledger

## Q1. \(R_5^{\rm cut}>0\) 只可能出现在哪些 denominator support patterns？

\[
\boxed{
\textbf{当前不能压到 }r_1=r_2.
}
\]

所有五类 support pattern 在 valuation level 都可出现；对 \(r_1\ne r_2\) 有精确必要条件

\[
\boxed{
R=2s-n_3-2\max(r_1,r_2)>0.
}
\]

而且 Pattern II 在完整 local \(\mathbf Z_5\)-raw-WGF 中确有 Hensel survivor。

## Q2. \(\nu=v_5(N)\) 的 exact formula？

\[
\boxed{
\nu=
\begin{cases}
2x,&x<y,\\
2y,&y<x,\\
2t+\lambda_N,&x=y=t.
\end{cases}
}
\]

其中

\[
x=\alpha_1+r_2,
\qquad y=\alpha_2+r_1.
\]

## Q3. 真正不可控的 norm excess 是否只剩 \(\lambda_N\)？

**条件性 YES。** fixed valuation support state 上，唯一额外 cancellation 正是 \(\lambda_N\)。

但 globally 在 \(r_1=r_2=0\) chamber，\(\alpha_1,\alpha_2\) 本身仍是 moving numerator valuations，所以不能把完整 \(\nu\) 只记作 \(\lambda_N\)。

## Q4. norm resonance能否写成 ratio congruence？

\[
\boxed{\textbf{YES}.}
\]

resonance chamber 中：

\[
\boxed{
a_1/a_2\equiv K_\sigma\pmod{5^{\lambda_N}}}
\]

或除去共同 numerator \(5^t\) 后的对应公式；\(\sigma\) 唯一。

## Q5. 能否合成 same-cut fixed-point congruence？

\[
\boxed{\textbf{YES}.}
\]

典型形式：

\[
\boxed{
 a_2(1+10^nK_\sigma)
\equiv C_5
\pmod{5^R}.
}
\]

且 derivative 为 unit，因此是 transverse Hensel fixed point。

## Q6. 是否存在 Norm-Excess Ceiling 或 Self-Amplification contradiction？

\[
\boxed{\textbf{NO from current mechanism}.}
\]

- tail certificate只给 denominator-side \(s\) ceiling；
- arbitrary-\(\lambda\) projected pseudo-family反驳 uniform local \(\lambda_N\) ceiling；
- Strict-Cut Shielding + leading-unit synchronization否定当前 phase-driven self-amplification。

## Q7. partial \(5\)-saturation 是否完整关闭？

\[
\boxed{\textbf{NO}.}
\]

## Q8. survivors 能否压成一个 canonical Hensel tower？

\[
\boxed{\textbf{NO globally}.}
\]

resonance subchambers可压成两 sign Hensel towers，但 nonresonant unequal-support branches独立存在。

## Q9. 若仍不能，缺少哪个单一额外 relation？

当前分析还保留一个已存在但尚未被完全榨干的 nonlocal gate：**\(5\)-adic Hensel branch 是否真的拥有满足固定 decimal digit interval 的 ordinary-integer representative**。UHL 本身不回答这一点。

如果 Q9 要求给出一个新的、与当前 \(5\)-adic completion 真正独立的 arithmetic relation，而不是笼统地说“再用 digit window”，那么最具体的候选是：

\[
\boxed{
\textbf{same determinant }\Delta=b_3P-a_3D
\textbf{ 的 source-labelled }2\textbf{-adic phase companion}.}
\]

目标形式：

\[
\boxed{
P\equiv C_2(T,a_3)\pmod{2^{R_2}}
}
\]

与现有 \(5\)-phase CRT 同步成真正 decimal suffix constraint。

---

## FROZEN

- Strict frontier = A1-only；
- \(S=10^{n_3}\)；
- \(D=10^gQ\)；
- \(n=m_2+g+k_{12}\), \(k_{12}\ge1\)；
- exact word quotient / oriented gap normal form；
- \(\Delta=b_3P-a_3D\)；
- \(e=\nu+3s-2\gamma-n_3\)；
- \(R=\max(0,\nu+2s-2\gamma-n_3)\)；
- phase-to-cut congruence；
- actual cut不可删除；
- forward flat-locus result仅作 anti-duplication。

## NEW PROVED

1. Exact Norm-Valuation Tree；
2. all denominator-support formulas；
3. unified unequal-support formula
   \[
   R=2s-n_3-2\max(r_1,r_2);
   \]
4. exact prefix denominator valuation resonance classification；
5. Prefix-Valuation Trichotomy；
6. exact domain与 valuation of \(C_5\)；
7. canonical \(\mathbf Z_5\) norm phase \((\sigma,\lambda_N,z_N)\)；
8. Same-Cut Transversality Lemma；
9. Equal-Denominator Strict-Cut Shielding with margin \(\ge4\)；
10. No-Denominator Numerator-Resonance Shielding with margin \(\ge3\)；
11. \(k_{12}\) as shielding multiplier；
12. Double Phase Leading-Unit Synchronization；
13. Pattern II Unequal-Support Local Hensel Survival over \(\mathbf Z_5\)；
14. arbitrary-depth projected same-cut norm+phase pseudo-family。

## DERIVED

- equal denominator support + \(R>0\Rightarrow s=g+r\)；
- no denominator equal numerator support + \(R>t\Rightarrow g=s+t\)；
- low mod \(5/25\) word phase cannot see norm sign；
- denominator tail \(5\)-adic ceiling
  \[
  2s\le n_3+2g+2v_5(Q)+3\gamma.
  \]

## COMPUTATIONAL EVIDENCE

- additional simple local roots in Patterns I and III；
- finite coefficient checks for the UHL polynomial and pseudo-family discovery。

No global nonexistence theorem depends on computation.

## DISPROVED / FAILED AS CURRENT ROUTES

- \(R>0\Rightarrow r_1=r_2\) as a pure valuation / pure \(5\)-adic local consequence；
- \(R>n\) as the true threshold for norm feedback；
- norm sign elimination at mod \(5\) or mod \(25\)；
- uniform local Norm-Excess Ceiling；
- phase-driven \(\lambda_N\mapsto\lambda_N+1\) self-amplification；
- reducedness alone killing both Hensel signs；
- \(k_{12}\ge1\) as penetration gain。

## OPEN

1. same-determinant \(2\)-adic phase companion；
2. CRT source-phase to actual decimal suffix；
3. integer/archimedean rejection of surviving \(\mathbf Z_5\) branches；
4. partial-\(5\) closure；
5. no-absorption chamber \(v_5(b_3)=0\)；
6. full-absorption chamber \(v_5(b_3)\ge n_3\)；
7. full A1 closure。

---

# Source / provenance ledger

本报告主要回查并冻结以下当前项目文件：

- `strict_layer_backward_A1_5phase_cut_synchronization_campaign.md`：Phase-to-Cut theorem、partial-\(5\) unit dictionary、norm-excess identity、previous pseudo-family；
- `strict_layer_backward_A1_word_recovery_architecture_campaign.md`：canonical \((T,W,n)\) chart、BR-WGF、oriented word gap、actual cut不可删除；
- `strict_layer_post_DD_consolidation_A1_frontier.md`：Strict frontier = A1-only、A1 coefficient definitions；
- `strict_layer_backward_exact_root_pair_fibre_campaign.md`：one-word collapse 与 cut semantics；
- `strict_layer_backward_denominator_decimal_interface.md`：denominator trace 与 tail normalization；
- `strict_layer_backward_algebraic_denominator_interface.md` / canonical synchronization 系列：anti-false-gluing boundary；
- `strict_layer_unified_exact_lift_campaign.md`：Exact-Lift definitions / tail certificate provenance；
- `exact_lift_research_synthesis_2026-08-10.md`：仅作历史 provenance locator，不恢复已撤回 closure claim；
- `strict_layer_A1_flat_locus_structural_elimination_campaign.md`：仅用于确认最新正向线 anti-duplication boundary，不用于本报告的新 backward 证明。

---

# Final research verdict

本轮最低成功标准已经达到：

\[
\boxed{
(a_1,a_2)
\to
N
\to
\nu
\to
R_5
\to
P\bmod5^{R_5}
\to
(a_1,a_2)
}
\]

已经真正闭成 exact same-cut feedback system。

但其结构不是“无 fixed point”，而是：

\[
\boxed{
\textbf{regular }5\textbf{-adic fixed point}
+
\textbf{strict-cut shielding}
+
\textbf{surviving local Hensel towers}.
}
\]

因此本轮最重要的研究方向修正是：

\[
\boxed{
\textbf{不要继续向 pure }5\textbf{-adic norm-excess 追加弱 lemma。}
}
\]

下一步若继续 backward，最短新 frontier 应直接是：

\[
\boxed{
\textbf{Same-Determinant }2\textbf{-Phase}\times5\textbf{-Phase}\times\textbf{Actual Decimal Suffix Synchronization}.
}
\]
