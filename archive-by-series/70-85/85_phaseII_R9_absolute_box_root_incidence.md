# 第二个八五计划·第九轮阶段报告

## Full-Root Absolute-Box Incidence × Non-Homogeneous Root Gap × Decimal Rectangle Extinction

**项目：** 三项十进制拼接平方和问题  
**范围：** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**轮次：** 第二个八五计划·R9  
**输入冻结：** R1–R8  
**最终状态：** \(J2\) 仍 OPEN  
**R9 终端判决：** `ONE_ABSOLUTE_BOX_GATE_IDENTIFIED`

---

# 0. Executive verdict

R9 按要求彻底停止 scaled-PCS / scaled-content / source-height / chord / discriminant-alone 等旧路线，直接研究

\[
\boxed{\mathcal V_{\rm root}^{\rm int}\cap\mathcal B_{\rm dec}}.
\]

本轮得到一个非常明确的架构判决：

1. **\((X,Y)\)-adapted full-root equation 已完整导出。** 通过
   \[
   Y=AX+HL,\qquad H=G/2,
   \]
   消去 \(L\)，full root 被压成关于 \(Z\) 的一个 exact quadratic。

2. **R9 原先优先级 1–4 的“实几何灭绝”机制被统一处决。** 对每一个合法 absolute decimal box 点
   \[
   \frac G{10}\le X<G,\qquad \frac{G^2K}{10}\le Y<G^2K,
   \]
   full-root quadratic 在 \(Z\) 上恰有两个实根，且一正一负。因此：
   - 不存在 box 内统一 residual sign；
   - discriminant 在 box 内不是负，而是严格正；
   - 正 root branch 不是绕开 rectangle，而是对整个 rectangle 都存在；
   - boundary-sign / real branch separation 不能关闭本问题。

3. **真正剩余的新信息是 integer spacing。** source lattice 对固定 \((X,Y)\) 把 \(Z\) 限制到一个模 \(2K\) 的单一等差类，而 full root 在正半轴只有一个实根 \(Z_+(X,Y)\)。因此 B9/C9 被精确压成：
   \[
   \boxed{Z_+(X,Y)\text{ 是否撞上该 }2K\text{-spaced source lattice coset}.}
   \]

4. R9 没有找到 full-root + double-box integral countermodel，也没有证明其不存在。因此不能宣布 J2 closure，也不能宣布 absolute-box architecture falsified。

5. R10 只允许攻击一条主 theorem：

\[
\boxed{\textbf{Absolute Positive-Branch Root–Lattice Interlacing Theorem}.}
\]

它等价于一个 box-adapted discriminant-square + exact divisibility / source-coset non-hit theorem。

所以本轮最终判：

```text
J2_STATUS=OPEN
ABSOLUTE_BOX_ARCHITECTURE=ALIVE
R9_TERMINAL_VERDICT=ONE_ABSOLUTE_BOX_GATE_IDENTIFIED
```

---

# 1. R1–R8 frozen verdicts

永久冻结：

```text
THEOREM_A=FALSE
DISCRIMINANT_ALONE=OLD_INFORMATION_CLASS
REAL_RADIAL_INCOMPATIBILITY=FALSE
CURRENT_PRIMITIVE_HEIGHT_MECHANISM=DEAD
SOURCE_INCIDENCE_ARCHITECTURE=FALSIFIED
SCALED_COMMON_U_ARCHITECTURE=NO_NEW_COMMON_U_INFORMATION
SCALED_PCS=NO_GAIN
SCALED_POWER_SECTION=NO_GAIN
```

R9 未重新使用：

- chord denominator / continued fractions；
- packet height / gauge repair；
- class group / genus / spinor genus；
- ambient discriminant-alone nonrepresentation；
- real radial ratio \(\rho\) obstruction；
- scaled \(UD\) modulus / \(UH^2\) section；
- generic \(U\)-support；
- source conic alone mining。

---

# 2. Full scaled root/source system recovered

设

\[
G=10^g,\qquad H=G/2,\qquad K=10^k,
\]

\[
uq=G+1,\qquad A=2u+1,\qquad B=2G+q.
\]

R8 scaled coordinates：

\[
X=Uc,\quad Z=Uz,\quad N=Un,\quad L=U\lambda,\quad Y=UC_2.
\]

辅助 scaled root words：

\[
P=UC_1,\qquad W=Uw,\qquad S=UT,\qquad D_2^*=Ud_2.
\]

精确系统：

\[
\boxed{L=r_0Z+2KN,}
\tag{S1}
\]

\[
\boxed{P=\frac{BZ+AL}{2K},}
\tag{S2}
\]

\[
\boxed{Y=AX+HL,}
\tag{S3}
\]

\[
\boxed{W=GHZ-uAX,}
\tag{S4}
\]

\[
\boxed{S=GZ+uL,}
\tag{S5}
\]

\[
\boxed{D_2^*=uX+GW,}
\tag{S6}
\]

\[
\boxed{H^2P^2+W^2=SD_2^*.}
\tag{ROOT}
\]

并有

\[
\boxed{2uKP=AS+Z.}
\tag{S9}
\]

absolute box：

\[
\boxed{\frac G{10}\le X<G,}
\qquad
\boxed{\frac{G^2K}{10}\le Y<G^2K.}
\tag{BOX}
\]

R8 exact-content / support 信息仍冻结为 side predicates，不作为本轮主机制：

\[
U=\gcd(X,Z,N),\qquad \gcd(U,uGH)=1.
\]

---

# 3. Eliminate \(L\): exact \((X,Y,Z)\)-adapted root equation

定义 absolute radial defect

\[
\boxed{\mathscr D:=Y-AX.}
\]

由 \(Y=AX+HL\) 与 \(H=G/2\)：

\[
\boxed{L=\frac{2\mathscr D}{G}.}
\tag{LXY}
\]

把它代入 R7/R8 的 exact \((X,Z,L)\) conic：

\[
\begin{aligned}
E={}&u^2A^2X^2+u^2(AG-1)XL-uGXZ\\
&-\frac{G^4}{4}Z^2-\frac{uG^3}{2}ZL
+\frac{G^2}{16K^2}(BZ+AL)^2,
\end{aligned}
\]

得到：

\[
\boxed{F(X,Y,Z)=0,}
\]

其中

\[
\boxed{
\begin{aligned}
F={}&
\frac{A^2}{4K^2}\mathscr D^2\\
&+\left(
\frac{ABG}{4K^2}Z-uG^2Z+2u^2X\left(A-\frac1G\right)
\right)\mathscr D\\
&+u^2A^2X^2-uGX Z
+\frac{G^2(B^2-4G^2K^2)}{16K^2}Z^2.
\end{aligned}}
\tag{R9-XY}
\]

这是 R9 要求的低维 absolute root equation。

---

# 4. The natural quadratic variable is \(Z\)

把 (R9-XY) 写成：

\[
\boxed{a_ZZ^2+b_ZZ+c_Z=0,}
\]

其中

\[
\boxed{
a_Z=\frac{G^2(B^2-4G^2K^2)}{16K^2},
}
\]

\[
\boxed{
b_Z=G\left(
\frac{AB\mathscr D}{4K^2}-uG\mathscr D-uX
\right),
}
\]

\[
\boxed{
c_Z=
\frac{A^2\mathscr D^2}{4K^2}
+2u^2X\mathscr D\left(A-\frac1G\right)
+u^2A^2X^2.
}
\]

这比 quadratic-in-\(Y\) 更适合 absolute box：\(a_Z\) 的符号只由 outer fibre 决定，而 \(c_Z\) 在 box 上可 exact 判正。

---

# 5. Legal outer bounds imply the whole decimal box has \(\mathscr D>0\)

当前 live scope：

\[
g\ge4,\qquad K=10^k\ge10,\qquad u>1,\qquad q>1,
\]

并继承当前 central \(q>1\) shell 的

\[
q\ge7.
\]

由 \(uq=G+1\)：

\[
u\le\frac{G+1}{7},
\]

故

\[
A=2u+1\le\frac{2(G+1)}7+1<G.
\]

另一方面，box 下

\[
Y\ge\frac{G^2K}{10}\ge G^2,
\]

而

\[
AX<AG<G^2.
\]

所以：

\[
\boxed{
\mathscr D=Y-AX>0
\quad\text{for every point of the entire absolute decimal rectangle.}
}
\tag{D+}
\]

这不是额外 source positivity 假设，而是 box + legal outer range 本身推出。

---

# 6. Exact sign of the \(Z^2\) coefficient

由于

\[
B=2G+q<3G+1,
\]

而

\[
2GK\ge20G,
\]

故

\[
B<2GK.
\]

定义

\[
\boxed{\Lambda:=4G^2K^2-B^2>0.}
\]

于是

\[
\boxed{a_Z=-\frac{G^2\Lambda}{16K^2}<0.}
\tag{AZ-}
\]

由 \(\mathscr D>0\)、\(X>0\)、\(A-1/G>0\)：

\[
\boxed{c_Z>0.}
\tag{CZ+}
\]

---

# 7. R9 Real Absolute-Box Surjectivity Theorem

## Theorem R9-RABS

对每一个 legal outer fibre，以及每一个 real box point

\[
(X,Y)\in
\left[\frac G{10},G\right)
\times
\left[\frac{G^2K}{10},G^2K\right),
\]

quadratic \(F(X,Y,Z)=0\) 恰有两个 distinct real roots，并且一正一负。

### Proof

由 (AZ-) 与 (CZ+)：

\[
a_Z<0<c_Z.
\]

因此两根乘积

\[
Z_+Z_-=\frac{c_Z}{a_Z}<0.
\]

故若根为实，则一正一负。

判别式：

\[
\Delta_Z=b_Z^2-4a_Zc_Z.
\]

因 \(a_Zc_Z<0\)，

\[
\boxed{
\Delta_Z>b_Z^2\ge0,
}
\]

且严格：

\[
\boxed{\Delta_Z>0.}
\]

故确有两个 distinct real roots，且一正一负。证毕。

### Consequence

\[
\boxed{
\pi_{X,Y}\bigl(\mathcal V_{\rm root}(\mathbb R)\bigr)
\supseteq\mathcal B_{\rm dec}.
}
\]

更精确地：**整个 absolute decimal rectangle 都被唯一正 root branch 覆盖。**

这直接 falsify 任何纯实版本的 Non-Homogeneous Root Gap。

---

# 8. Root branch formula and transverse monotonicity

正负 branches：

\[
\boxed{
Z_\pm=\frac{-b_Z\pm\sqrt{\Delta_Z}}{2a_Z},
}
\]

按符号重排后取 \(Z_+>0>Z_-\)。

因为 quadratic derivative

\[
F_Z=2a_ZZ+b_Z,
\]

在两根处：

\[
\boxed{F_Z(Z_+)=-\sqrt{\Delta_Z}<0,}
\]

\[
\boxed{F_Z(Z_-)=+\sqrt{\Delta_Z}>0.}
\]

所以：

- negative branch 是 upward transverse crossing；
- positive branch 是 downward transverse crossing；
- 两支从不切触，不存在 double-root boundary。

R9 没有证明 \(Z_+\) 对 \(x\) 或 \(y\) 的全局单调性；真正需要且已 exact 的 branch monotonicity 是对 residual 的 transverse crossing。

---

# 9. Required normalized equation

定义

\[
\boxed{x:=\frac XG,\qquad y:=\frac{Y}{G^2K}.}
\]

因此

\[
\boxed{x,y\in[1/10,1).}
\]

再定义唯一剩余 normalized root coordinate

\[
\boxed{\zeta:=\frac ZK,}
\]

以及

\[
\boxed{
\delta:=\frac{\mathscr D}{GK}
=Gy-\frac AKx.
}
\]

由 box theorem \(\delta>0\)。

将 \(X=Gx\)、\(Y=G^2Ky\)、\(Z=K\zeta\) 代入，并除以 \(G^2\)，得到 exact normalized relation：

\[
\boxed{
\mathcal F(x,y,\zeta)
=\alpha\zeta^2+\beta\zeta+\gamma=0,
}
\tag{NR9}
\]

其中

\[
\boxed{\alpha=-\frac{\Lambda}{16}<0,}
\]

\[
\boxed{
\beta=\frac{AB}{4}\delta-GK^2u\,\delta-Kux,
}
\]

\[
\boxed{
\gamma=
\frac{A^2}{4}\delta^2
+2Ku^2x\left(A-\frac1G\right)\delta
+A^2u^2x^2>0.
}
\]

Normalized discriminant：

\[
\boxed{
\Delta_\zeta=\beta^2+\frac{\Lambda}{4}\gamma>0.
}
\]

若定义

\[
\boxed{\mathscr S:=4\beta^2+\Lambda\gamma,}
\]

则

\[
\boxed{\mathscr S>0}
\]

且

\[
\boxed{
\zeta_\pm
=\frac{4(2\beta\pm\sqrt{\mathscr S})}{\Lambda}.
}
\]

因为

\[
\sqrt{\mathscr S}>|2\beta|,
\]

故

\[
\boxed{\zeta_+>0>\zeta_-.}
\]

这是本轮要求的 exact normalized root equation。

---

# 10. Legal \(k\)-range and why one global \(\kappa\le1/10\) assumption is illegal

当前 frozen exponent shell 包含

\[
\ell:=2g-k\ge6.
\]

所以

\[
\boxed{1\le k\le2g-6.}
\]

因此必须分清：

1. **low-\(k\)**：\(k<g\)，此时
   \[
   \kappa:=K/G=10^{k-g}\le1/10;
   \]
2. **boundary**：\(k=g\)，此时 \(\kappa=1\)；
3. **high-tail**：\(g<k\le2g-6\)，此时 \(\kappa>1\)。

所以 R9 不能把 \(K/G\le1/10\) 当成全局事实。

本轮 real-root theorem 不依赖这一 subdivision；这也是它的优点。

---

# 11. Priority 1: root residual sign — FALSE

由于对每个 box point：

\[
F(X,Y,0)=c_Z>0,
\]

而

\[
F(X,Y,Z)\to-\infty\qquad(Z\to+\infty),
\]

residual 必然改号。

更强地，本轮构造一个 exact root-independent source-compatible opposite-sign pair。

取 legal fibre：

\[
(g,k,u,q)=(4,1,73,137),
\]

\[
G=10000,\ K=10,\ H=5000,\ A=147,\ B=20137,\ r_0=9.
\]

固定：

\[
\boxed{X=1001,\qquad L=99969,}
\]

于是

\[
\boxed{Y=AX+HL=499992147.}
\]

显然 X/Y 双 box均 PASS，且 \(X,Y\) 均为 ten-unit。

## State S+：\(Z=1\)

source lattice：

\[
N=\frac{L-r_0Z}{2K}=4998,
\]

\[
U=\gcd(X,Z,N)=1.
\]

其余：

\[
P=735779,
\]

\[
W=39258269,
\]

\[
S=7307737,
\]

\[
D_2^*=392582763073.
\]

positive/order words \(h,m,r\) 也全为正：

\[
537853,\quad79054391,\quad2689191927.
\]

并 exact 检查：

```text
SOURCE_LATTICE=PASS
POSITIVE_BRANCH=PASS
TEN_UNIT=PASS
COMMON_V=PASS
FULL_PRIMITIVE=PASS
REGULAR=PASS
EXACT_CONTENT_U=PASS (U=1)
```

但 root residual 的 integer-cleared值为：

\[
\boxed{
\Psi(1)=170670688791025288960000000>0.
}
\]

## State S−：\(Z=61\)

仍有

\[
Z\equiv1\pmod{20},
\]

所以同一 source-lattice coset；

\[
N=4971,
\qquad U=1.
\]

并且：

\[
P=796190,
\]

\[
W=3039258269,
\]

\[
S=7907737,
\]

\[
D_2^*=30392582763073.
\]

同样 exact PASS：

```text
SOURCE_LATTICE=PASS
POSITIVE_BRANCH=PASS
TEN_UNIT=PASS
COMMON_V=PASS
FULL_PRIMITIVE=PASS
REGULAR=PASS
EXACT_CONTENT_U=PASS
```

但：

\[
\boxed{
\Psi(61)=-3444023960206875511040000000<0.
}
\]

因此：

\[
\boxed{\texttt{ROOT_RESIDUAL_SIGN=FALSE}.}
\]

而且这个 falsification 已穿过几乎全部 root-independent full-source gates；不是 relaxed ambient artifact。

---

# 12. Priority 2: Y-root branch absolute separation — FALSE as a real theorem

R9 原候选想证明：

\[
X\in[G/10,G)
\Longrightarrow
Y\notin[G^2K/10,G^2K).
\]

R9-RABS 给出严格相反结论：

> 对 box 中每一个 \((X,Y)\)，都有唯一正 real \(Z_+(X,Y)\) 使 full-root equation 成立。

所以 root surface 在 real level 不只是“穿过” rectangle，而是其 positive branch **投影覆盖整个 rectangle**。

因此：

\[
\boxed{\texttt{ROOT_BRANCH_SEPARATION=FALSE}.}
\]

这里的 FALSE 只针对原计划的 real Y-strip separation theorem；它不排除 integer branch spacing。

---

# 13. Priority 3: discriminant negativity — FALSE; square gate survives

已经证明：

\[
\boxed{\Delta_Z>0}
\]

在 entire rectangle 上成立。

所以：

\[
\boxed{\texttt{DISCRIMINANT_NEGATIVITY=FALSE}.}
\]

但 integral root 仍要求 discriminant成为 exact square并满足 root numerator divisibility。

为此清分母。

定义：

\[
\boxed{
\Pi:=AB\mathscr D-4uGK^2\mathscr D-4uK^2X,
}
\]

\[
\boxed{
\mathcal C_{\Box}:=
4A^2G\mathscr D^2
+32K^2u^2X\mathscr D(AG-1)
+16GK^2u^2A^2X^2.
}
\]

注意 \(\mathcal C_{\Box}>0\)。

把 (R9-XY) 乘 \(-16GK^2\)，得到完全 integral 的 quadratic：

\[
\boxed{
G^3\Lambda Z^2-4G^2\Pi Z-\mathcal C_{\Box}=0.
}
\tag{IQ}
\]

其判别式：

\[
\boxed{
\Delta_{\Box}
=16G^4\Pi^2+4G^3\Lambda\mathcal C_{\Box}
=4G^3\bigl(4G\Pi^2+\Lambda\mathcal C_{\Box}\bigr)>0.
}
\tag{DISC}
\]

若存在 integral positive root，则必须存在整数 \(W>0\)：

\[
\boxed{W^2=\Delta_{\Box},}
\tag{SQ}
\]

并且

\[
\boxed{
2G^3\Lambda\mid4G^2\Pi+W.
}
\tag{DIV}
\]

正 root 为

\[
\boxed{
Z_+=\frac{4G^2\Pi+W}{2G^3\Lambda}.
}
\]

这不是旧 R1 的 ambient square theorem：\(\Delta_{\Box}\) 明确读取 absolute \(X\sim G\)、\(Y\sim G^2K\) box coordinates。

R9 未关闭 (SQ)+(DIV)，所以：

```text
ROOT_DISCRIMINANT_BOX_GATE=OPEN
```

---

# 14. Priority 4: boundary exclusion — FALSE / not useful

box 四边上的任何 point 仍满足 \(\mathscr D>0\)，故同样：

\[
F(0)>0,
\qquad
F(Z)\to-\infty.
\]

因此每一条 boundary 的 admissible real portion上都存在 positive root branch。

不存在通过四边 residual 同号把 zero contour挡在 rectangle之外的机制。

所以：

\[
\boxed{\texttt{BOUNDARY_EXCLUSION=FALSE}.}
\]

corner leading-term sign 也不能改变这一 exact conclusion；无需依赖 asymptotic 图形判断。

---

# 15. Priority 5: source-lattice integer spacing — the unique surviving gate

B9 加入 source lattice。

由

\[
L=\frac{2\mathscr D}{G},
\]

首先必须有

\[
\boxed{L\in\mathbb Z.}
\]

然后：

\[
\boxed{L=r_0Z+2KN.}
\]

即

\[
\boxed{Z\equiv r_0^{-1}L\pmod{2K},}
\tag{ZCOS}
\]

其中 \(r_0\) 是 ten-unit，故对 \(2K\) 可逆。

设唯一 residue representative：

\[
0\le Z_0(L)<2K,
\qquad
Z_0(L)\equiv r_0^{-1}L\pmod{2K}.
\]

则所有 source-lattice candidates：

\[
\boxed{Z=Z_0(L)+2Km,\qquad m\in\mathbb Z.}
\tag{AP}
\]

而 full root 在正半轴只有一个 real root \(Z_+(X,Y)\)。

所以 B9 精确等价于：

\[
\boxed{
Z_+(X,Y)\in Z_0(L)+2K\mathbb Z_{\ge0}.
}
\tag{HIT}
\]

在 normalized coordinate \(\zeta=Z/K\) 中，source lattice spacing恰为：

\[
\boxed{\Delta\zeta=2.}
\]

这就是 R9 真正找到的 non-homogeneous integer mechanism。

它不是 chord rational approximation，也不是 old projective height；它是 absolute-box-selected unique root 与 exact source lattice 的直接 spacing incidence。

---

# 16. Exact spacing witness inside the box

继续使用：

\[
(g,k,u,q)=(4,1,73,137),
\]

\[
X=1001,\quad L=99969,\quad Y=499992147.
\]

由于 \(r_0=9\)：

\[
Z\equiv1\pmod{20}.
\]

exact residual：

\[
\Psi(1)>0,
\]

而直接计算：

\[
\Psi(21)=-1002551926556808311040000000<0.
\]

R9-RABS 又保证正 root唯一。

因此严格有：

\[
\boxed{1<Z_+(X,Y)<21.}
\]

但 source-lattice allowed positive sites 是：

\[
1,21,41,61,\ldots
\]

故该 box point 对 B9 是 exact extinct：

\[
\boxed{
Z_+(X,Y)\notin1+20\mathbb Z.
}
\]

这是本轮最清楚的“root × absolute box × lattice spacing”机制样本。

---

# 17. R8 C1/C3 differential in the new XY framework

## C1 — root survives, box dies

R8 deepest exact root/source survivor：

\[
(g,k,u,q)=(5,3,11,9091),
\]

\[
G=100000,\qquad K=1000,
\]

\[
c=2844241425759278313791310157183552723,
\]

\[
C_2=54695636408717919553598977546465994745062629.
\]

relative oversize：

\[
\frac cG\approx2.8442\times10^{31},
\]

\[
\frac{C_2}{G^2K}\approx5.4696\times10^{30}.
\]

所以对任何 \(U\ge1\)：

\[
X\ge c>G,
\qquad
Y\ge C_2>G^2K.
\]

signature：

```text
FULL_ROOT=PASS
FULL_SOURCE=PASS
X_BOX=FAIL_BY_ENORMOUS_OVERSIZE
Y_BOX=FAIL_BY_ENORMOUS_OVERSIZE
```

## C3 — box survives, root dies

R8 PLCF \(t=0\)：

\[
(g,k,u,q)=(5,1,11,9091),
\]

\[
X=99999,
\qquad
Y=15002149977,
\]

\[
Z=99999,
\qquad L=299997,
\qquad N=0.
\]

normalized box location：

\[
\boxed{x=0.99999,\qquad y=0.15002149977.}
\]

它通过 box / source lattice / exact content / common-U support，但 full root fail。

R9 在同一 \((X,Y)\) 上得到更强 diagnosis：

\[
\Psi(0)>0,
\]

\[
\Psi(1)<0.
\]

由 unique positive branch：

\[
\boxed{0<Z_+(X,Y)<1.}
\]

因此这个 C3 box point **连 ambient positive integral root 都没有**；R8 使用的 \(Z=99999\) 与真正 positive root branch相距极远。

这说明 C3 的 root failure 在 R9 language 中不是模糊 residual accident，而是一个 exact integer-spacing miss。

---

# 18. Counterexample guillotine A9/B9/C9

本轮严格区分：

## A9 — Ambient integer root + box

要求：

\[
X,Y,Z\in\mathbb Z_{>0},
\]

box + (IQ)。不要求 source lattice / primitive / exact content。

**Verdict:** OPEN。

R9 没有找到 certified integer countermodel，也没有证明 extinction。

有限 deterministic falsification probes：

- fibre \((g,k,u)=(4,1,73)\)：完整扫描 \(X\in[1000,9999]\)、\(1\le Z\le100\) 的 integer-\(Y\) quadratic roots，未找到 box hit；
- fibre \((5,1,11)\)：对应浅层 exact probe 未找到 hit。

这些只作 counterexample guillotine，不提升为 theorem。

## B9 — Source-lattice integer root + box

A9 加：

\[
L=\frac{2(Y-AX)}G\in\mathbb Z,
\]

\[
L\equiv r_0Z\pmod{2K}.
\]

**Verdict:** OPEN。

已精确压缩为 single-coset hit condition (HIT)。

## C9 — Full source integer root + box

再加：

- positive/order branch；
- primitive；
- common-\(V\)；
- regularity；
- exact content \(U\)；
- common-\(U\) support。

**Verdict:** OPEN。

当前 archive 中没有 full-root + double-box source countermodel。

因此：

```text
A9_AMBIENT_ROOT_BOX=NONE_FOUND
B9_SOURCE_LATTICE_ROOT_BOX=NONE_FOUND
C9_FULL_SOURCE_ROOT_BOX=NONE_FOUND
FULL_COMMON_U_STATE=NOT_FOUND
```

`NONE_FOUND` 只表示本轮 exact archive + falsification search未出现，不表示 proof。

---

# 19. Root geometry summary

1. **最自然 quadratic variable：** \(Z\)。
2. **real branches：** 恰两支，\(Z_+>0>Z_-\)。
3. **branch crossing：**
   \[
   F_Z(Z_+)<0,\qquad F_Z(Z_-)>0;
   \]
   两支均 transverse，无 double root。
4. **branch 是否进入 rectangle：** 不只是进入；positive real branch 的 \((X,Y)\)-projection覆盖整个 rectangle。
5. **discriminant sign：** box 内严格正。
6. **boundary sign：** 无法排除；每个 boundary point同样有 positive real root。
7. **deepest controls：**
   - C1：root 真，但相对 box 超大 \(10^{30+}\) 倍；
   - C3：box 真，但同一 \((X,Y)\) 的 actual positive real root落在 \((0,1)\)，因此被 integer spacing直接跳过。

---

# 20. What exactly died in R9

以下 theorem candidates 被 exact 处决：

```text
REAL_NON_HOMOGENEOUS_ROOT_GAP=FALSE
ROOT_RESIDUAL_UNIFORM_SIGN=FALSE
REAL_ROOT_BRANCH_Y_SEPARATION=FALSE
BOX_DISCRIMINANT_NEGATIVITY=FALSE
REAL_BOUNDARY_EXCLUSION=FALSE
```

这些失败不是 numerical accident，而是统一 theorem R9-RABS 的直接后果。

---

# 21. What survives

只剩：

\[
\boxed{\textbf{positive real root integrality / source-lattice hit}.}
\]

两个完全等价的 exact interfaces：

### Interface I — discriminant-square + numerator divisibility

\[
W^2=\Delta_{\Box},
\]

\[
2G^3\Lambda\mid4G^2\Pi+W.
\]

### Interface II — source-lattice interlacing

\[
Z_+(X,Y)\in Z_0(L)+2K\mathbb Z.
\]

R10 应把这两种写法视为同一个 theorem，而不是两个 campaign。

---

# 22. R10 unique main theorem

## Absolute Positive-Branch Root–Lattice Interlacing Theorem

对所有 legal R9 outer data，以及所有 integer box points

\[
\frac G{10}\le X<G,
\qquad
\frac{G^2K}{10}\le Y<G^2K,
\]

令

\[
\mathscr D=Y-AX,
\qquad
L=\frac{2\mathscr D}{G}.
\]

若 \(L\notin\mathbb Z\)，source lift立即失败。

若 \(L\in\mathbb Z\)，令

\[
Z_0\equiv r_0^{-1}L\pmod{2K}.
\]

设 \(Z_+(X,Y)\) 是 R9-RABS 唯一 positive real root。

R10 唯一目标：证明

\[
\boxed{
Z_+(X,Y)\notin Z_0+2K\mathbb Z_{\ge0}.
}
\tag{R10-MAIN}
\]

在需要时可改写成：

\[
\boxed{
\Delta_{\Box}\ne W^2
\quad\text{or}\quad
2G^3\Lambda\nmid4G^2\Pi+W
\quad\text{or}\quad
L\not\equiv r_0Z_+\pmod{2K}.
}
\]

但 R10 不得把这拆成三个独立路线。

---

# 23. Absolute-Box Ledger for the strongest new spacing pseudo-state

取 \((g,k,u,q)=(4,1,73,137)\)，\(X=1001,Y=499992147,L=99969\)。

```text
FULL_ROOT = FAIL at every tested source-lattice site
ROOT_BRANCH = PLUS exists uniquely over R

X_BOX = PASS
Y_BOX = PASS

SOURCE_LATTICE = PASS
POSITIVE_BRANCH = PASS
PRIMITIVE = PASS
COMMON_V = PASS
REGULAR = PASS

EXACT_CONTENT_U = PASS (U=1)

ROOT_DISCRIMINANT = STRICTLY_POSITIVE
ROOT_RESIDUAL(Z=1) = +170670688791025288960000000
ROOT_RESIDUAL(Z=61) = -3444023960206875511040000000
ROOT_RESIDUAL_SIGN = BOTH SIGNS

FULL_SOURCE_LIFT = FAIL ONLY BECAUSE FULL_ROOT≠0
```

同一 \((X,Y)\) 下：

\[
1<Z_+<21,
\]

而 source-lattice sites 是 \(1+20\mathbb Z\)，所以该 point exact misses root。

---

# 24. Terminal ledger

```text
J2_STATUS =
OPEN

R8_SCALED_COMMON_U =
FROZEN_NO_NEW_INFORMATION

ABSOLUTE_BOX_ARCHITECTURE =
ALIVE

XY_ADAPTED_ROOT_EQUATION =
COMPLETE

NORMALIZED_ROOT_EQUATION =
COMPLETE

A9_AMBIENT_BOX_EXTINCTION =
OPEN

B9_SOURCE_LATTICE_BOX_EXTINCTION =
OPEN

C9_FULL_SOURCE_BOX_EXTINCTION =
OPEN

ROOT_RESIDUAL_SIGN =
FALSE

ROOT_BRANCH_SEPARATION =
FALSE

ROOT_DISCRIMINANT_BOX_GATE =
OPEN
# negativity is FALSE; square/divisibility gate remains open

BOUNDARY_EXCLUSION =
FALSE

INTEGER_SPACING_GATE =
OPEN
# exact single remaining gate identified

FULL_ROOT_BOX_COUNTERMODEL =
NOT_FOUND

FULL_COMMON_U_COUNTERMODEL =
NOT_FOUND

R9_TERMINAL_VERDICT =
ONE_ABSOLUTE_BOX_GATE_IDENTIFIED
```

---

# 25. Final answer to R9 core question

R9 的最终核心问题是：

\[
\boxed{
\textbf{full root surface 是否真正穿过 absolute decimal rectangle？}
}
\]

答案必须分 real / integral 两层：

### Real answer

\[
\boxed{\textbf{YES — 而且 positive real root branch 的投影覆盖整个 rectangle。}}
\]

所以 real Non-Homogeneous Root Gap 正式死亡。

### Integral answer

\[
\boxed{\textbf{仍未证明 YES，也未找到 countermodel。}}
\]

但它不再是模糊的“root + box incidence”。R9 已把它 exact 压缩为：

\[
\boxed{
\textbf{唯一 positive real root}
\quad\times\quad
\textbf{step-}2K\textbf{ source lattice coset}
}
\]

的 hit/non-hit theorem。

这就是 R10 唯一合法主接口。

