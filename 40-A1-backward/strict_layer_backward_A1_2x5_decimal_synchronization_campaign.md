# 三项十进制拼接平方和问题：Backward Strict Layer — A1 Same-Determinant \(2\times5\) Decimal Synchronization Campaign

**文件名：** `strict_layer_backward_A1_2x5_decimal_synchronization_campaign.md`  
**日期：** 2026-08-16  
**研究范围：** Strict Layer，仅研究 \(A_1\)-only 的 backward exact recovery；主战场为

\[
\boxed{
\text{Same-Determinant }2\text{-Phase}
\times
\text{Frozen }5\text{-Phase}
\times
\text{Actual Decimal Cut}.
}
\]

---

# 1. Executive summary

本轮达到了最低成功标准，而且得到一个比预期更精确的 \(p=2\) 图景。

上一轮已经把 pure \(5\)-adic same-cut loop 研究到：

\[
\boxed{
\text{regular }5\text{-adic fixed point}
+
\text{strict-cut shielding}
+
\text{surviving Hensel towers},
}
\]

因此继续增加 pure \(5\)-adic precision 不再是正确路线。

本轮从 A1 自身 exact word identities 重建 \(2\)-side，没有迁移任何 DD source orientation。最终得到：

## NEW PROVED 1 — exact same-determinant \(2\)-adic master identity

定义

\[
s_2:=v_2(b_3),\qquad
\beta_2:=v_2(\mathbf B),
\]

\[
\nu_2:=v_2(N),\qquad
\gamma_2:=v_2(G),
\]

\[
\ell_2:=v_2(\Delta),
\qquad
c_2^+:=v_2(C_+),
\]

其中

\[
\Delta=b_3P-a_3D,
\qquad
C_+:=b_3\mathbf A+a_3\mathbf B.
\]

由 raw A1-WGF 精确得到

\[
\boxed{
\ell_2
=
\nu_2+2\beta_2+2s_2
-2\gamma_2-n_3-c_2^+.
}
\tag{2M}
\]

这是真正的 \(2\)-adic source equation；它与 \(5\)-side 的本质差异全部集中在：

\[
\boxed{
\beta_2
\quad\text{和}\quad
c_2^+.
}
\]

因此绝不能把 \(R_5\) 中的 \(5\) 机械替换成 \(2\)。

---

## NEW PROVED 2 — A1 Same-Determinant \(2\)-Phase-to-Cut Transfer

若

\[
\ell_2>s_2,
\]

写

\[
b_3=2^{s_2}b_3^\circ,
\qquad b_3^\circ\ \text{odd}.
\]

由

\[
2^{\ell_2}\mid b_3P-a_3D
\]

且 \(\ell_2>s_2\)，自动推出

\[
2^{s_2}\mid a_3D.
\]

因此不存在“形式除法”问题；真正 canonical residue 为

\[
\boxed{
C_2
:=
\frac{a_3D}{2^{s_2}}
\left(b_3^\circ\right)^{-1}.
}
\]

并有

\[
\boxed{
P\equiv C_2
\pmod{2^{R_2}},
\qquad
R_2:=\ell_2-s_2>0.
}
\tag{2CUT}
\]

所以本轮第一次严格建立了：

\[
\boxed{
\textbf{A1 same determinant }2\textbf{-phase}
\Longrightarrow
\textbf{actual }P\textbf{-congruence}.
}
\]

---

## NEW PROVED 3 — partial-\(2\) chamber 的“一位损失定理”

在

\[
\boxed{
0<s_2<n_3
}
\]

且 \(R_2>0\) 的真正 cut-visible chamber 中：

\[
v_2(\mathbf B)=s_2,
\qquad
v_2(E)=v_2(h)=0.
\]

同时 normalized gap pair 满足：

\[
v_2(Z_-)=n_3-s_2+v_2(\varepsilon)\ge3,
\]

而 \(Z_\pm\) 均为偶数，且

\[
\gcd(Z_-,Z_+)\mid2.
\]

于是被 \(Z_-\) 吃掉深 \(2\)-power 后，另一侧必须精确只有一位：

\[
\boxed{
v_2(Z_+)=1.
}
\]

等价地，在 raw plus factor 上：

\[
\boxed{
v_2(C_+)=s_2+1.
}
\]

代入 (2M)：

\[
\boxed{
\ell_2
=
\nu_2+3s_2-2\gamma_2-n_3-1.
}
\tag{2L}
\]

因此真正 cut-visible depth 是

\[
\boxed{
R_2
=
\nu_2+2s_2-2\gamma_2-n_3-1
>0.
}
\tag{R2}
\]

与 \(5\)-side

\[
R_5=\nu_5+2s_5-2\gamma_5-n_3
\]

相比，\(2\)-side恰好多一个

\[
\boxed{-1}.
\]

这不是 normalization accident，而是：

\[
\boxed{
x-y\text{ 深偶}
\Longrightarrow
x+y\text{ 精确只含一个 }2
}
\]

所强迫的 parity tax。

---

## NEW PROVED 4 — \(2\)-adic norm 完全没有 \(5\)-adic Hensel escape

令

\[
X=a_1b_2,
\qquad
Y=a_2b_1,
\qquad
N=X^2+Y^2.
\]

若

\[
x:=v_2(X),\qquad y:=v_2(Y),
\]

则：

\[
\boxed{
x\ne y
\Longrightarrow
v_2(N)=2\min(x,y),
}
\tag{N2a}
\]

而若

\[
x=y=t,
\]

则 normalized \(X_0,Y_0\) 均为 odd，故

\[
X_0^2+Y_0^2\equiv2\pmod8,
\]

从而

\[
\boxed{
v_2(N)=2t+1.
}
\tag{N2b}
\]

因此 \(p=2\) 没有 analogous

\[
\lambda_N\to\infty
\]

unit resonance。

这是本轮最强的局部刚性之一。

---

## NEW PROVED 5 — previous genuine \(\mathbf Z_5\) UHL survivor 被 \(2\)-side直接杀死

上一轮 Pattern-II UHL trace 为：

\[
b_1=1,\quad b_2=5,
\]

\[
b_3=10\,000\,625,
\quad
n_3=5,
\quad
g=3,
\]

\[
D=15000,\quad G=5,
\]

\[
a_1=a_3=1,
\qquad
a_2=4+5t.
\]

它在 \(\mathbf Z_5\) 中存在 genuine raw A1-WR simple Hensel branch。

但在 \(2\)-adic side：

\[
b_1,b_2,b_3,\mathbf B,a_1,a_3
\]

全部为 odd，而

\[
D
\]

为 even。

于是无论 \(a_2\) 奇偶：

- 若 \(a_2\) even，则 \(N=25+a_2^2\) 为 odd，故 \(v_2(N)=0\)；
- 若 \(a_2\) odd，则 \(N\) 是两个 odd squares 之和，故 \(v_2(N)=1\)。

另一方面 raw WGF RHS 至少含：

\[
2^{n_3}
\]

来自 \(S\)，以及至少一个 \(2\) 来自 plus factor，因此 RHS 的 \(2\)-valuation 至少为 \(6\)。

矛盾。

故：

\[
\boxed{
\textbf{UHL 的 genuine }\mathbf Z_5\textbf{ branch 没有任何 }\mathbf Z_2\textbf{ companion.}
}
\tag{UHL-2KILL}
\]

这证明 \(2\)-side 不是装饰性信息；它确实能杀掉 pure-\(5\) 看不见的真实 local branch。

---

## NEW PROVED 6 — conditional CRT 确实产生 genuine decimal suffix

冻结上一轮：

\[
P\equiv C_5\pmod{5^{R_5}}.
\]

若本轮同时有：

\[
P\equiv C_2\pmod{2^{R_2}},
\]

则 CRT 唯一给出：

\[
\boxed{
P\equiv C_{2,5}
\pmod{2^{R_2}5^{R_5}}.
}
\]

定义

\[
\boxed{
J:=\min(R_2,R_5).
}
\]

则：

\[
10^J\mid 2^{R_2}5^{R_5},
\]

所以第一次真正得到：

\[
\boxed{
P\equiv C_{10}\pmod{10^J}.
}
\tag{10CUT}
\]

这不是单素数 phase，而是真正的 base-10 suffix statement。

---

## FAILED / OPEN — partial-\(5\) 尚未关闭

本轮没有证明：

\[
0<v_5(b_3)<n_3
\Longrightarrow\varnothing.
\]

原因不是 \(2\)-side毫无作用，而是：

\[
\boxed{
R_2>0
}
\]

并不在所有 partial-\(5\) projected survivors 上自动出现。

特别是 \(b_3\) 可以为 odd，即

\[
s_2=0,
\]

而 determinant 本身也可以保持 odd，导致：

\[
R_2=0.
\]

因此：

\[
\boxed{
\textbf{partial-5}
\not\Longrightarrow
\textbf{nontrivial decimal suffix}.
}
\]

本轮最准确的最终结论是：

\[
\boxed{
\textbf{2-adic companion 是 genuinely decisive on some branches,}
}
\]

但：

\[
\boxed{
\textbf{not a uniform partial-5 closure engine.}
}
\]

---

# 2. Frozen A1 backward state

以下全部视为 **FROZEN**。

\[
P=a_1 10^n+a_2,
\]

\[
S=10^{n_3},
\]

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\]

\[
D=10^gQ,
\]

\[
n=m_2+g+k_{12},
\qquad
k_{12}\ge1.
\]

完整 words：

\[
\mathbf A=SP+a_3,
\qquad
\mathbf B=SD+b_3.
\]

令：

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\]

\[
\Gamma=\gcd(\mathbf B,\Lambda),
\qquad
E=\frac{\mathbf B}{\Gamma}.
\]

对 admissible exact trace：

\[
\boxed{
E\mid\mathbf A,
\qquad
\gcd(E,10)=1.
}
\]

写：

\[
\mathbf A=EW,
\qquad
\mathbf B=E\Gamma.
\]

再令：

\[
h=\gcd(W,\Gamma),
\qquad
W=hu,
\qquad
\Gamma=hv,
\qquad
\gcd(u,v)=1.
\]

定义：

\[
\varepsilon:=vP-Du>0.
\]

以及 same word determinant：

\[
\boxed{
\Delta:=b_3P-a_3D.
}
\]

冻结 exact bridge：

\[
\boxed{
\Delta=Eh\,\varepsilon.
}
\tag{DELTA}
\]

---

# 3. Frozen pure-\(5\) negative result

partial \(5\)-saturation：

\[
0<s_5:=v_5(b_3)<n_3.
\]

冻结：

\[
e_5:=v_5(\Delta)
=
\nu_5+3s_5-2\gamma_5-n_3,
\]

其中：

\[
\nu_5=v_5(N),
\qquad
\gamma_5=v_5(G).
\]

cut-visible depth：

\[
\boxed{
R_5
=
\max\{0,\nu_5+2s_5-2\gamma_5-n_3\}.
}
\]

若 \(R_5>0\)：

\[
\boxed{
P\equiv
C_5
:=
a_3\frac D{5^{s_5}}
\left(\frac{b_3}{5^{s_5}}\right)^{-1}
\pmod{5^{R_5}}.
}
\tag{5CUT}
\]

第三轮已经证明 pure \(5\)-adic same-cut feedback 可存在：

- regular fixed points；
- strict-cut shielding；
- Hensel-compatible local towers；
- arbitrary-depth projected pseudo-families。

因此本轮不尝试复活：

\[
\boxed{
\text{pure }5\text{-adic self-amplification}.
}
\]

---

# 4. Anti-duplication boundary

本轮不使用：

- moving primitive-core height；
- \(Q_0\to\infty\)；
- forward translation-line termination；
- DD source orientation；
- DD double resonance；
- DD post-deflation quotient；
- DD quotient overload。

当前正向线已经将 primitive-only closure 的缺口推进到 common-scale numerator / digit-window realization。

本轮 backward 只使用 fixed candidate / fixed trace / actual word arithmetic。

---

# 5. Same-determinant philosophy

本轮唯一允许的主 phase object 是：

\[
\boxed{
\Delta=b_3P-a_3D.
}
\]

原因是：

\[
P=a_1 10^n+a_2
\]

是真实 decimal cut。

若分别构造与 \(P\) 无关的 \(2\)-adic与 \(5\)-adic invariants，即使各自很深，也不能合法称作 decimal synchronization。

真正目标必须是：

\[
v_2(\Delta),\qquad v_5(\Delta)
\]

共同作用于同一个 \(P\)。

---

# 6. \(2\)-adic provenance audit

raw WGF：

\[
N\mathbf B^2b_3^2
=
G^2
(b_3\mathbf A-a_3\mathbf B)
(b_3\mathbf A+a_3\mathbf B).
\]

而：

\[
b_3\mathbf A-a_3\mathbf B
=
S\Delta.
\]

定义：

\[
C_+:=
b_3\mathbf A+a_3\mathbf B.
\]

故：

\[
\boxed{
N\mathbf B^2b_3^2
=
G^2S\Delta C_+.
}
\tag{WGF2}
\]

对 \(p=2\) 逐项取 valuation：

\[
\nu_2+2\beta_2+2s_2
=
2\gamma_2+n_3+\ell_2+c_2^+.
\]

即：

\[
\boxed{
\ell_2
=
\nu_2+2\beta_2+2s_2
-2\gamma_2-n_3-c_2^+.
}
\]

这就是本轮的真正 source audit。

---

# 7. \(2\)-support chambers

定义：

\[
s_2=v_2(b_3).
\]

分：

### Chamber 2-N

\[
s_2=0.
\]

### Chamber 2-P

\[
0<s_2<n_3.
\]

### Chamber 2-F

\[
s_2\ge n_3.
\]

真正 clean 的 growing residual \(2\)-phase 只在 Chamber 2-P 中自动存在。

Chamber 2-N 可以产生 determinant cancellation，但其来源不再是 tail residual absorption。

Chamber 2-F 中：

\[
v_2(\mathcal L)=0,
\]

因此 tail-deflated gap没有 forced residual \(2\)-modulus；任何 \(2\)-depth只能来自额外 exact cancellation。

---

# 8. \(v_2(\Delta)\) analysis

## 8.1 General determinant trichotomy

写：

\[
b_3=2^{s_2}b_3^\circ,
\qquad
D=2^dD^\circ.
\]

则：

\[
\Delta
=
2^{s_2}b_3^\circ P-a_3 2^dD^\circ.
\]

若：

\[
s_2+v_2(P)<d+v_2(a_3),
\]

则：

\[
v_2(\Delta)=s_2+v_2(P).
\]

若反向严格小于，则：

\[
v_2(\Delta)=d+v_2(a_3).
\]

只有两项 valuation 相等时，才可能出现 deep cancellation。

因此：

\[
\boxed{
R_2>0
}
\]

本身已经意味着 same-determinant forced cancellation，而不是 generic inequality。

---

# 9. \(2\)-adic normalization losses

partial-\(2\) 中：

\[
0<s_2<n_3.
\]

由：

\[
\gcd(a_3,b_3)=1
\]

得：

\[
a_3\text{ odd}.
\]

又：

\[
\mathbf B=SD+b_3,
\]

其中：

\[
v_2(SD)\ge n_3>s_2,
\]

所以：

\[
\boxed{
v_2(\mathbf B)=s_2.
}
\]

因为：

\[
v_2(E)=0,
\]

得：

\[
v_2(\Gamma)=s_2.
\]

而：

\[
\Gamma=h\eta\bar v,
\]

且：

\[
v_2(\eta)=s_2,
\]

所以：

\[
\boxed{
v_2(h)=v_2(\bar v)=0.
}
\]

又 \(2\mid v\) 与 \(\gcd(u,v)=1\) 给：

\[
u\text{ odd}.
\]

因此：

\[
c_a=\gcd(a_3,u)
\]

也是 odd。

这里与 \(5\)-side不同之处只剩 normalized plus/minus pair 的共享 factor \(2\)。

---

# 10. A1 \(2\)-Phase-to-Cut Transfer

## Theorem 2PC

若：

\[
\ell_2:=v_2(\Delta)>s_2:=v_2(b_3),
\]

则：

\[
2^{s_2}\mid a_3D.
\]

定义：

\[
b_3^\circ=b_3/2^{s_2}.
\]

则 \(b_3^\circ\) odd，从而在：

\[
\mathbf Z/2^{\ell_2-s_2}\mathbf Z
\]

中可逆。

因此：

\[
\boxed{
P
\equiv
\frac{a_3D}{2^{s_2}}
(b_3^\circ)^{-1}
\pmod{2^{\ell_2-s_2}}.
}
\]

定义：

\[
\boxed{
R_2^{\rm cut}:=(\ell_2-s_2)_+.
}
\]

这一定理不要求预先假设：

\[
v_2(D)\ge s_2.
\]

该整除性由 deep determinant congruence 自己强迫。

**状态：NEW PROVED.**

---

# 11. \(2\)-adic norm rigidity

令：

\[
X=a_1b_2,
\qquad
Y=a_2b_1.
\]

设：

\[
x=v_2(X),
\qquad
y=v_2(Y).
\]

若 \(x<y\)，则：

\[
N
=
2^{2x}
\left(
X_0^2+2^{2(y-x)}Y_0^2
\right),
\]

括号内为 odd，故：

\[
\boxed{
v_2(N)=2x.
}
\]

对 \(y<x\) 对称。

若：

\[
x=y=t,
\]

则：

\[
N
=
2^{2t}(X_0^2+Y_0^2),
\]

其中 \(X_0,Y_0\) odd。

由于 odd square：

\[
\equiv1\pmod8,
\]

所以：

\[
X_0^2+Y_0^2\equiv2\pmod8.
\]

故：

\[
\boxed{
v_2(N)=2t+1.
}
\]

**状态：NEW PROVED.**

这说明 \(2\)-side没有 \(5\)-side的：

\[
\boxed{
\text{arbitrarily deep unit norm resonance}.
}
\]

---

# 12. \(Z_-/Z_+\) parity allocation

partial-\(2\) 中：

\[
c_ac_\tau Z_-=\mathcal L\varepsilon.
\]

因为 \(a_3,u,\tau,\bar v\) 的 relevant normalized parts 均为 odd，可写：

\[
Z_-=B-A,
\qquad
Z_+=B+A,
\]

其中 \(A,B\) odd。

因此：

\[
Z_-,Z_+
\]

均为 even。

又：

\[
\gcd(Z_-,Z_+)\mid2.
\]

所以：

\[
\boxed{
\min(v_2(Z_-),v_2(Z_+))=1.
}
\]

更精确地：

\[
A,B\text{ odd}
\Longrightarrow
\begin{cases}
v_2(B-A)=1,\ v_2(B+A)\ge2,\\
\text{或}\\
v_2(B+A)=1,\ v_2(B-A)\ge2.
\end{cases}
\]

在 cut-visible branch：

\[
v_2(\Delta)>s_2,
\]

由 \(\Delta=Eh\varepsilon\) 与 \(E,h\) odd：

\[
v_2(\varepsilon)>s_2.
\]

于是：

\[
v_2(Z_-)
=
n_3-s_2+v_2(\varepsilon)
\ge3.
\]

故 orientation 被 same determinant 自己决定：

\[
\boxed{
v_2(Z_+)=1.
}
\]

注意：这不是 DD source orientation 的迁移；它只是 A1 normalized difference/sum pair 的 parity consequence。

---

# 13. Exact \(R_2\) formula

partial-\(2\)、cut-visible 时：

\[
v_2(\mathbf B)=s_2.
\]

并且：

\[
v_2(C_+)=s_2+1.
\]

代入 (2M)：

\[
\ell_2
=
\nu_2+2s_2+2s_2
-2\gamma_2-n_3-(s_2+1).
\]

所以：

\[
\boxed{
\ell_2
=
\nu_2+3s_2-2\gamma_2-n_3-1.
}
\]

从而：

\[
\boxed{
R_2
=
\nu_2+2s_2-2\gamma_2-n_3-1.
}
\]

该公式的适用域必须写清楚：

\[
\boxed{
0<s_2<n_3,
\qquad
R_2>0.
}
\]

不能在 boundary 上直接写成无条件 max-formula。

---

## 13.1 boundary parity reversal

若：

\[
n_3-s_2=1,
\qquad
v_2(\varepsilon)=0,
\]

则：

\[
v_2(Z_-)=1.
\]

此时 deep \(2\)-power 可转移到 \(Z_+\)，而：

\[
v_2(\Delta)=0.
\]

所以：

\[
R_2=0.
\]

这给出一个明确的：

\[
\boxed{
\textbf{2-adic phase reversal escape}.
}
\]

因此 \(p=2\) 的正确 theorem 必须是 chambered theorem，而不是机械的全局 formula。

---

# 14. Frozen \(R_5\) interface

本轮仍使用 frozen：

\[
R_5
=
\max\{0,\nu_5+2s_5-2\gamma_5-n_3\}.
\]

当 \(R_5>0\)：

\[
P\equiv C_5\pmod{5^{R_5}}.
\]

与 \(2\)-side 合并时，所有 residue 必须来自同一个：

\[
\boxed{
P.
}
\]

---

# 15. Joint \(b_3\) \((2,5)\)-profile

partial-\(5\) 固定：

\[
0<s_5<n_3.
\]

而：

\[
s_2=v_2(b_3)
\]

可以属于：

\[
0,
\quad
(0,n_3),
\quad
[n_3,\infty).
\]

所以 partial-\(5\) 不自动意味着 partial-\(2\)。

若：

\[
s_2>0,\qquad s_5>0,
\]

则 reducedness 给：

\[
\boxed{
\gcd(a_3,10)=1.
}
\]

即：

\[
a_3\bmod10\in\{1,3,7,9\}.
\]

但这本身并不强迫 \(R_2>0\)。

---

# 16. CRT synchronization

若：

\[
R_2>0,\qquad R_5>0,
\]

则：

\[
P\equiv C_2\pmod{2^{R_2}},
\]

\[
P\equiv C_5\pmod{5^{R_5}}.
\]

因为 moduli coprime，存在唯一：

\[
C_{2,5}
\bmod 2^{R_2}5^{R_5}.
\]

故：

\[
\boxed{
P\equiv C_{2,5}
\pmod{2^{R_2}5^{R_5}}.
}
\]

定义：

\[
J=\min(R_2,R_5).
\]

则：

\[
\boxed{
P\equiv C_{10}\pmod{10^J}.
}
\]

**状态：NEW PROVED / standard CRT applied to source-valid residues.**

---

# 17. Decimal Gap Depth

最自然的真正 decimal depth 为：

\[
\boxed{
R_{10}:=
\min(R_2,R_5).
}
\]

只有当两个 prime 都穿透到 actual \(P\) 时，才可称作：

\[
\boxed{
\textbf{Decimal Gap Depth}.
}
\]

单独的 \(R_5\) 或 \(R_2\) 都不能称为 decimal digits。

---

# 18. Actual suffix extraction

因为：

\[
P=a_1 10^n+a_2,
\]

若：

\[
J\le n,
\]

则：

\[
\boxed{
a_2\equiv C_{10}\pmod{10^J}.
}
\]

### Regime I

\[
J<n.
\]

锁定 \(a_2\) 最后 \(J\) 位。

### Regime II

\[
J=n.
\]

整个 \(a_2\) 被唯一决定为对应 \(n\)-digit representative。

### Regime III

\[
J>n.
\]

先有：

\[
a_2\equiv C_{10}\pmod{10^n},
\]

再有：

\[
\boxed{
a_1
\equiv
\frac{C_{10}-a_2}{10^n}
\pmod{10^{J-n}}.
}
\]

这是第一次 genuine cross-cut decimal recovery。

---

# 19. Mod \(10\) classification

若：

\[
J\ge1,
\]

则末位被锁定。

individual reducedness 给：

- 若 \(2\mid b_2\)，则 \(a_2\) odd；
- 若 \(5\mid b_2\)，则 \(5\nmid a_2\)；
- 若 \(10\mid b_2\)，则
  \[
  a_2\bmod10\in\{1,3,7,9\}.
  \]

但本轮没有得到 uniform forbidden-digit theorem。

事实上，对真正 candidate-derived phase：

- \(2\mid b_2\) 时，\(C_2\) 必须是 odd；
- \(5\mid b_2\) 时，\(C_5\) 必须是 \(5\)-adic unit。

所以在 both-support subchamber：

\[
\boxed{
\text{mod }10\text{ reducedness compatibility往往是自动保留的，}
}
\]

而不是自动制造 contradiction。

**状态：FAILED as a uniform closure mechanism.**

---

# 20. Mod \(100\) / \(1000\) escalation

若：

\[
J\ge2
\]

或：

\[
J\ge3,
\]

当然可分别读取：

\[
a_2\bmod100,
\qquad
a_2\bmod1000.
\]

但本轮没有证明：

\[
J\ge2
\]

或：

\[
J\ge3
\]

在所有 partial-\(5\) survivors 中成立。

所以：

\[
\boxed{
\text{Decimal Suffix Ladder 目前是 conditional exact machinery，}
}
\]

不是 uniform closure theorem。

---

# 21. Reducedness collision

本轮系统检查后，最强结论是：

\[
\boxed{
\textbf{没有发现 uniform decimal-suffix }\times\textbf{ reducedness contradiction.}
}
\]

原因有二：

1. \(R_2\) 可能为 \(0\)；
2. 即使 \(J\ge1\)，candidate-derived residue 往往自动落入 reducedness 允许的 unit class。

所以 reducedness 的作用仍更像：

\[
\boxed{
\text{branch filter}
}
\]

而不是当前唯一 terminal obstruction。

---

# 22. Decimal norm feedback

\(2\)-side norm比 \(5\)-side刚性得多：

\[
\nu_2
\]

完全由 support equality / inequality决定，不含额外 Hensel parameter。

在 partial-\(2\) cut-visible chamber：

\[
R_2
=
\nu_2+2s_2-2\gamma_2-n_3-1.
\]

令：

\[
r_i=v_2(b_i),
\qquad
\alpha_i=v_2(a_i).
\]

则：

\[
x=\alpha_1+r_2,
\qquad
y=\alpha_2+r_1.
\]

## 22.1 Both prefix denominators even, unequal depths

若：

\[
r_1,r_2>0,
\qquad
r_1\ne r_2,
\]

reducedness 给：

\[
\alpha_1=\alpha_2=0.
\]

因此：

\[
\nu_2=2\min(r_1,r_2).
\]

故：

\[
\boxed{
R_2
=
2s_2-n_3-1-2\max(r_1,r_2).
}
\tag{R2-U}
\]

---

## 22.2 Equal positive prefix support

若：

\[
r_1=r_2=r>0,
\]

则：

\[
\nu_2=2r+1.
\]

因此：

\[
\boxed{
R_2
=
2s_2-n_3-2r.
}
\tag{R2-E}
\]

注意这里 equal support 反而由 norm 的额外固定 \(+1\) 精确抵消 plus-factor parity tax。

---

## 22.3 Exactly one prefix denominator even

若：

\[
r_1>0,\qquad r_2=0,
\]

则：

\[
\alpha_1=0,
\]

所以：

\[
v_2(X)=0,
\qquad
v_2(Y)\ge1.
\]

因此：

\[
\nu_2=0.
\]

于是：

\[
\boxed{
R_2
=
2s_2-n_3-1-2r_1.
}
\]

对另一侧对称。

---

## 22.4 No prefix denominator has \(2\)

若：

\[
r_1=r_2=0,
\]

则：

- \(\alpha_1\ne\alpha_2\) 时：
  \[
  \nu_2=2\min(\alpha_1,\alpha_2);
  \]
- \(\alpha_1=\alpha_2=t\) 时：
  \[
  \nu_2=2t+1.
  \]

所以：

\[
R_2
=
\nu_2+2s_2-n_3-1.
\]

这给出完整的 partial-\(2\) norm-feedback tree。

---

# 23. Cut-boundary carry analysis

本轮没有得到：

\[
J\ge n.
\]

甚至没有得到 uniform：

\[
J\ge1.
\]

因此无法统一进入有限 carry closure。

如果某个 branch 另行得到：

\[
n-J\le C,
\]

则可以写：

\[
a_2=d+10^Jc,
\qquad
0\le c<10^C,
\]

并把有限 \(c\)-states代回 exact norm / WGF。

本轮把该机制保留为：

\[
\boxed{
\textbf{conditional finite-state closure engine}.
}
\]

---

# 24. Strict-cut shielding revisited

\(5\)-side shielding 的本质是：

\[
R_5
\]

追不上：

\[
n+\lambda_N.
\]

\(2\)-side完全不同：

\[
\lambda_N
\]

不存在。

因此 \(2\)-adic companion 确实绕开了 pure \(5\)-Hensel shielding 的机制来源。

但它没有绕过另一个更基础的问题：

\[
\boxed{
R_2\text{ 可能根本为 }0.
}
\]

所以新 bottleneck 不是“2-depth也追不上某个 Hensel error”，而是：

\[
\boxed{
\textbf{2-phase existence / visibility itself is branch-dependent.}
}
\]

---

# 25. Asymmetric CRT coordinates

若：

\[
R_5>R_2=J,
\]

完整信息不应粗暴压成 \(P\bmod10^J\)。

更自然的 coordinate 为：

\[
\boxed{
\left(
P\bmod10^J,
\;
\frac{P-C_{10}}{10^J}
\bmod5^{R_5-J}
\right).
}
\]

若：

\[
R_2>R_5,
\]

则对称保留 extra \(2\)-phase。

这避免丢失第三轮已经付出巨大代价获得的 deep \(5\)-adic information。

---

# 26. \(10\)-adic formulation

在两个 phase 都存在的 branch 上，可以写：

\[
\mathbf Z_{10}
\simeq
\mathbf Z_2\times\mathbf Z_5.
\]

same determinant：

\[
\Delta=b_3P-a_3D
\]

把 \(P\) 锁入一个 product cylinder：

\[
\boxed{
P\in
(C_2+2^{R_2}\mathbf Z_2)
\times
(C_5+5^{R_5}\mathbf Z_5).
}
\]

其真正 decimal cylinder depth正是：

\[
\min(R_2,R_5).
\]

但若：

\[
R_2=0,
\]

则该 cylinder 在 \(\mathbf Z_2\) 方向是 open/full 的；此时不能声称已经获得真正 \(10\)-adic rigidity。

---

# 27. Computational \((2^k\times5^\ell)\) experiments

计算仅用于 falsification / branch discovery。

## 27.1 PPF trace 的 \(2\)-adic raw-WGF lifting

取上一轮 arbitrary-depth projected pseudo-family 的 trace：

\[
b_1=b_2=5,
\]

\[
b_3=1025,
\quad
n_3=3,
\quad
D=550,
\quad
G=25,
\quad
a_3=101.
\]

对 raw A1-WGF residual 直接枚举：

\[
(a_1,a_2)\bmod2^k.
\]

对测试的 \(n=4,5,6\)，root counts 呈：

\[
\begin{array}{c|ccccccc}
2^k&2&4&8&16&32&64&128\\
\hline
\#\text{roots}
&2&4&8&16&32&64&0
\end{array}
\]

其后更深模数仍为 \(0\)。

所以该 particular projected \(5\)-family 并没有延伸成 \(\mathbf Z_2\) raw-WGF branch。

**状态：COMPUTATIONAL EVIDENCE ONLY.**

它强烈提示：

\[
\boxed{
\text{full raw WGF at }2
\text{ 比单纯 determinant parity 强得多}.
}
\]

但本报告不把 mod \(128\) 计算升级成 global theorem。

---

# 28. Counterexamples / pseudo-families

## 28.1 Frozen projected \(5\)-family仍可让 \(R_2=0\)

同一 PPF trace 中：

\[
b_3=1025
\]

为 odd。

且：

\[
D=550
\]

为 even，

\[
a_3=101
\]

为 odd。

若取 \(a_2\) odd，则：

\[
P\equiv a_2\equiv1\pmod2,
\]

从而：

\[
\Delta=b_3P-a_3D
\]

为 odd。

因此：

\[
\boxed{
R_2=0.
}
\]

上一轮的 \(5\)-adic congruences不固定 parity；用 ordinary CRT 可以在 projected family 中同时选择所需 \(5\)-classes 与 odd parity。

所以：

\[
\boxed{
\text{partial-5 projected same-cut data}
\not\Longrightarrow
R_2>0.
}
\]

**状态：NEW PROVED PROJECTED NEGATIVE RESULT.**

注意：该 family 本来就不满足 full BR-WGF，因此不能用来证明存在 genuine \(\mathbf Z_2\times\mathbf Z_5\) exact local survivor。

---

## 28.2 No arbitrary-depth full \(2\times5\) exact pseudo-family proved

本轮没有构造出满足：

\[
\text{WORD}
+
\text{CUT}
+
\text{RED}
+
\text{full raw WGF}
+
2\text{-phase}
+
5\text{-phase}
\]

的 arbitrary-depth \(\mathbf Z_2\times\mathbf Z_5\) family。

相反：

- previous genuine \(\mathbf Z_5\) UHL branch 被 \(2\)-side杀死；
- PPF trace 的 \(2\)-adic raw-WGF lifting 在计算上于 mod \(128\) 死亡。

因此 prompt 中的 Failure E：

\[
\boxed{
\text{arbitrary-depth full }2\times5\text{ local family}
}
\]

当前：

\[
\boxed{\textbf{NOT ESTABLISHED}.}
\]

---

# 29. Partial-\(5\) closure attempt

主 closure graph 原计划：

\[
\text{partial }5
\to
5\text{-cut}
\]

\[
+
\]

\[
2\text{-cut}
\to
\text{decimal suffix}
\to
\text{RED/NORM contradiction}.
\]

实际结果：

### Step A

\[
\boxed{
5\text{-cut}
}
\]

已冻结成立。

### Step B

\[
\boxed{
2\text{-cut}
}
\]

在 \(R_2>0\) branch 中严格成立。

### Step C

\[
\boxed{
R_2>0
}
\]

并非由 partial-\(5\) uniform 强迫。

### Step D

当两侧 phase 都存在时，CRT genuine decimal suffix成立。

### Step E

尚无 uniform suffix-reducedness / suffix-norm contradiction。

因此：

\[
\boxed{
0<v_5(b_3)<n_3
\Longrightarrow\varnothing
}
\]

本轮仍未证明。

**状态：OPEN.**

---

# 30. Surviving branch classification

partial-\(5\) survivors 现在至少应按 \(2\)-side分为：

## Type I — \(2\)-killed

full \(5\)-local branch存在，但 raw WGF parity / valuation在 \(2\) 上立即矛盾。

UHL 是 explicit theorem-level example。

---

## Type II — \(R_2>0\), true decimal suffix

存在 same determinant \(2\)-phase。

此时：

\[
J=\min(R_2,R_5)>0
\]

并可进入 genuine decimal suffix analysis。

该类目前未统一关闭。

---

## Type III — \(R_2=0\)

\(5\)-phase存在，但 \(2\)-side不穿透 actual \(P\)。

此时不存在真正 decimal suffix，只能保留：

\[
P\bmod5^{R_5}.
\]

这类是当前 CRT closure 的主要逃逸。

---

## Type IV — \(2\)-full absorption / parity-reversal

tail residual \(2\)-modulus消失，或 \(Z_-\) 恰好承担唯一一位 \(2\) 而 \(Z_+\) 承担剩余 depth。

这类不能用 partial-\(2\) formula硬套。

---

# 31. Exact missing relation if failure

本轮已经证明：

\[
\boxed{
\text{pure }5\text{-local information不足，}
}
\]

而：

\[
\boxed{
\text{adding }2\text{-local information能杀部分最强 branch，}
}
\]

但仍未得到 uniform closure。

因此若要求一个**真正独立、具体、不是“需要更多信息”**的下一 relation，本轮裁决为：

\[
\boxed{
\textbf{Ordinary-Integer / Common-Scale Decimal Realization}.
}
\]

其 forward-compatible 形式为：

存在同一个：

\[
\boxed{
U\in\mathbf Z_{>0}
}
\]

使 primitive numerator coordinates \(C_i\) 同时满足：

\[
\boxed{
a_i=UC_i,
}
\]

\[
\boxed{
10^{n_i-1}
\le
UC_i
<
10^{n_i}
\qquad(i=1,2,3),
}
\tag{CSNR}
\]

并有：

\[
\boxed{
\gcd(U,V)=1.
}
\]

在 backward semantic chart 中，它等价于要求 local \(2/5\)-adic cylinders 不是仅有 formal completion point，而是由**同一个 ordinary integer word**

\[
\mathbf A
=
S(a_1 10^n+a_2)+a_3
\]

实现，并且该 word 同时满足 full BR-WGF / CGS equality。

所以最小缺失 relation 不是“再加一个 prime”，而是：

\[
\boxed{
\textbf{local }(\mathbf Z_2\times\mathbf Z_5)
\textbf{ branch}
\;\cap\;
\textbf{one common Archimedean decimal scale}
\;\cap\;
\textbf{full exact CGS}.
}
\]

这与当前正向线暴露出的 common-\(U\) digit-window gate 正好对接，但本报告没有使用正向 theorem 来证明 backward 结论。

---

# 32. Migration to remaining \(5\)-chambers

由于 partial-\(5\) 未关闭，本轮不把 machinery 粗暴迁移到：

\[
v_5(b_3)=0
\]

或：

\[
v_5(b_3)\ge n_3.
\]

不过 general \(2\)-master identity：

\[
\ell_2
=
\nu_2+2\beta_2+2s_2
-2\gamma_2-n_3-c_2^+
\]

以及 general determinant-to-cut theorem：

\[
\ell_2>s_2
\Longrightarrow
P\bmod2^{\ell_2-s_2}
\]

对所有 A1 states 都有效。

所以这两条可以无损迁移。

partial-\(2\) 的简化 formula：

\[
R_2
=
\nu_2+2s_2-2\gamma_2-n_3-1
\]

则不可越过其 chamber assumptions。

---

# 33. PROVED / FAILED / OPEN ledger

## FROZEN

1. Strict frontier = A1-only；
2. actual cut
   \[
   P=a_1 10^n+a_2;
   \]
3. exact determinant
   \[
   \Delta=b_3P-a_3D;
   \]
4. exact bridge
   \[
   \Delta=Eh\varepsilon;
   \]
5. partial-\(5\) phase-to-cut theorem；
6. \(R_5\) formula；
7. pure \(5\)-adic same-cut Hensel survival；
8. strict-cut shielding；
9. projected arbitrary-depth \(5\)-pseudo-family。

---

## NEW PROVED

1. \(2\)-adic WGF master:
   \[
   \ell_2
   =
   \nu_2+2\beta_2+2s_2
   -2\gamma_2-n_3-c_2^+;
   \]

2. general A1 \(2\)-Phase-to-Cut theorem:
   \[
   \ell_2>s_2
   \Rightarrow
   P\equiv C_2\pmod{2^{\ell_2-s_2}};
   \]

3. partial-\(2\) normalization dictionary；

4. partial-\(2\) oriented parity allocation:
   \[
   R_2>0\Rightarrow v_2(Z_+)=1;
   \]

5. plus-factor exact valuation:
   \[
   v_2(C_+)=s_2+1;
   \]

6. partial-\(2\) exact cut depth:
   \[
   R_2
   =
   \nu_2+2s_2-2\gamma_2-n_3-1;
   \]

7. exact \(2\)-norm rigidity tree；

8. all partial-\(2\) denominator support formulas；

9. conditional CRT-to-decimal theorem；

10. UHL \(2\)-kill theorem；

11. projected partial-\(5\) does not force \(R_2>0\)。

---

## DERIVED

- if \(2\mid b_2\) and partial-\(2\) \(R_2>0\), then \(P\) is odd and determinant cancellation forces
  \[
  v_2(D)=s_2;
  \]
- if \(2,5\mid b_2\) and both phase transfers are candidate-derived, the last decimal digit is automatically a unit digit
  \[
  1,3,7,9;
  \]
- equal positive prefix \(2\)-support removes the parity tax in \(R_2\) because
  \[
  v_2(N)=2r+1.
  \]

---

## COMPUTATIONAL EVIDENCE

- PPF trace raw-WGF \(2\)-adic roots survive through mod \(64\) but disappear at mod \(128\) for tested \(n=4,5,6\)；
- small exact scans found no fully reduced A1 solutions in tested low boxes。

无 global nonexistence claim 依赖计算。

---

## DISPROVED / FAILED

1. mechanical \(5\mapsto2\) substitution；
2. partial-\(5\Rightarrow R_2>0\)；
3. \(R_2\) uniform deep lower bound；
4. \(J\ge1\) uniformly；
5. \(J\ge n\) uniformly；
6. mod \(10\) reducedness as uniform contradiction；
7. “2×5 CRT automatically closes partial-5”；
8. pure local decimal refinement as completed proof。

---

## OPEN

1. full partial-\(5\) nonexistence；
2. classification of exact Type-II \(R_2>0\) decimal-suffix survivors；
3. classification of exact Type-III \(R_2=0\) survivors；
4. ordinary-integer representative theorem for surviving local cylinders；
5. Common-Scale Numerator Realization / common-\(U\) digit-window gluing；
6. full A1-CGS；
7. full Strict Layer closure。

---

# 34. At most three next-round targets

## Target 1 — Exact Type-III \(R_2=0\) classification

不要继续 generic \(2\)-adic expansion。

只研究 partial-\(5\) survivors 中：

\[
\boxed{
v_2(\Delta)\le v_2(b_3).
}
\]

目标是判定：

\[
R_2=0
\]

是否迫使一个极小的 parity/content profile，例如：

\[
s_2=0,
\]

特定：

\[
(a_2,D,a_3)\bmod2^k,
\]

以及对应 full raw-WGF unit equation。

这是当前 CRT route 的唯一真正逃逸门。

---

## Target 2 — Full raw-WGF \(2\)-adic unit closure on surviving \(5\)-branches

UHL 已经显示：

\[
\boxed{
\mathbf Z_5\text{ survivor}
\not\Rightarrow
\mathbf Z_2\text{ survivor}.
}
\]

下一轮应直接对第三轮 surviving canonical \(5\)-branches 加入 raw-WGF 的 \(2\)-adic **unit equation**，而不只检查 \(R_2\)。

目标：

\[
\boxed{
\text{same }5\text{-Hensel branch}
\cap
\text{exact }2\text{-adic WGF}
=
\varnothing?
}
\]

这比继续增加 \(v_2\)-inequality 更接近真正 closure。

---

## Target 3 — Local branch \(\to\) common ordinary decimal scale

若仍有 \(\mathbf Z_2\times\mathbf Z_5\) exact local branches，则立即停止局部 refinement，转入：

\[
\boxed{
\textbf{Common-Scale Numerator Realization}.
}
\]

即研究 local completion branch 是否存在同一个普通整数：

\[
U
\]

同时满足三块 digit windows、actual cut、reducedness 与 full CGS。

这应是 backward 与当前 forward common-\(U\) frontier 的第一次真正对接点。

---

# 35. Answers to Q1–Q11

## Q1 — A1 中是否存在真正非平凡的 same-determinant \(2\)-phase？

\[
\boxed{\textbf{YES.}}
\]

而且来源完全是 A1 自身：

\[
\Delta=b_3P-a_3D
\]

与 raw WGF，不依赖 DD。

---

## Q2 — 能否严格传递到 actual \(P\)？

\[
\boxed{\textbf{YES, whenever }v_2(\Delta)>v_2(b_3).}
\]

有：

\[
P\equiv C_2\pmod{2^{R_2}}.
\]

---

## Q3 — \(R_2\) exact formula 是什么？

general exact source formula：

\[
\ell_2
=
\nu_2+2\beta_2+2s_2
-2\gamma_2-n_3-c_2^+.
\]

cut depth：

\[
R_2=(\ell_2-s_2)_+.
\]

partial-\(2\)、cut-visible 时简化为：

\[
\boxed{
R_2
=
\nu_2+2s_2-2\gamma_2-n_3-1.
}
\]

---

## Q4 — \(2\)-adic norm 是否更刚性？

\[
\boxed{\textbf{YES, decisively.}}
\]

equal support 时：

\[
v_2(N)=2t+1
\]

精确固定，没有 \(5\)-adic \(\lambda_N\)-type Hensel excess。

---

## Q5 — CRT decimal depth \(J\) 有多大？

\[
\boxed{
J=\min(R_2,R_5).
}
\]

但本轮没有 uniform positive lower bound。

---

## Q6 — 是否统一锁定 \(a_2\bmod10\)？

\[
\boxed{\textbf{NO uniformly.}}
\]

只在：

\[
R_2,R_5\ge1
\]

的 branch 中成立。

---

## Q7 — decimal suffix + reducedness 是否直接矛盾？

\[
\boxed{\textbf{NO uniformly.}}
\]

在 candidate-derived both-support branch 中，末位 unit condition往往自动兼容。

---

## Q8 — 加 exact norm 后是否关闭？

\[
\boxed{\textbf{NOT globally.}}
\]

但 exact \(2\)-norm / WGF 已经杀掉 previous UHL branch，这是实质进展。

---

## Q9 — partial-\(5\) chamber是否关闭？

\[
\boxed{\textbf{NO.}}
\]

---

## Q10 — 是否有 arbitrary-depth full \(2\times5\) same-cut compatible pseudo-family？

\[
\boxed{\textbf{NOT PROVED.}}
\]

当前反而有证据表明一些最强 \(5\)-branches在 \(2\)-side死亡。

---

## Q11 — 若 \(2\times5\) 仍不足，最小独立 relation 是什么？

\[
\boxed{
\textbf{Ordinary-Integer / Common-Scale Numerator Realization}
}
\]

即同一个 ordinary integer scale / word 必须同时实现：

\[
2\text{-local branch},
\quad
5\text{-local branch},
\quad
\text{actual decimal windows},
\quad
\text{actual cut},
\quad
\text{full CGS}.
\]

这已经不是继续增加 decimal-local lemma，而是 local-to-global integer realization gate。

---

# Final research verdict

本轮最关键的结构变化不是“又多一个 \(2\)-adic inequality”，而是：

\[
\boxed{
\textbf{A1 same-determinant }2\textbf{-phase 真正存在，且能穿透到 actual }P.
}
\]

更重要的是：

\[
\boxed{
\textbf{它确实杀掉了上一轮最强的 genuine }\mathbf Z_5\textbf{ local survivor。}
}
\]

所以：

\[
\boxed{
2\times5
}
\]

不是虚假的组合方向。

但同样重要的负结果是：

\[
\boxed{
\textbf{partial-5 并不自动提供 nontrivial }2\textbf{-phase。}
}
\]

因此当前最准确的新 frontier 是：

\[
\boxed{
\textbf{Exact }R_2=0\textbf{ escape classification}
}
\]

与：

\[
\boxed{
\textbf{surviving }(\mathbf Z_2\times\mathbf Z_5)
\textbf{ local branches}
\to
\textbf{one ordinary decimal scale}.
}
\]

换言之，本轮已经把问题从：

\[
\boxed{
\text{“5-adic precision 是否够深？”}
}
\]

推进为：

\[
\boxed{
\textbf{“一个 exact local branch 是否真的来自同一个普通十进制整数候选？”}
}
\]

这正是当前 backward A1 最小的新终局接口。
