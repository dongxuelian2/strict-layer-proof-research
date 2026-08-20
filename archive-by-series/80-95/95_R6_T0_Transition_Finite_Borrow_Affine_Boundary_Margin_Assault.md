# 95-R6 — T0 Transition Finite-Borrow Affine Boundary-Margin Assault

**文件名：** `95_R6_T0_Transition_Finite_Borrow_Affine_Boundary_Margin_Assault.md`  
**研究范围：** 三项十进制拼接平方和问题，Strict Layer — \(A_1\)-only  
**95 责任区：**
\[
A_1^{95}=A_1\cap\{J\neq2\}.
\]
**本轮主战区：**
\[
\mathcal H_{T0}.
\]

---

# Part I — Executive Verdict

本轮正式判决为

```text
T0_AFFINE_ARCHITECTURE_INSUFFICIENT
```

并且更精确地：

```text
T0_CLOSED=NO
T0_GLOBALLY_FINITE=NO
T0_AFFINE_EXACTIZED=YES
T0_FINITE_BORROW_CHAMBERS=YES
T0_REMAINDER_GLOBALLY_FINITE=NO_PROOF
T0_INDEPENDENT_S3_SPACING=NO
T0_AFFINE_TO_BOUNDARY_INTEGER_BRIDGE=NO
BACKWARD_2x5_NEW_T0_CODIMENSION=NO
T1_TRANSFER_ACTIVATED=NO
R7_PATH=C_TRANSITION_NEW_SOURCE_INVARIANT
```

这里 `T0_AFFINE_EXACTIZED=YES` 表示本轮把 \(d=0,R\neq0\) 的
inhomogeneous source system、四个 sign/borrow chambers、自然 affine
lattice spacing、actual source boundary integer 与 global freedom ledger
全部正规化；它**不**表示达到用户定义的 Level C，因为本轮没有证明
\(\widehat R\) 或 affine state 的 global finiteization。

本轮最重要的正结论不是 closure，而是：

\[
\boxed{
\textbf{T0 的非零 remainder 确实提供一个 resonance 中不存在的
inhomogeneous displacement；}
}
\]

但同时：

\[
\boxed{
\textbf{finite borrow 并没有把这个 displacement 转换成独立的
integer boundary spacing。}
}
\]

故 R5 的“transition 比 resonance 多一个 information class”判断只能升级为：

\[
\boxed{
\textbf{YES at affine-source level, NO at source-boundary codimension level.}
}
\]

---

# Part II — Frozen R5 Decision

R5 的冻结战略判决保持：

\[
\boxed{
\texttt{RESONANCE\_PAUSE\_TRANSITION\_ASSAULT}.
}
\]

理由保持不变：

1. exact resonance 在 R2–R5 已进入 information-class saturation；
2. transition 保留
   \[
   R\neq0,
   \]
   因而保留
   \[
   -M\widehat R
   \]
   这一真正 inhomogeneous displacement；
3. \(d=0\) 又把 prefix borrow 压到常数状态；
4. 因而 T0 是第一次测试
   \[
   \text{nonzero source remainder}
   +
   \text{finite borrow}
   \]
   能否产生第二 codimension 的最便宜战区。

本轮没有任何结果授权回到 resonance。

---

# Part III — T0 Canonical Definition

## 3.1 Exponent / branch skeleton

\[
\boxed{
g\ge1,\qquad d=0,\qquad R\neq0,\qquad J\neq2.
}
\]

由

\[
d=m_2-g
\]

得到：

\[
\boxed{
m_2=g,
\qquad
n_2=2g+k,
\qquad
m_3=n_3+g.
}
\]

primitive sphere：

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

定义：

\[
D=P_110^k-Q_0>0,
\]

\[
H=b_2Q_0-b_110^{m_2}D\neq0.
\]

sign convention：

\[
\boxed{\text{plus}\iff H<0},
\qquad
\boxed{\text{minus}\iff H>0}.
\]

对 \(d=0\)：

- plus 是 no-borrow chamber；
- minus 是 exactly one-borrow chamber。

为本轮统一表格，定义 chamber label

\[
c=
\begin{cases}
0,&H<0\quad(\text{plus/no borrow}),\\
1,&H>0\quad(\text{minus/one borrow}).
\end{cases}
\]

注意：历史上 \(c=\lceil H/Q_0\rceil\) 是 minus 的正式 borrow 定义；
plus 的 \(c=0\) 只是本轮的统一 chamber label，不改变旧语义。

并有：

\[
\boxed{
\text{plus}: -Q_0<H<0,
}
\]

\[
\boxed{
\text{minus}: 0<H<Q_0.
}
\]

## 3.2 Full Smith state

冻结：

\[
b_1=s\alpha u,
\qquad
b_2=s\alpha\beta t,
\qquad
b_3=s\beta v,
\]

\[
\gcd(\alpha,\beta)=1,
\qquad
\gcd(u,\beta t)=1,
\qquad
\gcd(\alpha t,v)=1.
\]

定义：

\[
\boxed{
\widehat R=\alpha t10^{n_3}-v,
}
\]

则：

\[
\boxed{
R=s\beta\widehat R.
}
\]

所以：

\[
\boxed{
\operatorname{sgn}R=\operatorname{sgn}\widehat R.
}
\]

并冻结：

\[
\boxed{
\gcd(\widehat R,\alpha t)=1,
}
\]

\[
\boxed{
\gcd(\widehat R,v)=\gcd(10^{n_3},v).
}
\]

令：

\[
P_2=vM,
\qquad
P_3=\alpha tN.
\]

Double Smith–Euclidean core：

\[
\delta_\beta=\gcd(\beta,10^{m_3}),
\qquad
\beta^\sharp=\frac{\beta}{\delta_\beta},
\]

\[
\Lambda_\beta=\frac{10^{m_3}}{\delta_\beta},
\qquad
\delta_v=\gcd(v,\Lambda_\beta),
\]

\[
v^\sharp=\frac v{\delta_v},
\qquad
J=\frac{\Lambda_\beta}{\delta_v},
\qquad
\gcd(v^\sharp,J)=1.
\]

存在

\[
Z\in\mathbb Z\setminus\{0\}
\]

使：

\[
\boxed{
tM10^{n_3}-A_3=JZ,
\qquad
A_3=\frac{Q_0-P_3}{\alpha},
}
\]

\[
\boxed{
H=s\alpha\beta^\sharp v^\sharp Z.
}
\]

故：

\[
\boxed{
\operatorname{sgn}Z=\operatorname{sgn}H.
}
\]

再定义：

\[
h_T=\gcd(tM,A_3),
\]

\[
h_T^\sharp=\frac{h_T}{\gcd(h_T,J)},
\]

历史 source 已给：

\[
h_T^\sharp\mid Z.
\]

故写：

\[
\boxed{
Z=h_T^\sharp q,
\qquad
q\in\mathbb Z\setminus\{0\}.
}
\]

## 3.3 Common-\(U\) semantic gate

Full Smith–Radial Cancellation：

\[
g_2=u_0v,
\qquad
g_3=u_0\alpha t,
\]

从而：

\[
\boxed{
C_2=\frac M{u_0},
\qquad
C_3=\frac N{u_0},
\qquad
u_0\mid M,N.
}
\]

原 source candidate 必须存在：

\[
U\in\mathbb Z_{>0}
\]

使：

\[
\boxed{
\frac U{u_0}\in
K_{MN},
}
\]

其中：

\[
K_{MN}
=
\left[
\max\!\left(
\frac{10^{n_2-1}}M,
\frac{10^{n_3-1}}N
\right),
\min\!\left(
\frac{10^{n_2}}M,
\frac{10^{n_3}}N
\right)
\right),
\]

并且：

\[
\boxed{
\gcd(U,V)=1,
\qquad
V=s\beta u_0v\alpha t.
}
\]

这一步不能从 affine ambient state 中删除。

---

# Part IV — Finite-Borrow Chamber Table

定义：

\[
d_2:=Q_0-P_2>0,
\]

\[
S_3:=P_2+P_3-Q_0=P_3-d_2.
\]

又定义：

\[
A_T:=\alpha Jh_T^\sharp q=\alpha JZ,
\]

\[
B_T:=M\widehat R.
\]

则：

\[
\boxed{
S_3=A_T-B_T.
}
\]

四个 T0 chambers 为：

| chamber | branch | \(c\) | sign \(H=Z=A_T\) | sign \(R=\widehat R=B_T\) | \(S_3\) geometry | status |
|---|---|---:|---|---|---|---|
| T0-P+ | plus | 0 | \(<0\) | \(>0\) | \(S_3<0\), sum-type | sign-mismatch |
| T0-P- | plus | 0 | \(<0\) | \(<0\) | \(S_3=-|A_T|+|B_T|\) | cancellation |
| T0-M+ | minus | 1 | \(>0\) | \(>0\) | \(S_3=|A_T|-|B_T|\) | cancellation |
| T0-M- | minus | 1 | \(>0\) | \(<0\) | \(S_3>0\), sum-type | sign-mismatch |

因此：

\[
\boxed{
\mathcal H_{T0}
=
\mathcal H_{T0}^{P+}
\sqcup
\mathcal H_{T0}^{P-}
\sqcup
\mathcal H_{T0}^{M+}
\sqcup
\mathcal H_{T0}^{M-}.
}
\]

这是正式的：

\[
\boxed{
\textbf{95-R6-T1 — T0 Finite-Borrow Chamber Theorem}.
}
\]

### Sign-mismatch exact absorption

在 T0-P+：

\[
\boxed{
d_2-P_3
=
|S_3|
=
\alpha J|Z|+M|\widehat R|
\ge
\alpha J+M.
}
\]

在 T0-M-：

\[
\boxed{
P_3-d_2
=
|S_3|
=
\alpha J|Z|+M|\widehat R|
\ge
\alpha J+M.
}
\]

所以两类 mismatch chamber 都满足：

\[
\boxed{
M<|S_3|,
\qquad
\alpha J<|S_3|.
}
\]

特别：

### plus / \(R>0\)

\[
|S_3|=d_2-P_3<d_2,
\]

故：

\[
\boxed{
M<d_2,
\qquad
\alpha J<d_2.
}
\]

又 \(P_2=vM\)，得：

\[
\boxed{
v>\frac{P_2}{d_2}.
}
\]

结合 frozen axis bounds：

\[
\frac{P_2}{Q_0}>\sqrt{96/101},
\qquad
\frac{d_2}{Q_0}<2.532\,10^{-2k},
\]

得到：

\[
\boxed{
v>
\frac{\sqrt{96/101}}{2.532}10^{2k}
>
0.385\,10^{2k}.
}
\]

这是 d=0 plus / \(R>0\) 的 exact Smith-absorption strengthening。

### minus / \(R<0\)

\[
|S_3|=P_3-d_2<P_3,
\]

故：

\[
\boxed{
M<P_3,
\qquad
\alpha J<P_3.
}
\]

又：

\[
v=\frac{P_2}{M}>\frac{P_2}{P_3}.
\]

由：

\[
\frac{P_3}{Q_0}<100\,10^{-(2g+k)}
\]

得到：

\[
\boxed{
v>
\frac{\sqrt{96/101}}{100}\,10^{2g+k}.
}
\]

这些是 genuine transition compression，但它们把巨大因子推入 transverse
Smith coordinate \(v\)，而 Full Smith–Radial Cancellation 告诉我们
\(v\) 不进入 projective endpoints；它只进入最终 unit sieve。
因此这些吸收不等于 radial closure。

---

# Part V — Inhomogeneous Affine Normal Form

本轮正式冻结：

\[
\boxed{
S_3
=
\alpha Jh_T^\sharp q
-
M\widehat R.
}
\tag{T0-AFF}
\]

同时：

\[
\boxed{
Q_0
=
\alpha t(M10^{n_3}+N)
-
\alpha Jh_T^\sharp q.
}
\tag{T0-Q}
\]

## 5.1 Exact scale identity

由：

\[
10^{m_3}H=b_3\alpha X_0,
\qquad
X_0=JZ,
\]

且：

\[
Z=h_T^\sharp q,
\]

得到：

\[
\boxed{
\alpha Jh_T^\sharp q
=
\frac{10^{m_3}}{b_3}H.
}
\]

令：

\[
\beta_3=\frac{b_3}{10^{m_3}}\in[0.1,1),
\]

则：

\[
\boxed{
A_T
=
\alpha Jh_T^\sharp q
=
\frac{H}{\beta_3}.
}
\tag{AT-SCALE}
\]

因此 d=0 finite borrow 给出的真正 scale 是：

\[
\boxed{
|H|<Q_0
\Longrightarrow
0<|A_T|<10Q_0.
}
\]

这只是一个 **normalized constant-width slab**：

\[
-10<\frac{A_T}{Q_0}<10,
\]

不是 \(O(1)\) 个 integer states。

## 5.2 Natural normalizations

\[
\boxed{
\frac{S_3}{M}
=
\alpha Jh_T^\sharp\frac qM
-
\widehat R.
}
\]

定义：

\[
\eta:=\frac qM.
\]

则：

\[
\boxed{
\frac{S_3}{M}
=
\alpha Jh_T^\sharp\eta-\widehat R.
}
\tag{ETA}
\]

但：

- \(M\) moving；
- \(q\) moving；
- \(\eta\) 不是固定 denominator 的整数 lattice；
- \(\alpha,J,h_T^\sharp\) 仍 moving。

所以这不是 finite-state reduction。

另有：

\[
\frac{\widehat R}{\alpha J}
=
\frac{\alpha t10^{n_3}-v}{\alpha J},
\]

当前没有 source theorem 把它压进 fixed finite rational grid。

## 5.3 Symbolic elimination audit

由：

\[
S_3=vM+\alpha tN-Q_0,
\]

\[
\widehat R=\alpha t10^{n_3}-v,
\]

得：

\[
S_3+M\widehat R
=
\alpha t(M10^{n_3}+N)-Q_0.
\]

故：

\[
\boxed{
S_3+M\widehat R
=
\alpha Jh_T^\sharp q
}
\]

与 (T0-Q) 是同一个 affine information class 的两种写法。

因此：

```text
AFF_PLUS_Q0_AS_TWO_EQUATIONS = REDUNDANT
```

同理：

\[
\boxed{
\alpha Jh_T^\sharp
\mid
S_3+M\widehat R
}
\]

只是 \(q\in\mathbb Z\) 的重写，不是新的 independent divisor of \(S_3\)。

这完成：

\[
\boxed{
\textbf{95-R6-T2 — Inhomogeneous Remainder Normal Form}.
}
\]

---

# Part VI — \(\widehat R\) Arithmetic

## 6.1 Primitive residual facts

\[
\boxed{
\widehat R=\alpha t10^{n_3}-v\neq0,
}
\]

\[
\boxed{
\gcd(\widehat R,\alpha t)=1,
}
\]

\[
\boxed{
\gcd(\widehat R,v)=\gcd(10^{n_3},v).
}
\]

因此：

\[
\boxed{
\gcd(\widehat R,\alpha tv)^{\langle10\rangle}=1.
}
\]

这意味着 nonzero remainder 是 genuine source datum；
但它并不自动带 useful odd prime。

历史 exact denominator skeleton 已明确允许 unit residual \(R=\pm1\)，
而旧 Smith audit 也明确记录 \(\widehat R=\pm1\) / pure \(2,5\)-smooth
不能被一般理论排除。

因此：

```text
R_NONZERO_IMPLIES_LARGE_GAP = FALSE
R_NONZERO_IMPLIES_NEW_ODD_PRIME = FALSE
```

但本轮**没有恢复一个 T0 source-valid unbounded \(\widehat R\) family**，
所以以下命题不能被伪装成“已反例处决”：

```text
|Rhat|=O(1) on full T0
```

它在本轮的正确状态是：

```text
NOT_PROVED / NO_T0_COUNTEREXAMPLE_RECOVERED
```

然而 current source system 也没有任何机制证明它。

## 6.2 Exact \(2/5\)-adic valuation audit

取 \(p\in\{2,5\}\)，记：

\[
a=\alpha t,
\qquad
r=v_p(v).
\]

由：

\[
\widehat R=a10^{n_3}-v,
\qquad
\gcd(a,v)=1,
\]

得到：

### Case 1 — \(p\mid a\)

此时 \(p\nmid v\)，故：

\[
\boxed{
v_p(\widehat R)=0.
}
\]

### Case 2 — \(p\nmid a\), \(r<n_3\)

两项 valuation 分别为 \(n_3\) 与 \(r\)，故：

\[
\boxed{
v_p(\widehat R)=r.
}
\]

### Case 3 — \(p\nmid a\), \(r>n_3\)

\[
\boxed{
v_p(\widehat R)=n_3.
}
\]

### Case 4 — \(p\nmid a\), \(r=n_3\)

\[
\widehat R
=
p^{n_3}
\left[
a\left(\frac{10}{p}\right)^{n_3}
-
\frac v{p^{n_3}}
\right],
\]

所以：

\[
\boxed{
v_p(\widehat R)
=
n_3
+
v_p\!\left(
a(10/p)^{n_3}-v/p^{n_3}
\right).
}
\]

因此 \(\widehat R\) 的 \(2/5\)-adic content 依赖 moving Smith coordinate
\(v\) 与临界 unit cancellation；它**不**由 \(c\in\{0,1\}\) 决定。

故：

```text
BACKWARD_SYNCHRONIZATION_LOCKS_RHAT_BY_C = NO
```

---

# Part VII — Affine Parameter Compression

本轮没有得到：

\[
\widehat R\to q\to h_T^\sharp\to S_3
\]

的 global finite chain。

## 7.1 Integrality gate

由 AFF：

\[
\boxed{
q
=
\frac{S_3+M\widehat R}
{\alpha Jh_T^\sharp}
\in\mathbb Z.
}
\]

故：

\[
\boxed{
\alpha Jh_T^\sharp
\mid
S_3+M\widehat R.
}
\]

但是该 gate 与定义完全等价，没有增加 codimension。

## 7.2 Why finite borrow does not finiteize \(q\)

\[
H
=
s\alpha\beta^\sharp v^\sharp h_T^\sharp q.
\]

d=0 给：

\[
|H|<Q_0.
\]

于是：

\[
|q|
<
\frac{Q_0}
{s\alpha\beta^\sharp v^\sharp h_T^\sharp}.
\]

只有当 denominator/Smith divisor 本身相对 \(Q_0\) 大时，
这才成为 finite small-\(q\) chamber。

Smith-poor states没有 uniform lower bound；历史上
“uniform \(|q|\le C\)”已经被 generic exact-word/Smith family否定。
本轮没有得到 d=0-specific repair。

因此：

```text
T0_Q_GLOBALLY_FINITE = NO_PROOF
T0_Q_FINITE_ON_SMITH_RICH_FIBRE = YES
```

但：

\[
\boxed{
\text{finite }q\text{ per structural fibre}
\not\Rightarrow
\text{global T0 finite}.
}
\]

---

# Part VIII — Boundary/Margin Construction

这是 R6 的核心审计。

## 8.1 Natural affine lattice spacing

令：

\[
A_T=\alpha Jh_T^\sharp q,
\qquad
B_T=M\widehat R.
\]

定义：

\[
\boxed{
\Lambda_{\rm aff}:=\gcd(|A_T|,|B_T|).
}
\]

因为：

\[
S_3=A_T-B_T,
\]

所以：

\[
\boxed{
\Lambda_{\rm aff}\mid S_3.
}
\]

因此若：

\[
S_3\neq0,
\]

自动：

\[
\boxed{
|S_3|\ge\Lambda_{\rm aff}.
}
\]

这给出一个很重要的 architecture fact：

> natural affine gcd spacing 本身不会“额外”制造 non-hit；
> 它只是说明任何 nonzero affine residual 已经落在该 lattice 上。

要 closure，仍必须从另一个独立 source 推出：

\[
0<|S_3|<\Lambda_{\rm aff}.
\]

当前没有这样的 source theorem。

### Mismatch chambers更强地杀掉 naive spacing hope

在 T0-P+ / T0-M-：

\[
|S_3|=|A_T|+|B_T|.
\]

而：

\[
\Lambda_{\rm aff}\le\min(|A_T|,|B_T|).
\]

故：

\[
\boxed{
|S_3|>\Lambda_{\rm aff}.
}
\]

所以在 sign-mismatch chambers 中，
“直接拿两 affine summands 的 gcd 当 boundary spacing”
**原则上不可能**给出所需的：

\[
0<|S_3|<\Lambda_{\rm aff}.
\]

这是本轮的 exact architecture kill。

在 sign-aligned chambers，
\(S_3\) 是 cancellation difference；
这里 small residual 可能发生，但任何 nonzero residual仍必须是
\(\Lambda_{\rm aff}\) 的倍数。
当前 decimal bounds没有把 cancellation 精确压到
一个小于 \(\Lambda_{\rm aff}\) 的 interval。

因此：

```text
95-R6-T4_AFFINE_DIVISIBILITY_BOUNDARY_GAP = NOT_ACHIEVED
NATURAL_AFFINE_GCD_SPACING = INSUFFICIENT
```

## 8.2 Actual source boundary integer

common-\(U\) replay 后，真正的 forbidden upper boundary不是抽象“整数附近”，
而是 actual numerator block hitting a power of ten。

### Face A

active upper endpoint：

\[
\frac U{u_0}<\frac{10^{n_3}}N.
\]

因为：

\[
a_3=UC_3=\frac{UN}{u_0},
\]

定义：

\[
\boxed{
B_T^{(A)}
:=
10^{n_3}-a_3
=
10^{n_3}-\frac{UN}{u_0}.
}
\]

合法 digit word严格给：

\[
\boxed{
B_T^{(A)}\in\mathbb Z_{\ge1}.
}
\]

而：

\[
B_T^{(A)}=0
\]

正是 forbidden upper endpoint。

等价乘 \(u_0\)：

\[
u_0B_T^{(A)}
=
10^{n_3}u_0-NU.
\]

### Face B

active upper endpoint：

\[
\frac U{u_0}<\frac{10^{n_2}}M.
\]

定义：

\[
\boxed{
B_T^{(B)}
:=
10^{n_2}-a_2
=
10^{n_2}-\frac{UM}{u_0}
\in\mathbb Z_{\ge1}.
}
\]

等价：

\[
u_0B_T^{(B)}
=
10^{n_2}u_0-MU.
\]

因此 R6 成功明确找到了：

\[
\boxed{
\textbf{T0 source boundary integer}.
}
\]

但 current AFF 中没有 \(U\)；
Full Smith–Radial Cancellation 又证明 exact-word/Smith 因子
不能靠 projective scaling自动恢复 \(U\)。

所以缺失的正是：

\[
\boxed{
\textbf{一条把 }
B_T^{(A/B)}
\textbf{ 与 }
(H,\widehat R,q,S_3)
\textbf{ 连接的独立整数关系。}
}
\]

这不是“margin 不够尖”，而是：

```text
NO_AFFINE_TO_SOURCE_BOUNDARY_INTEGER_BRIDGE
```

---

# Part IX — Backward Synchronization Audit

已有 backward A1 \(2\times5\) 工作表明：

1. 单独的 5-side phase/cut 不能强迫 2-side；
2. projected CRT 数据不能冒充 full exact \(2\times5\) source state；
3. common-\(U\) pullback 中 WGF/phase/normalized-gap 对 radial scale
   具有已审计的 equivariance / redundancy。

本轮的新 valuation audit进一步表明：

\[
v_2(\widehat R),v_5(\widehat R)
\]

并不由：

\[
d=0,\quad c=0,1
\]

锁死，而继续读取 moving \(v\) 与同层 unit cancellation。

因此：

```text
BACKWARD_SYNCHRONIZATION_REDUNDANT_AS_T0_SECOND_CODIMENSION
```

更精确地说：

- 它仍是合法 local sieve；
- 它可在给定 structural state 后删局部 residue；
- 但本轮没有恢复任何 theorem 使它成为
  \[
  \text{finite borrow}\to\text{fixed }v_2/v_5(\widehat R)
  \]
  的新 source equation。

---

# Part X — Source / Primitive Replay

本轮没有停在 ambient affine states。

任何 surviving T0 state仍必须通过：

\[
\boxed{
\frac U{u_0}\in K_{MN},
\qquad
\gcd(U,V)=1.
}
\]

这一 source gate。

### Why AFF does not automatically replay

AFF / T0-Q 只给：

\[
(M,N,Q_0,q,\widehat R;\alpha,t,J,h_T^\sharp)
\]

之间的 source-normalized affine关系。

actual boundary integer则读取：

\[
(U,M,N,u_0).
\]

所以二者共享 \(M,N\)，但没有共享一个已经冻结的第二 integer residual。

fixed-\(q\) sphere equation确实存在：

\[
(AMT-E)(AMT+2AN-E)
=
P_1^2+B^2M^2,
\]

其中：

\[
A=\alpha t,\quad
B=v,\quad
T=10^{n_3},\quad
E=\alpha Jh_T^\sharp q.
\]

但：

- \(A,B,E,P_1/M\) 仍 moving；
- finite \(q\) 不 finiteize \(M/N\)；
- radial endpoint 中 \(v,\alpha t\) 发生 Full Smith cancellation。

故：

```text
SOURCE_REPLAY_REQUIRES_NEW_PRIMITIVE_DATUM
```

当前最准确含义为：

\[
\boxed{
\textbf{需要一条 source-labelled cross-product / numerator-headroom
关系，把 affine residual 映射到 }B_T^{(A/B)}.
}
\]

---

# Part XI — Global Freedom Ledger

| variable | T0 status | reason |
|---|---|---|
| \(J\) | DEPENDENT / MOVING | \(J=\Lambda_\beta/\delta_v,\ J\neq2\)，无 transition absolute bound |
| \(g\) | MOVING | 仅 \(g\ge1\)，无 absolute bound |
| \(k\) | MOVING / DEPENDENT | 仅 height-type bounds |
| \(n_3\) | MOVING | 无 absolute bound |
| \(c\) | FINITE_ON_BRANCH | plus label 0；minus exactly 1 |
| \(R\) | DEPENDENT / MOVING | \(R=s\beta\widehat R\neq0\) |
| \(\widehat R\) | DEPENDENT / MOVING | \(\alpha t10^{n_3}-v\)，未 finiteize |
| \(q\) | DEPENDENT / MOVING | Smith-rich per-fibre finite；global no |
| \(h_T^\sharp\) | DEPENDENT / MOVING | gcd-derived |
| \(S_3\) | DEPENDENT / MOVING | affine residual / primitive geometry |
| \(M\) | MOVING | \(P_2=vM\) |
| \(N\) | MOVING | \(P_3=\alpha tN\) |
| \(u_0\) | MOVING | radial denominator |
| \(\alpha,t,v\) | MOVING | Smith coordinates |
| \(U\) | SOURCE-EXISTENTIAL / MOVING | terminal common-\(U\) gate |
| \(B_T^{(A/B)}\) | SOURCE-DEPENDENT / MOVING | actual numerator headroom |

真正被 T0 finite borrow直接 finiteize 的只有：

\[
\boxed{
\text{branch/carry label}.
}
\]

其余 global exponent / Smith / radial tails 均未被压成 finite set。

因此：

```text
T0_FINITE_PER_STRUCTURAL_FIBRE != T0_GLOBALLY_FINITE
GLOBAL_EXPONENT_TAIL_SURVIVES
```

---

# Part XII — Counterexample / Guillotine Ledger

本轮严格区分 `FALSIFIED` 与 `NOT PROVED`。

## C1 — \(R\neq0\) 自动给大 gap

```text
FALSIFIED
```

历史 denominator digit skeleton 可有：

\[
R=\pm1.
\]

所以：

\[
R\neq0
\]

不能当作 size lower bound。

## C2 — \(\widehat R\neq0\) 自动产生 useful odd prime

```text
FALSIFIED
```

\[
\widehat R=\pm1
\]

或 pure \(2,5\)-smooth 不能被 generic Smith theory排除。

## C3 — \(|\widehat R|=O(1)\) on full T0

```text
NOT PROVED
NO FULL-T0 COUNTEREXAMPLE RECOVERED
```

本轮不把“没有 theorem”伪装成反例。

## C4 — \(\widehat R\) uniquely determined by \(c\)

```text
NOT PROVED
STRUCTURALLY UNSUPPORTED
```

\(c\) 读取 \(H/Q_0\)，而 \(\widehat R\) 读取
\(\alpha t10^{n_3}-v\)；current source只通过 AFF连接它们，
没有 uniqueness theorem。

## C5 — \(q\) uniquely determined by \(\widehat R\)

```text
NOT PROVED
```

AFF 仍含：

\[
M,\ S_3,\ \alpha J h_T^\sharp.
\]

## C6 — \(S_3\) 总小于自然 divisor spacing

若自然 spacing 指：

\[
\Lambda_{\rm aff}=\gcd(A_T,B_T),
\]

则：

```text
FALSIFIED AS AN IDENTITY-LEVEL POSSIBILITY
```

因为：

\[
\Lambda_{\rm aff}\mid S_3,
\]

故：

\[
S_3\neq0
\Longrightarrow
|S_3|\ge\Lambda_{\rm aff}.
\]

mismatch chambers甚至：

\[
|S_3|=|A_T|+|B_T|>\Lambda_{\rm aff}.
\]

## C7 — T0 globally finite

```text
NOT PROVED
```

\(g,k,n_3,J,M,N,u_0\) 等 global tails仍 moving。

## C8 — plus/minus 可只靠“bounded carry”统一成同一个 boundary theorem

```text
FAILED AS CURRENT ARCHITECTURE
```

四室中：

- 两室是 sum-type；
- 两室是 cancellation-type。

因此 bounded carry alone不决定 affine margin geometry。

---

# Part XIII — T1 Transfer Audit

按 R6 纪律：

只有 T0 形成

\[
\text{finite borrow}
+
\text{inhomogeneous affine}
\Rightarrow
\text{finite boundary states / extinction}
\]

才允许正式 transfer 至 T1。

本轮没有得到这一 theorem。

而 T1：

\[
d=1
\]

只会把 minus carry 从 1 个扩成：

\[
1\le c\le10,
\]

并不会修复：

```text
NO_AFFINE_TO_SOURCE_BOUNDARY_INTEGER_BRIDGE
```

所以：

```text
95-R6-T6_T1_TRANSFER_VERDICT = NOT_ACTIVATED
```

这不是说 T1 一定更难；
只是 current R6 architecture 的失败点与 carry alphabet大小无关，
因此没有理由在本轮把同一失败 package复制十遍。

---

# Part XIV — Updated 95 Frontier

R6 没有删除：

\[
\mathcal H_{T0}.
\]

所以 R5 frontier 中 T0 保持 live。

形式上：

\[
\boxed{
A_1^{95,\mathrm{live}}(R6)
=
A_1^{95,\mathrm{live}}(R5).
}
\]

但 T0 的内部状态应升级为：

```text
T0 =
OPEN
/ FOUR_EXACT_SIGN_BORROW_CHAMBERS
/ INHOMOGENEOUS_AFFINE_EXACTIZED
/ SIGN_MISMATCH_ABSORPTION_PROVED
/ NATURAL_AFFINE_GCD_SPACING_INSUFFICIENT
/ ACTUAL_SOURCE_BOUNDARY_INTEGER_IDENTIFIED
/ AFFINE_TO_BOUNDARY_BRIDGE_MISSING
```

这比 R5 的：

```text
OPEN / LOW-CARRY / EXACT-AFFINE / HIGH-INDEPENDENCE
```

更精确。

尤其应把：

```text
HIGH-INDEPENDENCE
```

改写为：

```text
AFFINE_SOURCE_INDEPENDENCE = YES
BOUNDARY_CODIMENSION_INDEPENDENCE = NO
```

---

# Part XV — R7 Launch Decision

四条候选中，本轮选择：

\[
\boxed{
\textbf{Path C — transition new source invariant}.
}
\]

不选择：

### Path A — T0 terminal certificate / closure

因为：

\[
\mathcal H_{T0}
\]

未关闭。

### Path B — T1 transfer

因为 T0 architecture 未形成可 transfer theorem。

### Path D — outer-plus assault

outer-plus 的 carry确实更简单，
但它没有 T0 的 inhomogeneous low-state advantage；
在 T0 尚差“一条 affine-to-boundary source bridge”时立刻放弃 transition，
信息收益低于先攻击这个已经被精确命名的缺口。

## R7 唯一推荐 invariant target

定义 active source boundary integer：

\[
\boxed{
B_T=
\begin{cases}
10^{n_3}-a_3,&\text{Face A},\\
10^{n_2}-a_2,&\text{Face B}.
\end{cases}
}
\]

R7 不应再证明一个新的 \(H\)-divisor，也不应再 finiteize borrow。

唯一值得寻找的是一条**不能被 AFF elimination 消掉**的 source identity：

\[
\boxed{
\Phi_T
\bigl(
B_T,\widehat R,H,q,S_3;
\text{primitive/source data}
\bigr)=0
}
\]

满足至少一个：

1. 给
   \[
   D_T\mid B_T
   \]
   且 \(D_T>1\)；
2. 给
   \[
   0<B_T<1
   \]
   型 exact contradiction；
3. 给 fixed finite set
   \[
   B_T\in\mathcal B_T
   \]
   并可逐项 source replay；
4. 给一个真正的 cross-determinant，
   同时读取 affine displacement 与 common-\(U\) numerator headroom。

若不存在这样的 source invariant，
则 transition 的优势只能停留在 affine ambient 层，
届时才应正式重新分配 95 火力到 outer-plus / \(g=0\)。

---

# Theorem Ledger

## 95-R6-T1 — T0 Finite-Borrow Chamber Theorem

**PROVED.**

\[
\mathcal H_{T0}
\]

精确分为四个 sign/borrow chambers：

\[
(P+,P-,M+,M-),
\]

其中 \(c\in\{0,1\}\)。

---

## 95-R6-T2 — Inhomogeneous Remainder Normal Form

**PROVED / EXACTIZED.**

\[
\boxed{
S_3
=
\alpha Jh_T^\sharp q
-
M\widehat R,
}
\]

并有：

\[
\boxed{
\alpha Jh_T^\sharp q
=
H/\beta_3.
}
\]

同时完成 symbolic elimination audit：

AFF 与 T0-Q 属于同一 affine information class。

---

## 95-R6-T3 — T0 Remainder Compression

**NOT ACHIEVED GLOBALLY.**

没有证明：

\[
\widehat R\in\mathcal R_T,\qquad
\#\mathcal R_T=O(1).
\]

没有证明：

\[
|\widehat R|<C
\]

for absolute \(C\)。

---

## 95-R6-T4 — Affine Divisibility / Boundary Gap

**CURRENT ARCHITECTURE KILLED.**

自然 spacing：

\[
\Lambda_{\rm aff}
=
\gcd(
\alpha Jh_T^\sharp q,\,
M\widehat R
)
\]

只给：

\[
\Lambda_{\rm aff}\mid S_3.
\]

没有 independent decimal/source theorem 给：

\[
0<|S_3|<\Lambda_{\rm aff}.
\]

mismatch chambers甚至满足：

\[
|S_3|>\Lambda_{\rm aff}.
\]

---

## 95-R6-T5 — T0 Finite-State / Extinction Theorem

**FAILED TO REACH.**

\[
\boxed{
\mathcal H_{T0}\neq\text{proved empty},
}
\]

且：

\[
\boxed{
\mathcal H_{T0}\neq\text{proved globally finite}.
}
\]

正式 obstruction：

```text
BORROW_STATE_FINITE_BUT_NO_INTEGER_SPACING
REMAINDER_NOT_UNIFORMLY_FINITE
AFFINE_PARAMETER_REMAINS_MOVING
GLOBAL_EXPONENT_TAIL_SURVIVES
NO_AFFINE_TO_SOURCE_BOUNDARY_INTEGER_BRIDGE
SOURCE_REPLAY_REQUIRES_NEW_PRIMITIVE_DATUM
```

---

## 95-R6-T6 — T1 Transfer Verdict

**NOT ACTIVATED.**

T0 proof没有形成“bounded carry alone suffices”的 theorem。

---

# Final Strategic Verdict

R6 对核心问题：

\[
\boxed{
\text{“非零 remainder + finite borrow 是否就是 resonance 中缺失的第二信息类？”}
}
\]

的精确回答是：

\[
\boxed{
\begin{array}{c}
\textbf{作为 affine source datum：YES;}\\[2mm]
\textbf{作为可直接命中 common-}U\textbf{ boundary 的第二 codimension：NO.}
\end{array}
}
\]

transition 的 inhomogeneous correction 不能被当 error；
它确实改变了 sign geometry，并在 sign-mismatch chambers
给出强 Smith absorption。

但 finite borrow只控制：

\[
H/Q_0
\]

落在固定 slab；
它没有把：

\[
\widehat R,\ q,\ M/N,\ U
\]

压成 global finite state。

最关键的缺失不再模糊：

\[
\boxed{
\textbf{缺的是 affine displacement 与 actual numerator boundary headroom
之间的一条独立 source identity。}
}
\]

所以 R6 的终局不是回 resonance，也不是机械扩 T1，而是：

\[
\boxed{
\textbf{Path C — Transition Source-Boundary Invariant Assault.}
}
\]
