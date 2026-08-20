# DD-SA A0-Inert Coverage Audit

## 0. Executive verdict

本轮得到的不是 Coverage Theorem，而是一个相当明确的 **Coverage Countermodel Theorem**。

R20 的真正结论仍然只是

\[
\boxed{
D\text{ 中的 Gaussian non-split support 被清空}
}
\]

而不是

\[
\boxed{
\text{被清掉的 non-split support 必须迁移到 }A_0.
}
\]

R20 的 exact quotient、primitive gap quantum 与 \(D\)-split firewall 均已核对；其确实给出

\[
A_\kappa=LA_0,\qquad
Q=A_0q_0,\qquad
\tau=Dq_0,\qquad
c=\omega q_0,
\]

以及

\[
u=L(h/\gamma)j,\qquad
v=(h/\gamma)(Lj+2\gamma a_3),
\]

并证明

\[
p\mid D\Longrightarrow p\equiv1\pmod4.
\]

但是可以进一步严格构造：

\[
\boxed{
\text{对任意纯 split 的 }A_0=S,
\text{ 都存在无限 primitive、source-consistent 的 R20 states。}
}
\]

其中尤其包括

\[
A_0=1,\qquad A_0=5^r,\qquad A_0=p^r\;(p\equiv1\bmod4),
\]

以及任意有限乘积

\[
A_0=\prod p_i^{e_i},
\qquad p_i\equiv1\pmod4.
\]

因此按照本轮预先规定的 falsification standard，应判：

\[
\boxed{\textbf{Verdict B — SPLIT-ONLY SOURCE FAMILIES EXIST}.}
\]

即：

```text
A0_INERT_COVERAGE=FALSE
SPLIT_ONLY_FORMAL_FAMILY=EXHIBITED
NEXT_ROUTE=A0_INERT_RETIRED_AS_UNIVERSAL
```

这里的 `FALSE` 精确含义是：

> **\(A_0\)-inert coverage 不是 R20 branch-free source architecture 的 universal consequence，因此不能作为 DD-SA 下一条统一主线。**

这**不是**声称已经构造了 genuine original W0 solution；最后的 actual-cut norm realization 仍然是独立 gate。

---

## 1. Dependency freeze

R11–R20 的阶段结论已经明确把共同上游机制压成

\[
\boxed{
\text{Residual-Tail Exact Quotient}
\to
D\text{-Prime Equal-Load}
\to
D\text{-Split Firewall}.
}
\]

其现代解释正是：

\[
G=hD,
\]

其中 \(h\) 吸收 \(2\)-primary 与所有 \(3\bmod4\) denominator support，而 \(D\) 只允许 Gaussian split primes。

R20 对 \(A_0\)-inert support 的已有结论则只是：

\[
p\equiv3\pmod4,\quad p\mid A_0
\]

时，

\[
v_p(b_1)=v_p(b_2)\le v_p(b_3),
\]

以及

\[
v_p(A_0)=v_p(Q)-v_p(b_3).
\]

也就是说，它描述 **一旦 inert prime 已经在 \(A_0\) 中，它长什么样**；没有证明这种 prime 必须存在。

这正是本轮必须保持的：

\[
\boxed{
\textbf{PURIFICATION}\ne\textbf{FORCED RELOCATION}.
}
\]

---

## 2. \(A_0\) prime-support ledger

由

\[
Q=A_0q_0
\]

立刻有，对任意素数 \(p\)：

\[
\boxed{
v_p(A_0)=v_p(Q)-v_p(q_0).
}
\tag{2.1}
\]

因此：

\[
\boxed{
p\mid A_0\Longrightarrow p\mid Q.
}
\]

反过来：

\[
\boxed{
p\mid A_0
\iff
v_p(Q)>v_p(q_0).
}
\tag{2.2}
\]

又因为

\[
b_3=\omega Dq_0,
\]

所以

\[
v_p(q_0)
=
v_p(b_3)-v_p(\omega)-v_p(D).
\]

故一般地：

\[
\boxed{
v_p(A_0)
=
v_p(Q)-v_p(b_3)+v_p(\omega)+v_p(D).
}
\tag{2.3}
\]

若 \(p\mid A_0\)，由于

\[
\gcd(A_0,D)=1,
\]

自动有 \(p\nmid D\)，于是：

\[
\boxed{
v_p(A_0)
=
v_p(Q)-v_p(b_3)+v_p(\omega).
}
\tag{2.4}
\]

而对 odd \(p\neq5\)，\(\omega\mid10^{m_3}\) 故 \(p\nmid\omega\)，于是得到一个比 R20 inert 版本稍一般的公式：

\[
\boxed{
p\neq2,5,\quad p\mid A_0
\Longrightarrow
v_p(A_0)=v_p(Q)-v_p(b_3).
}
\tag{2.5}
\]

注意 (2.5) 对 \(p\equiv1\bmod4\) 和 \(p\equiv3\bmod4\) 都成立；真正区分二者的是 denominator prime graph，而不是 quotient algebra 本身。

### Prime ledger

| prime class | \(D\) | \(A_0\) | 当前结论 |
|---|---:|---:|---|
| \(p=2\) | impossible | algebraically possible | 无 relocation theorem |
| \(p=5\) | possible | possible，但不能同时与 \(D\) share | \(5\) 是 split prime |
| \(p\equiv1\pmod4\) | possible | possible | 无任何 firewall 阻止 \(A_0\) 纯 split |
| \(p\equiv3\pmod4\) | impossible | possible | 若出现则满足 R20 deep-cancellation localization |

所以目前完全没有 support ledger 能推出：

\[
A_0\text{ 必须含 inert prime}.
\]

---

## 3. 核心反构造：任意 split-only \(A_0\) 都能实现

这是本轮最重要的新 theorem。

### Theorem 3.1 — Arbitrary Split-Support Quotient Realization

任取奇正整数

\[
S\ge1
\]

使所有素因子均满足

\[
p\equiv1\pmod4.
\]

允许 \(S=1\)。

令

\[
k:=\ell(S),
\qquad
q:=10^k+1.
\]

取 denominator data

\[
\boxed{
b_1=b_2=S,\qquad b_3=q.
}
\tag{3.1}
\]

则

\[
m_1=m_2=k,\qquad m_3=k+1.
\]

因此

\[
Q=b_1 10^{m_2}+b_2
=S10^k+S
=S(10^k+1)
=Sq,
\]

\[
G=S^2,
\qquad
T=10^{k+1}.
\]

于是

\[
\kappa
=
\frac{TQG}{b_3}
=
10^{k+1}S^3.
\]

因为 \(S^2\mid\kappa\)，

\[
h=\gcd(\kappa,G)=S^2,
\]

故

\[
\boxed{D=1.}
\]

进一步：

\[
A_\kappa=\frac{\kappa}{h}=10^{k+1}S.
\]

另一方面：

\[
\omega
=
\gcd(10^{k+1},10^k+1)
=1,
\]

所以

\[
L=10^{k+1},
\qquad
\tau=q.
\]

代入 R20 exact quotient：

\[
A_\kappa=LA_0
\]

立即得到

\[
\boxed{A_0=S.}
\]

同时

\[
\boxed{
q_0=q,\qquad
c=q.
}
\]

并且：

\[
Dq_0=q=10^k+1<10^{k+1}=L,
\]

\[
\gcd(A_0,D)=1,
\]

\[
\gcd(L,Dq_0)
=
\gcd(10^{k+1},10^k+1)
=1.
\]

定义

\[
M=LS+1.
\]

因为

\[
M\equiv1\pmod S,
\]

有

\[
\boxed{
\gamma=\gcd(S^2,M)=1.
}
\]

所以全部 R20 residual quotient / primitive-gap coefficient architecture 都合法。

\[
\boxed{\text{QED}}
\]

### 3.2 直接覆盖四类测试

#### \(A_0=1\)

取

\[
S=1.
\]

于是：

\[
\boxed{A_0=1}
\]

完全没有在 R20 quotient architecture 上被排除。

#### \(A_0=5^r\)

取

\[
S=5^r.
\]

得到任意深度纯 \(5\)-support。

#### \(A_0=p^r,\ p\equiv1\bmod4\)

直接取

\[
S=p^r.
\]

#### arbitrary split-only product

取

\[
S=\prod_jp_j^{e_j},
\qquad
p_j\equiv1\pmod4.
\]

因此 \(A_0\) 不仅“偶尔可以 split-only”，而是：

\[
\boxed{
\textbf{split-only support 在 R20 quotient 层几乎可以任意指定。}
}
\]

这已经足够摧毁 universal inert coverage 的希望。

---

## 4. 提升到无限 primitive + source-consistent family

固定上面的任意 \(S\)。

令：

\[
d_3=1,
\qquad
n_3=m_3+1=k+2,
\]

并取

\[
\boxed{
a_3=10^{k+1}+1.
}
\tag{4.1}
\]

则：

\[
\gcd(a_3,b_3)
=
\gcd(10^{k+1}+1,10^k+1).
\]

相减可化为

\[
\gcd(10^k+1,9).
\]

而

\[
10^k+1\equiv2\pmod3,
\]

故：

\[
\boxed{
\gcd(a_3,b_3)=1.
}
\]

现在选择任意正整数 \(t\) 满足：

\[
\boxed{
Sa_3+Mq^2t\equiv0\pmod{10}.
}
\tag{4.2}
\]

由于

\[
Mq^2\equiv1\pmod{10},
\]

这样的 \(t\) 构成无限 arithmetic progression。

定义：

\[
\boxed{j=q^2t,}
\]

\[
\boxed{
P=\frac{Sa_3+Mq^2t}{10},
}
\tag{4.3}
\]

以及

\[
\boxed{
u=LS^2q^2t,
}
\]

\[
\boxed{
v=S^2(Lq^2t+2a_3).
}
\]

最后令：

\[
\boxed{
N=S^4Lt(Lq^2t+2a_3).
}
\tag{4.4}
\]

则逐项检查：

\[
10P-Sa_3
=Mq^2t
=Mj,
\]

而这里

\[
\omega=D=\gamma=1,
\]

故这正是

\[
\Xi=\frac M\gamma j.
\]

又：

\[
v-u
=
2S^2a_3
=
2ha_3.
\]

并且：

\[
uv
=
Nq^2
=
Nc^2.
\]

更重要的是，exact source factor sum 也自动满足：

\[
B_\kappa u+A_\kappa v
=
2GP10^{n_3}.
\]

因此这是一个完整的：

\[
\boxed{
\texttt{SOURCE-CONSISTENT R20 FAMILY}.
}
\]

---

## 5. 前两块 individual primitive 也可以同时实现

进一步令

\[
n_2=k=m_2.
\]

于是：

\[
s_2=0,
\qquad
d_3=1,
\qquad
k_{12}=s_2+d_3=1>0.
\]

所以该 construction 仍处于 DD carrier sign geometry 中。

把 (4.2) 的解写成：

\[
t=t_0+10z.
\]

则 \(P\) 随 \(z\) 作 affine progression：

\[
P=P_0+Cz,
\qquad
C=Mq^2,
\]

且

\[
\gcd(C,10)=1.
\]

现在指定 suffix：

\[
a_2=
\begin{cases}
1,&S=1,\\
S-1,&S>1.
\end{cases}
\]

显然：

\[
\gcd(a_2,S)=1.
\]

利用 \(C\) 对 \(10^k\) 可逆，可选 \(z\) 使：

\[
P\equiv a_2\pmod{10^k}.
\]

于是：

\[
P=a_1 10^k+a_2.
\]

再沿

\[
z\mapsto z+10^kw
\]

变化。

对每个 \(p\mid S\)：

- 若 \(p\nmid C\)，只需避开一个 \(w\bmod p\) residue，就能保证 \(p\nmid a_1\)；
- 若 \(p\mid C\)，则因为 \(M\equiv1\bmod p\)，只能来自 \(p\mid q\)。此时 source equation 模 \(p\) 强制 \(P\equiv0\bmod p\)，而
  \[
  a_2=S-1\equiv-1\pmod p,
  \]
  因而
  \[
  10^ka_1\equiv1\pmod p,
  \]
  自动有 \(p\nmid a_1\)。

CRT 因而给出无限多个 \(w\)，同时满足：

\[
\boxed{
\gcd(a_1,S)=1.
}
\]

结合前面：

\[
\gcd(a_2,S)=1,
\qquad
\gcd(a_3,q)=1,
\]

最终得到：

\[
\boxed{
\gcd(a_i,b_i)=1,\qquad i=1,2,3.
}
\]

---

## 6. Countermodel 层级分类

因此这个 family 的准确分层为：

\[
\boxed{
\begin{array}{c|c}
\text{Layer}&\text{Status}\\
\hline
\texttt{ALGEBRAIC}&\textbf{PROVED}\\
\texttt{INTEGRAL}&\textbf{PROVED}\\
\texttt{PRIMITIVE}&\textbf{PROVED}\\
\texttt{SOURCE-CONSISTENT}&\textbf{PROVED}\\
\texttt{ACTUAL-CUT-CONSISTENT}&\textbf{NOT ESTABLISHED}
\end{array}}
\]

最后一行必须严格保留。

我们构造出的 source \(N\) 为：

\[
N=S^4Lt(Lq^2t+2a_3),
\]

而 actual cut 要求：

\[
N
\stackrel{?}{=}
(a_1b_2)^2+(a_2b_1)^2
=
S^2(a_1^2+a_2^2).
\]

这个 equality 没有被 construction 自动满足。

因此：

\[
\boxed{
\text{这是 source-interface countermodel，}
\text{不是 original-problem solution。}
}
\]

但本轮判据正是：

> 只要存在无限 `SOURCE-CONSISTENT` split-only family，就足以否决把 \(A_0\)-inert 当作 universal route。

所以 Verdict B 已经达到。

---

## 7. \(A_0=1\) 的专门审计

\(A_0=1\) 不但 algebraically possible，而且落入上述无限 family。

最小形态取：

\[
S=1,\quad k=1,
\]

则：

\[
b_1=b_2=1,\qquad b_3=11,
\]

\[
Q=11,\qquad
G=1,
\]

\[
T=100,
\]

\[
h=D=1,
\]

\[
A_\kappa=100,
\]

\[
\omega=1,\qquad
L=100,
\]

\[
q_0=c=11,
\]

\[
\boxed{A_0=1}.
\]

同时：

\[
M=101,\qquad\gamma=1.
\]

随后按第 4–5 节的 \(t\)-progression 可以生成无限 primitive source-consistent states。

故：

\[
\boxed{
A_0=1\Longrightarrow\varnothing
}
\]

在 R20 branch-free source interface 上明确为假。

因此 F2 无法作为 coverage 第一步。

---

## 8. split-only 本身有没有简单同层 obstruction？

没有发现，而且上面的任意-\(S\) theorem 实际上强烈说明：

\[
\boxed{
\text{仅靠 split support bookkeeping 不可能形成同层 obstruction。}
}
\]

例如 split-only \(A_0\) 当然是 Gaussian norm：

\[
A_0=x^2+y^2.
\]

但我们的 family 同时具有：

\[
D=1,
\qquad
M=LA_0+1,
\]

并且：

\[
\gcd(A_0,M)=1.
\]

因此以下几类候选 obstruction 全部被 construction 吸收：

- \(A_0\) 为 Gaussian norm；
- \(A_0\) 与 \(M\) Gaussian/rational coprimality；
- complementary split-factor support；
- \(D\)-allocation；
- elementary split-prime capacity；
- 单纯由
  \[
  B_\kappa=LA_0+2D
  \]
  产生的 support incompatibility。

所以没有得到：

\[
A_0^{\rm inert}=1
\Longrightarrow
\mathcal O_{\rm split}.
\]

即：

\[
\boxed{
\texttt{A0_SUPPORT_DICHOTOMY=NOT_PROVED}.
}
\]

如果 split-only states 最终仍然全部死亡，那一刀必须读取至少一个新的 semantic layer，最明显的就是：

\[
\boxed{
\text{actual cut realization }N=(a_1b_2)^2+(a_2b_1)^2.
}
\]

---

## 9. 最短 inert \(\to P\) probe

假设：

\[
p\equiv3\pmod4,
\qquad
p\mid A_0.
\]

R20 已证明：

\[
e_1:=v_p(b_1)
=
e_2:=v_p(b_2)
\le
e_3:=v_p(b_3).
\]

考察特别重要的 **equal-load subcase**：

\[
\boxed{
e_1=e_2=e_3=E>0.
}
\]

由于 individual reducedness，

\[
p\nmid a_1a_2a_3.
\]

而 \(p\equiv3\bmod4\)，所以两平方和没有 unit-level cancellation，故 actual weighted norm 满足：

\[
\boxed{
v_p(N)=2E.
}
\]

又因 \(p\nmid D,\omega\)：

\[
v_p(h)=v_p(G)=2E,
\]

\[
v_p(c)=E.
\]

并且

\[
p\nmid L,\gamma,M.
\]

代入：

\[
u=L(h/\gamma)j,
\]

\[
v=(h/\gamma)(Lj+2\gamma a_3),
\]

以及：

\[
uv=Nc^2,
\]

右侧 valuation 为：

\[
v_p(Nc^2)=2E+2E=4E.
\]

但公共 factor

\[
(h/\gamma)^2
\]

已经贡献全部 \(4E\)。

所以必须：

\[
\boxed{
p\nmid j
}
\]

以及

\[
p\nmid Lj+2\gamma a_3.
\]

另一方面 primitive-gap equation 是：

\[
\omega D10^{d_3}P-A_0a_3
=
\frac M\gamma j.
\]

模 \(p\) 时，因为 \(p\mid A_0\)，且其余 coefficient 均为 \(p\)-units：

\[
p\mid P
\iff
p\mid j.
\]

故：

\[
\boxed{
e_1=e_2=e_3
\Longrightarrow
p\nmid P.
}
\tag{9.1}
\]

这非常关键。

原先诱惑是：

\[
p\mid A_0
\stackrel{?}{\Longrightarrow}
p\mid P.
\]

但在一个完全合法的 inert-load subcase 中，source + actual weighted norm 给出的方向恰好相反：

\[
\boxed{
p\mid A_0
\quad\text{且 equal denominator load}
\Longrightarrow
p\nmid P.
}
\]

因此统一的

\[
A_0\text{-inert}\to P\text{-phase forcing}
\]

不能成立。

---

## 10. 更一般的 inert load routing

若：

\[
e_1=e_2=E\le e_3,
\]

同样计算可得：

\[
v_p(N)=2E,
\]

\[
v_p(h)=2E,
\qquad
v_p(c)=e_3.
\]

于是 product relation 给：

\[
\boxed{
v_p(j)
+
v_p(Lj+2\gamma a_3)
=
2(e_3-E).
}
\tag{10.1}
\]

这里有两个合法 absorption channel：

1. \(j\) 吸收 excess；
2. \(Lj+2\gamma a_3\) 吸收 excess。

由于 \(a_3\) 是 \(p\)-unit：

- 一旦 \(p\mid j\)，第二 factor 自动为 unit；
- 若 \(j\) 为 unit，则 excess 可以进入第二 factor。

所以即使

\[
e_3>E,
\]

也没有 automatic theorem 强迫：

\[
p\mid j
\]

从而也没有 automatic theorem 强迫：

\[
p\mid P.
\]

要继续这一方向，首先必须另证：

\[
\boxed{
\text{actual survivor 中只允许某一个 load channel}.
}
\]

这已经是一个新的 auxiliary layer。

按本轮纪律，应停止。

因此：

```text
INERT_TO_P_PHASE_TRANSFER=FALSE_AS_UNIFORM_IMPLICATION
```

---

## 11. F1–F6 falsification ledger

### F1

\[
W0\Longrightarrow
\exists p\equiv3\pmod4:p\mid A_0.
\]

**Verdict：FALSE AS A CONSEQUENCE OF THE R20 BRANCH-FREE SOURCE SYSTEM.**

无限 split-only primitive source family 已构造。

对 genuine actual-cut survivor 的字面命题仍不能仅凭该 counterfamily 直接否证，因为 actual norm gate 尚未满足；但这已经足以退休它作为 R20-derived universal route。

### F2

\[
A_0=1\Longrightarrow\varnothing.
\]

**Verdict：FALSE AT SOURCE INTERFACE.**

\(S=1\) 给出无限 primitive source-consistent family。

### F3

\[
A_0\text{ split-only}\Longrightarrow\varnothing.
\]

**Verdict：FALSE AT SOURCE INTERFACE.**

事实上任意 split-only \(S\) 均可作为 \(A_0\)。

### F4

\[
p^r\mid A_0,\quad p\equiv3(4)
\Longrightarrow
p^r\mid P.
\]

**Verdict：FALSE AS UNIFORM SOURCE/ACTUAL-NORM CONSEQUENCE.**

equal-load subcase 甚至推出 \(p\nmid P\)。

### F5

\[
p\mid A_0,\quad p\equiv3(4)
\Longrightarrow
p\mid P.
\]

**Verdict：FALSE AS UNIFORM IMPLICATION.**

由 (9.1)：

\[
e_1=e_2=e_3>0
\Longrightarrow
p\nmid P.
\]

### F6

是否存在无限

\[
A_0\text{ split-only}
\]

且满足 R20 branch-free source constraints 的 family？

\[
\boxed{\textbf{YES — PROVED}.}
\]

而且可以同时满足：

- exact quotient；
- \(D=1\) firewall；
- primitive gap quantum；
- source product；
- source difference；
- exact factor sum；
- DD carrier signs；
- 三个 individual reducedness。

这是本轮决定性的 falsification theorem。

---

## 12. New general theorems

### Theorem A — \(A_0\) Support Quotient Ledger

\[
\boxed{
v_p(A_0)=v_p(Q)-v_p(q_0).
}
\]

对 odd \(p\neq5\) 且 \(p\mid A_0\)：

\[
\boxed{
v_p(A_0)=v_p(Q)-v_p(b_3).
}
\]

### Theorem B — Arbitrary Split-Support Source Realization

对任意 split-only odd integer \(S\ge1\)，存在无限 primitive R20 source-consistent states，使：

\[
\boxed{
A_0=S,\qquad D=1.
}
\]

特别：

\[
\boxed{
A_0=1
}
\]

和任意大的 pure-split \(A_0\) 都能出现。

### Theorem C — Equal-Load Inert Anti-Transfer

若 genuine source/actual weighted-norm state 中：

\[
p\equiv3\pmod4,\qquad p\mid A_0,
\]

且：

\[
v_p(b_1)=v_p(b_2)=v_p(b_3)>0,
\]

则：

\[
\boxed{
p\nmid P.
}
\]

所以 inert \(A_0\) 并不会普遍向 numerator prefix 复制 phase；在一个自然 subcase 中，它反而被 source architecture 排斥出 \(P\)。

---

## 13. Route retirement

本轮之后应正式退休以下命题作为 **DD-SA universal architecture**：

\[
\boxed{
D\text{-purification}
\Rightarrow
\text{non-split support relocates to }A_0.
}
\]

FALSE / UNSUPPORTED。

\[
\boxed{
W0
\Rightarrow
A_0\text{ has inert support}.
}
\]

NOT AVAILABLE FROM BRANCH-FREE SOURCE STRUCTURE。

\[
\boxed{
A_0\text{-inert}
\Rightarrow
p\mid P.
}
\]

FALSE AS UNIFORM IMPLICATION。

\[
\boxed{
A_0\text{ split-only}
\Rightarrow
\text{elementary Gaussian support obstruction}.
}
\]

FALSE AT CURRENT INFORMATION LEVEL；任意 split support 已被 explicit family 吸收。

因此 R20 最后的“当前最自然 frontier 是 \(A_0\)-inert deep cancellation × actual prefix cut”现在应当降级。

---

## 14. Universal W0 progress

本轮没有进一步关闭 genuine W0。

但是完成了一个很重要的负向架构决策：

\[
\boxed{
\textbf{\(A_0\)-inert localization 不是跨整个 W0 的共同 extinction mechanism。}
}
\]

这进一步澄清了 R11–R20 真正得到的统一结构究竟到哪里截止：

\[
\boxed{
\text{Gaussian support purification stops at }D.
}
\]

不能再无损地继续写成：

\[
D\text{-purification}
\to
A_0\text{-inert}
\to
P\text{-phase}.
\]

真正仍然 branch-free 且尚未消失的 semantic gate 是：

\[
\boxed{
(P,N)_{\rm source}
\stackrel{?}{\in}
\mathcal I_{\rm actual\ cut}.
}
\]

这与此前 DD-SA 已经得到的 source/cut image endpoint 一致，而不是一个新的长正规型。

---

## 15. Final machine-readable report

```text
DD-SA A0-INERT COVERAGE AUDIT
================================

R20_INPUT_STATUS=
FROZEN_AND_VERIFIED

A0_INERT_COVERAGE=
FALSE

A0_EQ_1_STATUS=
INFINITE_PRIMITIVE_SOURCE_CONSISTENT_FAMILY_EXISTS

SPLIT_ONLY_A0_STATUS=
ARBITRARY_SPLIT_ONLY_SUPPORT_REALIZABLE_AT_R20_SOURCE_INTERFACE

SPLIT_ONLY_FORMAL_FAMILY=
EXHIBITED_INFINITE_PRIMITIVE_SOURCE_CONSISTENT_FAMILY

INERT_TO_P_PHASE_TRANSFER=
FALSE_AS_UNIFORM_IMPLICATION
EQUAL_LOAD_SUBCASE_FORCES_P_NOT_DIVISIBLE_BY_p

SUPPORT_DICHOTOMY=
NOT_PROVED

UNIVERSAL_W0_PROGRESS=
A0_INERT_UNIVERSAL_ROUTE_FALSIFIED
ACTUAL_CUT_REALIZATION_REMAINS_THE_MISSING_SEMANTIC_GATE

ROUTES_RETIRED=
FORCED_NON_SPLIT_RELOCATION_TO_A0
A0_INERT_AS_UNIVERSAL_W0_ROUTE
UNCONDITIONAL_A0_INERT_TO_P_DIVISIBILITY
SPLIT_ONLY_GAUSSIAN_SUPPORT_AS_SAME_LAYER_KILLER

NEW_GENERAL_THEOREMS=
A0_SUPPORT_QUOTIENT_LEDGER
ARBITRARY_SPLIT_SUPPORT_SOURCE_REALIZATION
EQUAL_LOAD_INERT_ANTI_TRANSFER

NEXT_ROUTE=
A0_INERT_RETIRED_AS_UNIVERSAL

GO_NO_GO=
NO_GO
```

---

## 16. Final verdict

\[
\boxed{
\texttt{A0\_INERT\_COVERAGE=FALSE}
}
\]

\[
\boxed{
\texttt{SPLIT\_ONLY\_FORMAL\_FAMILY=EXHIBITED}
}
\]

\[
\boxed{
\texttt{NEXT\_ROUTE=A0\_INERT\_RETIRED\_AS\_UNIVERSAL}
}
\]

这次抽卡的价值就在于及时阻止了下一次十轮扩张。

R20 的 \(A_0\)-inert localization 本身仍是正确且漂亮的 conditional theorem；但 coverage audit 表明，它只是 W0 source space 的一个 conditional subset，而且连预想的

\[
p\mid A_0\to p\mid P
\]

在自然 equal-load subcase 中都会反向失败。

所以不应继续沿着：

\[
A_0\text{-inert}
\to
Q\text{ deep cancellation}
\to
P\text{ phase}
\]

再做一组 campaign。

## 是否值得继续投入 DD-SA

\[
\boxed{\textbf{FREEZE}}
\]

不是因为 DD-SA 没有价值——R11–R20 已经成功提炼出真正 branch-free 的 \(D\)-split purification——而是因为**这一独立结构线目前已经完成了它最重要的附加任务：确定统一机制在哪里停止。**

若未来因主证明需要重新调用 DD-SA，唯一值得重新接入的接口应是已经存在的：

\[
\boxed{
\text{source image}
\times
\text{actual decimal cut realization},
}
\]

而不是继续深挖 \(A_0\)-inert conditional consequences。
