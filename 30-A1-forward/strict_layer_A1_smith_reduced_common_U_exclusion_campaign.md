# A1 Smith-Reduced Common-U Exclusion Campaign

**文件名：** `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`  
**研究范围：** 三项十进制拼接平方和问题，Strict Layer — `A1-only`  
**直接 campaign 输入：** 用户本轮 A1-SRCU 任务书 fileciteturn9file13  
**最新 exact-word source of truth：** `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md` fileciteturn13file1  
**common-\(U\) semantics source of truth：** `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md` fileciteturn12file16  
**统一 moving/radial source：** `strict_layer_A1_unified_moving_profile_terminal_campaign.md` fileciteturn10file13  
**backward radial redundancy source：** `strict_layer_backward_A1_common_U_pullback_primitive_radial_gluing_campaign.md` fileciteturn11file14

---

# 1. Executive Summary

本轮正式执行：

\[
\boxed{
\textbf{Double Smith--Euclidean exact word}
\times
\textbf{common coprime radial realization}
}
\]

而不是继续追加新的 standalone word congruence。

本轮**没有**证明：

\[
A_1=\varnothing,
\]

因此：

\[
\boxed{
\textbf{Strict Layer 尚未 CLOSED.}
}
\]

但是，本轮完成了 A1-SRCU 所要求的关键接口审计，并把 common-\(U\) frontier 比 prompt 中预想的 \((\rho,\tau,\sigma)\) 图景进一步降了一维。

最重要的新结果不是某个更大的 \(H\)-divisor，而是：

## A1-SRCU-CORE — Full Smith–Radial Cancellation

在最新 full Smith 坐标中，可写

\[
\boxed{
 g_2=u_0v,
 \qquad
 g_3=u_0\alpha t,
}
\]

以及

\[
\boxed{
P_2=vM,
\qquad
P_3=\alpha tN.
}
\]

于是自动：

\[
\boxed{
C_2=\frac{M}{u_0},
\qquad
C_3=\frac{N}{u_0}.
}
\tag{SRCU-C}
\]

这使原 common-\(U\) interval 精确化为：

\[
\boxed{
I_{23}
=
 u_0
\left[
\max\left(\frac{10^{n_2-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{n_2}}M,\frac{10^{n_3}}N\right)
\right).
}
\tag{SRCU-I}
\]

更关键地，合法 \(U\) 满足：

\[
\boxed{
\gcd(U,V)=1,
\qquad
V=s\beta u_0v\alpha t.
}
\tag{SRCU-V}
\]

因此若令

\[
y:=\frac U{u_0},
\]

则 common-\(U\) 的 radial semantic 被精确拆成：

\[
\boxed{
\textbf{prescribed-denominator reduced fraction }U/u_0
}
\]

加上：

\[
\boxed{
\textbf{transverse unit sieve modulo }s\beta v\alpha t.
}
\]

也就是说，Smith factors \(v\) 与 \(\alpha t\) 在 projective/radial endpoints 中**完全抵消**；它们不控制 interval geometry，而只通过 \(V\)-coprimality 留在 unit sieve 中。

这对本轮策略有决定性影响：

> prompt 中“用 \(R\)-sign / \(\sigma\) 直接把 \(\rho\) 推到 \(0.1\) 或 \(10\) 边界”的候选机制，在完整 Smith reduction 后并不存在。

这不是一个弱反例，而是 exact algebraic cancellation。

本轮还严格证明：

1. A1 Radial Normal Form；
2. \(\rho,\tau,\sigma\) bridge 全部成立；
3. prompt 候选
   \[
   B_3^\sharp\mid H
   \]
   **成立**；
4. 但 \(B_3^\sharp\) 已被最新 iterated-Smith divisor 吸收，并非新的 independent strengthening；
5. 找到当前 strongest proved defect divisor
   \[
   \boxed{\mathcal M_{\max}=s\alpha\beta^\sharp v^\sharp h_T^\sharp\mid H};
   \]
6. 证明 Smith/GCD exact duality
   \[
   \boxed{
   \gcd(b_i,b_j)\operatorname{lcm}(g_i,g_j)=V;
   }
   \]
7. 推导 fixed-\(q\) exact affine radial equation；
8. resonance 被重写为 prescribed-denominator reduced-fraction unit problem，但没有关闭；
9. \(d=0,1\) 中原先基于 \(\sigma\) 的 radial-boundary route 被 exact cancellation 判定为 standalone 失败；
10. 已知 \(g=0\) synchronized pseudo-family 在新 radial coordinates 中直接死于 Layer C，另一个 exact real-cone point死于 Layer I。

因此，本轮后真正最小的 global frontier 已不再是原始 A1-SRCU 的 \(\operatorname{next}_V(L_{23})\) 形式，而是：

## A1-SRUS — Smith-Reduced Unit-Successor Exclusion

证明不存在 exact A1 Smith state 与正整数 \(U\)，使

\[
\boxed{
\frac U{u_0}
\in
K_{MN}
}
\]

且

\[
\boxed{
\gcd(U,s\beta u_0v\alpha t)=1,
}
\]

其中

\[
\boxed{
K_{MN}
:=
\left[
\max\left(\frac{10^{n_2-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{n_2}}M,\frac{10^{n_3}}N\right)
\right).
}
\tag{SRUS}
\]

这与 A1-SRCU 完全等价，但 arithmetic dimension 更低。

---

# 2. Frozen Strict-Layer State

DD 已关闭，且 Strict Layer 的剩余 frontier 为 A1-only。最新严格层 consolidations 将 A1 作为唯一剩余 chamber；本轮不重新讨论 DD。  

冻结：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

令：

\[
 g=m_3-n_3\ge0,
\qquad
 k\ge1,
\qquad
 d=m_2-g.
\]

于是：

\[
\boxed{
 m_2=g+d,
\quad
 n_2=2g+k+d,
\quad
 m_3=n_3+g.
}
\tag{EXP}
\]

primitive/common-denominator normalization：

\[
 g_i=\gcd(V,P_i),
\qquad
 C_i=P_i/g_i,
\]

\[
 a_i=UC_i,
\qquad
 b_i=V/g_i,
\qquad
\gcd(U,V)=1.
\]

forward reconstruction theorem 已证明：只要 synchronized primitive state、common-\(V\) gcd profile、denominator digits 与合法 coprime common integer \(U\) 同时成立，就能重建 original candidate。 fileciteturn12file10

因此 common-\(U\) 不是辅助条件，而是 terminal semantic gate。

---

# 3. Frozen Exact Word Core

定义：

\[
\boxed{D=P_110^k-Q_0>0},
\]

\[
\boxed{H=b_2Q_0-b_110^{m_2}D\ne0},
\]

\[
Q_{12}=b_110^{m_2}+b_2,
\]

\[
\boxed{
 b_1P_110^{m_2+k}=Q_0Q_{12}-H.
}
\tag{E1}
\]

第三尾：

\[
K_3=rac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbf Z_{>0},
\]

\[
\boxed{
 b_2P_2=10^gH+K_3.
}
\tag{E3}
\]

sign convention：

\[
\boxed{\text{plus}\iff H<0},
\qquad
\boxed{\text{minus}\iff H>0}.
\]

最新 report 已严格保留 \(H\ne0\)。

---

# 4. Frozen Double Euclidean Synchronization

prefix：

\[
c_{\rm pref}=\left\lceil\frac H{Q_0}\right\rceil,
\]

\[
q_{\rm pref}=Q_{12}-c_{\rm pref},
\]

\[
r_{\rm pref}=c_{\rm pref}Q_0-H,
\qquad 0\le r_{\rm pref}<Q_0.
\]

plus：

\[
-Q_0<H<0,
\qquad c_{\rm pref}=0.
\]

minus：

\[
1\le c\le10^d.
\]

若 \(g\ge1\)，Borrow Propagation Theorem 给：

\[
\boxed{c\le b_2}.
\]

因此 borrow 不跨 \(b_2\)-block。 fileciteturn11file16

tail：

\[
b_2P_2=10^gq_2+r,
\]

\[
K_3=10^gq_3+r,
\]

\[
\boxed{q_2-q_3=H}.
\]

---

# 5. Frozen Branch Map

对 \(g\ge1\)：

\[
\boxed{d\le-1\Longrightarrow\text{plus}},
\]

\[
\boxed{d=0,1\Longrightarrow\text{dual-sign transition}},
\]

\[
\boxed{d\ge2\Longrightarrow\text{minus}}.
\]

其中 \(d=-1\) minus 已闭合。 fileciteturn10file6

---

# 6. Latest Full Smith Chart

最新 exact-word/Smith source 已把三 pair gcd 全部完成。 fileciteturn12file15

写：

\[
\boxed{
 b_1=s\alpha u,
\quad
 b_2=s\alpha\beta t,
\quad
 b_3=s\beta v.
}
\tag{SMITH}
\]

并有：

\[
\gcd(\alpha,\beta)=1,
\]

\[
\gcd(u,\beta t)=1,
\qquad
\gcd(\alpha t,v)=1.
\]

第三 Smith factor：

\[
\gamma=\gcd(u,v).
\]

写：

\[
 u=\gamma u_0,
\qquad
 v=\gamma v_0,
\qquad
\gcd(u_0,v_0)=1.
\]

Full Smith LCM：

\[
\boxed{
V=s\alpha\beta\gamma u_0tv_0.
}
\tag{LCM}
\]

最新 report 还证明：

\[
\Sigma_b
=
\alpha\beta^{\langle10\rangle}\gamma^{\langle10\rangle}
\mid Q_0,
\]

以及：

\[
s\Sigma_b\mid H.
\]

但 \(\Sigma_b\) 可等于 1，不能单独 closure。 fileciteturn10file14

---

# 7. NEW PROVED — Exact Smith GCD Profile

由 \(g_i=V/b_i\) 与 (SMITH)、(LCM)：

\[
g_1
=\frac{V}{s\alpha u}
=\beta tv_0,
\]

\[
g_2
=\frac{V}{s\alpha\beta t}
=\gamma u_0v_0
=u_0v,
\]

\[
g_3
=\frac{V}{s\beta v}
=\alpha u_0t.
\]

因此：

\[
\boxed{
 g_2=u_0v,
\qquad
 g_3=u_0\alpha t.
}
\tag{G23}
\]

由 \(\gcd(v,\alpha t)=1\)：

\[
\boxed{
\gcd(g_2,g_3)=u_0.
}
\tag{U0}
\]

**状态：NEW DERIVED / EXACT.**

---

# 8. NEW PROVED — Primitive Coordinate Allocation

最新 Double-Smith tail reduction已有：

\[
\boxed{P_2=vM}
\]

for some \(M\in\mathbf Z_{>0}\). fileciteturn13file14

同时 \(\alpha\mid Q_0-P_3\) 与 full gcd ratio可将 third coordinate写成：

\[
\boxed{P_3=\alpha tN}
\]

for some \(N\in\mathbf Z_{>0}\).

由于 \(g_2\mid P_2\)：

\[
u_0v\mid vM,
\]

于是直接约去正整数 \(v\)：

\[
\boxed{u_0\mid M}.
\]

同理：

\[
\alpha u_0t\mid\alpha tN
\Longrightarrow
\boxed{u_0\mid N}.
\]

于是：

\[
\boxed{
C_2=\frac{P_2}{g_2}=\frac{M}{u_0},
}
\]

\[
\boxed{
C_3=\frac{P_3}{g_3}=\frac{N}{u_0}.
}
\tag{C23}
\]

这就是本轮最重要的 Smith–radial cancellation 入口。

---

# 9. A1 Radial Normal Form

定义：

\[
\boxed{
\tau:=\frac{10^{n_3}}{C_3},
}
\]

\[
\boxed{
\rho:=
\frac{C_2 10^{n_3}}{C_3 10^{n_2}}.
}
\]

则：

\[
\frac{10^{n_2}}{C_2}
=
\frac{10^{n_3}}{C_3}\cdot\frac1\rho
=
\frac\tau\rho.
\]

所以：

\[
I_3
=
\left[\frac\tau{10},\tau\right),
\]

\[
I_2
=
\left[\frac\tau{10\rho},\frac\tau\rho\right).
\]

故：

\[
\boxed{
I_{23}
=
\tau J(\rho),
}
\]

其中：

\[
\boxed{
J(\rho)
=
\left[
\max\left(\frac1{10},\frac1{10\rho}\right),
\min\left(1,\frac1\rho\right)
\right).
}
\tag{RNF}
\]

**状态：NEW PROVED.**

---

# 10. Continuous Feasibility

\(J(\rho)\ne\varnothing\) iff：

\[
\max\left(\frac1{10},\frac1{10\rho}\right)
<
\min\left(1,\frac1\rho\right).
\]

分 \(\rho\le1\) 与 \(\rho\ge1\) 即得：

\[
\boxed{
0.1<\rho<10.
}
\tag{CONE}
\]

endpoint 为 strict，因为两个原区间 upper endpoint 均为 open。

**状态：NEW PROVED / EQUIVALENT.**

---

# 11. Exact Radial Width

令：

\[
W:=R_{23}-L_{23}.
\]

若：

\[
0.1<\rho\le1,
\]

则：

\[
J(\rho)=\left[\frac1{10\rho},1\right),
\]

所以：

\[
\boxed{
W
=
\tau\left(1-\frac1{10\rho}\right).
}
\tag{W-}
\]

若：

\[
1\le\rho<10,
\]

则：

\[
J(\rho)=\left[\frac1{10},\frac1\rho\right),
\]

所以：

\[
\boxed{
W
=
\tau\left(\frac1\rho-\frac1{10}\right).
}
\tag{W+}
\]

在 \(\rho=1\) 两式一致：\(W=0.9\tau\)。

**状态：NEW PROVED.**

---

# 12. Radial Lattice Interpretation

若合法 \(U\) 存在，令：

\[
x:=\frac U\tau.
\]

则：

\[
x=\frac{UC_3}{10^{n_3}}
=\frac{a_3}{10^{n_3}},
\]

且：

\[
\rho x
=
\frac{UC_2}{10^{n_2}}
=\frac{a_2}{10^{n_2}}.
\]

所以：

\[
0.1\le x<1,
\qquad
0.1\le\rho x<1.
\]

即：

\[
\boxed{x\in J(\rho).}
\]

改变 \(U\mapsto U+1\) 时：

\[
\Delta x=\frac1\tau.
\]

因此 common-\(U\) 是：

\[
\boxed{
J(\rho)
\text{ 中是否存在一个 }(1/\tau)\mathbf Z
\text{ lattice point，}
}
\]

其 integer label \(U\) 还需：

\[
\boxed{\gcd(U,V)=1.}
\]

**状态：NEW PROVED / EQUIVALENT.**

---

# 13. Exact Integer Margins in Normalized Form

因为：

\[
a_i\le10^{n_i}-1,
\]

若 \(U\) 合法：

\[
1-x
=
\frac{10^{n_3}-a_3}{10^{n_3}}
\ge10^{-n_3},
\]

\[
1-\rho x
=
\frac{10^{n_2}-a_2}{10^{n_2}}
\ge10^{-n_2}.
\]

故：

\[
\boxed{1-x\ge10^{-n_3}},
\]

\[
\boxed{1-\rho x\ge10^{-n_2}}.
\tag{MARGIN-X}
\]

这是既有 Sharp Integer Radial Margin 的 normalized 版本。既有 theorem 本身见 unified moving-profile report。 fileciteturn10file0

---

# 14. \(\sigma\) Audit

定义：

\[
\boxed{
\sigma
:=
\frac{b_3}{b_2 10^{n_3-d}}.
}
\]

由于：

\[
 m_3-m_2=n_3-d,
\]

\(b_2\) 为 \(m_2\)-digit，\(b_3\) 为 \(m_3\)-digit，故：

\[
10^{m_2-1}\le b_2<10^{m_2},
\]

\[
10^{m_3-1}\le b_3<10^{m_3}.
\]

于是：

\[
\frac{10^{m_3-1}}{10^{m_2}10^{n_3-d}}
<\sigma<
\frac{10^{m_3}}{10^{m_2-1}10^{n_3-d}},
\]

即：

\[
\boxed{0.1<\sigma<10.}
\tag{SIG-W}
\]

同时令 denominator mantissas：

\[
\beta_i=b_i/10^{m_i},
\]

则：

\[
\boxed{\sigma=\beta_3/\beta_2.}
\tag{SIG-B}
\]

---

# 15. \(\sigma\) as Exact GCD Ratio

因为：

\[
\frac{b_3}{b_2}
=
\frac{V/g_3}{V/g_2}
=
\frac{g_2}{g_3},
\]

所以：

\[
\boxed{
\sigma
=
\frac{g_2}{10^{n_3-d}g_3}.
}
\tag{SIGG}
\]

在 Smith 坐标：

\[
\frac{g_2}{g_3}
=
\frac{v}{\alpha t},
\]

故：

\[
\boxed{
\sigma
=
\frac{v}{\alpha t10^{n_3-d}}.
}
\tag{SIGS}
\]

**状态：NEW PROVED.**

---

# 16. RHO3 / TAU Bridge — Exact Audit

由：

\[
\frac{C_2}{C_3}
=
\frac{b_2P_2}{b_3P_3},
\]

以及：

\[
\rho=rac{C_2}{C_3}10^{n_3-n_2},
\]

得：

\[
\rho
=
\frac{b_2P_2}{b_3P_3}10^{n_3-n_2}.
\]

使用：

\[
\frac{b_2}{b_3}
=
\frac1{\sigma10^{n_3-d}},
\]

以及：

\[
n_2=2g+k+d,
\]

可得：

\[
\boxed{
\rho
=
\frac{P_2}{\sigma10^{2g+k}P_3}.
}
\tag{RHO3}
\]

另外：

\[
\tau
=
\frac{10^{n_3}g_3}{P_3}.
\]

由 SIGG：

\[
g_3=\frac{g_2}{\sigma10^{n_3-d}},
\]

所以：

\[
\boxed{
\tau
=
\frac{10^d g_2}{\sigma P_3}.
}
\tag{TAU}
\]

prompt 候选 RHO3/TAU 均严格成立。

**状态：NEW PROVED.**

---

# 17. NEW PROVED — Full Smith–Radial Cancellation

现在代入：

\[
P_2=vM,
\quad
P_3=\alpha tN,
\quad
\sigma=\frac{v}{\alpha t10^{n_3-d}}.
\]

RHO3 给：

\[
\rho
=
\frac{vM}
{\frac{v}{\alpha t10^{n_3-d}}10^{2g+k}\alpha tN}
\]

所以所有 \(v,\alpha,t\) 完全消去：

\[
\boxed{
\rho
=
\frac MN
10^{n_3-(2g+k+d)}
=
\frac MN10^{n_3-n_2}.
}
\tag{SR-RHO}
\]

TAU：

\[
\tau
=
\frac{10^d(u_0v)}
{\frac{v}{\alpha t10^{n_3-d}}\alpha tN}
=
\boxed{
\frac{u_0 10^{n_3}}N.
}
\tag{SR-TAU}
\]

等价地，直接由 \(C_2=M/u_0,C_3=N/u_0\) 立即得到同样结果。

这是本轮的核心 theorem。

### 重要结构后果 1

\[
\boxed{
\text{denominator ratio factor }v/(\alpha t)
\text{ 不控制 }\rho.
}
\]

### 重要结构后果 2

\[
\boxed{
\text{\(R\)-sign / \(\sigma\)-position cannot by itself push \(\rho\) to a digit boundary.}
}
\]

### 重要结构后果 3

prompt 中候选：

> “\(d\) is radial-size parameter, not normalized-ratio parameter”

在 fully Smith-reduced chart 中不成立。

事实上：

\[
\boxed{
\tau=\frac{u_0 10^{n_3}}N
}
\]

没有显式 \(d\)，而：

\[
\boxed{
\rho=\frac MN10^{n_3-2g-k-d}
}
\]

显式包含 \(d\)。

因此本轮应正式替换原解释为：

\[
\boxed{
\textbf{after Smith cancellation, }d\textbf{ is a projective-decade shift parameter.}
}
\]

**状态：NEW PROVED / STRATEGY-CORRECTING.**

---

# 18. NEW PROVED — Smith-Reduced Common-\(U\) Interval

由 \(C_2=M/u_0,C_3=N/u_0\)：

\[
I_2
=
 u_0
\left[
\frac{10^{n_2-1}}M,
\frac{10^{n_2}}M
\right),
\]

\[
I_3
=
 u_0
\left[
\frac{10^{n_3-1}}N,
\frac{10^{n_3}}N
\right).
\]

定义：

\[
\boxed{
K_{MN}
:=
\left[
\max\left(\frac{10^{n_2-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{n_2}}M,\frac{10^{n_3}}N\right)
\right).
}
\]

则：

\[
\boxed{
I_{23}=u_0K_{MN}.
}
\tag{KMN}
\]

这比 \((\tau,\rho)\) 更适合与 full Smith arithmetic 接口。

---

# 19. Prescribed-Denominator Reduced Fraction Form

合法 \(U\) 必有：

\[
\gcd(U,V)=1.
\]

由于 \(u_0\mid V\)：

\[
\boxed{\gcd(U,u_0)=1.}
\]

因此：

\[
y=\frac U{u_0}
\]

已经是 lowest terms，且分母**恰为** \(u_0\)。

由 KMN：

\[
\boxed{
\frac U{u_0}\in K_{MN}.
}
\tag{RFRAC}
\]

同时：

\[
\frac{a_2}{M}
=
\frac{U(M/u_0)}M
=
\frac U{u_0},
\]

\[
\frac{a_3}{N}
=
\frac U{u_0}.
\]

故：

\[
\boxed{
\frac{a_2}{M}
=
\frac{a_3}{N}
=
\frac U{u_0}
\quad\text{in lowest terms.}
}
\tag{SAME-RF}
\]

这是 common-\(U\) 在 latest Smith chart 中最紧凑的 arithmetic representation。

---

# 20. Full Unit Sieve

由：

\[
V=s\alpha\beta\gamma u_0tv_0,
\]

以及：

\[
v=\gamma v_0,
\]

可重写：

\[
\boxed{
V=s\beta u_0v\alpha t.
}
\tag{VFACT}
\]

所以 legal \(U\) 等价满足：

\[
\boxed{
\gcd(U,u_0)=1,
}
\]

以及：

\[
\boxed{
\gcd(U,s\beta v\alpha t)=1.
}
\tag{TRANS-UNIT}
\]

因此 Smith radial problem 精确拆成：

\[
\boxed{
\textbf{reduced fraction denominator }u_0
}
\]

\[
\times
\]

\[
\boxed{
\textbf{transverse unit sieve }s\beta v\alpha t.
}
\]

这也是 Smith-rich / Smith-poor 真正应该被重新解释的方式。

---

# 21. Cross-Coordinate Identity Audit

由定义：

\[
C_i=P_i/g_i,
\qquad
b_i=V/g_i.
\]

所以：

\[
C_2b_3P_3
=
\frac{P_2}{g_2}\frac{V}{g_3}P_3,
\]

\[
C_3b_2P_2
=
\frac{P_3}{g_3}\frac{V}{g_2}P_2.
\]

二者相等：

\[
\boxed{
C_2b_3P_3=C_3b_2P_2.
}
\tag{CROSS}
\]

**状态：NEW PROVED.**

---

# 22. NEW PROVED — \(b_3\)-Residual Divisor of \(H\)

由 E3：

\[
b_2P_2
=
10^gH
+
\frac{b_3(Q_0-P_3)}{10^{n_3}}.
\]

乘 \(C_3\)，再用 CROSS：

\[
C_2b_3P_3
=
C_310^gH
+
C_3\frac{b_3(Q_0-P_3)}{10^{n_3}}.
\]

乘 \(10^{n_3}\)：

\[
b_3
\left(
10^{n_3}C_2P_3
-
C_3(Q_0-P_3)
\right)
=
C_310^{n_3+g}H.
\]

由 \(m_3=n_3+g\)：

\[
\boxed{
 b_3
\left(
10^{n_3}C_2P_3-C_3(Q_0-P_3)
\right)
=
C_310^{m_3}H.
}
\tag{B3H-ID}
\]

已知 reducedness consequence：

\[
\gcd(C_3,b_3)=1.
\]

所以：

\[
\boxed{b_3\mid10^{m_3}H.}
\]

定义：

\[
\boxed{
B_3^\sharp
:=
\frac{b_3}{\gcd(b_3,10^{m_3})}.
}
\]

则：

\[
\boxed{B_3^\sharp\mid H.}
\tag{B3DIV}
\]

因此 prompt 的 B3DIV 候选为真。

**状态：NEW PROVED.**

---

# 23. B3DIV Is Already Absorbed by Latest Iterated Smith

最新 report 已证明第二层 Smith deflation。 fileciteturn13file14

定义：

\[
\delta_\beta=\gcd(\beta,10^{m_3}),
\qquad
\beta^\sharp=\beta/\delta_\beta,
\]

\[
\Lambda_\beta=10^{m_3}/\delta_\beta.
\]

由 tail Smith：

\[
\Lambda_\beta q_H
=v(tM10^{n_3}-A_3).
\]

令：

\[
\delta_v=\gcd(v,\Lambda_\beta),
\]

\[
v^\sharp=v/\delta_v,
\qquad
J=\Lambda_\beta/\delta_v,
\]

则存在唯一 \(Z\ne0\)：

\[
q_H=v^\sharp Z,
\]

\[
tM10^{n_3}-A_3=JZ.
\]

所以：

\[
\boxed{
H=s\alpha\beta^\sharp v^\sharp Z.
}
\tag{DS-H}
\]

定义：

\[
\boxed{
M_H^{(2)}:=s\alpha\beta^\sharp v^\sharp.
}
\]

则：

\[
\boxed{M_H^{(2)}\mid H.}
\]

现在逐素数比较 \(B_3^\sharp\) 与

\[
s\beta^\sharp v^\sharp.
\]

对 \(p\notin\{2,5\}\)，后者包含 \(b_3=s\beta v\) 的完整 \(p\)-part。

对 \(p=2,5\)，记：

\[
a=v_p(s),\quad b=v_p(\beta),\quad c=v_p(v),\quad m=m_3.
\]

则：

\[
v_p(B_3^\sharp)=[a+b+c-m]_+.
\]

而：

\[
v_p(s\beta^\sharp v^\sharp)
=
a+[b-m]_+
+
\left[c-[m-b]_+\right]_+.
\]

分三种情况：

1. \(b\ge m\)：两边右式为 \(a+b+c-m\)；
2. \(b<m\) 且 \(b+c\ge m\)：右式为 \(a+b+c-m\)；
3. \(b+c<m\)：右式为 \(a\)，而左式 \(\le a\)。

所以：

\[
\boxed{
B_3^\sharp\mid s\beta^\sharp v^\sharp
\mid M_H^{(2)}.
}
\tag{B3-RED}
\]

因此：

\[
\boxed{
\textbf{B3DIV 为真，但不是 latest DS core 之外的新 independent divisor.}
}
\]

**状态：NEW PROVED + REDUNDANCY CERTIFICATE.**

---

# 24. Strongest Current State-Dependent Defect Divisor

旧 Smith-reduced tail report还定义：

\[
G_T:=\gcd(tP_2,vA_3),
\]

\[
G_T^\sharp
:=
\frac{G_T}{\gcd(G_T,\Lambda_\beta)},
\]

并证明：

\[
M_HG_T^\sharp\mid H.
\]

见 previous Smith campaign。 fileciteturn13file15

因为：

\[
P_2=vM,
\]

所以：

\[
G_T
=
\gcd(tvM,vA_3)
=
v\gcd(tM,A_3).
\]

定义：

\[
\boxed{
h_T:=\gcd(tM,A_3).
}
\]

而：

\[
tM10^{n_3}-A_3=JZ.
\]

由于 \(h_T\mid tM\) 且 \(h_T\mid A_3\)：

\[
h_T\mid JZ.
\]

定义：

\[
\boxed{
 h_T^\sharp
:=
\frac{h_T}{\gcd(h_T,J)}.
}
\]

则：

\[
\boxed{h_T^\sharp\mid Z.}
\tag{HTZ}
\]

因此：

\[
\boxed{
\mathcal M_{\max}
:=
s\alpha\beta^\sharp v^\sharp h_T^\sharp
\mid H.
}
\tag{MMAX}
\]

进一步逐素数可验证：

\[
\boxed{
G_T^\sharp=v^\sharp h_T^\sharp.
}
\tag{GT-ID}
\]

所以：

\[
\boxed{
\mathcal M_{\max}
=
M_HG_T^\sharp
=
M_H^{(2)}h_T^\sharp.
}
\]

这是截至本轮 strongest proved state-dependent defect divisor。

定义最终 defect quotient：

\[
\boxed{
q:=\frac H{\mathcal M_{\max}}
=
\frac Z{h_T^\sharp}
\in\mathbf Z\setminus\{0\}.
}
\tag{QMAX}
\]

本轮**没有**证明 \(|q|\) uniform bounded；旧 counterexample 对 uniform bounded quotient 的否定仍冻结。

---

# 25. Cross-Coordinate Divisor Audit — Other Pairs

本轮系统检查其他 pair。

## Pair \((2,3)\)

得到 B3DIV，已证明且被 DS core 吸收。

## Pair \((1,2)\)

与 E1 联立可导出：

\[
\beta t\mid10^{m_2}(Q_0+D)
=10^{m_2+k}P_1.
\]

但 full gcd profile 已有：

\[
g_1=\beta tv_0\mid P_1,
\]

所以这没有新增独立 \(H\)-divisor。

## Pair \((1,3)\)

消元后得到的 residual divisibility 被：

- full Smith determinant；
- XH identity；
- latest \(v^\sharp\) deflation

吸收，未产生一个强于 \(\mathcal M_{\max}\) 的 forced divisor。

因此：

\[
\boxed{
\textbf{当前 cross-coordinate divisor audit 已饱和于 }\mathcal M_{\max}.
}
\]

**状态：AUDITED / NO FURTHER INDEPENDENT DIVISOR FOUND.**

---

# 26. NEW PROVED — Smith/GCD Duality

任取：

\[
p^e\Vert V.
\]

令：

\[
a_i=v_p(g_i).
\]

则：

\[
v_p(b_i)=e-a_i.
\]

所以：

\[
v_p(\gcd(b_i,b_j))
=e-\max(a_i,a_j).
\]

而：

\[
v_p(\operatorname{lcm}(g_i,g_j))
=\max(a_i,a_j).
\]

两者相加为 \(e\)。故逐素数：

\[
\boxed{
\gcd(b_i,b_j)\operatorname{lcm}(g_i,g_j)=V.
}
\tag{DUAL}
\]

**状态：NEW PROVED.**

---

# 27. DUAL in the \((2,3)\) Smith Chart

由 Smith：

\[
\gcd(b_2,b_3)=s\beta.
\]

由：

\[
g_2=u_0v,
\quad
g_3=u_0\alpha t,
\quad
\gcd(v,\alpha t)=1,
\]

得：

\[
\operatorname{lcm}(g_2,g_3)
=u_0v\alpha t.
\]

所以：

\[
\boxed{
V=(s\beta)(u_0v\alpha t).
}
\]

这与 VFACT 完全一致。

因此 denominator overlap 与 primitive gcd absorption 确实 exact complementary。

但是本轮的 Smith–radial cancellation 表明：

- \(u_0\) 进入 reduced-fraction denominator / interval scale；
- \(v,\alpha t\) 从 endpoints 中消掉；
- \(v,\alpha t\) 只留在 unit sieve。

所以：

\[
\boxed{
\textbf{DUAL 不自动把 Smith-poor 变成 radial-spacing contradiction.}
}
\]

这是对 Smith-poor strategy 的重要校准。

---

# 28. Smith-Rich Redefinition

今后若使用 rich/poor，应基于：

\[
\boxed{\mathcal M_{\max}}
\]

而不是旧 \(M_H\)。

plus：

\[
|H|<Q_0.
\]

若：

\[
\mathcal M_{\max}>Q_0/K,
\]

则：

\[
1\le|q|<K.
\]

minus \(d=0\) 同样：

\[
0<H<Q_0,
\]

所以相同 finite quotient reduction。

minus \(d=1\)：

\[
0<H<10Q_0,
\]

若：

\[
\mathcal M_{\max}>10Q_0/K,
\]

则：

\[
1\le q<K.
\]

**状态：DERIVED.**

---

# 29. Fixed-\(q\) Exact Affine Radial Formula

由：

\[
Z=h_T^\sharp q,
\]

以及 latest affine identity：

\[
X=\alpha JZ,
\]

\[
X
=
\alpha t(M10^{n_3}+N)-Q_0,
\]

得到：

\[
\boxed{
\alpha t(M10^{n_3}+N)
=
Q_0+\alpha J h_T^\sharp q.
}
\tag{FQ-AFF}
\]

记：

\[
A:=\alpha t,
\quad
B:=v,
\quad
T:=10^{n_3},
\quad
E:=\alpha J h_T^\sharp q.
\]

则：

\[
\boxed{Q_0=A(MT+N)-E.}
\tag{QMN}
\]

同时：

\[
Q_0-P_3
=A MT-E>0.
\]

sphere：

\[
P_1^2+B^2M^2+A^2N^2
=
[A(MT+N)-E]^2.
\]

消掉 \(A^2N^2\)：

\[
\boxed{
(AMT-E)(AMT+2AN-E)
=P_1^2+B^2M^2.
}
\tag{FQ-SPH}
\]

若解出 \(N\)：

\[
\boxed{
N
=
\frac{
P_1^2+B^2M^2-(AMT-E)^2
}
{2A(AMT-E)}.
}
\tag{FQ-N}
\]

这是真正的 finite-\(q\) radial formula。

但即使 \(q\) finite：

- \(M\) 仍可移动；
- \(P_1\) 仍可移动；
- \(u_0\) 仍可移动；
- unit sieve仍未 fixed。

因此：

\[
\boxed{
\textbf{Smith-rich }\Rightarrow\textbf{ finite q}
\textbf{，但并不自动 }\Rightarrow\textbf{ finite radial states.}
}
\]

**状态：NEW PROVED REDUCTION / NOT CLOSURE.**

---

# 30. Smith-Poor Reassessment

若 \(\mathcal M_{\max}/Q_0\) small，DUAL 确实可以使某些：

\[
\operatorname{lcm}(g_i,g_j)
\]

large。

但 fully reduced radial endpoints只读取：

\[
u_0=\gcd(g_2,g_3),
\]

以及：

\[
M,N.
\]

complementary factors：

\[
v,
\qquad
\alpha t
\]

不会把 interval 自动变短，而是只增加：

\[
\gcd(U,s\beta v\alpha t)=1
\]

中的 forbidden primes。

因此：

\[
\boxed{
\textbf{Smith-poor }
\not\Rightarrow
\textbf{ interval geometry poor}
}
\]

without an exact positional unit-cover theorem。

尤其 \(U=1\) 永远是 unit，所以任何只依赖“\(V\) 有很多素因子”的 route 都不能 closure。

**状态：FAILED AS PURE MAGNITUDE ROUTE.**

---

# 31. Three Radial Failure Layers

本轮采用：

### Layer C — Continuous dead

\[
K_{MN}=\varnothing
\iff
I_{23}=\varnothing.
\]

### Layer I — Integer dead

\[
I_{23}\ne\varnothing,
\quad
I_{23}\cap\mathbf Z_{>0}=\varnothing.
\]

### Layer P — Unit/coprime dead

\[
I_{23}\cap\mathbf Z_{>0}\ne\varnothing,
\]

但：

\[
\forall U\in I_{23}\cap\mathbf Z_{>0},
\quad
\gcd(U,V)>1.
\]

任何 future proof 应尽量先 C，再 I，最后 P。

---

# 32. Exact Coprime Successor

对：

\[
I=[L,R),
\]

已有 exact count：

\[
\boxed{
N_V(L,R)
=
\sum_{d\mid\operatorname{rad}(V)}
\mu(d)
\left(
\left\lceil\frac Rd\right\rceil
-
\left\lceil\frac Ld\right\rceil
\right).
}
\tag{COPRIME}
\]

这一 endpoint convention 与旧 common-\(U\) report 一致。 fileciteturn12file16

所以：

\[
\boxed{
N_V(L,R)>0
\iff
\operatorname{next}_V(L)<R.
}
\]

在 Smith chart 中：

\[
L=u_0A,
\qquad
R=u_0B
\]

for \([A,B)=K_{MN}\)。

没有使用概率密度替代 exact count。

---

# 33. U=1 Gate

\(U=1\) 自动：

\[
\gcd(1,V)=1.
\]

所以必须优先检查。

在 Smith chart：

\[
1\in I_2
\iff
10^{n_2-1}\le C_2<10^{n_2}
\]

即：

\[
\boxed{
u_0 10^{n_2-1}\le M<u_0 10^{n_2}.}
\]

同理：

\[
\boxed{
u_0 10^{n_3-1}\le N<u_0 10^{n_3}.}
\]

因此：

\[
\boxed{
U=1\text{ survives}
\iff
M/u_0,N/u_0
\text{ themselves have the required digit lengths.}
}
\tag{U1}
\]

这再次说明 pure radical-rich / prime-density route 不足。

---

# 34. Slack Variables

若 \(U\) legal，定义：

\[
E_i^-:=P_iU-10^{n_i-1}g_i,
\]

\[
E_i^+:=10^{n_i}g_i-P_iU.
\]

则：

\[
E_i^-\ge0,
\qquad
E_i^+\ge1.
\]

消去 \(U\)：

\[
P_3(10^{n_2}g_2-E_2^+)
=
P_2(10^{n_3}g_3-E_3^+).
\]

所以：

\[
\boxed{
10^{n_2}g_2P_3
-
10^{n_3}g_3P_2
=
P_3E_2^+-P_2E_3^+.
}
\tag{SLACK}
\]

左侧又是：

\[
10^{n_2}g_2P_3(1-\rho).
\]

故：

\[
\boxed{
1-\rho
=
\frac{P_3E_2^+-P_2E_3^+}
{10^{n_2}g_2P_3}.
}
\]

**状态：NEW PROVED.**

目前没有从 exact-word 导出足够强的 slack bound，故这条 identity 暂不 closure。

---

# 35. Resonance Normal Form

定义：

\[
R=b_210^{n_3}-b_3.
\]

最新 source 已证明：

\[
R=0
\Longrightarrow
\boxed{d=0},
\]

\[
\boxed{\alpha=t=1},
\qquad
\boxed{v=10^{n_3}}.
\]

并：

\[
\boxed{b_3=b_210^{n_3}},
\]

\[
\boxed{g_2=10^{n_3}g_3}.
\]

见最新 resonance report。 fileciteturn8file9

---

# 36. NEW DERIVED — Resonance in Full Smith–Radial Coordinates

代 \(\alpha=t=1\)、\(v=10^{n_3}\) 入 full Smith：

\[
\boxed{
 g_2=u_0 10^{n_3},
\qquad
 g_3=u_0.
}
\]

又：

\[
P_2=vM
\Longrightarrow
\boxed{P_2=10^{n_3}M},
\]

\[
P_3=\alpha tN
\Longrightarrow
\boxed{P_3=N}.
\]

所以：

\[
\boxed{
C_2=M/u_0,
\qquad
C_3=N/u_0.
}
\]

VFACT 变成：

\[
\boxed{
V=s\beta u_0 10^{n_3}.
}
\tag{R-V}
\]

因此任何 legal U：

\[
\boxed{\gcd(U,10)=1}
\]

且 last digit 必为 \(1,3,7,9\)。

---

# 37. Resonance Radial Interval — Canonical Form

resonance 中 \(d=0\)，故：

\[
n_2=2g+k.
\]

所以：

\[
\boxed{
I_{23}
=
 u_0
\left[
\max\left(\frac{10^{2g+k-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{2g+k}}M,\frac{10^{n_3}}N\right)
\right).
}
\tag{RES-I}
\]

令：

\[
y=U/u_0.
\]

则 y 是 denominator exactly \(u_0\) 的 reduced rational，且：

\[
\boxed{
y\in K^{\rm res}_{MN}.
}
\]

同时：

\[
\boxed{
\gcd(U,s\beta u_0 10^{n_3})=1.
}
\]

相比 prompt 使用 \(U/g_2\)，该坐标剥掉了 tautological \(10^{n_3}\) factor，因而更低维。

---

# 38. Resonant \(J=L_R\) Identification

resonance 中最新 source 有：

\[
S_3=P_2+P_3-Q_0\ne0,
\]

以及：

\[
L_R
=
\frac{10^g}{\gcd(10^g,\delta_\beta)}
\mid S_3.
\]

在 iterated Smith coordinates：

\[
S_3=\alpha JZ-M\widehat R.
\]

resonance：

\[
\alpha=1,
\quad
\widehat R=0,
\]

所以：

\[
\boxed{S_3=JZ.}
\]

逐 \(2,5\)-valuation 比较 \(J=\Lambda_\beta/\delta_v\) 可恢复：

\[
\boxed{J=L_R>1.}
\tag{JLR}
\]

因此 old residual decimal divisor 与 latest Double-Smith divisor 是同一对象。

**状态：NEW DERIVED / IDENTIFICATION.**

---

# 39. Resonant Primitive Ratio Gap

旧 primitive ratio window 给：

\[
10^{2g+k-2}
<
\frac{P_2}{P_3}
<
10^{2g+k+2}.
\]

resonance：

\[
\frac{P_2}{P_3}
=
10^{n_3}\frac MN.
\]

所以：

\[
\boxed{
10^{2g+k-n_3-2}
<
\frac MN
<
10^{2g+k-n_3+2}.
}
\tag{RES-PR}
\]

但 continuous common-\(U\) 要求：

\[
0.1<\rho<10,
\]

而：

\[
\rho=\frac MN10^{n_3-(2g+k)}.
\]

故：

\[
\boxed{
10^{2g+k-n_3-1}
<
\frac MN
<
10^{2g+k-n_3+1}.
}
\tag{RES-CONE}
\]

比较可见：现有 primitive axis theorem 比真正 radial cone **左右各宽一 decade**。

因此当前 primitive ratio bounds 无法关闭 resonance；这精确解释了为什么 prompt 的 RG1 / Farey route没有自动完成。

---

# 40. Resonant 2-Adic Trichotomy — Frozen

最新 report 对：

\[
a=v_2(\beta)
\]

证明：

\[
a<g
\Longrightarrow
v_2(S_3)=g,
\]

\[
a=g
\Longrightarrow
v_2(S_3)\ge g+1,
\]

\[
g<a\le2g
\Longrightarrow
v_2(S_3)=2g-a,
\]

\[
a>2g
\Longrightarrow\bot.
\]

见 latest resonance source。 fileciteturn9file9

本轮将它与 RES-I 联立检查，没有导出：

\[
N_V(I_{23})=0.
\]

原因是该 valuation控制 \(S_3=JZ\)，而 interval geometry由 \(u_0,M,N\) 控制；缺少一个把 \(S_3\)-depth 变成 unit-successor location 的 exact bridge。

**状态：OPEN.**

---

# 41. Resonance Closure Verdict

本轮没有证明：

\[
\boxed{R=0\Longrightarrow N_V(I_{23})=0.}
\]

但 resonance 已被压成：

\[
\boxed{
\begin{array}{c}
P_2=10^{n_3}M,\quad P_3=N,\quad
V=s\beta u_0 10^{n_3},\\[1mm]
S_3=JZ\ne0,\quad J=L_R>1,\\[1mm]
U/u_0\in K^{\rm res}_{MN}\text{ reduced},\\[1mm]
\gcd(U,s\beta u_0 10^{n_3})=1,
\end{array}
}
\]

加上 sphere 与 resonant 2-adic trichotomy。

因此 resonance 的精确最小 theorem 是：

## Resonant Reduced-Fraction Unit Exclusion — OPEN

> 上述 exact resonant state 不存在一个 denominator exactly \(u_0\) 的 reduced rational \(U/u_0\) 落入 \(K^{\rm res}_{MN}\)，同时其 numerator \(U\) 为 \(s\beta10^{n_3}\)-unit。

---

# 42. \(d=0\) Nonresonant — \(\sigma\) Sign Map

\(d=0\)：

\[
\sigma
=
\frac{v}{\alpha t10^{n_3}}.
\]

而：

\[
\widehat R=\alpha t10^{n_3}-v.
\]

所以：

\[
\boxed{R>0\iff\sigma<1},
\]

\[
\boxed{R<0\iff\sigma>1}.
\]

这部分 prompt 是对的。

但是：

\[
\rho
=
\frac MN10^{n_3-(2g+k)}
\]

与 \(\sigma\) 无直接因子。

所以：

\[
\boxed{
R\text{-sign does not determine }\rho<1\text{ or }>1.
}
\]

必须再有一个真正限制 \(M/N\) 的 theorem 才能把 word sign传进 active radial endpoint。

**状态：NEW STRATEGY CORRECTION.**

---

# 43. \(d=0\) Minus One-Borrow

minus：

\[
c=1.
\]

因此：

\[
0<H<Q_0.
\]

若 Smith-rich：

\[
H=\mathcal M_{\max}q
\]

把 q finite-ize 后，FQ-AFF / FQ-SPH 全部可用。

但 fixed q 尚不能限制：

\[
\frac MN
\]

到一个 radial lattice cell；因此无法证明：

\[
W<1
\]

或：

\[
N_V(I_{23})=0.
\]

**状态：OPEN.**

---

# 44. \(d=0\) Plus

plus：

\[
-Q_0<H<0.
\]

相同地，rich 给 finite negative q。

latest sign-mismatch theorem 若 \(HR<0\)，给：

\[
|S_3|
=\alpha J|Z|+M|\widehat R|
\ge\alpha J+M.
\]

但 radial endpoints只读取 \(u_0,M,N\)。

\(\widehat R\) 或 \(v/(\alpha t)\) 的大/小不通过 identity直接控制 \(M/N\)。

所以 mismatch absorption 是 genuine arithmetic compression，但仍不是 SRCU closure。

**状态：OPEN.**

---

# 45. \(d=1\) Plus Near Resonance

旧 exact mantissa theorem 给：

\[
\beta_2<0.10258,
\qquad
\beta_3>0.9749.
\]

更精确地，使用：

\[
x=P_2/Q_0>\sqrt{96/101},
\]

可取：

\[
\beta_2<\frac1{10x},
\qquad
\beta_3>x.
\]

所以：

\[
\boxed{
\sigma=\frac{\beta_3}{\beta_2}>10x^2>\frac{960}{101}>9.50495.
}
\tag{D1-SIG}
\]

这严格确认 denominator mantissa ratio 靠近 10。

最新 Double-Smith 又给：

\[
\boxed{v>0.385\,10^{2k}.}
\]

见 latest report。 fileciteturn9file1

但 fully reduced radial ratio为：

\[
\boxed{
\rho
=
\frac MN10^{n_3-(2g+k+1)}.
}
\]

其中 \(v\) 与 \(\alpha t\) 全部消失。

所以：

\[
\boxed{
\sigma>9.5
\not\Rightarrow
\rho\approx0.1
}
\]

as a structural identity。

prompt 中 d=1 plus 的 “near-\(\sigma\) boundary \(\Rightarrow\) radial boundary” route 因此被严格否定为 standalone route。

**状态：DISPROVED AS DIRECT COUPLING.**

---

# 46. \(d=1\) Minus Finite Carry

minus：

\[
1\le c\le10.
\]

且：

\[
(c-1)Q_0<H\le cQ_0.
\]

Smith-rich 时，\((c,q)\) 确为 finite set。

然而 fixed \((c,q)\) 仍只给 FQ-AFF/FQ-SPH 中的 finite offset，未固定 \(M/N\) 或 \(u_0\)。

所以十个 carry branches 尚未关闭。

**状态：OPEN.**

---

# 47. General \(d\) — Correct Radial Role

由 SR-RHO / SR-TAU：

\[
\boxed{
\rho
=
\frac MN10^{n_3-2g-k-d},
}
\]

\[
\boxed{
\tau
=
\frac{u_0 10^{n_3}}N.
}
\]

因此在 canonical Smith chart：

- \(d\) 直接平移 projective ratio的 decimal decade；
- \(d\) 不直接缩放 radial lattice step；
- radial lattice step主要由 \(u_0/N\) 控制。

所以 outer \(d\) branches未来不应再按 “\(10^d\) 使 \(\tau\) 大/小” 组织。

正确组织应是：

\[
\boxed{
\text{d-shifted }M/N\text{ cone}
\times
\text{u}_0/N\text{ lattice scale}
\times
\text{unit sieve}.
}
\]

**状态：NEW STRUCTURAL CORRECTION.**

---

# 48. Exact Active Endpoint Map

RNF 仍给：

若：

\[
\rho<1,
\]

则：

\[
J(\rho)
=
\left[\frac1{10\rho},1\right),
\]

第三块 upper endpoint active。

若：

\[
\rho>1,
\]

则：

\[
J(\rho)
=
\left[\frac1{10},\frac1\rho\right),
\]

第二块 upper endpoint active。

但 \(R\)-sign 当前不能直接预测该 active block；需要 \(M/N\)-word coupling。

---

# 49. Width \(<1\) Criterion in Smith Coordinates

由：

\[
I_{23}=u_0K_{MN},
\]

若：

\[
\operatorname{length}(K_{MN})<1/u_0,
\]

则：

\[
\boxed{W<1.}
\]

至多一个 candidate \(U\)。

这等价于 RNF 的：

\[
w(\rho)<1/\tau.
\]

但本轮没有从 H/Smith 强制得到上述 inequality 对任何完整 chamber uniformly 成立。

**状态：OPEN.**

---

# 50. Smith-Poor Prime Complement — Exact Meaning

DUAL 给：

\[
\gcd(b_2,b_3)\operatorname{lcm}(g_2,g_3)=V.
\]

pair \(23\)：

\[
\operatorname{lcm}(g_2,g_3)=u_0v\alpha t.
\]

所以若 denominator overlap \(s\beta\) 小，则 complementary factor \(u_0v\alpha t\) 大。

但是：

\[
C_2=M/u_0,
\qquad
C_3=N/u_0.
\]

因此只有 \(u_0\) 进入 endpoints；\(v,\alpha t\) 不进入。

所以 Smith-poor 的 exact radial interpretation是：

\[
\boxed{
\text{large transverse unit modulus}
\text{，而不一定是 large radial denominator}.
}
\]

这比旧“至少两个 primitive coordinates吸收大 prime power”更直接，也说明 generic primewise magnitude路线为什么难 closure。

---

# 51. Simultaneous Reduced Fractions

对任意合法 \(U\)：

\[
\frac U{g_i}
=
\frac{a_i}{P_i}.
\]

因为：

\[
\gcd(U,g_i)=1,
\]

左侧为 lowest terms。

对 \(i=2,3\)：

\[
\frac{10^{n_i-1}}{P_i}
\le
\frac U{g_i}
<
\frac{10^{n_i}}{P_i}.
\]

Smith cancellation进一步统一为：

\[
\frac U{u_0}
=
\frac{a_2}{M}
=
\frac{a_3}{N}.
\]

因此真正 simultaneous reduced-fraction object不是两个不同 denominator \(g_2,g_3\)，而是同一个：

\[
\boxed{u_0=\gcd(g_2,g_3).}
\]

**状态：NEW COMPRESSION.**

---

# 52. Known \(g=0\) Infinite Pseudo-Family — SRCU Regression

旧 generic primitive-defect report 构造固定：

\[
(b_1,b_2,b_3)=(1,6,8),
\quad
V=24,
\]

\[
(g_1,g_2,g_3)=(24,4,3),
\]

\[
(g,k,m_2,n_2,n_3)=(0,1,1,2,1),
\]

的 infinite synchronized family，并证明：

\[
C_3>C_2.
\]

见 ordering theorem。 fileciteturn12file3

此时：

\[
\rho
=
\frac{C_2}{10C_3}
<0.1.
\]

所以整个 family 直接：

\[
\boxed{\textbf{Layer C dead}.}
\]

这验证了本轮 RNF 对已知 exact-word insufficiency certificate 的正确解释。

---

# 53. Known Real-Cone Point — Layer I Regression

旧 common-\(U\) report 有 exact synchronized point：

\[
(P_1,P_2,P_3,Q_0)
=(7776,71252,7899,72109),
\]

\[
V=24,
\quad
C_2=17813,
\quad
C_3=2633,
\]

\[
n_2=2,
\quad
n_3=1.
\]

其：

\[
I_{23}
e\varnothing,
\]

但：

\[
I_{23}\subset(0,1).
\]

因此：

\[
\boxed{\textbf{Layer I dead}.}
\]

这说明 continuous cone确实不是 integer radial gate。原 point 与结论见 source。 fileciteturn12file17

---

# 54. Known Double-Smith Regression States

最新 report 对同一 profile记录三个 synchronized states。 fileciteturn11file0

\[
(b_1,b_2,b_3)=(1,6,8),
\quad
V=24,
\quad
C_2=P_2/4,
\quad
C_3=P_3/3.
\]

### State A

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169).
\]

\[
C_2=13,
\quad
C_3=53,
\]

\[
\rho=\frac{13}{530}<0.1.
\]

Layer C dead。

### State B

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445).
\]

\[
C_2=109,
\quad
C_3=25,
\]

\[
\rho=109/250=0.436.
\]

\[
I_{23}
=
[10/109,2/5),
\]

所以 real overlap survives，但：

\[
R_{23}=0.4<1.
\]

Layer I dead。

### State C

\[
(P_1,P_2,P_3,Q_0)=(456,292,2907,2957).
\]

\[
C_2=73,
\quad
C_3=969,
\]

\[
\rho=73/9690<0.1.
\]

Layer C dead。

因此现有三个 exact-word/Smith regression survivor中：

- 2 个死于 continuous layer；
- 1 个死于 integer layer；
- 没有进入 Layer P。

这不是 proof，但非常支持 C \(\to\) I \(\to\) P hierarchy。

---

# 55. Computational Regression

本轮使用 exact integer/Fraction regression 脚本：

`strict_layer_A1_SRCU_regression.py`

仅用于：

1. B3 residual divisor subsumption 的 primewise regression；
2. DUAL identity regression；
3. exact Möbius endpoint convention；
4. known synchronized states radial census；
5. known \(g=0\) family前若干项的 continuous-dead classification。

所有 nonexistence theorem均不依赖有限计算。

**状态：COMPUTATIONAL REGRESSION ONLY.**

---

# 56. Killed Conjecture — \(\sigma\) Directly Controls \(\rho\)

prompt 中一个核心希望是：

\[
\sigma\approx1,10
\]

结合 \(R\)-sign 把 \(\rho\) 推向 cone boundary。

但：

\[
\rho
=
\frac{P_2}{\sigma10^{2g+k}P_3}
\]

代入：

\[
P_2=vM,
\quad
P_3=\alpha tN,
\quad
\sigma=v/(\alpha t10^{n_3-d}),
\]

严格得到：

\[
\rho=\frac MN10^{n_3-n_2}.
\]

所以：

\[
\boxed{
\textbf{all explicit }\sigma\textbf{ dependence cancels.}
}
\]

结论：

\[
\boxed{
\text{d=0/1 boundary attack requires a new constraint on }M/N,
\text{ not stronger control of }\sigma.
}
\]

**状态：DISPROVED AS DIRECT ROUTE.**

---

# 57. Killed Conjecture — DUAL Magnitude Alone Closes Smith-Poor

DUAL 确实使：

\[
\gcd(b_2,b_3)\text{ small}
\]

对应：

\[
\operatorname{lcm}(g_2,g_3)\text{ large}.
\]

但 large lcm中：

\[
v\alpha t
\]

从 radial endpoints里 exact cancel。

所以除非能够证明 candidate integers在 interval 的**位置**恰被这些 prime classes覆盖，否则：

\[
\boxed{
\text{large }\operatorname{lcm}(g_2,g_3)
\text{ alone does not imply }N_V=0.
}
\]

\(U=1\) 是最直接 obstruction。

**状态：FAILED AS STANDALONE MAGNITUDE ROUTE.**

---

# 58. Killed Conjecture — B3DIV Materially Enlarges Smith-Rich

虽然：

\[
B_3^\sharp\mid H
\]

为真，但：

\[
B_3^\sharp\mid M_H^{(2)}.
\]

所以：

\[
\operatorname{lcm}(M_H^{(2)},B_3^\sharp)=M_H^{(2)}.
\]

真正新增的最大 factor 来自：

\[
h_T^\sharp,
\]

而不是 B3 residual。

**状态：DISPROVED AS NEW-STRENGTHENING CLAIM.**

---

# 59. Smith-Rich Status

本轮 strongest exact chain：

\[
\boxed{
H=\mathcal M_{\max}q,
}
\]

\[
\boxed{
\alpha t(M10^{n_3}+N)
=Q_0+\alpha Jh_T^\sharp q.
}
\]

\[
\boxed{
(P_1)^2+(vM)^2+(\alpha tN)^2=Q_0^2.
}
\]

若 \(q\) finite，则 residual offset finite；但 \(M,N,P_1,u_0\) 仍移动。

所以 Smith-rich 已到：

\[
\boxed{
\textbf{finite defect offset × moving two-scale radial state}
}
\]

而不是 finite state。

**状态：STRUCTURALLY REDUCED / OPEN.**

---

# 60. Smith-Poor Status

Smith-poor 通过 DUAL 被翻译为：

\[
\boxed{
\textbf{large complementary unit modulus}
}
\]

但 exact positional covering尚缺。

当前不能证明：

\[
\boxed{
\text{every integer in }I_{23}
\text{ shares a prime with }V.
}
\]

也不能证明一个 height-independent Jacobsthal gap足以覆盖，因为 factorization可移动且 \(U=1\) 无法由 prime density排除。

**状态：OPEN.**

---

# 61. \(g\ge1\) Unified Status

本轮没有得到：

\[
\boxed{
g\ge1\Longrightarrow N_V(I_{23})=0.}
\]

原因并非 transition 常数不足，而是 canonical cancellation 后，所有 branch最终都共享同一个 remaining semantic：

\[
\boxed{
U/u_0\in K_{MN}
\text{ with }U\in(\mathbf Z/V\mathbf Z)^\times.
}
\]

现有 word arithmetic主要约束：

- finite defect offset；
- \(M\widehat R\) affine term；
- \(JZ\)；
- Smith divisors；

但尚未形成一个对 \(M/N\) 和 unit-successor位置的 universal exclusion。

---

# 62. \(g=0\) Status

known infinite word/Smith pseudo-family被 RNF 统一解释为 Layer C dead。

但这只证明**该 family**与若干固定 profile，不是 global \(g=0\) theorem。

因此：

\[
\boxed{g=0\text{ remains globally OPEN}.}
\]

不过本轮说明 future \(g=0\) 不应再开 broad backward campaign；应直接在 \((u_0,M,N)\) chart 做 SRUS。

---

# 63. Exact A1-SRCU Equivalence After Smith Reduction

原 A1-SRCU：

\[
\exists U\in I_{23}\cap\mathbf Z_{>0},
\quad
\gcd(U,V)=1.
\]

由 KMN 与 VFACT，严格等价于：

\[
\boxed{
\exists U\in\mathbf Z_{>0}:
\frac U{u_0}\in K_{MN},
\quad
\gcd(U,s\beta u_0v\alpha t)=1.
}
\tag{SRUS-EQ}
\]

这就是：

## A1-SRUS — Smith-Reduced Unit-Successor Exclusion

证明 SRUS-EQ 对任何 exact synchronized A1 Smith state均不成立。

若 A1-SRUS 成立，则：

\[
\boxed{A_1=\varnothing.}
\]

结合 DD closure：

\[
\boxed{\textbf{Strict Layer CLOSED}.}
\]

但本轮 A1-SRUS 尚未证明。

---

# 64. Why This Frontier Is Strictly Smaller Than Original A1-SRCU

原始 state 仍显式携带：

\[
(C_2,C_3,g_2,g_3,b_2,b_3,V,\rho,\tau,\sigma).
\]

full Smith cancellation 后，radial gate只需：

\[
\boxed{(u_0,M,N;n_2,n_3)}
\]

加 transverse modulus：

\[
\boxed{s\beta v\alpha t.}
\]

同时 exact-word core通过：

\[
\boxed{
\widehat R,
J,
q,
\mathcal M_{\max},
S_3
}
\]

限制 \((M,N)\) 与 primitive sphere。

所以 remaining theorem不是“所有原变量的 coprime successor”，而是一个真正的：

\[
\boxed{
\textbf{two-coordinate decimal interval}
\times
\textbf{prescribed denominator}
\times
\textbf{unit numerator exclusion}.
}
\]

---

# 65. Exact Minimal Frontier if A1 Remains Open

本轮建议只保留一个 global theorem：

## A1-SRUS — Smith-Reduced Unit-Successor Exclusion

**Hypotheses.** 一个 exact synchronized A1 state满足所有 frozen sphere/master/DES/Smith conditions，并写成：

\[
P_2=vM,
\quad
P_3=\alpha tN,
\quad
u_0\mid M,N,
\]

\[
V=s\beta u_0v\alpha t.
\]

**Claim.** 不存在 \(U\in\mathbf Z_{>0}\) 满足：

\[
\max\left(\frac{10^{n_2-1}}M,\frac{10^{n_3-1}}N\right)
\le
\frac U{u_0}
<
\min\left(\frac{10^{n_2}}M,\frac{10^{n_3}}N\right),
\]

以及：

\[
\gcd(U,s\beta u_0v\alpha t)=1.
\]

这是当前 A1 的 exact terminal theorem。

---

# 66. At Most Three Next-Round Targets

若下一轮继续，不建议再次做 broad campaign；只建议：

### Target 1 — Resonant Reduced-Fraction Unit Exclusion

在：

\[
\alpha=t=1,
\quad
v=10^{n_3},
\quad
S_3=JZ,
\quad
J=L_R>1
\]

和 resonant 2-adic trichotomy 下，证明：

\[
U/u_0\notin K^{\rm res}_{MN}
\]

for every \(V\)-unit numerator U。

**优先级：最高。**

### Target 2 — Transition Affine Unit-Successor Exclusion

只研究：

\[
d=0,1,
\]

用：

\[
S_3=\alpha Jh_T^\sharp q-M\widehat R
\]

与 finite \(q\)/carry，直接控制：

\[
M/N
\]

而不是再控制 \(\sigma\)。

**优先级：第二。**

### Target 3 — Smith-Poor Positional Unit Cover

仅在 Layer P genuinely出现后，证明某个 exact short interval 中的每个整数被：

\[
s\beta v\alpha t
\]

的 prime support覆盖。

禁止 probabilistic density；必须是 exact residue/floor theorem。

**优先级：第三。**

---

# 67. PROVED / DERIVED / FAILED / OPEN Ledger

## FROZEN

- DD closed；
- Strict frontier = A1-only；
- primitive sphere；
- exact GSYNC/master；
- DES；
- branch map；
- full Smith chart；
- common-\(U\) forward reconstruction；
- backward radial redundancy；
- latest iterated Smith factorization。

## NEW PROVED

1. Radial Normal Form：
   \[
   I_{23}=\tau J(\rho).
   \]
2. continuous criterion：
   \[
   0.1<\rho<10.
   \]
3. exact width formulas。
4. radial lattice spacing \(1/\tau\)。
5. normalized integer margins。
6. \(\sigma=\beta_3/\beta_2\in(0.1,10)\)。
7. \(\sigma=g_2/(10^{n_3-d}g_3)\)。
8. RHO3。
9. TAU。
10. full Smith gcd profile：
    \[
    g_2=u_0v,
    \quad
    g_3=u_0\alpha t.
    \]
11. \(u_0=\gcd(g_2,g_3)\)。
12. Smith-radial cancellation：
    \[
    C_2=M/u_0,
    \quad C_3=N/u_0.
    \]
13. canonical radial coordinates：
    \[
    \rho=(M/N)10^{n_3-n_2},
    \quad
    \tau=u_0 10^{n_3}/N.
    \]
14. \(I_{23}=u_0K_{MN}\)。
15. prescribed-denominator reduced fraction：
    \[
    a_2/M=a_3/N=U/u_0.
    \]
16. V factorization：
    \[
    V=s\beta u_0v\alpha t.
    \]
17. CROSS。
18. \(b_3\mid10^{m_3}H\)。
19. \(B_3^\sharp\mid H\)。
20. B3 divisor is subsumed by latest \(M_H^{(2)}\)。
21. \(h_T^\sharp\mid Z\)。
22. strongest defect divisor：
    \[
    \mathcal M_{\max}=s\alpha\beta^\sharp v^\sharp h_T^\sharp\mid H.
    \]
23. \(G_T^\sharp=v^\sharp h_T^\sharp\)。
24. Smith/GCD duality：
    \[
    \gcd(b_i,b_j)\operatorname{lcm}(g_i,g_j)=V.
    \]
25. fixed-q affine radial formula。
26. resonance full Smith-radial normal form。
27. \(J=L_R\) identification。
28. slack identity。
29. exact A1-SRCU \(\Longleftrightarrow\) A1-SRUS equivalence。

## DERIVED

- rich chamber finite q;
- d=1 plus exact \(\sigma>960/101\);
- resonance U is decimal unit;
- resonance primitive ratio bound is exactly one decade too weak on each side;
- outer d should be organized by projective decade shift, not \(\tau\)-size.

## COMPUTATIONAL EVIDENCE

- B3 subsumption regression;
- DUAL regression;
- endpoint count regression;
- three known Double-Smith states classify as C/I/C;
- first several members of known \(g=0\) infinite family classify as C.

## DISPROVED / FAILED AS ROUTES

1. pure exact-word alone closes A1；
2. uniform bounded \(q_H\)；
3. \(B_3^\sharp\) materially enlarges latest defect divisor；
4. \(R\)-sign / \(\sigma\) alone controls \(\rho\)-side；
5. d=1 plus near-\(\sigma=10\) alone pushes \(\rho\to0.1\)；
6. “\(d\) only scales \(\tau\)” after full Smith reduction；
7. DUAL magnitude alone closes Smith-poor；
8. large V-radical / probabilistic coprime scarcity as proof；
9. finite q automatically finite-izes radial state。

## OPEN

1. resonance SRCU closure；
2. d=0 closure；
3. d=1 closure；
4. general g≥1 SRCU；
5. general g=0 SRCU；
6. A1-SRUS；
7. \(A_1=\varnothing\)；
8. Strict Layer closure。

---

# 68. Final Verdict

本轮达到并超过最低成功标准：

\[
\boxed{
\textbf{A1 Radial Normal Form proved.}
}
\]

\[
\boxed{
\textbf{B3 residual divisor decided: TRUE.}
}
\]

\[
\boxed{
\textbf{Smith-reduced exact-word state }
\to
\textbf{ explicit SRCU chamber.}
}
\]

更重要的是，本轮发现了一个 prompt 未预期的进一步消元：

\[
\boxed{
\textbf{Full Smith–Radial Cancellation.}
}
\]

它把真正 common-\(U\) geometry 从：

\[
(g_2,g_3,P_2,P_3,\sigma,\rho,\tau)
\]

压到：

\[
\boxed{
(u_0,M,N)
}
\]

并把其余 Smith factors全部移入 unit sieve。

因此当前最准确的 terminal architecture 已经是：

\[
\boxed{
\textbf{Double Smith--Euclidean Core}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\textbf{restricted }(u_0,M,N)\textbf{ primitive state}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\textbf{prescribed-denominator reduced-fraction interval}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\textbf{transverse unit-successor exclusion}.
}
\]

A1 尚未闭合；但“还需继续研究 SRCU”已经不再是准确描述。

当前唯一推荐的 global theorem 应冻结为：

\[
\boxed{
\textbf{A1-SRUS — Smith-Reduced Unit-Successor Exclusion.}
}
\]

一旦证明它：

\[
\boxed{A_1=\varnothing}
\]

并结合：

\[
\boxed{DD=\varnothing}
\]

即可得到：

\[
\boxed{\textbf{Strict Layer CLOSED}.}
\]

但截至本报告，不能诚实宣称该最终 closure 已完成。
