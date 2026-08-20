# 三项十进制拼接平方和问题：DD Post-Deflation Campaign

**文件名：** `strict_layer_DD_post_deflation_campaign.md`  
**研究范围：** Strict Layer，仅研究 **DD chamber** 的 post-deflation small factor  
**本轮等级：** **SGR-5D — STRUCTURAL REDUCTION**  
**最终状态：** **DD 尚未闭合；未得到高度无关的 \(J^\sharp\) 常数界**

---

# 0. 结论摘要

本轮完全冻结上一轮的统一平方差正规形

\[
\varepsilon M^2-E=\varepsilon Y^2,
\qquad
J:=M-Y\in\mathbf Z_{\ge1},
\]

以及

\[
E=\varepsilon J(2M-J).
\]

顶部 DD 的 old Exact-Lift factors 满足

\[
\{F_-,F_+\}
=
\{\Lambda(M-Y),\Lambda(M+Y)\},
\]

其中

\[
\Lambda=UR^2\,10^{\lceil m_3/2\rceil}.
\]

对 \(p=2,5\)，double resonance 已给出

\[
v_p(M-Y)=v_p(M+Y)=j_p.
\]

定义

\[
D_0:=2^{j_2}5^{j_5},
\qquad
J^\sharp:=\frac{J}{D_0}.
\]

本轮的主要新结果是：在把所有强制 \(2,5\)-进尺度除掉以后，\(J^\sharp\) 确实存在一个很干净的 **post-deflation arithmetic normal form**。

首先令

\[
K^\sharp:=\frac{M+Y}{D_0},
\]

则

\[
\boxed{
J^\sharp,K^\sharp\in\mathbf Z_{>0},
\qquad
\gcd(J^\sharp K^\sharp,10)=1.
}
\]

再定义

\[
\boxed{
H^\sharp:=J^\sharp+K^\sharp=\frac{2M}{D_0},
}
\]

\[
\boxed{
N^\sharp:=J^\sharp K^\sharp
=
\frac{E}{\varepsilon D_0^2}.
}
\]

由于 \(D_0^2\) 正是 \(E/\varepsilon\) 的完整 \(2,5\)-primary part，

\[
\boxed{
\gcd(N^\sharp,10)=1.
}
\]

于是 \(J^\sharp\) 精确满足

\[
\boxed{
(J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0.
}
\tag{PD-1}
\]

这说明 post-deflation 后真正剩下的对象不是“一个仍带巨大十进制幂的平方差”，而是一个 **prime-to-\(10\) 的整数根**。

其次，本轮把 near-\(S\)-unit 与 rational-root divisibility 真正传到 \(J^\sharp\) 上。

记一个正整数的 prime-to-\(10\) 部分为

\[
n^{\langle10\rangle}
:=
\frac{n}{2^{v_2(n)}5^{v_5(n)}}.
\]

定义单一 residual supply

\[
\boxed{
\Omega_{\rm DD}
:=
\left(
Q_{12}\mathcal N_{12}\mathscr T
\right)^{\langle10\rangle},
}
\tag{PD-2}
\]

其中

\[
\mathscr T
=
\frac{\kappa^2(\kappa+2G)}{10^{m_3}}
\in\mathbf Z_{>0}.
\]

则本轮证明

\[
\boxed{
J^\sharp\mid\Omega_{\rm DD}^2.
}
\tag{PD-3}
\]

因此

\[
\boxed{
\operatorname{Supp}(J^\sharp)
\subseteq
\operatorname{Supp}(\Omega_{\rm DD}),
}
\]

而且不仅素因子来源被控制，连每个非 \(2,5\) 素数的指数也至多是
\(\Omega_{\rm DD}\) 中对应指数的两倍。

这给出了本轮最重要的答案：

\[
\boxed{
\text{强制 }2,5\text{-进尺度除掉以后，}
J^\sharp
\text{ 的全部 residual prime supply}
\text{ 都集中在一个整数 }\Omega_{\rm DD}.
}
\]

但

\[
\boxed{
\Omega_{\rm DD}
\text{ 目前没有高度无关的上界。}
}
\]

near-\(S\)-unit 只控制其中 tail 部分：

\[
\mathscr T<10^{S_{12}-7},
\]

却没有把

\[
Q_{12}^{\langle10\rangle},
\qquad
\mathcal N_{12}^{\langle10\rangle}
\]

压成固定有限素数集合或固定大小；这两个对象仍随 moving primitive core 变化。

第三，旧 deep Hensel phase 在 post-deflation 后确实留下信息，但它留下的是 **unit-class cancellation**，而不是新的 divisibility of \(J^\sharp\)。

若

\[
R_p^\sharp:=v_p(H^\sharp),
\qquad p=2,5,
\]

则由

\[
K^\sharp=H^\sharp-J^\sharp
\]

严格得到

\[
\boxed{
K^\sharp\equiv-J^\sharp
\pmod{p^{R_p^\sharp}},
}
\]

从而

\[
\boxed{
(J^\sharp)^2
\equiv
-N^\sharp
\pmod{p^{R_p^\sharp}}.
}
\tag{PD-4}
\]

因此 Hensel phase 的 post-deflation 含义是：

\[
\boxed{
J^\sharp
\text{ 是移动单位 }
-N^\sharp
\text{ 的一个 }p\text{-adic square-root class}.
}
\]

它并没有给出一个与 primitive core 无关的固定同余类

\[
J^\sharp\equiv u_0\pmod{10^r}.
\]

旧 \(5\)-进深 phase 的巨大模数仍然存在，但其右端单位
\(-N^\sharp\) 同时移动，所以目前不能与 Archimedean 小区间拼成矛盾。

第四，本轮把顶部 DD 的 Archimedean 信息直接作用到 \(J^\sharp\)。

由

\[
\rho=\frac{E}{\varepsilon M^2}
\]

有精确公式

\[
\boxed{
J^\sharp
=
\frac{M}{D_0}
\left(
1-\sqrt{1-\rho}
\right)
=
\frac{M\rho}
{D_0(1+\sqrt{1-\rho})}.
}
\tag{PD-5}
\]

因此

\[
\boxed{
\frac{M\rho}{2D_0}
\le
J^\sharp
\le
\frac{M\rho}{D_0}.
}
\tag{PD-6}
\]

或者用 \(H^\sharp=2M/D_0\)：

\[
\boxed{
\frac{H^\sharp\rho}{4}
\le
J^\sharp
\le
\frac{H^\sharp\rho}{2}.
}
\tag{PD-7}
\]

DD 已有

\[
\rho
<
143
\left(
10^{-2k_{12}}
+
10^{2(1-d_3-s_1)}
\right).
\]

所以本轮得到最强的 statewise upper bound

\[
\boxed{
J^\sharp
<
\frac{143M}{D_0}
\left(
10^{-2k_{12}}
+
10^{2(1-d_3-s_1)}
\right).
}
\tag{PD-8}
\]

继续只使用顶部已证区间，可粗化成一个完全显式的 height bound：

\[
\boxed{
J^\sharp
<
14443\cdot10^{3S_{12}-10}.
}
\tag{PD-9}
\]

这个指数已经比直接对 \(M\) 与 \(\rho\) 分开估计明显更强，但仍随
\(S_{12}\) 指数增长，因此不能得到

\[
J^\sharp\le C
\]

的高度无关常数。

所以本轮裁决为：

\[
\boxed{
\textbf{SGR-5D — STRUCTURAL REDUCTION}.
}
\]

DD 尚未闭合。

唯一留下的 terminal gap 统一定义为：

\[
\boxed{
\textbf{Residual Supply Gap: }
\Omega_{\rm DD}
=
(Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}
\textbf{ 是否能被进一步统一控制？}
}
\]

只要未来证明

\[
\Omega_{\rm DD}\le C
\]

或证明其可允许 divisor classes 与 (PD-4) 的双 Hensel unit classes 不相容，
则由

\[
J^\sharp\mid\Omega_{\rm DD}^2
\]

会立即把 DD 压成高度无关的有限 residual states。

---

# 1. 来源审计与范围冻结

本轮重点使用：

- `strict_layer_DD_error_closure_campaign.md`；
- `strict_layer_moving_core_square_spacing_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`。

并回查统一 Exact-Lift 报告中 gap quadratic、rational-root divisibility、
tail certificate 的证明接口。

当前 File Library 中，DD 顶部 double resonance、deep Hensel phase、
near-\(S\)-unit、extreme denominator asymmetry 的完整可检索证明链仍主要集中在
`exact_lift_research_synthesis_2026-08-10.md` 的 DD §§18–26。
上一轮已经检索过独立命名的更晚 DD 专门文件而未重新暴露；
因此本轮不虚构不可见来源，只在这些已审计公式上继续推导。

本轮严格冻结：

\[
\boxed{\text{DD only}.}
\]

不研究：

- \(A_1\)；
- 临界层；
- resultant；
- 总体 strict-layer 分类；
- 已经失败的裸 \(v_p(E)\Rightarrow E\) 小；
- 已经失败的裸 \(v_p(F_\pm)\Rightarrow F_{\min}\) 被过大模数整除。

---

# 2. 冻结的 post-deflation 起点

上一轮已经得到

\[
\varepsilon M^2-E=\varepsilon Y^2,
\qquad
0\le Y<M,
\]

并定义

\[
\boxed{
J:=M-Y.
}
\]

完整候选要求

\[
J\in\mathbf Z_{\ge1}.
\]

于是

\[
\boxed{
E=\varepsilon J(2M-J).
}
\tag{2.1}
\]

旧 DD factors 满足精确桥

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda(M-Y),
\Lambda(M+Y)
\},
}
\tag{2.2}
\]

其中

\[
\boxed{
\Lambda
=
UR^2\,10^{\lceil m_3/2\rceil}.
}
\tag{2.3}
\]

顶部 double resonance 给出，对 \(p=2,5\)，

\[
\boxed{
v_p(M-Y)=v_p(M+Y)=j_p.
}
\tag{2.4}
\]

定义

\[
\boxed{
D_0:=2^{j_2}5^{j_5}.
}
\tag{2.5}
\]

则

\[
D_0\mid J,
\qquad
D_0\mid(M+Y),
\]

且

\[
\boxed{
D_0^2
\text{ 是 }E/\varepsilon
\text{ 的完整 }(2,5)\text{-primary part}.
}
\tag{2.6}
\]

因此本轮真正变量为

\[
\boxed{
J^\sharp:=\frac{J}{D_0}.
}
\tag{2.7}
\]

---

# 3. 完整 post-deflation 二因子正规形

不仅除 \(J\)，同时定义另一因子

\[
\boxed{
K^\sharp
:=
\frac{M+Y}{D_0}.
}
\tag{3.1}
\]

由 (2.4) 的“赋值恰等于 \(j_p\)”：

\[
\boxed{
v_2(J^\sharp)=v_5(J^\sharp)=0,
}
\]

\[
\boxed{
v_2(K^\sharp)=v_5(K^\sharp)=0.
}
\]

所以

\[
\boxed{
\gcd(J^\sharp K^\sharp,10)=1.
}
\tag{3.2}
\]

定义

\[
\boxed{
H^\sharp
:=
J^\sharp+K^\sharp
=
\frac{2M}{D_0},
}
\tag{3.3}
\]

以及

\[
\boxed{
N^\sharp
:=
J^\sharp K^\sharp
=
\frac{E}{\varepsilon D_0^2}.
}
\tag{3.4}
\]

由 \(D_0^2\) 是完整 \(2,5\)-primary part，

\[
\boxed{
\gcd(N^\sharp,10)=1.
}
\tag{3.5}
\]

于是：

\[
\boxed{
(J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0.
}
\tag{3.6}
\]

并且

\[
\boxed{
(H^\sharp)^2-4N^\sharp
=
\left(
\frac{2Y}{D_0}
\right)^2.
}
\tag{3.7}
\]

这里 \(2Y/D_0\in\mathbf Z\)，因为

\[
D_0\mid(M-Y),
\qquad
D_0\mid(M+Y)
\]

推出

\[
D_0\mid2Y.
\]

因此 DD 的 post-deflation 终端对象可完全改写成：

> 找一个 prime-to-\(10\) 正整数根 \(J^\sharp\)，使得
> \[
> X^2-H^\sharp X+N^\sharp=0
> \]
> 且判别式为整数平方。

这一步已经完全去除了公共强制 \(2,5\)-进尺度。

---

# 4. Hensel phase 在 \(J^\sharp\) 上真正留下什么？

## 4.1 intrinsic residual cancellation depth

对 \(p=2,5\)，定义

\[
\boxed{
R_p^\sharp:=v_p(H^\sharp).
}
\tag{4.1}
\]

由于 \(J^\sharp,K^\sharp\) 都是 \(p\)-adic units，

\[
H^\sharp
=
J^\sharp+K^\sharp
\]

的高 \(p\)-进赋值只能来自两个 unit parts 的相消。

因此

\[
\boxed{
K^\sharp
\equiv
-J^\sharp
\pmod{p^{R_p^\sharp}}.
}
\tag{4.2}
\]

乘以 \(J^\sharp\)：

\[
N^\sharp
=
J^\sharp K^\sharp
\equiv
-(J^\sharp)^2
\pmod{p^{R_p^\sharp}}.
\]

所以

\[
\boxed{
(J^\sharp)^2
\equiv
-N^\sharp
\pmod{p^{R_p^\sharp}}.
}
\tag{4.3}
\]

这就是旧 “约掉共同赋值后的 Hensel phase” 在 post-deflation 坐标中的内在形式。

---

## 4.2 关键裁决：phase 控制 unit root，不控制大小

(4.3) 与

\[
D_0\mid J
\]

的性质完全不同。

在 deflation 前，double resonance 产生共同 \(2,5\)-进尺度；
在 deflation 后，

\[
\boxed{
J^\sharp
\text{ 已经是 }2,5\text{-adic unit}.
}
\]

于是 deep phase 只能告诉我们：

\[
\boxed{
J^\sharp
\in
\sqrt{-N^\sharp}
\pmod{2^{R_2^\sharp}}
}
\]

与

\[
\boxed{
J^\sharp
\in
\sqrt{-N^\sharp}
\pmod{5^{R_5^\sharp}}.
}
\]

但右端

\[
N^\sharp
=
\frac{E}{\varepsilon D_0^2}
\]

仍随 moving primitive core 变化。

所以现有 phase **不能**升级成：

\[
J^\sharp\equiv u_0\pmod{2^r},
\]

\[
J^\sharp\equiv v_0\pmod{5^s}
\]

其中 \(u_0,v_0\) 为固定、与 core 无关的单位。

这正是为什么“巨大 Hensel modulus + 小 Archimedean interval”目前还不能直接完成 CRT contradiction。

---

## 4.3 与旧 \(R_5\) 的关系

旧 DD 顶部证明在约掉两个 factors 的共同 \(5\)-进赋值后得到深 phase

\[
\mu_5
\equiv
\pm\rho_5\nu_5
\pmod{5^{R_5}},
\]

并有

\[
R_5>1.415S_{12}+9.
\]

通过

\[
\{F_-,F_+\}
=
\{\Lambda D_0J^\sharp,\Lambda D_0K^\sharp\}
\]

可以看到：旧 phase 所测量的正是共同尺度除掉以后两个 factor unit parts 的深相消。

因此它在新坐标中只会加强

\[
R_5^\sharp=v_5(H^\sharp)
\]

这一类 cancellation depth，而不会重新令

\[
5\mid J^\sharp.
\]

换言之：

\[
\boxed{
\text{deep Hensel survives deflation,
but survives as phase, not as valuation.}
}
\]

---

# 5. near-\(S\)-unit 在 \(J^\sharp\) 上真正留下什么？

旧顶部 DD 定义

\[
\boxed{
\mathscr T
=
\frac{\kappa^2(\kappa+2G)}{10^{m_3}}
\in\mathbf Z_{>0},
}
\tag{5.1}
\]

并已证

\[
\boxed{
1\le\mathscr T<10^{S_{12}-7}.
}
\tag{5.2}
\]

写

\[
\kappa=2^a5^bu,
\qquad
\gcd(u,10)=1,
\]

\[
\kappa+2G=2^c5^ev,
\qquad
\gcd(v,10)=1.
\]

则

\[
\boxed{
u^2\mid\mathscr T,
\qquad
v\mid\mathscr T,
}
\]

而事实上对 prime-to-\(10\) 部分有精确恒等

\[
\boxed{
\mathscr T^{\langle10\rangle}
=
u^2v.
}
\tag{5.3}
\]

旧结论还给出

\[
u<10^{(S_{12}-7)/2},
\qquad
v<10^{S_{12}-7}.
\]

这说明 tail coefficients 本身已经很接近 \(2,5\)-smooth。

但 \(J^\sharp\) 不只读取 \(\kappa,\kappa+2G\)：
它还读取 gap-root numerators \(\mu,\nu\)、\(\mathcal N_{12}\)、\(Q_{12}\) 与 \(G_0\)。

所以必须继续使用 rational-root divisibility。

---

# 6. 新定理：\(J^\sharp\) 的 residual prime supply

Gap quadratic 已证

\[
Q_{12}(\kappa+2G)\mu^2
-
2G\kappa C\,\mu\nu
+
\kappa Q_{12}\mathcal N_{12}\nu^2
=0,
\]

其中

\[
\gcd(\mu,\nu)=1.
\]

由 rational-root divisibility：

\[
\boxed{
\nu\mid Q_{12}(\kappa+2G),
}
\tag{6.1}
\]

\[
\boxed{
\mu\mid\kappa Q_{12}\mathcal N_{12}.
}
\tag{6.2}
\]

旧 factors 为

\[
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
\]

\[
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0}.
\]

定义

\[
\boxed{
\Omega_{\rm DD}
:=
\left(
Q_{12}\mathcal N_{12}\mathscr T
\right)^{\langle10\rangle}.
}
\tag{6.3}
\]

下面证明：

\[
\boxed{
J^\sharp\mid\Omega_{\rm DD}^2.
}
\tag{6.4}
\]

---

## 6.1 逐素数证明

固定

\[
p\ne2,5.
\]

记

\[
q=v_p(Q_{12}),
\qquad
n=v_p(\mathcal N_{12}),
\]

\[
a=v_p(\kappa),
\qquad
b=v_p(\kappa+2G),
\]

\[
t=v_p(\mathscr T).
\]

因为 \(p\nmid10\)，由 (5.1)

\[
\boxed{
t=2a+b.
}
\tag{6.5}
\]

再记

\[
r=v_p(\mu),
\qquad
s=v_p(\nu).
\]

由 (6.1)–(6.2)：

\[
\boxed{
r\le a+q+n,
}
\tag{6.6}
\]

\[
\boxed{
s\le q+b.
}
\tag{6.7}
\]

---

### 情形 I：小因子来自 \(F_-\)

忽略只会降低赋值的分母 \(G_0\)、\(\Lambda\)，有

\[
v_p(J^\sharp)
\le
b+2r.
\]

由 (6.6)：

\[
v_p(J^\sharp)
\le
b+2a+2q+2n.
\]

利用 \(t=2a+b\)：

\[
v_p(J^\sharp)
\le
t+2q+2n.
\]

而

\[
t+2q+2n
\le
2(q+n+t).
\]

故

\[
\boxed{
v_p(J^\sharp)
\le
2v_p(\Omega_{\rm DD}).
}
\tag{6.8}
\]

---

### 情形 II：小因子来自 \(F_+\)

同样

\[
v_p(J^\sharp)
\le
a+n+2s.
\]

由 (6.7)：

\[
v_p(J^\sharp)
\le
a+n+2q+2b.
\]

另一方面

\[
2(q+n+t)
=
2q+2n+4a+2b.
\]

两者之差为

\[
n+3a\ge0.
\]

所以仍有

\[
\boxed{
v_p(J^\sharp)
\le
2v_p(\Omega_{\rm DD}).
}
\tag{6.9}
\]

对所有 \(p\ne2,5\) 成立。

又因为 \(J^\sharp\) 本身与 \(10\) 互素，故：

\[
\boxed{
J^\sharp\mid\Omega_{\rm DD}^2.
}
\tag{6.10}
\]

证毕。

---

# 7. 这条定理对 near-\(S\)-unit 的真正解释

(6.10) 比“\(\kappa\) 和 \(\kappa+2G\) near-\(S\)-unit”更接近本轮真正需要的结论。

它说明：

\[
\boxed{
\text{post-deflation 后不会凭空产生新的奇素数。}
}
\]

所有可能进入 \(J^\sharp\) 的非 \(2,5\) prime power 都必须由

\[
\boxed{
Q_{12},
\quad
\mathcal N_{12},
\quad
\mathscr T
}
\]

提供。

其中：

- \(\mathscr T\) 是 tail residual supply；
- \(Q_{12}\) 是前两 denominator prefix supply；
- \(\mathcal N_{12}\) 是 primitive two-square prefix supply。

near-\(S\)-unit 已经把第一项压得相对较小：

\[
\mathscr T<10^{S_{12}-7}.
\]

但现有 DD 理论没有证明

\[
Q_{12}^{\langle10\rangle}
\]

或

\[
\mathcal N_{12}^{\langle10\rangle}
\]

来自固定素数集合。

因此：

\[
\boxed{
\text{near-}S\text{-unit}
\not\Longrightarrow
J^\sharp
\text{ 是固定 }S\text{-unit}.
}
\]

这正是 deflation 后 near-\(S\)-unit 留下的精确信息边界。

---

# 8. Extreme asymmetry 对 \(J^\sharp\) 的 Archimedean 作用

定义

\[
\rho
=
\frac{E}{\varepsilon M^2}.
\]

由

\[
Y=M\sqrt{1-\rho}
\]

得到

\[
J
=
M-Y
=
M(1-\sqrt{1-\rho}).
\]

有理化：

\[
\boxed{
J
=
\frac{M\rho}
{1+\sqrt{1-\rho}}.
}
\tag{8.1}
\]

所以

\[
\boxed{
J^\sharp
=
\frac{M\rho}
{D_0(1+\sqrt{1-\rho})}.
}
\tag{8.2}
\]

因为

\[
1\le1+\sqrt{1-\rho}\le2,
\]

得到

\[
\boxed{
\frac{M\rho}{2D_0}
\le
J^\sharp
\le
\frac{M\rho}{D_0}.
}
\tag{8.3}
\]

已有 DD digit estimate：

\[
\boxed{
\rho
<
143
\left[
10^{-2k_{12}}
+
10^{2(1-d_3-s_1)}
\right].
}
\tag{8.4}
\]

于是

\[
\boxed{
J^\sharp
<
\frac{143M}{D_0}
\left[
10^{-2k_{12}}
+
10^{2(1-d_3-s_1)}
\right].
}
\tag{8.5}
\]

这是现有全部 DD Archimedean 信息在 post-deflation 后的最直接形式。

---

# 9. 一个新的 height-explicit bound

虽然得不到高度无关常数，但顶部 DD 的现有 inequalities 可以进一步压出一个比
“\(J^\sharp\ll M\rho\)”明确得多的统一高度界。

记

\[
S:=S_{12}=m_1+m_2.
\]

顶部已证：

\[
10S+11\le n_3,
\]

\[
m_3\le6S+2.
\]

因为

\[
d_3=n_3-m_3,
\]

所以

\[
\boxed{
d_3\ge4S+9.
}
\tag{9.1}
\]

又由于每个 numerator 至少一位，

\[
n_i\ge1,
\]

所以

\[
s_i=n_i-m_i\ge1-m_i.
\]

而

\[
m_i\le S-1,
\]

故

\[
\boxed{
s_1,s_2\ge2-S.
}
\tag{9.2}
\]

特别

\[
k_{12}=d_3+s_2
\ge
d_3+2-S.
\tag{9.3}
\]

---

## 9.1 \(M\) 的前缀上界

在顶部 \(d_3\)-dominant sector，surplus simplex 给出

\[
s_1+s_2\le2.
\]

因此

\[
n_1+n_2
=
m_1+m_2+s_1+s_2
\le
S+2.
\]

普通前两分子拼接

\[
A_{12}=a_1 10^{n_2}+a_2
\]

于是满足

\[
\boxed{
A_{12}<10^{S+2}.
}
\tag{9.4}
\]

同时

\[
G=b_1b_2<10^S.
\]

而

\[
M
=
10^{\lfloor m_3/2\rfloor+d_3}
\frac{GA_{12}}{UR^2}.
\]

由于

\[
UR^2\ge1,
\]

有

\[
\boxed{
M
<
10^{\lfloor m_3/2\rfloor+d_3+2S+2}.
}
\tag{9.5}
\]

---

## 9.2 第一误差项

由 (9.3)

\[
-2k_{12}
\le
-2d_3+2S-4.
\]

所以

\[
M10^{-2k_{12}}
<
10^{
\lfloor m_3/2\rfloor
-d_3
+4S-2
}.
\]

因为

\[
d_3=n_3-m_3,
\]

\[
\lfloor m_3/2\rfloor-d_3
=
m_3+\lfloor m_3/2\rfloor-n_3
\le
\frac32m_3-n_3.
\]

故

\[
M10^{-2k_{12}}
<
10^{
\frac32m_3-n_3+4S-2
}.
\]

代入

\[
m_3\le6S+2,
\qquad
n_3\ge10S+11,
\]

得到

\[
\boxed{
M10^{-2k_{12}}
<
10^{3S-10}.
}
\tag{9.6}
\]

---

## 9.3 第二误差项

由

\[
s_1\ge2-S,
\]

有

\[
2(1-d_3-s_1)
\le
-2d_3+2S-2.
\]

因此

\[
M10^{2(1-d_3-s_1)}
<
10^{
\lfloor m_3/2\rfloor-d_3+4S
}.
\]

同理得到

\[
\boxed{
M10^{2(1-d_3-s_1)}
<
10^{3S-8}.
}
\tag{9.7}
\]

---

## 9.4 合并

由于 \(D_0\ge1\)，由 (8.5)、(9.6)、(9.7)：

\[
J^\sharp
<
143
\left(
10^{3S-10}
+
10^{3S-8}
\right).
\]

所以

\[
\boxed{
J^\sharp
<
14443\cdot10^{3S-10}.
}
\tag{9.8}
\]

这是本轮从全部现有顶部 DD inequalities 中得到的最强 **height-explicit uniform bound**。

但它仍然是

\[
10^{3S}
\]

级，而不是常数。

所以它没有达到 SGR-5C。

---

# 10. 为什么 extreme denominator asymmetry 仍未给常数界？

顶部还已证

\[
|m_1-m_2|
>
0.466872S+4.826675,
\]

以及

\[
|s_1-s_2|
>
1.466872S+4.826675.
\]

这些结论确实把前两块压成极端不对称形态，并在一个方向上给出短 numerator block。

但 post-deflation 后，真正需要比较的是

\[
\boxed{
\frac{M}{D_0}\rho.
}
\]

extreme asymmetry 会压低 \(\rho\)，但：

1. 没有给出随 \(S\) 增长的 \(D_0\) **下界**；
2. 没有把
   \[
   Q_{12}^{\langle10\rangle}
   \]
   压成固定大小；
3. 没有把
   \[
   \mathcal N_{12}^{\langle10\rangle}
   \]
   压成固定大小；
4. moving primitive core 仍允许前缀 arithmetic supply 与 \(S\) 同时增长。

因此现有不对称的最佳统一结果仍是类似 (9.8) 的高度函数，而不是

\[
J^\sharp\le C.
\]

---

# 11. 两种 residual control 的统一解释

本轮现在有两条真正作用于 \(J^\sharp\) 的信息。

## 11.1 Archimedean

\[
\boxed{
J^\sharp
=
\frac{M\rho}
{D_0(1+\sqrt{1-\rho})}.
}
\]

所以 size 的本质组合量是

\[
\boxed{
\Theta_{\rm DD}
:=
\frac{M\rho}{D_0}.
}
\]

且

\[
\frac{\Theta_{\rm DD}}2
\le
J^\sharp
\le
\Theta_{\rm DD}.
\]

---

## 11.2 Arithmetic

\[
\boxed{
J^\sharp\mid\Omega_{\rm DD}^2,
}
\]

其中

\[
\boxed{
\Omega_{\rm DD}
=
(Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}.
}
\]

所以 prime support 与 prime-power supply 的本质组合量是
\(\Omega_{\rm DD}\)。

---

## 11.3 为什么最终只保留 \(\Omega_{\rm DD}\) 一个 terminal gap？

若未来得到

\[
\Omega_{\rm DD}\le C,
\]

则立刻有

\[
J^\sharp\le C^2.
\]

于是所有无界 residual states 自动消失，转成有限 \(J^\sharp\) 枚举。

反过来，当前所有无法形成高度无关有限化的算术原因都可定位到：

\[
\boxed{
\Omega_{\rm DD}
\text{ 中仍含 moving prefix supply }
Q_{12}^{\langle10\rangle}
\mathcal N_{12}^{\langle10\rangle}.
}
\]

因此虽然 \(\Theta_{\rm DD}\) 是更尖锐的 Archimedean size comparator，
下一轮若只选择一个算术对象攻击，最小对象应取：

\[
\boxed{
\Omega_{\rm DD}.
}
\]

它同时控制：

- \(J^\sharp\) 的所有非 \(2,5\) 素因子；
- 对应 prime powers；
- \(J^\sharp\) 的一个直接整数上界 \(\Omega_{\rm DD}^2\)。

---

# 12. 目标 A–D 的逐项裁决

## 目标 A

希望：

\[
0<J<1.
\]

本轮未得到。

当前最强 post-deflation Archimedean bound 为 (8.5)，高度粗化为 (9.8)，仍允许增长。

**状态：未完成。**

---

## 目标 B

希望：

\[
D_0\mid J,
\qquad
0<J<D_0.
\]

第一式已知。

但没有得到随高度增长的 \(D_0\) 下界，更没有得到

\[
J<D_0.
\]

旧 Hensel phase 在除去 \(D_0\) 后变成 unit-class condition，不再增加 \(D_0\)。

**状态：未完成。**

---

## 目标 C

希望 \(J^\sharp\) 落在高度无关有限集合。

本轮得到

\[
J^\sharp\mid\Omega_{\rm DD}^2,
\]

所以对固定 \(\Omega_{\rm DD}\)，\(J^\sharp\) 确实只有有限多个 divisor states。

但 \(\Omega_{\rm DD}\) 仍可随 moving core 增长。

因此尚未得到 height-independent finite set。

**状态：局部有限化完成，全局有限化未完成。**

---

## 目标 D

希望 \(J^\sharp=1\) 或极少数小值后与 phase / recovery 冲突。

本轮还不能先把 \(J^\sharp\) 压到这些小值。

若未来 \(J^\sharp=c\) 固定，则 (4.3) 会要求

\[
\boxed{
N^\sharp
\equiv
-c^2
\pmod{2^{R_2^\sharp}},
}
\]

\[
\boxed{
N^\sharp
\equiv
-c^2
\pmod{5^{R_5^\sharp}}.
}
\]

这会成为非常具体的 terminal phase test。

但当前没有资格把它提升成 finite-state closure。

**状态：已得到终端测试接口，未得到 finite input list。**

---

# 13. 为什么本轮是 SGR-5D，而不是 5C / 5E

## 13.1 不是 SGR-5C

SGR-5C 要求存在高度无关常数

\[
J^\sharp\le C.
\]

本轮只得到：

\[
J^\sharp
<
14443\cdot10^{3S_{12}-10},
\]

以及

\[
J^\sharp\mid\Omega_{\rm DD}^2.
\]

二者都还允许随 moving core / \(S_{12}\) 增长。

所以不能标 5C。

---

## 13.2 也不是 SGR-5E

post-deflation 路线并没有“信息全部消失”。

相反，本轮新得到：

\[
\boxed{
\gcd(J^\sharp,10)=1,
}
\]

\[
\boxed{
(J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0,
}
\]

\[
\boxed{
(J^\sharp)^2\equiv-N^\sharp
\pmod{p^{R_p^\sharp}},
\quad p=2,5,
}
\]

\[
\boxed{
J^\sharp\mid\Omega_{\rm DD}^2,
}
\]

以及显式高度界

\[
\boxed{
J^\sharp
<
14443\cdot10^{3S_{12}-10}.
}
\]

所以 deflation 后仍保留了非常明确的 arithmetic structure。

失败的只是：

\[
\boxed{
\Omega_{\rm DD}
\text{ 尚未被统一压住。}
}
\]

因此正确等级是：

\[
\boxed{
\textbf{SGR-5D — STRUCTURAL REDUCTION}.
}
\]

---

# 14. 唯一 terminal gap

本轮从此不再把 DD 末端拆成：

- near-\(S\)-unit gap；
- Hensel gap；
- denominator asymmetry gap；
- square-spacing gap；
- valuation overload gap。

在 post-deflation 坐标中，它们统一压成一个 residual supply 问题：

\[
\boxed{
\Omega_{\rm DD}
=
\left(
Q_{12}\mathcal N_{12}\mathscr T
\right)^{\langle10\rangle}.
}
\]

并且

\[
\boxed{
J^\sharp\mid\Omega_{\rm DD}^2.
}
\]

所以唯一剩余问题是：

\[
\boxed{
\textbf{能否对 }\Omega_{\rm DD}
\textbf{ 建立 height-independent bound，
或证明其 divisor classes 与双 Hensel phase 不相容？}
}
\tag{TG}
\]

现有 near-\(S\)-unit 已经控制

\[
\mathscr T,
\]

但真正未被控制的是其中的 moving prefix contribution

\[
\boxed{
\left(
Q_{12}\mathcal N_{12}
\right)^{\langle10\rangle}.
}
\]

这就是本轮定位到的最后自由算术供应源。

---

# 15. 最终 ledger

## NEW PROVED / DERIVED

1. 完整 post-deflation companion factor：
   \[
   K^\sharp=(M+Y)/D_0.
   \]

2. 两个 residual factors 都与 \(10\) 互素：
   \[
   \gcd(J^\sharp K^\sharp,10)=1.
   \]

3. post-deflation sum/product：
   \[
   H^\sharp=2M/D_0,
   \qquad
   N^\sharp=E/(\varepsilon D_0^2).
   \]

4. residual quadratic：
   \[
   (J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0.
   \]

5. Hensel phase 的真正 residual 形式：
   \[
   (J^\sharp)^2\equiv-N^\sharp
   \pmod{p^{R_p^\sharp}}.
   \]

6. residual supply：
   \[
   \Omega_{\rm DD}
   =
   (Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}.
   \]

7. 核心新 divisibility：
   \[
   \boxed{
   J^\sharp\mid\Omega_{\rm DD}^2.
   }
   \]

8. exact Archimedean formula：
   \[
   J^\sharp
   =
   \frac{M\rho}
   {D_0(1+\sqrt{1-\rho})}.
   \]

9. 顶部 statewise bound：
   \[
   J^\sharp
   <
   \frac{143M}{D_0}
   \left[
   10^{-2k_{12}}
   +
   10^{2(1-d_3-s_1)}
   \right].
   \]

10. height-explicit bound：
    \[
    \boxed{
    J^\sharp
    <
    14443\cdot10^{3S_{12}-10}.
    }
    \]

---

## NOT PROVED

没有证明：

\[
J<1.
\]

没有证明：

\[
J<D_0.
\]

没有证明：

\[
J^\sharp\le C
\]

对绝对常数 \(C\)。

没有证明：

\[
J^\sharp
\]

属于高度无关有限集合。

没有排除：

\[
J^\sharp=1,2,3,\ldots
\]

中的某个固定有限表，因为目前尚未得到这样的有限表。

---

# 16. 最终裁决

\[
\boxed{
\textbf{SGR-5D — STRUCTURAL REDUCTION}
}
\]

\[
\boxed{
\textbf{DD NOT CLOSED}.
}
\]

\[
\boxed{
\textbf{No height-independent uniform bound for }J^\sharp
\textbf{ has been proved.}
}
\]

本轮真正的新压缩是：

\[
\boxed{
\text{all forced }2,5\text{-adic scale removed}
}
\]

之后，

\[
\boxed{
J^\sharp
\text{ 是一个 prime-to-}10\text{ 的整数根，}
}
\]

其全部剩余 prime-power supply 满足

\[
\boxed{
J^\sharp\mid
\left[
(Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}
\right]^2.
}
\]

因此唯一 terminal gap 为：

\[
\boxed{
\textbf{控制 }
\Omega_{\rm DD}
=
(Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle},
\textbf{ 尤其是其 moving prefix part }
(Q_{12}\mathcal N_{12})^{\langle10\rangle}.
}
\]

换言之：

\[
\boxed{
\text{共同尺度已经全部除掉；}
\quad
\text{现在剩下的不是一个“神秘小因子”，}
\quad
\text{而是一个由 }\Omega_{\rm DD}\text{ 供给的 prime-to-}10\text{ divisor state。}
}
\]
