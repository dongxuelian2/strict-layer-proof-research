# Fourth 85 · R1 — Lemma Package

## Lemma 1 — q>1 Sparse Recoordinate and N0 Return

在 central regular q>1 negative J2 chart，设
\[
G=10^g,\quad K=10^k,\quad uq=G+1,\quad A=2u+1,\quad B=2G+q,\quad H=G/2.
\]
由
\[
h=qHz-Ac,\qquad m=Ah-Gz
\]
及 \(qA-B=2\) 得
\[
\boxed{m=BH z-A^2c}.
\]
并且 legal image 上
\[
\boxed{z=\frac{2(m+A^2c)}{BG}},\qquad
\boxed{w=\frac{Gm-Ac}{B}},\qquad
\boxed{d_2=\frac{G^2m+c}{B}}.
\]
故该变换不降维。

若
\[
N_0=4u^2G^2K^2-(GA+1)^2+2,
\]
则 root square condition 等价于
\[
Q_{mc}(m,c)=(2BY)^2,
\]
其中
\[
Q_{mc}=G^2(N_0-1)m^2+2G(4GK^2u^2-A)mc+(4K^2u^2-GA^3(GA+2))c^2.
\]
其判别式为
\[
\boxed{\operatorname{disc}(Q_{mc})=(2GA(GA+1))^2N_0}.
\]
因此该 sparse elimination 的 square-class 精确返回 old \(N_0\)。

---

## Lemma 2 — q=1 Negative Decimal-Defect Lemma

固定历史 q=1 negative case \((K,d,\tau)\)，其中 \(K=10^k\), \(g-k\ge2\), \(G=10^g\)，且
\[
M=G^3\tau-(10G^2+4G-2)a<0.
\]
定义
\[
\boxed{\rho=a-\frac{\tau G}{10}}.
\]
则
\[
\boxed{M<0\iff\rho>0}.
\]
又由 DCDC
\[
31a+\tau\equiv0\pmod{2K}
\]
及 \(2K\mid G/10\)，有
\[
\boxed{31\rho+\tau\equiv0\pmod{2K}}.
\]
并且
\[
\gcd(\rho,10)=1,\qquad \gcd(\rho,\tau)=1,
\]
以及 source upper window
\[
\boxed{0<\rho<\frac{10-d\tau}{10d}G}.
\]

---

## Lemma 3 — q=1 Exact Decimal Valuation Signature

在 Lemma 2 的条件下，再假设 R15 fixed-\(\tau\) conic：
\[
Y_0^2=A_2(G,K)a^2+B_1(G,K,\tau)a+C_0(G,K,\tau).
\]
则 exact expansion 与 DCDC coefficient audit 给
\[
\boxed{v_2(Y_0^2-(2K\rho)^2)=g+2k+2},
\]
\[
\boxed{v_5(Y_0^2-(2K\rho)^2)=g+2k-1}.
\]
因此
\[
\boxed{v_2(Y_0)=k+1,\qquad v_5(Y_0)=k}.
\]
写
\[
\boxed{Y_0=2Ky},
\]
则 \(y\) 是 ten-unit，且
\[
\boxed{v_2(y^2-\rho^2)=g},
\qquad
\boxed{v_5(y^2-\rho^2)=g-1}.
\]
故存在 ten-unit \(\eta\) 使
\[
\boxed{(y-\rho)(y+\rho)=\frac G5\eta},
\]
并且
\[
\boxed{\eta\equiv\rho\tau\pmod{10}}.
\]
最终：
\[
\{v_2(y-\rho),v_2(y+\rho)\}=\{1,g-1\},
\]
\[
\{v_5(y-\rho),v_5(y+\rho)\}=\{0,g-1\}.
\]
所以只有四个 \((2,5)\)-valuation allocation branches。
