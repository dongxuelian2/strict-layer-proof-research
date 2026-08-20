# 105-R7B — Oriented Root Divisibility × Split-Prime Source Allocation × Integer-Lift Gate

**Scope:** 三项十进制拼接平方和问题 — Strict Layer — \(A_1\)-only  
**Round:** 105-R7B  
**Status:** **NOT KILLED / NOT CONSTRUCTED; REDUCED TO A SINGLE PRESCRIBED PRIMITIVE-DIVISOR GATE**  
**R8 authorization:** **NO**

---

# 1. Executive Verdict

R7B 没有得到 universal Kill，也没有构造出 S3/S4 source-legal integer lift。因此不能签发

\[
\texttt{ORIENTED\_INTEGER\_LIFT\_OBSTRUCTION\_PROVED}
\]

或

\[
\texttt{SPHERE\_MASTER\_INTEGRAL\_LIFT\_EVASION\_PROVED}.
\]

但是，本轮把 R7 留下的“两个 oriented divisibility + split-prime allocation”进一步严格压缩成了一个单一 arithmetic membership gate。

令 primitive master row 为

\[
\widehat A Q_0-\widehat B P_1=\widehat C,
\qquad
\gcd(\widehat A,\widehat B,\widehat C)=1,
\]

并令

\[
\mathcal N=P_2^2+P_3^2,
\qquad
\widehat W^2=\widehat C^2+(\widehat B^2-\widehat A^2)\mathcal N.
\]

本轮新的 source-specific coefficient theorem 给出

\[
\boxed{\widehat B>\widehat A>0}
\]

而且更强地

\[
\boxed{
\frac1K
<
\frac{\widehat A}{\widehat B}
<
\frac{1+1/b_1}{K}
\le \frac2K
\le \frac15.
}
\tag{1.1}
\]

同时

\[
\boxed{\widehat C<\widehat A\sqrt{\mathcal N}.}
\tag{1.2}
\]

故 square locus 上：

\[
\widehat W>\widehat C>0,
\]

两种 formal orientation 中只有

\[
\boxed{\delta=+1}
\]

能产生正的 \(S_\pm\)。因此 orientation 已完全塌缩。

定义

\[
a:=\widehat B-\widehat A>0,\qquad
b:=\widehat A+\widehat B>0,\qquad
c:=\widehat C,
\]

以及唯一正 real root quotient

\[
\boxed{
x_W:=\frac{\widehat W-c}{a}.
}
\tag{1.3}
\]

则

\[
S_+=x_W,
\qquad
S_-=\frac{\mathcal N}{x_W}
\]

在 rational sense 中恒成立；而 positive primitive integer lift 的 exact criterion 为：

\[
\boxed{
\begin{gathered}
\gcd(\widehat A,\widehat B)=1,\\
x_W\in\mathbf Z_{>0},\\
x_W\mid\mathcal N,\\
x_W\equiv \mathcal N/x_W\pmod2,\\
\gcd\!\left(
\gcd\!\left(\frac{x_W-\mathcal N/x_W}{2},
           \frac{x_W+\mathcal N/x_W}{2}\right),
\gcd(P_2,P_3)
\right)=1.
\end{gathered}}
\tag{1.4}
\]

换言之：

\[
\boxed{
\text{positive primitive integer lift}
\iff
x_W\in\operatorname{Div}^{\rm src}_{\rm prim}(\mathcal N).
}
\tag{1.5}
\]

等价的 \(W\)-free normal form 是：

\[
\boxed{
a x^2+2cx-b\mathcal N=0,
\qquad
x\in\operatorname{Div}^{\rm src}_{\rm prim}(\mathcal N).
}
\tag{1.6}
\]

由于左边对 \(x>0\) 严格递增，

\[
2ax+2c>0,
\]

full additive master 对每个 fixed source profile **至多选择一个** positive divisor。于是原来设想的 exponentially-many split-prime allocation freedom 在 full master 下不存在：prime packets 只是在检查唯一 \(x_W\) 是否属于 primitive divisor set 时出现。

因此本轮唯一未闭合对象被命名为：

\[
\boxed{
\texttt{PSDG}
=
\textbf{Prescribed Source Divisor Gate}.
}
\]

本轮达到：

\[
\boxed{
\texttt{ORIENTED\_LIFT\_REDUCED\_TO\_SINGLE\_PRESCRIBED\_DIVISOR\_GATE}.
}
\]

但没有证明 PSDG 永不成立，也没有找到 S3/S4 witness。因此：

\[
\boxed{\texttt{R8\_AUTHORIZED=NO}.}
\]

---

# 2. Frozen R1–R7 State

以下 architecture 全部冻结：

- R1: `COMMON_OBSTRUCTION_CERTIFIED = SOURCE_AFFINE_SECTION_LOSS`;
- R2: `SOURCE_SECTION_INTERNALIZATION_THEOREM_PROVED`;
- R3: `FINITE_SOURCE_COMPLETED_VALUATION_ATLAS_PROVED`;
- R4: S0/S1/S2 fixed proper character union；outer \(Z=10^d\) remains;
- R5: fixed base supports at most one \(Z\); unbounded depth requires moving base;
- R5C: first full-source failure gate isolated as sphere × master rational lift;
- R6: canonical complementary discriminant \(\mathscr D\); rational lift iff square;
- R7: factor allocation collapsed to two formal orientations; square-source status OPEN; integer-lift gate OPEN.

R7B 不重新打开 discriminant square-class、valuation atlas、\(J\)-architecture、moving \(2C\)-modulus 或旧 Gaussian phase architecture。

---

# 3. Primitive Master Row

Raw source-completed master：

\[
A_0Q_0-B_0P_1=C_0
\]

其中

\[
\boxed{
A_0=YG(b_1X+b_2)+b_3,
}
\]

\[
\boxed{
B_0=b_1XYGK,
}
\]

\[
\boxed{
C_0=b_2YP_2+b_3P_3.
}
\]

令

\[
d_{\rm row}=\gcd(A_0,B_0,C_0),
\]

\[
\boxed{
(\widehat A,\widehat B,\widehat C)
=
(A_0,B_0,C_0)/d_{\rm row}.
}
\]

由于 normalization 仅除以正整数，所有 ratio/sign 结论可在 raw row 上证明后直接下降。

## 3.1 Exact source provenance table

| quantity | exact source formula | \(2\)-part | \(5\)-part | primitive content | outer dependence |
|---|---|---|---|---|---|
| \(A_0\) | \(YG(b_1X+b_2)+b_3\) | moving; \(b_3\) prevents pure 10-adic extraction | moving | divide by \(d_{\rm row}\) | \(X=10^{g+d},Y,G\) |
| \(B_0\) | \(b_1XYGK\) | contains full power-10 block plus \(b_1\) | contains full power-10 block plus \(b_1\) | divide by \(d_{\rm row}\) | \(X,Y,G,K\) |
| \(C_0\) | \(b_2YP_2+b_3P_3\) | source dependent | source dependent | divide by \(d_{\rm row}\) | \(Y,P_2,P_3\) |
| \(m_-\) | \((A_0-B_0)/d_{\rm row}\) | moving | moving | primitive-row dependent | all outer variables |
| \(m_+\) | \((A_0+B_0)/d_{\rm row}\) | moving | moving | primitive-row dependent | all outer variables |

No new \(2/5\)-valuation atlas is needed or licensed in R7B.

---

# 4. Exact Oriented Divisibility Criterion

定义：

\[
m_-=\widehat A-\widehat B,
\qquad
m_+=\widehat A+\widehat B,
\]

\[
n_-(\delta)=\widehat C-\delta\widehat W,
\qquad
n_+(\delta)=\widehat C+\delta\widehat W.
\]

square identity gives：

\[
n_-(\delta)n_+(\delta)
=
\widehat C^2-\widehat W^2
=
(\widehat A^2-\widehat B^2)\mathcal N
=
\boxed{m_-m_+\mathcal N}.
\tag{4.1}
\]

formal quotient：

\[
s_+(\delta)=\frac{n_-(\delta)}{m_-},
\qquad
s_-(\delta)=\frac{n_+(\delta)}{m_+}.
\]

若两者为整数，则：

\[
s_+s_-=\mathcal N.
\]

R7B 的关键进一步压缩是：

> **One-Divisibility Reduction.**  
> 若 \(s_+(\delta)\in\mathbf Z\)，则
> \[
> s_-(\delta)=\mathcal N/s_+(\delta).
> \]
> 因而
> \[
> s_-(\delta)\in\mathbf Z
> \iff
> s_+(\delta)\mid\mathcal N.
> \]

所以“两条整除”并非两个独立 arithmetic channels。

---

# 5. Orientation Audit

## 5.1 New source coefficient separation theorem

因为 \(b_2\) 是 \(m_2\)-digit，

\[
b_2\le X-1,
\]

而 \(b_3\) 是 \(m_3=n_3+g\)-digit，

\[
b_3\le YG-1.
\]

又 \(b_1\ge1,\ K\ge10\)。因此

\[
A_0-B_0
=
YG\left[b_2-b_1X(K-1)\right]+b_3
\]

满足

\[
A_0-B_0
\le
YG[(X-1)-9X]+(YG-1)
=
-8XYG-1<0.
\]

故

\[
\boxed{B_0>A_0>0}
\]

及

\[
\boxed{\widehat B>\widehat A>0}.
\tag{5.1}
\]

进一步：

\[
\frac{A_0}{B_0}
=
\frac1K
+
\frac{b_2}{b_1XK}
+
\frac{b_3}{b_1XYGK}.
\]

由 \(b_2\le X-1,\ b_3<YG\)：

\[
\boxed{
\frac1K
<
\frac{\widehat A}{\widehat B}
<
\frac{1+1/b_1}{K}
\le\frac2K.
}
\tag{5.2}
\]

## 5.2 \(C<A\sqrt N\)

Cauchy：

\[
C_0
=
b_2YP_2+b_3P_3
\le
\sqrt{(b_2Y)^2+b_3^2}\sqrt{\mathcal N}.
\]

而

\[
A_0
>
b_2YG+b_3
>
\sqrt{(b_2Y)^2+b_3^2}.
\]

故

\[
\boxed{\widehat C<\widehat A\sqrt{\mathcal N}.}
\tag{5.3}
\]

## 5.3 Orientation collapse

square locus 上：

\[
\widehat W^2
=
\widehat C^2
+
(\widehat B^2-\widehat A^2)\mathcal N
>
\widehat C^2,
\]

故

\[
\widehat W>\widehat C>0.
\]

对 \(\delta=+1\)：

\[
s_+
=
\frac{\widehat C-\widehat W}{\widehat A-\widehat B}
=
\frac{\widehat W-\widehat C}{\widehat B-\widehat A}>0,
\]

\[
s_-=
\frac{\widehat C+\widehat W}{\widehat A+\widehat B}>0.
\]

对 \(\delta=-1\)，两个 quotient 都为负。

因此 positive source 精确选择：

\[
\boxed{\delta=+1}.
\tag{5.4}
\]

formal \(\{\pm1\}\) orientation 不再是两个 source possibilities。

---

# 6. Parity Audit

canonical positive orientation 下写：

\[
x=S_+,\qquad y=S_-.
\]

integer recovery：

\[
Q_0=\frac{x+y}{2},
\qquad
P_1=\frac{x-y}{2}.
\]

故 parity criterion exact 为：

\[
\boxed{x\equiv y\pmod2.}
\tag{6.1}
\]

若 \(\widehat A,\widehat B\) 异奇偶，则 \(m_\pm\) 都为奇数，linear master

\[
m_-x+m_+y=2\widehat C
\]

自动推出 \(x+y\) 偶，因此 parity 自动。

若 \(x,y\) 都偶，primitive sphere 进一步要求 \(P_1,Q_0\) 不能同时偶。于是必须：

\[
\boxed{\min(v_2(x),v_2(y))=1.}
\tag{6.2}
\]

若 \(\mathcal N\) 为奇，则 \(x,y\) 均奇，parity 自动。

---

# 7. CRT Root Class

在尝试 CRT 前必须先通过 row-gcd firewall：

\[
g_{AB}:=\gcd(\widehat A,\widehat B).
\]

primitive row 只有

\[
\gcd(\widehat A,\widehat B,\widehat C)=1.
\]

若 \(g_{AB}>1\)，则 \(g_{AB}\nmid\widehat C\)，所以

\[
\widehat A Q_0-\widehat B P_1=\widehat C
\]

不可能有整数 \((P_1,Q_0)\)。因此：

\[
\boxed{
g_{AB}>1\Longrightarrow\text{integer lift impossible}.
}
\tag{7.1}
\]

只有在 survivor \(g_{AB}=1\) 上才可合法写：

\[
g_m:=\gcd(\widehat B-\widehat A,\widehat A+\widehat B)\in\{1,2\}.
\]

令

\[
a=\widehat B-\widehat A,\quad
b=\widehat A+\widehat B,\quad
g=g_m,
\quad
L=\frac{ab}{g}.
\]

canonical root congruences：

\[
W\equiv C\pmod a,
\qquad
W\equiv-C\pmod b.
\]

令

\[
a'=a/g,\quad b'=b/g.
\]

则：

\[
t\equiv
-\frac{2C}{g}(a')^{-1}
\pmod{b'},
\]

\[
\boxed{
\mathcal R_+
\equiv
C+a\,t
\pmod L.
}
\tag{7.2}
\]

formal opposite orientation 为 \(-\mathcal R_+\)，但已被 positivity 删除。

---

# 8. Modulus-Size Audit

\[
L=\frac{\widehat B^2-\widehat A^2}{g}.
\]

同时：

\[
W^2=C^2+gL\mathcal N.
\]

因此：

\[
L>2W
\iff
L>
2g\mathcal N+2\sqrt{g^2\mathcal N^2+C^2}.
\tag{8.1}
\]

frozen source data 没有强制该 inequality。由于 \(\mathcal N\) 与 \(B\) 都可随 moving profile 增长，R7B 没有获得 universal \(L/W\) separation。

故：

\[
\boxed{\texttt{CRT\_SIZE\_RIGIDITY=NOT\_SOURCE\_FORCED}.}
\]

---

# 9. Quotient-Size Audit

source coefficient ratio 已给：

\[
0<\frac{P_1}{Q_0}
<
\frac{\widehat A}{\widehat B}
<
\frac2K.
\]

因此：

\[
\frac{S_+}{S_-}
=
\frac{1+P_1/Q_0}{1-P_1/Q_0}
<
\frac{K+2}{K-2}.
\]

结合 \(S_+S_-=\mathcal N\) 与 \(P_1>0\)：

\[
\boxed{
\sqrt{\mathcal N}
<
S_+
<
\sqrt{\frac{K+2}{K-2}}\sqrt{\mathcal N},
}
\tag{9.1}
\]

\[
\boxed{
\sqrt{\frac{K-2}{K+2}}\sqrt{\mathcal N}
<
S_-
<
\sqrt{\mathcal N}.
}
\tag{9.2}
\]

在 actual A1 integer/source lift 上还可调用 frozen SPM：

\[
\frac1K<\frac{P_1}{Q_0}
<
\frac{1+1/b_1}{K}.
\]

于是进一步：

\[
\boxed{
\sqrt{\frac{K+1}{K-1}}
<
\frac{S_+}{\sqrt{\mathcal N}}
<
\sqrt{
\frac{K+1+1/b_1}
     {K-1-1/b_1}
}.
}
\tag{9.3}
\]

对于最坏 \(K=10,b_1=1\)，上界为 \(\sqrt{3/2}\approx1.224745\)。

这是 genuine thin divisor annulus，但其绝对宽度仍随 \(\sqrt{\mathcal N}\) 增长，所以不能由 generic divisor spacing 宣称 finite possibilities。

---

# 10. Sphere Factor Pair

canonical orientation：

\[
\boxed{
S_+
=
\frac{W-C}{B-A},
\qquad
S_-=
\frac{W+C}{A+B}.
}
\tag{10.1}
\]

且

\[
\boxed{S_+S_-=\mathcal N.}
\tag{10.2}
\]

linear master：

\[
\boxed{
-(B-A)S_+ +(A+B)S_-=2C.
}
\tag{10.3}
\]

---

# 11. Shared-GCD \(h\) Extraction

若 integer lift 存在，令

\[
h=\gcd(P_1,Q_0).
\]

则

\[
S_+=hX,\qquad S_-=hY,
\]

\[
\gcd(X,Y)\in\{1,2\}.
\]

除 R7 已有

\[
h\mid2C
\]

外，本轮得到更强：

\[
C=AQ_0-BP_1
\]

直接给：

\[
\boxed{h\mid C.}
\tag{11.1}
\]

又

\[
\boxed{h^2\mid\mathcal N.}
\tag{11.2}
\]

所以：

\[
\boxed{
h\mid
\prod_p p^{\min(v_p(C),\lfloor v_p(\mathcal N)/2\rfloor)}.
}
\tag{11.3}
\]

---

# 12. Prime Support of \(h\)

primitive quadruple：

\[
\gcd(P_1,P_2,P_3,Q_0)=1
\]

意味着若 \(p\mid h\)，则 \(p\nmid\gcd(P_2,P_3)\)。

若奇素数 \(p\equiv3\pmod4\) 且 \(p\mid h\)，则 \(p\mid\mathcal N=P_2^2+P_3^2\) 强迫 \(p\mid P_2,P_3\)，矛盾。

若 \(2\mid h\)，则 \(4\mid\mathcal N\) 强迫 \(P_2,P_3\) 都偶，同样矛盾。

故：

\[
\boxed{
h\text{ odd},\qquad
p\mid h\Rightarrow p\equiv1\pmod4.
}
\tag{12.1}
\]

---

# 13. Reduced Coprime Factor Pair

写：

\[
S_+=hX,\qquad
S_-=hY.
\]

则：

\[
XY=\mathcal N/h^2,
\]

\[
\gcd(X,Y)\in\{1,2\},
\]

以及：

\[
\boxed{
-(B-A)X+(A+B)Y=\frac{2C}{h}.
}
\tag{13.1}
\]

因为 \(h\mid C\)，右侧整数。

---

# 14. Inert-Prime Packet Law

令

\[
g_{23}:=\gcd(P_2,P_3),
\qquad
P_2=g_{23}u,\quad P_3=g_{23}v,
\qquad
\gcd(u,v)=1.
\]

则：

\[
\mathcal N=g_{23}^2\mathcal N_*,
\qquad
\mathcal N_*=u^2+v^2.
\]

primitive sum-of-two-squares theorem 给出：

\[
q\equiv3\pmod4
\Longrightarrow
q\nmid\mathcal N_*.
\]

因此所有 odd inert prime content 都来自 \(g_{23}^2\)。

又

\[
\gcd(h,g_{23})=1.
\]

所以 inert \(q^{2e}\) 不能进入 shared \(h\)，并且在 reduced \(X,Y\) 中必须 whole-packet 分给一边。

---

# 15. Split-Prime Allocation Space

对 primitive norm：

\[
\mathcal N_*
=
2^\epsilon
\prod_{p\equiv1(4)}p^{e_p}.
\]

对每个 split prime \(p\)，定义 shared exponent

\[
t_p=v_p(h),
\qquad
0\le t_p\le
\min\!\left(
v_p(C),
\left\lfloor e_p/2\right\rfloor
\right),
\]

并且 \(e_p-2t_p\) 的剩余 packet 在 reduced \(X,Y\) 中必须 whole-packet 进入一边。

因此 formal packet space 可写成：

\[
\boxed{
\prod_{p\equiv1(4)}
\left\{
(t_p,\epsilon_p):
0\le t_p\le t_p^{\max},
\ \epsilon_p\in\{+,-\}
\text{ if }e_p-2t_p>0
\right\}
}
\tag{15.1}
\]

再乘上 \(g_{23}^2\) 中各 odd prime-square packet 的 side choice 以及唯一 \(2\)-adic parity law。

但这只是 multiplicative factor-pair space。full master 会把它压成至多一个 point；见第 20 节。

---

# 16. Gaussian Packet Interpretation

令：

\[
z_0=u+iv,\qquad \gcd(u,v)=1.
\]

则 odd \(q\equiv3(4)\) 不整除 \(N(z_0)\)。

若

\[
p=\pi\bar\pi,\qquad p\equiv1\pmod4,
\]

primitive \(z_0\) 对 \(\pi,\bar\pi\) 的选择只记录 split-prime packet orientation。quotient Gaussian unit 与整体 conjugation 后，没有 continuous phase freedom。

R7B 不需要也不允许 unit orbit / angle / phase machinery。

---

# 17. \((m_\pm)\)-vs-\(\mathcal N\) GCD Audit

定义：

\[
g_-=\gcd(\widehat A-\widehat B,\mathcal N),
\]

\[
g_+=\gcd(\widehat A+\widehat B,\mathcal N).
\]

本轮未发现 source theorem 强制 \(g_\pm\) 为固定值、固定大 divisor 或固定小 divisor。

特别地，prime \(p\mid m_-\) 并不需要通过 \(p\mid\mathcal N\) “供应”给 \(S_+\)。整除条件只是要求对应 square root 选定 local sign：

\[
W\equiv C\pmod{p^{v_p(m_-)}}.
\]

所以“modulus prime 必须由 sphere norm supply”不是正确的一般机制。

---

# 18. External Modulus Prime Audit

定义 external prime：

\[
p\mid m_-,
\qquad
p\nmid\mathcal N.
\]

由

\[
W^2-C^2=(B^2-A^2)\mathcal N
\]

可知 \(p\mid m_-\) 已自动使

\[
W^2\equiv C^2\pmod{p^e}.
\]

integer lift 要求选中 \(W\equiv C\) 的 local root branch；并不要求 \(p\mid\mathcal N\)。

因此：

\[
\boxed{
\texttt{EXTERNAL\_MODULUS\_PRIME\_SUPPLY\_OBSTRUCTION
=FALSE\_AS\_GENERAL\_MECHANISM}.
}
\]

---

# 19. Prescribed-Residue Divisor Problem

在 row-gcd survivor 上：

\[
a=B-A,\quad b=A+B,\quad g=\gcd(a,b)\in\{1,2\}.
\]

若 first quotient

\[
x=\frac{W-C}{a}
\]

为整数，则 second divisibility 等价于：

\[
b\mid ax+2C.
\]

即：

\[
\boxed{
\frac ag x
\equiv
-\frac{2C}{g}
\pmod{b/g}.
}
\tag{19.1}
\]

由于 \(\gcd(a/g,b/g)=1\)，这为 \(x\) 指定唯一 residue class modulo \(b/g\)。

但因为 \(x\) 已由 global square root 唯一确定，(19.1) 不是新的 independent tuning parameter；它是 divisor-membership gate 的 residue shadow。

---

# 20. Simultaneous Divisibility Theorem Attempt

定义：

\[
F(x)=a x^2+2Cx-b\mathcal N.
\]

则：

\[
F'(x)=2ax+2C>0
\qquad(x>0).
\]

因此 \(F\) 在正轴严格递增，最多一个正根。

并且：

\[
F(x)=0
\iff
-a x+b\frac{\mathcal N}{x}=2C.
\]

故：

> **R7B Unique Positive Divisor Theorem.**  
> 对 fixed source profile，full multiplicative + additive system
> \[
> xy=\mathcal N,\qquad -ax+by=2C,\qquad x,y>0
> \]
> 至多有一个 real solution pair。若 square locus 成立，该 pair 就是
> \[
> x=x_W=(W-C)/a,\qquad y=N/x_W.
> \]
> 因而 split/inert packet allocation 不能在 master 已固定后继续自由选择。

这正式否定了“从 exponentially many factor splits 中挑一个满足 master”的 architecture：master 已经先把 split space 压成 singleton-or-empty。

---

# 21. Split-Prime Source Allocation Obstruction

本轮没有证明某个 split-prime packet 永远冲突。

反而证明了更基础的 architecture correction：

\[
\boxed{
\text{split-prime allocation is not a second free channel after full master}.
}
\]

它只是在检查：

\[
x_W\in\operatorname{Div}_{\rm prim}^{\rm src}(\mathcal N)
\]

时提供 primewise certificate。

因此：

\[
\boxed{
\texttt{SPLIT\_PRIME\_SOURCE\_ALLOCATION\_OBSTRUCTION=NOT\_PROVED}.
}
\]

---

# 22. Reverse Integer-Lift Construction

R7B 的合法 reverse construction 不应自由工程 \(A,B,C\)。给定真实 source coefficients 后，只需寻找：

\[
x\mid\mathcal N
\]

满足：

\[
\boxed{
a x^2+2Cx-b\mathcal N=0.
}
\tag{22.1}
\]

然后令：

\[
y=\mathcal N/x,
\]

检查：

\[
x\equiv y\pmod2,
\]

并恢复：

\[
Q_0=\frac{x+y}{2},
\qquad
P_1=\frac{x-y}{2}.
\]

这一路径自动产生：

\[
W=C+ax.
\]

因此 square condition不再需要单独重新检查；它由 (22.1) 反推。

---

# 23. Exact Witness Search

R7 已完成的 reduced-shell exact scan 共检查 1,899,000 个值而无 square hit。该结果仍只作为 finite computational evidence。

R7B 没有找到新的 S3/S4 source-legal square + divisor witness。

保留 fixed-character regression：

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),
\]

\[
(\widehat A,\widehat B,\widehat C)=(21,125,549),
\]

\[
W=20621,\quad
S_+=193,\quad
S_-=145.
\]

它精确验证本轮 theorem，但位于 \(g=0\) fixed-character region，不是 outer witness。

---

# 24. \((P_1,Q_0)\) Recovery

若 PSDG 通过：

\[
x=x_W,\qquad y=\mathcal N/x,
\]

则：

\[
\boxed{
Q_0=(x+y)/2,
\qquad
P_1=(x-y)/2.
}
\]

由第 5 节 \(C<A\sqrt N\) 可证明 canonical positive rational root 自动满足 \(P_1>0\)，因此 sign defect已 theoremically eliminated。

---

# 25. Primitive Lift Audit

令：

\[
g_{23}=\gcd(P_2,P_3),
\]

\[
h(x)=
\gcd\left(
\frac{x-y}{2},
\frac{x+y}{2}
\right).
\]

则：

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1
\iff
\gcd(h(x),g_{23})=1.
}
\tag{25.1}
\]

因此定义 canonical primitive divisor set：

\[
\boxed{
\operatorname{Div}_{\rm prim}(\mathcal N;P_2,P_3)
=
\left\{
x>0:
\begin{array}{l}
x\mid\mathcal N,\ y=\mathcal N/x,\\
x>y,\ x\equiv y\pmod2,\\
\gcd(h(x),g_{23})=1
\end{array}
\right\}.
}
\tag{25.2}
\]

---

# 26. Smith / DES Audit

当前没有 outer integer witness，因此不能进入 genuine Smith/DES replay。

R7B 只使用了 frozen Smith consequences：

- source denominator dictionary;
- primitive/source gcd provenance;
- \(h\) 与 \(g_{23}\) 的 primitive firewall.

没有签 `SMITH_LIFT=YES` 或 `DES_LIFT=YES`。

---

# 27. Source Fibre / Digit / Actual-Cut Audit

没有 outer integer witness，因此：

```text
SOURCE_FIBRE_LIFT=NOT_REACHED
DIGIT_LIFT=NOT_REACHED
ACTUAL_CUT_LIFT=NOT_REACHED
OUTER_LIFT=NOT_REACHED
```

注意：第 5 节 coefficient separation 与第 9 节 quotient upper annulus确实使用了真实 decimal block provenance，但这不等价于完成 downstream source reconstruction。

---

# 28. New First-Failure Gate

由于尚未证明任何 S3/S4 integer lift 存在，不能把 first-failure gate 后移到 DES/digit/actual-cut。

但 R7 的 “two oriented divisibilities / split allocation” gate 已被重新命名并压缩为：

\[
\boxed{
\texttt{NEW\_FIRST\_FAILURE\_GATE
=
PRESCRIBED\_SOURCE\_DIVISOR\_MEMBERSHIP}.
}
\]

其 exact object：

\[
x_W=
\frac{W-C}{B-A}
\stackrel{?}{\in}
\operatorname{Div}_{\rm prim}(\mathcal N;P_2,P_3).
\]

---

# 29. Failed / Falsified Routes

本轮 theoremically retire：

1. **Two-independent-moduli heuristic** — false as architecture; one quotient integral + divisor membership already controls second.
2. **CRT square-modulus collision** — tautological:
   \[
   \mathscr D=C^2+gL\mathcal N\equiv C^2\equiv\mathcal R_+^2\pmod L.
   \]
3. **External-prime supply heuristic** — false; modulus primes need not divide \(\mathcal N\).
4. **Exponential split-choice after master** — false; additive master has at most one positive real factor pair.
5. **\(\gcd(m_-,m_+)\le2\) as pre-lift obstruction** — circular unless row-gcd survivor \(g_{AB}=1\) has first been established.
6. **Formal \(\delta=\pm1\) as two positive source orientations** — false; source coefficients force only \(\delta=+1\).
7. **Generic divisor spacing from thin annulus** — insufficient; absolute annulus width grows with \(\sqrt N\).

---

# 30. Exact Remaining Unknowns

只剩一个 central arithmetic question：

\[
\boxed{
\textbf{PSDG:}\quad
x_W=
\frac{W-C}{B-A}
\text{ 是否能属于 }
\operatorname{Div}_{\rm prim}(\mathcal N;P_2,P_3)
\text{ 对某个 S3/S4 source-legal square profile？}
}
\]

等价：

\[
\boxed{
\exists x\in\operatorname{Div}_{\rm prim}(\mathcal N;P_2,P_3):
(B-A)x^2+2Cx-(A+B)\mathcal N=0.
}
\tag{30.1}
\]

尚未证明 empty，也未构造 witness。

primewise 展开时，剩余 odd-prime information 由 shared split part \(h\)、primitive split packets、以及 \(g_{23}^2\) content packets完整描述；但它们不再是 independent tuning variables。

---

# 31. R7B Terminal Verdict

\[
\boxed{
\texttt{R7B\_TERMINAL\_VERDICT
=
SINGLE\_PRESCRIBED\_PRIMITIVE\_DIVISOR\_GATE}.
}
\]

本轮关键新增：

\[
\boxed{
B>A,\qquad
A/B<2/K,\qquad
C<A\sqrt N,
}
\]

\[
\boxed{
\text{positive orientation unique},
}
\]

\[
\boxed{
\text{two divisibilities}
\iff
\text{one divisibility + divisor membership},
}
\]

\[
\boxed{
\text{full factor-pair affine system has at most one positive candidate},
}
\]

\[
\boxed{
h\mid C,\quad
h^2\mid N,\quad
h\text{ split-prime supported},
}
\]

\[
\boxed{
\text{CRT square collision tautological}.
}
\]

但：

\[
\boxed{
\texttt{SIMULTANEOUS\_DIVISIBILITY\_STATUS=OPEN\_AT\_PSDG}.
}
\]

---

# 32. R8 Authorization Decision

用户给出的 R8 Route A/B/C 均未满足：

- Route A requires universal integer-lift kill — **NO**;
- Route B requires an integer lift followed by later failure — **NO witness**;
- Route C requires full source lift/family — **NO**.

Route D requires reduction specifically to a single split-prime gate。R7B 的更精确结论是 single **prescribed primitive-divisor gate**；它包含 split-prime packet certification，但尚不能 theoremically 删除全部 non-split packet content。因此不冒充 Route D。

故：

\[
\boxed{\texttt{R8\_AUTHORIZED=NO}.}
\]

若继续，必须仍停留在 R7 continuation，直接解决 PSDG，而不是重开 discriminant / valuation / generic Gaussian architecture。

---

# 33. Shock Checkpoint Answers

**Q1 — explicit \(m_\pm,n_\pm\)?** YES.  
**Q2 — two orientations independent?** NO; positive source collapses to \(\delta=+1\).  
**Q3 — CRT class rigid?** NO; square-mod collision tautological, size rigidity not proved.  
**Q4 — quotient-size finite?** NO; but exact thin multiplicative annulus proved.  
**Q5 — shared gcd \(h\) controlled?** YES profilewise: \(h\mid C,\ h^2\mid N,\ h\) split-only; no uniform finite bound.  
**Q6 — remaining packets binary?** YES after removing \(h\), all odd packets are whole-side packets; however full master fixes at most one allocation.  
**Q7 — inert direct contradiction?** NOT UNIVERSAL.  
**Q8 — split packets enough?** Not a free-choice question after master; reduced to membership.  
**Q9 — outer square + oriented witness?** NO.  
**Q10 — outer integer \(P_1,Q_0\)?** NO.

---

# 34. Machine-readable Terminal Block

```text
R7B_TERMINAL_VERDICT=SINGLE_PRESCRIBED_PRIMITIVE_DIVISOR_GATE

R1_R2_R3_R4_R5_R5C_R6_R7_STATE_FROZEN=YES

SQUARE_LOCUS_ASSUMED=YES
COMPLEMENTARY_DISCRIMINANT=W_HAT^2=C_HAT^2+(B_HAT^2-A_HAT^2)*N

MASTER_ROW_PRIMITIVE=YES
A_HAT=[YG(b1*X+b2)+b3]/d_row
B_HAT=[b1*X*Y*G*K]/d_row
C_HAT=[b2*Y*P2+b3*P3]/d_row
W_HAT=positive_sqrt(COMPLEMENTARY_DISCRIMINANT)

M_MINUS=A_HAT-B_HAT<0
M_PLUS=A_HAT+B_HAT>0
GCD_M_MINUS_M_PLUS=IN_{1,2}_ONLY_AFTER_GCD(A_HAT,B_HAT)=1_FIREWALL

ORIENTATION_SET={+1,-1}_FORMAL
ORIENTATION_COLLAPSED=YES_TO_DELTA_PLUS_FOR_POSITIVE_SOURCE

N_MINUS_PLUS=C_HAT-W_HAT
N_PLUS_PLUS=C_HAT+W_HAT
N_MINUS_MINUS=C_HAT+W_HAT
N_PLUS_MINUS=C_HAT-W_HAT

ORIENTED_DIVISIBILITY_PLUS=ONE_DIVISIBILITY_PLUS_DIVISOR_MEMBERSHIP
ORIENTED_DIVISIBILITY_MINUS=NEGATIVE_QUOTIENTS_SOURCE_ILLEGAL

ORIENTED_INTEGER_LIFT_INVARIANT=(ROW_GCD_DEFECT,FIRST_RESIDUE,DIVISOR_DEFECT,PARITY_DEFECT,PRIMITIVE_DEFECT)
PARITY_DEFECT=(S_PLUS-S_MINUS) mod 2
EXACT_INTEGER_LIFT_CRITERION=X_W_IN_DIV_PRIM_SOURCE(N;P2,P3)

CRT_MODULUS=(B_HAT^2-A_HAT^2)/g_m
CRT_ROOT_CLASS=W_HAT == C_HAT+(B_HAT-A_HAT)*t mod CRT_MODULUS; t=-(2C/g)*(a/g)^(-1) mod (b/g)
CRT_RIGIDITY=NO_SQUARE_MOD_COLLISION_IS_TAUTOLOGICAL_AND_SIZE_NOT_UNIVERSAL

QUOTIENT_SIZE_S_PLUS=sqrt(N)<S_PLUS<sqrt((K+2)/(K-2))*sqrt(N)
QUOTIENT_SIZE_S_MINUS=sqrt((K-2)/(K+2))*sqrt(N)<S_MINUS<sqrt(N)
FINITE_QUOTIENT_POSSIBILITIES=NO_UNIVERSAL

S_MINUS=(W_HAT+C_HAT)/(A_HAT+B_HAT)
S_PLUS=(W_HAT-C_HAT)/(B_HAT-A_HAT)
SPHERE_PRODUCT=S_PLUS*S_MINUS=N

SHARED_GCD_H=gcd(P1,Q0)
H_PRIME_SUPPORT=ODD_PRIMES_1_MOD_4_ONLY
H_DIVIDES_2C=YES_STRONGER_H_DIVIDES_C
H_SOURCE_BOUND=h | product_p p^min(vp(C),floor(vp(N)/2)); gcd(h,gcd(P2,P3))=1

REDUCED_FACTOR_X=S_PLUS/h
REDUCED_FACTOR_Y=S_MINUS/h
GCD_X_Y=1_OR_2

INERT_PRIME_PACKET_LAW=ALL_ODD_INERT_CONTENT_COMES_FROM_gcd(P2,P3)^2_AND_WHOLE_PACKET_TO_ONE_REDUCED_SIDE
SPLIT_PRIME_ALLOCATION_SPACE=SHARED_EXPONENT_t_p_PLUS_ONE_SIDE_BIT_FOR_REMAINING_PACKET
SPLIT_PRIME_SHARED_PART=h
SPLIT_PRIME_REMAINING_FREEDOM=FORMAL_PACKET_SPACE_COLLAPSES_TO_AT_MOST_ONE_POINT_AFTER_ADDITIVE_MASTER

GCD_M_MINUS_N=PROFILE_DEPENDENT_NO_UNIVERSAL_FORMULA
GCD_M_PLUS_N=PROFILE_DEPENDENT_NO_UNIVERSAL_FORMULA
EXTERNAL_MODULUS_PRIMES=NOT_AUTOMATIC_OBSTRUCTION

SIMULTANEOUS_DIVISIBILITY_STATUS=OPEN_AT_PSDG
SPLIT_PRIME_SOURCE_ALLOCATION_OBSTRUCTION=NOT_PROVED

INTEGER_LIFT_WITNESS_FOUND=NO_OUTER_WITNESS
WITNESS_ORIENTATION=N/A
P1=N/A_OUTER
Q0=N/A_OUTER
P2=N/A_OUTER_WITNESS
P3=N/A_OUTER_WITNESS

SPHERE_VALID=CONDITIONAL_ON_SQUARE_PROFILE
MASTER_VALID=RATIONAL_YES_ON_SQUARE_PROFILE
INTEGER_LIFT=OPEN_AT_PSDG
PRIMITIVE_LIFT=OPEN_AFTER_PSDG
SMITH_LIFT=NOT_REACHED
DES_LIFT=NOT_REACHED
SOURCE_FIBRE_LIFT=NOT_REACHED
DIGIT_LIFT=NOT_REACHED
ACTUAL_CUT_LIFT=NOT_REACHED
OUTER_LIFT=NO_WITNESS

NEW_FIRST_FAILURE_GATE=PRESCRIBED_SOURCE_DIVISOR_MEMBERSHIP

RETIRED_AFTER_R7B=TWO_ORIENTATION_POSITIVE_SOURCE;TWO_INDEPENDENT_DIVISIBILITY_HEURISTIC;CRT_SQUARE_COLLISION;EXTERNAL_PRIME_SUPPLY;EXPONENTIAL_SPLIT_CHOICE_AFTER_MASTER

R8_AUTHORIZED=NO
R8_ARCHITECTURE=NONE_YET
R8_SINGLE_ATTACK_TARGET=N/A_UNTIL_PSDG_RESOLVED
```
