# 105-R6 — General Moving-Profile Sphere × Full-Master Rational-Lift Gate

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — `A1-only`  
**Round:** `105-R6`  
**Authorized route:** Route C only  
**Central gate:** `GENERAL MOVING-PROFILE SPHERE × FULL-MASTER RATIONAL-LIFT`  
**Terminal architecture:** **generic square-class obstruction is canonical; the R5C odd-5-adic value is not source-canonical from the present theorem set; the exact exceptional square cover is isolated as the sole R7 target.**

---

# 1. Executive Verdict

R6 获得了一个比 R5C profile-specific discriminant 更高一级、且真正 canonical 的对象。

对任意 fixed moving profile，恢复 primitive sphere 与 full master 后，可写成

\[
Q_0^2-P_1^2=\mathcal N,
\qquad
\mathcal A Q_0-\mathcal B P_1=\mathcal C,
\]

其中

\[
\mathcal N=P_2^2+P_3^2.
\]

定义 essential sphere-master discriminant

\[
\boxed{
\mathscr D
:=
\mathcal C^2+(\mathcal B^2-\mathcal A^2)\mathcal N.
}
\tag{R6-D}
\]

则：

\[
\boxed{
\operatorname{Disc}_{Q_0}=4\mathcal B^2\mathscr D,
\qquad
\operatorname{Disc}_{P_1}=4\mathcal A^2\mathscr D.
}
\tag{R6-Disc}
\]

因此两种消元给出同一个 square class

\[
\boxed{
[\mathscr D]\in \mathbf Q^\times/\mathbf Q^{\times2}.
}
\]

更强地，有恒等式

\[
(\mathcal A Q_0-\mathcal B P_1)^2
+(\mathcal B^2-\mathcal A^2)(Q_0^2-P_1^2)
=(\mathcal BQ_0-\mathcal AP_1)^2.
\]

所以在 sphere + master 上：

\[
\boxed{
\mathscr D=(\mathcal BQ_0-\mathcal AP_1)^2.
}
\tag{COMP}
\]

这给出 R6 的核心 theorem：

> **Sphere–Linear-Master Complementary Discriminant Lemma.**  
> 在 source-legal nondegenerate profile 上，rational sphere×master lift 存在，当且仅当 \(\mathscr D\in\mathbf Q^{\times2}\)。

R5C 的 discriminant 正是该对象的 specialization，而不是独立的新 polynomial phenomenon。

但是 R6 的 canonical-normalization audit 同时证明：

- \(C_2=C_3=1\) 是 `SPECIAL_PROFILE`；
- \(b_1=b_2=1\) 是 `SPECIAL_PROFILE`；
- \(P_3=1\) 是 `SPECIAL_PROFILE`；
- 它们都不是 general moving profile 上可以通过 primitive/projective/Smith gauge 强制的 normalization。

在 general profile 中：

\[
\mathcal C=YC_2+C_3,
\]

而 \(\mathcal A,\mathcal B\) 读取 \(b_1,b_2,b_3\)，\(\mathcal N\) 读取 \(P_2,P_3\)。故 canonical R5C 中固定为 1 的三个 ratio 均真正进入 square class。

因此：

\[
\boxed{
\text{R5C 的 square-class invariant 本身 canonical；}
\quad
\mathfrak I_5=1\text{ 的值并未被证明 source-canonical。}
}
\]

R6 进一步识别 canonical R5C 的 \(5\)-adic mechanism：它不是“十进制自动产生奇 valuation”，而是一个 **tie + first cancellation stratum**。在 R5C 中两个最低 \(5\)-adic 项同阶，并在模 \(5\) 首次抵消，随后只提升一阶，从而得到奇 valuation。

同时，canonical R5C 甚至存在一个独立的 \(2\)-adic backup：对全部 R5C depths，其 essential discriminant 也不是 \(\mathbf Q_2\)-square。

但这同样没有推广到全部 moving profiles。

本轮还构造了一个严格标为 `REDUCED-SHELL LOCAL EVASION` 的 outer profile：

\[
g=2,\ d=-1,\ k=1,\ n_3=4,
\]
\[
b_1=b_2=1,\quad b_3=V=100120,
\]
\[
P_2=100120,\quad P_3=1,\quad C_2=C_3=1,
\]
\[
U=1001.
\]

它通过 outer exponent、denominator digits、2/3 Smith-radial dictionary、common-\(U\)、coprimality，并且其 \(\mathscr D\) 同时为 \(\mathbf Q_2\) 与 \(\mathbf Q_5\) 中的平方类；但 \(\mathscr D\notin\mathbf Q^{\times2}\)，且尚无 \(P_1,Q_0\) rational lift，因此不能标为 full source evasion。它严格说明：**单独把 \(2,5\) 当成 reduced outer profile 上的 universal local cover 已经不成立。**

最终 R6 签发：

```text
DISCRIMINANT_OBSTRUCTION_GENERIC_NOT_UNIVERSAL
CANONICAL_COMPLEMENTARY_DISCRIMINANT_CLASS_EXTRACTED
EXCEPTIONAL_SQUARE_COVER_ISOLATED
```

R7 只授权：

\[
\boxed{
\textbf{Exceptional Square-Locus Source Intersection}
}
\]

其单一对象为

\[
\boxed{
W^2=\mathscr D
}
\]

或等价的 factor-pair incidence：

\[
\boxed{
(W-\mathcal C)(W+\mathcal C)
=(\mathcal B^2-\mathcal A^2)\mathcal N.
}
\tag{FP}
\]

之后才允许检查 integral / primitive / DES / common-\(U\) lift。

---

# 2. Frozen R1–R5C State

以下全部冻结，不重新打开。

```text
R1 = COMMON_OBSTRUCTION_CERTIFIED
COMMON_OBSTRUCTION = SOURCE_AFFINE_SECTION_LOSS
PRE_BRANCH_MASTER_OBJECT = RECOVERED

R2 = SOURCE_SECTION_INTERNALIZATION_THEOREM_PROVED
KAPPA_SRC = CANONICAL
J = DES_SATURATION_DECORATION

R3 = FINITE_SOURCE_COMPLETED_VALUATION_ATLAS_PROVED
PRIMARY_CELLS = S0,S1,S2,S3,S4
VALUATION_ATLAS = SEMANTICALLY_SATURATED

R4 = FIXED_INCIDENCE_EXTRACTED_OFF_EXCEPTIONAL_CELLS
S0_S1_S2 = FIXED
OUTER_Z = X/G = 10^d
PLAIN_ALGEBRAIC_FIXEDNESS_EXTRACTION = RETIRED

R5 = FIXED_BASE_SUPPORTS_AT_MOST_ONE_Z
CURRENT_THREE_LANE_OUTER_FIXEDNESS_ENGINE = FALSIFIED
COMMON_R5_OBSTRUCTION = MOVING_BASE_SOURCE_PHASE_ESCAPE

R5C = FIRST_FULL_SOURCE_FAILURE_GATE_ISOLATED
R5C_GATE = SPHERE_X_MASTER_RATIONAL_LIFT
CANONICAL_MOVING_TRANSFER = KILLED
GLOBAL_OUTER_FIXEDNESS = UNRESOLVED
```

R5C canonical profile：

\[
K=10,\ X=10,\ Y=100G,\ V=10G^2,
\]
\[
b_1=b_2=1,\quad b_3=10G^2,
\]
\[
P_2=10G^2,\quad P_3=1.
\]

full master：

\[
111Q_0-1000P_1=100G+1.
\]

sphere：

\[
P_1^2+100G^4+1=Q_0^2.
\]

R5C discriminant：

\[
\Delta_{R5C}
=
80,000,000
(4,938,395G^4+500G^2+10G+49,384).
\]

其 \(v_5=7\) theorem 冻结。

---

# 3. Canonical R5C Lift Obstruction

把 R5C master 写成

\[
\mathcal A Q_0-\mathcal B P_1=\mathcal C
\]

得到：

\[
\mathcal A=111,
\quad
\mathcal B=1000,
\quad
\mathcal C=100G+1,
\]

以及

\[
\mathcal N=100G^4+1.
\]

故

\[
\begin{aligned}
\mathscr D_{R5C}
&=(100G+1)^2+(1000^2-111^2)(100G^4+1)\\
&=20(4,938,395G^4+500G^2+10G+49,384).
\end{aligned}
\]

而

\[
4\mathcal B^2\mathscr D_{R5C}
=
80,000,000(\cdots),
\]

精确恢复 R5C discriminant。

所以：

\[
\boxed{
[\Delta_{R5C}]=[\mathscr D_{R5C}].
}
\]

R5C \(\mathfrak I_5\) 精确等价于：

\[
\boxed{
v_5(\mathscr D_{R5C})\equiv1\pmod2.
}
\]

注意 raw discriminant 中的额外 \(4\mathcal B^2\) 是平方，不应进入 canonical invariant。

---

# 4. General Moving-Profile Parameter Recovery

R6 不重新引入全部历史变量，而采用最小 rational-lift base profile：

\[
\boxed{
\mathbf s=
(g,k,d,n_3;
G,K,X,Y;
V;
b_1,b_2,b_3;
g_1,g_2,g_3;
C_2,C_3;
P_2,P_3;
U;\mathrm{DES/Smith\ metadata}).
}
\]

其中：

\[
G=10^g,\qquad K=10^k,
\]
\[
X=10^{m_2}=10^{g+d},
\qquad
Y=10^{n_3},
\]
\[
n_2=2g+k+d,
\qquad
m_3=n_3+g.
\]

primitive/common denominator dictionary：

\[
g_i=\gcd(V,P_i),
\quad
C_i=P_i/g_i,
\quad
b_i=V/g_i.
\]

故

\[
g_i=V/b_i
\]

在 fixed denominator profile 上恢复。

第二、三 primitive coordinates：

\[
P_2=g_2C_2,
\qquad
P_3=g_3C_3.
\]

source radial selector：

\[
a_i=UC_i,
\qquad
\gcd(U,V)=1,
\]

并保留 exact digit windows。

\(P_1,Q_0\) **不属于 base profile 自由参数**；它们是当前 gate 要恢复的 lift coordinates。

---

# 5. General Profile Parameter Ledger

| parameter | source-native? | gauge? | primitive? | Smith-derived? | outer-dependent? | can normalize? | must retain? |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(g,k,d,n_3\) | YES | NO | NO | NO | YES | NO | YES |
| \(G,K,X,Y\) | DERIVED SOURCE | NO | NO | NO | YES | only notation | YES |
| \(V\) | YES / intrinsic LCM | NO | YES interface | YES | YES | NO | YES |
| \(U\) | YES radial | NO | NO | NO | YES | NO | legality metadata |
| \(b_1,b_2,b_3\) | YES | NO | via gcd profile | YES | YES | NO | YES |
| \(g_i=V/b_i\) | DERIVED | NO | YES | YES | YES | NO | YES |
| \(C_2,C_3\) | YES source carriers | NO | YES | YES radial cancellation | YES | NO | YES |
| \(P_2,P_3\) | DERIVED primitive | NO | YES | YES | YES | NO | YES |
| \(P_1,Q_0\) | lift variables | NO | YES after lift | partially | YES | NO | SOLVE |
| \(J\) | derived decoration | NO | NO | YES | YES | no | legality only |
| master-row common scalar | NO | **YES** | NO | NO | NO | YES | quotient out |

关键：真正允许 quotient 的只有 master equation 的非零 scalar multiple。primitive sphere tuple 已经 primitive-normalized，不能再整体 rescale。

---

# 6. Gauge vs Genuine Freedom Audit

## 6.1 Master-row gauge

若

\[
(\mathcal A,\mathcal B,\mathcal C)
\mapsto
\lambda(\mathcal A,\mathcal B,\mathcal C),
\qquad \lambda\in\mathbf Q^\times,
\]

则

\[
\mathscr D\mapsto\lambda^2\mathscr D.
\]

所以

\[
[\mathscr D]
\]

完全不变。

## 6.2 Primitive tuple scaling

在 ambient rational sphere 中存在 scaling，但 source problem 已固定

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

故非平凡 overall scaling 不是 source gauge。

## 6.3 Source radial scale

\(U\) 不进入 \(\mathscr D\)，说明 square-class gate 位于 common-\(U\) 之前；但这不意味着可以把 \(U\) 任意 normalization，因为其 digit windows / coprimality 仍是后续 source legality。

---

# 7. Canonical-Normalization Audit

## 7.1 \(C_2=C_3=1\)

```text
NORMALIZATION = SPECIAL_PROFILE
```

理由：\(C_i\) 是 primitive source carrier；primitive gcd 只杀整体公共 content，不允许把两个独立 positive carriers 同时强制为 1。

## 7.2 \(b_1=b_2=1\)

```text
NORMALIZATION = SPECIAL_PROFILE
```

理由：\(b_i=V/g_i\) 是真实 denominator blocks / gcd-profile data。其 ratio 不能由 Smith unimodular change 或 projective scaling抹去。

## 7.3 \(P_3=1\)

```text
NORMALIZATION = SPECIAL_PROFILE
```

理由：primitive normalization 只保证四元组无公共因子；并不保证某一个 coordinate 为 1。

## 7.4 \(V\)-division of the master row

```text
NORMALIZATION = SOURCE_CANONICAL ROW NORMALIZATION
```

因为 \(V=\operatorname{lcm}(b_1,b_2,b_3)\) 是 intrinsic，并且 raw master 的三个系数均含相应 \(V\)-presentation；除以 \(V\) 只改变 row scalar，不改变 square class。

---

# 8. General Primitive Sphere

恢复：

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2.
}
\]

令

\[
\boxed{
\mathcal N=P_2^2+P_3^2>0.
}
\]

则：

\[
\boxed{
Q_0^2-P_1^2=\mathcal N.
}
\]

等价：

\[
\boxed{
(Q_0-P_1)(Q_0+P_1)=\mathcal N.
}
\]

这是 general rational-lift gate 最小 sphere form。

---

# 9. General Full Master

R3 frozen pre-\(J\) master：

\[
 b_1XYG(KP_1-Q_0)
+b_2Y(P_2-GQ_0)
-b_3(Q_0-P_3)=0.
\tag{Mraw}
\]

整理：

\[
\boxed{
A_0Q_0-B_0P_1=C_0,
}
\]

其中 raw integer coefficients：

\[
\boxed{
A_0=YG(b_1X+b_2)+b_3,
}
\]

\[
\boxed{
B_0=b_1XYGK,
}
\]

\[
\boxed{
C_0=b_2YP_2+b_3P_3.
}
\]

利用 \(b_i=V/g_i\) 除以 intrinsic \(V\)，得到 normalized row：

\[
\boxed{
\mathcal A Q_0-\mathcal B P_1=\mathcal C,
}
\]

\[
\boxed{
\mathcal A
=
\frac{XYG}{g_1}+\frac{YG}{g_2}+\frac1{g_3},
}
\]

\[
\boxed{
\mathcal B
=
\frac{XYGK}{g_1},
}
\]

以及最重要的 source simplification：

\[
\boxed{
\mathcal C
=
\frac{YP_2}{g_2}+\frac{P_3}{g_3}
=
YC_2+C_3.
}
\tag{Csrc}
\]

这就是 general source-native linear master。

---

# 10. Nondegeneracy: \(\mathcal A\neq\mathcal B\) is Source-Forced

若 \(A_0=B_0\)，则

\[
b_3
=YG\bigl[b_1X(K-1)-b_2\bigr].
\]

方括号是整数。

- 若 \(\le0\)，则 \(b_3\le0\)，不合法；
- 若 \(\ge1\)，则
  \[
  b_3\ge YG=10^{m_3},
  \]
  与 \(b_3\) 为 \(m_3\)-digit denominator block 的
  \[
  b_3<10^{m_3}=YG
  \]
  矛盾。

所以：

\[
\boxed{
A_0\neq B_0,
\qquad
\mathcal A\neq\mathcal B.
}
\]

由于二者正，也不可能 \(\mathcal A=-\mathcal B\)。

因此所有 source-legal profile 的 sphere×master fibre 均为真正 degree-2 fibre；不存在 degenerate linear escape stratum。

---

# 11. Sphere–Linear-Master Discriminant Lemma

设

\[
Q^2-P^2=N,
\qquad
AQ-BP=C,
\qquad
A^2\neq B^2.
\]

消去 \(P\)：

\[
(B^2-A^2)Q^2+2ACQ-(C^2+B^2N)=0.
\]

判别式：

\[
\boxed{
\Delta_Q=4B^2\bigl(C^2+(B^2-A^2)N\bigr).
}
\]

消去 \(Q\)：

\[
(B^2-A^2)P^2+2BCP+(C^2-A^2N)=0,
\]

判别式：

\[
\boxed{
\Delta_P=4A^2\bigl(C^2+(B^2-A^2)N\bigr).
}
\]

故定义：

\[
\boxed{
D_{\rm ess}=C^2+(B^2-A^2)N.
}
\]

两种消元 square class 一致。

---

# 12. General Discriminant

R6 general essential discriminant：

\[
\boxed{
\mathscr D
=(YC_2+C_3)^2
+
(\mathcal B^2-\mathcal A^2)(P_2^2+P_3^2).
}
\tag{GEN-D}
\]

raw integer version：

\[
\boxed{
\mathscr D_0
=C_0^2+(B_0^2-A_0^2)(P_2^2+P_3^2).
}
\]

因为

\[
(A_0,B_0,C_0)=V(\mathcal A,\mathcal B,\mathcal C),
\]

所以：

\[
\boxed{
\mathscr D_0=V^2\mathscr D.
}
\]

因此

\[
[\mathscr D_0]=[\mathscr D].
\]

raw integer form最适合 integral/source divisibility，normalized form最适合 local square-class audit。

---

# 13. Square-Class Reduction

所有明显平方因子全部退休：

- \(4\)；
- \(A^2\) 或 \(B^2\) 的 elimination prefactor；
- master-row common scalar squared；
- raw/normalized conversion中的 \(V^2\)。

真正 invariant：

\[
\boxed{
\mathfrak S_p(\mathbf s)
:=[\mathscr D]_{\mathbf Q_p}
\in\mathbf Q_p^\times/\mathbf Q_p^{\times2}.
}
\]

全局：

\[
\boxed{
\mathfrak S(\mathbf s)
:=[\mathscr D]
\in\mathbf Q^\times/\mathbf Q^{\times2}.
}
\]

R5C \(\mathfrak I_5\) 只是

\[
v_5(\mathscr D)\bmod2
\]

在一个 special profile 上的粗 projection。

---

# 14. (5)-Adic Valuation Audit

令：

\[
a=v_5(\mathcal A),
\quad
b=v_5(\mathcal B),
\quad
c=v_5(\mathcal C),
\quad
n=v_5(\mathcal N),
\]

以及

\[
\delta=v_5(\mathcal B^2-\mathcal A^2).
\]

则：

\[
\boxed{
\mathscr D=\mathcal C^2+(\mathcal B^2-\mathcal A^2)\mathcal N.
}
\]

令

\[
e_1=2c,
\qquad
e_2=\delta+n.
\]

精确 valuation rule：

1. 若 \(e_1<e_2\)：
   \[
   v_5(\mathscr D)=2c,
   \]
   为偶数；更强地，\(\mathscr D/\mathcal C^2\in1+5\mathbf Z_5\)，因此 \(\mathscr D\) 自动是 \(\mathbf Q_5\)-square。

2. 若 \(e_1>e_2\)：
   \[
   v_5(\mathscr D)=\delta+n,
   \]
   square class 由第二项决定。

3. 若 \(e_1=e_2\)：发生 cancellation stratum，必须读取 leading units；valuation 可提高任意有限阶，其 parity 不再由 decimal power alone决定。

特别地：

\[
\boxed{
2v_5(\mathcal C)
<
v_5((\mathcal B^2-\mathcal A^2)\mathcal N)
\Longrightarrow
\mathscr D\in\mathbf Q_5^{\times2}.
}
\tag{5-EVADE}
\]

这给出一个明确的 \(5\)-adic evasion mechanism。若要证明 universal \(5\)-adic obstruction，就必须证明 source legality 永远禁止该 stratum，并同时杀掉 tie/second-term square strata。R1–R5C 没有这样的 theorem。

---

# 15. (5)-Adic Unit Audit

\(\mathbf Q_5\) square criterion：写

\[
\mathscr D=5^e u,
\qquad u\in\mathbf Z_5^\times.
\]

则

\[
\mathscr D\in\mathbf Q_5^{\times2}
\iff
\begin{cases}
e\equiv0\pmod2,\\
u\bmod5\in\{1,4\}.
\end{cases}
\]

所以 R6 的 finite local target atlas只有四个 classes：

```text
valuation parity 0/1 × unit Legendre class square/nonsquare
```

canonical R5C：

\[
\mathcal A=111\equiv1,
\quad
\mathcal B\equiv0,
\quad
\mathcal C\equiv1,
\quad
\mathcal N\equiv1
\pmod5.
\]

故最低阶：

\[
\mathcal C^2-\mathcal A^2\mathcal N\equiv0\pmod5.
\]

这是 **tie cancellation**，不是 generic dominant-term regime。

精确展开给：

\[
v_5(\mathscr D_{R5C})=1.
\]

所以 R5C 是一个 first-cancellation odd stratum。

---

# 16. (2)-Adic Backup

对 \(\mathbf Q_2\)：写

\[
\mathscr D=2^eu,
\qquad u\text{ odd}.
\]

则

\[
\mathscr D\in\mathbf Q_2^{\times2}
\iff
\begin{cases}
e\equiv0\pmod2,\\
u\equiv1\pmod8.
\end{cases}
\]

## Canonical R5C

\[
\mathscr D_{R5C}=20R(G),
\]

\[
R(G)=4,938,395G^4+500G^2+10G+49,384.
\]

R5C depth有 \(G=10^g,\ g\ge2\)。

### \(g\ge3\)

\[
R(G)\equiv8\pmod{16},
\]

故

\[
v_2(R)=3,
\qquad
v_2(\mathscr D)=5,
\]

奇 valuation，非 square。

### \(g=2\)

直接模 \(128\)：

\[
R(100)\equiv16\pmod{128},
\]

所以

\[
v_2(\mathscr D)=6,
\]

但 odd unit：

\[
\mathscr D/2^6\equiv5\pmod8,
\]

仍非 square。

因此：

\[
\boxed{
\text{R5C canonical profile 在 }\mathbf Q_2\text{ 与 }\mathbf Q_5\text{ 双重失败。}
}
\]

签：

```text
CANONICAL_TWO_PRIME_REDUNDANT_OBSTRUCTION = PROVED
```

但 general \(2\)-adic universality未证明。

---

# 17. Canonicality of \(\mathfrak I_5\)

必须区分“对象 canonical”与“值 universal”。

## 对象

\[
[\mathscr D]_{\mathbf Q_5}
\]

是 canonical：

- master row scaling只乘平方；
- raw/normalized切换乘 \(V^2\)；
- 消 \(P_1\) / 消 \(Q_0\) 只差 \(A^2/B^2\) 平方；
- complementary linear form给 intrinsic quadratic fibre discriminant。

## 值

R5C 的

\[
\mathfrak I_5=1
\]

不是由现有 source axioms自动推出。

其原因不是 heuristic，而是 general formula明确读取三个被 R5C special-fixed 的 genuine degrees：

\[
(C_2:C_3),
\qquad
(b_1:b_2),
\qquad
(P_2:P_3).
\]

故：

```text
I5_CANONICAL_OBJECT = YES
I5_VALUE_ONE_SOURCE_CANONICAL = NO_PROOF / NOT FORCED BY CURRENT NORMALIZATION
```

---

# 18. Alternative-Elimination Consistency

消 \(P_1\)：

\[
\Delta_Q=4\mathcal B^2\mathscr D.
\]

消 \(Q_0\)：

\[
\Delta_P=4\mathcal A^2\mathscr D.
\]

所以：

\[
\boxed{
[\Delta_Q]=[\Delta_P]=[\mathscr D].
}
\]

因此 R6 invariant不依赖 elimination direction。

---

# 19. Conic / Quadratic-Étale / Hilbert Interpretation

完整 sphere + master 在所有 coordinates 上可被看作 moving quadric section。

但 R6 固定 base profile \((P_2,P_3,\ldots)\) 后，剩余 \((P_1,Q_0)\) fibre 不是一个需要复杂 Hasse–Minkowski 的 projective conic，而是一个 degree-2 quadratic fibre。

其 coordinate algebra为：

\[
\boxed{
\mathbf Q[\sqrt{\mathscr D}].
}
\]

- 若 \([\mathscr D]=1\)，fibre split，两个 rational points；
- 若非 square，fibre 是 non-split quadratic étale algebra，无 rational point。

R5C odd \(v_5\) 正是该 étale fibre 在 \(\mathbf Q_5\) 不 split 的坐标表达。

所以本轮不需要重新启动历史 Brauer/Gaussian architecture；最 intrinsic 的对象已经是 quadratic discriminant class。

---

# 20. Mod-5 Source Residue Atlas

source coefficients：

\[
\mathcal C=YC_2+C_3.
\]

只要 \(n_3\ge1\)：

\[
\boxed{
\mathcal C\equiv C_3\pmod5
}
\]

在 \(C_3\) 为 \(5\)-unit 时尤为显著。

另一方面 \(\mathcal A,\mathcal B\) 的 residue取决于：

- \(g_1,g_2,g_3\) 的 \(5\)-adic depth；
- 等价地 \(b_1,b_2,b_3\) 在 common \(V\) 中的 allocation。

\(\mathcal N=P_2^2+P_3^2\) 则读取 primitive mod-5 orbit。

因此 source mod-5 map的最小数据不是单一 \(G\)，而是：

\[
\boxed{
(v_5\mathcal A,v_5\mathcal B,v_5\mathcal C,v_5\mathcal N;
\bar A,\bar B,\bar C,\bar N)
}
\]

再 quotient 到四个 \(\mathbf Q_5\) square classes。

这给出 finite **target** atlas，但不是 finite raw valuation atlas；valuation depths本身仍可增长。

---

# 21. Primitive Mod-5 Orbit Audit

primitive sphere mod 5：

\[
P_1^2+P_2^2+P_3^2=Q_0^2.
\]

\(-1\) 在 \(\mathbf F_5\) 中是平方，因此 primitive quadric有多个 projective residue orbit。

R5C canonical orbit具有：

\[
P_1\equiv P_2\equiv0\pmod5,
\qquad
P_3,Q_0\in\mathbf F_5^\times.
\]

没有 frozen source theorem 强迫所有 outer moving profile均落入这个 orbit。

因此：

```text
PRIMITIVE_MOD5_ORBIT = MULTIPLE
R5C_ORBIT = SPECIAL
ORBIT_INDEPENDENCE_OF_I5_VALUE = FALSE / NOT AVAILABLE
```

---

# 22. Finite Local Obstruction Cover

## 22.1 Canonical family

\[
\{2,5\}
\]

两者都杀 R5C canonical family。

## 22.2 General moving profiles

R6 未证明存在 fixed finite prime set \(\mathcal P_{fin}\) 杀全部 source profiles。

原因：\(\mathscr D\) 的 square-free kernel可含随 moving profile移动的 odd primes；generic quadratic fibre没有理由只在 base primes \(2,5\) 上失败。

更强地，下面的 reduced-shell profile同时通过 \(\mathbf Q_2\) 与 \(\mathbf Q_5\) local-square test，所以 \(\{2,5\}\) 不能作为 reduced outer profile space 上的 universal cover。

因此：

```text
FINITE_LOCAL_OBSTRUCTION_SET = {2,5} FOR R5C CANONICAL ONLY
FINITE_LOCAL_COVER_PROVED = NO
```

---

# 23. Square-Locus Construction

定义 extended square cover：

\[
\boxed{
\widetilde{\mathcal E}_{sq}
=
\{(\mathbf s,W):W^2=\mathscr D(\mathbf s)\}.
}
\]

对 nondegenerate \(\mathcal B^2-\mathcal A^2\neq0\)，在 coefficient function field中：

\[
\mathscr D=\mathcal C^2+T,
\qquad
T=(\mathcal B^2-\mathcal A^2)\mathcal N\neq0.
\]

把 \(\mathcal C\) 当作 indeterminate：若 \(\mathcal C^2+T\) 是 rational-function square，则 degree 2 square只能形如 \((\pm\mathcal C+r)^2\)；无 linear term迫使 \(r=0\)，再迫使 \(T=0\)，矛盾。

所以 generic function-field class nontrivial：

\[
\boxed{
\mathscr D\notin\mathbf Q(\mathbf s)^{\times2}
\quad\text{generically}.
}
\]

注意：base rational points上“\(\mathscr D\) 恰为平方”的集合一般不是一个 Zariski-closed 子集；正确对象是这个 nontrivial quadratic cover及其 rational sections/specializations。

---

# 24. Factor-Pair Form of the Exceptional Locus

\[
W^2-\mathcal C^2
=(\mathcal B^2-\mathcal A^2)\mathcal N.
\]

所以：

\[
\boxed{
(W-\mathcal C)(W+\mathcal C)
=(\mathcal B^2-\mathcal A^2)\mathcal N.
}
\]

令

\[
R_-=W-\mathcal C,
\qquad
R_+=W+\mathcal C.
\]

则：

\[
\boxed{
R_-R_+=(\mathcal B^2-\mathcal A^2)\mathcal N,
}
\]

\[
\boxed{
R_+-R_-=2(YC_2+C_3).
}
\]

这把 exceptional square specialization 转成 exact factor-pair × source additive gap incidence。

对 integral lift最好使用 raw integer coefficients：

\[
(W_0-C_0)(W_0+C_0)
=(B_0^2-A_0^2)\mathcal N.
\]

这就是 R7 的最小 arithmetic object。

---

# 25. Evasion Search

R6 按“放开一个自由度”审计后得到：

| freed degree | enters discriminant through | can change \(v_5\)? | can change unit class? | full source evasion found? |
|---|---|---:|---:|---:|
| \(C_2/C_3\) | \(\mathcal C=YC_2+C_3\), also \(\mathcal N\) | YES structurally | YES | NO |
| \(b_1/b_2\) | \(\mathcal A,\mathcal B\) | YES | YES | NO |
| \(P_2/P_3\) | \(\mathcal N\) | YES | YES | NO |

因此 R5C 的 odd-5 class没有 normalization invariance可依赖。

## Reduced-shell two-prime local evasion

取：

\[
g=2,\quad d=-1,\quad k=1,
\]
\[
G=100,\quad X=10,\quad Y=10000,
\]
\[
n_2=n_3=4,\quad m_3=6,
\]
\[
V=b_3=100120,
\quad b_1=b_2=1,
\]
\[
P_2=100120,\quad P_3=1,
\quad C_2=C_3=1,
\]
\[
U=1001,
\qquad
\gcd(U,V)=1.
\]

Smith data可取

\[
s=\alpha=\beta=t=u=u_0=1,
\quad v=100120,
\quad M=N=1.
\]

所以 2/3 Smith-radial dictionary exact：

\[
P_2=vM,
\qquad
P_3=N.
\]

raw master coefficients：

\[
A_0=11,100,120,
\]
\[
B_0=100,000,000,
\]
\[
C_0=1,001,300,120,
\]

\[
\mathcal N=10,024,014,401.
\]

得到

\[
\mathscr D_0
=99,005,059,494,136,010,240,640,000.
\]

factorization：

\[
\boxed{
\mathscr D_0
=2^{10}3^2 5^4\cdot163\cdot76801\cdot1373031264403.
}
\]

所以：

\[
\mathscr D_0\in\mathbf Q_2^{\times2},
\qquad
\mathscr D_0\in\mathbf Q_5^{\times2},
\]

但

\[
\mathscr D_0\notin\mathbf Q^{\times2}.
\]

这只是：

```text
EVASION_LEVEL = REDUCED_OUTER_SMITH_SOURCE_SHELL_LOCAL_EVASION
SOURCE_LEGAL = PARTIAL / PRE-LIFT
PRIMITIVE_LEGAL = NOT_REACHED
DES_LEGAL = NOT_REACHED
OUTER_LEGAL = YES
DIGIT_LEGAL_2_3 = YES
Q2_LOCAL = PASS
Q5_LOCAL = PASS
GLOBAL_SQUARE = NO
```

它不是 R6 Outcome C 的 full witness，但足以杀掉“\(2,5\) 必有一个失败”的 reduced-shell conjecture。

---

# 26. Minimal Evasion Degree

从 canonical R5C：

\[
V=100000
\]

移动到同一 exponent / carrier / Smith shape 的

\[
V=100120
\]

已经使 \(2\)-adic 与 \(5\)-adic 两个 local obstructions同时消失。

因此 local square class 对 moving denominator base \(V\) 极敏感。

但由于 global square仍失败，这个 degree只证明：

\[
\boxed{
\textbf{Minimal local evasion degree can live entirely in moving denominator/base data.}
}
\]

不能据此声称 rational lift evasion。

---

# 27. Rational Lift Reconstruction

若

\[
W^2=\mathscr D,
\]

则由于 \(\mathcal B^2-\mathcal A^2\neq0\)：

\[
\boxed{
Q_0
=
\frac{-\mathcal A\mathcal C\pm\mathcal BW}
{\mathcal B^2-\mathcal A^2},
}
\tag{Lift-Q}
\]

\[
\boxed{
P_1
=
\frac{-\mathcal B\mathcal C\pm\mathcal AW}
{\mathcal B^2-\mathcal A^2}.
}
\tag{Lift-P}
\]

同号选择对应同一个 quadratic root。

所以：

\[
\boxed{
\mathscr D\in\mathbf Q^{\times2}
\iff
(P_1,Q_0)\in\mathbf Q^2
\text{ sphere×master lift exists}.
}
\]

这是 exact iff，不只是必要条件。

R6 没有找到 source-compatible global-square profile，因此没有可进一步恢复的 full rational witness。

---

# 28. Integral / Primitive Lift Audit

rational lift之后还必须依次检查：

1. \(P_1,Q_0\in\mathbf Z_{>0}\)；
2. \(g_1=\gcd(V,P_1)=V/b_1\)；
3. \(C_1=P_1/g_1\in\mathbf Z_{>0}\)；
4. \(\gcd(C_1,b_1)=1\)；
5. \(\gcd(P_1,P_2,P_3,Q_0)=1\)；
6. leading condition \(KP_1-Q_0>0\)；
7. first numerator block \(UC_1\) exact digit window；
8. full DES rows / tail integrality；
9. full source replay。

因此 gate hierarchy必须保持：

```text
LOCAL SQUARE
< GLOBAL RATIONAL SQUARE
< RATIONAL P1,Q0
< INTEGER P1,Q0
< PRIMITIVE/GCD PROFILE
< DES
< FULL SOURCE
```

R6 未越过 global rational square。

---

# 29. DES / Source Completion Audit

由于 R6 没有 global rational evasion witness，DES 不得被伪造。

当前最准确状态：

```text
RATIONAL_LIFT = NO SOURCE WITNESS FOUND
INTEGRAL_LIFT = NOT_REACHED
PRIMITIVE_LIFT = NOT_REACHED
DES_LIFT = NOT_REACHED
FULL_SOURCE_LIFT = NOT_REACHED
```

必须强调：R5C 的 “first failure” 仍然是真实 first failure **for its canonical family**；R6 只是证明该 failure 的 local square-class value不能直接当作全部 moving profiles的 theorem。

---

# 30. Unbounded-Evasion Audit

没有得到：

\[
|d|\to\infty
\]

的 rational square family，更没有 full source family。

当前只知道：

- generic coefficient space上 square cover nontrivial；
- reduced outer source shell可以规避 \(2,5\) 两个指定 local tests；
- global square-specialization与 full source intersection仍未知。

因此：

```text
LOCAL_EVASION = YES (reduced-shell, 2&5)
GLOBAL_RATIONAL_EVASION = NO
UNBOUNDED_EVASION_FAMILY = NO
```

---

# 31. Failed Generalizations

R6 正式退休以下 conjectures：

1. `R5C_I5_VALUE_ONE_IS_AUTOMATIC_FROM_DECIMAL_BASE` — FAILED AS A DERIVATION.
2. `C2=C3=1_IS_GENERAL_GAUGE` — FALSE.
3. `b1=b2=1_IS_GENERAL_GAUGE` — FALSE.
4. `P3=1_IS_PRIMITIVE_CANONICAL_NORMALIZATION` — FALSE.
5. `{2,5}_IS_ALREADY_A_UNIVERSAL_REDUCED_OUTER_LOCAL_COVER` — FALSE, explicit reduced-shell local evasion.
6. `GENERAL_DISCRIMINANT_REQUIRES_HUGE_PROFILE_POLYNOMIAL` — RETIRED; replaced by \(\mathscr D\).
7. `ELIMINATION_DIRECTION_MAY_CHANGE_INVARIANT` — FALSE; exact square-class equality.
8. `R5C_ODD_V5_IS_A_BRAUER_PHENOMENON_REQUIRING_OLD_GAUSSIAN_ARCHITECTURE` — UNNECESSARY; quadratic étale discriminant already intrinsic.

---

# 32. Exact Remaining Unknowns

R6 将所有剩余不确定性压成一个 formal source-intersection problem：

\[
\boxed{
\exists\ \mathbf s\in\mathcal M_{mov}^{src},\ W\in\mathbf Q
:
W^2=\mathscr D(\mathbf s)?
}
\tag{SRC-SQ}
\]

其中 \(\mathcal M_{mov}^{src}\) 必须保留：

- outer exponent legality；
- full Smith/gcd profile；
- source digit windows / common-\(U\)；
- all pre-lift DES data genuinely defined；
- rational reconstruction后再施加 \(P_1,Q_0\)-dependent primitive/DES rows。

等价 factor form：

\[
\boxed{
R_-R_+=(\mathcal B^2-\mathcal A^2)\mathcal N,
\qquad
R_+-R_-=2(YC_2+C_3).
}
\tag{SRC-FP}
\]

**这一个 incidence 就是 R7 的唯一对象。**

---

# 33. Square-Class Shock Checkpoint

### Q1 — general sphere + master 是否 canonical minimal？

**YES.**

\[
Q_0^2-P_1^2=\mathcal N,
\quad
\mathcal AQ_0-\mathcal BP_1=\mathcal C.
\]

### Q2 — general square class 是否提取？

**YES.**

\[
[\mathscr D],
\quad
\mathscr D=\mathcal C^2+(\mathcal B^2-\mathcal A^2)\mathcal N.
\]

### Q3 — R5C 是否 exact specialization？

**YES.**

### Q4 — \(C_2/C_3\) 是否影响？

**YES, genuinely enters \(\mathcal C\) and \(\mathcal N\).**

### Q5 — \(b_1/b_2\) 是否影响？

**YES, genuinely enters \(\mathcal A,\mathcal B\).**

### Q6 — \(P_2/P_3\) 是否影响？

**YES, through \(\mathcal N\) and the gcd/source carriers.**

### Q7 — \(p=5\) 是否 universal obstruction？

**NO THEOREM.** Canonical value-one does not survive normalization audit; explicit reduced outer shell can be \(\mathbf Q_5\)-square.

### Q8 — \(p=2\) 是否补上？

**CANONICAL R5C: YES. GENERAL: NO.**

### Q9 — finite local cover？

**NO.** \(\{2,5\}\) already fails on the reduced outer shell.

### Q10 — source-legal local evasion？

**Only at reduced/pre-lift source-shell level; not a full source profile.**

### Q11 — true rational lift？

**NO source-compatible witness found.**

Checkpoint decision：

\[
\boxed{
\textbf{EVASION / EXCEPTIONAL-LOCUS ROUTE}
}
\]

但不是签发 explicit full rational evasion；而是签发用户允许的 structural Outcome：

```text
DISCRIMINANT_OBSTRUCTION_GENERIC_NOT_UNIVERSAL
```

---

# 34. R6 Terminal Verdict

R6 最大化完成了“generalization-or-evasion”中的 invariant 抽象部分，但 universal local obstruction没有成立。

最重要的新 canonical theorem 是：

\[
\boxed{
\textbf{Sphere×Master rational lift}
\iff
\mathscr D\in\mathbf Q^{\times2}.
}
\]

最重要的新 architecture correction 是：

\[
\boxed{
\mathfrak I_5\text{ 的对象可推广，值 }1\text{ 不能直接推广。}
}
\]

最重要的新 evasion geometry 是：

\[
\boxed{
(W-\mathcal C)(W+\mathcal C)
=(\mathcal B^2-\mathcal A^2)\mathcal N.
}
\]

因此 R7 不再研究“general discriminant formula”，而只研究这个 exceptional square cover 与 exact source selector 的交。

---

# 35. R7 Single Attack Target

授权：

```text
R7_ARCHITECTURE = Exceptional Square-Locus Source Intersection
```

唯一 target：

\[
\boxed{
\widetilde{\mathcal E}_{sq}(\mathbf Q)
\cap
\mathcal M_{mov}^{src}
}
\]

推荐优先用 raw factor form：

\[
(W_0-C_0)(W_0+C_0)
=(B_0^2-A_0^2)(P_2^2+P_3^2),
\]

同时：

\[
(W_0+C_0)-(W_0-C_0)=2C_0.
\]

R7 应回答：

1. source divisor/gcd/Smith structure能否禁止这样的 factor pair；
2. 若不能，构造第一个 global square source profile；
3. 若 global square出现，立即按 `Lift-Q/Lift-P` 恢复 \(P_1,Q_0\)，再做 integral/primitive/DES/common-\(U\) audit。

禁止重新返回 broad moving-base phase。

---

# 36. Machine-Readable Terminal Block

```text
R6_TERMINAL_VERDICT=DISCRIMINANT_OBSTRUCTION_GENERIC_NOT_UNIVERSAL__CANONICAL_COMPLEMENTARY_DISCRIMINANT_EXTRACTED__EXCEPTIONAL_SQUARE_COVER_ISOLATED

R1_R2_R3_R4_R5_R5C_STATE_FROZEN=YES

R5C_CANONICAL_PROFILE=K10_X10_Y100G_V10G2__b1b2_1__b3_10G2__P2_10G2__P3_1
R5C_DISCRIMINANT=80000000*(4938395*G^4+500*G^2+10*G+49384)
R5C_I5=1

GENERAL_MOVING_PROFILE_PARAMETERS=(g,k,d,n3;G,K,X,Y;V;b1,b2,b3;g1,g2,g3;C2,C3;P2,P3;U;Smith_DES_metadata)
GAUGE_PARAMETERS=MASTER_ROW_NONZERO_SCALAR_ONLY
GENUINE_SOURCE_PARAMETERS=(g,k,d,n3,V,b1,b2,b3,C2,C3,U_AND_DERIVED_P2_P3)

C2_C3_NORMALIZATION_STATUS=SPECIAL_PROFILE
B1_B2_NORMALIZATION_STATUS=SPECIAL_PROFILE
P2_P3_NORMALIZATION_STATUS=P3_EQ_1_IS_SPECIAL_PROFILE__P2_P3_RATIO_GENUINE

GENERAL_SPHERE_FORM=Q0^2-P1^2=N__N=P2^2+P3^2
GENERAL_MASTER_FORM=A*Q0-B*P1=C__C=Y*C2+C3
GENERAL_ELIMINATION_FORM=(B^2-A^2)Q0^2+2ACQ0-(C^2+B^2N)=0
GENERAL_DISCRIMINANT=4*B^2*D_ESS__D_ESS=C^2+(B^2-A^2)*N
GENERAL_SQUARE_CLASS=[D_ESS]

I5_GENERALIZATION=YES_AS_LOCAL_SQUARE_CLASS_OBJECT__NO_AS_UNIVERSAL_VALUE_ONE
I5_CANONICAL=YES_FOR_[D_ESS]_Q5
I5_CHART_INDEPENDENT=YES

V5_DISCRIMINANT_FORMULA=v5(C^2+(B^2-A^2)N)__DOMINANCE_TIE_RULE_PROVED
V5_PARITY_UNIVERSAL=NO_PROOF__CANONICAL_ODD_VALUE_NOT_SOURCE_FORCED
Q5_UNIT_CLASS=FULL_PARITY_PLUS_UNIT_RESIDUE_REQUIRED
Q5_SQUARE_CLASS_UNIVERSAL=NO

Q2_SQUARE_CLASS=R5C_CANONICAL_NON_SQUARE_FOR_ALL_DEPTHS
TWO_ADIC_BACKUP=YES_CANONICAL__NO_GENERAL

FINITE_LOCAL_OBSTRUCTION_SET={2,5}_CANONICAL_ONLY
FINITE_LOCAL_COVER_PROVED=NO

SQUARE_LOCUS=W^2=D_ESS_EQUIV_(W-C)(W+C)=(B^2-A^2)N
SQUARE_LOCUS_PROPER=YES_AS_NONTRIVIAL_QUADRATIC_COVER__NOT_A_ZARISKI_CLOSED_BASE_SQUARE_SET
SQUARE_LOCUS_SOURCE_INTERSECTION=OPEN_SINGLE_FORMAL_CONDITION

EVADING_PROFILE_FOUND=YES_REDUCED_SHELL_LOCAL_ONLY__V=100120_G=100_d=-1
EVADING_PROFILE_SOURCE_LEGAL=PARTIAL_PRE_LIFT_ONLY
EVADING_PROFILE_OUTER_DEPTH=d=-1
EVADING_PROFILE_DISCRIMINANT_SQUARE=Q2_YES_Q5_YES_GLOBAL_NO

RATIONAL_SPHERE_MASTER_LIFT=NO_SOURCE_WITNESS
INTEGRAL_SPHERE_MASTER_LIFT=NOT_REACHED
PRIMITIVE_SPHERE_MASTER_LIFT=NOT_REACHED
DES_COMPATIBLE=NOT_REACHED
FULL_SOURCE_COMPATIBLE=NOT_REACHED

UNBOUNDED_EVASION_FAMILY=NO

GENERAL_OUTER_RATIONAL_LIFT_STATUS=UNRESOLVED_ONLY_ON_EXCEPTIONAL_SQUARE_COVER
S3_STATUS=OPEN_ON_EXCEPTIONAL_SQUARE_COVER
S4_STATUS=OPEN_ON_EXCEPTIONAL_SQUARE_COVER

NEW_CANONICAL_LOCAL_INVARIANT=[C^2+(B^2-A^2)(P2^2+P3^2)]_Qp
NEW_EXCEPTIONAL_LOCUS=W^2=C^2+(B^2-A^2)(P2^2+P3^2)

RETIRED_AFTER_R6=PROFILE_SPECIFIC_DISCRIMINANT_EXPANSION__I5_VALUE_ONE_AS_UNIVERSAL_CONJECTURE__2_5_REDUCED_SHELL_LOCAL_COVER__ARBITRARY_CANONICAL_NORMALIZATIONS

R7_AUTHORIZED=YES_ROUTE_B
R7_ARCHITECTURE=EXCEPTIONAL_SQUARE_LOCUS_SOURCE_INTERSECTION
R7_SINGLE_ATTACK_TARGET=(W0-C0)(W0+C0)=(B0^2-A0^2)(P2^2+P3^2)_WITH_FULL_SOURCE_INCIDENCE
```

---

# 37. Companion Artifact Recommendations

建议归档：

```text
105_R6_General_Profile_Parameter_Ledger.csv
105_R6_Normalization_Audit.csv
105_R6_Discriminant_Registry.csv
105_R6_Local_Square_Class_Atlas.csv
105_R6_Mod5_Source_Orbit.csv
105_R6_Finite_Local_Cover.csv
105_R6_Evasion_Profile_Registry.csv
105_R6_Square_Locus.json
105_R6_scripts/
```

本轮已经实际生成：

```text
105_R6_Square_Locus.json
105_R6_scripts/verify_general_discriminant.py
105_R6_scripts/verification_output.txt
```

脚本仅承担 exact identity / canonical specialization / local-square regression verification，不承担 global nonexistence proof。

---

# 38. Provenance / Verification Notes

主要 frozen source：

- `105_R5C_Moving_Base_Full_Source_Decision.md`
- `105_R3_Source_Completed_Valuation_Atlas.md`
- `strict_layer_A1_unified_moving_profile_terminal_campaign.md`
- `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`
- `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
- `95_R6_T0_Transition_Finite_Borrow_Affine_Boundary_Margin_Assault.md`
- `95_R9_Outer_Plus_No_Borrow_Projective_Smallness_Assault.md`

计算与 theorem 的边界：

**Theoremized / exact symbolic:** general master normalization、nondegeneracy、discriminant lemma、alternative elimination consistency、complementary-form identity、R5C specialization、R5C 2/5-adic failure、5-adic dominance/tie rule。

**Exact finite arithmetic witness:** reduced-shell \(V=100120\) local evasion and its factorization。

**Not proved:** exceptional square cover与 full source outer selector的交为空或非空；不存在任何由有限 search 推导的 global conclusion。

---

# 39. Final Architecture Statement

R5C 首次发现的 odd \(5\)-adic discriminant不是偶然的“坏算式”；它确实来自一个 canonical quadratic fibre invariant。

但 R6 证明了必须把两个命题分开：

\[
\boxed{
\text{the invariant is canonical}
}
\]

与

\[
\boxed{
\text{the R5C value of that invariant is universal}.
}
\]

前者已证明，后者没有成立，并且 reduced outer source shell 已经可以同时规避 \(2\)-与 \(5\)-adic local failure。

因此下一步唯一合理对象不是继续扩展 local congruence atlas，而是直接攻击：

\[
\boxed{
W^2=\mathscr D(\mathbf s)
}
\]

与 source selector 的 intersection。

这把 R6 的 remaining uncertainty 从“general moving profiles 会不会逃”压成了一个单一、exact、可重建、可积分化审计的 arithmetic incidence problem。
