# 三项十进制拼接平方和问题：DD Orientation-Recovery Campaign

**文件名：** `strict_layer_DD_orientation_recovery_campaign.md`  
**研究范围：** Strict Layer，仅研究当前开放的 **DD top chamber**  
**本轮主等级：**
\[
\boxed{\textbf{SGR-8B — ORIENTATION RECOVERY GATE}}
\]
**最终状态：** orientation 已严格恢复；DD **尚未闭合**。  
**本轮最重要的新结论：**

\[
\boxed{
\omega_{\rm src}=+1,
\qquad
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp.
}
\]

也就是说，当前顶部 DD 中 source-labelled \(F_-\) **必为较小因子**；Vieta 共轭支并不是第二个合法 decimal candidate，而是在第三分子恢复时直接落入负数。

更进一步，本轮得到新的 exact source-labelled allocation 与一个完全显式的 oriented tail recovery invariant：

\[
\boxed{
\frac{\kappa+2G}{\gcd(\kappa,G)}
\mid F_-,
\qquad
\frac{\kappa}{\gcd(\kappa,G)}
\mid F_+,
}
\]

以及

\[
\boxed{
2a_3
=
\frac{F_+}{\kappa}
-
\frac{F_-}{\kappa+2G}
=
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right).
}
\]

因此 SGR-7 所剩的 orientation bit 已被彻底消去；新的唯一 terminal frontier 不再是 Hensel/orientation，而是：

\[
\boxed{
\textbf{DD Oriented Tail-Window Gap:}
\quad
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right)
\text{ 不可能落入 }
[2\cdot10^{n_3-1},\,2\cdot10^{n_3})
\text{ 的证明。}
}
\]

以下所有新陈述严格标记为 **PROVED / DERIVED / HEURISTIC / COMPUTATIONAL EVIDENCE / FAILED / OPEN**。

---

# 0. 本轮从哪里开始

SGR-7 已经证明：

\[
\{F_-,F_+\}
=
\{\Lambda D_0J^\sharp,\Lambda D_0K^\sharp\},
\]

其中

\[
J^\sharp=\frac{M-Y}{D_0},
\qquad
K^\sharp=\frac{M+Y}{D_0},
\]

并且一旦 source-labelled \(F_-\) 被指定，就有

\[
\boxed{
t:=\frac{\mu}{\nu}
=
\frac{\kappa F_-}
{10^{m_3}Q_{12}(\kappa+2G)}
}
\tag{0.1}
\]

以及

\[
\boxed{
t
=
\frac{10^{m_3}Q_{12}\mathcal N_{12}}{F_+}.
}
\tag{0.2}
\]

交换两个 source factors 恰好把 \(t\) 送到 Vieta 共轭

\[
\boxed{
t^\vee
=
\frac{\kappa\mathcal N_{12}}
{(\kappa+2G)t}.
}
\tag{0.3}
\]

SGR-7 因而把所有 source-level Hensel higher digits 都压缩掉，只留下

\[
\omega_{\rm src}\in\{\pm1\},
\]

其中约定

\[
\omega_{\rm src}=+1
\iff
F_-=\Lambda D_0J^\sharp,
\]

\[
\omega_{\rm src}=-1
\iff
F_-=\Lambda D_0K^\sharp.
\]

本轮不再追旧 \(\rho_p\) 的 branch naming convention，而直接从原六变量 decimal equation 反向恢复第三块。

---

# 1. 来源审计

## 1.1 本轮实际核对的主文件

重点核对：

- `strict_layer_DD_source_phase_information_audit.md`
- `strict_layer_DD_supply_phase_synchronization_campaign.md`
- `strict_layer_DD_post_deflation_campaign.md`
- `strict_layer_DD_error_closure_campaign.md`
- `exact_lift_research_synthesis_2026-08-10.md`

并交叉使用：

- `strict_layer_unified_exact_lift_campaign(1).md`
- `strict_layer_moving_core_square_spacing_campaign.md`
- backward recovery / synchronization 系列报告

用于确认 Exact-Lift 的反向 side conditions 与当前 top-DD 范围。

## 1.2 原始接口中真正需要的定义

本轮只使用以下已经可审计、且足以从定义重建 orientation 的接口：

\[
\mathcal R
=
\sqrt{r_1^2+r_2^2+r_3^2},
\]

\[
\boxed{
G(\mathcal R-r_3)=\frac{\mu}{\nu},
\qquad
\gcd(\mu,\nu)=1,
}
\tag{1.1}
\]

以及

\[
G_0
=
\gcd(
\mathcal N_{12}\nu^2-\mu^2,\,
2G\mu\nu
).
\]

DD 中

\[
Q:=Q_{12}=b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\]

\[
N:=\mathcal N_{12}
=
(a_1b_2)^2+(a_2b_1)^2,
\]

\[
A:=A_{12}
=
a_1 10^{n_2}+a_2,
\]

\[
C=10^{d_3}A,
\qquad
T:=10^{m_3},
\]

\[
\boxed{
\kappa
=
\frac{TQG}{b_3}
\in\mathbf Z_{>0},
\qquad
QG<\kappa\le10QG.
}
\tag{1.2}
\]

后文为避免与新归一化字母冲突，除特别说明外仍写 \(Q,G,N,C,T,\kappa\)。

---

# 2. 直接回到原六变量拼接等式

这是本轮关键步骤：不把 gap quadratic 当作黑箱，而把两个 Vieta roots 直接拉回原第三块。

DD 中

\[
n_3=m_3+d_3,
\]

故原分子拼接为

\[
\alpha
=
A10^{n_3}+a_3
=
T C+a_3,
\]

原分母拼接为

\[
\beta
=
Q10^{m_3}+b_3
=
TQ+b_3.
\]

同时

\[
r_1^2+r_2^2=\frac{N}{G^2}.
\]

因此原题在固定前两块后精确变成

\[
\boxed{
\frac{TC+a_3}{TQ+b_3}
=
\sqrt{
\frac N{G^2}
+
\frac{a_3^2}{b_3^2}
}.
}
\tag{2.1}
\]

由于合法 candidate 中所有量均正，平方不会引入符号歧义：

\[
\boxed{
G^2b_3^2(TC+a_3)^2
=
(TQ+b_3)^2
(Nb_3^2+G^2a_3^2).
}
\tag{2.2}
\]

这是后面所有 recovery 判断的最终原题基准。

---

# 3. 原六变量方程关于 \(a_3\) 的精确二次式

由

\[
b_3=\frac{TQG}{\kappa}
\]

代入 (2.2)，清除严格正的公共因子，得到关于 \(a:=a_3\) 的二次式

\[
\boxed{
P_a(a)
=
\kappa^3(\kappa+2G)a^2
-
2CG^2T\kappa^2a
+
T^2
\left[
NQ^2(\kappa+G)^2
-
C^2G^2\kappa^2
\right]
=0.
}
\tag{3.1}
\]

**状态：PROVED / DERIVED FROM ORIGINAL EQUATION.**

这不是新的必要条件，而是固定 prefix 与 \(b_3\) 后原始拼接等式的精确二次化。

---

## 3.1 与旧 primitive tail quadratic 的一致性

旧 Exact-Lift 定义

\[
T=\delta_3L,
\qquad
b_3=\delta_3\tau,
\qquad
a_3=\delta_3z_3,
\]

并有

\[
\kappa=\frac{LQG}{\tau}.
\]

把这些代入 (3.1) 并除去公共正因子，恰得到旧 primitive tail quadratic

\[
\boxed{
-\kappa(\kappa+2G)z_3^2
+
2G^2LC\,z_3
+
\mathcal C_3
=0,
}
\]

其中

\[
\mathcal C_3
=
G^2L^2C^2
-
N(LQ+\tau)^2.
\]

所以本轮从原六变量重新导出的二次式与旧 Exact-Lift tail equation 完全一致。

**状态：PROVED.**

---

# 4. Gap root 到第三分子的仿射恢复

由原定义

\[
t
=
G(\mathcal R-r_3)
\]

和

\[
\mathcal R=\frac{TC+a}{TQ+b},
\qquad
r_3=\frac ab,
\qquad
b=\frac{TQG}{\kappa},
\]

直接计算得到

\[
\boxed{
t
=
\frac{
\kappa(CGT-\kappa a)
}{
QT(\kappa+G)
}.
}
\tag{4.1}
\]

因此

\[
\boxed{
a(t)
=
\frac{TCG}{\kappa}
-
\frac{TQ(\kappa+G)}{\kappa^2}\,t.
}
\tag{4.2}
\]

并且

\[
\boxed{
\frac{da}{dt}
=
-\frac{TQ(\kappa+G)}{\kappa^2}
<0.
}
\tag{4.3}
\]

所以 third-tail recovery 对 \(t\) **严格单调递减**。

**状态：PROVED.**

这已经说明：两个 Vieta roots 即使都为正，也不可能在第三块上保持同一个 \(a_3\)。

---

# 5. Gap quadratic 与 tail quadratic 真正共轭

Gap quadratic 是

\[
\boxed{
Q(\kappa+2G)t^2
-
2G\kappa Ct
+
\kappa QN
=0.
}
\tag{5.1}
\]

把 (4.2) 代入 (3.1)，可直接化为

\[
\boxed{
Q(\kappa+2G)t^2
-
2G\kappa Ct
+
\kappa QN
=
\frac{\kappa}
{QT^2(\kappa+G)^2}
P_a(a(t)).
}
\tag{5.2}
\]

右端比例因子严格为正。

因此：

\[
\boxed{
t\text{ 是 gap root}
\iff
a(t)\text{ 是原第三块二次式的 root}.
}
\]

更重要地，Vieta involution 在两层之间严格交换：

\[
\boxed{
t\longleftrightarrow t^\vee
\quad\Longleftrightarrow\quad
a\longleftrightarrow a^\vee.
}
\tag{5.3}
\]

**状态：PROVED.**

这解决了 SGR-7 中最关键的“Vieta 共轭是否真的能向 tail 层 lift”问题：  
它**能 lift 到 tail quadratic**；但它是否能 lift 到**正十进制第三分子**仍需检查。

---

# 6. 两个 tail roots 的精确和

由 (3.1) 的 Vieta 公式：

\[
\boxed{
a+a^\vee
=
\Sigma_a
:=
\frac{2TCG^2}
{\kappa(\kappa+2G)}.
}
\tag{6.1}
\]

同样由 gap quadratic：

\[
t+t^\vee
=
\frac{2G\kappa C}{Q(\kappa+2G)},
\]

\[
\boxed{
tt^\vee
=
\frac{\kappa N}{\kappa+2G}.
}
\tag{6.2}
\]

由于 \(a(t)\) 严格递减，较小的 gap root 对应较大的 tail root。

---

# 7. 顶部 DD 的十进制量级把共轭 tail root 直接推成负数

这是本轮的 decisive step。

记

\[
S:=S_{12}=m_1+m_2.
\]

当前真正开放的顶部 DD 满足

\[
10S+11\le n_3\le11S+3.
\]

因此区间非空立即给出

\[
\boxed{S\ge8.}
\tag{7.1}
\]

顶部又必在 \(d_3\)-dominant sector，因此 surplus simplex 给出

\[
s_1+s_2\le2.
\]

于是

\[
n_1+n_2
=
S+s_1+s_2
\le S+2.
\]

因此普通 numerator prefix 满足

\[
\boxed{
A<10^{S+2}.
}
\tag{7.2}
\]

而 denominator prefix \(Q\) 恰有 \(S\) 位，所以

\[
\boxed{
Q\ge10^{S-1}.
}
\tag{7.3}
\]

再由

\[
\kappa>QG,
\qquad
\kappa+2G>\kappa,
\]

从 (6.1) 得

\[
\Sigma_a
<
\frac{2TC}{Q^2}.
\]

由于

\[
C=10^{d_3}A<10^{d_3+S+2},
\]

故

\[
\boxed{
\Sigma_a
<
2T10^{d_3-S+4}.
}
\tag{7.4}
\]

另一方面，合法第三分子有

\[
n_3=m_3+d_3
\]

位，因此

\[
\boxed{
a_3
\ge
10^{n_3-1}
=
T10^{d_3-1}.
}
\tag{7.5}
\]

比较 (7.4)–(7.5)：

\[
\boxed{
\frac{\Sigma_a}{a_3}
<
2\cdot10^{5-S}.
}
\tag{7.6}
\]

而 \(S\ge8\)，所以

\[
\boxed{
\frac{\Sigma_a}{a_3}
<
2\cdot10^{-3}.
}
\tag{7.7}
\]

因此若 \(a_3\) 是合法 source root，

\[
a^\vee
=
\Sigma_a-a_3
<
-0.998\,a_3
<0.
\]

即

\[
\boxed{
a_3^\vee<0.
}
\tag{7.8}
\]

**状态：PROVED.**

这是本轮最关键的新定理。

---

# 8. DD Orientation Recovery Theorem

## 定理 SGR-8-ORT

对任意当前顶部 DD 的合法 original candidate，Vieta 共轭 branch 在完整 third-tail recovery 中恢复出负的第三分子。因此两个 gap roots 中恰有一个可能通过 original decimal positivity/digit recovery。

更精确地：

1. 两个 gap roots 都是正有理数；
2. 较小 root 对应较大的 tail root；
3. 合法 source tail root 为正且有 \(n_3\) 位；
4. 共轭 tail root 为负；
5. 因此 source root 必为较小 Vieta root。

### 证明

(1) 由 gap quadratic 的正 product 与正 sum；  
(2) 由 (4.3)；  
(3) 为 original candidate 定义；  
(4) 由 (7.8)；  
(5) 立即得到。

证毕。

---

# 9. 从较小 Vieta root 翻译回 \(F_-,F_+\)

由 source factor 定义

\[
F_-
=
\frac{2(\kappa+2G)\mu^2}{G_0},
\]

\[
F_+
=
\frac{2\kappa N\nu^2}{G_0},
\]

所以

\[
\frac{F_-}{F_+}
=
\frac{(\kappa+2G)t^2}{\kappa N}.
\]

而

\[
tt^\vee
=
\frac{\kappa N}{\kappa+2G}.
\]

source root 为较小 root，即

\[
t<t^\vee,
\]

故

\[
t^2<tt^\vee
=
\frac{\kappa N}{\kappa+2G}.
\]

于是

\[
\boxed{
F_-<F_+.
}
\tag{9.1}
\]

但 post-deflation 已知

\[
J^\sharp<K^\sharp,
\]

且

\[
\{F_-,F_+\}
=
\{\Lambda D_0J^\sharp,\Lambda D_0K^\sharp\}.
\]

所以只能有

\[
\boxed{
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp.
}
\tag{9.2}
\]

即

\[
\boxed{
\omega_{\rm src}=+1.
}
\tag{9.3}
\]

**状态：PROVED.**

这不是 gauge choice。  
这是 original decimal positivity / digit recovery 对两个 algebraic branches 的真实选择。

---

# 10. 一个显式 orientation-odd quantity

定义

\[
\boxed{
\Psi_{\rm ori}(a)
:=
\kappa(\kappa+2G)a
-
TCG^2.
}
\tag{10.1}
\]

因为两个 tail roots 的中点为

\[
\frac{\Sigma_a}{2}
=
\frac{TCG^2}{\kappa(\kappa+2G)},
\]

所以

\[
\Psi_{\rm ori}(a^\vee)
=
-\Psi_{\rm ori}(a).
\]

即

\[
\boxed{
\Psi_{\rm ori}\text{ 在 Vieta conjugation 下严格变号。}
}
\tag{10.2}
\]

顶部 DD 中由 (7.6) 甚至有

\[
\frac{TCG^2}
{\kappa(\kappa+2G)a_3}
<
10^{5-S}
\le10^{-3},
\]

因此

\[
\boxed{
\Psi_{\rm ori}(a_3)>0
}
\]

且具有很大的正 margin。

所以可写成：

\[
\boxed{
\omega_{\rm src}
=
\operatorname{sgn}\Psi_{\rm ori}
=
+1
}
\tag{10.3}
\]

对当前顶部 DD 的合法 source candidate 恒成立。

**状态：PROVED.**

---

# 11. 两条完整 recovery diagrams

以下固定同一个 prefix state

\[
(a_1,b_1,a_2,b_2),
\]

同一个

\[
(Q,G,N,C,T,\kappa,\Lambda,D_0,J^\sharp,K^\sharp).
\]

从仅有 \((Q,G,N)\) 当然不能唯一反解前两块；这里比较的是**同一个 source coefficient state 下的两种 orientation**。

---

## 11.1 Orientation \(\mathcal O_J\)

\[
F_-^{(J)}
=
\Lambda D_0J^\sharp,
\qquad
F_+^{(J)}
=
\Lambda D_0K^\sharp.
\]

由 SGR-7：

\[
t_J
=
\frac{\kappa F_-^{(J)}}
{TQ(\kappa+2G)}.
\]

把 \(t_J\) 既约为

\[
t_J=\frac{\mu_J}{\nu_J},
\qquad
\gcd(\mu_J,\nu_J)=1.
\]

从球面 gap 定义：

\[
N
=
G^2(\mathcal R^2-r_3^2)
=
t\,G(\mathcal R+r_3),
\]

因此

\[
\boxed{
r_3(t)
=
\frac{N/t-t}{2G}.
}
\tag{11.1}
\]

若 \(t=\mu/\nu\)，则

\[
r_3
=
\frac{N\nu^2-\mu^2}
{2G\mu\nu}.
\]

定义

\[
G_0(t)
=
\gcd(
N\nu^2-\mu^2,\,
2G\mu\nu
),
\]

则 reduced third block 必为

\[
\boxed{
a_3(t)
=
\frac{N\nu^2-\mu^2}{G_0(t)},
}
\tag{11.2}
\]

\[
\boxed{
b_3(t)
=
\frac{2G\mu\nu}{G_0(t)}.
}
\tag{11.3}
\]

对真正 source branch，primitive recovery

\[
TQG_0=2\kappa\mu\nu
\]

又给出

\[
b_3(t_J)=\frac{TQG}{\kappa},
\]

与固定 denominator tail 完全一致。

随后检查：

- \(a_3>0\)；
- \(\gcd(a_3,b_3)=1\)；
- \(a_3\) 恰有 \(n_3\) 位；
- \(b_3\) 恰有 \(m_3\) 位；
- \(d_3=n_3-m_3>0\)；
- 原拼接
  \[
  \alpha=TC+a_3,\quad\beta=TQ+b_3;
  \]
- 原等式 (2.1)。

对 actual candidate，这条链全部通过。

---

## 11.2 Orientation \(\mathcal O_K\)

反过来令

\[
F_-^{(K)}
=
\Lambda D_0K^\sharp,
\qquad
F_+^{(K)}
=
\Lambda D_0J^\sharp.
\]

则

\[
t_K=t_J^\vee.
\]

它仍是正有理 gap root，因此仍可唯一约分成

\[
t_K=\frac{\mu_K}{\nu_K}.
\]

也仍可形式计算

\[
G_{0,K},
\qquad
r_{3,K},
\qquad
a_{3,K},
\qquad
b_{3,K}.
\]

但是顶部 DD 中已经严格证明：

\[
\boxed{
a_{3,K}=a_3^\vee<0.
}
\]

所以 recovery 在以下 side condition 处立即失败：

\[
\boxed{
a_3\in\mathbf Z_{>0}.
}
\]

因此不需要继续争论：

- \(G_{0,K}\) 是否与原 \(G_0\) 相同；
- \(b_{3,K}\) 是否仍等于原 \(b_3\)；
- 重新约分后 digit length 是否改变；
- gcd profile 是否改变；
- chamber 是否保持。

这些更后的检查都已被 positivity failure 前置截断。

---

# 12. Vieta involution 到底保持什么、不保持什么

| recovery datum | Vieta conjugation 是否保持 | 结论 |
|---|---:|---|
| gap quadratic | 是 | 两 roots 都是 algebraic roots |
| \(t>0\) | 是 | 两 roots 都为正 |
| 固定 prefix \(Q,G,N,C\) | 是 | coefficient state 不变 |
| reduced rational representation of \(t\) | 各自可唯一做 | \((\mu,\nu)\) 会改变 |
| gap discriminant | 是 | 同一二次式 |
| factor unordered pair | 是 | 恰交换 \(F_-,F_+\) |
| projected Hensel relation | 是/内生 | SGR-6/7 已证明无新信息 |
| third-tail quadratic | 是 | 恰交换两个 tail roots |
| \(a_3>0\) | **否** | 共轭支变成负数 |
| \(n_3\)-digit window | **否** | 共轭支连 positivity 都失败 |
| primitive \(b_3\) recovery | 不必再判 | 共轭支已提前死亡 |
| \(\gcd(a_3,b_3)=1\) | 不必再判 | 同上 |
| DD chamber membership | **否** | 负 \(a_3\) 不是 decimal block |
| original positive decimal candidate | **否** | 只有 source branch 可达 |

因此：

\[
\boxed{
\text{Vieta conjugation 是 Exact-Lift algebraic symmetry，}
\text{但不是 original positive-decimal candidate symmetry。}
}
\]

**状态：PROVED.**

---

# 13. 不存在原候选集合上的 Vieta involution

若要构造用户要求的

\[
\mathscr V:
(a_1,b_1,a_2,b_2,a_3,b_3)
\mapsto
(a'_1,b'_1,a'_2,b'_2,a'_3,b'_3)
\]

并使其在当前固定 prefix coefficient state 下对应

\[
F_-\leftrightarrow F_+,
\]

第三分子必须变为

\[
a_3^\vee=\Sigma_a-a_3.
\]

但顶部 DD 已证

\[
a_3^\vee<0.
\]

所以这样的 involution 不可能作用在正整数六元组候选集合上。

\[
\boxed{
\text{SGR-8D ORIGINAL INVOLUTION 在顶部 DD 中被严格排除。}
}
\]

注意：这不排除在允许 signed third numerator 的扩大代数空间中存在 involution；但那不再是原题候选集合。

---

# 14. orientation 解决后继续推进：直接恢复 \(a_3\) 的 factor formula

由 (4.2) 与 SGR-7 的 exact inversion

\[
t
=
\frac{\kappa F_-}{TQ(\kappa+2G)},
\]

代入可得

\[
\boxed{
a_3
=
\frac{TCG}{\kappa}
-
\frac{\kappa+G}
{\kappa(\kappa+2G)}F_-.
}
\tag{14.1}
\]

利用

\[
F_-+F_+=2TGC,
\]

进一步得到对称得多的形式：

\[
\boxed{
2a_3
=
\frac{F_+}{\kappa}
-
\frac{F_-}{\kappa+2G}.
}
\tag{14.2}
\]

现在 orientation 已固定为

\[
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp,
\]

因此

\[
\boxed{
2a_3
=
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right).
}
\tag{14.3}
\]

**状态：PROVED.**

这是真正的 **oriented exact tail-recovery invariant**。

它完全不依赖旧 Hensel branch naming。

---

# 15. 一个此前缺失的 source-labelled divisor allocation

由 (14.1) 可重写：

\[
\boxed{
(\kappa+G)F_-
=
(\kappa+2G)(TCG-\kappa a_3).
}
\tag{15.1}
\]

利用 \(F_++F_-=2TCG\)，同样得到：

\[
\boxed{
(\kappa+G)F_+
=
\kappa
\left(
TCG+(\kappa+2G)a_3
\right).
}
\tag{15.2}
\]

令

\[
\boxed{
h:=\gcd(\kappa,G).
}
\]

则

\[
\gcd(\kappa+G,\kappa+2G)
=
\gcd(\kappa+G,G)
=
h,
\]

以及

\[
\gcd(\kappa+G,\kappa)=h.
\]

所以由 (15.1)–(15.2) 得

\[
\boxed{
\frac{\kappa+2G}{h}
\mid F_-,
}
\tag{15.3}
\]

\[
\boxed{
\frac{\kappa}{h}
\mid F_+.
}
\tag{15.4}
\]

这正是 SGR-6 中明确没有得到的 **source-labelled allocation**。

**状态：PROVED.**

---

# 16. 把 allocation 传到 \(J^\sharp,K^\sharp\)

记公共 post scale

\[
S_0:=\Lambda D_0.
\]

定义

\[
A_\kappa:=\frac{\kappa}{h},
\qquad
B_\kappa:=\frac{\kappa+2G}{h}.
\]

则

\[
A_\kappa\mid S_0K^\sharp,
\]

\[
B_\kappa\mid S_0J^\sharp.
\]

因此定义 residual divisors

\[
\boxed{
\mathfrak a
:=
\frac{A_\kappa}
{\gcd(A_\kappa,S_0)},
}
\]

\[
\boxed{
\mathfrak b
:=
\frac{B_\kappa}
{\gcd(B_\kappa,S_0)},
}
\]

有

\[
\boxed{
\mathfrak a\mid K^\sharp,
\qquad
\mathfrak b\mid J^\sharp.
}
\tag{16.1}
\]

同时若写

\[
\kappa=hA_\kappa,
\qquad
G=hD,
\qquad
\gcd(A_\kappa,D)=1,
\]

则

\[
B_\kappa=A_\kappa+2D,
\]

并且

\[
\boxed{
\gcd(A_\kappa,B_\kappa)
=
\gcd(A_\kappa,2)
\in\{1,2\}.
}
\tag{16.2}
\]

另外

\[
\frac{B_\kappa}{A_\kappa}
=
1+\frac{2G}{\kappa}
<
1+\frac2Q.
\tag{16.3}
\]

所以 source recovery 强制把一对**极近但几乎互素**的大整数分配到相反 post factors 上：

\[
\boxed{
B_\kappa\to J^\sharp\text{-side},
\qquad
A_\kappa\to K^\sharp\text{-side}.
}
\]

这不是 projected Hensel phase。

---

# 17. denominator normalization：\(A_\kappa\mid TQ\)

由

\[
\kappa b_3=TQG
\]

和

\[
\kappa=hA_\kappa,
\qquad
G=hD,
\qquad
\gcd(A_\kappa,D)=1,
\]

有

\[
A_\kappa b_3=TQD.
\]

故

\[
\boxed{
A_\kappa\mid TQ.
}
\tag{17.1}
\]

定义

\[
\boxed{
c:=\frac{TQ}{A_\kappa}\in\mathbf Z_{>0}.
}
\tag{17.2}
\]

于是

\[
\boxed{
b_3=cD.
}
\tag{17.3}
\]

特别 prime-to-\(10\) 部分满足

\[
\boxed{
A_\kappa^{\langle10\rangle}
\mid
Q^{\langle10\rangle}.
}
\tag{17.4}
\]

而

\[
B_\kappa^{\langle10\rangle}
\]

来自 \((\kappa+2G)^{\langle10\rangle}\)，故受旧 near-\(S\)-unit tail residual 控制。

这给出一个真正的 prefix/tail source label：

- \(A_\kappa\) 的非十进制部分由 denominator prefix \(Q\) 提供；
- \(B_\kappa\) 的非十进制部分由 \(\kappa+2G\) 的 tail residual 提供；
- 二者分别被强制进入 \(K^\sharp\) 与 \(J^\sharp\)。

---

# 18. 新的 canonical oriented factors \(u,v\)

由 (15.3)–(15.4) 定义

\[
\boxed{
u:=\frac{F_-}{B_\kappa}\in\mathbf Z_{>0},
}
\tag{18.1}
\]

\[
\boxed{
v:=\frac{F_+}{A_\kappa}\in\mathbf Z_{>0}.
}
\tag{18.2}
\]

由于

\[
TQ=A_\kappa c,
\qquad
b_3=Dc,
\]

旧 factor product

\[
F_-F_+
=
NTQ(TQ+2b_3)
\]

化为

\[
F_-F_+
=
N(A_\kappa c)(B_\kappa c).
\]

除以 \(A_\kappa B_\kappa\)：

\[
\boxed{
uv=Nc^2.
}
\tag{18.3}
\]

另一方面 SGR-7 的 root inversion 变成

\[
t
=
\frac{\kappa F_-}
{TQ(\kappa+2G)}
=
\frac{u}{c}.
\tag{18.4}
\]

而

\[
\frac Nt
=
\frac vc.
\]

代入

\[
r_3
=
\frac{N/t-t}{2G}
\]

并使用

\[
r_3=\frac{a_3}{b_3}
=
\frac{a_3}{cD},
\qquad
G=hD,
\]

得到

\[
\boxed{
v-u=2ha_3.
}
\tag{18.5}
\]

于是

\[
\boxed{
a_3=\frac{v-u}{2h}.
}
\tag{18.6}
\]

因为 \(a_3>0\)：

\[
\boxed{
u<v.
}
\tag{18.7}
\]

这给出了一个非常干净的 source recovery normal form：

\[
\boxed{
uv=Nc^2,
\qquad
v-u=2ha_3,
\qquad
b_3=cD.
}
\tag{18.8}
\]

**状态：PROVED.**

---

# 19. 一个有用但不独立的新 square identity

由

\[
uv=Nc^2,
\qquad
v-u=2ha_3,
\]

有

\[
\left(\frac{u+v}{2}\right)^2
=
h^2a_3^2+Nc^2.
\]

即

\[
\boxed{
h^2a_3^2+Nc^2
=
W_3^2,
\qquad
W_3:=\frac{u+v}{2}\in\mathbf Z.
}
\tag{19.1}
\]

**状态：DERIVED.**

但是该 square identity 本质上是原 integer-sphere recovery 的归一化重写，不应误报为独立第三个 square gate。

因此本轮**不**把它列为新 frontier。

---

# 20. orientation 还带来一个新的 prefix digit restriction

由 (4.1) 且 \(t>0\)：

\[
CGT-\kappa a_3>0.
\]

所以

\[
a_3
<
\frac{TCG}{\kappa}
<
\frac{TC}{Q}.
\]

又因

\[
a_3\ge T10^{d_3-1},
\qquad
C=10^{d_3}A,
\]

得到

\[
\boxed{
\frac AQ>\frac1{10}.
}
\tag{20.1}
\]

另一方面

\[
A<10^{n_1+n_2}
=
10^{S+s_1+s_2},
\]

\[
Q\ge10^{S-1},
\]

所以

\[
\frac AQ
<
10^{s_1+s_2+1}.
\]

若

\[
s_1+s_2\le-2,
\]

则右端 \(\le10^{-1}\)，与 (20.1) 矛盾。

因此当前顶部 DD 的 source candidate 还必须满足

\[
\boxed{
-1\le s_1+s_2\le2.
}
\tag{20.2}
\]

**状态：PROVED.**

旧 surplus simplex 只给上界 \(s_1+s_2\le2\)；本轮从 exact positive tail recovery 得到新的下界。

所以现在

\[
\boxed{
s_1+s_2\in\{-1,0,1,2\}.
}
\tag{20.3}
\]

这进一步表明顶部的极端 \(|s_1-s_2|\) 必须发生在几乎完全相反的两个 prefix slopes 上。

---

# 21. orientation 后的 one-sided residual supply 改进

SGR-5 为了不知道小因子来自 \(F_-\) 还是 \(F_+\)，只能做两情形 envelope，最终得到

\[
J^\sharp
\mid
(QN\mathscr T)^{\langle10\rangle\,2}.
\]

现在已经证明小因子**必为 \(F_-\)**。

固定 \(p\ne2,5\)，记

\[
q=v_p(Q),
\quad
n=v_p(N),
\quad
a=v_p(\kappa),
\quad
b=v_p(\kappa+2G),
\]

\[
r=v_p(\mu),
\quad
\tau=v_p(\mathscr T)=2a+b.
\]

由 rational-root divisibility

\[
\mu\mid\kappa QN
\]

有

\[
r\le a+q+n.
\]

而

\[
F_-
=
\frac{2(\kappa+2G)\mu^2}{G_0}.
\]

忽略只会降低 \(p\)-valuation 的 \(G_0\) 与公共 scale，有

\[
v_p(J^\sharp)
\le
b+2r
\le
b+2a+2q+2n
=
\tau+2q+2n.
\]

因此

\[
\boxed{
J^\sharp
\mid
\left(
Q^2N^2\mathscr T
\right)^{\langle10\rangle}.
}
\tag{21.1}
\]

**状态：PROVED.**

相比旧

\[
(QN\mathscr T)^{\langle10\rangle\,2},
\]

本轮严格节省了一个完整的 \(\mathscr T^{\langle10\rangle}\) exponent。

这正是 orientation recovery 被立即用于 DD 后得到的 one-sided supply improvement。

---

# 22. 为什么这些新结果仍未直接关闭 DD

本轮继续尝试了几种立即闭合方式。

## 22.1 试图用 \(B_\kappa>Q\) 压死小因子

由

\[
B_\kappa
=
\frac{\kappa+2G}{h}
>
\frac{\kappa}{G}
>
Q
\]

可知分配到小 factor 的 source modulus 本身至少有 \(S\) 位量级。

但是实际 post factor 是

\[
F_-=\Lambda D_0J^\sharp.
\]

巨大公共 scale \(\Lambda D_0\) 可以吸收 \(B_\kappa\) 的大量 \(2,5\)-primary 部分及部分 primitive content。

因此不能推出

\[
B_\kappa\mid J^\sharp
\]

本身，只能推出 residual

\[
\mathfrak b
=
B_\kappa/\gcd(B_\kappa,\Lambda D_0)
\mid J^\sharp.
\]

而 near-\(S\)-unit 正允许 \(B_\kappa\) 的主要高度储存在 \(2,5\) 中。

**状态：FAILED.**

---

## 22.2 试图用 \(A_\kappa,B_\kappa\) 几乎互素直接 CRT 矛盾

已有

\[
\gcd(A_\kappa,B_\kappa)\le2
\]

且二者相对距离

\[
\frac{B_\kappa-A_\kappa}{A_\kappa}
=
\frac{2G}{\kappa}
<
\frac2Q.
\]

这看起来像一对极近、几乎互素的大整数。

但是它们被分配到**不同 factors**：

\[
B_\kappa\to F_-,
\qquad
A_\kappa\to F_+.
\]

没有现成等式要求它们同时整除同一个小整数。

因此单纯 CRT 不产生 contradiction。

**状态：FAILED.**

---

## 22.3 试图用 \(uv=Nc^2\) 与 \(v-u=2ha_3\) 做 factor-spacing

如果

\[
uv=P
\]

固定，差 \(v-u\) 的确受 factor pair 离散性约束。

但是当前

\[
P=Nc^2
\]

本身随 prefix 与 tail scale 移动，且高度足以容纳

\[
2ha_3.
\]

粗 inequality

\[
v-u<uv
\]

给出的上界远不足以与 top digit window 冲突。

**状态：FAILED.**

---

## 22.4 试图把 (19.1) 当作新的平方门

\[
h^2a_3^2+Nc^2=W_3^2
\]

形式上很好看。

但反查定义后发现它就是 integer-sphere / gap factorization 的规范重写，没有产生独立于已知 sphere gate 的第二张票。

因此不能用它虚构新的 square-spacing contradiction。

**状态：FAILED AS INDEPENDENT GATE.**

---

# 23. failed attempts ledger

## 23.1 size orientation

**idea：** 根据 \(J^\sharp<K^\sharp\) 猜 source \(F_-\) 必然是小因子。  
**希望：** \(F_-\) 的减号命名似乎暗示“小”。  
**失败点：** 在 SGR-7 前这完全是 circular；\(F_-\) 的下标来自 source formula，不是大小定义。  
**本轮修复：** 先从 tail digit recovery 证明 actual \(t\) 是较小 Vieta root，再推出 \(F_-<F_+\)。

---

## 23.2 pure sign \(t^2<N\)

由

\[
r_3(t)
=
\frac{N/t-t}{2G}
\]

可知

\[
r_3>0
\iff
t^2<N.
\]

**idea：** 用这个条件直接证明两个 roots 中只有一个正-tail。  
**失败点：** 仅由

\[
tt^\vee
=
\frac{\kappa}{\kappa+2G}N<N
\]

不能排除两个 roots 同时小于 \(\sqrt N\)。  
需要 top decimal magnitude 才能把共轭 tail root推到负数。

**状态：FAILED ALONE.**

---

## 23.3 \(\mu-\nu\) sign

**idea：** 检查 Vieta conjugation 是否翻转 \(\mu-\nu\)。  
**失败点：** \(t\) 是否跨过 \(1\) 没有统一 top theorem；\(\mu-\nu\) 不是稳定 source orientation datum。

**状态：FAILED.**

---

## 23.4 gcd orientation

**idea：** 比较两个 roots 约分后的 \((\mu,\nu)\)、\(G_0\) 是否只有一支能满足 primitive recovery。  
**失败点：** 这确实可能产生非对称，但在 top DD 中已经无需追到这一层：共轭支在 \(a_3>0\) 处更早死亡。  
因此没有必要依靠一个更脆弱的 gcd branch theorem。

**状态：ABANDONED AFTER STRONGER RESULT.**

---

## 23.5 digit-length orientation

**idea：** 两 roots 通过同一 tail quadratic，但只有一根能进入 \(n_3\)-digit window。  
**结果：** 成功，而且得到比“跨位数边界”更强的结论：另一根直接为负。

**状态：PROVED SUCCESS.**

---

## 23.6 monotonicity

**idea：** recovery map \(a(t)\) 在两个 roots 之间严格单调。  
**结果：** 成功，且用于把“合法 tail root”翻译成“较小 gap root”。

**状态：PROVED SUCCESS.**

---

## 23.7 source involution

**idea：** 构造 original candidate 集合上的
\[
F_-\leftrightarrow F_+
\]
involution。  
**失败点：** 共轭 third numerator \(a_3^\vee<0\)，因此离开正整数 candidate space。

**状态：FAILED / IMPOSSIBILITY PROVED IN TOP DD.**

---

## 23.8 exact concatenation asymmetry

**idea：** Vieta root 可能保持平方 equation，但破坏 exact decimal recovery。  
**结果：** 成功。破坏点比 carry/gcd 更早：第三 numerator positivity / digit realization。

**状态：PROVED SUCCESS.**

---

# 24. toy-model / computational exploration

本轮使用 symbolic expansion 辅助发现并核对：

- 原六变量 \(a_3\)-quadratic；
- affine \(t\leftrightarrow a_3\) transformation；
- gap polynomial 与 tail polynomial 的正比例关系；
- normalized factor identities。

**COMPUTATIONAL EVIDENCE：** 符号展开与手工推导完全一致。

但最终定理没有依赖计算机代数黑箱；所有关键等式已经在正文中给出人工可审计推导。

另外可以构造脱离真实 prefix/digit side conditions 的小型 algebraic quadratics，使两个 tail roots 都为正。这说明：

\[
\boxed{
\text{“二次式本身”并不会自动选择 orientation。}
}
\]

真正负责选根的是 current top-DD decimal magnitude。

这些 toy states 不满足完整 original-source realizability，因此不作为原题反例。

---

# 25. Exact equivalence 的反向 side-condition 审计

从 terminal algebraic state 反向到 original candidate，必须依次通过：

1. **algebraic root**
   \[
   t\text{ satisfies gap quadratic};
   \]

2. **positive rational root**
   \[
   t>0;
   \]

3. **reduced root pair**
   \[
   t=\mu/\nu,\quad\gcd(\mu,\nu)=1;
   \]

4. **primitive third ratio**
   \[
   r_3=(N/t-t)/(2G);
   \]

5. **positive third numerator**
   \[
   N\nu^2-\mu^2>0;
   \]

6. **primitive gcd**
   \[
   G_0=\gcd(N\nu^2-\mu^2,2G\mu\nu);
   \]

7. **denominator match**
   \[
   \frac{2G\mu\nu}{G_0}
   =
   \frac{TQG}{\kappa};
   \]

8. **numerator digit window**
   \[
   10^{n_3-1}\le a_3<10^{n_3};
   \]

9. **denominator digit window**
   \[
   10^{m_3-1}\le b_3<10^{m_3};
   \]

10. **individual reducedness**
    \[
    \gcd(a_3,b_3)=1;
    \]

11. **DD chamber**
    \[
    d_3=n_3-m_3>0,
    \quad
    k_{12}>0;
    \]

12. **exact decimal concatenation**
    \[
    \alpha=TC+a_3,
    \quad
    \beta=TQ+b_3;
    \]

13. **original equation**
    \[
    \alpha/\beta=\mathcal R.
    \]

本轮证明：

\[
\boxed{
\text{Vieta conjugate 在第 5 项已经失败。}
}
\]

因此此前把 terminal algebraic system 与 actual source candidate 看得过近，确实遗漏了一个 real recovery filter。

但该 filter 现在已经被完全显式化，而不再是 representation obstruction。

---

# 26. 本轮对 SGR-6 / SGR-7 frontier 的修正

SGR-6 的 projected Hensel synchronization：

\[
(J^\sharp)^2\equiv-N^\sharp\pmod{p^R}
\]

已经证明只是

\[
p^R\mid H^\sharp
\]

的内生后果。

SGR-7 又把所有 higher source digits 压成 orientation bit。

本轮进一步证明：

\[
\boxed{
\omega_{\rm src}
\text{ 也不应继续作为 frontier。}
}
\]

但原因不是“orientation 是 gauge”，而是相反：

\[
\boxed{
\text{original decimal recovery 强制唯一 orientation。}
}
\]

所以此前“最后可能剩一 bit”的叙事应正式更新为：

\[
\boxed{
\text{Hensel phase 已全部死亡；}
\quad
\text{orientation 已由 tail recovery 固定；}
\quad
\text{真正独立信息是 oriented tail realization。}
}
\]

---

# 27. 新 canonical DD terminal system

在当前 top DD 中，从今以后可固定 ordered pair：

\[
\boxed{
J^\sharp<K^\sharp,
}
\]

并且不再保留 \(\omega_{\rm src}\)：

\[
\boxed{
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp.
}
\]

canonical source-tail parameters：

\[
h=\gcd(\kappa,G),
\]

\[
A_\kappa=\kappa/h,
\qquad
D=G/h,
\qquad
B_\kappa=A_\kappa+2D,
\]

\[
c=TQ/A_\kappa,
\qquad
b_3=cD.
\]

canonical oriented factor quotients：

\[
u=\frac{\Lambda D_0J^\sharp}{B_\kappa},
\]

\[
v=\frac{\Lambda D_0K^\sharp}{A_\kappa}.
\]

所有 actual candidates 必须满足

\[
\boxed{
u,v\in\mathbf Z_{>0},
}
\]

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

以及

\[
\boxed{
10^{n_3-1}\le\frac{v-u}{2h}<10^{n_3}.
}
\]

这就是 quotient 掉 Hensel ambiguity、恢复 orientation 后最自然的 source terminal coordinates。

---

# 28. 为什么 DD 仍未闭合

虽然得到：

\[
\omega_{\rm src}=+1,
\]

新的 source-labelled allocation，

\[
s_1+s_2\in\{-1,0,1,2\},
\]

以及改进后的

\[
J^\sharp
\mid
(Q^2N^2\mathscr T)^{\langle10\rangle},
\]

但现有 top-DD inequalities 尚不能证明 oriented tail difference

\[
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right)
\]

避开整个 \(2a_3\) digit window。

尤其：

- \(\Lambda D_0\) 仍移动；
- \(Q,N\) 的 prime support 仍移动；
- \(A_\kappa,B_\kappa\) 的大 \(2,5\)-primary 部分可能被公共 scale 吸收；
- normalized product \(uv=Nc^2\) 的高度仍足以容纳当前差值。

因此本轮不能标 SGR-8A。

---

# 29. 唯一剩余 terminal target

从现在起 DD 不再同时保留：

- projected Hensel CRT；
- source higher digits；
- orientation bit；
- factor swap ambiguity；

这些全部应从 frontier 删除。

唯一 terminal target 压成：

## DD Oriented Tail-Window Lemma

证明不存在当前 top-DD terminal state，使

\[
\boxed{
2\cdot10^{n_3-1}
\le
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right)
<
2\cdot10^{n_3}.
}
\tag{29.1}
\]

其中已经固定

\[
J^\sharp<K^\sharp,
\]

\[
J^\sharp K^\sharp=N^\sharp,
\qquad
J^\sharp+K^\sharp=H^\sharp,
\]

并同时继承当前所有 top-DD 已证条件。

因为左端精确等于

\[
2a_3,
\]

一旦证明 (29.1) 不可能，第三 numerator decimal recovery 即失败，DD 随即闭合。

这是本轮结束后唯一保留的 frontier。

\[
\boxed{
\textbf{OPEN: DD Oriented Tail-Window Lemma.}
}
\]

---

# 30. 最终 PROVED / DERIVED / HEURISTIC / COMPUTATIONAL / FAILED / OPEN ledger

## PROVED

1. 原六变量 DD equation 精确化为 \(a_3\)-quadratic (3.1)。
2. 该 quadratic 与旧 primitive tail quadratic 完全一致。
3. \(a_3\) 是 gap root \(t\) 的严格递减仿射函数。
4. gap Vieta conjugation 精确 lift 到 tail-root conjugation。
5. tail roots 和
   \[
   \Sigma_a=2TCG^2/[\kappa(\kappa+2G)].
   \]
6. top DD 强制 \(S\ge8\)。
7. top digit bounds 强制
   \[
   \Sigma_a/a_3<0.002.
   \]
8. conjugate third numerator
   \[
   a_3^\vee<0.
   \]
9. source gap root 是较小 Vieta root。
10. source factor 满足
    \[
    F_-<F_+.
    \]
11. 因而
    \[
    F_-=\Lambda D_0J^\sharp,
    \quad
    F_+=\Lambda D_0K^\sharp.
    \]
12. 所以
    \[
    \omega_{\rm src}=+1.
    \]
13. original positive-candidate involution 不存在。
14. oriented tail recovery
    \[
    2a_3=F_+/\kappa-F_-/(\kappa+2G).
    \]
15. source-labelled divisor allocation
    \[
    (\kappa+2G)/h\mid F_-,
    \quad
    \kappa/h\mid F_+.
    \]
16. \(\kappa/h\mid TQ\)，并可写 \(b_3=c(G/h)\)。
17. normalized factors
    \[
    uv=Nc^2,\quad v-u=2ha_3.
    \]
18. prefix slope lower bound
    \[
    A/Q>1/10.
    \]
19. top DD 新限制
    \[
    -1\le s_1+s_2\le2.
    \]
20. one-sided supply improvement
    \[
    J^\sharp\mid(Q^2N^2\mathscr T)^{\langle10\rangle}.
    \]

## DERIVED

1. orientation-odd quantity
   \[
   \Psi_{\rm ori}
   =
   \kappa(\kappa+2G)a_3-TCG^2.
   \]
2. normalized square
   \[
   h^2a_3^2+Nc^2=W_3^2.
   \]
   但它是旧 sphere gate 的重写，不是独立 gate。

## HEURISTIC

当前没有把任何 closing claim 标为 heuristic。

## COMPUTATIONAL EVIDENCE

符号展开曾用于发现/复核 (3.1)、(5.2) 与若干 normalized identities；最终证明均已人工化。

## FAILED

1. 仅靠 Hensel branch naming 选 orientation。
2. 仅靠 \(t^2<N\) 选 orientation。
3. 用 \(\mu-\nu\) sign 选 orientation。
4. 先追 conjugate \(G_0\) / gcd asymmetry。
5. 构造 original candidate involution。
6. 用 \(B_\kappa>Q\) 直接压死 \(J^\sharp\)。
7. 仅靠 \(A_\kappa,B_\kappa\) near-coprime 做 CRT。
8. 用 \(uv=Nc^2\) 的粗 factor spacing 直接闭合。
9. 把 normalized square (19.1) 当成独立新 gate。

## OPEN

仅剩：

\[
\boxed{
\textbf{DD Oriented Tail-Window Lemma (29.1).}
}
\]

---

# 31. 最终裁决

\[
\boxed{
\textbf{SGR-8B — ORIENTATION RECOVERY GATE}.
}
\]

orientation 的最终数学地位不是 gauge，也不是 original involution：

\[
\boxed{
\text{它是 algebraic Vieta branching，
但 original top-DD decimal recovery 唯一选择较小 Vieta root。}
}
\]

在 SGR-7 的符号约定下：

\[
\boxed{
\omega_{\rm src}=+1.
}
\]

共轭 orientation 仍是合法的正有理 gap root，却恢复出

\[
\boxed{
a_3^\vee<0,
}
\]

所以不是 primitive positive source root，更不是 original decimal candidate。

orientation 被解决后，本轮继续得到：

\[
\boxed{
\frac{\kappa+2G}{\gcd(\kappa,G)}
\to F_-\to J^\sharp,
}
\]

\[
\boxed{
\frac{\kappa}{\gcd(\kappa,G)}
\to F_+\to K^\sharp,
}
\]

以及新的 exact tail-recovery formula

\[
\boxed{
2a_3
=
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right).
}
\]

DD 尚未闭合，但 frontier 已再次缩成一个 scalar exact recovery window，而不再是 Hensel/source orientation 问题。
