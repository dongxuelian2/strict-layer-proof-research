# DD-SA 第二十轮归档  
## Residual-Tail Exact Quotient × Primitive Gap Quantum × \(D\)-Split Firewall

**项目：** 三项十进制拼接平方和问题  
**层级：** DD / W0 preterminal structural analysis  
**目标：** 寻找跨 \(W0\)-A / \(W0\)-B / \(W0\)-C 三个 branch 都成立的共同上游机制  
**本轮状态：** 取得新的 branch-free source firewall；尚未证明 \(W0=\varnothing\)

---

# 0. 本轮结论摘要

本轮从 canonical source system 出发，不使用 \(W0\)-A / \(W0\)-B / \(W0\)-C 的 branch 定义，得到一个新的完整 residual-tail quotient normal form：

\[
A_\kappa=LA_0,\qquad
Q=A_0q_0,\qquad
\tau=Dq_0,\qquad
c=\omega q_0,
\]

其中

\[
10^{m_3}=\omega L,\qquad
b_3=\omega\tau,\qquad
\gcd(L,\tau)=1,
\]

并且

\[
\gcd(A_0,D)=1,\qquad
\gcd(L,Dq_0)=1,\qquad
Dq_0<L.
\]

进一步定义

\[
M:=LA_0+D,\qquad
\gamma:=\gcd(h,M),
\]

可将 canonical source pair 精确写成

\[
u=L\frac h\gamma j,
\]

\[
v=\frac h\gamma(Lj+2\gamma a_3),
\]

其中 \(j\in\mathbb Z_{>0}\)。

从这个正规型得到本轮核心 firewall：

> 对任意素数 \(p\mid D\)，有
> \[
> v_p(u)=v_p(v)=v_p(h),
> \]
> 从而
> \[
> v_p(N)=2\bigl(v_p(h)-v_p(c)\bigr).
> \]

再与 actual weighted norm

\[
N=(a_1b_2)^2+(a_2b_1)^2
\]

以及 denominator prime graph 联立，得到：

\[
\boxed{
p\mid D\Longrightarrow p\equiv1\pmod4.
}
\]

因此：

\[
\boxed{
D\ \text{只含 Gaussian split primes}.
}
\]

特别地：

\[
2\nmid D,
\]

且所有

\[
p\equiv3\pmod4
\]

都不能整除 \(D\)。

于是 \(h=G/D\) 吸收了 prefix denominator 中全部 \(2\)-primary 与 Gaussian inert support：

\[
v_2(h)=v_2(G),
\]

以及

\[
v_p(h)=v_p(G)
\qquad
(p\equiv3\pmod4).
\]

这给出了一个跨三个 W0 branch 的共同上游机制：

\[
\boxed{
\text{Residual-Tail Exact Quotient}
+
\text{Primitive Equal-Load}
+
\text{Gaussian Split-Cofactor Firewall}.
}
\]

---

# 1. Canonical source system

沿用 DD canonical notation：

\[
T:=10^{m_3},
\]

\[
Q:=b_1 10^{m_2}+b_2,
\]

\[
G:=b_1b_2.
\]

定义：

\[
h:=\gcd(\kappa,G),
\]

\[
A_\kappa:=\frac{\kappa}{h},
\]

\[
D:=\frac Gh.
\]

因此：

\[
\gcd(A_\kappa,D)=1.
\]

第三 denominator 的 canonical factorization 为

\[
b_3=cD.
\]

source pair 满足：

\[
uv=Nc^2,
\]

\[
v-u=2ha_3,
\]

以及 exact factor sum

\[
B_\kappa u+A_\kappa v
=
2GP10^{n_3},
\]

其中

\[
B_\kappa=A_\kappa+2D.
\]

同时 individual reducedness 给：

\[
\gcd(a_3,b_3)=1.
\]

---

# 2. Residual tail decomposition

令

\[
\omega:=\gcd(T,b_3).
\]

写：

\[
T=\omega L,
\]

\[
b_3=\omega\tau,
\]

其中：

\[
\gcd(L,\tau)=1.
\]

由于

\[
0<b_3<T,
\]

故：

\[
0<\tau<L.
\]

canonical denominator relation：

\[
TQD=A_\kappa b_3
\]

变为：

\[
\omega LQD=A_\kappa\omega\tau,
\]

即：

\[
LQD=A_\kappa\tau.
\]

因为：

\[
\gcd(L,\tau)=1,
\]

得到：

\[
\boxed{L\mid A_\kappa.}
\]

于是写：

\[
\boxed{
A_\kappa=LA_0.
}
\]

代回：

\[
QD=A_0\tau.
\]

再由：

\[
\gcd(A_0,D)=1,
\]

存在唯一正整数 \(q_0\)，使：

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

因此：

\[
\boxed{
c=\omega q_0,
}
\]

以及：

\[
\boxed{
b_3=\omega Dq_0.
}
\]

又有：

\[
\boxed{
\kappa=hLA_0,
}
\]

\[
\boxed{
G=hD.
}
\]

所以：

\[
\boxed{
B_\kappa=LA_0+2D.
}
\]

此外：

\[
\gcd(L,\tau)=1
\]

变为：

\[
\boxed{
\gcd(L,Dq_0)=1.
}
\]

而 \(\tau<L\) 给：

\[
\boxed{
Dq_0<L.
}
\]

于是得到：

## Theorem 2.1 — Residual-Tail Exact Quotient Normal Form

\[
\boxed{
A_\kappa=LA_0,\quad
Q=A_0q_0,\quad
\tau=Dq_0,\quad
c=\omega q_0,
}
\]

并且：

\[
\boxed{
\gcd(A_0,D)=1,\quad
\gcd(L,Dq_0)=1,\quad
Dq_0<L.
}
\]

**Status: PROVED**

---

# 3. Primitive gap quantum 的 sharpened normal form

定义：

\[
\boxed{
M:=LA_0+D.
}
\]

因为：

\[
\gcd(A_0,D)=1,
\]

以及：

\[
\gcd(L,D)=1,
\]

可得：

\[
\boxed{
\gcd(M,LA_0D)=1.
}
\]

现在使用：

\[
B_\kappa u+A_\kappa v
=
2GP10^{n_3},
\]

和：

\[
v-u=2ha_3.
\]

将：

\[
v=u+2ha_3
\]

代入：

\[
(LA_0+2D)u+LA_0(u+2ha_3)
=
2hDP10^{n_3}.
\]

除以 \(2\)：

\[
(LA_0+D)u+hLA_0a_3
=
hDP10^{n_3}.
\]

即：

\[
Mu+hLA_0a_3
=
hDP10^{n_3}.
\]

利用：

\[
n_3=m_3+d_3,
\]

以及：

\[
10^{m_3}=T=\omega L,
\]

得：

\[
Mu+hLA_0a_3
=
hD P\,\omega L10^{d_3}.
\]

因为：

\[
\gcd(M,L)=1,
\]

右侧与第二项都被 \(L\) 整除，所以：

\[
\boxed{
L\mid u.
}
\]

写：

\[
u=LU.
\]

则：

\[
MU+hA_0a_3
=
h\omega D10^{d_3}P.
\]

故：

\[
\boxed{
MU
=
h\left(
\omega D10^{d_3}P-A_0a_3
\right).
}
\]

定义：

\[
\boxed{
\Xi
:=
\omega D10^{d_3}P-A_0a_3.
}
\]

DD orientation 给：

\[
\Xi>0.
\]

再定义：

\[
\boxed{
\gamma:=\gcd(h,M).
}
\]

由于：

\[
M/\gamma
\]

与：

\[
h/\gamma
\]

互素，从

\[
MU=h\Xi
\]

得到：

\[
\frac M\gamma\mid\Xi.
\]

因此存在：

\[
j\in\mathbb Z_{>0}
\]

使：

\[
\boxed{
\Xi=\frac M\gamma j.
}
\]

于是：

\[
U=\frac h\gamma j,
\]

故：

\[
\boxed{
u=L\frac h\gamma j.
}
\]

由：

\[
v-u=2ha_3
\]

得到：

\[
\boxed{
v=
\frac h\gamma
\left(
Lj+2\gamma a_3
\right).
}
\]

因此：

## Theorem 3.1 — Primitive Gap Quantum

存在 \(j\in\mathbb Z_{>0}\) 使：

\[
\boxed{
u=L(h/\gamma)j,
}
\]

\[
\boxed{
v=(h/\gamma)(Lj+2\gamma a_3).
}
\]

其中：

\[
\boxed{
\gamma=\gcd(h,LA_0+D).
}
\]

**Status: PROVED**

---

# 4. 对此前 carrier quantum 的校准

此前曾使用基于：

\[
\gcd(h,LQ+\tau)
\]

的 gap quantum。

但现在：

\[
Q=A_0q_0,
\qquad
\tau=Dq_0,
\]

所以：

\[
LQ+\tau
=
q_0(LA_0+D)
=
q_0M.
\]

而 source numerator 中本身也含相同的 \(q_0\)，因此应先消去该公共因子。

真正 primitive modulus 是：

\[
\boxed{
M=LA_0+D,
}
\]

而非：

\[
LQ+\tau.
\]

所以旧版本应视为 **nonprimitive form**，本轮已 sharpen。

---

# 5. Sharpened Quantized Carrier Compensation

设完整 ratio：

\[
\mathcal W
\]

及第三 ratio：

\[
r_3=\frac{a_3}{b_3}.
\]

canonical relation：

\[
u=hb_3(\mathcal W-r_3).
\]

代入：

\[
u=L\frac h\gamma j,
\]

得到：

\[
hb_3(\mathcal W-r_3)
=
L\frac h\gamma j.
\]

消去 \(h\)：

\[
\boxed{
\mathcal W-r_3
=
\frac{Lj}{\gamma b_3}.
}
\]

因此：

\[
\boxed{
\mathcal W-r_3
\in
\frac{L}{\gamma b_3}\mathbb Z_{>0}.
}
\]

这是 sharpened source gap lattice。

**Status: PROVED**

---

# 6. \(D\)-prime 的 primitive firewall

现在固定任意素数：

\[
p\mid D.
\]

因为：

\[
\gcd(L,D)=1,
\]

\[
\gcd(A_0,D)=1,
\]

以及：

\[
M=LA_0+D,
\]

可知：

\[
p\nmid L,
\]

\[
p\nmid A_0,
\]

\[
p\nmid M.
\]

因此：

\[
p\nmid\gamma.
\]

另一方面：

\[
p\mid D\mid b_3.
\]

由 individual reducedness：

\[
\gcd(a_3,b_3)=1,
\]

所以：

\[
\boxed{
p\nmid a_3.
}
\]

看：

\[
\Xi
=
\omega D10^{d_3}P-A_0a_3.
\]

模 \(p\)：

\[
\Xi
\equiv
-A_0a_3
\not\equiv0
\pmod p.
\]

由：

\[
\Xi=\frac M\gamma j,
\]

且：

\[
p\nmid M/\gamma,
\]

得到：

\[
\boxed{
p\nmid j.
}
\]

同时：

\[
\frac M\gamma j
\equiv
-A_0a_3
\pmod p.
\]

因：

\[
M\equiv LA_0\pmod p,
\]

可消去 \(A_0\)，得到：

\[
\boxed{
Lj\equiv-\gamma a_3
\pmod p.
}
\]

于是：

\[
Lj+2\gamma a_3
\equiv
\gamma a_3
\not\equiv0
\pmod p.
\]

由：

\[
u=L(h/\gamma)j,
\]

\[
v=(h/\gamma)(Lj+2\gamma a_3),
\]

得到：

\[
\boxed{
v_p(u)=v_p(h),
}
\]

\[
\boxed{
v_p(v)=v_p(h).
}
\]

故：

## Theorem 6.1 — \(D\)-Prime Equal-Load Firewall

对每个：

\[
p\mid D,
\]

均有：

\[
\boxed{
v_p(u)=v_p(v)=v_p(h).
}
\]

**Status: PROVED**

---

# 7. \(D\)-prime norm load 精确公式

由：

\[
uv=Nc^2,
\]

取 \(p\)-adic valuation：

\[
v_p(u)+v_p(v)
=
v_p(N)+2v_p(c).
\]

而 Theorem 6.1 给：

\[
v_p(u)+v_p(v)
=
2v_p(h).
\]

所以：

\[
\boxed{
v_p(N)
=
2\bigl(v_p(h)-v_p(c)\bigr)
\qquad(p\mid D).
}
\]

特别：

\[
\boxed{
v_p(c)\le v_p(h).
}
\]

这是 exact equality，不是 bound。

## Theorem 7.1 — \(D\)-Prime Norm Load

\[
\boxed{
p\mid D
\Longrightarrow
v_p(N)=2(v_p(h)-v_p(c)).
}
\]

**Status: PROVED**

---

# 8. 排除所有 odd inert primes from \(D\)

设：

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

因为：

\[
G=hD=b_1b_2,
\]

有：

\[
e_1+e_2=H+d.
\]

又：

\[
b_3=cD,
\]

所以：

\[
e_3:=v_p(b_3)=C+d.
\]

actual weighted norm：

\[
N=(a_1b_2)^2+(a_2b_1)^2.
\]

对：

\[
p\equiv3\pmod4,
\]

\(-1\) 为 quadratic nonresidue。

结合 individual reducedness，可得：

\[
\boxed{
v_p(N)=2\min(e_1,e_2).
}
\]

而 Theorem 7.1 给：

\[
v_p(N)=2(H-C).
\]

因此：

\[
\min(e_1,e_2)=H-C.
\]

由：

\[
e_1+e_2=H+d,
\]

得到：

\[
\max(e_1,e_2)
=
d+C
=
e_3.
\]

即：

\[
\boxed{
e_3=\max(e_1,e_2).
}
\]

---

## 8.1 非对角情形 \(e_1\ne e_2\)

此时最大 valuation 由：

- \(b_3\)
- \(b_1,b_2\) 中较大的一个

恰好两块取得。

即 pair-max。

而 denominator prime graph 已证明：

\[
p\equiv3\pmod4
\]

不允许 exactly-two max。

矛盾。

---

## 8.2 对角情形 \(e_1=e_2\)

此时：

\[
e_1=e_2=e_3=:E.
\]

于是：

\[
v_p(Q)\ge E.
\]

又因为 \(p\ne2,5\)：

\[
v_p(\kappa)
=
v_p(Q)+2E-E
\ge2E.
\]

同时：

\[
v_p(G)=2E.
\]

因此：

\[
v_p(h)=2E.
\]

于是：

\[
v_p(D)
=
v_p(G)-v_p(h)
=
0.
\]

与：

\[
p\mid D
\]

矛盾。

故：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
p\nmid D.
}
\]

**Status: PROVED**

---

# 9. 排除 \(2\) from \(D\)

假设：

\[
2\mid D.
\]

由 Theorem 7.1：

\[
v_2(N)=2(H-C),
\]

所以：

\[
\boxed{
v_2(N)\ \text{为偶数}.
}
\]

denominator prime graph 对 \(p=2\) 已给：

\[
\boxed{
\max_i v_2(b_i)
\text{ 必须唯一取得}.
}
\]

下面分情况。

---

## 9.1 \(e_1,e_2>0\)

reducedness 给：

\[
a_1,a_2\text{ 都奇}.
\]

若：

\[
e_1=e_2=e,
\]

则：

\[
v_2(N)=2e+1,
\]

为奇数。

与 DLOAD 的偶性矛盾。

所以：

\[
e_1\ne e_2.
\]

此时：

\[
v_2(N)=2\min(e_1,e_2).
\]

与 odd-inert case 相同，推出：

\[
e_3=\max(e_1,e_2).
\]

于是最大值由两块同时取得，违反 \(2\)-adic unique-max。

---

## 9.2 恰有一个 \(e_i>0\)

例如：

\[
e_1>0,\qquad e_2=0.
\]

由 reducedness：

\[
a_1\text{ odd}.
\]

所以：

\[
a_1b_2
\]

为奇数，因此：

\[
v_2(N)=0.
\]

DLOAD 给：

\[
H=C.
\]

而：

\[
e_1=H+d,
\]

\[
e_3=C+d.
\]

所以：

\[
e_1=e_3.
\]

又形成 pair-max，违反 unique-max。

故：

\[
\boxed{2\nmid D.}
\]

**Status: PROVED**

---

# 10. \(D\)-Split Firewall

综合 Sections 8–9：

\[
2\nmid D,
\]

且：

\[
p\equiv3\pmod4
\Longrightarrow
p\nmid D.
\]

因此：

\[
\boxed{
p\mid D
\Longrightarrow
p\equiv1\pmod4.
}
\]

于是：

\[
\boxed{
D\text{ 的所有素因子均为 Gaussian split primes}.
}
\]

特别：

\[
\boxed{
D\text{ odd},
}
\]

\[
\boxed{
D\equiv1\pmod4.
}
\]

而且：

\[
\boxed{
D\in\operatorname{Norm}_{\mathbb Z[i]/\mathbb Z}.
}
\]

但这里比普通 sum-of-two-squares 更强，因为 \(D\) 根本没有：

- \(2\)
- 任意 \(3\bmod4\) prime

的 support。

## Theorem 10.1 — \(D\)-Split Firewall

\[
\boxed{
p\mid D
\Rightarrow
p\equiv1\pmod4.
}
\]

**Status: PROVED**

---

# 11. \(h\) 的结构解释：Gaussian Non-Split Absorber

由于：

\[
G=hD,
\]

而 \(D\) 不含 \(2\) 与任意 \(3\bmod4\) prime，因此：

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

即：

\[
\boxed{
\text{prefix denominator 中所有 Gaussian non-split support 均被 }h\text{ 完全吸收}.
}
\]

因此可将：

\[
h=\gcd(\kappa,G)
\]

解释为：

\[
\boxed{\textbf{Gaussian Non-Split Absorber}.}
\]

而：

\[
D=G/h
\]

则是 surviving Gaussian-split cofactor。

**Status: PROVED**

---

# 12. 为什么 \(5\) 成为 W0-A/B/C 的真正 branch prime

现在有一个结构解释：

- \(2\) 被 \(D\)-Split Firewall 排除；
- 所有 \(p\equiv3\pmod4\) 也被排除；
- 但
  \[
  5\equiv1\pmod4.
  \]

因此在十进制素数中：

\[
\boxed{
5
}
\]

是唯一能够合法留在 split cofactor / source allocation system 中继续重新分配的 prime。

所以 W0-A/B/C 围绕 \(5\)-adic allocation 分裂，并非任意 bookkeeping。

更准确地：

\[
\boxed{
\text{W0 branch split 发生之前，
source integrality 已经清除了全部 non-split denominator freedom。}
}
\]

三支只是在这一共同 firewall **之后** 对 surviving split decimal prime \(5\) 的不同分配状态。

这正是本轮对“跨三个 W0 branch 都成立的原因”的主要结构解释。

---

# 13. Odd-Inert Gram Excess 作为统一 killer 的退休

上一轮曾考虑 denominator-only kernel：

\[
\mathfrak G
=
L(10^{2d_3}H_n-Q^2)-2Q\tau
\]

是否对所有 W0 source state 都必须出现 odd exponent inert prime：

\[
p\equiv3\pmod4.
\]

该猜想过强。

构造 denominator/source-normalized formal state：

\[
b_1=b_2=1,
\qquad
b_3=2,
\]

\[
m_2=m_3=1.
\]

则：

\[
Q=11,
\qquad
G=1,
\]

\[
\kappa=55,
\qquad
h=D=1,
\]

\[
A_\kappa=55,
\qquad
B_\kappa=57,
\qquad
c=2.
\]

取：

\[
d_3=1,\qquad n_2=1.
\]

则：

\[
\omega=2,
\qquad
L=5,
\qquad
\tau=1,
\]

\[
A_0=11,
\qquad
q_0=1.
\]

并且：

\[
\mathfrak G=49873.
\]

而：

\[
\boxed{
49873=12^2+223^2,
}
\]

且：

\[
49873=53\cdot941,
\]

其中：

\[
53\equiv941\equiv1\pmod4.
\]

所以：

\[
\boxed{
\text{W0 denominator/source normalization}
\not\Rightarrow
\text{odd-inert Gram excess}.
}
\]

因此：

\[
\boxed{
\textbf{Odd-Inert Gram Excess as a W0-wide killer is RETIRED.}
}
\]

注意该 state 只是 architecture falsification，不是 genuine original candidate。

---

# 14. \(A_0\) 中 inert support 的定位

虽然 \(D\) 中已不存在 inert prime，但 \(A_0\) 仍可能含：

\[
p\equiv3\pmod4.
\]

设：

\[
p\mid A_0,
\qquad
p\equiv3\pmod4.
\]

由于：

\[
p\nmid L,
\qquad
p\nmid D,
\qquad
p\nmid\omega,
\]

设：

\[
a:=v_p(A_0)>0,
\]

\[
E:=v_p(q_0).
\]

则：

\[
v_p(b_3)=E,
\]

而：

\[
v_p(Q)=E+a>E.
\]

记：

\[
e_i:=v_p(b_i).
\]

若：

\[
e_1\ne e_2,
\]

则：

\[
v_p(Q)=\min(e_1,e_2).
\]

所以：

\[
\min(e_1,e_2)>E=e_3.
\]

此时 prefix 中较大的 \(e_i\) 为 unique maximum。

denominator prime graph 对 inert prime 要求其余两块 valuation 相等，于是应有：

\[
\min(e_1,e_2)=e_3,
\]

矛盾。

因此：

\[
e_1=e_2.
\]

若：

\[
e_1=e_2>E,
\]

则 \(b_1,b_2\) 为 pair-max，又违反 inert prime graph。

故：

\[
\boxed{
v_p(b_1)=v_p(b_2)\le v_p(b_3).
}
\]

此外：

\[
Q=A_0q_0
\]

给：

\[
\boxed{
v_p(A_0)
=
v_p(Q)-v_p(b_3).
}
\]

所以：

> \(A_0\) 中的 inert support 精确记录了 first-two denominator concatenation \(Q\) 超过第三 denominator \(p\)-depth 的额外 cancellation。

即：

\[
\boxed{
p\mid A_0,\ p\equiv3\pmod4
}
\]

并非普通 factor support，而是一个 **deep prefix decimal cancellation signature**。

## Theorem 14.1 — \(A_0\)-Inert Localization

\[
\boxed{
p\mid A_0,\quad p\equiv3\pmod4
\Longrightarrow
v_p(b_1)=v_p(b_2)\le v_p(b_3).
}
\]

并且：

\[
\boxed{
v_p(A_0)=v_p(Q)-v_p(b_3).
}
\]

**Status: PROVED**

---

# 15. 当前对跨三支共同机制的判断

此前候选依次经历：

- RTNT
- DTLC
- SCDF
- Half-Tail Phase
- Full-Tail Gaussian Decontenting
- Odd-Inert Gram Excess

本轮后更准确的共同机制是：

\[
\boxed{
\textbf{Full-Tail Exact Quotient}
+
\textbf{Primitive \(D\)-Prime Equal-Load}
+
\textbf{Gaussian Split-Cofactor Firewall}.
}
\]

完整信息链：

\[
10^{m_3}=\omega L,
\qquad
b_3=\omega\tau
\]

\[
\Downarrow
\]

\[
A_\kappa=LA_0,
\quad
Q=A_0q_0,
\quad
\tau=Dq_0
\]

\[
\Downarrow
\]

\[
M=LA_0+D
\]

\[
\Downarrow
\]

\[
u=L(h/\gamma)j,
\qquad
v=(h/\gamma)(Lj+2\gamma a_3)
\]

\[
\Downarrow
\]

对每个：

\[
p\mid D
\]

有：

\[
v_p(u)=v_p(v)=v_p(h)
\]

\[
\Downarrow
\]

\[
v_p(N)=2(v_p(h)-v_p(c))
\]

\[
\Downarrow
\]

结合 actual weighted norm 与 denominator prime graph：

\[
\boxed{
p\mid D\Rightarrow p\equiv1\pmod4.
}
\]

因此三条 W0 branch 的 \(5\)-adic 分裂发生在一个已经被统一清洗过的 source architecture 内。

---

# 16. 当前 frontier

仍未证明：

\[
\boxed{W0=\varnothing.}
\]

因此：

\[
\boxed{
W0\text{-A/B/C simultaneous extinction = OPEN.
}
\]

当前最值得继续的对象已不是：

- 新 Gaussian kernel；
- higher Hensel；
- \(2/5\)-local phase；
- generic reciprocity；
- denominator-only odd-inert excess。

而是：

\[
\boxed{
A_0\text{-inert deep cancellation}
\times
\text{actual numerator prefix cut}.
}
\]

具体：

若

\[
p\equiv3\pmod4,
\qquad
p\mid A_0,
\]

已知：

\[
v_p(b_1)=v_p(b_2)\le v_p(b_3),
\]

且：

\[
v_p(Q)>v_p(b_3).
\]

下一步需要把 source 对同一个 \(p\) 所强迫的 numerator phase 与：

\[
P=a_1 10^{n_2}+a_2
\]

联立。

理想目标是获得：

\[
p^r\mid P
\]

或其他 source-imposed prefix phase。

若同时有：

\[
p^r\mid Q,
\]

则两条 decimal cancellation 将同步约束：

\[
\frac{a_2b_1}{a_1b_2}
\]

并把 actual norm：

\[
N=(a_1b_2)^2+(a_2b_1)^2
\]

压到：

\[
1+10^{2s_2}
\]

型 local character。

对：

\[
p\equiv3\pmod4
\]

这可能成为下一条真正的 source × decimal-cut collision theorem。

---

# 17. Ledger

| Item | Status |
|---|---|
| Residual-Tail Exact Quotient Normal Form | **PROVED** |
| \(L\mid A_\kappa\) | **PROVED** |
| \(Q=A_0q_0,\ \tau=Dq_0,\ c=\omega q_0\) | **PROVED** |
| Primitive Gap Quantum sharpening | **PROVED** |
| Old \(g_0\)-quantum formulation | **SHARPENED / NONPRIMITIVE FORM RETIRED** |
| \(D\)-Prime Equal-Load Firewall | **PROVED** |
| \(D\)-Prime Norm Load | **PROVED** |
| Odd inert primes in \(D\) | **IMPOSSIBLE** |
| \(2\mid D\) | **IMPOSSIBLE** |
| \(D\)-Split Firewall | **PROVED** |
| \(h\) as Gaussian Non-Split Absorber | **PROVED** |
| \(A_0\)-Inert Localization | **PROVED** |
| Odd-Inert Gram Excess as uniform W0 killer | **RETIRED** |
| W0-A/B/C simultaneous extinction | **OPEN** |

---

# 18. Terminal verdict

本轮尚不能写：

\[
W0=\varnothing.
\]

但可正式冻结以下结构性结论：

\[
\boxed{
D
\text{ is a purely Gaussian-split cofactor.}
}
\]

以及：

\[
\boxed{
h
\text{ absorbs all \(2\)-primary and \(3\bmod4\) denominator support.}
}
\]

因此 W0-A/B/C 的 \(5\)-adic 分支不是三个彼此独立的根本机制；它们发生在一个共同的 pre-branch source firewall 之后。

当前最自然的下一研究对象为：

\[
\boxed{
A_0\text{-inert deep cancellation}
\times
P\text{-cut phase}.
}
\]

---
