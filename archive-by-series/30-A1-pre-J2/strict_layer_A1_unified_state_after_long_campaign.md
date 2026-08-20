# A1 Unified State After Long Campaign

**Scope:** Strict Layer, `A1-only`.  
**Status:**

\[
\boxed{DD=\varnothing,\qquad A_1\text{ OPEN}.}
\]

## 1. Minimal semantic witness

\[
\boxed{(P_1,P_2,P_3,Q_0;U,V),\qquad\gcd(U,V)=1}
\]

with

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

Recover

\[
g_i=\gcd(V,P_i),
\quad C_i=P_i/g_i,
\quad a_i=UC_i,
\quad b_i=V/g_i.
\]

Full master:

\[
V\mathbf A^\sharp=Q_0\mathbf B.
\]

Backward WGF / phase / Gaussian / norm data are derived only.

## 2. Exponent normal form

\[
g=m_3-n_3\ge0,
\qquad
k\ge1,
\qquad
d=m_2-g,
\]

\[
\boxed{m_2=g+d,\quad n_2=2g+k+d,\quad m_3=n_3+g.}
\]

For \(g\ge1\):

\[
\text{plus}\Rightarrow d\le1,
\qquad
\text{minus}\Rightarrow d\ge-1.
\]

## 3. Axis gap

\[
\Theta=Q_0-P_2,
\qquad
\Theta(2Q_0-\Theta)=P_1^2+P_3^2.
\]

Let

\[
r_1=10^kP_1/Q_0=1+\varepsilon/b_1,
\]

\[
r_3=10^{2g+k}P_3/Q_0.
\]

Then

\[
\boxed{
10^{2k}\Theta/Q_0
=
\frac{r_1^2+10^{-4g}r_3^2}{1+P_2/Q_0}.
}
\]

For \(g\ge1\):

\[
\boxed{1/2<10^{2k}\Theta/Q_0<2.532.}
\]

Hence

\[
\Theta\asymp Q_0 10^{-2k}.
\]

Bounded \(\Theta\) is equivalent to

\[
k\ge\frac12\log_{10}Q_0-O(1).
\]

This lower critical bound is **OPEN**.

## 4. Unified decimal defect

\[
D=P_1 10^k-Q_0>0,
\]

\[
\boxed{\Omega=b_2Q_0-b_1 10^{m_2}D\ne0.}
\]

Define

\[
\boxed{\tau_3=b_3(Q_0-P_3)/10^{n_3}\in\mathbf Z_{>0}.}
\]

Then exact master becomes

\[
\boxed{b_2P_2-\tau_3=10^g\Omega.}
\]

Also

\[
\boxed{\Omega/Q_0=\beta_2(P_2/Q_0)10^d-\beta_3(1-P_3/Q_0).}
\]

plus \(\iff\Omega<0\), minus \(\iff\Omega>0\).

## 5. Common integer radial gate

\[
I_{23}
=
\left[\frac{10^{n_2-1}}{C_2},\frac{10^{n_2}}{C_2}\right)
\cap
\left[\frac{10^{n_3-1}}{C_3},\frac{10^{n_3}}{C_3}\right)
=[L,R).
\]

Exact terminal condition:

\[
\boxed{N_V(L,R)>0}
\]

or equivalently

\[
\boxed{\operatorname{next}_V(L)<R.}
\]

## 6. Sharp Integer Radial Margin

Any integer common \(U\) implies

\[
\boxed{10^{n_3}C_2-10^{n_2-1}C_3\ge C_2,}
\]

\[
\boxed{10^{n_2}C_3-10^{n_3-1}C_2\ge C_3.}
\]

Sharp; equality forces \(U=1\).  
But margin alone is insufficient: a known synchronized real-cone point satisfies both margins while \(I_{23}\subset(0,1)\).

## 7. Small-shift gcd

Let

\[
d_Q=\gcd(Q_0,V),
\qquad g_2=\gcd(P_2,V).
\]

Then

\[
\boxed{\gcd(d_Q,g_2)\mid\Theta,}
\]

\[
\boxed{d_Qg_2\le V\Theta,}
\]

\[
\boxed{d_Q\le b_2\Theta.}
\]

Potentially decisive only after bounded \(\Theta\) or a new lower bound on \(d_Q/b_2\).

## 8. Backward tail normalization

\[
\varepsilon^\sharp
=
\frac{b_3(Q_0-P_3)}{10^{n_3}d_Q}.
\]

Exact natural scale:

\[
\boxed{
\frac{\varepsilon^\sharp}{10^g(Q_0/d_Q)}
=\beta_3(1-P_3/Q_0).
}
\]

For \(g\ge1\), this lies in \((0.09,1)\).

## 9. Killed routes

- primitive/master alone \(\Rightarrow\Theta=O(1)\): **false**;
- integer radial margin alone: **insufficient**;
- pure \(\varepsilon\)-vs-\(\beta_2\) rational spacing: **insufficient**;
- direct quantitative fixed-profile upgrade: **insufficient**;
- generic \(2/5\) phase overload: **not uniform**;
- bare Pythagorean/Gaussian axis parametrization: **no new radial information**.

## 10. Exact frontier

### Terminal theorem

For every synchronized primitive A1 state in the quantized-defect normal form, prove

\[
\boxed{\operatorname{next}_V(L)\ge R.}
\]

### Highest-leverage intermediate theorem

Prove an absolute \(C\) such that common integer radial feasibility forces

\[
\boxed{k\ge\frac12\log_{10}Q_0-C,}
\]

or equivalently

\[
\boxed{\Theta=O(1).}
\]

## 11. Fate of backward line

\[
\boxed{\textbf{ONLY AS DERIVED TOOLKIT}.}
\]

No independent backward A1 program should continue.
