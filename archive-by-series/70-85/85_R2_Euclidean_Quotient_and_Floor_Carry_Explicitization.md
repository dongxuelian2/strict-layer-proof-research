# 85 第二轮 — Euclidean Quotient Explicitization × Floor-Carry Externalization × Finite/Periodic Chart Decomposition × Deterministic Defect × Exact-Root Collision

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 85 第二轮  
**Primary frozen input:** `85_R1_J2_Terminal_Recompression_and_Minimal_Survivor.md`  
**Historical exact quotient package:** `J2-55-R6-Euclidean-Quotient-Defect-Report.md`, R7–R12 carry/root dependency audit  
**New exact artifacts:**

- `85_R2_Quotient_Explicitization_symbolic.py`
- `85_R2_CarrySpectrum.tsv`
- `85_R2_symbolic_execution.log`

---

# 1. Executive Summary

\[
\boxed{\textbf{J2 OPEN}}
\]

本轮的核心结论不是“又得到一个正规型”，而是对 Euclidean floor 的剩余自由度给出了一次终局级审计。

结论分成两层，而且两层必须严格区分。

## 1.1 Fixed-fibre 层：floor 已经被彻底 externalize

对每一个冻结的 nonzero-tail structural fibre，旧 55-R6 的结论可以恢复成完全精确的形式：

\[
\frac{uD_2}{\mathcal M}=P(G)+r(G),
\qquad r(G)\to0,
\]

其中 \(P\) 是显式有理二次多项式，而 \(r\) 是显式有理函数。

再引入 exact integer carry

\[
\boxed{\chi=J(G)-D\mu\in\mathbb Z},
\qquad J=DP\in\mathbb Z[G],
\]

则对所有指数都有

\[
\boxed{
\mu=P-\frac{\chi}{D}.
}
\]

在固定 fibre 上，一旦进入显式有限前缀之后的 one-grid regime，\(\chi\) 或等价的 \(\varepsilon_{\rm fl}=\mu-P\) 由一个有限且最终周期的 chart 唯一决定。

因此：

\[
\boxed{
\textbf{fixed-fibre Euclidean quotient opacity = RETIRED}.
}
\]

这是一个严格的 R2-S3 级结果，但只在 **fixed fibre** 意义下成立。

## 1.2 Moving-source-family 层：不存在当前证明意义下的统一 \(O(1)\) carry alphabet

高/边界分支的 carry denominator 是

\[
\boxed{
D_{\rm fl}=2d_0q^2(q+4)c(q),
\qquad
c(q)=q^3+10q^2+12q+8,
}
\]

而 reverse fixed-depth 表示中是

\[
\boxed{
D_R=2R^2d_0q^2(q+4)c(q).
}
\]

因此 fixed-fibre periodicity 的 modulus 本身随 \(q\)、valuation data、reverse depth 移动。

这不是 fixed-period phenomenon，而是：

\[
\boxed{\textbf{moving modulus phenomenon}.}
\]

新的 exact replay 更清楚地显示这一点。对冻结的历史 boundary corpus \(g\le1200\)：

- 总计 79 个 DCDC states；
- \(\mu-P\) 共出现 52 个不同精确值；
- 仅 \(q=11\) 的 44 个 states 就出现 44 个不同 carry 值；
- 但同一个 critical high \(q=11\) fixed fibre 的六个远距离指数，carry 完全相同。

所以实验现象恰好支持理论区分：

\[
\boxed{
\text{fixed fibre: finite/periodic}
\quad\neq\quad
\text{moving family: uniform }O(1)\text{ alphabet}.
}
\]

本轮**没有**证明 carry spectrum 在全 source family 上数学意义“无界”；不能把 52 个观测值升级成无界性 theorem。严格结论只是：现有 exact chart theorem 的 modulus 随 source data 移动，因而不能合法升级成统一固定 chart theorem。

## 1.3 Closure 层：carry-only architecture 已被历史 dependency theorem 判定不足

更关键的是，旧 R12 已经严格证明：在把 tail/RCE/DCDC/floor/carry/R8–R11 residual chain 全部饱和以后，full root 并没有被消费掉。

冻结事实是：

```text
FULL_ROOT_MOD_CARRY_IDEAL=NONZERO
```

并留下：

\[
P_B(G)=0,\quad \deg_G P_B=4,
\]

\[
P_H(G)=0,\quad \deg_G P_H=4,
\]

\[
P_R(R)=0,\quad \deg_R P_R=7,
\]

以及 special \(k=1\) reverse 的七次 polynomial。

因此：

\[
\boxed{
\text{carry explicitization can retire the floor,}
\quad
\text{but carry alone cannot consume the exact root.}
}
\]

这不是经验判断，而是 dependency-level 的严格结果。

故本轮最终 verdict 为：

```text
R2_TERMINAL_VERDICT=
QUOTIENT_EXPLICITIZATION_NOT_CLOSURE_CAPABLE
```

这里的 “NOT_CLOSURE_CAPABLE” 不表示 quotient work 失败；它表示：

\[
\boxed{
\mu\text{ 已不再是 frontier，继续只细化 carry 不值得。}
}
\]

本轮没有关闭三个 OPEN tail regions 中任何一个。

---

# 2. R1 Accepted Terminal State

85-R1 冻结：

\[
\boxed{
S_R<0,
\quad g\ge4,
\quad u>1,
\quad \ell\ge6,
\quad J=2,
\quad R=0.
}
\]

基础尺度：

\[
G=10^g,
\qquad K=10^k,
\qquad L=10^\ell,
\qquad \ell=2g-k.
\]

并有：

\[
uq=G+1,
\qquad A=2u+1.
\]

RCE source reconstruction：

\[
Z=\frac{At-2N}{q(q+4)},
\]

\[
a_3=\frac{(G-1)t-qN}{2(q+4)},
\]

\[
\mathcal X=\frac{Z+uN}{2},
\]

\[
\boxed{D_2=ua_3+G\mathcal X.}
\]

为避免记号冲突，本报告固定：

\[
\mathfrak m:=\frac L8,
\qquad
\boxed{\mathcal M:=A\mathfrak m=\frac{AL}{8}}.
\]

于是 Euclidean division 是

\[
\boxed{
uD_2=\mathcal M\mu+\varrho,
\qquad 0\le\varrho<\mathcal M.
}
\]

旧 live R6 corpus 中事实上有 \(0<\varrho<\mathcal M\)，但本轮保留 \(\varrho=0\) endpoint，不把它静默删除。

精确 root normalization：

\[
\Omega=\frac{A\mathcal X^2+ZD_2}{2K},
\]

\[
\boxed{
\mathscr R(x)=\mathcal Mx^2-uD_2x+\Omega.
}
\]

Source Level 0 root 是 \(Q(x)=0\)，而 \(\mathscr R(x)=0\) 是同一 exact root layer 的合法 normalization。

R1 当前 regular terminal variable 是唯一 source-selected CRT candidate \(x_*\) 上的 normalized exact residual quantum：

\[
\boxed{
\varepsilon_*
=
\frac{\mathscr R(x_*)}{A^3u\mathfrak m}
}
\]

（R1 中母体的 \(M\) 记号对应此 decimal scale；本报告用 \(\mathfrak m\) 避免与 Bezout identity 中的 \(M=uB\) 冲突。）

Source solution 必须满足：

\[
\boxed{\varepsilon_*=0.}
\]

---

# 3. Frozen Source Identities

按 85-R1/R2 指令冻结：

\[
uq=G+1,
\]

\[
A=2u+1,
\]

\[
B:=2G+q.
\]

于是：

\[
\boxed{qA-B=2},
\]

\[
\boxed{uB-GA=1},
\]

并令 Bezout multiplier：

\[
\boxed{M_{\rm Bez}:=uB=GA+1.}
\]

注意：历史 55 tail 文件曾把

\[
(q+2)(q^2-4q-4)
\]

也记为 \(B\)。本报告永久改记：

\[
\boxed{\mathcal B(q):=(q+2)(q^2-4q-4)}
\]

以免与当前 frozen \(B=2G+q\) 混淆。

另定义：

\[
\boxed{c(q)=q^3+10q^2+12q+8},
\qquad
C(q)=qc(q).
\]

nonzero-tail source relation 写作：

\[
\boxed{
C(q)N-\mathcal B(q)t
=
\alpha\frac{G}{d}.
}
\]

这里 \(d\) 依 tail chart 决定；high/boundary 中 \(d=d_0=2\cdot5^b\)，\(b=v_5(q+4)\)。

---

# 4. Exact Euclidean Division

## 4.1 EQL-1：先精确消掉 \(N\)

从

\[
N=\frac{\mathcal B(q)t+\alpha G/d}{qc(q)}
\]

代入 RCE reconstruction，可精确得到：

\[
\boxed{
D_2
=
\frac{
\mathcal D_3G^3+
\mathcal D_2G^2+
\mathcal D_1G+
\mathcal D_0
}
{2dq^2(q+4)c(q)}.
}
\tag{EQL-1}
\]

其中：

\[
\mathcal D_3=\alpha(q+4),
\]

\[
\mathcal D_2
=
2\alpha
+2dq^4t+14dq^3t+12dq^2t-24dqt-16dt,
\]

\[
\mathcal D_1
=
-\alpha q
+dq^4t+14dq^3t+28dq^2t+8dqt,
\]

\[
\mathcal D_0=-2dq^4t-8dq^3t.
\]

这是 exact identity，不含 asymptotic approximation。

---

## 4.2 High / Boundary exact polynomial division

令：

\[
\delta=k-g\ge0,
\qquad H=10^\delta,
\qquad L=G/H,
\qquad d=d_0.
\]

定义：

\[
\mathscr U_H
:=
\frac{uD_2}{\mathcal M}
=
\frac{8uD_2}{AL}.
\]

对 \(G\) 做 exact polynomial long division，得到：

\[
\boxed{
\mathscr U_H=P_H(G)+r_H(G).
}
\tag{H-DIV}
\]

其中

\[
\boxed{
P_H(G)=
-\frac{H}{2d_0q^2(q+4)c}
\Bigl[
-4\alpha(q+4)G^2
+2\alpha(q^2+4q-4)G
}
\]

\[
\boxed{
\qquad
-8d_0q^4tG-56d_0q^3tG-48d_0q^2tG
+96d_0qtG+64d_0tG
}
\]

\[
\boxed{
\qquad
-\alpha q^3-6\alpha q^2
+4d_0q^5t+24d_0q^4t-32d_0q^3t
-160d_0q^2t-64d_0qt
\Bigr].
}
\tag{PH}
\]

等价地，可把负号吸收进去；artifact 中冻结的是 SymPy exact expanded form。

余项为：

\[
\boxed{
 r_H(G)=
\frac{H\,\mathcal N_H^{\rm rem}(G)}
{2Gd_0q(q+4)(2G+q+2)c},
}
\tag{rH}
\]

其中

\[
\begin{aligned}
\mathcal N_H^{\rm rem}(G)
={}&-G\alpha q^3-8G\alpha q^2-12G\alpha q-8G\alpha\\
&+4Gd_0q^5t+32Gd_0q^4t+8Gd_0q^3t\\
&-176Gd_0q^2t-160Gd_0qt-64Gd_0t\\
&-16d_0q^3t-64d_0q^2t.
\end{aligned}
\]

因此：

\[
\boxed{r_H(G)=O(G^{-1})}
\]

在 frozen fibre 上成立，但本轮的 floor theorem 不依赖把 \(O(G^{-1})\) 当作 floor 替代；真正使用的是 exact rational expression 与 one-grid inequality。

把等式乘回 \(\mathcal M\)：

\[
\boxed{
uD_2=\mathcal M P_H+\mathcal M r_H.}
\]

这就是本轮 Result 1 所要求的 exact algebraic division。注意 \(\mathcal M r_H\) 不是 Euclidean integer remainder \(\varrho\)；后者只有在取 floor 以后才定义。

---

## 4.3 Reverse fixed-depth exact division

令 reverse depth \(R_{10}=10^r\)；为了不与全局 Exact Resonance \(R=0\) 冲突，本报告把历史 reverse scale \(R\) 改写为 \(R_{10}\)。

于是：

\[
L=R_{10}G,
\qquad d=d_0R_{10}.
\]

exact division 给：

\[
\boxed{
\mathscr U_R:=\frac{uD_2}{\mathcal M}
=P_R(G)+r_R(G).
}
\]

其中

\[
\boxed{
P_R(G)=
-\frac{1}{2R_{10}^2d_0q^2(q+4)c}
\Bigl[
-4\alpha(q+4)G^2
}
\]

\[
\boxed{
\qquad
+G\bigl(
-8R_{10}d_0q^4t-56R_{10}d_0q^3t-48R_{10}d_0q^2t
+96R_{10}d_0qt+64R_{10}d_0t
+2\alpha q^2+8\alpha q-8\alpha
\bigr)
}
\]

\[
\boxed{
\qquad
+4R_{10}d_0q^5t+24R_{10}d_0q^4t-32R_{10}d_0q^3t
-160R_{10}d_0q^2t-64R_{10}d_0qt
-\alpha q^3-6\alpha q^2
\Bigr].
}
\tag{PR}
\]

以及：

\[
\boxed{
 r_R(G)=
\frac{\mathcal N_R^{\rm rem}(G)}
{2GR_{10}^2d_0q(q+4)(2G+q+2)c},
}
\]

其中：

\[
\begin{aligned}
\mathcal N_R^{\rm rem}(G)
={}&4GR_{10}d_0q^5t+32GR_{10}d_0q^4t+8GR_{10}d_0q^3t\\
&-176GR_{10}d_0q^2t-160GR_{10}d_0qt-64GR_{10}d_0t\\
&-G\alpha q^3-8G\alpha q^2-12G\alpha q-8G\alpha\\
&-16R_{10}d_0q^3t-64R_{10}d_0q^2t.
\end{aligned}
\]

这也满足 fixed-depth \(r_R(G)=O(G^{-1})\)。

---

# 5. Quotient Polynomial Extraction

## 5.1 High / Boundary structural denominator

定义：

\[
\boxed{
D_{\rm fl}:=2d_0q^2(q+4)c(q).
}
\]

则：

\[
\boxed{
J_H(G):=D_{\rm fl}P_H(G)\in\mathbb Z[G]
}
\]

在合法 source parameter integrality 下成立。

所以：

\[
\mathscr U_H
=\frac{J_H(G)}{D_{\rm fl}}+r_H(G).
\]

这比 \(P+O(1)\) 强得多，因为：

1. \(J_H\) exact；
2. denominator exact；
3. remainder exact；
4. floor endpoint 可以逐点追踪。

## 5.2 Reverse denominator

对应地：

\[
\boxed{
D_R:=2R_{10}^2d_0q^2(q+4)c(q),
}
\]

\[
\boxed{
J_R(G):=D_RP_R(G)\in\mathbb Z[G].
}
\]

所以：

\[
\mathscr U_R=\frac{J_R(G)}{D_R}+r_R(G).
\]

## 5.3 Fixed low-\(k\) collapse

历史 R6 还证明：固定 \((q,k,\alpha,t)\) low-\(k\) fibre 上，主 polynomial 可进一步退化到常数 \(P_0\)，remainder 仍 \(O(G^{-1})\)。因此每个 fixed tail fibre 只剩有限 exponent prefix。

但 \(\alpha,t\) 可随 \(g\) 移动，所以这不等价于关闭整个 \((q,k)\) type。

---

# 6. Carry Definition

## 6.1 Exact integer carry

对 high/boundary 定义：

\[
\boxed{
\chi:=J_H(G)-D_{\rm fl}\mu.
}
\tag{CHI}
\]

这是 exact integer；不需要 one-grid threshold。

因此：

\[
\boxed{
\mu=P_H(G)-\frac{\chi}{D_{\rm fl}}.
}
\]

定义 rational floor carry：

\[
\boxed{
\varepsilon_{\rm fl}:=\mu-P_H(G)
=-\frac{\chi}{D_{\rm fl}}.
}
\]

reverse 同理：

\[
\chi_R:=J_R-D_R\mu,
\qquad
\varepsilon_{\rm fl,R}=-\frac{\chi_R}{D_R}.
\]

## 6.2 为什么不能直接把 \(\varepsilon_{\rm fl}\) 写成一个预设小集合

在 fixed fibre one-grid regime 中，它确实落在有限 alphabet；但 denominator \(D\) 随 source fibre 变动。

所以：

\[
\boxed{
\chi\in\{-D,\ldots,D\}
}
\]

之类 bound 即使成立，也不是 uniform \(O(1)\) states，因为 \(D\) 本身不是固定常数。

## 6.3 全局 q-content

历史 R7 的 exact integerization 进一步给出 active \(q>1\) nonzero-tail source states 上：

\[
\boxed{q\mid\chi.}
\]

这是真正的全指数结构限制。

它把 carry grid 从 spacing 1 压到 spacing \(q\)，但仍没有把全局 chart 数压成高度无关常数，因为：

\[
\frac{D_{\rm fl}}q
=2d_0q(q+4)c(q)
\]

仍随 \(q\) 移动。

---

# 7. Carry Spectrum

# Result 2 — Carry Spectrum

必须区分 theorem spectrum 与 observed spectrum。

## 7.1 Fixed-fibre theorem spectrum

设 frozen fibre 上：

\[
\mathscr U=\frac{J(G)}D+r(G),
\qquad J\in\mathbb Z[G],
\]

并选取显式 \(G_0\)，使：

\[
\boxed{|r(G)|<1/D\qquad(G\ge G_0).}
\]

令：

\[
a(G):=J(G)\bmod D,
\qquad0\le a<D.
\]

则：

\[
\boxed{
\mu=
\begin{cases}
(J-a)/D,&a>0,\\[2mm]
J/D,&a=0,\ r\ge0,\\[2mm]
J/D-1,&a=0,\ r<0.
\end{cases}
}
\tag{FLOOR-LAW}
\]

所以：

\[
\boxed{
\varepsilon_{\rm fl}
\in
\left\{-\frac aD:1\le a<D\right\}
\cup\{0,-1\}
}
\]

但在某一个 fixed fibre 上，实际出现的只是 \(a(G)\) 的有限周期 orbit，不是整个集合。

## 7.2 Periodicity

写：

\[
D=2^a5^bD_*,
\qquad \gcd(D_*,10)=1.
\]

当 \(g\ge\max(a,b)\) 后：

\[
10^g\bmod D
\]

的 ten-primary prefix 已稳定，而 prime-to-10 part 周期长度整除：

\[
\boxed{\operatorname{ord}_{D_*}(10).}
\]

由于 \(r(G)\) 的 numerator 是低次、denominator 正增长，其符号也在 fixed fibre 上最终稳定。

故：

\[
\boxed{
\varepsilon_{\rm fl}(g)
\text{ 在 fixed fibre 上最终周期。}
}
\]

## 7.3 新 exact boundary replay

本轮执行 `85_R2_Quotient_Explicitization_symbolic.py`，从 frozen source equations 重建 \(g\le1200\) 的完整历史 boundary DCDC corpus，不 hard-code states。

得到：

| \(q\) | DCDC states | distinct \(\mu-P\) | \(D_{\rm fl}\) | observed min | observed max |
|---:|---:|---:|---:|---:|---:|
| 7 | 28 | 1 | 1,994,300 | \(-7153/12950\) | 同左 |
| 11 | 44 | 44 | 97,320,300 | \(-58255/58982\) | \(-1801/58982\) |
| 17 | 5 | 5 | 194,572,140 | \(-33709/38930\) | \(-42701/272510\) |
| 19 | 2 | 2 | 355,534,460 | \(-78775/81358\) | \(-68997/81358\) |

总计：

\[
\boxed{79\text{ states},\qquad52\text{ distinct exact carry values}.}
\]

并且：

\[
\boxed{79/79:\ q\mid\chi.}
\]

所有观测 carry 都严格落在：

\[
\boxed{-1<\varepsilon_{\rm fl}<0.}
\]

## 7.4 Fixed-fibre contrast

critical high fibre：

\[
(q,\delta,\alpha,t)=(11,1,152510,31)
\]

的六个历史 exponent：

\[
471,
13077,
50895,
63501,
101319,
126531
\]

全部给出同一个：

\[
\boxed{
\varepsilon_{\rm fl}
=-\frac{11402}{29491}.
}
\]

这正是 fixed-fibre carry stabilization 的典型样本。

## 7.5 允许与不允许的结论

允许：

\[
\boxed{
\text{fixed fibre carry spectrum finite / eventually periodic.}
}
\]

允许：

\[
\boxed{
\text{moving-family exact sample already shows many carry values.}
}
\]

不允许：

\[
\boxed{
52\text{ observed values}\Rightarrow\text{global spectrum unbounded}
}
\]

因为这不是 theorem。

---

# 8. Floor-Transition Locus

# Result 4 — Carry Transition Locus

真正的 floor transition 是：

\[
\boxed{
\mathscr U=\frac{uD_2}{\mathcal M}\in\mathbb Z.
}
\]

等价：

\[
\boxed{\varrho=0.}
\]

对任意整数 \(j\)，定义：

\[
\boxed{
F_j:=uD_2-j\mathcal M.
}
\]

则：

\[
\boxed{
F_j=0
}
\]

就是 exact floor-transition hypersurface。

在 chart representation

\[
\mathscr U=J/D+r
\]

中，若 \(|r|<1/D\)：

### Case A: \(a=J\bmod D>0\)

fractional grid point 距离最近整数至少 \(1/D\)，而 \(|r|<1/D\)，因此不能跨越相邻整数。floor 唯一。

### Case B: \(a=0\)

只有这一格能发生 floor jump：

\[
\mu=J/D
\quad\text{if }r\ge0,
\]

\[
\mu=J/D-1
\quad\text{if }r<0.
\]

exact endpoint：

\[
\boxed{a=0,\quad r=0}
\]

对应：

\[
\boxed{\varrho=0.}
\]

因此本轮没有把 floor jump 当作 numerical noise；它被精确定位为 \(a=0\) chart 上的 remainder-sign crossing。

---

# 9. Finite / Periodic Chart Construction

chart data 的最小合法形式是：

\[
\boxed{
\mathcal C=
(q,\delta,\alpha,t;
 a=J(10^g)\bmod D;
 \operatorname{sgn}r\text{ if }a=0).
}
\]

固定 fibre 后，\(q,\delta,\alpha,t,D\) frozen，剩下：

1. \(10^g\bmod D_*\) 的有限周期；
2. ten-primary prefix；
3. 至多一个 endpoint sign bit。

所以 fixed-fibre chart graph 是 finite-state。

但是全 source family 中：

\[
D=D(q,b)
\]

或 reverse 中：

\[
D_R=D_R(q,b,R_{10}),
\]

会移动。

因此不能把所有 source data 塞进一个 fixed finite residue automaton 而不额外证明新的 uniform compression theorem。

本轮没有找到这样的 theorem。

---

# 10. Euclidean Quotient Chart Theorem

# Result 3 — Euclidean Quotient Chart Theorem

## Theorem 10.1 — Fixed-Fibre Euclidean Quotient Chart Theorem

对任意冻结的合法 \(q>1\) nonzero-tail structural fibre，假设 exact quotient decomposition：

\[
\frac{uD_2}{\mathcal M}=\frac{J(10^g)}D+r(10^g),
\]

其中：

\[
J\in\mathbb Z[G],
\qquad
r(G)=O(G^{-1})
\]

且 exact expression 已知。

则存在有效可计算 \(g_0\)，使对所有 \(g\ge g_0\)：

\[
|r(10^g)|<1/D.
\]

写：

\[
a_g=J(10^g)\bmod D.
\]

则 \(\mu\) 由 FLOOR-LAW 唯一决定。

此外，若：

\[
D=2^a5^bD_*,\quad(D_*,10)=1,
\]

则 \(a_g\) 在 ten-primary finite prefix 后具有 period dividing：

\[
\operatorname{ord}_{D_*}(10).
\]

故：

\[
\boxed{
\mu=P(G)+\varepsilon_{\rm fl}(g)
}
\]

且 \(\varepsilon_{\rm fl}\) 属于一个 fixed-fibre finite eventual-periodic alphabet。

### Proof

1. exact long division 给 \(J/D+r\)；
2. \(r=O(G^{-1})\) 给有效 \(g_0\)；
3. one-grid inequality 保证只有 \(a=0\) cell 可跨整数；
4. \(10^g\) modulo prime-to-ten denominator 是有限周期；
5. remainder numerator / denominator 是固定低次函数，sign eventually constant；
6. 合并即得。

\(\square\)

## Theorem 10.2 — Uniformization Firewall

上述 theorem **不能**由现有结果升级为：

> 存在与 \(q,g,k\) 无关的固定有限 charts \(\mathcal C_1,\ldots,\mathcal C_r\)，使全部 source family 的 \(\mu\) 都由这些 charts 给出。

理由不是哲学性的，而是 theorem interface 本身依赖：

\[
D_{\rm fl}=2d_0q^2(q+4)c(q),
\]

以及 reverse 的移动 denominator。

因此：

\[
\boxed{
\text{fixed-fibre periodicity = PROVED},
}
\]

\[
\boxed{
\text{uniform fixed-period source theorem = NOT PROVED}.
}
\]

本轮也没有证明后一者“绝对不可能”；只是没有任何合法依据把前者冒充成后者。

---

# 11. Deterministic Defect Formula

# Result 5 — Deterministic Defect Formula

一旦 chart 给定，floor 可以完全消失。

令 chart \(i\) 给定 exact carry \(\chi_i\)。则：

\[
\boxed{
\mu_i=\frac{J-\chi_i}{D}.
}
\]

Euclidean remainder 直接由 subtraction 得：

\[
\boxed{
\varrho_i=uD_2-\mathcal M\frac{J-\chi_i}{D}.
}
\]

source-selected root candidate：

\[
\boxed{
x_i=\mu_i-s
=\frac{J-\chi_i}{D}-s.
}
\]

定义 raw deterministic defect：

\[
\boxed{
\widehat\Delta_i
:=
\Omega-x_i(\varrho_i+\mathcal Ms).
}
\tag{DEF-RAW}
\]

完全展开：

\[
\boxed{
\widehat\Delta_i
=
\Omega-
\left(\frac{J-\chi_i}{D}-s\right)
\left[
 uD_2-\mathcal M\frac{J-\chi_i}{D}+\mathcal Ms
\right].
}
\tag{DEF-FLOORFREE}
\]

这里没有：

- floor；
- nearest integer；
- unspecified carry；
- ambiguous quotient。

为了得到 denominator-cleared integer arithmetic object，定义：

\[
\boxed{
\Delta_i^{(D)}
:=D^2\widehat\Delta_i.
}
\]

于是：

\[
\boxed{
\Delta_i^{(D)}
=
D^2\Omega
-
(J-\chi_i-Ds)
\bigl[
DuD_2-\mathcal M(J-\chi_i)+D\mathcal Ms
\bigr].
}
\tag{DEF-D}
\]

这是本轮要求的 chart-wise explicit arithmetic defect。

## 11.1 High specialization

high 有：

\[
\boxed{s=0.}
\]

所以：

\[
\boxed{
\Delta_{H,i}^{(D)}
=D^2\Omega
-(J-\chi_i)
\left[DuD_2-\mathcal M(J-\chi_i)\right].
}
\]

## 11.2 Boundary specialization

boundary：

\[
\boxed{0\le s\le20}
\]

保留 DEF-D；只有 21 个 source defect shifts，但 carry 本身不能被统一成 21 个状态。

## 11.3 Reverse

reverse 用 \((J_R,D_R,\chi_R)\) 完全同样替换即可，无需第二个 floor。

---

# 12. Exact-Root Collision

旧 R5 已证明：在 A-root + decimal-root necessities 已通过时，

\[
\boxed{
\Theta(x):=\frac{\Omega-x\varrho}{\mathcal M}\in\mathbb Z,
}
\]

且：

\[
\boxed{
\mathscr R(x)=\mathcal M(\Theta-sx).
}
\]

所以 Level 1 structural exact root 是：

\[
\boxed{\Theta=sx.}
\]

同时：

\[
\widehat\Delta_i
=\Omega-x_i(\varrho_i+\mathcal Ms)
=\mathcal M(\Theta_i-sx_i).
\]

因此：

\[
\boxed{
Q(x_i)=0
\iff
\mathscr R(x_i)=0
\iff
\Theta_i=sx_i
\iff
\widehat\Delta_i=0
\iff
\Delta_i^{(D)}=0.
}
\]

这给出完全合法的 exact-root collision。

但关键在于：

\[
\boxed{
\Delta_i^{(D)}\text{ 显式}
\quad\not\Rightarrow\quad
\Delta_i^{(D)}\ne0.
}
\]

## 12.1 Closure Form A — Exact nonzero defect

**未全局证明。**

R12 证明 carry-saturated full-root polynomial 非零，意思是 defect 不是 carry ideal 中的恒等零元素；这不等于对每个合法 source point 都非零。

## 12.2 Closure Form B — Sign contradiction

**未得到 uniform sign theorem。**

历史 exact root polynomial 的 moving coefficients 阻止了固定 sign conclusion。

## 12.3 Closure Form C — Divisibility contradiction

carry residual 确实带来大量 \(2/5/q\)-content，但 R11 已证明若只继续从旧 carry constant-term 提取 power-ten divisibility，会重新得到旧 \(\Gamma\)-core，而不是新的独立 root contradiction。

## 12.4 Closure Form D — Interval / spacing contradiction

fixed fibre 上有若干成功 extinction，例如 historical critical high q11 fibre；但没有得到覆盖整个 high/boundary/reverse family 的统一 spacing theorem。

因此：

\[
\boxed{
\text{deterministic defect explicit = YES,}
\qquad
\text{uniform defect nonvanishing = NO.}
}
\]

---

# 13. High-Tail Audit

范围：

\[
\delta>0.
\]

冻结：

\[
\boxed{s=0.}
\]

本轮得到：

1. exact \(P_H+r_H\)；
2. exact integer carry \(\chi\)；
3. fixed-fibre finite/periodic chart；
4. floor-free high defect \(\Delta_{H,i}^{(D)}\)；
5. critical \((11,1,152510,31)\) fixed fibre 的 carry constant 被 exact replay 复现。

但 moving \((q,\alpha,t)\) 情形仍不能由 stable carry equality 全局化。

历史 R7 的核心 correction 必须保留：fixed-fibre constant coefficient \(=0\) 与 all-exponent exact root congruence 不是同一陈述。

因此：

```text
HIGH_TAIL_STATUS=REDUCED
UNDERLYING_CLOSURE_STATUS=OPEN
```

---

# 14. Boundary Audit

范围：

\[
\delta=0,
\qquad q>1.
\]

冻结：

\[
0\le s\le20.
\]

新的 observed Carry Spectrum 最丰富地出现在这里：

\[
79\text{ historical DCDC states}
\to52\text{ distinct }\mu-P.
\]

这直接 falsify 任何未经证明的：

> “boundary carry 只有 \(-1,0,1\) 三个 raw states”

之类猜测。

但因为每个 exact carry 都仍可被整数化为 \(\chi\)，所以不是 floor opacity，而是 moving-family multiplicity。

同时历史 R7/R8 已有 exact unstable carry residual：

\[
\Gamma_B
=
\alpha P_\alpha-d_0tP_t-2q(D_{\rm fl}s+\chi),
\]

以及实际 root 必须满足的巨大 decimal depth，而不是全局 \(\Gamma_B=0\)。

本轮不重新搭 residual ladder。

因此：

```text
BOUNDARY_Q_GT_1_STATUS=REDUCED
UNDERLYING_CLOSURE_STATUS=OPEN
```

---

# 15. Reverse Nonzero-Tail Audit

范围：

\[
\delta<0,
\qquad q>1,
\]

且 reverse zero-tail 永久 RETIRED，不重开。

本轮得到 fixed-depth exact：

\[
\mathscr U_R=P_R+r_R,
\]

\[
D_R=2R_{10}^2d_0q^2(q+4)c,
\]

\[
\chi_R=J_R-D_R\mu.
\]

所以 reverse floor 本身也可 externalize。

但历史 reverse 审计已经暴露更强事实：

\[
\Gamma_R=R_{10}\Phi_R
\]

的 exact moving decimal-depth factor 会随 reverse scale 增长；继续追 “next carry bit” 只会重新发现 moving depth。

此外 R12 的 independent root polynomial 在 generic reverse 中仍是七次对象。

因此：

```text
REVERSE_NONZERO_TAIL_STATUS=REDUCED
UNDERLYING_CLOSURE_STATUS=OPEN
REVERSE_ZERO_TAIL_STATUS=RETIRED
```

---

# 16. DD Common-Gap Transfer Audit

# Result 7 — DD Common-Gap Audit

本轮逐个测试：

\[
\chi,
\qquad
\varrho,
\qquad
\Delta_{\rm def}.
\]

判据：

1. source cut 是否迫使非零；
2. primitive/gcd 是否给 lower bound；
3. digit shell 是否给 upper bound；
4. exact root 是否要求为零；
5. valuation/square spacing 是否给独立 restriction。

## 16.1 \(\chi\)

- source-generated：YES；
- exact integerized：YES；
- \(q\mid\chi\)：YES on active q>1 nonzero-tail；
- exact root 要求 \(\chi=0\)：NO；
- primitive lower bound：NO uniform theorem；
- global small upper bound：NO。

所以 \(\chi\) 不是 DD-style terminal gap。

## 16.2 \(\varrho\)

- exact source Euclidean remainder：YES；
- upper bound \(0\le\varrho<\mathcal M\)：YES；
- root 要求 \(\varrho=0\)：NO；
- primitive lower bound：NO；
- valuation capacity：NO independent terminal theorem。

所以 \(\varrho\) 也不是。

## 16.3 \(\Delta_{\rm def}\)

- source-selected after chart：YES；
- exact root 要求 \(\Delta=0\)：YES；
- unique/finite candidate support：YES in regular terminal architecture；
- primitive nonabsorption lower bound：尚未证明；
- independent 2/5 capacity：尚未闭合。

它最接近 DD pattern，但目前只满足 source selection + exact-zero target 两大项；还缺 primitive/capacity 的同一对象碰撞。

## 16.4 结论

没有一个单一对象同时拿到至少三项、并形成已证 closure mechanism。

所以：

```text
DD_STYLE_COMMON_GAP_FOUND=NO
```

但 R1 的 mechanism-level transfer 仍保留：

\[
\boxed{
\text{source selection}
\to
\text{canonical candidate}
\to
\text{normalized exact residual}
\to
\text{primitive/capacity attack}.
}
\]

换言之，本轮没有找到 “DD 的 gap”，但进一步确认了 R1 的判断：真正值得迁移的是 **Source-Cut Residual Exclusion architecture**，不是 carry 自身。

---

# 17. \(N_0\) Collision Audit

# Result 8 — N0 Collision Audit

冻结：

\[
B=2G+q,
\qquad
C_\pm=2GK\pm B,
\]

\[
\boxed{
N_0=2+u^2C_-C_+.
}
\]

以及：

\[
\gcd(C_-,C_+)=1,
\]

\[
N_0\equiv2\pmod{C_\pm},
\qquad
N_0\equiv2\pmod{u^2},
\]

\[
N_0\equiv1\pmod G,
\]

\[
\boxed{
v_5(N_0-1)=g,
\qquad
v_2(N_0-1)=g+1.
}
\]

本轮检查 quotient law 的 exact ingredients：

\[
(q,\delta,\alpha,t),
\quad
J(G)\bmod D,
\quad
\operatorname{sgn}r,
\]

与 \(N_0\) square-class / Gaussian split fingerprint 之间，没有发现 source-proved implication：

\[
N_0\text{ split class}
\Rightarrow
\chi\text{ chart},
\]

也没有：

\[
\chi\text{ chart}
\Rightarrow
N_0\text{ nonsplit}.
\]

这与 R1 的 architecture 一致：

\[
\boxed{
N_0=\text{outer structured prefilter},
\quad
\chi=\text{pre-root carry coordinate},
\quad
\varepsilon_*=\text{terminal source residual}.
}
\]

因此：

```text
N0_QUOTIENT_COLLISION=NO_PROMOTED_COUPLING
N0_STATUS=OUTER_PREFILTER_ONLY
```

不把 75-R8 split theory 强行接入 carry。

---

# 18. Failed Approaches / Counterexamples

## F1 — 把 \(P+O(G^{-1})\) 直接 floor 化

**ILLEGAL.**

即使误差小，若 rational polynomial part 恰在 integer grid 附近，floor 会跳。

修正：exact \(J/D+r\) + residue \(a=J\bmod D\) + endpoint sign。

## F2 — 把 fixed-fibre carry resonance 全局化

**FALSE AS A LOGICAL STEP.**

R7 已审计：固定 fibre 在 finite prefix 后从 divisibility 得 constant coefficient zero，不等于 moving source family 上 raw all-exponent identity。

修正：全局保留 unstable divisibility / normalized residual。

## F3 — 假设 carry 只有三五个状态

**COMPUTATIONALLY FALSIFIED AS A RAW MOVING-FAMILY CLAIM.**

仅 boundary historical corpus 就有 52 个不同 exact \(\mu-P\)，其中 q=11 有 44 个不同值。

这不是无界性 theorem，但足以否定“已经看到小常数 alphabet”的说法。

## F4 — 继续从 carry constant term 抽新的 power-ten obstruction

**DEPENDENCY-REDUNDANT.**

R11 已证明旧 constant-term route 只是 \(\Gamma\)-carry core 的重写。

## F5 — 认为 carry saturation 会自动等价 full root

**FALSE.**

R12：

```text
FULL_ROOT_MOD_CARRY_IDEAL=NONZERO
```

full root 在 carry saturation 后仍留下 independent low-degree exact polynomials。

## F6 — 用 predicted/discriminant root 代替 Level 0 root

**RETIRED.**

本轮所有 defect collision 都回到：

\[
Q(x)=0
\iff
\Theta=sx.
\]

---

# 19. Proven Statements vs Computational Evidence

## 19.1 PROVED

1. EQL-1 exact \(D_2\) cubic formula。
2. High/boundary exact \(P_H+r_H\) decomposition。
3. Reverse fixed-depth exact \(P_R+r_R\) decomposition。
4. \(J_H=D_{\rm fl}P_H\) exact integer polynomial presentation。
5. exact carry integerization：\(\chi=J-D\mu\in\mathbb Z\)。
6. \(\mu=P-\chi/D\) exact。
7. fixed-fibre one-grid FLOOR-LAW。
8. fixed-fibre eventual periodicity。
9. active q>1 nonzero-tail \(q\mid\chi\)（inherited exact theorem）。
10. chart-wise floor-free deterministic defect DEF-D。
11. exact-root equivalence：
    \[
    Q(x)=0\iff\Theta=sx\iff\Delta_i^{(D)}=0.
    \]
12. carry saturation 不消费 full root：R12 dependency theorem。

## 19.2 NEW EXACT COMPUTATIONAL EVIDENCE

脚本从 frozen source equations 重建：

\[
79\text{ boundary DCDC states at }g\le1200.
\]

精确输出：

\[
52\text{ distinct }\mu-P.
\]

以及：

\[
79/79:q\mid\chi.
\]

文件：

`85_R2_CarrySpectrum.tsv`。

## 19.3 NOT PROVED

1. moving source family 的 global carry spectrum 无界；
2. global chart count 数学意义必然随 q 无界；
3. \(\Delta_{\rm def}\ne0\) on all source-valid charts；
4. high/boundary/reverse 任一整个 OPEN region 被本轮关闭；
5. \(N_0\) square-class 控制 carry；
6. DD-style common gap 已在 \(\chi,\varrho,\Delta\) 中找到。

---

# 20. Formal Results 1–8

## Result 1 — Exact Euclidean Division Lemma

**PROVED.**

High/boundary：

\[
\boxed{
\frac{uD_2}{\mathcal M}=P_H(G)+r_H(G)
}
\]

with explicit PH/rH above。

Reverse fixed-depth：

\[
\boxed{
\frac{uD_2}{\mathcal M}=P_R(G)+r_R(G).
}
\]

## Result 2 — Carry Spectrum

**PROVED fixed-fibre finite/eventual-periodic; global \(O(1)\) alphabet NOT proved.**

Exact：

\[
\boxed{
\varepsilon_{\rm fl}=-\chi/D.
}
\]

Observed boundary corpus：52 distinct values / 79 states。

## Result 3 — Euclidean Quotient Chart Theorem

**PROVED in maximal legal fixed-fibre form.**

Uniform moving-family theorem not established because modulus moves。

## Result 4 — Carry Transition Locus

**PROVED.**

\[
\boxed{
\varrho=0
\iff
uD_2-j\mathcal M=0
\text{ for some }j\in\mathbb Z.
}
\]

Stable one-grid representation中只可能在 \(J\equiv0\pmod D\) cell 发生 jump，sign 由 exact \(r\) 决定。

## Result 5 — Deterministic Defect Formula

**PROVED.**

\[
\boxed{
\Delta_i^{(D)}
=
D^2\Omega
-(J-\chi_i-Ds)
[DuD_2-\mathcal M(J-\chi_i)+D\mathcal Ms].
}
\]

无 floor。

## Result 6 — Tail Region Table

| Region | R2 status | Explanation |
|---|---|---|
| \(\delta>0\) | **REDUCED** | floor explicit; high exact defect explicit; global root nonvanishing open |
| \(\delta=0,q>1\) | **REDUCED** | 21 s-shifts + exact carry; moving family remains open |
| \(\delta<0,q>1\) | **REDUCED** | reverse floor explicit; independent degree-7 root remains |
| reverse zero-tail | **RETIRED** | inherited CLOSED; not reopened |

没有新 CLOSED tail region。

## Result 7 — DD Common-Gap Audit

```text
DD_STYLE_COMMON_GAP_FOUND=NO
```

\(\Delta_{\rm def}\) 最接近，但还缺 primitive nonabsorption + capacity 同对象 theorem。

## Result 8 — N0 Collision Audit

```text
N0_QUOTIENT_COLLISION=NO_PROMOTED_COUPLING
```

保持 outer prefilter，不强行混合。

---

# 21. Success Ladder Audit

## R2-S0

超过。

## R2-S1

超过。

## R2-S2

**Fixed-fibre sense：达到。**

Global uniform sense：未达到，因为 alphabet dependence 经过 moving modulus。

## R2-S3

**Fixed-fibre sense：达到。**

\(\chi\) / \(\varepsilon_{\rm fl}\) 由有限周期 chart 唯一决定。

## R2-S4

**未达到。**

虽然每个 chart 上 deterministic defect 已显式，但没有删除整个 OPEN tail region。

## R2-S5

**未达到。**

\[
\boxed{J2\text{ remains OPEN}.}
\]

---

# 22. Kill Criteria Audit

## K1 — \(\mu-P\) 真正无界复杂度

**NOT PROVED.**

不虚构。

## K2 — chart 数随 \(q/G\) 无界增长

**STRICT UNBOUNDEDNESS NOT PROVED.**

但现有 exact theorem 的 modulus 明确随 \(q\) 移动，所以无法合法给出 fixed global chart set；observed q11 moving corpus 已有 44 distinct raw carry values。

## K3 — floor externalization 等价原 J2 equation

**FALSE.**

恰恰相反，R12 证明 full root independent modulo carry ideal。

## K4 — 需要更难分布 theorem

**NOT NEEDED TO REACH CURRENT VERDICT.**

## K5 — defect 可自由取大范围值

**NOT PROVED.**

### Closure-capability verdict 的真正依据

本轮判定 quotient route 不 closure-capable，并不是伪造 K1/K2/K5 theorem，而是使用更强的已有 dependency theorem：

\[
\boxed{
\textbf{carry ideal saturation leaves a nonzero independent full-root remainder.}
}
\]

因此 carry refinement 本身已经证明不是 complete information class。

---

# 23. R2 Terminal Verdict

最终：

```text
J2_STATUS=OPEN

FIXED_FIBRE_QUOTIENT_EXPLICITIZATION=PROVED
FIXED_FIBRE_FINITE_PERIODIC_CARRY=PROVED
EXACT_INTEGER_CARRY=PROVED
GLOBAL_UNIFORM_O1_CARRY_ALPHABET=NOT_PROVED
DETERMINISTIC_DEFECT_FLOOR_FREE=PROVED
ONE_TAIL_REGION_CLOSED=NO
DD_STYLE_COMMON_GAP_FOUND=NO
N0_QUOTIENT_COUPLING=NO_PROMOTED_COUPLING

R2_TERMINAL_VERDICT=
QUOTIENT_EXPLICITIZATION_NOT_CLOSURE_CAPABLE
```

解释：

\[
\boxed{
\text{floor 已被消灭为 frontier，}
\quad
\text{但 exact root 没有被 carry 消灭。}
}
\]

所以 85 不应继续第三次重做 quotient/carry normalization。

---

# 24. R3 Attack Target

J2 未闭，因此必须给唯一目标。

85-R1 已把 regular source profile 压到唯一 A³+decimal CRT candidate \(x_*\)。本轮又确认继续细化 \(\mu\) 不会替代 full root。

因此 R3 应恢复到真正 terminal information class：

\[
\boxed{
\textbf{R3 ATTACK TARGET}
:
q>1,
\ d_A=1,
\ x=x_*
\Longrightarrow
\varepsilon_*
e0.
}
\]

即严格证明：

\[
\boxed{
\mathcal C_{\rm source}^{\rm regular}
\cap
\{\varepsilon_*=0\}
=\varnothing.
}
\]

其中：

\[
\varepsilon_*
=
\frac{\mathscr R(x_*)}{A^3u\mathfrak m}.
\]

R3 不再问：

> carry 是什么？

而只问：

\[
\boxed{
\text{唯一 source-selected candidate 为什么不能让 exact residual quantum 为零？}
}
\]

优先碰撞顺序固定为：

\[
\boxed{
\text{source-cut image}
+
\text{primitive nonabsorption}
+
(2,5)\text{-capacity}
}
\]

并只把 \(N_0\) split fingerprint 当 secondary prefilter。

若能证明：

\[
\varepsilon_*\ne0
\]

for all regular q>1 source profiles，则 regular J2 branch 关闭；然后再进入 singular \(j\)-line。

---

# 25. Source Semantics Firewall Audit

### Check 1 — \(\mu\) 是否仍来自原 Euclidean division？

**PASS.**

\[
\mu=\left\lfloor\frac{uD_2}{\mathcal M}\right\rfloor.
\]

### Check 2 — 是否把 floor 错换成 \(z+O(1)\)？

**PASS / NO.**

使用 exact \(J/D+r\) 和 one-grid theorem。

### Check 3 — 是否忽略 endpoint \(\varrho=0\)？

**PASS / NO.**

明确保留为 floor-transition locus。

### Check 4 — 是否默认 remainder positive？

**PASS / NO.**

\(a=0\) chart 显式按 \(r\ge0\) / \(r<0\) 分裂。

### Check 5 — 是否除以 \(q-1,\delta\) 或 defect 丢 boundary？

**PASS / NO.**

high/boundary/reverse 分支只在合法 source chart 后 specialization；没有除以 moving defect。

---

# 26. Root-Level Firewall

## Level 0 — Source root

\[
\boxed{Q(x)=0.}
\]

## Level 1 — Structural exact root

\[
\boxed{\Theta=sx.}
\]

与 Level 0 在已证 modular necessities 下严格等价。

## Level 2 — Eliminated / carry-saturated root

R12 的 \(P_B,P_H,P_R,P_{K1}\) 只作为 Level 1 的合法 saturation image 使用。

它们：

- 证明 full root 不属于 carry ideal；
- 不被当作四个独立 physical root equations；
- 不允许 extraneous zero 冒充 source survivor。

---

# 27. Final Statement

85-R2 对问题

\[
\boxed{
\text{“最后一个 Euclidean floor 到底隐藏了多少真实自由度？”}
}
\]

给出的答案是：

\[
\boxed{
\text{在固定 structural fibre 上，几乎没有连续自由度：}
\text{它只剩 finite/eventual-periodic carry。}
}
\]

但：

\[
\boxed{
\text{当 source fibre 自身移动时，carry modulus 也移动；}
\text{不存在当前已证的统一 }O(1)\text{ alphabet。}
}
\]

更重要的是：

\[
\boxed{
\text{即使把 carry 整层完全饱和，exact root 仍留下独立信息。}
}
\]

所以本轮真正完成的不是 “找到另一个 terminal coordinate”，而是：

\[
\boxed{
\textbf{正式退休 Euclidean floor 作为 J2 主 frontier。}
}
\]

下一轮唯一值得攻击的是 source-selected exact residual quantum：

\[
\boxed{
\varepsilon_*\ne0.
}
\]

---

## Artifact Audit

Generated and executed:

```text
85_R2_Quotient_Explicitization_symbolic.py
85_R2_CarrySpectrum.tsv
85_R2_symbolic_execution.log
85_R2_Euclidean_Quotient_and_Floor_Carry_Explicitization.md
```

Execution headline:

```text
SYMBOLIC_HIGH_DIVISION=PASS
SYMBOLIC_REVERSE_DIVISION=PASS
BOUNDARY_DCDC_TOTAL=79
BOUNDARY_CHI_DIV_Q=79/79
BOUNDARY_DISTINCT_EPS_TOTAL=52
```

No J2 closure certificate is generated because:

\[
\boxed{J2\text{ remains OPEN}.}
\]
