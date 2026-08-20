# 85 第五轮：Pre-Root Independence Firewall × Canonical Root Order Collision × Actual Digit-Window Orientation × Signed Source Affine Mismatch

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Round:** 85-R5  
**Primary target:** \(q>1,\ d_A=1\) regular branch  
**Completion criterion:** \(J=2\Longrightarrow\varnothing\)  
**Status:** **REGULAR J2 STILL OPEN**  
**R5 terminal verdict:** `CANONICAL_ROOT_ORDER_ARCHITECTURE_FAILS`  
**R5 success level:** **R5-S1 achieved; no R5-S3 chamber closure**  
**Exact diagnostic:** `85_R5_order_diagnostic.py`  
**Diagnostic certificate:** `85_R5_order_diagnostic_certificate.txt`

---

# 1. Executive Summary

85-R5 does **not** close any of the three live regular \(q>1\) tail chambers.

The round does, however, answer the central R5 question decisively:

\[
\boxed{
\text{the demanded universal pre-root order collision is false.}
}
\]

The key provenance correction is that the genuinely independent pre-root quadratic should be retained **before DCDC normalization**:

\[
\boxed{
Q_{\rm pre}(X)
=
AH^2X^2-2uKD_2X+\widetilde F,
\qquad
\widetilde F=A\mathcal X^2+ZD_2.
}
\tag{PRQ}
\]

Here all coefficients are reconstructed from source data before one is allowed to assume an actual root \(X=a_1\).

By contrast,

\[
\Omega=\frac{\widetilde F}{2K}\in\mathbb Z
\]

is only available after the DCDC root-necessary sieve.  The inherited dependency certificate explicitly records

```text
DCDC_PRE_ROOT_PROVENANCE=FALSE
DCDC_SAFE_EARLY_SIEVE=TRUE
OMEGA_INTEGER_PRE_ROOT=FALSE
OMEGA_RATIONAL_PRE_ROOT=TRUE
```

so \(\Omega\)-integrality cannot be placed inside the minimal independent pre-root state.

The strongest genuinely source-side information recovered in R5 is the **Source Affine Window Theorem**.  Let

\[
\mu_{\rm src}:=Um
=
\frac{AN+(q+2)Z}{2}>0
\]

be the actual-radialized source coordinate occurring in J2.5.  Then

\[
\boxed{
GKa_1=Aa_2+\mu_{\rm src}.
}
\tag{AFF}
\]

Using the exact second numerator block window

\[
\frac{G^2K}{10}\le a_2<G^2K,
\]

one gets

\[
\boxed{
I_{\rm src}
=
\left[
\frac{AG}{10}+\frac{\mu_{\rm src}}{GK},
\;
AG+\frac{\mu_{\rm src}}{GK}
\right).
}
\tag{SRC-WIN}
\]

This is strictly sharper than the historical lower bound \(a_1>AG/10\).  But the new signed term is only a translation:

\[
\boxed{
|I_{\rm src}|=\frac{9}{10}AG.
}
\tag{SRC-WIDTH}
\]

Thus \(\mu_{\rm src}\) does **not** create a short interval.  It translates a macroscopically wide interval without changing its width.  In particular, integer spacing cannot be the global closure mechanism.

The root geometry is also completely explicit.  Put

\[
a:=AH^2,\qquad b:=uKD_2,\qquad c:=\widetilde F,
\]

\[
\Delta_0=b^2-ac.
\]

If \(\Delta_0\ge0\), both real roots are positive and

\[
r_-+r_+
=
\frac{2uKD_2}{AH^2}
=
\boxed{
\frac{8uD_2}{AL}
},
\]

\[
r_-r_+
=
\frac{\widetilde F}{AH^2}>0,
\]

while the vertex is

\[
\boxed{
X_v
=
\frac{uKD_2}{AH^2}
=
\frac{4uD_2}{AL}.
}
\tag{VERTEX}
\]

Hence the historical upper bound

\[
a_1<\frac{8uD_2}{AL}
\]

is exactly the **sum of the two positive roots**.  It does not select one root and does not itself create a one-sided contradiction.

More strongly, exact reconstruction supplies counterexamples to the universal order-disjointness claim in **all three** tail orientations.  In each displayed example below,

- all pre-root reconstruction and linear/digit gates pass;
- \(d_A=1\);
- \(\gcd(Z,u)=1\);
- the endpoint signs are computed by exact integer arithmetic;
- and
  \[
  Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}),
  \]
  so one real root lies strictly inside the actual source affine window.

Examples:

\[
(q,g,k,\ell,\alpha,t)
=
(11,9,10,8,17260,29)
\]

for high tail,

\[
(7,9,9,9,5781,25)
\]

for boundary, and

\[
(7,9,8,10,137582,25)
\]

for reverse nonzero tail.

The boundary and reverse failure persists even after imposing the root-necessary DCDC sieve.  Explicit DCDC-pass regular primitive examples are

\[
(q,g,k,\ell,\alpha,t)
=
(11,359,359,359,228530,13)
\]

and

\[
(7,9,8,10,337012,25),
\]

respectively, again with

\[
Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}).
\]

Their discriminants are nonsquares, so they are **not actual roots**.  That is precisely the point: they are killed by the original arithmetic root condition, not by real order.  Therefore a universal theorem of the form

\[
I_{\rm root}\cap I_{\rm src}=\varnothing
\]

cannot be the regular closure mechanism.

The exact diagnostic census further gives:

```text
high pre-root, g<=100:
  WINDOW_BETWEEN_ROOTS = 46
  ONE_ROOT_INSIDE      = 12

boundary pre-root, g<=100:
  WINDOW_BETWEEN_ROOTS = 402
  ONE_ROOT_INSIDE      = 88
  WINDOW_RIGHT_BOTH    = 12

reverse pre-root, g<=20:
  WINDOW_BETWEEN_ROOTS = 5950
  ONE_ROOT_INSIDE      = 1300
  WINDOW_RIGHT_BOTH    = 148

boundary post-DCDC, g<=1200:
  WINDOW_BETWEEN_ROOTS = 42
  ONE_ROOT_INSIDE      = 8

reverse post-DCDC, g<=12:
  WINDOW_BETWEEN_ROOTS = 30
  ONE_ROOT_INSIDE      = 7
```

These counts are diagnostics, not global theorems; a single exact counterexample is already enough to falsify the universal order theorem.

Accordingly:

```text
REGULAR_HIGH_TAIL=OPEN
REGULAR_BOUNDARY=OPEN
REGULAR_REVERSE_NONZERO_TAIL=OPEN

R5_TERMINAL_VERDICT=
CANONICAL_ROOT_ORDER_ARCHITECTURE_FAILS
```

No sixth residual/order-sharpening package should be introduced.

---

# 2. R4 Frozen Verdict

R4 is frozen as follows:

```text
J2_STATUS=OPEN
REGULAR_J2_STATUS=OPEN
FORCED_ODD_DIVISOR_DISCOVERY=FAILED
ODD_FACTOR_ALLOCATION=NOT_REACHED
ODD_PRIME_ALLOCATION_ARCHITECTURE=RETIRED
```

The primitive root-factor package is

\[
\Omega^\flat=C_1\lambda^\flat,
\qquad
\lambda^\flat=ud_2-AMC_1,
\]

but R4 also proved that the sphere and third Euclidean identity reconstruct this equality rather than giving an independent second source obstruction.

Thus R5 is forbidden to use full root-containing sphere algebra as a second gate.

---

# 3. Pre-Root Independence Firewall

R5 uses the following rule.

A relation is **PRE_ROOT-compatible** when it can be derived from source reconstruction without assuming that the unknown first block is an actual root of \(Q_{\rm pre}\).

A relation is **ROOT_DERIVED / NON-INDEPENDENT** when its proof already uses the exact root equation, or when the proposed “second source equation” becomes equivalent to the root equation after the rest of the same source chart is restored.

This distinction is stricter than merely asking whether the symbol \(C_1\) appears.

An equation may contain the unknown \(C_1\) and still be PRE_ROOT-compatible, provided it is a source reconstruction equation and does not use \(Q_{\rm pre}(C_1)=0\).

---

# 4. Identity Provenance Table

| identity | contains actual \(C_1/a_1\)? | uses root quadratic? | independent pre-root use? | R5 status |
|---|---:|---:|---:|---|
| \(GKC_1=AC_2+m\) / \(GKa_1=Aa_2+\mu_{\rm src}\) | yes, as unknown | no | yes | **PRE_ROOT-COMPATIBLE** |
| \(H^2C_1^2+w^2=Td_2\) | yes | not by itself | only with firewall caveat | **SOURCE-STRUCTURAL; NOT A SECOND ROOT GATE** |
| \(2uKC_1=AT+z\) | yes | not by itself | only with firewall caveat | **SOURCE-STRUCTURAL; NOT A SECOND ROOT GATE** |
| sphere + third Euclidean identity together | yes | exactly reconstructs root | no | **ROOT-EQUIVALENT PACKAGE** |
| \(\Omega^\flat=C_1\lambda^\flat\) | yes | yes | no | **ROOT_DERIVED** |
| DIG2, DIG3 | no root assumption | no | yes | **PRE_ROOT** |
| \(GKa_1=Aa_2+\mu_{\rm src}\) + DIG2 | unknown only | no | yes | **PRE_ROOT SOURCE WINDOW** |
| \(\gcd(U,V)=1,\ \gcd(A,10)=1\) | no | no | yes | **PRE_ROOT** |
| \(\gcd(C_1,\lambda^\flat)=1\) as root-factor firewall | yes | uses root-factor package | no as a second order gate | **ROOT-LAYER** |
| \(2K\mid\widetilde F\) (DCDC) | no \(C_1\) | root-necessary sieve | not source-independent | **SAFE EARLY SIEVE, NOT PRE_ROOT** |
| \(\Omega=\widetilde F/(2K)\in\mathbb Z\) | no \(C_1\) | depends on DCDC | no | **NOT PRE_ROOT** |

## 4.1 Exact dependency loop

In primitive variables the pre-root quadratic is

\[
Q_{\rm prim}(C_1)
=
AH^2C_1^2
-2uKd_2C_1
+Aw^2+zd_2.
\]

Using the sphere row,

\[
H^2C_1^2+w^2=Td_2,
\]

gives

\[
\begin{aligned}
Q_{\rm prim}(C_1)
&=
A(Td_2-w^2)-2uKd_2C_1+Aw^2+zd_2\\
&=
d_2(AT+z-2uKC_1).
\end{aligned}
\]

Therefore, since \(d_2>0\),

\[
\boxed{
\text{sphere} + Q_{\rm prim}(C_1)=0
\iff
2uKC_1=AT+z.
}
\tag{FIREWALL}
\]

Equivalently,

\[
\boxed{
\text{sphere}+\text{third Euclidean identity}
\Longrightarrow
Q_{\rm prim}(C_1)=0.
}
\]

This is the exact dependency loop R5 was designed to detect.

---

# 5. Minimal Pre-Root State

For the regular \(q>1\) negative J2 branch define

\[
\boxed{
\mathfrak P_{\rm pre}
=
(G,K,L,u,q,N,t;
A,Z,a_3,\mathcal X,D_2,\mu_{\rm src})
}
\]

with

\[
G=10^g,\qquad K=10^k,\qquad L=10^\ell,\qquad KL=G^2,
\]

\[
uq=G+1,\qquad A=2u+1,
\]

and exact RCE reconstruction

\[
Z=\frac{At-2N}{q(q+4)},
\]

\[
a_3=\frac{(G-1)t-qN}{2(q+4)},
\]

\[
\mathcal X=\frac{Z+uN}{2},
\]

\[
D_2=ua_3+G\mathcal X,
\]

\[
\boxed{
\mu_{\rm src}
=
\frac{AN+(q+2)Z}{2}.
}
\]

The live source conditions include positivity, ten-unit conditions, actual DIG3, and the inherited radial inequalities.

For the regular subproblem add

\[
\boxed{d_A=\gcd(A,D_2)=1.}
\]

The unknown first actual numerator block is denoted

\[
X=a_1.
\]

It is **not** an element of \(\mathfrak P_{\rm pre}\) as fixed data.

Neither DCDC nor \(\Omega\in\mathbf Z\) is included in \(\mathfrak P_{\rm pre}\).

---

# 6. Pre-Root Quadratic Theorem

From \(\mathfrak P_{\rm pre}\), define

\[
\widetilde F=A\mathcal X^2+ZD_2.
\]

Then the genuine independent root equation is

\[
\boxed{
Q_{\rm pre}(X)
=
AH^2X^2-2uKD_2X+\widetilde F.
}
\]

A source solution must have

\[
\boxed{
Q_{\rm pre}(a_1)=0.
}
\]

No \(\Omega\)-integrality is needed to write this equation.

If DCDC later passes, division by \(2K\) gives the historically normalized equation, but that is a later root-necessary normalization rather than new pre-root information.

---

# 7. Actual Digit Windows

The exact frozen numerator windows are

\[
\boxed{
\frac{G^2K}{10}\le a_2<G^2K
}
\tag{DIG2}
\]

and

\[
\boxed{
\frac G{10}\le a_3<G.
}
\tag{DIG3}
\]

The historical DRL only retained

\[
a_1>\frac{AG}{10}.
\]

R5 restores the second-block affine term and obtains a two-sided source projection.

It is useful to distinguish:

\[
\boxed{
I_{\rm coarse}^{\rm src}
=
\left(\frac{AG}{10},\infty\right)
}
\]

from the exact affine source window

\[
\boxed{
I_{\rm src}
=
\left[
\frac{AG}{10}+\frac{\mu_{\rm src}}{GK},
\;
AG+\frac{\mu_{\rm src}}{GK}
\right).
}
\]

The old interval

\[
\left(
\frac{AG}{10},
\frac{8uD_2}{AL}
\right)
\]

must **not** be called a pure source window: its lower endpoint is source-digit information while its upper endpoint comes from root complementary-factor positivity.

---

# 8. Signed Affine Remainders

The source coordinate used here is

\[
\boxed{
\mu_{\rm src}
=
\frac{AN+(q+2)Z}{2}.
}
\]

In the live negative source chart it is positive and a ten-unit.

Crucially, it is **not** an Euclidean remainder satisfying

\[
0\le\mu_{\rm src}<A
\]

or any analogous uniform \(O(A)\) bound.

The old source-normal-form variable \(m\) is a positive derived coordinate, not a small residue class representative.  Therefore the hoped-for statement

\[
0<m<A
\]

is unavailable and must not be silently assumed.

Likewise \(Z>0\) is reconstructed exactly, with the inherited radial upper bound

\[
Z
<
\frac{2\eta u}{K}
+
\frac{2uA}{G},
\qquad
\eta=\frac{1299}{500},
\]

but \(Z\) is not a signed affine remainder for J2.5.

Thus the useful R5 sign fact is

\[
\boxed{\mu_{\rm src}>0,}
\]

not “\(\mu_{\rm src}\) is tiny.”

---

# 9. Source Affine Window Theorem

From

\[
GKa_1=Aa_2+\mu_{\rm src}
\]

and DIG2,

\[
\frac{G^2K}{10}\le a_2<G^2K,
\]

one obtains

\[
\boxed{
\frac{AG}{10}
+
\frac{\mu_{\rm src}}{GK}
\le
a_1
<
AG
+
\frac{\mu_{\rm src}}{GK}.
}
\tag{SAW}
\]

This proves the requested signed affine source window.

Its exact width is

\[
\begin{aligned}
|I_{\rm src}|
&=
AG+\frac{\mu_{\rm src}}{GK}
-
\left(
\frac{AG}{10}+\frac{\mu_{\rm src}}{GK}
\right)\\
&=
\boxed{\frac{9}{10}AG}.
\end{aligned}
\]

Therefore the signed affine coordinate cancels from the width.

This yields an exact negative theorem:

> **Signed-Shift Noncompression Theorem.**  
> J2.5 plus the exact second block window changes the *location* of the first-block interval but does not reduce its real width at all.

Since the current live chamber has \(g\ge4\) and \(u>1\), this width is enormous compared with \(1\).  Integer spacing is not a global closure mechanism at this level.

---

# 10. Canonical Root Localization

Write

\[
Q_{\rm pre}(X)=aX^2-2bX+c
\]

with

\[
a=AH^2>0,\qquad
b=uKD_2>0,\qquad
c=\widetilde F>0.
\]

Define

\[
\Delta_0=b^2-ac.
\]

If

\[
\Delta_0<0,
\]

there is no real root and the state dies immediately at root existence.

Assume now

\[
\Delta_0\ge0.
\]

Then both roots are positive because

\[
r_-r_+=\frac ca>0,
\qquad
r_-+r_+=\frac{2b}{a}>0.
\]

Using

\[
H^2=\frac{G^2}{4}=\frac{KL}{4},
\]

one gets

\[
\boxed{
r_-+r_+
=
\frac{8uD_2}{AL}.
}
\tag{ROOT-SUM}
\]

The vertex is

\[
\boxed{
X_v
=
\frac{r_-+r_+}{2}
=
\frac{4uD_2}{AL}.
}
\]

Thus

\[
Q'_{\rm pre}(X)
=
2AH^2(X-X_v).
\]

This provides the exact monotonicity test requested in R5.

---

# 11. Complementary-Factor Ordering

Define algebraically

\[
\Lambda(X)
=
2uKD_2-AH^2X.
\]

Then

\[
Q_{\rm pre}(X)
=
\widetilde F-X\Lambda(X).
\]

At a positive root,

\[
\Lambda(X)=\frac{\widetilde F}{X}>0.
\]

Also, because

\[
r_-+r_+=\frac{2uKD_2}{AH^2},
\]

for a root \(r_i\),

\[
\boxed{
\Lambda(r_i)=AH^2r_j,
\qquad
\{i,j\}=\{-,+\}.
}
\]

Hence **both positive roots automatically have positive complementary factor**.

Therefore

\[
\Lambda>0
\Longrightarrow
X<\frac{8uD_2}{AL}
\]

does not select \(r_-\) versus \(r_+\).  It is a root-sum bound, not a root-order collision theorem.

This is another exact reason why the hoped-for two-line closure

\[
a_1>L_{\rm digit},
\qquad
a_1<U_{\rm root},
\qquad
L_{\rm digit}\ge U_{\rm root}
\]

does not materialize uniformly.

---

# 12. Vertex / Monotonicity Audit

The sign of the derivative on the source interval is determined by the position of

\[
X_v=\frac{4uD_2}{AL}.
\]

Three regimes occur:

1. \(U_{\rm src}\le X_v\): \(Q_{\rm pre}\) decreases across the source interval.
2. \(L_{\rm src}\ge X_v\): \(Q_{\rm pre}\) increases across the source interval.
3. \(L_{\rm src}<X_v<U_{\rm src}\): the source interval crosses the vertex.

The exact diagnostics show that regime 3 occurs abundantly, while regime 2 also occurs.

Thus no uniform derivative sign survives on the whole actual source window.

---

# 13. Endpoint Sign Analysis

To avoid radicals, put

\[
Y=GKX.
\]

The affine source endpoints become the integers

\[
\boxed{
Y_L
=
\frac{AG^2K}{10}
+
\mu_{\rm src},
}
\]

\[
\boxed{
Y_U
=
AG^2K+\mu_{\rm src}.
}
\]

Define the scaled exact endpoint polynomial

\[
\boxed{
\mathcal E(Y)
:=
(GK)^2Q_{\rm pre}\!\left(\frac{Y}{GK}\right)
}
\]

so that

\[
\mathcal E(Y)
=
AH^2Y^2
-2uKD_2(GK)Y
+\widetilde F(GK)^2.
\]

Then

\[
\operatorname{sgn}Q_{\rm pre}(L_{\rm src})
=
\operatorname{sgn}\mathcal E(Y_L),
\]

\[
\operatorname{sgn}Q_{\rm pre}(U_{\rm src})
=
\operatorname{sgn}\mathcal E(Y_U).
\]

This is the exact integer endpoint test used in the R5 certificate.

## 13.1 Uniform sign factorization is impossible

The requested ideal outcome would be a factorization proving, for example,

\[
\mathcal E(Y_L)>0,\qquad
\mathcal E(Y_U)>0
\]

throughout the regular source class.

Exact legal pre-root states instead realize

\[
\boxed{
\mathcal E(Y_L)<0<\mathcal E(Y_U),
}
\]

and other states realize

\[
\mathcal E(Y_L)<0,\qquad
\mathcal E(Y_U)<0.
\]

Therefore no factorization into already-frozen uniformly positive factors can exist for both endpoints on the full regular pre-root class.

Any future symbolic factorization must contain a genuinely sign-changing source factor; it cannot be a hidden universal closure.

---

# 14. Positive-Chamber Transfer Audit

The historically successful positive closure must be described accurately.

The archived positive proof did **not** close by merely comparing

\[
a_1>\frac{AG}{10}
\]

with the generic positivity upper bound on a root.

Its decisive splice was

\[
a_1>\frac{AG}{10}
\]

plus a **forced decimal-core lower bound on the complementary factor**

\[
\Lambda\ge\frac{H^2}{5},
\]

which yielded

\[
\widetilde F=a_1\Lambda>\frac{AG^3}{200},
\]

and this contradicted the positive radial upper bound

\[
\widetilde F<3Au^2.
\]

Thus the successful mechanism was

\[
\boxed{
\text{digit lower}
+
\text{forced complementary-factor capacity}
+
\text{radial product upper}.
}
\]

For the current live negative deficiency chamber \(\ell\ge6\), the generic decimal core is only

\[
2K=\frac{2G^2}{L}.
\]

Compare:

\[
\frac{H^2/5}{2K}
=
\frac{G^2/20}{2G^2/L}
=
\boxed{\frac{L}{40}}.
\]

The positive proof therefore possessed a complementary-factor lower load larger by the enormous factor \(L/40\).

This loss is not a missing \(\pm1\) or a coarse inequality.  It is **Type E structural slack**.

A second positive advantage was the much sharper radial geometry

\[
0<W<u,
\qquad
\widetilde F<3Au^2,
\]

which does not survive in the same form in the regular negative chamber.

### Positive-to-Regular Transfer Ledger

| ingredient | positive chamber | regular negative live chamber | transfer |
|---|---|---|---|
| second-digit DRL \(a_1>AG/10\) | yes | yes | **SURVIVES** |
| signed affine sharpening | not needed | \(\mu_{\rm src}>0\) | **NEW but only translates window** |
| complementary factor \(>0\) | yes | yes | **SURVIVES but weak** |
| forced factor core \(H^2/5\) | yes | no | **FAILS** |
| live generic core | \(H^2/5\) scale | \(2K=2G^2/L\) | **loses \(L/40\)** |
| strong radial upper \(\widetilde F<3Au^2\) | yes | no | **FAILS** |
| pure order disjointness | not the actual closure | false in R5 diagnostics | **FAILS** |

---

# 15. High-Tail Analysis

For \(\delta>0\), the requested uniform PRE_ROOT order theorem is false.

An exact pre-root witness is

\[
\boxed{
(q,g,k,\ell,\alpha,t)
=
(11,9,10,8,17260,29).
}
\]

Its reconstructed data include

\[
N=58526331,
\]

\[
u=90909091,\qquad
A=181818183,
\]

\[
\mu_{\rm src}=5320575783140621,
\]

and it satisfies

\[
d_A=1,\qquad
\gcd(Z,u)=1.
\]

Exact endpoint arithmetic gives

\[
Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}).
\]

Thus one real root is strictly inside \(I_{\rm src}\).

For orientation, normalized by \(AG\),

\[
\frac{L_{\rm src}}{AG}
=
0.100000000000000000002926\ldots,
\]

\[
\frac{r_+}{AG}
=
0.58526332590336005035\ldots,
\]

\[
\frac{U_{\rm src}}{AG}
=
1.000000000000000000002926\ldots.
\]

The overlap has macroscopic clearance.

This state fails DCDC, but DCDC is not PRE_ROOT-independent.  Hence it is a valid falsifier of the R5 theorem **as formulated under the Pre-Root Independence Firewall**.

No claim is made that high tail is impossible to attack after adding later root-necessary sieves.  R5 proves only that pure PRE_ROOT order collision does not close it.

Therefore:

```text
REGULAR_HIGH_TAIL=OPEN
PRE_ROOT_HIGH_ORDER_THEOREM=FALSE
```

---

# 16. Boundary Analysis

The boundary order theorem fails even after DCDC.

A compact pre-root witness is

\[
(q,g,k,\ell,\alpha,t)
=
(7,9,9,9,5781,25),
\]

with

\[
Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}).
\]

More decisively, a DCDC-pass regular primitive witness is

\[
\boxed{
(q,g,k,\ell,\alpha,t)
=
(11,359,359,359,228530,13).
}
\]

It satisfies

\[
d_A=1,
\qquad
\gcd(Z,u)=1,
\qquad
2K\mid\widetilde F,
\]

yet again

\[
\boxed{
Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}).
}
\]

Its large root lies at approximately

\[
\frac{r_+}{AG}
=
0.77491438065850598487\ldots
\]

while the source affine interval is essentially

\[
[0.1AG,1.0AG).
\]

The discriminant is not a square.  The state dies at the arithmetic root layer, not at order.

The exact historical DCDC census through \(g\le1200\), after filtering to primitive regular states, is

```text
WINDOW_BETWEEN_ROOTS = 42
ONE_ROOT_INSIDE      = 8
```

Therefore:

```text
REGULAR_BOUNDARY=OPEN
BOUNDARY_ORDER_DISJOINTNESS_EVEN_AFTER_DCDC=FALSE
```

No boundary endpoint equality theorem is reached because genuine strict interior overlap already exists.

---

# 17. Reverse Nonzero-Tail Analysis

Reverse zero-tail remains closed/retired and is not reopened.

For reverse nonzero tail, pure order is again false.

A pre-root witness is

\[
(q,g,k,\ell,\alpha,t)
=
(7,9,8,10,137582,25),
\]

with

\[
Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}).
\]

A stronger DCDC-pass regular primitive witness is

\[
\boxed{
(q,g,k,\ell,\alpha,t)
=
(7,9,8,10,337012,25).
}
\]

Its reconstructed values include

\[
N=2602409267,
\]

\[
u=142857143,\qquad
A=285714287,
\]

\[
\mu_{\rm src}=371772754214810813.
\]

Again

\[
d_A=1,\qquad
\gcd(Z,u)=1,\qquad
2K\mid\widetilde F,
\]

and exactly

\[
Q_{\rm pre}(L_{\rm src})<0<Q_{\rm pre}(U_{\rm src}).
\]

The exact DCDC diagnostic for \(g\le12\) gives

```text
WINDOW_BETWEEN_ROOTS = 30
ONE_ROOT_INSIDE      = 7
```

after primitive regular filtering.

Therefore:

```text
REGULAR_REVERSE_NONZERO_TAIL=OPEN
REVERSE_ORDER_DISJOINTNESS_EVEN_AFTER_DCDC=FALSE
```

---

# 18. Integer-Spacing and Congruence Tie-Breaker Audit

The exact source affine width is

\[
\frac{9}{10}AG.
\]

Thus the hoped-for terminal form

\[
n<a_1<n+1
\]

does not arise from the pre-root source affine theorem.

The explicit one-root-inside witnesses have overlap on a fixed positive fraction of the \(AG\)-scale.  This is not an \(O(1)\) gap that a residue class can repair.

Consequently the canonical congruence

\[
a_1^2\equiv Z^2\pmod u
\]

remains useful as a later arithmetic root sieve, but **not** as an interval tie-breaker after R5.

Reopening CRT/carry purely to exploit a macroscopic real overlap would violate the R2/R3 retirement decisions.

---

# 19. Computational Reconnaissance

The exact script

```text
85_R5_order_diagnostic.py
```

reconstructs states from the frozen tail/RCE equations and uses only integer/Fraction arithmetic for all gate and endpoint-sign decisions.

The endpoint test is performed through

\[
\mathcal E(Y)
=
(GK)^2Q_{\rm pre}(Y/(GK)),
\]

at the integer endpoints \(Y_L,Y_U\).

The certificate records

```text
FLOAT_GATE_DECISIONS=0
CERTIFICATE_STATUS=PASS
```

and the exact censuses quoted above.

The normalized decimal root locations printed in this report are for orientation only; no proof decision uses them.

---

# 20. Counterexamples

The following table is sufficient to falsify a universal R5 order theorem.

| chamber | \(q,g,k,\ell,\alpha,t\) | DCDC | \(d_A\) | \(\gcd(Z,u)\) | endpoint signs | result |
|---|---|---:|---:|---:|---|---|
| high | \(11,9,10,8,17260,29\) | no | 1 | 1 | \(-,+\) | real root inside \(I_{\rm src}\) |
| boundary | \(7,9,9,9,5781,25\) | no | 1 | 1 | \(-,+\) | real root inside |
| reverse | \(7,9,8,10,137582,25\) | no | 1 | 1 | \(-,+\) | real root inside |
| boundary | \(11,359,359,359,228530,13\) | **yes** | 1 | 1 | \(-,+\) | real root inside even after DCDC |
| reverse | \(7,9,8,10,337012,25\) | **yes** | 1 | 1 | \(-,+\) | real root inside even after DCDC |

Every listed discriminant is nonsquare.

Thus these are not source solutions; they are exact **architecture counterexamples** showing that order is not what kills them.

---

# 21. Proven vs Computational Claims

## PROVED

1. Minimal PRE_ROOT state can be chosen without integer \(\Omega\).
2. The independent pre-root quadratic is \(Q_{\rm pre}\) in (PRQ).
3. J2.5 plus DIG2 gives the exact Source Affine Window Theorem (SAW).
4. \(|I_{\rm src}|=9AG/10\).
5. The signed source coordinate translates but does not narrow \(I_{\rm src}\).
6. Root sum and vertex are exactly
   \[
   r_-+r_+=8uD_2/(AL),
   \qquad
   X_v=4uD_2/(AL).
   \]
7. Both positive roots have positive complementary factor.
8. Sphere + third Euclidean identity reconstruct the root quadratic and are not an independent two-gate package.
9. Therefore the full root-containing sphere package cannot be reused as a second independent obstruction.

## EXACT COMPUTATIONAL FALSIFICATION

1. There exist legal PRE_ROOT regular states in high, boundary, and reverse nonzero tail with one real root strictly inside \(I_{\rm src}\).
2. There exist boundary and reverse regular primitive DCDC-pass states with one real root strictly inside \(I_{\rm src}\).
3. The cited diagnostics use exact endpoint signs, not floating comparisons.

## NOT PROVED

1. No uniform theorem that every DCDC-pass high-tail state has a root inside \(I_{\rm src}\).
2. No claim that the displayed nonsquare states can be promoted to actual roots.
3. No claim that every possible future source-image refinement fails.
4. No singular \(d_A>1\) statement is made.

---

# 22. Regular Closure Table

| regular branch | R5 status | reason |
|---|---|---|
| \(d_A=1,\ \delta>0\) | **OPEN** | universal PRE_ROOT order collision falsified |
| \(d_A=1,\ \delta=0,\ q>1\) | **OPEN** | order collision falsified even after DCDC |
| \(d_A=1,\ \delta<0,\ q>1\) | **OPEN** | nonzero-tail order collision falsified even after DCDC |

No regular tail chamber is closed in R5.

---

# 23. Retired / Active Information-Class Register after R5

| information class | status after R5 |
|---|---|
| floor/carry | **RETIRED** |
| source-cut as second residual gate | **RETIRED** |
| \(2/5\)-capacity | **RETIRED** |
| odd-prime allocation | **RETIRED** |
| full root-containing sphere algebra | **ROOT-EQUIVALENT / NON-INDEPENDENT** |
| pre-root digit/order | **VALID INFORMATION, FAILED AS UNIFORM CLOSURE ENGINE** |
| signed affine source coordinate | **VALID PRE_ROOT IDENTITY, FAILED AS INTERVAL-COMPRESSION ENGINE** |
| integer spacing / congruence tie-breaker | **NOT ACTIVATED: overlap is macroscopic** |
| singular \(d_A>1\) | **UNTOUCHED** |

The identities in the two “FAILED” rows remain valid bookkeeping; what is retired is the **order-collision closure architecture** built from them.

---

# 24. R5 Terminal Verdict

The strongest accurate verdict is

```text
J2_STATUS=OPEN
REGULAR_J2_STATUS=OPEN

PRE_ROOT_FIREWALL=PROVED
MINIMAL_PRE_ROOT_STATE=RECOVERED
PRE_ROOT_QUADRATIC=PROVED
SOURCE_AFFINE_WINDOW=PROVED
SIGNED_SHIFT_NONCOMPRESSION=PROVED
CANONICAL_ROOT_GEOMETRY=PROVED

HIGH_ORDER_DISJOINTNESS=FALSE_AT_PRE_ROOT_LEVEL
BOUNDARY_ORDER_DISJOINTNESS=FALSE_EVEN_AFTER_DCDC
REVERSE_NONZERO_ORDER_DISJOINTNESS=FALSE_EVEN_AFTER_DCDC

ONE_REGULAR_CHAMBER_CLOSED=NO

R5_TERMINAL_VERDICT=
CANONICAL_ROOT_ORDER_ARCHITECTURE_FAILS
```

This is not merely

```text
PRE_ROOT_WINDOW_RECOVERED_BUT_NO_COLLISION
```

because the universal collision theorem is positively falsified by exact states with a root strictly inside the sharp source window.

---

# 25. R6 Attack Target

Because regular J2 remains open, R6 must **not** move to singular \(d_A>1\).

Because R1–R5 have now retired residual/carry/source-cut/\(2,5\)/odd-prime/root-factor/order packaging, R6 must change interface.

The recommended target is

\[
\boxed{
\textbf{N0 Actual Split-Family Source Image}
\times
\textbf{Pre-Radial Full-Word Mantissa Glue}.
}
\]

Concretely:

1. retreat to the full numerator/denominator concatenation state **before** the first-block variable is collapsed into the root coordinate;
2. retain exact leading-block sandwich / unit mantissa defect and common-\(U\) realization;
3. intersect that source image with the already-frozen actual \(N_0\) split family;
4. forbid any return to \(x\)-residual, carry, source-cut residual, factor support, or real-root order sharpening.

The new question should be:

\[
\boxed{
\text{Can an actual split }N_0\text{ fibre lie in the full-word/common-scale source image?}
}
\]

This is a genuinely different information interface: it asks about the **image of the original decimal word before root localization**, rather than extracting another consequence after a root candidate has already been built.

---

# 26. Artifact Audit

Generated:

```text
85_R5_PreRoot_Order_Collision_and_Digit_Window.md
85_R5_order_diagnostic.py
85_R5_order_diagnostic_certificate.txt
```

The separate first-five-round checkpoint is generated as

```text
85_R1_R5_First_Five_Round_Closure_Checkpoint.md
```

No J2 closure certificate is generated because

\[
\boxed{J2\text{ remains OPEN}.}
\]
