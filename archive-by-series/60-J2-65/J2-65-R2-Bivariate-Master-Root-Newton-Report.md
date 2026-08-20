# J2-65-R2 — Pre-Floor Bivariate Master Root × Branch-Independent Saturation × Laurent–Newton Polytope × R12 Exact Chart Recovery

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 65 第二轮 / A1 统一终端线第二十七轮  
**Status:** **J2 OPEN**

---

## 1. Executive verdict

本轮得到的是 **Outcome B — finite chart family over one common Level-1 master root**，而不是单一 Level-2 bivariate polynomial。

核心结论：

\[
\boxed{\text{LEVEL0 universal root quadratic = PROVED}}
\]

\[
\boxed{\text{LEVEL1 branch-independent structural-saturated root = PROVED}}
\]

\[
\boxed{\text{LEVEL2 nonzero }P(G,K;\Theta)\text{ from structural elimination alone = FALSE}}
\]

原因不是计算复杂，而是代数结构本身：在只使用 branch-independent structural relations 时，\(x\) 仍是 full-root coordinate，不是 definitional variable。\(Q_{\rm sat}\) 对 \(x\) 是非零二次式；主理想 \((Q_{\rm sat})\) 与不含 \(x\) 的 coefficient ring 的交为零。因此若不加入 floor graph / deterministic-root graph，就不存在非零的 structural-only elimination polynomial \(P(G,K;\Theta)\)。

然而 Level-1 的 \((G,K)\)-Newton geometry 极其小：

\[
\operatorname{Supp}_{G,K}(Q_{\rm sat})=
\{(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(3,1),(4,1)\},
\]

共 **10** 个格点，凸包只有四个顶点：

\[
\boxed{(1,0),(5,0),(4,1),(0,1)}.
\]

对物理权重

\[
w_\rho(a,b)=a+b\rho,\qquad \rho=k/g,
\]

generic coefficient locus 上只有一条正 \(\rho\)-wall：

\[
\boxed{\rho=1}.
\]

因此在 formal \((G,K)\)-Newton sense 中：

\[
\boxed{\rho<1\;\Longleftrightarrow\;\text{reverse cone}},
\]

\[
\boxed{\rho=1\;\Longleftrightarrow\;K=G\;\Longleftrightarrow\;\text{boundary Newton wall}},
\]

\[
\boxed{\rho>1\;\Longleftrightarrow\;\text{high cone}}.
\]

这是真正的 65-style global compression：high / boundary / reverse 在 pre-floor 层不是三个独立对象，而是同一个四边形 Newton polygon 的两个 cones 与一条 wall。

注意：这里的 coefficients 仍包含 moving \(\Theta\)，尤其 \(x,\alpha,t,d\)。因此这是 **formal monomial fan theorem**；把它升级为实际数值大小的 asymptotic dominance 仍需 coefficient-height / place data。R2 不偷做这一步。

---

## 2. Source/provenance correction：历史 `B` 重名必须拆开

65-R1 的 determinant chart 中：

\[
B_{\rm det}=2G+q.
\]

但 R12 `RootSaturation-full-derivation.py` 中局部代码变量 `B` 实际定义为：

\[
B_{\rm tail}(q)=(q+2)(q^2-4q-4).
\]

两者不是同一对象。

因此本轮 structural ideal 和 variable ledger 强制使用：

- `B_det`：J2 determinant coordinate；
- `B_tail`：R12 tail polynomial。

\[
\boxed{\text{B_SYMBOL_OVERLOAD_CORRECTED=PASS}.}
\]

若把两者误合并，会制造假的 structural relation / elimination；本轮没有这样做。

---

## 3. Branch-independent variable ledger verdict

完整账本见 `J2-65-R2-VariableLedger.tsv`。

本轮真正消去的仅有 definitional variables：

\[
L,u,A,B_{\rm det},B_{\rm tail},c,N,Z,a_3,X,D_2,F,\Omega.
\]

保留：

\[
G,K,q,d,\alpha,t,x
\]

作为 common Level-1 的 monomial/moving coordinates。

进入 chart 后才出现/保留：

\[
e,\gamma,f,w,s,\chi,\chi_R,H,R,\delta.
\]

Primitive gates

\[
\gcd(Z,u)=1,\qquad \gcd(x,u)=1
\]

和 LOW/UP 均 externalize，不进入 \(\mathcal I_{\rm str}\)。

特别地：

\[
\boxed{x\text{ 不被消去。}}
\]

它在 pre-floor 层是 full-root coordinate；只有加入 chart graph 后才 deterministic。

---

## 4. Level 0 — universal exact root from source

R12 source reconstruction使用：

\[
u=\frac{G+1}{q},\qquad A=2u+1,
\]

\[
c=q^3+10q^2+12q+8,
\]

\[
B_{\rm tail}=(q+2)(q^2-4q-4),
\]

\[
N=\frac{B_{\rm tail}t+\alpha G/d}{qc},
\]

\[
Z=\frac{At-2N}{q(q+4)},
\]

\[
a_3=\frac{(G-1)t-qN}{2(q+4)},
\]

\[
X=\frac{Z+uN}{2},
\]

\[
D_2=ua_3+GX,
\]

\[
F=AX^2+ZD_2.
\]

从 R12/R4/GRFC 的 root normalization 重新核验：

\[
\boxed{\Omega=\frac{F}{2K}.}
\]

因此 universal root 是：

\[
\boxed{
\mathcal Q_0
=A\frac{L}{8}x^2-uD_2x+\frac{F}{2K}=0.
}
\]

用

\[
KL=G^2
\]

得到：

\[
\mathcal Q_0
=A\frac{G^2}{8K}x^2-uD_2x+\frac{F}{2K}=0.
\]

只乘 structural Laurent clearing monomial \(8K\)：

\[
\boxed{
Q_{\rm clr}=AG^2x^2-8KuD_2x+4F=0.
}
\tag{L0-CLEAR}
\]

这里没有除以 \(\alpha,t,e,\gamma,x\) 或任何未证非零 moving factor。

---

## 5. Level 1 — structural-saturated pre-floor polynomial

把 §4 中真正 definitional relations 代入 (L0-CLEAR)，得到有理函数，其 exact denominator 是：

\[
\boxed{
D_{\rm str}
=d^2q^5(q+4)^2c^2.
}
\]

在 actual J2 structural locus 上，\(q,d,q+4,c\) 都是已知非零 structural factors，因此可合法 localize / clear。

定义：

\[
\boxed{
Q_{\rm sat}(G,K,x;q,d,\alpha,t)
:=D_{\rm str}\,Q_{\rm clr}.
}
\]

这是真正的 Level-1 polynomial。

Exact degree：

\[
\deg_GQ_{\rm sat}=5,
\qquad
\deg_KQ_{\rm sat}=1,
\qquad
\deg_xQ_{\rm sat}=2.
\]

其 \((G,K)\) support 恰为前述 10 点。

完整 expanded coefficients 与 factorization 在：

`J2-65-R2-NewtonSupport.tsv`。

---

## 6. Saturation ledger

合法 localization factors：

\[
2,\;G,\;K,\;q,\;d,\;q+4,\;c.
\]

明确没有 invert：

\[
\alpha,t,e,\gamma,x.
\]

`J2-65-R2-SaturationLedger.tsv` 对每个 factor 记录 source/status。

因此：

```text
SATURATION_LEDGER_CHECK=PASS
UNPROVED_FACTOR_INVERTED=FALSE
```

---

## 7. 为什么 Level 2 single polynomial 不存在

设 coefficient domain 为：

\[
R_\Theta=\mathbb Z[\Theta][G,K]
\]

经过已证 structural localization 后仍是 integral domain。

现在：

\[
Q_{\rm sat}\in R_\Theta[x],\qquad \deg_xQ_{\rm sat}=2.
\]

若存在非零

\[
h(G,K;\Theta)\in (Q_{\rm sat})\cap R_\Theta,
\]

则

\[
h=Q_{\rm sat}r
\]

对某个 \(r\in R_\Theta[x]\)。由于 domain 中非零多项式的 \(x\)-degree 可加：

\[
\deg_x h=\deg_xQ_{\rm sat}+\deg_xr\ge2,
\]

与 \(h\) 不含 \(x\) 矛盾。

故：

\[
\boxed{(Q_{\rm sat})\cap R_\Theta=0.}
\]

所以：

\[
\boxed{\text{LEVEL2_BIVARIATE_MASTER_POLYNOMIAL=FALSE}.}
\]

这不是“没算出来”，而是 structural-only elimination 的严格零结论。

要得到 nonzero bivariate/univariate chart polynomial，必须加入额外 graph relation：

\[
D_\sigma x-X_\sigma(G,K;\Theta)=0.
\]

因此正确对象是：

\[
\boxed{\text{one Level-1 master root + finite normalization/chart family}.}
\]

---

## 8. Newton polygon

Support：

\[
\begin{aligned}
\operatorname{Supp}_{G,K}(Q_{\rm sat})=
\{&(1,0),(2,0),(3,0),(4,0),(5,0),\\
&(0,1),(1,1),(2,1),(3,1),(4,1)\}.
\end{aligned}
\]

Convex hull：

\[
\boxed{
\operatorname{Newt}(Q_{\rm sat})
=\operatorname{conv}\{(1,0),(5,0),(4,1),(0,1)\}.
}
\]

因此：

```text
MASTER_NEWTON_SUPPORT_SIZE=10
MASTER_NEWTON_VERTEX_COUNT=4
MASTER_NEWTON_EDGE_COUNT=4
```

---

## 9. Physical Archimedean fan

令

\[
G=10^g,\qquad K=10^k,\qquad \rho=k/g.
\]

monomial \(G^aK^b\) 的 formal weight：

\[
w_\rho(a,b)=a+b\rho.
\]

generic support 上：

### Reverse side \(0<\rho<1\)

唯一 top vertex：

\[
\boxed{(5,0)}.
\]

### Boundary \(\rho=1\)

top face：

\[
\boxed{[(5,0),(4,1)]}.
\]

### High side \(1<\rho<2\)

唯一 top vertex：

\[
\boxed{(4,1)}.
\]

因此：

\[
\boxed{\rho=1\text{ 是 genuine Newton wall}.}
\]

而 boundary 的 monomial identity 确实是：

\[
K=G.
\]

所以不是巧合的 degree match。

---

## 10. Exposed coefficients 与 support-degeneration loci

physical fan 在 generic locus 上真正暴露的只有两个 coefficients：

\[
\boxed{
C_{5,0}=2\alpha^2(q+4)^2,
}
\]

\[
\boxed{
C_{4,1}=-4\alpha d q^2x(q+4)^2c.
}
\]

因此在 actual LOW gate 给出 \(x>0\) 后，generic physical support 的共同 degeneration 只有：

\[
\boxed{\alpha=0.}
\]

在 boundary wall \(K=G\) 上，两项 top-face coefficient 合并为：

\[
\boxed{
C_{\rm wall}
=2\alpha(q+4)^2\bigl(\alpha-2dq^2cx\bigr).
}
\]

所以首阶 boundary cancellation locus 是有限的两个代数条件：

\[
\boxed{\alpha=0}
\]

或

\[
\boxed{\alpha=2dq^2cx.}
\]

没有产生新的 residual variable。

### \(\alpha=0\) support degeneration

直接 exact substitute \(\alpha=0\) 后 support 缩成：

\[
\{(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1)\}.
\]

其物理 \(\rho>0\) top vertex 变成：

\[
\boxed{(3,1)}
\]

且 coefficient 为：

\[
\begin{aligned}
C^{(\alpha=0)}_{3,1}={}&-8d^2q^2tx(q+2)(q+4)c\\
&\times(q^3+5q^2-4q-4).
\end{aligned}
\]

对 actual \(t\neq0,x>0\) 和 legal positive q，这给一个显式 coefficient-degeneracy component，而不是新的 coefficient ladder。

因此 R3 的三 place 分析只需处理：

1. generic exposed pair \((5,0),(4,1)\)；
2. \(\alpha=0\) degeneration component；
3. boundary face cancellation \(\alpha=2dq^2cx\)。

---

## 11. Boundary chart exact recovery

Boundary：

\[
L=G,\qquad K=G.
\]

Level-1 support 在 substitution \(K=G\) 下按 affine map：

\[
(a,b)\mapsto a+b
\]

投影到 powers：

\[
\{1,2,3,4,5\}.
\]

R12 source floor graph 与 carry normalization 加入后，出现一个 structural \(G\)-factor；去除后得到 degree 4 primitive polynomial。

本轮 current-run source reconstruction 后的 exact hash：

```text
92af2937c40fdf2dc056472228ec1a91d7b01444dd26f6f6718e68b261a35648
```

与 R12 frozen hash 完全一致。

```text
BOUNDARY_CHART_RECOVERY=EXACT
P_B_HASH_MATCH=PASS
```

所以 \(P_B\) 与 master 的关系不是“凭 degree 猜测”：它是 boundary wall restriction +真实 floor/carry graph + structural \(G\)-factor removal 的 exact chart。

---

## 12. High chart exact recovery

High 使用：

\[
K=HG,
\qquad H=10^\delta,
\qquad s=0.
\]

formal \(\rho>1\) 落在 master polygon 的 high normal cone。

加入真实 high floor graph 与 R8 carry normalization 后，去除 structural \(G\)-factor，得到 degree 4：

```text
cf7b8ef58e9e24e8a63daf29d5d78ea5184bf19052a525563c5cb0ff80f5e180
```

exact match：

```text
HIGH_CHART_RECOVERY=EXACT
P_H_HASH_MATCH=PASS
```

因此 \(P_B\neq P_H\) 的来源不是不同的 Level-1 Newton polygon；其差异来自：

- monomial specialization \(K=G\) vs. \(K=HG\)；
- high 的 \(s=0\) floor graph；
- chart-specific moving-coefficient/carry substitution。

不是一条新的 full-root equality。

---

## 13. Generic reverse exact recovery and degree 4→7 explanation

Reverse：

\[
G=KR.
\]

若只对 Level-1 Newton support 做 fixed-\(K\) projection：

\[
(a,b)\mapsto a,
\]

只能得到 powers：

\[
0,1,2,3,4,5.
\]

因此：

\[
\boxed{\deg_R7\text{ 绝不是 Level-1 polygon 的简单 projection}.}
\]

R12 source route还加入：

- reverse reconstruction \(d=2fR\)；
- reverse floor graph；
- generic carry normalization；
- rational clearing。

source-heavy derivation得到 raw reverse numerator 的最低 \(R\)-power 恰为：

\[
\boxed{R^2}.
\]

除去该已记录 structural monomial 后，primitive polynomial degree 为 7。

exact hash：

```text
9b67233170bf9203917a84ec309989dbe2d87351c0210342af6912dc3455a0b3
```

```text
REVERSE_CHART_RECOVERY=EXACT
P_R_HASH_MATCH=PASS
```

因此 degree 7 的来源是 **reverse chart reconstruction / denominator clearing / carry saturation 的组合**，不是 master polygon 自己突然多出两个 G/K lattice directions。

---

## 14. k=1,b=0 special normalization and first noncommutation

Generic reverse source relation：

\[
\Gamma_R=\frac{K}{4f^2w}\gamma.
\]

但在 special \(k=1,b=0\) 中，R12 source 明确禁止机械使用该 normalizer；合法关系是：

\[
\boxed{K=10,\quad f=1,\quad G=10R,\quad \Gamma_R=\gamma.}
\]

从 common source root 重新走 special normalization，得到：

```text
d950fb494bfb4b4e4bcae5a4054f64041170856bfc2ecc78dc8aae9ea393afd2
```

```text
K1_SPECIAL_CHART_RECOVERY=EXACT
P_K1_HASH_MATCH=PASS
```

同时 compact exact audit 验证：

```text
FORMAL_GENERIC_K10_EQUALS_SPECIAL=FALSE
```

所以 commutation verdict 必须分层写：

\[
\boxed{\text{branch-independent structural saturation commutes}}
\]

但：

\[
\boxed{\text{full carry-saturation/chart specialization only PARTIAL}.}
\]

最早明确 noncommuting object：

\[
\boxed{K/(4f^2w)\text{ generic reverse carry normalizer}.}
\]

这就是 R12 为什么需要独立 \(P_{K1}\) 的结构解释。

---

## 15. Chart support comparison

Exact supports：

\[
\operatorname{Supp}(P_B)=\operatorname{Supp}(P_H)=\{0,1,2,3,4\},
\]

\[
\operatorname{Supp}(P_R)=\operatorname{Supp}(P_{K1})=\{0,1,2,3,4,5,6,7\}.
\]

所以 \(P_{K1}\) 与 \(P_R\) 的差异：

\[
\boxed{\text{发生在 coefficients / normalization，不发生在 univariate support set}.}
\]

---

## 16. N1–N4 direct answers

### N1 — \(\mathcal N_B\) 是否是 master 的 projected face？

**严格说不是“单个 exposed face 的投影”**。Boundary 是 \(\rho=1\) wall；把**整个 Level-1 support**按 \((a,b)\mapsto a+b\) 投影得到 powers \(1\ldots5\)，再经 floor/carry specialization 与 structural \(G\)-factor removal 得 \(P_B\) 的 \(0\ldots4\)。

因此：

\[
\boxed{\text{wall restriction + support projection + chart saturation}.}
\]

### N2 — High 是否 master 的另一个 exposed cone？

**YES，在 formal \((G,K)\)-Newton fan 中。** \(\rho>1\) 的 top vertex 是 \((4,1)\)。但完整 \(P_H\) 不是只取这个 vertex；它仍是 full chart polynomial。

### N3 — Reverse degree 7 是否只是 affine projection？

**NO。** Level-1 fixed-K projection最多到 degree 5；degree 7 来自 reverse reconstruction/floor/carry/clearing，随后还去除 raw \(R^2\) structural factor。

### N4 — \(P_{K1}\) 的区别在 support 还是 coefficients？

\[
\boxed{\text{coefficients / normalization}.}
\]

两者 univariate support 都是 \(0\ldots7\)。

---

## 17. Deficiency wedge cannot be recovered from this fan alone

旧 deficiency work 的 quantitative inequalities 包括 slope-3、后续 \(17/7\)、fixed-q slope-1 等。它们使用了：

- LOW / actual digit-root lower bound；
- complementary root-factor decimal core；
- radial upper bounds；
- positivity / digit width；
- outer \(q\)-suppression；
- tail divisibility。

而本轮 Level-1 Newton fan 的唯一 generic positive wall是：

\[
\rho=1.
\]

例如 \(g\le3\ell\) 写成 \(\ell=2g-k\) 后等价于一个不同的 slope constraint，并不对应 \(\rho=1\) 的新 face wall。

所以：

```text
OLD_DEFICIENCY_WEDGE_FROM_NEWTON=FALSE
```

但 Newton fan **统一解释了 qualitative chamber split**：

\[
K<G,\quad K=G,\quad K>G.
\]

换言之，旧 wedge 的“方向坐标”来自 Newton geometry，数值压缩强度则来自外部 non-polynomial gates。

---

## 18. q=1 algebraic test

把 \(q=1\) 代入 Level-1 structural denominator：

\[
D_{\rm str}=25\cdot31^2\,d^2\neq0
\]

在合法正 \(d\) structural locus 上无 degeneration。

因此：

```text
Q1_MASTER_DEGENERATION=NONE
```

本轮没有进入 q=1 Pell/norm orbit 或 Gaussian closure。

---

## 19. Place metadata — only preparation, no bit ladder

`J2-65-R2-PlaceMetadata.tsv` 已记录每个 support coefficient 的 symbolic \(v_2/v_5\) metadata。

对下一轮最关键的 exposed pair：

\[
C_{5,0}=2\alpha^2(q+4)^2,
\]

所以在 q odd 时：

\[
v_2(C_{5,0})=1+2v_2(\alpha),
\]

\[
v_5(C_{5,0})=2v_5(\alpha)+2v_5(q+4).
\]

以及：

\[
C_{4,1}=-4\alpha d q^2x(q+4)^2c,
\]

其 valuations 保留为 moving expressions。

本轮没有做：

\[
4\mid e\to8\mid e\to16\mid e
\]

之类 descent。

---

## 20. Q1–Q8 final answers

### Q1 — 四个 R12 root polynomials 是什么？

\[
\boxed{\textbf{FINITE MASTER CHART FAMILY over one common Level-1 root}.}
\]

不是单一 Level-2 \(P(G,K)\)。Boundary/high/generic reverse 都来自 common pre-floor object；K1 还暴露了 carry normalization 的特殊 noncommutation。

### Q2 — Branch split 最早严格发生在哪一步？

在 common Level-1 之后的 **monomial/floor graph specialization** 开始；最早可明确证明“generic route 与 special route 不 commute”的地方是：

\[
\boxed{\text{reverse carry normalizer }K/(4f^2w)\text{ at }k=1,b=0.}
\]

### Q3 — 是否存在 branch-independent \(Q_{\rm sat}(G,K,x;\Theta)=0\)？

\[
\boxed{\textbf{YES — PROVED}.}
\]

### Q4 — 是否进一步存在 structural-only nonzero \(P(G,K;\Theta)=0\)？

\[
\boxed{\textbf{NO — FALSE}.}
\]

其 elimination ideal 是零；必须加入 floor/root graph 才能产生 nonzero chart polynomial。

### Q5 — Boundary \(K=G\) 是否 genuine Newton wall？

\[
\boxed{\textbf{YES on the generic support locus}.}
\]

wall 是 \(\rho=1\)，top face \((5,0)-(4,1)\)。\(\alpha=0\) 是显式 support-degeneration locus，已单独记录。

### Q6 — High / reverse 是否 Newton fan 不同 cones？

\[
\boxed{\textbf{YES in formal }(G,K)\textbf{ Newton geometry}.}
\]

High: \(\rho>1\)；reverse: \(\rho<1\)。但 reverse degree 7 不是 simple projection。

### Q7 — 旧 deficiency wedge 能否从 fan 单独重获？

\[
\boxed{\textbf{NO}.}
\]

只能重获 qualitative split；quantitative wedge 需要 LOW/root-factor/radial/positivity/digit/tail ingredients。

### Q8 — 进入 2/5-adic geometry 前真正需保留多少 exposed coefficients？

对物理 \(0<\rho<2\) generic fan：

\[
\boxed{\textbf{2}.}
\]

即：

\[
\boxed{C_{5,0},\;C_{4,1}.}
\]

完整 polygon boundary 上有 10 个 support terms，但只有这两个会控制 generic physical top-face competition。另保留一个 \(\alpha=0\) support-degeneration component；这不是新增 coefficient ladder。

---

## 21. Regression / execution transparency

四个历史 hashes 均 exact match：

```text
P_B_HASH_MATCH=PASS
P_H_HASH_MATCH=PASS
P_R_HASH_MATCH=PASS
P_K1_HASH_MATCH=PASS
```

本轮先执行了 source-direction reconstruction；在将完整 heavy chart derivation 打包成独立脚本重放时，一次 self-contained heavy replay 超过 120s execution cap。该事实不隐藏。最终 `J2-65-R2-ChartRecovery.py` 保存的是本轮 source-derived exact factors 的 **compact exact replay**，用于快速验证 expressions / supports / hashes / K1 mismatch；common-source derivation本身由 `MasterRoot-symbolic.py`、本报告公式链和历史 R12 from-source derivation共同审计。

`J2-65-R2-execution.log` 记录最终可执行 certificates，并附 heavy-replay timeout note。

---

## 22. New global theorem

### PREFLOOR NEWTON-FAN TRICHOTOMY

在 actual J2 structural chart、保留 moving coefficients、只消去 branch-independent definitional variables后，full exact root具有统一 Level-1 polynomial \(Q_{\rm sat}\)，其 generic \((G,K)\)-Newton polygon为：

\[
\operatorname{conv}\{(1,0),(5,0),(4,1),(0,1)\}.
\]

在物理 \(0<\rho=k/g<2\) 中：

\[
\rho<1\Rightarrow(5,0)\text{ exposed},
\]

\[
\rho=1\Rightarrow[(5,0),(4,1)]\text{ exposed},
\]

\[
\rho>1\Rightarrow(4,1)\text{ exposed}.
\]

唯一 first support-degeneration locus 是 \(\alpha=0\)；boundary first-face cancellation 进一步由：

\[
\alpha=2dq^2cx
\]

控制。

这把 high / boundary / reverse 从三套局部 polynomial 重新压成：

\[
\boxed{
\text{one Level-1 Newton polygon}
+
\text{finite coefficient-degeneracy loci}
+
\text{finite normalization chart family}.
}
\]

---

## 23. Next unique object

J2 仍未闭合：

\[
\boxed{\textbf{J2 OPEN}.}
\]

但 frontier 不再是“moving coefficients difficult”。

下一轮唯一自然对象是：

\[
\boxed{
(\infty,2,5)\textbf{ Three-Place Tropical Collision}
}
\]

具体只需在：

1. generic exposed pair \((5,0),(4,1)\)；
2. \(\alpha=0\) support-degeneration component；
3. boundary face-cancellation locus \(\alpha=2dq^2cx\)；

上同步比较：

- Archimedean top-face tie；
- 2-adic minimum-valuation tie；
- 5-adic minimum-valuation tie。

不得退回 coefficient-bit ladder。

---

## 24. Artifact index

本轮生成：

- `J2-65-R2-Bivariate-Master-Root-Newton-Report.md`
- `J2-65-R2-MasterRoot-symbolic.py`
- `J2-65-R2-Saturation.py`
- `J2-65-R2-NewtonPolytope.py`
- `J2-65-R2-ChartRecovery.py`
- `J2-65-R2-VariableLedger.tsv`
- `J2-65-R2-SaturationLedger.tsv`
- `J2-65-R2-NewtonSupport.tsv`
- `J2-65-R2-ArchimedeanFan.tsv`
- `J2-65-R2-PlaceMetadata.tsv`
- `J2-65-R2-ChartRegression.tsv`
- `J2-65-R2-certificate.txt`
- `J2-65-R2-execution.log`
- `J2-65-R2-MasterFamily.tsv`
- `J2-65-R2-Level1MasterRoot.txt`

没有生成 `J2-65-R2-MasterPolynomial.txt`，因为 Level-2 single polynomial 已严格判为 FALSE。
