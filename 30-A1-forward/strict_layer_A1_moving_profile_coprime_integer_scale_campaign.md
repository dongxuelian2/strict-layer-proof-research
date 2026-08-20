# 三项十进制拼接平方和问题：A1 Moving-Profile Coprime Integer-Scale — Long-Horizon Escape Elimination Campaign

**文件名：** `strict_layer_A1_moving_profile_coprime_integer_scale_campaign.md`  
**研究范围：** Strict Layer 正向线，仅研究 `A1-only`；DD 保持 closed。  
**本轮结论：**

\[
\boxed{
\textbf{A1 尚未闭合；但 moving-profile frontier 再次发生结构降维。}
}
\]

最重要的校准是：

\[
\boxed{
h:=Q_0-P_1
\textbf{ 不是 near-axis 小参数；真实 canonical gap 是 }
d_2:=Q_0-P_2.
}
\]

更强地，本轮得到：

\[
\boxed{
10^{-k}
<
\frac{P_1}{Q_0}
<
\left(1+\frac1{b_1}\right)10^{-k}
\le 2\cdot10^{-k},
}
\tag{MP-LEAD}
\]

所以 \(k\ge1\) 时恒有 \(P_1/Q_0<0.2\)。因此

\[
\boxed{
0.8<\frac{Q_0-P_1}{Q_0}<1
}
\]

而不是 \(Q_0-P_1=o(Q_0)\)。

与此同时，第二 primitive coordinate 被强制为真正的主轴：

\[
\boxed{
P_2>\sqrt{\frac{24}{2525}}\,Q_0>\frac{Q_0}{11}.
}
\tag{MP-P2}
\]

若 \(g\ge1\)，则进一步：

\[
\boxed{
P_2>\sqrt{\frac{96}{101}}\,Q_0>0.975\,Q_0.
}
\tag{MP-P2+}
\]

所以任何 \(Q_0\to\infty\) 的 genuine A1 family 都必须沿一个
**\(P_2\)-axis decimal sector** 逃逸，而不是沿 prompt 中预设的 \(P_1\)-axis near-axis sector。

本轮还建立：

\[
\boxed{
\frac{Q_0}{2\,10^{2k}}
<
d_2:=Q_0-P_2
<
\frac{Q_0}{10^{2k}}
\left[
\left(1+\frac1{b_1}\right)^2+10^{4-4g}
\right],
}
\tag{MP-D2}
\]

从而：

\[
\boxed{
10^{2k}<10004\,Q_0,
}
\tag{MP-K}
\]

且 \(g\ge1\) 时：

\[
\boxed{
10^{2k}<5Q_0.
}
\tag{MP-K+}
\]

这把 \(k\) 也压到平方根高度：

\[
\boxed{k\le \tfrac12\log_{10}Q_0+O(1).}
\]

另一方面，\(\lambda=U/V\) 的 reduction 成功把大量 gcd/profile notation 消成真实 radial ratio：

\[
\boxed{
\frac{a_i}{b_i}=\lambda P_i.
}
\]

A1 的第二、三块给出：

\[
\boxed{
10^{g+k-1}<\lambda P_2<10^{g+k+1},
}
\tag{DR2}
\]

\[
\boxed{
10^{-g-1}<\lambda P_3<10^{-g+1}.
}
\tag{DR3}
\]

故：

\[
\boxed{
10^{2g+k-2}
<
\frac{P_2}{P_3}
<
10^{2g+k+2},
}
\tag{RATIO}
\]

\[
\boxed{
10^{k-2}
<
\lambda^2P_2P_3
<
10^{k+2}.
}
\tag{PRODUCT}
\]

但 product law 在本轮被证明是一个**正确而不足的 conservation law**：代入 canonical \(P_2\)-axis sector 后，它与 sphere 完全相容，不产生 contradiction。

最终，moving-profile 的 exact nonflat balance 可压到一个新的 mantissa normal form。令

\[
\beta_i:=\frac{b_i}{10^{m_i}}\in[10^{-1},1),
\qquad
x:=\frac{P_2}{Q_0},
\qquad
y:=\frac{P_3}{Q_0},
\]

并定义 leading defect coordinate

\[
\boxed{
\varepsilon
:=
\frac{b_1(P_1 10^k-Q_0)}{Q_0}
\in(0,1).
}
\tag{EPS}
\]

则 exact GSYNC 等价推出：

\[
\boxed{
\varepsilon
=
\beta_2\left(1-\frac{x}{10^g}\right)
+
\beta_3\frac{1-y}{10^{m_2}}.
}
\tag{MB}
\]

或令

\[
d:=m_2-g,
\]

写成：

\[
\boxed{
10^g(\varepsilon-\beta_2)
=
-\beta_2x
+
\beta_3(1-y)10^{-d}.
}
\tag{MB-d}
\]

这把原先庞大的 moving gcd/exponent profile，至少在全局 size/sign 几何上压成：

\[
\boxed{
(P_1,P_2,P_3,Q_0)
+
(\lambda,g,k)
+
(\beta_2,\beta_3,\varepsilon,d),
}
\]

而 \(n_3\)、\(g_2/g_3\) 等大量 presentation variables 不再是 primitive escape geometry 的独立坐标。

本轮最终没有得到：

- \(g\) 的绝对界；
- eventual unique-\(U\)；
- tropical unique ray；
- A1 closure。

但是已经把真正的 remaining infinite escape 分类成一个相当窄的
**\(P_2\)-axis sector + exact decimal mantissa balance + ordinary coprime rational scale** 问题。

---

# 1. Executive Summary

## 1.1 FROZEN — 前四轮状态

冻结：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
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
\gcd(U,V)=1,
\]

\[
g=m_3-n_3\ge0,
\qquad
k=s_2+s_3\ge1,
\]

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g.
\]

flat locus 已删除；定义

\[
D=P_1 10^k-Q_0>0,
\]

\[
\Delta_{12}
=
g_2 10^{m_2}D-g_1Q_0,
\]

\[
\Delta_3
=
g_3P_2 10^{n_3}-g_2(Q_0-P_3),
\]

并有

\[
\boxed{
g_1\Delta_3
=
-10^{m_3}g_3\Delta_{12},
}
\]

\[
\Delta_{12}\Delta_3\ne0.
\]

第三轮已有：

\[
\boxed{
10^{2g+k-2}
<
\frac{P_2}{P_3}
<
10^{2g+k+2},
}
\]

\[
\boxed{
10^{2g+k-2}<Q_0,
\qquad
10^g<\sqrt{10Q_0}.
}
\]

第四轮已有：

\[
\boxed{
(g_2,g_3,n_2,n_3)\ \text{fixed}
\Longrightarrow
Q_0\ \text{bounded}
}
\]

以及 minimal common-\(U\) gate

\[
U\in I_{23}\cap\mathbf Z_{>0},
\qquad
\gcd(U,V)=1.
\]

**状态：FROZEN / PREVIOUSLY PROVED.**

---

## 1.2 NEW PROVED — \(\lambda=U/V\) 是真正的 radial quotient

由 primitive normalization：

\[
\boxed{
\frac{a_i}{b_i}
=
\frac UVP_i
=
\lambda P_i.
}
\]

令

\[
\alpha_i:=\frac{a_i}{10^{n_i}}\in[10^{-1},1),
\qquad
\beta_i:=\frac{b_i}{10^{m_i}}\in[10^{-1},1).
\]

则：

\[
\boxed{
\lambda P_i
=
\frac{\alpha_i}{\beta_i}10^{s_i}.
}
\tag{1.1}
\]

因此：

\[
\boxed{
10^{s_i-1}<\lambda P_i<10^{s_i+1}.
}
\tag{1.2}
\]

A1 中 \(s_2=g+k,\ s_3=-g\)，立即得到 (DR2)、(DR3)、(RATIO)、(PRODUCT)。

---

## 1.3 NEW PROVED — common-\(V\) 后 radial arms 永远由 Arm 2 主导

定义第四轮：

\[
X_2=\frac{g_2 10^{n_2}}{U\sqrt{Q_0}},
\qquad
X_3=\frac{g_3 10^{n_3}}{U\sqrt{Q_0}}.
\]

因为

\[
g_i=\frac V{b_i}
=
\frac{V}{\beta_i10^{m_i}},
\]

得：

\[
\boxed{
X_2
=
\frac{10^{g+k}}
{\lambda\beta_2\sqrt{Q_0}},
}
\tag{1.3}
\]

\[
\boxed{
X_3
=
\frac{1}
{\lambda\beta_3 10^g\sqrt{Q_0}}.
}
\tag{1.4}
\]

故精确：

\[
\boxed{
\frac{X_2}{X_3}
=
10^{2g+k}\frac{\beta_3}{\beta_2}.
}
\tag{1.5}
\]

因

\[
10^{-1}<\frac{\beta_3}{\beta_2}<10,
\]

所以：

\[
\boxed{
10^{2g+k-1}
<
\frac{X_2}{X_3}
<
10^{2g+k+1}.
}
\tag{1.6}
\]

而 \(2g+k\ge1\)，于是：

\[
\boxed{
X_2>X_3
}
\]

对每个 genuine A1 state 恒成立。

所以：

- **Arm 3 dominant：IMPOSSIBLE；**
- balanced arms 只有在 \(2g+k\) bounded 时才可能；
- \(2g+k\to\infty\) 时必为 Arm 2 strongly dominant。

更强地，本轮随后证明：

\[
\boxed{
X_2>\frac{\sqrt{Q_0}}{11},
}
\]

所以 genuine infinite sequence 中：

\[
\boxed{X_2\to\infty.}
\]

第四轮的 \(X_2\gtrsim1\) 因而可提升为线性 primitive-height forcing。

---

# 2. Frozen Four-Round Results

本轮不重新证明：

1. DD 已闭合；
2. fixed primitive core \(\Rightarrow\) finite decimal fibre；
3. A1 translation line；
4. flat coefficient locus 不存在；
5. exact primitive GSYNC；
6. primitive synchronization alone insufficient；
7. common-\(U\) 是最后的 numerator radial realization；
8. fixed \((g_2,g_3,n_2,n_3)\) 后 integer-\(U\) 使 \(Q_0\) bounded；
9. exact coprime counting formula；
10. common-\(U\) real cone 不等于 integer radial feasibility；
11. moving profile 下 interval width 不会仅因 \(Q_0\to\infty\) 自动缩到 \(<1\)。

本轮只在这些 theorem 之上继续做 moving-profile elimination。

---

# 3. Minimal Remaining A1 State

## 3.1 PROVED — semantic minimality 可进一步压到 primitive sphere + reduced rational \(\lambda\)

一旦给定：

\[
(P_1,P_2,P_3,Q_0)
\]

以及 reduced positive rational

\[
\lambda=\frac UV,
\qquad
\gcd(U,V)=1,
\]

则：

\[
g_i=\gcd(V,P_i)
\]

唯一确定，继而：

\[
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}
\]

唯一恢复。

各：

\[
n_i=\ell(a_i),
\qquad
m_i=\ell(b_i),
\qquad
s_i=n_i-m_i
\]

也唯一确定。

因此从 exact witness dimension 看：

\[
\boxed{
(P_1,P_2,P_3,Q_0;\lambda)
}
\]

已经足以恢复全部 block/gcd/profile presentation data。

**注意：** 这不是说 \(\lambda\) 的实数大小足够；必须保留它的**既约有理表示** \(U/V\)，因为 denominator gcd profile 读取 \(V\) 的逐素数信息。

---

## 3.2 PROVED — profile movement 不是独立的“很多自由变量”

\[
g_i,n_i,m_i,U,V
\]

并非同层独立自由变量：

- \(U,V\) 是 reduced \(\lambda\) 的分子分母；
- \(g_i\) 由 \(V\) 与 \(P_i\) 决定；
- \(n_i,m_i\) 由恢复出的 \(a_i,b_i\) 决定；
- \(g,k\) 由 \(s_2,s_3\) 决定。

因此 moving-profile infinity 更准确的表述是：

\[
\boxed{
\text{moving primitive rational direction}
+
\text{moving reduced rational height of }\lambda.
}
\]

profile notation 仍然非常适合做局部算术，但不应再被当作 intrinsic high-dimensional witness space。

---

# 4. Common-\(U\) Reconstruction

第四轮的 complete reconstruction principle 保持有效：

若 primitive sphere、exact common-\(V\) recovery、A1 exponent relations、GSYNC、denominator digit legality，以及一个 coprime integer \(U\) 的 numerator digit legality全部成立，则完整 original strict candidate 已恢复。

因此本轮没有再假想一个 forward norm gate。

同时：

\[
U=\gcd(a_1,a_2,a_3),
\qquad
V=\operatorname{lcm}(b_1,b_2,b_3)
\]

在 exact primitive normalization 中成立。

---

# 5. Fixed-Profile Finiteness

第四轮：

\[
Q_0
<
\frac{
g_2^2(10^{n_2}-1)^2+
g_3^2(10^{n_3}-1)^2
}{U^2}
\]

说明 fixed \((g_2,g_3,n_2,n_3)\) 无法无限逃逸。

本轮强化其 geometric interpretation：

真正 escaping arm 不仅至少 \(\sqrt{Q_0}\) 级，而实际上第二 arm 必须线性支持 primitive height：

\[
\boxed{
\frac{g_2 10^{n_2}}{U}
>
\frac{Q_0}{11}.
}
\tag{5.1}
\]

故：

\[
\boxed{
X_2>\frac{\sqrt{Q_0}}{11}.
}
\]

这说明所有 genuine moving-profile compensation 最终都必须把足够多的 scale mass 放在 block 2 上。

---

# 6. Radial Escape Arms

## 6.1 PROVED — Arm 3 dominant impossible

由 (1.6)：

\[
X_2/X_3>1.
\]

所以不存在：

\[
X_3\gg X_2.
\]

---

## 6.2 PROVED — asymptotically balanced arms \(\Rightarrow 2g+k\) bounded

若某序列满足：

\[
X_2/X_3\le C
\]

for a fixed constant \(C\)，则：

\[
10^{2g+k-1}<C,
\]

即：

\[
2g+k\le1+\log_{10}C.
\]

所以 genuine growing translation depth 必然转入 Arm 2 dominant。

---

## 6.3 NEW PROVED — Arm 2 实际上 always linearly large

由后文 Theorem MP-P2：

\[
P_2>Q_0/11.
\]

又由 numerator mantissa：

\[
X_2
=
\frac{P_2}{\alpha_2\sqrt{Q_0}},
\qquad
\alpha_2<1.
\]

故：

\[
\boxed{
X_2>\frac{\sqrt{Q_0}}{11}.
}
\]

所以 infinite family 中 Arm 2 不只是 dominant，而是 diverging。

---

# 7. \(h=Q_0-P_1\) Coordinates — Route Correction

这是本轮最重要的 prompt-level correction。

定义：

\[
h:=Q_0-P_1.
\]

prompt 希望研究：

\[
h=O(1),\qquad h=o(Q_0),\qquad h\asymp Q_0.
\]

本轮证明前两种在 A1 中根本不会发生。

---

## 7.1 NEW PROVED — exact leading-block sandwich

设完整 numerator / denominator words：

\[
A
=
a_1 10^{n_2+n_3}
+
a_2 10^{n_3}
+
a_3,
\]

\[
B
=
b_1 10^{m_2+m_3}
+
b_2 10^{m_3}
+
b_3.
\]

写：

\[
A
=
10^{n_2+n_3}(a_1+\theta_A),
\qquad
\frac1{10}\le\theta_A<1,
\]

\[
B
=
10^{m_2+m_3}(b_1+\theta_B),
\qquad
\frac1{10}\le\theta_B<1.
\]

A1 中：

\[
(n_2+n_3)-(m_2+m_3)=k.
\]

又：

\[
\frac AB=\lambda Q_0,
\qquad
\frac{a_1}{b_1}=\lambda P_1.
\]

所以：

\[
\frac{Q_0}{P_1}
=
10^k
\frac{1+\theta_A/a_1}
{1+\theta_B/b_1}.
\]

已有 \(D=P_110^k-Q_0>0\)，因此：

\[
\frac{Q_0}{P_1}<10^k.
\]

另一方面：

\[
1+\frac{\theta_A}{a_1}>1,
\qquad
1+\frac{\theta_B}{b_1}<1+\frac1{b_1},
\]

于是：

\[
\boxed{
\frac{10^k b_1}{b_1+1}
<
\frac{Q_0}{P_1}
<
10^k.
}
\tag{7.1}
\]

即：

\[
\boxed{
10^{-k}
<
\frac{P_1}{Q_0}
<
\left(1+\frac1{b_1}\right)10^{-k}.
}
\tag{7.2}
\]

---

## 7.2 NEW PROVED — exact leading defect coordinate

定义：

\[
\boxed{
\varepsilon
=
\frac{b_1D}{Q_0}
=
b_1\left(
10^k\frac{P_1}{Q_0}-1
\right).
}
\]

由 (7.1)：

\[
\boxed{0<\varepsilon<1.}
\]

并且：

\[
\boxed{
\frac{P_1}{Q_0}
=
10^{-k}\left(1+\frac{\varepsilon}{b_1}\right).
}
\tag{7.3}
\]

所以 \(D/Q_0=\varepsilon/b_1\)。

这比只知道 \(D>0\) 强得多：前部 primitive defect 已被压成一个 genuine unit interval coordinate。

---

## 7.3 DISPROVED — near-\(P_1\)-axis conjecture

因为 \(k\ge1\)：

\[
P_1/Q_0<0.2.
\]

所以：

\[
\boxed{
\frac{h}{Q_0}
=
1-\frac{P_1}{Q_0}
>0.8.
}
\]

而且：

\[
\frac{h}{Q_0}
<
1-10^{-k}.
\]

因此：

\[
\boxed{
h\asymp Q_0
}
\]

对所有 A1 states 恒成立。

所以本轮 prompt 中：

- \(h=O(1)\) dangerous regime；
- \(h=o(Q_0)\) near-axis regime；

都应正式删除。

---

# 8. The Correct Near-Axis Coordinate: \(d_2=Q_0-P_2\)

由 sphere：

\[
\boxed{
P_1^2+P_3^2
=
d_2(2Q_0-d_2),
\qquad
d_2:=Q_0-P_2\ge1.
}
\tag{8.1}
\]

这才是 A1 moving-profile 的 natural near-axis factorization。

---

## 8.1 NEW PROVED — universal \(P_2\) linear-height theorem

由 ratio theorem：

\[
P_2/P_3>10^{2g+k-2}\ge10^{-1},
\]

所以：

\[
P_3<10P_2.
\]

又由 \(P_1<0.2Q_0\)：

\[
Q_0^2
=
P_1^2+P_2^2+P_3^2
<
\frac{Q_0^2}{25}+101P_2^2.
\]

故：

\[
\boxed{
P_2>
\sqrt{\frac{24}{2525}}\,Q_0
>
\frac{Q_0}{11}.
}
\tag{8.2}
\]

---

## 8.2 NEW PROVED — \(g\ge1\) 时 primitive direction 强制贴近 \(P_2\)-axis

若 \(g\ge1\)，则：

\[
2g+k\ge3,
\]

故：

\[
P_2/P_3>10,
\qquad
P_3<P_2/10.
\]

于是：

\[
Q_0^2
<
\frac{Q_0^2}{25}
+
\frac{101}{100}P_2^2.
\]

故：

\[
\boxed{
P_2>
\sqrt{\frac{96}{101}}\,Q_0
>0.975Q_0.
}
\tag{8.3}
\]

因此 growing-\(g\) family 确实是一个真正的 \(P_2\)-axis family。

---

## 8.3 NEW PROVED — \(d_2\) 与 \(k\) 的双向平方尺度

由：

\[
d_2
=
\frac{P_1^2+P_3^2}{Q_0+P_2},
\]

及：

\[
P_1>Q_0 10^{-k},
\]

得到：

\[
\boxed{
d_2
>
\frac{Q_0}{2\,10^{2k}}.
}
\tag{8.4}
\]

另一方面：

\[
P_1
<
\left(1+\frac1{b_1}\right)Q_0 10^{-k},
\]

且：

\[
P_3
<
Q_0 10^{2-(2g+k)}.
\]

所以：

\[
\boxed{
d_2
<
\frac{Q_0}{10^{2k}}
\left[
\left(1+\frac1{b_1}\right)^2
+
10^{4-4g}
\right].
}
\tag{8.5}
\]

这给出：

\[
\boxed{
d_2
\asymp_{\text{decimal constants}}
Q_0 10^{-2k}.
}
\]

因此：

\[
\boxed{
k
\text{ 控制 }P_2\text{-axis radial gap}.
}
\]

---

## 8.4 NEW PROVED — square-root \(k\)-height collapse

因为 \(d_2\ge1\)，由 (8.5)：

\[
10^{2k}
<
Q_0
\left[
\left(1+\frac1{b_1}\right)^2
+
10^{4-4g}
\right].
\]

统一：

\[
\boxed{
10^{2k}<10004Q_0.
}
\tag{8.6}
\]

若 \(g\ge1\)：

\[
\boxed{
10^{2k}<5Q_0.
}
\tag{8.7}
\]

所以 \(k\) 也不能以 \(\log Q_0\) 的 full slope 增长，而只能：

\[
\boxed{
k\le\frac12\log_{10}Q_0+O(1).
}
\]

这是本轮重要的新 height theorem。

---

# 9. Moving GCD/Profile Budget

## 9.1 PROVED — \(g_i\) 并非独立 growth coefficients

\[
g_i=\gcd(V,P_i)
\]

所以：

\[
g_i\mid V,
\qquad
g_i\mid P_i,
\qquad
g_i\le P_i<Q_0.
\]

但不能从 \(g_i\) 大推出 \(V\) radical-rich。

大 gcd 可以由少数 prime powers 提供。

---

## 9.2 FAILED — “\(g_2,g_3\) 的大 mass 必须由 disjoint primes 承担”

该 conjecture 不成立。

若：

\[
p\mid g_2,g_3,
\]

仅得到：

\[
p\mid P_2,P_3,V.
\]

sphere mod \(p\) 只给：

\[
P_1^2\equiv Q_0^2\pmod p,
\]

即：

\[
P_1\equiv\pm Q_0\pmod p,
\]

并不强迫：

\[
p\mid P_1,Q_0.
\]

最简单的 primitive sphere 例子：

\[
1^2+2^2+2^2=3^2
\]

中 prime \(2\) 同时整除 \(P_2,P_3\)，但 primitive gcd 仍为 \(1\)。

所以“primitive geometry 禁止 \(g_2,g_3\) 共享 prime mass”是错误的。

---

## 9.3 FAILED AS A GENERAL ROUTE — radical-rich \(\Rightarrow\) coprime scarcity

当前没有 theorem：

\[
g_2,g_3\text{ large}
\Longrightarrow
\omega(V)\to\infty
\]

或：

\[
\operatorname{rad}(V)\text{ 必以某个足够快速度增长}.
\]

因此不能把 moving gcd magnitude 自动转换成 Jacobsthal/coprime-gap contradiction。

coprime sieve 仍是 exact terminal gate，但当前没有足够的 global prime-support forcing 使其成为 uniform closure engine。

---

# 10. Common-\(V\) Window

对 fixed gcd profile：

\[
b_i=\frac V{g_i}
\]

的 digit legality 等价于：

\[
\boxed{
V\in
J_i:=
[g_i10^{m_i-1},g_i10^{m_i}).
}
\]

故：

\[
\boxed{
V\in I_V:=J_1\cap J_2\cap J_3.
}
\]

但与 common-\(U\) 不同，\(V\) 还必须满足：

\[
\boxed{
\gcd(V,P_i)=g_i
\qquad(i=1,2,3).
}
\]

因此 common-\(V\) 是：

\[
\boxed{
\text{decimal interval}
+
\text{exact gcd-profile sieve},
}
\]

而不是纯 interval problem。

---

# 11. Two-Radial-Scale Formulation

在 profile presentation 中：

\[
U\in I_U,
\qquad
V\in I_V,
\]

并要求：

\[
\gcd(U,V)=1,
\qquad
\gcd(V,P_i)=g_i.
\]

所以可以形式上看作：

\[
(U,V)\in\mathcal R
\subset\mathbf R_{>0}^2.
\]

但本轮裁决：

\[
\boxed{
\text{二维 rectangle / geometry-of-numbers 不是 canonical final language}.
}
\]

原因：

1. \(g_i\) 本身由 \(V\) 决定；
2. \(U,V\) 不是两个独立 real radii，而是 reduced rational \(\lambda=U/V\) 的 arithmetic numerator/denominator；
3. 两个窗口都跨约一个 decade，moving profile 时不会自动变薄；
4. coprimality 与 gcd-profile 是逐素数条件，不能由区域面积替代。

因此：

\[
\boxed{
\lambda=U/V
}
\]

是比 \((U,V)\) 的 continuous rectangle 更 intrinsic 的 global radial coordinate。

---

# 12. \(\lambda=U/V\) Reduction

由：

\[
\lambda P_i=\frac{a_i}{b_i},
\]

A1 的核心 ratio geometry 成为：

\[
\boxed{
\lambda P_2\sim_{\times 10}10^{g+k},
\qquad
\lambda P_3\sim_{\times 10}10^{-g}.
}
\]

而本轮进一步由 \(P_2>Q_0/11\) 得：

\[
\boxed{
10^{g+k-1}
<
\lambda Q_0
<
110\,10^{g+k}.
}
\tag{12.1}
\]

所以：

\[
\boxed{
\lambda Q_0
\asymp_{\times 1100}
10^{g+k}.
}
\]

这识别了 prompt 中猜测的实际 word scale：

\[
\lambda Q_0=\frac AB
\]

正是完整 concatenated fraction 的值。

---

# 13. Decimal-Ratio Normal Form

对每块：

\[
\lambda P_i
=
\frac{\alpha_i}{\beta_i}10^{s_i}.
\]

因此 \((g,k)\) 不再只是 metadata：

\[
\boxed{
2g+k
}
\]

是 primitive angular ratio \(P_2/P_3\) 的 decimal logarithmic coordinate，

而：

\[
\boxed{k}
\]

又通过 \(d_2\) 控制 \(P_2\)-axis radial gap。

因此 moving primitive geometry 的两个最自然 discrete decimal coordinates 是：

\[
\boxed{
k
\quad\text{和}\quad
T:=2g+k.
}
\]

等价地：

- \(k\)：radial gap exponent；
- \(T\)：third-coordinate angular exponent；
- \(g=(T-k)/2\)：first/third transverse anisotropy。

---

# 14. \(P_2/P_3\) Sandwich

冻结第三轮：

\[
10^{T-2}
<
\frac{P_2}{P_3}
<
10^{T+2},
\qquad T=2g+k.
\]

结合 \(P_2>Q_0/11\) 得：

\[
\boxed{
\frac{Q_0}{1100\,10^T}
<
P_3
<
100Q_0\,10^{-T}.
}
\tag{14.1}
\]

再结合 leading \(P_1\)-sandwich：

\[
\boxed{
10^{2g-2}
<
\frac{P_1}{P_3}
<
2200\,10^{2g}.
}
\tag{14.2}
\]

因此：

\[
\boxed{
k\text{ controls }P_1/Q_0,
\quad
2g+k\text{ controls }P_3/Q_0,
\quad
2g\text{ controls }P_1/P_3.
}
\]

这比原来的 generic “\(P_3/P_2\to0\)” 强得多。

---

# 15. Product Law \(\lambda^2P_2P_3\)

由 DR2 × DR3：

\[
\boxed{
10^{k-2}
<
\lambda^2P_2P_3
<
10^{k+2}.
}
\]

这是一个真正的 \(g\)-free conservation law。

但将 canonical scales：

\[
\lambda\sim\frac{10^{g+k}}{Q_0},
\qquad
P_2\sim Q_0,
\qquad
P_3\sim Q_0 10^{-(2g+k)}
\]

代入后：

\[
\lambda^2P_2P_3
\sim
10^k.
\]

所以该 relation 与 \(P_2\)-axis escape 完全同阶相容。

**裁决：**

\[
\boxed{
\text{PROVED structural invariant, FAILED as standalone closure}.
}
\]

---

# 16. Sphere / Near-Axis Coupling

正确的 exact coupling 是：

\[
\boxed{
P_1^2+P_3^2
=
(Q_0-P_2)(Q_0+P_2).
}
\]

而不是把：

\[
P_2^2+P_3^2
=
(Q_0-P_1)(Q_0+P_1)
\]

当作 small-excess identity。

本轮得到：

\[
d_2/Q_0
\asymp
10^{-2k}.
\]

所以若 \(k\to\infty\)，primitive point 确实趋近 \(P_2\)-axis。

若 \(k\) bounded，\(d_2/Q_0\) 可以保持常数量级，但 \(P_2\) 仍线性于 \(Q_0\)。

---

## 16.1 FAILED — pure integer square-spacing closure

即使 sector 很窄，primitive sphere 本身仍有大量 lattice directions。

### Theorem — Open decimal sectors contain infinitely many primitive sphere points

固定任意 \(g\ge0,k\ge1\)，考虑 real unit sphere positive octant中满足：

\[
10^{-k}
<
x_1
<
2\cdot10^{-k},
\]

\[
10^{2g+k-2}
<
x_2/x_3
<
10^{2g+k+2}.
\]

这是非空 open patch。

有理点在 \(S^2\) 上稠密（可由 stereographic rational parametrization直接得到），因此该 patch 含无限多个 rational sphere points。

清分母并 primitive reduction 后，得到无限多个：

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

primitive integer points满足同一 sector。

由于 bounded \(Q_0\) 只有有限 primitive points，这些点的 \(Q_0\) 必无界。

所以：

\[
\boxed{
\text{sphere}
+
\text{decimal ratio sector}
+
\text{integer }P_3,d_2
}
\]

本身绝不可能关闭 A1。

**状态：NEW PROVED NEGATIVE THEOREM.**

---

# 17. Plus/Minus Branch Consequences

定义：

\[
d:=m_2-g.
\]

注意：

\[
\boxed{
n_2
=
m_2+g+k
=
2g+k+d
=
T+d.
}
\tag{17.1}
\]

这已经把 \(n_2\) 从独立 profile variable 中删除。

---

## 17.1 NEW PROVED — exact mantissa/defect balance

由 leading defect：

\[
\varepsilon
=
\frac{b_1D}{Q_0},
\]

以及：

\[
\beta_i=b_i/10^{m_i},
\quad
x=P_2/Q_0,
\quad
y=P_3/Q_0,
\]

将 GSYNC 代入并消去 \(g_i,V,U,n_3\)，得到：

\[
\boxed{
\varepsilon
=
\beta_2(1-x10^{-g})
+
\beta_3(1-y)10^{-m_2}.
}
\tag{17.2}
\]

等价：

\[
\boxed{
10^g(\varepsilon-\beta_2)
=
-\beta_2x
+
\beta_3(1-y)10^{-d}.
}
\tag{17.3}
\]

这是本轮最重要的 exact moving-profile normal form。

特别：

\[
\Delta_{12}>0
\iff
\varepsilon>\beta_2,
\]

\[
\Delta_{12}<0
\iff
\varepsilon<\beta_2.
\]

---

## 17.2 NEW PROVED — sign branch 直接约束 \(m_2-g\)

plus branch：

\[
\varepsilon>\beta_2
\]

等价于：

\[
\boxed{
10^d
<
\frac{\beta_3(1-y)}
{\beta_2x}.
}
\tag{17.4+}
\]

minus branch：

\[
\boxed{
10^d
>
\frac{\beta_3(1-y)}
{\beta_2x}.
}
\tag{17.4-}
\]

### universal plus

由：

\[
x>1/11,
\qquad
\beta_3/\beta_2<10,
\]

得 RHS \(<110\)。

所以：

\[
\boxed{
\text{plus}\Longrightarrow d\le2.
}
\tag{17.5}
\]

### \(g\ge1\) plus

此时：

\[
x>\sqrt{96/101}>0.975.
\]

故 RHS \(<10.26\)，于是：

\[
\boxed{
g\ge1,\ \text{plus}
\Longrightarrow
d\le1.
}
\tag{17.6}
\]

即：

\[
\boxed{
m_2\le g+1.
}
\]

### \(g\ge1\) minus

此时 \(P_3<P_2/10\)，故 \(y<0.1\)。

又：

\[
\beta_3/\beta_2>0.1,
\quad
x<1,
\]

所以 RHS \(>0.09\)。

minus 要求 \(10^d>0.09\)，故：

\[
\boxed{
g\ge1,\ \text{minus}
\Longrightarrow
d\ge-1.
}
\tag{17.7}
\]

即：

\[
\boxed{
m_2\ge g-1.
}
\]

这把第三轮 minus bound \(g\le m_2+2\) 改善为 growing-\(g\) 区域的 \(g\le m_2+1\)。

---

## 17.3 NEW branch profile classification

若 \(g\ge1\)：

\[
d\le-2
\Longrightarrow
\text{plus},
\]

\[
d\ge2
\Longrightarrow
\text{minus},
\]

而：

\[
d\in\{-1,0,1\}
\]

是唯一真正 mantissa-sensitive transition strip。

因此 sign branch 的 moving-profile freedom已经从无限整数轴压成：

\[
\boxed{
\text{two half-lines + three transition slices}.
}
\]

---

# 18. Absolute-\(g\) Attempts

本轮没有得到：

\[
g\le G.
\]

已有：

\[
10^{2g+k-2}<Q_0,
\]

和新的：

\[
10^{2k}<10004Q_0.
\]

它们只给：

\[
g,k=O(\log Q_0).
\]

---

## 18.1 why \(g\to\infty\) still survives size geometry

当 \(g\to\infty\)：

\[
P_3/P_2\to0,
\]

但 \(P_1/Q_0\) 主要由 \(k\) 控制，而不是由 \(g\) 控制。

若 \(k\) bounded：

\[
P_1/Q_0
\asymp10^{-k}
\]

仍为固定常数，而：

\[
P_3/Q_0
\asymp10^{-(2g+k)}
\to0.
\]

sphere 只把：

\[
P_2/Q_0
\]

推向：

\[
\sqrt{1-(P_1/Q_0)^2},
\]

完全相容。

所以：

\[
\boxed{
g\to\infty
}
\]

不是由 primitive sphere alone 排除的。

---

## 18.2 Minus growing-\(g\) 的新近似结构

minus 且 \(g\to\infty\) 时：

\[
m_2\ge g-1\to\infty.
\]

于是 (17.2) 给：

\[
\varepsilon
=
\beta_2
-
\beta_2x10^{-g}
+
O(10^{-g+1}),
\]

即：

\[
\boxed{
\varepsilon-\beta_2
=
O(10^{-g})
\quad\text{from below}.
}
\]

这暴露出一个新的 exact rational-approximation frontier：

\[
\boxed{
\varepsilon
=
\frac{b_1D}{Q_0}
\quad\text{必须长期以 }10^{-g}\text{ 级精度逼近 }
\beta_2=\frac{b_2}{10^{m_2}}.
}
\]

但本轮没有证明其 rational spacing 与 gcd/reducedness 不兼容。

**状态：NEW REDUCTION / OPEN.**

---

# 19. Tropical Escape Analysis

取 subsequence 使下列 logarithmic slopes 存在：

\[
\rho
=
\lim
\frac{g\log10}{\log Q_0},
\]

\[
\kappa
=
\lim
\frac{k\log10}{\log Q_0}.
\]

定义：

\[
\alpha_i
=
\lim
\frac{\log P_i}{\log Q_0}.
\]

由本轮 exact sector：

\[
\boxed{
\alpha_1=1-\kappa,
}
\]

\[
\boxed{
\alpha_2=1,
}
\]

\[
\boxed{
\alpha_3=1-(2\rho+\kappa).
}
\]

并且：

\[
\boxed{
\log d_2/\log Q_0
=
1-2\kappa.
}
\]

\[
\boxed{
\log\lambda/\log Q_0
=
\rho+\kappa-1.
}
\]

约束：

\[
\boxed{
0\le\kappa\le\frac12,
}
\]

\[
\boxed{
\rho\ge0,
\qquad
2\rho+\kappa\le1.
}
\tag{19.1}
\]

---

## 19.1 FAILED — Tropical uniqueness

当前 strict size relations留下的是一个二维三角区：

\[
\boxed{
\mathcal T
=
\{
(\rho,\kappa):
\rho\ge0,\ 
0\le\kappa\le1/2,\ 
2\rho+\kappa\le1
\}.
}
\]

不是一个唯一 ray。

因此本轮没有达到 prompt Level 4 “Tropical uniqueness”。

更准确的成果是：

\[
\boxed{
\textbf{Tropical dimension reduction from many profile slopes to two slopes }(\rho,\kappa).
}
\]

任何进一步 tropical closure 必须使用 exact mantissa/GSYNC arithmetic，而不是继续重复 sphere size balance。

---

# 20. Integer-\(U\) Interval Width

第四轮已经指出 moving profile 中 interval 不自动变窄。

本轮用 actual numerator mantissas把这一点写得更直接。

因为：

\[
C_i=\frac{a_i}{U}
=
\frac{\alpha_i10^{n_i}}U,
\]

故：

\[
I_i
=
\left[
\frac{10^{n_i-1}}{C_i},
\frac{10^{n_i}}{C_i}
\right)
=
\left[
\frac{U}{10\alpha_i},
\frac{U}{\alpha_i}
\right).
\]

因此：

\[
I_{23}
=
\left[
\max\left(
\frac{U}{10\alpha_2},
\frac{U}{10\alpha_3}
\right),
\min\left(
\frac{U}{\alpha_2},
\frac{U}{\alpha_3}
\right)
\right).
\]

若记：

\[
\alpha_{\min}=\min(\alpha_2,\alpha_3),
\qquad
\alpha_{\max}=\max(\alpha_2,\alpha_3),
\]

则：

\[
\boxed{
|I_{23}|
=
U\left(
\frac1{\alpha_{\max}}
-
\frac1{10\alpha_{\min}}
\right).
}
\tag{20.1}
\]

只要 projective cone不是逼近边界：

\[
\alpha_{\max}=10\alpha_{\min},
\]

width 就是 \(U\) 的正比例量。

因此：

\[
\boxed{
Q_0\to\infty
\not\Rightarrow
|I_{23}|<1.
}
\]

**裁决：FAILED as a global geometry-only route.**

这并不排除 full GSYNC 后某个 branch 的 interval eventually unique；只是说明必须使用 exact arithmetic，而不能从 scale size 单独推出。

---

# 21. Coprime Scarcity

exact count：

\[
N_V([L,R))
=
\sum_{d\mid\operatorname{rad}(V)}
\mu(d)
\left(
\left\lceil\frac Rd\right\rceil
-
\left\lceil\frac Ld\right\rceil
\right)
\]

继续有效。

但本轮没有得到 uniform：

\[
N_V(I_{23})\le C.
\]

原因：

1. interval width可与 \(U\) 同阶；
2. \(V\) 不必 radical-rich；
3. large gcd profile可以靠 prime powers，而不是大量 distinct primes；
4. moving profile允许把 decimal growth放在 digit lengths而不是 \(\operatorname{rad}(V)\)。

因此当前最精确结论是：

\[
\boxed{
\text{coprime scarcity 是 terminal arithmetic sieve，}
}
\]

但：

\[
\boxed{
\text{不是目前已证明的 global escape killer}.
}
\]

---

# 22. Computation / Counterexamples

本轮计算只用于 falsification / geometry audit，不用于任何 nonexistence theorem。

以下 primitive sphere points均满足：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

并落入相应 \((g,k)\) 的粗 decimal sector：

| \(g\) | \(k\) | \(P_1\) | \(P_2\) | \(P_3\) | \(Q_0\) | \(P_2/P_3\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 99792 | 425544 | 444671 | 623521 | 0.957 |
| 1 | 1 | 296820 | 1754264 | 115227 | 1782925 | 15.224 |
| 1 | 2 | 4748 | 430464 | 1557 | 430493 | 276.470 |
| 2 | 1 | 144738 | 1153038 | 691 | 1162087 | 1668.651 |
| 0 | 2 | 9920 | 608505 | 147516 | 626209 | 4.125 |

这些点**不声称满足 GSYNC/common-\(U\)**。

它们只说明：

\[
\boxed{
\text{primitive integer sphere + decimal angular sector 本身非常富集}.
}
\]

因此不能把新的 \(P_2\)-axis picture误读成“integer spacing 已经接近 closure”。

**状态：EXPERIMENTAL ILLUSTRATION supporting a separately PROVED density theorem.**

---

# 23. Failed Conjectures

## 23.1 DISPROVED — every escape has \(h=Q_0-P_1\) small

实际：

\[
h/Q_0>0.8.
\]

---

## 23.2 DISPROVED — Arm 3 can dominate

实际：

\[
X_2/X_3>1.
\]

---

## 23.3 FAILED — balanced arms as growing-\(g\) frontier

若 \(2g+k\to\infty\)，则 \(X_2/X_3\to\infty\) up to fixed decade factors。

---

## 23.4 FAILED — \(g\) must be absolutely bounded by size geometry

现有 sphere/ratio/word-length constraints允许 \(\rho>0\) 的 tropical region。

---

## 23.5 FAILED — \(I_{23}\) eventually has width \(<1\)

moving mantissas can keep width proportional to \(U\)。

---

## 23.6 FAILED — moving gcd mass forces \(V\) radical-rich

prime powers and shared gcd support defeat this implication。

---

## 23.7 DISPROVED — \(g_2,g_3\) cannot share large prime support by primitive sphere

sphere mod shared prime only forces \(P_1\equiv\pm Q_0\)，not common divisibility。

---

## 23.8 FAILED — product law \(\lambda^2P_2P_3\asymp10^k\) closes A1

它正好与 canonical escape scaling 相容。

---

## 23.9 FAILED — near-axis integer spacing alone closes the sector

rational points are dense on sphere；每个 fixed \((g,k)\) 的 open sector含无限 primitive directions。

---

## 23.10 OPEN — common \(U,V\) automatically force fixed profile

没有证明。

第四轮已经证明 fixed profile impossible to escape；本轮只说明 profile redundancy可由 reduced \(\lambda\) 重新组织，不等于 profile 自己会 freeze。

---

# 24. New Proven Lemmas

### A1-MP-1 — Decimal Radial Quotient

\[
\lambda P_i=(\alpha_i/\beta_i)10^{s_i}.
\]

**NEW PROVED.**

### A1-MP-2 — Product Conservation

\[
10^{k-2}<\lambda^2P_2P_3<10^{k+2}.
\]

**NEW PROVED.**

### A1-MP-3 — Exact Arm Ratio

\[
X_2/X_3=10^{2g+k}\beta_3/\beta_2.
\]

**NEW PROVED.**

### A1-MP-4 — Arm-2 Dominance

\[
X_2>X_3.
\]

**NEW PROVED.**

### A1-MP-5 — Leading-Block Primitive Sandwich

\[
\frac{10^k b_1}{b_1+1}<Q_0/P_1<10^k.
\]

**NEW PROVED.**

### A1-MP-6 — Unit Leading Defect

\[
\varepsilon=b_1(P_110^k-Q_0)/Q_0\in(0,1),
\]

\[
P_1/Q_0=10^{-k}(1+\varepsilon/b_1).
\]

**NEW PROVED.**

### A1-MP-7 — \(P_2\) Linear Height

\[
P_2>Q_0/11.
\]

**NEW PROVED.**

### A1-MP-8 — Strong \(P_2\)-Axis for \(g\ge1\)

\[
P_2>\sqrt{96/101}\,Q_0.
\]

**NEW PROVED.**

### A1-MP-9 — Canonical \(d_2\) Window

\[
\frac{Q_0}{2\,10^{2k}}
<
Q_0-P_2
<
\frac{Q_0}{10^{2k}}
\left[
(1+1/b_1)^2+10^{4-4g}
\right].
\]

**NEW PROVED.**

### A1-MP-10 — Square-Root \(k\) Collapse

\[
10^{2k}<10004Q_0,
\]

and \(g\ge1\):

\[
10^{2k}<5Q_0.
\]

**NEW PROVED.**

### A1-MP-11 — Primitive Coordinate Scales

\[
\frac{Q_0}{1100\,10^{2g+k}}
<
P_3
<
100Q_0\,10^{-(2g+k)}.
\]

**NEW PROVED.**

### A1-MP-12 — First/Third Anisotropy

\[
10^{2g-2}<P_1/P_3<2200\,10^{2g}.
\]

**NEW PROVED.**

### A1-MP-13 — Full Word Scale

\[
10^{g+k-1}<\lambda Q_0<110\,10^{g+k}.
\]

**NEW PROVED.**

### A1-MP-14 — Exact Mantissa Balance

\[
\varepsilon
=
\beta_2(1-x10^{-g})
+
\beta_3(1-y)10^{-m_2}.
\]

**NEW PROVED.**

### A1-MP-15 — Branch Drift Bound

plus:

\[
m_2-g\le2,
\]

and if \(g\ge1\):

\[
m_2-g\le1.
\]

minus and \(g\ge1\):

\[
m_2-g\ge-1.
\]

**NEW PROVED.**

### A1-MP-16 — Primitive-Sector Density Negative Theorem

每个 fixed \((g,k)\) 的 nonempty open A1 ratio sector 含无限 primitive sphere directions。

**NEW PROVED NEGATIVE THEOREM.**

---

# 25. Current Infinite-Escape Classification

若存在 genuine sequence：

\[
Q_0\to\infty,
\]

则经过 subsequence 后，它必须满足：

\[
\boxed{
P_1/Q_0
=
10^{-k}(1+O(1)),
}
\]

更精确 factor \(<2\)；

\[
\boxed{
P_2/Q_0>1/11,
}
\]

且若 \(g\ge1\)：

\[
P_2/Q_0>0.975;
\]

\[
\boxed{
P_3/Q_0
\asymp_{\times 10^5}
10^{-(2g+k)};
}
\]

\[
\boxed{
(Q_0-P_2)/Q_0
\asymp_{\times 2\cdot10^4}
10^{-2k};
}
\]

\[
\boxed{
\lambda Q_0
\asymp
10^{g+k};
}
\]

并且：

\[
\boxed{
0\le\kappa\le1/2,
\quad
\rho\ge0,
\quad
2\rho+\kappa\le1.
}
\]

再加 exact mantissa equation：

\[
\boxed{
10^g(\varepsilon-\beta_2)
=
-\beta_2x+\beta_3(1-y)10^{-(m_2-g)}.
}
\]

因此真正的 infinite frontier 已从：

\[
(g_i,n_i,m_i,g,k,U,V)\text{ 大系统}
\]

压到：

\[
\boxed{
\textbf{\(P_2\)-axis primitive sector}
+
\textbf{reduced rational scale }\lambda
+
\textbf{one exact decimal mantissa balance}.
}
\]

---

# 26. Early-Splice Interface

本轮没有证明：

\[
N_V(I_{23})\le1
\]

或 \(O(1)\)。

因此尚未达到 prompt 原定的 strict unique-\(U\) splice criterion。

但是 forward/backward architecture 已经出现一个更自然的接点。

最新 backward work 已经表明：

- pure \(5\)-adic same-cut feedback存在 transverse Hensel survivors；
- \(2\)-adic companion能杀部分 branches，但不是 uniform closure；
- 真正缺失的 nonlocal relation是：
  **同一个 ordinary integer decimal scale / word realization** 与 local \(2\times5\) branches、full exact relation 的交。

而本轮 forward 已把这个 ordinary scale压成：

\[
\boxed{
\lambda=U/V
}
\]

及：

\[
\boxed{
\lambda Q_0\asymp10^{g+k},
\quad
P_2\text{-axis sector},
\quad
\text{exact mantissa balance (MB)}.
}
\]

所以若下一轮不希望继续纯 forward 消耗，最小 splice object 应是：

\[
\boxed{
(P_1,P_2,P_3,Q_0;\ U,V)
}
\]

或等价：

\[
\boxed{
(P_1,P_2,P_3,Q_0;\ \lambda_{\rm reduced})
}
\]

加实际 recovered blocks，而不是重新扩张整个旧 Exact-Lift state。

**状态：RECOMMENDED INTERFACE / not itself a closure theorem.**

---

# 27. Remaining Frontier

本轮之后最值得继续的纯正向问题已经不是：

\[
\text{“profile 怎么移动？”}
\]

而是下面这个单一 exact approximation / mantissa synchronization：

\[
\boxed{
\varepsilon
=
\beta_2(1-x10^{-g})
+
\beta_3(1-y)10^{-m_2},
}
\]

其中：

\[
\varepsilon
=
\frac{b_1(P_110^k-Q_0)}{Q_0}
\in(0,1),
\]

\[
\beta_i=\frac{b_i}{10^{m_i}}\in[0.1,1),
\]

\[
x=P_2/Q_0,
\qquad
y=P_3/Q_0,
\]

并且：

\[
x>1/11
\]

（\(g\ge1\) 时 \(x>0.975\)），

\[
y\asymp10^{-(2g+k)}.
\]

### Recommended Next Campaign A — Exact Mantissa Spacing / Reduced Rational Approximation

特别攻击 minus growing-\(g\)：

\[
m_2\ge g-1,
\]

所以：

\[
0<
\beta_2-\varepsilon
\ll10^{-g}.
\]

研究：

\[
\varepsilon=\frac{b_1D}{Q_0}
\]

与：

\[
\beta_2=\frac{b_2}{10^{m_2}}
\]

的 exact denominator/gcd spacing，尝试得到 nonflat lower bound与 \(10^{-g}\) upper bound冲突。

这是目前最可能产生 absolute-\(g\) bound 的纯正向路线。

### Recommended Next Campaign B — Plus Low-\(m_2\) Compression

plus 中：

\[
m_2\le g+1.
\]

若 \(m_2\ll g\)，(MB) 的 third term不是 \(10^{-g}\)-small，而是由 fixed/slow denominator mantissa控制。

应把这一 branch 与：

\[
n_2=T+d,
\qquad
d\le1,
\]

和已有 plus tail collapse联立，尝试得到 denominator digit conflict。

### Recommended Next Campaign C — Forward/Backward Reduced-\(\lambda\) Splice

若前两条仍只产生 Hensel-compatible rational approximations，不再追 generic coprime scarcity。

直接把：

\[
(U,V)
\]

恢复成 actual blocks，送入 backward \(2\times5\) actual-cut system。

---

# 28. Status Against Requested Outcome Levels

## Level 1 — A1 closure

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

## Level 2 — Moving-profile extinction

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

## Level 3 — Absolute \(g\)-bound

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

## Level 4 — Tropical uniqueness

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

反而证明 current size system leaves a 2D triangle.

## Level 5 — Unique \(U\)

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

moving width may scale like \(U\).

## Level 6 — Moving-profile pseudo-family

没有构造满足 **GSYNC + common-\(U/V\)** 的无界 pseudo-family；按第四轮 reconstruction theorem，那已经会极接近或等价于真实 strict candidate，因此不能轻率声称存在。

但本轮构造/证明了更低层的无限 ambient families：

\[
\boxed{
\text{primitive sphere + exact decimal angular sector}
}
\]

对每个 fixed \((g,k)\) 都有无限 primitive points。

所以本轮最准确等级应写成：

\[
\boxed{
\textbf{NEW CANONICAL \(P_2\)-AXIS ESCAPE NORMAL FORM}
+
\textbf{SQUARE-ROOT \(k\)-HEIGHT COLLAPSE}
+
\textbf{EXACT MANTISSA FRONTIER}.
}
\]

---

# 29. Negative-Result Ledger

后续不要重新投入大量 token 于：

1. \(h=Q_0-P_1\) small / near-\(P_1\)-axis；
2. Arm 3 dominant；
3. pure sphere integer spacing；
4. tropical size balance alone；
5. \(\lambda^2P_2P_3\asymp10^k\) alone；
6. moving gcd magnitude \(\Rightarrow\) radical-rich \(V\)；
7. primitive gcd \(\Rightarrow g_2,g_3\) prime supports disjoint；
8. generic interval width \(\Rightarrow\) eventual unique \(U\)；
9. geometry-of-numbers on a bare \(U,V\) rectangle；
10. fixed-profile conic infinity。

这些路线要么已被严格否定，要么已证明不足。

---

# 30. Source / Provenance Audit

本轮重点核对并使用：

- `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`
  - common-\(U\) exact interval；
  - integer/coprime count；
  - fixed-profile radial finiteness；
  - terminal reconstruction equivalence；
  - moving-profile width caveat。

- `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`
  - exact GSYNC；
  - Primitive Ratio Window；
  - \(10^{2g+k-2}<Q_0\)；
  - plus/minus sign facts；
  - primitive-only insufficiency。

- `strict_layer_A1_flat_locus_structural_elimination_campaign.md`
  - flat coefficient elimination；
  - nonzero defects。

- `strict_layer_A1_moving_core_decimal_translation_global_campaign.md`
  - moving-core interpretation；
  - fixed-core finite fibre provenance；
  - saturated/nonsaturated scope audit。

- `strict_layer_unified_exact_lift_campaign.md`
  和 `(1)`
  - primitive normalization；
  - \(U,V,g_i,C_i\) exact dictionary；
  - multiplication carry states；
  - master equation；
  - \(V=\operatorname{lcm}(b_i)\)。

- `strict_layer_post_DD_consolidation_A1_frontier.md`
  - Strict frontier = A1-only；
  - fixed-core finite decimal fibre；
  - exact word/cut reconstruction status。

- `strict_layer_moving_core_square_spacing_campaign.md`
  - bare square-spacing is auxiliary；
  - \(g\)-large alone does not force normalized square error to zero。

- backward A1 word / \(5\)-phase / same-cut norm / \(2\times5\) campaigns
  - only used to identify anti-duplication boundary and splice interface；
  - no backward phase theorem was used to prove the new forward lemmas.

旧 synthesis 仅用于 provenance locator；本轮新的 leading-block、\(P_2\)-axis、\(d_2\)、mantissa balance theorem 均从当前 exact definitions 与已冻结 theorem 直接重推。

---

# 31. Final Assessment

本轮最初的问题是：

\[
\boxed{
\text{moving profile 如何长期补偿，才能保留 coprime integer }U?
}
\]

研究后，最准确的答案不是“profile 必须沿某个复杂高维方向移动”。

大量 profile 其实是 presentation redundancy。

真正的 moving escape 已经压成：

\[
\boxed{
\begin{gathered}
Q_0\to\infty,\\
P_1/Q_0
=
10^{-k}(1+\varepsilon/b_1),\\
P_2/Q_0
\text{ 为线性主坐标},\\
P_3/Q_0
\asymp10^{-(2g+k)},\\
(Q_0-P_2)/Q_0
\asymp10^{-2k},\\
\lambda Q_0
\asymp10^{g+k},
\end{gathered}
}
\]

再加一个 exact decimal mantissa balance：

\[
\boxed{
\varepsilon
=
\beta_2(1-x10^{-g})
+
\beta_3(1-y)10^{-m_2}.
}
\]

所以新的核心问题应表述为：

\[
\boxed{
\textbf{一个 primitive \(P_2\)-axis direction，能否长期与一个 reduced rational scale }
\lambda
\textbf{ 以及 exact decimal mantissas 同步？}
}
\]

而不是：

\[
\text{“几十个 gcd/digit profile variables 能否一起长大？”}
\]

本轮没有关闭 A1，但已经把 prompt 原先的 moving-profile problem 从高维 profile bookkeeping，压缩成了一个更接近终端的：

\[
\boxed{
\textbf{\(P_2\)-axis arithmetic}
\times
\textbf{reduced rational scale}
\times
\textbf{exact mantissa synchronization}.
}
\]

如果下一轮继续 pure forward，优先攻击 (MB) 的 exact rational spacing。

如果该路线再次出现稳定 local/rational survivors，则应该提前与 backward 的 actual-cut \(2\times5\) system 拼接，而不再消耗 token 于 generic coprime-density 或 profile enumeration。
