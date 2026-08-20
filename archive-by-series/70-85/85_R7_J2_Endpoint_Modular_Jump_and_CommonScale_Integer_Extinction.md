# 85 第七轮阶段报告：J2 Endpoint Modular-Jump Control × Common-Scale Integer Extinction

**项目：** 三项十进制拼接平方和问题  
**范围：** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**轮次：** 85-R7  
**主任务：** Endpoint Modular Jump / Common-Scale Source-Lift Obstruction  
**最终状态：** J2 OPEN；endpoint-jump architecture 在合法 PRE_ROOT information class 上被判定缺乏 rigidity  
**诊断脚本：** `85_R7_endpoint_jump_diagnostic.py`  
**诊断证书：** `85_R7_endpoint_jump_certificate.txt`

---

# 1. Executive Summary

R7 的目标是第一次用一个同时读取

\[
\text{outer decimal base}
\quad+\quad
\text{primitive fibre}
\]

的 mixed invariant，直接攻击 R6 找到的 genuine source-projection loss：

\[
\exists U\in I_{23}\cap\mathbb Z_{>0},
\qquad
\gcd(U,V)=1.
\]

候选 mixed invariants 为

\[
\delta_2=(-10^{2g+k-1})\bmod C_2,
\qquad
\delta_3=(-10^{g-1})\bmod C_3.
\]

本轮完整恢复了 exact endpoint theorem，并在 J2 中得到 exact required-jump bounds；同时恢复了 root-independent J2 linear source chart

\[
C_3=c,
\qquad
C_2=Ac+H\lambda,
\]

以及

\[
2KC_1=Bz+A\lambda,
\qquad
T=Gz+u\lambda.
\]

结论并不是 jump 被锁死。恰恰相反：

\[
\boxed{\textbf{J2 PRE\_ROOT linear information does not rigidify }
\delta_2,\delta_3.}
\]

有三个独立证据。

第一，J2 specialization 下 required-small-jump bound 经常根本“不 small”。  
Face A：

\[
\Delta_2^{\rm req}
=
\left\lfloor\frac{C_2(G-1)}{C_3}\right\rfloor
-\frac{G^2K}{10},
\]

Face B：

\[
\Delta_3^{\rm req}
=
\left\lfloor\frac{C_3(G^2K-1)}{C_2}\right\rfloor
-\frac G{10}.
\]

若

\[
\Delta_i^{\rm req}\ge C_i-1,
\]

则因为

\[
0\le\delta_i<C_i,
\]

整个 jump condition 自动成立；endpoint phase 完全不再提供 codimension。

第二，在 R6 使用过的同一个 live outer base

\[
(g,k,u,q)=(4,1,73,137)
\]

上，对严格 PRE_ROOT 线性 chart 做 exact finite reconnaissance：

```text
linear_pre_root             = 104370
continuous                  = 11190
ordinary_feasible           = 10809
coprime_feasible            = 10284
required_window_vacuous     = 10477
required_window_active      = 712
required_window_negative    = 1
```

也就是说，在 11190 个连续可行 state 中，有 10477 个 state 的 required jump window 已经覆盖整个 jump modulus。

而 ordinary-feasible states 的 jump ratio 实际覆盖极宽区间：

Face A：

\[
\frac{\delta_2}{C_2}
\in
\left[
\frac{4190}{10000419},
\frac{6665744}{6666609}
\right]
\]

在本次 exact scan 中已经从接近 \(0\) 到接近 \(1\)。

Face B：

\[
\frac{\delta_3}{C_3}
\in
\left[
\frac1{77},
\frac{26}{27}
\right].
\]

所以不存在 finite jump spectrum，也不存在 forbidden-small-jump pattern 的实验迹象。

第三，也是本轮最强 falsification result：存在一个严格可证的**无限 PRE_ROOT-linear common-scale/coprime family**。

对任意

\[
g=5+22t,\qquad t\ge0,
\]

令

\[
G=10^g,\quad K=10,\quad
u=11,\quad q=\frac{G+1}{11},\quad
A=23,\quad H=\frac G2,
\]

并取

\[
C_3=c=1,\qquad z=1,\qquad \lambda=3.
\]

则

\[
C_2=23+3H=\frac{3G+46}{2},
\]

\[
C_1=\frac{(2G+q)+69}{20},
\qquad
T=G+33
\]

均为合法整数，并满足全部本轮所用的 J2 PRE_ROOT 线性 identities、ten-unit/reducedness 条件以及 regular

\[
\gcd(A,d_2)=1.
\]

取

\[
\boxed{U=G-1}
\]

则同时有

\[
G^2\le UC_2<10G^2,
\]

\[
\frac G{10}\le UC_3<G,
\]

且

\[
V=uGH=\frac{11G^2}{2},
\qquad
\boxed{\gcd(U,V)=1}.
\]

因此 ordinary common-scale 与 coprimality 在这个 PRE_ROOT information class 上都不是 thin obstruction。

更强地，该族处于 Face A，且

\[
\Delta_2^{\rm req}
=
C_2(G-1)-G^2
=
\frac{G^2+43G-46}{2},
\]

并满足

\[
\Delta_2^{\rm req}\ge C_2-1.
\]

所以 Face A jump restriction 对该无限族是**完全 vacuous**。

此外可精确计算

\[
10^{2g+k-1}=G^2,
\]

\[
G^2\bmod C_2
=
\frac{4C_2+2116}{9},
\]

故

\[
\boxed{
\delta_2
=
\frac{5C_2-2116}{9}
}
\]

并且

\[
\boxed{
\frac{\delta_2}{C_2}\longrightarrow\frac59.
}
\]

即使 jump 稳定在一个远离 \(0\) 的正比例位置，common-scale 仍然完全可行。

这直接判死：

\[
\boxed{
\text{“J2 forces endpoint jump too large for common-scale feasibility”}
}
\]

作为一个只使用 PRE_ROOT source identities 的 universal architecture。

必须强调：上述无限族**不是** primitive-sphere/root survivor，更不是 J2 solution family。它的用途是 dependency/model falsification：

> 任何只从当前合法 PRE_ROOT linear \(C_2,C_3\) information 推导 universal jump extinction 的证明，都必须同时杀掉这个 family；但这个 family 已 exact 通过 ordinary common-scale，甚至通过 coprimality。

而历史档案明确把 DCDC 标为

```text
DCDC_PRE_ROOT_PROVENANCE=FALSE
DCDC_SAFE_EARLY_SIEVE=TRUE
```

所以 R7 不能借 DCDC 或 full root/sphere gate 删除该 family，再宣称得到独立 source-lift obstruction。

因此：

```text
J2_STATUS=OPEN

ENDPOINT_JUMP_MIXED_INVARIANT=TRUE
ENDPOINT_JUMP_INDEPENDENT_OF_FA_FB_AS_A_DEFINITION=TRUE
J2_PRE_ROOT_JUMP_RIGIDITY=ABSENT
FINITE_JUMP_SPECTRUM=FALSE_AT_PRE_ROOT_INFORMATION_CLASS
FORBIDDEN_SMALL_JUMP=FALSE_AS_UNIVERSAL_PRE_ROOT_MECHANISM
REQUIRED_SMALL_JUMP_WINDOW=OFTEN_VACUOUS

ORDINARY_COMMON_SCALE_PRE_ROOT_LINEAR=LARGE
COPRIME_COMMON_SCALE_PRE_ROOT_LINEAR=LARGE
ORDINARY_COMMON_SCALE_FULL_PRIMITIVE_SURVIVOR=UNKNOWN

R7_SUCCESS_LEVEL=R7-S1

R7_TERMINAL_VERDICT=
ENDPOINT_JUMP_RIGIDITY_ABSENT
```

R8 不应进入 Jacobsthal/coprime refinement，因为 coprimality 已经不能救当前 endpoint information class；也不应继续 endpoint jump、ZGAP、radial gap 或 generic common-\(U\) spacing。

R8 必须再换 mixed information class。

---

# 2. R6 Frozen Verdict

R6 冻结：

\[
\boxed{
\exists U\in I_{23}\cap\mathbb Z_{>0},
\qquad
\gcd(U,V)=1
}
\]

是从 pre-radial/radial state 返回 genuine full-word source 时真正丢失的信息。

J2 中：

\[
I_2=
\left[
\frac{G^2K}{10C_2},
\frac{G^2K}{C_2}
\right),
\]

\[
I_3=
\left[
\frac{G}{10C_3},
\frac{G}{C_3}
\right),
\]

\[
I_{23}=I_2\cap I_3.
\]

R6 同时证明 actual \(N_0\)-split 只读取 outer base；在 fixed split base 内对 primitive/common-scale fibre 没有额外 codimension。

因此：

```text
N0_FULLWORD_INTERFACE=INSUFFICIENT
```

R7 不重开 \(N_0\)-split × full-word 交叉。

---

# 3. Why \(N_0\) Is Retired

\(N_0=N_0(G,K,u,q)\) 不读取

\[
U,\quad C_1,C_2,C_3,
\]

所以对 fixed outer base：

\[
N_0\text{-split}
\]

无法区分：

- common-scale feasible primitive fibre；
- common-scale infeasible primitive fibre。

R7 需要一个真正同时读取 base 与 primitive fibre 的量。

Endpoint jumps 满足这一最低要求：

\[
\delta_2
=
(-10^{2g+k-1})\bmod C_2,
\]

\[
\delta_3
=
(-10^{g-1})\bmod C_3.
\]

---

# 4. Common-Scale Source-Lift Criterion

定义

\[
x_2:=10^{n_2-1},
\qquad
x_3:=10^{n_3-1}.
\]

J2 中

\[
n_2=2g+k,
\qquad
n_3=g,
\]

故

\[
\boxed{
x_2=\frac{G^2K}{10},
\qquad
x_3=\frac G{10}.
}
\]

两个 block window 为

\[
I_2=
\left[\frac{x_2}{C_2},\frac{10x_2}{C_2}\right),
\qquad
I_3=
\left[\frac{x_3}{C_3},\frac{10x_3}{C_3}\right).
\]

ordinary common-scale existence：

\[
\boxed{
I_{23}\cap\mathbb Z_{>0}\ne\varnothing.
}
\]

full source lift 还需

\[
\boxed{
\exists U\in I_{23}\cap\mathbb Z_{>0},
\qquad
\gcd(U,V)=1.
}
\]

---

# 5. J2 Endpoint Jump Definitions

对任意 \(C_i>0\)，定义最小非负 Euclidean jump：

\[
\boxed{
\delta_i
=
\left\lceil\frac{x_i}{C_i}\right\rceil C_i-x_i
=
(-x_i)\bmod C_i.
}
\]

因此 J2：

\[
\boxed{
\delta_2
=
\left(-\frac{G^2K}{10}\right)\bmod C_2,
}
\tag{E2}
\]

\[
\boxed{
\delta_3
=
\left(-\frac G{10}\right)\bmod C_3.
}
\tag{E3}
\]

取值约定：

\[
0\le\delta_2<C_2,
\qquad
0\le\delta_3<C_3.
\]

若 lower endpoint 本身为整数，则对应 jump 为 \(0\)，不能强行改成 modulus。

---

# 6. Face A / Face B Endpoint Legality Theorem

## 6.1 Face A

Face A 定义为 block 2 给出 active lower endpoint：

\[
\frac{x_2}{C_2}
\ge
\frac{x_3}{C_3}.
\]

令

\[
\boxed{
G_A^\circ
=
C_2\,10^{n_3}
-
C_3\,10^{n_2-1}.
}
\]

J2 中：

\[
\boxed{
G_A^\circ
=
C_2G
-
C_3\frac{G^2K}{10}.
}
\]

连续可行要求：

\[
G_A^\circ>0.
\]

第一个可能整数为

\[
U_A
=
\left\lceil\frac{x_2}{C_2}\right\rceil
=
\frac{x_2+\delta_2}{C_2}.
\]

其落入 inactive upper endpoint

\[
U_A<\frac{10x_3}{C_3}
\]

当且仅当

\[
\boxed{
C_3\delta_2<G_A^\circ.
}
\]

又因为

\[
G_A^\circ-C_3\delta_2
\]

是 \(C_2\) 的整数倍，所以严格不等式等价于

\[
\boxed{
G_A^\circ
\ge
C_3\delta_2+C_2.
}
\tag{FA}
\]

这就是 exact endpoint legality theorem。

---

## 6.2 Face B

Face B 定义为

\[
\frac{x_3}{C_3}
>
\frac{x_2}{C_2}.
\]

令

\[
\boxed{
G_B^\circ
=
C_3\,10^{n_2}
-
C_2\,10^{n_3-1}.
}
\]

J2 中：

\[
\boxed{
G_B^\circ
=
C_3G^2K
-
C_2\frac G{10}.
}
\]

第一个可能整数：

\[
U_B
=
\left\lceil\frac{x_3}{C_3}\right\rceil.
\]

ordinary survival 当且仅当

\[
\boxed{
C_2\delta_3<G_B^\circ
}
\]

等价于

\[
\boxed{
G_B^\circ
\ge
C_2\delta_3+C_3.
}
\tag{FB}
\]

---

## 6.3 两个 face 的关系

两 face 不是“同一 state 要同时满足”的两条独立约束。

它们由 active lower endpoint 的 orientation 分割：

\[
\boxed{
\text{每个连续可行 state 恰落入 Face A 或 Face B。}
}
\]

Face A/B 是 endpoint theorem 的两张 chart。

边界

\[
x_2/C_2=x_3/C_3
\]

按本报告 convention 归入 Face A；此时两个 lower endpoints 相同。

---

# 7. Required Small-Jump Bounds

从 Face A：

\[
G_A^\circ
\ge
C_3\delta_2+C_2
\]

得

\[
\delta_2
\le
\left\lfloor
\frac{G_A^\circ-C_2}{C_3}
\right\rfloor.
\]

定义

\[
\boxed{
\Delta_2^{\rm req}
=
\left\lfloor
\frac{C_2(G-1)}{C_3}
\right\rfloor
-
\frac{G^2K}{10}.
}
\tag{D2REQ}
\]

同理：

\[
\boxed{
\Delta_3^{\rm req}
=
\left\lfloor
\frac{C_3(G^2K-1)}{C_2}
\right\rfloor
-
\frac G{10}.
}
\tag{D3REQ}
\]

ordinary survival 的 jump form 为：

Face A：

\[
\boxed{\delta_2\le\Delta_2^{\rm req};}
\]

Face B：

\[
\boxed{\delta_3\le\Delta_3^{\rm req}.}
\]

但必须马上加入一个重要三分法：

### impossible required window

\[
\Delta_i^{\rm req}<0
\]

则该 face 无 ordinary integer。

### active modular window

\[
0\le\Delta_i^{\rm req}<C_i-1.
\]

只有这里 modular jump 真正有机会增加 codimension。

### vacuous modular window

\[
\boxed{
\Delta_i^{\rm req}\ge C_i-1.
}
\]

此时任意

\[
0\le\delta_i<C_i
\]

自动通过。

这一区分是 R7 的核心新校准。

---

# 8. \((C_2,C_3)\) Provenance Audit

J2 frozen linear normal form令

\[
c:=C_3.
\]

引入 third Euclidean ten-unit \(z\) 和 fourth Euclidean coordinate \(\lambda\)（这里特意不用 \(\ell\)，避免与当前 deficiency \(\ell=2g-k\) 冲突）。

在 sphere/root elimination 之前，线性 Euclidean system 给：

\[
\boxed{
C_3=c,
}
\tag{C3-PRE}
\]

\[
\boxed{
C_2=Ac+H\lambda,
}
\tag{C2-PRE}
\]

\[
\boxed{
2KC_1=Bz+A\lambda,
}
\tag{C1-PRE}
\]

\[
\boxed{
T=Gz+u\lambda.
}
\tag{T-PRE}
\]

其中

\[
A=2u+1,\quad
B=2G+q,\quad
H=G/2,\quad
uq=G+1.
\]

并有 sign-unified linear chart：

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
X=GHz-uAc,
\]

\[
d_2=uc+GX.
\]

negative branch：

\[
X>0.
\]

## Provenance classification

| object | provenance | R7 可否用于独立 jump law |
|---|---|---|
| \(C_3=c\) | PRE_ROOT coordinate | YES |
| \(C_2=Ac+H\lambda\) | PRE_ROOT linear Euclidean | YES |
| \(2KC_1=Bz+A\lambda\) | PRE_ROOT linear Euclidean | YES |
| \(T=Gz+u\lambda\) | PRE_ROOT linear Euclidean | YES |
| CZ linear identities | PRE_ROOT linear Euclidean | YES |
| DCDC \(2K\mid\widetilde F\) | ROOT-necessary early sieve; historical provenance says not PRE_ROOT | NO for independence proof |
| sphere quadratic | ROOT-equivalent / root-containing layer | NO |
| discriminant square / root divisibility | ROOT layer | NO |
| \(\varepsilon_*=0\) | FULL ROOT | NO |

因此 R7 的 independent source-lift obstruction 必须在前五行的 PRE_ROOT information class 内成立。

---

# 9. J2-Specialized Modular Reduction

R7 寻找：

\[
10^{2g+k-1}\pmod{C_2},
\qquad
10^{g-1}\pmod{C_3}.
\]

J2 linear form给出一些 exact reduction，但没有 rigidification。

## 9.1 \(C_2\)-side

由

\[
C_2=Ac+H\lambda
\]

得

\[
H\lambda\equiv-Ac\pmod{C_2}.
\]

而

\[
10^{2g+k-1}
=
\frac{G^2K}{10}
=
H\frac{GK}{5}.
\]

故

\[
\boxed{
\lambda\,10^{2g+k-1}
\equiv
-\frac{AGK}{5}\,c
\pmod{C_2}.
}
\tag{MR2}
\]

这是 genuine mixed base–primitive congruence。

但一般

\[
\gcd(\lambda,C_2)
=
\gcd(\lambda,Ac)
\]

不必为 \(1\)，所以不能统一 invert \(\lambda\) 得到唯一 residue mod \(C_2\)。

即使局部可逆，右侧仍读取移动变量 \(c,\lambda\)，不是 finite spectrum。

---

## 9.2 \(C_3\)-side

由

\[
h=qHz-Ac
\]

模 \(c=C_3\)：

\[
qHz\equiv h\pmod c.
\]

因为

\[
10^{g-1}=H/5,
\]

得到

\[
\boxed{
5qz\,10^{g-1}
\equiv h
\pmod{C_3}.
}
\tag{MR3a}
\]

又由

\[
r=Hh-uc
\]

得

\[
\boxed{
5h\,10^{g-1}
\equiv r
\pmod{C_3}.
}
\tag{MR3b}
\]

同样，这些是 exact mixed congruences，但右端 \(h,r,z\) 随 primitive fibre 移动。

---

## 9.3 hidden cyclotomic congruence audit

真正 cyclotomic relation 是

\[
uq=G+1.
\]

它自然给出

\[
G\equiv-1\pmod u,
\]

即 power-of-ten control 发生在 modulus \(u\)。

R7 需要的 modulus 却是

\[
C_2,\quad C_3.
\]

PRE_ROOT linear dictionary没有证明：

\[
C_i\mid u,
\qquad
u\mid C_i,
\]

也没有固定：

\[
C_i\equiv f(G,u,q)\pmod{\text{bounded modulus}}.
\]

因此：

\[
\boxed{
uq=G+1
\text{ does not transfer a cyclotomic order law to }C_2,C_3.
}
\]

---

# 10. Complementary Remainder Analysis

若

\[
r_i:=10^{n_i-1}\bmod C_i,
\qquad
0<r_i<C_i,
\]

则

\[
\delta_i=C_i-r_i.
\]

因此 small positive remainder 会产生 large jump。

这个 orientation 是正确的。

但 R7 的问题不是 orientation，而是 required window 本身经常已经大到：

\[
\Delta_i^{\rm req}\ge C_i-1.
\]

在这种 state 上，无论

\[
r_i
\]

small、large 或 generic，

\[
\delta_i\le\Delta_i^{\rm req}
\]

都自动成立。

所以 complementary-remainder collision 只能作用于 active modular window：

\[
0\le\Delta_i^{\rm req}<C_i-1.
\]

它不能成为全局 J2 closure mechanism。

---

# 11. Jump Spectrum Computation

本轮 exact reconnaissance 固定 R6 使用过的 live outer base：

\[
g=4,\quad
G=10000,\quad
k=1,\quad
K=10,
\]

\[
u=73,\quad
q=137,\quad
A=147,\quad
H=5000.
\]

使用：

\[
z=1,
\]

枚举

\[
1\le C_3=c\le5000,
\]

\[
1\le\lambda\le2000,
\]

仅保留：

- \(c,\lambda\) ten-unit；
- \(2K\mid Bz+A\lambda\)；
- \(C_1,C_2,T,h,m,r,X,d_2>0\)；
- negative \(X>0\)；
- ten-unit propagation；
- \(\gcd(A,d_2)=1\)；
- \(\gcd(C_1,u)=1\)；
- \(\gcd(C_2,H)=1\)；
- \(\gcd(C_3,GH)=1\)。

不使用 sphere、discriminant、root 或 DCDC。

exact census：

```text
linear_pre_root          104370
continuous                11190
Face A                     10171
Face B                      1019
ordinary_feasible          10809
coprime_feasible           10284

required_window_vacuous    10477
required_window_active       712
required_window_negative        1
```

因此：

\[
\boxed{
\frac{10477}{11190}
}
\]

的连续可行 sample state 中，jump modulus 整体已经落在 required window 内。

---

## 11.1 Face A jump support

ordinary-feasible sample：

\[
9791
\]

个。

最小观测 ratio：

\[
\boxed{
\frac{\delta_2}{C_2}
=
\frac{4190}{10000419}
}
\]

来自

\[
C_3=377,\quad
\lambda=1989,\quad
C_2=10000419.
\]

最大观测 ratio：

\[
\boxed{
\frac{\delta_2}{C_2}
=
\frac{6665744}{6666609}
}
\]

来自

\[
C_3=147,\quad
\lambda=1329,\quad
C_2=6666609.
\]

即 fixed outer base 内 jump 已从几乎 \(0\) 走到几乎整个 modulus。

---

## 11.2 Face B jump support

ordinary-feasible sample：

\[
1018
\]

个。

最小：

\[
\boxed{
\delta_3/C_3=1/77
}
\]

最大：

\[
\boxed{
\delta_3/C_3=26/27.
}
\]

同样没有 finite-image / forbidden-small-jump pattern。

---

## 11.3 active-window fail 与 survive 同时存在

active failure：

\[
C_3=9,\quad
\lambda=1789,\quad
C_2=8946323,
\]

Face B：

\[
\delta_3=8,
\qquad
\Delta_3^{\rm req}=5,
\]

故无 ordinary integer。

而 active survival：

\[
C_3=213,\quad
\lambda=429,\quad
C_2=2176311,
\]

Face A：

\[
\delta_2=110306,
\qquad
\Delta_2^{\rm req}=2164007,
\]

且

\[
I_{23}\cap\mathbb Z=\{46\}.
\]

所以 endpoint jump 确实能杀某些 state，但没有 uniform orientation。

---

# 12. Independence Firewall

## 12.1 definitions themselves are genuinely mixed

\[
\delta_2,\delta_3
\]

同时读取：

- decimal base exponent；
- primitive modulus \(C_i\)。

因此：

```text
ENDPOINT_JUMP_MIXED_INVARIANT=TRUE
```

它们不是 \(N_0\)-split 那种 outer-only object。

---

## 12.2 FA/FB 与 jump definition 的关系

jump definition：

\[
\delta_i=(-x_i)\bmod C_i
\]

不由 FA/FB 定义，所以作为 arithmetic coordinate 它是 independent。

但：

\[
\delta_i\le\Delta_i^{\rm req}
\]

本身**就是** FA/FB 的 endpoint legality 重写。

因此任何“新 theorem”若最终只证明

\[
G_A^\circ-C_3\delta_2-C_2\ge0
\]

或 symmetric form，而来源仍是 ZGAP/RU-H/radial gap，则是 dependency loop。

历史 campaign 已经证明：

\[
\text{ZGAP/RU-H}
+
\delta_i
\]

会代数折回 raw endpoint survival。

所以：

```text
OLD_ZGAP_ENDPOINT_SPLICE=DEPENDENCY_REDUNDANT
RU_H_ENDPOINT_SPLICE=DEPENDENCY_REDUNDANT
```

---

## 12.3 new J2 modular laws

(MR2)、(MR3a)、(MR3b) 是由 J2 PRE_ROOT linear identities直接推出，不是 FA/FB 的反向重建。

所以：

```text
J2_MODULAR_REDUCTION_PROVENANCE=INDEPENDENT_PRE_ROOT_LINEAR
```

但它们没有增加 usable codimension，因为移动变量没有消失：

\[
(C_3,\lambda,z,h,r)
\]

仍保留完整 fibre freedom。

因此更准确的 verdict 是：

```text
ENDPOINT_JUMP_CONSTRAINT=
INDEPENDENT_BUT_NONRIGID
```

而不是错误地标为 dependency-redundant。

---

# 13. Generic-A1 Dependency Comparison

generic A1 endpoint campaign 的失败机制是：

\[
\text{old radial gap}
\longrightarrow
\text{first-candidate excess}
\longrightarrow
\text{raw endpoint legality}.
\]

R7 没有重复这一回路。

本轮真正新增的 negative result 是：

\[
\boxed{
\text{即使加入 J2-specific }uq=G+1
\text{ 与 Euclidean }(c,z,\lambda)\text{ structure，}
}
\]

\[
\boxed{
\text{endpoint jump 仍有宽 support，
且 required window 通常不 small。}
}
\]

所以 R7 的失败原因比 generic campaign 更强：

> 不是我们又把旧条件重写了一次，而是 exact J2-specific PRE_ROOT family 本身已经给出 endpoint architecture 的反模型。

---

# 14. Face A Extinction Attempt

目标：

\[
G_A^\circ<C_3\delta_2+C_2.
\]

失败。

无限 family（Part 19）满足：

\[
\Delta_2^{\rm req}\ge C_2-1,
\]

故对全部可能 jump：

\[
\delta_2\le C_2-1\le\Delta_2^{\rm req}.
\]

因此：

\[
\boxed{
\text{Face A cannot be uniformly closed by endpoint jump
from the current PRE_ROOT information class.}
}
\]

---

# 15. Face B Extinction Attempt

Face B 的 fixed-base exact scan 中，1019 个连续可行 state 有：

\[
1018
\]

个 ordinary feasible。

并且这 1018 个全部满足：

\[
\Delta_3^{\rm req}\ge C_3-1,
\]

即 jump condition 对整个 modulus vacuous。

只有一个 active Face-B state：

\[
C_3=9,\lambda=1789
\]

被 jump 杀死。

因此：

\[
\boxed{
\text{Face B endpoint jump also has no uniform rigidity
in the audited PRE_ROOT chart.}
}
\]

---

# 16. Endpoint Equality Cases

exact theorem 的 equality：

Face A：

\[
G_A^\circ=C_3\delta_2+C_2
\]

对应：

\[
G_A^\circ-C_3\delta_2=C_2,
\]

即 candidate count 恰从 0 跳到 1。

同理 Face B。

因此 equality 不是可被粗 inequality 丢掉的“measure-zero”情形，而是：

\[
\boxed{\text{exactly one endpoint-lattice quantum survives}}
\]

的合法情况。

本轮没有发现 equality 自身带来新的 J2-specific contradiction。

若后续 architecture 再遇 equality，必须继续检查：

- strict upper endpoint；
- \(U>0\)；
- common scale；
- \(\gcd(U,V)=1\)；
- full block legality。

R7 不宣称 equality closed。

---

# 17. Ordinary Integer Feasibility

必须分两个语义层级。

## 17.1 PRE_ROOT linear source-projection information class

exact fixed-base scan：

\[
10809/11190
\]

continuous states 有 ordinary common scale。

更强地，Part 19 给出无限 exact family。

所以：

```text
ORDINARY_COMMON_SCALE_PRE_ROOT_LINEAR=LARGE
```

并且不是只在一个偶然 finite box 中 LARGE。

---

## 17.2 Full current primitive/root-eligible survivor

R7 没有构造一个通过 primitive sphere/root compatibility 的 \(g\ge4\) survivor。

历史 \(g=2,3\) exact primitive census本身没有 primitive survivors；那是已经关闭的小 \(g\) 区域，不能外推到当前 \(g\ge4\) frontier。

因此：

```text
ORDINARY_COMMON_SCALE_FULL_PRIMITIVE_SURVIVOR=UNKNOWN
```

绝不能把 PRE_ROOT-linear counterfamily误报成 J2 solution family。

---

# 18. Coprime-Layer Decision

用户预设：

> ordinary feasibility LARGE 时，可转 coprimality。

但 R7 得到更强的 architecture-level反结果：

在 fixed-base scan 中：

\[
10284
\]

个 state 已经有 coprime common scale。

而无限 family直接给：

\[
U=G-1,
\qquad
V=\frac{11G^2}{2},
\]

\[
\boxed{\gcd(U,V)=1}.
\]

因此在**同一个 PRE_ROOT endpoint information class**中，coprimality 也不是 missing codimension。

所以：

```text
COPRIME_LAYER=
NOT_ACTIVATED_AS_R8_ENDPOINT_CONTINUATION
```

原因不是 “coprimality 已经证明永远可行”，而是：

\[
\boxed{
\text{endpoint/common-scale information class itself already admits
infinite coprime lifts.}
}
\]

继续 Jacobsthal、density 或 finite candidate gcd exclusion无法修复这个 information-class defect。

---

# 19. Counterexamples / Infinite Feasible Families

## Theorem R7-PLCF — PRE_ROOT Linear Coprime Feasible Family

对任意

\[
t\in\mathbb Z_{\ge0},
\qquad
g=5+22t,
\]

令

\[
G=10^g,\quad
K=10,\quad
u=11,\quad
q=\frac{G+1}{11},
\]

\[
A=23,\quad
H=G/2,\quad
B=2G+q.
\]

取

\[
\boxed{
C_3=c=1,\qquad z=1,\qquad\lambda=3.
}
\]

定义：

\[
\boxed{
C_2=\frac{3G+46}{2},
}
\]

\[
\boxed{
C_1=\frac{B+69}{20},
}
\]

\[
\boxed{
T=G+33.
}
\]

再定义：

\[
h=qH-23,
\]

\[
m=23h-G,
\]

\[
r=Hh-11,
\]

\[
X=GH-253,
\]

\[
d_2=11+GX.
\]

则以下全部成立。

### (i) \(q\) integral

因为 \(g\) 为奇数，

\[
10^g\equiv-1\pmod{11}.
\]

故

\[
11\mid G+1.
\]

### (ii) \(C_1\) integral

对 \(g\ge3\) 奇数，

\[
G\equiv120\pmod{220},
\]

故

\[
q\equiv11\pmod{20}.
\]

于是

\[
B+69
=
2G+q+69
\equiv0\pmod{20}.
\]

### (iii) reducedness

\[
\gcd(C_2,H)
=
\gcd(3H+23,H)
=1.
\]

\[
\gcd(C_3,GH)=1.
\]

又因为

\[
\operatorname{ord}_{121}(10)=22,
\]

且

\[
g\equiv5\pmod{22},
\]

有

\[
G\equiv10^5\equiv54\pmod{121},
\]

故

\[
q\equiv5\pmod{11}.
\]

从而

\[
C_1
=
\frac{2G+q+69}{20}
\equiv8\pmod{11},
\]

所以

\[
\gcd(C_1,u)=1.
\]

### (iv) regularity

\[
2d_2
=
22+G^3-506G
\equiv
G^3-1
\pmod{23}.
\]

因为

\[
\operatorname{ord}_{23}(10)=22,
\qquad
g\equiv5\pmod{22},
\]

\[
G^3
\equiv10^{15}
\equiv5\pmod{23}.
\]

所以

\[
2d_2\equiv4\pmod{23},
\]

即

\[
\boxed{\gcd(A,d_2)=1}.
\]

### (v) exact J2 PRE_ROOT linear identities

直接代数验证：

\[
C_3=2r-qX,
\]

\[
d_2=2ur-X,
\]

\[
Ar-X=mH,
\]

\[
GKC_1=AC_2+m,
\]

\[
uC_2+X=HT,
\]

\[
2uKC_1=AT+z.
\]

并且

\[
X>0,
\]

所以是 negative sign。

### (vi) common scale

取

\[
\boxed{U=G-1}.
\]

block 3：

\[
\frac G{10}\le G-1<G.
\]

block 2：

\[
UC_2-G^2
=
\frac{G^2+43G-46}{2}>0,
\]

\[
10G^2-UC_2
=
\frac{17G^2-43G+46}{2}>0.
\]

故

\[
\boxed{U\in I_{23}.}
\]

### (vii) coprimality

\[
V=uGH=\frac{11G^2}{2}.
\]

因为

\[
\gcd(G-1,G)=1
\]

且 \(g\) odd 时

\[
G-1\equiv-2\pmod{11},
\]

所以

\[
\boxed{\gcd(U,V)=1.}
\]

### (viii) jump is not small

Face A成立。

\[
\Delta_2^{\rm req}
=
C_2(G-1)-G^2
=
\frac{G^2+43G-46}{2}.
\]

而

\[
\Delta_2^{\rm req}-(C_2-1)
=
\frac{G^2+40G-90}{2}>0.
\]

故 required window 覆盖全部 jump residues。

此外：

\[
C_2=\frac{3G+46}{2}
\equiv2\pmod9.
\]

由

\[
3G\equiv-46\pmod{C_2}
\]

得

\[
9G^2\equiv2116\pmod{C_2}.
\]

于是：

\[
G^2\bmod C_2
=
\frac{4C_2+2116}{9},
\]

所以：

\[
\boxed{
\delta_2
=
C_2-\frac{4C_2+2116}{9}
=
\frac{5C_2-2116}{9}.
}
\]

因此：

\[
\boxed{
\delta_2/C_2\to5/9.
}
\]

证毕。

### Scope firewall

该 family 没有使用、也没有声称满足 sphere/root quadratic。

例如首个 \(g=5\) sample 的 sphere residual 为：

\[
H^2C_1^2+X^2-Td_2
=
-24743075589166136354\ne0.
\]

因此它不是 J2 source solution。

它是一个**information-class countermodel**：

\[
\boxed{
\text{PRE_ROOT J2 linear identities}
+
\text{common-scale}
+
\text{coprimality}
}
\]

本身不推出 contradiction。

---

# 20. Codimension Ledger

| condition | reads outer base? | reads primitive fibre? | independent? | codimension gain |
|---|---:|---:|---|---|
| \(N_0\)-split | YES | NO | YES | outer only |
| old radial gap / ZGAP | partial | YES | old | retired for endpoint closure |
| \(\delta_2\) definition | YES | YES | YES as coordinate | none by itself |
| \(\delta_3\) definition | YES | YES | YES as coordinate | none by itself |
| FA/FB | YES | YES | source-lift theorem | exact integer incidence |
| MR2/MR3 J2 modular laws | YES | YES | PRE_ROOT-independent of FA/FB | no uniform codimension |
| required jump bound | YES | YES | equivalent to FA/FB | no extra codimension |
| coprimality \(\gcd(U,V)=1\) | YES | YES | genuine source gate | survives in infinite PRE_ROOT family |
| sphere/root compatibility | YES | YES | later/root-equivalent | forbidden as R7 source-lift proof input |

最核心回答：

\[
\boxed{
\text{J2 jump law does not add an independent usable codimension beyond
the common-scale incidence at the PRE_ROOT level.}
}
\]

更精确地：

- jump coordinate 本身 independent；
- J2 modular reduction也是真正的新 PRE_ROOT consequence；
- 但其 fibre image仍然太大；
- 所以 **independent \(\neq\) rigid**。

---

# 21. Proven vs Computational Claims

## PROVED

1. J2 endpoint jump definitions。
2. Face A/B exact legality theorem。
3. required jump bounds (D2REQ)/(D3REQ)。
4. active/vacuous/impossible required-window trichotomy。
5. PRE_ROOT linear reconstruction
   \[
   C_3=c,\quad C_2=Ac+H\lambda.
   \]
6. modular reductions (MR2), (MR3a), (MR3b)。
7. cyclotomic modulus mismatch：
   \(uq=G+1\) naturally controls mod \(u\)，not mod \(C_i\)。
8. infinite PRE_ROOT-linear coprime common-scale family R7-PLCF。
9. exact family jump formula
   \[
   \delta_2=(5C_2-2116)/9.
   \]
10. family required jump window is vacuous。
11. family has \(\gcd(U,V)=1\) with \(U=G-1\)。

## COMPUTATIONAL / EXACT FINITE RECONNAISSANCE

Fixed base：

\[
(g,k,u,q)=(4,1,73,137)
\]

inside stated finite box gives：

```text
linear_pre_root          104370
continuous                11190
ordinary_feasible          10809
coprime_feasible           10284
required_window_vacuous    10477
required_window_active       712
required_window_negative        1
```

所有运算均 exact integer/Fraction。

这些 counts 不被外推成全局 theorem；全局 negative theorem 由 R7-PLCF 提供。

## NOT PROVED

1. 所有 full primitive/sphere survivor 都有 ordinary common scale。
2. 所有 full primitive/sphere survivor 都没有 ordinary common scale。
3. \(\delta_i\) 在 full root-compatible locus 上有 full support。
4. J2 closure。
5. singular branch closure。

---

# 22. R7 Terminal Verdict

本轮 success ladder：

### R7-S0

恢复旧 endpoint theorem：完成。

### R7-S1

证明 jump 是 genuine mixed invariant，并完成 independence/provenance audit：完成。

### R7-S2

得到 root-independent finite jump spectrum / lower bound / forbidden-small-jump theorem：**失败且 architecture-level falsified**。

### R7-S3/S4/S5

未达到。

最终：

```text
J2_STATUS=OPEN

R7_SUCCESS_LEVEL=R7-S1

ENDPOINT_JUMP_MIXED_INVARIANT=TRUE

J2_MODULAR_REDUCTION=
PROVED_BUT_MOVING_FIBRE_REMAINS

FINITE_JUMP_SPECTRUM=
FALSE_AT_PRE_ROOT_INFORMATION_CLASS

FORBIDDEN_SMALL_JUMP=
FALSE_AS_UNIVERSAL_PRE_ROOT_MECHANISM

REQUIRED_SMALL_JUMP_WINDOW=
OFTEN_VACUOUS

ORDINARY_COMMON_SCALE_PRE_ROOT_LINEAR=
LARGE

COPRIME_COMMON_SCALE_PRE_ROOT_LINEAR=
LARGE

ORDINARY_COMMON_SCALE_FULL_PRIMITIVE_SURVIVOR=
UNKNOWN

ENDPOINT_JUMP_RIGIDITY=
ABSENT

R7_TERMINAL_VERDICT=
ENDPOINT_JUMP_RIGIDITY_ABSENT
```

这比

```text
MIXED_ENDPOINT_ARCHITECTURE_DEPENDENCY_REDUNDANT
```

更准确。

原因是新 J2 modular laws并非旧 FA/FB 的代数重写；它们是真的 independent PRE_ROOT consequences。

但它们没有产生 rigidity。

所以 R7 的失败类型是：

\[
\boxed{
\textbf{independent mixed invariant, but no independent codimension gain.}
}
\]

---

# 23. R8 Attack Target

按 R7 kill criterion，R8 禁止继续：

- endpoint jumps；
- old ZGAP；
- radial gap；
- generic common-\(U\) spacing；
- “required jump 再 sharpen 一点”；
- Jacobsthal 作为 endpoint architecture 的补丁；
- prime-by-prime jump modulus 分解。

也不建议把 R8 定义成 common-scale coprime exclusion，因为 R7-PLCF 已证明在当前 PRE_ROOT endpoint information class 内：

\[
\exists U\in I_{23},
\qquad
\gcd(U,V)=1
\]

有无限 family。

因此 R8 必须寻找一个新的 mixed information class，且它必须**同时做到**：

1. 在 sphere/root 之前合法；
2. 读取 outer decimal base；
3. 读取 primitive fibre；
4. 排除 R7-PLCF 这类 common-scale/coprime PRE_ROOT states；
5. 不能退化成 FA/FB、ZGAP、radial gap 或 root residual。

建议将 R8 的 architecture target 写成：

\[
\boxed{
\textbf{Pre-Root Primitive Compatibility Beyond Common Scale}
\times
\textbf{Source-Projection Fibre Exclusion}
}
\]

也就是不再问：

\[
\text{“有没有 }U\text{？”}
\]

而问：

\[
\boxed{
\text{“在有 }U\text{ 且甚至 }\gcd(U,V)=1
\text{ 的 PRE_ROOT fibre 中，
还缺哪一个 genuinely primitive/source semantic gate？”}
}
\]

这正是 R7 之后剩下的最小 architecture question。

---

# Final Assessment

R6 找到 common-scale integer incidence 是 genuine source information loss，这一点没有被 R7 推翻。

R7 推翻的是另一件事：

\[
\boxed{
\text{endpoint modular phase并不是攻击这项 loss 的 universal rigidifier。}
}
\]

因为 J2-specific structure

\[
uq=G+1
\]

虽然确实给出 mixed modular relations，但没有把 \(C_2,C_3\) 锁到一个 thin cyclotomic image。

相反，PRE_ROOT fibre仍有足够自由，使：

\[
\delta_i/C_i
\]

跨越宽区间，而 required jump window经常覆盖整个 modulus。

最强的 exact negative theorem 是 R7-PLCF：

\[
\boxed{
\text{存在无限 PRE_ROOT J2 linear family，
common-scale 与 coprimality 同时成立。}
}
\]

所以本轮必须按既定纪律退休 endpoint architecture：

\[
\boxed{
\texttt{R7\_TERMINAL\_VERDICT=
ENDPOINT\_JUMP\_RIGIDITY\_ABSENT}.
}
\]

J2 仍 OPEN。
