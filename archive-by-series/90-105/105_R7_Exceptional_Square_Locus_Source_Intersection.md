# 105-R7：Exceptional Square-Locus Source Intersection × Factor-Pair Allocation × Fixed Additive Gap × Primitive/Smith Divisor Rigidity × Kill-or-Lift

**项目：** 三项十进制拼接平方和问题  
**范围：** Strict Layer — \(A_1\)-only  
**轮次：** 105-R7  
**唯一允许路线：** Exceptional Square-Locus Source Intersection  
**归档状态：** R1–R6 frozen；R7 完成一次严格的 factor-pair / divisor-gate 重构与 falsification audit，但**没有**得到 S3/S4 square-source empty theorem，也**没有**找到 S3/S4 source-legal square lift。

---

# 1. Executive Verdict

R7 的最重要结果不是再次计算 discriminant，而是把 R6 的 exceptional square cover 精确分成了三个不同层次：

\[
\boxed{
\text{rational square cover}
\;\supsetneq\;
\text{integral divisor lift}
\;\supseteq\;
\text{primitive/source lift}.
}
\]

R6 冻结 theorem 说，在 genuine source profile 的 nondegenerate fibre 上：

\[
\mathscr D=W^2\in\mathbf Q^2
\iff
\exists (P_1,Q_0)\in\mathbf Q^2
\]

满足 sphere + full master。R7 证明：**不能把**

\[
S_+\mid \mathcal N
\]

作为这个 rational equivalence 的附加条件。它只在要求 \(P_1,Q_0\in\mathbf Z\) 时出现。因此本轮把“Divisor-Constrained Discriminant”严格改名为：

\[
\boxed{
\textbf{Divisor-Constrained Integral Lift Gate}.
}
\]

R7 同时得到一个比原计划更强的 exact factor bridge。取 canonical complementary root

\[
W:=\mathcal BQ_0-\mathcal AP_1,
\qquad
\mathcal C=\mathcal AQ_0-\mathcal BP_1,
\]

定义

\[
S_+=Q_0+P_1,
\qquad
S_-=Q_0-P_1,
\]

\[
R_-=W-\mathcal C,
\qquad
R_+=W+\mathcal C.
\]

则不是“可能”而是恒等地：

\[
\boxed{
R_-=(\mathcal B-\mathcal A)S_+,
\qquad
R_+=(\mathcal A+\mathcal B)S_-.
}
\tag{R7-BRIDGE}
\]

因此 complementary pair 与 sphere pair 不是两个独立 factorization architectures。coefficient channels 的 allocation 已被 master **完全定向**；真正未被确定的是

\[
\boxed{S_+S_-=\mathcal N=P_2^2+P_3^2}
\]

内部的 divisor split。

这导致本轮第一项新的正式 theorem：

\[
\boxed{
\texttt{FACTOR\_ALLOCATION\_CHANNELS\_COLLAPSED\_TO\_TWO\_ORIENTATIONS}.
}
\]

第二项新 theorem 来自 raw integer row。R6 有

\[
(A_0,B_0,C_0)=V(\mathcal A,\mathcal B,\mathcal C),
\qquad
\mathscr D_0=V^2\mathscr D\in\mathbf Z.
\]

若 \(\mathscr D\in\mathbf Q^2\)，则 \(\mathscr D_0\) 是整数中的有理平方，所以它的有理平方根实际为整数：

\[
\boxed{W_0:=VW\in\mathbf Z.}
\]

于是 raw complementary pair 总是整数：

\[
\boxed{
R_-^{(0)}=W_0-C_0\in\mathbf Z,
\qquad
R_+^{(0)}=W_0+C_0\in\mathbf Z.
}
\]

这完全解决了 R7 的 integrality-scale 问题，但**没有**自动使 \(S_\pm\) 整数。

第三项新 theorem 是 primitive-row coefficient rigidity。令

\[
d_{\rm row}:=\gcd(A_0,B_0,C_0),
\]

\[
(\widehat A,\widehat B,\widehat C)
:=
\frac1{d_{\rm row}}(A_0,B_0,C_0).
\]

若存在 integer lift，则

\[
\widehat A Q_0-\widehat B P_1=\widehat C.
\]

所以 \(\gcd(\widehat A,\widehat B)\mid\widehat C\)。但 primitive row 定义给

\[
\gcd(\widehat A,\widehat B,\widehat C)=1,
\]

故：

\[
\boxed{
\gcd(\widehat A,\widehat B)=1.
}
\tag{ROW-PRIM}
\]

从而：

\[
\boxed{
\gcd(\widehat A-\widehat B,\widehat A+\widehat B)\in\{1,2\}.
}
\tag{COEFF-GCD}
\]

这是 R7 比原 prompt 中“理想上 coefficient gcd 小”更强的 exact integral-lift necessity。

第四项新 theorem 是 primitive sphere divisor-packet rigidity。令

\[
h:=\gcd(P_1,Q_0).
\]

primitive quadruple

\[
\gcd(P_1,P_2,P_3,Q_0)=1
\]

并**不**推出 \(h=1\)。事实上

\[
(P_1,P_2,P_3,Q_0)=(60,7,24,65)
\]

是 primitive sphere，然而 \(h=5\)，并且

\[
\gcd(S_-,S_+)=5.
\]

所以“\(\gcd(S_-,S_+)\in\{1,2\}\)”作为 universal primitive theorem 是 **FALSE**。

正确 theorem 是：

\[
\boxed{
h\text{ 为奇数，且 }p\mid h\Longrightarrow p\equiv1\pmod4.}
\tag{SPH-GCD}
\]

并且

\[
\boxed{
\gcd(S_-,S_+)
=
\begin{cases}
h,&P_1,Q_0\text{ 异奇偶},\\
2h,&P_1,Q_0\text{ 均奇}.
\end{cases}
}
\]

于是对每个 \(p\equiv3\pmod4\)，由于

\[
v_p(\mathcal N)\equiv0\pmod2
\]

且该 \(p\) 不可能同时除 \(S_+,S_-\)，整个 \(p^{2e}\) packet 必须**完整地进入其中一个 sphere factor**。这给出了不依赖 Gaussian orientation 的 factor-allocation theorem。

第五项结论是对 Lane B 的严格 falsification。moving-modulus condition

\[
M\equiv R_\pm^2\pmod{2\mathcal C}
\]

确实是必要条件，但它只是 exact square factorization 的一个投影，不能自动比 square locus 更强。更关键地，在 frozen R5C canonical outer family 中，取

\[
G=10^4,
\qquad
\mathcal A=111,
\qquad
\mathcal B=1000,
\qquad
\mathcal C=100G+1=1{,}000{,}001,
\]

则精确计算给

\[
M\equiv1{,}000{,}001\pmod{2{,}000{,}002},
\]

而

\[
1{,}000{,}001^2
\equiv1{,}000{,}001
\pmod{2{,}000{,}002}.
\]

所以：

\[
\boxed{
\texttt{MOVING\_MODULUS\_UNIVERSAL\_OBSTRUCTION=FALSE}.
}
\]

这并不说 R5C 的 full square condition成立；R5C 仍由 frozen global nonsquare theorem 杀死。它只证明：R7 不能把“每个 source profile 都违反 \(M\bmod2C\) 的平方性”作为 universal closure theorem。

最后，R7 做了一个定向 exact finite search：在 R6 已合法使用的 reduced shell

\[
b_1=b_2=C_2=C_3=P_3=1
\]

中，对

\[
(g,k)=(1,1),(1,2),(1,3),(2,1)
\]

分别穷尽对应完整 \(V\)-digit interval，总计

\[
9{,}000+90{,}000+900{,}000+900{,}000=1{,}899{,}000
\]

个 \(V\) 值，未发现任何 \(\mathscr D_0\) 平方。此结论只记为 computational evidence，不升级为 theorem。

因此 R7 的严格终局不是虚构的 KILL 或虚构的 LIFT：

\[
\boxed{
\textbf{S3/S4 exceptional square-source intersection 仍 OPEN。}
}
\]

但 R7 已把它压到一个更小且更准确的算术门：

\[
\boxed{
\textbf{primitive-row oriented root divisibility}
\;\times\;
\textbf{primitive sum-of-two-squares packet allocation}.
}
\]

按题设给出的 R8 严格授权规则，目前 A/B/C/D 四条授权条件均未满足。因此：

\[
\boxed{
\texttt{R8\_AUTHORIZED=NO}.
}
\]

若继续，应仍记作 R7 continuation，而不是伪造一个 R8 route。

---

# 2. Frozen R1–R6 State

本轮完全冻结：

- R1 `COMMON_OBSTRUCTION_CERTIFIED`；
- R2 `SOURCE_SECTION_INTERNALIZATION_THEOREM_PROVED`；
- R3 `FINITE_SOURCE_COMPLETED_VALUATION_ATLAS_PROVED`；
- R4 S0/S1/S2 fixed proper character union 与 S3/S4 outer half-rays；
- R5 fixed source-completed base 至多一个 \(Z\)；
- R5C canonical moving profile 的 sphere × full-master first failure；
- R6 complementary discriminant theorem 与 generic-not-universal local square-class verdict。

特别冻结 R6 raw master：

\[
A_0Q_0-B_0P_1=C_0,
\]

\[
A_0=YG(b_1X+b_2)+b_3,
\]

\[
B_0=b_1XYGK,
\]

\[
C_0=b_2YP_2+b_3P_3,
\]

以及 normalized source row：

\[
\mathcal A
=\frac{XYG}{g_1}+\frac{YG}{g_2}+\frac1{g_3},
\]

\[
\mathcal B
=\frac{XYGK}{g_1},
\]

\[
\mathcal C
=YC_2+C_3.
\]

R6 已证明 genuine source profile 上：

\[
\boxed{\mathcal A\ne\mathcal B,}
\]

且 \(\mathcal A,\mathcal B>0\)，故 \(\mathcal A=-\mathcal B\) 亦不可能。

---

# 3. Complementary Discriminant Recap

冻结：

\[
\mathcal N=P_2^2+P_3^2>0,
\]

\[
Q_0^2-P_1^2=\mathcal N,
\]

\[
\mathcal AQ_0-\mathcal BP_1=\mathcal C,
\]

\[
\mathscr D
=
\mathcal C^2+(\mathcal B^2-\mathcal A^2)\mathcal N.
\]

在 lift 上：

\[
\boxed{
\mathscr D
=(\mathcal BQ_0-\mathcal AP_1)^2.
}
\]

raw version：

\[
\mathscr D_0
=C_0^2+(B_0^2-A_0^2)\mathcal N
=V^2\mathscr D.
\]

---

# 4. Square-Locus Definition

本轮 square cover：

\[
\mathcal E_{\rm sq}:
\qquad
W^2=\mathscr D.
\]

要严格区分：

1. ambient / rational square cover；
2. source-completed coefficient profile 与 square cover 的交；
3. integral lift；
4. primitive lift；
5. DES / radial / actual-cut completion。

R7 的核心修正是：第 1 层不能偷偷加入第 3 层的 divisor condition。

---

# 5. Explicit Lift Reconstruction

设

\[
AQ-BP=C,
\]

\[
BQ-AP=W,
\]

且

\[
A^2-B^2\ne0.
\]

线性系统 determinant 为

\[
B^2-A^2.
\]

所以：

\[
\boxed{
Q
=
\frac{-AC+BW}{B^2-A^2}
=
\frac{AC-BW}{A^2-B^2},
}
\tag{INV-Q}
\]

\[
\boxed{
P
=
\frac{-BC+AW}{B^2-A^2}
=
\frac{BC-AW}{A^2-B^2}.
}
\tag{INV-P}
\]

若只给 absolute square root \(w^2=\mathscr D\)，则取 \(W=\delta w\)，\(\delta\in\{\pm1\}\)，得到两支 rational root。

### Square-Locus-to-Lift Lemma

在 \(A^2\ne B^2\) 时：

\[
\boxed{
C^2+(B^2-A^2)N\in\mathbf Q^2
\iff
\exists(P,Q)\in\mathbf Q^2:
Q^2-P^2=N,
AQ-BP=C.
}
\]

integral lift 则额外要求 (INV-Q)/(INV-P) 的 numerator 对 determinant 整除；更自然的等价版本见 sphere pair。

---

# 6. Integrality-Scale Audit

## 6.1 Rational square of an integer

若 \(n\in\mathbf Z\) 且 \(n=(a/b)^2\) with \(\gcd(a,b)=1\)，则 \(b^2\mid a^2\)，故 \(b=1\)。所以：

\[
\boxed{
\mathbf Z\cap\mathbf Q^2=\mathbf Z^2.
}
\]

应用于

\[
\mathscr D_0=V^2\mathscr D\in\mathbf Z.
\]

若 \(\mathscr D=W^2\) with \(W\in\mathbf Q\)，则

\[
\mathscr D_0=(VW)^2,
\]

从而：

\[
\boxed{W_0:=VW\in\mathbf Z.}
\tag{W0}
\]

因此 normalized \(W\) 的准确 lattice 是：

\[
\boxed{W\in\frac1V\mathbf Z.}
\]

而 raw pair 为 genuine integer pair。

## 6.2 Primitive integer row

令

\[
d_{\rm row}=\gcd(A_0,B_0,C_0),
\]

\[
\widehat A=A_0/d_{\rm row},
\quad
\widehat B=B_0/d_{\rm row},
\quad
\widehat C=C_0/d_{\rm row}.
\]

因为

\[
\mathscr D_0=d_{\rm row}^2\widehat{\mathscr D}
=W_0^2,
\]

有 \(d_{\rm row}\mid W_0\)，故

\[
\boxed{
\widehat W:=W_0/d_{\rm row}\in\mathbf Z.
}
\]

这给出 R7 最自然的 integer normalization：

\[
\boxed{
(\widehat A,\widehat B,\widehat C,\widehat W)
\text{ primitive integer row}.
}
\]

---

# 7. Complementary Factor Pair \(R_\pm\)

在 primitive integer row 上定义

\[
\widehat R_-:=\widehat W-\widehat C,
\qquad
\widehat R_+:=\widehat W+\widehat C.
\]

则

\[
\boxed{
\widehat R_-\widehat R_+
=(\widehat B^2-\widehat A^2)\mathcal N,
}
\]

\[
\boxed{
\widehat R_+-\widehat R_-=2\widehat C.
}
\]

并有 exact gcd formula。令

\[
h_R:=\gcd(\widehat W,\widehat C),
\quad
\widehat W=h_Rw,
\quad
\widehat C=h_Rc,
\quad
\gcd(w,c)=1.
\]

则

\[
\boxed{
\gcd(\widehat R_-,\widehat R_+)
=h_R\varepsilon_2,
\qquad
\varepsilon_2\in\{1,2\}.
}
\]

且 \(\varepsilon_2=2\) 当且仅当 reduced \(w,c\) 均奇。

这比单纯

\[
g_R\mid2C,
\qquad
g_R^2\mid M
\]

更精确。

---

# 8. Sphere Factor Pair \(S_\pm\)

定义

\[
S_+=Q_0+P_1,
\qquad
S_-=Q_0-P_1.
\]

则

\[
\boxed{S_+S_-=\mathcal N.}
\tag{SPROD}
\]

master 变成

\[
\boxed{
(A-B)S_+ +(A+B)S_-=2C.
}
\tag{SLIN}
\]

若 \(W=BQ_0-AP_1\)，则直接相加相减得：

\[
\boxed{
W-C=(B-A)S_+,
}
\]

\[
\boxed{
W+C=(A+B)S_-.
}
\]

即 (R7-BRIDGE)。

反过来：

\[
\boxed{
S_+
=
\frac{C-W}{A-B},
\qquad
S_-
=
\frac{C+W}{A+B}.
}
\tag{SINV}
\]

这是 R7 比直接使用 (INV-P/Q) 更清楚的 inverse lift。

---

# 9. Comparison of Two Factorizations

结论：

\[
\boxed{
\textbf{sphere pair 更 source-native；complementary pair 更适合 integer scale/gap。}
}
\]

但两者不是独立信息。

原计划将

\[
M=(B-A)(B+A)\mathcal N
\]

视为三个 multiplicative channels 并研究它们在 \(R_-,R_+\) 之间如何自由分配。R7-BRIDGE 证明这种自由不存在：对 canonical \(W\)，

\[
\boxed{
B-A\text{ 整体进入 }R_-,
\qquad
A+B\text{ 整体进入 }R_+.
}
\]

剩余唯一真正 divisor allocation 是

\[
\boxed{\mathcal N=S_+S_-}.
\]

若换 \(W\mapsto-W\)，只得到 negated swap：

\[
(R_-,R_+)
\mapsto
(-R_+,-R_-).
\]

因此 finite whole-channel atlas 精确只有两种 orientation，而非任意 channel subset。

---

# 10. Primitive GCD Audit

对 integer sphere lift：

\[
\gcd(S_-,S_+)
=
\gcd(Q_0-P_1,Q_0+P_1).
\]

令

\[
h=\gcd(P_1,Q_0).
\]

除以 \(h\) 后两个 reduced 数互素，所以：

\[
\boxed{
\gcd(S_-,S_+)=h\varepsilon_2,
\qquad\varepsilon_2\in\{1,2\}.
}
\tag{SGCD}
\]

## 10.1 为什么 primitive 不推出 \(h=1\)

exact counterexample：

\[
60^2+7^2+24^2=65^2,
\]

\[
\gcd(60,7,24,65)=1,
\]

但

\[
\gcd(60,65)=5,
\]

\[
S_-=5,
\qquad
S_+=125.
\]

所以 R7 prompt 中“理想只有 1 或 2”不能当 theorem。

## 10.2 正确 primitive support theorem

若 \(p\equiv3\pmod4\) 且 \(p\mid P_1,Q_0\)，则

\[
p\mid Q_0^2-P_1^2=P_2^2+P_3^2.
\]

标准二平方性质给 \(p\mid P_2,P_3\)，于是 \(p\) 除四个 primitive coordinates，矛盾。

若 \(2\mid P_1,Q_0\)，则

\[
4\mid P_2^2+P_3^2,
\]

迫使 \(P_2,P_3\) 均偶，同样矛盾。

故：

\[
\boxed{
h\text{ 奇且只含 }p\equiv1\pmod4.}
\]

---

# 11. \(A\pm B\) Source Provenance

R6 source formulas：

\[
\mathcal A
=
\frac{XYG}{g_1}
+
\frac{YG}{g_2}
+
\frac1{g_3},
\]

\[
\mathcal B
=
\frac{XYGK}{g_1}.
\]

所以：

\[
\mathcal A-\mathcal B
=
-\frac{XYG(K-1)}{g_1}
+
\frac{YG}{g_2}
+
\frac1{g_3},
\]

\[
\mathcal A+\mathcal B
=
\frac{XYG(K+1)}{g_1}
+
\frac{YG}{g_2}
+
\frac1{g_3}.
\]

它们不是 arbitrary coefficients，但当前 R7 未从这些 expressions 抽出 fixed prime support。

最强普适 coefficient theorem 来自 primitive integer row + integral lift：

\[
\boxed{
\gcd(\widehat A,\widehat B)=1,
}
\]

因而

\[
\boxed{
\gcd(\widehat A-\widehat B,
\widehat A+\widehat B)\le2.
}
\]

这应取代“尝试证明 coefficient gcd 小”的开放措辞。

---

# 12. \(C\) Source Provenance

冻结：

\[
\boxed{
\mathcal C=YC_2+C_3>0.
}
\]

raw：

\[
C_0=b_2YP_2+b_3P_3.
\]

\(C\) 是真正 source affine anchor，不是自由常数。

R7 未得到 general

\[
\gcd(C,M)\mid D_{\rm fin}
\]

的 fixed finite-support theorem。

---

# 13. \(M\) Source Factorization

\[
\boxed{
M=(B^2-A^2)\mathcal N
=(B-A)(B+A)(P_2^2+P_3^2).
}
\]

但在 lift 上进一步：

\[
M
=
[(B-A)S_+][(B+A)S_-]
=
R_-R_+.
\]

因此 coefficient channels 与 sphere divisors 是 cross-paired，而非三块自由分箱。

---

# 14. \(\gcd(C,M)\) Audit

## 14.1 General source

R7 没有证明 source-uniform fixed bound。

对 odd prime \(p\mid C\cap N\)，由

\[
(A-B)S_+ +(A+B)S_-=2C
\]

可得：若 \(p\nmid\gcd(S_+,S_-)\)，则

- \(p\mid S_+\Rightarrow p\mid A+B\)；
- \(p\mid S_-\Rightarrow p\mid A-B\)。

而 primitive theorem 说明 \(p\equiv3\pmod4\) 不可能属于 \(\gcd(S_+,S_-)\)。所以：

\[
\boxed{
 p\equiv3\pmod4,
\quad p\mid\gcd(C,N)
\Longrightarrow
p\mid(A^2-B^2).
}
\tag{CM-INERT}
\]

这是一个 genuine source-independent support transfer，但仍不把 moving coefficient support压成 finite fixed set。

## 14.2 Canonical R5C profile-specific bound

R5C 有

\[
A=111,
\quad B=1000,
\quad C=100G+1,
\quad N=100G^4+1.
\]

\[
B^2-A^2=987679=7\cdot11\cdot101\cdot127.
\]

由

\[
100G\equiv-1\pmod C
\]

得

\[
100^3N
=100^4G^4+100^3
\equiv1+10^6
=1{,}000{,}001
\pmod C.
\]

且 \(\gcd(C,100)=1\)，故

\[
\boxed{
\gcd(C,N)\mid1{,}000{,}001=101\cdot9901.
}
\]

所以：

\[
\boxed{
\gcd(C,M)
\mid
987679\cdot1{,}000{,}001.
}
\]

这是很漂亮的 factor-gap bridge，但它是 **R5C canonical family-specific**，不能回升为 R7 universal theorem。

---

# 15. Factor Allocation Atlas

R7 得到一个有限的 **packet-type atlas**，但不是 finite exact divisor atlas。

## Type C0 — canonical coefficient orientation

\[
R_-=(B-A)S_+,
\qquad
R_+=(A+B)S_-.
\]

## Type C1 — opposite square-root orientation

\[
(R_-,R_+)\mapsto(-R_+,-R_-).
\]

## Type N-I — inert primes \(p\equiv3\pmod4\)

\[
v_p(N)=2e.
\]

primitive sphere 禁止 \(p\) 同时进入 \(S_+,S_-\)，故：

\[
\boxed{
(p^{2e}\mid S_+,\ p\nmid S_-)
\quad\text{or}\quad
(p^{2e}\mid S_-,\ p\nmid S_+).
}
\]

整个 inert packet 不可拆。

## Type N-S — split primes \(p\equiv1\pmod4\)

允许在 \(S_+,S_-\) 间分配，也允许通过

\[
h=\gcd(P_1,Q_0)
\]

形成 shared content。

这是当前仍然无限移动的自由度。

## Type N-2a — odd \(N\)

\(P_1,Q_0\) 异奇偶，故 \(S_+,S_-\) 均奇。

## Type N-2b — even \(N\)

primitive 排除 \(P_1,Q_0\) 同偶；若二者同奇，则

\[
N=Q_0^2-P_1^2\equiv0\pmod8.
\]

且 \(S_+,S_-\) 均偶，其中一个的 \(v_2\) 恰为 1，另一个承担剩余 \(2\)-power。

因此：

\[
\boxed{
\texttt{FINITE\_FACTOR\_ALLOCATION\_ATLAS=YES\_AT\_PACKET\_TYPE\_LEVEL},
}
\]

但：

\[
\boxed{
\texttt{FINITE\_EXACT\_DIVISOR\_CLASSES=NO\_PROOF}.
}
\]

---

# 16. Sum-of-Two-Squares Divisor Structure

不使用 Gaussian orientation，只使用必要 arithmetic：

\[
N=P_2^2+P_3^2.
\]

所以每个 \(p\equiv3\pmod4\) 满足

\[
v_p(N)\equiv0\pmod2.
\]

注意：当前 source provenance 只保证 full primitive quadruple；并没有恢复 universal theorem

\[
\gcd(P_2,P_3)=1.
\]

所以不能错误升级成“所有 \(3\bmod4\) prime 都不出现”。正确结论只是 exponent even；再结合 primitive \(S\)-gcd theorem，得到 whole-packet allocation。

---

# 17. Divisor-Constrained Lift Gate

这是 R7 的核心语义修正。

## 17.1 Rational gate

若 \(\mathscr D=W^2\in\mathbf Q^2\)，则 \(S_\pm\in\mathbf Q\)，且

\[
S_+S_-=N.
\]

这里 **不要求** \(S_+\mid N\)。

## 17.2 Integral gate

使用 primitive integer row \((\widehat A,\widehat B,\widehat C)\) 与 \(\widehat W\in\mathbf Z\)。取 canonical orientation：

\[
\boxed{
S_+
=
\frac{\widehat C-\widehat W}
{\widehat A-\widehat B},
}
\]

\[
\boxed{
S_-
=
\frac{\widehat C+\widehat W}
{\widehat A+\widehat B}.
}
\]

因此 integer sphere/master lift 当且仅当某个 square-root orientation满足：

\[
\boxed{
\widehat A-\widehat B
\mid
\widehat C-\delta\widehat W,
}
\tag{OD1}
\]

\[
\boxed{
\widehat A+\widehat B
\mid
\widehat C+\delta\widehat W,
}
\tag{OD2}
\]

并且所得 \(S_+,S_-\) 同奇偶。

这给出新 canonical gate：

\[
\boxed{
\mathfrak D_{\rm or}(\delta)
:=
\left(
\widehat C-\delta\widehat W\bmod(\widehat A-\widehat B),
\widehat C+\delta\widehat W\bmod(\widehat A+\widehat B)
\right).
}
\]

integer lift 要求至少一个 \(\delta\) 使

\[
\boxed{
\mathfrak D_{\rm or}(\delta)=(0,0)
}
\]

再通过 parity。

这是比 \(M\bmod2C\) 更贴近真实 denominator 的 moving-modulus invariant。

---

# 18. Moving-Modulus Square Condition

从

\[
R_+\equiv R_-\pmod{2C}
\]

得

\[
\boxed{
M=R_-R_+
\equiv R_-^2
\pmod{2C}.
}
\]

所以

\[
\boxed{
M\in\operatorname{Sq}(\mathbf Z/2C\mathbf Z)
}
\]

是 integral raw factor pair 的必要条件。

但它是 square factorization 的 projection：若 genuine \(W\in\mathbf Z\) 已存在，则它自动成立。

因此它最多可在“不先知道 \(W\)”时作为 cheap source sieve，不是 square cover 内额外 independent condition。

---

# 19. Variable-Modulus Local Obstruction

R7 对 canonical R5C family 做了 exact audit：

\[
A=111,
\quad B=1000,
\quad C=100G+1,
\quad N=100G^4+1.
\]

\(g=1,\ldots,12\) 的 \(M\bmod2C\) quadratic-residue status 不是常数；其中：

\[
g=4,5,11
\]

为 residue，其他所检值中多为 nonresidue。

特别 \(g=4\) 有手工可验的 exact witness：

\[
M\equiv C\pmod{2C},
\]

且 \(C\) 为奇数，所以

\[
C^2-C=C(C-1)
\]

被 \(2C\) 整除，故

\[
C^2\equiv C\equiv M\pmod{2C}.
\]

因此“所有 source-legal profile 都违反 moving-modulus square condition”的 universal Outcome C 被严格 falsify。

---

# 20. Degenerate \(A=\pm B\) Cases

抽象 algebra 中需要处理，但 genuine source 已由 R6 kill。

## 20.1 \(A=B\ne0\)

master：

\[
A(Q-P)=C,
\]

所以

\[
S_-=C/A.
\]

若 \(C\ne0\)，则

\[
S_+=N/S_-,
\]

可直接恢复 rational lift；integral 条件为二者整数同 parity。

若 \(C=0\) 且 \(N>0\)，则要求 \(S_-=0\)，与 \(S_+S_-=N\) 矛盾。

但 R6 source theorem 已证明 \(A=B\) source-empty。

## 20.2 \(A=-B\ne0\)

同理

\[
A(Q+P)=C,
\quad
S_+=C/A.
\]

source 中因 \(A,B>0\)，此支不存在。

## 20.3 \(A=0\) 或 \(B=0\)

抽象系统若另一 coefficient 非零，仍属于 nondegenerate determinant，可由一般 inverse formula处理。

但 source formulas每项正，故 genuine source：

\[
\boxed{A=0\text{ impossible},\quad B=0\text{ impossible}.}
\]

---

# 21. Sign / Parity Atlas

source：

\[
A>0,
\quad B>0,
\quad C>0,
\quad N>0.
\]

若 positive sphere lift：

\[
Q_0>P_1>0,
\]

所以

\[
S_+>S_->0.
\]

canonical \(W=BQ_0-AP_1\) 下：

\[
R_+=(A+B)S_->0,
\]

\[
\operatorname{sgn}(R_-)
=
\operatorname{sgn}(B-A).
\]

同时

\[
R_+-R_-=2C>0.
\]

parity：

- \(P_1,Q_0\) 异奇偶 \(\Rightarrow S_\pm\) 均奇，\(N\) 奇；
- \(P_1,Q_0\) 均奇 \(\Rightarrow S_\pm\) 均偶，\(v_2(N)\ge3\)；
- primitive 排除 \(P_1,Q_0\) 均偶。

---

# 22. Magnitude / Square-Gap Audit

对整数 \(C\ge0,W\)：

\[
W^2-C^2=M.
\]

若 \(M>0\)，则 \(|W|\ge C+1\)，故最小 positive gap 为

\[
(C+1)^2-C^2=2C+1.
\]

所以：

\[
\boxed{0<M<2C+1\Longrightarrow\text{ no square lift}.}
\]

若 \(M<0\) 且 \(C\ge1\)，则 \(|W|\le C-1\)，故最近 negative gap 的 absolute value 至少

\[
C^2-(C-1)^2=2C-1.
\]

因此：

\[
\boxed{-2C+1<M<0\Longrightarrow\text{ no square lift}.}
\]

source 中 \(M=0\) 等价于 \(A=B\)（因 \(N>0,A+B>0\)），已由 R6 source nondegeneracy 排除。

R7 未得到能在 general S3/S4 large region uniform 触发上述 inequalities 的 source theorem，所以 magnitude route只保留为 late support。

---

# 23. Source-Legal Square Search

## 23.1 Reduced-shell scan

固定 R6 已合法使用的 reduced shell shape：

\[
b_1=b_2=C_2=C_3=P_3=1,
\]

\[
P_2=V,
\]

并按 outer decimal relations令对应 \(Y,G,K\) 取实际 powers of ten。

exact scan：

| \((g,k)\) | \(V\) interval | checked | square hits |
|---|---:|---:|---:|
| (1,1) | [1000,10000) | 9,000 | 0 |
| (1,2) | [10000,100000) | 90,000 | 0 |
| (1,3) | [100000,1000000) | 900,000 | 0 |
| (2,1) | [100000,1000000) | 900,000 | 0 |

总计 1,899,000 exact values，无 square hit。

**状态：COMPUTATIONAL EVIDENCE ONLY。**

这不能证明 infinite shell，更不能证明 general S3/S4 empty。

## 23.2 Fixed-character positive control

历史 synchronized state：

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169)
\]

确实给 integral sphere+master。其 master raw row可写

\[
168Q_0-1000P_1=60P_2+8P_3=4392.
\]

primitive row：

\[
(\widehat A,\widehat B,\widehat C)=(21,125,549).
\]

有

\[
\widehat W=125\cdot169-21\cdot24=20621,
\]

\[
S_+=193,
\quad S_-=145,
\quad N=27985.
\]

并且

\[
\frac{549-20621}{21-125}=193,
\]

\[
\frac{549+20621}{21+125}=145.
\]

这精确验证了 oriented divisor reconstruction。

但该 state 位于

\[
g=0,
\qquad X=10=10G,
\]

属于 R4 已压入 fixed-character union 的状态，不是 S3/S4 outer witness。因此 R7 明确禁止用它签 `SPHERE_MASTER_INTEGRAL_LIFT_EVASION_PROVED`。

---

# 24. \(P_1,Q_0\) Recovery

对任意真正找到的 S3/S4 square root，恢复顺序固定为：

1. primitive raw row取得 \(\widehat W\in\mathbf Z\)；
2. 检查两种 \(\delta\in\{\pm1\}\) 的 (OD1)/(OD2)；
3. 得 \(S_\pm\)；
4. parity；
5. 恢复
   \[
   Q_0=(S_++S_-)/2,
   \]
   \[
   P_1=(S_+-S_-)/2;
   \]
6. 检查 sign / size / gcd profile。

当前没有 S3/S4 square root，因此本轮没有可合法恢复的 outer \(P_1,Q_0\)。

---

# 25. Integral / Primitive Lift Audit

本轮得到 conditional exact criteria，但没有 outer witness。

### Integral lift exact gate

\[
\boxed{
\exists\delta\in\{\pm1\}:
\begin{cases}
\widehat A-\widehat B\mid\widehat C-\delta\widehat W,\\
\widehat A+\widehat B\mid\widehat C+\delta\widehat W,\\
S_+\equiv S_-\pmod2.
\end{cases}
}
\]

### Primitive lift exact audit

所得 quadruple 必须满足

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

并重新核验

\[
g_i=\gcd(V,P_i),
\qquad
b_i=V/g_i.
\]

特别第一 coordinate 的 \(g_1\) 不能在 square search 前被视为 automatically preserved。

---

# 26. DES Audit

R7 没有找到 outer integral sphere×master lift，所以 full DES 未进入。

状态：

```text
DES_COMPATIBLE=NOT_REACHED_ON_S3_S4
```

R6 的 \(J\) 继续只作 saturation decoration；R7 未重开 \(J\)-branch。

---

# 27. Source Interval / Actual Cut Audit

同理，由于没有 outer integer/primitive lift：

```text
SOURCE_INTERVAL_COMPATIBLE=NOT_REACHED_AFTER_LIFT
ACTUAL_CUT_COMPATIBLE=NOT_REACHED_AFTER_LIFT
```

注意 pre-lift source shells 可以有合法 \(U\) interval，这不等价于恢复后的 \(P_1\) 也满足完整 first-coordinate gcd/digit/source semantics。

---

# 28. Unbounded-Lift Family Search

R7 没有找到单个 S3/S4 source-legal square lift，因此更没有得到

\[
|d(t)|\to\infty
\]

的 full lift family。

```text
UNBOUNDED_LIFT_FAMILY=NO
```

这里 `NO` 意味“未构造”，不是证明不存在。

---

# 29. Finite Exceptional Components

R7 的 factor-allocation atlas虽然在 packet type 层有限，但 split-prime \(p\equiv1\pmod4\) 的 divisor allocation与 moving coefficient support仍可无界变化。

所以当前不能把

\[
\mathcal E_{\rm sq}^{\rm src}
\]

压成已证明的 finite proper components。

唯一已精确关闭的 algebraic components 是 source-degenerate strata：

\[
A=B,
\qquad A=-B,
\qquad A=0,
\qquad B=0.
\]

它们本来就由 R6 source positivity/nondegeneracy排除，不构成新的 S3/S4 exceptional list。

因此：

\[
\boxed{
\texttt{FINITE\_EXCEPTIONAL\_SOURCE\_COMPONENTS=NO\_PROOF}.
}
\]

---

# 30. Failed / Falsified Routes

R7 后应正式退休或降级：

1. **“square \(\Rightarrow S_+\mid N\)” at rational level** — FALSE；divisor condition属于 integral gate。
2. **three-channel arbitrary allocation** — FALSE；R7-BRIDGE 强制 coefficient channels。
3. **primitive sphere \(\Rightarrow\gcd(S_-,S_+)\in\{1,2\}** — FALSE；exact counterexample gcd=5。
4. **moving modulus \(M\bmod2C\) universally non-square** — FALSE；R5C \(g=4\) exact residue witness。
5. **packet-type finite atlas \(\Rightarrow\) finite source components** — NOT DERIVED；split-prime freedom remains。
6. **reduced-shell finite no-hit scan \(\Rightarrow\) theorem** — FORBIDDEN；只作 computational evidence。
7. **fixed-character integral control \(\Rightarrow\) outer evasion** — FALSE scope transfer；该点不属于 S3/S4。

继续冻结 R6 已退休：fixed finite-prime cover、odd-\(v_5\) universalization 等。

---

# 31. Exact Remaining Unknowns

R7 后真正剩余的问题已比开局更小：

## U1 — Outer source square existence

是否存在 genuine S3/S4 source-completed profile 使

\[
\mathscr D\in\mathbf Q^2?
\]

这仍是第一全局 unknown。

## U2 — Oriented root divisibility

若 U1 YES，是否某一 orientation满足

\[
\widehat A-\widehat B\mid\widehat C-\delta\widehat W,
\]

\[
\widehat A+\widehat B\mid\widehat C+\delta\widehat W?
\]

## U3 — Split-prime allocation compression

是否 source provenance 能约束 \(p\equiv1\pmod4\) 的 shared / split allocation，使 \(\operatorname{Div}_{\rm src}(N)\) 从无限 moving divisor set 压成 finite-type components？

## U4 — General \(\gcd(C,M)\) control

canonical R5C family有 fixed bound，但 general moving profile是否存在 source-uniform analogue仍 open。

这四个 unknown 中 U1/U2 是一个连续 gate 的两层，不建议再拆成多战区。

---

# 32. R7 Terminal Verdict

## Mid-round shock choice

A/B Lane 初攻后，没有 square witness；moving-modulus universal route被 falsify。因此研究方向选择 **KILL-side**，继续攻击 divisor/gcd rigidity。

但最终没有得到：

\[
\mathcal E_{\rm sq}^{\rm src}=\varnothing,
\]

也没有得到一个 genuine S3/S4 square source point。

数学上不能把“未找到 witness”写成 KILL，也不能把 fixed-character control写成 LIFT。

因此正式终局：

\[
\boxed{
\texttt{R7\_TERMINAL\_VERDICT=
KILL\_ATTEMPT\_INCOMPLETE\_\_LIFT\_NOT\_FOUND\_\_DIVISOR\_GATE\_REFACTORED}.
}
\]

同时签发以下 **真实** R7 theorems：

```text
RAW_INTEGER_SQUARE_ROOT_SCALE_PROVED
PRIMITIVE_ROW_COEFFICIENT_GCD_RIGIDITY_PROVED
COMPLEMENTARY_SPHERE_FACTOR_BRIDGE_PROVED
FACTOR_ALLOCATION_CHANNELS_COLLAPSED_TO_TWO_ORIENTATIONS
DIVISOR_CONSTRAINED_GATE_RECLASSIFIED_AS_INTEGRAL_NOT_RATIONAL
PRIMITIVE_SPHERE_INERT_PACKET_ALLOCATION_PROVED
MOVING_MODULUS_UNIVERSAL_OBSTRUCTION_FALSIFIED
```

不签发：

```text
EXCEPTIONAL_SQUARE_LOCUS_SOURCE_EMPTY
DIVISOR_CONSTRAINED_LIFT_OBSTRUCTION_PROVED_GLOBALLY
MOVING_MODULUS_FACTOR_GAP_OBSTRUCTION_PROVED
SPHERE_MASTER_INTEGRAL_LIFT_EVASION_PROVED_ON_S3_S4
SQUARE_LOCUS_COMPRESSED_TO_FINITE_SOURCE_COMPONENTS
```

---

# 33. R8 Single Attack Target

题设严格规定 R8 只有四种授权来源：

- square locus source-empty；
- finite exceptional source components；
- outer integral sphere×master lift；
- full source unbounded lift family。

R7 一个也没有证明。

所以：

\[
\boxed{
\texttt{R8\_AUTHORIZED=NO}.
}
\]

若继续研究，应先进行 **105-R7B**，而不是伪称 R8。唯一攻击目标建议固定为：

\[
\boxed{
\textbf{Primitive-Row Oriented Root Divisibility}
\times
\textbf{Split-Prime Source Allocation}
}
\]

即直接研究：

\[
\boxed{
\mathscr D=\widehat W^2
}
\]

与

\[
\boxed{
\widehat A-\widehat B\mid\widehat C-\delta\widehat W,
\qquad
\widehat A+\widehat B\mid\widehat C+\delta\widehat W
}
\]

能否在 S3/S4 source profiles 上同时发生，并把 \(p\equiv1\pmod4\) 的剩余自由纳入 full Smith/source gcd provenance。

这比继续 \(M\bmod2C\)、继续 generic discriminant、继续固定 prime local obstruction都更精确。

---

# Machine-readable terminal block

```text
R7_TERMINAL_VERDICT=KILL_ATTEMPT_INCOMPLETE__LIFT_NOT_FOUND__DIVISOR_GATE_REFACTORED

R1_R2_R3_R4_R5_R5C_R6_STATE_FROZEN=YES

SQUARE_LOCUS=OPEN_ON_S3_S4_SOURCE_INTERSECTION
COMPLEMENTARY_DISCRIMINANT=FROZEN_R6__D=C^2+(B^2-A^2)N

W_INTEGRAL_SCALE=NORMALIZED_W_IN_(1/V)Z__RAW_W0=V*W_IN_Z__PRIMITIVE_ROW_W_HAT_IN_Z
R_MINUS=W_HAT-C_HAT__RAW_R0_MINUS=W0-C0
R_PLUS=W_HAT+C_HAT__RAW_R0_PLUS=W0+C0
S_MINUS=(C_HAT+DELTA*W_HAT)/(A_HAT+B_HAT)
S_PLUS=(C_HAT-DELTA*W_HAT)/(A_HAT-B_HAT)

SPHERE_FACTOR_PRODUCT=S_MINUS*S_PLUS=N=P2^2+P3^2
MASTER_FACTOR_LINEAR_RELATION=(A-B)S_PLUS+(A+B)S_MINUS=2C

GCD_S_MINUS_S_PLUS=h*epsilon2__h=gcd(P1,Q0)_ODD_SPLIT_PRIME_SUPPORTED__epsilon2_IN_{1,2}
GCD_C_M=NO_GENERAL_SOURCE_UNIFORM_FIXED_BOUND_PROVED__R5C_PROFILE_SPECIFIC_BOUND_EXISTS
GCD_AB_COEFFICIENTS=INTEGRAL_LIFT_ON_PRIMITIVE_ROW_FORCES_gcd(A_HAT,B_HAT)=1__THUS_gcd(A_HAT-B_HAT,A_HAT+B_HAT)_IN_{1,2}

SOURCE_DIVISOR_SET=INTEGER_DIVISORS_SPLUS_OF_N_WITH_SMINUS=N/SPLUS__PARITY__ORDER__PRIMITIVE_PACKET_RULES__MASTER_AFFINE_RELATION
DIVISOR_CONSTRAINED_LIFT=PROVED_AS_EXACT_INTEGRAL_LIFT_GATE__NOT_AN_EXTRA_RATIONAL_SQUARE_GATE

FACTOR_ALLOCATION_TYPES=TWO_W_ORIENTATIONS_X_TWO_PARITY_TYPES_PLUS_INERT_PACKET_WHOLE_ALLOCATION
FINITE_FACTOR_ALLOCATION_ATLAS=YES_AT_PACKET_TYPE_LEVEL__NO_AT_EXACT_DIVISOR_COMPONENT_LEVEL

MOVING_MODULUS=2*C
M_MOD_2C=M_CONGRUENT_R_MINUS^2_CONGRUENT_R_PLUS^2_MOD_2C
MOVING_MODULUS_SQUARE_NECESSARY=YES_FOR_INTEGER_FACTOR_PAIR
MOVING_MODULUS_OBSTRUCTION=NOT_UNIVERSAL__EXACTLY_FALSIFIED_BY_CANONICAL_R5C_g4_RESIDUE_WITNESS

DEGENERATE_A_EQ_B=SOURCE_EMPTY_BY_FROZEN_R6_NONDEGENERACY
DEGENERATE_A_EQ_MINUS_B=SOURCE_EMPTY_BY_POSITIVITY
A_ZERO_CASE=SOURCE_EMPTY_BY_POSITIVITY
B_ZERO_CASE=SOURCE_EMPTY_BY_POSITIVITY

SQUARE_SOURCE_PROFILE_FOUND=NO_GENUINE_S3_S4_PROFILE_FOUND
SQUARE_PROFILE_SOURCE_LEGAL=NO_OUTER_WITNESS__FIXED_CHARACTER_CONTROL_EXISTS_BUT_EXCLUDED

P1_RECOVERED=NO_ON_S3_S4__YES_ONLY_FIXED_CHARACTER_REGRESSION_CONTROL
Q0_RECOVERED=NO_ON_S3_S4__YES_ONLY_FIXED_CHARACTER_REGRESSION_CONTROL
RATIONAL_LIFT=EQUIVALENT_TO_SQUARE_LOCUS_BY_FROZEN_R6__SOURCE_EXISTENCE_OPEN
INTEGRAL_LIFT=OPEN_ON_S3_S4
PRIMITIVE_LIFT=OPEN_ON_S3_S4

DES_COMPATIBLE=NOT_REACHED_ON_S3_S4
SOURCE_INTERVAL_COMPATIBLE=NOT_REACHED_AFTER_S3_S4_LIFT
ACTUAL_CUT_COMPATIBLE=NOT_REACHED_AFTER_S3_S4_LIFT
OUTER_COMPATIBLE=NO_FULL_LIFT_WITNESS

UNBOUNDED_LIFT_FAMILY=NO_WITNESS__NONEXISTENCE_NOT_PROVED

SQUARE_LOCUS_SOURCE_STATUS=OPEN
FINITE_EXCEPTIONAL_SOURCE_COMPONENTS=NO_PROOF

NEW_CANONICAL_INVARIANT=PRIMITIVE_ROW_ORIENTED_ROOT_DIVISIBILITY_CLASS
NEW_FIRST_FAILURE_GATE=GLOBAL_SOURCE_SQUARE_INTERSECTION_REMAINS_FIRST__CONDITIONAL_NEXT_GATE=ORIENTED_INTEGER_DIVISIBILITY

S3_STATUS=OPEN_AT_EXCEPTIONAL_SQUARE_SOURCE_INTERSECTION
S4_STATUS=OPEN_AT_EXCEPTIONAL_SQUARE_SOURCE_INTERSECTION

RETIRED_AFTER_R7=ARBITRARY_THREE_CHANNEL_FACTOR_ALLOCATION;PRIMITIVE_GCD_S_IN_{1,2}_CONJECTURE;MOVING_MODULUS_AS_UNIVERSAL_KILLER;DIVISOR_CONSTRAINT_AS_RATIONAL_GATE

R8_AUTHORIZED=NO
R8_ARCHITECTURE=NONE__STRICT_AUTHORIZATION_CONDITIONS_NOT_MET
R8_SINGLE_ATTACK_TARGET=NOT_APPLICABLE__CONTINUE_AS_R7B_ORIENTED_ROOT_DIVISIBILITY_X_SPLIT_PRIME_SOURCE_ALLOCATION
```

---

# Companion artifacts

本轮同时生成：

- `105_R7_Factor_Pair_Registry.csv`
- `105_R7_Source_Divisor_Ledger.csv`
- `105_R7_GCD_Audit.csv`
- `105_R7_Factor_Allocation_Atlas.csv`
- `105_R7_Moving_Modulus_Residue_Audit.csv`
- `105_R7_Square_Profile_Registry.csv`
- `105_R7_Lift_Reconstruction_Registry.csv`
- `105_R7_Exceptional_Component_Register.csv`
- `105_R7_scripts/verify_r7_factor_pair.py`
- `105_R7_scripts/verify_r7_factor_pair.log`

脚本中明确区分 symbolic theorem checks 与 finite computational evidence；finite shell search不被写成 global theorem。

---

# Provenance note

本轮主要冻结 provenance 来自：

- `105_R6_General_Moving_Profile_Sphere_Master_Lift.md`：general raw/normalized master、complementary discriminant、source nondegeneracy；
- `105_R5C_Moving_Base_Full_Source_Decision.md`：canonical outer moving profile 与 R5C first failure；
- `105_R3_Source_Completed_Valuation_Atlas.md`：S3 source-completed counterfamily / primitive sphere completion；
- `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`：primitive/common-U/source reconstruction semantics；
- `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md` 与后续 A1 reports：fixed-character synchronized integral control。

R7 新增代数结论均可由本文件与 companion script 独立复核。
