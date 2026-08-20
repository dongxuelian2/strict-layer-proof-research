# 三项十进制拼接平方和问题：Backward Strict Layer — A1 Common-\(U\) Pullback / Primitive–Radial Gluing Campaign

**文件名：** `strict_layer_backward_A1_common_U_pullback_primitive_radial_gluing_campaign.md`  
**日期：** 2026-08-16  
**研究范围：** Strict Layer，仅研究 \(A_1\)-only；以 backward line 为主，但与最新 forward common-\(U\) terminal reduction 做第一次严格合流。  
**最终裁决：**

\[
\boxed{\textbf{A1 NOT CLOSED}}
\]

但本轮得到了一组比“再加一个局部同余”更重要的结构结果：

\[
\boxed{
\textbf{Backward terminal arithmetic is radially equivariant under }a_i=UC_i,
}
\]

\[
\boxed{
\textbf{all audited backward semantic gates are consequences of the exact forward terminal state,}
}
\]

并且：

\[
\boxed{
\textbf{partial }2/5\textbf{-phase constrains the primitive state, not the radial scale }U.
}
\]

更强地，canonical backward gap pair 本身完全塌缩为 primitive sphere 的尾因子：

\[
\boxed{
Z_\pm=\frac{Q_0\pm P_3}{\gcd(Q_0,P_3)}.
}
\]

因此本轮给出的最准确架构不是“backward 再给 \(U\) 一个 residue”，而是：

\[
\boxed{
\text{primitive synchronized locus}
\longrightarrow
\text{derived primitive local/factorization language}
\longrightarrow
\text{common-}U\text{ real interval}
\longrightarrow
\text{coprime positive integer }U.
}
\]

当前唯一真正未闭合的顶层义务仍是：

\[
\boxed{
\textbf{Moving-Profile Coprime Integer-Scale Exclusion}.
}
\]

---

# 1. Executive summary

本轮最重要的结果分为九组。

## 1.1 NEW PROVED — Exact common-\(U\) pullback dictionary

设

\[
a_i=UC_i,\qquad b_i=\frac V{g_i},\qquad \gcd(U,V)=1,
\]

并将 backward prefix 统一重命名为

\[
\Pi=a_1 10^n+a_2.
\]

定义 primitive prefix carrier

\[
\boxed{H:=C_1 10^n+C_2}
\]

以及

\[
\boxed{\mathbf A^\sharp:=SH+C_3}.
\]

则精确有

\[
\boxed{\Pi=UH,\qquad \mathbf A=U\mathbf A^\sharp.}
\]

再定义

\[
N^\sharp=b_2^2C_1^2+b_1^2C_2^2,
\]

\[
\delta=b_3H-C_3D,
\]

\[
C_+^\sharp=b_3\mathbf A^\sharp+C_3\mathbf B.
\]

则

\[
\boxed{
N=U^2N^\sharp,\qquad
\Delta=U\delta,\qquad
C_+=UC_+^\sharp.
}
\]

这整套 dictionary 是 exact identity，不含近似，也不依赖局部 chamber。

---

## 1.2 NEW PROVED — Raw-WGF Radial Homogeneity

raw WGF

\[
N\mathbf B^2b_3^2
=
G^2S\Delta C_+
\]

代入上式后 \(U^2\) 精确消掉：

\[
\boxed{
N^\sharp\mathbf B^2b_3^2
=
G^2S\delta C_+^\sharp.
}
\tag{PB-WGF}
\]

因此：

\[
\boxed{
\textbf{raw WGF 本身完全不读取 common radial scale }U.
}
\]

尤其它不可能单独给出：

\[
U\bmod 2^r,\qquad U\bmod5^s,
\]

也不可能单独给出一个新的 \(M\mid U\) radial divisor。

---

## 1.3 NEW PROVED — \(E\mid\mathbf A\) 实际上是 Possibility A

最新 unified exact-lift 已证明：

\[
\boxed{\Lambda:=\operatorname{lcm}(b_1,b_2,b_3)=V.}
\]

而 forward exact master 给出

\[
\boxed{
V\mathbf A^\sharp=Q_0\mathbf B.
}
\tag{MASTER-WORD}
\]

定义

\[
\Gamma=\gcd(\mathbf B,V),\qquad E=\frac{\mathbf B}{\Gamma}.
\]

写

\[
V=\Gamma V_0,\qquad \mathbf B=\Gamma E,
\qquad \gcd(V_0,E)=1.
\]

由 (MASTER-WORD)

\[
V_0\mathbf A^\sharp=Q_0E.
\]

所以：

\[
\boxed{E\mid\mathbf A^\sharp.}
\tag{E-PRIM}
\]

因此 backward 的

\[
E\mid\mathbf A=U\mathbf A^\sharp
\]

不是由 \(U\) 补一个 divisor；它已经在 primitive word 上成立。

这明确排除了 prompt 中 Possibility B，并把 consistency audit 定格为：

\[
\boxed{\textbf{Possibility A}.}
\]

---

## 1.4 NEW PROVED — canonical quotient variables全部显式拉回 primitive sphere

令

\[
d:=\gcd(Q_0,V).
\]

定义

\[
W^\sharp:=\frac{\mathbf A^\sharp}{E}.
\]

由于

\[
\frac{W^\sharp}{\Gamma}
=
\frac{\mathbf A^\sharp}{\mathbf B}
=
\frac{Q_0}{V},
\]

约分得到：

\[
\boxed{
u^\sharp=\frac{Q_0}{d},
\qquad
v=\frac{V}{d}.
}
\]

同时

\[
\boxed{
h=\frac{\Gamma d}{V},
\qquad
W^\sharp=h\,u^\sharp,
\qquad
\Gamma=h\,v.
}
\]

actual backward quotient满足

\[
\boxed{
W=UW^\sharp,
\qquad
u=Uu^\sharp=U\frac{Q_0}{d},
\qquad
v=\frac Vd.
}
\]

由于 \(\Gamma\mid V\) 且 \(\gcd(U,V)=1\)：

\[
\gcd(U,\Gamma)=1,
\]

故

\[
\boxed{
h=\gcd(W,\Gamma)=\gcd(W^\sharp,\Gamma)
}
\]

完全不依赖 \(U\)。

---

## 1.5 NEW PROVED — Primitive oriented gap 具有 closed form

定义

\[
\varepsilon^\sharp
:=
vH-Du^\sharp.
\]

由

\[
u=Uu^\sharp,\qquad \Pi=UH
\]

立即得

\[
\boxed{
\varepsilon=U\varepsilon^\sharp.
}
\]

更重要的是，由 master word identity：

\[
S(VH-Q_0D)
=
b_3(Q_0-P_3),
\]

所以

\[
\boxed{
\varepsilon^\sharp
=
\frac{b_3(Q_0-P_3)}{S\,d}
\in\mathbf Z_{>0}.
}
\tag{EPS-PRIM}
\]

因此 backward oriented-gap integrality等价于一个纯 primitive/profile divisibility：

\[
\boxed{
Sd\mid b_3(Q_0-P_3).
}
\]

并且 primitive determinant bridge 为：

\[
\boxed{
\delta=Eh\,\varepsilon^\sharp.
}
\]

---

## 1.6 NEW PROVED — PB-WGF 完全塌缩为 primitive sphere factorization

由

\[
V\mathbf A^\sharp=Q_0\mathbf B
\]

得到

\[
\boxed{
S\delta
=
\frac{\mathbf B(Q_0-P_3)}{g_3},
}
\tag{TAIL-}
\]

以及

\[
\boxed{
C_+^\sharp
=
\frac{\mathbf B(Q_0+P_3)}{g_3}.
}
\tag{TAIL+}
\]

另一方面：

\[
\boxed{
N^\sharp
=
\frac{V^2}{g_1^2g_2^2}(P_1^2+P_2^2)
=
\frac{G^2}{V^2}(Q_0-P_3)(Q_0+P_3).
}
\tag{N-TAIL}
\]

于是 PB-WGF 逐项化为同一个恒等式：

\[
P_1^2+P_2^2
=
(Q_0-P_3)(Q_0+P_3).
\]

因此：

\[
\boxed{
\textbf{PB-WGF 是 primitive sphere + exact master 的 DERIVED consequence.}
}
\]

它在语义上不缩小 exact forward terminal candidate set。

---

## 1.7 NEW PROVED — normalized backward \(Z_\pm\) 恰为 primitive tail factors

这是本轮最强的 normalization collapse 之一。

令

\[
c_0:=\gcd(Q_0,P_3).
\]

则 backward cross-content normal form中的

\[
Z_-,Z_+
\]

精确等于：

\[
\boxed{
Z_-=\frac{Q_0-P_3}{c_0},
\qquad
Z_+=\frac{Q_0+P_3}{c_0}.
}
\tag{Z-TAIL}
\]

所以自动有

\[
\boxed{\gcd(Z_-,Z_+)\mid2.}
\]

而

\[
Z_-Z_+
=
\frac{P_1^2+P_2^2}{c_0^2}.
\]

因此旧 backward 的 source-labelled Gaussian gap theorem现在可以重新解释为：

> primitive sphere 的 normalized tail factor pair \(Q_0\pm P_3\) 在 odd \(3\bmod4\) primes 上分别具有偶 valuation。

也就是说：

\[
\boxed{
\textbf{这部分 Gaussian structure 也是 primitive sphere 的 derived factor language。}
}
\]

---

## 1.8 NEW PROVED — \(2/5\)-phase真正约束 primitive tail gap，而非 \(U\)

设 \(p\in\{2,5\}\) 且

\[
s_p:=v_p(b_3)<n_3.
\]

因为

\[
v_p(\mathbf B)=s_p,
\]

由 (TAIL-)：

\[
n_3+v_p(\delta)
=
s_p+v_p(Q_0-P_3)-v_p(g_3).
\]

故 determinant cut depth统一写成

\[
\boxed{
R_p^{\rm det}
=
\max\left(
0,\,
v_p(Q_0-P_3)-n_3-v_p(g_3)
\right).
}
\tag{R-TAIL}
\]

在既有 partial-\(5\) cut-visible chamber，这就是原来的 \(R_5\)。

在 partial-\(2\) cut-visible chamber，这就是原来的 \(R_2\)。

因此原来的 phase-to-cut congruence拉回后成为：

\[
\boxed{
H\equiv
C_3\frac D{p^{s_p}}
\left(\frac{b_3}{p^{s_p}}\right)^{-1}
\pmod{p^{R_p}}.
}
\tag{PPS-p}
\]

这里不存在 \(U\)。

---

## 1.9 FINAL ARCHITECTURE VERDICT

本轮没有找到 independent radial backward sieve。

相反，完成了：

\[
\boxed{
\textbf{A1 Backward Radial Redundancy Certificate}
}
\]

在当前审计的 terminal A1 backward architecture 中：

- raw WGF homogeneous；
- phase对 \(U\) 可消；
- \(E\mid\mathbf A^\sharp\) primitive；
- reducedness由 gcd profile+\(\gcd(U,V)=1\) 自动恢复；
- \(h,v,Z_\pm,N_0\) 等 normalized objects primitive-only；
- \(c_a,c_N\) 虽随 \(U\) 线性增长，但该 \(U\)-content在 normalization 中精确消掉；
- 没有留下独立的 \(M_{\rm req}\mid U\)；
- 唯一真正打破 radial scaling 的是 numerator digit windows / integer interval / coprimality，即 forward RAD gate。

因此：

\[
\boxed{
\textbf{backward 不再承担独立 semantic gate；}
}
\]

但：

\[
\boxed{
\textbf{backward 仍可作为 derived primitive arithmetic language 使用。}
}
\]

---

# 2. Frozen forward/backward frontier

## FROZEN

Strict Layer：

\[
\boxed{DD=\varnothing.}
\]

仅剩：

\[
\boxed{A_1\text{-only}.}
\]

forward 已冻结：

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
g_i=\gcd(V,P_i),
\]

\[
C_i=P_i/g_i,
\qquad
b_i=V/g_i,
\]

\[
a_i=UC_i,
\qquad
\gcd(U,V)=1.
\]

minimal radial gate：

\[
\boxed{
U\in I_{23}\cap\mathbf Z_{>0},
\qquad
\gcd(U,V)=1.
}
\tag{RAD}
\]

fixed \((g_2,g_3,n_2,n_3)\)+integer \(U\) 已知强迫 \(Q_0\) bounded。

因此 fixed-profile infinity 已从 frontier 删除。

真正开放：

\[
\boxed{
\textbf{Moving-Profile Coprime Integer-Scale Exclusion}.
}
\]

---

# 3. Notation collision cleanup

本轮统一使用：

\[
\boxed{\Pi:=a_1 10^n+a_2}
\]

代替 backward 历史记号 \(P\)，避免与 primitive \(P_i\) 混淆。

定义：

\[
S=10^{n_3},
\]

\[
Q=b_1 10^{m_2}+b_2,
\qquad
D=10^gQ,
\]

\[
\mathbf B=SD+b_3,
\qquad
G=b_1b_2,
\]

\[
\mathbf A=S\Pi+a_3.
\]

weighted prefix norm：

\[
N=b_2^2a_1^2+b_1^2a_2^2.
\]

same-word determinant：

\[
\Delta=b_3\Pi-a_3D.
\]

plus factor：

\[
C_+=b_3\mathbf A+a_3\mathbf B.
\]

---

# 4. Exact common-\(U\) pullback dictionary

定义：

\[
H=C_1 10^n+C_2,
\]

\[
\mathbf A^\sharp=SH+C_3.
\]

则：

\[
\Pi
=
UC_1 10^n+UC_2
=
UH.
\]

以及：

\[
\mathbf A
=
S(UH)+UC_3
=
U\mathbf A^\sharp.
\]

定义：

\[
N^\sharp=b_2^2C_1^2+b_1^2C_2^2.
\]

则：

\[
N
=
b_2^2(U C_1)^2+b_1^2(U C_2)^2
=
U^2N^\sharp.
\]

同理：

\[
\Delta
=
b_3UH-UC_3D
=
U\delta,
\]

其中：

\[
\delta=b_3H-C_3D.
\]

以及：

\[
C_+
=
b_3U\mathbf A^\sharp+UC_3\mathbf B
=
UC_+^\sharp.
\]

**状态：NEW PROVED.**

---

# 5. Radial degree table

以下表格描述 radial action

\[
(C_i;\text{denominator profile})
\mapsto
(a_i=UC_i;\text{same denominator profile}).
\]

| object | exact \(U\)-behaviour | radial status |
|---|---:|---|
| \(a_i\) | \(U C_i\) | degree 1 |
| \(\Pi\) | \(UH\) | degree 1 |
| \(\mathbf A\) | \(U\mathbf A^\sharp\) | degree 1 |
| \(N\) | \(U^2N^\sharp\) | degree 2 |
| \(\Delta\) | \(U\delta\) | degree 1 |
| \(C_+\) | \(UC_+^\sharp\) | degree 1 |
| \(G,D,\mathbf B,V,b_i\) | unchanged | degree 0 |
| \(\Lambda\) | \(V\) | degree 0 |
| \(\Gamma,E\) | denominator-only | degree 0 |
| \(W\) | \(UW^\sharp\) | degree 1 |
| \(h\) | unchanged | degree 0 |
| \(u\) | \(Uu^\sharp\) | degree 1 |
| \(v\) | unchanged | degree 0 |
| \(\varepsilon\) | \(U\varepsilon^\sharp\) | degree 1 |
| \(\eta,\mathcal L,\tau,\bar v\) | unchanged | degree 0 |
| \(c_a\) | \(Uc_a^\sharp\) | degree 1 content |
| \(c_\tau\) | unchanged | degree 0 |
| \(Z_\pm\) | unchanged | degree 0 |
| \(c_N\) | \(Uc_N^\sharp\) | degree 1 content |
| \(N_0=N/c_N^2\) | unchanged | degree 0 |
| digit legality | not homogeneous | **radial-breaking** |

核心结论：

\[
\boxed{
\textbf{normalized backward arithmetic is degree 0;}
\quad
\textbf{only digit/integer realization breaks radial symmetry.}
}
\]

---

# 6. Raw-WGF homogeneity theorem

由：

\[
N=U^2N^\sharp,
\]

\[
\Delta=U\delta,
\]

\[
C_+=UC_+^\sharp,
\]

raw WGF 变成：

\[
U^2N^\sharp\mathbf B^2b_3^2
=
G^2S(U\delta)(UC_+^\sharp).
\]

约掉 \(U^2>0\)：

\[
\boxed{
N^\sharp\mathbf B^2b_3^2
=
G^2S\delta C_+^\sharp.
}
\]

### Theorem A1-BR-CU1 — Raw-WGF Radial Homogeneity

对任意 exact common-\(U\) state，raw WGF 在去掉 common numerator content 后完全不含 \(U\)。

**状态：NEW PROVED.**

直接后果：

\[
\boxed{
\text{WGF}\not\Rightarrow U\bmod p^r
}
\]

除非额外引入一个非齐次、非 homogeneous 的外部条件。

---

# 7. Primitive determinant \(\delta\)

定义：

\[
\delta=b_3H-C_3D.
\]

它满足：

\[
\boxed{\delta>0.}
\]

证明见第 15 节的 exact tail formula：

\[
S\delta=\mathbf B(Q_0-P_3)/g_3,
\]

而所有量均为正且 \(Q_0>P_3\)。

因此 backward oriented determinant在 common-\(U\) pullback 后仍保持 orientation，但 orientation 是 primitive。

---

# 8. Primitive norm \(N^\sharp\)

\[
N^\sharp
=
b_2^2C_1^2+b_1^2C_2^2.
\]

代入

\[
b_1=\frac V{g_1},
\quad
b_2=\frac V{g_2},
\quad
C_i=\frac{P_i}{g_i},
\]

得：

\[
N^\sharp
=
\frac{V^2}{g_1^2g_2^2}
(P_1^2+P_2^2).
\]

又：

\[
P_1^2+P_2^2
=
Q_0^2-P_3^2
=
(Q_0-P_3)(Q_0+P_3).
\]

所以：

\[
\boxed{
N^\sharp
=
\frac{G^2}{V^2}
(Q_0-P_3)(Q_0+P_3).
}
\]

**状态：NEW PROVED / primitive sphere rewrite.**

---

# 9. Partial-\(5\) phase pullback

冻结 partial-\(5\)：

\[
0<s_5:=v_5(b_3)<n_3.
\]

已有：

\[
\Pi
\equiv
a_3
\frac D{5^{s_5}}
\left(
\frac{b_3}{5^{s_5}}
\right)^{-1}
\pmod{5^{R_5}}.
\]

代入：

\[
\Pi=UH,\qquad a_3=UC_3.
\]

因为：

\[
5\mid b_3\Longrightarrow5\mid V,
\]

而：

\[
\gcd(U,V)=1,
\]

故：

\[
5\nmid U.
\]

于是 \(U\in\mathbf Z_5^\times\)，可以严格消去：

\[
\boxed{
H
\equiv
C_3
\frac D{5^{s_5}}
\left(
\frac{b_3}{5^{s_5}}
\right)^{-1}
\pmod{5^{R_5}}.
}
\tag{PPS5}
\]

### Cancellation Lemma

若 \(p\nmid U\)，则：

\[
UH\equiv U C_3K\pmod{p^R}
\iff
H\equiv C_3K\pmod{p^R}.
\]

因此：

\[
\boxed{
\textbf{partial-5 phase constrains }H,\textbf{ not }U.
}
\]

---

# 10. Partial-\(2\) phase pullback

在：

\[
0<s_2:=v_2(b_3)<n_3
\]

且 cut-visible 时，已有：

\[
\Pi
\equiv
a_3
\frac D{2^{s_2}}
\left(
\frac{b_3}{2^{s_2}}
\right)^{-1}
\pmod{2^{R_2}}.
\]

因为：

\[
2\mid b_3\Longrightarrow2\mid V,
\]

\[
\gcd(U,V)=1
\Longrightarrow
U\text{ odd}.
\]

所以：

\[
\boxed{
H
\equiv
C_3
\frac D{2^{s_2}}
\left(
\frac{b_3}{2^{s_2}}
\right)^{-1}
\pmod{2^{R_2}}.
}
\tag{PPS2}
\]

同样：

\[
\boxed{
\textbf{partial-2 phase constrains primitive }H,\textbf{ not }U.
}
\]

---

# 11. Correct interpretation of the \(2\times5\) decimal suffix

若：

\[
R_2>0,\qquad R_5>0,
\]

则：

\[
H\equiv H_2\pmod{2^{R_2}},
\]

\[
H\equiv H_5\pmod{5^{R_5}}.
\]

CRT 唯一给出：

\[
\boxed{
H\equiv H_{2,5}
\pmod{2^{R_2}5^{R_5}}.
}
\]

令：

\[
J=\min(R_2,R_5).
\]

则：

\[
\boxed{
H\equiv H_{10}\pmod{10^J}.
}
\tag{PPS10}
\]

所以上一轮 “actual \(\Pi\) 的 decimal suffix” 在 common-\(U\) state 中的正确 primitive解释是：

\[
\boxed{
\textbf{primitive prefix carrier }H
\textbf{ lies in a fixed }10\textbf{-adic cylinder}.
}
\]

不是：

\[
U\bmod10^J.
\]

---

# 12. Normalized-content \(U\)-dependence audit

本节逐项检查此前最容易误判的 gcd/content objects。

## 12.1 \(E\)

\[
E=\mathbf B/\gcd(\mathbf B,V)
\]

完全 denominator-only。

并且已经证明：

\[
E\mid\mathbf A^\sharp.
\]

所以 \(E\) 对 \(U\) 无读取能力。

## 12.2 \(W\)

\[
W=\mathbf A/E
=
U\mathbf A^\sharp/E
=
UW^\sharp.
\]

degree 1，但只是整体 radial scaling。

## 12.3 \(h\)

\[
h=\gcd(W,\Gamma)
=
\gcd(UW^\sharp,\Gamma).
\]

因为：

\[
\gcd(U,\Gamma)=1,
\]

所以：

\[
\boxed{h=\gcd(W^\sharp,\Gamma).}
\]

degree 0。

## 12.4 \(c_a\)

\[
c_a=\gcd(a_3,u)
=
\gcd(UC_3,Uu^\sharp)
=
U\gcd(C_3,u^\sharp).
\]

定义：

\[
c_a^\sharp:=\gcd(C_3,u^\sharp).
\]

则：

\[
\boxed{c_a=Uc_a^\sharp.}
\]

它确实“读取” \(U\)，但只把整个 \(U\) 当作 common scalar content。

除去 \(c_a\) 后的 normalized coordinates完全 primitive。

## 12.5 \(c_N\)

\[
c_N
=
\gcd(a_1b_2,a_2b_1)
\]

变为：

\[
c_N
=
U\gcd(C_1b_2,C_2b_1).
\]

定义：

\[
c_N^\sharp
=
\gcd(C_1b_2,C_2b_1),
\]

则：

\[
\boxed{c_N=Uc_N^\sharp.}
\]

所以：

\[
N_0=N/c_N^2
=
N^\sharp/(c_N^\sharp)^2.
\]

完全 primitive。

---

# 13. Audit of \(E\mid\mathbf A\)

这是本轮的 consistency audit 核心。

由 exact primitive master：

\[
V\mathbf A^\sharp=Q_0\mathbf B.
\]

又：

\[
\Gamma=\gcd(\mathbf B,V),
\qquad
E=\mathbf B/\Gamma,
\qquad
V=\Gamma V_0.
\]

则：

\[
V_0\mathbf A^\sharp=Q_0E.
\]

因为：

\[
\gcd(V_0,E)=1,
\]

得到：

\[
\boxed{E\mid\mathbf A^\sharp.}
\]

所以：

\[
E\mid U\mathbf A^\sharp
\]

对任意 \(U\) 都自动成立。

### Verdict

prompt 中三个 possibilities：

- A: \(E\mid\mathbf A^\sharp\)；
- B: \(U\) 需要补 prime；
- C: 只是在 master 后自动出现但未必 primitive divisibility；

正确的是：

\[
\boxed{\textbf{A，且可直接从 master 证明。}}
\]

---

# 14. Reducedness pullback

令任意素数 \(p\)，设：

\[
e=v_p(V),
\qquad
f=v_p(P_i).
\]

则：

\[
v_p(g_i)=\min(e,f).
\]

若：

\[
p\mid C_i=P_i/g_i,
\]

则：

\[
f>\min(e,f),
\]

这只能发生在：

\[
e\le f.
\]

于是：

\[
v_p(g_i)=e,
\]

从而：

\[
p\nmid V/g_i=b_i.
\]

因此：

\[
\boxed{
\gcd(C_i,b_i)=1.
}
\]

又因为：

\[
b_i\mid V,
\qquad
\gcd(U,V)=1,
\]

所以：

\[
\boxed{
\gcd(UC_i,b_i)=1.
}
\]

### Verdict

\[
\boxed{
\textbf{individual reducedness is already absorbed by exact gcd profile + }\gcd(U,V)=1.
}
\]

它不再提供新的 radial sieve。

---

# 15. Forward reconstruction dependency audit

最新 forward terminal theorem给出：

\[
\boxed{
\text{primitive sphere}
+
\text{exact GSYNC/master}
+
\text{exact gcd profile}
+
\text{legal denominator blocks}
+
\text{coprime integer }U
+
\text{numerator digit legality}
}
\]

双向恢复 original candidate。

本轮直接重推其最关键 word equality：

\[
V\mathbf A^\sharp=Q_0\mathbf B.
\]

于是：

\[
\frac{\mathbf A}{\mathbf B}
=
\frac{U\mathbf A^\sharp}{\mathbf B}
=
\frac{UQ_0}{V}.
\]

而每个 reduced block：

\[
\frac{a_i}{b_i}
=
\frac{UC_i}{V/g_i}
=
\frac{UP_i}{V}.
\]

sphere：

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

立即给：

\[
\sum_i\left(\frac{a_i}{b_i}\right)^2
=
\left(\frac{UQ_0}{V}\right)^2
=
\left(\frac{\mathbf A}{\mathbf B}\right)^2.
\]

所以 norm equality已经恢复，不存在 common-\(U\) 后的“independent norm gate”。

---

# 16. Backward-on-Forward redundancy theorem

### Theorem A1-BR-CU2 — Backward-on-Forward Redundancy

固定一个 exact A1 terminal forward state：

1. primitive sphere；
2. exact A1 exponent relations；
3. exact GSYNC/master；
4. \(g_i=\gcd(V,P_i)\)；
5. \(b_i=V/g_i\) 合法；
6. \(U\in\mathbf Z_{>0}\)；
7. \(\gcd(U,V)=1\)；
8. \(a_i=UC_i\) 满足 numerator digit windows。

则：

- original equation成立；
- actual word/cut成立；
- individual reducedness成立；
- \(\Lambda=V\)；
- \(E\mid\mathbf A^\sharp\mid\mathbf A\)；
- canonical quotient \(W,h,u,v\) 全部存在；
- \(\varepsilon>0\)；
- raw WGF成立；
- PB-WGF成立；
- partial-\(2/5\) phase若其 chamber hypotheses成立，则对应 phase congruence自动成立；
- Gaussian/cross-content factorization全部是 derived views。

因此：

\[
\boxed{
\textbf{backward A1 gates do not add semantic candidates constraints after the terminal forward state.}
}
\]

**状态：NEW PROVED by existing forward equivalence + direct pullback algebra.**

---

# 17. Semantic vs proof-theoretic independence

必须严格区分：

## Semantic independence

答案：

\[
\boxed{\textbf{NO}.}
\]

backward relations不再增加 terminal candidate definition。

## Proof-theoretic usefulness

答案：

\[
\boxed{\textbf{YES}.}
\]

例如：

- \(v_p(Q_0-P_3)\) 的 tail-gap phase；
- \(Z_\pm\) factorization；
- determinant/cut congruence；
- \(2\)-adic parity tax；
- local Hensel incompatibility；

仍可作为从 forward master 派生出的 elimination language。

因此本轮没有宣布“backward theorem 都没用”，只宣布：

\[
\boxed{
\textbf{它们的正确身份是 derived primitive invariants，而非 independent radial gates.}
}
\]

---

# 18. Primitive Backward Normal Form

定义：

\[
d=\gcd(Q_0,V),
\]

\[
q:=Q_0/d,
\qquad
v:=V/d.
\]

则：

\[
u^\sharp=q.
\]

primitive word slope：

\[
\frac{\mathbf A^\sharp}{\mathbf B}
=
\frac{Q_0}{V}
=
\frac qv.
\]

primitive backward normal form可写成：

\[
\boxed{
H=C_1 10^n+C_2,
}
\]

\[
\boxed{
\mathbf A^\sharp=SH+C_3,
}
\]

\[
\boxed{
V\mathbf A^\sharp=Q_0\mathbf B,
}
\]

\[
\boxed{
\varepsilon^\sharp
=
vH-Dq
=
\frac{b_3(Q_0-P_3)}{Sd}>0,
}
\]

\[
\boxed{
\delta=Eh\varepsilon^\sharp
=
\frac{\mathbf B(Q_0-P_3)}{Sg_3},
}
\]

\[
\boxed{
C_+^\sharp
=
\frac{\mathbf B(Q_0+P_3)}{g_3},
}
\]

\[
\boxed{
N^\sharp
=
\frac{G^2}{V^2}(Q_0-P_3)(Q_0+P_3).
}
\]

这一组式子完全不出现 \(U\)。

---

# 19. Primitive \(5\)-Phase Sieve

在 partial-\(5\)：

\[
0<s_5<n_3.
\]

因为 \(5\nmid U\)：

\[
v_5(N)=v_5(N^\sharp).
\]

所以旧公式：

\[
R_5
=
v_5(N)+2s_5-2v_5(G)-n_3
\]

变成：

\[
\boxed{
R_5
=
v_5(N^\sharp)+2s_5-2v_5(G)-n_3.
}
\tag{PR5}
\]

而更进一步，由 (TAIL-)：

\[
\boxed{
R_5
=
v_5(Q_0-P_3)-n_3-v_5(g_3)
}
\tag{PR5-TAIL}
\]

在 \(R_5>0\) chamber 中精确成立。

于是：

\[
\boxed{
H\equiv H_5\pmod{5^{R_5}}.
}
\]

### Verdict

整个 partial-\(5\) phase system 是 primitive/profile-determined。

---

# 20. Primitive \(2\)-Phase Sieve

在 partial-\(2\)：

\[
0<s_2<n_3.
\]

因为 \(U\) odd：

\[
v_2(N)=v_2(N^\sharp).
\]

cut-visible时：

\[
\boxed{
R_2
=
v_2(N^\sharp)+2s_2-2v_2(G)-n_3-1.
}
\tag{PR2}
\]

另一方面由 determinant tail factor：

\[
\boxed{
R_2
=
v_2(Q_0-P_3)-n_3-v_2(g_3).
}
\tag{PR2-TAIL}
\]

这解释了之前的 \(-1\) parity tax：

由

\[
C_+^\sharp
=
\mathbf B(Q_0+P_3)/g_3
\]

和既有：

\[
v_2(C_+^\sharp)=s_2+1
\]

得到：

\[
\boxed{
v_2(Q_0+P_3)=v_2(g_3)+1.
}
\]

该额外 \(+1\) 正好在 norm factorization中产生旧公式的 \(-1\)。

---

# 21. Primitive \(10\)-adic sieve

若：

\[
R_2,R_5>0,
\]

定义：

\[
M_{2,5}:=2^{R_2}5^{R_5}.
\]

则：

\[
\boxed{
H\equiv H_{2,5}\pmod{M_{2,5}}.
}
\]

以及：

\[
\boxed{
H\equiv H_{10}\pmod{10^J},
\qquad
J=\min(R_2,R_5).
}
\]

但这是：

\[
\boxed{
\textbf{derived primitive cylinder},
}
\]

不是：

\[
\boxed{
\textbf{new independent gate on }U.
}
\]

---

# 22. Reinterpretation of UHL \(2\)-kill

上一轮 UHL theorem构造的是一个 genuine \(\mathbf Z_5\) raw-WGF local branch，并证明它没有 compatible \(\mathbf Z_2\) companion。

本轮需要校准其 scope：

- UHL 本身不是一个已经嵌入 exact forward terminal state 的 common-\(U\) candidate；
- 因此不能直接给它分配一个完整 \(P_i,Q_0,V,U\) terminal profile；
- 但是如果某 local branch能够嵌入 terminal common-\(U\) state，则 \(U\) 在 relevant \(2/5\)-side 上为 unit，故 local incompatibility必然发生在 primitive/profile layer，而不是 radial scale。

所以更准确的 interpretation 是：

\[
\boxed{
\textbf{UHL-2KILL 是 primitive-local incompatibility 的证据/模板，而不是 radial }U\textbf{-kill.}
}
\]

---

# 23. Primitive conic × local sieve

forward fixed profile：

\[
\text{sphere}\cap\text{GSYNC/master plane}
\]

通常是 projective conic。

backward pullback给：

\[
H\equiv H_p\pmod{p^{R_p}}.
\]

但本轮证明：

\[
\text{PB-WGF/PPS}_p
\]

都是 sphere+master 的 arithmetic consequences。

因此若“exact forward conic”已经包含完整 master，则集合论上：

\[
\boxed{
\mathcal C_{\rm sync}
\cap
\mathcal S_{2,5}^{\rm primitive}
=
\mathcal C_{\rm sync}
}
\]

在“sieve”只包含这些 derived necessary conditions的意义下成立。

它们的价值是：

- 以 valuation/cylinder 语言重写 exact conic points；
- 在 partial search / contradiction proof 中提前切 branch；
- 不是再添加一个新 semantic condition。

---

# 24. Is the sieve already implied by GSYNC?

### Answer

\[
\boxed{\textbf{YES, once primitive sphere is included.}}
\]

证明链：

\[
\text{GSYNC/master}
\Longrightarrow
V\mathbf A^\sharp=Q_0\mathbf B.
\]

与 sphere：

\[
P_1^2+P_2^2+P_3^2=Q_0^2
\]

合起来给：

\[
N^\sharp
=
\frac{G^2}{V^2}(Q_0-P_3)(Q_0+P_3),
\]

\[
S\delta
=
\frac{\mathbf B(Q_0-P_3)}{g_3},
\]

\[
C_+^\sharp
=
\frac{\mathbf B(Q_0+P_3)}{g_3}.
\]

于是 PB-WGF自动成立。

phase congruence只是对 \(\delta\) 的 \(p\)-adic valuation读取。

因此 dependency graph为：

\[
\boxed{
\text{sphere}+\text{master}
\to
\text{tail factorization}
\to
\text{PB-WGF}
\to
\text{phase-to-cut}.
}
\]

---

# 25. Primitive phase × real digit cone

minimal continuous common-scale condition：

\[
10^{n_2-n_3-1}
<
\frac{C_2}{C_3}
<
10^{n_2-n_3+1}.
\]

phase：

\[
H=C_1 10^n+C_2
\equiv H_p\pmod{p^{R_p}}.
\]

当：

\[
R_p\le n,
\]

有：

\[
C_2\equiv H_p\pmod{p^{R_p}}.
\]

当：

\[
R_p>n,
\]

开始读取 \(C_1\)。

本轮没有得到一个 universal theorem：

\[
\text{local cylinder}
+
\text{real ratio strip}
\Longrightarrow\varnothing.
\]

原因有两层：

1. phase是 exact conic的 derived local shadow；
2. genus-zero conic在有 rational point 时有限多个 local open conditions与 real arc 通常不能仅靠 topology 杀掉全部 rational points。

因此：

\[
\boxed{
\textbf{pure local-real slicing is not yet a closure mechanism.}
}
\]

---

# 26. Common-\(U\) radial interval

真正 terminal radial interval仍是：

\[
I_{23}=[L,R),
\]

其中：

\[
L
=
\max\left(
\frac{10^{n_2-1}}{C_2},
\frac{10^{n_3-1}}{C_3}
\right),
\]

\[
R
=
\min\left(
\frac{10^{n_2}}{C_2},
\frac{10^{n_3}}{C_3}
\right).
\]

最终 gate：

\[
\boxed{
N_V(L,R)>0.
}
\]

精确计数：

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
\]

本轮没有用 heuristic density替代它。

---

# 27. Search for a genuine radial backward sieve

本轮系统检查：

1. raw WGF；
2. \(E\mid\mathbf A\)；
3. quotient integrality；
4. \(h\)；
5. \(\varepsilon\)；
6. \(c_a\)；
7. \(c_N\)；
8. \(Z_\pm\)；
9. partial \(2/5\) phase；
10. global word gcd；
11. reducedness；
12. exact cut algebra。

结果：

\[
\boxed{
\textbf{No independent radial backward sieve found.}
}
\]

更强的是，在上述 audited terminal architecture中，已经证明它们全部 radial-equivariant或 primitive-derived。

唯一非齐次输入是：

- actual digit lengths；
- endpoint half-openness；
- positive integer \(U\)；
- \(\gcd(U,V)=1\)。

这些正是 forward RAD。

---

# 28. Content-divisibility route

prompt 建议对：

\[
M\mid U\mathbf A^\sharp
\]

定义：

\[
M_{\rm req}
=
\frac M{\gcd(M,\mathbf A^\sharp)}.
\]

最重要候选 \(M=E\)。

但本轮证明：

\[
E\mid\mathbf A^\sharp.
\]

所以：

\[
\boxed{
E_{\rm req}=1.
}
\]

对 \(c_a,c_N\)：

它们不是外部 fixed modulus，而是随 \(U\) 线性增长的 common contents：

\[
c_a=Uc_a^\sharp,
\qquad
c_N=Uc_N^\sharp.
\]

normalized equations除去它们后完全不含 \(U\)。

因此没有提取到：

\[
\boxed{M_{\rm req}>1\text{ fixed and }M_{\rm req}\mid U.}
\]

---

# 29. Exact coprime interval count

本轮保留 forward exact formula，不使用：

\[
(R-L)\varphi(V)/V
\]

作 proof。

尤其当 interval很短时，必须精确检查：

\[
\left\lceil\frac Rd\right\rceil
-
\left\lceil\frac Ld\right\rceil.
\]

当前 backward primitive phase尚未给出一个统一的 interval endpoint residue covering theorem。

---

# 30. \(U=1\) escape

因为：

\[
\gcd(1,V)=1
\]

永远成立，任何只依赖“\(V\) prime support越来越大”的 coprime-density路线都必须先处理：

\[
\boxed{U=1.}
\]

本轮 backward radial redundancy意味着：

\[
U=1
\]

不会被 WGF/phase/content 单独识别。

所以：

\[
\boxed{
\textbf{pure denominator-prime-density closure cannot be terminal unless it separately excludes }U=1.
}
\]

\(U=1\) 是否在所有 sufficiently large moving profiles中被 forward height/digit constraints排除：

\[
\boxed{\textbf{OPEN}.}
\]

---

# 31. bounded-\(U\) regime

假设 infinite moving sequence中：

\[
U
\]

bounded。

抽 subsequence可取：

\[
U=U_0.
\]

则：

\[
10^{n_i-1}
\le
U_0 C_i
<
10^{n_i}.
\]

所以：

\[
C_i
\asymp
10^{n_i}/U_0.
\]

但由于 \(n_i,g_i\) 本身允许 moving，本轮没有从现有 backward primitive phase推出 absolute bounded profile。

因此：

\[
\boxed{
\textbf{fixed }U\textbf{ does not currently imply fixed profile or bounded }Q_0.
}
\]

这一 regime仍 OPEN。

---

# 32. unbounded-\(U\) regime

若：

\[
U\to\infty,
\]

forward weighted shell控制的是：

\[
UQ_0
\]

与 decimal/gcd scale的同步。

本轮未证明：

\[
R-L=O(1/U)
\]

uniformly over moving profiles；最新 forward报告已经指出 moving digit exponents可随 height同步移动，因此 common-scale geometry alone不推出 eventual unique-\(U\)。

backward primitive phase也没有直接作用于 \(U\)。

所以：

\[
\boxed{
U\to\infty
}
\]

仍需要真正的 profile-height / endpoint argument。

---

# 33. Type-II \(R_2>0\) radial splice

Type-II 中：

\[
R_2>0,
\]

若同时：

\[
R_5>0,
\]

则 primitive prefix满足：

\[
H\equiv H_{2,5}\pmod{2^{R_2}5^{R_5}}.
\]

若：

\[
J=\min(R_2,R_5)\le n,
\]

只读：

\[
C_2\bmod10^J.
\]

若：

\[
J>n,
\]

开始读取 \(C_1\)。

这一信息可以和 \(C_2\) 的 Archimedean box相交，但本轮没有证明 uniform：

\[
10^J>\text{primitive interval width}.
\]

所以 Type-II 尚未关闭。

---

# 34. Type-III \(R_2=0\) radial splice

对 unsaturated \(2\)-side：

\[
s_2=v_2(b_3)<n_3,
\]

由 (R-TAIL)：

\[
R_2^{\rm det}=0
\]

等价于：

\[
\boxed{
v_2(Q_0-P_3)
\le
n_3+v_2(g_3).
}
\tag{TYPEIII}
\]

在 \(s_2=0\) 时，由 determinant integrality通常进一步落到 boundary equality。

这表明 Type-III 并不天然压成一个有限 parity list；它首先是一个 primitive tail-gap valuation chamber。

加入 common-\(U\) interval后是否统一有：

\[
N_V(I_{23})=0
\]

本轮没有证明。

因此 Q11 的严格答案是：

\[
\boxed{\textbf{OPEN}.}
\]

但已经校准为：

\[
\boxed{
\textbf{Type-III 是 primitive tail-gap escape，不是 radial }U\textbf{ phase escape。}
}
\]

---

# 35. Primitive determinant magnitude

精确：

\[
\boxed{
\delta
=
\frac{\mathbf B(Q_0-P_3)}{10^{n_3}g_3}.
}
\]

以及：

\[
0<Q_0-P_3<Q_0.
\]

因此：

\[
0<\delta
<
\frac{\mathbf BQ_0}{10^{n_3}g_3}.
\]

但这个 bound含完整 denominator word \(\mathbf B\)，在 moving profiles中可以很大。

所以单靠：

\[
p^{R_p}\mid\delta
\]

没有得到 modulus > magnitude。

---

# 36. Divisibility-vs-magnitude overload

假设 \(2,5\) 两侧均 cut-visible，并设：

\[
M:=2^{R_2}5^{R_5}.
\]

由：

\[
R_p=v_p(Q_0-P_3)-n_3-v_p(g_3),
\]

定义：

\[
\operatorname{dec}(x)
:=
2^{v_2(x)}5^{v_5(x)},
\]

则：

\[
\boxed{
M
=
\frac{\operatorname{dec}(Q_0-P_3)}
{10^{n_3}\operatorname{dec}(g_3)}.
}
\]

而：

\[
\delta
=
\frac{\mathbf B(Q_0-P_3)}
{10^{n_3}g_3}.
\]

因此：

\[
\boxed{
\frac{\delta}{M}
=
\mathbf B
\frac{\operatorname{core}_{10}(Q_0-P_3)}
{\operatorname{core}_{10}(g_3)}.
}
\tag{OVERLOAD-Q}
\]

右侧虽由 integrality保证最终为整数，但其大小没有 current absolute bound。

尤其包含：

\[
\mathbf B
\]

以及 moving ten-free core。

因此：

\[
\boxed{
\textbf{no uniform }\delta<M
\textbf{ or }\delta<KM\textbf{ with absolute }K
}
\]

可由现有 phase depths推出。

**状态：FAILED AS A UNIFORM OVERLOAD ROUTE.**

---

# 37. Asymmetric \(2^{R_2}5^{R_5}\) modulus

本轮明确保留 asymmetric modulus，而不只看：

\[
10^J.
\]

这确实比 \(10^J\) 强。

但 (OVERLOAD-Q) 表明：

\[
2^{R_2}5^{R_5}
\]

的额外 strength恰好只能移除 \(Q_0-P_3\) 的 decimal-prime excess；剩余 quotient仍有：

- \(\mathbf B\)；
- ten-free tail core；
- ten-free \(g_3\) normalization。

所以 asymmetric modulus本身仍不足以形成 constant quotient。

---

# 38. Constant-quotient reduction

prompt 希望：

\[
\delta=Mq,
\qquad
1\le q<K
\]

with absolute \(K\)。

本轮得到 exact quotient：

\[
q
=
\mathbf B
\frac{\operatorname{core}_{10}(Q_0-P_3)}
{\operatorname{core}_{10}(g_3)}.
\]

这不是 absolute finite alphabet。

因此：

\[
\boxed{
\textbf{Constant-Quotient Closure FAILED with current inputs.}
}
\]

若未来能证明该 ten-free quotient bounded，才值得恢复此路线。

---

# 39. Decimal endpoint linear forms

定义：

\[
\Omega_{ij}
=
10^{n_j}C_i
-
10^{n_i-1}C_j.
\]

这些量确实控制 common-\(U\) interval endpoint ordering / width。

backward phase控制：

\[
H=C_1 10^n+C_2.
\]

本轮尝试寻找：

\[
M\mid\Omega_{ij}
\]

由 PPS2/PPS5推出。

没有得到 uniform implication。

原因是 PPS直接作用于：

\[
b_3H-C_3D=\delta,
\]

而 endpoint determinant使用的十进制 coefficients和 denominator profile不匹配。

因此：

\[
\boxed{
\textbf{no Decimal Linear-Form Overload theorem proved this round.}
}
\]

---

# 40. Affine lattice viewpoint

若固定 \(U\)，digit windows给：

\[
(C_1,C_2)
\]

一个 rectangle，phase给：

\[
C_1 10^n+C_2\equiv h_0\pmod M.
\]

这确实是一条 affine lattice穿过 Archimedean rectangle。

但是 \(U\) 本身是未知 radial witness；若先固定 primitive conic point，则 \(C_i\) 已确定，不再需要 lattice counting。

因此两种视角分别适合：

- proof search：fix \(U\), count primitive boxes；
- semantic terminal：fix primitive state, count \(U\in I_{23}\)。

本轮没有得到 determinant > box-size 的 uniform theorem。

---

# 41. Moving-profile finite-type reduction

当前可安全冻结的 finite labels包括：

- forward sign branch；
- whether \(s_2<n_3\), \(s_2\ge n_3\)；
- whether \(s_5<n_3\), \(s_5\ge n_3\)；
- whether \(R_2=0\)；
- whether \(R_5=0\)；
- ordering of \(C_2,C_3\)；
- bounded/unbounded \(U\)。

但：

\[
g_2,g_3,V,n_2,n_3
\]

的 magnitudes仍可 moving。

因此本轮没有证明 finite absolute type theorem。

---

# 42. Plus branch attack

plus branch已有 frozen：

\[
P_3(1+10^{n_2-1})<Q_0,
\]

以及：

\[
10^g<\sqrt{10Q_0}.
\]

本轮新增 backward primitive formula：

\[
\varepsilon^\sharp
=
\frac{b_3(Q_0-P_3)}{10^{n_3}d}.
\]

plus branch若未来能把：

\[
Q_0-P_3
\]

压得足够小，则 \(\varepsilon^\sharp\in\mathbf Z_{>0}\) 是一个很自然的 divisibility-vs-magnitude入口。

但本轮未从 plus inequalities推出：

\[
0<\varepsilon^\sharp<1.
\]

所以 plus仍：

\[
\boxed{\textbf{OPEN}.}
\]

---

# 43. Minus branch attack

general minus branch仍：

\[
\boxed{\textbf{OPEN}.}
\]

本轮不重做第三/第四轮 fixed-profile conic family。

新的接口说明：

- fixed profile infinity已被 integer \(U\) 杀；
- general moving minus profile必须同时维持：
  \[
  \varepsilon^\sharp\in\mathbf Z_{>0},
  \]
  \[
  N_V(I_{23})>0.
  \]

这比继续追 primitive private-prime 更接近终局。

---

# 44. Homogeneity regression experiment

取之前 exact synchronized primitive state：

\[
(P_1,P_2,P_3,Q_0)=(24,52,159,169),
\]

\[
V=24,
\qquad
(g_1,g_2,g_3)=(24,4,3),
\]

故：

\[
(C_1,C_2,C_3)=(1,13,53),
\]

\[
(b_1,b_2,b_3)=(1,6,8).
\]

取：

\[
n=2,\qquad n_3=1,\qquad S=10,
\]

\[
Q=D=16,\qquad \mathbf B=168.
\]

primitive quantities：

\[
H=113,
\]

\[
\mathbf A^\sharp=1183,
\]

\[
N^\sharp=205,
\]

\[
\delta=56,
\]

\[
C_+^\sharp=18368.
\]

验证：

\[
V\mathbf A^\sharp
=
24\cdot1183
=
28392
=
169\cdot168
=
Q_0\mathbf B.
\]

并且：

\[
N^\sharp\mathbf B^2b_3^2
=
370298880
=
G^2S\delta C_+^\sharp.
\]

canonical quotient：

\[
\Gamma=24,\quad E=7,
\]

\[
W^\sharp=169,\quad h=1,
\]

\[
u^\sharp=169,\quad v=24,
\]

\[
\varepsilon^\sharp=8.
\]

cross-content：

\[
Z_-=10,
\qquad
Z_+=328.
\]

对 formal radial scales \(U=1,5,7,11\)（这些并不都满足当前 fixed digit windows，因此只做 homogeneity regression），得到：

| \(U\) | \(W\) | \(u\) | \(\varepsilon\) | \(c_a\) | \(c_N\) | \(Z_-\) | \(Z_+\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 169 | 169 | 8 | 1 | 1 | 10 | 328 |
| 5 | 845 | 845 | 40 | 5 | 5 | 10 | 328 |
| 7 | 1183 | 1183 | 56 | 7 | 7 | 10 | 328 |
| 11 | 1859 | 1859 | 88 | 11 | 11 | 10 | 328 |

这与 degree table完全一致。

**状态：COMPUTATIONAL REGRESSION / theorem本身不依赖计算。**

---

# 45. Primitive sieve experiments

本轮没有新做大规模枚举。

原因是接口 theorem 已经代数上证明：

\[
\text{phase sieve}
\]

是 exact forward state 的 derived consequence。

因此若枚举“sphere+master exact hits”后再统计 PPS2/PPS5死亡率，任何死亡都应被解释为：

- implementation bug；
- chamber hypothesis不满足却误用公式；
- 或 state其实并非 exact master hit。

下一轮若做实验，正确用途应是：

\[
\boxed{
\text{定位 tail-gap valuation types 与 }N_V(I_{23})\text{ 的经验相关性},
}
\]

而不是把 derived sieve当独立筛层计算“死亡率”。

---

# 46. Moving escape experiments

建议记录真正有意义的 moving observables：

\[
Q_0,\quad
V,\quad
g_2,g_3,\quad
n_2,n_3,\quad
U,
\]

\[
q_-:=Q_0-P_3,
\]

\[
d=\gcd(Q_0,V),
\]

\[
\varepsilon^\sharp
=
\frac{b_3q_-}{10^{n_3}d},
\]

\[
R_2^{\rm det},
\quad
R_5^{\rm det},
\]

\[
L,R,\quad
N_V(L,R).
\]

相比旧变量：

\[
E,h,W,Z_\pm
\]

这些新 observables更接近 terminal moving-profile problem。

---

# 47. Pseudo-families / counterexamples

当前已知的 primitive-only infinite pseudo-family仍证明：

\[
\text{sphere+GSYNC+gcd profile}
\]

不足。

本轮没有构造满足完整 terminal forward state的 infinite family；如果构造成功，就会是真正 original A1 candidate family，必须立即重建原题核验。

本轮得到的 formal scaling regression只用于证明 radial homogeneity，不是 original candidate family，因为 fixed digit windows可能失败。

---

# 48. Exact interface theorem

### Theorem A1-FBI — Full Backward/Forward Interface

对一个 exact A1 state，下列两种描述等价：

## Forward terminal description

\[
\mathcal P=
(P_1,P_2,P_3,Q_0;V;g_i;\text{A1 exponent profile})
\]

满足：

- primitive sphere；
- exact GSYNC/master；
- exact gcd profile；
- legal denominator blocks；

再存在：

\[
U\in I_{23}\cap\mathbf Z_{>0},
\qquad
\gcd(U,V)=1.
\]

## Original / backward description

由：

\[
a_i=UC_i,\qquad b_i=V/g_i
\]

恢复 original candidate，并进一步唯一确定：

\[
\Pi,\mathbf A,\mathbf B,N,\Delta,C_+,
E,\Gamma,W,h,u,v,\varepsilon,
\eta,\mathcal L,\tau,\bar v,
c_a,c_\tau,Z_\pm,c_N,N_0.
\]

其中所有 backward objects都是 deterministic derived views。

**状态：EQUIVALENT / NEW EXPLICIT INTERFACE, semantic core inherited from forward A1-CU-13.**

---

# 49. Strongest new closure theorem

本轮没有得到：

\[
A_1=\varnothing.
\]

最强的“closure-like”结果是对错误搜索空间的关闭：

### A1 Backward Radial Redundancy Certificate

在 exact terminal common-\(U\) coordinates中：

\[
\boxed{
\text{raw WGF / phase / normalized content / reducedness}
}
\]

不提供 independent radial condition beyond：

\[
\boxed{
U\in\mathbf Z_{>0},
\quad
\gcd(U,V)=1,
\quad
U\in I_{23}.
}
\]

特别禁止以后继续期待：

\[
\text{phase}\to U\text{-residue},
\]

\[
\text{WGF}\to U\text{-divisor},
\]

\[
E\mid\mathbf A\to M_{\rm req}\mid U.
\]

**状态：NEW PROVED ANTI-WASTE THEOREM.**

---

# 50. Does backward retain independent value?

必须分两种意义。

## Semantic value

\[
\boxed{\textbf{NO independent value}.}
\]

terminal candidate定义不需要再加 backward gate。

## Proof-theoretic value

\[
\boxed{\textbf{YES, but derived}.}
\]

当前最值得保留的 backward outputs 已经压成：

\[
\boxed{
\varepsilon^\sharp
=
\frac{b_3(Q_0-P_3)}{10^{n_3}\gcd(Q_0,V)}
\in\mathbf Z_{>0},
}
\]

\[
\boxed{
R_p^{\rm det}
=
\max(0,v_p(Q_0-P_3)-n_3-v_p(g_3)),
}
\]

\[
\boxed{
Z_\pm
=
\frac{Q_0\pm P_3}{\gcd(Q_0,P_3)}.
}
\]

这些比继续保留 \(W,h,c_a,c_\tau\) 大量中间变量更适合下一轮。

---

# 51. Exact remaining A1 obligation

本轮之后，A1 的 minimal exact obligation是：

> 不存在一列 moving exact synchronized primitive states
>
> \[
> \mathcal P_j
> \]
>
> 使
>
> \[
> Q_{0,j}\to\infty
> \]
>
> 且每个 state 都满足
>
> \[
> \boxed{
> N_{V_j}(I_{23,j})>0.
> }
> \]

等价地：

\[
\boxed{
\textbf{A1 Moving-Profile Primitive × Coprime-Radial Exclusion}.
}
\]

backward可提供 derived tail-gap arithmetic，但不再增加 semantic predicate。

---

# 52. PROVED / REDUNDANT / FAILED / OPEN ledger

## FROZEN

1. \(DD=\varnothing\)；
2. Strict frontier = A1-only；
3. primitive sphere；
4. exact GSYNC/master；
5. common-\(V\) gcd profile；
6. common-\(U\) interval；
7. exact coprime count；
8. fixed-profile radial termination；
9. backward raw WGF；
10. partial \(5\)-phase theorem；
11. partial \(2\)-phase theorem；
12. pure \(5\)-adic Hensel survival；
13. UHL \(2\)-kill。

## NEW PROVED

1. complete common-\(U\) pullback dictionary；
2. raw-WGF radial homogeneity；
3. \(E\mid\mathbf A^\sharp\)；
4. explicit \(W^\sharp,h,u^\sharp,v\) formulas；
5. explicit primitive \(\varepsilon^\sharp\)；
6. primitive determinant bridge；
7. \(S\delta=\mathbf B(Q_0-P_3)/g_3\)；
8. \(C_+^\sharp=\mathbf B(Q_0+P_3)/g_3\)；
9. \(N^\sharp=(G^2/V^2)(Q_0-P_3)(Q_0+P_3)\)；
10. PB-WGF derived directly from sphere+master；
11. \(c_a=Uc_a^\sharp\)；
12. \(c_N=Uc_N^\sharp\)；
13. normalized \(Z_\pm\) radial independence；
14. exact
    \[
    Z_\pm=(Q_0\pm P_3)/\gcd(Q_0,P_3);
    \]
15. partial-\(5\) phase cancels \(U\)；
16. partial-\(2\) phase cancels \(U\)；
17. primitive \(10\)-adic suffix interpretation；
18. tail-gap phase depth formula；
19. Type-III tail-gap characterization in unsaturated \(2\)-side；
20. Backward-on-Forward Redundancy Theorem；
21. Full Backward/Forward Interface theorem；
22. Backward Radial Redundancy Certificate。

## DERIVED / REDUNDANT SEMANTICALLY

1. PB-WGF；
2. \(2/5\)-phase on exact terminal states；
3. normalized Gaussian gap pair；
4. reducedness after gcd profile+\(\gcd(U,V)=1\)；
5. \(E\mid\mathbf A\) after primitive master；
6. same-cut norm after sphere+master。

## COMPUTATIONAL EVIDENCE

1. homogeneity regression on the \((24,52,159,169)\), \(V=24\) synchronized state；
2. no global claim depends on this regression。

## DISPROVED / FAILED AS ROUTES

1. phase gives \(U\)-residue；
2. raw WGF gives independent \(U\)-divisibility；
3. \(E\mid\mathbf A\) forces a nontrivial divisor of \(U\)；
4. individual reducedness adds radial sieve；
5. \(2\times5\) automatically yields constant determinant quotient；
6. primitive determinant modulus currently exceeds magnitude uniformly；
7. local real+adic topology alone closes moving conic；
8. pure denominator-prime density can ignore \(U=1\)。

## OPEN

1. plus moving-profile radial exclusion；
2. general minus moving-profile radial exclusion；
3. Type-III + common-\(U\) exact closure；
4. whether \(\varepsilon^\sharp\) can be bounded by \(0<\varepsilon^\sharp<1\) or a finite absolute set in a sign branch；
5. ten-free tail quotient control；
6. full \(A_1=\varnothing\)；
7. Strict Layer closure。

---

# 53. At most three next-round targets

## Target 1 — Primitive tail-gap quotient × common-\(U\) interval

主对象改为：

\[
\boxed{
\varepsilon^\sharp
=
\frac{b_3(Q_0-P_3)}
{10^{n_3}\gcd(Q_0,V)}
\in\mathbf Z_{>0}.
}
\]

目标是利用：

- plus/minus frozen height；
- \(C_2/C_3\) digit cone；
- \(U\in I_{23}\)；

证明某 branch 中：

\[
0<\varepsilon^\sharp<1
\]

或至少：

\[
\varepsilon^\sharp\in\{1,\ldots,K\}.
\]

这是当前最干净的 backward-to-forward bridge。

---

## Target 2 — Type-III \(R_2=0\) × exact radial count

不要继续 generic \(2\)-adic expansion。

直接使用：

\[
R_2=0
\Longrightarrow
v_2(Q_0-P_3)
\le
n_3+v_2(g_3)
\]

（在 unsaturated \(2\)-side），与：

\[
N_V(I_{23})
\]

做 exact splice。

目标：

\[
R_2=0
\Longrightarrow
N_V(I_{23})=0
\]

或构造明确反例 chamber。

---

## Target 3 — Ten-free quotient exhaustion / backward retirement test

若还希望 backward 保持独立研究线，只研究：

\[
\boxed{
\frac{\operatorname{core}_{10}(Q_0-P_3)}
{\operatorname{core}_{10}(g_3)}
}
\]

与 \(\mathbf B\) 的 exact interaction。

因为当前：

\[
\frac{\delta}{2^{R_2}5^{R_5}}
=
\mathbf B
\frac{\operatorname{core}_{10}(Q_0-P_3)}
{\operatorname{core}_{10}(g_3)}.
\]

如果能 bounded，constant-quotient closure复活。

如果能构造 moving pseudo-family使它无界，则应正式停止独立 backward line，将全部预算合并到 forward moving-profile radial exclusion。

---

# 54. Explicit answers to Q1–Q12

## Q1 — pullback dictionary exact?

\[
\boxed{\textbf{YES}.}
\]

\[
\Pi=UH,\quad
N=U^2N^\sharp,\quad
\Delta=U\delta,\quad
C_+=UC_+^\sharp.
\]

全部 exact。

---

## Q2 — raw WGF radial-homogeneous?

\[
\boxed{\textbf{YES}.}
\]

精确变为：

\[
N^\sharp\mathbf B^2b_3^2
=
G^2S\delta C_+^\sharp.
\]

---

## Q3 — partial-\(5\) phase constrains \(H\) or \(U\)?

\[
\boxed{\textbf{\(H\), not \(U\)}.}
\]

因为 \(5\mid V\Rightarrow5\nmid U\)，可以消去 \(U\)。

---

## Q4 — partial-\(2\) 同样?

\[
\boxed{\textbf{YES}.}
\]

\(2\mid V\Rightarrow U\) odd。

---

## Q5 — \(2\times5\) decimal suffix正确解释?

\[
\boxed{
H\equiv H_{10}\pmod{10^J}.
}
\]

是 primitive prefix cylinder，不是 \(U\)-suffix。

---

## Q6 — \(E,h,c_a,c_N,\ldots\) 是否产生 nonhomogeneous \(U\)-constraint?

\[
\boxed{\textbf{NO, in the audited terminal architecture}.}
\]

\(E,h\) degree 0；

\[
c_a=Uc_a^\sharp,
\qquad
c_N=Uc_N^\sharp,
\]

但 \(U\) 只是可约去的 common content。

没有发现 fixed \(M_{\rm req}>1\) 强迫 \(M_{\rm req}\mid U\)。

---

## Q7 — forward terminal reconstruction 是否意味着 backward gates自动成立?

\[
\boxed{\textbf{YES}.}
\]

并且本轮给出了 direct algebraic dependency，而不只引用“original candidate故显然”。

---

## Q8 — Backward-on-Forward Redundancy Theorem?

\[
\boxed{\textbf{PROVED}.}
\]

---

## Q9 — 能否抽出 Primitive Phase Sieve?

\[
\boxed{\textbf{YES, but it is DERIVED}.}
\]

更干净形式是：

\[
R_p^{\rm det}
=
\max(0,v_p(Q_0-P_3)-n_3-v_p(g_3)).
\]

---

## Q10 — primitive phase + common-\(U\) interval能否得到
\[
M\mid\Omega,\quad0<|\Omega|<KM?
\]

\[
\boxed{\textbf{NOT YET}.}
\]

对最自然的 \(\Omega=\delta\)，exact quotient仍含 moving \(\mathbf B\) 和 ten-free core，故无 absolute \(K\)。

---

## Q11 — Type-III \(R_2=0\) 加 common-\(U\) 后是否仍大量存在?

严格答案：

\[
\boxed{\textbf{OPEN}.}
\]

本轮只证明它是 primitive tail-gap chamber：

\[
v_2(Q_0-P_3)\le n_3+v_2(g_3),
\]

没有证明 uniform radial death，也没有构造 full terminal infinite survivors。

---

## Q12 — backward line还剩真正独立的 proof obligation吗?

若“独立”指 semantic / terminal gate：

\[
\boxed{\textbf{NO}.}
\]

若指可继续利用的 derived proof language：

\[
\boxed{\textbf{YES, CONDITIONAL ON IT PRODUCING A MOVING-PROFILE ELIMINATION}.}
\]

最准确的一句话是：

\[
\boxed{
\textbf{backward 已无独立语义义务；剩余价值只在于能否把 primitive tail-gap invariants}
}
\]

\[
\boxed{
\textbf{真正转化成 }N_V(I_{23})=0\textbf{ 的证明。}
}
\]

---

# 55. Final research verdict

本轮没有闭合 \(A_1\)。

但 forward/backward interface 已经发生了决定性的 architecture correction。

此前可能的错误直觉是：

\[
\text{backward phase}
\longrightarrow
U\text{-residue}
\longrightarrow
\text{radial kill}.
\]

本轮严格证明正确图景是：

\[
\boxed{
\text{backward phase}
\longrightarrow
\text{primitive tail-gap / prefix cylinder}
}
\]

而：

\[
\boxed{
U
}
\]

仍只由：

\[
\boxed{
I_{23}\cap\mathbf Z_{>0}\cap(\mathbf Z/V\mathbf Z)^\times
}
\]

读取。

更强地：

\[
\boxed{
Z_\pm
=
\frac{Q_0\pm P_3}{\gcd(Q_0,P_3)}
}
\]

说明此前 backward 的大块 factor/Gaussian architecture本质上也是 primitive sphere 的规范化投影。

因此本轮之后，最不应继续花 token 的方向是：

- phase \(\to U\)-residue；
- WGF \(\to U\)-divisor；
- \(E\mid\mathbf A\to U\)-content；
- generic 第三个 prime；
- pure \(5\)-adic self-amplification；
- 把 derived local sieve当成新 semantic gate。

真正剩余 frontier 可以压成：

\[
\boxed{
\begin{array}{c}
\text{exact synchronized primitive moving state}
\\
\Downarrow
\\
\text{optional derived tail-gap arithmetic}
\\
\Downarrow
\\
I_{23}
\\
\Downarrow
\\
N_V(I_{23})>0?
\end{array}
}
\]

所以本轮最终等级建议记为：

\[
\boxed{
\textbf{LEVEL 7A — BACKWARD RADIAL REDUNDANCY + PRIMITIVE TAIL-FACTOR COLLAPSE}
}
\]

而不是 A1 closure。

最核心的新 theorem 可以浓缩为：

\[
\boxed{
\textbf{Exact A1 terminal backward arithmetic is a deterministic primitive view plus radial scaling.}
}
\]

从现在开始，若 backward 还要保留独立预算，唯一合理理由是它能从：

\[
Q_0-P_3
\]

的 primitive divisibility真正推出 common-\(U\) interval的整数空性；否则应正式与 forward moving-profile line 合并。
