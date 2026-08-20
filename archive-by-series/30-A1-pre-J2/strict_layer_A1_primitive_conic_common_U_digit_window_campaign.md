# 三项十进制拼接平方和问题：A1 Primitive Conic × Common-\(U\) Digit Window Deep Intersection Campaign

**文件名：** `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`  
**研究范围：** Strict Layer 正向线，仅研究 `A1-only`；DD 保持 closed；不重做 backward same-cut norm/phase。  
**本轮最终等级：**

\[
\boxed{\textbf{LEVEL 6 ACHIEVED — COMMON-}U\textbf{ INTEGER-RADIAL REDUCTION}}
\]

A1 **尚未整体闭合**。但本轮把“primitive synchronized conic 与真实 numerator realization 之间”的缺口压缩到了一个比预期更小的终端对象：

\[
\boxed{
\textbf{coprime positive integer point in one common-scale digit interval}
}
\]

并证明了两个此前没有明确分开的事实：

1. **continuous/projective common-scale cone 并不会使 fixed conic 离散化**；它通常仍截出开放 conic arc；
2. **真正制造 fixed-profile finiteness 的不是 cone，而是正整数 radial condition \(U\in\mathbf Z_{>0}\)。**

更强地，本轮证明：

\[
\boxed{
\text{fixed }(g_2,g_3,n_2,n_3)
+\text{ common integer }U
\Longrightarrow Q_0\text{ absolutely bounded}.
}
\]

因此 prompt 中最核心的 fixed-profile infinite-crossing question 已得到否定答案：

> **一条 fixed-profile synchronized primitive conic 可以有无限 rational points，也可以穿过 real common-scale digit cone；但它不可能有 primitive height \(Q_0\to\infty\) 的 common-integer-\(U\) legal points。**

同时，本轮重新审计了 forward reconstruction，得到另一条重要校准：一旦保留的是**精确** GSYNC/master plane、精确 common-\(V\) gcd profile、合法 denominator words，并找到 coprime integer \(U\) 使 numerator blocks 合法，则已经可直接恢复完整 original exact candidate。也就是说，forward line 在语义上没有再缺一个独立 norm gate；backward same-cut norm feedback 仍然是很有价值的**消灭这些候选的证明机制**，但不是 common-\(U\) 之后还要补上的新语义数据。

---

# 1. Executive Summary

本轮最重要的新结果分为九组。

## 1.1 PROVED — Exact common-\(U\) interval admits a one-line canonical form

令

\[
C_i:=\frac{P_i}{g_i}>0,
\qquad
I_i:=\left[\frac{10^{n_i-1}}{C_i},\frac{10^{n_i}}{C_i}\right).
\]

定义

\[
L:=\max_i\frac{10^{n_i-1}}{C_i},
\qquad
R:=\min_i\frac{10^{n_i}}{C_i}.
\]

则 real common scale 存在当且仅当

\[
\boxed{L<R.}
\]

endpoint 必须严格：若 \(L=R\)，该点必为至少一个窗口的右端点，而右端点不属于窗口。

再定义 normalized decimal rays

\[
d_i:=\frac{C_i}{10^{n_i}},
\qquad
d_{\min}:=\min_i d_i,
\qquad d_{\max}:=\max_i d_i.
\]

则

\[
\boxed{
L=\frac1{10d_{\min}},
\qquad
R=\frac1{d_{\max}},
}
\]

所以

\[
\boxed{
I_{\rm num}\neq\varnothing
\iff
d_{\max}<10d_{\min}.
}
\tag{CU-1}
\]

这是本轮最干净的 common-scale canonical form。

---

## 1.2 PROVED — Projective digit cone is an open convex hexagon in log coordinates

对任意 \(i,j\)，(CU-1) 等价于

\[
\boxed{
10^{n_i-n_j-1}
<\frac{C_i}{C_j}
<10^{n_i-n_j+1}.
}
\tag{CU-PAIR}
\]

所有边界均严格。

定义

\[
r_i:=\log_{10}C_i-n_i,
\qquad
\eta_{ij}:=r_i-r_j
=\log_{10}\frac{C_i}{C_j}-(n_i-n_j).
\]

则

\[
\boxed{
I_{\rm num}\neq\varnothing
\iff
\max_i r_i-\min_i r_i<1
\iff
|\eta_{ij}|<1\quad\forall i,j.
}
\tag{CU-LOG}
\]

在 projective log-chart \((\eta_{12},\eta_{13})\) 中，digit cone 是

\[
|\eta_{12}|<1,
\qquad
|\eta_{13}|<1,
\qquad
|\eta_{13}-\eta_{12}|<1,
\]

即三个 open strips 的交：一个 open convex hexagon，而不是独立 rectangular box。

**状态：NEW PROVED — Type B achieved.**

---

## 1.3 PROVED — Complete digit-length ordering compatibility

由 (CU-PAIR)：

\[
\boxed{
n_i>n_j\Longrightarrow C_i>C_j,
}
\]

\[
\boxed{
n_i<n_j\Longrightarrow C_i<C_j.
}
\]

若 \(n_i=n_j\)，则仅有

\[
\boxed{0.1<C_i/C_j<10,}
\]

不强制 coordinate order。

这比“位数差至少 2 才强制大小”更强：相邻 digit lengths 已经严格强制 ordering，因为低位数窗口的右端点排除而高位数窗口的左端点包含。

第三轮 family 的

\[
n_2=2>1=n_3
\]

因此任何 common scale 都要求

\[
C_2>C_3,
\]

而该 family 全部满足 \(C_3>C_2\)，故整个 family 被一个统一 cone-separation theorem 杀掉。

**状态：NEW PROVED.**

---

## 1.4 PROVED — The multiplication-carry skeleton is much more discrete than the raw ratio cone

令

\[
u:=\ell(U),
\qquad
\lambda_i:=\ell(C_i).
\]

由 exact primitive recovery 已有

\[
\boxed{
n_i=u+\lambda_i-1+\varepsilon_i,
\qquad
\varepsilon_i\in\{0,1\}.
}
\tag{CU-CARRY}
\]

定义

\[
e_i:=n_i-\lambda_i.
\]

则

\[
\boxed{
e_i\in\{u-1,u\}.}
\]

所以任何 genuine common-\(U\) state 必满足

\[
\boxed{
\max_i e_i-\min_i e_i\le1,
\qquad e_i\ge0.
}
\tag{CU-GAP}
\]

等价地，common digit length \(u\) 必属于

\[
\boxed{
\bigcap_i\{e_i,e_i+1\}.
}
\]

这只是必要 carry skeleton，不是充分条件；mantissa alignment 仍由 (CU-1) 决定。

**状态：NEW PROVED / REPACKAGED FROM EXACT MULTIPLICATION CARRY.**

---

## 1.5 PROVED — In the minimal A1 frontier, the first numerator window can be existentially eliminated

完整 fixed SGR state 若已经固定 \(n_1\)，当然必须保留 \(I_1\)。

但是 A1 的 primitive master plane / GSYNC 只使用

\[
n_2+n_3,
\qquad n_3,
\]

A1 chamber 也只使用 \(s_2,s_3\)。\(n_1\) 不进入 concatenation shifts，也不进入 GSYNC。

因此在**全局最小 A1 frontier** 中，一旦找到 integer \(U>0\)，可以直接定义

\[
a_1:=UC_1,
\qquad
n_1:=\ell(a_1),
\]

第一块自动合法。

于是若不人为冻结完整 \(n_1\)-carry state，真正需要求解的 numerator scale gate 可压成

\[
\boxed{
U\in I_{23}
:=
\left[\frac{10^{n_2-1}}{C_2},\frac{10^{n_2}}{C_2}\right)
\cap
\left[\frac{10^{n_3-1}}{C_3},\frac{10^{n_3}}{C_3}\right),
}
\tag{CU-23}
\]

再加

\[
\boxed{U\in\mathbf Z_{>0},\qquad\gcd(U,V)=1.}
\]

其 continuous/projective 条件仅为单个 ratio strip：

\[
\boxed{
10^{n_2-n_3-1}
<\frac{C_2}{C_3}
<10^{n_2-n_3+1}.
}
\tag{CU-23-RATIO}
\]

这把本轮的三维 digit-cone picture 在 minimal A1 semantics 下进一步压成一维 ratio interval + 一个 radial integer interval。

**状态：NEW PROVED FRONTIER REDUCTION.**

---

## 1.6 PROVED — Integer \(U\), not the projective cone, is what forces fixed-profile finiteness

这是本轮最重要的新 theorem。

若 \(U\in\mathbf Z_{>0}\) 且第二、三 numerator blocks 合法，则

\[
C_2\le\frac{10^{n_2}-1}{U},
\qquad
C_3\le\frac{10^{n_3}-1}{U}.
\]

所以

\[
P_2=g_2C_2
\le
\frac{g_2(10^{n_2}-1)}U,
\]

\[
P_3=g_3C_3
\le
\frac{g_3(10^{n_3}-1)}U.
\]

sphere 给

\[
P_2^2+P_3^2
=Q_0^2-P_1^2
=(Q_0-P_1)(Q_0+P_1).
\]

因为 \(Q_0>P_1>0\) 且均为整数，

\[
Q_0-P_1\ge1,
\]

故

\[
\boxed{Q_0<P_2^2+P_3^2.}
\tag{RAD-1}
\]

从而

\[
\boxed{
Q_0
<
\frac{
 g_2^2(10^{n_2}-1)^2
+g_3^2(10^{n_3}-1)^2
}{U^2}.
}
\tag{RAD-2}
\]

特别地，因 \(U\ge1\)：

\[
\boxed{
Q_0
<
 g_2^2(10^{n_2}-1)^2
+g_3^2(10^{n_3}-1)^2.
}
\tag{RAD-3}
\]

于是：

\[
\boxed{
\text{fixed }(g_2,g_3,n_2,n_3)
\Longrightarrow
Q_0\text{ bounded}
\Longrightarrow
\text{only finitely many primitive lattice states}.
}
\tag{FPRT}
\]

该结论甚至不需要 GSYNC；sphere + integer common scale 已经足够。

因此 prompt 中：

\[
\text{“fixed profile synchronized conic 能否在 }Q_0\to\infty\text{ 时持续穿过 common-}U\text{ cone？”}
\]

的答案是：

\[
\boxed{\textbf{NO, once }U\textbf{ is required to be a positive integer.}}
\]

**状态：NEW PROVED — Type D achieved in the correct integer-radial sense.**

---

## 1.7 PROVED — Continuous common-scale cone is still insufficient

固定第三轮 profile：

\[
V=24,
\qquad(g_1,g_2,g_3)=(24,4,3),
\]

\[
(b_1,b_2,b_3)=(1,6,8),
\qquad
(m_2,n_3,k,g)=(1,1,1,0),
\]

故 \(n_2=2,m_3=1\)。

该 conic 可在 affine chart \(x=1\) 参数化。取 rational parameter

\[
t=-\frac{31}{29},
\]

得到 primitive integer point

\[
(x,y,z,q)=(324,17813,2633,72109).
\]

定义

\[
P_1=24x=7776,
\quad
P_2=4y=71252,
\quad
P_3=3z=7899,
\quad
Q_0=72109.
\]

直接有

\[
7776^2+71252^2+7899^2=72109^2,
\]

\[
\gcd(24,P_1)=24,
\quad
\gcd(24,P_2)=4,
\quad
\gcd(24,P_3)=3,
\]

并且

\[
\Delta_{12}=-1{,}504{,}576,
\qquad
\Delta_3=1{,}880{,}720,
\]

故

\[
24\Delta_3=-10\cdot3\Delta_{12}.
\]

若固定三位数 profile

\[
(n_1,n_2,n_3)=(1,2,1),
\]

则

\[
C_1=324,
\quad C_2=17813,
\quad C_3=2633,
\]

且

\[
I_{\rm num}
=
\left[\frac1{324},\frac{10}{2633}\right)
\ne\varnothing.
\]

所以这是一个**精确 common-\(V\) gcd profile + sphere + GSYNC + real three-window common-scale** survivor。

但

\[
\frac{10}{2633}<1,
\]

因此

\[
I_{\rm num}\cap\mathbf Z_{>0}=\varnothing.
\]

也就是说：

\[
\boxed{
\text{continuous conic}\cap\mathcal K_{\mathbf n}\ne\varnothing
\quad\not\Rightarrow\quad
\text{integer common-}U.
}
\]

**状态：NEW PROVED CONTINUOUS-SCALE INSUFFICIENCY CERTIFICATE.**

---

## 1.8 PROVED — The entire third-round fixed profile, not merely its polynomial subfamily, is killed by integer \(U\)

第三轮只证明了显式 polynomial family 满足 \(C_3>C_2\)，因此被 ordering gate 杀掉。

本轮更进一步：对整个 conic profile

\[
1000x+10y+z=7q,
\]

\[
576x^2+16y^2+9z^2=q^2,
\]

若存在 integer \(U\) 使

\[
10\le Uy\le99,
\qquad
1\le Uz\le9,
\]

则 \(U\ge1\) 给

\[
y\le99,
\qquad z\le9.
\]

又由 triangle inequality：

\[
q\le24x+4y+3z,
\]

与 linear equation 联立：

\[
1000x+10y+z
=7q
\le168x+28y+21z,
\]

所以

\[
832x\le18y+20z\le1962,
\]

即

\[
\boxed{x\le2.}
\]

把 \(q\) 消去，conic 等价于

\[
-242944x^2-5000xy-500xz+171y^2-5yz+110z^2=0.
\tag{REG-C}
\]

视为关于 \(y\) 的二次式，其判别式为

\[
49D_{x,z},
\]

其中

\[
\boxed{
D_{x,z}
=3{,}901{,}504x^2+8{,}000xz-1{,}535z^2.
}
\tag{REG-D}
\]

对仅剩的

\[
x\in\{1,2\},
\qquad z\in\{1,\dots,9\},
\]

逐格可用一个很小的 quadratic-nonresidue witness 排除 \(D_{x,z}\) 为平方；第 11 节给出完整 grouped table。

因此：

\[
\boxed{
\text{该 fixed profile 的整个 synchronized conic}
\cap
\text{integer common-}U
=\varnothing.
}
\]

这比第三轮“一个显式 infinite arc 被 ordering 杀掉”严格更强。

**状态：NEW PROVED — REGRESSION PROFILE COMPLETELY CLOSED AT COMMON-\(U\) LEVEL.**

---

## 1.9 PROVED — Coprime integer common-\(U\) is already terminal forward reconstruction

在 exact A1 profile 下，GSYNC 展开后就是 primitive master equation：

\[
\frac{P_1}{g_1}10^{n_2+n_3}
+\frac{P_2}{g_2}10^{n_3}
+\frac{P_3}{g_3}
=
Q_0\left(
\frac{10^{m_2+m_3}}{g_1}
+\frac{10^{m_3}}{g_2}
+\frac1{g_3}
\right).
\tag{MASTER/g}
\]

若再有 exact common-\(V\) profile

\[
g_i=\gcd(V,P_i),
\qquad b_i=V/g_i,
\]

以及一个

\[
U\in\mathbf Z_{>0},
\qquad\gcd(U,V)=1,
\]

使

\[
a_i=UP_i/g_i
\]

落入要求的 numerator digit windows，则：

1. \(\gcd(a_i,b_i)=1\) 自动成立；
2. (MASTER/g) 乘回 \(U,V\) 直接给 exact concatenation identity
   \[
   \frac{A}{B}=\frac{UQ_0}{V};
   \]
3. primitive sphere 给
   \[
   \sqrt{(a_1/b_1)^2+(a_2/b_2)^2+(a_3/b_3)^2}
   =\frac{UQ_0}{V}.
   \]

所以它已经是完整 original exact candidate。

因此本轮之后，forward line 的终端 obstruction 可以准确写成：

\[
\boxed{
I_{23}
\cap
\{U\in\mathbf Z_{>0}:\gcd(U,V)=1\}
=\varnothing
}
\]

对所有 synchronized A1 primitive states 成立。

这也意味着 backward same-cut norm feedback 的正确接口是：它可以作为证明上述集合为空的另一套坐标/机制；但不应再把 norm 当成 common-\(U\) 之后“尚未恢复”的独立 semantic gate。

**状态：NEW PROVED RECONSTRUCTION AUDIT.**

---

# 2. Frozen Previous Results

本轮冻结前三轮已经建立的结果，不重新攻击 private-prime / pure valuation / flat locus。

## 2.1 A1 chamber and exponent relations

\[
\boxed{s_3\le0,\qquad s_2+s_3>0.}
\]

令

\[
g=m_3-n_3\ge0,
\qquad
k=s_2+s_3\ge1,
\]

则

\[
\boxed{n_2=m_2+g+k,}
\qquad
\boxed{m_3=n_3+g.}
\]

## 2.2 Primitive normalization

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

\[
\gcd(U,V)=1,
\qquad
g_i=\gcd(V,P_i),
\qquad
C_i=P_i/g_i,
\]

\[
a_i=UC_i,
\qquad
b_i=V/g_i.
\]

Exact-Lift bridge：

\[
q=V,
\qquad y_i=UP_i,
\qquad H=UQ_0.
\]

## 2.3 Flat closure and GSYNC

flat locus 已闭合，故

\[
\Delta_{12}\ne0,
\qquad\Delta_3\ne0.
\]

定义

\[
D=P_1 10^k-Q_0>0,
\]

\[
\Delta_{12}
=g_2 10^{m_2}D-g_1Q_0,
\]

\[
\Delta_3
=g_3P_2 10^{n_3}-g_2(Q_0-P_3),
\]

则

\[
\boxed{
g_1\Delta_3=-10^{m_3}g_3\Delta_{12}.
}
\tag{GSYNC}
\]

## 2.4 Frozen height collapse

第三轮已严格得到

\[
\boxed{10^{2g+k-2}<Q_0,}
\]

从而

\[
\boxed{10^g<\sqrt{10Q_0}.}
\]

plus branch：

\[
P_3(1+10^{n_2-1})<Q_0,
\]

\[
10^{n_2-1}<Q_0-1,
\]

\[
10^{m_3}<\frac{Q_0(Q_0-1)}{10}.
\]

minus branch：

\[
\boxed{g\le m_2+2.}
\]

## 2.5 Primitive-only insufficiency

第三轮 fixed profile

\[
V=24,
\quad(g_1,g_2,g_3)=(24,4,3),
\quad(m_2,n_3,k,g)=(1,1,1,0)
\]

存在显式 infinite synchronized minus pseudo-family，且具有 exact common-\(V\) gcd profile 与合法 denominator digits。

因此：

\[
\boxed{
\text{sphere + GSYNC + common-}V\text{ + denominator digits}
\not\Rightarrow
\text{numerator common-}U.
}
\]

本轮接受这一结论，不再回 primitive-only closure。

---

# 3. Why Primitive Synchronization Is Insufficient

第三轮的负结果现在可以被更精确地重新解释。

固定 gcd/exponent profile 后，primitive master equation是一个 homogeneous plane：

\[
h_1 10^{n_2+n_3}P_1
+h_2 10^{n_3}P_2
+h_3P_3
=KQ_0,
\]

其中

\[
h_i=L_g/g_i,
\qquad
K=h_1 10^{m_2+m_3}+h_2 10^{m_3}+h_3.
\]

与 sphere

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

相交，通常得到 nondegenerate projective conic。

若含 rational point，则 rational slope parametrization 给无限 rational points。因此 primitive geometry 本身天然不会离散化。

真正 missing 的不是一个新的 prime congruence，而是：

- projective direction 必须落入 decimal ratio cone；
- 更重要的是 primitive integer representative 的 radial height 必须使对应 interval 真正含 \(U\in\mathbf Z_{>0}\)；
- 还必须 \(\gcd(U,V)=1\)。

本轮的核心结构因此是：

\[
\boxed{
\text{projective cone}
\times
\text{integer radial shell}
\times
\text{coprime sieve}.
}
\]

第三轮只看到了第一个显式 family 在 projective cone 外死亡；本轮证明，即使 conic 真正进入 projective cone，integer radial shell 仍可把它完全杀掉。

---

# 4. Exact Definition of \(C_i,U,V\) and Reducedness

定义

\[
C_i=P_i/g_i,
\qquad
g_i=\gcd(V,P_i),
\qquad
\gcd(U,V)=1.
\]

恢复

\[
a_i=UC_i,
\qquad
b_i=V/g_i.
\]

## 4.1 PROVED — \(\gcd(C_i,b_i)=1\)

对任意素数 \(p\)，设

\[
v_p(V)=e,
\qquad v_p(P_i)=f.
\]

则

\[
v_p(g_i)=\min(e,f).
\]

若 \(p\mid C_i=P_i/g_i\)，则

\[
f>\min(e,f),
\]

这强制 \(e\le f\)，故 \(v_p(g_i)=e\)，于是

\[
p\nmid V/g_i=b_i.
\]

所以

\[
\boxed{\gcd(C_i,b_i)=1.}
\]

再由 \(\gcd(U,V)=1\)：

\[
\boxed{\gcd(a_i,b_i)=\gcd(UC_i,b_i)=1.}
\]

因此在 exact primitive normalization 中，逐项 reducedness **不需要在 common-\(U\) 后作为额外独立 gate 再检查一次**；它已经由 \(g_i=\gcd(V,P_i)\) 与 \(\gcd(U,V)=1\) 自动恢复。

## 4.2 PROVED — \(\gcd(C_1,C_2,C_3)=1\)

若某素数 \(p\mid C_1,C_2,C_3\)，则 \(p\mid P_1,P_2,P_3\)，由 sphere 得 \(p\mid Q_0\)，违反 primitive gcd。

故

\[
\boxed{\gcd(C_1,C_2,C_3)=1.}
\]

于是 actual numerator triple 中

\[
\boxed{U=\gcd(a_1,a_2,a_3).}
\]

这说明 \(U\) 是真实 numerator common content，而不是一个虚构 auxiliary scale。

---

# 5. Common-\(U\) Interval Form

对 fixed full numerator digit vector \(\mathbf n=(n_1,n_2,n_3)\)，定义

\[
I_i=
\left[
\frac{10^{n_i-1}}{C_i},
\frac{10^{n_i}}{C_i}
\right).
\]

则

\[
I_{\rm num}=I_1\cap I_2\cap I_3=[L,R),
\]

其中

\[
L=\max_i\frac{10^{n_i-1}}{C_i},
\qquad
R=\min_i\frac{10^{n_i}}{C_i}.
\]

### Theorem A1-CU-1 — Continuous common-scale criterion

\[
\boxed{
\exists u>0:
10^{n_i-1}\le uC_i<10^{n_i}\ \forall i
\iff L<R.
}
\]

**PROVED.**

### Endpoint audit

若 \(L=R=u_0\)，则 \(u_0\) 是某个 lower endpoint，同时是某个 upper endpoint。upper endpoint 对应 strict inequality \(uC_j<10^{n_j}\)，故 \(u_0\notin I_j\)。因此 equality 不可保留。

---

# 6. Projective Digit Cone

定义

\[
d_i=C_i10^{-n_i}.
\]

则

\[
I_i=\left[\frac1{10d_i},\frac1{d_i}\right).
\]

故

\[
L=\frac1{10d_{\min}},
\qquad
R=\frac1{d_{\max}}.
\]

于是：

### Theorem A1-CU-2 — One-decade projective cone

\[
\boxed{
I_{\rm num}\ne\varnothing
\iff
\frac{d_{\max}}{d_{\min}}<10.
}
\]

即所有 normalized coordinates \(C_i/10^{n_i}\) 必须落在同一个 multiplicative decade 中。

这一定义显然对

\[
(C_1,C_2,C_3)\mapsto t(C_1,C_2,C_3)
\]

不变，所以 continuous feasibility 是纯 projective 条件。

定义

\[
\mathcal K_{\mathbf n}
:=
\left\{
[C_1:C_2:C_3]\in\mathbf P^2_{>0}
:
\frac{d_{\max}}{d_{\min}}<10
\right\}.
\]

这就是 canonical common-scale digit cone。

---

# 7. Pairwise Ratio Characterization

从 \(A_i<B_j\) 对所有 ordered pairs \((i,j)\) 得

\[
\frac{10^{n_i-1}}{C_i}
<
\frac{10^{n_j}}{C_j}.
\]

整理：

\[
\frac{C_i}{C_j}>10^{n_i-n_j-1}.
\]

交换 \(i,j\)：

\[
\frac{C_i}{C_j}<10^{n_i-n_j+1}.
\]

因此：

### Theorem A1-CU-3 — Exact pairwise ratio theorem

\[
\boxed{
I_{\rm num}\ne\varnothing
\iff
10^{n_i-n_j-1}
<\frac{C_i}{C_j}
<10^{n_i-n_j+1}
\quad\forall i\ne j.
}
\]

**PROVED.**

注意这是充分且必要，不是 crude necessary bound。

---

# 8. Ordering Compatibility

令 \(d=n_i-n_j\)。

| \(d\) | 强制结论 |
|---:|---|
| \(d\ge1\) | \(C_i/C_j>10^{d-1}\ge1\)，故 \(C_i>C_j\) |
| \(d=0\) | \(0.1<C_i/C_j<10\)，order 不固定 |
| \(d\le-1\) | \(C_i/C_j<10^{d+1}\le1\)，故 \(C_i<C_j\) |

因此：

\[
\boxed{
\operatorname{sgn}(n_i-n_j)\ne0
\Longrightarrow
\operatorname{sgn}(C_i-C_j)=\operatorname{sgn}(n_i-n_j).
}
\]

这给出一个完整的 digit-length ordering compatibility theorem。

特别第三轮 profile

\[
n_2-n_3=1
\]

要求

\[
\boxed{C_2>C_3.}
\]

所以任何 sector \(C_3\ge C_2\) 都与 digit cone 完全分离。

---

# 9. Logarithmic / Decimal-Phase Geometry

定义

\[
r_i=\log_{10}C_i-n_i.
\]

common scale \(u\) 在 log 中只是把三个 coordinate 同时加上 \(\log_{10}u\)。相对 quantity

\[
\eta_{ij}=r_i-r_j
\]

保持不变。

### Theorem A1-CU-4 — Decimal phase synchronization

\[
\boxed{
I_{\rm num}\ne\varnothing
\iff
\max_i r_i-\min_i r_i<1.
}
\]

等价于

\[
\boxed{|\eta_{ij}|<1\quad\forall i,j.}
\]

在 \((\eta_{12},\eta_{13})\) 中：

\[
|\eta_{12}|<1,
\quad
|\eta_{13}|<1,
\quad
|\eta_{13}-\eta_{12}|<1.
\]

所以 \(\mathcal K_{\mathbf n}\) 在 log-projective plane 中是 convex hexagon。

### Mantissa interpretation

令

\[
\mu_i:=\frac{uC_i}{10^{n_i-1}}\in[1,10).
\]

则

\[
\frac{\mu_i}{\mu_j}
=10^{n_j-n_i}\frac{C_i}{C_j}.
\]

所以 pairwise normalized mantissa ratios 正好是

\[
10^{\eta_{ij}},
\]

其范围必须在 \((0.1,10)\)。

---

# 10. Fixed-Profile Conic Parametrization

对第三轮 fixed profile：

\[
(g_1,g_2,g_3)=(24,4,3),
\quad
(m_2,n_3,k,g)=(1,1,1,0),
\]

写

\[
P_1=24x,
\quad P_2=4y,
\quad P_3=3z,
\quad Q_0=q.
\]

plane + sphere：

\[
1000x+10y+z=7q,
\tag{10.1}
\]

\[
576x^2+16y^2+9z^2=q^2.
\tag{10.2}
\]

在 affine chart \(x=1\) 中消去 \(q\)：

\[
\boxed{
171y^2-5yz-5000y+110z^2-500z-242944=0.
}
\tag{10.3}
\]

已知 rational point

\[
(y,z)=(13,53).
\]

过该点作 slope-\(t\) line

\[
z=53+t(y-13).
\]

第二交点给出：

\[
\boxed{
y(t)=
\frac{1430t^2-11160t+3042}
{110t^2-5t+171},
}
\tag{10.4}
\]

\[
\boxed{
z(t)=
\frac{-5265t^2+554t+9063}
{110t^2-5t+171},
}
\tag{10.5}
\]

\[
\boxed{
q(t)=
\frac{17005t^2-16578t+30069}
{110t^2-5t+171}.
}
\tag{10.6}
\]

因此 ratio

\[
\boxed{
\frac{C_2}{C_3}=\frac{y(t)}{z(t)}
=
-2\frac{715t^2-5580t+1521}
{5265t^2-554t-9063}.
}
\tag{10.7}
\]

其导数：

\[
\boxed{
\frac{d}{dt}\frac{y}{z}
=
-28\frac{
2070185t^2-2069730t+3672441
}{(5265t^2-554t-9063)^2}.
}
\tag{10.8}
\]

而 numerator quadratic 的 discriminant 为

\[
-26{,}126{,}746{,}813{,}440<0,
\]

leading coefficient positive，所以

\[
\boxed{y(t)/z(t)\text{ 在每个 pole-free interval 上严格递减}.}
\]

这是 prompt 希望的“conic ratio 在 slope parameter 上 monotone”的一个完整实例。

---

# 11. Explicit Third-Round Family Reanalysis and Whole-Profile Closure

## 11.1 Frozen polynomial family

第三轮 family：

\[
X_t=3{,}553{,}056t^2+160{,}341t+1{,}809,
\]

\[
Y_t=44{,}000{,}352t^2+2{,}018{,}892t+23{,}153,
\]

\[
Z_t=188{,}129{,}520t^2+8{,}492{,}928t+95{,}849,
\]

\[
Q_t=597{,}312{,}720t^2+27{,}003{,}264t+305{,}197.
\]

满足

\[
1000X_t+10Y_t+Z_t=7Q_t,
\]

\[
576X_t^2+16Y_t^2+9Z_t^2=Q_t^2.
\]

primitive reduction 后

\[
C_2=y_t,
\qquad C_3=z_t,
\]

且

\[
Z_t-Y_t
=12(1167t+26)(10292t+233)>0.
\]

所以

\[
C_3>C_2.
\]

而 \(n_2=2>1=n_3\) 要求 \(C_2>C_3\)。

因此整个 polynomial family 与 \(\mathcal K_{\mathbf n}\) 分离。

**PROVED.**

## 11.2 New stronger result: whole fixed conic has no integer common-\(U\) point

若 integer \(U\) 合法：

\[
10\le Uy\le99,
\qquad
1\le Uz\le9.
\]

所以

\[
y\le99,
\qquad z\le9.
\]

由 (10.1)-(10.2) 和 triangle inequality：

\[
832x\le18y+20z\le1962,
\]

所以

\[
x\in\{1,2\}.
\]

conic 的 \(y\)-discriminant为

\[
49D_{x,z},
\qquad
D_{x,z}=3{,}901{,}504x^2+8{,}000xz-1{,}535z^2.
\]

若 integer \(y\) 存在，\(D_{x,z}\) 必为 square。

剩余 18 个 \((x,z)\) 可按以下 nonresidue witnesses 一次性排除：

### \(x=1\)

| \(z\) | witness prime \(p\) | \(D_{1,z}\bmod p\) |
|---:|---:|---:|
| 1 | 11 | 10 |
| 2 | 11 | 6 |
| 3 | 7 | 5 |
| 4 | 11 | 6 |
| 5 | 7 | 6 |
| 6 | 11 | 2 |
| 7 | 7 | 5 |
| 8 | 13 | 11 |
| 9 | 17 | 12 |

### \(x=2\)

| \(z\) | witness prime \(p\) | \(D_{2,z}\bmod p\) |
|---:|---:|---:|
| 1 | 11 | 8 |
| 2 | 11 | 7 |
| 3 | 7 | 3 |
| 4 | 11 | 2 |
| 5 | 23 | 5 |
| 6 | 7 | 6 |
| 7 | 7 | 6 |
| 8 | 11 | 2 |
| 9 | 13 | 6 |

这些 residue 分别不在相应 prime 的 quadratic residue set 中。

因此整个 fixed profile：

\[
\boxed{
\mathcal C_{(24,4,3;1,1,1,0)}
\cap
\{\text{integer common-}U\text{ legal points}\}
=\varnothing.
}
\]

**状态：NEW PROVED.**

这是真正的 conic–integer-window separation，不再局限于第三轮构造的一个 arc。

---

# 12. Continuous Conic–Cone Intersection Is Not Finite

projective cone \(\mathcal K_{\mathbf n}\) 是 open set。

若 nondegenerate rational conic \(\mathcal C\) 含一个 rational point，则 rational parametrization

\[
t\mapsto \mathcal C(t)
\]

在 pole 外连续，且 \(\mathbf Q\) 在 \(\mathbf R\) 中稠密。

因此：

### Theorem A1-CU-RAT — Interior rational point implies infinitely many rational projective cone points

若

\[
\mathcal C(\mathbf Q)\cap\mathcal K_{\mathbf n}
\]

含一个非边界 rational point，则该交集含无限 rational projective points。

**PROVED.**

所以 prompt 中 Type D 若解释为

\[
\#(\mathcal C(\mathbf Q)\cap\mathcal K_{\mathbf n})<\infty
\]

则一般是错误目标。

真正可证的 finite theorem 必须保留：

\[
\boxed{U\in\mathbf Z_{>0}}
\]

所产生的 radial cap。

---

# 13. Exact Real-Cone Survivor on the Regression Conic

取

\[
t=-31/29.
\]

由 (10.4)-(10.6)：

\[
y=17813/324,
\qquad
z=2633/324,
\qquad
q=72109/324.
\]

清分母得到

\[
(x,y,z,q)=(324,17813,2633,72109).
\]

其 primitive coordinates：

\[
(P_1,P_2,P_3,Q_0)
=(7776,71252,7899,72109).
\]

直接核验：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

common \(V=24\) profile：

\[
\gcd(24,P_1)=24,
\quad
\gcd(24,P_2)=4,
\quad
\gcd(24,P_3)=3.
\]

GSYNC：

\[
D=5651>0,
\]

\[
\Delta_{12}=-1{,}504{,}576,
\qquad
\Delta_3=1{,}880{,}720,
\]

\[
24\Delta_3=-10\cdot3\Delta_{12}.
\]

选择

\[
(n_1,n_2,n_3)=(1,2,1),
\]

得到

\[
I_1=[1/324,10/324),
\]

\[
I_2=[10/17813,100/17813),
\]

\[
I_3=[1/2633,10/2633).
\]

故

\[
\boxed{
I_{\rm num}
=[1/324,10/2633)\ne\varnothing.
}
\]

但整个 interval 小于 1，所以无 positive integer \(U\)。

这一个点已经严格推翻：

\[
\text{“exact synchronized conic + exact gcd profile + real digit cone 自动产生 integer scale.”}
\]

**状态：PROVED COUNTEREXAMPLE.**

---

# 14. Integer-\(U\) Analysis

对

\[
I=[L,R)
\]

正整数数目精确为

\[
\boxed{
N_{\mathbf Z}(I)
=
\max\{0,\lceil R\rceil-\lceil L\rceil\}.
}
\tag{INT-COUNT}
\]

因此 integer feasibility 等价于

\[
\boxed{\lceil L\rceil<R.}
\]

prompt 中该判据是正确的。

## 14.1 Unique-\(U\) sufficient condition

若

\[
R-L\le1,
\]

则 interval 至多含一个 integer。

更精确地：

\[
\boxed{
N_{\mathbf Z}(I)\le1
\iff
\lceil R\rceil-\lceil L\rceil\le1.
}
\]

## 14.2 Interval width in canonical variables

\[
R-L
=
\frac1{d_{\max}}-\frac1{10d_{\min}}
=
\frac{10d_{\min}-d_{\max}}
{10d_{\min}d_{\max}}.
\tag{WIDTH}
\]

projective direction只决定 ratio \(d_{\max}/d_{\min}\)；绝对 width 还依赖 radial size。

若同一 projective direction按

\[
C\mapsto HC
\]

放大，而 digit exponents固定，则

\[
I\mapsto H^{-1}I.
\]

所以 width \(\asymp H^{-1}\)。这解释 fixed profile 中为什么 primitive height增大后 interval 先变成 unique，再直接落到 \((0,1)\) 而彻底无 integer。

反之，若 digit profile随 height一起移动，interval width 可以保持大甚至增长；因此不能从 \(Q_0\to\infty\) 单独推出 eventual unique-\(U\)。

**结论：** “integer \(U\) eventually unique” **不能由 common-scale geometry alone 证明**；moving-profile case 仍 OPEN。

---

# 15. Coprime-\(U\) and Reducedness

integer survivor 还需

\[
\gcd(U,V)=1.
\]

设

\[
\operatorname{rad}(V)=\prod_{p\mid V}p.
\]

由 Möbius inclusion-exclusion，\([L,R)\) 中与 \(V\) 互素的整数个数为

\[
\boxed{
N_V(L,R)
=
\sum_{d\mid\operatorname{rad}(V)}
\mu(d)
\left(
\left\lceil\frac Rd\right\rceil
-
\left\lceil\frac Ld\right\rceil
\right).
}
\tag{COPRIME-COUNT}
\]

所以 terminal forward gate 可以完全 elementary 地写为

\[
\boxed{N_V(L,R)>0.}
\]

一旦它成立，逐项 reducedness 自动成立（第 4 节）。

因此 reducedness 不再是一个神秘 downstream obstruction；它只是 common scale interval 上的 finite coprime sieve。

---

# 16. Common-\(U\) Sphere Height Relation

Exact-Lift bridge 给

\[
H=UQ_0,
\qquad
UP_i=g_i a_i.
\]

primitive sphere 乘 \(U^2\)：

\[
\boxed{
H^2
=(g_1a_1)^2+(g_2a_2)^2+(g_3a_3)^2.
}
\tag{H-SPHERE}
\]

若完整 \(\mathbf n\) fixed，digit windows 给

\[
10^{n_i-1}\le a_i<10^{n_i}.
\]

定义

\[
M_{\mathbf g,\mathbf n}
:=
\sqrt{
 g_1^2 10^{2n_1-2}
+g_2^2 10^{2n_2-2}
+g_3^2 10^{2n_3-2}
}.
\]

则

\[
\boxed{
M_{\mathbf g,\mathbf n}
\le UQ_0
<10M_{\mathbf g,\mathbf n}.
}
\tag{H-DECADE}
\]

这是一个 exact one-decade height shell。

所以用户要求的

\[
UQ_0\asymp10^{n_*}
\]

可以更精确地写成 (H-DECADE)：真正 controlling scale 是 weighted digit Euclidean norm，而不是单独某一个 \(n_i\)。

---

# 17. Fixed-Profile Radial Termination

再次强调 (RAD-2)：

\[
Q_0
<
\frac{
 g_2^2(10^{n_2}-1)^2
+g_3^2(10^{n_3}-1)^2
}{U^2}.
\]

因此：

### Theorem A1-CU-9 — Fixed-profile radial termination

对任何固定

\[
(g_2,g_3,n_2,n_3),
\]

common-integer-\(U\) legal primitive states 的 \(Q_0\) 有显式绝对上界。

特别：

\[
\boxed{
\#\{
\text{primitive common-}U\text{ legal states in fixed profile}
\}<\infty.
}
\]

**PROVED.**

### Corollary — no fixed-profile infinite A1 family survives common integer scale

任何 \(Q_0\to\infty\) A1 sequence若 genuine common-\(U\) legal，至少有

\[
\boxed{
\max\{g_2 10^{n_2},g_3 10^{n_3}\}\to\infty.
}
\]

更定量地由 \(Q_0<P_2^2+P_3^2\) 及

\[
P_i<g_i10^{n_i}/U
\]

得到

\[
\boxed{
\max\{g_2 10^{n_2},g_3 10^{n_3}\}
>U\sqrt{Q_0/2}.
}
\tag{ESCAPE}
\]

所以 common-\(U\) 把 top-level escape 从“conic point height”改写成“moving digit/gcd arm 必须至少平方根级增长”。

---

# 18. Plus Branch Analysis

plus branch：

\[
\Delta_{12}>0,
\qquad
\Delta_3<0.
\]

第三轮已经得到

\[
P_3(1+10^{n_2-1})<Q_0.
\tag{PLUS-COLLAPSE}
\]

本轮重新把它放回 digit cone，得到一个重要 route audit：

\[
\Delta_3<0
\]

等价推出

\[
P_3\frac{C_2}{C_3}10^{n_3}<Q_0-P_3.
\]

而 common real scale cone 给

\[
\frac{C_2}{C_3}>10^{n_2-n_3-1}.
\]

代入即得

\[
P_3 10^{n_2-1}<Q_0-P_3,
\]

也就是 (PLUS-COLLAPSE)。

所以：

\[
\boxed{
\text{A1-GPDS-4 正是 plus sign 与 common-scale cone lower boundary 的 projective consequence。}
}
\]

这意味着单纯“再画一次 continuous digit cone”不会在 plus branch 自动产生比第三轮更强的新不等式。

真正尚未使用的新信息是：

\[
\boxed{U\in\mathbf Z_{>0},\quad\gcd(U,V)=1,}
\]

即 radial + coprime 层。

## 18.1 New plus lower bound on \(UQ_0\)

由

\[
P_3(1+10^{n_2-1})<Q_0
\]

与

\[
P_3=g_3C_3,
\qquad
UC_3\ge10^{n_3-1},
\]

得到

\[
\boxed{
UQ_0
>
 g_3 10^{n_3-1}(1+10^{n_2-1}).
}
\tag{PLUS-H}
\]

这是一个 genuine integer-scale compatible lower bound，但由于 \(n_1\) 可自由随 \(a_1\) 移动，目前没有一个只由 \((n_2,n_3,g_i)\) 给出的匹配 upper bound 能制造 contradiction。

### Plus status

\[
\boxed{\textbf{OPEN.}}
\]

本轮没有证明 Type A。

但是 plus 的下一步已经明确不再是 projective cone，而是：

\[
\boxed{
\text{integer radial interval}
+\text{coprime sieve}
+\text{moving-profile growth}.
}
\]

---

# 19. Minus Branch Analysis

minus branch：

\[
\Delta_{12}<0,
\qquad
\Delta_3>0.
\]

第三轮已有 explicit infinite primitive synchronized family，所以 primitive geometry 不可关闭。

本轮新增两点：

1. 该 family 本身由 ordering theorem 统一杀掉；
2. 更强地，其**整个 fixed profile conic**在 integer common-\(U\) 层被第 11 节彻底杀掉。

此外第 13 节又证明同一个 conic 确实能进入 real projective digit cone，所以不能把 closure 错归因于“conic 与 cone 完全不相交”。

正确机制是：

\[
\boxed{
\text{real conic arc enters digit cone}
\quad\text{but}\quad
U\text{-interval lies below }1
}
\]

或在其他 arcs 上先被 ordering ratio 排除。

这正是“projective feasibility 与 integer radial feasibility”必须分层的原因。

### Minus status

整个 regression profile：

\[
\boxed{\textbf{CLOSED AT COMMON-}U\textbf{ LEVEL}.}
\]

general minus branch：

\[
\boxed{\textbf{OPEN}.}
\]

---

# 20. Boundary \(P_3/Q_0\to0\)

第三轮已证明：若

\[
g\to\infty,
\]

则

\[
P_3/P_2\to0.
\]

common-scale ratio theorem 给

\[
10^{n_3-n_2-1}
<\frac{C_3}{C_2}
<10^{n_3-n_2+1}.
\]

若 gcd ratio \(g_3/g_2\) 固定，则

\[
P_3/P_2\to0
\]

确实强制

\[
n_2-n_3\to\infty.
\]

但在 genuine moving A1 family 中 profile 本身可以移动，而且

\[
n_2-n_3
=(m_2-m_3)+(2g+k).
\]

所以 growing \(g\) 本身就能够提供 large positive digit gap；denominator gcd profile 也可移动。

因此 prompt 中的 strong Type F：

\[
g\to\infty
\Longrightarrow
P_3/P_2\to0
\Longrightarrow
I_{\rm num}=\varnothing
\]

**本轮没有证明，且 projective ratio geometry 本身不支持它。**

更准确的结论是：

\[
\boxed{
\text{fixed profile boundary escape 被 integer }U\text{ 终止；}
\quad
\text{moving profile boundary escape 仍 OPEN。}
}
\]

**状态：FAILED AS A PURE PROJECTIVE BOUNDARY CLOSURE PLAN / OPEN WITH MOVING PROFILE.**

---

# 21. Product and Volume Constraints

由 numerator windows 连乘：

\[
10^{n_1+n_2+n_3-3}
\le
U^3C_1C_2C_3
<
10^{n_1+n_2+n_3}.
\]

即

\[
\boxed{
U^3
\asymp_{10^3}
\frac{10^{n_1+n_2+n_3}}
{C_1C_2C_3}.
}
\]

又

\[
C_1C_2C_3
=\frac{P_1P_2P_3}{g_1g_2g_3}.
\]

sphere + AM-GM 给

\[
P_1P_2P_3
\le
\left(\frac{Q_0^2}{3}\right)^{3/2}
=\frac{Q_0^3}{3\sqrt3}.
\]

所以可导出一组 product lower bounds on \(UQ_0\)。

但这些 bounds 被第 16 节更直接的 exact weighted sphere shell

\[
H^2=\sum(g_i a_i)^2
\]

支配，未产生新的 branch closure。

**状态：PROVED BUT SUBSUMED / INSUFFICIENT.**

---

# 22. Profile Finiteness Audit

本轮需要明确区分三种“profile”。

## 22.1 Fixed primitive core

已有 SGR：fixed core \(\Rightarrow\) finite decimal fibre。

## 22.2 Fixed gcd/exponent profile

固定

\[
(g_i,m_2,n_3,k,g,\dots)
\]

通常给一个 projective conic，real/rational points 可以无限。

但一旦加入 integer \(U\)，只需要固定

\[
(g_2,g_3,n_2,n_3)
\]

就由 (FPRT) 得 primitive height finite。

## 22.3 Global moving profile

目前没有 global finite alphabet。

第三轮 square-root height：

\[
10^g<\sqrt{10Q_0}
\]

只给 \(g=O(\log Q_0)\)，并不把

\[
g_i,m_2,n_3,k
\]

压成 absolute finite list。

因此本轮之后真正的 remaining infinity 已经不是：

\[
\text{fixed conic rational parameter }t\to\infty,
\]

而是：

\[
\boxed{
Q_0\to\infty
\text{ together with a moving decimal/gcd profile}.
}
\]

这比第三轮 frontier 更精确。

---

# 23. Terminal Reconstruction Equivalence

这是本轮的 dependency audit 中最重要的一步。

GSYNC 展开：

\[
g_1(g_3P_2 10^{n_3}-g_2(Q_0-P_3))
=-10^{m_3}g_3(g_2 10^{m_2}(P_1 10^k-Q_0)-g_1Q_0).
\]

除以 \(g_1g_2g_3\)，利用

\[
n_2+n_3=m_2+m_3+k,
\]

得到

\[
\frac{P_1}{g_1}10^{n_2+n_3}
+\frac{P_2}{g_2}10^{n_3}
+\frac{P_3}{g_3}
=
Q_0\left(
\frac{10^{m_2+m_3}}{g_1}
+\frac{10^{m_3}}{g_2}
+\frac1{g_3}
\right).
\]

这就是 primitive master equation divided by common \(L_g\)。

现在令

\[
a_i=UP_i/g_i,
\qquad
b_i=V/g_i.
\]

左边乘 \(U\) 是 numerator concatenation coefficient，右边乘 \(V\) 是 denominator coefficient。

于是：

### Theorem A1-CU-13 — Forward terminal reconstruction

下列数据：

1. primitive sphere；
2. exact gcd profile \(g_i=\gcd(V,P_i)\)；
3. exact A1 exponent relations；
4. exact GSYNC；
5. denominator digit legality；
6. \(U\in\mathbf Z_{>0}\), \(\gcd(U,V)=1\)；
7. numerator digit legality；

足以双向恢复完整 original strict candidate。

**PROVED.**

因此 common-\(U\) 之后没有“还缺一个 norm equality”——norm 已由 primitive sphere 恢复。

### Interface to backward line

backward same-cut norm-excess feedback 仍然非常有价值，因为它可以在另一套 coordinates 中证明：

\[
\boxed{
\text{上述 terminal integer scale survivor 不可能存在。}
}
\]

但它是 elimination mechanism，不是额外 semantic gate。

这可以防止正反两线重复建模。

---

# 24. Computational Experiments

本轮计算只服务于 structural discovery，不作为 global closure。

## 24.1 Small primitive scan

枚举：

\[
Q_0\le250,
\qquad
1\le V\le60,
\qquad
1\le k\le4,
\]

所有 positive primitive sphere triples；对由 \(V\) 导出的 exact \(g_i,b_i,m_i\)，枚举 A1 的

\[
1\le n_3\le m_3,
\qquad
n_2=m_2+(m_3-n_3)+k,
\]

并精确检查 primitive master equation。

结果：在该盒中只出现一个 synchronized state：

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),
\]

\[
V=24,
\quad(g_1,g_2,g_3)=(24,4,3),
\]

\[
(n_2,n_3,k,g)=(2,1,1,0),
\]

且为 minus：

\[
\Delta_{12}=-1216,
\qquad
\Delta_3=1520.
\]

它的 pair common-real-scale interval已为空，因为

\[
C_2=13<C_3=53
\]

而 \(n_2>n_3\)。

**状态：EXPERIMENTAL, FINITE BOX ONLY.**

## 24.2 Symbolic conic experiment

第三轮 conic 的 rational parametrization由 symbolic elimination 得到 (10.4)-(10.6)，随后全部 identity 可直接人工展开验证。

## 24.3 Exact real-cone gcd-profile examples

在 real-cone arc 内搜索 rational slopes，可找到多个清分母后仍满足 exact \(V=24\) gcd profile 的 primitive states，例如：

\[
t=-23/21:
(x,y,z,q)=(8501,468017,59001,1891453),
\]

\[
t=-31/29:
(x,y,z,q)=(324,17813,2633,72109),
\]

\[
t=-37/31:
(x,y,z,q)=(409,22553,1105,90805).
\]

它们都处于 minus GSYNC sector，并且 real common-scale interval非空但位于 \((0,1)\)。

这进一步支持：projective cone intersection 本身不是稀薄现象；integer radial gate 才是 decisive separation。

前述每个具体点都可直接 exact arithmetic 核验；“该 arc 上有无穷 exact gcd-profile points”本轮未提升为 theorem。

**状态：EXPERIMENTAL PATTERN + INDIVIDUALLY VERIFIED EXAMPLES.**

---

# 25. Counterexamples / Failed Conjectures / Status Ledger

## 25.1 “continuous common-\(U\) cone closes A1”

\[
\boxed{\textbf{FALSE}.}
\]

第 13 节给出 exact sphere + GSYNC + exact common-\(V\) profile + real three-window scale survivor。

失败点正是：

\[
I_{\rm num}\subset(0,1).
\]

---

## 25.2 “fixed profile gives finite projective conic-cone rational points”

\[
\boxed{\textbf{FALSE IN THE CONTINUOUS/PROJECTIVE SENSE}.}
\]

若有一个 rational interior point，则 rational parametrization 给 infinitely many rational points in the same open cone arc。

---

## 25.3 “fixed profile gives finite integer-common-\(U\) primitive states”

\[
\boxed{\textbf{TRUE — PROVED}.}
\]

由 Fixed-Profile Radial Termination (FPRT)。

---

## 25.4 “integer \(U\) eventually unique”

\[
\boxed{\textbf{NOT PROVED GLOBALLY}.}
\]

fixed profile 下 interval随 radial height缩小并最终无 integer；但 moving profile 可以同步移动 digit exponents，所以不能从 \(Q_0\) 单独推出 \(|I\cap\mathbf Z|\le1\)。

作为 common-scale geometry alone 的 universal theorem，该路线 **FAILED / INSUFFICIENT**。

---

## 25.5 “\(P_3/Q_0\to0\) incompatible with common-\(U\)”

\[
\boxed{\textbf{NOT ESTABLISHED}.}
\]

fixed profile 已由更强 radial theorem终止；moving profile 中 \(n_2-n_3\) 可随 \(g\) 增长以匹配 ratio collapse。

作为 pure projective Type F route：**FAILED / INSUFFICIENT**。

---

## 25.6 “digit-length ordering alone kills all minus”

\[
\boxed{\textbf{FALSE AS A GENERAL PLAN}.}
\]

ordering kills third-round explicit arc，但同一 conic 的 \(t=-31/29\) point满足正确 ordering并进入 real digit cone。

真正 decisive 的是 integer radial scale。

---

## 25.7 “plus has no real common-scale state”

本轮没有得到 global theorem，也没有构造 plus exact common-real-scale state。

\[
\boxed{\textbf{OPEN}.}
\]

第三轮 finite scan 的“0 plus hits”仍仅是实验信号。

---

## 25.8 “common integer \(U\) + exact GSYNC 之后还缺一个 independent norm gate”

\[
\boxed{\textbf{FALSE AS A SEMANTIC CLAIM}.}
\]

若 exact primitive sphere、exact common-\(V\) profile 与 GSYNC/master 全部保留，则 coprime integer \(U\) + digit legality 已恢复 full original candidate。

backward norm machinery仍可作为 contradiction mechanism，但不是新增语义。

---

# 26. New Proven Lemmas

本轮可冻结以下 theorem ledger。

### A1-CU-1 — Continuous Common-Scale Interval

\[
I_{\rm num}=[L,R),
\qquad
I_{\rm num}\ne\varnothing\iff L<R.
\]

**PROVED.**

### A1-CU-2 — One-Decade Projective Cone

\[
I_{\rm num}\ne\varnothing
\iff
\max_i(C_i10^{-n_i})
<10\min_i(C_i10^{-n_i}).
\]

**PROVED.**

### A1-CU-3 — Pairwise Ratio / Log-Hexagon Theorem

\[
10^{n_i-n_j-1}<C_i/C_j<10^{n_i-n_j+1}
\]

for all pairs; equivalently \(|\eta_{ij}|<1\)。

**PROVED.**

### A1-CU-4 — Ordering Compatibility

\[
n_i>n_j\Rightarrow C_i>C_j,
\qquad
n_i<n_j\Rightarrow C_i<C_j.
\]

**PROVED.**

### A1-CU-5 — Multiplication Carry Skeleton

\[
n_i-\ell(C_i)\in\{\ell(U)-1,\ell(U)\}.
\]

**PROVED.**

### A1-CU-6 — Minimal A1 First-Block Elimination

若 \(n_1\) 未被完整 state 预先冻结，global A1 scale legality只需显式检查 block 2,3 common interval；block 1 digit length由 \(UC_1\) 派生。

**PROVED.**

### A1-CU-7 — Exact Integer Count

\[
\#([L,R)\cap\mathbf Z)=\max(0,\lceil R\rceil-\lceil L\rceil).
\]

**PROVED.**

### A1-CU-8 — Coprime Count

(COPRIME-COUNT)。

**PROVED.**

### A1-CU-9 — Fixed-Profile Radial Termination

\[
Q_0<
\frac{g_2^2(10^{n_2}-1)^2+g_3^2(10^{n_3}-1)^2}{U^2}.
\]

**PROVED.**

### A1-CU-10 — Continuous Scale Insufficiency

第三轮 fixed conic 存在 exact common-\(V\) gcd-profile rational/primitive point落入 real three-window cone，但 interval整体在 \((0,1)\)。

**PROVED.**

### A1-CU-11 — Regression Whole-Conic Integer-Scale Closure

第三轮整个 fixed profile conic 无 positive integer common-\(U\) legal point。

**PROVED.**

### A1-CU-12 — Weighted Common-Scale Height Shell

\[
M_{\mathbf g,\mathbf n}
\le UQ_0<10M_{\mathbf g,\mathbf n}.
\]

**PROVED.**

### A1-CU-13 — Forward Terminal Reconstruction

exact sphere + exact GSYNC/master + exact common-\(V\) profile + legal denominator digits + coprime integer common-\(U\) numerator realization \(\Longleftrightarrow\) complete original exact candidate。

**PROVED.**

---

# 27. Branch Status

## Plus

\[
\boxed{\textbf{OPEN}.}
\]

已知：

\[
P_3(1+10^{n_2-1})<Q_0,
\]

\[
10^{n_2-1}<Q_0-1,
\]

\[
10^{m_3}<Q_0(Q_0-1)/10,
\]

\[
10^g<\sqrt{10Q_0}.
\]

本轮校准：这些 Archimedean bounds 已经吸收了 continuous cone 的主要 pairwise content；下一层必须真正用 integer radial/coprime information。

## Minus

\[
\boxed{\textbf{OPEN GLOBALLY}.}
\]

但：

- primitive-only infinite family frozen；
- 该 explicit family被 ordering theorem杀掉；
- 整个 corresponding fixed conic profile 被 integer common-\(U\) theorem完全关闭；
- 同一 conic仍存在 real-cone exact gcd-profile points，证明 radial integrality不可删除。

## Full A1

\[
\boxed{A_1\textbf{ NOT CLOSED}.}
\]

但 fixed-profile infinity 已被 common integer scale完全删除。

---

# 28. Minimal Remaining Semantic Obstruction

本轮前 frontier：

\[
\text{primitive synchronized conic}
\longrightarrow
\text{common-}U\text{ digit cone}
\longrightarrow
\text{actual word/cut/norm}.
\]

本轮后可以改写成：

\[
\boxed{
\begin{array}{c}
\text{moving synchronized primitive state}
\cr
\Downarrow
\cr
I_{23}=[L_{23},R_{23})
\cr
\Downarrow
\cr
N_V(L_{23},R_{23})>0\ ?
\end{array}
}
\]

其中

\[
N_V(L,R)
=
\#\{U\in\mathbf Z_{>0}\cap[L,R):\gcd(U,V)=1\}.
\]

若答案 yes，则 exact forward reconstruction 已经恢复完整 candidate；若 original theorem 正确，这种 state 必须不存在。

所以真正 minimal remaining obstruction 是：

\[
\boxed{
\textbf{Moving-Profile Coprime Integer-Scale Exclusion.}
}
\]

不是 fixed conic rational-point finiteness，也不是新的 prime support theorem。

---

# 29. Interface to Backward Same-Cut Norm Feedback

反向线当前主攻 same-cut norm-excess feedback。

本轮不复制其 phase / norm 推导。

新的无重复接口应写成：

### Forward supplies

\[
(P_i,Q_0),
\quad
V,g_i,b_i,
\quad
(n_2,n_3,m_2,m_3,k,g),
\]

exact GSYNC branch，以及

\[
I_{23}\cap\{U\in\mathbf Z_{>0}:\gcd(U,V)=1\}.
\]

若该集合为空，forward 直接死亡。

若出现候选 \(U\)，forward 直接恢复

\[
a_i=UP_i/g_i,
\qquad b_i=V/g_i.
\]

此时 backward 可以读取同一个 actual cut \((a_1,a_2)\)，用其 norm-excess / residual phase machinery导出 contradiction。

但逻辑上：

\[
\boxed{
\text{backward norm feedback 是 survivor elimination engine，}
\text{不是 forward reconstruction 仍缺失的数据。}
}
\]

这能避免两条线重复证明同一个 normalization。

---

# 30. Recommended Next Campaign

本轮之后，不建议第五轮再做 generic conic parametrization campaign；fixed profile 的 infinity 已经被 integer radial theorem处理。

最值得投入高预算的新主战场应改名为：

\[
\boxed{
\textbf{A1 Moving-Profile Coprime Integer-Scale Campaign}
}
\]

优先顺序：

## Target 1 — Moving-profile escape normalization

从

\[
Q_0
<
\frac{g_2^2(10^{n_2}-1)^2+g_3^2(10^{n_3}-1)^2}{U^2}
\]

和

\[
10^g<\sqrt{10Q_0}
\]

出发，定义真正的 moving scale，例如

\[
X_2:=\frac{g_2 10^{n_2}}{U\sqrt{Q_0}},
\qquad
X_3:=\frac{g_3 10^{n_3}}{U\sqrt{Q_0}},
\]

至少一个必须 \(>1/\sqrt2\)。研究 plus/minus GSYNC 是否允许这种 escape arm持续移动。

## Target 2 — Exact pair interval arithmetic

minimal A1 下只需

\[
I_{23}
=
\left[
\max\left(
\frac{10^{n_2-1}g_2}{P_2},
\frac{10^{n_3-1}g_3}{P_3}
\right),
\min\left(
\frac{10^{n_2}g_2}{P_2},
\frac{10^{n_3}g_3}{P_3}
\right)
\right).
\]

直接研究

\[
\boxed{N_V(I_{23})}
\]

而不是继续研究 abstract cone。

## Target 3 — Plus radial attack

plus projective inequality已基本等价于 cone boundary；下一步应把

\[
UQ_0>g_3 10^{n_3-1}(1+10^{n_2-1})
\]

与 exact integer interval endpoint、\(V\)-coprimality、sphere factorization

\[
(Q_0-P_1)(Q_0+P_1)=P_2^2+P_3^2
\]

同步。

## Target 4 — Minus moving-profile classification

不要再研究 third-round fixed profile；它已完全关闭。

真正问题是：是否存在 sequence of profiles

\[
(g_2,g_3,n_2,n_3,\dots)
\]

使 synchronized primitive state 和 coprime integer interval同时逃逸。

## Target 5 — Early splice criterion with backward line

若 forward 可将

\[
N_V(I_{23})
\]

压到 1 或 very small finite set，不必再试图单独 forward closure；可立刻把 exact \(U\) / actual blocks交给 backward same-cut norm feedback。

---

# 31. Final Assessment

本轮没有证明

\[
A_1=\varnothing.
\]

也没有关闭 plus 或 general minus。

但它完成了一个比“再排一个 conic arc”更根本的 architecture correction。

第三轮后看起来主问题是：

\[
\boxed{
\text{一条 synchronized conic 能否无限次穿过 digit cone？}
}
\]

本轮证明这句话必须拆成两层：

\[
\boxed{
\textbf{Projective question:}
\quad
\mathcal C_{\rm sync}\cap\mathcal K_{\mathbf n}
}
\]

和

\[
\boxed{
\textbf{Radial arithmetic question:}
\quad
[L,R)\cap\mathbf Z_{>0}\cap(\mathbf Z/V\mathbf Z)^\times.
}
\]

第一层可以很大：open conic arcs、无限 rational points都完全可能。

第二层才是决定性刚性。

特别：

\[
\boxed{
\text{fixed profile}
\Longrightarrow
\text{integer common-}U\text{ forces }Q_0\text{ bounded}.
}
\]

所以所有 fixed-profile conic infinity 已经从 genuine A1 frontier 删除。

剩余问题不再是：

\[
\text{“fixed conic 上 rational parameter 会不会无限？”}
\]

而是：

\[
\boxed{
\textbf{能否存在一个 moving profile sequence，}
\textbf{使每一层的 synchronized primitive state 都产生 coprime positive integer }U？
}
\]

同时，forward reconstruction audit 表明：若这样的 \(U\) 真存在，它已经恢复完整 exact candidate。因此 A1 正向线现在已经压到一个真正低维、终端、可与 backward 无缝对接的问题：

\[
\boxed{
\textbf{Moving-Profile Coprime Integer-Scale Exclusion.}
}
\]

这应当作为下一轮的唯一顶层目标。

---

# 32. Claim Ledger

## PROVED

1. common-\(U\) interval canonical form \([L,R)\)；
2. exact projective one-decade criterion；
3. exact pairwise ratio theorem；
4. log-hexagon / decimal-phase characterization；
5. complete digit-order compatibility；
6. multiplication carry gap \(\max(n_i-\ell C_i)-\min(n_i-\ell C_i)\le1\)；
7. minimal A1 first-block digit window existential elimination；
8. exact integer count formula；
9. exact coprime count formula；
10. reducedness automatic from \(g_i=\gcd(V,P_i)\) and \(\gcd(U,V)=1\)；
11. weighted height shell \(M\le UQ_0<10M\)；
12. fixed-profile radial termination；
13. fixed profile has finite integer-common-\(U\) primitive states；
14. continuous projective cone can contain infinitely many rational conic points；
15. third-round conic explicit rational parametrization；
16. \(C_2/C_3\) monotonicity for that parametrization；
17. exact common-\(V\) real-cone survivor at \(t=-31/29\)；
18. continuous common scale does not imply integer common scale；
19. third-round entire fixed profile conic has no integer common-\(U\) point；
20. exact GSYNC/master + coprime integer common-\(U\) + exact profile reconstructs full original candidate。

## CONDITIONAL

1. any use of three-window \(\mathcal K_{\mathbf n}\) globally assumes \(n_1\) is part of the frozen full SGR state；minimal A1 frontier may eliminate it；
2. rational interior point \(\Rightarrow\) infinitely many rational cone points assumes nondegenerate rational conic parametrization on that component。

## EXPERIMENTAL

1. finite scan \(Q_0\le250,V\le60,k\le4\) found only the known minus state；
2. several additional rational slopes on the regression conic yield exact gcd-profile real-cone states；infinite exact gcd-profile density was not proved。

## FAILED / DISPROVED

1. continuous common-scale cone as a closure mechanism；
2. fixed-profile projective rational finiteness；
3. digit ordering as a general minus closure；
4. pure projective boundary \(P_3/Q_0\to0\) as uniform Type-F closure；
5. unique-\(U\) from common-scale geometry alone；
6. interpreting backward norm as semantic information still missing after exact integer scale reconstruction。

## OPEN

1. plus branch；
2. general minus branch across moving profiles；
3. uniform exclusion of coprime integer \(U\) on moving synchronized states；
4. whether forward can reduce \(N_V(I_{23})\) to \(0/1\) uniformly enough to splice immediately into backward same-cut norm；
5. full
   \[
   \boxed{A_1=\varnothing.}
   \]

---

# 33. Provenance / Dependency Audit

本轮主要依赖以下当前 Strict-Layer 自建文件：

- `strict_layer_A1_moving_core_decimal_translation_global_campaign.md`；
- `strict_layer_A1_flat_locus_structural_elimination_campaign.md`；
- `strict_layer_A1_generic_primitive_defect_synchronization_campaign.md`；
- `strict_layer_unified_exact_lift_campaign.md`；
- `strict_layer_post_DD_consolidation_A1_frontier.md`（通过前述报告冻结）；
- backward 文件仅用于确认 anti-duplication interface，不用于本轮新 theorem 的证明。

本轮新结论的依赖分层如下。

### Common-scale cone theorems

只依赖：

\[
a_i=UC_i
\]

与原始 decimal digit definition。

### Fixed-profile radial termination

只依赖：

- common integer \(U\) 的 block-2/3 digit legality；
- \(P_i=g_iC_i\)；
- primitive sphere；
- positivity/integrality。

不依赖 GSYNC、Hensel、Gaussian、backward phase。

### Regression whole-conic closure

只依赖：

- 第三轮 exact profile plane+sphere；
- integer digit bounds \(Uy\in[10,100),Uz\in[1,10)\)；
- elementary triangle inequality；
- 18 个 terminal quadratic-nonresidue checks。

### Terminal reconstruction theorem

只依赖：

- exact primitive sphere；
- exact common-\(V\) gcd profile；
- exact A1 GSYNC/master identity；
- common integer \(U\)；
- numerator/denominator digit legality；
- \(\gcd(U,V)=1\)。

没有调用 External Exact-Lift closure theorem，也没有调用 backward same-cut phase。

因此本轮主要结构结论具有干净、自包含的 Strict-Layer provenance。

