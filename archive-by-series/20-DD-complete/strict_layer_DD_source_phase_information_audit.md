# 三项十进制拼接平方和问题：DD Source-Phase Information Audit

**文件名：** `strict_layer_DD_source_phase_information_audit.md`  
**研究范围：** Strict Layer，仅审计 DD chamber 的旧 source-level deep Hensel / phase 数据在
\[
(\mu,\nu,\text{source data})
\longrightarrow
F_-,F_+
\longrightarrow
M\pm Y
\longrightarrow
J^\sharp,K^\sharp
\]
过程中是否丢失真正独立的信息。  
**冻结：** 不继续 post-deflation CRT；不研究 divisor supply；不做新的 DD 总体攻击。  
**本轮等级：**
\[
\boxed{\textbf{SGR-7E — REPRESENTATION OBSTRUCTION}}
\]

---

# 0. Executive summary

本轮得到的最强可靠结论不是“找到了新的 source Hensel digit”，而是：

\[
\boxed{
\text{一旦恢复 }F_-\text{ 与 }F_+\text{ 的 source orientation，}
\text{旧 Hensel phase 的全部 higher digits 都由 }
(J^\sharp,K^\sharp)
\text{ 与既知 source coefficients 精确恢复。}
}
\]

更具体地，DD 的 source factors 为

\[
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
\qquad
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0},
\]

而旧/new exact bridge 已证

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda D_0J^\sharp,\,
\Lambda D_0K^\sharp
\}.
}
\]

这里右端在现有报告中只以 **unordered pair** 出现。

另一方面 primitive recovery identity

\[
10^{m_3}Q_{12}G_0=2\kappa\mu\nu
\]

立即给出两个精确反演公式：

\[
\boxed{
\frac{\mu}{\nu}
=
\frac{\kappa F_-}
{10^{m_3}Q_{12}(\kappa+2G)}
}
\tag{0.1}
\]

以及

\[
\boxed{
\frac{\mu}{\nu}
=
\frac{10^{m_3}Q_{12}\mathcal N_{12}}
{F_+}.
}
\tag{0.2}
\]

因此，只要知道 post-deflation 两个因子中**哪一个是 source-labelled \(F_-\)**，
就能恢复完整有理数 \(\mu/\nu\)，从而恢复它在 \(p=2,5\) 的所有 valuation-normalized
unit digits，不只是到旧 Hensel 深度 \(R_p\)。

所以：

\[
\boxed{
\text{不存在“第一位尚未恢复的 higher Hensel digit”。}
}
\]

所有可能的信息损失都压缩成一个更低层的、非 \(p\)-adic-digit 型对象：

\[
\boxed{
\omega_{\rm src}\in\{\pm1\},
}
\]

其中可取定义

\[
\boxed{
\omega_{\rm src}=+1
\iff
F_-=\Lambda D_0J^\sharp,
}
\tag{0.3}
\]

\[
\boxed{
\omega_{\rm src}=-1
\iff
F_-=\Lambda D_0K^\sharp.
}
\tag{0.4}
\]

等价地，

\[
\boxed{
\omega_{\rm src}
=
\operatorname{sgn}
\left(
\kappa\mathcal N_{12}\nu^2
-
(\kappa+2G)\mu^2
\right),
}
\tag{0.5}
\]

因为 \(2/G_0>0\)。

本轮还能严格证明：交换这个 orientation 恰好把 gap root
\[
t:=\mu/\nu
\]
送到它的 Vieta 共轭根

\[
\boxed{
t^\vee
=
\frac{\kappa\mathcal N_{12}}
{(\kappa+2G)t}.
}
\tag{0.6}
\]

因此旧 \(5\)-进关系

\[
\mu_5\equiv\pm\rho_5\nu_5\pmod{5^{R_5}}
\]

中的两个符号，至少在当前可审计接口下，正好对应这两个全局 algebraic orientations；
它们不是额外的 higher-digit freedom。

但目前还不能把 (0.3)–(0.4) 的 source orientation bit 正式 quotient 掉。
原因有两个：

1. 当前 File Library 没有暴露旧 DD deep-Hensel 原始文件中
   \[
   \rho_2,\rho_5,R_2,R_5
   \]
   的完整 source-level 定义与 branch convention；
2. 现有 exact bridge 只证明 unordered factor identity，尚未证明
   “交换 \(F_-,F_+\)”必然对应**同一个 prefix/tail source state 下**
   另一个同样 globally recoverable decimal candidate。

换言之，当前严格状态是：

\[
\boxed{
\text{old phase}
=
\text{endogenous factor cancellation}
\oplus
\text{at most one source-orientation bit}.
}
\tag{0.7}
\]

没有证据支持任何额外 surviving higher digit。

因此本轮不是 SGR-7A/7B；
也不能安全升级到 SGR-7D。
真正障碍已经从 “Hensel 深度不清楚” 降成：

\[
\boxed{
\text{source-labelled orientation 是否只是表示选择，}
\text{还是完整 decimal recovery 真正选择其中一支？}
}
\]

---

# 1. Source audit 与证据边界

## 1.1 本轮重点复核的文件

重点使用：

- `strict_layer_DD_supply_phase_synchronization_campaign.md`
- `strict_layer_DD_post_deflation_campaign.md`
- `strict_layer_DD_error_closure_campaign.md`
- `exact_lift_research_synthesis_2026-08-10.md`

并为精确 gap-root 与 primitive-profile 接口回查：

- `strict_layer_unified_exact_lift_campaign(1).md`
- `strict_layer_backward_global_witness_gluing_campaign.md`
- `strict_layer_backward_canonical_dependency_skeleton.md`

---

## 1.2 原始 DD deep-Hensel 文件的可见性问题

当前可检索 File Library 没有暴露一个独立命名、比 synthesis / SGR-6 更原始的
DD deep-Hensel 专门文件。

现有已审计接口明确记录：

\[
\boxed{
\mu_5
\equiv
\pm\rho_5\nu_5
\pmod{5^{R_5}},
}
\tag{1.1}
\]

并记录旧证明给出很深的 \(R_5\)，例如

\[
R_5>1.415S_{12}+9.
\]

但当前材料没有完整暴露：

- \(\rho_5\) 的最初定义式；
- \(\rho_2\) 的最初定义式；
- \(2\)-adic branch 在旧证明中究竟如何编号；
- branch sign 是否曾由某个 prefix/tail orientation convention 固定。

因此本报告不虚构这些缺失定义。

这正是最后不能把结果升级为 SGR-7D 的唯一表示层障碍之一。

---

# 2. 完整 source \(\to\) factor \(\to\) post-deflation 映射

## 2.1 DD source coefficients

统一记

\[
Q_{12}
=
b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\]

\[
\mathcal N_{12}
=
(a_1b_2)^2+(a_2b_1)^2,
\]

\[
A_{12}
=
a_1 10^{n_2}+a_2.
\]

DD 中

\[
C=10^{d_3}A_{12},
\qquad
D=Q_{12}.
\]

尾权为

\[
\boxed{
\kappa
=
\frac{10^{m_3}Q_{12}G}{b_3}
\in\mathbf Z_{>0}.
}
\tag{2.1}
\]

---

## 2.2 Gap root

Exact-Lift 的 DD gap quadratic 为

\[
\boxed{
Q_{12}(\kappa+2G)\mu^2
-
2G\kappa C\,\mu\nu
+
\kappa Q_{12}\mathcal N_{12}\nu^2
=0,
}
\tag{2.2}
\]

其中

\[
\gcd(\mu,\nu)=1.
\]

令

\[
t:=\frac{\mu}{\nu}>0.
\]

则

\[
\boxed{
Q_{12}(\kappa+2G)t^2
-
2G\kappa C\,t
+
\kappa Q_{12}\mathcal N_{12}=0.
}
\tag{2.3}
\]

一个完整 candidate 一旦固定，实际 \(t\) 是 candidate 的 deterministic projection；
二次式的两个 theoretical roots 只是 projected search branching。

---

## 2.3 Primitive recovery identity

旧 DD factorization 同时使用

\[
\boxed{
10^{m_3}Q_{12}G_0
=
2\kappa\mu\nu.
}
\tag{2.4}
\]

这里 \(G_0\) 是旧 factor construction 中的 source gcd normalization。

---

## 2.4 Source-labelled factors

定义

\[
\boxed{
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
}
\tag{2.5}
\]

\[
\boxed{
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0}.
}
\tag{2.6}
\]

它们满足

\[
F_-+F_+
=
2GA_{12}10^{n_3},
\]

以及

\[
F_-F_+
=
\mathcal N_{12}10^{m_3}Q_{12}
\left(
10^{m_3}Q_{12}+2b_3
\right).
\]

于是若

\[
X_{\rm old}=GA_{12}10^{n_3},
\]

\[
Y_{\rm old}^2
=
X_{\rm old}^2-F_-F_+,
\]

则

\[
\boxed{
\{F_-,F_+\}
=
\{X_{\rm old}-Y_{\rm old},\,
X_{\rm old}+Y_{\rm old}\}.
}
\tag{2.7}
\]

---

## 2.5 Exact lattice scaling

定义

\[
\boxed{
\Lambda
=
UR^2\,10^{\lceil m_3/2\rceil}.
}
\tag{2.8}
\]

旧/new bridge 已证

\[
X_{\rm old}=\Lambda M,
\qquad
Y_{\rm old}=\Lambda Y.
\]

因此

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda(M-Y),\,
\Lambda(M+Y)
\}.
}
\tag{2.9}
\]

顶部 double resonance 对 \(p=2,5\) 给出

\[
v_p(M-Y)=v_p(M+Y)=:j_p.
\]

定义

\[
\boxed{
D_0=2^{j_2}5^{j_5},
}
\tag{2.10}
\]

\[
\boxed{
J^\sharp=\frac{M-Y}{D_0},
\qquad
K^\sharp=\frac{M+Y}{D_0}.
}
\tag{2.11}
\]

则

\[
\gcd(J^\sharp K^\sharp,10)=1,
\]

并且

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda D_0J^\sharp,\,
\Lambda D_0K^\sharp
\}.
}
\tag{2.12}
\]

这是本轮信息审计的核心投影。

注意：**(2.12) 在现有证明中是 unordered identity。**

---

# 3. 一个关键的新精确反演：oriented factor 可恢复整个 gap root

把 (2.4) 代入 (2.5)：

\[
\begin{aligned}
F_-
&=
2(\kappa+2G)\mu^2
\frac{10^{m_3}Q_{12}}{2\kappa\mu\nu}\\
&=
10^{m_3}Q_{12}
\frac{\kappa+2G}{\kappa}
\frac{\mu}{\nu}.
\end{aligned}
\]

因此

\[
\boxed{
t=\frac{\mu}{\nu}
=
\frac{\kappa F_-}
{10^{m_3}Q_{12}(\kappa+2G)}.
}
\tag{3.1}
\]

同理由 (2.6)：

\[
\boxed{
t
=
\frac{10^{m_3}Q_{12}\mathcal N_{12}}{F_+}.
}
\tag{3.2}
\]

这是本轮最重要的 information-theoretic identity。

它意味着：

> 给定既知 source coefficients
> \[
> \kappa,Q_{12},G,\mathcal N_{12},m_3
> \]
> 和 source-labelled \(F_-\) 或 \(F_+\)，
> 整个 rational gap root \(t=\mu/\nu\) 都被精确恢复。

因此对任何素数 \(p\)，其：

- valuation \(v_p(t)\)；
- normalized unit；
- 模 \(p\) 的 square class；
- branch sign；
- 任意深度的 lifted digits

都由 oriented factor 精确决定。

所以本轮已经排除如下可能：

\[
\boxed{
\text{orientation 已知之后还存在某个第一 surviving higher digit }c_r.
}
\]

不存在这样的 \(r\)。

---

# 4. \(p\)-adic valuation normalization

固定

\[
p\in\{2,5\}.
\]

写

\[
\mu=p^{r_p}\mu_p,
\qquad
\nu=p^{s_p}\nu_p,
\]

其中

\[
\mu_p,\nu_p\in\mathbf Z_p^\times.
\]

再写

\[
\kappa+2G=p^{f_p}\alpha_p,
\]

\[
\kappa=p^{k_p}\beta_p,
\]

\[
\mathcal N_{12}=p^{n_p}\eta_p,
\]

\[
G_0=p^{c_p}\gamma_p,
\]

其中

\[
\alpha_p,\beta_p,\eta_p,\gamma_p\in\mathbf Z_p^\times.
\]

令

\[
\delta_p:=\frac{2}{p^{v_p(2)}}.
\]

于是

\[
\delta_2=1,
\qquad
\delta_5=2.
\]

旧 factors 的 valuations 为

\[
v_p(F_-)
=
v_p(2)+f_p+2r_p-c_p,
\]

\[
v_p(F_+)
=
v_p(2)+k_p+n_p+2s_p-c_p.
\]

顶部 double resonance 恰为

\[
\boxed{
f_p+2r_p
=
k_p+n_p+2s_p.
}
\tag{4.1}
\]

令公共 factor valuation 为

\[
\boxed{
e_p
:=
v_p(F_-)
=
v_p(F_+).
}
\tag{4.2}
\]

则 normalized factor units 为

\[
\boxed{
U_{-,p}
:=
p^{-e_p}F_-
=
\delta_p\gamma_p^{-1}\alpha_p\mu_p^2,
}
\tag{4.3}
\]

\[
\boxed{
U_{+,p}
:=
p^{-e_p}F_+
=
\delta_p\gamma_p^{-1}\beta_p\eta_p\nu_p^2.
}
\tag{4.4}
\]

---

# 5. 旧 Hensel root relation 的真正内容

旧 deep phase 的本质是两个 equal-valuation factor units 深度相消。

若旧证明在某一层给出

\[
p^{R_p}\mid
U_{-,p}+U_{+,p},
\]

则由 (4.3)–(4.4)：

\[
\alpha_p\mu_p^2
+
\beta_p\eta_p\nu_p^2
\equiv0
\pmod{p^{R_p}}.
\]

因为 \(\nu_p\) 是 unit，

\[
\boxed{
\left(
\frac{\mu_p}{\nu_p}
\right)^2
\equiv
-
\frac{\beta_p\eta_p}{\alpha_p}
\pmod{p^{R_p}}.
}
\tag{5.1}
\]

因此旧记号 \(\rho_p\) 的可审计数学角色必然是某个 unit root：

\[
\boxed{
\rho_p^2
\equiv
-
\frac{\beta_p\eta_p}{\alpha_p}
\pmod{p^{R_p}},
}
\tag{5.2}
\]

从而旧 Hensel branch 写成类似

\[
\boxed{
\mu_p
\equiv
\text{(one lifted root)}\cdot\nu_p
\pmod{p^{R_p}}.
}
\tag{5.3}
\]

对 \(p=5\)，现有 source interface 明确记录为

\[
\boxed{
\mu_5
\equiv
\pm\rho_5\nu_5
\pmod{5^{R_5}}.
}
\tag{5.4}
\]

对 \(p=2\)，当前 library 没暴露旧 \(\rho_2\) 的原始 branch convention，
因此只能安全保留 (5.1) 的 square-root relation，
不能声称旧证明究竟把四个 \(2\)-adic local roots 如何编号。

---

# 6. 旧 phase 如何进入 \(J^\sharp,K^\sharp\)

由 (2.12)，对每个 \(p=2,5\) 有

\[
e_p=v_p(\Lambda D_0).
\]

定义

\[
\boxed{
c_p
:=
p^{-e_p}\Lambda D_0
\in\mathbf Z_p^\times.
}
\tag{6.1}
\]

于是无序地有

\[
\boxed{
\{U_{-,p},U_{+,p}\}
=
\{
c_pJ^\sharp,\,
c_pK^\sharp
\}.
}
\tag{6.2}
\]

因此

\[
U_{-,p}+U_{+,p}
=
c_p(J^\sharp+K^\sharp)
=
c_pH^\sharp.
\]

所以

\[
\boxed{
v_p(U_{-,p}+U_{+,p})
=
v_p(H^\sharp).
}
\tag{6.3}
\]

若旧 \(R_p\) 是一个 certified lower depth，则

\[
R_p\le v_p(H^\sharp).
\]

若旧 \(R_p\) 本身定义为最大相消深度，则

\[
\boxed{
R_p=v_p(H^\sharp).
}
\tag{6.4}
\]

这证明：

\[
\boxed{
\text{旧 Hensel cancellation depth 完全进入了 }
H^\sharp.
}
\]

它不是独立 gate。

---

# 7. 信息量审计总表

下面把旧 Hensel 信息拆成：

\[
\text{valuation depth}
+
\text{unit square class}
+
\text{branch sign}
+
\text{higher lifted digits}.
\]

## 7.1 \(p=5\)

| 信息成分 | source 表达 | post-deflation 状态 | 分类 |
|---|---|---|---|
| valuation normalization | \(r_5,s_5,f_5,k_5,n_5,c_5\) 与 resonance (4.1) | 决定公共 \(e_5\)，再进入 \(\Lambda D_0\) | Projection-surviving / 已知 normalization |
| cancellation depth | \(R_5\) | \(v_5(H^\sharp)\) 或其已证下界 | **Endogenous** |
| unit square class | \(-\beta_5\eta_5/\alpha_5\) | 由 normalized factor pair 的比值恢复 | Projection-surviving |
| \(\pm\) branch | \(\mu_5/\nu_5\equiv\pm\rho_5\) | 两个 oriented factor assignments / Vieta-conjugate roots | **可能只剩 orientation bit** |
| higher lifted digits | \(\mu_5/\nu_5\bmod5^r\) | oriented factor 经 (3.1) 精确恢复 | **Endogenous once orientation fixed** |

因此：

\[
\boxed{
p=5:
\quad
\text{不存在独立 higher digit；
唯一可能遗失的是 factor/root orientation。}
}
\]

---

## 7.2 \(p=2\)

对 \(R\ge3\)，若只看

\[
x^2\equiv-N^\sharp\pmod{2^R},
\]

一个 odd square 可有四个 local roots。
以 \(J^\sharp\) 为一根，可写成

\[
J^\sharp,\quad
-J^\sharp,\quad
J^\sharp+2^{R-1},\quad
-J^\sharp+2^{R-1}
\pmod{2^R}.
\]

但完整 gap quadratic 全球只有至多两个 algebraic roots。

因此必须区分：

\[
\boxed{
\text{local }2\text{-adic root multiplicity}
\neq
\text{global gap-root branching}.
}
\]

本轮可证明的是：

| 信息成分 | source 表达 | post-deflation 状态 | 分类 |
|---|---|---|---|
| valuation normalization | \(r_2,s_2,f_2,k_2,n_2,c_2\) 与 resonance | 公共 \(e_2\)，进入 \(\Lambda D_0\) | Projection-surviving |
| cancellation depth | old \(R_2\) | \(v_2(H^\sharp)\) 或其下界 | **Endogenous** |
| unit square class | \(-\beta_2\eta_2/\alpha_2\) | normalized factor pair 决定 | Projection-surviving |
| global algebraic branch | \(t\) vs \(t^\vee\) | factor orientation | **可能只剩 orientation bit** |
| extra local \(2\)-adic root labels | 旧 \(\rho_2\) convention 未暴露 | 无法确认是否曾被 source convention 使用 | **Representation obstruction** |
| higher digits on chosen global branch | exact \(t\) | oriented factor 经 (3.1) 精确恢复 | **Endogenous once orientation fixed** |

因此：

\[
\boxed{
p=2:
\quad
\text{也没有证据存在 surviving higher digit；
但旧四根 branch 编号的原始定义缺失。}
}
\]

---

# 8. Branch sign audit：交换因子就是 Vieta root exchange

DD gap quadratic (2.3) 的两个根设为

\[
t,\quad t^\vee.
\]

Vieta 给出

\[
\boxed{
tt^\vee
=
\frac{\kappa\mathcal N_{12}}
{\kappa+2G}.
}
\tag{8.1}
\]

因此

\[
\boxed{
t^\vee
=
\frac{\kappa\mathcal N_{12}}
{(\kappa+2G)t}.
}
\tag{8.2}
\]

另一方面，若 \(F_-\) 对应 root \(t\)，则由 (3.1)

\[
F_-
=
10^{m_3}Q_{12}
\frac{\kappa+2G}{\kappa}t.
\]

若交换两 source-labelled factors，把原来的 \(F_+\) 当作新的 \(F_-\)，则恢复出的 ratio 为

\[
\begin{aligned}
t_{\rm swap}
&=
\frac{\kappa F_+}
{10^{m_3}Q_{12}(\kappa+2G)}\\
&=
\frac{\kappa}{10^{m_3}Q_{12}(\kappa+2G)}
\cdot
\frac{10^{m_3}Q_{12}\mathcal N_{12}}{t}\\
&=
\frac{\kappa\mathcal N_{12}}
{(\kappa+2G)t}\\
&=
t^\vee.
\end{aligned}
\]

所以严格有

\[
\boxed{
F_-\leftrightarrow F_+
\quad\Longleftrightarrow\quad
t\leftrightarrow t^\vee.
}
\tag{8.3}
\]

这证明了：

\[
\boxed{
\text{source factor orientation 与 gap-quadratic root branch 是同一个二值分支。}
}
\]

它们不能被当成两个独立 bits。

---

# 9. Hensel \(\pm\) 与 factor exchange

由 resonance (4.1)：

\[
2(r_p-s_p)=k_p+n_p-f_p.
\]

定义 normalized gap unit

\[
u_p:=\frac{\mu_p}{\nu_p}.
\]

对 Vieta 共轭根 \(t^\vee\)，对应 normalized unit 记为 \(u_p^\vee\)。

由 (8.1) 的 \(p\)-adic unit part：

\[
\boxed{
u_pu_p^\vee
=
\frac{\beta_p\eta_p}{\alpha_p}.
}
\tag{9.1}
\]

而 Hensel relation (5.1) 给出

\[
u_p^2
\equiv
-\frac{\beta_p\eta_p}{\alpha_p}
\pmod{p^{R_p}}.
\]

于是

\[
u_pu_p^\vee
\equiv
-u_p^2
\pmod{p^{R_p}}.
\]

因为 \(u_p\) 是 unit，可约去：

\[
\boxed{
u_p^\vee
\equiv
-u_p
\pmod{p^{R_p}}.
}
\tag{9.2}
\]

因此在所有当前可审计的 Hensel 深度上：

\[
\boxed{
\text{Vieta conjugation}
\Longrightarrow
\text{opposite Hensel branch}.
}
\tag{9.3}
\]

对 \(p=5\)，这直接说明旧

\[
\pm\rho_5
\]

两支就是两个 global algebraic orientations 的局部投影。

对 \(p=2\)，(9.3) 至少识别出两条 global orientations；
但不能从当前材料断言旧证明是否还人为选择了四个 local roots 中的某个额外 lift label。

---

# 10. Higher lifted digits audit

用户要求特别检查：

\[
\frac{\mu_p}{\nu_p}
=
\pm\rho_p
+
c_1p^{r_1}
+
c_2p^{r_2}
+\cdots
\]

中是否存在第一位无法从 post-deflation state 恢复的 digit。

答案是：

\[
\boxed{
\textbf{在 source orientation 固定以后，不存在。}
}
\]

原因不是仅靠 Hensel 唯一性，而是更强的 exact rational identity (3.1)。

若

\[
F_-=\Lambda D_0X,
\qquad
X\in\{J^\sharp,K^\sharp\},
\]

则

\[
\boxed{
t
=
\frac{
\kappa\Lambda D_0X
}{
10^{m_3}Q_{12}(\kappa+2G)
}.
}
\tag{10.1}
\]

右侧是一个**精确有理数**。

所以对任意 \(r\ge1\)：

\[
t\bmod p^r
\]

全部可计算。

再从 \(v_p(t)=r_p-s_p\) 除去 valuation，即得

\[
u_p=\frac{\mu_p}{\nu_p}
\]

的任意深度 \(p\)-adic digit。

所以：

\[
\boxed{
\forall r,\qquad
u_p\bmod p^r
\text{ 由 oriented post factor 精确决定。}
}
\tag{10.2}
\]

没有最小 surviving \(r\)。

---

# 11. 非单射 projection audit

## 11.1 Algebraic representation level

定义 oriented source state 的 relevant projection：

\[
(t,F_-,F_+)
\mapsto
\{F_-,F_+\}.
\]

由 (8.3)，一般存在 involution

\[
\boxed{
(t,F_-,F_+)
\longleftrightarrow
(t^\vee,F_+,F_-),
}
\tag{11.1}
\]

它们映射到同一个 unordered factor pair。

因此在**algebraic representation level**，
projection generically 是二对一。

这就是 source orientation bit 被丢掉的精确位置。

---

## 11.2 Post-deflation symmetric state

因为

\[
H^\sharp=J^\sharp+K^\sharp,
\qquad
N^\sharp=J^\sharp K^\sharp,
\]

所以交换

\[
J^\sharp\leftrightarrow K^\sharp
\]

不会改变

\[
(H^\sharp,N^\sharp).
\]

因此：

\[
\boxed{
\omega_{\rm src}
\text{ 不可能由对称二次数据 }
(H^\sharp,N^\sharp)
\text{恢复。}
}
\]

若只保留 unordered pair

\[
\{J^\sharp,K^\sharp\},
\]

同样无法恢复。

---

## 11.3 但是否存在两个合法 source candidates？

这里必须保持量词纪律。

现有证明只告诉我们：

- gap quadratic 有两个 theoretical roots；
- 交换 roots 与交换 factors 对应；
- 一个完整 candidate 的 actual gap root 是确定的。

它**没有证明**：

\[
t\text{ 与 }t^\vee
\]

都同时满足：

- 同一个 \(G_0\) recovery；
- 同一个 prefix/tail source decomposition；
- 同一个 primitive recovery；
- 同一个 decimal concatenation identity。

因此目前不能构造：

\[
S_1\neq S_2
\]

两个都合法的完整 source states，而又满足

\[
S_1,S_2
\mapsto
(J^\sharp,K^\sharp,H^\sharp,N^\sharp)
\]

完全相同。

反过来，也没有 theorem 证明至多一个 orientation globally recoverable。

所以用户提出的理想现象

\[
S_1,S_2
\mapsto
\text{same post state},
\qquad
\text{only one globally recoverable}
\]

当前正好停在这里。

---

# 12. “Phase defect”审计

## 12.1 没有发现非平凡 \(p\)-adic higher-digit defect

由于 oriented factor 已能恢复 exact \(t\)，
不存在一个真正新的

\[
\Theta_p
\]

其内容是“某一 higher Hensel digit 与 factor pair 不一致”。

任何这样的 defect 在 orientation 固定后恒等为零。

---

## 12.2 唯一剩余 defect 是 orientation defect

若强行定义最小 defect，可以定义

\[
\boxed{
\Theta_{\rm ori}
:=
\omega_{\rm src}.
}
\tag{12.1}
\]

或者对“假设 \(J^\sharp\) 是 \(F_-\)-side”定义：

\[
\boxed{
t_J
=
\frac{
\kappa\Lambda D_0J^\sharp
}{
10^{m_3}Q_{12}(\kappa+2G)
},
}
\tag{12.2}
\]

\[
\boxed{
t_K
=
\frac{
\kappa\Lambda D_0K^\sharp
}{
10^{m_3}Q_{12}(\kappa+2G)
}.
}
\tag{12.3}
\]

实际 source gap root \(t_{\rm src}\) 必须满足

\[
\boxed{
t_{\rm src}\in\{t_J,t_K\}.
}
\tag{12.4}
\]

并且

\[
\boxed{
\Theta_{\rm ori}=+1
\iff
t_{\rm src}=t_J.
}
\tag{12.5}
\]

这是一个真正 source-determined、post-symmetric state 看不到的 bit。

但它目前只能称为：

\[
\boxed{
\text{representation / orientation defect},
}
\]

不能称为已经证明的 independent arithmetic phase gate。

---

# 13. Orientation-quotiented collapse theorem

## 定理 SGR-7-COLLAPSE\(^\mathrm{or}\)

固定一个 DD source coefficient state

\[
(
Q_{12},
G,
\mathcal N_{12},
\kappa,
m_3,
\Lambda,
D_0,
\ldots
)
\]

以及 \(p\in\{2,5\}\)。

假设 source orientation 已给定，即已知

\[
F_-=\Lambda D_0X,
\qquad
X\in\{J^\sharp,K^\sharp\}.
\]

则：

1. \(t=\mu/\nu\) 由 (10.1) 唯一精确恢复；
2. \(v_p(t)=r_p-s_p\) 唯一恢复；
3. valuation-normalized unit
   \[
   u_p=\mu_p/\nu_p
   \]
   唯一恢复为 \(p\)-adic unit；
4. 对任意 \(R\ge1\)，
   \[
   u_p\bmod p^R
   \]
   唯一恢复；
5. old Hensel square relation
   \[
   u_p^2\equiv
   -\beta_p\eta_p/\alpha_p
   \pmod{p^{R_p}}
   \]
   只是该 exact ratio 的必要局部投影；
6. cancellation depth 由
   \[
   v_p(H^\sharp)
   \]
   给出；
7. 不存在 orientation 之外的 source-only Hensel digit。

故：

\[
\boxed{
\frac{
\text{old source Hensel data}
}{
F_-\leftrightarrow F_+
}
\quad
\text{在当前 DD reduction 中完全内生化。}
}
\tag{13.1}
\]

### 证明

(1)–(4) 由 exact inverse formula (3.1)；
(5) 由 normalized factor relation (5.1)；
(6) 由 (6.3)；
(7) 因任意 finite lifted digit 都是 exact \(t\) 的函数。

证毕。

---

# 14. 为什么本轮不能升级为 SGR-7D

SGR-7D 要求：

\[
\boxed{
\text{旧 source-level Hensel phase 全部内生化，没有任何独立剩余信息。}
}
\]

本轮已经证明：

\[
\boxed{
\text{orientation quotient 之后确实全部 collapse。}
}
\]

但还差一件事：

\[
\boxed{
\omega_{\rm src}
\text{ 是否可以合法 quotient 掉？}
}
\]

当前不能证明。

原因不是 higher digits 不清楚，而是：

1. source \(F_-/F_+\) 标签在 old/new bridge 中被变成 unordered pair；
2. 旧 \(\rho_2,\rho_5\) 原始 branch convention 没有暴露；
3. 未证明 Vieta-conjugate root 在相同 prefix/tail source state 下也通过完整 recovery；
4. 也未证明只有一个 orientation 可通过完整 recovery。

所以真正缺失的是 **source recovery datum / orientation theorem**，
不是另一个 \(p\)-adic estimate。

因此等级应为

\[
\boxed{
\textbf{SGR-7E — REPRESENTATION OBSTRUCTION}.
}
\]

---

# 15. 为什么不是 SGR-7A / 7B / 7C

## 15.1 不是 SGR-7A

没有找到已证 independent source phase congruence

\[
J^\sharp
\equiv
\Psi(\text{prefix/tail})
\pmod{p^r}
\]

且不由 factor pair 推出。

---

## 15.2 不是 SGR-7B

没有第一 surviving higher digit。

事实上 orientation 固定后，
所有 digits 都由 exact ratio 一次性恢复。

---

## 15.3 不优先标 SGR-7C

目前未决点并不是：

\[
\text{“审计到 }p^r\text{ 后下一位不知道”。}
\]

而是在进入任何 higher-digit audit 之前，
source-labelled orientation 已在 unordered projection 中被丢掉。

因此这比 ordinary partial information map 更准确地属于：

\[
\boxed{
\text{representation obstruction}.
}
\]

---

# 16. 本轮最终信息分解

可以把旧 DD deep Hensel 信息压成：

\[
\boxed{
\text{old phase information}
=
\mathcal E_{\rm val}
\oplus
\mathcal E_{\rm cancel}
\oplus
\mathcal E_{\rm root}
\oplus
\mathcal O_{\rm src}.
}
\]

其中：

### 1. Valuation normalization

\[
\mathcal E_{\rm val}
\]

由 source valuations 与 common factor valuation 决定，
在 deflation 中被显式剥除。

### 2. Cancellation depth

\[
\mathcal E_{\rm cancel}
\]

等价于

\[
v_p(H^\sharp).
\]

完全 endogenous。

### 3. Lifted root digits modulo orientation

\[
\mathcal E_{\rm root}
\]

由 oriented post factor 经 exact inverse formula 精确恢复。

完全 endogenous。

### 4. Source orientation

\[
\boxed{
\mathcal O_{\rm src}
=
\omega_{\rm src}\in\{\pm1\}.
}
\]

这是目前唯一可能在 unordered projection 中消失的 datum。

所以最清楚的结论是：

\[
\boxed{
\text{old phase information}
=
\text{endogenous part}
\oplus
\text{at most one source-orientation bit}.
}
\tag{16.1}
\]

---

# 17. Hensel synchronization 路线是否可以正式废弃？

当前应区分两种说法。

## 可以正式废弃的版本

以下路线可以永久停止：

\[
\boxed{
\text{继续从 }
(J^\sharp)^2\equiv-N^\sharp
\pmod{p^R}
\text{ 本身寻找独立 phase gate。}
}
\]

同样可以停止寻找：

\[
\boxed{
\text{orientation 固定以后某个新的 higher lifted digit。}
}
\]

因为它们已被严格证明内生。

---

## 暂时不能废弃的唯一残片

只保留：

\[
\boxed{
\text{source orientation 是否被完整 decimal recovery 单独锁定？}
}
\]

这已经不是“继续 Hensel lifting”的任务，
而是一个 source-labelled recovery / representation 问题。

若下一轮证明 orientation 只是 factor exchange，
则立即升级为：

\[
\boxed{
\textbf{SGR-7D — COMPLETE COLLAPSE},
}
\]

并永久废弃 DD Hensel synchronization 路线。

若证明只有一个 orientation 通过 prefix/tail recovery，
则得到：

\[
\boxed{
\textbf{SGR-7A — INDEPENDENT SOURCE PHASE FOUND},
}
\]

但其最小 invariant 应是 orientation/source-root selection，
而不是某个 higher Hensel digit。

---

# 18. 下一轮唯一 terminal target

本轮只留下一个目标：

\[
\boxed{
\textbf{DD Source-Orientation Recovery Theorem}.
}
\]

精确问题：

给定一个完整 DD post-deflation state

\[
(
J^\sharp,K^\sharp,H^\sharp,N^\sharp
)
\]

以及全部 already-known source coefficients

\[
(
Q_{12},G,\mathcal N_{12},\kappa,m_3,\Lambda,D_0,\ldots
),
\]

定义两个 candidate gap roots

\[
t_J
=
\frac{
\kappa\Lambda D_0J^\sharp
}{
10^{m_3}Q_{12}(\kappa+2G)
},
\]

\[
t_K
=
\frac{
\kappa\Lambda D_0K^\sharp
}{
10^{m_3}Q_{12}(\kappa+2G)
}.
\]

证明以下二者之一：

### Collapse alternative

\[
\boxed{
t_J\leftrightarrow t_K
\text{ 只是可 quotient 的 factor/Vieta exchange，}
}
\]

从而 source orientation 不增加 recovery information。

### Surviving-source alternative

\[
\boxed{
\text{prefix/tail source recovery 恰好选择 }t_J\text{ 或 }t_K
\text{ 中的一支，}
}
\]

并把这个选择写成显式 source formula。

除此之外，不再研究任何 Hensel higher digit。

---

# 19. Final verdict

\[
\boxed{
\textbf{SGR-7E — REPRESENTATION OBSTRUCTION}.
}
\]

本轮已经证明：

\[
\boxed{
\text{不存在 surviving higher Hensel digit。}
}
\]

并得到 orientation-quotiented collapse：

\[
\boxed{
\text{一旦 }F_-/F_+\text{ 的 source orientation 恢复，}
\quad
(\mu,\nu)\text{ 的全部 }2\text{-adic 与 }5\text{-adic phase}
\text{都由 }J^\sharp,K^\sharp
\text{精确决定。}
}
\]

当前唯一可能丢失的信息是：

\[
\boxed{
\omega_{\rm src}
=
\text{“哪一个 post factor 是 source }F_-\text{”}
}
\]

这一单独 orientation bit。

它是否只是因子交换，还是完整 prefix/tail recovery 真正锁定的一位 source datum，
现有可见 proof library 尚不足以决定。

因此：

\[
\boxed{
\text{DD 的 Hensel higher-digit synchronization 路线可以正式停止；}
}
\]

但

\[
\boxed{
\text{source-orientation recovery 仍需最后一次独立审计。}
}
\]

