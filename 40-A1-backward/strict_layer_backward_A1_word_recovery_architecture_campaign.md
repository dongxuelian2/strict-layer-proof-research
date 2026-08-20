# 三项十进制拼接平方和问题：Backward Strict Layer — A1 Word-Recovery Architecture Campaign

**文件名：** `strict_layer_backward_A1_word_recovery_architecture_campaign.md`  
**日期：** 2026-08-16  
**研究范围：** Strict Layer，仅研究 \(A_1\)-only 的反向 exact-recovery；DD 已闭合。  
**本轮纪律：** 不使用 moving primitive-core height、\(Q_0\to\infty\)、large-height square-spacing 或任何正向终止定理制造新反向结论；不迁移 DD 专属 source orientation / quotient machinery；所有计算仅作 falsification / structure discovery。

---

# 1. Executive summary

本轮没有关闭 \(A_1\)，但得到了一个明显比原始 A1-WR 更适合长期反向推进的规范形，并且较系统地判死了几类过强的 prime-support / determinant / Gaussian 猜想。

最重要的结论可以压成四层。

## 1.1 第一层：fixed-\(T\) 后最自然的 exact semantic coordinate 不是 raw \(\mathbf A\)，而是一个 canonical word quotient

固定

\[
T=(b_1,b_2,b_3,S),\qquad S=10^{n_3},
\]

令

\[
\mathbf B=SD+b_3,\qquad D=10^gQ,
\qquad Q=b_1 10^{m_2}+b_2,
\qquad G=b_1b_2,
\]

以及

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3).
\]

定义

\[
\boxed{
\Gamma:=\gcd(\mathbf B,\Lambda),
\qquad
E:=\frac{\mathbf B}{\Gamma}.
}
\]

已有 strict-layer canonical balance / denominator-kernel theorem 给出

\[
\boxed{E\mid\mathbf A.}
\]

因此可写

\[
\boxed{
\mathbf A=EW,\qquad
\mathbf B=E\Gamma.
}
\]

于是

\[
\boxed{
\frac{\mathbf A}{\mathbf B}=\frac W\Gamma.
}
\]

所以 fixed \(T\) 后，推荐把 residual full-word coordinate 从 \(\mathbf A\) 改写为

\[
\boxed{W=\mathbf A/E.}
\]

完整 exact A1 recovery 的最短 backward chart 因而是

\[
\boxed{
(T,W,n),
}
\]

其中 \(n\) 是 first-two cut；在 two-cut collision 时它只剩一位 binary choice。

**状态：REINTERPRETED EXISTING RESULT + NEW CANONICAL NORMAL FORM.**

---

## 1.2 第二层：raw WGF 不增加逻辑信息，但 exact balance 会把其中伪造的 \(\mathbf B^2\) prime supply 精确消掉

raw A1-WR 给出

\[
N\mathbf B^2b_3^2
=
G^2
(b_3\mathbf A-a_3\mathbf B)
(b_3\mathbf A+a_3\mathbf B).
\]

设

\[
K_-:=b_3W-a_3\Gamma,
\qquad
K_+:=b_3W+a_3\Gamma.
\]

由于

\[
\mathbf A=EW,\qquad
\mathbf B=E\Gamma,
\]

两边的 \(E^2\) 精确约掉，得到

\[
\boxed{
N\Gamma^2b_3^2
=
G^2K_-K_+.
}
\tag{BR-WGF}
\]

而由

\[
\mathbf A=SP+a_3,\qquad
\mathbf B=SD+b_3
\]

有

\[
\boxed{
K_-
=
S(\Gamma P-DW)>0.
}
\tag{BR-GAP}
\]

因此：

- raw WGF **不是** A1-WR 之外的新 necessary condition；
- 但经 exact-balance quotient 后，它成为一个真正有 source labels 的 factorization normal form；
- 特别地，原先看似“denominator word \(\mathbf B^2\) 需要巨大 square supply”的直觉会严重过计：其中 \(E^2\) 是强制的 global word content，会在两 gap factors 中同步出现并精确消去。

**状态：NEW PROVED NORMALIZATION / STRONG NEGATIVE RESULT AGAINST RAW \(\mathbf B^2\)-SUPPLY ROUTE.**

---

## 1.3 第三层：primitive slope + tail deflation 给出真正的 A1 oriented determinant

令

\[
h:=\gcd(W,\Gamma),
\qquad
W=hu,\quad \Gamma=hv,
\qquad
\gcd(u,v)=1.
\]

则

\[
\frac{\mathbf A}{\mathbf B}=\frac uv
\]

为全局拼接比的最简分数。

由 (BR-GAP) 可得

\[
\boxed{
J_-:=b_3u-a_3v
=
S\varepsilon>0,
}
\tag{PWG-}
\]

其中

\[
\boxed{
\varepsilon=vP-Du\in\mathbf Z_{>0}.
}
\]

并定义

\[
J_+:=b_3u+a_3v.
\]

于是

\[
\boxed{
Nv^2b_3^2
=
G^2J_-J_+.
}
\tag{PWG}
\]

这已经给出一个**完全来自 A1 word structure 自身的 orientation**：

\[
\boxed{
b_3u-a_3v>0.
}
\]

它不是 DD source orientation 的迁移。

进一步使用已有 tail normalization

\[
\eta:=\gcd(S,b_3),
\qquad
S=\eta\mathcal L,
\qquad
b_3=\eta\tau,
\qquad
\gcd(\mathcal L,\tau)=1,
\]

由 \(\gcd(a_3,b_3)=1\) 与 \(J_-=S\varepsilon\) 得

\[
\boxed{\eta\mid v.}
\]

写

\[
v=\eta\bar v.
\]

则 primitive word gap 精确降为

\[
\boxed{
\tau u-a_3\bar v
=
\mathcal L\,\varepsilon>0.
}
\tag{DG}
\]

同时

\[
\boxed{
N\eta^2\bar v^2\tau^2
=
G^2
(\tau u-a_3\bar v)
(\tau u+a_3\bar v).
}
\tag{DG-N}
\]

本报告建议把 (DG)+(DG-N) 称为

\[
\boxed{
\textbf{Deflated A1 Oriented Word-Gap Normal Form}.
}
\]

这是本轮最值得以后连续推进的 arithmetic language。

**状态：NEW PROVED.**

---

## 1.4 第四层：reducedness 把两个 gap factors 的共同 odd-prime freedom 压到显式 cross-content

定义

\[
c_a:=\gcd(a_3,u),
\qquad
c_\tau:=\gcd(\tau,\bar v).
\]

则

\[
\gcd(c_a,c_\tau)=1.
\]

写

\[
a_3=c_a a,\qquad
u=c_a x,
\]

\[
\tau=c_\tau b,\qquad
\bar v=c_\tau y.
\]

则

\[
\gcd(bx,ay)=1.
\]

定义

\[
\boxed{
Z_-:=bx-ay,
\qquad
Z_+:=bx+ay.
}
\]

于是

\[
\boxed{
\tau u\mp a_3\bar v
=
c_ac_\tau Z_\mp,
}
\]

并且

\[
\boxed{
\gcd(Z_-,Z_+)\mid2.
}
\tag{CG}
\]

所以 normalized gap pair 在所有 odd primes 上是真正的 complementary allocation。

更重要的是，\(\mathcal L\) 与 \(c_\tau\) 互素，因此

\[
\boxed{
c_ac_\tau Z_-
=
\mathcal L\varepsilon
}
\]

中，任何 residual decimal-prime depth \(\mathcal L\) 都不可能被 \(c_\tau\) 吸收；它只能进入

\[
c_a
\quad\text{或}\quad
Z_-.
\]

对 \(p=5\)，一旦还有 residual depth 进入 \(Z_-\)，由 \(\gcd(Z_-,Z_+)=1\) at \(5\)，该 depth 完全单侧定向。

**状态：NEW PROVED.**

---

## 1.5 Prefix norm 也有一个 canonical reducedness content

令

\[
X=a_1b_2,\qquad
Y=a_2b_1,
\qquad
N=X^2+Y^2.
\]

逐项既约性给出精确公式

\[
\boxed{
\gcd(X,Y)
=
\gcd(a_1,a_2)\gcd(b_1,b_2).
}
\tag{NC}
\]

且右边两个因子互素。

令

\[
c_N:=\gcd(X,Y),
\qquad
X=c_Nx_0,\quad Y=c_Ny_0,
\qquad
\gcd(x_0,y_0)=1,
\]

\[
\boxed{
N=c_N^2N_0,
\qquad
N_0=x_0^2+y_0^2.
}
\]

因此对每个

\[
p\equiv3\pmod4,
\]

有

\[
p\nmid N_0.
\]

将其代入 normalized gap equation 得

\[
\boxed{
(c_N\eta\bar v\tau)^2N_0
=
(Gc_ac_\tau)^2Z_-Z_+.
}
\tag{SC}
\]

故在 \(\mathbf Q^\times/\mathbf Q^{\times2}\) 中

\[
[Z_-Z_+]=[N_0].
\]

又因 odd primes 不可能同时进入 \(Z_-,Z_+\)，所以：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
v_p(Z_-),v_p(Z_+)\text{ 都是偶数}.
}
\tag{IR}
\]

从而：

\[
\boxed{
Z_-,Z_+
\text{ 各自都是两个平方之和}.
}
\tag{GS}
\]

这不是 generic \(r_2(N)\) representation counting，而是保留了 **actual decimal word-gap labels** 的 Gaussian-compatible invariant。

**状态：NEW PROVED.**

---

## 1.6 但是 pure prime / Gaussian / determinant route 仍不足以闭合 A1

存在一个显式无限 ambient pseudo-family，它满足：

- 全局 exact ratio / balance；
- third-tail word；
- A1-WR 所需的 slope difference；
- reducedness；
- 二平方 norm；
- Deflated oriented gap；
- tail certificate；
- \(Z_\pm\) 的 near-coprime / sum-of-two-squares structure；

却只在一个地方失败：

\[
\boxed{
\textbf{用于 norm 的 first-two pair 不是完整 word }P\textbf{ 的真实 decimal cut}.
}
\]

取

\[
b_1=b_2=b_3=1,\qquad S=10,
\]

任意 \(k\ge1\)，令

\[
a_1=10k,\qquad
a_2=50k^2,\qquad
a_3=1,
\]

\[
t=50k^2+1.
\]

则

\[
a_1^2+a_2^2+a_3^2=t^2.
\]

令 balanced numerator word

\[
\mathbf A^*=111t.
\]

则

\[
\frac{\mathbf A^*}{111}=t,
\qquad
\mathbf A^*\equiv1\pmod{10}.
\]

并且

\[
N=a_1^2+a_2^2=t^2-1
=
(t-1)(t+1).
\]

此时

\[
Z_-=t-1=50k^2,
\qquad
Z_+=t+1=50k^2+2,
\]

且

\[
Z_-= (5k)^2+(5k)^2,
\]

\[
Z_+=(5k-1)^2+(5k+1)^2.
\]

但

\[
P^*=\frac{\mathbf A^*-1}{10}
=
555k^2+11
\]

并不等于

\[
a_1 10^{\ell(a_2)}+a_2.
\]

\(k=1\) 时：

\[
P^*=566,
\qquad
10\cdot100+50=1050.
\]

\(k\ge2\) 时量级已经分别为 \(O(k^2)\) 与 \(>500k^3\)，更不可能相等。

因此：

\[
\boxed{
\textbf{任何忘掉 actual first-two decimal cut 的 backward obstruction，}
\textbf{即使保留 norm、prime、Gaussian、tail、reducedness，仍然不够。}
}
\]

**状态：NEW PROVED AMBIENT PSEUDO-FAMILY / FUNDAMENTAL NEGATIVE RESULT.**

---

## 1.7 本轮最终结论

A1 的 backward 本体现在可以压成三个真正不可丢的 semantic relations：

\[
\boxed{
R_{\rm word}
\Join
R_{\rm norm}
\Join
R_{\rm red}.
}
\]

其中：

- \(R_{\rm word}\)：同一个 \(W\) 必须通过 \(E\) 恢复同一个完整 numerator word，并由一个 A1-legal cut 产生 \(a_1,a_2,a_3\)；
- \(R_{\rm norm}\)：同一个 cut 必须满足 BR-WGF / DG-N；
- \(R_{\rm red}\)：三个恢复块逐项既约。

root quadratics / discriminants / resultants / tail certificate 在当前 exact A1 fibre 中均应作为 derived certificates / prefilters，而不是第四个 terminal world。

本轮没有证明

\[
R_{\rm word}\Join R_{\rm norm}\Join R_{\rm red}
=\varnothing.
\]

所以：

\[
\boxed{\textbf{A1 NOT CLOSED.}}
\]

但剩余 proof obligation 已经从“研究许多 prime gates”压成了一个单一的：

\[
\boxed{
\textbf{Backward A1 Cut–Gap Synchronization Theorem}.
}
\]

其精确定理陈述见第 23 节。

---

# 2. Frozen A1 state after SGR-10B

本轮重新核验并冻结以下状态。

\[
\boxed{
\delta_3\le0,\qquad
\delta_2+\delta_3>0.
}
\]

令

\[
g=m_3-n_3\ge0,
\]

\[
k_{12}=n_2-m_2-g\ge1.
\]

于是

\[
n_2=m_2+g+k_{12}.
\]

有效第三尾尺度：

\[
\boxed{
S=10^{n_3}.
}
\]

固定

\[
\boxed{
T=(b_1,b_2,b_3,S)
}
\]

后，以下量全部 deterministic：

\[
m_i,\quad
Q=b_1 10^{m_2}+b_2,
\quad
G=b_1b_2,
\]

\[
g=m_3-n_3,
\quad
D=10^gQ,
\]

\[
\eta=\gcd(S,b_3),
\quad
\mathcal L=S/\eta,
\quad
\tau=b_3/\eta,
\]

以及 denominator-side \(\kappa\)、tail certificate 等。

完整 denominator word：

\[
\boxed{
\mathbf B=SD+b_3.
}
\]

完整 numerator word：

\[
\boxed{
\mathbf A=SP+a_3,
\qquad
P=A_{12}.
}
\]

fixed \((T,\mathbf A)\) 后：

\[
a_3=\mathbf A\bmod S,
\qquad
P=\left\lfloor\frac{\mathbf A}{S}\right\rfloor.
\]

对 cut \(n\)：

\[
q_n=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
r_n=P\bmod10^n,
\]

\[
a_1=q_n,\qquad
a_2=r_n.
\]

weighted prefix norm：

\[
\boxed{
F_n=b_2^2q_n^2+b_1^2r_n^2.
}
\]

A1-WR：

\[
\boxed{
F_n
=
G^2
\left[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
-
\left(\frac{a_3}{b_3}\right)^2
\right].
}
\tag{A1-WR}
\]

fixed \((T,\mathbf A)\) 后，legal cut fibre \(\le2\)，且该 bound prefix-locally sharp。

Twin-Lift Principle 冻结为：

\[
\boxed{
\text{若两个 cuts 有相同 }(T,\mathbf A,N)
\text{ 且各自 legal/reduced，downstream exact data 无法区分。}
}
\]

因此本轮不再追 fibre \(\le1\)。

**状态：PROVED / FROZEN.**

---

# 3. Anti-duplication boundary

本轮已阅读最新正向 A1 报告

`strict_layer_A1_moving_core_decimal_translation_global_campaign.md`，

但只用它确认责任边界。

本报告**没有使用**其中新的：

- \(Q_0\to\infty\)；
- primitive-core height；
- translation-line asymptotics；
- \(g=O(\log Q_0)\)；
- flat moving locus；
- square-cubic moving geometry；
- large-height uniform termination

来证明任何本轮 theorem。

因此本轮所有 NEW PROVED 都是 fixed-word / exact-recovery arithmetic。

同样，本轮没有迁移 DD 的：

- source-labelled \(F_-/F_+\) orientation；
- post-deflation \(J^\sharp,K^\sharp\)；
- DD double resonance；
- top-tail quotient difference；
- Hensel source phase；
- DD \(5\)-adic overload theorem。

A1 中出现的 minus orientation 完全来自

\[
\frac{\mathbf A}{\mathbf B}>\frac{a_3}{b_3}
\]

与 decimal word identity 本身。

---

# 4. Source / provenance audit

本轮重点使用或交叉核对：

1. `strict_layer_post_DD_consolidation_A1_frontier.md`
   - DD closure 后 Strict Layer 只剩 A1；
   - fixed \(T\) 的 denominator deterministic views；
   - A1-WR；
   - root/quadratic data 在 exact fibre 中退化为 elimination shadows。

2. `strict_layer_backward_exact_root_pair_fibre_campaign.md`
   - A1 one-word collapse；
   - exact word-cut fibre bijection；
   - strict discrete convexity；
   - fibre \(\le2\)；
   - repunit infinite sharpness；
   - Twin-Lift Principle。

3. `strict_layer_backward_denominator_decimal_interface.md`
   - canonical balance
     \[
     \Lambda\mathbf A=t\mathbf B;
     \]
   - A1 effective tail \(S=10^{n_3}\)；
   - \((\eta,\mathcal L,\tau)\) 为 trace-derived。

4. `strict_layer_backward_algebraic_denominator_interface.md`
   - fixed \(T\) freezing；
   - quadratic compatibility strictly weaker than exact recovery；
   - local prefix realization 是 genuinely missing source information。

5. `strict_layer_backward_canonical_synchronization_quotient.md`
   - exact gluing 不可被无证明的粗 quotient 替代；
   - coefficient plane / real blocks 必须指向同一个 completion。

6. `strict_layer_backward_global_witness_gluing_campaign.md`
   - canonical global witness；
   - natural-join / same-witness interpretation。

7. `strict_layer_unified_exact_lift_campaign.md`
   与 `(1)` 版本：
   - A1 coefficient definitions；
   - tail certificate
     \[
     S\mid\kappa^2(\kappa+2G).
     \]

8. `strict_layer_final_campaign.md`
   - strict foundation 中已有
     \[
     E=\mathbf B/\gcd(\mathbf B,\Lambda)\mid\mathbf A
     \]
     的 denominator-kernel forcing；
   - global word gcd \(\gcd(\mathbf A,\mathbf B)\) prime-to-\(10\)；
   - denominator kernel 的 odd-prime structure。

9. `exact_lift_research_synthesis_2026-08-10.md`
   - 只接受被后续报告重新审计保留的 A1 facts；
   - 不采用其中已经撤回的旧 A1 closure。

10. 最新正向 A1 moving-core 报告：
    - 只作为 anti-duplication boundary。

本轮没有把 synthesis 中旧“gap scale mismatch”或 Gaussian flip closure 当作 theorem。

---

# 5. Minimal backward state reconstruction

## 5.1 Raw semantic chart

SGR-10B 后，最直接的 exact chart 是

\[
(T,\mathbf A,n).
\]

其中 \(n\) 是 legal first-two cut。

一旦 fixed：

\[
a_3=\mathbf A\bmod S,
\qquad
P=\lfloor\mathbf A/S\rfloor,
\]

\[
a_1=\lfloor P/10^n\rfloor,
\qquad
a_2=P\bmod10^n.
\]

因此所有原六块都已恢复。

---

## 5.2 Canonical quotient chart

令

\[
\Gamma=\gcd(\mathbf B,\Lambda),
\qquad
E=\mathbf B/\Gamma.
\]

由 inherited denominator-kernel theorem：

\[
E\mid\mathbf A.
\]

定义

\[
W=\mathbf A/E.
\]

则：

\[
\mathbf A=EW,
\qquad
\mathbf B=E\Gamma.
\]

fixed \(T\) 时 \(E,\Gamma\) 均已知，所以

\[
\boxed{
(T,\mathbf A,n)
\Longleftrightarrow
(T,W,n).
}
\]

因此 \(W\) 没有丢信息，却移除了一个完全由 denominator word 强制出来的 common multiplier。

这正是反向 prime analysis 最需要的 normalization。

---

## 5.3 Exact sufficiency

固定 \(T\)，取 \(W>0\)，令

\[
\mathbf A=EW.
\]

若：

1. \(a_3=\mathbf A\bmod S\) 是合法 \(n_3\)-digit block；
2. \(P=(\mathbf A-a_3)/S\)；
3. 存在 A1-legal cut \(n\ge m_2+g+1\)；
4. 由该 cut 得到的 \(a_1,a_2\) digit-legal；
5. \(\gcd(a_i,b_i)=1\)；
6. BR-WGF 成立；

则：

\[
\frac{\mathbf A}{\mathbf B}=\frac W\Gamma,
\]

而 BR-WGF 等价于

\[
\frac{a_1^2}{b_1^2}
+
\frac{a_2^2}{b_2^2}
=
\left(\frac W\Gamma\right)^2
-
\frac{a_3^2}{b_3^2}.
\]

故恢复出完整 original candidate。

因此：

\[
\boxed{
\text{fixed }T\text{ 后，}
(T,W,n)+\text{digit}+\text{reducedness}+\text{BR-WGF}
}
\]

是一个 exact iff normal form。

**状态：NEW PROVED.**

---

# 6. Candidate coordinate systems

| 坐标 | 优点 | 缺点 | 本轮裁决 |
|---|---|---|---|
| \((T,\mathbf A,n)\) | semantic 最直接；SGR-10B 已验证 | raw word content 过大 | exact，但不最适合 prime audit |
| \((\mathbf A,\mathbf B,N,n)\) | A1-WR 对称 | 忘记 denominator provenance | 可用，不作为主坐标 |
| \((P,D,a_3,b_3,N,n)\) | determinant 直接 | global exact balance 不显式 | 辅助 |
| \((\Delta,U_+,N)\) | factorization 漂亮 | raw \(\mathbf B^2\) supply 过计 | 不作为最终坐标 |
| \((T,W,n)\) | 无损去除强制 word content | 仍保留 decimal cut | **主 semantic chart** |
| \((u,v;a_3,b_3)\) | primitive slope / gcd / Gaussian 清晰 | 丢掉 global multiplier \(h\) 与 carry | arithmetic projection |
| \((u,\bar v;a_3,\eta,\tau,\mathcal L)\) | tail-deflated determinant最清楚 | 仍需回接 \(W\) 与 cut | **主 arithmetic chart** |

本轮最终采用双层语言：

\[
\boxed{
\text{semantic layer }(T,W,n)
}
\]

加

\[
\boxed{
\text{arithmetic layer }(u,\bar v,a_3;\eta,\tau,\mathcal L).
}
\]

---

# 7. A1 word-gap factorization derivation

由 A1-WR：

\[
N
=
G^2
\left[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
-
\left(\frac{a_3}{b_3}\right)^2
\right].
\]

乘以 \(\mathbf B^2b_3^2\)：

\[
\boxed{
N\mathbf B^2b_3^2
=
G^2
(b_3\mathbf A-a_3\mathbf B)
(b_3\mathbf A+a_3\mathbf B).
}
\tag{WGF-0}
\]

A1 中：

\[
\mathbf A=SP+a_3,
\qquad
\mathbf B=SD+b_3.
\]

所以

\[
b_3\mathbf A-a_3\mathbf B
=
S(b_3P-a_3D).
\]

定义

\[
\Delta=b_3P-a_3D.
\]

因为 \(N>0\)，所有量正，A1-WR 强制

\[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
>
\left(\frac{a_3}{b_3}\right)^2.
\]

两边正，因此

\[
\boxed{
\frac{\mathbf A}{\mathbf B}>
\frac{a_3}{b_3},
}
\]

故

\[
\boxed{\Delta>0.}
\]

于是：

\[
\boxed{
N\mathbf B^2b_3^2
=
G^2S\Delta
(b_3\mathbf A+a_3\mathbf B).
}
\tag{WGF}
\]

用户给出的 valuation identity 因而正确：

\[
\boxed{
v_p(N)+2v_p(\mathbf B)+2v_p(b_3)
=
2v_p(G)+v_p(S)+v_p(\Delta)
+v_p(b_3\mathbf A+a_3\mathbf B).
}
\]

**状态：NEW PROVED DIRECT DERIVATION.**

---

# 8. Is WGF genuinely stronger than A1-WR?

## 8.1 逻辑上：否

WGF 只是 A1-WR 乘分母后的 difference-of-squares factorization。

因此：

\[
\boxed{
\text{WGF alone does not add a new necessary condition.}
}
\]

任何只把 WGF 当“出现两个整数因子，所以有新 obstruction”的论证都是误判。

---

## 8.2 规范化后：是一个明显更好的 source-labelled normal form

代入

\[
\mathbf A=EW,\qquad
\mathbf B=E\Gamma
\]

得到：

\[
U_\pm:=b_3\mathbf A\pm a_3\mathbf B
=
E(b_3W\pm a_3\Gamma).
\]

raw WGF 两边的 \(E^2\) 消去：

\[
\boxed{
N\Gamma^2b_3^2
=
G^2
(b_3W-a_3\Gamma)
(b_3W+a_3\Gamma).
}
\]

所以：

\[
\boxed{
\text{WGF 的真正价值不是多出一个 equation，}
}
\]

而是：

\[
\boxed{
\text{在 exact balance 后暴露“哪些 prime mass 是强制 common content，}
\text{哪些才是真正 residual allocation”。}
}
\]

这也是本轮最重要的负面修正：

\[
\boxed{
\mathbf B^2\text{ 的巨大 square divisor 不能直接当作需要 gap factors 外部供给的质量。}
}
\]

---

# 9. \((U_-,U_+)\) gcd / support analysis

## 9.1 Raw gcd 不能假定很小

raw

\[
U_\pm=b_3\mathbf A\pm a_3\mathbf B
\]

满足

\[
\gcd(U_-,U_+)
\mid2b_3\mathbf A,
\]

\[
\gcd(U_-,U_+)
\mid2a_3\mathbf B.
\]

但这远不足以推出一个 uniform small gcd。

因为

\[
U_\pm
=
E h J_\pm,
\]

其中 \(E h=\gcd(\mathbf A,\mathbf B)\) 可以带入真正的 global common content。

所以：

\[
\boxed{
\gcd(U_-,U_+)\mid O(1)
}
\]

是错误方向。

---

## 9.2 Primitive slope

令

\[
h=\gcd(W,\Gamma),
\qquad
W=hu,\quad
\Gamma=hv,
\quad
\gcd(u,v)=1.
\]

则

\[
K_\pm=b_3W\pm a_3\Gamma
=
hJ_\pm,
\]

其中

\[
J_\pm=b_3u\pm a_3v.
\]

又

\[
J_-=S(vP-Du)>0.
\]

---

## 9.3 Tail deflation

写

\[
b_3=\eta\tau,\qquad
S=\eta\mathcal L.
\]

由 \(J_-=S\varepsilon\)：

\[
\eta\tau u-a_3v
=
\eta\mathcal L\varepsilon.
\]

因为

\[
\gcd(a_3,\eta)=1,
\]

得

\[
\eta\mid v.
\]

令

\[
v=\eta\bar v.
\]

得到：

\[
H_-:=\tau u-a_3\bar v
=
\mathcal L\varepsilon,
\]

\[
H_+:=\tau u+a_3\bar v.
\]

---

## 9.4 Cross-content extraction theorem

定义

\[
c_a=\gcd(a_3,u),
\qquad
c_\tau=\gcd(\tau,\bar v).
\]

写

\[
a_3=c_aa,\quad u=c_ax,
\]

\[
\tau=c_\tau b,\quad \bar v=c_\tau y.
\]

由：

\[
\gcd(a_3,\tau)=1,
\qquad
\gcd(u,\bar v)=1
\]

可逐项验证：

\[
\gcd(a,x)=
\gcd(b,y)=
\gcd(a,b)=
\gcd(x,y)=1,
\]

并且

\[
\boxed{
\gcd(bx,ay)=1.
}
\]

故

\[
Z_\pm=bx\pm ay
\]

满足

\[
\gcd(Z_-,Z_+)
\mid
\gcd(2bx,2ay)
\mid2.
\]

所以：

\[
\boxed{
\gcd(Z_-,Z_+)\in\{1,2\}.
}
\]

原 factors 则为：

\[
\boxed{
H_\pm=c_ac_\tau Z_\pm,
}
\]

\[
\boxed{
J_\pm=\eta c_ac_\tau Z_\pm,
}
\]

\[
\boxed{
U_\pm=Eh\eta c_ac_\tau Z_\pm.
}
\]

因此所有 odd common-prime freedom 被精确定位到：

\[
E,\quad h,\quad\eta,\quad c_a,\quad c_\tau,
\]

而 \(Z_-,Z_+\) 的 odd prime supports disjoint。

**状态：NEW PROVED.**

---

# 10. Prime-supply valuation ledger

本轮不再使用 raw WGF 的单层 ledger，而保留四个尺度。

## 10.1 Raw word level

\[
v_p(N)+2v_p(\mathbf B)+2v_p(b_3)
=
2v_p(G)+v_p(U_-)+v_p(U_+).
\]

---

## 10.2 Exact-balance reduced level

\[
\boxed{
v_p(N)+2v_p(\Gamma)+2v_p(b_3)
=
2v_p(G)+v_p(K_-)+v_p(K_+).
}
\tag{L1}
\]

这里已经删除全部强制 word multiplier \(E\)。

---

## 10.3 Primitive slope level

\[
\boxed{
v_p(N)+2v_p(v)+2v_p(b_3)
=
2v_p(G)+v_p(J_-)+v_p(J_+).
}
\tag{L2}
\]

---

## 10.4 Tail-deflated / cross-content level

由

\[
v=\eta\bar v,\qquad b_3=\eta\tau,
\]

以及

\[
J_\pm=\eta c_ac_\tau Z_\pm,
\]

得到：

\[
\boxed{
v_p(N)
+2v_p(\eta)
+2v_p(\bar v)
+2v_p(\tau)
=
2v_p(G)
+2v_p(c_a)
+2v_p(c_\tau)
+v_p(Z_-)
+v_p(Z_+).
}
\tag{L3}
\]

这是本轮推荐的 prime-supply ledger。

其优势是：

- forced global word content \(E,h\) 已完全删除；
- common third-tail content \(\eta\) 显式保留；
- residual cross-content \(c_a,c_\tau\) 显式保留；
- \(Z_\pm\) odd-prime supports disjoint；
- decimal modulus \(\mathcal L\) 只进入 oriented minus side。

---

# 11. \(2/5\)-adic branch

## 11.1 Residual decimal demand 精确落在 minus factor

由

\[
c_ac_\tau Z_-=\mathcal L\varepsilon
\]

且

\[
\gcd(c_\tau,\mathcal L)=1,
\]

对 \(p\in\{2,5\}\) 得：

\[
\boxed{
v_p(c_a)+v_p(Z_-)
=
v_p(\mathcal L)+v_p(\varepsilon).
}
\tag{D-p}
\]

所以 residual tail demand

\[
v_p(\mathcal L)
=
n_3-\min(n_3,v_p(b_3))
\]

只能由：

\[
c_a=\gcd(a_3,u)
\]

与

\[
Z_-
\]

承担。

---

## 11.2 Partial-saturation branch 更刚性

若

\[
0<v_p(b_3)<n_3,
\]

则 \(p\mid\eta\)。

因为：

\[
\eta\mid v,\qquad \gcd(u,v)=1
\]

有

\[
p\nmid u.
\]

又因

\[
p\mid b_3,\qquad \gcd(a_3,b_3)=1
\]

有

\[
p\nmid a_3.
\]

故

\[
v_p(c_a)=0.
\]

因此：

\[
\boxed{
v_p(Z_-)
=
v_p(\mathcal L)+v_p(\varepsilon)
\ge
n_3-v_p(b_3).
}
\tag{PS}
\]

对 \(p=5\)，由于

\[
\gcd(Z_-,Z_+)=1\text{ at }5,
\]

有

\[
\boxed{
v_5(Z_+)=0.
}
\]

所以 partial \(5\)-saturation 产生真正的 one-sided residual depth。

**状态：NEW PROVED.**

---

## 11.3 \(v_p(b_3)=0\) 的 escape

若 \(p\nmid b_3\)，则 \(\eta\) 不含该 \(p\)，而 \(a_3\) 可以含 \(p\)。

此时

\[
c_a=\gcd(a_3,u)
\]

可以吸收部分甚至全部 residual decimal depth。

因此 pure statement

\[
v_p(\mathcal L)\le v_p(Z_-)
\]

并非 uniform true。

这是一个明确的 escape mechanism。

---

## 11.4 Saturated branch

若

\[
S\mid b_3,
\]

则

\[
\mathcal L=1.
\]

于是 (DG) 失去任何 residual decimal modulus：

\[
\tau u-a_3\bar v=\varepsilon.
\]

所以：

\[
\boxed{
\text{saturated A1 中，pure residual }2/5\text{-phase route 本身没有大 modulus 可用。}
}
\]

这解释了为什么只靠 \(S\) 的显式出现不能统一关闭 A1。

---

## 11.5 与 denominator-tail certificate 的关系

已有：

\[
\kappa\tau=G\mathcal LD.
\]

因为

\[
\gcd(\mathcal L,\tau)=1,
\]

有：

\[
\boxed{\mathcal L\mid\kappa.}
\]

写

\[
\kappa=\mathcal L\kappa_0.
\]

则

\[
\kappa_0\tau=GD.
\]

tail certificate：

\[
S=\eta\mathcal L
\mid
\kappa^2(\kappa+2G)
\]

化为

\[
\eta\mathcal L
\mid
\mathcal L^2\kappa_0^2
(\mathcal L\kappa_0+2G).
\]

因此至少一个完整 \(\mathcal L\) 因子已经由 denominator-side \(\kappa\) 自动提供。

而 exact word recovery 的 (DG) 要求的是：

\[
\boxed{
\mathcal L
\mid
\tau u-a_3\bar v.
}
\]

所以二者不是“同一批 prime mass 的重复写法”：

- tail certificate 是**乘法 supply**；
- word gap 是**加法 phase / determinant synchronization**。

本轮认为这里存在真正的 backward coupling 机会。

但无限 detached-prefix pseudo-family（第 19 节）证明：

\[
\boxed{
\text{即使两者同时成立，若不接 actual cut，仍不足以矛盾。}
}
\]

---

## 11.6 \(5\) versus \(2\)

当前反向线中：

\[
\boxed{
p=5
}
\]

比 \(p=2\) 更干净，因为：

- \(\gcd(Z_-,Z_+)\mid2\)，所以 \(5\) 永远不会在 normalized pair 两侧共享；
- residual \(5\)-depth 因而严格 one-sided；
- \(2\) 仍允许一个 common factor \(2\)，且 equal-valuation cancellation 的 parity bookkeeping 更复杂。

因此若下一轮做 decimal-prime phase，优先 \(5\)。

---

# 12. \(p\equiv3\pmod4\) norm-rigid branch

## 12.1 Primitive two-square theorem

若

\[
p\equiv3\pmod4
\]

且

\[
p\mid x^2+y^2,
\]

则：

\[
x^2\equiv-y^2\pmod p.
\]

若 \(p\nmid y\)，则

\[
(xy^{-1})^2\equiv-1\pmod p,
\]

与 \(-1\) 在 \(p\equiv3\pmod4\) 时非二次剩余矛盾。

故：

\[
p\mid y.
\]

再代回得 \(p\mid x\)。

所以：

\[
\boxed{
p\mid x^2+y^2
\Longrightarrow
p\mid x,\ p\mid y.
}
\]

递归除去 \(p^2\) 得：

\[
\boxed{
v_p(x^2+y^2)=2\min(v_p(x),v_p(y)).
}
\tag{2SQ}
\]

---

## 12.2 应用于 prefix norm

取

\[
X=a_1b_2,\qquad Y=a_2b_1.
\]

逐项既约性给出：

\[
\gcd(X,Y)
=
\gcd(a_1,a_2)\gcd(b_1,b_2).
\]

令 \(c_N=\gcd(X,Y)\)，则

\[
N=c_N^2N_0,
\qquad
N_0=x_0^2+y_0^2,
\quad
\gcd(x_0,y_0)=1.
\]

因此：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
p\nmid N_0.
}
\]

---

## 12.3 Norm-rigid squareclass transfer to word gaps

由 (SC)：

\[
(c_N\eta\bar v\tau)^2N_0
=
(Gc_ac_\tau)^2Z_-Z_+.
\]

所以 odd inert prime 在 \(Z_-Z_+\) 中总指数为偶数。

又因

\[
\gcd(Z_-,Z_+)\mid2,
\]

odd \(p\) 只能进入一侧。

所以：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
v_p(Z_-)\equiv
v_p(Z_+)\equiv0\pmod2.
}
\]

---

## 12.4 Exact inert-prime ledger

写

\[
v_p(Z_-)=2r_-,
\qquad
v_p(Z_+)=2r_+.
\]

对 \(p\equiv3\pmod4\)，(L3) 除以 \(2\) 得：

\[
\boxed{
v_p(c_N)
+v_p(\eta)
+v_p(\bar v)
+v_p(\tau)
=
v_p(G)
+v_p(c_a)
+v_p(c_\tau)
+r_-+r_+.
}
\tag{IR-L}
\]

这是一个真正的 integer mass conservation。

但它本身没有不等式方向。

因此：

\[
\boxed{
p\equiv3\pmod4
\text{ 提供 parity / source rigidity，}
\text{尚未提供 forced depth。}
}
\]

---

## 12.5 当前裁决

相比 \(5\)-adic residual phase：

- inert primes 的 theorem 更“硬”；
- 但没有由 decimal \(S\) 自动强迫一个 growing exponent；
- denominator word 中出现 inert prime 也不自动意味着 contradiction，因为它可进入 square content / \(Z_\pm\) 的偶次幂。

所以当前优先级：

\[
\boxed{
5\text{-adic phase}
>
(3\bmod4)\text{ parity}
}
\]

作为直接 closure 候选。

但在 saturated / no-residual-\(5\) branch 中，inert-prime squareclass 可能重新成为主力。

---

# 13. \(p\equiv1\pmod4\) / Gaussian branch

## 13.1 旧 Gaussian route 为什么失败

旧 Gaussian flip / descent 的主要问题不是“Gaussian integers 无信息”，而是：

\[
\boxed{
\text{generic representation move 不保持 actual decimal coefficient plane / cut.}
}
\]

所以统计

\[
r_2(N)
\]

或对 \(X+iY\) 做任意 conjugation / factor swap 不能代表 original candidate symmetry。

---

## 13.2 新表示中 Gaussian information 可以合法复活

本轮不对 generic \(N\) representation 操作。

而是直接作用于由 original candidate 唯一决定的：

\[
\boxed{Z_-,Z_+.}
\]

已经证明它们：

- 正；
- source-labelled；
- gcd at odd primes disjoint；
- 每个 \(3\bmod4\) prime exponent even；
- 因而各自是二平方和。

所以 Gaussian machinery 若以后使用，应作用于：

\[
\boxed{
Z_-=N(\alpha_-),
\qquad
Z_+=N(\alpha_+)
}
\]

并始终保留：

\[
Z_\pm=bx\pm ay
\]

这一 decimal coefficient plane。

这属于：

\[
\boxed{
\text{FAILURE OF PREVIOUS REPRESENTATION, not fundamental uselessness.}
}
\]

---

## 13.3 但 \(1\bmod4\) prime allocation 仍然高度自由

对

\[
p\equiv1\pmod4
\]

没有 inert parity obstruction。

而 \(p=5\) 本身就是 split prime。

显式 pseudo-family：

\[
Z_-=50k^2,
\qquad
Z_+=50k^2+2
\]

已经允许 \(5\)-adic depth在 minus side 任意增长，同时 \(Z_+\) 保持合法 sum-of-two-squares。

所以：

\[
\boxed{
\text{Gaussian compatibility alone cannot close A1.}
}
\]

下一次若复活 Gaussian，必须与 actual cut / multiplier \(W\) 同步。

---

# 14. Denominator-word support forcing

## 14.1 Raw support lemma

若 \(p\mid\mathbf B\)，则：

\[
U_\pm
=
b_3\mathbf A\pm a_3\mathbf B
\equiv
b_3\mathbf A
\pmod p.
\]

若

\[
p\nmid b_3\mathbf A,
\]

则

\[
p\nmid U_-U_+.
\]

由 raw WGF：

\[
v_p(N)+2v_p(\mathbf B)+2v_p(b_3)
=
2v_p(G).
\]

此时 \(p\nmid b_3\)，所以：

\[
\boxed{
v_p(G)
=
v_p(\mathbf B)+\frac12v_p(N)
\ge v_p(\mathbf B).
}
\]

故 contrapositive：

\[
\boxed{
v_p(\mathbf B)>v_p(G)
\Longrightarrow
p\mid b_3\mathbf A.
}
\tag{DW-raw}
\]

用户提出的这一方向是正确的。

---

## 14.2 但 canonical exact-balance forcing 更干净

定义

\[
E=\frac{\mathbf B}{\gcd(\mathbf B,\Lambda)}.
\]

已有 theorem：

\[
\boxed{E\mid\mathbf A.}
\]

primewise：

\[
\boxed{
\max\bigl(
0,\,
v_p(\mathbf B)-v_p(\Lambda)
\bigr)
\le
v_p(\mathbf A).
}
\tag{DW}
\]

这比 (DW-raw) 更内在，因为它直接识别 denominator word 中“超过 canonical denominator”的 excess content。

---

## 14.3 Decimal primes 给出真正 T-only filter

strict foundation 还给出：

\[
\gcd(\mathbf A,\mathbf B,10)=1
\]

等价地 global word gcd prime-to-\(10\)。

由于 \(E\mid\gcd(\mathbf A,\mathbf B)\)：

\[
\boxed{\gcd(E,10)=1.}
\tag{E10}
\]

所以任何 trace 若满足：

\[
v_2(\mathbf B)>v_2(\Lambda)
\]

或

\[
v_5(\mathbf B)>v_5(\Lambda),
\]

立即不可 lift。

这是一个真正的:

\[
\boxed{
\textbf{Denominator Word Decimal-Prime Forcing Lemma}.
}
\]

它是 fixed-\(T\) filter，不使用 moving height。

**状态：REINTERPRETED EXISTING GLOBAL-GCD RESULT + NEW A1 PLACEMENT.**

---

## 14.4 非十进制 prime 不会自动传播到 blocks

不能从

\[
p\mid\mathbf A,\mathbf B
\]

推出任何：

\[
p\mid a_i,b_i.
\]

最简单的 ambient counterexample：

\[
\mathbf B=111,
\qquad
\mathbf A=1221.
\]

则

\[
3\mid\mathbf A,\mathbf B,
\]

但 block decomposition

\[
(1,22,1),
\qquad
(1,1,1)
\]

中没有 matched block 被 \(3\) 整除。

所以：

\[
\boxed{
\text{non-decimal word primes are carry/cyclotomic objects,}
}
\]

不能用“word gcd \(\Rightarrow\) block gcd”短路 reducedness。

---

## 14.5 最终裁决

完整 \(\mathbf B\) 的 prime-square supply **确实有 forcing**，但其强度必须分成两层：

1. excess word content \(E\) 被 exact balance 强制进入 \(\mathbf A\)；
2. 在 WGF 中该 \(E^2\) 又完全消掉。

因此 raw “\(\mathbf B^2\) 太大，gap factors 无法供给”的路线：

\[
\boxed{\textbf{FAILED IN RAW FORM}.}
\]

真正剩下的是：

\[
\Gamma,\quad
\eta,\quad
v,\quad
c_a,c_\tau,\quad
Z_\pm
\]

之间的兼容供给。

---

# 15. Determinant / lattice interpretation of the word gap

primitive word gap：

\[
J_-=b_3u-a_3v
=
S\varepsilon.
\]

可写成：

\[
\boxed{
J_-
=
\det
\begin{pmatrix}
u&a_3\\
v&b_3
\end{pmatrix}.
}
\]

因此：

\[
\frac uv-\frac{a_3}{b_3}
=
\frac{S\varepsilon}{vb_3}.
\]

两个向量：

\[
(u,v),
\qquad
(a_3,b_3)
\]

分别 primitive。

矩阵的 Smith first invariant 为 \(1\)，second invariant 为：

\[
\boxed{S\varepsilon.}
\]

所以它们生成的子格 index 正是 \(S\varepsilon\)。

这是一个很自然的几何解释：

\[
\boxed{
\text{A1 要求两个 primitive rational slopes 的 lattice index}
\text{ 是 }10^{n_3}\text{ 的正倍数。}
}
\]

但 primitive 性本身完全不限制 determinant 的大小或 prime support。

因此：

\[
\boxed{
\text{Farey / primitive lattice alone cannot close A1.}
}
\]

要利用 determinant，必须同时读：

- norm；
- word multiplier；
- actual cut；
- reducedness。

**状态：NEW INTERPRETATION / DIRECT DETERMINANT-ONLY ROUTE FAILED.**

---

# 16. Reducedness as source information

本轮最明确的结论之一是：

\[
\boxed{
\gcd(a_i,b_i)=1
\text{ 绝不是末端 checkbox。}
}
\]

它在三处直接进入核心算术。

## 16.1 第三块 reducedness

\[
\gcd(a_3,b_3)=1
\]

负责：

1. 从 \(\eta\mid b_3\) 推出 \(\gcd(a_3,\eta)=1\)；
2. 由 \(J_-=S\varepsilon\) 推出 \(\eta\mid v\)；
3. 支撑 \(c_a,c_\tau\) cross-content 分解；
4. 删除很多 simultaneous gap primes。

---

## 16.2 前两块 reducedness

\[
\gcd(a_1,b_1)=
\gcd(a_2,b_2)=1
\]

负责 prefix norm content theorem：

\[
\gcd(a_1b_2,a_2b_1)
=
\gcd(a_1,a_2)\gcd(b_1,b_2).
\]

从而得到 primitive \(N_0\) 与 inert-prime rigidity。

---

## 16.3 Global word reducedness consequence

已有 strict foundation：

\[
\boxed{
\gcd(\mathbf A,\mathbf B)\text{ is prime-to-}10.
}
\]

在当前坐标中：

\[
\gcd(\mathbf A,\mathbf B)=Eh,
\]

所以：

\[
\boxed{
\gcd(Eh,10)=1.
}
\]

这把 global word common content 的 decimal-prime escape 彻底删除。

---

## 16.4 一个 exact raw A1 word state 只因 reducedness 失败

显式例：

\[
(a_1,b_1,a_2,b_2,a_3,b_3)
=
(7,3,92,4,3,2).
\]

完整 words：

\[
\mathbf A=7923,
\qquad
\mathbf B=342.
\]

并且精确满足：

\[
\left(\frac{7923}{342}\right)^2
=
\left(\frac73\right)^2
+
\left(\frac{92}{4}\right)^2
+
\left(\frac32\right)^2.
\]

位数：

\[
n_3=m_3=1,\quad
n_2=2,\quad
m_2=1,
\]

所以

\[
g=0,\qquad
k_{12}=1.
\]

唯一问题是：

\[
\gcd(92,4)=4.
\]

另外两块 reduced。

因此：

\[
\boxed{
\text{reducedness 可以是一个 raw exact A1 word state 的唯一死亡原因。}
}
\]

**状态：NEW COMPUTATION-VERIFIED EXPLICIT COUNTEREXAMPLE TO “REDUCEDNESS IS ONLY A FINAL CHECK”.**

---

# 17. A1-specific decimal-cut interaction

## 17.1 Adjacent-cut difference

若：

\[
q_n=10q_{n+1}+d,
\qquad
r_{n+1}=d10^n+r_n,
\]

其中 \(d\in\{1,\dots,9\}\)，则：

\[
F_n=b_2^2q_n^2+b_1^2r_n^2.
\]

直接展开得：

\[
\boxed{
\begin{aligned}
F_{n+1}-F_n
={}&
b_1^2
\left(
d^2 10^{2n}
+2d10^nr_n
\right)
\\
&-
b_2^2
\left(
99q_{n+1}^2
+20dq_{n+1}
+d^2
\right).
\end{aligned}
}
\tag{CUT-D}
\]

A1 legal region：

\[
n\ge m_2+g+1
\]

本身没有固定该式符号。

---

## 17.2 A1 threshold 不能杀死 double cuts

已有 prefix-local infinite family：

\[
b_1=b_2=1,
\]

\[
R_k=\underbrace{11\cdots1}_{k\text{ digits}},
\]

\[
P=R_{p+q}.
\]

cut \(p\) 与 cut \(q\) 分别给出：

\[
(R_q,R_p),
\qquad
(R_p,R_q),
\]

且：

\[
F_p=F_q=R_p^2+R_q^2.
\]

只要把 \(p,q\) 都取到任意预设 threshold 以上，就同时满足：

\[
p,q\ge m_2+g+1.
\]

因此：

\[
\boxed{
\text{A1 legal-cut lower bound 本身不产生 uniqueness 或 sign theorem。}
}
\]

---

## 17.3 本轮裁决

不再花 token 证明：

\[
\text{legal cut }\le1.
\]

真正需要的是：

\[
\boxed{
\text{actual cut 如何与 oriented deflated gap phase 同步。}
}
\]

也就是说 cut 不是 fibre-count 问题，而是 arithmetic attachment 问题。

---

# 18. Synchronization / MUS interpretation

fixed \(T\) 后定义三个 concrete relations。

## 18.1 \(R_{\rm word}\)

变量：

\[
(W,n).
\]

要求：

\[
\mathbf A=EW,
\]

\[
a_3=\mathbf A\bmod S,
\qquad
P=\lfloor\mathbf A/S\rfloor,
\]

\[
a_1=\lfloor P/10^n\rfloor,
\qquad
a_2=P\bmod10^n,
\]

真实 digit windows，且：

\[
n\ge m_2+g+1.
\]

---

## 18.2 \(R_{\rm norm}\)

同一个 cut 必须满足：

\[
F_n\Gamma^2b_3^2
=
G^2K_-K_+,
\]

等价于 DG-N。

---

## 18.3 \(R_{\rm red}\)

\[
\gcd(a_1,b_1)=
\gcd(a_2,b_2)=
\gcd(a_3,b_3)=1.
\]

---

## 18.4 Exact A1 terminal join

在 frozen A1 semantics 下：

\[
\boxed{
\text{Complete A1 candidate}
\iff
R_{\rm word}
\Join
R_{\rm norm}
\Join
R_{\rm red}
\ne\varnothing.
}
\tag{JOIN}
\]

T-only denominator / tail admissibility可以作为进入该 join 前的 prefilter。

root quadratics / discriminants / resultants 是该 exact join 的 projections / elimination shadows。

---

## 18.5 三个 relation 都不能轻易删除

本轮给出三类独立压力测试：

### \(R_{\rm word}+R_{\rm red}\) 不推出 \(R_{\rm norm}\)

例：

\[
b_1=b_2=b_3=2,
\qquad
\mathbf B=222,
\]

\[
\Lambda=2,
\quad
\Gamma=2,
\quad
E=111.
\]

取

\[
W=29,
\qquad
\mathbf A=3219.
\]

则：

\[
P=321,
\quad
a_3=9.
\]

cut \(n=2\)：

\[
(a_1,a_2,a_3)=(3,21,9),
\]

三块都与 denominator \(2\) 既约，A1 cut legal。

exact balance：

\[
\Lambda\mathbf A=29\mathbf B.
\]

但：

\[
\left(\frac{\mathbf A}{\mathbf B}\right)^2
=210.25,
\]

而三项平方和为：

\[
132.75.
\]

所以 norm 失败。

---

### \(R_{\rm norm}+R_{\rm red}\) 即使加 global balance/tail 也不推出 \(R_{\rm word}\)

第 19 节的无限 detached-prefix pseudo-family给出。

---

### \(R_{\rm word}+R_{\rm norm}\) 不推出 \(R_{\rm red}\)

例：

\[
(7/3,\ 92/4,\ 3/2)
\]

精确满足完整 word equation，但第二块不既约。

所以 reducedness 不能删除。

---

## 18.6 当前 MUS verdict

尚未证明：

\[
R_{\rm word}
\Join
R_{\rm norm}
\Join
R_{\rm red}
=
\varnothing,
\]

因此不能称其为 formal minimal unsatisfiable subsystem。

但可以严格称为：

\[
\boxed{
\textbf{three-relation exact synchronization core with pairwise nonredundancy witnesses.}
}
\]

---

# 19. Computational stress tests

本轮计算只用于验证显式 identity、寻找反例，不用于 nonexistence proof。

## 19.1 bounded raw A1 scan

扫描：

\[
1\le b_1,b_2,b_3\le9,
\]

\[
1\le a_1,a_3\le9,
\qquad
10\le a_2\le99,
\]

即：

\[
n_3=m_3=1,
\quad
n_2=2,
\quad
m_2=1,
\quad
g=0,
\quad
k_{12}=1.
\]

要求 raw exact word equation，但暂不要求 reducedness。

找到恰好三个 states：

\[
(1,1,72,9,8,2),
\]

\[
(7,3,92,4,3,2),
\]

\[
(7,6,92,8,3,4).
\]

全部至少有一个 reducedness failure。

在该小盒子里 fully reduced exact candidate 数为：

\[
0.
\]

**状态：COMPUTATIONAL EVIDENCE ONLY.**

本报告不把“0”外推成 theorem。

---

## 19.2 Infinite detached-prefix pseudo-family

取：

\[
b_1=b_2=b_3=1,
\qquad
\mathbf B=111,
\qquad
\Lambda=1.
\]

对每个 \(k\ge1\)：

\[
a_1=10k,\qquad
a_2=50k^2,\qquad
a_3=1,
\]

\[
t=50k^2+1.
\]

有：

\[
(10k)^2+(50k^2)^2+1
=
(50k^2+1)^2.
\]

令：

\[
\mathbf A^*=111t.
\]

则：

\[
\frac{\mathbf A^*}{111}=t,
\qquad
\mathbf A^*\equiv1\pmod{10}.
\]

prefix norm：

\[
N=(10k)^2+(50k^2)^2=t^2-1.
\]

primitive gap：

\[
J_-=t-1=50k^2=10(5k^2),
\]

\[
J_+=t+1=50k^2+2.
\]

tail normalization：

\[
\eta=1,\quad
\mathcal L=10,\quad
\tau=1.
\]

denominator-side：

\[
Q=11,\quad
D=11,\quad
G=1,
\]

\[
\kappa=110.
\]

tail certificate：

\[
10\mid110^2\cdot112.
\]

normalized gaps：

\[
Z_-=50k^2,
\qquad
Z_+=50k^2+2,
\]

且：

\[
\gcd(Z_-,Z_+)=2.
\]

Gaussian realizations：

\[
Z_-=(5k)^2+(5k)^2,
\]

\[
Z_+=(5k-1)^2+(5k+1)^2.
\]

唯一 systematic failure：

\[
P^*
=
\frac{111t-1}{10}
=
555k^2+11
\]

不是

\[
10k\cdot10^{\ell(50k^2)}+50k^2.
\]

这是一条非常强的 representation-failure certificate：

\[
\boxed{
\text{prime/gcd/Gaussian/tail/norm 全部可以长期同步，}
\text{而 actual decimal cut 仍然失败。}
}
\]

---

# 20. Counterexamples and failed conjectures

## C1. “WGF 本身就是新 obstruction”

**DISPROVED / REINTERPRETED.**

它与 A1-WR 等价。

真正新的是 exact-balance cancellation 后的 BR-WGF。

---

## C2. “\(\mathbf B^2\) 的巨大 square supply 会自动 overload gaps”

**FAILED IN RAW FORM.**

\(E^2\) 是强制 common word content，精确从两边消掉。

---

## C3. “\(\gcd(U_-,U_+)\) 应该很小”

**DISPROVED structurally.**

raw gcd 至少可含：

\[
E h\eta c_ac_\tau.
\]

真正 small 的只有 normalized：

\[
\gcd(Z_-,Z_+)\mid2.
\]

---

## C4. “primitive determinant 大 \(10\)-power 与 primitive vectors 不相容”

**FALSE.**

primitive \(2\times2\) determinant 可任意大。

primitive lattice/SNF 只解释 index，不提供 upper bound。

---

## C5. “\(p\equiv3\bmod4\) 在 \(N\) 中指数偶，所以 contradiction”

**FALSE.**

正确结论只是 normalized gaps 的 inert exponents individually even。

供给仍可由 squares 完全满足。

---

## C6. “Gaussian representation count 控制 complete fibre”

**FALSE / OLD FAILURE.**

complete fibre \(\le2\) 来自 decimal cuts，不来自 \(r_2(N)\)。

---

## C7. “Gaussian 永远无用”

**TOO STRONG; REPAIRED.**

Gaussian descent 不保持 decimal plane，但对 source-labelled \(Z_\pm\) 的 local norm structure 可以合法使用。

---

## C8. “A1 legal threshold 会消灭 prefix twins”

**FALSE.**

repunit twin family可把两个 cuts 同时放到任意 threshold 以上。

---

## C9. “word common prime 会向 blocks 传播”

**FALSE.**

\[
3\mid111,\ 1221
\]

但对应 blocks 不必逐块含 \(3\)。

---

## C10. “\(5\)-adic residual depth 单独即可矛盾”

**FALSE AS A STANDALONE ROUTE.**

detached-prefix pseudo-family中：

\[
v_5(Z_-)
\]

可任意增长，同时 norm、tail、Gaussian、reducedness 全部兼容。

所以必须接 actual cut。

---

# 21. Best surviving obstruction language

本轮最终不选择：

- raw WGF；
- generic prime graph；
- generic Gaussian representation；
- pure determinant；
- pure valuation；
- cut convexity

作为主语言。

推荐长期使用以下两层。

## 21.1 Exact semantic layer

\[
\boxed{
(T,W,n).
}
\]

其中：

\[
\mathbf A=EW,
\qquad
\mathbf B=E\Gamma.
\]

这层负责：

- multiplication / carry；
- actual full word；
- actual cut；
- digit windows；
- exact block identity。

---

## 21.2 Deflated arithmetic layer

\[
\boxed{
(u,\bar v,a_3;\eta,\tau,\mathcal L).
}
\]

核心 equation：

\[
\boxed{
\tau u-a_3\bar v
=
\mathcal L\varepsilon>0,
}
\]

\[
\boxed{
N\eta^2\bar v^2\tau^2
=
G^2
(\tau u-a_3\bar v)
(\tau u+a_3\bar v).
}
\]

再抽 cross-content：

\[
\boxed{
c_ac_\tau Z_-=\mathcal L\varepsilon,
\qquad
\gcd(Z_-,Z_+)\mid2.
}
\]

这层负责：

- oriented prime allocation；
- \(2/5\)-phase；
- inert-prime squareclass；
- Gaussian ideals；
- determinant / lattice。

---

## 21.3 两层之间唯一不能忘的桥

primitive reduction：

\[
W=hu,\qquad
\Gamma=h\eta\bar v.
\]

但 actual word 仍必须满足：

\[
\boxed{
EW
=
S(a_1 10^n+a_2)+a_3.
}
\]

所以：

\[
\boxed{
\textbf{任何 arithmetic obstruction 若不把 }h,u
\textbf{重新乘回同一个 decimal word/cut，就可能被 pseudo-family 击穿。}
}
\]

这就是本轮找到的最关键 architecture principle。

---

# 22. New theorem(s)

本轮建议正式记录以下 theorem / lemma。

## A1-BR1 — Exact Word-Quotient Normal Form

fixed \(T\) 后，令

\[
\Gamma=\gcd(\mathbf B,\Lambda),
\qquad
E=\mathbf B/\Gamma.
\]

完整 candidate 必有 \(E\mid\mathbf A\)。

令 \(W=\mathbf A/E\)，则 complete A1 recovery 等价于在 \((T,W,n)\) 上满足 digit/A1/reducedness 与 BR-WGF。

**状态：NEW NORMAL-FORM THEOREM，核心 divisibility 为 REINTERPRETED EXISTING RESULT。**

---

## A1-BR2 — Balance-Cancelled WGF

\[
\boxed{
N\Gamma^2b_3^2
=
G^2
(b_3W-a_3\Gamma)
(b_3W+a_3\Gamma).
}
\]

并且

\[
\boxed{
b_3W-a_3\Gamma
=
S(\Gamma P-DW)>0.
}
\]

**状态：NEW PROVED.**

---

## A1-BR3 — Primitive Oriented Decimal Determinant

令

\[
W=hu,\quad \Gamma=hv,\quad \gcd(u,v)=1.
\]

则：

\[
\boxed{
b_3u-a_3v
=
S(vP-Du)>0.
}
\]

**状态：NEW PROVED.**

---

## A1-BR4 — Tail-Deflated Gap

令

\[
S=\eta\mathcal L,
\quad
b_3=\eta\tau.
\]

则：

\[
\eta\mid v.
\]

写 \(v=\eta\bar v\)，有：

\[
\boxed{
\tau u-a_3\bar v
=
\mathcal L(vP-Du)>0.
}
\]

**状态：NEW PROVED.**

---

## A1-BR5 — Cross-Content Coprime Gap Pair

定义：

\[
c_a=\gcd(a_3,u),
\qquad
c_\tau=\gcd(\tau,\bar v).
\]

则存在正整数 \(Z_\pm\) 满足：

\[
\tau u\mp a_3\bar v
=
c_ac_\tau Z_\mp,
\]

且：

\[
\boxed{
\gcd(Z_-,Z_+)\mid2.
}
\]

**状态：NEW PROVED.**

---

## A1-BR6 — Prefix Norm Content Theorem

\[
\boxed{
\gcd(a_1b_2,a_2b_1)
=
\gcd(a_1,a_2)\gcd(b_1,b_2).
}
\]

因此：

\[
N=c_N^2N_0,
\]

其中 \(N_0\) 是 primitive sum of two squares。

**状态：NEW PROVED.**

---

## A1-BR7 — Source-Labelled Gaussian Gap Theorem

normalized \(Z_\pm\) 满足：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
v_p(Z_\pm)\text{ even}.
}
\]

故：

\[
\boxed{
Z_\pm
\text{ each are sums of two squares}.
}
\]

**状态：NEW PROVED.**

---

## A1-BR8 — Residual Decimal-Prime Allocation

\[
c_ac_\tau Z_-=\mathcal L\varepsilon,
\qquad
\gcd(c_\tau,\mathcal L)=1.
\]

所以对 \(p=2,5\)：

\[
v_p(c_a)+v_p(Z_-)
=
v_p(\mathcal L)+v_p(\varepsilon).
\]

若

\[
0<v_p(b_3)<n_3,
\]

则 \(v_p(c_a)=0\)，故：

\[
v_p(Z_-)\ge n_3-v_p(b_3).
\]

对 \(p=5\)，同时：

\[
v_5(Z_+)=0.
\]

**状态：NEW PROVED.**

---

## A1-BR9 — Detached-Prefix Infinite Pseudo-Family

第 19 节 family 证明：

\[
\boxed{
\text{若删除 actual first-two word attachment，}
}
\]

则 norm + reducedness + global balance + tail certificate + oriented gap + Gaussian compatibility 仍有无限 compatible family。

**状态：NEW PROVED NEGATIVE THEOREM.**

---

# 23. Exact remaining proof obligation

本轮没有得到 pure recovery contradiction。

当前最小、最硬的 terminal theorem 可以写成：

## Backward A1 Cut–Gap Synchronization Theorem — A1-CGS

固定任意 A1 denominator–decimal trace

\[
T=(b_1,b_2,b_3,S)
\]

并定义：

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\qquad
D=10^gQ,
\]

\[
\mathbf B=SD+b_3,
\qquad
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\]

\[
\Gamma=\gcd(\mathbf B,\Lambda),
\qquad
E=\mathbf B/\Gamma.
\]

证明不存在整数：

\[
W>0,\qquad
n\ge m_2+g+1
\]

使得令：

\[
\mathbf A=EW,
\]

\[
a_3=\mathbf A\bmod S,
\qquad
P=\lfloor\mathbf A/S\rfloor,
\]

\[
a_1=\lfloor P/10^n\rfloor,
\qquad
a_2=P\bmod10^n,
\]

后同时满足：

1. 三个 numerator blocks 为真实 positive digit blocks；
2.
   \[
   \gcd(a_i,b_i)=1
   \quad(i=1,2,3);
   \]
3.
   \[
   k_{12}=n-m_2-g\ge1;
   \]
4. exact balance-cancelled word-gap equation
   \[
   \boxed{
   (b_2^2a_1^2+b_1^2a_2^2)\Gamma^2b_3^2
   =
   G^2
   (b_3W-a_3\Gamma)
   (b_3W+a_3\Gamma).
   }
   \tag{CGS}
   \]

等价地，在 primitive tail-deflated variables 中：

\[
\boxed{
\tau u-a_3\bar v
=
\mathcal L\varepsilon>0
}
\]

与 normalized prime/Gaussian constraints 必须由**同一个 actual decimal cut**实现。

若 A1-CGS 证明，则：

\[
\boxed{A_1=\varnothing}
\]

且 Strict Layer 完全闭合。

**当前状态：OPEN.**

这不是“继续研究 prime support”的宽泛目标，而是一个单一、精确、height-free 的 exact arithmetic theorem。

---

# 24. Next-round targets — at most three

## Target 1 — Residual \(5\)-Phase × Actual Cut

只研究：

\[
v_5(\mathcal L)>0.
\]

利用：

\[
c_ac_\tau Z_-=\mathcal L\varepsilon,
\qquad
\gcd(Z_-,Z_+)\mid2,
\]

把 one-sided \(5\)-adic depth真正传回：

\[
EW=S(a_1 10^n+a_2)+a_3.
\]

目标不是再证明一个 valuation capacity，而是得到一个 cut-preserving congruence：

\[
\boxed{
P=a_1 10^n+a_2
\quad\text{与}\quad
\tau u-a_3\bar v\equiv0\pmod{5^r}
}
\]

无法由同一个 \(W\) 同时实现。

优先研究 partial-saturation：

\[
0<v_5(b_3)<n_3,
\]

因为此时 \(c_a\) 不能吸收 residual \(5\)-depth。

---

## Target 2 — Full Decimal-Content Absorption Locus

研究 residual \(5\)-phase 消失或被 cross numerator content 吸收的 states：

\[
v_5(\mathcal L)=0
\]

或

\[
v_5(c_a)\ge v_5(\mathcal L).
\]

特别包括 saturated：

\[
\mathcal L=1.
\]

这里 pure \(5\)-adic phase不能工作。

应利用：

- \(c_a=\gcd(a_3,u)\) 大；
- global word multiplier \(W=hu\)；
- actual tail digit；
- prefix cut reducedness；
- inert-prime / Gaussian squareclass

寻找另一种 source synchronization。

---

## Target 3 — Source-Labelled Gaussian / Squareclass × Cut Multiplier

只对：

\[
Z_-,Z_+
\]

做 Gaussian factorization，不再对 generic \(N\) 做 representation counting。

利用：

\[
Z_\pm=N(\alpha_\pm),
\qquad
\gcd(Z_-,Z_+)\mid2,
\]

\[
[Z_-Z_+]=[N_0],
\]

再把 factor allocation 回接：

\[
W=hu
\]

与：

\[
P=\lfloor EW/S\rfloor.
\]

目标是证明 actual decimal cut 无法支持所需的 \(1\bmod4\) prime orientation，或者构造新的无限 pseudo-family从而彻底判死 Gaussian route。

---

# 25. Final Q1–Q7 + PROVED / HEURISTIC / FAILED / OPEN ledger

## Q1 — A1 exact recovery 最自然的 backward normal form 是什么？

\[
\boxed{
\textbf{Exact semantic: }(T,W,n).
}
\]

其中：

\[
W=\mathbf A/
\left(
\mathbf B/\gcd(\mathbf B,\Lambda)
\right).
\]

其 arithmetic projection 是：

\[
\boxed{
\tau u-a_3\bar v
=
\mathcal L\varepsilon>0,
}
\]

\[
\boxed{
N\eta^2\bar v^2\tau^2
=
G^2
(\tau u-a_3\bar v)
(\tau u+a_3\bar v).
}
\]

因此最自然的对象不是单纯 norm representation，也不是单纯 prime graph，而是：

\[
\boxed{
\textbf{a decimal-cut constrained primitive slope determinant / norm factorization.}
}
\]

---

## Q2 — WGF 是否比 A1-WR 真正增加结构？

逻辑上：

\[
\boxed{\text{NO}.}
\]

WGF 与 A1-WR 等价。

但 exact balance normalization 后：

\[
\boxed{\text{YES as a better normal form}.}
\]

它暴露：

- \(E^2\) forced word content cancellation；
- oriented minus gap；
- primitive determinant；
- tail-deflated modulus \(\mathcal L\)；
- near-coprime normalized factors。

---

## Q3 — denominator word \(\mathbf B\) 的 prime-square supply 是否产生真正 forcing？

\[
\boxed{\text{YES, but much less than raw WGF suggests}.}
\]

真正 theorem 是：

\[
E=\mathbf B/\gcd(\mathbf B,\Lambda)\mid\mathbf A.
\]

对 \(p=2,5\)：

\[
\gcd(E,10)=1
\]

给出 T-only death filter。

但在 WGF 中 \(E^2\) 精确消掉，所以：

\[
\boxed{
\text{raw }\mathbf B^2\text{ overload is not a valid closure mechanism}.
}
\]

真正 residual supply 位于：

\[
\Gamma,\eta,\bar v,\tau,c_a,c_\tau,Z_\pm.
\]

---

## Q4 — \(2,5\) 与 \(p\equiv3\bmod4\) 谁更有希望 decisive？

当前排序：

\[
\boxed{
5\text{-adic residual phase}
>
3\bmod4\text{ norm rigidity}
>
2\text{-adic phase}.
}
\]

理由：

- \(5\) 有 \(\mathcal L\mid H_-\) 的 forced depth，并且 normalized plus factor不能共享 \(5\)；
- \(3\bmod4\) 给出很强的 even-exponent / sum-of-two-squares rigidity，但没有自动 growing depth；
- \(2\) 有额外 common factor \(2\) 与 parity complication。

但 saturated / absorbed branch 会让 \(5\)-route失去 modulus，所以最终可能需要 branch-adaptive combination。

---

## Q5 — individual reducedness 是末端检查还是核心 obstruction？

\[
\boxed{\textbf{CORE SOURCE INFORMATION}.}
\]

它负责：

- tail deflation；
- cross-content gcd theorem；
- prefix norm primitive content；
- inert-prime rigidity；
- global decimal-prime exclusion。

显式 raw exact A1 state：

\[
(7/3,\ 92/4,\ 3/2)
\]

只因一个 reducedness 条件失败，进一步说明它可以成为唯一死亡原因。

---

## Q6 — 是否出现不依赖 moving-core height 的纯 recovery contradiction？

\[
\boxed{\textbf{NO.}}
\]

本轮所有新 theorem 都 height-free，但它们尚未合成 contradiction。

得到的是 canonical architecture + strong negative route eliminations，而不是 closure。

---

## Q7 — 当前最小、最硬的 backward proof obligation 是什么？

\[
\boxed{
\textbf{A1-CGS — Backward A1 Cut–Gap Synchronization Theorem}.
}
\]

即第 23 节的 single exact theorem：

> 不存在同一个 \(W\) 与 A1-legal cut \(n\)，同时实现真实 decimal word、逐块 reducedness 与 balance-cancelled oriented norm factorization。

---

## PROVED / DERIVED / REINTERPRETED

- DD 已闭合，Strict frontier 仅 A1；
- fixed \(T\) denominator trace；
- A1-WR；
- fixed \((T,\mathbf A)\) cut fibre \(\le2\)；
- Twin-Lift；
- canonical exact balance；
- \(E\mid\mathbf A\)；
- global word gcd prime-to-\(10\)；
- tail normalization；
- tail certificate；
- BR-WGF；
- primitive oriented gap；
- tail-deflated gap；
- cross-content gcd \(\le2\)；
- prefix norm content theorem；
- source-labelled Gaussian gap theorem；
- residual decimal-prime allocation；
- A1-CGS exact normal form equivalence。

---

## COMPUTATIONAL EVIDENCE

有限 box：

\[
b_i\le9,\quad
a_1,a_3\le9,\quad
10\le a_2\le99
\]

中 raw exact A1 states 共发现 \(3\) 个，全部 reducedness failure；fully reduced 为 \(0\)。

不作全局外推。

---

## PROVED AMBIENT COUNTEREXAMPLES / NEGATIVE RESULTS

- raw \(\mathbf B^2\) supply overcounts \(E^2\)；
- repunit twin cuts survive arbitrary A1 cut thresholds；
- nondecimal word primes不向 blocks 自动传播；
- determinant primitive性不限制 \(S\varepsilon\)；
- standalone inert-prime parity不矛盾；
- Gaussian compatibility不矛盾；
- residual \(5\)-depth不矛盾；
- infinite detached-prefix pseudo-family证明 actual cut 不可删除。

---

## FAILED

- WGF-alone obstruction；
- raw denominator square overload；
- \(\gcd(U_-,U_+)\) uniformly small；
- determinant-only / Farey-only closure；
- pure \(p\equiv3\bmod4\) parity closure；
- generic Gaussian descent；
- generic Gaussian representation count；
- A1 legal threshold \(\Rightarrow\) cut uniqueness；
- word-gcd \(\Rightarrow\) block-gcd；
- pure residual-\(5\) valuation closure；
- tail-certificate alone + word-gap alone closure。

---

## HEURISTIC / CONJECTURAL

- residual \(5\)-phase 与 actual cut 可能形成下一层 source congruence obstruction；
- saturated / absorption locus 可能需要 inert-prime squareclass 或 large cross-content；
- source-labelled Gaussian ideal allocation 只有在重新接入 \(W\) 与 cut 后才可能有终止力。

---

## OPEN

\[
\boxed{
\textbf{A1-CGS}.
}
\]

以及三个限定 next targets：

1. Residual \(5\)-Phase × Actual Cut；
2. Full Decimal-Content Absorption Locus；
3. Source-Labelled Gaussian / Squareclass × Cut Multiplier。

---

# Final campaign verdict

本轮达到的不是 A1 closure，而是：

\[
\boxed{
\textbf{Outcome A + Outcome B/E/F 的组合：}
}
\]

\[
\boxed{
\textbf{A canonical backward normal form}
+
\textbf{a genuine oriented prime-allocation structure}
+
\textbf{a sharp negative theorem showing why prime arithmetic without the cut cannot close.}
}
\]

A1 的反向问题现在最短地可以读成：

\[
\boxed{
\textbf{为什么一个 denominator-forced word multiplier }E
\textbf{、一个 primitive slope determinant }
\mathcal L\mid(\tau u-a_3\bar v)
}
\]

\[
\boxed{
\textbf{和一个真实 first-two decimal cut }
P=a_1 10^n+a_2
\textbf{ 无法由同一个 }W\textbf{ 同时实现？}
}
\]

这比继续分别追 quadratic / resultant / generic valuation / generic Gaussian representation 更接近真正的 exact-recovery bottleneck。
