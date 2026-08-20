# J2-65-R4 Additive-Bracket Cancellation Complex Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 65 第四轮 / A1 统一终端线第二十九轮  
**Status:** **J2 OPEN**  
**Main object:** Factor-Aware Additive-Bracket Cancellation Complex × primitive projective pair \([\alpha:dt]\) × pairwise determinant-GCD × simultaneous \((2/5)\)-adic depth × three-place cell algebraization.

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}.}
\]

R4 确实解决了 R3 留下的那句

> additive bracket cancellation depth remains uncontrolled

但解决方式不是把所有 cancellation depth 逐 bit 算完，而是把它们统一提升为一个有限的 **adelic algebraic cancellation complex**。

本轮得到的核心压缩为：

\[
\boxed{
10\text{ grouped coefficients}
\longrightarrow
7\text{ primitive additive brackets}
}
\]

其中

\[
\boxed{5\text{ 个 projective linear brackets}+2\text{ 个 homogeneous quadratic conics}.}
\]

五个线性 generator 全部写成

\[
B_i=U_i(q)\alpha+V_i(q)T,
\qquad T:=dt,
\]

且 source 证明 \(t\) 为奇数，所以

\[
\boxed{T\ne0.}
\]

令

\[
h=\gcd(\alpha,T),\qquad \alpha=hA_0,\qquad T=hT_0,
\qquad \gcd(A_0,T_0)=1,
\]

则

\[
B_i=hL_i,
\qquad
L_i=U_i(q)A_0+V_i(q)T_0.
\]

对任意两条线性 bracket，定义

\[
\Delta_{ij}(q)=U_iV_j-U_jV_i.
\]

本轮严格证明

\[
\boxed{
\gcd(L_i,L_j)\mid\Delta_{ij}(q).
}
\tag{DET-GCD}
\]

五条线产生的 10 个 pair determinant **全部非零**，没有隐藏 proportional generator。它们总共有 16 个 raw irreducible polynomial factors，但在 live \((2,5)\)-primary geometry 中只有

\[
\boxed{8\text{ 个 determinant-kernel factors}}
\]

真正可能控制额外深度，其中 7 个给出无界但有限类型的 Hensel/structural root tubes；剩余一个

\[
q^2+6q+4
\]

在 live \(q\equiv2\pmod5\) branch 上满足精确公式

\[
\boxed{v_5(q^2+6q+4)=1,}
\]

所以并不产生无限 residue ladder。

R3 的 27 个 cells 已全部 lift 到 coefficient/bracket level。严格按本轮定义的 cell equivalence（必须同时保留 Arch face、p2 pattern、p5 pattern），仍有

\[
\boxed{27\text{ strict classes}.}
\]

这不是失败：它们的 bracket compatibility 数据已经因子化为

\[
\boxed{
3\text{ Arch escape faces}
\times
9\text{ bracket-pattern fibres}.
}
\]

当前无法合法宣称任何 raw R3 meta-cell 被 determinant 直接关闭，因为 R3 的 row-min cell 只说明某一 row 必须发生内部 cancellation，并不指定究竟是哪两个 coefficients、也不自动给一个固定 bracket pair 的正深度下界。于是 determinant theorem 关闭的是 **refined C3 subcells**，而不是在未 refinement 前整块 row-order cell。

因此，本轮最终 survivor 不再是“27 个 raw cells + uncontrolled unit cancellation”，而是

\[
\boxed{
\begin{array}{c}
3\text{ Arch faces}\times9\text{ bracket-pattern fibres}\[1mm]
\text{over}\quad
5\text{ projective lines}+2\text{ conics}\[1mm]
\text{controlled by an }8\text{-factor }(2/5)\text{-determinant kernel}.
\end{array}
}
\]

这就是 R4 的 finite adelic algebraic cancellation complex。

---

# Part II — Source Regression and Frozen R3 Interface

R4 重新从 R2 common master definitions 构造：

\[
u=\frac{G+1}{q},\qquad A=2u+1,
\]

\[
c=q^3+10q^2+12q+8,
\qquad
B_{\rm tail}=(q+2)(q^2-4q-4),
\]

\[
N=\frac{B_{\rm tail}t+\alpha G/d}{qc},
\quad
Z=\frac{At-2N}{q(q+4)},
\]

\[
a_3=\frac{(G-1)t-qN}{2(q+4)},
\quad
X=\frac{Z+uN}{2},
\quad
D_2=ua_3+GX,
\]

\[
F=AX^2+ZD_2,
\]

\[
Q_{\rm clr}=AG^2x^2-8KuD_2x+4F.
\]

exact structural denominator：

\[
D_{\rm str}=d^2q^5(q+4)^2c^2,
\qquad
Q_{\rm sat}=D_{\rm str}Q_{\rm clr}.
\]

重新构造所得 master numerator SHA-256：

```text
8892befa7c4d420b20cd73dfc06cb6ebd52a1a093ea90ca421a52166b29fc2dc
```

10-point grouped support 回归为

\[
\{(1,0),(2,0),(3,0),(4,0),(5,0),
(0,1),(1,1),(2,1),(3,1),(4,1)\}.
\]

冻结 R3：

\[
q>1\Longrightarrow\alpha\ne0,
\]

\[
\left|\frac{T_{50}}{-T_{41}}\right|
<\frac{75}{2K^2}\le\frac38,
\]

\[
Q_{\rm sat}=0\Longrightarrow\Delta_{\rm arch}\le\frac6g,
\]

Arch escape faces：

\[
\sigma=0,\qquad \sigma=1,\qquad\Delta_\alpha=0,
\]

以及

\[
T_2=2v_2(d)+k+3+v_2(x),
\]

\[
T_5=2v_5(d)+2b_5+2c_5+k+v_5(x).
\]

R4 不重新打开 \(\alpha=0\)、boundary top-face cancellation、support degeneration，也未使用 bit ladder。

---

# Part III — Exact Grouped-Coefficient Factorization

10 个 grouped coefficients 中：

- 3 个只有 monomial/product structure；
- 7 个含真正 additive factor；
- 这 7 个 additive generators 无重复、无 projectively proportional pair。

monomial/product-only coefficients 是：

\[
C_{50}=2\alpha^2(q+4)^2,
\]

\[
C_{01}=8d^2q^5tx(q+4)^2c,
\]

\[
C_{41}=-4\alpha dq^2x(q+4)^2c.
\]

五个 Type-L generator 为：

## B10

\[
B_{10}=c\alpha+V_{10}T,
\]

\[
V_{10}=3q^6+36q^5+156q^4+352q^3+240q^2-64q-64.
\]

且

\[
C_{10}=2dq^2t(q+4)B_{10}.
\]

## B40

\[
B_{40}=(q^2+6q+16)\alpha
+8(q+2)(q^3+5q^2-4q-4)T.
\]

## B11

\[
\boxed{
B_{11}=\alpha+(q^3-6q^2-28q-8)T.
}
\]

## B21

\[
B_{21}=(2-q)\alpha
+(q+2)(3q-2)(q^2+8q+4)T.
\]

## B31

\[
B_{31}=(q+6)\alpha
+2(q+2)(q^3+5q^2-4q-4)T.
\]

另外两个 additive generators 是 Type H：

\[
\boxed{H_{20}(q,\alpha,T,Y),\qquad H_{30}(q,\alpha,T,Y),}
\qquad Y:=dx.
\]

它们都是 \((\alpha,T,Y)\) 的 homogeneous quadratic forms；generic SymPy exact factorization 下保持 irreducible，不能合法强行写成 \(U\alpha+VT\)。完整表达式见 `J2-65-R4-BracketCatalog.tsv`。

因此第一压缩指标为：

```text
GROUPED_COEFFICIENT_COUNT=10
PRIMITIVE_BRACKET_GENERATOR_COUNT=7
LINEAR_PROJECTIVE_BRACKET_COUNT=5
HIGHER_BRACKET_COUNT=2
```

---

# Part IV — Primitive Projectivization

旧 source 给出 \(t\) 奇数，因此

\[
\boxed{T=dt\ne0.}
\]

没有恢复到任何旧 theorem 可以合法推出

\[
\gcd(\alpha,dt)=1.
\]

因此本轮不猜 \(h=1\)，而只写

\[
h=\gcd(\alpha,T),
\quad
\alpha=hA_0,
\quad
T=hT_0,
\quad
\gcd(A_0,T_0)=1.
\]

由 \(v_2(t)=0\)：

\[
v_2(h)=\min(v_2(\alpha),v_2(d)).
\]

同时

\[
v_5(h)=\min(v_5(\alpha),v_5(d)+v_5(t)).
\]

五个 linear brackets 全部化为

\[
B_i=hL_i,
\qquad
L_i=U_i(q)A_0+V_i(q)T_0.
\]

因此真正的 extra unit cancellation depth 被剥离成 \(v_p(L_i)\)，没有把 common content \(h\) 混进 projective cancellation。

---

# Part V — Pairwise Determinant-GCD Theorem

对

\[
L_i=U_iA_0+V_iT_0,
\qquad
L_j=U_jA_0+V_jT_0,
\]

定义

\[
\Delta_{ij}=U_iV_j-U_jV_i.
\]

exact identities：

\[
V_jL_i-V_iL_j=\Delta_{ij}A_0,
\]

\[
U_iL_j-U_jL_i=\Delta_{ij}T_0.
\]

令 \(g_{ij}=\gcd(L_i,L_j)\)。则

\[
g_{ij}\mid \Delta_{ij}A_0,
\qquad
g_{ij}\mid \Delta_{ij}T_0.
\]

因为 \(\gcd(A_0,T_0)=1\)，存在整数 \(r,s\) 使

\[
rA_0+sT_0=1.
\]

故

\[
g_{ij}\mid \Delta_{ij}.
\]

于是得到本轮主 theorem：

\[
\boxed{
\gcd(L_i,L_j)\mid\Delta_{ij}(q).
}
\tag{R4-DET-GCD}
\]

因此如果同一 refined survivor 要求

\[
v_p(L_i)\ge r,
\qquad
v_p(L_j)\ge s,
\]

则必有

\[
\boxed{
v_p(\Delta_{ij}(q))\ge\min(r,s).
}
\]

这把未知的 two-bracket unit cancellation depth 统一转换成 one-variable determinant polynomial 的 local geometry。

---

# Part VI — All Ten Determinants

五个 linear generators 给出 10 个非零 determinants：

\[
\Delta_{10,40}=-(q+4)D_1,
\]

\[
D_1=3q^7+34q^6+148q^5+568q^4+1456q^3+1184q^2+64q-128;
\]

\[
\Delta_{10,11}=-2q(q+4)D_2,
\]

\[
D_2=q^4+12q^3+68q^2+80q+32;
\]

\[
\Delta_{10,21}
=2q(q+4)(3q+2)(q^2+4q-4)(q^2+6q+4);
\]

\[
\Delta_{10,31}=-(q+4)D_4,
\]

\[
D_4=q^6+16q^5+132q^4+480q^3+432q^2-64;
\]

\[
\Delta_{40,11}=(q+4)D_5,
\]

\[
D_5=q^4-12q^3-56q^2-96q-16;
\]

\[
\Delta_{40,21}=(q+2)^2(q+4)D_6,
\]

\[
D_6=3q^3+30q^2-4q-8;
\]

\[
\Delta_{40,31}
=2(q-2)(q+2)(q+4)D_7,
\]

\[
D_7=q^3+5q^2-4q-4;
\]

\[
\Delta_{11,21}=4q(q+4)D_8,
\]

\[
D_8=q^2+q+2;
\]

\[
\Delta_{11,31}=(q+4)D_9,
\]

\[
D_9=q^3+10q^2+36q+8;
\]

\[
\Delta_{21,31}=-(q+2)(q+4)D_{10},
\]

\[
D_{10}=5q^3+26q^2-4q-8.
\]

全部 10 determinants 非零，所以

```text
LINEAR_PAIR_PROPORTIONALITY=NONE
NONZERO_DETERMINANT_COUNT=10
```

raw distinct irreducible polynomial factors 共 16 个；真正 live 的 \((2,5)\)-primary determinant support kernel 可压到：

\[
\boxed{
\mathcal D_{\min}=\{
q+4,
D_7,
D_8,
3q+2,
q^2+6q+4,
D_4,
q-2,
D_9
\}.
}
\]

因此

\[
\boxed{\texttt{DETERMINANT\_KERNEL\_SIZE}=8.}
\]

---

# Part VII — Complete 2-Adic Determinant Tubes

因为 \(q\) 是 ten-unit，所以 \(q\) 为奇数。

除 \(D_7,D_8\) 外，所有 determinant factors 在 \(\mathbb Z_2^\times\) 上都是 2-units。

\(D_7,D_8\) 各自在 mod 2 有唯一 simple unit root \(1\)，因此 Hensel 唯一提升到

\[
\rho_{D7},\rho_{D8}\in\mathbb Z_2^\times.
\]

对应 tube 中：

\[
\boxed{v_2(D_7(q))=v_2(q-\rho_{D7}),}
\]

\[
\boxed{v_2(D_8(q))=v_2(q-\rho_{D8}).}
\]

因此 10 pair determinants 的 2-adic depth 精确压成：

\[
\begin{array}{c|c}
\text{pair}&v_2(\Delta_{ij})\\ \hline
10,40&0\\
10,11&1\\
10,21&1\\
10,31&0\\
40,11&0\\
40,21&0\\
40,31&1+v_2(D_7(q))\\
11,21&2+v_2(D_8(q))\\
11,31&0\\
21,31&0
\end{array}
\]

于是 \(\mathcal G_2\) 只有 4 条可能含 2 的边，其中只有两条具有 unbounded extra depth。

没有 mod \(2^n\) ladder。

---

# Part VIII — Complete 5-Adic Determinant Tubes

沿 R3 structural live classification：

\[
b_5>0\Longrightarrow q\equiv1\pmod5,
\quad c_5=0,
\]

而

\[
b_5=0,\ c_5\ge1
\Longrightarrow q\equiv2\text{ or }4\pmod5.
\]

保留旧 tube：

\[
\boxed{v_5(q+4)=b_5.}
\]

它不重新命名。

其余 live exceptional factors：

### \(3q+2\)

在 \(q\equiv1\pmod5\) 有 simple root，故

\[
v_5(3q+2)=v_5(q-\rho_{3q+2}),
\quad \rho_{3q+2}=-2/3\in\mathbb Z_5.
\]

### \(q^2+6q+4\)

mod 5 在 \(q\equiv2\) 有 double residue root，但没有 \(\mathbb Z_5\) root。精确写

\[
q=2+5z
\]

得

\[
q^2+6q+4
=5(4+10z+5z^2),
\]

括号为 5-unit，因此

\[
\boxed{v_5(q^2+6q+4)=1.}
\]

这直接阻止该 factor 形成无限 bit/depth ladder。

### \(D_4\)

在 live \(q\equiv4\pmod5\) 有一个 simple Hensel tube。

### \(q-2\)

就是 live \(q\equiv2\pmod5\) exact tube。

### \(D_9\)

在 live \(q\equiv1\pmod5\) 有一个 simple Hensel tube。

因此 raw \(q\equiv1\) graph 因旧 \(q+4\) factor而完全图化；quotient 掉已存在的 \(b_5\) structural depth 后，只有 4 条 pair edges 还携带额外 5-adic depth。

所有 5-adic unbounded depth 都由有限 simple-root tubes / existing structural tube 描述。

---

# Part IX — Tail Reexpression Dependency Audit

对每个 linear bracket，代入

\[
\alpha=d\frac{qcN-B_{\rm tail}t}{G}
\]

可统一写成

\[
\boxed{
B_i=\frac dG
\left[
U_i(q)qcN+igl(V_i(q)G-U_i(q)B_{\rm tail}\bigr)t
\right].
}
\tag{TAIL-REEXP}
\]

因此五个 linear brackets 都可在 old tail coordinates 中 reexpress，但这不等于它们是旧 tail identity 的 multiples。

逐项 exact dependency check 表明：

```text
BRACKETS_RETIRED_AS_OLD_SHADOWS=0
LINEAR_BRACKETS_NEW_EXACT_COMBINATIONS=5
HIGHER_BRACKETS_NEW=2
```

尤其没有把

\[
\alpha\equiv-8dt\pmod q
\]

错误提升为 equality。

为了检测是否只是 DTF mismatch

\[
-\alpha+cT,
\]

计算 projective determinant \(U_ic+V_i\)，五个均非零：

\[
U_{10}c+V_{10}
=4q(q+2)^2(q+4)(q^2+6q+2),
\]

\[
U_{40}c+V_{40}
=(q+4)(q^4+20q^3+64q^2+32q+16),
\]

\[
U_{11}c+V_{11}=2q(q-2)(q+4),
\]

\[
U_{21}c+V_{21}=2q^2(q+4)(q+6),
\]

\[
U_{31}c+V_{31}=(q+4)(3q^3+18q^2+12q+8).
\]

故它们不是 DTF1 的比例重写。

---

# Part X — A New Real Projective Retirement: B21=0 Is Impossible

DTF1 给

\[
G(dct-\alpha)=2d(q+4)(ca_3+q^2t)>0.
\]

因为 \(T=dt>0\)，故 real projective ratio

\[
y:=\frac\alpha T
\]

满足

\[
\boxed{y<c.}
\tag{REAL-HALFSPACE}
\]

而 \(B_{21}=0\) 要求

\[
y=\frac{V_{21}}{q-2}.
\]

直接 exact subtraction：

\[
V_{21}-(q-2)c
=2q^2(q+4)(q+6)>0.
\]

所以

\[
\frac{V_{21}}{q-2}>c.
\]

与 \(y<c\) 矛盾。

于是：

\[
\boxed{B_{21}=0\Longrightarrow\varnothing.}
\tag{B21-ZERO-DEAD}
\]

注意这只关闭 **exact zero locus**。它不允许写成“B21 的深 2-adic tube 与深 5-adic tube互相矛盾”，因为 CRT 本身仍可兼容两个 local neighborhoods。

---

# Part XI — Higher-Degree Bracket Resultant Complex

两个 Type H conics 真正参与 G-row internal cancellation，所以不能丢弃。

本轮只对 live 7-generator complex做有限 elimination：

- \(H_{20}\) 与 5 个 linear brackets各做一次 exact line-conic elimination；
- \(H_{30}\) 与 5 个 linear brackets各做一次；
- \(H_{20},H_{30}\) 再做一次 pair resultant。

总计：

\[
\boxed{11\text{ exact higher-bracket resultants}.}
\]

没有对 141 monomials 做无目的巨大 resultant，也没有对 equivalent full-root shadows做 fake resultant。

```text
HIGHER_BRACKET_RESULTANTS_NOT_NEEDED=FALSE
HIGHER_BRACKET_RESULTANT_COUNT=11
FAKE_EQUIVALENT_RESULTANT_USED=FALSE
```

---

# Part XII — Lift of the 27 R3 Three-Place Cells

每个 place 的 row type仍严格分为：

1. `K_LT_G`：K-row minimum strictly lower，故 K-row内部必须至少双 minimum；
2. `K_EQ_G`：cross-row minimum天然 tie；
3. `G_LT_K`：G-row minimum strictly lower，故 G-row内部必须至少双 minimum。

对应 mechanism：

- `K_EQ_G` 是 **C1 — Cross-row tie**；
- internal rows 仍是 **C2 internal monomial tie OR C3 genuine bracket lift** 的 exact disjunction；
- R3 的 coarse row-order information本身不决定究竟 C2 还是 C3。

这点决定了为什么不能把 determinant theorem夸大成 “27→0”。

27-cell regression：

```text
R3_META_CELL_REGRESSION=PASS
R3_META_CELL_COUNT=27
```

计数：

- p2,p5 都是 cross-row 的 cells：3；
- 至少一个 place 是 cross-row：15；
- 至少一个 place 是 internal：24。

严格按用户定义：两个 cells 只有在 Arch face、p2 bracket condition、p5 bracket condition、determinant support、depth pattern 全同才等价。因此：

\[
\boxed{R4\_BRACKET\_EQUIVALENCE\_CLASSES=27\_STRICT.}
\]

但是如果只看 bracket compatibility pattern 而把 Arch face作为外部 base，则只有

\[
\boxed{9\text{ bracket-pattern fibres}.}
\]

所以真正的结构是

\[
\boxed{
27=3\text{ Arch faces}\times9\text{ bracket fibres}.
}
\]

这比把 27 复制成 27 套 bracket theory 更整体。

---

# Part XIII — Bracket Depth Requirements

对每个 potential C3 refinement，定义 required lower bound

\[
v_p(L_i)\ge\Lambda_{i,p}.
\]

这只是 inequality metadata，不是 residual variable。

对 linear generators得到：

## p=2

\[
\Lambda_{10,2}
=\max\{0,\ v_2(d)+k+2+v_2(x)-g-v_2(h)\},
\]

\[
\Lambda_{40,2}
=\max\{0,\ 2v_2(d)+k+3+v_2(x)-4g-v_2(\alpha)-v_2(h)\},
\]

以及

\[
\Lambda_{11,2}
=\Lambda_{21,2}
=\Lambda_{31,2}
=\max\{0,\ v_2(d)+1-g-v_2(h)\}.
\]

## p=5

\[
\Lambda_{10,5}
=\max\{0,\ v_5(d)+b_5+2c_5+k+v_5(x)-g-v_5(t)-v_5(h)\},
\]

\[
\Lambda_{40,5}
=\max\{0,\ 2v_5(d)+b_5+2c_5+k+v_5(x)-4g-v_5(\alpha)-v_5(h)\},
\]

以及

\[
\Lambda_{11,5}
=\Lambda_{21,5}
=\Lambda_{31,5}
=\max\{0,\ v_5(d)+b_5+c_5-g-v_5(h)\}.
\]

Type H 不伪造 scalar bracket depth formula，而是保留 conic valuation/resultant interface。

若 refined C3 subcell 同时要求 \(L_i,L_j\) 深，则直接与

\[
v_p(\Delta_{ij})
\]

比较；这正是 determinant extinction 的合法触发条件。

---

# Part XIV — Why No Raw Cell Dies Yet by Determinant-GCD

本轮得到：

```text
CELLS_CLOSED_BY_DETERMINANT_GCD=0_RAW_META_CELLS
```

原因是逻辑粒度，而不是 determinant theorem弱。

一个 R3 internal row cell 给出的 necessity 是：

\[
\text{row minimum below target}
\Longrightarrow
\text{至少有两个 row terms共享最低阶或通过内部 cancellation抬升}.
\]

但是它没有指定：

- 哪两个 terms；
- 是否是两个 monomial-base ties（C2）；
- 是否需要某一个 linear bracket 深（C3）；
- 是否需要两个不同 brackets 同时深；
- required depth是否严格正。

因此若在这一层直接宣称某 pair determinant bound杀掉整个 cell，就会把 disjunction 偷换成 conjunction。

R4 正确结论是：

\[
\boxed{
\text{DET-GCD gives a finite extinction rule for every refined C3 pair,}
}
\]

但 raw 27 row-order cells 还需下一层 structural input 才能决定真正进入哪个 pair/tube。

---

# Part XV — Simultaneous 2/5 Depth and Archimedean Size

对同一 primitive linear bracket，若某 refined state真正要求

\[
v_2(L_i)\ge r_2,
\qquad
v_5(L_i)\ge r_5,
\]

则一次性得到

\[
2^{r_2}5^{r_5}\mid L_i.
\]

从旧 tail/height bounds，令

\[
M:=\max(1,G/K),
\]

本轮给出 safe explicit bounds：

\[
|L_{10}|<\frac{8280dq^7M}{h},
\]

\[
|L_{40}|<\frac{372dq^6M}{h},
\]

\[
|L_{11}|<\frac{42dq^4M}{h},
\]

\[
|L_{21}|<\frac{96dq^5M}{h},
\]

\[
|L_{31}|<\frac{84dq^5M}{h}.
\]

因此 conditional depth-to-zero lemma 已经可用：

\[
\boxed{
2^{r_2}5^{r_5}>|L_i|
\quad\&\quad
2^{r_2}5^{r_5}\mid L_i
\Longrightarrow
L_i=0.
}
\]

但 R3 raw cell并不强迫同一 fixed \(L_i\) 在两个 places同时具有足够正深度，因此本轮不能诚实写：

```text
TEN_PRIMARY_DEPTH_TO_ZERO=PROVED
```

正确 certificate 是：

```text
TEN_PRIMARY_DEPTH_TO_ZERO=FALSE_AT_R3_META_CELL_LEVEL
```

其 conditional theorem 和全部 bracket height bounds 已准备好，一旦下一轮 cyclotomic/tube splice 指定具体 generator，即可直接触发。

---

# Part XVI — Adelic Projective Ratio Complex

对五个 linear generators，analysis-only 坐标

\[
y=\frac\alpha{dt}
\]

给每条 exact zero locus 一个 rational function center：

\[
y_i(q)=-\frac{V_i(q)}{U_i(q)}.
\]

local deep cancellation等价于 \([A_0:T_0]\) 落入该 center 的 2-adic/5-adic neighborhood。

本轮因此得到：

\[
\boxed{
\text{one real half-space/window}
\times
\text{finite 2-adic determinant tubes}
\times
\text{finite 5-adic determinant tubes}.
}
\]

但完整 7-generator object还含两个 quadratic conics，所以最终状态是：

```text
ADELIC_PROJECTIVE_COMPLEX=PARTIAL
LINEAR_PART=PROVED
GLOBAL_EXTENSION=FINITE_BY_2_TYPE_H_CONICS_AND_11_RESULTANTS
```

不是失败，也不伪称所有 obstruction 都在 \(\mathbf P^1\) 上。

---

# Part XVII — Tail-Saturation Face Audit

R3 的第三 Arch escape face

\[
\Delta_\alpha=0
\]

表示 \(|\alpha|\) 的 height 接近 inherited tail upper envelope。

本轮检查它与 projective ratio \([\alpha:T]\) 的关系：source-level height theorem 只给 \(\alpha\) 和 \(t\) 的独立上界/scale，不给一个 exact narrow real interval把 \(\alpha/(dt)\) 唯一化到某个 \(-V_i/U_i\)。因此不能把 tail-height saturation直接升级成 unique bracket zero。

真正可严格加入的是 DTF1 real half-space

\[
\alpha/(dt)<c,
\]

并由此关闭 B21 exact zero locus。

所以 tail-saturation × projective cancellation 得到的是一个更窄的 real-adelic complex，但尚未产生统一 exact algebraic locus。

---

# Part XVIII — q=1 Bracket Specialization Audit

本轮不进入 q=1 Pell/Gaussian campaign，只做 specialization。

在 \(q=1\)、\(\alpha\ne0\) stratum，五个 linear brackets变为：

\[
B_{10}=31\alpha+659T,
\]

\[
B_{40}=23\alpha-48T,
\]

\[
B_{11}=\alpha-41T,
\]

\[
B_{21}=\alpha+39T,
\]

\[
B_{31}=7\alpha-12T.
\]

五个 projective centers仍互异，所有 pair determinants非零。

两个 conics specialize 为：

\[
H_{20}(1)=31\alpha^2+698\alpha T+3471T^2+72075Y^2,
\]

\[
H_{30}(1)=5(10\alpha^2+44\alpha T+221T^2+4805Y^2).
\]

在 \(q=1,\alpha=0\) stratum，因为 \(T\ne0\) 且五个 \(V_i(1)\ne0\)，五个 linear brackets都退化为固定 nonzero \(T\)-multiples；linear cancellation-zero loci消失，两个 conics仍保留。

因此：

```text
Q1_BRACKET_COMPLEX=CLASSIFIED
```

没有进入 norm/Pell orbit extermination。

---

# Part XIX — Success Ledger

## Success A — Complete bracket extraction

**ACHIEVED.**

\[
10\to7=5L+2H.
\]

## Success B — Dependency retirement

**ACHIEVED.**

全部 7 generators 做了 dependency audit；没有 generator 是旧 tail/RCE/carry shadow，也没有 line-line proportional duplication。

## Success C — Projective linearization

**PARTIAL / STRONG.**

五个主要 linear brackets完全统一到 \([\alpha:dt]\in\mathbf P^1\)，但两个 genuine homogeneous quadratic conics不能合法强行线性化。

## Success D — Determinant-GCD theorem

**ACHIEVED.**

\[
\gcd(L_i,L_j)\mid\Delta_{ij}(q)
\]

exact proved。

## Success E — Lift 27 cells

**ACHIEVED.**

27 个 R3 cells全部附上 exact coefficient/bracket incidence、C1/C2/C3 mechanism、conditional depth requirements 和 determinant interfaces。

## Success F — Compress 27

**PARTIAL.**

严格 equivalence（含 Arch face）仍为 27；但 bracket compatibility 因子化为 9 fibres over 3 Arch faces。

## Success G — Ten-primary depth forces exact zero

**NOT TRIGGERED GLOBALLY.**

conditional theorem proved；raw R3 cells尚未强迫足够 simultaneous depth。B21 exact zero independently retired。

## Success H — Finite algebraic/adelic survivor complex

**ACHIEVED in finite adelic-complex form, not finite exact-locus form.**

得到 5 projective lines + 2 conics + 8 live determinant factors + finite root tubes。

## Success I — q>1 closure

**NOT ACHIEVED.**

q>1 remains OPEN。

---

# Part XX — Direct Answers to the Twelve Required Questions

## Q1 — 10 个 grouped coefficients 中多少 distinct primitive additive brackets？

\[
\boxed{7.}
\]

## Q2 — 多少是 \(U(q)\alpha+V(q)dt\) 型？

\[
\boxed{5.}
\]

另外 2 个是 genuine homogeneous quadratic Type H conics。

## Q3 — 多少只是旧 tail/RCE/carry shadow？

\[
\boxed{0.}
\]

五个 linear brackets都能 tail-reexpress，但不是旧 structural linear form 的比例重复；两个 H 也 genuinely new。

## Q4 — primitive projectivization \([\alpha:dt]\) 是否合法、覆盖多少？

合法，因为 \(T=dt\ne0\)。它完整覆盖 5 个 linear problematic brackets；不覆盖 2 个 Type H conics。

## Q5 — 是否证明 \(\gcd(L_i,L_j)\mid\Delta_{ij}(q)\)？

\[
\boxed{\textbf{YES, exactly.}}
\]

## Q6 — determinants 最终只依赖多少 irreducible factors？

raw distinct irreducible polynomial factors：

\[
\boxed{16.}
\]

live \((2,5)\)-primary minimal determinant kernel：

\[
\boxed{8.}
\]

## Q7 — 这些 factors 的 2/5 深度是否可有限 root tubes 描述？

\[
\boxed{\textbf{YES}.}
\]

p=2 只有 \(D_7,D_8\) 两个 unbounded simple-root tubes；p=5 的 live unbounded structure由旧 \(q+4\) tube、\(3q+2,D_4,q-2,D_9\) 等 finitely many simple/exact tubes控制；\(q^2+6q+4\) 在 \(q\equiv2\pmod5\) 上恒为 depth 1。

## Q8 — 27 cells lift 后多少真正 distinct bracket patterns？

\[
\boxed{9\text{ bracket-pattern fibres}.}
\]

如果按 prompt 的严格 equivalence 把 Arch face也算进去，则仍是 27 strict classes；结构上是 \(3\times9\)。

## Q9 — 多少由 pairwise determinant-GCD 直接杀死？

whole raw meta-cells：

\[
\boxed{0.}
\]

原因是 raw cell不指定具体 pair/depth；determinant theorem 已成为 refined C3 subcell 的 exact death rule。

## Q10 — simultaneous 2/5 depth + Arch size 能否强迫 exact zero？

conditional theorem可以；但当前 raw meta-cell 尚未 force 一个 fixed generator达到所需 two-place depth，所以本轮没有合法得到 forced zero。另有一个 independent real result：\(B_{21}=0\) exact locus已被 DTF1关闭。

## Q11 — 最终 surviving object 是什么？

不是 uncontrolled raw cells，也尚不是 finite exact algebraic loci；而是

\[
\boxed{
\textbf{finite adelic line-conic cancellation complex}
}
\]

具体为

\[
3\text{ Arch faces}\times9\text{ bracket fibres}
\]

over 5 projective lines + 2 conics，受 8-factor determinant kernel与 finite p-adic tubes控制。

## Q12 — J2 仍 OPEN，下一轮唯一攻击什么？

本轮没有把 tube 强迫成 exact algebraic locus，所以不能机械跳到 S-unit/Thue–Mahler。

下一轮唯一自然对象是：

\[
\boxed{
q\mid10^g+1
\quad\times\quad
\textbf{finite determinant root tubes}
}
\]

即 **Cyclotomic-Divisor × Determinant-Root-Tube Collision**。

目标是利用 \(q\mid10^g+1\) 的 multiplicative-order/cyclotomic complementarity，给 7 个 live unbounded determinant tubes统一 exponent-depth restriction，把 finite p-adic tubes进一步 algebraize / bound；两个 Type H conics和 11 个 exact resultants作为有限 side kernel随行，而不是重新展开 residue bits。

---

# Part XXI — Final Frontier

本轮以后，禁止再写：

> additive bracket cancellation depth remains uncontrolled.

正确 frontier 已经是：

\[
\boxed{
\begin{aligned}
&5\text{ primitive projective linear brackets}\;+
2\text{ quadratic conics}\\
&+\;8\text{ live }(2/5)\text{-determinant factors}\\
&+\;7\text{ unbounded but finitely classified root tubes}\\
&+\;3\text{ Arch escape faces}\times9\text{ bracket fibres}.
\end{aligned}
}
\]

并且：

- all 10 pair determinants nonzero；
- determinant-GCD theorem proved；
- no bit ladder；
- no fixed-q prime hunt；
- no fake resultant；
- B21 exact zero locus retired；
- q=1 bracket complex classified；
- no S-unit reduction claimed prematurely。

因此 terminal statement 为：

\[
\boxed{\textbf{J2 OPEN}.}
\]

而下一唯一对象为：

\[
\boxed{
\textbf{CYCLOTOMIC DIVISOR }q\mid10^g+1
\times
\textbf{ DETERMINANT ROOT TUBES}.
}
\]

---

# Part XXII — Artifact Index

Generated:

- `J2-65-R4-Additive-Bracket-Complex-Report.md`
- `J2-65-R4-BracketExtraction.py`
- `J2-65-R4-BracketProjectivization.py`
- `J2-65-R4-BracketDeterminants.py`
- `J2-65-R4-BracketCellLift.py`
- `J2-65-R4-AdelicCompatibility.py`
- `J2-65-R4-TailReexpression.py`
- `J2-65-R4-CoefficientFactorization.tsv`
- `J2-65-R4-BracketCatalog.tsv`
- `J2-65-R4-BracketIncidence.tsv`
- `J2-65-R4-BracketDependency.tsv`
- `J2-65-R4-BracketDeterminants.tsv`
- `J2-65-R4-2AdicDeterminantTubes.tsv`
- `J2-65-R4-5AdicDeterminantTubes.tsv`
- `J2-65-R4-LiftedThreePlaceCells.tsv`
- `J2-65-R4-BracketDepthRequirements.tsv`
- `J2-65-R4-BracketHeightBounds.tsv`
- `J2-65-R4-BracketCellQuotient.tsv`
- `J2-65-R4-TailReexpression.tsv`
- `J2-65-R4-HigherBracketResultants.tsv`
- `J2-65-R4-AdelicProjectiveComplex.tsv`
- `J2-65-R4-certificate.txt`
- `J2-65-R4-execution.log`

Not generated:

- `J2-65-R4-AlgebraicSurvivorLoci.tsv` — no exact locus is forced by a whole live R3 meta-cell yet.
- `J2-Resonance-Closure-Certificate.md` — J2 remains OPEN.
