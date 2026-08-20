# 95-R4 — Successor-Conditioned Primitive Root Gate × Source-Geometry Lift × Negative \(Ud_2\) Capacity × Architecture Repair-or-Kill

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Ownership:** \(A_1^{95}=A_1\cap\{J\neq2\}\)  
**Round:** 95-R4  
**Canonical output:** `95_R4_Successor_Conditioned_Primitive_Root_Gate_and_Negative_Ud2_Capacity.md`

---

# Part I — Executive Verdict

本轮完成。

最终 verdict：

```text
95_R4_STATUS = COMPLETE

POSITIVE_PRIMITIVE_ROOT_CLOSED = NO
POSITIVE_PRIMITIVE_ROOT_FINITE = YES_PER_STRUCTURAL_FIBRE
POSITIVE_PRIMITIVE_ROOT_EXACTIZED = YES

SUCCESSOR_CONDITIONED_PRIMITIVE_CONIC = ESTABLISHED
SUCCESSOR_TO_D2_UNIQUENESS = FALSE / NOT NEEDED
SUCCESSOR_TO_D2_FINITE_CAPACITY = ESTABLISHED

ROOT_DIVISIBILITY_GATE = ESTABLISHED
GENERAL_ROOT_DIVISIBILITY_EXTINCTION = NOT_PROVED
GENERAL_PRIMITIVE_C1_D2_COPRIMALITY = NOT_PROVED

H5_1_GLOBAL_TAIL = OPEN
H5_1_ROOT_GATE = FINITE_PER_FIXED_N3_FIBRE

NEGATIVE_UD2_VERDICT = UNIFORM_UD2_CAPACITY_ESTABLISHED
NEGATIVE_SIGNED_RRGS = REPAIRED_TO_FINITE_SUCCESSOR_PER_STRUCTURAL_FIBRE

R5_RECOMMENDATION = ARCHITECTURE_SHOCK_CHECKPOINT
```

因此 R4 的主线达到题设允许的：

\[
\boxed{\textbf{Level B/C — Primitive-root finiteization + exact root gate}}
\]

而不是 positive full extinction。

副线则达到最强等级：

\[
\boxed{\textbf{N-A — UNIFORM\_UD2\_CAPACITY\_ESTABLISHED}.}
\]

这里的 “uniform” 指：

\[
\boxed{
\text{上界不再含 }Q_0,C_2,C_3,d_2
}
\]

这些 moving primitive-height quantities；它仍允许依赖固定 structural fibre 的

\[
(g,k,n_3,u_0,b_1,\ldots).
\]

本轮最重要的结构变化有两个。

第一，R3 的

\[
(\xi,U,W)
\]

不再直接去撞 endpoint，而是通过 original primitive sphere 与 leading-defect/source core 得到一个 general-\(J\)、pre-\(J2\) 的 exact binary conic：

\[
\boxed{
F_{\Sigma,W}(C_1,d_2)=0.
}
\]

第二，R3 negative branch 缺失的

\[
Ud_2
\]

上界，事实上可以由 **general A1 \(P_2\)-axis theorem × signed RRGS × actual digit windows** 闭合；不需要 J2-specific axis chart。

---

# Part II — Frozen R3 Boundary

永久冻结：

\[
G:=10^g,\qquad n_2=2g+k,\qquad k\ge1.
\]

Exact resonance：

\[
P_2=10^{n_3}M,\qquad P_3=N,
\]

\[
C_2=\frac{M}{u_0},\qquad C_3=\frac{N}{u_0},
\]

\[
a_2=UC_2,\qquad a_3=UC_3,
\qquad \gcd(U,V)=1.
\]

定义 primitive axis gap：

\[
\boxed{d_2:=Q_0-P_2>0.}
\]

deflated resonance core：

\[
D=\beta_0D_1,
\]

\[
\boxed{uJD_1=d_*Q_0-W,}
\]

\[
\boxed{
S_R=\frac{G}{d_*}W.
}
\]

令：

\[
\boxed{K_*:=\frac G{d_*}.}
\]

于是：

\[
\boxed{S_R=K_*W.}
\]

cyclotomic reduced denominator：

\[
u_0\mid G+1,
\]

\[
\gcd(u_0,Q_0)=\gcd(u_0,S_R)=\gcd(u_0,10)=1.
\]

R3 positive finite successor：

\[
\boxed{\xi:=UW,}
\]

\[
0<\xi<u_0d_*10^{n_3-g},
\qquad
U\mid\xi,
\qquad
W=\frac{\xi}{U}.
\]

R3 的 genuine unimodular lower spacing 继续保留，但 endpoint collision architecture 已死亡：

```text
FINITE_SUCCESSOR_ENDPOINT_INCIDENCE_ARCHITECTURE_INSUFFICIENT
```

negative side 则冻结：

\[
\boxed{
0<U|W|<
\frac{d_*}{G}\,Ud_2.
}
\tag{R3-SIGNED}
\]

---

# Part III — Source Dependency Diagram

本轮恢复后的最小 source dependency graph：

```text
structural tuple Σ
    |
    | EXACT
    v
(G,k,n3,J,d*,β0,u,u0,V,g1,b1,K*)
    |
    +--------------------------+
    |                          |
    | EXACT                    | EXACT
    v                          v
successor (ξ,U,W)          source coefficients
W=ξ/U                       A=uJ+β0 d*
    |                          |
    |                          |
    | NOT_CONTROLLED            |
    +-------------> d2 <--------+
                       |
                       | EXACT + DIVISIBILITY
                       v
              C3=(d2+K*W)/u0
                       |
                       +-------------------+
                       |                   |
                       | EXACT             | EXACT NEW SOURCE INFORMATION
                       v                   v
                 P3=d2+K*W       F_{Σ,W}(C1,d2)=0
                                           |
                                           | SQUARE + ROOT DIVISIBILITY
                                           v
                                          C1
                                           |
                                           | EXACT + DIVISIBILITY
                                           v
                  Q0=(uJ g1 C1 10^k+β0 W)/A
                                           |
                                           +--------------------+
                                           |                    |
                                           v                    v
                            C2=(Q0-d2)/(u0 10^n3)      primitive/gcd profile
                                           |                    |
                                           +---------+----------+
                                                     |
                                                     v
                                             SRUS / exact words
                                                     |
                                                     v
                                             original source replay
```

R3 缺失的桥现在可以精确描述：

\[
\boxed{
\text{successor 不唯一决定 }d_2,
}
\]

但 R4 新增：

\[
\boxed{
\text{successor}
+
\text{primitive conic}
+
\text{axis capacity}
\Longrightarrow
\text{fixed fibre 内有限 }d_2.
}
\]

所以原来的 `NOT_CONTROLLED` 并没有被伪装成 `EXACT`，而是被升级为：

```text
SUCCESSOR -> d2 : FINITE + INEQUALITY
```

这是 R4 的真正 information cut。

---

# Part IV — Canonical Primitive Equations

## 4.1 Resonance Smith/source dictionary

在 exact resonance：

\[
\alpha=t=1,\qquad v=10^{n_3}.
\]

Full Smith gcd profile 给：

\[
g_1=\beta v_0,
\]

其中：

\[
u=\gamma u_0,
\qquad
v=\gamma v_0,
\qquad
\gcd(u_0,v_0)=1.
\]

并有：

\[
P_1=g_1C_1,
\]

\[
P_2=u_0 10^{n_3}C_2,
\]

\[
P_3=u_0C_3.
\]

primitive sphere：

\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2,
}
\tag{SPH}
\]

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\tag{PRIM}
\]

---

## 4.2 \(W\) 的 primitive exact semantics

由：

\[
S_R=P_2+P_3-Q_0
\]

与：

\[
d_2=Q_0-P_2,
\]

得到：

\[
S_R=P_3-d_2.
\]

又：

\[
S_R=K_*W.
\]

因此：

\[
\boxed{
P_3-d_2=K_*W.
}
\tag{W-SEM}
\]

即：

\[
\boxed{
W=\frac{P_3-d_2}{K_*}
=\frac{u_0C_3-d_2}{K_*}.
}
\]

所以 \(W\) 不是普通 remainder；它的最准确 primitive 语义是：

\[
\boxed{
\textbf{deflated signed displacement between }
P_3
\textbf{ and the }P_2\textbf{-axis gap }d_2.
}
\]

于是：

\[
\boxed{
C_3=\frac{d_2+K_*W}{u_0}.
}
\tag{C3}
\]

这是 exact source reconstruction，要求：

\[
\boxed{
u_0\mid d_2+K_*W.
}
\tag{C3-DIV}
\]

---

## 4.3 Leading defect 与 deflated core 的 exact splice

A1 leading defect：

\[
\boxed{
D=P_110^k-Q_0.
}
\tag{LD}
\]

又：

\[
D=\beta_0D_1,
\]

\[
uJD_1=d_*Q_0-W.
\]

代入：

\[
uJ(P_110^k-Q_0)
=
\beta_0(d_*Q_0-W).
\]

整理：

\[
\boxed{
(uJ+\beta_0d_*)Q_0
=
uJP_110^k+\beta_0W.
}
\]

定义：

\[
\boxed{
A:=uJ+\beta_0d_*.
}
\tag{ADEF}
\]

再代入 \(P_1=g_1C_1\)：

\[
\boxed{
AQ_0
=
uJg_1C_110^k+\beta_0W.
}
\tag{Q-LIN}
\]

即：

\[
\boxed{
Q_0=
\frac{uJg_1C_110^k+\beta_0W}{A}.
}
\tag{QREC}
\]

因此 source 必须满足：

\[
\boxed{
A\mid uJg_1C_110^k+\beta_0W.
}
\tag{QDIV}
\]

---

# Part V — Elimination and Root Construction

## 5.1 消去 \(C_2,C_3,Q_0\)

由：

\[
P_2=Q_0-d_2,
\]

\[
P_3=d_2+K_*W,
\]

sphere 成为：

\[
g_1^2C_1^2+(Q_0-d_2)^2+(d_2+K_*W)^2=Q_0^2.
\]

约去 \(Q_0^2\)：

\[
g_1^2C_1^2
+d_2^2
+(d_2+K_*W)^2
-2d_2Q_0
=0.
\]

代入 \(Q_0\) 的线性公式并乘 \(A\)，得到：

\[
\boxed{
\begin{aligned}
F_{\Sigma,W}(C_1,d_2)
:={}&
A g_1^2C_1^2
-2uJg_1 10^k d_2 C_1\\
&+
A\Bigl[d_2^2+(d_2+K_*W)^2\Bigr]
-2\beta_0Wd_2
=0.
\end{aligned}
}
\tag{PRIM-CONIC}
\]

这是本轮 central theorem。

它是：

\[
\boxed{
\textbf{general-}J,\quad
\textbf{pre-}J2,\quad
\textbf{exact},\quad
\textbf{source-equivalent up to the recorded divisibility replay}.
}
\]

并且它确实包含 R3 所缺失的 primitive sphere information。

---

## 5.2 为什么自然得到 binary conic，而不是单变量 polynomial

固定：

\[
(\Sigma,\xi,U,W)
\]

后，\(W\) 被固定，但：

\[
d_2
\]

并没有由 RRGS/endpoint 唯一决定。

因此当前 source equations 自然产生：

\[
\boxed{
F_{\Sigma,W}(C_1,d_2)=0,
}
\]

而不是一个不含 moving parameter 的：

\[
F_{\xi,U}(X)=0.
\]

这不是失败包装。

R4 的修复是：

\[
\boxed{
\text{用 independent }P_2\text{-axis theorem 把 }d_2
\text{ 压成 fixed-fibre finite set}.
}
\]

之后每个 \(d_2\) 都给一个真正的 quadratic root gate。

---

# Part VI — Root Divisibility Audit

## 6.1 Reduced discriminant

把 primitive conic 视为 \(C_1\) 的 quadratic：

\[
aC_1^2+bC_1+c=0,
\]

其中：

\[
a=A g_1^2,
\]

\[
b=-2uJg_1 10^k d_2,
\]

\[
c=
A\Bigl[d_2^2+(d_2+K_*W)^2\Bigr]
-2\beta_0Wd_2.
\]

full discriminant：

\[
\Delta_{\rm full}
=
4g_1^2\Delta_{\rm prim},
\]

其中：

\[
\boxed{
\Delta_{\rm prim}
=
(uJd_210^k)^2
-
A^2\Bigl[d_2^2+(d_2+K_*W)^2\Bigr]
+
2A\beta_0Wd_2.
}
\tag{DISC}
\]

任何 source survivor 必须：

\[
\boxed{
\Delta_{\rm prim}=R^2,
\qquad R\in\mathbf Z_{\ge0}.
}
\tag{SQ}
\]

---

## 6.2 Integral root is strictly stronger

根化简为：

\[
\boxed{
C_1
=
\frac{uJd_210^k\pm R}{A g_1}.
}
\tag{ROOT}
\]

所以合法 root 必须满足：

\[
\boxed{
A g_1
\mid
uJd_210^k\pm R,
}
\tag{ROOT-DIV}
\]

并且：

\[
C_1>0.
\]

因此：

\[
\boxed{
\Delta_{\rm prim}=\square
\neq
\text{source root}.
}
\]

这正是 R2 的 \(J=5\) certificate 所展示的 general lesson。

---

## 6.3 R2 J5 gate 被严格恢复为本公式的 specialization

当：

\[
\beta_0=1,
\qquad
u=u_0,
\]

则：

\[
A=u_0J+d_*.
\]

而：

\[
d_2+K_*W=u_0C_3.
\]

所以：

\[
\Delta_{\rm prim}
=
(d_2u_0J10^k)^2
-
A^2(d_2^2+u_0^2C_3^2)
+
2Ad_2W,
\]

正是 R2 的 \(J5\)-DISC。

根：

\[
C_1=
\frac{d_2u_0J10^k\pm R}{Ag_1},
\]

也正是 R2 的 \(J5\)-ROOT。

因此：

\[
\boxed{
\textbf{J5 root gate 不是 J5 accident；
它确实来自 general pre-specialization primitive conic。}
}
\]

---

## 6.4 Coefficient gcd audit

由 resonance support complementarity：

\[
\gcd(J,d_*)=1.
\]

又因为：

\[
\gcd(u,\beta)=1,
\qquad
\beta=(G/J)d_*\beta_0,
\]

得到：

\[
\gcd(u,d_*)=\gcd(u,\beta_0)=1.
\]

且 \(\beta_0\) ten-free，而 \(J,d_*\) 仅有 \(2,5\)-support，因此：

\[
\gcd(J,\beta_0)=\gcd(d_*,\beta_0)=1.
\]

所以：

\[
A=uJ+\beta_0d_*
\]

满足：

\[
\boxed{
\gcd(A,u)=
\gcd(A,J)=
\gcd(A,d_*)=
\gcd(A,\beta_0)=1.
}
\tag{A-UNIT}
\]

这是 genuine root-content information。

但本轮没有证明：

\[
A g_1\nmid uJd_210^k\pm R
\]

对所有 non-\(J2\) candidate 恒成立。

所以：

```text
ROOT_DIVISIBILITY_GATE = GENUINE
GENERAL_ROOT_DIVISIBILITY_EXTINCTION = NOT_PROVED
```

---

# Part VII — Primitive / Source Replay

一个 \((\Sigma,\xi,U)\) survivor 的合法 replay 顺序现在应冻结为：

1. 计算：
   \[
   W=\xi/U;
   \]

2. 利用本轮 capacity theorem 枚举有限：
   \[
   d_2;
   \]

3. 检查：
   \[
   u_0\mid d_2+K_*W,
   \]
   并恢复：
   \[
   C_3=(d_2+K_*W)/u_0;
   \]

4. 构造：
   \[
   \Delta_{\rm prim};
   \]

5. 要求：
   \[
   \Delta_{\rm prim}=R^2;
   \]

6. 检查两个 root：
   \[
   A g_1\mid uJd_210^k\pm R;
   \]

7. 恢复正整数：
   \[
   C_1;
   \]

8. 恢复：
   \[
   Q_0=
   \frac{uJg_1C_110^k+\beta_0W}{A};
   \]

9. 要求：
   \[
   u_010^{n_3}\mid Q_0-d_2,
   \]
   并恢复：
   \[
   C_2=\frac{Q_0-d_2}{u_010^{n_3}};
   \]

10. primitive normalization：
    \[
    \gcd(P_1,P_2,P_3,Q_0)=1;
    \]

11. exact Smith gcd profile：
    \[
    g_i=\gcd(V,P_i)
    \]
    必须恢复原 profile，而不是只检查 \(g_i\mid P_i\)；

12. numerator digit windows：
    \[
    10^{n_2-1}\le UC_2<10^{n_2},
    \]
    \[
    10^{n_3-1}\le UC_3<10^{n_3};
    \]

13. SRUS：
    \[
    U/u_0\in K_{MN};
    \]

14. unit gate：
    \[
    \gcd(U,V)=1;
    \]

15. exact full-word/original source replay。

---

## 7.1 Primitive gcd firewall：不能非法搬运 J2 theorem

J2 历史曾证明：

\[
\gcd(C_1,d_2)=1.
\]

但其 proof 使用 J2-specific Euclidean rows 与 sphere propagation。

本轮没有 general-\(J\) source theorem 支撑：

\[
\boxed{\gcd(C_1,d_2)=1}
\]

对全部 non-\(J2\) resonance 成立。

因此正式冻结：

```text
GENERAL_C1_D2_COPRIMALITY = NOT_PROVED
J2_C1_D2_COPRIMALITY_TRANSFER = ILLEGAL
```

R4 的 primitive gate 采用原始：

\[
\gcd(P_1,P_2,P_3,Q_0)=1
\]

与 exact Smith profile，而不是偷搬 J2 coprimality。

---

# Part VIII — Positive Primitive-Root Finiteization

这是 R4 的 principal success。

## 8.1 General A1 \(d_2\) axis theorem

历史 general A1 theorem 给：

\[
d_2
<
\frac{Q_0}{10^{2k}}
\left[
\left(1+\frac1{b_1}\right)^2
+
10^{4-4g}
\right].
\]

定义：

\[
\boxed{
\chi
:=
10^{-2k}
\left[
\left(1+\frac1{b_1}\right)^2
+
10^{4-4g}
\right].
}
\tag{CHI}
\]

则：

\[
\boxed{d_2<\chi Q_0.}
\tag{AX}
\]

由于：

\[
g\ge1,\quad k\ge1,\quad b_1\ge1,
\]

有：

\[
\left(1+\frac1{b_1}\right)^2\le4,
\qquad
10^{4-4g}\le1,
\]

所以：

\[
\boxed{
0<\chi\le\frac5{100}=0.05<1.
}
\tag{CHI<1}
\]

这一严格小于 1 是 negative capacity 修复的关键。

---

## 8.2 Signed exact \(UQ_0\) identity

由：

\[
Q_0=P_2+d_2
=
u_010^{n_3}C_2+d_2,
\]

以及：

\[
Ud_2+K_*\xi=u_0a_3
\]

在 \(W>0\) 下可写：

\[
\boxed{
UQ_0
=
u_0(10^{n_3}a_2+a_3)
-
K_*\xi.
}
\tag{UQ+}
\]

actual digit windows：

\[
a_2<10^{n_2},
\qquad
a_3<10^{n_3}.
\]

定义纯 structural upper budget：

\[
\boxed{
B_0
:=
u_0\,10^{n_3}\left(10^{n_2}+1\right)
=
u_0\,10^{n_3}\left(10^{2g+k}+1\right).
}
\tag{B0}
\]

于是 positive：

\[
\boxed{
UQ_0<B_0.
}
\]

axis theorem 给：

\[
Ud_2<\chi UQ_0.
\]

故：

\[
\boxed{
Ud_2<\chi B_0.
}
\tag{POS-UD2}
\]

从而：

\[
\boxed{
1\le d_2<
\frac{\chi B_0}{U}.
}
\tag{D2-FIN}
\]

这不含 \(Q_0,C_2,C_3,d_2\) 本身。

---

## 8.3 Positive Primitive-Root Fibre Finiteization Theorem

固定 structural fibre：

\[
\Sigma
=
(g,k,n_3,J,d_*,\beta_0,u,u_0,V,g_1,b_1,\ldots)
\]

与一个 R2 successor：

\[
(\xi,U,W),
\qquad W=\xi/U>0.
\]

则：

\[
d_2
\]

只能取有限多个正整数：

\[
1\le d_2<\chi B_0/U.
\]

对每个 \(d_2\)，primitive conic 对 \(C_1\) 是 quadratic，因此至多两个 algebraic roots；合法 source root 还要通过：

\[
\Delta_{\rm prim}=\square,
\]

\[
Ag_1\mid uJd_210^k\pm\sqrt{\Delta_{\rm prim}},
\]

以及完整 source replay。

所以：

\[
\boxed{
\textbf{每个 positive successor 在 fixed structural fibre 内只允许有限 exact primitive roots。}
}
\]

正式 verdict：

```text
POSITIVE_PRIMITIVE_ROOT_FINITE = YES_PER_STRUCTURAL_FIBRE
POSITIVE_PRIMITIVE_ROOT_CLOSED = NO
```

---

# Part IX — \(J=5,\mathcal H_{5,1}\) Stress Test

\(\mathcal H_{5,1}\)：

\[
J=5,
\qquad
g=1,
\qquad
d_*=1,
\qquad
\beta=2,
\qquad
\beta_0=1,
\]

\[
u=5^r u_0,
\qquad
u_0\mid11,
\qquad
n_3\ge2,
\qquad
0\le r\le n_3.
\]

因为：

\[
\gamma=5^r,
\]

\[
v_0=\frac{10^{n_3}}{5^r},
\]

故：

\[
\boxed{
g_1
=
\beta v_0
=
\frac{2\,10^{n_3}}{5^r}
=
2^{n_3+1}5^{n_3-r}.
}
\]

并且：

\[
K_*=10,
\]

\[
A=5u+1.
\]

primitive conic 专化为：

\[
\boxed{
\begin{aligned}
&(5u+1)g_1^2C_1^2
-10u g_1 10^k d_2C_1\\
&\qquad
+(5u+1)\Bigl[d_2^2+(d_2+10W)^2\Bigr]
-2Wd_2
=0.
\end{aligned}
}
\tag{H51-CONIC}
\]

reduced discriminant：

\[
\boxed{
\begin{aligned}
\Delta_{5,1}
={}&
(5u d_210^k)^2\\
&-(5u+1)^2
\Bigl[d_2^2+(d_2+10W)^2\Bigr]\\
&+2(5u+1)Wd_2.
\end{aligned}
}
\]

root：

\[
\boxed{
C_1
=
\frac{5u d_210^k\pm\sqrt{\Delta_{5,1}}}
{(5u+1)g_1}.
}
\]

因此 H5.1 已经真正进入：

```text
SQUARE
+
ROOT_DIVISIBILITY
+
SOURCE_REPLAY
```

而不再只是 successor/endpoints。

但是 positive \(d_2\) bound 中：

\[
B_0
=
u_0 10^{n_3}(10^{k+2}+1)
\]

仍随 \(n_3\) 增长。

所以：

\[
\boxed{
\mathcal H_{5,1}
\textbf{ 对每个 fixed }n_3\textbf{ fibre finite，}
}
\]

但：

\[
\boxed{
n_3\to\infty
}
\]

的 global tail 没有被本轮 uniform extinguish。

准确 stress verdict：

```text
H5_1_ROOT_GATE = FINITE_PER_FIXED_N3_FIBRE
H5_1_GLOBAL_TAIL = OPEN
TAIL_PARAMETER_REMAINS_FREE = YES
```

本轮没有构造 source-valid infinite survivor，因此不能写：

```text
PRIMITIVE_REPLAY_SURVIVES
```

作为 theorem；当前结论只是 global uniform finiteization 未得到。

---

# Part X — Negative \(Ud_2\) Capacity

这是 R4 最强的新 theorem。

## 10.1 Signed exact identity

negative branch：

\[
W<0.
\]

令：

\[
\boxed{\xi_-:=U|W|>0.}
\]

R3 给：

\[
\boxed{
0<\xi_-<
\frac{d_*}{G}Ud_2
=
\frac{Ud_2}{K_*}.
}
\tag{NEG-RRGS}
\]

所以：

\[
\boxed{
K_*\xi_-<Ud_2.
}
\tag{NEG-FB}
\]

另一方面 exact \(UQ_0\) 变成：

\[
\boxed{
UQ_0
=
u_0(10^{n_3}a_2+a_3)
+
K_*\xi_-.
}
\tag{UQ-}
\]

digit windows 给：

\[
u_0(10^{n_3}a_2+a_3)<B_0.
\]

因此：

\[
UQ_0
<
B_0+K_*\xi_-
<
B_0+Ud_2.
\]

---

## 10.2 Feedback absorption

axis theorem：

\[
Ud_2<\chi UQ_0.
\]

代入：

\[
Ud_2
<
\chi(B_0+Ud_2).
\]

于是：

\[
(1-\chi)Ud_2<\chi B_0.
\]

因为：

\[
0<\chi<1,
\]

可除：

\[
\boxed{
Ud_2
<
\frac{\chi}{1-\chi}\,B_0.
}
\tag{UD2-CAP}
\]

即显式：

\[
\boxed{
Ud_2
<
\frac{\chi}{1-\chi}\,
u_0\,10^{n_3}
\left(10^{2g+k}+1\right),
}
\]

其中：

\[
\boxed{
\chi
=
10^{-2k}
\left[
\left(1+\frac1{b_1}\right)^2
+
10^{4-4g}
\right]
<1.
}
\]

右端完全不含：

\[
Q_0,\quad C_2,\quad C_3,\quad d_2.
\]

因此：

\[
\boxed{
\texttt{UNIFORM\_UD2\_CAPACITY\_ESTABLISHED}.
}
\]

---

## 10.3 Negative signed RRGS becomes finite

再由：

\[
U|W|<
\frac{d_*}{G}Ud_2,
\]

得到：

\[
\boxed{
U|W|
<
\frac{d_*}{G}
\frac{\chi}{1-\chi}
u_0\,10^{n_3}
\left(10^{2g+k}+1\right).
}
\tag{NEG-SUCC}
\]

所以 fixed structural fibre 中 negative branch 也成为 finite successor problem。

R3 的：

```text
SIGNED_RRGS_PARTIAL
```

在 R4 后升级为：

```text
SIGNED_RRGS_FINITE_PER_STRUCTURAL_FIBRE
```

这是一个真正的 architecture repair，而不是符号重写。

---

# Part XI — Counterexample / Failure Ledger

| Conjecture | R4 verdict | Reason |
|---|---|---|
| fixed successor determines \(d_2\) | FALSE / R3-killed | \(d_2\) remains source variable |
| fixed successor determines \(C_3\) | FALSE | \(C_3=(d_2+K_*W)/u_0\) |
| \(\Delta\) never square | FALSE | R2 H5.3 exact square near-survivor |
| square discriminant implies source root | FALSE | root denominator divisibility is independent necessary gate |
| square root numerator is never divisible | NOT PROVED GENERALLY | H5.3 gives one failure, not uniform theorem |
| \(Ud_2\) structurally bounded | TRUE | theorem (UD2-CAP) |
| H5.1 dies by same uniform finite bound | FALSE AS GLOBAL CLAIM | capacity still grows with moving \(n_3\) |
| primitive sphere always kills large successor | NOT PROVED | sphere becomes exact conic, no uniform extinction |
| general \(\gcd(C_1,d_2)=1\) | NOT PROVED / ILLEGAL J2 TRANSFER | J2 proof uses special Euclidean rows |
| current equations give univariate successor polynomial without \(d_2\) | NOT OBTAINED | natural exact object is binary conic |
| more endpoint sharpening is needed | REJECTED | new cut comes from axis + primitive source geometry |

---

# Part XII — Information Independence Audit

## 12.1 Genuine new information

### A. Primitive conic

\[
F_{\Sigma,W}(C_1,d_2)=0
\]

uses：

- primitive sphere；
- leading defect；
- deflated resonance core；
- exact \(W\)-semantics。

它不是 RRGS、endpoint 或 \(W\)-definition 的单纯重写。

```text
PRIMITIVE_CONIC_NOVELTY = PASS
```

### B. Root divisibility

\[
Ag_1\mid uJd_210^k\pm R
\]

比：

\[
\Delta_{\rm prim}=R^2
\]

严格更强。

```text
ROOT_DIVISIBILITY_NOVELTY = PASS
```

### C. Negative capacity

\[
Ud_2<
\frac{\chi}{1-\chi}B_0
\]

来自：

\[
\text{general A1 axis}
\times
\text{signed RRGS}
\times
\text{digit windows}.
\]

它不是旧：

\[
|W|<d_*Q_0/G
\]

的循环重写，因为 \(Q_0\) 已被完全消去。

```text
NEGATIVE_CAPACITY_NOVELTY = PASS
```

---

## 12.2 Derived / non-new pieces

\[
C_3=(d_2+K_*W)/u_0
\]

本身只是：

\[
P_3-d_2=K_*W
\]

的 exact reconstruction。

```text
C3_FORMULA = EXACT_BUT_NOT_NEW_CODIMENSION
```

RRGS 模 \(U\) 仍只恢复旧 radial divisibility。

```text
RRGS_MOD_U = REDUNDANT
```

mantissa gap 与 enhanced-divisor ratio 继续保持 R2 的 redundancy verdict。

---

# Part XIII — Updated 95 Frontier

集合层面，R4 没有诚实删除新的 full source class。

所以：

\[
\boxed{
A_1^{95,\mathrm{live}}(R4)
=
A_1^{95,\mathrm{live}}(R3).
}
\]

即仍为：

\[
\boxed{
\begin{aligned}
A_1^{95,\mathrm{live}}(R4)
={}&
\mathcal H_0
\sqcup
\mathcal H_R^{\rm gen}
\sqcup
\mathcal H_{5,1}\\
&\sqcup
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

但 resonance information representation 发生了两次实质升级。

R3：

\[
\mathcal H_R^{\rm gen}
=
\mathcal H_{R,+}^{\rm succ}
\sqcup
\mathcal H_{R,-}^{W}.
\]

R4 后应改写为：

\[
\boxed{
\mathcal H_R^{\rm gen}
=
\mathcal H_{R,+}^{\rm root-fin}
\sqcup
\mathcal H_{R,-}^{\rm succ-fin},
}
\]

其中：

- \(\mathcal H_{R,+}^{\rm root-fin}\)：fixed structural fibre 内 finite successor，且每个 successor 进一步 finite primitive roots；
- \(\mathcal H_{R,-}^{\rm succ-fin}\)：通过 \(Ud_2\) capacity 获得 fixed-fibre finite signed successor，并可进入同一 primitive conic replay。

因此虽然 set frontier 未缩小，information dimension 已实质下降。

---

# Part XIV — Theorem Ledger

## 95-R4-T1 — Source Geometry Lift

定义：

\[
A=uJ+\beta_0d_*.
\]

则 genuine source state 满足：

\[
P_1=g_1C_1,
\]

\[
P_2=u_010^{n_3}C_2,
\]

\[
P_3=d_2+K_*W=u_0C_3,
\]

\[
AQ_0=uJg_1C_110^k+\beta_0W.
\]

**Status:** PROVED.

---

## 95-R4-T2 — Successor-Conditioned Primitive Conic

\[
\boxed{
\begin{aligned}
0={}&
A g_1^2C_1^2
-2uJg_110^kd_2C_1\\
&+
A[d_2^2+(d_2+K_*W)^2]
-2\beta_0Wd_2.
\end{aligned}}
\]

**Status:** PROVED.

---

## 95-R4-T3 — Root Divisibility Gate

\[
\Delta_{\rm prim}=R^2,
\]

\[
C_1=
\frac{uJd_210^k\pm R}{Ag_1}
\in\mathbf Z_{>0}.
\]

故必要：

\[
Ag_1\mid uJd_210^k\pm R.
\]

**Status:** PROVED.

---

## 95-R4-T4 — Primitive / Source Replay Gate

必须继续检查：

\[
u_0\mid d_2+K_*W,
\]

\[
A\mid uJg_1C_110^k+\beta_0W,
\]

\[
u_010^{n_3}\mid Q_0-d_2,
\]

primitive quadruple gcd、exact Smith profile、digits、SRUS、\(\gcd(U,V)=1\)、original source replay。

general：

\[
\gcd(C_1,d_2)=1
\]

**NOT PROVED**。

---

## 95-R4-T5 — Positive Primitive-Root Fibre Finiteization

令：

\[
\chi
=
10^{-2k}
\left[
(1+1/b_1)^2+10^{4-4g}
\right],
\]

\[
B_0=u_010^{n_3}(10^{2g+k}+1).
\]

则 positive branch：

\[
\boxed{
Ud_2<\chi B_0.
}
\]

所以 fixed structural fibre 与 successor 下 \(d_2\) finite，且每个 \(d_2\) 至多两个 root。

**Status:** PROVED.

**Verdict:**

```text
POSITIVE_PRIMITIVE_ROOT_FINITE
```

不是 closed。

---

## 95-R4-T6 — Negative \(Ud_2\) Capacity

\[
\boxed{
Ud_2
<
\frac{\chi}{1-\chi}
u_010^{n_3}(10^{2g+k}+1).
}
\]

并：

\[
\boxed{
U|W|
<
\frac{d_*}{G}
\frac{\chi}{1-\chi}
u_010^{n_3}(10^{2g+k}+1).
}
\]

**Status:** PROVED.

**Verdict:**

```text
UNIFORM_UD2_CAPACITY_ESTABLISHED
```

---

# Part XV — R5 Architecture Shock Checkpoint Input

R4 之后不建议直接写普通 R5 resonance 数学攻击。

前四轮已经形成足够清晰的 architecture inventory。

## 15.1 R1-R4 真正减少 information dimension 的 theorem

1. R1：
   - full \(A_1\) historical recovery；
   - non-\(J2\) frontier freeze；
   - exact resonance \(J\)-support / RGCD / Smith / SRUS 资产恢复。

2. R2：
   - positive finite successor：
     \[
     \xi=UW;
     \]
   - H5.2+, H5.3+ exact closure；
   - discriminant-only hypothesis 被反例处决。

3. R3：
   - unimodular cross-product genuine；
   - endpoint bridge falsified；
   - negative signed RRGS 精确压成只缺 \(Ud_2\) capacity。

4. R4：
   - general-\(J\) successor-conditioned primitive conic；
   - root divisibility gate；
   - positive fixed-fibre primitive-root finiteization；
   - negative \(Ud_2\) capacity；
   - negative signed finite successor repair。

---

## 15.2 死亡 architectures

正式列入 R5 shock inventory：

```text
GENERIC_ENDPOINT_UNIMODULAR_COLLISION
MANTISSA_GAP_REVIVAL
ENHANCED_DIVISOR_ENDPOINT_REVIVAL
PURE_CYCLOTOMIC_SUPPORT_CLOSURE
GENERIC_SRUS_RESIDUE_PILEUP
DISCRIMINANT_ONLY_EXTINCTION
ILLEGAL_J2_ROOT_ARCHITECTURE_TRANSFER
GENERAL_C1_D2_COPRIMALITY_ASSUMPTION
```

---

## 15.3 Resonance 当前最小接口

positive：

\[
\boxed{
\text{finite successor}
\to
\text{finite }d_2
\to
\text{quadratic root}
\to
\text{source replay}.
}
\]

negative：

\[
\boxed{
\text{new }Ud_2\text{ capacity}
\to
\text{finite signed successor}
\to
\text{same primitive conic replay}.
}
\]

所以 resonance 当前真正剩下的 obstruction 已经不是：

\[
\text{endpoint freedom}
\]

也不是：

\[
\text{negative unbounded }W.
\]

而是：

\[
\boxed{
\textbf{moving structural tail}
+
\textbf{lack of a second global source codimension}.
}
\]

最明显实例即：

\[
\boxed{
\mathcal H_{5,1}:\ n_3\to\infty.
}
\]

---

## 15.4 尚未投入的战区

仍然有：

\[
\mathcal H_0,
\quad
\mathcal H_{T0},
\quad
\mathcal H_{T1},
\quad
\mathcal H_{O+},
\quad
\mathcal H_{O-}.
\]

因此 95 不应无限把所有额度继续投入 resonance。

---

## 15.5 R5 decision input

建议 R5 正式作为：

\[
\boxed{
\textbf{First 95 Architecture Shock Checkpoint}
}
\]

而不是普通第五轮补丁。

checkpoint 应回答：

1. resonance 经过 R2-R4 后，剩余 global tail 是否还有一个值得总攻的 independent invariant；
2. H5.1 moving \(n_3\) 是否能通过 coefficient-height / root-divisibility / Smith-profile growth 形成真正 uniform cut；
3. 若没有，是否应暂时冻结 resonance，把额度切到 transition / outer；
4. 哪些 R1-R4 assets 能迁移出 resonance；
5. 是否存在一个可以统一 positive/negative root replay 的 computational certificate architecture，而不再次陷入 fixed-prefix brute force。

---

# Final R4 Statement

R4 没有证明：

\[
\mathcal H_{R,+}^{\rm succ}=\varnothing.
\]

但它已经完成题设的 Success 路径：

\[
\boxed{
\textbf{finite successor 被真正提升到 primitive/source exact root gate。}
}
\]

更准确地：

\[
\boxed{
(\Sigma,\xi,U,W)
\longrightarrow
\text{finite }d_2
\longrightarrow
F_{\Sigma,W}(C_1,d_2)=0
\longrightarrow
\text{square + root divisibility + source replay}.
}
\]

同时 negative side 获得：

\[
\boxed{
\texttt{UNIFORM\_UD2\_CAPACITY\_ESTABLISHED}.
}
\]

所以 R3 的核心缺口：

\[
\boxed{
\text{primitive/source geometry 没有进入 successor architecture}
}
\]

在 R4 已被修复。

当前真正剩余的问题已经转移为：

\[
\boxed{
\textbf{如何把 fixed-fibre root finiteization
提升成 moving-structural-tail extinction。}
}
\]

这正是 R5 architecture shock checkpoint 应清算的问题，而不是再返回 endpoint patching。
