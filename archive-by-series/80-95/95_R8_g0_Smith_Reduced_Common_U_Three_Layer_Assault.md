# 95-R8 — \(g=0\) Smith-Reduced Common-\(U\) Three-Layer Assault

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Ownership:** \(A_1^{95}=A_1\cap\{J\neq2\}\)  
**Round:** 95-R8  
**Main theatre:** \(\mathcal H_0\)  
**Required order:** Continuous Cone \(\to\) Integer Successor \(\to\) Positional Unit  
**Main archive:** `95_R8_g0_Smith_Reduced_Common_U_Three_Layer_Assault.md`

---

# Part I — Executive Verdict

本轮不能数学诚实地签发题设四个预设 machine verdict 中的任何一个：

```text
H0_CLOSED
H0_GLOBALLY_FINITE
H0_UNIT_SUCCESSOR_COMPRESSED
H0_THREE_LAYER_ARCHITECTURE_INSUFFICIENT
```

前三个没有被证明；第四个也要求证明 C/I/P 三层架构本身留下一个无法切割的大 moving family，而本轮并没有得到这种 architecture falsification。

因此本轮正式采用 provenance-safe verdict：

```text
H0_STATUS = OPEN_AT_INTEGER_SUCCESSOR
REQUESTED_ENUM_VERDICT = NOT_ISSUED
H0_DOMINANT_GATE = I
H0_DOMINANT_GATE_QUALIFIER = FRONTIER_DIAGNOSIS_NOT_GLOBAL_EXTINCTION_THEOREM
H0_LAYER_P_ACTIVATED = NO
H0_SET_LEVEL_CLOSURE = NO
H0_INFORMATION_GAIN = YES
```

核心结论分为六条。

1. \(g=0\) 的 exponent collapse 精确为
   \[
   \boxed{
   m_3=n_3,\qquad d=m_2,\qquad n_2=m_2+k,
   }
   \]
   **不**强迫 \(n_2=n_3\)。

2. H0 的 continuous cone 精确为
   \[
   \boxed{
   10^{m_2+k-m_3-1}
   <
   \frac MN
   <
   10^{m_2+k-m_3+1}.
   }
   \]
   所以“\(0.1<M/N<10\)”不是 H0 的全局形式。

3. “所有 H0 都在 Layer C 死亡”被 exact \(g=0\) regression 反例正式处决；同时历史 infinite pseudo-family 确实整体死在 C。

4. 现有所有恢复到的 non-\(J2\) \(g=0\) exact C-survivors 均死于 Layer I；历史定向 exact raw scans 也没有出现 \(I_1\)、\(I_{\ge2}\) 或 P witness。该事实只支持
   \[
   \boxed{\text{H0 的当前 dominant gate 是 I}}
   \]
   ，不等于全局 I-extinction theorem。

5. 本轮得到一个新的 H0 source-space compression。若 genuine H0 source candidate 落在 plus branch \(H<0\)，则
   \[
   \boxed{
   b_2\le10,\qquad k\le4,\qquad m_2\le2,\qquad n_2\le6,\qquad U<10^6.
   }
   \]
   更细地，若 \(b_1\ge3\)，则 \(k\le3\)。

6. 没有恢复到任何真正 H0 positional theorem
   \[
   U\equiv U_0\pmod D,\qquad D\mid V
   \]
   或 equivalent prime-cover theorem。因此 Layer P 不得被人为启动。

本轮最小 live frontier 是：

\[
\boxed{
\mathcal H_0^{\rm live}
=
\{\text{C-pass, I-not-yet-killed H0 states}\},
}
\]

其中 plus source-survivor 子类进一步满足上面的有限 \(b_2,k,U\) bounds；minus 子类仍是主要未解决部分。

---

# Part II — Frozen R7 Decision

R7 的正式判决冻结为：

```text
TRANSITION_AFFINE_BOUNDARY_BRIDGE_KILLED
CURRENT_TRANSITION_ARCHITECTURE = SATURATED
T0 = OPEN
T0_CURRENT_ARCHITECTURE = SATURATED
T1_TRANSFER_ACTIVATED = NO
```

R7 的关键 meta-result 是：

\[
\boxed{
\text{transition 中 algebraic bridge 存在，但 arithmetic novelty 为零。}
}
\]

所以 R8 不回 resonance，也不继续 sharpen transition AFF / headroom / cross determinant。

R8 的合法入口是 R7 选定的：

\[
\boxed{
\mathcal H_0:\quad g=0,\quad J\neq2.
}
\]

---

# Part III — H0 Canonical Definition

从 frozen A1 source state 恢复：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

指数定义：

\[
g=m_3-n_3\ge0,
\qquad
d=m_2-g,
\]

\[
m_2=g+d,
\qquad
n_2=2g+k+d,
\qquad
m_3=n_3+g,
\qquad k\ge1.
\]

H0 额外要求：

\[
\boxed{
g=0,\qquad J\neq2.
}
\]

Full Smith chart：

\[
b_1=s\alpha u,\qquad
b_2=s\alpha\beta t,\qquad
b_3=s\beta v,
\]

\[
\gcd(\alpha,\beta)=1,
\qquad
\gcd(u,\beta t)=1,
\qquad
\gcd(\alpha t,v)=1.
\]

写

\[
\gamma=\gcd(u,v),
\qquad
u=\gamma u_0,
\qquad
v=\gamma v_0,
\qquad
\gcd(u_0,v_0)=1.
\]

则

\[
V=s\alpha\beta\gamma u_0tv_0
=s\beta u_0v\alpha t.
\]

并有：

\[
g_2=u_0v,
\qquad
g_3=u_0\alpha t.
\]

取：

\[
P_2=vM,
\qquad
P_3=\alpha tN,
\qquad
u_0\mid M,N.
\]

因此：

\[
\boxed{
C_2=\frac M{u_0},
\qquad
C_3=\frac N{u_0}.
}
\]

original source candidate 需要真正的：

\[
U\in\mathbf Z_{>0},
\qquad
a_2=UC_2=\frac{UM}{u_0},
\qquad
a_3=UC_3=\frac{UN}{u_0},
\]

并且：

\[
\boxed{
\gcd(U,V)=1.
}
\]

因为 \(u_0\mid V\)：

\[
\boxed{
\gcd(U,u_0)=1.
}
\]

所以 \(U/u_0\) 已是 prescribed-denominator reduced fraction。

---

# Part IV — 95-R8-T1: \(g=0\) Exponent and Denominator-Sign Collapse

## T1(a) — Exponent collapse

由 \(g=0\)：

\[
m_3=n_3.
\]

又：

\[
d=m_2-g=m_2.
\]

并且：

\[
n_2=2g+k+d=k+m_2.
\]

故：

\[
\boxed{
m_3=n_3,\qquad
d=m_2,\qquad
n_2=m_2+k.
}
\tag{H0-EXP}
\]

这是 H0 的完整 direct exponent collapse。

特别：

\[
\boxed{
n_2-n_3=m_2+k-m_3
}
\]

仍可移动。

所以：

\[
\boxed{
g=0\not\Rightarrow n_2=n_3.
}
\]

历史 exact profile
\[
(m_2,m_3,n_3,k,n_2)=(1,1,1,1,2)
\]
已经是直接反例。

---

## T1(b) — Denominator resonance impossible in H0

定义 denominator remainder：

\[
R=b_2 10^{n_3}-b_3.
\]

在 H0：

\[
n_3=m_3.
\]

而 \(b_3\) 是 \(m_3\)-digit positive integer，所以：

\[
b_3<10^{m_3}=10^{n_3}.
\]

又 \(b_2\ge1\)，故：

\[
b_2 10^{n_3}\ge10^{n_3}>b_3.
\]

因此：

\[
\boxed{
R>0
}
\tag{H0-R+}
\]

对全部 H0 exact states 成立。

所以：

\[
\boxed{
g=0\Longrightarrow R\neq0.
}
\]

H0 与 exact denominator resonance \(R=0\) 不相交。

在 Smith-reduced notation 中：

\[
R=s\beta\widehat R,
\qquad
\widehat R=\alpha t10^{n_3}-v,
\]

故：

\[
\boxed{
\widehat R>0.
}
\]

---

## T1(c) — No resonance-specific \(u_0\) theorem imported

本轮**不**使用：

\[
u_0\mid10^g+1,
\]

因为该结论属于 resonance-specific applicability。

在 H0 没有恢复到一个合法 theorem 给出：

\[
u_0\mid2,
\qquad
u_0\in\{1,2\},
\]

或任何 absolute bound。

所以：

```text
H0_U0_ABSOLUTELY_BOUNDED = NOT_PROVED
RESONANCE_U0_THEOREM_IMPORTED = NO
```

---

# Part V — Full Smith/Common-\(U\) Reconstruction

H0 的 common-\(U\) interval 为：

\[
\boxed{
I_{23}
=
u_0
\left[
\max\left(
\frac{10^{n_2-1}}M,
\frac{10^{n_3-1}}N
\right),
\,
\min\left(
\frac{10^{n_2}}M,
\frac{10^{n_3}}N
\right)
\right).
}
\tag{I23}
\]

half-open convention 精确保持：

\[
I_{23}=[L,R).
\]

等价地：

\[
\boxed{
K_{MN}:=
\left[
\max\left(
\frac{10^{n_2-1}}M,
\frac{10^{n_3-1}}N
\right),
\,
\min\left(
\frac{10^{n_2}}M,
\frac{10^{n_3}}N
\right)
\right),
}
\]

并要求：

\[
\boxed{
\frac U{u_0}\in K_{MN}.
}
\]

source-level terminal condition：

\[
\boxed{
\exists U\in\mathbf Z_{>0}:
\frac U{u_0}\in K_{MN},
\quad
\gcd(U,s\beta u_0v\alpha t)=1.
}
\tag{H0-SRUS}
\]

这就是 H0 的完整 C/I/P semantic gate。

---

# Part VI — Layer C: Continuous Cone

## 95-R8-T2 — H0 Continuous Cone Criterion

定义：

\[
\rho
:=
\frac{C_2 10^{n_3}}{C_3 10^{n_2}}
=
\frac MN10^{n_3-n_2},
\]

\[
\tau:=\frac{10^{n_3}}{C_3}
=\frac{u_0 10^{n_3}}N.
\]

则：

\[
I_{23}
=
\tau J(\rho),
\]

其中：

\[
J(\rho)
=
\left[
\max\left(\frac1{10},\frac1{10\rho}\right),
\,
\min\left(1,\frac1\rho\right)
\right).
\]

直接比较 endpoints：

\[
J(\rho)\neq\varnothing
\iff
\frac1{10}<\rho<10.
\]

所以：

\[
\boxed{
I_{23}\neq\varnothing
\iff
10^{-1}
<
\frac MN10^{n_3-n_2}
<
10.
}
\]

等价于：

\[
\boxed{
10^{n_2-n_3-1}
<
\frac MN
<
10^{n_2-n_3+1}.
}
\tag{CONE-GEN}
\]

代入 H0 exponent collapse：

\[
n_2-n_3=m_2+k-m_3,
\]

得到：

\[
\boxed{
I_{23}\neq\varnothing
\iff
10^{m_2+k-m_3-1}
<
\frac MN
<
10^{m_2+k-m_3+1}.
}
\tag{H0-CONE}
\]

这是本轮 canonical H0 ratio theorem。

---

## 95-R8-T3 — Global Layer-C Exclusion is False

题设希望优先测试：

\[
\forall \mathcal H_0,\quad I_{23}=\varnothing.
\]

该命题被 exact H0 states 否定。

### Exact C-pass / I-fail state B

\[
(b_1,b_2,b_3)=(1,6,8),
\]

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445).
\]

其：

\[
V=24,
\qquad
(g_1,g_2,g_3)=(24,4,3),
\]

\[
(C_2,C_3)=(109,25),
\]

\[
(m_2,m_3,n_3,k,n_2)=(1,1,1,1,2).
\]

于是：

\[
I_{23}
=
\left[\frac{10}{109},\frac25\right),
\]

严格非空。

所以：

\[
\boxed{
\text{H0 Continuous Cone Exclusion is false.}
}
\]

### Exact C-pass / I-fail state E

\[
(b_1,b_2,b_3)=(5,5,1),
\]

\[
(P_1,P_2,P_3,Q_0)=(298,2514,1485,2935).
\]

有：

\[
V=5,
\qquad
(C_2,C_3)=(2514,297),
\]

\[
I_{23}
=
\left[\frac5{1257},\frac{10}{297}\right),
\]

亦非空。

因此：

```text
H0_T3_GLOBAL_C_EXCLUSION = DISPROVED
H0_RATIO_FINITE_CLASSES = NOT_OBTAINED
```

---

## Historical infinite Layer-C death remains valid

固定：

\[
(b_1,b_2,b_3)=(1,6,8)
\]

的 synchronized conic：

\[
1000x+10y+z=7q,
\]

\[
576x^2+16y^2+9z^2=q^2,
\]

对应：

\[
P=(24x,4y,3z).
\]

历史 explicit polynomial family满足：

\[
z>y.
\]

其 profile：

\[
n_2=2,\qquad n_3=1.
\]

所以：

\[
\rho=\frac{y}{10z}<\frac1{10}.
\]

因此整个 family：

\[
\boxed{
I_{23}=\varnothing.
}
\]

这证明了 Layer C 对一个 genuine infinite ambient synchronized family 的杀伤力，但不能推广成所有 H0。

---

## Layer-C width audit

当：

\[
10^{-1}<\rho\le1,
\]

有：

\[
|I_{23}|
=
\tau\left(1-\frac1{10\rho}\right).
\]

当：

\[
1\le\rho<10,
\]

有：

\[
|I_{23}|
=
\tau\left(\frac1\rho-\frac1{10}\right).
\]

现有 source geometry 不支持：

\[
\boxed{
|I_{23}|<1
}
\]

作为 global H0 theorem。

历史 C-pass H0 regressions均满足 width \(<1\)，但这是 evidence，不是证明。

所以：

```text
H0_WIDTH_LT_1 = OPEN
H0_UNIQUE_SUCCESSOR_GLOBAL = OPEN
```

---

# Part VII — Layer I: Integer Successor

只对 C-pass state 定义：

\[
L=
u_0
\max\left(
\frac{10^{n_2-1}}M,
\frac{10^{n_3-1}}N
\right),
\]

\[
R=
u_0
\min\left(
\frac{10^{n_2}}M,
\frac{10^{n_3}}N
\right).
\]

canonical successor：

\[
\boxed{
U_*=\lceil L\rceil.
}
\]

则：

\[
\boxed{
I_{23}\cap\mathbf Z_{>0}\neq\varnothing
\iff
U_*<R.
}
\tag{I-SUCC}
\]

若 \(|I_{23}|<1\)，则 \(U_*\) 是唯一 possible integer successor。

注意：\(U_*<R\) 只是 exact endpoint formulation；本身是 `NO_NEW_INFORMATION`。

---

## Immediate integer-core gate

任何 positive integer \(U\in I_{23}\) 必须满足：

\[
UC_2<10^{n_2},
\qquad
UC_3<10^{n_3}.
\]

由于 \(U\ge1\)：

\[
\boxed{
C_2<10^{n_2},
\qquad
C_3<10^{n_3}.
}
\tag{CORE-I}
\]

即：

\[
\boxed{
M<u_0 10^{n_2},
\qquad
N<u_0 10^{n_3}.
}
\tag{CORE-MN}
\]

这正是历史 H0 C-pass regressions死亡的最便宜 Layer-I reason。

例如 state B：

\[
C_2=109\ge100=10^{n_2},
\]

因此：

\[
R\le\frac{100}{109}<1,
\]

无 positive integer \(U\)。

state E：

\[
C_2=2514\ge100,
\]

同样直接 I_FAIL。

---

## Smith-reduced integer margin

定义：

\[
x_2=10^{n_2-1},
\qquad
x_3=10^{n_3-1}.
\]

### Face A

若：

\[
L_2\ge L_3,
\]

则 define：

\[
\mathcal G_A
:=
M10^{n_3}
-
N10^{n_2-1}.
\]

C-pass 需要：

\[
\mathcal G_A>0.
\]

若还存在 integer \(U\)，则 sharp integer margin 给：

\[
\boxed{
\mathcal G_A\ge M.
}
\tag{IRM-A}
\]

故：

\[
\boxed{
0<\mathcal G_A<M
\Longrightarrow
I_{23}\cap\mathbf Z_{>0}=\varnothing.
}
\]

### Face B

若：

\[
L_3>L_2,
\]

定义：

\[
\mathcal G_B
:=
N10^{n_2}
-
M10^{n_3-1}.
\]

integer feasibility 必须：

\[
\boxed{
\mathcal G_B\ge N.
}
\tag{IRM-B}
\]

故：

\[
\boxed{
0<\mathcal G_B<N
\Longrightarrow
I_{23}\cap\mathbf Z_{>0}=\varnothing.
}
\]

等号只能发生在 \(U=1\) 的 sharp boundary situation。

这是真正的 Layer-I arithmetic theorem，而不是 continuous cone 的重写。

---

## Endpoint Euclidean formulation

对 \(i=2,3\)：

\[
10^{n_i-1}
=
q_iC_i+r_i,
\qquad
0\le r_i<C_i.
\]

则：

\[
\boxed{
\left\lceil
\frac{10^{n_i-1}}{C_i}
\right\rceil
=
q_i+\mathbf 1_{r_i>0}.
}
\]

所以 active lower endpoint 一旦确定，successor 是普通 decimal-power modulo \(C_i\) 的 Euclidean jump。

这一层的关键不是再构造一个 affine equation，而是控制这个 exact jump 是否 overshoot inactive upper endpoint。

截至 R8：

```text
UNIFORM_H0_CEILING_JUMP = NOT_PROVED
```

---

# Part VIII — New H0 Source Compression on the Plus Branch

这是本轮真正的新 source-space reduction。

冻结 exact word：

\[
D=P_110^k-Q_0>0,
\]

\[
H=b_2Q_0-b_110^{m_2}D\neq0,
\]

以及 tail：

\[
10^{m_3}H
=
b_2P_210^{n_3}
-
b_3(Q_0-P_3).
\]

在 H0：

\[
m_3=n_3.
\]

所以定义：

\[
K_3
:=
\frac{b_3(Q_0-P_3)}{10^{n_3}}
\in\mathbf Z_{>0}.
\]

得到：

\[
\boxed{
b_2P_2=H+K_3.
}
\tag{H0-TAIL}
\]

又因为：

\[
b_3<10^{n_3},
\qquad
Q_0-P_3<Q_0,
\]

故：

\[
\boxed{
0<K_3<Q_0.
}
\tag{K3-Q}
\]

---

## 95-R8-T4(a) — H0 Plus Denominator Collapse

假设 plus：

\[
H<0.
\]

由 (H0-TAIL)：

\[
b_2P_2<K_3<Q_0.
\]

frozen global A1 axis theorem：

\[
\boxed{
P_2>\sqrt{\frac{24}{2525}}\,Q_0>\frac{Q_0}{11}.
}
\]

所以：

\[
b_2\frac{Q_0}{11}
<
b_2P_2
<
Q_0.
\]

因此：

\[
b_2<11.
\]

即：

\[
\boxed{
H<0,\ g=0
\Longrightarrow
b_2\le10.
}
\tag{H0-PLUS-B2}
\]

于是：

\[
\boxed{
m_2\le2.
}
\]

而且：

- \(1\le b_2\le9\Rightarrow m_2=1\)；
- \(b_2=10\Rightarrow m_2=2\)。

这不是 generic transition theorem；它使用了 \(g=0\) tail cancellation。

---

## 95-R8-T4(b) — H0 Plus Sign-to-Sphere Collapse

H0 已证明：

\[
R>0.
\]

plus 有：

\[
H<0.
\]

所以 \(H\) 与 \(R\) 异号。

Double-Smith affine sign theorem：

\[
S_3
=
\alpha JZ-M\widehat R,
\]

且：

\[
\operatorname{sgn}Z=\operatorname{sgn}H,
\qquad
\widehat R>0.
\]

于是：

\[
Z<0,\qquad
-M\widehat R<0,
\]

所以：

\[
\boxed{
S_3=P_2+P_3-Q_0<0.
}
\]

即：

\[
Q_0>P_2+P_3.
\]

平方并使用 sphere：

\[
Q_0^2
=
P_1^2+P_2^2+P_3^2,
\]

\[
Q_0^2>(P_2+P_3)^2
=
P_2^2+P_3^2+2P_2P_3.
\]

所以：

\[
\boxed{
P_1^2>2P_2P_3.
}
\tag{H0-PLUS-SPH}
\]

---

## 95-R8-T4(c) — H0 Plus \(k\)-Bound

令：

\[
c_0:=\sqrt{\frac{24}{2525}}.
\]

frozen source bounds：

\[
P_2>c_0Q_0,
\]

\[
\frac{P_1}{Q_0}
<
\left(1+\frac1{b_1}\right)10^{-k},
\]

以及 H0 decade ratio：

\[
\frac{P_2}{P_3}<10^{k+2}.
\]

最后一式等价于：

\[
\frac{P_3}{Q_0}
>
\frac{P_2/Q_0}{10^{k+2}}
>
c_0 10^{-k-2}.
\tag{P3-LOW}
\]

另一方面由 (H0-PLUS-SPH)：

\[
2P_2P_3<P_1^2.
\]

所以：

\[
\frac{P_3}{Q_0}
<
\frac{1}{2c_0}
\left(\frac{P_1}{Q_0}\right)^2
<
\frac{(1+1/b_1)^2}{2c_0}10^{-2k}.
\tag{P3-UP}
\]

联立：

\[
c_0 10^{-k-2}
<
\frac{(1+1/b_1)^2}{2c_0}10^{-2k}.
\]

因此：

\[
10^k
<
\frac{50(1+1/b_1)^2}{c_0^2}.
\]

因为：

\[
c_0^2=\frac{24}{2525},
\]

得到：

\[
\boxed{
10^k
<
\frac{126250}{24}
\left(1+\frac1{b_1}\right)^2.
}
\tag{H0-K-EXACT}
\]

对 \(b_1\ge1\)：

\[
\left(1+\frac1{b_1}\right)^2\le4,
\]

所以：

\[
10^k<\frac{505000}{24}<21042.
\]

故：

\[
\boxed{
k\le4.
}
\tag{H0-PLUS-K}
\]

若：

\[
b_1\ge3,
\]

则：

\[
\left(1+\frac1{b_1}\right)^2
\le\frac{16}{9},
\]

于是：

\[
10^k
<
\frac{2020000}{216}
<9352
<10^4,
\]

故：

\[
\boxed{
b_1\ge3\Longrightarrow k\le3.
}
\tag{H0-PLUS-K3}
\]

---

## 95-R8-T4(d) — Plus source scale is absolutely bounded

由：

\[
m_2\le2,
\qquad
k\le4,
\]

H0 exponent：

\[
n_2=m_2+k
\]

给：

\[
\boxed{
n_2\le6.
}
\]

若一个 genuine source candidate 真正通过 Layer I，则：

\[
a_2=UC_2<10^{n_2}.
\]

由于 \(C_2\ge1\)：

\[
U<10^{n_2}\le10^6.
\]

因此：

\[
\boxed{
g=0,\ H<0,\ \text{source survivor}
\Longrightarrow
U<10^6.
}
\tag{H0-PLUS-U}
\]

注意：

\[
U<10^6
\]

**不**意味着整个 plus H0 已 globally finite，因为 \(m_3=n_3\)、Smith profile、\(Q_0\) 等其他 coordinates 仍可移动。

所以：

```text
H0_PLUS_U_BOUNDED = PROVED
H0_PLUS_GLOBALLY_FINITE = NOT_PROVED
```

---

# Part IX — Layer P: Positional Unit Sieve

Layer P 只允许在：

\[
I_{23}\cap\mathbf Z_{>0}\neq\varnothing
\]

后启动。

canonical unit condition 是：

\[
\boxed{
\gcd(U,V)=1,
\qquad
V=s\beta u_0v\alpha t.
}
\tag{UNIT}
\]

等价的 H0-SRUS formulation：

\[
\boxed{
\frac U{u_0}\in K_{MN},
\qquad
\gcd(U,s\beta u_0v\alpha t)=1.
}
\]

---

## 95-R8-T5 — Positional Unit Theorem Status

本轮没有得到 global theorem：

\[
U\equiv U_0\pmod D,
\qquad
D\mid V,
\]

也没有得到：

\[
\forall U\in I_{23}\cap\mathbf Z,\quad \gcd(U,V)>1.
\]

所以：

```text
H0_POSITIONAL_UNIT_EXTINCTION = NOT_PROVED
H0_LAYER_P_WITNESS = NOT_RECOVERED
H0_JACOBSTHAL_ACTIVATED = NO
```

---

## Conditional saturated first-candidate sieve

若 Face A active lower endpoint saturated：

\[
C_2\mid10^{n_2-1},
\]

则：

\[
U_0=\frac{10^{n_2-1}}{C_2}\in\mathbf Z.
\]

若 \(p\in\{2,5\}\) 且：

\[
p\mid b_2,
\]

source reducedness：

\[
\gcd(C_2,b_2)=1
\]

给：

\[
p\nmid C_2.
\]

若 \(n_2\ge2\)，则：

\[
p\mid U_0.
\]

又 \(b_2\mid V\)，故：

\[
p\mid V.
\]

所以：

\[
\boxed{
\delta_2=0,\ n_2\ge2,\ p\mid\gcd(b_2,10)
\Longrightarrow
\gcd(U_0,V)>1.
}
\tag{SAT-P-A}
\]

Face B 对称。

但这只杀**第一 candidate**；saturated interval 可含 later candidates，所以不能冒充 chamber closure。

---

## \(U=1\) warning

若：

\[
U=1,
\]

则自动：

\[
\gcd(U,V)=1.
\]

所以 \(U=1\) 一旦进入 \(I_{23}\)，它不是 Layer-P target，而是 full radial/source survivor。

因此：

\[
\boxed{
\text{任何只依赖 }\gcd(U,V)\text{ 的 theorem 都不可能排除 }U=1.
}
\]

截至 R8：

```text
H0_U_EQ_1_GLOBAL_EXCLUSION = NOT_PROVED
```

---

# Part X — Historical Regression Replay

## Smith provenance for the principal \(g=0\) profile

对：

\[
(b_1,b_2,b_3)=(1,6,8),
\]

可取：

\[
s=1,\quad
\alpha=1,\quad
\beta=2,\quad
u=1,\quad
t=3,\quad
v=4.
\]

于是：

\[
u_0=1.
\]

在：

\[
m_3=1
\]

时：

\[
\delta_\beta=\gcd(2,10)=2,
\]

\[
\Lambda_\beta=10/2=5,
\]

\[
\delta_v=\gcd(4,5)=1,
\]

所以：

\[
\boxed{
J=5.
}
\]

因此这一整组 regression 属于 95 ownership，而不是 J2。

---

## Regression ledger

### State A — C_FAIL

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),
\]

\[
(C_2,C_3)=(13,53),
\]

\[
\rho=\frac{13}{530}<0.1.
\]

故：

\[
\boxed{C\_FAIL.}
\]

---

### State B — I_FAIL

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445),
\]

\[
(C_2,C_3)=(109,25),
\]

\[
\rho=\frac{109}{250}\in(0.1,10).
\]

\[
I_{23}
=
\left[
\frac{10}{109},\frac25
\right)
\subset(0,1).
\]

故：

\[
\boxed{I\_FAIL.}
\]

更便宜地：

\[
C_2=109\ge100=10^{n_2}.
\]

---

### State C — C_FAIL

\[
(P_1,P_2,P_3,Q_0)=(456,292,2907,2957),
\]

\[
(C_2,C_3)=(73,969),
\]

\[
\rho=\frac{73}{9690}<0.1.
\]

故：

\[
\boxed{C\_FAIL.}
\]

---

### State D — C_FAIL at exact boundary

\[
(P_1,P_2,P_3,Q_0)=(552,3796,2847,4777),
\]

\[
(C_2,C_3)=(949,949).
\]

因为：

\[
n_2=2,\quad n_3=1,
\]

有：

\[
\rho=\frac{949\cdot10}{949\cdot100}=\frac1{10}.
\]

这是 half-open cone 的 exact boundary：

\[
\boxed{C\_FAIL.}
\]

---

### State E — \(J=10\), I_FAIL

对：

\[
(b_1,b_2,b_3)=(5,5,1),
\]

Smith chart 可取：

\[
s=1,\quad\alpha=5,\quad\beta=1,\quad u=t=v=1,
\]

故 \(u_0=1\)。

在 \(m_3=1\)：

\[
J=10.
\]

所以同样属于 95。

exact state：

\[
(P_1,P_2,P_3,Q_0)=(298,2514,1485,2935),
\]

\[
(C_2,C_3)=(2514,297),
\]

\[
I_{23}
=
\left[
\frac5{1257},\frac{10}{297}
\right)
\subset(0,1).
\]

故：

\[
\boxed{I\_FAIL.}
\]

---

## Exact real-cone point — I_FAIL

历史 fixed synchronized conic 中有：

\[
(x,y,z,q)
=
(324,17813,2633,72109).
\]

对应：

\[
(P_1,P_2,P_3,Q_0)
=
(7776,71252,7899,72109),
\]

\[
(C_2,C_3)=(17813,2633).
\]

连续 cone 非空，但：

\[
I_{23}
=
\left[
\frac{10}{17813},
\frac{10}{2633}
\right)
\subset(0,1).
\]

故：

\[
\boxed{I\_FAIL.}
\]

这一点成功复现题设 Regression B。

---

## Infinite pseudo-family — C_FAIL

历史 explicit infinite \(g=0\) family 满足：

\[
C_3>C_2,
\qquad
n_2=2,\quad n_3=1.
\]

于是：

\[
\rho=\frac{C_2}{10C_3}<0.1.
\]

故 family 每一项均：

\[
\boxed{C\_FAIL.}
\]

这成功复现题设 Regression A。

---

# Part XI — Counterexample Ledger

| Conjecture | R8 verdict | Exact reason |
|---|---|---|
| \(g=0\Rightarrow n_2=n_3\) | **DISPROVED** | exact profile \(n_2=2,n_3=1\) |
| \(0.1<M/N<10\) is global H0 cone | **DISPROVED** | correct cone has factor \(10^{n_2-n_3}\) |
| \(I_{23}\) always empty | **DISPROVED** | states B/E and real-cone point |
| \(M/N\) always outside cone | **DISPROVED** | same witnesses |
| \(|I_{23}|<1\) globally | **OPEN** | true on known C-pass regressions, no theorem |
| \(\#(I_{23}\cap\mathbf Z)\le1\) globally | **OPEN** | no uniform width theorem |
| all integer successors are non-units | **OPEN / NO WITNESS** | no exact H0 I-survivor recovered |
| \(u_0\) is absolutely bounded in H0 | **NOT PROVED** | no provenance-safe theorem |
| H0 denominator resonance \(R=0\) can occur | **DISPROVED** | \(g=0\Rightarrow m_3=n_3\) and digit length gives \(R>0\) |
| RU-H supplies independent radial magnitude | **FAILED / OLD IDENTITY** | full Smith/MNZ reduces it to radial identity |
| generic Jacobsthal should be launched now | **REJECTED** | Layer P not activated |

---

# Part XII — H0 Three-Layer State Ledger

## Symbolic first-death partition

定义：

\[
\mathcal H_{0,C}
=
\{X\in\mathcal H_0:I_{23}(X)=\varnothing\}.
\]

定义：

\[
\mathcal H_{0,I}
=
\{X\in\mathcal H_0:
I_{23}(X)\neq\varnothing,\ 
I_{23}(X)\cap\mathbf Z_{>0}=\varnothing\}.
\]

定义：

\[
\mathcal H_{0,P}
=
\{X\in\mathcal H_0:
I_{23}(X)\cap\mathbf Z_{>0}\neq\varnothing,\ 
\forall U\in I_{23}(X)\cap\mathbf Z_{>0},\ \gcd(U,V)>1\}.
\]

定义：

\[
\mathcal H_0^{\rm live}
=
\{X\in\mathcal H_0:
\exists U\in I_{23}(X)\cap\mathbf Z_{>0},\ \gcd(U,V)=1\}.
\]

于是定义层面有 disjoint partition：

\[
\boxed{
\mathcal H_0
=
\mathcal H_{0,C}
\sqcup
\mathcal H_{0,I}
\sqcup
\mathcal H_{0,P}
\sqcup
\mathcal H_0^{\rm live}.
}
\tag{H0-PART}
\]

本轮**没有**证明最后一块为空。

---

## Recovered exact-state ledger

| State | \(J\) | C | I | P | Classification |
|---|---:|---|---|---|---|
| A: \((24,52,159,169)\) | 5 | fail | n/a | n/a | `C_FAIL` |
| B: \((48,436,75,445)\) | 5 | pass | fail | n/a | `I_FAIL` |
| C: \((456,292,2907,2957)\) | 5 | fail | n/a | n/a | `C_FAIL` |
| D: \((552,3796,2847,4777)\) | 5 | boundary fail | n/a | n/a | `C_FAIL` |
| E: \((298,2514,1485,2935)\) | 10 | pass | fail | n/a | `I_FAIL` |
| exact real-cone point | 5 | pass | fail | n/a | `I_FAIL` |
| infinite synchronized family | 5 | fail uniformly | n/a | n/a | `C_FAIL` |

没有 recovered exact row 到达 P。

---

## Historical exact finite scans

历史 exact raw-survivor campaign 已覆盖：

1. \(g=0,\ m_2=m_3=n_3=1\)，one-digit denominator blocks，\(k=1,2,3\)；
2. \(g=0,\ (m_2,n_3,k)=(2,1,1)\)；
3. \(g=0,\ (m_2,n_3,k)=(1,2,1)\)。

这些 finite slices 的 raw-possible boxes 具有 exact coverage theorem，因为：

\[
U\ge1
\Longrightarrow
C_2\le10^{n_2}-1,\quad C_3\le10^{n_3}-1.
\]

历史结果：

```text
I1_HITS = 0
I_GE_2_HITS = 0
P_HITS = 0
COPRIME_RADIAL_SURVIVORS = 0
```

这些只是上述 slices 的 deterministic finite certificates，不能提升为 global H0 theorem。

---

# Part XIII — Dominant Gate Diagnosis

Layer C 不能成为 global dominant closure gate，因为 exact C-survivors 存在。

Layer P 也不能成为当前 dominant gate，因为：

\[
\boxed{
\text{没有 recovered exact H0 state 进入 Layer P。}
}
\]

所有已恢复 C-survivors 都死于 I；历史有限 exact H0 scans 也没有发现 I-survivor。

所以当前最诚实的 diagnosis 是：

```text
H0_DOMINANT_GATE = I
H0_DOMINANT_GATE_QUALIFIER = EMPIRICALLY_AND_STRUCTURALLY_SUPPORTED_FRONTIER
GLOBAL_I_EXTINCTION = NOT_PROVED
```

本轮没有资格写：

\[
\mathcal H_0=\varnothing.
\]

---

# Part XIV — Information Independence and Cross-Theatre Transfer Audit

## NO_NEW_INFORMATION

以下对象本身不算新 codimension：

1. \(I_{23}\) 的定义；
2. cone criterion 的纯 endpoint 重写；
3. \(U_*=\lceil L\rceil\)；
4. \(\gcd(U,V)=1\) 的重复陈述；
5. Full Smith factorization identity；
6. RU-H 在 full Smith/MNZ 下的闭环恒等化。

---

## Genuine information reductions

### G1 — \(g=0\) denominator-sign collapse

\[
\boxed{R>0}
\]

把 H0 永久从 denominator resonance 删除。

### G2 — Sharp Layer-I integer margins

\[
\mathcal G_A\ge M
\quad\text{or}\quad
\mathcal G_B\ge N
\]

是 continuous cone 之外的真实 arithmetic condition。

### G3 — H0 plus source compression

\[
\boxed{
H<0
\Longrightarrow
b_2\le10,\ k\le4,\ n_2\le6,
}
\]

并对 source survivor：

\[
\boxed{U<10^6.}
\]

这是本轮最主要的 NEW_INFORMATION。

---

## Cross-theatre transfer value

G1 依赖 \(g=0\)，不能直接 transfer 到 resonance / transition。

G2 本来就是 generic Smith/common-\(U\) asset，不是 R8 新发现。

G3 同时使用：

- \(g=0\) tail cancellation；
- \(R>0\)；
- global \(P_2\)-axis theorem；
- H0 decade ratio。

所以它不是一个可无条件 transfer 的 transition/resonance theorem。

本轮没有得到真正的 positional common-\(U\) congruence：

\[
U\equiv U_0\pmod D.
\]

因此：

```text
CROSS_THEATRE_POSITIONAL_THEOREM = NO
R9_PATH_D_ACTIVATED = NO
```

---

# Part XV — Updated 95 Frontier and R9 Launch Decision

R8 没有 set-level 删除 \(\mathcal H_0\)。

所以 95 live frontier 仍为：

\[
\boxed{
\begin{aligned}
A_1^{95,\mathrm{live}}
={}&
\mathcal H_0
\sqcup
\mathcal H_R^{\rm gen}
\sqcup
\mathcal H_{5,1}
\sqcup
\mathcal H_{5,2}^{-}
\sqcup
\mathcal H_{5,3}^{-}\\
&\sqcup
\mathcal H_{T0}
\sqcup
\mathcal H_{T1}
\sqcup
\mathcal H_{O+}
\sqcup
\mathcal H_{O-}.
\end{aligned}
}
\]

其中：

```text
H0 = OPEN_AT_INTEGER_SUCCESSOR
T0 = OPEN_BUT_ARCHITECTURE_FROZEN
T1 = FROZEN
```

---

## 95-R8 theorem ledger

### 95-R8-T1 — \(g=0\) Exponent and Denominator-Sign Collapse

```text
STATUS = PROVED
```

\[
m_3=n_3,\qquad d=m_2,\qquad n_2=m_2+k,
\qquad R>0.
\]

### 95-R8-T2 — H0 Continuous Cone Criterion

```text
STATUS = PROVED
```

\[
I_{23}\neq\varnothing
\iff
10^{m_2+k-m_3-1}
<
M/N
<
10^{m_2+k-m_3+1}.
\]

### 95-R8-T3 — H0 Continuous Exclusion / Compression

```text
GLOBAL_C_EXCLUSION = DISPROVED
FINITE_RATIO_CLASSES = NOT_OBTAINED
INFINITE_C_DEATH_FAMILY = REPLAYED
```

### 95-R8-T4 — H0 Integer Successor Theorem

```text
SHARP_INTEGER_MARGIN = FROZEN_AND_REPLAYED
UNIFORM_UNIQUE_SUCCESSOR = NOT_PROVED
NEW_H0_PLUS_COMPRESSION = PROVED
```

\[
H<0
\Longrightarrow
b_2\le10,\ k\le4,\ n_2\le6,
\]

且 genuine source survivor：

\[
U<10^6.
\]

### 95-R8-T5 — H0 Positional Unit Theorem

```text
GLOBAL_POSITIONAL_UNIT_THEOREM = NOT_PROVED
SATURATED_FIRST_CANDIDATE_FILTER = AVAILABLE_CONDITIONALLY
LAYER_P_WITNESS = NONE_RECOVERED
```

### 95-R8-T6 — H0 Extinction / Minimal Survivor

```text
H0_EXTINCTION = NOT_PROVED
H0_MINIMAL_FRONTIER = C_PASS + INTEGER_SUCCESSOR_GATE
H0_DOMINANT_GATE = I
```

---

## R9 launch decision

题设允许：

### Path A — H0 terminal finite certificate

当前不合法，因为 H0 尚未 globally finite。

### Path B — H0 positional-unit second-stage

当前不应启动，因为尚无 genuine H0 I-survivor；直接进入 P 会违反本轮 C \(\to\) I \(\to\) P discipline。

### Path D — new cross-theatre common-\(U\) invariant

当前不合法，因为本轮没有产生 transferable positional theorem。

因此 R9 选择：

\[
\boxed{
\textbf{Path C — }\mathcal H_{O+}\textbf{ assault}.
}
\]

理由不是放弃 H0，而是：

\[
\boxed{
\textbf{H0 当前已被压到真正的 integer-successor frontier，
但尚缺足够新信息把 I gate 关闭或合法激活 P。}
}
\]

继续在同一信息类中反复重写 endpoint/floor 将有高 redundancy risk。

因此冻结：

```text
R9_PATH = C_OUTER_PLUS
H0 = OPEN_AT_I_AND_FROZEN_FOR_NEW_INFORMATION
T0 = ARCHITECTURE_FROZEN
T1 = FROZEN
```

---

# Provenance / Frozen Inputs

本报告只使用并重组以下已归档资产：

- `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
- `95_R7_Transition_Source_Boundary_Bridge_Repair_or_Kill.md`
- `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`
- `strict_layer_A1_SRCU_state_after_campaign.md`
- `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`
- `strict_layer_A1_endpoint_quotient_integer_alignment_campaign.md`
- `strict_layer_A1_RU_H_first_candidate_excess_campaign.md`
- `strict_layer_A1_moving_profile_coprime_integer_scale_campaign.md`
- `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`
- `strict_layer_A1_SRCU_regression.py`
- `strict_layer_A1_radial_gate_scan_output.txt`

J2-only theorems没有用于 H0 证明。

---

# Final One-Line Verdict

\[
\boxed{
\textbf{R8 falsified global Layer-C extinction, recovered H0 exactly at the source gate, proved a new plus-branch }(b_2,k,U)\textbf{ compression, and located the honest global frontier at Integer Successor; Layer P remains unactivated.}
}
\]
