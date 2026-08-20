# 105-R30 — TC3 / TC4 Exact Definitions Recovery

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R30  
**Purpose:** recover the authoritative TC3/TC4 definitions before any elimination; no formula in this file is inferred from chat summary.

---

## 1. Authoritative provenance

The exact TC3 formulas are inherited from:

- `105_R15_Master_G1_Z_Shell_Phase_Offensive.md`;
- `105_R15_Z_Shell_Normalization.csv`;
- `105_R15_Q_Successor_Registry.csv`.

The exact TC4 formulas are inherited from:

- `105_R8_Common_U_Integer_Source_Fibre.md`;
- `105_R2_Source_Section_Internalization.md` for the historical source-chart `q_src=1` affine progression;
- `105_R3_Source_Completed_Valuation_Atlas.md` for the same source-completed semantics.

`105-R26-stage-archive.md` is the authoritative carrier-only wrapper that invokes TC1--TC4 and defines the finite predicate \(\mathcal C_{26}\).

**Notation firewall.** R15 uses the letter \(q\) for the residual transverse denominator integer in
\(z=\Lambda q\). R8/R2 historical files also contain a *different* structural source-chart label historically called `q=1`. In R30 that old label is always written
\(q_{\rm src}=1\). The two variables are not identified.

---

# Part A — TC3 exact recovery

## 2. Master/tail/Smith shell

For a fixed finite shape, set

\[
M_0=u_0AW,
\qquad
g_0=\gcd(M_0,P_1).
\]

The exact master gcd corridor is

\[
 g_0\mid g_1^*\mid P_1.
\]

When it holds, define

\[
\mu=\frac{g_1^*}{g_0},
\qquad
R_1=\frac{P_1}{g_1^*}.
\]

The exact gcd shell is

\[
\gcd(M_0z,P_1)=g_1^*
\iff
z=\mu q_0,\quad \gcd(q_0,R_1)=1.
\]

Let

\[
Y=10^{n_3},
\qquad
T_3=Q_0-P_3,
\]

and define the tail scale

\[
\lambda_z=\frac{Y}{\gcd(Y,WT_3)}.
\]

Then

\[
\tau=\frac{\lambda_z}{\gcd(\lambda_z,\mu)},
\qquad
\Lambda=\operatorname{lcm}(\mu,\lambda_z)=\mu\tau.
\]

The fixed-shape compatibility checks are

\[
\gcd(A,C_2)=1,
\qquad
\gcd(W,C_3)=1,
\]

\[
\gcd(\tau,R_1)=1,
\qquad
\gcd(\Lambda,C_2C_3)=1.
\]

Once these hold, define the canonical forbidden factor

\[
\boxed{
F=\operatorname{rad}(R_1C_2C_3)
=\operatorname{rad}\!\left(\frac{P_1}{g_1^*}C_2C_3\right).
}
\]

Then the raw simultaneous master/tail/Smith \(z\)-shell is exactly

\[
\boxed{
z=\Lambda q,
\qquad
\gcd(q,F)=1.
}
\tag{TC3-shell}
\]

No parity or hidden congruence is left outside this formula at the R15 shell level; the prime-support conditions have been absorbed into \(\Lambda\), \(F\), and the four compatibility checks above.

## 3. Exact integer \(z\)-window

The two denominator block-length conditions are

\[
10^{m_2-1}\le zA<10^{m_2},
\qquad
10^{m_3-1}\le zW<10^{m_3}.
\]

Because \(z\in\mathbb Z_{>0}\), define exact integer endpoints

\[
\boxed{
Z_-=
\max\!\left(
\left\lceil\frac{10^{m_2-1}}A\right\rceil,
\left\lceil\frac{10^{m_3-1}}W\right\rceil
\right),
}
\]

\[
\boxed{
Z_+=
\min\!\left(
\left\lfloor\frac{10^{m_2}-1}{A}\right\rfloor,
\left\lfloor\frac{10^{m_3}-1}{W}\right\rfloor
\right).
}
\]

The `-1` in the two upper numerators is the exact conversion of the strict decimal upper bounds to an integer inequality.

## 4. Exact residual \(q\)-window

Substitute \(z=\Lambda q\). Then

\[
\boxed{
Q_-:=\left\lceil\frac{Z_-}{\Lambda}\right\rceil,
\qquad
Q_+:=\left\lfloor\frac{Z_+}{\Lambda}\right\rfloor.
}
\]

Therefore TC3 is exactly

\[
\boxed{
Q_-\le q\le Q_+,
\qquad
\gcd(q,F)=1,
\qquad q\in\mathbb Z_{>0}.
}
\tag{TC3}
\]

The canonical TC3 successor is

\[
q_{\min}^{(F)}
:=\min\{q\ge Q_-:\gcd(q,F)=1\},
\]

with the exact criterion

\[
\boxed{
TC3\iff q_{\min}^{(F)}\le Q_+.
}
\]

Since \(Q_-,Q_+\) are already integers,

\[
\boxed{
\lceil Q_-\rceil=Q_-;
\qquad
\lfloor Q_+\rfloor=Q_+.
}
\]

The raw integer candidate count before the coprimality sieve is therefore

\[
\boxed{
N_{q,\rm raw}=\max(0,Q_+-Q_-+1).
}
\]

There is no additional real-to-integer ambiguity at TC3 after \(Q_\pm\) have been formed.

---

# Part B — TC4 exact recovery

## 5. Fixed source-completed profile and radial coordinate

For each frozen post-PSDG source-completed profile, the source fibre has rank one and the radial integer is

\[
\boxed{U=\gcd(a_1,a_2,a_3)\in\mathbb Z_{>0}.}
\]

The primitive source condition is

\[
\boxed{\gcd(U,V)=1.}
\]

The block-2 and block-3 radial intervals are

\[
L_i=\frac{10^{n_i-1}}{C_i},
\qquad
R_i=\frac{10^{n_i}}{C_i}=10L_i,
\qquad i=2,3.
\]

For regular source-completed strata,

\[
\boxed{
L=\max(L_2,L_3),
\qquad
R_{\rm src}=\min(R_2,R_3),
\qquad
I_{23}=[L,R_{\rm src}).
}
\]

There are only two regular active faces:

### Face A

If \(L_2\ge L_3\), then

\[
[L,R_{\rm src})=[L_2,R_3),
\]

\[
G_A=C_2\,10^{n_3}-C_3\,10^{n_2-1}.
\]

### Face B

If \(L_3>L_2\), then

\[
[L,R_{\rm src})=[L_3,R_2),
\]

\[
G_B=C_3\,10^{n_2}-C_2\,10^{n_3-1}.
\]

## 6. Generic source progression

On generic / non-\(q_{\rm src}=1\) completed strata the source progression is the full integer lattice:

\[
\boxed{h_U=1.}
\]

Thus before coprimality the canonical integer successor is simply

\[
U_{\mathbb Z}=\max(1,\lceil L\rceil)=\lceil L\rceil
\]

for the positive regular intervals under consideration.

## 7. Historical \(q_{\rm src}=1\) decorated source stratum

The old historical source-chart `q=1` branch must retain its extra *open* real interval

\[
\boxed{
\frac{d_q\tau_{\rm src}G}{10C_3}<U<\frac{G}{C_3}.
}
\tag{Q1-window}
\]

Its exact affine source congruence is

\[
\boxed{
31C_3U+d_q\tau_{\rm src}\equiv0\pmod{2Kd_q}.
}
\tag{Q1-cong}
\]

Put

\[
N_q=2Kd_q,
\qquad
d_U=\gcd(C_3,N_q).
\]

Because \(31\) is a unit modulo the historical \(N_q\), solvability is equivalent to

\[
\boxed{d_U\mid d_q\tau_{\rm src}.}
\]

If solvable, the affine lattice has step

\[
\boxed{
h_U=\frac{2Kd_q}{d_U}
=\frac{2Kd_q}{\gcd(C_3,2Kd_q)}
}
\]

and unique residue

\[
\boxed{
U\equiv r_{q1}\pmod{h_U},
}
\]

where

\[
\boxed{
r_{q1}
\equiv
-\frac{d_q\tau_{\rm src}}{d_U}
\left(\frac{31C_3}{d_U}\right)^{-1}
\pmod{h_U}.
}
\]

If the historical predicate \(\gcd(\rho,10\tau_{\rm src})=1\) is active, with

\[
\rho(U)=\frac{UC_3}{d_q}-\frac{\tau_{\rm src}G}{10},
\]

it induces an additional finite period in the progression parameter. It is part of the frozen fixed-source selector; it is not a second free radial coordinate.

## 8. Canonical residue selector and successor

Write the fixed source-native affine/periodic part of a completed source profile as a finite residue set

\[
\mathcal R_0\subseteq\mathbb Z/P_0\mathbb Z.
\]

For the literal R8 representation, after including primitive coprimality \(\gcd(U,V)=1\), one may take

\[
M_U=\operatorname{lcm}(P_0,V)
\]

and

\[
\mathcal R_{\rm adm}
=
\{r\bmod M_U:
 r\bmod P_0\in\mathcal R_0,
 \gcd(r,V)=1\}.
\]

In the simplest generic source chart \(P_0=1\), this reduces to

\[
M_U=V,
\qquad
\mathcal R_{\rm adm}=(\mathbb Z/V\mathbb Z)^\times.
\]

For a regular closed lower endpoint define

\[
\ell=\max(L,1)
\]

and for each canonical representative \(0\le r<M_U\),

\[
\boxed{
S_r(L)=
r+M_U\left\lceil\frac{\ell-r}{M_U}\right\rceil.
}
\]

Then

\[
\boxed{
U_{\min}=\min_{r\in\mathcal R_{\rm adm}}S_r(L),
}
\]

with \(U_{\min}=+\infty\) if \(\mathcal R_{\rm adm}=\varnothing\).

For a left-open decorated lower endpoint, replace the closed ceiling by the strict successor

\[
r+M_U\left(\left\lfloor\frac{L-r}{M_U}\right\rfloor+1\right).
\]

This is the exact floor/ceiling normalization of the source successor.

Finally TC4 is exactly

\[
\boxed{
TC4\iff U_{\min}<R_{\rm src}.
}
\tag{TC4}
\]

For regular faces this is equivalent to the integer cross-products

\[
\boxed{
C_3J_{{\rm src},2}<G_A,
\quad
J_{{\rm src},2}=C_2U_{\min}-10^{n_2-1}
}
\]

on Face A, and

\[
\boxed{
C_2J_{{\rm src},3}<G_B,
\quad
J_{{\rm src},3}=C_3U_{\min}-10^{n_3-1}
}
\]

on Face B.

---

## 9. Exact semantic conclusion

The exact TC3 object is **not** an arbitrary real denominator window: it is an integer interval \([Q_-,Q_+]\) plus the prime-support sieve \((q,F)=1\).

The exact TC4 object is **not** a black-box function: it is a decorated real source interval, a finite affine/periodic residue selector, primitive coprimality \((U,V)=1\), and the corresponding least arithmetic successor.

R30 may therefore eliminate \(q\) only after preserving both of these exact meanings.
