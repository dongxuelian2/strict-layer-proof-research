# Strict Layer A1 — Exact Resonance RGCD Overload Extinction Campaign

**文件名：** `strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md`  
**范围：** 三项十进制拼接平方和问题，Strict Layer，仅 \(A_1\)-only，且本文件只研究 exact resonance \(R=0\)。  
**目标：**
\[
\boxed{R=0\Longrightarrow\varnothing.}
\]

---

# 1. Executive Summary

本轮**没有**证明

\[
\boxed{R=0\Longrightarrow\varnothing.}
\]

因此不能生成假的 resonance closure certificate，也不进入 \(d=0,1\) nonresonant transition。

但本轮得到了一组比起点 RGCD-overload 明显更低维的 exact normal forms，并且首次把 resonance 的 word/Smith arithmetic 严格接到 prescribed radial denominator \(u_0\)。

最重要的新结论如下。

## 1.1 Exact Overload–\(J\) Dictionary

令

\[
G:=10^g,
\qquad
h_R=\gcd(G^2D,\;GQ_0-S_R).
\]

写

\[
D=2^a5^bD_\perp,
\qquad
h_R=2^{r_2}5^{r_5}h_\perp,
\]

\[
e_2=r_2-(a+g),
\qquad
e_5=r_5-(b+g),
\qquad
\lambda_\perp:=D_\perp/h_\perp.
\]

则

\[
\boxed{
\beta
=
2^{g-e_2}5^{g-e_5}\lambda_\perp
}
\]

以及

\[
\boxed{
J=\frac{G}{\gcd(G,\beta)}
=
2^{e_2^+}5^{e_5^+}.
}
\]

利用 resonance 已有 \(v_2(\beta)\le2g\) 与 \(\beta<G\) 对 \(5\)-adic excess 的自动上界，可再定义

\[
\boxed{
d_*:=2^{e_2^-}5^{e_5^-}
}
\]

并得到

\[
\boxed{
\beta=\frac{G}{J}\,d_*\,\lambda_\perp.
}
\]

所以 RGCD overload

\[
2^{e_2}5^{e_5}>\lambda_\perp
\]

精确等价于

\[
\boxed{
J>d_*\lambda_\perp.
}
\]

而 denominator digit information 更强，实际给出

\[
\boxed{
c_R=s\,d_*\lambda_\perp<J.
}
\]

换言之，RGCD overload 与 resonance divisor \(J\) 并非两份独立信息；它们是同一份 \(2/5\)-adic content 的正、负 excess 两侧。

---

## 1.2 Resonant Ten-Free Saturation

由

\[
\beta=\frac{G^2D}{h_R}
\]

取 ten-free part：

\[
\boxed{
\beta^{\langle10\rangle}
=
\frac{D_\perp}{h_\perp}
=
\lambda_\perp.
}
\]

而

\[
b_2=s\beta=\frac{Gc_R}{J}
\]

且 \(G/J\) 为 \(2,5\)-smooth，所以

\[
\boxed{
\lambda_\perp=\beta^{\langle10\rangle}\mid c_R.
}
\]

结合已有 ASYM-4：

\[
\boxed{
p\mid\beta^{\langle10\rangle}
\Longrightarrow
p\equiv1\pmod4.
}
\]

因此 ten-free missing content 不能任意增长；它必须完整装进

\[
c_R<J.
\]

特别地，若 \(c_R<13\)，则

\[
\boxed{\beta^{\langle10\rangle}=1.}
\]

所以对

\[
J\in\{2,4,5,8,10\}
\]

所有 small-\(J\) states，ten-free defect quotient 自动完全饱和：

\[
\boxed{h_\perp=D_\perp.}
\]

---

## 1.3 用户候选 \(K_c\mid S_R\) — 成立

冻结

\[
L:=G/J,
\qquad
b_2=Lc_R,
\qquad
S_R=JZ.
\]

从 leading defect identity 可得

\[
\boxed{
b_1JD=c_R\left(Q_0-\frac{S_R}{G}\right).
}
\]

等价地

\[
G\mid c_RS_R.
\]

令

\[
g_c:=\gcd(L,c_R),
\qquad
T_c:=L/g_c.
\]

则

\[
T_c\mid Z.
\]

故

\[
\boxed{
K_c:=JT_c
=
\frac{G}{g_c}
\mid S_R.
}
\]

并且

\[
\boxed{K_c\ge J.}
\]

所以本轮最低验收线之一：

\[
\boxed{
K_c=
\frac{10^g}{\gcd(10^g/J,c_R)}
\mid S_R
}
\]

严格成立。

---

## 1.4 更强：Canonical Enhanced Divisor \(K_*\)

事实上 \(K_c\) 仍不是最自然的最终 deflation。

令

\[
L=\gcd(G,\beta)=G/J,
\qquad
\Lambda:=\beta/L,
\qquad
d_*:=\gcd(L,\Lambda).
\]

由 exact overload dictionary：

\[
\boxed{
\Lambda=d_*\beta_0,
\qquad
\beta_0:=\beta^{\langle10\rangle}.
}
\]

并且

\[
\boxed{
c_R=s\,d_*\beta_0.
}
\]

RGCD identity 可化为

\[
uGD=\Lambda(LQ_0-Z).
\]

写

\[
L=d_*T,
\qquad
\Lambda=d_*\beta_0,
\qquad
\gcd(T,\beta_0)=1.
\]

约去 \(d_*\) 后，模 \(T\) 得

\[
T\mid Z.
\]

令

\[
Z=TW.
\]

于是

\[
\boxed{
S_R
=
\frac{G}{d_*}W.
}
\]

定义

\[
\boxed{
K_*:=\frac{G}{d_*}.
}
\]

则

\[
\boxed{
K_*\mid S_R.
}
\]

因为 \(d_*\mid g_c\)，

\[
\boxed{
K_*\ge K_c\ge J.
}
\]

因此真正的 canonical enhanced divisor 是

\[
\boxed{
K_*=\frac{10^g}{d_*}.
}
\]

---

## 1.5 Canonical Fully-Deflated Resonance Core

进一步，因为

\[
\gcd(\beta_0,uJ)=1
\]

且

\[
uJD=\beta_0(d_*Q_0-W),
\]

得到

\[
\boxed{\beta_0\mid D.}
\]

写

\[
D=\beta_0D_1.
\]

则 resonance 的 RGCD core 精确压成

\[
\boxed{
uJD_1=d_*Q_0-W.
}
\tag{CORE}
\]

同时：

\[
\boxed{
S_R=K_*W=\frac{G}{d_*}W,
}
\tag{S-W}
\]

\[
\boxed{
c_R=s\,d_*\beta_0,
}
\tag{C-CONTENT}
\]

\[
\boxed{
D=\beta_0D_1.
}
\]

并且因为 \(0<|S_R|<Q_0\)：

\[
\boxed{
0<|W|<\frac{d_*Q_0}{G}.
}
\tag{WBOUND}
\]

这就是本轮后最小的 resonance arithmetic core。

---

## 1.6 Ultra-Sharp Resonant Mantissa

由

\[
b_1=su
\]

与 (CORE)：

\[
b_1JD
=
s\beta_0(d_*Q_0-W).
\]

而

\[
c_R=s\,d_*\beta_0.
\]

故：

\[
\boxed{
b_1JD
=
c_RQ_0-s\beta_0W.
}
\tag{USM-EXACT}
\]

于是

\[
\left|
\frac{b_1JD}{c_RQ_0}-1
\right|
=
\frac{|W|}{d_*Q_0}
<
\frac1G.
\]

即

\[
\boxed{
\left|
\frac{b_1JD}{c_RQ_0}-1
\right|
<
10^{-g}.
}
\tag{RUSM}
\]

等价于

\[
\boxed{
\frac{c_R}{b_1J}(1-10^{-g})
<
\frac D{Q_0}
<
\frac{c_R}{b_1J}(1+10^{-g}).
}
\tag{D-ULTRA}
\]

所以

\[
\boxed{
1+\frac{c_R}{b_1J}(1-10^{-g})
<
\frac{10^kP_1}{Q_0}
<
1+\frac{c_R}{b_1J}(1+10^{-g}).
}
\tag{P1-ULTRA}
\]

这严格加强 frozen SPM：

\[
0<D<Q_0/b_1.
\]

---

## 1.7 NEW — Cyclotomic Radial Denominator Theorem

这是本轮最重要的新 word/radial splice。

resonance full Smith 中

\[
u=\gamma u_0,
\qquad
u_0\mid M,N,
\qquad
\gcd(u,\beta)=1.
\]

因此

\[
\gcd(u_0,\beta)=1.
\]

primitive sphere 又给

\[
\boxed{\gcd(u_0,Q_0)=1.}
\]

证明：若 \(p\mid u_0,Q_0\)，则 \(p\mid P_2,P_3,Q_0\)，由 sphere 得 \(p\mid P_1\)，与 primitive quadruple 矛盾。

另一方面

\[
S_R=P_2+P_3-Q_0
\equiv -Q_0
\pmod{u_0},
\]

所以

\[
\boxed{\gcd(u_0,S_R)=1.}
\tag{U0-S}
\]

现在把 RGCD identity

\[
uG^2D=\beta(GQ_0-S_R)
\]

模 \(u_0\)：

\[
GQ_0\equiv S_R\pmod{u_0}.
\]

再代入

\[
S_R\equiv-Q_0\pmod{u_0},
\]

并利用 \(\gcd(u_0,Q_0)=1\)，得到

\[
\boxed{
u_0\mid G+1=10^g+1.
}
\tag{CYC-U0}
\]

因此：

\[
\boxed{
u_0\text{ 是 }10^g+1\text{ 的 cyclotomic divisor。}
}
\]

特别：

\[
\boxed{
\gcd(u_0,10)=1,
\qquad
u_0\le10^g+1.
}
\]

同时由于 \(K_*\mid S_R\)：

\[
\boxed{
\gcd(u_0,K_*)=1,
\qquad
\gcd(u_0,W)=1.
}
\]

这正是此前 resonance reports 明确缺失的：

\[
\boxed{
\text{word/Smith depth}
\longrightarrow
\text{prescribed radial denominator }u_0
}
\]

的 exact bridge。

---

# 2. Provenance Audit

本轮优先核查：

- `strict_layer_A1_resonant_transition_reduced_fraction_unit_exclusion_campaign.md`；
- `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`；
- `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`；
- `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`；
- `strict_layer_A1_unified_moving_profile_terminal_campaign.md`；
- `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`；
- `strict_layer_A1_RU_H_first_candidate_excess_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`。

source audit 确认：

1. RGCD identity、\(J\mid S_R\)、integerized \(c_R\) 是上一轮 frozen result；
2. 旧 report 已有 resonance \(2\)-adic trichotomy；
3. 旧 report 明确认为当时缺少一个把 \(S_R\)-depth 接到 \(u_0\) 的 exact bridge；
4. 本轮没有在 synthesis 或后续 endpoint report 中找到
   \[
   u_0\mid10^g+1
   \]
   的等价 theorem；
5. 本轮 \(K_*\) 与 cyclotomic radial denominator theorem 因而可标记为 NEW PROVED。

主要 source provenance：fileciteturn12file0 fileciteturn12file5 fileciteturn13file0 fileciteturn13file1

---

# 3. Frozen Resonance Normal Form

固定：

\[
\boxed{R=0.}
\]

则：

\[
\boxed{
d=0,
\qquad
m_2=g,
\qquad
n_2=2g+k,
}
\]

\[
\boxed{
\alpha=t=1,
\qquad
v=10^{n_3}.
}
\]

Smith denominator：

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

Smith-radial：

\[
\boxed{
g_2=u_010^{n_3},
\qquad
g_3=u_0,
}
\]

\[
\boxed{
P_2=10^{n_3}M,
\qquad
P_3=N,
}
\]

\[
\boxed{
C_2=M/u_0,
\qquad
C_3=N/u_0.
}
\]

primitive sphere：

\[
\boxed{
P_1^2+10^{2n_3}M^2+N^2=Q_0^2.
}
\]

leading defect：

\[
\boxed{
D=10^kP_1-Q_0>0.
}
\]

frozen sharp mantissa：

\[
\boxed{
0<D<Q_0/b_1.
}
\]

resonance gap：

\[
\boxed{
S_R=P_2+P_3-Q_0\ne0.
}
\]

\[
\boxed{
10^gH=b_2S_R.
}
\]

plus：

\[
S_R<0.
\]

minus：

\[
S_R>0.
\]

---

# 4. IMPORTANT PROVENANCE CORRECTION — Integer Margin Normalization

本轮在使用 Face A/B integer margin 前重新逐式核验，发现上一 resonance / iterated-Smith report 中有一个 \(u_0\)-normalization slip。

正确的 Face A 推导是：

\[
MU\ge10^{n_2-1}u_0,
\]

\[
10^{n_3}u_0-NU\ge1.
\]

因此：

\[
\boxed{
u_0\mathcal G_A\ge M,
}
\qquad
\mathcal G_A:=M10^{n_3}-N10^{n_2-1}.
\tag{IGA-CORRECT}
\]

因为 \(M=u_0C_2\)，它等价于

\[
\boxed{
\mathcal G_A\ge C_2,
}
\]

而**不是**

\[
\mathcal G_A\ge M
\]

除非 \(u_0=1\)。

Face B 同理：

\[
\boxed{
u_0\mathcal G_B\ge N,
}
\qquad
\mathcal G_B:=N10^{n_2}-M10^{n_3-1},
\]

等价于

\[
\boxed{
\mathcal G_B\ge C_3.
}
\]

后来的 first-candidate / endpoint-quotient report 给出的 intrinsic criteria

\[
G_A^\circ\ge C_3\delta_2+C_2,
\]

\[
G_B^\circ\ge C_2\delta_3+C_3
\]

与此完全一致。fileciteturn13file0

所以此前由误写的

\[
\mathcal G_A\ge M,
\qquad
\mathcal G_B\ge N
\]

推出的两个 \(u_0\)-independent “integer-surviving ratio slabs”不能继续作为 global frozen theorem 使用。

正确 coarse slabs 是：

### Face A

令

\[
r=P_3/P_2.
\]

则：

\[
\boxed{
r
\le
10^{1-n_2}
\left(
1-\frac1{u_010^{n_3}}
\right).
}
\tag{A-SLAB-CORR}
\]

### Face B

\[
\boxed{
r
\ge
\frac1{10(10^{n_2}-1/u_0)}.
}
\tag{B-SLAB-CORR}
\]

连续 Face A/B boundaries 不受影响。

此前 sign–face–\(\kappa\) 粗表主要来自 continuous boundaries，因此仍可保留：

\[
\boxed{
\begin{array}{c|c|c}
 & A & B\\
\hline
+ & k-2g\le0 & k-2g\le1\\
- & k-2g\ge-1 & k-2g\ge0.
\end{array}}
\]

但任何使用旧 stronger integer slab 的后续 sharpening 必须重新核验 scope。

---

# 5. Primewise RGCD Decomposition

定义：

\[
A_R=G^2D,
\qquad
B_R=GQ_0-S_R.
\]

\[
h_R=\gcd(A_R,B_R).
\]

由 reduced identity：

\[
uA_R=\beta B_R,
\qquad
\gcd(u,\beta)=1,
\]

严格得到：

\[
\boxed{
u=B_R/h_R,
\qquad
\beta=A_R/h_R.
}
\]

又 \(\beta<b_2<G\)，所以：

\[
\boxed{
h_R>GD.
}
\]

写：

\[
D=2^a5^bD_\perp,
\]

\[
h_R=2^{r_2}5^{r_5}h_\perp,
\]

\[
e_2=r_2-(a+g),
\qquad
e_5=r_5-(b+g).
\]

则：

\[
\boxed{
\lambda_\perp:=D_\perp/h_\perp\in\mathbf Z_{\ge1}.
}
\]

并且：

\[
\boxed{
2^{e_2}5^{e_5}>\lambda_\perp.
}
\tag{OV}
\]

这就是 Decimal Overload Necessity。

ten-free part本身不能提供 overload：

\[
h_\perp\le D_\perp.
\]

overload 必须由 extra \(2/5\)-adic common depth 提供。

---

# 6. Exact \(J/e_2/e_5\) Dictionary

从

\[
\beta=\frac{G^2D}{h_R}
\]

直接：

\[
v_2(\beta)=g-e_2,
\qquad
v_5(\beta)=g-e_5.
\]

resonance iterated-Smith 的 \(J\) 精确简化为：

\[
\boxed{
J=\frac{G}{\gcd(G,\beta)}.
}
\]

因此：

\[
\boxed{
v_2(J)=e_2^+,
\qquad
v_5(J)=e_5^+.
}
\]

即：

\[
\boxed{
J=2^{e_2^+}5^{e_5^+}.
}
\]

另一方面，利用 resonance \(2\)-adic theorem

\[
v_2(\beta)\le2g
\]

以及 \(\beta<G\Rightarrow v_5(\beta)<2g\)，negative excess 完整进入

\[
d_*:
\]

\[
\boxed{
d_*=2^{e_2^-}5^{e_5^-}.
}
\]

ten-free quotient：

\[
\boxed{
\beta_0=\lambda_\perp.
}
\]

所以：

\[
\boxed{
\beta
=
\frac{G}{J}d_*\beta_0.
}
\]

而 integerized mantissa：

\[
\boxed{
c_R=s\,d_*\beta_0.
}
\]

因此：

\[
\boxed{
d_*\beta_0<J
}
\]

且实际上

\[
\boxed{
s\,d_*\beta_0<J.
}
\]

这比单纯 OV 更强。

---

# 7. Exact Formula for the Overloaded GCD

由

\[
D=\beta_0D_1,
\qquad
\beta=(G/J)d_*\beta_0,
\]

得到：

\[
h_R
=
\frac{G^2D}{\beta}
=
\frac{GJ}{d_*}D_1.
\]

所以：

\[
\boxed{
h_R=K_*JD_1,
\qquad
K_*=\frac{G}{d_*}.
}
\]

并且：

\[
\frac{h_R}{GD}
=
\frac{J}{d_*\beta_0}.
\]

RGCD overload

\[
h_R>GD
\]

因而恰好等价于：

\[
\boxed{
J>d_*\beta_0.
}
\]

digit range 则给：

\[
\boxed{
J>s\,d_*\beta_0=c_R.
}
\]

所以“异常大 gcd”不再是一个神秘随机事件，而是 denominator mantissa 的 exact content theorem。

---

# 8. \(D\) 的 Decimal Source Facts

因为 \(Q_0\) odd 且 \(k\ge1\)：

\[
10^kP_1\text{ 为偶数},
\]

所以：

\[
\boxed{
D=10^kP_1-Q_0\text{ 永远为奇数}.
}
\]

即：

\[
\boxed{v_2(D)=0.}
\]

此外，若 \(5\mid\beta\)，则：

- \(5\nmid u\)；
- \(5\nmid u_0\)；
- \(5\nmid C_2,C_3\)；
- \(5\mid P_1,P_2\)；
- \(5\nmid P_3\)。

由 primitive sphere：

\[
\boxed{5\nmid Q_0.}
\]

于是：

\[
10^kP_1\equiv0\pmod5,
\qquad
Q_0\not\equiv0\pmod5,
\]

故：

\[
\boxed{
5\mid\beta
\Longrightarrow
v_5(D)=0.
}
\]

这会显著收紧 decimal overload 的 source cancellation。

---

# 9. NEW — \(5\)-Adic Resonant Tail Lock

假设：

\[
5\mid\beta.
\]

如上：

\[
v_5(P_2)=n_3,
\]

\[
v_5(P_1)>n_3,
\]

\[
v_5(P_3)=v_5(Q_0)=0.
\]

sphere：

\[
Q_0^2-P_3^2=P_1^2+P_2^2.
\]

右侧最低 \(5\)-valuation 唯一来自 \(P_2^2\)，所以：

\[
\boxed{
v_5(Q_0^2-P_3^2)=2n_3.
}
\]

enhanced divisor \(K_*\) 在 \(5\mid\beta\) 时必仍含正 \(5\)-adic depth，因此

\[
5\mid S_R.
\]

而：

\[
Q_0-P_3=P_2-S_R
\]

也被 \(5\) 整除。

由于 \(Q_0,P_3\) 都是 \(5\)-units，\(Q_0-P_3\) 与 \(Q_0+P_3\) 不可能同时被 \(5\) 整除，所以：

\[
\boxed{
v_5(Q_0-P_3)=2n_3.
}
\]

比较

\[
P_2-S_R
\]

中 \(P_2\) 的 valuation \(n_3\)，要得到 \(2n_3>n_3\)，必须：

\[
\boxed{
v_5(S_R)=n_3.
}
\tag{5-LOCK}
\]

这是一条新的 source-level exact lock。

---

# 10. \(2\)-Adic Resonant Tail Classification

若：

\[
2\mid\beta,
\]

则：

\[
P_3,Q_0\text{ odd},
\]

\[
v_2(P_2)=n_3,
\qquad
v_2(P_1)>n_3.
\]

所以：

\[
v_2(Q_0^2-P_3^2)=2n_3.
\]

由于 odd square difference 必被 \(8\) 整除，立即得到：

\[
\boxed{
2\mid\beta
\Longrightarrow
n_3\ge2.
}
\]

令

\[
a:=v_2(\beta).
\]

冻结旧 resonance trichotomy：

\[
a<g\Rightarrow v_2(S_R)=g,
\]

\[
a=g\Rightarrow v_2(S_R)\ge g+1,
\]

\[
g<a\le2g\Rightarrow v_2(S_R)=2g-a.
\]

又 \(S_R=P_2+P_3-Q_0\) 必为偶数，所以：

\[
\boxed{a=2g\text{ impossible}.}
\]

若

\[
v_2(S_R)\ge2,
\]

则 \(Q_0-P_3=P_2-S_R\) 是 \(Q_0^2-P_3^2\) 的 high \(2\)-adic factor，因此：

\[
\boxed{
v_2(S_R)=n_3.
}
\]

所以：

\[
\boxed{
\begin{array}{ll}
a<g,\ g\ge2
&\Rightarrow n_3=g,\\[1mm]
a=g
&\Rightarrow n_3=v_2(S_R)\ge g+1,\\[1mm]
g<a\le2g-2
&\Rightarrow n_3=2g-a,\\[1mm]
a=2g-1
&\Rightarrow v_2(S_R)=1\text{，为 low-factor branch}.
\end{array}
}
\tag{2-LOCK}
\]

这把旧纯 valuation trichotomy 升级成 source-coordinate \(n_3\) lock。

---

# 11. Small-\(J\): \(J=2\)

因为：

\[
c_R=1,
\]

而

\[
c_R=s\,d_*\beta_0,
\]

得到：

\[
\boxed{
s=d_*=\beta_0=1.
}
\]

因此：

\[
\boxed{
\beta=G/2,
\qquad
b_2=G/2,
\qquad
K_*=G.
}
\]

canonical core：

\[
\boxed{
2uD=Q_0-W,
}
\]

\[
\boxed{
S_R=GW.
}
\]

## 11.1 \(g\ge2\)

此时 \(\beta=G/2\) 同时含 \(2,5\)。

由 \(5\)-lock：

\[
n_3=g+v_5(W).
\]

而

\[
v_2(\beta)=g-1<g.
\]

旧 \(2\)-adic trichotomy给：

\[
v_2(S_R)=g.
\]

当 \(g\ge2\) 时为 high branch，故：

\[
n_3=g.
\]

所以：

\[
\boxed{
v_5(W)=0,
\qquad
v_2(W)=0.
}
\]

即：

\[
\boxed{
J=2,\ g\ge2
\Longrightarrow
n_3=g,\quad
\gcd(W,10)=1.
}
\tag{J2-N}
\]

又 \(\gcd(u,\beta)=1\)，所以 \(u\) decimal-unit，\(\gamma=1\)，因此：

\[
\boxed{
u=u_0\mid G+1.
}
\]

并且：

\[
\boxed{b_1=u_0.}
\]

sphere tail factor进一步给：

\[
v_5(Q_0-P_3)=2g,
\]

\[
v_2(Q_0-P_3)=2g-1.
\]

因此存在 ten-unit \(T\) 使：

\[
\boxed{
Q_0-P_3
=
\frac{G^2}{2}T,
\qquad
\gcd(T,10)=1.
}
\tag{J2-TAIL}
\]

所以 \(J=2,g\ge2\) 已压成：

\[
\boxed{
\begin{gathered}
u_0\mid G+1,\qquad
b_1=u_0,\quad
b_2=G/2,\quad
n_3=g,\\
S_R=GW,\quad
\gcd(W,10)=1,\\
2u_0D=Q_0-W,\\
Q_0-P_3=(G^2/2)T,\quad
\gcd(T,10)=1.
\end{gathered}
}
\]

但本轮未从这些式子推出 contradiction。

## 11.2 \(g=1\)

此时：

\[
\beta=5,
\qquad
S_R=10W,
\qquad
2uD=Q_0-W.
\]

只可用 \(5\)-lock：

\[
\boxed{
n_3=1+v_5(W).
}
\]

cyclotomic theorem 给：

\[
u_0\mid11.
\]

因为 \(\gcd(u,5)=1\)，\(u\) 的 decimal overlap 只能来自 \(2\)-part；可写成

\[
u=2^r u_0,
\qquad
u_0\mid11,
\]

且 cyclotomic \(u_0\) 保持 decimal-unit。

该 \(g=1\) exceptional chamber 仍 OPEN。

---

# 12. Small-\(J\): \(J=5\)

由于：

\[
c_R<5
\]

且 \(\beta_0\) 的所有 odd ten-free primes 都必须 \(1\bmod4\)，得到：

\[
\boxed{\beta_0=1.}
\]

又：

\[
J=5
\]

强迫：

\[
v_5(\beta)=g-1,
\qquad
v_2(\beta)\ge g.
\]

所以：

\[
d_*=2^{v_2(\beta)-g}.
\]

由

\[
c_R=s\,d_*<5
\]

可知：

\[
\boxed{
d_*\in\{1,2,4\}.
}
\]

canonical core：

\[
\boxed{
5uD=d_*Q_0-W,
}
\]

\[
\boxed{
S_R=(G/d_*)W.
}
\]

## 12.1 \(g\ge2\)

此时 \(5\mid\beta\)。

由 core 模 \(5\)：

\[
W\equiv d_*Q_0\not\equiv0\pmod5.
\]

所以：

\[
v_5(W)=0.
\]

结合 \(5\)-lock：

\[
\boxed{
n_3=g.
}
\tag{J5-5}
\]

现在分 \(d_*\)。

### \(d_*=1\)

此时：

\[
v_2(\beta)=g.
\]

旧 \(2\)-adic trichotomy给：

\[
v_2(S_R)\ge g+1.
\]

但 \(n_3=g\ge2\)，high factor lock要求

\[
v_2(S_R)=n_3=g.
\]

矛盾。

故：

\[
\boxed{
J=5,\ g\ge2,\ d_*=1
\Longrightarrow\bot.
}
\]

### \(d_*=2\)

此时：

\[
v_2(\beta)=g+1,
\]

\[
v_2(S_R)=g-1.
\]

若 \(g\ge3\)，则 \(g-1\ge2\)，high factor lock给：

\[
n_3=g-1,
\]

与 \(n_3=g\) 矛盾。

因此只剩：

\[
\boxed{
(g,n_3,d_*)=(2,2,2).
}
\]

此时：

\[
G=100,
\qquad
\beta=40,
\]

\[
c_R=2s<5
\Longrightarrow
s\in\{1,2\}.
\]

所以：

\[
\boxed{
b_2\in\{40,80\}.
}
\]

又 \(\gcd(u,40)=1\)，故 \(\gamma=1\)：

\[
\boxed{
u=u_0\mid101.
}
\]

### \(d_*=4\)

此时：

\[
v_2(\beta)=g+2.
\]

旧 \(a=2g\) branch 已被 source parity排除，所以 \(g=2\) 不可能。

若 \(g\ge4\)：

\[
v_2(S_R)=g-2\ge2,
\]

high factor lock给：

\[
n_3=g-2,
\]

与 \(n_3=g\) 矛盾。

只剩：

\[
\boxed{
(g,n_3,d_*)=(3,3,4).
}
\]

此时：

\[
G=1000,
\qquad
\beta=800.
\]

\[
c_R=4s<5
\Longrightarrow
s=1.
\]

所以：

\[
\boxed{
b_2=800.
}
\]

并且：

\[
\boxed{
u=u_0\mid1001.
}
\]

故对 \(g\ge2\)：

\[
\boxed{
J=5
\Longrightarrow
(g,n_3,d_*)
\in
\{(2,2,2),(3,3,4)\}.
}
\tag{J5-FINITE-EXP}
\]

这是很强的 exponent finiteization，但两个 chamber 尚未严格关闭。

## 12.2 \(g=1\)

此时 \(v_5(\beta)=0\)，不能使用 \(5\)-lock。

\(d_*=2\) 对应 \(v_2(\beta)=2=2g\)，已由 \(S_R\) 必偶排除。

所以只剩：

\[
\boxed{
g=1,\quad d_*=1,\quad\beta=2.
}
\]

且：

\[
c_R=s<5
\Longrightarrow
s\in\{1,2,3,4\}.
\]

所以：

\[
\boxed{
b_2\in\{2,4,6,8\}.
}
\]

由 \(2\)-adic \(a=g\) branch：

\[
v_2(S_R)\ge2.
\]

因此：

\[
\boxed{n_3\ge2.}
\]

又 \(\gcd(u,2)=1\)，resonance decimal overlap of \(u\) 只能来自 \(5\)-part，可写：

\[
\boxed{
u=5^r u_0,
\qquad
u_0\mid11,
\qquad
0\le r\le n_3.
}
\]

所以 \(J=5\) 最终压成三个 exceptional families：

\[
\boxed{
\begin{array}{c|c}
\text{chamber}&\text{exact residual data}\\
\hline
g=1&
d_*=1,\ \beta=2,\ b_2\in\{2,4,6,8\},\ u=5^ru_0,\ u_0\mid11,\ n_3\ge2\\
g=2&
d_*=2,\ n_3=2,\ \beta=40,\ b_2\in\{40,80\},\ u_0\mid101\\
g=3&
d_*=4,\ n_3=3,\ \beta=800,\ b_2=800,\ u_0\mid1001.
\end{array}}
\]

本轮没有证明这三类为空，因此：

\[
\boxed{J=5\text{ NOT CLOSED}.}
\]

但其无界 \(g\)-freedom 已被完全删除。

---

# 13. General Small-\(J\) Consequence

因为：

\[
\beta_0\mid c_R<J
\]

且 \(\beta_0\) 的 odd primes只能 \(1\bmod4\)，第一枚可能出现的 nondecimal prime 是：

\[
13.
\]

因此：

\[
\boxed{
J<13
\Longrightarrow
\beta_0=1.
}
\]

在 \(J\mid10^g\) 的 admissible values 中：

\[
\boxed{
J\in\{2,4,5,8,10\}
\Longrightarrow
\beta_0=1.
}
\]

第一个可能有 nontrivial ten-free quotient 的 \(J\)-chamber 是：

\[
J=16
\]

且必须至少允许 \(c_R=13\)。

---

# 14. Exact Center \(\Omega=0\) — New Decimal Support Classification

冻结：

\[
\Omega=N10^{n_2}-M10^{n_3}=0
\]

等价于：

\[
\boxed{
P_2=10^{n_2}P_3.
}
\]

已有：

\[
n_2\ge n_3.
\]

若：

\[
n_2>n_3,
\]

旧 theorem 给：

\[
J=G.
\]

由

\[
J=G/\gcd(G,\beta)
\]

立即加强为：

\[
\boxed{
n_2>n_3
\Longrightarrow
\gcd(\beta,10)=1.
}
\]

所以这一支是 pure decimal-unit \(\beta\) chamber。

此时：

\[
L=1,
\qquad
d_*=1,
\qquad
\beta_0=\beta,
\]

\[
\boxed{
S_R=GW,
}
\]

\[
\boxed{
D=\beta D_1,
}
\]

\[
\boxed{
uGD_1=Q_0-W,
}
\]

\[
\boxed{
u_0\mid G+1.
}
\]

---

## 14.1 \(\Omega=0,\ n_2=n_3\)

此时：

\[
n_3=n_2=2g+k.
\]

若 \(5\mid\beta\)，由 \(5\)-lock 与 canonical core primewise comparison 得：

\[
\boxed{
v_5(\beta)=g.
}
\]

若 \(2\mid\beta\)，由 \(2\)-adic source lock 得：

\[
\boxed{
v_2(\beta)\in\{g,2g-1\}.
}
\]

但若 \(\beta\) 同时含 \(2,5\)：

- \(v_2(\beta)=g,\ v_5(\beta)=g\) 已强迫 \(\beta\ge G\)；
- \(v_2(\beta)=2g-1,\ v_5(\beta)=g\) 更强迫 \(\beta\ge G\)。

这与：

\[
\beta<G
\]

矛盾。

因此：

\[
\boxed{
\Omega=0,\ n_2=n_3
\Longrightarrow
\beta\text{ 不可能同时含 }2,5.
}
\]

exact center 只剩三种 decimal support：

### Type U — decimal-unit

\[
\boxed{
\gcd(\beta,10)=1,
\qquad
J=G.
}
\]

### Type 5 — pure \(5\)-support

\[
\boxed{
v_5(\beta)=g,
\qquad
2\nmid\beta,
\qquad
J=2^g.
}
\]

### Type 2 — pure \(2\)-support

\[
\boxed{
5\nmid\beta,
\qquad
v_2(\beta)\in\{g,2g-1\},
\qquad
J=5^g.
}
\]

所以 double resonance \(\Omega=0\) 已从“任意 \(J,\beta\)”压成三个 exact decimal-support profiles。

仍未全部关闭。

---

# 15. Normalized Resonance Equation

令：

\[
r:=P_3/P_2,
\qquad
z:=S_R/Q_0,
\]

\[
a_R:=\frac{c_R}{b_1J}.
\]

由 ultra-sharp exact identity：

\[
\frac D{Q_0}
=
a_R\left(1-\frac zG\right).
\]

故：

\[
\boxed{
\frac{P_1}{Q_0}
=
10^{-k}
\left[
1+a_R\left(1-\frac zG\right)
\right].
}
\]

又：

\[
P_2+P_3=Q_0(1+z).
\]

所以：

\[
\frac{P_2}{Q_0}=\frac{1+z}{1+r},
\]

\[
\frac{P_3}{Q_0}=\frac{r(1+z)}{1+r}.
\]

代入 sphere：

\[
\boxed{
10^{-2k}
\left[
1+a_R\left(1-\frac zG\right)
\right]^2
+
(1+z)^2\frac{1+r^2}{(1+r)^2}
=1.
}
\tag{NZ}
\]

这是 resonance continuous core 的最小二变量方程。

在 formal center \(z=0\)：

\[
\boxed{
\frac{2r_*}{(1+r_*)^2}
=
10^{-2k}(1+a_R)^2.
}
\tag{CENTER}
\]

small physical root 为：

\[
\boxed{
r_*
=
\frac{1-c-\sqrt{1-2c}}c,
\qquad
c=10^{-2k}(1+a_R)^2.
}
\]

这解释了旧 \(\kappa=k-2g\) threshold，但本轮没有从 (NZ) alone 得到 global contradiction。

---

# 16. \(W\)-Master Form

使用 canonical \(K_*\)：

\[
S_R=K_*W.
\]

定义：

\[
x=P_3/P_2,
\qquad
y=W/P_2.
\]

则：

\[
\frac{Q_0}{P_2}=1+x-K_*y.
\]

由

\[
b_1JD=c_RQ_0-s\beta_0W
\]

得到：

\[
\frac{P_1}{P_2}
=
\frac{
(b_1J+c_R)(1+x-K_*y)-s\beta_0y
}{
b_1J10^k
}.
\]

所以 exact WMASTER：

\[
\boxed{
\left[
\frac{
(b_1J+c_R)(1+x-K_*y)-s\beta_0y
}{
b_1J10^k
}
\right]^2
+
1+x^2
=
(1+x-K_*y)^2.
}
\tag{WMASTER}
\]

它是 homogeneous/projective quadratic core。

本轮对其判别式、center expansion、sign geometry 做了审计，但没有发现一个 uniform factorization 能直接杀掉所有 integer \(W\)。

因此 WMASTER 保留为 next-level algebraic core，不冒充 closure。

---

# 17. Enhanced Divisor versus Magnitude — Re-Audit

旧 route 只有：

\[
J\mid S_R,\qquad J\mid\Delta_R
\]

其中：

\[
\Delta_R=P_1^2-2P_2P_3.
\]

本轮提升为：

\[
\boxed{
K_*\mid S_R,
\qquad
K_*\mid\Delta_R.
}
\]

因为：

\[
\Delta_R
=
S_R(S_R-2(P_2+P_3)).
\]

这对 small \(J\) 的确显著加强了 decimal depth。

但 \(Q_0\) 可相对 \(G\) 无界增长；本轮未能 uniform 地证明：

\[
|\Delta_R|<K_*
\]

或：

\[
|S_R|<K_*.
\]

所以 generic divisor-vs-size route 仍未闭合。

---

# 18. Self-Modulus Congruences

从 fully-deflated core：

\[
uJD_1=d_*Q_0-W.
\]

对任意 ten-free prime power

\[
p^e\mid\beta_0
\]

有：

\[
p^e\mid D,
\]

且由原 RGCD：

\[
p^e\mid GQ_0-S_R.
\]

因此：

\[
\boxed{
GQ_0\equiv S_R\pmod{\beta_0}.
}
\]

再用：

\[
Q_0\equiv10^kP_1\pmod{\beta_0}
\]

得到：

\[
\boxed{
S_R
\equiv
G10^kP_1
\pmod{\beta_0}.
}
\]

由于：

\[
\beta_0\mid c_R<J,
\]

ten-free self-modulus 的缺口被 small mantissa严格控制。

对 \(p=2,5\)，canonical \(W\) coordinates 则把所有 overload phase压到：

\[
\boxed{
S_R=(G/d_*)W
}
\]

与 (CORE)，不再需要把 \(Z\) 当作独立 Hensel variable。

---

# 19. Radial Gate after the \(u_0\) Correction

真正的 radial semantic仍是：

\[
\frac U{u_0}\in K_{MN},
\qquad
\gcd(U,V)=1.
\]

但 endpoint arithmetic 最自然的 intrinsic coordinates 是：

\[
C_2=M/u_0,
\qquad
C_3=N/u_0.
\]

Face A raw survival：

\[
\boxed{
G_A^\circ\ge C_3\delta_2+C_2,
}
\]

其中：

\[
\delta_2=(-10^{n_2-1})\bmod C_2.
\]

Face B：

\[
\boxed{
G_B^\circ\ge C_2\delta_3+C_3.
}
\]

本轮 enhanced RGCD arithmetic 尚未 uniform 地限制 \(\delta_2,\delta_3\)。

所以：

\[
\boxed{
K_*+\text{cyclotomic }u_0
}
\]

虽然首次接上 radial denominator，但还没有最终接上 **endpoint modular phase**。

这就是 resonance 尚未闭合的精确原因。

---

# 20. Endpoint Equality Exceptions

冻结：

third lower equality 只能：

\[
\boxed{
n_3=1,\quad U=C_3=1.
}
\]

second lower equality强迫：

\[
\boxed{
U=1,\quad C_2=10^{n_2-1}.
}
\]

本轮增加：

若 second lower equality发生，则

\[
10\mid C_2.
\]

由：

\[
\gcd(C_2,b_2)=1
\]

得到：

\[
\gcd(b_2,10)=1.
\]

因此：

\[
\boxed{
J=G.
}
\]

并仍有：

\[
\boxed{
u_0\mid G+1.
}
\]

所以任何 resonance \(U=1\) lower-equality survivor 必落入 maximal-\(J\) cyclotomic denominator chamber。

但 \(U=1\) 本身自动通过 coprimality gate，故不能用 Layer P 排除；仍需 exact primitive/word contradiction。

---

# 21. Computational Evidence

本轮计算只用于验证 exact identities 与寻找反例，不作为 nonexistence dependency。

## 21.1 Generic reduced resonance generator

使用 fully-deflated variables：

\[
(G,J,d_*,\beta_0,s,u,D_1,W)
\]

重建：

\[
D=\beta_0D_1,
\]

\[
Q_0=(uJD_1+W)/d_*,
\]

\[
S_R=(G/d_*)W,
\]

\[
P_1=(Q_0+D)/10^k.
\]

再令：

\[
A=P_2+P_3=Q_0+S_R.
\]

sphere 要求：

\[
(P_2-P_3)^2
=
2(Q_0^2-P_1^2)-A^2
\]

为非负完全平方。

随后 exact 检查：

- \(P_2\equiv0\pmod{10^{n_3}}\)；
- Smith gcd profile；
- \(C_2,C_3\) reducedness；
- primitive quadruple；
- resonance；
- Layer C/I/P。

## 21.2 bounded checks

有限 exact searches 未找到 full synchronized resonance hit：

- \(g=1\) 的若干低 \(n_3,k,D_1\) slices：0 hits；
- specialized \(J=2,g=2,n_3=2\)，使用
  \[
  u_0\mid101
  \]
  的 divisor restriction，在大幅扩展的 \(D\)-slice 中：0 hits。

这些均标记：

\[
\boxed{\text{COMPUTATIONAL EVIDENCE ONLY}.}
\]

由于 \(Q_0,D_1,k\) 仍可移动，不能升级成 global theorem。

---

# 22. Killed / Downgraded Conjectures

## 22.1 “ten-free gcd 可以自己制造 overload”

**FALSE.**

\[
h_\perp\le D_\perp.
\]

overload 必须来自 \(2/5\)-adic excess。

---

## 22.2 “RGCD 与 \(J\) 是两套 independent 强条件”

**DOWNGRADED.**

exact content theorem：

\[
J=2^{e_2^+}5^{e_5^+},
\]

\[
d_*=2^{e_2^-}5^{e_5^-},
\]

\[
\beta_0=D_\perp/h_\perp.
\]

RGCD overload 等价于：

\[
J>d_*\beta_0.
\]

它是 \(J\)-mantissa system 的 primitive-defect projection。

---

## 22.3 “\(K_c\) 也许不成立”

**DISPROVED.**

\[
\boxed{K_c\mid S_R}
\]

成立，并被更强：

\[
\boxed{K_*\mid S_R}
\]

支配。

---

## 22.4 “旧 integer-surviving ratio slabs 可直接 frozen”

**FALSE AS STATED GLOBALLY.**

旧 report 把：

\[
u_0\mathcal G_A\ge M
\]

错误简化为：

\[
\mathcal G_A\ge M.
\]

正确是：

\[
\mathcal G_A\ge M/u_0=C_2.
\]

所以 old \(u_0\)-independent slabs 仅在 \(u_0=1\) 时成立。

---

## 22.5 “\(J=5\) 的 \(d_*=1\) 可形成无界 \(g\) survivor”

**FALSE for \(g\ge2\).**

\(5\)-lock 给 \(n_3=g\)，而 \(2\)-adic \(a=g\) branch要求 \(n_3\ge g+1\)。

因此：

\[
J=5,\ g\ge2,\ d_*=1
\Rightarrow\bot.
\]

---

## 22.6 “\(\Omega=0\) 可有 mixed \(2,5\)-support \(\beta\)”

**FALSE.**

在 \(n_2=n_3\) exact center：

\[
5\mid\beta\Rightarrow v_5(\beta)=g,
\]

\[
2\mid\beta\Rightarrow v_2(\beta)\in\{g,2g-1\}.
\]

mixed support 强迫 \(\beta\ge G\)，与 \(\beta<G\) 矛盾。

---

# 23. Current Exact Minimal Resonance Survivor Theorem

本轮后，任何仍可能存在的 exact resonance A1 state 必满足：

\[
\boxed{
\begin{gathered}
R=0,\quad
d=0,\quad
n_2=2g+k,\quad
\alpha=t=1,\quad
v=10^{n_3},\\
P_2=10^{n_3}M,\quad
P_3=N,\quad
u_0\mid M,N,\\
P_1^2+P_2^2+P_3^2=Q_0^2,\quad
\gcd(P_1,P_2,P_3,Q_0)=1,\\
J\mid G,\quad
J>1,\quad
d_*\text{ is }2,5\text{-smooth},\\
\beta_0^{\langle10\rangle}=\beta_0,\quad
p\mid\beta_0\Rightarrow p\equiv1\pmod4,\\
c_R=s\,d_*\beta_0<J,\\
D=\beta_0D_1,\quad
uJD_1=d_*Q_0-W,\\
S_R=(G/d_*)W\ne0,\quad
0<|W|<d_*Q_0/G,\\
u_0\mid G+1,\quad
\gcd(u_0,S_R)=1,\\
\left|
\frac{b_1JD}{c_RQ_0}-1
\right|<G^{-1}.
\end{gathered}
}
\tag{RES-MIN}
\]

并还必须通过 corrected intrinsic radial gate：

Face A：

\[
G_A^\circ\ge C_3\delta_2+C_2,
\]

或 Face B：

\[
G_B^\circ\ge C_2\delta_3+C_3,
\]

再满足：

\[
\gcd(U,V)=1.
\]

这已经比本轮起点 A1-RBMI 明显低维。

---

# 24. Closure Status

本轮没有证明：

\[
\boxed{R=0\Longrightarrow\varnothing.}
\]

所以：

\[
\boxed{\textbf{Exact Resonance remains OPEN}.}
\]

但最低验收线已严格完成：

\[
\boxed{
K_c=
\frac{10^g}{\gcd(10^g/J,c_R)}
\mid S_R.
}
\]

并且得到更强：

\[
\boxed{
K_*=\frac{10^g}{d_*}\mid S_R.
}
\]

第二条最低验收线同样完成：

\[
\boxed{
\frac{D_\perp}{h_\perp}
=
\beta^{\langle10\rangle}
\mid c_R.
}
\]

此外新增真正连接 radial denominator 的：

\[
\boxed{
u_0\mid10^g+1.
}
\]

---

# 25. PROVED / DERIVED / DISPROVED / OPEN Ledger

## FROZEN

- DD closed；
- Strict frontier = A1-only；
- resonance normal form；
- primitive sphere；
- SPM；
- \(S_R\ne0\)；
- \(J\mid S_R\)；
- RGCD identity；
- RGCD overload；
- integerized \(c_R\)；
- old resonance \(2\)-adic trichotomy；
- common-\(U\) reconstruction。

## NEW PROVED

1. Exact \(J/e_2/e_5\) dictionary；
2. \(d_*=2^{e_2^-}5^{e_5^-}\) dictionary；
3. ten-free saturation
   \[
   D_\perp/h_\perp=\beta_0\mid c_R;
   \]
4. \(K_c\mid S_R\)；
5. stronger \(K_*\mid S_R\)；
6. canonical fully-deflated core
   \[
   uJD_1=d_*Q_0-W;
   \]
7. ultra-sharp mantissa RUSM；
8. \(\gcd(u_0,Q_0)=1\)；
9. \(\gcd(u_0,S_R)=1\)；
10. cyclotomic radial denominator
    \[
    u_0\mid10^g+1;
    \]
11. \(5\)-adic tail lock
    \[
    5\mid\beta\Rightarrow v_5(S_R)=n_3;
    \]
12. refined \(2\)-adic source lock；
13. \(J=2,g\ge2\Rightarrow n_3=g,\ \gcd(W,10)=1\)；
14. \(J=5,g\ge2\) exponent finiteization；
15. \(J=5\) exact three-family residual classification；
16. exact-center decimal support classification；
17. corrected \(u_0\)-dependent coarse integer slabs。

## DERIVED / REPACKAGED

- RGCD overload is exactly
  \[
  J>d_*\beta_0;
  \]
- digit mantissa strengthens it to
  \[
  J>s\,d_*\beta_0;
  \]
- WMASTER / NZ normalized forms；
- \(K_*\mid\Delta_R\)。

## DISPROVED / CORRECTED

- old \(\mathcal G_A\ge M,\mathcal G_B\ge N\) normalization；
- old \(u_0\)-independent integer-surviving slabs as global statements；
- \(J=5,d_*=1,g\ge2\) infinite escape；
- mixed \(2,5\)-support exact center；
- “another generic bigger divisor” as the main missing mechanism。

## COMPUTATIONAL EVIDENCE

- low resonance slices：0 exact hits；
- \(J=2,g=2,n_3=2\) enlarged finite search：0 exact hits。

## OPEN

1. \(J=2\) full extinction；
2. three \(J=5\) exceptional families；
3. \(J\ge4\) general \(W\)-master / endpoint phase coupling；
4. \(\Omega=0\) three support profiles；
5. resonance endpoint modular phase；
6. \(R=0\Rightarrow\varnothing\)。

---

# 26. At Most Three Next Targets

本轮禁止进入 nonresonant transition。若继续 resonance，只建议：

### Target 1 — Cyclotomic \(u_0\) × Endpoint Phase

利用：

\[
u_0\mid10^g+1
\]

与 active endpoint reduced denominators 中 \(u_0\) 的不可约保留，直接攻击：

\[
\delta_2=(-10^{n_2-1})\bmod C_2,
\qquad
\delta_3=(-10^{n_3-1})\bmod C_3.
\]

目标是第一次把 cyclotomic radial denominator 变成 first-candidate phase restriction。

### Target 2 — \(J=2\) Terminal Conic

只研究：

\[
J=2,\quad
g\ge2,\quad
n_3=g,\quad
u_0\mid10^g+1,
\]

\[
2u_0D=Q_0-W,
\quad
S_R=10^gW,
\quad
\gcd(W,10)=1,
\]

\[
Q_0-P_3=(10^{2g}/2)T.
\]

这是当前最干净的 infinite resonance chamber。

### Target 3 — \(J=5\) Exceptional Cleanup

只处理：

\[
g=1,\beta=2;
\qquad
(g,n_3,\beta)=(2,2,40);
\qquad
(g,n_3,\beta)=(3,3,800).
\]

尤其后两支的 \(u_0\) 只取：

\[
u_0\mid101
\quad\text{或}\quad
u_0\mid1001,
\]

已接近 finite denominator-profile classification。

---

# 27. Final Verdict

本轮没有打穿：

\[
\boxed{R=0\Rightarrow\varnothing.}
\]

但 resonance 已从

\[
\boxed{
\text{“large self-generated gcd”}
}
\]

进一步压成：

\[
\boxed{
\textbf{exact decimal content dictionary}
+
\textbf{canonical deflated gap }W
+
\textbf{cyclotomic radial denominator }u_0
+
\textbf{source-level }2/5\textbf{-adic tail locks}.
}
\]

最重要的 architecture 更新是：

\[
\boxed{
R=0
\Longrightarrow
u_0\mid10^g+1.
}
\]

这第一次推翻了此前 resonance 中

\[
\boxed{
S_R\text{-depth 与 radial denominator }u_0\text{ 完全脱钩}
}
\]

的局面。

当前真正剩余的最后接口不再是“继续寻找更大 gcd”，而是：

\[
\boxed{
\textbf{Cyclotomic prescribed denominator}
\times
\textbf{endpoint modular phase}.
}
\]

在它闭合前，不应进入 nonresonant transition。
