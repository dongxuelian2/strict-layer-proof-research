# 三项十进制拼接平方和问题：A1 Generic Primitive-Defect Synchronization Campaign

**文件名：** `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`  
**研究范围：** Strict Layer 正向线，仅研究 `A1-only`；DD 保持 closed。  
**本轮最终等级：**

\[
\boxed{\textbf{LEVEL 5 ACHIEVED — PRIMITIVE SYNCHRONIZATION INSUFFICIENCY CERTIFICATE}}
\]

同时得到一组新的、严格的 digit-to-primitive height 压缩定理。A1 **尚未闭合**，但本轮对 frontier 的判断发生了实质变化：

\[
\boxed{
\text{GSYNC 本身不是“偶然的 prime synchronization”；它就是十进制 split/carry balance 的 primitive 投影。}
}
\]

而且 primitive sphere + exact GSYNC + exact common-\(V\) gcd profile + denominator digit semantics **仍存在显式无限伪族**。真正缺失的最小 forward semantic gate 是：

\[
\boxed{
\textbf{同一个 numerator scale }U\textbf{ 必须同时把 }C_i=P_i/g_i\textbf{ 放入真实 digit windows。}
}
\]

这把下一轮最自然的正向目标从“继续追 prime support”改写成：

\[
\boxed{
\textbf{Primitive Conic}\times\textbf{Common-Scale Digit Window Synchronization}.
}
\]

---

# 1. Executive Summary

本轮得到四个核心结果。

## 1.1 PROVED — defect synchronization 是 exact decimal split identity

令

\[
Q_{12}:=b_1 10^{m_2}+b_2,
\qquad
\mathcal R:=\frac{A}{B}=\frac{UQ_0}{V},
\]

并在 A1 中写

\[
X_{12}:=a_1 10^{m_2+k},
\qquad
X_3:=a_2 10^{n_3}+a_3.
\]

由于

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g,
\]

完整 numerator / denominator words 恰可分裂成

\[
A=10^{m_3}X_{12}+X_3,
\]

\[
B=10^{m_3}Q_{12}+b_3.
\]

定义 word-visible defects

\[
\boxed{
\delta_{12}:=X_{12}-\mathcal RQ_{12},
}
\]

\[
\boxed{
\delta_3:=X_3-\mathcal Rb_3.
}
\]

则由 \(A=\mathcal RB\) **恒等地**得到

\[
\boxed{
\delta_3=-10^{m_3}\delta_{12}.
}
\tag{DS-WORD}
\]

另一方面 primitive normalization

\[
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}
\]

给出

\[
\boxed{
\delta_{12}
=
\frac{U}{g_1g_2}\Delta_{12},
}
\tag{DS-12}
\]

\[
\boxed{
\delta_3
=
\frac{U}{g_2g_3}\Delta_3.
}
\tag{DS-3}
\]

因此

\[
\delta_3=-10^{m_3}\delta_{12}
\iff
\boxed{
 g_1\Delta_3=-10^{m_3}g_3\Delta_{12}.
}
\]

也就是说，GSYNC 的纯 \(10^{m_3}\) ratio 不是一个外加的算术巧合；它正是**完整十进制 word 在第三 denominator block 处切开后，前后误差必须精确互相抵消**的 primitive 版本。

**状态：NEW PROVED.**

---

## 1.2 PROVED — 通用 Primitive Ratio Window 与平方根高度塌缩

对任意两个坐标 \(i,j\)，由

\[
\frac{P_i}{P_j}
=
\frac{a_i/b_i}{a_j/b_j}
=
\frac{a_i b_j}{a_j b_i}
\]

及 digit windows 得到粗但统一的

\[
\boxed{
10^{s_i-s_j-2}
<
\frac{P_i}{P_j}
<
10^{s_i-s_j+2},
}
\tag{PRW}
\]

其中 \(s_i=n_i-m_i\)。

在 A1 中

\[
s_2=g+k,
\qquad
s_3=-g,
\]

故

\[
\boxed{
10^{2g+k-2}
<
\frac{P_2}{P_3}
<
10^{2g+k+2}.
}
\tag{A1-PRW}
\]

因为 \(P_3\ge1\) 且 \(P_2<Q_0\)，立即得到

\[
\boxed{
10^{2g+k-2}<Q_0.
}
\tag{HC-1}
\]

由于 \(k\ge1\)，

\[
\boxed{
10^g<\sqrt{10Q_0}.
}
\tag{HC-2}
\]

这是本轮最强的 branch-independent height collapse。它把上一轮

\[
10^g<\frac{Q_0^3}{2}
\]

直接改善为平方根高度。

**状态：NEW PROVED.**

---

## 1.3 PROVED — minus branch 在 primitive/gcd 层存在显式无限 synchronized family

固定

\[
(g_1,g_2,g_3)=(24,4,3),
\]

\[
(m_2,n_3,k,g)=(1,1,1,0),
\]

故

\[
m_3=1,
\qquad
n_2=2,
\]

以及

\[
L_g=24,
\qquad
(h_1,h_2,h_3)=(1,6,8).
\]

此 profile 的 primitive master plane 为

\[
\boxed{
1000P_1+60P_2+8P_3=168Q_0.
}
\tag{P-PLANE}
\]

写

\[
P_1=24x,
\qquad
P_2=4y,
\qquad
P_3=3z,
\]

则 plane + sphere 化为

\[
\boxed{
1000x+10y+z=7q,
}
\tag{C-LIN}
\]

\[
\boxed{
576x^2+16y^2+9z^2=q^2.
}
\tag{C-SPH}
\]

这是一个 projective conic。

它至少有简单有理/整数点

\[
(x,y,z,q)=(1,13,53,169),
\]

对应

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169).
\]

更强地，第 14 节给出一条**显式无限 polynomial family**，其每个 primitive reduction 都满足：

- primitive sphere；
- exact GSYNC；
- \(D=P_1 10^k-Q_0>0\)；
- exact common-\(V\) profile \(V=24\)，即
  \[
  \gcd(24,P_1)=24,
  \quad
  \gcd(24,P_2)=4,
  \quad
  \gcd(24,P_3)=3;
  \]
- denominator blocks
  \[
  (b_1,b_2,b_3)=(1,6,8)
  \]
  的真实 one-digit legality；
- 固定 A1 exponent profile
  \[
  s_3=0,
  \qquad
  s_2+s_3=1;
  \]
- 且始终处于
  \[
  \boxed{\Delta_{12}<0,\quad\Delta_3>0.}
  \]

因此：

\[
\boxed{
\textbf{minus branch 不可能仅靠 primitive sphere + GSYNC + common-}V\textbf{ gcd profile + denominator digits 被消灭。}
}
\]

**状态：NEW PROVED NEGATIVE THEOREM / LEVEL-5 CERTIFICATE.**

---

## 1.4 PROVED — 该无限伪族恰好死在 common-\(U\) numerator digit window

上述 family 中始终有

\[
\boxed{C_3>C_2},
\qquad
C_i:=P_i/g_i.
\]

但固定 exponent profile 要求

\[
n_2=2,
\qquad
n_3=1.
\]

若存在同一个 \(U>0\) 实现 numerator blocks，则

\[
a_2=UC_2
\]

必须是两位数，而

\[
a_3=UC_3
\]

必须是一位数，所以必有

\[
a_2>a_3.
\]

这与 \(C_3>C_2\) 矛盾。

因此该 family 的**第一处必死 semantic gate**正是：

\[
\boxed{
\exists U\in\mathbf Z_{>0},\ \gcd(U,V)=1,
\quad
10^{n_i-1}\le UC_i<10^{n_i}\ \forall i.
}
\tag{DIG-U}
\]

这给出了本轮要求的“actual decimal word 在哪里提供最后缺失信息”的精确答案。

**状态：NEW PROVED.**

---

# 2. Frozen Proven Inputs

本轮冻结以下已审计结果，不重新证明：

1. Strict Layer 的剩余 frontier 只有 A1-only；
2. primitive sphere
   \[
   P_1^2+P_2^2+P_3^2=Q_0^2,
   \quad
   \gcd(P_1,P_2,P_3,Q_0)=1;
   \]
3. primitive normalization
   \[
   g_i=\gcd(V,P_i),
   \quad
   C_i=P_i/g_i,
   \quad
   a_i=UC_i,
   \quad
   b_i=V/g_i;
   \]
4. A1 relations
   \[
   g=m_3-n_3\ge0,
   \quad
   k=s_2+s_3\ge1,
   \]
   \[
   n_2=m_2+g+k,
   \quad
   m_3=n_3+g;
   \]
5. flat locus 已删除；
6. \(D=P_1 10^k-Q_0>0\)；
7. defects
   \[
   \Delta_{12}=g_2 10^{m_2}D-g_1Q_0,
   \]
   \[
   \Delta_3=g_3P_2 10^{n_3}-g_2(Q_0-P_3);
   \]
8. exact synchronization
   \[
   g_1\Delta_3=-10^{m_3}g_3\Delta_{12};
   \]
9. \(\Delta_{12}\Delta_3\ne0\)；
10. universal tail divisibility
    \[
    10^{n_3}\mid g_1g_2(Q_0-P_3);
    \]
11. previous sign-height bounds；
12. fixed primitive core \(\Rightarrow\) finite decimal fibre；
13. exact A1 terminal semantics仍需要真实 numerator word / cut / digit / reducedness / norm consistency。

### Source visibility note

本轮再次以精确文件名检索 `strict_layer_global_reduction_campaign.md`，File Library 仍未直接暴露其正文；因此本报告不伪称重新读取了它。所需的 SGR-1 facts 均由后续 `strict_layer_unified_exact_lift_campaign.md`、square-spacing、SGR-10B 及 A1 两轮报告中已经自包含重推或明确冻结的版本提供。

**状态：AUDITED SCOPE.**

---

# 3. Exact Defect Definitions and the Carry Dictionary

定义

\[
Q_{12}=b_1 10^{m_2}+b_2.
\]

A1 中

\[
A
=
 a_1 10^{n_2+n_3}
+a_2 10^{n_3}
+a_3.
\]

利用

\[
n_2+n_3
=
(m_2+k)+m_3,
\]

得到

\[
\boxed{
A
=10^{m_3}\bigl(a_1 10^{m_2+k}\bigr)
+igl(a_2 10^{n_3}+a_3\bigr).
}
\tag{3.1}
\]

同理

\[
\boxed{
B=10^{m_3}Q_{12}+b_3.
}
\tag{3.2}
\]

所以 \(\mathcal R=A/B\) 是两个 local carrier ratios 的正权平均：

\[
\mathcal R
=
\frac{
10^{m_3}Q_{12}
\left(\frac{a_1 10^{m_2+k}}{Q_{12}}\right)
+
 b_3
\left(\frac{a_2 10^{n_3}+a_3}{b_3}\right)
}{10^{m_3}Q_{12}+b_3}.
\tag{3.3}
\]

因此：

\[
\boxed{
\Delta_{12}>0
\iff
\frac{a_1 10^{m_2+k}}{Q_{12}}
>
\frac{a_2 10^{n_3}+a_3}{b_3},
}
\tag{3.4+}
\]

\[
\boxed{
\Delta_{12}<0
\iff
\frac{a_1 10^{m_2+k}}{Q_{12}}
<
\frac{a_2 10^{n_3}+a_3}{b_3}.
}
\tag{3.4-}
\]

也就是说两种 sign chamber 的真实含义不是“两个神秘 defect 的符号”，而是：

\[
\boxed{
\text{prefix carrier ratio 与 tail carrier ratio 的严格次序。}
}
\]

**状态：NEW PROVED INTERPRETATION.**

---

# 4. Sign-Chamber Audit

## 4.1 Plus branch

假设

\[
\Delta_{12}>0,
\qquad
\Delta_3<0.
\]

已有

\[
10^{n_3}<Q_0.
\]

本轮可明显加强。

由

\[
\Delta_3<0
\]

有

\[
g_3P_2 10^{n_3}<g_2(Q_0-P_3).
\]

注意

\[
\frac{g_3}{g_2}P_2
=
P_3\frac{C_2}{C_3}
=
P_3\frac{a_2}{a_3}.
\]

故

\[
P_3\frac{a_2}{a_3}10^{n_3}<Q_0-P_3.
\tag{4.1}
\]

真实 digit windows 给

\[
a_2\ge10^{n_2-1},
\qquad
 a_3<10^{n_3},
\]

所以

\[
\frac{a_2}{a_3}10^{n_3}>10^{n_2-1}.
\]

代回：

\[
\boxed{
P_3\bigl(1+10^{n_2-1}\bigr)<Q_0.
}
\tag{PLUS-P3}
\]

特别

\[
\boxed{
10^{n_2-1}<Q_0-1.
}
\tag{PLUS-n2}
\]

即

\[
\boxed{
10^{m_2+g+k-1}<Q_0-1.
}
\tag{PLUS-product}
\]

因此

\[
\boxed{
10^g<\frac{Q_0-1}{10^{m_2+k-1}}
\le\frac{Q_0-1}{10}.
}
\tag{PLUS-g}
\]

再与旧

\[
10^{n_3}<Q_0
\]

合并：

\[
\boxed{
10^{m_3}
=10^{n_3+g}
<\frac{Q_0(Q_0-1)}{10}
<\frac{Q_0^2}{10}.
}
\tag{PLUS-m3}
\]

这把旧 plus bound

\[
10^{m_3}<Q_0^3/2
\]

再改善一个完整的 \(Q_0\) 次数。

**状态：NEW PROVED.**

### Plus branch status

尚未得到 contradiction。

但 plus branch 已被压到同时满足：

\[
10^{n_2-1}<Q_0,
\qquad
10^{n_3}<Q_0,
\qquad
10^{2g+k-2}<Q_0.
\]

它比 minus branch 更像一个适合继续做 pure digit-cone / Archimedean exclusion 的区域。

**状态：OPEN, STRONGLY COMPRESSED.**

---

## 4.2 Minus branch

假设

\[
\Delta_{12}<0,
\qquad
\Delta_3>0.
\]

同样从

\[
\frac{\Delta_3}{g_2}
=
P_3\frac{a_2}{a_3}10^{n_3}-(Q_0-P_3)
>0
\]

得到

\[
\frac{Q_0}{P_3}
<
1+\frac{a_2}{a_3}10^{n_3}.
\]

利用精确 digit endpoint

\[
a_2\le10^{n_2}-1,
\qquad
 a_3\ge10^{n_3-1},
\]

有

\[
1+\frac{a_2}{a_3}10^{n_3}
\le
1+10(10^{n_2}-1)
=
10^{n_2+1}-9
<10^{n_2+1}.
\]

故

\[
\boxed{
\frac{Q_0}{P_3}<10^{n_2+1}.
}
\tag{MINUS-QP3}
\]

又由 Primitive Ratio Window：

\[
10^{2g+k-2}<\frac{P_2}{P_3}<\frac{Q_0}{P_3},
\]

所以

\[
2g+k-2<n_2+1=m_2+g+k+1.
\]

即

\[
\boxed{g-m_2<3.}
\]

因 \(g,m_2\in\mathbf Z\)：

\[
\boxed{g\le m_2+2.}
\tag{MINUS-rel}
\]

**状态：NEW PROVED.**

### Minus branch status

本轮没有消灭 minus branch；相反，第 14 节证明 minus branch 在 primitive/gcd 层存在显式无限 synchronized family。

因此：

\[
\boxed{
\textbf{minus branch 的下一步必须使用 common-}U\textbf{ digit realization 或更深 exact semantics。}
}
\]

---

# 5. Defect Magnitude Analysis

定义

\[
A_*:=|g_1\Delta_3|,
\qquad
B_*:=|g_3\Delta_{12}|.
\]

GSYNC 给

\[
A_*=10^{m_3}B_*.
\]

本轮对 pure magnitude route 的裁决是：

\[
\boxed{\textbf{FAILED AS A PRIMITIVE-ONLY CLOSURE ROUTE}.}
\]

原因不是“暂时没找到好界”，而是第 14 节构造了一条 fixed-profile infinite family，其上

\[
m_3=1,
\qquad
\frac{A_*}{B_*}=10
\]

对所有参数**精确恒成立**，同时 primitive height 无界。

因此任何声称

\[
\frac{A_*}{B_*}\notin10^{\mathbf Z}
\]

仅由 primitive sphere + gcd profile + fixed exponent profile 推出的 theorem 都是假的。

真正可用的 magnitude information 必须来自：

- common-\(U\) digit window；
- exact numerator word/cut；
- reducedness 与 norm feedback；
- 或其他尚未被 GSYNC 吸收的 semantic condition。

**状态：PROVED NEGATIVE RESULT.**

---

# 6. (2,5)-adic Gap Analysis

定义

\[
\Gamma_2
:=v_2(g_1\Delta_3)-v_2(g_3\Delta_{12}),
\]

\[
\Gamma_5
:=v_5(g_1\Delta_3)-v_5(g_3\Delta_{12}).
\]

对 exact GSYNC state，当然有

\[
\Gamma_2=
\Gamma_5=m_3.
\]

本轮的新判断是：

\[
\boxed{
\textbf{“证明 }\Gamma_2\ne\Gamma_5\textbf{”不能被当成一个独立 primitive-master target。}
}
\]

原因有两层。

### 第一层：形式冗余

GSYNC 与 word split identity 等价。一旦 primitive master equation 成立，equal gap 已经是代数后果。

### 第二层：显式反例压力

第 14 节 family 上

\[
\Delta_{12}=-64E_s,
\qquad
\Delta_3=80E_s,
\]

从而

\[
g_1\Delta_3=1920E_s,
\qquad
 g_3|\Delta_{12}|=192E_s,
\]

所以

\[
\Gamma_2=\Gamma_5=1
\]

沿无限 family 恒成立。

因此 equal-gap route 只有在加入一个**外部于 GSYNC 的 gate**后才可能重新产生内容，例如：

\[
\text{digit interval}
\to
\text{forced }v_2/v_5\text{ profile}
\to
\text{contradiction}.
\]

**状态：FAILED AS STANDALONE ROUTE; RECLASSIFIED AS A CONSEQUENCE / FILTER.**

---

# 7. Non-Decimal Support Synchronization

同理，

\[
\operatorname{core}_{10}(g_1\Delta_3)
=
\operatorname{core}_{10}(g_3\Delta_{12})
\]

是 GSYNC 的直接投影。

第 14 节 family 更具体地给出：

\[
\Delta_{12}=-64E_s,
\qquad
\Delta_3=80E_s,
\]

所以两个 defects 的全部 nondecimal core 本身就是同一个 \(\operatorname{core}_{10}(E_s)\)。

因此以下过强猜想均被**显式否定**：

1. “两个 defects 必有一个 nondecimal private prime”；
2. “共同 nondecimal support 只能落在有限 exceptional locus”；
3. “\(\gcd(\Delta_{12},\Delta_3)\) 的 ten-free part 一定很小”；
4. “\(\Sigma_{\log}>0\) 可由 primitive geometry 统一推出”。

在该 family 中

\[
\boxed{
\gcd(\Delta_{12},\Delta_3)=16E_s,
}
\]

其大小随 primitive height 增长。

**状态：FAILED AS UNIFORM PRIMITIVE OBSTRUCTION.**

---

# 8. gcd / Cross-Divisibility Analysis

从

\[
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}
\]

令

\[
d_{13}:=\gcd(g_1,g_3),
\qquad
 g_1=d_{13}u,
\quad
 g_3=d_{13}v,
\quad
\gcd(u,v)=1.
\]

则

\[
u\Delta_3=-10^{m_3}v\Delta_{12}.
\]

因此严格有：

\[
\boxed{v\mid\Delta_3,}
\]

以及若 \(u^{\langle10\rangle}\) 表示去掉 \(2,5\) 的部分，

\[
\boxed{u^{\langle10\rangle}\mid\Delta_{12}.}
\]

这与上一轮 cross-divisibility 一致。

但本轮 family 表明：这类 divisibility 不能自动转成 contradiction。固定

\[
(g_1,g_3)=(24,3)
\]

时

\[
u=8,
\quad
v=1,
\]

而

\[
\Delta_{12}=-64E_s
\]

精确吸收全部需求。

**状态：PROVED NECESSARY; INSUFFICIENT FOR CLOSURE.**

---

# 9. Primitive Sphere Coupling

本轮最重要的 primitive-sphere 新接口不是新的 congruence，而是 **ratio window**。

## 9.1 General Primitive Ratio Window

对任意 \(i,j\)：

\[
\boxed{
\frac{10^{n_i-1}10^{m_j-1}}
{(10^{n_j}-1)(10^{m_i}-1)}
\le
\frac{P_i}{P_j}
\le
\frac{(10^{n_i}-1)(10^{m_j}-1)}
{10^{n_j-1}10^{m_i-1}}.
}
\tag{PRW-exact}
\]

粗化即得到 (PRW)。

这说明 decimal carrier profile 不是仅仅作用在 word 层；它在 primitive sphere 上直接切出一个 projective cone。

## 9.2 A1 projective cone

A1 中

\[
\frac{P_2}{P_3}\asymp 10^{2g+k}
\]

（误差最多两个十进制数量级）。

因此任何

\[
g\to\infty
\]

的 A1 sequence 必有

\[
\boxed{
\frac{P_3}{P_2}\to0.
}
\]

所以 projective compactness 若要使用，正确的 boundary 不是上一轮已删除的 flat locus，而首先是 primitive sphere 的 coordinate face

\[
\boxed{x_3=0.}
\]

**状态：NEW PROVED ASYMPTOTIC GEOMETRY.**

---

# 10. \(Q_0-P_3\) Factor Geometry

仍有

\[
(Q_0-P_3)(Q_0+P_3)=P_1^2+P_2^2.
\]

本轮对 Gaussian / \(3\bmod4\) prime 路线没有发现新的 universal contradiction。

原因更明确了：

- GSYNC plane 与 sphere 可以形成有理 conic；
- 第 14 节 family 已经在 common-\(V\) gcd semantics 下提供无界 primitive states；
- 这些 states 并不需要 \(Q_0-P_3\) 的 nondecimal support 出现不一致。

因此：

\[
\boxed{
\text{普通 Gaussian support / sum-of-two-squares 不能作为 generic synchronization closure。}
}
\]

它若未来重新有用，必须读取 **同一个 actual digit/cut state** 产生的额外 norm information，而不是只读取

\[
P_1^2+P_2^2=(Q_0-P_3)(Q_0+P_3).
\]

**状态：FAILED AS STANDALONE; CONSISTENT WITH PREVIOUS AUDITS.**

---

# 11. Decimal / Carry Interpretation

本轮得到一个比 valuation 更直接的解释。

设

\[
r_{12}:=\frac{a_1 10^{m_2+k}}{Q_{12}},
\qquad
r_3^{\rm tail}:=\frac{a_2 10^{n_3}+a_3}{b_3}.
\]

则

\[
\mathcal R
=
\frac{10^{m_3}Q_{12}\,r_{12}+b_3r_3^{\rm tail}}
{10^{m_3}Q_{12}+b_3}.
\]

所以 \(\mathcal R\) 只是这两个 local ratios 的 exact weighted average。

因此：

- plus branch = prefix local ratio 在上、tail local ratio 在下；
- minus branch = tail local ratio 在上、prefix local ratio 在下；
- GSYNC = weighted-average cancellation 的整数化版本。

这直接解释了为什么

\[
\frac{-g_1\Delta_3}{g_3\Delta_{12}}
\]

会恰好是 \(10^{m_3}\)：

\[
\boxed{
\text{它就是两个 block 在完整 word 中相隔 }m_3\text{ 个十进制位的 place-value 权重。}
}
\]

所以 “为什么 ratio 恰好是纯 \(10\) 幂？” 的答案是：

> **在 master-equation 层，它必须如此；真正需要证明的是为什么一个同时满足 sphere、gcd、digit、cut、norm 的 state 不能实现这种 carry balance。**

**状态：NEW STRUCTURAL ANSWER / PROVED.**

---

# 12. Common-Scale Digit Realization Gate

定义

\[
C_i:=P_i/g_i.
\]

真实 numerator scale 必须存在同一个

\[
U\in\mathbf Z_{>0},
\qquad
\gcd(U,V)=1,
\]

使

\[
10^{n_i-1}\le UC_i<10^{n_i}
\qquad(i=1,2,3).
\]

等价于

\[
\boxed{
U\in
I_{\rm num}
:=
\bigcap_{i=1}^3
\left[
\frac{10^{n_i-1}}{C_i},
\frac{10^{n_i}}{C_i}
\right)
}
\tag{DIG-I}
\]

且该交集内存在与 \(V\) 互素的整数。

这是一个非常小、但此前 primitive-defect 坐标中被投影掉的 semantic gate。

它产生两类约束：

1. **projective ratio constraints**：\(C_i/C_j\) 必须落入由 \(n_i-n_j\) 决定的窄 cone；
2. **integer-scale constraints**：这些区间的公共交还必须真正包含同一个整数 \(U\)，并满足 \(\gcd(U,V)=1\)。

本轮显式 pseudo-family 在第一层已经死亡，因此无需进入 actual prefix cut。

这给正向线和反向线一个非常干净的 anti-duplication 分界：

- 正向线下一步可以只研究 \(I_{\rm num}\) / projective digit cone；
- 反向线继续研究 actual cut + same-cut norm / residual phase。

**状态：NEW MINIMAL INTERFACE.**

---

# 13. Fixed-Profile Conic Geometry

固定

\[
(g_1,g_2,g_3;m_2,n_3,k,g).
\]

于是

\[
h_i=L_g/g_i,
\qquad
n_2=m_2+g+k,
\qquad
m_3=n_3+g
\]

全部固定。

primitive master equation 是 \((P_1,P_2,P_3,Q_0)\) 的 homogeneous linear equation：

\[
\boxed{
 h_1 10^{n_2+n_3}P_1
+h_2 10^{n_3}P_2
+h_3P_3
=
KQ_0,
}
\tag{13.1}
\]

其中

\[
K
:=
 h_1 10^{m_2+m_3}
+h_2 10^{m_3}
+h_3.
\]

与 sphere

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

相交，在 projective \(\mathbf P^3\) 中得到一个 plane conic（可能退化）。

若该 conic 非退化且含一个 rational point，则过该点作 rational-slope lines 即给出 rational parametrization，因此有无限 rational points。

所以：

\[
\boxed{
\textbf{固定 profile 后，GSYNC 并不天然把 primitive core 离散化；它通常只是把 sphere 降成一条 conic。}
}
\]

这解释了为什么把 synchronization 当作“极低概率 prime coincidence”会误判其几何规模。

**状态：NEW PROVED GEOMETRIC REDUCTION.**

---

# 14. Explicit Infinite Ambient / Pseudo-Family

这是本轮最关键的 falsification theorem。

## 14.1 Fixed profile

固定

\[
V=24,
\]

\[
(g_1,g_2,g_3)=(24,4,3),
\]

故

\[
(b_1,b_2,b_3)=\left(\frac{24}{24},\frac{24}{4},\frac{24}{3}\right)=(1,6,8).
\]

固定

\[
(m_2,n_3,k,g)=(1,1,1,0),
\]

所以

\[
(m_3,n_2)=(1,2).
\]

这确实是 formal A1 profile：

\[
s_3=n_3-m_3=0,
\]

\[
s_2=n_2-m_2=1,
\]

\[
s_2+s_3=1>0.
\]

---

## 14.2 Polynomial conic family

对任意整数 \(t\ge0\)，定义

\[
X_t
=
3{,}553{,}056t^2
+160{,}341t
+1{,}809,
\]

\[
Y_t
=
44{,}000{,}352t^2
+2{,}018{,}892t
+23{,}153,
\]

\[
Z_t
=
188{,}129{,}520t^2
+8{,}492{,}928t
+95{,}849,
\]

\[
Q_t
=
597{,}312{,}720t^2
+27{,}003{,}264t
+305{,}197.
\]

直接展开可验证两个 polynomial identities：

\[
\boxed{
1000X_t+10Y_t+Z_t=7Q_t,
}
\tag{14.1}
\]

\[
\boxed{
576X_t^2+16Y_t^2+9Z_t^2=Q_t^2.
}
\tag{14.2}
\]

令

\[
d_t:=\gcd(X_t,Y_t,Z_t,Q_t),
\]

并定义

\[
x_t=X_t/d_t,
\quad
y_t=Y_t/d_t,
\quad
z_t=Z_t/d_t,
\quad
q_t=Q_t/d_t.
\]

注意：

- \(Y_t,Z_t,Q_t\) 恒为奇数，因此 \(d_t\) 为奇数；
- \(Y_t\equiv2\pmod3\)，因此 \(3\nmid d_t\) 且 \(3\nmid y_t\)；
- \(z_t\) 为奇数。

定义

\[
\boxed{
P_1=24x_t,
\quad
P_2=4y_t,
\quad
P_3=3z_t,
\quad
Q_0=q_t.
}
\tag{14.3}
\]

则 (14.2) 给 primitive sphere。

而 primitive gcd 也成立：

- 公因子 \(2\) 不可能，因为 \(P_3,q_t\) 为奇；
- 公因子 \(3\) 不可能，因为 \(P_2=4y_t\) 且 \(3\nmid y_t\)；
- 任意 \(p\ge5\) 若同时整除四坐标，则会同时整除 \(x_t,y_t,z_t,q_t\)，与其 primitive 定义矛盾。

因此

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

---

## 14.3 Exact common-\(V\) gcd profile

由上述 parity / mod-3 facts：

\[
\gcd(24,P_1)=24,
\]

\[
\gcd(24,P_2)
=4\gcd(6,y_t)=4,
\]

\[
\gcd(24,P_3)
=3\gcd(8,z_t)=3.
\]

所以

\[
\boxed{
(g_1,g_2,g_3)=(24,4,3)
}
\]

不是形式上指定的假 profile，而是真正由同一个 \(V=24\) 实现。

**状态：PROVED.**

---

## 14.4 Exact GSYNC and fixed minus sign

定义

\[
E_t:=Q_t-150X_t.
\]

直接化简：

\[
\boxed{
E_t
=
64{,}354{,}320t^2
+2{,}952{,}114t
+33{,}847
>0.
}
\tag{14.4}
\]

同时

\[
240X_t-Q_t
=
255{,}420{,}720t^2
+11{,}478{,}576t
+128{,}963
>0,
\]

所以

\[
D=P_1 10-Q_0>0.
\]

在 primitive reduction 后仍写

\[
e_t:=E_t/d_t>0.
\]

则直接得到

\[
\boxed{
\Delta_{12}=-64e_t,
}
\tag{14.5}
\]

\[
\boxed{
\Delta_3=80e_t.
}
\tag{14.6}
\]

因此

\[
\boxed{
24\Delta_3
=-10\cdot3\Delta_{12}.
}
\]

且对每个 \(t\)：

\[
\boxed{
\Delta_{12}<0,
\qquad
\Delta_3>0.
}
\]

这是一个**固定 sign、固定 gcd profile、固定 exponent profile 的 exact synchronized family**。

---

## 14.5 Family is genuinely infinite

比值

\[
Y_t/X_t
\]

不是常数 rational function，因此这些 projective conic points 不可能只取有限多个方向。

故 primitive reductions 给出无限多个不同 primitive sphere states；特别有一 subsequence 满足

\[
Q_0\to\infty.
\]

**状态：PROVED.**

---

## 14.6 Exact semantic failure: numerator digit order

直接有

\[
\boxed{
Z_t-Y_t
=
12(1167t+26)(10292t+233)>0.
}
\tag{14.7}
\]

所以

\[
z_t>y_t.
\]

即

\[
C_3>C_2.
\]

但 formal profile 要求

\[
n_2=2,
\qquad
 n_3=1.
\]

任何同一个 \(U>0\) 都保持大小次序：

\[
UC_3>UC_2.
\]

然而真实 digit windows 要求

\[
10\le a_2=UC_2\le99,
\]

\[
1\le a_3=UC_3\le9,
\]

于是必须 \(a_2>a_3\)，矛盾。

所以整个 family 都在

\[
\boxed{\textbf{Common-Scale Numerator Digit Gate}}
\]

处死亡。

这正是一个严格的 Level-5 insufficiency certificate。

---

# 15. Projective / Asymptotic Analysis

本轮 projective route 的结论分两部分。

## 15.1 DISPROVED — “任何 synchronized limit 都必须回到 flat locus”

第 14 节 family 的 leading coefficients 给

\[
\frac{E_t}{Q_t}
\to
\frac{64{,}354{,}320}{597{,}312{,}720}
\approx0.10774.
\]

因此 defects 在 primitive height normalization 后并不趋零；family 的 projective limit 是一个真正 non-flat synchronized point。

所以：

\[
\boxed{
\text{compactness limit }\Rightarrow\text{ flat locus}
}
\]

作为 universal strategy 是错误的。

**状态：FAILED / COUNTEREXAMPLE.**

## 15.2 PROVED — 若 \(g\to\infty\)，则趋向 \(P_3=0\) face

由 A1-PRW：

\[
\frac{P_3}{P_2}<10^{-2g-k+2}.
\]

故任何 \(g\to\infty\) sequence 都满足

\[
P_3/P_2\to0.
\]

同时 HC-2 又给

\[
g\le\frac12\log_{10}Q_0+O(1).
\]

所以真正 projective asymptotic split 是：

1. **bounded \(g\)**：fixed-profile conic 型 moving-core family 可以存在；
2. **unbounded \(g\)**：primitive direction 被压向 \(P_3=0\) face。

这比“generic vs flat”更适合下一阶段。

---

# 16. Computational Experiments

计算仅用于 falsification / structure discovery；所有最终 PROVED claims 都已被写成可手工核验的代数恒等式或 elementary inequalities。

## 16.1 Fixed one-digit profile scan

扫描：

- \(b_1,b_2,b_3\in\{1,\dots,9\}\)；
- \(V=\operatorname{lcm}(b_1,b_2,b_3)\)；
- fixed
  \[
  m_2=m_3=n_3=k=1,
  \quad g=0,
  \quad n_2=2;
  \]
- \(C_1\le100\)，\(C_2\le200\)；
- 对 \(C_3\) 使用 conic quadratic 的 exact discriminant-square 解，而不是近似搜索；
- 要求 common-\(V\) gcd profile、primitive sphere、\(D>0\)、GSYNC。

得到：

- plus branch hits：\(0\)；
- minus branch hits：\(3\)。

其中包括：

\[
(b_1,b_2,b_3)=(1,6,8),
\]

\[
(C_1,C_2,C_3,Q_0)=(1,13,53,169),
\]

以及

\[
(2,109,25,445),
\]

\[
(19,73,969,2957).
\]

**状态：EXPERIMENTAL.**

该 scan 不能证明 plus branch 为空；它只说明本轮发现的最自然 ambient synchronized geometry 明显偏向 minus branch。

---

# 17. Failed Conjectures / Route Verdicts

本轮主动测试并裁决如下。

## 17.1 “一个 sign branch 在 primitive 层必为空”

- minus branch：**FALSE**，第 14 节有无限 family；
- plus branch：仍 OPEN；有限实验未命中，但无证明。

## 17.2 “\(\Gamma_2\ne\Gamma_5\) 恒成立”

**FALSE**。第 14 节 family 上二者恒等于 \(1\)。

## 17.3 “两个 defects 必有 private nondecimal prime”

**FALSE**。family 中

\[
\Delta_{12}=-64E_t,
\qquad
\Delta_3=80E_t,
\]

nondecimal part 完全共享。

## 17.4 “\(\gcd(\Delta_{12},\Delta_3)\) 的 ten-free part 很小”

**FALSE**。family 中

\[
\gcd(\Delta_{12},\Delta_3)=16E_t
\]

无界。

## 17.5 “pure magnitude 可以排除 \(10^{m_3}\) ratio”

**FALSE**。family 上 ratio 恒为 \(10\)。

## 17.6 “projective limit 必退化到 flat locus”

**FALSE**。family 有 non-flat projective limit。

## 17.7 “ordinary Gaussian / norm support 足够”

**FAILED / INSUFFICIENT**，与前轮及 backward detached-prefix theorem 一致。

## 17.8 “primitive layer 完全没用，必须立即回 actual word”

**FALSE AS STATED**。本轮 Primitive Ratio Window 仍在 primitive/digit interface 上给出了

\[
10^g<\sqrt{10Q_0}
\]

这样的强新压缩。

正确判断是：

\[
\boxed{
\text{pure primitive algebra 不足；primitive geometry + minimal digit-scale interface 仍很有力。}
}
\]

---

# 18. New Proven Lemmas

本轮新增可冻结 theorem ledger：

### A1-GPDS-1 — Word/Primitive Defect Dictionary

\[
\delta_{12}=\frac{U}{g_1g_2}\Delta_{12},
\quad
\delta_3=\frac{U}{g_2g_3}\Delta_3,
\]

\[
\delta_3=-10^{m_3}\delta_{12}.
\]

**PROVED.**

### A1-GPDS-2 — Primitive Ratio Window

\[
10^{s_i-s_j-2}<P_i/P_j<10^{s_i-s_j+2}.
\]

**PROVED.**

### A1-GPDS-3 — A1 Square-Root Translation Height

\[
10^{2g+k-2}<Q_0,
\qquad
10^g<\sqrt{10Q_0}.
\]

**PROVED.**

### A1-GPDS-4 — Plus Tail-to-Prefix Digit Collapse

plus branch 中

\[
P_3(1+10^{n_2-1})<Q_0,
\]

\[
10^{n_2-1}<Q_0-1,
\]

\[
10^{m_3}<Q_0(Q_0-1)/10.
\]

**PROVED.**

### A1-GPDS-5 — Minus Relative Translation Bound

minus branch 中

\[
g\le m_2+2.
\]

**PROVED.**

### A1-GPDS-6 — Fixed-Profile Conic Principle

固定 gcd/exponent profile 后，primitive master + sphere 是 projective plane conic；nondegenerate rational-point case 具有 rational parametrization。

**PROVED.**

### A1-GPDS-7 — Infinite Minus Primitive Synchronization Pseudo-Family

第 14 节 polynomial family。

**PROVED.**

### A1-GPDS-8 — Common-Scale Digit Realization is Independent

sphere + GSYNC + exact common-\(V\) gcd profile + denominator digit legality 不推出 numerator common-\(U\) digit legality。

**PROVED by infinite family.**

---

# 19. Status of Each Sign Branch

## Plus

\[
\boxed{\textbf{OPEN}}
\]

但新增：

\[
10^{n_2-1}<Q_0-1,
\]

\[
10^{m_3}<Q_0^2/10,
\]

并继承 universal

\[
10^g<\sqrt{10Q_0}.
\]

没有 ambient infinite family 被本轮构造出来。

**当前判断：** plus 是下一轮最适合继续尝试 pure forward elimination 的 branch。

## Minus

\[
\boxed{\textbf{OPEN}}
\]

并有

\[
g\le m_2+2,
\]

但 primitive/gcd 层存在显式无限 synchronized family。

**当前判断：** 不应继续对 minus 做 pure private-prime / equal-gap / magnitude campaign；应直接进入 common-\(U\) digit cone，再必要时与 actual cut 对接。

---

# 20. Minimal Remaining Obstruction

本轮之后，Generic Primitive-Defect Synchronization 不能再被准确描述为：

\[
\text{“证明两个 defect 的 prime factorization 不可能同步。”}
\]

更准确的终端结构是：

\[
\boxed{
\begin{array}{c}
\text{primitive sphere}
+\text{ fixed-profile conic/GSYNC}
+\text{ common-}V\text{ gcd profile}
\\[1mm]
\Downarrow
\\[1mm]
\textbf{必须存在同一个 }U\textbf{ 穿过全部 numerator digit windows}
\\[1mm]
\Downarrow
\\[1mm]
\text{actual word/cut}
+\text{ reducedness}
+\text{ same-cut norm}
\end{array}
}
\]

其中第一条尚未被充分利用的最小 gate 是：

\[
\boxed{
I_{\rm num}\cap
\{U\in\mathbf Z_{>0}:\gcd(U,V)=1\}
\ne\varnothing.
}
\tag{OPEN-DIG-U}
\]

这比直接跳到完整 word classification 更轻，也比继续追 GSYNC prime support 更有信息。

---

# 21. Anti-Duplication Interface with the Backward Line

反向线当前已经把 A1 exact recovery 压到：

- actual denominator trace；
- full numerator word；
- legal cut；
- same-cut norm；
- residual \(5\)-phase / norm-excess feedback。

并且已经证明：

- detached-prefix norm/prime data 允许无限伪族；
- phase-to-cut + reducedness 也仍允许伪族；
- 最后需要的是同一个 actual cut 对 norm / phase 的反馈。

正向线本轮不应重复这些内容。

最小接口建议为：

\[
\boxed{
\textbf{Forward supplies: }
(P_i,Q_0,g_i;n_i,m_i)
+\text{ conic branch}
+I_{\rm num}.
}
\]

若 \(I_{\rm num}=\varnothing\)，正向直接死亡。

只有当 \(I_{\rm num}\) 非空并产生极少数 scale \(U\) 时，才把恢复出的真实 numerator blocks 交给 backward 的 same-cut norm / phase machinery。

这样两条线不会重复花 token。

---

# 22. Recommended Next Campaign

下一轮正向线建议改名为：

\[
\boxed{
\textbf{A1 Primitive-Conic × Common-Scale Digit-Window Campaign}
}
\]

优先级如下。

## Target 1 — Plus Branch Digit-Cone Elimination

利用

\[
P_3(1+10^{n_2-1})<Q_0,
\]

\[
10^{2g+k-2}<P_2/P_3,
\]

sphere 与 \(D>0\)，尝试把 plus branch 压成空集或更薄的 coordinate cone。

**原因：** plus 尚无 ambient infinite family，且已有两个独立的强 projective inequalities。

## Target 2 — Common-Scale Interval Theorem

研究

\[
I_{\rm num}
=
\bigcap_i
\left[
10^{n_i-1}/C_i,
10^{n_i}/C_i
\right).
\]

目标是证明 fixed synchronized conic 与该 interval gate 的交集：

- 为空；或
- 只能落在有限 exceptional slopes；或
- 自动把 \(U\) 压到唯一值 / 极短区间。

这可能把 moving conic 直接变成 finite arithmetic problem。

## Target 3 — Minus Branch Conic × Digit-Cone Intersection

第 14 节已经给出 primitive conic family并证明其整体避开真实 digit cone。

下一步不应再证“conic 存在”，而应问：

> 是否任何 minus synchronized conic 的 common-\(U\) digit-legal部分都必须退化到有限/空？

若答案仍否，再把仅剩 points 交给 backward same-cut norm。

---

# 23. Dependency / Provenance Audit

本轮新 theorem 的依赖非常短。

## 23.1 A1-GPDS-1

只依赖：

- A1 exponent identities；
- primitive normalization；
- 完整 numerator / denominator concatenation definition；
- \(A/B=\mathcal R\)。

不依赖旧 saturated theorem、Gaussian、square gate 或 backward phase。

## 23.2 A1-GPDS-2 / 3 / 4 / 5

只依赖：

- 原始 digit-window definition；
- primitive normalization \(a_i/b_i=(U/V)P_i\)；
- A1 exponent identities；
- 对 4 / 5 再加 defect sign。

因此这些新 height bounds 具有很干净的 provenance。

## 23.3 Infinite pseudo-family

只依赖：

- 显式 polynomial identities；
- elementary gcd/parity/mod-3 检查；
- fixed profile master equation；
- primitive sphere definition。

没有调用旧 External Exact-Lift 的强 closure lemma。

因此本轮最主要的新负结果是**独立可审计**的。

---

# 24. Claim Ledger

## PROVED

1. Word/primitive defect dictionary；
2. GSYNC = decimal split/carry identity；
3. sign chamber = prefix/tail local ratio ordering；
4. general Primitive Ratio Window；
5. A1
   \[
   10^{2g+k-2}<Q_0;
   \]
6. universal
   \[
   10^g<\sqrt{10Q_0};
   \]
7. plus
   \[
   P_3(1+10^{n_2-1})<Q_0;
   \]
8. plus
   \[
   10^{m_3}<Q_0(Q_0-1)/10;
   \]
9. minus
   \[
   g\le m_2+2;
   \]
10. fixed-profile master+sphere is a conic；
11. explicit infinite synchronized minus pseudo-family；
12. family has exact common-\(V\) gcd profile；
13. family has unbounded primitive height；
14. family dies at common-\(U\) numerator digit gate；
15. common-scale digit realization is independent information beyond primitive synchronization。

## DERIVED

1. any \(g\to\infty\) sequence has \(P_3/P_2\to0\)；
2. projective asymptotic boundary for growing \(g\) is \(P_3=0\) face；
3. plus branch all of \(n_2,n_3,g\) are logarithmically compressed with better constants than before。

## EXPERIMENTAL

1. one-digit denominator scan in the stated box: 0 plus hits, 3 minus hits；
2. plus branch may be arithmetically thinner than minus branch。

## FAILED / DISPROVED

1. primitive private-prime theorem；
2. uniform \(\Gamma_2\ne\Gamma_5\)；
3. small gcd of defects；
4. pure magnitude exclusion；
5. projective limit \(\Rightarrow\) flat；
6. ordinary Gaussian support as generic closure；
7. treating \(\mathscr S=\operatorname{core}_{10}\) as an independent global invariant capable of closing primitive A1。

## OPEN

1. plus branch elimination；
2. common-\(U\) digit-window synchronization on general synchronized conics；
3. minus branch after imposing real numerator digit cone；
4. exact interface from surviving scale-legal primitive states to backward same-cut norm；
5. full
   \[
   A_1=\varnothing.
   \]

---

# 25. Final Assessment

本轮没有达到 A1 closure，也没有消灭完整 sign branch。

但是它完成了一个更重要的 frontier correction：

\[
\boxed{
\textbf{Generic primitive-defect synchronization 本身并不是终端 obstruction。}
}
\]

其原因已经不是 heuristic，而是有显式无限 family 作证。

同时，primitive line 仍然产生了真正新的强约束：

\[
\boxed{
10^g<\sqrt{10Q_0},
}
\]

说明不能简单宣布“primitive layer 无用”。

最准确的新图景是：

\[
\boxed{
\text{Sphere}
\cap
\text{GSYNC plane}
=
\text{moving conic},
}
\]

然后真正的十进制语义要求该 conic 进一步穿过

\[
\boxed{
\text{common-}U\text{ digit cone / interval}.
}
\]

第 14 节 family 表明这两个集合可以大规模错开。

所以本轮真正回答了 prompt 最后的核心问题：

> 为什么两个 defect 的比值会恰好是一个纯 \(10\) 幂？

答案是：

\[
\boxed{
\textbf{因为那正是完整 decimal word 的 place-value cancellation。}
}
\]

真正需要证明的不是“这个 \(10\) 幂为什么不自然”，而是：

\[
\boxed{
\textbf{为什么一个同步 conic point 不可能同时拥有同一个合法 numerator scale、真实 cut 与 same-cut norm。}
}
\]

本轮已经把其中第一道缺失 gate 单独抽出并证明它确实独立：

\[
\boxed{
\textbf{Common-Scale Numerator Digit Realization.}
}
\]

因此最终等级为：

\[
\boxed{
\textbf{LEVEL 5 — PRIMITIVE LAYER INSUFFICIENCY CERTIFICATE}
+
\textbf{NEW STRONG HEIGHT COLLAPSE}.
}
\]

A1 仍 OPEN，但 frontier 已从“prime synchronization mystery”推进到一个明显更具体的：

\[
\boxed{
\textbf{Conic × Decimal Scale-Window Gluing Problem}.
}
\]

