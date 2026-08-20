# 105-R29 阶段归档
## Architecture-Free μ-Core Audit × Smith-Collision Falsification × Post-Radial Support Saturation

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — `(A_1)`-only  
**Round:** 105-R29  
**Status:** FROZEN / ARCHIVED  
**Date:** 2026-08-20  
**Arithmetic:** exact integer / exact rational arithmetic

---

# Executive Verdict

R29 的主攻命题

\[
\text{TC1+shape+positive radial}
\Longrightarrow
(\mu,C_2C_3)>1
\]

是 **false**，而且存在正式历史 frozen witness 直接构成 genuine counterexample。

最强真实结论：

\[
\boxed{\texttt{MU\_SMITH\_UNIVERSAL\_COLLISION=FALSE}.}
\]

反例为

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*;n,m,k,g)=(1,20,1,80;4,1,1,0),
\]

其

\[
(C_2,C_3,\mu)=(71,4727,4),
\]

并同时通过：

- primitive sphere；
- legal selectors；
- shape gcd；
- R28 TC1；
- positive radial；
- master corridor；
- μ-Smith；
- tail support。

但是

\[
\gcd(4,71\cdot4727)=1.
\]

因此 R29 不可能签 `ARCHITECTURE_FREE_MU_SMITH_EXTINCTION=YES`。

反例继续向下追杀后，第一失败门为 denominator ratio/chamber：

\[
\Theta=1/50<1/10,
\]

且 R26 对同一 primitive packet 的完整 carrier-only replay 给出唯一 candidate

\[
Z_-=50>Z_+=9,
\]

从而该 packet 全局不可 lift。

R29 同时证明一个新的 architecture-free support theorem：

\[
\boxed{
\operatorname{supp}(\mu)\cap\operatorname{supp}(C_2C_3)
\subseteq\{2,5\}.
}
\]

所以非十进制 Smith collision 全部自动不可能；真正自由只剩 decimal-primary allocation。但反例说明 decimal-primary collision 也不是 universal。

最终：

```text
STRICT_A1_UNLIFTABILITY_PROVED=NO
ARCHITECTURE_FREE_MU_SMITH_EXTINCTION=NO
UNIVERSAL_DECIMAL_PRIME_SUPPORT_COLLISION=NO
GLOBAL_POST_RADIAL_FINITE_REDUCTION=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
MU_SMITH_UNIVERSAL_COLLISION=FALSE
R29_POST_RADIAL_SUPPORT_SATURATION_CERTIFICATE=PROVED
R29_TERMINAL_ATTACK_FAILED=YES
```

---

# Part I — File / Hash Audit

## I.1 R28 frozen artifacts recovered

R29 从 File Library 的正式 frozen references 重新恢复了：

- `105-R28-stage-archive.md`；
- `105-R28-TC1-derivation.md`；
- `105-R28-observed-architecture-registry.csv`；
- `105-R28-SHA256-MANIFEST.txt`；
- `105-R28-execution.log`；
- `105-R28-TC1-hit-registry.csv`。

R28 stage archive / manifest 同时确认以下 companion 存在并冻结：

- `105-R28-TC1-rejection-registry.csv`；
- `105-R28-factorization-registry.csv`；
- `105-R28-symbolic-elimination.txt`。

File Library 本轮只对其中部分 companion 暴露独立 parsed object；无法直接获取其原始 bytes。其存在性、文件名与 digest 由 R28 frozen manifest ledger 交叉确认；实际用于 R29 证明的公式均从 R28 stage archive / TC1 derivation / formal historical archives 重新恢复，不依赖聊天摘要。

## I.2 R28 frozen SHA-256 ledger cross-check

关键 digest：

```text
ee1bf90f78f4317eefc3e3c341c3f15828e7e69724e2b5fa393765ab106f14a1  105-R28-stage-archive.md
4dbeba031fdba7c9ead02c72a53e6300b306b5ca610aa8f9adc1931f43363f3a  105-R28-TC1-derivation.md
dae7d0c1e65d6d5dcbce852d8bcbe4dea13d631a99d9815b6cfdf0f4fd92084e  105-R28-observed-architecture-registry.csv
2bc615f781089ec1f6954c299b9cdd1df6a5ee06176f49a17075068ded099002  105-R28-execution.log
0b325db25e2305022ac0aaae92c70cc504210f2ce5fe1ce003c01a0318f2df3e  105-R28-TC1-hit-registry.csv
159fcdb0c486160868d69933746ebf519865adada84933e9ebaf460a1bb1b78b  105-R28-TC1-rejection-registry.csv
cecc01ec28000d69c0f48ec88dc03894850915e006a31d871368aa5d5a7a4f3f  105-R28-factorization-registry.csv
65a2db697194df38f48d876e201c8aa7470664d7ffa6241623d0d57995947c4d  105-R28-symbolic-elimination.txt
```

R28 frozen zip companion：

```text
a6159aab026b08c2474071fe67bff49c5b33bc5ce496a78ac9b9c5824f32162c  105-R28-frozen-artifacts.zip
```

### Hash audit limitation

File Library 提供的是 parsed/reference object，不是 active runtime 中的 R28 原始 byte path。因此 R29 **不能诚实声称**重新对 R28 bytes 做 `sha256sum`。本轮执行的是 frozen manifest ledger cross-check。

R29 自身所有新 artifacts 则在 active runtime 中实际重新计算 SHA-256；见 `105-R29-SHA256-MANIFEST.txt`。

## I.3 R29 generated artifacts

主归档 / proof：

- `105-R29-stage-archive.md`；
- `105-R29-stage-archive.sha256.txt`；
- `105-R29-mu-core-derivation.md`；
- `105-R29-smith-collision-proof.md`；
- `105-R29-POST-RADIAL-SUPPORT-SATURATION-CERTIFICATE.md`。

机器 certificates：

- `105-R29-architecture-free-certificate.csv`；
- `105-R29-exceptional-branch-registry.csv`；
- `105-R29-survivor-registry.csv`；
- `105-R29-R28-positive-radial-autopsy.csv`；
- `105-R29-gcd-valuation-registry.csv`；
- `105-R29-resultant-registry.csv`；
- `105-R29-symbolic-factorization.txt`；
- `105-R29-execution.log`。

可重跑 script：

- `105-R29-scripts/r29_support_core.py`。

没有生成 `105-R29-STRICT-A1-EXTINCTION-CERTIFICATE.md`，因为 Strict A1 global extinction 未证明；伪造该 certificate 将违反 R29 文件纪律。

---

# Part II — Frozen R28 Core

冻结

\[
X=10^m,\quad Y=10^n,\quad G=10^g,\quad K=10^k,
\]

\[
T=Q_0-P_3>0,
\quad
H=GQ_0-P_2>0,
\quad
D=KP_1-Q_0>0.
\]

R28 TC1：

\[
\boxed{
g_1^*[WT+AYH]=AWu_0XYG D.
}
\tag{TC1}
\]

R24 face definitions：

\[
P_2=u_0WC_2,
\qquad
P_3=u_0AC_3.
\]

R28：

\[
(u_0,g_1^*)=1.
\]

定义

\[
g_0=(AW,P_1),
\qquad
\mu=\frac{g_1^*}{g_0},
\qquad
a_0=\frac{AW}{g_0},
\]

\[
\ell=\frac{W+A10^{n+g}}{u_0},
\]

\[
\Xi=Q_0\ell-AW(C_3+10^nC_2)>0.
\]

R28 μ-core：

\[
\boxed{
\mu\Xi=a_0 10^{m+n+g}D.
}
\tag{MU-CORE}
\]

R24 Smith：

\[
\boxed{(\mu,C_2C_3)=1.}
\tag{SMITH}
\]

R28 已证明 Smith survivor 必有

\[
\boxed{C_3\text{ odd}.}
\]

---

# Part III — Exact `(C2,C3,Xi)` Algebra

由 face definitions：

\[
C_2=\frac{P_2}{u_0W},
\qquad
C_3=\frac{P_3}{u_0A}.
\]

并且

\[
\boxed{
u_0\Xi=WT+AYH.}
\]

这里公式左边应读作 `u_0 Xi`，即

\[
\boxed{
u_0\Xi
=W(Q_0-P_3)+A10^n(10^gQ_0-P_2).}
\]

完全展开：

\[
\boxed{
u_0\Xi
=WQ_0-WP_3+A10^{n+g}Q_0-A10^nP_2.}
\]

代 face definitions：

\[
\boxed{
u_0\Xi
=Q_0(W+A10^{n+g})-u_0AW(C_3+10^nC_2).}
\]

从而

\[
\Xi
=Q_0\ell-AW(C_3+10^nC_2).
\]

### Support-core fully expanded normal form

写 `r=m+n+g`，清掉 `ell,Xi`：

\[
\begin{aligned}
0=F_{\rm support-core}:={}&
\mu Q_0W
+\mu A10^{n+g}Q_0
-\mu u_0AWC_3\\
&-\mu u_0AW10^nC_2
-u_0a_0 10^{r+k}P_1
+u_0a_0 10^rQ_0.
\end{aligned}
\tag{SC}
\]

该式不产生新 factor；它是 TC1 在 `g1*=g0 mu`, `AW=g0 a0` 与 face substitutions 下的等价重写。

### TC1 与 R24 Direct-W 完全相同

R24 Direct-W：

\[
W[u_0AXYGD-g_1^*T]=g_1^*AYH.
\]

移项即

\[
AWu_0XYGD=g_1^*(WT+AYH),
\]

正是 TC1。

故：

\[
\boxed{\texttt{TC1\_EQUALS\_DIRECT\_W\_MASTER=YES}.}
\]

---

# Part IV — `(2/5)`-adic Support Allocation

## IV.1 New coprimality

由 `g0=(AW,P1)`：

\[
\left(a_0,\frac{P_1}{g_0}\right)=1.
\]

又 `mu|P1/g0`，所以

\[
\boxed{(\mu,a_0)=1.}
\]

## IV.2 μ divides decimal scale times Q0

MU-CORE 给

\[
\mu\mid10^rD.
\]

而 `mu|P1` 且

\[
D=10^kP_1-Q_0\equiv-Q_0\pmod\mu,
\]

故

\[
\boxed{\mu\mid10^rQ_0.}
\]

## IV.3 Nondecimal support is globally safe

任意 prime `p != 2,5`，若 `p|mu`，则 `p|Q0,P1`。

若再有 `p|C2`，则 `p|P2`，sphere 强迫 `p|P3`；若 `p|C3` 同理强迫 `p|P2`。均违反 primitive。

所以

\[
\boxed{
\operatorname{supp}(\mu)\cap\operatorname{supp}(C_2C_3)
\subseteq\{2,5\}.
}
\]

这把 arbitrary-prime support bookkeeping 全部删除。

## IV.4 Exact decimal valuations

对 `p=2,5`：

\[
\boxed{
v_p(\mu)+v_p(\Xi)
=v_p(a_0)+r+v_p(D).
}
\]

primitive sphere 给 `Q0` odd；`k>=1`，故 `D` odd。因此

\[
\boxed{
v_2(\mu)+v_2(\Xi)=v_2(a_0)+r.
}
\]

若 `2|mu`，由 `(mu,a0)=1` 得 `a0` odd，于是

\[
v_2(\mu)+v_2(\Xi)=r.
\]

但这不迫使 radial support 偶：真实 counterexample 的 `C2,C3` 均为 odd。

---

# Part V — Positive-Radial Fusion

R24 positive radial 是存在 integer `U>=1` 使

\[
10^{n_2-1}\le UC_2<10^{n_2},
\]

\[
10^{n-1}\le UC_3<10^n,
\]

其中

\[
n_2=m+g+k.
\]

R29 主动测试的两个理想 size-kill：

\[
0<\Xi<10^r,
\qquad
0<\Xi<\min(C_2,C_3)
\]

均为 false。

在 genuine support-pass counterexample 上

\[
\Xi=35,575,000,
\qquad
10^r=100,000,
\qquad
\min(C_2,C_3)=71.
\]

因此 radial positivity 不给足以杀 MU-CORE 的 universal Xi upper bound。

此反例还展示 exact decimal absorption：

\[
v_2(\mu)=2,
\quad
v_2(\Xi)=3,
\quad
r=5,
\]

\[
v_5(\mu)=0,
\quad
v_5(\Xi)=5.
\]

即 2-adic content 在 `mu/Xi` 间分配，而 5-adic content 可全部由 `Xi` 吸收；`C2*C3` 同时保持 ten-unit。

---

# Part VI — Historical Autopsy

R28 execution ledger 对其 **observed** 31 个 fixed architectures 做全 conic completion，得到 exactly 4 个 global positive-radial conic points，0 个 R24 support points。R28 同时明确声明该 architecture 集合不是 global cover。

R29 对这 4 个点做 exact symbolic autopsy：

| ID | packet | `(A,W,u0,g1*)` | `(C2,C3,mu)` | `gcd(mu,C2)` | `gcd(mu,C3)` | total | shape |
|---|---|---|---|---:|---:|---:|---|
| ARCH_07 | `(240,1155,56;1181)` | `(1,1,7,80)` | `(165,8,80)` | 5 | 8 | 40 | pass |
| ARCH_08 | same | `(7,7,1,80)` | `(165,8,80)` | 5 | 8 | 40 | fail |
| ARCH_24 | `(480,1040,2499;2749)` | `(3,2,1,240)` | `(520,833,40)` | 40 | 1 | 40 | pass |
| ARCH_30 | `(200,365,104;429)` | `(13,1,1,40)` | `(365,8,40)` | 5 | 8 | 40 | pass |

其中 ARCH_08 在 shape gcd `(A,W)=7` 已死。

历史 `gcd=40` 的 prime mechanism 并不统一：

- ARCH_07 / ARCH_30：`5` 来自 `C2`，`2^3` 来自 `C3`；
- ARCH_24：整个 `2^3*5` 都来自 `C2`。

更关键的是，R20/R21 genuine support point 给

\[
(\mu,C_2,C_3)=(4,71,4727),
\]

其 total gcd = 1。

因此

\[
\boxed{d_{\rm forced}=1.}
\]

R28 的 40 没有任何 nontrivial universal component。

完整 exact autopsy 见：

- `105-R29-R28-positive-radial-autopsy.csv`；
- `105-R29-gcd-valuation-registry.csv`。

---

# Part VII — Counterexample Search

R29 没有继续无意义扩大 raw-TC1 bound，而是按要求直接搜索 post-radial Smith-admissible core。

历史 frozen R20/R21 已经提供一个 genuine full-support-stack pass：

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*)=(1,20,1,80),
\]

\[
(n,m,k,g)=(4,1,1,0).
\]

恢复：

\[
C_2=71,
\quad C_3=4727,
\quad g_0=20,
\quad\mu=4,
\]

\[
T=250,
\quad H=3557,
\quad D=1423,
\]

\[
\ell=10020,
\quad\Xi=35,575,000,
\quad r=5.
\]

### Exact TC1

\[
80[20\cdot250+10^4\cdot3557]
=2,846,000,000,
\]

\[
20\cdot10^5\cdot1423
=2,846,000,000.
\]

### Exact μ-core

\[
4\cdot35,575,000
=142,300,000
=10^5\cdot1423.
\]

### Shape / radial / Smith

\[
(1,71)=(20,4727)=(1,20)=1,
\]

radial interval：

\[
U_{\rm rad}=[1,1].
\]

Smith：

\[
\boxed{\gcd(4,71\cdot4727)=1.}
\]

### Tail support

Frozen R20/R21：

\[
\lambda_z=2,
\quad\tau=1,
\quad\Lambda=4,
\]

且 tail support gcds pass。

所以：

\[
\boxed{\texttt{MU\_SMITH\_UNIVERSAL\_COLLISION=FALSE}.}
\]

### Next first-failure

\[
d=(n+g)-m=3,
\]

\[
\Theta=10^{-3}\frac{W}{A}=\frac1{50}.
\]

故 ratio lower bound `1/10` 失败。

R26 对这个 packet 的完整 carrier-only enumeration 已证明：唯一 dual-collision tuple 正是该 tuple，且

\[
Z_-=50,
\qquad
Z_+=9.
\]

因此该 primitive packet 全局不可 lift。

---

# Part VIII — Global Theorem / Saturation

## VIII.1 What R29 proves globally

### Theorem R29-A — μ/a0 coprimality

\[
\boxed{(\mu,a_0)=1.}
\]

### Theorem R29-B — Q0 support capture

\[
\boxed{\mu\mid10^rQ_0.}
\]

### Theorem R29-C — nondecimal Smith overlap extinction

\[
\boxed{
\operatorname{supp}(\mu)\cap\operatorname{supp}(C_2C_3)
\subseteq\{2,5\}.
}
\]

### Theorem R29-D — universal μ-Smith collision is false

存在 genuine TC1 + shape + positive radial + Smith + tail point

\[
(640,1420,4727,4977;
1,20,1,80;
4,1,1,0)
\]

满足

\[
\gcd(\mu,C_2C_3)=1.
\]

### Theorem R29-E — historical gcd 40 has no universal divisor >1

因为上面 genuine survivor 的 gcd 为 1。

### Theorem R29-F — TC1-conditioned denominator ratio gives no new equation

R28 TC1 与 R24 Direct-W 是完全相同的 equation，故 post-support/master locus 上：

\[
\boxed{
\texttt{TC1\_CONDITIONED\_DENOMINATOR\_RATIO\_INFORMATION\_GAIN=0}.
}
\]

这不是“证明不出来”的声明，而是 exact semantic equivalence。

## VIII.2 What remains globally

R29 没有证明所有 primitive carriers extinction，也没有得到 global finite post-radial core。

R26 已经给出真正 architecture-free terminal carrier predicate：固定 primitive sphere packet

\[
\pi=(P_1,P_2,P_3,Q_0),
\]

其 full lift iff finite exact predicate

\[
\mathcal C_{26}(\pi)=1.
\]

因此当前未消掉的全局对象精确为

\[
\boxed{
\mathscr P_{26}
=
\{\pi\text{ positive primitive sphere packet}:\mathcal C_{26}(\pi)=1\}.
}
\]

R27 已把其压入 packet-only exceptional locus，但已证明该 exceptional locus本身无限。

R29 的贡献是：`SUPPORT_ADMISSIBLE_TC1_MU_CORE` 不再可以靠 universal μ-Smith collision 消失；其中存在真实 support survivor。该 survivor 的下一道 first-failure 是 denominator chamber。

同时，因为 TC1 = Direct-W，R29 不允许把“TC1 × denominator ratio”包装成 R21–R25 的第二轮同义改写；任何后续推进必须引入 **独立于 TC1/Direct-W/μ-core 的 frozen gate information**，或者直接攻击 carrier-only predicate `C26(pi)` 的全局 primitive-sphere image。

---

# Answers to the Twelve Mandatory Questions

1. **μ-CORE 最简 architecture-free normal form？**  
   \(\mu\Xi=a_0 10^rD\)，并加强为 `(mu,a0)=1`, `mu|10^rD`, `mu|10^rQ0`。

2. **C2,C3 exact formulas 与 Xi？**  
   \(C_2=P_2/(u_0W), C_3=P_3/(u_0A)\)，且 `u0 Xi = W T + A 10^n H`；support-core 完全展开见 Part III。

3. **positive radial 是否给 Xi 足够强 upper bound？**  
   否。真实 counterexample 有 `Xi=35,575,000 > 10^r=100,000` 且 `>min(C2,C3)=71`。

4. **Smith 强迫哪些 prime allocation？**  
   所有 nondecimal common support 自动 impossible；只剩 `2,5`。但 decimal budget 可由 `Xi` 吸收，不能 globalize。

5. **2|mu universal？**  
   R29 未证明也未反证。真实 survivor 的 `mu=4`；但该命题即使成立也不足以杀 Smith，因为 `C2*C3` 可 odd。

6. **2|C2 universal？**  
   False：counterexample `C2=71`。

7. **5|mu universal？**  
   False：counterexample `mu=4`。

8. **5|C2C3 universal？**  
   False：`71*4727` 为 5-unit。

9. **历史 gcd 40 哪部分 structural？**  
   没有 nontrivial universal divisor。R28 sample 内 prime placement 本身就不同，且 genuine support survivor gcd=1。

10. **是否存在 post-radial Smith-admissible point？**  
    Yes，上述 R20/R21 exact point，而且满足 R28 TC1 与 tail support。

11. **它下一道 first-failure？**  
    Denominator ratio/chamber，`Theta=1/50`; exact integer window `50>9`。

12. **今天是否已能证明所有 architecture support-extinct？**  
    No；该命题本身 false，因为真实 support-admissible point 存在。Strict A1 global extinction 仍未证明。

---

# Terminal Verdict

```text
R29_TERMINAL_VERDICT=MU_SMITH_UNIVERSAL_COLLISION_FALSE__POST_RADIAL_SUPPORT_SATURATED__COUNTEREXAMPLE_DIES_AT_DENOMINATOR_CHAMBER

STRICT_A1_UNLIFTABILITY_PROVED=NO
ARCHITECTURE_FREE_MU_SMITH_EXTINCTION=NO
UNIVERSAL_DECIMAL_PRIME_SUPPORT_COLLISION=NO
GLOBAL_POST_RADIAL_FINITE_REDUCTION=NO
FULL_STRICT_A1_WITNESS_FOUND=NO

MU_SMITH_UNIVERSAL_COLLISION=FALSE
GENUINE_COUNTEREXAMPLE_FOUND=YES
COUNTEREXAMPLE_TC1=PASS
COUNTEREXAMPLE_SHAPE=PASS
COUNTEREXAMPLE_POSITIVE_RADIAL=PASS
COUNTEREXAMPLE_SMITH=PASS
COUNTEREXAMPLE_TAIL_SUPPORT=PASS
COUNTEREXAMPLE_NEXT_FIRST_FAILURE=DENOMINATOR_RATIO_CHAMBER
COUNTEREXAMPLE_PACKET_UNLIFTABLE_BY_R26=YES

MU_A0_COPRIME_THEOREM=PROVED
MU_DIVIDES_10R_Q0_THEOREM=PROVED
NONDECIMAL_MU_SMITH_OVERLAP_EXTINCTION=PROVED
DECIMAL_PRIMARY_MU_SMITH_COLLISION=NOT_UNIVERSAL
HISTORICAL_GCD40_UNIVERSAL_COMPONENT=1

TC1_EQUALS_DIRECT_W_MASTER=YES
TC1_CONDITIONED_DENOMINATOR_RATIO_INFORMATION_GAIN=0

R29_POST_RADIAL_SUPPORT_SATURATION_CERTIFICATE=PROVED
R29_TERMINAL_ATTACK_FAILED=YES
```

R29 不是 Strict A1 的终局证明；但它完成了用户要求的 Verdict 6：以 genuine counterexample 严格推翻 universal μ-Smith collision，并在同一轮继续追到下一道真实 first-failure。它同时禁止未来继续把 gcd 40 或 TC1-conditioned ratio 当成 global killer。
