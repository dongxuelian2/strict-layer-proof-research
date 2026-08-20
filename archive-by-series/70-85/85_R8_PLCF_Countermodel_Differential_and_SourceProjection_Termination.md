# 85 第八轮阶段报告：R7-PLCF Countermodel Differential Audit × Source-Projection Termination Decision

**项目：** 三项十进制拼接平方和问题  
**范围：** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**轮次：** 85-R8  
**主任务：** 对 R7-PLCF 做 root-independent gate differential audit，决定 source-projection programme 是否仍有未使用的独立 gate  
**最终状态：** \(J2\) OPEN  
**本轮核心判决：**

```text
ROOT_INDEPENDENT_MISSING_GATE=NONE
PRIMITIVE_COMMONSCALE_INTERSECTION=LARGE
SOURCE_PROJECTION_PROGRAMME=EXHAUSTED
R8_SUCCESS_LEVEL=R8-S3B
R8_TERMINAL_VERDICT=
SOURCE_PROJECTION_EXHAUSTED_FULL_ROOT_IS_NEXT_INDEPENDENT_GATE
```

> **Scope firewall.** 这里的 `EXHAUSTED` 是相对于已经恢复并冻结的 J2 terminal/source gate basis 而言：它证明当前 architecture 中没有尚未使用的 root-independent source gate 可以继续作为“source-projection missing invariant”。它不是一个形而上的断言，称未来绝不可能从原始方程重新组织出新的联合 root–source theorem。

---

# 1. Executive Summary

R7 已构造无限 PRE_ROOT-linear family：

\[
g=5+22t,\qquad t\ge0,
\]

\[
G=10^g,\quad K=10,\quad u=11,\quad q=\frac{G+1}{11},
\]

并取

\[
C_3=c=1,\qquad z=1,\qquad \lambda=3,
\]

使 ordinary common scale 与 coprimality 同时成立。R8 的任务不是继续攻击 endpoint jump，而是把该 family 沿真实 J2 Gate DAG 从弱到强重放，寻找第一条 **Type-A：genuine root-independent source gate**。

本轮得到的答案是：

\[
\boxed{\textbf{不存在 Type-A FAIL。}}
\]

更强地，PLCF 不只是通过 R7 当时显式使用的 linear/common-scale 信息；它还精确通过：

- 完整 negative-J2 PRE_ROOT Euclidean rows；
- regularity；
- exact common-\(V\) gcd profile；
- denominator block legality；
- primitive normalization；
- exact non-root word/master synchronization；
- 三个 numerator block 的实际 digit windows；
- common \(U=G-1\)；
- \(\gcd(U,V)=1\)；
- individual reducedness；
- A-root residue（虽属 root-necessary residue，但在该 family 上自动通过）。

PLCF 随后第一次开始失败的地方已经进入 root-derived layer：

1. **U-SQ**：失败；但 U-SQ 精确等于 full root quadratic modulo \(u\)，因此是 Type B root shadow；
2. **DCDC**：失败；85-R5 的最新 provenance 已明确 `DCDC_PRE_ROOT_PROVENANCE=FALSE`，因此仍是 Type B；
3. **sphere**：失败；但 PLCF 已满足第三 Euclidean identity，所以在 frozen state 上 sphere 与 full root 严格等价，属于 Type C；
4. **root-factor primitive gcd** \(\gcd(C_1,d_2)=1\)：PLCF 也失败（事实上 \(3\mid C_1,d_2\)），但历史证明链经过 sphere，因此同样不是 Type A；
5. **full root**：失败。

因此真正的 differential conclusion 是：

\[
\boxed{
\text{all recovered root-independent source semantics survive PLCF;}
}
\]

而

\[
\boxed{
\text{the first actual extinction comes only after root arithmetic begins.}
}
\]

这正满足 R8-S3B：source-projection campaign 应正式退休，R9 必须转向

\[
\boxed{
\mathcal V_{\rm root}
\cap
\mathcal I_{\rm exact-source}
}
\]

的联合 incidence，而不能再寻找 “lost source congruence / primitive lift / common-scale refinement”。

---

# 2. R7 Frozen Verdict

冻结 85-R7：

```text
J2_STATUS=OPEN
ORDINARY_COMMON_SCALE_PRE_ROOT_LINEAR=LARGE
COPRIME_COMMON_SCALE_PRE_ROOT_LINEAR=LARGE
ORDINARY_COMMON_SCALE_FULL_PRIMITIVE_SURVIVOR=UNKNOWN
ENDPOINT_JUMP_RIGIDITY=ABSENT
R7_TERMINAL_VERDICT=ENDPOINT_JUMP_RIGIDITY_ABSENT
```

R7 的最强 negative theorem 是无限 R7-PLCF：在当前 PRE_ROOT endpoint information class 内同时存在 ordinary common scale 与 coprime common scale。

R8 不重开 \(\delta_2,\delta_3\)、endpoint jump、Jacobsthal、generic spacing 或 \(N_0\)-split。

---

# 3. Exact PLCF Definition

对任意

\[
t\in\mathbf Z_{\ge0},\qquad g=5+22t,
\]

令

\[
G=10^g,\qquad K=10,\qquad u=11,
\]

\[
q=\frac{G+1}{11},\qquad
A=2u+1=23,
\]

\[
B=2G+q,\qquad H=\frac G2.
\]

取 R7 的原始 family parameters

\[
\boxed{c=C_3=1,\qquad z=1,\qquad \lambda=3.}
\]

于是 PRE_ROOT Euclidean reconstruction 给

\[
\boxed{C_3=1,}
\]

\[
\boxed{C_2=A+3H=\frac{3G+46}{2},}
\]

\[
\boxed{
C_1=\frac{B+69}{20}
=\frac{23G+760}{220},
}
\]

\[
\boxed{T=G+33.}
\]

negative chart 的其余量为

\[
\boxed{
h=\frac{G(G+1)}{22}-23,
}
\]

\[
\boxed{
w=\frac{G^2}{2}-253,
}
\]

\[
\boxed{
m=\frac{23G^2+G}{22}-529,
}
\]

\[
\boxed{
r=\frac{G\bigl(G(G+1)-506\bigr)}{44}-11,
}
\]

\[
\boxed{
d_2=\frac{G(G^2-506)}{2}+11.
}
\]

对 \(G\ge10^5\) 全部为正，且 R7 已审计本 chart 所需的 ten-unit/legality 条件。

因为 \(g\equiv5\pmod{22}\)，有

\[
G\equiv-1\pmod{11},
\]

并且 exact periodic congruence 给

\[
G\equiv780\pmod{2420},
\]

故

\[
\boxed{C_1\in\mathbf Z,\qquad C_1\equiv8\pmod{11}.}
\]

同时 \(10^{22}\equiv1\pmod{23}\)，所以

\[
G\equiv10^5\equiv19\pmod{23}.
\]

由 \(506=22\cdot23\) 得

\[
d_2\equiv \frac{19^3}{2}+11\equiv2\pmod{23},
\]

故

\[
\boxed{\gcd(A,d_2)=1.}
\]

PLCF 全部位于 regular chart。

---

# 4. Complete J2 Gate DAG

R8 采用以下经过 provenance 校正的 DAG。

## Layer 0 — Outer Base

\[
G=10^g,\quad K=10^k,\quad H=G/2,
\]

\[
uq=G+1,\quad A=2u+1,\quad B=2G+q,
\]

以及 Exact Resonance \(R=0,J=2\) 的 exponent/chamber relations。

## Layer 1 — Linear / Euclidean PRE_ROOT

negative-J2 chart：

\[
C_3=2r-qw,
\]

\[
d_2=2ur-w,
\]

\[
Ar-w=mH,
\]

\[
GKC_1=AC_2+m,
\]

\[
uC_2+w=HT,
\]

第三 Euclidean row：

\[
\boxed{2uKC_1=AT+z.}
\]

等价的 \((c,z,\lambda)\) parameterization：

\[
C_3=c,
\quad C_2=Ac+H\lambda,
\quad 2KC_1=Bz+A\lambda,
\quad T=Gz+u\lambda.
\]

这些均不使用 full root。

## Layer 2 — Root-independent Primitive / Word Structural Completion

从 common denominator state 定义

\[
P_1=GHC_1,
\quad P_2=uGC_2,
\quad P_3=uC_3,
\quad Q_0=P_2+d_2,
\]

\[
V=uGH.
\]

root-independent source shell 要求：

1. exact common-\(V\) gcd profile
   \[
   g_i=\gcd(V,P_i),\qquad C_i=P_i/g_i;
   \]
2. denominator blocks
   \[
   b_i=V/g_i
   \]
   具有正确 digit lengths；
3. primitive normalization
   \[
   \gcd(P_1,P_2,P_3,Q_0)=1;
   \]
4. exact non-root word/master synchronization；
5. orientation / positivity / exponent relations。

注意：这里**不**放入 primitive sphere，因为在当前 J2 chart 上它与 third Euclidean row 联合即重构 full root。

## Layer 3 — Full-Word Semantic / Common Scale

\[
a_i=UC_i,
\quad b_i=V/g_i,
\quad U\in\mathbf Z_{>0},
\]

\[
\gcd(U,V)=1,
\]

以及三个 numerator digit windows、individual reducedness、exact block reconstruction。

## Layer 4 — Root-Necessary Early Sieves / Modular Shadows

这些可比 full root 更便宜，但逻辑信息来自 root：

- A-root \(Kx\equiv-Z\pmod A\)；
- U-SQ \(x^2\equiv Z^2\pmod u\)；
- DCDC \(2K\mid\widetilde F\)；
- A-adic lifts / other root residues；
- carry-saturated root shadows。

## Layer 5 — Full Root / Root-Equivalent Package

\[
\boxed{Q_{\rm pre}(C_1)=0}
\]

或 primitive version

\[
\boxed{
Q_{\rm prim}(C_1)
=AH^2C_1^2-2uKd_2C_1+Aw^2+zd_2=0.
}
\]

在当前 third-row frozen chart 上，sphere

\[
H^2C_1^2+w^2=Td_2
\]

与 full root 等价，因此同属 Layer 5 的 Type-C package。

---

# 5. Gate Provenance Principles

本轮采用三类 FAIL：

- **Type A — Genuine Structural Fail**：原始 source 必要、root-independent、且不通过 root-equivalent sphere；
- **Type B — Root-Necessary Early Fail**：full root 的 modular/divisibility shadow；
- **Type C — Root-Equivalent Fail**：在 frozen identities 下与 full root 等价，或其证明实质经过该等价 package。

特别需要记录一个历史 provenance correction：65-R1 / 更早 carry bookkeeping 曾把 DCDC 放入 “structural/pre-root” 类，但 85-R5 的 Pre-Root Independence Firewall 已给出更细的逻辑判定：

```text
DCDC_PRE_ROOT_PROVENANCE=FALSE
DCDC_SAFE_EARLY_SIEVE=TRUE
```

R8 的问题正是 “root-independent?”，因此必须采用 **85-R5 的较新、更严格 provenance**，而不是旧 carry-ideal bookkeeping 标签。

---

# 6. Root-Independent Structural Layer

## 6.1 Outer identities — PASS

PLCF 的定义本身给

\[
uq=G+1,\qquad A=23,\qquad B=2G+q.
\]

从而

\[
qA-B=2,
\qquad
uB-GA=1.
\]

全部 exact。

## 6.2 Linear Euclidean rows — PASS

直接代入 §3 的 closed forms，恒等验证：

\[
C_3-(2r-qw)=0,
\]

\[
d_2-(2ur-w)=0,
\]

\[
Ar-w-mH=0,
\]

\[
GKC_1-AC_2-m=0,
\]

\[
uC_2+w-HT=0,
\]

\[
2uKC_1-AT-z=0.
\]

这不是 sample；附带 symbolic certificate 对一般符号 \(G\) 精确化简为零。

## 6.3 Two auxiliary master consequences — PASS

定义

\[
D=HC_2+r.
\]

则 PLCF 恒等满足

\[
\boxed{P_1K-Q_0=D,}
\]

\[
\boxed{Q_0-P_3=GHT.}
\]

所以这些 old two-row/master shadows 不产生新的 missing gate。

---

# 7. Root-Necessary Early Sieve Layer

PLCF 到达这一层以前已经通过所有恢复出的 root-independent source gates。这里第一次出现 FAIL，但它们不能被升级成 Type A。

## 7.1 A-root — PASS, but Type B provenance

primitive A-root 为

\[
KC_1+z\equiv0\pmod A.
\]

由 PRE_ROOT row

\[
2KC_1=Bz+A\lambda
\]

和

\[
B=qA-2
\]

可得

\[
2(KC_1+z)\equiv0\pmod A.
\]

\(A=23\) 为奇数，因此

\[
\boxed{KC_1+z\equiv0\pmod A.}
\]

所以 A-root 不区分 PLCF。

## 7.2 U-SQ — FAIL, Type B

历史 PRCC provenance 已证明

\[
Q(x)\equiv\frac{x^2-Z^2}{4}\pmod u,
\]

所以

\[
\boxed{x^2\equiv Z^2\pmod u}
\]

只是 full root modulo \(u\) 的 canonical shadow，不是独立 source equation。

PLCF 中

\[
x=UC_1,\qquad Z=Uz,
\]

且 \(\gcd(U,u)=1\)，故 U-SQ 等价于

\[
C_1^2\equiv z^2\pmod{11}.
\]

但

\[
C_1\equiv8\pmod{11},\qquad z=1,
\]

所以

\[
C_1^2-z^2\equiv64-1\equiv8\not\equiv0\pmod{11}.
\]

因此

```text
U_SQ_STATUS=FAIL
U_SQ_PROVENANCE=ROOT_MOD_U_SHADOW
U_SQ_FAIL_TYPE=B
```

## 7.3 DCDC — FAIL, Type B

common-\(U\) pullback 下

\[
\widetilde F
=U^2\bigl(Aw^2+zd_2\bigr).
\]

PLCF 中 \(U=G-1\equiv-1\pmod{20}\)，故 \(U^2\equiv1\pmod{20}\)。又 \(g\ge5\) 时

\[
w=G^2/2-253\equiv7\pmod{20},
\]

\[
d_2\equiv11\pmod{20}.
\]

于是

\[
Aw^2+zd_2
\equiv23\cdot7^2+11
\equiv18\pmod{20}.
\]

因为 \(2K=20\)，

\[
\boxed{20\nmid\widetilde F.}
\]

故

```text
DCDC_STATUS=FAIL
DCDC_PROVENANCE=ROOT_NECESSARY_EARLY_SIEVE
DCDC_FAIL_TYPE=B
```

这正说明：PLCF 被 root arithmetic 很早就能杀掉，但这**支持** source-projection exhaustion，而不是发现新 source gate。

---

# 8. Full-Root Layer

定义 primitive root residual

\[
Q_{\rm prim}(C_1)
=AH^2C_1^2-2uKd_2C_1+Aw^2+zd_2.
\]

由 third Euclidean row

\[
2uKC_1=AT+z
\]

有

\[
\boxed{
Q_{\rm prim}(C_1)
=A\bigl(H^2C_1^2+w^2-Td_2\bigr).
}
\tag{ROOT-SPHERE}
\]

因此在 PLCF 已冻结的 Layer-1 state 上：

\[
\boxed{
Q_{\rm prim}(C_1)=0
\iff
H^2C_1^2+w^2=Td_2.
}
\]

full root 与 sphere 是同一个剩余 equality 的两种写法。

---

# 9. PLCF Gate Differential Matrix

下表的 PLCF 三行仅作为 regression display；状态对全部 \(t\ge0\) 已由一般公式证明。

| state | outer | linear rows | common-\(V\) profile | denom legality | primitive norm. | non-root master | all digit windows | common-\(U\) | coprime | A-root | U-SQ | DCDC | sphere | full root |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLCF \(t=0\) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL-B** | **FAIL-B** | **FAIL-C** | FAIL |
| PLCF \(t=1\) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL-B** | **FAIL-B** | **FAIL-C** | FAIL |
| PLCF \(t=2\) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL-B** | **FAIL-B** | **FAIL-C** | FAIL |

其中：

- **FAIL-B** = root-necessary early failure；
- **FAIL-C** = root-equivalent failure；
- 没有任何 **FAIL-A**。

因此：

\[
\boxed{
\textbf{FIRST FAILING ROOT-INDEPENDENT GATE = NONE.}
}
\]

---

# 10. Common-(V) / Denominator Audit

定义

\[
V=uGH=\frac{11G^2}{2},
\]

\[
P_1=GHC_1,
\quad P_2=11GC_2,
\quad P_3=11.
\]

因为 \(C_1\equiv8\pmod{11}\)，

\[
\gcd(11,C_1)=1.
\]

因此

\[
\boxed{
g_1=\gcd(V,P_1)=\frac{G^2}{2}.
}
\]

又

\[
C_2=3H+23,
\]

且 \(H=5\cdot10^{g-1}\) 只含 \(2,5\)-support，所以

\[
\gcd(C_2,H)=\gcd(23,H)=1.
\]

故

\[
\boxed{
g_2=\gcd(V,P_2)=11G.
}
\]

最后

\[
\boxed{g_3=\gcd(V,P_3)=11.}
\]

于是 exact denominator blocks 为

\[
\boxed{b_1=11,}
\]

\[
\boxed{b_2=H=5\cdot10^{g-1},}
\]

\[
\boxed{b_3=GH=5\cdot10^{2g-1}.}
\]

其 digit lengths 精确为

\[
\boxed{m_1=2,\qquad m_2=g,\qquad m_3=2g.}
\]

而 numerator profile 为

\[
\boxed{n_1=2g,\qquad n_2=2g+1,\qquad n_3=g.}
\]

因此

\[
s_3=n_3-m_3=-g,
\]

\[
(s_2+s_3)
=(n_2-m_2)+(n_3-m_3)=1=k,
\]

精确满足 J2 exponent relation。

## Primitive normalization

任何公共因子必须整除 \(P_3=11\)。但 \(11\nmid P_1\)，故

\[
\boxed{\gcd(P_1,P_2,P_3,Q_0)=1.}
\]

所以 PLCF 在 canonical common-\(V\) primitive extraction 上没有缺口。

---

# 11. Primitive Master-Identity Audit

定义 primitive numerator word

\[
\mathcal A^\sharp
=C_1 10^{n_2+n_3}+C_2 10^{n_3}+C_3.
\]

PLCF 中

\[
10^{n_2+n_3}=10^{3g+1}=10G^3,
\]

所以

\[
\boxed{
\mathcal A^\sharp=10G^3C_1+GC_2+1.
}
\]

定义 denominator word

\[
\mathcal B
=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3,
\]

于是

\[
\boxed{
\mathcal B
=11G^3+HG^2+GH
=\frac{G^2(23G+1)}2.
}
\]

同时

\[
Q_0=P_2+d_2
=\frac{G^3+33G^2+22}{2}.
\]

直接 exact expansion 给

\[
\boxed{
V\mathcal A^\sharp=Q_0\mathcal B.
}
\tag{MASTER}
\]

附带 symbolic certificate 对一般 \(G\) 验证左减右恒等于零。

因此：

```text
NON_ROOT_MASTER_IDENTITY=PASS
MASTER_FIRST_FAIL=NO
```

R7-PLCF 不是 “只满足几条 linear rows 的伪 family”；在 root-independent word synchronization 意义下，它已经进入 exact pre-root source shell。

---

# 12. Full-Word/Common-Scale Audit

取 R7 的

\[
\boxed{U=G-1.}
\]

## Block 3

\[
a_3=U C_3=G-1,
\]

故

\[
\frac G{10}\le a_3<G.
\]

## Block 2

\[
a_2=(G-1)\left(\frac{3G}{2}+23\right).
\]

对 \(G\ge10^5\)：

\[
G^2<a_2<10G^2.
\]

这正是 \(n_2=2g+1\) 的 exact window，因为 \(K=10\)。

## Block 1

\[
a_1=U C_1
=\frac{(G-1)(23G+760)}{220}.
\]

下界：

\[
(G-1)(23G+760)-22G^2
=G^2+737G-760>0,
\]

故

\[
a_1>\frac{G^2}{10}.
\]

上界显然有

\[
a_1<G^2.
\]

所以

\[
\boxed{n_1=2g.}
\]

## Coprimality

\[
V=\frac{11G^2}{2}.
\]

因为 \(\gcd(G-1,G)=1\)，\(U=G-1\) 为奇数，且

\[
G\equiv-1\pmod{11}
\Longrightarrow
U\equiv-2\not\equiv0\pmod{11},
\]

有

\[
\boxed{\gcd(U,V)=1.}
\]

## Individual reducedness

common-\(V\) profile 已给：

\[
\gcd(C_1,b_1)=1,
\quad
\gcd(C_2,b_2)=1,
\quad
\gcd(C_3,b_3)=1.
\]

再结合 \(\gcd(U,V)=1\)，得到

\[
\boxed{\gcd(a_i,b_i)=1\quad(i=1,2,3).}
\]

故：

```text
FULL_THREE_BLOCK_DIGIT_LEGALITY=PASS
COMMON_U=PASS
COPRIMALITY=PASS
INDIVIDUAL_REDUCEDNESS=PASS
```

---

# 13. DCDC Provenance

R8 采用 85-R5 的最新 provenance，而不是旧 carry bookkeeping：

```text
DCDC_PRE_ROOT_PROVENANCE=FALSE
DCDC_SAFE_EARLY_SIEVE=TRUE
```

逻辑链是：

\[
\text{integral full root}
\Longrightarrow
2K\mid\widetilde F.
\]

因此 PLCF 的 DCDC failure 只说明它已经被 root arithmetic 的 cheap sieve 排除，不说明 source projection 遗漏了一条独立 source condition。

本轮精确得到：

\[
\widetilde F\equiv18\pmod{20},
\]

所以 DCDC 对所有 PLCF 都失败。

结论：

```text
DCDC_PROVENANCE=ROOT_NECESSARY_EARLY_SIEVE
DCDC_CAN_BE_NEW_SOURCE_GATE=NO
```

---

# 14. Sphere Provenance

这是本轮最重要的 dependency theorem。

历史上 sphere 本身来自原始 Pythagorean/source semantics；若单独看公式，它并不是通过先写 \(Q_{\rm pre}=0\) 才能被“发现”。

但是 R8 关心的是：**在当前 frozen J2 state 中，它是否仍提供独立于 full root 的信息？**

答案是否定的。

因为 PLCF / current linear state 已包含第三 Euclidean row

\[
2uKC_1=AT+z,
\]

而恒等式 (ROOT-SPHERE) 给

\[
Q_{\rm prim}(C_1)
=A\bigl(H^2C_1^2+w^2-Td_2\bigr).
\]

所以：

\[
\boxed{
\text{sphere}
\iff
\text{full primitive root}
\quad\text{on the frozen Layer-1 state}.
}
\]

因此正式判决为：

```text
SPHERE_PROVENANCE=ROOT_EQUIVALENT_ON_FROZEN_STATE
SPHERE_FAIL_TYPE=C
SPHERE_CAN_BE_R8_SOURCE_GATE=NO
```

这同时解释了为什么 R3/R4 的若干 “primitive root-factor gcd” 不能在 R8 被重新包装成 Type A。

---

# 15. First Failing Gate

## 15.1 Root-independent search

逐层 replay 后：

\[
\boxed{
\texttt{ROOT_INDEPENDENT_MISSING_GATE=NONE}.
}
\]

不存在 PLCF 第一次失败的 Type-A gate。

## 15.2 First actual failures after root arithmetic begins

按 cheap residue 顺序：

- A-root：PASS；
- U-SQ：FAIL-B；
- DCDC：FAIL-B；
- sphere：FAIL-C；
- full root：FAIL。

因此 “PLCF 的 first fail” 与 “first root-independent fail” 必须严格分开。

## 15.3 Apparent primitive gcd failure is not Type A

由 \(G=10^g\equiv1\pmod3\) 且

\[
C_1=\frac{23G+760}{220},
\]

有

\[
3\mid C_1.
\]

同时

\[
d_2=\frac{G(G^2-506)}2+11
\]

也满足

\[
3\mid d_2.
\]

所以 PLCF 确实违反历史 root-factor theorem

\[
\gcd(C_1,d_2)=1.
\]

但 85-R3 的 provenance proof 明确使用 sphere：先由 \(p\mid C_1,d_2\) 和 sphere 推出 \(p\mid w\)，再沿 Euclidean rows 传播到 primitive normalization 矛盾。

因此该 gcd theorem 的 dependency chain 包含 sphere；而 sphere 在 frozen state 上又 root-equivalent。

故：

```text
ROOT_FACTOR_GCD_FAIL=TRUE
ROOT_FACTOR_GCD_PROVENANCE=SPHERE_DEPENDENT
ROOT_FACTOR_GCD_FAIL_TYPE=C
```

不能把它提升为 `Primitive Compatibility Theorem`。

---

# 16. Positive-Control Validation

本轮没有发现 Type-A candidate，因此 positive controls 的作用不是为某个新 gate “背书”，而是验证 provenance 分层没有误杀历史 source-derived states。

## Control A — synchronized A1 primitive state（architecture control）

历史 exact synchronized state

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),\qquad V=24
\]

精确满足：

- primitive sphere；
- exact GSYNC/master；
- exact common-\(V\) profile；
- denominator legality；
- primitive normalization；

最终死于 common-\(U\) gate。

它不属于当前 J2 branch，但严格验证了：primitive sphere/master/profile 与 radial integer scale 本来就是不同 semantic layers，不能把后者偷渡进 primitive equation。

## Control B — R5 boundary DCDC-pass regular primitive state

\[
(q,g,k,\ell,\alpha,t)
=(11,359,359,359,228530,13).
\]

历史 exact audit 给

\[
d_A=1,
\quad \gcd(Z,u)=1,
\quad 2K\mid\widetilde F,
\]

且真实 root interval 与 source affine window 有 interior overlap，但 discriminant nonsquare，故死于 arithmetic root layer。

这证明：DCDC 即使 PASS 也不能代替 full root。

## Control C — R5 reverse DCDC-pass regular primitive state

\[
(q,g,k,\ell,\alpha,t)
=(7,9,8,10,337012,25).
\]

同样满足 regular primitive + DCDC，而最终仍由 arithmetic root layer排除。

## Control D — R6 same-base common-scale pseudo-state

在 actual split base

\[
(g,k,u,q)=(4,1,73,137)
\]

历史 R6 state 取

\[
C_1=1073,\quad C_2=45441,\quad U=2201
\]

通过 linear rows、common-\(U\)、coprimality，却有 nonzero sphere residual。

它与 PLCF 一起说明：common scale 可在 root 之前稳定存在，而 sphere/root 是后层信息。

没有任何 positive control 被本轮声称的 root-independent completion set 误杀。

---

# 17. Primitive Compatibility Theorem, if any

本轮**没有**合法的 Type-A `Primitive Compatibility Theorem`。

更准确地，恢复出的 root-independent primitive completion set 是：

\[
\boxed{
\mathcal P_{\rm prim}^{\rm ind}
=
\mathcal P_{\rm linear}
+
\left\{
\begin{array}{l}
\text{common-}V\text{ gcd profile},\\
\text{denominator legality},\\
\text{primitive normalization},\\
\text{exact non-root master},\\
\text{orientation/exponent compatibility}
\end{array}
\right\}.
}
\]

而 PLCF 对全部这些条件 PASS。

因此差集

\[
\mathcal P_{\rm prim}^{\rm ind}
\setminus
\mathcal P_{\rm linear}
\]

已被显式计算并 replay；其中没有一项杀掉 PLCF。

以下对象**不**列入该差集：

- sphere：Type C；
- \(\gcd(C_1,d_2)=1\)：sphere-dependent Type C consequence；
- U-SQ：Type B root shadow；
- DCDC：Type B root-necessary sieve；
- A-adic lifts：root-derived；
- full root。

---

# 18. Primitive × Common-Scale Intersection

定义 root-independent primitive shell

\[
\mathcal P_{\rm prim}^{\rm ind}
\]

如 §17，并令

\[
\mathcal W_{\rm common}
=
\{\text{all digit windows}+\exists U+\gcd(U,V)=1\}.
\]

R7-PLCF 对每个 \(t\ge0\) 都给出一个点

\[
\xi_t
\in
\mathcal P_{\rm prim}^{\rm ind}
\cap
\mathcal W_{\rm common}.
\]

因此至少有一个 unbounded infinite family：

\[
\boxed{
\left|
\mathcal P_{\rm prim}^{\rm ind}
\cap
\mathcal W_{\rm common}
\right|=\infty.
}
\]

按本轮 EMPTY / THIN / LARGE 的 architecture convention：

```text
PRIMITIVE_COMMONSCALE_INTERSECTION=LARGE
```

这里的 LARGE 意思是：它包含显式 unbounded infinite PLCF，因此不能作为 uniform extinction mechanism；不声称已经计算整个 ambient variety 的代数几何维数。

---

# 19. Codimension Ledger

| stage | new information | effect on generic ambient state | effect on R7-PLCF |
|---|---|---|---|
| \(\mathcal P_{\rm linear}\) | outer + Euclidean rows | substantial reconstruction | infinite PLCF exists |
| \(\mathcal P_{\rm prim}^{\rm ind}\) | gcd profile + denominator + primitive normalization + master | cuts generic pseudo-states | **PLCF remains infinite** |
| \(\mathcal P_{\rm prim}^{\rm ind}\cap\mathcal W_{\rm common}\) | exact digits + integer \(U\) + coprimality | genuine source-image incidence | **PLCF remains infinite** |
| + A-root | root residue mod \(A\) | cheap root shadow | PLCF still survives |
| + U-SQ | root mod \(u\) | root-derived codimension | **PLCF empty** |
| + DCDC | root divisibility | root-derived codimension | also **PLCF empty** |
| + sphere / full root | terminal equality | true remaining equality | PLCF empty |

所以 PLCF 的 one-parameter unbounded family 在**所有 root-independent source additions**之后仍然保持 one-parameter unbounded；真正 extinction 首次只由 root-derived information 产生。

这正是本轮所需的 codimension separation。

---

# 20. Source-Projection Exhaustion Audit

## Theorem R8-SPST — Pre-Root Source-Projection Saturation Theorem

在当前 J2 terminal architecture 中，采用 85-R5 的最新 root-independence provenance，并冻结 R6 的 pre-root word-semantic shell。则 R7-PLCF 对所有 \(t\ge0\) 满足：

1. outer J2 identities；
2. all PRE_ROOT linear/Euclidean rows；
3. regularity；
4. exact common-\(V\) gcd profile；
5. legal denominator blocks；
6. primitive normalization；
7. exact non-root master/word synchronization；
8. all three numerator digit windows；
9. common integer \(U=G-1\)；
10. \(\gcd(U,V)=1\) 与 individual reducedness。

PLCF 的 subsequent failures 均属于 root-derived layer：U-SQ、DCDC、sphere/full root 及其 consequences。

因此在已经恢复的 exact gate basis 内：

\[
\boxed{
\text{不存在尚未使用的 root-independent source gate
可以解释 PLCF 的失败。}
}
\]

于是：

```text
ROOT_INDEPENDENT_MISSING_GATE=NONE
SOURCE_PROJECTION_PROGRAMME=EXHAUSTED
```

这不是因为 source conditions “很弱”，而是因为我们现在有一个 explicit family 证明：**pre-root exact source shell 本身就非空且无限；剩余独立方程确实是 root/sphere equality。**

---

# 21. Retired Routes Update

R8 后正式退休以下作为 R9 主攻界面：

- common-\(U\) existence；
- endpoint jump / required jump；
- Jacobsthal / coprime density；
- lost congruence alone；
- common-\(V\) profile；
- denominator legality；
- primitive extraction / SNF compatibility alone；
- source reconstruction / saturation alone；
- \(N_0\)-split × full-word；
- root-factor gcd 作为“新的 source invariant”；
- sphere 作为“第二条 independent root equation”。

同时继续冻结 R1–R5 已退休：carry、residual、\(2/5\)-capacity、odd-prime allocation、root order。

---

# 22. Proven vs Computational Claims

## PROVED / SYMBOLIC EXACT

1. R7-PLCF 的一般 closed forms；
2. 所有 PRE_ROOT linear rows；
3. third Euclidean row；
4. regularity \(\gcd(A,d_2)=1\)；
5. common-\(V\) gcd profile；
6. denominator digit lengths；
7. primitive normalization；
8. exact non-root word master；
9. 三个 numerator windows；
10. \(U=G-1\) 与 \(\gcd(U,V)=1\)；
11. A-root PASS；
12. U-SQ FAIL，并且其 provenance 是 \(Q\bmod u\)；
13. DCDC FAIL，并且其 provenance 是 root-necessary；
14. sphere residual 的 exact polynomial；
15. sphere \(\iff\) full root on frozen third-row state；
16. \(3\mid C_1,d_2\)，故 root-factor gcd firewall fails；
17. 该 gcd firewall 的历史 proof 使用 sphere；
18. `ROOT_INDEPENDENT_MISSING_GATE=NONE` relative to recovered gate basis；
19. `SOURCE_PROJECTION_PROGRAMME=EXHAUSTED` relative to current architecture。

## EXACT REGRESSION ONLY

附带脚本对 PLCF \(t=0,1,2\) 做 exact integer regression，以防符号变量到实际 decade lengths 的实现错误。三行只用于 regression，不承担无限 family 的证明。

历史 positive controls 来自既有 exact reports/certificates；R8 未重新枚举原始 concatenation states。

## NOT PROVED

1. J2 closure；
2. singular branch closure；
3. full root-compatible locus 的全局参数化；
4. \(\mathcal V_{\rm root}\cap\mathcal I_{\rm exact-source}\) 为空；
5. 一个新的 joint-incidence theorem 已经存在；
6. 对所有可能未来重构的数学语言，source side 永远不可能产生新 insight。

---

# 23. R8 Terminal Verdict

本轮达到 R8-S2B，并进一步达到 R8-S3B。

```text
J2_STATUS=OPEN

ROOT_INDEPENDENT_MISSING_GATE=NONE

COMMON_V_PROFILE_ON_PLCF=PASS
DENOMINATOR_LEGALITY_ON_PLCF=PASS
PRIMITIVE_NORMALIZATION_ON_PLCF=PASS
NONROOT_MASTER_ON_PLCF=PASS
FULL_WORD_DIGIT_WINDOWS_ON_PLCF=PASS
COMMON_U_ON_PLCF=PASS
COPRIMALITY_ON_PLCF=PASS

A_ROOT_ON_PLCF=PASS
U_SQ_ON_PLCF=FAIL_ROOT_DERIVED
DCDC_ON_PLCF=FAIL_ROOT_DERIVED
SPHERE_ON_PLCF=FAIL_ROOT_EQUIVALENT
FULL_ROOT_ON_PLCF=FAIL

SPHERE_PROVENANCE=
ROOT_EQUIVALENT_ON_FROZEN_STATE

DCDC_PROVENANCE=
ROOT_NECESSARY_EARLY_SIEVE

PRIMITIVE_COMMONSCALE_INTERSECTION=LARGE

SOURCE_PROJECTION_PROGRAMME=EXHAUSTED

R8_SUCCESS_LEVEL=R8-S3B

R8_TERMINAL_VERDICT=
SOURCE_PROJECTION_EXHAUSTED_FULL_ROOT_IS_NEXT_INDEPENDENT_GATE
```

最重要的逻辑结论不是 “PLCF 被杀掉了”——它当然被 root arithmetic 杀掉。

真正结论是：

\[
\boxed{
\textbf{PLCF 在被 root 杀掉以前，已经通过整个恢复出的
root-independent source shell。}
}
\]

因此再寻找一条 “也许 source projection 还漏了什么” 的 gate 已经没有架构依据。

---

# 24. R9 Attack Target

R9 必须正式切换为：

\[
\boxed{
\textbf{Joint Full-Root × Exact Source-Incidence Geometry/Arithmetic}
}
\]

即研究

\[
\boxed{
\mathcal V_{\rm root}
\cap
\mathcal I_{\rm exact-source}.
}
\]

这里的正确姿势不是回到 root equation 内部逐个挖 local consequence，也不是再从 source side猜新 invariant，而是把两层作为**联合 incidence object**：

- \(\mathcal I_{\rm exact-source}\)：R8 已恢复并验证的 exact pre-root word/common-scale source shell；
- \(\mathcal V_{\rm root}\)：full root / primitive sphere 的真正剩余 equality（包括其合法 modular shadows，但不重复计数）。

R9 禁止重新返回：

- carry；
- residual；
- \(2/5\) capacity；
- odd-prime allocation；
- root order；
- \(N_0\)；
- endpoint jump；
- common-scale alone；
- lost congruence alone；
- primitive lift / saturation alone。

R9 的第一个对象应当是一个**联合 root-source incidence normal form**，而不是另一条局部 root residue。

---

# Appendix A. Exact Sphere / Root Residual on PLCF

PLCF 的 primitive sphere residual 为

\[
\boxed{
R_{\rm sph}
:=H^2C_1^2+w^2-Td_2
=-\frac{P(G)}{193600},
}
\]

其中

\[
\boxed{
P(G)=
47871G^4
+3159440G^3
-577600G^2
-1614236800G
-12321865600.
}
\]

对 \(G\ge10^5\)：

\[
3159440G^3-1614236800G>0,
\]

且

\[
47871G^4-577600G^2-12321865600>0.
\]

故

\[
P(G)>0,
\]

于是

\[
\boxed{R_{\rm sph}<0.}
\]

因此 sphere 对所有 PLCF 都严格失败，而由 (ROOT-SPHERE)：

\[
\boxed{Q_{\rm prim}(C_1)=23R_{\rm sph}<0.}
\]

full root 同样对全部 PLCF 失败。

primitive Pythagorean residual 还满足

\[
\boxed{
P_1^2+P_2^2+P_3^2-Q_0^2
=G^2R_{\rm sph}<0.
}
\]

---

# Appendix B. Historical Sources Audited

本轮主要恢复/对照：

- `85_R7_J2_Endpoint_Modular_Jump_and_CommonScale_Integer_Extinction.md`
- `85_R6_N0_Split_Family_x_FullWord_Source_Projection_Rearchitecture.md`
- `85_R5_PreRoot_Order_Collision_and_Digit_Window.md`
- `85_R3_Source_Cut_Residual_Exclusion_and_Regular_J2_Closure.md`
- `A1_J2_NRSEC_Report.md`
- `A1_J2_PRCC10_Report.md`
- `J2-65-R1-JParametric-Unimodular-Skeleton-Report.md`
- `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`
- `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`

其中 provenance 冲突采用**较晚且更专门的 85-R5 Pre-Root Independence Firewall** 作为 R8 的最终逻辑分类标准。

---

# Appendix C. Artifact / Certificate

本轮附带 exact symbolic/regression certificate：

- `85_R8_PLCF_gate_differential.py`
- `85_R8_PLCF_gate_certificate.txt`

certificate 不搜索新 solution；只验证一般代数恒等式以及 \(t=0,1,2\) 的 integer implementation regressions。
