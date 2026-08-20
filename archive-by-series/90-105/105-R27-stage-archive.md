# 105-R27 阶段归档
## Primitive-Sphere Decimal-Content Collapse × Gaussian Split × Exceptional-Locus Extinction × Global Survivor-or-Witness

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — `(A_1)`-only  
**Round:** 105-R27  
**Status:** FROZEN / ARCHIVED  
**Arithmetic:** exact integers / exact valuations; finite enumeration is reconnaissance only

---

# 0. Executive Verdict

R27 没有证明全局空性，也没有得到全局 primitive-packet 有限化，更没有发现 full Strict-`A_1` witness。

但是 R27 对 R26 留下的唯一无限对象——positive primitive integral 3-sphere carrier locus——取得了真正的 **packet-only exceptional-locus collapse**。

本轮最强正式结论为：

\[
\boxed{\texttt{PRIMITIVE\_SPHERE\_EXCEPTIONAL\_LOCUS\_COLLAPSE=YES}}
\]

更精确地，定义

\[
T_-:=Q_0-P_3,\qquad T_+:=Q_0+P_3,
\]

以及对 `p=2,5` 的 packet-only decimal capacities

\[
\mathfrak C_p(\pi)=v_p(T_-)+
\begin{cases}
 x_p+y_p-z_p,&y_p\ge z_p,\\[2mm]
 \min(x_p,y_p)+\max(0,x_p-z_p),&y_p<z_p,
\end{cases}
\tag{CAP-p}
\]

其中

\[
x_p=v_p(P_1),\quad y_p=v_p(P_2),\quad z_p=v_p(P_3).
\]

则任何 R26 full survivor `C26(pi)=1` 必须满足

\[
\boxed{\mathfrak C_2(\pi)\ge1,\qquad \mathfrak C_5(\pi)\ge1}
\tag{DEC-CAP}
\]

以及 selector-free size gate

\[
\boxed{P_1P_2T_->10P_3.}
\tag{ARCH}
\]

故定义

\[
\boxed{
\mathscr E_{27}:=
\{\pi\text{ primitive positive sphere}:\
\mathfrak C_2(\pi)\ge1,\ 
\mathfrak C_5(\pi)\ge1,\
P_1P_2T_->10P_3\}
}
\]

则

\[
\boxed{\mathscr P_{26}\subseteq\mathscr E_{27}.}
\tag{E27-CONTAIN}
\]

而 `E27` 是严格子 locus：例如 `(P1,P2,P3,Q0)=(1,2,2,3)` 已在 `C2` capacity 处死亡。

同时，R27 构造了无限 primitive family 全部落在 `E27`，证明当前 collapse **不是 global finite reduction**。因此本轮不得签 Verdict 1/2/3。

此外，R27 完成了：

1. `gcd(T_-,T_+)` 的 exact primitive classification；
2. primitive sphere 的 exact parity classification；
3. `v2(P1^2+P2^2)` 与 `v5(P1^2+P2^2)` 的完整局部分类；
4. Gaussian gcd support theorem；
5. `p≡3 (mod 4)` 在 `T_±` 中只能以偶指数出现的 theorem；
6. `sqf(T_-)` 的真实全局限制与“有限 square-kernel”猜想的无限反例族；
7. R26 divisors/selectors 在 `p=2,5` 层面的 existential elimination；
8. R26 dual-decimal TC1 在 `Q0<=500` complete-in-bound reconnaissance，并证明所有 raw TC1 hits 在 frozen R24 support gates 前已死亡——仅作侦察，不作 global theorem。

---

# Part I — File Inventory

## I.1 Frozen R26 files actually read

本轮开始前实际读取并确认：

- `105-R26-stage-archive.md`
- `105-R26-stage-archive.sha256.txt`

R26 companion 中冻结的主归档 SHA-256：

```text
41f4e2aad7720862a98349d61d22c482b7f5045b6c54bfea56651d4032d97680  105-R26-stage-archive.md
```

此外，为恢复 `TC1` 前的 frozen support semantics，本轮读取：

- `105_R24_Post_Support_Source_Carrier_Image.md`

只恢复 R24 已冻结公式，不重开 R24 architecture。

## I.2 R27 generated proof/archive files

- `105-R27-stage-archive.md` — 本主归档；
- `105-R27-stage-archive.sha256.txt` — 本主归档 hash companion；
- `105-R27-SHA256-MANIFEST.txt` — 所有 R27 artifact 的 hash ledger；
- `105-R27-SHA256-MANIFEST.sha256.txt` — manifest 自身 hash companion。

## I.3 R27 machine certificates / registries

- `105-R27-certificate-registry.csv`
- `105-R27-survivor-registry.csv`
- `105-R27-exceptional-locus-registry.csv`
- `105-R27-R26-survivor-counts.csv`
- `105-R27-primitive-sphere-sample.csv`
- `105-R27-valuation-patterns.csv`
- `105-R27-Tminus-square-kernels.csv`
- `105-R27-execution.log`

## I.4 Rerunnable code

- `105-R27-scripts/r27_recon.py`

所有 enumeration/count claims 均以 CSV + log + script 为证，不依赖 Markdown 单独宣告。

---

# Part II — Frozen Inputs

R27 仅使用以下 R26 authoritative facts。

## II.1 Primitive carrier

\[
\pi=(P_1,P_2,P_3,Q_0),
\qquad
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

全部坐标 positive。

## II.2 Finite selectors

固定 `pi` 后：

\[
A\mid P_3,
\qquad
W\mid P_2,
\qquad
u_0\mid\gcd(P_2/W,P_3/A),
\qquad
g_1^*\mid P_1.
\tag{SEL}
\]

本文用 `u0` 记 R26 的 `u_0`；不要与历史其它 chart 中的 `u` 混淆。

恢复

\[
C_2=\frac{P_2}{u_0W},
\qquad
C_3=\frac{P_3}{u_0A}.
\]

R24 frozen shape/support conditions中本轮实际使用：

\[
(A,C_2)=(W,C_3)=(A,W)=1,
\tag{SGCD}
\]

\[
g_0=(u_0AW,P_1),
\qquad
g_0\mid g_1^*\mid P_1,
\tag{MASTER}
\]

\[
\mu=g_1^*/g_0,
\qquad
(\mu,C_2C_3)=1.
\tag{MU}
\]

其余 tail/support 条件只会进一步减少 survivors；本轮 capacity theorem 不需要把它们放松后的最大值夸成 full-support 等价。

## II.3 R26 decimal quotient

\[
T_3=Q_0-P_3=T_-.
\]

\[
N_E=\frac{Wg_1^*T_-}{A},
\qquad
10^nE=N_E,
\qquad E\in\mathbb Z_{>0}.
\tag{NE}
\]

故

\[
1\le n\le\nu_{10}(N_E),
\qquad
10^n\mid N_E.
\tag{NBOUND}
\]

## II.4 Radial `delta` window

令

\[
M_r=P_2/W,
\qquad
N_r=P_3/A.
\]

R26：

\[
10^{\delta-1}<\frac{M_r}{N_r}<10^{\delta+1},
\tag{DELTA}
\]

且 exponent simplex 满足

\[
n+\delta\ge2.
\tag{SIMPLEX}
\]

## II.5 Full dual-decimal collision

\[
\boxed{R_n=10^{n+\delta-\rho}S_{m,\rho}}
\tag{CDN}
\]

其中

\[
R_n=\frac{Wg_1^*T_-}{A10^n}-g_1^*P_2,
\]

\[
S_{m,\rho}
= Wu_0P_1 10^\rho
-Q_0(Wu_0 10^m+g_1^*).
\]

R27 不把 R26 偷换成单独 `10^n|N_E`；后者只作为第一层 projection。Part VI 会把完整 CDN 重新投入。

---

# Part III — Primitive Sphere Arithmetic

# III.1 Primitive parity theorem

## Theorem R27-PARITY

对 positive primitive sphere packet，必有

\[
\boxed{Q_0\text{ odd}.}
\]

且 `P1,P2,P3` 中恰有一个为 odd。

### Proof

若 `Q0` even，则右边 `Q0^2≡0 (mod4)`。平方模 4 只有 `0,1`，三个平方之和要为 0 mod4 只能三者全为 0 mod4，因此 `P1,P2,P3` 全偶，与 primitive 矛盾。

故 `Q0` odd。此时右边 `≡1 (mod4)`，三个平方中 odd square 的个数必须为 1；三个 odd 给 3 mod4，不可能。证毕。

因此只有两种与 `P3` 相关的 parity type：

- `P3` odd，`P1,P2` both even；
- `P3` even，`P1,P2` exactly one even and one odd。

特别地，`P1,P2` both odd 永不出现。

---

# III.2 Exact gcd structure of `T_- , T_+`

令

\[
c:=\gcd(Q_0,P_3).
\]

## Lemma R27-COMMON-SUPPORT

`c` 为 odd，且每个 prime `p|c` 都满足

\[
\boxed{p\equiv1\pmod4.}
\]

### Proof

`Q0` odd，所以 `c` odd。

若存在 `p≡3 mod4` 且 `p|Q0,P3`，则

\[
p^2\mid Q_0^2-P_3^2=P_1^2+P_2^2.
\]

对 inert prime `p≡3 mod4`，`p|x^2+y^2` 强迫 `p|x,y`。于是 `p|P1,P2,P3,Q0`，违背 primitive。证毕。

## Theorem R27-GCD-TPM

\[
\boxed{
\gcd(T_-,T_+)=
\begin{cases}
 c,&P_3\text{ even},\\
 2c,&P_3\text{ odd}.
\end{cases}}
\tag{GCD-TPM}
\]

其中 `c` 只含 `1 mod4` odd primes。

### Proof

写 `Q0=cq, P3=cr`，则 `(q,r)=1` 且 `c` odd。

\[
\gcd(T_-,T_+)=c\gcd(q-r,q+r).
\]

后一个 gcd 同时整除 `2q,2r`，而 `(q,r)=1`，故只可能为 1 或 2。

- 若 `P3` even，则 `r` even、`q` odd，故 `q±r` odd，gcd=1；
- 若 `P3` odd，则 `q,r` both odd，故 `q±r` both even，且除 2 外无公共 odd prime，gcd=2。

证毕。

因此问题 1 的答案不是 `{1,2}`；真正可能的是 `c` 或 `2c`，而 `c` 可以拥有任意 split-prime content。

---

# III.3 Exact 2-adic norm classification

对任意 nonzero integers `x,y`，令

\[
a=v_2(x),\qquad b=v_2(y),\qquad r=\min(a,b).
\]

则

\[
\boxed{
 v_2(x^2+y^2)=
 \begin{cases}
 2r,&a\ne b,\\
 2r+1,&a=b.
 \end{cases}}
\tag{V2-NORM}
\]

证明：除去 `2^r`。若 valuations 不同，括号中一项 odd 一项 divisible by 4，和 odd；若相同，则两个 reduced legs odd，平方和 `≡2 mod4`，valuation exactly 1。

对 primitive sphere，再结合 III.1：

- `P3` odd 时，`P1,P2` both even；
- `P3` even 时，`P1,P2` mixed parity，因此 `v2(P1^2+P2^2)=0`，且 `T_-,T_+` 都 odd；
- `P3` odd 时 `T_±` both even，且由
  \[
  T_+-T_-=2P_3\equiv2\pmod4
  \]
  可知 `v2(T_-),v2(T_+)` 中恰有一个等于 1。

这是完整 primitive 2-adic factor-pair structure。

---

# III.4 Exact 5-adic norm classification and Hensel branches

令

\[
a=v_5(P_1),\quad b=v_5(P_2),\quad r=\min(a,b).
\]

## Unequal valuations

若 `a≠b`，则

\[
\boxed{v_5(P_1^2+P_2^2)=2r.}
\tag{V5-UNEQ}
\]

因为除去 `5^{2r}` 后恰有一个平方为 5-adic unit，另一个 divisible by 25，不能 cancellation。

## Equal valuations

若 `a=b=r`，写

\[
P_1=5^rX,\qquad P_2=5^rY,
\qquad 5\nmid XY.
\]

在 `Z_5` 中令 `iota` 为 `iota^2=-1` 的 Hensel root 且 `iota≡2 (mod5)`。则

\[
X^2+Y^2=(X-\iota Y)(X+\iota Y).
\]

两个 factors 不可能同时 divisible by 5，因为差为 `2 iota Y`，是 5-adic unit。因此若不发生 cancellation，extra valuation 为 0；若发生，则唯一落在两条 branch 之一：

\[
\boxed{X/Y\equiv+\iota\pmod{5^k}}
\quad\text{or}\quad
\boxed{X/Y\equiv-\iota\pmod{5^k}}.
\]

更精确：选择唯一符号 `eps∈{±1}` 使 `5|X-eps*iota Y`，则

\[
\boxed{
v_5(P_1^2+P_2^2)
=2r+v_5(X-\varepsilon\iota Y).
}
\tag{V5-HENSEL}
\]

这给出真正的两个 thin 5-adic Hensel branches，而不是模 5 的经验 residue。

---

# III.5 Gaussian gcd theorem

令

\[
d_0:=\gcd(P_1,P_2),
\qquad P_1=d_0a,
\qquad P_2=d_0b,
\qquad(a,b)=1.
\]

在 `Z[i]` 中：

\[
(P_1+iP_2)(P_1-iP_2)=T_-T_+.
\]

## Theorem R27-GAUSS-GCD

up to Gaussian unit，

\[
\boxed{
\gcd_{\mathbb Z[i]}(P_1+iP_2,P_1-iP_2)
\sim d_0(1+i)^\epsilon,
}
\tag{GGCD}
\]

其中

\[
\epsilon=
\begin{cases}
1,&a,b\text{ both odd},\\
0,&a,b\text{ opposite parity}.
\end{cases}
\]

### Proof

去掉 rational common factor `d0` 后，任意 common Gaussian prime `pi` 同时整除

\[
2a,
\qquad2ib.
\]

若 `pi` 不在 `2` 上，则其 norm 下的 rational prime 同时整除 `a,b`，矛盾。因此唯一可能的 extra Gaussian prime 是 `1+i`。

`1+i | a+ib` iff `a,b` same parity；由于 `(a,b)=1`，same parity 只能 both odd。此时 norm `a^2+b^2≡2 mod4`，故 `(1+i)` 的 extra exponent exactly 1。证毕。

信息增益：Gaussian common support 被完全定位到 rational common content + one dyadic factor；不存在隐藏 odd Gaussian overlap。

---

# III.6 Inert-prime even-exponent theorem for `T_±`

## Theorem R27-INERT-TPM

对任意 `p≡3 mod4`：

\[
\boxed{v_p(T_-)\text{ even},\qquad v_p(T_+)\text{ even}.}
\tag{INERT}
\]

### Proof

由 III.2，`p` 不能同时整除 `T_-` 与 `T_+`。

若 `p|T_-`，则 `p|T_-T_+=P_1^2+P_2^2`，故 `p|P1,P2`。不断除去共同的 `p`，得到 norm valuation 为偶数。由于 `p∤T_+`，全部 `p`-valuation 都落在 `T_-`，所以 `v_p(T_-)` 偶。`T_+` 同理。证毕。

Corollary：

\[
\boxed{T_-\text{ 与 }T_+\text{ 各自都是两个平方之和。}}
\]

并且

\[
\boxed{
\operatorname{supp}(\operatorname{sqf}(T_-))
\subseteq\{2\}\cup\{p:p\equiv1\pmod4\}.
}
\tag{SQF-SUPPORT}
\]

---

# III.7 Why no finite square-kernel theorem exists

上述 support theorem 不能加强成 finite prime set。

对任意 prime `p≡1 mod4`，取 `p=a^2+b^2`，`a>b>0`，定义

\[
P_1=4(a^2-b^2),
\qquad
P_2=8ab,
\qquad
P_3=3p,
\qquad
Q_0=5p.
\tag{SQF-FAM}
\]

则

\[
P_1^2+P_2^2=16p^2,
\qquad
P_3^2=9p^2,
\qquad
Q_0^2=25p^2.
\]

该 packet primitive：`P3,Q0` 的公共 prime `p` 不整除 `P1,P2`；且 `P3,Q0` odd，故无 common 2。

而

\[
T_-=2p,
\qquad
T_+=8p,
\]

所以

\[
\boxed{\operatorname{sqf}(T_-)=2p.}
\]

由于 `p` 可遍历所有 `1 mod4` primes，`T_-` 的 square kernel 没有 finite split-prime support。

正式结论：

```text
TMINUS_INERT_EVEN_EXPONENT_THEOREM=PROVED
TMINUS_FINITE_SQUARE_KERNEL_RESTRICTION=FALSE
```

这同时说明纯 Gaussian/norm factorization 不能独自把 primitive sphere finite-ize。

---

# III.8 Factor-pair normalization audit

令 `d=gcd(T_-,T_+)`。Prompt 建议检查是否 `d|P1,P2`。

该命题 **false**。在 family (SQF-FAM) 中

\[
d=2p,
\]

但 `p∤P1P2`，故 `d∤P1,P2`。

失败原因精确：split prime 可以同时进入 rational factors `T_-`,`T_+` 而在 Gaussian factorization 中分配到 conjugate prime directions，不必进入 rational legs 的 gcd。

因此 factor-pair short kill 不能 universalize。

---

# Part IV — Global Selector Elimination

这是 R27 的主信息增益。

# IV.1 Local selector variables

固定 prime `p`（最终只需 `p=2,5`），记

\[
x=v_p(P_1),\quad y=v_p(P_2),\quad z=v_p(P_3),\quad t=v_p(T_-).
\]

对 R26 selector 记

\[
a=v_p(A),\quad w=v_p(W),\quad u=v_p(u_0),\quad s=v_p(g_1^*).
\]

并写

\[
c_2=v_p(C_2)=y-u-w,
\qquad
c_3=v_p(C_3)=z-u-a.
\]

由 divisor selectors：

\[
0\le a\le z,
\quad
0\le w\le y,
\quad
0\le u\le\min(y-w,z-a),
\quad
0\le s\le x.
\]

shape gcds 给 primewise：

\[
a>0\Rightarrow w=c_2=0,
\]

\[
w>0\Rightarrow a=c_3=0.
\tag{SHAPE-p}
\]

定义

\[
r:=v_p(g_0)=\min(u+a+w,x).
\]

master 给

\[
s\ge r.
\]

mu-Smith 给：若 `s>r`，则 `mu` 含 p，于是必须

\[
c_2=c_3=0.
\tag{MU-p}
\]

最后

\[
\boxed{v_p(N_E)=w+s+t-a.}
\tag{OBJ}
\]

我们要消去 `(a,w,u,s)`，求其在这些 frozen necessary gates 下的 exact maximum。

---

# IV.2 Packet-only Decimal Capacity Theorem

## Theorem R27-CAPACITY

对任意 prime `p`，在 `(SEL)+(SGCD)+(MASTER)+(MU)` 的 local p-adic constraints 下，

\[
\boxed{
\max v_p(N_E)
=t+
\begin{cases}
 x+y-z,&y\ge z,\\[2mm]
 \min(x,y)+\max(0,x-z),&y<z.
\end{cases}}
\tag{CAP}
\]

### Proof — Case `y>=z`

下界由

\[
a=0,
\quad u=z,
\quad w=y-z,
\quad c_2=c_3=0,
\quad s=x
\]

实现，得 `t+x+y-z`。

上界：

- 若 `w>0`，shape 强迫 `a=0,c3=0`，故 `u=z` 且 `w<=y-z`，而 `s<=x`，所以 objective `<=t+x+y-z`；
- 若 `w=0`，objective `s+t-a<=x+t<=t+x+y-z`。

故 equality。

### Proof — Case `y<z`

首先 `w>0` 不可能：若 `w>0`，shape 强迫 `a=0,c3=0`，于是 `z=u`，但 `y=u+w+c2>u=z`，矛盾。所以 `w=0`。

若 `a=0`，因 `z>y` 必有 `c3>0`，mu-Smith 不允许 `s>r`，故

\[
s=r\le\min(x,y),
\]

且取 `u=y` 达到 `t+min(x,y)`。

若 `a>0`，shape 强迫 `c2=0`，所以 `u=y`。

- 若 `c3>0`，仍有 `s=r`，objective 不超过 `t+min(x,y)`；
- 唯一允许 `s` 提升到 `x` 的 endpoint 是 `c3=0`，即 `a=z-y`，得到
  \[
  t+x-(z-y)=t+x+y-z.
  \]

两者最大值为

\[
t+\max(\min(x,y),x+y-z)
=t+\min(x,y)+\max(0,x-z).
\]

证毕。

注意：这是对 frozen divisor/shape/master/mu gates 的 exact maximum；tail gates 可能继续降低，但绝不可能提高它。因此它是 full `C26` survivor 的 rigorous upper capacity。

---

# IV.3 Decimal capacity corollary

对 `p=2,5` 定义 `(CAP-p)` 的 `C_p(pi)`。

R26 要求 `10^n|N_E`, `n>=1`，所以任意 full survivor 必须：

\[
\boxed{n\le\mathfrak C_2(\pi),\qquad n\le\mathfrak C_5(\pi).}
\tag{CAP-n}
\]

特别

\[
\boxed{\mathfrak C_2(\pi)\ge1,\qquad\mathfrak C_5(\pi)\ge1.}
\]

这已经把 `A,W,u0,g1*` 在 decimal prime support 层完全 existentially eliminated。

机器 `105-R27-scripts/r27_recon.py` 对

```text
x,y,z = 0..6
t = 0..4
```

共 1715 个 valuation boxes 对 `p=2` 与 `p=5` 分别 exhaustive local selector search，闭式 `CAP` 全部 exact match。该计算只是 theorem regression；证明见上。

---

# IV.4 Primitive simplification of the 2-adic exceptional locus

利用 III.1，可把 `C2(pi)>=1` 化成极简 packet condition。

## Theorem R27-E2

对 primitive sphere：

\[
\boxed{
\mathfrak C_2(\pi)\ge1
\iff
\begin{cases}
P_3\text{ odd}, &\text{or}\\
P_3\text{ even and }v_2(P_{\rm even})>v_2(P_3),
\end{cases}}
\tag{E2}
\]

其中当 `P3` even 时，`P1,P2` 恰有一个 even，`P_even` 指这个 even horizontal leg。

### Proof

- `P3` odd：`z=0`, `P1,P2` both even，且 `t=v2(T_-)>=1`，故 capacity positive。
- `P3` even：`T_-` odd，所以 `t=0`；设 even horizontal leg valuation 为 `e>=1`，另一个 valuation 0。代入 CAP，恰得到 `max(0,e-z)`。

证毕。

因此 2-adic exceptional locus 已经是一个 exact parity/valuation branch，而不是 broad atlas。

---

# IV.5 Primitive simplification of the 5-adic exceptional locus

令

\[
x=v_5(P_1),\quad y=v_5(P_2),\quad z=v_5(P_3),\quad t=v_5(T_-).
\]

由 CAP 与 sphere norm，可完全分类 `C5>=1`。

## Theorem R27-E5

\[
\boxed{
\mathfrak C_5(\pi)\ge1
\iff
\text{以下四 branch 之一成立:}}
\]

1. **BOTH_HORIZONTAL_5**
   \[
   x>0,\ y>0.
   \]
2. **P1_5_EXCESS_OVER_P3**
   \[
   x>0,\ y=0,\ x>z.
   \]
3. **P2_5_EXCESS_OVER_P3**
   \[
   x=0,\ y>0,\ y>z.
   \]
4. **HENSEL_TMINUS**
   \[
   x=y=0,\quad t>0.
   \]

在最后一支，`P1,P2` 都是 5-units，而

\[
5\mid T_-\Rightarrow 5\mid(P_1^2+P_2^2),
\]

故

\[
\boxed{P_1/P_2\equiv\pm2\pmod5,}
\]

更高 depth 恰沿 III.4 的两条 Hensel roots `±iota` lift。

### Proof sketch

- `x,y>0` 时 primitive 强迫 `z=0`，CAP 显然 positive；
- `x>0,y=0` 或反之时，norm 是 5-unit，因此 `t=0`，CAP 化为相应 `max(0,x-z)` / `max(0,y-z)`；
- `x=y=0` 时 CAP exactly equals `t`。

证毕。

因此 5-adic survivor 不再是 arbitrary valuation pattern，而是四个 exact branches，其中唯一没有 horizontal 5-content 的 branch 是两条 Hensel direction。

---

# IV.6 Selector-free Archimedean projection

这是第二条真正的 global selector elimination。

由 R26 delta window：

\[
\frac{AP_2}{WP_3}>10^{\delta-1}.
\]

又 `n+delta>=2`，故 `delta-1>=1-n`，于是

\[
\frac{AP_2}{WP_3}>10^{1-n},
\]

即

\[
\boxed{10^n>\frac{10WP_3}{AP_2}.}
\tag{A1}
\]

另一方面 `10^nE=N_E`, `E>=1`：

\[
10^n\le N_E=\frac{Wg_1^*T_-}{A}.
\tag{A2}
\]

合并 A1/A2 并消去 `A,W`：

\[
g_1^*P_2T_->10P_3.
\]

而 `g1*|P1`，所以 `g1*<=P1`：

\[
\boxed{P_1P_2T_->10P_3.}
\tag{ARCH again}
\]

这是完全 packet-only 的 necessary condition。

它也包含 prompt 要求的 simple size audit，但比单独

\[
Wg_1^*T_-\le P_1P_2T_-
\]

更有效，因为把 delta/exponent feasibility 一并焊入。

---

# Part V — Exceptional Locus

# V.1 Definition

定义

\[
\boxed{
\mathscr E_{27}
=
\left\{\pi:
\begin{array}{l}
\pi\text{ positive primitive sphere},\\
\mathfrak C_2(\pi)\ge1,\\
\mathfrak C_5(\pi)\ge1,\\
P_1P_2(Q_0-P_3)>10P_3
\end{array}
\right\}.
}
\]

由 IV.3 + IV.6：

## Theorem R27-EXCEPTIONAL-CONTAINMENT

\[
\boxed{\mathscr P_{26}\subseteq\mathscr E_{27}.}
\]

这是本轮 Verdict 4 的 exact mathematics。

---

# V.2 Strictness

`E27` 不是 entire primitive sphere。

例如

\[
(P_1,P_2,P_3,Q_0)=(1,2,2,3)
\]

primitive sphere，且 `P3` even；even horizontal leg 是 `P2`，

\[
v_2(P_2)=v_2(P_3)=1,
\]

故 `C2=0`，不在 `E27`。

因此

\[
\boxed{\mathscr E_{27}\subsetneq\{\text{all primitive positive spheres}\}.}
\]

---

# V.3 `E27` remains infinite — no global finite reduction

为防止把“exceptional”偷换成“finite”，构造无限 family。

取整数 `c` 满足：

\[
c\ge8,\qquad c\equiv0\pmod2,
\]

\[
c\equiv2\text{ or }3\pmod5,
\]

\[
13\nmid c/2.
\]

定义

\[
\boxed{
P_1=c,\qquad
P_2=5c,\qquad
P_3=\frac{c^2-26}{2},\qquad
Q_0=\frac{c^2+26}{2}.
}
\tag{E27-INF}
\]

则

\[
T_-=26,
\qquad
T_+=c^2,
\]

且

\[
P_1^2+P_2^2=26c^2=T_-T_+.
\]

primitive：写 `c=2d`，

\[
\gcd(c,P_3)=\gcd(2d,2d^2-13)=\gcd(d,13)=1
\]

由 `13∤d`；故全 packet primitive。

2-adic：`P3,Q0` both odd，所以 E2 automatic pass。

5-adic：`5∤P1`, `v5(P2)=1`，且 `c^2≡4 mod5`, `26≡1 mod5`，故 `5∤P3`; 落在 `P2_5_EXCESS_OVER_P3` branch。

Arch：

\[
P_1P_2T_-=130c^2
>5(c^2-26)=10P_3.
\]

因此整族

\[
\boxed{\pi(c)\in\mathscr E_{27}}
\]

且 `c` 有无限多个合法值。

正式签：

```text
GLOBAL_PRIMITIVE_SPHERE_FINITE_REDUCTION=NO
E27_INFINITE_FAMILY=PROVED
```

这不是 R27 failure；它精确定位了本轮 packet-only projection 的极限。

---

# Part VI — R26 Certificate Re-entry

# VI.1 We reinsert the full dual-decimal relation

通过 E2/E5/ARCH 并不等价于 `C26(pi)=1`。真正 survivor 仍必须存在 selectors/exponents 满足完整

\[
R_n=10^{n+\delta-\rho}S_{m,\rho}
\]

并继续过 TC2–TC4。

因此 R27 的正确 remaining set 是

\[
\boxed{
\mathscr P_{26}
=
\mathscr E_{27}
\cap
\{\pi:\exists\text{ R26 tuple passing TC1--TC4}\}.
}
\]

这里第一项已是 packet-only thin locus；第二项仍是一条 moving dual-decimal/source incidence。

R27 没有找到把 TC1 全量化消元成 fixed finite residue family 的正确 theorem，因此没有伪造 global closure。

---

# VI.2 Exact bounded reconnaissance — scope and completeness

运行：

```text
105-R27-scripts/r27_recon.py
```

范围：

\[
\boxed{Q_0\le500}
\]

枚举 **全部有向 positive primitive sphere packets**，并对每个 packet 完整枚举 R26 archive 中公开的：

- `A|P3`;
- `W|P2`;
- `u0|gcd(P2/W,P3/A)`;
- `g1*|P1`;
- `1<=n<=nu10(NE)`;
- `delta in D_sigma`;
- complete `(rho,m)` exponent simplex;
- exact TC1 CDN equality.

对 TC1 hits 再重放 R24 frozen pre-support gates：shape gcd、positive radial box、master、mu-Smith、tail-g1、tail-Smith。

**没有**把 TC2 denominator q-successor / TC4 downstream full source replay 重新实现；因为没有一个 raw TC1 hit 能穿过这些更早的 R24 support gates。

因此 bounded result 的精确语义是：

```text
COMPLETE_IN_BOUND_FOR_PRIMITIVE_PACKET_ENUMERATION=YES
COMPLETE_IN_BOUND_FOR_R26_PUBLIC_SELECTOR_PLUS_TC1=YES
R24_SUPPORT_REPLAY_FOR_EACH_TC1_HIT=YES
FULL_TC2_TC4_REPLAY_IMPLEMENTED=NO_NOT_REACHED
GLOBAL_NONEXISTENCE_INFERENCE=FORBIDDEN
```

---

# VI.3 Certified bounded counts

机器 log / registries 记录：

```text
BOUND_Q0=500
ORIENTED_PRIMITIVE_PACKETS=50910
CAP2_GE1=22586
CAP5_GE1=23492
CAP_BOTH_GE1=10352
E27_CAP_ARCH=10253
RAW_TC1_HIT_PACKETS=4
RAW_TC1_HIT_TUPLES=5
R24_SUPPORT_PLUS_TC1=0
TOTAL_SELECTOR_LABELS_VISITED=20429774
TOTAL_EXPONENT_RECORDS_VISITED=1477548
```

这些 counts 均有 CSV certificate；不从高度 `500` 外推。

---

# VI.4 The five raw TC1 tuples and exact first deaths

完整 registry 位于 `105-R27-survivor-registry.csv`。

五个 raw TC1 tuples：

1. `pi=(20,120,123,173)`
   - `(A,W,u0,g1*,n,delta,rho,m,g)=(1,2,1,10,2,0,2,1,0)`
   - first death: `POSITIVE_RADIAL_BOX`, exact `Ulo=1>0=Uhi`.

2. `pi=(200,365,104,429)`
   - `(13,1,1,40,1,2,2,1,1)`
   - first death: `MU_SMITH`; this exactly reappears as R24 historical G=10 diagnostic packet.

3. `pi=(48,436,75,445)`
   - `(3,4,1,24,1,1,2,1,0)`
   - first death: `POSITIVE_RADIAL_BOX`;该 packet 是历史 R7D PSDG witness，但不是 R27 full carrier survivor。

4. `pi=(435,160,168,493)`
   - `(3,2,2,435,1,1,2,1,0)`
   - first death: `SHAPE_GCD`.

5. 同一 packet
   - `(6,4,1,435,1,1,2,1,0)`
   - first death: `SHAPE_GCD`.

因此：

\[
\boxed{
Q_0\le500\text{ 的 complete-in-bound TC1 reconnaissance 中，}
0\text{ tuple 穿过 R24 support.}}
\]

这只是一条 regression certificate，不是 height-bounded global theorem。

---

# Part VII — Extinction / Finite Reduction / Witness

# VII.1 Short-kill audit

## valuation imbalance

成功局部 universalize：若 `C2(pi)=0` 或 `C5(pi)=0`，则任意 selectors 都有 `v2(NE)<1` 或 `v5(NE)<1`，不能存在 `n>=1`。

## primitive contradiction

成功得到 `Q0` odd、exact parity type、以及 `gcd(Q0,P3)` 不含 inert primes。

## divisor-size contradiction

成功投影成 selector-free

\[
P_1P_2T_->10P_3.
\]

不是 universal kill，但是真 packet-only filter。

## factor-pair contradiction

失败为 universal route。`d=gcd(T_-,T_+)` 不必整除 `P1,P2`; split-prime family (SQF-FAM) 提供无限 counterexamples。

## parity contradiction

成功完成 exact branch classification，但不能独立灭绝所有 packets。

## Gaussian inert-prime contradiction

成功证明 inert primes 在 `T_±` 中 exponent even，但 split primes 任意，故不能 global kill。

---

# VII.2 Information-gain audit

### `T_-` factorization

**INFORMATION_GAIN=YES, BUT NONFINITE.**

得到 exact gcd / inert exponent / sum-of-two-squares structure；但 split-prime kernel unlimited。

### 2/5-adic analysis

**INFORMATION_GAIN=YES.**

不只是 valuation atlas；它通过 local selector maximization 把 `A,W,u0,g1*` 消掉，产生 packet-only capacities `C2,C5` 与 exact E2/E5 branches。

### Gaussian factorization

**INFORMATION_GAIN=LIMITED_POSITIVE.**

Gaussian gcd 与 inert support 被定理化；但任意 `1 mod4` primes 的 family 证明其不能有限化 sphere。

### selector elimination

**INFORMATION_GAIN=YES_PARTIAL.**

Decimal prime capacities与 size gate已完全 packet-only；full TC1 moving decimal incidence尚未消元。

### remaining infinite degree

不再准确描述为“整个 primitive sphere”。更精确是：

\[
\boxed{
\text{primitive spheres in }\mathscr E_{27}
\text{ that also hit the full R26 dual-decimal/support successor incidence.}
}
\]

即 E2/E5/ARCH 三重 exceptional locus上的 moving TC1–TC4 incidence。

---

# VII.3 Terminal verdict

本轮不能签：

```text
STRICT_A1_UNLIFTABILITY_PROVED=YES
FULL_STRICT_A1_WITNESS_FOUND=YES
GLOBAL_PRIMITIVE_SPHERE_FINITE_REDUCTION=YES
```

本轮正式签：

```text
R1_TO_R26_STATE_FROZEN=YES
R26_AUTHORITATIVE_ARCHIVE_READ=YES
R26_SHA256_COMPANION_READ=YES

PRIMITIVE_SPHERE_PARITY_THEOREM=PROVED
TPM_GCD_STRUCTURE_THEOREM=PROVED
TPM_COMMON_GCD_INERT_SUPPORT=EMPTY
V2_SUM_OF_TWO_SQUARES_CLASSIFICATION=PROVED
V5_SUM_OF_TWO_SQUARES_HENSEL_CLASSIFICATION=PROVED
GAUSSIAN_CONJUGATE_GCD_THEOREM=PROVED
TPM_INERT_PRIME_EVEN_EXPONENT_THEOREM=PROVED
TMINUS_SUM_OF_TWO_SQUARES=PROVED
TMINUS_FINITE_SQUARE_KERNEL_RESTRICTION=FALSE

PACKET_ONLY_DECIMAL_CAPACITY_THEOREM=PROVED
R26_2ADIC_SELECTOR_ELIMINATION=PROVED
R26_5ADIC_SELECTOR_ELIMINATION=PROVED
PRIMITIVE_E2_BRANCH_CLASSIFICATION=PROVED
PRIMITIVE_E5_BRANCH_CLASSIFICATION=PROVED
PACKET_ONLY_ARCHIMEDEAN_GATE=PROVED

PRIMITIVE_SPHERE_EXCEPTIONAL_LOCUS_COLLAPSE=YES
E27_EXACT_DEFINITION=C2>=1__C5>=1__P1*P2*Tminus>10*P3
P26_SUBSET_E27=PROVED
E27_STRICT_SUBLOCUS=PROVED
E27_INFINITE_FAMILY=PROVED

GLOBAL_PRIMITIVE_SPHERE_FINITE_REDUCTION=NO
STRICT_A1_UNLIFTABILITY_PROVED=NO
FULL_STRICT_A1_WITNESS_FOUND=NO

R26_FULL_DUAL_DECIMAL_REENTERED=YES
FULL_TC1_EXISTENTIAL_ELIMINATION=OPEN
BOUNDED_Q0_500_TC1_RECON_COMPLETE=YES
BOUNDED_RAW_TC1_HIT_TUPLES=5
BOUNDED_R24_SUPPORT_PLUS_TC1=0
BOUNDED_RESULT_USED_AS_GLOBAL_THEOREM=NO

TERMINAL_VERDICT=PRIMITIVE_SPHERE_EXCEPTIONAL_LOCUS_COLLAPSE=YES
```

---

# Final Eight Questions

## Q1. `gcd(Q0-P3,Q0+P3)` 究竟有哪些可能？

令 `c=gcd(Q0,P3)`。则 `c` odd，且其所有 prime factors 都 `≡1 mod4`。精确地：

\[
\boxed{
\gcd(Q_0-P_3,Q_0+P_3)=
\begin{cases}
 c,&P_3\text{ even},\\
 2c,&P_3\text{ odd}.
\end{cases}}
\]

`c` 不必等于 1，因此 gcd 不局限于 1 或 2。

## Q2. `T_-` 的 2/5-adic content 能否由 `(P1,P2)` 全局控制？

**能精确控制 norm side，但不能给 universal bounded valuation。**

- 2-adic norm valuation由 `(v2(P1),v2(P2))` exact 决定；
- 5-adic unequal case exact，equal case只剩两条 Hensel branches；
- 结合 selectors后，R27 进一步得到 packet-only capacities `C2(pi),C5(pi)`。

所以“控制”成立，但值本身可随 primitive family 无界增长。

## Q3. primitive condition 是否迫使 `T_-` 具有受限 square kernel？

**部分。** 所有 `3 mod4` primes 在 `T_-` 中 exponent 必为 even，因此

\[
\operatorname{sqf}(T_-)
\text{ 只含 }2\text{ 与 }1\pmod4\text{ primes}.
\]

但不存在 finite prime support：对任意 `p≡1 mod4` 都有 primitive family 使 `sqf(T_-)=2p`。

## Q4. R26 selectors 能否 existentially eliminated？

**在 decimal-prime capacity 与 size 层面 YES；在完整 TC1–TC4 层面 NO。**

已经消掉 `A,W,u0,g1*` 得到 `C2,C5,ARCH` packet-only necessary conditions；full CDN moving incidence 尚未得到 packet-only equivalent closed form。

## Q5. `C26(pi)=1` 是否迫使 `pi` 落入严格更薄 congruence/valuation locus？

**YES.**

\[
\boxed{\mathscr P_{26}\subseteq\mathscr E_{27}\subsetneq\text{primitive sphere}.}
\]

其中 E2 是 exact dyadic branch，E5 是四个 exact 5-adic branches（含两条 Hensel directions），再交 ARCH。

## Q6. fixed-packet finite theorem 能否升级成 global finite primitive-packet theorem？

**本轮 NO。**

显式 infinite family (E27-INF) 全部通过 R27 packet-only exceptional gates，因此没有 global height/parameter bound。

## Q7. 是否发现 genuine survivor / witness？

**没有 full Strict-A1 witness。**

`Q0<=500` reconnaissance 有 5 个 raw TC1 tuples，但全部在 R24 frozen support gates 前死亡；该 bounded no-hit 不作 global inference。

## Q8. 如果今天必须结束 105，剩下的唯一无限对象能否比“primitive sphere locus”描述得更精确？

**YES.** 当前最精确描述为：

\[
\boxed{
\mathscr E_{27}
\cap
\{\text{full R26 dual-decimal TC1--TC4 incidence hits}\}.
}
\]

即：

> 先落入 exact 2-adic exceptional branch；
> 再落入四类 exact 5-adic/Hensel branch之一；
> 再满足 `P1 P2 (Q0-P3)>10P3`；
> 最后还必须命中 R26 moving dual-decimal collision 与 source successor。

所以 R27 已把“最后无限 primitive sphere”压成一个真正更薄的 **decimal-capacity exceptional sphere locus + moving CDN incidence**，但尚未把最后这条 incidence 全局消灭或有限化。

---

# Archive Note

所有有限 counts 的 authoritative machine evidence 在：

- `105-R27-execution.log`
- `105-R27-certificate-registry.csv`
- `105-R27-R26-survivor-counts.csv`
- `105-R27-survivor-registry.csv`

所有 theorem 的 proof responsibility 在本主归档；finite reconnaissance 只负责 regression / counterexample discovery / bounded audit，不替代证明。
