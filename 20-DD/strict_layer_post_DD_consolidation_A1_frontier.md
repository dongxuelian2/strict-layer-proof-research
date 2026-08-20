# 三项十进制拼接平方和问题：Strict Layer Post-DD Consolidation & A1 Frontier

**文件名：** `strict_layer_post_DD_consolidation_A1_frontier.md`  
**轮次：** SGR-10 — Post-DD Consolidation / A1-only Frontier Rebuild  
**最终等级：**

\[
\boxed{\textbf{SGR-10B — CONSOLIDATION + A1 REDUCTION}}
\]

**核心结论：**

\[
\boxed{DD=\varnothing}
\]

已经可以正式接入 Strict-Layer 主依赖链；严格层因此只剩

\[
\boxed{A_1\text{-only}.}
\]

更重要的是，重新审计 \(A_1\) 后，旧的 gap quadratic、primitive-tail quadratic、discriminant/resultant、square-spacing 等不再应被并列为 frontier。当前最短的 exact terminal language 是：

\[
\boxed{
\text{A1 denominator–decimal trace }T
+
\text{full numerator word }\mathbf A
+
\text{至多一个二元 prefix-cut label}.
}
\]

其中真正未解决的不是“某个 quadratic 是否有根”，而是：

\[
\boxed{
\text{是否存在一个 legal decimal cut，使同一完整 word 同时满足}
\text{ exact norm realization、逐块既约与 A1 digit cell。}
}
\]

---

# 1. Source audit

本轮重点核对并交叉使用：

- `strict_layer_DD_oriented_tail_window_campaign.md`
- `strict_layer_DD_orientation_recovery_campaign.md`
- `strict_layer_DD_error_closure_campaign.md`
- `strict_layer_DD_post_deflation_campaign.md`
- `strict_layer_DD_supply_phase_synchronization_campaign.md`
- `strict_layer_unified_exact_lift_campaign.md`
- `strict_layer_unified_exact_lift_campaign(1).md`
- `strict_layer_moving_core_square_spacing_campaign.md`
- `exact_lift_research_synthesis_2026-08-10.md`
- `strict_layer_final_campaign.md`
- `strict_layer_backward_denominator_decimal_interface.md`
- `strict_layer_backward_algebraic_denominator_interface.md`
- `strict_layer_backward_exact_root_pair_fibre_campaign.md`
- backward global recovery / synchronization 系列报告。

后面三个 backward 文件尤其重要，因为它们已经对旧 \(A_1\) quadratic/recovery presentation 做了比 2026-08-10 synthesis 更晚、更严格的消元审计。

---

# 2. SGR-9 DD closure dependency audit

## 2.1 旧 DD 最终开放区域

此前 DD reduction 的冻结结论是：

\[
\boxed{
\text{DD 的唯一 surviving open core 是 top DD chamber.}
}
\]

该区域满足

\[
10S+11\le n_3\le 11S+3,
\]

\[
d_3\le5S,
\]

并因此

\[
m_3=n_3-d_3\ge5S+11.
\]

同时 top DD 已进入 \(5\)-adic resonance；更高阈值下旧分析还得到 \(2\)-adic resonance，但 SGR-9 的最终矛盾只需要 \(p=5\)。

**状态：AUDITED / inherited PROVED reduction.**

本轮未发现 pre-SGR-9 reduction 的新量词缺口。SGR-9 本身明确把自己的结论表述为“relative to the frozen pre-SGR-9 reductions”；本轮核对到的后续 DD 文件也一致把 top chamber 视为唯一开放核，而不是某个示例子区域。

---

## 2.2 Double resonance 的覆盖范围

SGR-9 所需的实际输入是：

\[
v_5(F_-)=v_5(F_+)
\]

在 current top DD 上成立。

旧 DD resonance theorem 在更低阈值已经给出 \(5\)-adic resonance，而 current top DD 满足更强的

\[
n_3\ge10S+11.
\]

所以 SGR-9 使用的 \(5\)-adic resonance 覆盖整个最终开放区域。

**状态：AUDITED.**

注意：SGR-9 最终 contradiction 不需要把 \(2\)-adic resonance 当作 decisive input。

---

## 2.3 Orientation theorem 的覆盖范围

SGR-8 的研究范围就是 **current open DD top chamber**。它从原六变量 decimal equation 重新导出 third-tail quadratic，证明 gap root 到 \(a_3\) 的恢复是严格单调的，并证明 Vieta 共轭支在 top DD 恢复出负第三分子。

因此对任意 top-DD original candidate：

\[
\boxed{
\omega_{\rm src}=+1,
}
\]

\[
\boxed{
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp,
\qquad
F_-<F_+.
}
\]

**状态：AUDITED / PROVED.**

这不是一个任意 DD 或任意 chamber 的 gauge choice，而是 top-DD decimal magnitude + positivity 推出的 theorem。

---

## 2.4 Source-labelled factorization 是否引入额外假设

令

\[
h=\gcd(\kappa,G),
\qquad
A_\kappa=\frac{\kappa}{h},
\qquad
D=\frac Gh,
\qquad
B_\kappa=\frac{\kappa+2G}{h}.
\]

SGR-8 已证：

\[
B_\kappa\mid F_-,
\qquad
A_\kappa\mid F_+,
\]

以及

\[
A_\kappa\mid10^{m_3}Q.
\]

故可定义

\[
c=\frac{10^{m_3}Q}{A_\kappa}\in\mathbf Z_{>0},
\]

并得到

\[
b_3=cD.
\]

再定义

\[
u=\frac{F_-}{B_\kappa},
\qquad
v=\frac{F_+}{A_\kappa}.
\]

则严格有

\[
\boxed{
uv=Nc^2,
}
\]

\[
\boxed{
v-u=2ha_3,
}
\]

\[
\boxed{
b_3=cD.
}
\]

这些式子来自：

- original exact candidate；
- SGR-8 orientation；
- rational/source divisibility；
- denominator normalization；
- 正整数性。

本轮没有发现额外的“默认互素”“默认单侧分配”“默认 \(Y>0\)”等隐藏假设。事实上 SGR-9 还专门修正了过强的

\[
\gcd(u,v)\mid2h
\]

猜想，只保留其真正可证版本。

**状态：AUDITED.**

---

## 2.5 SGR-9 的 decisive contradiction

top DD 给出

\[
m_3\ge5S+11.
\]

又由

\[
\kappa,\kappa+2G< O(10^{2S})
\]

得到

\[
v_5(\kappa),
\ v_5(\kappa+2G)
\le3S+3.
\]

由

\[
c=\frac{10^{m_3}Q}{A_\kappa}
\]

推出

\[
\boxed{
v_5(c)\ge2S+8.
}
\]

于是

\[
5\mid c\mid b_3.
\]

原题逐块既约性

\[
\gcd(a_3,b_3)=1
\]

强迫

\[
v_5(a_3)=0.
\]

结合

\[
v-u=2ha_3
\]

得到 quotient difference 的精确 \(5\)-进深度。

再把 source-labelled resonance

\[
v_5(F_-)=v_5(F_+)
\]

除以已定向的 \(A_\kappa,B_\kappa\)，SGR-9 得到

\[
\boxed{
2m_3\le9S+9.
}
\]

而 top lower bound 给出

\[
\boxed{
2m_3\ge10S+22.
}
\]

矛盾。

**状态：PROVED.**

---

# 3. DD formal closure

四项审计均通过：

1. current open DD 已 exhaustive reduction 到 top chamber；
2. top chamber 全部具有 SGR-9 所需 \(5\)-adic resonance；
3. SGR-8 orientation theorem 覆盖同一区域；
4. source-labelled quotient system 没有发现未声明额外假设。

因此：

\[
\boxed{
DD=\varnothing.
}
\]

**状态：AUDITED + PROVED RELATIVE TO THE FROZEN DD REDUCTION CHAIN.**

从本轮起，下列对象全部退出 Strict-Layer frontier：

- DD near-square；
- DD post-deflation \(J\)；
- DD projected/source Hensel；
- DD source orientation；
- DD residual supply；
- DD tail window；
- DD near-\(S\)-unit；
- DD top resonance。

它们的状态统一改为：

\[
\boxed{\text{historical nodes inside a completed DD proof chain}.}
\]

---

# 4. Strict-layer chamber exhaustiveness

令

\[
s_i=n_i-m_i=\delta_i.
\]

carrier positive-weight argument 已证明：若

\[
s_3\le0,
\qquad
s_2+s_3\le0,
\]

则三个 weighted carrier terms 全都严格小于 \(\mathcal R\)，不可能得到 exact weighted average。

所以任意 candidate 必落在恰好三个 chamber 之一：

\[
A_2\text{-only}:
\quad
s_3>0,\quad s_2+s_3\le0;
\]

\[
DD:
\quad
s_3>0,\quad s_2+s_3>0;
\]

\[
A_1\text{-only}:
\quad
s_3\le0,\quad s_2+s_3>0.
\]

**状态：PROVED.**

严格层定义为

\[
\boxed{
\delta_2+\delta_3\ge1.
}
\]

因此 \(A_2\)-only 的

\[
\delta_2+\delta_3\le0
\]

与 strict condition 直接不相容。

故：

\[
\boxed{
\text{Strict candidate}
\Longrightarrow
DD\ \text{or}\ A_1\text{-only}.
}
\]

**状态：PROVED.**

结合 DD closure：

\[
\boxed{
\text{Strict candidate}
\Longrightarrow
A_1\text{-only}.
}
\]

所以现在可以正式写：

\[
\boxed{
\textbf{Strict Layer}=A_1\textbf{-only frontier}.
}
\]

这里的等号指“严格层不存在性证明的剩余 chamber”，不是说 \(A_1\) 已经被证明非空。

---

# 5. A1-only：重新从原始坐标开始

\(A_1\)-only 满足

\[
s_3\le0,
\qquad
s_2+s_3>0.
\]

定义

\[
\boxed{
g=-s_3=m_3-n_3\ge0,
}
\]

\[
\boxed{
k_{12}=s_2+s_3\ge1.
}
\]

于是

\[
s_2=g+k_{12},
\qquad
n_2=m_2+g+k_{12}.
\]

有效第三尾长为

\[
\boxed{
\ell=m_3-g=n_3.
}
\]

所以 \(A_1\) 有一个与 DD 很不同的特征：

\[
\boxed{
10^\ell=10^{n_3}
}
\]

就是第三分子的真实 decimal block scale。

---

# 6. A1 coefficient pair 的真正简化

旧统一 notation 中

\[
\widehat C
=
10^{g+k_{12}+m_2}C_1+C_2,
\qquad
\widehat D=10^g\widehat Q.
\]

但

\[
g+k_{12}+m_2=n_2.
\]

因此

\[
\boxed{
\widehat C=\widehat A_{12},
\qquad
C=A_{12},
}
\]

而

\[
\boxed{
D=10^gQ_{12}.
}
\]

**状态：PROVED / AUDITED.**

所以 A1 的 coefficient pair 不是两个神秘的 unified variables；它们就是：

- 原始前两分子的真实 prefix word \(A_{12}\)；
- 原始前两分母 word \(Q_{12}\) 乘一个 decimal shift \(10^g\)。

这已经提示：A1 不应该继续以 DD-style near-square factor language 为主坐标。

---

# 7. Denominator–decimal trace 冻结后的 A1 data

取

\[
\boxed{
T=(b_1,b_2,b_3,S),
\qquad
S=10^{n_3}.
}
\]

这是已有 backward work 中的 sufficient proper denominator–decimal trace。

由 \(T\) 唯一恢复：

\[
m_i,\quad
M_i=10^{m_i},\quad
Q=b_1M_2+b_2,\quad
G=b_1b_2,
\]

以及

\[
n_3=\log_{10}S,
\qquad
g=m_3-n_3.
\]

所以：

\[
\boxed{
g\text{ 不是 fixed-}T\text{ fibre 中的自由变量。}
}
\]

定义

\[
\eta_3=\gcd(S,b_3),
\qquad
L=\frac S{\eta_3},
\qquad
\tau=\frac{b_3}{\eta_3}.
\]

再由已有 tail weight：

\[
\boxed{
\kappa
=
\frac{M_3QG}{b_3}
=
\frac{10^gLQG}{\tau}.
}
\]

以及

\[
\boxed{
D=\frac{M_3}{S}Q=10^gQ.
}
\]

故

\[
L,\tau,\eta_3,\kappa,D,g
\]

全部由 \(T\) 恢复。

**状态：PROVED / DERIVED.**

尾证书

\[
\boxed{
S\mid\kappa^2(\kappa+2G)
}
\]

仍是强有力的 T-only admissibility filter，但不再是独立 terminal theorem。

---

# 8. Gap/tail quadratics 的重新审计

固定 \(T\)，令

\[
\theta=\frac{\mu}{\nu},
\qquad
\zeta=z_3.
\]

后续 backward exact-recovery 审计已经证明：

\[
D=D_T,
\]

\[
N
=
\theta^2+\frac{2G}{\tau}\theta\zeta,
\]

\[
C
=
\frac{
G\kappa\zeta+(G+\kappa)\tau\theta
}{
G^2L
}.
\]

并有 exact oriented coefficient-plane identity

\[
\boxed{
G^2LC
-G\kappa\zeta
-(G+\kappa)\tau\theta
=0.
}
\]

在这些 exact reconstruction identities 下：

\[
\boxed{
Q_{\rm gap}\equiv0,
}
\]

\[
\boxed{
Q_{\rm tail}\equiv0.
}
\]

也就是说：

\[
\boxed{
\text{gap quadratic 与 primitive-tail quadratic}
}
\]

在 fixed exact recovery fibre 中都只是 elimination shadows。

**状态：PROVED / REDUNDANT AS INDEPENDENT FRONTIER GATES.**

同理：

- discriminant-square 是 rational-root existence 的 certificate；
- resultant 是旧 quadratic information 的消元投影；
- 它们都不应继续被列为与 exact recovery 并列的 terminal obligation。

**状态：REDUNDANT AS INDEPENDENT FRONTIER GATES.**

这不等于这些恒等式“无用”；它们仍可作为搜索、筛选或局部算术工具。

---

# 9. A1-specific one-word collapse

定义完整 denominator word

\[
\boxed{
\mathbf B
=
b_1M_2M_3+b_2M_3+b_3
=
M_3Q+b_3.
}
\]

fixed \(T\) 后 \(\mathbf B\) 已冻结。

对 actual tail root，

\[
a_3=\eta_3\zeta.
\]

定义

\[
\boxed{
\mathbf A:=SC+a_3.
}
\]

在 \(A_1\) 中

\[
S=10^{n_3},
\qquad
C=A_{12},
\]

所以

\[
\boxed{
\mathbf A
=
A_{12}10^{n_3}+a_3
=
\operatorname{concat}(a_1,a_2,a_3).
}
\]

而 exact coefficient plane 变成最原始的

\[
\boxed{
\mathcal R=\frac{\mathbf A}{\mathbf B}.
}
\]

后续 root-pair fibre theorem 更进一步证明：

\[
\boxed{
(T,\theta,\zeta)
\simeq
(T,\mathbf A)
\qquad
(A_1\text{-only}).
}
\]

原因是 \(T\) 已固定 \(n_3\)，所以从 \(\mathbf A\) 可恢复：

\[
a_3=\mathbf A\bmod S,
\]

\[
A_{12}=\left\lfloor\frac{\mathbf A}{S}\right\rfloor,
\]

继而恢复 \(\mathcal R,N,\theta,\zeta\)。

**状态：PROVED.**

这是本轮 A1 frontier 重建中最重要的压缩：

\[
\boxed{
\text{旧 root pair 也不是 A1 最小 residual language；}
}
\]

\[
\boxed{
\text{fixed }T\text{ 后，一个 full numerator word }\mathbf A
\text{ 已携带全部 residual algebraic semantics。}
}
\]

---

# 10. Fixed \((T,\mathbf A)\) 后真正还剩什么？

令

\[
\boxed{
P
=
\left\lfloor\frac{\mathbf A}{S}\right\rfloor
=A_{12}.
}
\]

第三块已经确定：

\[
\boxed{
a_3=\mathbf A\bmod S.
}
\]

剩下的唯一 recovery choice 是：在哪里把固定 decimal word \(P\) 切成

\[
P=a_1 10^{n_2}+a_2.
\]

对一个候选 cut \(n\)，定义

\[
q_n=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
r_n=P\bmod10^n.
\]

于是

\[
a_1=q_n,\qquad a_2=r_n.
\]

定义 weighted prefix norm

\[
\boxed{
F_n=b_2^2q_n^2+b_1^2r_n^2.
}
\]

从 \((T,\mathbf A)\) 直接定义

\[
\boxed{
\mathscr N(T,\mathbf A)
:=
G^2
\left[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
-
\left(\frac{a_3}{b_3}\right)^2
\right].
}
\]

那么一个 legal cut 必须满足

\[
\boxed{
F_n=\mathscr N(T,\mathbf A).
}
\tag{A1-WR}
\]

这就是 A1 最自然的 **word-recovery equation**。

此外必须满足：

\[
\gcd(q_n,b_1)=1,
\]

\[
\gcd(r_n,b_2)=1,
\]

\[
\gcd(a_3,b_3)=1,
\]

真实 digit windows，以及

\[
\boxed{
k_{12}
=
n-m_2-g
\ge1.
}
\]

注意：

\[
g=m_3-n_3
\]

已由 \(T\) 决定，因此给定 cut \(n\) 后

\[
k_{12}=n-m_2-g
\]

也被恢复。

所以：

\[
\boxed{
g,\ k_{12}
\text{ 都不是 fixed }(T,\mathbf A,n)\text{ 的独立自由变量。}
}
\]

---

# 11. A1 Word-Recovery Equivalence

### Theorem — A1 exact word normal form

给定正整数数据 \((T,\mathbf A,n)\)，其中

\[
T=(b_1,b_2,b_3,S),
\qquad
S=10^{n_3},
\]

按上一节恢复

\[
a_3,\ P,\ a_1,\ a_2.
\]

若：

1. 所有 block 均为合法正十进制块；
2. \(g=m_3-n_3\ge0\)；
3. \(k_{12}=n-m_2-g\ge1\)；
4. \(\gcd(a_i,b_i)=1\)；
5. (A1-WR) 成立；

则

\[
\frac{\mathbf A}{\mathbf B}
=
\sqrt{
\left(\frac{a_1}{b_1}\right)^2+
\left(\frac{a_2}{b_2}\right)^2+
\left(\frac{a_3}{b_3}\right)^2
}.
\]

反之，任意 original \(A_1\)-only candidate 都唯一产生这种 \((T,\mathbf A,n)\)。

**状态：DERIVED.**

### 证明

由

\[
F_n
=
b_2^2a_1^2+b_1^2a_2^2
\]

及

\[
G=b_1b_2
\]

有

\[
\frac{F_n}{G^2}
=
\left(\frac{a_1}{b_1}\right)^2
+
\left(\frac{a_2}{b_2}\right)^2.
\]

(A1-WR) 正好给出

\[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
=
\frac{F_n}{G^2}
+
\left(\frac{a_3}{b_3}\right)^2.
\]

所有量为正，故取正平方根即可。

反向由 original candidate 的定义直接得到。

---

# 12. Prefix-cut fibre 已经是 uniformly finite

后续 exact root-pair fibre theorem 已证明 decimal split strict convexity：

沿 legal cut set，

\[
F_n
\]

是严格离散凸的。

因此任意水平线

\[
F_n=N
\]

至多命中两次。

结合 \(A_1\) 的 one-word collapse：

\[
\boxed{
\text{fixed }(T,\mathbf A)
\Longrightarrow
\text{至多两个完整 A1 prefix realizations}.
}
\]

**状态：PROVED.**

若确有两个 cut，multiplicity 的来源不是：

- Vieta conjugation；
- Gaussian conjugation；
- Hensel branch；
- denominator normalization；

而只是：

\[
\boxed{
\text{同一个 prefix decimal word 有两个内部 cut，且 weighted norm 相同。}
}
\]

所以 fixed \((T,\mathbf A)\) 后的 genuine residual freedom 至多是一位：

\[
\boxed{
\omega_{12}\in\{0,1\}.
}
\]

它是有限 choice，不是新的无界参数。

---

# 13. SGR-3 的 A1 负结果重新解释

SGR-3 的 normalized error 为

\[
\rho
=
\frac{E}{\varepsilon M^2}.
\]

在 \(A_1\) 中：

\[
C=A_{12},
\qquad
D=10^gQ,
\]

所以

\[
\rho_{A_1}
=
10^{2g}
\frac{Q^2N}{G^2A_{12}^2}
\left(
1+\frac{2b_3}{10^{m_3}Q}
\right).
\]

但

\[
n_2=m_2+g+k_{12},
\]

所以 \(A_{12}\) 自身也随 \(g\) 带入相同级别的 decimal growth。

因此：

\[
\boxed{
g\to\infty
\not\Longrightarrow
\rho\to0
}
\]

是一个真正的结构性负结果。

**状态：PROVED / AUDITED.**

更精确地，已有统一下界：

\[
\boxed{
\rho>\frac1{400}10^{-2k_{12}}.
}
\]

所以 near-square precision 真正读取的是 \(k_{12}\)，而不是裸 \(g\)。

---

## 13.1 \(k_{12}\) 是否仍无界？

当前没有 A1 theorem 给出全局 uniform upper bound

\[
k_{12}\le K_0.
\]

所以：

\[
\boxed{
k_{12}\text{ 的全局有界性仍 OPEN。}
}
\]

但 fixed primitive core finite fibre 立即说明：

\[
\boxed{
\text{固定 primitive core 时 }k_{12}\text{ 不可能沿 exact candidates 无界。}
}
\]

任何 \(k_{12}\to\infty\) 的 exact sequence 都必须同时使 primitive-core height

\[
Q_0\to\infty.
\]

所以 \(k_{12}\) 不是一个与 moving core 独立的 infinity direction。

---

## 13.2 \(k_{12}\) 与 primitive-core height 是否独立？

不能证明一个 deterministic formula

\[
k_{12}=f(Q_0).
\]

所以二者不是“函数依赖”意义上的已证关系。

但在无界性层面：

\[
\boxed{
k_{12}\to\infty
\Longrightarrow
Q_0\to\infty
}
\]

对 exact candidate sequence 成立。

**状态：DERIVED FROM FIXED-CORE FINITE FIBRE.**

因此：

- \(k_{12}\) 是重要 precision statistic；
- 它不是第二个 top-level independent infinity source。

---

## 13.3 square-spacing 的新地位

uniform square-spacing theorem 仍然严格有效：

\[
0<E<\varepsilon(2M-1)
\Longrightarrow
\text{state 不可提升}.
\]

但 A1 中没有 theorem 能把所有 moving-core states 自动送入该 death region。

所以：

\[
\boxed{
\text{A1 square-spacing = valid auxiliary death test, not terminal frontier.}
}
\]

**状态：PROVED TOOL / REDUNDANT AS FRONTIER LABEL.**

---

# 14. A1 的真正独立 recovery conditions

在新的 \((T,\mathbf A,n)\) normal form 中：

## 14.1 Positivity / digit blocks

必须有：

\[
a_1,a_2,a_3>0,
\]

且每个 cut 与第三块均满足真实 decimal digit window。

**状态：ACTIVE.**

---

## 14.2 A1 carrier cell

\[
g=m_3-n_3\ge0,
\]

\[
k_{12}=n_2-m_2-g\ge1.
\]

二者在 \(T\) 与 cut 固定后都是 derived integers。

**状态：ACTIVE, BUT NOT FREE COORDINATES.**

---

## 14.3 Individual reducedness

\[
\boxed{
\gcd(a_i,b_i)=1
\quad(i=1,2,3).
}
\]

这没有被 quadratic identity 吸收。

DD closure 已经展示过 reducedness 可能是 decisive source information；A1 中也必须保留。

**状态：ACTIVE / INDEPENDENT RECOVERY CONDITION.**

---

## 14.4 Exact word/norm consistency

唯一核心 equation 是 (A1-WR)：

\[
\boxed{
b_2^2a_1^2+b_1^2a_2^2
=
G^2
\left[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
-
\left(\frac{a_3}{b_3}\right)^2
\right].
}
\]

它直接表达：

\[
\boxed{
\text{同一个完整 decimal word}
\text{ 必须同时是同一个 rational sphere witness}.
}
\]

**状态：ACTIVE / TERMINAL.**

---

## 14.5 Tail divisibility / valuation constraints

\[
S\mid\kappa^2(\kappa+2G)
\]

以及其 \(2\)-、\(5\)-adic projections仍是有效必要条件。

但：

- \(2\)-adic capacity；
- \(5\)-adic capacity；

只是同一个 decimal tail divisibility 的两个投影。

并且一旦使用完整 exact word-recovery theorem，这些条件是 exact candidate 的后果。

因此：

\[
\boxed{
\text{tail divisibility = strong admissibility filter, not separate terminal theorem.}
}
\]

**状态：PROVED / AUXILIARY.**

---

# 15. A1 source-labelled factorization audit

本轮没有审计到一个自然的 \(A_1\) analogue，可以严格替代成 DD 的

\[
F_-=B_\kappa u,
\qquad
F_+=A_\kappa v,
\]

并同时拥有：

- canonical orientation；
- quotient product；
- quotient difference；
- original reducedness 的 source-level interpretation。

特别地，SGR-8 的 orientation proof 使用 top-DD 特有的 decimal magnitude，并证明共轭第三分子为负；这不能迁移到 \(A_1\)。

因此：

\[
\boxed{
\text{DD source orientation / }uv=Nc^2\text{ machinery}
\text{ 不得迁移到 A1。}
}
\]

**状态：INVALID AS AN UNPROVED TRANSFER.**

这不证明 A1 永远不存在任何有用 factorization；只说明当前 proof library 中没有一个已证的 DD-style canonical source factor system 值得进入 A1 terminal normal form。

---

# 16. A1 真正有几个无界自由参数？

这里必须区分两种含义。

## 16.1 Algebraic-coordinate count

不能声称整个 A1 family 被一个整数 \(Q_0\) 参数化。

当 primitive core 移动时，

\[
P_i,\quad g_i,\quad U,V,\quad
T,\quad\mathbf A,\ldots
\]

都可能协同变化。

所以：

\[
\boxed{
\text{“A1 只有一个代数自由变量”并未证明。}
}
\]

**状态：INVALID if interpreted literally.**

---

## 16.2 Top-level infinity-source count

SGR-1 已证：

\[
\boxed{
\text{fixed primitive core}
\Longrightarrow
\text{finite decimal fibre}.
}
\]

因此任何无限 A1 candidate sequence 必有

\[
\boxed{
Q_0\to\infty.
}
\]

反过来，对每个固定 \(Q_0=H\)，primitive integer sphere core 只有有限多个；每个 core 又只有有限 lift fibre。

所以：

\[
\boxed{
\text{每个 fixed height shell }Q_0=H\text{ 的 A1 candidate set 有限。}
}
\]

**状态：DERIVED.**

因此在“无界逃逸源”的严格意义下：

\[
\boxed{
\textbf{A1 只有一个 top-level infinity direction：moving primitive-core height }H=Q_0.
}
\]

但这句话只表示：

\[
\text{无限序列}\Longrightarrow Q_0\to\infty,
\]

不表示所有其他坐标都是 \(Q_0\) 的函数。

---

# 17. 旧 A1 “无穷尾” 的重新解释

旧 synthesis 把 saturated \(L=1\) 中的

\[
g\to\infty
\]

视为最危险的独立 escape。

现在应修正为：

1. fixed trace \(T\) 后，\(g\) 已被 \(m_3,n_3\) 唯一决定；
2. fixed primitive core 后，整个 decimal fibre 有限；
3. 因而任何 \(g\to\infty\) exact sequence 必有
   \[
   Q_0\to\infty.
   \]

所以：

\[
\boxed{
g\text{ 是 moving-core sequence 的 projection，不是第二个独立 infinity axis。}
}
\]

同理，对 \(k_{12}\)、\(m_3\)、\(n_2\)、denominator depth 等表面无界量，都应先问它们是否能在固定 core 上独立逃逸。SGR-1 已经统一回答：不能。

---

# 18. SGR-1 / 2 / 3 / 4–9 对 A1 的最终地位

## SGR-1

\[
\boxed{
\text{fixed primitive core}\Rightarrow\text{finite decimal fibre}.
}
\]

完整适用于 A1。

**状态：PROVED / ACTIVE GLOBAL STRUCTURE.**

---

## SGR-2

变量桥接

\[
q=V,
\qquad
y_i=UP_i,
\qquad
H=UQ_0
\]

完整适用。

SGR depth gate仍可作为 finite-fibre machinery 的一部分。

**状态：PROVED / ACTIVE GLOBAL STRUCTURE.**

---

## SGR-3

统一 square gate

\[
\varepsilon M^2-E=\varepsilon Y^2
\]

适用于 A1。

但：

\[
g\to\infty\not\Rightarrow\rho\to0.
\]

所以它保留为 auxiliary death test，不再作为主 frontier。

**状态：PROVED / AUXILIARY.**

---

## SGR-4–9

当前这些轮次的实质结论依赖 DD：

- DD error/post-deflation；
- DD residual supply；
- DD phase synchronization；
- DD source-information audit；
- DD orientation；
- DD quotient valuation overload。

尤其不得迁移：

\[
\text{top wedge},
\]

\[
\text{double resonance},
\]

\[
\omega_{\rm src}=+1,
\]

\[
uv=Nc^2,
\]

\[
v-u=2ha_3,
\]

\[
2m_3\le9S+9.
\]

**状态：DD-ONLY / INVALID TO TRANSFER WITHOUT NEW PROOF.**

---

# 19. Redundant / auxiliary / active ledger

| Object / gate | A1 status after audit |
|---|---|
| gap quadratic | **REDUNDANT as independent gate** |
| primitive-tail quadratic | **REDUNDANT as independent gate** |
| discriminant square | **AUXILIARY certificate** |
| resultant coupling | **REDUNDANT elimination shadow** |
| \(2\)-adic tail capacity | **AUXILIARY projection** |
| \(5\)-adic tail capacity | **AUXILIARY projection** |
| \(S\mid\kappa^2(\kappa+2G)\) | **ACTIVE filter, not frontier** |
| Gaussian flip | **INVALID as descent in saturated A1** |
| square-spacing | **AUXILIARY death test** |
| \(g\) | **DERIVED from \(T\), not independent** |
| \(k_{12}\) | **DERIVED from \(T+\)cut; precision statistic** |
| root pair \((\theta,\zeta)\) | **REDUNDANT as A1 coordinate after one-word collapse** |
| full numerator word \(\mathbf A\) | **ACTIVE residual semantic coordinate** |
| prefix cut \(n_2\) | **ACTIVE finite choice, fibre size \(\le2\)** |
| digit windows | **ACTIVE recovery condition** |
| individual gcd | **ACTIVE recovery condition** |
| exact word/norm equation (A1-WR) | **ONE TERMINAL GATE** |
| DD source orientation | **INVALID transfer** |

---

# 20. Minimal strict-layer dependency graph

从本轮起，Strict-Layer 主图应写成：

\[
\boxed{
\text{Original strict candidate}
}
\]

\[
\Downarrow
\]

\[
\boxed{
DD\ \text{or}\ A_1\text{-only}
}
\]

\[
\Downarrow
\]

\[
\boxed{
DD=\varnothing
}
\]

\[
\Downarrow
\]

\[
\boxed{
A_1\text{-only}
}
\]

\[
\Downarrow
\]

\[
\boxed{
T=(b_1,b_2,b_3,10^{n_3})
+
\mathbf A
+
\text{legal prefix cut }n_2
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{A1-WR}
+
\text{digit cell}
+
\gcd(a_i,b_i)=1
}
\]

\[
\Downarrow
\]

\[
\boxed{
\textbf{ONE OPEN TERMINAL THEOREM}.
}
\]

DD Hensel、DD orientation、near-square、resultant、A1 quadratic 等不再出现在主 dependency graph。

---

# 21. Strict-layer status table

| Structure | Strict-layer status |
|---|---|
| global primitive-core reduction | **PROVED** |
| primitive / Exact-Lift bridge | **PROVED** |
| fixed-core finite fibre | **PROVED** |
| carrier chamber exhaustiveness | **PROVED** |
| \(A_2\)-only | **moved to critical layer** |
| DD | **CLOSED** |
| DD Hensel / phase | **historical, closed** |
| DD orientation | **historical, solved** |
| DD post-deflation / residual supply | **historical, closed** |
| DD tail window | **historical, closed** |
| \(A_1\)-only | **OPEN** |
| A1 \(g\)-shift | **projected statistic, not independent infinity source** |
| A1 \(k_{12}\) | **active precision statistic; global bound OPEN** |
| A1 square-spacing | **auxiliary** |
| A1 gap/tail quadratic | **REDUNDANT as independent gates** |
| A1 discriminant/resultant | **auxiliary / redundant as frontier** |
| A1 tail divisibility | **active admissibility filter** |
| A1 exact recovery | **ACTIVE** |
| A1 one-word collapse \(T+\mathbf A\) | **PROVED** |
| fixed \(T,\mathbf A\) prefix fibre \(\le2\) | **PROVED** |
| A1 DD-style source factorization | **not established; transfer invalid** |

---

# 22. The one open terminal theorem

## A1 Moving-Core Word-Realization Theorem

定义一个 **A1 admissible trace**

\[
T=(b_1,b_2,b_3,S),
\qquad
S=10^{n_3},
\]

并令

\[
\mathbf B
=
b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3.
\]

对任意正整数 full numerator word \(\mathbf A\)，定义

\[
a_3=\mathbf A\bmod S,
\qquad
P=\left\lfloor\frac{\mathbf A}{S}\right\rfloor.
\]

对任意 legal cut \(n\)，令

\[
a_1=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
a_2=P\bmod10^n.
\]

再定义

\[
g=m_3-n_3,
\qquad
k_{12}=n-m_2-g.
\]

### Terminal theorem

不存在 \(T,\mathbf A,n\) 同时满足：

1. \(g\ge0,\ k_{12}\ge1\)；
2. 三个 numerator blocks 均有正确 digit lengths；
3. \(\gcd(a_i,b_i)=1\)；
4. 必要的 A1 denominator/tail admissibility；
5. exact word-recovery equation
   \[
   \boxed{
   b_2^2a_1^2+b_1^2a_2^2
   =
   G^2
   \left[
   \left(\frac{\mathbf A}{\mathbf B}\right)^2
   -
   \left(\frac{a_3}{b_3}\right)^2
   \right].
   }
   \]

**状态：OPEN.**

这一定理与

\[
A_1\text{-only}=\varnothing
\]

等价，但它已经删除了：

- independent quadratic-root search；
- discriminant gate；
- resultant gate；
- root-pair branch；
- independent \(g\)；
- independent \(k_{12}\)；
- unbounded cut multiplicity。

而且 fixed \((T,\mathbf A)\) 时只需检查至多两个 cut。

因此它是当前最短、最接近 original recovery semantics 的 A1 terminal theorem。

---

# 23. Moving-core grading of the terminal theorem

对任何通过 A1-WR 的 candidate，都可 canonical recover primitive core

\[
(P_1,P_2,P_3,Q_0).
\]

定义 height

\[
\boxed{H:=Q_0.}
\]

SGR-1 给出：

\[
\boxed{
H\text{ fixed}
\Longrightarrow
\text{只有有限多个 A1 terminal states}.
}
\]

所以 terminal theorem 可以按有限 shell 分级：

\[
\mathfrak X_H
=
\{
(T,\mathbf A,n):
\text{满足 A1 terminal system，recovered }Q_0=H
\}.
\]

每个

\[
\mathfrak X_H
\]

都是有限集。

唯一 remaining infinity problem 是：

\[
\boxed{
H\to\infty
}
\]

时这些 finite shells 是否可能一直非空。

因此下一轮如果强攻，不应再开五条“square / gcd / Hensel / recovery / valuation”并行 frontier；应只攻击：

\[
\boxed{
\mathfrak X_H=\varnothing
\quad\text{for all }H.
}
\]

具体选择什么工具，是下一轮的问题。

---

# 24. Five required answers

## Q1 — DD 是否可以正式标记 CLOSED？

\[
\boxed{\textbf{YES}.}
\]

四项 dependency audit 通过，未发现 SGR-9 coverage gap。

**状态：AUDITED / PROVED.**

---

## Q2 — 严格层是否因此只剩 \(A_1\)-only？

\[
\boxed{\textbf{YES}.}
\]

carrier exhaustiveness 给出三 chamber，而 strict condition 直接排除 \(A_2\)-only；SGR-9 再删除 DD。

\[
\boxed{
\text{Strict candidate}\Longrightarrow A_1\text{-only}.
}
\]

**状态：PROVED.**

---

## Q3 — A1-only 当前真正有几个无界自由参数？

严格答案分两层：

\[
\boxed{
\text{一个 top-level infinity direction：}H=Q_0\to\infty.
}
\]

但：

\[
\boxed{
\text{没有证明整个 A1 被一个标量 }H\text{ 单参数化。}
}
\]

\(g,k_{12},T,\mathbf A\) 可以随 moving core 协同增长；只是 fixed core fibre 有限，所以它们不能形成独立的 infinity axis。

fixed \((T,\mathbf A)\) 后更只剩至多一个二元 cut bit。

---

## Q4 — 哪些旧 A1 gates 不再应列入 frontier？

应删除为独立 frontier 的有：

\[
\boxed{
\text{gap quadratic},
\quad
\text{primitive-tail quadratic},
\quad
\text{discriminant square},
\quad
\text{resultant},
\quad
\text{square-spacing}.
}
\]

其中：

- 前两个是 exact reconstruction elimination shadows；
- discriminant/resultant 是 certificate / projection；
- square-spacing 是有效 auxiliary death test，但不能 uniform close A1；
- \(2/5\)-adic capacity 是同一个 tail divisibility 的投影。

真正必须保留的是：

\[
\boxed{
\text{exact word realization}
+
\text{digit/cut consistency}
+
\text{individual reducedness}.
}
\]

---

## Q5 — 下一轮唯一 terminal target？

\[
\boxed{
\textbf{A1 Moving-Core Word-Realization Theorem}.
}
\]

即证明不存在任何 admissible

\[
(T,\mathbf A,n_2)
\]

通过 A1-WR + digit cell + individual gcd。

---

# 25. Final verdict

本轮不是新的 A1 强攻，但 consolidation 产生了真正的结构缩短：

\[
\boxed{
DD
\text{ 从 Strict-Layer 研究前线彻底删除。}
}
\]

并且：

\[
\boxed{
A_1\text{ 不再是“若干 quadratic / valuation / spacing gates 的集合”。}
}
\]

当前最短描述是：

\[
\boxed{
\text{denominator trace }T
+
\text{one numerator word }\mathbf A
+
\text{at most one cut bit}
}
\]

通过一个 exact word/norm recovery gate。

因此最终等级：

\[
\boxed{
\textbf{SGR-10B — CONSOLIDATION + A1 REDUCTION}.
}
\]

Strict-Layer 下一步不需要再讨论 DD，也不需要先重新发明 A1 quadratic machinery。

真正应该强攻的只有一个命题：

\[
\boxed{
\text{A1 exact word realization is empty.}
}
\]
