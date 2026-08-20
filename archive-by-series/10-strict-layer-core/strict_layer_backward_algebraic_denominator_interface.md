# 三项十进制拼接平方和问题：Backward Strict Layer — Algebraic–Denominator Residual Interface over fixed \(T_{\rm den,10}\)

**文件名：** `strict_layer_backward_algebraic_denominator_interface.md`  
**研究范围：** Backward Strict Layer；只研究固定 denominator–decimal trace 后的 Algebraic–Denominator residual interface  
**冻结：** 不重新做总体 Backward 抽象；不进入 DD / \(A_1\) 局部分支攻关；不做 moving-core / square-spacing / height / valuation-capacity；不继续 den–decimal 压缩  
**本轮核心结论：** fixed \(T\) 后，\((C,D,\mathcal N_{12},\mathcal C_3,[\mu:\nu],z_3)\) 存在显著 over-parameterization；当前 Exact-Lift 证明库中的 alg–den 共享信息可压到一个 **two-coordinate oriented root trace**
\[
\boxed{
R_T=([\mu:\nu],z_3)
}
\]
并配一个明确的 exact coefficient-plane relation / reconstruction predicate。  
**最强新结构：** gap quadratic 与 primitive-tail quadratic 在 fixed \(T\) 并加入 exact coefficient plane 后不再是两个独立 quadratic gates，而是同一个 scalar identity 的两个比例写法。

---

# 1. Executive summary

本轮从 sufficient proper denominator–decimal trace

\[
\boxed{
T=T_{\rm den,10}
\simeq
(b_1,b_2,b_3,S)
\simeq
(B,M_2,M_3,S)
}
\]

出发，其中

\[
M_i=10^{m_i},
\qquad
S=10^\ell.
\]

固定 \(T\) 后，首先严格冻结：

\[
b_i,\quad m_i,\quad M_i,\quad B,\quad
\Lambda=\operatorname{lcm}(b_i),
\quad d_i=\Lambda/b_i,
\]

\[
Q=b_1M_2+b_2,
\qquad
G=b_1b_2,
\]

以及 tail split

\[
\eta_3=\gcd(S,b_3),
\qquad
\mathcal L=\frac S{\eta_3},
\qquad
\tau=\frac{b_3}{\eta_3}.
\]

此外，已有 strict-layer 统一材料已经证明

\[
\boxed{
\kappa=\frac{M_3QG}{b_3}.
}
\]

**REINTERPRETED EXISTING RESULT.**  
本报告绝不把该公式标为新结果；这里只重新解释其 fixed-\(T\) 后果：\(\kappa\) 是 denominator trace 的确定函数。

本轮第一个真正的新压缩是 coefficient \(D\)。严格层只保留 DD 与 \(A_1\)-only，而两支的既有定义统一给出

\[
\boxed{
D=D_T:=\frac{M_3}{S}\,Q.
}
\tag{1.1}
\]

所以：

\[
\boxed{
D\text{ 在 fixed-}T\text{ fibre 中没有任何 residual freedom。}
}
\]

进一步，结合 \(S=\eta_3\mathcal L\)、\(b_3=\eta_3\tau\) 与已有 \(\kappa\) 公式，得到

\[
\boxed{
\kappa\tau=G\mathcal L D.
}
\tag{1.2}
\]

这条 identity 是后续全部消元的核心。

令

\[
\theta:=\frac{\mu}{\nu}>0,
\qquad
\gcd(\mu,\nu)=1,
\qquad
\zeta:=z_3.
\]

从 exact reconstruction 而不是从两个 quadratic 猜测，可以得到统一 coefficient-plane identity

\[
\boxed{
\mathcal R
=
\frac{\mathcal LC+\zeta}{\mathcal LD+\tau},
\qquad
r_3=\frac{\zeta}{\tau},
\qquad
\theta=G(\mathcal R-r_3).
}
\]

因此

\[
\boxed{
\mathcal F_{\rm ex}
:=
G^2\mathcal LC
-
G\kappa\zeta
-
(G+\kappa)\tau\theta
=0.
}
\tag{1.3}
\]

这不是一个新的 obstruction gate，而是 **exact coefficient-plane reconstruction 的 fixed-\(T\) 正规形**。

再利用 sphere identity

\[
\mathcal N_{12}
=
G^2(r_1^2+r_2^2)
=
G^2(\mathcal R^2-r_3^2),
\]

得到

\[
\boxed{
\mathcal N_{12}
=
\theta^2+\frac{2G}{\tau}\theta\zeta.
}
\tag{1.4}
\]

由 (1.3) 解出

\[
\boxed{
C
=
\frac{
G\kappa\zeta+(G+\kappa)\tau\theta
}{
G^2\mathcal L
}.
}
\tag{1.5}
\]

而

\[
\mathcal C_3
=
G^2\mathcal L^2C^2
-
\mathcal N_{12}(\mathcal LD+\tau)^2
\]

进一步化为

\[
\boxed{
\mathcal C_3
=
\kappa^2\zeta^2
-
2(G+\kappa)\tau\theta\zeta.
}
\tag{1.6}
\]

于是 fixed \(T\) + exact reconstruction 上有严格 deterministic chain：

\[
\boxed{
(\theta,\zeta)
\Longrightarrow
D,\ C,\ \mathcal N_{12},\ \mathcal C_3,\ K_{C,D}.
}
\tag{1.7}
\]

所以原先看起来像五六份共享信息的

\[
(C,D,\mathcal N_{12},\mathcal C_3,[\mu:\nu],z_3)
\]

实际上可以压成

\[
\boxed{
([\mu:\nu],z_3).
}
\]

更强地，gap quadratic

\[
Q_{\rm gap}
=
D(\kappa+2G)\theta^2
-2G\kappa C\theta
+\kappa D\mathcal N_{12}
\]

与 primitive-tail quadratic

\[
Q_{\rm tail}
=
-\kappa(\kappa+2G)\zeta^2
+2G^2\mathcal LC\zeta
+\mathcal C_3
\]

在 fixed \(T\) 且 \(\mathcal F_{\rm ex}=0\) 时满足精确比例

\[
\boxed{
Q_{\rm tail}
=
-
\frac{
\mathcal L\tau(G+\kappa)^2
}{
G\kappa^2
}
Q_{\rm gap}.
}
\tag{1.8}
\]

因此：

\[
\boxed{
\mathcal F_{\rm ex}=0
\Longrightarrow
\bigl(
Q_{\rm gap}=0
\iff
Q_{\rm tail}=0
\bigr).
}
\tag{1.9}
\]

这证明两个 quadratic 在 **exact coefficient plane 上不是两个独立的 residual shared gates**。

但是，如果只要求两个 quadratic 同时成立而丢掉 coefficient-plane orientation，则出现第二个线性因子

\[
\boxed{
\mathcal F_{\rm conj}
=
G^2\kappa\mathcal LC
+
G\kappa(\kappa+2G)\zeta
-
(G+\kappa)(\kappa+2G)\tau\theta
=0.
}
\tag{1.10}
\]

它给出 genuine false gluing。一个完全显式的整数例子是

\[
G=1,\quad
\kappa=110,\quad
\mathcal L=10,\quad
\tau=1,\quad
D=11,
\]

\[
\theta=55,\quad
\zeta=3,\quad
C=588,\quad
\mathcal N_{12}=2800,
\quad
\mathcal C_3=75600.
\]

此时两个 quadratic 都严格为零，但

\[
\mathcal F_{\rm ex}
=
10\cdot588-110\cdot3-111\cdot55
=
-555\ne0.
\]

所以：

\[
\boxed{
\text{“两个 quadratic 都有同一组看似可行的 roots”}
\not\Rightarrow
\text{exact recovery gluing}.
}
\tag{1.11}
\]

这正是本轮要求的 false-gluing pressure test。

最终，本报告提出：

\[
\boxed{
T_{\rm alg\mid den}
=
R_T
=
([\mu:\nu],z_3).
}
\tag{1.12}
\]

它也等价于

\[
\boxed{
R_T\simeq(\mathcal R,r_3),
}
\tag{1.13}
\]

因为 fixed \(T\) 后

\[
r_3=\frac{z_3}{\tau},
\qquad
\mathcal R=\frac{\mu/\nu}{G}+\frac{z_3}{\tau}.
\]

因此 gap root 与 tail root 不应被解释为“两个独立 global branches”；它们是同一完整 candidate 的两个 typed projections，等价于“总 norm + 第三分量”。

但本轮也得到一个明确的负结果：

\[
\boxed{
[\mu:\nu]\text{ 单独不能 deterministic-recover }z_3,
}
\]

\[
\boxed{
z_3\text{ 单独也不能 deterministic-recover }[\mu:\nu]
}
\]

在 fixed-\(T\) ambient recovery fibre 上都有严格 collision 反例。因此当前自然语义坐标下 deterministic elimination 停在一个 two-coordinate trace，而不是 one-root trace。

本轮不声称这是所有可能编码中的 categorical minimality theorem；那仍为 **OPEN**。

---

# 2. Corrections to previous ledger

## 2.1 \(\kappa=M_3QG/b_3\) 的状态修正

上一轮 denominator–decimal 报告把

\[
\kappa=\frac{M_3QG}{b_3}
\]

放在“新压缩”语境中，容易造成它是本轮首次证明的印象。

本轮明确修正为：

\[
\boxed{
\kappa=\frac{M_3QG}{b_3}
\quad
\textbf{是 EXISTING PROVED RESULT}.
}
\]

本轮唯一新增的是：

> 在 fixed \(T_{\rm den,10}\) fibre 中，把它重新解释为 denominator-determined constant。

**状态：REINTERPRETED EXISTING RESULT。**

---

## 2.2 \(T_{\rm den,10}\) 的地位修正

本轮只使用

\[
\boxed{
T_{\rm den,10}
\simeq
(b_1,b_2,b_3,S)
\simeq
(B,M_2,M_3,S)
}
\]

作为：

\[
\boxed{
\text{sufficient proper denominator–decimal trace}.
}
\]

不再称其为整个 Exact-Lift 的“唯一 intrinsic maximal common factor”。

上一轮 pairwise lossless theorem 也只解释为：

\[
\boxed{
\text{cleaned denominator semantic block}
\;\times_T\;
\text{cleaned decimal semantic block}
}
\]

的 lossless pullback。

本轮完全冻结这一边，不继续研究它是否还能压缩。

---

## 2.3 Source-audit limitation

本轮实际回查了：

- `strict_layer_backward_denominator_decimal_interface.md`；
- `strict_layer_backward_canonical_synchronization_quotient.md`；
- `strict_layer_backward_canonical_dependency_skeleton.md`；
- `strict_layer_backward_global_witness_gluing_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`；
- `strict_layer_unified_exact_lift_campaign.md` 及其当前可见重复版本；
- 当前正向 strict-layer 统一 / moving-core 报告中 \((C,D)\)、\(\kappa\)、gap/tail quadratic 的原始推导接口；
- DD source audit 仅用于核对“actual root 是 candidate 的 deterministic projection”这一语义，不进入 DD 攻关。

当前 File Library 检索没有重新暴露名为 `strict_layer_final_campaign.md` 的正文；后续 Backward 报告对其 N4–N5 有明确引用，但本轮不把那些二手引用用于新增 algebraic elimination theorem。因此本轮新增定理不依赖该文件不可见部分。

---

# 3. Fixed \(T_{\rm den,10}\) data

定义

\[
\Omega_T
=
\left\{
v\in\Omega_{\rm rec}^{\rm str}:
T(v)=T
\right\}.
\]

这里 fixed \(T\) 采用 block form

\[
T=(b_1,b_2,b_3,S),
\]

或等价 word form

\[
T=(B,M_2,M_3,S).
\]

## 3.1 直接冻结

由 \(T\) 唯一恢复：

\[
\boxed{
b_1,b_2,b_3,
\quad
m_1,m_2,m_3,
\quad
M_1,M_2,M_3,
}
\]

\[
\boxed{
B,
\quad
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\quad
d_i=\Lambda/b_i,
}
\]

\[
\boxed{
Q=b_1M_2+b_2,
\qquad
G=b_1b_2.
}
\]

**状态：PROVED / inherited from denominator–decimal interface。**

---

## 3.2 Tail normalization 冻结

\[
\boxed{
\eta_3=\gcd(S,b_3),
\quad
\mathcal L=S/\eta_3,
\quad
\tau=b_3/\eta_3.
}
\]

因此：

\[
\boxed{
S=\eta_3\mathcal L,
\qquad
b_3=\eta_3\tau,
\qquad
\gcd(\mathcal L,\tau)=1.
}
\]

**状态：DERIVED FROM PROVED RESULTS。**

---

## 3.3 \(\kappa\) 冻结

已有：

\[
\boxed{
\kappa=\frac{M_3QG}{b_3}.
}
\]

所以 fixed \(T\) 后 \(\kappa\) 为常量。

**状态：REINTERPRETED EXISTING RESULT。**

---

## 3.4 新的 \(D\)-freezing theorem

严格层当前只含 DD 与 \(A_1\)-only。

已有 coefficient definitions：

\[
DD:
\qquad
D=Q,
\qquad
\ell=m_3,
\]

\[
A_1:
\qquad
D=10^gQ,
\qquad
\ell=m_3-g.
\]

因为

\[
S=10^\ell,
\qquad
M_3=10^{m_3},
\]

两支都满足

\[
\boxed{
D
=
\frac{M_3}{S}Q.
}
\tag{3.1}
\]

于是定义

\[
\chi_T:=\frac{M_3}{S},
\]

则

\[
\boxed{
D=\chi_TQ.
}
\]

### NEW PROVED — Fixed-Trace \(D\)-Freezing Lemma

在整个 strict DD/\(A_1\) scope 上：

\[
\boxed{
T
\Longrightarrow
D.
}
\]

因此 \(D\) 不应进入 residual algebraic interface。

---

## 3.5 新的 tail–coefficient identity

由

\[
\kappa=\frac{M_3QG}{b_3},
\qquad
D=\frac{M_3Q}{S},
\]

以及

\[
S=\eta_3\mathcal L,
\qquad
b_3=\eta_3\tau,
\]

有

\[
\kappa\tau
=
\frac{M_3QG}{\eta_3\tau}\tau
=
\frac{M_3QG}{\eta_3},
\]

而

\[
G\mathcal LD
=
G\frac{S}{\eta_3}\frac{M_3Q}{S}
=
\frac{M_3QG}{\eta_3}.
\]

故

\[
\boxed{
\kappa\tau=G\mathcal LD.
}
\tag{3.2}
\]

**状态：NEW PROVED。**

这是 fixed-\(T\) 后 algebraic elimination 的核心 coefficient identity。

---

# 4. Remaining algebraic variable inventory

令

\[
\theta:=\frac{\mu}{\nu},
\qquad
\zeta:=z_3.
\]

下面的“branching”只指 projected search branching，不指原始 candidate 新增自由度。

| quantity \(q\) | fixed \(T\) 决定？ | 由其他 algebraic data 决定？ | projected branching? | 真正 alg–den shared? |
|---|---:|---:|---:|---:|
| \(D\) | **是** | — | 否 | **否：已吸收入 \(T\)** |
| \(C\) | 否 | **是，由 \((\theta,\zeta)\)+exact plane** | 否 | 可消元 |
| \(\mathcal N_{12}\) | 否 | **是，由 \((\theta,\zeta)\)** | 否 | 可消元 |
| \(\mathcal C_3\) | 否 | **是，由 \((\theta,\zeta)\)** | 否 | 可消元 |
| \(K_{C,D}\) | 否 | 由 \(C,D,\mathcal N_{12}\) | 否 | certificate summary，非坐标 |
| \(W\) | 否 | 判别平方 certificate | \(\pm\) symmetry | 否 |
| \([\mu:\nu]\) | 否 | 完整 candidate 决定 | quadratic search 可有两根 | **是** |
| \(z_3\) | 否 | 完整 candidate 决定 | quadratic search 可有两根 | **是** |
| \(a_3\) | 否 | fixed \(\eta_3\) 后由 \(z_3\) reduced form 决定 | 否 | \(z_3\) 的 denominator-side view |
| \(G_0\) | 否 | 由 root/coefficient data gcd 决定 | 否 | 可消元 |
| \(\mathcal R\) | 否 | \(\theta/G+\zeta/\tau\) | 否 | 与 root pair 等价 |
| \(r_3\) | 否 | \(\zeta/\tau\) | 否 | 与 root pair 等价 |

核心审计结论：

\[
\boxed{
\text{fixed }T\text{ 后，真正需要继续研究的自然 residual coordinates 只有 }
(\theta,\zeta).
}
\]

但这还没有证明“二者相互独立”；下一节开始严格消元。

---

# 5. Dependency graph over fixed \(T\)

当前 proof library 在 fixed \(T\) 后可压成：

\[
\boxed{
T
\longrightarrow
(G,Q,D,\kappa,\eta_3,\mathcal L,\tau)
}
\]

以及

\[
\boxed{
(\theta,\zeta)
\longrightarrow
(\mathcal R,r_3)
}
\]

其中

\[
r_3=\frac{\zeta}{\tau},
\qquad
\mathcal R=\frac{\theta}{G}+\frac{\zeta}{\tau}.
\]

sphere identity 给出

\[
\boxed{
(\theta,\zeta)
\longrightarrow
\mathcal N_{12}.
}
\]

exact coefficient plane 给出

\[
\boxed{
(T,\theta,\zeta)
\longrightarrow
C.
}
\]

然后：

\[
\boxed{
(T,\theta,\zeta)
\longrightarrow
\mathcal C_3,\ K_{C,D},\ G_0,\ldots
}
\]

因此更准确的 dependency DAG 是

\[
\boxed{
\begin{array}{ccc}
&T&\\
&\downarrow&\\
G,Q,D,\kappa,\eta_3,\mathcal L,\tau
&\qquad&
(\theta,\zeta)\\
&\searrow\quad\swarrow&\\
C,\mathcal N_{12},\mathcal C_3,K_{C,D},\ldots\\
&\downarrow&\\
\text{quadratic / divisibility / discriminant certificates}
\end{array}
}
\]

而不是

\[
(C,D,\mathcal N_{12},[\mu:\nu],z_3)
\]

五个平行 independent vertices。

---

# 6. Elimination of \((C,D,\mathcal N_{12})\) redundancy

## 6.1 第一层：\(D\) 完全消失

由 (3.1)：

\[
D=D_T.
\]

所以立即有

\[
\boxed{
(C,D,\mathcal N_{12})
\longrightarrow
(C,\mathcal N_{12})
}
\]

在 fixed \(T\) fibre 上 lossless。

因此：

\[
\boxed{
\dim_{\rm info}(C,D,\mathcal N_{12})\le2.
}
\]

这里的 dimension 只表示自然独立算术信息数量。

---

## 6.2 但 \(C\) 与 \(\mathcal N_{12}\) 不能彼此 deterministic-eliminate

这一步不能只靠“公式看起来不同”判断；直接构造 fixed-\(T\) collisions。

取

\[
b_1=b_2=b_3=1,
\qquad
T=(111,10,10,10).
\]

### Same \(\mathcal N_{12}\), different \(C\)

两组 integer-sphere states：

\[
(1,6,18;19),
\qquad
(6,1,18;19).
\]

都有

\[
1^2+6^2+18^2=19^2,
\]

且同属 DD-sign region。

因为 \(b_1=b_2=1\)，

\[
\mathcal N_{12}=a_1^2+a_2^2=37
\]

两者相同。

但

\[
A_{12}=16,\ 61,
\]

而 \(d_3=1\)，所以

\[
C=160,\ 610.
\]

因此：

\[
\boxed{
T+\mathcal N_{12}
\not\Longrightarrow
C.
}
\tag{6.1}
\]

**状态：NEW PROVED。**

---

### Same \(C\), different \(\mathcal N_{12}\)

取

\[
(1,12,12;17),
\qquad
(11,2,10;15).
\]

因为

\[
1^2+12^2+12^2=17^2,
\]

\[
11^2+2^2+10^2=15^2.
\]

第一组：

\[
A_{12}=1\cdot100+12=112,
\qquad
\mathcal N_{12}=145.
\]

第二组：

\[
A_{12}=11\cdot10+2=112,
\qquad
\mathcal N_{12}=125.
\]

两组均 \(d_3=1\)，故

\[
C=1120
\]

相同，而 \(\mathcal N_{12}\) 不同。

所以：

\[
\boxed{
T+C
\not\Longrightarrow
\mathcal N_{12}.
}
\tag{6.2}
\]

**状态：NEW PROVED。**

因此如果不引入更底层 root geometry，\((C,\mathcal N_{12})\) 的两个自然信息通道都是真实的。

---

## 6.3 Sphere geometry 消掉 \(\mathcal N_{12}\)

由定义

\[
\mathcal N_{12}
=
(a_1b_2)^2+(a_2b_1)^2.
\]

因为

\[
G=b_1b_2,
\]

有

\[
\mathcal N_{12}
=
G^2(r_1^2+r_2^2).
\]

而

\[
r_1^2+r_2^2
=
\mathcal R^2-r_3^2.
\]

定义

\[
\theta
=
G(\mathcal R-r_3),
\qquad
r_3=\frac{\zeta}{\tau}.
\]

于是

\[
\mathcal R
=
\frac{\theta}{G}+\frac{\zeta}{\tau}.
\]

代入：

\[
\begin{aligned}
\mathcal N_{12}
&=
G^2\left[
\left(
\frac{\theta}{G}+\frac{\zeta}{\tau}
\right)^2
-
\left(
\frac{\zeta}{\tau}
\right)^2
\right]\\
&=
\theta^2+\frac{2G}{\tau}\theta\zeta.
\end{aligned}
\]

故：

\[
\boxed{
\mathcal N_{12}
=
N_T(\theta,\zeta)
:=
\theta^2+\frac{2G}{\tau}\theta\zeta.
}
\tag{6.3}
\]

**状态：NEW PROVED。**

---

## 6.4 Exact coefficient plane 消掉 \(C\)

严格层两种 chamber 都满足统一 concatenation normal form：

\[
\boxed{
A=SC+a_3,
\qquad
B=SD+b_3.
}
\tag{6.4}
\]

证明只是把既有 DD/\(A_1\) coefficient definitions 代回真实 concatenation：

- DD：\(S=M_3\)，\(C=10^{d_3}A_{12}\)，于是
  \[
  A=A_{12}10^{n_3}+a_3
  =M_3C+a_3=SC+a_3.
  \]
- \(A_1\)：\(S=10^{n_3}\)，\(C=A_{12}\)，而 \(D=10^gQ\)，\(M_3=10^gS\)，同样得到 (6.4)。

再除去 \(\eta_3\)：

\[
a_3=\eta_3\zeta,
\qquad
b_3=\eta_3\tau,
\qquad
S=\eta_3\mathcal L.
\]

所以 exact ratio 为

\[
\boxed{
\mathcal R
=
\frac{
\mathcal LC+\zeta
}{
\mathcal LD+\tau
}.
}
\tag{6.5}
\]

同时

\[
r_3=\frac{\zeta}{\tau}.
\]

于是

\[
\frac{\theta}{G}
=
\mathcal R-r_3
=
\frac{
\mathcal L(\tau C-D\zeta)
}{
\tau(\mathcal LD+\tau)
}.
\]

得到

\[
G\mathcal L(\tau C-D\zeta)
=
\tau(\mathcal LD+\tau)\theta.
\tag{6.6}
\]

再用

\[
G\mathcal LD=\kappa\tau
\]

化简为

\[
\boxed{
G^2\mathcal LC
-
G\kappa\zeta
-
(G+\kappa)\tau\theta
=
0.
}
\tag{6.7}
\]

因此

\[
\boxed{
C
=
C_T(\theta,\zeta)
=
\frac{
G\kappa\zeta+(G+\kappa)\tau\theta
}{
G^2\mathcal L
}.
}
\tag{6.8}
\]

**状态：NEW PROVED。**

---

## 6.5 最终 reduction chain

于是：

\[
(C,D,\mathcal N_{12})
\]

在 fixed \(T\) + exact reconstruction 上严格压成：

\[
\boxed{
(C,D,\mathcal N_{12})
\longrightarrow
(\theta,\zeta).
}
\]

更精确：

\[
\boxed{
D=D_T,
\quad
C=C_T(\theta,\zeta),
\quad
\mathcal N_{12}=N_T(\theta,\zeta).
}
\tag{6.9}
\]

所以不能再把 \((C,D,\mathcal N_{12})\) 当三个 residual invariants。

---

# 7. Gap-root vs tail-root audit

## 7.1 两者不是“同一个 root”

定义：

\[
\theta=\frac{\mu}{\nu}
=
G(\mathcal R-r_3),
\]

\[
\zeta=z_3=\frac{a_3}{\eta_3}.
\]

fixed \(T\) 后：

\[
r_3=\frac{\zeta}{\tau},
\]

所以

\[
\mathcal R
=
\frac{\theta}{G}+\frac{\zeta}{\tau}.
\]

因此：

\[
\boxed{
(\theta,\zeta)
\longleftrightarrow
(\mathcal R,r_3)
}
\tag{7.1}
\]

是双向 deterministic change of coordinates。

这说明两类 root 的正确解释不是：

\[
\text{two independent global root choices},
\]

而是：

\[
\boxed{
\text{same candidate 的两个 typed projections：}
\text{overall norm direction + third component}.
}
\]

---

## 7.2 Gap root alone 不足

仍取

\[
T=(111,10,10,10).
\]

两组 sphere states：

\[
(1,6,18;19),
\qquad
(1,8,32;33).
\]

都有

\[
\theta
=
\mathcal R-r_3
=
1.
\]

但

\[
\zeta=18,\ 32.
\]

所以

\[
\boxed{
T+\theta
\not\Longrightarrow
\zeta.
}
\tag{7.2}
\]

**状态：NEW PROVED。**

---

## 7.3 Tail root alone 不足

取

\[
(3,4,12;13),
\qquad
(4,6,12;14).
\]

都有

\[
\zeta=12.
\]

但

\[
\theta=13-12=1,
\qquad
\theta'=14-12=2.
\]

所以

\[
\boxed{
T+\zeta
\not\Longrightarrow
\theta.
}
\tag{7.3}
\]

**状态：NEW PROVED。**

---

## 7.4 对“one algebraic branch”理想的裁决

因此在当前自然 recovery coordinates 上：

\[
\boxed{
\text{fixed }T
\text{ 后不能把 residual trace deterministic 压成}
\theta\text{ alone}
}
\]

也不能压成

\[
\zeta\text{ alone}.
\]

这否定的是“one of the two natural root coordinates determines the other”。

它**没有**证明不存在某种人为 Cantor pairing / exotic scalar encoding，因此不能写成绝对 categorical “information dimension \(\ge2\)” theorem。

正确状态：

\[
\boxed{
\textbf{DISPROVED CANDIDATE: one-root deterministic reduction;}
}
\]

\[
\boxed{
\textbf{OPEN: categorical minimal encoding dimension.}
}
\]

---

# 8. Primitive-tail quadratic normalization

已有：

\[
Q_{\rm tail}
=
-\kappa(\kappa+2G)\zeta^2
+
2G^2\mathcal LC\zeta
+
\mathcal C_3.
\]

以及

\[
\mathcal C_3
=
G^2\mathcal L^2C^2
-
\mathcal N_{12}(\mathcal LD+\tau)^2.
\]

fixed \(T\) 后 \(G,\kappa,\mathcal L,D,\tau\) 都冻结。

把 (6.3)、(6.8) 代入：

\[
\boxed{
\mathcal C_3
=
\kappa^2\zeta^2
-
2(G+\kappa)\tau\theta\zeta.
}
\tag{8.1}
\]

所以 primitive-tail polynomial coefficients 全部是

\[
\boxed{
A_T=-\kappa(\kappa+2G),
}
\]

\[
\boxed{
B_T(\theta,\zeta)
=
2G^2\mathcal L\,C_T(\theta,\zeta),
}
\]

\[
\boxed{
C_T^{\rm tail}(\theta,\zeta)
=
\kappa^2\zeta^2
-
2(G+\kappa)\tau\theta\zeta.
}
\]

这严格回答了 prompt 的问题：

\[
\boxed{
\mathcal C_3
\text{ 不是新的 residual invariant。}
}
\]

它由 fixed \(T\) 与 root pair 唯一确定。

---

# 9. Candidate residual interfaces

本轮依次压力测试以下候选。

## Candidate A — full coefficient/root tuple

\[
R_A
=
(C,D,\mathcal N_{12},[\mu:\nu],z_3).
\]

**裁决：DISPROVED CANDIDATE（over-parameterized）。**

因为：

\[
D=D_T,
\]

\[
C=C_T(\theta,\zeta),
\]

\[
\mathcal N_{12}=N_T(\theta,\zeta).
\]

故它严格冗余。

---

## Candidate B — coefficient pair

\[
R_B=(C,\mathcal N_{12}).
\]

优点：能写两个 quadratic coefficients。

缺点：

1. fixed-\(T\) fibre 中 \(C,\mathcal N_{12}\) 彼此不决定；
2. root existence 仍要额外选择 compatible actual roots；
3. 两个 quadratic 同时可解并不保证 exact coefficient-plane orientation。

**裁决：DISPROVED CANDIDATE as sufficient residual interface。**

---

## Candidate C — discriminant / square data

例如

\[
R_C=(K_{C,D},W)
\]

或只保留 discriminant square class。

**裁决：DISPROVED CANDIDATE。**

理由：

- \(W\leftrightarrow-W\) 常为 certificate symmetry；
- discriminant-square 只回答“存在某个 rational root”；
- denominator reconstruction 读取的是同一个 reduced root 的 numerator/denominator；
- 它不能保证 gap root 与 tail root 来自同一个 exact coefficient plane。

因此 square certificate 不是 shared coordinate。

---

## Candidate D — gap root only

\[
R_D=[\mu:\nu].
\]

由 (7.2) collision：

\[
T+\theta
\not\Longrightarrow
z_3.
\]

**裁决：DISPROVED CANDIDATE。**

---

## Candidate E — tail root only

\[
R_E=z_3.
\]

由 (7.3) collision：

\[
T+z_3
\not\Longrightarrow
[\mu:\nu].
\]

**裁决：DISPROVED CANDIDATE。**

---

## Candidate F — oriented root pair

\[
\boxed{
R_F
=
R_T
=
([\mu:\nu],z_3).
}
\]

它具有以下性质：

1. \(D\) 已由 \(T\) 决定；
2. \(\mathcal N_{12}\) 由 root pair 决定；
3. \(C\) 由 exact plane + root pair 决定；
4. \(\mathcal C_3\)、\(K_{C,D}\) 继续 deterministic；
5. denominator-side reduced-root divisibility 只需读取 root pair 的 reduced integer representatives；
6. discriminant/root-existence certificates不再增加 coordinate；
7. root pair 与 \((\mathcal R,r_3)\) 等价，具有明确 candidate semantics。

**裁决：SURVIVING CANDIDATE / 本轮最终 interface。**

---

# 10. Disproved candidates / false gluings

## 10.1 两个 quadratic 并不足以同步 roots

定义

\[
Q_{\rm gap}
=
D(\kappa+2G)\theta^2
-
2G\kappa C\theta
+
\kappa D\mathcal N_{12},
\]

\[
Q_{\rm tail}
=
-\kappa(\kappa+2G)\zeta^2
+
2G^2\mathcal LC\zeta
+
G^2\mathcal L^2C^2
-
\mathcal N_{12}(\mathcal LD+\tau)^2.
\]

利用 fixed-\(T\) identity

\[
\kappa\tau=G\mathcal LD,
\]

从 \(Q_{\rm gap}=0\) 消去 \(\mathcal N_{12}\)，得到精确分解：

\[
\boxed{
Q_{\rm tail}\big|_{Q_{\rm gap}=0}
=
\frac{
\mathcal F_{\rm ex}\mathcal F_{\rm conj}
}{
G^2\kappa
},
}
\tag{10.1}
\]

其中

\[
\boxed{
\mathcal F_{\rm ex}
=
G^2\mathcal LC
-
G\kappa\zeta
-
(G+\kappa)\tau\theta,
}
\]

\[
\boxed{
\mathcal F_{\rm conj}
=
G^2\kappa\mathcal LC
+
G\kappa(\kappa+2G)\zeta
-
(G+\kappa)(\kappa+2G)\tau\theta.
}
\]

**状态：NEW PROVED。**

所以 simultaneous quadratics 只推出：

\[
\boxed{
\mathcal F_{\rm ex}=0
\quad\text{or}\quad
\mathcal F_{\rm conj}=0.
}
\]

actual exact reconstruction 只允许第一支。

---

## 10.2 Explicit false gluing

取

\[
b_1=b_2=b_3=1,
\qquad
M_2=M_3=10,
\qquad
S=10.
\]

于是

\[
Q=11,\quad
G=1,\quad
D=11,\quad
\mathcal L=10,\quad
\tau=1,
\]

\[
\kappa=\frac{10\cdot11\cdot1}{1}=110.
\]

再取

\[
\theta=55,
\qquad
\zeta=3,
\qquad
C=588,
\qquad
\mathcal N_{12}=2800.
\]

定义

\[
\mathcal C_3
=
G^2\mathcal L^2C^2
-
\mathcal N_{12}(\mathcal LD+\tau)^2
=
75600.
\]

直接计算：

\[
11\cdot112\cdot55^2
-
2\cdot110\cdot588\cdot55
+
110\cdot11\cdot2800
=
0.
\]

以及

\[
-110\cdot112\cdot3^2
+
2\cdot10\cdot588\cdot3
+
75600
=
0.
\]

所以：

\[
Q_{\rm gap}=Q_{\rm tail}=0.
\]

而

\[
\mathcal F_{\rm ex}
=
10\cdot588
-
110\cdot3
-
111\cdot55
=
-555
\ne0.
\]

同时

\[
\mathcal F_{\rm conj}=0.
\]

因此这是一个严格的 algebraic false positive：

\[
\boxed{
\text{same fixed }T
+
\text{both quadratics}
\not\Rightarrow
\text{same exact recovery state}.
}
\]

**状态：NEW PROVED false-gluing counterexample。**

这也说明：

\[
\boxed{
\text{真正需要同步的是 oriented coefficient plane，}
}
\]

而不是仅仅“两个 quadratic 各自有根”。

---

# 11. Final \(T_{\rm alg\mid den}\) and residual relation

本轮最终定义：

\[
\boxed{
T_{\rm alg\mid den}
=
R_T
:
\Omega_T
\to
\mathcal T_{\rm alg\mid den},
}
\]

\[
\boxed{
R_T(v)
=
([\mu:\nu](v),z_3(v)).
}
\tag{11.1}
\]

由于 \(\eta_3\) fixed，\(z_3=a_3/\eta_3\) 为 reduced rational，因此也可以写成：

\[
\boxed{
R_T\simeq([\mu:\nu],a_3).
}
\tag{11.2}
\]

又因为

\[
r_3=\frac{z_3}{\tau},
\qquad
\mathcal R=\frac{\mu/\nu}{G}+\frac{z_3}{\tau},
\]

有：

\[
\boxed{
R_T\simeq(\mathcal R,r_3).
}
\tag{11.3}
\]

---

## 11.1 Explicit reconstruction map

令

\[
\theta=\mu/\nu,
\qquad
\zeta=z_3.
\]

则：

\[
\boxed{
D_T=\frac{M_3}{S}Q,
}
\]

\[
\boxed{
N_T(\theta,\zeta)
=
\theta^2+\frac{2G}{\tau}\theta\zeta,
}
\]

\[
\boxed{
C_T(\theta,\zeta)
=
\frac{
G\kappa\zeta+(G+\kappa)\tau\theta
}{
G^2\mathcal L
},
}
\]

\[
\boxed{
\mathcal C_{3,T}(\theta,\zeta)
=
\kappa^2\zeta^2
-
2(G+\kappa)\tau\theta\zeta.
}
\]

再定义

\[
\boxed{
K_T(\theta,\zeta)
=
G^2C_T(\theta,\zeta)^2
-
D_T^2N_T(\theta,\zeta).
}
\]

于是所有主要 algebraic coefficient summaries 都 factor through \(R_T\)。

---

## 11.2 Residual admissibility predicate

不能把“任意 rational pair \((\theta,\zeta)\)”直接称为 valid shared state。

定义：

\[
\mathfrak A_T(\theta,\zeta)
\]

要求至少：

1. \(\theta>0\)，并取 reduced form
   \[
   \theta=\mu/\nu,\quad\gcd(\mu,\nu)=1;
   \]

2. \(\zeta>0\) 与 fixed tail denominator normalization compatible；在 actual recovery 中
   \[
   \zeta=a_3/\eta_3,\quad\gcd(a_3,\eta_3)=1;
   \]

3. reconstructed
   \[
   C_T,\ N_T,\ \mathcal C_{3,T}
   \]
   满足对应整数性 / 正性 / block-realization requirements；

4. denominator-side reduced-root projections满足既有 rational-root divisibility：
   \[
   \boxed{
   \nu\mid D_T(\kappa+2G),
   }
   \]
   \[
   \boxed{
   \mu\mid\kappa D_TN_T,
   }
   \]
   \[
   \boxed{
   a_3\mid\mathcal C_{3,T}.
   }
   \]

5. T-only tail requirement
   \[
   \eta_3\mid\kappa(\kappa+2G)
   \]
   已在 fibre 外部预先检查，不再算 residual coordinate。

这样：

\[
\boxed{
\text{shared information}
=
R_T,
\qquad
\text{shared compatibility}
=
\mathfrak A_T(R_T).
}
\tag{11.4}
\]

这符合本轮要求的形式：

\[
\boxed{
\text{same residual trace}
+
\text{one explicit residual relation/predicate}.
}
\]

---

# 12. Properness status

必须证明 \(R_T\) 不是 canonical state 的重新编码。

仍取

\[
T=(111,10,10,10).
\]

考虑

\[
v=(1,6,18;19),
\]

\[
v'=(6,1,18;19).
\]

二者是不同的 canonical sphere states：

\[
v\ne v'.
\]

但：

\[
T(v)=T(v'),
\]

\[
\theta(v)
=
19-18
=
1
=
\theta(v'),
\]

\[
z_3(v)=18=z_3(v').
\]

所以

\[
\boxed{
R_T(v)=R_T(v').
}
\]

但 prefix-local information 不同，例如：

\[
C(v)=160,
\qquad
C(v')=610.
\]

因此：

\[
\boxed{
(T,R_T)
\text{ 严格遗忘某些 purely local prefix information。}
}
\tag{12.1}
\]

**状态：NEW PROVED — ambient fixed-\(T\) properness。**

### 边界

这里的 \(v,v'\) 位于 fixed-\(T\) canonical recovery fibre / strict-sign sphere ambient space；本轮没有证明它们都是完整 exact original candidates。

因此得到的是：

\[
\boxed{
\text{properness on }\Omega_T,
}
\]

不是：

\[
\boxed{
\text{properness on the exact-candidate subfibre}.
}
\]

后者仍为 **OPEN**，且本轮没有必要强行证明。

---

# 13. Fixed-Trace Algebraic–Denominator Interface Theorem

## Theorem ADRI-1 — coefficient compression

**NEW PROVED.**

固定一个 strict denominator–decimal trace \(T\)。在 DD/\(A_1\) exact-reconstruction locus 上，令

\[
\theta=\mu/\nu,
\qquad
\zeta=z_3.
\]

则：

\[
\boxed{
D
=
\frac{M_3}{S}Q,
}
\]

\[
\boxed{
\mathcal N_{12}
=
\theta^2+\frac{2G}{\tau}\theta\zeta,
}
\]

\[
\boxed{
C
=
\frac{
G\kappa\zeta+(G+\kappa)\tau\theta
}{
G^2\mathcal L
},
}
\]

\[
\boxed{
\mathcal C_3
=
\kappa^2\zeta^2
-
2(G+\kappa)\tau\theta\zeta.
}
\]

所以：

\[
\boxed{
(C,D,\mathcal N_{12},\mathcal C_3)
\text{ 不增加 }R_T=([\mu:\nu],z_3)
\text{ 之外的 residual shared information。}
}
\]

---

## Theorem ADRI-2 — quadratic collapse on the exact plane

**NEW PROVED.**

在 fixed \(T\) 下令

\[
\mathcal F_{\rm ex}
=
G^2\mathcal LC-G\kappa\zeta-(G+\kappa)\tau\theta.
\]

若

\[
\mathcal F_{\rm ex}=0,
\]

则

\[
\boxed{
Q_{\rm tail}
=
-
\frac{
\mathcal L\tau(G+\kappa)^2
}{
G\kappa^2
}
Q_{\rm gap}.
}
\]

因此：

\[
\boxed{
Q_{\rm gap}=0
\iff
Q_{\rm tail}=0.
}
\]

也就是说：

\[
\boxed{
\text{真正需要同步的是 coefficient-plane orientation，}
}
\]

而不是两个 independent quadratic-root gates。

---

## Theorem ADRI-3 — false-gluing dichotomy

**NEW PROVED.**

若 fixed-\(T\) identity \(\kappa\tau=G\mathcal LD\) 成立，并且

\[
Q_{\rm gap}=Q_{\rm tail}=0,
\]

则消元后必须满足

\[
\boxed{
\mathcal F_{\rm ex}\mathcal F_{\rm conj}=0.
}
\]

其中 \(\mathcal F_{\rm conj}\) 如 (1.10)。

而 explicit example 证明：

\[
\mathcal F_{\rm conj}=0,\quad
\mathcal F_{\rm ex}\ne0
\]

可以发生。

因此：

\[
\boxed{
\text{quadratic compatibility}
\text{ strictly weaker than }
\text{exact recovery compatibility}.
}
\]

---

## Theorem ADRI-4 — audited residual interface

**NEW PROVED relative to the currently audited Exact-Lift alg–den relation family.**

对 fixed \(T\)，当前 proof library 中涉及

\[
D,C,\mathcal N_{12},\mathcal C_3,
K_{C,D},
[\mu:\nu],
z_3
\]

的 alg–den cross-data 全部可 factor through

\[
\boxed{
R_T=([\mu:\nu],z_3)
}
\]

与显式 predicate

\[
\boxed{
\mathfrak A_T(R_T).
}
\]

更准确地：

\[
\boxed{
\text{audited alg–den cross compatibility}
\iff
\mathfrak A_T(\theta,\zeta)
}
\]

这里的“audited”只覆盖当前已回查的：

- exact coefficient-plane reconstruction；
- gap/tail quadratic；
- rational-root divisibility；
- denominator-tail normalization；
- discriminant / coefficient summaries；
- primitive gcd data 的 deterministic projection。

它**不是**：

\[
\boxed{
\operatorname{Liftable(original problem)}
\iff
\mathfrak A_T(\theta,\zeta).
}
\]

full liftability 仍需要 local prefix realization、完整 canonical recovery、decimal balance 的其余 local data 等。

因此本轮没有越界成三块 global gluing theorem。

---

# 14. What remains genuinely local

fixed \(T\) 与 \(R_T\) 后仍可能遗忘：

1. 前两 numerator blocks 的具体 decomposition；
2. \(a_1,a_2\) 的 order / prefix realization；
3. canonical sphere coordinates \(x_1,x_2\) 的具体 local realization；
4. 某些 prime allocation / Hensel labels 若它们只是证明坐标而没有独立 mathematical predicate，应继续 quotient 掉；
5. exact decimal word \(A\) 的 local block realization；
6. chamber 内更细的 source orientation 若它不被 \(R_T\) 与 exact plane 自动恢复。

尤其 Section 12 的 collision 直接证明：

\[
(T,R_T)
\]

仍会忘掉前两块的 local ordering / prefix realization。

因此最终结构不是 canonical state 的另一种编码。

---

# 15. Consequence for the global Backward architecture

上一轮已经得到：

\[
\boxed{
T_{\rm den,10}
}
\]

作为 cleaned den–decimal pair 的 sufficient proper interface。

本轮进一步得到：

\[
\boxed{
T_{\rm alg\mid den}
=
([\mu:\nu],z_3)
}
\]

以及一个 exact residual relation / predicate

\[
\boxed{
\mathfrak A_T.
}
\]

所以当前 Backward architecture 可以压成：

\[
\boxed{
\text{Global recovery synchronization}
=
T_{\rm den,10}
+
([\mu:\nu],z_3)
+
\text{purely local realization data}.
}
\tag{15.1}
\]

更具体地：

\[
\boxed{
T_{\rm den,10}
\Longrightarrow
G,Q,D,\kappa,\eta_3,\mathcal L,\tau,
}
\]

\[
\boxed{
([\mu:\nu],z_3)
\Longrightarrow
C,\mathcal N_{12},\mathcal C_3,K_{C,D},\ldots
}
\]

在 exact plane 上成立。

因此整个旧图景

\[
T
+
(C,D,\mathcal N_{12})
+
[\mu:\nu]
+
z_3
+
\mathcal C_3
\]

可以严格缩短为

\[
\boxed{
T
+
([\mu:\nu],z_3)
+
\text{local data}.
}
\]

这是本轮最核心的结构性成果。

---

# 16. Next theorem only if justified

本轮结果已经说明下一步不应继续问：

- \(C,D,\mathcal N_{12}\) 是否还能彼此做更多形式 resultant；
- 两个 quadratic 的 discriminant 是否还能组合出新 square gate；
- 是否能只从“都有 rational root”得到 synchronization。

这些路线现在都已被压缩或被 false-gluing 反例否定。

若继续 Backward Strict Layer，最自然的下一 theorem 应该是：

\[
\boxed{
\textbf{Root-Pair Local-Realization Fibre Theorem}.
}
\]

固定

\[
(T,\theta,\zeta),
\]

研究所有满足

\[
C=C_T(\theta,\zeta),
\qquad
\mathcal N_{12}=N_T(\theta,\zeta)
\]

的 actual prefix realizations

\[
(a_1,a_2)
\]

是否：

1. 唯一；
2. uniformly finite；
3. 或仍存在真正 higher-order non-rectangularity。

这会直接检验：

\[
\boxed{
T+R_T
}
\]

是否已经接近完整 Backward separator。

但本轮不继续做这一 theorem。

---

# 17. PROVED / existing / computational / heuristic / open ledger

## PROVED — inherited

1. canonical denominator recovery；
2. sufficient proper den–decimal trace
   \[
   T\simeq(b_1,b_2,b_3,S);
   \]
3. strict scope 的 DD/\(A_1\) coefficient definitions；
4. gap quadratic；
5. primitive-tail quadratic；
6. rational-root divisibility；
7. tail normalization；
8. denominator-tail certificate；
9. complete candidate \(\to\) actual gap root / actual tail root 为 deterministic projections。

---

## REINTERPRETED EXISTING RESULT

\[
\boxed{
\kappa=\frac{M_3QG}{b_3}.
}
\]

本轮只解释其 fixed-\(T\) freezing 作用。

---

## NEW PROVED

1. Fixed-\(T\) \(D\)-freezing：
   \[
   D=\frac{M_3}{S}Q.
   \]

2. Tail–coefficient identity：
   \[
   \kappa\tau=G\mathcal LD.
   \]

3. Unified exact coefficient-plane normal form：
   \[
   \mathcal R
   =
   \frac{\mathcal LC+z_3}{\mathcal LD+\tau}.
   \]

4. Exact oriented linear relation：
   \[
   G^2\mathcal LC-G\kappa z_3-(G+\kappa)\tau\frac{\mu}{\nu}=0.
   \]

5. Sphere/root reconstruction：
   \[
   \mathcal N_{12}
   =
   \left(\frac{\mu}{\nu}\right)^2
   +
   \frac{2G}{\tau}
   \frac{\mu}{\nu}z_3.
   \]

6. \(C\) reconstruction：
   \[
   C
   =
   \frac{
   G\kappa z_3+(G+\kappa)\tau(\mu/\nu)
   }{
   G^2\mathcal L
   }.
   \]

7. \(\mathcal C_3\) reconstruction：
   \[
   \mathcal C_3
   =
   \kappa^2z_3^2
   -
   2(G+\kappa)\tau(\mu/\nu)z_3.
   \]

8. Exact-plane quadratic proportionality：
   \[
   Q_{\rm tail}
   =
   -
   \frac{
   \mathcal L\tau(G+\kappa)^2
   }{
   G\kappa^2
   }
   Q_{\rm gap}.
   \]

9. Quadratic false-gluing factorization：
   \[
   Q_{\rm gap}=Q_{\rm tail}=0
   \Longrightarrow
   \mathcal F_{\rm ex}\mathcal F_{\rm conj}=0.
   \]

10. Explicit false-gluing integer example。

11. Fixed-\(T\) collisions proving：
   \[
   T+\theta\not\Rightarrow z_3,
   \]
   \[
   T+z_3\not\Rightarrow\theta.
   \]

12. Fixed-\(T\) collisions proving：
   \[
   T+\mathcal N_{12}\not\Rightarrow C,
   \]
   \[
   T+C\not\Rightarrow\mathcal N_{12}.
   \]

13. Properness collision：
   \[
   v\ne v',
   \quad
   T(v)=T(v'),
   \quad
   R_T(v)=R_T(v').
   \]

14. Audited residual interface：
   \[
   R_T=([\mu:\nu],z_3)
   \]
   suffices to reconstruct all currently audited alg–den shared coefficient summaries over fixed \(T\).

---

## DERIVED FROM PROVED RESULTS

1. \(D\) 不是 residual algebraic information；
2. \(\mathcal C_3\)、\(K_{C,D}\)、discriminant square root certificates 不应作为独立 interface coordinates；
3. root pair 与
   \[
   (\mathcal R,r_3)
   \]
   等价；
4. theoretical quadratic root multiplicity 不能解释成 two independent global freedoms；
5. denominator-tail certificate 的 denominator-only部分已经完全被 \(T\) 吸收。

---

## DISPROVED CANDIDATE

1. \((C,D,\mathcal N_{12})\) 是三个独立 residual invariants；
2. gap root alone 是 sufficient residual interface；
3. tail root alone 是 sufficient residual interface；
4. discriminant-square data 是 sufficient shared datum；
5. “两个 quadratic 同时有 admissible-looking roots”自动给 exact gluing；
6. 把所有 coefficients + roots 原样打包是 meaningful compression；
7. 在自然 recovery coordinates 中“只剩一个 root coordinate”。

---

## COMPUTATIONAL EVIDENCE

本轮符号计算用于发现：

\[
Q_{\rm tail}\big|_{Q_{\rm gap}=0}
\]

的二线性因子分解。

但最终报告中该 identity 已按显式代数式写出，可直接手工展开验证；因此 theorem 本身标记 **NEW PROVED**，不是仅 computational evidence。

false-gluing 数字例同样已经直接代入核验，不依赖搜索程序作为证明。

---

## HEURISTIC

1. \(R_T=([\mu:\nu],z_3)\) 很可能已经接近 algebraic–denominator 的自然最小 semantic separator；
2. 下一层真正复杂性可能主要存在于 fixed \((T,R_T)\) 下的 prefix local-realization fibre，而不是更多 quadratic coefficients；
3. 如果该 fibre 可 uniformly finite，则 Backward architecture 会显著接近
   \[
   T_{\rm den,10}
   +
   \text{finite root-pair branch}
   +
   \text{local fibre}.
   \]

---

## OPEN

1. 是否存在比 \(([\mu:\nu],z_3)\) 更小、且仍有自然 recovery semantics 的 categorical residual quotient；
2. fixed exact-candidate subfibre 上的 properness 是否仍可用两个真正完整 candidates 证明；
3. fixed \((T,R_T)\) 后 prefix realization fibre 是否 finite / uniformly bounded / rectangular；
4. 当前 \(R_T\) 是否足以作为未来三块 global gluing 的 complete separator；
5. 是否存在 higher-order relation 在当前 audited alg–den relations 之外仍读取额外 shared data。

---

# Final theorem-level verdict

本轮达到的不是“又整理了一组 algebraic variables”，而是：

\[
\boxed{
\textbf{Fixed-Trace Algebraic–Denominator Residual Compression}
}
\]

即：

\[
\boxed{
T_{\rm den,10}
\text{ fixed}
\quad\Longrightarrow\quad
(C,D,\mathcal N_{12},\mathcal C_3,[\mu:\nu],z_3)
\text{ 可压为 }
([\mu:\nu],z_3)
}
\]

在 exact coefficient plane 上。

并且：

\[
\boxed{
\text{gap quadratic}
\quad\text{与}\quad
\text{primitive-tail quadratic}
}
\]

并非两个独立 shared gates；它们在 exact plane 上严格成比例。

真正不可丢失的是：

\[
\boxed{
\textbf{oriented root-pair compatibility},
}
\]

因为若只保留两个 quadratic 的存在性，就会出现明确的 conjugate false gluing。

所以当前 Backward 主架构可写成：

\[
\boxed{
\text{Global recovery synchronization}
=
T_{\rm den,10}
+
T_{\rm alg\mid den}
+
\text{purely local data},
}
\]

其中

\[
\boxed{
T_{\rm alg\mid den}
=
([\mu:\nu],z_3).
}
\]

本轮没有证明 full three-block global rectangularity，也没有进入任何 strict chamber 的 contradiction 攻关。
