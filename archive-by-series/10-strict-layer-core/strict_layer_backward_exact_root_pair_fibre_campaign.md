# 三项十进制拼接平方和问题：Backward Strict Layer — Exact Admissible Root-Pair Fibre Compression

**文件名：** `strict_layer_backward_exact_root_pair_fibre_campaign.md`  
**研究范围：** fixed denominator–decimal trace \(T=T_{\rm den,10}\) 与 residual root pair \((\theta,\zeta)\) 之后的 exact realization fibre  
**冻结：** 不推进 moving-core termination、height、square-spacing、DD small factor、valuation-capacity asymptotics；只研究 recovery map 的 fibre / injectivity / compatibility  
**本轮最终等级：** **Outcome B + chamber-specific Outcome D + stronger recovery collapse**

---

# 1. Executive summary

本轮真正把上一轮留下的

\[
T+(\theta,\zeta)+\text{local realization data}
\]

继续压缩了一层。

最重要的结论不是又得到一个新的 quadratic，而是：

\[
\boxed{
\text{fixed }(T,\theta,\zeta)
\text{ 后，全部完整候选自由度只剩一个十进制切分位置 }n_2.
}
\]

更精确地，固定

\[
T\simeq(b_1,b_2,b_3,S)
\]

以及

\[
\theta=\frac\mu\nu>0,
\qquad
\zeta=z_3,
\]

上一轮已经严格恢复

\[
D=D_T,
\]

\[
N:=\mathcal N_{12}
=
\theta^2+\frac{2G}{\tau}\theta\zeta,
\]

\[
C
=
\frac{G\kappa\zeta+(G+\kappa)\tau\theta}{G^2\mathcal L},
\]

以及

\[
\mathcal C_3
=
\kappa^2\zeta^2
-2(G+\kappa)\tau\theta\zeta.
\]

本轮首先完成 prompt 要求的 quadratic 审计：

\[
\boxed{
Q_{\rm gap}(T,\theta,\zeta,C_T,N_T)\equiv0
}
\]

在 fixed-\(T\) identity

\[
\kappa\tau=G\mathcal L D
\]

下成立；而

\[
\boxed{
Q_{\rm tail}(T,\theta,\zeta,C_T,C_{3,T})\equiv0
}
\]

更是直接恒等消失。

所以本轮正式升级：

\[
\boxed{
Q_{\rm gap},Q_{\rm tail}
\text{ 都是 exact coefficient reconstruction 的 elimination shadows，}
}
\]

不再是 residual synchronization gates。

随后出现了比预设的“circle \(\cap\) line”更强的结构。

定义完整 denominator word

\[
\mathbf B
:=
 b_1M_2M_3+b_2M_3+b_3
=M_3Q+b_3.
\]

fixed \(T\) 后 \(\mathbf B\) 已冻结，并且

\[
\mathbf B
=SD+b_3
=\eta_3(\mathcal LD+\tau).
\]

另一方面，actual root 必须满足

\[
a_3=\eta_3\zeta\in\mathbf Z_{>0}.
\]

定义

\[
\boxed{
\mathbf A
:=
SC+a_3.
}
\]

上一轮 ADRI 已经从两支 Exact-Lift coefficient definitions 严格证明，而本轮重新回查并提升其作用：在 DD 与 \(A_1\)-only 两个 strict chamber 中，\(\mathbf A\) 恰好就是**完整 numerator concatenation word**：

\[
\boxed{
\mathbf A
=\operatorname{concat}(a_1,a_2,a_3).
}
\]

而且 exact coefficient plane 立即变成

\[
\boxed{
\mathcal R
=\frac{\mathbf A}{\mathbf B}
=\frac\theta G+\frac\zeta\tau.
}
\]

因此 root pair 不只是决定若干 coefficients；它决定了整个 numerator word。

更进一步，定义

\[
\boxed{
\mathscr I_T(\theta,\zeta)
:=(\mathbf A,N).
}
\]

则在 positive exact-admissible locus 上有一个 lossless semantic reparametrization：

\[
\boxed{
(T,\theta,\zeta)
\simeq
(T,\mathbf A,N).
}
\]

逆向恢复极其短：

\[
\mathcal R=\frac{\mathbf A}{\mathbf B},
\]

\[
r_3
=
\sqrt{
\mathcal R^2-\frac N{G^2}
}>0,
\]

\[
\zeta=\tau r_3,
\qquad
\theta=G(\mathcal R-r_3).
\]

所以从 recovery semantics 看，root pair 最自然的含义其实是：

\[
\boxed{
\text{full numerator word }\mathbf A
+
\text{first-two weighted norm }N.
}
\]

现在固定 \((T,\theta,\zeta)\)。于是 \(\mathbf A,N,a_3,n_3\) 都固定。令

\[
P:=A_{12}
=\frac{\mathbf A-a_3}{10^{n_3}}.
\]

完整候选中唯一还没决定的是：这个固定十进制整数 \(P\) 在哪里切成

\[
P=a_1 10^{n_2}+a_2.
\]

对一个候选切分位置 \(n\)，定义

\[
q_n:=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
r_n:=P\bmod10^n.
\]

于是该 cut 唯一给出

\[
a_1=q_n,
\qquad
a_2=r_n,
\]

并且它成为完整 candidate 的充要条件，除 digit / reducedness / strict-cell 条件外，只剩

\[
\boxed{
F_n
:=
b_2^2q_n^2+b_1^2r_n^2
=N.
}
\]

因此：

\[
\boxed{
\mathfrak F_T(\theta,\zeta)
\text{ 与满足 }F_n=N\text{ 的 legal decimal cuts }n
\text{ 一一对应。}
}
\]

本轮的主新定理是一个 **Decimal Split Strict Convexity Lemma**。

若

\[
n_1<n_2<n_3
\]

是三个 legal cuts，则

\[
q_{n_1}^2-q_{n_2}^2
>
q_{n_2}^2-q_{n_3}^2,
\]

而

\[
r_{n_2}^2-r_{n_1}^2
<
r_{n_3}^2-r_{n_2}^2.
\]

所以沿 legal cuts，\(F_n\) 的离散一阶差分严格递增。换言之：

\[
\boxed{
F_n\text{ 在 decimal cut set 上严格离散凸。}
}
\]

从而任意水平线 \(F_n=N\) 至多击中两次：

\[
\boxed{
\left|\mathfrak F_T(\theta,\zeta)\right|
\le2.
}
\]

这是一个**绝对常数 bound**，不依赖

\[
r_2(N),\quad d(N),\quad\text{Gaussian divisor count},\quad N\text{ 的大小}.
\]

所以本轮达成 Outcome B。

如果 fibre size = 2，则 multiplicity 的来源也已经完全识别：

\[
\boxed{
\text{不是 quadratic conjugate branch，}
\text{不是 Gaussian conjugation，}
\text{不是 denominator normalization，}
}
\]

而是

\[
\boxed{
\textbf{同一个 first-two numerator word }P
\textbf{ 有两个不同内部 decimal cuts，}
\textbf{且恰好给出同一个 weighted norm }N.
}
\]

因此在 fixed root pair 后，所有 genuine residual freedom 最多是一位二元 cut label：

\[
\boxed{
\omega_{12}\in\{0,1\}.
}
\]

给定 \((T,\theta,\zeta,\omega_{12})\)，若 fibre 非空，则 complete candidate 唯一恢复。

最后，root-pair minimality 也出现一个 chamber-specific 加强：

- 在 \(A_1\)-only 中，\(T\) 已经固定 \(S=10^{n_3}\)，因此 \(n_3\) 固定；完整 word \(\mathbf A\) 自己就恢复 \(a_3\)、\(N\)、\(\theta,\zeta\)。故
  \[
  \boxed{
  (T,\theta,\zeta)
  \simeq
  (T,\mathbf A)
  \qquad(A_1\text{-only}).
  }
  \]
  这是一个真正的一坐标 semantic collapse。

- 在 DD 中，\(T\) 只固定 \(S=M_3\)，不固定 \(n_3>m_3\)。\(\mathbf A\) 单独不能恢复 third cut。本轮给出显式 algebraically admissible collision，证明 **\(\mathbf A\) alone is insufficient in DD**。因此 uniform strict interface 目前最自然仍是两份 semantic information \((\mathbf A,N)\)，或等价 root pair。

这不构成 categorical minimal encoding dimension theorem；但它把 two-root narrative 的真正语义已经解释清楚。

---

# 2. Source audit and proof boundary

本轮重新核对了：

- `strict_layer_backward_algebraic_denominator_interface.md`；
- `strict_layer_backward_denominator_decimal_interface.md`；
- `strict_layer_backward_canonical_synchronization_quotient.md`；
- `strict_layer_backward_canonical_dependency_skeleton.md`；
- `strict_layer_backward_global_witness_gluing_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`；
- `strict_layer_final_campaign.md`；
- `strict_layer_unified_exact_lift_campaign(1).md` 中 DD / \(A_1\) 的实际 coefficient definitions。

与上一轮 ADRI 报告不同，本轮通过 exact-title 检索重新暴露了 `strict_layer_final_campaign.md` 正文，因此该 source-visibility limitation 本轮已经解除。

不过本轮新增 theorem 的关键代数链并不依赖旧 `strict_layer_final_campaign.md` 的 N4/N5 或其 forward strict branch geometry；真正使用的是已经直接回查的 Exact-Lift 定义：

\[
Q=b_1M_2+b_2,
\qquad
G=b_1b_2,
\]

\[
\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2,
\]

以及 strict scope 的两支 coefficient form：

### DD

\[
C
=10^{m_2+k_{12}}a_1+10^{d_3}a_2
=10^{d_3}A_{12},
\]

\[
D=Q,
\qquad
S=M_3.
\]

### \(A_1\)-only

\[
C
=10^{g+k_{12}+m_2}a_1+a_2
=A_{12},
\]

\[
D=10^gQ,
\qquad
S=10^{n_3}.
\]

这里

\[
A_{12}:=a_1 10^{n_2}+a_2,
\]

\[
d_3=n_3-m_3>0
\quad(DD),
\]

\[
g=m_3-n_3\ge0
\quad(A_1).
\]

所有新 fibre theorem 都从这些 exact definitions 与上一轮已经证明的 root reconstruction 直接推出，不依赖 synthesis 中未回查的强陈述。

本轮没有使用：

- moving primitive core；
- fixed-core finite fibre；
- SGR depth quadratic；
- square-spacing；
- near-square asymptotics；
- DD post-deflation \(J\)；
- \(2/5\)-adic capacity growth；
- height bound。

所以 anti-duplication boundary 保持完整。

---

# 3. Frozen results from ADRI

固定

\[
T=T_{\rm den,10}
\simeq
(b_1,b_2,b_3,S).
\]

令

\[
M_i=10^{m_i},
\qquad
Q=b_1M_2+b_2,
\qquad
G=b_1b_2.
\]

fixed \(T\) 后冻结

\[
b_i,m_i,M_i,Q,G,
\Lambda,
\eta_3,\mathcal L,\tau,\kappa,D,
\]

其中

\[
\eta_3=\gcd(S,b_3),
\qquad
\mathcal L=\frac S{\eta_3},
\qquad
\tau=\frac{b_3}{\eta_3},
\]

\[
\kappa=\frac{M_3QG}{b_3},
\]

\[
\boxed{
D=\frac{M_3}{S}Q,
}
\]

并且

\[
\boxed{
\kappa\tau=G\mathcal LD.
}
\tag{3.1}
\]

令

\[
\theta:=\frac\mu\nu>0,
\qquad
\gcd(\mu,\nu)=1,
\qquad
\zeta:=z_3.
\]

上一轮已经证明 exact oriented plane

\[
\boxed{
G^2\mathcal LC
-G\kappa\zeta
-(G+\kappa)\tau\theta
=0.
}
\tag{3.2}
\]

因此

\[
\boxed{
C=C_T(\theta,\zeta)
=
\frac{
G\kappa\zeta+(G+\kappa)\tau\theta
}{G^2\mathcal L}.
}
\tag{3.3}
\]

sphere/root reconstruction 给出

\[
\boxed{
N=N_T(\theta,\zeta)
=
\theta^2+\frac{2G}{\tau}\theta\zeta.
}
\tag{3.4}
\]

而 primitive-tail coefficient 已压成

\[
\boxed{
\mathcal C_3
=C_{3,T}(\theta,\zeta)
=
\kappa^2\zeta^2
-2(G+\kappa)\tau\theta\zeta.
}
\tag{3.5}
\]

因此

\[
(C,D,N,\mathcal C_3)
\]

不再是 independent residual coordinates。

本轮从此只把它们当 deterministic projections。

---

# 4. Quadratic gates are fully internalized

## 4.1 Gap quadratic

旧 gap quadratic 为

\[
Q_{\rm gap}
=
D(\kappa+2G)\theta^2
-2G\kappa C\theta
+\kappa DN.
\]

把 (3.3)、(3.4) 直接代入并因式分解，得到

\[
\boxed{
Q_{\rm gap}
=
-\frac{2\theta}{G\mathcal L\tau}
\bigl(\kappa\tau-G\mathcal LD\bigr)
\bigl(
G\kappa\zeta+(G+\kappa)\tau\theta
\bigr).
}
\tag{4.1}
\]

而 fixed \(T\) 已有 (3.1)：

\[
\kappa\tau=G\mathcal LD.
\]

所以

\[
\boxed{
Q_{\rm gap}
\bigl(T,\theta,\zeta,C_T,N_T\bigr)
\equiv0.
}
\tag{4.2}
\]

**状态：NEW PROVED / REINTERPRETED EXISTING ELIMINATION.**

这里必须注意适用范围：

- 使用了 fixed-\(T\) tail–coefficient identity (3.1)；
- 使用了 exact oriented coefficient plane (3.2)；
- 使用了 exact sphere/root reconstruction (3.4)。

所以它不是“任意 algebraic coefficients 下 gap polynomial 恒零”，而是：

\[
\boxed{
\text{一旦使用 Exact-Lift 本身的 coefficient reconstruction，}
Q_{\rm gap}\text{ 就不再提供新的 residual condition。}
}
\]

## 4.2 Primitive-tail quadratic

旧 tail quadratic 为

\[
Q_{\rm tail}
=
-\kappa(\kappa+2G)\zeta^2
+2G^2\mathcal LC\zeta
+\mathcal C_3.
\]

直接代入 (3.3)、(3.5)，全部项严格消去：

\[
\boxed{
Q_{\rm tail}
\bigl(T,\theta,\zeta,C_T,C_{3,T}\bigr)
\equiv0.
}
\tag{4.3}
\]

这里甚至不需要再调用 (3.1)。

**状态：NEW PROVED / REINTERPRETED EXISTING ELIMINATION.**

## 4.3 Verdict

因此上一轮的 proportionality theorem 现在可以进一步解释为：

\[
\boxed{
Q_{\rm gap},Q_{\rm tail}
\text{ 都不是 fixed root-pair fibre 中剩余的 gate；}
}
\]

它们是从 exact coefficient plane / sphere / tail definitions 消元以后留下的影子。

上一轮 simultaneous quadratics 的 conjugate false-gluing branch 仍有意义，但只用于说明：

\[
\boxed{
\text{若丢掉 exact orientation，quadratic shadows 会产生假阳性。}
}
\]

本轮不再攻击这两个 quadratic。

---

# 5. Exact definition of the fixed-\((T,\theta,\zeta)\) fibre

定义

\[
\boxed{
\mathfrak F_T(\theta,\zeta)
}
\]

为所有完整六块正既约整数候选

\[
(a_1,b_1,a_2,b_2,a_3,b_3)
\]

满足：

1. denominator–decimal trace 等于固定 \(T\)；
2. 处于当前 strict scope（DD 或 \(A_1\)-only）；
3. 实际 Exact-Lift gap root 等于 \(\theta\)；
4. 实际 primitive-tail root 等于 \(\zeta\)；
5. 原题 exact concatenation equality 成立。

若 \((\theta,\zeta)\) 连 ADRI 的 integrality / positivity / denominator compatibility 都不通过，则定义

\[
\mathfrak F_T(\theta,\zeta)=\varnothing.
\]

本轮研究的是非空可能性下 fibre 的真实 cardinality，而不是 projected quadratic roots 的数量。

---

# 6. New semantic trace: root pair \(\leftrightarrow(\mathbf A,N)\)

这是本轮第一项超出原 prompt 预设的压缩。

## 6.1 Denominator word

定义固定 denominator word

\[
\boxed{
\mathbf B
:=
 b_1M_2M_3+b_2M_3+b_3
=M_3Q+b_3.
}
\tag{6.1}
\]

由

\[
D=\frac{M_3}{S}Q
\]

有

\[
\boxed{
\mathbf B=SD+b_3.
}
\tag{6.2}
\]

再用

\[
S=\eta_3\mathcal L,
\qquad
b_3=\eta_3\tau,
\]

得到

\[
\boxed{
\mathbf B
=\eta_3(\mathcal LD+\tau).
}
\tag{6.3}
\]

## 6.2 Numerator word reconstructed from the root pair

actual tail root 满足

\[
\boxed{
a_3=\eta_3\zeta.
}
\tag{6.4}
\]

定义

\[
\boxed{
\mathbf A
:=SC+a_3
=\eta_3(\mathcal LC+\zeta).
}
\tag{6.5}
\]

上一轮 exact plane 写成

\[
\mathcal R
=
\frac{\mathcal LC+\zeta}{\mathcal LD+\tau}.
\]

结合 (6.3)–(6.5)：

\[
\boxed{
\mathcal R=\frac{\mathbf A}{\mathbf B}.
}
\tag{6.6}
\]

还可以把 \(\mathbf A\) 直接写成 root pair 的线性函数。由 (3.3)：

\[
\boxed{
\mathbf A
=
\frac{\eta_3(G+\kappa)}{G^2}
\bigl(G\zeta+\tau\theta\bigr).
}
\tag{6.7}
\]

同时

\[
\boxed{
\mathbf B
=
\frac{b_3(G+\kappa)}G.
}
\tag{6.8}
\]

因此 fixed \(T\) 后，组合

\[
\rho:=\tau\theta+G\zeta
\]

正是完整 numerator word 的一个常数倍。

但第 12 节会说明：在 DD 中，\(\rho\) 或 \(\mathbf A\) 单独仍不足以确定 third cut。

## 6.3 Why \(\mathbf A\) is the actual decimal numerator word

### DD

DD 中

\[
S=M_3=10^{m_3},
\]

\[
C=10^{d_3}A_{12},
\qquad
d_3=n_3-m_3.
\]

所以

\[
SC
=10^{m_3+d_3}A_{12}
=10^{n_3}A_{12}.
\]

故

\[
\boxed{
\mathbf A
=A_{12}10^{n_3}+a_3.
}
\]

### \(A_1\)-only

\(A_1\) 中

\[
S=10^{n_3},
\qquad
C=A_{12}.
\]

所以同样

\[
\boxed{
\mathbf A
=A_{12}10^{n_3}+a_3.
}
\]

于是统一得到：

\[
\boxed{
\mathbf A
=\operatorname{concat}(a_1,a_2,a_3).
}
\tag{6.9}
\]

**状态：PROVED / inherited from ADRI exact concatenation normal form；本轮 REINTERPRETED 为 root-pair 对完整 numerator word 的 deterministic reconstruction。**

## 6.4 Root pair is equivalent to \((\mathbf A,N)\)

正向：

\[
(\theta,\zeta)
\Longrightarrow
\mathbf A
\]

由 (6.5)/(6.7)，而

\[
(\theta,\zeta)
\Longrightarrow
N
\]

由 (3.4)。

反向：固定 \(T\)，因此 \(\mathbf B,G\) 固定。这里把 \((\mathbf A,N)\) 的 admissible image 明确定义为满足：

- \(\mathbf A,N\in\mathbf Z_{>0}\)；
- \(\mathcal R:=\mathbf A/\mathbf B>0\)；
- \(\mathcal R^2-N/G^2\) 是正有理平方；
- 由其正平方根恢复的 \(a_3=b_3r_3\) 为正整数、与 \(b_3\) 既约，并满足 fixed-\(T\) tail profile。

在这个 semantic image 上，令

\[
\mathcal R:=\frac{\mathbf A}{\mathbf B}.
\]

则

\[
\frac N{G^2}=r_1^2+r_2^2,
\]

所以

\[
\boxed{
r_3
=
\sqrt{
\mathcal R^2-\frac N{G^2}
}>0
}
\tag{6.10}
\]

取正根唯一。

再令

\[
\boxed{
\zeta=\tau r_3,
\qquad
\theta=G(\mathcal R-r_3).
}
\tag{6.11}
\]

于是 root pair 唯一恢复。

因此在 exact-positive semantic locus：

\[
\boxed{
(T,\theta,\zeta)
\simeq
(T,\mathbf A,N).
}
\tag{6.12}
\]

**状态：NEW PROVED — lossless semantic reparametrization。**

注意这不是 tuple-length trick。\(\mathbf A\) 是原题真实 numerator word，\(N\) 是真实 first-two weighted norm；它们正是后面 local fibre 实际读取的两份信息。

---

# 7. Primitive recovery equations for \((a_1,a_2)\)

固定 \((T,\theta,\zeta)\)，于是：

\[
\mathbf A,
\quad N,
\quad a_3=\eta_3\zeta
\]

全部固定。

令

\[
\boxed{
n_3:=\operatorname{digits}(a_3).
}
\tag{7.1}
\]

actual admissibility 要求 third-tail trace 与 \(n_3\) 相容：

### DD

\[
S=M_3,
\qquad
n_3>m_3.
\]

### \(A_1\)-only

\[
S=10^{n_3},
\qquad
n_3\le m_3.
\]

因此 \((T,\zeta)\) 同时决定 chamber label；branch 不再是独立 choice。

定义

\[
\boxed{
P:=A_{12}
=\frac{\mathbf A-a_3}{10^{n_3}}.
}
\tag{7.2}
\]

在 exact-admissible locus 中该量必须为正整数。

也可写成

\[
\boxed{
P
=\frac{SC}{10^{n_3}}.
}
\tag{7.3}
\]

现在 first-two block recovery 完全变成：

> 对固定十进制整数 \(P\)，选择一个 cut position \(n=n_2\)，令
> \[
> a_1=\left\lfloor P/10^n\right\rfloor,
> \qquad
> a_2=P\bmod10^n.
> \]

没有其他连续参数。

定义

\[
q_n:=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
r_n:=P\bmod10^n.
\tag{7.4}
\]

一个 **legal decimal cut** 必须满足：

1. \(1\le n<\operatorname{digits}(P)\)；
2. \(q_n>0\)；
3. \(10^{n-1}\le r_n<10^n\)，即第二块恰有 \(n\) 位、无前导零；
4. reducedness：
   \[
   \gcd(q_n,b_1)=1,
   \qquad
   \gcd(r_n,b_2)=1;
   \]
5. strict cell：
   \[
   s_2+s_3>0,
   \]
   即
   \[
   \boxed{
   n+n_3>m_2+m_3.
   }
   \tag{7.5}
   \]

此外 third block 已单独要求

\[
\gcd(a_3,b_3)=1.
\]

对这样的 cut，唯一尚需检查的是 first-two norm：

\[
\boxed{
(b_2q_n)^2+(b_1r_n)^2=N.
}
\tag{7.6}
\]

这已经是完整 local fibre equation。

---

# 8. Exact Word-Cut Fibre Bijection

## Theorem RPF-1 — Exact word-cut fibre bijection

**NEW PROVED.**

固定一个通过 ADRI basic admissibility 的 \((T,\theta,\zeta)\)。令 \(P,N,n_3\) 如上。

定义

\[
\mathcal K_T(\theta,\zeta)
\]

为所有满足第 7 节 legal-cut 条件以及

\[
F_n:=b_2^2q_n^2+b_1^2r_n^2=N
\tag{8.1}
\]

的 cut positions \(n\)。

则有自然双射

\[
\boxed{
\mathfrak F_T(\theta,\zeta)
\longleftrightarrow
\mathcal K_T(\theta,\zeta).
}
\tag{8.2}
\]

### 证明：candidate \(\to\) cut

完整 candidate 已有真实 \(n_2\)。由于

\[
P=a_1 10^{n_2}+a_2,
\]

所以

\[
a_1=q_{n_2},
\qquad
a_2=r_{n_2}.
\]

真实十进制表示、逐项既约和 strict chamber 自动给出 legal-cut 条件；而 Exact-Lift 定义

\[
N=(a_1b_2)^2+(a_2b_1)^2
\]

给出 (8.1)。

### 证明：cut \(\to\) complete candidate

反过来，取 \(n\in\mathcal K_T\)，定义

\[
a_1=q_n,
\qquad
a_2=r_n.
\]

legal conditions 保证 blocks 正、位数正确、逐项既约，并处于正确 strict chamber。

由 (8.1)：

\[
\frac N{G^2}
=
\frac{a_1^2}{b_1^2}
+
\frac{a_2^2}{b_2^2}.
\]

另一方面

\[
r_3=\frac{a_3}{b_3}=\frac\zeta\tau,
\]

而 (3.4) 给出

\[
\frac N{G^2}
=
\left(\frac\theta G\right)^2
+2\frac\theta G\frac\zeta\tau.
\]

因此

\[
\frac N{G^2}+r_3^2
=
\left(
\frac\theta G+\frac\zeta\tau
\right)^2.
\]

由 (6.6)

\[
\frac{\mathbf A}{\mathbf B}
=
\frac\theta G+\frac\zeta\tau>0.
\]

故

\[
\boxed{
\left(\frac{\mathbf A}{\mathbf B}\right)^2
=
\frac{a_1^2}{b_1^2}
+
\frac{a_2^2}{b_2^2}
+
\frac{a_3^2}{b_3^2}.
}
\]

同时 \(\mathbf A\) 与 \(\mathbf B\) 已经分别是三块真实十进制拼接。

所以原题 exact candidate 条件全部成立。

证毕。

### Consequence

这一步非常重要：

\[
\boxed{
\text{fixed root pair 后，不再有隐藏 sphere witness、root sign、}
C,D,N,C_3\text{ 或 denominator normalization freedom。}
}
\]

唯一可能的 complete-realization multiplicity 就是 decimal cut multiplicity。

---

# 9. \((X,Y)\) reformulation: not one line, but a decimal line pencil

令

\[
\boxed{
X:=a_1b_2,
\qquad
Y:=a_2b_1.
}
\tag{9.1}
\]

则

\[
\boxed{
X^2+Y^2=N.
}
\tag{9.2}
\]

对一个固定 cut \(n=n_2\)，prefix equation

\[
P=a_1 10^n+a_2
\]

乘 \(G=b_1b_2\) 后得到

\[
\boxed{
 b_1 10^n X+b_2Y=GP.
}
\tag{9.3}
\]

所以每个 cut 确实给出

\[
\boxed{
\text{circle}\cap\text{line}.
}
\]

但原 prompt 中最诱人的猜测——“fixed root pair 后只有一条固定 line”——是错误的。

真正结构是：

\[
\boxed{
X^2+Y^2=N
}
\]

与一族离散 line

\[
\boxed{
\ell_n:
 b_1 10^n X+b_2Y=GP,
\qquad n\in\mathcal K_{\rm digit}.
}
\]

的交。

即：

\[
\boxed{
\textbf{circle }\cap\textbf{ decimal line pencil}.
}
\]

对每个固定 \(n\)，decimal concatenation 本身已经唯一指定

\[
X=b_2q_n,
\qquad
Y=b_1r_n,
\]

所以单条 line 的二次交点数并不是 fibre complexity 的真正来源。

真正问题是：不同 lines \(\ell_n\) 能否在 circle 上各命中一个合法 decimal point。

下一节证明最多两条能命中。

---

# 10. Decimal Split Strict Convexity

这是本轮主新定理。

对每个 legal cut \(n\)，定义

\[
\boxed{
F_n:=b_2^2q_n^2+b_1^2r_n^2.
}
\tag{10.1}
\]

## Lemma RPF-2 — prefix-square loss strictly decreases

取任意三个 legal cuts

\[
n_1<n_2<n_3.
\]

因为十进制 prefix 每向右移动至少一位，

\[
q_{n_1}\ge10q_{n_2},
\qquad
q_{n_2}>q_{n_3}\ge1.
\]

所以

\[
q_{n_1}^2-q_{n_2}^2
\ge99q_{n_2}^2,
\]

而

\[
q_{n_2}^2-q_{n_3}^2
<q_{n_2}^2.
\]

因此

\[
\boxed{
q_{n_1}^2-q_{n_2}^2
>
q_{n_2}^2-q_{n_3}^2.
}
\tag{10.2}
\]

## Lemma RPF-3 — suffix-square gain strictly increases

因为 \(n_2\) 是 legal cut，

\[
r_{n_2}<10^{n_2}.
\]

于是

\[
r_{n_2}^2-r_{n_1}^2
<r_{n_2}^2
<10^{2n_2}.
\tag{10.3}
\]

另一方面 \(n_3\) 是 legal cut，因此当把 suffix 从 \(n_2\) 扩到 \(n_3\) 位时，新加入的 leading decimal block 非零。故

\[
r_{n_3}\ge10^{n_2}+r_{n_2}.
\]

于是

\[
r_{n_3}^2-r_{n_2}^2
\ge
(10^{n_2}+r_{n_2})^2-r_{n_2}^2
>10^{2n_2}.
\tag{10.4}
\]

结合 (10.3)：

\[
\boxed{
r_{n_2}^2-r_{n_1}^2
<
r_{n_3}^2-r_{n_2}^2.
}
\tag{10.5}
\]

## Theorem RPF-4 — strict discrete convexity

沿按大小排列的 legal cuts，\(F_n\) 的一阶差分严格递增。

事实上：

\[
F_{n_2}-F_{n_1}
=
-b_2^2
(q_{n_1}^2-q_{n_2}^2)
+b_1^2
(r_{n_2}^2-r_{n_1}^2),
\]

\[
F_{n_3}-F_{n_2}
=
-b_2^2
(q_{n_2}^2-q_{n_3}^2)
+b_1^2
(r_{n_3}^2-r_{n_2}^2).
\]

由 (10.2)、(10.5)，

\[
\boxed{
F_{n_3}-F_{n_2}
>
F_{n_2}-F_{n_1}.
}
\tag{10.6}
\]

所以 \(F\) 在 legal decimal cut set 上严格离散凸。

**状态：NEW PROVED。**

## Corollary RPF-5 — no triple collision

若存在三个 cuts

\[
n_1<n_2<n_3
\]

满足

\[
F_{n_1}=F_{n_2}=F_{n_3}=N,
\]

则由前两个等式

\[
b_2^2(q_{n_1}^2-q_{n_2}^2)
=
b_1^2(r_{n_2}^2-r_{n_1}^2),
\]

由后两个等式

\[
b_2^2(q_{n_2}^2-q_{n_3}^2)
=
b_1^2(r_{n_3}^2-r_{n_2}^2).
\]

但第一式左边严格大于第二式左边，而第一式右边严格小于第二式右边，矛盾。

因此

\[
\boxed{
\#\{n:\ F_n=N\}\le2.
}
\tag{10.7}
\]

结合 RPF-1：

## Theorem RPF-6 — Uniform Exact Root-Pair Fibre Bound

\[
\boxed{
\left|\mathfrak F_T(\theta,\zeta)\right|
\le2.
}
\tag{10.8}
\]

对所有 fixed \(T\)、所有 algebraically admissible \((\theta,\zeta)\) 统一成立。

**状态：NEW PROVED — Outcome B。**

这个 bound 不依赖任何 divisor-count / Gaussian factor-count invariant。

---

# 11. Double-fibre mechanism and the exact collision equation

若 fibre size = 2，设两个 cut 为

\[
n<m.
\]

写

\[
P
=q10^m+c10^n+r,
\]

其中

\[
q\ge1,
\qquad
c\ge1,
\qquad
0\le r<10^n.
\]

于是：

### cut \(n\)

\[
a_1=10^{m-n}q+c,
\qquad
a_2=r;
\]

### cut \(m\)

\[
a_1'=q,
\qquad
a_2'=c10^n+r.
\]

same-norm collision 的精确条件是

\[
\boxed{
 b_2^2
\Bigl[
(10^{m-n}q+c)^2-q^2
\Bigr]
=
 b_1^2
\Bigl[
(c10^n+r)^2-r^2
\Bigr].
}
\tag{11.1}
\]

等价地，若记

\[
q_n=10^{m-n}q+c,
\qquad
r_m=c10^n+r,
\]

则

\[
\boxed{
\left(\frac{b_2}{b_1}\right)^2
=
\frac{r_m^2-r_n^2}{q_n^2-q_m^2}.
}
\tag{11.2}
\]

所以 two-cut multiplicity 本质上是一个**decimal secant slope 恰为 denominator ratio square** 的算术事件。

进一步，(11.1) 对 \(r\) 是线性的：

\[
\boxed{
r
=
\frac{
 b_2^2\bigl[(10^{2h}-1)q^2+2\cdot10^hqc+c^2\bigr]
-b_1^2c^2 10^{2n}
}{
2b_1^2c10^n
},
\qquad h=m-n.
}
\tag{11.3}
\]

因此固定

\[
(b_1,b_2,n,m,q,c)
\]

后，若 double collision 存在，则末尾 \(r\) 至多唯一。

这进一步说明 multiplicity 不是一个高维 divisor-allocation family，而是极薄的 decimal arithmetic coincidence。

---

# 12. Route C: Gaussian interpretation

令

\[
Z:=X+iY
=(a_1b_2)+i(a_2b_1).
\]

则

\[
\boxed{
N_{\mathbf Z[i]}(Z)=N.
}
\]

所以所有 first-two representations 的 ambient universe 确实可以由 Gaussian divisors / sum-of-two-squares representations 描述。

但 fixed root pair 后还必须满足某个 decimal cut line：

\[
 b_1 10^nX+b_2Y=GP.
\]

Gaussian 写法为

\[
\boxed{
\operatorname{Re}
\Bigl[
(b_1 10^n-i b_2)Z
\Bigr]
=GP.
}
\tag{12.1}
\]

所以 Gaussian representations 只有落在 discrete real-part slices (12.1) 上才与 decimal recovery 有关。

RPF-6 说明：

\[
\boxed{
\text{无论 }r_2(N)\text{ 多大，最终 complete fibre 仍至多有两个点。}
}
\]

因此：

- Gaussian divisor allocation 不是 fibre growth source；
- \(r_2(N)\) 不是正确的 complexity formula；
- 许多 Gaussian representations 被 decimal prefix equation 一次性全部杀掉；
- 剩余 multiplicity 由 cut collision，而不是 Gaussian conjugation 控制。

## 12.1 Gaussian symmetry is not the only local double mechanism

一个 explicit prefix-local counterexample：

\[
P=737,
\qquad
b_1=2,
\qquad
b_2=1.
\]

cut \(n=1\)：

\[
(a_1,a_2)=(73,7),
\]

\[
(X,Y)=(73,14),
\]

\[
N=73^2+14^2=5525.
\]

cut \(n=2\)：

\[
(a_1,a_2)=(7,37),
\]

\[
(X,Y)=(7,74),
\]

\[
N=7^2+74^2=5525.
\]

两组都满足

\[
\gcd(a_1,2)=1,
\qquad
\gcd(a_2,1)=1.
\]

而

\[
(73,14)
\notin
\{(7,74),(74,7),(7,-74),\ldots\}.
\]

所以 double collision 不只是 Gaussian conjugation / coordinate swap。

**状态：COUNTEREXAMPLE — prefix-local, not a complete exact original candidate。**

这个边界非常重要：它证明“Gaussian symmetry only source of multiplicity”作为 local recovery theorem 是 FALSE，但没有构造原题解。

---

# 13. Route D: further root-pair compression

本轮对“root pair 是否 minimal”得到一个比上一轮更精确的答案。

## 13.1 Uniform semantic replacement: \((\theta,\zeta)\leftrightarrow(\mathbf A,N)\)

由 RPF §6：

\[
\boxed{
(T,\theta,\zeta)
\simeq
(T,\mathbf A,N)
}
\]

在 exact-positive recovery semantics 上 lossless。

这不是减少 coordinate count，但它把 root pair 的数学含义完全去神秘化：

\[
\boxed{
\theta,\zeta
\text{ 只是 numerator word + first-two norm 的一种 algebraic coordinate system。}
}
\]

## 13.2 Stronger collapse in \(A_1\)-only

在 \(A_1\)-only 中

\[
\boxed{
S=10^{n_3}.
}
\]

因此 fixed \(T\) 已固定 third cut length \(n_3\)。

给定完整 word \(\mathbf A\)，有

\[
\boxed{
a_3=\mathbf A\bmod S,
}
\]

\[
\boxed{
A_{12}=\left\lfloor\frac{\mathbf A}{S}\right\rfloor.
}
\]

又因 \(\mathbf B\) fixed，

\[
\mathcal R=\frac{\mathbf A}{\mathbf B},
\qquad
r_3=\frac{a_3}{b_3}.
\]

所以

\[
\boxed{
N
=G^2(\mathcal R^2-r_3^2)
}
\tag{13.1}
\]

由 \((T,\mathbf A)\) 唯一确定。

随后

\[
\zeta=\frac{a_3}{\eta_3},
\qquad
\theta=G(\mathcal R-r_3)
\]

也唯一。

故：

## Theorem RPF-7 — \(A_1\) one-word root collapse

\[
\boxed{
(T,\theta,\zeta)
\simeq
(T,\mathbf A)
\qquad
\text{on the }A_1\text{-only exact-admissible locus}.
}
\tag{13.2}
\]

**状态：NEW PROVED — chamber-specific Outcome D。**

自然的一坐标 residual invariant 可以取

\[
\boxed{
\rho_{A_1}:=\mathbf A
}
\]

或 fixed-\(T\) 等价的 linear root combination

\[
\boxed{
\rho_{A_1}'=\tau\theta+G\zeta.
}
\]

## 13.3 Why the same scalar collapse fails in DD

DD 中

\[
S=M_3
\]

只固定 denominator third length \(m_3\)，而

\[
n_3>m_3
\]

仍由 numerator tail 决定。

因此 \(\mathbf A\) alone 并不知道 third cut 在哪里。

本轮构造一个强 algebraic counterexample。

取

\[
b_1=b_2=b_3=1,
\qquad
M_2=M_3=S=10.
\]

则

\[
Q=D=11,
\quad
G=1,
\quad
\eta_3=\tau=1,
\quad
\mathcal L=10,
\quad
\kappa=110,
\]

\[
\mathbf B=111.
\]

固定同一个 numerator word

\[
\boxed{
\mathbf A=56166=111\cdot506.
}
\]

### DD tail cut 1

取

\[
n_3=2,
\qquad
a_3=66.
\]

则

\[
\zeta=66,
\qquad
\theta=506-66=440,
\]

\[
C=\frac{56166-66}{10}=5610,
\]

\[
N=506^2-66^2=251680,
\]

\[
\mathcal C_3=46260720>0.
\]

### DD tail cut 2

取

\[
n_3=3,
\qquad
a_3=166.
\]

则

\[
\zeta=166,
\qquad
\theta=506-166=340,
\]

\[
C=\frac{56166-166}{10}=5600,
\]

\[
N=506^2-166^2=228480,
\]

\[
\mathcal C_3=320897920>0.
\]

两组都满足：

- 同一个 fixed \(T\)；
- 同一个 \(\mathbf A\)；
- \(n_3>m_3\)，均为 DD tail profile；
- \(C,N,\mathcal C_3\) 都为正整数；
- exact coefficient plane；
- gap quadratic；
- primitive-tail quadratic；
- rational-root divisibility（这里 \(\nu=1\)）；
- \(a_3\mid\mathcal C_3\)。

但 root pairs 不同。

因此

\[
\boxed{
(T,\mathbf A)
\not\Rightarrow
(\theta,\zeta)
\qquad(DD)
}
\tag{13.3}
\]

已经在很强的 algebraic/tail-admissible locus 上成立。

**状态：COUNTEREXAMPLE。**

边界：这两个 states 的 first-two norm 尚未由真实 prefix split 实现，因此它们不是完整原题候选；该例用于否定 DD 的 one-word deterministic root reduction，不用于声称 exact fibre 有两个解。

所以当前最准确的 uniform semantic interface 是

\[
\boxed{
(T,\mathbf A,N),
}
\]

而 chamber-specific \(A_1\) 可以继续压到

\[
\boxed{
(T,\mathbf A).
}
\]

---

# 14. Route E: does \((C,N)\) recover the root pair?

用户特别要求反向研究

\[
(\theta,\zeta)
\mapsto(C,N).
\]

本轮可以完整算出其 algebraic fibre。

由 exact plane：

\[
\boxed{
\zeta
=
\frac{
G^2\mathcal LC-(G+\kappa)\tau\theta
}{G\kappa}.
}
\tag{14.1}
\]

代入

\[
N=\theta^2+\frac{2G}{\tau}\theta\zeta
\]

后，得到的单变量方程正是：

\[
\boxed{
D(\kappa+2G)\theta^2
-2G\kappa C\theta
+\kappa DN
=0.
}
\tag{14.2}
\]

也就是旧 gap quadratic。

所以：

\[
\boxed{
(T,C,N)
\text{ 至多恢复两个 algebraic root pairs。}
}
\]

但这没有产生新的 gate；它只是在 inverse-map 语境中重新出现 elimination shadow。

此外 Jacobian 为

\[
\boxed{
\det
\frac{\partial(C,N)}{\partial(\theta,\zeta)}
=
\frac{2}{\mathcal L}
\left(
\theta-\frac{\kappa}{\tau}\zeta
\right).
}
\tag{14.3}
\]

因此除曲线

\[
\tau\theta=\kappa\zeta
\]

外，该 map generically locally invertible；不存在由 coefficient reconstruction 本身强迫的 one-dimensional algebraic relation

\[
P_T(\theta,\zeta)=0.
\]

这说明：

\[
\boxed{
\text{若 root pair 继续降维，来源必须是 integer/decimal realization，}
\text{而不是 coefficient map 的纯代数维数塌缩。}
}
\]

**状态：NEW PROVED algebraic analysis。**

---

# 15. Computational / collision campaign

本轮做了一个 prefix-local exact enumeration，用于压力测试 Unique Prefix Reconstruction Conjecture 和 fibre bound。

搜索范围：

\[
10\le P\le20000,
\qquad
1\le b_1,b_2\le8.
\]

对每个 \(P\) 枚举全部 legal first-two decimal cuts，要求：

- second block 无前导零；
- \(\gcd(a_1,b_1)=1\)；
- \(\gcd(a_2,b_2)=1\)；

并按

\[
N=(a_1b_2)^2+(a_2b_1)^2
\]

分组。

结果：

\[
\boxed{
\text{maximum observed multiplicity}=2.
}
\]

总共找到

\[
\boxed{109}
\]

个 \((b_1,b_2,P,N)\) double-collision classes，没有 triple collision。

**状态：COMPUTATIONAL EVIDENCE。**

随后 RPF-4/RPF-6 已经严格证明 max multiplicity \(\le2\)，所以计算不再承担 theorem 证明责任；它只用于发现 sharp local examples 与失败机制。

## 15.1 Infinite local sharpness family

取

\[
b_1=b_2=1.
\]

令

\[
R_k:=\underbrace{11\cdots1}_{k\text{ digits}}.
\]

对任意 \(p\ne q\)，取

\[
P=R_{p+q}.
\]

cut \(q\) 给出

\[
(a_1,a_2)=(R_p,R_q),
\]

而 cut \(p\) 给出

\[
(a_1',a_2')=(R_q,R_p).
\]

二者有同一个

\[
N=R_p^2+R_q^2.
\]

所以 pure prefix inversion 的 \(\le2\) bound 是 sharp 的。

**状态：PROVED prefix-local infinite family。**

再次强调：这不构造完整 original exact candidates；它只证明不能从 prefix map 本身把 \(2\) 进一步降成 \(1\)。

---

# 16. Twin-Lift Principle: two cuts are globally indistinguishable downstream

这里出现一个重要结构性结论。

假设 fixed denominators \(b_1,b_2\) 与 fixed first-two word \(P\) 有两个 legal reduced cuts：

\[
P=a_1 10^{n}+a_2
=a_1'10^{m}+a_2',
\]

并且

\[
(a_1b_2)^2+(a_2b_1)^2
=
(a_1'b_2)^2+(a_2'b_1)^2
=N.
\]

那么对任何共同 tail

\[
(a_3,b_3,n_3)
\]

只要两种 cut 都满足相同 strict digit condition，二者具有：

- 同一个完整 numerator word \(\mathbf A\)；
- 同一个 denominator word \(\mathbf B\)；
- 同一个 \(N\)；
- 同一个 \(r_3\)；
- 同一个 Euclidean norm；
- 同一个 \((C,D,N,\mathcal C_3)\)；
- 同一个 \((\theta,\zeta)\)。

因此：

## Theorem RPF-8 — Twin-Lift Principle

\[
\boxed{
\text{若一个 double-cut prefix state 的某一 cut 能完成 exact lift，}
\text{另一 cut 也同时 exact lift。}
}
\tag{16.1}
\]

只要两边各自满足 reducedness / digit-cell 条件。

**状态：NEW PROVED。**

这意味着 fibre size \(2\) 若真正出现，不是因为我们“证明工具不够精细”；而是因为 root/coefficient/tail 层在数学上**确实无法区分这两个 candidates**。

所以 exact recovery 的最终 residual multiplicity 若非零，最多就是一个 genuine binary decimal-cut bit：

\[
\boxed{
\omega_{12}\in\{0,1\}.
}
\]

定义 \(\omega_{12}=0\) 选较小 cut，\(\omega_{12}=1\) 选较大 cut，则：

\[
\boxed{
(T,\theta,\zeta,\omega_{12})
\Longrightarrow
\text{complete candidate uniquely}
}
\tag{16.2}
\]

在 fibre 非空时成立。

---

# 17. Admissible root-pair locus after exact local realization

上一轮只得到 algebraic-denominator predicate

\[
\mathfrak A_T(\theta,\zeta).
\]

本轮可以定义真正 exact-realizable root locus：

\[
\boxed{
\mathscr L_T^{\rm ex}
:=
\{(\theta,\zeta):
\mathfrak F_T(\theta,\zeta)\ne\varnothing\}.
}
\]

RPF-1 给出一个完全显式的 membership test。

给定 \((\theta,\zeta)\)：

1. 恢复
   \[
   a_3=\eta_3\zeta;
   \]
2. 取
   \[
   n_3=\operatorname{digits}(a_3);
   \]
3. 检查 DD / \(A_1\) tail trace compatibility；
4. 恢复
   \[
   \mathbf A=SC_T(\theta,\zeta)+a_3;
   \]
5. 恢复
   \[
   P=(\mathbf A-a_3)/10^{n_3};
   \]
6. 恢复
   \[
   N=N_T(\theta,\zeta);
   \]
7. 枚举 \(P\) 的 legal cuts \(n\)，检查
   \[
   F_n=N.
   \]

RPF-6 保证最后一步最多返回两个 cut。

因此：

\[
\boxed{
\mathscr L_T^{\rm ex}
\text{ 不是一个自由的 }\mathbf Q^2\text{ locus；}
}
\]

它是被完整 numerator word、tail boundary 和 weighted decimal split 强烈离散化的 arithmetic set。

但是本轮不声称存在一个单一多项式

\[
P_T(\theta,\zeta)=0
\]

刻画它。事实上 §14 的 Jacobian 分析说明 coefficient map 本身 generically 仍是二维；真正的 collapse 来自 digit/integer realization。

---

# 18. Failed Conjecture / Failed Parametrization Ledger

## F1. Unique Prefix Reconstruction Conjecture

\[
(T,\theta,\zeta)
\Longrightarrow
(a_1,a_2)\text{ unique}.
\]

**状态：OPEN on the exact-candidate locus；FALSE as a pure prefix-local theorem。**

反例机制：repunit swap family、\(P=737\) weighted nonsymmetric collision。

本轮不能把 local collision 冒充 exact-original collision；没有构造原题解。

教训：最强无条件 structural theorem 是 \(\le2\)，不是 \(\le1\)。

---

## F2. One fixed circle–line model

\[
X^2+Y^2=N,
\qquad
\alpha_T X+\beta_TY=\gamma_T.
\]

**状态：DISPROVED as the global fibre model。**

真实 second equation 是

\[
 b_1 10^{n_2}X+b_2Y=GP,
\]

其 coefficient 依赖 unknown cut \(n_2\)。

正确模型：

\[
\boxed{
\text{circle}\cap\text{discrete decimal line pencil}.
}
\]

---

## F3. Fibre growth controlled by \(r_2(N)\) / divisor count

**状态：DISPROVED。**

RPF-6 给出绝对 bound

\[
|\mathfrak F_T|\le2.
\]

Gaussian representation number 可以任意大，但 complete prefix fibre 不随之增长。

---

## F4. Gaussian conjugation is the only multiplicity source

**状态：DISPROVED prefix-locally。**

\(P=737,b_1=2,b_2=1\) 的两个 Gaussian points

\[
73+14i,
\qquad
7+74i
\]

不是彼此的 swap / conjugate / associate。

---

## F5. Quadratic gates remain residual synchronization gates

**状态：DISPROVED / REINTERPRETED。**

Exact coefficient reconstruction 后

\[
Q_{\rm gap}\equiv0,
\qquad
Q_{\rm tail}\equiv0.
\]

它们是 elimination shadows。

---

## F6. \((C,N)\) is a cleaner deterministic replacement of root pair

**状态：NOT DETERMINISTIC in general algebraic sense。**

其 inverse polynomial 正是 gap quadratic，generic degree \(2\)。

所以 \((C,N)\) 没有消除 algebraic conjugacy。

---

## F7. Full numerator word \(\mathbf A\) alone is a uniform strict interface

**状态：FALSE。**

在 \(A_1\) 中 TRUE；在 DD 中由 \(\mathbf A=56166\) explicit collision 否定。

失败机制：DD 的 third numerator cut \(n_3>m_3\) 不被 \(T\) 固定。

---

## F8. \(\theta,\zeta\) genuinely form a free two-dimensional exact-realizable locus

**状态：FALSE as a recovery interpretation；no single algebraic-curve theorem claimed。**

在 complete-realizable locus，它们 factor through

\[
(\mathbf A,N)
\]

并最终通过 decimal cuts 实现。其 discreteness 来自 integer/decimal realization，而非 coefficient map 的纯代数维数下降。

---

# 19. Fibre-size theorem and complete recovery collapse

本轮最短的最终 theorem 可以写成：

## Theorem RPF-9 — Exact Admissible Root-Pair Fibre Compression

固定 strict denominator–decimal trace

\[
T=T_{\rm den,10}
\]

与 positive residual root pair

\[
(\theta,\zeta).
\]

若其 ADRI reconstruction 不满足整数性 / tail compatibility，则

\[
\mathfrak F_T(\theta,\zeta)=\varnothing.
\]

否则，由 \((T,\theta,\zeta)\) 唯一恢复：

\[
\mathbf A,
\quad
\mathbf B,
\quad
a_3,
\quad n_3,
\quad
P=A_{12},
\quad
N.
\]

所有完整 original candidates 与 \(P\) 的 legal decimal cuts \(n\) 满足

\[
 b_2^2
\left\lfloor\frac P{10^n}\right\rfloor^2
+
 b_1^2
(P\bmod10^n)^2
=N
\]

一一对应。

该 cut-energy function 在 legal cut set 上严格离散凸，因此

\[
\boxed{
|\mathfrak F_T(\theta,\zeta)|\le2.
}
\]

若等号成立，两候选唯一差异是 first-two numerator internal cut；所有 downstream Exact-Lift root/coefficient/tail invariants 完全相同。

**状态：NEW PROVED。**

这回答了本轮核心问题：

\[
\boxed{
\text{fixed }(T,\theta,\zeta)
\text{ 后的 exact realization fibre 是 0-dimensional、uniformly finite，}
}
\]

并且具有绝对上界 \(2\)。

它不是 unbounded fibre，也不需要 arithmetic complexity formula \(F(N)\)。

---

# 20. Consequences for Backward Strict Layer

上一轮 Backward architecture 暂写为

\[
T
+(\theta,\zeta)
+\mathfrak A_T
+\mathfrak F_T.
\]

本轮以后可以严格缩成：

\[
\boxed{
T
+(\mathbf A,N)
+\text{decimal cut test},
}
\tag{20.1}
\]

其中 decimal cut test 最多产生两个 candidates。

等价地，在 root coordinates 中：

\[
\boxed{
T
+(\theta,\zeta)
+\omega_{12},
\qquad
\omega_{12}\in\{0,1\},
}
\tag{20.2}
\]

已经足以唯一指定任何存在的 complete candidate。

所以从 canonical synchronization 角度：

\[
\boxed{
\text{alg–den–decimal higher-order non-rectangularity
没有留下无界 local fibre。}
}
\]

剩余 local gluing 只有一个 at-most-binary decimal cut ambiguity。

在 \(A_1\)-only 内更短：

\[
\boxed{
T+\mathbf A+\omega_{12}
}
\]

即可完整恢复。

在 DD 内目前最自然：

\[
\boxed{
T+(\mathbf A,N)+\omega_{12},
}
\]

或原 root coordinates

\[
T+(\theta,\zeta)+\omega_{12}.
\]

---

# 21. Next frontier

本轮不建议再回去攻击：

- gap quadratic；
- primitive-tail quadratic；
- \((C,N)\) resultant；
- Gaussian representation count；
- generic algebraic injectivity。

这些已经不是 fixed root-pair fibre 的障碍。

最自然的新 Backward frontier 有两条。

## Frontier A — Double-Cut Arithmetic Classification

研究 two-cut collision equation

\[
 b_2^2(q_n^2-q_m^2)
=
 b_1^2(r_m^2-r_n^2)
\]

在 reducedness + strict digit cell 下能否进一步分类。

目标不是证明 root pair fibre \(\le2\)（已经完成），而是回答：

\[
\boxed{
\text{exact-realizable double fibre 是否实际上永远不发生？}
}
\]

如果能排除，则可升级到 unique fibre；若不能，则 binary bit 是真正最终接口。

注意 Twin-Lift Principle 说明任何只读取

\[
T,\mathbf A,N,\theta,\zeta,C,D,\mathcal C_3
\]

的 downstream invariant 都无法区分 double cuts。要排除它，只能攻击 double-cut prefix arithmetic 本身，或证明没有 exact state 能落到其 image。

## Frontier B — DD third-cut compression

\(A_1\) 已有

\[
(T,\theta,\zeta)\simeq(T,\mathbf A).
\]

DD 尚差的是：

\[
\mathbf A
\rightsquigarrow
n_3?
\]

也就是问 fixed DD \(T\) 与 full numerator word \(\mathbf A\) 后，是否能由 exact admissibility 唯一恢复 third cut；本轮 explicit collision 证明**纯 algebraic/tail admissibility不够**，因此若继续压缩，必须使用 first-two norm realization。

这两条 frontier 都是 backward recovery 问题，不需要进入 moving-core termination。

---

# 22. Final proved / disproved / computational / open ledger

## PROVED — inherited / frozen

1. sufficient proper denominator–decimal trace
   \[
   T\simeq(b_1,b_2,b_3,S);
   \]
2. fixed-\(T\) \(D\)-freezing
   \[
   D=(M_3/S)Q;
   \]
3. tail–coefficient identity
   \[
   \kappa\tau=G\mathcal LD;
   \]
4. exact oriented coefficient plane;
5. root-pair reconstruction of \(C,N,\mathcal C_3\);
6. canonical denominator recovery / exact concatenation framework;
7. exact DD / \(A_1\) coefficient definitions;
8. rational-root divisibility and tail normalization.
9. ADRI exact concatenation normal form
   \[
   \mathbf A=SC+a_3,
   \qquad
   \mathbf B=SD+b_3.
   \]

## NEW PROVED

1. Full internalization of the two quadratics:
   \[
   Q_{\rm gap}\equiv0,
   \qquad
   Q_{\rm tail}\equiv0
   \]
   after exact reconstruction.
2. Root-pair semantic equivalence:
   \[
   (T,\theta,\zeta)
   \simeq
   (T,\mathbf A,N).
   \]
3. Exact Word-Cut Fibre Bijection.
4. Decimal Split Strict Convexity.
5. No Triple Cut Collision.
6. Uniform Exact Root-Pair Fibre Bound:
   \[
   |\mathfrak F_T(\theta,\zeta)|\le2.
   \]
7. Exact double-cut collision equation / secant-square condition.
8. Twin-Lift Principle.
9. Chamber-specific \(A_1\) one-word collapse:
    \[
    (T,\theta,\zeta)\simeq(T,\mathbf A).
    \]
10. \((C,N)\) inverse is degree \(\le2\) and returns the gap quadratic.
11. Coefficient-map Jacobian
    \[
    \frac{2}{\mathcal L}
    \left(\theta-\frac\kappa\tau\zeta\right).
    \]

## DISPROVED / FAILED

1. a single fixed circle–line model;
2. unbounded fibre / divisor-count-controlled fibre;
3. Gaussian symmetry as the only multiplicity source;
4. the quadratics as residual gates;
5. \((C,N)\) as deterministic root replacement in general;
6. full numerator word \(\mathbf A\) alone as a uniform DD + \(A_1\) interface.

## COMPUTATIONAL EVIDENCE

Prefix-local exhaustive run

\[
P\le20000,
\qquad
b_1,b_2\le8
\]

found max multiplicity \(2\), with 109 double classes; no triple. The theorem now supersedes this evidence.

## OPEN

1. Exact-candidate unique fibre:
   \[
   |\mathfrak F_T(\theta,\zeta)|\le1?
   \]
2. Classification / exclusion of double-cut arithmetic on exact-realizable states.
3. Whether DD admits a further natural one-coordinate semantic collapse after using first-two realization.
4. Categorical minimal encoding dimension of the residual interface.
5. Main strict-layer nonexistence theorem — untouched by this backward fibre result.

---

# 23. Final verdict

本轮成功标准要求至少回答 exact realization freedom 属于

\[
0\text{-dimensional / finite / unique / unbounded}
\]

中的哪一种。

答案现在是严格的：

\[
\boxed{
\textbf{0-dimensional and uniformly finite, with absolute fibre size }\le2.
}
\]

而 multiplicity 的唯一机制也已识别：

\[
\boxed{
\textbf{同一个完整 numerator word 的 first-two decimal cut collision。}
}
\]

所以 fixed root pair 后并不存在隐藏的 Gaussian/divisor/Hensel continuum，也不存在随 \(N\) 增长的 representation fibre。

Backward recovery 可以进一步压成：

\[
\boxed{
T+(\mathbf A,N)+\text{at most one binary cut bit}.
}
\]

在 \(A_1\)-only 中还可进一步压成：

\[
\boxed{
T+\mathbf A+\text{at most one binary cut bit}.
}
\]

这就是本轮的 exact admissible root-pair fibre compression。
