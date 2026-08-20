# 105-R40 FINAL FAILURE REPORT

```text
STRICT_A1_UNLIFTABILITY_PROVED=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
```

## 1. 本轮证明的全局 theorem

### 1.1 Primitive production root 的新整除定理

沿用 frozen normalization

\[
M_0=u_0AW=g_0a,\qquad P_1=g_0\mu s,\qquad (a,\mu s)=1,
\]

以及

\[
L=a10^{n_2+n_3},\quad
B=\mu\bigl(W+A10^{m_3}\bigr)+a10^{m_2+m_3},
\]

\[
C=\mu M_0\bigl(C_3+10^{n_3}C_2\bigr),\qquad
LP_1=BQ_0-C,
\]

则每一枚 primitive selector-consistent production root 必满足

\[
\boxed{u_0\mid W+A10^{m_3}}. \tag{R40-DIV}
\]

证明：因为 \(u_0\mid P_2,P_3\)，若素数 \(p\mid(u_0,P_1)\)，sphere 迫使 \(p\mid Q_0\)，与 packet primitive 矛盾；故 \((u_0,P_1)=1\)。于是 \((u_0,g_0)=1\)，从 \(g_0a=u_0AW\) 得 \(u_0\mid a\)。又由 \((a,\mu s)=1\) 得 \((u_0,\mu)=1\)。同理，若 \(p\mid(u_0,Q_0)\)，sphere 模 \(p\) 迫使 \(p\mid P_1\)，仍矛盾；故 \((u_0,Q_0)=1\)。最后将 incidence 模 \(u_0\) 化简为

\[
\mu\bigl(W+A10^{m_3}\bigr)Q_0\equiv0\pmod{u_0},
\]

消去两个单位即得 (R40-DIV)。

因此每个固定 exponent cell 中 \(u_0\) 严格有限；结合

\[
1\le U\le10^{n_3}-1,
\]

每个固定 \((n_2,n_3)\) digit cell 都是可穷举的有限问题。

### 1.2 两个完整 digit cell 的 exact extinction

本轮的 exact integer enumeration 使用 actual source boxes、全部合法 \((m_2,m_3,g,k)\)、全部 digit-compatible \((A,W)\)、共同 \(z\)-window、全部 \(g_0\mid u_0AW\)、全部可能 \(\mu\)，并以整数判平方解 incidence+sphere；之后依次检查 selector、primitivity、positivity、\(\Lambda\)-support、denominator window 与 MASTER cutoff。

- \((n_2,n_3)=(2,1)\)：由 source 得 \(1\le U\le9\)，由 (R40-DIV) 得 \(1\le u_0\le99\)。全部情况的 selector survivor 数为 0。
- \((n_2,n_3)=(3,1)\)：由 source 得 \(1\le U\le9\)，由 (R40-DIV) 得 \(1\le u_0\le999\)。全部情况的 production-root survivor 数为 0。

这两个结论覆盖各自整个 cell，不是局部 \(Q_0\)-bounded no-hit。

R39 的全局定理 \(\mathcal A_N<0\) 亦经 authoritative verifier 复核；linear branch 仍全局死亡。

## 2. 被 exact counterexample 击穿的 conjecture

若把 OVERFLOW 的 antecedent 弱化为“actual \(U\)+digit/exponent synchronization+incidence+sphere+selector”，则 OVERFLOW 为假。精确反例为

\[
(n_2,n_3,m_2,m_3,g,k)=(3,2,2,2,0,1),
\]

\[
(u_0,A,W,C_2,C_3,g_0,a,\mu,s,z,q)
=(1,3,2,725,75,6,1,25,1,25,1),
\]

\[
(P_1,P_2,P_3,Q_0)=(150,1450,225,1475).
\]

这里 \(U=1\)，且

\[
C_2=725<10^3,\qquad C_3=75<10^2,
\]

所以两面都不 overflow。精确核验给出

\[
150^2+1450^2+225^2=1475^2=2{,}175{,}625,
\]

\[
LP_1=BQ_0-C=15{,}000{,}000,
\]

并且 \(Az=75,Wz=50,D=H=25\)。

它同时击穿“actual \(U\)+selector+exponent synchronization 自动足以 lift”的弱命题。它不击穿带全部 primitive/support hypotheses 的 full OVERFLOW；full OVERFLOW 在本轮仍未被证明或反证。

## 3. 最深 genuine survivor

actual-source 方向最深的 exact survivor 是上一节的 packet

\[
\boxed{(150,1450,225,1475)}.
\]

它通过 actual \(U=1\)、source digit rooms、exponent synchronization、incidence、sphere、selector、\(D>0\) 与 \(H>0\)。

primitive-production 方向的不可比 maximal survivor 仍是 R39 packet

\[
\boxed{(48,436,75,445)},
\]

它通过 primitivity、selector、shape、\(\mu\)-support 与 exact \(\Lambda\)-recovery，但没有正整数 source \(U\)。本轮没有找到同时超过这两枚 packet 的 candidate。

## 4. 最深 survivor 的 exact first-failure

对 \((150,1450,225,1475)\)，首个失败的 frozen mandatory condition 是 primitivity：

\[
\gcd(150,1450,225,1475)=25\ne1.
\]

它还独立失败于 support：

\[
\lambda=1,\qquad \Lambda=25,\qquad
\gcd(\Lambda,C_2C_3)=25\ne1.
\]

因此它不是 Strict \(A_1\) witness，不能 reconstruction 回原问题。

对 R39 packet，exact first-failure 保持为

\[
I_{23}=\left[\frac{10}{109},\frac25\right),\qquad
I_{23}\cap\mathbf Z_{>0}=\varnothing,
\]

即 \(U_{\rm lo}=1>0=U_{\rm hi}\)。

## 5. 当前问题是否已经被证明 finite

\[
\boxed{\text{NO}.}
\]

(R40-DIV) 只证明每个固定 digit/exponent cell 有限。R26 的 terminal iff 同样只在固定 primitive packet 上给出有限判定。当前没有任何已证明的全局上界限制

\[
n_2,\ n_3
\]

或等价的全局 complexity parameter；因此 Strict \(A_1\) 仍是无限多个有限 cell 的并集。对有限个 cell 的 0-hit 不能推出原问题无解。

## 6. 为什么当前运行仍无法完成原问题

本轮没有得到覆盖所有 digit lengths 的符号矛盾，也没有得到把 \((n_2,n_3)\) 限制在有限集合内的 theorem；同时全部 exact 搜索没有产生 terminal pair。继续扩大任何有限的 \(U,u_0,n_2,n_3,Q_0\) 范围，逻辑上仍只是 bounded no-hit，不能满足不存在性证明的覆盖要求。另一方面，没有 candidate 通过完整 terminal predicate，故也不存在可供原变量 reconstruction 的 witness。

所以两项成功标志均不成立。R40 的最终状态是：Strict \(A_1\) 在本次运行中仍未决定。
