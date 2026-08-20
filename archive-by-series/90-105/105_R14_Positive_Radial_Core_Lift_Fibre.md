# 105-R14 — Positive-Digit-Box Radial Core × Exact Post-PSDG Lift Fibre × Transverse Certificate Elimination × Lift-or-Empty

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R14  
**Architecture:** Positive-Digit-Box Radial Core Liftability  
**Terminal class:** **STRUCTURAL SUCCESS / OUTCOME C**

---

## 1. Executive Verdict

R14 没有证明
\[
\forall \mathbf r\in\mathscr B_+,\qquad
\operatorname{Lift}_{\rm post}(\mathbf r)=\varnothing,
\]
也没有构造出
\[
\mathbf r\in\mathscr B_+,\qquad
\operatorname{Lift}_{\rm post}(\mathbf r)\neq\varnothing.
\]

但本轮完成了四个真正的新压缩。

### 1.1 Sphere 被 CF 完全吸收

令
\[
c:=h\varepsilon.
\]
R13 的 Full Smith-radial cancellation 可重写为
\[
P_2=WM_r,\qquad P_3=AN_r,
\]
于是
\[
\boxed{
c^2X_0Y_0=W^2M_r^2+A^2N_r^2.
}
\tag{CF}
\]
配合
\[
P_1=\frac{c(X_0-Y_0)}2,\qquad
Q_0=\frac{c(X_0+Y_0)}2
\]
后，sphere 不再是独立方程。

因此：
```text
SPHERE_ABSORBED_INTO_CF=YES
```

### 1.2 Smith transverse data 压成 \((A,W,z)\)

从 frozen Smith chart 定义
\[
\boxed{
A:=\frac{g_3}{u_0}=\alpha t,\qquad
W:=\frac{g_2}{u_0}=v,\qquad
z:=\frac{V}{u_0AW}=s\beta.
}
\tag{AWZ}
\]
于是
\[
\boxed{
P_2=WM_r,\qquad P_3=AN_r,
}
\]
\[
\boxed{
V=zu_0AW,\qquad b_2=zA,\qquad b_3=zW.
}
\]
原来的
\[
(s,\alpha,\beta,\gamma,t,v_0)
\]
不再需要全部作为 independent transverse coordinates。

### 1.3 Raw master 精确塌成一个 forced-\(g_1\) equation

令
\[
T_3:=Q_0-P_3
\]
以及
\[
\boxed{
\Omega
:=
WT_3-AY(P_2-GQ_0).
}
\]
利用
\[
P_2=WM_r,\qquad P_3=AN_r
\]
还可写成
\[
\boxed{
\Omega
=
Q_0(W+AYG)-AW(N_r+YM_r).
}
\tag{OMEGA}
\]

将
\[
b_1=\frac{V}{g_1}
=\frac{zu_0AW}{g_1},
\quad
b_2=zA,
\quad
b_3=zW
\]
代入 frozen raw master：
\[
b_1XYGD+b_2Y(P_2-GQ_0)-b_3T_3=0,
\]
除以 \(z>0\)，得到
\[
\boxed{
g_1\Omega=u_0AWXYGD.
}
\tag{GM}
\]

所以每个 fixed finite shape 都强制
\[
\boxed{
g_1^*
=
\frac{u_0AWXYGD}{\Omega}.
}
\tag{G1*}
\]
它必须是正整数，并且必须与 source gcd shell 相等：
\[
\boxed{
\gcd(zu_0AW,P_1)=g_1^*.
}
\tag{G1}
\]

这是 R14 最重要的新 transverse equation。

### 1.4 Fixed-core lift fibre 是 finite

固定
\[
\mathbf r=(u_0,M_r,N_r,n_2,n_3).
\]

由
\[
g\ge0,\qquad k\ge1,\qquad
m_2=n_2-g-k\ge1
\]
可知 exponent chart \((g,k)\) 有限。

对 fixed chart，
\[
10^{m_2-1}\le zA<10^{m_2},
\qquad
10^{m_3-1}\le zW<10^{m_3}
\]
直接给出 \(A,W,z\) 的有限上界。

固定 \(A,W\) 后，
\[
N:=W^2M_r^2+A^2N_r^2
\]
固定，而 CF 只允许有限个整数因子分解。

所以：
\[
\boxed{
|\operatorname{Lift}_{\rm post}(\mathbf r)|<\infty
}
\]
对每个 fixed core 都成立。

没有证明 uniform bound。

因此 R14 的真正 terminal reduction 是：

\[
\boxed{
\textbf{finite transverse shape}
\quad+\quad
\textbf{one exact denominator-scale selector }z.
}
\]

---

## 2. Frozen R1–R13 State

R1–R13 全部永久冻结。

- R1：`SOURCE_AFFINE_SECTION_LOSS`。
- R2：canonical absolute source section 已恢复。
- R3：valuation atlas `SEMANTICALLY_SATURATED`。
- R4–R6：fixed incidence / moving-base / sphere×master rational lift / complementary discriminant / exceptional square locus frozen。
- R7–R7D：orientation / PSDG / determinant packet / source \(g_1\)-firewall frozen；`PSDG_WITNESS_CONSTRUCTED=YES`。
- R8：post-PSDG source fibre rank one；\(U\) 是唯一 radial variable。
- R9–R11：successor / endpoint quotient / DES residue-coset chain frozen。
- R12：`LOCAL_DES_NUMERATOR_INTERFACE_SATURATED=YES`，`CONTINUE_DES_ENDPOINT_CHAIN=NO`。
- R13：radial image factors through \((u_0,M_r,N_r,n_2,n_3)\)。

R14 没有返回 endpoint residue、\(\Xi_{i,p}\)、DES quotient、normalized numerator、generic PSDG、packet allocation 或 valuation atlas。

---

## 3. R13 Radial-Core Factorization

Frozen identities：
\[
P_2=vM_r,\qquad
P_3=\alpha tN_r,
\]
\[
g_2=u_0v,\qquad
g_3=u_0\alpha t,
\]
\[
\boxed{
C_2=\frac{M_r}{u_0},
\qquad
C_3=\frac{N_r}{u_0}.
}
\]

所以 radial geometry 只读取
\[
\boxed{
\mathbf r=(u_0,M_r,N_r,n_2,n_3).
}
\]

---

## 4. Definition of Positive Radial Core

定义
\[
\boxed{
\mathscr B_+
=
\left\{
\mathbf r:
\exists U\in\mathbf Z_{>0}
\text{ 满足 }
u_0 10^{n_2-1}\le UM_r<u_0 10^{n_2},
\ 
u_0 10^{n_3-1}\le UN_r<u_0 10^{n_3}
\right\}.
}
\]

两式交叉给出：
\[
\boxed{
10^{n_3-n_2-1}
<
\frac{N_r}{M_r}
<
10^{n_3-n_2+1}.
}
\tag{BOX-RATIO}
\]

这是 genuine radial information，但尚不能直接 kill transverse lift。

---

## 5. Definition of \(\operatorname{Lift}_{\rm post}\)

对 fixed
\[
\mathbf r\in\mathscr B_+,
\]
\[
\operatorname{Lift}_{\rm post}(\mathbf r)
\]
是所有能够恢复完整 frozen post-PSDG profile 的 transverse integer certificates。

其中必须通过：

- CF / primitive sphere；
- full master；
- Smith gcd dictionary；
- tail integrality；
- frozen PSDG/determinant-packet regression；
- source \(g_1\)-firewall；
- frozen source-completed cell predicates。

\(U\) 不属于 transverse fibre。

---

## 6. Radial / Transverse Variable Split

### Radial core
\[
(u_0,M_r,N_r,n_2,n_3).
\]

### R14 independent transverse variables
\[
\boxed{
(g,k;\ A,W;\ c,X_0,Y_0;\ z).
}
\]

### Derived variables
\[
m_2,m_3,G,K,X,Y,
\]
\[
P_1,P_2,P_3,Q_0,
\]
\[
V,g_1,g_2,g_3,b_1,b_2,b_3,
\]
\[
D,T_3,\Omega,H,K_3,R,\ldots
\]

---

## 7. Dependency Graph

\[
\mathbf r+(g,k)
\longrightarrow
(m_2,m_3,G,K,X,Y).
\]

\[
\mathbf r+(A,W)
\longrightarrow
(P_2,P_3)
\longrightarrow
N=P_2^2+P_3^2.
\]

\[
N+(c,X_0,Y_0)
\longrightarrow
(P_1,Q_0)
\longrightarrow
(D,T_3,\Omega,g_1^*).
\]

\[
z+(u_0,A,W,g_1^*)
\longrightarrow
(V,b_1,b_2,b_3)
\longrightarrow
(H,K_3,R).
\]

最后只做 frozen source predicates regression。

详见：
`105_R14_Transverse_Variable_Graph.csv`。

---

## 8. Independent Transverse Coordinates

R13 的 reconstruction certificate 中曾保留
\[
s,\alpha,\beta,\gamma,t,v_0.
\]

R14 使用
\[
A=\alpha t,\qquad
W=\gamma v_0,\qquad
z=s\beta
\]
进行 source-native quotient。

因为 full liftability 所需的
\[
P_2,P_3,V,b_2,b_3,g_2,g_3
\]
全部可由 \((A,W,z)\) 精确恢复，所以这些旧变量无需全部并列存在。

这不是 relaxed quotient；最终 full witness 仍需做 Smith chart regression。

---

## 9. Redundancy Audit

| frozen equation / predicate | R14 status |
|---|---|
| sphere | **absorbed into CF** |
| \(H=b_2Q_0-b_1XD\) | derived |
| \(K_3=b_3T_3/Y\) | derived after tail |
| \(b_2P_2=GH+K_3\) | equivalent to raw master |
| raw master | independent; collapses to (GM) |
| source \(g_1\)-firewall | canonicalized into exact gcd shell |
| generic PSDG allocation | frozen regression only |
| D-ratio | valid but already contained in R7C |
| endpoint/DES quotient | retired |

---

## 10. Minimal Lift System

对 fixed \(\mathbf r\in\mathscr B_+\)，minimal system \(\mathcal L_{\mathbf r}\) 取：

1. finite exponent chart：
   \[
   g\ge0,\ k\ge1,\ m_2=n_2-g-k\ge1,\ m_3=n_3+g;
   \]
2. denominator windows：
   \[
   10^{m_2-1}\le zA<10^{m_2},
   \quad
   10^{m_3-1}\le zW<10^{m_3};
   \]
3. CF；
4. factor coprimality/parity；
5. primitive predicate；
6. \(D>0\) 与 \(T_3>0\)；
7. master-forced \(g_1^*\in\mathbf Z_{>0}\)；
8. tail \(z\)-divisibility；
9. Smith \(g_2/g_3\) gcd shells；
10. canonical Smith reconstruction predicate（含 frozen pairwise gcd，特别是 \(\gcd(A,W)=1\)）；
11. \(g_1\) exact gcd shell；
12. \(H\ne0\) 与 frozen source-cell predicate；
13. frozen PSDG/determinant regression。

详见：
`105_R14_Minimal_Lift_System.csv`。

---

## 11. Proof of Equivalence to Full Post-PSDG Lift

### Forward direction

任意 full post-PSDG lift 都带有 frozen R13 Smith data。

定义
\[
A=g_3/u_0,\qquad W=g_2/u_0,\qquad
z=V/(u_0AW).
\]

于是自动得到
\[
P_2=WM_r,\quad
P_3=AN_r,\quad
b_2=zA,\quad
b_3=zW.
\]

sphere factorization 给 CF。

raw master 经代入给 (GM)。

tail equation给 \(\lambda_z\mid z\)。

三个 gcd definitions 给 Smith + \(g_1\) shells。

因此 full lift 必然映到 \(\mathcal L_{\mathbf r}\)。

### Reverse direction

若 \(\mathcal L_{\mathbf r}\) 有解，恢复
\[
P_2=WM_r,\qquad P_3=AN_r,
\]
\[
P_1=\frac{c(X_0-Y_0)}2,\qquad
Q_0=\frac{c(X_0+Y_0)}2,
\]
\[
V=zu_0AW,
\]
\[
g_2=u_0W,\quad g_3=u_0A,\quad g_1=g_1^*,
\]
\[
b_i=V/g_i.
\]

Smith gcd predicates保证 \(g_i=\gcd(V,P_i)\) 精确成立；canonical Smith reconstruction predicate 再要求由 \((b_1,b_2,b_3)\) 恢复出的
\[
s,lpha,eta,u,t,v
\]
满足 frozen denominator Smith normal form 与 pairwise gcd。特别地
\[
\gcd(A,W)=1
\]
必须成立。该 regression 是 deterministic finite check，不重新引入连续/无界 transverse coordinate。

tail 使
\[
K_3=\frac{b_3T_3}{Y}\in\mathbf Z_{>0}.
\]

(GM) 与 raw master代数等价，从而 UDD/H package 精确恢复。

再通过 frozen cell / PSDG regression predicate，即得到 full post-PSDG lift。

所以：
\[
\boxed{
\mathcal F_{\mathbf r}\neq\varnothing
\iff
\operatorname{Lift}_{\rm post}(\mathbf r)\neq\varnothing.
}
\]

---

## 12. CF Equation

\[
\boxed{
c^2X_0Y_0=W^2M_r^2+A^2N_r^2.
}
\]

这是 R14 第一主方程。

---

## 13. Sphere Absorption Audit

因为
\[
Q_0^2-P_1^2
=
\frac{c^2}{4}
\left[
(X_0+Y_0)^2-(X_0-Y_0)^2
\right]
=
c^2X_0Y_0,
\]
CF 等价给出
\[
Q_0^2-P_1^2=P_2^2+P_3^2.
\]

因此：
\[
\boxed{
P_1^2+P_2^2+P_3^2=Q_0^2.
}
\]

所以：
```text
SPHERE_ABSORBED_INTO_CF=YES
```

---

## 14. Factor Coprimality / Parity

要求：
\[
\gcd(X_0,Y_0)=1,
\qquad
X_0>Y_0>0.
\]

integrality 精确为：

- \(X_0,Y_0\) 同为 odd：任意 \(c>0\)；
- 一奇一偶：必须 \(2\mid c\)。

二者不可能都偶。

---

## 15. Reconstruction of \(P_1,Q_0,P_2,P_3\)

\[
\boxed{
P_1=\frac{c(X_0-Y_0)}2,
\qquad
Q_0=\frac{c(X_0+Y_0)}2,
}
\]

\[
\boxed{
P_2=WM_r,
\qquad
P_3=AN_r.
}
\]

---

## 16. \(D>0\) Factor-Ratio Gate

\(k\ge1\) 给
\[
K=10^k\ge10>1.
\]

于是
\[
D>0
\iff
K(X_0-Y_0)>X_0+Y_0,
\]
即：
\[
\boxed{
\frac{X_0}{Y_0}>
\frac{K+1}{K-1}.
}
\tag{D-RATIO}
\]

但这条 ratio lower bound 已经是 R7C root-localization theorem 的同一内容。

所以：
```text
NEW_INFORMATION_BEYOND_R7C=NO
CF_FACTOR_RATIO_OBSTRUCTION=NO
```

R14 不重开 generic near-balanced divisor route。

---

## 17. Positive-Box Ratio Consequences

从 positive box：
\[
10^{n_3-n_2-1}
<
\frac{N_r}{M_r}
<
10^{n_3-n_2+1}.
\]

定义
\[
\theta=\frac{P_3}{P_2}
=
\frac{AN_r}{WM_r}.
\]

另一方面：
\[
\frac{A}{W}=\frac{b_2}{b_3}.
\]

所以 positive box 与 denominator windows 的结合只把 \(\theta\) 放入既有 source-scale corridor，没有得到新的 universal forbidden interval。

---

## 18. Tail Divisibility

Frozen tail equation：
\[
Y\mid b_3T_3.
\]

代
\[
b_3=zW
\]
得：
\[
Y\mid zWT_3.
\]

定义
\[
\boxed{
\lambda_z
:=
\frac{Y}{\gcd(Y,WT_3)}.
}
\]

于是 exact：
\[
\boxed{
\lambda_z\mid z.
}
\tag{TAIL-z}
\]

旧形式仍等价：
\[
\frac{Y}{\gcd(Y,b_3)}\mid T_3.
\]

在 frozen master package 中没有独立的 block-2 tail equation；Face-A endpoint transport 已在 R12 后退休。

```text
BLOCK2_TAIL_ANALOGUE=NO
```

---

## 19. Tail Divisibility × Size Collision

两块 denominator digit windows 等价于
\[
z\in[L_z,R_z),
\]
其中
\[
L_z=
\max\left(
\frac{10^{m_2-1}}A,
\frac{10^{m_3-1}}W
\right),
\]
\[
R_z=
\min\left(
\frac{10^{m_2}}A,
\frac{10^{m_3}}W
\right).
\]

tail-admissible 最小 multiple：
\[
\boxed{
z_{\rm tail}
=
\lambda_z
\left\lceil
\frac{L_z}{\lambda_z}
\right\rceil.
}
\]

因此：
\[
\boxed{
z_{\rm tail}\ge R_z
\Longrightarrow
\text{this finite shape is empty}.
}
\tag{TAIL-COLLISION}
\]

这是 exact size obstruction。

但是 positive core 本身不能控制
\[
\gcd(Y,b_3)
\]
到足够小，因为 \(z\) 可以吸收 \(2,5\)-parts。

所以 universal
\[
Q_0-P_3<
\frac{Y}{\gcd(Y,b_3)}
\]
没有被证明。

---

## 20. Master-Lift Elimination

raw master：
\[
b_1XYGD+b_2Y(P_2-GQ_0)-b_3T_3=0.
\]

代
\[
b_1=\frac{zu_0AW}{g_1},
\quad
b_2=zA,
\quad
b_3=zW.
\]

除 \(z\)：
\[
\frac{u_0AW}{g_1}XYGD
+
AY(P_2-GQ_0)
-
WT_3
=0.
\]

于是：
\[
\boxed{
g_1\Omega=u_0AWXYGD.
}
\]

这是 R14 第二主方程。

---

## 21. Elimination of \(H,K_3\)

tail 通过后：
\[
\boxed{
K_3=\frac{zWT_3}{Y}.
}
\]

master forced \(g_1\) 后：
\[
b_1=\frac{zu_0AW}{g_1}.
\]

所以
\[
\boxed{
H
=
zA
\left(
Q_0-\frac{u_0W}{g_1}XD
\right).
}
\]

同时：
\[
\boxed{
R=b_2Y-b_3=z(AY-W).
}
\]

所以：

- \(H\) 不再 independent；
- \(K_3\) 不再 independent；
- \(R\)-sign 只依赖 finite shape 的 \(AY-W\)，不依赖 \(z\) 大小。

---

## 22. Smith Transverse Predicates

由
\[
V=zu_0AW,\qquad
P_2=u_0WC_2,\qquad
P_3=u_0AC_3
\]
有：
\[
\gcd(V,P_2)
=
u_0W\gcd(zA,C_2),
\]
\[
\gcd(V,P_3)
=
u_0A\gcd(zW,C_3).
\]

所以 exact Smith shell：
\[
\boxed{
\gcd(zA,C_2)=1,
\qquad
\gcd(zW,C_3)=1.
}
\tag{S23}
\]

特别：
\[
\gcd(A,C_2)>1
\]
或
\[
\gcd(W,C_3)>1
\]
会立即 kill finite shape。

此外 frozen Smith pairwise gcd 给：
\[
oxed{\gcd(A,W)=1.}
\]
更完整地，候选 \((b_1,b_2,b_3)\) 必须经过 canonical Smith decomposition regression。这个 predicate 只检查 factor/gcd consistency，不增加新的 independent variable。

---

## 23. PSDG Reconstruction Predicate

PSDG 已被冻结。

R14 不重新研究：

- arbitrary divisor packet；
- orientation；
- split-prime distribution；
- determinant packet allocation。

只在 candidate 已经通过新的 lift system 后做 exact frozen PSDG/determinant regression。

因此 PSDG 是：
```text
FROZEN_EXACT_REGRESSION_PREDICATE
```
不是 R14 的新 independent equation。

---

## 24. Source \(g_1\) Firewall

master 先强制
\[
g_1=g_1^*.
\]

然后 source firewall 只剩：
\[
\boxed{
\gcd(zu_0AW,P_1)=g_1^*.
}
\tag{G1-SHELL}
\]

令
\[
e_M=v_p(u_0AW),
\qquad
e_P=v_p(P_1),
\qquad
e_*=v_p(g_1^*).
\]

则 exact：
\[
\min(v_p(z)+e_M,e_P)=e_*.
\]

若
\[
e_*<e_P,
\]
则必须：
\[
e_M\le e_*,
\qquad
v_p(z)=e_*-e_M.
\]

若
\[
e_*=e_P,
\]
则：
\[
v_p(z)\ge\max(0,e_P-e_M).
\]

所以 \(g_1\)-firewall 已经变成一个 exact one-dimensional valuation shell。

---

## 25. Primitive Predicate

必须保留：
\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

CF 本身不推出 primitive。

---

## 26. Fixed-Core Fibre Dimension

对每个 fixed core：
\[
\boxed{
\operatorname{Lift}_{\rm post}(\mathbf r)
\text{ 是 finite discrete set}.
}
\]

因此 semantic dimension：
```text
POSITIVE_CORE_LIFT_FIBRE_DIMENSION=0__FINITE_DISCRETE
```

这不等同于 relaxed algebraic envelope 的 ordinary dimension。

---

## 27. Finite-Fibre Audit

证明不依赖 solver。

### Exponent charts finite

\[
g+k\le n_2-1.
\]

### \(A,W,z\) finite

\[
zA<10^{m_2},
\qquad
zW<10^{m_3}.
\]

### CF finite

固定 \(A,W\) 后
\[
W^2M_r^2+A^2N_r^2
\]
是 fixed positive integer。

其 factorization 只有有限个。

因此 entire fixed-core lift fibre finite。

没有 uniform
\[
|\operatorname{Lift}_{\rm post}(\mathbf r)|\le C
\]
theorem。

---

## 28. \(U=1\) Positive-Core Lift Search

Discovery scope：
\[
u_0=1,\qquad n_2=2,\qquad n_3=1.
\]

由 exponent constraints 唯一：
\[
g=0,\qquad k=1,\qquad
m_2=m_3=1.
\]

\(U=1\) 时：
\[
C_2=10,\ldots,99,
\]
\[
C_3=1,\ldots,9.
\]

共：
\[
90\times9=810
\]
个 positive cores。

对每个 core，穷尽：

- \(b_2,b_3\in\{1,\ldots,9\}\)；
- 每个 \(z\mid\gcd(b_2,b_3)\)；
- exact \(A=b_2/z,W=b_3/z\)；
- exact \(g_2/g_3\) Smith shell；
- 全部 CF factor pairs；
- primitive；
- \(D,T_3>0\)；
- tail；
- master / forced-\(g_1\)。

无 master pass。

---

## 29. \(U=2,3\) Discovery Search

同一 exact chamber：

### \(U=2\)
\[
C_2=5,\ldots,49,
\quad
C_3=1,\ldots,4.
\]
共：
\[
45\times4=180.
\]

### \(U=3\)
\[
C_2=4,\ldots,33,
\quad
C_3=1,\ldots,3.
\]
共：
\[
30\times3=90.
\]

总计：
\[
\boxed{1080}
\]
个 prescribed-\(U\) positive-core rows。

这对该 bounded chamber 的 **必要 transverse over-approximation** 是 complete enumeration；不是 global extinction theorem。搜索故意没有先用完整 canonical Smith reconstruction/pairwise-gcd 去缩小集合，因此枚举域比真正 full lift fibre 更大。即便这个更大的集合也没有任何 master pass，所以 bounded chamber 的 no-hit 结论保持严格有效。

---

## 30. First-Failure Statistics

core-level first failure：

```text
POSITIVE_CORES_TESTED=1080

FAIL_CF=0
FAIL_PRIMITIVE=120
FAIL_D_RATIO=0
FAIL_TAIL=378
FAIL_MASTER=582

FULL_LIFT_COUNT=0
```

对所有已经通过 tail 的 assignments：

```text
TAIL_SURVIVING_ASSIGNMENTS=18581

G1STAR_NONINTEGRAL=18449
G1_GCD_SHELL_MISMATCH=132
MASTER_PASS=0
```

这不是概率推断。

它只用于定位最可能值得 theoremize 的 exact transverse interface。

---

## 31. Minimal UNSAT Cores

### 31.1 \(g_1^*\) nonintegral

代表点：

`U=1, C2=10, C3=1, b2=1, b3=1, z=1, A=1, W=1, P1=50, P2=10, P3=1, Q0=51, D=449, T3=50, Omega=460, Nmaster=44900, gcd(V,P1)=1`

在该 fixed shape 上：
\[
g_1^*=\frac{N_{\rm master}}{\Omega}
\notin\mathbf Z.
\]

所以：
\[
\{\mathrm{CF},D>0,T_3>0,\mathrm{tail},\mathrm{master}\}
\]
已经形成 exact UNSAT subset。

### 31.2 Integer \(g_1^*\) but gcd shell mismatch

代表点：

`U=1, C2=11, C3=3, b2=1, b3=2, z=1, A=1, W=2, P1=6, P2=22, P3=3, Q0=23, D=37, T3=20, Omega=50, Nmaster=7400, gcd(V,P1)=2, g1*=148`

其中：
\[
g_1^*=148,
\qquad
\gcd(V,P_1)=2.
\]

所以：
\[
\{\mathrm{master},\mathrm{source}\ g_1\text{-shell}\}
\]
直接矛盾。

---

## 32. CF/Ratio Obstruction Attempt

D-RATIO exact 成立。

但它没有比 R7C 多提供新的 factor annulus。

positive box 也没有把它推进成 impossible ratio。

所以：
```text
CF_FACTOR_RATIO_OBSTRUCTION=NO
NEW_INFORMATION_BEYOND_R7C=NO
```

---

## 33. Tail Obstruction Attempt

R14 得到的新 theorem 是：
\[
z_{\rm tail}\ge R_z
\Longrightarrow
\text{finite shape empty}.
\]

这是 exact、source-specific、依赖 positive-core/exponent shape 的 obstruction。

但不是 universal。

---

## 34. Radial-Core-Induced GCD Obstruction

若 finite shape 已经满足 shape-level
\[
\gcd(A,C_2)=\gcd(W,C_3)=1,
\]
则 Smith 进一步要求
\[
\gcd(z,C_2C_3)=1.
\]

tail 同时要求
\[
\lambda_z\mid z.
\]

所以：
\[
\boxed{
\gcd(\lambda_z,C_2C_3)>1
\Longrightarrow
\text{finite shape has no lift}.
}
\tag{RAD-GCD}
\]

这是 R14 合法的新：
\[
\boxed{
\text{radial-core-induced transverse gcd obstruction}.
}
\]

但它不是 universal，因为 \(C_2C_3\) 可以与 \(10\) 互素。

---

## 35. Positive-Core Construct Lane

构造顺序应改成：

1. 固定 \(\mathbf r\in\mathscr B_+\)；
2. 枚举 finite exponent chart \((g,k)\)；
3. 选有限 \(A,W\)；
4. 解 CF；
5. 检查 primitive / \(D,T_3\)；
6. 计算 \(\Omega\)；
7. 要求 \(g_1^*\in\mathbf Z_{>0}\)；
8. 再解 single \(z\)-selector；
9. 最后 frozen PSDG/cell regression。

这比从原始 \(s,\alpha,\beta,\gamma,t,v_0,h,\varepsilon,\ldots\) brute force 明显更低维。

---

## 36. First Full Transverse Lift

没有找到。

```text
FULL_TRANSVERSE_LIFT_FOUND=NO
```

bounded exact chamber
\[
u_0=1,\ n_2=2,\ n_3=1,\ U=1,2,3
\]
在 master/\(g_1\) necessary subsystem 已经全部 empty。

---

## 37. Exact Plain \(U\) Recovery

由于没有 new full transverse lift，本轮没有激活 downstream plain-\(U\) recovery。

未来若有 lifted core，则：
\[
U_{\rm plain}
=
\min
\left\{
U>0:
10^{n_2-1}\le UC_2<10^{n_2},
\ 
10^{n_3-1}\le UC_3<10^{n_3}
\right\}.
\]

---

## 38. Source Selector Audit

未到达新的 lifted core。

```text
Q1_PROGRESSION_ACTIVE=NO
Q1_PROGRESSION_PASS=NOT_REACHED
COPRIMALITY_PASS=NOT_REACHED

SOURCE_INTEGER_U_FOUND=NO
```

---

## 39. Downstream Word/Cut Audit

```text
DIGIT_SYNCHRONIZATION=NOT_REACHED
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED
```

---

## 40. New First-Failure Gate

对一个已经通过 finite shape checks 的
\[
\sigma=(g,k,A,W,c,X_0,Y_0),
\]
定义：
\[
\boxed{
\mathcal Z(\mathbf r;\sigma)
=
\left\{
z\in\mathbf Z_{>0}:
\begin{array}{l}
L_z\le z<R_z,\\
\lambda_z\mid z,\\
\gcd(zA,C_2)=1,\\
\gcd(zW,C_3)=1,\\
\gcd(zu_0AW,P_1)=g_1^*
\end{array}
\right\}.
}
\tag{Z-SEL}
\]

其中 \(g_1^*\) 已由 master 唯一强制。

因此新的唯一 gate 是：
\[
\boxed{
\mathcal Z(\mathbf r;\sigma)\neq\varnothing\ ?
}
\]

这不是 endpoint、DES quotient、generic PSDG 或 radial image 的重命名。

---

## 41. Failed / Falsified Routes

1. positive box 单独给 universal tail-size kill：**NO**。
2. D-RATIO 是 R14 新 obstruction：**NO，R7C 已有**。
3. generic near-balanced divisor spacing：继续退休。
4. Smith variables 必须全部保留：**NO，压成 \(A,W,z\)**。
5. sphere 必须独立保留：**NO，absorbed into CF**。
6. \(H,K_3\) 是 independent transverse variables：**NO**。
7. fixed-core fibre positive-dimensional：**NO，finite theorem**。
8. \(U=1,2,3\) bounded no-hit 等于 global theorem：**NO**。
9. R12 DES interface 可以帮助决定 \(z\)：**NO，禁止复活**。
10. tail 是 bounded census 的唯一主杀手：**NO，master-forced \(g_1\) 更强**。

---

## 42. Exact Remaining Unknowns

只剩一个顶层 unknown：

\[
\boxed{
\exists
\mathbf r\in\mathscr B_+,
\ \exists\text{ finite shape }\sigma:
\mathcal Z(\mathbf r;\sigma)\neq\varnothing
\ ?
}
\]

R15 若继续，只允许 theoremize：

- \(g_1^*\) integrality；
- \(z\)-valuation shell；
- tail divisor；
- \(z\)-digit interval；

之间的 exact collision，或构造第一个 exact \(z\)。

---

## 43. R14 Terminal Verdict

\[
\boxed{
\texttt{
R14_TERMINAL_VERDICT=
FIXED_CORE_FIBRE_FINITE
__SPHERE_ABSORBED_INTO_CF
__SMITH_COMPRESSED_TO_A_W_Z
__MASTER_COLLAPSED_TO_FORCED_G1
__TAIL_AND_GCD_REDUCED_TO_ONE_DIMENSIONAL_Z_SELECTOR
__CHEAPEST_POSITIVE_CHAMBER_EXACTLY_EMPTY
__NO_UNIVERSAL_EXTINCTION
__NO_FULL_LIFT
__SINGLE_TRANSVERSE_GATE
}.
}
\]

所以 R14 是：

\[
\boxed{\textbf{Outcome C}}
\]

而不是 A/B。

---

## 44. R15 Authorization Decision

R15 只授权 Route D：

\[
\boxed{
\textbf{Finite-Shape Master-}g_1
\times
\textbf{Exact Transverse }z\textbf{-Selector}.
}
\]

唯一 attack target：
\[
\boxed{
\mathcal Z(\mathbf r;\sigma)\neq\varnothing
}
\]
在 master 已经强制 \(g_1^*\) 之后的 exact truth value。

R15 禁止返回：

- carrier image；
- endpoint；
- DES quotient；
- generic PSDG；
- discriminant；
- packet allocation；
- radial-core elimination。

---

# Machine-readable Terminal Block

```text
R14_TERMINAL_VERDICT=FIXED_CORE_FIBRE_FINITE__SPHERE_ABSORBED_INTO_CF__SMITH_COMPRESSED_TO_A_W_Z__MASTER_COLLAPSED_TO_FORCED_G1__TAIL_AND_GCD_REDUCED_TO_ONE_DIMENSIONAL_Z_SELECTOR__CHEAPEST_POSITIVE_CHAMBER_EXACTLY_EMPTY__NO_UNIVERSAL_EXTINCTION__NO_FULL_LIFT__SINGLE_TRANSVERSE_GATE

R1_TO_R13_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=POST_PSDG_MASTER_G1_TAIL_Z_SELECTOR_NONEMPTINESS_ON_POSITIVE_RADIAL_CORE

RADIAL_CORE=(u0,Mr,Nr,n2,n3)
POSITIVE_RADIAL_CORE_SPACE=B_PLUS

RADIAL_CORE_FROZEN_DURING_LIFT_ANALYSIS=YES

TRANSVERSE_INDEPENDENT_VARIABLES=(g,k,A,W,c,X0,Y0,z)
TRANSVERSE_DERIVED_VARIABLES=(m2,m3,G,K,X,Y,P1,P2,P3,Q0,V,g1,g2,g3,b1,b2,b3,D,T3,Omega,H,K3,R)
TRANSVERSE_DISCRETE_CHOICES=(finite_exponent_chart;finite_CF_factor_pair;finite_frozen_cell_label)

SPHERE_ABSORBED_INTO_CF=YES

CF_EQUATION=c^2*X0*Y0=W^2*Mr^2+A^2*Nr^2
CF_COPRIMALITY=gcd(X0,Y0)=1
CF_PARITY=(X0,Y0_BOTH_ODD)_OR_(OPPOSITE_PARITY_AND_2|c)

P1_RECONSTRUCTION=c*(X0-Y0)/2
Q0_RECONSTRUCTION=c*(X0+Y0)/2
P2_RECONSTRUCTION=W*Mr
P3_RECONSTRUCTION=A*Nr

D_POSITIVITY_RATIO=X0/Y0>(K+1)/(K-1),K=10^k>=10

TAIL_DIVISIBILITY=Y|z*W*(Q0-A*Nr)<=>lambda_z|z,lambda_z=Y/gcd(Y,W*(Q0-A*Nr))
TAIL_DIVISIBILITY_SIZE_LOWER_BOUND=z>=z_tail=lambda_z*ceil(Lz/lambda_z)
TAIL_SIZE_UPPER_BOUND=z<Rz
TAIL_SIZE_COLLISION=EXACT_PER_FINITE_SHAPE_IF_z_tail>=Rz__NOT_UNIVERSAL

MASTER_LIFT_EQUATION=g1*Omega=u0*A*W*X*Y*G*D,Omega=W*T3-A*Y*(P2-G*Q0)
MASTER_LIFT_INDEPENDENT=YES

SMITH_TRANSVERSE_PREDICATES=gcd(z*A,C2)=1;gcd(z*W,C3)=1;gcd(A,W)=1;g2=u0W;g3=u0A
SMITH_RECONSTRUCTION_PREDICATE=CANONICAL_DECOMPOSITION_OF_(b1,b2,b3)_MUST_REPLAY_FROZEN_SMITH_PAIRWISE_GCD
PSDG_RECONSTRUCTION_PREDICATE=FROZEN_EXACT_REGRESSION__NOT_REOPENED
G1_FIREWALL_PREDICATE=gcd(z*u0*A*W,P1)=g1star
PRIMITIVE_PREDICATE=gcd(P1,P2,P3,Q0)=1

MINIMAL_LIFT_SYSTEM=L1_exponent_chart+L2_denominator_windows+L3_CF+L4_primitive+L5_D_T3_positive+L6_master_forced_g1+L7_tail_z_divisibility+L8_Smith23_gcd+L9_canonical_Smith_reconstruction+L10_g1_shell+L11_frozen_cell+L12_PSDG_regression

MINIMAL_LIFT_SYSTEM_EQUIVALENT_TO_FULL_POST_PSDG=YES_WITH_FROZEN_EXACT_CELL_AND_PSDG_REGRESSION_PREDICATES

POSITIVE_CORE_LIFT_FIBRE_FINITE=YES
POSITIVE_CORE_LIFT_FIBRE_DIMENSION=0__FINITE_DISCRETE

U1_POSITIVE_CORES_TESTED=810__COMPLETE_FOR_u0=1_n2=2_n3=1
U2_POSITIVE_CORES_TESTED=180__COMPLETE_FOR_u0=1_n2=2_n3=1
U3_POSITIVE_CORES_TESTED=90__COMPLETE_FOR_u0=1_n2=2_n3=1

FAIL_CF=0
FAIL_PRIMITIVE=120
FAIL_D_RATIO=0
FAIL_TAIL=378
FAIL_MASTER=582
FAIL_SMITH=0_AS_CORE_FIRST_FAILURE_AFTER_EXISTENTIAL_ENUMERATION
FAIL_PSDG=NOT_REACHED_AFTER_MASTER
FAIL_G1_FIREWALL=132_ASSIGNMENTS_WITH_INTEGER_g1star_BUT_GCD_SHELL_MISMATCH

RADIAL_CORE_INDUCED_GCD_OBSTRUCTION=PROVED_CONDITIONAL__gcd(lambda_z,C2*C3)>1_KILLS_SHAPE

TAIL_DIVISIBILITY_OBSTRUCTION=CONDITIONAL_EXACT__NOT_UNIVERSAL
CF_FACTOR_RATIO_OBSTRUCTION=NO__D_RATIO_ALREADY_FROZEN_IN_R7C

FULL_TRANSVERSE_LIFT_FOUND=NO
LIFTED_RADIAL_CORE=NONE
LIFTED_TRANSVERSE_DATA=NONE

PLAIN_INTEGER_RADIAL_GATE_PASSED=NOT_REACHED
PLAIN_U=NONE

Q1_PROGRESSION_ACTIVE=NO
Q1_PROGRESSION_PASS=NOT_REACHED
COPRIMALITY_PASS=NOT_REACHED

SOURCE_INTEGER_U_FOUND=NO
SOURCE_INTEGER_U=NONE

COMMON_U_INTEGER_SUCCESSOR_GATE=NOT_REACHED_AFTER_NEW_FULL_LIFT

DIGIT_SYNCHRONIZATION=NOT_REACHED
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

NEW_FIRST_FAILURE_GATE=POST_PSDG_FINITE_SHAPE_MASTER_G1__TAIL_GCD_Z_SELECTOR_NONEMPTINESS

POSITIVE_RADIAL_CORE_UNLIFTABILITY_PROVED=NO
POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NOT_PROVED

R14_SINGLE_TRANSVERSE_LIFTABILITY_GATE=YES

R15_AUTHORIZED=YES
R15_ARCHITECTURE=ROUTE_D__FINITE_SHAPE_MASTER_G1_X_EXACT_TRANSVERSE_Z_SELECTOR
R15_SINGLE_ATTACK_TARGET=EXACT_NONEMPTINESS_OR_UNIVERSAL_COLLISION_OF_Z_SELECTOR_AFTER_MASTER_FORCES_g1star
```

---

## Provenance Ledger

Primary frozen archives used:

- `105_R13_Post_PSDG_Source_Carrier_Image.md`
- `105_R3_Source_Completed_Valuation_Atlas.md`
- `105_R7C_Prescribed_Source_Divisor_Gate.md`
- `105_R7D_Determinant_Packet_Source_GCD_Firewall.md`
- `105_R8_Common_U_Integer_Source_Fibre.md`
- `105_R12_Normalized_Local_DES_Numerator_Residue.md`
- `strict_layer_A1_double_euclidean_smith_gcd_terminal_campaign.md`
- `strict_layer_backward_denominator_decimal_interface.md`

所有 bounded computation 与 global theorem 在本报告中严格分开。
