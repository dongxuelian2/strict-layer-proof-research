# A1 SRCU State After Smith-Reduced Campaign

**Scope:** Strict Layer — A1-only  
**Main report:** `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`

---

## 1. Current theorem status

\[
\boxed{DD=\varnothing,\qquad A_1\text{ OPEN}.}
\]

因此：

\[
\boxed{\textbf{Strict Layer 尚未 CLOSED}.}
\]

---

## 2. Frozen exact word state

\[
D=P_110^k-Q_0>0,
\]

\[
H=b_2Q_0-b_110^{m_2}D\ne0,
\]

\[
b_1P_110^{m_2+k}=Q_0Q_{12}-H,
\]

\[
K_3=\frac{b_3(Q_0-P_3)}{10^{n_3}}\in\mathbf Z_{>0},
\]

\[
b_2P_2=10^gH+K_3.
\]

Exponent normal form：

\[
\boxed{
m_2=g+d,
\quad
n_2=2g+k+d,
\quad
m_3=n_3+g.
}
\]

For \(g\ge1\)：

\[
d\le-1\Rightarrow\text{plus},
\qquad
d=0,1\Rightarrow\text{dual-sign},
\qquad
d\ge2\Rightarrow\text{minus}.
\]

---

## 3. Full Smith chart

\[
\boxed{
b_1=s\alpha u,
\quad
b_2=s\alpha\beta t,
\quad
b_3=s\beta v,
}
\]

\[
\gcd(\alpha,\beta)=1,
\qquad
\gcd(u,\beta t)=1,
\qquad
\gcd(\alpha t,v)=1.
\]

Let：

\[
\gamma=\gcd(u,v),
\quad
u=\gamma u_0,
\quad
v=\gamma v_0,
\quad
\gcd(u_0,v_0)=1.
\]

Then：

\[
\boxed{V=s\alpha\beta\gamma u_0tv_0.}
\]

---

## 4. NEW frozen gcd dictionary

\[
\boxed{
g_1=\beta tv_0,
\quad
g_2=u_0v,
\quad
g_3=u_0\alpha t.
}
\]

Hence：

\[
\boxed{u_0=\gcd(g_2,g_3).}
\]

Primitive coordinates：

\[
\boxed{P_2=vM,
\qquad
P_3=\alpha tN.}
\]

Then：

\[
\boxed{u_0\mid M,N.}
\]

and：

\[
\boxed{
C_2=M/u_0,
\qquad
C_3=N/u_0.
}
\]

This is the permanent Smith–radial dictionary.

---

## 5. Radial Normal Form

\[
\tau=\frac{10^{n_3}}{C_3},
\qquad
\rho=\frac{C_210^{n_3}}{C_310^{n_2}}.
\]

\[
\boxed{
I_{23}=\tau J(\rho),
}
\]

\[
J(\rho)=
\left[
\max\left(\frac1{10},\frac1{10\rho}\right),
\min\left(1,\frac1\rho\right)
\right).
\]

Continuous feasibility：

\[
\boxed{0.1<\rho<10.}
\]

Width：

\[
0.1<\rho\le1
\Rightarrow
W=\tau\left(1-\frac1{10\rho}\right),
\]

\[
1\le\rho<10
\Rightarrow
W=\tau\left(\frac1\rho-\frac1{10}\right).
\]

---

## 6. Smith–radial cancellation

Define：

\[
\sigma=\frac{b_3}{b_210^{n_3-d}}
=\frac{g_2}{10^{n_3-d}g_3}
=\frac{v}{\alpha t10^{n_3-d}}.
\]

The pre-cancellation formulas are：

\[
\rho=\frac{P_2}{\sigma10^{2g+k}P_3},
\]

\[
\tau=\frac{10^dg_2}{\sigma P_3}.
\]

After full Smith substitution：

\[
\boxed{
\rho=\frac MN10^{n_3-n_2}
=\frac MN10^{n_3-2g-k-d},
}
\]

\[
\boxed{
\tau=\frac{u_0 10^{n_3}}N.
}
\]

Thus \(v/(\alpha t)\) cancels completely from radial geometry.

**Permanent strategy correction:** do not use \(R\)-sign or \(\sigma\)-position alone to infer a \(\rho\)-boundary.

---

## 7. Canonical SRCU interval

Define：

\[
\boxed{
K_{MN}
=
\left[
\max\left(\frac{10^{n_2-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{n_2}}M,\frac{10^{n_3}}N\right)
\right).
}
\]

Then：

\[
\boxed{I_{23}=u_0K_{MN}.}
\]

A legal common scale is equivalent to：

\[
\boxed{
\frac U{u_0}\in K_{MN},
}
\]

with：

\[
\boxed{
\gcd(U,V)=1.
}
\]

Since \(u_0\mid V\)：

\[
\gcd(U,u_0)=1,
\]

so \(U/u_0\) is a reduced fraction with exact denominator \(u_0\).

Also：

\[
\boxed{
\frac{a_2}{M}
=
\frac{a_3}{N}
=
\frac U{u_0}.
}
\]

---

## 8. Full unit modulus

\[
\boxed{V=s\beta u_0v\alpha t.}
\]

Therefore legal U must satisfy：

\[
\boxed{
\gcd(U,u_0)=1,
\qquad
\gcd(U,s\beta v\alpha t)=1.
}
\]

Interpretation：

\[
\boxed{
\text{radial denominator }u_0
\times
\text{transverse unit sieve }s\beta v\alpha t.
}
\]

---

## 9. Strongest defect divisor

Let：

\[
\delta_\beta=\gcd(\beta,10^{m_3}),
\quad
\beta^\sharp=\beta/\delta_\beta,
\quad
\Lambda_\beta=10^{m_3}/\delta_\beta.
\]

Let：

\[
\delta_v=\gcd(v,\Lambda_\beta),
\quad
v^\sharp=v/\delta_v,
\quad
J=\Lambda_\beta/\delta_v.
\]

Then：

\[
q_H=v^\sharp Z,
\]

\[
tM10^{n_3}-A_3=JZ,
\]

\[
\boxed{H=s\alpha\beta^\sharp v^\sharp Z.}
\]

Define：

\[
h_T=\gcd(tM,A_3),
\qquad
h_T^\sharp=\frac{h_T}{\gcd(h_T,J)}.
\]

Then：

\[
\boxed{h_T^\sharp\mid Z.}
\]

Hence strongest current divisor：

\[
\boxed{
\mathcal M_{\max}
=s\alpha\beta^\sharp v^\sharp h_T^\sharp
\mid H.
}
\]

Define：

\[
\boxed{q=H/\mathcal M_{\max}=Z/h_T^\sharp.}
\]

No uniform bound on q is known.

---

## 10. B3 residual divisor verdict

Cross identity：

\[
C_2b_3P_3=C_3b_2P_2.
\]

Combining with E3 gives：

\[
\boxed{b_3\mid10^{m_3}H.}
\]

Thus：

\[
\boxed{
B_3^\sharp
=\frac{b_3}{\gcd(b_3,10^{m_3})}
\mid H.
}
\]

But：

\[
\boxed{
B_3^\sharp
\mid s\beta^\sharp v^\sharp
\mid \mathcal M_{\max}.
}
\]

So B3DIV is true but redundant relative to the latest iterated Smith divisor.

---

## 11. Smith/GCD duality

For every pair \((i,j)\)：

\[
\boxed{
\gcd(b_i,b_j)\operatorname{lcm}(g_i,g_j)=V.
}
\]

In pair 23：

\[
\boxed{
(s\beta)(u_0v\alpha t)=V.
}
\]

Important limitation：large \(\operatorname{lcm}(g_2,g_3)\) does not itself make the radial interval sparse because \(v,\alpha t\) cancel from endpoints.

---

## 12. Resonance frozen normal form

If：

\[
R=b_210^{n_3}-b_3=0,
\]

then：

\[
\boxed{d=0,\quad\alpha=t=1,\quad v=10^{n_3}.}
\]

Hence：

\[
\boxed{
g_2=u_0 10^{n_3},
\quad
g_3=u_0,
}
\]

\[
\boxed{P_2=10^{n_3}M,
\quad
P_3=N,
}
\]

\[
\boxed{V=s\beta u_0 10^{n_3}.}
\]

and：

\[
\boxed{S_3=P_2+P_3-Q_0=JZ,\qquad J=L_R>1.}
\]

Legal U is a decimal unit and must satisfy：

\[
\frac U{u_0}
\in
\left[
\max\left(\frac{10^{2g+k-1}}M,\frac{10^{n_3-1}}N\right),
\min\left(\frac{10^{2g+k}}M,\frac{10^{n_3}}N\right)
\right).
\]

Resonance remains OPEN.

---

## 13. Transition correction

### d=0

\(R\)-sign determines \(\sigma<1\) or \(>1\), but does **not** determine \(\rho<1\) or \(>1\).

### d=1 plus

\[
\boxed{\sigma>960/101>9.50495}
\]

and latest report gives：

\[
v>0.385\,10^{2k}.
\]

But these factors cancel from：

\[
\rho=\frac MN10^{n_3-(2g+k+1)}.
\]

So the direct near-\(\sigma=10\) radial-boundary route is dead.

### d=1 minus

\[
1\le c\le10.
\]

Smith-rich gives finite \((c,q)\), but not finite radial states.

---

## 14. Fixed-q formula

Let：

\[
Z=h_T^\sharp q.
\]

Then：

\[
\boxed{
\alpha t(M10^{n_3}+N)
=Q_0+\alpha Jh_T^\sharp q.
}
\]

With：

\[
A=\alpha t,
\quad B=v,
\quad T=10^{n_3},
\quad E=\alpha Jh_T^\sharp q,
\]

sphere becomes：

\[
\boxed{
(AMT-E)(AMT+2AN-E)
=P_1^2+B^2M^2.
}
\]

and：

\[
\boxed{
N=
\frac{P_1^2+B^2M^2-(AMT-E)^2}
{2A(AMT-E)}.
}
\]

Finite q is therefore a finite defect offset, not a finite radial state.

---

## 15. Radial failure hierarchy

Use in order：

1. **C:** \(K_{MN}=\varnothing\)；
2. **I:** real interval nonempty but no positive integer U；
3. **P:** integers exist but all fail \(\gcd(U,V)=1\).

Known exact-word regression states currently die as：

\[
\boxed{C/I/C.}
\]

Known infinite \(g=0\) pseudo-family dies at C.

Known exact real-cone point dies at I.

No proved Level-P family is known.

---

## 16. Exact terminal theorem

### A1-SRUS — Smith-Reduced Unit-Successor Exclusion

For every exact synchronized A1 Smith state, prove there is no \(U\in\mathbf Z_{>0}\) such that：

\[
\boxed{
\frac U{u_0}\in K_{MN},
}
\]

and：

\[
\boxed{
\gcd(U,s\beta u_0v\alpha t)=1.
}
\]

This is exactly equivalent to A1-SRCU.

If proved：

\[
\boxed{A_1=\varnothing}
\]

and therefore：

\[
\boxed{\textbf{Strict Layer CLOSED}.}
\]

---

## 17. Next targets — max three

1. **Resonant Reduced-Fraction Unit Exclusion**.
2. **d=0/1 Transition Affine Unit-Successor Exclusion**, controlling \(M/N\), not \(\sigma\).
3. **Smith-poor exact positional unit-cover**, only if genuine Layer-P survivors appear.

---

## 18. Final status

\[
\boxed{
\textbf{A1-SRCU not closed, but fully reduced to A1-SRUS.}
}
\]

The permanent new architecture is：

\[
\boxed{
\text{Double Smith--Euclidean}
\to
(u_0,M,N)
\to
U/u_0\text{ short interval}
\to
V\text{-unit exclusion}.
}
\]
