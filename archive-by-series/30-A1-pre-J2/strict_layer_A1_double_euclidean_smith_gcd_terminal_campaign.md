# Strict Layer A1：Double Euclidean Word Synchronization × Smith-GCD Terminal Campaign

**研究范围：** Strict Layer，`A1-only`  
**直接起点：** `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`  
**本轮最终状态：**

\[
\boxed{DD=\varnothing,\qquad A_1\text{ OPEN}.}
\]

本轮没有闭合 A1，但取得了三个实质推进，并得到一个重要的负结论：

1. 同一个非零整数 \(H\) 的 leading quotient/remainder 与 tail quotient/suffix 可以完全统一成 **Double Euclidean Normal Form**；
2. Smith bridge 对 \(H\) 的真正强制因子比 prompt 候选更强：
   \[
   \boxed{M_H=s\alpha\frac{\beta}{\gcd(\beta,10^{m_3})}\mid H};
   \]
3. 得到 Smith-reduced defect/master、完整 borrow propagation classification、resonance 的新 decimal-gap divisor，以及 \(d=0,1\) 的新 long-tail constraints；
4. 但已有 fixed-profile infinite synchronized family 严格证明：**exact-word + Smith-GCD 全局上仍不足以替代 common-\(U\)**。因此 A1 的正确最终 theorem 必须重新接上 common integer radial gate。

---

# 1. Frozen terminal semantics

冻结 primitive sphere：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

令

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

此前已证明：

\[
\boxed{
\text{Original admissible A1 candidate}
\iff
\text{exact synchronized primitive state + legal coprime common integer }U.
}
\]

所以 backward norm/phase/Gaussian data 只是 terminal witness 上的 derived invariants，不再是 common-\(U\) 之后的独立 semantic gate。

---

# 2. Exponent normal form

冻结：

\[
g=m_3-n_3\ge0,
\qquad
k\ge1,
\qquad
d:=m_2-g,
\]

从而

\[
\boxed{m_2=g+d},
\qquad
\boxed{n_2=2g+k+d},
\qquad
\boxed{m_3=n_3+g}.
\]

对 \(g\ge1\)，最新 branch map 为：

\[
\boxed{d\le-1\Longrightarrow\text{plus}},
\]

\[
\boxed{d\ge2\Longrightarrow\text{minus}},
\]

真正 dual-sign transition 只剩

\[
\boxed{d\in\{0,1\}}.
\]

注意：最新 report 中所谓 resonance 的 exact invariant 是

\[
\boxed{R:=b_2 10^{n_3}-b_3},
\]

不是一个另立的抽象 \(\mathscr R\)。必须严格区分 \(R=0\) 与 \(H=0\)。

---

# 3. Exact core variables

定义

\[
\boxed{D:=P_1 10^k-Q_0>0},
\]

\[
\boxed{H:=b_2Q_0-b_1 10^{m_2}D\ne0},
\]

\[
\boxed{Q_{12}:=b_1 10^{m_2}+b_2},
\]

以及

\[
\boxed{
K_3:=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbb Z_{>0}.
}
\]

exact master 给出两条核心 identity：

\[
\boxed{
b_1P_1 10^{m_2+k}=Q_0Q_{12}-H,
}
\tag{E1}
\]

\[
\boxed{
b_2P_2=10^gH+K_3.
}
\tag{E3}
\]

sign convention：

\[
\boxed{\text{plus}\iff H<0},
\qquad
\boxed{\text{minus}\iff H>0}.
\]

flat elimination 已给

\[
\boxed{H\ne0}.
\]

因此 \(H=0\) chamber 已经关闭，不能与 denominator resonance \(R=0\) 混用。

---

# 4. Unified prefix Euclidean division

令

\[
A:=b_1P_1 10^{m_2+k}.
\]

由 E1：

\[
A=Q_0Q_{12}-H.
\]

定义 canonical prefix borrow

\[
\boxed{
c_{\rm pref}:=\left\lceil\frac{H}{Q_0}\right\rceil.
}
\]

plus 中已有

\[
-Q_0<H<0,
\]

故 \(c_{\rm pref}=0\)。minus 中 \(c_{\rm pref}\) 就是此前的 canonical borrow \(c\)。

定义

\[
\boxed{r_{\rm pref}:=c_{\rm pref}Q_0-H}.
\]

则统一有

\[
\boxed{0\le r_{\rm pref}<Q_0},
\]

以及

\[
\boxed{
A=Q_0(Q_{12}-c_{\rm pref})+r_{\rm pref}.
}
\tag{PREF-U}
\]

所以：

\[
\boxed{
q_{\rm pref}=Q_{12}-c_{\rm pref},
\qquad
r_{\rm pref}=c_{\rm pref}Q_0-H.
}
\]

特殊化：

### plus

\[
\boxed{q_{\rm pref}=Q_{12},\qquad r_{\rm pref}=-H.}
\]

### minus

\[
\boxed{q_{\rm pref}=Q_{12}-c,\qquad r_{\rm pref}=cQ_0-H.}
\]

且

\[
\boxed{1\le c\le10^d}.
\]

在 \(d=0\) 时：

\[
\boxed{c=1}.
\]

这完成了 prompt 要求的统一 quotient/remainder theorem。

---

# 5. Tail Euclidean division

由 E3：

\[
b_2P_2=10^gH+K_3.
\]

令

\[
r_{10}:=b_2P_2\bmod10^g.
\]

则

\[
\boxed{K_3\bmod10^g=r_{10}}.
\]

写

\[
b_2P_2=10^gq_2+r_{10},
\]

\[
K_3=10^gq_3+r_{10}.
\]

于是

\[
\boxed{q_2-q_3=H.}
\tag{QDIFF}
\]

并且

\[
\boxed{
q_2=\left\lfloor10^d\beta_2P_2\right\rfloor,
}
\]

\[
\boxed{
q_3=\left\lfloor\beta_3(Q_0-P_3)\right\rfloor.
}
\]

因此

\[
\boxed{
H=
\left\lfloor10^d\beta_2P_2\right\rfloor
-
\left\lfloor\beta_3(Q_0-P_3)\right\rfloor.
}
\tag{HQ}
\]

这是 exact formula，不是 approximation。

---

# 6. Double Euclidean Synchronization Theorem — DES

同一个非零整数 \(H\) 同时满足：

\[
\boxed{
\begin{array}{c|c}
\text{leading Euclidean data}&\text{tail Euclidean data}\\
\hline
q_{\rm pref}=Q_{12}-c_{\rm pref}
&q_2-q_3=H\\[1mm]
r_{\rm pref}=c_{\rm pref}Q_0-H
&K_3\equiv b_2P_2\pmod{10^g}
\end{array}}
\]

其中

\[
c_{\rm pref}=\left\lceil H/Q_0\right\rceil.
\]

这就是本轮要求的 clean Double Euclidean Normal Form。

但 DES 若脱离 Smith/common-\(U\) 仍只是 exact identity system，不足以单独闭合 A1。

---

# 7. New Borrow Propagation Theorem

minus branch 中

\[
1\le c\le10^d.
\]

又因 \(b_2\) 是 \(m_2=g+d\) 位正整数，

\[
b_2\ge10^{m_2-1}=10^{g+d-1}.
\]

若 \(g\ge1\)，则

\[
10^{g+d-1}\ge10^d,
\]

故

\[
\boxed{c\le b_2.}
\]

因此：

\[
\boxed{
g\ge1,\ \text{minus}
\Longrightarrow
Q_{12}-c=b_1 10^{m_2}+(b_2-c).
}
\tag{BP1}
\]

即 borrow **永远不会从 \(b_2\) block 传播进 \(b_1\)**。

若 \(g\ge2\)，甚至 \(c<b_2\)。

若 \(g=0\)，则 \(d=m_2\)，cross-block borrow 恰在

\[
\boxed{c>b_2}
\]

时发生；此时最多传播一层：

\[
\boxed{
Q_{12}-c
=(b_1-1)10^{m_2}
+\bigl(10^{m_2}+b_2-c\bigr).
}
\tag{BP0}
\]

所以 cross-block borrow 是一个纯 \(g=0\) exceptional phenomenon。

---

# 8. Smith-GCD denominator normal form

定义

\[
s:=\gcd(b_1,b_2,b_3),
\]

\[
c_{12}:=\gcd(b_1,b_2),
\qquad
c_{23}:=\gcd(b_2,b_3),
\]

\[
\alpha:=c_{12}/s,
\qquad
\beta:=c_{23}/s.
\]

则

\[
\boxed{\gcd(\alpha,\beta)=1}.
\]

存在 \(u,t,v\in\mathbb Z_{>0}\) 使

\[
\boxed{
b_1=s\alpha u,
\quad
b_2=s\alpha\beta t,
\quad
b_3=s\beta v,
}
\]

并有 exact pairwise gcd 条件

\[
\boxed{\gcd(u,\beta t)=1},
\qquad
\boxed{\gcd(\alpha t,v)=1}.
\]

冻结最新 allocation：

\[
\boxed{\alpha\mid(Q_0-P_3)},
\tag{AALLOC}
\]

\[
\boxed{\beta\mid10^{m_2+m_3}D}.
\tag{BALLOC}
\]

因此

\[
\boxed{\beta^{\langle10\rangle}\mid D}.
\]

并冻结 ASYM-4：

\[
\boxed{
p\mid\alpha^{\langle10\rangle}\beta^{\langle10\rangle}
\Longrightarrow p\equiv1\pmod4.}
\]


---

# 9. Strongest direct Smith divisor of \(H\)

最新 Smith bridge 定义

\[
\widehat H:=\beta tQ_0-u10^{m_2}D,
\]

并给

\[
\boxed{H=s\alpha\widehat H},
\]

\[
\boxed{10^{m_3}\widehat H=\beta Z}
\tag{SNF}
\]

for some \(Z\in\mathbb Z\).

令

\[
\boxed{\delta_\beta:=\gcd(\beta,10^{m_3})},
\]

\[
\boxed{\beta^\sharp:=\frac{\beta}{\delta_\beta}}.
\]

因为

\[
\beta\mid10^{m_3}\widehat H,
\]

约掉与 \(10^{m_3}\) 可共同吸收的部分，严格得到

\[
\boxed{\beta^\sharp\mid\widehat H}.
\]

从而：

## Theorem A1-SMITH-H — Maximal direct Smith defect divisor

\[
\boxed{
M_H:=s\alpha\beta^\sharp
=s\alpha\frac{\beta}{\gcd(\beta,10^{m_3})}
\mid H.
}
\tag{MH}
\]

这比 prompt 的候选

\[
\alpha_0\beta_0\mid H
\]

更强。特别：

\[
\boxed{\alpha_0\beta_0\mid H}
\]

正确；

\[
\boxed{s\alpha\beta_0\mid H}
\]

也正确；而 \(M_H\) 还保留了 \(\beta\) 中超过 \(10^{m_3}\) 可吸收深度的 2/5-parts。

从单独 relation

\[
\beta\mid10^{m_3}\widehat H
\]

出发，\(\beta/\gcd(\beta,10^{m_3})\) 正是对 \(\widehat H\) 可无条件强迫的最大 factor-only divisor。

---

# 10. Smith-Reduced Defect Quotient

定义

\[
\boxed{
q_H:=\frac{H}{M_H}
=\frac{\widehat H}{\beta^\sharp}
\in\mathbb Z\setminus\{0\}.
}
\tag{qH}
\]

由于 \(\alpha\mid Q_0-P_3\)，定义

\[
\boxed{
A_3:=\frac{Q_0-P_3}{\alpha}\in\mathbb Z_{>0}.
}
\]

又定义

\[
\boxed{
\Lambda_\beta:=\frac{10^{m_3}}{\delta_\beta}.
}
\]

Smith relation 中

\[
E_3=
\alpha tP_2 10^{n_3}-v(Q_0-P_3)
=\alpha Z,
\]

所以

\[
\boxed{Z=tP_2 10^{n_3}-vA_3}.
\]

而

\[
10^{m_3}\beta^\sharp q_H
=\beta Z
=\delta_\beta\beta^\sharp Z.
\]

约掉 \(\beta^\sharp\)：

## Smith-Reduced Tail Equation

\[
\boxed{
\Lambda_\beta q_H
=tP_2 10^{n_3}-vA_3.
}
\tag{SR-T}
\]

这是本轮得到的最小 tail-side ordinary-integer equation。

另一方面

\[
\widehat H=\beta tQ_0-u10^{m_2}D.
\]

因为 \(\beta^\sharp\mid\widehat H\)、\(\beta^\sharp\mid\beta\)，且 \(\gcd(u,\beta)=1\)，有

\[
\boxed{\beta^\sharp\mid10^{m_2}D}.
\]

定义

\[
\boxed{
D^\sharp:=\frac{10^{m_2}D}{\beta^\sharp}\in\mathbb Z.
}
\]

则：

## Smith-Reduced Leading Equation

\[
\boxed{
q_H=\delta_\beta tQ_0-uD^\sharp.
}
\tag{SR-L}
\]

这已经把 \(s,\alpha,\beta^\sharp\) 从 defect equation 中完全抽掉。

---

# 11. Smith-Reduced Tail DES

因为

\[
\frac{b_2}{M_H}
=
\frac{s\alpha\beta t}{s\alpha\beta^\sharp}
=\delta_\beta t,
\]

而 \(M_H\mid H\)，由 E3 可知 \(M_H\mid K_3\)。定义

\[
\boxed{K_3^\sharp:=K_3/M_H}.
\]

于是

\[
\boxed{
\delta_\beta tP_2
=10^gq_H+K_3^\sharp.
}
\tag{SR-DES}
\]

并且利用 \(Q_0-P_3=\alpha A_3\)：

\[
K_3
=
\frac{s\beta v\alpha A_3}{10^{n_3}},
\]

故

\[
\boxed{
K_3^\sharp
=\frac{\delta_\beta vA_3}{10^{n_3}}
\in\mathbb Z_{>0}.
}
\tag{K3sharp}
\]

这给出一个真正的 **Smith-reduced Double Euclidean tail equation**。

---

# 12. Tail-refined forced divisor

SR-T 还允许进一步抽取一个 state-dependent divisor。

令

\[
G_T:=\gcd(tP_2,vA_3).
\]

由

\[
\Lambda_\beta q_H
=tP_2 10^{n_3}-vA_3
\]

有

\[
G_T\mid\Lambda_\beta q_H.
\]

定义

\[
\boxed{
G_T^\sharp:=\frac{G_T}{\gcd(G_T,\Lambda_\beta)}.
}
\]

则

\[
\boxed{G_T^\sharp\mid q_H}.
\]

因此：

\[
\boxed{M_HG_T^\sharp\mid H}.
\]

这是比纯 Smith divisor 更强的 coordinate-dependent refinement，但 \(G_T^\sharp\) 可以等于 1，因此不能作为 uniform height obstruction。

---

# 13. Defect quotient bounds in transition chambers

虽然 uniform constant bound 失败，但 exact sign/magnitude 仍给 transition-specific bounds。

## plus

\[
0<-H<Q_0.
\]

因此

\[
\boxed{
1\le -q_H<\frac{Q_0}{M_H}.
}
\]

特别：

\[
\boxed{\text{plus}\Longrightarrow M_H<Q_0}.
\]

若 \(M_H>Q_0/K\)，则 \(-q_H\) 只有 \(K-1\) 个可能值。

## minus, \(d=0\)

\[
0<H<Q_0,
\]

故

\[
\boxed{
1\le q_H<\frac{Q_0}{M_H}.
}
\]

同样要求 \(M_H<Q_0\)。

## minus, \(d=1\)

\[
0<H<10Q_0,
\]

故

\[
\boxed{
1\le q_H<\frac{10Q_0}{M_H}.
}
\]

因此 Smith-rich transition states 确实成为 finite-quotient states。

---

# 14. DISPROVED — uniform defect quotient bound

不能证明

\[
|q_H|\le C
\]

uniformly，因为已有 explicit infinite synchronized pseudo-family 严格杀死该 conjecture。

固定

\[
V=24,
\quad
(g_1,g_2,g_3)=(24,4,3),
\]

\[
(b_1,b_2,b_3)=(1,6,8),
\]

\[
(m_2,n_3,k,g)=(1,1,1,0).
\]

旧报告构造 polynomial family，primitive reduction 后满足：

- primitive sphere；
- exact GSYNC/master；
- exact common-\(V\) gcd profile；
- denominator digit legality；
- fixed minus sign；
- \(Q_0\to\infty\) along a subsequence。

并有

\[
\Delta_{12}=-64e_t,
\qquad
\Delta_3=80e_t,
\]

其中 \(e_t\to\infty\)。

latest defect dictionary 给

\[
H=-c_{12}\frac{\Delta_{12}}{\gcd(g_1,g_2)}.
\]

这里

\[
c_{12}=\gcd(1,6)=1,
\qquad
\gcd(24,4)=4,
\]

故

\[
\boxed{H=16e_t}.
\]

该 denominator triple 的 Smith factors 为

\[
s=1,
\quad
\alpha=1,
\quad
\beta=2,
\quad
u=1,
\quad
t=3,
\quad
v=4.
\]

又 \(m_3=1\)，所以

\[
\delta_\beta=\gcd(2,10)=2,
\quad
\beta^\sharp=1,
\quad
M_H=1.
\]

因此

\[
\boxed{q_H=H=16e_t\to\infty}.
\]

所以：

\[
\boxed{
\textbf{Defect quotient is not uniformly bounded at the exact-word + Smith level.}
}
\]

---

# 15. Smith-rich / Smith-poor split

这迫使新的正确分裂：

### Smith-rich

\[
M_H/Q_0
\]

不小。plus、\(d=0\) minus、\(d=1\) minus 都进入 finite quotient classification。

### Smith-poor

\[
M_H/Q_0
\]

很小，甚至 \(M_H=1\)。

旧 infinite family 就属于真正 Smith-poor escape。

因此任何 closure architecture 都不能假设 pairwise denominator gcd content 必然占据 height 的固定比例。

---

# 16. \(H=0\) chamber

无需继续攻击：

\[
\boxed{H=0\text{ 已由 flat elimination 排除}.}
\]

所以 exact double quotient equality 不是 A1 的 surviving resonance。

真正 resonance 只有 denominator mismatch \(R=0\)。

---

# 17. Exact denominator resonance \(R=0\)

定义

\[
\boxed{R=b_2 10^{n_3}-b_3}.
\]

latest report 证明

\[
R=0
\Longrightarrow
\boxed{b_3=b_2 10^{n_3}},
\]

\[
\boxed{d=0},
\qquad
\boxed{m_2=g},
\qquad
\boxed{\beta_2=\beta_3},
\]

\[
\boxed{g_2=10^{n_3}g_3}.
\]

Smith coordinates 中进一步有

\[
\boxed{\alpha=1,\qquad t=1,\qquad v=10^{n_3}},
\]

所以

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
\tag{R-DEN}
\]

而 defect equation 化成

\[
\boxed{
10^gH=b_2(P_2+P_3-Q_0).
}
\tag{R-H}
\]

flat elimination 给

\[
P_2+P_3\ne Q_0.
\]

并有 sign interpretation：

\[
\boxed{
\text{minus}
\iff P_2+P_3>Q_0
\iff2P_2P_3>P_1^2,
}
\]

\[
\boxed{
\text{plus}
\iff P_2+P_3<Q_0
\iff2P_2P_3<P_1^2.
}
\]

---

# 18. NEW — Resonant decimal-gap divisor

在 resonance 中定义

\[
\boxed{S_R:=P_2+P_3-Q_0\ne0}.
\]

因为 \(\alpha=t=1\)，

\[
M_H=s\beta^\sharp.
\]

将 R-H 除以 \(M_H\)：

\[
10^gq_H
=
\frac{s\beta}{s\beta^\sharp}S_R
=\delta_\beta S_R.
\]

所以

\[
\boxed{
10^gq_H=\delta_\beta S_R.
}
\tag{R-q}
\]

于是：

\[
\boxed{
L_R:=\frac{10^g}{\gcd(10^g,\delta_\beta)}
\mid S_R.
}
\tag{R-DIV}
\]

又因 resonance 中 \(m_2=g\)，而 \(b_2=s\beta\) 恰为 \(g\)-digit block，

\[
s\beta=b_2<10^g.
\]

故

\[
\delta_\beta\le\beta<10^g,
\]

所以

\[
\boxed{L_R>1}.
\]

因此 every resonant survivor 必须满足：

\[
\boxed{\gcd(S_R,10)>1}.
\]

更精确地，\(S_R\) 必须吸收 residual decimal-power factor \(L_R\)。

这是新的 resonance arithmetic，但仍未形成 contradiction。


---

# 19. Resonant sign rigidity

冻结 latest coarse classification（\(g\ge1\)）：

\[
\boxed{k\le2g-3\Longrightarrow\text{resonant plus}},
\]

\[
\boxed{k\ge2g+4\Longrightarrow\text{resonant minus}}.
\]

只有

\[
\boxed{-2\le k-2g\le3}
\]

仍是 resonant sign-sensitive strip。

本轮新的 \(L_R\mid S_R\) 尚不足以把该 strip 全部删除。

结论：

\[
\boxed{R=0\text{ remains OPEN}.}
\]

---

# 20. \(d=0\): full-block suffix chamber

\(d=0\) 等价于

\[
\boxed{m_2=g}.
\]

所以 tail modulus

\[
10^g=10^{m_2}
\]

正好覆盖整个 \(b_2\)-block length。

因此

\[
\boxed{
K_3\equiv b_2P_2\pmod{10^{m_2}}
}
\]

是 full-block product suffix。

minus 中又有

\[
\boxed{c=1},
\]

故 prefix quotient 精确为

\[
\boxed{
Q_{12}-1
=b_1 10^{m_2}+(b_2-1).
}
\]

这正是 one-borrow / full-suffix chamber。

但是不存在一个自动 identity 把

\[
b_2-1
\]

与

\[
b_2P_2\bmod10^{m_2}
\]

直接相等或相差固定量；两者的唯一 exact bridge 仍是 \(H\)。因此“borrow/no-borrow mismatch”本身还不是 contradiction theorem。

---

# 21. NEW — \(d=0\) sign-mismatch long-tail theorem

令

\[
\Theta:=Q_0-P_2.
\]

latest H-R identity：

\[
\boxed{
10^{m_3}H
=Q_0R-b_2\Theta10^{n_3}+b_3P_3.
}
\tag{HR}
\]

在 \(d=0\) 时

\[
\frac{R}{10^{m_3}}=\beta_2-\beta_3,
\]

且

\[
\boxed{
\frac{H}{Q_0}
=
\frac{R}{10^{m_3}}
-eta_2\frac{\Theta}{Q_0}
+eta_3\frac{P_3}{Q_0}.
}
\tag{D0-HR}
\]

## plus but \(R>0\)

若 \(H<0\) 且 \(R>0\)，则

\[
0<R
<10^{m_3}\beta_2\frac{\Theta}{Q_0}
<10^{m_3}\frac{\Theta}{Q_0}.
\]

对 \(g\ge1\)，冻结 axis bound：

\[
\frac{\Theta}{Q_0}<2.532\,10^{-2k}.
\]

所以

\[
\boxed{
0<R<2.532\,10^{m_3-2k}.
}
\]

因 \(R\in\mathbb Z_{>0}\)：

\[
\boxed{
d=0,\ g\ge1,\ \text{plus},\ R>0
\Longrightarrow m_3\ge2k.
}
\tag{D0+}
\]

## minus but \(R<0\)

若 \(H>0\) 且 \(R<0\)，则

\[
0<-R
<10^{m_3}\beta_3\frac{P_3}{Q_0}
<10^{m_3}\frac{P_3}{Q_0}.
\]

使用

\[
\frac{P_3}{Q_0}<100\,10^{-(2g+k)},
\]

得

\[
\boxed{
0<-R<100\,10^{m_3-(2g+k)}.
}
\]

由于 \(|R|\ge1\)：

\[
\boxed{
d=0,\ g\ge1,\ \text{minus},\ R<0
\Longrightarrow m_3\ge2g+k-1.
}
\tag{D0-}
\]

所以在 tail 不够长时，\(H\) 与 \(R\) 的 sign 必须对齐或进入 exact resonance。

这是新的 transition compression，但没有关闭 \(d=0\)。

---

# 22. \(d=0\) closure verdict

当前 exact state 已压成：

\[
\boxed{c=1},
\]

\[
\boxed{0<|H|<Q_0},
\]

\[
\boxed{M_H\mid H},
\]

full-block suffix，Smith-reduced equations，以及 \(R=0/R\ne0\) split。

但：

\[
\boxed{d=0\text{ NOT CLOSED}.}
\]

---

# 23. \(d=1\): one-extra-digit chamber

\[
\boxed{m_2=g+1}.
\]

写

\[
\boxed{b_2=\ell10^g+r_b},
\]

其中

\[
1\le\ell\le9,
\qquad
0\le r_b<10^g.
\]

Tail suffix 只读取

\[
r_bP_2\pmod{10^g},
\]

而 minus borrow 满足

\[
\boxed{1\le c\le10}.
\]

又由 Borrow Propagation Theorem，\(g\ge1\) 时这十种 carry 全部只在 \(b_2\)-block 内发生，不影响 \(b_1\)。

---

# 24. NEW — \(d=1\) plus is forced near denominator resonance

对 \(d=1\)：

\[
\frac{R}{10^{m_3}}
=10\beta_2-\beta_3.
\]

因为

\[
10\beta_2\ge1>\beta_3,
\]

所以

\[
\boxed{R>0}.
\]

若同时 plus，\(H<0\)，由 sign equation

\[
10\beta_2x<\beta_3(1-y)
\]

得到

\[
\boxed{
\beta_2<\frac1{10x}
<\frac1{10\sqrt{96/101}}
<0.10258,
}
\]

以及

\[
\boxed{
\beta_3>\frac{x}{1-y}>x>\sqrt{96/101}>0.9749.
}
\]

因此 \(d=1\) plus 强迫：

- \(b_2\) mantissa 极靠近该 decade 的 lower endpoint；
- \(b_3\) mantissa 极靠近 upper endpoint。

进一步：

\[
10\beta_2-\beta_3
=
\frac{H}{Q_0}
+10\beta_2(1-x)-\beta_3y
<10\beta_2(1-x)
<\frac{1-x}{x}.
\]

故

\[
\boxed{
0<R<10^{m_3}\frac{\Theta}{P_2}.
}
\tag{D1R}
\]

结合

\[
\Theta/Q_0<2.532\,10^{-2k},
\qquad
P_2/Q_0>\sqrt{96/101},
\]

得到

\[
\boxed{
0<R<2.598\,10^{m_3-2k}.
}
\]

于是

\[
\boxed{
g\ge1,\ d=1,\ \text{plus}\Longrightarrow m_3\ge2k.}
\tag{D1+}
\]

这是真正的新 d=1 plus compression。

---

# 25. \(d=1\) minus finite-carry status

minus 中：

\[
\boxed{c\in\{1,\dots,10\}},
\]

\[
(c-1)Q_0<H\le cQ_0,
\]

\[
M_H\mid H.
\]

Smith-rich state 可化成有限 \(q_H\)；Smith-poor state 不能。

本轮未能逐个关闭全部十个 carry slabs。

所以：

\[
\boxed{d=1\text{ NOT CLOSED}.}
\]

---

# 26. Generic \(d\) branches

对 \(g\ge1\)：

### \(d\le-1\)

只可能 plus，且

\[
0<-H<Q_0.
\]

### \(d\ge2\)

只可能 minus。此前已有 fixed-scale H theorem：

\[
0.08749\,10^dQ_0<H<10^dQ_0.
\]

所以 large positive \(d\) 的 \(H\) 不是小 remainder，而是 \(10^dQ_0\) 尺度的整数差。

但是如果 \(M_H\) 很小，\(q_H\) 仍可非常大，因此 Smith divisor alone 不给 closure。

---

# 27. Prefix floor inversion / nearest-multiple audit

plus 中

\[
\left\lfloor
\frac{b_1P_1 10^{m_2+k}}{Q_0}
\right\rfloor
=b_1 10^{m_2}+b_2.
\]

等价于

\[
\frac{b_2}{b_1 10^{m_2}}
\le
\frac{D}{Q_0}
<
\frac{b_2+1}{b_1 10^{m_2}}.
\]

这确实是 source-generated exact interval，但其 cross-multiplication 就是

\[
0<-H<Q_0.
\]

Prompt 中候选 nearest integer：

\[
D=\left\lceil\frac{b_2Q_0}{b_1 10^{m_2}}\right\rceil
\]

只有当每次 quotient jump

\[
b_1 10^{m_2}
\]

大于可允许误差尺度 \(Q_0\) 时才自动成立。现有 theorem 并未全局保证

\[
b_1 10^{m_2}>Q_0.
\]

因此：

\[
\boxed{
\text{nearest-multiple formulation is conditional, not a global theorem.}
}
\]

---

# 28. Full suffix word decomposition

令

\[
r_g:=b_2P_2\bmod10^g.
\]

则

\[
K_3=10^gq_3+r_g.
\]

所以

\[
\boxed{
b_3(Q_0-P_3)
=10^{m_3}q_3+10^{n_3}r_g.
}
\tag{WORD3}
\]

这是一条真正的 decimal word decomposition。

但 \(r_g\) 可以有 leading zeros，原始 digit legality 并不自动排除。

---

# 29. Borrow–suffix obstruction audit

本轮重点寻找了类似

\[
b_2P_2\equiv b_2-c\pmod{10^g}
\]

的直接 word-overlap equation。

结论：

\[
\boxed{
\text{E1/E3/DES 本身不推出这种直接 congruence.}
}
\]

prefix borrowed block 与 tail copied suffix 的 exact coupling 仍只通过同一个 \(H\) 实现：

\[
q_{\rm pref}=Q_{12}-c_{\rm pref},
\]

\[
q_2-q_3=H,
\]

\[
r_{\rm pref}=c_{\rm pref}Q_0-H.
\]

所以 “one-borrow/full-suffix mismatch” 是很好的 structural description，但当前还不是 theorem-level contradiction。

---

# 30. Generic \(R\ne0\) verdict

latest report 已明确给出 denominator skeleton 可达到

\[
\boxed{R=\pm1}.
\]

因此：

\[
\boxed{
R\ne0\text{ does not imply a growing arithmetic gap.}
}
\]

generic branch 必须用 H-R bridge、Smith allocation、primitive geometry 或 common-\(U\)；不能只靠 \(|R|\ge1\)。

---

# 31. Exact-word + Smith insufficiency certificate

这是本轮对整体战略最重要的裁决。

前述 fixed profile infinite synchronized family：

\[
(b_1,b_2,b_3)=(1,6,8),
\quad
g=0,
\]

满足：

- primitive sphere；
- exact GSYNC/master；
- common-\(V\) gcd profile；
- denominator digit legality；
- E1/E3；
- DES；
- Smith decomposition / allocation。

但它仍无限、\(Q_0\to\infty\)，且 \(q_H\to\infty\)。

该 family 的精确死亡点是 common-\(U\)：

\[
C_3>C_2,
\]

但 formal numerator lengths 要求

\[
n_2=2>1=n_3,
\]

任何公共正尺度 \(U\) 都保持 \(UC_3>UC_2\)，不可能同时让 \(a_2\) 为两位数而 \(a_3\) 为一位数。

所以严格得到：

\[
\boxed{
\textbf{DES + Smith-GCD arithmetic is globally insufficient for A1 closure.}
}
\]

这不是“暂时没有找到 word contradiction”，而是一个有显式无限 family 支撑的 negative theorem。

---

# 32. Common-\(U\) fallback is genuinely necessary

对 synchronized primitive state，令

\[
I_i=
\left[
\frac{10^{n_i-1}}{C_i},
\frac{10^{n_i}}{C_i}
\right).
\]

minimal A1 frontier 可只保留第二、三 blocks：

\[
I_{23}=I_2\cap I_3=[L_{23},R_{23}).
\]

exact terminal condition 是：

\[
\boxed{N_V(L_{23},R_{23})>0},
\]

或等价地

\[
\boxed{\operatorname{next}_V(L_{23})<R_{23}}.
\]

本轮证明 exact-word 不能替代该 gate。

---

# 33. Q1–Q13 answers

## Q1

Can the system be written as a clean Double Euclidean Normal Form?

\[
\boxed{\textbf{YES}.}
\]

见 DES。

## Q2

Strongest guaranteed Smith divisor of \(H\)?

\[
\boxed{
M_H=s\alpha\frac{\beta}{\gcd(\beta,10^{m_3})}\mid H.
}
\]

所以 \(\alpha_0\beta_0\mid H\) 正确但不 sharp。

## Q3

Is defect quotient bounded?

\[
\boxed{\textbf{NO uniformly before common-}U.}
\]

已有 exact synchronized infinite family 给 \(q_H\to\infty\)。

## Q4

Can \(H=0\) occur?

\[
\boxed{\textbf{NO}.}
\]

flat elimination 已关闭。

## Q5

What is resonance and is it closed?

\[
\boxed{R=b_2 10^{n_3}-b_3}.
\]

\(R=0\) 已坍缩到 rigid denominator normal form，并新增 \(L_R\mid(P_2+P_3-Q_0)\)，但

\[
\boxed{R=0\text{ remains OPEN}.}
\]

## Q6

Can \(d=0\) be closed?

\[
\boxed{\textbf{NO}.}
\]

one-borrow/full-block-suffix + Smith quotient + resonance split 均已 exact 化，但尚无 global contradiction。

## Q7

Can \(d=1\) be closed?

\[
\boxed{\textbf{NO}.}
\]

minus 只有十个 carry；plus 被压入 extreme near-resonance 且 \(m_3\ge2k\)，仍未全关。

## Q8

Which signs can occur for general \(d\)?

对 \(g\ge1\)：

\[
\boxed{d\le-1\Rightarrow\text{plus}},
\]

\[
\boxed{d=0,1\text{ dual-sign}},
\]

\[
\boxed{d\ge2\Rightarrow\text{minus}}.
\]

## Q9

Does borrow propagate into \(b_1\)?

\[
\boxed{\textbf{Only if }g=0.}
\]

\(g\ge1\) 时永不跨 block。

## Q10

Can prefix self-reference + Smith force contradiction?

Smith-rich 可以 finite-quotient；全局不行。Smith-poor infinite family 是反例。

## Q11

Can suffix become a true global block/carry obstruction?

\[
\boxed{\textbf{Not yet}.}
\]

未得到 prefix low block 与 tail suffix 的额外 automatic congruence。

## Q12

Is common-\(U\) genuinely necessary after exact-word constraints?

\[
\boxed{\textbf{YES}.}
\]

有严格的 infinite exact-word/Smith insufficiency certificate。

## Q13

Can A1 be closed?

\[
\boxed{\textbf{NO in this campaign}.}
\]

所以 Strict Layer 仍是

\[
\boxed{DD=\varnothing,\qquad A_1\text{ OPEN}.}
\]

---

# 34. PROVED / DISPROVED / OPEN ledger

## PROVED

1. Unified Double Euclidean Normal Form；
2. exact tail quotient difference \(q_2-q_3=H\)；
3. complete borrow propagation classification；
4. strongest direct Smith-only divisor
   \[
   M_H=s\alpha\beta/\gcd(\beta,10^{m_3})\mid H;
   \]
5. Smith-reduced leading equation SR-L；
6. Smith-reduced tail equation SR-T；
7. Smith-reduced tail DES；
8. state-dependent refined divisor \(G_T^\sharp\mid q_H\)；
9. \(H=0\) absent；
10. resonant decimal-gap divisor \(L_R\mid(P_2+P_3-Q_0)\) with \(L_R>1\)；
11. \(d=0\) sign-mismatch long-tail constraints；
12. \(d=1\) plus near-resonance theorem；
13. exact-word + Smith insufficiency certificate。

## DISPROVED / FAILED

1. uniform constant \(|q_H|\) bound before common-\(U\)；
2. uniform \(M_H\gg Q_0\)；
3. generic \(R\ne0\) growing lower bound；
4. pure one-borrow/full-suffix contradiction；
5. global nearest-integer theorem for \(D\) without additional modulus-height inequality；
6. ASYM-4 as standalone closure；
7. pure exact-word arithmetic as a global substitute for common-\(U\)。

## OPEN

1. \(R=0\) complete elimination；
2. \(d=0\) complete elimination；
3. \(d=1\) complete elimination；
4. generic \(d\ge2\) minus radial exclusion；
5. plus half-line radial exclusion；
6. A1 closure。

---

# 35. Exact remaining theorem

本轮最重要的战略校准是：由于已经有显式 infinite DES+Smith pseudo-family，**不能再把一个纯 word-only theorem 作为全局唯一 frontier**。

正确的最小全局 closure statement 应该是：

## A1 Smith-Reduced Common-U Exclusion Theorem — A1-SRCU

对任意满足：

1. primitive sphere；
2. exact common-\(V\) gcd profile + denominator digit legality；
3. exact master / E1 / E3 / DES；
4. Smith decomposition 与 asymmetric allocation；
5. 当前全部 sign/exponent constraints；

的 synchronized primitive A1 state，定义

\[
C_i=P_i/g_i
\]

以及

\[
I_{23}
=
\left[
\frac{10^{n_2-1}}{C_2},
\frac{10^{n_2}}{C_2}
\right)
\cap
\left[
\frac{10^{n_3-1}}{C_3},
\frac{10^{n_3}}{C_3}
\right)
=[L_{23},R_{23}).
\]

证明：

\[
\boxed{
\operatorname{next}_V(L_{23})\ge R_{23}.
}
\tag{A1-SRCU}
\]

等价地：

\[
\boxed{N_V(L_{23},R_{23})=0.}
\]

若该 theorem 成立，则所有 synchronized primitive states 都无法获得 legal coprime common integer \(U\)，从而

\[
\boxed{A_1=\varnothing}.
\]

结合已闭合的 DD，届时才可得

\[
\boxed{\text{Strict Layer CLOSED}.}
\]

---

# 36. Dependency audit

### DES

只依赖 E1/E3、plus bound \(-Q_0<H<0\)、minus canonical borrow。

### Borrow propagation

只依赖

\[
c\le10^d,
\quad
m_2=g+d,
\quad
b_2\ge10^{m_2-1}.
\]

### Strong Smith divisor

只依赖

\[
H=s\alpha\widehat H,
\quad
10^{m_3}\widehat H=\beta Z.
\]

### Smith-reduced equations

依赖 strong Smith divisor、\(\alpha\mid Q_0-P_3\)、pairwise gcd conditions。

### Resonant decimal-gap divisor

依赖 resonance normal form、R-H 与 strong Smith divisor。

### Exact-word insufficiency

依赖 generic primitive-defect campaign 的 explicit polynomial synchronized family 及 common-\(U\) campaign 对其死亡点的证明。

本轮新增 theorem 不调用 DD-only closure machinery，也没有重新依赖已撤回的旧 External Exact-Lift closure claim。

---

# 37. At most three next-round targets

## Target 1 — \(d=0,1\) exact-word × common-\(U\) splice

不要继续把 transition slices 当纯 word problem。将：

- \(d=0\)：one-borrow/full-block suffix + \(M_H\mid H\)；
- \(d=1\)：ten carries + near-resonance plus theorem；

直接代入 \(I_{23}\) / \(\operatorname{next}_V\) gate，尝试得到 radial contradiction。

## Target 2 — resonance \(R=0\) × common-\(U\)

冻结

\[
\alpha=t=1,
\quad
m_2=g,
\quad
b_3=b_2 10^{n_3},
\]

和新的

\[
L_R\mid(P_2+P_3-Q_0).
\]

在这个小 normal form 上专攻 integer radial interval，而不是继续 generic Hensel / Gaussian。

## Target 3 — Smith-rich / Smith-poor radial dichotomy

- Rich：finite \(q_H\) 全分类；
- Poor：把小 pairwise denominator overlap 直接翻译成 common-\(U\) successor obstruction。

不要重新回到 generic private-prime program。

---

# 38. Final assessment

本轮没有得到

\[
\boxed{A_1=\varnothing}.
\]

但 exact ordinary-integer frontier 已经被进一步降维到：

\[
\boxed{
\text{Double Euclidean Synchronization}
\times
\text{Smith-reduced defect quotient}
\times
\text{integer common-}U\text{ radial gate}.
}
\]

最关键的新负结论是：

\[
\boxed{
\textbf{pure exact-word + Smith closure is globally false as a proof architecture.}
}
\]

所以正确的下一阶段不是继续无限叠加 word lemma，而是把这轮获得的强离散 normal form **外科式接回 common-\(U\)**。

当前最终状态：

\[
\boxed{
DD=\varnothing,
\qquad
A_1\text{ OPEN}.
}
\]
