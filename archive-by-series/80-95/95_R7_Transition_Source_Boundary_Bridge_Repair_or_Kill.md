# 95-R7 — Transition Source-Boundary Bridge Repair-or-Kill

**文件名：** `95_R7_Transition_Source_Boundary_Bridge_Repair_or_Kill.md`  
**项目：** 三项十进制拼接平方和问题  
**层级：** Strict Layer — \(A_1\)-only  
**95 责任区：**
\[
A_1^{95}=A_1\cap\{J\neq2\}.
\]
**本轮主战区：**
\[
\mathcal H_{T0}.
\]
**继承：** 95-R1--R6  
**本轮性质：** Transition Source-Boundary Bridge Repair-or-Kill

---

# Part I — Executive Verdict

```text
TRANSITION_AFFINE_BOUNDARY_BRIDGE_KILLED

T0_CLOSED=NO
T0_GLOBAL_HEADROOM_FINITEIZATION=NO
GENUINE_AFFINE_BOUNDARY_BRIDGE=NO
ALGEBRAIC_AFFINE_BOUNDARY_BRIDGES=YES
ARITHMETIC_NOVELTY_FROM_THOSE_BRIDGES=NO

TRANSITION_AFFINE_TO_SOURCE_BOUNDARY_BRIDGE=NO
BRIDGE_EXISTS_BUT_NO_NEW_ARITHMETIC_INFORMATION=YES
CURRENT_TRANSITION_ARCHITECTURE=SATURATED

T1_TRANSFER_ACTIVATED=NO
R8_PATH=E_H0_ASSAULT
```

本轮达到用户定义的：

\[
\boxed{\textbf{Level D — Kill}.}
\]

更精确地说，本轮确实能够把

\[
S_3=\alpha Jh_T^\sharp q-M\widehat R
\]

与 actual numerator headroom

\[
B_B=10^{n_2}-\frac{UM}{u_0},
\qquad
B_A=10^{n_3}-\frac{UN}{u_0}
\]

写进同一个 exact equation；但所有最自然的 Face B / Face A mixed equations 在把 frozen definitions 代回后都发生**完全消去**：

\[
\boxed{
\text{mixed affine/headroom identity}
\quad\Longrightarrow\quad
\text{headroom definition itself}.
}
\]

因此 R7 的主判决不是“桥完全写不出来”，而是：

\[
\boxed{
\textbf{代数桥存在，但没有第二个 arithmetic codimension。}
}
\]

本轮进一步证明一个更强的结构性事实：若把 T0 affine structural state 视为已冻结系数层，则单独一面的 headroom equation 在消去 common-\(U\) 后，对该 headroom **不产生任何非零 algebraic elimination relation**；同时保留两面时，唯一新增 elimination relation 是旧的 source-only two-headroom/slack identity

\[
\boxed{
NB_B-MB_A
=
N10^{n_2}-M10^{n_3}.
}
\tag{R7-2H}
\]

它不含 \(\widehat R,S_3,H,q\)，因此不是 affine-to-boundary bridge。

故：

\[
\boxed{
\textbf{R6 找到的 affine source datum 与 actual source boundary
在当前 architecture 下仍是 arithmetic-independent information classes。}
}
\]

这正式处决：

```text
T0_AFFINE_HEADROOM_DIRECT_ELIMINATION
T0_AFFINE_HEADROOM_DIVISOR_EXTRACTION
T0_AFFINE_HEADROOM_CROSS_DETERMINANT_NONHIT
T0_TWO_HEADROOM_FINITEIZATION
```

作为当前架构的 uniform closure 路线。

---

# Part II — Frozen R6 Architecture

本轮精确继承 R6，不重开其已榨干对象。

## 2.1 T0 state

\[
\boxed{
g\ge1,\qquad
d=0,\qquad
R\neq0,\qquad
J\neq2.
}
\]

指数骨架：

\[
\boxed{
m_2=g,\qquad
n_2=2g+k,\qquad
m_3=n_3+g.
}
\]

特别注意：

\[
\boxed{
n_3
}
\]

仍是独立 moving decimal depth；当前没有 theorem 给出

\[
n_2-n_3=\text{constant}.
\]

所以 R7 不允许人为把两 headrooms 放到同一个固定十进制深度。

## 2.2 Full Smith state

\[
b_1=s\alpha u,\qquad
b_2=s\alpha\beta t,\qquad
b_3=s\beta v,
\]

\[
\gcd(\alpha,\beta)=1,\qquad
\gcd(u,\beta t)=1,\qquad
\gcd(\alpha t,v)=1.
\]

定义：

\[
\boxed{
\widehat R=\alpha t10^{n_3}-v\neq0,
}
\]

\[
R=s\beta\widehat R.
\]

并有：

\[
\boxed{
\gcd(\widehat R,\alpha t)=1,
}
\]

\[
\boxed{
\gcd(\widehat R,v)=\gcd(10^{n_3},v).
}
\]

primitive Smith coordinates：

\[
\boxed{
P_2=vM,\qquad
P_3=\alpha tN.
}
\]

## 2.3 Double Smith–Euclidean defect

存在 \(Z\neq0\)：

\[
\boxed{
tM10^{n_3}-A_3=JZ,
\qquad
A_3=\frac{Q_0-P_3}{\alpha},
}
\]

\[
\boxed{
H=s\alpha\beta^\sharp v^\sharp Z.
}
\]

定义：

\[
h_T=\gcd(tM,A_3),
\qquad
h_T^\sharp=\frac{h_T}{\gcd(h_T,J)},
\]

则：

\[
h_T^\sharp\mid Z,
\qquad
Z=h_T^\sharp q.
\]

为压缩记号，本轮令：

\[
\boxed{
E:=\alpha JZ
=\alpha Jh_T^\sharp q.
}
\tag{EDEF}
\]

## 2.4 Frozen AFF / T0-Q

R6 已冻结：

\[
\boxed{
S_3=E-M\widehat R.
}
\tag{AFF}
\]

并且：

\[
\boxed{
Q_0=\alpha t(M10^{n_3}+N)-E.
}
\tag{T0-Q}
\]

等价地：

\[
\boxed{
Q_0+E=\alpha t(M10^{n_3}+N).
}
\tag{QE}
\]

R6 已证明 AFF 与 T0-Q 是同一 affine information class 的两种坐标化，不能把二者虚构成两个独立方程。

## 2.5 Finite borrow

T0 四 chamber：

| chamber | sign \(H\) | sign \(R\) | carry label | AFF type |
|---|---:|---:|---:|---|
| T0-P+ | \(-\) | \(+\) | \(c=0\) | sign-mismatch / sum |
| T0-P- | \(-\) | \(-\) | \(c=0\) | cancellation |
| T0-M+ | \(+\) | \(+\) | \(c=1\) | cancellation |
| T0-M- | \(+\) | \(-\) | \(c=1\) | sign-mismatch / sum |

且：

\[
\text{plus}:\ -Q_0<H<0,
\qquad
\text{minus}:\ 0<H<Q_0.
\]

sign-mismatch 中：

\[
\boxed{
|S_3|
=
|E|+M|\widehat R|
\ge \alpha J+M.
}
\]

这些仍可作为 auxiliary size input，但 R7 不再 sharpen 它们。

## 2.6 Affine gcd-gap permanently frozen

\[
\Lambda_{\rm aff}
=
\gcd(|E|,|M\widehat R|).
\]

已有：

\[
\Lambda_{\rm aff}\mid S_3.
\]

因此：

\[
S_3\neq0
\Longrightarrow
|S_3|\ge\Lambda_{\rm aff}.
\]

没有

\[
0<|S_3|<\Lambda_{\rm aff}
\]

的空间。

本轮不再研究 \(\Lambda_{\rm aff}\) 本身。

---

# Part III — Source Headroom Definitions

Full Smith–Radial Cancellation 给：

\[
g_2=u_0v,\qquad
g_3=u_0\alpha t,
\]

\[
\boxed{
C_2=\frac{M}{u_0},
\qquad
C_3=\frac{N}{u_0},
\qquad
u_0\mid M,N.
}
\]

actual common-\(U\) recovery：

\[
\boxed{
a_2=UC_2=\frac{UM}{u_0},
\qquad
a_3=UC_3=\frac{UN}{u_0},
}
\]

且：

\[
\boxed{
\gcd(U,V)=1,
\qquad
V=s\beta u_0v\alpha t.
}
\]

因为 \(u_0\mid V\)：

\[
\boxed{
\gcd(U,u_0)=1.
}
\]

## 3.1 Face B headroom

\[
\boxed{
B_B
:=
10^{n_2}-a_2
=
10^{n_2}-UC_2
=
10^{n_2}-\frac{UM}{u_0}.
}
\tag{HB}
\]

即：

\[
\boxed{
u_0B_B=u_010^{n_2}-UM.
}
\tag{HB-u}
\]

合法 source：

\[
\boxed{
B_B\in\mathbb Z_{\ge1}.
}
\]

## 3.2 Face A headroom

\[
\boxed{
B_A
:=
10^{n_3}-a_3
=
10^{n_3}-UC_3
=
10^{n_3}-\frac{UN}{u_0}.
}
\tag{HA}
\]

即：

\[
\boxed{
u_0B_A=u_010^{n_3}-UN.
}
\tag{HA-u}
\]

合法 source：

\[
\boxed{
B_A\in\mathbb Z_{\ge1}.
}
\]

## 3.3 First strategic correction

这两个对象并非 R7 首次出现的新 source variable。

它们正是 common-\(U\) upper-endpoint slack 的 normalized version：

\[
E_2^+=u_0B_B,
\qquad
E_3^+=u_0B_A.
\]

因此：

\[
\boxed{
\textbf{headroom exactization = source semantics recovery，}
}
\]

但：

\[
\boxed{
\textbf{headroom existence itself不增加 information dimension。}
}
\]

R7 真正需要的是 transition affine datum 对 \(B_A,B_B\) 的**额外** arithmetic law。

这完成：

\[
\boxed{
\textbf{95-R7-T1 — Source Headroom Exactization}.
}
\]

**Status:** PROVED / HISTORICALLY IDENTIFIED WITH ENDPOINT SLACK.

---

# Part IV — Face B Bridge Assault

Face B 是本轮 70% 主预算，因为 AFF 显式含 \(M\)。

令：

\[
T_2:=10^{n_2}.
\]

由：

\[
u_0B_B=u_0T_2-UM
\]

得：

\[
UM=u_0(T_2-B_B).
\tag{B-M}
\]

AFF：

\[
S_3=E-M\widehat R.
\]

乘 \(U\)：

\[
US_3=UE-UM\widehat R.
\]

代入 (B-M)：

\[
US_3
=
UE-u_0(T_2-B_B)\widehat R.
\]

整理：

\[
\boxed{
u_0\widehat R B_B
=
US_3-UE+u_0T_2\widehat R.
}
\tag{B-BRIDGE}
\]

这正是 R7 prompt 期待的 prototype：

\[
\boxed{
\text{headroom}\times\text{nonzero remainder}
=
\text{affine/source integer combination}.
}
\]

然而把 AFF 重新代回：

\[
S_3-E=-M\widehat R.
\]

所以 (B-BRIDGE) 右侧：

\[
U(S_3-E)+u_0T_2\widehat R
=
-UM\widehat R+u_0T_2\widehat R
\]

即：

\[
\widehat R(u_0T_2-UM).
\]

因此：

\[
u_0\widehat R B_B
=
\widehat R(u_0T_2-UM).
\]

T0 有：

\[
\widehat R\neq0.
\]

在整数环中约掉 \(\widehat R\)：

\[
\boxed{
u_0B_B=u_0T_2-UM,
}
\]

恰好回到 (HB-u)。

所以：

```text
FACE_B_BRIDGE = ALGEBRAIC_BRIDGE_ONLY
FACE_B_NEW_ARITHMETIC_LATTICE = NO
FACE_B_SECOND_CODIMENSION = NO
```

## 4.1 Face B Cancellation Lemma

### 95-R7-T2B — Exact Face-B Bridge Collapse

在 T0 中，任何通过

\[
\text{AFF}
+
\text{Face-B headroom definition}
\]

直接消去 \(M\) 得到的 canonical linear bridge

\[
u_0\widehat R B_B
=
US_3-UE+u_0T_2\widehat R
\]

在利用 \(\widehat R\neq0\) 后严格等价于 headroom definition。

因此它不产生：

- 新整除；
- 新 residue；
- 新 lattice spacing；
- 新 size inequality；
- 新 source replay gate。

\[
\boxed{\square}
\]

## 4.2 Why divisibility extraction fails

若试图从 (B-BRIDGE) 找 \(D_T\mid B_B\)，自然 structural factors 只能来自：

\[
E,\quad
M\widehat R,\quad
S_3,\quad
\widehat R.
\]

但桥式本身可化为：

\[
u_0\widehat R B_B
=
\widehat R(u_0T_2-UM).
\]

所有由 \(\widehat R\) 带入的 divisor 同时出现在 \(B_B\) 的系数上，因此不能用

\[
\gcd(D_T,u_0\widehat R)=1
\]

剥离。

若 divisor 来自：

\[
\Lambda_{\rm aff}=\gcd(E,M\widehat R),
\]

则 \(\Lambda_{\rm aff}\mid E\)，因此后面构造的 cross-determinant 中它同样首先加载在 headroom coefficient \(E\) 上，而不是加载到 \(B_B\) 本身。

这称为：

\[
\boxed{
\textbf{Affine Divisor Coefficient Absorption}.
}
\]

它是 R7 的核心负结果之一。

---

# Part V — Face A Bridge Assault

Face A 使用 \(N\) 与 T0-Q。

令：

\[
T_3:=10^{n_3}.
\]

由：

\[
u_0B_A=u_0T_3-UN
\]

得：

\[
UN=u_0(T_3-B_A).
\tag{A-N}
\]

T0-Q：

\[
Q_0+E=\alpha t(MT_3+N).
\]

乘 \(U\)：

\[
UQ_0+UE
=
U\alpha tMT_3
+
\alpha tUN.
\]

代入 (A-N)：

\[
UQ_0+UE
=
U\alpha tMT_3
+
\alpha t u_0(T_3-B_A).
\]

整理：

\[
\boxed{
\alpha t\,u_0B_A
=
U\alpha tMT_3
+
\alpha t\,u_0T_3
-
UE
-
UQ_0.
}
\tag{A-BRIDGE}
\]

再代：

\[
Q_0+E=\alpha t(MT_3+N),
\]

右侧变为：

\[
\alpha t\bigl(u_0T_3-UN\bigr).
\]

约掉正整数 \(\alpha t\)：

\[
\boxed{
u_0B_A=u_0T_3-UN.
}
\]

恰回到 (HA-u)。

所以：

```text
FACE_A_BRIDGE = ALGEBRAIC_BRIDGE_ONLY
FACE_A_NEW_ARITHMETIC_LATTICE = NO
FACE_A_SECOND_CODIMENSION = NO
```

## 5.1 Face A is not rescued by T0-Q

虽然 Face A 不与 AFF 的 \(M\widehat R\) 项直接共享 \(N\)，但 T0-Q 显式含 \(N\)。

这只意味着可以写出另一条 mixed identity；它仍然完全消去。

因此本轮纠正一个可能的战略误觉：

\[
\boxed{
\textbf{Face B 在 syntactic variable-sharing 上更直接，}
}
\]

但：

\[
\boxed{
\textbf{在 arithmetic novelty 上并不比 Face A 更强。}
}
\]

两面均 collapse to definition。

---

# Part VI — Two-Headroom Elimination

两式：

\[
B_B=T_2-UC_2,
\]

\[
B_A=T_3-UC_3.
\]

消去 \(U\)：

\[
C_3(T_2-B_B)=C_2(T_3-B_A).
\]

整理：

\[
\boxed{
C_2B_A-C_3B_B
=
C_2T_3-C_3T_2.
}
\tag{2H-C}
\]

乘 \(u_0\)，使用

\[
M=u_0C_2,
\qquad
N=u_0C_3,
\]

得到：

\[
\boxed{
MB_A-NB_B
=
M10^{n_3}-N10^{n_2}.
}
\tag{2H-1}
\]

等价地：

\[
\boxed{
NB_B-MB_A
=
N10^{n_2}-M10^{n_3}.
}
\tag{2H-2}
\]

定义：

\[
\Omega:=N10^{n_2}-M10^{n_3},
\]

则：

\[
\boxed{
NB_B-MB_A=\Omega.
}
\tag{SLACK-2H}
\]

这就是旧 common-\(U\) slack identity 的 normalized form。

关键点：

\[
\boxed{
\text{右侧只读取 }(M,N,n_2,n_3),
}
\]

不读取：

\[
\widehat R,\quad
S_3,\quad
H,\quad
q,\quad
E.
\]

因此：

```text
TWO_HEADROOM_IDENTITY = GENUINE_SOURCE_RELATION
AFFINE_TO_BOUNDARY_BRIDGE = NO
NEW_FOR_R7 = NO
GLOBAL_FINITEIZATION = NO
```

## 6.1 Why it cannot finiteize both heads

固定 \(C_2,C_3,T_2,T_3\) 时：

\[
(B_B,B_A)
=
(T_2,T_3)-U(C_2,C_3).
\]

所以两 headrooms 沿一条 integral affine line 随 \(U\) 移动。

若 common-\(U\) interval 含 \(L\) 个 admissible integers，则至少在 source-only 层可以有 \(O(L)\) 个不同 headroom pairs。

当前没有 uniform bound：

\[
L=O(1).
\]

所以一条 two-headroom linear relation只把两个坐标恢复为原本同一个 common-\(U\) 参数，并没有产生新的绝对有限化。

---

# Part VII — Divisibility Extraction

本节专门检查：

\[
D_T\mid B_T.
\]

## 7.1 Source-only decimal divisor

由：

\[
B_B=T_2-UC_2
\]

立即有：

\[
\boxed{
\gcd(C_2,T_2)\mid B_B.
}
\tag{DEC-B}
\]

同理：

\[
\boxed{
\gcd(C_3,T_3)\mid B_A.
}
\tag{DEC-A}
\]

这是真整除，但：

1. 不使用 AFF；
2. 不使用 \(R\neq0\)；
3. 正是 endpoint reduction/Farey layer 已经读取的 decimal gcd；
4. 该 gcd 可等于 \(1\)；
5. 没有 uniform
   \[
   1\le B_i<\gcd(C_i,T_i).
   \]

所以：

```text
DECIMAL_HEADROOM_DIVISOR = TRUE
VERDICT = REDUNDANT_SOURCE_ONLY
```

## 7.2 Natural affine divisor fails to transfer

令：

\[
\Lambda_{\rm aff}=\gcd(E,M\widehat R).
\]

它满足：

\[
\Lambda_{\rm aff}\mid S_3.
\]

但 Face B bridge collapse 后：

\[
u_0\widehat RB_B
=
\widehat R(u_0T_2-UM).
\]

\(\Lambda_{\rm aff}\) 的 \(\widehat R\)-part 直接被 coefficient 吸收；其 \(E\)-part也没有独立进入右侧 source slack。

因此 current data 不给：

\[
\Lambda_{\rm aff}'\mid B_B
\]

其中 \(\Lambda_{\rm aff}'>1\) 且与 \(u_0\widehat R\) uniformly coprime。

Face A 同理。

## 7.3 Unit condition does not fix a residue

\[
\gcd(U,V)=1
\]

只说明 \(U\) 是模 \(V\) 的 unit。

若 \(D\mid V\)，则：

\[
U\in(\mathbb Z/D\mathbb Z)^\times,
\]

但 current source 没有 theorem 固定：

\[
U\equiv u_*(D)\pmod D.
\]

而：

\[
B_B\equiv T_2-UC_2\pmod D.
\]

因此“\(U\) 是 unit”本身不推出：

\[
D\mid B_B.
\]

若 \(D\nmid V\)，则 \(\gcd(U,V)=1\) 对 \(U\bmod D\) 更没有约束。

所以 current Layer-P information 也不能修复 divisor bridge。

## 7.4 \(2\times5\)-adic audit

R6 已证明 finite borrow 不锁死：

\[
v_2(\widehat R),
\qquad
v_5(\widehat R).
\]

本轮只允许其作为 coefficient peeling tool。

但 Face B 的 coefficient 是：

\[
u_0\widehat R.
\]

任何从 \(\widehat R\) 本身得到的 \(2/5\)-factor首先落在这个 coefficient 中；没有 independent right-side divisor 可以与之 coprime。

因此：

```text
BACKWARD_2x5_HEADROOM_PEELING = NO_NEW_DIVISOR
```

## 7.5 Divisibility verdict

本轮没有得到：

\[
\boxed{
D_T>1,\quad D_T\mid B_A
}
\]

或：

\[
\boxed{
D_T>1,\quad D_T\mid B_B
}
\]

其中 \(D_T\) genuinely 来自 transition AFF/source structure 且具有 uniform oversize potential。

所以：

\[
\boxed{
\textbf{95-R7-T4 — Headroom Divisibility / Finiteization Lemma}
}
\]

的正向目标失败。

准确状态：

```text
AFFINE_FORCED_HEADROOM_DIVISOR = NO
SOURCE_ONLY_DECIMAL_DIVISOR = YES_BUT_REDUNDANT
```

---

# Part VIII — Cross-Determinant Audit

自然比较：

\[
\frac{M\widehat R}{E}
\]

与 Face B source occupancy：

\[
\frac{UC_2}{T_2}
=
1-\frac{B_B}{T_2}.
\]

定义：

\[
D_{\times,B}
:=
T_2M\widehat R-EUC_2.
\]

使用：

\[
M\widehat R=E-S_3,
\qquad
UC_2=T_2-B_B,
\]

得到：

\[
\boxed{
D_{\times,B}
=
EB_B-T_2S_3.
}
\tag{CROSS-B}
\]

这是 nontrivial integer cross-product。

同理，若把同一 affine ratio 与 third numerator occupancy比较：

\[
D_{\times,A}
:=
T_3M\widehat R-EUC_3,
\]

则：

\[
\boxed{
D_{\times,A}
=
EB_A-T_3S_3.
}
\tag{CROSS-A}
\]

## 8.1 Independence audit

这些式子不是“等于 \(S_3\)”的简单复写；但它们仍完全由：

- AFF；
- headroom definition；

机械产生。

例如：

\[
EB_B-T_2S_3
=
E(T_2-UC_2)-T_2(E-M\widehat R).
\]

故：

\[
D_{\times,B}
=
T_2M\widehat R-EUC_2.
\]

没有第三条 source equation参与。

所以：

```text
CROSS_B = DEPENDENT_CROSS_PRODUCT
CROSS_A = DEPENDENT_CROSS_PRODUCT
```

## 8.2 Natural spacing is poisoned by coefficient sharing

\[
\Lambda_{\rm aff}
=
\gcd(E,M\widehat R)
\]

自动满足：

\[
\Lambda_{\rm aff}\mid D_{\times,B},
\qquad
\Lambda_{\rm aff}\mid D_{\times,A}
\]

只要相应 integrality成立。

但这个“新 spacing”没有 closure 力，因为：

- \(\Lambda_{\rm aff}\mid E\)；
- headroom 在 cross equation 中恰被 \(E\) 乘着；
- 因而不能从
  \[
  \Lambda_{\rm aff}\mid EB_i
  \]
  剥出
  \[
  \Lambda_{\rm aff}\mid B_i.
  \]

同时没有 uniform size theorem 给：

\[
0<|D_{\times,i}|<\Lambda_{\rm aff}.
\]

事实上现有 bounds 只允许它处于 moving scale：

\[
|D_{\times,i}|
\lesssim
|E|\,10^{n_i}+|S_3|\,10^{n_i},
\]

而 \(n_i,Q_0,E,S_3\) 均可移动。

故：

```text
CROSS_DETERMINANT_INTEGER = YES
CROSS_DETERMINANT_NEW_SPACING = FORMAL_ONLY
CROSS_DETERMINANT_NONHIT = NO
```

---

# Part IX — Old Word / Carry Bridge Audit

本轮只问：

\[
\boxed{
\text{旧 word/carry 是否给 }B_A\text{ 或 }B_B\text{ 一条新 equation？}
}
\]

## 9.1 What R6 already consumed

T0 的 finite borrow：

\[
c=
\begin{cases}
0,&\text{plus},\\
1,&\text{minus},
\end{cases}
\]

已经被 exactized 进 \(H\)/AFF structural state。

nonzero remainder：

\[
\widehat R
\]

也已经进入：

\[
S_3=E-M\widehat R.
\]

所以再恢复同一 third-tail / prefix borrow word，只会重建 AFF 或其 normalized versions，除非能显式出现 \(U\)。

## 9.2 No recovered word equation contains \(U\)

当前 canonical transition word equations读取：

\[
H,\widehat R,q,S_3,M,N
\]

以及 Smith coefficients。

actual numerator headroom读取：

\[
U,M,N,u_0.
\]

R7 的 source census 没有恢复任何旧 word equation在保留 exact semantics 后额外含有 \(U\) 而又不等价于 common-\(U\) reconstruction。

因此：

```text
OLD_WORD_NEW_HEADROOM_EQUATION = NO
THIRD_TAIL_HEADROOM_CODIMENSION = NO
FINITE_BORROW_TO_ACTUAL_U = NO
```

本轮按纪律停止 old-word archaeology。

---

# Part X — Primitive / Smith Bridge Enhancers

本节只检查 primitive/sphere 是否能让 algebraic bridge获得 arithmetic novelty。

## 10.1 Fixed-\(q\) primitive equation

令：

\[
A=\alpha t,\quad
B=v,\quad
T=T_3,\quad
E=\alpha JZ.
\]

R6 frozen：

\[
Q_0=A(MT+N)-E.
\]

sphere 等价于：

\[
\boxed{
(AMT-E)(AMT+2AN-E)
=
P_1^2+B^2M^2.
}
\tag{SPH-FQ}
\]

## 10.2 Substitute Face B headroom

令：

\[
X:=u_0(T_2-B_B)=UM.
\]

即：

\[
M=\frac XU.
\]

把它代入 (SPH-FQ) 并清 denominator \(U^2\)，得到一个看似包含 \(B_B\) 的大整数方程。

但：

\[
X=UM
\]

本身恰是 headroom definition。

因此整个清分母方程除去 \(U^2\) 后严格恢复原 (SPH-FQ)。

换言之：

\[
\boxed{
\text{primitive sphere}
+
\text{headroom substitution}
}
\]

没有产生一个新的 \(B_B\)-specific primitive divisor。

## 10.3 Substitute Face A headroom

同理令：

\[
Y:=u_0(T_3-B_A)=UN.
\]

则：

\[
N=Y/U.
\]

代入 (SPH-FQ) 清分母后，所有新增 \(U\)-factors只是在恢复 \(N=Y/U\)，没有新 source divisor落到 \(B_A\)。

所以：

```text
PRIMITIVE_SPHERE_AS_BRIDGE_ENHANCER = NO_NEW_INFORMATION
SMITH_DIVISOR_AS_BRIDGE_ENHANCER = COEFFICIENT_ABSORBED
```

这不处决 primitive geometry本身；它只说明：

\[
\boxed{
\textbf{在 current AFF + headroom architecture 中，
primitive equation不能把 tautological bridge变成 second codimension。}
}
\]

---

# Part XI — Counterexample / Guillotine Ledger

本轮严格区分：

- full T0 source counterexample；
- exact Smith/common-\(U\) interface countermodel；
- merely not proved。

## C1 — \(D_T\mid B_T\) for a nontrivial affine \(D_T\)

```text
NOT PROVED
NO UNIFORM CANDIDATE SURVIVED
```

没有恢复 full-T0 counterexample，因为当前没有完整 T0 generator/certificate corpus。

但所有 natural \(D_T\in\{E,\widehat R,\Lambda_{\rm aff},J,h_T^\sharp\}\) 都在 bridge 中发生 coefficient absorption 或缺少 required coprimality。

## C2 — \(B_T=O(1)\) globally

```text
NOT PROVED
NO FULL-T0 COUNTEREXAMPLE RECOVERED
```

现有 digit window仅给 moving bound：

\[
1\le B_i\le 9\cdot10^{n_i-1}.
\]

AFF 没有删除 \(n_i\)-tail。

## C3 — \(B_A=B_B\)

```text
FALSE AS A SOURCE-SEMANTIC NECESSITY
```

两者满足的是：

\[
C_2B_A-C_3B_B=C_2T_3-C_3T_2,
\]

并不要求相等。

这不是 full-T0 nonexistence counterexample；它是 exact common-\(U\) algebra对该等式必要性的直接反证。

## C4 — \(B_T=1\) impossible

```text
NO_ARCHITECTURAL_EXCLUSION
```

在 source boundary semantics 中：

\[
B_B=1
\iff
UC_2=T_2-1.
\]

例如 isolated common-\(U\) block：

\[
U=1,\quad
C_2=T_2-1
\]

完全满足 \(B_B=1\) 与 upper digit legality。

这不声称已经嵌入 full T0 primitive sphere；它严格证明：

\[
\boxed{
\text{boundary semantics本身不排除 }B_B=1.
}
\]

AFF direct bridge又 collapse，因此 current architecture没有额外机制杀它。

Face A 同理。

## C5 — \(\gcd(U,\widehat R)=1\)

```text
FALSE AS A CONSEQUENCE OF THE FROZEN SMITH/UNIT GATES
```

取 exact Smith-interface data：

\[
\alpha=t=s=\beta=u_0=1,
\quad
n_3=2,
\quad
v=97.
\]

则：

\[
\widehat R=100-97=3,
\]

\[
V=97.
\]

取：

\[
U=3.
\]

则：

\[
\gcd(U,V)=1,
\qquad
\gcd(U,\widehat R)=3.
\]

所以：

\[
\boxed{
\gcd(U,V)=1
\not\Rightarrow
\gcd(U,\widehat R)=1.
}
\]

该 countermodel 位于 exact Smith/unit interface；不冒充 full primitive T0 source solution。

## C6 — \(\gcd(M,\widehat R)=1\)

```text
NOT A FROZEN THEOREM
```

primitive normalization没有给出该 coprimality；current Smith dictionary也没有。

不得作为 divisor peeling 输入。

## C7 — Face B always stronger than Face A

```text
FALSE AS AN ARITHMETIC-NOVELTY CLAIM
```

Face B syntactically直接共享 \(M\)，但其 bridge exact collapse。

Face A 使用 T0-Q 共享 \(N\)，同样 exact collapse。

所以：

\[
\boxed{
\text{Face B 的 70\% 优先预算是合理搜索顺序，
但不是 theorem-level strength ordering。}
}
\]

## C8 — two-headroom equation globally finiteizes both heads

```text
FALSE AT SOURCE-SEMANTIC LEVEL
```

固定：

\[
C_2=C_3=1,\qquad
T_2=T_3=10^n.
\]

则：

\[
B_A=B_B=10^n-U.
\]

只要 \(U\) 在合法 digit range 内移动，就产生随 \(n\) 增长的 headroom states。

因此 two-headroom relation本身不可能给 digit-length-independent finiteization。

再次强调：这是 source-gate countermodel，不宣称每个状态均满足 full T0 primitive equations。

---

# Part XII — Bridge Candidate Ledger

| Candidate | Uses AFF? | Uses actual \(B_T\)? | Uses source reconstruction? | Algebraically independent? | New arithmetic lattice? | Divisibility? | Finiteization? | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Face B \(u_0\widehat RB_B=U(S_3-E)+u_0T_2\widehat R\) | YES | YES | YES | NO | NO | NO | NO | `ALGEBRAIC_BRIDGE_ONLY` |
| Face A \(\alpha tu_0B_A=U\alpha tMT_3+\alpha tu_0T_3-U(E+Q_0)\) | YES via T0-Q | YES | YES | NO | NO | NO | NO | `ALGEBRAIC_BRIDGE_ONLY` |
| two-headroom \(NB_B-MB_A=N T_2-M T_3\) | NO | YES | YES | source-genuine | NO affine novelty | NO new | NO | `REDUNDANT` |
| decimal gcd \(\gcd(C_2,T_2)\mid B_B\) | NO | YES | YES | YES source | old endpoint lattice | YES | NO | `REDUNDANT` |
| decimal gcd \(\gcd(C_3,T_3)\mid B_A\) | NO | YES | YES | YES source | old endpoint lattice | YES | NO | `REDUNDANT` |
| \(D_{\times,B}=EB_B-T_2S_3\) | YES | YES | YES | NO | formal only | divisor coefficient-poisoned | NO | `DEPENDENT_CROSS_PRODUCT` |
| \(D_{\times,A}=EB_A-T_3S_3\) | YES | YES | YES | NO | formal only | divisor coefficient-poisoned | NO | `DEPENDENT_CROSS_PRODUCT` |
| primitive sphere + Face B substitution | YES indirectly | YES | YES | NO after undoing substitution | NO | NO | NO | `REDUNDANT` |
| primitive sphere + Face A substitution | YES indirectly | YES | YES | NO after undoing substitution | NO | NO | NO | `REDUNDANT` |
| backward \(2\times5\) coefficient peeling | YES | YES | partial | N/A | NO | coefficient only | NO | `INSUFFICIENT` |

本轮没有 candidate 达到：

```text
GENUINE_BRIDGE
PROMISING
```

标准。

---

# Part XIII — Information-Dimension Audit

这是 R7 的决定性部分。

## 13.1 Algebraic separation theorem

把已经满足 T0 structural equations 的所有变量视为 coefficient field \(K\)。

尤其 \(K\) 已包含：

\[
C_2,C_3,T_2,T_3,
\widehat R,E,S_3,Q_0,\ldots
\]

并已施加：

\[
S_3=E-M\widehat R,
\]

\[
Q_0+E=\alpha t(MT_3+N).
\]

### One-face projection

Face B source equation：

\[
B_B-T_2+UC_2=0.
\]

在：

\[
K[U,B_B]
\]

中，因为 \(C_2\neq0\)，对任意 \(B_B\) 都可形式解：

\[
U=\frac{T_2-B_B}{C_2}.
\]

因此消去 \(U\) 后：

\[
\boxed{
I_B\cap K[B_B]=(0).
}
\]

也就是说：

\[
\boxed{
\textbf{单靠 structural AFF + one-face common-\(U\) equation，
没有任何非零 polynomial condition 被强迫到 }B_B.
}
\]

Face A 完全同理：

\[
\boxed{
I_A\cap K[B_A]=(0).
}
\]

### Two-face projection

同时保留：

\[
B_B-T_2+UC_2=0,
\]

\[
B_A-T_3+UC_3=0.
\]

消去 \(U\) 的 resultant 是：

\[
\boxed{
C_2B_A-C_3B_B-C_2T_3+C_3T_2=0.
}
\]

这就是 (2H-C)。

它不含任何 transition affine datum。

所以：

\[
\boxed{
\textbf{当前 AFF 与 source-boundary 两个 information classes
在 algebraic elimination 层没有产生 mixed generator。}
}
\]

## 13.2 Integrality does not repair the missing codimension

algebraic separation 本身还不能排除 integrality 产生新信息。

因此继续加入：

\[
U\in\mathbb Z_{>0},
\qquad
\gcd(U,V)=1.
\]

但 current theory只把 \(U\) 限制到 unit classes，不给 fixed residue；而 headroom residue：

\[
B_i\equiv T_i-UC_i\pmod D
\]

仍依赖 moving unit \(U\)。

因此没有：

\[
\boxed{
\text{AFF structural divisor}
\Longrightarrow
\text{fixed headroom residue}
}
\]

的 theorem。

## 13.3 Canonical freedom count

R6 structural T0 state仍含 moving：

\[
(g,k,n_3,J,M,N,u_0,\widehat R,q,\ldots).
\]

加入 actual source 后，\(U\) 是 semantic realization parameter。

引入：

\[
B_A,\ B_B
\]

并没有增加 independent freedom，因为二者由 \(U\) 定义。

R7 的 two-headroom relation也只是把二者重新压回同一个 \(U\)。

而 AFF 不进一步约束 \(U\)。

因此：

\[
\boxed{
\Delta(\text{canonical freedom})=0
}
\]

for R7 current bridge architecture.

本轮真正获得的是：

\[
\boxed{
\textbf{negative architecture theorem},
}
\]

而不是：

\[
\boxed{
\textbf{new solution-space compression}.
}
\]

所以：

```text
R7_INFORMATION_DIMENSION_DROP=NO
R7_ARCHITECTURE_KILL_INFORMATION=YES
```

这完成：

\[
\boxed{
\textbf{95-R7-T3 — Bridge Independence / Arithmetic Novelty Lemma}.
}
\]

---

# Part XIV — T1 Transfer Verdict

R7 的 transfer rule 是：

只有在 T0 建立 genuine bridge 后，才允许研究该桥是否只要求 finite \(c\)。

当前：

\[
\boxed{
\texttt{GENUINE\_AFFINE\_BOUNDARY\_BRIDGE=NO}.
}
\]

因此：

\[
\boxed{
\texttt{T1\_TRANSFER\_ACTIVATED=NO}.
}
\]

T1 继续冻结。

理由不是 T1 更难，而是：

\[
\boxed{
\textbf{不能把 T0 已经被证明 arithmetic-redundant 的 bridge
复制到 10 个 borrow states 上。}
}
\]

---

# Part XV — Updated 95 Frontier

R7 没有 set-level 关闭：

\[
\mathcal H_{T0}.
\]

所以当前 live frontier 不删除 T0。

承接 R5/R6：

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

但 T0 status 必须更新为：

```text
T0 = OPEN
T0_AFFINE_EXACTIZED = YES
T0_FINITE_BORROW = YES
T0_DIRECT_AFFINE_GCD_GAP = KILLED
T0_DIRECT_AFFINE_HEADROOM_BRIDGE = KILLED
T0_CURRENT_ARCHITECTURE = SATURATED
```

以后若重新进入 T0，必须带来**新的 information class**，不能继续：

- sharpen AFF；
- sharpen \(\widehat R\)；
- sharpen \(\Lambda_{\rm aff}\)；
- 再定义 numerator headroom；
- 再做 AFF × headroom direct elimination；
- 再做同型 cross determinant；
- 把 T0-Q 当第二独立 affine equation；
- 把 primitive sphere做纯 substitution 后称为 bridge。

允许未来重新进入 T0 的最低门槛应是：

\[
\boxed{
\textbf{出现一条 genuinely含 }U\textbf{ 的新 source equation，
且不能从 common-}U\textbf{ reconstruction 消去。}
}
\]

或者：

\[
\boxed{
\textbf{出现一个真正 positional unit theorem，
把 AFF structural state 映到 }U\bmod D.
}
\]

否则 T0 保持 architecture-frozen。

---

# Part XVI — R8 Launch Decision

R7 必须在 Path D / E 中重新决策。

R5 的旧边际价值排序为：

\[
\mathcal H_0:
\quad
\text{MEDIUM\_SPECULATIVE},
\]

\[
\mathcal H_{O+}:
\quad
\text{LOW\_TO\_MEDIUM}.
\]

经过 R6-R7，transition 的“nonzero affine datum”已经确认无法触碰 actual source boundary；这削弱了继续依赖同类 affine/source-splice 思路的收益。

比较：

## Path D — Outer Plus

\[
g\ge1,\qquad
d\le-1,\qquad
\text{plus only}.
\]

优势：

- sign fixed；
- no borrow；
- \(P_3\) 有更强 projective smallness。

但：

- \(d\) 是新的 unbounded structural direction；
- 当前没有 T0 那样已经 exactized 的 low-dimensional affine normal form；
- 若现在进入 outer-plus，很容易把刚刚确认的“source-boundary independence”问题带进更大的 state space。

## Path E — \(\mathcal H_0\)

\[
g=0.
\]

优势：

- 整个 exponent direction \(g\) 被永久冻结；
- 可以直接从 Full Smith–Radial Cancellation 后的
  \[
  (u_0,M,N)
  \]
  / SRUS source chart 开始；
- 历史上已有 pseudo-family 在 Layer C 死、exact real-cone point 在 Layer I 死，说明这一 chamber 的真正问题已经天然靠近 common-\(U\) semantic gate；
- 不需要先复制一个已死亡的 affine bridge。

缺点：

- 尚缺一个 low-state theorem；
- 历史结构不如 transition 成熟。

综合 R5 原排序与 R7 新 architecture death：

\[
\boxed{
\textbf{R8 选择 Path E — }\mathcal H_0\textbf{ assault}.
}
\]

正式 machine-readable decision：

```text
R8_PATH=E_H0_ASSAULT
OUTER_PLUS=RESERVE
T0=ARCHITECTURE_FROZEN
T1=FROZEN
```

R8 不应写成 R7.1。

---

# Part XVII — Theorem Target Ledger

## 95-R7-T1 — Source Headroom Exactization

\[
\boxed{
B_B=10^{n_2}-UC_2,
\qquad
B_A=10^{n_3}-UC_3.
}
\]

**Status:** PROVED / identified with old endpoint slack.

## 95-R7-T2 — Affine-to-Headroom Elimination Identity

Face B：

\[
\boxed{
u_0\widehat RB_B
=
US_3-UE+u_0T_2\widehat R.
}
\]

Face A：

\[
\boxed{
\alpha t\,u_0B_A
=
U\alpha tMT_3+\alpha t\,u_0T_3-U(E+Q_0).
}
\]

**Status:** PROVED.

## 95-R7-T3 — Bridge Independence / Arithmetic Novelty Lemma

两条 bridge 均 exact collapse；one-face elimination ideal为零；two-face唯一 resultant是 source-only slack identity。

**Status:** PROVED NEGATIVE.

## 95-R7-T4 — Headroom Divisibility / Finiteization

没有 transition-forced nontrivial headroom divisor，也没有 digit-length-independent finiteization。

**Status:** NOT ACHIEVED / NATURAL ROUTES KILLED.

## 95-R7-T5 — T0 Source-Boundary Closure / Compression

\[
\boxed{
\mathcal H_{T0}=\varnothing
}
\]

未证明。

没有 canonical freedom reduction。

**Status:** NO.

## 95-R7-T6 — Transition Architecture Verdict

\[
\boxed{
\texttt{TRANSITION\_AFFINE\_BOUNDARY\_BRIDGE\_KILLED}.
}
\]

**Status:** PROVED AS CURRENT-ARCHITECTURE VERDICT.

---

# Part XVIII — Final Architecture Autopsy

R6 的判断：

\[
\boxed{
\text{AFF source datum genuinely independent of resonance}
}
\]

仍然正确。

R7 的新判断是：

\[
\boxed{
\text{AFF datum is not automatically independent of source boundary
in the useful arithmetic sense}.
}
\]

更准确的 dependency graph 是：

```text
                 structural T0 source
                         |
                         v
              AFF: S3 = E - M Rhat
                         |
                 [no U appears]
                         |
                         X
              actual-U residue/location
                         |
                         v
        B_B = T2 - U C2 ; B_A = T3 - U C3
                         |
                         v
              common-U / unit successor
```

把 \(M\) 或 \(N\) 当共享变量做 direct elimination，只会在中间画出一条 algebraic 线，最终仍回到定义。

真正缺失的仍是：

\[
\boxed{
\textbf{一个含 }U\textbf{ 的独立 source-labelled equation}
}
\]

或：

\[
\boxed{
\textbf{一个 structural state }\to U\bmod D
\textbf{ 的 positional theorem}.
}
\]

这不是“再算一次 gcd”能补出来的。

因此：

\[
\boxed{
\textbf{R6 找到了两岸；
R7 证明当前材料搭出的桥只是投影重合，不承载新的整数交通。}
}
\]

95 的正确动作是停止当前 transition architecture，转向：

\[
\boxed{
\mathcal H_0.
}
\]

---

# Provenance / Frozen Inputs Used

本轮主要核准并继承：

- `95_R6_T0_Transition_Finite_Borrow_Affine_Boundary_Margin_Assault.md`
- `95_R5_First_Architecture_Shock_Checkpoint.md`
- `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
- `strict_layer_A1_SRCU_state_after_campaign.md`
- `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`
- `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`
- `strict_layer_A1_resonant_transition_reduced_fraction_unit_exclusion_campaign.md`
- later RGCD correction of the old integer-margin normalization

本轮特别保留的 provenance correction：

\[
\boxed{
u_0\mathcal G_A\ge M
\iff
\mathcal G_A\ge C_2,
}
\]

\[
\boxed{
u_0\mathcal G_B\ge N
\iff
\mathcal G_B\ge C_3,
}
\]

不能再使用旧误写：

\[
\mathcal G_A\ge M,\qquad
\mathcal G_B\ge N
\]

除非 \(u_0=1\)。

---

# Final One-Line Verdict

\[
\boxed{
\textbf{T0 的 actual numerator headroom 可以与 AFF 代数拼接，
但拼接后严格塌回 common-}U\textbf{ 定义；
没有新 divisor、没有新 lattice、没有 finiteization。
当前 transition architecture 正式饱和并处决，R8 转攻 }\mathcal H_0.
}
\]
