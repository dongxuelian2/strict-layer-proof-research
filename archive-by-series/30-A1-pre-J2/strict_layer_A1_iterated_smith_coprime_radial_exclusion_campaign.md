# Strict Layer A1 正向线第八轮：Iterated-Smith Coprime-Radial Exclusion — Final Radial Successor Campaign

**文件名：** `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`  
**研究范围：** 三项十进制拼接平方和问题，Strict Layer，仅 `A1-only`。  
**直接目标：** 对所有 admissible A1 terminal states 证明

\[
\boxed{N_V(I_{23})=0}
\]

等价地

\[
\boxed{\operatorname{next}_V(L_{23})\ge R_{23}}.
\]


**本轮审计过的直接来源：**

- `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`；
- `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`；
- `strict_layer_A1_moving_profile_coprime_integer_scale_campaign.md`；
- `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`；
- `strict_layer_A1_unified_moving_profile_terminal_campaign.md`；
- `strict_layer_backward_A1_common_U_pullback_primitive_radial_gluing_campaign.md`；
- 执行本轮时 File Library 中发现的更新并行报告 `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`，其中只吸收了可由 frozen core 独立核准的 Smith-reduced identities。

**本轮最终裁决：**

\[
\boxed{\textbf{A1 尚未闭合。}}
\]

但本轮得到了此前 terminal reports 明确缺失的一类精确桥：

\[
\boxed{
\textbf{Double-Smith / DES integer defects}
\longleftrightarrow
\textbf{actual radial interval slack}
}
\]

并把剩余问题压成了 **两个 explicit active-face successor cases**，没有再产生新的顶层无限框架。

---

# 1. Executive Summary

前七轮已经把 A1 压到：

\[
\boxed{
\text{primitive sphere}
+\text{ exact word/DES}
+\text{ Iterated Smith}
+\text{ common coprime radial scale }U
}.
\]

第七轮的正确终点是：

\[
\boxed{
\text{word/Smith arithmetic 本身不足；最终语义 gate 是 common-}U.
}
\]

本轮首先核准 reconstruction theorem：一旦 exact synchronized primitive state、canonical gcd profile、denominator legality 与一个合法 coprime integer \(U\) 同时存在，就已经恢复 original A1 candidate。因此不存在一个尚未提取的独立 numerator semantic gate；backward phase/WGF/norm 在 exact forward state 上均为 derived/radially homogeneous view。于是本轮必须正面处理 radial successor，而不能再假设 DES 会凭空给出 \(U\bmod p\)。

本轮主要得到以下结果。

## 1.1 NEW PROVED — Full Smith–Radial Cancellation

令 full Smith chart 为

\[
b_1=s\alpha u,\qquad
b_2=s\alpha\beta t,\qquad
b_3=s\beta v,
\]

\[
\gamma=\gcd(u,v),\qquad
u=\gamma u_0,\qquad
v=\gamma v_0.
\]

则

\[
V=s\alpha\beta\gamma u_0tv_0,
\]

\[
g_2=u_0v,\qquad g_3=u_0\alpha t.
\]

又由 \(g_i\mid P_i\) 可写

\[
P_2=vM,\qquad P_3=\alpha tN,
\]

并有 \(u_0\mid M,N\)。于是

\[
\boxed{C_2=M/u_0,\qquad C_3=N/u_0.}
\tag{SR-C}
\]

因此 radial endpoints 精确化为

\[
\boxed{
L_2=\frac{u_0 10^{n_2-1}}M,
\qquad
L_3=\frac{u_0 10^{n_3-1}}N.
}
\tag{SR-L}
\]

这证明：\(\alpha,\beta,\gamma,t,v_0\) 等显式 Smith factors 在 projective/radial endpoints 中大量**完全消掉**。所以“Smith-rich 自动把 interval 乘法压短”不是合法的直接机制；Smith richness 只能通过约束 \((M,N,u_0,Z,\ldots)\) 间接进入 radial geometry。

## 1.2 NEW PROVED — Correct Active-Face Sign for \(R_U\)

定义 prompt 建议的 numerator radial resonance

\[
\boxed{
R_U:=C_2 10^{n_3-1}-C_3 10^{n_2-1}.
}
\]

则必须纠正 prompt 中一个符号方向：

\[
\boxed{
L_2\ge L_3\iff R_U\le0,
}
\]

而不是 \(R_U\ge0\)。同理

\[
\boxed{
L_3>L_2\iff R_U>0.
}
\]

\(R_U=0\iff L_2=L_3\)。

## 1.3 NEW PROVED — Exact Integer Radial Gap

定义

\[
A_U:=C_3 10^{n_2-1},\qquad
B_U:=C_2 10^{n_3-1},\qquad
W_U:=C_2C_3.
\]

则

\[
\boxed{
I_{23}
=
\left[
\frac{\max(A_U,B_U)}{W_U},
\frac{10\min(A_U,B_U)}{W_U}
\right).
}
\tag{RG-1}
\]

定义整数 radial slack

\[
\boxed{
G_U:=10\min(A_U,B_U)-\max(A_U,B_U).
}
\tag{RG-2}
\]

于是

\[
\boxed{I_{23}\ne\varnothing\iff G_U>0,}
\]

\[
\boxed{|I_{23}|=\frac{G_U}{C_2C_3}.}
\tag{RG-3}
\]

并且因为 \(R_U=B_U-A_U\)：

\[
\boxed{
G_U=9\min(A_U,B_U)-|R_U|.
}
\tag{RG-4}
\]

若定义

\[
\rho_U=\frac{\max(L_2,L_3)}{\min(L_2,L_3)}\in[1,10),
\qquad
\delta_U=10-\rho_U,
\]

则

\[
\boxed{
\delta_U=\frac{G_U}{\min(A_U,B_U)}.
}
\tag{RG-5}
\]

所以本轮确实找到了所要求的形式：

\[
\boxed{
\textbf{radial slack = normalized exact integer defect}.
}
\]

## 1.4 NEW PROVED — DES \(\leftrightarrow R_U\) Bridge

利用

\[
VC_i=b_iP_i
\]

和 exact tail relation

\[
10^{m_3}H=b_2P_2 10^{n_3}-b_3(Q_0-P_3),
\]

得到

\[
\boxed{
10VR_U
=
10^{m_3}H
+b_3\bigl(Q_0-P_3(1+10^{n_2})\bigr).
}
\tag{RU-H}
\]

这是一个低复杂度、完全 exact 的 \(R_U\)-DES bridge。

## 1.5 NEW PROVED — DES \(\leftrightarrow\) Actual Radial Slack Bridge

这比 (RU-H) 更直接。

### Face A: \(L_2\ge L_3\)（等价 \(R_U\le0\)）

定义

\[
G_A:=C_2 10^{n_3}-C_3 10^{n_2-1}=G_U>0.
\]

则

\[
\boxed{
VG_A
=
10^{m_3}H
+b_3\bigl(Q_0-P_3(1+10^{n_2-1})\bigr).
}
\tag{GAP-A}
\]

### Face B: \(L_3>L_2\)（等价 \(R_U>0\)）

定义

\[
G_B:=C_3 10^{n_2}-C_2 10^{n_3-1}=G_U>0.
\]

则

\[
\boxed{
10VG_B
=
-10^{m_3}H
+b_3\bigl(P_3(10^{n_2+1}+1)-Q_0\bigr).
}
\tag{GAP-B}
\]

这两条是本轮最重要的新增 theorem：它们第一次把第七轮的 integer defect \(H\) 直接写进了**真正决定 common-\(U\) interval width 的整数 gap**。

## 1.6 NEW PROVED — Iterated-Smith \(Z\) \(\leftrightarrow\) Radial Gap Bridge

第七轮有

\[
H=M_H^{(2)}Z,
\qquad
M_H^{(2)}=s\alpha\beta^\sharp v^\sharp,
\]

\[
tM10^{n_3}-A_3=JZ,
\qquad
A_3=(Q_0-P_3)/\alpha.
\]

故

\[
\boxed{
Q_0+\alpha JZ
=\alpha t(M10^{n_3}+N).
}
\tag{MNZ}
\]

定义 Smith-reduced face gaps

\[
\mathcal G_A:=M10^{n_3}-N10^{n_2-1},
\]

\[
\mathcal G_B:=N10^{n_2}-M10^{n_3-1}.
\]

则

\[
\boxed{
\alpha t\,\mathcal G_A
=
Q_0+\alpha JZ-P_3(1+10^{n_2-1}).
}
\tag{ZGAP-A}
\]

\[
\boxed{
10\alpha t\,\mathcal G_B
=
P_3(10^{n_2+1}+1)-Q_0-\alpha JZ.
}
\tag{ZGAP-B}
\]

这正是此前 SRCU/Smith-reduced report 所缺的“\(Z\) 进入 radial slack”的 exact bridge。

## 1.7 NEW PROVED — Integer-Radial Margin in Smith Gap Coordinates

若 Face A 中存在任何 integer \(U\in I_{23}\)，则

\[
\boxed{\mathcal G_A\ge M.}
\tag{IRM-A}
\]

若 Face B 中存在任何 integer \(U\in I_{23}\)，则

\[
\boxed{\mathcal G_B\ge N.}
\tag{IRM-B}
\]

因此：

\[
0<\mathcal G_A<M\Longrightarrow N_{\rm raw}=0,
\]

\[
0<\mathcal G_B<N\Longrightarrow N_{\rm raw}=0.
\]

这把旧 Sharp Integer Radial Margin 变成了最适合与 \(Z\)-bridge 联立的形式。

## 1.8 NEW PROVED — Endpoint Euclidean Layer Cancels the Smith gcd Factor

对 \(i=2,3\) 写

\[
10^{n_i-1}g_i=q_iP_i+r_i,
\qquad0\le r_i<P_i.
\]

因为 \(P_i=g_iC_i\)，自动有 \(g_i\mid r_i\)。约去 \(g_i\) 后就是

\[
\boxed{
10^{n_i-1}=q_iC_i+r_i',
\qquad0\le r_i'<C_i.
}
\tag{END-EUC}
\]

从而

\[
\boxed{
\left\lceil L_i\right\rceil
=q_i+\mathbf 1_{r_i'>0}.
}
\]

所以所谓“第三 Euclidean layer”确实存在，但其本质是 **decimal power 对 primitive numerator core \(C_i\) 的普通 Euclidean division**；\(g_i\) 本身精确消掉。它直接读取 endpoint location，但不自动与 DES 的 leading/tail quotient 同步。

## 1.9 FINAL VERDICT

本轮没有得到

\[
N_V(I_{23})=0
\]

的 uniform proof。

但是剩余 frontier 已可压成两个 explicit successor cases：

### Face A

\[
I_{23}=
\left[
\frac{u_0 10^{n_2-1}}M,
\frac{u_0 10^{n_3}}N
\right),
\]

\[
\mathcal G_A=M10^{n_3}-N10^{n_2-1}>0,
\]

需要证明

\[
\boxed{
\operatorname{next}_V\!\left(\frac{u_0 10^{n_2-1}}M\right)
\ge
\frac{u_0 10^{n_3}}N.
}
\tag{SUCC-A}
\]

### Face B

\[
I_{23}=
\left[
\frac{u_0 10^{n_3-1}}N,
\frac{u_0 10^{n_2}}M
\right),
\]

\[
\mathcal G_B=N10^{n_2}-M10^{n_3-1}>0,
\]

需要证明

\[
\boxed{
\operatorname{next}_V\!\left(\frac{u_0 10^{n_3-1}}N\right)
\ge
\frac{u_0 10^{n_2}}M.
}
\tag{SUCC-B}
\]

因此本轮达到的是 prompt 的 **Level 7 — Final radial normal form**，并额外建立了 DES/Smith 到 radial width 的 exact coupling；尚未达到 A1 closure。

---

# 2. Frozen Seven-Round Results

以下作为 frozen inputs，不在本报告重复证明。

## 2.1 Primitive sphere

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

\(Q_0\) 为 odd。

## 2.2 Exponent normal form

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
\tag{EXP}
\]

对 \(g\ge1\)：

\[
d\le-1\Rightarrow\text{plus},
\qquad
d\ge2\Rightarrow\text{minus},
\]

transition 只剩 \(d=0,1\)。

## 2.3 Exact word core

\[
D=P_110^k-Q_0>0,
\]

\[
H=b_2Q_0-b_110^{m_2}D\ne0.
\]

plus iff \(H<0\)，minus iff \(H>0\)。

\[
b_1P_110^{m_2+k}=Q_0Q_{12}-H,
\]

\[
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbf Z_{>0},
\]

\[
\boxed{b_2P_2=10^gH+K_3.}
\]

等价：

\[
\boxed{
10^{m_3}H
=b_2P_210^{n_3}-b_3(Q_0-P_3).
}
\tag{H3}
\]

## 2.4 Full Smith determinant

\[
b_1=s\alpha u,
\quad b_2=s\alpha\beta t,
\quad b_3=s\beta v,
\]

\[
\alpha,\beta,\gamma\text{ pairwise coprime},
\qquad
\gamma=\gcd(u,v).
\]

\[
\Sigma_b
=\alpha\beta_0\gamma_0
\mid Q_0,
\]

\[
s\Sigma_b\mid H.
\]

所有进入 \(\Sigma_b\) 的 odd ten-free primes 均 \(\equiv1\pmod4\)。

## 2.5 Iterated Smith defect

\[
\widehat R=\alpha t10^{n_3}-v,
\qquad
R=s\beta\widehat R.
\]

\[
H=s\alpha\beta^\sharp v^\sharp Z,
\qquad Z\ne0.
\]

\[
tM10^{n_3}-A_3=JZ,
\qquad A_3=(Q_0-P_3)/\alpha.
\]

\[
\boxed{
\frac{\alpha J}{M_H^{(2)}}=\frac1{\beta_3},
\qquad
M_H^{(2)}=s\alpha\beta^\sharp v^\sharp.
}
\]

\[
\boxed{
S_3=P_2+P_3-Q_0
=\alpha JZ-M\widehat R.
}
\]

## 2.6 Common-\(U\) semantics

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

合法 numerator blocks 要求

\[
10^{n_i-1}\le UC_i<10^{n_i}.
\]

reconstruction theorem 已证明：上述 exact primitive/word/gcd state 加合法 coprime \(U\) 足以恢复 original A1 candidate。

---

# 3. Exact Radial Gate

只保留 block \(2,3\)：

\[
I_2=\left[\frac{10^{n_2-1}}{C_2},\frac{10^{n_2}}{C_2}\right),
\]

\[
I_3=\left[\frac{10^{n_3-1}}{C_3},\frac{10^{n_3}}{C_3}\right).
\]

因为每个 interval 都是 \([L_i,10L_i)\)，只有两个 active face：

\[
\boxed{
I_{23}
=
[\max(L_2,L_3),10\min(L_2,L_3)).
}
\tag{I23}
\]

合法 candidate 当且仅当

\[
\exists U\in I_{23}\cap\mathbf Z_{>0},
\qquad\gcd(U,V)=1.
\]

定义

\[
N_V(I)=\#\{u\in I\cap\mathbf Z_{>0}:\gcd(u,V)=1\}.
\]

最终目标：

\[
\boxed{N_V(I_{23})=0.}
\]

---

# 4. Smith Terminal Coordinates

写

\[
u=\gamma u_0,
\qquad
v=\gamma v_0.
\]

由 full Smith LCM：

\[
V=s\alpha\beta\gamma u_0tv_0.
\]

因此

\[
g_1=\beta tv_0,
\quad
g_2=u_0v,
\quad
g_3=u_0\alpha t.
\]

令

\[
P_2=vM,
\qquad
P_3=\alpha tN.
\]

由于 \(g_2\mid P_2\)、\(g_3\mid P_3\)：

\[
u_0\mid M,N.
\]

于是

\[
C_2=M/u_0,
\qquad
C_3=N/u_0.
\]

并可重写

\[
\boxed{V=s\beta u_0v\alpha t.}
\tag{V-SR}
\]

合法 \(U\) 满足

\[
\gcd(U,u_0)=1,
\qquad
\gcd(U,s\beta v\alpha t)=1.
\]

所以 \(U/u_0\) 是 lowest terms、denominator 恰为 \(u_0\) 的 reduced rational。

**状态：PROVED / inherited + re-audited.**

---

# 5. Re-Derivation of \(I_{23}\)

由 (SR-C)：

\[
I_2
=u_0\left[\frac{10^{n_2-1}}M,\frac{10^{n_2}}M\right),
\]

\[
I_3
=u_0\left[\frac{10^{n_3-1}}N,\frac{10^{n_3}}N\right).
\]

定义

\[
K_{MN}:=
\left[
\max\left(\frac{10^{n_2-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{n_2}}M,\frac{10^{n_3}}N\right)
\right).
\]

则

\[
\boxed{I_{23}=u_0K_{MN}.}
\tag{KMN}
\]

等价 radial semantic：

\[
\boxed{
\frac U{u_0}\in K_{MN},
\qquad
\gcd(U,s\beta u_0v\alpha t)=1.
}
\tag{SRUS}
\]

这就是本轮使用的 Smith-reduced successor form。

---

# 6. Active Radial Faces

定义

\[
R_U=C_210^{n_3-1}-C_310^{n_2-1}.
\]

注意：prompt 中 active-face 与 \(R_U\) 的符号写反了。

因为

\[
L_2-L_3
=
\frac{C_310^{n_2-1}-C_210^{n_3-1}}{C_2C_3}
=-\frac{R_U}{C_2C_3},
\]

所以：

### Face A

\[
\boxed{L_2\ge L_3\iff R_U\le0.}
\]

此时

\[
\boxed{
I_{23}
=\left[L_2,10L_3\right)
=\left[
\frac{u_010^{n_2-1}}M,
\frac{u_010^{n_3}}N
\right).
}
\tag{FACE-A}
\]

### Face B

\[
\boxed{L_3>L_2\iff R_U>0.}
\]

此时

\[
\boxed{
I_{23}
=\left[L_3,10L_2\right)
=\left[
\frac{u_010^{n_3-1}}N,
\frac{u_010^{n_2}}M
\right).
}
\tag{FACE-B}
\]

**状态：NEW PROVED / prompt sign corrected.**

---

# 7. Radial Slack

定义

\[
A_U=C_310^{n_2-1},
\qquad
B_U=C_210^{n_3-1},
\qquad
W_U=C_2C_3.
\]

则

\[
I_{23}
=\left[
\frac{\max(A_U,B_U)}{W_U},
\frac{10\min(A_U,B_U)}{W_U}
\right).
\]

定义

\[
G_U=10\min(A_U,B_U)-\max(A_U,B_U).
\]

于是：

- \(G_U\le0\)：continuous radial intersection empty；
- \(G_U>0\)：continuous overlap exists；
- exact width \(=G_U/W_U\)。

在 Smith coordinates 中：

### Face A

\[
\mathcal G_A=M10^{n_3}-N10^{n_2-1},
\]

\[
\boxed{G_U=\mathcal G_A/u_0,}
\]

\[
\boxed{
|I_{23}|=\frac{u_0\mathcal G_A}{MN}.
}
\tag{WIDTH-A}
\]

### Face B

\[
\mathcal G_B=N10^{n_2}-M10^{n_3-1},
\]

\[
\boxed{G_U=\mathcal G_B/u_0,}
\]

\[
\boxed{
|I_{23}|=\frac{u_0\mathcal G_B}{MN}.
}
\tag{WIDTH-B}
\]

这两个整数 \(\mathcal G_A,\mathcal G_B\) 是本轮真正适合接 DES/Smith 的 radial gap coordinates。

---

# 8. Numerator Radial Resonance \(R_U\)

\[
R_U=C_210^{n_3-1}-C_310^{n_2-1}.
\]

其 Smith-reduced version：

\[
\boxed{
\widetilde R_U:=u_0R_U
=M10^{n_3-1}-N10^{n_2-1}.
}
\tag{RU-SR}
\]

因此 \(R_U\) 只读取 \((M,N,u_0;n_2,n_3)\)，而不显式读取 \(\alpha,\beta,\gamma,t,v_0\)。

另外

\[
\boxed{
R_U=0
\iff
\frac{M}{N}=10^{n_2-n_3}.
}
\]

此时 \(L_2=L_3\)，real interval 为 \([L,10L)\)，在 continuous sense 是最大 overlap；但 integer/coprime feasibility仍完全未自动保证。

---

# 9. Relation Between \(R_U\) and DES/Smith Variables

## 9.1 \(R_U\)-\(H\) bridge

由 \(VC_2=b_2P_2\)、\(VC_3=b_3P_3\)：

\[
VR_U=b_2P_210^{n_3-1}-b_3P_310^{n_2-1}.
\]

结合 (H3) 得：

\[
\boxed{
10VR_U
=
10^{m_3}H+b_3\bigl(Q_0-P_3(1+10^{n_2})\bigr).
}
\]

**状态：NEW PROVED.**

## 9.2 Face A radial-gap bridge

\[
\boxed{
VG_A
=
10^{m_3}H
+b_3\bigl(Q_0-P_3(1+10^{n_2-1})\bigr).
}
\]

## 9.3 Face B radial-gap bridge

\[
\boxed{
10VG_B
=
-10^{m_3}H
+b_3\bigl(P_3(10^{n_2+1}+1)-Q_0\bigr).
}
\]

## 9.4 Smith-\(Z\) bridge

第七轮 DS2：

\[
JZ=tM10^{n_3}-\frac{Q_0-P_3}{\alpha}.
\]

乘 \(\alpha\)，并用 \(P_3=\alpha tN\)：

\[
\boxed{
Q_0+\alpha JZ=\alpha t(M10^{n_3}+N).
}
\]

于是：

\[
\boxed{
\alpha t\mathcal G_A
=Q_0+\alpha JZ-P_3(1+10^{n_2-1}),
}
\]

\[
\boxed{
10\alpha t\mathcal G_B
=P_3(10^{n_2+1}+1)-Q_0-\alpha JZ.
}
\]

这是本轮最重要的 exact coupling。

### Sign-sensitive interpretation

plus 中 \(Z<0\)。Face A：

\[
\alpha t\mathcal G_A
=
\underbrace{Q_0-P_3(1+10^{n_2-1})}_{>0\ \text{in plus}}
-\alpha J|Z|.
\tag{A+}
\]

minus 中 \(Z>0\)。Face B：

\[
10\alpha t\mathcal G_B
=
\underbrace{P_3(10^{n_2+1}+1)-Q_0}_{>0\ \text{for a surviving Face B}}
-\alpha JZ.
\tag{B-}
\]

所以最有 hope 的短-interval cancellation faces 是：

\[
\boxed{\text{plus + Face A}}
\]

和

\[
\boxed{\text{minus + Face B}}.
\]

另外两种 face/sign 组合中 \(\alpha J|Z|\) 以加法进入 gap，不能期待 Smith-rich 自动压短 interval。

---

# 10. Smith-Rich Definition

本轮不再用未归一化的“\(M_H^{(2)}\) 大/小”。最自然的 richness 是相对当前 branch 的 \(H\)-envelope。

定义

\[
B_H=
\begin{cases}
Q_0,&\text{plus},\\
Q_0,&\text{minus},\ d=0,\\
10Q_0,&\text{minus},\ d=1,\\
10^dQ_0,&\text{minus},\ d\ge2.
\end{cases}
\]

其中 plus 有 sharp \(|H|<Q_0\)，generic large-\(d\) minus 有 \(H<10^dQ_0\)。

定义 requested richness：

\[
\boxed{
\mathcal S_Z:=\frac{M_H^{(2)}}{B_H}.
}
\]

若采用最近一次 Smith-reduced audit 的 strongest divisor

\[
\mathcal M_{\max}
=s\alpha\beta^\sharp v^\sharp h_T^\sharp\mid H,
\]

则更强地定义

\[
\boxed{
\mathcal S_q:=\frac{\mathcal M_{\max}}{B_H}.
}
\]

前者控制 \(Z\)，后者控制 final quotient \(q=H/\mathcal M_{\max}\)。

**状态：DEFINITION / canonicalized.**

---

# 11. Smith-Rich \(Z\)-Compression

由

\[
H=M_H^{(2)}Z
\]

立即：

\[
|Z|<\frac{B_H}{M_H^{(2)}}.
\]

所以对任意正整数 \(C\)：

\[
\boxed{
M_H^{(2)}>\frac{B_H}{C+1}
\Longrightarrow
1\le|Z|\le C.
}
\tag{FZ}
\]

特别：

\[
M_H^{(2)}>B_H/2
\Longrightarrow
|Z|=1.
\]

plus 还能更 sharp。由 (MNZ) 与 \(Z<0\)：

\[
Q_0=\alpha t(M10^{n_3}+N)+\alpha J|Z|.
\]

所以

\[
\alpha J|Z|<Q_0.
\]

而

\[
\alpha J=\frac{M_H^{(2)}}{\beta_3}.
\]

故

\[
\boxed{|H|=M_H^{(2)}|Z|<\beta_3Q_0.}
\tag{PLUS-H-SHARP}
\]

因此 plus 中甚至可用 \(B_H^+=\beta_3Q_0\)。

若

\[
M_H^{(2)}\ge\beta_3Q_0,
\]

plus 直接 impossible；若

\[
M_H^{(2)}>\beta_3Q_0/2,
\]

则

\[
\boxed{Z=-1.}
\]

**状态：NEW DERIVED / finite-\(Z\) theorem.**

但 finite \(Z\) 并未自动 finite-ize \((M,N,u_0)\)，因此不等于 radial closure。

---

# 12. Smith-Rich Interval Bounds

关键校准：

\[
C_2=M/u_0,
\qquad C_3=N/u_0.
\]

所以任何形式的

\[
\Sigma_b\text{ large}
\]

或

\[
M_H^{(2)}\text{ large}
\]

都不会作为一个显式 multiplicative factor直接进入 \(L_2,L_3\)。

因此 conjecture

\[
\text{“Smith-rich 自动 }|I_{23}|<1”
\]

目前**不能**从 Smith magnitude 推出。

真正可证明的是 sign-sensitive necessary inequalities。

### plus + Face A + raw integer survivor

由 (A+) 与 \(\mathcal G_A\ge M\)：

\[
\boxed{
Q_0-P_3(1+10^{n_2-1})
\ge
\alpha tM+\alpha J|Z|.
}
\tag{A+-INT}
\]

这严格强于 plain plus collapse

\[
Q_0>P_3(1+10^{n_2-1}).
\]

### minus + Face B + raw integer survivor

由 (B-) 与 \(\mathcal G_B\ge N\)：

\[
\boxed{
P_3(10^{n_2+1}+1)-Q_0
\ge
10\alpha tN+\alpha JZ.
}
\tag{B--INT}
\]

这是 radial integer margin 真正进入 affine Smith equation 后得到的 strengthened inequality。

**状态：NEW PROVED NECESSARY CONDITIONS / not yet contradiction.**

---

# 13. Smith-Rich Coprime Coverage

本轮没有得到一个 uniform “Smith-rich \(\Rightarrow\) CRT cover” theorem。

原因：

1. rich divisor 的 prime factors主要控制 \(H,Z\)；
2. radial endpoint位置由 \(M,N,u_0\) 控制；
3. full Smith factors \(v,\alpha t\) 从 radial ratio 中 exact cancel；
4. 在没有先将 \(N_{\rm raw}\) 压到小常数前，prime coverage只是无位置的 density statement。

因此：

\[
\boxed{
\textbf{Smith-rich should first be used to constrain }Z/q\textbf{ and }\mathcal G_{A/B},
}
\]

而不是先做 generic Jacobsthal/CRT。

**状态：OPEN / strategy narrowed.**

---

# 14. Smith-Poor Definition

与 rich 对偶，定义 Smith-poor 为：

\[
\mathcal S_Z\ll1
\]

以及（若用 strongest divisor）

\[
\mathcal S_q\ll1.
\]

但本轮的 Smith–radial cancellation 给出一个重要修正：

\[
\boxed{
\text{Smith-poor 更自然意味着 large transverse unit modulus，}
}
\]

而不一定意味着 radial denominator \(u_0\) 大或 interval 自动短。

pair \((2,3)\) 的 exact duality：

\[
\gcd(b_2,b_3)\operatorname{lcm}(g_2,g_3)=V.
\]

这里

\[
\operatorname{lcm}(g_2,g_3)=u_0v\alpha t.
\]

但 \(v\alpha t\) 从 endpoints 中 exact cancel；它只留在 \(U\)-unit sieve 中。

所以“poor overlap \(\Rightarrow\) short interval”不是一般 magnitude theorem。

---

# 15. \(\Sigma_b=1\) Normal Form

\[
\Sigma_b=\alpha\beta_0\gamma_0=1
\]

严格推出：

\[
\alpha=1,
\]

且 \(\beta,\gamma\) 的 prime supports 都包含于 \(\{2,5\}\)。又因 \(\gcd(\beta,\gamma)=1\)，两者的 \(2/5\)-supports disjoint。

精确分类：

- 若 \(\beta,\gamma\) 都 nontrivial，则一个只能是 pure \(2\)-power，另一个只能是 pure \(5\)-power；
- 若其中一个为 \(1\)，另一个可以是任意 \(2^a5^b\)。

但必须强调：

\[
\boxed{
\Sigma_b=1\not\Rightarrow \operatorname{rad}(V)\subseteq\{2,5\}.
}
\]

因为 residual factors

\[
s,u_0,t,v_0
\]

仍可含 arbitrary odd primes。

所以把 \(\Sigma_b=1\) 直接重写成“\(V\) 主要是 \(2,5\)-smooth”是错误的。

**状态：NEW AUDIT / prompt simplification corrected.**

---

# 16. Smith-Poor Radial Alignment

在 Smith-poor chamber，目前真正需要证明的不是 density，而是 endpoint alignment：

Face A：

\[
m_A:=\left\lceil\frac{u_010^{n_2-1}}M\right\rceil,
\]

Face B：

\[
m_B:=\left\lceil\frac{u_010^{n_3-1}}N\right\rceil.
\]

若 interval short，则只需研究这些 endpoint quotients 及后续少数整数 modulo \(V\)。

由于 backward radial redundancy 已证明 DES/WGF/phase 对 \(U\) 不提供独立 residue，Smith-poor 的最终刀口只能来自：

\[
\boxed{
\text{exact endpoint quotient/remainder}
+\text{terminal restrictions on }M,N,u_0.
}
\]

本轮尚未证明这些 quotients 被固定到 forbidden residue classes。

**状态：OPEN.**

---

# 17. Radial Endpoint Euclidean Division

对 \(i=2,3\)：

\[
10^{n_i-1}=q_iC_i+r_i',
\qquad0\le r_i'<C_i.
\]

于是

\[
\left\lceil L_i\right\rceil
=q_i+\mathbf1_{r_i'>0}.
\]

如果 \(L_i\) 是 active lower face，令

\[
U_{i,\min}:=\lceil L_i\rceil.
\]

定义 active numerator excess

\[
e_i:=U_{i,\min}C_i-10^{n_i-1}.
\]

则

\[
0\le e_i<C_i.
\]

对于任一 actual common \(U\)：

\[
UC_2=10^{n_2-1}+e_2,
\qquad
UC_3=10^{n_3-1}+e_3.
\]

消去 \(U\)：

\[
\boxed{
C_3e_2-C_2e_3
=R_U.
}
\tag{RAD-EXCESS}
\]

这条式子 exact，但它是 common-\(U\) 本身的重写，不是一个独立 gate。

endpoint integrality：

\[
L_i\in\mathbf Z
\iff
C_i\mid10^{n_i-1}.
\]

所以只有当 \(C_i\) 为 \(2,5\)-smooth divisor of \(10^{n_i-1}\) 时 lower endpoint integer。

**状态：PROVED / useful normalization, no closure yet.**

---

# 18. Candidate Integer Count

一般精确公式：

\[
\boxed{
N_{\rm raw}
=
\max(0,\lceil R_{23}\rceil-\lceil L_{23}\rceil).
}
\]

在两个 face 中：

### Face A

\[
\boxed{
N_{\rm raw}^{A}
=
\max\left(
0,
\left\lceil\frac{u_010^{n_3}}N\right\rceil
-
\left\lceil\frac{u_010^{n_2-1}}M\right\rceil
\right).
}
\tag{NRAW-A}
\]

### Face B

\[
\boxed{
N_{\rm raw}^{B}
=
\max\left(
0,
\left\lceil\frac{u_010^{n_2}}M\right\rceil
-
\left\lceil\frac{u_010^{n_3-1}}N\right\rceil
\right).
}
\tag{NRAW-B}
\]

目前没有证明 global \(N_{\rm raw}\le1,2,3\)。此前 moving-profile analysis 已说明 interval width 不会仅因 \(Q_0\to\infty\) 自动变成 \(<1\)。本轮的新 Smith cancellation 也没有改变这一点。

**状态：GLOBAL SMALL-CONSTANT RAW BOUND OPEN.**

---

# 19. Coprime Successor

定义

\[
\operatorname{next}_V(L)
=
\min\{u\ge L:u\in\mathbf Z_{>0},\ \gcd(u,V)=1\}.
\]

则：

### Face A

\[
\boxed{
\operatorname{next}_V\left(\frac{u_010^{n_2-1}}M\right)
\ge
\frac{u_010^{n_3}}N
}
\]

是 closure 所需 exact theorem。

### Face B

\[
\boxed{
\operatorname{next}_V\left(\frac{u_010^{n_3-1}}N\right)
\ge
\frac{u_010^{n_2}}M.
}
\]

等价的 integer strip form：

令

\[
A_{\max}=\max(A_U,B_U),
\quad
A_{\min}=\min(A_U,B_U),
\quad
W=C_2C_3.
\]

raw candidates 恰为

\[
\boxed{
\mathcal U_{\rm raw}
=
\{u\in\mathbf Z_{>0}:A_{\max}\le Wu\le10A_{\min}-1\}.
}
\tag{RAW-STRIP}
\]

closure 即证明这些 integers 全部与 \(V\) 有非平凡 gcd。

---

# 20. Killer-Prime Ledger

本轮对现有 exact synchronized regression states 重新计算 radial gate。

结果：当前已知 exact word/Smith regression states 全部在：

- **Layer C**：continuous interval empty；或
- **Layer I**：continuous interval nonempty，但没有 positive integer；

死亡。

当前没有发现一个 exact terminal regression state 满足

\[
N_{\rm raw}>0,
\qquad
N_V=0.
\]

也就是说：

\[
\boxed{
\textbf{当前 killer-prime ledger 在真正 Layer-P 上是空的。}
}
\]

这不是 global theorem，但对研究资源分配非常重要：在找到 Level-P survivor 前，泛 CRT / Jacobsthal covering 尚不是最强 empirical mechanism；目前最常见 killer 是 interval geometry / integer location 本身。

**状态：EXPERIMENTAL / exact regression.**

---

# 21. \(d=0\) Chamber

\[
m_2=g,
\qquad
n_2=2g+k.
\]

本轮新 radial formulas 仍然全部适用。

在 \(d=0\) 中 \(H\) 的两种 sign 都可能发生；若 minus，则 canonical borrow \(c=1\)。

Smith-rich 可把 \(Z\) 或 stronger quotient \(q\) 压成 finite set，但 (ZGAP-A/B) 仍含 moving \(M,N,u_0\)。因此：

\[
\boxed{d=0\text{ 尚未 radial-closed}.}
\]

真正需要的新信息是对 \(M/N\) 或 endpoint quotient 的定位，而不是继续精化 denominator ratio \(\sigma\)：full Smith substitution 后 \(\sigma\) 在 radial ratio 中精确消掉。

**状态：OPEN.**

---

# 22. \(d=1\) Plus Chamber

第七轮已有：\(d=1\), plus 的 sign mismatch/local tail 约束很强，并有额外 lower bounds on denominator residual parameters。

但 full Smith cancellation 说明：这些 denominator-ratio restrictions 不会自动变成 \(\rho_U\) boundary restriction。

plus + Face A 时：

\[
\alpha t\mathcal G_A
=Q_0-P_3(1+10^{n_2-1})-\alpha J|Z|.
\]

若 integer survivor存在：

\[
Q_0-P_3(1+10^{n_2-1})
\ge\alpha tM+\alpha J|Z|.
\]

这是一条真正使用 radial gate 的 d=1-plus necessary inequality，但本轮未把 RHS 推到超过 LHS。

**状态：OPEN / substantially sharpened.**

---

# 23. Large-\(d\) Minus Chamber

对 \(g\ge1,d\ge2\)：

\[
H\asymp10^dQ_0,
\qquad Z>0.
\]

若 \(M_H^{(2)}\) rich relative to \(10^dQ_0\)，则 finite \(Z\)。若使用 strongest divisor \(\mathcal M_{\max}\)，则 finite final quotient \(q\)。

AFF：

\[
S_3=\alpha JZ-M\widehat R
\]

确实要求大项 cancellation，但单独 integer linear form spacing 仍不足，因为 \(|S_3|\) 本身可为 \(Q_0\)-scale，而 coefficients/variables均 moving。

新贡献是：同一个 \(Z\) 现在也进入 (ZGAP-A/B)，所以 large-\(d\) cancellation 不再只是一条 word equation；它同时必须与 radial gap positivity、integer margin相容。

目前仍未得到 contradiction。

**状态：OPEN.**

---

# 24. Denominator Resonance \(R\)

\[
R=b_210^{n_3}-b_3.
\]

\(R=0\) 已知推出：

\[
d=0,
\qquad
b_3=b_210^{n_3},
\qquad
g_2=10^{n_3}g_3.
\]

在 Smith coordinates 中可取

\[
\alpha=t=1,
\qquad
v=10^{n_3}.
\]

本轮没有证明 denominator resonance 本身 radial-impossible。

**状态：OPEN.**

---

# 25. Double Resonance \(R=R_U=0\)

若同时

\[
R=0,
\qquad
R_U=0,
\]

则

\[
g_2=10^{n_3}g_3,
\]

以及

\[
\frac{C_2}{C_3}=10^{n_2-n_3}.
\]

所以

\[
\boxed{
\frac{P_2}{P_3}=10^{n_2}.
}
\]

在 resonance 的 \(d=0\) 下

\[
n_2=2g+k,
\]

因此

\[
\boxed{P_2=10^{2g+k}P_3.}
\tag{DR}
\]

代入 sphere：

\[
\boxed{
P_1^2+(10^{4g+2k}+1)P_3^2=Q_0^2.
}
\]

等价：

\[
\boxed{
(Q_0-P_1)(Q_0+P_1)
=(10^{4g+2k}+1)P_3^2.
}
\tag{DR-F}
\]

这是 strong exact reduction，但**尚不能**据此宣布 double resonance impossible。该二次型本身存在 rational/integer families；需要继续使用 exact A1 word/Smith constraints。

因此 prompt conjecture

\[
R=R_U=0\Longrightarrow\bot
\]

本轮状态是：

\[
\boxed{\textbf{OPEN, not proved.}}
\]

---

# 26. Cyclotomic Common-Gap Input

冻结已有：若 suitable shared odd prime power同时进入旧 common gaps，则

\[
p^e\mid10^{2(g+k)}+1.
\]

本轮没有把它升级成 radial closure，因为：

1. radial endpoints 读取 \(M,N,u_0\)；
2. shared gap primes主要位于 transverse Smith channels；
3. 尚未出现一个必须由这些 primes 覆盖的 small raw-candidate list。

因此 cyclotomic restriction 保留为 branch sieve，不单独研究 factorization。

**状态：DERIVED TOOLKIT ONLY.**

---

# 27. Exact \(U\)-Residue Attempts

reconstruction/backward audit 给出关键 negative result：

\[
\boxed{
\text{all audited DES/WGF/phase equations are radial-equivariant in }U.
}
\]

所以没有合法推导：

\[
\text{DES alone}\Rightarrow p\mid U.
\]

若要得到 forced common divisor of \(U\)，必须通过 active endpoint quotient：

\[
U_*=\lceil L_{23}\rceil
\]

及其 Euclidean remainder。

对 actual candidate：

\[
U\equiv (10^{n_i-1}+e_i)C_i^{-1}\pmod p
\]

只有在 \(p\nmid C_i\) 且另有 theorem 强制

\[
e_i\equiv-10^{n_i-1}\pmod p
\]

时才能得到 \(p\mid U\)。本轮未找到这样的 uniform theorem。

**状态：FAILED AS DIRECT DES ROUTE / endpoint route OPEN.**

---

# 28. CRT / Short-Cover Arguments

若未来证明

\[
N_{\rm raw}\le C
\]

for small absolute \(C\)，则可 exact 检查

\[
m,m+1,\ldots,m+C-1
\]

的 gcd。

对于 Smith determinant 的 nondecimal odd primes：

\[
p\equiv1\pmod4,
\qquad p\ge13.
\]

所以在长度 \(<13\) 的 run 中，每个此类 prime至多杀一个 candidate；dense coverage主要还需 \(2,5\) 或 residual small primes。

但 residual \(s,u_0,t,v_0\) 可含 \(3,7,11,\ldots\)，因此不能只按 \(\alpha,\beta,\gamma\) 三个 channels 做一个 universal three-candidate cover。

本轮没有得到 global small-\(C\) theorem，故不启动 general Jacobsthal machinery。

**状态：CONDITIONAL TOOLKIT.**

---

# 29. Computational Experiments

本轮实验只做 radial gate，使用 exact integer/Fraction arithmetic。

## 29.1 Existing \((b_1,b_2,b_3)=(1,6,8)\), \(V=24\) synchronized states

profile：

\[
g=0,\quad k=1,\quad m_2=m_3=n_3=1,\quad n_2=2.
\]

### State A

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169).
\]

\[
C_2=13,\quad C_3=53.
\]

continuous interval empty。Layer C dead。

### State B

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445).
\]

\[
C_2=109,\quad C_3=25.
\]

\[
I_{23}=[10/109,2/5).
\]

real overlap survives，但 \(R_{23}<1\)，无 positive integer。Layer I dead。

### State C

\[
(P_1,P_2,P_3,Q_0)=(456,292,2907,2957).
\]

\[
C_2=73,\quad C_3=969.
\]

continuous interval empty。Layer C dead。

## 29.2 NEW exact boundary regression

同 denominator/profile 还发现：

\[
\boxed{
(P_1,P_2,P_3,Q_0)=(552,3796,2847,4777).
}
\]

检查：

- primitive sphere：exact；
- exact master：exact；
- canonical gcd profile：exact；
- \(D=743>0\)；
- \(H=21232\ne0\)；
- \(R=52\)；
- \(C_2=C_3=949\)。

于是

\[
L_2=10/949,
\qquad
L_3=1/949,
\]

\[
R_{23}=10/949=L_{23}.
\]

即

\[
\boxed{G_U=0.}
\]

这是一个 fully synchronized sphere/master/Smith ambient state 恰好落在 radial continuous boundary 的 exact regression point。

在 Smith variables：

\[
M=N=949,
\qquad
J=5,
\qquad
Z=5308,
\]

并且 (ZGAP-A) 的 RHS 精确为零。

这验证了本轮 radial-gap bridge 的 endpoint convention，也说明 terminal arithmetic 可以逼到 \(G_U=0\) boundary；不能假设存在一个 uniform positive real slack margin。

## 29.3 Another denominator pattern

\[
(b_1,b_2,b_3)=(5,5,1),
\qquad V=5,
\]

存在 synchronized state

\[
(P_1,P_2,P_3,Q_0)=(298,2514,1485,2935),
\]

\[
C_2=2514,\quad C_3=297.
\]

real overlap存在但 entire interval位于 \((0,1)\)，仍是 Layer I dead。

## 29.4 \(g=1,d=0\) small regression

在 profile

\[
g=1,n_3=1,m_3=2,m_2=1,k=1,n_2=3
\]

的小范围 exact scan 中，出现 primitive state

\[
(P_1,P_2,P_3,Q_0)=(32,264,123,293)
\]

对应 denominator realizations \((5,5,10)\) / \((7,7,14)\)，但 radial continuous cone即死亡。

## 29.5 Current empirical verdict

当前 exact regression set：

\[
\boxed{\text{C / I / C / boundary-C / I / C}.}
\]

没有发现真正 Layer-P state：

\[
N_{\rm raw}>0,
\qquad N_V=0.
\]

更没有发现 \(N_V>0\) 的 full terminal survivor。

**状态：EXPERIMENTAL；不用于 global nonexistence。**

---

# 30. Explicit Counterexamples / Regression Points

本轮应永久保留三类 negative witnesses。

## 30.1 Exact-word + Smith does not imply real radial feasibility

State A/C 以及已知 fixed-profile infinite pseudo-family均在 Layer C 死亡。

## 30.2 Real radial feasibility does not imply integer radial feasibility

State B 与旧 real-cone point说明

\[
I_{23}\ne\varnothing
\]

仍可 entire below \(1\)。

## 30.3 Terminal arithmetic can hit radial boundary exactly

新 state

\[
(552,3796,2847,4777),\quad(b_1,b_2,b_3)=(1,6,8)
\]

满足

\[
G_U=0.
\]

因此不能建立一个不使用 integer/coprime location 的 uniform positive slack theorem。

---

# 31. Failed Conjectures

以下逐项给出本轮裁决。

### “Smith-rich 自动使 \(|I_{23}|<1\)”

**FAILED AS DIRECT MECHANISM / NOT PROVED GLOBALLY.**

原因：full Smith substitution 后大部分 Smith factors从 endpoints exact cancel；richness只能通过 \(M,N,u_0,Z\) 间接作用。

### “Smith-poor 自动使 \(|R_U|\) 很大”

**FAILED AS GENERIC MAGNITUDE ROUTE.**

\(R_U\) 只读取 \(M,N,u_0\)，transverse Smith magnitude可消掉。

### “\(\Sigma_b=1\) 自动容易关闭”

**FAILED.**

\(\Sigma_b=1\) 只清空 three-channel ten-free content；residual \(s,u_0,t,v_0\) 仍可含 arbitrary odd primes。

### “\(\lceil L_{23}\rceil\) 总与 \(V\) 不互素”

**NOT ESTABLISHED / no theorem.**

现有 exact regressions甚至尚未进入 Layer P，无法支持该 universal claim。

### “raw candidate count 总 \(\le1\)”

**FAILED AS GENERIC MOVING-PROFILE INFERENCE.**

已有理论说明 moving width 不会仅因 height 自动收缩；本轮未得到新的 uniform bound。

### “\(R_U=0\) impossible”

**OPEN.**

未证明；其 algebraic consequence本身并不矛盾。

### “double resonance \(R=R_U=0\) impossible”

**OPEN.**

已压到 (DR-F)，尚缺 word/Smith contradiction。

### “\(d=0\) radial chamber automatically empty”

**FAILED / contradicted by real-cone ambient behavior.**

不能从 \(d=0\) alone 关闭。

### “Smith odd primes can cover all candidate \(U\)”

**FAILED AS STANDALONE GENERAL ROUTE.**

没有 small raw-count theorem，也不能忽略 residual prime channels。

### “DES gives a forced divisor of \(U\)”

**FAILED AS DIRECT ROUTE.**

backward/common-\(U\) audit 已证明 audited word/phase relations radial-homogeneous；只能通过 endpoint location重新进入 \(U\)。

---

# 32. New Proven Lemmas

本轮新增、可冻结到下一轮的 theorem list：

1. **A1-ISR-1 — Full Smith–Radial Cancellation**
   \[
   C_2=M/u_0,\quad C_3=N/u_0.
   \]

2. **A1-ISR-2 — Correct Radial-Face Sign**
   \[
   L_2\ge L_3\iff R_U\le0.
   \]

3. **A1-ISR-3 — Integer Radial Gap Normal Form**
   \[
   |I_{23}|=G_U/(C_2C_3).
   \]

4. **A1-ISR-4 — Radial Slack Identity**
   \[
   G_U=9\min(A_U,B_U)-|R_U|.
   \]

5. **A1-ISR-5 — \(R_U\)-DES Bridge**
   \[
   10VR_U=10^{m_3}H+b_3(Q_0-P_3(1+10^{n_2})).
   \]

6. **A1-ISR-6A/B — DES Radial-Gap Bridge**
   (GAP-A), (GAP-B).

7. **A1-ISR-7A/B — Iterated-Smith \(Z\) Radial-Gap Bridge**
   (ZGAP-A), (ZGAP-B).

8. **A1-ISR-8 — Smith Gap Integer Margin**
   \[
   \mathcal G_A\ge M\text{ or }\mathcal G_B\ge N
   \]
   whenever an integer radial point exists.

9. **A1-ISR-9 — Endpoint Euclidean Cancellation**
   \[
   10^{n_i-1}=q_iC_i+r_i'.
   \]

10. **A1-ISR-10 — Plus Sharp Defect Envelope**
    \[
    |H|<\beta_3Q_0.
    \]

11. **A1-ISR-11 — Two-Face Exact Successor Normal Form**
    (SUCC-A), (SUCC-B).

---

# 33. Smith-Rich Status

\[
\boxed{\textbf{NOT CLOSED}.}
\]

但已得到：

- branch-normalized finite-\(Z\) theorem；
- stronger finite-\(q\) theorem if using \(\mathcal M_{\max}\)；
- plus sharp envelope \(|H|<\beta_3Q_0\)；
- \(Z\) 已直接进入 radial gaps；
- plus+Face A / minus+Face B 形成真正 cancellation configuration。

仍缺：

\[
\boxed{
\text{finite }Z/q
\Longrightarrow
\text{endpoint quotient or }\mathcal G_{A/B}\text{ sufficiently constrained}.
}
\]

---

# 34. Smith-Poor Status

\[
\boxed{\textbf{NOT CLOSED}.}
\]

已知：poor overlap常把 arithmetic mass推向 complementary gcd/lcm factors，但这些 transverse factors不会直接缩 interval。

当前最小难点：

\[
\boxed{
\text{large transverse unit modulus}
\times
\text{endpoint quotient position}.
}
\]

在没有 Layer-P sample 前，没有证据表明需要 general Jacobsthal；更可能先需要一个 \(M/N\) / endpoint remainder theorem。

---

# 35. Raw Candidate Bound

global：

\[
\boxed{N_{\rm raw}\le C\text{ for absolute }C\quad\textbf{OPEN}.}
\]

已证明的 sharp local test：

### Face A

\[
0<\mathcal G_A<M\Rightarrow N_{\rm raw}=0.
\]

### Face B

\[
0<\mathcal G_B<N\Rightarrow N_{\rm raw}=0.
\]

若未来可将 \(\mathcal G_A/M\) 或 \(\mathcal G_B/N\) uniform bound 到 \(<r\)，即可得到 small raw list。

---

# 36. Coprime Candidate Bound

目前 global exact bound 仍只是 Möbius count：

\[
N_V(L,R)
=
\sum_{d\mid\operatorname{rad}(V)}
\mu(d)
\left(
\left\lceil\frac Rd\right\rceil
-
\left\lceil\frac Ld\right\rceil
\right).
\]

没有证明：

\[
N_V(I_{23})=0
\]

或 uniform \(N_V\le C\)。

但由于当前 exact regression没有 Layer-P sample，下一轮不应优先扩大 prime-cover machinery；应先压 endpoint count/location。

---

# 37. Status of \(g,k,d,n_3\)

冻结已有：

- \(g\) 不是独立于 \(Q_0\) 的 second height；
- \(g\ge1\) 时 \(P_2/Q_0>\sqrt{96/101}\)；
- \(10^{2k}<2.532Q_0\)（latest sharpened axis bound）；
- fixed \((g_2,g_3,n_2,n_3)\) common-\(U\) profile有限；
- \(g\ge1\) branch split只剩 \(d=0,1\) transition + one-sign outer chambers。

本轮没有得到 absolute bounds on \(g,k,d,n_3\)。

\[
\boxed{\textbf{profile finiteness revival not yet achieved}.}
\]

---

# 38. Remaining Terminal Chamber

本轮后不再需要把 frontier 写成几十维变量。

保留：

\[
(P_1,P_2,P_3,Q_0),
\]

\[
(g,k,d,n_3),
\]

\[
(s,\alpha,\beta,u_0,v,t),
\]

\[
(M,N,J,Z),
\]

满足 frozen sphere/DES/Smith equations，并只剩两个 radial successor cases。

### Terminal Face A

\[
\mathcal G_A=M10^{n_3}-N10^{n_2-1}>0,
\]

\[
\alpha t\mathcal G_A
=Q_0+\alpha JZ-P_3(1+10^{n_2-1}),
\]

\[
\boxed{
\nexists U:\
\frac{u_010^{n_2-1}}M\le U<\frac{u_010^{n_3}}N,
\quad\gcd(U,V)=1
}
\]

仍待证明。

### Terminal Face B

\[
\mathcal G_B=N10^{n_2}-M10^{n_3-1}>0,
\]

\[
10\alpha t\mathcal G_B
=P_3(10^{n_2+1}+1)-Q_0-\alpha JZ,
\]

\[
\boxed{
\nexists U:\
\frac{u_010^{n_3-1}}N\le U<\frac{u_010^{n_2}}M,
\quad\gcd(U,V)=1
}
\]

仍待证明。

这已经是一个有限数量（两个）的 explicit radial successor forms，而不是新的抽象无限层。

---

# 39. A1 Closure Status

\[
\boxed{
A_1\text{ remains OPEN}.
}
\]

因此：

\[
\boxed{
DD=\varnothing,
\qquad
\text{Strict Layer 尚未 CLOSED}.
}
\]

本轮没有伪报：

- \(N_V(I_{23})=0\)；
- Smith-rich closure；
- Smith-poor closure；
- resonance closure；
- double-resonance contradiction；
- finite global profile bound。

---

# 40. Dependency Audit if Closed

本轮未闭合，因此不生成假的 Closure Certificate。

但进行 interface audit 后确认：

1. common-\(U\) reconstruction theorem仍成立；
2. individual reducedness在 \(g_i=\gcd(V,P_i)\) + \(\gcd(U,V)=1\) 后自动恢复；
3. backward WGF/phase/norm没有额外独立 radial predicate；
4. 本轮新增 (GAP-A/B)、(ZGAP-A/B) 都只使用 frozen exact identities + elementary integer algebra；
5. 没有调用外部 theorem 作为 nonexistence dependency；
6. computational regression只用于 falsification/structure discovery。

因此若下一轮能证明 (SUCC-A) 与 (SUCC-B)，即可直接接回：

\[
\text{A1 reduction}
\to
\mathfrak a\ne0
\to
\text{GSYNC}
\to
\text{common-}U
\to
\text{DES}
\to
\text{Iterated Smith}
\to
\text{two-face successor exclusion}.
\]

---

# 41. Recommended Next Step

不建议再开 broad campaign。下一步只保留一个目标：

## A1-EQUA — Endpoint Quotient / Unit Alignment

分别对两个 face 研究 active lower endpoint：

### Face A

\[
\boxed{
m_A
=\left\lceil\frac{u_010^{n_2-1}}M\right\rceil
=\left\lceil\frac{10^{n_2-1}}{C_2}\right\rceil.
}
\]

目标：用

\[
\alpha t\mathcal G_A
=Q_0+\alpha JZ-P_3(1+10^{n_2-1})
\]

和 endpoint Euclidean remainder一起证明：

1. 要么 \(m_A\ge u_010^{n_3}/N\)（raw death）；
2. 要么 \(\gcd(m_A,V)>1\)；
3. 若还有 \(m_A+j\)，则把 \(j\) 的数量由 \(\mathcal G_A/M\) 压成 small finite list并逐一 kill。

### Face B

\[
\boxed{
m_B
=\left\lceil\frac{u_010^{n_3-1}}N\right\rceil
=\left\lceil\frac{10^{n_3-1}}{C_3}\right\rceil.
}
\]

同样用

\[
10\alpha t\mathcal G_B
=P_3(10^{n_2+1}+1)-Q_0-\alpha JZ
\]

去控制 \(m_B\) 与后续少数 integers。

这不是新顶层框架，而是当前 theorem

\[
\boxed{N_V(I_{23})=0}
\]

本身的 endpoint arithmetic implementation。

---

# Final Verdict

本轮没有完成

\[
\boxed{A_1=\varnothing}.
\]

但真正完成了第七轮以后最关键的一次 splice：

\[
\boxed{
\text{DES / Iterated Smith}
\longrightarrow
\text{exact radial gap }\mathcal G_A,\mathcal G_B
\longrightarrow
\text{two explicit successor intervals}.
}
\]

尤其新 identity

\[
\boxed{
\alpha t\mathcal G_A
=Q_0+\alpha JZ-P_3(1+10^{n_2-1})
}
\]

和

\[
\boxed{
10\alpha t\mathcal G_B
=P_3(10^{n_2+1}+1)-Q_0-\alpha JZ
}
\]

首次把第七轮的 iterated-Smith integer \(Z\) 真正接到了 common-\(U\) interval width。

因此 A1 的剩余问题已经不再是“DES/Smith 与 radial gate并列而互不相干”，而是非常具体的：

\[
\boxed{
\textbf{这些 exact radial-gap identities 为什么迫使 active endpoint successor}
\textbf{永远不是 }V\textbf{-unit？}
}
\]

这就是下一步唯一值得继续的正向 terminal obligation。
