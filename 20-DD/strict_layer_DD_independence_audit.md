# 三项十进制拼接平方和问题：DD Independence Audit

**文件名：** `strict_layer_DD_independence_audit.md`  
**研究层：** Backward Strict Layer / DD provenance audit  
**目标：** 对 SGR-9A `DD CLOSED` 做 theorem-level independence 审计，并把旧 External Exact-Lift 从最终 DD closure DAG 中尽可能删除。  
**最终等级：**

\[
\boxed{\textbf{DIA-1B — MINIMAL LEGACY KERNEL ISOLATED}}
\]

---

# 0. Executive verdict

本轮没有发现 SGR-9.1 的 terminal valuation contradiction 本身存在逻辑缺口，也没有发现不可消除的循环依赖。

更重要的是，SGR-9 原先 ledger 中大部分 “inherited” 节点都不是最终 DD closure 的不可替代外部输入。经过从原题重新定向后：

- 旧 `SGR-8` 的 \(J^\sharp/K^\sharp\) source orientation theorem 可以从最短 DD proof spine **完全删除**；
- source-labelled divisibility 可以改写成 canonical source-factor 的**定义/恒等后果**；
- 
  \[
  c=\frac{10^{m_3}Q}{A_\kappa}\in\mathbf Z,\qquad b_3=cD
  \]
  可以由一个独立重证的 tail-weight integrality lemma 推出；
- 
  \[
  uv=Nc^2,\qquad v-u=2ha_3
  \]
  可以直接由 original rational sphere + positivity 构造，不需要 old gap quadratic / Vieta branch；
- SGR-9 所需的
  \[
  v_5(F_-)=v_5(F_+)
  \]
  也不需要 old double-Hensel theorem：在 terminal-height 区域可以由 factor sum、reducedness 与一个极短的 \(5\)-adic argument **独立重证**；
- \(2\)-adic resonance、higher Hensel phase、near-\(S\)-unit、residual divisor supply、post-deflation \(J^\sharp\)、square-spacing、resultant、Pell/descent 等全部退出最终 DAG。

但本轮仍不能合法升级为 DIA-1A。

最终无法从当前 SGR/Strict-Layer 独立材料中重证的 theorem-level 输入可以压成唯一一个弱命题：

\[
\boxed{
\textbf{LH — Minimal DD Terminal-Height Localization}
}
\]

> 对任一真实 original DD candidate，pre-SGR-9 的 exhaustiveness reduction 已排除 sub-terminal DD strata，因此若该 candidate 存在，必有
> \[
> \boxed{m_3\ge 5S+11},
> \qquad S:=m_1+m_2.
> \]

现有旧链通过

\[
\text{DD frontier}
\subset
\{10S+11\le n_3,\ d_3\le5S\}
\]

得到该结论；但当前可独立回查的 SGR/Strict-Layer 文件没有给出“所有更低 DD strata 已被排除”的自包含证明。因此该节点仍然是 **LEGACY-DEPENDENT**。

所以最终：

\[
\boxed{
K_{\rm legacy}=\{\mathrm{LH}\},
\qquad
|K_{\rm legacy}|=1.
}
\]

本轮得到的是：

\[
\boxed{
\text{External Exact-Lift 的 DD theorem dependency 已从一整套 machinery}
\text{ 压成一个 terminal-height localization lemma。}
}
\]

---

# 1. Audit scope and source policy

本轮审计重点沿以下 Strict-Layer 文件逆向展开：

- `strict_layer_DD_oriented_tail_window_campaign.md`
- `strict_layer_DD_orientation_recovery_campaign.md`
- `strict_layer_DD_source_phase_information_audit.md`
- `strict_layer_DD_supply_phase_synchronization_campaign.md`
- `strict_layer_DD_post_deflation_campaign.md`
- `strict_layer_DD_error_closure_campaign.md`
- `strict_layer_moving_core_square_spacing_campaign.md`
- `strict_layer_unified_exact_lift_campaign.md`
- `strict_layer_post_DD_consolidation_A1_frontier.md`
- Backward recovery / denominator / algebraic interface 系列

旧 `exact_lift_research_synthesis_2026-08-10.md` 及其历史来源只用于：

1. provenance locator；
2. notation dictionary；
3. adversarial comparison；
4. 确认 frozen reduction 曾声称什么。

本报告不把旧文件中的任何未重证非平凡 theorem 直接计入 “independent” chain。

---

# 2. Canonical original-DD notation

固定一个 original DD candidate。记

\[
r_i=\frac{a_i}{b_i}>0,
\qquad
\gcd(a_i,b_i)=1.
\]

位数为

\[
n_i=\operatorname{digits}(a_i),
\qquad
m_i=\operatorname{digits}(b_i),
\]

并令

\[
s_i=n_i-m_i.
\]

DD chamber 意味着

\[
d_3:=s_3>0,
\qquad
s_2+s_3>0.
\]

记

\[
S:=m_1+m_2,
\]

\[
Q:=b_1 10^{m_2}+b_2,
\qquad
G:=b_1b_2,
\]

\[
N:=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
A:=a_1 10^{n_2}+a_2,
\]

\[
T:=10^{m_3},
\qquad
C:=10^{d_3}A.
\]

因为

\[
n_3=m_3+d_3,
\]

完整 numerator / denominator word 可写为

\[
\boxed{
\alpha=TC+a_3,
\qquad
\beta=TQ+b_3.
}
\]

原题 exact condition 为

\[
\boxed{
\frac{\alpha}{\beta}
=
\mathcal R
:=
\sqrt{
\frac{N}{G^2}+\frac{a_3^2}{b_3^2}
}.
}
\]

这些全部属于 **ORIGINAL / DEFINITIONAL**。

---

# 3. SGR-9 dependency DAG: old presentation

SGR-9 原 ledger 的逆向依赖大致为

\[
\boxed{
\begin{array}{c}
\text{Original DD candidate}\\
\Downarrow\\
\text{frozen DD frontier}\\
\Downarrow\\
10S+11\le n_3,\quad d_3\le5S\\
\Downarrow\\
m_3\ge5S+11\\
\Downarrow\\
\kappa,\ h,\ A_\kappa,\ B_\kappa,\ c\\
\Downarrow\\
F_-\leftrightarrow J^\sharp,\quad F_+\leftrightarrow K^\sharp\\
\Downarrow\\
B_\kappa\mid F_-,
\quad
A_\kappa\mid F_+\\
\Downarrow\\
u,v,\quad uv=Nc^2,\quad v-u=2ha_3\\
\Downarrow\\
v_5(F_-)=v_5(F_+)\\
\Downarrow\\
2m_3\le9S+9\\
\Downarrow\\
2m_3\ge10S+22\\
\Downarrow\\
\bot.
\end{array}}
\]

这个 presentation 容易给人一种印象：orientation、old Hensel resonance、Exact-Lift factor roots 都是不可替代输入。

本轮证明这不是 intrinsic dependency DAG。

---

# 4. Hidden inherited nodes found by the audit

除了 prompt 中列出的 I1–I8，SGR-9 实际还暗读以下节点。

## H0. Tail-weight integrality

SGR-9 使用

\[
\boxed{
\kappa=\frac{TQG}{b_3}\in\mathbf Z_{>0}.
}
\]

这不是单纯“定义”：整数性本身需要证明。

**原 ledger 状态：** inherited / hidden.  
**本轮状态：** **REPROVED LOCALLY**。

---

## H1. Tail-weight size window

由 \(b_3\) 恰有 \(m_3\) 位：

\[
10^{m_3-1}\le b_3<10^{m_3}=T,
\]

从而

\[
\boxed{
QG<\kappa\le10QG.
}
\]

**状态：** **ORIGINAL + DERIVED**。

---

## H2. Coprime source normalization

令

\[
h=\gcd(\kappa,G),
\]

\[
A_\kappa=\frac{\kappa}{h},
\qquad
D=\frac{G}{h},
\qquad
B_\kappa=\frac{\kappa+2G}{h}=A_\kappa+2D.
\]

则

\[
\boxed{
\gcd(A_\kappa,D)=1,
}
\]

\[
\boxed{
\gcd(A_\kappa,B_\kappa)
=
\gcd(A_\kappa,2)\in\{1,2\}.
}
\]

**状态：** **DEFINITIONAL / ELEMENTARY**。

---

## H3. Exact factor sum

SGR-9 的 resonance 实际还读取

\[
\boxed{
F_-+F_+=2GA10^{n_3}.
}
\]

这在旧 presentation 中来自 near-square factor pair；本轮重新从 canonical factorization 直接推出。

**状态：** **REPROVED LOCALLY**。

---

# 5. New Lemma 1 — Independent tail-weight integrality

## Lemma DIA-DD-1

对任一 original candidate，特别对任一 DD candidate，

\[
\boxed{
b_3\mid TQG.
}
\]

因此

\[
\boxed{
\kappa:=\frac{TQG}{b_3}\in\mathbf Z_{>0}.
}
\]

### Proof

令

\[
q=\operatorname{lcm}(b_1,b_2,b_3),
\qquad
y_i=\frac{a_iq}{b_i}.
\]

由原题

\[
\mathcal R=\frac{\alpha}{\beta}\in\mathbf Q
\]

且

\[
(q\mathcal R)^2=y_1^2+y_2^2+y_3^2\in\mathbf Z.
\]

有理数的平方若为整数，则该有理数本身为整数。故存在

\[
H=q\mathcal R\in\mathbf Z_{>0},
\]

满足

\[
H^2=y_1^2+y_2^2+y_3^2.
\]

现在固定任意素数 \(p\)，设

\[
e_i=v_p(b_i),
\qquad
e_3=e>0.
\]

我们证明 \(p^e\mid TQG\)。

### Case 1

若

\[
e\le\max(e_1,e_2),
\]

则 \(p^e\) 已整除 \(b_1\) 或 \(b_2\)，所以

\[
p^e\mid G=b_1b_2.
\]

### Case 2

若

\[
e>\max(e_1,e_2),
\]

则 \(e=v_p(q)\) 且第三分母在 \(p\) 上是唯一最大者。

由 \(\gcd(a_3,b_3)=1\)，

\[
p\nmid a_3,
\]

故

\[
p\nmid y_3=\frac{a_3q}{b_3}.
\]

而 \(e>e_1,e_2\) 给出

\[
p\mid y_1,\qquad p\mid y_2.
\]

于是模 \(p\)

\[
H^2
=
y_1^2+y_2^2+y_3^2
\equiv y_3^2\not\equiv0.
\]

所以

\[
p\nmid H.
\]

因此有理数

\[
\mathcal R=\frac Hq
\]

的既约分母在 \(p\) 上恰有指数 \(e\)。

另一方面

\[
\mathcal R=\frac{\alpha}{\beta}.
\]

既约分母必整除任一表示中的 denominator \(\beta\)，故

\[
p^e\mid\beta.
\]

但

\[
\beta=TQ+b_3
\]

且

\[
p^e\mid b_3,
\]

所以

\[
p^e\mid TQ.
\]

两种情况都给出

\[
p^e\mid TQG.
\]

逐素数合并：

\[
b_3\mid TQG.
\]

证毕。

### Status

\[
\boxed{\textbf{PROVED — NEW LOCAL REPROOF}.}
\]

### Consequence

因为 \(b_3\) 有 \(m_3\) 位，

\[
\boxed{
QG<\kappa\le10QG.
}
\]

因此 SGR-9 中 \(\kappa\) 的整数性不再属于 legacy kernel。

---

# 6. New Lemma 2 — Independent denominator normalization

令

\[
h=\gcd(\kappa,G),
\quad
A_\kappa=\kappa/h,
\quad
D=G/h.
\]

由

\[
\kappa b_3=TQG
\]

得到

\[
A_\kappa b_3=TQD.
\]

而

\[
\gcd(A_\kappa,D)=1.
\]

故

\[
\boxed{
A_\kappa\mid TQ.
}
\]

定义

\[
\boxed{
c:=\frac{TQ}{A_\kappa}\in\mathbf Z_{>0}.
}
\]

于是

\[
\boxed{
b_3=cD.
}
\]

再令

\[
\boxed{
B_\kappa=A_\kappa+2D
=\frac{\kappa+2G}{h}.
}
\]

全部仅使用 Lemma DIA-DD-1 与 gcd normalization。

### Status

\[
\boxed{\textbf{PROVED — REPROVED LOCALLY}.}
\]

---

# 7. New Lemma 3 — Canonical oriented DD factorization without SGR-8 orientation

这是本轮最重要的 dependency deletion。

## 7.1 Construct the integer center directly

由 original sphere equation：

\[
\mathcal R^2
=
\frac N{G^2}
+
\frac{a_3^2}{b_3^2}.
\]

定义

\[
\boxed{
W_3:=h b_3\mathcal R.
}
\]

它首先是正有理数。

利用

\[
G=hD,
\qquad
b_3=cD,
\]

得到

\[
\begin{aligned}
W_3^2
&=
h^2b_3^2\mathcal R^2\\
&=
h^2b_3^2\frac N{G^2}
+h^2a_3^2\\
&=
Nc^2+h^2a_3^2.
\end{aligned}
\]

右端为整数。

因为 \(W_3\in\mathbf Q_{>0}\) 且 \(W_3^2\in\mathbf Z\)，所以

\[
\boxed{
W_3\in\mathbf Z_{>0}.
}
\]

又因

\[
Nc^2>0,
\]

有

\[
W_3>ha_3.
\]

定义

\[
\boxed{
u:=W_3-ha_3,
\qquad
v:=W_3+ha_3.
}
\]

于是

\[
\boxed{
u,v\in\mathbf Z_{>0},
\qquad
u<v.
}
\]

并且

\[
\boxed{
uv=Nc^2,
}
\]

\[
\boxed{
v-u=2ha_3.
}
\]

这已经给出 orientation：

\[
\boxed{
\text{minus factor = the smaller positive recovery factor }u,
\quad
\text{plus factor = the larger factor }v.
}
\]

这里完全没有调用：

- gap Vieta roots；
- \(J^\sharp,K^\sharp\)；
- Hensel branch sign；
- SGR-8 conjugate numerator negativity。

---

## 7.2 Define canonical source factors

定义

\[
\boxed{
F_-^{\rm can}:=B_\kappa u,
\qquad
F_+^{\rm can}:=A_\kappa v.
}
\]

于是

\[
\boxed{
B_\kappa\mid F_-^{\rm can},
\qquad
A_\kappa\mid F_+^{\rm can}
}
\]

成为定义的直接后果，不再是需要 old source theorem 支持的 divisibility。

以下省略 superscript `can`。

---

## 7.3 Exact factor sum

先注意

\[
\beta=TQ+b_3
=
c(A_\kappa+D).
\]

且

\[
W_3
=
hb_3\mathcal R
=
cG\mathcal R.
\]

所以

\[
(A_\kappa+D)W_3
=
G\beta\mathcal R
=
G\alpha.
\]

因此

\[
\begin{aligned}
F_-+F_+
&=
(A_\kappa+2D)(W_3-ha_3)
+A_\kappa(W_3+ha_3)\\
&=
2(A_\kappa+D)W_3-2Dha_3\\
&=
2G\alpha-2Ga_3\\
&=
2GTC\\
&=
\boxed{2GA10^{n_3}}.
\end{aligned}
\]

---

## 7.4 Exact factor product

由

\[
TQ=cA_\kappa,
\qquad
TQ+2b_3=cB_\kappa,
\]

以及 \(uv=Nc^2\)，

\[
\begin{aligned}
F_-F_+
&=
A_\kappa B_\kappa uv\\
&=
A_\kappa B_\kappa Nc^2\\
&=
\boxed{
NTQ(TQ+2b_3).
}
\end{aligned}
\]

因此 canonical pair 与历史 near-square factor pair 保存完全相同的 sum/product arithmetic；但最终 proof 不需要识别它们与 \(J^\sharp,K^\sharp\) 的历史命名。

### Status

\[
\boxed{\textbf{PROVED — CANONICAL REPLACEMENT}.}
\]

### Dependency consequence

历史节点

\[
F_-\leftrightarrow J^\sharp,
\qquad
F_+\leftrightarrow K^\sharp
\]

在最短 DD closure DAG 中：

\[
\boxed{\textbf{REDUNDANT}.}
\]

---

# 8. Weak \(5\)-adic resonance can be reproved without Hensel

SGR-9 真正需要的不是完整 old double resonance theorem，而仅是

\[
v_5(F_-)=v_5(F_+).
\]

下面从 terminal-height + canonical factors 直接证明。

## Lemma DIA-DD-4 — Weak top \(5\)-resonance

假设

\[
\boxed{
m:=m_3\ge5S+11.
}
\tag{LH}
\]

则 canonical factors 满足

\[
\boxed{
v_5(F_-)=v_5(F_+).
}
\]

### Step 1: source valuations are \(O(S)\)

记

\[
k=v_5(\kappa),
\qquad
f=v_5(\kappa+2G).
\]

由于

\[
Q<10^S,
\qquad
G<10^S,
\qquad
\kappa\le10QG<10^{2S+1},
\]

并且

\[
\kappa+2G<11QG<11\cdot10^{2S},
\]

有

\[
\boxed{
k,f\le3S+3.
}
\]

再记

\[
H=v_5(h),
\quad
a=v_5(A_\kappa),
\quad
b=v_5(B_\kappa).
\]

则

\[
k=H+a,
\qquad
f=H+b,
\]

所以

\[
a,b\le3S+3.
\]

同时 \(h\mid G<10^S\)，而

\[
5^{2S}>10^S,
\]

故

\[
\boxed{
H\le2S-1.
}
\]

---

## Step 2: terminal height forces \(5\mid c\)

令

\[
q_5=v_5(Q).
\]

由

\[
c=\frac{TQ}{A_\kappa}
\]

得到

\[
v_5(c)=m+q_5-a.
\]

利用 \(m\ge5S+11\) 与 \(a\le3S+3\)：

\[
\boxed{
v_5(c)\ge2S+8>0.
}
\]

所以

\[
5\mid c\mid b_3.
\]

原题逐块既约性给出

\[
\gcd(a_3,b_3)=1,
\]

故

\[
5\nmid a_3.
\]

由

\[
v-u=2ha_3
\]

得到

\[
\boxed{
v_5(v-u)=H.
}
\tag{8.1}
\]

---

## Step 3: unequal factor valuations are impossible

记

\[
x=v_5(u),
\qquad
y=v_5(v).
\]

则

\[
v_5(F_-)=b+x,
\qquad
v_5(F_+)=a+y.
\]

假设二者不等。

由

\[
F_-+F_+=2GA10^{n_3}
\]

知

\[
v_5(F_-+F_+)\ge n_3.
\]

当两个加数的 \(5\)-进赋值不相等时，和的赋值恰为较小者，所以

\[
b+x\ge n_3,
\qquad
a+y\ge n_3.
\]

DD 中 \(d_3\ge1\)，故

\[
n_3=m+d_3\ge5S+12.
\]

因此

\[
x\ge n_3-b\ge2S+9,
\]

\[
y\ge n_3-a\ge2S+9.
\]

于是

\[
v_5(v-u)\ge\min(x,y)\ge2S+9.
\]

但 (8.1) 给出

\[
v_5(v-u)=H\le2S-1.
\]

矛盾。

所以

\[
\boxed{
v_5(F_-)=v_5(F_+).
}
\]

证毕。

### Status

\[
\boxed{
\textbf{PROVED — old double-Hensel resonance removed from final DAG}.
}
\]

### Important consequence

以下全部不再需要：

- projected \(5\)-adic phase；
- source Hensel branch；
- higher Hensel digits；
- old \(\mu,\nu\) resonance formula；
- \(2\)-adic resonance。

---

# 9. Independent quotient valuation overload

继续在

\[
m\ge5S+11
\]

下工作。

记

\[
x=v_5(u),
\quad
y=v_5(v),
\]

\[
H=v_5(h),
\quad
a=v_5(A_\kappa),
\quad
b=v_5(B_\kappa).
\]

由 weak resonance：

\[
b+x=a+y.
\tag{9.1}
\]

由

\[
uv=Nc^2
\]

与

\[
v_5(c)=m+q_5-a
\]

得到

\[
x+y
=
v_5(N)+2m+2q_5-2a.
\tag{9.2}
\]

另一方面

\[
v_5(v-u)=H.
\]

我们证明

\[
\boxed{
x+y\le2H+a+b.
}
\tag{9.3}
\]

### 若 \(x\ne y\)

则

\[
H=v_5(v-u)=\min(x,y).
\]

由 (9.1)，

\[
x-y=a-b.
\]

所以较大的那个赋值相对 \(H\) 的 excess 至多 \(|a-b|\le a+b\)，故

\[
x+y\le2H+a+b.
\]

### 若 \(x=y\)

(9.1) 给出 \(a=b\)。

而

\[
\gcd(A_\kappa,B_\kappa)\mid2
\]

说明

\[
\min(a,b)=0,
\]

故

\[
a=b=0.
\]

又

\[
v_5(v-u)=H\ge x,
\]

所以

\[
x+y=2x\le2H.
\]

(9.3) 仍成立。

将 (9.2) 代入：

\[
v_5(N)+2m+2q_5
\le
2H+3a+b.
\tag{9.4}
\]

又因为

\[
k=H+a,
\qquad
f=H+b,
\qquad
\min(a,b)=0,
\]

分两种情况：

- \(a=0\) 时
  \[
  2H+3a+b=2H+b\le3(H+b)=3f;
  \]
- \(b=0\) 时
  \[
  2H+3a+b=2H+3a\le3(H+a)=3k.
  \]

所以

\[
2H+3a+b
\le
3\max(k,f).
\]

由

\[
k,f\le3S+3
\]

得到

\[
v_5(N)+2m+2q_5
\le9S+9.
\]

丢掉非负项：

\[
\boxed{
2m\le9S+9.
}
\tag{9.5}
\]

而 LH 给出

\[
\boxed{
2m\ge10S+22.
}
\tag{9.6}
\]

矛盾。

因此：

\[
\boxed{
\text{不存在满足 LH 的 original DD candidate.}
}
\]

### Status

\[
\boxed{\textbf{PROVED}.}
\]

---

# 10. Provenance classification table

| Node | Statement / role | Old provenance | Audit class | Final status |
|---|---|---|---|---|
| O1 | original concatenation, positivity, digit lengths | 原题 | A | **PROVED / ORIGINAL** |
| O2 | \(\gcd(a_i,b_i)=1\) | 原题 | A | **PROVED / ORIGINAL** |
| O3 | integer sphere \(q\mathcal R=H\) | SGR/Exact common layer | B / locally checkable | **PROVED** |
| H0 | \(\kappa=TQG/b_3\in\mathbb Z\) | historical tail normalization | C | **PROVED anew** |
| H1 | \(QG<\kappa\le10QG\) | digit bound | A/C | **DERIVED** |
| H2 | \(h,A_\kappa,D,B_\kappa\) gcd normalization | definitions | A | **PROVED** |
| I7 | \(c=TQ/A_\kappa\in\mathbb Z,\ b_3=cD\) | SGR-8 / old denominator recovery | C | **PROVED anew** |
| I8 | \(uv=Nc^2,\ v-u=2ha_3\) | SGR-8 / root inversion | C | **PROVED anew** |
| I5 | \(F_-\leftrightarrow J^\sharp,\ F_+\leftrightarrow K^\sharp\) | SGR-8 orientation | — | **REDUNDANT** |
| I6 | \(B_\kappa\mid F_-,\ A_\kappa\mid F_+\) | SGR-8 source theorem | C/A | **DEFINITIONAL after canonical replacement** |
| H3 | \(F_-+F_+=2GA10^{n_3}\) | old near-square factors | C | **PROVED anew** |
| I4 | \(v_5(F_-)=v_5(F_+)\) | old top double resonance | C | **PROVED anew in weak form** |
| I2 | \(d_3\le5S\) | historical DD squarefree gap | D historically | — | **REDUNDANT as separate final input** |
| I3-upper | \(n_3\le11S+3\) | historical DD top window | D historically | — | **REDUNDANT** |
| I3-lower | \(n_3\ge10S+11\) on surviving frontier | historical DD reduction | D | compressed into LH | **LEGACY-DEPENDENT** |
| I1 | only surviving DD frontier is top chamber | historical DD reduction | D | compressed into LH | **LEGACY-DEPENDENT** |
| LH | every actual DD candidate must satisfy \(m_3\ge5S+11\) | consequence of I1 + I2 + I3-lower | D | final kernel | **LEGACY-DEPENDENT / OPEN FOR INDEPENDENT REPROOF** |

---

# 11. Why \(d_3\le5S\) is no longer a separate final obligation

SGR-9 原 proof 使用

\[
10S+11\le n_3,
\qquad
d_3\le5S
\]

来推出

\[
m_3=n_3-d_3\ge5S+11.
\]

但 terminal valuation proof 之后从未再次读取 \(d_3\) 或 \(n_3\) upper bound。

因此 independence DAG 不应保留比需要更强的两个 theorem。

正确压缩为：

\[
\boxed{
\mathrm{LH}:
\quad
\text{original DD candidate}
\Longrightarrow
m_3\ge5S+11.
}
\]

于是：

- \(d_3\le5S\) 不再是 standalone final dependency；
- \(n_3\le11S+3\) 完全删除；
- \(m_3\le6S+2\) 完全删除；
- extreme asymmetry 完全删除；
- near-\(S\)-unit 完全删除；
- top \(2\)-adic resonance 完全删除。

这不是说历史证明中从未使用这些东西，而是说它们现在至多属于 LH 的 provenance 内部，而不属于 SGR-9 terminal proof spine。

---

# 12. Minimal legacy kernel

最终只剩：

\[
\boxed{
K_{\rm legacy}
=
\{\mathrm{LH}\}.
}
\]

## LH — Minimal DD Terminal-Height Localization

### Precise statement

令

\[
S=m_1+m_2.
\]

若存在一个 original candidate 且属于 DD chamber，则 frozen pre-SGR-9 exhaustive DD reduction 强制

\[
\boxed{
m_3\ge5S+11.
}
\]

### Exact hypotheses

只允许：

1. original exact concatenation equation；
2. \(a_i,b_i>0\)；
3. \(\gcd(a_i,b_i)=1\)；
4. genuine decimal digit lengths；
5. DD conditions
   \[
   s_3>0,\qquad s_2+s_3>0.
   \]

不允许把 “已位于 top chamber” 本身作为额外假设，否则该 lemma 将失去 exhaustiveness 内容。

### Why it is still legacy-dependent

当前可回查材料一致声称：

\[
\text{DD 的唯一 surviving open core}
=
\{10S+11\le n_3\le11S+3,\ d_3\le5S,\ldots\}.
\]

但是当前 Strict-Layer 自己的独立文件没有重新给出：

\[
\boxed{
\text{所有 }n_3\le10S+10
\text{ 的 DD 原题候选为何已经被排除}
}
\]

的完整自包含 proof chain。

同时，旧

\[
d_3\le5S
\]

的证明依赖 historical DD squarefree-gap / tail-certificate machinery；本轮没有为了复制旧 DD 体系而重新建立整套 theorem，因为 terminal proof 只读取最终的 \(m_3\) lower bound。

因此不能把 LH 误标成 Class B。

### Status

\[
\boxed{\textbf{LEGACY-DEPENDENT / OPEN}.}
\]

### Next exact target

下一轮若要达到 DIA-1A，只需要独立证明：

\[
\boxed{
\textbf{DD Height Localization Lemma:}
\qquad
DD\Longrightarrow m_3\ge5S+11.
}
\]

允许证明更弱但足以与

\[
2m_3\le9S+9
\]

冲突的版本；实际上 terminal contradiction 只要求

\[
\boxed{
2m_3>9S+9.
}
\]

所以最小可替代目标甚至是：

\[
\boxed{
DD\Longrightarrow
m_3>\frac{9S+9}{2}.
}
\]

这比历史 \(5S+11\) 更弱，可能显著减少下一轮重建工作。

---

# 13. Deleted legacy machinery

以下历史结构在新的 final DD dependency DAG 中均已证明为不必要。

## 13.1 Completely removed

- ordinary near-square spacing；
- post-deflation \(J=M-Y\)；
- \(J^\sharp,K^\sharp\) prime-to-\(10\) quadratic；
- projected Hensel phase；
- source higher Hensel digits；
- \(2\)-adic double resonance；
- near-\(S\)-unit；
- residual divisor supply；
- extreme denominator asymmetry；
- square-spacing campaign terminal route；
- resultant coupling；
- normalized square as an independent gate；
- quadratic reciprocity gate；
- Pell / squarefree finite-state route；
- Vieta descent。

全部状态：

\[
\boxed{\textbf{REDUNDANT FOR FINAL DD CLOSURE}.}
\]

---

## 13.2 Historical orientation theorem

SGR-8 证明了：

\[
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp,
\qquad
J^\sharp<K^\sharp,
\]

并通过 conjugate third numerator \(<0\) 固定 source orientation。

该 theorem 本身仍是正确的 SGR result；本审计没有否定它。

但新的 canonical construction

\[
u=W_3-ha_3,
\qquad
v=W_3+ha_3
\]

直接给出

\[
0<u<v.
\]

因此：

\[
\boxed{
\text{SGR-8 orientation theorem is valid but not a dependency of the shortest DD closure.}
}
\]

状态：

\[
\boxed{\textbf{REDUNDANT}.}
\]

---

## 13.3 Old double-Hensel resonance

完整 old theorem 比 SGR-9 真正所需的结论强得多。

新的 Lemma DIA-DD-4 仅使用：

- exact factor sum；
- terminal height；
- source divisor size；
- \(5\mid c\)；
- third-block reducedness；
- \(v-u=2ha_3\)。

即可得到

\[
v_5(F_-)=v_5(F_+).
\]

因此 old Hensel machinery 从 final DAG 中删除。

状态：

\[
\boxed{\textbf{REDUNDANT}.}
\]

---

# 14. Circularity audit

## 14.1 Historical potential cycle

旧 presentation 容易形成如下视觉依赖：

\[
\text{orientation}
\to
\text{source factor labels}
\to
\text{phase/resonance}
\to
\text{root recovery}
\to
\text{orientation}.
\]

严格检查后，没有证据表明历史证明真的逻辑循环；但这种 presentation 使 audit 非常脆弱，因为 factor labels 与 source root labels 混在一起。

新的 construction 完全删除该问题：

\[
\boxed{
W_3
\to
u=W_3-ha_3
<
v=W_3+ha_3
\to
(F_-,F_+).
}
\]

orientation 只依赖 positivity。

---

## 14.2 Resonance circularity check

新的 weak resonance 证明使用 LH，但不使用 quotient-overload conclusion。

顺序为：

\[
\mathrm{LH}
\to
5\mid c
\to
v_5(v-u)=H
\]

以及

\[
\mathrm{LH}
+
F_-+F_+
\to
v_5(F_-)=v_5(F_+).
\]

然后才使用 resonance 推出

\[
2m_3\le9S+9.
\]

所以没有

\[
\text{resonance}\to\text{height}\to\text{resonance}
\]

循环。

---

## 14.3 Tail-weight circularity check

\(\kappa\in\mathbf Z\) 的新证明只使用：

- original exact candidate；
- lcm sphere lift；
- reducedness；
- denominator word。

不使用：

- DD top reduction；
- resonance；
- \(c\)；
- \(u,v\)；
- SGR-9 contradiction。

因此没有 denominator-normalization cycle。

---

## 14.4 Height node

LH 在新 DAG 中是一个 root-side inherited theorem：

\[
\text{Original DD candidate}
\Longrightarrow
\mathrm{LH}.
\]

它不允许从 SGR-9 closure 本身反推。

本报告没有发现现有文件显式犯这种 circularity；真正问题只是 LH 尚未被独立重证。

---

# 15. Hidden hypotheses audit

SGR-9 terminal calculation 所需全部 side conditions如下。

| Hypothesis | Source | Status |
|---|---|---|
| \(a_i,b_i>0\) | 原题 | ORIGINAL |
| \(\gcd(a_i,b_i)=1\) | 原题 | ORIGINAL |
| \(m_i,n_i\ge1\) | digit definition | ORIGINAL |
| \(S=m_1+m_2\ge2\) | digit definition | DERIVED |
| DD gives \(d_3\ge1\) | chamber definition | ORIGINAL/DEFINITIONAL |
| \(\kappa\in\mathbb Z_{>0}\) | formerly hidden | **REPROVED** |
| \(h,A_\kappa,B_\kappa,D\in\mathbb Z_{>0}\) | gcd normalization | DERIVED |
| \(\gcd(A_\kappa,B_\kappa)\mid2\) | normalization | DERIVED |
| \(c\in\mathbb Z_{>0}\) | tail normalization | **REPROVED** |
| \(u,v\in\mathbb Z_{>0}\) | canonical sphere factorization | **REPROVED** |
| \(u<v\) | positivity | **REPROVED** |
| factor sum/product | exact word + sphere | **REPROVED** |
| weak 5-resonance | local p-adic lemma | **REPROVED** |
| \(m_3\ge5S+11\) | pre-SGR-9 exhaustive DD reduction | **LEGACY-DEPENDENT** |

没有发现 terminal proof 暗中要求：

- \(\gcd(u,v)=1\)；
- \(\gcd(u,v)\mid2h\)；
- \(Y>0\)；
- near-\(S\)-unit；
- \(2\)-adic resonance；
- denominator asymmetry；
- generic nondegenerate resultant；
- fixed primitive core。

---

# 16. New minimal DD proof spine

删除旧 presentation 后，DD terminal proof 可压成：

\[
\boxed{
\begin{array}{c}
\text{Original DD candidate}\\[1mm]
\Downarrow\\
\textbf{Lemma 1: sphere-denominator tail-weight integrality}\\
b_3\mid TQG,\quad \kappa\in\mathbf Z\\[1mm]
\Downarrow\\
\textbf{Lemma 2: canonical denominator normalization}\\
c\in\mathbf Z,\quad b_3=cD\\[1mm]
\Downarrow\\
\textbf{Lemma 3: canonical positive factorization}\\
uv=Nc^2,\quad v-u=2ha_3,\\
F_-=B_\kappa u,\quad F_+=A_\kappa v,\\
F_-+F_+=2GA10^{n_3}\\[1mm]
\Downarrow\\
\boxed{\mathrm{LH}:m_3\ge5S+11}
\qquad\text{(only legacy node)}\\[1mm]
\Downarrow\\
\textbf{Lemma 4: elementary weak }5\textbf{-resonance}\\
v_5(F_-)=v_5(F_+)\\[1mm]
\Downarrow\\
\textbf{Lemma 5: quotient valuation overload}\\
2m_3\le9S+9\\[1mm]
\Downarrow\\
2m_3\ge10S+22\\[1mm]
\Downarrow\\
\bot.
\end{array}}
\]

若把 Lemma 2 吸收到 Lemma 1，把 weak resonance 与 overload 合并成一个 \(5\)-adic terminal lemma，则 DD-specific spine 可进一步压成 **3 个复合 lemma + LH**。

为了 audit 清晰，本报告保留 5 个较小 lemma。

---

# 17. Minimal independent theorem content actually needed

把 constants 进一步抽象后，terminal proof 并不真正需要历史精确 bound

\[
m_3\ge5S+11.
\]

它只需要足以同时保证：

1. \(5\mid c\)；
2. unequal factor valuations 与
   \[
   v_5(v-u)=v_5(h)
   \]
   冲突；
3. terminal upper bound
   \[
   2m_3\le9S+9
   \]
   被打破。

其中最强要求是第三项：

\[
\boxed{
2m_3>9S+9.
}
\]

因此一个完全独立的未来 replacement lemma 只需证明：

\[
\boxed{
DD
\Longrightarrow
m_3>\frac{9S+9}{2}.
}
\tag{MH}
\]

历史

\[
m_3\ge5S+11
\]

比 (MH) 强。

这说明 independence repair 的真正 frontier 已经从

\[
\text{整个 old DD top machinery}
\]

压成：

\[
\boxed{
\textbf{one minimal DD denominator-height inequality}.
}
\]

---

# 18. Dependency certificate

## 18.1 Certified independent nodes

本报告正式认证以下节点不再依赖 External Exact-Lift theorem black box：

\[
\boxed{
\begin{aligned}
&\kappa\in\mathbf Z,\\
&QG<\kappa\le10QG,\\
&c\in\mathbf Z,\quad b_3=cD,\\
&u,v\in\mathbf Z_{>0},\quad u<v,\\
&uv=Nc^2,\\
&v-u=2ha_3,\\
&F_-=B_\kappa u,\quad F_+=A_\kappa v,\\
&F_-+F_+=2GA10^{n_3},\\
&F_-F_+=NTQ(TQ+2b_3),\\
&v_5(F_-)=v_5(F_+)\quad\text{under LH},\\
&2m_3\le9S+9\quad\text{under LH}.
\end{aligned}}
\]

---

## 18.2 Certified deleted nodes

以下不属于 final DD theorem dependency：

\[
\boxed{
\begin{aligned}
&J^\sharp/K^\sharp\text{ orientation},\\
&\text{old Hensel phase},\\
&\text{higher Hensel digits},\\
&2\text{-adic resonance},\\
&\text{near-}S\text{-unit},\\
&\text{residual supply},\\
&\text{extreme asymmetry},\\
&\text{ordinary square spacing},\\
&\text{resultant},\\
&\text{Pell/descent}.
\end{aligned}}
\]

状态统一为：

\[
\boxed{\textbf{REDUNDANT}.}
\]

---

## 18.3 Remaining certificate failure

唯一无法签署 independence 的节点：

\[
\boxed{
\mathrm{LH}:
\quad
DD\Longrightarrow m_3\ge5S+11.
}
\]

因此：

\[
\boxed{
\textbf{DD is not yet fully independently closed in SGR/Strict-Layer.}
}
\]

但同时：

\[
\boxed{
\textbf{SGR-9 terminal closure mechanism itself is independently reconstructed.}
}
\]

换言之，legacy dependence 已不在 SGR-9 的核心 arithmetic，而只在“为什么所有 DD candidate 必须先到达这个高度”这一 pre-terminal localization。

---

# 19. Final grade

\[
\boxed{
\textbf{DIA-1B — MINIMAL LEGACY KERNEL ISOLATED}
}
\]

理由：

1. 没有发现 SGR-9 terminal contradiction 的实质缺口；
2. 没有发现不可消除 circularity；
3. hidden hypothesis \(\kappa\in\mathbb Z\) 已被独立修复；
4. orientation、source divisibility、canonical factors、weak \(5\)-resonance 均已去 legacy 化；
5. final legacy kernel 严格压到一个 statement：
   \[
   K_{\rm legacy}=\{\mathrm{LH}\};
   \]
6. 只有独立重证 LH（或更弱的 (MH)）后，才可升级为
   \[
   \boxed{\textbf{DIA-1A — FULL DD INDEPENDENCE}}.
   \]

---

# 20. Proof-status ledger

## PROVED

- original sphere lift；
- new tail-weight integrality lemma；
- denominator normalization；
- canonical positive factorization；
- canonical source-factor sum/product；
- source orientation by positivity；
- weak \(5\)-adic resonance under LH；
- quotient valuation overload under LH；
- no-cycle property of the new terminal DAG。

## DERIVED

- \(QG<\kappa\le10QG\)；
- \(\gcd(A_\kappa,D)=1\)；
- \(\gcd(A_\kappa,B_\kappa)\in\{1,2\}\)；
- \(v_5(c)\ge2S+8\) under LH；
- \(v_5(v-u)=v_5(h)\) under LH；
- \(2m_3\le9S+9\) under LH。

## LEGACY-DEPENDENT

\[
\boxed{
\mathrm{LH}:
DD\Longrightarrow m_3\ge5S+11.
}
\]

## REDUNDANT

- old \(J^\sharp/K^\sharp\) orientation bridge；
- old source-Hensel branch；
- old \(2/5\) double-resonance theorem as a whole；
- \(2\)-adic resonance；
- near-\(S\)-unit；
- extreme denominator asymmetry；
- post-deflation divisor supply；
- square-spacing；
- resultant；
- Pell；
- descent；
- \(n_3\le11S+3\)；
- \(m_3\le6S+2\)；
- \(d_3\le5S\) as a standalone terminal input。

## FAILED

- 本轮未能从当前 independent SGR/Strict-Layer chain 重证 complete sub-terminal DD elimination；
- 因而未能证明 LH。

## OPEN

唯一 independence obligation：

\[
\boxed{
DD
\Longrightarrow
2m_3>9S+9.
}
\]

证明这个更弱 statement 已足以把本报告升级为 DIA-1A。

---

# 21. Final certificate in one line

\[
\boxed{
\text{SGR-9 的 arithmetic closure 已独立化；}
\quad
\text{DD 全独立性只差一个 pre-terminal height localization lemma。}
}
\]
