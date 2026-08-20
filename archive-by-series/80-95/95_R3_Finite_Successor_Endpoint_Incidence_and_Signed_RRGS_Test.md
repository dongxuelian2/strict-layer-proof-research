# 95-R3 — Finite-Successor Endpoint Incidence × Unimodular Cross-Product × Positive Resonance Closure × Negative Signed-RRGS Capacity Test

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Ownership:** \(A_1^{95}=A_1\cap\{J\neq2\}\)  
**Round:** 95-R3  
**Canonical output:** `95_R3_Finite_Successor_Endpoint_Incidence_and_Signed_RRGS_Test.md`

---

# Part I — Executive Verdict

本轮最终判决：

```text
95_R3_STATUS = COMPLETE

POSITIVE_ENDPOINT_ARCHITECTURE_FALSIFIED
POSITIVE_RESONANCE_CLOSED = NO
POSITIVE_RESONANCE_GLOBAL_FINITE = NO

FINITE_SUCCESSOR_CANONICALIZATION = FROZEN_AND_REAUDITED
ENDPOINT_PHASE = EXACTLY_RECONSTRUCTED_BUT_NOT_SUCCESSOR_DETERMINED
UNIMODULAR_CROSS_PRODUCT = GENUINE_NEW_SPACING
UNIMODULAR_TO_DECIMAL_ENDPOINT_BRIDGE = MISSING

J5_1_STRESS_TEST = FAILS_UNIFORM_ENDPOINT_FINITEIZATION
SIGNED_RRGS_VERDICT = SIGNED_RRGS_PARTIAL
SIGNED_RRGS_REPAIR_DATUM = INDEPENDENT_BOUND_ON_U_d2

R4_LAUNCH = YES
```

因此本轮达到 prompt 允许的：

\[
\boxed{\textbf{Level D — Architecture Falsification}}
\]

而不是 Level A/B/C。

R3 的核心结论不是“determinant 没用”，恰好相反：

\[
\boxed{
\text{general-}J\text{ unimodular envelope 确实产生 genuine new spacing}.
}
\]

真正失败的是三方碰撞中的第三条边：

\[
\boxed{
\text{decimal endpoint}
\not\Longrightarrow
\text{canonical unimodular slope 的短邻域}.
}
\]

更具体地：

1. R2 的
   \[
   \xi=UW
   \]
   的确把 positive \((U,W)\) 压成 finite successor；
2. 旧 A1 endpoint theorem 的 exact phase 仍由
   \[
   C_2,C_3,\delta_2,\delta_3
   \]
   控制；
3. 固定 \((\xi,U,W)\) **并不固定 \(C_2,C_3\)**，因此也不固定 endpoint phase；
4. unimodular determinant 可以给 \(U/u_0\) 与 canonical slope 之间的严格 lower gap；
5. 但 SRUS 只告诉
   \[
   U/u_0\in K_{MN},
   \]
   没有 theorem 把 \(K_{MN}\) 放到 canonical slope 附近；
6. 所以不存在本轮所需的
   \[
   \text{decimal upper}<\text{unimodular lower}
   \]
   collision。

negative side 则得到一个精确的 signed reformulation：

\[
\boxed{
0<U|W|<\frac{d_*}{G}\,U d_2,
}
\]

但右端仍含 moving primitive gap \(Ud_2\)。因此 signed RRGS 不是完全失败，而是被精确定位为：

\[
\boxed{
\textbf{只缺一条 independent }Ud_2\textbf{ upper bound}.
}
\]

---

# Part II — Frozen R2 Assets

以下全部永久冻结，不重新证明。

令：

\[
G:=10^g.
\]

在 exact resonance \(R=0\) 中：

\[
d=0,\qquad n_2=2g+k,\qquad \alpha=t=1,\qquad v=10^{n_3},
\]

\[
P_2=10^{n_3}M,\qquad P_3=N,
\]

\[
C_2=M/u_0,\qquad C_3=N/u_0,
\qquad u_0\mid M,N.
\]

actual radial recovery：

\[
a_2=UC_2,\qquad a_3=UC_3,
\qquad \gcd(U,V)=1.
\]

fully deflated arithmetic：

\[
D=\beta_0D_1,
\]

\[
uJD_1=d_*Q_0-W,
\]

\[
S_R=K_*W,
\qquad
K_*=\frac{G}{d_*},
\]

\[
c_R=s\,d_*\beta_0<J.
\]

cyclotomic reduced denominator：

\[
u_0\mid G+1,
\]

\[
\gcd(u_0,Q_0)=\gcd(u_0,S_R)=\gcd(u_0,10)=1,
\]

故：

\[
\gcd(u_0,W)=1.
\]

exact mantissa difference：

\[
b_1JD-c_RQ_0=-s\beta_0W.
\]

因此 R2 已经永久处决：

```text
GENERIC_MANTISSA_LATTICE_GAP = REDUNDANT
ENHANCED_DIVISOR_TIMES_ENDPOINT_SIZE = NOT_INDEPENDENT
PURE_CYCLOTOMIC_SUPPORT_CLOSURE = INSUFFICIENT
```

general-\(J\) RRGS：

\[
\Xi:=UW,
\]

\[
U(Q_0-P_2)+K_*\Xi=u_0a_3,
\tag{RRGS-1}
\]

\[
d_*(10^{n_3}a_2+a_3)
=
\frac{G+1}{u_0}\Xi+\gamma JUD_1.
\tag{RRGS-2}
\]

在 \(S_R>0\)：

\[
0<\Xi<u_0d_*10^{n_3-g}.
\tag{RRGS-3}
\]

unimodular envelope：

\[
q_0:=\frac{G+1}{u_0},
\]

\[
\bar A_J:=Ju_0+1,
\qquad
\bar B_J:=JG+q_0,
\]

\[
q_0\bar A_J-\bar B_J=J,
\]

\[
\boxed{
u_0\bar B_J-G\bar A_J=1.
}
\tag{UNI}
\]

R2 已 certified：

\[
\boxed{
\mathcal H_{5,2}^{+}=\varnothing,
\qquad
\mathcal H_{5,3}^{+}=\varnothing.
}
\]

这两支不得重新打开。

---

# Part III — Finite Successor Canonicalization

## 3.1 95-R3-T1 / 95-R2-FS — Positive Resonant Finite Successor Theorem

取一个 genuine non-\(J2\) exact-resonance source state，满足：

\[
S_R>0.
\]

于是：

\[
W>0,
\qquad
\xi:=UW>0.
\]

RRGS-3 给：

\[
\boxed{
0<\xi<B_+,
\qquad
B_+:=u_0d_*10^{n_3-g}.
}
\]

又：

\[
\gcd(U,u_0)=1,
\qquad
\gcd(W,u_0)=1,
\]

故：

\[
\boxed{\gcd(\xi,u_0)=1.}
\]

定义：

\[
\mathcal X_+(B_+,u_0)
=
\{x\in\mathbf Z_{>0}:x<B_+,\ \gcd(x,u_0)=1\}.
\]

则：

\[
\boxed{
\xi\in\mathcal X_+(B_+,u_0).
}
\]

并且：

\[
\boxed{
U\mid\xi,
\qquad
W=\xi/U.
}
\]

因此 fixed structural fibre

\[
(g,J,\beta_0,h,d_*,n_3,u_0)
\]

内，所有 positive source candidate 都必须经过：

\[
\boxed{
\text{finite }\xi
\longrightarrow
\text{finite divisor }U\mid\xi
\longrightarrow
W=\xi/U.
}
\]

这是真正的 state-space reduction。

但必须再次强调：

\[
\boxed{
\text{fixed-fibre finite}
\neq
\text{global finite}.
}
\]

尤其 \(B_+\) 仍含：

\[
10^{n_3-g}.
\]

---

## 3.2 successor 后仍需通过的 terminal source gates

每个 \((\xi,U,W)\) 仍必须通过：

\[
\frac U{u_0}\in K_{MN},
\]

\[
\gcd(U,V)=1,
\]

以及：

- primitive sphere；
- exact leading defect；
- Smith divisibility；
- numerator realization；
- exact source equations；
- original decimal word replay。

所以 finite successor 是入口，不是 source certificate。

---

# Part IV — Endpoint Phase Reconstruction

## 4.1 canonical endpoint 不是新 mantissa，而是 SRUS interval

令：

\[
x_2:=10^{n_2-1},
\qquad
x_3:=10^{n_3-1}.
\]

旧 A1 endpoint theorem 给：

\[
K_{MN}
=
\left[
\max\left(\frac{x_2}{M},\frac{x_3}{N}\right),
\min\left(\frac{10x_2}{M},\frac{10x_3}{N}\right)
\right),
\]

且：

\[
\boxed{
\frac U{u_0}\in K_{MN}.
}
\]

由于：

\[
M=u_0C_2,\qquad N=u_0C_3,
\]

这等价于 actual digit windows：

\[
\boxed{
x_2\le UC_2<10x_2,
}
\]

\[
\boxed{
x_3\le UC_3<10x_3.
}
\]

---

## 4.2 Type-A exact endpoint excess

定义：

\[
\boxed{
e_2:=UC_2-x_2=a_2-x_2,
}
\]

\[
\boxed{
e_3:=UC_3-x_3=a_3-x_3.
}
\]

则：

\[
0\le e_i<9x_i,
\]

并且：

\[
\boxed{
e_i\equiv -x_i\pmod U.
}
\]

这给出 exact integer endpoint phase。

但它只说明：

\[
e_i
\in
(-x_i\bmod U)+U\mathbf Z,
\]

没有唯一化 \(e_i\)。

---

## 4.3 old Euclidean endpoint phase

旧 endpoint theorem 的 canonical jump 是：

\[
\boxed{
\delta_2=(-x_2)\bmod C_2,
\qquad
\delta_3=(-x_3)\bmod C_3.
}
\]

Face A：

\[
G_A^\circ\ge C_3\delta_2+C_2.
\]

Face B：

\[
G_B^\circ\ge C_2\delta_3+C_3.
\]

所以真正的 endpoint phase 仍显式依赖：

\[
\boxed{C_2,C_3.}
\]

而 R2 successor 只固定：

\[
\boxed{\xi,U,W.}
\]

这正是第一处维数缺口。

---

## 4.4 95-R3-T2 — Successor-conditioned Third Endpoint Formula

在 positive branch：

\[
d_2+K_*W=u_0C_3.
\]

乘 \(U\)：

\[
Ud_2+K_*\xi=u_0a_3.
\]

故：

\[
\boxed{
u_0e_3
=
Ud_2+K_*\xi-u_0x_3.
}
\tag{EP3}
\]

因此 fixed successor \((\xi,U,W)\) 后，third endpoint phase **并不唯一**；它仍然沿 moving primitive gap \(d_2\) 仿射移动。

同理：

\[
C_3=\frac{d_2+K_*W}{u_0}.
\]

所以：

\[
\boxed{
\text{successor}
\to
\text{endpoint}
}
\]

之间缺失的第一个明确 datum 是：

\[
\boxed{d_2}
\]

或等价的：

\[
\boxed{C_3}.
\]

---

## 4.5 RRGS modulo \(U\) 的 novelty audit

RRGS-1 模 \(U\)：

\[
K_*\xi\equiv u_0a_3\pmod U.
\]

但：

\[
\xi=UW,
\]

故左边为 \(0\pmod U\)。

于是：

\[
u_0a_3\equiv0\pmod U.
\]

而：

\[
\gcd(U,u_0)=1,
\]

所以：

\[
U\mid a_3.
\]

这正是：

\[
a_3=UC_3
\]

的重写。

因此：

```text
RRGS1_ENDPOINT_RESIDUE = SOURCE_DIVISIBILITY_REPACKAGING
```

RRGS-2 模 \(U\) 同样退化到 \(U\mid a_3\)（利用 \(d_*\) 为 \(2,5\)-smooth、而 \(U\) 是 ten-unit）。

所以：

\[
\boxed{
\text{RRGS 没有额外制造一个 independent endpoint residue class.}
}
\]

---

## 4.6 Endpoint exactization verdict

本轮确实把 endpoint phase 写成 exact integer / Euclidean residue：

\[
e_i,\quad \delta_i,
\]

但：

\[
\boxed{
(\xi,U,W)
\not\Longrightarrow
\text{finite exact endpoint phases}
}
\]

在当前 information class 下无法成立。

因此本轮不能签发 Level C：

```text
POSITIVE_RESONANCE_ENDPOINT_EXACTIZED
```

只能签发：

```text
ENDPOINT_PHASE_FORMULA_EXACT
SUCCESSOR_TO_ENDPOINT_FINITE_MAP = NOT_OBTAINED
```

---

# Part V — Unimodular Incidence

## 5.1 genuine radial–canonical cross-product

考虑 actual reduced radial fraction：

\[
\frac U{u_0}
\]

与 canonical unimodular fraction：

\[
\frac{\bar B_J}{\bar A_J}.
\]

定义：

\[
\boxed{
D_{\rm rad}
:=
\bar A_JU-u_0\bar B_J.
}
\]

由：

\[
u_0\bar B_J-G\bar A_J=1
\]

得到：

\[
\boxed{
D_{\rm rad}
=
\bar A_J(U-G)-1.
}
\tag{CROSS}
\]

这不是 \(W\)、\(S_R\) 或旧 mantissa remainder 的倍数。

它是：

\[
\boxed{
\textbf{genuinely distinct sourced cross-product}.
}
\]

---

## 5.2 source ten-unit condition 加强 determinant spacing

resonance 中：

\[
V=s\beta u_0 10^{n_3}.
\]

source gate：

\[
\gcd(U,V)=1.
\]

因此：

\[
\gcd(U,10)=1.
\]

而：

\[
G=10^g
\]

不是 ten-unit。

故：

\[
\boxed{U\neq G.}
\]

于是：

\[
|U-G|\ge1.
\]

由 (CROSS)：

\[
|D_{\rm rad}|
=
|\bar A_J(U-G)-1|.
\]

若 \(U-G\ge1\)：

\[
D_{\rm rad}\ge\bar A_J-1=Ju_0.
\]

若 \(U-G\le-1\)：

\[
|D_{\rm rad}|\ge\bar A_J+1.
\]

因此统一得到：

\[
\boxed{
|D_{\rm rad}|\ge Ju_0.
}
\tag{LOW-D}
\]

---

# Part VI — Arithmetic Lower Bound

由：

\[
\left|
\frac U{u_0}
-
\frac{\bar B_J}{\bar A_J}
\right|
=
\frac{|D_{\rm rad}|}{u_0\bar A_J},
\]

以及 (LOW-D)：

\[
\boxed{
\left|
\frac U{u_0}
-
\frac{\bar B_J}{\bar A_J}
\right|
\ge
\frac{J}{\bar A_J}
=
\frac{J}{Ju_0+1}.
}
\tag{UNI-LOW}
\]

这比 generic reduced-fraction lower bound：

\[
\frac1{u_0\bar A_J}
\]

强一个 \(Ju_0\) 因子。

所以 R3 的失败**绝不是 arithmetic lower spacing 太弱**。

相反：

\[
\boxed{
\text{unimodular lower spacing 已经相当强。}
}
\]

---

# Part VII — Decimal Upper Bound Audit

R3 所需的 closure 形式应该是：

\[
\left|
\frac U{u_0}
-
\frac{\bar B_J}{\bar A_J}
\right|
<
\frac{J}{\bar A_J}.
\]

但现有 decimal endpoint theorem 只给：

\[
\frac U{u_0}\in K_{MN}.
\]

即：

\[
\frac U{u_0}
\]

位于两个 decimal blocks 决定的 half-open interval 中。

没有 frozen theorem 给：

\[
K_{MN}
\subset
\left(
\frac{\bar B_J}{\bar A_J}-\varepsilon,
\frac{\bar B_J}{\bar A_J}+\varepsilon
\right)
\]

其中：

\[
\varepsilon<\frac{J}{\bar A_J}.
\]

也没有 theorem 给：

\[
\operatorname{dist}
\left(
K_{MN},
\frac{\bar B_J}{\bar A_J}
\right)
\]

的任何 uniform small upper bound。

因此：

```text
DECIMAL_UPPER_SEPARATION = NOT_AVAILABLE
MISSING_EDGE = ENDPOINT_INTERVAL_TO_UNIMODULAR_SLOPE
```

---

## 7.1 为什么 exact Euclidean jump 也没有补上这条边

\[
\delta_2=(-x_2)\bmod C_2,
\qquad
\delta_3=(-x_3)\bmod C_3
\]

可以告诉我们：

\[
U/u_0
\]

离 active lower decimal endpoint 有多远。

但它不告诉我们：

\[
\frac{\bar B_J}{\bar A_J}
\]

与该 decimal endpoint 的相对位置。

所以即使 endpoint jump 完全 exact，也只得到：

\[
\boxed{
\text{radial point}
\leftrightarrow
\text{decimal endpoint}
}
\]

这一条边。

unimodular envelope 给：

\[
\boxed{
\text{radial point}
\leftrightarrow
\text{canonical slope}
}
\]

另一条边。

缺失的是：

\[
\boxed{
\text{decimal endpoint}
\leftrightarrow
\text{canonical slope}.
}
\]

三角形没有闭合。

---

# Part VIII — Collision / Non-Hit Verdict

## 8.1 cross-product novelty test

本轮主要 candidate：

\[
D_{\rm rad}
=
\bar A_JU-u_0\bar B_J
\]

通过 symbolic elimination 后：

- 不等于 \(C\cdot W\)；
- 不等于 \(C\cdot S_R\)；
- 不等于 old mantissa remainder；
- 不等于 enhanced-divisor normalization。

因此：

```text
CROSS_PRODUCT_NOVELTY = PASS
```

---

## 8.2 collision test

但：

```text
ARITHMETIC_LOWER_BOUND = STRONG
DECIMAL_CORRESPONDING_UPPER_BOUND = MISSING
UPPER_LESS_THAN_LOWER = NOT_REACHED
```

因此：

\[
\boxed{
\textbf{95-R3-T5 Positive Successor Non-Hit Theorem：NOT PROVED}.
}
\]

并正式判决：

```text
FINITE_SUCCESSOR_ENDPOINT_INCIDENCE_ARCHITECTURE_INSUFFICIENT
```

这里的 “insufficient” 具有精确含义：

\[
\boxed{
\text{缺失 independent datum}
=
\text{把 }(C_2,C_3,d_2)
\text{ 接到 unimodular slope 的 source equation}.
}
\]

不是“需要再加几个模数”。

---

# Part IX — SRUS Source Replay

R3 后，positive successor 的合法 replay 顺序应冻结为：

\[
(\xi,U,W)
\]

先恢复：

\[
W=\xi/U.
\]

然后枚举/求解 source-labelled：

\[
d_2,\quad C_3,\quad C_2,\quad D_1,\quad C_1,
\]

并逐层执行：

1. RRGS-1 / endpoint equation；
2. RRGS-2 / deflated source equation；
3. primitive sphere；
4. leading defect；
5. exact root / root divisibility；
6. digit windows；
7. SRUS：
   \[
   U/u_0\in K_{MN};
   \]
8. unit condition：
   \[
   \gcd(U,V)=1;
   \]
9. original source reconstruction；
10. original decimal equation exact replay。

本轮的重要位置校准是：

\[
\boxed{
\text{SRUS 应继续留在 terminal source gate，}
}
\]

而不能指望：

\[
\text{successor}
+
\text{generic determinant}
\]

自动替代 primitive/source equations。

---

# Part X — \(J=5,\mathcal H_{5,1}\) Stress Test

这一支：

\[
J=5,\qquad g=1,\qquad d_*=\beta_0=1,
\]

\[
u_0\mid11,
\qquad
u=5^ru_0,
\qquad
n_3\ge2.
\]

positive successor bound：

\[
\boxed{
0<\xi<u_0 10^{n_3-1}.
}
\]

因此 \(n_3\) tail 没有 uniform finiteization。

---

## 10.1 unimodular envelope 在 \(\mathcal H_{5,1}\) 中完全显式

### \(u_0=1\)

\[
q_0=11,
\qquad
\bar A_5=6,
\qquad
\bar B_5=61.
\]

并且：

\[
1\cdot61-10\cdot6=1.
\]

### \(u_0=11\)

\[
q_0=1,
\qquad
\bar A_5=56,
\qquad
\bar B_5=51.
\]

并且：

\[
11\cdot51-10\cdot56=1.
\]

所以 determinant 本身没有退化。

---

## 10.2 但 moving \(n_3\) 不受 canonical slope 控制

取 successor-layer test：

\[
\xi=1,
\qquad
U=W=1.
\]

对所有 \(n_3\ge2\)：

\[
1<u_0 10^{n_3-1},
\]

故它始终属于允许的 finite-successor set。

third numerator digit window允许：

\[
10^{n_3-1}\le C_3<10^{n_3}.
\]

positive gap只要求：

\[
d_2=u_0C_3-10>0.
\]

因此在这一 **successor-endpoint incidence layer** 中，候选 \(C_3\) 数量随 \(n_3\) 指数增长。

例如 \(u_0=1\) 时，除去 \(C_3=10\) 的边界失败，规模仍为：

\[
\asymp 9\cdot10^{n_3-1}.
\]

这些不是 full source solutions；它们只是精确证明：

\[
\boxed{
\text{successor theorem 本身不能把 H5.1 tail 变成 global finite endpoint set}.
}
\]

要继续删除这些 states，必须读 primitive sphere / root/source information。

---

## 10.3 H5.1 verdict

```text
H5_1_SUCCESSOR_FINITE_PER_n3 = YES
H5_1_GLOBAL_SUCCESSOR_FINITE = NO_THEOREM
H5_1_ENDPOINT_UNIQUE_FROM_SUCCESSOR = FALSE_AT_INCIDENCE_LEVEL
H5_1_UNIMODULAR_DETERMINANT_DEGENERACY = NO
H5_1_MISSING_DATUM = MOVING_SOURCE_GEOMETRY / PRIMITIVE GAP
```

因此 \(\mathcal H_{5,1}\) 成功扮演了 R3 stress fibre：

\[
\boxed{
\text{它证明当前 architecture 的失败来自 moving endpoint/source geometry，}
}
\]

而不是 small-\(J\) determinant 失效。

---

# Part XI — Negative Signed-RRGS Capacity Test

## 11.1 Sign Dependency Map

从：

\[
S_R=P_3-d_2=K_*W,
\qquad
P_3=u_0C_3,
\]

得到：

\[
d_2+K_*W=u_0C_3.
\tag{S1}
\]

### positive: \(S_R>0\)

此时：

\[
W>0.
\]

由 \(d_2>0\)：

\[
0<K_*W<u_0C_3.
\]

乘 \(U\)：

\[
0<K_*\xi<u_0a_3.
\]

再用：

\[
a_3<10^{n_3},
\]

得到：

\[
0<\xi<u_0d_*10^{n_3-g}.
\]

所以 RRGS-3 的 sign-sensitive step 正是：

\[
\boxed{
d_2>0
\quad+\quad
W>0
\Longrightarrow
K_*W<u_0C_3.
}
\]

---

### negative: \(S_R<0\)

写：

\[
w:=|W|=-W>0.
\]

(S1) 变成：

\[
d_2-K_*w=u_0C_3,
\]

即：

\[
\boxed{
d_2=u_0C_3+K_*w.
}
\tag{S-}
\]

于是方向反转：

\[
0<K_*w<d_2,
\]

而不是：

\[
K_*w<u_0C_3.
\]

乘 \(U\)，令：

\[
\xi_-:=Uw,
\]

得到：

\[
\boxed{
0<K_*\xi_-<Ud_2.
}
\]

即：

\[
\boxed{
0<\xi_-<
\frac{d_*}{G}\,Ud_2.
}
\tag{SRRGS-PARTIAL}
\]

这就是 general-\(J\) 当前合法的 signed analogue。

---

## 11.2 为什么 third-digit upper bound 在 negative sign 下失效

positive：

\[
K_*\xi<u_0a_3
\]

所以 third digit：

\[
a_3<10^{n_3}
\]

直接切 \(\xi\)。

negative：

\[
K_*\xi_-=Ud_2-u_0a_3.
\]

third digit只能控制被减去的：

\[
u_0a_3,
\]

却没有控制：

\[
Ud_2.
\]

因此没有 sign-symmetric 的 RRGS-3。

---

## 11.3 95-R3-T6 — Signed-RRGS Repair Criterion

若未来能独立证明：

\[
\boxed{
Ud_2<L(g,J,u_0,d_*,n_3,\ldots),
}
\tag{UD2-L}
\]

则立刻有：

\[
\boxed{
0<\xi_-<
\frac{d_*}{G}L.
}
\]

若右端只依赖 fixed structural tuple，则 negative branch 同样被 successor-finiteize。

所以 signed repair 的唯一核心 datum 可以冻结为：

\[
\boxed{
\textbf{independent actual-radial primitive-gap bound on }Ud_2.
}
\]

---

## 11.4 exact obstruction witness

为了证明 “RRGS algebra + decimal digit windows” 自身无法产生 negative finite successor，构造以下 **information-class pseudo-family**。

对任意 \(t\ge0\)，取：

\[
g=1,\quad G=10,\quad J=10,
\]

\[
u=u_0=d_*=\beta_0=s=1,
\]

\[
n_3=1,\quad k=1,\quad n_2=3,
\]

\[
U=1,\quad C_2=100,\quad C_3=1,
\]

\[
w=100t+99,
\qquad
W=-w,
\]

\[
d_2=1000t+991,
\]

\[
P_2=1000,\qquad P_3=1,
\]

\[
Q_0=1000t+1991,
\]

\[
D_1=D=110t+209,
\]

\[
P_1=111t+220.
\]

逐式检查：

\[
D=10P_1-Q_0,
\]

\[
S_R=P_2+P_3-Q_0=-10w,
\]

\[
10D_1=Q_0+w,
\]

\[
Ud_2+10(UW)=a_3=1,
\]

\[
10a_2+a_3
=
11(UW)+10UD_1
=
1001.
\]

同时：

\[
a_2=100
\]

是三位数，

\[
a_3=1
\]

是一位数，并且：

\[
U/u_0=1\in[1,10)=K_{MN}.
\]

所以它通过：

- deflated core；
- exact mantissa identity；
- RRGS-1/2；
- digit windows；
- SRUS radial interval；
- unit gate \(U=1\)。

而：

\[
\xi_-=Uw=100t+99\to\infty.
\]

它**不是 source solution**，因为 primitive sphere 失败：

\[
Q_0^2-(P_1^2+P_2^2+P_3^2)
=
987679t^2+3933160t+2915680
>0.
\]

因此该 witness 的合法结论是：

\[
\boxed{
\text{RRGS + endpoint/SRUS information class alone
不能给 uniform negative }\xi_-\text{ bound}.
}
\]

它同时精确指出下一条 independent information 必须来自：

\[
\boxed{
\text{primitive sphere / axis geometry}.
}
\]

所以最终 verdict 不是 “impossible forever”，而是：

```text
SIGNED_RRGS_PARTIAL
```

---

## 11.5 J2 只能作为 repair-capacity witness，不能迁移 theorem

历史 J2-private 工作曾通过：

- strong \(P_2\)-axis theorem；
- \(d_2/Q_0\) upper bound；
- second numerator digit window；

得到：

\[
Ud_2<\eta\frac{uG^3}{K},
\]

进而：

\[
U|W|<\eta\frac{uG^2}{K}.
\]

这说明 Repair Criterion 不是空想。

但它依赖 J2-specific chart，不能机械升级成 general-\(J\) theorem。

因此 R4 若想 reunify signs，必须重新在 non-\(J2\) source 语义中证明对应的 \(Ud_2\) bound。

---

# Part XII — Counterexample / Failure Ledger

| Candidate conjecture | R3 verdict | Exact reason |
|---|---|---|
| fixed \((\xi,U,W)\) uniquely determines endpoint | KILLED AT INFORMATION-CLASS LEVEL | \(C_2,C_3,d_2\) remain moving |
| RRGS mod \(U\) gives new endpoint residue | REDUNDANT | reduces to \(U\mid a_3\) |
| unimodular cross-product is only old \(W\) | FALSE | \(D_{\rm rad}=\bar A_J(U-G)-1\) is independent |
| determinant spacing is too weak | FALSE | obtains \(\ge J/\bar A_J\) |
| endpoint interval is automatically near canonical slope | NOT PROVED / ARCHITECTURE FAIL | no \(K_{MN}\to\bar B_J/\bar A_J\) bridge |
| H5.1 becomes globally finite after successor compression | NOT OBTAINED | \(B_+\sim10^{n_3-1}\), \(n_3\) moving |
| negative RRGS is sign-symmetric | FALSE | inequality orientation reverses |
| negative RRGS has no useful remnant | FALSE | \(0<\xi_-<(d_*/G)Ud_2\) |
| RRGS+digits alone bound negative \(\xi_-\) | FALSE | explicit \(t\)-pseudo-family above |
| primitive sphere is dispensable after endpoint compression | FALSE AS ARCHITECTURE | negative witness survives everything listed except sphere |

---

# Part XIII — Updated 95 Frontier

R2 frontier：

\[
\begin{aligned}
A_1^{95,\rm live}(R2)
={}&
\mathcal H_0
\sqcup
\mathcal H_R^{\rm gen}
\sqcup
\mathcal H_{5,1}\\
&\sqcup
\mathcal H_{5,2}^{-}
\sqcup
\mathcal H_{5,3}^{-}
\sqcup
\mathcal H_{T0}
\sqcup
\mathcal H_{T1}
\sqcup
\mathcal H_{O+}
\sqcup
\mathcal H_{O-}.
\end{aligned}
\]

R3 没有诚实删除新的 full source class。

因此集合层面：

\[
\boxed{
A_1^{95,\rm live}(R3)
=
A_1^{95,\rm live}(R2).
}
\]

但 information representation 已改变：

\[
\boxed{
\mathcal H_{R,+}^{\rm succ}
}
\]

现在带有：

\[
\boxed{
(\xi,U,W)
\to
(d_2,C_3)
\to
(e_3,\delta_3)
\to
\text{primitive/source replay}
}
\]

的 exact dependency map。

negative：

\[
\boxed{
\mathcal H_{R,-}^{W}
}
\]

现在升级为：

\[
\boxed{
\mathcal H_{R,-}^{Ud_2}
}
\]

其明确缺口是：

\[
\boxed{
Ud_2\text{ upper bound}.
}
\]

若把 \(J=5,g=1\) 单独按符号拆开，则：

\[
\mathcal H_{5,1}
=
\mathcal H_{5,1}^{+}
\sqcup
\mathcal H_{5,1}^{-},
\]

两者本轮均未删除。

所以 R3 的真实推进是：

\[
\boxed{
\text{dependency exactization}
+
\text{architecture kill}
+
\text{negative repair datum identification},
}
\]

而不是集合 cardinality reduction。

---

# Part XIV — R4 Launch Decision

最多保留三个下一步。

## Path A — Positive terminal closure：Successor-conditioned Primitive Root Gate

positive endpoint architecture 已被处决，因此不要继续给 determinant 加模数。

下一步应把 R2/J5 已经证明有效的：

\[
\text{primitive sphere}
+
\text{square}
+
\text{integral root}
+
\text{root divisibility}
\]

推广为 symbolic non-\(J2\) successor-conditioned gate。

目标形式：

\[
(\xi,U,W,C_3,k;\text{structural tuple})
\Longrightarrow
\text{one exact root-factor equation}.
\]

真正需要让：

\[
d_2
\]

或：

\[
C_3
\]

进入 primitive/root equation，从而补上 R3 缺失的信息类。

**优先级：1。**

---

## Path B — Negative sign reunification：General non-\(J2\) \(Ud_2\) theorem

直接攻击：

\[
\boxed{
Ud_2<L(\text{structural tuple}).
}
\]

合法来源优先：

- primitive \(P_2/Q_0\) axis lower bound；
- \(d_2/Q_0\) sharp estimate；
- actual second numerator digit；
- source-labelled sphere identity。

一旦成立：

\[
\xi_-=U|W|
\]

立刻 finiteize。

**优先级：2。**

---

## Path C — Moving-tail extinction：\(n_3-g\) / H5.1 source theorem

H5.1 证明：

\[
\text{fixed-fibre finite}
\]

无法升级成：

\[
\text{global finite}
\]

的真正原因是 moving \(n_3-g\)。

因此需要一个新 information class：

\[
\boxed{
\text{full decimal word / carry / primitive-tail relation}
}
\]

直接约束：

\[
n_3-g
\]

或使 large tail 自动违反 primitive/root gate。

这比继续 cyclotomic prime search 更有价值。

**优先级：3。**

---

# Theorem Ledger

## 95-R3-T1 — Finite Successor Canonicalization

```text
STATUS = PROVED / FROZEN
```

\[
0<\xi<u_0d_*10^{n_3-g},
\quad
\gcd(\xi,u_0)=1,
\quad
U\mid\xi,
\quad
W=\xi/U.
\]

---

## 95-R3-T2 — Successor-conditioned Endpoint Formula

```text
STATUS = PROVED
```

\[
u_0e_3
=
Ud_2+K_*\xi-u_0 10^{n_3-1}.
\]

结论：

```text
ENDPOINT_EXACT = YES
ENDPOINT_SUCCESSOR_DETERMINED = NO
```

---

## 95-R3-T3 — Unimodular Cross-Product Lemma

```text
STATUS = PROVED
NOVELTY = PASS
```

\[
D_{\rm rad}
=
\bar A_JU-u_0\bar B_J
=
\bar A_J(U-G)-1,
\]

\[
|D_{\rm rad}|\ge Ju_0,
\]

\[
\left|
\frac U{u_0}
-
\frac{\bar B_J}{\bar A_J}
\right|
\ge
\frac{J}{Ju_0+1}.
\]

---

## 95-R3-T4 — Decimal Endpoint Upper Separation

```text
STATUS = NOT OBTAINED
FAILURE = NO_ENDPOINT_TO_UNIMODULAR_SLOPE_BRIDGE
```

---

## 95-R3-T5 — Positive Successor Non-Hit

```text
STATUS = NOT PROVED
REPLACEMENT_VERDICT = POSITIVE_ENDPOINT_ARCHITECTURE_FALSIFIED
```

---

## 95-R3-T6 — Signed-RRGS Verdict

```text
STATUS = SIGNED_RRGS_PARTIAL
```

\[
0<U|W|<\frac{d_*}{G}Ud_2.
\]

Repair criterion：

\[
Ud_2<L
\Longrightarrow
U|W|<\frac{d_*L}{G}.
\]

---

# Provenance / Canonical Inputs

本报告只使用并重组以下已归档资产：

- `95_R2_NonJ2_Resonant_Cyclotomic_Endpoint_Collision.md`
- `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
- `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`
- `strict_layer_A1_endpoint_quotient_integer_alignment_campaign.md`
- `strict_layer_A1_resonant_transition_reduced_fraction_unit_exclusion_campaign.md`
- `strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md`
- pre-specialization RRGS archive (`Part I — Executive Status.md`)
- J2-only reports仅用于 **capacity comparison / repair witness**，不作为 general-\(J\) theorem 迁移。

---

# Final One-Line Verdict

\[
\boxed{
\textbf{R2 把 positive resonance 压成 finite successor；}
\quad
\textbf{R3 证明 determinant spacing 是真的，但 endpoint bridge 不存在于当前信息类。}
}
\]

因此：

\[
\boxed{
\textbf{下一步必须引入 primitive/root 或 }Ud_2\textbf{ 这种真正独立的 source datum，}
}
\]

而不是继续给 cyclotomic / endpoint architecture 加模数。
