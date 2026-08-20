# 第二个 85 · 第二轮
## Absolute-Oversize Guillotine × Radial Ratio Band × Square-Conditioned Common-\(U\) Extinction

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 第二个 85 · 第二轮 / Phase-II Central Assault  
**Frozen input:** `85_phaseII_R1_moving_square_exactization.md`  
**Global completion criterion:** \(J=2\Rightarrow\varnothing\)

> 注：标题中的控制字符仅来自生成环境，正文数学记号统一使用 `common-U`；不改变任何定义。

---

# 1. Executive Verdict

```text
J2_STATUS = OPEN

ABSOLUTE_OVERSIZE_THEOREM = OPEN

REAL_RADIAL_INCOMPATIBILITY = FALSE
# meaning: the raw Task-E theorem
# exact-root + R1 deep gates => rho notin B_10
# is exactly falsified.

LEVEL_II_AFTER_OVERSIZE_BYPASS = NOT_REACHED
# no K1 countermodel c<G and C2<G^2 K has been found.

INTEGER_RADIAL_EXTINCTION = NOT_REACHED
COPRIME_RADIAL_EXTINCTION = NOT_REACHED

FULL_COMMON_U_COUNTERMODEL = NOT_FOUND

RADIAL_PRIMARY_FAILURE_LEVEL = OVERSIZE

MOVING_INFORMATION_ACTIVATED = YES

CLASS_INTERFACE = NOT_VISIBLE
DESCENT_INTERFACE = NOT_VISIBLE

R2_TERMINAL_VERDICT = NEXT_GATE_IDENTIFIED
```

本轮没有关闭 \(J=2\)，但完成了两件严格推进。

第一，精确恢复 common-\(U\) 两个窗口后，real overlap 完全等价于一个严格开 decade band：

\[
\boxed{
I_2\cap I_3\neq\varnothing
\iff
\frac1{10}<\rho<10.
}
\]

第二，本轮构造了一个比 R1 更深的 exact countermodel。它同时通过：

- exact root；
- moving square；
- source lattice；
- positivity；
- ten-unit；
- regularity；
- common-\(V\)；
- full primitive normalization；
- **real radial overlap** \(I_2\cap I_3\neq\varnothing\)；

但仍满足

\[
\boxed{c\ge G,\qquad C_2\ge G^2K.}
\]

因此它死在 real-overlap 之前的 absolute scale gate，而不是 ratio gate。

这严格杀掉了候选定理

\[
\boxed{
\text{square-conditioned exact root}
\Longrightarrow
\rho\notin(1/10,10)
}
\]

作为 universal architecture。

当前真正仍存活的对象已经不是 “root branch 是否进入 decade band”，而是：

\[
\boxed{
\textbf{进入 decade band 的 primitive source ray，
其最小整数代表是否必然 oversize？}
}
\]

这就是 R3 唯一主接口。

---

# 2. R1 Frozen Inputs

固定

\[
G=10^g,\qquad K=10^k,\qquad H=\frac G2,
\]

\[
uq=G+1,
\qquad
A=2u+1,
\qquad
B=2G+q.
\]

R1 当前 fully audited central regular scope 为

\[
g\ge4,\qquad k\ge1,\qquad \ell=2g-k\ge6,
\qquad u>1,\quad q>1.
\]

Exact PRE_ROOT reconstruction：

\[
\boxed{C_3=c,}
\]

\[
\boxed{C_2=Ac+H\lambda,}
\tag{2.1}
\]

\[
\boxed{2KC_1=Bz+A\lambda,}
\tag{2.2}
\]

\[
\boxed{T=Gz+u\lambda.}
\tag{2.3}
\]

并定义

\[
h=qHz-Ac,
\]

\[
m=Ah-Gz,
\]

\[
r=Hh-uc,
\]

\[
w=GHz-uAc,
\]

\[
d_2=uc+Gw.
\]

Exact root 为

\[
\boxed{
H^2C_1^2+w^2=Td_2.
}
\tag{ROOT}
\]

R1 已经证明 ambient square nonrepresentation 为假，并将 deepest known failure 压到 common-\(U\) radial digit lift；discriminant/class-group/descent 在本轮继续冻结。

---

# 3. Exact common-\(U\) inequalities

J2 的第二、第三 numerator digit windows 精确是

\[
\boxed{
\frac{G^2K}{10}\le UC_2<G^2K,
}
\tag{U2}
\]

\[
\boxed{
\frac G{10}\le Uc<G.
}
\tag{U3}
\]

其中 \(U\in\mathbf Z_{>0}\) 是 actual common radial numerator scale。

所以 exact integer interval 为

\[
U_{\rm lo}
=
\max\left(
\left\lceil\frac{G^2K}{10C_2}\right\rceil,
\left\lceil\frac G{10c}\right\rceil,
1
\right),
\]

\[
U_{\rm hi}
=
\min\left(
\left\lfloor\frac{G^2K-1}{C_2}\right\rfloor,
\left\lfloor\frac{G-1}{c}\right\rfloor
\right).
\]

端点 convention 因而是：

\[
\boxed{\text{left closed, right open}.}
\]

没有额外的 equality branch：若 \(UC_2=G^2K\) 或 \(Uc=G\)，已经进入下一 digit length，故严格排除。

Full common-\(U\) 还要求

\[
\boxed{\gcd(U,uGH)=1.}
\]

本轮按攻击树不提前使用该 gcd。

---

# 4. Exact real intervals

暂时放松到

\[
U\in\mathbf R_{>0}.
\]

定义

\[
\boxed{
I_2=
\left[
\frac{G^2K}{10C_2},
\frac{G^2K}{C_2}
\right),
}
\tag{I2}
\]

\[
\boxed{
I_3=
\left[
\frac{G}{10c},
\frac Gc
\right).
}
\tag{I3}
\]

于是

\[
\boxed{
\text{real common-}U
\iff
I_2\cap I_3\ne\varnothing.
}
\]

---

# 5. Radial ratio band — exact iff theorem

定义

\[
\boxed{
\rho:=\frac{C_2}{GKc}.
}
\tag{RHO}
\]

令

\[
a=\frac{G^2K}{10C_2},
\qquad
b=\frac G{10c}.
\]

则

\[
I_2=[a,10a),
\qquad
I_3=[b,10b).
\]

两个 half-open intervals 相交，当且仅当

\[
a<10b
\quad\text{且}\quad
b<10a.
\]

而

\[
\frac ab
=
\frac{GKc}{C_2}
=
\frac1\rho.
\]

故

\[
a<10b
\iff
\rho>\frac1{10},
\]

\[
b<10a
\iff
\rho<10.
\]

因此得到 exact iff：

\[
\boxed{
I_2\cap I_3\ne\varnothing
\iff
\rho\in\mathcal B_{10},
}
\]

其中

\[
\boxed{
\mathcal B_{10}:=\left(\frac1{10},10\right).
}
\tag{B10}
\]

两个端点都**不允许等号**。

- \(\rho=1/10\) 时，一个 interval 的 lower endpoint 恰等于另一个 interval 的 excluded upper endpoint；
- \(\rho=10\) 同理。

所以粗写成 \([1/10,10]\) 是错误的。

---

# 6. 更自然的 normalized radial plane

定义

\[
\boxed{
r_3:=\frac cG,
\qquad
r_2:=\frac{C_2}{G^2K}.
}
\]

则两个 digit windows 统一写成

\[
\boxed{
\frac1{10}\le Ur_i<1,
\qquad i=2,3.
}
\]

并且

\[
\boxed{
\rho=\frac{r_2}{r_3}.
}
\]

因此三个层级有一个极清楚的几何解释：

### Level I — absolute box

任何正整数 \(U\ge1\) 存在的必要条件是

\[
\boxed{r_2<1,\qquad r_3<1.}
\]

即

\[
\boxed{C_2<G^2K,\qquad c<G.}
\]

Absolute-Oversize Theorem 正是在说 deep root locus 根本进不了这个 open unit square。

### Level II — projective decade cone

放松 \(U\) 到 positive real 后，绝对半径消失，只剩

\[
\boxed{1/10<r_2/r_3<10.}
\]

### Level III — integer lattice in \(U\)

只有同时进入 unit square 与 decade cone 后，integer spacing 才有意义。

这解释了为什么 Level I 必须优先于 integer/gcd。

---

# 7. Pullback to projective root variables

由 R1 exact formula

\[
C_2=Ac+H\lambda
\]

直接得到

\[
\rho
=
\frac{A}{GK}
+
\frac{H\lambda}{GKc}.
\]

由于 \(H=G/2\)，令

\[
\boxed{t:=\frac\lambda c>0,}
\]

则

\[
\boxed{
\rho=f_{g,k,u}(t)
=
\frac{A}{GK}+\frac{t}{2K}.
}
\tag{7.1}
\]

这是本轮最重要的 projective exactization。

它是严格递增 affine function：

\[
\boxed{f'(t)=\frac1{2K}>0.}
\]

所以 decade band 等价于

\[
\boxed{
\frac K5-\frac{2A}{G}
<t<
20K-\frac{2A}{G}.
}
\tag{7.2}
\]

再令

\[
\boxed{s:=\frac zc.}
\]

将 ROOT 除以 \(c^2\)，得到 exact projective conic：

\[
\boxed{
\mathcal F_{g,k,u}(s,t)=0,
}
\]

其中

\[
\mathcal F(s,t)
=
H^2\left(\frac{Bs+At}{2K}\right)^2
+
(GHs-uA)^2
-
(Gs+ut)\bigl(u+G(GHs-uA)\bigr).
\tag{7.3}
\]

因此 R2 的 real shape problem 被精确压成：

\[
\boxed{
\mathcal F(s,t)=0
\quad\text{且}\quad
t\in
\left(
\frac K5-\frac{2A}{G},
20K-\frac{2A}{G}
\right).
}
\]

---

# 8. Root-Branch Differential：预期 separation 结构被消灭

对固定 \(t\)，\(\mathcal F(s,t)=0\) 至多给两个 \(s\)-branches：

\[
s=s_+(t),
\qquad
s=s_-(t).
\]

但由 (7.1)，\(\rho\) **完全不依赖 \(s\)**。

所以严格有

\[
\boxed{
\rho_+(t)=\rho_-(t)=f(t).
}
\]

因此不可能出现

\[
\rho_+(t)>10,
\qquad
\rho_-(t)<1/10
\]

这种“同一个 \(t\) 下两个 root branch 分居 decade band 两侧”的机制。

Root branch 仍会决定：

- positivity；
- orientation；
- \(h,m,r,w,d_2\) 的符号；

但 **radial ratio 本身不是 branch discriminator**。

这永久退休了一个过强的 Root-Branch Radial Separation 设想。

---

# 9. Counterexample Guillotine — new R2 deep ratio-band witness

固定首个 live audited outer base：

\[
(g,k,u,q)=(4,1,73,137),
\]

\[
G=10000,
\quad K=10,
\quad H=5000,
\quad A=147,
\quad B=20137.
\]

本轮使用 R1 已知 isotropic point

\[
p_0=
(44166648285459361797000000,
9530621959721527629285,
84945551173868016406925)
\]

以及 source-lattice compatible chord direction

\[
y=(9,75934,2036559106).
\]

对 R1 homogeneous conic polynomial \(\Phi\)，取 chord formula

\[
P(y)
=
\Phi(y)p_0-\mathcal B_\Phi(p_0,y)y.
\]

本例 exact values 为

\[
\Phi(y)=3674070508576600000,
\]

\[
\mathcal B_\Phi(p_0,y)
=-242348320413237174913057803567880000,
\]

raw vector 的 common gcd 为

\[
2920000.
\]

primitive reduction 后得到：

\[
\boxed{
c=
55572391133361773812119871611530969901,
}
\]

\[
\boxed{
z=
18294059737282238636057102641763401,
}
\]

\[
\boxed{
\lambda=
169133142022529638483244734153511450709.
}
\]

重构：

\[
C_1=
1261547967912075464822562889823168643008,
\]

\[
C_2=
853834851609252373166605291894452306120447,
\]

\[
T=
12529659965017485995637436619623969911757,
\]

\[
h=
4362289423434152715317494182712877109553,
\]

\[
m=
641073604647447626765311073832375301094291,
\]

\[
r=
21807390332618028167099186162936743786962227,
\]

\[
w=
318355657612006737024996789824831211992369,
\]

\[
d_2=
3183560632904620105659456182998939761684492773.
\]

Exact root：

\[
\boxed{H^2C_1^2+w^2-Td_2=0.}
\]

对应 square witness：

\[
\boxed{
Z=
9248758080226018624366062426043674948098881102840,
}
\]

且

\[
\boxed{Q_{4,1,73}(c,z)=Z^2.}
\]

full primitive blocks 为

\[
P_1=
63077398395603773241128144491158432150400000000,
\]

\[
P_2=
623299441674754232411621863082950183467926310000,
\]

\[
P_3=
4056784552735409488284750627641760802773,
\]

\[
Q_0=
626483002307658852517281319265949123229610802773,
\]

并且

\[
\boxed{\gcd(P_1,P_2,P_3,Q_0)=1.}
\]

common-\(V\) profile 亦全部通过。

---

# 10. R2-CM1 Radial Compatibility Ledger

```text
EXACT_ROOT = PASS
SQUARE = PASS
PRIMITIVE = PASS
COMMON_V = PASS
TEN_UNIT = PASS
REGULAR = PASS
SOURCE_LATTICE = PASS
SOURCE_MASTER = PASS

c < G = FAIL
C2 < G^2 K = FAIL

REAL_INTERVAL_OVERLAP = PASS
INTEGER_U_EXISTS = NOT_REACHED_BY_TREE
COPRIME_U_EXISTS = NOT_REACHED_BY_TREE

FULL_COMMON_U = FAIL
FULL_SOURCE_LIFT = FAIL_AT_ABSOLUTE_RADIAL_SCALE
```

该点的 exact ratio：

\[
\boxed{
\rho=
\frac{
284611617203084124388868430631484102040149
}{
1852413037778725793737329053717698996700000
}
}
\]

数值仅作阅读辅助：

\[
\rho\approx0.1536437130.
\]

因此严格有

\[
\boxed{\frac1{10}<\rho<10,}
\]

从而

\[
\boxed{I_2\cap I_3\ne\varnothing.}
\]

但是

\[
c\gg G,
\qquad
C_2\gg G^2K.
\]

故两个 interval 的 upper endpoint 已经都落在 \(1\) 以下；positive integer \(U\) 在 Level I 就被消灭。

这里没有进入 Level III integer-spacing analysis；“无整数”只是 Absolute-Oversize 的直接后果。

---

# 11. 对 R1 countermodel 的严格推进

R1 deepest countermodel 的 ratio 为

\[
\rho_{R1}
=
\frac{
5313085891038522492492041303577054753071485488943
}{
3392423925490388301846351077248660911837814546900000
}
\approx0.00156616,
\]

所以它不仅 oversize，而且

\[
\rho_{R1}<1/10.
\]

R2-CM1 修复了后一项：

\[
\boxed{
\text{R1: oversize + no real overlap}
}
\]

推进为

\[
\boxed{
\text{R2: oversize + real overlap + all deep arithmetic gates}.
}
\]

因此 failure differential 进一步收缩为：

\[
\boxed{
\textbf{projective shape 可以合法；
absolute primitive height 仍然失败。}
}
\]

这就是本轮最重要的新信息。

---

# 12. Real Radial Incompatibility 的判决

若把 Task E 的 theorem 按其原始强形式写成

\[
\boxed{
\text{exact root}
+
\text{R1 surviving deep gates}
\Longrightarrow
\rho\notin\mathcal B_{10},
}
\]

那么 R2-CM1 是 exact counterexample。

故：

```text
UNCONDITIONAL_ROOT_RATIO_SEPARATION = FALSE
REAL_RADIAL_INCOMPATIBILITY = FALSE
```

但必须保留攻击树 scope firewall：

本轮**没有**找到同时满足

\[
c<G,
\qquad
C_2<G^2K
\]

的 exact-root countermodel。

所以严格的 ladder K2：

\[
\text{K1 bypass}
+
\text{real overlap}
\]

尚未达到。

因此：

```text
LEVEL_II_AFTER_OVERSIZE_BYPASS = NOT_REACHED
K2_STRICT_LADDER_COUNTERMODEL = NOT_FOUND
```

这不是矛盾：我们杀掉的是“ratio 本身 universal incompatible”这个过强 theorem，而不是证明 Level-I bypass 已经存在。

---

# 13. Absolute-Oversize Guillotine — global OPEN, first live base exactly cleared

全局候选仍是

\[
\boxed{
\text{deep exact-root state}
\Longrightarrow
c\ge G
\ \lor\ 
C_2\ge G^2K.
}
\tag{AO}
\]

R2 没有得到 global proof，也没有得到 global counterexample。

所以：

```text
ABSOLUTE_OVERSIZE_THEOREM = OPEN
```

但本轮对第一 live audited base 完成了完整 exact Level-I box audit。

## 13.1 outer base coverage

\[
G=10000,
\qquad
G+1=10001=73\cdot137.
\]

central regular \(u,q>1\) 中：

- \(u=73,q=137\) 合法；
- \(u=137,q=73\) 给 \(A=275\)，违反 inherited \(\gcd(A,10)=1\)；
- \(u=1\) 或 \(q=1\) 不属于当前 central live scope。

又由

\[
\ell=2g-k\ge6
\]

可知

\[
k\in\{1,2\}.
\]

所以这里只需审计 \((k,u)=(1,73),(2,73)\)。

## 13.2 k=1 exact finite reduction

假设

\[
1\le c<G,
\qquad
C_2=147c+5000\lambda<G^2K=10^9.
\]

则

\[
1\le\lambda\le199999.
\]

ROOT 展开为

\[
0=
115154361c^2
+7833624671c\lambda
-730000cz
+1350562500\lambda^2
-36129982625000\lambda z
-2474656326937500z^2.
\tag{F1}
\]

记右侧为 \(F_1\)。

对固定 \(z\)，\(-F_1\) 关于 \(c\) 与 \(\lambda\) 分别为严格凹二次函数；故在 rectangle

\[
1\le c\le9999,
\qquad
1\le\lambda\le199999
\]

上的最小值出现在四个 corners。

Exact corner check 给

\[
\min_{\rm corners}\{-F_1(c,10,\lambda)\}
=
236235542621117810>0.
\]

而 \(-F_1\) 对 \(z>0\) 严格递增，所以任何 positive root 必有

\[
\boxed{1\le z\le9.}
\]

随后 exact enumeration 覆盖

\[
9999\times9=89991
\]

个 \((c,z)\) cells，对 \(\lambda\)-quadratic 判别式逐一作 integer-square test：

```text
square_discriminants = 0
level1_countermodels = 0
```

## 13.3 k=2 exact finite reduction

同理

\[
1\le\lambda\le1999999.
\]

ROOT 展开为

\[
0=
115154361c^2
+7833624671c\lambda
-730000cz
+13505625\lambda^2
-36496299826250\lambda z
-2499746563269375z^2.
\tag{F2}
\]

exact corner margin：

\[
\min_{\rm corners}\{-F_2(c,3,\lambda)\}
=
11015768312187810>0.
\]

故

\[
\boxed{1\le z\le2.}
\]

完整覆盖

\[
9999\times2=19998
\]

个 cells，同样得到

```text
square_discriminants = 0
level1_countermodels = 0
```

所以得到严格 fixed-base theorem：

\[
\boxed{
(g,u,q)=(4,73,137),\quad k\in\{1,2\}
\Longrightarrow
\text{no exact root with }c<G,\ C_2<G^2K.
}
\tag{AO-g4}
\]

这是 theorem，不是 sampling；但它不能被偷升格为 all-\(g\) closure。

---

# 14. Absolute Scale vs Projective Shape

这是 R2 的结构核心。

对任何正整数 \(d\)：

\[
(c,z,\lambda)
\mapsto
(dc,dz,d\lambda).
\]

于是

\[
C_1,C_2,T,h,m,r,w,d_2
\]

全部乘以 \(d\)。

ROOT 是 homogeneous degree two，所以仍成立：

\[
\boxed{
\text{root/projective shape 不读取 absolute scale}.
}
\]

同时

\[
s=z/c,
\qquad
t=\lambda/c,
\qquad
\rho=C_2/(GKc)
\]

全部保持不变。

但 normalized absolute radii

\[
r_3=c/G,
\qquad
r_2=C_2/(G^2K)
\]

都乘以 \(d\)。

更关键地，primitive blocks

\[
(P_1,P_2,P_3,Q_0)
\]

也全部乘以 \(d\)。

所以若一个 integral source ray 已经取到 full primitive representative，继续乘 \(d>1\) 会立刻破坏

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

换句话说：

\[
\boxed{
\textbf{projective conic 给 ray，
primitive source lattice 选择该 ray 的最小 integral representative。}
}
\]

decimal shell 检查的正是这个最小代表的绝对高度。

因此 R1 大量 square/root solutions 与 common-\(U\) 全灭之间不存在矛盾：

\[
\boxed{
\text{square/root abundance = ray abundance,}
}
\]

\[
\boxed{
\text{common-}U\text{ = primitive ray height requirement.}
}
\]

这就是本轮得到的 **Scale-Fixing Obstruction** 的正确形式。

---

# 15. 为什么 \(\rho\) 不能成为最终 closure variable

R2-CM1 已证明：

\[
\rho\in\mathcal B_{10}
\]

可以与：

- exact root；
- square；
- source lattice；
- common-\(V\)；
- full primitive；
- regularity；
- ten-unit；

全部共存。

所以 \(\rho\) 只能控制 **relative radial shape**，不能控制 **absolute primitive height**。

真正需要的第二无量纲量是

\[
\boxed{
\mathfrak H_{\rm rad}
:=
\max\left(
\frac cG,
\frac{C_2}{G^2K}
\right).
}
\tag{HRAD}
\]

Level I exactly asks：

\[
\boxed{
\mathfrak H_{\rm rad}\ge1
\quad ?
}
\]

而 R2-CM1 的信息是：

\[
\boxed{
\rho\in\mathcal B_{10}
\quad\text{但}\quad
\mathfrak H_{\rm rad}\gg1.
}
\]

这把下一轮变量从 “ratio” 精确切换成了 “primitive radial height”。

---

# 16. Countermodel Ladder verdict

## K1 — Level-I countermodel

要求

\[
c<G,
\qquad
C_2<G^2K.
\]

```text
FOUND = NO
GLOBAL STATUS = OPEN
FIRST LIVE BASE g=4 = EXACTLY EXCLUDED
```

## K2 — strict ladder Level-II countermodel

要求进一步 real overlap。

因为 K1 尚无 countermodel：

```text
K2_STRICT_LADDER_COUNTERMODEL = NOT_FOUND
```

但 raw/unconditional ratio theorem 已由 R2-CM1 exact falsified。

## K3 — integer countermodel

```text
NOT_REACHED
```

## K4 — full common-U countermodel

```text
NOT_FOUND
```

没有进入 coprime repair。

---

# 17. Information-Difference Audit

当前最强 countermodel failure set 已从 R1 的

\[
\boxed{
\text{absolute oversize}
+
\text{ratio incompatibility}
}
\]

压缩到 R2 的

\[
\boxed{
\textbf{absolute primitive scale only}.
}
\]

因此本轮回答核心问题：

> 在 square-conditioned exact-root state 上，两个 absolute decimal radial windows 第一次在哪里变得不可同时实现？

当前最强证据指向：

\[
\boxed{
\textbf{OVERSIZE / primitive height level}.
}
\]

但 global theorem 尚未完成，所以不能宣布 \(J=2\) closed。

---

# 18. R3 唯一中央 theorem

全局 Absolute-Oversize

\[
\text{all deep roots}\Longrightarrow\mathfrak H_{\rm rad}\ge1
\]

仍可能比真正需要的 theorem 过强。

因为若

\[
\rho\notin\mathcal B_{10},
\]

real overlap 已经自动死亡，不必再控制其 absolute height。

所以 R3 应只证明更小、更精确的：

## Band-Conditioned Primitive Height Guillotine

\[
\boxed{
\begin{gathered}
\text{exact root}
+
\text{square/source reconstruction}
+
\text{ten-unit}
+
\text{regular}
+
\text{common-}V
+
\text{full primitive}
\\
+
\rho\in\left(\frac1{10},10\right)
\\[1mm]
\Longrightarrow
\max\left(
\frac cG,
\frac{C_2}{G^2K}
\right)
\ge1.
\end{gathered}
}
\tag{BCPHG}
\]

等价地，以 projective coordinate \(t=\lambda/c\) 写：

\[
\boxed{
\mathcal F(s,t)=0,
\quad
\frac K5-\frac{2A}{G}
<t<
20K-\frac{2A}{G},
}
\]

且取该 source-lattice rational ray 的 full primitive integral representative，则证明其 primitive radial height \(\mathfrak H_{\rm rad}\ge1\)。

若 BCPHG 成立，则：

- band 外：Level II real overlap 为空；
- band 内：Level I absolute oversize 杀掉 positive integer \(U\)。

因此不需要进入 generic integer-spacing 或 gcd campaign，就能关闭当前 square-conditioned common-\(U\) interface。

这比 global AO 更弱，也更贴近 R2-CM1 暴露出的真实信息差。

---

# 19. R3 推荐攻击坐标

R3 不应回到 discriminant/class/descent。

应直接使用 rational-conic height parameter。

在 fixed outer fibre 上：

1. 选 R1/R2 source-lattice isotropic basepoint；
2. 用 rational chord slope \(m=a/b\) parameterize primitive rays；
3. 把 decade-band 条件翻译成一个 exact interval
   \[
   m\in\mathscr M_{10}(g,k,u);
   \]
4. 把 source lattice congruence翻译成 \((a,b)\) 的 fixed linear congruence；
5. 证明任何落入 \(\mathscr M_{10}\) 的 reduced rational parameter，其 denominator / source height 已大到迫使
   \[
   c\ge G
   \quad\text{或}\quad
   C_2\ge G^2K.
   \]

在首个 live base，R2 的 exact box audit已经证明 BCPHG；下一轮真正任务是 moving-\(g\) uniformization。

这是一条 **height / lattice-spacing interface**，不是 class-group 或 descent interface。

---

# 20. Proof-status ledger

## PROVED

1. exact common-\(U\) window endpoints；
2. \(I_2,I_3\) exact half-open form；
3. exact decade band
   \[
   \mathcal B_{10}=(1/10,10);
   \]
4. exact projective formula
   \[
   \rho=A/(GK)+t/(2K);
   \]
5. exact band in \(t\)；
6. root branch cannot separate \(\rho\) at fixed \(t\)；
7. R2-CM1 exact root/square/common-V/full-primitive ratio-band countermodel；
8. raw Real Radial Incompatibility theorem is FALSE；
9. exact Scale-Fixing decomposition: projective shape vs primitive radial height；
10. first live base \(g=4\), \(k=1,2\) Level-I box contains no exact root.

## OPEN

1. global Absolute-Oversize Theorem；
2. existence/nonexistence of any K1 countermodel at larger moving bases；
3. Band-Conditioned Primitive Height Guillotine uniformly in \(g,k,u\)；
4. full \(J=2\) closure.

## NOT REACHED

1. ordered Level-II theorem after an actual Level-I bypass；
2. integer interval extinction；
3. coprime radial extinction.

## RETIRED / FALSIFIED

1. ambient square nonrepresentation；
2. discriminant-alone moving obstruction；
3. universal root-branch radial separation；
4. universal raw theorem \(\rho\notin\mathcal B_{10}\) on deep exact-root states.

---

# 21. Terminal machine-readable block

```text
J2_STATUS = OPEN

ABSOLUTE_OVERSIZE_THEOREM = OPEN

REAL_RADIAL_INCOMPATIBILITY = FALSE

INTEGER_RADIAL_EXTINCTION = NOT_REACHED

COPRIME_RADIAL_EXTINCTION = NOT_REACHED

FULL_COMMON_U_COUNTERMODEL = NOT_FOUND

RADIAL_PRIMARY_FAILURE_LEVEL = OVERSIZE

MOVING_INFORMATION_ACTIVATED = YES

CLASS_INTERFACE = NOT_VISIBLE

DESCENT_INTERFACE = NOT_VISIBLE

R2_TERMINAL_VERDICT = NEXT_GATE_IDENTIFIED

RAW_RATIO_SEPARATION = FALSE
LEVEL_I_COUNTERMODEL = NOT_FOUND
LEVEL_I_G4_FIRST_LIVE_BASE = PROVED_EMPTY
LEVEL_II_AFTER_OVERSIZE_BYPASS = NOT_REACHED

R3_UNIQUE_CENTRAL_THEOREM =
BAND_CONDITIONED_PRIMITIVE_HEIGHT_GUILLOTINE
```

---

# 22. Artifact / certificate audit

本轮生成：

```text
85_phaseII_R2_radial_extinction.md
85_phaseII_R2_radial_certificate.py
85_phaseII_R2_radial_certificate.txt
```

certificate 使用 exact integer/rational arithmetic 验证：

- R2-CM1 chord construction；
- exact root；
- moving square witness；
- ten-unit；
- regularity；
- common-\(V\)；
- source master；
- full primitive gcd；
- \(1/10<\rho<10\)；
- real interval overlap；
- absolute oversize；
- \(g=4,k=1,2\) Level-I box complete exact audit。

没有使用 floating-point decision 作为任何 theorem 依据。

---

# 23. Final answer to the R2 central question

本轮最终问题是：

\[
\boxed{
\text{在 square-conditioned exact-root state 上，
两个 absolute decimal radial windows
第一次在哪一层无法同时实现？}
}
\]

R2 的最强可证回答是：

\[
\boxed{
\textbf{不是 projective ratio / real overlap。}
}
\]

因为存在 exact deep primitive root point 满足

\[
\boxed{1/10<\rho<10.}
\]

当前第一条仍未被穿透的 gate 是

\[
\boxed{
\textbf{primitive integral representative 的 absolute radial height。}
}
\]

即：

\[
\boxed{
\textbf{OVERSIZE remains the live guillotine.}
}
\]

但 global AO 尚未证明，因此 \(J=2\) 继续 OPEN。

R3 不应继续研究 ratio band 本身；它应直接攻击：

\[
\boxed{
\textbf{band-conditioned primitive ray height}.}
\]
