# 第二个八五计划·第三轮
## Band-Conditioned Primitive Height Guillotine × Rational-Conic Parameterization × Source-Lattice Denominator Explosion

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 第二个八五计划·R3  
**Global completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 0. Executive Verdict

本轮没有关闭 \(J=2\)，也没有找到 Band-Conditioned Primitive Height Guillotine 的 exact counterexample。

真正的新进展是：

\[
\boxed{
\text{projective root ray}
\longrightarrow
\text{source-lattice primitive ray}
\longrightarrow
\text{decimal content synchronization}
\longrightarrow
\text{absolute height}
}
\]

这条链第一次被完整写成 exact algebra。

核心新接口不是“source lattice 的 determinant 很大”，而是：

\[
\boxed{
\textbf{source-lattice primitive content 在 }2,5\textbf{ 上必须精确同步。}
}
\]

在 source-adapted quadratic parameterization 的基底坐标

\[
(X(a,b),Y(a,b),N(a,b))
\]

中，若

\[
D(a,b)=\gcd(X,Y,N),
\]

则 raw ten-unit condition 精确等价于

\[
\boxed{
v_p(X)=v_p(Y)=v_p(D)\le v_p(N),
\qquad p=2,5.
}
\tag{PCS}
\]

这使真正的 denominator explosion 机制变成：

\[
\boxed{
\textbf{high-modulus slope congruence forced by primitive-content synchronization},
}
\]

而不是单纯的 finite-index lattice sparsity。

当前终端判决：

```text
J2_STATUS = OPEN

BAND_CONDITIONED_PRIMITIVE_HEIGHT = OPEN

RATIONAL_CONIC_PARAMETERIZATION = COMPLETE
SOURCE_LATTICE_PULLBACK = PARTIAL
CONTENT_BOUND = PROVED

DENOMINATOR_EXPLOSION = PLAUSIBLE

FIXED_FIBRE_HEIGHT_THEOREM = PROVED
UNIFORM_HEIGHT_THEOREM = OPEN

SMALL_HEIGHT_COUNTERMODEL = NOT_FOUND

INTEGER_COMMON_U_CANDIDATE = NOT_REACHED
FULL_COMMON_U_COUNTERMODEL = NOT_FOUND

MOVING_INFORMATION_ACTIVATED = YES

MOVING_HEIGHT_MECHANISM =
DECIMAL_PRIMITIVE_CONTENT_SYNCHRONIZATION
(identified exactly; uniform height transfer still open)

R3_TERMINAL_VERDICT = UNIFORMIZATION_REQUIRED
```

R4 不再允许重新发散。唯一接口冻结为：

\[
\boxed{
\textbf{Uniform Two-Prime Primitive-Content Height Transfer}.
}
\]

---

# 1. R1–R2 Frozen Verdicts

R1–R2 的以下判决全部冻结。

```text
THEOREM_A = FALSE
DISCRIMINANT_ALONE = OLD_INFORMATION_CLASS

CLASS_INTERFACE = NOT_VISIBLE
DESCENT_INTERFACE = NOT_VISIBLE

REAL_RADIAL_INCOMPATIBILITY = FALSE
```

因此本轮没有重新使用：

- ambient square nonrepresentation；
- discriminant sharpening；
- genus / class group / spinor genus；
- generic descent；
- floor/carry；
- terminal residual；
- odd-prime allocation。

R2 已证明：

\[
\boxed{
I_2\cap I_3\neq\varnothing
\iff
\frac1{10}<\rho<10
}
\]

其中

\[
\boxed{
\rho=\frac{C_2}{GKc}.
}
\]

并且

\[
\boxed{
\rho
=
\frac{A}{GK}
+
\frac{t}{2K},
\qquad
t=\frac{\lambda}{c}.
}
\tag{1.1}
\]

所以 decade band 精确等价于

\[
\boxed{
\frac K5-\frac{2A}{G}
<
t
<
20K-\frac{2A}{G}.
}
\tag{1.2}
\]

---

# 2. Exact Homogeneous Conic

沿用：

\[
G=10^g,\qquad
K=10^k,\qquad
H=\frac G2,
\]

\[
uq=G+1,
\qquad
A=2u+1,
\qquad
B=2G+q.
\]

PRE\_ROOT variables：

\[
C_3=c,
\qquad
C_2=Ac+H\lambda,
\]

\[
2KC_1=Bz+A\lambda,
\qquad
T=Gz+u\lambda,
\]

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

full root equation：

\[
\boxed{
H^2C_1^2+w^2-Td_2=0.
}
\tag{ROOT}
\]

清除 \(C_1\) 的 \(2K\) 分母，定义：

\[
\boxed{
\Phi_{g,k,u}(c,z,\lambda)
=
G^2(Bz+A\lambda)^2
+
16K^2w^2
-
16K^2Td_2.
}
\tag{2.1}
\]

于是：

\[
\boxed{
\Phi=16K^2
\left(
H^2C_1^2+w^2-Td_2
\right),
}
\]

故 exact root 等价于：

\[
\boxed{\Phi(c,z,\lambda)=0}
\]

同时保留 source-lattice divisibility

\[
\boxed{
2K\mid Bz+A\lambda.
}
\tag{2.2}
\]

\(\Phi\) 是整数系数齐次二次式。

---

# 3. Projective Affine Chart

在 genuine positive source state 中：

\[
c>0.
\]

所以 chart \(c\neq0\) 覆盖当前正向 source branch。

定义：

\[
\boxed{
s=\frac zc,
\qquad
t=\frac{\lambda}{c}.
}
\]

除以 \(c^2\)：

\[
\boxed{
\mathcal F_{g,k,u}(s,t)
=
H^2
\left(
\frac{Bs+At}{2K}
\right)^2
+
(GHs-uA)^2
-
(Gs+ut)
\left(
u+G(GHs-uA)
\right)
=0.
}
\tag{3.1}
\]

points at infinity 对应 \(c=0\)。它们不属于当前 positive \(C_3=c>0\) source state，但在 projective parameterization 中必须保留为边界点。

若某 outer fibre 的 ternary conic 退化，则必须单独线性因子化；本报告的 chord theorem 对 nondegenerate fibre 使用。当前计算证书所覆盖的 live fibres 均通过 exact nonzero parameterization regression。

---

# 4. Exact Source Lattice

由于 inherited condition

\[
\gcd(A,10)=1,
\]

而

\[
2K=2\cdot10^k,
\]

故：

\[
\gcd(A,2K)=1.
\]

定义唯一 residue：

\[
\boxed{
r_0
\equiv
-A^{-1}B
\pmod{2K},
\qquad
0\le r_0<2K.
}
\tag{4.1}
\]

则：

\[
2K\mid Bz+A\lambda
\iff
\boxed{
\lambda=r_0z+2Kn
}
\]

对某个 \(n\in\mathbf Z\)。

因此 exact source lattice 为：

\[
\boxed{
\Lambda_{\rm src}
=
\mathbf Ze_1
\oplus
\mathbf Ze_2
\oplus
\mathbf Ze_3
}
\]

其中：

\[
\boxed{
e_1=(1,0,0),
\quad
e_2=(0,1,r_0),
\quad
e_3=(0,0,2K).
}
\tag{4.2}
\]

任意 source-lattice point 唯一写成：

\[
\boxed{
(c,z,\lambda)
=
(x,y,r_0y+2Kn).
}
\tag{4.3}
\]

这一步完全 exact；source-lattice 本身已经被拉直。

---

# 5. Rational-Conic Parameterization

设 fixed fibre 上存在一个 nonzero integral isotropic source-lattice point

\[
p\in\Lambda_{\rm src},
\qquad
\Phi(p)=0.
\]

如果只先知道 ambient rational point，可先清分母，再乘一次 lattice index 使其进入 \(\Lambda_{\rm src}\)。齐次性保证仍为 isotropic point。

令：

\[
\mathcal B_\Phi(x,y)
=
\Phi(x+y)-\Phi(x)-\Phi(y)
\]

为 integral polar form。

若 \(p\) 的 \(e_3\)-coordinate 非零，取 transverse plane：

\[
y(a,b)=ae_1+be_2.
\]

定义：

\[
\boxed{
R(a,b)
=
\Phi(y(a,b))\,p
-
\mathcal B_\Phi(p,y(a,b))\,y(a,b).
}
\tag{5.1}
\]

则：

\[
\boxed{
R(a,b)\in\Lambda_{\rm src},
}
\]

每个 coordinate 都是 \(a,b\) 的 homogeneous quadratic polynomial，并且：

\[
\boxed{
\Phi(R(a,b))=0.
}
\tag{5.2}
\]

证明：将直线 \(p+\tau y\) 代入 \(\Phi\)：

\[
\Phi(p+\tau y)
=
\tau\mathcal B_\Phi(p,y)
+
\tau^2\Phi(y),
\]

除去已知根 \(\tau=0\)，第二交点正是 (5.1) 的 projective class。

只要 conic nondegenerate 且 transverse plane 不含 \(p\)，每条经过 \(p\) 的 projective line 唯一与该 plane 相交，因此 (5.1) 参数化全部 rational rays。

\[
(a,b)\sim(-a,-b)
\]

给同一 projective point，因为所有 coordinates 为 degree \(2\)。

若选定 plane 不 transverse，只需在三组

\[
\langle e_1,e_2\rangle,\quad
\langle e_1,e_3\rangle,\quad
\langle e_2,e_3\rangle
\]

中换一组。至少一组可用。

因此：

```text
RATIONAL_CONIC_PARAMETERIZATION = COMPLETE
```

这里的 COMPLETE 是 rational-ray level；它不等于 full source arithmetic closure。

---

# 6. Primitive Ray Selector

把 (5.1) 写成 raw coordinates：

\[
R(a,b)
=
\bigl(
R_c(a,b),R_z(a,b),R_\lambda(a,b)
\bigr).
\]

因为 \(R(a,b)\in\Lambda_{\rm src}\)，

\[
\boxed{
R_n(a,b)
=
\frac{
R_\lambda-r_0R_z
}{2K}
\in\mathbf Z.
}
\tag{6.1}
\]

定义 source-basis content：

\[
\boxed{
D_\Lambda(a,b)
=
\gcd
\left(
R_c,R_z,R_n
\right).
}
\tag{6.2}
\]

则该 rational ray 在 \(\Lambda_{\rm src}\) 中的 primitive generator 为：

\[
\boxed{
(c_0,z_0,\lambda_0)
=
\frac1{D_\Lambda}
\bigl(
R_c,R_z,R_\lambda
\bigr),
}
\tag{6.3}
\]

再由 positive source orientation 固定整体符号。

这比 raw gcd

\[
\gcd(R_c,R_z,R_\lambda)
\]

更正确，因为 primitive normalization 必须在真正 source lattice 内执行。

---

# 7. Full Primitive 与 Lattice Primitive 的区别

定义：

\[
P_1=GHC_1,
\]

\[
P_2=uGC_2,
\]

\[
P_3=uc,
\]

\[
Q_0=P_2+d_2.
\]

full primitive condition 是：

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\tag{7.1}
\]

若 source-lattice point 在 \(\Lambda_{\rm src}\) 中仍有 common content \(d>1\)，则所有 source-derived linear quantities均乘 \(d\)，四个 primitive blocks 也都乘 \(d\)。

因此：

\[
\boxed{
\text{full primitive}
\Longrightarrow
\text{source-lattice primitive}.
}
\tag{7.2}
\]

反向不成立。

所以真正参数筛选顺序必须是：

\[
\boxed{
(a,b)
\to
D_\Lambda
\to
v_0
\to
\gcd(P_1,P_2,P_3,Q_0).
}
\]

不能把 raw parameter numerator 的 gcd 当作 full primitive。

---

# 8. Fixed-Fibre Global Content Bound

把 source-basis coordinate quadratics 的固定 coefficient content 先整体除去，得到 primitive coefficient forms：

\[
f_1(a,b),\qquad
f_2(a,b),\qquad
f_3(a,b).
\]

于是：

\[
D_\Lambda(a,b)
=
\gcd(f_1(a,b),f_2(a,b),f_3(a,b))
\]

差一个已经固定除去的 fibre constant。

若三式在 \(\mathbf Q[a,b]\) 上没有共同 projective zero，则由 homogeneous Bézout / resultant elimination，存在只依赖该 fixed fibre 和 chart 的非零整数：

\[
\kappa_0,\qquad
\kappa_\infty
\]

使：

\[
\kappa_0 a^N
\in
(f_1,f_2,f_3),
\]

\[
\kappa_\infty b^N
\in
(f_1,f_2,f_3)
\]

对某个固定 \(N\) 成立。

若：

\[
\gcd(a,b)=1,
\]

则逐 prime 选取 \(a\) 或 \(b\) 的 unit chart，得到：

\[
\boxed{
D_\Lambda(a,b)
\mid
\mathfrak D_{g,k,u},
}
\tag{8.1}
\]

其中可取：

\[
\boxed{
\mathfrak D_{g,k,u}
=
|\kappa_0\kappa_\infty|.
}
\]

若某一对 coordinate forms 已 coprime，则可更具体取两个 affine charts 的 pairwise resultants product。

所以：

```text
CONTENT_BOUND = PROVED
```

但必须强调：

\[
\boxed{
\mathfrak D_{g,k,u}
\text{ 当前没有 uniform 小上界。}
}
\]

它可以随 fibre 和 basepoint 很大，因此 (8.1) 本身不够推出：

\[
c_0\ge G.
\]

这正是 fixed-fibre content theorem 与 uniform height theorem 的边界。

---

# 9. Radial Band Pullback

由：

\[
\lambda_0
=
r_0z_0+2Kn_0,
\]

且 content 在 ratio 中消去：

\[
\boxed{
t(a,b)
=
\frac{\lambda_0}{c_0}
=
\frac{
r_0f_2(a,b)+2Kf_3(a,b)
}{
f_1(a,b)
}.
}
\tag{9.1}
\]

定义：

\[
t_-=
\frac K5-\frac{2A}{G},
\qquad
t_+=
20K-\frac{2A}{G}.
\]

则：

\[
\boxed{
\mathscr M_{g,k,u}
=
\left\{
[a:b]\in\mathbf P^1(\mathbf R):
t_-<t(a,b)<t_+
\right\}
}
\tag{9.2}
\]

再与全部 source positivity/orientation quadratic inequalities 相交。

因为 \(f_i\) 都是 binary quadratics，所有边界由 quadratic equations 给出。

因此：

\[
\boxed{
\mathscr M_{g,k,u}
}
\]

是有限个 real intervals 的并。

这给出了 exact slope reduction；数值 endpoint 只用于侦察，不参与 theorem 判决。

---

# 10. Primitive Radial Height Formula

source primitive representative：

\[
c_0=
\frac{|f_1(a,b)|}{D_\Lambda(a,b)}.
\]

又：

\[
\lambda_0
=
\frac{
r_0f_2(a,b)+2Kf_3(a,b)
}{
D_\Lambda(a,b)
}.
\]

所以：

\[
C_{2,0}
=
Ac_0+H\lambda_0.
\]

于是：

\[
\boxed{
\mathfrak H_{\rm rad}(a,b)
=
\max
\left(
\frac{|f_1(a,b)|}{G D_\Lambda(a,b)},
\;
\frac{
\left|
A f_1
+
H(r_0f_2+2Kf_3)
\right|
}{
G^2K D_\Lambda(a,b)
}
\right).
}
\tag{10.1}
\]

这就是 R3 真正需要 lower-bound 的 exact rational function。

---

# 11. 关键新定理：Decimal Primitive-Content Synchronization

这是本轮最重要的新 exact observation。

在 source basis 中：

\[
(c,z,\lambda)
=
(X,Y,r_0Y+2KN).
\]

令：

\[
D=\gcd(X,Y,N).
\]

source primitive representative 为：

\[
\left(
\frac XD,
\frac YD,
r_0\frac YD+2K\frac ND
\right).
\]

由于 \(A,B\) 都是 ten-units，而：

\[
r_0\equiv-A^{-1}B\pmod{2K},
\]

所以：

\[
\gcd(r_0,10)=1.
\]

对：

\[
p\in\{2,5\},
\]

因为 \(p\mid2K\)：

\[
\lambda_0
\equiv
r_0 z_0
\pmod p.
\]

所以：

\[
p\nmid c_0z_0\lambda_0
\]

当且仅当：

\[
p\nmid c_0,
\qquad
p\nmid z_0.
\]

而：

\[
v_p(D)
=
\min
\left(
v_p(X),v_p(Y),v_p(N)
\right).
\]

故得到：

## Theorem R3-PCS

\[
\boxed{
p\nmid c_0z_0\lambda_0
\iff
v_p(X)
=
v_p(Y)
=
\min(v_p(X),v_p(Y),v_p(N)),
}
\tag{PCS}
\]

对 \(p=2,5\) 分别成立。

这是：

\[
\boxed{
\textbf{primitive denominator/content explosion 的第一个 exact interface}.
}
\]

它不是 prime-by-prime hunting，而是 source primitive normalization 在 decimal primes 上的整体 equality condition。

---

# 12. 为什么 Pure Lattice-Determinant Mechanism 不够

有限指数 lattice 本身不能成为最终 obstruction。

对 homogeneous rational conic：

1. 任一 rational ray 可清分母成 integral ray；
2. 再乘 lattice index 可进入任意 fixed full-rank finite-index lattice；
3. 在 lattice basis 内再除 coordinate gcd 得 primitive lattice point。

因此：

\[
\boxed{
\text{finite-index source lattice}
}
\]

本身只能改变 primitive representative 的绝对 scale / content，不会把 nonempty rational projective arc 自动变空。

所以 M1/M2 的合法版本必须是：

\[
\boxed{
\text{lattice}
+
\text{primitive content}
+
\text{absolute decimal height}.
}
\]

不能只证明 “determinant 很大”。

---

# 13. \(g=5\) Source-Adapted Content Audit

使用此前 frozen finite scan 中全部 \(g=5\) live \(N_0\)-split outer fibres：

\[
(5,1,11,9091),
\]

\[
(5,3,11,9091),
\]

\[
(5,4,11,9091),
\]

\[
(5,1,9091,11),
\]

\[
(5,3,9091,11).
\]

这里 tuple 顺序为：

\[
(g,k,u,q).
\]

对每个 fibre：

1. 取 exact integral source-lattice isotropic basepoint；
2. 建立 (5.1) source-adapted quadratic parameterization；
3. 除 fixed coefficient content；
4. 研究 \((X,Y,N)\) 的 \(2/5\)-adic content。

得到 exact necessary residue ledger：

| \((g,k,u,q)\) | \(r_0\) | \(\min v_2(X\text{-coeff})\) | necessary \(m=a/b\pmod{2^e}\) | \(\min v_5(X\text{-coeff})\) | necessary \(m\pmod{5^e}\) |
|---|---:|---:|---|---:|---|
| \((5,1,11,9091)\) | 3 | 4 | \(0,3\pmod{16}\) | 5 | \(0,957\pmod{3125}\) |
| \((5,3,11,9091)\) | 1083 | 4 | \(0,11\pmod{16}\) | 5 | \(0,1727\pmod{3125}\) |
| \((5,4,11,9091)\) | 3083 | 4 | \(0,11\pmod{16}\) | 5 | \(0,2227\pmod{3125}\) |
| \((5,1,9091,11)\) | 3 | 4 | \(0,3\pmod{16}\) | 5 | \(0,1352\pmod{3125}\) |
| \((5,3,9091,11)\) | 1683 | 4 | \(0,3\pmod{16}\) | 6 | \(14722\pmod{15625}\) |

这里 “necessary” 的意思严格是：

若 ten-unit primitive ray 存在，则为了让 \(D\) 至少吸收 \(X\) 的最小 decimal depth，\(Y,N\) 必须同时达到相同 depth。

它不是 sufficient condition。

这已经说明：

\[
\boxed{
\text{band rational slope}
}
\]

不是任意 rational slope，而必须落入越来越精细的 decimal-content residue packet。

---

# 14. Real-Band Diagnostic

以下 endpoint 为高精度数值，仅用于解释 search geometry；所有 certificate PASS/FAIL 决策仍使用 exact integer polynomial inequalities。

| fibre | source-adapted real feasible \(m=a/b\) interval | approximate width |
|---|---|---:|
| \((5,1,11,9091)\) | \((19654513.3264717870,\ 19654513.3280774125)\) | \(1.606\times10^{-3}\) |
| \((5,3,11,9091)\) | \((19762840.5289314912,\ 19762840.5289361459)\) | \(4.655\times10^{-6}\) |
| \((5,4,11,9091)\) | \((19762848.8955229631,\ 19762848.8955246104)\) | \(1.647\times10^{-6}\) |
| \((5,1,9091,11)\) | \((30.0547405150834,\ 30.0547405172120)\) | \(2.129\times10^{-9}\) |
| \((5,3,9091,11)\) | \((30.2454020605150,\ 30.2454020608925)\) | \(3.775\times10^{-10}\) |

因此 M4/Farey 机制确实出现，但必须与 (PCS) 一起使用。

单纯 “interval 很窄” 仍不足以证明 height theorem。

---

# 15. Small-Denominator Counterexample Guillotine

对上述五个 \(g=5\) live fibres，使用 source-adapted complete parameterization，exact 枚举：

\[
\gcd(a,b)=1,
\qquad
|a|\le300,
\qquad
0\le b\le300,
\]

并 quotient：

\[
(a,b)\sim(-a,-b).
\]

每个参数都 exact 执行：

1. conic identity；
2. source-lattice identity；
3. source-basis primitive reduction；
4. positive orientation；
5. derived positivity；
6. radial decade band。

结果：

```text
g=5,k=1,u=11,q=9091   BAND_POSITIVE_SMALL_PARAMS = 0
g=5,k=3,u=11,q=9091   BAND_POSITIVE_SMALL_PARAMS = 0
g=5,k=4,u=11,q=9091   BAND_POSITIVE_SMALL_PARAMS = 0
g=5,k=1,u=9091,q=11   BAND_POSITIVE_SMALL_PARAMS = 0
g=5,k=3,u=9091,q=11   BAND_POSITIVE_SMALL_PARAMS = 0
```

所以：

```text
SMALL_HEIGHT_COUNTERMODEL = NOT_FOUND
```

但这只是 finite exact guillotine：

\[
\boxed{
B=300.
}
\]

不得外推为 uniform theorem。

---

# 16. Two Exact Ten-Unit Band Rays Beyond Small Denominator

进一步沿 (PCS) 的 \(2/5\)-adic residue classes搜索，找到两个 exact positive band rays，它们已经通过：

- exact root；
- source lattice；
- positive branch；
- decade band；
- \(\gcd(cz\lambda,10)=1\)；
- derived ten-unit package；
- regularity；

但在 common-\(V\) 的

\[
\gcd(C_1,u)=1
\]

处失败。

## Candidate R3-TU1

\[
(g,k,u,q)=(5,1,11,9091),
\]

parameter：

\[
\boxed{
(a,b)
=
(224277651577,\ 11411).
}
\]

source primitive point：

\[
c=
7552484809409187343652490186865568828046248860489,
\]

\[
z=
19602285445098332635298259690944933864745567,
\]

\[
\lambda=
31707187878848240450045098563697628215480153798681.
\]

\[
C_1=
36668199133975529291004220769104240806137852635963,
\]

\[
C_2=
1585533101093028433811158935459179318857052753657841247.
\]

并且：

\[
\gcd(C_1,11)=11.
\]

full block gcd 也是：

\[
\boxed{11}.
\]

所以它不是 full primitive/common-\(V\) state。

---

## Candidate R3-TU2

\[
(g,k,u,q)=(5,3,11,9091),
\]

\[
\boxed{
(a,b)
=
(5982784950483,\ 302729).
}
\]

source primitive point：

\[
c=
25497201999198914781027313724524295510593,
\]

\[
z=
5157086659422659922510573993232659,
\]

\[
\lambda=
64326917455289932167507738750666510531303697.
\]

\[
C_1=
739760089886037572598031924461878280614944,
\]

\[
C_2=
3216346459200142589950426901161541190623981593639.
\]

同样：

\[
\gcd(C_1,11)=11,
\]

full block gcd：

\[
\boxed{11}.
\]

这两个 candidate 的作用不是提供反例，而是定位信息差：

\[
\boxed{
\text{decimal content synchronization}
\text{ 可以穿过，}
\quad
\text{但 full primitive/common-}V
\text{ 仍继续筛选。}
}
\]

所以不能把 (PCS) 单独宣布成 closure theorem。

---

# 17. Strongest Fixed-Fibre Height Theorem

R2 已经 exact 证明：

\[
G=10^4,
\qquad
G+1=10001=73\cdot137,
\]

在 inherited \(\gcd(A,10)=1\) 的 central regular branch 中唯一 live orientation：

\[
(u,q)=(73,137).
\]

并且 \(k\in\{1,2\}\)。

对这两个 fibre，R2 完整 exact finite reduction证明：

\[
\boxed{
c<G,
\qquad
C_2<G^2K
}
\]

下没有 positive exact root。

因此：

\[
\boxed{
(g,u,q)=(4,73,137),
\quad
k\in\{1,2\}
\Longrightarrow
\mathfrak H_{\rm rad}\ge1
}
\tag{17.1}
\]

对所有 exact positive roots成立。

这比本轮只在 band 内需要的 theorem 更强。

所以：

```text
FIXED_FIBRE_HEIGHT_THEOREM = PROVED
```

但仍然：

```text
UNIFORM_HEIGHT_THEOREM = OPEN
```

---

# 18. Strongest Full-Deep Band Countermodel

当前最强 full-deep band witness 仍为 R2-CM1：

\[
(g,k,u,q)=(4,1,73,137),
\]

\[
c=
55572391133361773812119871611530969901,
\]

\[
z=
18294059737282238636057102641763401,
\]

\[
\lambda=
169133142022529638483244734153511450709.
\]

\[
C_2=
853834851609252373166605291894452306120447.
\]

它通过：

- exact root；
- square reconstruction；
- ten-unit；
- regular；
- common-\(V\)；
- full primitive；
- source lattice；
- radial decade band。

但：

\[
c\gg G,
\qquad
C_2\gg G^2K.
\]

其：

\[
\boxed{
\mathfrak H_{\rm rad}
=
\frac{
55572391133361773812119871611530969901
}{
10000
}.
}
\tag{18.1}
\]

数值仅供阅读：

\[
\mathfrak H_{\rm rad}
\approx
5.5572391\times10^{33}.
\]

在当前 R1–R3 已 exact 验证的 **full-deep decade-band witness corpus** 中，这是目前记录的最小 \(\mathfrak H_{\rm rad}\)。

这不是 global minimum theorem。

---

# 19. R2-CM1 Source-Parameter Reconstruction

对同一 \(g=4,k=1,u=73\) fibre：

\[
r_0=9.
\]

可取 source-lattice isotropic basepoint：

\[
p=
(38079018077000,\,
8172514980,\,
-1119479382000).
\]

在 \(y(a,b)=ae_1+be_2\) chart 中，R2-CM1 对应 reduced parameter：

\[
\boxed{
a=
3871298103487563077046544629366541,
}
\]

\[
\boxed{
b=
835381452246978018750354829941,
}
\]

\[
\gcd(a,b)=1.
\]

其 raw source-basis quadratic vector 的 content 为：

\[
\boxed{
D_\Lambda
=
243593191253934894536696190040271162280000000.
}
\]

除去该 content 后 exact 恢复 R2-CM1。

这直接展示：

\[
\boxed{
\text{巨大 numerator growth}
\quad\text{和}\quad
\text{巨大 content cancellation}
}
\]

必须同时审计。

只看 quadratic numerator 大小会严重高估 primitive height。

---

# 20. Countermodel Ledger

对 R2-CM1：

```text
EXACT_ROOT = PASS
SQUARE = PASS
PRIMITIVE = PASS
COMMON_V = PASS
REGULAR = PASS

RHO_IN_DECADE_BAND = PASS

SOURCE_LATTICE_PARAMETER = PASS
PRIMITIVE_PARAMETER = PASS

c < G = FAIL
C2 < G^2 K = FAIL

REAL_COMMON_U = PASS
INTEGER_COMMON_U = FAIL
COPRIME_COMMON_U = FAIL

FULL_SOURCE_LIFT = FAIL
```

first failure 仍是：

\[
\boxed{
\textbf{absolute primitive radial height}.
}
\]

本轮没有把 first failure 推进到 integer-spacing。

---

# 21. Why a Pure Denominator Theorem Is Not Yet Enough

即使证明：

\[
\max(|a|,|b|)\ge B,
\]

仍不能直接推出：

\[
c_0\ge G.
\]

因为：

\[
c_0
=
\frac{|f_1(a,b)|}{D_\Lambda(a,b)}.
\]

必须同时控制：

\[
D_\Lambda(a,b).
\]

本轮已经证明 fixed-fibre：

\[
D_\Lambda\mid\mathfrak D_{g,k,u},
\]

但 \(\mathfrak D_{g,k,u}\) 仍可能过大。

因此 denominator explosion 的合法终局形式必须是：

\[
\boxed{
\frac{
\text{quadratic parameter height}
}{
\text{primitive content}
}
\gtrsim
G.
}
\]

而不是：

\[
|a|+|b|\text{ 大}.
\]

---

# 22. Uniformity Audit

## 22.1 What is genuinely moving

R3 中 moving datum 实际进入：

1. source lattice modulus
   \[
   2K;
   \]

2. residue
   \[
   r_0\equiv-A^{-1}B\pmod{2K};
   \]

3. chord coordinate quadratics \(f_i\) 的 coefficients；

4. decimal-content valuations at \(2,5\)；

5. radial band endpoints
   \[
   K/5-2A/G,
   \qquad
   20K-2A/G;
   \]

6. height denominators
   \[
   G,
   \qquad
   G^2K.
   \]

所以：

```text
MOVING_INFORMATION_ACTIVATED = YES
```

---

## 22.2 What is not yet uniform

尚未证明以下任一 statement：

\[
v_5(f_1\text{-coeff})
\ge c g
\]

以适用于所有 live fibres；

也未证明：

\[
\text{PCS residue modulus}
\gg G^\theta
\]

对统一 \(\theta>0\) 成立；

更没有证明：

\[
\frac{|f_1(a,b)|}{D_\Lambda(a,b)}
\ge G
\]

对所有 legal band parameters 成立。

因此不能把 \(g=5\) 的 residue explosion 偷升格为 all-\(g\) theorem。

---

# 23. Status of the Five Candidate Mechanisms

## M1 — Lattice determinant

\[
\boxed{\text{INSUFFICIENT ALONE}}
\]

finite-index lattice 不会自动消灭 rational rays。

---

## M2 — Congruence denominator

\[
\boxed{\text{ACTIVATED}}
\]

但真正 congruence 来自 primitive content synchronization，而不是 lattice membership 本身。

---

## M3 — Content bound

\[
\boxed{\text{PROVED FIXED-FIBRE}}
\]

通过 Bézout/resultant constant。

uniformly small bound 未证明。

---

## M4 — Farey gap

\[
\boxed{\text{PLAUSIBLE SUPPORTING MECHANISM}}
\]

\(g=5\) source-adapted band 可极窄，但必须与 PCS residue classes结合。

---

## M5 — Direct height transfer

\[
\boxed{\text{NOT YET PROVED}}
\]

这正是 R4 唯一任务。

---

# 24. Main Answer to R3

本轮最终核心问题是：

> 在 \(\rho\in(1/10,10)\) 的真正 source-compatible rational root rays 中，primitive representative 是否必然满足
> \[
> c\ge G
> \quad\lor\quad
> C_2\ge G^2K?
> \]

当前严格答案：

\[
\boxed{
\textbf{UNRESOLVED GLOBALLY.}
}
\]

但这不是“若干方向仍需研究”的开放式结束。

当前唯一尚未闭合的 theorem interface 已经压成：

\[
\boxed{
\textbf{Two-Prime Primitive-Content Height Transfer}.
}
\]

即：

\[
\boxed{
\begin{gathered}
[a:b]\in\mathscr M_{g,k,u},
\\
\gcd(a,b)=1,
\\
v_p(f_1)=v_p(f_2)=
\min(v_p(f_1),v_p(f_2),v_p(f_3))
\quad(p=2,5),
\\
\text{full primitive/common-}V/\text{regular predicates}
\\
\Longrightarrow
\mathfrak H_{\rm rad}(a,b)\ge1.
\end{gathered}
}
\tag{R4-TPCHT}
\]

R4 只允许证明或 falsify 这一 theorem。

---

# 25. R4 Unique Interface

正式冻结：

## R4 Primary Theorem — Uniform Two-Prime Primitive-Content Height Transfer

对每个 live outer fibre，取 source-adapted complete quadratic parameterization：

\[
(f_1,f_2,f_3).
\]

证明：

\[
\boxed{
\begin{aligned}
&
[a:b]\in\mathscr M_{g,k,u},
\\
&
\gcd(a,b)=1,
\\
&
\text{PCS}_{2},
\quad
\text{PCS}_{5},
\\
&
\text{common-}V,
\quad
\text{full primitive},
\quad
\text{regular}
\\
&\Longrightarrow
\\
&
\max
\left(
\frac{|f_1|}{GD_\Lambda},
\frac{
|Af_1+H(r_0f_2+2Kf_3)|
}{
G^2KD_\Lambda
}
\right)
\ge1.
\end{aligned}
}
\tag{R4}
\]

攻击顺序固定为：

\[
\boxed{
\text{PCS residue modulus}
\to
\text{Farey / congruence spacing}
\to
\text{uniform content upper bound}
\to
\text{height transfer}.
}
\]

如果这一 theorem 被 exact Level-I counterexample 杀死，才允许自动转入：

\[
\boxed{
\text{Integer Radial Extinction}.
}
\]

在此之前不打开 integer-spacing / coprime-\(U\) campaign。

---

# 26. Terminal Ledger

```text
J2_STATUS =
OPEN

BAND_CONDITIONED_PRIMITIVE_HEIGHT =
OPEN

RATIONAL_CONIC_PARAMETERIZATION =
COMPLETE

SOURCE_LATTICE_PULLBACK =
PARTIAL

CONTENT_BOUND =
PROVED

DENOMINATOR_EXPLOSION =
PLAUSIBLE

FIXED_FIBRE_HEIGHT_THEOREM =
PROVED

UNIFORM_HEIGHT_THEOREM =
OPEN

SMALL_HEIGHT_COUNTERMODEL =
NOT_FOUND

INTEGER_COMMON_U_CANDIDATE =
NOT_REACHED

FULL_COMMON_U_COUNTERMODEL =
NOT_FOUND

MOVING_INFORMATION_ACTIVATED =
YES

MOVING_HEIGHT_MECHANISM =
DECIMAL_PRIMITIVE_CONTENT_SYNCHRONIZATION:
v_p(X)=v_p(Y)=min(v_p(X),v_p(Y),v_p(N))
for p=2,5,
combined with the moving source-adapted slope band.

R3_TERMINAL_VERDICT =
UNIFORMIZATION_REQUIRED
```

---

# 27. Mathematical Object Ledger

本轮已得到：

1. exact projective conic — (2.1), (3.1)；
2. affine chart — \(s=z/c,\ t=\lambda/c\)；
3. complete rational chord parameterization — (5.1)；
4. transverse-plane / degenerate-fibre exception audit；
5. source-lattice primitive representative — (6.2), (6.3)；
6. fixed-fibre global content bound — (8.1)；
7. slope variable — \(m=a/b\)；
8. radial feasible set — \(\mathscr M_{g,k,u}\)；
9. exact source lattice — (4.2)；
10. primitive radial height — (10.1)；
11. small-denominator exact search ledger；
12. strongest fixed-fibre theorem — (17.1)；
13. uniformity audit；
14. strongest full-deep countermodel — R2-CM1；
15. R4 unique theorem — (R4).

---

# 28. Computation Certificate Scope

附带：

```text
85_phaseII_R3_primitive_height_certificate.py
```

以及运行输出：

```text
85_phaseII_R3_primitive_height_certificate.txt
```

certificate 只承担以下有限、deterministic 责任：

1. 验证五个 \(g=5\) source-lattice basepoints exact isotropic；
2. 验证 source-adapted chord formula恒落在 conic 与 source lattice；
3. exact 扫描 \(|a|,|b|\le300\)；
4. exact 输出 \(2/5\)-content necessary slope residue classes；
5. 不使用 floating-point 进行任何 PASS/FAIL gate 判决。

它不承担：

- all-\(g\) completeness；
- uniform height proof；
- minimum denominator theorem；
- global absence theorem。

---

# 29. Provenance / Frozen Inputs

本轮主要承接：

- `85_phaseII_R1_moving_square_exactization.md`
- `85_phaseII_R2_radial_extinction.md`
- `85_phaseII_R2_counterexample_certificate.py`
- `J2-65-R20-Semantic-Conductor-Ruling-Report.md`
- `J2-65-R13-Radial-Lattice-Ray-Report.md`
- `85_R6_live_N0_split_base_scan_certificate.txt`

---

# 30. Final Verdict

R3 没有证明：

\[
J=2\Rightarrow\varnothing.
\]

也没有杀死 primitive-height architecture。

但 R3 已经把“为什么 primitive ray 可能变得过高”从 vague height intuition 压成一个 exact mechanism：

\[
\boxed{
\text{source-adapted quadratic ray}
\to
\text{lattice content}
\to
2/5\text{-adic equal-depth synchronization}
\to
\text{high-modulus slope packet}
\to
\text{Archimedean height}.
}
\]

因此第二个八五计划·第三轮的终端判断是：

\[
\boxed{
\textbf{UNIFORMIZATION REQUIRED}.
}
\]

而 R4 的唯一主接口是：

\[
\boxed{
\textbf{Uniform Two-Prime Primitive-Content Height Transfer}.
}
\]
