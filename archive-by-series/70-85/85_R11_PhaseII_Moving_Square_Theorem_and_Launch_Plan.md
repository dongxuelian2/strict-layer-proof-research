# 85-R11 — Phase-II Moving-Square Theorem Extraction × Launch Plan

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 85-R11  
**Purpose:** Extract a standalone Phase-II theorem, falsify its natural strengthenings, and choose one narrow R12 target.

---

# 1. Executive Summary

R11 的最重要校准是：

```text
MOVING_SQUARE_THEOREM_STATUS=
NEEDS_SOURCE_RESTRICTION
```

而不是：

```text
PRIMARY_PHASE_II_TARGET
```

in the unrestricted sense.

原因是：R10 已经构造 live outer base 上的 exact root-compatible integral points satisfying the moving conic/square equation but failing source arithmetic. Therefore：

\[
\boxed{
\text{“moving square equation alone has no solutions” is false.}
}
\]

真正仍可能成立的是：

\[
\boxed{
\textbf{source-restricted moving binary quadratic form does not represent a square}.
}
\]

Phase II should therefore reverse the old hierarchy：

\[
\text{source normal form}
\to
\text{root condition}
\]

becomes：

\[
\boxed{
\text{moving square equation as the main Diophantine object}
}
\]

with source semantics used only as exact arithmetic-domain restrictions.

The unique R12 recommendation is a **square-conditioned source-lift extinction theorem**：  
do not re-study common-\(U\) by itself; impose the moving square and integral root first, then ask whether the remaining primitive/common-\(V\) point can ever admit a legal common-\(U\) digit lift.

---

# 2. Result 5 — Source-Restricted Moving Square Form

Let：

\[
g,k\in\mathbf Z_{>0},
\qquad
G=10^g,\quad K=10^k.
\]

Let \(u>0\) satisfy：

\[
u\mid G+1,
\qquad
q:=\frac{G+1}{u}.
\]

Set：

\[
A=2u+1,
\qquad
B=2G+q,
\qquad
H=\frac G2.
\]

For \(c,z\in\mathbf Z\), define：

\[
\boxed{
W:=G^2z-2uAc,
}
\]

\[
\boxed{
D:=GW+2uc.
}
\]

Then：

\[
w=\frac W2,
\qquad
d_2=\frac D2.
\]

Define the moving binary quadratic form：

\[
\boxed{
\mathscr Q_{g,k,u}(c,z)
:=
4u^2K^2D^2
-
AG^2(AW^2+2zD).
}
\]

The full-root square condition is：

\[
\boxed{
\mathscr Q_{g,k,u}(c,z)=16Y^2.
}
\tag{MS}
\]

Equivalently：

\[
\widehat\Delta(c,z):=16\Delta_0
=
\mathscr Q_{g,k,u}(c,z).
\]

This is the standalone arithmetic core of Phase II.

---

# 3. Result 11 — Binary Quadratic Form Standardization

Write：

\[
\widehat\Delta(c,z)
=
\alpha c^2+\beta cz+\gamma z^2.
\]

With：

\[
N_0
=
4u^2G^2K^2-(GA+1)^2+2,
\]

the coefficients are：

\[
\boxed{
\alpha
=
4u^2\left(
4K^2u^2(GA-1)^2-G^2A^4
\right),
}
\]

\[
\boxed{
\beta
=
-4G^2u
\left(
AN_0+GA^2-4GK^2u^2
\right),
}
\]

\[
\boxed{
\gamma=G^4(N_0-1).
}
\]

Hence：

\[
\boxed{
\beta^2-4\alpha\gamma
=
(4G^2uA)^2N_0.
}
\tag{DISC}
\]

Therefore：

\[
\boxed{
[\disc(\widehat\Delta)]=[N_0].
}
\]

This has two consequences.

First：

\[
\boxed{
\text{the moving-square family is genuinely a family of binary quadratic forms}.
}
\]

Second：

\[
\boxed{
\text{its ordinary square-class invariant is not new; it is precisely the old }N_0.
}
\]

So Phase II must attack **source-restricted representation**, not merely classify the underlying quadratic field/form class.

---

# 4. Minimal Source Restrictions

R11 evidence shows that outer data and the square equation alone are insufficient.

For the current central regular \(q>1\) shell, the minimal plausible theorem should retain three genuinely source-sensitive ingredients.

## 4.1 Integral root / source-lattice reconstruction

Given a square witness \(Y\), require：

\[
\exists\sigma\in\{\pm1\}
\]

such that：

\[
\boxed{
C_1=
\frac{uKd_2+\sigma Y}{AH^2}
\in\mathbf Z_{>0},
}
\]

and：

\[
\boxed{
\lambda=\frac{2KC_1-Bz}{A}
\in\mathbf Z_{>0}.
}
\]

Then set：

\[
C_2=Ac+H\lambda,
\qquad
T=Gz+u\lambda.
\]

This is necessary because ambient square points need not lie on the source lattice.

## 4.2 Primitive / common-\(V\) reducedness

At minimum retain：

\[
\boxed{
\gcd(C_1,u)=1,
}
\]

\[
\boxed{
\gcd(C_2,H)=1,
}
\]

\[
\boxed{
\gcd(c,GH)=1.
}
\]

These are precisely the conditions violated by the live R10 root-compatible pseudo-point.

The full Version A additionally retains：

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

## 4.3 Actual common-\(U\) decimal realization

Define：

\[
V=uGH,
\]

\[
U_{\rm lo}
=
\max\left(
\left\lceil\frac{G^2K}{10C_2}\right\rceil,
\left\lceil\frac G{10c}\right\rceil,
1
\right),
\]

\[
U_{\rm hi}
=
\min\left(
\left\lfloor\frac{G^2K-1}{C_2}\right\rfloor,
\left\lfloor\frac{G-1}{c}\right\rfloor
\right).
\]

Require：

\[
\boxed{
\exists U\in[U_{\rm lo},U_{\rm hi}]\cap\mathbf Z_{>0}
:
\gcd(U,V)=1.
}
\tag{SRC-U}
\]

This is the exact radial digit lift.

R7 proves common-\(U\) alone is not a universal killer.  
R12 must therefore study it **conditioned on the square and integral root**.

---

# 5. Result 6 — Candidate Phase-II Main Theorem, Version A

## Theorem A — Full Source-Restricted Moving-Square Nonrepresentation

Let：

\[
g\ge4,\qquad
k\ge1,\qquad
\ell:=2g-k\ge6,
\]

\[
G=10^g,\qquad K=10^k.
\]

Let：

\[
u>1,\qquad
u\mid G+1,
\qquad
q=\frac{G+1}{u}>1,
\]

\[
A=2u+1,\qquad
\gcd(A,10)=1,
\qquad
H=G/2.
\]

Assume the current audited regular negative branch conditions, including：

\[
\gcd(A,d_2)=1
\]

and the exact R9 source orientation/positivity predicates.

For positive integers \(c,z,Y\), define：

\[
W=G^2z-2uAc,
\]

\[
D=GW+2uc,
\]

\[
\mathscr Q_{g,k,u}(c,z)
=
4u^2K^2D^2
-
AG^2(AW^2+2zD).
\]

Assume all exact source predicates：

\[
\mathcal C_{\rm integrality},
\quad
\mathcal C_{\rm primitive},
\quad
\mathcal C_{\rm digit},
\quad
\mathcal C_{\rm common-scale},
\quad
\mathcal C_{\rm branch}.
\]

Then：

\[
\boxed{
\mathscr Q_{g,k,u}(c,z)\ne16Y^2.
}
\]

Equivalently：

\[
\boxed{
\mathfrak S_{J2,\mathrm{reg}}^{(11)}=\varnothing.
}
\]

### Logical role

Within the R9/R10 fully audited central regular \(q>1\) shell, Theorem A is exactly the desired branch closure theorem.

### Scope firewall

Theorem A is **not yet advertised as a complete global \(J2\) theorem**, because R10 explicitly did not certify that singular \(d_A>1\) reverse semantics are fully equivalent to this same source shell.

A separate singular bridge or prior closure certificate is required before replacing：

\[
J2_{\rm regular}\Rightarrow\varnothing
\]

by：

\[
J2\Rightarrow\varnothing.
\]

---

# 6. Result 7 — Reduced Theorem, Version B

The full source shell contains several conditions already known to be algebraically redundant once the R9 chart is established.

The next stronger but still plausible theorem is：

## Theorem B — Reduced Square × Source-Lift Nonrepresentation

Under the same outer/live exponent conditions, assume：

1. the square equation：

\[
\mathscr Q_{g,k,u}(c,z)=16Y^2;
\]

2. a positive integral root/source-lattice lift：

\[
C_1\in\mathbf Z_{>0},
\qquad
\lambda\in\mathbf Z_{>0};
\]

3. source ten-unit / orientation positivity for \(c,z,\lambda,C_2,T,h,m,r,w,d_2\);

4. the common-\(V\) reducedness conditions：

\[
\gcd(C_1,u)
=
\gcd(C_2,H)
=
\gcd(c,GH)
=
1;
\]

5. the exact common-\(U\) digit realization：

\[
\exists U\in[U_{\rm lo},U_{\rm hi}]
\cap\mathbf Z_{>0},
\qquad
\gcd(U,uGH)=1.
\]

Then no such tuple exists.

### What B deliberately omits

B does **not** require as hypotheses：

- carry/floor；
- source-cut residual；
- \(2/5\)-capacity；
- odd-prime allocation；
- endpoint jump；
- \(N_0\)-split；
- full-word master；
- a second root/sphere equation；
- generic class-group data.

The full-word master is automatic.  
The sphere is already encoded by the square + integral root.  
All Phase-I retired packages are omitted.

B also deliberately drops the full primitive tuple gcd：

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

Therefore：

\[
\boxed{
\text{Theorem B} \Longrightarrow \text{Theorem A}.
}
\]

B is the preferred Phase-II theorem if it survives falsification.

---

# 7. Result 7 — Ambient Version C

## Theorem C — Ambient Moving-Square Nonrepresentation

Delete source restrictions and require only：

\[
G=10^g,\qquad
K=10^k,
\qquad
u\mid G+1,
\]

with positive：

\[
c,z,Y,
\]

and ask whether：

\[
\mathscr Q_{g,k,u}(c,z)\ne16Y^2
\]

always holds.

This theorem is **false**.

Therefore：

```text
AMBIENT_MOVING_SQUARE_THEOREM=FALSE
```

The Phase-II theorem cannot be formulated without source restrictions.

---

# 8. Result 8 — Exact Counterexample Ladder

R11 separates theorem strength by adding source constraints.

## Level A — moving square equation only

**SURVIVES.**

R10 already provides exact positive integral points on the moving conic.

Thus：

\[
\boxed{
\mathscr Q=16Y^2
}
\]

alone is abundant enough to have exact solutions.

## Level B — \(+\;uq=10^g+1\)

**SURVIVES in a live outer base.**

R10 gives a root-compatible integral point at：

\[
(g,k,u,q)=(4,1,73,137),
\]

with：

\[
c=
44166648285459361797000000,
\]

\[
z=
9530621959721527629285,
\]

and integral：

\[
\lambda=
84945551173868016406925.
\]

This point lies on the exact root conic and satisfies the source lattice relation for \(C_1\), but it is not a source state.

Hence：

\[
\boxed{
uq=G+1
}
\]

does not suppress square representations.

## Level C — \(+\) integrality / primitive-type restrictions

### Live current domain

**UNKNOWN globally.**

The R10 live root point fails primitive/common-\(V\) conditions, so it is not a Level-C survivor.

### Relaxed diagnostic outside the live \(g\ge4\) frontier

R11 exact search found：

\[
\boxed{
(g,k,u,q,c,z,Y)
=
(1,1,1,11,483,29,4820).
}
\]

It satisfies the moving square equation and has an integral positive root reconstruction with：

\[
C_1=130,\qquad
\lambda=567,
\]

\[
C_2=4284,\qquad
T=857,
\]

\[
w=1,\qquad
d_2=493.
\]

The basic common-\(V\) gcd checks are satisfied in this relaxed small-\(g\) state.

But it fails the actual digit/common-\(U\) shell completely.

Interpretation：

\[
\boxed{
\text{integral root + primitive-type gcd is not an ambient universal obstruction}.
}
\]

The live \(g\ge4\) theorem remains open.

## Level D — \(+\) digit windows

**UNKNOWN in the live domain.**

No theorem or genuine survivor is currently known.

## Level E — \(+\) common-scale / coprimality

**UNKNOWN after conditioning on the square.**

This distinction is crucial：

- R7 proves common-scale + coprimality can be large **before the full root**；
- R10 proves square/root points can be large **outside the source shell**；
- no known theorem decides their intersection.

This is exactly why R12 targets Level E.

## Level F — full root-independent source shell + square

**UNKNOWN.**

No genuine Level-F survivor is known.

If one is found, full source reconstruction is mandatory.

If it satisfies all \(J2\) conditions, it is a genuine \(J2\) counterexample.

If it dies at a supposedly exhausted root-independent gate, R8 must be rolled back.

---

# 9. Additional R11 Exact Reconnaissance

R11 performed exact integer reconnaissance; none of the following is promoted to a global theorem.

## 9.1 Live first outer base, primitive projective scan

For：

\[
g=4,\qquad
u=73,\qquad
q=137,
\]

and：

\[
k\in\{1,2\},
\]

R11 scanned primitive projective ten-unit pairs：

\[
1\le c,z\le1500,
\qquad
\gcd(c,z)=1,
\]

using exact integer square tests.

Total tested pairs across the two \(k\)-values：

\[
\boxed{608154}.
\]

Square count：

\[
\boxed{0}.
\]

This supports the plausibility of a live reduced theorem but is not proof.

## 9.2 Why projective normalization is only diagnostic

Because \(\mathscr Q\) is homogeneous of degree \(2\), scaling \((c,z,Y)\) preserves the ambient equation.

But source digit/common-\(U\) constraints are not homogeneous.

Therefore primitive \((c,z)\) scans are useful for ambient reconnaissance only and cannot replace source reconstruction.

---

# 10. What Actually Blocks the R10 Live Square Point?

The R10 live root-compatible point fails source semantics at precisely the restrictions Phase II must preserve.

For the displayed live point：

\[
(g,k,u,q)=(4,1,73,137),
\]

the exact reconstruction gives：

\[
C_1=
10220256521273550014136501,
\]

\[
C_2=
6917225053831866266193625000.
\]

It fails：

\[
\gcd(C_1,u)=73,
\]

\[
\gcd(C_2,H)=5000,
\]

and the common-\(U\) interval has：

\[
U_{\rm lo}=1,
\qquad
U_{\rm hi}=0.
\]

Thus the root-compatible ambient square is killed by：

\[
\boxed{
\textbf{primitive/common-}V
+
\textbf{actual digit/common-}U.
}
\]

This is the strongest available evidence for the minimal Phase-II restrictions.

It does **not** prove either gate alone is sufficient.

---

# 11. Result 9 — Independent Information-Class Audit

The audit result is：

```text
NEW_INDEPENDENT_INFORMATION_CLASS_IDENTIFIED=NO
```

The candidates behave as follows.

### source-preserving descent

No valid map currently exists.

### DD orientation / two-endpoint lock

DD-specific; no A1 transfer theorem.

### binary-form class/genus/composition

Potentially useful only if upgraded to source-labelled data.  
Otherwise it reduces to the already-known \(N_0\) square-class / 65 norm layer.

### fixed odd local obstruction

No fixed source-coupled modulus is currently identified.

### critical finite-state discriminant method

Valid as a finishing weapon after a new finite-state theorem, not a new information source.

Therefore Phase II should not launch a speculative fifth class before testing the direct reduced theorem.

---

# 12. Result 10 — Descent Audit

```text
DESCENT_INTERFACE=FAILED
```

Reason：

\[
\boxed{
\text{no known transform lowers a natural height while preserving}
}
\]

simultaneously：

- \(G=10^g\) and the required exponent profile；
- \(u\mid G+1\)；
- source lattice；
- decimal windows；
- primitive reducedness；
- Exact Resonance；
- \(J=2\).

The historical Gaussian/Vieta moves fail exactly at this preservation requirement.

Minimal-counterexample language may still be used in future proofs, but R11 does not pretend that a descent map has been found.

---

# 13. Result 11 — Standard Mathematical Object Identification

The Phase-II problem is closest to three standard objects.

## Object 1 — integral points on a moving family of conics / binary quadratic square representations

Primary interpretation：

\[
\widehat\Delta_{g,k,u}(c,z)=16Y^2
\]

is a ternary quadratic equation or, equivalently, a binary quadratic form representing a square.

What is nonstandard is the source domain：

\[
\mathcal C_{\rm src}^{(11)}.
\]

This is the **primary weapon class**.

## Object 2 — norm-form / quadratic-order representation with moving discriminant

Because：

\[
[\disc(\widehat\Delta)]=[N_0],
\]

the form corresponds to a norm problem in the quadratic algebra determined by \(N_0\).

This opens genus/class/composition language, but only as a secondary tool because 65 already showed that ambient norm information loses source lattice data.

## Object 3 — exponential-Diophantine conic fibration over a power-of-ten base

The coefficients satisfy：

\[
G=10^g,\qquad
K=10^k,\qquad
u\mid10^g+1.
\]

Thus globally it is an exponential-Diophantine family with an arithmetic divisor fibre.

R10 shows this is **not yet** a Laurent/ESS torus problem, because \(u,c,z,Y\) do not lie in a fixed finite-rank multiplicative group.

---

# 14. Binary Quadratic Form / Class-Group Audit

Classical quadratic-form theory can potentially provide：

- primitive representation criteria；
- genus/spinor-genus restrictions；
- composition laws；
- ambiguous class analysis；
- reduction.

But a valid Phase-II use must pass a source-fidelity test.

## Kill condition

If the derived obstruction depends only on：

\[
[N_0]
\]

or only on an ambient class/genus of \(\widehat\Delta\),

then it is not a new information class.

R10 already shows the discriminant square-class is \(N_0\); 65 already audited norm/Hermitian/class layers and found that source-lattice/digit realization is not automatic.

Therefore：

```text
CLASS_GROUP_ROUTE=CANDIDATE_RESERVE_ONLY
```

It may be promoted only if a new invariant is attached to：

\[
(C_1,C_2,c;U)
\]

or an equivalent source-labelled ideal/lattice state.

---

# 15. Result 12 — External-Theory Migration Audit

No new external theorem is activated in R11.

```text
NEW_MIGRATION_CARDS=NONE
```

Reason：

1. the primary theorem has now been identified precisely；
2. classical ambient binary-form/class-group theorems do not by themselves preserve source restrictions；
3. \(\Gamma_{10}\) Laurent/ESS activation threshold remains unmet；
4. no uniform theorem found in the existing 65/75 arsenal already implies the reduced source-restricted nonrepresentation statement.

Therefore R11 does not reopen a broad literature campaign.

A new Migration Card becomes justified only after R12 exposes a narrower standard interface—for example a fixed source-labelled genus obstruction, a finite set of quadratic orders, or a uniform \(S\)-integral conic theorem with the exact digit sector retained.

---

# 16. Result 13 — Phase-II Candidate Architectures

Only three architectures survive the R11 novelty test.

## Architecture A — Source-Restricted Moving Binary-Quadratic Square Representation

Attack：

\[
\widehat\Delta(c,z)=16Y^2
\]

directly on the reduced source domain.

### Why it is genuinely Phase II

The form itself is old NRSEC fibrewise.

The new object is the uniform quantifier：

\[
\forall(g,k,u)
\quad
\left(
\{\widehat\Delta=16Y^2\}
\cap
\mathcal C_{\rm src}^{(11)}
\right)
=\varnothing.
\]

This was not proved or falsified by R9.

### Death condition

If an infinite family satisfying the **reduced/full source shell and the square equation** is constructed：

```text
ARCH_A=KILL
```

A genuine Level-F survivor requires full original reconstruction immediately.

---

## Architecture B — Source-Preserving Minimal-Counterexample Descent

Assume a minimal solution under a height such as \(g\), \(u\), or a quadratic-form height and construct a smaller legal source solution.

### Current status

No legal descent map exists.

### Death condition

If every natural reduction changes：

- power-of-ten exponents；
- source lattice；
- decimal windows；
- primitive reducedness；

then：

```text
ARCH_B=KILL
```

R11 current audit already triggers this condition.

Thus B is **not launched**.

---

## Architecture C — Source-Coupled Class/Genus/Composition Obstruction

Use the quadratic form of discriminant class \(N_0\), but only if the represented square and source-labelled integral lift force a forbidden class/genus state.

### Death condition

If all class information collapses to：

\[
[N_0]
\]

or an ambient norm statement already present in 65/75：

```text
ARCH_C=KILL
```

Current evidence makes C reserve-only.

---

# 17. Result 14 — Architecture Ranking

Scoring scale：5 = strongest/best, except “theorem burden” where 5 = heaviest.

| Architecture | Distance to J2 closure | Genuine novelty | Source fidelity | Theorem burden | Falsifiable in 2–3 rounds | Rank |
|---|---:|---:|---:|---:|---:|---:|
| A. source-restricted moving square | **5** | 4 | **5** | 3 | **5** | **1** |
| B. source-preserving descent | 4 | **5** | 1 currently | **5** | 4 | 3 |
| C. source-coupled class/genus | 3 | 2 | 2 currently | 4 | 4 | 2 |

Unique recommendation：

\[
\boxed{
\textbf{Architecture A}.
}
\]

---

# 18. R12 — Unique Narrow Attack Target

R12 must not say：

> continue studying the moving-square theorem.

It should decide one precise implication.

## R12 target — Square-Conditioned Common-Scale Extinction

Assume the current live regular outer data and the moving square：

\[
\mathscr Q_{g,k,u}(c,z)=16Y^2.
\]

Assume an integral positive root/source-lattice reconstruction：

\[
C_1
=
\frac{uKd_2+\sigma Y}{AH^2}
\in\mathbf Z_{>0},
\]

\[
\lambda
=
\frac{2KC_1-Bz}{A}
\in\mathbf Z_{>0},
\]

with source positivity/ten-unit conditions and：

\[
\gcd(C_1,u)
=
\gcd(C_2,H)
=
\gcd(c,GH)
=
1.
\]

Then prove or falsify：

\[
\boxed{
[U_{\rm lo},U_{\rm hi}]
\cap
\{U\in\mathbf Z_{>0}:\gcd(U,uGH)=1\}
=
\varnothing.
}
\tag{R12}
\]

Equivalently, prove that every square/root-lattice/common-\(V\) state either：

\[
U_{\rm lo}>U_{\rm hi},
\]

or every integer in the interval shares a prime with \(uGH\).

### Why this does not reopen R6/R7

R6/R7 studied：

\[
\text{PRE\_ROOT source}
\Longrightarrow?
\text{common-}U\text{ extinction}.
\]

R12 studies：

\[
\boxed{
\text{SQUARE}
+
\text{INTEGRAL ROOT}
+
\text{COMMON-}V\text{ REDUCEDNESS}
\Longrightarrow?
\text{common-}U\text{ extinction}.
}
\]

The full-root square is exactly the missing independent information identified by R8.

This is a new intersection theorem, not an endpoint/common-scale refinement.

### R12 death condition

If one exact state satisfies all R12 hypotheses and admits a coprime common-\(U\), then：

```text
R12_REDUCED_THEOREM=FALSE
```

and that witness must be pushed immediately to the remaining full primitive/source predicates.

This makes R12 highly falsifiable.

---

# 19. Phase-II Launch Verdict

```text
MOVING_SQUARE_THEOREM_STATUS=
NEEDS_SOURCE_RESTRICTION

R11_TERMINAL_VERDICT=
PHASE_I_FROZEN_MOVING_SQUARE_THEOREM_EXTRACTED

85_PHASE_II_STATUS=
LAUNCH

PHASE_II_PRIMARY_OBJECT=
SOURCE_RESTRICTED_MOVING_BINARY_QUADRATIC_SQUARE_REPRESENTATION

PRIMARY_THEOREM=
THEOREM_B_REDUCED_SOURCE_RESTRICTED_NONREPRESENTATION

R12_ATTACK_TARGET=
SQUARE_ROOT_LATTICE_COMMONV_IMPLIES_COMMONU_EXTINCTION

DESCENT_INTERFACE=
FAILED

CLASS_GROUP_INTERFACE=
RESERVE_ONLY

NEW_MIGRATION_CARDS=
NONE

J2_STATUS=
OPEN
```

---

# 20. Answer to the R11 Core Question

R11 asked：

\[
\boxed{
\text{我们现在究竟是在证明什么 theorem？}
}
\]

The answer is：

> **Phase-II Main Theorem target.** For a power-of-ten outer base
> \(G=10^g,\ K=10^k\), with \(u\mid G+1\), the associated moving binary quadratic form
> \(\widehat\Delta_{g,k,u}(c,z)\) may represent squares ambiently. However, no such square
> representation should admit the exact integral root reconstruction, primitive/common-\(V\)
> reduction, and common-\(U\) decimal digit realization required by a genuine central regular
> \(J=2\) source state.

This is not a new coordinate system.

It is the first explicit Phase-II arithmetic nonrepresentation theorem.

