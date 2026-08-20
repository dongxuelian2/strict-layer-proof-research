# Strict Layer A1 — Resonant / Transition Reduced-Fraction Unit Exclusion Campaign

**文件名：** `strict_layer_A1_resonant_transition_reduced_fraction_unit_exclusion_campaign.md`  
**研究范围：** 三项十进制拼接平方和问题，Strict Layer，仅 `A1-only`  
**本轮主目标：** A1-SRUS 中的 exact resonance `R=0`，以及在 resonance 无法闭合时对 `d=0,1` transition 的最小后续审计。

---

# 1. Executive Summary

本轮没有证明

\[
\boxed{A_1=\varnothing}.
\]

因此 Strict Layer 仍未整体闭合：

\[
\boxed{DD=\varnothing,\qquad A_1\ \mathrm{OPEN}.}
\]

但本轮对当前最低维 frontier 做了实质压缩，并纠正了若干 prompt 中“可能是新 theorem”的候选。

最重要的结论如下。

## 1.1 Sharp Primitive Mantissa 不是新 theorem

prompt 建议优先证明

\[
0<D<Q_0,
\qquad
1<\frac{10^kP_1}{Q_0}<2.
\]

source audit 后确认：此前 exact-mantissa / moving-profile 报告已经冻结了更强结论

\[
\boxed{
10^{-k}<\frac{P_1}{Q_0}
<\left(1+\frac1{b_1}\right)10^{-k}
\le2\cdot10^{-k}.
}
\tag{SPM}
\]

等价地

\[
\boxed{
0<D<\frac{Q_0}{b_1}\le Q_0.
}
\tag{D-SHARP}
\]

所以本轮不把 SPM 重新计为 NEW PROVED；真正的新工作是把它第一次系统压进 resonance 的 sign / radial face / integer-margin geometry。

---

## 1.2 Resonance 被精确拆成两个 radial faces

在

\[
R=b_210^{n_3}-b_3=0
\]

下，冻结：

\[
\boxed{d=0,\quad \alpha=t=1,\quad v=10^{n_3}},
\]

\[
\boxed{n_2=2g+k},
\]

\[
\boxed{P_2=10^{n_3}M,\qquad P_3=N},
\]

\[
\boxed{g_2=u_010^{n_3},\qquad g_3=u_0},
\]

\[
\boxed{V=s\beta u_010^{n_3}}.
\]

令

\[
n:=n_2=2g+k,
\qquad
r:=\frac{P_3}{P_2}
=\frac{N}{10^{n_3}M}.
\]

则 continuous SRUS cone 等价于

\[
\boxed{10^{-n-1}<r<10^{-n+1}.}
\tag{RES-CONE-r}
\]

而两个 active face 精确为：

### Face A

\[
L_2\ge L_3
\iff
r\ge10^{-n},
\]

所以 surviving continuous state 必满足

\[
\boxed{10^{-n}\le r<10^{1-n}.}
\tag{RA}
\]

### Face B

\[
L_3>L_2
\iff
r<10^{-n},
\]

所以

\[
\boxed{10^{-n-1}<r<10^{-n}.}
\tag{RB}
\]

这比只写“一个 decade 的 cone”更适合与 resonance sign 联立。

---

## 1.3 NEW PROVED — Resonant Face Integer Margin

若 Face A 中存在任何整数 radial point，则最新 Smith-reduced Integer Margin

\[
\mathcal G_A=M10^{n_3}-N10^{n-1}\ge M
\]

在 primitive ratio 坐标中化为

\[
P_2-10^{n-1}P_3\ge \frac{P_2}{10^{n_3}}.
\]

除以 \(P_2\)：

\[
\boxed{
r\le10^{1-n}\left(1-10^{-n_3}\right).
}
\tag{RIM-A}
\]

Face B 中若存在 integer \(U\)，则

\[
\mathcal G_B=N10^n-M10^{n_3-1}\ge N,
\]

即

\[
10^nP_3-\frac{P_2}{10}\ge P_3.
\]

故

\[
\boxed{
r\ge\frac1{10(10^n-1)}.
}
\tag{RIM-B}
\]

所以 resonance 中一旦真正进入 Layer I survivor，两个 face 的 ratio window 被进一步收紧为：

\[
\boxed{
\text{Face A: }
10^{-n}\le r
\le10^{1-n}(1-10^{-n_3}),
}
\]

\[
\boxed{
\text{Face B: }
\frac1{10(10^n-1)}
\le r<10^{-n}.
}
\]

这是本轮新的 exact radial sharpening；它直接读取 ordinary integer existence，而不仅是 continuous cone。

---

## 1.4 NEW PROVED — Resonant Sign–Face–Exponent Compression

定义

\[
\boxed{\kappa:=k-2g.}
\]

resonance 中

\[
S_R:=P_2+P_3-Q_0
=P_3-d_2,
\qquad d_2:=Q_0-P_2.
\]

且

\[
10^gH=b_2S_R.
\]

因此

\[
\boxed{\operatorname{sgn}S_R=\operatorname{sgn}H}.
\]

也就是：

\[
\boxed{
\text{plus}\iff S_R<0\iff P_3<d_2,
}
\]

\[
\boxed{
\text{minus}\iff S_R>0\iff P_3>d_2.
}
\]

source 已冻结

\[
\boxed{
\frac12<10^{2k}\frac{d_2}{Q_0}<2.532,
}
\tag{AXIS-GAP}
\]

以及

\[
\boxed{
\frac{P_2}{Q_0}>x_0:=\sqrt{96/101}.
}
\]

将这些与 Face A/B 的 ratio decade 联立，得到以下严格整数压缩。

### plus + Face A

Face A 给

\[
\frac{P_3}{Q_0}\ge x_0 10^{-n}.
\]

plus 给

\[
\frac{P_3}{Q_0}<2.532\,10^{-2k}.
\]

故

\[
10^{k-2g}<\frac{2.532}{x_0}<2.60.
\]

由于 \(\kappa\in\mathbf Z\)：

\[
\boxed{\text{plus + Face A}\Longrightarrow \kappa\le0.}
\tag{K-A+}
\]

若进一步使用 SPM 的 \(b_1\)-dependent upper bound，则

\[
\frac{P_1^2}{2P_2^2}
<
\frac{(1+1/b_1)^2}{2x_0^2}10^{-2k}.
\]

当 \(b_1\ge3\) 时系数严格小于 1，于是甚至

\[
\boxed{
\text{plus + Face A + }b_1\ge3
\Longrightarrow \kappa\le-1.
}
\tag{K-A+-STR}
\]

### plus + Face B

使用 Face B 的 continuous lower boundary

\[
\frac{P_3}{Q_0}>x_0 10^{-n-1}
\]

与 plus 的 \(P_3<d_2\)，得到

\[
10^\kappa<\frac{25.32}{x_0}<26,
\]

故

\[
\boxed{\text{plus + Face B}\Longrightarrow \kappa\le1.}
\tag{K-B+}
\]

### minus + Face A

minus 给

\[
\frac{P_3}{Q_0}>\frac12\,10^{-2k},
\]

Face A upper decade给

\[
\frac{P_3}{Q_0}<10^{1-n}.
\]

所以

\[
\frac12<10^{k-2g+1},
\]

故

\[
\boxed{\text{minus + Face A}\Longrightarrow \kappa\ge-1.}
\tag{K-A-}
\]

### minus + Face B

Face B 给

\[
\frac{P_3}{Q_0}<10^{-n},
\]

而 minus 给

\[
\frac{P_3}{Q_0}>\frac12\,10^{-2k}.
\]

故

\[
\frac12<10^{k-2g},
\]

从而

\[
\boxed{\text{minus + Face B}\Longrightarrow \kappa\ge0.}
\tag{K-B-}
\]

所以所有 resonance Layer-C survivors 已落入：

| resonance branch | necessary \(\kappa=k-2g\) |
|---|---:|
| plus + Face A | \(\kappa\le0\)；若 \(b_1\ge3\)，\(\kappa\le-1\) |
| plus + Face B | \(\kappa\le1\) |
| minus + Face A | \(\kappa\ge-1\) |
| minus + Face B | \(\kappa\ge0\) |

这比此前“primitive ratio 左右各宽一个 decade”明显更窄，但仍不是 finite \(\kappa\) theorem。

---

## 1.5 NEW PROVED — Resonant Reduced-Denominator GCD Overload

这是本轮最重要的新 exact algebraic splice。

resonance 中

\[
b_1=su,
\qquad
b_2=s\beta,
\qquad
m_2=g,
\qquad
\gcd(u,\beta)=1.
\]

由 defect definition

\[
H=b_2Q_0-b_110^gD
=s\beta Q_0-su10^gD
\]

以及

\[
10^gH=b_2S_R=s\beta S_R
\]

消去 \(H\)：

\[
\boxed{
u10^{2g}D
=
\beta(10^gQ_0-S_R).
}
\tag{RGCD-0}
\]

令

\[
\boxed{
h_R:=\gcd(10^{2g}D,\ 10^gQ_0-S_R).
}
\]

因为 \(\gcd(u,\beta)=1\)，(RGCD-0) 已经是一个 reduced fraction identity，严格得到

\[
\boxed{
u=rac{10^gQ_0-S_R}{h_R},
\qquad
\beta=rac{10^{2g}D}{h_R}.
}
\tag{RGCD-1}
\]

又 \(b_2=s\beta\) 恰为 \(g\) 位正整数，所以

\[
\beta\le b_2<10^g.
\]

因此

\[
\boxed{
h_R>10^gD.
}
\tag{RGCD-2}
\]

即：任何 resonant exact state 都要求

\[
\boxed{
\gcd(10^{2g}D,\ 10^gQ_0-S_R)
>
10^gD.
}
\tag{RGCD-OVERLOAD}
\]

这是一个非常强的 ordinary-integer necessary condition：resonance 不仅要求 \(S_R\) 有 decimal divisor，还要求两个明显不同来源的整数共享一个超过 \(10^gD\) 的 gcd。

目前尚未从 primitive sphere / SRUS margin 推出该 gcd 不可能，因此它是**新的 survivor normal-form condition，而非 closure**。

---

## 1.6 NEW DERIVED — Resonance 的精确 denominator recovery

(RGCD-1) 还给出：

\[
\boxed{
\frac u\beta
=
\frac{10^gQ_0-S_R}{10^{2g}D}
\quad\text{in lowest terms}.
}
\tag{RES-u-beta}
\]

因此 resonance denominator core \((u,\beta)\) 已不再是自由 pair；给定 primitive/defect state \((Q_0,D,S_R,g)\) 后，它们由一个 gcd 唯一恢复。

这比只保留

\[
L_R\mid S_R
\]

更强，因为它同时读取：

- leading defect \(D\)；
- resonance tail defect \(S_R\)；
- exact denominator reducedness \(\gcd(u,\beta)=1\)；
- \(b_2\) 的 digit length。

需要校准：不等式 (RGCD-2) 在 (RGCD-1) 已建立后，正是 \(\beta<10^g\) 的 primitive/defect-only 投影，因此它不是一个与 digit length 独立的新 gate。它的价值在于：\(\beta\) 已被消掉，条件现在只读取 \(D,Q_0,S_R,g\)，可直接与 sphere / radial margin 联立。

## 1.6.1 NEW PROVED — Resonant Integer Mantissa Normal Form

由

\[
J=L_R=\frac{10^g}{\gcd(10^g,\delta_\beta)}
\]

可知 \(J\mid10^g\)。令

\[
\boxed{\chi_R:=10^g/J.}
\]

按定义 \(\chi_R\mid\beta\)，写

\[
\beta=\chi_R\beta_R.
\]

再定义

\[
\boxed{c_R:=s\beta_R\in\mathbf Z_{>0}.}
\]

则 denominator block 被精确写成

\[
\boxed{b_2=s\beta=\frac{c_R}{J}10^g.}
\tag{IRMANT-1}
\]

因为 \(b_2\) 恰为 \(g\) 位：

\[
10^{g-1}\le b_2<10^g,
\]

所以

\[
\boxed{\frac J{10}\le c_R<J.}
\]

等价于整数范围

\[
\boxed{\lceil J/10\rceil\le c_R\le J-1.}
\tag{IRMANT-2}
\]

再由

\[
S_R=JZ,
\qquad
10^gH=b_2S_R,
\]

得到极简 exact defect pair：

\[
\boxed{S_R=JZ,\qquad H=c_RZ.}
\tag{IRMANT-3}
\]

所以 resonance 的真实 denominator mantissa不再是连续变量，而是

\[
\boxed{\frac{b_2}{10^g}=\frac{c_R}{J},\qquad \lceil J/10\rceil\le c_R<J.}
\]

这给出一个非常自然的 small-\(J\) / large-\(J\) 分裂：

- fixed \(J\) 时 \(c_R\) 只有至多 \(9J/10\) 个 ordinary integers；
- \(s\mid c_R\)，所以 fixed \(J\) 后 \(s,\beta_R\) 也只剩有限 divisor choices；
- \(J=2\) 时唯一 \(c_R=1\)，故
  \[
  \boxed{b_2=5\cdot10^{g-1},\quad H=Z,\quad S_R=2Z;}
  \]
- \(J=5\) 时 \(c_R\in\{1,2,3,4\}\)，故
  \[
  \boxed{b_2\in\{2,4,6,8\}\cdot10^{g-1}.}
  \]

这不是 resonance closure，因为 \(J\) 本身仍可随 state 增长；但它把“small residual decimal divisor” chamber 变成真正 finite mantissa states。

---

## 1.7 Resonance amplified divisor audit

prompt 建议把 strongest Smith divisor of \(H\) 经

\[
10^gH=b_2S_R
\]

放大成 \(S_R\) divisor。

这一方向 source audit 后的结论是：

- iterated Smith 已有
  \[
  H=s\beta^\sharp v^\sharp h_T^\sharp q
  \]
  的对应 strongest form；
- resonance 中 \(v=10^{n_3}\)，大部分新增 factor 与 \(b_2=s\beta\) 或 pure decimal factor发生系统 cancellation；
- 已冻结的 canonical decimal part最终正是
  \[
  \boxed{J=L_R>1,\qquad J\mid S_R.}
  \]

本轮没有得到一个对所有 resonance states 都严格大于 \(J\) 的 independent amplified divisor。

因此：

\[
\boxed{
\text{“再挖一个 uniform larger divisor of }S_R\text{” 本轮 FAILED.}
}
\]

正确的新 splice 是上一节的 reduced-denominator gcd overload，而不是重复 divisor hunting。

---

## 1.8 Resonance congruence与 \(\Delta_R\)

由

\[
J\mid S_R=P_2+P_3-Q_0
\]

和 primitive sphere：

\[
Q_0^2=P_1^2+P_2^2+P_3^2,
\]

得到

\[
Q_0\equiv P_2+P_3\pmod J,
\]

所以

\[
\boxed{
P_1^2\equiv2P_2P_3\pmod J.
}
\tag{RES-CONG}
\]

定义

\[
\boxed{\Delta_R:=P_1^2-2P_2P_3.}
\]

则

\[
\boxed{J\mid\Delta_R.}
\tag{DELTA-DIV}
\]

并且 exact factorization：

\[
\Delta_R
=S_R\bigl(S_R-2(P_2+P_3)\bigr).
\]

由于

\[
Q_0>|P_2-P_3|,
\]

可得

\[
|S_R|<2\min(P_2,P_3)<2(P_2+P_3),
\]

故第二因子始终为负，严格有

\[
\boxed{
\operatorname{sgn}\Delta_R=-\operatorname{sgn}S_R.
}
\]

也就是：

\[
\boxed{
\text{plus}\iff \Delta_R>0,
\qquad
\text{minus}\iff \Delta_R<0.
}
\]

这与 source 的 \(F=2P_2P_3-P_1^2\) factorization 完全一致。

但 \(|\Delta_R|\) 可以远大于 \(J\)，现有 bounds 不能推出

\[
0<|\Delta_R|<J.
\]

所以 prompt 候选的 “\(J\mid\Delta_R\) + magnitude closure” 本轮**没有完成**。

---

# 2. Source / Notation Audit

本轮以以下报告为 source of truth：

1. `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`；
2. `strict_layer_A1_double_euclidean_smith_gcd_terminal_campaign.md`；
3. `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`；
4. `strict_layer_A1_unified_moving_profile_terminal_campaign.md`；
5. 与上述 frozen core 一致的并行更新 `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`，仅吸收其已可独立核验的 radial-gap / integer-margin identities。

本轮没有引入外部数学定理作为 nonexistence dependency。

---

# 3. Frozen A1-SRUS State

primitive sphere：

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

exponents：

\[
\boxed{
m_2=g+d,
\qquad
n_2=2g+k+d,
\qquad
m_3=n_3+g.
}
\]

Smith chart：

\[
\boxed{
b_1=s\alpha u,
\quad
b_2=s\alpha\beta t,
\quad
b_3=s\beta v,
}
\]

with

\[
\boxed{
\gcd(\alpha,\beta)=1,
\quad
\gcd(u,\beta t)=1,
\quad
\gcd(\alpha t,v)=1.
}
\]

Full Smith–radial cancellation：

\[
\boxed{
g_2=u_0v,
\qquad
g_3=u_0\alpha t,
}
\]

\[
\boxed{
P_2=vM,
\qquad
P_3=\alpha tN,
}
\]

\[
\boxed{
C_2=M/u_0,
\qquad
C_3=N/u_0,
\qquad
u_0\mid M,N.
}
\]

radial gate：

\[
\boxed{
\frac U{u_0}
\in
K_{MN}
}
\]

且

\[
\boxed{
\gcd(U,V)=1.
}
\]

---

# 4. Exponent Dictionary

统一保留：

\[
\boxed{
n_2=2g+k+d.}
\]

定义 normalized decade offset：

\[
\boxed{
\ell_d:=n_3-(2g+k+d).
}
\]

则

\[
\boxed{
z:=10^{\ell_d}\frac MN}
\]

满足 Layer-C 必要条件

\[
\boxed{1/10<z<10.}
\]

resonance 中 \(d=0\)，所以

\[
\ell_0=n_3-(2g+k).
\]

---

# 5. Smith-Reduced Integer Margin — Frozen and Rechecked

Face A：

\[
\frac{10^{n_2-1}}M
\le
\frac U{u_0}
<
\frac{10^{n_3}}N.
\]

由

\[
MU\ge10^{n_2-1}u_0,
\]

\[
10^{n_3}u_0-NU\ge1,
\]

严格得

\[
\boxed{
u_0\left(M10^{n_3}-N10^{n_2-1}\right)\ge M.}
\]

因为 \(u_0\mid M\)，等价于 source 的

\[
\boxed{\mathcal G_A\ge M.}
\]

Face B 同理：

\[
\boxed{
u_0\left(N10^{n_2}-M10^{n_3-1}\right)\ge N.}
\]

这是本轮所有 Layer-I 攻击的 frozen lower bound。

---

# 6. Reduced Endpoint Margin — NEW PROVED General Lemma

设 endpoint 约分为

\[
\frac AB,
\qquad
\gcd(A,B)=1,
\]

且 radial fraction

\[
\frac U{u_0}
\]

为 lowest terms。

若两者不同，则 cross determinant 为非零整数：

\[
|UB-Au_0|\ge1.
\]

所以

\[
\boxed{
\left|
\frac U{u_0}-\frac AB
\right|
\ge
\frac1{u_0B}.
}
\tag{RF-MARGIN}
\]

应用到 decimal endpoint

\[
\frac{10^m}{X},
\]

其 reduced denominator 为

\[
\boxed{
X^\star:=\frac X{\gcd(X,10^m)}.
}
\]

于是任何 distinct denominator-\(u_0\) reduced fraction距离该 endpoint 至少

\[
\boxed{
\frac1{u_0X^\star}.
}
\]

这是 plain integer margin 的精化；当 \(X\) 有深 2/5 factors 时，\(X^\star\ll X\)，margin 可显著增大。

本轮尚未从 resonance exact arithmetic uniform 地证明 active endpoint 的 \(X^\star\) 足够小，所以这仍是 secondary Layer-I tool，而不是 closure。

## 6.1 NEW PROVED — Two-Sided Reduced-Endpoint / Farey Margin

还有一个比单端 (RF-MARGIN) 更强的版本。

若

\[
\frac AB<\frac xy<\frac CD
\]

三者均为 lowest terms，令 endpoint determinant

\[
\Delta_F:=CB-AD>0.
\]

则

\[
\frac xy-\frac AB\ge\frac1{By},
\qquad
\frac CD-\frac xy\ge\frac1{Dy}.
\]

相加并用

\[
\frac CD-\frac AB=\frac{\Delta_F}{BD}
\]

得到

\[
\boxed{y\ge\frac{B+D}{\Delta_F}.}
\tag{FAREY-2}
\]

这不要求 endpoints 是 Farey neighbors；\(\Delta_F=1\) 只是最强特例。

### Face A specialization

令

\[
a:=\gcd(M,10^{n_2-1}),
\qquad
b:=\gcd(N,10^{n_3}).
\]

active endpoints reduced 后 denominators 为

\[
B=M/a,
\qquad
D=N/b,
\]

且 determinant

\[
\Delta_F=\frac{M10^{n_3}-N10^{n_2-1}}{ab}
=\frac{\mathcal G_A}{ab}.
\]

因此，只要 \(U/u_0\) 严格位于两个 endpoints 之间：

\[
\boxed{
u_0\mathcal G_A\ge Mb+Na.}
\tag{FAREY-A}
\]

它严格加强 plain margin \(u_0\mathcal G_A\ge M\)。

### Face B specialization

令

\[
c:=\gcd(N,10^{n_3-1}),
\qquad
e:=\gcd(M,10^{n_2}).
\]

同理：

\[
\boxed{
u_0\mathcal G_B\ge Ne+Mc.}
\tag{FAREY-B}
\]

在 resonance 中，第 13 节会证明 lower endpoint equality 除极小 \(U=1\) exceptions 外不可能，所以 (FAREY-A/B) 实际覆盖绝大多数 genuine Layer-I survivor。

---

# 7. Resonance Normal Form

冻结：

\[
\boxed{R=0\Longrightarrow d=0,\quad\alpha=t=1,\quad v=10^{n_3}.}
\]

因此：

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

\[
\boxed{
P_2=10^{n_3}M,
\quad
P_3=N.
}
\]

\[
\boxed{
V=s\beta u_010^{n_3}.
}
\]

故 legal \(U\) 必满足

\[
\boxed{\gcd(U,10)=1.}
\]

---

# 8. Resonance H–S Identity

从 tail exact equation：

\[
10^gH=b_2(P_2+P_3-Q_0).
\]

定义

\[
\boxed{S_R:=P_2+P_3-Q_0.}
\]

则

\[
\boxed{10^gH=b_2S_R.}
\tag{H-SR}
\]

所以

\[
\boxed{\operatorname{sgn}H=\operatorname{sgn}S_R.}
\]

flat elimination 已给

\[
\boxed{S_R\ne0.}
\]

---

# 9. Resonance Sphere Identity

\[
Q_0=P_2+P_3-S_R.
\]

代入 sphere：

\[
P_1^2+P_2^2+P_3^2=(P_2+P_3-S_R)^2.
\]

得到

\[
\boxed{
P_1^2
=2P_2P_3
-2S_R(P_2+P_3)
+S_R^2.
}
\tag{RES-SPH}
\]

等价

\[
\boxed{
P_1^2-2P_2P_3
=S_R\bigl(S_R-2(P_2+P_3)\bigr).
}
\]

因此：

\[
\boxed{
S_R>0\iff P_1^2<2P_2P_3,
}
\]

\[
\boxed{
S_R<0\iff P_1^2>2P_2P_3.
}
\]

---

# 10. Sharp Mantissa Provenance and Use

已冻结：

\[
1<\frac{10^kP_1}{Q_0}<1+\frac1{b_1}\le2.
\]

故

\[
\frac{Q_0^2}{10^{2k}}
<P_1^2
<
\left(1+\frac1{b_1}\right)^2
\frac{Q_0^2}{10^{2k}}.
\]

本轮将其用于 resonance sign threshold，而不重新宣称 theorem。

---

# 11. Resonance Sign Threshold in \(P_3/Q_0\)

minus：

\[
P_1^2<2P_2P_3.
\]

由 \(P_1>Q_0/10^k\)、\(P_2<Q_0\)：

\[
\boxed{
\frac{P_3}{Q_0}>rac1{2\cdot10^{2k}}.
}
\tag{MINUS-P3}
\]

plus：

\[
P_1^2>2P_2P_3.
\]

使用

\[
P_1<\left(1+\frac1{b_1}\right)Q_010^{-k},
\]

及

\[
P_2>x_0Q_0,
\]

得

\[
\boxed{
\frac{P_3}{Q_0}
<
\frac{(1+1/b_1)^2}{2x_0}
10^{-2k}.
}
\tag{PLUS-P3-SHARP}
\]

粗略化即

\[
\frac{P_3}{Q_0}<\frac2{x_0}10^{-2k}<2.06\,10^{-2k},
\]

严格优于直接使用 \(d_2<2.532Q_010^{-2k}\) 的常数。

因此前述 \(\kappa\)-压缩还可在个别 \(b_1\)-regime 进一步加强；但仍未把 \(\kappa\) 双向夹成 finite set。

---

# 12. Resonance Divisor \(J=L_R\)

source 已冻结：

\[
\boxed{S_R=JZ,\qquad J=L_R>1.}
\]

且

\[
\boxed{
J=rac{10^g}{\gcd(10^g,\delta_\beta)}
}
\]

按当前 notation interpretation。

与 sphere 合并得到

\[
\boxed{J\mid(P_1^2-2P_2P_3).}
\]

但本轮没有发现 uniform \(|\Delta_R|/J<1\) 或 bounded quotient theorem。

---

# 13. Resonance Lower-Endpoint Equality Classification — NEW PROVED

resonance 中 legal \(U\) 是 decimal unit。

又 reducedness 给

\[
\gcd(C_3,b_3)=1.
\]

由于 \(10^{n_3}\mid b_3\)，有

\[
\boxed{\gcd(C_3,10)=1.}
\]

### third lower endpoint equality

若

\[
\frac U{u_0}
=
\frac{10^{n_3-1}}N,
\]

因为 \(N=u_0C_3\)，等价

\[
UC_3=10^{n_3-1}.
\]

但 \(U,C_3\) 均与 10 互素。

故：

- 若 \(n_3\ge2\)，不可能；
- 若 \(n_3=1\)，只能
  \[
  \boxed{U=C_3=1.}
  \]

所以

\[
\boxed{
\text{resonance third-lower equality}
\Longrightarrow
n_3=1,\ U=C_3=1.
}
\tag{EQ3}
\]

### second lower endpoint equality

若

\[
\frac U{u_0}
=
\frac{10^{n-1}}M,
\]

等价于

\[
UC_2=10^{n-1}.
\]

因 \(U\) 是 decimal unit：

\[
\boxed{U=1,\qquad C_2=10^{n-1}.}
\tag{EQ2}
\]

所以 resonance 中所有 nontrivial lower endpoint equality都被压成极小的 \(U=1\) exceptional configurations。

这对未来 Farey / reduced-margin proof 很有用：除上述异常外，active lower endpoint与 \(U/u_0\) 必为 distinct reduced rationals，可以合法使用严格 Farey margin。

---

# 14. Double Radial Resonance \(\Omega=0\)

定义

\[
\boxed{
\Omega:=N10^n-M10^{n_3}.
}
\]

\(\Omega=0\) 等价

\[
\boxed{
M10^{n_3}=N10^n.
}
\]

resonance primitive coordinates 中即

\[
\boxed{P_2=10^nP_3.}
\tag{DOUBLE-RES}
\]

又

\[
\frac{C_2}{C_3}=\frac MN=10^{n-n_3}.
\]

因为 \(\gcd(C_3,10)=1\)，若 \(n<n_3\)，则上式会强迫 \(10\mid C_3\)，矛盾。

因此：

\[
\boxed{
\Omega=0\Longrightarrow n_2=n\ge n_3.
}
\tag{OMEGA0-ORDER}
\]

若严格

\[
n>n_3,
\]

则

\[
C_2=C_3 10^{n-n_3},
\]

所以 \(10\mid C_2\)。由

\[
\gcd(C_2,b_2)=1
\]

得到

\[
\boxed{\gcd(b_2,10)=1.}
\]

resonance 中 \(b_2=s\beta\)，故

\[
\boxed{\gcd(s\beta,10)=1.}
\]

于是在 iterated-Smith definition of \(J\) 中所有 decimal absorption来自 \(v=10^{n_3}\)，直接得到

\[
\boxed{J=10^g.}
\tag{OMEGA0-J}
\]

所以：

\[
\boxed{
\Omega=0,\ n>n_3
\Longrightarrow
10^g\mid S_R.
}
\]

这显著加强了 double resonance 的 decimal depth，但尚未与 sphere/margin 形成 contradiction。

\(n=n_3\) 时则 \(C_2=C_3\)，需要单独继续；本轮没有关闭。

---

# 15. Why \(\Omega=0\) Is Not Yet Closed

\(\Omega=0\) 位于 radial cone 的中心，而不是 boundary：两个 upper endpoints 对齐，continuous overlap最大。

因此它不是 natural Layer-I death state。

要关闭它，必须依赖 exact word / sphere / reducedness，而不能期待 interval width 自己消失。

本轮得到的最小 exact exceptional system为：

\[
\boxed{
\begin{cases}
P_2=10^nP_3,\\
S_R=JZ\ne0,\\
J\mid P_1^2-2P_2P_3,\\
1<10^kP_1/Q_0<1+1/b_1,\\
\gcd(10^{2g}D,10^gQ_0-S_R)>10^gD,\\
n\ge n_3,\\
n>n_3\Rightarrow J=10^g.
\end{cases}
}
\tag{OMEGA0-NF}
\]

这比原来的 “ratio center” 明显更小，但仍不是空集 theorem。

---

# 16. Slack Identity Audit

prompt 定义

\[
E_2=10^{n}u_0-MU,
\qquad
E_3=10^{n_3}u_0-NU.
\]

对于合法 integer \(U\)：

\[
\boxed{E_2,E_3\ge1.}
\]

消去 \(U\)：

\[
\boxed{
u_0\left(N10^n-M10^{n_3}\right)
=NE_2-ME_3.
}
\tag{SLACK}
\]

即

\[
\boxed{u_0\Omega=NE_2-ME_3.}
\]

本轮没有从 resonance word arithmetic得到一个 uniform divisor of \(E_2\) 或 \(E_3\) 足以造成

\[
0<E_i<L\mid E_i.
\]

所以 “slack overload” 仍 OPEN。

---

# 17. GCD of \(M,N,u_0\) — audit correction

由于

\[
C_2=M/u_0,
\qquad
C_3=N/u_0
\]

本身为整数，严格有

\[
\boxed{u_0\mid M,N.}
\]

因此 prompt 中“是否 \(\gcd(M,u_0)=1\)”的候选方向必须删除：一般恰恰相反，\(u_0\) 是 \(M,N\) 的共同因子。

正确的 reducedness 是

\[
\boxed{
\gcd(M/u_0,b_2)=1,
\qquad
\gcd(N/u_0,b_3)=1.
}
\]

resonance 中第二式进一步给

\[
\boxed{\gcd(N/u_0,10)=1.}
\]

这是本轮 endpoint equality / \(\Omega=0\) 分析真正使用的 gcd 信息。

---

# 18. Can \(\gcd(M,N)\) Be Uniformly Small?

不能从 primitive sphere 单独推出

\[
\gcd(M,N)=1
\]

或只含 \(2,5\)。

原因是 \(u_0\mid M,N\) 本身已经提供共同因子；primitive condition 只约束完整 quadruple

\[
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

并不禁止 \(P_2,P_3\) 有任意共同因子，只要该 prime不同时进入 \(P_1,Q_0\)。

所以本轮没有把 \(M/N\) 当作 lowest terms fraction；Farey margin必须对 endpoints 自身先做 gcd reduction。

---

# 19. Resonance Layer-P Audit

resonance：

\[
\boxed{V/u_0=s\beta10^{n_3}.}
\]

所以如果真的到达 Layer P，candidate \(U\) 必满足

\[
\boxed{\gcd(U,s\beta10)=1.}
\]

但本轮没有发现一个 genuine exact resonance state 已经严格通过 C 与 I、只死在 P。

因此遵守 campaign discipline：

\[
\boxed{
\text{本轮不启动 generic positional unit-cover theorem。}
}
\]

---

# 20. Resonance Closure Verdict

本轮没有证明

\[
\boxed{R=0\Longrightarrow\varnothing.}
\]

因此不能诚实地进入“resonance 已闭合后全面清扫 d=0,1”的阶段。

但 resonance survivor 已被压到以下 exact normal form。

## Resonant SRUS Survivor Normal Form

任意仍可能存在的 resonance A1-SRUS state 必同时满足：

\[
\boxed{
\begin{gathered}
d=0,\quad n=2g+k,\quad \alpha=t=1,\quad v=10^{n_3},\\
P_2=10^{n_3}M,\quad P_3=N,\\
V=s\beta u_010^{n_3},\\
S_R=JZ\ne0,\quad J>1,\\
10^gH=b_2S_R,\\
\gcd(10^{2g}D,10^gQ_0-S_R)>10^gD.
\end{gathered}
}
\tag{RES-NF-CORE}
\]

并且根据 sign / active face：

\[
\boxed{
\begin{array}{c|c|c}
 & \text{Face A} & \text{Face B}\\
\hline
\text{plus} & k-2g\le0 & k-2g\le1\\
\text{minus} & k-2g\ge-1 & k-2g\ge0
\end{array}
}
\tag{RES-K-TABLE}
\]

若已经通过 Layer I，则还必须满足：

\[
\boxed{
\text{Face A: }
10^{-n}\le\frac{P_3}{P_2}
\le10^{1-n}(1-10^{-n_3}),
}
\]

\[
\boxed{
\text{Face B: }
\frac1{10(10^n-1)}
\le\frac{P_3}{P_2}<10^{-n}.
}
\]

lower endpoint equality除极小 \(U=1\) cases 外全部被排除。

若再落入 \(\Omega=0\)：

\[
\boxed{n\ge n_3,}
\]

且

\[
\boxed{n>n_3\Longrightarrow J=10^g.}
\]

这就是本轮达到的**最小精确 resonance frontier**。

---

# 21. Why the “one-decade gap” Was Only Partially Removed

此前 primitive ratio：

\[
10^{-n-2}<\frac{P_3}{P_2}<10^{-n+2}
\]

（等价于 source 的 \(M/N\) 表达）比 radial cone左右各宽一个 decade。

SPM + exact resonance sign 确实消掉了其中**与 sign 不相容的一大半**，并进一步由 active face 得到 (RES-K-TABLE)。

但它没有把：

- plus 的 \(k-2g\) 给出 uniform lower bound；
- minus 的 \(k-2g\) 给出 uniform upper bound。

因此：

\[
\boxed{
\text{SPM 补掉了 coarse mantissa loss，但没有单独完成 resonance closure。}
}
\]

剩余缺口不是“还差一个 factor 10 的 primitive bound”，而已经变成：

\[
\boxed{
\text{sign-compatible half-line}
\times
\text{radial face margin}
\times
\text{RGCD overload}.
}
\]

这比上一轮的 diagnosis 更精确。

---

# 22. Transition Affine Identity — Provenance Recovery

虽然 resonance 尚未闭合，本轮仍对 prompt 要求的 transition affine identity做了 provenance audit，避免下一轮重新找式子。

latest iterated-Smith variables给：

\[
\boxed{
S_3=\alpha JZ-M\widehat R,
}
\tag{AFF}
\]

其中

\[
\boxed{
\widehat R=\alpha t10^{n_3}-v.
}
\]

strongest quotient normalization写

\[
\boxed{Z=h_T^\sharp q.}
\]

所以

\[
\boxed{
S_3=\alpha J h_T^\sharp q-M\widehat R.
}
\tag{AFF-q}
\]

这正是 prompt 中 opaque candidate 的 source-correct version。

又

\[
S_3=P_2+P_3-Q_0
=vM+\alpha tN-Q_0.
\]

消去 \(S_3\)：

\[
\boxed{
Q_0
=\alpha t(M10^{n_3}+N)-\alpha J h_T^\sharp q.
}
\tag{FQ-AFF}
\]

这里使用

\[
v+\widehat R=\alpha t10^{n_3}.
\]

这是 d=0/1 transition 后续真正应使用的 affine formula。

---

# 23. Fixed-q Sphere Equation

记

\[
A:=\alpha t,
\quad
B:=v,
\quad
T:=10^{n_3},
\quad
E:=\alpha J h_T^\sharp q.
\]

则

\[
Q_0=A(MT+N)-E.
\]

sphere：

\[
P_1^2+B^2M^2+A^2N^2
=[A(MT+N)-E]^2.
\]

消去 \(A^2N^2\)：

\[
\boxed{
(AMT-E)(AMT+2AN-E)
=P_1^2+B^2M^2.
}
\tag{FQ-SPH}
\]

这也是 source 已有的 fixed-q radial equation。

---

# 24. FAILED AS UNIFORM ROUTE — “fixed q gives a fixed conic in M,N”

prompt 希望 fixed \(q\) 后得到真正 fixed-coefficient conic，然后只分析 \(M/N\) root。

本轮审计表明：作为 **uniform transition theorem**，这一步仍不成立。

将 (FQ-SPH) 除以 \(M^2\)，令

\[
x:=\frac NM,
\qquad
\lambda:=\frac{P_1}{M},
\]

得到

\[
\boxed{
\left(AT-\frac EM\right)
\left(AT+2Ax-\frac EM\right)
=\lambda^2+B^2.
}
\tag{FQ-NORM}
\]

即使 \(q\) 固定：

- \(A=\alpha t\) 仍可移动；
- \(B=v\) 仍可移动；
- \(J,h_T^\sharp\) 可移动；
- \(E/M\) 可移动；
- \(P_1/M\) 可移动。

所以没有得到一个仅含 normalized ratio \(x=M/N\) 的固定多项式。

因此：

\[
\boxed{
\text{finite }q\not\Rightarrow\text{finite normalized root family}
}
\]

without one more scale theorem。

这解释了为什么上一轮 Smith-rich “finite quotient” 仍未自动变成 Layer-C closure。

---

# 25. d=0 Transition — Minimal Audit

对 \(g\ge1,d=0,R\ne0\)：

\[
\boxed{n_2=2g+k},
\]

minus carry：

\[
\boxed{c=1.}
\]

plus：

\[
-Q_0<H<0,
\]

minus：

\[
0<H<Q_0.
\]

sign mismatch source 已冻结：

- plus + \(R>0\)：\(S_3<0\) 且
  \[
  |S_3|\ge\alpha J+M,
  \qquad m_3\ge2k;
  \]
- minus + \(R<0\)：\(S_3>0\) 且
  \[
  S_3\ge\alpha J+M,
  \qquad m_3\ge2g+k-1.
  \]

但 \(M/N\) 中 \(v/(\alpha t)\) 已被 Smith-radial cancellation exact 消掉，单独 \(R\)-sign仍不能确定 radial face。

本轮没有发现一条新的 identity 可把上述 \(|S_3|\ge\alpha J+M\) uniform 转成

\[
\mathcal G_A<M
\quad\text{or}\quad
\mathcal G_B<N.
\]

所以 d=0 nonresonant **仍 OPEN**。

---

# 26. d=1 Transition — Minimal Audit

\[
\boxed{n_2=2g+k+1.}
\]

minus：

\[
\boxed{c\in\{1,\ldots,10\}.}
\]

plus source 已冻结 near-denominator-resonance constraints，包括

\[
\boxed{m_3\ge2k,}
\]

及

\[
\boxed{v>0.385\,10^{2k}.}
\]

但完整 radial ratio是

\[
\frac MN10^{n_3-(2g+k+1)},
\]

显式 \(v,\alpha t\) 仍 exact cancel。

因此这些 denominator-mantissa bounds只有在进入 AFF coefficients 后才有意义；本轮没有得到 uniform boundary-margin contradiction。

所以 d=1 **仍 OPEN**。

---

# 27. Reduced-Fraction Margin in Transition

即使 d=0/1 continuous cone surviving，也可以无损使用第 6 节：

对 active upper endpoint

\[
\frac{10^{n_i}}X
\]

先化 lowest terms，分母

\[
X^\star=X/\gcd(X,10^{n_i}),
\]

任何 distinct \(U/u_0\) 必离它至少

\[
\frac1{u_0X^\star}.
\]

这比 raw

\[
10^{n_i}u_0-XU\ge1
\]

在 decimal-rich \(X\) 上更强。

但 transition 中尚未有 theorem 保证 \(M^\star\) 或 \(N^\star\) uniformly small，所以本轮只冻结工具，不伪报 closure。

---

# 28. Layer C / I / P Census — Logical Status

本轮没有进行足以支撑统计结论的大规模 exact-state enumeration，因此不制造百分比。

严格 theorem status：

- resonance：C 未完全关闭；I 新增 face-margin、reduced-margin、endpoint-equality restrictions；P 未进入 generic campaign；
- d=0：C/I 仍 open；
- d=1：C/I 仍 open；
- 没有证明存在 genuine Layer-P survivor；
- 没有发现 full SRUS survivor并完成 original reconstruction。

因此现阶段仍应坚持

\[
\boxed{C\to I\to P}
\]

优先级。

---

# 29. Killed / Downgraded Conjectures

## 29.1 “SPM 是本轮新 theorem”

**DOWNGRADED / ALREADY FROZEN.**

source 已有更强 \((1+1/b_1)\)-bound。

## 29.2 “SPM + resonance sign 会自动把 \(k-2g\) 压成 finite set”

**FAILED.**

实际只得到 face-dependent half-lines (RES-K-TABLE)。

## 29.3 “\(J\mid\Delta_R\) 且 \(|\Delta_R|<J\)”

**FAILED AS CURRENT MAGNITUDE ROUTE.**

整除正确，但 uniform size bound不足。

## 29.4 “更强 H divisor自动产生更强 independent \(S_R\) divisor”

**FAILED UNIFORMLY.**

resonance 中主要 forced factors与 \(b_2\)/decimal content cancellation；canonical uniform remainder仍是 \(J=L_R\)。

## 29.5 “fixed q \(\Rightarrow\) fixed ratio polynomial”

**FAILED AS UNIFORM TRANSITION ROUTE.**

(FQ-NORM) 仍含多个 moving normalized coefficients。

## 29.6 “\(\gcd(M,u_0)=1\)”

**FALSE.**

事实上 \(u_0\mid M,N\)。

## 29.7 “resonance exact center \(\Omega=0\) 应由 Layer I 自动杀掉”

**FAILED AS GEOMETRIC EXPECTATION.**

\(\Omega=0\) 位于最大 continuous overlap center；需要 exact arithmetic closure。

---

# 30. Strongest NEW PROVED Results

本轮真正可冻结的新 theorem / compression：

### A1-RT-1 — Resonant Face Integer Margin

\[
\text{Face A}\Rightarrow
\frac{P_3}{P_2}
\le10^{1-n}(1-10^{-n_3}),
\]

\[
\text{Face B}\Rightarrow
\frac{P_3}{P_2}
\ge\frac1{10(10^n-1)}
\]

for integer-radial survivors。

### A1-RT-2 — Resonant Sign–Face–Exponent Compression

\[
\boxed{
\begin{array}{c|c|c}
 & A & B\\
\hline
+ & k-2g\le0 & k-2g\le1\\
- & k-2g\ge-1 & k-2g\ge0
\end{array}
}
\]

with plus/A sharpened to \(k-2g\le-1\) if \(b_1\ge3\)。

### A1-RT-3 — Resonant Reduced-Denominator GCD Identity

\[
\boxed{
u10^{2g}D=\beta(10^gQ_0-S_R)}
\]

in coprime coefficients。

### A1-RT-4 — Resonant GCD Overload

\[
\boxed{
\gcd(10^{2g}D,10^gQ_0-S_R)>10^gD.
}
\]

### A1-RT-5 — Resonant Integer Mantissa Normal Form

\[
\boxed{b_2=10^g c_R/J,\quad S_R=JZ,\quad H=c_RZ,}
\]

\[
\boxed{\lceil J/10\rceil\le c_R\le J-1.}
\]

### A1-RT-6 — Reduced Endpoint Margin

\[
\boxed{
\left|\frac U{u_0}-\frac AB\right|
\ge\frac1{u_0B}
}
\]

for distinct reduced rationals。

### A1-RT-7 — Two-Sided Reduced-Endpoint Margin

\[
\boxed{u_0\mathcal G_A\ge M\gcd(N,10^{n_3})+N\gcd(M,10^{n_2-1})}
\]

或

\[
\boxed{u_0\mathcal G_B\ge N\gcd(M,10^{n_2})+M\gcd(N,10^{n_3-1})}
\]

for strict interior reduced-fraction survivors。

### A1-RT-8 — Resonance Endpoint Equality Classification

third lower equality only possible at

\[
\boxed{n_3=1,\ U=C_3=1};
\]

second lower equality forces

\[
\boxed{U=1,\ C_2=10^{n-1}}.
\]

### A1-RT-9 — Double Radial Resonance Decimal Ordering

\[
\boxed{\Omega=0\Rightarrow n_2\ge n_3,}
\]

and

\[
\boxed{
\Omega=0,\ n_2>n_3\Rightarrow J=10^g.
}
\]

---

# 31. Exact Remaining Resonance Theorem

本轮后，不建议再把 resonance 写成模糊的

> “需要 better control of common U”。

真正剩余的是：

## A1-RBMI — Resonant Boundary-Margin + GCD-Overload Exclusion

证明不存在正整数 state 满足：

\[
\boxed{
\begin{gathered}
P_1^2+P_2^2+P_3^2=Q_0^2,\\
P_2=10^{n_3}M,\quad P_3=N,\\
n=2g+k,\\
S_R=P_2+P_3-Q_0=JZ\ne0,\\
1<10^kP_1/Q_0<1+1/b_1,\\
\gcd(10^{2g}D,10^gQ_0-S_R)>10^gD,
\end{gathered}
}
\]

并同时落入某个 allowed sign/face slab (RES-K-TABLE)，且通过相应 Smith-Reduced Integer Margin / reduced-fraction margin。

这比上一轮的

\[
\boxed{\text{Resonant Reduced-Fraction Unit Exclusion}}
\]

又多了一个非常具体的 non-radial arithmetic overload：

\[
\boxed{\textbf{RGCD-OVERLOAD}.}
\]

---

# 32. Exact Remaining Transition Theorem

由于 resonance 未闭合，本轮不宣称 transition 已被主攻到 closure。

但 source-correct frontier可冻结为：

## A1-TABM — Transition Affine Boundary-Margin Exclusion

对 \(d\in\{0,1\}\)、\(R\ne0\)，利用

\[
\boxed{S_3=\alpha Jh_T^\sharp q-M\widehat R}
\]

以及

\[
\boxed{Q_0=\alpha t(M10^{n_3}+N)-\alpha Jh_T^\sharp q}
\]

直接证明 active radial gap违反

\[
\boxed{\mathcal G_A\ge M}
\]

或

\[
\boxed{\mathcal G_B\ge N},
\]

必要时再调用 Reduced Endpoint Margin。

不能再把“finite q”本身当作 closure。

---

# 33. Generic Outer d Quick Audit

对 \(g\ge1\)：

\[
d\le-1\Rightarrow\text{plus},
\qquad
d\ge2\Rightarrow\text{minus}.
\]

本轮没有进入 outer generic SRUS，因为 resonance 本身尚未关闭，且 campaign discipline 要求不在低维核心尚开时重新膨胀。

因此 outer branches 状态维持：

\[
\boxed{\text{OPEN / not materially advanced this round}.}
\]

---

# 34. Strict Layer Closure Audit

未达到 A1 closure，所以不生成假的 closure certificate。

当前依赖关系仍为：

\[
DD=\varnothing,
\]

\[
\boxed{
\text{Strict Layer CLOSED}
\Longleftrightarrow
A_1=\varnothing.
}
\]

本轮未完成后者。

---

# 35. PROVED / DERIVED / FAILED / OPEN Ledger

## FROZEN

- DD closed；
- Strict frontier = A1-only；
- primitive sphere；
- exponent normal form；
- common-U reconstruction；
- DES / H；
- Full Smith chart；
- Full Smith–radial cancellation；
- two radial faces；
- Smith-reduced Integer Margin；
- iterated-Smith affine/radial-gap bridge；
- resonance normal form；
- \(J=L_R\mid S_R\)；
- SPM stronger \((1+1/b_1)\)-bound。

## NEW PROVED

1. Resonant Face Integer Margin in \(P_3/P_2\) coordinates；
2. Resonant Sign–Face–Exponent Compression table；
3. plus/Face-A \(b_1\ge3\Rightarrow k-2g\le-1\) sharpening；
4. Resonant reduced-denominator identity \(u10^{2g}D=\beta(10^gQ_0-S_R)\)；
5. Resonant GCD Overload；
6. Resonant Integer Mantissa Normal Form；
7. Reduced Endpoint Margin theorem；
8. Two-Sided Reduced-Endpoint / Farey Margin；
9. resonance lower endpoint equality classification；
10. \(\Omega=0\Rightarrow n_2\ge n_3\)；
11. \(\Omega=0,n_2>n_3\Rightarrow J=10^g\)。

## DERIVED / REPACKAGED

- H–\(S_R\) sign identity；
- \(J\mid\Delta_R\)；
- exact transition AFF-q provenance；
- fixed-q sphere equation provenance。

## FAILED / DOWNGRADED

- SPM as a new theorem；
- SPM alone finite-izes \(k-2g\)；
- \(J\mid\Delta_R\) + current magnitude closes resonance；
- uniform amplified divisor beyond \(J\)；
- fixed-q implies fixed normalized conic；
- \(\gcd(M,u_0)=1\)；
- \(\Omega=0\) is automatically Layer-I dead。

## OPEN

1. Resonant Boundary-Margin + GCD-Overload Exclusion；
2. d=0 Transition Affine Boundary-Margin Exclusion；
3. d=1 Transition Affine Boundary-Margin Exclusion；
4. outer d branches；
5. A1-SRUS；
6. \(A_1=\varnothing\)；
7. Strict Layer closure。

---

# 36. At Most Three Next Targets

## Target 1 — RGCD Overload Extinction

只研究 resonance：

\[
\gcd(10^{2g}D,10^gQ_0-S_R)>10^gD
\]

与

\[
S_R=JZ,
\quad
P_1^2+P_2^2+P_3^2=Q_0^2,
\quad
\text{RES-K-TABLE}
\]

能否冲突。

优先 primewise 分解这个“大于 denominator 的 gcd”，而不是继续 generic \(2/5\)-Hensel。

## Target 2 — Resonance Face-Margin Extinction

分别研究：

\[
\text{Face A: }
10^{-n}\le r\le10^{1-n}(1-10^{-n_3}),
\]

\[
\text{Face B: }
\frac1{10(10^n-1)}\le r<10^{-n},
\]

联立 sign-specific \(P_3\gtrless d_2\) 与 SPM，目标把 RES-K-TABLE 的 half-lines进一步压成 finite \(\kappa\)。

## Target 3 — Transition AFF \(\to\) Boundary Gap

只有前两项不能闭 resonance时，再进入：

\[
S_3=\alpha Jh_T^\sharp q-M\widehat R
\]

直接消元到 \(\mathcal G_A/M\) 或 \(\mathcal G_B/N\)，不要再停在 “q finite”。

---

# 37. Final Assessment

本轮没有达到 prompt 的 strong success / very strong success。

但它把 exact resonance 从：

\[
\boxed{
S_R=JZ\ne0
+
\text{one-decade ratio gap}
+
\text{reduced fraction }U/u_0
}
\]

进一步压成：

\[
\boxed{
\text{sign-specific radial face}
\times
\text{integer face margin}
\times
\text{half-line }(k-2g)
\times
\textbf{large exact gcd overload}
}
\]

其中真正新增、最值得下一轮继续追击的是

\[
\boxed{
\gcd(10^{2g}D,10^gQ_0-S_R)>10^gD.
}
\]

因此当前最小 resonance frontier 不再只是“找一个 common-U successor”，而是：

\[
\boxed{
\textbf{一个必须同时满足极强 reduced-denominator gcd overload 的 SRUS successor problem。}
}
\]

这就是本轮最实质的推进。
