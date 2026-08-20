# 105-R7C — Prescribed Source Divisor Gate × Primitive Determinant-Packet Compatibility

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R7C  
**Status:** **PSDG reduced to one arithmetic gate; neither universal EMPTY nor outer WITNESS proved**  
**R8 authorization:** **NO**

---

# 1. Executive Verdict

R7C 没有得到可以诚实签发的

\[
\texttt{PRESCRIBED\_SOURCE\_DIVISOR\_GATE\_EMPTY},
\]

也没有构造出 genuine outer S3/S4 PSDG witness。

但是，本轮完成了三次关键压缩，并纠正了 prompt 中一个会把研究带错方向的符号错误。

## 1.1 Coefficient-to-Norm Supply Lane 被严格 falsify

R7B 的正确 sphere-factor master 是

\[
\boxed{
-(\widehat B-\widehat A)x+(\widehat A+\widehat B)y=2\widehat C.
}
\]

令

\[
a=\widehat B-\widehat A,\qquad
b=\widehat A+\widehat B,\qquad
c=\widehat C,
\]

则正确式为

\[
\boxed{by-ax=2c,}
\tag{1.1}
\]

而不是 R7C prompt Task Y 中写出的

\[
aX+bY=2c/h.
\]

因此建议中的

\[
\frac a{\gcd(a,2c)}\mid N,
\qquad
\frac b{\gcd(b,2c)}\mid N
\]

**不是必要条件**。

一个 exact primitive sphere/master counterexample 为：

\[
(P_1,P_2,P_3,Q_0)=(2,14,5,15),
\]

\[
(\widehat A,\widehat B,c)=(1,6,3).
\]

于是

\[
N=14^2+5^2=221,
\]

\[
x=Q_0+P_1=17,\qquad
y=Q_0-P_1=13,
\]

\[
xy=221,
\]

\[
by-ax=7\cdot13-5\cdot17=6=2c.
\]

但

\[
\frac a{\gcd(a,2c)}=5\nmid221,
\qquad
\frac b{\gcd(b,2c)}=7\nmid221.
\]

所以：

\[
\boxed{
\texttt{COEFFICIENT\_TO\_NORM\_SUPPLY\_OBSTRUCTION
=FALSE\_AS\_PROPOSED}.
}
\]

正确的 replacement 是 **coefficient-anchor divisibility**：

\[
d_a:=\gcd(a,2c),\qquad d_b:=\gcd(b,2c),
\]

则由 (1.1)：

\[
\boxed{
\frac{d_a}{\gcd(d_a,b)}\mid y,
}
\tag{1.2}
\]

\[
\boxed{
\frac{d_b}{\gcd(d_b,a)}\mid x.
}
\tag{1.3}
\]

在 integer-lift survivor 上 \(\gcd(a,b)\le2\)，所以尤其：

\[
\boxed{
(d_a)_{\rm odd}\mid y,
\qquad
(d_b)_{\rm odd}\mid x.
}
\tag{1.4}
\]

也就是说，被 norm 供应的是 coefficient 与 additive anchor \(2c\) 的 **common part**，不是 prompt 所猜测的 external quotient。

---

## 1.2 Shared gcd 得到新的 source compression

令

\[
h=\gcd(P_1,Q_0),
\qquad
g_{23}:=\gcd(P_2,P_3),
\]

并写

\[
P_2=g_{23}u,\qquad
P_3=g_{23}v,\qquad
\gcd(u,v)=1.
\]

R7B 已有：

\[
h\mid c,\qquad h^2\mid N,
\qquad
h\text{ odd},
\]

且

\[
p\mid h\Longrightarrow p\equiv1\pmod4,
\qquad
\gcd(h,g_{23})=1.
\]

R7C 使用 raw source formula

\[
C_0=b_2YP_2+b_3P_3
\]

得到新的 theorem。置

\[
\alpha_c:=b_2Y,\qquad \beta_c:=b_3.
\]

因为

\[
C_0=g_{23}(\alpha_cu+\beta_cv),
\]

且 \(h\mid c=C_0/d_{\rm row}\)、\(\gcd(h,g_{23})=1\)，故

\[
h\mid \alpha_cu+\beta_cv.
\]

又 \(h^2\mid u^2+v^2\)。恒等式

\[
(\alpha_cu+\beta_cv)^2
+
(\beta_cu-\alpha_cv)^2
=
(\alpha_c^2+\beta_c^2)(u^2+v^2)
\]

逐素数推出：

\[
\boxed{
h\mid (b_2Y)^2+b_3^2.
}
\tag{1.5}
\]

因此 shared part 被压入：

\[
\boxed{
h\mid H_{\max},
}
\tag{1.6}
\]

其中可取 canonical profilewise bound

\[
\boxed{
H_{\max}
=
\gcd\!\left(
c,\,
(b_2Y)^2+b_3^2,\,
\operatorname{sqrootpart}_{1\bmod4}(u^2+v^2)
\right).
}
\tag{1.7}
\]

这里

\[
\operatorname{sqrootpart}_{1\bmod4}(m)
:=
\prod_{p\equiv1(4)}
p^{\lfloor v_p(m)/2\rfloor}.
\]

这是 **finite values for each fixed source profile**，但 \(H_{\max}\) 随 moving profile 变化，所以不是 uniform finite-values theorem。

进一步引入 frozen denominator Smith chart

\[
b_1=s\alpha\mathfrak u,\qquad
b_2=s\alpha\beta\mathfrak t,\qquad
b_3=s\beta\mathfrak v,
\]

以及

\[
\beta_0:=\beta^{\langle10\rangle},
\qquad
\gamma_0:=\gamma^{\langle10\rangle},
\]

则 frozen Smith allocation 给

\[
\beta\mid P_1,\qquad
\beta_0\mid Q_0,
\]

从而：

\[
\boxed{\beta_0\mid h.}
\tag{1.8}
\]

同时

\[
\alpha\mid P_3,Q_0,
\qquad
\gamma_0\mid P_2,Q_0.
\]

primitive sphere 因此给：

\[
\boxed{
\gcd(h,\alpha\gamma_0)=1.
}
\tag{1.9}
\]

综合：

\[
\boxed{
\beta_0
\mid h
\mid H_{\max},
\qquad
\gcd(h,\alpha\gamma_0g_{23})=1.
}
\tag{1.10}
\]

这是本轮对 shared gcd 最强的 source compression。

---

## 1.3 PSDG 被压成单一 Primitive Determinant-Packet Gate

设

\[
x=Q_0+P_1,\qquad y=Q_0-P_1.
\]

写

\[
x=hX,\qquad y=hY,
\qquad
\varepsilon:=\gcd(X,Y)\in\{1,2\},
\]

再写

\[
X=\varepsilon X_0,\qquad
Y=\varepsilon Y_0,
\qquad
\gcd(X_0,Y_0)=1.
\]

令

\[
g:=\gcd(a,b)\in\{1,2\},
\qquad
a=ga',\qquad b=gb',
\qquad
\gcd(a',b')=1.
\]

则 PSDG 的 reduced core 精确成为：

\[
\boxed{
X_0Y_0=M
:=
\frac{N}{h^2\varepsilon^2},
}
\tag{1.11}
\]

\[
\boxed{
b'Y_0-a'X_0
=
\Delta
:=
\frac{2c}{g\varepsilon h},
}
\tag{1.12}
\]

\[
\boxed{
\gcd(X_0,Y_0)=1.
}
\tag{1.13}
\]

这里 \(\Delta\in\mathbf Z_{>0}\) 是任何 PSDG survivor 的必要条件。

而 (1.12) 立即产生 determinant-packet coupling：

\[
\boxed{
\gcd(X_0,\Delta)=\gcd(X_0,b'),
}
\tag{1.14}
\]

\[
\boxed{
\gcd(Y_0,\Delta)=\gcd(Y_0,a').
}
\tag{1.15}
\]

所以：

\[
\boxed{
\gcd(M,\Delta)\mid a'b'.
}
\tag{1.16}
\]

更精确地，对每个 \(p^e\Vert M\)：

- 若整个 \(p^e\) packet 落入 \(X_0\)，则
  \[
  \min(v_p(\Delta),e)=\min(v_p(b'),e);
  \]
- 若整个 packet 落入 \(Y_0\)，则
  \[
  \min(v_p(\Delta),e)=\min(v_p(a'),e).
  \]

因为 \(\gcd(a',b')=1\)，任何

\[
p\mid\gcd(M,\Delta)
\]

若只进入 \(a'\) 或 \(b'\) 的一边，就会 **强制定向** 对应 packet；若

\[
p\mid\gcd(M,\Delta),
\qquad
p\nmid a'b',
\]

则 PSDG 立即不可能。

因此 R7C 的真正 terminal gate 是：

\[
\boxed{
\textbf{Primitive Determinant-Packet Compatibility}
}
\]

而不是 coefficient external-prime supply，也不是 generic near-square-root divisor spacing。

最终本轮只能诚实签发：

\[
\boxed{
\texttt{PSDG\_REDUCED\_TO\_SINGLE\_ARITHMETIC\_GATE}.
}
\]

---

# 2. Frozen R1–R7B State

以下全部冻结，不重新打开：

```text
R1 = COMMON_OBSTRUCTION_CERTIFIED
COMMON_OBSTRUCTION = SOURCE_AFFINE_SECTION_LOSS

R2 = SOURCE_SECTION_INTERNALIZATION_THEOREM_PROVED
J = DES_SATURATION_DECORATION

R3 = FINITE_SOURCE_COMPLETED_VALUATION_ATLAS_PROVED
VALUATION_ATLAS = SEMANTICALLY_SATURATED

R4 = S0/S1/S2 FIXED CHARACTER UNION
OUTER FAMILY = Z=10^d

R5 = FIXED SOURCE-COMPLETED BASE SUPPORTS AT MOST ONE Z

R5C = FIRST FULL-SOURCE FAILURE GATE
GATE = SPHERE x MASTER RATIONAL LIFT

R6 = CANONICAL COMPLEMENTARY DISCRIMINANT
RATIONAL LIFT IFF DISCRIMINANT SQUARE
GENERIC NONSQUARE NOT UNIVERSAL

R7 = COMPLEMENTARY FACTOR BRIDGE
R7B = POSITIVE ORIENTATION COLLAPSED
R7B = ONE PRESCRIBED PRIMITIVE-DIVISOR GATE
```

R7C 不重新研究：

- discriminant square-class；
- \(2/5\)-adic local cover；
- orientation；
- two independent divisibilities；
- arbitrary split-prime allocation；
- generic divisor spacing；
- valuation atlas；
- \(J\)-split。

---

# 3. PSDG Canonical Definition

primitive master row：

\[
\widehat A Q_0-\widehat B P_1=\widehat C,
\qquad
\gcd(\widehat A,\widehat B,\widehat C)=1.
\]

integer-lift survivor 必须先通过：

\[
\boxed{\gcd(\widehat A,\widehat B)=1.}
\tag{3.1}
\]

定义：

\[
a:=\widehat B-\widehat A>0,
\qquad
b:=\widehat A+\widehat B>0,
\qquad
c:=\widehat C>0,
\]

\[
N:=P_2^2+P_3^2.
\]

square locus：

\[
W^2=c^2+abN.
\]

唯一正 root：

\[
\boxed{
x_*=\frac{W-c}{a}
=
\frac{bN}{W+c}.
}
\tag{3.2}
\]

另一 factor：

\[
\boxed{
y_*=\frac{W+c}{b}
=
\frac N{x_*}.
}
\tag{3.3}
\]

PSDG 是：

\[
\boxed{
x_*
\stackrel{?}{\in}
\operatorname{Div}^{\rm src}_{\rm prim}(N;\mathbf s).
}
\]

其中 \(\mathbf s\) 表示完整 fixed source profile，而不只是 \((N,P_2,P_3)\)。

---

# 4. Exact \((a,b,c,N)\) Source Provenance

raw source master：

\[
A_0Q_0-B_0P_1=C_0
\]

具有：

\[
A_0=YG(b_1X+b_2)+b_3,
\]

\[
B_0=b_1XYGK,
\]

\[
C_0=b_2YP_2+b_3P_3.
\]

令：

\[
d_{\rm row}:=\gcd(A_0,B_0,C_0).
\]

于是：

\[
\widehat A=A_0/d_{\rm row},
\quad
\widehat B=B_0/d_{\rm row},
\quad
c=C_0/d_{\rm row}.
\]

所以：

\[
\boxed{
a=
\frac{
YG[b_1X(K-1)-b_2]-b_3
}{
d_{\rm row}
}.
}
\tag{4.1}
\]

\[
\boxed{
b=
\frac{
YG[b_1X(K+1)+b_2]+b_3
}{
d_{\rm row}
}.
}
\tag{4.2}
\]

\[
\boxed{
c=
\frac{
b_2YP_2+b_3P_3
}{
d_{\rm row}
}.
}
\tag{4.3}
\]

source dictionary：

\[
G=10^g,\qquad K=10^k,
\]

\[
X=10^{m_2}=10^{g+d},
\qquad
Y=10^{n_3},
\]

\[
g_i=\gcd(V,P_i)=V/b_i,
\qquad
C_i=P_i/g_i,
\]

\[
P_2=(V/b_2)C_2,
\qquad
P_3=(V/b_3)C_3.
\]

因此：

\[
\boxed{
N=
\left(\frac V{b_2}C_2\right)^2
+
\left(\frac V{b_3}C_3\right)^2.
}
\tag{4.4}
\]

而：

\[
C_0=V(YC_2+C_3).
\]

## Source provenance ledger

| quantity | exact source formula | positivity | gcd / primitive data | power-10 content | outer dependence |
|---|---|---:|---|---|---|
| \(a\) | (4.1) | YES | primitive row quotient | additive \(b_3\) destroys pure \(10\)-power content | \(G,K,X,Y\) |
| \(b\) | (4.2) | YES | primitive row quotient | additive \(b_3\) destroys pure \(10\)-power content | \(G,K,X,Y\) |
| \(c\) | (4.3) | YES | source affine anchor | mixed through \(P_2,P_3\) | \(Y\), primitive coordinates |
| \(N\) | (4.4) | YES | primitive sphere norm | no universal pure \(2/5\) content | \(V,b_2,b_3,C_2,C_3\) |

R7C 没有发现新的合法理由重新开启 \(2/5\)-valuation atlas。

---

# 5. Unique Positive Root Theorem

定义：

\[
F(x):=ax^2+2cx-bN.
\]

有：

\[
F(0)=-bN<0,
\]

且：

\[
F'(x)=2ax+2c>0
\qquad(x>0).
\]

所以：

\[
\boxed{
F\text{ 在 }(0,\infty)\text{ 上有唯一正根}.
}
\]

该根正是：

\[
\boxed{
x_*=
\frac{\sqrt{c^2+abN}-c}{a}.
}
\tag{5.1}
\]

因此 fixed source profile 上不存在“从多个 positive divisors 中让 master 自由挑一个”的 architecture。

---

# 6. Root Localization

令：

\[
t:=\frac{P_1}{Q_0},
\qquad
\rho:=\frac{\widehat A}{\widehat B}.
\]

master 给：

\[
\widehat A Q_0-\widehat B P_1=c,
\]

所以：

\[
\boxed{
t=\rho-\frac{c}{\widehat BQ_0}<\rho.
}
\tag{6.1}
\]

source formula：

\[
\boxed{
\rho
=
\frac1K
+
\frac{b_2}{b_1XK}
+
\frac{b_3}{b_1XYGK}.
}
\tag{6.2}
\]

因此：

\[
\boxed{
\frac1K
<
\rho
<
\frac{1+1/b_1}{K}
\le\frac2K.
}
\tag{6.3}
\]

在 genuine A1 lift 上 frozen leading-block sandwich 进一步给：

\[
\boxed{
\frac1K<t<
\frac{1+1/b_1}{K}.
}
\tag{6.4}
\]

结合 (6.1)：

\[
\boxed{
\frac1K<t<\rho<
\frac{1+1/b_1}{K}.
}
\tag{6.5}
\]

---

# 7. Normalized Root Annulus

因为：

\[
x=Q_0+P_1,
\qquad
y=Q_0-P_1,
\]

有：

\[
\frac xy=\frac{1+t}{1-t},
\]

以及：

\[
\boxed{
r_*:=\frac{x_*}{\sqrt N}
=
\sqrt{\frac{1+t}{1-t}}.
}
\tag{7.1}
\]

由 (6.5)：

\[
\boxed{
\sqrt{\frac{K+1}{K-1}}
<
r_*
<
\sqrt{\frac{1+\rho}{1-\rho}}.
}
\tag{7.2}
\]

但：

\[
\frac{1+\rho}{1-\rho}
=
\frac ba.
\]

所以得到比 R7B gross bound 更 sharp 的 **per-profile upper wall**：

\[
\boxed{
\sqrt{\frac{K+1}{K-1}}
<
\frac{x_*}{\sqrt N}
<
\sqrt{\frac ba}
<
\sqrt{
\frac{K+1+1/b_1}
     {K-1-1/b_1}
}.
}
\tag{7.3}
\]

等价地：

\[
\boxed{
\frac{K+1}{K-1}
<
\frac{x_*}{y_*}
<
\frac ba.
}
\tag{7.4}
\]

而且有 exact ratio defect：

\[
\boxed{
\frac ba-\frac{x_*}{y_*}
=
\frac{2c}{ay_*}>0.
}
\tag{7.5}
\]

这比“靠近 \(\sqrt N\)”更精确：PSDG factor ratio 必须严格逼近一个 source coefficient ratio \(b/a\)，但永远在其下方。

## 7.1 Sharp \(a/b\) source bounds

由 \(\rho\) bounds：

\[
\boxed{
\frac{K-1-1/b_1}{K+1+1/b_1}
<
\frac ab
<
\frac{K-1}{K+1}.
}
\tag{7.6}
\]

## 7.2 \(c/\sqrt N\) source defect

由：

\[
Q_0/\sqrt N=\frac1{\sqrt{1-t^2}},
\]

得到 exact：

\[
\boxed{
\frac c{\sqrt N}
=
\frac{\widehat A-\widehat Bt}
{\sqrt{1-t^2}}
=
\widehat B\frac{\rho-t}{\sqrt{1-t^2}}.
}
\tag{7.7}
\]

从 \(t>1/K\) 且该表达对当前 \(t\)-window 递减，可得：

\[
\boxed{
0<
\frac c{\sqrt N}
<
\frac{\widehat B(\rho-1/K)}
{\sqrt{1-K^{-2}}}.
}
\tag{7.8}
\]

这重写了 R7B 的粗界 \(c<\widehat A\sqrt N\) 为 source leading-defect bound。

---

# 8. Primitive Source Divisor Set Definition

必须区分两个层次。

## 8.1 Primitive sphere divisor set

令：

\[
g_{23}:=\gcd(P_2,P_3).
\]

对 \(x\mid N\)，令：

\[
y=N/x,
\]

\[
P_1(x)=\frac{x-y}{2},
\qquad
Q_0(x)=\frac{x+y}{2}.
\]

定义：

\[
h(x):=\gcd(P_1(x),Q_0(x)).
\]

则：

\[
\boxed{
\operatorname{Div}_{\rm sph,prim}(N;P_2,P_3)
}
\]

为所有满足：

\[
x>y>0,
\]

\[
x\equiv y\pmod2,
\]

\[
\gcd(h(x),g_{23})=1
\]

的正 divisor \(x\mid N\)。

这与 primitive sphere recovery 精确等价。

## 8.2 Source-profile refinement

“source divisor”不能只由 \((N,P_2,P_3)\) 决定，因为 frozen source data还包含

\[
V,\ b_1,\ U,\ \text{Smith/DES metadata}.
\]

至少必须加入 first gcd-profile firewall：

\[
\boxed{
\gcd(V,P_1(x))=g_1=V/b_1.
}
\tag{8.1}
\]

然后：

\[
C_1=P_1/g_1,
\qquad
\gcd(C_1,b_1)=1.
\]

R6 的 downstream hierarchy还要求：

\[
KP_1-Q_0>0,
\]

first numerator block \(UC_1\) 的 exact digit window，随后才是 DES/source fibre/digit/actual cut。

因此本报告把 PSDG 核心定义为：

\[
\boxed{
\operatorname{Div}^{\rm src}_{\rm prim}
=
\operatorname{Div}_{\rm sph,prim}
\cap
\{\text{source }g_1\text{-profile firewall}\},
}
\tag{8.2}
\]

而 Smith/DES/digit/actual-cut 保持为 post-PSDG downstream audit，避免把“PSDG witness”与“full original witness”混成一个概念。

---

# 9. Primitive Divisor Characterization

对 candidate divisor \(x\)：

\[
y=N/x.
\]

primitive integer-lift iff：

1. \(x,y\in\mathbf Z_{>0}\)；
2. \(x>y\)；
3. \(x\equiv y\pmod2\)；
4. \(\gcd(h(x),g_{23})=1\)；
5. source gcd profile (8.1)；
6. master residual为零：
   \[
   by-ax-2c=0.
   \]

由于 master positive root唯一，条件 6 一旦成立便自动有：

\[
x=x_*.
\]

因此：

\[
\boxed{
\text{PSDG}
\iff
\exists x\in\operatorname{Div}^{\rm src}_{\rm prim}(N)
:
by-ax=2c.
}
\tag{9.1}
\]

---

# 10. Shared-GCD \(h\) Extraction

若 PSDG 成立：

\[
h:=\gcd(P_1,Q_0).
\]

则：

\[
\boxed{h\mid c.}
\tag{10.1}
\]

因为：

\[
c=\widehat A Q_0-\widehat B P_1.
\]

又：

\[
N=Q_0^2-P_1^2,
\]

故：

\[
\boxed{h^2\mid N.}
\tag{10.2}
\]

并且：

\[
\boxed{
\gcd(x,y)
=
\begin{cases}
h,&x,y\text{ odd},\\
2h,&x,y\text{ even}.
\end{cases}
}
\tag{10.3}
\]

定义：

\[
x=hX,\qquad y=hY.
\]

则：

\[
\gcd(X,Y)\in\{1,2\}.
\]

---

# 11. \(h\)-Prime Support

primitive sphere 给：

\[
\boxed{h\text{ odd}.}
\tag{11.1}
\]

若 odd prime：

\[
p\equiv3\pmod4
\]

且 \(p\mid h\)，则 \(p\mid P_1,Q_0\)，所以：

\[
P_2^2+P_3^2\equiv0\pmod p.
\]

\(-1\) 非平方迫使 \(p\mid P_2,P_3\)，与 primitive quadruple矛盾。

故：

\[
\boxed{
p\mid h\Longrightarrow p\equiv1\pmod4.
}
\tag{11.2}
\]

同时：

\[
\boxed{\gcd(h,g_{23})=1.}
\tag{11.3}
\]

---

# 12. \(h\)-Source Compression

这一节是 R7C 新增的主要 theorem 之一。

写：

\[
P_2=g_{23}u,\qquad
P_3=g_{23}v,
\qquad
\gcd(u,v)=1.
\]

由于：

\[
N=g_{23}^2(u^2+v^2),
\]

且 \(\gcd(h,g_{23})=1\)，由 \(h^2\mid N\) 得：

\[
\boxed{h^2\mid u^2+v^2.}
\tag{12.1}
\]

另一方面：

\[
C_0=b_2YP_2+b_3P_3
=
g_{23}\left(b_2Yu+b_3v\right).
\]

由 \(h\mid c\) 可得 \(h\mid C_0\)，再由 \(\gcd(h,g_{23})=1\)：

\[
\boxed{
h\mid b_2Yu+b_3v.
}
\tag{12.2}
\]

令：

\[
L=b_2Yu+b_3v,
\qquad
M_c=b_3u-b_2Yv.
\]

恒等式：

\[
L^2+M_c^2
=
\left((b_2Y)^2+b_3^2\right)(u^2+v^2).
\]

对任意 \(p^t\mid h\)，(12.1) 给 \(p^{2t}\mid u^2+v^2\)，(12.2) 给 \(p^t\mid L\)，故 \(p^t\mid M_c\)。再使用：

\[
b_2Y L+b_3M_c
=
\left((b_2Y)^2+b_3^2\right)u,
\]

\[
b_3L-b_2YM_c
=
\left((b_2Y)^2+b_3^2\right)v,
\]

并利用 \(\gcd(u,v)=1\)，得到：

\[
\boxed{
p^t\mid (b_2Y)^2+b_3^2.
}
\]

故：

\[
\boxed{
h\mid (b_2Y)^2+b_3^2.
}
\tag{12.3}
\]

定义：

\[
\boxed{
H_{\max}
=
\gcd\!\left(
c,\,
(b_2Y)^2+b_3^2,\,
\operatorname{sqrootpart}_{1\bmod4}(u^2+v^2)
\right).
}
\tag{12.4}
\]

则：

\[
\boxed{h\mid H_{\max}.}
\tag{12.5}
\]

## 12.1 Smith lower anchor

frozen Smith chart 给：

\[
\beta_0:=\beta^{\langle10\rangle}\mid P_1,Q_0.
\]

所以：

\[
\boxed{\beta_0\mid h.}
\tag{12.6}
\]

同时：

\[
\alpha\mid P_3,Q_0,
\qquad
\gamma_0\mid P_2,Q_0.
\]

若某 \(p\mid h\cap\alpha\)，则 \(p\mid P_1,Q_0,P_3\)，sphere 强迫 \(p\mid P_2\)，破坏 primitive。故：

\[
\gcd(h,\alpha)=1.
\]

同理：

\[
\gcd(h,\gamma_0)=1.
\]

最终：

\[
\boxed{
\beta_0
\mid h
\mid H_{\max},
\qquad
\gcd(h,\alpha\gamma_0g_{23})=1.
}
\tag{12.7}
\]

这把 shared freedom压成 **profilewise finite canonical divisor interval**。

---

# 13. Reduced Coprime Factor Pair

写：

\[
x=hX,\qquad y=hY,
\]

\[
\varepsilon:=\gcd(X,Y)\in\{1,2\},
\]

\[
X=\varepsilon X_0,\qquad
Y=\varepsilon Y_0,
\qquad
\gcd(X_0,Y_0)=1.
\]

则：

\[
\boxed{
X_0Y_0
=
M
=
\frac{N}{h^2\varepsilon^2}.
}
\tag{13.1}
\]

令：

\[
g=\gcd(a,b)\in\{1,2\},
\]

\[
a=ga',
\qquad
b=gb',
\qquad
\gcd(a',b')=1.
\]

正确 reduced master：

\[
\boxed{
b'Y_0-a'X_0
=
\Delta
=
\frac{2c}{g\varepsilon h}.
}
\tag{13.2}
\]

注意：这与 prompt 中的 \(aX+bY=2c/h\) 符号不同。

---

# 14. Inert Packet Structure

写：

\[
N=g_{23}^2N_*,
\qquad
N_*=u^2+v^2,
\qquad
\gcd(u,v)=1.
\]

若：

\[
q\equiv3\pmod4,
\]

则：

\[
q\nmid N_*.
\]

因此 odd inert prime content全部来自：

\[
g_{23}^2.
\]

又：

\[
\gcd(h,g_{23})=1.
\]

所以所有 inert \(q^{2e}\) packet 均不能进入 shared \(h\)，而在 reduced coprime pair \((X_0,Y_0)\) 中必须 whole-side。

\[
\boxed{
\texttt{INERT\_PACKET\_STRUCTURE=WHOLE\_SIDE}.
}
\]

但 R7C 没有证明 source formulas 强制存在一个足够大的 inert packet，所以：

\[
\boxed{
\texttt{FORCED\_INERT\_PRIME=NO\_UNIVERSAL\_THEOREM}.
}
\]

---

# 15. Split Packet Structure

对：

\[
p\equiv1\pmod4,
\qquad
e=v_p(N),
\]

shared exponent：

\[
t_p=v_p(h)
\]

必须满足：

\[
0\le t_p\le\lfloor e/2\rfloor,
\]

以及 source restrictions：

\[
t_p\le v_p(H_{\max}).
\]

R7C 更强地有 Smith lower/avoidance：

\[
v_p(\beta_0)\le t_p,
\]

而：

\[
p\mid\alpha\gamma_0g_{23}
\Longrightarrow
t_p=0.
\]

除去 \(2t_p\) 后，剩余 exponent：

\[
e-2t_p
\]

因为 \(\gcd(X_0,Y_0)=1\)，必须 whole-side。

所以 split-prime freedom不再是任意 sharing，而是：

\[
\boxed{
\text{finite }h\text{-choice}
+
\text{whole-packet side assignment}.
}
\]

full master再通过 determinant equation把 side assignment压成至多一个 survivor。

---

# 16. Near-Balanced Primitive Divisor Gate

PSDG 要求：

\[
\boxed{
\frac{K+1}{K-1}
<
\frac{x}{y}
<
\frac ba.
}
\tag{16.1}
\]

但 **primitive sphere 本身并不禁止 arbitrarily near-balanced divisors**。

对任意 \(n\ge1\)，令：

\[
\boxed{
(P_1,P_2,P_3,Q_0)
=
(2n,\,2n^2,\,1,\,2n^2+1).
}
\tag{16.2}
\]

则：

\[
(2n)^2+(2n^2)^2+1
=
(2n^2+1)^2,
\]

且因 \(P_3=1\)：

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

sphere factors：

\[
x=2n^2+2n+1,
\]

\[
y=2n^2-2n+1,
\]

\[
xy=4n^4+1=N.
\]

且：

\[
\frac xy\to1.
\]

所以：

\[
\boxed{
\texttt{GENERIC\_PRIMITIVE\_NEAR\_BALANCED\_DIVISOR\_OBSTRUCTION=FALSE}.
}
\tag{16.3}
\]

更进一步，取：

\[
n=K-1,
\qquad
K=10^k,
\]

则：

\[
\frac{P_1}{Q_0}
=
\frac{2(K-1)}{2(K-1)^2+1},
\]

对 \(K\ge10\) 有：

\[
\frac1K
<
\frac{P_1}{Q_0}
<
\frac2K.
\]

因此粗 A1 angular band 也不足以单独 kill。

结论：

\[
\boxed{
\text{near-balanced gate 必须使用 source determinant/Smith incidence，}
}
\]

不能只用 primitive sphere 或 divisor spacing。

---

# 17. \(\gcd(a,2c)\) Audit

定义：

\[
d_a:=\gcd(a,2c).
\]

由：

\[
by=ax+2c,
\]

有：

\[
d_a\mid by.
\]

故：

\[
\boxed{
\frac{d_a}{\gcd(d_a,b)}\mid y.
}
\tag{17.1}
\]

因为：

\[
\gcd(a,b)\le2,
\]

所以：

\[
\boxed{
(d_a)_{\rm odd}\mid y.
}
\tag{17.2}
\]

但 frozen source data没有证明：

\[
d_a
\]

是 fixed small、fixed support 或 power-of-ten type。

状态：

```text
GCD_A_2C = PROFILE_DEPENDENT
NEW_UNIFORM_BOUND = NO
CORRECT_USE = ANCHOR_PART_FORCES_Y_DIVISIBILITY
```

---

# 18. \(\gcd(b,2c)\) Audit

定义：

\[
d_b:=\gcd(b,2c).
\]

由：

\[
ax=by-2c,
\]

有：

\[
d_b\mid ax.
\]

故：

\[
\boxed{
\frac{d_b}{\gcd(d_b,a)}\mid x.
}
\tag{18.1}
\]

在 \(\gcd(a,b)\le2\) 下：

\[
\boxed{
(d_b)_{\rm odd}\mid x.
}
\tag{18.2}
\]

同样没有得到 uniform fixed support theorem。

---

# 19. Coefficient-to-Norm Supply Lemma — Falsified and Replaced

prompt 提议：

\[
a_{\rm ext}:=\frac a{\gcd(a,2c)},
\]

\[
b_{\rm ext}:=\frac b{\gcd(b,2c)}.
\]

并希望证明：

\[
a_{\rm ext}\mid N,
\qquad
b_{\rm ext}\mid N.
\]

该命题是 false。

## Exact counterexample

\[
(P_1,P_2,P_3,Q_0)=(2,14,5,15),
\]

\[
(\widehat A,\widehat B,c)=(1,6,3).
\]

则：

\[
a=5,\quad b=7,\quad N=221,
\]

\[
x=17,\quad y=13,
\]

\[
by-ax=6.
\]

但：

\[
a_{\rm ext}=5\nmid221,
\]

\[
b_{\rm ext}=7\nmid221.
\]

所以：

\[
\boxed{
\texttt{A\_EXTERNAL\_DIVIDES\_N=FALSE\_AS\_NECESSARY\_CONDITION},
}
\]

\[
\boxed{
\texttt{B\_EXTERNAL\_DIVIDES\_N=FALSE\_AS\_NECESSARY\_CONDITION}.
}
\]

正确 replacement 是 (17.1)/(18.1)。

---

# 20. Forced Inert-Prime Search

原 Lane A 希望从 \(a_{\rm ext}\) 或 \(b_{\rm ext}\) 找到 forced \(3\bmod4\) prime 并强迫其进入 \(N\)。

由于 external supply theorem已 false，该路线不能成立。

R7C 允许保留的 inert-prime killer只有两种：

1. 某个 source theorem直接强制
   \[
   q^{2e}\mid M
   \]
   且 packet side 与 determinant equation冲突；
2. 某个
   \[
   q\mid\gcd(M,\Delta)
   \]
   但
   \[
   q\nmid a'b',
   \]
   由 determinant-packet lemma直接 kill。

当前没有证明 source family universally触发这两种情况。

因此：

\[
\boxed{
\texttt{FORCED\_INERT\_PRIME=NO}.
}
\]

---

# 21. Source Norm Supply Audit — Determinant-Packet Coupling

这是 R7C 对“prime supply”真正有效的替代。

由：

\[
b'Y_0-a'X_0=\Delta,
\qquad
\gcd(X_0,Y_0)=1,
\]

模 \(X_0\)：

\[
\Delta\equiv b'Y_0\pmod{X_0}.
\]

因为 \(Y_0\) 是模 \(X_0\) unit：

\[
\boxed{
\gcd(X_0,\Delta)=\gcd(X_0,b').
}
\]

同理：

\[
\boxed{
\gcd(Y_0,\Delta)=\gcd(Y_0,a').
}
\]

所以：

\[
\boxed{
\gcd(M,\Delta)\mid a'b'.
}
\]

## Packet forcing rule

对 \(p^e\Vert M\)：

### 若 \(p^e\mid X_0\)

\[
\min(v_p(\Delta),e)=\min(v_p(b'),e).
\]

### 若 \(p^e\mid Y_0\)

\[
\min(v_p(\Delta),e)=\min(v_p(a'),e).
\]

因此：

- \(p\mid\Delta\cap M\), \(p\mid b'\), \(p\nmid a'\) 时，packet只能进 \(X_0\)；
- \(p\mid\Delta\cap M\), \(p\mid a'\), \(p\nmid b'\) 时，packet只能进 \(Y_0\)；
- \(p\mid\Delta\cap M\), \(p\nmid a'b'\) 时，立即 impossible。

这才是 R7C 的 canonical prime-packet membership bridge。

---

# 22. Primitive Sphere Parametrization

在 \(x,y\) 均偶的 parity branch，可以使用 Euler/Gaussian 参数：

\[
P_1=r^2+s^2-t^2-u^2,
\]

\[
P_2=2(rt+su),
\]

\[
P_3=2(ru-st),
\]

\[
Q_0=r^2+s^2+t^2+u^2.
\]

则：

\[
\boxed{
Q_0+P_1=2(r^2+s^2),
}
\]

\[
\boxed{
Q_0-P_1=2(t^2+u^2).
}
\]

所以 sphere factor pair确实天然是两个 quadratic norms。

odd \(x,y\) branch 经唯一 \(2\)-adic normalization后有同样的 Gaussian factor interpretation。

但是：当前 source \(P_2,P_3\) 不是任意参数点；把 source provenance投回参数空间后，尚未得到比 determinant-packet gate更强的新 congruence 或 gcd theorem。

因此 mid-round checkpoint 选择：

\[
\boxed{
\textbf{Route D — divisor/determinant arithmetic}
}
\]

而不切换到 standalone parameter route。

---

# 23. PSDG in Parametric Coordinates

在 even-factor branch：

\[
x=2(r^2+s^2),
\qquad
y=2(t^2+u^2).
\]

master：

\[
by-ax=2c
\]

变成：

\[
\boxed{
b(t^2+u^2)
-
a(r^2+s^2)
=
c.
}
\tag{23.1}
\]

并且：

\[
N=4(r^2+s^2)(t^2+u^2).
\]

这确实是 binary norm intersection。

但 source \(P_2+iP_3\) 同时要求：

\[
P_2+iP_3
=
2(r+is)(t-iu)
\]

up to units/conjugation。

因此 parameter route只是 determinant packet assignment 的 Gaussian-coordinate presentation，没有产生新的 independent killer。

状态：

\[
\boxed{
\texttt{PRIMITIVE\_SPHERE\_PARAMETRIZATION\_USED=YES\_AUDIT\_ONLY}.
}
\]

---

# 24. Reverse PSDG Witness Construction

对 fixed genuine source profile，正确 reverse search 应为：

1. 计算：
   \[
   a,b,c,N;
   \]
2. 计算 source-bounded shared classes：
   \[
   \beta_0\mid h\mid H_{\max},
   \quad
   \gcd(h,\alpha\gamma_0g_{23})=1;
   \]
3. 根据 \(v_2(N)\) 确定 \(\varepsilon\)；
4. 计算：
   \[
   M=N/(h^2\varepsilon^2);
   \]
5. 仅枚举 **coprime packet divisors**：
   \[
   X_0Y_0=M;
   \]
6. 检查：
   \[
   b'Y_0-a'X_0=\Delta;
   \]
7. 恢复：
   \[
   x=h\varepsilon X_0,
   \quad
   y=h\varepsilon Y_0;
   \]
8. 恢复：
   \[
   P_1=\frac{x-y}{2},
   \quad
   Q_0=\frac{x+y}{2};
   \]
9. 检查：
   \[
   \gcd(V,P_1)=V/b_1;
   \]
10. 再进入 Smith/DES/digit/source fibre。

本轮没有得到 genuine outer profile使上述流程走到第 9 步。

---

# 25. Master Residual Search

对任意 divisor \(d\mid N\)，令：

\[
e=N/d.
\]

定义正确 residual：

\[
\boxed{
R_{\rm PSDG}(d)
=
be-ad-2c.
}
\tag{25.1}
\]

则：

\[
\boxed{
R_{\rm PSDG}(d)=0
\iff
d=x_*.
}
\]

由于原 quadratic \(F(x)\) 对 \(x>0\) 单调，positive zero仍唯一。

在 shared-gcd normalization后：

\[
R_{\rm red}(X_0)
=
b'\frac M{X_0}-a'X_0-\Delta.
\]

所以：

\[
\boxed{
\text{PSDG}
\iff
\exists X_0\mid M,\ \gcd(X_0,M/X_0)=1:
R_{\rm red}(X_0)=0
}
\tag{25.2}
\]

再通过 source gcd-profile firewall。

这是本轮建议以后机器搜索唯一应使用的 residual。

---

# 26. Exact Witness Audit

## 26.1 Genuine outer PSDG witness

\[
\boxed{\texttt{NOT\_FOUND}.}
\]

因此不能填写：

```text
WITNESS_X
WITNESS_Y
WITNESS_P1
WITNESS_Q0
```

为 genuine outer data。

## 26.2 Frozen fixed-character regression

R7B 有 exact regression：

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),
\]

\[
(\widehat A,\widehat B,\widehat C)=(21,125,549),
\]

\[
x=193,\qquad y=145.
\]

它验证 PSDG algebra，但属于 \(g=0\) fixed-character region，不是 outer witness。

## 26.3 Coefficient-supply falsifier

本轮：

\[
(2,14,5,15),
\quad
(\widehat A,\widehat B,c)=(1,6,3)
\]

仅用于 falsify Lane A；不声称为 source profile。

## 26.4 Near-balanced infinite family

\[
(2n,2n^2,1,2n^2+1)
\]

仅用于 falsify generic near-balanced obstruction；不声称为 full source witness。

---

# 27. Primitive Lift Audit

若 determinant gate产生 candidate：

\[
P_1=\frac{x-y}{2},
\qquad
Q_0=\frac{x+y}{2},
\]

primitive iff：

\[
\boxed{
\gcd(h,g_{23})=1.
}
\]

R7C 已把该条件编码进 h-class：

\[
\gcd(h,\alpha\gamma_0g_{23})=1.
\]

但由于没有 genuine outer determinant survivor，本轮：

```text
PRIMITIVE_LIFT = NOT_REACHED_FOR_OUTER_WITNESS
```

---

# 28. Smith / DES Audit

R7C 对 Smith 的新增使用仅限于 shared-gcd compression：

\[
\beta_0\mid h,
\]

\[
\gcd(h,\alpha\gamma_0)=1.
\]

并冻结 source gcd profile：

\[
g_1=\gcd(V,P_1)=V/b_1.
\]

没有 outer PSDG witness，因此：

```text
SMITH_LIFT = NOT_REACHED
DES_LIFT = NOT_REACHED
```

不能伪造 post-PSDG completion。

---

# 29. Source Fibre / Digit / Actual-Cut Audit

没有 outer integer/primitive witness，所以：

```text
SOURCE_FIBRE_LIFT = NOT_REACHED
DIGIT_LIFT = NOT_REACHED
ACTUAL_CUT_LIFT = NOT_REACHED
OUTER_LIFT = NOT_REACHED
```

本轮 source provenance真实用于：

- \(a,b,c,N\) exact formulas；
- \(\rho\) root localization；
- \(h\mid(b_2Y)^2+b_3^2\)；
- Smith lower/avoidance；
- \(g_1\)-profile firewall。

因此 R7C 不是 ambient divisor theory，但也没有冒充完成 downstream source replay。

---

# 30. New First-Failure Gate

R7B 的 gate：

\[
x_*\in\operatorname{Div}^{\rm src}_{\rm prim}(N)
\]

在 R7C 后可重写为一个单一 arithmetic object：

\[
\boxed{
\texttt{PRIMITIVE\_DETERMINANT\_PACKET\_COMPATIBILITY
\_WITH\_SOURCE\_GCD\_FIREWALL}.
}
\]

其 exact data 为：

\[
\boxed{
\beta_0\mid h\mid H_{\max},
\qquad
\gcd(h,\alpha\gamma_0g_{23})=1,
}
\]

\[
\boxed{
M=N/(h^2\varepsilon^2),
}
\]

\[
\boxed{
X_0Y_0=M,
\qquad
\gcd(X_0,Y_0)=1,
}
\]

\[
\boxed{
b'Y_0-a'X_0=\Delta,
}
\]

\[
\boxed{
\gcd(V,P_1)=V/b_1.
}
\]

所有 orientation、square-class、two-divisibility、arbitrary allocation freedom均已退出。

---

# 31. Failed / Falsified Routes

R7C 正式退休：

1. **Wrong-sign reduced master**
   \[
   aX+bY=2c/h
   \]
   — FALSE; correct sign is \(bY-aX=2c/h\).

2. **Weighted AM-GM on the wrong positive sum** — INAPPLICABLE.

3. **Coefficient external supply**
   \[
   a/\gcd(a,2c)\mid N,\quad
   b/\gcd(b,2c)\mid N
   \]
   — FALSE.

4. **Forced inert prime from \(a_{\rm ext},b_{\rm ext}\)** — architecture invalid after 3.

5. **Generic primitive near-balanced divisor obstruction** — FALSE by infinite family (16.2).

6. **Generic divisor spacing** — still insufficient.

7. **Sphere angular band alone** — insufficient; family with \(n=K-1\) enters gross A1 band.

8. **Primitive sphere parametrization as standalone killer** — no gain over determinant packet gate.

9. **Arbitrary split-prime allocation** — already retired; after h extraction all remaining odd packets are whole-side, and master fixes at most one assignment.

10. **Baker/log packet imbalance as next step** — not justified; prime set remains moving and determinant congruence is more exact.

---

# 32. Exact Remaining Unknowns and Shock Checkpoint

## Q1 — \(\operatorname{Div}^{\rm src}_{\rm prim}(N)\) 到底是什么？

**Answer:** primitive sphere part已 exact：

\[
x\mid N,\quad x>y,\quad x\equiv y\pmod2,\quad
\gcd(h(x),g_{23})=1.
\]

source refinement至少加入：

\[
\gcd(V,P_1(x))=V/b_1.
\]

R7C further compresses h by (12.7).

## Q2 — root annulus多窄？

**Answer:** exact per-profile：

\[
\sqrt{\frac{K+1}{K-1}}
<
x/\sqrt N
<
\sqrt{b/a}.
\]

并有 source \(b_1\)-upper wall (7.3)。

## Q3 — \(h\) 是否被 source data有效控制？

**Answer:** **YES, profilewise strongly**：

\[
\beta_0\mid h\mid H_{\max},
\qquad
\gcd(h,\alpha\gamma_0g_{23})=1.
\]

但没有 uniform finite-values theorem。

## Q4 — coefficient-to-norm supply theorem？

**Answer:** **NO; proposed theorem is false.**  
正确 replacement 是 anchor common-part divisibility (17.1)/(18.1)。

## Q5 — source norm能否供应 external coefficients？

问题本身在 falsification 后退休。真正的 supply audit是 determinant-packet coupling (21)。

## Q6 — near-balanced primitive divisors仍可无限存在吗？

**YES.**

\[
(2n,2n^2,1,2n^2+1)
\]

给出 infinite primitive near-balanced family。

## Q7 — sphere parametrization更强吗？

**NO.** 当前 source data下它与 divisor/Gaussian factorization同信息级，Route D 更强。

## Q8 — PSDG witness？

**NO genuine outer witness found.**

## Q9 — 没有 witness 时，第一个 failure 在哪里？

目前不能说 integrality universally失败；最小 unresolved gate 是：

\[
\boxed{
\text{primitive determinant-packet compatibility + source }g_1\text{ firewall}.
}
\]

## Q10 — 足以授权 R8 吗？

**NO.**

---

# 33. R7C Terminal Verdict

本轮不能诚实选择 `EMPTY`：

\[
\texttt{PSDG\_EMPTY\_THEOREM=NOT\_PROVED}.
\]

也不能选择 genuine `WITNESS`：

\[
\texttt{PSDG\_WITNESS\_FOUND=NO}.
\]

但题设第 65/71 节允许 single arithmetic gate partial success，因此严格 verdict 为：

\[
\boxed{
\texttt{R7C\_TERMINAL\_VERDICT
=
PSDG\_REDUCED\_TO\_SINGLE\_ARITHMETIC\_GATE}.
}
\]

该 gate：

\[
\boxed{
\textbf{Primitive Determinant-Packet Compatibility}
\times
\textbf{Source }g_1\textbf{ Firewall}.
}
\]

这里“\(\times\)”不是两个 research architectures，而是同一个 candidate divisor 的 arithmetic membership predicate：determinant equation决定 factor packet，\(g_1\) 只验 source provenance。

---

# 34. R8 Authorization Decision

R8 Route A requires：

\[
\texttt{PSDG\_EMPTY\_THEOREM=PROVED}.
\]

没有。

Route B/C requires genuine PSDG witness。

没有。

因此：

\[
\boxed{
\texttt{R8\_AUTHORIZED=NO}.
}
\]

下一轮仍应是 R7 continuation，只攻击：

\[
\boxed{
\texttt{PRIMITIVE\_DETERMINANT\_PACKET\_COMPATIBILITY
\_WITH\_SOURCE\_GCD\_FIREWALL}.
}
\]

不得 broad R8。

---

# Machine-readable Terminal Block

```text
R7C_TERMINAL_VERDICT=PSDG_REDUCED_TO_SINGLE_ARITHMETIC_GATE__NO_OUTER_WITNESS__R8_NOT_AUTHORIZED

R1_R2_R3_R4_R5_R5C_R6_R7_R7B_STATE_FROZEN=YES

PSDG=X_STAR_IN_PRIMITIVE_SOURCE_DIVISOR_SET_WITH_MASTER_RESIDUAL_ZERO
PSDG_STATUS=OPEN_SINGLE_GATE

A=(B0-A0)/d_row=[YG*(b1*X*(K-1)-b2)-b3]/d_row
B=(B0+A0)/d_row=[YG*(b1*X*(K+1)+b2)+b3]/d_row
C=C0/d_row=[b2*Y*P2+b3*P3]/d_row
N=P2^2+P3^2

A_POSITIVE=YES
B_POSITIVE=YES
C_POSITIVE=YES

UNIQUE_POSITIVE_ROOT=YES
ROOT_FORMULA=(sqrt(C^2+A*B*N)-C)/A
ROOT_NORMALIZED_RATIO=sqrt((1+P1/Q0)/(1-P1/Q0))
ROOT_LOWER_BOUND=sqrt((K+1)/(K-1))
ROOT_UPPER_BOUND=sqrt(B/A)_STRICT; ALSO < sqrt((K+1+1/b1)/(K-1-1/b1))

SOURCE_PRIMITIVE_DIVISOR_SET=DIV_SPH_PRIM_INTERSECT_SOURCE_G1_PROFILE_FIREWALL
SOURCE_DIVISOR_CHARACTERIZATION=x|N; y=N/x; x>y; x==y(mod2); gcd(h(x),gcd(P2,P3))=1; gcd(V,P1(x))=V/b1

X_STAR_INTEGER=OPEN
X_STAR_DIVIDES_N=OPEN
Y_STAR=N/X_STAR
PARITY_COMPATIBLE=OPEN

P1_RECOVERED=(X_STAR-Y_STAR)/2_IF_GATE_PASSES
Q0_RECOVERED=(X_STAR+Y_STAR)/2_IF_GATE_PASSES

SHARED_GCD_H=gcd(P1,Q0)
H_DIVIDES_C=PROVED
H_SQUARE_DIVIDES_N=PROVED
H_PRIME_SUPPORT=ODD_SPLIT_PRIMES_ONLY
H_SOURCE_COMPRESSION=BETA0|H|H_MAX_AND_gcd(H,ALPHA*GAMMA0*g23)=1
H_MAX=gcd(C,(b2*Y)^2+b3^2,sqrootpart_1mod4((P2/g23)^2+(P3/g23)^2))

REDUCED_X=X_STAR/(H*EPSILON)
REDUCED_Y=Y_STAR/(H*EPSILON)
GCD_REDUCED_XY=1
EPSILON=gcd(X_STAR/H,Y_STAR/H)_IN_{1,2}

INERT_PACKET_STRUCTURE=WHOLE_SIDE_AFTER_H_EXTRACTION
SPLIT_PACKET_STRUCTURE=SHARED_EXPONENT_IN_H_THEN_ALL_RESIDUAL_ODD_PACKETS_WHOLE_SIDE
NEAR_BALANCED_DIVISOR_GATE=NOT_EMPTY_GENERALLY__MUST_USE_SOURCE_DETERMINANT_INCIDENCE

GCD_A_2C=gcd(A,2*C)_PROFILE_DEPENDENT
GCD_B_2C=gcd(B,2*C)_PROFILE_DEPENDENT
A_EXTERNAL=A/gcd(A,2*C)
B_EXTERNAL=B/gcd(B,2*C)

COEFFICIENT_TO_NORM_DIVISIBILITY=FALSE_AS_PROPOSED__REPLACED_BY_ANCHOR_COMMON_PART_DIVISIBILITY
A_EXTERNAL_DIVIDES_N=NO_NOT_NECESSARY
B_EXTERNAL_DIVIDES_N=NO_NOT_NECESSARY
FORCED_INERT_PRIME=NO_UNIVERSAL
COEFFICIENT_NORM_SUPPLY_STATUS=PROPOSED_LANE_A_FALSIFIED

CORRECT_A_ANCHOR_DIVISOR=gcd(A,2*C)/gcd(gcd(A,2*C),B)_DIVIDES_Y
CORRECT_B_ANCHOR_DIVISOR=gcd(B,2*C)/gcd(gcd(B,2*C),A)_DIVIDES_X

PRIMITIVE_SPHERE_PARAMETRIZATION_USED=YES_AUDIT_ONLY
PARAMETRIC_PSDG_FORM=X0*Y0=M; Bprime*Y0-Aprime*X0=DELTA; gcd(X0,Y0)=1

DETERMINANT_PACKET_LEMMA=gcd(X0,DELTA)=gcd(X0,Bprime); gcd(Y0,DELTA)=gcd(Y0,Aprime); gcd(M,DELTA)|Aprime*Bprime

PSDG_WITNESS_FOUND=NO_GENUINE_OUTER
WITNESS_X=
WITNESS_Y=
WITNESS_P1=
WITNESS_Q0=

SPHERE_VALID=NOT_REACHED_FOR_GENUINE_OUTER_WITNESS
MASTER_VALID=NOT_REACHED_FOR_GENUINE_OUTER_WITNESS
PRIMITIVE_LIFT=NOT_REACHED
SMITH_LIFT=NOT_REACHED
DES_LIFT=NOT_REACHED
SOURCE_FIBRE_LIFT=NOT_REACHED
DIGIT_LIFT=NOT_REACHED
ACTUAL_CUT_LIFT=NOT_REACHED
OUTER_LIFT=NOT_REACHED

NEW_FIRST_FAILURE_GATE=PRIMITIVE_DETERMINANT_PACKET_COMPATIBILITY_WITH_SOURCE_G1_FIREWALL

PSDG_EMPTY_THEOREM=NOT_PROVED
PSDG_SINGLE_REMAINING_GATE=YES

RETIRED_AFTER_R7C=WRONG_SIGN_SUM_FORM;WEIGHTED_AMGM_ON_WRONG_FORM;COEFFICIENT_EXTERNAL_SUPPLY;FORCED_INERT_FROM_EXTERNAL_COEFFICIENT;GENERIC_NEAR_BALANCED_DIVISOR_OBSTRUCTION;SPHERE_PARAMETRIZATION_AS_STANDALONE_KILLER;GENERIC_DIVISOR_SPACING

R8_AUTHORIZED=NO
R8_ARCHITECTURE=NOT_AUTHORIZED
R8_SINGLE_ATTACK_TARGET=NONE_UNTIL_SINGLE_GATE_IS_RESOLVED; NEXT_ROUND_STAYS_R7_CONTINUATION
```
