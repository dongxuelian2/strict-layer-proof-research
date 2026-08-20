# 三项十进制拼接平方和问题：A1 Endpoint Quotient × Integer Alignment — Raw Radial Extinction Campaign

**文件名：** `strict_layer_A1_endpoint_quotient_integer_alignment_campaign.md`  
**研究范围：** Strict Layer，`A1-only` 正向线，第九轮。  
**核心任务：** Endpoint Quotient / Integer Alignment；优先普通整数存在性，只有 strict raw survivor 出现后才进入 coprimality。  
**最终状态：**

\[
\boxed{\textbf{Endpoint Euclidean Normal Form — PROVED}}
\]

\[
\boxed{\textbf{Global Raw Radial Extinction — OPEN}}
\]

\[
\boxed{\textbf{A1 — OPEN}}
\]

---

# 1. Executive Summary

本轮没有证明

\[
I_{23}\cap\mathbf Z_{>0}=\varnothing
\]

对所有 A1 terminal states 成立，因此不能宣布 \(A_1\) 闭合。

但是本轮完成了第八轮之后最重要的一次 **terminal arithmetic 压缩**：

\[
\boxed{
\text{Smith radial interval}
\Longrightarrow
\text{intrinsic }(C_2,C_3)\text{ chart}
\Longrightarrow
\text{Euclidean endpoint jump}
}
\]

并把普通整数层完全改写为两个有限整数不等式。

最核心的新结果如下。

## 1.1 PROVED — Smith presentation redundancy can be removed completely

第八轮已经有

\[
C_2=\frac{M}{u_0},\qquad
C_3=\frac{N}{u_0}.
\]

由于 \(C_2,C_3\in\mathbf Z_{>0}\)，必有

\[
\boxed{u_0\mid M,\qquad u_0\mid N.}
\]

因此定义

\[
M=u_0C_2,\qquad N=u_0C_3.
\]

则真正 radial endpoints 直接变成

\[
\boxed{
L_2=\frac{10^{n_2-1}}{C_2},\qquad
L_3=\frac{10^{n_3-1}}{C_3}.
}
\]

所以 ordinary integer alignment **完全不依赖 Smith presentation factor \(u_0\)**。

---

## 1.2 PROVED — Exact endpoint modular jumps

定义

\[
x_2:=10^{n_2-1},\qquad x_3:=10^{n_3-1}.
\]

对 block 2：

\[
x_2=q_2C_2+r_2,\qquad 0\le r_2<C_2,
\]

\[
m_2^\ast:=\left\lceil\frac{x_2}{C_2}\right\rceil,
\]

\[
\boxed{
\delta_2:=m_2^\ast C_2-x_2
=
\begin{cases}
0,&r_2=0,\\
C_2-r_2,&r_2>0.
\end{cases}}
\]

即

\[
\boxed{\delta_2=(-10^{n_2-1})\bmod C_2}
\]

取最小非负代表。

同理

\[
\boxed{
\delta_3
=
\left\lceil\frac{10^{n_3-1}}{C_3}\right\rceil C_3
-10^{n_3-1}
=
(-10^{n_3-1})\bmod C_3.
}
\]

---

## 1.3 PROVED — Exact Raw-Survival Theorem

### Face A

若

\[
L_2\ge L_3,
\]

定义 intrinsic radial gap

\[
\boxed{
G_A^\circ
:=
C_2\,10^{n_3}
-
C_3\,10^{n_2-1}.
}
\]

连续可行当且仅当

\[
G_A^\circ>0.
\]

则：

\[
\boxed{
I_A\cap\mathbf Z_{>0}\ne\varnothing
\iff
C_3\delta_2<G_A^\circ.
}
\tag{A-RAW}
\]

由于

\[
G_A^\circ-C_3\delta_2
\]

必为 \(C_2\) 的整数倍，所以严格不等式还能精确量化为

\[
\boxed{
I_A\cap\mathbf Z_{>0}\ne\varnothing
\iff
G_A^\circ\ge C_3\delta_2+C_2.
}
\tag{A-RAW-Q}
\]

### Face B

若

\[
L_3>L_2,
\]

定义

\[
\boxed{
G_B^\circ
:=
C_3\,10^{n_2}
-
C_2\,10^{n_3-1}.
}
\]

则

\[
\boxed{
I_B\cap\mathbf Z_{>0}\ne\varnothing
\iff
C_2\delta_3<G_B^\circ
}
\]

并精确等价于

\[
\boxed{
I_B\cap\mathbf Z_{>0}\ne\varnothing
\iff
G_B^\circ\ge C_2\delta_3+C_3.
}
\tag{B-RAW-Q}
\]

这比第八轮的

\[
G_A^\circ\ge C_2,\qquad
G_B^\circ\ge C_3
\]

严格更强；旧 threshold 只是 \(\delta=0\) 时的退化下界。

---

## 1.4 PROVED — Exact gap decomposition

Face A 令

\[
s_A:=10^{n_3}-m_2^\ast C_3\in\mathbf Z.
\]

则

\[
\boxed{
G_A^\circ
=
C_3\delta_2+C_2s_A.
}
\tag{A-DECOMP}
\]

所以

\[
\boxed{
\text{Face A raw survives}
\iff
s_A\ge1.
}
\]

Face B 对称地令

\[
s_B:=10^{n_2}-m_3^\ast C_2,
\]

则

\[
\boxed{
G_B^\circ
=
C_2\delta_3+C_3s_B,
}
\tag{B-DECOMP}
\]

且

\[
\boxed{
\text{Face B raw survives}
\iff
s_B\ge1.
}
\]

这给出本轮最直接的解释：

\[
\boxed{
\text{radial gap}
=
\text{endpoint jump cost}
+
\text{post-jump upper slack}.
}
\]

---

## 1.5 PROVED — Exact raw candidate count

Face A：

\[
\boxed{
N_A
=
\max\left(
0,
\left\lceil\frac{s_A}{C_3}\right\rceil
\right)
}
\]

即

\[
\boxed{
N_A
=
\max\left(
0,
\left\lceil
\frac{G_A^\circ-C_3\delta_2}{C_2C_3}
\right\rceil
\right).
}
\tag{COUNT-A}
\]

对任意 \(j\ge1\)：

\[
\boxed{
N_A\ge j
\iff
G_A^\circ
\ge
C_3\delta_2
+
(j-1)C_2C_3
+
C_2.
}
\tag{COUNT-Aj}
\]

Face B：

\[
\boxed{
N_B
=
\max\left(
0,
\left\lceil
\frac{G_B^\circ-C_2\delta_3}{C_2C_3}
\right\rceil
\right),
}
\tag{COUNT-B}
\]

且

\[
\boxed{
N_B\ge j
\iff
G_B^\circ
\ge
C_2\delta_3
+
(j-1)C_2C_3
+
C_3.
}
\tag{COUNT-Bj}
\]

因此本轮不仅得到 existence criterion，还得到完整的 raw-count hierarchy。

---

## 1.6 FAILED AS STANDALONE CLOSURE — ZGAP × endpoint jump collapses to the endpoint condition itself

将第八轮 ZGAP-A/B 与上述 exact \(\delta\)-threshold 联立后，利用

\[
P_3=\alpha tN,
\]

以及

\[
Q_0+\alpha JZ
=
\alpha t(M10^{n_3}+N),
\]

所有 \(Z,J,Q_0,P_3\) 项会精确消去，最后重新得到

\[
10^{n_3}-m_2^\ast C_3\ge1
\]

或

\[
10^{n_2}-m_3^\ast C_2\ge1.
\]

换言之：

\[
\boxed{
\text{ZGAP 精确编码 radial slack，}
}
\]

但：

\[
\boxed{
\text{它本身不提供独立 endpoint-phase control。}
}
\]

因此不能靠“把 ZGAP 再代一次”关闭 RAW。

真正尚缺的是：

\[
\boxed{
\textbf{对 }\delta_2,\delta_3
\textbf{ 本身的独立 arithmetic control。}
}
\]

---

## 1.7 Current strategic verdict

本轮最准确的新终端表述不是

\[
\operatorname{next}_V(L)\ge R,
\]

而是在 ordinary integer layer 上先写成：

### Face A

\[
\boxed{
G_A^\circ
\stackrel{?}{\ge}
C_3\delta_2+C_2.
}
\]

### Face B

\[
\boxed{
G_B^\circ
\stackrel{?}{\ge}
C_2\delta_3+C_3.
}
\]

若 inequality 成立，则 raw integer 存在；若失败，则 Layer \(I_0\) 死亡。

因此：

\[
\boxed{
\textbf{A1 ordinary radial gate = two modular-jump threshold tests.}
}
\]

---

# 2. Frozen Eight-Round Results

本轮冻结以下输入，不重新证明其上游架构。

## 2.1 Primitive sphere

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

## 2.2 A1 exponent normal form

\[
g=m_3-n_3\ge0,\qquad k\ge1,\qquad d=m_2-g,
\]

\[
\boxed{
m_2=g+d,\quad
n_2=2g+k+d,\quad
m_3=n_3+g.
}
\]

## 2.3 Exact word core

\[
D=P_110^k-Q_0>0,
\]

\[
H=b_2Q_0-b_110^{m_2}D\ne0,
\]

\[
b_2P_2=10^gH+K_3,
\]

\[
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbf Z_{>0}.
\]

plus / minus：

\[
\text{plus}\iff H<0,\qquad
\text{minus}\iff H>0.
\]

## 2.4 Common-\(U\) reconstruction

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

合法 terminal \(U\) 一旦存在，即可恢复 original strict candidate；不存在额外独立 norm gate。

## 2.5 Iterated Smith

冻结：

\[
g_2=u_0v,
\qquad
g_3=u_0\alpha t,
\]

\[
P_2=vM,
\qquad
P_3=\alpha tN,
\]

\[
C_2=M/u_0,
\qquad
C_3=N/u_0.
\]

并有

\[
H=M_H^{(2)}Z,
\]

\[
tM10^{n_3}-\frac{Q_0-P_3}{\alpha}=JZ.
\]

## 2.6 Face sign

\[
R_U=C_210^{n_3-1}-C_310^{n_2-1},
\]

\[
\boxed{
L_2\ge L_3
\iff
R_U\le0,
}
\]

\[
\boxed{
L_3>L_2
\iff
R_U>0.
}
\]

不再使用旧错误方向。

---

# 3. Exact Face A/B Radial Charts

由

\[
M=u_0C_2,\qquad N=u_0C_3
\]

得到：

\[
L_2=\frac{10^{n_2-1}}{C_2},
\qquad
L_3=\frac{10^{n_3-1}}{C_3}.
\]

## 3.1 Face A

\[
L_2\ge L_3.
\]

则

\[
\boxed{
I_A
=
\left[
\frac{10^{n_2-1}}{C_2},
\frac{10^{n_3}}{C_3}
\right).
}
\]

定义

\[
\boxed{
G_A^\circ
=
C_2 10^{n_3}
-
C_3 10^{n_2-1}.
}
\]

于是

\[
I_A\ne\varnothing
\iff
G_A^\circ>0,
\]

且

\[
\boxed{
|I_A|
=
\frac{G_A^\circ}{C_2C_3}.
}
\]

第八轮 Smith gap 为

\[
\mathcal G_A
=
M10^{n_3}-N10^{n_2-1}
=
u_0G_A^\circ.
\]

## 3.2 Face B

\[
L_3>L_2.
\]

则

\[
\boxed{
I_B
=
\left[
\frac{10^{n_3-1}}{C_3},
\frac{10^{n_2}}{C_2}
\right).
}
\]

定义

\[
\boxed{
G_B^\circ
=
C_3 10^{n_2}
-
C_2 10^{n_3-1}.
}
\]

于是

\[
I_B\ne\varnothing
\iff
G_B^\circ>0,
\]

并有

\[
\boxed{
|I_B|
=
\frac{G_B^\circ}{C_2C_3}.
}
\]

且

\[
\mathcal G_B=u_0G_B^\circ.
\]

**结论：** ordinary radial geometry 应优先写成 \(C_2,C_3\) intrinsic chart；\(M,N,u_0\) 只在与 DES/Smith 外部 constraints 对接时恢复。

---

# 4. Endpoint Euclidean Division

## 4.1 Face A lower endpoint

写

\[
10^{n_2-1}=q_2C_2+r_2,
\qquad
0\le r_2<C_2.
\]

第一个可能整数：

\[
\boxed{
m_A
=
q_2+\mathbf 1_{r_2>0}
=
\left\lceil\frac{10^{n_2-1}}{C_2}\right\rceil.
}
\]

定义

\[
\boxed{
\delta_2
=
m_AC_2-10^{n_2-1}.
}
\]

于是

\[
0\le\delta_2<C_2,
\]

并且：

\[
r_2=0\iff\delta_2=0,
\]

\[
r_2>0\Longrightarrow\delta_2=C_2-r_2.
\]

## 4.2 Face B lower endpoint

同理

\[
10^{n_3-1}=q_3C_3+r_3,
\qquad
0\le r_3<C_3,
\]

\[
\boxed{
m_B
=
\left\lceil\frac{10^{n_3-1}}{C_3}\right\rceil,
}
\]

\[
\boxed{
\delta_3
=
m_BC_3-10^{n_3-1}.
}
\]

---

# 5. Exact Raw-Survival Criterion

## 5.1 Face A derivation

raw integer 存在当且仅当第一个可能整数仍低于 open upper endpoint：

\[
m_A<\frac{10^{n_3}}{C_3}.
\]

乘 \(C_2C_3\)：

\[
m_AC_2C_3<C_2 10^{n_3}.
\]

而

\[
m_AC_2
=
10^{n_2-1}+\delta_2.
\]

故：

\[
C_3 10^{n_2-1}+C_3\delta_2
<
C_2 10^{n_3}.
\]

于是：

\[
\boxed{
C_3\delta_2<G_A^\circ.
}
\tag{5.1}
\]

这严格处理了 half-open upper endpoint。

若 \(\delta_2=0\)，则 lower endpoint 本身就是整数；只要 \(G_A^\circ>0\)，upper endpoint 严格更大，所以：

\[
\boxed{
\delta_2=0,\ G_A^\circ>0
\Longrightarrow
\text{raw automatically survives}.
}
\tag{5.2}
\]

若 \(\delta_2>0\)，则 (5.1) 正是 modular successor jump 与 radial width 的比较。

更强地：

\[
G_A^\circ-C_3\delta_2
=
C_2(10^{n_3}-m_AC_3).
\]

右边是 \(C_2\) 的整数倍，所以

\[
G_A^\circ>C_3\delta_2
\]

等价于至少多出一个完整 \(C_2\)-quantum：

\[
\boxed{
G_A^\circ\ge C_3\delta_2+C_2.
}
\tag{5.3}
\]

## 5.2 Face B derivation

完全同理：

\[
m_B<\frac{10^{n_2}}{C_2}
\]

等价于

\[
\boxed{
C_2\delta_3<G_B^\circ
}
\tag{5.4}
\]

并量化为

\[
\boxed{
G_B^\circ\ge C_2\delta_3+C_3.
}
\tag{5.5}
\]

---

# 6. Modular Jump \(\delta_2,\delta_3\)

本轮真正 canonical 的 endpoint variables 是：

\[
\boxed{
\delta_2=(-10^{n_2-1})\bmod C_2,
}
\]

\[
\boxed{
\delta_3=(-10^{n_3-1})\bmod C_3.
}
\]

它们不是随机 fractional parts，而是完全 exact 的 Euclidean residues。

定义 fractional endpoint phase：

\[
\phi_A
:=
m_A-\frac{10^{n_2-1}}{C_2}
=
\frac{\delta_2}{C_2},
\]

\[
\phi_B
:=
m_B-\frac{10^{n_3-1}}{C_3}
=
\frac{\delta_3}{C_3}.
\]

因此：

\[
\boxed{
\text{Face A raw survives}
\iff
\phi_A<|I_A|,
}
\]

\[
\boxed{
\text{Face B raw survives}
\iff
\phi_B<|I_B|.
}
\]

这里 \(\phi=0\) 也统一包含：只要 continuous width \(>0\)，整数 lower endpoint 自动属于 interval。

---

# 7. Removal of Smith Presentation Redundancy

prompt 中原始 Euclidean division 是：

\[
u_010^{n_2-1}=q_AM+r_A,
\qquad 0\le r_A<M.
\]

因为

\[
M=u_0C_2,
\]

直接有

\[
\boxed{
r_A=u_0r_2.
}
\]

presentation modular jump：

\[
\Delta_A
:=
\begin{cases}
0,&r_A=0,\\
M-r_A,&r_A>0
\end{cases}
\]

满足

\[
\boxed{
\Delta_A=u_0\delta_2.
}
\]

同理：

\[
\boxed{
r_B=u_0r_3,\qquad
\Delta_B=u_0\delta_3.
}
\]

因此 prompt 中的判据确实正确：

\[
\boxed{
N\Delta_A<u_0\mathcal G_A
}
\]

与

\[
\boxed{
M\Delta_B<u_0\mathcal G_B.
}
\]

代入

\[
N=u_0C_3,\quad
M=u_0C_2,\quad
\mathcal G_A=u_0G_A^\circ,\quad
\mathcal G_B=u_0G_B^\circ
\]

后恰约成 intrinsic criteria：

\[
C_3\delta_2<G_A^\circ,
\]

\[
C_2\delta_3<G_B^\circ.
\]

### Quantized presentation form

Face A：

\[
\boxed{
u_0\mathcal G_A
\ge
N\Delta_A+u_0M.
}
\]

Face B：

\[
\boxed{
u_0\mathcal G_B
\ge
M\Delta_B+u_0N.
}
\]

所以 \(u_0\) 是纯 presentation redundancy，不应继续污染 endpoint arithmetic。

---

# 8. ZGAP × Endpoint Splice

冻结：

\[
\alpha t\mathcal G_A
=
Q_0+\alpha JZ-P_3(1+10^{n_2-1}),
\]

\[
10\alpha t\mathcal G_B
=
P_3(10^{n_2+1}+1)-Q_0-\alpha JZ,
\]

以及

\[
Q_0+\alpha JZ
=
\alpha t(M10^{n_3}+N),
\]

\[
P_3=\alpha tN.
\]

## 8.1 Face A

raw survival 的 quantized threshold：

\[
G_A^\circ\ge C_3\delta_2+C_2.
\]

乘 \(u_0\alpha t\)：

\[
\alpha t\mathcal G_A
\ge
\alpha tN\delta_2+\alpha tM.
\]

用

\[
\alpha tN=P_3
\]

及 ZGAP-A：

\[
Q_0+\alpha JZ-P_3(1+10^{n_2-1})
\ge
P_3\delta_2+\alpha tM.
\]

再用 MNZ：

\[
\alpha t(M10^{n_3}+N)
-
P_3(1+10^{n_2-1})
\ge
P_3\delta_2+\alpha tM.
\]

消去 \(P_3=\alpha tN\) 后：

\[
M(10^{n_3}-1)
\ge
N(10^{n_2-1}+\delta_2).
\]

而

\[
10^{n_2-1}+\delta_2=m_AC_2,
\]

\[
M=u_0C_2,\quad N=u_0C_3,
\]

所以恰化成：

\[
\boxed{
10^{n_3}-m_AC_3\ge1.
}
\]

这正是 first candidate 严格低于 open upper endpoint。

因此 ZGAP splice 没有产生新的 independent inequality。

## 8.2 Face B

完全对称地，ZGAP-B + MNZ + quantized raw threshold 最后化成：

\[
\boxed{
10^{n_2}-m_BC_2\ge1.
}
\]

## 8.3 Verdict

\[
\boxed{
\textbf{FAILED AS STANDALONE RAW-CLOSURE ROUTE.}
}
\]

但不是说 ZGAP 错误；恰恰相反，它太 exact，以至于在 endpoint variables 中只是重新编码了同一个 upper-slack condition。

真正需要的新输入必须能独立限制

\[
\delta_2,\delta_3
\]

或 first-candidate excess，而不能只是再重写 \(G_A^\circ,G_B^\circ\)。

---

# 9. Face A Analysis

Face A 的 canonical state：

\[
\boxed{
(C_2,C_3,n_2,n_3;\delta_2,G_A^\circ).
}
\]

连续层：

\[
G_A^\circ>0.
\]

整数层：

\[
\boxed{
G_A^\circ\ge C_3\delta_2+C_2.
}
\]

定义

\[
s_A=10^{n_3}-m_AC_3.
\]

则

\[
G_A^\circ=C_3\delta_2+C_2s_A.
\]

因此四种状态：

\[
s_A\le0
\Longrightarrow I_0,
\]

\[
1\le s_A\le C_3
\Longrightarrow I_1,
\]

\[
s_A\ge C_3+1
\Longrightarrow I_{\ge2}.
\]

### First candidate

\[
\boxed{
U_0=m_A.
}
\]

只要 \(s_A\ge1\)，所有 later candidates 为：

\[
U_j=m_A+j.
\]

---

# 10. Face B Analysis

Face B：

\[
\boxed{
(C_2,C_3,n_2,n_3;\delta_3,G_B^\circ).
}
\]

连续层：

\[
G_B^\circ>0.
\]

整数层：

\[
\boxed{
G_B^\circ\ge C_2\delta_3+C_3.
}
\]

定义：

\[
s_B=10^{n_2}-m_BC_2.
\]

则：

\[
G_B^\circ=C_2\delta_3+C_3s_B.
\]

状态分类：

\[
s_B\le0\Rightarrow I_0,
\]

\[
1\le s_B\le C_2\Rightarrow I_1,
\]

\[
s_B\ge C_2+1\Rightarrow I_{\ge2}.
\]

---

# 11. \(U=1\) Chamber

\[
U=1
\]

自动满足

\[
\gcd(1,V)=1.
\]

所以任何 exact terminal state 若 \(U=1\) raw-live，已经直接绕过未来所有 prime-cover / Jacobsthal arguments。

其必要充分条件就是：

\[
\boxed{
10^{n_2-1}\le C_2<10^{n_2},
}
\]

\[
\boxed{
10^{n_3-1}\le C_3<10^{n_3}.
}
\tag{U1}
\]

此时

\[
a_2=C_2,\qquad a_3=C_3.
\]

定义 excess：

\[
e_2=C_2-10^{n_2-1},
\qquad
e_3=C_3-10^{n_3-1}.
\]

如果 active face 是 A，则 first candidate 必为 \(m_A=1\)，从而

\[
\delta_2=e_2.
\]

如果 active face 是 B：

\[
\delta_3=e_3.
\]

### 本轮裁决

没有从现有 DES / Smith / ZGAP 证明

\[
U=1\Longrightarrow\bot.
\]

所以：

\[
\boxed{\textbf{\(U=1\) closure remains OPEN.}}
\]

任何未来 purely-coprime obstruction 都必须先单独处理这个 chamber。

---

# 12. Raw Candidate Count

Face A：

\[
R_A=\frac{10^{n_3}}{C_3}.
\]

精确整数数目：

\[
N_A
=
\max(0,\lceil R_A\rceil-m_A).
\]

利用

\[
R_A
=
m_A+\frac{s_A}{C_3},
\]

得到：

\[
\boxed{
N_A
=
\max\left(0,\left\lceil\frac{s_A}{C_3}\right\rceil\right).
}
\]

再利用 gap decomposition：

\[
s_A
=
\frac{G_A^\circ-C_3\delta_2}{C_2},
\]

得到 (COUNT-A)。

### Exactly one

\[
N_A=1
\iff
1\le s_A\le C_3.
\]

等价于：

\[
\boxed{
C_3\delta_2+C_2
\le
G_A^\circ
\le
C_3\delta_2+C_2C_3.
}
\]

也可写成下一 threshold 之前：

\[
\boxed{
G_A^\circ
<
C_3\delta_2+C_2C_3+C_2.
}
\]

后者与前者因 \(G_A^\circ-C_3\delta_2\) 必为 \(C_2\) 倍数而等价。

Face B 完全对称。

### Global status

本轮没有证明：

\[
N_{\rm raw}\le1
\]

uniformly over all full terminal states。

也没有证明：

\[
N_{\rm raw}\le C
\]

for an absolute \(C\)。

因此：

\[
\boxed{\textbf{Global small-count theorem remains OPEN.}}
\]

---

# 13. Numerator Excess Coordinates

对任意 raw candidate \(U\)，定义

\[
e_2:=UC_2-10^{n_2-1},
\]

\[
e_3:=UC_3-10^{n_3-1}.
\]

那么：

\[
0\le e_2\le9\cdot10^{n_2-1}-1,
\]

\[
0\le e_3\le9\cdot10^{n_3-1}-1.
\]

并有 exact identity：

\[
\boxed{
C_3e_2-C_2e_3
=
C_210^{n_3-1}
-
C_310^{n_2-1}
=
R_U.
}
\tag{EX}
\]

## 13.1 Face A first candidate

\[
U=m_A,
\]

所以

\[
\boxed{e_2=\delta_2.}
\]

prompt 中 presentation jump \(\Delta_A\) 满足：

\[
\boxed{
\Delta_A=u_0e_2.
}
\]

由 (EX)：

\[
\boxed{
e_3
=
\frac{C_3\delta_2-R_U}{C_2}.
}
\tag{E3-A}
\]

Face A raw survival 等价于：

\[
\boxed{
e_3\le9\cdot10^{n_3-1}-1.
}
\tag{A-EX-RAW}
\]

同时

\[
s_A=9\cdot10^{n_3-1}-e_3.
\]

## 13.2 Face B first candidate

\[
U=m_B,
\]

\[
\boxed{e_3=\delta_3.}
\]

由 (EX)：

\[
\boxed{
e_2
=
\frac{R_U+C_2\delta_3}{C_3}.
}
\tag{E2-B}
\]

raw survival 等价于：

\[
\boxed{
e_2\le9\cdot10^{n_2-1}-1.
}
\tag{B-EX-RAW}
\]

这说明：

\[
\boxed{
\text{endpoint jump控制 active excess，}
}
\]

而：

\[
\boxed{
R_U\text{ 将它传递到 inactive block excess。}
}
\]

这比直接 ZGAP splice 更可能承载真正的新 contradiction。

---

# 14. \(R_U\) and Active Face

冻结：

\[
R_U
=
C_210^{n_3-1}
-
C_310^{n_2-1}.
\]

Face A：

\[
R_U\le0.
\]

Face B：

\[
R_U>0.
\]

第八轮有 exact bridge：

\[
\boxed{
10VR_U
=
10^{m_3}H
+
b_3\left(
Q_0-P_3(1+10^{n_2})
\right).
}
\tag{RU-H}
\]

本轮的新观察是：若将 RU-H 与 first-candidate excess 联立，则不再只是 gap identity。

### Face A

\[
e_3
=
\frac{C_3\delta_2-R_U}{C_2}.
\]

因此若能由 RU-H 给出足够负的 \(R_U\)，便会强迫 \(e_3\) 超过 third-block upper digit bound，从而杀掉 raw survivor。

### Face B

\[
e_2
=
\frac{R_U+C_2\delta_3}{C_3}.
\]

若 \(R_U\) 足够正，则会强迫 \(e_2\) 超过 second-block upper digit bound。

### Verdict

本轮没有获得满足所有 branches 的 uniform RU-H size theorem，因此：

\[
\boxed{
\textbf{RU-H × first-candidate excess remains OPEN but non-tautological.}
}
\]

这应当优先于重复 ZGAP substitution。

---

# 15. \(d=0\) Chamber

\[
d=0
\Longrightarrow
m_2=g,
\]

\[
\boxed{
n_2=2g+k.
}
\]

因此：

\[
L_2
=
\frac{10^{2g+k-1}}{C_2}.
\]

这确实把 endpoint exponent 与 primitive ratio exponent \(2g+k\) 对齐。

但是现有 theorem 已经表明：

- \(d=0\) 并不自动 continuous-dead；
- denominator resonance \(R=0\) 就落在 \(d=0\)；
- \(R_U=0\) 也可以与该 chamber algebraically compatible。

因此：

\[
\boxed{
d=0\Longrightarrow\text{raw-dead}
}
\]

本轮没有证明。

### Useful exact specialization

\[
\delta_2
=
(-10^{2g+k-1})\bmod C_2.
\]

这将成为下一轮针对 decimal content / RU-H 的自然入口。

---

# 16. \(d=1\) Plus

第八轮中 plus + Face A 是短-gap cancellation 最有希望的 branch 之一：

\[
Z<0.
\]

ZGAP-A：

\[
\alpha t\mathcal G_A
=
Q_0-P_3(1+10^{n_2-1})
-\alpha J|Z|.
\]

这确实压小 radial gap。

但本轮加入 exact endpoint jump 后，单纯把该式代入 raw criterion 最终仍通过 MNZ 塌回 upper endpoint condition。

所以：

\[
\boxed{
\textbf{plus + Face A small gap is not enough;}
}
\]

真正还必须证明：

\[
\boxed{
\delta_2
\text{ cannot shrink at the same time.}
}
\]

本轮没有得到该 independence theorem。

---

# 17. Large-\(d\) Minus

large \(d\) minus 中：

\[
Z>0,
\]

且 \(\alpha JZ\) 可以使某些 radial gaps 变大。

因此这是 RAW conjecture 最危险的 branch 之一：

\[
\boxed{
\text{large gap}
\Longrightarrow
\text{integer survival more plausible}.
}
\]

当前已有 exact terminal scan 尚未给出 raw survivor，但样本规模不足以支持 theorem。

所以：

\[
\boxed{
\textbf{large-\(d\) minus is a priority falsification chamber for RAW.}
}
\]

本轮没有把它错误地压回 generic prime covering。

---

# 18. Double Resonance

副线：

\[
R=0,\qquad R_U=0.
\]

已有：

\[
P_2=10^{2g+k}P_3.
\]

sphere：

\[
\boxed{
P_1^2+
(10^{4g+2k}+1)P_3^2
=
Q_0^2.
}
\]

即：

\[
\boxed{
(Q_0-P_1)(Q_0+P_1)
=
(10^{4g+2k}+1)P_3^2.
}
\]

Smith resonance 又给：

\[
\alpha=t=1,
\qquad
v=10^{n_3},
\]

\[
g_2=u_010^{n_3},
\qquad
g_3=u_0.
\]

但本轮没有从 factor allocation 得到 contradiction。

更重要的是：

\[
R_U=0
\Longrightarrow
L_2=L_3,
\]

所以 real interval 是最大-overlap form：

\[
[L,10L).
\]

如果 \(L\) 恰为整数，则 continuous feasibility 会自动给 raw integer。

因此 double resonance 并不是一个天然的 raw-death chamber。

\[
\boxed{
R=R_U=0\Longrightarrow\bot
}
\]

仍为：

\[
\boxed{\textbf{OPEN}.}
\]

---

# 19. \(g=0\)

本轮 core endpoint theorem 本身只依赖：

\[
C_2,C_3,n_2,n_3,
\]

因此 **不需要 \(g\ge1\)**。

所以：

- Euclidean jump theorem；
- raw survival criterion；
- exact candidate count；
- numerator excess equation；

全部自动覆盖 \(g=0\)。

现有已知 \(g=0\) synchronized infinite pseudo-family：

\[
(b_1,b_2,b_3)=(1,6,8),
\]

\[
(n_2,n_3)=(2,1)
\]

整体满足

\[
C_3>C_2,
\]

因 digit ordering 被 Layer C 关闭。

现有另外的 real-overlap \(g=0\) regression point则死于 Layer I。

因此：

\[
\boxed{
\text{known }g=0\text{ families/states are C/I dead},
}
\]

但：

\[
\boxed{
\textbf{all \(g=0\) terminal states raw-dead}
}
\]

尚未证明。

---

# 20. Computational Survivor Classification

本轮不把有限计算升级为 nonexistence theorem。

已有 exact radial regression corpus 包含：

### State 1

\[
(C_2,C_3;n_2,n_3)=(13,53;2,1).
\]

Face A：

\[
G_A^\circ
=
13\cdot10-53\cdot10
=
-400.
\]

Layer C。

### State 2

\[
(C_2,C_3;n_2,n_3)=(109,25;2,1).
\]

\[
G_A^\circ
=
1090-250
=
840>0.
\]

但

\[
\delta_2
=
109-10
=
99.
\]

raw threshold：

\[
C_3\delta_2+C_2
=
25\cdot99+109
=
2584.
\]

所以：

\[
840<2584.
\]

\[
\boxed{\text{Layer }I_0.}
\]

这精确解释了：

\[
I_{23}=[10/109,2/5).
\]

### State 3

\[
(C_2,C_3;n_2,n_3)=(73,969;2,1).
\]

\[
G_A^\circ=-8960.
\]

Layer C。

### State 4 — exact continuous boundary

\[
(C_2,C_3;n_2,n_3)=(949,949;2,1).
\]

\[
G_A^\circ=0.
\]

boundary-C。

### State 5

\[
(C_2,C_3;n_2,n_3)=(2514,297;2,1).
\]

\[
G_A^\circ=22170>0.
\]

\[
\delta_2=2514-10=2504.
\]

threshold：

\[
297\cdot2504+2514
=
746202.
\]

所以：

\[
22170\ll746202.
\]

Layer \(I_0\)。

### State 6/7

\[
(C_2,C_3;n_2,n_3)=(132,123;3,1).
\]

\[
G_A^\circ
=
1320-123000<0.
\]

Layer C。

### Another exact real-cone point

\[
(C_2,C_3;n_2,n_3)=(17813,2633;2,1).
\]

\[
G_A^\circ=151800>0,
\]

但

\[
\delta_2=17803,
\]

\[
C_3\delta_2+C_2
=
46\,893\,112.
\]

所以仍为强 Layer \(I_0\)。

### Experimental verdict

当前 audited exact corpus：

\[
\boxed{
C/I_0/C/\partial C/I_0/C/C
}
\]

并有其他 real-cone \(I_0\) points。

没有发现：

\[
I_1,
\qquad
I_{\ge2},
\qquad
P.
\]

但：

\[
\boxed{
\textbf{absence in current corpus is EXPERIMENTAL only.}
}
\]

---

# 21. Layer C / I / P Ledger

从本轮开始建议严格使用：

## Layer C

\[
G^\circ\le0.
\]

real interval empty 或 boundary-empty。

## Layer \(I_0\)

\[
G^\circ>0
\]

但 modular-jump threshold 失败。

Face A：

\[
G_A^\circ<C_3\delta_2+C_2.
\]

Face B：

\[
G_B^\circ<C_2\delta_3+C_3.
\]

## Layer \(I_1\)

exactly one raw integer。

Face A：

\[
C_3\delta_2+C_2
\le G_A^\circ
\le
C_3\delta_2+C_2C_3.
\]

Face B 对称。

## Layer \(I_{\ge2}\)

第二个 candidate threshold 也通过。

Face A：

\[
G_A^\circ
\ge
C_3\delta_2+C_2C_3+C_2.
\]

Face B：

\[
G_B^\circ
\ge
C_2\delta_3+C_2C_3+C_3.
\]

## Layer P

只有 raw candidates 已经存在后才定义：

\[
\forall U\in I_{23}\cap\mathbf Z_{>0},
\qquad
\gcd(U,V)>1.
\]

---

# 22. Explicit Raw Survivors if Any

在本轮审计到的 existing exact terminal regression corpus 中：

\[
\boxed{
\textbf{no strict raw survivor was found.}
}
\]

因此本报告没有虚构 \(I_1\) 或 \(I_{\ge2}\) example。

重要限定：

\[
\boxed{
\text{这不是 global RAW theorem。}
}
\]

现有 scan 规模和 profile coverage 都不足以将“未找到”升级为“不存在”。

---

# 23. Explicit Coprime Survivors if Any

由于 audited corpus 中尚未出现 raw integer：

\[
I_{23}\cap\mathbf Z_{>0}\ne\varnothing,
\]

所以本轮严格遵守纪律：

\[
\boxed{
\textbf{没有提前启动 Layer P prime-cover analysis。}
}
\]

因此也没有：

- killer-prime ledger；
- Jacobsthal；
- generic CRT covering；
- \(\varphi(V)/V\) density。

目前：

\[
\boxed{
\textbf{no coprime raw survivor is known in the audited corpus.}
}
\]

若未来出现，必须立即恢复：

\[
a_i=UC_i,\qquad b_i=V/g_i
\]

并验证 original equation。

---

# 24. Failed Conjectures

## FAILED AS A STANDALONE ROUTE

### 24.1 “ZGAP + remainder criterion automatically proves raw death”

失败。

两者联立后精确塌回 upper endpoint legality。

### 24.2 “large Smith divisor gives a large endpoint jump”

没有证明。

Smith transverse factors大量从 \(C_2,C_3\) endpoints 中 exact cancel。

### 24.3 “\(\delta_i\) has a uniform Smith-size lower bound”

没有证明。

能保证的 universal lower bound来自 decimal gcd，见第 25 节。

### 24.4 “raw candidate count always \(\le1\)”

没有证明。

本轮得到 exact threshold，但没有 global bound on \(G^\circ\)。

### 24.5 “\(U=1\) impossible”

没有证明。

仍是独立高优先级 chamber。

### 24.6 “double resonance impossible”

没有证明。

仍 OPEN。

### 24.7 “Face A plus automatically raw-dead”

没有证明。

short-gap cancellation不等于 endpoint-phase obstruction。

### 24.8 “Face B minus automatically raw-dead”

同样没有证明。

### 24.9 “Layer P does not exist”

没有 theorem。

当前只是没有实验样本。

---

# 25. New Proven Lemmas

## A1-EQIA-1 — Intrinsic Radial Cancellation

\[
\boxed{
M=u_0C_2,\qquad
N=u_0C_3.
}
\]

ordinary endpoint arithmetic只依赖 \(C_2,C_3\)。

**PROVED.**

---

## A1-EQIA-2 — Endpoint Euclidean Jump

\[
\boxed{
\delta_i
=
\left\lceil
\frac{10^{n_i-1}}{C_i}
\right\rceil C_i
-
10^{n_i-1}.
}
\]

**PROVED.**

---

## A1-EQIA-3A/B — Exact Raw Survival

Face A：

\[
\boxed{
I_A\cap\mathbf Z_{>0}\ne\varnothing
\iff
G_A^\circ\ge C_3\delta_2+C_2.
}
\]

Face B：

\[
\boxed{
I_B\cap\mathbf Z_{>0}\ne\varnothing
\iff
G_B^\circ\ge C_2\delta_3+C_3.
}
\]

**PROVED.**

---

## A1-EQIA-4A/B — Gap Decomposition

\[
\boxed{
G_A^\circ=C_3\delta_2+C_2s_A,
}
\]

\[
\boxed{
G_B^\circ=C_2\delta_3+C_3s_B.
}
\]

**PROVED.**

---

## A1-EQIA-5A/B — Exact Candidate Count

\[
\boxed{
N_A
=
\max\left(
0,
\left\lceil
\frac{G_A^\circ-C_3\delta_2}{C_2C_3}
\right\rceil
\right),
}
\]

\[
\boxed{
N_B
=
\max\left(
0,
\left\lceil
\frac{G_B^\circ-C_2\delta_3}{C_2C_3}
\right\rceil
\right).
}
\]

**PROVED.**

---

## A1-EQIA-6 — Decimal-content jump lower bound

定义

\[
h_2:=\gcd(C_2,10^{n_2-1}),
\]

\[
h_3:=\gcd(C_3,10^{n_3-1}).
\]

若 \(\delta_2>0\)，则

\[
\boxed{
h_2\mid\delta_2,
\qquad
\delta_2\ge h_2.
}
\]

若 \(\delta_3>0\)：

\[
\boxed{
h_3\mid\delta_3,
\qquad
\delta_3\ge h_3.
}
\]

因此 nonintegral lower endpoint 的必要 raw conditions为：

Face A：

\[
\boxed{
G_A^\circ\ge C_3h_2+C_2.
}
\]

Face B：

\[
\boxed{
G_B^\circ\ge C_2h_3+C_3.
}
\]

**PROVED.**

---

## A1-EQIA-7 — Reduced endpoint fraction

令

\[
C_2=h_2C_2^\ast,
\qquad
10^{n_2-1}=h_2x_2^\ast,
\]

则

\[
\gcd(C_2^\ast,x_2^\ast)=1.
\]

若 \(C_2^\ast=1\)，lower endpoint 是整数：

\[
\delta_2=0.
\]

若 \(C_2^\ast>1\)，则：

\[
\delta_2=h_2\delta_2^\ast,
\]

其中

\[
1\le\delta_2^\ast<C_2^\ast,
\]

并且

\[
\boxed{
\gcd(\delta_2^\ast,C_2^\ast)=1.
}
\]

Face B 对称。

**PROVED.**

这给出一个重要 bifurcation：

### Decimal-saturated endpoint

\[
C_2\mid10^{n_2-1}
\Longrightarrow
\delta_2=0.
\]

于是只要 Face A continuous-live，就自动 raw-live。

所以任何 global RAW proof 都必须明确关闭这类 exact-alignment chamber。

### Unsaturated endpoint

\[
C_2^\ast>1,
\]

则 normalized modular jump是 reduced denominator 的 unit residue。

---

## A1-EQIA-8 — Gap residue encoding

Face A：

\[
G_A^\circ
=
C_210^{n_3}
-
C_310^{n_2-1}
\]

给出：

\[
\boxed{
G_A^\circ
\equiv
C_3\delta_2
\pmod{C_2}.
}
\]

Face B：

\[
\boxed{
G_B^\circ
\equiv
C_2\delta_3
\pmod{C_3}.
}
\]

若

\[
\gcd(C_2,C_3)=1,
\]

则 \(\delta_2\) / \(\delta_3\) 可由 gap modulo active core 唯一恢复。

**PROVED / ENCODING ONLY.**

它本身不是新 obstruction，因为 gap定义已经包含同一 endpoint power。

---

## A1-EQIA-9 — First-candidate Excess Dictionary

Face A：

\[
\boxed{
e_2^{(0)}=\delta_2,
}
\]

\[
\boxed{
e_3^{(0)}
=
\frac{C_3\delta_2-R_U}{C_2}.
}
\]

Face B：

\[
\boxed{
e_3^{(0)}=\delta_3,
}
\]

\[
\boxed{
e_2^{(0)}
=
\frac{R_U+C_2\delta_3}{C_3}.
}
\]

**PROVED.**

---

## A1-EQIA-10 — Later Candidate Arithmetic Progression

若 first candidate 为 \(U_0\)，则：

\[
U_j=U_0+j,
\]

\[
e_2^{(j)}
=
e_2^{(0)}+jC_2,
\]

\[
e_3^{(j)}
=
e_3^{(0)}+jC_3.
\]

**PROVED.**

这为未来真正出现 Layer P 后的 finite unit check 提供直接接口。

---

# 26. Status of Raw Extinction

目标：

\[
\boxed{
I_{23}\cap\mathbf Z_{>0}=\varnothing
}
\]

for every terminal A1 state。

本轮：

\[
\boxed{\textbf{NOT PROVED}.}
\]

但 proof obligation 已精确压缩为：

### Face A

证明所有 admissible Face A terminal states 均满足

\[
\boxed{
G_A^\circ
<
C_3\delta_2+C_2.
}
\tag{RAW-A}
\]

### Face B

证明

\[
\boxed{
G_B^\circ
<
C_2\delta_3+C_3.
}
\tag{RAW-B}
\]

这是比第八轮“interval exists / does not exist”更低维的 exact target。

---

# 27. Status of \(U=1\)

\[
\boxed{
U=1
\iff
\ell(C_2)=n_2,\quad
\ell(C_3)=n_3
}
\]

在 block 2/3 terminal sense 下。

本轮没有排除。

所以：

\[
\boxed{\textbf{\(U=1\) remains OPEN.}}
\]

并且：

\[
\boxed{
\text{任何只作用于 }\gcd(U,V)\text{ 的 future theorem 都无法处理它。}
}
\]

---

# 28. Status of Layer P

Layer P 需要先存在：

\[
I_{23}\cap\mathbf Z_{>0}\ne\varnothing.
\]

当前 audited exact corpus 中没有这样的 state。

因此：

\[
\boxed{
\textbf{Layer P has not yet been empirically activated.}
}
\]

这不是证明 Layer P 不存在。

本轮不建议下一步直接转 Jacobsthal / prime density，除非先构造一个 strict \(I_1\) 或 \(I_{\ge2}\) survivor。

---

# 29. A1 Closure Status

本轮没有得到：

\[
A_1=\varnothing.
\]

所以 Strict Layer 仍未完全闭合。

但 terminal architecture 已进一步缩成：

\[
\boxed{
\text{Exact A1 terminal state}
\Longrightarrow
\begin{cases}
\text{Face A: }G_A^\circ\ \text{vs. }C_3\delta_2+C_2,\\[2mm]
\text{Face B: }G_B^\circ\ \text{vs. }C_2\delta_3+C_3.
\end{cases}
}
\]

若 raw survives，再恢复：

\[
U_0=\left\lceil L_{23}\right\rceil
\]

以及 later candidates。

只有此后才进入：

\[
\gcd(U,V).
\]

---

# 30. Recommended Next Campaign / Closure Audit

本轮结果表明，第十轮不应重新回到 generic Smith determinant，也不应直接启动 coprime prime covering。

最高 leverage 的三个方向如下。

## Target 1 — \(R_U\)-H × First-Candidate Excess

不要再用 ZGAP 表示 width。

直接使用：

\[
10VR_U
=
10^{m_3}H
+
b_3(Q_0-P_3(1+10^{n_2}))
\]

与：

Face A：

\[
e_3^{(0)}
=
\frac{C_3\delta_2-R_U}{C_2},
\]

Face B：

\[
e_2^{(0)}
=
\frac{R_U+C_2\delta_3}{C_3}.
\]

目标是证明 inactive excess 越过 digit upper boundary。

这是当前最明显的 **non-tautological endpoint splice**。

---

## Target 2 — Decimal Content / Exact-Alignment Chamber

系统分析：

\[
h_2=\gcd(C_2,10^{n_2-1}),
\qquad
h_3=\gcd(C_3,10^{n_3-1}).
\]

尤其必须单独处理：

\[
C_2\mid10^{n_2-1}
\]

或

\[
C_3\mid10^{n_3-1},
\]

因为：

\[
\delta=0
\]

会使 continuous-live 自动变 raw-live。

因此 global RAW theorem 若为真，必须从 primitive / Smith / sphere 结构本身排除这些 endpoint-exact-alignment states。

---

## Target 3 — Targeted Exact Survivor Search

计算不再泛扫无解，而只搜：

\[
I_1,\qquad I_{\ge2},
\]

优先：

- large-\(d\) minus；
- \(d=0\) nonresonance；
- \(R=0\) / \(R_U\) small；
- active-core decimal-saturated states。

一旦找到 raw integer，立刻恢复 \(U\)。

若：

\[
\gcd(U,V)=1,
\]

立即重构 original equation。

若所有 raw integers均不互素，才正式证明 Layer P 真的存在，并将下一轮切换到 Coprime Unit Alignment。

---

# 31. Final Claim Ledger

## PROVED

1. \(u_0\mid M,N\) and complete removal of Smith presentation from ordinary endpoints；
2. intrinsic Face A/B charts；
3. exact endpoint Euclidean quotient/remainder；
4. exact modular jumps \(\delta_2,\delta_3\)；
5. half-open-correct raw survival criterion；
6. quantized one-integer threshold；
7. exact radial gap decomposition；
8. exact raw candidate count；
9. exact \(N_{\rm raw}\ge j\) threshold hierarchy；
10. presentation \(\Delta_A,\Delta_B\) reduce to intrinsic \(\delta_2,\delta_3\)；
11. decimal-content gcd lower bound；
12. reduced endpoint denominator/unit-residue theorem；
13. gap residue encoding；
14. numerator excess dictionary；
15. later-candidate arithmetic progression；
16. core endpoint theory covers \(g=0\) without special assumptions.

## CONDITIONAL / OPEN

1. global RAW extinction；
2. global \(N_{\rm raw}\le1\)；
3. global \(N_{\rm raw}\le C\)；
4. \(U=1\) closure；
5. double resonance closure；
6. RU-H × excess closure；
7. active-core decimal-saturated chamber elimination；
8. Layer P existence；
9. A1 closure.

## EXPERIMENTAL

1. current exact regression corpus contains C and \(I_0\) only；
2. no \(I_1\), \(I_{\ge2}\), or P state found in the audited corpus；
3. known \(g=0\) synchronized families/states are C/I-dead.

## FAILED AS ROUTES

1. ZGAP × remainder as an independent endpoint-phase theorem；
2. generic Smith magnitude \(\Rightarrow\) large \(\delta\)；
3. raw count \(\le1\) from interval-height heuristics alone；
4. generic prime cover before a raw survivor；
5. treating endpoint fractional parts as random/equidistributed.

---

# 32. Final Assessment

第八轮已经把 A1 压到 radial gap。

第九轮进一步证明：真正普通整数层不是一个模糊的“successor function”，而是两个完全 explicit 的 Euclidean comparisons：

\[
\boxed{
\text{Face A: }
G_A^\circ
\quad\text{vs.}\quad
C_3\delta_2+C_2,
}
\]

\[
\boxed{
\text{Face B: }
G_B^\circ
\quad\text{vs.}\quad
C_2\delta_3+C_3.
}
\]

其中：

\[
\delta_2=(-10^{n_2-1})\bmod C_2,
\]

\[
\delta_3=(-10^{n_3-1})\bmod C_3.
\]

所以本轮确实实现了：

\[
\boxed{
\textbf{A1 ordinary integer layer = two modular-jump inequalities.}
}
\]

但进一步 audit 也证明：

\[
\boxed{
\textbf{ZGAP controls exact slack, not independent endpoint phase.}
}
\]

因此当前真正剩余的数学问题已经非常明确：

\[
\boxed{
\textbf{为什么 A1 terminal arithmetic 不能让 }
10^{n_i-1}
\textbf{ 恰好足够靠近下一个 }C_i\textbf{-multiple？}
}
\]

这就是下一轮应攻击的唯一核心。

在它被解决之前：

\[
\boxed{\textbf{Raw Extinction OPEN,\quad \(A_1\) OPEN.}}
\]
