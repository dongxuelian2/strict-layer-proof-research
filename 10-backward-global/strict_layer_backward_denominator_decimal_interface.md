# Backward Strict Layer：Denominator–Decimal Explicit Recovery Interface

**文件：** `strict_layer_backward_denominator_decimal_interface.md`  
**研究对象：** 三项十进制拼接平方和问题，Backward Strict Layer  
**本轮唯一目标：** denominator recovery 与 decimal recovery 的显式、proper、可证明同步接口  
**最终状态：** **Outcome A（在重新清洗后的 canonical denominator-recovery block 与 decimal-completion block 之间得到 lossless pairwise interface）**；同时明确说明旧的 broad arithmetic/denominator block 为什么不能原样用于该定理。

---

# 1. Executive summary

本轮最重要的结论不是再定义一个抽象 quotient，而是把 denominator–decimal 的共享信息完全算术化。

首先固定记号冲突。令 canonical common denominator 为

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\]

而把旧 Exact-Lift 中第三尾正规化所写的 \(\delta_3,L,\tau\) 改记为

\[
\eta_3:=\gcd(10^\ell,b_3),\qquad
\mathcal L:=\frac{10^\ell}{\eta_3},\qquad
\tau:=\frac{b_3}{\eta_3}.
\]

这里 \(\eta_3\) 是 **tail gcd**，不能与 digit difference 混用；\(\mathcal L\) 是 **tail quotient**，不能与 canonical common denominator \(\Lambda\) 混用。

定义

\[
M_i:=10^{m_i},\qquad
S:=10^\ell,
\]

以及 denominator word

\[
B=b_1M_2M_3+b_2M_3+b_3.
\]

本轮得到的显式 interface 有两个完全等价的正规形：

\[
\boxed{
T_{\rm blk}(v)=(b_1,b_2,b_3,S)
}
\tag{1.1}
\]

和

\[
\boxed{
T_{\rm word}(v)=(B,M_2,M_3,S).
}
\tag{1.2}
\]

其中 \(T_{\rm blk}\) 是 intrinsic block form，\(T_{\rm word}\) 是 decimal-word form。二者互相唯一恢复，因此表示同一个 arithmetic quotient，而不是两个不同 interface。

**NEW PROVED — Explicit Denominator–Decimal Interface Theorem.**  
在重新定义后的 canonical denominator-recovery block 与 decimal-completion block 上，所有真正的 denominator–decimal cross-synchronization 都 factor through (1.1)/(1.2)。更精确地：

1. 从 \(T\) 唯一恢复全部三个 reduced denominators；
2. 唯一恢复 denominator block boundaries；
3. 唯一恢复 \(\Lambda\)、\(d_i=\Lambda/b_i\)、全部 denominator valuation/gcd profile；
4. 唯一恢复第三尾 split \((\eta_3,\mathcal L,\tau)\)；
5. 唯一恢复 Exact-Lift 的 denominator prefix objects \(Q,G\)；
6. 在 Exact-Lift admissible locus 上，统一恢复整数尾权 \(\kappa\)；
7. denominator-tail certificate 成为一个纯 \(T\)-predicate；
8. exact decimal balance \(\Lambda A=tB\) 中来自 denominator side 的全部数据恰为 \((\Lambda,B)\)，仍由 \(T\) 唯一恢复。

最关键的新压缩是：旧报告分别写成

\[
\kappa=\frac{\mathcal LQG}{\tau}
\qquad(DD),
\]

和

\[
\kappa=10^g\frac{\mathcal LQG}{\tau}
\qquad(A_1),
\]

但因为

\[
S=10^\ell,\qquad
\frac{\mathcal L}{\tau}=\frac{S}{b_3},
\]

而在 \(A_1\) 中 \(g=m_3-\ell\)，所以两式严格统一为

\[
\boxed{
\kappa
=
\frac{M_3QG}{b_3}.
}
\tag{1.3}
\]

因此

\[
\boxed{
S\mid \kappa^2(\kappa+2G)
}
\tag{1.4}
\]

完全是 interface arithmetic：不读取 \(x_i\)、\(a_i\)、\(\mu,\nu\)、\(C,D\) 或 \(\mathcal N_{12}\)。

另一方面，interface 是 genuinely proper。事实上不仅存在 collision，而且存在一个无限 fibre：对每个 \(r\ge3\)，

\[
v_r=(1,2r,2r^2,1)
\]

满足

\[
1^2+(2r)^2+(2r^2)^2=(2r^2+1)^2,
\]

其 recovered denominators 全为 \(1\)，并都落入 DD-sign region，且

\[
T_{\rm word}(v_r)=(111,10,10,10).
\]

故

\[
\#T^{-1}(111,10,10,10)=\infty
\]

在 ambient strict recovery space 上成立。于是该 interface 严格遗忘 canonical numerator/sphere information，properness 不是 tuple-length 意义上的伪压缩。

最后，对清洗后的 semantic blocks 有

\[
\boxed{
J_{\rm den,10}
=
D_{\rm den}
\times_{\mathcal T_{\rm den,10}}
D_{10}.
}
\tag{1.5}
\]

并且该显式 \(T\) 与上一轮 abstract maximal common factor \(\Sigma_{\rm den,10}^{\rm abs}\) 在本轮语义块定义下 **proven equivalent**。

---

# 2. Anti-duplication boundary

本轮不使用 interface 去攻击：

- moving primitive core；
- \(Q_0\to\infty\)；
- square-spacing；
- deflated quadratic gate；
- DD post-deflation small factor \(J=M-Y\)；
- \(2\)-adic / \(5\)-adic capacity growth；
- near-square termination；
- height estimates；
- resultant / polynomial coupling；
- reachable-set shrinking。

特别地，虽然 (1.4) 可以继续做 valuation growth，本报告只证明它已经被压成 interface predicate，不继续利用它产生 large-height contradiction。

本报告也不把 \(D_{\rm alg}\) 加进 fibre product。所有 \(\mu,\nu,C,D,\mathcal N_{12},z_3\) 等 algebraic/root quantities 若与 denominator arithmetic 相遇，统一标记为 **alg–den coupling**，不伪装成 den–decimal overlap。

---

# 3. Source audit and notation repair

## 3.1 Canonical recovery

既有基础定理给出 canonical recovery：对

\[
v=(x_1,x_2,x_3,\Lambda),
\qquad
\gcd(x_1,x_2,x_3,\Lambda)=1,
\]

令

\[
d_i=\gcd(x_i,\Lambda).
\]

则

\[
\boxed{
a_i=\frac{x_i}{d_i},
\qquad
b_i=\frac{\Lambda}{d_i}.
}
\tag{3.1}
\]

反过来，canonical condition 保证

\[
\boxed{
\Lambda=\operatorname{lcm}(b_1,b_2,b_3).
}
\tag{3.2}
\]

这说明 denominator recovery 的 intrinsic mathematical output 是 reduced denominator triple \((b_1,b_2,b_3)\) 及其 canonical lcm/gcd profile，而不是某个 proof label。

## 3.2 Decimal reconstruction

令

\[
n_i=\operatorname{digits}(a_i),
\qquad
m_i=\operatorname{digits}(b_i).
\]

则

\[
A=a_1 10^{n_2+n_3}+a_2 10^{n_3}+a_3,
\]

\[
\boxed{
B=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3.
}
\tag{3.3}
\]

canonical exact balance 是

\[
\boxed{
\Lambda A=tB.
}
\tag{3.4}
\]

因此 decimal completion 真正从 denominator side 读取的是 denominator word 及其 segmentation，以及由它得到的 \(\Lambda\)。

## 3.3 Effective third-tail normalization

Existing Exact-Lift 给出有效尾长

\[
\ell=
\begin{cases}
m_3,&DD,\\
m_3-g,&A_1,
\end{cases}
\tag{3.5}
\]

其中 \(A_1\) 中

\[
g=-s_3=m_3-n_3\ge0.
\]

所以在 strict layer 中

\[
\boxed{
\ell=
\begin{cases}
m_3,&DD,\\
n_3,&A_1.
\end{cases}
}
\tag{3.6}
\]

定义

\[
S:=10^\ell,
\]

再定义

\[
\boxed{
\eta_3:=\gcd(S,b_3),
\qquad
\mathcal L:=\frac{S}{\eta_3},
\qquad
\tau:=\frac{b_3}{\eta_3}.
}
\tag{3.7}
\]

于是

\[
\gcd(\mathcal L,\tau)=1,
\qquad
S=\eta_3\mathcal L,
\qquad
b_3=\eta_3\tau.
\tag{3.8}
\]

**DERIVED FROM PROVED RESULTS.**  
这立刻说明旧 tuple

\[
(\eta_3,\mathcal L,\tau,\ell,b_3,S)
\]

不是六份独立信息；只要知道 \((b_3,S)\)，其余全部唯一恢复。

---

# 4. Exact semantic denominator block

上一轮 broad \(R_{\rm den}\) 把以下东西混在一起：

- canonical denominator recovery；
- denominator prime graph；
- tail split；
- root rationality divisibility；
- primitive quadratic divisibility；
- algebraic discriminant data。

这对全局 obstruction map 有用，但对本轮 **denominator–decimal common factor** 太宽。

本轮重新定义：

\[
\boxed{
\lambda_{\rm den}:
\Omega_{\rm rec}^{\rm str}
\to D_{\rm den}
}
\]

只表示 **canonical denominator-recovery closure**，即以下数学数据及它们的 deterministic views：

1. reduced denominator triple \((b_1,b_2,b_3)\)；
2. canonical common denominator \(\Lambda\)；
3. gcd profile \((d_1,d_2,d_3)\)；
4. denominator digit lengths \((m_1,m_2,m_3)\)；
5. denominator word \(B\)；
6. prefix quantities
   \[
   Q=b_1 10^{m_2}+b_2,
   \qquad
   G=b_1b_2;
   \]
7. effective tail request \(S=10^\ell\)；
8. tail split \((\eta_3,\mathcal L,\tau)\)；
9. all denominator-only valuation/gcd/prime-support views；
10. on the Exact-Lift admissible locus, the denominator-determined tail weight \(\kappa\) and denominator-tail certificate.

以下量 **不再放入** \(D_{\rm den}\)：

\[
\mu,\nu,C,D,\mathcal N_{12},z_3,a_3,\mathcal C_3,W.
\]

原因不是这些量“不重要”，而是它们不是 denominator recovery 的自由度：

- \(\mu,\nu,W\) 是 root/algebraic recovery；
- \(C,D,\mathcal N_{12}\) 含 numerator/algebraic information；
- \(z_3=a_3/\eta_3\) 明确读取 numerator；
- \(a_3\mid\mathcal C_3\) 是 alg–den certificate，而不是 den–decimal interface datum。

这一步是本轮最重要的 semantic cleanup。

---

# 5. Exact semantic decimal block

定义

\[
\boxed{
\lambda_{10}:
\Omega_{\rm rec}^{\rm str}
\to D_{10}.
}
\]

不把完整 canonical state 生硬复制进 \(D_{10}\)。相反，将它拆成

\[
\boxed{
\lambda_{10}(v)
=
F_{10}\bigl(T_{10}^{\rm den}(v),\lambda_{10}^{\rm local}(v)\bigr).
}
\tag{5.1}
\]

其中 denominator-facing port 是

\[
\boxed{
T_{10}^{\rm den}(v)
=(B,M_2,M_3,S),
}
\tag{5.2}
\]

而 \(\lambda_{10}^{\rm local}\) 只保留 decimal completion 自己的 local information，例如：

- numerator-side digit information；
- numerator word/coefficient-plane local contribution；
- carry / digit-cell data；
- positivity / no-leading-zero local checks；
- exact balance 中的 local side \((A,t)\) 或相应 residual；
- 不来自 denominator recovery 的 decimal constraints。

关键点是：decimal block 中所有 **来自 denominator side 的 coefficient / modulus / block boundary / exact-balance data** 都必须由 (5.2) 提供，而不能偷偷在 local part 再保存一份 denominator tuple。

---

# 6. Raw overlap inventory

下面把主要 quantity 按本轮语义重新分类。

| quantity | den reads/outputs? | decimal reads/outputs? | deterministic from | classification |
|---|---:|---:|---|---|
| \(b_1,b_2,b_3\) | yes | yes | final \(T\) | **literal core overlap** |
| \(m_i\) | yes (digit profile) | yes | \(b_i\) | redundant deterministic overlap |
| \(B\) | yes as denominator word view | yes | \((b_i,m_i)\) | deterministic overlap |
| \(\Lambda\) | yes | yes in exact balance | \(\operatorname{lcm}(b_i)\) | deterministic overlap |
| \(d_i\) | yes | no independent need | \(\Lambda/b_i\) | den-local deterministic view |
| \(S=10^\ell\) | yes for tail split/certificate | yes | final \(T\) | **literal core overlap** |
| \(\ell\) | yes | yes | \(S\) | redundant representation |
| \(\eta_3\) | yes | yes in tail normalization | \(\gcd(S,b_3)\) | redundant overlap |
| \(\mathcal L\) | yes | yes in tail formulas | \(S/\eta_3\) | redundant overlap |
| \(\tau\) | yes | yes in tail formulas | \(b_3/\eta_3\) | redundant overlap |
| \(Q\) | yes in tail formulas | denominator coefficient in decimal/Exact-Lift | \(b_1M_2+b_2\) | redundant overlap |
| \(G\) | yes | denominator coefficient | \(b_1b_2\) | redundant overlap |
| \(\kappa\) | yes | tail arithmetic | \(M_3QG/b_3\) on EL locus | redundant overlap |
| denominator valuation profile | yes | some digit/tail checks | \((b_i,S)\) | redundant overlap |
| tail modulus | yes | yes | \(S\) | redundant overlap |
| tail representative \(b_3\) | yes | yes | final \(T\) | literal core overlap |
| \(a_i\) | no in den-core | yes/local | canonical numerator data | **not den–decimal shared** |
| \(n_i\) | only through \(S\) in \(A_1\) | yes | local; projection \(S\) shared | deterministic projection overlap |
| \(A\) | no | yes | numerator decimal local | not den–decimal shared |
| \(t\) | no | yes/algebraic | sphere/algebraic | not den–decimal shared |
| \(\mu,\nu\) | no in den-core | no direct decimal need | algebraic/root | apparent overlap |
| \(C,D,\mathcal N_{12}\) | no in den-core | coefficient/algebraic local | numerator + prefix | alg–decimal / alg–den |
| \(z_3\) | no in den-core | numerator/tail algebra | \(a_3,\eta_3\) | apparent den–decimal overlap |

**NEW PROVED.**  
因此本轮真正不可消除的共享 arithmetic information 不是

\[
(\eta_3,\mathcal L,\tau,\ell,b_3,\Lambda,\ldots)
\]

这样的长列表，而是：

\[
\boxed{
\text{complete denominator block-word information}
+
\text{effective tail scale }S.
}
\]

---

# 7. Deterministic overlap elimination

## 7.1 Tail tuple collapses to \((b_3,S)\)

由 (3.7)：

\[
\eta_3=\gcd(S,b_3),
\]

\[
\mathcal L=S/\eta_3,
\qquad
\tau=b_3/\eta_3.
\]

所以

\[
\boxed{
(b_3,S)
\Longleftrightarrow
(S,b_3,\eta_3,\mathcal L,\tau)
}
\tag{7.1}
\]

在 admissible tail image 上是 lossless deterministic equivalence。

## 7.2 \(\ell\) 不需要单独保存

因为 \(S\) 被限制为正整数十次幂，

\[
\ell=\log_{10}S
\]

唯一恢复。

## 7.3 \(\Lambda\) 不需要单独保存

canonical T3 给出

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3).
\]

因此 \(\Lambda\) 是 denominator triple 的 deterministic view。

## 7.4 \(d_i\) 不需要单独保存

\[
d_i=\frac{\Lambda}{b_i}.
\]

## 7.5 \(Q,G\) 不需要单独保存

\[
Q=b_1M_2+b_2,
\qquad
G=b_1b_2.
\]

## 7.6 \(\kappa\) 也不需要单独保存

见下一节的新统一恒等式。

---

# 8. New arithmetic compression: a branch-free denominator formula for \(\kappa\)

这是本轮最具体的新算术结论。

Existing Exact-Lift 在 DD 中给出

\[
\kappa=\frac{\mathcal LQG}{\tau}.
\tag{8.1}
\]

在 \(A_1\) 中给出

\[
\kappa=10^g\frac{\mathcal LQG}{\tau}.
\tag{8.2}
\]

由

\[
\frac{\mathcal L}{\tau}
=
\frac{S/\eta_3}{b_3/\eta_3}
=
\frac{S}{b_3},
\tag{8.3}
\]

DD 中 \(S=M_3\)，故

\[
\kappa=\frac{M_3QG}{b_3}.
\tag{8.4}
\]

而 \(A_1\) 中

\[
g=m_3-\ell,
\]

所以

\[
10^gS
=10^{m_3-\ell}10^\ell
=M_3.
\]

代入 (8.2)：

\[
\kappa
=10^g\frac{SQG}{b_3}
=\frac{M_3QG}{b_3}.
\tag{8.5}
\]

因此：

\[
\boxed{
\textbf{NEW PROVED:}
\qquad
\kappa
=
\frac{M_3QG}{b_3}
=
\frac{10^{m_3}(b_1 10^{m_2}+b_2)b_1b_2}{b_3}
}
\tag{8.6}
\]

同时覆盖 DD 与 \(A_1\)，不需要 branch label。

这带来两个直接后果。

### 8.1 \(\kappa\) 是纯 denominator-word quantity

一旦 denominator blocks 及其 boundaries 已固定，\(\kappa\) 已固定；有效尾长 \(\ell\) 甚至不参与 \(\kappa\) 本身。

### 8.2 denominator-tail certificate 是纯 interface predicate

Existing certificate

\[
S\mid\kappa^2(\kappa+2G)
\]

现在可以写成

\[
\boxed{
S
\mid
\left(\frac{M_3QG}{b_3}\right)^2
\left(
\frac{M_3QG}{b_3}+2G
\right).
}
\tag{8.7}
\]

在 Exact-Lift admissible locus 上括号中的 \(\kappa\) 已知为整数。

因此 prompt 中的问题 D 得到明确回答：

> denominator-tail certificate 不需要任何额外 \((x_1,x_2,x_3)\) 数据。  
> 它确实需要第三尾 split 之外的 prefix denominator information，但该信息恰由 \((b_1,b_2,m_2)\)，即完整 denominator word 的前缀部分提供。

---

# 9. Candidate traces and stress tests

## 9.1 Candidate C0: tail scale only

\[
T^{(0)}=S.
\]

**DISPROVED CANDIDATE.**  
显然无法恢复任何 denominator word 信息。

## 9.2 Candidate C1: third-tail only

\[
T^{(1)}=(b_3,S).
\]

它足以恢复 \((\eta_3,\mathcal L,\tau)\)，但不能恢复 \(B,\Lambda,Q,G\)。

**DISPROVED CANDIDATE.**  
例如下面两个 ambient strict recovery states 都有 \((b_3,S)=(1,10)\)：

\[
(a;b)=(1,6,18;\ 1,1,1),
\]

\[
(a;b)=(1,10,10;\ 1,11,1),
\]

但 denominator word 分别为 \(111\) 与 \(1111\)，canonical \(\Lambda\) 也分别为 \(1\) 与 \(11\)。

所以 tail normalization 不是完整 den–decimal interface。

## 9.3 Candidate C2: denominator word + tail scale, no cuts

\[
T^{(2)}=(B,S).
\]

**DISPROVED CANDIDATE by actual canonical collision.**

状态 I：

\[
(a_1,a_2,a_3)=(1,10,10),
\qquad
(b_1,b_2,b_3)=(1,11,1),
\]

\[
\Lambda=11,
\qquad
(x_1,x_2,x_3)=(11,10,110),
\qquad
t=111,
\]

满足

\[
11^2+10^2+110^2=111^2.
\]

状态 II：

\[
(a_1,a_2,a_3)=(1,2,22),
\qquad
(b_1,b_2,b_3)=(11,1,1),
\]

\[
\Lambda=11,
\qquad
(x_1,x_2,x_3)=(1,22,242),
\qquad
t=243,
\]

满足

\[
1^2+22^2+242^2=243^2.
\]

两者都是 canonical，且都处在 DD-sign region；都有

\[
B=1111,
\qquad
S=10,
\]

但 block segmentation 不同。因此 \((B,S)\) 不能恢复 denominator triple。

## 9.4 Candidate C3: retain third cut but delete second cut

\[
T^{(3)}=(B,M_3,S).
\]

上面同一对状态仍给出

\[
(B,M_3,S)=(1111,10,10),
\]

但

\[
M_2=100
\quad\text{vs}\quad
M_2=10.
\]

故：

\[
\boxed{M_2\text{ cannot be deleted}.}
\]

这里不是形式字符串反例，而是两个真实 canonical sphere states。

## 9.5 Candidate C4: retain second cut but delete third cut

\[
T^{(4)}=(B,M_2,S).
\]

**DISPROVED CANDIDATE by actual canonical collision.**

状态 III：

\[
(a;b)=(1,188,60;\ 111,1,1),
\]

\[
\Lambda=111,
\qquad
x=(1,20868,6660),
\qquad
t=21905,
\]

且

\[
1^2+20868^2+6660^2=21905^2.
\]

它处在 DD-sign region，

\[
(B,M_2,M_3,S)=(11111,10,10,10).
\]

状态 IV：

\[
(a;b)=(47,102,6;\ 11,1,11),
\]

\[
\Lambda=11,
\qquad
x=(47,1122,6),
\qquad
t=1123,
\]

且

\[
47^2+1122^2+6^2=1123^2.
\]

其 digit differences 满足

\[
s_2=2,
\qquad
s_3=-1,
\qquad
s_2+s_3=1,
\]

所以落入 \(A_1\)-sign region，并有有效尾长 \(\ell=1\)，于是

\[
(B,M_2,M_3,S)=(11111,10,100,10).
\]

两者具有相同

\[
(B,M_2,S)=(11111,10,10),
\]

但 \(M_3\) 不同。因此：

\[
\boxed{M_3\text{ cannot be deleted}.}
\]

## 9.6 Candidate C5: delete effective tail scale

\[
T^{(5)}=(B,M_2,M_3).
\]

在 DD 中 \(S=M_3\)，所以单独看 DD，\(S\) 确实冗余。

但 uniform strict interface 必须同时覆盖 \(A_1\)。下面两个 canonical states denominator triple 完全相同：

\[
(b_1,b_2,b_3)=(1,1,100),
\qquad
(B,M_2,M_3)=(11100,10,1000).
\]

状态 V：

\[
(a_1,a_2,a_3)=(1,11,137),
\]

\[
\Lambda=100,
\qquad
x=(100,1100,137),
\qquad
t=1113,
\]

\[
100^2+1100^2+137^2=1113^2.
\]

这里

\[
s_2=1,
\qquad s_3=0,
\]

故 \(A_1\)-sign profile 有

\[
\ell=n_3=3,
\qquad S=1000.
\]

状态 VI：

\[
(a_1,a_2,a_3)=(2,212,49),
\]

\[
\Lambda=100,
\qquad
x=(200,21200,49),
\qquad
t=21201,
\]

\[
200^2+21200^2+49^2=21201^2.
\]

这里

\[
s_2=2,
\qquad s_3=-1,
\]

故

\[
\ell=n_3=2,
\qquad S=100.
\]

因此 denominator triple 本身不能决定 \(A_1\) 的 effective tail scale。

\[
\boxed{
S\text{ is necessary for the uniform DD + }A_1\text{ interface}.}
\]

---

# 10. Final explicit trace

经过上述删减与反例压力测试，冻结：

\[
\boxed{
T_{\rm den,10}^{\rm word}(v)
=
(B,M_2,M_3,S).
}
\tag{10.1}
\]

其中

\[
M_i=10^{m_i},
\qquad
S=10^\ell.
\]

其 intrinsic block form 为

\[
\boxed{
T_{\rm den,10}^{\rm blk}(v)
=
(b_1,b_2,b_3,S).
}
\tag{10.2}
\]

## 10.1 Word form \(\Rightarrow\) block form

设

\[
P=\left\lfloor\frac{B}{M_3}\right\rfloor.
\]

则

\[
\boxed{
b_3=B\bmod M_3,}
\tag{10.3}
\]

\[
\boxed{
b_2=P\bmod M_2,}
\tag{10.4}
\]

\[
\boxed{
b_1=\left\lfloor\frac{P}{M_2}\right\rfloor.}
\tag{10.5}
\]

在 trace image 中自动有 digit-window conditions

\[
\frac{M_2}{10}\le b_2<M_2,
\qquad
\frac{M_3}{10}\le b_3<M_3,
\qquad
b_1\ge1,
\]

所以恢复没有 leading-zero ambiguity。

## 10.2 Block form \(\Rightarrow\) word form

由 \(b_i\) 取实际十进制位数

\[
m_i=\operatorname{digits}(b_i),
\qquad
M_i=10^{m_i},
\]

再由 (3.3) 唯一恢复 \(B\)。

因此：

\[
\boxed{
T_{\rm den,10}^{\rm word}
\simeq
T_{\rm den,10}^{\rm blk}
}
\tag{10.6}
\]

是 proven arithmetic equivalence。

这里没有声称“4 个坐标比 4 个 canonical coordinates 更低维”；真正的压缩来自下一节的 fibre theorem。

---

# 11. Factorization theorem

## Theorem 11.1 — Denominator factorization

**NEW PROVED.**  
存在显式 deterministic map \(F_{\rm den}\)，使

\[
\boxed{
\lambda_{\rm den}(v)
=
F_{\rm den}\bigl(T_{\rm den,10}(v)\bigr).
}
\tag{11.1}
\]

证明逐项如下。

从 \(T\) 解码 \(b_1,b_2,b_3\)。于是：

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\]

\[
d_i=\Lambda/b_i,
\]

\[
m_i=\operatorname{digits}(b_i),
\]

\[
Q=b_1M_2+b_2,
\qquad
G=b_1b_2,
\]

\[
\eta_3=\gcd(S,b_3),
\]

\[
\mathcal L=S/\eta_3,
\qquad
\tau=b_3/\eta_3.
\]

全部 denominator valuation / prime-support / gcd data 因此唯一确定。

在 Exact-Lift admissible locus，进一步有

\[
\kappa=M_3QG/b_3,
\]

所以 tail certificate 的 truth value 也由 \(T\) 唯一决定。

证毕。

## Theorem 11.2 — Decimal factorization

**NEW PROVED at the semantic-interface level.**  
存在 decimal-local state \(\lambda_{10}^{\rm local}\) 与 deterministic map \(F_{10}\)，使

\[
\boxed{
\lambda_{10}(v)
=
F_{10}
\left(
T_{\rm den,10}(v),
\lambda_{10}^{\rm local}(v)
\right).
}
\tag{11.2}
\]

而 \(\lambda_{10}^{\rm local}\) 不保存 denominator tuple 的副本。

证明的实质是 denominator-origin inputs 全部由 \(T\) 重建：

- denominator blocks；
- block boundaries；
- denominator word \(B\)；
- canonical \(\Lambda\)；
- effective tail modulus \(S\)；
- \((\eta_3,\mathcal L,\tau)\)；
- \(Q,G,\kappa\) 等 denominator coefficients。

exact balance

\[
\Lambda A=tB
\]

中 denominator side 只剩

\[
(\Lambda,B),
\]

二者均为 \(T\)-functions；\((A,t)\) 属 decimal/algebraic local side。

因此固定 \(T\) 后，decimal block 不需要再次询问 denominator block 任何额外 mathematical datum。

证毕。

---

# 12. Pairwise synchronization theorem

令

\[
\mathcal T_{\rm den,10}
=
\operatorname{Im}T_{\rm den,10}.
\]

令

\[
\rho_{\rm den}:D_{\rm den}\to\mathcal T_{\rm den,10},
\qquad
\rho_{10}:D_{10}\to\mathcal T_{\rm den,10}
\]

为自然 trace maps。

由 Theorem 11.1，denominator state 对固定 \(T\) 是唯一的：存在 \(h\) 使

\[
\lambda_{\rm den}=h\circ T.
\tag{12.1}
\]

现在设

\[
(d,e)
\in
D_{\rm den}
\times_{\mathcal T_{\rm den,10}}
D_{10}.
\]

因为 \(e\in D_{10}=\operatorname{Im}\lambda_{10}\)，存在某个 canonical recovery state \(v\) 使

\[
\lambda_{10}(v)=e.
\]

于是

\[
T(v)=\rho_{10}(e)=\rho_{\rm den}(d).
\]

而 denominator state 由该 trace 唯一决定，故

\[
\lambda_{\rm den}(v)
=h(T(v))
=d.
\]

所以

\[
(d,e)
=(\lambda_{\rm den}(v),\lambda_{10}(v))
\in J_{\rm den,10}.
\]

反向包含显然成立。

因此：

\[
\boxed{
\textbf{NEW PROVED:}
\qquad
J_{\rm den,10}
=
D_{\rm den}
\times_{\mathcal T_{\rm den,10}}
D_{10}.
}
\tag{12.2}
\]

这给出本轮要求的 lossless pairwise join。

## 12.1 为什么这不是循环定义

我们没有令

\[
T=(\lambda_{\rm den},\lambda_{10}).
\]

而是明确给出

\[
T=(B,M_2,M_3,S),
\]

并从十进制除法、lcm、gcd 与 Exact-Lift 的 tail identities 显式证明两 block 的 cross-dependence factor through 它。

## 12.2 为什么旧 broad \(R_{\rm den}\) 不能直接套这个 theorem

如果把 \(\mu,\nu,C,D,\mathcal N_{12},z_3,W\) 等 algebraic/root data 强行继续塞进 denominator block，那么固定 \(T\) 后 denominator state 不再唯一；这会重新制造“hidden residual coupling”。

但这不是 den–decimal coupling，而是把 alg–den edge 错塞进 den node 后造成的 presentation dependence。

所以本轮 theorem 的一个实质内容就是：

\[
\boxed{
R_{\rm den}^{\rm old}
\rightsquigarrow
D_{\rm den}^{\rm recovery}
+
D_{\rm alg\leftrightarrow den}^{\rm certificate}.
}
\tag{12.3}
\]

只有第一项属于本轮 pairwise interface。

---

# 13. Properness theorem

## Theorem 13.1 — Infinite recovery fibre

**NEW PROVED.**  
\(T_{\rm den,10}\) 在 ambient strict recovery space 上不是 injective；事实上存在无限 fibre。

对任意整数 \(r\ge3\)，取

\[
\Lambda=1,
\qquad
(x_1,x_2,x_3)=(1,2r,2r^2).
\]

则

\[
1^2+(2r)^2+(2r^2)^2
=1+4r^2+4r^4
=(2r^2+1)^2.
\]

所以

\[
v_r=(1,2r,2r^2,1)\in\Omega_{\rm rec}.
\]

因为 \(\Lambda=1\)，有

\[
d_1=d_2=d_3=1,
\]

\[
b_1=b_2=b_3=1.
\]

于是

\[
B=111,
\qquad
M_2=M_3=10.
\]

当 \(r\ge3\) 时

\[
a_3=2r^2\ge18,
\]

故 \(s_3>0\)，且 \(s_2+s_3>0\)，落入 DD-sign region；因而

\[
\ell=m_3=1,
\qquad
S=10.
\]

因此所有 \(r\ge3\) 满足

\[
\boxed{
T_{\rm den,10}(v_r)
=(111,10,10,10).
}
\]

但 \(v_r\) 两两不同。

故

\[
\boxed{
\#T^{-1}(111,10,10,10)=\infty.
}
\tag{13.1}
\]

特别地，\(T\) 严格遗忘 canonical numerator/sphere direction information。

这满足 prompt 对 properness 的强要求，而且比只找一对 collision 更强。

## 13.2 Fibre interpretation

固定 \(T\) 后被完全冻结的是：

\[
(b_1,b_2,b_3),
\quad
(m_1,m_2,m_3),
\quad
B,
\quad
\Lambda,
\quad
d_i,
\quad
Q,G,
\quad
S,
\quad
\eta_3,\mathcal L,\tau,
\]

以及 Exact-Lift admissible locus 上的 \(\kappa\) 与 denominator-tail certificate。

仍可变化的是 numerator/sphere data，例如

\[
(x_1,x_2,x_3,t),
\qquad
(a_1,a_2,a_3),
\]

以及由它们产生的 decimal-local / algebraic-local data。

因此 fibre 不是一个人为编码造成的“多个表示”，而是数学上真实存在的 numerator/sphere freedom。

**OPEN.**  
若进一步把 exact decimal balance、全部 algebraic gates 与 final candidate conditions 一并切进 fibre，所得 exact-candidate subfibre 的大小本轮不研究。

---

# 14. Coordinate-deletion stress ledger

本节只证明当前 word normal form 的四个显式分量均有实际作用；不把它冒充成所有可能编码中的 categorical minimality theorem。

| deleted component | surviving trace | actual canonical counterexample? | status |
|---|---|---:|---|
| \(B\) | \((M_2,M_3,S)\) | yes | **DISPROVED** |
| \(M_2\) | \((B,M_3,S)\) | yes | **DISPROVED** |
| \(M_3\) | \((B,M_2,S)\) | yes | **DISPROVED** |
| \(S\) | \((B,M_2,M_3)\) | yes, using \(A_1\) | **DISPROVED uniformly** |

### Delete \(B\)

\[
(a;b)=(1,6,18;1,1,1)
\]

与

\[
(a;b)=(1,4,16;2,1,1)
\]

都是 DD-sign canonical sphere states，且都有

\[
(M_2,M_3,S)=(10,10,10),
\]

但

\[
B=111\neq211.
\]

### Delete \(M_2\)

Section 9.3 的两个 states 有

\[
(B,M_3,S)=(1111,10,10)
\]

但 \(M_2=100\) 与 \(10\)。

### Delete \(M_3\)

Section 9.5 的两个 states 有

\[
(B,M_2,S)=(11111,10,10)
\]

但 \(M_3=10\) 与 \(100\)。

### Delete \(S\)

Section 9.6 的两个 \(A_1\)-sign states 有相同

\[
(B,M_2,M_3)=(11100,10,1000),
\]

但 \(S=1000\) 与 \(100\)。

所以当前 trace 已经过一次真正的“逐分量删除压力测试”。

---

# 15. Relation with the abstract maximal common factor

上一轮 abstract pairwise common factor 可写成由 equivalence relation

\[
E_{\rm abs}
=
\operatorname{EqCl}
\bigl(
\ker\lambda_{\rm den}
\cup
\ker\lambda_{10}
\bigr)
\]

定义的 quotient

\[
\Sigma_{\rm den,10}^{\rm abs}
=\Omega_{\rm rec}^{\rm str}/E_{\rm abs}.
\]

本轮清洗后的 denominator block 满足：

\[
\lambda_{\rm den}=h\circ T,
\]

并且反过来 \(T\) 可从 \(\lambda_{\rm den}\) 唯一读出，因为 denominator state 中含 reduced denominator blocks 与 effective tail request。故

\[
\boxed{
\ker\lambda_{\rm den}=\ker T.
}
\tag{15.1}
\]

另一方面，\(T\) 是 decimal block 的 denominator-facing projection，因此

\[
\boxed{
\ker\lambda_{10}\subseteq\ker T.
}
\tag{15.2}
\]

所以

\[
\operatorname{EqCl}
(\ker\lambda_{\rm den}\cup\ker\lambda_{10})
=
\ker T.
\tag{15.3}
\]

从而：

\[
\boxed{
\Sigma_{\rm den,10}^{\rm abs}
\cong
\operatorname{Im}T_{\rm den,10}.
}
\tag{15.4}
\]

**NEW PROVED under the cleaned semantic blocks.**  
因此本轮 explicit trace 不只是 factor through abstract quotient；它真正实现了该 pairwise maximal common factor。

这也解释了上一轮的 presentation dependence：若把 algebraic certificates 塞入 \(R_{\rm den}\)，则 \(\ker\lambda_{\rm den}\) 被人为缩小，abstract quotient 会错误地显得更接近 injective。把 semantic boundary 修正后，canonical common factor 才显露为 (10.1)/(10.2)。

---

# 16. What is genuinely shared, in one sentence

本轮最终答案可以压成：

\[
\boxed{
\text{denominator recovery 与 decimal recovery 真正必须同步的，}
\text{是同一个完整 reduced denominator word（含切分）}
\text{以及同一个 effective tail scale }10^\ell.
}
\tag{16.1}
\]

第三尾的

\[
\eta_3,\mathcal L,\tau
\]

不是额外共享自由度；\(\Lambda,d_i,Q,G,\kappa\) 也不是；它们全部是该 trace 的 deterministic arithmetic views。

而 numerator/root/algebraic quantities 不属于这个 pairwise common factor。

---

# 17. Consequences for Backward Strict Layer

## 17.1 The old tail tuple is over-parameterized

以后不应再把

\[
(\eta_3,\mathcal L,\tau,\ell,b_3)
\]

当作五个同步变量。对 den–decimal gluing 来说，它们压成 \((b_3,S)\)。

## 17.2 Prefix denominator information is genuinely required

只同步 third tail 不够。因为 \(Q,G,\Lambda,B\) 都依赖前两 denominator blocks，而 exact balance 与 tail certificate 都实际读取这些 prefix views。

因此“denominator–decimal overlap = tail overlap”是错误的。

## 17.3 No numerator information crosses this interface except the projected A1 tail scale

DD 中

\[
S=M_3,
\]

所以 den–decimal interface 完全由 denominator word 决定。

\(A_1\) 中

\[
S=10^{n_3},
\]

因此 numerator-side 只通过一个投影 —— effective tail scale —— 穿过该 interface。完整 \(a_3\)、\(z_3\)、\(n_1,n_2\) 都无需同步到 denominator block。

## 17.4 DD has a smaller chamber-specific interface

在 DD 单独内部，\(S=M_3\)，所以

\[
\boxed{
T_{\rm den,10}^{DD}
=(B,M_2,M_3)
\simeq
(b_1,b_2,b_3).
}
\tag{17.1}
\]

即 DD 的 denominator–decimal interface 没有额外 tail coordinate。

uniform strict interface 多出的 \(S\) 完全是为了兼容 \(A_1\)。

这是一项结构性的 chamber comparison，而不是 forward termination argument。

---

# 18. What this theorem does **not** prove

1. 不证明 strict layer empty；
2. 不证明 DD 或 \(A_1\) empty；
3. 不产生 moving-core height bound；
4. 不证明 square-spacing contradiction；
5. 不证明 \(2/5\)-adic capacity contradiction；
6. 不证明 primitive tail quadratic 的 algebraic part 自动 glues；
7. 不把 \(\mu,\nu,C,D,\mathcal N_{12},z_3\) 消掉；
8. 不证明三块 \(D_{\rm alg}\times D_{\rm den}\times D_{10}\) 已 rectangular；
9. 不证明 exact-candidate fibre 对固定 \(T\) 有限或无限；
10. 不声称当前四分量 word encoding 是所有抽象编码中的唯一 minimal code。

本轮证明的是一个更窄但严格的结果：**denominator recovery 与 decimal completion 之间的 pairwise common factor 已经算术化并 lossless。**

---

# 19. Next theorem only if justified

因为本轮已经得到

\[
J_{\rm den,10}
=
D_{\rm den}
\times_{\mathcal T}
D_{10},
\]

下一轮才有理由加入 algebraic block。

但不应直接做泛泛三块 rectangularity。最自然的下一步是研究：

\[
\boxed{
\textbf{Algebraic–Denominator Interface over fixed }T_{\rm den,10}.
}
\]

即先固定

\[
T=(B,M_2,M_3,S),
\]

从而冻结

\[
\Lambda,d_i,Q,G,\eta_3,\mathcal L,\tau,\kappa,
\]

再问 primitive tail quadratic 中剩下的

\[
(C,D,\mathcal N_{12},z_3,\mu,\nu)
\]

究竟通过什么最小 algebraic datum 与这个固定 denominator skeleton 同步。

这样下一轮不会回到整个 strict layer，也不会与正向 moving-core 路线重复。

---

# 20. Proof / status ledger

## PROVED / existing inputs

- canonical common-denominator reconstruction
  \[
  d_i=\gcd(x_i,\Lambda),\quad
  a_i=x_i/d_i,\quad
  b_i=\Lambda/d_i;
  \]
- canonical normalization
  \[
  \Lambda=\operatorname{lcm}(b_1,b_2,b_3);
  \]
- exact balance
  \[
  \Lambda A=tB;
  \]
- effective tail normalization
  \[
  S=10^\ell,
  \quad
  \eta_3=\gcd(S,b_3),
  \quad
  \mathcal L=S/\eta_3,
  \quad
  \tau=b_3/\eta_3;
  \]
- DD tail weight
  \[
  \kappa=\mathcal LQG/\tau;
  \]
- \(A_1\) tail weight
  \[
  \kappa=10^g\mathcal LQG/\tau;
  \]
- denominator-tail certificate
  \[
  S\mid\kappa^2(\kappa+2G).
  \]

## DERIVED FROM PROVED RESULTS

- strict \(A_1\) effective tail identity
  \[
  \ell=n_3;
  \]
- \((b_3,S)\) uniquely determines \((\eta_3,\mathcal L,\tau)\)；
- \((b_1,b_2,b_3)\) uniquely determines \(\Lambda,d_i,m_i,B,Q,G\)。

## NEW PROVED

1. word/block trace equivalence
   \[
   (B,M_2,M_3,S)
   \simeq
   (b_1,b_2,b_3,S);
   \]
2. branch-free denominator formula
   \[
   \boxed{\kappa=M_3QG/b_3};
   \]
3. denominator-tail certificate is a pure \(T\)-predicate；
4. exact denominator block factorization through \(T\)；
5. decimal denominator-facing factorization through \(T\)；
6. pairwise lossless theorem
   \[
   J_{\rm den,10}=D_{\rm den}\times_{\mathcal T}D_{10};
   \]
7. explicit equivalence with the abstract maximal common factor under cleaned semantic blocks；
8. properness by an infinite fibre
   \[
   v_r=(1,2r,2r^2,1),\ r\ge3;
   \]
9. actual canonical counterexamples to deleting \(B,M_2,M_3,S\) from the current word trace.

## DISPROVED CANDIDATES

- \(T=S\)；
- \(T=(b_3,S)\) as full den–decimal interface；
- \(T=(B,S)\)；
- \(T=(B,M_3,S)\)；
- \(T=(B,M_2,S)\)；
- uniform \(T=(B,M_2,M_3)\) across DD + \(A_1\)。

## OPEN

- exact-candidate fibre size after all algebraic/decimal gates；
- minimal algebraic–denominator interface over fixed \(T\)；
- full three-block rectangularity after adding \(D_{\rm alg}\)；
- any use of the interface toward strict-layer termination（frozen this round）。

---

# 21. Final theorem statement

把本轮结果压成一个可直接继承的 theorem：

> **Denominator–Decimal Explicit Recovery Interface Theorem.**  
> 在 canonical strict recovery state 上，令
> \[
> M_i=10^{m_i},\qquad S=10^\ell,
> \]
> \[
> B=b_1M_2M_3+b_2M_3+b_3,
> \]
> 并定义
> \[
> T_{\rm den,10}=(B,M_2,M_3,S).
> \]
> 则 \(T_{\rm den,10}\) 与 \((b_1,b_2,b_3,S)\) 算术等价。Canonical denominator recovery 的全部数学输出、第三尾 split、denominator prefix quantities、以及 Exact-Lift admissible locus 上的 \(\kappa\) 和 denominator-tail certificate 均唯一 factor through \(T_{\rm den,10}\)。Decimal completion 从 denominator side 读取的全部信息也 factor through 同一 trace。清除误归入 denominator block 的 algebraic/root certificates 后，
> \[
> J_{\rm den,10}
> =
> D_{\rm den}
> \times_{\operatorname{Im}T_{\rm den,10}}
> D_{10}.
> \]
> 此外 \(T_{\rm den,10}\) proper；其 ambient recovery fibre 甚至可以无限。并且在上述 semantic blocks 下，\(\operatorname{Im}T_{\rm den,10}\) 与上一轮 abstract maximal common factor \(\Sigma_{\rm den,10}^{\rm abs}\) canonically equivalent。

因此本轮真正识别出的“最后那一点共享信息”是：

\[
\boxed{
\textbf{same segmented denominator word}
+
\textbf{same effective decimal-tail scale}.
}
\]

除此之外，所有此前看似共享的 denominator-tail quantities 都是 deterministic projections；所有剩余 numerator/root quantities 则属于下一条 algebraic interface，而不是 denominator–decimal interface。
