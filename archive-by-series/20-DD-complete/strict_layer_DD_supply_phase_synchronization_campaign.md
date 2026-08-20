# 三项十进制拼接平方和问题：DD Supply–Phase Synchronization Campaign

**文件名：** `strict_layer_DD_supply_phase_synchronization_campaign.md`  
**研究范围：** Strict Layer，仅研究 **DD chamber**  
**本轮等级：** **SGR-6F — SYNCHRONIZATION ROUTE FAILS**  
**最终状态：** **DD 尚未闭合**  
**核心裁决：** 当前 post-deflation “Hensel phase” 在精确二因子系统中是高阶相消深度的等价重写，而不是独立于 divisor supply 的第二道算术门；因此仅凭 SGR-5 已投影出的 supply + phase 数据，无法形成 supply–phase incompatibility。

---

# 0. 结论摘要

SGR-5 把 DD 顶部压成

\[
J^\sharp K^\sharp=N^\sharp,
\qquad
J^\sharp+K^\sharp=H^\sharp,
\qquad
\gcd(J^\sharp K^\sharp,10)=1,
\]

同时有 residual divisor envelope

\[
J^\sharp\mid\Omega_{\rm DD}^2,
\qquad
\Omega_{\rm DD}
=
\left(
Q_{12}\mathcal N_{12}\mathscr T
\right)^{\langle10\rangle},
\]

以及所谓 deep phases

\[
(J^\sharp)^2\equiv-N^\sharp
\pmod{p^{R_p^\sharp}},
\qquad
R_p^\sharp=v_p(H^\sharp),
\quad p=2,5.
\]

本轮最重要的发现是：**这两个 phase congruences 并不是 factor-pair system 之外的额外条件。**

因为恒等地有

\[
\boxed{
(J^\sharp)^2+N^\sharp
=
J^\sharp(J^\sharp+K^\sharp)
=
J^\sharp H^\sharp.
}
\tag{SYNC-1}
\]

而 \(J^\sharp\) 对 \(p=2,5\) 都是 unit，所以对任意整数 \(R\ge0\)，

\[
\boxed{
(J^\sharp)^2\equiv-N^\sharp\pmod{p^R}
\iff
p^R\mid H^\sharp.
}
\tag{SYNC-2}
\]

因此取

\[
R=R_p^\sharp=v_p(H^\sharp)
\]

时，phase 自动成立。

同理，

\[
\boxed{
(K^\sharp)^2+N^\sharp
=
K^\sharp H^\sharp,
}
\tag{SYNC-3}
\]

所以 \(K^\sharp\) 也自动满足同一个 square-root congruence，并且

\[
\boxed{
K^\sharp\equiv-J^\sharp
\pmod{p^{R_p^\sharp}}.
}
\tag{SYNC-4}
\]

这把本轮原先设想的

\[
\text{moving divisor supply}
\quad\cap\quad
\text{deep Hensel phase}
\]

重新解释为：

\[
\boxed{
\text{divisor / factor-pair recovery}
\quad+\quad
\text{factor-pair sum的高 }2,5\text{-adic cancellation}.
}
\]

后者不是独立 gate。

更强地，本轮构造了一个**任意深度兼容模型**。给定任意

\[
A,B\ge1,
\qquad
L=2^A5^B,
\]

任取 \(\gcd(d,10)=1\)，再取 \(t\) 使 \(tL>d\)，定义

\[
J^\sharp=d,
\qquad
K^\sharp=tL-d,
\qquad
H^\sharp=tL,
\qquad
N^\sharp=d(tL-d).
\]

则

\[
J^\sharp K^\sharp=N^\sharp,
\qquad
J^\sharp+K^\sharp=H^\sharp,
\]

且

\[
(J^\sharp)^2\equiv-N^\sharp
\pmod{2^A},
\qquad
(J^\sharp)^2\equiv-N^\sharp
\pmod{5^B}.
\]

若再取任意 \(\Omega\) 使 \(d\mid\Omega^2\)（例如 \(\Omega=d\)），则 residual supply 条件也成立。特别 \(d=1\) 时，任意深度都可兼容。

这不是一个真实 DD candidate 的构造；它证明的是更精确的逻辑结论：

\[
\boxed{
\text{SGR-5 当前投影出的 }
\{J^\sharp\mid\Omega^2,\,
JK=N,\,
J+K=H,\,
J^2\equiv-N\}
\text{ 本身不能推出矛盾。}
}
\tag{SYNC-5}
\]

所以本轮等级为

\[
\boxed{\textbf{SGR-6F — SYNCHRONIZATION ROUTE FAILS}.}
\]

失败的不是“DD arithmetic 没有结构”，而是**当前 phase 被投影得过于内在**：它没有保留一个由 prefix/tail source 独立决定、再与 \(J^\sharp\) 相撞的外部局部目标。

---

# 1. 来源审计与范围

## 1.1 本轮实际使用的主文件

重点核对：

- `strict_layer_DD_post_deflation_campaign.md`
- `strict_layer_DD_error_closure_campaign.md`
- `strict_layer_moving_core_square_spacing_campaign.md`
- `exact_lift_research_synthesis_2026-08-10.md`
- `strict_layer_unified_exact_lift_campaign(1).md`

其中：

- post-deflation 文件给出 \(J^\sharp,K^\sharp,H^\sharp,N^\sharp\)、\(\Omega_{\rm DD}\) 与 residual phase；
- error-closure 文件给出 old/new factor 的精确缩放、double resonance、\(E\) 的源变量表达；
- moving-core 文件给出 \(M,E,\rho\) 的规范坐标；
- synthesis 给出当前 DD 顶部尖角、near-\(S\)-unit、极端 denominator asymmetry；
- unified Exact-Lift 文件用于复核 gap quadratic、rational-root divisibility、primitive-profile 尺度。

## 1.2 关于“原始 DD deep Hensel 文件”

当前可检索 File Library 没有暴露一个独立命名、晚于 synthesis 且比上述文件更原始的 DD deep-Hensel 专门报告。上一轮 `strict_layer_DD_post_deflation_campaign.md` 已明确做过同一来源审计，并把可核实的旧 \(5\)-进 phase 记录为

\[
\mu_5\equiv\pm\rho_5\nu_5
\pmod{5^{R_5}},
\]

且旧报告给出

\[
R_5>1.415S_{12}+9.
\]

本轮不虚构未暴露的原始来源；所有“旧 phase \(\to\) post-deflation phase”的使用均以已审计接口为准。

---

# 2. 冻结 DD primitive / prefix / tail 坐标

统一记

\[
S_{12}=m_1+m_2,
\]

\[
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0,
\]

\[
Q_{12}=b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\]

\[
\mathcal N_{12}
=
(a_1b_2)^2+(a_2b_1)^2,
\]

\[
A_{12}
=
a_1 10^{n_2}+a_2.
\]

DD 中

\[
n_3=m_3+d_3.
\]

尾权为

\[
\boxed{
\kappa
=
\frac{10^{m_3}Q_{12}G}{b_3}
\in\mathbf Z,
}
\tag{2.1}
\]

并满足

\[
Q_{12}G<\kappa\le10Q_{12}G.
\]

primitive-profile 写成

\[
a_i=UC_i,
\qquad
b_i=Rh_i,
\]

于是

\[
Q_{12}=R\widehat Q,
\]

\[
G=R^2\widehat G,
\]

\[
\mathcal N_{12}
=
U^2R^2\widehat{\mathcal N},
\]

\[
A_{12}=U\widehat A_{12}.
\]

DD 的统一平方差坐标为

\[
\varepsilon M^2-E=\varepsilon Y^2,
\qquad
0\le Y<M,
\]

其中

\[
\boxed{
M
=
10^{\lfloor m_3/2\rfloor+d_3}
\frac{GA_{12}}{UR^2},
}
\tag{2.2}
\]

\[
\boxed{
E
=
\frac{
Q_{12}\mathcal N_{12}
(10^{m_3}Q_{12}+2b_3)
}{
U^2R^4
}.
}
\tag{2.3}
\]

使用 \(\kappa\)：

\[
\boxed{
E
=
\frac{
10^{m_3}Q_{12}^2\mathcal N_{12}
(\kappa+2G)
}{
U^2R^4\kappa
}.
}
\tag{2.4}
\]

tail certificate 定义

\[
\boxed{
\mathscr T
=
\frac{
\kappa^2(\kappa+2G)
}{
10^{m_3}
}
\in\mathbf Z_{>0},
}
\tag{2.5}
\]

所以

\[
\boxed{
E
=
\frac{
10^{2m_3}Q_{12}^2\mathcal N_{12}\mathscr T
}{
U^2R^4\kappa^3
}.
}
\tag{2.6}
\]

顶部 near-\(S\)-unit 给出

\[
\boxed{
1\le\mathscr T<10^{S_{12}-7}.
}
\tag{2.7}
\]

---

# 3. post-deflation synchronization system 的精确重建

旧 DD factors 为

\[
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
\]

\[
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0}.
\]

error-closure 已证

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda(M-Y),\,
\Lambda(M+Y)
\},
}
\tag{3.1}
\]

其中

\[
\boxed{
\Lambda
=
UR^2\,10^{\lceil m_3/2\rceil}.
}
\tag{3.2}
\]

顶部 double resonance 对 \(p=2,5\) 给出

\[
\boxed{
v_p(M-Y)
=
v_p(M+Y)
=:j_p.
}
\tag{3.3}
\]

定义

\[
\boxed{
D_0=2^{j_2}5^{j_5}.
}
\tag{3.4}
\]

于是

\[
\boxed{
J^\sharp=\frac{M-Y}{D_0},
\qquad
K^\sharp=\frac{M+Y}{D_0}.
}
\tag{3.5}
\]

并有

\[
\boxed{
\gcd(J^\sharp K^\sharp,10)=1.
}
\tag{3.6}
\]

定义

\[
\boxed{
H^\sharp
=
J^\sharp+K^\sharp
=
\frac{2M}{D_0},
}
\tag{3.7}
\]

\[
\boxed{
N^\sharp
=
J^\sharp K^\sharp
=
\frac{E}{\varepsilon D_0^2}.
}
\tag{3.8}
\]

因为 \(D_0^2\) 是 \(E/\varepsilon\) 的完整 \(2,5\)-primary part，

\[
\boxed{
N^\sharp
=
\left(\frac E\varepsilon\right)^{\langle10\rangle},
\qquad
\gcd(N^\sharp,10)=1.
}
\tag{3.9}
\]

所以完整 quadratic 为

\[
\boxed{
X^2-H^\sharp X+N^\sharp=0,
}
\tag{3.10}
\]

两个正整数根恰为

\[
J^\sharp,\quad K^\sharp.
\]

判别式为

\[
\boxed{
(H^\sharp)^2-4N^\sharp
=
\left(\frac{2Y}{D_0}\right)^2.
}
\tag{3.11}
\]

---

# 4. \(N^\sharp\) 与 prefix / tail source 的精确关系

SGR-5 只强调

\[
J^\sharp\mid\Omega_{\rm DD}^2.
\]

但 factor-pair 同时给出

\[
J^\sharp K^\sharp=N^\sharp,
\]

所以必须首先核实 \(N^\sharp\) 自身的 prime-to-\(10\) source factorization。

定义

\[
\boxed{
P_{\rm DD}
:=
(Q_{12}\mathcal N_{12})^{\langle10\rangle}.
}
\tag{4.1}
\]

prime-to-\(10\) part 对乘积是乘法的，因此

\[
\boxed{
\Omega_{\rm DD}
=
P_{\rm DD}\,
\mathscr T^{\langle10\rangle}.
}
\tag{4.2}
\]

但是 \(N^\sharp\) **不是**简单的

\[
P_{\rm DD}^2\mathscr T^{\langle10\rangle}.
\]

由 (2.6)，固定任意素数

\[
\ell\neq2,5.
\]

记

\[
q_\ell=v_\ell(Q_{12}),
\quad
n_\ell=v_\ell(\mathcal N_{12}),
\quad
a_\ell=v_\ell(\kappa),
\]

\[
t_\ell=v_\ell(\mathscr T),
\quad
u_\ell=v_\ell(U),
\quad
r_\ell=v_\ell(R).
\]

因为 \(\ell\nmid10\)，

\[
t_\ell
=
2a_\ell+v_\ell(\kappa+2G).
\]

又因为 \(\varepsilon,D_0\) 只有 \(2,5\)-primary contribution，

\[
v_\ell(N^\sharp)=v_\ell(E).
\]

因此由 (2.6) 得到**精确 source valuation identity**

\[
\boxed{
v_\ell(N^\sharp)
=
2q_\ell+n_\ell+t_\ell
-3a_\ell
-2u_\ell
-4r_\ell.
}
\tag{4.3}
\]

等价地，若记

\[
b_\ell=v_\ell(\kappa+2G),
\]

则

\[
\boxed{
v_\ell(N^\sharp)
=
2q_\ell+n_\ell+b_\ell-a_\ell
-2u_\ell-4r_\ell.
}
\tag{4.4}
\]

### PROVED / DERIVED

(4.3)–(4.4) 是从已经证明的 \(E\) 精确乘商公式直接逐素数取赋值得到的；没有使用估计。

它揭示了一个重要事实：

\[
\boxed{
\Omega_{\rm DD}
\text{ 是 residual supply 的上包络，}
\text{不是 }N^\sharp\text{ 的精确乘法分解。}
}
\]

其中存在真实 valuation sinks

\[
-3v_\ell(\kappa),
\qquad
-2v_\ell(U),
\qquad
-4v_\ell(R).
\]

所以仅由

\[
\ell\mid Q_{12},
\quad
\ell\mid\mathcal N_{12},
\quad
\ell\mid\mathscr T
\]

不能直接判断它最终以什么指数进入 \(N^\sharp\)。

---

# 5. \(J^\sharp,K^\sharp,N^\sharp\) 的最强 prime-factor allocation

## 5.1 先计算 \(\gcd(J^\sharp,K^\sharp)\)

定义

\[
\boxed{
g^\sharp:=\gcd(J^\sharp,K^\sharp).
}
\tag{5.1}
\]

由

\[
J^\sharp+K^\sharp=H^\sharp
\]

立即有

\[
\boxed{
g^\sharp
=
\gcd(J^\sharp,H^\sharp)
=
\gcd(K^\sharp,H^\sharp).
}
\tag{5.2}
\]

另一方面，

\[
\gcd(M-Y,M+Y)
\]

对任意奇素数 \(\ell\) 的赋值，与

\[
\gcd(M,Y)
\]

相同：若 \(\ell\mid M-Y,M+Y\)，则 \(\ell\mid2M,2Y\)，而 \(\ell\) 奇，所以
\(\ell\mid M,Y\)；反向显然。

\(D_0\) 正好除掉两个 factors 共同的全部 \(2,5\)-primary part，因此

\[
\boxed{
g^\sharp
=
\gcd(M,Y)^{\langle10\rangle}.
}
\tag{5.3}
\]

这是当前能得到的最强无条件 gcd 公式。

它并没有把 \(g^\sharp\) 压成常数，但把“两个 residual factors 的公共奇素数”精确定位成：

\[
\boxed{
\text{统一平方根 }(M,Y)
\text{ 的 prime-to-}10\text{ common content}.
}
\]

---

## 5.2 canonical coprime-kernel decomposition

写

\[
\boxed{
J^\sharp=g^\sharp A,
\qquad
K^\sharp=g^\sharp B,
\qquad
\gcd(A,B)=1,
}
\tag{5.4}
\]

且

\[
\gcd(g^\sharp AB,10)=1.
\]

于是

\[
\boxed{
N^\sharp=(g^\sharp)^2AB,
}
\tag{5.5}
\]

\[
\boxed{
H^\sharp=g^\sharp(A+B).
}
\tag{5.6}
\]

固定任意 \(\ell\neq2,5\)，令

\[
\gamma_\ell=v_\ell(g^\sharp),
\quad
\alpha_\ell=v_\ell(A),
\quad
\beta_\ell=v_\ell(B).
\]

因为 \(\gcd(A,B)=1\)，

\[
\boxed{
\min(\alpha_\ell,\beta_\ell)=0.
}
\tag{5.7}
\]

而

\[
\boxed{
v_\ell(N^\sharp)
=
2\gamma_\ell+\alpha_\ell+\beta_\ell.
}
\tag{5.8}
\]

所以每个 residual prime exponent 具有严格的两级 allocation：

1. \(2\gamma_\ell\) 进入公共平方 content \((g^\sharp)^2\)；
2. 剩余
   \[
   v_\ell(N^\sharp)-2\gamma_\ell
   \]
   **全部且仅能进入 \(A,B\) 的一侧**。

因此：

\[
\boxed{
N^\sharp/(g^\sharp)^2
=
AB
\text{ 是一次真正的 coprime complementary allocation}.
}
\tag{5.9}
\]

特别：

- 若 \(v_\ell(N^\sharp)=1\)，则 \(\ell\) 必须只进入 \(J^\sharp,K^\sharp\) 中一边；
- 若某个 exponent 的奇数部分不能被公共平方 content 吸收，则其残余必须单边分配；
- 两边能共享的 residual prime 只来自 \(g^\sharp\)。

这是本轮在 factor-pair 方向得到的最强新结构。

---

## 5.3 source-labelled allocation 尚未得到

Gap quadratic 为

\[
Q_{12}(\kappa+2G)\mu^2
-
2G\kappa C\,\mu\nu
+
\kappa Q_{12}\mathcal N_{12}\nu^2
=0,
\]

\[
\gcd(\mu,\nu)=1,
\]

并有 rational-root divisibility

\[
\boxed{
\nu\mid Q_{12}(\kappa+2G),
}
\tag{5.10}
\]

\[
\boxed{
\mu\mid\kappa Q_{12}\mathcal N_{12}.
}
\tag{5.11}
\]

SGR-5 对每个 \(\ell\neq2,5\) 由此得到

\[
v_\ell(J^\sharp)
\le
2v_\ell(\Omega_{\rm DD}),
\]

最终即

\[
J^\sharp\mid\Omega_{\rm DD}^2.
\]

但 (5.10)–(5.11) 只给 source **capacity**，没有给：

\[
\ell\mid Q_{12}
\Longrightarrow
\ell\text{ 只能进入 }J^\sharp,
\]

或

\[
\ell\mid\mathscr T
\Longrightarrow
\ell\text{ 只能进入 }K^\sharp
\]

一类 exclusivity。

原因是：

- \(Q_{12}\) 同时出现在 \(\mu,\nu\) 的上界中；
- \(\mathcal N_{12}\) 可进入 \(\mu\)；
- \(\kappa,\kappa+2G\) 的 residual primes 又通过 \(\mathscr T\) 合并；
- \(G_0,\Lambda\) 会进一步消去赋值。

### OPEN

尚无已证定理把

\[
Q_{12},
\qquad
\mathcal N_{12},
\qquad
\mathscr T
\]

的 prime supports 分成三个互斥 source labels。

同样，现有材料没有证明

\[
\gcd(
P_{\rm DD},
\mathscr T^{\langle10\rangle}
)
\]

有高度无关上界或属于固定有限素数集合。

因此 supply 不能严谨地改写成一个固定生成元的 multiplicative semigroup。

---

# 6. deep Hensel phases：完整 lifted root structure

现在固定

\[
p\in\{2,5\},
\qquad
R_p^\sharp=v_p(H^\sharp).
\]

由于

\[
\gcd(J^\sharp K^\sharp,10)=1,
\]

\(J^\sharp,K^\sharp,N^\sharp\) 都是 \(p\)-adic units。

---

## 6.1 5-adic roots

考虑

\[
x^2\equiv-N^\sharp\pmod{5^R}.
\]

只要存在一个 unit root，导数

\[
2x
\]

在模 \(5\) 下为 unit，因此每个模 \(5\) 的 root 唯一 Hensel-lift 到所有深度。

在本系统中 \(J^\sharp\) 本身就是 root，所以对 \(R\ge1\) 精确有两条 lifted branches：

\[
\boxed{
x\equiv\pm J^\sharp
\pmod{5^R}.
}
\tag{6.1}
\]

而

\[
K^\sharp
\equiv-J^\sharp
\pmod{5^{R_5^\sharp}},
\]

所以 complementary factor 正好占据 opposite branch。

### 来源审计

旧 DD \(5\)-进分析确实有

\[
\mu_5
\equiv
\pm\rho_5\nu_5
\pmod{5^{R_5}},
\]

并有很深的 \(R_5\)。但可核实的 post-deflation transfer 只把它识别为两个 factor unit parts 的深相消；现有文件没有证明旧 \(\pm\) sign 被额外的 decimal carrier 数据唯一锁死。

因此本轮不能把 5-adic root branches 从两条缩成一条外部固定 branch。

---

## 6.2 2-adic roots

考虑奇数 unit

\[
u=-N^\sharp.
\]

对 \(R\ge3\)，奇 unit 是平方模 \(2^R\) 当且仅当

\[
u\equiv1\pmod8.
\]

本系统已有奇 root \(J^\sharp\)，所以该条件自动成立。

root 数量为：

- \(R=1\)：一个 odd class；
- \(R=2\)：两个 root classes；
- \(R\ge3\)：四个 root classes。

若 \(R\ge3\)，以 \(J^\sharp\) 为一个 root，可写成

\[
\boxed{
x\equiv
J^\sharp,\ 
-J^\sharp,\ 
J^\sharp+2^{R-1},\
-J^\sharp+2^{R-1}
\pmod{2^R}.
}
\tag{6.2}
\]

等价地，

\[
\boxed{
x\equiv\pm J^\sharp
\pmod{2^{R-1}}.
}
\tag{6.3}
\]

而 actual complementary factor 满足更强的

\[
\boxed{
K^\sharp\equiv-J^\sharp
\pmod{2^{R_2^\sharp}}.
}
\tag{6.4}
\]

### OPEN

现有 DD 文件没有暴露一个独立的 2-adic branch-locking theorem，把 \(J^\sharp\) 从四个 root classes 中固定到一个由 prefix/tail 单独决定的 class。

---

# 7. 新核心定理：Phase Redundancy / Automatic Synchronization

## 定理 DD-SYNC-R

设

\[
J,K,H,N\in\mathbf Z_{>0},
\]

满足

\[
JK=N,
\qquad
J+K=H,
\]

并设 \(p\nmid J\)。

则对任意 \(R\ge0\)，

\[
\boxed{
J^2\equiv-N\pmod{p^R}
\iff
p^R\mid H.
}
\tag{7.1}
\]

### 证明

由

\[
N=JK
\]

以及

\[
H=J+K
\]

有

\[
J^2+N
=
J^2+JK
=
J(J+K)
=
JH.
\]

所以

\[
J^2\equiv-N\pmod{p^R}
\]

等价于

\[
p^R\mid JH.
\]

因为 \(p\nmid J\)，等价于

\[
p^R\mid H.
\]

证毕。

---

## DD 中的直接推论

对

\[
p=2,5
\]

都有

\[
p\nmid J^\sharp.
\]

因此

\[
\boxed{
(J^\sharp)^2\equiv-N^\sharp
\pmod{p^R}
\iff
p^R\mid H^\sharp.
}
\tag{7.2}
\]

特别取

\[
R=R_p^\sharp=v_p(H^\sharp),
\]

SGR-5 的 residual Hensel phase 是自动成立的。

同理，

\[
\boxed{
(K^\sharp)^2\equiv-N^\sharp
\pmod{p^R}
\iff
p^R\mid H^\sharp.
}
\tag{7.3}
\]

所以两个 complementary factors 同时是 \(-N^\sharp\) 的 roots，不是额外巧合，而是 factor-pair identity 的必然结果。

---

## 7.1 elimination 立即退化

原本可以尝试消去 \(J^\sharp\)：

\[
(J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0
\]

与

\[
(J^\sharp)^2+N^\sharp\equiv0\pmod{p^R}.
\]

两式相减：

\[
-H^\sharp J^\sharp\equiv0\pmod{p^R}.
\]

由于 \(J^\sharp\) 是 unit，

\[
\boxed{
H^\sharp\equiv0\pmod{p^R}.
}
\]

这正是 \(R\le v_p(H^\sharp)\)。

因此本轮允许的“新 elimination”在当前 phase 上**严格退化为定义本身**；不会生成新的 prefix/tail compatibility polynomial。

---

## 7.2 character / subgroup 攻击为何也在当前投影上退化

phase 给出

\[
-N^\sharp
\equiv
(J^\sharp)^2
\pmod{p^R}.
\]

所以 \(-N^\sharp\) 所属的 square coset 本来就是由 \(J^\sharp\) 自己生成。

若没有一个独立于 \(J^\sharp\) 的 source theorem 先限制 \(J^\sharp\) 所在的 unit subgroup / character class，则：

\[
\text{“phase target subgroup”}
\]

不是外部目标，而是 actual factor 自身的像。

因此仅从

\[
J^\sharp\mid\Omega_{\rm DD}^2
\]

和

\[
J^{\sharp2}\equiv-N^\sharp
\]

不能构造一个非平凡 character contradiction。

---

# 8. CRT synchronization：存在，但没有产生新约束

定义

\[
\boxed{
L_{\rm phase}
=
2^{R_2^\sharp}5^{R_5^\sharp}.
}
\tag{8.1}
\]

由两个 cancellation conditions，

\[
\boxed{
L_{\rm phase}\mid H^\sharp.
}
\tag{8.2}
\]

并且

\[
\boxed{
K^\sharp\equiv-J^\sharp
\pmod{L_{\rm phase}}.
}
\tag{8.3}
\]

若 \(R_2^\sharp\ge3\)、\(R_5^\sharp\ge1\)，纯平方根方程最多给

\[
4\times2=8
\]

个 CRT root classes modulo \(L_{\rm phase}\)。

但是 actual \(J^\sharp\) 的 class 必然是其中之一，actual \(K^\sharp\) 必然是相反 branch。

因此：

\[
\boxed{
\mathcal R_{\rm phase}
\text{ 不是一个预先独立生成的稀疏集合；}
\text{它随 actual factor pair 同步移动。}
}
\tag{8.4}
\]

即使未来证明

\[
L_{\rm phase}>J^\sharp
\]

或

\[
L_{\rm phase}>2J^\sharp,
\]

也只会说明**给定当前移动 target 后代表元唯一**，不会自动说明这个代表元不是 \(J^\sharp\)，因为 target 本来就是由 \(J^\sharp\) 生成的。

所以 Mechanism I / DD-SYNC-2 所需的关键缺项不是“模数再大一点”，而是：

\[
\boxed{
\text{phase residue 必须先独立于 }J^\sharp
\text{ 被 source data 固定。}
}
\]

---

# 9. residual divisor set 的严格层级

不能把所有

\[
d\mid\Omega_{\rm DD}^2
\]

都当成 actual candidates。

本轮区分三层集合。

## 9.1 envelope divisor set

\[
\boxed{
\mathcal D_{\rm env}
=
\{
d>0:
d\mid\Omega_{\rm DD}^2,\ 
\gcd(d,10)=1
\}.
}
\tag{9.1}
\]

这是 SGR-5 直接证明的外包络。

---

## 9.2 source-capacity divisor set

令 \(\mathcal D_{\rm src}\subseteq\mathcal D_{\rm env}\) 进一步要求存在 primitive root witness
\((\mu,\nu)\) 满足：

\[
\gcd(\mu,\nu)=1,
\]

gap quadratic，

\[
\nu\mid Q_{12}(\kappa+2G),
\]

\[
\mu\mid\kappa Q_{12}\mathcal N_{12},
\]

并且 \(d\) 等于两个 Exact factors 中较小者除去 \(\Lambda D_0\)。

这个定义保留了 source orientation，而不把它虚假简化成任意 divisor。

---

## 9.3 actual DD residual set

\[
\boxed{
\mathcal D_{\rm actual}
}
\]

还必须同时满足全部：

- primitive recovery；
- exact coefficient plane；
- digit windows；
- denominator recovery；
- third-tail realization；
- DD chamber；
- top-corner conditions；
- square gate。

于是

\[
\boxed{
\mathcal D_{\rm actual}
\subseteq
\mathcal D_{\rm src}
\subseteq
\mathcal D_{\rm env}.
}
\tag{9.2}
\]

本轮的新裁决是：

\[
\boxed{
d\in\mathcal D_{\rm actual}
\Longrightarrow
d\in\mathcal R_{\rm phase}
}
\]

在当前 residual phase 定义下是**自动的**，而不是一个可能排空交集的额外过滤器。

所以当前正确的关系不是

\[
\mathcal D_{\rm actual}
\cap
\mathcal R_{\rm phase}
\stackrel{?}{=}\varnothing,
\]

而是

\[
\boxed{
\mathcal D_{\rm actual}
\subseteq
\mathcal R_{\rm phase}.
}
\tag{9.3}
\]

这里的 \(\mathcal R_{\rm phase}\) 是随同一 candidate 移动的 phase fibre。

---

# 10. 任意深度兼容模型：证明不是“估计还不够强”

这是 SGR-6F 的关键。

## 定理 DD-SYNC-M（abstract arbitrary-depth compatibility）

给定任意

\[
A,B\ge1,
\]

令

\[
L=2^A5^B.
\]

任取

\[
d\in\mathbf Z_{>0},
\qquad
\gcd(d,10)=1,
\]

再取整数 \(t\ge1\) 使

\[
tL>d.
\]

定义

\[
\boxed{
J=d,
\quad
K=tL-d,
\quad
H=tL,
\quad
N=d(tL-d).
}
\tag{10.1}
\]

则：

\[
JK=N,
\qquad
J+K=H.
\]

因为

\[
K\equiv-d\pmod{10},
\]

有

\[
\gcd(JK,10)=1.
\]

并且

\[
J^2+N
=
d^2+d(tL-d)
=
dtL.
\]

所以

\[
\boxed{
J^2\equiv-N\pmod{2^A},
}
\tag{10.2}
\]

\[
\boxed{
J^2\equiv-N\pmod{5^B}.
}
\tag{10.3}
\]

若再取任意 \(\Omega\) 使

\[
d\mid\Omega^2,
\]

则 supply 条件也成立。

特别取

\[
d=1,
\qquad
t=1,
\]

得到

\[
\boxed{
J=1,
\quad
K=L-1,
\quad
H=L,
\quad
N=L-1,
\quad
\Omega=1.
}
\tag{10.4}
\]

于是对任意 \(A,B\) 都有一个满足：

\[
J\mid\Omega^2,
\]

\[
JK=N,
\]

\[
J+K=H,
\]

\[
J^2\equiv-N\pmod{2^A},
\]

\[
J^2\equiv-N\pmod{5^B}
\]

的正整数 unit model。

### 解释边界

这**不是**原题 DD candidate。

它不声称 \(Q_{12},\mathcal N_{12},\kappa,\mathscr T,U,R\) 能恢复出该模型。

它严格证明的是：

\[
\boxed{
\text{只保留 SGR-5 的 residual supply + factor pair + residual phase，
即使 phase depth 任意大，也不存在逻辑矛盾。}
}
\tag{10.5}
\]

因此“divisor scarcity vs deep phase”若要复活，必须引入一个在上述抽象模型中没有编码、但真实 DD candidate 必须满足的新 invariant。

---

# 11. 对原先五种 synchronization mechanism 的裁决

## Mechanism I — divisor scarcity vs phase modulus

**裁决：当前形式失败。**

原因不是 divisor count 估计弱，而是 target residue 由 \(J^\sharp\) 自己移动生成。

即使

\[
L_{\rm phase}\gg \Omega_{\rm DD}^2
\]

或

\[
L_{\rm phase}\gg J^\sharp,
\]

也不能从当前 phase 推出矛盾。

---

## Mechanism II — factor-pair synchronization

**裁决：得到真正新结构，但 phase 不增加约束。**

新结构是

\[
J^\sharp=g^\sharp A,
\quad
K^\sharp=g^\sharp B,
\quad
\gcd(A,B)=1,
\]

\[
N^\sharp=(g^\sharp)^2AB.
\]

这把每个 residual prime 分成：

\[
\text{common square content}
+
\text{exclusive complementary allocation}.
\]

但

\[
J^{\sharp2}\equiv-N^\sharp
\]

只是

\[
p^R\mid H^\sharp
\]

的重写。

---

## Mechanism III — source-labelled prime allocation

**裁决：尚未形成。**

现有 RRT 只给 capacity upper bounds；没有从

\[
Q_{12},
\quad
\mathcal N_{12},
\quad
\mathscr T
\]

到 \(A/B\) 的互斥 source labelling theorem。

---

## Mechanism IV — quadratic root uniqueness

**裁决：当前 phase 与 quadratic 完全同源。**

消去 \(J^\sharp\) 后只剩

\[
p^R\mid H^\sharp.
\]

因此不能把“quadratic root”和“phase root”当两套独立 root selectors。

---

## Mechanism V — prefix / tail independence

**裁决：现有公式没有证明这种解耦。**

当前

\[
N^\sharp
\]

同时读取 prefix 与 tail：

\[
v_\ell(N^\sharp)
=
2q_\ell+n_\ell+t_\ell
-3a_\ell-2u_\ell-4r_\ell.
\]

而 phase 又由

\[
H^\sharp=J^\sharp+K^\sharp
\]

生成。

所以没有得到：

\[
\text{prefix 独立决定 supply},
\qquad
\text{tail 独立决定 phase}.
\]

恰恰相反，当前 phase 是 full factor-pair 的内部投影。

---

# 12. near-\(S\)-unit 的真实剩余作用

写

\[
\kappa=2^a5^bu,
\qquad
\kappa+2G=2^c5^ev,
\]

其中

\[
\gcd(uv,10)=1.
\]

则

\[
\boxed{
\mathscr T^{\langle10\rangle}=u^2v.
}
\tag{12.1}
\]

并且

\[
\mathscr T<10^{S_{12}-7}.
\]

所以 tail residual generators 的 Archimedean 规模确实受压。

但是：

1. \(P_{\rm DD}\) 仍移动；
2. 没有证明
   \[
   \gcd(P_{\rm DD},\mathscr T^{\langle10\rangle})
   \]
   高度无关；
3. 没有证明 \(\omega(\mathscr T)\) 或 \(\tau(\mathscr T)\) 高度无关；
4. 即使 tail generators 很少，当前 phase 也没有提供独立 character target。

所以 near-\(S\)-unit 本轮没有转化成 DD-SYNC-4。

它仍然可能在未来与一个**非内生 phase invariant**结合，但不能和 (7.2) 这一 tautological phase 单独闭合。

---

# 13. Archimedean modulus comparison 的最终裁决

SGR-5 已有

\[
\boxed{
J^\sharp
<
14443\cdot10^{3S_{12}-10}.
}
\tag{13.1}
\]

旧 \(5\)-进 phase 文献接口给出很深的 \(R_5\)，但当前材料没有一个可安全使用的、同时对

\[
R_2^\sharp,
\quad
R_5^\sharp
\]

给出完整线性增长公式并证明

\[
2^{R_2^\sharp}5^{R_5^\sharp}
>
14443\cdot10^{3S_{12}-10}.
\]

因此目前不能证明

\[
L_{\rm phase}>J^\sharp.
\]

更重要的是，本轮证明：

\[
\boxed{
\text{即使未来得到 }L_{\rm phase}>J^\sharp,
\text{也不会仅凭当前 phase 自动闭合。}
}
\tag{13.2}
\]

因为 current residue class 是由 actual \(J^\sharp\) 自身定义的。

所以“phase eventually exceeds supply resolution”必须改写为：

> **source independently predicts a phase class**, and only then can the growing modulus outrun the divisor interval.

缺少“independently”这一项时，modulus growth 本身没有终止力。

---

# 14. 最强新 obstruction / 负 obstruction 定理

本轮没有得到 DD-SYNC-1 至 DD-SYNC-5 中的正向 closure。

得到的是一个严格的 **negative synchronization theorem**：

## DD-SYNC-N — Endogenous Phase Theorem

在 DD post-deflation 系统中，若只保留

\[
J^\sharp K^\sharp=N^\sharp,
\]

\[
J^\sharp+K^\sharp=H^\sharp,
\]

\[
\gcd(J^\sharp K^\sharp,10)=1,
\]

并定义

\[
R_p^\sharp=v_p(H^\sharp),
\]

则所谓 local phase

\[
(J^\sharp)^2\equiv-N^\sharp
\pmod{p^{R_p^\sharp}}
\]

不是独立约束，而是 factor-pair identity 的严格推论；事实上对任意 \(R\) 有 equivalence (7.2)。

因此：

\[
\boxed{
\text{任何只使用 }
J^\sharp\mid\Omega_{\rm DD}^2
\text{ 与 residual phase (PD-4) 的 proof，
若不重新引入 source-specific information，
都不可能产生真正的 supply–phase contradiction。}
}
\tag{14.1}
\]

这里“都不可能”的精确含义是：

- 该投影系统存在任意深度的兼容整数模型；
- phase elimination 只返回 \(p^R\mid H^\sharp\)；
- phase 不独立缩小 actual factor-pair fibre。

这正好达到用户为 SGR-6F 要求的“模型解释”。

---

# 15. 唯一剩余 terminal gap

本轮结束后，不再留下：

- divisor scarcity；
- CRT；
- Hensel；
- near-\(S\)-unit；
- factor pair；
- subgroup

六个平行方向。

它们现在压成一个最小缺口：

\[
\boxed{
\textbf{Non-tautological phase descent gap.}
}
\]

精确命题如下。

> **Terminal Gap DD-NTPS.**  
> 从旧 DD 的 \((\mu,\nu,\kappa,Q_{12},\mathcal N_{12},G,G_0)\) deep-Hensel / source 数据中，
> 提取一个对 \(p=2\) 或 \(5\) 的 source-determined unit invariant
> \[
> \Theta_p
> =
> \Theta_p(
> Q_{12},\mathcal N_{12},\kappa,G,\ldots
> )
> \]
> 与深度 \(r_p\)，使完整 candidate 必须满足
> \[
> J^\sharp\in\Theta_p\pmod{p^{r_p}},
> \]
> 且该条件**不是**
> \[
> p^{r_p}\mid H^\sharp
> \]
> 或
> \[
> K^\sharp\equiv-J^\sharp
> \]
> 的形式推论。
> 随后再将这个真正外部的 source phase 与
> \[
> J^\sharp\in\mathcal D_{\rm src}
> \]
> 比较。

等价地：

\[
\boxed{
\text{必须证明 old }\mu/\nu\text{ Hensel branch
在映射到 }J^\sharp\text{ 后仍保留一位“非内生数字”。}
}
\tag{15.1}
\]

如果所有 old phase 在 exact bridge 下都完全坍缩为

\[
K^\sharp\equiv-J^\sharp,
\]

那么 supply–phase 路线就彻底结束；DD 必须使用别的 invariant。

这是本轮唯一保留的 terminal gap。

---

# 16. 结果等级

## SGR-6A — DD CLOSED

未达到。

## SGR-6B — SYNCHRONIZATION TAIL CLOSED

未达到。

## SGR-6C — UNIFORM SYNCHRONIZATION LEMMA

未得到正向 incompatibility；反而得到 uniform redundancy theorem。

## SGR-6D — FINITE RESIDUAL SYNCHRONIZATION

未达到。\(P_{\rm DD}\) 仍移动。

## SGR-6E — STRUCTURAL PARTIAL

本轮确有新的 gcd / factor allocation 结构，但这低估了核心负结果，因为已经严格证明当前 projected synchronization route 本身不能闭合。

## SGR-6F — SYNCHRONIZATION ROUTE FAILS

\[
\boxed{\textbf{达到。}}
\]

理由：

1. residual phase 与 \(H^\sharp\) cancellation depth 等价；
2. elimination 严格退化；
3. 有任意深度兼容模型；
4. 当前 supply envelope 与 phase 不存在可由现有投影推出的 uniform incompatibility；
5. 唯一需要恢复的是一个非内生的 source phase invariant。

---

# 17. PROVED / DERIVED / HEURISTIC / COMPUTATIONAL EVIDENCE / OPEN ledger

## PROVED

继承：

1. 
   \[
   J^\sharp K^\sharp=N^\sharp,
   \qquad
   J^\sharp+K^\sharp=H^\sharp.
   \]
2.
   \[
   \gcd(J^\sharp K^\sharp,10)=1.
   \]
3.
   \[
   J^\sharp\mid\Omega_{\rm DD}^2.
   \]
4.
   \[
   \Omega_{\rm DD}
   =
   (Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}.
   \]
5.
   \[
   \mathscr T<10^{S_{12}-7}.
   \]
6. old/new factor bridge 与 double resonance。

本轮新证：

7. **Phase Redundancy Theorem**
   \[
   J^{\sharp2}\equiv-N^\sharp\pmod{p^R}
   \iff
   p^R\mid H^\sharp.
   \]
8. companion factor 也满足同一 phase。
9. phase + quadratic elimination 只返回
   \[
   p^R\mid H^\sharp.
   \]
10. 
    \[
    \gcd(J^\sharp,K^\sharp)
    =
    \gcd(M,Y)^{\langle10\rangle}.
    \]
11. canonical coprime-kernel factorization
    \[
    J^\sharp=g^\sharp A,\ 
    K^\sharp=g^\sharp B,\ 
    \gcd(A,B)=1.
    \]
12. residual exponent 分成 common-square + exclusive allocation：
    \[
    v_\ell(N^\sharp)
    =
    2\gamma_\ell+\alpha_\ell+\beta_\ell,
    \quad
    \min(\alpha_\ell,\beta_\ell)=0.
    \]
13. 任意深度 abstract compatibility model DD-SYNC-M。

---

## DERIVED

1. 
   \[
   N^\sharp=(E/\varepsilon)^{\langle10\rangle}.
   \]
2. 对 \(\ell\neq2,5\)，
   \[
   v_\ell(N^\sharp)
   =
   2q_\ell+n_\ell+t_\ell
   -3a_\ell-2u_\ell-4r_\ell.
   \]
3.
   \[
   \Omega_{\rm DD}
   =
   P_{\rm DD}\mathscr T^{\langle10\rangle}.
   \]
4. actual phase fibre 对 actual divisor 不提供额外过滤：
   \[
   \mathcal D_{\rm actual}
   \subseteq
   \mathcal R_{\rm phase}.
   \]
5. current character/subgroup attack 若只读取 residual phase，则没有独立 target。

---

## HEURISTIC

1. 旧 \((\mu,\nu)\) phase 也许仍含有在 SGR-5 投影时丢失的 sign/source information。
2. 若能保留一条由 prefix/tail 单独决定的 branch lock，则 synchronization route 可能复活。
3. extreme denominator asymmetry 也许能进一步压 \(g^\sharp\) 或 source-labelled allocation，但本轮没有证明。

---

## COMPUTATIONAL EVIDENCE

**无。**

本轮所有新结论均为符号推导；没有使用固定模数搜索或 divisor enumeration。

---

## OPEN

只保留一个：

\[
\boxed{
\text{DD-NTPS：旧 deep Hensel 是否能下降为一个
不等价于 }p^R\mid H^\sharp
\text{ 的 source-determined }J^\sharp\text{ unit invariant？}
}
\]

---

# 18. 最终裁决

本轮原问题是：

\[
\boxed{
\text{一个由 moving prefix 供给的整数，}
\text{是否有能力同时命中两个极深局部平方根？}
}
\]

答案在当前 SGR-5 residual 坐标中是：

\[
\boxed{
\textbf{有，而且 phase 命中是自动的。}
}
\]

因为“目标平方根”本身就是由同一个 factor pair 产生：

\[
-N^\sharp
\equiv
(J^\sharp)^2
\]

不是来自独立 source 的外部要求。

因此不能把 DD 的最后自由度描述成：

\[
\text{divisor supply}
\quad\text{vs}\quad
\text{deep phase}.
\]

更准确的最终结构是：

\[
\boxed{
\text{source-constrained factor pair}
\quad\text{vs}\quad
\text{尚未恢复的 non-tautological old-Hensel information}.
}
\]

所以：

\[
\boxed{
\textbf{SGR-6F — SYNCHRONIZATION ROUTE FAILS}.
}
\]

\[
\boxed{
\textbf{DD remains open.}
}
\]

唯一下一步不是继续加深 CRT，而是判断旧 DD Hensel 数据在经过

\[
(F_-,F_+)
\longleftrightarrow
\Lambda D_0(J^\sharp,K^\sharp)
\]

这条 exact bridge 后，是否还保留任何不被

\[
J^\sharp K^\sharp=N^\sharp,
\qquad
J^\sharp+K^\sharp=H^\sharp
\]

吸收的 source-dependent branch datum。
