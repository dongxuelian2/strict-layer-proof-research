# 105-R3 — Source-Completed Valuation Atlas × Canonical Initial-Form Fan × Semantic Dimension-Drop Audit

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R3  
**Date:** 2026-08-19  
**Nature:** source-completed valuation/initial-form architecture checkpoint; not an extinction round

---

# 1. Executive Verdict

本轮得到两个必须同时读取的结论。

第一，存在一个有限的 **source-completed combinatorial atlas modulo arithmetic depth**。在 canonical source-completed category 中，所有仍合法的历史 485/95 局部战区可压到五个 primary semantic cell：

\[
\boxed{
\mathfrak F_{\rm sem}^{\rm prim}
=
\{S0,S1,S2,S3,S4\}.
}
\]

它们不是按 \(J\) 命名，而由 pre-\(J\) master state 的五种真实 initial/dominance regimes 决定：

\[
\begin{array}{c|l}
S0 & g=0,\\
S1 & g>0,\ R=0,\\
S2 & g>0,\ R\ne0,\ d\in\{0,1\},\\
S3 & g>0,\ d\le-1,\\
S4 & g>0,\ d\ge2.
\end{array}
\]

其中 \(d=m_2-g\)，
\[
R=b_2 10^{n_3}-b_3.
\]

第二，source completion 修复了 provenance，却**没有让 valuation layer 自己产生新的 semantic codimension**。条件在一个 cell 内固定以后，canonical radial source fibre 仍是 rank one；q=1 只把它替换成一个有限指数 affine sublattice，rank 仍为 one；\(J\) 只是 DES denominator saturation decoration，不对 \(U\) 产生新 rank loss。

因此本轮的 architecture verdict 为：

\[
\boxed{
\texttt{FINITE\_INITIAL\_FORM\_TYPES\_MODULO\_DEPTH=PROVED}
}
\]

并且，在 105 所采用的 mixed decorated semantic category 中可以进一步写成：

\[
\boxed{
\texttt{FINITE\_SOURCE\_COMPLETED\_VALUATION\_ATLAS=PROVED}
}
\]

其严格 qualifier 是：

> **finite 指 combinatorial cell/decorated type 有限，不指 \(J\)、\(v_2(J)\)、\(v_5(J)\)、q=1 source-sublattice index 或其他 arithmetic depth 数值有界。**

但同时：

\[
\boxed{
\texttt{NEW\_SEMANTIC\_DIMENSION\_DROP\_FROM\_VALUATION=NO}
}
\]

以及：

\[
\boxed{
\texttt{VALUATION\_ATLAS\_SEMANTICALLY\_SATURATED}.
}
\]

这意味着 105-R4 不应继续细分 valuation，而应转入：

\[
\boxed{
\Gamma_{10}
\times
\kappa_{\rm src}
\times
\textbf{fixed-incidence extraction}.
}
\]

本轮没有证明 \(A_1=\varnothing\)。

---

# 2. R1/R2 Frozen State

105-R1/R2 的以下对象全部冻结，不再重新证明。

## 2.1 Canonical source fibre

对 pre-\(J\) base state \(x\)：

\[
\mathbf C_x=(C_1,C_2,C_3),
\qquad
\gcd(C_1,C_2,C_3)=1,
\]

\[
\boxed{
L_x=\mathbf Z\mathbf C_x\subset\mathbf Z^3.
}
\]

真实 numerator triple：

\[
(a_1,a_2,a_3)=U(C_1,C_2,C_3),
\]

且：

\[
\boxed{
U=\gcd(a_1,a_2,a_3).
}
\]

所以 \(U\) 是 intrinsic common content，不能 projectivize 掉。

## 2.2 Admissible section

\[
L(x)
=
\max_i \frac{10^{n_i-1}}{C_i},
\qquad
R(x)
=
\min_i \frac{10^{n_i}}{C_i},
\]

\[
\boxed{
\operatorname{SrcLift}(x)
=
\left\{
U\mathbf C_x:
U\in\mathbf Z_{>0},\ 
L(x)\le U<R(x),\
\gcd(U,V)=1,\
\text{exact source conditions}
\right\}.
}
\]

actual word / cut 是 \((x,U)\) 的 deterministic function。

## 2.3 \(J\) saturation

设：

\[
\delta_\beta=\gcd(\beta,10^{m_3}),
\qquad
\Lambda_\beta=\frac{10^{m_3}}{\delta_\beta},
\]

\[
\delta_v=\gcd(v,\Lambda_\beta),
\qquad
J=\frac{\Lambda_\beta}{\delta_v}.
\]

定义：

\[
D_x=\Lambda_\beta\mathbf Z,
\qquad
\operatorname{Sat}_v(D_x)
=
D_x+v\mathbf Z.
\]

则：

\[
\boxed{
J=
[\operatorname{Sat}_v(D_x):D_x].
}
\]

所以 \(J\) 是 canonical DES denominator saturation index，不是 radial \(U\)-lattice index。

## 2.4 q=1 source glue

在 q=1 fixed source stratum：

\[
a_3=UC_3=d_q a,
\qquad
\rho=a-\frac{\tau G}{10}.
\]

source domain 要求：

\[
\boxed{
31C_3U+d_q\tau
\equiv0
\pmod{2Kd_q}.
}
\]

若非空：

\[
U=U_0+h_U z,
\qquad
\boxed{
h_U=
\frac{2Kd_q}{\gcd(C_3,2Kd_q)}.
}
\]

且：

\[
\boxed{
\rho(U)
=
\frac{UC_3}{d_q}-\frac{\tau G}{10}.
}
\]

因此 q=1 的历史 \(\rho\)-coset一般只是 source image 的一个 supercoset；\(\rho\) 是 affine observable，不取代 \(U\)。

---

# 3. Master Exact Equation Package

R3 不从 historical branches 反推 master。下面固定一个足以生成本轮 atlas 的 pre-\(J\) source-completed exact subsystem。

## 3.1 Layer A — primitive algebraic rows

\[
\boxed{
F_{\rm sph}
=
P_1^2+P_2^2+P_3^2-Q_0^2
=
0
}
\]

以及：

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

令：

\[
g_i=\gcd(V,P_i),
\qquad
C_i=P_i/g_i,
\qquad
b_i=V/g_i.
\]

## 3.2 Layer B — decimal synchronization rows

A1 exponent normal form：

\[
g=m_3-n_3\ge0,
\qquad
k\ge1,
\]

\[
\boxed{
n_2=m_2+g+k,
\qquad
m_3=n_3+g.
}
\]

令：

\[
G=10^g,
\qquad
K=10^k,
\qquad
X=10^{m_2},
\qquad
Y=10^{n_3}.
\]

则：

\[
10^{m_3}=YG,
\qquad
10^{n_2}=XGK.
\]

把 powers of ten 当作 variables 而不是 moving coefficients，primitive word master 可写成固定有限 support：

\[
\boxed{
b_1XYG(KP_1-Q_0)
+
b_2Y(P_2-GQ_0)
-
b_3(Q_0-P_3)
=
0.
}
\tag{M}
\]

定义：

\[
\boxed{
D=KP_1-Q_0>0,
}
\]

\[
\boxed{
T_3=Q_0-P_3>0.
}
\]

则 (M) 为：

\[
\boxed{
b_1XYGD+b_2Y(P_2-GQ_0)-b_3T_3=0.
}
\]

## 3.3 Ordinary-integer defect package

定义：

\[
\boxed{
H=b_2Q_0-b_1XD.
}
\]

flat locus 已关闭，因此：

\[
\boxed{H\ne0.}
\]

定义：

\[
\boxed{
\tau_3=\frac{b_3T_3}{Y}\in\mathbf Z_{>0}.
}
\]

则 exact UDD：

\[
\boxed{
b_2P_2-\tau_3=GH.
}
\tag{UDD}
\]

再定义：

\[
\boxed{
R=b_2Y-b_3.
}
\tag{R}
\]

\(R=0\) 是 resonance；\(R\ne0\) 是 nonresonance。

## 3.4 GSYNC form

\[
\Delta_{12}
=
g_2XD-g_1Q_0,
\]

\[
\Delta_3
=
g_3P_2Y-g_2T_3,
\]

\[
\boxed{
g_1\Delta_3
=
-YG\,g_3\Delta_{12}.
}
\]

这是 word master 的 primitive defect view，不作为额外 independent gate。

## 3.5 Layer C — DES / saturation

DES rows保留在 base state 中；\(J\) 仅由：

\[
D_x=\Lambda_\beta\mathbf Z
\longmapsto
\operatorname{Sat}_v(D_x)
\]

读取。

## 3.6 Layer D/E — source section

\[
a_i=UC_i,
\]

\[
10^{n_i-1}\le UC_i<10^{n_i},
\]

\[
\gcd(U,V)=1.
\]

q=1 再 intersection：

\[
31C_3U+d_q\tau\equiv0\pmod{2Kd_q}.
\]

## 3.7 Layer F — derived observables only

以下不得反过来定义 master：

- \(H\)-sign；
- \(R=0\) / \(R\ne0\)；
- \(d=m_2-g\)；
- resonance / transition / outer；
- \(J\)；
- q=1 \(\rho\)；
- historical Gaussian / norm coordinates。

---

# 4. Minimal Valuation Carrier Set

本轮的关键结论是：**raw \(2/5\)-adic tuples 不是 minimal state。**

定义 primary combinatorial carrier：

\[
\boxed{
\nu_{\rm sem}^{\rm prim}
=
(\chi_g,\chi_R,\chi_d,\operatorname{sgn}H,\operatorname{sgn}R).
}
\]

其中：

\[
\chi_g\in\{g=0,g>0\},
\]

\[
\chi_R\in\{R=0,R\ne0\},
\]

\[
\chi_d
\in
\{d\le-1,d=0,d=1,d\ge2\}.
\]

sign 坐标只在没有被 branch theorem 强制时保留。

secondary decorations：

\[
\boxed{
\mathfrak d_{\rm sem}
=
(
J_{\rm sat},
q{\rm -status},
\mathcal A_L,\mathcal A_R,
\mathcal L_{\rm src}
).
}
\]

这里：

- \(J_{\rm sat}\)：完整 saturation index value，但数值 depth 不 split cell；
- q-status：只在 \(J=2\) special arithmetic decoration 上记录 q=1/q>1；
- \(\mathcal A_L,\mathcal A_R\)：Archimedean digit interval active faces；
- \(\mathcal L_{\rm src}\)：rank-one full source lattice或 q=1 rank-one affine finite-index sublattice schema。

## 4.1 从 minimal carrier 删除的量

### \(v_2(U),v_5(U)\)

不进入 master initial support。若 \(\gcd(U,V)=1\) 强制某处 unit，这只是 source gate，不应添加常量 valuation coordinate。

### raw \(v_p(C_i)\)

只有在某个局部 arithmetic proof中选择 prime 时才有用；它们不是 global cell selector。

### \(v_2(R),v_5(R)\) for \(R\ne0\)

当前 primary support只需要 \(R=0\) vs \(R\ne0\)。nonzero valuation depth没有产生新的 master support。

### \(v_2(J),v_5(J)\)

可从完整 \(J\) 读取；它们是 arithmetic depth，不是 cell coordinate。

---

# 5. Semantic Weight Definition

令 decimal toric variables：

\[
(G,K,X,Y)
=
(10^g,10^k,10^{m_2},10^{n_3}).
\]

给 monomial \(G^aK^bX^cY^e\) 的 real weight：

\[
w(a,b,c,e)
=
ag+bk+cm_2+en_3.
\]

但 exact A1 exponent relations把 relevant wall arrangement压到有限 comparator：

1. \(g=0\) vs \(g>0\)；
2. \(R=0\) vs \(R\ne0\)；
3. \(d=m_2-g\) 位于
   \[
   (-\infty,-1],\{0\},\{1\},[2,\infty);
   \]
4. \(H,R\) sign。

因此 R3 不把 \(g,k,m_2,n_3\) 的所有数值当成不同 cone。

数字 depth translation 可无界，但 initial support type不变。

---

# 6. Newton / Initial-Form Dictionary

对 algebraic subsystem：

\[
\mathcal I_{\rm alg}
=
\langle
F_{\rm sph},F_D,F_{T3},F_H,F_R,F_\tau,F_{\rm UDD}
\rangle
\]

可取：

\[
F_D=D-KP_1+Q_0,
\]

\[
F_{T3}=T_3-Q_0+P_3,
\]

\[
F_H=H-b_2Q_0+b_1XD,
\]

\[
F_R=R-b_2Y+b_3,
\]

\[
F_\tau=Y\tau_3-b_3T_3,
\]

\[
F_{\rm UDD}=b_2P_2-\tau_3-GH.
\]

所有 polynomial support 均固定且有限。

## 6.1 coefficient vs variable decision

\(G,K,X,Y\) 必须作为 variables。

若把 \(10^g,10^k,10^{m_2},10^{n_3}\) 当 moving coefficients，则会人为制造“无限 moving polynomial family”。把它们 toricize 后，support固定。

## 6.2 historical dictionary

### \(g=0\)

不是某个新 prime signature，而是 decimal depth face：

\[
G=1.
\]

### resonance

由：

\[
R=0
\iff
b_2Y=b_3
\]

产生 exact face。

### transition

由：

\[
d=0,1
\iff
X/G\in\{1,10\}
\]

产生两条 adjacent depth walls；它们共享同一个 source-completed local support，所以归入同一 primary cell。

### outer plus

\[
d\le-1
\iff
X/G\le 10^{-1}.
\]

historical theorem给：

\[
H<0,\qquad R<0.
\]

### outer minus

\[
d\ge2
\iff
X/G\ge100.
\]

在 surviving nontransition regime：

\[
H>0,\qquad R>0.
\]

### \(J=2\)

不是 Newton face。

它是：

\[
J_{\rm sat}=2
\]

这一 arithmetic saturation decoration。

### q=1

不是新的 primary initial form。

它是 \(J=2\) decoration 上的 secondary source specialization，并附 finite-index \(U\)-sublattice。

---

# 7. Canonical Cell Construction

定义 mixed semantic initial form：

\[
\boxed{
\operatorname{In}^{\rm sem}_\sigma(\mathcal E_{\rm master})
=
\left(
\operatorname{in}_{w_\sigma}\mathcal I_{\rm alg},
\mathfrak d_{\rm sat},
\mathfrak d_{\rm src},
\mathfrak d_{\rm Arch}
\right).
}
\]

它不是裸 tropical variety。

## S0 — depth-zero cell

\[
\boxed{
S0:\quad g=0.
}
\]

已知 \(R=0\) 在该 stratum 不发生，因此 \(R>0\)。

\(H\)-sign/borrow若需要保留，作为 finite secondary decoration。

## S1 — resonance cell

\[
\boxed{
S1:\quad g>0,\ R=0.
}
\]

historical general resonance、J5 residual，以及**当前 recovered 485/J2 exact-resonance corpus** 的 q-specializations统一落在这里。这里的逻辑是 “recovered J2 corpus is resonance-specialized”，不是 “J=2 本身强迫 resonance”。

## S2 — transition cell

\[
\boxed{
S2:\quad
g>0,\ R\ne0,\ d\in\{0,1\}.
}
\]

d=0 / d=1、plus/minus、finite borrow只是 secondary decoration。

## S3 — outer-low cell

\[
\boxed{
S3:\quad
g>0,\ d\le-1.
}
\]

historical exact branch map：

\[
H<0,\qquad R<0.
\]

## S4 — outer-high cell

\[
\boxed{
S4:\quad
g>0,\ d\ge2.
}
\]

historical surviving branch：

\[
H>0,\qquad R>0.
\]

outer-minus carry depth可无界，但它改变 coefficient/value，不改变 master monomial support，因此不能把每个 carry value升格成新 cell。

---

# 8. Finiteness Proof

## Theorem R3.1 — Finite source-completed initial-form types modulo depth

在 canonical source-completed category 中，Strict \(A_1\) 的 master states modulo arithmetic depth translation 只有有限种 semantic initial-form type。

### Proof

**Step 1 — algebraic support finite.**

把 \(G,K,X,Y\) toricize 后，\(\mathcal I_{\rm alg}\) 由固定有限 support polynomials生成。不存在随 \(g,k,m_2,n_3\) 产生新的 monomial exponent set。

**Step 2 — exact branch walls finite.**

历史已证明：

\[
g=0
\quad\text{or}\quad
g>0.
\]

当 \(g>0\)：

\[
R=0
\]

产生 resonance；当 \(R\ne0\)，\(d\) 只需按：

\[
d\le-1,\quad d=0,\quad d=1,\quad d\ge2
\]

分类。branch theorem进一步把这些 chambers压成 S1–S4，而不是无限 \(d\)-cells。

**Step 3 — signs finite.**

\(\operatorname{sgn}H,\operatorname{sgn}R\) 只有有限状态；S3/S4已被 exact branch law固定。

**Step 4 — Archimedean source faces finite.**

\[
L=\max_i10^{n_i-1}/C_i,
\qquad
R_{\rm src}=\min_i10^{n_i}/C_i.
\]

active lower set \(\mathcal A_L\) 是 \(\{1,2,3\}\) 的非空子集，active upper set同理，因此最多：

\[
(2^3-1)^2=49
\]

种 active-face type。数值 endpoint 可以移动，但 combinatorial face type有限。

**Step 5 — source lattice schemas finite.**

generic source lattice只有：

\[
\mathbf Z\mathbf C_x.
\]

q=1 specialization只有一个额外 schema：

\[
U\in U_0+h_U\mathbf Z.
\]

\(h_U\) 可无界，但它是 arithmetic depth/index value，不产生新的 rank/type。

**Step 6 — \(J\) depth不 split cells.**

\(J\) 是同一个 rank-one denominator saturation construction的 index value。不同 \(J\) 数值属于同一 decoration schema。

故 primary semantic types只有：

\[
\boxed{5}.
\]

加入上述有限 secondary combinatorial decorations后仍有限。

\[
\square
\]

### Qualifier

本 theorem **不声称**完整计算了所有可能 historical auxiliary Gröbner fan；它证明的是 105 所需的 **source-completed master semantic atlas** 有限。

---

# 9. Historical-to-Canonical Branch Quotient

历史 branch 数显著大于 canonical primary cell 数。

\[
\boxed{
\text{485/95 are no longer architectures; they are charts/decorations over }S0\text{--}S4.
}
\]

主要 quotient：

- \(\mathcal H_0\to S0\)；
- general resonance \(\to S1\)；
- J5 residual resonance \(\to S1\) + \(J=5\) decoration；
- \(J=2,q>1\to S1\) + \(J=2\) decoration；
- \(J=2,q=1\to S1\) + \(J=2,q=1\) source-sublattice decoration；
- transition d=0,1 \(\to S2\)；
- outer plus \(\to S3\)；
- outer minus \(\to S4\)。

已关闭的 historical cases 不重新作为 cells。

---

# 10. \(J\)-Decoration Theorem

## Theorem R3.2 — \(J\) is not a primary atlas coordinate

在 R2 已证明 saturation functoriality后：

\[
J=
[\operatorname{Sat}_v(D_x):D_x]
\]

完全由 pre-\(J\) DES denominator module及 \(v\) 读取。

因此：

1. \(J\) 不改变 canonical radial fibre；
2. \(J\) 不改变 algebraic master monomial support；
3. \(J\) 可改变 arithmetic specialization强度；
4. \(J=2\) 可激活额外 q-coordinate，但该 coordinate属于 decorated chart，而不是新的 master object。

故：

\[
\boxed{
\texttt{J\_AS\_ARCHITECTURE\_VARIABLE=NO}.
}
\]

---

# 11. q=1 Decorated Cell

q=1 放在 S1 的 \(J=2\) decoration 下。

其 source-completed data 必须包含：

\[
L_x=\mathbf Z\mathbf C_x,
\]

\[
U\in\operatorname{SrcLift}(x),
\]

\[
31C_3U+d_q\tau\equiv0\pmod{2Kd_q},
\]

\[
\rho(U)
=
\frac{UC_3}{d_q}-\frac{\tau G}{10},
\]

\[
U=
\frac{d_q(\rho+\tau G/10)}{C_3}.
\]

若定义：

\[
a_0=\frac{\tau G}{10}+r_{K,\tau},
\]

则：

\[
j_\rho(U)
=
\frac{UC_3/d_q-a_0}{2K},
\]

历史 norm coordinate满足 affine image：

\[
C_{\rm norm}(U)
=
c_{K,\tau,g}
+
A_2j_\rho(U).
\]

所以 q=1 的正确 cell object 是：

\[
\boxed{
\text{S1 initial form}
+
(J=2,q=1)
+
(U_0+h_U\mathbf Z)
+
\rho(U)
+
\kappa_{\rm src}.
}
\]

不是 naked Gaussian circle。

---

# 12. q>1 \(J=2\) Cells

q>1 的 485 high/boundary/reverse、regular/singular等历史 labels只在需要时作为 secondary arithmetic/coordinate decorations。

它们不能重新把 S1 分裂为顶层研究 architecture，因为：

- source fibre仍是同一 embedded rank-one \(\mathbf Z\mathbf C_x\)；
- \(J=2\) 仍只来自 DES saturation；
- q-coordinate是 specialization后的 observable；
- 已恢复的 q>1 conic/norm/source packets属于 master pullback charts。

---

# 13. H0 Cell

\[
S0:g=0.
\]

H0 的 source geometry仍是：

\[
L_x=\mathbf Z\mathbf C_x,
\]

\[
\operatorname{SrcLift}(x)
=
[L,R)\cap\mathbf Z_{>0}\cap(\mathbf Z/V\mathbf Z)^\times.
\]

历史 C/I/P hierarchy：

- continuous failure；
- integer failure；
- coprime-unit failure；

只是同一 source fibre的三种 first-death location。

它们不是三个 new valuation cells。

---

# 14. Resonance Cell

\[
S1:R=0.
\]

历史 resonance 已有强结构：

\[
b_2Y=b_3,
\]

并在相应 Smith/DES坐标产生额外 restrictions。

这些是 **inherited base restrictions**。

R3 不把它们误记成“valuation 新产生的 global codimension”。

---

# 15. Transition Cell

\[
S2:R\ne0,\ d=0,1.
\]

历史 R6/R7 已 exactize affine defect与 source headroom，但 R7 证明：

\[
\Delta(\text{canonical freedom})=0
\]

for current affine-to-boundary bridge architecture。

这在 R3 中得到统一解释：

> transition 的 extra affine coordinates 是同一个 S2 source section 的 observables；它们没有生成新的 \(U\)-equation。

---

# 16. Outer Plus Cell

\[
S3:d\le-1.
\]

historical exact sign：

\[
H<0,\qquad R<0.
\]

projective smallness：

\[
P_3/P_2
\]

可以随 depth退化，但 source/Smith ratio同步吸收该退化。

R3 不再把每个 \(d=-1,-2,\ldots\) 作为新 cell。

它们都是同一 outer-low initial/dominance type 的 numeric depth translations。

---

# 17. Outer Minus Cell

\[
S4:d\ge2.
\]

outer-minus 的 carry alphabet可能随 \(d\) 增长。

但：

\[
1\le c\le10^d
\]

是 **coordinate value range**，不是新的 monomial support。

因此：

\[
\boxed{
\text{unbounded carry value}
\ne
\text{infinitely many canonical initial-form types}.
}
\]

只有当未来证明 carry 改变 source-completed master support本身，才有资格拆新 cell；目前没有这种证据。

---

# 18. Cell-Overlap / Cocycle Audit

R3 的 gluing 不是通过任意 historical naked chart之间做 birational map，而是通过 **pull back 到同一个 source-completed master state**。

因此 transition map 是：

\[
\text{chart}_i
\leftarrow
\text{master state}
\rightarrow
\text{chart}_j.
\]

在 overlap 上：

\[
U_i=U_j,
\qquad
\kappa_{\rm src}^{(i)}=\kappa_{\rm src}^{(j)}.
\]

于是 triple overlap上的 composition 自动满足 cocycle。

## 18.1 transition \(\to\) resonance

取 \(R\to0\) specialization：

\[
\kappa_{\rm src}^{T}|_{R=0}
=
\kappa_{\rm src}^{R}.
\]

## 18.2 outer \(\to\) transition

\(d\) 跨：

\[
-1\to0,
\qquad
1\to2
\]

时，变化的是 Archimedean/dominance chamber，不改变 underlying \(\mathbf Z\mathbf C_x\) 与 \(U\)。

## 18.3 \(J=2\) specialization

只改变 saturation decoration：

\[
\mathfrak d_{\rm sat}\mapsto (J=2).
\]

## 18.4 q>1 \(\to\) q=1

q=1 不是 full-coset identification，而是：

\[
\mathbf Z_U
\supset
U_0+h_U\mathbf Z.
\]

source point可双向恢复，但 image是 finite-index sublattice。

## 18.5 \(g>0\to g=0\)

作为 exponent specialization：

\[
G\to1.
\]

source lattice仍为：

\[
\mathbf Z\mathbf C_x.
\]

### Verdict

\[
\boxed{
\texttt{CELL\_OVERLAP\_COCYCLE=PROVED}
}
\]

qualifier：

> **在 master-pullback source-completed category 中。**  
> 不声称 historical naked Gaussian / reduced outer-minus charts本身构成 source-preserving cocycle。

---

# 19. Source-Fibre Decoration

每个 primary cell都携带：

\[
\boxed{
L_x=\mathbf Z\mathbf C_x.
}
\]

generic admissible set：

\[
\boxed{
[L,R)\cap\mathbf Z_{>0}\cap(\mathbf Z/V\mathbf Z)^\times.
}
\]

q=1：

\[
\boxed{
[L,R)\cap(U_0+h_U\mathbf Z)
\cap(\mathbf Z/V\mathbf Z)^\times.
}
\]

因此 source rank：

\[
\boxed{1}
\]

在所有非空 cells 中保持。

---

# 20. Archimedean Chamber Decoration

定义：

\[
\mathcal A_L
=
\operatorname{argmax}_{i=1,2,3}
\frac{10^{n_i-1}}{C_i},
\]

\[
\mathcal A_R
=
\operatorname{argmin}_{i=1,2,3}
\frac{10^{n_i}}{C_i}.
\]

每个是 \(\{1,2,3\}\) 的非空子集。

这记录 tie / active endpoint，而不把每个 endpoint数值当新 cell。

最大 combinatorial type count：

\[
49.
\]

---

# 21. Primitive Decoration

primitive条件：

\[
\gcd(P_1,P_2,P_3,Q_0)=1
\]

以及：

\[
\gcd(C_1,C_2,C_3)=1
\]

保留为 arithmetic predicate。

它不通过 raw \(v_p(C_i)\) 向量展开。

---

# 22. Minimal Canonical Cell Register

| Cell | Primary condition | Initial/dominance type | \(J\) | source lattice | q-status | historical quotient | new R3 semantic drop |
|---|---|---|---|---|---|---|---|
| S0 | \(g=0\) | depth-zero | decoration | rank-1 | generic | H0 | NO |
| S1 | \(g>0,R=0\) | resonance face | decoration | rank-1; q1 finite-index refinement | q1/q>1 secondary | resonance, J5, J2 | NO NEW |
| S2 | \(g>0,R\ne0,d=0,1\) | transition walls | decoration | rank-1 | generic | T0/T1 | NO |
| S3 | \(g>0,d\le-1\) | outer-low, \(H<0,R<0\) | decoration | rank-1 | generic | outer plus | NO |
| S4 | \(g>0,d\ge2\) | outer-high, \(H>0,R>0\) | decoration | rank-1 | generic | outer minus | NO |

---

# 23. Semantic Dimension Ledger

R3 区分：

\[
\texttt{AMBIENT\_CODIMENSION},
\quad
\texttt{SOURCE\_CODIMENSION},
\quad
\texttt{SEMANTIC\_CODIMENSION}.
\]

这里的 `SEMANTIC_FREEDOM_AFTER` 是 **conditioning on the cell以后** 的 source-compatible freedom，不把“属于这个 cell”本身重复计算成新发现。

## S0

```text
BASE_PARAMETERS = primitive/Smith/word state with g=0
RADIAL_PARAMETERS = U
DISCRETE_PARAMETERS = J, active faces, Smith data
INITIAL_FORM_CONSTRAINTS = G=1
SOURCE_LATTICE_CONSTRAINTS = U in [L,R), gcd(U,V)=1
SEMANTIC_FREEDOM_BEFORE = conditioned H0 base + one radial parameter
SEMANTIC_FREEDOM_AFTER = same rank-one radial parameter
DIMENSION_DROP = NONE_NEW
DROP_CAUSE = n/a
```

## S1

```text
BASE_PARAMETERS = resonance-compatible primitive/Smith/word state
RADIAL_PARAMETERS = U
DISCRETE_PARAMETERS = J; optional q-status
INITIAL_FORM_CONSTRAINTS = R=0
SOURCE_LATTICE_CONSTRAINTS = rank-one; q1 finite-index rank-one refinement
SEMANTIC_FREEDOM_BEFORE = conditioned resonance base + one radial parameter
SEMANTIC_FREEDOM_AFTER = one radial parameter
DIMENSION_DROP = NONE_NEW_AFTER_CELL_CONDITIONING
DROP_CAUSE = inherited R=0 base restriction only
```

## S2

```text
BASE_PARAMETERS = transition-compatible primitive/Smith/word state
RADIAL_PARAMETERS = U
DISCRETE_PARAMETERS = d in {0,1}; sign/borrow; J
INITIAL_FORM_CONSTRAINTS = R!=0 and transition depth wall
SOURCE_LATTICE_CONSTRAINTS = rank-one
SEMANTIC_FREEDOM_BEFORE = conditioned transition base + U
SEMANTIC_FREEDOM_AFTER = same
DIMENSION_DROP = NONE
DROP_CAUSE = R7 bridge independence
```

## S3

```text
BASE_PARAMETERS = outer-low state
RADIAL_PARAMETERS = U
DISCRETE_PARAMETERS = J, active faces
INITIAL_FORM_CONSTRAINTS = d<=-1, H<0, R<0
SOURCE_LATTICE_CONSTRAINTS = rank-one
SEMANTIC_FREEDOM_BEFORE = conditioned outer-low base + U
SEMANTIC_FREEDOM_AFTER = same
DIMENSION_DROP = NONE
DROP_CAUSE = valuation only locates the degeneration
```

## S4

```text
BASE_PARAMETERS = outer-high state
RADIAL_PARAMETERS = U
DISCRETE_PARAMETERS = J, carry value, active faces
INITIAL_FORM_CONSTRAINTS = d>=2, H>0, R>0
SOURCE_LATTICE_CONSTRAINTS = rank-one
SEMANTIC_FREEDOM_BEFORE = conditioned outer-high base + U
SEMANTIC_FREEDOM_AFTER = same
DIMENSION_DROP = NONE
DROP_CAUSE = unbounded carry depth is not codimension
```

### Global ledger conclusion

\[
\boxed{
\operatorname{rank}_{\rm src}=1
\quad\text{before and after valuation classification}.
}
\]

q=1 finite-index restriction不改变 rank。

---

# 24. Dimension-Drop Audit

## Theorem R3.3 — No-new-radial-drop theorem

固定任何 primary cell \(\sigma\)。

如果 base state \(x\in\sigma\) 的 source section非空，则：

- generic:
  \[
  \operatorname{SrcLift}_\sigma(x)
  \subset
  \mathbf Z\mathbf C_x
  \]
  是 rank-one lattice上的 interval/unit subset；
- q=1:
  \[
  \operatorname{SrcLift}_\sigma(x)
  \subset
  (U_0+h_U\mathbf Z)\mathbf C_x
  \]
  仍是 rank-one affine sublattice上的 subset。

primary cell predicates：

\[
g=0,\ R=0,\ d\text{-chamber},\operatorname{sgn}H,\operatorname{sgn}R
\]

全部在 pre-\(J\) base上定义，并没有额外给出：

\[
U=f(x)
\]

或：

\[
U\equiv u_*(x)\pmod{M_*(x)}
\]

的新 universal equation。

所以 valuation atlas本身不把 radial rank从 1 降到 0。

\[
\square
\]

## Important distinction

S0 的 \(g=0\)、S1 的 \(R=0\)、S2 的 \(d=0,1\) 的确是 **cell-defining base restrictions**。

R3 不否认它们把整个 unrestricted master state切成 proper strata。

但它们不是 source completion 后新发现的 cross-cell rigidity，更没有把剩余 source-compatible family压到 fixed proper power-of-ten incidence。

所以 terminal verdict必须写：

\[
\boxed{
\texttt{SEMANTIC\_DIMENSION\_DROP=NONE\_NEW\_FROM\_VALUATION\_LAYER}.
}
\]

---

# 25. Valuation Saturation Countertest

本轮构造一个 explicit pseudo-source counterfamily，用来压力测试：

> “same canonical cell + same \(J\) decoration + same source geometry” 是否自动产生 codimension？

它**不是 original A1 solution**，因为它故意不满足 full master/UDD。它的用途正是隔离 valuation/source/primitive information 与 global master incidence之间的独立性。

## 25.1 S3-R3-VSCF

对每个整数 \(r\ge1\)，令：

\[
G=10^{r+1},
\qquad
K=10,
\]

\[
V=10^{2r+3}=10G^2.
\]

定义：

\[
P_2=V,
\qquad
P_3=1,
\]

\[
P_1=\frac{V^2}{2},
\qquad
Q_0=\frac{V^2+2}{2}.
\]

则：

\[
Q_0-P_1=1,
\qquad
Q_0+P_1=V^2+1,
\]

故：

\[
Q_0^2-P_1^2=V^2+1=P_2^2+P_3^2.
\]

所以：

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2.
}
\]

且 \(P_3=1\)，primitive gcd 自动为 1。

又：

\[
g_1=g_2=V,
\qquad
g_3=1,
\]

所以：

\[
C_1=V/2,
\qquad
C_2=C_3=1,
\]

\[
b_1=b_2=1,
\qquad
b_3=V.
\]

取：

\[
m_1=m_2=1,
\qquad
m_3=2r+4,
\]

\[
n_2=n_3=r+3,
\qquad
n_1=3r+5.
\]

于是：

\[
g=m_3-n_3=r+1,
\]

\[
k=1,
\]

\[
d=m_2-g=-r\le-1.
\]

因此所有 \(r\) 都在：

\[
\boxed{S3}.
\]

source interval exact 为：

\[
\boxed{
10^{r+2}
\le U
<
2\cdot10^{r+2}.
}
\]

取：

\[
\boxed{
U_r=10^{r+2}+1.
}
\]

因为 \(V\) 是 pure \(10\)-power：

\[
\gcd(U_r,V)=1.
\]

所以 primitive、source interval、coprime gate全部通过，且 Archimedean active-face pattern对所有 \(r\) 相同。

## 25.2 Same \(J\) decoration

取 Smith/DES-compatible presentation：

\[
s=\alpha=\beta=t=u=1,
\qquad
v=V,
\]

于是：

\[
b_1=s\alpha u=1,
\]

\[
b_2=s\alpha\beta t=1,
\]

\[
b_3=s\beta v=V.
\]

因为 \(\beta=1\)：

\[
\Lambda_\beta=10^{m_3}=10^{2r+4}.
\]

而：

\[
\delta_v=\gcd(V,\Lambda_\beta)=V=10^{2r+3}.
\]

因此：

\[
\boxed{
J=10
}
\]

对所有 \(r\) 恒定。

所以该 family固定：

- primary cell = S3；
- \(J\)-decoration = 10；
- q-status = generic；
- source lattice type = rank-one；
- Arch active-face type = fixed；
- primitive status = fixed；
- source coprime legality = PASS；

但：

\[
r\to\infty.
\]

## 25.3 Exact location of failure

对该 family：

\[
D=KP_1-Q_0
=
450G^4-1,
\]

\[
H=Q_0-10D
=
11-4450G^4<0.
\]

又：

\[
R=10^{n_3}-V
=
100G-10G^2<0.
\]

所以 exact sign profile也始终固定为 S3。

并有：

\[
\tau_3
=
\frac{b_3(Q_0-P_3)}{10^{n_3}}
=
5G^5.
\]

UDD residual：

\[
\mathcal R_{\rm UDD}
=
P_2-\tau_3-GH
\]

化简为：

\[
\boxed{
\mathcal R_{\rm UDD}
=
G(4445G^4+10G-11)>0.
}
\]

所以它被 **global master incidence** 精确杀死，而不是被 valuation/source/J/digit data 杀死。

## 25.4 Countertest verdict

\[
\boxed{
\texttt{VALUATION\_SATURATION\_COUNTERFAMILY=S3-R3-VSCF}.
}
\]

它证明：

> finite valuation signature、固定 \(J\)、合法 rank-one source fibre、primitive sphere、合法 digit chamber，并不足以生成 global codimension。

这与历史 485/95 “finite branching without closure” 现象吻合，但现在是在 source completion 后用统一语言得到。

---

# 26. Cross-Cell Rigidity Candidates

R3 检验 K1–K7：

| Candidate | Verdict |
|---|---|
| K1 initial-form rank deficiency | NO uniform new rank gain |
| K2 fixed character \(G^aK^b=c\) | NOT FOUND |
| K3 lattice/source incompatibility | q1 only finite-index refinement; no uniform emptiness |
| K4 affine-cell exclusion | cell-dependent, no cross-cell theorem |
| K5 primitive degeneration | historical local uses exist; no uniform cross-cell mechanism |
| K6 rank-one radial collapse | FALSE at valuation level |
| K7 fixed anomalous component | NOT YET EXTRACTED |

最有价值的 surviving candidate不再是 valuation invariant，而是：

\[
\boxed{
\textbf{SOURCE-COMPLETED POWER10 FIXED-INCIDENCE EXTRACTION}.
}
\]

---

# 27. \(\Gamma_{10}\) Activation Audit

令：

\[
\Gamma_{10}
=
\{(10^g,10^k):g,k\in\mathbf Z_{\ge0}\}.
\]

本轮只做资格审计。

## 27.1 What is fixed now

把：

\[
G,K,X,Y
\]

作为 variables 后，master **total space** 是 fixed polynomial incidence over \(\mathbf Z\)。

这修复了 “moving monomial support” 的假问题。

## 27.2 What is not fixed

投影到：

\[
(G,K)
\]

后，primitive / Smith / source coefficients仍移动：

\[
P_i,Q_0,b_i,C_i,V,\ldots
\]

而 source interval：

\[
[L(x),R(x))
\]

也随这些 base data移动。

当前没有得到：

\[
\boxed{
(G,K)\in\Gamma_{10}
\cap
V_{\rm fixed}^{\rm proper}
}
\]

这样的 fixed proper incidence。

也没有得到：

\[
\boxed{
G^aK^b=c
}
\]

之类 nontrivial fixed character relation。

## 27.3 Eligibility

```text
POWER10_PROJECTION = DEFINED
FIXED_VARIETY = NO
MOVING_COEFFICIENTS = P_i,Q0,b_i,C_i,V,source interval
CHARACTER_RELATION = NONE_PROVED
ALGEBRAICIZATION_LOSS = SOURCE_INTERVAL_AND_ARITHMETIC_DECORATIONS_NOT_YET_FIXED
LAURENT_ELIGIBLE = NO
ESS_ELIGIBLE = NO
UNLIKELY_INTERSECTION_ELIGIBLE = NO
```

这些 `NO` 是资格判断，不是对相关理论的永久否定。

---

# 28. Fixedness Audit

| Object | current role | coordinate-artifact movement? | genuine arithmetic movement? |
|---|---|---:|---:|
| \(10^{m_3}\) | coefficient in old charts | YES; replace by \(YG\) | NO |
| \(10^{n_2}\) | coefficient in old charts | YES; replace by \(XGK\) | NO |
| \(G,K,X,Y\) | toric variables | NO | YES as power-ten orbit |
| \(J\) | DES index | NO | YES numeric depth, but decoration only |
| \(U\) | source radial coordinate | NO | YES |
| \(C_i\) | source direction | NO | YES |
| \(P_i,Q_0\) | primitive direction | NO | YES |
| q1 modulus \(2Kd_q\) | source image lattice | NO | YES arithmetic depth |
| Gaussian integral phase | historical chart choice | YES / noncanonical | NO canonical source meaning |

所以 R4 的 fixedness problem现在被精确定位为：

> **不是固定 monomial support，而是如何消除/压缩 genuine moving primitive-source coefficients，使 \((G,K)\) 落入 fixed proper incidence。**

---

# 29. Failed / Falsified Ideas

R3 正式退休：

1. \(J\) 作为顶层 branch architecture；
2. raw \(v_2,v_5\) depth splitting；
3. 把 q=1 \(\rho\)-coset当 canonical source fibre；
4. naked Gaussian initial form；
5. outer-minus 每个 carry value当新 cell；
6. “有限 valuation signature \(\Rightarrow\) semantic drop”；
7. “source completion 自动让 valuation 变 rigid”；
8. 从 algebraic codimension直接宣称 semantic codimension；
9. valuation atlas 继续无限细化；
10. historical theatre names作为 canonical cell IDs。

---

# 30. R3 Terminal Verdict

本轮同时取得：

\[
\boxed{
\texttt{FINITE\_SOURCE\_COMPLETED\_VALUATION\_ATLAS\_PROVED}
}
\]

qualifier：

\[
\boxed{
\textbf{FINITE COMBINATORIAL TYPES MODULO ARITHMETIC DEPTH}.
}
\]

并取得：

\[
\boxed{
\texttt{VALUATION\_ATLAS\_SEMANTICALLY\_SATURATED}.
}
\]

所以优先 terminal label 取后者，因为它决定 R4 architecture。

五个最高问题：

### Q1 — \(\mathfrak F_{\rm sem}\) 是否 finite？

\[
\boxed{\textbf{YES, modulo arithmetic depth.}}
\]

primary cell count：

\[
\boxed{5}.
\]

### Q2 — 485/95 是否都只是 cells？

\[
\boxed{\textbf{YES, at the source-completed master level.}}
\]

更精确：它们是 S0–S4 的 charts / arithmetic decorations / historical refinements。

### Q3 — \(J\) 是否彻底降为 saturation decoration？

\[
\boxed{\textbf{YES}.}
\]

### Q4 — source-completed valuation 是否产生 semantic dimension drop？

\[
\boxed{
\textbf{NO NEW DROP FROM THE VALUATION LAYER ITSELF}.
}
\]

### Q5 — 下一层缺少什么 information class？

\[
\boxed{
\texttt{SOURCE\_COMPLETED\_POWER10\_FIXED\_INCIDENCE\_EXTRACTION}.
}
\]

不是“更强 valuation theorem”。

---

# 31. Exact Remaining Unknowns

R3 之后真正未决：

1. 能否从 fixed master total space 消去足够多 moving primitive/Smith coordinates，得到对 \((G,K)\) 的 fixed proper incidence？
2. source section \(\kappa_{\rm src}\) 能否被 algebraicized/encoded 到该 fixed incidence中，而不丢失 interval、coprime与 q1 image-sublattice？
3. 是否能得到 cell-independent character relation：
   \[
   G^aK^b=c
   \]
   或 finite family of such relations？
4. 如果不能，是否存在另一种 fixed algebraic/exponential component language？
5. S4 的 moving carry是否在 global incidence extraction时完全被消去，还是成为 genuine exceptional component parameter？
6. S1 q=1 finite-index source sublattice是否在 global projection中产生 fixed congruence/character component？

---

# 32. R4 Attack Target

唯一授权 architecture：

\[
\boxed{
\textbf{SOURCE-COMPLETED POWER10 FIXED-INCIDENCE EXTRACTION}.
}
\]

建议 R4 目标写成：

> 从 source-completed master equations + \(\kappa_{\rm src}\) 出发，在不按 S0–S4 分裂研究 architecture 的前提下，构造一个 fixed total incidence \(\mathcal V\)，并证明所有 real source candidates 的 \((G,K)\in\Gamma_{10}\) 投影落入有限个 proper fixed components；若无法做到，则精确证明哪个 moving coefficient class 阻止 fixedness。

R4 不再研究：

- 更细 \(v_2/v_5\) fan；
- 更多 historical branch signatures；
- q=1 单独 Gaussian；
- outer-minus carry枚举；
- transition headroom；
- resonance successor sharpening。

---

# Machine-readable terminal block

```text
R3_TERMINAL_VERDICT=VALUATION_ATLAS_SEMANTICALLY_SATURATED

SOURCE_COMPLETION_FROZEN=YES
KAPPA_SRC_STATUS=CANONICAL

VALUATION_CARRIER_SET=DEPTH_FACE(g=0/g>0);RESONANCE_FACE(R=0/R!=0);D_CHAMBER(d<=-1,d=0,d=1,d>=2);H_R_SIGN_WHEN_NOT_FORCED;J_SATURATION_DECORATION;Q1_SOURCE_SUBLATTICE_DECORATION;ARCH_ACTIVE_FACE_DECORATION
CANONICAL_CELL_COUNT=5_PRIMARY
CELL_COUNT_FINITE_PROVED=YES_MODULO_ARITHMETIC_DEPTH
HISTORICAL_BRANCHES_QUOTIENTED=YES

J_ROLE=CANONICAL_DES_SATURATION_DECORATION
J_AS_ARCHITECTURE_VARIABLE=NO

Q1_CELL_STATUS=S1_DECORATED_EXCEPTIONAL_SUBCELL_WITH_FINITE_INDEX_U_SUBLATTICE
OUTER_MINUS_CELL_STATUS=S4_PRIMARY;NUMERIC_CARRY_DEPTH_UNBOUNDED_BUT_INITIAL_SUPPORT_FIXED

INITIAL_FORM_CLASSIFICATION=FINITE_INITIAL_FORM_TYPES_MODULO_DEPTH_PROVED
CELL_OVERLAP_COCYCLE=PROVED_IN_MASTER_PULLBACK_SOURCE_COMPLETED_CATEGORY

SEMANTIC_DIMENSION_DROP=NONE_NEW_FROM_VALUATION_LAYER
DROP_CELLS=NONE_WITH_NEW_R3_DROP
NO_DROP_CELLS=S0,S1,S2,S3,S4_AFTER_CELL_CONDITIONING
EXCEPTIONAL_CELLS=NONE_FOR_ATLAS_FINITENESS;Q1_IS_DECORATED_NOT_PRIMARY

VALUATION_SATURATION_COUNTERFAMILY=S3-R3-VSCF

POWER10_PROJECTION_STATUS=FIXED_TOTAL_SPACE__PROJECTION_NOT_YET_PROPER_FIXED
FIXED_INCIDENCE_STATUS=NO
LAURENT_ELIGIBILITY=NO
ESS_ELIGIBILITY=NO
UNLIKELY_INTERSECTION_ELIGIBILITY=NO

NEW_GLOBAL_RIGIDITY_CANDIDATE=SOURCE_COMPLETED_POWER10_FIXED_INCIDENCE_EXTRACTION

RETIRED_AFTER_R3=J_AS_BRANCH_ARCHITECTURE;RAW_VALUATION_DEPTH_SPLITTING;Q1_RHO_COSET_MASTER;NAKED_GAUSSIAN_INITIAL_FORM;OUTER_MINUS_CARRY_AS_CELL_SPLITTER;VALUATION_AS_RIGIDITY_MECHANISM

R4_ATTACK_TARGET=GAMMA10_X_KAPPA_SRC_FIXED_INCIDENCE_EXTRACTION
```

---

# Provenance Ledger

R3 主要读取并继承：

- `105_R1_Common_Obstruction_Reconstruction.md`
- `105_R2_Source_Section_Internalization.md`
- `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
- `95_R7_Transition_Source_Boundary_Bridge_Repair_or_Kill.md`
- `95_R8_g0_Smith_Reduced_Common_U_Three_Layer_Assault.md`
- `95_R9_Outer_Plus_No_Borrow_Projective_Smallness_Assault.md`
- `95_R10_Second_Architecture_Shock_Checkpoint_and_New_Invariant_Audit.md`
- `Fourth_85_R6_Gaussian_Source_Embedding.md`
- `strict_layer_A1_unified_moving_profile_terminal_campaign.md`
- `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`
- `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`
- `strict_layer_A1_exact_word_state_after_double_euclidean_campaign.md`
- `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`

本报告的 S3-R3-VSCF 由 companion script `105_R3_scripts/verify_s3_counterfamily.py` 用 exact integer algebra 验证。该计算只验证显式恒等式；finite atlas theorem 的 finiteness proof不是由有限枚举推出。
