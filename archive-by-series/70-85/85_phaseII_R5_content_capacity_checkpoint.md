# 第二个八五计划·第五轮
## Uniform Source-Chord Content Capacity × Moving Exponent Comparison × First-Five-Round Architecture Shock Checkpoint

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 第二个八五计划·第五轮  
**Completion criterion:** \(J=2\Longrightarrow\varnothing\)  
**Status:** checkpoint completed; \(J2\) remains open

---

# 0. Executive verdict

本轮得到的不是 height closure，也不是 height counterexample，而是一个严格的 **single-obstruction diagnosis**：

\[
\boxed{\texttt{R5\_CHECKPOINT\_VERDICT
=UNIFORMIZATION\_OBSTRUCTION\_EXACTLY\_IDENTIFIED}.}
\]

新的正结果是：

\[
\boxed{
D_\Lambda\mid
\mathcal C_{\rm src}(g,k,u,q)
:=
\frac{G^2u^2N_0}{4},
}
\]

其中

\[
\boxed{
N_0
=
4u^2G^2K^2-(GA+1)^2+2,
\qquad
A=2u+1.
}
\]

这是 **source-semantic、basepoint-independent** 的 primitive-content capacity theorem；R4 的
\(|p_3|\operatorname{Res}(Q,L)\) 中的巨大 basepoint growth 可以完全删除。

但与此同时，本轮证明 R4 的另一个量——chord parameter height
\[
H(a,b)=\max(|a|,|b|)
\]
——不是 source-invariant。改变 primitive isotropic basepoint / source basis / \(\mathbf P^1\) gauge 后，同一个 source point 的 parameter height 可以从巨大值压到 \(1\)。因此：

\[
\boxed{
\text{R4 representative packet 的巨大 }H_{\min}
\text{ 不能直接充当 moving source-height supply。}
}
\]

故当前唯一 principal obstruction 是：

\[
\boxed{
\texttt{UNIFORMIZATION\_OBSTRUCTION=BASEPOINT\_ARTIFACT}
}
\]

更精确地说：

\[
\boxed{
\textbf{PCS packet height 与 physical/source primitive height 之间
缺少 chart-independent / low-distortion transfer theorem。}
}
\]

这不是 `RESULTANT_GROWTH`；resultant 已 exact 化并去 artifact。

这也不是 `ODD_CONTENT_CAPACITY`；odd content 已 aggregate 控制。

这不是 `BAND_QUADRATIC_CANCELLATION` 的独立第二问题；在没有 controlled chart distortion 之前，
所谓 uniform quadratic coefficient \(A(g,k,u,q)\) 本身也随 gauge 改变，因此它属于同一个 principal
chart-height obstruction。

---

# 1. Frozen R1–R4 verdicts

本轮接受并不重新打开：

```text
THEOREM_A=FALSE
DISCRIMINANT_ALONE=OLD_INFORMATION_CLASS
CLASS_INTERFACE=NOT_VISIBLE
DESCENT_INTERFACE=NOT_VISIBLE

REAL_RADIAL_INCOMPATIBILITY=FALSE

PURE_SOURCE_LATTICE_DETERMINANT_INSUFFICIENT=TRUE

PCS_2_5=PROVED_ON_THE_AUDITED_CHORD_MODEL
FULL_PRIMITIVE_PACKET_GUILLOTINE=FALSE

R4_FIXED_FIBRE_CONTENT_DIVISOR=CORRECT
R4_ALL_G_HEIGHT_TRANSFER=OPEN
```

R4 的核心 bridge 保留：

\[
F_1=Qp_1-La,\qquad
F_2=Qp_2-Lb,\qquad
F_3=Qp_3,
\]

\[
D_\Lambda=\gcd(F_1,F_2,F_3),
\]

以及 fixed chart 中

\[
D_\Lambda\mid |p_3|\gcd(Q,L).
\]

R5 的任务是把这里的 chart constant exact 化并审计其 invariant content。

---

# 2. Canonical source coordinates

仍令

\[
G=10^g,\qquad
K=10^k,\qquad
H=\frac G2,
\]

\[
uq=G+1,\qquad
A=2u+1,\qquad
B=2G+q.
\]

source congruence为

\[
Bz+A\lambda\equiv0\pmod{2K}.
\]

取

\[
r_0\equiv-A^{-1}B\pmod{2K},
\]

并写 source-lattice basis coordinates

\[
\boxed{\lambda=r_0z+2Kn.}
\]

定义

\[
\boxed{
s_0:=\frac{B+Ar_0}{2K}\in\mathbb Z,
\qquad
t_0:=G+ur_0.
}
\]

于是

\[
C_1=s_0z+An,
\]

\[
T=t_0z+2uKn,
\]

\[
w=\frac{G^2}{2}z-uAc,
\]

\[
d_2=uc+Gw.
\]

利用 inherited determinant identity

\[
uB-GA=1
\]

可得到新的 exact normalization identity：

\[
\boxed{
At_0=2uKs_0-1.
}
\tag{R5-AT}
\]

这一式是 determinant exactization 的关键 cancellation。

---

# 3. Primitive integral source conic

不再使用带有明显 clearing artifact 的

\[
\Phi=16K^2\bigl(H^2C_1^2+w^2-Td_2\bigr).
\]

在 source lattice coordinates \((c,z,n)\) 中，exact root 本身已经是 integral ternary quadratic form：

\[
\boxed{
E(c,z,n)
=
H^2C_1^2+w^2-Td_2.
}
\]

展开得

\[
\boxed{
\begin{aligned}
E={}&
u^2A^2c^2\\
&+u\!\left(-AG^2+AGt_0-t_0\right)cz\\
&+2Ku^2(AG-1)cn\\
&+\frac{G^2}{4}
\left(G^2-2Gt_0+s_0^2\right)z^2\\
&+\frac{G^2}{2}
\left(As_0-2GKu\right)zn\\
&+\frac{G^2A^2}{4}n^2.
\end{aligned}}
\tag{R5-E}
\]

由于 \(G=10^g\)，所有系数均为整数。

## 3.1 Coefficient-content theorem

\[
\boxed{\operatorname{content}(E)=1.}
\]

证明只需检查任一假设整除全部系数的素数 \(p\)。

- \(p=2\) 不可能，因为 \(u^2A^2\) 为奇数；
- \(p=5\) 不可能，因为 \(u,A\) 均为 ten-unit；
- 若 \(p\mid u\)，则
  \[
  p\nmid \frac{G^2A^2}{4}
  \]
  因 \(\gcd(u,GA)=1\)；
- 若 \(p\mid A\)，则
  \[
  2Ku^2(AG-1)\equiv-2Ku^2\not\equiv0\pmod p.
  \]

因此没有素数能整除全部系数。

这一步把“source conic coefficient content”本身从 moving ambiguity 中删除。

---

# 4. Exact determinant

令 \(S_E\) 为 \(E\) 的 symmetric Gram matrix，即

\[
E(x)=x^TS_Ex.
\]

将 (R5-AT) 代入 determinant 后精确得到：

\[
\boxed{
\det S_E
=
-\frac{G^2u^2N_0}{16},
}
\tag{R5-DET}
\]

其中

\[
\boxed{
N_0
=
4u^2G^2K^2-(GA+1)^2+2.
}
\tag{R5-N0}
\]

这里 \(N_0\) 正是历史上已经出现的 moving square-class / Gaussian split quantity，
但本轮不使用其 class-group 信息；这里只使用它作为 source conic determinant 的 exact factor。

在当前 \(K\ge10\) 下，

\[
2uK>A=2u+1,
\]

所以

\[
2uGK>GA+1,
\]

进而

\[
\boxed{N_0>0.}
\]

此外：

\[
\boxed{N_0\equiv1\pmod2,\qquad N_0\equiv1\pmod5.}
\]

又由 \(G\equiv-1\pmod u\)、\(A\equiv1\pmod u\)：

\[
GA+1\equiv0\pmod u,
\]

故

\[
\boxed{N_0\equiv2\pmod u}
\]

而 \(u\) 为奇数，因此：

\[
\boxed{\gcd(N_0,u)=1.}
\tag{R5-N0U}
\]

---

# 5. Exact chord resultant theorem

考虑任意 ternary quadratic form

\[
Q_3(x)=x^TSx
\]

及 primitive isotropic basepoint \(p\)，\(Q_3(p)=0\)。

在一个 transverse plane \(x_3=0\) 上令

\[
Q(a,b):=Q_3(a,b,0),
\]

\[
L(a,b):=\mathcal B(p,(a,b,0)).
\]

对 binary quadratic \(Q\) 与 linear form \(L\) 的 homogeneous resultant，直接消元得到：

\[
\boxed{
\operatorname{Res}(Q,L)
=
-4p_3^2\det S.
}
\tag{R5-RES}
\]

这是 exact identity，不是 upper bound。

因此 R4 的 \(\mathcal R\) 不需要保持 black box。

---

# 6. Basepoint-dependence audit

## 6.1 R4 raw constant 确有巨大 artifact

R4 使用的 cleared form 为

\[
\Phi=16K^2E.
\]

所以

\[
\det S_\Phi
=
(16K^2)^3\det S_E
=
-256K^6G^2u^2N_0.
\]

由 (R5-RES)：

\[
\boxed{
|\operatorname{Res}(Q_\Phi,L_\Phi)|
=
1024K^6G^2u^2N_0\,p_3^2.
}
\tag{R5-RAW-RES}
\]

若再沿 R4 的

\[
D_\Lambda\mid |p_3|\operatorname{Res}(Q,L),
\]

则 raw capacity增长为

\[
\boxed{
1024K^6G^2u^2N_0\,|p_3|^3.
}
\]

这个 \(|p_3|^3\) 不是 source-semantic growth。

原因很直接：split conic 上有无限多个 primitive integral isotropic points；选择越来越高的 primitive point
作为 chord basepoint，可以使 \(|p_3|\) 无界。因此 raw capacity 可以只靠“换 basepoint”被任意放大。

所以：

\[
\boxed{
\texttt{R4\_RAW\_BASEPOINT\_CAPACITY
=COORDINATE\_ARTIFACT}.
}
\]

这不否定 R4 fixed-fibre theorem；它只说明 raw constant 不能用于 moving exponent comparison。

---

# 7. Canonicalization: primitive basepoint to \(e_3\)

任取 primitive source-lattice isotropic point \(p\in\mathbb Z^3\)。

因为 \(p\) primitive，存在

\[
U\in SL_3(\mathbb Z)
\]

把 \(e_3\) 送到 \(p\)。

在这个 unimodular source basis 中：

\[
\boxed{p=e_3,\qquad p_3=1.}
\]

unimodular change 不改变：

- source-lattice primitiveness；
- coordinate gcd/content；
- \(|\det S_E|\)。

于是取 transverse plane \(x_3=0\)，chord map 直接变为：

\[
\boxed{
F(a,b)=(-L(a,b)a,\,-L(a,b)b,\,Q(a,b)).
}
\tag{R5-CAN-CHORD}
\]

若 \(\gcd(a,b)=1\)，则

\[
\boxed{
D_\Lambda(a,b)
=
\gcd(Q(a,b),L(a,b)).
}
\]

再由 resultant divisibility：

\[
D_\Lambda\mid|\operatorname{Res}(Q,L)|.
\]

结合 (R5-DET)、(R5-RES)：

\[
\boxed{
D_\Lambda(a,b)
\mid
\frac{G^2u^2N_0}{4}.
}
\tag{R5-USCCC}
\]

这就是本轮的主 theorem：

## Theorem R5-USCCC — Uniform Source-Chord Content Capacity

\[
\boxed{
\mathcal C_{\rm src}(g,k,u,q)
=
\frac{G^2u^2N_0}{4}
}
\]

是 canonical source-semantic content capacity。

它：

- 不依赖 chord basepoint height；
- 不依赖 arbitrary affine chart scaling；
- 不含额外 \(H(a,b)^\eta\) 损失；
- 可取
  \[
  \boxed{\eta=0.}
  \]

因此 Question 1 的答案是：

\[
\boxed{\textbf{YES}.}
\]

R4 fixed-fibre content theorem 确实可以升级成 moving source-semantic theorem。

---

# 8. SNF / source-lattice index audit

source reconstruction matrix为

\[
M_{\rm src}
=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&r_0&2K
\end{pmatrix}.
\]

由于左上角已有 \(I_2\)，其 Smith normal form 立即为：

\[
\boxed{
\operatorname{SNF}(M_{\rm src})
=
\operatorname{diag}(1,1,2K).
}
\tag{R5-SNF}
\]

因此：

\[
[\mathbb Z^3:\Gamma_{\rm src}]=2K.
\]

最重要的是：

\[
\boxed{
\text{source-lattice index 本身没有任何 odd invariant factor。}
}
\]

所以 R3 的“finite-index lattice alone 不足”得到更具体的确认：
odd primitive content 的来源不是 lattice index，而是 conic incidence / determinant。

---

# 9. Two-prime vs odd content

由

\[
\mathcal C_{\rm src}
=
\frac{G^2}{4}\,u^2N_0
\]

以及 \(u,N_0\) 均为 ten-unit：

\[
\boxed{
D_{2,5}\mid\frac{G^2}{4}
=
2^{2g-2}5^{2g},
}
\tag{R5-D25}
\]

而去掉 \(2,5\) 后：

\[
\boxed{
D_{\rm odd}\mid u^2N_0.
}
\tag{R5-DODD}
\]

因此：

```text
ODD_CONTENT_CAPACITY=PROVED
```

且这是 aggregate theorem，不需要 odd-prime-by-odd-prime campaign。

---

# 10. Full-primitive feedback

R4 已给同一 \((g,k,u,q)=(5,3,11,9091)\) packet 内的 full-primitive survivor：

\[
(a,b)=(6300650477551,318813),
\]

并且

\[
D_\Lambda=52175200000000000.
\]

其中：

\[
v_{11}(D_\Lambda)=3.
\]

但 decontent 后 full primitive/common-\(V\) 仍 PASS。

所以 full primitive 的作用不能写成：

\[
p\mid u\Longrightarrow p\nmid D_\Lambda.
\]

相反，某些情况下恰恰需要足够的 raw content 去吸收 raw coordinate 中的 \(u\)-adic load，
decontent 后才恢复 primitive block。

因此本轮不能把 \(u^2\) 从 (R5-DODD) 中统一删除。

结论：

\[
\boxed{
\text{full primitive does not supply a uniform further reduction of }
\mathcal C_{\rm odd}.
}
\]

但这不再是 obstruction，因为 \(u^2N_0\) 已是一个 exact moving capacity。

---

# 11. Moving growth of intrinsic content capacity

由

\[
N_0
<
4u^2G^2K^2
\]

得到：

\[
\boxed{
\mathcal C_{\rm src}
<
G^4u^4K^2.
}
\tag{R5-CAP-UP}
\]

利用

\[
u=\frac{G+1}{q}
\]

得到：

\[
\boxed{
\mathcal C_{\rm src}
<
G^4K^2\left(\frac{G+1}{q}\right)^4.
}
\tag{R5-CAP-UQ}
\]

若用 exponent bookkeeping：

\[
K=G^\kappa,\qquad q=G^\zeta
\]

仅作为 scale notation，则 proven upper exponent 为：

\[
\boxed{
\delta
\le
8+2\kappa-4\zeta+o(1).
}
\]

在当前 live notation

\[
k=2g-\ell,\qquad
K=G^2\,10^{-\ell},
\]

即

\[
\kappa=2-\frac{\ell}{g},
\]

所以：

\[
\boxed{
\delta
\le
12-2\frac{\ell}{g}-4\zeta+o(1).
}
\tag{R5-DELTA}
\]

最危险 content regime 是：

- \(q\) 尽可能小；
- \(u\) 尽可能大；
- \(k\) 尽可能大 / \(\ell\) 尽可能小。

这完成 Task N/O 的 content-side worst-regime audit。

但这还不能形成 closure，因为 supply-side \(\gamma\) 尚未成为 invariant quantity。

---

# 12. Exact packet-spacing theorem

R4 packet：

\[
a\equiv rb\pmod M
\]

写成：

\[
\boxed{a=rb+M\ell.}
\]

若

\[
\alpha<\frac ab<\beta,
\qquad
W=\beta-\alpha,
\]

则等价于：

\[
\boxed{
\frac{b(\alpha-r)}M
<
\ell
<
\frac{b(\beta-r)}M.
}
\tag{R5-SP}
\]

若再有 \(\gcd(b,M)=1\)，则：

\[
\gcd(a,b)
=
\gcd(M\ell,b)
=
\gcd(\ell,b).
\]

所以给定 \(b\)，exact admissibility是：

\[
\boxed{
\exists\ell\in\mathbb Z:
\quad
\frac{b(\alpha-r)}M<\ell<
\frac{b(\beta-r)}M,
\quad
\gcd(\ell,b)=1.
}
\tag{R5-SP-EXACT}
\]

这就是 R4 certificate 实际执行的 floor/root comparison 的抽象形式。

---

# 13. Width-only lower bound is false

设

\[
x_b:=\frac{b(\alpha-r)}M,
\qquad
\omega_b:=\frac{bW}{M}.
\]

忽略 coprimality 时，candidate 存在当且仅当区间

\[
(x_b,x_b+\omega_b)
\]

命中一个整数。

因此真正控制 first hit 的不是 \(W\) 单独，而是 moving phase：

\[
\boxed{
\{x_b\}
=
\left\{
\frac{b(\alpha-r)}M
\right\}.
}
\]

特别地，任何希望仅由 \(M,W\) 推出

\[
b\gtrsim\frac MW
\]

的 theorem 都是假的。

反例是结构性的：对任意 \(M\) 与任意小 \(W>0\)，让 band 包含某个

\[
r+M\ell_0.
\]

则 \(b=1\) 已满足 packet，且可以让 \(W\to0\)。

所以：

\[
\boxed{
\texttt{WIDTH\_ONLY\_PACKET\_HEIGHT=FALSE}.
}
\]

R4 五个 fibres 的巨大 minimum denominator来自 **packet phase 与 band position 的特殊对齐**，
不是 width 本身。

---

# 14. Correct position variable is \(b\)-dependent

Task L 提出的 static projective distance 可作为诊断，但不足以控制全部 denominator。

正确的 exact phase quantity是：

\[
\boxed{
\Delta_b
=
\min\{m-x_b:m\in\mathbb Z,\ m>x_b\}.
}
\]

在不考虑 coprimality时：

\[
\boxed{
b\text{ admits a packet-band hit}
\iff
\Delta_b<\frac{bW}{M}.
}
\tag{R5-PHASE}
\]

再加上命中整数 \(\ell\) 与 \(b\) coprime，得到 reduced hit。

因此 all-\(g\) height theorem 真正需要控制：

\[
\boxed{
\left\{
\frac{b(\alpha-r)}M
\right\}
}
\]

这一 moving rotation/Diophantine phase，而不是只估计 \(M\) 与 \(W\)。

当前 R1–R4 没有这种 uniform phase theorem。

---

# 15. Representative packet-height data

R4 的五个 \(g=5\) representative fibres 的 exact minimum \(H_{\min}\) 仍完全有效，
但只对 **R4 选定的 chord gauge** 有效。

| fibre \((g,k,u,q)\) | \(M\) | band width \(W\) | exact \(H_{\min}\) | old \(|p_3|\) → canonical | canonical \(|\mathcal R|=\mathcal C_{\rm src}\) | known \(D_\Lambda\) (first / largest relevant) | smallest known \(\mathfrak H_{\rm rad}\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \((5,1,11,9091)\) | 50,000 | \(1.605625450836\!\times10^{-3}\) | 224,277,651,577 | 34,314,889,578,218,925,533,528,307,745,537 → 1 | 144,809,773,608,500,302,500,000,000 | 80,000,000 / 80,000,000 | \(7.55248\times10^{43}\) † |
| \((5,3,11,9091)\) | 50,000 | \(4.654724341434\!\times10^{-6}\) | 5,982,784,950,483 | 3,392,919,501,447,241,941,637 → 1 | 1,464,098,399,773,608,500,302,500,000,000 | 800,000,000,000 / 52,175,200,000,000,000 | \(2.84424\times10^{31}\) * |
| \((5,4,11,9091)\) | 50,000 | \(1.647236502727\!\times10^{-6}\) | 20,939,904,412,893 | 283,813,447,632,039,758,139,971 → 1 | 146,409,998,399,773,608,500,302,500,000,000 | 80,000,000,000,000 / 80,000,000,000,000 | \(1.06006\times10^{40}\) † |
| \((5,1,9091,11)\) | 50,000 | \(2.128636184343\!\times10^{-9}\) | 297,757,093 | 61,389,166,937,996,021,134,115,696,297,424,344,064,603 → 1 | 67,620,961,718,444,921,111,495,115,702,500,000,000 | 80,000,000 / 80,000,000 | \(1.48974\times10^{56}\) † |
| \((5,3,9091,11)\) | 250,000 | \(3.774851955087\!\times10^{-10}\) | 538,232,869 | 2,906,493,992,266,186,268,677,700,308,668,281,928,657 → 1 | 683,040,093,197,183,235,311,111,495,115,702,500,000,000 | 4,000,000,000,000 / 4,000,000,000,000 | \(1.18826\times10^{56}\) † |

† 该数字来自 first PCS-band hit；first hit 未通过 full primitive/common-\(V\)。  
* 该数字来自 R4 已知 full-primitive/common-\(V\) survivor，是当前该 representative fibre 中更危险的已知 full-deep witness。

这张表说明两件相反的事实：

1. fixed chart 中 packet separation 极强；
2. old \(|p_3|\) 同样极端巨大，说明该 chart 本身已经带有巨量 coordinate distortion。

因此不能把第 1 列的 Archimedean gain 与第 2 种 artifact 分开计算后宣布 exponent victory。

---

# 16. Why parameter height is not source-semantic

这是本轮 architecture shock 的核心。

设某个 source rational point 在某个 \(\mathbf P^1\) chart 中参数为 primitive pair

\[
(a,b),\qquad \gcd(a,b)=1.
\]

存在

\[
V\in SL_2(\mathbb Z)
\]

把

\[
(1,0)
\]

送到

\[
(a,b).
\]

在新的 integral projective gauge 中，同一个 source point 的 parameter coordinate 就是

\[
(1,0),
\]

因此：

\[
\boxed{H_{\rm parameter}=1.}
\]

也就是说：

\[
\boxed{
H(a,b)\text{ 可以被 fibre/candidate-dependent unimodular gauge 任意重标定。}
}
\]

所以“packet parameter height 很大”只有在 **预先固定且 distortion 可控的 canonical chart**
中才可能转化成 physical primitive height。

R4 五个 \(H_{\min}\) 的 exactness 不受影响；受影响的是它们的 **moving invariant interpretation**。

---

# 17. Raw quadratic height audit

R4 fixed fibre 中，

\[
F_c,\qquad F_{C_2}
\]

确为 quadratic forms；在避开各自 zero direction 的 closed sub-band 上，
固定 fibre 可以取

\[
A_{\rm fibre}>0
\]

使

\[
\mathcal F_{\rm rad}(a,b)
\ge
A_{\rm fibre}H(a,b)^2.
\]

因此 fixed-fibre asymptotic statement

\[
H\to\infty
\Longrightarrow
\mathfrak H_{\rm rad}\to\infty
\]

仍正确。

但 under moving source-basis / basepoint change：

- \(H(a,b)\) 改变；
- quadratic coefficients 改变；
- band 在 \(\mathbf P^1\) 上的 Euclidean width 改变；
- \(A_{\rm fibre}\) 也改变。

因此当前没有 source-invariant的

\[
\boxed{
A(g,k,u,q)H_{\min}^2
}
\]

可与 \(\mathcal C_{\rm src}\) 比较。

这不是第二个独立 gap，而是和第 16 节同一个 chart distortion。

故：

```text
RAW_QUADRATIC_HEIGHT=PARTIAL
```

---

# 18. Moving exponent comparison

content side 已经 exact：

\[
\eta=0,
\]

\[
D_\Lambda\le\mathcal C_{\rm src}
<
G^4u^4K^2.
\]

但 supply side 当前没有合法的 source-invariant \(\gamma\)：

\[
H_{\min}\gtrsim G^\gamma
\]

只在 R4 representative gauges 上有 sample exponent，没有 all-\(g\) theorem，
且 \(H_{\min}\) 本身随 \(SL_2(\mathbb Z)\) gauge 改变。

所以：

\[
\boxed{
(2-\eta)\gamma-\delta
}
\]

目前不是一个 well-defined source-semantic comparison。

因此：

\[
\boxed{
\texttt{MOVING\_EXPONENT\_COMPARISON=UNRESOLVED}.
}
\]

不是 `UNFAVORABLE`，因为没有证明 intrinsic physical height 供应不足。

也不是 `FAVORABLE`，因为 representative parameter exponents 不能升级为 invariant proof。

---

# 19. Strongest countermodel ledger

本轮没有发现

\[
\mathfrak H_{\rm rad}<1
\]

的 full-primitive band-compatible exact-root state。

当前最危险已知 witness 仍为 R4 full survivor：

```text
FIBRE = (g,k,u,q) = (5,3,11,9091)
PARAMETER_R4_CHART = (6300650477551,318813)

EXACT_ROOT = PASS
SOURCE_LATTICE = PASS
RADIAL_BAND = PASS

PCS_2 = PASS
PCS_5 = PASS

FULL_PRIMITIVE = PASS
COMMON_V = PASS
REGULAR = PASS

PACKET_HEIGHT_R4_CHART = 6300650477551

D_LAMBDA_R4_CHART =
52175200000000000

RAW_QUADRATIC_HEIGHT_R4_CHART =
2853755768752139196292937373282372569022591680600800000000000

OLD_BASEPOINT_p3 =
-3392919501447241941637

OLD_RAW_RESULTANT =
69036271144208011595582882335838105323937083605990770831335547381760000000000000000000000000000

OLD_RAW_CONTENT_CAPACITY =
234234510672382861693001273671673037441119197198602414904830874417791810554636554078341120000000000000000000000000000

CANONICAL_INTRINSIC_CONTENT_CAPACITY =
1464098399773608500302500000000

c =
2844241425759278313791310157183552723

C2 =
54695636408717919553598977546465994745062629

c/G =
2844241425759278313791310157183552723 / 100000

C2/(G^2 K) =
54695636408717919553598977546465994745062629 / 10000000000000

H_RAD =
2844241425759278313791310157183552723 / 100000

REAL_COMMON_U = PASS
INTEGER_COMMON_U = FAIL
COPRIME_COMMON_U = FAIL
FULL_SOURCE_LIFT = FAIL
```

注意：

`D_LAMBDA_R4_CHART` 与 `CANONICAL_INTRINSIC_CONTENT_CAPACITY`
属于不同 chord gauges，不能把前者的数值小于后者误写成同-chart divisibility proof。
canonical theorem 保证的是 **canonical adapted chart 中的 content** 被 \(\mathcal C_{\rm src}\) 控制。

本 witness 的作用仍只是：

\[
\boxed{
\text{full primitive + PCS + band 可以存活，}
\quad
\text{但 actual common-}U\text{ 因 absolute height 失败。}
}
\]

它不 falsify uniform height theorem。

---

# 20. Small-height counterexample guillotine

R4 representative exact search：

```text
SMALL_HEIGHT_FULL_PRIMITIVE_COUNTERMODEL=NOT_FOUND
```

R5 没有得到新的 \(\mathfrak H_{\rm rad}<1\) witness。

因此按纪律：

```text
UNIFORM_HEIGHT_TRANSFER=OPEN
INTEGER_COMMON_U_CANDIDATE=NOT_REACHED
RADIAL_ARCHITECTURE_FALSIFIED=NO
```

不能启动 integer-common-\(U\) campaign。

---

# 21. Information-class audit

当前真正存在五类信息：

1. **projective root information**  
   exact conic \(E=0\)。

2. **radial band information**  
   \[
   1/10<\rho<10.
   \]

3. **PCS local content information**  
   \(p=2,5\) valuation synchronization及 packet。

4. **full primitive odd-content information**  
   不能删除整个 packet，但读取 raw odd depth minus decontent depth。

5. **Archimedean absolute height information**  
   common-\(U\) digit windows。

R5 的 content theorem确实联合了：

\[
\text{projective conic determinant}
+
\text{primitive content}
\]

两个 information classes。

R4 packet-band theorem则联合：

\[
\text{PCS}
+
\text{Archimedean band}.
\]

所以 R1–R4 不是纯粹把同一个 invariant 换语言。

但当试图把两条链最终相乘时，出现了一个 **model/gauge interface**：

\[
\boxed{
\text{parameter height}
\not\equiv
\text{source physical height}.
}
\]

这使当前 closure quantity 不是 invariant。

---

# 22. Connection with 75: architecture shock

这一 obstruction 不是完全新的。

75-R5 已经把 USSPAL/source-height route 的 bottleneck 压到：

```text
source-integral splitting-frame distortion
+ low-height allowed-ruling basepoint
```

且没有 certified：

```text
EXACT_LOW_HEIGHT_ALLOWED_RULING_BASEPOINT
TOTAL_JOINT_COST_G_EXPONENT_IMPROVEMENT
```

随后 75 的 frozen transverse chart 被证明存在 \(G/4\) 级 intrinsic barrier；
但当时也明确 **没有** 证明所有 birational source charts 都有同一 barrier。

R5 现在从相反方向重新撞到同一件事：

\[
\boxed{
\textbf{缺少 chart-independent quantitative transfer
between }\mathbf P^1\textbf{ height and source height.}
}
\]

因此本 checkpoint 必须判：

\[
\boxed{
\texttt{R1\_R4\_ARCHITECTURE=LOOPING}
}
\]

这里 `LOOPING` 的精确含义不是“R1–R4 没有新数学”；
而是：

> R5 的最终唯一未闭合接口已经回到 75 明确留下、且当前 theorem stack 未解决的 source-chart distortion bottleneck。

所以不应把它包装成“再做五轮同类 exponent estimate”。

---

# 23. R1–R5 architecture autopsy

```text
R1:
Killed:
  ambient square nonrepresentation;
  discriminant-only closure.
Surviving interface:
  source-compatible absolute radial digit lift.

R2:
Killed:
  real radial incompatibility.
Surviving interface:
  primitive absolute height inside the decade band.

R3:
Killed:
  finite-index lattice determinant as a standalone obstruction.
Surviving interface:
  PCS at p=2,5 -> projective residue packets -> parameter-height pressure.

R4:
Killed:
  whole-packet full-primitive guillotine.
Surviving interface:
  fixed-fibre chord-content divisor + exact packet-band first-hit height.

R5:
New proved:
  primitive integral source conic E;
  exact determinant;
  exact chord resultant;
  canonical intrinsic content capacity;
  SNF;
  aggregate odd-content capacity;
  exact phase form of packet spacing.
Killed:
  raw |p3|Res as intrinsic moving capacity;
  width-only M/W denominator theorem;
  interpretation of R4 parameter H_min as source-semantic moving height.
Current verdict:
  the only remaining factor is controlled canonical-chart / source-height distortion.
```

搜索空间在 R1–R5 内确实严格收缩：

\[
\boxed{\text{YES}.}
\]

但 continuation space 不再是新的 primitive-height subproblem，
而是回到了一个历史 source-chart distortion interface。

所以“是否只是换语言循环”的答案是：

\[
\boxed{
\text{前四轮不是；R5 终端接口发生 historical loop。}
}
\]

---

# 24. Terminal ledger

```text
J2_STATUS =
OPEN

R1_R4_ARCHITECTURE =
LOOPING

CHORD_CONTENT_THEOREM =
CORRECTED

BASEPOINT_DEPENDENCE =
STRUCTURAL

INTRINSIC_CONTENT_CAPACITY =
PROVED

RESULTANT_GROWTH =
EXACT

ODD_CONTENT_CAPACITY =
PROVED

PACKET_HEIGHT_LOWER_BOUND =
PARTIAL

UNIFORM_PACKET_HEIGHT =
OPEN

RAW_QUADRATIC_HEIGHT =
PARTIAL

MOVING_EXPONENT_COMPARISON =
UNRESOLVED

UNIFORM_HEIGHT_TRANSFER =
OPEN

SMALL_HEIGHT_FULL_PRIMITIVE_COUNTERMODEL =
NOT_FOUND

INTEGER_COMMON_U_CANDIDATE =
NOT_REACHED

FULL_COMMON_U_COUNTERMODEL =
NOT_FOUND

COMMON_U_EXTINCTION =
OPEN

UNIFORMIZATION_OBSTRUCTION =
BASEPOINT_ARTIFACT
# precise meaning:
# source-chart / projective-height distortion;
# R4 H_min is gauge-dependent and has no current invariant transfer to physical height.

R5_CHECKPOINT_VERDICT =
UNIFORMIZATION_OBSTRUCTION_EXACTLY_IDENTIFIED
```

`CHORD_CONTENT_THEOREM=CORRECTED` 表示“R4 theorem 正确但其 moving constant 被严格 canonicalize/strengthen”，
不是说 R4 fixed-fibre proof 为假。

---

# 25. Answers to the three mandatory questions

## Question 1

> R4 fixed-fibre content bound 能否改造成 source-semantic uniform bound？

\[
\boxed{\textbf{YES}.}
\]

而且得到 exact invariant：

\[
\boxed{
D_\Lambda
\mid
\frac{G^2u^2N_0}{4}.
}
\]

basepoint factor 被完全删除。

---

## Question 2

> PCS packet × radial band 的 moving rational height 是否增长得比 primitive-content capacity 更快？

\[
\boxed{\textbf{NO}.}
\]

这里的 NO 是严格的 checkpoint 含义：

> **当前 theorem stack 不能把这个命题合法表述成 source-invariant exponent comparison。**

R4 chart 中的 representative answer 是“高度非常大”；但同一 source point 的
\(\mathbf P^1\) parameter height 可被 unimodular re-gauging 压到 \(1\)。

所以不能从现有 \(H_{\min}\) 宣布：

\[
H_{\min}^2>\mathcal C_{\rm src}
\]

是 source-semantic theorem。

这不是证明 physical primitive height 增长更慢，而是证明 **当前 supply variable 选错了 gauge**。

---

## Question 3

> 第二个八五 R1–R5 的 primitive-height architecture 是否值得直接进入第二组五轮？

\[
\boxed{\textbf{NO}.}
\]

原因不是该方向已经被 counterexample 杀死，而是：

1. content side 已经完成；
2. 唯一剩余接口是 source-chart distortion；
3. 该接口与 75 已冻结的 quantitative source-chart bottleneck 同类；
4. 在没有新的 invariant height gauge 前，再做 packet/resultant/exponent table 会重复历史 loop。

因此不应预先承诺 R6–R10 五轮。

---

# 26. Unique R6 route

虽然 Question 3 为 NO，按本轮 route-selection rule 仍允许且只允许一个 **repair-or-kill R6**：

\[
\boxed{
\textbf{R6:
Canonical Source-Height Gauge
× PCS Pullback Distortion
× Chart-Invariant Height Transfer Audit}.
}
\]

R6 只攻击：

\[
\boxed{\texttt{BASEPOINT\_ARTIFACT}.}
\]

它必须二选一。

### R6-A — repair

构造一个由 source data 预先决定的 canonical chart \(\Phi_\tau\)，并证明：

\[
H_{\rm src}
\asymp_{\rm controlled}
H_{\Phi_\tau}^{2}
\]

或足够强的 one-sided quantitative transfer，同时把 PCS packet pullback 到该 chart，
得到 all-\(g\) phase/height lower bound。

只有这样才重新授权 primitive-height architecture。

### R6-B — kill

证明任何 natural/source-canonical chart 都必须支付与 packet gain 同阶或更大的 distortion，
或者证明 PCS packet height 可在 low-distortion gauges 中系统 collapse。

则：

\[
\boxed{
\texttt{HEIGHT\_ARCHITECTURE\_CURRENT\_MECHANISM=DEAD}
}
\]

并 architecture reset。

R6 禁止再研究：

- resultant；
- new packet modulus tables；
- odd-prime content；
- more fixed fibres；
- generic discriminant；
- generic small-zero theorems。

---

# 27. Final checkpoint sentence

第二个八五前五轮真正压出的 quantitative statement 不是

\[
\text{height supply}>\text{content capacity},
\]

而是：

\[
\boxed{
\underbrace{
D_\Lambda\mid \frac{G^2u^2N_0}{4}
}_{\text{content capacity 已 invariant}}
\qquad\text{versus}\qquad
\underbrace{
H_{\min}^{\rm chord}
}_{\text{尚非 invariant}}.
}
\]

所以本轮的 death-or-closure line 已经非常明确：

\[
\boxed{
\textbf{先给 packet height 一个 source-semantic gauge，
否则不能再谈 exponent domination。}
}
\]

---

# 28. Artifact / certificate

本报告配套：

```text
85_phaseII_R5_content_capacity_checkpoint_certificate.py
85_phaseII_R5_content_capacity_checkpoint_certificate.txt
```

certificate exact 验证：

1. source conic coefficient expansion；
2. determinant identity；
3. chord resultant identity；
4. 五个 representative fibres 的 primitive coefficient content \(=1\)；
5. \(N_0\) ten-unit 与 \(\gcd(N_0,u)=1\)；
6. canonical content capacity；
7. old basepoint \(p_3\) inflation；
8. source reconstruction SNF。

```text
FLOAT_GATE_DECISIONS=0
CERTIFICATE_STATUS=PASS
```
