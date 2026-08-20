# 三项十进制拼接平方和问题：Backward Strict Layer — A1 Residual 5-Phase × Actual Cut Synchronization Campaign

**文件名：** `strict_layer_backward_A1_5phase_cut_synchronization_campaign.md`  
**日期：** 2026-08-16  
**研究范围：** Strict Layer，仅研究 \(A_1\)-only 的 backward exact recovery；本轮集中于
\[
\boxed{\text{Residual }5\text{-Phase}\times\text{Actual Decimal Cut}}.
\]

**最终状态：**

\[
\boxed{\textbf{A1 PARTIAL-5 NOT CLOSED}}
\]

但本轮达成了预设的最低成功标准，而且把预设的 phase picture 作了一个关键修正：

\[
\boxed{
\textbf{normalized residual }5\textbf{-depth}
\Longrightarrow
\textbf{actual decimal-cut congruence}
}
\]

确实可以严格建立；然而真正穿透到 \(P=a_1 10^n+a_2\) 的，并不是裸的
\[
n_3-v_5(b_3),
\]
而是经完整 normalization-loss audit 后剩下的 **norm-excess depth**。

---

# 1. Executive summary

本轮最重要的结论可以压成六条。

## 1.1 NEW PROVED — word-visible determinant bridge

固定 A1 trace，沿上一轮 notation：

\[
\mathbf A=SP+a_3=EW,
\qquad
\mathbf B=SD+b_3=E\Gamma,
\]

\[
W=hu,\qquad
\Gamma=hv,\qquad
\gcd(u,v)=1,
\]

\[
\varepsilon:=vP-Du>0.
\]

定义真正读取 first-two word 的 determinant

\[
\boxed{
\Delta:=b_3P-a_3D.
}
\]

则有精确恒等式

\[
\boxed{
\Delta=Eh\,\varepsilon.
}
\tag{PC-1}
\]

证明只需：

\[
E(\Gamma P-DW)
=
\mathbf BP-D\mathbf A
=
b_3P-a_3D.
\]

而

\[
\Gamma P-DW=h(vP-Du)=h\varepsilon.
\]

这是本轮最关键的新 dictionary。它表明 normalized gap 与 actual cut 之间不是模糊的 valuation transfer，而有一个精确乘法桥。

---

## 1.2 NEW PROVED — partial \(5\)-saturation 下所有 normalization loss 可精确计算

令

\[
\boxed{
s:=v_5(b_3),
\qquad
0<s<n_3.
}
\]

写

\[
S=10^{n_3},
\qquad
\eta=\gcd(S,b_3),
\qquad
S=\eta\mathcal L,
\qquad
b_3=\eta\tau.
\]

则对任何真实 candidate：

\[
v_5(\eta)=s,
\qquad
v_5(\mathcal L)=n_3-s,
\qquad
v_5(\tau)=0.
\]

更强地，由 global word gcd prime-to-\(10\) 得

\[
v_5(E)=0.
\]

又因为

\[
\mathbf B=SD+b_3
\]

且

\[
v_5(SD)=n_3+v_5(D)>s,
\]

所以

\[
\boxed{
v_5(\mathbf B)=s.
}
\]

因此

\[
v_5(\Gamma)=s.
\]

而

\[
\Gamma=h\eta\bar v
\]

给出

\[
\boxed{
v_5(h)=0,
\qquad
v_5(\bar v)=0.
}
\]

由 \(\gcd(u,v)=1\) 且 \(5\mid v\)：

\[
\boxed{v_5(u)=0.}
\]

由 \(\gcd(a_3,b_3)=1\)：

\[
\boxed{v_5(a_3)=0.}
\]

故上一轮的

\[
c_a=\gcd(a_3,u),
\qquad
c_\tau=\gcd(\tau,\bar v)
\]

均为 \(5\)-adic units：

\[
\boxed{
v_5(c_a)=v_5(c_\tau)=0.
}
\]

这重新严格核验并加强了上一轮的 partial-saturation assertion。

---

## 1.3 NEW PROVED — raw residual phase 在回到 word determinant 时发生精确“尾尺度抵消”

令

\[
e:=v_5(\varepsilon).
\]

上一轮 normalized gap 为

\[
H_-:=\tau u-a_3\bar v
=
\mathcal L\varepsilon
=
c_ac_\tau Z_-.
\]

在 partial \(5\)-saturation 中：

\[
\boxed{
v_5(Z_-)=n_3-s+e,
\qquad
v_5(Z_+)=0.
}
\tag{PC-2}
\]

但把所有 scale 乘回去：

\[
Z_-
\to
H_-
\to
J_-:=\eta H_-
\to
K_-:=hJ_-
\to
b_3\mathbf A-a_3\mathbf B:=EK_-
\]

时，\(5\)-adic depth 依次是

\[
n_3-s+e,
\quad
n_3-s+e,
\quad
n_3+e,
\quad
n_3+e,
\quad
n_3+e.
\]

而

\[
b_3\mathbf A-a_3\mathbf B
=
S(b_3P-a_3D)
=
S\Delta.
\]

除以

\[
S=10^{n_3}
\]

后：

\[
\boxed{
v_5(\Delta)=e.
}
\tag{PC-3}
\]

所以：

\[
\boxed{
\textbf{forced residual depth }n_3-s
\textbf{ 本身没有一位净穿透到 }\Delta.
}
\]

它先与 \(\eta\) 合并重建完整 \(S\)-depth，随后又被从 raw word determinant 中除去的 \(S\) 精确吃掉。

因此本轮推翻了一个过强预期：

\[
\boxed{
n_3-s
\not\Rightarrow
\text{同样深度的 }P\text{-congruence}.
}
\]

真正 word-visible 的 depth 是

\[
\boxed{e=v_5(\varepsilon).}
\]

---

## 1.4 NEW PROVED — balance 精确计算这个额外 depth

定义

\[
\gamma:=v_5(G),
\qquad
\nu:=v_5(N),
\]

其中

\[
G=b_1b_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2.
\]

利用

\[
N\eta^2\bar v^2\tau^2
=
G^2H_-H_+
\]

和 partial-saturation unit dictionary，有：

\[
\nu+2s
=
2\gamma+(n_3-s+e).
\]

故：

\[
\boxed{
e
=
\nu+3s-2\gamma-n_3.
}
\tag{PC-4}
\]

这是 exact equality，不是 lower bound。

因此任何 partial-\(5\) candidate 必满足必要条件：

\[
\boxed{
\nu+3s\ge2\gamma+n_3.
}
\tag{PC-5}
\]

若右侧超过左侧，则该 trace/cut 立即死亡。

---

## 1.5 NEW PROVED — Phase-to-Cut Transfer Lemma

因为

\[
\Delta=b_3P-a_3D
\]

且

\[
v_5(\Delta)=e,
\]

写

\[
b_3=5^sb_3',
\qquad
5\nmid b_3'.
\]

若

\[
e>s,
\]

则必有

\[
v_5(D)\ge s.
\]

于是可除去 \(5^s\)，得到：

\[
b_3'P
\equiv
a_3\frac D{5^s}
\pmod{5^{e-s}}.
\]

由于 \(b_3'\) 为 \(5\)-adic unit：

\[
\boxed{
P
\equiv
a_3\frac D{5^s}(b_3')^{-1}
\pmod{5^{R_5}},
}
\tag{PC-6}
\]

其中真正的 cut-readable depth 为

\[
\boxed{
R_5
:=
e-s
=
\nu+2s-2\gamma-n_3
>0.
}
\tag{PC-7}
\]

若右式不正，则定义

\[
\boxed{
R_5^{\rm cut}
:=
\max\{0,\nu+2s-2\gamma-n_3\}.
}
\tag{PC-8}
\]

因此本轮第一次严格完成了：

\[
\boxed{
\textbf{residual algebraic phase}
\to
\textbf{actual word determinant}
\to
\textbf{actual decimal-cut congruence}.
}
\]

但 depth budget 的正确版本不是 \(n_3-s\)，而是 \(R_5^{\rm cut}\)。

---

## 1.6 OPEN — partial \(5\)-saturation 尚不能由 reducedness 单独关闭

得到 (PC-6) 后：

\[
P=a_1 10^n+a_2.
\]

对任意

\[
j\le n
\]

有

\[
P\equiv a_2\pmod{5^j}.
\]

因此：

\[
\boxed{
a_2
\equiv
a_3\frac D{5^s}(b_3')^{-1}
\pmod{5^j},
\qquad
j=\min(R_5^{\rm cut},n).
}
\tag{PC-9}
\]

若

\[
R_5^{\rm cut}>n,
\]

则超出 cut 的部分继续读取 \(a_1\)。

然而：

- 若 \(5\mid b_2\)，reducedness 给 \(5\nmid a_2\)，这并不自动与 (PC-9) 冲突；
- 实际上任何真实 candidate 若 \(5\mid b_2\) 且 \(R_5^{\rm cut}>0\)，必须自动进入 unit-target cancellation \(v_5(D)=s\)；
- 若 \(5\nmid b_2\)，reducedness 对 \(a_2\) 的 \(5\)-adic class 没有限制。

所以：

\[
\boxed{
\textbf{partial }5\textbf{-saturation 不能由 phase-to-cut + individual reducedness 直接统一关闭。}
}
\]

真正剩余的单一缺口已经变成：

\[
\boxed{
\textbf{Norm-Excess Cut Incompatibility}.
}
\]

也就是必须把 \(R_5^{\rm cut}\) 中的

\[
\nu=v_5(N)
\]

与同一个 actual cut 的 \(a_1,a_2\) 再同步一次。

---

# 2. Frozen backward A1 architecture

本轮冻结上一轮已经审计的 A1 exact state：

\[
\delta_3\le0,
\qquad
\delta_2+\delta_3>0.
\]

令

\[
g=m_3-n_3\ge0,
\]

\[
k_{12}=n_2-m_2-g\ge1.
\]

记 first-two cut depth：

\[
\boxed{
n:=n_2=m_2+g+k_{12}.
}
\tag{2.1}
\]

有效第三尾尺度：

\[
\boxed{
S=10^{n_3}.
}
\tag{2.2}
\]

固定 denominator-decimal trace：

\[
\boxed{
T=(b_1,b_2,b_3,S).
}
\]

于是：

\[
Q=b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\]

\[
D=10^gQ,
\]

\[
\mathbf B=SD+b_3.
\]

完整 numerator word：

\[
\boxed{
\mathbf A=SP+a_3,
\qquad
P=a_1 10^n+a_2.
}
\tag{2.3}
\]

令：

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\]

\[
\Gamma=\gcd(\mathbf B,\Lambda),
\]

\[
E=\mathbf B/\Gamma.
\]

已有 exact-balance forcing：

\[
\boxed{
E\mid\mathbf A.
}
\]

写：

\[
\mathbf A=EW,
\qquad
\mathbf B=E\Gamma.
\]

再写：

\[
h=\gcd(W,\Gamma),
\qquad
W=hu,
\qquad
\Gamma=hv,
\qquad
\gcd(u,v)=1.
\]

这些全部属于 **FROZEN**。

---

# 3. Anti-duplication boundary

当前 File Library 暴露的最新已完成 A1 正向报告为：

`strict_layer_A1_moving_core_decimal_translation_global_campaign.md`。

另有更新的 flat-locus campaign prompt，但本轮没有把一个未完成 prompt 当作 theorem source。

本报告不使用正向线中的：

- \(Q_0\to\infty\)；
- \(g=O(\log Q_0)\)；
- translation-line height argument；
- flat-locus elimination；
- moving-core termination；
- square-cubic moving geometry

来证明任何新 backward theorem。

本轮所有 NEW PROVED 都是 fixed candidate / fixed trace / actual word arithmetic。

同样，本轮没有迁移 DD 专属：

- source orientation；
- DD Hensel branch；
- double resonance；
- post-deflation quotient；
- DD near-\(S\)-unit；
- DD quotient overload。

---

# 4. Provenance / notation audit

本轮使用的主要来源如下。

## 4.1 `strict_layer_backward_A1_word_recovery_architecture_campaign.md`

冻结：

- exact quotient chart \((T,W,n)\)；
- \(E\mid\mathbf A\)；
- \(\gcd(E,10)=1\) on an admissible exact trace；
- BR-WGF；
- primitive oriented determinant；
- tail deflation；
- \(c_a,c_\tau,Z_\pm\)；
- partial decimal-prime allocation；
- detached-prefix pseudo-family。

## 4.2 `strict_layer_post_DD_consolidation_A1_frontier.md`

冻结：

- Strict frontier 只剩 A1；
- \(S=10^{n_3}\)；
- \(D=10^gQ\)；
- \(n=m_2+g+k_{12}\)；
- \(k_{12}\ge1\)。

## 4.3 `strict_layer_backward_exact_root_pair_fibre_campaign.md`

只使用：

- A1 one-word semantic collapse；
- actual cut 是 genuine residual bit；
- fixed word 下 cut fibre \(\le2\)。

## 4.4 `strict_layer_backward_denominator_decimal_interface.md`

只使用：

- \(T\simeq(b_1,b_2,b_3,S)\)；
- \((\eta,\mathcal L,\tau)\) 是 trace-derived；
- numerator information不能被 denominator trace 替代。

## 4.5 `strict_layer_backward_algebraic_denominator_interface.md`

只使用其 anti-false-gluing conclusion：

- algebraic compatibility 不自动等于 actual source realization。

## 4.6 `strict_layer_backward_canonical_synchronization_quotient.md`

只作为方法论边界：

- 不允许把丢失 actual witness 的 quotient 当成 lossless gluing。

## 4.7 `strict_layer_unified_exact_lift_campaign.md`

回查 A1 coefficient definitions：

\[
C=P,
\qquad
D=10^gQ.
\]

## 4.8 `exact_lift_research_synthesis_2026-08-10.md`

只作历史 provenance locator；不使用其中后来已撤回的 A1 closure。

---

# 5. Partial \(5\)-saturation chamber

本轮主 chamber：

\[
\boxed{
0<s:=v_5(b_3)<n_3.
}
\tag{5.1}
\]

由于：

\[
\gcd(a_3,b_3)=1,
\]

立即得到 source-level fact：

\[
\boxed{5\nmid a_3.}
\tag{5.2}
\]

令：

\[
\eta=\gcd(S,b_3),
\qquad
S=\eta\mathcal L,
\qquad
b_3=\eta\tau.
\]

则：

\[
\boxed{
v_5(\eta)=s,
\qquad
v_5(\mathcal L)=n_3-s,
\qquad
v_5(\tau)=0.
}
\tag{5.3}
\]

这是真正的 partial absorption：

- \(s\) 位 \(5\)-depth 被 \(b_3\) 吸收进 \(\eta\)；
- 剩余 \(n_3-s\) 位留在 \(\mathcal L\)。

---

# 6. Residual oriented \(5\)-phase

上一轮已证：

\[
b_3u-a_3v
=
S\varepsilon,
\qquad
\varepsilon=vP-Du>0.
\tag{6.1}
\]

又：

\[
v=\eta\bar v.
\]

因此：

\[
\boxed{
\tau u-a_3\bar v
=
\mathcal L\varepsilon.
}
\tag{6.2}
\]

定义：

\[
H_-:=\tau u-a_3\bar v,
\qquad
H_+:=\tau u+a_3\bar v.
\]

cross-content extraction：

\[
a_3=c_aa,
\quad
u=c_ax,
\]

\[
\tau=c_\tau b,
\quad
\bar v=c_\tau y,
\]

\[
Z_-=bx-ay,
\qquad
Z_+=bx+ay.
\]

并有：

\[
H_\pm=c_ac_\tau Z_\pm,
\qquad
\gcd(Z_-,Z_+)\mid2.
\tag{6.3}
\]

---

# 7. Normalization-loss audit

这是本轮最关键的 technical section。

## 7.1 \(E\) 不吸收任何 \(5\)-depth

已有 global word gcd theorem：

\[
\gcd(E,10)=1.
\]

因此：

\[
\boxed{v_5(E)=0.}
\tag{7.1}
\]

## 7.2 \(\mathbf B\) 的 \(5\)-depth 精确等于 \(s\)

因为：

\[
\mathbf B=SD+b_3,
\]

而：

\[
v_5(SD)=n_3+v_5(D)>s=v_5(b_3),
\]

两项 valuation 不同，无 cancellation。

故：

\[
\boxed{
v_5(\mathbf B)=s.
}
\tag{7.2}
\]

由：

\[
\mathbf B=E\Gamma
\]

与 (7.1)：

\[
\boxed{
v_5(\Gamma)=s.
}
\tag{7.3}
\]

## 7.3 \(h,\bar v,u\) 全部是 \(5\)-units

由：

\[
\Gamma=hv=h\eta\bar v
\]

和：

\[
v_5(\Gamma)=v_5(\eta)=s
\]

可得：

\[
\boxed{
v_5(h)=v_5(\bar v)=0.
}
\tag{7.4}
\]

又：

\[
5\mid v,
\qquad
\gcd(u,v)=1,
\]

所以：

\[
\boxed{
v_5(u)=0.
}
\tag{7.5}
\]

结合 \(5\nmid a_3,\tau,\bar v\)：

\[
\boxed{
v_5(c_a)=v_5(c_\tau)=0.
}
\tag{7.6}
\]

这证明上一轮的 \(v_5(c_a)=0\) 没有隐藏额外假设；它只使用：

- partial saturation；
- third-block reducedness；
- primitive slope gcd；
- admissible word trace 的 \(E\)-unit theorem。

## 7.4 \(Z_-\) 与 \(Z_+\) 的精确 valuation

令：

\[
e:=v_5(\varepsilon).
\]

由：

\[
c_ac_\tau Z_-=\mathcal L\varepsilon
\]

和 (7.6)：

\[
\boxed{
v_5(Z_-)=n_3-s+e.
}
\tag{7.7}
\]

又因为 \(n_3-s\ge1\)：

\[
\tau u\equiv a_3\bar v\pmod5.
\]

两边均为 units，于是：

\[
H_+
=
\tau u+a_3\bar v
\equiv
2\tau u
\not\equiv0
\pmod5.
\]

故：

\[
\boxed{
v_5(Z_+)=v_5(H_+)=0.
}
\tag{7.8}
\]

所以 directional allocation 在 partial \(5\)-saturation 中是 exact 的。

---

# 8. \(Z_-\to\Delta\to P\) transfer

## 8.1 Word-visible determinant

定义：

\[
\boxed{
\Delta:=b_3P-a_3D.
}
\tag{8.1}
\]

从 word identities：

\[
\mathbf A=SP+a_3,
\qquad
\mathbf B=SD+b_3
\]

得到：

\[
\mathbf BP-D\mathbf A
=
b_3P-a_3D
=
\Delta.
\tag{8.2}
\]

另一方面：

\[
\mathbf BP-D\mathbf A
=
E(\Gamma P-DW).
\]

而：

\[
\Gamma P-DW
=
h(vP-Du)
=
h\varepsilon.
\]

所以：

\[
\boxed{
\Delta=Eh\varepsilon.
}
\tag{8.3}
\]

由于 \(E,h\) 均为 \(5\)-units：

\[
\boxed{
v_5(\Delta)=e.
}
\tag{8.4}
\]

这是 exact equality。

## 8.2 完整 transfer chain

将用户要求的每一步显式列出：

\[
Z_-
\longrightarrow
H_-
\longrightarrow
J_-
\longrightarrow
K_-
\longrightarrow
b_3\mathbf A-a_3\mathbf B
\longrightarrow
\Delta
\longrightarrow
P.
\]

其中：

\[
H_-=c_ac_\tau Z_-,
\]

\[
J_-=\eta H_-=b_3u-a_3v,
\]

\[
K_-=hJ_-=b_3W-a_3\Gamma,
\]

\[
b_3\mathbf A-a_3\mathbf B
=
EK_-,
\]

\[
b_3\mathbf A-a_3\mathbf B=S\Delta.
\]

valuation ledger：

| level | exact object | \(v_5\) |
|---|---|---:|
| cross-normalized | \(Z_-\) | \(n_3-s+e\) |
| tail-deflated | \(H_-\) | \(n_3-s+e\) |
| reinsert \(\eta\) | \(J_-\) | \(n_3+e\) |
| reinsert \(h\) | \(K_-\) | \(n_3+e\) |
| reinsert \(E\) | \(b_3\mathbf A-a_3\mathbf B\) | \(n_3+e\) |
| divide actual tail \(S\) | \(\Delta=b_3P-a_3D\) | \(e\) |
| solve coefficient \(b_3\) | \(P\)-residue | \((e-s)_+\) |

因此：

\[
\boxed{
\textbf{normalization loss}
=
(n_3-s)+s=n_3
}
\]

恰好等于真实 tail scale \(S\) 的 \(5\)-depth。

---

# 9. Canonical \(5\)-depth budget

本轮建议以后固定三层 depth，不再把它们混写。

## 9.1 Normalized phase depth

\[
\boxed{
R_5^{\rm norm}
:=
v_5(Z_-)
=
n_3-s+e.
}
\tag{9.1}
\]

## 9.2 Word-determinant depth

\[
\boxed{
R_5^{\rm word}
:=
v_5(\Delta)
=
e.
}
\tag{9.2}
\]

## 9.3 Cut-readable depth

只有超过 \(b_3\) coefficient 自身的 \(5^s\) 后，才真正能解出 \(P\) 的 residue：

\[
\boxed{
R_5^{\rm cut}
:=
\max(0,e-s).
}
\tag{9.3}
\]

这三个 depth 的区别是本轮的核心修正。

裸 residual tail depth

\[
n_3-s
\]

不应再称为“到达 cut 的 phase depth”。

---

# 10. Deep cancellation analysis

令：

\[
d:=v_5(D),
\qquad
p:=v_5(P).
\]

写：

\[
b_3=5^sb_3',
\qquad
D=5^dD',
\]

其中：

\[
5\nmid b_3'D'.
\]

则：

\[
\Delta
=
5^sb_3'P
-
a_3 5^dD'.
\tag{10.1}
\]

两项 valuation 分别为：

\[
s+p,
\qquad
d.
\]

## 10.1 Generic no-cancellation regime

若：

\[
s+p\ne d,
\]

则：

\[
\boxed{
e
=
\min(s+p,d).
}
\tag{10.2}
\]

这是 exact equality。

此时没有 higher phase；\(\Delta\) 的 valuation 完全由较浅一项决定。

## 10.2 Forced-cancellation regime

若：

\[
e>\min(s+p,d),
\]

则必有：

\[
\boxed{
s+p=d.
}
\tag{10.3}
\]

定义 unit-cancellation surplus：

\[
\boxed{
\chi_5:=e-d>0.
}
\tag{10.4}
\]

则：

\[
b_3'\frac P{5^p}
\equiv
a_3D'
\pmod{5^{\chi_5}},
\]

即：

\[
\boxed{
\frac P{5^p}
\equiv
a_3D'(b_3')^{-1}
\pmod{5^{\chi_5}}.
}
\tag{10.5}
\]

这是比普通 \(P\bmod5^{R_5}\) 更精确的 **unit-phase lock**。

因此本轮建议区分：

\[
\boxed{
R_5^{\rm cut}=(e-s)_+
}
\]

与：

\[
\boxed{
R_5^{\rm unit}=(e-d)_+.
}
\]

前者读取 \(P\) 的 residue；后者读取 \(P\) 去掉强制 \(5^p\) 后的 unit digits。

---

# 11. Phase-to-Cut Transfer Lemma

## Theorem A1-PC1 — Partial-5 Exact Phase–Cut Synchronization

**状态：NEW PROVED.**

设一个完整 A1 candidate 满足：

\[
0<s=v_5(b_3)<n_3.
\]

令：

\[
\gamma=v_5(G),
\qquad
\nu=v_5(N).
\]

则：

\[
\boxed{
v_5(b_3P-a_3D)
=
\nu+3s-2\gamma-n_3.
}
\tag{11.1}
\]

特别：

\[
\boxed{
\nu+3s\ge2\gamma+n_3.
}
\tag{11.2}
\]

若定义：

\[
\boxed{
R_5
=
\nu+2s-2\gamma-n_3,
}
\tag{11.3}
\]

则：

### (i) \(R_5\le0\)

当前 residual phase 不产生任何非平凡 \(P\)-congruence。

### (ii) \(R_5>0\)

必有：

\[
v_5(D)\ge s,
\]

并且：

\[
\boxed{
P
\equiv
C_5(T,a_3)
\pmod{5^{R_5}},
}
\tag{11.4}
\]

其中：

\[
\boxed{
C_5(T,a_3)
:=
a_3\frac D{5^s}
\left(\frac{b_3}{5^s}\right)^{-1}
\in\mathbf Z_5.
}
\tag{11.5}
\]

这里 inverse 取 \(5\)-adic unit inverse；在模 \(5^{R_5}\) 下是唯一的。

---

# 12. Actual suffix \(a_2\) extraction

真实 cut：

\[
P=a_1 10^n+a_2.
\]

因为：

\[
10^n=2^n5^n,
\]

有：

\[
\boxed{
P\equiv a_2\pmod{5^n}.
}
\tag{12.1}
\]

故若 \(R_5>0\)，令：

\[
j:=\min(R_5,n),
\]

则：

\[
\boxed{
a_2
\equiv
C_5(T,a_3)
\pmod{5^j}.
}
\tag{12.2}
\]

这是真正的 block-level congruence。

但必须强调：

\[
\boxed{
a_2\bmod5^j
\text{ 并不等于锁死 }a_2\text{ 的十进制末 }j\text{ 位。}
}
\]

尤其即使 \(j=n\)，一个 \(n\)-digit decimal interval 仍大约含

\[
\frac{9\cdot10^{n-1}}{5^n}
\asymp
2^n
\]

个同一 \(5^n\)-residue 的可能整数。

所以单独 \(5\)-phase 仍保留指数级 decimal representatives；真正的 decimal suffix 需要同步 \(2\)-adic information。

---

# 13. Beyond-cut-depth extraction of \(a_1\)

若：

\[
R_5>n,
\]

不能继续把 \(P\) 替换成 \(a_2\)。

取 \(C_R\) 为：

\[
C_5(T,a_3)\pmod{5^{R_5}}
\]

的任一 canonical residue representative，使：

\[
P\equiv C_R\pmod{5^{R_5}}.
\]

由：

\[
P-a_2=5^n2^na_1,
\]

并且：

\[
C_R\equiv a_2\pmod{5^n},
\]

可除 \(5^n\) 得：

\[
\boxed{
2^na_1
\equiv
\frac{C_R-a_2}{5^n}
\pmod{5^{R_5-n}}.
}
\tag{13.1}
\]

由于 \(2^n\) 为 \(5\)-unit：

\[
\boxed{
a_1
\equiv
2^{-n}
\frac{C_R-a_2}{5^n}
\pmod{5^{R_5-n}}.
}
\tag{13.2}
\]

因此 prompt 所设想的两阶段读取严格成立，但需作一个修正：

- Stage 1：只锁 \(a_2\) 的 \(5\)-adic residue；
- Stage 2：超过 \(n\) 后，新增 depth 才开始读取 \(a_1\)。

---

# 14. Interaction with \(k_{12}\ge1\)

\[
n=m_2+g+k_{12}.
\]

本轮得到的 cut depth：

\[
R_5
=
\nu+2s-2\gamma-n_3
\]

中没有显式 \(k_{12}\)。

因此：

\[
\boxed{
k_{12}\ge1
\text{ 并不会自动增加 }R_5.
}
\tag{14.1}
\]

相反，它增大：

\[
n,
\]

所以把 phase 穿透到 \(a_1\) 所需的阈值：

\[
R_5>n
\]

会更难达到。

因此对 Q4 的第一答案是：

\[
\boxed{
\textbf{strict excess }k_{12}\ge1
\textbf{ 不直接增强 }5\textbf{-adic penetration。}
}
\]

不过有一个有用的条件性作用。

若：

\[
v_5(Q)\le m_2,
\]

则：

\[
d=v_5(D)=g+v_5(Q)\le g+m_2=n-k_{12}<n.
\]

所以在 deep forced-cancellation regime：

\[
e>d,
\qquad
p=d-s,
\]

自动有：

\[
p<n.
\]

于是：

\[
v_5(P)=v_5(a_2)=p,
\]

且 unit-phase congruence (10.5) 真正落在 \(a_2\) 上，而不会跨过 cut 混入 \(a_1\)。

因此：

\[
\boxed{
v_5(Q)\le m_2
\quad+\quad
k_{12}\ge1
}
\]

提供一个 one-cut-margin localization。

**状态：DERIVED / CONDITIONAL.**

若：

\[
v_5(Q)>m_2,
\]

这本身代表 prefix denominator word \(Q=b_1 10^{m_2}+b_2\) 发生了独立高阶 \(5\)-adic cancellation；该 denominator-resonant escape 不能在本轮无证明删除。

---

# 15. Reducedness collision analysis

记：

\[
r_1:=v_5(b_1),
\qquad
r_2:=v_5(b_2).
\]

逐块既约性给：

\[
r_1>0\Longrightarrow v_5(a_1)=0,
\]

\[
r_2>0\Longrightarrow v_5(a_2)=0.
\]

partial tail 已给：

\[
s>0\Longrightarrow v_5(a_3)=0.
\]

## 15.1 若 \(5\mid b_2\)

则：

\[
5\nmid a_2.
\]

因为 \(n\ge1\)：

\[
P\equiv a_2\pmod5,
\]

故：

\[
\boxed{v_5(P)=0.}
\]

如果：

\[
R_5>0,
\]

则：

\[
e>s.
\]

此时 \(\Delta\) 两项必须发生高阶 cancellation，因此：

\[
\boxed{
v_5(D)=s.
}
\tag{15.1}
\]

而 target：

\[
C_5(T,a_3)
=
a_3\frac D{5^s}(b_3')^{-1}
\]

是 \(5\)-unit。

所以 transferred residue 自动满足：

\[
5\nmid a_2.
\]

结论：

\[
\boxed{
5\mid b_2
\text{ 并不会与 Phase-to-Cut congruence 自动冲突。}
}
\]

reducedness 只是迫使 deep transfer 进入 unit-target branch。

## 15.2 若 \(5\nmid b_2\)

reducedness 对 \(a_2\) 的 \(5\)-adic valuation没有限制。

所以即使 transfer 强迫：

\[
5^j\mid a_2,
\]

也没有直接 contradiction。

## 15.3 \(a_1\) side

即使：

\[
R_5>n
\]

而得到 \(a_1\) 的 residue class，也没有从当前公式推出：

\[
5\mid b_1
\Longrightarrow
5\mid a_1.
\]

相反，一个真实 candidate 会自动选择与 reducedness 兼容的 unit class，除非再使用 norm / trace 的更深 relation。

因此：

\[
\boxed{
\textbf{individual reducedness alone does not close partial }5\textbf{-saturation.}
}
\]

---

# 16. Denominator \(5\)-support cases

这一节把：

\[
\nu=v_5(N)
\]

尽可能压成 denominator support。

令：

\[
\alpha_i:=v_5(a_i).
\]

则：

\[
v_5(a_1b_2)=\alpha_1+r_2,
\]

\[
v_5(a_2b_1)=\alpha_2+r_1.
\]

记：

\[
x:=\alpha_1+r_2,
\qquad
y:=\alpha_2+r_1.
\]

若：

\[
x\ne y,
\]

则 sum-of-two-squares 的两项 valuation 不同：

\[
\boxed{
\nu=2\min(x,y).
}
\tag{16.1}
\]

若：

\[
x=y=t,
\]

则：

\[
\boxed{
\nu=2t+\lambda_N,
}
\tag{16.2}
\]

其中：

\[
\lambda_N
=
v_5(X_0^2+Y_0^2)\ge0
\]

是 normalized unit-sum phase；由于 \(-1\) 在 \(\mathbf F_5\) 中为平方，\(\lambda_N\) 不存在 uniform small bound。

## 16.1 Exactly one prefix denominator contains \(5\)

若：

\[
r_1>0,\ r_2=0
\]

或：

\[
r_1=0,\ r_2>0,
\]

reducedness 使一个 weighted square term成为 \(5\)-unit，因此：

\[
\boxed{\nu=0.}
\]

令：

\[
r=\max(r_1,r_2).
\]

则：

\[
\boxed{
e=3s-2r-n_3,
}
\tag{16.3}
\]

\[
\boxed{
R_5=2s-2r-n_3.
}
\tag{16.4}
\]

所以 candidate 必须满足：

\[
\boxed{
3s\ge n_3+2r.
}
\tag{16.5}
\]

而要真正读出 \(P\)：

\[
\boxed{
2s>n_3+2r.
}
\tag{16.6}
\]

## 16.2 Both prefix denominators contain \(5\), unequal depths

若：

\[
r_1,r_2>0,
\qquad
r_1\ne r_2,
\]

则：

\[
\nu=2\min(r_1,r_2).
\]

令：

\[
r_{\max}=\max(r_1,r_2).
\]

仍得到完全相同的 canonical formula：

\[
\boxed{
e=3s-2r_{\max}-n_3,
}
\tag{16.7}
\]

\[
\boxed{
R_5=2s-2r_{\max}-n_3.
}
\tag{16.8}
\]

所以在这些 nonresonant denominator-support cases 中，phase depth完全由 trace 决定。

## 16.3 Equal positive prefix support

若：

\[
r_1=r_2=r>0,
\]

reducedness 给：

\[
\alpha_1=\alpha_2=0.
\]

于是：

\[
\nu=2r+\lambda_N.
\]

因此：

\[
\boxed{
e=\lambda_N+3s-2r-n_3,
}
\tag{16.9}
\]

\[
\boxed{
R_5=\lambda_N+2s-2r-n_3.
}
\tag{16.10}
\]

这里真正的 escape 是：

\[
\boxed{\lambda_N}
\]

——即 prefix norm 自身的 \(5\)-adic unit cancellation。

## 16.4 Neither prefix denominator contains \(5\)

若：

\[
r_1=r_2=0,
\]

则：

\[
\boxed{
e=\nu+3s-n_3,
}
\tag{16.11}
\]

\[
\boxed{
R_5=\nu+2s-n_3.
}
\tag{16.12}
\]

此时全部额外 phase 都来自 actual numerator norm \(N\)。

---

# 17. Optional \(2\)-adic synchronization

本轮没有重新开启一条独立 \(2\)-adic campaign。

但 determinant bridge：

\[
\Delta=Eh\varepsilon
\]

本身对任意 prime 成立。

若未来独立得到：

\[
P\equiv C_2\pmod{2^{R_2}}
\]

和本轮：

\[
P\equiv C_5\pmod{5^{R_5}},
\]

则 CRT 自动得到：

\[
\boxed{
P\bmod10^j,
\qquad
j\le\min(R_2,R_5).
}
\]

这才是真正的 decimal suffix。

当前不能无条件给出 \(R_2\)，原因是 normalized plus/minus pair 在 \(p=2\) 允许共享一个 factor \(2\)，不能直接复用：

\[
v_5(Z_+)=0
\]

的单侧分配。

**状态：OPEN / NOT ACTIVATED.**

---

# 18. Norm re-entry is necessary

本轮得到一个非常明确的逻辑结论：

\[
\boxed{
\text{phase}\to\text{cut}
\]

可以完成；

但：

\[
\boxed{
\text{cut congruence}+\text{reducedness}
\]

仍不足。

真正决定 \(R_5\) 的是：

\[
\nu=v_5(N).
\]

而：

\[
N=(a_1b_2)^2+(a_2b_1)^2
\]

本身读取 actual cut。

因此下一步正确顺序是：

\[
\boxed{
\text{phase}
\to
\text{actual cut}
\to
\text{actual norm}
}
\]

与 prompt 设定完全一致。

最重要的是：norm 不是为了重新做 generic Gaussian representation count，而是为了控制同一个 actual cut 所产生的：

\[
\boxed{
\nu=v_5(N)
}
\]

以及它反馈回：

\[
R_5.
\]

这是一个 closed feedback loop：

\[
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
(a_1,a_2).
\]

本轮认为这才是 partial-\(5\) 真正剩余的 terminal mechanism。

---

# 19. Computational falsification

计算只用于检查公式和寻找 counterexample，不用于证明 nonexistence。

## 19.1 Identity checks

对小参数 synthetic states 检查了：

\[
\Delta=b_3P-a_3D
=
Eh\varepsilon
\]

及：

\[
v_5(\Delta)=e
\]

的代数一致性。

由于这些式子已在第 8 节直接符号证明，计算不进入 theorem dependency。

## 19.2 Deep phase-to-cut congruence 可以与 WORD+CUT+RED 无限兼容

下一节给出一个完全符号化的无限 pseudo-family；计算曾用于先发现其结构，最终证明不依赖搜索。

---

# 20. Infinite pseudo-family / counterexample

本轮构造一个比上一轮 detached-prefix family 更贴近当前 target 的反例。

它保留：

- actual WORD；
- actual legal CUT；
- individual RED；
- partial \(5\)-saturation；
- 任意深的 word-visible determinant cancellation；
- 任意深的 actual \(P\)-congruence；

但故意不满足 norm / BR-WGF。

因此它严格证明：

\[
\boxed{
\text{Phase-to-Cut congruence}
+
\text{WORD}
+
\text{CUT}
+
\text{RED}
}
\]

仍不能闭合 A1。

## 20.1 Family

固定：

\[
b_1=1,
\qquad
b_2=5,
\qquad
b_3=15.
\]

于是：

\[
m_2=1,
\qquad
m_3=2.
\]

取：

\[
n_3=2,
\qquad
g=0,
\qquad
S=100.
\]

故：

\[
s=v_5(b_3)=1<n_3=2.
\]

并有：

\[
Q=1\cdot10+5=15,
\qquad
D=15,
\qquad
G=5.
\]

完整 denominator word：

\[
\mathbf B=100\cdot15+15=1515.
\]

\[
\Lambda=15,
\qquad
\Gamma=15,
\qquad
E=101.
\]

取 legal cut：

\[
n=2.
\]

则：

\[
k_{12}=n-m_2-g=1.
\]

对任意：

\[
\chi\ge2,
\]

令：

\[
\boxed{
a_1=101\cdot5^{\chi-2},
\qquad
a_2=11,
\qquad
a_3=11.
}
\tag{20.1}
\]

于是：

\[
P=100a_1+11
=
11+404\cdot5^\chi.
\tag{20.2}
\]

完整 numerator word：

\[
\mathbf A=100P+11
=
101(11+400\cdot5^\chi).
\]

所以：

\[
E\mid\mathbf A,
\]

且：

\[
W=11+400\cdot5^\chi.
\]

逐块 reducedness：

\[
\gcd(a_1,1)=1,
\]

\[
\gcd(11,5)=1,
\]

\[
\gcd(11,15)=1.
\]

全部成立。

## 20.2 Arbitrarily deep actual cut cancellation

\[
\Delta
=
15P-11\cdot15
=
15(P-11)
=
15\cdot404\cdot5^\chi.
\]

故：

\[
\boxed{
v_5(\Delta)=\chi+1.
}
\]

而：

\[
s=1.
\]

所以：

\[
\boxed{
R_5^{\rm cut}
=
\chi.
}
\]

并且：

\[
\boxed{
P\equiv11\pmod{5^\chi},
}
\]

但：

\[
P\not\equiv11\pmod{5^{\chi+1}}.
\]

因此 actual cut congruence 可以任意深。

## 20.3 Norm 永远失败

这里：

\[
N
=
(5a_1)^2+11^2.
\]

因此：

\[
N\equiv1\pmod5.
\]

BR-WGF 在本 trace 中化简为：

\[
9N=W^2-121.
\]

但：

\[
W\equiv11\pmod5,
\]

所以：

\[
W^2-121\equiv0\pmod5.
\]

而：

\[
9N\equiv4\pmod5.
\]

矛盾。

故对所有：

\[
\chi\ge2
\]

均有：

\[
\boxed{\text{BR-WGF fails}.}
\]

所以这是一个严格的 infinite pseudo-family。

**状态：NEW PROVED NEGATIVE THEOREM.**

它说明：

\[
\boxed{
\textbf{即便 actual cut 已被 arbitrarily deep }5\textbf{-phase 锁定，}
\textbf{只要不重新接入 norm，仍然存在无限逃逸。}
}
\]

---

# 21. Partial-saturation closure attempt

当前 partial-\(5\) chamber 可以按：

\[
e
=
\nu+3s-2\gamma-n_3
\]

分成四个 canonical regimes。

## Regime A — valuation deficit

若：

\[
\nu+3s<2\gamma+n_3,
\]

则：

\[
e<0,
\]

不可能。

因此：

\[
\boxed{\text{CLOSED.}}
\]

## Regime B — normalized phase survives, but cut is invisible

若：

\[
0\le e\le s,
\]

则 normalized \(Z_-\) 仍含：

\[
n_3-s
\]

的 forced depth，但：

\[
R_5^{\rm cut}=0.
\]

所以 actual \(P\) 没有非平凡 forced residue。

**状态：OPEN escape regime.**

这精确对应 prompt 的 Failure II：

\[
\boxed{
\text{normalization loss eats all cut-visible phase.}
}
\]

## Regime C — cut-visible phase

若：

\[
e>s,
\]

则：

\[
P\equiv C_5(T,a_3)\pmod{5^{e-s}}.
\]

**状态：NEW PROVED transfer, but not closed.**

## Regime D — deep unit cancellation

若进一步：

\[
e>d=v_5(D),
\]

则：

\[
s+v_5(P)=d
\]

并有 unit lock：

\[
\frac P{5^{d-s}}
\equiv
a_3D'(b_3')^{-1}
\pmod{5^{e-d}}.
\]

这是最强 phase chamber。

但当前仍缺：

\[
\boxed{
\text{unit lock}
+
\text{same-cut norm}
\Longrightarrow\bot.
}
\]

---

# 22. Full-absorption escape audit

若：

\[
v_5(b_3)\ge n_3,
\]

则：

\[
v_5(\eta)=n_3,
\qquad
v_5(\mathcal L)=0.
\]

所以：

\[
H_-=\mathcal L\varepsilon
\]

中不再有任何 forced residual \(5\)-modulus。

特别 saturated：

\[
S\mid b_3
\]

时：

\[
\mathcal L
\]

在 \(5\)-adic side 是 unit；若 full \(10\)-saturation 则甚至：

\[
\mathcal L=1.
\]

因此本轮 partial mechanism 失效的原因非常准确：

\[
\boxed{
\textbf{不是 congruence 推不动，}
\textbf{而是 residual phase source 本身已经消失。}
}
\]

记录为：

\[
\boxed{
\textbf{Full-Absorption Escape Chamber}.
}
\]

本轮不强行对其制造 \(5\)-adic contradiction。

---

# 23. Strongest new theorem

本轮建议把最强结果正式命名为：

## A1 Partial-5 Phase–Cut Synchronization Theorem

**状态：NEW PROVED.**

设一个完整 A1 candidate 满足：

\[
0<s=v_5(b_3)<n_3.
\]

定义：

\[
\gamma=v_5(b_1b_2),
\]

\[
\nu
=
v_5\!\left(
(a_1b_2)^2+(a_2b_1)^2
\right).
\]

则：

\[
\boxed{
v_5(b_3P-a_3D)
=
\nu+3s-2\gamma-n_3.
}
\tag{23.1}
\]

因此必要地：

\[
\boxed{
\nu+3s\ge2\gamma+n_3.
}
\tag{23.2}
\]

令：

\[
\boxed{
R_5
=
\nu+2s-2\gamma-n_3.
}
\tag{23.3}
\]

若：

\[
R_5>0,
\]

则：

\[
\boxed{
P
\equiv
a_3
\frac D{5^s}
\left(\frac{b_3}{5^s}\right)^{-1}
\pmod{5^{R_5}}.
}
\tag{23.4}
\]

进而：

\[
\boxed{
a_2
\equiv
a_3
\frac D{5^s}
\left(\frac{b_3}{5^s}\right)^{-1}
\pmod{5^{\min(R_5,n)}}.
}
\tag{23.5}
\]

若：

\[
R_5>n,
\]

则剩余：

\[
R_5-n
\]

位继续给出 \(a_1\) 的 \(5\)-adic congruence。

---

# 24. Exact remaining obligation

本轮之后，不应再把下一目标写成泛泛的：

\[
\text{“把 }5\text{-phase 传到 cut”.}
\]

这一步已经完成。

真正剩余的最小 theorem 是：

## A1 Partial-5 Norm-Excess Cut Obstruction

\[
\boxed{\textbf{OPEN.}}
\]

建议精确陈述：

> 固定一个 A1 partial-\(5\) denominator trace
> \[
> 0<v_5(b_3)<n_3.
> \]
> 对任意 legal actual cut
> \[
> P=a_1 10^n+a_2,
> \qquad
> n=m_2+g+k_{12},
> \quad
> k_{12}\ge1,
> \]
> 若 individual reducedness 成立，并令
> \[
> N=(a_1b_2)^2+(a_2b_1)^2,
> \]
> 则证明由
> \[
> R_5
> =
> v_5(N)+2v_5(b_3)-2v_5(G)-n_3
> \]
> 所产生的 Phase-to-Cut residue
> \[
> P\equiv C_5(T,a_3)\pmod{5^{R_5}}
> \]
> 与同一个 cut 的 exact norm realization 不可同时发生。

这比上一轮 A1-CGS 更小，因为它已经只剩：

\[
\boxed{
\text{actual cut}
+
\text{one norm valuation/phase feedback}
+
\text{one explicit }5\text{-adic target}.
}
\]

---

# 25. Q1–Q7 answers

## Q1 — 真正可传递到 word level 的 residual \(5\)-depth 是多少？

必须区分三层：

\[
\boxed{
R_5^{\rm norm}
=
n_3-s+e,
}
\]

\[
\boxed{
R_5^{\rm word}
=
e
=
\nu+3s-2\gamma-n_3,
}
\]

\[
\boxed{
R_5^{\rm cut}
=
\max(0,e-s)
=
\max(0,\nu+2s-2\gamma-n_3).
}
\]

真正到达 \(P\) 的是最后一个。

裸 residual：

\[
n_3-s
\]

本身净传递为 \(0\)。

---

## Q2 — 能否得到 canonical \(P\bmod5^R\) congruence？

\[
\boxed{\textbf{YES, if }R_5^{\rm cut}>0.}
\]

精确为：

\[
\boxed{
P
\equiv
a_3
\frac D{5^s}
\left(\frac{b_3}{5^s}\right)^{-1}
\pmod{5^{R_5^{\rm cut}}}.
}
\]

若：

\[
R_5^{\rm cut}=0,
\]

则当前 phase 不给任何非平凡 \(P\)-residue。

---

## Q3 — 能否进一步得到 \(a_2\) 或 \(a_1\) congruence？

\[
\boxed{\textbf{YES.}}
\]

\[
a_2
\equiv
C_5(T,a_3)
\pmod{5^{\min(R_5^{\rm cut},n)}}.
\]

若：

\[
R_5^{\rm cut}>n,
\]

则超出的：

\[
R_5^{\rm cut}-n
\]

位继续读取 \(a_1\)。

---

## Q4 — \(k_{12}\ge1\) 是否真正增强 phase penetration？

\[
\boxed{\textbf{NO, not directly.}}
\]

\(R_5^{\rm cut}\) 没有显式 \(k_{12}\)。

增加 \(k_{12}\) 反而增大 cut depth \(n\)，使进入 \(a_1\) 更难。

但在条件：

\[
v_5(Q)\le m_2
\]

下，\(k_{12}\ge1\) 确保 \(v_5(D)<n\)，从而 deep unit phase 被定位在 lower block \(a_2\)。

---

## Q5 — individual reducedness 能否直接制造 contradiction？

\[
\boxed{\textbf{NO, not uniformly.}}
\]

尤其：

\[
5\mid b_2
\]

时，reducedness 使 \(P\) 为 unit；任何非平凡 deep transfer 会自动迫使：

\[
v_5(D)=s,
\]

从而 target 也是 unit，并不矛盾。

---

## Q6 — partial \(5\)-saturation chamber 能否完整关闭？

\[
\boxed{\textbf{NO, not in this round.}}
\]

已关闭 valuation-deficit subchamber：

\[
\nu+3s<2\gamma+n_3.
\]

但：

- \(0\le e\le s\) 有 phase-annihilation escape；
- \(e>s\) 虽然得到 actual cut congruence，但 infinite pseudo-family 证明 congruence + WORD + CUT + RED 仍不足；
- 必须重新接入 same-cut norm。

---

## Q7 — 如果不能关闭，最小缺口是什么？

\[
\boxed{
\textbf{A1 Partial-5 Norm-Excess Cut Obstruction}.
}
\]

不是继续做 phase transfer；phase transfer 已经完成。

---

# 26. PROVED / FAILED / OPEN ledger

## FROZEN

- Strict frontier = A1-only；
- \(S=10^{n_3}\)；
- \(D=10^gQ\)；
- \(n=m_2+g+k_{12}\), \(k_{12}\ge1\)；
- \(\mathbf A=SP+a_3\)；
- \(\mathbf B=SD+b_3\)；
- \(E=\mathbf B/\Gamma\mid\mathbf A\)；
- \(\gcd(E,10)=1\) for admissible exact traces；
- \(W=hu,\Gamma=hv\)；
- primitive oriented gap；
- tail deflation；
- cross-content gap pair；
- BR-WGF；
- detached-prefix anti-waste theorem。

## NEW PROVED

1. exact word-visible determinant:
   \[
   \Delta=Eh\varepsilon;
   \]

2. partial-\(5\) unit dictionary:
   \[
   v_5(E)=v_5(h)=v_5(u)=v_5(\bar v)
   =v_5(\tau)=v_5(c_a)=v_5(c_\tau)=0;
   \]

3. exact:
   \[
   v_5(Z_-)=n_3-s+e,\qquad v_5(Z_+)=0;
   \]

4. phase annihilation:
   \[
   v_5(\Delta)=e;
   \]

5. norm-excess identity:
   \[
   e=\nu+3s-2\gamma-n_3;
   \]

6. Phase-to-Cut Transfer Lemma:
   \[
   R_5^{\rm cut}
   =
   \max(0,\nu+2s-2\gamma-n_3);
   \]

7. actual \(P\), \(a_2\), and beyond-cut \(a_1\) congruences;

8. no-cancellation / forced-cancellation dichotomy;

9. denominator-support simplification of \(\nu\) in nonresonant cases;

10. infinite WORD+CUT+RED+deep-phase pseudo-family showing norm is necessary.

## DERIVED

- if \(5\mid b_2\) and \(R_5^{\rm cut}>0\), then
  \[
  v_5(D)=s;
  \]
- if \(v_5(Q)\le m_2\), strict \(k_{12}\ge1\) localizes deep unit phase to \(a_2\);
- partial trace death when
  \[
  \nu+3s<2\gamma+n_3.
  \]

## COMPUTATIONAL EVIDENCE

- finite arithmetic checks were used only for falsification / family discovery;
- no nonexistence claim depends on computation.

## DISPROVED

### Overstrong conjecture A

\[
n_3-s
\text{ residual depth passes essentially unchanged to }P.
\]

False. It is exactly cancelled by rebuilding and then dividing the actual tail scale \(S\).

### Overstrong conjecture B

\[
k_{12}\ge1
\text{ automatically gives one extra }5\text{-adic digit of penetration}.
\]

False in general.

### Overstrong conjecture C

\[
\text{deep Phase-to-Cut congruence}+\text{reducedness}
\Longrightarrow\bot.
\]

False as a standalone mechanism; Section 20 gives an infinite pseudo-family.

## FAILED AS CLOSURE ROUTES

- pure residual \(5\)-depth;
- Phase-to-Cut + reducedness only;
- digit-window counting from a \(5^n\)-residue alone;
- treating \(5\)-adic digits as decimal digits;
- trying to use \(k_{12}\ge1\) as automatic depth gain.

## OPEN

1. A1 Partial-5 Norm-Excess Cut Obstruction;
2. equal-prefix-\(5\)-support norm resonance \(\lambda_N\);
3. prefix denominator resonance \(v_5(Q)>m_2\);
4. no-absorption \(v_5(b_3)=0\);
5. full absorption \(v_5(b_3)\ge n_3\);
6. optional \(2\)-adic synchronization sufficient to turn \(5\)-residue into actual decimal suffix;
7. full A1 closure.

---

# 27. At most three next-round targets

## Target 1 — Same-Cut Norm-Excess Feedback

只研究：

\[
R_5
=
v_5(N)+2s-2v_5(G)-n_3
\]

与：

\[
P=a_1 10^n+a_2
\]

的 self-consistency。

目标：

\[
\boxed{
\text{same cut produces }\nu
\Longrightarrow
\text{same cut cannot satisfy its induced residue}.
}
\]

这是首选。

## Target 2 — Prefix \(5\)-Resonance Split

只分离两个真正仍能制造大 \(\nu\) / 大 \(v_5(Q)\) 的 escape：

\[
r_1=r_2>0
\]

中的 norm unit resonance \(\lambda_N\)，以及：

\[
v_5(Q)>m_2.
\]

不要再做全素数 audit。

## Target 3 — Conditional \(2\times5\) Decimal Suffix Synchronization

只有在 Target 1 需要 actual base-10 suffix 时，再从同一个 determinant bridge提取最小必要的 \(2\)-adic depth，与本轮 \(R_5\) CRT 合成：

\[
P\bmod10^j.
\]

不单独发展 generic \(2\)-adic campaign。

---

# 28. Final assessment

本轮最初的问题是：

\[
\boxed{
\text{怎样把 }5\text{-adic phase 变成 decimal information？}
}
\]

现在答案已经相当精确。

不是：

\[
5^{n_3-s}\mid Z_-
\Longrightarrow
5^{n_3-s}\mid\text{某个 }P\text{-expression}.
\]

而是：

\[
\boxed{
\begin{aligned}
&v_5(Z_-)
=
n_3-s+e,\\
&\Downarrow\\
&v_5(b_3P-a_3D)=e,\\
&\Downarrow\\
&R_5^{\rm cut}=(e-s)_+,\\
&\Downarrow\\
&P\equiv C_5(T,a_3)\pmod{5^{R_5^{\rm cut}}},
\end{aligned}
}
\]

并且：

\[
\boxed{
e
=
v_5(N)+3s-2v_5(G)-n_3.
}
\]

所以真正的 phase source 已从“tail residual depth”重新识别为：

\[
\boxed{
\textbf{same-cut norm excess over the absorbed tail budget}.
}
\]

这使 partial-\(5\) 的下一轮问题明显变小：

\[
\boxed{
\textbf{不再问 phase 能不能到 cut；}
}
\]

而只问：

\[
\boxed{
\textbf{一个 actual cut 能否同时制造足够大的 }\nu=v_5(N)
\textbf{，并满足由这个 }\nu\textbf{ 反向生成的 residue class？}
}
\]

这就是当前 backward A1 的最小 partial-\(5\) frontier。
