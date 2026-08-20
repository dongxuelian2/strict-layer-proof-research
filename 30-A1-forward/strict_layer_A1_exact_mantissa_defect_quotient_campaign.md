# 三项十进制拼接平方和问题：A1 Exact Mantissa Synchronization × Defect Quotient Campaign

**文件名：** `strict_layer_A1_exact_mantissa_defect_quotient_campaign.md`  
**研究范围：** Strict Layer 正向线，仅研究 `A1-only`；DD 保持 closed。  
**本轮结论等级：**

\[
\boxed{
\textbf{A1 尚未闭合；但达到 Level 7 型 Exact-Prefix / Exact-Tail-Block Reduction，}
}
\]

并得到一个比第五轮 MB 更低维的整数 normal form、一个新的 transition-slice closure，以及一组 actual-denominator-gcd 的 Smith 型整除定理。

最重要的新结论是：

1. 第五轮的 mantissa balance 可完全整数化为同一个 signed integer defect `H` 的两侧 Euclidean/carry 表达；
2. 第三尾并非只给近似或 valuation：它给出一个**无损失的 exact g-digit suffix congruence**；
3. plus branch 中，\(\varepsilon=b_1D/Q_0\) 的前 \(m_2\) 位十进制数字**恰好就是** \(b_2\)；
4. growing-\(g\) minus 的 \(d=-1\) slice 可严格删除，因此
   \[
   \boxed{g\ge1,\ \text{minus}\Longrightarrow d\ge0;}
   \]
5. denominator resonance
   \[
   R=b_2 10^{n_3}-b_3=0
   \]
   严格强迫
   \[
   \boxed{d=0,\quad b_3=b_2 10^{n_3},\quad g_2=10^{n_3}g_3,\quad \beta_2=\beta_3;}
   \]
6. 把三块 denominator 的 pairwise gcd 做 Smith 型分解后，得到新的 exact allocation
   \[
   \boxed{\alpha\mid(Q_0-P_3),\qquad \beta\mid10^{m_2+m_3}D}
   \]
   并推出 \(\alpha,\beta\) 的所有 \(3\bmod4\) odd prime support 均被禁止；
7. 但 generic \(R\ne0\) 的 denominator mismatch **可以精确小到 1**，因此“\(R\neq0\) 自动产生足够大 gap”是错误的 standalone closure 目标；
8. 本轮仍未得到 absolute \(g\)-bound、absolute \(d\)-bound、absolute \(n_3\)-bound，也未证明所有 infinite escape 必落入 \(R=0\)。

因此本轮真正留下的 terminal frontier 是：

\[
\boxed{
\text{Exact leading Euclidean quotient}
\times
\text{exact third-tail suffix block}
\times
\text{asymmetric denominator-gcd allocation}
}
\]

而不是单纯的 real mantissa proximity。

---

# 1. Frozen Five-Round Results

本轮冻结并使用前五轮已经证明的：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

\[
g_i=\gcd(V,P_i),
\qquad
C_i=P_i/g_i,
\]

\[
a_i=UC_i,
\qquad
b_i=V/g_i,
\qquad
\gcd(U,V)=1,
\]

\[
g=m_3-n_3\ge0,
\qquad
k\ge1,
\]

\[
n_2=m_2+g+k,
\qquad
m_3=n_3+g,
\]

以及 flat elimination、GSYNC、common-\(U\) reconstruction、fixed-profile radial termination、第五轮 \(P_2\)-axis geometry 与：

\[
10^{-k}<\frac{P_1}{Q_0}<\left(1+\frac1{b_1}\right)10^{-k},
\]

\[
P_2>\sqrt{96/101}\,Q_0\qquad(g\ge1),
\]

\[
\frac{Q_0}{2\,10^{2k}}<d_2:=Q_0-P_2,
\]

\[
d_2<\frac{Q_0}{10^{2k}}
\left[
\left(1+\frac1{b_1}\right)^2+10^{4-4g}
\right],
\]

\[
\frac{Q_0}{1100\,10^{2g+k}}
< P_3
<100Q_0\,10^{-(2g+k)},
\]

以及 branch drift：

\[
g\ge1,\ \text{plus}\Longrightarrow d:=m_2-g\le1,
\]

\[
g\ge1,\ \text{minus}\Longrightarrow d\ge-1.
\]

本轮不重新证明这些结果。

---

# 2. Exact Terminal Variables

定义：

\[
D:=P_1 10^k-Q_0>0,
\]

\[
\varepsilon:=\frac{b_1D}{Q_0}\in(0,1),
\]

\[
\beta_i:=\frac{b_i}{10^{m_i}}\in[0.1,1),
\]

\[
x:=\frac{P_2}{Q_0},
\qquad
y:=\frac{P_3}{Q_0},
\]

\[
d:=m_2-g,
\qquad
d_2:=Q_0-P_2,
\qquad
T_3:=Q_0-P_3.
\]

第五轮 exact mantissa balance 是：

\[
\boxed{
\varepsilon
=
\beta_2(1-x10^{-g})
+
\beta_3(1-y)10^{-m_2}.
}
\tag{MB1}
\]

等价地：

\[
\boxed{
10^g(\varepsilon-\beta_2)
=
-\beta_2x
+
\beta_3(1-y)10^{-d}.
}
\tag{MB2}
\]

再用 \(x=1-d_2/Q_0\)：

\[
\boxed{
10^g(\varepsilon-\beta_2)
=
(\beta_3 10^{-d}-\beta_2)
+
\beta_2\frac{d_2}{Q_0}
-
\beta_3\frac{P_3}{Q_0}10^{-d}.
}
\tag{MB3}
\]

**状态：FROZEN / RE-DERIVED EXACTLY.**

---

# 3. Integer Defect \(H\): exact normalization

定义 signed integer：

\[
\boxed{
H:=b_2Q_0-b_1 10^{m_2}D.
}
\tag{H0}
\]

则：

\[
\boxed{
\beta_2-\varepsilon
=
\frac{H}{10^{m_2}Q_0}.
}
\tag{H1}
\]

因此：

- minus branch \(\iff H>0\)；
- plus branch \(\iff H<0\)。

flat 已删除，所以：

\[
\boxed{H\ne0.}
\]

由 MB2 还得到完全不含 \(\varepsilon\) 的版本：

\[
\boxed{
H
=
Q_0\left[
10^d\beta_2x-\beta_3(1-y)
\right].
}
\tag{H2}
\]

即：

\[
\boxed{
H
=
10^d\beta_2P_2
-
\beta_3(Q_0-P_3).
}
\tag{H2'}
\]

这条式子虽然含 terminating mantissas，但总和严格为整数。

**状态：NEW PROVED NORMAL FORM.**

---

# 4. \(H\) 是 primitive defect 的 pairwise-gcd quotient

前轮定义：

\[
\Delta_{12}
=
g_2 10^{m_2}D-g_1Q_0.
\]

令：

\[
h_{12}:=\gcd(g_1,g_2),
\qquad
c_{12}:=\gcd(b_1,b_2).
\]

由于 \(g_i\mid V\) 且 \(b_i=V/g_i\)：

\[
\boxed{
c_{12}=\frac{V}{\operatorname{lcm}(g_1,g_2)}.
}
\]

写：

\[
g_1=h_{12}r_1,
\qquad
g_2=h_{12}r_2,
\qquad\gcd(r_1,r_2)=1.
\]

则存在 \(c_{12}>0\) 使：

\[
b_1=c_{12}r_2,
\qquad
b_2=c_{12}r_1.
\]

故：

\[
H
=c_{12}(r_1Q_0-r_2 10^{m_2}D),
\]

而：

\[
\Delta_{12}
=h_{12}(r_2 10^{m_2}D-r_1Q_0).
\]

所以：

\[
\boxed{
H
=-c_{12}\frac{\Delta_{12}}{h_{12}}.
}
\tag{HQ-12}
\]

这说明 \(H\) 不是与旧 defect 无关的新变量；它是：

\[
\boxed{
\text{把 }\Delta_{12}\text{ 约掉 }\gcd(g_1,g_2)
\text{ 后，再乘上 }\gcd(b_1,b_2)
}
\]

得到的 actual denominator-normalized primitive defect。

**状态：NEW PROVED.**

---

# 5. Third-tail exact quotient \(K_3\)

从 MB/H 等式严格整理：

\[
\boxed{
10^{m_3}H
=
b_2P_2 10^{n_3}
-
b_3(Q_0-P_3).
}
\tag{H3}
\]

因为：

\[
m_3=n_3+g,
\]

所以：

\[
\boxed{
10^{n_3}(b_2P_2-10^gH)
=
b_3(Q_0-P_3).
}
\tag{H4}
\]

因此本轮得到一个此前只以较弱形式出现的 exact divisor：

\[
\boxed{
10^{n_3}\mid b_3(Q_0-P_3).
}
\tag{TDIV}
\]

定义：

\[
\boxed{
K_3
:=
\frac{b_3(Q_0-P_3)}{10^{n_3}}
\in\mathbb Z_{>0}.
}
\tag{K3}
\]

则：

\[
\boxed{
b_2P_2=10^gH+K_3.}
\tag{K3-H}
\]

**状态：NEW PROVED.**

这比“先提取 \(2,5\)-valuation 再损失若干位”的版本更强：对 full exact A1 state，\(K_3\) 本身已经是整数，无需 valuation loss。

---

# 6. Exact g-digit third-tail suffix synchronization

由 (K3-H)：

\[
\boxed{
K_3\equiv b_2P_2\pmod{10^g}.
}
\tag{TAIL-SUFFIX}
\]

即：

\[
\boxed{
\frac{b_3(Q_0-P_3)}{10^{n_3}}
\equiv
b_2P_2
\pmod{10^g}.
}
\]

等价地：

\[
\boxed{
b_3(Q_0-P_3)
\equiv
b_2P_2 10^{n_3}
\pmod{10^{n_3+g}}.
}
\]

其十进制意义非常直接：

1. \(b_3(Q_0-P_3)\) 的最后至少 \(n_3\) 位为 0；
2. 删除这 \(n_3\) 个 trailing zeros 后，所得整数的最后 \(g\) 位，必须与 \(b_2P_2\) 的最后 \(g\) 位完全一致。

这正是本轮要求的 **exact decimal block synchronization**。

**状态：NEW PROVED — LEVEL 7 TYPE RESULT.**

---

# 7. \(H\) 不是 quotient；它是两个 actual quotients 的差

普遍 conjecture：

\[
H\stackrel{?}=\left\lfloor\frac{b_2P_2}{10^g}\right\rfloor
\]

是错误的。

正确关系来自：

\[
b_2P_2-K_3=10^gH.
\]

令：

\[
r_g:=b_2P_2\bmod10^g=K_3\bmod10^g,
\]

\[
Q_2:=\left\lfloor\frac{b_2P_2}{10^g}\right\rfloor,
\qquad
Q_3:=\left\lfloor\frac{K_3}{10^g}\right\rfloor.
\]

则：

\[
b_2P_2=10^gQ_2+r_g,
\]

\[
K_3=10^gQ_3+r_g,
\]

故：

\[
\boxed{H=Q_2-Q_3.}
\tag{QDIFF}
\]

也就是说：

\[
\boxed{
H\text{ 是两个共享同一 }g\text{-digit suffix 的整数在删除该 suffix 后的 quotient difference。}
}
\]

这是比“\(H\) 是 prefix quotient”更准确的 carry interpretation。

**状态：NEW PROVED / original quotient conjecture FAILED.**

---

# 8. Denominator resonance integer \(R\)

定义：

\[
\boxed{R:=b_2 10^{n_3}-b_3.}
\tag{R0}
\]

因为：

\[
m_3+d=(n_3+g)+(m_2-g)=m_2+n_3,
\]

有：

\[
\boxed{
\beta_2-\beta_3 10^{-d}
=
\frac{R}{10^{m_2+n_3}}.
}
\tag{R1}
\]

所以 \(R\) 正是 MB3 主 resonance 的 integer numerator。

**状态：NEW PROVED.**

---

# 9. Digit-length orientation of \(R\)

令：

\[
M:=m_2+n_3.
\]

整数 \(b_2 10^{n_3}\) 有恰好 \(M\) 位，而 \(b_3\) 有：

\[
m_3=M-d
\]

位。

因此：

### Theorem R-DIGIT

\[
\boxed{d\ge1\Longrightarrow R>0}
\]

\[
\boxed{d\le-1\Longrightarrow R<0}
\]

\[
\boxed{R=0\Longrightarrow d=0.}
\]

更精确地：

若 \(d\ge1\)：

\[
\boxed{
R
\ge
10^{M-1}-10^{M-d}+1.
}
\tag{R+}
\]

特别：

\[
d=1\Longrightarrow R\ge1,
\]

而：

\[
d\ge2\Longrightarrow
\frac{R}{10^M}>0.1-10^{-d}\ge0.09.
\]

若 \(d=-1\)：

因为：

\[
b_3\ge10^M,
\qquad
b_2 10^{n_3}\le10^M-10^{n_3},
\]

故：

\[
\boxed{-R\ge10^{n_3}.}
\tag{R-1}
\]

这个 \(d=-1\) 的 discrete gap 将在第 16 节直接关闭 minus transition slice。

**状态：NEW PROVED.**

---

# 10. Direct \(H\)–\(R\) integer identity

把：

\[
P_2=Q_0-d_2
\]

代入 H3，并使用：

\[
R=b_2 10^{n_3}-b_3,
\]

得到：

\[
\boxed{
10^{m_3}H
=
Q_0R
-
b_2d_2 10^{n_3}
+
b_3P_3.
}
\tag{HR}
\]

这是本轮最重要的 exact integer identity 之一。

它把：

- leading defect \(H\)；
- denominator mantissa mismatch \(R\)；
- canonical radial gap \(d_2\)；
- small third primitive coordinate \(P_3\)

压入一个四项整数关系。

与 MB3 相比，(HR) 没有任何 real mantissa、Big-O 或 floating approximation。

**状态：NEW PROVED TERMINAL INTEGER NORMAL FORM.**

---

# 11. Pairwise-gcd normalized \(R\)

令：

\[
h_{23}:=\gcd(g_2,g_3),
\]

\[
p:=\frac{g_3}{h_{23}},
\qquad
q:=\frac{g_2}{h_{23}},
\qquad
\gcd(p,q)=1,
\]

以及：

\[
c_{23}:=\gcd(b_2,b_3)
=
\frac{V}{\operatorname{lcm}(g_2,g_3)}.
\]

则：

\[
b_2=c_{23}p,
\qquad
b_3=c_{23}q.
\]

从而：

\[
\boxed{
R=c_{23}\widehat R,
\qquad
\widehat R:=p10^{n_3}-q.
}
\tag{RRED}
\]

故 generic case \(R\ne0\) 至少有：

\[
\boxed{|R|\ge c_{23}=\gcd(b_2,b_3).}
\tag{RGAP}
\]

这比 prompt 中候选的 \(V/(g_2g_3)\) 更强。

但它仍不够闭合 generic A1，因为 \(c_{23}\) 可以等于 1，且 \(|\widehat R|\) 可以等于 1。

---

# 12. Primitive tail defect in \(R\)-coordinates

定义：

\[
E_3:=\frac{\Delta_3}{h_{23}}.
\]

则：

\[
E_3
=
pP_2 10^{n_3}-q(Q_0-P_3).
\]

代入 \(P_2=Q_0-d_2\)：

\[
\boxed{
E_3
=
Q_0\widehat R
-
pd_2 10^{n_3}
+
qP_3.
}
\tag{E3-R}
\]

同时由 H3：

\[
\boxed{
10^{m_3}H
=
c_{23}E_3.
}
\tag{H-E3}
\]

因此 (HR) 的真正 primitive 版本是：

\[
\boxed{
\frac{\Delta_3}{\gcd(g_2,g_3)}
=
Q_0\left(
\frac{g_3}{h_{23}}10^{n_3}-\frac{g_2}{h_{23}}
\right)
-
\frac{g_3}{h_{23}}d_2 10^{n_3}
+
\frac{g_2}{h_{23}}P_3.
}
\]

这说明 \(R\) 并非外加变量；它是 primitive gcd-ratio defect 的 leading coefficient。

**状态：NEW PROVED.**

---

# 13. Three-denominator Smith normal form

本轮进一步把 denominator triple 的真正 gcd redundancy 完全抽掉。

定义：

\[
s:=\gcd(b_1,b_2,b_3),
\]

\[
c_{12}:=\gcd(b_1,b_2),
\qquad
c_{23}:=\gcd(b_2,b_3),
\]

\[
\alpha:=\frac{c_{12}}s,
\qquad
\beta:=\frac{c_{23}}s.
\]

primewise 可立即看出：

\[
\boxed{\gcd(\alpha,\beta)=1.}
\]

因为若同一 prime 在 \(\alpha,\beta\) 中都出现，则它在三块 denominator 中的共同 exponent 应大于 \(s\)，矛盾。

又因：

\[
\operatorname{lcm}(c_{12},c_{23})=s\alpha\beta\mid b_2,
\]

定义：

\[
t:=\frac{b_2}{s\alpha\beta},
\qquad
u:=\frac{b_1}{s\alpha},
\qquad
v:=\frac{b_3}{s\beta}.
\]

则：

\[
\boxed{
b_1=s\alpha u}
\]

\[
\boxed{
b_2=s\alpha\beta t}
\]

\[
\boxed{
b_3=s\beta v.}
\]

并且 pairwise gcd exactness 等价给：

\[
\boxed{\gcd(u,\beta t)=1}
\]

\[
\boxed{\gcd(\alpha t,v)=1.}
\]

这是本轮最自然的 denominator lattice chart。

---

# 14. Smith bridge for \(H\)

在第 13 节坐标中定义：

\[
\widehat H
:=
\beta tQ_0-u10^{m_2}D,
\]

\[
E_3
:=
\alpha tP_2 10^{n_3}-v(Q_0-P_3).
\]

则：

\[
H=s\alpha\widehat H,
\]

而 H3 给：

\[
10^{m_3}s\alpha\widehat H
=
s\beta E_3.
\]

约去 \(s\)：

\[
\boxed{
\alpha10^{m_3}\widehat H
=
\beta E_3,
\qquad
\gcd(\alpha,\beta)=1.
}
\tag{SNF}
\]

因此存在一个整数 \(Z\) 使：

\[
\boxed{E_3=\alpha Z}
\]

\[
\boxed{10^{m_3}\widehat H=\beta Z.}
\]

这就是本轮低维 coefficient lattice 的 Smith 型 normal form。

**状态：NEW PROVED.**

---

# 15. New exact denominator-gcd allocation theorem

由：

\[
\alpha\mid E_3
\]

和：

\[
E_3
=
\alpha tP_2 10^{n_3}-v(Q_0-P_3),
\]

模 \(\alpha\)：

\[
E_3\equiv-v(Q_0-P_3)\pmod\alpha.
\]

又：

\[
\gcd(v,\alpha)=1
\]

来自 \(\gcd(\alpha t,v)=1\)。因此：

\[
\boxed{
\alpha\mid(Q_0-P_3).
}
\tag{ALLOC-A}
\]

另一方面：

\[
\beta\mid10^{m_3}\widehat H.
\]

而：

\[
\widehat H
=
\beta tQ_0-u10^{m_2}D.
\]

故：

\[
\beta
\mid
u10^{m_2+m_3}D.
\]

由：

\[
\gcd(u,\beta)=1
\]

得：

\[
\boxed{
\beta\mid10^{m_2+m_3}D.
}
\tag{ALLOC-B}
\]

特别，若记去掉 \(2,5\) 后的 ten-free core 为 \(N^{\langle10\rangle}\)，则：

\[
\boxed{
\beta^{\langle10\rangle}\mid D.
}
\tag{ALLOC-B*}
\]

这两条整除不是旧 primitive-only support 的复读；它们是从 actual denominator gcd lattice + exact H synchronization 才出现的。

**状态：NEW PROVED — MAJOR.**

---

# 16. New \(1\bmod4\) support theorem for denominator asymmetry

使用第四轮已经冻结的：

\[
V=\operatorname{lcm}(b_1,b_2,b_3),
\]

\[
g_i=V/b_i=\gcd(V,P_i).
\]

### Theorem ASYM-4

任意 odd prime：

\[
p\equiv3\pmod4
\]

都不能整除 \(\alpha\) 或 \(\beta\)。

因此：

\[
\boxed{
\alpha^{\langle10\rangle}
\text{ 与 }
\beta^{\langle10\rangle}
\text{ 的所有 prime factors 均为 }1\pmod4.
}
\tag{ASYM-4}
\]

### Proof for \(p\mid\alpha\)

\(p\mid\alpha\) 意味着：

\[
v_p(\gcd(b_1,b_2))
>
\min_i v_p(b_i),
\]

所以 \(b_3\) 的 \(p\)-exponent 严格低于 \(b_1,b_2\)。因此 \(V/b_3=g_3\) 含 \(p\)，故：

\[
p\mid P_3.
\]

又由 (ALLOC-A)：

\[
p\mid Q_0-P_3,
\]

所以：

\[
p\mid Q_0.
\]

另一方面，\(b_1,b_2\) 中至少一个达到 \(V\) 的 maximal \(p\)-exponent，所以对应的 \(g_1\) 或 \(g_2\) 不含 \(p\)，因此对应的 \(P_1\) 或 \(P_2\) 不含 \(p\)。

sphere 模 \(p\)：

\[
P_1^2+P_2^2\equiv0\pmod p.
\]

若 \(p\equiv3\pmod4\)，则 \(-1\) 非平方，强迫：

\[
p\mid P_1,P_2,
\]

与至少一个 coordinate \(p\)-free 矛盾。

### Proof for \(p\mid\beta\)

若 \(p\equiv3\pmod4\)，则 \(p\ne2,5\)。由 (ALLOC-B)：

\[
p\mid D.
\]

而 \(p\mid\beta\) 意味着 \(b_1\) 的 \(p\)-exponent 严格低于 \(b_2,b_3\)，故：

\[
p\mid g_1\mid P_1.
\]

因：

\[
D=P_110^k-Q_0,
\]

且 \(p\nmid10\)，得到：

\[
p\mid Q_0.
\]

sphere 模 \(p\)：

\[
P_2^2+P_3^2\equiv0\pmod p.
\]

但 \(b_2,b_3\) 中至少一个达到 maximal \(p\)-exponent，对应 \(P_2\) 或 \(P_3\) 为 \(p\)-free，故 \(p\equiv3\pmod4\) 不可能。

证毕。

**状态：NEW PROVED.**

---

# 17. Transition closure: \(d=-1\) minus is impossible

这是本轮一个低成本但实质的新 closure。

假设：

\[
g\ge1,
\qquad
d=-1,
\qquad\text{minus}.
\]

此时：

\[
m_2=g-1,
\]

并由第 9 节：

\[
10\beta_3-\beta_2
=
\frac{b_3-b_2 10^{n_3}}{10^{m_2+n_3}}
\ge
10^{-m_2}
=
10^{1-g}.
\tag{17.1}
\]

minus condition 是：

\[
\beta_2x
>
10\beta_3(1-y).
\]

整理：

\[
10\beta_3 y
>
10\beta_3-\beta_2x
=
(10\beta_3-\beta_2)+\beta_2(1-x)
\ge
10^{1-g}.
\]

而：

\[
\beta_3<1,
\]

所以：

\[
10y>10^{1-g},
\]

即：

\[
\boxed{y>10^{-g}.}
\tag{17.2}
\]

第五轮 MP-11 给：

\[
y<100\,10^{-(2g+k)}.
\]

因此：

\[
10^{-g}
<
100\,10^{-(2g+k)},
\]

即：

\[
10^{g+k}<100.
\]

但：

\[
g\ge1,
\qquad k\ge1,
\]

且 \(d=-1\) 实际还要求 \(m_2=g-1\ge1\)，故 \(g\ge2\)。于是明显矛盾。

因此：

\[
\boxed{
g\ge1,\ d=-1\Longrightarrow\text{minus impossible}.}
\tag{D-1-CLOSE}
\]

结合第五轮：

\[
g\ge1,\ \text{minus}\Longrightarrow d\ge-1,
\]

得到改进：

\[
\boxed{
g\ge1,\ \text{minus}\Longrightarrow d\ge0.}
\tag{MINUS-D0}
\]

**状态：NEW PROVED — transition slice closed.**

---

# 18. Plus branch: exact leading decimal prefix theorem

plus 中：

\[
H<0.
\]

由 (H2)：

\[
-H
=
Q_0\left[
\beta_3(1-y)-10^d\beta_2x
\right].
\]

plus sign 保证括号正；同时：

\[
\beta_3(1-y)<1.
\]

所以：

\[
\boxed{0<-H<Q_0.}
\tag{PLUS-H}
\]

令：

\[
A_0:=b_1D.
\]

从 H0：

\[
10^{m_2}A_0=b_2Q_0-H.
\]

plus 时写 \(J:=-H\)，则：

\[
\boxed{
10^{m_2}A_0=b_2Q_0+J,
\qquad
0<J<Q_0.
}
\tag{LD+}
\]

因此：

\[
\boxed{
\left\lfloor
10^{m_2}\frac{A_0}{Q_0}
\right\rfloor
=b_2.
}
\]

即：

\[
\boxed{
\operatorname{Pref}_{m_2}(\varepsilon)=b_2.
}
\tag{PREFIX+}
\]

这不是 \(O(10^{-g})\) 意义的近似，而是 exact decimal-prefix equality。

更具体地：

\[
\boxed{
10^{m_2}\varepsilon
=b_2+\frac{-H}{Q_0},
\qquad
0<\frac{-H}{Q_0}<1.
}
\]

所以 \(\varepsilon\) 的十进制展开可以严格读作：

> 先出现 denominator block \(b_2\) 的全部 \(m_2\) 位，然后继续展开 \((-H)/Q_0\)。

**状态：NEW PROVED — EXACT PREFIX REDUCTION.**

---

# 19. Leading denominator-prefix Euclidean quotient

定义 actual denominator prefix：

\[
Q_{12}:=b_1 10^{m_2}+b_2.
\]

由：

\[
D=P_110^k-Q_0
\]

和 H0：

\[
\boxed{
 b_1P_1 10^{m_2+k}
=
Q_0Q_{12}-H.
}
\tag{LEAD-EUCLID}
\]

plus 中 \(-H\in(0,Q_0)\)，因此：

\[
\boxed{
Q_{12}
=
\left\lfloor
\frac{b_1P_1 10^{m_2+k}}{Q_0}
\right\rfloor.
}
\tag{Q12+}
\]

且 remainder 恰为：

\[
\boxed{-H.}
\]

所以 plus branch 中，actual first-two-denominator word \(Q_{12}\) 被 primitive data 通过一次 Euclidean division **精确恢复**。

这是一个比普通 mantissa closeness 更强的 source-visible statement。

**状态：NEW PROVED.**

---

# 20. Minus branch: exact borrow/carry normal form

由第 17 节，growing-\(g\) minus 已有：

\[
d\ge0.
\]

由 (H2)：

\[
0<H
<
Q_0 10^d\beta_2x
<
10^dQ_0.
\]

故定义：

\[
\boxed{
c:=\left\lceil\frac{H}{Q_0}\right\rceil}
\]

则：

\[
\boxed{1\le c\le10^d.}
\tag{BORROW}
\]

并且：

\[
10^{m_2}A_0
=b_2Q_0-H
=(b_2-c)Q_0+(cQ_0-H),
\]

其中：

\[
0\le cQ_0-H<Q_0.
\]

因此：

\[
\boxed{
\left\lfloor10^{m_2}\varepsilon\right\rfloor
=b_2-c.
}
\tag{PREFIX-}
\]

这给出一个 canonical decimal borrow integer \(c\)。

### Special slice \(d=0\)

此时：

\[
0<H<Q_0,
\]

所以：

\[
\boxed{c=1}
\]

\[
\boxed{
\operatorname{Pref}_{g}(\varepsilon)=b_2-1.
}
\tag{D0-PREFIX}
\]

且：

\[
10^g\varepsilon
=(b_2-1)+\frac{Q_0-H}{Q_0}.
\]

这与 plus 的 \(b_2\) prefix 形成精确一位 borrow 二分。

**状态：NEW PROVED.**

---

# 21. Minus branch: carry-safe g-digit prefix synchronization

一般 minus \(d\ge0\) 中：

\[
m_2=g+d.
\]

写：

\[
b_2=B10^d+L,
\qquad
0\le L<10^d,
\]

其中：

\[
B=\left\lfloor\frac{b_2}{10^d}\right\rfloor
=
\operatorname{Pref}_{g}(\beta_2).
\]

因为：

\[
1\le c\le10^d,
\]

减去 \(c\) 最多只会向前借 1 次，所以：

\[
\left\lfloor\frac{b_2-c}{10^d}\right\rfloor
\in\{B,B-1\}.
\]

又：

\[
\operatorname{Pref}_{g}(\varepsilon)
=
\left\lfloor
\frac{\lfloor10^{m_2}\varepsilon\rfloor}{10^d}
\right\rfloor.
\]

故：

\[
\boxed{
\operatorname{Pref}_{g}(\varepsilon)
\in
\left
\{
\operatorname{Pref}_{g}(\beta_2),
\operatorname{Pref}_{g}(\beta_2)-1
\right\}.
}
\tag{G-PREFIX-}
\]

这是一条真正处理 carry/borrow 的 exact prefix theorem。

它比“\(|\beta_2-\varepsilon|<10^{-g}\) 所以前 \(g\) 位相同”更准确，因为后一说法会在 decimal boundary 处失败。

**状态：NEW PROVED — EXACT PREFIX WITH ONE BORROW BIT.**

---

# 22. Minus \(d\ge2\): fixed-scale H theorem

若：

\[
g\ge1,
\qquad d\ge2,
\]

第五轮给：

\[
x>\sqrt{96/101}.
\]

由：

\[
\frac{H}{10^dQ_0}
=
\beta_2x-\beta_3(1-y)10^{-d},
\]

使用：

\[
\beta_2\ge0.1,
\quad
\beta_3<1,
\quad
1-y<1,
\quad
10^{-d}\le0.01,
\]

得到：

\[
\boxed{
\frac{H}{10^dQ_0}
>
0.1\sqrt{96/101}-0.01
>0.08749.
}
\]

而显然：

\[
H<10^dQ_0.
\]

所以：

\[
\boxed{
0.08749\,10^dQ_0
< H
<10^dQ_0.
}
\tag{H-SCALE}
\]

这严格锁定了 minus large-positive-\(d\) 的 defect scale。

但本轮没有找到一个 universal divisor 大于该 magnitude，因此这条 theorem 尚不能单独关闭 \(d\to+\infty\)。

**状态：NEW PROVED / NOT CLOSING.**

---

# 23. Exact resonance \(R=0\)

由 R0：

\[
R=0
\iff
b_3=b_2 10^{n_3}.
\]

比较 digit lengths：

左边 \(b_3\) 有：

\[
m_3=n_3+g
\]

位；右边 \(b_2 10^{n_3}\) 有：

\[
m_2+n_3
\]

位。

因此：

\[
\boxed{m_2=g}
\]

即：

\[
\boxed{d=0.}
\tag{R-D0}
\]

并且：

\[
\boxed{\beta_2=\beta_3.}
\]

再由：

\[
\frac{b_3}{b_2}
=
\frac{g_2}{g_3},
\]

得到：

\[
\boxed{g_2=10^{n_3}g_3.}
\tag{R-G}
\]

特别：

\[
\boxed{10^{n_3}\mid g_2\mid P_2.}
\]

**状态：NEW PROVED.**

---

# 24. Resonance in Smith coordinates is even more rigid

在第 13 节 coordinates 中：

\[
R=s\beta(\alpha t10^{n_3}-v).
\]

若 \(R=0\)，则：

\[
v=\alpha t10^{n_3}.
\]

但：

\[
\gcd(\alpha t,v)=1.
\]

因此：

\[
\boxed{\alpha t=1}
\]

即：

\[
\boxed{\alpha=1,\qquad t=1}
\]

以及：

\[
\boxed{v=10^{n_3}.}
\]

所以 denominator triple 必退化成：

\[
\boxed{
b_1=su}
\]

\[
\boxed{
b_2=s\beta}
\]

\[
\boxed{
b_3=s\beta 10^{n_3}}
\]

\[
\boxed{\gcd(u,\beta)=1.}
\tag{R-DEN}
\]

特别：

\[
\boxed{
\gcd(b_1,b_2)=\gcd(b_1,b_2,b_3)=s,
}
\]

\[
\boxed{
\gcd(b_2,b_3)=b_2.
}
\]

这比单独 \(g_2=10^{n_3}g_3\) 更完整地描述了 resonant denominator geometry。

**状态：NEW PROVED — RESONANT NORMAL FORM.**

---

# 25. Resonance-specific leading divisor

在 resonance 中：

\[
\alpha=1,
\qquad t=1.
\]

ALLOC-B 变成：

\[
\boxed{
\beta\mid10^{m_2+m_3}D.
}
\]

因此：

\[
\boxed{
\beta^{\langle10\rangle}\mid D.
}
\tag{R-BETA-D}
\]

并由 ASYM-4：

\[
\boxed{
\text{每个 }p\mid\beta^{\langle10\rangle}
\text{ 都满足 }p\equiv1\pmod4.
}
\]

所以 resonant locus 若继续逃逸，其 \(b_2/s\) 的 nondecimal content 必完全由 \(1\bmod4\) primes 构成并进入 small leading gap \(D\)。

这没有闭合 resonance，但已经把其 nondecimal denominator freedom压得非常具体。

---

# 26. Resonance simplifies H to one primitive integer gap

在 \(R=0\) 时，HR 变成：

\[
10^{m_3}H
=
-b_2d_2 10^{n_3}+b_3P_3.
\]

使用：

\[
b_3=b_2 10^{n_3},
\qquad
m_3=n_3+g,
\]

得到：

\[
\boxed{
10^gH
=
b_2(P_3-d_2).
}
\]

而：

\[
P_3-d_2
=P_2+P_3-Q_0.
\]

所以：

\[
\boxed{
10^gH
=
b_2(P_2+P_3-Q_0).
}
\tag{R-H}
\]

flat 已删除，故：

\[
\boxed{P_2+P_3\ne Q_0.}
\]

而：

\[
(P_2+P_3)^2-Q_0^2
=
2P_2P_3-P_1^2.
\]

因此 resonant branch sign 具有 exact primitive interpretation：

\[
\boxed{
\text{minus}
\iff
P_2+P_3>Q_0
\iff
2P_2P_3>P_1^2,
}
\]

\[
\boxed{
\text{plus}
\iff
P_2+P_3<Q_0
\iff
2P_2P_3<P_1^2.
}
\tag{R-SIGN}
\]

**状态：NEW PROVED.**

---

# 27. Resonant sign is confined by \(k-2g\)

对 \(g\ge1\)，第五轮 bounds 给：

\[
P_2>\sqrt{96/101}\,Q_0,
\]

\[
\frac{Q_0}{1100\,10^{2g+k}}<P_3<100Q_0\,10^{-(2g+k)},
\]

\[
Q_0 10^{-k}<P_1<2Q_0 10^{-k}.
\]

因此：

\[
\frac{2P_2P_3}{P_1^2}
<
200\,10^{k-2g}.
\]

若：

\[
k\le2g-3,
\]

则右边 \(<1\)，故 resonance 必为 plus。

另一方面：

\[
\frac{2P_2P_3}{P_1^2}
>
\frac{\sqrt{96/101}}{2200}
10^{k-2g}.
\]

若：

\[
k\ge2g+4,
\]

则右边 \(>1\)，故 resonance 必为 minus。

所以只有：

\[
\boxed{
-2\le k-2g\le3
}
\]

仍然是 resonant sign-sensitive transition strip。

**状态：NEW PROVED COARSE RESONANT CLASSIFICATION.**

---

# 28. Third-tail divisibility can be combined with the old primitive divisor

前轮已有：

\[
10^{n_3}
\mid
g_1g_2(Q_0-P_3).
\]

本轮新得：

\[
10^{n_3}
\mid
b_3(Q_0-P_3).
\]

primewise 取 coefficient 的较小 valuation：

\[
\boxed{
10^{n_3}
\mid
\gcd(b_3,g_1g_2)(Q_0-P_3).
}
\tag{TAIL-GCD}
\]

这比任一单独 divisor 更强。

但在 exact resonance：

\[
b_3=b_2 10^{n_3},
\qquad
g_2=g_3 10^{n_3},
\]

所以两侧 coefficient 都自动携带 \(10^{n_3}\)，(TAIL-GCD) 完全失去强制力。

因此：

\[
\boxed{
R=0
\text{ 正是 third-tail decimal divisibility 被 denominator/gcd profile 自身完全吸收的 exceptional locus。}
}
\]

这是本轮对 resonant locus 为什么危险的一个结构解释。

---

# 29. Exact \(Q_0\)-content of \(H\)

由：

\[
H=b_2Q_0-b_1 10^{m_2}D
\]

得：

\[
\gcd(H,Q_0)
=
\gcd(b_1 10^{m_2}D,Q_0).
\]

又：

\[
D\equiv P_1 10^k\pmod{Q_0},
\]

所以：

\[
\boxed{
\gcd(H,Q_0)
=
\gcd(b_1P_1 10^{m_2+k},Q_0).
}
\tag{HQ0}
\]

特别对任意：

\[
p\ne2,5,
\qquad p\mid Q_0,
\]

有：

\[
\boxed{
p\mid H\iff p\mid b_1P_1.}
\tag{HQ0-PRIME}
\]

因此 \(H\) 不会无缘无故吸收 \(Q_0\) 的 nondecimal core。

这回答了 prompt 中的 \(Q_0\)-content question，但方向是“content rigidity / absence”，而不是“\(H\) 自动含有 huge \(Q_0\)-divisor”。

**状态：NEW PROVED.**

---

# 30. Exact \(2,5\)-valuation tree of \(H\)

对 \(p\in\{2,5\}\)，设：

\[
A_p:=v_p(b_2Q_0),
\]

\[
B_p:=v_p(b_1)+m_2+v_p(D).
\]

因为：

\[
H=b_2Q_0-b_1 10^{m_2}D,
\]

得到标准 exact two-term valuation tree：

\[
\boxed{
A_p<B_p\Longrightarrow v_p(H)=A_p,
}
\]

\[
\boxed{
B_p<A_p\Longrightarrow v_p(H)=B_p,
}
\]

而：

\[
A_p=B_p
\]

是唯一 cancellation chamber，此时：

\[
v_p(H)\ge A_p
\]

并由 normalized unit difference 决定额外深度。

又 primitive sphere 给 \(Q_0\) odd；且 \(10^kP_1\) 为偶数，所以：

\[
\boxed{D\text{ odd}.}
\]

因此：

\[
A_2=v_2(b_2),
\qquad
B_2=v_2(b_1)+m_2.
\]

本轮没有发现 universal valuation inequality 能从该 tree 单独关闭 A1；它最有价值的作用是准确定位 cancellation chamber，避免误把普通 congruence 当 large divisor theorem。

**状态：NEW PROVED CLASSIFICATION / NO CLOSURE.**

---

# 31. Why \(V\mid H\) is false as a structural expectation

由第 4 节：

\[
H=c_{12}\widehat H,
\qquad
c_{12}=\frac{V}{\operatorname{lcm}(g_1,g_2)}.
\]

因此真正 universal guaranteed factor 只是：

\[
\boxed{c_{12}=\gcd(b_1,b_2).}
\]

并且：

\[
\boxed{
V\mid H
\iff
\operatorname{lcm}(g_1,g_2)\mid\widehat H.
}
\]

没有任何定义性理由保证后者。

第三轮 exact synchronized pseudo-state：

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),
\]

\[
(b_1,b_2,b_3)=(1,6,8),
\qquad
V=24,
\]

\[
m_2=n_3=m_3=k=1,
\qquad g=0,
\]

有：

\[
D=71,
\]

\[
H=6\cdot169-10\cdot71=304.
\]

但：

\[
24\nmid304.
\]

该 state 最终死于 common-\(U\) gate，所以它不反驳“所有 full A1 candidate vacuously satisfy any statement”；但它严格说明：

\[
\boxed{
V\mid H
\text{ 不能从 primitive sphere + GSYNC + exact common-}V\text{ profile 推出。}
}
\]

**状态：FAILED AS A STRUCTURAL ROUTE.**

---

# 32. Generic \(R\neq0\): quantitative distance is real but not automatically strong

由 RRED：

\[
|R|
\ge
c_{23}
=
\gcd(b_2,b_3).
\]

所以：

\[
\left|
\beta_2-\beta_3 10^{-d}
\right|
\ge
\frac{\gcd(b_2,b_3)}{10^{m_2+n_3}}.
\]

但不能进一步无条件升级成一个 fixed constant 或 \(Q_0^{-1/2+\eta}\) gap。

原因是 denominator layer 自身允许 exact unit residual。

例如在 \(d=0\)、\(g=1\) 的合法 digit skeleton 中，可以取：

\[
b_2=2,
\qquad
b_3=2\cdot10^{n_3}-1,
\]

则 \(b_3\) 恰有 \(n_3+1\) 位，且：

\[
\boxed{R=1.}
\]

同样：

\[
b_2=1,
\qquad
b_3=10^{n_3}+1
\]

给：

\[
\boxed{R=-1.}
\]

这些只是 denominator skeleton，不声称满足 sphere/master/common-\(U\)；它们的作用是严格否定：

> “terminating mantissa + common denominator presentation 本身会给 \(|R|\) 一个 growing lower bound”。

因此 generic \(R\neq0\) 若要关闭，必须真正使用 primitive geometry / H bridge / gcd allocation，而不能只用 \(|R|\ge1\)。

**状态：FAILED standalone conjecture.**

---

# 33. Exact resonance is not automatically impossible

本轮证明了：

\[
R=0
\Longrightarrow
\left
\{
\begin{aligned}
&d=0,\\
&b_3=b_2 10^{n_3},\\
&g_2=10^{n_3}g_3,\\
&\beta_2=\beta_3,\\
&\alpha=t=1,\\
&10^gH=b_2(P_2+P_3-Q_0).
\end{aligned}
\right.
\]

但是尚未得到 contradiction。

特别：

\[
10^{n_3}\mid P_2
\]

只给：

\[
Q_0^2\equiv P_1^2+P_3^2\pmod{10^{2n_3}},
\]

而 primitive sphere 本身允许大量 coordinate 被深度 \(10\)-整除的点；因此“deep square congruence”不能直接冒充 resonant closure。

本轮有限搜索同样未找到 resonant original A1 hit，但这只属于实验信号。

**状态：OPEN.**

---

# 34. Computational experiments

本轮计算只用于 identity audit / falsification，不用于全局 nonexistence theorem。

## 34.1 Symbolic identity audit

用 exact symbolic expansion 核对：

\[
b_2P_2 10^{n_3}-b_3(Q_0-P_3)
\]

与：

\[
Q_0R-b_2d_2 10^{n_3}+b_3P_3
\]

完全一致。

因此 (HR) 无隐藏 sign/exponent bug。

## 34.2 Direct original-equation scan: smallest growing-g transition profile

扫描：

\[
g=1,
\quad
k=1,
\quad
d=0,
\quad
m_2=1,
\quad
n_3=1,
\]

故：

\[
m_3=2,
\qquad
n_2=3.
\]

取：

- \(a_1,b_1,a_3,b_2\) 全部一位数；
- \(b_3\) 遍历全部两位数；
- \(a_2\) 遍历/通过 exact quadratic discriminant recovery 检查全部三位数；
- 每个 \(a_i/b_i\) 要求 reduced；
- 直接核验 original concatenation-square equation。

结果：

\[
\boxed{0\text{ hits}.}
\]

## 34.3 Resonant subset

进一步强制：

\[
b_3=10b_2,
\]

并把：

\[
a_1,b_1
\]

扩到 \(1\)–\(99\)，其余保持上述最小 profile。

结果仍为：

\[
\boxed{0\text{ hits}.}
\]

**状态：EXPERIMENTAL ONLY.**

这些数据与 “resonant locus 很薄” 相容，但远不足以证明其为空。

---

# 35. Explicit counterexamples / failed conjectures

## FAILED 1 — “\(H\) 就是 \(b_2P_2\) 去掉后 \(g\) 位的 quotient”

错误。正确的是：

\[
H=Q_2-Q_3.
\]

第三轮 pseudo-state \((b_2P_2,K_3,g)=(312,8,0)\) 已直接显示 \(H=304\ne312\)。

## FAILED 2 — “\(V\mid H\)”

无结构保证；第三轮 synchronized pseudo-state 有 \(V=24,H=304\)。

## FAILED 3 — “\(R\neq0\) 自动有强 gap”

错误；denominator digit skeleton 可有 \(R=\pm1\)。

## FAILED 4 — “\(d=-1\) minus 仅由 \(10\beta_3\ge1>\beta_2\) 直接矛盾”

该 naive argument 忽略 \(x,1-y\) 因子，不成立。

但把 exact digit gap \(-R\ge10^{n_3}\) 与 MP-11 的 \(P_3\)-height 联立后，\(d=-1\) minus **确实被严格关闭**。

## FAILED 5 — “\(R=0\) 自动 contradiction”

本轮只能压到 rigid resonant normal form，尚未 contradiction。

## FAILED 6 — “mantissa balance alone 会给 absolute \(|d|\)-bound”

没有。large-positive minus 与 large-negative plus 在纯 size 层仍相容。

---

# 36. Status of \(d\)

对 \(g\ge1\)：

第五轮：

\[
\text{plus}\Longrightarrow d\le1,
\]

本轮：

\[
\text{minus}\Longrightarrow d\ge0.
\]

所以当前 branch map 改进为：

\[
\boxed{d\le-1\Longrightarrow\text{plus}}
\]

\[
\boxed{d\ge2\Longrightarrow\text{minus}}
\]

而真正 dual-sign transition 只剩：

\[
\boxed{d\in\{0,1\}.}
\]

其中：

- \(d=0\)：plus/minus 均可能；resonance \(R=0\) 只可能在此；
- \(d=1\)：minus 通常自然，plus 仍 OPEN；
- \(d=-1\)：minus 已关闭，只剩 plus。

这比第五轮的 \(\{-1,0,1\}\) transition strip 再少一层。

**状态：NEW PROVED COMPRESSION.**

---

# 37. Status of \(g\)

本轮没有得到：

\[
g\le G
\]

的 absolute bound。

已有：

\[
10^{2g+k-2}<Q_0,
\]

\[
10^{2k}<5Q_0
\qquad(g\ge1),
\]

仍只给：

\[
g,k=O(\log Q_0).
\]

本轮的新 exact prefix/suffix theorems说明：

\[
g\to\infty
\]

若发生，不再只是 real approximation 越来越好，而是会制造：

1. plus：越来越长的 exact leading prefix \(b_2\)；
2. minus：长度 \(g\) 的 prefix 至多差一个 borrow bit；
3. 所有 branch：third-tail quotient 与 \(b_2P_2\) 有 exact \(g\)-digit suffix congruence。

所以 \(g\) 的下一次 closure 应攻击这些 exact words，而不是继续做 sector size。

---

# 38. Status of \(n_3\)

本轮没有证明 \(n_3\) absolute bounded。

新 divisor：

\[
10^{n_3}\mid b_3(Q_0-P_3)
\]

与：

\[
10^{n_3}\mid g_1g_2(Q_0-P_3)
\]

可合并成 (TAIL-GCD)，但 coefficient 本身可以随 profile 移动。

更重要的是 resonance 中：

\[
b_3\text{ 与 }g_2
\]

都自动含 \(10^{n_3}\)，所以该机制对 \(R=0\) 完全饱和。

因此：

\[
\boxed{n_3\text{ boundedness remains OPEN}.}
\]

---

# 39. Special audit: \(g=0\)

本轮的 strongest \(P_2\)-axis constants 与 \(d=-1\) closure只针对 \(g\ge1\)。

当：

\[
g=0,
\]

有：

\[
d=m_2\ge1.
\]

因此：

- resonance \(R=0\Rightarrow d=0\) 自动说明：
  \[
  \boxed{g=0\text{ 时 }R=0\text{ 不可能};
  }
  \]
- plus 的 exact prefix theorem仍完全成立；
- H3/K3/tail suffix theorem仍完全成立；
- 第五轮 plus 给 \(d\le2\)，故 \(g=0\) plus 只剩 \(m_2=1,2\)；
- \(g=0\) minus 仍可能有任意正 \(m_2\)，本轮没有闭合。

因此 full A1 closure 仍必须保留 \(g=0\) minus chamber。

---

# 40. New Proven Lemma Ledger

### A1-EMDQ-1 — Exact H Normalization

\[
H=b_2Q_0-b_1 10^{m_2}D,
\qquad
\beta_2-\varepsilon=H/(10^{m_2}Q_0).
\]

**PROVED.**

### A1-EMDQ-2 — Pairwise Primitive Defect Quotient

\[
H=-\gcd(b_1,b_2)\,
\frac{\Delta_{12}}{\gcd(g_1,g_2)}.
\]

**PROVED.**

### A1-EMDQ-3 — Exact Third-Tail Quotient

\[
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbb Z_{>0}.
\]

**PROVED.**

### A1-EMDQ-4 — Exact g-Digit Tail Suffix

\[
K_3\equiv b_2P_2\pmod{10^g}.
\]

**PROVED.**

### A1-EMDQ-5 — Quotient-Difference Interpretation

\[
H=
\left\lfloor\frac{b_2P_2}{10^g}\right\rfloor
-
\left\lfloor\frac{K_3}{10^g}\right\rfloor.
\]

**PROVED.**

### A1-EMDQ-6 — Denominator Resonance Numerator

\[
R=b_210^{n_3}-b_3,
\qquad
\beta_2-\beta_3 10^{-d}=R/10^{m_2+n_3}.
\]

**PROVED.**

### A1-EMDQ-7 — H–R Integer Identity

\[
10^{m_3}H
=Q_0R-b_2d_2 10^{n_3}+b_3P_3.
\]

**PROVED.**

### A1-EMDQ-8 — Three-Denominator Smith Form

\[
\alpha10^{m_3}\widehat H=\beta E_3,
\qquad\gcd(\alpha,\beta)=1.
\]

**PROVED.**

### A1-EMDQ-9 — Asymmetric GCD Allocation

\[
\alpha\mid Q_0-P_3,
\qquad
\beta\mid10^{m_2+m_3}D.
\]

**PROVED.**

### A1-EMDQ-10 — Asymmetric \(1\bmod4\) Support

No odd \(3\bmod4\) prime divides \(\alpha\beta\).

**PROVED.**

### A1-EMDQ-11 — Minus \(d=-1\) Closure

\[
g\ge1,\ d=-1\Longrightarrow\text{minus impossible}.
\]

**PROVED.**

### A1-EMDQ-12 — Plus Exact Prefix

\[
\operatorname{Pref}_{m_2}(\varepsilon)=b_2.
\]

**PROVED.**

### A1-EMDQ-13 — Minus Exact Borrow

\[
\operatorname{Pref}_{m_2}(\varepsilon)=b_2-c,
\qquad
c=\lceil H/Q_0\rceil,
\qquad1\le c\le10^d.
\]

**PROVED.**

### A1-EMDQ-14 — Minus g-Prefix One-Borrow Theorem

\[
\operatorname{Pref}_{g}(\varepsilon)
\in
\{\operatorname{Pref}_{g}(\beta_2),\operatorname{Pref}_{g}(\beta_2)-1\}.
\]

**PROVED.**

### A1-EMDQ-15 — Exact Resonant Normal Form

\[
R=0
\Longrightarrow
\left
\{
\begin{aligned}
&d=0,\\
&b_3=b_210^{n_3},\\
&g_2=10^{n_3}g_3,\\
&\beta_2=\beta_3,\\
&\alpha=t=1.
\end{aligned}
\right.
\]

**PROVED.**

### A1-EMDQ-16 — Resonant Primitive Sign

\[
\operatorname{sgn}H
=
\operatorname{sgn}(P_2+P_3-Q_0)
=
\operatorname{sgn}(2P_2P_3-P_1^2).
\]

**PROVED.**

---

# 41. What did not close

本轮明确没有证明：

\[
R\ne0\Longrightarrow\text{contradiction},
\]

也没有证明：

\[
Q_0\to\infty\Longrightarrow R=0.
\]

原因不是缺一个普通 rational spacing：\(R\) 本身可以是 unit residual。

同样没有证明：

\[
R=0\Longrightarrow\text{contradiction}.
\]

resonance 目前被压成：

\[
\boxed{
\begin{gathered}
d=0,\quad m_2=g,\quad
b_3=b_210^{n_3},\quad
g_2=10^{n_3}g_3,\\
\beta_2=\beta_3,\quad
\alpha=t=1,\quad
\beta^{\langle10\rangle}\mid D,\\
10^gH=b_2(P_2+P_3-Q_0).
\end{gathered}
}
\]

这是一个很小但仍真实存在的 arithmetic chamber。

---

# 42. Infinite-escape classification after this round

若存在：

\[
Q_0\to\infty
\]

的 genuine A1 sequence，则对 \(g\ge1\) subsequence：

### Plus

\[
\boxed{d\le1}
\]

并且：

\[
\boxed{
\operatorname{Pref}_{m_2}(b_1D/Q_0)=b_2,
}
\]

同时：

\[
\boxed{
\frac{b_3(Q_0-P_3)}{10^{n_3}}
\equiv b_2P_2\pmod{10^g}.
}
\]

### Minus

\[
\boxed{d\ge0}
\]

并且：

\[
\boxed{
\operatorname{Pref}_{g}(b_1D/Q_0)
\in
\{\operatorname{Pref}_{g}(\beta_2),
\operatorname{Pref}_{g}(\beta_2)-1\},
}
\]

以及同一 exact tail suffix congruence。

### Resonant subsequence

若进一步 \(R=0\)：

\[
\boxed{
\text{全部 profile 自由度坍缩到第 41 节的 resonant normal form。}
}
\]

因此本轮已经把“real mantissa synchronization”升级为“two-sided exact decimal word synchronization”。

---

# 43. Remaining terminal obstruction

本轮之后，最小 forward obstruction 不再适合表述成：

> 为什么 \(\varepsilon\) 与 \(\beta_2\) 靠得太近？

更准确的是：

\[
\boxed{
\begin{gathered}
\text{为什么 primitive leading product }
 b_1P_1 10^{m_2+k}
\text{ 的 Euclidean quotient}\
\text{必须精确恢复 denominator prefix }Q_{12}
\text{（或只差一个 bounded borrow），}\
\text{同时 third-tail product }b_3(Q_0-P_3)
\text{ 又必须具有 }n_3\text{ 个 trailing zeros}\
\text{并在删除后复制 }b_2P_2\text{ 的 }g\text{-digit suffix？}
\end{gathered}
}
\]

而这两种 exact word constraints 还被：

\[
\alpha\mid(Q_0-P_3),
\qquad
\beta^{\langle10\rangle}\mid D
\]

及 ASYM-4 的 \(1\bmod4\) support 同时约束。

这已经是比 MB 明显更低维、更整数化的 terminal state。

---

# 44. Recommended next campaign

下一轮不建议重新研究 real mantissa distance。

最值得集中攻击两个对象：

## Target A — Double Euclidean Word Synchronization

同时使用：

\[
b_1P_1 10^{m_2+k}=Q_0Q_{12}-H,
\]

和：

\[
b_2P_2=10^gH+K_3,
\qquad
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}.
\]

目标是把同一个 \(H\) 作为：

- leading Euclidean remainder / borrow；
- tail quotient difference

同步分析，而不是分开做 approximation。

## Target B — Resonant / Nonresonant denominator-gcd split

用 Smith coordinates：

\[
(b_1,b_2,b_3)
=(s\alpha u,\ s\alpha\beta t,\ s\beta v)
\]

分：

\[
\widehat R=\alpha t10^{n_3}-v\ne0
\]

与：

\[
\widehat R=0.
\]

generic case 不再幻想 unit spacing 自动 closure，而应联立：

\[
\alpha\mid T_3,
\qquad
\beta^{\langle10\rangle}\mid D,
\qquad
\text{ASYM-4},
\qquad
\text{tail suffix congruence}.
\]

resonant case直接冻结：

\[
\alpha=t=1,
\quad
m_2=g,
\quad
b_3=b_210^{n_3},
\quad
g_2=10^{n_3}g_3,
\]

只研究剩余的：

\[
10^gH=b_2(P_2+P_3-Q_0)
\]

与：

\[
\beta^{\langle10\rangle}\mid D.
\]

这应比继续围绕 \(R\) 的普通 magnitude 更有希望。

---

# 45. Final Assessment

本轮没有达到：

\[
\boxed{A_1=\varnothing.}
\]

也没有达到 infinite escape extinction。

但取得了三个实质层级的推进：

### I. MB 被完全整数化

\[
\boxed{
\text{MB}
\Longrightarrow
(H,R,d_2,P_3)\text{ exact integer identity}
}
\]

而不是继续停留在 mantissa closeness。

### II. Actual decimal prefix / suffix 被精确恢复

\[
\boxed{
\text{plus: }
\operatorname{Pref}_{m_2}(\varepsilon)=b_2
}
\]

\[
\boxed{
\text{minus: }
\operatorname{Pref}_{g}(\varepsilon)
\text{ 与 }\operatorname{Pref}_{g}(\beta_2)
\text{ 至多差一个 borrow}
}
\]

\[
\boxed{
K_3\equiv b_2P_2\pmod{10^g}
}
\]

### III. Denominator gcd lattice 出现新的 exact arithmetic obstruction

\[
\boxed{
\alpha\mid(Q_0-P_3),
\qquad
\beta\mid10^{m_2+m_3}D,
}
\]

并有：

\[
\boxed{
\alpha^{\langle10\rangle},\beta^{\langle10\rangle}
\text{ 只含 }1\bmod4\text{ primes}.
}
\]

另外：

\[
\boxed{
g\ge1,\ \text{minus}\Longrightarrow d\ge0}
\]

把第五轮的 transition strip 从 \(\{-1,0,1\}\) 缩到真正双分支的 \(\{0,1\}\)。

所以本轮最终等级最准确地写成：

\[
\boxed{
\textbf{LEVEL 7 ACHIEVED — EXACT PREFIX / TAIL-BLOCK REDUCTION}
}
\]

并附带：

\[
\boxed{
\textbf{NEW SMITH-GCD ALLOCATION + ONE TRANSITION SLICE CLOSED.}
}
\]

A1 仍 OPEN；但 remaining frontier 已经不再是一个 real approximation 问题，而是一个非常具体的：

\[
\boxed{
\textbf{double Euclidean decimal synchronization}
\times
\textbf{asymmetric denominator-gcd arithmetic}
}
\]

问题。

---

# 46. Provenance / dependency notes

本报告实际核准并使用的主要前序文件：

1. `strict_layer_A1_moving_profile_coprime_integer_scale_campaign.md`
   - exact MB；
   - \(P_2\)-axis bounds；
   - \(d_2\)、\(P_3\) bounds；
   - fifth-round branch drift。
2. `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`
   - exact common-\(U\) reconstruction；
   - \(g_i=\gcd(V,P_i)\)；
   - \(b_i=V/g_i\)；
   - \(V=\operatorname{lcm}(b_1,b_2,b_3)\) / reducedness interface。
3. `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`
   - exact GSYNC；
   - \(\Delta_{12},\Delta_3\) definitions；
   - universal tail divisor；
   - synchronized pseudo-family used only for route falsification。
4. `strict_layer_A1_flat_locus_structural_elimination_campaign.md`
   - flat locus removed；
   - \(D>0\)；
   - primitive sphere parity / prior divisor facts。
5. `strict_layer_A1_moving_core_decimal_translation_global_campaign.md`
   - translation-line provenance。
6. `strict_layer_unified_exact_lift_campaign(1).md`
   - primitive-profile master equation and reconstruction dictionary。

本轮新增证明不依赖 DD-only closure machinery，也没有把旧 External Exact-Lift synthesis 中未独立审计的 closure claim 当 theorem 使用。

