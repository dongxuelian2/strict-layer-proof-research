# 105-R28 — Exact TC1 Normal Form

## Frozen variables

Let

\[
X=10^m,\qquad Y=10^n,\qquad G=10^g,\qquad K=10^k,
\]

\[
T:=Q_0-P_3,\qquad D:=KP_1-Q_0,\qquad H:=GQ_0-P_2.
\]

The frozen exponent relation is

\[
m+k+g=n+\delta,\qquad m,n,k\ge1,\quad g\ge0.
\]

R26/R27 TC1 is

\[
R_n=G S_{m,\rho},\qquad \rho=m+k,
\]

with

\[
R_n=\frac{Wg_1^*T}{AY}-g_1^*P_2,
\]

\[
S_{m,\rho}=Wu_0P_1XK-Q_0(Wu_0X+g_1^*).
\]

## Cleared primitive integral equation

Multiplying by `A Y` and expanding gives

\[
\boxed{
AWu_0P_1XYGK
-AWu_0Q_0XYG
-Ag_1^*Q_0YG
+Ag_1^*P_2Y
-Wg_1^*(Q_0-P_3)=0.
}
\tag{F-TC1}
\]

Equivalently, with all positive defects exposed,

\[
\boxed{
g_1^*\bigl[WT+AYH\bigr]
=AWu_0XYG D.
}
\tag{PF-TC1}
\]

Since `Q0>P2`, `T>0`, and `G>=1`, one has `H>0`.  Therefore every TC1 solution satisfies

\[
\boxed{D=10^kP_1-Q_0>0.}
\tag{D+}
\]

## Universal decimal exponent ordering

Using `m+k+g=n+delta`, the five expanded powers are

\[
e_1=2n+\delta,
\quad e_2=2n+\delta-k,
\quad e_3=n+g=2n+\delta-m-k,
\quad e_4=n,
\quad e_5=0,
\]

and hence

\[
\boxed{e_1>e_2>e_3\ge e_4>e_5.}
\]

The successive gaps are exactly

\[
\boxed{k,\ m,\ g,\ n.}
\]

Thus there is only one leading cancellation architecture: the first two terms combine to `AWu0XYG D>0`; the middle two combine to `-A g1* Y H<0`; the constant term is `-W g1* T<0`.

## Hyperplane form

Define

\[
\begin{aligned}
c_1&=AWu_0XYGK,\\
c_2&=AYg_1^*,\\
c_3&=Wg_1^*,\\
B&=Wg_1^*+AYGg_1^*+AWu_0XYG.
\end{aligned}
\]

Then TC1 is exactly

\[
\boxed{BQ_0=c_1P_1+c_2P_2+c_3P_3.}
\tag{HYP}
\]

Together with the primitive sphere equation this gives the fixed-architecture conic

\[
\boxed{(c_1P_1+c_2P_2+c_3P_3)^2
=B^2(P_1^2+P_2^2+P_3^2).}
\tag{CONIC}
\]

## Selector-ratio normal form

Primitive selectors force

\[
\boxed{\gcd(g_1^*,u_0)=1.}
\]

Therefore PF-TC1 gives the **reduced fraction identity**

\[
\boxed{
\frac{g_1^*}{u_0}
=
\frac{AWXYG(10^kP_1-Q_0)}{W(Q_0-P_3)+AY(GQ_0-P_2)}
}
\tag{RATIO}
\]

and, after reducing the right-hand fraction to coprime numerator/denominator, those two integers are exactly `g1*` and `u0`.  There is no residual common scale.

## R24-W fusion

R24 uses

\[
J=u_0AXYG D-g_1^*T,
\qquad
N_W=g_1^*AYH.
\]

PF-TC1 is exactly

\[
\boxed{WJ=N_W.}
\]

Hence every TC1 hit automatically has `J>0`, `J|N_W`, and reconstructed `W=N_W/J`; the R24 gates `J_NONPOS`, `W_NONINTEGRAL`, and `W_MISMATCH` are redundant on TC1.

## Post-shape support core

Put

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3.
\]

Then TC1 implies

\[
\boxed{u_0\mid W+A10^{n+g}.}
\tag{U-DIV}
\]

Let

\[
\ell:=\frac{W+A10^{n+g}}{u_0}.
\]

After the R24 shape gcds,

\[
(A,C_2)=(W,C_3)=(A,W)=1,
\]

one obtains

\[
\boxed{(u_0,A)=1,\quad
\gcd(u_0,W)=\gcd(u_0,10^{n+g}),\quad
A\mid g_1^*Q_0.}
\]

Moreover, if `W^(10')` denotes the factor of `W` coprime to 10, then

\[
\boxed{W^{(10')}\mid g_1^*Q_0.}
\]

Because `(u0,P1)=1`, the master gcd simplifies to

\[
g_0=(AW,P_1).
\]

Set

\[
\mu=g_1^*/g_0,\qquad a_0=AW/g_0,
\]

and define the new R28 support core

\[
\Xi:=Q_0\ell-AW(C_3+10^nC_2)
=\frac{W(Q_0-P_3)+A10^n(GQ_0-P_2)}{u_0}.
\]

Then TC1 is exactly

\[
\boxed{
\mu\Xi=a_0\,10^{m+n+g}(10^kP_1-Q_0),
\qquad \Xi>0.
}
\tag{MU-CORE}
\]

A full R24 survivor must additionally satisfy

\[
\boxed{(\mu,C_2C_3)=1.}
\]

This `MU-CORE + mu-Smith + radial box` is the smallest unresolved R28 global incidence after the eliminations above.
