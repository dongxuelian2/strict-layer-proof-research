# 105-R28 阶段归档
## Full Moving-TC1 Annihilation × Decimal Gap Rigidity × Primitive-Sphere Incidence Elimination × Extinction-or-Witness

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — `(A_1)`-only  
**Round:** 105-R28  
**Status:** FROZEN / ARCHIVED  
**Arithmetic:** exact integers / exact symbolic algebra; finite searches are explicitly scoped

---

# 0. Executive Verdict

R28 没有证明 Strict-`A_1` 全局不可提升，也没有找到 full witness，也没有证明 TC1 与 R24 support 在所有 architecture 上全局不相容。

但 R28 对 TC1 做出了三次不可逆的结构坍缩，并且**证明了 raw-TC1 global extinction 本身是错误目标**：

1. TC1 完全清分母后只有一个正因子 architecture；
2. primitive 性使 `g1*` 与 `u0` 从两个 divisor selectors 变成一个 reduced rational pair，二者不再有公共尺度自由度；
3. TC1 与 R24 `W` reconstruction 完全等价地焊接，`J_NONPOS/W_NONINTEGRAL/W_MISMATCH` 在 TC1 上自动消失；
4. 进入 shape/master 后，TC1 进一步压成单一 `mu`-core：
   
   \[
   \boxed{
   \mu\Xi=\frac{AW}{g_0}10^{m+n+g}(10^kP_1-Q_0)
   }
   \]
   
   并得到新的 selector-support allocation 与 `C3` 奇性定理；
5. 更决定性地，R28 构造出一个**显式无限 primitive raw-TC1 conic family**，所以
   
   \[
   \boxed{\mathfrak T_{28}\text{ raw-TC1 incidence is infinite}.}
   \]

因此以下两个目标被正式否定：

```text
GLOBAL_RAW_TC1_EXTINCTION=FALSE
GLOBAL_RAW_TC1_FINITE_CLASSIFICATION=FALSE
```

这不是 failure；它删除了错误终局目标。真正仍可能结束 105 的只剩：

\[
\boxed{\text{TC1} \times \text{R24 support global incompatibility}.}
\]

本轮最强真实 terminal verdict 为：

```text
R28_TERMINAL_ATTACK_FAILED
```

但附带严格的

```text
R28_TC1_SATURATION_CERTIFICATE=PROVED
```

其最小剩余对象为 `SUPPORT_ADMISSIBLE_TC1_MU_CORE`，见 Part VIII。

---

# Part I — FILE AND HASH AUDIT

## I.1 R27 frozen inputs actually read

R28 开始前重新读取了：

- `105-R27-stage-archive.md`;
- `105-R27-survivor-registry.csv`;
- `105-R27-certificate-registry.csv`;
- `105-R27-execution.log`;
- `105-R27-SHA256-MANIFEST.txt`;
- `105-R27-scripts/r27_recon.py`;
- 为 exact provenance 还读取了 `105-R26-stage-archive.md` 与 `105_R24_Post_Support_Source_Carrier_Image.md`。

R27 frozen manifest 给出的关键 SHA-256：

```text
5a18cba2cbae8346300f54d845107699c4cd3f31cca7b527c11de77597bd74b2  105-R27-stage-archive.md
9a0eb6659484e94bee67ff9931916ef73836d6c2c448664930ad1864e77297f7  105-R27-survivor-registry.csv
e5b16509d83650becb1d234e6b472937c5509f4cc4cb91f93e39387e86f4df1e  105-R27-certificate-registry.csv
aae601c682ac75fb77e2ec1e7d595dd8a6c35a2e2d19072f9e342bb0a7daa55b  105-R27-execution.log
4ed2f0750d8e5f1d6a78cf48ea18fda583981c7440c8426288a1326e3f4fc85b  105-R27-scripts/r27_recon.py
```

**Hash audit limitation:** File Library 在本运行环境中提供的是 parsed/reference object，而不是可直接 `sha256sum` 的原始字节路径。因此 R28 可以逐项核对 R27 frozen manifest ledger 与 companion 中记录的 digest，但不能诚实声称在 active runtime 对 R27 原始 bytes 做了第二次 cryptographic recomputation。该限制已显式归档；R28 自身所有生成文件则在 active runtime 重新计算 SHA-256。

## I.2 R28 generated artifacts

主文件：

- `105-R28-stage-archive.md`
- `105-R28-stage-archive.sha256.txt`
- `105-R28-TC1-normal-form.md`
- `105-R28-TC1-derivation.md`
- `105-R28-execution.log`
- `105-R28-SHA256-MANIFEST.txt`

机器 registry / certificate：

- `105-R28-certificate-registry.csv`
- `105-R28-TC1-hit-registry.csv`
- `105-R28-TC1-rejection-registry.csv`
- `105-R28-exceptional-family-registry.csv`
- `105-R28-historical-hit-autopsy.csv`
- `105-R28-observed-architecture-registry.csv`
- `105-R28-observed-architecture-support-points.csv`
- `105-R28-resultant-registry.csv`
- `105-R28-factorization-registry.csv`
- `105-R28-symbolic-elimination.txt`

可重跑代码：

- `105-R28-scripts/r28_recon.py`
- `105-R28-scripts/r28_recon_fast.cpp`
- `105-R28-scripts/r28_architecture_cert.py`
- `105-R28-scripts/r28_symbolic_cert.py`

没有生成 `105-R28-complete-decision-certificate.csv`，因为 R28 **没有**得到 global finite complete classification；伪造该文件会违反本轮文件标准。

---

# Part II — EXACT TC1 NORMAL FORM

冻结

\[
X=10^m,\quad Y=10^n,\quad G=10^g,\quad K=10^k,
\]

\[
T=Q_0-P_3,\quad D=KP_1-Q_0,\quad H=GQ_0-P_2.
\]

R26/R27 exact TC1：

\[
\frac{Wg_1^*T}{AY}-g_1^*P_2
=G\left[Wu_0P_1XK-Q_0(Wu_0X+g_1^*)\right].
\]

清分母并完全展开：

\[
\boxed{
AWu_0P_1XYGK
-AWu_0Q_0XYG
-Ag_1^*Q_0YG
+Ag_1^*P_2Y
-Wg_1^*T=0.
}
\tag{R28-F}
\]

最低复杂度正因子 normal form：

\[
\boxed{
 g_1^*[WT+AYH]=AWu_0XYG D.
}
\tag{R28-PF}
\]

这里 `T>0`，`H>0`，故

\[
\boxed{D=10^kP_1-Q_0>0.}
\]

这一步立即删除了所有假想的 sign-cancellation branches。

## II.1 Hyperplane normal form

定义

\[
\begin{aligned}
c_1&=AWu_0XYGK,\\
c_2&=AYg_1^*,\\
c_3&=Wg_1^*,\\
B&=Wg_1^*+AYGg_1^*+AWu_0XYG.
\end{aligned}
\]

则

\[
\boxed{BQ_0=c_1P_1+c_2P_2+c_3P_3.}
\tag{R28-HYP}
\]

所以固定 selector/exponent architecture 后，TC1 × sphere 不是 generic high-dimensional incidence，而是一个 projective ternary conic。

---

# Part III — DECIMAL CANCELLATION CLASSIFICATION

由 frozen exponent relation

\[
m+k+g=n+\delta
\]

五项的十进制指数精确为

\[
\boxed{
2n+\delta,
\quad2n+\delta-k,
\quad n+g,
\quad n,
\quad0.
}
\]

并满足

\[
2n+\delta>2n+\delta-k>n+g\ge n>0.
\]

相邻 gaps 恰为

\[
\boxed{k,m,g,n.}
\]

因此 leading architecture 唯一：

- top `+/-` pair 精确合并为 `AWu0XYG D>0`；
- middle `-/+` pair精确合并为 `-Ag1*YH<0`；
- constant 为 `-Wg1*T<0`。

不存在“最高两项 coefficient exact cancel”这一额外 special locus；所有 leading cancellation 已被 defect `D` 完全表示。

## III.1 Exact recurrences

\[
\boxed{R_n-10R_{n+1}=9g_1^*P_2.}
\]

固定 `k=rho-m` 的合法 diagonal shift：

\[
\boxed{S_{m+1,\rho+1}=10S_{m,\rho}+9Q_0g_1^*.}
\]

TC1 对 `G` 还是一次式：

\[
\boxed{
A10^nG(g_1^*Q_0-Wu_010^mD)
=g_1^*(A10^nP_2-WT).
}
\]

所以非 `0/0` 支固定其余数据时 `G` 至多一个；`0/0` 支恰回到 R26 已冻结的 zero-over-zero branch，并不恢复 fixed-packet infinite scale。

---

# Part IV — GAP RIGIDITY

## IV.1 Proved rigidity

R28 正式证明的是：

```text
TC1_DECIMAL_ORDER_RIGIDITY_THEOREM=PROVED
FIXED_NONDEGENERATE_G_ZERO_ONE_FIBRE=PROVED
```

即 exponent ordering 与 cancellation architecture 全局固定，且固定 packet/selectors/`m,n,k` 后 `g` 非退化至多一个。

## IV.2 Universal numerical gap bound

R28 **没有**证明

\[
k,m,g,n\in\mathcal D
\]

对某个固定有限集合 `D` 全局成立。

机器侦察也明确否定了“所有 hit 都有 `m=1`”这一过强猜测：在 E27、`Q0<=3000` 的 complete-in-bound search 中，37 个 raw hits 的 signatures 为

```text
m: {1:36, 2:1}
k: {1:37}
g: {0:35, 1:2}
n: {1:17, 2:16, 3:3, 4:1}
delta: {-2:1, -1:2, 0:15, 1:19}
```

这些只是 reconnaissance，不外推成 theorem。

## IV.3 Why the gap attack stops

清分母后的 dominant decimal powers并不独立；它们被两个移动 defects

\[
D=10^kP_1-Q_0,
\qquad
H=10^gQ_0-P_2
\]

精确吸收。primitive sphere 本身不能给出 `D/H` 的统一相对 lower bound。更重要的是，Part VII 构造了无限 raw-TC1 rational conic family，证明单纯依靠 leading size / fixed-height coefficient separation 不可能消灭 TC1。

因此 R28 没有伪签 `TC1_DECIMAL_GAP_RIGIDITY_THEOREM` 的数值版本。

---

# Part V — HISTORICAL HIT AUTOPSY

R27 五个 raw hits 的 exact symbolic audit 位于 `105-R28-historical-hit-autopsy.csv`。

共同 signature：

\[
\boxed{m=k=1,\qquad\rho=2,\qquad(g_1^*,u_0)=1.}
\]

其中后一个 gcd 不只是样本规律，而在 R28 被证明为 universal primitive selector theorem。

五个 hits 的 primitive TC1 hyperplanes：

1. H1: `1000 P1 + 50 P2 + P3 = 151 Q0`; death `POSITIVE_RADIAL_BOX`.
2. H2: `3250 P1 + 130 P2 + P3 = 1626 Q0`; death `MU_SMITH`.
3. H3: `250 P1 + 15 P2 + 2 P3 = 42 Q0`; death `POSITIVE_RADIAL_BOX`.
4. H4: `400 P1 + 435 P2 + 29 P3 = 504 Q0`; death `SHAPE_GCD`.
5. H5: same primitive hyperplane as H4, different selector realization; death `SHAPE_GCD`.

因此五者**不共享一个单一 support death**，但 H4/H5 共享同一个 algebraic TC1 conic，且全部属于极低 exponent corner。

R28 还发现：R27 的 H2 不属于 E27；所以 E27 内历史四 hits 的 death types 实际只有 radial/shape。

---

# Part VI — TC1 × SUPPORT FUSION

## VI.1 Primitive selector ratio deletion

由 `u0|P2,P3` 和 primitive sphere：

\[
\boxed{(u_0,P_1)=(u_0,Q_0)=(u_0,g_1^*)=1.}
\]

所以 R28-PF 给

\[
\boxed{
\frac{g_1^*}{u_0}
=
\frac{AW10^{m+n+g}(10^kP_1-Q_0)}
{W(Q_0-P_3)+A10^n(10^gQ_0-P_2)}
}
\tag{RATIO}
\]

且右边约分后的 numerator/denominator **分别就是** `g1*`,`u0`。不存在额外 scale。

这使 R28 machine search 从枚举 `(A,W,u0,g1*)` 降成枚举 `(A,W)` 后 deterministic recovery `(g1*,u0)`。

## VI.2 TC1 = R24 W-reconstruction

R24

\[
J=u_0AXYG D-g_1^*T,
\qquad
N_W=g_1^*AYH.
\]

TC1 精确等价于

\[
\boxed{WJ=N_W.}
\]

于是任何 TC1 hit 自动满足：

```text
J>0
J | N_W
W_rec=N_W/J=W
```

所以三个历史 pre-support failure labels在 TC1 上永久退休：

```text
J_NONPOS
W_NONINTEGRAL
W_MISMATCH
```

## VI.3 New TC1 support allocation theorem

写

\[
P_2=u_0WC_2,
\qquad
P_3=u_0AC_3.
\]

TC1 推出

\[
\boxed{u_0\mid W+A10^{n+g}.}
\]

若 shape gcds 成立，则进一步：

\[
\boxed{(u_0,A)=1,}
\]

\[
\boxed{\gcd(u_0,W)=\gcd(u_0,10^{n+g}),}
\]

故 `u0` 与 `W` 的公共 prime support 只能来自 `{2,5}`。

令 `W^(10')` 为 `W` 的十进制外部分，则：

\[
\boxed{A\mid g_1^*Q_0,\qquad W^{(10')}\mid g_1^*Q_0.}
\]

这是 moving-TC1 导出的 selector-support allocation，不是 R27 packet-only capacity 的重述。

## VI.4 Mu-core

因为 `(u0,P1)=1`：

\[
g_0=(AW,P_1),
\qquad
\mu=g_1^*/g_0,
\qquad
a_0=AW/g_0.
\]

令

\[
\ell=\frac{W+A10^{n+g}}{u_0},
\]

\[
\Xi=Q_0\ell-AW(C_3+10^nC_2)>0.
\]

则 TC1 化为：

\[
\boxed{
\mu\Xi=a_0 10^{m+n+g}(10^kP_1-Q_0).
}
\tag{MU-CORE}
\]

full support 还必须满足

\[
\boxed{(\mu,C_2C_3)=1.}
\]

因此 TC1 的 post-support 本质已经压成一个 Smith-collision equation。

## VI.5 New global theorem: C3 must be odd

### Theorem R28-C3-ODD

TC1 + R24 shape gcd + mu-Smith 强迫

\[
\boxed{C_3\text{ odd}.}
\]

Proof 已完整写入 `105-R28-TC1-derivation.md`。核心是：若 `C3` even，则 shape 迫使 `W` odd；`u0|W+A10^(n+g)` 又迫使 `u0,ell` odd；primitive sphere 给 `Q0` odd，所以 `Xi` odd。mu-Smith 又迫使 `mu` odd，但 MU-CORE 右边含至少 `10^(m+n)`，必偶，矛盾。

这第一次把 TC1 与 R24 support 直接焊出一个**全局删除分支**。

## VI.6 Complete-in-bound reconnaissance and global extension of observed architectures

新的 selector-ratio search 被两套实现交叉检查：Python exact search 与 C++ exact search 在 `Q0<=500/1000` 的 packet/E27 counts 与 hit sets 一致。

C++ complete E27 search 扩到：

\[
\boxed{Q_0\le3000.}
\]

得到：

```text
ORIENTED_PRIMITIVE_PACKETS=1,840,644
E27_PACKETS=376,991
A/W_LABELS=28,853,397
EXPONENT_RECORDS=80,352,953
RAW_TC1_HITS=37
RAW_TC1_HIT_PACKETS=28
R24_SUPPORT_PLUS_TC1=0
DEATHS:
  SHAPE_GCD=9
  POSITIVE_RADIAL_BOX=26
  MU_SMITH=2
```

这些 37 hits 落入 30 个 distinct selector/exponent architectures。

然后 R28 **不再停在 bounded height**：对这 30 architectures，再加入 mandatory R27-H2 architecture，总计 31 个 fixed architectures。每个 architecture 的 TC1×sphere 都是一条 exact conic；positive radial box 给

\[
1\le C_2<10^{n+\delta},
\qquad
1\le C_3<10^n,
\]

所以可以对该 architecture 做全高度、有限、complete exact conic classification。

结果：

```text
FIXED_ARCHITECTURES_GLOBALIZED=31
GLOBAL_POSITIVE_RADIAL_CONIC_POINTS=4
GLOBAL_R24_SUPPORT_POINTS=0
```

四个 architecture-points 中：

- `(240,1155,56,1181)` 在一个 architecture 上死于 `MU_SMITH`，另一个 selector realization 先死 `SHAPE_GCD`；
- `(480,1040,2499,2749)` 死于 `MU_SMITH`；
- R27-H2 `(200,365,104,429)` 死于 `MU_SMITH`。

三条真正 shape-pass radial points 都满足

\[
\boxed{\gcd(\mu,C_2C_3)=40.}
\]

这是一条 exact finite-family theorem，**但不是所有 global TC1 architectures 的 cover theorem**。

---

# Part VII — ELIMINATION / DISCRIMINANT

## VII.1 Resultant

\[
\operatorname{Res}_{Q_0}(F_{TC1},F_{sphere})
\]

除去整体符号后就是

\[
\boxed{
(c_1P_1+c_2P_2+c_3P_3)^2
-B^2(P_1^2+P_2^2+P_3^2).
}
\]

无 universal new factor。因此依 R28 kill-line 标准：

```text
RESULTANT_INFORMATION_GAIN=0
```

路线立即停止，不伪造 resultant obstruction。

## VII.2 Solve-for-Tminus discriminant

设

\[
L_0=A10^nG(g_1^*+Wu_010^m),
\]

\[
N_0=AWu_010^{m+n}GK P_1+g_1^*A10^nP_2.
\]

TC1 × sphere 给

\[
(L_0+2g_1^*W)T^2-2N_0T+L_0(P_1^2+P_2^2)=0.
\]

其 discriminant core：

\[
\Delta_0=N_0^2-L_0(L_0+2g_1^*W)(P_1^2+P_2^2).
\]

但 exact substitution 得

\[
\boxed{
\Delta_0=(L_0P_3-g_1^*WT)^2.
}
\]

所以 square condition 自动由 TC1+sphere 提供 witness：

```text
DISCRIMINANT_INFORMATION_GAIN=0
```

没有开 Pell 新战线。

## VII.3 Infinite raw-TC1 family — decisive falsification of TC1-only extinction

R27-H1 architecture：

\[
(A,W,u_0,g_1^*,n,\delta,m,k,g)=(1,2,1,10,2,0,1,1,0)
\]

有 primitive hyperplane：

\[
\boxed{1000P_1+50P_2+P_3=151Q_0.}
\]

其 sphere intersection 被显式参数化为：

\[
\begin{aligned}
P_1&=60(6767r^2-80999rs+529833s^2),\\
P_2&=-20(21191r^2-1966698rs+5863194s^2),\\
P_3&=123(20301r^2-100000rs-977199s^2),\\
Q_0&=2565073r^2-19242000rs+170904573s^2.
\end{aligned}
\]

且

\[
Q_0-P_3=50(1361r^2-138840rs+5822001s^2).
\]

取

\[
N=10j+3,
\qquad
r=16998N+1,
\qquad
s=947N+1.
\]

则四坐标共同 content 与 10 互素；primitive normalization 保留 `10|P1`, `2|P2`, `10^2|Wg1*T/A`。显式二次多项式又证明所有 `N>=3` 正，且

\[
5P_2>P_3,
\qquad
P_2<20P_3,
\]

正是 `delta=0` window。

参数 slope 不同，故得到无限多个 distinct primitive raw TC1 packets。

正式冻结：

```text
RAW_TC1_INFINITE_CONIC_FAMILY_PROVED=YES
GLOBAL_TC1_EXTINCTION_PROVED=NO__FALSIFIED
GLOBAL_TC1_FINITE_CLASSIFICATION_PROVED=NO__FALSIFIED
```

但这个无限 family 本身被 R24 radial box **全局杀死**：固定 architecture 下 `C2,C3<=99`，complete exact conic classifier 得 0 个 radial points。

## VII.4 Decimal lifting / Zsigmondy / S-unit lines

- `mod 10^n` 的第一层 lifting 只重获 frozen `A10^n|Wg1*T` / `E` identity；
- selector-ratio reduction 比单纯 residue tree 更强，直接恢复 `(g1*,u0)`；
- 最低 TC1 normal form 没有出现需要独立处理的 `10^r±1` factor；
- resultant/discriminant均无新 factor。

因此本轮没有合法理由调用 Zsigmondy/Baker/S-unit theorem；这些路线按 `INFORMATION_GAIN=0` 处决，而不是只列工具名。

---

# Part VIII — GLOBAL RESULT

## VIII.1 What is proved globally

```text
TC1_CLEARED_INTEGRAL_NORMAL_FORM=PROVED
TC1_POSITIVE_FACTOR_NORMAL_FORM=PROVED
TC1_DECIMAL_ORDER_RIGIDITY=PROVED
PRIMITIVE_SELECTOR_GCD_THEOREM=PROVED
G1_U0_REDUCED_RATIO_RECONSTRUCTION=PROVED
TC1_EQ_R24_W_RECONSTRUCTION=PROVED
TC1_SUPPORT_U_DIVISIBILITY=PROVED
TC1_SUPPORT_SELECTOR_ALLOCATION=PROVED
TC1_SUPPORT_MU_CORE=PROVED
TC1_SUPPORT_C3_ODD_THEOREM=PROVED
RAW_TC1_INFINITE_CONIC_FAMILY_PROVED=YES
OBSERVED_31_ARCHITECTURES_GLOBAL_R24_EXTINCTION=PROVED
```

## VIII.2 What is not proved

```text
STRICT_A1_UNLIFTABILITY_PROVED=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
TC1_SUPPORT_GLOBAL_INCOMPATIBILITY_PROVED=NO
TC1_FINITE_EXCEPTIONAL_FAMILIES_PROVED=NO
UNIVERSAL_NUMERICAL_EXPONENT_GAP_BOUND=NO
```

## VIII.3 Exact saturation certificate

固定一个 selector/exponent architecture 后：

1. TC1 × sphere 是一条 projective conic（dimension 1）；
2. R24 radial box 把 `C2,C3` 放进显式 finite rectangle，所以该 architecture 的 support fibre 可 complete finite 决定；
3. R28 已对发现的 31 architectures 完成这种**全高度 global extension**并全部杀死；
4. 但 R28 没有证明 global architecture label set 本身有限，也没有证明每一个尚未发现的 architecture 必落入已杀的 31 类。

因此最终不可消灭的最小对象不是 raw TC1，也不是 primitive sphere 本身，而是：

\[
\boxed{
\mathfrak M_{28}:=
\left\{
\begin{array}{l}
\text{primitive positive sphere + shape/radial architecture},\\
 u_0\mid W+A10^{n+g},\\
 C_3\text{ odd},\\
 \mu\Xi=(AW/g_0)10^{m+n+g}(10^kP_1-Q_0),\\
 (\mu,C_2C_3)=1,\\
 \text{frozen tail support}
\end{array}
\right\}.
}
\]

称为：

```text
SUPPORT_ADMISSIBLE_TC1_MU_CORE
```

其 fibrewise dimension 已被降到 0（固定 architecture 后 finite），但 architecture index 仍为 unbounded discrete family。

这就是 R28 的 exact remaining freedom。

---

# 9. Ten mandatory questions

## Q1. TC1 完全清分母后最低复杂度 normal form？

\[
\boxed{g_1^*[W(Q_0-P_3)+A10^n(10^gQ_0-P_2)]
=AWu_010^{m+n+g}(10^kP_1-Q_0).}
\]

## Q2. 移动 exponent 有几个独立自由度？

固定 `delta` 时，`m,k,g,n` 有一个线性 relation，所以 pre-TC1 为 3 个离散自由度；固定 `(n,delta)` 后为 2 个。非退化 TC1 再固定 packet/selectors/`m,n,k` 后 `g` 至多一个。

## Q3. 是否存在 universal exponent-gap bound？

**未证明。** 已证明 universal ordering；数值 bound 不得签。`Q<=3000` 侦察只显示 `k=1`, `m<=2`, `g<=1`, 不能外推。

## Q4. leading decimal term 如何 cancellation？

唯一方式：top pair形成 positive defect `D=10^kP1-Q0`; middle pair形成 `H=10^gQ0-P2`; 最终为 PF-TC1。无第二 architecture。

## Q5. 五个 R27 hits 是否共享同一 algebraic signature？

共享 `m=k=1,rho=2` 与 primitive reduced selector scale；但不是同一 hyperplane / death。H4/H5 共享同一个 hyperplane。

## Q6. TC1 能否全局推出 R24 support failure？

**尚不能。** 已全局推出 `C3 odd` 及 selector allocation，并对 31 个 observed architectures 全高度证明 support failure；缺少 global architecture cover。

## Q7. solve-for-T 后是否产生 square discriminant？

**是。** 但 square witness恰为 `L0 P3-g1*WT`，所以 information gain 为 0。

## Q8. TC1 incidence 是否可被有限 families 完整覆盖？

**未证明。** 且 raw TC1 已证明存在无限 rational conic family；不能把 bounded architecture census冒充 global cover。

## Q9. 是否存在 genuine post-support survivor？

全局未知。complete E27 `Q<=3000` 为 0；发现的 31 architectures 向全高度延拓后也为 0。

## Q10. 今天必须结束 105，TC1 还剩哪个最小自由度？

\[
\boxed{\texttt{SUPPORT_ADMISSIBLE_TC1_MU_CORE}}
\]

即 unbounded discrete architecture label 上的 `MU-CORE + mu-Smith + radial/tail` incidence。

---

# 10. TERMINAL VERDICT

```text
R1_TO_R27_STATE_FROZEN=YES

STRICT_A1_UNLIFTABILITY_PROVED=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
GLOBAL_TC1_EXTINCTION_PROVED=NO__FALSIFIED_BY_INFINITE_CONIC_FAMILY
TC1_SUPPORT_GLOBAL_INCOMPATIBILITY_PROVED=NO
GLOBAL_TC1_FINITE_CLASSIFICATION_PROVED=NO__FALSIFIED_FOR_RAW_TC1
TC1_FINITE_EXCEPTIONAL_FAMILIES_PROVED=NO

TC1_CLEARED_INTEGRAL_NORMAL_FORM=PROVED
TC1_POSITIVE_FACTOR_NORMAL_FORM=PROVED
TC1_DECIMAL_ORDER_RIGIDITY_THEOREM=PROVED
PRIMITIVE_SELECTOR_GCD_THEOREM=PROVED
G1_U0_RATIO_ELIMINATION_THEOREM=PROVED
TC1_R24_W_RECONSTRUCTION_FUSION=PROVED
TC1_SUPPORT_SELECTOR_ALLOCATION_THEOREM=PROVED
TC1_SUPPORT_C3_ODD_THEOREM=PROVED
TC1_SUPPORT_MU_CORE=PROVED
RAW_TC1_INFINITE_CONIC_FAMILY_PROVED=YES
OBSERVED_31_ARCHITECTURES_GLOBAL_R24_EXTINCTION=PROVED

RESULTANT_INFORMATION_GAIN=0
DISCRIMINANT_INFORMATION_GAIN=0

R28_TERMINAL_ATTACK_FAILED
R28_TC1_SATURATION_CERTIFICATE=PROVED
MINIMAL_REMAINING_OBJECT=SUPPORT_ADMISSIBLE_TC1_MU_CORE
```

R28 的真正结果不是“TC1 仍然困难”。

而是：

\[
\boxed{
\text{raw TC1 已被完整撕开，并证明其本身无限；}
\\
\text{真正未闭合的只剩 support-admissible architecture index。}
}
\]
