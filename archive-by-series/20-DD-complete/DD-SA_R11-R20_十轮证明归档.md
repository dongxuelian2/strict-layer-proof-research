# DD-SA R11–R20 阶段归档  
## 跨三个 W0 branch 的共同机制研究：从 Residual Tail 到 D-Split Firewall

> **归档范围**：DD-SA 第十一轮至第二十轮  
> **核心目标**：寻找一个在 \(W0\)-A / \(W0\)-B / \(W0\)-C 三个 branch 分裂之前已经成立、并有希望解释三支共同灭绝的结构原因。  
> **当前总状态**：
>
> \[
> \boxed{W0\text{-A/B/C simultaneous extinction = OPEN}}
> \]
>
> 但十轮之后，若干假路线已被严格退休，并得到一条明显更上游的统一结构链：
>
> \[
> \boxed{
> \text{Residual-Tail Exact Quotient}
> \;\Longrightarrow\;
> \text{\(D\)-Prime Equal-Load}
> \;\Longrightarrow\;
> \text{\(D\)-Split Firewall}
> }
> \]
>
> 即：在 \(5\)-adic W0 branch 分裂之前，source integrality 已经把所有 Gaussian non-split denominator support 清洗进 \(h\)，而 surviving cofactor \(D=G/h\) 只能含 \(p\equiv1\pmod4\) 的素因子。

---

# 0. 统一记号与冻结背景

本阶段始终研究 DD 的 W0 区域，且不再把 W0-A/B/C 当作首要研究坐标。

统一记：

\[
T:=10^{m_3},
\qquad
Q:=b_1 10^{m_2}+b_2,
\qquad
G:=b_1b_2,
\]

\[
P:=a_1 10^{n_2}+a_2,
\qquad
N:=(a_1b_2)^2+(a_2b_1)^2.
\]

source normalization：

\[
h:=\gcd(\kappa,G),
\qquad
A_\kappa:=\frac{\kappa}{h},
\qquad
D:=\frac Gh,
\]

\[
c:=\frac{TQ}{A_\kappa},
\qquad
b_3=cD.
\]

canonical source factor system：

\[
uv=Nc^2,
\qquad
v-u=2ha_3,
\]

\[
F_-:=B_\kappa u,
\qquad
F_+:=A_\kappa v,
\qquad
B_\kappa:=A_\kappa+2D,
\]

以及 exact factor sum：

\[
F_-+F_+=2GP10^{n_3}.
\]

DD carrier surplus：

\[
d_3:=n_3-m_3>0,
\]

并保留阶段前文已经恢复的 surplus simplex：

\[
s_1+s_2+d_3-\max(s_1,s_2,d_3)\le2.
\]

W0 的旧三分支为：

\[
W0\text{-A}: 5\nmid c,
\]

\[
W0\text{-B}: 5\mid c,\quad v_5(F_-)\ne v_5(F_+),
\]

\[
W0\text{-C}: 5\mid c,\quad v_5(F_-)=v_5(F_+),
\]

但 R11–R20 的主策略是：

\[
\boxed{
\textbf{优先寻找 branch split 之前的统一 source/cut 机制。}
}
\]

---

# 1. R11：Residual-Tail / Norm Transfer

## 1.1 residual decimal tail

定义：

\[
\omega:=\gcd(T,b_3),
\]

\[
L:=\frac{T}{\omega},
\qquad
\tau:=\frac{b_3}{\omega},
\qquad
\gcd(L,\tau)=1.
\]

因为 \(0<b_3<T\)，有：

\[
\boxed{L>1.}
\]

所以每个 genuine DD candidate 都携带非平凡 residual decimal tail。

---

## 1.2 \(L\mid A_\kappa\)

由：

\[
\kappa=\frac{TQG}{b_3},
\qquad
G=hD,
\]

得到：

\[
A_\kappa
=
\frac{\kappa}{h}
=
\frac{TQD}{b_3}
=
\frac{LQD}{\tau}.
\]

因为 \(A_\kappa\in\mathbb Z\) 且 \(\gcd(L,\tau)=1\)，有：

\[
\boxed{L\mid A_\kappa.}
\]

---

## 1.3 \(L\mid u\)

设：

\[
C:=10^{d_3}P,
\]

完整 numerator / denominator：

\[
\alpha=TC+a_3,
\qquad
\beta=TQ+b_3.
\]

定义 oriented decimal determinant：

\[
\Delta:=Cb_3-Qa_3.
\]

则：

\[
\alpha b_3-a_3\beta
=
T\Delta.
\]

由 source geometry：

\[
u
=
hb_3
\left(
\frac{\alpha}{\beta}
-
\frac{a_3}{b_3}
\right)
=
\frac{hT\Delta}{\beta}.
\]

又：

\[
\beta=\omega(LQ+\tau),
\]

所以：

\[
u=\frac{hL\Delta}{LQ+\tau}.
\]

因为：

\[
\gcd(L,LQ+\tau)=1,
\]

integrality of \(u\) 强迫：

\[
\boxed{L\mid u.}
\]

于是由：

\[
uv=Nc^2,
\]

得到：

\[
\boxed{L\mid Nc^2.}
\]

---

## 1.4 Residual-Tail / Norm Transfer

对 \(p=2,5\)，定义：

\[
t_p:=v_p(b_3),
\qquad
r_p:=v_p(L)=\max(m_3-t_p,0).
\]

则：

\[
\boxed{
r_p\le v_p(N)+2v_p(c).
}
\]

即：

\[
\boxed{
(m_3-v_p(b_3))_+
\le
v_p(N)+2v_p(c).
}
\]

**状态：PROVED**

---

## 1.5 exact \(2\)-adic norm law

令：

\[
X:=a_1b_2,\qquad
Y:=a_2b_1.
\]

若：

\[
\lambda_X:=v_2(X),
\qquad
\lambda_Y:=v_2(Y),
\]

则：

\[
\boxed{
v_2(N)
=
2\min(\lambda_X,\lambda_Y)
+
\mathbf 1_{\lambda_X=\lambda_Y}.
}
\]

原因：

- 若两 valuation 不等，无 cancellation；
- 若相等，约去共同 \(2\)-power 后得到两个奇数平方之和，模 \(8\) 等于 \(2\)，只多一位。

这说明：

\[
\boxed{
2\text{-adic equal-leg cancellation capacity}=1.
}
\]

---

# 2. R12：Decimal-Tail Deficit 与 \(1/3\)-phase

## 2.1 \(\gcd(L,D)=1\)

已有：

\[
L\mid A_\kappa,
\qquad
\gcd(A_\kappa,D)=1.
\]

故：

\[
\boxed{\gcd(L,D)=1.}
\]

因此若：

\[
p\mid L,
\]

则：

\[
p\nmid D.
\]

因为：

\[
b_3=cD,
\]

得到：

\[
\boxed{
v_p(c)=v_p(b_3)
\qquad (p\mid L).
}
\]

---

## 2.2 Decimal-Tail Deficit Theorem

设：

\[
t_p:=v_p(b_3)<m_3.
\]

由：

\[
L\mid u
\]

有：

\[
v_p(u)\ge m_3-t_p.
\]

而：

\[
uv=Nc^2,
\qquad
v_p(c)=t_p.
\]

所以：

\[
v_p(N)+2t_p
=
v_p(u)+v_p(v)
\ge m_3-t_p.
\]

故：

\[
\boxed{
v_5(N)\ge
\bigl(m_3-3v_5(b_3)\bigr)_+.
}
\]

对 \(p=2\)，因为 \(2\mid u\) 后：

\[
v-u=2ha_3
\]

强迫 \(v\) 也为偶数，所以多一位：

\[
\boxed{
v_2(N)\ge
\bigl(m_3+1-3v_2(b_3)\bigr)_+.
}
\]

**状态：PROVED**

---

## 2.3 \(1/3\)-phase boundary

令：

\[
\delta_5:=
(m_3-3v_5(b_3))_+,
\]

\[
\delta_2:=
(m_3+1-3v_2(b_3))_+.
\]

则：

\[
\boxed{
2^{\delta_2}5^{\delta_5}\mid N.
}
\]

系数 \(3\) 的来源：

- residual tail 要求 \(m-t\)；
- \(c^2\) 最多吸收 \(2t\)；
- 净 deficit：
  \[
  m-t-2t=m-3t.
  \]

所以：

\[
\boxed{t\approx m/3}
\]

不是人为阈值，而是系统自身产生的相变面。

---

## 2.4 odd third denominator parity collapse

R12 进一步证明：

\[
\boxed{
b_3\text{ odd}
\Longrightarrow
b_1,b_2\text{ both odd}.
}
\]

证明分两步：

1. \(b_1,b_2\) mixed parity 会使 \(N\) 为奇数，但 \(\delta_2>0\) 强迫 \(N\) 偶；
2. \(b_1,b_2\) 同时偶会与 exact factor-sum valuation 和 source difference 冲突。

**状态：PROVED**

---

# 3. R13：Same-Cut Feedback 与 source/cut parity matching

## 3.1 all-W0 same-cut feedback

定义：

\[
\alpha_i:=v_2(a_i),
\qquad
e_i:=v_2(b_i).
\]

则：

\[
v_2(N)
=
2s+\varepsilon,
\]

其中：

\[
s=
\min(\alpha_1+e_2,\alpha_2+e_1).
\]

而：

\[
P=a_1 10^{n_2}+a_2.
\]

可证明：

\[
\boxed{
v_2(GP)
\ge
\left\lfloor\frac{v_2(N)}2\right\rfloor.
}
\]

因此 exact factor sum：

\[
F_-+F_+
=
2GP10^{n_3}
\]

给：

\[
\boxed{
v_2(F_-+F_+)
\ge
n_3+1+
\left\lfloor\frac{v_2(N)}2\right\rfloor.
}
\]

这是第一条真正的：

\[
\boxed{
\text{tail}\to N\to actual\ cut\to P\to factor\ sum
}
\]

闭环。

---

## 3.2 source label exceptional layer

在 residual \(2\)-tail 下，记：

\[
r:=m_3-v_2(b_3),
\qquad
q:=v_2(Q).
\]

则：

\[
v_2(A_\kappa)=r+q.
\]

而：

\[
B_\kappa=A_\kappa+2D,
\qquad
D\text{ odd}.
\]

于是：

\[
v_2(A_\kappa)\ge2
\Longrightarrow
v_2(B_\kappa)=1.
\]

唯一异常：

\[
\boxed{
v_2(A_\kappa)=1
\iff
r=1,\quad q=0.
}
\]

**状态：PROVED**

---

## 3.3 resonance 下 exact no-hidden-slack

若：

\[
v_2(F_-)=v_2(F_+),
\]

且 \(2\mid b_3\)，设：

\[
a:=v_2(A_\kappa),
\qquad
b:=v_2(B_\kappa),
\qquad
g:=v_2(G),
\qquad
t:=v_2(b_3).
\]

则：

\[
\boxed{
v_2(N)
=
2+2g+|a-b|-2t.
}
\]

非异常时：

\[
a=r+q,\qquad b=1,
\]

所以：

\[
\boxed{
v_2(N)
=
\delta_2+2v_2(G)+v_2(Q).
}
\]

此外 exact two-square law 给：

\[
\boxed{
\mathbf1_{v_2(a_1b_2)=v_2(a_2b_1)}
\equiv
|v_2(A_\kappa)-v_2(B_\kappa)|
\pmod2.
}
\]

即 source labels 的 parity 决定 actual cut weighted legs 是否落在同一 \(2\)-adic diagonal。

---

# 4. R14：Cut-Loaded Parity Collapse 与 Half-Tail Phase

## 4.1 cut-loaded parity collapse

在：

\[
\delta_2:=m_3+1-3v_2(b_3)>0
\]

的区域：

- mixed parity 不可能；
- even/even 也不可能。

最终：

\[
\boxed{
\delta_2>0
\Longrightarrow
b_1,b_2\text{ both odd}.
}
\]

**状态：PROVED**

这是 R14 的核心收缩。

---

## 4.2 even/even pseudo-survivor 被删除

R13 曾留下一个“even/even prefix 通过超深 denominator seam cancellation 逃离 resonance”的候选。

R14 重新检查 exact factor-sum 后证明：

- factor sum 先强制 resonance；
- resonance 与 even/even norm capacity 冲突。

因此：

\[
\boxed{
\text{Deep Denominator-Seam Escape}= \varnothing.
}
\]

**状态：RETIRED / ELIMINATED**

---

## 4.3 automatic \(2\)-factor resonance

除唯一浅层：

\[
(m_3,v_2(b_3))=(1,0)
\]

外，cut-loaded 区自动有：

\[
\boxed{
v_2(F_-)=v_2(F_+).
}
\]

若 \(t:=v_2(b_3)>0\)，则：

\[
\boxed{
v_2(N)=m_3+1-3t.
}
\]

若 \(t=0,\ m_3\ge2\)，则：

\[
\boxed{
v_2(N)
=
m_3+1+2v_2(a_3).
}
\]

---

## 4.4 Common Numerator \(2\)-Core

因为 cut-loaded 下 \(b_1,b_2\) 都奇，令：

\[
\sigma
:=
\left\lfloor\frac{v_2(N)}2\right\rfloor.
\]

则：

\[
\boxed{
2^\sigma\mid a_1,
\qquad
2^\sigma\mid a_2.
}
\]

所以：

\[
2^\sigma\mid P.
\]

---

## 4.5 Half-Tail Phase Law

定义：

\[
\eta
:=
v_2(P)-\sigma\ge0.
\]

归一化 source factors 后：

\[
\widetilde F_\pm
:=
F_\pm/2^{v_2(F_\pm)}.
\]

则：

\[
\boxed{
v_2(\widetilde F_-+\widetilde F_+)
=
d_3+
\left\lfloor\frac{r_2+1}{2}\right\rfloor
+\eta.
}
\]

其中：

\[
r_2:=m_3-v_2(b_3).
\]

若 \(r_2\) 偶：

\[
\boxed{\eta=0.}
\]

所以：

\[
\boxed{
v_2(\widetilde F_-+\widetilde F_+)
=
d_3+\frac{r_2}{2}.
}
\]

---

## 4.6 纯 valuation-size 路线失败

将 common numerator core 与 surplus simplex 拼接，只能得到：

\[
2\sigma
<
(S+2)\log_2 10.
\]

而 W0 height envelope 的 slope 约：

\[
2\log_5 10
=
2.861353\ldots
\]

低于：

\[
\log_2 10
=
3.321928\ldots
\]

所以：

\[
\boxed{
\text{surplus simplex + pure \(2\)-core size}
}
\]

不足以 closure。

**状态：FAILED BY SLOPE**

---

# 5. R15：Local Hensel Collapse 与 Norm-Load Router

## 5.1 Half-Tail Phase 不是 local \(2\)-adic killer

在 cut-loaded normalized source system 中，可写：

\[
u=2^{r+\zeta}U,
\qquad
v=2^{1+\zeta}V,
\]

其中 \(U,V\) 奇。

归一化 product / difference 后得到：

\[
UV=N_0c_0^2,
\]

\[
V-2^{r-1}U=ha_3^\circ.
\]

消去 \(V\)：

\[
\boxed{
2^{r-1}U^2
+
ha_3^\circ U
-
N_0c_0^2
=
0.
}
\]

其导数：

\[
2^rU+ha_3^\circ
\]

为 \(2\)-adic unit。

因此 Hensel 唯一提升到任意深度。

所以：

\[
\boxed{
\text{Half-Tail Phase as pure \(2\)-adic killer = FALSE.}
}
\]

**状态：RETIRED**

---

## 5.2 Two-Prime No-Hidden-Slack

对 \(p=2,5\)，令：

\[
e_p:=v_p(2)
=
\begin{cases}
1,&p=2,\\
0,&p=5.
\end{cases}
\]

在 residual、resonant、nonexceptional normal form 中：

\[
\boxed{
v_p(N)
=
m_3
+
v_p(Q)
+
2v_p(G)
+
e_p
+
2v_p(a_3)
-
3v_p(b_3).
}
\]

这统一了此前分别得到的 \(2\)-adic 与 \(5\)-adic no-hidden-slack。

---

## 5.3 Two-Prime normalized source system

归一化后统一得到：

\[
\boxed{
p^{a-e_p}U^2
+
\lambda_p h_0a_3^\circ U
-
N_pc_0^2
=
0,
}
\]

其中：

\[
\lambda_2=1,
\qquad
\lambda_5=2.
\]

导数在 \(p=2,5\) 下都是 \(p\)-adic unit。

所以：

\[
\boxed{
\text{deep source Hensel cannot be the common W0 obstruction.}
}
\]

**状态：RETIRED**

---

## 5.4 Norm-Load Decomposition

令：

\[
X=a_1b_2,
\qquad
Y=a_2b_1.
\]

对 \(p=2,5\)，定义：

\[
s_p:=\min(v_p(X),v_p(Y)),
\]

\[
\lambda_p:=v_p(N)-2s_p.
\]

则：

\[
\boxed{
v_p(N)=2s_p+\lambda_p.
}
\]

其中：

\[
\boxed{
\lambda_2\in\{0,1\},
}
\]

而：

\[
\lambda_5
\]

可以任意深，并在 equal-leg 时等价于 Gaussian phase：

\[
X_0
\equiv
\pm \iota_k Y_0
\pmod{5^k},
\qquad
\iota_k^2\equiv-1\pmod{5^k}.
\]

由此解释：

- \(2\)：**Core-Forcing Prime**；
- \(5\)：**Phase-Escape Prime**。

---

# 6. R16：Source–Cut Defect Fingerprint 与 Cut-Index Discriminant

## 6.1 Source–Cut defect

定义：

\[
\boxed{
\mathscr C
:=
N-b_1^2P^2.
}
\]

若 genuine cut：

\[
P=10^na_1+a_2,
\]

则：

\[
\boxed{
\mathscr C
=
a_1
\left[
b_2^2a_1
-b_1^210^{2n}a_1
-2b_1^210^na_2
\right].
}
\]

---

## 6.2 Cut-Defect Orientation Law

对 \(p=2,5\)，定义：

\[
\ell_{1,p}:=v_p(a_1b_2),
\]

\[
\ell_{2,p}:=v_p(a_2b_1),
\]

\[
\nu_p:=v_p(N),
\qquad
d_p:=v_p(\mathscr C).
\]

则：

\[
\boxed{
d_p=
\begin{cases}
\nu_p,&\ell_{1,p}<\ell_{2,p},\\
\nu_p-\lambda_p,&\ell_{1,p}=\ell_{2,p},\\
>\nu_p,&\ell_{1,p}>\ell_{2,p}.
\end{cases}
}
\]

特别 \(p=2\)：

\[
\boxed{
\nu_2\text{ odd}
\Longrightarrow
d_2=\nu_2-1,
}
\]

\[
\boxed{
\nu_2\text{ even}
\Longrightarrow
d_2\ge\nu_2.
}
\]

这给出 source-only cheap cut gate。

---

## 6.3 positive defect gap support synchronization

定义：

\[
\Gamma_p:=\nu_p-d_p.
\]

若：

\[
\Gamma_p>0,
\]

则 equal weighted-leg valuation 强迫：

\[
\boxed{
v_p(b_1)=v_p(b_2),
}
\]

\[
\boxed{
v_p(a_1)=v_p(a_2).
}
\]

并有：

\[
\boxed{
v_p(P)
=
\frac{d_p}{2}-v_p(b_1).
}
\]

---

## 6.4 Cut-Index Discriminant

固定 cut depth \(n\)，写：

\[
P=10^nq+r.
\]

actual norm：

\[
N=b_2^2q^2+b_1^2r^2.
\]

消去 \(r\) 得：

\[
\boxed{
(b_2^2+b_1^210^{2n})q^2
-
2b_1^2P10^nq
+
(b_1^2P^2-N)=0.
}
\]

其四分之一判别式：

\[
\boxed{
\Delta_n
=
(b_2^2+b_1^210^{2n})N
-
b_1^2b_2^2P^2.
}
\]

亦即：

\[
\boxed{
\Delta_n
=
b_1^2N10^{2n}
+
b_2^2\mathscr C.
}
\]

genuine cut 时：

\[
\boxed{
\Delta_n
=
(b_2^2a_1-b_1^210^na_2)^2.
}
\]

于是最后 prefix realization 被压成单一 cut-index square condition。

---

## 6.5 SCDF 不是统一 closure

虽然它可以更早杀掉部分 formal survivor，但后续 falsification audit 表明：

\[
\boxed{
\text{SCDF alone cannot kill all three W0 branches.}
}
\]

**状态：RETIRED AS SOLE KILLER**

---

# 7. R17：Prefix-Defect Lock 与 Source-Seam Fixed Point

## 7.1 fixed \(P\) 后没有连续 fibre

必须校准：

固定 \(P\) 与 cut depth \(n\) 后：

\[
\boxed{
a_1=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
a_2=P\bmod10^n.
}
\]

所以真正 residual freedom 是离散的 cut index \(n\)，不是连续一维 progression。

---

## 7.2 Prefix-Defect Divisor Identity

记：

\[
q_n:=\left\lfloor\frac P{10^n}\right\rfloor,
\qquad
r_n:=P\bmod10^n.
\]

genuine cut 要求：

\[
N=b_2^2q_n^2+b_1^2r_n^2.
\]

由 \(\mathscr C=N-b_1^2P^2\) 得：

\[
\boxed{
b_2^2q_n^2-\mathscr C
=
b_1^2q_n10^n(P+r_n).
}
\]

所以：

\[
\boxed{
\mathscr C
\equiv
(b_2q_n)^2
\pmod{b_1^2q_n10^n}.
}
\]

以及：

\[
\boxed{q_n\mid\mathscr C.}
\]

---

## 7.3 ghost suffix

定义：

\[
\boxed{
R_n
:=
\frac{
b_2^2q_n^2-\mathscr C
}{
b_1^2q_n10^n
}.
}
\]

若 genuine：

\[
R_n=P+r_n.
\]

于是 source 预测 ghost suffix：

\[
\boxed{
\widehat r_n:=R_n-P.
}
\]

而 actual suffix：

\[
r_n=P\bmod10^n.
\]

所以：

\[
\boxed{
\widehat r_n=r_n
}
\]

是最终 seam fixed point。

---

## 7.4 seam residual

定义：

\[
\boxed{
\varepsilon_n
:=
\widehat r_n-r_n.
}
\]

则：

\[
\boxed{
\varepsilon_n
=
\frac{
F_n-N
}{
b_1^2q_n10^n
},
}
\]

其中：

\[
F_n:=b_2^2q_n^2+b_1^2r_n^2.
\]

因此：

\[
\boxed{
\varepsilon_n=0
\iff
F_n=N.
}
\]

---

## 7.5 与 carrier mismatch 的同一性

设：

\[
\mathcal W
=
\frac{\alpha}{\beta_{\rm full}},
\]

actual cut radius：

\[
\mathcal R_{\rm act}^2
=
\frac{F_n}{G^2}
+
\left(\frac{a_3}{b_3}\right)^2.
\]

source sphere：

\[
\frac N{G^2}
=
\mathcal W^2
-
\left(\frac{a_3}{b_3}\right)^2.
\]

于是：

\[
N-F_n
=
G^2
(\mathcal W^2-\mathcal R_{\rm act}^2).
\]

故：

\[
\boxed{
\varepsilon_n
=
-
\frac{b_2^2}{q_n10^n}
(\mathcal W-\mathcal R_{\rm act})
(\mathcal W+\mathcal R_{\rm act}).
}
\]

所以 seam residual 与 DD carrier mismatch 是同一个标量误差。

---

## 7.6 Carrier Overshoot conjecture 未成 theorem

有限 slab 中大量 surviving formal rows 都出现：

\[
\varepsilon_n<0,
\]

提示：

\[
\mathcal W>\mathcal R_{\rm act}
\]

可能是共同方向。

但这只是 finite diagnostic，不能升级为 theorem。

**状态：OPEN / later refined**

---

# 8. R18：Dual Defect Lock 与 Three-Factor Matching

## 8.1 Three-Factor Matching Law

定义 source alignment：

\[
R_s:=v/u,
\]

\[
\beta_s:=B_\kappa/A_\kappa.
\]

旧 DD near-square：

\[
\rho_s
=
\frac{4\beta_sR_s}{(R_s+\beta_s)^2}.
\]

定义 actual-cut alignment：

\[
H_n:=b_1^210^{2n_2}+b_2^2,
\]

\[
\chi_n^2
:=
\frac{(GP)^2}{H_nF_n}.
\]

Lagrange identity：

\[
H_nF_n-(GP)^2
=
(b_1^210^{n_2}a_2-b_2^2a_1)^2.
\]

再定义 denominator scale：

\[
\Omega_n
:=
\frac{Q^2\beta_s}{10^{2d_3}H_n}.
\]

则：

\[
\boxed{
\frac N{F_n}
=
\frac{\rho_s\chi_n^2}{\Omega_n}.
}
\]

所以：

\[
\boxed{
N=F_n
\iff
\rho_s\chi_n^2=\Omega_n.
}
\]

由此证明：

\[
\boxed{
\text{carrier dominance alone cannot determine sign}(F_n-N).
}
\]

**状态：RAW CARRIER SIGN CLOSURE RETIRED**

---

## 8.2 Alignment Dichotomy

将：

\[
z:=\frac{b_2}{b_1 10^{m_2}}
\in(0,1)
\]

代入，可得：

\[
\Omega_n
<
\frac{52}{11}
10^{-2(d_3+s_2)}.
\]

若 genuine：

\[
\rho_s\chi_n^2=\Omega_n.
\]

于是：

\[
\boxed{
\min(\rho_s,\chi_n^2)
<
2.175\ldots\times10^{-(d_3+s_2)}.
}
\]

这是 branch-free alignment degeneration theorem。

---

## 8.3 Dual defect

除左 defect：

\[
\mathscr C_L:=N-b_1^2P^2
\]

外，定义右 defect：

\[
\boxed{
\mathscr C_R
:=
10^{2n_2}N-b_2^2P^2.
}
\]

genuine cut 时：

\[
\boxed{
a_1\mid\mathscr C_L,
\qquad
a_2\mid\mathscr C_R.
}
\]

并可从 source 两侧分别预测 ghost suffix / prefix：

\[
\widehat a_2-a_2
=
\frac{F-N}{b_1^2a_1 10^{n_2}},
\]

\[
\widehat a_1-a_1
=
\frac{10^{n_2}(F-N)}{b_2^2a_2}.
\]

二者同号，且：

\[
\boxed{
\frac{\widehat a_1-a_1}
{\widehat a_2-a_2}
=
\frac{b_1^2a_1 10^{2n_2}}
{b_2^2a_2}.
}
\]

---

## 8.4 Dual-Ghost Escape Theorem

若：

- 两侧 ghost 均为整数；
- 两侧均落在正确 digit cell；
- 但 \(F\ne N\)；

则：

\[
\boxed{
b_1^210^{n_2}<9b_2^2.
}
\]

即：

\[
\boxed{
\frac{b_2}{b_1}
>
\frac{10^{n_2/2}}3.
}
\]

从 digit lengths 得：

\[
\boxed{
n_2+2m_1-2m_2\le2.
}
\]

等价：

\[
\boxed{
2m_1-m_2+s_2\le2.
}
\]

这给出 source–cut pseudo-survivor 必须进入强 denominator asymmetry 的现代来源。

---

# 9. R19：Coupled Square Elimination 与 Denominator Gaussian Norm Gate

## 9.1 actual-cut square

actual cut 产生：

\[
\boxed{
Y_c^2
=
(b_1^210^{2n_2}+b_2^2)N-G^2P^2.
}
\]

---

## 9.2 source PTS square

已有：

\[
\boxed{
Y_s^2
=
G^2P^2 10^{2n_3}
-
TQ(TQ+2b_3)N.
}
\]

---

## 9.3 联立消元 numerator

将 cut square 乘 \(10^{2n_3}\) 后与 PTS 相加，消去 \(P\)：

\[
\boxed{
Y_s^2+10^{2n_3}Y_c^2
=
\mathfrak K N,
}
\]

其中：

\[
\boxed{
\mathfrak K
=
10^{2n_3}
(b_1^210^{2n_2}+b_2^2)
-
TQ(TQ+2b_3).
}
\]

因为左边是两平方和，且 \(N\) 自身是两平方和，所以：

\[
\boxed{
\mathfrak K
\text{ 必须是两平方和整数。}
}
\]

亦即对所有：

\[
p\equiv3\pmod4,
\]

\[
\boxed{
v_p(\mathfrak K)\equiv0\pmod2.
}
\]

---

## 9.4 Denominator Gram Defect

定义：

\[
\mathbf d
=
(
b_1 10^{n_2+n_3},
b_2 10^{n_3},
b_3
),
\]

完整 denominator：

\[
\beta
=
b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3.
\]

则：

\[
\boxed{
\mathfrak K
=
\|\mathbf d\|^2-\beta^2.
}
\]

所以 \(\mathfrak K\) 是纯 denominator Gram defect。

---

## 9.5 Full-Tail Gaussian decontenting

因为：

\[
n_3=m_3+d_3,
\]

可提取：

\[
\mathfrak K=T\mathfrak K_0,
\]

再用：

\[
T=\omega L,
\qquad
b_3=\omega\tau,
\]

得到：

\[
\boxed{
\mathfrak K=T\omega\mathfrak G,
}
\]

其中：

\[
\boxed{
\mathfrak G
=
L(10^{2d_3}H_n-Q^2)-2Q\tau.
}
\]

因为 \(T\omega\) 只含 \(2,5\)，自身是 Gaussian norm，所以：

\[
\boxed{
\mathfrak G
\text{ 必须也是两平方和。}
}
\]

---

## 9.6 source-exclusive inert prime exclusion

若：

\[
p\equiv3\pmod4
\]

只落在 \(\kappa\) 与 \(\kappa+2G\) 之一中，则可证明：

\[
\boxed{p\nmid\mathfrak G.}
\]

所以 source-exclusive inert prime 不能进入 decontented kernel。

---

## 9.7 universal \(3\)-adic Gram gate

因为：

\[
10^r\equiv1\pmod9,
\]

有：

\[
\mathfrak K
\equiv
-2[
b_1b_2+b_3(b_1+b_2)
]
\pmod9.
\]

若：

\[
b_1b_2+b_3(b_1+b_2)
\equiv3,6\pmod9,
\]

则：

\[
v_3(\mathfrak K)=1,
\]

违背 Gaussian norm。

因此：

\[
\boxed{
b_1b_2+b_3(b_1+b_2)
\not\equiv3,6\pmod9.
}
\]

---

## 9.8 Odd-Inert Gram Excess 不是统一 killer

存在严格 denominator/source-normalized W0 formal state，使：

\[
\mathfrak G
\]

本身确实是 Gaussian norm。

所以不能证明：

\[
\text{every W0 source state}
\Rightarrow
\exists p\equiv3(4)
\text{ odd valuation in }\mathfrak G.
\]

**状态：RETIRED AS SOLE KILLER**

---

# 10. R20：Residual-Tail Exact Quotient 与 \(D\)-Split Firewall

这是本十轮最重要的一轮。

## 10.1 Residual-Tail Exact Quotient Normal Form

仍有：

\[
T=\omega L,
\qquad
b_3=\omega\tau,
\qquad
\gcd(L,\tau)=1.
\]

source identity：

\[
TQD=A_\kappa b_3
\]

变成：

\[
LQD=A_\kappa\tau.
\]

由 \(\gcd(L,\tau)=1\)：

\[
L\mid A_\kappa.
\]

写：

\[
\boxed{
A_\kappa=LA_0.
}
\]

则：

\[
QD=A_0\tau.
\]

又因为：

\[
\gcd(A_0,D)=1,
\]

存在唯一正整数 \(q_0\)：

\[
\boxed{
Q=A_0q_0,
}
\]

\[
\boxed{
\tau=Dq_0.
}
\]

于是：

\[
\boxed{
c=\omega q_0,
}
\]

\[
\boxed{
b_3=\omega Dq_0.
}
\]

source labels：

\[
\boxed{
\kappa=hLA_0,
}
\]

\[
\boxed{
G=hD,
}
\]

\[
\boxed{
B_\kappa=LA_0+2D.
}
\]

并且：

\[
\boxed{
\gcd(L,Dq_0)=1,
}
\]

\[
\boxed{
\gcd(A_0,D)=1,
}
\]

\[
\boxed{
Dq_0=\tau<L.
}
\]

这是一套比早先 RTNT 更精确的 exact quotient structure。

---

## 10.2 Primitive Gap Quantum Sharpening

定义：

\[
\boxed{
M:=LA_0+D.
}
\]

则：

\[
\boxed{
\gcd(M,LA_0D)=1.
}
\]

由 exact factor sum + source difference 可得：

\[
Mu+hLA_0a_3
=
hDP\omega L10^{d_3}.
\]

因为：

\[
\gcd(M,L)=1,
\]

再次得到：

\[
L\mid u.
\]

写：

\[
u=LU.
\]

则：

\[
\boxed{
MU
=
h(
\omega D10^{d_3}P-A_0a_3
).
}
\]

定义：

\[
\Xi
:=
\omega D10^{d_3}P-A_0a_3>0,
\]

\[
\gamma:=\gcd(h,M).
\]

于是：

\[
\boxed{
\Xi=\frac M\gamma j,
\qquad
j\in\mathbb Z_{>0}.
}
\]

故：

\[
\boxed{
u=L\frac h\gamma j,
}
\]

\[
\boxed{
v=\frac h\gamma
(Lj+2\gamma a_3).
}
\]

并得到 sharpened carrier gap：

\[
\boxed{
\mathcal W-r_3
=
\frac{Lj}{\gamma b_3}.
}
\]

> **校准**：此前用 \(\gcd(h,LQ+\tau)\) 写出的 quantum 不是最 primitive 的版本，因为 \(LQ+\tau=q_0M\) 仍带可约掉的 \(q_0\)。R20 的 \(M,\gamma\) 版本应取代旧版本。

---

## 10.3 \(D\)-Prime Equal-Load Firewall

取任意：

\[
p\mid D.
\]

由：

\[
\gcd(M,LA_0D)=1
\]

有：

\[
p\nmid M,\ L,\ A_0,\ \gamma.
\]

又：

\[
p\mid D\mid b_3,
\]

primitive 给：

\[
p\nmid a_3.
\]

模 \(p\) 看：

\[
\Xi
=
\omega D10^{d_3}P-A_0a_3
\equiv
-A_0a_3
\not\equiv0.
\]

因此：

\[
\boxed{p\nmid j.}
\]

又：

\[
\frac M\gamma j
\equiv
-A_0a_3
\pmod p.
\]

因为：

\[
M\equiv LA_0\pmod p,
\]

所以：

\[
\boxed{
Lj\equiv-\gamma a_3\pmod p.
}
\]

进而：

\[
Lj+2\gamma a_3
\equiv
\gamma a_3
\not\equiv0
\pmod p.
\]

由 \(u,v\) 的 exact formula：

\[
\boxed{
v_p(u)=v_p(v)=v_p(h)
\qquad(p\mid D).
}
\]

这是：

\[
\boxed{\textbf{\(D\)-Prime Equal-Load Firewall}.}
\]

---

## 10.4 \(D\)-Prime Norm Load

由：

\[
uv=Nc^2,
\]

得到：

\[
\boxed{
v_p(N)
=
2(v_p(h)-v_p(c))
\qquad(p\mid D).
}
\]

于是：

\[
\boxed{
v_p(c)\le v_p(h).
}
\]

注意这是 exact equality，不是 lower bound。

---

## 10.5 排除所有 odd inert primes from \(D\)

假设：

\[
p\mid D,
\qquad
p\equiv3\pmod4.
\]

记：

\[
e_i:=v_p(b_i),
\]

\[
H:=v_p(h),
\]

\[
d:=v_p(D)>0,
\]

\[
C:=v_p(c).
\]

则：

\[
e_1+e_2=H+d,
\]

\[
e_3:=v_p(b_3)=C+d.
\]

actual norm：

\[
N=(a_1b_2)^2+(a_2b_1)^2.
\]

因为 \(-1\) 在 \(p\equiv3\pmod4\) 下非二次剩余：

\[
\boxed{
v_p(N)
=
2\min(e_1,e_2).
}
\]

与 \(D\)-Prime Norm Load 比较：

\[
2\min(e_1,e_2)
=
2(H-C).
\]

所以：

\[
\min(e_1,e_2)=H-C.
\]

而：

\[
e_1+e_2=H+d.
\]

得到：

\[
\boxed{
\max(e_1,e_2)=d+C=e_3.
}
\]

即：

\[
\boxed{
v_p(b_3)
=
\max(v_p(b_1),v_p(b_2)).
}
\]

若 \(e_1\ne e_2\)，则最大值由 \(b_3\) 与 \(b_1,b_2\) 中较大者恰好两块取得，形成 pair-max，与此前 denominator prime graph 对 \(p\equiv3\pmod4\) 的禁令冲突。

若：

\[
e_1=e_2=e_3,
\]

则会推出：

\[
v_p(D)=0,
\]

同样矛盾。

因此：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
p\nmid D.
}
\]

---

## 10.6 排除 \(2\mid D\)

假设：

\[
2\mid D.
\]

由 equal-load：

\[
v_2(N)
=
2(v_2(h)-v_2(c)),
\]

所以 \(v_2(N)\) 为偶数。

结合此前 denominator prime graph 已知：

\[
\max_i v_2(b_i)
\]

必须 unique-max。

逐分情况可得：

- 若 \(e_1=e_2>0\)，则 \(v_2(N)=2e+1\) 为奇数，矛盾；
- 若 \(e_1\ne e_2\)，equal-load 强迫 \(e_3=\max(e_1,e_2)\)，产生 pair-max，违背 unique-max；
- 若仅一个 prefix denominator 含 \(2\)，同样得到 prefix 最大值与 \(b_3\) tie。

所以：

\[
\boxed{2\nmid D.}
\]

---

## 10.7 \(D\)-Split Firewall

综合：

\[
2\nmid D
\]

及：

\[
p\equiv3\pmod4
\Longrightarrow
p\nmid D,
\]

得到：

\[
\boxed{
p\mid D
\Longrightarrow
p\equiv1\pmod4.
}
\]

因此：

\[
\boxed{
D\text{ 的全部素因子都是 Gaussian split primes}.
}
\]

特别：

\[
\boxed{
D\text{ odd},
\qquad
D\equiv1\pmod4.
}
\]

并且：

\[
D\in\operatorname{Norm}_{\mathbb Z[i]/\mathbb Z}.
\]

但比“\(D\) 是两平方和”更强，因为 \(D\) 完全没有 \(2\) 与 inert prime。

**状态：PROVED**

---

## 10.8 \(h\) = Gaussian non-split absorber

因为：

\[
G=hD
\]

而 \(D\) 不含 \(2\) 与任何 \(3\bmod4\) prime，所以：

\[
\boxed{
v_2(h)=v_2(G),
}
\]

以及：

\[
\boxed{
v_p(h)=v_p(G)
\qquad
(p\equiv3\pmod4).
}
\]

所以：

\[
\boxed{
\textbf{前两 denominator 中所有 Gaussian non-split support 全部被 \(h\) 吸收。}
}
\]

这是对 \(h=\gcd(\kappa,G)\) 的新结构解释。

---

## 10.9 \(A_0\)-inert localization

若：

\[
p\equiv3\pmod4,
\qquad
p\mid A_0,
\]

则可证明：

\[
\boxed{
v_p(b_1)=v_p(b_2)\le v_p(b_3).
}
\]

而：

\[
\boxed{
v_p(A_0)
=
v_p(Q)-v_p(b_3).
}
\]

所以 \(A_0\) 中的 inert support 精确测量：

> first-two denominator concatenation \(Q\) 超过第三 denominator inert-depth 的额外 cancellation。

这把 residual non-split freedom 压到了一个非常窄的地方。

---

# 11. 十轮累计证明链

将 R11–R20 的真正 theorem 压缩后，主链如下。

## 11.1 Tail load chain

\[
T=\omega L,
\qquad
b_3=\omega\tau
\]

\[
\Downarrow
\]

\[
L\mid A_\kappa,
\qquad
L\mid u
\]

\[
\Downarrow
\]

\[
L\mid Nc^2
\]

\[
\Downarrow
\]

\[
v_5(N)\ge(m_3-3v_5(b_3))_+
\]

\[
v_2(N)\ge(m_3+1-3v_2(b_3))_+.
\]

---

## 11.2 Cut-loaded \(2\)-adic chain

\[
\delta_2>0
\]

\[
\Downarrow
\]

\[
b_1,b_2\text{ both odd}
\]

\[
\Downarrow
\]

automatic source-factor resonance

\[
\Downarrow
\]

exact \(v_2(N)\)

\[
\Downarrow
\]

common numerator \(2\)-core.

但 normalized source equation 是 nonsingular Hensel，故：

\[
\boxed{
\text{deep \(2\)-adic local phase cannot be final killer}.
}
\]

---

## 11.3 Source–cut interface chain

source 同时恢复：

\[
(P,N)
\]

\[
\Downarrow
\]

\[
\mathscr C=N-b_1^2P^2
\]

\[
\Downarrow
\]

source–cut defect fingerprint

\[
\Downarrow
\]

prefix defect divisor lock

\[
\Downarrow
\]

dual defect lock

\[
\Downarrow
\]

ghost prefix / suffix fixed points.

但这些最终若 closure，只会回到：

\[
F_n=N.
\]

所以它们是强 prefilters / semantic interfaces，不是当前已证明的 universal extinction engine。

---

## 11.4 Coupled-square Gaussian chain

source PTS square + actual-cut square

\[
\Downarrow
\]

numerator elimination

\[
\Downarrow
\]

denominator Gram defect：

\[
\mathfrak K
=
\|\mathbf d\|^2-\beta^2
\]

必须是 Gaussian norm。

DD full-tail retention：

\[
\Downarrow
\]

\[
\mathfrak G
=
L(10^{2d_3}H_n-Q^2)-2Q\tau
\]

也必须是 Gaussian norm。

但 denominator-only W0 formal states 可以通过此 gate。

故：

\[
\boxed{
\text{odd-inert Gram excess cannot be sole universal killer}.
}
\]

---

## 11.5 最终上游 source chain

R20 exact quotient：

\[
A_\kappa=LA_0,
\]

\[
Q=A_0q_0,
\]

\[
\tau=Dq_0,
\]

\[
c=\omega q_0.
\]

再定义：

\[
M=LA_0+D,
\qquad
\gamma=\gcd(h,M).
\]

得到：

\[
u=L(h/\gamma)j,
\]

\[
v=(h/\gamma)(Lj+2\gamma a_3).
\]

于是对：

\[
p\mid D
\]

有：

\[
v_p(u)=v_p(v)=v_p(h),
\]

进而：

\[
v_p(N)=2(v_p(h)-v_p(c)).
\]

结合 actual norm 与 denominator prime graph：

\[
\boxed{
p\mid D
\Longrightarrow
p\equiv1\pmod4.
}
\]

这是目前 R11–R20 最强、最上游、最明显跨三个 W0 branch 的 theorem。

---

# 12. 已正式退休 / 校准的路线

以下路线在十轮内被明确 falsify、证明冗余或证明不可能单独 closure。

## 12.1 纯 Half-Tail \(2\)-adic killer

**RETIRED**

原因：normalized source quadratic 的导数为 \(2\)-adic unit，任意深 Hensel 自动存在。

---

## 12.2 deep \(5\)-adic source Hensel

**RETIRED**

原因：\(p=5\) 的 normalized source quadratic 同样 nonsingular。

---

## 12.3 surplus simplex + common \(2\)-core size

**FAILED BY SLOPE**

纯 valuation capacity slope 不足。

---

## 12.4 SCDF 作为统一 W0 killer

**RETIRED AS SOLE KILLER**

它是强 cheap gate，但存在 formal states 通过 SCDF 后仍死于 actual cut。

---

## 12.5 local \(2\times5\) CRT incompatibility

**RETIRED**

fixed word 与 \(5\)-Gaussian phase 横截，系数为 \(5\)-adic unit，每个 sign branch 都有唯一 local residue。

---

## 12.6 carrier dominance alone determines sign

**RETIRED**

Three-Factor Matching 证明 residual sign 同时依赖 source alignment、actual-cut alignment 与 denominator scale。

---

## 12.7 seam residual divisor overload as closure

**RETIRED**

若最终推出 \(F-N=0\)，那正是 genuine cut，不是 contradiction。

---

## 12.8 generic dual reciprocity as uniform killer

**RETIRED / NO NEGATIVE CHARACTER**

当前缺统一 nonresidue theorem。

---

## 12.9 odd-inert Gram excess as universal W0 killer

**RETIRED**

存在 denominator/source-normalized W0 formal state，其 \(\mathfrak G\) 本身就是 Gaussian norm。

---

## 12.10 carrier quantum 旧版本

早期用：

\[
\gcd(h,LQ+\tau)
\]

写出的 quantum **不是最 primitive 形式**。

R20 正确 sharpened 版本应使用：

\[
\boxed{
M=LA_0+D,
\qquad
\gamma=\gcd(h,M).
}
\]

---

# 13. 有限诊断：哪些结果不能进入 theorem dependency

R17–R18 曾使用有限 slab 做 architecture falsification / survivor profiling。

这些结果的正确地位：

\[
\boxed{\textbf{仅用于诊断，不可进入无界证明依赖。}}
\]

其中观察到：

- SCDF 大量保留 formal states；
- left PDDI 极强但仍留极少 pseudo-survivor；
- dual right defect 可以进一步杀掉 left-only pseudo-row；
- 某些 slab 中 residual \(\varepsilon_n\) 全为同号。

但：

\[
\boxed{
\text{任何 finite count、经验符号、有限 survivor 数都不是 theorem。}
}
\]

---

# 14. 当前最重要的结构解释

经过十轮，关于“为什么三个 W0 branch 应该有共同上游原因”，当前最有力的解释已经不是某个共同 \(2/5\)-adic congruence。

而是：

\[
\boxed{
\textbf{Residual-tail source integrality
先执行一次 Gaussian support purification，}
}
\]

具体：

\[
G=hD,
\]

其中：

\[
\boxed{
h
\text{ 吸收所有 }2\text{ 与 }p\equiv3\pmod4\text{ support},
}
\]

而：

\[
\boxed{
D
\text{ 只剩 }p\equiv1\pmod4\text{ split support}.
}
\]

所以 W0-A/B/C 后来围绕 \(5\) 分裂并非偶然：

\[
\boxed{
5\equiv1\pmod4
}
\]

是 decimal primes 中唯一能够继续留在 split cofactor / source allocation 中的 prime；

而 \(2\) 与所有 odd inert primes 在 branch split 之前已经被统一 source firewall 清洗掉。

这就是目前对三支共同结构最干净的解释。

---

# 15. 当前 frontier

仍未证明：

\[
\boxed{W0=\varnothing.}
\]

下一轮最自然的 frontier 已经非常窄：

\[
\boxed{
\textbf{\(A_0\)-Inert Deep Cancellation}
\times
\textbf{Actual Prefix Cut Phase}.
}
\]

已知若：

\[
p\equiv3\pmod4,
\qquad
p\mid A_0,
\]

则：

\[
\boxed{
v_p(b_1)=v_p(b_2)\le v_p(b_3),
}
\]

且：

\[
\boxed{
v_p(A_0)=v_p(Q)-v_p(b_3).
}
\]

所以 inert support 不再能进入 \(D\)，只能以：

\[
\boxed{
\text{first-two denominator concatenation \(Q\) 的额外 deep cancellation}
}
\]

形式留在 \(A_0\)。

下一步最值得证明的是：

> 若 \(p\equiv3\pmod4\) 深入 \(A_0\)，source factor allocation 是否进一步强迫 \(P\) 发生对应的 \(p\)-adic decimal cancellation？

若能得到：

\[
p^r\mid Q,
\qquad
p^r\mid P,
\]

则：

\[
P=a_1 10^{n_2}+a_2,
\qquad
Q=b_1 10^{m_2}+b_2
\]

会产生双 decimal phase，从而把：

\[
N=(a_1b_2)^2+(a_2b_1)^2
\]

直接压向：

\[
1+10^{2s_2}
\]

型 inert-prime obstruction。

当前这条是最自然的下一阶段攻击线。

---

# 16. 最终 Ledger

| 项目 | 状态 |
|---|---|
| Residual-Tail / Norm Transfer | **PROVED** |
| \(L\mid A_\kappa\) | **PROVED** |
| \(L\mid u\) | **PROVED** |
| \(\gcd(L,D)=1\) | **PROVED** |
| Decimal-Tail Deficit | **PROVED** |
| \(1/3\)-phase boundary | **PROVED** |
| Cut-Loaded Parity Collapse | **PROVED** |
| Automatic cut-loaded \(2\)-resonance | **PROVED** |
| Common Numerator \(2\)-Core | **PROVED** |
| Half-Tail Phase Law | **PROVED** |
| Pure Half-Tail Hensel killer | **RETIRED** |
| Two-Prime No-Hidden-Slack | **PROVED** |
| Deep source Hensel common obstruction | **RETIRED** |
| Norm-Load Decomposition | **PROVED** |
| Source–Cut Defect Fingerprint | **PROVED as gate** |
| SCDF as uniform killer | **RETIRED** |
| Cut-Index Discriminant | **PROVED** |
| Prefix-Defect Divisor Identity | **PROVED** |
| Ghost suffix fixed point | **PROVED / equivalent to norm realization** |
| Dual Defect Lock | **PROVED** |
| Dual-Ghost Escape Theorem | **PROVED** |
| Three-Factor Matching | **PROVED** |
| Raw carrier sign closure | **RETIRED** |
| Coupled source-cut square | **PROVED** |
| Denominator Gaussian Norm Gate | **PROVED necessary** |
| Full-Tail Gaussian Decontenting | **PROVED** |
| Universal odd-inert Gram excess | **RETIRED** |
| Residual-Tail Exact Quotient Normal Form | **PROVED** |
| Primitive Gap Quantum Sharpening | **PROVED** |
| \(D\)-Prime Equal-Load Firewall | **PROVED** |
| \(D\)-Prime Norm Load | **PROVED** |
| \(D\)-Split Firewall | **PROVED** |
| \(h\) as Gaussian non-split absorber | **PROVED** |
| \(A_0\)-Inert Localization | **PROVED** |
| W0-A/B/C simultaneous extinction | **OPEN** |

---

# 17. 一句话阶段结论

\[
\boxed{
\textbf{R11–R20 最大成果不是关闭 W0，}
}
\]

而是把“跨三个 W0 branch 的共同原因”从模糊的 source–cut mismatch 逐步压到：

\[
\boxed{
\textbf{Residual-tail exact quotient
\(\rightarrow\)
non-split support purification
\(\rightarrow\)
\(D\)-split firewall}.
}
\]

因此目前最可信的结构图景是：

\[
\boxed{
\textbf{W0-A/B/C 不是三个根本机制，}
}
\]

而是：

\[
\boxed{
\textbf{在 branch split 之前完成 Gaussian support purification 后，
仅剩 split prime \(5\) 的三种下游 allocation 状态。}
}
\]

后续真正需要攻击的，是被挤到 \(A_0\) 中的 inert deep cancellation 与 actual prefix decimal cut 之间的冲突，而不是重新分别研究 W0-A/B/C。
