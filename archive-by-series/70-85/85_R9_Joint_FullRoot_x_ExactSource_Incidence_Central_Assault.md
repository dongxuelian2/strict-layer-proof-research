# 85 第九轮：Joint Full-Root × Exact Source-Incidence Central Assault

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 85-R9  
**Status:** Central Assault completed; no J2 closure certificate issued  
**Primary certificate:** `85_R9_joint_incidence_certificate.py` / `85_R9_joint_incidence_certificate.txt`

---

# 1. Executive Summary

本轮第一次把

\[
\mathcal V_{\rm root}
\quad\text{与}\quad
\mathcal I_{\rm exact-source}
\]

放进同一组 PRE_ROOT 坐标中，而不是先 root、再 source，或先 source、再 root。

核心结论分成五层。

## 1.1 Joint functional 确实存在，而且非常低复杂度

固定

\[
G=10^g,\qquad H=G/2,\qquad K=10^k,
\]

\[
uq=G+1,\qquad A=2u+1,\qquad B=2G+q,
\]

并采用 R7/R8 已认证的 PRE_ROOT chart：

\[
C_3=c,
\]

\[
C_2=Ac+H\lambda,
\]

\[
2KC_1=Bz+A\lambda,
\]

\[
T=Gz+u\lambda,
\]

\[
w=GHz-uAc,
\]

\[
d_2=uc+Gw.
\]

则 full root / sphere 正好变成

\[
\boxed{
\mathscr F(c,z,\lambda)
:=
\frac{G^2}{16K^2}(Bz+A\lambda)^2
+
\left(\frac{G^2z}{2}-uAc\right)^2
-
(Gz+u\lambda)
\left(uc+G\left(\frac{G^2z}{2}-uAc\right)\right)
=0.
}
\tag{JRI}
\]

清除固定正因子 \(16K^2\) 后：

\[
\boxed{
\Phi
:=16K^2\mathscr F
=G^2(Bz+A\lambda)^2+16K^2w^2-16K^2Td_2.
}
\tag{JRI-clr}
\]

这里没有除以 moving factor，也没有引入 extraneous root。

而且：

\[
\deg_c\mathscr F=
\deg_z\mathscr F=
\deg_\lambda\mathscr F=2,
\qquad
\deg_{\rm total}\mathscr F=2.
\]

所以 R9-S1 完成。

## 1.2 但 source master 在该 chart 上自动坍缩，不提供新 codimension

定义 primitive/full-word quantities：

\[
P_1=GHC_1,
\qquad
P_2=uGC_2,
\qquad
P_3=uc,
\qquad
Q_0=P_2+d_2,
\]

\[
V=uGH.
\]

当前 denominator profile 为

\[
b_1=u,
\qquad
b_2=H,
\qquad
b_3=GH.
\]

定义去 common-\(U\) 后 numerator word：

\[
\mathcal A^\sharp
:=KG^3C_1+GC_2+c,
\]

以及 denominator word：

\[
\mathcal B
:=uG^3+HG^2+GH.
\]

直接 symbolic elimination 得到：

\[
\boxed{
V\mathcal A^\sharp-Q_0\mathcal B
=\frac{G^5z}{4}(uq-G-1).
}
\tag{MASTER-RES}
\]

因此 Exact Resonance 外层恒等式 \(uq=G+1\) 一旦施加，立即有

\[
\boxed{V\mathcal A^\sharp=Q_0\mathcal B.}
\]

更强地，因

\[
\mathcal B=VB,
\]

故

\[
\boxed{\mathcal A^\sharp=BQ_0.}
\tag{MASTER-AUTO}
\]

这说明 R8 所谓“完整 root-independent source shell”中的 non-root master，在当前 joint chart 内**不是第二条独立等式**；它已经被 PRE_ROOT affine rows 与 \(uq=G+1\) 吸收。

这是本轮最重要的 source-side structural diagnosis：

\[
\boxed{
\text{exact source incidence在此 chart 上主要剩 inequalities / congruences / gcd，}
\text{不再提供新的 algebraic codimension。}
}
\]

## 1.3 universal signed-incidence theorem 被 exact source counterexample 击穿

R8 的 PLCF 给出一整族 \(\mathscr F<0\) source-shell states。

R9 主动搜索正号后，在同一 live outer base

\[
(g,k,u,q)=(4,1,73,137)
\]

找到两个**完整 root-independent exact-source-shell** 点，甚至具有相同

\[
(c,z,U)=(147,1,7),
\]

而只相差 \(\lambda\)：

### Negative state

\[
\lambda=25969,
\]

\[
(C_1,C_2,T)=(191879,129866609,1905737),
\]

\[
w=48422543,
\qquad
d_2=484225440731,
\]

\[
\boxed{
\mathscr F=-22\,830\,046\,786\,898<0.
}
\tag{N-EX}
\]

### Positive state

\[
\lambda=25989,
\]

\[
(C_1,C_2,T)=(192026,129966609,1907197),
\]

相同

\[
w=48422543,
\qquad
d_2=484225440731,
\]

且

\[
\boxed{
\mathscr F=681\,051\,684\,745\,842>0.
}
\tag{P-EX}
\]

两点均有唯一 common-scale witness：

\[
\boxed{U=7.}
\]

因此

\[
\boxed{
\texttt{JOINT\_SIGN=CHANGES\_SIGN}.
}
\]

固定符号 closure architecture 正式 falsified。

## 1.4 zero surface 进入 source domain 的实内部；真正障碍回到整数/平方层

在上述固定

\[
(c,z)=(147,1)
\]

上，\(\mathscr F\) 是关于 \(\lambda\) 的开口向上的二次式。

它的正实根为

\[
\lambda_+\approx25969.649171914785.
\]

而相邻 source-shell lattice points

\[
25969,
\qquad25989
\]

分别给负号与正号。

所以：

\[
\boxed{
\mathcal V_{\rm root}(\mathbb R)
\text{ 穿过 exact-source domain 的连续 relaxation。}
}
\]

真正未解决的不是 real boundary disjointness，而是：

\[
\boxed{
\text{该 crossing 上是否存在满足全部 integrality / square / divisibility 的整数点。}
}
\]

## 1.5 这一整数问题严格回到旧 NRSEC

把 \(\mathscr F\) 收集为 \(\lambda\) 二次式：

\[
\boxed{
\mathscr F
=a\lambda^2+b\lambda+d,
}
\]

其中

\[
\boxed{
a=\frac{G^2A^2}{16K^2}>0,
}
\]

\[
\boxed{
b=\frac{G^2ABz}{8K^2}-ud_2,
}
\]

\[
\boxed{
d=\frac{G^2B^2z^2}{16K^2}+w^2-Gzd_2.
}
\]

令

\[
\Delta_\lambda=b^2-4ad.
\]

历史 NRSEC 的 reduced discriminant 是

\[
\Delta_0
=u^2K^2d_2^2-AH^2(Aw^2+zd_2).
\]

R9 exact symbolic bridge 为

\[
\boxed{
\Delta_\lambda=\frac{\Delta_0}{K^2}.
}
\tag{DISC-BRIDGE}
\]

并且坐标变换本身就是

\[
\boxed{
C_1=\frac{Bz+A\lambda}{2K},
\qquad
\lambda=\frac{2KC_1-Bz}{A}.
}
\tag{AFFINE-BRIDGE}
\]

所以 R9 的 full-root conic 与历史 CZ-Q / NRSEC conic 不是相似对象，而是**严格同一个对象的可逆仿射重写**。

source domain 并没有改变判别式，也没有把 square condition 变成新的 source-restricted invariant。

因此本轮触发用户预设 kill criterion：

```text
R9_TERMINAL_VERDICT=OLD_NRSEC_INTERFACE_REAPPEARS
```

全局状态：

```text
JOINT_ROOT_SOURCE_INCIDENCE=UNKNOWN
J2_STATUS=OPEN
```

本轮没有合法依据宣称 EMPTY、THIN 或 LARGE。

---

# 2. R8 Frozen Verdict

永久冻结：

```text
SOURCE_PROJECTION_PROGRAMME=EXHAUSTED
ROOT_INDEPENDENT_MISSING_GATE=NONE
R8_TERMINAL_VERDICT=
SOURCE_PROJECTION_EXHAUSTED_FULL_ROOT_IS_NEXT_INDEPENDENT_GATE
```

R8 的 PLCF 已通过全部当前认证的 root-independent source shell：

- outer J2 identities；
- PRE_ROOT Euclidean rows；
- primitive reducedness；
- exact common-\(V\) profile；
- denominator legality；
- non-root full-word master；
- numerator digit windows；
- common-\(U\) existence；
- \(\gcd(U,V)=1\)。

其第一次失败进入 full-root layer。

R9 不再搜索 missing source gate。

---

# 3. Why Both Side-Programmes Are Retired

## 3.1 root-local programme 已耗尽

R1–R5 已经退休：

- floor/carry；
- residual quantum；
- \(2/5\)-adic capacity；
- odd-prime allocation；
- source-cut as second gate；
- canonical one-dimensional root order；
- 单独 common-scale / endpoint-jump obstruction。

本轮不恢复这些路线。

## 3.2 source-projection programme 已耗尽

R6–R8 已经证明 PRE_ROOT source image 具有 large fibres，并最终构造 PLCF 通过全部当前 root-independent source shell。

R9 的新结论 (MASTER-AUTO) 进一步解释为什么继续 source-side mining 很难产生 algebraic codimension：

\[
V\mathcal A^\sharp-Q_0\mathcal B
\]

在当前 chart 上只剩 outer resonance residual

\[
\frac{G^5z}{4}(uq-G-1).
\]

也就是说：完整 non-root decimal master 已经被现有 affine chart 吸收。

因此两个侧翼都没有独立 gate 可以继续挖。

---

# 4. Joint PRE_ROOT Coordinates

本轮使用：

\[
\boxed{C_3=c,}
\]

\[
\boxed{C_2=Ac+H\lambda,}
\]

\[
\boxed{2KC_1=Bz+A\lambda,}
\]

\[
\boxed{T=Gz+u\lambda.}
\]

并定义：

\[
\boxed{h=qHz-Ac,}
\]

\[
\boxed{m=Ah-Gz,}
\]

\[
\boxed{r=Hh-uc,}
\]

\[
\boxed{w=GHz-uAc,}
\]

\[
\boxed{d_2=uc+Gw.}
\]

Outer determinant identities：

\[
\boxed{qA-B=2,}
\]

\[
\boxed{uB-GA=1.}
\]

由此还可得到一个有用的简化：

\[
\boxed{m=HBz-A^2c.}
\]

当前 regular live branch 采用：

\[
g\ge4,
\qquad
u>1,
\qquad
q>1,
\qquad
S_R<0,
\qquad
w>0,
\]

以及已有 deficiency/frontier 条件；R9 不重新证明这些 outer closures。

---

# 5. Exact Reconstruction Formulas

上述 chart 恰好重构 R7/R8 全部 PRE_ROOT rows：

\[
\boxed{c=2r-qw,}
\tag{PRE-1}
\]

\[
\boxed{d_2=2ur-w,}
\tag{PRE-2}
\]

\[
\boxed{Ar-w=mH,}
\tag{PRE-3}
\]

\[
\boxed{GKC_1=AC_2+m,}
\tag{PRE-4}
\]

\[
\boxed{uC_2+w=HT,}
\tag{PRE-5}
\]

\[
\boxed{2uKC_1=AT+z.}
\tag{PRE-6}
\]

另外定义

\[
D:=HC_2+r,
\]

则：

\[
\boxed{KP_1=Q_0+D,}
\]

以及：

\[
\boxed{Q_0-P_3=GHT.}
\]

这些都是 PRE_ROOT / source-side exact identities；没有使用 sphere。

---

# 6. Full Root Functional

full-root sphere：

\[
H^2C_1^2+w^2=Td_2
\]

直接代入 chart 得到 (JRI)。

定义：

\[
\boxed{
\mathscr F
:=H^2C_1^2+w^2-Td_2.
}
\]

则：

\[
\boxed{
\mathscr F=0
\iff
\text{full sphere/root holds on the frozen PRE_ROOT state}.
}
\]

同时历史 primitive-root polynomial：

\[
Q_{\rm prim}
:=AH^2C_1^2-2uKd_2C_1+Aw^2+zd_2
\]

满足 exact identity：

\[
\boxed{Q_{\rm prim}=A\mathscr F.}
\tag{ROOT-EQUIV}
\]

证明只使用 PRE-6：

\[
2uKC_1=AT+z.
\]

因此本轮没有把 root shadow 当作新的 source gate。

更进一步：

\[
\boxed{
P_1^2+P_2^2+P_3^2-Q_0^2
=G^2\mathscr F.
}
\tag{PRIM-RES}
\]

所以 \(\mathscr F\) 同时是 primitive sphere residual 的精确归一化。

---

# 7. Algebraic Simplification / Factorization

## 7.1 compact controlled form

首选形式是：

\[
\boxed{
\mathscr F
=
\frac{G^2}{16K^2}(Bz+A\lambda)^2
+w^2
-(Gz+u\lambda)d_2.
}
\tag{F-COMPACT}
\]

其中

\[
w=\frac{G^2z}{2}-uAc,
\]

\[
d_2=uc+Gw.
\]

这比完全展开的几十项 polynomial 更保留 source semantics。

## 7.2 quadratic in \(\lambda\)

\[
\boxed{
\mathscr F
=
\frac{G^2A^2}{16K^2}\lambda^2
+
\left(
\frac{G^2ABz}{8K^2}-ud_2
\right)\lambda
+
\left(
\frac{G^2B^2z^2}{16K^2}+w^2-Gzd_2
\right).
}
\tag{F-LAMBDA}
\]

注意 \(w,d_2\) 不依赖 \(\lambda\)。

这使 joint root geometry 极其明确。

## 7.3 no useful new factor

施加 \(uq=G+1\) 后，\(\mathscr F\) 不出现新的 universal source-sign factor，例如：

\[
q-1,
\quad
q+4,
\quad
u-1,
\quad
K-1,
\quad
c-z,
\quad
\lambda-z
\]

均不作为合法 universal factor 出现。

唯一大规模 cancellation 发生在 non-root master，而不是 full-root functional。

---

# 8. PLCF Regression

R8-PLCF：

\[
g=5+22t,
\qquad
G=10^g,
\]

\[
K=10,
\qquad
u=11,
\qquad
q=\frac{G+1}{11},
\]

\[
A=23,
\qquad
c=z=1,
\qquad
\lambda=3.
\]

代入本轮 \(\mathscr F\)，exact symbolic regression 恢复：

\[
\boxed{
\mathscr F_{\rm PLCF}
=-\frac{P(G)}{193600},
}
\]

其中

\[
\boxed{
P(G)
=47871G^4+3159440G^3-577600G^2
-1614236800G-12321865600.
}
\]

R8 已证明在相关 \(G\ge10^5\) 上

\[
P(G)>0.
\]

故：

\[
\boxed{\mathscr F_{\rm PLCF}<0.}
\]

R9 regression：

```text
PLCF_REGRESSION=PASS
```

---

# 9. Exact Source-Incidence Domain

本节定义 current regular negative J2 branch 的 root-independent exact source domain：

\[
\boxed{
\mathcal D_{\rm src}(G,K,u,q)
\subset\mathbb Z^3_{(c,z,\lambda)}.
}
\]

## 9.1 outer conditions

\[
G=10^g,
\qquad
K=10^k,
\]

\[
\boxed{uq=G+1,}
\]

\[
A=2u+1,
\qquad
B=2G+q,
\]

\[
\boxed{\gcd(A,10)=1.}
\]

当前 live regular scope：

\[
g\ge4,
\quad
u>1,
\quad
q>1,
\quad
w>0,
\quad
\gcd(A,d_2)=1.
\]

## 9.2 lattice / integrality conditions

\[
\boxed{c,z,\lambda\in\mathbb Z_{>0},}
\]

\[
\boxed{\gcd(cz\lambda,10)=1,}
\]

\[
\boxed{Bz+A\lambda\equiv0\pmod{2K}.}
\tag{LAT}
\]

然后

\[
C_1=\frac{Bz+A\lambda}{2K}
\]

必须为正整数。

## 9.3 positivity / orientation

要求：

\[
C_1,C_2,c,T,h,m,r,w,d_2>0.
\]

当前 negative resonance orientation：

\[
\boxed{w=GHz-uAc>0.}
\]

## 9.4 ten-unit PRE_ROOT package

\[
\boxed{\gcd(hmrwTd_2,10)=1.}
\]

## 9.5 exact common-\(V\) profile

令

\[
V=uGH.
\]

要求：

\[
\boxed{\gcd(C_1,u)=1,}
\]

\[
\boxed{\gcd(C_2,H)=1,}
\]

\[
\boxed{\gcd(c,GH)=1.}
\]

于是：

\[
\gcd(V,P_1)=GH,
\]

\[
\gcd(V,P_2)=uG,
\]

\[
\gcd(V,P_3)=u,
\]

从而 denominator blocks 精确恢复为：

\[
\boxed{
(b_1,b_2,b_3)=(u,H,GH).
}
\]

## 9.6 primitive normalization

即使 sphere 尚未施加，当前 source shell 仍保留 primitive candidate normalization：

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\tag{PRIM}
\]

## 9.7 non-root master

要求实际 full-word master：

\[
V\mathcal A^\sharp=Q_0\mathcal B.
\]

但由 (MASTER-AUTO)，在本 chart 上这已经自动成立。

所以它不再提供额外 equality codimension。

## 9.8 exact numerator digit/common-\(U\) gate

minimal A1 semantics 下，第一 numerator block 的位数可以由 \(a_1=UC_1\) 自动定义；真正固定的是第二、第三块。

令

\[
x_2:=10^{n_2-1}=\frac{G^2K}{10},
\]

\[
x_3:=10^{n_3-1}=\frac G{10}.
\]

则：

\[
\boxed{
\frac{G^2K}{10}\le UC_2<G^2K,
}
\tag{DIG2}
\]

\[
\boxed{
\frac G{10}\le Uc<G.
}
\tag{DIG3}
\]

精确整数 interval：

\[
\boxed{
U_{\rm lo}
=
\max\left(
\left\lceil\frac{x_2}{C_2}\right\rceil,
\left\lceil\frac{x_3}{c}\right\rceil,
1
\right),
}
\]

\[
\boxed{
U_{\rm hi}
=
\min\left(
\left\lfloor\frac{10x_2-1}{C_2}\right\rfloor,
\left\lfloor\frac{10x_3-1}{c}\right\rfloor
\right).
}
\]

source lift 当且仅当存在

\[
\boxed{
U\in[U_{\rm lo},U_{\rm hi}]\cap\mathbb Z_{>0}
}
\]

且

\[
\boxed{\gcd(U,V)=1.}
\tag{COMMON-U}
\]

连续投影只给 ratio strip：

\[
\boxed{
\frac{GK}{10}
<
\frac{C_2}{c}
<
10GK.
}
\tag{SRC-RATIO}
\]

而：

\[
\frac{C_2}{c}=A+H\frac{\lambda}{c}.
\]

这正是 source domain 的一个显式半代数边界，但不是新的 equation。

## 9.9 actual blocks

一旦有合法 \(U\)：

\[
\boxed{a_i=UC_i,}
\]

\[
\boxed{b_1=u,\quad b_2=H,\quad b_3=GH.}
\]

上述 gcd package 保证逐项 reducedness。

---

# 10. Freedom / Dimension Ledger

固定 outer tuple

\[
(G,K,u,q).
\]

## 10.1 PRE_ROOT affine chart

自由变量：

\[
(c,z,\lambda).
\]

即实 relaxation 为三维。

所有

\[
C_1,C_2,T,h,m,r,w,d_2
\]

均是派生 affine functions。

## 10.2 source equations

关键发现：non-root master 自动化为 (MASTER-AUTO)。

其余 source conditions是：

- open inequalities；
- fixed congruence sublattice；
- gcd conditions；
- existential common-\(U\) interval。

这些在实维数意义上不再减少一维。

故：

\[
\boxed{
\dim_{\mathbb R}\mathcal D_{\rm src}^{\rm rel}=3
}
\]

在存在 interior 的 chamber 中成立。

## 10.3 加 full root

\[
\mathscr F=0
\]

是一条 homogeneous quadratic equation。

所以 generic affine real dimension：

\[
\boxed{3-1=2.}
\]

由于 \(\mathscr F\) 对 \((c,z,\lambda)\) homogeneous degree 2，projectivize 后变成：

\[
\boxed{
\text{projective conic / curve-like object，维数 }1.
}
\]

## 10.4 arithmetic layer

integrality / congruence / gcd 可能进一步把整数点变 thin，甚至 empty。

但 R9 没有证明这种 arithmetic thinning。

因此：

```text
REAL_JOINT_GEOMETRY=AFFINE_SURFACE / PROJECTIVE_CONIC
ARITHMETIC_JOINT_GEOMETRY=UNKNOWN
```

---

# 11. Sign Decomposition

## 11.1 PLCF negative family

R8-PLCF：

\[
\mathscr F<0.
\]

## 11.2 R7 original box regression

固定：

\[
(g,k,u,q)=(4,1,73,137),
\]

\[
z=1,
\quad
1\le c\le5000,
\quad
1\le\lambda\le2000,
\]

并加入本轮补全的：

- exact common-\(V\) profile；
- primitive normalization；
- non-root master；
- exact common-\(U\) / coprime witness。

得到：

```text
SOURCE_SHELL=10284
F<0         =10284
F=0         =0
F>0         =0
```

这解释了为什么 PLCF-guided negative sign conjecture 看起来非常自然。

## 11.3 active positive search falsifies universal sign

扩大 \(\lambda\) 后，在完全相同 outer base 上得到 (N-EX) 与 (P-EX)。

更强地，固定：

\[
(c,z)=(147,1),
\]

扫描：

\[
1\le\lambda\le40000
\]

的 exact source-shell points：

```text
TOTAL=1393
F<0=1266
F>0=127
F=0=0
```

因此：

\[
\boxed{
\texttt{JOINT_SIGN=CHANGES_SIGN}.
}
\]

本轮不得再尝试全域 sum-of-positive-pieces decomposition。

---

# 12. Source Boundary Geometry

N/P 反例具有相同：

\[
(c,z,U)=(147,1,7).
\]

相邻 source lattice points：

\[
\lambda_-=25969,
\]

\[
\lambda_+=25989.
\]

满足：

\[
\mathscr F(\lambda_-)<0<\mathscr F(\lambda_+).
\]

对应 real zero：

\[
\lambda_*\approx25969.649171914785.
\]

因此 root zero locus 并非位于 source interval 外。

这直接排除一种新的“joint boundary disjointness”全局 closure：

\[
\boxed{
\text{continuous source domain 与 root surface真实相交。}
}
\]

R5 的 old root-order route 也不需要重启：这里没有 global real order collision，问题已经下降为 lattice hit / discriminant square。

---

# 13. Discriminant / Square Analysis

## 13.1 R9 \(\lambda\)-discriminant

由 (F-LAMBDA)：

\[
\Delta_\lambda=b^2-4ad.
\]

exact simplification：

\[
\boxed{
\Delta_\lambda
=\frac1{K^2}
\left[
 u^2K^2d_2^2
-AH^2(Aw^2+zd_2)
\right].
}
\]

故：

\[
\boxed{
\Delta_\lambda=\Delta_0/K^2.
}
\]

## 13.2 exact NRSEC coordinate equivalence

历史 CZ-Q：

\[
\boxed{
AH^2C_1^2-2uKd_2C_1+Aw^2+zd_2=0.
}
\tag{CZ-Q}
\]

由

\[
C_1=\frac{Bz+A\lambda}{2K}
\]

代入后，恰得到

\[
A\mathscr F=0.
\]

反向：

\[
\lambda=\frac{2KC_1-Bz}{A}.
\]

这是一个固定 outer base 上的可逆 affine change。

所以：

\[
\boxed{
\text{R9 discriminant geometry = old NRSEC discriminant geometry exactly.}
}
\]

## 13.3 integral root conditions

若

\[
\Delta_0=R_0^2,
\]

则旧 root formula：

\[
\boxed{
C_1=
\frac{uKd_2\pm R_0}{AH^2}.
}
\]

必须同时满足：

\[
\boxed{AH^2\mid uKd_2\pm R_0,}
\]

以及 joint chart 返回 source lattice：

\[
\boxed{A\mid2KC_1-Bz,}
\]

\[
\boxed{\lambda=(2KC_1-Bz)/A>0,}
\]

\[
\boxed{\gcd(\lambda,10)=1,}
\]

再检查 \((c,z,\lambda)\in\mathcal D_{\rm src}\)。

这没有产生新的 source-restricted discriminant；它只是把旧 NRSEC 的 reconstruction filter 写回 joint coordinates。

---

# 14. Integer Incidence

## 14.1 two exact source-shell sign witnesses

### N witness

Outer：

\[
G=10000,
\ K=10,
\ u=73,
\ q=137,
\ A=147,
\ B=20137.
\]

Joint coordinate：

\[
(c,z,\lambda)=(147,1,25969).
\]

Common scale：

\[
U=7.
\]

Actual numerator blocks：

\[
(a_1,a_2,a_3)
=(1343153,909066263,1029).
\]

Denominator blocks：

\[
(b_1,b_2,b_3)
=(73,5000,50000000).
\]

全部逐项 reduced。

Actual numerator word：

\[
13431539090662631029.
\]

Actual denominator word：

\[
73500050000000.
\]

且 exact master ratio：

\[
\frac{A_{\rm word}}{B_{\rm word}}
=
\frac{UQ_0}{V}.
\]

但：

\[
\mathscr F<0.
\]

### P witness

同一 outer / \(c,z,U\)，仅：

\[
\lambda=25989.
\]

Actual numerator blocks：

\[
(a_1,a_2,a_3)
=(1344182,909766263,1029),
\]

同一 denominator blocks。

Actual numerator word：

\[
13441829097662631029.
\]

且：

\[
\mathscr F>0.
\]

因此 source arithmetic lattice 本身不会固定 \(\mathscr F\) 的符号。

## 14.2 no Class-Z found in certified fixed-base scans

见 §17。

这只是 finite census，不是 global theorem。

---

# 15. Modular Incidence

优先测试：

\[
5,8,16,20,25,40,80.
\]

在固定 live base 的 exact source shell 中，均可找到：

\[
\boxed{\mathscr F\equiv0\pmod m}
\]

的合法 source-shell state。

具体 certificate 首个 witness：

- mod \(8,16\)：\((c,z,\lambda,U)=(9,1,49,407)\)；
- mod \(5\)：\((11,1,29,683)\)；
- mod \(25\)：\((11,1,49,407)\)；
- mod \(20\)：\((21,1,49,407)\)；
- mod \(40\)：\((21,1,69,289)\)；
- mod \(80\)：\((21,1,109,183)\)。

因此：

\[
\boxed{
\text{这些固定小模数都不能仅凭 exact source residue class 立即排除 }\mathscr F=0.
}
\]

这不否认更复杂的 joint congruence 可能存在；只说明用户指定的 first-line fixed-modulus route没有出现直接 closure。

---

# 16. High / Boundary / Reverse Chamber Audit

## 16.1 universal algebra

JRI、MASTER-AUTO、DISC-BRIDGE 都不依赖 high / boundary / reverse 的后续 tail presentation。

所以 exact algebraic diagnosis是 branch-independent 的：

\[
\boxed{
\text{source master不增 codimension；full root回到同一个 NRSEC conic。}
}
\]

## 16.2 reverse / low-\(k\) chamber

明确的 N/P exact sign-change counterexamples 位于：

\[
g=4,
\qquad
k=1,
\qquad
\ell=2g-k=7.
\]

这是当前 reverse / low-\(k\) 区域。

因此 universal sign theorem 至少在 reverse chamber彻底失败。

## 16.3 boundary / high reconnaissance

额外 exact sampling 在：

\[
(g,k,u,q)=(6,6,101,9901)
\]

等 boundary base，以及

\[
(g,k,u,q)=(7,8,11,909091)
\]

等 high base 上，抽到的合法 source-shell states 均为负号。

但这只是 reconnaissance：

\[
\boxed{
\text{R9没有证明 boundary/high chamber 固定负号。}
}
\]

由于 joint conic 已严格回到 NRSEC，本轮不允许继续 coefficient mining 来把这种数值现象包装成新 architecture。

---

# 17. Exact Computational Census

所有 computation 使用 exact integer / rational arithmetic。

## 17.1 R7 original box upgraded to full source shell

Outer：

\[
(g,k,u,q)=(4,1,73,137).
\]

Box：

\[
z=1,
\]

\[
1\le c\le5000,
\qquad
1\le\lambda\le2000.
\]

完整 source-shell survivors：

\[
\boxed{10284.}
\]

分类：

\[
\boxed{
N=10284,
\qquad
Z=0,
\qquad
P=0.
}
\]

## 17.2 sign-change line

固定：

\[
(c,z)=(147,1),
\qquad
1\le\lambda\le40000.
\]

source-shell states：

\[
\boxed{1393.}
\]

其中：

\[
\boxed{N=1266,}
\]

\[
\boxed{P=127,}
\]

\[
\boxed{Z=0.}
\]

唯一观察到的 sign transition 紧邻：

\[
25969\to25989.
\]

## 17.3 Class-Z root-conditional scans

为了搜索 genuine root intersection，可以合法使用历史 NRSEC 在 **假设 full root** 下导出的 \(Uz\) 上界；该上界没有被塞回 source domain。

采用 rigorous rational majorant：

\[
\eta<2.598=1299/500.
\]

于是 root candidate 必满足：

\[
Uz<\frac{2\eta u}{K}+\frac{2uA}{G}.
\]

因 \(U\ge1\)，可得到 finite \(z\)-ceiling。

### Base A

\[
(g,k,u,q)=(4,1,73,137).
\]

\[
z<40.077,
\qquad z\le40.
\]

检查：

\[
\boxed{35350}
\]

个通过 linear/positivity/regular package 的 \((c,z)\) cells。

全部 \(\Delta_0\ge0\)，但：

\[
\boxed{\Delta_0\text{ square count}=0.}
\]

故该 fixed base：

\[
\boxed{\text{Class Z count}=0.}
\]

### Base B

\[
(g,k,u,q)=(4,2,73,137).
\]

\[
z<5.93928,
\qquad z\le5.
\]

检查：

\[
\boxed{3350}
\]

cells；square discriminant：

\[
\boxed{0.}
\]

### Base C

\[
(g,k,u,q)=(5,1,11,9091).
\]

\[
z<5.72066,
\qquad z\le5.
\]

检查：

\[
\boxed{76522}
\]

cells；square discriminant：

\[
\boxed{0.}
\]

## 17.4 interpretation

这些 fixed-base emptiness results是真实 exact certificate，但它们不能升级为 R9 global closure，因为搜索核心正是：

\[
\Delta_0=\square
+
\text{old integral-root divisibility}
+
\text{source reconstruction}.
\]

这正是 old NRSEC interface。

所以它们被归档为 regression / reconnaissance，而不是新 theorem architecture。

---

# 18. Counterexamples to Sign/Thinness Conjectures

## 18.1 universal negative sign — DISPROVED

由 (P-EX)：

\[
\boxed{\mathscr F>0}
\]

在完整 exact source shell 中成立。

所以：

```text
SIGNED_JOINT_INCIDENCE_FUNCTIONAL_ESTABLISHED=NO
```

## 18.2 real boundary exclusion — DISPROVED

同一 source-compatible \(\lambda\)-line 上有 N/P transition。

因此 zero surface 穿入 source real domain。

## 18.3 fixed small modulus exclusion — NOT AVAILABLE

mod \(5,8,16,20,25,40,80\) 均有 source states satisfying

\[
\mathscr F\equiv0.
\]

## 18.4 THIN conjecture — NOT PROVED

虽然 \(\mathscr F=0\) projectivize 后是 conic/curve-like，但用户定义的 THIN 要求：

\[
\mathcal J
\subset
\bigcup_{i=1}^{O(1)}\mathcal C_i
\]

并给出 explicit arithmetic families。

R9 没有这样的 theorem。

仅仅说“一个二次方程降一维”不满足 THIN 定义。

## 18.5 LARGE conjecture — NOT PROVED

R9 没有构造任何 genuine infinite family 同时满足：

- exact source shell；
- \(\mathscr F=0\)；
- full root integer conditions。

因此也不能判 LARGE。

---

# 19. Old-NRSEC Firewall

本轮 firewall 触发是 exact，而不是“看起来像”。

链条为：

\[
\boxed{
\mathscr F(c,z,\lambda)=0
}
\]

\[
\Updownarrow
\]

\[
\boxed{
Q_{\rm prim}(C_1)=0
}
\]

通过

\[
C_1=\frac{Bz+A\lambda}{2K}.
\]

然后：

\[
\boxed{
\Delta_\lambda=\Delta_0/K^2.
}
\]

所以 square locus 完全相同。

与此同时，source master 没有生成新的 equation，而是：

\[
\boxed{
V\mathcal A^\sharp-Q_0\mathcal B
\equiv0
}
\]

on \(uq=G+1\)。

因此 exact source domain 进入 reduction 的方式只剩：

- interval；
- congruence；
- gcd；
- post-root reconstruction legality。

它没有改变 root discriminant object。

符合 prompt kill criterion：

```text
R9_NEW_ARCHITECTURE=NO
R9_TERMINAL_VERDICT=OLD_NRSEC_INTERFACE_REAPPEARS
```

必须停止继续把该 conic 当作新 R9 route 深挖。

---

# 20. Source-Semantics Firewall

本轮没有为了 simplification 丢掉：

- common-\(U\)；
- \(\gcd(U,V)=1\)；
- actual DIG2/DIG3；
- exact common-\(V\) profile；
- primitive normalization；
- regular \(d_A=1\)；
- non-root full-word master。

相反，MASTER-AUTO 是在完整 source semantics下证明的。

第一 numerator block 没有被“忘掉”；minimal A1 semantics允许在合法 \(U\) 后定义

\[
a_1=UC_1,
\qquad
n_1=\ell(a_1),
\]

因此不必人为冻结一个额外 \(I_1\) window。

root-derived objects：

- sphere；
- \(Q_{\rm prim}\)；
- \(\Delta_0\)；
- NRSEC \(Uz\) root bound；

全部只在 ROOT side 使用，没有被伪装成 source gate。

所以：

```text
JOINT_NORMAL_FORM=SOURCE_VALID
SOURCE_SEMANTICS_FIREWALL=PASS
```

---

# 21. Joint Incidence Status

定义：

\[
\mathcal J
:=
\mathcal V_{\rm root}
\cap
\mathcal D_{\rm src}.
\]

当前能够严格说的是：

### Real geometry

\[
\boxed{
\mathcal V_{\rm root}(\mathbb R)
\cap
\mathcal D_{\rm src}^{\rm rel}
\ne\varnothing
}
\]

在 fixed live base 的连续 relaxation 中已经由 sign crossing 证明。

### Integer geometry

没有发现 certified Class Z point in tested bases，但没有 global exclusion。

因此：

```text
JOINT_ROOT_SOURCE_INCIDENCE=UNKNOWN
```

不能写 EMPTY，因为没有 global proof。

不能写 THIN，因为没有 explicit arithmetic thin-family theorem。

不能写 LARGE，因为没有 genuine infinite full-root-compatible family。

最准确的结构描述是：

\[
\boxed{
\text{real intersection survives;
integer intersection reduces exactly to old NRSEC square/divisibility problem.}
}
\]

---

# 22. R9 Terminal Verdict

最终判决：

```text
R8_FROZEN_VERDICT=PASS

JOINT_PRE_ROOT_COORDINATES=PROVED
EXACT_JOINT_ROOT_FUNCTIONAL=PROVED
PLCF_REGRESSION=PASS
EXACT_SOURCE_DOMAIN=EXPLICIT
SOURCE_MASTER_CODIMENSION_GAIN=NONE

JOINT_SIGN=CHANGES_SIGN
REAL_SOURCE_BOUNDARY_EXCLUSION=FALSE
FIXED_SMALL_MODULUS_CLOSURE=NOT_FOUND

DISCRIMINANT_BRIDGE=
DELTA_LAMBDA_EQUALS_DELTA0_OVER_K2

JOINT_ROOT_SOURCE_INCIDENCE=UNKNOWN
J2_STATUS=OPEN

R9_SUCCESS_LEVEL=
R9-S1_PLUS_EXPLICIT_DOMAIN_BELOW_S2

R9_TERMINAL_VERDICT=
OLD_NRSEC_INTERFACE_REAPPEARS
```

解释：

- S1 达成：低复杂度 exact joint functional 已建立；
- exact source domain 也已显式化；
- 但 S2 所要求的“新的 joint restriction”没有出现；
- 相反，source master被证明在该 chart 上自动冗余；
- sign route 被 exact counterexample 击穿；
- root arithmetic 严格回到 NRSEC。

这是一项有价值的 negative result，因为它阻止 85 在中央区域再次把旧 discriminant architecture 误命名为新路线。

---

# 23. R10 Attack Target

由于本轮触发：

```text
R9_TERMINAL_VERDICT=OLD_NRSEC_INTERFACE_REAPPEARS
```

因此 **R10 不应执行“继续解 \(\Delta_0\)”或“再磨 \(\mathscr F\) 系数”**。

尤其禁止：

- 对同一 \(\Delta_0\) 做新的 prime-by-prime square analysis；
- 把 \(\lambda\)-quadratic 当成新 discriminant campaign；
- 继续 PLCF-guided sign coefficient mining；
- 重新启动 R5 one-dimensional root-order；
- 仅靠更多 fixed-base NRSEC census 宣称结构进展。

如果 85 必须继续到第十轮，那么唯一合理的 R10 目标应改为：

\[
\boxed{
\textbf{NRSEC-Reappearance Architecture Shock Audit}
}
\]

核心问题不是“怎样处决当前 conic”，而是：

\[
\boxed{
\text{为什么 exact source incidence 在 PRE_ROOT chart 中只留下 inequalities/gcd，}
\text{并让 full root 精确退化回 old NRSEC？}
}
\]

R10 若要产生新 architecture，必须找到一个满足以下条件的对象：

1. 同时读取 full root 与 exact source semantics；
2. 不是 \(\Delta_0\) 的可逆重参数化；
3. 不是 sphere-derived source shadow；
4. 真正改变 arithmetic incidence class，而不是只换坐标；
5. 能解释或利用 source master 的 automaticity (MASTER-AUTO)。

若做不到，应结束当前 85 central architecture，而不是继续局部 patch。

---

# Appendix A — Exact identities frozen by R9

\[
qA-B=2,
\qquad
uB-GA=1.
\]

\[
C_3=c,
\quad
C_2=Ac+H\lambda,
\quad
2KC_1=Bz+A\lambda,
\quad
T=Gz+u\lambda.
\]

\[
h=qHz-Ac,
\quad
m=Ah-Gz=HBz-A^2c,
\]

\[
r=Hh-uc,
\quad
w=GHz-uAc,
\quad
d_2=uc+Gw.
\]

\[
c=2r-qw,
\quad
d_2=2ur-w,
\]

\[
Ar-w=mH,
\quad
GKC_1=AC_2+m,
\]

\[
uC_2+w=HT,
\quad
2uKC_1=AT+z.
\]

\[
P_1=GHC_1,
\quad
P_2=uGC_2,
\quad
P_3=uc,
\quad
Q_0=P_2+d_2.
\]

\[
KP_1=Q_0+D,
\qquad
Q_0-P_3=GHT.
\]

\[
\mathcal B=VB,
\qquad
\mathcal A^\sharp=BQ_0.
\]

\[
\mathscr F
=H^2C_1^2+w^2-Td_2.
\]

\[
Q_{\rm prim}=A\mathscr F.
\]

\[
P_1^2+P_2^2+P_3^2-Q_0^2=G^2\mathscr F.
\]

\[
\Delta_\lambda=\Delta_0/K^2.
\]

---

# Appendix B — Exact computational files

Generated in this round:

```text
85_R9_Joint_FullRoot_x_ExactSource_Incidence_Central_Assault.md
85_R9_joint_incidence_certificate.py
85_R9_joint_incidence_certificate.txt
```

Certificate terminal lines:

```text
JOINT_ROOT_SOURCE_INCIDENCE=UNKNOWN
R9_SUCCESS_LEVEL=R9-S1_PLUS_EXPLICIT_DOMAIN_BELOW_S2
R9_TERMINAL_VERDICT=OLD_NRSEC_INTERFACE_REAPPEARS
CERTIFICATE_STATUS=PASS
```

---

# Appendix C — Provenance ledger

Primary inherited sources used:

```text
85_R8_PLCF_Countermodel_Differential_and_SourceProjection_Termination.md
85_R8_PLCF_gate_differential.py
85_R7_J2_Endpoint_Modular_Jump_and_CommonScale_Integer_Extinction.md
85_R7_endpoint_jump_diagnostic.py
85_R6_N0_Split_Family_x_FullWord_Source_Projection_Rearchitecture.md
A1_J2_NRSEC_Report.md
strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md
85_R1_R5_First_Five_Round_Closure_Checkpoint.md
```

The new R9 certificate independently checks the key symbolic bridges rather than trusting notation transfer.
