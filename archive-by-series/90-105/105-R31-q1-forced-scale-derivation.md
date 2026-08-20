# 105-R31 — q=1 Forced-Scale Derivation

**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R31  
**Status:** exact symbolic derivation + scoped exact counterexample search; no global q=1 extinction theorem is claimed.

## 1. Frozen definitions recovered

From the frozen R30 TC3 shell, for one fixed legal post-support architecture,

\[
Z_-=
\max\!\left(
\left\lceil\frac{10^{m_2-1}}A\right\rceil,
\left\lceil\frac{10^{m_3-1}}W\right\rceil
\right),
\]

\[
Z_+=
\min\!\left(
\left\lfloor\frac{10^{m_2}-1}A\right\rfloor,
\left\lfloor\frac{10^{m_3}-1}W\right\rfloor
\right),
\]

\[
Q_- = \left\lceil\frac{Z_-}{\Lambda}\right\rceil,
\qquad
Q_+ = \left\lfloor\frac{Z_+}{\Lambda}\right\rfloor,
\]

\[
\Lambda=\operatorname{lcm}(\mu,\lambda_z),\quad
\mu=\frac{g_1^*}{g_0},\quad
\lambda_z=\frac{10^{n_3}}{\gcd(10^{n_3},W(Q_0-P_3))},
\]

\[
F=\operatorname{rad}\!\left(\frac{P_1}{g_1^*}C_2C_3\right),
\qquad z=\Lambda q,
\qquad (q,F)=1.
\]

R30 also proved that the decontented source fibre is independent of the residual denominator \(q\); residual \(q\) enters TC4 only through \((U,q)=1\).

## 2. Exact unit-denominator theorem

Because \(Z_-,Z_+,\Lambda\) are positive integers,

\[
1\in[Q_-,Q_+]
\iff Q_-=1\text{ and }Q_+\ge1.
\]

Moreover,

\[
\left\lceil\frac{Z_-}{\Lambda}\right\rceil=1
\iff Z_-\le\Lambda,
\]

and

\[
\left\lfloor\frac{Z_+}{\Lambda}\right\rfloor\ge1
\iff \Lambda\le Z_+.
\]

Therefore

\[
\boxed{
q=1\text{ is TC3-admissible}
\iff
Z_-\le\Lambda\le Z_+.
}
\tag{R31-Q1}
\]

Equivalently, the four exact digit inequalities are

\[
10^{m_2-1}\le A\Lambda\le10^{m_2}-1,
\]

\[
10^{m_3-1}\le W\Lambda\le10^{m_3}-1.
\]

A cleared two-function form is

\[
L_\Lambda:=\max(10^{m_2-1}-A\Lambda,\ 10^{m_3-1}-W\Lambda)\le0,
\]

\[
R_\Lambda:=\min(10^{m_2}-1-A\Lambda,\ 10^{m_3}-1-W\Lambda)\ge0.
\]

This is an exact forced-scale statement, not a ratio approximation.

## 3. Universal multiplicative width theorem

Each individual decimal block satisfies

\[
\left\lfloor\frac{10^m-1}{A}\right\rfloor
<10\left\lceil\frac{10^{m-1}}A\right\rceil.
\]

Taking an intersection can only decrease the upper endpoint and increase the lower endpoint. Hence, whenever the \(Z\)-window is nonempty,

\[
\boxed{Z_+<10Z_-.}
\]

If the residual q-window is nonempty,

\[
\boxed{
\Gamma_q:=\frac{Q_+}{Q_-}<10.
}
\tag{R31-GAMMA}
\]

Since \(Q_\pm\in\mathbb Z\), this gives \(Q_+\le10Q_--1\). In the unit chamber \(Q_-=1\), necessarily \(1\le Q_+\le9\).

## 4. Full opening of the q-independent source set

On a regular completed source stratum, R8 gives the real interval

\[
I_{23}=[L,R),
\]

\[
L=\max\left(\frac{10^{n_2-1}}{C_2},\frac{10^{n_3-1}}{C_3}\right),
\qquad
R=\min\left(\frac{10^{n_2}}{C_2},\frac{10^{n_3}}{C_3}\right).
\]

The equivalent closed integer block bounds are

\[
U_{\rm lo}=\max\left(
\left\lceil\frac{10^{n_2-1}}{C_2}\right\rceil,
\left\lceil\frac{10^{n_3-1}}{C_3}\right\rceil
\right),
\]

\[
U_{\rm hi}=\min\left(
\left\lfloor\frac{10^{n_2}-1}{C_2}\right\rfloor,
\left\lfloor\frac{10^{n_3}-1}{C_3}\right\rfloor
\right).
\]

Let the frozen chart-native periodic selector be \(U\bmod P_0\in\mathcal R_0\). Let

\[
V_0=\Lambda u_0AW.
\]

Then the exact R30 q-independent source set is

\[
\boxed{
\mathcal U_0=
\{U\in\mathbb Z_{>0}:U_{\rm lo}\le U\le U_{\rm hi},\ U\bmod P_0\in\mathcal R_0,\ (U,V_0)=1,\ \mathsf{SrcComp}(U)\},
}
\]

where \(\mathsf{SrcComp}\) denotes the already-frozen source-completed/PSDG cell predicates. In generic completed strata R8 proves \(h_U=1\), so the source-native progression contributes no extra step; chart-local exceptional source strata keep their own frozen finite-index progression and strict-boundary correction.

Equivalently define

\[
M_U^{\rm rad}=\operatorname{lcm}(P_0,\operatorname{rad}(V_0)),
\]

\[
\mathcal R_{\rm adm}=
\{r\bmod M_U^{\rm rad}:r\bmod P_0\in\mathcal R_0,\ (r,V_0)=1\}.
\]

For a closed lower endpoint,

\[
U_{\min}=
\min_{r\in\mathcal R_{\rm adm}}
\left[r+M_U^{\rm rad}
\left\lceil\frac{\max(L,1)-r}{M_U^{\rm rad}}\right\rceil\right],
\]

with the frozen strict-lower correction on open decorated branches. Then \(\mathcal U_0\ne\varnothing\iff U_{\min}<R\), together with the frozen source-completed predicate.

**Notation firewall.** The historical chart label formerly called `q=1` in R2/R8 is a source-chart label, not the R15 residual denominator q. Its affine progression must not be imported into every residual-q=1 architecture.

## 5. U=1 exact iff

On a generic regular completed stratum, \(U=1\) automatically satisfies every coprimality condition. Its digit-room condition is exactly

\[
\boxed{
10^{n_2-1}\le C_2\le10^{n_2}-1,
\qquad
10^{n_3-1}\le C_3\le10^{n_3}-1,
}
\tag{R31-U1}
\]

plus the fixed chart-native completed-source predicate. Thus `U=1 automatic` is false globally, but its arithmetic test is completely explicit.

For residual \(q=1\), if any \(U\in\mathcal U_0\) exists then

\[
(1,FU)=1
\]

and therefore

\[
\boxed{Q_-=1\ \&\ \mathcal U_0\ne\varnothing\Longrightarrow N_{30}>0.}
\]

Conversely, in the unit chamber \(Q_-=1\) with nonempty q-window, q=1 is available, so

\[
\boxed{N_{30}>0\iff\mathcal U_0\ne\varnothing.}
\tag{R31-UNIT-DECISION}
\]

This is stronger than merely saying q=1 is dangerous: in the entire unit chamber, the prime cover disappears and the terminal decision is purely source-fibre nonemptiness.

## 6. q=1 denominator specialization

Set q=1. Then

\[
z=\Lambda,\qquad
V=V_0=\Lambda u_0AW,
\]

\[
b_2=\Lambda A,\qquad b_3=\Lambda W,
\qquad b_1=\frac{\Lambda u_0AW}{g_1^*}.
\]

The tail divisibility is already absorbed because \(\lambda_z\mid\Lambda\). The Smith conditions become exactly

\[
(\Lambda A,C_2)=1,
\qquad
(\Lambda W,C_3)=1,
\]

with the frozen shape gcds. No extra q-content remains.

## 7. q=1, U=1: exact F11 reconstruction equation

Let

\[
X=10^m,\quad Y=10^n,\quad G=10^g,\quad K=10^k,
\]

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3.
\]

Define

\[
L=AWu_0XYGK,
\]

\[
B=g_1^*(W+AYG)+AWu_0XYG,
\]

\[
C=g_1^*(WP_3+AYP_2).
\]

The frozen TC1 normal form is exactly the linear relation

\[
\boxed{LP_1=BQ_0-C.}
\]

Substitution into the primitive sphere equation yields the single quadratic

\[
\boxed{
F_{11}(Q_0):=(B^2-L^2)Q_0^2-2BCQ_0+C^2+L^2(P_2^2+P_3^2)=0.
}
\tag{R31-F11}
\]

Its discriminant factors as

\[
\Delta_{11}=4L^2\Big(C^2+(L^2-B^2)(P_2^2+P_3^2)\Big).
\]

This is the exact architecture-first generator used in R31: enumerate the finite digit blocks forced by q=1 and prescribed U, demand a nonnegative square discriminant, reconstruct \(Q_0,P_1\), then replay primitive/master/tail/Smith. It is a search generator, not a new global discriminant obstruction; on an actual TC1+sphere point the square is tautologically witnessed.

## 8. TC2 audit under q=1

TC2/source-room itself does not contain the residual q. Therefore q=1 does not turn TC2 into a new equality. Its effect is indirect: q=1 forces \(A\Lambda\) and \(W\Lambda\) into their denominator digit blocks, after which the source carrier \((C_2,C_3)\) must still admit an integer U in the independent numerator digit room.

The complete R28 corpus up to \(Q_0\le3000\) shows exactly this collision: every raw-TC1 q=1 forced-scale hit has \(U_{\rm lo}=1>0=U_{\rm hi}\).

## 9. Exact bounded theorem and active falsification search

R28's complete E27 search through \(Q_0\le3000\) contains 37 raw TC1 hits. R31 exact replay finds exactly **7** satisfying (R31-Q1). They are:

`20:120:123:173`, `48:436:75:445`, `120:900:691:1141`, `140:1240:491:1341`, `230:330:1593:1643`, `288:2584:585:2665`, `298:2514:1485:2935`.

All seven have first failure `POSITIVE_RADIAL_BOX`; all seven satisfy

\[
U_{\rm lo}=1>0=U_{\rm hi}.
\]

Hence

```text
Q1_FORCED_SCALE_SOURCE_COLLISION_Q0_LE_3000=PROVED
```

This is a complete-in-bound theorem because R27 already proved every full survivor lies in E27 and R28 completely enumerated E27 raw-TC1 incidence in that height range. It is not promoted to an unbounded theorem.

R31 also ran architecture-first exact reverse searches using (R31-F11), so the machine lane was not merely a replay of the old packet-height census:

- `Q1_U1_TO_U3_L8_K1`: 350,723 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.
- `Q1_U1_L8_K2`: 3,230,116 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.
- `SMALL_Q_U1_L6_K1`: 380,912 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.

No search scope produced even an integer TC1-conic solution. These are exact finite classifications of the stated architecture boxes only.

## 10. q=1 verdict

```text
Q1_EXACT_FORCED_SCALE_EQUIVALENCE=PROVED
UNIT_CHAMBER_N30_IFF_U0_NONEMPTY=PROVED
Q1_SOURCE_COLLISION_Q0_LE_3000=PROVED
Q1_FORCED_SCALE_EXTINCTION_GLOBAL=NOT_PROVED_NOT_FALSIFIED
GENUINE_POST_SUPPORT_Q1_ARCHITECTURE_FOUND=NO
```

The global missing theorem in the unit chamber is now literally:

\[
\boxed{
Q_-=1\Longrightarrow\mathcal U_0=\varnothing
}
\]

on every legal post-support architecture. No weaker prime-cover statement is relevant there.
