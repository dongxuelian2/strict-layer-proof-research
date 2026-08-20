# J2-65-R8 — Binary Norm-Torus Torsor × Even Clifford/Brauer Class × Ramification-Divisor Pullback

**Scope:** Strict Layer — A1-only — Exact Resonance R=0 — J=2  
**Round:** 65 第八轮 / A1 统一终端线第三十三轮  
**Status:** **J2 OPEN**

## Executive verdict

本轮完成：
\[
\boxed{\text{one smooth conic fibre}\to\text{one norm torsor}\to\text{one Brauer class}}.
\]

直接沿 R7 completed-square 得到的 \(F(\sqrt a)\) 仍随 \(\lambda\) 移动；但同一个 even-Clifford class 存在更强的固定表示
\[
\boxed{\beta=(-R,-A_1(2X+q+2)\Xi)}.
\]
因此全部 power-of-ten fibres 共享固定 norm torus \(F(\sqrt{-R})\)，moving power-of-ten 信息只进入 target 的 \(\Xi\)。

## 1. Exact moving norm form

\[
A(r)=A+Br+Cr^2,\qquad L(r)=E+Fr,
\]
\[
A(r)+Dy^2+\lambda yL(r)=0.
\]
令
\[
z=2Dy+\lambda L(r),
\]
则
\[
z^2=ar^2+br+c
\]
with
\[
a=\lambda^2F^2-4DC,\quad b=2\lambda^2EF-4DB,\quad c=\lambda^2E^2-4DA.
\]
令 \(w=2ar+b\)，得到
\[
\boxed{w^2-4az^2=\Delta_B},\qquad \Delta_B=b^2-4ac.
\]
所以在 \(a\ne0\) chart，
\[
\Delta_B\in N_{F(\sqrt a)/F}\iff (a,\Delta_B)=0.
\]

## 2. Square-class collapse

Exact regression:
\[
\Delta_B=-64D\det(M_P+\lambda M_S).
\]
而
\[
D=Xq^4(q+4)^2(2X+q+2)c^2,
\]
\[
\det M=Xq^6(X+1)^2(q+4)^4(2X+q+2)c^4\Xi.
\]
故
\[
\boxed{[\Delta_B]=[-\Xi]}.
\]

同时
\[
[a]=[4\lambda^2(X+1)^2f^2-X(2X+q+2)C].
\]
因此 moving presentation 的 norm field 确实有 genuine additive \(\lambda^2\) dependence。

## 3. Fixed norm-torus theorem

定义
\[
H=4AC-B^2.
\]
exactly
\[
\boxed{H=[2q(X+1)(q+4)c]^2R}.
\]
故 \([-H]=[-R]\)，与 \(\lambda\) 无关。

令
\[
J_A=2AF-BE,\quad
V=2A\alpha+BT+\lambda EY,\quad
W=HT+\lambda J_AY.
\]
从 conic equation exact 得
\[
\boxed{W^2+HV^2=-16A\det(M)Y^2}.
\]
actual q>1 有 \(Y>0\)，于是
\[
N_{F(\sqrt{-H})/F}\left(W/Y+(V/Y)\sqrt{-H}\right)=-16A\det(M).
\]
写 \(A=XA_1\) 并删 squares：
\[
\boxed{\beta=(-R,-A_1(2X+q+2)\Xi)}.
\]

这证明：
\[
\boxed{\text{all power-of-ten fibres are torsors under one fixed norm torus}}.
\]

\(F(\sqrt a)\) 与 \(F(\sqrt{-R})\) 都只是 quaternion 的 quadratic subfield presentations；ternary even Clifford algebra 的 center 是 \(F\)。

## 4. Even Clifford regression

moving diagonal form
\[
\langle1,-4a,-\Delta_B\rangle
\]
给
\[
C^+=(a,\Delta_B).
\]
fixed block diagonalization给
\[
C^+=(-R,-A_1(2X+q+2)\Xi).
\]
两者 exact equivalent，故 binary norm 与 original ternary conic 是同一个 Brauer invariant。

## 5. \(a=0\) is a coordinate degeneration

\(a=0\) 只使 moving \(r\)-leading coefficient presentation 退化。actual conic 已知 smooth，且 fixed block 上 \(R>0\)，所以 fixed norm presentation不退化。无需建立新 branch。

## 6. True affine horizontal Brauer ramification

用
\[
\beta=(-R,-A_1h\Xi),\qquad h=2X+q+2.
\]
候选 divisors 只有 \(R,A_1,h,\Xi\)。

- \(A_1=0\)：由 \(4AC-B^2=s^2R\) 且 \(A=XA_1\)，\(-R\) 为 square，residue trivial。
- \(h=0\)：exactly \(R=-4(X+1)^2\)，故 residue trivial。
- \(R=0\)：exact identity
\[
X^4A_1h-q^2m^2=Re^2,
\]
\[
m=2X^3+2X^2q+8X^2+Xq+4X-q,
\]
所以 \(A_1h\) 在 \(\kappa(R)\) 为 square；同时 \(\Xi|_R\) 是负 square，完整 residue trivial。
- \(\Xi=0\)：\(R=[2\lambda X^2(X+1)]^2\)，故 tame residue 是 \([-1]\)，nontrivial。

因此在 affine generic base over \(\mathbb Q\)：
\[
\boxed{\operatorname{Ram}(\beta)=V(\Xi)}.
\]

R7 safe bad divisor 中只有 \(\Xi\) 是真正 horizontal Brauer ramification component；常数 2 属于 arithmetic vertical place，不计入这个 \(\mathbb Q\)-parameter-space component count。

## 7. Generic class nontrivial

\[
\partial_\Xi(\beta)=[-1]\ne1
\]
直接给
\[
\boxed{\beta_{\rm generic}\ne0}.
\]
这从 Brauer class 内部解释 R7 的 universal rational section = FALSE。

## 8. Cyclotomic pullback

代入
\[
X=uq-1,\qquad \lambda=K/X.
\]
定义
\[
\rho=R(uq-1,q)/q^2,
\]
\[
\sigma=A_1(uq-1,q)/q,
\]
\[
\Phi=\rho-4K^2u^2(uq-1)^2.
\]
exactly
\[
R=q^2\rho,\quad A_1=q\sigma,\quad h=q(2u+1),\quad \Xi=q^2\Phi.
\]
故
\[
\boxed{\beta_{\rm act}=(-\rho,-\sigma(2u+1)\Phi)}.
\]
true ramification pullback继续只有
\[
\boxed{V(\Phi)}.
\]

\[\rho=4 q^{2} u^{4} + 4 q^{2} u^{3} + q^{2} u^{2} - 8 q u^{3} - 4 q u^{2} + 4 u^{2} - 2\]

\[\sigma=2 q^{4} u^{3} + q^{4} u^{2} + 16 q^{3} u^{3} + 4 q^{3} u^{2} + 32 q^{2} u^{3} - 8 q^{2} u^{2} + 4 q^{2} u - 32 q u^{2} + 8 q u + 8 u - 4\]

## 9. Power-of-ten section

没有独立 multiplicative \(G\) 或 \(K\) square-class entry；\(K\) 只通过 \(K^2\) additively 出现在 \(\Phi\)。因此不能把 \(K^2\) 从加法表达式中删除。

结论不是 finite parity states：
\[
\boxed{\text{finite parity collapse = FALSE}},
\]
而是
\[
\boxed{\text{infinite exponent orbit = one low-degree Brauer symbol}}.
\]

## 10. Signs and real place

R7 \(M_P\) positive definite给 actual \(R>0,A_1>0\)。pullback后
\[
\rho>0,\quad \sigma>0,\quad 2u+1>0.
\]
R7 singular-size theorem给 \(\Xi<0\)，故 \(\Phi<0\)。所以 fixed field \(\mathbb Q(\sqrt{-\rho})\) 是 imaginary quadratic，而 target
\[
-\sigma(2u+1)\Phi>0.
\]
real place 与 R7 signature=(2,1) 完全一致，不给 obstruction。

此外 moving presentation 的 \(a\) 在 actual q>1 section 上其实也有统一符号：
\[
\boxed{a>0}.
\]
证明不需要枚举。写
\[
[a]=[a_0],\qquad
a_0=4\lambda^2(X+1)^2f^2-X(2X+q+2)C,
\]
并代入
\[
X=uq-1,\qquad \lambda=K/X,\qquad q\ge3,\ u\ge1,\ K\ge10.
\]
令 \(P=X^2a_0\)。它关于 \(K^2\) 单调非减，因为 \(K^2\)-系数 exact 为
\[
4q^2u^2\Bigl(
2q^6u^2+14q^5u^2-3q^5u+12q^4u^2-14q^4u-q^4
-24q^3u^2+4q^3u-8q^3
-16q^2u^2+56q^2u-16q^2+32qu-32q-16
\Bigr)^2.
\]
故只需 \(K=10\)。再置 \(u=1+U,\ q=3+Q\)，\(P(10)\) 恰有 105 个 monomials，全部系数严格正，最小系数 1555。因此 \(P>0\)，从而 \(a>0\)。

所以 moving norm field在 actual real place是 real quadratic；fixed field \(\mathbb Q(\sqrt{-\rho})\) 则是 imaginary quadratic。两种 presentation 都与 R7 real solubility 一致。

## 11. Global reciprocity

本轮没有得到 q>1 global contradiction。Hilbert reciprocity只约束 nonzero invariants 的总和；当前没有 theorem 强迫 odd finite ramification pattern。

正确整体 frontier 是
\[
\boxed{-\sigma(2u+1)\Phi\in N_{\mathbb Q(\sqrt{-\rho})/\mathbb Q}}
\]
是否沿全部 actual section成立，而不是 prime list。

## 12. Structural norm facts

在 fixed extension 中 \(R=N(\sqrt{-R})\)，所有 base-field squares都是 norms。并且
\[
N(B+s\sqrt{-R})=B^2+s^2R=4AC,
\]
故 \(AC\) 是一个 exact structural norm。没有证明 \(G,K,G+1,q,u\) individually uniformly属于 norm subgroup。

## 13. Primitive shared-d gate

仅有
\[
(\alpha,d,t,x)\mapsto[\alpha:dt:dx]
\]
中的 shared-d 本身不构成 projective obstruction：任意 rational projective point都可清分母后整体乘任意指定整数 d。真正可能有约束的是 source-defined d、primitive gcd、LOW/UP 和 digit region。

由于 all-actual Brauer split 尚未分类：
\[
\boxed{\text{LATTICE_GATE_STAGE_NOT_TRIGGERED=TRUE}}.
\]

## 14. R4/R5 regression

在 horizontal Brauer ramification 层：
\[
\boxed{R4:0/8,\qquad R5:0/7}.
\]
旧 determinant tubes 是 coefficient-cancellation/local-model shadows，不是 conic rational-solubility 的 fundamental horizontal ramification divisors。specialization 到 \(\mathbb Q\) 后，codimension-2/vertical arithmetic 仍可能影响 Hilbert invariants；这里不夸大为“所有旧 local arithmetic 永久无关”。

## 15. q=1 specialization

\[
R_1=4X^4+12X^3+13X^2+6X-1,
\]
\[
A_{1,1}=50X^3+115X^2+100X+31,
\]
\[
\Xi_1=R_1-4\lambda^2X^4(X+1)^2.
\]
generic:
\[
\boxed{\beta|_{q=1}=(-R_1,-A_{1,1}(2X+3)\Xi_1)}.
\]
Brauer class本身不退化；q=1 的 \(\alpha=0\) 仍是额外 source chart stratum。

## 16. Fourteen direct answers

1. YES，\(w^2-4az^2=\Delta_B\) exact。  
2. prompt presentation 是 \(F(\sqrt a)\)；更强 fixed presentation 是 \(F(\sqrt{-R})\)。  
3. YES，rational solubility iff one quaternion/Brauer class splits。  
4. YES，与 ternary even Clifford class exact一致。  
5. \([a]=[4\lambda^2(X+1)^2f^2-X(2X+q+2)C]\)。  
6. \([\Delta_B]=[-\Xi]\)。  
7. moving \(F(\sqrt a)\) 依赖 \(\lambda\)；但同一 class 有 fixed \(F(\sqrt{-R})\)，\(\lambda\) 只进 target。  
8. R7 nonconstant safe factors中只有 1 个 horizontal factor \(\Xi\) 真正 ramified。  
9. affine horizontal true ramification components = 1。  
10. YES，cyclotomic pullback 变成 \((-\rho,-\sigma(2u+1)\Phi)\)。  
11. NO finite parity collapse；但 multiplicative exponent parity coordinates 已消失，剩余是 \(\Phi\) 的 genuine additive dependence。  
12. NO，global reciprocity尚不给 q>1 contradiction。  
13. YES，若 Brauer split，剩余才是 source-defined primitive/digit lattice embedding。  
14. YES，frontier 可写为
\[
\boxed{\text{one fixed norm-torus torsor}+\text{one ramification divisor }V(\Phi)+\text{one primitive lattice gate}}.
\]

## Final status

\[
\boxed{\textbf{J2 OPEN}}.
\]

下一轮不应回到 prime/tube/cell；最自然对象是
\[
\boxed{V(\Phi)\times\{uq=X+1\}}
\]
的整体 arithmetic intersection，以及
\[
N_{\mathbb Q(\sqrt{-\rho})/\mathbb Q}(\xi)=-\sigma(2u+1)\Phi
\]
与 primitive digit lattice image 的交。
