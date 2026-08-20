# A1-SRUS State After Resonance / Transition Campaign

## Status

\[
\boxed{DD=\varnothing,\qquad A_1\ \mathrm{OPEN}.}
\]

Strict Layer 未闭合。

## Frozen SRUS

\[
C_2=M/u_0,\qquad C_3=N/u_0,
\]

\[
\frac U{u_0}\in K_{MN},\qquad \gcd(U,V)=1.
\]

## Resonance

\[
R=0\Rightarrow d=0,\ \alpha=t=1,\ v=10^{n_3},\ n_2=2g+k.
\]

\[
P_2=10^{n_3}M,\qquad P_3=N,
\]

\[
S_R=P_2+P_3-Q_0=JZ\ne0,
\qquad J=L_R>1.
\]

\[
10^gH=b_2S_R.
\]

### NEW — sign / face compression

令 \(\kappa=k-2g\)。

\[
\boxed{
\begin{array}{c|c|c}
 & \text{Face A} & \text{Face B}\\
\hline
\text{plus} & \kappa\le0 & \kappa\le1\\
\text{minus} & \kappa\ge-1 & \kappa\ge0
\end{array}}
\]

plus + Face A 且 \(b_1\ge3\) 时：

\[
\boxed{\kappa\le-1.}
\]

### NEW — integer face margin

Face A integer survivor：

\[
\boxed{
10^{-n_2}\le\frac{P_3}{P_2}
\le10^{1-n_2}(1-10^{-n_3}).
}
\]

Face B integer survivor：

\[
\boxed{
\frac1{10(10^{n_2}-1)}
\le\frac{P_3}{P_2}<10^{-n_2}.
}
\]

### NEW — reduced-denominator gcd overload

\[
\boxed{
u10^{2g}D=\beta(10^gQ_0-S_R),\qquad \gcd(u,\beta)=1.}
\]

令

\[
h_R=\gcd(10^{2g}D,10^gQ_0-S_R).
\]

则

\[
\boxed{
u=(10^gQ_0-S_R)/h_R,\quad \beta=10^{2g}D/h_R,}
\]

并因 \(b_2=s\beta<10^g\)：

\[
\boxed{h_R>10^gD.}
\]

### NEW — integerized resonance mantissa

存在整数 \(c_R\) 使

\[
\boxed{b_2=10^g c_R/J,\quad S_R=JZ,\quad H=c_RZ,}
\]

且

\[
\boxed{\lceil J/10\rceil\le c_R\le J-1.}
\]

所以 fixed \(J\) 后 denominator mantissa 为有限 ordinary-integer states。

### NEW — two-sided Farey margin

除 lower-endpoint equality exceptions 外：

\[
\boxed{
u_0\mathcal G_A\ge M\gcd(N,10^{n_3})+N\gcd(M,10^{n_2-1})}
\]

或

\[
\boxed{
u_0\mathcal G_B\ge N\gcd(M,10^{n_2})+M\gcd(N,10^{n_3-1}).}
\]

### NEW — exact center

若

\[
\Omega=N10^{n_2}-M10^{n_3}=0,
\]

则

\[
\boxed{n_2\ge n_3.}
\]

若 \(n_2>n_3\)，则

\[
\boxed{J=10^g.}
\]

### Endpoint equality

third lower equality只有：

\[
\boxed{n_3=1,\ U=C_3=1.}
\]

second lower equality强迫：

\[
\boxed{U=1,\ C_2=10^{n_2-1}.}
\]

## Transition frozen identity

\[
\boxed{S_3=\alpha Jh_T^\sharp q-M\widehat R,}
\]

\[
\boxed{Q_0=\alpha t(M10^{n_3}+N)-\alpha Jh_T^\sharp q.}
\]

固定 q 并不会 uniform 地固定 normalized \(M/N\) conic；仍需额外 scale theorem。

## Current exact frontiers

1. **Resonant Boundary-Margin + GCD-Overload Exclusion**；
2. **d=0 Transition Affine Boundary-Margin Exclusion**；
3. **d=1 Transition Affine Boundary-Margin Exclusion**。

Layer P 尚无必要展开，因为尚未严格发现 genuine C+I survivor只死于 transverse unit condition。
