# 95-R2 — J5 Certificate Recovery × Non-(J2) Resonant Cyclotomic–Endpoint Collision × Symbolic Resonance Central Assault × Information-Class Extinction Test

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Ownership:** 95 only, hence \(J\neq2\) throughout  
**Round:** 95-R2  
**Canonical output:** `95_R2_NonJ2_Resonant_Cyclotomic_Endpoint_Collision.md`

---

# Part I — Executive Verdict

本轮的最终状态是：

```text
95_R2_STATUS = COMPLETE
NONJ2_RESONANCE_STATUS = NONJ2_RESONANCE_COMPRESSED_NOT_CLOSED
J5_2_POSITIVE = CLOSED_BY_REPLAY_CERTIFICATE
J5_3_POSITIVE = CLOSED_BY_REPLAY_CERTIFICATE
GENERAL_POSITIVE_RESONANCE = SUCCESSOR_COMPRESSED
GENERAL_NEGATIVE_RESONANCE = OPEN_NO_SIGNED_RRGS3
CYCLOTOMIC_PRIME_SUPPORT_CLOSURE = INSUFFICIENT
MANTISSA_LATTICE_GAP = REDUNDANT_AT_FROZEN_KERNEL
FINITE_EXCEPTIONAL_J_THEOREM = NOT_OBTAINED
R3_LAUNCH = YES
```

因此本轮达到 **Level C — Useful Compression**，但没有达到 Level A / B。

本轮真正完成了三件事：

1. 对历史 \(J=5\) 两个 fixed-depth positive residual family 重新建立 deterministic exact certificate，并用第二实现逐状态复验；
2. 把 general positive resonance 的 \((U,W)\) 两个移动整数压成一个有限 successor
   \[
   \xi:=UW;
   \]
3. 证明原计划中最诱人的 “mantissa × lattice gap” 并不是独立信息：mantissa difference 已经**精确等于** \(-s\beta_0W\)，而 enhanced divisor ratio 也**精确等于** \(W\)。

最终的 architecture verdict 不是 “全无效”，而是：

\[
\boxed{
\text{positive side 有真实 finite-successor cut，}
\quad
\text{negative side 缺少同等级 independent size information.}
}
\]

---

# Part II — J5 Certificate Recovery

## 2.1 历史状态

95-R1 已恢复 exact three-family classification：

\[
\mathcal H_{5,1},\qquad \mathcal H_{5,2},\qquad \mathcal H_{5,3}.
\]

其中历史 radialized report 声称：

\[
\mathcal H_{5,2}\cap\{S_R>0\}=\varnothing,
\qquad
\mathcal H_{5,3}\cap\{S_R>0\}=\varnothing,
\]

但 95-R1 没有恢复 standalone generator / verifier / certificate bundle，因此当时只能标记：

```text
CLAIMED_BUT_CERTIFICATE_NOT_RECOVERED
```

本轮再次搜索 File Library，仍只恢复到 report-level exhaustive specification，没有发现旧 standalone bundle。

因此 R2 按历史 theorem 的**原有限域**重建最小 deterministic replay；没有扩大搜索域，也没有重新做原题 brute force。

---

## 2.2 历史有限 theorem 的 exact replay interface

对两个 positive fixed-depth family 都有：

\[
\beta_0=1,\qquad u=u_0,\qquad n_3=g.
\]

定义：

\[
A_0:=u_0J+d_*.
\]

由历史 core + leading defect 消元：

\[
Q_0=
\frac{u_0Jg_1C_1 10^k+W}{A_0}.
\]

又：

\[
d_2=u_0C_3-K_*W>0,
\qquad
K_*={10^g\over d_*}.
\]

primitive sphere 对 \(C_1\) 的必要二次门可写成：

\[
\boxed{
\Delta'
=
(d_2u_0J10^k)^2
-A_0^2\bigl(d_2^2+u_0^2C_3^2\bigr)
+2A_0d_2W.
}
\tag{J5-DISC}
\]

任何 survivor 必须：

\[
\Delta'=R_0^2,
\]

并且至少一个根满足：

\[
\boxed{
C_1=
\frac{d_2u_0J10^k\pm R_0}{A_0g_1}
\in\mathbf Z_{>0}.
}
\tag{J5-ROOT}
\]

resonance Smith dictionary 给：

\[
g_1=\beta t v_0.
\]

这里 \(t=1\)，且 \(u=u_0\mid10^g+1\) 自动与 \(10\) 互素，因此 \(\gamma=1\)、\(v_0=10^g\)。所以：

\[
\boxed{g_1=\beta10^g.}
\]

这给：

- \(g=2,\beta=40\Rightarrow g_1=4000\)；
- \(g=3,\beta=800\Rightarrow g_1=800000\)。

---

## 2.3 \(\mathcal H_{5,2}^{+}\) — exact replay

历史 family：

\[
J=5,\quad(g,n_3,d_*)=(2,2,2),\quad\beta=40,
\]

\[
u_0\mid101,
\qquad
1\le C_3<100,
\]

positive condition \(d_2>0\) 等价于：

\[
1\le W<\frac{u_0C_3}{50}.
\]

历史 axis theorem 已把 exponent 严格压到：

\[
1\le k\le8.
\]

canonical base-state count 重放为：

\[
\boxed{9998}.
\]

展开 \(k\) 后总检查：

\[
\boxed{79,984}
\]

个 exact states。

结果：

- negative discriminant：1,170；
- exact nonsquare：78,814；
- square discriminant：0；
- positive integral \(C_1\)：0。

因此：

\[
\boxed{
\mathcal H_{5,2}\cap\{S_R>0\}=\varnothing.
}
\tag{95-R2-J5-2+}
\]

注意 \(\mathcal H_{5,2}\) 中历史允许 \(s=1,2\)，对应 \(b_2=40,80\)。上述 primitive discriminant/root necessary gate 不含 \(s\)；两个 source \(s\)-case 都投影到同一 replay state space，因此没有漏支。

---

## 2.4 \(\mathcal H_{5,3}^{+}\) — exact replay

历史 family：

\[
J=5,\quad(g,n_3,d_*)=(3,3,4),\quad\beta=800,
\]

\[
u_0\mid1001,
\qquad
1\le C_3<1000,
\]

\[
1\le W<\frac{u_0C_3}{250},
\qquad
1\le k\le12.
\]

canonical divisors：

\[
u_0\in\{1,7,11,13,77,91,143,1001\}.
\]

base-state count：

\[
\boxed{2,681,304}.
\]

展开 \(k\) 后：

\[
\boxed{32,175,648}
\]

个 exact states。

结果：

- negative discriminant：301,650；
- exact nonsquare：31,873,997；
- square discriminant但 root divisibility失败：1；
- positive integral \(C_1\)：0。

唯一 square-discriminant near-survivor 精确复现为：

\[
\boxed{
(u_0,C_3,W,d_2,k)=(7,737,9,2909,1).
}
\]

且：

\[
\Delta'=983278492816=991604^2.
\]

此时：

\[
A_0=39,
\qquad
g_1=800000,
\qquad
A_0g_1=31,200,000.
\]

两个 root numerator：

\[
2,009,754,
\qquad
26,546,
\]

均不被 \(31,200,000\) 整除。

所以：

\[
\boxed{
\mathcal H_{5,3}\cap\{S_R>0\}=\varnothing.
}
\tag{95-R2-J5-3+}
\]

这也再次严格处决：

\[
\boxed{
\text{“fixed-depth J5 中 discriminant 永不为平方”}
}
\]

这一错误 conjecture。真正的 finite gate 必须是：

\[
\boxed{
\text{square discriminant}
+\text{root divisibility}.
}
\]

---

## 2.5 Replay certificate bundle

本轮生成：

- `95_R2_J5_certificate_replay.py`
- `95_R2_J5_certificate_verifier.py`
- `95_R2_J5_certificate.json`
- `95_R2_J5_rejection_ledger.tsv`
- `95_R2_J5_near_survivors.tsv`
- `95_R2_J5_verifier_report.json`
- `95_R2_J5_SHA256SUMS.txt`

rejection ledger 对每个 canonical base state 保存一个 \(k\)-reason string：

```text
D = negative discriminant
N = exact non-square
I = square but root integrality/divisibility fails
P = positive integral C1 survivor
```

因此每个 expanded \((\text{base},k)\) state 都有明确 rejection reason。

canonical uncompressed rejection stream SHA-256：

```text
0612182b02a4e89b3af7d91cdebd3176f81a4026c1f1494f1dafa1700eca6f86
```

第二实现逐行重建并复验：

```text
VERIFIER_STATUS = PASS
BASE_ROWS_VERIFIED = 2,691,302
EXPANDED_STATES_VERIFIED = 32,255,632
INTEGRAL_C1_SURVIVORS = 0
```

因此本轮允许正式升级：

```text
H_5,2 ∩ {S_R>0} : CLOSED
H_5,3 ∩ {S_R>0} : CLOSED
```

---

# Part III — Frozen General Resonance Kernel

以下只列本轮直接使用的 95-R1 frozen theorem；不重新证明历史部分。

令：

\[
G:=10^g.
\]

## 3.1 Resonance support

\[
\boxed{
J={G\over\gcd(G,\beta)}=2^{e_2^+}5^{e_5^+}>1.
}
\]

\[
\boxed{
d_*=2^{e_2^-}5^{e_5^-}.
}
\]

因此对每个 \(p\in\{2,5\}\)：

\[
e_p^+e_p^-=0,
\]

从而得到本轮首先显式抽出的 support complementarity：

\[
\boxed{
\gcd(J,d_*)=1.
}
\tag{COMP}
\]

所以：

- 若 \(2\mid J\) 且 \(5\mid J\)，则 \(d_*=1\)；
- 若 \(J=2^A\)，则 \(d_*\) 只能是 \(5\)-power；
- 若 \(J=5^B\)，则 \(d_*\) 只能是 \(2\)-power。

这比把 \(d_*\) 当任意 \(2,5\)-smooth integer 更窄。

## 3.2 Content

\[
\boxed{
\beta_0=\beta^{\langle10\rangle},
\qquad
c_R=s d_*\beta_0<J,
\qquad
\beta_0\mid c_R.
}
\]

## 3.3 Enhanced divisor and deflated gap

\[
\boxed{
D=\beta_0D_1,
}
\]

\[
\boxed{
uJD_1=d_*Q_0-W,
}
\]

\[
\boxed{
S_R=K_*W,
\qquad
K_*={G\over d_*}.
}
\]

并且：

\[
\boxed{
0<|W|<{d_*Q_0\over G}.
}
\tag{W-BOUND}
\]

## 3.4 Ultra-sharp mantissa — exact form

真正的 exact identity 是：

\[
\boxed{
b_1JD=c_RQ_0-s\beta_0W.
}
\tag{M-EXACT}
\]

因此：

\[
\boxed{
b_1JD-c_RQ_0=-s\beta_0W.
}
\tag{M-DIFF}
\]

以及：

\[
\left|
{b_1JD\over c_RQ_0}-1
\right|<G^{-1}.
\]

## 3.5 Cyclotomic reduced denominator

\[
\boxed{
u_0\mid G+1,
}
\]

\[
\boxed{
\gcd(u_0,Q_0)=\gcd(u_0,S_R)=1,
\qquad
\gcd(u_0,10)=1.
}
\]

于是：

\[
\boxed{
\gcd(u_0,W)=1.
}
\]

## 3.6 RRGS

令：

\[
\Xi:=UW.
\]

则：

\[
\boxed{
U(Q_0-P_2)+K_*\Xi=u_0a_3,
}
\tag{RRGS-1}
\]

\[
\boxed{
d_*(10^{n_3}a_2+a_3)
={G+1\over u_0}\Xi+\gamma JUD_1.
}
\tag{RRGS-2}
\]

且在：

\[
S_R>0
\]

时：

\[
\boxed{
0<\Xi<u_0d_*10^{n_3-g}.
}
\tag{RRGS-3}
\]

## 3.7 Reduced-denominator unimodular envelope

定义：

\[
q_0={G+1\over u_0},
\qquad
\bar A_J=Ju_0+1,
\qquad
\bar B_J=JG+q_0.
\]

则：

\[
q_0\bar A_J-\bar B_J=J,
\]

\[
\boxed{
u_0\bar B_J-G\bar A_J=1.
}
\tag{UNI}
\]

即：

\[
\det
\begin{pmatrix}
G&u_0\\
\bar B_J&\bar A_J
\end{pmatrix}
=-1.
\]

## 3.8 Resonant SRUS

source recovery 要求存在 actual \(U\) 满足：

\[
{U\over u_0}\in K^{\rm res}_{MN},
\]

并且：

\[
\boxed{
\gcd(U,s\beta u_0 10^{n_3})=1.
}
\]

因此：

\[
\gcd(U,u_0)=1.
\]

---

# Part IV — 95-R2-T1: Resonant Cyclotomic Capacity Lemma

## 4.1 Exact prime-power order class

取任意 prime power：

\[
\pi=p^a\mid u_0.
\]

因为：

\[
u_0\mid10^g+1,
\]

有：

\[
10^g\equiv-1\pmod\pi.
\]

故 \(p\notin\{2,5\}\)，且令：

\[
r_\pi:=\operatorname{ord}_\pi(10),
\]

则：

\[
r_\pi\mid2g,
\qquad
r_\pi\nmid g.
\]

更精确地，因为 \(10^g\) 在 \((\mathbf Z/\pi\mathbf Z)^\times\) 中的 order 恰为 \(2\)：

\[
{r_\pi\over\gcd(r_\pi,g)}=2.
\]

所以存在 \(d\mid g\)，使：

\[
\boxed{
r_\pi=2d,
\qquad
{g\over d}\text{ 为奇数}.
}
\tag{CYC-ORD}
\]

这是 \(u_0\mid10^g+1\) 的 exact elementary cyclotomic content。

---

## 4.2 Support separation, not support collision

由于：

\[
J,d_*\text{ 都是 }2,5\text{-primary},
\]

而：

\[
\gcd(u_0,10)=1,
\]

直接有：

\[
\boxed{
\gcd(u_0,Jd_*)=1.
}
\]

又由 Smith：

\[
\gcd(u,\beta)=1,
\qquad u_0\mid u,
\]

故：

\[
\boxed{
\gcd(u_0,\beta_0)=1.
}
\]

所以当前 frozen kernel 中，cyclotomic prime support 与 decimal-content support 的基本关系是：

\[
\boxed{
\textbf{强制分离，而不是强制相交。}
}
\]

这直接处决一种原候选 architecture：

```text
“某个 p|u0 必须同时进入 J / d* / beta0 content，产生冲突”
```

实际上 frozen theorem 恰恰把这些 prime support 分开。

---

## 4.3 为什么 Zsigmondy 不给 closure

即使 \(10^g+1\) 在许多 \(g\) 上具有 primitive prime divisor，当前 state 只要求：

\[
u_0\mid10^g+1,
\]

并没有要求 \(u_0\) 吸收 \(10^g+1\) 的某个 primitive prime。

最极端地：

\[
\boxed{u_0=1}
\]

永远通过 cyclotomic divisibility 本身。

因此 primitive-divisor theorem 不能把“\(10^g+1\) 有新素因子”升级成“每个 admissible \(u_0\) 都携带新素因子”。

**T1 verdict：**

```text
95-R2-T1 = PROVED
CYCLOTOMIC_CAPACITY = EXACT_ORDER_CLASS_OBTAINED
UNIFORM_FINITE_U0 = NO
CYCLOTOMIC_PRIME_SUPPORT_EXTINCTION = NO
```

---

# Part V — 95-R2-T2: Resonant Content Compression Lemma

由：

\[
c_R=s d_*\beta_0<J
\]

定义：

\[
\boxed{
h:={c_R\over\beta_0}=s d_*\in\mathbf Z_{>0}.
}
\]

于是：

\[
\boxed{
1\le h\le
\left\lfloor{J-1\over\beta_0}\right\rfloor.
}
\tag{H-RANGE}
\]

且：

\[
d_*\mid h.
\]

结合 \(d_*\) 的 \(2,5\)-primary 性与 \(\gcd(J,d_*)=1\)，得到 exact parameterization：

\[
\boxed{
(J,\beta_0,h,d_*)
\quad\text{with}\quad
1\le h\le\Bigl\lfloor{J-1\over\beta_0}\Bigr\rfloor,
\quad
d_*\mid h,
\quad
d_*\text{ supported only on }\{2,5\}\setminus\operatorname{supp}(J).
}
\tag{CONTENT-NF}
\]

并且：

\[
\boxed{s={h\over d_*}.}
\]

所以 \(s\) 不再是独立变量。

---

## 5.1 Quotient-class theorem

若写：

\[
\rho:={J\over\beta_0},
\]

则：

\[
h<\rho.
\]

故：

### \(\rho\le2\)

\[
h=1
\Longrightarrow
\boxed{s=d_*=1}.
\]

### \(\rho\le3\)

\[
h\in\{1,2\}.
\]

候选 \((s,d_*)\) 只可能来自：

\[
(1,1),\ (2,1),\ (1,2),
\]

再由 support complementarity 删除不允许的 \(d_*=2\) case。

### \(\rho\le4\)

\[
h\in\{1,2,3\},
\]

其中 \(h=3\) 时 \(d_*=1\)。

这给出真正 symbolic 的 quotient-class compression，而不是逐个 \(J\) 打地鼠。

---

## 5.2 三个 J-support regime

由 \(\gcd(J,d_*)=1\)：

### Mixed support

\[
J=2^A5^B,\quad A,B>0
\Longrightarrow
\boxed{d_*=1}.
\]

所以：

\[
c_R=s\beta_0<J.
\]

### Pure-2 support

\[
J=2^A
\Longrightarrow
\boxed{d_*=5^b}.
\]

### Pure-5 support

\[
J=5^B
\Longrightarrow
\boxed{d_*=2^a}.
\]

这三类是 R2 后继续研究 general resonance 时应采用的 content information classes。

**T2 verdict：**

```text
95-R2-T2 = PROVED
CONTENT_VARIABLES (s,d*) -> (h,d*)
J_SUPPORT_SPLIT = MIXED / PURE_2 / PURE_5
UNIFORM_J_BOUND = NO
```

---

# Part VI — 95-R2-T3: Enhanced Divisor / Endpoint Successor Lemma

## 6.1 Normalized ratio is exactly W

原计划要求研究：

\[
\Xi_R:={S_R\over K_*}.
\]

但 frozen core 已经精确给：

\[
S_R=K_*W.
\]

所以不是“估计”：

\[
\boxed{
\Xi_R=W\in\mathbf Z\setminus\{0\}.
}
\tag{XI-W}
\]

因此 enhanced divisor 已经把 \(S_R\) 完全量化成 gap integer \(W\)。

这说明：

- Type-A 若要 closure，真正目标是 \(|W|<1\)；
- 单独再估 \(|S_R|\) 不会比直接估 \(|W|\) 更强。

---

## 6.2 Positive RRGS turns W into a finite successor

现在取：

\[
S_R>0.
\]

则：

\[
W>0,
\qquad
\xi:=UW>0.
\]

RRGS-3 给：

\[
\boxed{
0<\xi<B_+,
\qquad
B_+:=u_0d_*10^{n_3-g}.
}
\tag{SUCC-B}
\]

同时：

\[
\gcd(U,u_0)=\gcd(W,u_0)=1,
\]

故：

\[
\boxed{
\gcd(\xi,u_0)=1.
}
\]

于是 define：

\[
\boxed{
\mathcal X_+(B_+,u_0)
:=
\{x\in\mathbf Z_{>0}:x<B_+,\ \gcd(x,u_0)=1\}.
}
\]

每个 positive full state 必须满足：

\[
\boxed{
\xi=UW\in\mathcal X_+(B_+,u_0).
}
\tag{POS-SUCC}
\]

因此固定 structural tuple：

\[
(g,J,\beta_0,h,d_*,n_3,u_0)
\]

后，\(\xi\) 是严格有限集合。

更进一步：

\[
U\mid\xi,
\qquad
W={\xi\over U}.
\]

所以原来两个移动 positive integers \((U,W)\) 已压成：

\[
\boxed{
\text{一个有限 successor }\xi
+\text{它的 divisor allocation }U\mid\xi.
}
\]

这是本轮 general symbolic assault 中真正的新低维接口。

---

## 6.3 Exact extinction / rigidity thresholds

因为 \(\xi\in\mathbf Z_{>0}\)：

### Oversize extinction

若：

\[
B_+\le1,
\]

则：

\[
\boxed{S_R>0\Longrightarrow\varnothing.}
\tag{POS-B1}
\]

### First successor rigidity

若：

\[
1<B_+\le2,
\]

则：

\[
\xi=1.
\]

因为 \(U,W\in\mathbf Z_{>0}\)：

\[
\boxed{U=W=1.}
\tag{POS-B2}
\]

### General finite successor

若：

\[
m<B_+\le m+1,
\]

则：

\[
\boxed{
\xi\in\{1,\ldots,m\}
\cap(\mathbf Z/u_0\mathbf Z)^\times.
}
\]

这正是 prompt 所要求的 “continuous interval \(\to\) discrete successor”。

---

## 6.4 Mixed-J corollary

若：

\[
2\mid J,
\qquad5\mid J,
\]

T2 已给：

\[
d_*=1.
\]

于是 positive successor bound 简化为：

\[
\boxed{
0<UW<u_0 10^{n_3-g}.
}
\]

特别：

\[
u_0=1,
\qquad n_3\le g
\Longrightarrow
\boxed{\varnothing}.
\]

若 \(n_3=g\)：

\[
0<UW<u_0.
\]

但当 \(u_0>1\) 时 reduced residues \(1,\ldots,u_0-1\) 通常非空，所以这一层本身不闭合。

---

## 6.5 Sign asymmetry

对：

\[
S_R<0,
\]

RRGS-1/2 仍成立，但历史 RRGS-3 **不成立为已证明 theorem**。

当前只保留：

\[
0<|W|<{d_*Q_0\over G},
\]

其右侧仍依赖 moving primitive height \(Q_0\)。

所以 negative side 尚不能得到 structural finite successor set。

这精确定位本轮第一大 failure interface：

```text
ENDPOINT_INTERVAL_SIGN_ASYMMETRIC
POSITIVE: finite successor xi=UW
NEGATIVE: no structural bound independent of Q0
```

**T3 verdict：**

```text
95-R2-T3 = PROVED
NORMALIZED_RATIO = W EXACTLY
POSITIVE_SUCCESSOR_FINITEIZATION = PROVED
NEGATIVE_ANALOGUE = NOT_AVAILABLE
```

---

# Part VII — 95-R2-T4: Mantissa Lattice Gap Lemma / Redundancy Guillotine

原计划希望从：

\[
E_R:=b_1JD-c_RQ_0
\]

寻找大 lattice divisor \(\Lambda_R\)，再证明：

\[
0<|E_R|<\Lambda_R.
\]

但 exact frozen identity 给：

\[
\boxed{
E_R=-s\beta_0W.
}
\]

所以最自然的 canonical spacing：

\[
\Lambda_0:=s\beta_0
\]

已经被 \(W\) 精确饱和：

\[
\boxed{
{E_R\over\Lambda_0}=-W\in\mathbf Z\setminus\{0\}.
}
\]

于是：

\[
|E_R|\ge s\beta_0,
\]

且 \(|W|=1\) 时达到等号。

---

## 7.1 Ultra-sharp mantissa is exactly W-BOUND

mantissa inequality：

\[
|E_R|<{c_RQ_0\over G}
\]

代：

\[
E_R=-s\beta_0W,
\qquad
c_R=s d_*\beta_0,
\]

约去 \(s\beta_0\)：

\[
\boxed{
|W|<{d_*Q_0\over G}.
}
\]

这正是 frozen `W-BOUND`。

所以：

\[
\boxed{
\textbf{ultra-sharp mantissa 与 deflated W-bound 在当前 canonical variables 中是同一信息。}
}
\]

不是两个可以相乘的 independent cuts。

---

## 7.2 Cyclotomic factor不能补 spacing

若想用 \(u_0\) 增强：

\[
u_0\mid E_R,
\]

则需要 \(u_0\mid s\beta_0W\)。

但 frozen theorem 给：

\[
\gcd(u_0,\beta_0W)=1.
\]

因此除非另有 theorem 强迫 \(u_0\mid s\)，cyclotomic denominator 不会自动进入 \(E_R\)。

当前没有这一 theorem。

所以：

```text
NO_NONTRIVIAL_LATTICE_DIVISOR
```

是本轮信息集下的准确判决。

---

## 7.3 Unimodular envelope为什么还没接上

`UNI` 给：

\[
|u_0\bar B_J-G\bar A_J|=1.
\]

所以它确实给一个 determinant-1 neighboring lattice pair。

但当前没有 sourced equality 把：

\[
(b_1JD,c_RQ_0)
\]

或 active endpoint residue pair 映成：

\[
(G,u_0),\quad(\bar B_J,\bar A_J)
\]

之间的 cross-product。

因此 determinant \(1\) 目前只是一个**potential spacing asset**，不是 mantissa spacing theorem。

缺失接口准确写为：

```text
UNIMODULAR_SPACING_NOT_COUPLED_TO_ENDPOINT_DIFFERENCE
```

**T4 verdict：**

```text
95-R2-T4 = PROVED_AS_REDUNDANCY / ARCHITECTURE_KILL
MANTISSA_GAP = EXACT_W_REPACKAGING
NEW_LATTICE_CODIMENSION = 0
```

---

# Part VIII — 95-R2-T5: Resonant SRUS Collision Lemma

## 8.1 Positive successor × SRUS

对 positive sign，T3 给：

\[
\xi=UW\in\mathcal X_+(B_+,u_0),
\]

且：

\[
U\mid\xi.
\]

另一方面 SRUS/source recovery 要求：

\[
{U\over u_0}\in K^{\rm res}_{MN},
\qquad
\gcd(U,V)=1.
\]

因此 admissible \(U\) 必须属于：

\[
\boxed{
\mathcal U_+(\xi)
:=
\left\{
U:U\mid\xi,
\ \gcd(U,V)=1,
\ {U\over u_0}\in K^{\rm res}_{MN}
\right\}.
}
\tag{SRUS-SIEVE}
\]

于是：

\[
\boxed{
U
\in
\bigcup_{\xi\in\mathcal X_+(B_+,u_0)}
\mathcal U_+(\xi).
}
\]

这把原来的 common-\(U\) “区间中找 unit successor” 改写成：

\[
\boxed{
\text{有限 }\xi
\to
\text{有限 divisor }U
\to
\text{exact SRUS / endpoint replay}.
}
\]

这是 R2 对 SRUS 的真正新用途。

---

## 8.2 为什么没有 uniform cyclotomic-unit contradiction

要形成 Type C closure，需要证明：

\[
\mathcal U_+(\xi)=\varnothing
\]

对所有 admissible structural fibres 都成立。

当前做不到，原因有三层：

1. \(u_0=1\) 时 cyclotomic prime support 完全消失；
2. 即使 \(u_0>1\)，\(\xi\) 被强制与 \(u_0\) 互素，而非强制分享 prime；
3. SRUS 的真正 residue data 仍依赖 \(M,N\) / endpoint interval；当前没有 theorem 把这些 residue 与 \(10^g\equiv-1\pmod{u_0}\) 直接锁死。

因此 pure CRT 若不读取 active endpoint/source semantics，仍属于旧的 dead architecture。

---

## 8.3 H5.1 stress test

\(\mathcal H_{5,1}\) 有：

\[
J=5,\quad g=1,\quad d_*=\beta_0=1,
\]

\[
u_0\mid11,
\qquad
u=5^ru_0,
\qquad
n_3\ge2.
\]

positive successor bound 仅给：

\[
0<UW<u_0 10^{n_3-1}.
\]

右端随 \(n_3\) 指数增长。

所以即使 cyclotomic denominator 已经缩到：

\[
u_0\in\{1,11\},
\]

也没有 uniform finite successor across the family。

这说明：

\[
\boxed{
\mathcal H_{5,1}
\text{ 是 current cyclotomic-successor architecture 的 genuine stress fibre。}
}
\]

它不是“忘了搜的小 case”，而是 \(g=1\) 下 tail lock 退化导致的独立结构。

**T5 verdict：**

```text
95-R2-T5 = PROVED_AS_FINITE_POSITIVE_DIVISOR_SIEVE
SRUS_INTERSECTION = FINITE_PER_STRUCTURAL_FIBRE
SRUS_INTERSECTION_UNIFORMLY_EMPTY = NOT_PROVED
```

---

# Part IX — RRGS / Unimodular Envelope Audit

## 9.1 RRGS equations themselves do not create a second U-equation

因为：

\[
a_i=UC_i,
\qquad
\Xi=UW,
\]

RRGS-1 除以 \(U\) 后：

\[
Q_0-P_2+K_*W=u_0C_3,
\]

正是：

\[
d_2+S_R=P_3.
\]

RRGS-2 除以 \(U\) 后：

\[
d_*(10^{n_3}C_2+C_3)
={G+1\over u_0}W+\gamma JD_1.
\]

其代数主体仍是 deflated source/core 的 reduced-scale presentation。

因此 RRGS 的独立价值不是“又多两条 algebraic equations”，而是：

\[
\boxed{
\textbf{它把 actual digit inequalities 施加在 }\Xi=UW\textbf{ 上。}
}
\]

尤其 RRGS-3 才是 positive finite successor 的新增 cutting power。

---

## 9.2 determinant-1 asset保留，但必须等 endpoint bridge

由：

\[
u_0\bar B_J-G\bar A_J=1,
\]

可写 exact rational separation：

\[
\left|
{\bar B_J\over\bar A_J}
-{G\over u_0}
\right|
={1\over u_0\bar A_J}.
\]

这是一个 genuine Farey-like neighboring relation。

R2 的失败并不是 determinant 不够强，而是：

\[
\boxed{
\text{active endpoint / mantissa fraction 尚未被证明就是这两个 neighboring slopes 之间的第三个格点。}
}
\]

所以这项资产保留给 R3，不应在 R2 伪装成 closure。

---

# Part X — Counterexample / Failure Ledger

## 10.1 Arithmetic-kernel infinite pseudo-family

为了测试“cyclotomic + content + enhanced divisor + mantissa 是否本身已经足够”，定义对任意 \(g\ge1\)：

\[
G=10^g,
\qquad
J=G,
\]

并取：

\[
\beta=d_*=\beta_0=s=u=u_0=D=D_1=c_R=W=1,
\]

\[
Q_0=G+1,
\qquad
S_R=G.
\]

则逐项有：

\[
J={G\over\gcd(G,\beta)}=G,
\]

\[
c_R=1<J,
\]

\[
K_*=G\mid S_R,
\]

\[
uJD_1=G=Q_0-W,
\]

\[
u_0=1\mid G+1,
\]

以及：

\[
b_1JD-c_RQ_0
=G-(G+1)
=-1
=-s\beta_0W.
\]

并：

\[
\left|{G\over G+1}-1\right|
={1\over G+1}
<{1\over G}.
\]

所以这是一个对所有 \(g\) 存在的：

\[
\boxed{
\textbf{frozen arithmetic-kernel pseudo-family}.
}
\]

**重要：它不是 full source solution。** 它没有被宣称满足 primitive sphere / digit endpoint / SRUS。

它的作用是严格证明：

\[
\boxed{
\text{T1 + T2 + }K_*\mid S_R+\text{core+mantissa alone cannot close general resonance.}
}
\]

因此 missing independent information 必须来自 source geometry / endpoint / primitive compatibility，而不是继续在同一 arithmetic kernel 上制造同义式。

---

## 10.2 Killed conjectures

### C1 — “mantissa closeness gives a fresh lattice gap”

**KILLED EXACTLY** by：

\[
E_R=-s\beta_0W.
\]

### C2 — “cyclotomic prime support must collide with J/content”

**KILLED**：

\[
\gcd(u_0,Jd_*\beta_0)=1.
\]

### C3 — “primitive divisor theorem of \(10^g+1\) forces u0 to contain a new prime”

**KILLED**：\(u_0\) 只是任意 divisor；\(u_0=1\) 永远通过该 gate。

### C4 — “unimodular determinant automatically closes mantissa”

**NOT SOURCED**：determinant-1 pair 与 active endpoint difference之间缺 bridge。

### C5 — “positive successor is uniformly finite over H5.1”

**FALSE AS UNIFORM STATEMENT**：

\[
B_+=u_010^{n_3-1}\to\infty.
\]

### C6 — “J5 fixed-depth discriminant never square”

**FALSE**：唯一 exact near-survivor：

\[
\Delta'=991604^2.
\]

root divisibility 才杀死它。

---

# Part XI — 95-R2-T6: Non-J2 Resonance Compression Theorem

本轮没有证明：

\[
\mathcal H_R^{\rm gen}=\varnothing.
\]

也没有证明存在 finite exceptional \(J\)-set：

\[
\mathcal H_R^{\rm gen}
\subseteq
\bigcup_{J\in\mathcal J_{\rm exc}}\mathcal H_J,
\qquad
\#\mathcal J_{\rm exc}<\infty.
\]

但可以形成一个新的 sign-split canonical interface。

---

## 11.1 Positive class

定义 structural tuple：

\[
\Theta_+
:=(g,J,\beta_0,h,d_*,n_3,u_0).
\]

其中：

\[
1\le h\le\left\lfloor{J-1\over\beta_0}\right\rfloor,
\qquad
s=h/d_*,
\]

\[
\gcd(J,d_*)=1,
\qquad
u_0\mid10^g+1.
\]

则 positive full state 必须进一步选择：

\[
\xi\in\mathcal X_+(u_0d_*10^{n_3-g},u_0),
\]

再选择：

\[
U\mid\xi,
\qquad
W=\xi/U,
\]

并通过：

\[
{U\over u_0}\in K^{\rm res}_{MN},
\qquad
\gcd(U,V)=1,
\]

以及 primitive sphere / endpoint gates。

所以：

\[
\boxed{
\mathcal H_{R,+}^{\rm gen}
\to
(\Theta_+,\xi)
+\text{finite divisor allocation}
+\text{source replay}.
}
\tag{POS-NF}
\]

这是严格低于 R1 的 \((U,W)\)-free-moving interface。

---

## 11.2 Negative class

negative side 当前只能压到：

\[
\Theta_-=(g,J,\beta_0,h,d_*,u_0,Q_0,W),
\]

满足：

\[
0<|W|<{d_*Q_0\over G},
\]

再通过 SRUS / endpoint。

没有 structural bound 把 \(W\) 脱离 \(Q_0\)。

因此：

\[
\boxed{
\text{negative side 是本轮无法完成 Level B 的首要 obstruction。}
}
\]

---

## 11.3 T6 verdict

```text
95-R2-T6_EXTINCTION = NOT_PROVED
95-R2-T6_FINITE_EXCEPTIONAL_J = NOT_PROVED
95-R2-T6_REPLACEMENT = SIGN_SPLIT_SUCCESSOR_COMPRESSION
```

因此：

\[
\boxed{
\texttt{NONJ2_RESONANCE_COMPRESSED_NOT_CLOSED}.
}
\]

---

# Part XII — J5 Stress Test and Classification

## 12.1 \(\mathcal H_{5,2}\), \(\mathcal H_{5,3}\)

它们的 fixed-depth positive halves 完全符合 general positive successor picture：

\[
n_3=g,
\]

所以：

\[
0<UW<u_0d_*.
\]

这先把 \((U,W)\) 压成 finite successor；历史 fixed-depth axis theorem 再把 \(k\) 压成 finite interval；最后 square + root divisibility 完成 extinction。

因此这两支应被理解为：

\[
\boxed{
\text{general positive architecture 的 fixed-depth finite specialization}
+\text{J5-specific exponent locks}.
}
\]

不是孤立 brute force。

---

## 12.2 \(\mathcal H_{5,1}\)

这一支是 genuine J5 low-depth degeneracy：

\[
g=1,
\qquad
n_3\ge2,
\qquad
u=5^ru_0.
\]

它失去 \(g\ge2\) 时的 \(5\)-adic tail finiteization，并允许 decimal overlap \(5^r\) 留在 full \(u\) 中，而 cyclotomic theorem 只控制 reduced \(u_0\mid11\)。

因此：

\[
\boxed{
\mathcal H_{5,1}
\text{ 属于 J5-specific degeneracy，不应假装已被 general successor theorem 吸收。}
}
\]

它仍然 OPEN。

---

# Part XIII — Updated 95 Frontier

95-R1 给：

\[
A_1^{95,\rm live}
=
\mathcal H_0
\sqcup
\mathcal H_R^{\rm gen}
\sqcup
\mathcal H_{5,1}
\sqcup
\mathcal H_{5,2}
\sqcup
\mathcal H_{5,3}
\sqcup
\mathcal H_{T0}
\sqcup
\mathcal H_{T1}
\sqcup
\mathcal H_{O+}
\sqcup
\mathcal H_{O-}.
\]

R2 之后，把 \(\mathcal H_{5,2},\mathcal H_{5,3}\) 按 \(S_R\) 符号拆分，positive halves 已删除。

因此新的 global 95 frontier 可写成：

\[
\boxed{
\begin{aligned}
A_1^{95,\rm live}(R2)
={}&\mathcal H_0
\sqcup
\mathcal H_R^{\rm gen}
\sqcup
\mathcal H_{5,1}\\
&\sqcup
\mathcal H_{5,2}^{-}
\sqcup
\mathcal H_{5,3}^{-}
\sqcup
\mathcal H_{T0}
\sqcup
\mathcal H_{T1}
\sqcup
\mathcal H_{O+}
\sqcup
\mathcal H_{O-},
\end{aligned}
}
\tag{95-R2-MNF}
\]

其中 superscript \((- )\) 在这里**只表示 \(S_R<0\)**。

\(\mathcal H_R^{\rm gen}\) 内部进一步升级为：

\[
\boxed{
\mathcal H_R^{\rm gen}
=
\mathcal H_{R,+}^{\rm succ}
\sqcup
\mathcal H_{R,-}^{W},
}
\]

其中：

- \(\mathcal H_{R,+}^{\rm succ}\)：使用 `POS-NF` 的 finite-successor interface；
- \(\mathcal H_{R,-}^{W}\)：仍缺 structural \(W\)-bound。

与 R1 比较，真正删除的 information classes 是：

\[
\boxed{
\mathcal H_{5,2}^{+},
\qquad
\mathcal H_{5,3}^{+}.
}
\]

真正降低维数但没有删除的是：

\[
\boxed{
\mathcal H_{R,+}^{\rm gen}.
}
\]

---

# Part XIV — Redundancy / Novelty Audit

| Item | R2 verdict | Information effect |
|---|---|---|
| \(S_R/K_*=W\) | exact normalization | removes fake continuous ratio |
| \(c_R=\beta_0h,\ h=sd_*\) | new canonical packaging | removes independent \(s\) |
| \(\gcd(J,d_*)=1\) | explicit derived theorem | splits mixed/pure support regimes |
| cyclotomic order class | exact | restricts prime-power orders, not cardinality |
| \(E_R=-s\beta_0W\) | exact | kills fake mantissa-lattice independence |
| RRGS-3 + SRUS | genuinely new collision | \((U,W)\to(\xi,U\mid\xi)\) on positive side |
| unimodular determinant | retained asset | no endpoint bridge yet |
| generic CRT | rejected | no new global input |
| Zsigmondy-only route | insufficient | u0 need not contain primitive prime |
| J5 discriminant-only | false | exact square near-survivor |
| J5 square + root gate | certified | closes H5.2+, H5.3+ |

---

# Part XV — Failure Interface Ledger

```text
CYCLOTOMIC_CAPACITY_TOO_LARGE = YES
  witness: u0=1; arbitrary divisor selection; no uniform cardinality bound

ENDPOINT_INTERVAL_TOO_WIDE = POSITIVE:NO_PER_FIBRE / NEGATIVE:YES
  positive: xi finite per structural fibre
  negative: W bound still scales with Q0

NO_NONTRIVIAL_LATTICE_DIVISOR = YES
  reason: mantissa difference = -s beta0 W exactly

SRUS_INTERSECTION_NONEMPTY = NOT_UNIFORMLY_EXCLUDED
  positive SRUS is now finite divisor sieve, but no global emptiness theorem

J_DEPENDENCE_NOT_UNIFORM = YES
  content quotient h can grow with J; u0 capacity moves with g

FINITE_EXCEPTIONAL_J_REMAIN = NOT_REACHED
  no theorem reducing general resonance to finitely many J

J5_SPECIAL_DEGENERACY = YES
  H5.1 is the g=1 moving-n3 / moving-5-overlap stress fibre

UNIMODULAR_SPACING_NOT_COUPLED_TO_ENDPOINT_DIFFERENCE = YES
```

---

# Part XVI — R3 Launch Decision

R2 已经明确处决两条不应继续投入的路线：

1. **不要继续找 “更大的 generic mantissa gcd”**；
2. **不要继续做纯 cyclotomic prime-support / generic CRT**。

下一轮最值得攻击的新 interface 是：

\[
\boxed{
\textbf{Finite Successor }\xi
\times
\textbf{Exact Endpoint Phase}
\times
\textbf{Unimodular Determinant}
\times
\textbf{SRUS Source Replay}.
}
\]

建议 95-R3 的主目标定为：

\[
\boxed{
\textbf{Positive Resonant Successor–Endpoint Incidence}
\times
\textbf{Cyclotomic Unimodular Non-Hit}.
}
\]

核心输入不再是 free \(U,W\)，而是：

\[
\xi\in\mathcal X_+(B_+,u_0),
\qquad
U\mid\xi,
\qquad
W=\xi/U.
\]

然后真正读取 active endpoint residues：

\[
\delta_2=(-10^{n_2-1})\bmod C_2,
\qquad
\delta_3=(-10^{n_3-1})\bmod C_3,
\]

尝试构造一个 sourced determinant / cross-product：

\[
0<|\mathcal D_{\rm end}|<1
\]

或：

\[
0<|\mathcal D_{\rm end}|<\Lambda_{\rm arith}.
\]

同时 R3 必须有一个独立副任务：

\[
\boxed{
\textbf{Negative Signed-RRGS Capacity Test}.
}
\]

目标只有两个可能结果：

- 找到 negative analogue，把 \(|UW|\) 也压成 structural finite successor；
- 或严格证明当前 source inequalities 无法给出这种 bound，并据此把 negative side 转向另一 information class。

不应在 negative side 没有新 independent size input 时继续堆 modulus。

---

# Part XVII — Final Theorem Ledger

## 95-R2-T1 — Resonant Cyclotomic Capacity Lemma

**PROVED.**

对每个 \(p^a\mid u_0\)：

\[
\operatorname{ord}_{p^a}(10)=2d,
\qquad
d\mid g,
\qquad
g/d\text{ odd},
\]

且：

\[
\gcd(u_0,Jd_*\beta_0)=1.
\]

**No uniform finite \(u_0\)-class.**

---

## 95-R2-T2 — Resonant Content Compression Lemma

**PROVED.**

\[
h={c_R\over\beta_0}=sd_*,
\qquad
1\le h\le\left\lfloor{J-1\over\beta_0}\right\rfloor,
\]

\[
d_*\mid h,
\qquad
\gcd(J,d_*)=1,
\qquad
s=h/d_*.
\]

并得到 mixed / pure-2 / pure-5 support split。

---

## 95-R2-T3 — Enhanced Divisor Endpoint Lemma

**PROVED / SIGN-SPLIT.**

\[
{S_R\over K_*}=W.
\]

positive sign：

\[
\xi=UW
\in
\mathcal X_+(u_0d_*10^{n_3-g},u_0).
\]

negative sign：没有 corresponding structural finite bound。

---

## 95-R2-T4 — Mantissa Lattice Gap Lemma

**PROVED AS REDUNDANCY / NO-GO.**

\[
b_1JD-c_RQ_0=-s\beta_0W.
\]

因此 mantissa inequality 与 W-bound 等价；当前没有新增 \(\Lambda_R>s\beta_0\) 的 uniform spacing theorem。

---

## 95-R2-T5 — Resonant SRUS Collision Lemma

**PROVED AS POSITIVE FINITE DIVISOR SIEVE.**

\[
U\mid\xi,
\qquad
{U\over u_0}\in K^{\rm res}_{MN},
\qquad
\gcd(U,V)=1.
\]

positive source reconstruction 变成 finite divisor replay；uniform emptiness 未证明。

---

## 95-R2-T6 — Non-J2 Resonance Extinction / Exceptional-Fibre Theorem

**EXTINCTION NOT PROVED. FINITE-EXCEPTIONAL-J NOT PROVED.**

替代成果：

\[
\boxed{
\mathcal H_R^{\rm gen}
=
\mathcal H_{R,+}^{\rm succ}
\sqcup
\mathcal H_{R,-}^{W}.
}
\]

以及：

\[
\boxed{
\mathcal H_{5,2}^{+}=\mathcal H_{5,3}^{+}=\varnothing.
}
\]

---

# Part XVIII — Final Status

本轮不能写：

```text
NONJ2_RESONANCE_CLOSED
```

也不能写：

```text
NONJ2_RESONANCE_FINITE_EXCEPTIONAL
```

正确状态是：

```text
NONJ2_RESONANCE_COMPRESSED_NOT_CLOSED
```

其中最有价值的两项永久资产是：

\[
\boxed{
\textbf{positive resonance: }(U,W)\to\xi=UW\textbf{ finite successor}
}
\]

与：

\[
\boxed{
\textbf{mantissa difference is exactly }-s\beta_0W,
\textbf{ so the naive lattice-gap multiplication is dead.}
}
\]

而正式删除的历史 residuals 是：

\[
\boxed{
\mathcal H_{5,2}\cap\{S_R>0\}=\varnothing,
\qquad
\mathcal H_{5,3}\cap\{S_R>0\}=\varnothing.
}
\]

95-R3 应只在**新的 successor-conditioned endpoint interface**上继续，而不应复活已被 R2 证明冗余的 generic mantissa / prime-support 路线。

---

# Provenance Sources Used

本报告的历史 frozen input 来自以下已归档 artifacts：

1. `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`
2. `strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md`
3. `strict_layer_A1_resonance_state_after_RGCD_campaign.md`
4. `Part I — Executive Status.md`（RRGS / historical J5 fixed-depth exact enumeration report）
5. `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`
6. `strict_layer_A1_SRCU_state_after_campaign.md`

本轮新生成的 J5 certificate bundle 列于 Part II，并由 SHA-256 manifest 固化。
