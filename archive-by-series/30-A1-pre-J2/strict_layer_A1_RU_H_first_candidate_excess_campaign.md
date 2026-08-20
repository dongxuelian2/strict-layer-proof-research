# 三项十进制拼接平方和问题：Strict Layer A1 正向线第十轮
## \(R_U\)-\(H\) × First-Candidate Excess — Raw Extinction / Survivor Discovery Campaign

**文件名：** `strict_layer_A1_RU_H_first_candidate_excess_campaign.md`  
**日期：** 2026-08-16  
**研究范围：** Strict Layer，仅 `A1-only` 正向 terminal layer。  
**本轮纪律：** 冻结前九轮宏观架构；只研究 intrinsic radial endpoints、first-candidate excess、decimal-saturated endpoint、\(U=1\)、unsaturated modular jump，以及定向 exact survivor search。  

---

# 1. Executive Summary

本轮没有证明

\[
\boxed{A_1=\varnothing}.
\]

也没有找到第一个严格 raw survivor。因此

\[
\boxed{\textbf{Global RAW Extinction — OPEN}},
\qquad
\boxed{\textbf{Layer P existence — NOT OBSERVED}},
\qquad
\boxed{\textbf{A1 — OPEN}}.
\]

但是，本轮对第九轮提出的首选闭合机制做出了两个决定性的结构裁决，并得到若干新的 exact endpoint theorem。

## 1.1 PROVED — first-candidate overflow 与 RAW survival 是精确互补，而不是 RAW 之后的第二道 gate

第九轮已经证明，Face A 第一 candidate

\[
U_0=m_A=\left\lceil\frac{10^{n_2-1}}{C_2}\right\rceil
\]

满足

\[
e_2^{(0)}=\delta_2,
\qquad
 e_3^{(0)}=\frac{C_3\delta_2-R_U}{C_2}.
\]

本轮把这个 dictionary 与 digit upper bound 完整合并，得到

\[
\boxed{
I_A\cap\mathbf Z_{>0}\ne\varnothing
\iff
0\le e_3^{(0)}<9\cdot10^{n_3-1}.
}
\tag{FC-A}
\]

Face B 对称：

\[
\boxed{
I_B\cap\mathbf Z_{>0}\ne\varnothing
\iff
0\le e_2^{(0)}<9\cdot10^{n_2-1}.
}
\tag{FC-B}
\]

所以 prompt 中希望作为“优先 theorem 1”的命题

\[
\text{RAW-A 假设}
\Longrightarrow
 e_3^{(0)}\ge9\cdot10^{n_3-1}
\]

以及 Face B 对称命题，均与 frozen RAW theorem 直接矛盾。

因此其状态必须标记为：

\[
\boxed{\textbf{FAILED — LOGICALLY IMPOSSIBLE AS STATED}.}
\]

正确的 closure target 不是“先假设 raw-live，再杀 first candidate”，而是：

> 对任意 exact terminal state，在尚未假设 RAW survival 前，用一个真正独立于 endpoint definition 的 terminal arithmetic theorem 强迫 inactive excess overflow。

这一区分是本轮最重要的逻辑校准。

---

## 1.2 PROVED — RU-H 在完整 Iterated-Smith + MNZ 下精确退化成 \(10R_U=10R_U\)

第八轮 exact bridge：

\[
\boxed{
10VR_U
=10^{m_3}H
+b_3\bigl[Q_0-P_3(1+10^{n_2})\bigr].
}
\tag{RU-H}
\]

第七、八轮同时有

\[
H=M_H^{(2)}Z,
\]

\[
\frac{\alpha J}{M_H^{(2)}}=\frac1{\beta_3},
\qquad
\beta_3=\frac{b_3}{10^{m_3}},
\]

故

\[
10^{m_3}H=\alpha J b_3 Z.
\]

又

\[
g_3=\alpha u_0t,
\qquad
\frac{b_3}{V}=\frac1{g_3},
\]

所以

\[
\boxed{
\frac{10^{m_3}H}{V}
=
\frac{JZ}{u_0t}.
}
\tag{HZV}
\]

另一方面，Iterated-Smith 的 MNZ identity 为

\[
\boxed{
Q_0+\alpha JZ
=
\alpha t(M10^{n_3}+N).
}
\tag{MNZ}
\]

并且

\[
C_2=\frac{M}{u_0},
\qquad
C_3=\frac{N}{u_0}.
\]

将 (HZV) 代入 RU-H 后除以 \(V\)：

\[
10R_U
=
\frac{JZ}{u_0t}
+
\frac{Q_0}{\alpha u_0t}
-
C_3(1+10^{n_2}).
\]

前两项合并：

\[
\frac{Q_0+\alpha JZ}{\alpha u_0t}
=
\frac{M10^{n_3}+N}{u_0}.
\]

故

\[
10R_U
=
\frac{M10^{n_3}+N-N(1+10^{n_2})}{u_0}
\]

\[
=
\frac{M10^{n_3}-N10^{n_2}}{u_0}
\]

\[
=
10\frac{M10^{n_3-1}-N10^{n_2-1}}{u_0}
=10R_U.
\]

因此：

\[
\boxed{
\textbf{RU-H 本身不是 independent magnitude source.}
}
\tag{RUH-RED}
\]

它是完整 Double-Smith/MNZ compatibility 的一个投影恒等式。

这直接否定以下本轮候选路线：

- “RU-H 单独把 \(R_U\) 推向 decade edge”；
- “把 \(H=M_H^{(2)}Z\) 代入 RU-H 后得到独立 affine \(R_U=A Z+B\)”；
- “large \(|Z|\) 仅通过 RU-H 自动导致 raw death”；
- “small \(|Z|\) 仅通过 RU-H 自动留下 finite radial states”。

这些均标记：

\[
\boxed{\textbf{FAILED AS STANDALONE RU-H ROUTES}.}
\]

若未来仍要利用 \(Z\)，必须加入一个**没有被 MNZ 吸收**的独立 sphere / sign / divisibility / endpoint-phase theorem，使 \((M,N)\) 与 \(Z\) 发生新的非恒等约束。

---

## 1.3 PROVED — Radial Decade-Budget Normal Form

令

\[
x_2:=10^{n_2-1},
\qquad
x_3:=10^{n_3-1}.
\]

Face A 定义

\[
\rho_C:=\frac{C_3x_2}{C_2x_3}\ge1,
\]

以及 normalized endpoint-jump budget

\[
\eta_A:=\frac{C_3\delta_2}{C_2x_3}\ge0.
\]

则

\[
\boxed{
\frac{e_3^{(0)}}{x_3}
=(\rho_C-1)+\eta_A.
}
\tag{DB-A1}
\]

因此

\[
\boxed{
\text{Face A raw-live}
\iff
\rho_C+\eta_A<10.
}
\tag{DB-A2}
\]

Face B 令

\[
\sigma_C:=\frac{C_2x_3}{C_3x_2}>1,
\qquad
\eta_B:=\frac{C_2\delta_3}{C_3x_2},
\]

则

\[
\boxed{
\frac{e_2^{(0)}}{x_2}
=(\sigma_C-1)+\eta_B,
}
\tag{DB-B1}
\]

\[
\boxed{
\text{Face B raw-live}
\iff
\sigma_C+\eta_B<10.
}
\tag{DB-B2}
\]

所以 ordinary integer layer 可以统一理解为：

\[
\boxed{
\textbf{radial ratio budget}
+
\textbf{endpoint modular-jump budget}
<10
}
\]

时 first integer survives；达到或超过 \(10\) 时 raw-dead。

这精确区分了 prompt 所说的两种 death mechanism：

1. geometric-edge death：ratio 接近 decade edge；
2. modular-jump death：\(\delta_i\) 消耗剩余 decade slack。

---

## 1.4 PROVED — saturated first candidate 的 exact coprimality filter

Face A saturated：

\[
\delta_2=0
\iff
C_2\mid10^{n_2-1}.
\]

由于 exact gcd profile 给

\[
\gcd(C_2,b_2)=1,
\]

若 \(p\in\{2,5\}\) 且 \(p\mid b_2\)，则 saturated \(C_2\) 不能含 \(p\)。A1 中 \(n_2\ge2\)，于是

\[
U_0=\frac{10^{n_2-1}}{C_2}
\]

必被 \(p\) 整除。又 \(b_2\mid V\)，故

\[
\boxed{
\delta_2=0,
\ p\mid\gcd(b_2,10)
\Longrightarrow
\gcd(U_0,V)>1.
}
\tag{SAT-P-A}
\]

Face B 对称：若 \(n_3\ge2\)、\(\delta_3=0\) 且 \(p\mid\gcd(b_3,10)\)，则第一 raw candidate 与 \(V\) 非互素。

特别地，Face A saturated 且 \(U_0=1\) 时

\[
C_2=10^{n_2-1},
\]

从 reducedness 立即得到

\[
\boxed{
\gcd(b_2,10)=1.
}
\tag{SAT-U1-A}
\]

Face B 若 \(n_3\ge2\) 同理；\(n_3=1\) 时 saturated 只给 \(C_3=1,U_0=1\)，必须单列。

注意：这只杀**第一 candidate**；saturated interval 可能含 later candidates，所以不能冒充 saturated chamber closure。

---

## 1.5 PROVED — saturated active interval 本身往往支持很多 integers

Face A saturated 时

\[
L_2=U_0\in\mathbf Z,
\qquad
I_2=[U_0,10U_0).
\]

因此仅从 active block 看，恰有

\[
\boxed{9U_0}
\]

个 positive integer positions。

于是 saturated endpoint 并不是“天然 single-candidate chamber”；恰恰相反，它是 \(I_{\ge2}\) 的危险来源之一。真正 candidate count 由 inactive upper endpoint 截断。

Face B 对称。

---

## 1.6 PROVED — \(U=1\) 一旦出现，不可能属于 Layer P

\[
U=1
\iff
10^{n_2-1}\le C_2<10^{n_2},
\qquad
10^{n_3-1}\le C_3<10^{n_3}.
\]

并且

\[
\gcd(1,V)=1.
\]

forward reconstruction theorem 已冻结：exact synchronized primitive/word/gcd state + denominator legality + legal coprime common \(U\) 已足够恢复 original strict candidate。

所以：

\[
\boxed{
\text{任何 exact terminal }U=1\text{ state 都是 full radial survivor，}
}
\]

而不是 Layer P。

若找到它，必须立即恢复原题；若 original no-solution conjecture正确，则 \(U=1\) 必须在 terminal state 形成之前被结构性排除。

本轮仍未得到这种 global 排除。

---

## 1.7 EXPERIMENTAL — targeted exact survivor search 仍未发现 \(I_1/I_{\ge2}/P\)

本轮没有做 general random search，而是使用 exact integer arithmetic、primitive master+sphere 联立、二次判别式 exact-square test，并对 \(C_1\) 作代数消元。

新增定向 finite slices 中均未发现 raw-live exact terminal state：

1. \(g=0,m_2=m_3=n_3=1\)，三 denominator blocks 全为一位数，\(k=1,2,3\)；对每个 \(k\)，只扫描 raw 可能区间所必需的
   \[
   1\le C_2<10^{k+1},\qquad1\le C_3\le9,
   \]
   并 exact 消去 \(C_1\)：0 hits。

2. \(g=0,(m_2,n_3,k)=(2,1,1)\)，\(b_1\) 一位、\(b_2\) 两位、\(b_3\) 一位；raw 必需
   \[
   C_2\le999,\quad C_3\le9.
   \]
   在 27,023,535 个 reduced \((b,C_2,C_3)\) tuple 上出现 19 个 perfect-discriminant events，但 0 个通过完整 integer/root/primitive/\(D>0\) terminal checks。

3. \(g=0,(m_2,n_3,k)=(1,2,1)\)，\(b_1\) 一位、\(b_2\) 一位、\(b_3\) 两位；raw 必需
   \[
   C_2\le99,\quad C_3\le99.
   \]
   28,285,308 个 reduced tuples，29 个 perfect-discriminant events，0 terminal hits。

4. 第一条 \(g\ge1\) transition slice：
   \[
   (g,d,n_3,k)=(1,0,1,1),
   \]
   \(b_1\) 一位、\(b_2\) 一位、\(b_3\) 两位；raw 必需
   \[
   C_2\le999,\quad C_3\le9.
   \]
   27,451,836 个 reduced tuples，4 个 perfect-discriminant events，0 terminal hits。

5. 同一 transition slice 的 \(U=1\) 专门搜索：24,721,272 个 reduced tuples，2 个 perfect-discriminant events，0 terminal hits。

6. double-resonant \(U=1\) 定向盒：\(g\le2,n_3\le2,k\le4,b_1\le100\)，\(b_2\) 枚举完整 \(g\)-digit range，并用
   \[
   C_2=10^{n_2-n_3}C_3
   \]
   强制 \(R_U=0\)。530,000 个 reduced parameter tuples 中没有一个 perfect quadratic discriminant，更没有 terminal hit。

这些是 **EXPERIMENTAL exact finite exhaustions**，不是 global proof；尤其 \(b_1\) 或 profile 仍可移动，不能把“0 hits”升级成 theorem。

---

## 1.8 Notation Audit — `RAW-A/RAW-B` 标签在第九轮文本中有一次反向复用

本轮回查发现：第九轮前部把

\[
G_A^\circ\ge C_3\delta_2+C_2
\]

作为 **raw-live criterion**；但第九轮后部的 “Status of Raw Extinction” 又把目标 dead inequality

\[
G_A^\circ<C_3\delta_2+C_2
\]

也标成 `(RAW-A)`。Face B 同样存在这一标签复用。

为避免本轮再发生逻辑混淆，本文不再用裸标签 `RAW-A/RAW-B` 指代方向，而统一写：

- **raw-live:** \(G_A^\circ\ge C_3\delta_2+C_2\)（Face B 对称）；
- **raw-dead:** \(G_A^\circ<C_3\delta_2+C_2\)。

这也解释了为什么“RAW-A 假设后证明 overflow”必须先明确 RAW-A 到底指 live 还是 dead；本 prompt 明确冻结的是 live criterion，因此该版本与 overflow 直接互斥。

---

# 2. Frozen Nine-Round Results

本轮冻结以下结果，不重新搭建宏观架构。

## 2.1 Primitive/common-scale state

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

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

## 2.2 A1 exponent chart

\[
g=m_3-n_3\ge0,
\qquad k\ge1,
\qquad d=m_2-g,
\]

\[
\boxed{
m_2=g+d,
\quad n_2=2g+k+d,
\quad m_3=n_3+g.
}
\]

## 2.3 Exact word defects

\[
D=P_110^k-Q_0>0,
\]

\[
\boxed{
H=b_2Q_0-b_110^{m_2}D\ne0.
}
\]

plus iff \(H<0\)，minus iff \(H>0\)。

尾部：

\[
\boxed{
10^{m_3}H
=b_2P_210^{n_3}-b_3(Q_0-P_3).
}
\tag{H3}
\]

## 2.4 Full Smith / radial cancellation

\[
b_1=s\alpha u,
\quad
b_2=s\alpha\beta t,
\quad
b_3=s\beta v,
\]

\[
\gamma=\gcd(u,v),
\quad u=\gamma u_0,
\quad v=\gamma v_0,
\]

\[
V=s\alpha\beta\gamma u_0tv_0.
\]

\[
P_2=vM,
\qquad
P_3=\alpha tN,
\qquad
u_0\mid M,N.
\]

因此

\[
\boxed{
C_2=M/u_0,
\qquad
C_3=N/u_0.
}
\]

## 2.5 Iterated-Smith core

\[
H=M_H^{(2)}Z,
\qquad
M_H^{(2)}=s\alpha\beta^\sharp v^\sharp,
\qquad Z\ne0,
\]

\[
 tM10^{n_3}-A_3=JZ,
\qquad
 A_3=(Q_0-P_3)/\alpha,
\]

\[
\frac{\alpha J}{M_H^{(2)}}=\frac1{\beta_3},
\qquad
\beta_3=b_3/10^{m_3}.
\]

以及

\[
Q_0+\alpha JZ
=\alpha t(M10^{n_3}+N).
\]

## 2.6 Intrinsic radial endpoints

\[
L_2=\frac{10^{n_2-1}}{C_2},
\qquad
R_2=\frac{10^{n_2}}{C_2},
\]

\[
L_3=\frac{10^{n_3-1}}{C_3},
\qquad
R_3=\frac{10^{n_3}}{C_3}.
\]

---

# 3. Exact Intrinsic Radial State

定义

\[
\boxed{
R_U=C_210^{n_3-1}-C_310^{n_2-1}.
}
\]

则

\[
R_U\le0
\iff
L_2\ge L_3
\]

为 Face A；

\[
R_U>0
\iff
L_3>L_2
\]

为 Face B。

Face A：

\[
I_A=
\left[
\frac{10^{n_2-1}}{C_2},
\frac{10^{n_3}}{C_3}
\right),
\]

\[
G_A^\circ=C_210^{n_3}-C_310^{n_2-1}.
\]

Face B：

\[
I_B=
\left[
\frac{10^{n_3-1}}{C_3},
\frac{10^{n_2}}{C_2}
\right),
\]

\[
G_B^\circ=C_310^{n_2}-C_210^{n_3-1}.
\]

continuous-live iff对应 \(G^\circ>0\)。

---

# 4. Verification of RU-H

从

\[
VC_i=b_iP_i
\]

有

\[
VR_U
=b_2P_2 10^{n_3-1}-b_3P_3 10^{n_2-1}.
\]

乘 \(10\)：

\[
10VR_U
=b_2P_210^{n_3}-b_3P_310^{n_2}.
\]

由 (H3)：

\[
b_2P_210^{n_3}
=10^{m_3}H+b_3(Q_0-P_3).
\]

代入：

\[
10VR_U
=10^{m_3}H
+b_3(Q_0-P_3)
-b_3P_310^{n_2}.
\]

所以

\[
\boxed{
10VR_U
=10^{m_3}H
+b_3[Q_0-P_3(1+10^{n_2})].
}
\]

系数 \(10V\)、指数 \(m_3\)、符号以及 \((1+10^{n_2})\) 全部核准。

**状态：PROVED.**

---

# 5. Verification of First-Candidate Excess

Face A：

\[
\delta_2=(-10^{n_2-1})\bmod C_2,
\]

\[
m_AC_2=10^{n_2-1}+\delta_2.
\]

取 \(U_0=m_A\)，则

\[
\boxed{e_2^{(0)}=\delta_2.}
\]

又 general excess identity

\[
C_3e_2-C_2e_3=R_U
\]

给

\[
\boxed{
e_3^{(0)}
=\frac{C_3\delta_2-R_U}{C_2}.
}
\]

Face B 完全对称：

\[
\boxed{e_3^{(0)}=\delta_3,}
\]

\[
\boxed{
e_2^{(0)}
=\frac{R_U+C_2\delta_3}{C_3}.
}
\]

**状态：PROVED / frozen formula re-audited.**

---

# 6. Intrinsic Simplification of RU-H

本节给出本轮最关键的新 algebra audit。

由 BAL：

\[
M_H^{(2)}=\alpha J\beta_3
=\alpha J\frac{b_3}{10^{m_3}}.
\]

所以

\[
10^{m_3}H
=10^{m_3}M_H^{(2)}Z
=\alpha Jb_3Z.
\]

除 \(V\)：

\[
\frac{10^{m_3}H}{V}
=\alpha JZ\frac{b_3}{V}
=\frac{\alpha JZ}{g_3}
=\frac{JZ}{u_0t}.
\]

RU-H 因而写成

\[
10R_U
=
\frac{JZ}{u_0t}
+
\frac{Q_0}{\alpha u_0t}
-
C_3(1+10^{n_2}).
\]

再用 MNZ：

\[
Q_0+\alpha JZ
=\alpha t(M10^{n_3}+N),
\]

立即得到

\[
10R_U=10R_U.
\]

### Theorem A1-RUH-1 — Full-Smith RU-H Redundancy

在完整 Iterated-Smith terminal state 上，RU-H 不提供独立于 MNZ 与 \(C_2=M/u_0,C_3=N/u_0\) 的 affine / magnitude constraint。

**状态：NEW PROVED.**

### Consequence

\(Z\) 是 transverse word-defect coordinate；radial endpoint本身只读

\[
(M,N,u_0;n_2,n_3).
\]

因此：

\[
\boxed{
R_U\text{ 在 intrinsic chart 中不以 }Z\text{ 为独立自由度。}
}
\]

任何未来 \(Z\to R_U\) theorem 必须先证明一个额外关系，使 \((M,N)\) 受 \(Z\) 约束；不能从 RU-H 本身获得。

---

# 7. Face A First-Candidate Analysis

写

\[
x_2=10^{n_2-1},\qquad x_3=10^{n_3-1}.
\]

Face A：

\[
R_U=C_2x_3-C_3x_2\le0.
\]

第一 candidate：

\[
U_0=m_A,
\qquad
m_AC_2=x_2+\delta_2.
\]

inactive excess：

\[
e_3^{(0)}
=\frac{C_3\delta_2-R_U}{C_2}.
\]

展开 \(R_U\)：

\[
e_3^{(0)}
=\frac{C_3(\delta_2+x_2)}{C_2}-x_3
=m_AC_3-x_3.
\]

因此

\[
e_3^{(0)}<9x_3
\iff
m_AC_3<10x_3
\iff
m_A<\frac{10^{n_3}}{C_3}.
\]

右侧正是 \(U_0\in I_A\) 的 inactive upper test。

所以：

\[
\boxed{
\text{Face A first-candidate inactive excess legality}
\iff
\text{Face A raw survival}.
}
\]

这不是新的 gate，而是同一 gate 的 numerator-coordinate 表示。

---

# 8. Face B First-Candidate Analysis

完全对称。

\[
R_U=C_2x_3-C_3x_2>0.
\]

\[
U_0=m_B,
\qquad
m_BC_3=x_3+\delta_3.
\]

\[
e_2^{(0)}
=\frac{R_U+C_2\delta_3}{C_3}
=m_BC_2-x_2.
\]

所以

\[
e_2^{(0)}<9x_2
\iff
m_B<\frac{10^{n_2}}{C_2}
\iff
U_0\in I_B.
\]

即：

\[
\boxed{
\text{Face B first-candidate inactive excess legality}
\iff
\text{Face B raw survival}.
}
\]

---

# 9. Inactive Excess Overflow

本轮因此必须重新表述“overflow theorem”。

错误版本：

\[
\text{RAW-live}\Longrightarrow\text{overflow}.
\]

正确可能版本：

### Face A independent overflow target

对任意 admissible Face A terminal state，证明

\[
\boxed{
C_3\delta_2-R_U
\ge
9C_2x_3.
}
\tag{OF-A}
\]

这将直接推出 raw-dead，但**不能先假设 RAW-A**。

### Face B independent overflow target

\[
\boxed{
R_U+C_2\delta_3
\ge
9C_3x_2.
}
\tag{OF-B}
\]

本轮没有证明 (OF-A)/(OF-B)。

并且 RU-H 无法独立提供它们，因为 RU-H 在 full Smith 下退化为恒等式。

**状态：OPEN, with RU-H standalone route FAILED.**

---

# 10. Radial Ratio Normalization

Face A：

\[
\rho_C:=\frac{C_3x_2}{C_2x_3}\in[1,10)
\]

on continuous-live states。

于是

\[
-R_U=C_2x_3(\rho_C-1),
\]

\[
e_3^{(0)}
=\frac{C_3\delta_2}{C_2}+x_3(\rho_C-1).
\]

定义

\[
\eta_A:=\frac{C_3\delta_2}{C_2x_3}.
\]

则

\[
\boxed{
\frac{e_3^{(0)}}{x_3}=\rho_C-1+\eta_A.
}
\]

raw-live iff

\[
\boxed{\rho_C+\eta_A<10.}
\]

Face B 定义 reciprocal ratio

\[
\sigma_C:=\frac{C_2x_3}{C_3x_2}>1,
\]

\[
\eta_B:=\frac{C_2\delta_3}{C_3x_2},
\]

得到

\[
\boxed{
\frac{e_2^{(0)}}{x_2}=\sigma_C-1+\eta_B,
}
\]

\[
\boxed{\sigma_C+\eta_B<10\iff\text{raw-live}.}
\]

这就是本轮建议冻结的新 ordinary-integer normal form：

\[
\boxed{\textbf{Decade Budget}.}
\]

---

# 11. Decimal-Saturated Face A

Face A saturated：

\[
\delta_2=0
\iff
C_2\mid x_2.
\]

所以

\[
C_2=2^a5^b,
\qquad
0\le a,b\le n_2-1.
\]

此时

\[
U_0=\frac{x_2}{C_2}\in\mathbf Z_{>0}
\]

且

\[
e_2^{(0)}=0,
\qquad
 e_3^{(0)}=-\frac{R_U}{C_2}
=x_3(\rho_C-1).
\]

因此

\[
\boxed{
\text{continuous-live}\iff\rho_C<10
\iff\text{raw-live}.
}
\]

所以 saturated chamber 不可能靠 ordinary endpoint jump 自杀。

### New exact reducedness consequence

\[
\gcd(C_2,b_2)=1.
\]

若 \(2\mid b_2\) 或 \(5\mid b_2\)，则该 prime 不进入 \(C_2\)，于是进入 \(U_0=x_2/C_2\)。故

\[
\gcd(U_0,V)>1.
\]

这给出第一 candidate 的 exact Layer-P filter，但不能排除 later candidates。

### Ten-free part of \(P_2\)

因为

\[
P_2=g_2C_2
\]

且 \(C_2\) 仅含 \(2,5\)，故所有 non-\((2,5)\) prime powers of \(P_2\) 全部进入 \(g_2\mid V\)：

\[
\boxed{
P_2^{\langle10\rangle}\mid g_2\mid V.
}
\]

**状态：PROVED structural restriction, insufficient for RAW closure.**

---

# 12. Decimal-Saturated Face B

Face B：

\[
\delta_3=0
\iff
C_3\mid x_3.
\]

若 \(n_3\ge2\)，完全对称得到：

\[
C_3=2^a5^b,
\]

\[
U_0=x_3/C_3,
\]

\[
\gcd(C_3,b_3)=1,
\]

且任何 \(p\in\{2,5\}\cap\operatorname{supp}(b_3)\) 均强迫

\[
p\mid\gcd(U_0,V).
\]

若 \(n_3=1\)，则

\[
x_3=1,
\qquad
\delta_3=0\iff C_3=1,
\]

从而

\[
U_0=1.
\]

这个边界不能由 coprimality 杀掉，必须直接进入 \(U=1\) chamber。

---

# 13. \(U=1\) Chamber

\[
U=1
\]

合法 iff

\[
10^{n_2-1}\le C_2<10^{n_2},
\]

\[
10^{n_3-1}\le C_3<10^{n_3}.
\]

此时

\[
a_2=C_2,
\qquad
 a_3=C_3,
\]

且完整 primitive recovery 给

\[
a_1=C_1.
\]

所以

\[
\boxed{
\gcd(a_1,a_2,a_3)=U=1.
}
\]

更重要的是：

\[
\gcd(1,V)=1.
\]

因此 \(U=1\) 绝不属于 Layer P。

### Exact word simplification

common scale \(\lambda=1/V\)，故完整 concatenated ratio 满足

\[
\boxed{
\frac AB=\frac{Q_0}{V},
\qquad
VA=Q_0B.
}
\tag{U1-BAL}
\]

令

\[
d_0:=\gcd(Q_0,V),
\]

则

\[
\boxed{
V/d_0\mid B,
\qquad
Q_0/d_0\mid A.
}
\]

这是 exact balance divisibility，但本轮没有从中推出 uniform contradiction。

### Status

\[
\boxed{U=1\textbf{ remains OPEN globally}.}
\]

任何未来发现的 exact \(U=1\) state 都必须立即 original reconstruction；不能把它留在 abstract radial ledger。

---

# 14. Unsaturated Endpoint Decomposition

Face A unsaturated：

\[
\delta_2>0.
\]

定义

\[
h_2:=\gcd(C_2,x_2),
\]

\[
C_2=h_2C_2^*,
\qquad
x_2=h_2x_2^*,
\]

\[
\gcd(C_2^*,x_2^*)=1.
\]

则

\[
\boxed{
\delta_2=h_2\delta_2^*,
}
\]

其中

\[
\delta_2^*\equiv-x_2^*\pmod{C_2^*},
\]

\[
1\le\delta_2^*<C_2^*,
\qquad
\gcd(\delta_2^*,C_2^*)=1.
\]

Face B 对称。

**状态：PROVED / frozen ninth-round theorem re-audited.**

---

# 15. \(h_i,C_i^*,\delta_i^*\)

若

\[
C_i=2^a5^br,
\qquad
\gcd(r,10)=1,
\]

记 \(N_i=n_i-1\)，则

\[
\boxed{
h_i
=2^{\min(a,N_i)}5^{\min(b,N_i)}.
}
\]

\[
\boxed{
C_i^*
=2^{\max(a-N_i,0)}5^{\max(b-N_i,0)}r.
}
\]

所以 \(C_i^*\) 精确包含：

- ten-free core \(r\)；
- 超过 decimal power capacity 的 excess \(2/5\)-valuation。

最弱 nonzero jump：

\[
\boxed{\delta_i\ge h_i.}
\]

因此 Face A 可由

\[
G_A^\circ<C_3h_2+C_2
\]

充分判死；Face B 对称。

本轮没有证明这两个 inequality 对所有 terminal states成立。

### ten-free chamber

若 \(n_i\ge2\) 且 \(\gcd(C_i,10)=1\)，则 \(h_i=1\)，上述 weak lower bound 仅给

\[
\delta_i\ge1.
\]

所以 ten-free endpoint 正是 modular-jump route 最薄弱的 chamber。

---

# 16. \(Z\)-Dependence of \(R_U\)

Intrinsic Smith chart：

\[
\boxed{
R_U
=\frac{M10^{n_3-1}-N10^{n_2-1}}{u_0}.
}
\]

它只读

\[
(M,N,u_0;n_2,n_3).
\]

虽然 RU-H 表面含 \(H\sim Z\)，但第 6 节证明完整消元后 \(Z\) 消失。

所以本轮正式冻结：

\[
\boxed{
\textbf{Z is transverse to the intrinsic radial coordinate unless an additional coupling theorem is supplied.}
}
\]

这解释了为何此前 ZGAP / RU-H 反复消元后都会退回 endpoint/slack identity。

---

# 17. Large-\(|Z|\) Chamber

prompt 候选：

\[
|Z|\text{ large}
\Longrightarrow
|R_U|\text{ large}
\Longrightarrow
\text{overflow}.
\]

本轮裁决：

\[
\boxed{\textbf{FAILED AS A CONSEQUENCE OF RU-H ALONE}.}
\]

原因是 MNZ 同时移动 \(Q_0\)：

\[
Q_0
=\alpha t(M10^{n_3}+N)-\alpha JZ.
\]

对 fixed \((M,N)\)，\(Z\) 改变 \(Q_0\) 而不改变 \(R_U\)。

只有未来另证 sphere/branch arithmetic 将 \(M/N\) 与 \(Z\) 锁定，large-\(|Z|\) 才可能重新有 radial power。

---

# 18. Small-\(|Z|\) Chamber

同理，small \(|Z|\) 并不自动使 \((M,N)\) 落入 finite set。

已知

\[
Q_0+\alpha JZ=\alpha t(M10^{n_3}+N)
\]

只固定一个 affine combination；\(M,N,Q_0\) 仍可同步移动。

因此：

\[
\boxed{
\text{“small }|Z|\Rightarrow\text{ finite terminal states”}
\textbf{ remains UNPROVED / FAILED as a direct inference}.}
\]

---

# 19. \(d=0\)

\[
d=0
\Longrightarrow
n_2=2g+k.
\]

这里 endpoint exponent 与 primitive axis exponent exact 对齐，因此仍是高价值 chamber。

但：

- denominator resonance \(R=0\) 落在 \(d=0\)；
- \(R_U=0\) 与 \(d=0\) 可完全兼容；
- parallel resonant audit 已证明 exact center 是 maximal radial-overlap danger zone，而不是自动 Layer-I death。

本轮新增 finite search：\(g=1,d=0,n_3=1,k=1\) 的一位-leading-denominator raw-possible slice 为 0 hits，但不能升级成 general \(d=0\) theorem。

**状态：OPEN globally / EXPERIMENTALLY strengthened.**

---

# 20. Large-\(d\) Minus

对 \(g\ge1,d\ge2\) 已知为 minus。

已有 primitive lower bound

\[
P_3>
\frac{Q_0}{1100\,10^{2g+k}}.
\]

而

\[
n_2=2g+k+d.
\]

若 \(d\ge4\)，则

\[
P_310^{n_2}
>
Q_0\frac{10^d}{1100}
>Q_0.
\]

故

\[
\boxed{
d\ge4\Longrightarrow
T_U:=Q_0-P_3(1+10^{n_2})<0.
}
\tag{TU-LD}
\]

这是一个真实 sign theorem。

但 minus 中 \(H>0\)，所以 RU-H 的两项异号，仍可能 cancellation；而且第 6 节说明完整 Smith 消元后 RU-H 不产生 independent magnitude。

因此 (TU-LD) 是 useful branch fact，但不闭合 large-\(d\) minus。

**状态：NEW DERIVED SIGN FACT / closure OPEN.**

---

# 21. Double Resonance

双共振：

\[
R=0,
\qquad
R_U=0.
\]

已有

\[
P_2=10^{2g+k}P_3,
\]

\[
P_1^2+(10^{4g+2k}+1)P_3^2=Q_0^2.
\]

以及

\[
C_2=10^{n_2-n_3}C_3.
\]

radial interval 因而最大对齐：

\[
L_2=L_3=L,
\qquad
I_{23}=[L,10L).
\]

所以 double resonance 确实是寻找 raw survivor 的优先实验区，而不是容易杀的区。

### \(U=1\) inside double resonance

若 \(C_3\) 恰有 \(n_3\) 位，则

\[
C_2=10^{n_2-n_3}C_3
\]

自动恰有 \(n_2\) 位，故 \(U=1\) 与 radial geometry 完全兼容。

本轮 bounded exact search 未命中 terminal state，但没有 global contradiction。

parallel resonance audit 还给出 endpoint equality restrictions：在 denominator resonance 中，second-lower equality 强迫 \(U=1,C_2=10^{n_2-1}\)；third-lower equality只可能在 \(n_3=1,U=C_3=1\)。这些进一步说明 \(U=1\) 是 resonance boundary 的真实 exceptional core，而不是可以忽略的退化点。

**状态：OPEN.**

---

# 22. \(g=0\)

第六轮已经证明 denominator resonance \(R=0\) 在 \(g=0\) 不可能，但 ordinary radial endpoint chart 与 RU-H 都仍适用。

known \(g=0\) synchronized states与 explicit infinite pseudo-family均在 C/I 层死亡；这不是 global theorem。

本轮的 exact finite survivor scans 显著扩大了 \(g=0\) 的 audited raw-possible region：

- one-digit denominator, \(k=1,2,3\)：0 raw terminal hits；
- \((m_2,n_3,k)=(2,1,1)\)：0；
- \((1,2,1)\)：0。

因此：

\[
\boxed{g=0\textbf{ remains OPEN globally, but no raw survivor has been found}.}
\]

---

# 23. Targeted Raw-Survivor Search

## 23.1 Exact elimination method

固定 denominator profile 与 \((C_2,C_3)\) 后，令

\[
A
=C_1 10^{n_2+n_3}+C_2 10^{n_3}+C_3,
\]

\[
B
=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3.
\]

primitive master 为

\[
VA=Q_0B.
\]

又

\[
P_i=g_iC_i,
\qquad
P_1^2+P_2^2+P_3^2=Q_0^2.
\]

消去 \(Q_0=VA/B\)，得到关于 \(C_1\) 的 exact quadratic：

\[
B^2\bigl[(g_1C_1)^2+(g_2C_2)^2+(g_3C_3)^2\bigr]
=
V^2\bigl(C_110^{n_2+n_3}+C_210^{n_3}+C_3\bigr)^2.
\]

本轮对判别式只使用 integer square test；不使用 floating point。

每个 root 再 exact 检查：

- \(C_1\in\mathbf Z_{>0}\)；
- \(\gcd(C_i,b_i)=1\)；
- master divisibility；
- primitive sphere；
- \(\gcd(P_1,P_2,P_3,Q_0)=1\)；
- \(D=P_110^k-Q_0>0\)；
- declared profile / digit ranges；
- radial interval与 raw candidates。

## 23.2 Why raw boxes are finite in the audited slices

若某 positive integer \(U\) legal，则

\[
UC_2<10^{n_2},
\qquad
UC_3<10^{n_3}.
\]

因 \(U\ge1\)：

\[
C_2\le10^{n_2}-1,
\qquad
C_3\le10^{n_3}-1.
\]

所以针对 fixed \((n_2,n_3)\) 的“raw-possible core box”是 exact finite，不需要人为 primitive-height cutoff。

## 23.3 Search verdict

当前所有新增 exact slices均为 0 raw terminal hits。

\[
\boxed{
\textbf{No }I_1,
\ I_{\ge2},
\ P,
\textbf{ or coprime radial survivor discovered.}
}
\]

**状态：EXPERIMENTAL / finite exact census only.**

---

# 24. Layer C / \(I_0\) / \(I_1\) / \(I_{\ge2}\) / P Ledger

本轮统一 ledger：

### Layer C

\[
I_{23}=\varnothing.
\]

已有多个 known synchronized regression states与 infinite pseudo-family在此死亡。

### Layer \(I_0\)

\[
I_{23}\ne\varnothing,
\qquad
I_{23}\cap\mathbf Z_{>0}=\varnothing.
\]

已有 exact regression states。

### Layer \(I_1\)

\[
N_{\rm raw}=1.
\]

当前没有 exact terminal witness。

### Layer \(I_{\ge2}\)

\[
N_{\rm raw}\ge2.
\]

当前没有 exact terminal witness。

### Layer P

\[
N_{\rm raw}\ge1,
\qquad
N_V=0.
\]

当前没有 exact terminal witness。

### Full radial survivor

\[
\exists U\in I_{23}\cap\mathbf Z_{>0},
\quad
\gcd(U,V)=1.
\]

当前没有 witness；若出现必须立即 original reconstruction。

---

# 25. \(U=1\) Search Results

本轮特别把 \(U=1\) 当作“若存在则直接 full survivor”的危险 chamber，而不是 coprimality 旁支。

有限 exact searches：

1. 所有本轮 raw-possible g=0 slices自动包含 \(U=1\) states，均 0 terminal hits；
2. \((g,d,n_3,k)=(1,0,1,1)\) transition 的专门 \(U=1\) scan：0 hits；
3. bounded double-resonant \(U=1\) scan：0 hits。

因此：

\[
\boxed{
\textbf{No }U=1\textbf{ terminal state found, but no global theorem excludes it.}
}
\]

---

# 26. Coprime Check for Actual Raw Survivors

本轮没有找到 strict raw survivor，因此没有 genuine Layer-P gcd ledger 可填写。

但是 saturated first-candidate theorem (SAT-P-A/B) 给出一个 conditional exact rule：

- saturated active block；
- first candidate \(U_0>1\)；
- active denominator含 \(2\) 或 \(5\)；

则第一 candidate 必 noncoprime。

它展示了 coprimality 可能如何真实激活，但目前尚无 exact terminal state使其成为一个 actual Layer-P witness。

---

# 27. Original-Equation Verification if Needed

本轮无 coprime radial survivor，所以没有 original candidate 需要重构。

冻结 protocol：若未来发现

\[
U\in I_{23}\cap\mathbf Z_{>0},
\qquad
\gcd(U,V)=1,
\]

立即取

\[
a_i=UC_i,
\qquad
b_i=V/g_i,
\]

恢复完整 words

\[
A=a_110^{n_2+n_3}+a_210^{n_3}+a_3,
\]

\[
B=b_110^{m_2+m_3}+b_210^{m_3}+b_3,
\]

并 exact 验证

\[
\left(\frac{a_1}{b_1}\right)^2
+
\left(\frac{a_2}{b_2}\right)^2
+
\left(\frac{a_3}{b_3}\right)^2
=
\left(\frac AB\right)^2.
\]

forward reconstruction theorem说明：若上述 terminal hypotheses均真实，理论上该 equality 应自动成立；若失败则意味着 reconstruction implementation 或 semantic gate 有 bug，必须立即定位。

---

# 28. Failed Conjectures

## FAILED 1 — “RAW-live 后 first candidate overflow”

直接与 exact RAW/excess equivalence矛盾。

## FAILED 2 — “RU-H 是 independent radial magnitude source”

full Smith + BAL + MNZ 后退化为 \(10R_U=10R_U\)。

## FAILED 3 — “RU-H gives affine \(R_U=A Z+B\) with useful independent spacing”

\(Z\)-term被 \(Q_0\) 的 MNZ dependence 精确吸收。

## FAILED 4 — “large \(|Z|\) automatically raw-dead through RU-H”

无额外 \((M,N)\)-\(Z\) coupling theorem 时不成立。

## FAILED 5 — “small \(|Z|\) automatically leaves finite states”

MNZ 仍允许 \((M,N,Q_0)\) moving。

## FAILED 6 — “saturated endpoint should be RAW-impossible”

相反，saturated + continuous-live 自动 raw-live。

## FAILED 7 — “saturated first candidate被 coprimality杀掉即可关闭 saturated chamber”

later candidates可以存在；active interval本身有 \(9U_0\) 个 integer positions。

## FAILED 8 — “\(U=1\) 可由 denominator prime richness处理”

\(\gcd(1,V)=1\) 恒成立。

## FAILED 9 — “sphere mod \(C_2^*\) 自动控制 endpoint decimal residue”

由 \(C_2^*\mid P_2\) 只能得到

\[
P_1^2+P_3^2\equiv Q_0^2\equiv d_2^2\pmod{C_2^*},
\]

这只是 sphere identity 的 residue shadow，没有把 \(10^{n_2-1}\bmod C_2^*\) 读出来。

## FAILED / OPEN 10 — “Global RAW extinction”

没有被证伪，也没有被证明；当前 finite exact searches仍为 0 survivor。

---

# 29. New Proven Lemmas

## A1-RUH-1 — Full-Smith RU-H Redundancy

RU-H + BAL + MNZ 精确化简为 \(10R_U=10R_U\)。

## A1-FC-1 — Face A First-Candidate Equivalence

\[
I_A\cap\mathbf Z_{>0}\ne\varnothing
\iff
0\le e_3^{(0)}<9\cdot10^{n_3-1}.
\]

## A1-FC-2 — Face B First-Candidate Equivalence

\[
I_B\cap\mathbf Z_{>0}\ne\varnothing
\iff
0\le e_2^{(0)}<9\cdot10^{n_2-1}.
\]

## A1-DB — Decade-Budget Normal Form

Face A：

\[
\rho_C+\eta_A<10
\iff\text{raw-live}.
\]

Face B：

\[
\sigma_C+\eta_B<10
\iff\text{raw-live}.
\]

## A1-SAT-P — Saturated First-Candidate Decimal-Prime Filter

若 active saturated core 与 active denominator共享 decimal prime channel（通过 denominator，而非 core），则 first candidate 与 \(V\) 非互素。

## A1-SAT-U1 — Saturated \(U_0=1\) Denominator Unit Restriction

Face A saturated \(U_0=1\) 强迫 \(\gcd(b_2,10)=1\)；Face B 对 \(n_3\ge2\) 对称。

## A1-U1-FULL — \(U=1\) Cannot Be Layer P

任何 exact terminal \(U=1\) state自动为 coprime radial survivor，必须 original reconstruction。

## A1-COUNT-EX — Excess Candidate Count

Face A 定义

\[
J_2=
\left\lfloor
\frac{9x_2-1-\delta_2}{C_2}
\right\rfloor,
\]

\[
J_3=
\left\lfloor
\frac{9x_3-1-e_3^{(0)}}{C_3}
\right\rfloor.
\]

则

\[
\boxed{
N_A
=
\max\bigl(0,1+\min(J_2,J_3)\bigr).
}
\]

Face B 对称。

这是 later-candidate arithmetic progression 的 exact count form。

---

# 30. Global RAW Extinction Status

本轮没有证明

\[
\boxed{I_{23}\cap\mathbf Z_{>0}=\varnothing}
\]

for every exact A1 terminal state。

更重要的是，本轮证明了第九轮建议的核心 `RU-H × first-candidate overflow` 不能以原形式完成：

1. first-candidate overflow 是 RAW survival 的精确补集；
2. RU-H 在 full Smith/MNZ 后不含 independent radial information。

因此当前最小 global RAW theorem 应改写为：

### A1-DBE — Direct Decade-Budget Exclusion

证明所有 exact A1 terminal states 均满足：

Face A：

\[
\boxed{
\rho_C
+
\frac{C_3\delta_2}{C_2 10^{n_3-1}}
\ge10,
}
\]

或 Face B：

\[
\boxed{
\sigma_C
+
\frac{C_2\delta_3}{C_3 10^{n_2-1}}
\ge10.
}
\]

关键要求：证明必须来自一个**独立 endpoint-phase / master-sphere correlation**，不能再次使用等价的 radial slack identity。

\[
\boxed{\textbf{Global RAW Extinction — OPEN}.}
\]

---

# 31. Layer P Existence Status

当前所有 audited exact terminal states：

- either Layer C；
- or Layer \(I_0\)；
- 新 finite searches则在形成 raw terminal hit之前已空。

因此：

\[
\boxed{\textbf{Layer P has still not been empirically activated}.}
\]

但本轮 saturated first-candidate theorem第一次给出了一个非常具体的 conditional P mechanism：若 saturated raw terminal state出现，且 active denominator带 decimal prime，则 first candidate可被该 prime exact kill。

这还不是 Layer P existence theorem，因为 later candidates与 terminal-state existence均未解决。

---

# 32. A1 Closure Status

\[
\boxed{A_1\textbf{ remains OPEN}.}
\]

本轮没有发现 full coprime radial survivor，所以也没有推翻 strict no-solution conjecture或 reconstruction theorem。

但是 terminal frontier 已被重新校准：

\[
\boxed{
\text{不要再追 }
H\to R_U
\text{ 的 standalone magnitude chain。}
}
\]

完整 Smith 后，真正 radial information只在

\[
\boxed{(C_2,C_3;n_2,n_3)\quad\text{或}\quad(M,N,u_0;n_2,n_3)}
\]

中。

剩余独立 arithmetic 必须直接作用于：

\[
\boxed{
10^{n_i-1}\bmod C_i
}
\]

或直接约束 decade ratio \(C_3x_2/(C_2x_3)\)，而不是再次通过已被消去的 RU-H/ZGAP 投影绕回去。

---

# 33. Recommended Next Campaign / Closure Audit

本轮之后，最值得继续的方向不应再命名为 RU-H campaign。

建议下一轮只保留三个 targets：

## Target 1 — Direct Endpoint Phase × Decade Budget

直接研究

\[
\delta_2=(-10^{n_2-1})\bmod C_2,
\qquad
\delta_3=(-10^{n_3-1})\bmod C_3,
\]

与

\[
\rho_C,\sigma_C
\]

的 independent arithmetic correlation。

目标就是 A1-DBE，而不是再把 gap/RU-H 重写一遍。

优先分类：

- saturated；
- ten-free \(h_i=1\)；
- excess-\((2,5)\)-valuation；
- \(\delta_i=1\) rare phase。

## Target 2 — \(U=1\) Exact Closure

因为 \(U=1\) 永远穿过 coprimality gate，必须独立攻击：

\[
VA=Q_0B
\]

+ primitive sphere + exact gcd profile + A1 exponent relations。

尤其继续集中在：

- resonance endpoint equality；
- double resonance；
- \(d=0\) transition；
- denominator balance divisor \(V/d_0\mid B\)。

## Target 3 — Saturated / First-Actual-Layer-P Discovery

定向寻找一个真正 saturated raw terminal state；若出现：

1. exact candidate count via excess progression；
2. 对每个 \(U_j\) 检查 \(\gcd(U_j,V)\)；
3. 若全部被杀，得到第一个 Layer-P witness；
4. 若有 coprime \(U_j\)，立即 original reconstruction。

在没有真实 Layer P 之前，继续禁止 generic Jacobsthal/CRT/unit-density campaign。

---

# Final Verdict

前九轮把 A1 压到 first integer radial scale 后，第十轮最重要的发现不是“终于从 RU-H 得到了一个大 lower bound”，而恰好相反：

\[
\boxed{
\textbf{RU-H 在完整 Smith/MNZ 中没有独立 radial information。}
}
\]

同时：

\[
\boxed{
\textbf{first-candidate excess overflow 就是 RAW failure 本身。}
}
\]

因此所谓

\[
H\to R_U\to e_{\rm inactive}^{(0)}\to\text{overflow}
\]

若只使用现有 RU-H/Smith/MNZ，不可能产生新的 contradiction；它会在 algebra 上闭环回 endpoint definition。

真正剩余的、比第九轮更低维的 frontier 是：

\[
\boxed{
\textbf{Direct Endpoint Phase}
\times
\textbf{Decade Budget}
}
\]

即：

\[
\boxed{
\rho_C
+
\frac{C_3\delta_2}{C_2 10^{n_3-1}}
\stackrel{?}{\ge}10
}
\]

或对称式。

本轮 exact searches仍没有找到 \(I_1/I_{\ge2}/P\) survivor，所以 RAW extinction 尚未被事实证伪；但现在也已经清楚，若要证明它，必须找到一个**真正读取 endpoint modular phase 的新 arithmetic source**，而不是继续从 RU-H 或 ZGAP 进行等价消元。

\[
\boxed{\textbf{A1 OPEN — frontier strictly sharpened.}}
\]
