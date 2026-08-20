# 95-R9 — Outer-Plus No-Borrow Projective-Smallness Assault

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Ownership:** \(A_1^{95}=A_1\cap\{J\neq2\}\)  
**Round:** 95-R9  
**Main theatre:** \(\mathcal H_{O+}\)  
**Main archive:** `95_R9_Outer_Plus_No_Borrow_Projective_Smallness_Assault.md`

---

# Part I — Executive Verdict

本轮不能签发

```text
OUTER_PLUS_CLOSED
```

也不能签发

```text
OUTER_PLUS_DEEP_TAIL_CLOSED
```

或

```text
OUTER_PLUS_STRUCTURALLY_COMPRESSED
```

因为没有证明任何绝对 \(D\) 使 \(d<-D\) 无解，也没有得到 \(b_2,k,-d\) 中两项的 uniform bound。

本轮正式 verdict 为：

```text
OUTER_PLUS_PROJECTIVE_ARCHITECTURE_INSUFFICIENT
```

更精确地：

```text
OUTER_PLUS_STATUS = OPEN
OUTER_PLUS_PROJECTIVE_SMALLNESS = PROVED
OUTER_PLUS_DEEP_D_EXTINCTION = NOT_PROVED
OUTER_PLUS_D_DEPENDENCE_CANCELS_AT_FIXED_G = YES
OUTER_PLUS_PRIMITIVE_LOWER_WINDOW_DECAYS_WITH_G = YES
OUTER_PLUS_R8_STYLE_DENOMINATOR_COLLAPSE = KILLED
OUTER_PLUS_NO_BORROW_DIVISOR_GAP = NOT_UNIFORM
OUTER_PLUS_CURRENT_PROJECTIVE_ARCHITECTURE = SATURATED
```

本轮最重要的正结论有三个。

第一，outer-plus 确实具有 genuine deep-\(d\) projective smallness。由
\[
m_2=g+d\ge1
\]
可得
\[
g\ge1-d.
\]
结合 Smith-reduced projective window，
\[
\boxed{
10^{-(2g+k+2)}
<
\frac{P_3}{P_2}
<
10^{-(2g+k-2)},
}
\]
得到
\[
\boxed{
\frac{P_3}{P_2}
<
10^{2d-1}
<
10^d
\qquad(d\le-1).
}
\tag{R9-PROJ-D}
\]
因此 prompt 中主动要求证伪的
\[
P_3/P_2<10^d
\]
并没有被反例杀掉，而是被升级为 theorem。

第二，这种 deep-\(d\) smallness **不能**与当前 primitive/source lower window形成碰撞。历史独立 primitive axis theorem 只给
\[
\boxed{
\frac{P_3}{P_2}
>
\frac{1}{1100}\,10^{-(2g+k)},
}
\tag{R9-PRIM-LOW}
\]
它与 upper window 同样按 \(10^{-(2g+k)}\) 衰减。由于 deep negative \(d\) 只强迫
\[
g\ge1-d
\]
而不控制 \(g\) 的上界，因此不存在由当前信息推出的
\[
P_3/P_2\ge c>0
\]
或任何只依赖 \(d\) 的正 lower window。

第三，\(d\) 对 source ratio 与 transverse Smith ratio的影响会**精确反向吸收**。有
\[
\boxed{
\frac{P_3}{P_2}
=
\frac{\alpha t}{v}\frac NM.
}
\]
其中 denominator digit words 强迫
\[
\boxed{
10^{n_3-d-1}
<
\frac v{\alpha t}
<
10^{n_3-d+1},
}
\tag{R9-TRANS}
\]
而 common-\(U\) numerator words 强迫
\[
\boxed{
10^{n_3-n_2-1}
<
\frac NM
<
10^{n_3-n_2+1}.
}
\tag{R9-SOURCE}
\]
乘起来后
\[
d
\]
完全消失，恢复上面的 \(10^{-(2g+k)}\) projective window。

因此 R9 对本轮核心架构的精确 kill label 为：

```text
PROJECTIVE_UPPER_DECAYS_WITH_DEEP_D_ONLY_THROUGH_G
TRANSVERSE_SMITH_RATIO_SYNCHRONOUSLY_ABSORBS_D
PRIMITIVE_LOWER_DECAYS_AT_THE_SAME_10^{-(2g+k)}_SCALE
NO_CURRENT_SOURCE_LEVEL_D_INDEPENDENT_LOWER_RATIO_BOUND
```

---

# Part II — Frozen R8 Decision

R8 已经证明：

```text
H0_STATUS = OPEN_AT_INTEGER_SUCCESSOR
H0_DOMINANT_GATE = I
H0_LAYER_P_ACTIVATED = NO
```

并在 \(g=0\)、plus 中得到
\[
\boxed{
b_2\le10,\qquad
m_2\le2,\qquad
k\le4,\qquad
n_2\le6,\qquad
U<10^6.
}
\]

但 R8 同时明确审计：

```text
CROSS_THEATRE_POSITIONAL_THEOREM = NO
```

其 denominator collapse 使用了 \(g=0\) 的特殊 tail cancellation，不能直接迁移到 \(g\ge1\)。

因此 R9 不继续 H0 的原因是：H0 已经到达 Layer-I positional frontier，但 R8 没有产生一个可迁移的新 positional theorem；在没有新信息类时继续 floor/ceiling 只会重复旧架构。

---

# Part III — Outer-Plus Canonical Definition

从 R1 / exact-word / Smith source-of-truth 恢复：

\[
\boxed{
\mathcal H_{O+}
:
\quad
g\ge1,\quad
d\le-1,\quad
J\neq2.
}
\]

A1 exponent normal form：
\[
g=m_3-n_3\ge0,
\qquad
d=m_2-g,
\qquad
k\ge1,
\]
\[
\boxed{
m_2=g+d,\qquad
n_2=2g+k+d,\qquad
m_3=n_3+g.
}
\tag{EXP}
\]

由于 \(m_2\) 是 \(b_2\) 的 decimal digit length：
\[
\boxed{m_2\ge1.}
\]
所以 outer-plus 立即有
\[
\boxed{
g\ge1-d.
}
\tag{GD}
\]

primitive sphere：
\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

exact word core：
\[
D=P_110^k-Q_0>0,
\]
\[
H=b_2Q_0-b_110^{m_2}D\ne0,
\]
\[
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbf Z_{>0},
\]
\[
b_2P_2=10^gH+K_3.
\]

outer branch map 给：
\[
\boxed{
d\le-1\Longrightarrow H<0.
}
\]

denominator mismatch：
\[
R:=b_210^{n_3}-b_3.
\]
对 \(d\le-1\)：
\[
\boxed{R<0.}
\]

所以 outer-plus 的 exact sign profile 为：
\[
\boxed{
H<0,\qquad R<0,\qquad HR>0.
}
\tag{OP-SIGN}
\]

这点与 H0 plus 的
\[
H<0,\quad R>0
\]
完全不同；R8 的 sign-to-sphere collapse不能迁移。

---

# Part IV — Historical Outer-Plus Asset Recovery

本轮实际使用的历史 kernel：

1. `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
   - non-\(J2\) ownership；
   - \(\mathcal H_{O+}\) canonical responsibility；
   - \(d\le-1\Rightarrow\) plus；
   - \(d=-1\) minus historical closure。

2. `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`
   - plus iff \(H<0\)；
   - plus exact prefix；
   - \(0<-H<Q_0\)；
   - \(d=-1\) minus closure；
   - large-negative plus 在 pure size layer仍兼容。

3. `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`
   - full Smith chart；
   - \(R=s\beta\widehat R\)；
   - outer \(d\le-1\) 中 \(H,R\) 同号；
   - strongest plus defect divisor / Smith-rich finite quotient；
   - Smith-poor 无 uniform divisor lower bound。

4. `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`
   - Full Smith–Radial Cancellation；
   - \(C_2=M/u_0,\ C_3=N/u_0\)；
   - \(P_2=vM,\ P_3=\alpha tN\)；
   - radial cone；
   - transverse unit sieve；
   - \(\sigma\)-to-\(\rho\) direct coupling被 exact cancellation处决。

5. `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`
   - primitive axis theorem；
   - plus
     \[
     P_3(1+10^{n_2-1})<Q_0;
     \]
   - moving projective boundary alone不能 closure。

6. `95_R8_g0_Smith_Reduced_Common_U_Three_Layer_Assault.md`
   - H0 plus denominator collapse；
   - 该 collapse 明确依赖 \(g=0\)，不可 cross-theatre transfer。

---

# Part V — No-Borrow Exact Word Structure

令
\[
\boxed{h:=-H>0.}
\]

plus exact prefix theorem 给：
\[
\boxed{
0<h<Q_0.
}
\tag{NB0}
\]

又
\[
H=b_2Q_0-b_110^{m_2}D,
\]
故
\[
\boxed{
10^{m_2}b_1D=b_2Q_0+h,
\qquad
0<h<Q_0.
}
\tag{NB1}
\]

因此：
\[
\boxed{
\left\lfloor
10^{m_2}\frac{b_1D}{Q_0}
\right\rfloor
=b_2.
}
\tag{NB2}
\]

这就是 outer-plus 的 canonical no-borrow theorem。

同样：
\[
\boxed{
\left\lfloor
\frac{b_1P_110^{m_2+k}}{Q_0}
\right\rfloor
=
b_110^{m_2}+b_2,
}
\tag{NB3}
\]
remainder 恰为 \(h\)。

## 5.1 关键修正：no-borrow word 的长度是 \(m_2\)，不是 \(-d\)

因为
\[
m_2=g+d,
\]
deep negative \(d\) 并不迫使 prefix 变长。

事实上对任意 \(r\ge1\)，取 structural profile
\[
d=-r,\qquad g=r+1
\]
就有
\[
\boxed{m_2=1.}
\]

所以：
\[
\boxed{
-d\to\infty
\not\Longrightarrow
m_2\to\infty.
}
\tag{NB-LENGTH-KILL}
\]

这直接处决了：

> “one-sided deep separation 自动产生越来越长 no-borrow prefix”

这一潜在机制。

---

# Part VI — \(d\)-Stratified Geometry

## 6.1 \(d=-1\)

\[
m_2=g-1\ge1
\Longrightarrow
g\ge2.
\]

历史 closure 只关闭：
\[
\boxed{d=-1,\ \text{minus}.}
\]

outer-plus 的 \(d=-1\) 仍 live。

denominator gap：
\[
b_210^{n_3}
\le
(10^{m_2}-1)10^{n_3}
=
10^{m_3-1}-10^{n_3},
\]
而
\[
b_3\ge10^{m_3-1}.
\]

故：
\[
\boxed{
R\le-10^{n_3}.
}
\tag{D1-R}
\]

但 \(H<0\) 与 \(R<0\) 同号，因此 Double-Smith affine form 中两个大项符号相反，不能推出固定 \(S_3\)-sign。

状态：

```text
d=-1 PLUS = OPEN
d=-1 MINUS = HISTORICALLY_CLOSED
d=-1 PROJECTIVE_ARCHITECTURE = NO_CLOSURE
```

## 6.2 \(d\le-2\)

因为
\[
m_2+n_3=m_3+d\le m_3-2,
\]
有
\[
b_210^{n_3}<10^{m_3-2},
\]
而
\[
b_3\ge10^{m_3-1}.
\]

所以：
\[
\boxed{
-R>9\cdot10^{m_3-2}.
}
\tag{DEEP-R}
\]

raw denominator mismatch 确实在 deep \(d\) 中很大。

但是这个大 mismatch 进入 Smith chart 后主要表现为
\[
v/(\alpha t)
\]
的大 decade，而该 transverse ratio 会在 \(P_3/P_2\) 中与 source ratio \(N/M\) 反向抵消。

因此 raw \(R\)-largeness 不自动形成 projective codimension。

---

# Part VII — Projective Smallness

Full Smith–Radial Cancellation：

\[
g_2=u_0v,\qquad
g_3=u_0\alpha t,
\]
\[
P_2=vM,\qquad
P_3=\alpha tN,
\]
\[
C_2=M/u_0,\qquad
C_3=N/u_0.
\]

于是：
\[
\boxed{
\frac{P_3}{P_2}
=
\frac{\alpha t}{v}\frac NM.
}
\tag{P-RATIO}
\]

## 7.1 Denominator transverse window

因为
\[
\frac v{\alpha t}
=
\frac{b_3}{b_2},
\]
而 \(b_i\) 是 \(m_i\)-digit：
\[
10^{m_3-m_2-1}
<
\frac{b_3}{b_2}
<
10^{m_3-m_2+1}.
\]

又：
\[
m_3-m_2=n_3-d,
\]
所以：
\[
\boxed{
10^{n_3-d-1}
<
\frac v{\alpha t}
<
10^{n_3-d+1}.
}
\tag{TW}
\]

## 7.2 Source common-\(U\) ratio window

合法 source 有：
\[
a_2=UC_2,\qquad a_3=UC_3.
\]

digit windows：
\[
10^{n_2-1}\le a_2<10^{n_2},
\qquad
10^{n_3-1}\le a_3<10^{n_3}.
\]

所以：
\[
\boxed{
10^{n_3-n_2-1}
<
\frac{C_3}{C_2}
=
\frac NM
<
10^{n_3-n_2+1}.
}
\tag{SW}
\]

## 7.3 Exact cancellation

将 (TW)、(SW) 代入 (P-RATIO)：

\[
\boxed{
10^{d-n_2-2}
<
\frac{P_3}{P_2}
<
10^{d-n_2+2}.
}
\]

使用
\[
n_2=2g+k+d
\]
得到：
\[
\boxed{
10^{-(2g+k+2)}
<
\frac{P_3}{P_2}
<
10^{-(2g+k-2)}.
}
\tag{PWIN}
\]

这里：
\[
\boxed{d\text{ 完全消失}.}
\]

等价地，用历史 \(\sigma,\rho\)：
\[
\boxed{
\frac{P_3}{P_2}
=
\frac{1}{\sigma\rho\,10^{2g+k}},
\qquad
0.1<\sigma,\rho<10.
}
\]

这就是 R9 的中央 projective theorem。

---

# Part VIII — Primitive/Source Ratio Lower Bound

历史独立 primitive axis theorem：
\[
\boxed{
\frac{Q_0}{1100\,10^{2g+k}}
<
P_3
<
100Q_0\,10^{-(2g+k)}.
}
\]

又
\[
P_2<Q_0,
\]
所以：
\[
\boxed{
\frac{P_3}{P_2}
>
\frac1{1100}\,10^{-(2g+k)}.
}
\tag{PRIM-L}
\]

这确实是一个 independent lower gate，但它不是 \(d\)-uniform lower gate。

因为 deep negative \(d\) 只给：
\[
g\ge1-d,
\]
而 \(g\) 仍可继续增大。

因此：
\[
\boxed{
\inf_{\text{current allowed }g}
\frac1{1100}\,10^{-(2g+k)}
=0.
}
\]

于是不存在当前信息可推出的：
\[
\boxed{
L_{\rm prim}>0
}
\]
independent of \(d\)。

更重要地，primitive lower 与 projective upper都具有同一个：
\[
\boxed{10^{-(2g+k)}}
\]
主尺度。

所以本轮没有：
\[
U_{\rm word}(d)<L_{\rm prim}.
\]

---

# Part IX — Large-\((|d|)\) Collision

尽管 direct \(d\)-dependence 在 fixed-\(g\) projective ratio中取消，outer legality还有：
\[
m_2=g+d\ge1.
\]

故：
\[
g\ge1-d.
\]

代入 (PWIN) 的 upper：
\[
\frac{P_3}{P_2}
<
10^{-(2g+k-2)}
\le
10^{-((3-2d)-2)}
=
10^{2d-1}.
\]

因此：

\[
\boxed{
\frac{P_3}{P_2}
<
10^{2d-1}.
}
\tag{DEEP-SMALL}
\]

而对 \(d\le-1\)：
\[
2d-1<d.
\]

所以：
\[
\boxed{
\frac{P_3}{P_2}<10^d.
}
\tag{PROMPT-CONJECTURE-PROVED}
\]

这说明 deep outer-plus **确实**被挤向 \(P_3=0\) face。

但没有 extinction，因为 lower window同时允许：
\[
P_3/P_2\to0.
\]

因此正确结论不是：

```text
DEEP_D_DOES_NOT_CAUSE_SMALLNESS
```

而是：

```text
DEEP_D_CAUSES_SMALLNESS
BUT_NO_INDEPENDENT_POSITIVE_LOWER_WINDOW_EXISTS
```

这一区分非常重要。

---

# Part X — Plus Tail / Sign Compression

plus：
\[
H=-h,\qquad0<h<Q_0.
\]

tail：
\[
b_2P_2=10^gH+K_3
\]
变成：
\[
\boxed{
K_3=b_2P_2+10^gh.
}
\tag{TAIL+}
\]

而：
\[
K_3
=
\frac{b_3(Q_0-P_3)}{10^{n_3}}.
\]

由于：
\[
b_3<10^{m_3}=10^{n_3+g},
\]
所以：
\[
\boxed{
K_3<10^g(Q_0-P_3)<10^gQ_0.
}
\]

于是：
\[
b_2P_2<K_3<10^gQ_0.
\]

用 growing-\(g\) axis theorem
\[
P_2>\sqrt{96/101}\,Q_0
\]
只得到：
\[
\boxed{
b_2<\sqrt{101/96}\,10^g.
}
\tag{TAIL-B2}
\]

但 original digit length 已经给：
\[
b_2<10^{m_2}=10^{g+d}\le10^{g-1}.
\]

而：
\[
10^{g-1}
<
\sqrt{101/96}\,10^g.
\]

所以 (TAIL-B2) **严格弱于**已有 digit bound。

因此：

\[
\boxed{
\text{R8 的 sign + tail + axis denominator collapse
在 outer-plus 中完全失去切割力。}
}
\]

machine verdict：

```text
OUTER_PLUS_R8_STYLE_SIGN_TAIL_DENOMINATOR_COMPRESSION = KILLED
```

## 10.1 为什么 H0 能压而 O+ 不能

H0 有：
\[
g=0
\]
所以：
\[
K_3<Q_0.
\]
于是 plus：
\[
b_2P_2<K_3<Q_0
\]
直接给 \(b_2\le10\)。

O+ 有：
\[
g\ge1
\]
所以只有：
\[
K_3<10^gQ_0,
\]
而这个 \(10^g\) 恰好吞掉所有 denominator compression。

---

# Part XI — Smith / Common-\(U\) Transfer

本轮确实得到 exact cross-layer relation：
\[
\boxed{
\frac{P_3}{P_2}
=
\lambda_{\rm Smith}\frac NM,
\qquad
\lambda_{\rm Smith}:=\frac{\alpha t}{v}.
}
\]

但：
\[
\lambda_{\rm Smith}
\]
不是 fixed，也不是 finite alphabet。

由 (TW)：
\[
\boxed{
10^{-n_3+d-1}
<
\lambda_{\rm Smith}
<
10^{-n_3+d+1}.
}
\]

因此当 \(d\to-\infty\) 时：
\[
\lambda_{\rm Smith}\to0
\]
at the exact opposite decimal rate needed to offset the motion of
\[
N/M.
\]

所以：

```text
PROJECTIVE_TO_COMMON_U_EXACT_TRANSFER = YES
TRANSFER_MULTIPLIER_FIXED_OR_FINITE = NO
D_SHIFT_SURVIVES_TRANSFER = NO
```

这精确回答了本轮最后的战略问题：

> 哪一个 source coordinate 跟着 \(d\) 同步退化？

答案是：
\[
\boxed{
\lambda_{\rm Smith}
=
\alpha t/v
=
g_3/g_2.
}
\]

等价地：
\[
\boxed{
v/(\alpha t)
}
\]
随 \(-d\) 同步增长。

---

# Part XII — No-Borrow Divisor Gap

plus：
\[
0<h=-H<Q_0.
\]

历史 Double-Smith 给：
\[
\boxed{
M_H^{(2)}
=
s\alpha\beta^\sharp v^\sharp
\mid h.
}
\]

因此 Smith-rich 时若
\[
M_H^{(2)}>Q_0/K,
\]
则：
\[
h/M_H^{(2)}\in\{1,\ldots,K-1\}.
\]

这是 genuine finite quotient reduction。

但历史已经证明存在 Smith-poor synchronized ambient families，因此没有 uniform：
\[
M_H^{(2)}\gg Q_0.
\]

更完整的 Smith-radial campaign虽可把 strongest known divisor进一步写成
\[
\mathcal M_{\max}\mid H,
\]
但同样没有 theorem 迫使：
\[
\mathcal M_{\max}\ge Q_0.
\]

deep \(d\) 也不能自动修复这一点：其大 transverse factor
\[
v/(\alpha t)
\]
可以主要落在 decimal \(2,5\)-support 上，ten-free residual factor并不必然增长。

因此：

```text
NO_BORROW_REMAINDER_HAS_INDEPENDENT_DIVISOR = YES
UNIFORM_LARGE_DIVISOR = NO
QUOTIENT_REMAINDER_GAP_CLOSURE = NO
```

注意第一行只表示“存在独立 divisor channel”，不是“该 divisor 足够大”。

---

# Part XIII — Counterexample / Conjecture Ledger

## C1 — \(P_3/P_2<10^d\)

```text
STATUS = PROVED
```

更强：
\[
\boxed{
P_3/P_2<10^{2d-1}.
}
\]

## C2 — \(d\le-2\Rightarrow\varnothing\)

```text
STATUS = NOT_PROVED
PROJECTIVE/SRUS ROUTE = FALSIFIED AS A STANDALONE CLOSURE ENGINE
```

见下文 reduced-information witness。

## C3 — \(b_2\) uniformly bounded

```text
STATUS = NOT_PROVED
CURRENT SIGN/TAIL METHOD = KILLED
```

tail 只给比原 digit bound更弱的 \(O(10^g)\) bound。

## C4 — \(N/M\asymp P_3/P_2\) with fixed/finitely controlled multiplier

```text
STATUS = DISPROVED
```

因为：
\[
\frac{N/M}{P_3/P_2}
=
\frac v{\alpha t},
\]
而该 ratio位于 moving decade
\[
(10^{n_3-d-1},10^{n_3-d+1}).
\]

## C5 — all no-borrow remainders carry a uniformly large divisor

```text
STATUS = DISPROVED AS A UNIFORM THEOREM
```

Smith-rich可 finite quotient，但 Smith-poor无 uniform lower。

## C6 — plus sign alone closes outer-plus

```text
STATUS = DISPROVED AS A CLOSURE ROUTE
```

对 deep \(d\) plus 已由 branch geometry强制成立；它不是新增 codimension。

## C7 — large \(|d|\) always impossible

```text
STATUS = NOT_PROVED
CURRENT PROJECTIVE ARCHITECTURE CANNOT ESTABLISH IT
```

---

# Part XIV — Reduced-Information Deep-\(d\) Witness

为证明 R9 的 architecture kill 不是“暂时没把常数 sharpen 好”，构造一个 exact **Smith-radial reduced-information witness**。

它不是 original candidate，也不声称满足 full \(P_1/Q_0\) leading word/master；它只用于测试本轮所依赖的：

- exponent profile；
- denominator digits；
- Smith-radial dictionary；
- source \(C_2/C_3\) windows；
- common-\(U\) C/I/P；
- projective ratio。

对任意：
\[
r\ge1
\]
令：
\[
d=-r,\qquad
g=r+1,\qquad
k=1.
\]

则：
\[
m_2=g+d=1,
\]
\[
n_2=r+3.
\]

取：
\[
n_3=n_2=r+3,
\qquad
m_3=n_3+g=2r+4.
\]

取 Smith data：
\[
s=\alpha=\beta=t=u=u_0=1,
\]
\[
v=10^{n_3-d}=10^{2r+3}.
\]

于是：
\[
b_2=1,
\qquad
b_3=v=10^{2r+3},
\]
且 \(b_3\) 恰为 \(m_3=2r+4\) digit。

取：
\[
M=N=1.
\]

则：
\[
g_2=v,\qquad
g_3=1,
\]
\[
P_2=v,\qquad
P_3=1,
\]
\[
C_2=C_3=1.
\]

有：
\[
\boxed{
\rho=1,\qquad
\sigma=1,
}
\]
以及：
\[
\boxed{
\frac{P_3}{P_2}
=
10^{-(2r+3)}
=
10^{-(2g+k)}.
}
\]

common-\(U\) interval为：
\[
10^{r+2}\le U<10^{r+3}.
\]

取：
\[
\boxed{
U=10^{r+2}+1.
}
\]

则：
\[
\gcd(U,V)=1
\]
因为 \(V=v\) 是 \(10\)-power，而 \(U\equiv1\pmod{10}\)。

所以该 reduced state 对所有 \(r\) 都同时通过：

```text
EXPONENT PROFILE
DENOMINATOR DIGIT LENGTHS
FULL SMITH-RADIAL DICTIONARY (2/3 coordinates)
CONTINUOUS COMMON-U CONE
INTEGER COMMON-U SUCCESSOR
COPRIME UNIT GATE
PROJECTIVE RATIO WINDOW
```

而：
\[
d=-r\to-\infty.
\]

它没有执行：

```text
P1/Q0 LEADING-WORD GATE
FULL SPHERE/MASTER COUPLING
FULL J != 2 SEMANTICS
```

因此它不是 full outer-plus pseudo-solution。

它的作用是证明：

\[
\boxed{
\text{R9 当前 projective + Smith-radial + common-U 信息类
本身允许任意深 }d.
}
\]

所以若未来要关闭 deep outer-plus，必须由上述尚未施加的 independent channel进入，而不能继续 sharpen同一 projective ratio。

---

# Part XV — Information Independence Audit

| 信息 | 来源 | 是否独立 | R9 作用 |
|---|---|---:|---|
| \(0<h<Q_0\) | plus/no-borrow word | YES | exact remainder |
| prefix floor \(=b_2\) | 同一个 \(H\)-word | NO（相对上一行） | 等价重写 |
| tail \(K_3=b_2P_2+10^gh\) | exact tail/source | PARTIAL | 但 denominator bound弱于 digit bound |
| \(N/M\) decade | common-\(U\) numerator words | YES | source ratio |
| \(v/\alpha t\) decade | denominator words/Smith | YES | transverse ratio |
| \(P_3/P_2=(\alpha t/v)(N/M)\) | Smith cancellation | NO new codimension | 使 \(d\) 精确抵消 |
| primitive \(P_3\) lower | sphere/axis geometry | YES | independent lower，但同尺度衰减 |
| \(M_H^{(2)}\mid h\) | Smith arithmetic | YES | finite quotient on rich states |
| \(M_H^{(2)}\gg Q_0\) | — | NOT AVAILABLE | divisor gap不能 closure |
| \(S_3\)-sign | affine sign geometry | NOT FIXED in O+ | H,R同号导致两项可取消 |

核心结论：

\[
\boxed{
\textbf{R9 找到了多个 independent information classes，}
}
\]

但：
\[
\boxed{
\textbf{它们目前没有在同一 quantity 上形成 incompatible windows。}
}
\]

最接近 collision 的 pair 是：

\[
\text{projective upper}
\quad\text{vs}\quad
\text{primitive lower},
\]
但二者都按：
\[
10^{-(2g+k)}
\]
缩放。

---

# Part XVI — Updated 95 Frontier

R9 没有 set-level 删除 \(\mathcal H_{O+}\)。

所以：
\[
\boxed{
\begin{aligned}
A_1^{95,\mathrm{live}}
={}&
\mathcal H_0
\sqcup
\mathcal H_R^{\rm gen}
\sqcup
\mathcal H_{5,1}
\sqcup
\mathcal H_{5,2}^{-}
\sqcup
\mathcal H_{5,3}^{-}\\
&\sqcup
\mathcal H_{T0}
\sqcup
\mathcal H_{T1}
\sqcup
\mathcal H_{O+}
\sqcup
\mathcal H_{O-}.
\end{aligned}
}
\]

状态更新：

```text
H0 = OPEN_AT_INTEGER_SUCCESSOR / FROZEN_FOR_NEW_INFORMATION
RESONANCE = PAUSED / ARCHITECTURE_SATURATED
T0 = OPEN_BUT_ARCHITECTURE_FROZEN
T1 = FROZEN
O+ = OPEN / PROJECTIVE_SMALLNESS_ARCHITECTURE_FROZEN
O- = OPEN / NOT_AUTO_ACTIVATED
```

outer-plus minimal live statement：

\[
\boxed{
\begin{gathered}
g\ge1,\quad d\le-1,\quad m_2=g+d\ge1,\quad J\ne2,\\
H<0,\quad R<0,\quad 0<-H<Q_0,\\
10^{-(2g+k+2)}
<
P_3/P_2
<
10^{-(2g+k-2)},\\
P_3/P_2<10^{2d-1},\\
U/u_0\in K_{MN},\quad \gcd(U,V)=1,\\
\text{且尚缺 independent transverse/positional/source obstruction.}
\end{gathered}
}
\]

---

# Part XVII — R10 Launch Decision

题设要求：若 O+ projective architecture失败，不得自动进入 O−，必须先比较 O−、H0、新 positional invariant 与历史 residual families。

本轮比较如下。

### O−

当前有：
\[
1\le c\le10^d
\]
且 \(d\ge2\) 时 carry alphabet随 \(d\) 膨胀。R9 没有产生能控制这个 alphabet 的新 theorem。

**不启动。**

### H0

H0 的 Layer-I gate最具体，但 R9 没有产生新的 positional-\(U\) theorem；直接返回只会重复 R8。

**暂不重开。**

### Resonance / Transition

均已有 architecture freeze；R9 没有带来可合法解冻的新 information class。

**不重开。**

### O+

本轮已经证明 projective smallness，但也精确找出同步退化 coordinate
\[
\alpha t/v.
\]
继续 sharpen同类 projective bounds的边际价值很低。

因此 R10 正式选择：

\[
\boxed{
\textbf{Path E — Second 95 Architecture Shock Checkpoint}.
}
\]

machine-readable：

```text
R10_PATH = E_SECOND_95_ARCHITECTURE_SHOCK_CHECKPOINT
DO_NOT_AUTO_ATTACK_O_MINUS = YES
DO_NOT_RETURN_TO_H0_WITHOUT_NEW_POSITIONAL_INFORMATION = YES
DO_NOT_SHARPEN_O_PLUS_PROJECTIVE_RATIO = YES
```

R10 checkpoint 应只认可真正新的 information class，例如：

1. 一个不能从 digit windows 消掉的 transverse Smith constraint，直接约束
   \[
   \alpha t/v;
   \]

2. 一个 actual positional source theorem：
   \[
   U\equiv U_0\pmod D
   \]
   或等价 successor-phase restriction；

3. 一个 deep-\(d\) 强迫增长的 **ten-free** divisor，且独立整除
   \[
   h=-H;
   \]

4. 一个将 leading \(P_1/Q_0\) source word 与 \((M,N,u_0)\) 直接耦合的 exact equation，能够杀 Part XIV 的 reduced-information witness。

否则不得把同一批 ratio、prefix、tail、Smith factors重新排列后称为新架构。

---

# 95-R9 Theorem Ledger

## 95-R9-T1 — Outer-Plus No-Borrow Word Theorem

```text
STATUS = PROVED / RECOVERED
```

\[
0<-H<Q_0,
\]
\[
10^{m_2}b_1D=b_2Q_0-H,
\]
即写 \(h=-H\)：
\[
10^{m_2}b_1D=b_2Q_0+h,
\quad0<h<Q_0.
\]

并且：
\[
-d\to\infty
\not\Rightarrow
m_2\to\infty.
\]

## 95-R9-T2 — Outer-Plus Projective Smallness Theorem

```text
STATUS = PROVED
```

\[
10^{-(2g+k+2)}
<
P_3/P_2
<
10^{-(2g+k-2)}.
\]

进一步：
\[
\boxed{
P_3/P_2<10^{2d-1}<10^d.
}
\]

## 95-R9-T3 — Primitive/Source Ratio Lower Gate

```text
STATUS = RECOVERED
D_INDEPENDENT_POSITIVE_LOWER = NO
```

\[
P_3/P_2>
\frac1{1100}10^{-(2g+k)}.
\]

lower 与 upper 同尺度衰减。

## 95-R9-T4 — Deep-\(d\) Extinction / Compression

```text
DEEP_D_PROJECTIVE_SMALLNESS = YES
DEEP_D_EXTINCTION = NO
FINITE_D_STRIP = NOT_OBTAINED
```

## 95-R9-T5 — Plus Tail Denominator Compression

```text
R8_STYLE_DENOMINATOR_COLLAPSE = KILLED
SMITH_RICH_FINITE_QUOTIENT = RETAINED
UNIFORM_B2_BOUND = NOT_OBTAINED
```

## 95-R9-T6 — Outer-Plus Extinction / Minimal Frontier

```text
OUTER_PLUS_EXTINCTION = NOT_PROVED
OUTER_PLUS_PROJECTIVE_ARCHITECTURE_INSUFFICIENT = YES
```

---

# Final Strategic Verdict

R9 最初希望验证：

\[
d\to-\infty
\Longrightarrow
P_3/P_2\to0
\]
并让它撞上：
\[
P_3/P_2\ge c>0.
\]

第一半成立，而且比预期更干净：
\[
\boxed{
P_3/P_2<10^{2d-1}.
}
\]

第二半失败。

失败原因不是“primitive lower bound常数还不够好”，而是：

\[
\boxed{
\textbf{source ratio }N/M\textbf{ 与 transverse Smith ratio }\alpha t/v
\textbf{ 随 }d\textbf{ 反向同步移动。}
}
\]

其 product：
\[
P_3/P_2
\]
只读到：
\[
2g+k,
\]
而 deep \(d\) 仅通过：
\[
m_2=g+d\ge1
\]
间接迫使 \(g\) 增长。

所以 R9 最终判决是：

\[
\boxed{
\textbf{Outer Plus 确实被挤向 source cone 的 }P_3=0\textbf{ face，}
}
\]
但：
\[
\boxed{
\textbf{当前 primitive/source geometry 也允许该 face 同步退化，}
}
\]
因此：
\[
\boxed{
\texttt{OUTER\_PLUS\_PROJECTIVE\_SMALLNESS\_ARCHITECTURE\_INSUFFICIENT}.
}
\]

下一轮不应继续 sharpen \(P_3/P_2\)，而应先做第二次 95 Architecture Shock Checkpoint，重新决定哪一个全新的 information class 值得投入。
