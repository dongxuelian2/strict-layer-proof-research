# 三项十进制拼接平方和问题：Moving-Core Square-Spacing Campaign

**文件名：** `strict_layer_moving_core_square_spacing_campaign.md`  
**本轮等级：** **SGR-3C — UNIFORM SQUARE-SPACING LEMMA**  
**研究范围：** 严格层仅保留 **DD** 与 **\(A_1\)-only**；不研究 \(A_2\)-only、deep-even、source Hensel 或其他临界层内容。

---

# 0. 结论摘要

本轮没有关闭 DD 或 \(A_1\)-only，也没有证明全部 moving primitive cores 终止。

但得到了一条比上一轮
\[
\Phi_\Sigma(Z_*^2)=0
\]
更直接、更规范的统一结构。

核心发现是：对 DD 与 \(A_1\)-only，上一轮次数至多 \(6\) 的 Exact 判别平方门

\[
Z^2
=
\widetilde\kappa
\left(
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right)
\]

都可以**严格抽掉一个完整平方因子**
\[
(\widehat Q\widehat G)^2
\]
以及十进制平方部分，把它降成一个次数至多 \(3\) 的
\[
\boxed{\text{square / }10\times\text{square}}
\]
门。

更具体地，令

\[
\chi=
\begin{cases}
1,&DD,\\
10^g,&A_1\text{-only},
\end{cases}
\qquad
\widehat D=\chi\widehat Q,
\]

则有

\[
\boxed{
\Psi
=
10^{m_3}\widehat K
-
2h_3\chi^2\widehat Q\widehat{\mathcal N}
}
\]

并且完整候选必满足

\[
\boxed{
\Psi=
\begin{cases}
Y^2,&m_3\text{ 偶},\\
10Y^2,&m_3\text{ 奇},
\end{cases}
\qquad Y\in\mathbf Z_{>0}.
}
\tag{US-1}
\]

把

\[
\widehat K
=
\widehat G^2\widehat C^2
-
\chi^2\widehat Q^2\widehat{\mathcal N}
\]

代入，可得到一个**无剩余项的精确主项—误差分解**

\[
\boxed{
\varepsilon M^2-E=\varepsilon Y^2,
}
\tag{US-2}
\]

其中

\[
\varepsilon=
\begin{cases}
1,&m_3\text{ 偶},\\
10,&m_3\text{ 奇},
\end{cases}
\]

\[
\boxed{
M
=
10^{\lfloor m_3/2\rfloor}
\widehat G\widehat C,
}
\]

\[
\boxed{
E
=
\chi^2\widehat Q\widehat{\mathcal N}
\left(
10^{m_3}\widehat Q+2h_3
\right)>0.
}
\]

因此

\[
E
=
\varepsilon(M-Y)(M+Y).
\]

因为 \(0<Y<M\)，相邻平方间距立即给出

\[
\boxed{
E\ge
\varepsilon(2M-1).
}
\tag{US-3}
\]

于是得到真正 uniform 的死亡判据：

\[
\boxed{
0<E<\varepsilon(2M-1)
\Longrightarrow
\text{该 strict state 不可能有完整候选}.
}
\tag{US-4}
\]

这个结论对所有 primitive-core height、所有 DD 状态、所有 \(A_1\)-only 状态统一成立，并且不依赖渐近近似。

定义无量纲误差

\[
\boxed{
\rho
:=
\frac{E}{\varepsilon M^2}
=
\frac{
D^2\mathcal N_{12}
}{
G^2C^2
}
\left(
1+
\frac{2b_3}{10^{m_3}Q_{12}}
\right).
}
\tag{US-5}
\]

则任何完整候选必须满足

\[
\boxed{
\frac{2}{M}-\frac1{M^2}
\le
\rho
<1.
}
\tag{US-6}
\]

这就是本轮得到的 **uniform square-spacing lemma**。

它同时解释了旧 DD 顶部 near-square 为什么出现：DD 中

\[
C=10^{d_3}A_{12},\qquad D=Q_{12},
\]

所以

\[
\rho_{DD}
=
10^{-2d_3}
\frac{Q_{12}^2\mathcal N_{12}}{G^2A_{12}^2}
\left(
1+\frac{2b_3}{10^{m_3}Q_{12}}
\right).
\]

但对 \(A_1\)-only，

\[
C=A_{12},\qquad D=10^gQ_{12},
\]

所以

\[
\rho_{A_1}
=
10^{2g}
\frac{Q_{12}^2\mathcal N_{12}}{G^2A_{12}^2}
\left(
1+\frac{2b_3}{10^{m_3}Q_{12}}
\right).
\]

由于
\[
n_2=m_2+g+k_{12},
\]
\(A_{12}\) 自身也随 \(g\) 增长，故裸 \(10^{2g}\) 并不会产生一个随 \(g\to\infty\) 自动趋零的误差。事实上本轮证明了两 chamber 共同的下界

\[
\boxed{
\rho>\frac1{400}\,10^{-2k_{12}}.
}
\tag{US-7}
\]

所以真正控制“离主平方有多近”的公共十进制参数是 \(k_{12}\)，而不是 DD 的 \(d_3\) 或 \(A_1\) 的 \(g\) 单独增长。

另一方面，将三次门 \(\Psi(T)\) 模 SGR depth quadratic 约化后，只需一次三次对二次的余式计算即可得到

\[
\boxed{
\mathcal A_\Sigma T+\mathcal B_\Sigma
=
\varepsilon_\Sigma X,
\qquad X=\square.
}
\tag{US-8}
\]

再消去 \(T\) 所得二次式的两个根，仍然只是 SGR depth roots 的仿射像。故上一轮的
\(\Phi_\Sigma\) 本身不会制造新的根间距：

\[
\boxed{
X_\pm
=
\frac{\mathcal B_\Sigma+\mathcal A_\Sigma T_\pm}
{\varepsilon_\Sigma}.
}
\tag{US-9}
\]

其判别式仍为

\[
\boxed{
\varepsilon_\Sigma^2
\mathcal A_\Sigma^2
(f_1^2-4f_2f_0).
}
\]

因此本轮确认：

> **真正有内容的 square-spacing 不应从 \(\Phi_\Sigma\) 的二次公式中寻找，而应在 Exact 判别平方被规范抽平方以后，直接研究 \(\varepsilon M^2-E\)。**

最后，\(E\) 与 actual-lift recovery 不是彼此无关。因为

\[
\widetilde\kappa
=
10^{m_3}\widehat Q\widehat G,
\]

有

\[
\widetilde\kappa+2h_3\widehat G
=
\widehat G
\left(
10^{m_3}\widehat Q+2h_3
\right),
\]

故

\[
\boxed{
v_p(E)
=
2v_p(\chi)
+v_p(\widehat Q)
+v_p(\widehat{\mathcal N})
+v_p(\widetilde\kappa+2h_3\widehat G)
-v_p(\widehat G),
\quad p=2,5.
}
\tag{US-10}
\]

于是 tail certificate

\[
10^\ell\mid\kappa^2(\kappa+2G)
\]

与 square-spacing error \(E\) 已经落在**同一个显式整数**上。这给出了本轮所要求的

\[
\boxed{
\text{square spacing}
+
(2,5)\text{-adic recovery}
}
\]

统一接口。

但现有 valuation capacity 尚不足以把 \(E\) 的强制模数推到超过其 Archimedean 大小，因此没有形成 SGR-3A/B。

本轮最终等级：

\[
\boxed{\textbf{SGR-3C — UNIFORM SQUARE-SPACING LEMMA}.}
\]

---

# 1. 来源审计与 strict-scope 修正

## 1.1 实际使用的来源

本轮重点使用：

- `strict_layer_unified_exact_lift_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`。

其中前者已经自包含重推：

- primitive-core / Exact-Lift 变量字典；
- fixed-state SGR depth quadratic；
- Exact 判别平方在 primitive-profile 坐标中的尺度消去；
- \(\widetilde\kappa\)、\(\widehat Q,\widehat G,\widehat{\mathcal N},\widehat C,\widehat D\)；
- resultant coupling；
- tail capacity。

后者用于回查：

- DD 既有 near-square；
- DD 顶部尖角；
- DD \(2/5\)-adic double resonance；
- \(A_1\) saturated 尾长界及仍开放的 \(g\)-shift。

### 关于 `strict_layer_global_reduction_campaign.md`

本轮再次以精确文件名、SGR-1、global reduction 等关键词检索 File Library，仍未重新暴露该报告正文。

因此本文不伪称重新读到了它；只使用上一轮统一报告已经自包含重推或明确冻结的 SGR-1 输入：

\[
\boxed{
\text{fixed primitive core}
\Longrightarrow
\text{finite decimal fibre},
}
\]

以及

\[
\boxed{
F_\Sigma(T)
=
f_2T^2+f_1T+f_0
=
0,
\qquad
T=10^{\ell(V)}.
}
\]

这足以完成本文全部新推导。

---

## 1.2 strict-scope 修正

严格层定义为

\[
\boxed{
\delta_2+\delta_3\ge1.
}
\]

而上一轮 carrier 字典中

\[
A_2\text{-only}:
\quad
\delta_3>0,\qquad
\delta_2+\delta_3\le0.
\]

结合已经冻结的全局条件

\[
\delta_2+\delta_3\ge0
\]

只能得到

\[
\delta_2+\delta_3=0.
\]

故

\[
\boxed{
A_2\text{-only 属于临界层，不属于严格层。
}
}
\]

本报告从此只研究

\[
\boxed{
DD,\qquad A_1\text{-only}.
}
\]

后文不使用 \(A_2\) 的 deep-even、source Hensel 或其他临界层结果。

---

# 2. 统一 primitive-profile 骨架

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

恢复

\[
a_i=UC_i,
\qquad
b_i=\frac V{g_i}.
\]

令

\[
L_g=\operatorname{lcm}(g_1,g_2,g_3),
\qquad
h_i=\frac{L_g}{g_i},
\qquad
R=\frac V{L_g}.
\]

则

\[
b_i=Rh_i.
\]

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

于是

\[
Q_{12}=R\widehat Q,
\qquad
G=R^2\widehat G,
\qquad
\mathcal N_{12}=U^2R^2\widehat{\mathcal N}.
\]

Exact 与 SGR 的共同 primitive normalization 是

\[
q=V,
\qquad
y_i=UP_i,
\qquad
H=UQ_0.
\]

SGR-1 的 finite-fibre theorem 因而给出

\[
\boxed{
\text{若 strict candidates 无穷，
则必有 }Q_0\to\infty.
}
\]

本轮所有“uniform”都指对这种 moving-core sequence 一致，而不是固定某一个 core 后继续拉长 decimal tail。

---

# 3. DD 与 \(A_1\)-only 的共同 coefficient form

定义

\[
\boxed{
\chi=
\begin{cases}
1,&DD,\\
10^g,&A_1\text{-only}.
\end{cases}
}
\]

于是两个 chamber 都满足

\[
\boxed{
\widehat D=\chi\widehat Q.
}
\tag{3.1}
\]

## 3.1 DD

记

\[
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0.
\]

有

\[
\boxed{
\widehat C
=
10^{m_2+k_{12}}C_1
+
10^{d_3}C_2.
}
\tag{3.2-DD}
\]

由于

\[
m_2+k_{12}
=
m_2+s_2+d_3
=
n_2+d_3,
\]

若定义

\[
A_{12}=a_1 10^{n_2}+a_2,
\qquad
\widehat A_{12}=\frac{A_{12}}U,
\]

则

\[
\boxed{
\widehat C=10^{d_3}\widehat A_{12},
\qquad
C=10^{d_3}A_{12}.
}
\tag{3.3-DD}
\]

---

## 3.2 \(A_1\)-only

记

\[
g=-s_3\ge0,
\qquad
k_{12}=s_2+s_3\ge1.
\]

于是

\[
s_2=g+k_{12}.
\]

已有 coefficient pair 为

\[
\widehat C
=
10^{g+k_{12}+m_2}C_1+C_2,
\qquad
\widehat D=10^g\widehat Q.
\]

但

\[
g+k_{12}+m_2
=
s_2+m_2
=
n_2.
\]

故实际上

\[
\boxed{
\widehat C=\widehat A_{12},
\qquad
C=A_{12}.
}
\tag{3.3-A1}
\]

所以两个 chamber 的差异可浓缩为

\[
\boxed{
\begin{array}{c|cc}
& C & D\\ \hline
DD&10^{d_3}A_{12}&Q_{12}\\
A_1&A_{12}&10^gQ_{12}
\end{array}
}
\tag{3.4}
\]

这张两行表将直接解释后面的 near-square 主项。

---

# 4. Exact 判别平方的规范降阶

已有统一判别平方为

\[
\boxed{
Z^2
=
\widetilde\kappa
\left(
\widetilde\kappa\widehat K
-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}
\right),
}
\tag{4.1}
\]

其中

\[
\boxed{
\widehat K
=
\widehat G^2\widehat C^2
-
\widehat D^2\widehat{\mathcal N},
}
\]

以及

\[
\boxed{
\widetilde\kappa
=
10^{m_3}\widehat Q\widehat G.
}
\tag{4.2}
\]

由 (3.1)

\[
\widehat D=\chi\widehat Q.
\]

代入 (4.1)：

\[
\begin{aligned}
Z^2
&=
10^{m_3}\widehat Q\widehat G
\left[
10^{m_3}\widehat Q\widehat G\widehat K
-
2h_3\widehat G\chi^2\widehat Q^2\widehat{\mathcal N}
\right]\\
&=
10^{m_3}
(\widehat Q\widehat G)^2
\left[
10^{m_3}\widehat K
-
2h_3\chi^2\widehat Q\widehat{\mathcal N}
\right].
\end{aligned}
\]

定义

\[
\boxed{
\Psi
:=
10^{m_3}\widehat K
-
2h_3\chi^2\widehat Q\widehat{\mathcal N}.
}
\tag{4.3}
\]

得到

\[
\boxed{
Z^2
=
10^{m_3}
(\widehat Q\widehat G)^2
\Psi.
}
\tag{4.4}
\]

因为 \(\widehat Q\widehat G\in\mathbf Z_{>0}\)，若其平方整除 \(Z^2\)，则

\[
\widehat Q\widehat G\mid Z.
\]

故存在 \(Z_1\in\mathbf Z_{>0}\) 使

\[
\boxed{
Z_1^2
=
10^{m_3}\Psi.
}
\tag{4.5}
\]

---

# 5. Decimal-square deflation lemma

## 定理 5.1 — 十进制平方抽取

若正整数 \(\Psi\) 满足

\[
Z_1^2=10^m\Psi,
\]

则

\[
\boxed{
\Psi=
\begin{cases}
Y^2,&m\text{ 偶},\\
10Y^2,&m\text{ 奇},
\end{cases}
}
\]

其中 \(Y\in\mathbf Z_{>0}\)。

### 证明

若

\[
m=2r,
\]

则

\[
Z_1^2=10^{2r}\Psi.
\]

由 \(10^{2r}\mid Z_1^2\) 得 \(10^r\mid Z_1\)。写

\[
Z_1=10^rY
\]

即可得到

\[
\Psi=Y^2.
\]

若

\[
m=2r+1,
\]

则

\[
Z_1^2=10^{2r+1}\Psi.
\]

对 \(p=2,5\)，\(v_p(Z_1^2)\ge2r+1\)，故

\[
v_p(Z_1)\ge r+1.
\]

于是

\[
10^{r+1}\mid Z_1.
\]

写

\[
Z_1=10^{r+1}Y,
\]

则

\[
10^{2r+2}Y^2
=
10^{2r+1}\Psi,
\]

所以

\[
\Psi=10Y^2.
\]

证毕。

应用于 (4.5)：

\[
\boxed{
\Psi
=
\varepsilon Y^2,
\qquad
\varepsilon=
\begin{cases}
1,&m_3\text{ 偶},\\
10,&m_3\text{ 奇}.
\end{cases}
}
\tag{5.1}
\]

这一步已经把原次数至多 \(6\) 的平方门压成了 \(\Psi\) 的 square/\(10\)-square 门。

---

# 6. 精确主项—误差分解

由

\[
\widehat K
=
\widehat G^2\widehat C^2
-
\chi^2\widehat Q^2\widehat{\mathcal N},
\]

(4.3) 化为

\[
\boxed{
\Psi
=
10^{m_3}\widehat G^2\widehat C^2
-
\chi^2\widehat Q\widehat{\mathcal N}
\left(
10^{m_3}\widehat Q+2h_3
\right).
}
\tag{6.1}
\]

定义

\[
\boxed{
M=
10^{\lfloor m_3/2\rfloor}
\widehat G\widehat C,
}
\tag{6.2}
\]

以及

\[
\boxed{
E=
\chi^2\widehat Q\widehat{\mathcal N}
\left(
10^{m_3}\widehat Q+2h_3
\right).
}
\tag{6.3}
\]

则

\[
10^{m_3}\widehat G^2\widehat C^2
=
\varepsilon M^2.
\]

结合 (5.1)：

\[
\boxed{
\varepsilon M^2-E
=
\varepsilon Y^2.
}
\tag{6.4}
\]

即

\[
\boxed{
E
=
\varepsilon(M^2-Y^2)
=
\varepsilon(M-Y)(M+Y).
}
\tag{6.5}
\]

由于 \(E>0\)，有

\[
0<Y<M.
\]

所以 \(Y\le M-1\)，从而

\[
M-Y\ge1,
\qquad
M+Y\ge2M-1.
\]

得到

\[
\boxed{
E\ge\varepsilon(2M-1).
}
\tag{6.6}
\]

这就是本轮的核心 uniform square-spacing theorem。

---

# 7. Uniform Square-Spacing Lemma

## 定理 SGR-3C.1

对任意 DD 或 \(A_1\)-only 完整 strict candidate，令 \(M,E,\varepsilon\) 如 (6.2)–(6.3)，则必有

\[
\boxed{
E\ge\varepsilon(2M-1).
}
\]

因此若某个 moving-core state 满足

\[
\boxed{
0<E<\varepsilon(2M-1),
}
\]

则该 state 不可完整提升。

该结论：

- 不要求固定 primitive core；
- 不要求 \(Q_0\) 有界；
- 不要求 \(m_3\) 偶；
- 不要求 \(f_2\neq0\)；
- 不要求 resultant 非退化；
- 同时覆盖 DD 与 \(A_1\)-only。

所以它没有 generic-case 漏洞。

---

## 7.1 无量纲误差

定义

\[
\boxed{
\rho
:=
\frac{E}{\varepsilon M^2}.
}
\]

由

\[
\varepsilon M^2
=
10^{m_3}\widehat G^2\widehat C^2
\]

得到

\[
\boxed{
\rho
=
\frac{
\chi^2\widehat Q^2\widehat{\mathcal N}
}{
\widehat G^2\widehat C^2
}
\left(
1+\frac{2h_3}{10^{m_3}\widehat Q}
\right).
}
\tag{7.1}
\]

换回原 Exact 变量，尺度 \(U,R\) 完全消去：

\[
\boxed{
\rho
=
\frac{
D^2\mathcal N_{12}
}{
G^2C^2
}
\left(
1+\frac{2b_3}{10^{m_3}Q_{12}}
\right).
}
\tag{7.2}
\]

候选还必须满足 \(\Psi>0\)，所以

\[
\rho<1.
\]

而 (6.6) 给出

\[
\rho
\ge
\frac{2M-1}{M^2}.
\]

故

\[
\boxed{
\frac2M-\frac1{M^2}
\le
\rho
<1.
}
\tag{7.3}
\]

这比“\(\rho\to0\)”之类渐近描述严格得多：它给出候选必须保持的精确平方格点安全距离。

---

# 8. DD：旧 near-square 是统一主项的局部表现

DD 中

\[
C=10^{d_3}A_{12},
\qquad
D=Q_{12}.
\]

所以

\[
\boxed{
\rho_{DD}
=
10^{-2d_3}
\frac{
Q_{12}^2\mathcal N_{12}
}{
G^2A_{12}^2
}
\left(
1+\frac{2b_3}{10^{m_3}Q_{12}}
\right).
}
\tag{8.1}
\]

因此 \(d_3\) 的巨大 surplus 确实在统一判别平方中表现为一个显式的

\[
10^{-2d_3}
\]

near-square 因子。

这说明旧 Exact-Lift 在 DD 顶部看到的 near-square 不是偶然的局部技巧；它是统一判别平方主项

\[
\varepsilon M^2
\]

的 DD 投影。

不过 \(d_3\) 大本身仍不足以关闭，因为

\[
\frac{\mathcal N_{12}}{A_{12}^2}
\]

可以同时因 \(s_1,s_2\) 的方向而放大。

---

## 8.1 一个完全显式的 digit upper bound

由

\[
Q_{12}=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\]

有

\[
\frac{Q_{12}}G
=
\frac{10^{m_2}}{b_2}
+
\frac1{b_1}.
\]

因此

\[
\boxed{
1<
\frac{Q_{12}}G
<11.
}
\tag{8.2}
\]

又因

\[
b_3<10^{m_3},
\qquad
Q_{12}\ge11,
\]

有

\[
\boxed{
1<
1+\frac{2b_3}{10^{m_3}Q_{12}}
<
\frac{13}{11}.
}
\tag{8.3}
\]

而

\[
A_{12}>a_1 10^{n_2}.
\]

故

\[
\frac{a_1b_2}{A_{12}}
<
\frac{b_2}{10^{n_2}}
<
10^{-s_2},
\]

并且

\[
\frac{a_2b_1}{A_{12}}
<
\frac{b_1}{a_1}
<
10^{1-s_1}.
\]

所以

\[
\frac{\mathcal N_{12}}{A_{12}^2}
<
10^{-2s_2}
+
10^{2(1-s_1)}.
\]

代入 (8.1)：

\[
\boxed{
\rho_{DD}
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

这里使用

\[
k_{12}=d_3+s_2.
\]

因此一个充分死亡条件是

\[
143
\left[
10^{-2k_{12}}
+
10^{2(1-d_3-s_1)}
\right]
<
\frac2M-\frac1{M^2}.
\tag{8.5}
\]

当前已有 DD 顶部结构尚不能对所有 moving cores 统一推出 (8.5)。

所以 DD 未关闭。

---

# 9. \(A_1\)-only：为什么 \(g\to\infty\) 不被裸 square-spacing 自动杀死

\(A_1\)-only 中

\[
C=A_{12},
\qquad
D=10^gQ_{12}.
\]

于是

\[
\boxed{
\rho_{A_1}
=
10^{2g}
\frac{
Q_{12}^2\mathcal N_{12}
}{
G^2A_{12}^2
}
\left(
1+\frac{2b_3}{10^{m_3}Q_{12}}
\right).
}
\tag{9.1}
\]

同时

\[
s_2=g+k_{12},
\qquad
n_2=m_2+g+k_{12}.
\]

所以 \(A_{12}\) 自身含一个随 \(g\) 同步增长的十进制块。

同样的 digit estimate 给出

\[
\boxed{
\rho_{A_1}
<
143
\left[
10^{-2k_{12}}
+
10^{2(g+1-s_1)}
\right].
}
\tag{9.2}
\]

更重要的是，可以得到一个两 chamber 共同的严格下界。

---

# 10. 一个共同的 \(k_{12}\)-floor

因为

\[
A_{12}
<
(a_1+1)10^{n_2}
\le
2a_1 10^{n_2},
\]

且

\[
\mathcal N_{12}
\ge
(a_1b_2)^2,
\]

再利用

\[
b_2\ge10^{m_2-1},
\qquad
Q_{12}/G>1,
\]

可得：

### DD

\[
\begin{aligned}
\rho_{DD}
&>
10^{-2d_3}
\left(
\frac{a_1b_2}{A_{12}}
\right)^2\\
&>
10^{-2d_3}
\left(
\frac{10^{m_2-1}}{2\cdot10^{n_2}}
\right)^2\\
&=
\frac1{400}
10^{-2(d_3+s_2)}.
\end{aligned}
\]

由于

\[
d_3+s_2=k_{12},
\]

得到

\[
\rho_{DD}
>
\frac1{400}10^{-2k_{12}}.
\]

### \(A_1\)

同理

\[
\begin{aligned}
\rho_{A_1}
&>
10^{2g}
\left(
\frac{a_1b_2}{A_{12}}
\right)^2\\
&>
10^{2g}
\left(
\frac{10^{m_2-1}}{2\cdot10^{n_2}}
\right)^2\\
&=
\frac1{400}
10^{-2(s_2-g)}\\
&=
\frac1{400}10^{-2k_{12}}.
\end{aligned}
\]

因此统一得到

\[
\boxed{
\rho
>
\frac1{400}10^{-2k_{12}}.
}
\tag{10.1}
\]

这说明：

\[
\boxed{
\text{DD 的 }d_3
\text{ 与 }A_1\text{ 的 }g
\text{ 并不是统一 near-square 精度的真正自由参数；}
}
\]

真正共同控制误差能够压到多小的十进制量是

\[
\boxed{k_{12}.}
\]

对 \(A_1\) saturated 的危险序列尤其重要：

> 单纯令 \(g\to\infty\) 并不会迫使 \(\rho\to0\)。因此“主平方 + 相邻平方间距”这一机制不能仅靠 \(g\) 的无界性自动关闭 \(A_1\)。

这不是说 \(A_1\) 不可能被 square-spacing + arithmetic 关闭；只是证明**纯 Archimedean 的 \(g\)-large near-square 路线并不存在**。

---

# 11. 把新三次门放回 SGR depth quadratic

固定完整 moving state \(\Sigma\)。

SGR depth gate 写成

\[
\boxed{
F_\Sigma(T)
=
f_2T^2+f_1T+f_0
=
0,
\qquad
T=10^v,
}
\tag{11.1}
\]

且

\[
\boxed{
f_0\ne0.
}
\]

在未清分母的 primitive-profile 形式中，

\[
F_2
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
\]

\[
F_1
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
\]

\[
\boxed{
F_0=h_3(P_3-Q_0)<0.
}
\tag{11.2}
\]

乘最小必要的 \(10\)-幂可得到整数 \(f_i\)。

---

# 12. \(\Psi_\Sigma(T)\) 的 DD / \(A_1\) 统一展开

令

\[
\alpha_2
=
10^{-\gamma_2+1-\eta_2},
\qquad
\alpha_3
=
10^{-\gamma_3+1-\eta_3}.
\]

于是

\[
10^{m_2}=\alpha_2T,
\qquad
10^{m_3}=\alpha_3T.
\]

定义

\[
q_1=h_1\alpha_2,
\qquad
q_0=h_2,
\]

所以

\[
\widehat Q=q_1T+q_0.
\]

再写

\[
\widehat C=c_1T+c_0.
\]

两个 chamber 分别为：

\[
\boxed{
\begin{array}{c|cc}
&c_1&c_0\\ \hline
DD&
10^{k_{12}}C_1\alpha_2&
10^{d_3}C_2\\[1mm]
A_1&
10^{g+k_{12}}C_1\alpha_2&
C_2
\end{array}
}
\tag{12.1}
\]

令

\[
G_*=\widehat G,
\qquad
N_*=\widehat{\mathcal N}.
\]

因为

\[
\widehat D=\chi\widehat Q,
\]

有

\[
\widehat K
=
K_2T^2+K_1T+K_0,
\]

其中

\[
\boxed{
K_2
=
G_*^2c_1^2-\chi^2N_*q_1^2,
}
\]

\[
\boxed{
K_1
=
2\left(
G_*^2c_1c_0-\chi^2N_*q_1q_0
\right),
}
\]

\[
\boxed{
K_0
=
G_*^2c_0^2-\chi^2N_*q_0^2.
}
\tag{12.2}
\]

于是

\[
\Psi_\Sigma(T)
=
\psi_3T^3+\psi_2T^2+\psi_1T+\psi_0,
\]

其中

\[
\boxed{
\psi_3=\alpha_3K_2,
}
\]

\[
\boxed{
\psi_2=\alpha_3K_1,
}
\]

\[
\boxed{
\psi_1
=
\alpha_3K_0
-
2h_3\chi^2N_*q_1,
}
\]

\[
\boxed{
\psi_0
=
-2h_3\chi^2N_*q_0
=
-2h_2h_3\chi^2N_*
<0.
}
\tag{12.3}
\]

这是一项重要简化：

\[
\boxed{
\deg_T\Psi_\Sigma\le3,
}
\]

而上一轮直接使用的

\[
\mathscr P_\Sigma(T)=Z^2
\]

次数至多 \(6\)。

---

# 13. 三次门模 SGR 二次门：显式 \((\mathcal A,\mathcal B)\)

由于 \(\psi_i\) 可能含负的十进制指数，取最小 \(e_\Sigma\ge0\) 使

\[
10^{2e_\Sigma}\psi_i\in\mathbf Z
\]

对所有 \(i\) 成立。

定义

\[
\overline\Psi
=
10^{2e_\Sigma}\Psi
=
\bar\psi_3T^3+\bar\psi_2T^2+\bar\psi_1T+\bar\psi_0.
\]

因为乘子是完整平方，

\[
\overline\Psi
=
\varepsilon\overline Y^2
\]

仍保持 square/\(10\)-square 类型。

若

\[
f_2\ne0,
\]

由

\[
T^2
\equiv
-\frac{f_1}{f_2}T-\frac{f_0}{f_2}
\pmod{F},
\]

\[
T^3
\equiv
\frac{f_1^2-f_0f_2}{f_2^2}T
+
\frac{f_0f_1}{f_2^2}
\pmod{F},
\]

得到

\[
f_2^2\overline\Psi(T)
=
\mathcal A T+\mathcal B
\]

在所有 \(F(T)=0\) 的根上成立，其中

\[
\boxed{
\mathcal A
=
\bar\psi_1f_2^2
-
\bar\psi_2f_1f_2
+
\bar\psi_3(f_1^2-f_0f_2),
}
\tag{13.1}
\]

\[
\boxed{
\mathcal B
=
\bar\psi_0f_2^2
-
\bar\psi_2f_0f_2
+
\bar\psi_3f_0f_1.
}
\tag{13.2}
\]

因此完整候选满足

\[
\boxed{
\mathcal A T+\mathcal B
=
\varepsilon
(f_2\overline Y)^2.
}
\tag{13.3}
\]

令

\[
X=(f_2\overline Y)^2.
\]

则

\[
\boxed{
\mathcal A T+\mathcal B
=
\varepsilon X.
}
\tag{13.4}
\]

这就是上一轮 \(AT+B=X\) 的一个更低次数、规范化后的版本。

---

# 14. 新 \(\Phi_\Sigma\) 及其根位置

若

\[
\mathcal A\ne0,
\]

则

\[
T
=
\frac{\varepsilon X-\mathcal B}{\mathcal A}.
\]

代回

\[
f_2T^2+f_1T+f_0=0
\]

得

\[
\boxed{
\Phi_\Sigma^{\rm defl}(X)
=
f_2\varepsilon^2X^2
+
\varepsilon(f_1\mathcal A-2f_2\mathcal B)X
+
f_2\mathcal B^2
-f_1\mathcal A\mathcal B
+f_0\mathcal A^2
=
0.
}
\tag{14.1}
\]

更重要的是，这是恒等式

\[
\boxed{
\Phi_\Sigma^{\rm defl}(X)
=
\mathcal A^2
F_\Sigma
\left(
\frac{\varepsilon X-\mathcal B}{\mathcal A}
\right).
}
\tag{14.2}
\]

因此若

\[
T_\pm
=
\frac{-f_1\pm\sqrt{\Delta_F}}{2f_2},
\qquad
\Delta_F=f_1^2-4f_2f_0,
\]

则

\[
\boxed{
X_\pm
=
\frac{
\mathcal B+\mathcal A T_\pm
}{\varepsilon}.
}
\tag{14.3}
\]

而

\[
\boxed{
\operatorname{disc}_X
\Phi_\Sigma^{\rm defl}
=
\varepsilon^2\mathcal A^2
\Delta_F.
}
\tag{14.4}
\]

如果 \(T\) 本身是整数 SGR root，则

\[
\Delta_F
=
(2f_2T+f_1)^2.
\]

所以：

\[
\boxed{
\Phi_\Sigma\text{ 的根判别式没有增加任何新的平方信息。}
}
\]

这严格解释了为什么“直接对 \(\Phi_\Sigma\) 的二次公式做 \(Q_0\)-渐近”不是正确的主攻点。

真正需要离散化的是：

\[
\boxed{
X\text{ 必须本身是平方},
}
\]

而最佳规范坐标正是第 6 节的

\[
\boxed{
\varepsilon M^2-E=\varepsilon Y^2.
}
\]

---

# 15. moving primitive-core height：为什么不存在纯 \(Q_0\) 单变量主项

上一轮希望寻找

\[
X
=
M_\Sigma(Q_0)^2+E_\Sigma(Q_0).
\]

本轮得到的结论更精确，但也指出一个必要修正：

\[
\boxed{
M,E\text{ 必须依赖完整 moving state，
不能只依赖 }Q_0.
}
\]

最简单的证据来自 SGR depth constant term：

\[
F_0=h_3(P_3-Q_0).
\]

球面恒等式给出

\[
\boxed{
Q_0-P_3
=
\frac{P_1^2+P_2^2}{Q_0+P_3}.
}
\tag{15.1}
\]

即使只看 primitive sphere cores，\(Q_0-P_3\) 相对 \(Q_0\) 的尺度也没有 uniform 单一行为。

例如，对任意 \(t\ge1\)，

\[
\boxed{
(1,\,2t,\,2t^2,\,2t^2+1)
}
\]

满足

\[
1^2+(2t)^2+(2t^2)^2=(2t^2+1)^2
\]

且整体 primitive，并且

\[
Q_0-P_3=1.
\]

而坐标置换

\[
\boxed{
(2t,\,2t^2,\,1,\,2t^2+1)
}
\]

同样 primitive，但

\[
Q_0-P_3=2t^2=Q_0-1.
\]

因此沿 moving primitive cores，

\[
Q_0-P_3
\]

可以从 \(O(1)\) 到 \(\asymp Q_0\) 变化。

这并不证明这些示例本身能通过 DD/\(A_1\) decimal recovery；它只严格说明：

> 在尚未把 chamber/recovery 数据耦合进去以前，不存在从 sphere equation 单独导出的统一 \(Q_0\)-only first correction。

所以本轮采用的正确 uniform 量是

\[
(M_\Sigma,E_\Sigma,\rho_\Sigma),
\]

而不是试图强制把所有 moving states 投影为一个 \(Q_0\) 的单变量渐近级数。

---

# 16. square-spacing 与 \(2,5\)-adic recovery 落在同一个误差 \(E\) 上

已有

\[
\widetilde\kappa
=
10^{m_3}\widehat Q\widehat G.
\]

故

\[
\boxed{
\widetilde\kappa+2h_3\widehat G
=
\widehat G
\left(
10^{m_3}\widehat Q+2h_3
\right).
}
\tag{16.1}
\]

而

\[
E
=
\chi^2\widehat Q\widehat{\mathcal N}
\left(
10^{m_3}\widehat Q+2h_3
\right).
\]

所以对任意素数 \(p\)，

\[
\boxed{
v_p(E)
=
2v_p(\chi)
+
v_p(\widehat Q)
+
v_p(\widehat{\mathcal N})
+
v_p(\widetilde\kappa+2h_3\widehat G)
-
v_p(\widehat G).
}
\tag{16.2}
\]

特别对

\[
p=2,5.
\]

另一方面 actual-lift tail certificate 给出

\[
10^\ell
\mid
\kappa^2(\kappa+2G),
\]

而 primitive-profile capacity 为

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
\tag{16.3}
\]

于是

\[
\boxed{
v_p(\widetilde\kappa+2h_3\widehat G)
\ge
\ell
-
6v_p(R)
-
2v_p(\widetilde\kappa)
+
3v_p(h_3).
}
\tag{16.4}
\]

代入 (16.2) 得

\[
\boxed{
\begin{aligned}
v_p(E)
\ge\;&
2v_p(\chi)
+v_p(\widehat Q)
+v_p(\widehat{\mathcal N})
-v_p(\widehat G)\\
&+\ell
-6v_p(R)
-2v_p(\widetilde\kappa)
+3v_p(h_3).
\end{aligned}
}
\tag{16.5}
\]

这就是 requested arithmetic coupling。

此外由

\[
E
=
\varepsilon(M-Y)(M+Y)
\]

还有

\[
\boxed{
v_p(E)-v_p(\varepsilon)
=
v_p(M-Y)+v_p(M+Y).
}
\tag{16.6}
\]

所以 Archimedean square spacing 与 \(2,5\)-adic recovery 已不再是两个互不相关的变量系统：

\[
\boxed{
\text{二者都约束同一个 }E.
}
\]

---

## 16.1 为什么这一步还没有闭合

若 (16.5) 能统一给出某个 \(r\) 使

\[
10^r\mid E
\]

并且同时由 DD/\(A_1\) 的 Archimedean bounds 得到

\[
0<E<10^r,
\]

立即矛盾。

但当前粗 capacity 中

\[
2v_p(\widetilde\kappa)
\]

本身可能吸收大量 tail demand，使 (16.4) 的右端变成非正数。

因此仅靠现有 unified tail certificate 尚不能保证

\[
v_p(E)
\]

随 \(Q_0\) 或 \(m_3\) 线性增长到足以超过 \(\log E\)。

DD 顶部已有更强的 double resonance，但它目前作用在 \((\mu,\nu)\) 的 near-square factorization 上；尚缺一个严格传递引理，把该 resonance 转成对本轮 \(E\) 的统一高模数。

这正是一个可接受的 terminal gap，而不是新的大分类。

---

# 17. 全部退化状态

## 17.1 \(f_2=0\)

因为

\[
f_0\ne0,
\]

若

\[
f_2=0,
\]

则 SGR gate 是真正线性的：

\[
\boxed{
f_1T+f_0=0.
}
\]

若同时 \(f_1=0\)，则 \(f_0=0\)，矛盾。

所以

\[
\boxed{
f_2=f_1=0
\Longrightarrow
\text{无候选}.
}
\]

而 \(f_2=0,\ f_1\ne0\) 时

\[
\boxed{
T=-\frac{f_0}{f_1}
}
\]

唯一确定，并必须是正的 \(10\) 的幂；再直接检查第 5–7 节的 uniform square-spacing gate。

因此 \(f_2=0\) 不造成 proof hole。

---

## 17.2 \(\mathcal A=0\)

在第 13 节若

\[
\mathcal A=0,
\]

则 (13.3) 退化为

\[
\boxed{
\mathcal B
=
\varepsilon(f_2\overline Y)^2.
}
\]

这不再消去 \(T\)，但它是一个固定 state 的 square/\(10\)-square test。

重要的是：

\[
\boxed{
\mathcal A=0
\text{ 并不逃出第 6–7 节的 }M^2-E\text{ 定理}.
}
\]

所以本轮不需要把 \(\mathcal A=0\) 宣称为“有限多个 profile”才能保证 square-spacing 定理完整。

目前没有证明 \(\mathcal A=0\) 在 moving cores 中只发生有限次，因此也不作该断言。

---

## 17.3 SGR 重根

若

\[
\Delta_F=0,
\]

则

\[
T=-\frac{f_1}{2f_2}
\]

是重根。

此时

\[
\Phi_\Sigma^{\rm defl}
\]

也只有一个重根，因为

\[
\operatorname{disc}\Phi
=
\varepsilon^2\mathcal A^2\Delta_F.
\]

所以 resultant root separation 完全消失。

但第 6–7 节的 square-spacing 仍然有效，因为其平方中心来自 Exact 判别式本身，而不是来自两个 \(\Phi\)-roots 的间距。

---

## 17.4 \(\Psi\) 降阶

可能出现

\[
\psi_3=0
\]

甚至

\[
\psi_3=\psi_2=0.
\]

这只意味着三次 polynomial representation 降阶。

由于

\[
M>0,
\qquad
E>0
\]

始终成立，精确式

\[
\varepsilon M^2-E=\varepsilon Y^2
\]

不退化。

所以本轮的主 square-spacing lemma 对这些状态仍完整覆盖。

---

# 18. 本轮实际证明等级

## PROVED — NEW

1. **strict-scope correction**
   \[
   \boxed{
   \text{Strict Layer}=DD\cup A_1\text{-only}
   }
   \]
   （在本轮冻结条件下）；\(A_2\)-only 不再进入严格层研究。

2. **Exact square factorization**
   \[
   \boxed{
   Z^2
   =
   10^{m_3}(\widehat Q\widehat G)^2\Psi
   }
   \]
   对 DD 与 \(A_1\)-only 统一成立。

3. **decimal-square deflation**
   \[
   \boxed{
   \Psi=\square
   \quad\text{或}\quad
   \Psi=10\square
   }
   \]
   只由 \(m_3\) 奇偶决定。

4. **degree reduction**
   \[
   \boxed{
   \deg_T\Psi\le3
   }
   \]
   相比上一轮 \(\deg\mathscr P\le6\) 严格降阶。

5. **uniform exact main term / error**
   \[
   \boxed{
   \varepsilon M^2-E=\varepsilon Y^2.
   }
   \]

6. **uniform square-spacing lemma**
   \[
   \boxed{
   E\ge\varepsilon(2M-1).
   }
   \]

7. **scale-free normalized spacing window**
   \[
   \boxed{
   \frac2M-\frac1{M^2}
   \le\rho<1.
   }
   \]

8. **common \(k_{12}\)-floor**
   \[
   \boxed{
   \rho>\frac1{400}10^{-2k_{12}}.
   }
   \]

9. **显式 cubic-to-linear reduction**
   \[
   \boxed{
   \mathcal A T+\mathcal B
   =
   \varepsilon X,\quad X=\square.
   }
   \]

10. **resultant root inheritance**
    \[
    \boxed{
    X_\pm
    =
    \frac{\mathcal B+\mathcal A T_\pm}{\varepsilon};
    }
    \]
    因此 \(\Phi\) 的根渐近本身不产生新信息。

11. **square-error / recovery valuation coupling**
    \[
    \boxed{
    v_p(E)
    =
    2v_p(\chi)+v_p(\widehat Q)+v_p(\widehat{\mathcal N})
    +v_p(\widetilde\kappa+2h_3\widehat G)
    -v_p(\widehat G).
    }
    \]

---

## DERIVED FROM PROVED RESULTS

1. 任意无穷 strict candidate sequence 必有
   \[
   Q_0\to\infty.
   \]

2. DD 旧 near-square 是统一 \(\rho\) 中
   \[
   10^{-2d_3}
   \]
   因子的局部表现。

3. \(A_1\) 中单纯 \(g\to\infty\) 不会自动令统一 normalized error \(\rho\to0\)；因此裸 Archimedean adjacent-square mechanism 不能单独终止 saturated \(g\)-escape。

---

## 未证明

本轮没有证明：

\[
DD=\varnothing,
\]

没有证明：

\[
A_1=\varnothing,
\]

也没有证明：

\[
Q_0\gg1
\Longrightarrow
\text{无 strict candidate}.
\]

因此不能标为 SGR-3A 或 SGR-3B。

---

# 19. 为什么等级是 SGR-3C，而不是 SGR-3D/E

本轮已经得到一个对全部 DD 与 \(A_1\)-only moving states 严格有效的 square-spacing theorem：

\[
\boxed{
0<E<\varepsilon(2M-1)
\Longrightarrow
\text{不可能为完整候选}.
}
\]

而且 \(M,E\) 都是显式整数表达式，没有 \(o(1)\)、\(O(\cdot)\) 或数值实验。

因此已经达到：

\[
\boxed{
\textbf{SGR-3C — UNIFORM SQUARE-SPACING LEMMA}.
}
\]

但还没有把现有 DD/A1 的全部约束推到该死亡区，所以没有 chamber closure。

同时也不能标 SGR-3E：resultant 二次公式作为独立路线确实被证明是信息继承，但 square-spacing 方向本身并未失败；它已经在规范降阶后的 \(M^2-E\) 坐标中形成真正的新统一定理。

---

# 20. 下一轮只留下两个最小 terminal gaps

## Gap 1 — DD normalized-error closure

当前 DD 顶部仍为既有尖角：

\[
10S_{12}+11
\le n_3\le
11S_{12}+3
\]

并带 double resonance、near-\(S\)-unit、极端 denominator asymmetry。

本轮把下一步精确压成：

\[
\boxed{
\text{证明该 moving-core 尖角统一满足 }
\rho_{DD}
<
\frac2M-\frac1{M^2},
}
\]

或者证明对某个 \(p\in\{2,5\}\)

\[
p^r\mid E,
\qquad
0<E<p^r.
\]

不需要再寻找新的 DD 分类。

---

## Gap 2 — \(A_1\) recovery synchronization

对 \(A_1\) saturated 的 moving \(g\)-escape，本轮证明裸 \(g\)-large square-spacing 不会自动关闭它。

因此剩余最小任务不是继续做实数近似，而是：

\[
\boxed{
\text{把 }
10^\ell\mid\kappa^2(\kappa+2G)
\text{、}
E=\varepsilon(M-Y)(M+Y)
\text{ 与 moving-core state 联立，
得到 }g\text{ 或 }k_{12}\text{ 的统一高度约束。}
}
\]

理想终端形式仍是

\[
M_{\rm adic}\mid E,
\qquad
0<E<M_{\rm adic},
\]

或直接得到

\[
g\le C\,\ell(Q_0)+O(1)
\]

并与 SGR/decimal state 的另一侧高度关系冲突。

不再增加新的 \(A_1\) 子分类。

---

# 21. 最终状态

\[
\boxed{
\textbf{SGR-3C — UNIFORM SQUARE-SPACING LEMMA}
}
\]

本轮最重要的简化不是一个新的 resultant，而是：

\[
\boxed{
\text{degree-6 square gate}
\Longrightarrow
\text{degree-3 square/10-square gate}
\Longrightarrow
\varepsilon M^2-E=\varepsilon Y^2.
}
\]

从此 moving-core square-spacing 的真正终端变量可以固定为

\[
\boxed{
(M,E,\rho)
}
\]

而不需要继续围绕 \(\Phi_\Sigma\) 的二次根公式增加分类。

当前只剩：

\[
\boxed{
\text{DD：把 }\rho\text{ 压入相邻平方禁区};
}
\]

\[
\boxed{
A_1：把 recovery 的 }2/5\text{-进容量真正传递到同一个 }E.
}
\]

这两项之外，本轮不建议再扩张 strict-layer terminal list。
