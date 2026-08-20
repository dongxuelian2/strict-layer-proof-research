# Strict Layer A1 正向线第七轮：Double Euclidean Word Synchronization × Smith GCD Allocation — Terminal Closure Campaign

**文件名：** `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`  
**研究范围：** 三项十进制拼接平方和问题，Strict Layer，仅 `A1-only`。  
**本轮直接起点：**

- `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`
- `strict_layer_A1_double_euclidean_smith_gcd_terminal_campaign.md`（本轮执行期间 File Library 中发现的更新并行 terminal 报告；本文把它作为已完成输入，而不重复宣称其中结果）
- `strict_layer_A1_exact_word_state_after_double_euclidean_campaign.md`
- `strict_layer_A1_unified_state_after_long_campaign.md`
- 前五轮 A1 forward reports
- backward common-\(U\) pullback / radial redundancy audit（只作 provenance 与 anti-duplication）

---

# 1. Executive Summary

本轮**没有证明**

\[
\boxed{A_1=\varnothing}.
\]

因此 Strict Layer 仍未整体闭合：

\[
\boxed{DD=\varnothing,\qquad A_1\ {\rm OPEN}.}
\]

但是，相比此前 Double-Euclidean + Smith 报告，本轮又完成了四次真正的终端压缩。

## 1.1 NEW PROVED — Generic denominator mismatch 的 primitive residual 被完全正规化

令

\[
c_{23}:=\gcd(b_2,b_3).
\]

在 Smith 坐标

\[
b_1=s\alpha u,\qquad
b_2=s\alpha\beta t,\qquad
b_3=s\beta v
\]

中有

\[
c_{23}=s\beta,
\qquad
\gcd(\alpha t,v)=1.
\]

定义

\[
\boxed{
\widehat R:=\alpha t10^{n_3}-v.
}
\]

则

\[
\boxed{
R=c_{23}\widehat R=s\beta\widehat R.
}
\]

并且

\[
\boxed{\gcd(\widehat R,\alpha t)=1},
\]

\[
\boxed{
\gcd(\widehat R,v)=\gcd(10^{n_3},v),
}
\]

从而

\[
\boxed{
\gcd(\widehat R,\alpha tv)^{\langle10\rangle}=1.
}
\]

但 \(\widehat R=\pm1\) 或纯 \(2,5\)-smooth 仍可发生，因此：

\[
\boxed{
\text{“generic }R\neq0\text{ 自动产生 useful new odd prime”}
}
\]

是 **FAILED**。

---

## 1.2 NEW PROVED — \(HR2\) 的 canonical affine form

定义

\[
d_2:=Q_0-P_2,
\qquad
T_3:=Q_0-P_3,
\qquad
S_3:=P_3-d_2=P_2+P_3-Q_0.
\]

由

\[
10^{m_3}H
=
Q_0R-b_2d_2 10^{n_3}+b_3P_3
\]

和

\[
b_3=b_2 10^{n_3}-R
\]

得到：

\[
\boxed{
10^{m_3}H
=
R\,T_3+b_2 10^{n_3}S_3.
}
\tag{HR2}
\]

这条式子是 **PROVED**。

但其模 \(10^{n_3}\) 推论

\[
10^{n_3}\mid R T_3
\]

并不是新的独立 decimal divisor gate；本轮证明：

\[
\boxed{
\gcd(R,10^{n_3})
=
\gcd(b_3,10^{n_3}),
}
\]

因此

\[
\frac{10^{n_3}}{\gcd(R,10^{n_3})}\mid T_3
\]

与既有

\[
K_3=\frac{b_3T_3}{10^{n_3}}\in\mathbb Z
\]

携带的是同一 decimal divisibility。

所以：

\[
\boxed{
\text{DIV-R 是 exact regrouping，但不是新的 independent closure gate.}
}
\]

---

## 1.3 NEW PROVED — Double Smith–Euclidean Core

这是本轮最重要的新正规形。

继承上一份 terminal 报告：

\[
\delta_\beta:=\gcd(\beta,10^{m_3}),
\qquad
\beta^\sharp:=\frac{\beta}{\delta_\beta},
\]

\[
M_H=s\alpha\beta^\sharp\mid H,
\]

\[
q_H:=\frac{H}{s\alpha\beta^\sharp},
\]

\[
A_3:=\frac{Q_0-P_3}{\alpha},
\]

\[
\Lambda_\beta:=\frac{10^{m_3}}{\delta_\beta},
\]

以及 Smith-reduced tail equation

\[
\Lambda_\beta q_H
=
tP_2 10^{n_3}-vA_3.
\]

由 \(\gcd(\alpha t,v)=1\) 与 gcd-profile ratio 可写

\[
P_2=vM,\qquad M\in\mathbb Z_{>0}.
\]

于是：

\[
\Lambda_\beta q_H
=
v\left(tM10^{n_3}-A_3\right).
\]

定义

\[
\delta_v:=\gcd(v,\Lambda_\beta),
\]

\[
\boxed{
v^\sharp:=\frac{v}{\delta_v},
\qquad
J:=\frac{\Lambda_\beta}{\delta_v},
\qquad
\gcd(v^\sharp,J)=1.
}
\]

则存在唯一

\[
\boxed{Z\in\mathbb Z\setminus\{0\}}
\]

使：

\[
\boxed{
q_H=v^\sharp Z,
}
\tag{DS1}
\]

\[
\boxed{
tM10^{n_3}-A_3=JZ.
}
\tag{DS2}
\]

因此：

\[
\boxed{
H=s\alpha\beta^\sharp v^\sharp Z.
}
\tag{DS3}
\]

这是比此前

\[
s\alpha\beta^\sharp\mid H
\]

更强的 forced divisor theorem。

若记

\[
\boxed{
M_H^{(2)}
:=
s\alpha\beta^\sharp v^\sharp,
}
\]

则：

\[
\boxed{M_H^{(2)}\mid H.}
\]

同时：

\[
\boxed{
\alpha J\mid X,
}
\]

其中 \(X\) 是下文的 affine geometric defect。

更漂亮的是：

\[
\boxed{
\frac{\alpha J}{M_H^{(2)}}
=
\frac1{\beta_3},
\qquad
\beta_3=\frac{b_3}{10^{m_3}}\in[0.1,1).
}
\tag{BAL}
\]

所以两个强制 divisor 的大小自动相差一个真实 denominator mantissa，比例始终在 \((1,10]\) 内。

这是真正的：

\[
\boxed{
\textbf{Double Smith–Euclidean Core}.
}
\]

---

## 1.4 NEW PROVED — 第三个 Smith 因子与完整 denominator determinant

此前 Smith 只显式使用 pair \(12\) 与 pair \(23\)。

本轮定义：

\[
\boxed{
\gamma
:=
\frac{\gcd(b_1,b_3)}s.
}
\]

由 Smith chart 可严格证明：

\[
\boxed{\gamma=\gcd(u,v).}
\]

而且：

\[
\boxed{
\gcd(\alpha,\beta)
=
\gcd(\beta,\gamma)
=
\gcd(\gamma,\alpha)
=1.
}
\]

因此三对 denominator gcd 完整写成：

\[
\boxed{
\gcd(b_1,b_2)=s\alpha,
}
\]

\[
\boxed{
\gcd(b_2,b_3)=s\beta,
}
\]

\[
\boxed{
\gcd(b_1,b_3)=s\gamma.
}
\]

定义

\[
\beta_0:=\beta^{\langle10\rangle},
\qquad
\gamma_0:=\gamma^{\langle10\rangle}.
\]

则本轮证明：

\[
\boxed{\alpha\mid Q_0,}
\]

\[
\boxed{\beta_0\mid Q_0,}
\]

\[
\boxed{\gamma_0\mid Q_0.}
\]

又三者两两互素，故：

\[
\boxed{
\Sigma_b
:=
\alpha\beta_0\gamma_0
\mid Q_0.
}
\tag{SMITH-Q}
\]

并且：

\[
\boxed{
s\Sigma_b\mid H.
}
\tag{SMITH-H}
\]

所有 \(\Sigma_b\) 中的 odd prime 均满足

\[
\boxed{p\equiv1\pmod4.}
\]

所以本轮终于得到一个真正完整的 denominator Smith determinant allocation。

但是：

\[
\Sigma_b
\]

没有 uniform lower bound；可以等于 \(1\)。因此 determinant capacity **仍不足以单独闭合**。

---

## 1.5 NEW PROVED — sign mismatch 被精确压进 transition chambers

定义：

\[
\widehat R=\alpha t10^{n_3}-v.
\]

再令

\[
P_2=vM.
\]

定义：

\[
\boxed{
X_0:=tM10^{n_3}-A_3.
}
\]

则：

\[
\boxed{
10^{m_3}H=b_3\alpha X_0,
}
\]

所以

\[
\boxed{\operatorname{sgn}H=\operatorname{sgn}X_0.}
\]

而：

\[
\boxed{\operatorname{sgn}R=\operatorname{sgn}\widehat R.}
\]

进一步：

\[
\boxed{
S_3=\alpha X_0-M\widehat R.
}
\tag{AFF}
\]

结合 Double Smith–Euclidean Core：

\[
X_0=JZ,
\]

得：

\[
\boxed{
S_3=\alpha JZ-M\widehat R.
}
\tag{AFF2}
\]

若 \(H,R\) 异号，则 \(JZ\) 与 \(\widehat R\) 异号，因此：

\[
\boxed{
|S_3|
=
\alpha J|Z|
+
M|\widehat R|
\ge
\alpha J+M.
}
\tag{MIS}
\]

这把原本 approximate 的 “sign coupling” 变成 exact integer theorem。

特别对 \(g\ge1\)：

- \(d\le-1\)：必为 plus，而 \(R<0\)，故**自动同号**；
- \(d\ge2\)：必为 minus，而 \(R>0\)，故**自动同号**；
- \(d=1\)：\(R>0\)，异号只可能是 **plus**；
- 所有其他异号只能发生在 \(d=0\)。

所以：

\[
\boxed{
\textbf{all H/R sign mismatch is localized to }d=0
\textbf{ or }(d=1,\text{plus}).
}
\tag{TRANS-SIGN}
\]

这是本轮对 generic \(R\neq0\) 最干净的新压缩之一。

---

## 1.6 FINAL VERDICT

本轮没有得到：

\[
R\neq0\Longrightarrow\bot
\]

也没有得到：

\[
R=0\Longrightarrow\bot.
\]

更重要的是，已有 fixed-profile synchronized pseudo-family 严格表明：

\[
\boxed{
\text{exact word + Smith + primitive sphere}
}
\]

在不恢复 common-\(U\) 时仍可无界。

因此正确的 terminal architecture 已经非常清楚：

\[
\boxed{
\text{Double Smith–Euclidean Core}
+
\text{primitive affine sign geometry}
+
\text{common coprime }U\text{ successor gate}.
}
\]

本轮认为下一步最小剩余 theorem 应写成：

\[
\boxed{
\textbf{Iterated-Smith Coprime-Radial Exclusion Theorem}.
}
\]

而不是继续寻找第三个 standalone word congruence。

---

# 2. Frozen Six-Round + Parallel-Terminal Results

以下全部冻结使用，不重复证明。

## 2.1 Primitive sphere

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

并且 primitive hypotenuse：

\[
\boxed{Q_0\text{ odd}.}
\]

## 2.2 Common radial reconstruction

\[
g_i=\gcd(V,P_i),
\]

\[
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac V{g_i},
\qquad
\gcd(U,V)=1.
\]

## 2.3 Exponents

\[
g=m_3-n_3\ge0,
\qquad
k\ge1,
\qquad
d=m_2-g,
\]

\[
\boxed{
m_2=g+d,
\quad
n_2=2g+k+d,
\quad
m_3=n_3+g.
}
\]

## 2.4 Axis geometry

\[
d_2:=Q_0-P_2,
\]

\[
P_1^2+P_3^2=d_2(2Q_0-d_2).
\]

对 \(g\ge1\)：

\[
\boxed{
\sqrt{96/101}<P_2/Q_0<1,
}
\]

\[
\boxed{
\frac12
<
10^{2k}\frac{d_2}{Q_0}
<
2.532,
}
\]

以及：

\[
\boxed{
\frac{Q_0}{1100\,10^{2g+k}}
<
P_3
<
100Q_0\,10^{-(2g+k)}.
}
\]

## 2.5 Defect / Euclidean system

\[
D:=P_1 10^k-Q_0>0,
\]

\[
H:=b_2Q_0-b_1 10^{m_2}D\ne0.
\]

plus / minus：

\[
\boxed{\text{plus}\iff H<0,}
\qquad
\boxed{\text{minus}\iff H>0.}
\]

定义：

\[
Q_{12}:=b_1 10^{m_2}+b_2.
\]

Leading exact relation：

\[
\boxed{
b_1P_1 10^{m_2+k}
=
Q_0Q_{12}-H.
}
\tag{E1}
\]

定义：

\[
K_3
:=
\frac{b_3(Q_0-P_3)}{10^{n_3}}
\in\mathbb Z_{>0}.
\]

Tail exact relation：

\[
\boxed{
b_2P_2
=
10^gH+K_3.
}
\tag{E3}
\]

因此：

\[
\boxed{
K_3\equiv b_2P_2\pmod{10^g}.
}
\]

## 2.6 Prefix Euclidean division

定义：

\[
c_{\rm pref}
:=
\left\lceil\frac H{Q_0}\right\rceil.
\]

则：

\[
\boxed{
q_{\rm pref}=Q_{12}-c_{\rm pref},
}
\]

\[
\boxed{
r_{\rm pref}=c_{\rm pref}Q_0-H,
\quad
0\le r_{\rm pref}<Q_0.
}
\]

plus：

\[
c_{\rm pref}=0,
\qquad
r_{\rm pref}=-H.
\]

minus：

\[
c=c_{\rm pref}\ge1.
\]

对 \(g\ge1\)：

\[
\boxed{1\le c\le10^d\le b_2,}
\]

因此 borrow 不进入 \(b_1\) block。

## 2.7 Branch map

对 \(g\ge1\)：

\[
\boxed{
d\le-1\Longrightarrow\text{plus},
}
\]

\[
\boxed{
d\ge2\Longrightarrow\text{minus}.
}
\]

真正 dual-sign transition：

\[
\boxed{d\in\{0,1\}.}
\]

## 2.8 Smith chart

\[
\boxed{
b_1=s\alpha u,
\quad
b_2=s\alpha\beta t,
\quad
b_3=s\beta v,
}
\]

\[
\boxed{
\gcd(u,\beta t)=1,
\qquad
\gcd(\alpha t,v)=1,
\qquad
\gcd(\alpha,\beta)=1.
}
\]

已有：

\[
\boxed{
\alpha\mid(Q_0-P_3),
}
\]

\[
\boxed{
\beta\mid10^{m_2+m_3}D,
}
\]

\[
\boxed{
\beta^{\langle10\rangle}\mid D.
}
\]

---

# 3. Exact Terminal State

本文后续只使用：

\[
(P_1,P_2,P_3,Q_0),
\]

\[
(g,k,d,n_3),
\]

\[
(s,\alpha,\beta,u,t,v),
\]

\[
(D,H,R,K_3),
\]

和本轮新 reduced variables：

\[
(M,A_3,\widehat R),
\]

\[
(\delta_\beta,\beta^\sharp,\Lambda_\beta),
\]

\[
(\delta_v,v^\sharp,J,Z),
\]

以及第三 Smith factor：

\[
\gamma.
\]

不重新引入旧几十维 profile chart。

---

# 4. Leading Euclidean Relation

冻结：

\[
A_{\rm lead}
:=
b_1P_1 10^{m_2+k}.
\]

则：

\[
A_{\rm lead}
=
Q_0Q_{12}-H.
\]

因此 exact Euclidean quotient / remainder 为：

\[
q_{\rm pref}=Q_{12}-\left\lceil H/Q_0\right\rceil,
\]

\[
r_{\rm pref}
=
\left\lceil H/Q_0\right\rceil Q_0-H.
\]

**PROVED / inherited.**

这核准了 prompt 中 E1 的 sign：

\[
\boxed{
b_1P_1 10^{m_2+k}
=
Q_0Q_{12}-H.
}
\]

---

# 5. Third-Tail Euclidean Relation

冻结：

\[
K_3
=
\frac{b_3T_3}{10^{n_3}},
\qquad
T_3=Q_0-P_3.
\]

\[
b_2P_2
=
10^gH+K_3.
\]

令：

\[
r_{10}:=b_2P_2\bmod10^g.
\]

则：

\[
K_3\bmod10^g=r_{10}.
\]

写：

\[
b_2P_2=10^gq_2+r_{10},
\]

\[
K_3=10^gq_3+r_{10},
\]

则：

\[
\boxed{
q_2-q_3=H.
}
\]

**PROVED / inherited.**

---

# 6. Double Euclidean Diagram

完整 exact cascade：

\[
\boxed{
b_1D
\xrightarrow{\times10^{m_2}}
b_2Q_0-H
}
\]

\[
\boxed{
H
\xrightarrow{\times10^g}
b_2P_2-K_3
}
\]

\[
\boxed{
K_3
\xrightarrow{\times10^{n_3}}
b_3(Q_0-P_3).
}
\]

这一 cascade 可以组合恢复 master，但本轮的关键不是组合回旧 master，而是对中间 defect 连续做 gcd/SNF deflation。

---

# 7. \(H\) as Remainder / Borrow

plus：

\[
-Q_0<H<0.
\]

故：

\[
\boxed{
r_{\rm pref}=-H.
}
\]

minus：

\[
H=cQ_0-r_{\rm pref},
\qquad
1\le c\le10^d.
\]

对 \(g\ge1\)：

\[
c\le b_2,
\]

所以所有 borrow 都留在 \(b_2\) block 内。

**PROVED / inherited.**

---

# 8. \(R\) and Pairwise GCD-Ratio Defect

定义：

\[
R:=b_2 10^{n_3}-b_3.
\]

利用：

\[
b_2=s\alpha\beta t,
\qquad
b_3=s\beta v,
\]

得到：

\[
\boxed{
R=s\beta(\alpha t10^{n_3}-v).
}
\]

定义：

\[
\boxed{
\widehat R:=\alpha t10^{n_3}-v.
}
\tag{Rhat}
\]

于是：

\[
\boxed{
R=s\beta\widehat R.
}
\]

### Lemma 8.1

\[
\boxed{
\gcd(\widehat R,\alpha t)=1.
}
\]

**Proof.**

若 \(p\mid\widehat R,\alpha t\)，则

\[
v
=
\alpha t10^{n_3}-\widehat R
\equiv0\pmod p,
\]

与 \(\gcd(\alpha t,v)=1\) 矛盾。

**状态：PROVED.**

### Lemma 8.2

\[
\boxed{
\gcd(\widehat R,v)
=
\gcd(10^{n_3},v).
}
\]

**Proof.**

模 \(v\)：

\[
\widehat R
\equiv
\alpha t10^{n_3}\pmod v.
\]

而 \(\gcd(\alpha t,v)=1\)。

**状态：PROVED.**

因此：

\[
\boxed{
\gcd(\widehat R,\alpha tv)^{\langle10\rangle}=1.
}
\tag{Rhat-coprime}
\]

这严格证明 prompt 中 \(S_0\) ten-free coprimality 的正确版本。

---

# 9. FAILED — \(S_0\neq0\) 自动产生 useful new odd prime

虽然：

\[
\gcd(\widehat R,\alpha tv)^{\langle10\rangle}=1,
\]

但：

\[
\widehat R=\pm1
\]

完全可能。

也可以有：

\[
|\widehat R|=2^a5^b.
\]

因此不存在 unconditional theorem：

\[
\widehat R\ne0
\Longrightarrow
\exists p\ne2,5,\ p\mid\widehat R.
\]

所以 Zsigmondy / private-prime 路线在 moving \((\alpha t,v)\) 下不能作为 generic closure 主轴。

**状态：FAILED.**

---

# 10. Derivation of HR2

冻结：

\[
10^{m_3}H
=
Q_0R-b_2d_2 10^{n_3}+b_3P_3.
\]

代入：

\[
b_3=b_2 10^{n_3}-R.
\]

得到：

\[
10^{m_3}H
=
R(Q_0-P_3)
+
b_2 10^{n_3}(P_3-d_2).
\]

即：

\[
\boxed{
10^{m_3}H
=
RT_3+b_2 10^{n_3}S_3.
}
\tag{HR2}
\]

其中：

\[
T_3=Q_0-P_3,
\qquad
S_3=P_3-d_2.
\]

**状态：NEW PROVED.**

---

# 11. Decimal Divisor Allocation from HR2 is Redundant

HR2 模 \(10^{n_3}\)：

\[
\boxed{
10^{n_3}\mid RT_3.
}
\tag{DIV-R}
\]

乍看似乎得到：

\[
M_{10}
:=
\frac{10^{n_3}}{\gcd(R,10^{n_3})}
\mid T_3.
\]

但本轮进一步证明：

\[
\boxed{
\gcd(R,10^{n_3})
=
\gcd(b_3,10^{n_3}).
}
\tag{R10}
\]

### Proof

对 \(p=2,5\)，令：

\[
c=v_p(s\beta),
\qquad
r=v_p(v).
\]

由：

\[
\widehat R=\alpha t10^{n_3}-v,
\qquad
\gcd(\alpha t,v)=1,
\]

可得：

\[
\min(v_p(\widehat R),n_3)=\min(r,n_3).
\]

于是：

\[
\min(v_p(R),n_3)
=
\min(c+r,n_3)
=
\min(v_p(b_3),n_3).
\]

证毕。

因此：

\[
\boxed{
\frac{10^{n_3}}{\gcd(R,10^{n_3})}
=
\frac{10^{n_3}}{\gcd(b_3,10^{n_3})}.
}
\]

而后者正是由：

\[
10^{n_3}\mid b_3T_3
\]

已经得到的最小 decimal divisor。

所以：

\[
\boxed{
\text{HR2 的 DIV-R 不新增 decimal depth。}
}
\]

**状态：NEW PROVED REDUNDANCY RESULT.**

---

# 12. Smith GCD Allocation — Full Three-Pair Completion

已有：

\[
s=\gcd(b_1,b_2,b_3),
\]

\[
\gcd(b_1,b_2)=s\alpha,
\]

\[
\gcd(b_2,b_3)=s\beta.
\]

本轮定义：

\[
\boxed{
\gamma
:=
\frac{\gcd(b_1,b_3)}s.
}
\]

由：

\[
b_1=s\alpha u,
\qquad
b_3=s\beta v,
\]

以及：

\[
\gcd(\alpha,\beta)=1,
\]

\[
\gcd(u,\beta)=1,
\]

\[
\gcd(\alpha,v)=1,
\]

得到：

\[
\boxed{
\gamma=\gcd(u,v).
}
\tag{GAMMA}
\]

并立即：

\[
\boxed{
\gcd(\gamma,\alpha)
=
\gcd(\gamma,\beta)
=1.
}
\]

因此：

\[
\boxed{
\alpha,\beta,\gamma
\text{ pairwise coprime}.
}
\]

**状态：NEW PROVED.**

---

# 13. Full Smith LCM Formula

写：

\[
u=\gamma u_0,
\qquad
v=\gamma v_0,
\qquad
\gcd(u_0,v_0)=1.
\]

利用三数 lcm identity：

\[
\operatorname{lcm}(b_1,b_2,b_3)
=
\frac{
b_1b_2b_3\gcd(b_1,b_2,b_3)
}{
\gcd(b_1,b_2)\gcd(b_2,b_3)\gcd(b_1,b_3)
},
\]

得到：

\[
\boxed{
V
=
s\alpha\beta\gamma u_0tv_0.
}
\tag{V-SNF}
\]

从而：

\[
\boxed{
g_1=\frac V{b_1}
=
\beta tv_0,
}
\]

\[
\boxed{
g_2=\frac V{b_2}
=
\gamma u_0v_0,
}
\]

\[
\boxed{
g_3=\frac V{b_3}
=
\alpha u_0t.
}
\tag{g-SNF}
\]

因此：

\[
\boxed{\beta\mid g_1\mid P_1,}
\]

\[
\boxed{\gamma\mid g_2\mid P_2,}
\]

\[
\boxed{\alpha\mid g_3\mid P_3.}
\]

这使 denominator pairwise gcd lattice 与 primitive coordinates 的 allocation 完全对称。

**状态：NEW PROVED.**

---

# 14. Smith Determinant Allocation into \(Q_0\)

## 14.1 \(\alpha\)-channel

已有：

\[
\alpha\mid T_3=Q_0-P_3.
\]

而新 full-Smith formula 给：

\[
\alpha\mid P_3.
\]

所以：

\[
\boxed{\alpha\mid Q_0.}
\]

因为 \(Q_0\) odd：

\[
\boxed{\alpha\text{ odd}.}
\]

## 14.2 \(\beta\)-channel

定义：

\[
\beta_0:=\beta^{\langle10\rangle}.
\]

已有：

\[
\beta_0\mid D.
\]

而：

\[
\beta\mid P_1.
\]

所以：

\[
\beta_0\mid P_1.
\]

由：

\[
D=P_1 10^k-Q_0
\]

且 \(\gcd(\beta_0,10)=1\)，得到：

\[
\boxed{\beta_0\mid Q_0.}
\]

## 14.3 \(\gamma\)-channel

定义：

\[
\gamma_0:=\gamma^{\langle10\rangle}.
\]

由：

\[
\gamma\mid P_2
\]

知：

\[
\gamma_0\mid P_2.
\]

另一方面，从 E3 与 H definition 消元得到 exact master form：

\[
\boxed{
b_2 10^{n_3}(P_2-10^gQ_0)
+
b_1 10^{m_2+m_3}D
=
b_3T_3.
}
\tag{MASTER-23}
\]

除以 \(s\)，模 \(\gamma_0\)：

- \(\gamma_0\mid u\)；
- \(\gamma_0\mid v\)；
- \(\gcd(\gamma_0,\alpha\beta t10)=1\)。

所以第二项与右侧均为 \(0\pmod{\gamma_0}\)，第一项系数为 unit，故：

\[
\boxed{
\gamma_0\mid P_2-10^gQ_0.
}
\]

再用：

\[
\gamma_0\mid P_2,
\qquad
\gcd(\gamma_0,10)=1,
\]

得到：

\[
\boxed{\gamma_0\mid Q_0.}
\]

---

## 14.4 Full determinant

由于：

\[
\alpha,\beta_0,\gamma_0
\]

两两互素：

\[
\boxed{
\Sigma_b
:=
\alpha\beta_0\gamma_0
\mid Q_0.
}
\]

这是本轮回答 prompt “denominator Smith determinant” 的最自然 exact form。

**状态：NEW PROVED.**

---

# 15. Prime Class of the Third Smith Channel

若 odd prime：

\[
p\mid\gamma_0,
\]

则：

\[
p\mid P_2,Q_0.
\]

sphere 模 \(p\)：

\[
P_1^2+P_3^2\equiv0\pmod p.
\]

primitive gcd 保证 \(P_1,P_3\) 不可能同时被 \(p\) 整除。

所以 \(-1\) 必为 \(p\) 的 quadratic residue：

\[
\boxed{p\equiv1\pmod4.}
\]

结合已有 \(\alpha,\beta_0\) 结果：

\[
\boxed{
p\mid\Sigma_b
\Longrightarrow
p\equiv1\pmod4.
}
\]

**状态：NEW PROVED EXTENSION OF ASYM-4.**

---

# 16. Double Smith–Euclidean Deflation

继承：

\[
\widehat H
=
\beta tQ_0-u10^{m_2}D,
\]

\[
H=s\alpha\widehat H.
\]

定义：

\[
\delta_\beta=\gcd(\beta,10^{m_3}),
\]

\[
\beta^\sharp=\beta/\delta_\beta.
\]

已有：

\[
\beta^\sharp\mid\widehat H.
\]

定义：

\[
q_H:=\widehat H/\beta^\sharp
=
H/(s\alpha\beta^\sharp).
\]

又：

\[
A_3:=T_3/\alpha,
\]

\[
\Lambda_\beta:=10^{m_3}/\delta_\beta.
\]

已有：

\[
\boxed{
\Lambda_\beta q_H
=
tP_2 10^{n_3}-vA_3.
}
\tag{SR-T}
\]

由：

\[
g_2=u_0v,
\]

故：

\[
v\mid P_2.
\]

定义：

\[
\boxed{
M:=P_2/v\in\mathbb Z_{>0}.
}
\]

于是：

\[
\Lambda_\beta q_H
=
v\left(tM10^{n_3}-A_3\right).
\]

定义：

\[
\delta_v:=\gcd(v,\Lambda_\beta),
\]

\[
v^\sharp:=v/\delta_v,
\]

\[
J:=\Lambda_\beta/\delta_v.
\]

则：

\[
\gcd(v^\sharp,J)=1.
\]

所以存在唯一非零整数 \(Z\) 使：

\[
\boxed{
q_H=v^\sharp Z,
}
\]

\[
\boxed{
tM10^{n_3}-A_3=JZ.
}
\]

这就是 **Double Smith–Euclidean Core**。

**状态：NEW PROVED.**

---

# 17. New Strongest Forced Divisor of \(H\)

由：

\[
H=s\alpha\beta^\sharp q_H
\]

和：

\[
q_H=v^\sharp Z
\]

得到：

\[
\boxed{
H
=
s\alpha\beta^\sharp v^\sharp Z.
}
\]

因此：

\[
\boxed{
M_H^{(2)}
=
s\alpha\beta^\sharp v^\sharp
\mid H.
}
\tag{MH2}
\]

又：

\[
\beta_0\mid\beta^\sharp,
\]

\[
\gamma_0\mid v^\sharp
\]

（因为从 \(v\) 到 \(v^\sharp\) 只剥除 \(2,5\)-part），故：

\[
\boxed{
s\alpha\beta_0\gamma_0=s\Sigma_b\mid H.
}
\]

这把 Smith determinant 同时分配给：

\[
Q_0
\]

与：

\[
H.
\]

**状态：NEW PROVED.**

---

# 18. Affine Geometric Defect \(X\)

定义：

\[
\boxed{
X_0:=tM10^{n_3}-A_3.
}
\]

则 Double Smith core 给：

\[
\boxed{X_0=JZ.}
\]

因为：

\[
P_3=\alpha u_0t C_3
\]

且 ratio reduction 给：

\[
g_3/g_2=\alpha t/v,
\]

也可直接写：

\[
P_3=\alpha tN
\]

for some integer \(N>0\)。

于是：

\[
A_3
=
\frac{Q_0-P_3}{\alpha}.
\]

所以：

\[
\alpha X_0
=
\alpha tM10^{n_3}-T_3.
\]

定义：

\[
\boxed{
X:=\alpha X_0.
}
\]

则：

\[
\boxed{
X
=
\alpha t(M10^{n_3}+N)-Q_0.
}
\tag{X1}
\]

同时 exact Smith-tail relation 重构为：

\[
\boxed{
10^{m_3}H=b_3X.
}
\tag{XH}
\]

所以：

\[
\boxed{
H=\beta_3X.
}
\]

因此：

\[
\boxed{\operatorname{sgn}H=\operatorname{sgn}X.}
\]

**状态：NEW PROVED.**

---

# 19. \(X\), \(\widehat R\), \(S_3\) — Canonical Affine Identity

由：

\[
\widehat R=\alpha t10^{n_3}-v
\]

和：

\[
P_2=vM,
\]

\[
P_3=\alpha tN,
\]

计算：

\[
S_3
=
P_2+P_3-Q_0
=
vM+\alpha tN-Q_0.
\]

另一方面：

\[
M\widehat R
=
\alpha tM10^{n_3}-vM.
\]

相加：

\[
S_3+M\widehat R
=
\alpha t(M10^{n_3}+N)-Q_0
=
X.
\]

所以：

\[
\boxed{
X=S_3+M\widehat R.
}
\tag{AFF-X}
\]

即：

\[
\boxed{
S_3
=
\alpha JZ-M\widehat R.
}
\tag{AFF-Z}
\]

这是本轮认为最值得冻结的新 canonical identity。

它统一：

- generic denominator mismatch \(\widehat R\)；
- resonant sign gap \(S_3\)；
- exact defect \(H\)；
- iterated Smith quotient \(Z\)。

---

# 20. Exact Interlacing Theorem

令：

\[
A:=t10^{n_3}.
\]

则：

\[
\widehat R=\alpha A-v,
\]

\[
X_0=MA-A_3.
\]

因此：

\[
\operatorname{sgn}\widehat R
=
\operatorname{sgn}
\left(
A-\frac v\alpha
\right),
\]

\[
\operatorname{sgn}X_0
=
\operatorname{sgn}
\left(
A-\frac{A_3}{M}
\right).
\]

而：

\[
\frac v\alpha-\frac{A_3}{M}
=
\frac{S_3}{\alpha M}.
\]

因此：

## A1-DEWS-INTERLACE

\[
\boxed{
H\text{ 与 }R\text{ 异号}
}
\]

当且仅当：

\[
\boxed{
t10^{n_3}
\text{ 严格位于 }
\frac v\alpha
\text{ 与 }
\frac{A_3}{M}
\text{ 之间}.
}
\]

等价地：

\[
\boxed{
|S_3|
=
\alpha|X_0|
+
M|\widehat R|.
}
\]

再用 \(X_0=JZ\)：

\[
\boxed{
|S_3|
=
\alpha J|Z|
+
M|\widehat R|
\ge
\alpha J+M.
}
\]

**状态：NEW PROVED.**

---

# 21. Generic \(R\neq0\): Sign-Mismatch Localization

对 \(g\ge1\)：

### \(d\le-1\)

digit-length theorem：

\[
R<0.
\]

branch theorem：

\[
H<0.
\]

所以：

\[
\boxed{HR>0.}
\]

### \(d\ge2\)

\[
R>0,
\qquad
H>0.
\]

所以：

\[
\boxed{HR>0.}
\]

### \(d=1\)

\[
R>0.
\]

所以：

- minus：同号；
- plus：异号。

### \(d=0\)

两种 sign mismatch 均可能。

因此：

\[
\boxed{
HR<0
\Longrightarrow
d=0
\text{ or }
(d=1,\text{plus}).
}
\]

**状态：NEW PROVED.**

这比“outside tiny transition locus asymptotically sign-coupled”更强：它是 exact discrete theorem。

---

# 22. Transition Sign-Mismatch Absorption

若 \(HR<0\)，由：

\[
|S_3|\ge\alpha J+M
\]

得到：

\[
\boxed{
M<|S_3|,
\qquad
\alpha J<|S_3|.
}
\]

又：

\[
P_2=vM.
\]

所以：

\[
\boxed{
v>\frac{P_2}{|S_3|}.
}
\tag{ABS-v}
\]

这意味着任何 sign mismatch 都必须由：

1. **非常大的 gcd-ratio factor \(v\)**；
2. **非常小的 residual decimal modulus \(J\)**

共同吸收。

这是一种真正的 transition allocation，不只是 sign inequality。

---

# 23. \(d=1\) Plus: Stronger Absorption Theorem

\(d=1\) plus 时：

\[
R>0,
\qquad
H<0.
\]

所以：

\[
S_3<0,
\]

即：

\[
d_2>P_3.
\]

且：

\[
\boxed{
d_2-P_3
\ge
\alpha J+M.
}
\]

特别：

\[
M<d_2.
\]

因此：

\[
v=\frac{P_2}{M}
>
\frac{P_2}{d_2}.
\]

使用：

\[
P_2/Q_0>\sqrt{96/101},
\]

\[
d_2/Q_0<2.532\,10^{-2k},
\]

得：

\[
\boxed{
v
>
\frac{\sqrt{96/101}}{2.532}
10^{2k}
>
0.385\,10^{2k}.
}
\tag{D1-v}
\]

同时：

\[
\boxed{
\alpha J<d_2.
}
\]

这比此前仅有：

\[
m_3\ge2k
\]

进一步揭示了真正承担 mismatch 的 arithmetic channel。

**状态：NEW PROVED.**

---

# 24. \(d=0\) Sign-Mismatch Subchambers

## plus + \(R>0\)

同样：

\[
S_3<0,
\]

所以：

\[
\boxed{
d_2-P_3
\ge
\alpha J+M.
}
\]

从而：

\[
v>P_2/d_2>0.385\,10^{2k}.
\]

## minus + \(R<0\)

此时：

\[
S_3>0,
\]

所以：

\[
\boxed{
P_3-d_2
\ge
\alpha J+M.
}
\]

进而：

\[
v
=
P_2/M
>
\frac{P_2}{P_3-d_2}
>
\frac{P_2}{P_3}.
\]

使用 ratio window：

\[
\frac{P_2}{P_3}
>
10^{2g+k-2},
\]

得到：

\[
\boxed{
v>10^{2g+k-2}.
}
\tag{D0-v}
\]

这些都没有直接 contradiction，但把 mismatch 明确转化成 huge gcd-ratio demand。

**状态：NEW PROVED.**

---

# 25. Generic \(R\neq0\): \(\gcd(D,T_3)\) Audit

令：

\[
G_{13}:=\gcd(D,T_3).
\]

若 odd prime：

\[
p\ne2,5,
\qquad
p\mid G_{13},
\]

则：

\[
D\equiv0,
\quad
T_3\equiv0
\pmod p.
\]

所以：

\[
Q_0\equiv P_1 10^k\equiv P_3\pmod p.
\]

sphere 给：

\[
P_1^2+P_2^2\equiv0\pmod p.
\]

若：

\[
p\equiv3\pmod4,
\]

则：

\[
p\mid P_1,P_2,
\]

进而：

\[
p\mid Q_0,P_3,
\]

违反 primitive gcd。

所以：

\[
\boxed{
p\mid G_{13}^{\langle10\rangle}
\Longrightarrow
p\equiv1\pmod4.
}
\]

**状态：PROVED.**

---

# 26. Cyclotomic Restriction on the Unit Part of \(\gcd(D,T_3)\)

进一步，若 prime power：

\[
p^e\mid D,
\qquad
p^e\mid T_3,
\]

且：

\[
\gcd(p,10b_2)=1,
\]

则：

\[
\boxed{
p^e\mid 10^{2(g+k)}+1.
}
\tag{CYC}
\]

### Proof

由：

\[
D\equiv0
\]

得：

\[
P_1 10^k\equiv Q_0\pmod{p^e}.
\]

由：

\[
T_3\equiv0
\]

得：

\[
P_3\equiv Q_0\pmod{p^e}.
\]

因为 \(K_3=b_3T_3/10^{n_3}\)，且 \(p\nmid10\)：

\[
K_3\equiv0\pmod{p^e}.
\]

E3：

\[
b_2P_2
=
10^gH+K_3.
\]

又：

\[
H\equiv b_2Q_0\pmod{p^e}
\]

因为 \(D\equiv0\)。

由于 \(p\nmid b_2\)：

\[
P_2\equiv10^gQ_0\pmod{p^e}.
\]

若 \(p\mid Q_0\)，则以上同余迫使 \(p\mid P_1,P_2,P_3,Q_0\)，不可能；故 \(Q_0\) 为 unit。

代入 sphere 并约去 \(Q_0^2\)：

\[
10^{-2k}+10^{2g}+1\equiv1\pmod{p^e}.
\]

所以：

\[
10^{-2k}+10^{2g}\equiv0.
\]

乘 \(10^{2k}\)：

\[
\boxed{
1+10^{2(g+k)}\equiv0\pmod{p^e}.
}
\]

证毕。

因此 \(\gcd(D,T_3)\) 的 nondecimal、\(b_2\)-unit 部分不是自由 prime support，而被 cyclotomic integer

\[
10^{2(g+k)}+1
\]

吸收。

**状态：NEW PROVED.**

但该 cyclotomic integer 本身随 \(g+k\) 增长，所以仍不是 finite support theorem。

---

# 27. Plus Prefix Chamber

plus：

\[
0<-H<Q_0.
\]

新 strongest divisor：

\[
M_H^{(2)}
=
s\alpha\beta^\sharp v^\sharp
\mid H.
\]

所以：

\[
\boxed{
M_H^{(2)}<Q_0.
}
\]

若：

\[
M_H^{(2)}>Q_0/K,
\]

则：

\[
-H/M_H^{(2)}
\]

只有 \(K-1\) 个正整数值。

因此 Smith-rich plus 仍是 finite quotient chamber。

但存在 Smith-poor synchronized ambient families，所以无 uniform lower bound：

\[
M_H^{(2)}\gg Q_0
\]

可用。

**状态：PROVED finite-quotient reduction / FAILED uniform closure.**

---

# 28. Minus Borrow Chamber

minus：

\[
H>0,
\qquad
c=\lceil H/Q_0\rceil.
\]

对 \(g\ge1\)：

\[
1\le c\le10^d\le b_2.
\]

所以 no cross-block borrow。

## \(d=0\)

\[
\boxed{c=1.}
\]

## \(d=1\)

\[
\boxed{c\in\{1,\dots,10\}.}
\]

## \(d\ge2\)

冻结：

\[
0.08749\,10^dQ_0
<
H
<
10^dQ_0.
\]

所以：

\[
c
>
0.08749\,10^d.
\]

因此：

\[
\boxed{
\text{“minus 总有 }c=1\text{”}
}
\]

不可能作为 large-\(d\) structural theorem。

**状态：FAILED as universal conjecture.**

---

# 29. \(d=0\) Full Prefix/Suffix Overlap

\(d=0\)：

\[
m_2=g.
\]

所以：

- leading prefix block长度 = \(g\)；
- tail suffix modulus = \(10^g\)。

minus 更有：

\[
c=1,
\]

leading block 为：

\[
b_2-1.
\]

tail 使用：

\[
b_2P_2\bmod10^g.
\]

然而 exact arithmetic 中不存在 identity：

\[
b_2-1
\stackrel?=
b_2P_2\bmod10^g.
\]

二者之间仍只通过 \(H\) / Smith core 联系。

因此：

\[
\boxed{
\text{one-borrow/full-suffix overlap 本身不是 contradiction。}
}
\]

**状态：FAILED as standalone carry argument.**

---

# 30. \(d=1\) One-Extra-Digit Chamber

冻结 parallel terminal 报告：

\[
m_2=g+1.
\]

minus：

\[
c\in\{1,\dots,10\}.
\]

plus：

\[
R>0,
\]

并且：

\[
\beta_2<0.10258,
\qquad
\beta_3>0.9749,
\]

\[
m_3\ge2k.
\]

本轮加强：

\[
\boxed{
d=1,\text{ plus}
\Longrightarrow
d_2-P_3\ge\alpha J+M,
}
\]

\[
\boxed{
v>0.385\,10^{2k}.
}
\]

所以 d=1 plus 已成为：

\[
\boxed{
\text{near-denominator resonance}
+
\text{huge gcd-ratio absorption}
}
\]

chamber。

仍未 contradiction。

---

# 31. Resonant \(R=0\)

冻结：

\[
R=0
\Longrightarrow
d=0,
\]

\[
b_3=b_2 10^{n_3},
\]

\[
g_2=10^{n_3}g_3,
\]

\[
\beta_2=\beta_3,
\]

Smith：

\[
\boxed{
\alpha=1,
\quad
t=1,
\quad
v=10^{n_3},
}
\]

\[
\boxed{
b_1=su,
\quad
b_2=s\beta,
\quad
b_3=s\beta10^{n_3},
\quad
\gcd(u,\beta)=1.
}
\]

以及：

\[
\boxed{
10^gH=b_2S_3,
\qquad
S_3=P_3-d_2.
}
\tag{RES}
\]

flat elimination 给：

\[
S_3\ne0.
\]

---

# 32. Resonant Denominator Normal Form — Exact \(V,g_i\)

resonance 中：

\[
v=10^{n_3}.
\]

定义：

\[
w:=\gcd(u,10^{n_3}).
\]

由三 denominator lcm：

\[
V
=
\operatorname{lcm}(su,s\beta,s\beta10^{n_3}),
\]

\[
\gcd(u,\beta)=1,
\]

得到：

\[
\boxed{
V
=
\frac{s u\beta10^{n_3}}w.
}
\]

于是：

\[
\boxed{
g_1=\frac{\beta10^{n_3}}w,
}
\]

\[
\boxed{
g_2=\frac{u10^{n_3}}w,
}
\]

\[
\boxed{
g_3=\frac u w.
}
\]

这显式恢复：

\[
g_2=10^{n_3}g_3.
\]

并且 resonant 第三 Smith factor：

\[
\gamma=\gcd(u,10^{n_3})=w
\]

完全 \(10\)-smooth，所以：

\[
\boxed{\gamma_0=1.}
\]

**状态：NEW PROVED.**

---

# 33. Resonant \(F\)-factorization

定义：

\[
F:=2P_2P_3-P_1^2.
\]

由：

\[
P_1^2=d_2(2Q_0-d_2)-P_3^2
\]

计算：

\[
F
=
2(Q_0-d_2)P_3
-d_2(2Q_0-d_2)
+P_3^2.
\]

整理：

\[
\boxed{
F
=
(P_3-d_2)(2Q_0-d_2+P_3).
}
\]

即：

\[
\boxed{
F
=
S_3(Q_0+P_2+P_3).
}
\tag{Ffac}
\]

所以：

\[
\operatorname{sgn}F
=
\operatorname{sgn}S_3
=
\operatorname{sgn}H.
\]

**状态：PROVED.**

---

# 34. FAILED — \(F\) 提供独立 resonant valuation obstruction

resonance 已有：

\[
10^gH=b_2S_3.
\]

而：

\[
F=S_3(Q_0+P_2+P_3).
\]

所以任何：

\[
10^g\mid b_2F
\]

型结论只是把已知的 \(S_3\)-divisibility 乘上一个大因子。

因此：

\[
\boxed{
F\text{ 不提供 independent decimal depth。}
}
\]

**状态：FAILED AS INDEPENDENT ROUTE.**

---

# 35. Boundary \(S_3=0\) Audit

若：

\[
S_3=0,
\]

则：

\[
P_3=d_2,
\]

\[
F=0,
\]

\[
P_1^2=2P_2P_3.
\]

这个 primitive boundary 本身并非 sphere 上的稀有孤点。

例如：

\[
\boxed{
(P_1,P_2,P_3,Q_0)
=
(2ab,a^2,2b^2,a^2+2b^2)
}
\]

在：

\[
\gcd(a,b)=1,
\qquad a\text{ odd}
\]

的适当 primitive 子族中给无限 boundary sphere points。

对称地：

\[
\boxed{
(P_1,P_2,P_3,Q_0)
=
(2ab,2a^2,b^2,2a^2+b^2)
}
\]

也给无限 boundary family。

所以：

\[
\boxed{
\text{pure primitive square/product spacing 不能排除 }S_3\approx0.
}
\]

resonance 中真正排除 \(S_3=0\) 的只是：

\[
H\ne0
\]

和：

\[
10^gH=b_2S_3.
\]

**状态：NEW COUNTEREXAMPLE / FAILED SPACING ROUTE.**

---

# 36. Resonant Complementary \(2\)-Adic Allocation

这是本轮对 resonance 的新 exact local theorem。

令：

\[
\beta_0:=\beta^{\langle10\rangle},
\qquad
\beta=\delta\beta_0,
\]

其中 \(\delta\) 只含 \(2,5\)。

因为：

\[
\beta_0\mid Q_0,
\qquad
\beta_0\mid D,
\]

写：

\[
Q_0=\beta_0Q_1,
\qquad
D=\beta_0D_0.
\]

由于 \(Q_0\) odd：

\[
Q_1\text{ odd}.
\]

又：

\[
D=P_110^k-Q_0,
\qquad
k\ge1,
\]

所以：

\[
D\text{ odd},
\qquad
D_0\text{ odd}.
\]

resonance：

\[
H
=
s\beta_0
\left(
\delta Q_1-u10^gD_0
\right).
\]

定义：

\[
H_0:=\delta Q_1-u10^gD_0.
\]

而：

\[
10^gH=b_2S_3=s\beta_0\delta S_3
\]

给：

\[
\boxed{
10^gH_0=\delta S_3.
}
\tag{RES-2}
\]

令：

\[
a:=v_2(\beta)=v_2(\delta).
\]

由于 \(g\ge1\) in resonance：

### Case 1: \(a<g\)

两项 valuation 不同：

\[
v_2(\delta Q_1)=a,
\]

\[
v_2(u10^gD_0)\ge g.
\]

所以：

\[
v_2(H_0)=a.
\]

代入 (RES-2)：

\[
\boxed{
v_2(S_3)=g.
}
\]

### Case 2: \(a=g\)

若 \(a>0\)，\(\gcd(u,\beta)=1\) 给 \(u\) odd。

括号内两项除去 \(2^g\) 后均为 odd，因此相减为 even：

\[
v_2(H_0)\ge g+1.
\]

所以：

\[
\boxed{
v_2(S_3)\ge g+1.
}
\]

### Case 3: \(a>g\)

此时 \(u\) odd，第二项 valuation 恰为 \(g\)，故：

\[
v_2(H_0)=g.
\]

于是：

\[
\boxed{
v_2(S_3)=2g-a.
}
\]

因此必须：

\[
\boxed{a\le2g.}
\]

若：

\[
a>2g,
\]

直接 contradiction。

总结：

\[
\boxed{
\begin{array}{c|c}
a=v_2(\beta)&v_2(S_3)\\
\hline
a<g&g\\
a=g&\ge g+1\\
g<a\le2g&2g-a\\
a>2g&\text{impossible}
\end{array}
}
\tag{RES-2ADIC}
\]

**状态：NEW PROVED.**

这是真正比“\(10^g/\gcd(10^g,\delta_\beta)\mid S_3\)”更精细的 complementary allocation。

但它仍未关闭全部 resonance。

---

# 37. Resonant Status

已有：

- \(d=0\)；
- explicit denominator normal form；
- \(10^{n_3}\mid P_2\)；
- \(S_3\ne0\)；
- residual decimal divisor；
- sign strip；
- full \(F\)-factorization；
- new \(2\)-adic trichotomy。

但目前仍不能推出：

\[
R=0\Longrightarrow\bot.
\]

特别：

- \(\beta\) 的 \(2\)-adic exponent可以落在允许区间；
- \(S_3\) 的大小与 required decimal divisor仍可相容；
- pure primitive boundary spacing不工作；
- common-\(U\) gate 尚未被上述 local equations自动读取。

所以：

\[
\boxed{R=0\text{ OPEN}.}
\]

---

# 38. Long-Division Dynamics

定义：

\[
r_j
=
10^j b_1D
-
Q_0
\left\lfloor
\frac{10^j b_1D}{Q_0}
\right\rfloor.
\]

则：

\[
r_{j+1}\equiv10r_j\pmod{Q_0}.
\]

在：

\[
j=m_2
\]

处：

plus：

\[
\boxed{r_{m_2}=-H.}
\]

minus：

\[
\boxed{r_{m_2}=cQ_0-H.}
\]

继续 \(g\) 位：

\[
r_{m_2+g}
\equiv
10^g r_{m_2}
\pmod{Q_0}.
\]

利用 E3 可将其改写成 \(K_3-b_2P_2\) 的模 \(Q_0\) 形式。

**状态：PROVED.**

但这只是 E3 的 remainder repackaging；状态 \(r_j\) 仍在：

\[
\{0,\dots,Q_0-1\}
\]

中移动，没有压成一个与 \(Q_0\) 无关的小 finite automaton。

因此：

\[
\boxed{
\text{finite carry automaton / no-cycle theorem}
}
\]

目前没有成立。

**状态：FAILED AS STANDALONE FINITE-STATE CLOSURE.**

---

# 39. Prefix/Suffix Overlap Verdict

double word synchronization 的 exact content现在可写成：

\[
\boxed{
\text{leading Euclidean defect }H
}
\]

经第一层 Smith deflation：

\[
H
\to q_H,
\]

再经第二层 tail Smith deflation：

\[
q_H\to Z,
\]

最终 tail word为：

\[
\boxed{
tM10^{n_3}-A_3=JZ.
}
\]

因此真正共享的不是简单的某段 digit word，而是：

\[
\boxed{
\text{同一个 primitive integer }Z
}
\]

同时控制：

- leading defect quotient；
- tail denominator residual；
- affine sign gap。

这是本轮对 “Double Euclidean Word Synchronization” 最精确的新解释。

---

# 40. Backward Lemmas Used

本轮没有重新运行 backward campaign。

仅使用其已审计架构结论：

\[
\boxed{
\text{backward terminal arithmetic 对 common radial scale }U\text{ 齐次/等变}.
}
\]

所以：

- WGF；
- normalized \(Z_\pm\)；
- \(2/5\)-phase；
- same-cut norm feedback；

不能被假定为独立 common-\(U\) gate。

本文新增证明全部在 forward exact terminal coordinates 中完成。

**状态：PROVENANCE ONLY.**

---

# 41. Computational Experiments / Regression Checks

计算只用于 sanity check，不用于 nonexistence proof。

使用已有 synchronized ambient profile：

\[
(b_1,b_2,b_3)=(1,6,8),
\]

\[
V=24,
\qquad
(g_1,g_2,g_3)=(24,4,3),
\]

\[
(m_2,n_3,m_3,k,g)=(1,1,1,1,0).
\]

其 Smith：

\[
s=1,
\quad
\alpha=1,
\quad
\beta=2,
\quad
u=1,
\quad
t=3,
\quad
v=4.
\]

所以：

\[
\widehat R
=
3\cdot10-4
=
26,
\]

\[
R=2\cdot26=52.
\]

并且：

\[
\delta_\beta=2,
\quad
\beta^\sharp=1,
\quad
\Lambda_\beta=5,
\]

\[
\delta_v=1,
\quad
v^\sharp=4,
\quad
J=5.
\]

三个已知 synchronized states：

### State A

\[
(P_1,P_2,P_3,Q_0)
=
(24,52,159,169).
\]

\[
D=71,
\quad
H=304,
\quad
c=2,
\]

\[
d_2=117,
\quad
S_3=42.
\]

\[
M=P_2/v=13.
\]

\[
X_0=380=5\cdot76.
\]

\[
Z=76.
\]

\[
H=4Z=304.
\]

### State B

\[
(P_1,P_2,P_3,Q_0)
=
(48,436,75,445).
\]

\[
D=35,
\quad
H=2320,
\quad
c=6,
\]

\[
M=109,
\]

\[
X_0=2900=5\cdot580,
\]

\[
Z=580,
\quad
H=4Z.
\]

### State C

\[
(P_1,P_2,P_3,Q_0)
=
(456,292,2907,2957).
\]

\[
D=1603,
\quad
H=1712,
\quad
c=1,
\]

\[
M=73,
\]

\[
X_0=2140=5\cdot428,
\]

\[
Z=428,
\quad
H=4Z.
\]

所有新 identities 均精确通过。

这些 states 最终仍死于 common-\(U\) gate。

因此它们严格说明：

\[
\boxed{
\text{generic }R\ne0
+
\text{DES}
+
\text{Smith}
}
\]

在不使用 radial gate 时并不自动矛盾。

**状态：EXPERIMENTAL REGRESSION / STRUCTURAL COUNTEREVIDENCE.**

---

# 42. Counterexamples / Failed Conjectures Ledger

## FAILED 1

\[
R\ne0
\Longrightarrow
\operatorname{sgn}H=\operatorname{sgn}R
\]

全局不成立。

正确 theorem：

\[
HR<0
\]

只可能落在：

\[
d=0
\]

或：

\[
d=1,\text{ plus}.
\]

---

## FAILED 2

\[
S_0\ne0
\Longrightarrow
\text{useful new odd prime}.
\]

错误；\(\widehat R=\pm1\) / pure \(2,5\)-smooth 可发生。

---

## FAILED 3

\[
10^{n_3}\mid R T_3
\]

是新的 decimal depth。

错误；它与 \(K_3\) integrality 等价携带相同 depth。

---

## FAILED 4

\[
\text{minus}\Longrightarrow c=1.
\]

作为 structural theorem错误；large \(d\) 时 \(c\) 必为 \(10^d\)-scale，且 synchronized ambient states已有 \(c=2,6\)。

---

## FAILED 5

\[
F=2P_2P_3-P_1^2
\]

提供新的 resonant divisor。

错误；\(F=S_3(Q_0+P_2+P_3)\)，只是旧 \(S_3\) 的乘积重写。

---

## FAILED 6

\[
S_3=0
\]

在 primitive sphere 上本身稀有/不可能。

错误；存在无限 primitive boundary families。

---

## FAILED 7

\[
\Sigma_b
\]

必随 \(Q_0\) 增长。

没有 theorem；\(\Sigma_b=1\) 完全可能。

---

## FAILED 8

\[
\text{long-division dynamics}
\]

自动给 fixed finite-state no-cycle theorem。

当前 remainder state 仍是 \(Q_0\)-sized。

---

## FAILED 9

\[
\text{exact-word + Smith alone closes }A_1.
\]

已被 common-\(U\)-dead synchronized infinite family否定。

---

# 43. New Proven Lemmas Ledger

### A1-DEWS-1 — Primitive Denominator Residual

\[
R=s\beta\widehat R,
\qquad
\widehat R=\alpha t10^{n_3}-v.
\]

**PROVED.**

### A1-DEWS-2 — Residual Coprimality

\[
\gcd(\widehat R,\alpha t)=1,
\]

\[
\gcd(\widehat R,v)=\gcd(10^{n_3},v),
\]

\[
\gcd(\widehat R,\alpha tv)^{\langle10\rangle}=1.
\]

**PROVED.**

### A1-DEWS-3 — HR2

\[
10^{m_3}H
=
R(Q_0-P_3)
+
b_2 10^{n_3}(P_3-d_2).
\]

**PROVED.**

### A1-DEWS-4 — DIV-R Redundancy

\[
\gcd(R,10^{n_3})
=
\gcd(b_3,10^{n_3}).
\]

**PROVED.**

### A1-DEWS-5 — Third Smith Factor

\[
\gamma=\gcd(u,v)=\gcd(b_1,b_3)/s.
\]

**PROVED.**

### A1-DEWS-6 — Full Smith LCM

\[
V=s\alpha\beta\gamma u_0tv_0
\]

for \(u=\gamma u_0,v=\gamma v_0\).

**PROVED.**

### A1-DEWS-7 — Full Smith Hypotenuse Allocation

\[
\Sigma_b
=
\alpha\beta^{\langle10\rangle}\gamma^{\langle10\rangle}
\mid Q_0.
\]

**PROVED.**

### A1-DEWS-8 — Full Smith Defect Allocation

\[
s\Sigma_b\mid H.
\]

**PROVED.**

### A1-DEWS-9 — Iterated Smith Deflation

\[
q_H=v^\sharp Z,
\qquad
X_0=JZ.
\]

**PROVED.**

### A1-DEWS-10 — Strong Defect Divisor

\[
s\alpha\beta^\sharp v^\sharp\mid H.
\]

**PROVED.**

### A1-DEWS-11 — Balanced Divisor Pair

\[
\frac{\alpha J}{s\alpha\beta^\sharp v^\sharp}
=
\frac1{\beta_3}.
\]

**PROVED.**

### A1-DEWS-12 — Affine Terminal Identity

\[
S_3=\alpha JZ-M\widehat R.
\]

**PROVED.**

### A1-DEWS-13 — Sign Interlacing

If \(HR<0\),

\[
|S_3|
=
\alpha J|Z|+M|\widehat R|
\ge\alpha J+M.
\]

**PROVED.**

### A1-DEWS-14 — Exact Sign-Mismatch Localization

For \(g\ge1\),

\[
HR<0
\Longrightarrow
d=0
\text{ or }
(d=1,\text{plus}).
\]

**PROVED.**

### A1-DEWS-15 — \(d=1\) Plus GCD-Ratio Absorption

\[
v>0.385\,10^{2k}.
\]

**PROVED.**

### A1-DEWS-16 — Cyclotomic Common-Gap Restriction

If

\[
p^e\mid D,\quad
p^e\mid T_3,\quad
\gcd(p,10b_2)=1,
\]

then:

\[
p^e\mid10^{2(g+k)}+1.
\]

**PROVED.**

### A1-DEWS-17 — Resonant \(2\)-Adic Trichotomy

For \(a=v_2(\beta)\):

\[
a<g\Rightarrow v_2(S_3)=g,
\]

\[
a=g\Rightarrow v_2(S_3)\ge g+1,
\]

\[
g<a\le2g\Rightarrow v_2(S_3)=2g-a,
\]

\[
a>2g\Rightarrow\bot.
\]

**PROVED.**

---

# 44. Generic Branch Status

\[
\boxed{R\ne0\text{ remains OPEN}.}
\]

但 generic branch 不再是 free \(R\) problem。

它被压成：

\[
\boxed{
\widehat R=\alpha t10^{n_3}-v\ne0,
}
\]

\[
\boxed{
S_3=\alpha JZ-M\widehat R,
}
\]

\[
\boxed{
H=s\alpha\beta^\sharp v^\sharp Z,
}
\]

\[
\boxed{
\Sigma_b\mid Q_0.
}
\]

此外：

- outer \(d\)-half-lines自动 \(H,R\) 同号；
- sign mismatch只在 transition；
- mismatch强迫 huge \(v\)；
- common gap unit part受 cyclotomic restriction。

所以 generic frontier 已比第六轮明显更离散。

但 synchronized \(g=0\) ambient survivors证明：这些 exact-word + Smith conditions本身还不能杀 generic。

---

# 45. Resonant Branch Status

\[
\boxed{R=0\text{ remains OPEN}.}
\]

最新 normal form：

\[
\alpha=t=1,
\qquad
v=10^{n_3},
\qquad
d=0,
\]

\[
10^gH=b_2S_3,
\]

\[
S_3\ne0.
\]

新增：

- exact \(V,g_i\) parametrization；
- third Smith factor ten-free part消失；
- \(F\)-factorization被判定 redundant；
- primitive boundary spacing被 infinite family否定；
- resonant \(2\)-adic trichotomy。

仍缺：

\[
\boxed{
\text{decimal depth of }S_3
+
\text{common-}U\text{ radial gate}
\Longrightarrow\bot.
}
\]

---

# 46. Plus / Minus Status

## Plus

\[
H<0,
\qquad
-H<Q_0.
\]

Smith-rich 时 finite quotient。

对 \(g\ge1\)：

\[
d\le1.
\]

\(d\le-1\) 自动与 \(R\) 同号。

\(d=1\) plus 是唯一非zero-\(d\) sign-mismatch chamber，且满足：

\[
v>0.385\,10^{2k}.
\]

## Minus

\[
H>0.
\]

对 \(g\ge1\)：

\[
d\ge0.
\]

\(d=0\)：one borrow。

\(d=1\)：十个 carry states。

\(d\ge2\)：\(H,c\) 都为 \(10^dQ_0\)/\(10^d\) scale。

outer \(d\ge2\) 自动与 \(R\) 同号。

---

# 47. Status of \(g\)

仍没有：

\[
\boxed{g\le G}
\]

absolute theorem。

已有：

\[
10^{2g+k-2}<Q_0,
\]

只能给：

\[
g=O(\log Q_0).
\]

本轮没有伪造 absolute \(g\)-bound。

---

# 48. \(g=0\) Audit

\(g=0\) 时：

\[
m_2=d\ge1.
\]

resonance：

\[
R=0\Rightarrow d=0
\]

与 \(m_2\ge1\) 冲突，所以：

\[
\boxed{
g=0\Longrightarrow R\ne0.
}
\]

但 known synchronized ambient family恰好位于 \(g=0,R\ne0\)，并满足 Double Smith core，却死于 common-\(U\)。

因此：

\[
\boxed{
g=0\text{ 是最明确证明 radial gate仍不可删除的 chamber。}
}
\]

full A1 的 \(g=0\) minus 仍 OPEN。

---

# 49. Why Backward Same-Cut Machinery Does Not Close This

最新 backward common-\(U\) pullback audit 已证明：

\[
\boxed{
\text{WGF / phase / normalized gap arithmetic 对 }U\text{ radially equivariant}.
}
\]

因此本轮即使把 exact words 压到 \(Z\)，也不能期待 backward phase 自动提供：

\[
M\mid U
\]

或新 successor obstruction。

所以：

\[
\boxed{
\text{下一步必须把 }Z,J,v^\sharp,\Sigma_b
\text{ 接到 actual common-}U\text{ interval/successor。}
}
\]

这不是回到旧大框架，而是当前 exact terminal state 唯一尚未利用的 semantic gate。

---

# 50. Exact Remaining Terminal Chamber

本轮建议把 surviving state改写为：

\[
\boxed{
\mathcal T_{\rm DEWS}
=
(
P_1,P_2,P_3,Q_0;
g,k,d,n_3;
s,\alpha,\beta,\gamma,t;
J,v^\sharp,Z;
U,V
).
}
\]

但真正 independent terminal equations只有：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

\[
D=P_1 10^k-Q_0>0,
\]

\[
\Sigma_b\mid Q_0,
\]

\[
H=s\alpha\beta^\sharp v^\sharp Z,
\]

\[
X_0=JZ,
\]

\[
S_3=\alpha JZ-M\widehat R,
\]

\[
\widehat R=\alpha t10^{n_3}-v,
\]

以及 common radial gate：

\[
\boxed{
\operatorname{next}_V(L_{23})<R_{23}.
}
\]

这已经是一个比第六轮更小、更硬的 terminal chamber。

---

# 51. Exact Next Theorem

本轮没有 closure，所以给出一个尽可能单一的下一 theorem。

## A1-ISR — Iterated-Smith Coprime-Radial Exclusion

对任意满足：

1. primitive sphere；
2. A1 exponent normal form；
3. exact leading/tail Euclidean system；
4. full three-pair Smith chart；
5. iterated Smith core
   \[
   q_H=v^\sharp Z,
   \qquad
   X_0=JZ;
   \]
6. full Smith determinant allocation
   \[
   \Sigma_b\mid Q_0;
   \]
7. all digit-length / sign constraints；

的 synchronized primitive state，证明其 common numerator-scale interval

\[
I_{23}=[L_{23},R_{23})
\]

不含与 \(V\) 互素的正整数：

\[
\boxed{
\operatorname{next}_V(L_{23})\ge R_{23}.
}
\tag{A1-ISR}
\]

若 A1-ISR 成立，则：

\[
\boxed{A_1=\varnothing.}
\]

再结合 DD closure：

\[
\boxed{\text{Strict Layer closed}.}
\]

---

# 52. Recommended Next Step

只建议三条，而且按优先级排序。

## Target 1 — \(J,v^\sharp\) × common-\(U\) successor

当前最值得追的是：

\[
\boxed{
JZ=tM10^{n_3}-A_3
}
\]

如何限制：

\[
C_2=P_2/g_2,
\qquad
C_3=P_3/g_3
\]

的 common-\(U\) interval。

这是新 core 与唯一剩余 semantic gate 的直接接口。

## Target 2 — Transition sign-mismatch absorption

专攻：

\[
d=0,\ HR<0,
\]

和：

\[
d=1,\text{ plus}.
\]

这里已经有：

\[
|S_3|\ge\alpha J+M,
\]

\[
v>P_2/|S_3|.
\]

最可能继续升级成 radial interval emptiness。

## Target 3 — Resonant \(2\)-adic law × radial interval

在 \(R=0\) 中联立：

\[
10^{n_3}\mid P_2,
\]

\[
v_2(S_3)
\]

的 exact trichotomy，以及 numerator interval。

不要再单独追 \(F\)、generic \(5\)-phase 或 primitive square-spacing。

---

# 53. Final Research Verdict

本轮没有做到理想的：

\[
\boxed{
R\ne0\Rightarrow\bot,
\qquad
R=0\Rightarrow\bot.
}
\]

因此不能宣称 A1 closure。

但本轮确实把第六轮的：

\[
\boxed{
H\times R\times\text{prefix/suffix}\times(\alpha,\beta)
}
\]

进一步压成：

\[
\boxed{
\widehat R
\times
Z
\times
(J,v^\sharp)
\times
(\alpha,\beta,\gamma)
\times
S_3
}
\]

的 exact ordinary-integer system。

最核心的新 chain 是：

\[
\boxed{
\begin{aligned}
R&=s\beta\widehat R,\\
H&=s\alpha\beta^\sharp v^\sharp Z,\\
X_0&=JZ,\\
S_3&=\alpha JZ-M\widehat R,\\
\Sigma_b&=\alpha\beta_0\gamma_0\mid Q_0.
\end{aligned}
}
\]

而且：

\[
\boxed{
HR<0
\Longrightarrow
|S_3|\ge\alpha J+M.
}
\]

所以“double Euclidean synchronization”现在已经不再只是 prefix / suffix 两个 word facts，而是一个真正的：

\[
\boxed{
\textbf{iterated Smith factorization of the same integer defect}.
}
\]

本轮最重要的 architecture correction 也是明确的：

\[
\boxed{
\textbf{exact-word + Smith 本身仍不足；}
}
\]

但不是因为它们还太“近似”，而是因为已有 synchronized ambient family证明：

\[
\boxed{
\textbf{最后缺的确实是 common coprime radial realization。}
}
\]

因此第八轮若继续正向，不应该再开一个新的 word obstruction；应该直接研究：

\[
\boxed{
\textbf{Double Smith–Euclidean Core}
\times
\textbf{Coprime Radial Successor}.
}
\]

这已经是当前最窄、最可审计、最接近 A1 closure 的 terminal frontier。
