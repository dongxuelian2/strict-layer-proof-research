# J2-65-R7 — Veronese Pullback × Projective Two-Quadric Pencil × Power-of-Ten Fibre × Completed-Square Norm Form

**Scope:** Strict Layer — A1-only — Exact Resonance R=0 — J=2  
**Round:** 65 第七轮 / A1 统一终端线第三十二轮  
**Status:** **J2 OPEN**

## Executive verdict

本轮完成再次升维回收，并额外得到两个全局关闭：

\[
\boxed{q>1\text{ Case Z CLOSED}},\qquad
\boxed{\text{all actual singular conic fibres CLOSED}}.
\]

因此 q>1 只剩 **smooth power-of-ten conic fibres**。

## 1. Veronese pullback / 4+2 block

令 \(T=dt,\ Y=dx,\ \mathbf v=(\alpha,T,Y)^T\)。从 R2 source definitions exact 重建 \(Q_{\rm sat}\)，再按 R6 抽取两行后：

\[
P=A\alpha^2+B\alpha T+CT^2+DY^2,\qquad S=E\alpha Y+FTY.
\]

所以
\[
M_P=\begin{pmatrix}A&B/2&0\\B/2&C&0\\0&0&D\end{pmatrix},\quad
M_S=\begin{pmatrix}0&0&E/2\\0&0&F/2\\E/2&F/2&0\end{pmatrix}.
\]

`VERONESE_BLOCK_SEPARATION=PROVED`，且 \(M_S\) generic rank 2。

## 2. Reducible S-row

精确地
\[
S=-4q^2(X+1)(q+4)c\,Y\,[Xe(X,q)\alpha+f(X,q)T],
\]
其中 \(e=X^2(q+4)+2X-q\)。这把 R6 的固定 \(X+1\) 因子解释成 reducible pencil member 的 coefficient degeneration。

## 3. Projective map and H removal

P,S 对 \(\mathbf v\) 都是二次齐次式，故
\[
\phi_{q,X}:[\mathbf v]\mapsto[-P:S]
\]
不依赖 common scale。Case NZ 的 \(GP+KS=0\) 给
\[
\boxed{\phi_{q,G}([\alpha:T:Y])=[K:G]}.
\]
因此 raw gcd H 只属于最后 integral lifting，不属于 projective fibre geometry。

## 4. One conic pencil

\[
\mathcal Q_{U,V}=UP+VS.
\]
Case Z 是 base locus \(P=S=0\)；Case NZ 是 power-of-ten target fibre。两者统一成 one pencil。

## 5. Exact discriminant

定义
\[
R(X,q)=4X^4+4X^3q+8X^3+X^2q^2+8X^2q+4X^2+2Xq^2+4Xq-q^2.
\]

精确地
\[
\det(UM_P+VM_S)=UXq^6(X+1)^2(q+4)^4(2X+q+2)c^4
[U^2R-4V^2X^4(X+1)^2].
\]

所以 affine \(\lambda=V/U\) 下 discriminant 只有
\[
\boxed{R(X,q)-4\lambda^2X^4(X+1)^2},
\]
即 degree 2 且 linear-\(\lambda\) term 为 0。

## 6. Actual singular fibres globally empty

actual singular condition为
\[
R(G,q)=4K^2G^2(G+1)^2.
\]
由 \(uq=G+1\) 得 \(q\le G+1\)。R 对 q 在 \(G\ge1,q\ge0\) 单调增加，并且
\[
R(G,G+1)=(G+1)^2(9G^2+6G-1)<16G^2(G+1)^2.
\]
而 \(k\ge1\Rightarrow K\ge10\)，右边至少 \(400G^2(G+1)^2\)。矛盾。

因此所有 actual Case NZ fibres 都 smooth。

## 7. Real signature

\(M_P\) positive definite；actual pencil的 top-left \(2\times2\) block不随 target 改变，而 full determinant严格为负。因此
\[
\boxed{\operatorname{signature}=(2,1)}.
\]
real place 对 actual orbit 自动 soluble。

## 8. Case Z closes directly

q>1 actual 有 \(Y>0,\alpha\ne0\)。S=0 唯一固定 \(r=T/\alpha=-Xe/f\)。代回 P=0：
\[
\boxed{(Y/\alpha)^2=-X^4(X+1)^2/(q^2f^2)<0}.
\]
所以 q>1 Case Z CLOSED。

## 9. L_row / W_row de-fundamentalization

R6 的 \(L_{\rm row}=0\) projective ratio exact 对应 common root
\[
\boxed{X=-(q+2)/2}.
\]
因此它是 negative-X base-alignment shadow，不是 actual \(G>0\) component。

\(W_{\rm row}\) 是低次 base system 消去 X 后的 projection shadow；direct positive-X base locus已空：

`W_ROW_FUNDAMENTAL=FALSE`。

## 10. Completed-square norm form

q>1 chart 中 \(r=T/\alpha, y=Y/\alpha, \lambda=K/G=10^\delta\)：
\[
A(r)+Dy^2+\lambda yL(r)=0
\]
化为
\[
\boxed{(2Dy+\lambda L(r))^2=\lambda^2L(r)^2-4DA(r)}.
\]

且
\[
\boxed{\Delta_{\rm bin}=-64D\det(M_P+\lambda M_S)}.
\]
所以 binary norm discriminant 与 conic determinant 是同一个 invariant。

## 11. Universal rational section

`UNIVERSAL_RATIONAL_SECTION=FALSE`。若 generic \(F(\lambda)\)-conic（\(F=\mathbb Q(q,X)\)）有 rational point，properness 允许 specialization 到 \(\lambda=0\)；但该 fibre 是 positive-definite P=0，在 \(q>0,X>0\) ordering 下 anisotropic，矛盾。

## 12. Hasse–Minkowski finite bad-prime support

任一 smooth rational specialization primitive-integralize 后，odd prime p 若不整除 primitive content 与 determinant，则 mod p 是 nondegenerate ternary quadratic form；其在 \(F_p\) 上 isotropic，且 smooth point Hensel lift 到 \(\mathbb Q_p\)。

故只需有限 bad-prime support。一个安全 over-inclusive divisor：
\[
\mathfrak D_{\rm bad}=2GKq(G+1)(q+4)(2G+q+2)c\,\Xi,
\]
\[
\Xi=R(G,q)-4K^2G^2(G+1)^2\ne0.
\]
完整 symbolic Hilbert classification 尚未完成；没有 prime hunt / residue ladder。

## 13. q=1

同一 pencil/discriminant generic 不退化。差别仅是 \(\alpha=0\) 仍为 additional projective stratum，所以 q>1 的 affine chart不能覆盖全部 q=1。本轮不进入 Pell/norm orbit。

## 14. Q1--Q14 direct answers

1. YES，exact ternary forms存在。  
2. YES，Case Z/NZ = one pencil 的 base locus/fibres。  
3. YES，raw H 从 projective frontier删除。  
4. YES，strict 4+2 block separation。  
5. YES，S-row reducible，generic rank 2。  
6. total cubic；affine target degree 2 且只含 \(\lambda^2\)。  
7. actual power-of-ten target与 singular discriminant无交；所有 actual NZ fibres smooth。  
8. YES，且 q>1 Case Z CLOSED。  
9. \(L_{\rm row}\) 是 negative-X shadow；\(W_{\rm row}\) 是 elimination shadow。  
10. YES，one binary norm form。  
11. universal rational section = FALSE。  
12. finite bad-prime support由 2、primitive content、determinant divisor控制。  
13. actual admissible sector 与 rational smooth fibre的交仍未被排除；real place自动可解，剩余 obstruction在 finite bad primes + primitive shared-d lattice + actual sector。  
14. YES。q>1 frontier已成为
\[
\boxed{\text{one smooth power-of-ten conic bundle}+\text{finite bad-prime/discriminant geometry}+\text{primitive lattice gate}}.
\]

## Final status

\[
\boxed{\textbf{J2 OPEN}}.
\]

但 Case Z 与 singular fibres均已永久退出。下一轮优先：
\[
\boxed{\textbf{Norm-Class / Hilbert-Symbol Geometry}\times\textbf{Power-of-Ten Orbit}\times\textbf{Primitive shared-d lattice gate}}.
\]
