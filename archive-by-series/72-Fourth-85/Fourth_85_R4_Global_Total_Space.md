# Fourth 85 · R4 — Global Moving-Conic Total Space × Function-Field Norm Geometry × Power-of-Ten Section × Repair-or-Kill

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — \(J=2\)  
**Round:** 第四个八五计划 · R4  
**Inherited live shell attacked:** \(q=1\) negative fixed-\((K,d,\tau)\) family  
**Completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 1. Executive Verdict

R4 **没有**证明完整的

\[
q=1\Longrightarrow\varnothing,
\]

因此也没有证明

\[
J=2\Longrightarrow\varnothing.
\]

但是，本轮第一次获得了第四个八五中真正满足 Novelty Guillotine 的 **function-field information class**，并且它立即关闭了 \(K=10\) 的全部 q=1 negative source cases。

正式 verdict：

\[
\boxed{\texttt{FIXED_TOTAL_SPACE_EXTRACTED=YES}}
\]

\[
\boxed{\texttt{FUNCTION_FIELD_NORM_RIGIDITY=YES}}
\]

\[
\boxed{\texttt{GENERIC_NORM_TORSOR_NONTRIVIAL=YES}}
\]

\[
\boxed{\texttt{K10\_Q1\_NEGATIVE\_CLOSED=YES}}
\]

但：

\[
\boxed{\texttt{FIXED_CURVE_PROJECTION_EXTRACTED=NO}}
\]

\[
\boxed{\texttt{FIXED_EXPONENTIAL_DIOPHANTINE_INTERFACE=NO}}
\]

\[
\boxed{\texttt{TOTAL_SPACE_DIMENSION_DROP=NO}}
\]

\[
\boxed{\texttt{Q1_BRANCH_CLOSED=NO}}
\]

\[
\boxed{\texttt{J2_CLOSED=NO}}.
\]

24 个历史 source cases 中，\(K=10\) 的 8 个全部关闭；剩余 \(K=100,1000\) 共 16 个。

因此：

\[
\boxed{\texttt{Q1_GLOBAL_MOVING_FAMILY_ARCHITECTURE=ALIVE\_WITH\_NEW\_RIGIDITY}}
\]

而不是 DEAD。

本轮最核心的新事实不是“surface 固定”，而是完成平方后 12 个 \((K,\tau)\) coefficient templates 在函数域层进一步坍缩成 **仅 3 个 \(K\)-dependent norm torsors**：

\[
\boxed{
x^2-A_2(G,K)v^2=T_4(G,K)
}.
\]

更强地，这三个 generic torsor 都在 \(\mathbf Q(G)\) 上非平凡；所以 R3 的 moving-field obstruction 确实被消除了，并且消除后产生了新的 arithmetic rigidity。

---

# 2. R1–R3 Architecture Freeze

继续永久冻结：

- q=1 factor-gap architecture；
- \(h\)-support × Gaussian support collision；
- fixed-\(\tau\) specialized Pell field；
- fixed Lucas / fixed unit / fixed recurrence；
- specialize-\(G\)-first 后的 moving real quadratic field；
- full-\(\eta\) parameterization；
- old \(N_0\) square-class repackaging。

R4 不复活这些对象。

历史 q=1 shell：

\[
K\in\{10,100,1000\},
\]

\[
(d,\tau)\in
\{(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)\},
\]

\[
G=10^g,\qquad g-k\ge2.
\]

定义

\[
\rho=a-\frac{\tau G}{10}>0,
\]

并保留

\[
31\rho+\tau\equiv0\pmod{2K},
\]

\[
\gcd(\rho,10\tau)=1,
\]

\[
0<\rho<\frac{10-d\tau}{10d}G.
\]

---

# 3. Exact q=1 Source Skeleton and Residue Quotient

因为

\[
\gcd(31,2K)=1,
\]

对每个 fixed \((K,\tau)\) 存在唯一 residue

\[
r_{K,\tau}\in[0,2K)
\]

满足

\[
31r_{K,\tau}+\tau\equiv0\pmod{2K}.
\]

取

\[
\boxed{\rho=r_{K,\tau}+2Kn},
\qquad n\in\mathbf Z.
\]

12 个 residue：

| \(K\) | \(\tau=1\) | \(\tau=3\) | \(\tau=7\) | \(\tau=9\) |
|---:|---:|---:|---:|---:|
| 10 | 9 | 7 | 3 | 1 |
| 100 | 129 | 187 | 103 | 161 |
| 1000 | 129 | 387 | 903 | 1161 |

于是

\[
a=\frac{\tau G}{10}+r_{K,\tau}+2Kn.
\]

为了避免分母，定义

\[
Z:=10a=\tau G+10r_{K,\tau}+20Kn
\]

以及

\[
\mathcal Y:=10Y_0.
\]

注意这里的 \(n\) 是 **R4 residue quotient**，不是早期 primitive recovery 中满足
\(\tau=-31a+2Kn_{\rm src}\) 的 \(n_{\rm src}\)。完整 source replay 仍必须保留后者的 primitive 条件。

---

# 4. Global Total-Space Construction

历史 fixed-\(\tau\) conic：

\[
Y_0^2=A_2a^2+B_1a+C_0,
\]

其中

\[
\begin{aligned}
A_2={}&100G^6K^2-100G^6+280G^5K^2-380G^5\\
&+236G^4K^2-545G^4+16G^3K^2-362G^3\\
&-52G^2K^2-93G^2-8GK^2+4K^2,
\end{aligned}
\]

\[
B_1=-\tau G^2P(G,K),
\]

\[
\begin{aligned}
P(G,K)={}&20G^5K^2-20G^5+48G^4K^2-68G^4\\
&+32G^3K^2-85G^3-46G^2-4GK^2-4G+3,
\end{aligned}
\]

\[
C_0=\frac{\tau^2G^5}{4}Q_K(G),
\]

\[
Q_K(G)=4G^3K^2-4G^3+8G^2K^2-12G^2+4GK^2-13G-6.
\]

清分母后得到固定 total space：

\[
\boxed{
\mathcal S_{K,\tau}:\quad
\mathcal Y^2=\mathcal F_{K,\tau}(G,n)
}
\]

其中

\[
\boxed{
\mathcal F_{K,\tau}
=
A_2Z^2+10B_1Z+25\tau^2G^5Q_K.
}
\]

这是严格的 \(\mathbf Z[G,n]\) polynomial。

---

# 5. Polynomial Content / Degree / Factorization

对 12 个 fixed \((K,\tau)\) templates 逐一 exact factor audit：

\[
\boxed{\operatorname{content}(\mathcal F_{K,\tau})=1}
\]

\[
\boxed{\deg_G\mathcal F_{K,\tau}=6}
\]

\[
\boxed{\deg_n\mathcal F_{K,\tau}=2}.
\]

这里 \(\deg_G=6\) 值得强调：原始各项表面上可出现更高 \(G\)-次数，但在 boundary-defect translation 后发生 exact cancellation。

12 个 \(\mathcal F_{K,\tau}\) 均在

\[
\mathbf Q[G,n]
\]

上 irreducible。

因此：

- 没有固定 polynomial content 可继续剥离；
- 没有固定 square polynomial factor；
- total-space polynomial 本身不通过 factorization 降维。

**Information gain:** `STRUCTURAL`.

---

# 6. Exact \(n\)-Quadratic Structure

写

\[
Z_0:=\tau G+10r_{K,\tau}.
\]

则

\[
\mathcal F=A_K(G)n^2+B_{K,\tau}(G)n+C_{K,\tau}(G),
\]

其中

\[
\boxed{
A_K(G)=400K^2A_2(G,K)
}
\]

\[
\boxed{
B_{K,\tau}(G)
=
40K\bigl(A_2Z_0+5B_1\bigr)
}
\]

\[
\boxed{
C_{K,\tau}(G)
=
A_2Z_0^2+10B_1Z_0+25\tau^2G^5Q_K.
}
\]

判别式发生关键坍缩：

\[
\boxed{
B_{K,\tau}^2-4A_KC_{K,\tau}
=
\left[
200K\tau G^2(G+1)(2G+3)
\right]^2T_4(G,K)
}
\]

其中

\[
\boxed{
T_4(G,K)
=
4G^4K^2-4G^4+8G^3K^2-12G^3+4G^2K^2-13G^2-6G+1.
}
\]

所以：

\[
\boxed{
(2A_Kn+B_{K,\tau})^2
-
A_2(G,K)(40K\mathcal Y)^2
=
S_{K,\tau}(G)^2T_4(G,K)
}
\]

其中

\[
S_{K,\tau}(G)
=
200K\tau G^2(G+1)(2G+3).
\]

---

# 7. Central R4 Collapse: 12 Templates \(\to\) 3 Fixed Norm Torsors

在 \(\mathbf Q(G)\) 中除以 \(S_{K,\tau}(G)^2\)，令

\[
x=
\frac{2A_Kn+B_{K,\tau}}{S_{K,\tau}},
\]

\[
v=
\frac{40K\mathcal Y}{S_{K,\tau}},
\]

则全部 \(\tau,r,d\) 从 generic norm equation 中消失：

\[
\boxed{
x^2-A_2(G,K)v^2=T_4(G,K).
}
\tag{NF}
\]

所以：

\[
\boxed{
12\text{ coefficient templates}
\longrightarrow
3\text{ function-field torsors}
}
\]

只由

\[
K=10,100,1000
\]

区分。

这是 R4 的第一项 genuine `FUNCTION_FIELD` 信息。

它不是 R3 fixed-\(\tau\) Pell 的改名：R3 在每个 \(G=10^g\) specialization 后得到 moving quadratic field；R4 现在固定的是

\[
\boxed{
\mathbf Q(G)(\sqrt{A_2(G,K)})/\mathbf Q(G).
}
\]

---

# 8. Function-Field Quadratic Extension

对每个 \(K\in\{10,100,1000\}\)：

\[
C_K:\quad z^2=A_2(G,K).
\]

exact CAS audit：

- \(A_2(G,K)\) irreducible；
- squarefree；
- degree \(6\)。

故：

\[
\boxed{g(C_K)=2}.
\]

branch locus 是 \(A_2\) 的 6 个有限简单根。

因为次数为偶数，infinity 不 ramify；有两个 infinity points。

leading coefficient：

\[
100(K^2-1).
\]

而 \(K>1\) 时

\[
(K-1)^2<K^2-1<K^2,
\]

所以 \(K^2-1\) 不是有理平方。两个 infinity points 在

\[
\mathbf Q(\sqrt{K^2-1})
\]

上分裂，在 \(\mathbf Q\) 上互为共轭。

因此 square-class

\[
[A_2]\in\mathbf Q(G)^\times/\mathbf Q(G)^{\times2}
\]

严格 nontrivial。

---

# 9. Function-Field Units

令

\[
R_K=\mathbf Q[G,z]/(z^2-A_2).
\]

任何 unit 的 principal divisor 只能支撑在两个 infinity points。

但这两个 points 在 \(\mathbf Q\) 上共轭。一个 \(\mathbf Q\)-rational principal divisor 若只支撑于它们，Galois invariance 强迫两点系数相同；degree zero 又强迫该系数为零。

所以：

\[
\boxed{R_K^\times=\mathbf Q^\times}.
\]

也就是说，R4 确实得到了一个固定 function field，但它并没有一个可自由吸收 divisor growth 的 \(\mathbf Q\)-rational polynomial Pell unit group。

这直接区分于 R3 的 moving fundamental-unit picture。

**Information gain:** `FUNCTION_FIELD`.

---

# 10. Norm / Divisor Geometry

(NF) 等价于

\[
N_{\mathbf Q(G)(\sqrt{A_2})/\mathbf Q(G)}
(x+v\sqrt{A_2})
=
T_4.
\]

并且

\[
T_4
\]

对三个 \(K\) 都是 irreducible squarefree quartic。

辅助固定曲线：

\[
E_K:\quad w^2=T_4(G,K)
\]

因此具有：

\[
\boxed{g(E_K)=1}.
\]

但必须严格区分：

\[
C_K,\ E_K
\]

是 **auxiliary fixed curves**，不是从每个 source point 得到的 fixed-curve projection。一个 source point不会自动给出

\[
\sqrt{A_2(G,K)}\in\mathbf Q
\]

或

\[
\sqrt{T_4(G,K)}\in\mathbf Q.
\]

所以：

\[
\boxed{\texttt{FIXED_CURVE_PROJECTION_EXTRACTED=NO}}.
\]

---

# 11. Fixed Divisor Support

exact resultant：

\[
\boxed{
\operatorname{Res}_G(A_2,T_4)
=
1024(K-1)^2(K+1)^2
(32K^6+348K^4-1220K^2+727)^2.
}
\]

对三个 \(K\) 非零，所以：

\[
\gcd_{\mathbf Q[G]}(A_2,T_4)=1.
\]

在 genus-2 curve \(C_K\) 上，

\[
\operatorname{div}(T_4)
\]

有：

- 4 个 quartic roots；
- 每个 root 在 unramified quadratic cover 上给两个点；
- 因而 8 个 finite simple zeros；
- 两个 infinity points 各有 pole order 4。

因此 norm RHS 的 divisor support 是固定有限 places。

使用未归一化的 integral identity 时，额外加入

\[
G=0,\quad G=-1,\quad G=-\frac32
\]

上方的 fixed places；仍是 fixed \(S\)。

所以 R4 确实建立了合法的：

\[
\boxed{\text{fixed function-field }S}.
\]

但是这个 \(S\)-unit structure只直接控制 **rational-function sections**；不能把单个 arithmetic specialization 偷换成 function-field solution。

---

# 12. Generic Norm Torsor Is Nontrivial

定义 quaternion class

\[
\boxed{
\beta_K=(A_2,T_4)\in\operatorname{Br}(\mathbf Q(G))[2].
}
\]

若 (NF) 在 \(\mathbf Q(G)\) 上有点，则 \(\beta_K=0\)。

R4 给出一个非常直接的反证。

固定任意

\[
K\in\{10,100,1000\}.
\]

对所有整数

\[
G\equiv1\pmod{16},
\]

exact residue audit 给：

\[
A_2(G,K)\equiv56\pmod{64},
\]

\[
T_4(G,K)\equiv14\pmod{16}.
\]

因此在 \(\mathbf Q_2\)：

\[
v_2(A_2)=3,\qquad A_2/8\equiv7\pmod8,
\]

\[
v_2(T_4)=1,\qquad T_4/2\equiv7\pmod8.
\]

2-adic Hilbert symbol：

\[
\boxed{(A_2,T_4)_2=-1}.
\]

所以每个这样的 specialization 都没有 \(\mathbf Q_2\)-point。

假设 generic conic 有 \(\mathbf Q(G)\)-point。其 rational functions 只在有限个 \(G\)-值有 pole / indeterminacy。无限多个

\[
G\equiv1\pmod{16}
\]

避开这些例外，从而应 specialize 出 \(\mathbf Q\)-point，矛盾。

故：

\[
\boxed{\beta_K\neq0}
\]

并且：

\[
\boxed{
x^2-A_2v^2=T_4
\text{ 在 }\mathbf Q(G)\text{ 上无 rational section}.
}
\]

这是本轮最重要的 Architecture Shock 结果：

\[
\boxed{
\text{global family geometry 不是一个有大量 }\mathbf Q(G)\text{-sections 的 trivial conic bundle}.
}
\]

---

# 13. Exact \(K=10\) Power-of-Ten Closure

现在把特殊 arithmetic section

\[
G=10^g
\]

加回来。

对于

\[
K=10,
\]

有

\[
T_4(G,10)
=
396G^4+788G^3+387G^2-6G+1.
\]

又：

\[
G=10^g=(1+9)^g\equiv1+9g\pmod{81}.
\]

直接计算：

\[
T_4(1,10)=1566\equiv27\pmod{81},
\]

以及

\[
T_4'(1,10)=4716\equiv0\pmod9.
\]

Taylor modulo \(81\) 因此给：

\[
\boxed{
T_4(10^g,10)\equiv27\pmod{81}
}
\]

对所有 \(g\ge1\) 成立。

故：

\[
\boxed{v_3(T_4)=3}.
\]

另一方面，

\[
G\equiv K\equiv1\pmod3,
\]

而

\[
A_2(1,1)\equiv2\pmod3.
\]

故：

\[
\boxed{
A_2(10^g,10)\equiv2\pmod3
}
\]

是 \(3\)-进 nonsquare unit。

于是

\[
\mathbf Q_3(\sqrt{A_2})/\mathbf Q_3
\]

是 unramified quadratic extension；其 norm 的 \(3\)-进 valuation 必须为偶数。

但 (NF) 要求

\[
N(x+v\sqrt{A_2})=T_4
\]

而右端 valuation 为 3，矛盾。

因此：

\[
\boxed{
K=10,\ q=1,\ \text{negative branch}
\Longrightarrow\varnothing.
}
\]

\(K=10\) 对应的 8 个 \((d,\tau)\) source cases 全部关闭。

这是：

\[
\boxed{\texttt{BRANCH_CLOSURE}}
\]

级别的信息。

---

# 14. Why the Same \(3\)-adic Killer Does Not Close \(K=100,1000\)

exact check：

对于实际 power-of-ten base，

\[
K=100\quad\text{或}\quad1000,
\]

仍有

\[
A_2\equiv2\pmod3,
\]

但

\[
v_3(T_4)=2
\]

而不是 3。

因此 unramified quadratic norm 的 parity gate 不矛盾。

所以不能把 \(K=10\) proof机械复制到其余 16 source cases。

R4 不伪造完整 q1 closure。

---

# 15. Cleared Affine Singular-Locus Audit

清分母 total space 的 \(n\)-discriminant 包含 square factor：

\[
G^4(G+1)^2(2G+3)^2.
\]

当 \(A_K\neq0\) 时，二次曲面

\[
\mathcal Y^2=A_Kn^2+Bn+C
\]

的 affine singularity 出现在 repeated-discriminant base points。

三个 singular points：

\[
\boxed{
G=0,\quad
n=-\frac r{2K},\quad
\mathcal Y=0
}
\]

\[
\boxed{
G=-1,\quad
n=-\frac{20r+3\tau}{40K},\quad
\mathcal Y=0
}
\]

\[
\boxed{
G=-\frac32,\quad
n=-\frac{145r+12\tau}{290K},\quad
\mathcal Y=0.
}
\]

并且：

\[
A_2(0)=4K^2,\qquad
A_2(-1)=4,\qquad
A_2(-3/2)=\frac{841K^2}{16},
\]

均非零。

这些 singularities 来自 clearing / completion 中的 square discriminant factors，而不是 actual power-of-ten section 的 arithmetic singularity。

---

# 16. Conic-Bundle / Surface Classification

归一化后 generic fibre：

\[
x^2-A_2(G,K)v^2=T_4(G,K).
\]

因此 R4 total space 是一个固定 conic bundle over the \(G\)-line。

square factors

\[
G^4(G+1)^2(2G+3)^2
\]

被 minimal normalization 吸收后，真正的 geometric degenerate fibres 位于

\[
T_4(G,K)=0
\]

的 4 个简单根。

在 \(\overline{\mathbf Q}\) 上，它是 rational surface：\(\overline{\mathbf Q}(G)\) 上 conic 有点。

但：

\[
\boxed{
\text{geometrically rational}
\neq
\text{\(\mathbf Q\)-rational}.
}
\]

R4 已证明 generic conic 无 \(\mathbf Q(G)\)-section，因此不能把 surface 判为“太灵活而死亡”。

这正是 function-field twist 的 arithmetic content。

---

# 17. Normalization by Powers of \(G\)

设

\[
u=\frac nG,
\qquad
v_\infty=\frac{\mathcal Y}{G^4}.
\]

则：

\[
\frac{\mathcal F(G,uG)}{G^8}
=
40000K^2(K^2-1)u^2+O(G^{-1}).
\]

所以固定 \(u\neq0\) 时：

\[
\boxed{
\frac{v_\infty}{u}
=
\pm200K\sqrt{K^2-1}+O(G^{-1}).
}
\]

等价：

\[
\boxed{
\frac{\mathcal Y}{nG^3}
=
\pm200K\sqrt{K^2-1}+O(G^{-1}).
}
\]

leading slope 确实 irrational。

但这不足以调用 Roth / Ridout。

在 source sector 中若

\[
n\asymp G,
\]

则 rational denominator

\[
nG^3\asymp G^4,
\]

而 approximation error 只有

\[
O(G^{-1})=O(q^{-1/4}),
\]

远弱于 Roth 型

\[
q^{-2-\varepsilon}.
\]

而且 sector 允许

\[
u=n/G\to0,
\]

此时连除以 \(u\) 的 asymptotic 都失效。

所以：

\[
\boxed{\texttt{IRRATIONAL\_SLOPE\_AUTO\_EXTINCTION=FALSE}}.
\]

**Information gain:** `STRUCTURAL`, not closure.

---

# 18. Source Sector

由

\[
\rho=r+2Kn
\]

以及

\[
0<\rho<\frac{10-d\tau}{10d}G
\]

得到：

\[
0\le\frac nG
<
\frac{10-d\tau}{20Kd}
-
\frac{r}{2KG}.
\]

因此：

\[
\boxed{
u=\frac nG
\in
\left[
0,\frac{10-d\tau}{20Kd}
\right)
+O(G^{-1}).
}
\]

这是真正的 fixed Archimedean sector。

但它没有把 \(u\) 压成单个 slope；仍保留一维 interval freedom。

---

# 19. Fixed-Curve Projection Audit

R4 得到两个漂亮固定曲线：

\[
C_K:z^2=A_2(G,K),\qquad g=2,
\]

\[
E_K:w^2=T_4(G,K),\qquad g=1.
\]

然而 source point

\[
(G,n,\mathcal Y)
\]

不自然给出 \(z\in\mathbf Q\) 或 \(w\in\mathbf Q\)。

因此它们是 **coefficient / discriminant covers**，不是 arithmetic projection。

没有合法得到

\[
(G,n,\mathcal Y)\mapsto(U,V)\in C(\mathbf Q)
\]

从而把全部 source points压到 fixed curve rational points。

正式：

\[
\boxed{\texttt{FIXED_CURVE_PROJECTION_EXTRACTED=NO}}.
\]

---

# 20. Fixed Exponential Interface Audit

直接 substitute

\[
G=10^g
\]

当然得到固定 exponential-polynomial equation

\[
\mathcal F(10^g,n)=\mathcal Y^2.
\]

但这不满足 R4 的高标准，因为 coefficients 仍随 \(n,\mathcal Y\) 自由变化；它不能直接成为 fixed \(S\)-unit linear relation、fixed recurrence 或 Baker equation。

所以不把形式上的

\[
F(n,\mathcal Y,10^g)=0
\]

奖励成：

\[
\texttt{FIXED\_EXPONENTIAL\_DIOPHANTINE\_INTERFACE}.
\]

唯一真正利用 power-of-ten 的新算术，是 \(K=10\) 的 fixed 3-adic norm obstruction。

---

# 21. Primitive-\(h\) Quotient Audit

重新设

\[
y=hy_1,\qquad
\rho=h\rho_1,\qquad
\gcd(y_1,\rho_1)=1,
\]

并使用

\[
h\mid\Psi_K(G)
\]

不会自动增加 algebraic codimension。

若写

\[
\Psi_K(G)=hm,
\]

只是增加变量 \(m\) 和一条定义方程；除非新的 primitive equation消掉 \(h\) 或强迫 fixed support，否则 dimension count 不下降。

R4 没有发现这种 degree drop。

因此：

\[
\boxed{\texttt{PRIMITIVE\_h\_TOTAL\_SPACE\_DIMENSION\_DROP=NO}}.
\]

并按 prompt 纪律停止，不重启 support collision。

---

# 22. Function-Field \(S\)-Unit / Mason Audit

固定 divisor support 已经建立。

但是：

- 对真正 rational-function section，norm factorization可进入 fixed function-field divisor allocation；
- 对 isolated arithmetic specialization，这不能直接套用；
- generic torsor甚至没有 \(\mathbf Q(G)\)-section。

因此 Mason / function-field abc 当前最自然的作用是 **section classification / no-section certificate**，而不是直接逐 \(g\) 杀 arithmetic fibres。

R4 已经通过 2-adic specialization更直接地证明 no generic section，因此没有必要继续制造庞大 function-field \(S\)-unit machinery。

---

# 23. Runge / Integral-Point Audit

当前没有从 source point合法投影到 fixed affine curve，因此 Runge 不可直接启动。

辅助 genus-2 / genus-1 curves 的 integral points 并不是 source points。

所以：

\[
\boxed{\texttt{RUNGE\_INTERFACE=NOT\_YET\_LEGAL}}.
\]

---

# 24. Counterexample Guillotine

### Conjecture A — total space 自动产生新 codimension

**FALSE.**

surface 仍二维；没有 dimension drop。

### Conjecture B — function-field norm geometry 比 specialized Pell 更刚性

**TRUE, but partially.**

它给出 fixed genus-2 quadratic extension、fixed divisor support、nonzero quaternion class，并关闭 \(K=10\)。

### Conjecture C — \(n/G\) normalization 完全消掉 \(G\)

**FALSE.**

只在 leading weighted infinity form 中消掉 \(G\)。

### Conjecture D — power-of-ten 自动形成 fixed \(S\)-unit equation

**FALSE.**

只有 function-field \(S\) 固定；arithmetic prime support 仍不固定。

### Conjecture E — infinity 给 \(n=\lambda G+O(1)\)

**FALSE.**

source sector保留整段 \(u=n/G\) freedom；没有单一 \(\lambda\)。

### Conjecture F — irrational slope 自动排除 \(10^g\)

**FALSE.**

approximation exponent 远远不够。

---

# 25. Information Gain Ledger

| Result | Grade |
|---|---|
| explicit fixed total space | `STRUCTURAL` |
| 12 templates all primitive irreducible | `STRUCTURAL` |
| 12 \(\to\) 3 norm torsors | `FUNCTION_FIELD` |
| genus-2 fixed quadratic function field | `FUNCTION_FIELD` |
| \(R_K^\times=\mathbf Q^\times\) | `FUNCTION_FIELD` |
| fixed divisor support | `FUNCTION_FIELD` |
| nonzero \(\beta_K=(A_2,T_4)\) | `FUNCTION_FIELD` |
| no \(\mathbf Q(G)\)-section | `FUNCTION_FIELD` |
| \(K=10\) all q1 negative cases empty | `BRANCH_CLOSURE` |
| \(n/G\) sector | `STRUCTURAL` |
| irrational infinity slope | `STRUCTURAL` |
| fixed arithmetic curve projection | `ZERO` / not obtained |
| fixed exponential interface | `ZERO` / not obtained |
| full q1 closure | not obtained |

---

# 26. Architecture Shock Checkpoint

必须分别回答两个问题。

## 26.1 保持 \(G\) 为变量后，是否消除了 R3 moving-field obstruction？

\[
\boxed{\textbf{YES}.}
\]

R3 的 specialized fields

\[
\mathbf Q(\sqrt{D_{K,g}})
\]

被替换为真正 fixed function fields

\[
\boxed{
\mathbf Q(G)(\sqrt{A_2(G,K)})
}.
\]

而且 12 \(\tau\)-templates 在 generic norm 层压成 3 个 \(K\)-torsors。

## 26.2 消除 moving-field obstruction 后，是否产生新 arithmetic rigidity？

\[
\boxed{\textbf{YES}.}
\]

不是仅仅“surface fixed”。

新 rigidity 包括：

1. genus-2 fixed cover；
2. 无 nonconstant \(\mathbf Q\)-units；
3. fixed divisor support；
4. nonzero quaternion class；
5. generic no-section theorem；
6. \(K=10\) actual power-ten 3-adic norm obstruction，关闭 8 source cases。

所以本轮不触发

\[
\texttt{Q1\_GLOBAL\_MOVING\_FAMILY\_ARCHITECTURE=DEAD}.
\]

---

# 27. Final q=1 Verdict

\[
\boxed{
K=10:
\quad q=1\text{ negative branch CLOSED}.
}
\]

\[
\boxed{
K=100,1000:
\quad q=1\text{ negative branch OPEN}.
}
\]

因此：

\[
\boxed{
q=1\Longrightarrow\varnothing
\quad\text{NOT YET PROVED}.
}
\]

历史 24 cases：

\[
\boxed{
24\to16.
}
\]

---

# 28. R5 Reallocation Decision

R4 获得了 genuine function-field rigidity，并且产生 actual branch closure，因此 R5 **允许 exploitation**。

但 R5 不应回到“继续分类 surface”。

最高 marginal-value target 应是：

\[
\boxed{
K=100,1000
}
\]

上的 specialized evaluation of the fixed Brauer / norm torsor：

\[
\beta_K(10^g)
=
(A_2(10^g,K),T_4(10^g,K)).
\]

具体应优先问：

1. 是否存在按 \(g\) 的有限 residue classes 分裂的 fixed local obstruction；
2. 是否能对 Hilbert-symbol ramification做 reciprocity / resultant-level compression，而不 factor \(T_4(10^g,K)\)；
3. 是否存在 fixed finite cover of exponent classes；
4. 如果 local obstruction不是 uniform，是否可证明 surviving locally soluble fibres落到 fixed curve / finite exponential interface；
5. 若这些都失败，再宣布 function-field architecture 对剩余 \(K\) 的 marginal value耗尽。

**不建议** R5 重新做 generic genus / surface classification；这些在 R4 已经足够清楚。

---

# 29. Generated Artifact Index

主文件：

`Fourth_85_R4_Global_Total_Space.md`

Function-field certificate：

`Fourth_85_R4_Function_Field_Norm_Certificate.md`

\(K=10\) partial closure certificate：

`Fourth_85_R4_K10_q1_Local_Closure_Certificate.md`

计算目录：

`Fourth_85_R4_computation/`

其中包括：

- exact total-space polynomial skeleton；
- 12-template content / degree / irreducibility audit；
- \(A_2,T_4\) factorization；
- exact resultant；
- singular locus；
- genus / function-field data；
- 2-adic generic torsor nontriviality；
- \(K=10\) power-ten 3-adic closure；
- weighted infinity audit；
- conic-bundle classification；
- reproducible symbolic certificate script。

---

# 30. Terminal Statement

R4 的结果不是：

> “把 moving conics 合起来得到一个漂亮 surface。”

真正结果是：

\[
\boxed{
\text{24 source cases}
\to
\text{12 polynomial templates}
\to
\text{3 fixed function-field norm torsors}
}
\]

并且这些 torsors：

\[
\boxed{
x^2-A_2(G,K)v^2=T_4(G,K)
}
\]

具有 genuinely nontrivial arithmetic twisting。

其中 \(K=10\) 在 actual power-of-ten section 上被一个 exact \(3\)-adic norm parity obstruction 直接处决。

所以第四个八五第一次从“moving field 无法统一”跨到了：

\[
\boxed{
\text{fixed function-field class}
+
\text{actual arithmetic branch closure}.
}
\]

这足以授权 R5，但 R5 的目标必须非常窄：

\[
\boxed{
\text{evaluate / exploit the same fixed norm-Brauer structure on }K=100,1000.
}
\]

如果下一轮证明这两个 \(K\) 上的 power-ten incidence不能被 fixed local / reciprocity / exponential mechanism控制，则再正式 Kill；本轮还没有理由处决这条 architecture。
