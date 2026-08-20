# J2-55-R1 — A-Residue Primitive Root-Lift Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第一轮 / 统一终端线第十一轮 — \(A\)-Residue Primitive Root Lift × Singular-GCD Exhaustion × Actual-Root Rigidity  
**Inherited primary sources:** `A1_J2_PRCC10_Report.md`, `A1_J2_GRFC9_Report.md`, `A1_J2_RCRF4_Report.md`, `A1_J2_CZDR_Report.md`, `A1_J2_DCDC5_Report.md`  
**New symbolic audit:** `J2-55-R1-A-Root-Lift-symbolic.py`  
**New symbolic certificate:** `J2-55-R1-A-Root-Lift-certificate.txt`

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

本轮没有得到

\[
J=2\Longrightarrow\varnothing.
\]

但本轮对 55 campaign 第一目标——**actual root \(a_1\) 的 \(A\)-adic rigidification**——完成了比“普通 Hensel lifting”更精确的终端分类。

最重要的结论是：

\[
\boxed{
\textbf{mod }A\textbf{ 没有 singular branch。}
}
\]

因为 inherited primitive-root residue 本身就是

\[
\boxed{
Ka_1\equiv-Z\pmod A,
}
\tag{AROOT}
\]

而

\[
\gcd(K,A)=1.
\]

所以每一个 admissible structural profile 都有唯一的第一 \(A\)-digit：

\[
\boxed{
a_1\equiv r_A:=-K^{-1}Z\pmod A,
\qquad 0\le r_A<A.
}
\tag{ARL-1}
\]

真正的 singularity **只从 \(A\to A^2\) lift 开始**，并且其退化度恰为

\[
\boxed{
d_A:=\gcd(Q'(r_A),A)=\gcd(D_2,A).
}
\tag{DEG}
\]

这里

\[
Q(x)=AH^2x^2-2uKD_2x+\widetilde F,
\qquad
\widetilde F=A\mathcal X^2+ZD_2.
\]

本轮的核心新解释是：

\[
\boxed{
\textbf{derivative degeneracy = polynomial common-content degeneracy.}
}
\]

若

\[
d=d_A=\gcd(A,D_2),
\]

则不是只看到“导数不可逆”，而是整个根多项式都可精确除以 \(d\)：

\[
\boxed{
Q(x)=d\,Q^\sharp(x),
}
\tag{CONTENT}
\]

其中

\[
A^\sharp=\frac Ad,
\qquad
D_2^\sharp=\frac{D_2}{d},
\qquad
\gcd(A^\sharp,D_2^\sharp)=1,
\]

\[
\boxed{
Q^\sharp(x)
=A^\sharp H^2x^2
-2uKD_2^\sharp x
+A^\sharp\mathcal X^2
+ZD_2^\sharp.
}
\tag{QSH}
\]

而且

\[
\boxed{
(Q^\sharp)'(r_A)\equiv KD_2^\sharp\pmod{A^\sharp},
}
\]

故 deflated derivative 自动 primitive：

\[
\boxed{
\gcd((Q^\sharp)'(r_A),A^\sharp)=1.
}
\tag{DEF-PRIM}
\]

因此 singular branch 不再是模糊的 “Hensel failure”，而被完全分类为：

\[
\boxed{
\textbf{one primitive lift modulo }A/d
\quad+\quad
\textbf{exactly }d\textbf{ classes modulo }A.
}
\]

其存在条件正是 inherited PRCC10 条件

\[
\boxed{d\mid T_A,}
\tag{SOLV}
\]

其中

\[
\boxed{
T_A:=\frac{Q(r_A)}A
=H^2r_A^2+\mathcal X^2-KD_2r_A+D_2n_A,
}
\tag{TA}
\]

\[
\boxed{
n_A:=\frac{Kr_A+Z}{A}\in\mathbf Z.
}
\]

于是本轮的 global \(A^2\)-classification 为：

\[
\boxed{
\begin{array}{ll}
d_A=1:& \text{唯一 }r_{A^2}\pmod{A^2};\\[1mm]
d_A>1,\,d_A\nmid T_A:& \text{无 }A^2\text{-lift};\\[1mm]
d_A>1,\,d_A\mid T_A:& \text{恰有 }d_A\text{ 个 canonical }A^2\text{-classes}.
\end{array}}
\tag{ARL-3}
\]

所以用户预定的“对每个 structural profile 至多一个 lift mod \(A^2\)”在全局上是**假的**。旧 exact diagnostic 已经给出真实 counterexamples：26 个 derivative-degenerate cell 中有 6 个 \(d_A=3\) 的状态成功抬到 \(A^2\)，每个有三个 lift class。不能删除这个分支。

不过本轮进一步得到一个新的 prime-power singular signature。若

\[
p^e\Vert A,
\qquad
s:=\min(e,v_p(D_2))>0,
\]

则 local lift 必须满足

\[
\boxed{v_p(T_A)\ge s.}
\tag{P-SOLV}
\]

并且这强迫

\[
\boxed{
(GZ)^2+(2K\mathcal X)^2\equiv0\pmod{p^s}.
}
\tag{P-SOS}
\]

特别地，若

\[
p\equiv3\pmod4,
\]

则令

\[
r_p:=\left\lceil\frac s2\right\rceil,
\]

有

\[
\boxed{
p^{r_p}\mid Z,\ \mathcal X,\ N,\ a_3,\ a_1.}
\tag{BADP-ALIGN}
\]

若同时

\[
p\nmid q+4,
\]

则进一步

\[
\boxed{p^{r_p}\mid t.}
\tag{BADP-T}
\]

这没有在本轮形成 contradiction，但把 singular branch 压成了一个非常明确的 **scale-alignment branch**。

另一方面，\(p=2,5\) 根本不会成为 \(A\)-prime branch，因为 inherited theorem 已有

\[
\boxed{\gcd(A,10)=1.}
\]

所以本轮没有重新开启 generic \(2/5\)-phase。事实上 \(H,K,10^\ell\) 在模 \(A\) 上都是 units；\(A^2\)-lift 中 quadratic correction 消失的原因是它带 \(A^3\)，不是 decimal valuation。

最后，本轮得到一个新的 **regular actual-root singleton subchamber**。令

\[
C_\ell:=\frac{1299}{500}+10^{-\ell}.
\]

inherited root-carry bound 给出

\[
\boxed{\frac{a_1}{A^2}<C_\ell q.}
\tag{CARRY-SIZE}
\]

若

\[
\boxed{d_A=1,
\qquad A>C_\ell q,}
\tag{A3-THRESH}
\]

则唯一继续 lift 到 \(A^3\) 后，必有

\[
0<a_1<A^3,
\qquad
a_1\equiv r_{A^3}\pmod{A^3},
\]

所以

\[
\boxed{a_1=r_{A^3}}
\]

或该 profile 根本无 actual root。因此：

\[
\boxed{
\#\{a_1\text{ actual root for the fixed regular profile}\}\le1.
}
\tag{ARL-4R}
\]

对当前 live \(\ell\ge6\)，一个方便的统一 sufficient condition 是

\[
\boxed{
q^2<\frac{2,000,000}{2,598,001}(G+1)
\Longrightarrow
A>C_\ell q,
}
\tag{A3-SUFF}
\]

即近似

\[
q<0.877395\sqrt{G+1}.
\]

这不是全 J2 closure，但是真正把一大片 regular outer-divisor chamber 从“\(O(q)\) root carries”压成“至多一个 actual integer root”。

因此本轮精确 surviving obstruction 是：

\[
\boxed{
\begin{array}{c}
\textbf{large-}q\textbf{ regular carry branch}\[1mm]
\text{or}\[1mm]
\textbf{content-singular branch }d_A>1,\ d_A\mid T_A,
\end{array}}
\]

再与

\[
\boxed{
(a_1)^2\equiv Z^2\pmod u
}
\]

以及 CQRF / exact carry polynomial 同步碰撞。

这已经足够进入 55 第二轮的 \(u\)-square synchronization；不需要也不应该再发明新的 root quotient。

---

# Part II — Inherited Exact Root Equations

本节只恢复已在 archive 中出现、且本轮实际使用的 exact identities。

## 2.1 Outer / radial data

当前 live J2 frontier 已处于 negative deficiency sector，并冻结

\[
G=10^g,
\qquad
H=\frac G2,
\qquad
K=10^k,
\qquad
\ell=2g-k\ge6,
\]

\[
uq=G+1,
\qquad
A=2u+1,
\qquad
M=q(q+4).
\]

RCE reconstruction：

\[
\boxed{
2Aa_3=q(G-1)Z-N,
}
\tag{RCE1}
\]

\[
\boxed{
(G-1)t=2(q+4)a_3+qN,
}
\tag{RCE2}
\]

\[
\boxed{
q(q+4)Z=At-2N.
}
\tag{RCE3}
\]

故

\[
\boxed{
a_3=\frac{(G-1)t-qN}{2(q+4)},
}
\]

\[
\boxed{
Z=\frac{At-2N}{q(q+4)},
}
\]

\[
\boxed{
\mathcal X=\frac{Z+uN}{2},
\qquad
D_2=ua_3+G\mathcal X.
}
\tag{RECON}
\]

CQRF clearing data：

\[
R:=At-2N,
\qquad
Y:=R+uNM,
\]

\[
E:=uq((G-1)t-qN)+GY,
\]

于是

\[
Z=\frac RM,
\qquad
\mathcal X=\frac{Y}{2M},
\qquad
D_2=\frac{E}{2M}.
\]

## 2.2 Root-factor system

actual root：

\[
\boxed{x:=a_1.}
\]

定义

\[
\boxed{
\widetilde F:=A\mathcal X^2+ZD_2.
}
\]

inherited radial root quadratic：

\[
\boxed{
Q(x):=AH^2x^2-2uKD_2x+\widetilde F=0.
}
\tag{RQ}
\]

同一方程的 CQRF-cleared 形式为

\[
\boxed{
AG^2M^2x^2-4uKEMx+AY^2+2RE=0.
}
\tag{CQRF-Q}
\]

两式不是独立 root equations；后式只是前式乘上清分母因子后的同一多项式。

root-factor pair：

\[
\boxed{
a_1\Lambda=\widetilde F,
}
\tag{RF1}
\]

\[
\boxed{
AH^2a_1+\Lambda=2uKD_2.
}
\tag{RF2}
\]

## 2.3 GRFQE / \(\kappa=a_1\)

上一轮之前引入的 GRFQ variable 满足

\[
A10^\ell\kappa^2-8uD_2\kappa+8\widehat\Omega=0,
\qquad
\widehat\Omega=\frac{\widetilde F}{2K}.
\]

清分母以后是

\[
AG^2\kappa^2-8uKD_2\kappa+4\widetilde F=0,
\]

即 \(4Q(\kappa)=0\)。而 frozen exact root reconstruction 已经严格给出

\[
\boxed{\kappa=a_1.}
\]

所以本轮不保留 \(\kappa\) 作为坐标。

## 2.4 Primitive root residues

两个 inherited primitive-root conditions 是

\[
\boxed{Ka_1\equiv-Z\pmod A,}
\tag{A-ROOT}
\]

\[
\boxed{a_1^2\equiv Z^2\pmod u.}
\tag{U-SQ}
\]

重要 dependency audit：

- A-ROOT 来自 primitive recovery，并非简单地假设 \(Q\equiv0\pmod A\) 后约掉 \(D_2\)；
- U-SQ 在 algebraic 层面正是 \(Q(x)=0\pmod u\)，不是另一条概率独立的 root equation；
- 在 \(d_A>1\) 时，A-ROOT 比 \(Q(x)\equiv0\pmod A\) 更强。

## 2.5 Digit / interval data

严格恢复到的 actual-root lower bound 是

\[
\boxed{a_1>\frac{AG}{10}.}
\tag{DRL}
\]

**没有**恢复到已经证明的

\[
a_1<AG.
\]

因此本轮禁止使用该 desired upper endpoint。

合法 upper bound 来自 complementary factor positivity：

\[
\Lambda=2uKD_2-AH^2a_1>0,
\]

所以

\[
\boxed{
a_1<\frac{8uD_2}{A10^\ell}.
}
\tag{ROOT-UP}
\]

因此 actual root necessary interval 是

\[
\boxed{
I_{a_1}
=
\left(
\frac{AG}{10},
\frac{8uD_2}{A10^\ell}
\right).
}
\tag{IA1}
\]

## 2.6 \(D_1\) audit

当前 terminal root polynomial / CQRF ledger 中真正参与 root coefficient 的量是 \(D_2\)。没有恢复到一个与 \(D_2\) 平行、且独立进入 \(Q(a_1)\) 的 live \(D_1\) coefficient。

因此本轮不凭 prompt 的 schematic notation 人为制造 \(D_1\)。

---

# Part III — Root Equation Ledger

| Object | Exact formula | \(A\)-support / gcd | Role |
|---|---|---|---|
| \(A\) | \(2u+1\) | \(\gcd(A,10)=1\), \(\gcd(A,u)=1\) | root modulus |
| \(K\) | \(10^k\) | \(\gcd(K,A)=1\) | primitive linear coefficient |
| \(H\) | \(G/2\) | \(\gcd(H,A)=1\) | quadratic coefficient unit part |
| \(Z\) | \((At-2N)/M\) | no global \(\gcd(Z,A)=1\) theorem | A-root constant |
| \(\mathcal X\) | \((Z+uN)/2\) | ten-unit on legal states; may share odd primes with \(A\) | root constant data |
| \(D_2\) | \(ua_3+G\mathcal X=E/(2M)\) | ten-unit; \(d_A=\gcd(D_2,A)\) may be \(>1\) | derivative degeneracy |
| \(\widetilde F\) | \(A\mathcal X^2+ZD_2\) | if \(d\mid A,D_2\), then \(d\mid\widetilde F\) | constant coefficient |
| \(Q(x)\) | \(AH^2x^2-2uKD_2x+\widetilde F\) | exact integer quadratic | actual-root equation |
| A-ROOT | \(Kx+Z\equiv0\pmod A\) | coefficient \(K\) always invertible | unconditional unique mod-A class |
| \(T_A\) | \(Q(r_A)/A\) | integer | first A-adic carry |
| \(Q'(r_A)\) | \(2AH^2r_A-2uKD_2\) | \(\equiv KD_2\pmod A\) | A→A² lift coefficient |

The key distinction is therefore:

\[
\boxed{
\text{primitive A-root coefficient }K\text{ is always regular},
}
\]

but

\[
\boxed{
\text{quadratic derivative coefficient has degeneracy }d_A=\gcd(D_2,A).
}
\]

---

# Part IV — mod \(A\): Unconditional Primitive Root Class

From A-ROOT,

\[
Ka_1\equiv-Z\pmod A.
\]

Because

\[
K=10^k,
\qquad
\gcd(A,10)=1,
\]

we have

\[
\boxed{\gcd(K,A)=1.}
\]

Thus there is no need to introduce

\[
\delta_A=\gcd(K,A)
\]

as a branch variable: it is identically \(1\).

Define

\[
\boxed{
r_A:=(-K^{-1}Z)\bmod A,
\qquad0\le r_A<A.
}
\]

Then

\[
\boxed{a_1\equiv r_A\pmod A.}
\]

This proves **ARL-1** globally.

A useful gcd corollary is

\[
\boxed{
\gcd(r_A,A)=\gcd(Z,A),
}
\tag{RA-GCD}
\]

because multiplication by the \(A\)-unit \(K\) preserves gcd with \(A\).

The canonical structural formula can also be written as

\[
\boxed{
r_A
\equiv
-10^{-k}\,rac{At-2N}{q(q+4)}
\pmod A,
}
\]

where the fraction denotes the already-reconstructed integer \(Z\), not modular division by \(q(q+4)\).

### Important singularity audit

Reducing the quadratic itself gives

\[
Q(x)\equiv D_2(Kx+Z)\pmod A.
\]

If \(\gcd(D_2,A)=1\), Q mod A alone recovers A-ROOT.

If \(\gcd(D_2,A)>1\), Q mod A has extra spurious classes. Therefore the correct first root class comes from **primitive A-ROOT**, not from cancelling \(D_2\) in Q modulo A.

This resolves the prompt's first singular-gcd concern completely:

\[
\boxed{
\textbf{mod }A\textbf{ regularity is unconditional; derivative singularity is a later phenomenon.}
}
\]

---

# Part V — Exact First Carry \(T_A\)

Since

\[
Kr_A+Z=An_A
\]

for

\[
\boxed{n_A:=\frac{Kr_A+Z}{A}\in\mathbf Z,}
\]

substituting \(r_A\) into Q gives

\[
\begin{aligned}
Q(r_A)
&=AH^2r_A^2-2uKD_2r_A+A\mathcal X^2+ZD_2\\
&=A\left(H^2r_A^2+\mathcal X^2-KD_2r_A+D_2n_A\right),
\end{aligned}
\]

where \(-2u=A(-1)+1\) has been used in the exact rearrangement.

Hence

\[
\boxed{
T_A:=\frac{Q(r_A)}A
=H^2r_A^2+\mathcal X^2-KD_2r_A+D_2n_A.
}
\]

This is the exact object controlling the second A-digit.

A second inherited CQRF identity is

\[
4AM^2T_A
=
AG^2M^2r_A^2
-4uKEMr_A
+AY^2+2RE,
\]

so \(T_A\) is not an opaque auxiliary carry: it is exactly CQRF evaluated at the primitive first root digit, divided by its forced \(A\)-factor.

---

# Part VI — A→A² Lift and Complete Composite-Modulus Classification

Write

\[
a_1=r_A+Ac.
\]

Because Q is quadratic,

\[
\boxed{
Q(r_A+Ac)
=Q(r_A)+AcQ'(r_A)+A^3H^2c^2.
}
\tag{TAYLOR}
\]

Modulo \(A^2\), the last term vanishes identically. Since \(Q(r_A)=AT_A\), a necessary and sufficient congruence for the primitive A-class to lift to a Q-root modulo \(A^2\) is

\[
\boxed{
T_A+Q'(r_A)c\equiv0\pmod A.
}
\tag{LIFT-A2}
\]

Derivative:

\[
Q'(r_A)=2AH^2r_A-2uKD_2.
\]

As

\[
-2u\equiv1\pmod A,
\]

we have

\[
\boxed{
Q'(r_A)\equiv KD_2\pmod A.
}
\tag{DER}
\]

Since K is an A-unit,

\[
\boxed{
\gcd(Q'(r_A),A)=\gcd(D_2,A)=d_A.
}
\]

Therefore linear congruence theory gives the full answer:

### Regular branch

If

\[
d_A=1,
\]

then

\[
\boxed{
c\equiv c_A:=-T_AQ'(r_A)^{-1}\pmod A.}
\]

于是

\[
\boxed{
r_{A^2}=r_A+Ac_A\pmod{A^2}}
\]

is unique.

### Singular branch

If

\[
d_A>1,
\]

then lift exists iff

\[
\boxed{d_A\mid T_A.}
\]

If this fails, the primitive A-root dies before any u-side condition.

If it holds, divide by \(d_A\):

\[
\boxed{
\frac{T_A}{d_A}
+
\frac{Q'(r_A)}{d_A}c
\equiv0
\pmod{A/d_A}.
}
\tag{DEFLIFT}
\]

and the coefficient is invertible modulo \(A/d_A\). Thus c is unique modulo \(A/d_A\), hence exactly \(d_A\) classes modulo A.

This recovers PRCC10, but the next section explains *why* this is the right classification.

---

# Part VII — New: Singular-Content Deflation Theorem

Let

\[
\boxed{d:=\gcd(A,D_2).}
\]

Then

\[
d\mid A,
\qquad
d\mid D_2.
\]

Also

\[
\widetilde F=A\mathcal X^2+ZD_2
\]

implies

\[
\boxed{d\mid\widetilde F.}
\]

Therefore every coefficient of Q is divisible by d:

\[
Q(x)=AH^2x^2-2uKD_2x+\widetilde F.
\]

Define

\[
A^\sharp=\frac Ad,
\qquad
D_2^\sharp=\frac{D_2}{d}.
\]

Then

\[
\boxed{
Q(x)=dQ^\sharp(x),
}
\]

with

\[
\boxed{
Q^\sharp(x)
=A^\sharp H^2x^2
-2uKD_2^\sharp x
+A^\sharp\mathcal X^2
+ZD_2^\sharp.
}
\]

By definition of d,

\[
\boxed{\gcd(A^\sharp,D_2^\sharp)=1.}
\]

Differentiate:

\[
(Q^\sharp)'(r_A)
=2A^\sharp H^2r_A-2uKD_2^\sharp.
\]

Since

\[
A=dA^\sharp=2u+1,
\]

we have modulo \(A^\sharp\)

\[
-2u=1-dA^\sharp\equiv1,
\]

hence

\[
\boxed{
(Q^\sharp)'(r_A)
\equiv KD_2^\sharp\pmod{A^\sharp}.
}
\]

因为 K 是 unit 且 \(\gcd(D_2^\sharp,A^\sharp)=1\)，

\[
\boxed{
\gcd((Q^\sharp)'(r_A),A^\sharp)=1.
}
\]

### Interpretation

The singularity has no mysterious residual derivative defect after content removal.

\[
\boxed{
\textbf{All A-derivative degeneracy is exactly coefficient content }d_A.
}
\]

Moreover

\[
Q^\sharp(r_A)
=\frac{Q(r_A)}d
=\frac AdT_A.
\]

Thus

\[
\boxed{
d\mid T_A}
\]

is equivalent to

\[
\boxed{A\mid Q^\sharp(r_A).}
\]

Once this condition is satisfied, the remaining lift equation is primitive modulo \(A/d\).

This is the strongest conceptual simplification obtained in the present round.

---

# Part VIII — Prime-Power Decomposition of Singular Lifts

Let

\[
p^e\Vert A.
\]

Since \(\gcd(A,10)=1\), necessarily

\[
\boxed{p\ne2,5.}
\]

Put

\[
f:=v_p(D_2),
\qquad
s:=\min(e,f).
\]

Then

\[
v_p(d_A)\text{ at }p=s.
\]

The A² lift congruence

\[
T_A+Q'(r_A)c\equiv0\pmod{p^e}
\]

has coefficient valuation exactly s. Therefore:

\[
\boxed{
\text{local lift exists}
\iff
v_p(T_A)\ge s.
}
\tag{PP-SOLV}
\]

If it exists, divide by \(p^s\):

\[
\frac{T_A}{p^s}
+
\frac{Q'(r_A)}{p^s}c
\equiv0
\pmod{p^{e-s}},
\]

and the second coefficient is a unit modulo \(p^{e-s}\). Hence

\[
\boxed{
 c\text{ is unique modulo }p^{e-s},
}
\]

and exactly

\[
\boxed{p^s}
\]

classes modulo \(p^e\) survive locally.

CRT over all \(p^e\Vert A\) multiplies these counts and recovers exactly

\[
\prod_{p\mid A}p^{s_p}=d_A
\]

canonical A² classes in the solvable singular branch.

### Extreme local content

If

\[
f\ge e,
\]

then \(s=e\). In that prime-power component, after the necessary condition

\[
v_p(T_A)\ge e
\]

holds, the first new digit c is unrestricted modulo \(p^e\). This is not an infinite freedom: it is exactly a **one-digit content delay** caused by \(p^e\) dividing every coefficient of Q.

---

# Part IX — New: Singular Sum-of-Two-Squares Signature

The solvability condition has additional arithmetic content.

Fix

\[
p^e\Vert A,
\qquad
s=\min(e,v_p(D_2))>0.
\]

If an A² lift exists, then

\[
p^s\mid T_A.
\]

But

\[
T_A
=H^2r_A^2+\mathcal X^2+D_2(n_A-Kr_A).
\]

Since \(p^s\mid D_2\),

\[
\boxed{
H^2r_A^2+\mathcal X^2\equiv0\pmod{p^s}.
}
\tag{S1}
\]

Also

\[
Kr_A+Z=An_A
\]

and \(p^e\mid A\), so

\[
Kr_A\equiv-Z\pmod{p^s}.
\]

Using \(2H=G\), multiply (S1) by \(4K^2\):

\[
\boxed{
(GZ)^2+(2K\mathcal X)^2\equiv0\pmod{p^s}.
}
\tag{S2}
\]

This is a necessary condition for every singular lift.

## 9.1 \(p\equiv3\pmod4\)

For an odd prime \(p\equiv3\pmod4\), \(-1\) is a quadratic nonresidue. Standard valuation of a sum of two squares gives

\[
v_p(X_1^2+X_2^2)=2\min(v_p(X_1),v_p(X_2))
\]

after removing the common p-power. Therefore (S2) implies

\[
\boxed{
p^{\lceil s/2\rceil}\mid GZ,\ 2K\mathcal X.}
\]

Since p is not 2 or 5,

\[
\gcd(p,2GK)=1,
\]

hence

\[
\boxed{
p^{\lceil s/2\rceil}\mid Z,\mathcal X.}
\]

Write

\[
r_p:=\lceil s/2\rceil.
\]

From

\[
2\mathcal X=Z+uN,
\qquad
\gcd(u,p)=1
\]

we get

\[
\boxed{p^{r_p}\mid N.}
\]

From

\[
D_2=ua_3+G\mathcal X,
\qquad
p^s\mid D_2,
\]

and \(r_p\le s\),

\[
\boxed{p^{r_p}\mid a_3.}
\]

Finally, A-ROOT modulo \(p^e\) gives

\[
\boxed{p^{r_p}\mid a_1.}
\]

Thus

\[
\boxed{
p^{r_p}\mid a_1,a_3,Z,\mathcal X,N.}
\]

If additionally

\[
p\nmid q+4,
\]

then from

\[
q+4\equiv2(1-G)\pmod p
\]

we have \(p\nmid G-1\). RCE2 then gives

\[
\boxed{p^{r_p}\mid t.}
\]

This is a sharp structural signature, not yet a contradiction.

## 9.2 \(p\equiv1\pmod4\)

If neither term in (S2) vanishes modulo p, then

\[
\left(\frac{GZ}{2K\mathcal X}\right)^2\equiv-1\pmod p.
\]

Thus the singular prime must select one of the two square roots of \(-1\) modulo p. This gives a two-cell local signature, but the present round does not promote it into a new long-term local-prime campaign.

---

# Part X — The \(p=2,5\) Audit and “Decimal Annihilation”

Inherited J2 arithmetic proves

\[
\boxed{\gcd(A,10)=1.}
\]

Therefore:

\[
2\nmid A,
\qquad
5\nmid A.
\]

Consequences:

1. no \(2\)-adic or \(5\)-adic prime-power component occurs in the A-lift modulus;
2. \(K=10^k\), \(H=G/2\), and \(10^\ell\) are all invertible modulo A;
3. there is no special decimal singular derivative at p=2 or 5;
4. generic \(2/5\)-phase machinery is irrelevant to this round.

The quadratic correction

\[
A^3H^2c^2
\]

vanishes modulo \(A^2\), but this is because it contains \(A^3\), not because \(H\) carries large powers of 2 or 5.

Hence the correct verdict for the prompt's Mechanism 4 is:

\[
\boxed{
\textbf{A-adic Taylor annihilation: YES; decimal }2/5\textbf{ annihilation: NO.}
}
\]

This negative result is useful because it prevents reopening an already-retired generic phase campaign.

---

# Part XI — Higher Lift: Stop at the First Useful Depth

The general inherited elementary lift is:

if

\[
Q(r_n)\equiv0\pmod{A^n}
\]

and

\[
x=r_n+A^nc,
\]

then modulo \(A^{n+1}\)

\[
\boxed{
\frac{Q(r_n)}{A^n}+Q'(r_n)c\equiv0\pmod A.
}
\tag{AN-LIFT}
\]

In the regular branch \(d_A=1\), the derivative remains an A-unit at every lift because

\[
Q'(r_n)\equiv KD_2\pmod A.
\]

Thus every subsequent A-digit is unique.

本轮不做无限 Hensel 展开。只在它立刻与 actual interval 发生 collision 时抬到 \(A^3\)。

---

# Part XII — Actual-Root Interval Rigidity

## 12.1 Correct interval

The valid interval is

\[
\boxed{
\frac{AG}{10}<a_1<\frac{8uD_2}{A10^\ell}.
}
\]

No \(a_1<AG\) theorem is used.

## 12.2 Inherited A² carry form

For any canonical A² lift

\[
0\le r_{A^2}<A^2,
\]

write only as an interval index

\[
\boxed{
a_1=r_{A^2}+A^2j.}
\tag{JINDEX}
\]

Here j is **not** a new structural quotient.

The inherited bound is

\[
\boxed{
0\le j<q\left(\frac{1299}{500}+10^{-\ell}\right)<2.599q
\qquad(\ell\ge6).
}
\tag{JBOUND}
\]

More strongly, the derivation gives

\[
\boxed{
\frac{a_1}{A^2}
<q\left(\frac{1299}{500}+10^{-\ell}\right).
}
\tag{XSIZE}
\]

Thus mod \(A^2\) does not globally isolate one integer root when q is large.

## 12.3 New regular A³ singleton theorem

Put

\[
C_\ell=\frac{1299}{500}+10^{-\ell}.
\]

Assume

\[
d_A=1.
\]

Then there is a unique canonical A³ root class

\[
0\le r_{A^3}<A^3.
\]

If

\[
A>C_\ell q,
\]

then from (XSIZE)

\[
a_1<A^2C_\ell q<A^3.
\]

Since

\[
a_1\equiv r_{A^3}\pmod{A^3},
\]

there are only two possibilities:

- \(r_{A^3}=0\): no positive root in \((0,A^3)\);
- \(r_{A^3}>0\): the only possible actual root is
  \[
  \boxed{a_1=r_{A^3}}.
  \]

Therefore:

\[
\boxed{
 d_A=1,\ A>C_\ell q
\Longrightarrow
\#\{a_1\text{ in the actual root interval}\}\le1.
}
\tag{SINGLETON}
\]

This is a genuine **Success C** subchamber.

## 12.4 Outer-divisor sufficient condition

Since

\[
A=2u+1=\frac{2(G+1)}q+1,
\]

a sufficient condition for \(A>C_\ell q\) is

\[
q^2<\frac{2(G+1)}{C_\ell}.
\]

For every \(\ell\ge6\),

\[
C_\ell\le\frac{2,598,001}{1,000,000}.
\]

Hence the uniform sufficient condition

\[
\boxed{
q^2<\frac{2,000,000}{2,598,001}(G+1)
}
\]

implies the singleton theorem.

Numerically this is approximately

\[
q<0.877395\sqrt{G+1}.
\]

No claim is made that all remaining q satisfy this.

---

# Part XIII — Two-A-Side-Equation Collision Audit

The prompt requested checking whether GRFQE and CQRF might independently produce incompatible A² lifts.

The answer is negative.

The following are algebraically the same root equation:

1. radial Q:
   \[
   AH^2a_1^2-2uKD_2a_1+\widetilde F=0;
   \]
2. cleared GRFQE with \(\kappa=a_1\):
   \[
   AG^2a_1^2-8uKD_2a_1+4\widetilde F=0;
   \]
3. CQRF-cleared root polynomial:
   \[
   AG^2M^2a_1^2-4uKEMa_1+AY^2+2RE=0.
   \]

Therefore they cannot yield genuinely independent A² classes whose disagreement would close J2.

Likewise RQDC

\[
uD_2a_1-\Omega=\frac{A10^\ell}{8}a_1^2
\]

is the normalized full-root factor identity, not an independent A-adic equation.

Thus Mechanism 8 is audited as:

\[
\boxed{
\textbf{no independent second A-side polynomial currently exists.}
}
\]

The next genuinely different modulus is u, not another reformulation of Q.

---

# Part XIV — Computational Reconnaissance

No new broad original-state enumeration was required. The inherited exact PRCC10 diagnostic already gives the relevant falsification data.

On the historical h=0 diagnostic corpus

\[
g\le1200,
\qquad
q\in\{7,11,17,19\},
\]

there were 79 DCDC/root-layer cells.

Distribution:

\[
\boxed{
\gcd(D_2,A):
\{1:53,\ 3:21,\ 7:4,\ 11:1\}.
}
\]

Hence

\[
\boxed{\gcd(D_2,A)=1\text{ globally}}
\]

is false.

Among 26 derivative-degenerate cells:

- 20 fail \(d_A\mid T_A\);
- 6 survive the A² solvability test;
- all 6 have \(d_A=3\);
- each has three A² root classes;
- all are later killed by U-SQ in that finite diagnostic.

This finite diagnostic is **not** promoted to a global theorem. Its role is to certify that singular A² liftability is genuinely nonempty, so a proof that simply discards \(d_A>1\) would be invalid.

The new symbolic file `J2-55-R1-A-Root-Lift-symbolic.py` independently verifies:

1. \(Q=dQ^\sharp\);
2. deflated derivative reduction;
3. original derivative after content division;
4. exact A² Taylor identity;
5. singular sum-of-two-squares signature.

Certificate status:

```text
J2_55_R1_SYMBOLIC_STATUS=PASS
CONTENT_DEFLATION=Q=d*Qsharp
DEFLATED_DERIVATIVE=Qsharp_prime(r) == K*(D2/d) (mod A/d)
ORIGINAL_DERIVATIVE_AFTER_DIVISION=(Qprime(r)/d) == K*(D2/d) (mod A/d)
A2_TAYLOR_RESIDUAL=0
SINGULAR_SIGNATURE=4*K^2*T_A == (G*Z)^2+(2*K*X)^2 (mod p^s)
P25_A_PRIME_BRANCH=ABSENT because inherited gcd(A,10)=1
```

---

# Part XV — Mechanism Audit

## Mechanism 1 — primitive linear coefficient

\[
\boxed{\textbf{SUCCESS globally}.}
\]

Coefficient is K and

\[
\gcd(K,A)=1.
\]

Thus mod A root class is unique for every admissible profile.

## Mechanism 2 — singular branch self-destructs

\[
\boxed{\textbf{FALSE globally}.}
\]

There are genuine singular A² lifts. Correct replacement is singular-content deflation.

## Mechanism 3 — derivative primitive

\[
\boxed{\textbf{TRUE iff }d_A=1.}
\]

Globally derivative degeneracy is exactly \(d_A=\gcd(D_2,A)\).

## Mechanism 4 — decimal annihilation

\[
\boxed{\textbf{NO as a }2/5\textbf{ mechanism}.}
\]

But the A³ Taylor correction automatically vanishes mod A².

## Mechanism 5 — actual interval collision

\[
\boxed{\textbf{PARTIAL SUCCESS}.}
\]

Regular branch plus \(A>C_\ell q\) gives at most one actual root after the A³ digit.

## Mechanism 6 — primitive digit collision

No global contradiction from \(p\mid a_1\) was proved. Since \(p\mid A\) implies \(p\nmid uH\), such p may be absorbed by the common scale U without violating \(\gcd(U,V)=1\). Do not claim extinction.

## Mechanism 7 — coefficient valuation mismatch

\[
\boxed{\textbf{SUCCESS as an exact local test}.}
\]

For \(p^e\Vert A\), local singularity exponent \(s=\min(e,v_p(D_2))\) requires

\[
v_p(T_A)\ge s.
\]

Failure kills the branch immediately.

## Mechanism 8 — two independent A-side equations disagree

\[
\boxed{\textbf{NOT AVAILABLE}.}
\]

GRFQE, radial Q and CQRF are algebraically the same polynomial. No independent second A-side lift was found.

---

# Part XVI — Rigorous Theorem Package

## Theorem ARL-1 — A-Root Residue Lemma

Every admissible J2 root satisfies

\[
\boxed{
a_1\equiv r_A:=-K^{-1}Z\pmod A.
}
\]

The class is globally unique because \(\gcd(K,A)=1\).

---

## Lemma ARL-2 — Singular-A Content Classification

Let

\[
d_A=\gcd(A,D_2).
\]

Then

\[
\boxed{Q=d_AQ^\sharp}
\]

with

\[
\gcd(A/d_A,D_2/d_A)=1,
\]

and

\[
\boxed{
\gcd((Q^\sharp)'(r_A),A/d_A)=1.
}
\]

Thus every derivative singularity is exactly common polynomial content.

---

## Theorem ARL-3 — Primitive A² Root Lift Classification

Let

\[
T_A=Q(r_A)/A.
\]

Then:

\[
\boxed{
\begin{cases}
d_A\nmid T_A:& \text{no A}^2\text{-lift};\\
d_A\mid T_A:& \text{exactly }d_A\text{ canonical A}^2\text{-classes}.
\end{cases}}
\]

In particular, if \(d_A=1\), the A² class is unique:

\[
\boxed{
a_1\equiv r_{A^2}\pmod{A^2}.}
\]

---

## Lemma ARL-3P — Prime-Power Singular Criterion

For \(p^e\Vert A\), let

\[
s=\min(e,v_p(D_2)).
\]

Then local A² lift exists iff

\[
\boxed{v_p(T_A)\ge s.}
\]

If it exists, c is unique modulo \(p^{e-s}\) and there are exactly \(p^s\) local classes modulo \(p^e\).

If \(s>0\), liftability also forces

\[
\boxed{(GZ)^2+(2K\mathcal X)^2\equiv0\pmod{p^s}.}
\]

---

## Corollary ARL-3B — Bad-Prime Scale Alignment

If \(p\equiv3\pmod4\) and \(s>0\), every singular A² lift satisfies

\[
\boxed{
p^{\lceil s/2\rceil}\mid a_1,a_3,Z,\mathcal X,N.}
\]

If \(p\nmid q+4\), also

\[
\boxed{p^{\lceil s/2\rceil}\mid t.}
\]

---

## Corollary ARL-4 — Actual-Root Fibre Bound

For a regular profile \(d_A=1\), if

\[
A>q\left(\frac{1299}{500}+10^{-\ell}\right),
\]

then after the unique A³ lift

\[
\boxed{
\#\left\{a_1\in I_{a_1}:a_1\equiv r_{A^3}\pmod{A^3}\right\}\le1.
}
\]

A uniform sufficient condition for \(\ell\ge6\) is

\[
\boxed{
q^2<\frac{2,000,000}{2,598,001}(G+1).
}
\]

---

## Interface ARL-5 — u-Compatibility Interface

For every surviving A² class

\[
0\le r_{A^2}<A^2,
\]

write only the residual interval index

\[
a_1=r_{A^2}+A^2j.
\]

Because

\[
A=2u+1
\]

implies

\[
\boxed{A^2\equiv1\pmod u,}
\]

U-SQ becomes

\[
\boxed{
(r_{A^2}+j)^2\equiv Z^2\pmod u.
}
\tag{ARL-U}
\]

with

\[
\boxed{
0\le j<q\left(\frac{1299}{500}+10^{-\ell}\right)<2.599q.
}
\]

The exact root equation becomes the carry polynomial

\[
\boxed{
\frac{Q(r_{A^2})}{A^2}
+Q'(r_{A^2})j
+A^3H^2j^2=0.
}
\tag{ARL-CARRY}
\]

This is the correct handoff to 55 Round 2.

---

# Part XVII — Survivor Classification

After this round every admissible J2 root profile lies in exactly one of the following categories.

## Class R0 — regular / interval-singleton

\[
d_A=1,
\qquad
A>C_\ell q.
\]

Unique A³ class, hence at most one actual integer root. The next action is immediate substitution into U-SQ and exact Q/CQRF; no carry campaign is needed.

## Class R1 — regular / large-q carry

\[
d_A=1,
\qquad
A\le C_\ell q.
\]

Unique A² class but a short interval index remains:

\[
0\le j<C_\ell q.
\]

Next obstruction is

\[
(r_{A^2}+j)^2\equiv Z^2\pmod u
\]

plus exact carry polynomial.

## Class S0 — singular / valuation-dead

\[
d_A>1,
\qquad
d_A\nmid T_A.
\]

Closed immediately at A² lift.

## Class S1 — singular / content-survivor

\[
d_A>1,
\qquad
d_A\mid T_A.
\]

There are exactly \(d_A\) A² classes. For every \(p^e\Vert d_A\), the prime-power sum-of-two-squares signature is mandatory. This is the exact singular obstruction still open globally.

No fifth class is needed.

---

# Part XVIII — What Failed, Precisely

The round did **not** prove

\[
\gcd(D_2,A)=1.
\]

It cannot: inherited exact finite data contain genuine counterexamples.

The round did **not** prove singular derivative means no A² lift.

It cannot: six inherited diagnostic cells with \(d_A=3\) do lift.

The round did **not** obtain a global actual interval shorter than A².

The valid root interval still permits \(O(q)\) A² carries in the large-q chamber.

The round did **not** find a second independent A-polynomial.

GRFQE and CQRF are the same Q after normalization / clearing.

The round did **not** use \(a_1<AG\), because that theorem is absent from the recovered corpus.

These failures leave a sharp obstruction rather than vague openness.

---

# Part XIX — Precise Next-Round Interface

The next 55 round should begin from **only** the following terminal data.

For every outer structural profile, compute:

\[
A,u,q,G,K,N,t,Z,\mathcal X,D_2,
\]

\[
r_A=(-K^{-1}Z)\bmod A,
\]

\[
T_A=Q(r_A)/A,
\]

\[
d_A=\gcd(A,D_2).
\]

Then:

1. if \(d_A\nmid T_A\), kill;
2. otherwise enumerate the **canonical A² root classes only** — one when regular, exactly \(d_A\) when singular;
3. in the regular threshold chamber \(A>C_\ell q\), lift once to A³ and substitute the unique integer candidate immediately;
4. otherwise use
   \[
   a_1=r_{A^2}+A^2j,
   \quad0\le j<C_\ell q;
   \]
5. collide with
   \[
   (r_{A^2}+j)^2\equiv Z^2\pmod u;
   \]
6. keep the exact carry polynomial
   \[
   Q(r_{A^2})/A^2+Q'(r_{A^2})j+A^3H^2j^2=0
   \]
   as the final global-root consistency check;
7. do **not** define another quotient of \(a_1\) or j.

For singular primes \(p\equiv3\pmod4\), carry forward the additional forced alignment

\[
p^{\lceil s/2\rceil}\mid a_1,a_3,Z,\mathcal X,N
\]

as a side lemma to collide with u-square / CRT structure.

The intended next campaign can therefore be stated narrowly as

\[
\boxed{
\textbf{A²-root fibres}
\times
\textbf{short actual carry}
\times
\textbf{u-square synchronization}.
}
\]

---

# Part XX — J2 Closure Status

\[
\boxed{\textbf{J2 OPEN}}
\]

The exact surviving root obstruction is

\[
\boxed{
\begin{aligned}
&\text{choose one of the canonical primitive }A^2\text{-root classes }r_{A^2},\\
&0\le j<q\left(\frac{1299}{500}+10^{-\ell}\right),\\
&(r_{A^2}+j)^2\equiv Z^2\pmod u,\\
&\frac{Q(r_{A^2})}{A^2}
+Q'(r_{A^2})j
+A^3H^2j^2=0,
\end{aligned}}
\tag{SURVIVING-ROOT}
\]

with, in the singular chamber,

\[
\boxed{
d_A=\gcd(A,D_2)>1,
\qquad
d_A\mid T_A,
}
\]

and prime-power constraints (P-SOS)/(BADP-ALIGN).

The present round therefore reaches:

\[
\boxed{\textbf{Success A globally}}
\]

and the corrected composite version of

\[
\boxed{\textbf{Success B: unique on regular branch, exactly classified on singular branch}.}
\]

It reaches a genuine

\[
\boxed{\textbf{Success C subchamber}}
\]

through the regular A³ singleton theorem, but not globally.

It does not reach Success D.

---

# Final Strategic Verdict

The correct conclusion of 55 Round 1 is not “we need a better root quotient”.

It is:

\[
\boxed{
\textbf{the first A-digit is rigid; the second A-digit is completely classified;}
}
\]

\[
\boxed{
\textbf{all singularity is coefficient content;}
}
\]

and

\[
\boxed{
\textbf{the remaining freedom is now only the actual root carry that must collide with }u\textbf{-square.}
}
\]

So the 55 discipline remains intact:

\[
\boxed{
\textbf{Do not parameterize the root again. Lift it, rigidify it, and collide it.}
}
\]
