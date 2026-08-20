# A1 J2 PRCC10 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** A-Residue Root Lift × \(u\)-Square Compatibility × CQRF Integer-Root Collision  
**Status date:** 2026-08-16  
**Inherited frozen sources:** `A1_J2_GRFC9_Report.md`, `A1_J2_CZDR_Report.md`, `A1_J2_RCRF4_Report.md`, `A1_J2_CQLRC8_Report.md`  
**New symbolic files:** `A1_J2_PRCC10_Aroot.py`, `A1_J2_PRCC10_CRT.py`  
**New exact regression:** `A1_J2_PRCC10_search.py`  

---

# Part I — Executive Status

\[
\boxed{\textbf{Full J2 OPEN}}
\]

\[
\boxed{A^2\textbf{-Root Lift PROVED}}
\]

\[
\boxed{h=0\textbf{ OPEN globally}}
\]

\[
\boxed{h=1\textbf{ OPEN globally}}
\]

\[
\boxed{h<0\textbf{ OPEN globally}}
\]

The round nevertheless produces two genuinely new uniform theorems and one decisive diagnostic collapse.

First, the requested composite-modulus root lift is exact.  Put

\[
Q(x):=AH^2x^2-2uKD_2x+\widetilde F,
\qquad
\widetilde F=A\mathcal X^2+ZD_2,
\]

and let

\[
r_A\equiv-K^{-1}Z\pmod A,
\qquad 0\le r_A<A.
\]

Then, with

\[
n_A:=\frac{Kr_A+Z}{A},
\]

one has the exact integer

\[
\boxed{
T_A:=\frac{Q(r_A)}A
=H^2r_A^2+\mathcal X^2-KD_2r_A+D_2n_A.
}
\tag{PRCC-T}
\]

Writing \(x=r_A+Ac\), the next \(A\)-digit is governed by

\[
\boxed{
T_A+Q'(r_A)c\equiv0\pmod A.
}
\tag{A2-LIFT}
\]

The sign in the prompt's displayed formula for \(c_A\) needs correction: in the nondegenerate case,

\[
\boxed{
c_A\equiv-\,T_A\,Q'(r_A)^{-1}\pmod A.
}
\tag{SIGN-CORRECTION}
\]

Second, this round proves a **uniform Root Carry Bound**.  Every remaining root that reaches an \(A^2\)-lift class

\[
x=r_{A^2}+A^2j,
\qquad 0\le r_{A^2}<A^2,
\]

satisfies

\[
\boxed{
0\le j<q\left(\frac{1299}{500}+10^{-\ell}\right)<2.599q
}
\qquad(\ell\ge6).
\tag{RCB}
\]

Thus the large actual root \(x\) has genuinely collapsed to a carry alphabet of size \(O(q)\), uniformly across high, boundary, and reverse \(k\)-chambers.  This is the main new dimensional collapse of PRCC10.

Third, the inherited boundary census was re-run through the new pipeline.  For the exact 79 DCDC/root-layer pseudo-cells with

\[
h=0,\qquad q\in\{7,11,17,19\},\qquad g\le1200,
\]

PRCC10 obtains:

```text
DCDC cells                     79
A^2-lift solvable              59
Derivative-degenerate          26
Primitive gcd(Z,u)=1           75
Total legal carry j candidates 812
U-square carry candidates       0
Exact integer roots             0
```

With first-death ordering, 20 cells die at the \(A^2\)-lift divisibility condition, 3 at primitive \(\gcd(Z,u)=1\), 1 at the root interval, and the remaining 55 at the transformed \(u\)-square gate.  Hence all 79 historical boundary cells are now explained without using a global discriminant-square test.

This **does not** prove infinite \(h=0\) closure: the census is still only the inherited finite diagnostic.  The new infinite theorem is the carry reduction (RCB), not the finite table.

---

# Part II — Frozen Root Ledger

Throughout,

\[
G=10^g,\qquad H=\frac G2,\qquad K=10^k,
\qquad \ell=2g-k\ge6,
\]

\[
uq=G+1,\qquad A=2u+1,\qquad M=q(q+4).
\]

For CQRF,

\[
R=At-2N,
\qquad
Y=R+uNM,
\]

\[
E=uq\bigl((G-1)t-qN\bigr)+GY,
\]

and

\[
Z=\frac RM,
\qquad
\mathcal X=\frac{Y}{2M},
\qquad
D_2=\frac{E}{2M}.
\]

The frozen quadratic is

\[
\boxed{
Q(x)=AH^2x^2-2uKD_2x+\widetilde F=0,
}
\tag{RQ}
\]

with

\[
\widetilde F=A\mathcal X^2+ZD_2,
\qquad x=a_1.
\]

Clearing CQRF denominators gives

\[
\boxed{
AG^2M^2x^2-4uKEMx+AY^2+2RE=0.
}
\tag{CQRF-ROOT}
\]

No root-factor quotient distinct from \(x\) is introduced in this round.

---

# Part III — Primitive-Root Dependency Audit

The provenance audit is essential because these conditions are not generic pre-root identities.

| Condition | Pre-root? | Integral-root necessary? | Primitive recovery? | Exact status |
|---|---:|---:|---:|---|
| \(Kx\equiv-Z\pmod A\) | No | Yes | Yes | Frozen primitive \(C_1\)-residue, radialized |
| \(x^2\equiv Z^2\pmod u\) | No | Yes | Yes | Frozen primitive square residue, radialized |
| \(\gcd(Z,u)=1\) | No | Not root-only | Yes | Needs primitive gcd plus common-\(U\) coprimality |
| \(x>AG/10\) | No | Yes | Actual digit | Frozen DRL |
| root upper bound below | No | Yes | No extra primitive gcd | Complementary-factor positivity |
| \(A^2\)-lift | No | Yes | Uses A-ROOT | Consequence of \(Q(x)=0\) after canonical first residue |

Two important independence corrections follow.

### 3.1 U-SQ is exactly the root quadratic modulo \(u\)

Because

\[
A\equiv1,\quad G\equiv-1,\quad H\equiv-\frac12\pmod u,
\]

and

\[
\mathcal X=\frac{Z+uN}{2}\equiv\frac Z2\pmod u,
\]

\[
D_2=ua_3+G\mathcal X\equiv-\frac Z2\pmod u,
\]

we get

\[
\widetilde F
=A\mathcal X^2+ZD_2
\equiv-\frac{Z^2}{4}\pmod u.
\]

Therefore

\[
\boxed{
Q(x)\equiv\frac{x^2-Z^2}{4}\pmod u.
}
\tag{Q-mod-u}
\]

Since \(u\) is odd,

\[
Q(x)\equiv0\pmod u
\iff
x^2\equiv Z^2\pmod u.
\]

Thus U-SQ is not probabilistically independent of the root quadratic.  It is the canonical \(u\)-component of the same exact equation.  It remains extremely useful after the \(A^2\) coordinate change because it becomes a congruence on the small carry \(j\).

### 3.2 A-ROOT and the root quadratic modulo \(A\)

Modulo \(A\),

\[
-2u\equiv1\pmod A,
\qquad
\widetilde F\equiv ZD_2\pmod A,
\]

so

\[
\boxed{
Q(x)\equiv D_2(Kx+Z)\pmod A.
}
\tag{Q-mod-A}
\]

Hence if \(\gcd(D_2,A)=1\), A-ROOT is exactly the unique root of \(Q\) modulo \(A\).  If \(\gcd(D_2,A)>1\), the primitive A-ROOT condition is stronger than merely requiring \(Q(x)\equiv0\pmod A\).

The CRT combination used later is therefore legitimate arithmetic over coprime moduli, but it is **not** described as multiplying independent probabilities.

---

# Part IV — \(A\)-Residue Root

Since \(A\) is a ten-unit,

\[
\gcd(K,A)=1.
\]

The primitive root residue gives the canonical representative

\[
\boxed{
r_A:=(-K^{-1}Z)\bmod A,
\quad 0\le r_A<A,
}
\]

and

\[
\boxed{x=r_A+Ac.}
\]

Define

\[
\boxed{
n_A:=\frac{Kr_A+Z}{A}\in\mathbb Z.}
\]

Then direct factorization gives

\[
Q(r_A)
=A\left(
H^2r_A^2+\mathcal X^2-KD_2r_A+D_2n_A
\right).
\]

Thus (PRCC-T) follows.

The same object has an exact CQRF form.  Substituting

\[
\mathcal X=\frac{Y}{2M},\quad
D_2=\frac{E}{2M},\quad
Z=\frac RM,
\]

and clearing denominators yields

\[
\boxed{
4AM^2T_A
=AG^2M^2r_A^2-4uKEMr_A+AY^2+2RE.
}
\tag{CQRF-TA}
\]

So the constant term after the primitive A-residue is not an opaque huge integer: it is exactly the CQRF root polynomial evaluated at \(r_A\), divided by its forced \(A\)-factor.

Expanding the CQRF polynomial at \(x=Ac+r_A\),

\[
\mathcal Q_A(c)
=AG^2M^2(Ac+r_A)^2
-4uKEM(Ac+r_A)+AY^2+2RE,
\]

one obtains

\[
\boxed{
\mathcal Q_A(c)
=A\Bigl[
A^2G^2M^2c^2
+\bigl(2AG^2M^2r_A-4uKEM\bigr)c
+4M^2T_A
\Bigr].
}
\tag{ACQ-FACT}
\]

This is the requested coefficient cancellation: after fixing the primitive first A-digit, the entire CQRF root polynomial acquires an explicit factor \(A\), and its constant term is the carry \(T_A\).

---

# Part V — \(A^2\)-Root Lift

For

\[
x=r_A+Ac,
\]

quadratic Taylor expansion is exact:

\[
Q(r_A+Ac)
=Q(r_A)+AcQ'(r_A)+A^3H^2c^2.
\]

Therefore modulo \(A^2\),

\[
\boxed{
T_A+Q'(r_A)c\equiv0\pmod A.
}
\]

Also

\[
Q'(r_A)=2AH^2r_A-2uKD_2,
\]

so

\[
\boxed{
Q'(r_A)\equiv KD_2\pmod A.
}
\]

Since \(\gcd(K,A)=1\),

\[
\boxed{
\gcd(Q'(r_A),A)=\gcd(D_2,A)=:d_A.
}
\tag{DEG}
\]

This proves the requested complete composite-modulus classification.

### Nondegenerate chamber

If \(d_A=1\), there is one and only one next digit

\[
\boxed{
c_A\equiv-\,T_AQ'(r_A)^{-1}\pmod A,
\qquad 0\le c_A<A,
}
\]

and hence a unique

\[
\boxed{
r_{A^2}=r_A+Ac_A\pmod{A^2}.}
\]

### Degenerate chamber

If \(d_A>1\), the lift exists iff

\[
\boxed{d_A\mid T_A.}
\tag{DEG-SOLV}
\]

When it exists, \(c\) is one class modulo \(A/d_A\), hence exactly \(d_A\) classes modulo \(A\), giving \(d_A\) canonical roots modulo \(A^2\).

The tempting supporting conjecture

\[
\gcd(D_2,A)=1
\]

is **false globally even in the old boundary diagnostic**.  Among the 79 historical cells,

\[
\boxed{
\gcd(D_2,A)\text{ distribution}
=\{1:53,\ 3:21,\ 7:4,\ 11:1\}.
}
\]

Thus derivative-degenerate states are genuine and cannot be deleted from the theorem.  Of those 26 degenerate cells, 20 fail (DEG-SOLV); the remaining 6 all have \(d_A=3\), hence three \(A^2\)-lift classes, and are later killed by U-SQ.

### General elementary A-adic lift

No prime-power Hensel lemma is required.  If

\[
Q(r_n)\equiv0\pmod{A^n},
\]

write

\[
x=r_n+A^nc.
\]

Modulo \(A^{n+1}\),

\[
\boxed{
\frac{Q(r_n)}{A^n}+Q'(r_n)c\equiv0\pmod A.
}
\tag{A-n-LIFT}
\]

In the nondegenerate chamber this uniquely determines each subsequent A-digit.  In the degenerate chamber it is again an elementary linear-congruence problem with the same gcd criterion.

The supplied symbolic script verifies exact zero residuals for the \(T_A\) factorization, derivative reduction, \(A^2\) Taylor expansion, and CQRF-\(T_A\) identity.

---

# Part VI — Root Carry \(j\)

Choose any canonical \(A^2\)-lift

\[
0\le r_{A^2}<A^2,
\qquad
x=r_{A^2}+A^2j.
\]

## 6.1 Exact root interval

The frozen corpus does **not** contain a proved theorem \(x<AG\).  It would be incorrect to insert that desired endpoint without proof.

The valid lower endpoint is the frozen DRL

\[
\boxed{x>\frac{AG}{10}.}
\]

For the upper endpoint, use the positive complementary factor

\[
\Lambda=2uKD_2-AH^2x>0.
\]

Therefore

\[
AH^2x<2uKD_2.
\]

Since

\[
H^2=\frac{G^2}{4},
\qquad
K=\frac{G^2}{10^\ell},
\]

we obtain the exact root-necessary upper bound

\[
\boxed{
x<\frac{8uD_2}{A10^\ell}.}
\tag{ROOT-UP}
\]

Hence the actual root-necessary interval used by PRCC10 is

\[
\boxed{
I_x=\left(\frac{AG}{10},\frac{8uD_2}{A10^\ell}\right).
}
\tag{IX}
\]

For each \(r_{A^2}\), the exact carry endpoints are

\[
\boxed{
 j_{\min}
 =\left\lfloor\frac{AG/10-r_{A^2}}{A^2}\right\rfloor+1,
}
\]

\[
\boxed{
 j_{\max}
 =\left\lceil\frac{8uD_2/(A10^\ell)-r_{A^2}}{A^2}\right\rceil-1.
}
\]

## 6.2 Uniform Root Carry Bound

The frozen negative/radial estimate is

\[
\mathcal XK<\eta uG^2,
\qquad
\eta=\frac{1299}{500},
\]

and DIG3 gives

\[
a_3<G.
\]

Since \(K=G^2/10^\ell\),

\[
\mathcal X<\eta u10^\ell.
\]

Therefore

\[
D_2=ua_3+G\mathcal X
<uG\left(1+\eta10^\ell\right).
\]

Use (ROOT-UP):

\[
\frac{x}{A^2}
<\frac{8uD_2}{A^3 10^\ell}
<\frac{8u^2G(1+\eta10^\ell)}{A^3 10^\ell}.
\]

Because \(A=2u+1>2u\),

\[
A^3>8u^3.
\]

Thus

\[
\frac{x}{A^2}
<\frac{G}{u}\left(\eta+10^{-\ell}\right)
=\frac{qG}{G+1}\left(\eta+10^{-\ell}\right)
<q\left(\eta+10^{-\ell}\right).
\]

Finally, \(0\le r_{A^2}<A^2\) and \(x>0\) force \(j\ge0\).  Hence

\[
\boxed{
0\le j<q\left(\eta+10^{-\ell}\right)
<2.599q
\qquad(\ell\ge6).
}
\]

This theorem is independent of the sign of \(h=k-g\).  It uses only the sign-unified frozen radial bound, DIG3, and the root-factor upper endpoint.  Therefore it applies to high, boundary, and Reverse-CQRF root states alike.

This is **Success C2 — Root Carry Bound**.

---

# Part VII — \(u\)-Square Compatibility

Because

\[
A=2u+1\equiv1\pmod u,
\]

we have

\[
A^2\equiv1\pmod u.
\]

Thus

\[
x=r_{A^2}+A^2j
\]

implies

\[
x\equiv r_{A^2}+j\pmod u.
\]

The primitive square residue becomes

\[
\boxed{
(r_{A^2}+j)^2\equiv Z^2\pmod u.
}
\tag{J-USQ}
\]

This is exactly the desired transfer of a huge-root condition to the small carry.

If \(\gcd(Z,u)=1\), then because \(u\) is odd one may write

\[
r_{A^2}+j\equiv\eta_u Z\pmod u,
\qquad
\eta_u^2\equiv1\pmod u.
\]

However PRCC10 deliberately does **not** require factoring \(u\) in the computational reducer.  The direct congruence (J-USQ) can be tested on the proven interval of fewer than \(2.599q\) carries.  This also handles valuation-overlap states with \(\gcd(Z,u)>1\), where a naive sign-cell decomposition is invalid.

The q=11 historical regressions are exactly such a warning: both \(g=471\) and \(g=63501\) have

\[
\boxed{\gcd(Z,u)=13.}
\]

So the coprime sign representation must not be used there.

---

# Part VIII — Primitive CRT Collapse

For a chosen \(u\)-root residue \(r_u\pmod u\), combine

\[
x\equiv r_{A^2}\pmod{A^2},
\qquad
x\equiv r_u\pmod u.
\]

Since

\[
\gcd(A,u)=1,
\]

this determines

\[
\boxed{x\pmod{A^2u}.}
\]

Equivalently, because \(A^2\equiv1\pmod u\),

\[
\boxed{
j\equiv r_u-r_{A^2}\pmod u.}
\tag{J-CRT}
\]

The Root Carry Bound sharpens the scale comparison:

- if \(u>2.599q\), every fixed \(u\)-root class contains **at most one** legal carry \(j\);
- if merely \(u>q\), every fixed \(u\)-root class contains at most three legal carries, because the total carry interval has length below \(2.599q<3u\);
- if \(u\le q\), then \(q^2\ge G+1\), exactly the large-\(q\) chamber where the inherited outer suppression is strongest.

Thus the prompt's conceptual \(u>q\) / \(u\le q\) split survives, but the exact uniqueness threshold is \(u>2.599q\), not merely \(u>q\).

There is also a clean A-adic alternative.  In the nondegenerate chamber, the \(A^3\)-lift determines \(j\pmod A\).  Whenever

\[
A>q\left(\eta+10^{-\ell}\right),
\]

the carry interval is shorter than one A-modulus, so the A-adic lift alone leaves at most one carry candidate.  This gives a natural small/intermediate-\(q\) single-candidate region without any infinite Hensel construction.

---

# Part IX — Carry Polynomial

Let

\[
x=r_{A^2}+A^2j.
\]

Because \(Q(r_{A^2})\equiv0\pmod{A^2}\), exact Taylor expansion gives

\[
Q(r_{A^2}+A^2j)
=Q(r_{A^2})+A^2jQ'(r_{A^2})+A^5H^2j^2.
\]

Divide by \(A^2\):

\[
\boxed{
T_{A^2}(j)
:=\frac{Q(r_{A^2})}{A^2}
+Q'(r_{A^2})j
+A^3H^2j^2.
}
\tag{CARRY-Q}
\]

A genuine integer root requires

\[
\boxed{T_{A^2}(j)=0.}
\]

This is the correct final quadratic variable: \(j\) is uniformly \(O(q)\), while \(x\) itself is of root-digit scale.

Modulo \(A\), (CARRY-Q) gives the optional \(A^3\)-lift

\[
\boxed{
\frac{Q(r_{A^2})}{A^2}+Q'(r_{A^2})j\equiv0\pmod A.
}
\tag{A3-LIFT}
\]

No deeper A-adic theory is needed unless this congruence still leaves multiple carries in the actual interval.

---

# Part X — \(h=0\) Campaign

The inherited exact diagnostic was reproduced for

\[
g\le1200,
\qquad
q\in\{7,11,17,19\}.
\]

The new exact gate counts are:

| \(q\) | DCDC | A2 solvable | degenerate | primitive gcd pass | legal \(j\) | U-SQ \(j\) | exact roots |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 7  | 28 | 24 | 4  | 28 | 126 | 0 | 0 |
| 11 | 44 | 32 | 18 | 41 | 650 | 0 | 0 |
| 17 | 5  | 1  | 4  | 4  | 26  | 0 | 0 |
| 19 | 2  | 2  | 0  | 2  | 10  | 0 | 0 |
| **Total** | **79** | **59** | **26** | **75** | **812** | **0** | **0** |

The first-death distribution in the implemented ordering is

```text
A2_LIFT                  20
PRIMITIVE_GCD(Z,u)        3
J_INTERVAL                1
U_SQUARE                 55
EXACT_ROOT_SURVIVOR       0
```

One additional primitive-gcd failure is already dead at the earlier A2 gate, so the raw \(\gcd(Z,u)=1\) pass count is 75/79.

This is a strong mechanistic improvement over the old statement “79 DCDC cells, 0 global squares”: every old pseudo-cell is now killed by a primitive-root/carry gate, and the global square test is not used by PRCC10.

Nevertheless,

\[
\boxed{h=0\textbf{ remains OPEN globally}.}
\]

The finite census is not promoted beyond its audited range.  What is global is (RCB) and the A-adic lift theorem.

---

# Part XI — \(h=1\) Campaign and the q=11 regressions

The fixed historical fibre is

\[
q=11,
\qquad t=31,
\qquad \alpha=152510.
\]

For this fibre,

\[
u=\frac{G+1}{11},
\qquad
A=\frac{2G+13}{11},
\]

\[
N=\frac{15251G+29419}{29491},
\]

and an exact simplification gives

\[
\boxed{
Z=\frac{13(696G+5239)}{324401}.
}
\tag{Q11-Z}
\]

The denominator is coprime to 13, so every integral state on this fixed formula has \(13\mid Z\).  For both requested regressions, also \(13\mid u\), hence \(\gcd(Z,u)=13\).

## Regression A: \(g=471\)

Exact summary:

```text
u:   470 digits, suffix 909090909091
A:   471 digits, suffix 818181818183
Z:   470 digits, suffix 783881677307
D2: 1412 digits, suffix 610220067139
r_A suffix:   323947830001
c_A suffix:   586136977973
r_A2 suffix:  562109713060
gcd(D2,A): 1
gcd(Z,u):  13
j interval: 1..28
U-SQ legal j: none
exact root: none
```

Thus the first full primitive-recovery failure is already

\[
\gcd(Z,u)=13\ne1.
\]

Even if that gcd gate is intentionally postponed, the unique nondegenerate \(A^2\)-lift leaves exactly 28 carry candidates and all 28 fail (J-USQ).  This replaces the old explanation “\(\Psi\equiv8\pmod{11}\) is a nonresidue” with a direct root-coordinate incompatibility.

## Regression B: \(g=63501\)

Exact summary:

```text
u:      63500 digits, suffix 909090909091
A:      63501 digits, suffix 818181818183
Z:      63500 digits, suffix 783881677307
D2:    190502 digits, suffix 610220067139
r_A suffix:   323947830001
c_A suffix:   444973023504
r_A2 suffix:  213461403233
gcd(D2,A): 1
gcd(Z,u):  13
j interval: 1..28
U-SQ legal j: none
exact root: none
```

This is the important structural-local-stack counterexample from the previous round.  PRCC10 now explains its death without appealing to a new killer prime:

1. full primitive recovery already fails at \(\gcd(Z,u)=13\);
2. independently of the coprime sign-cell classification, direct valuation-aware U-SQ finds no legal \(j\in\{1,\dots,28\}\);
3. hence the exact carry polynomial is never reached by a legal primitive carry.

Therefore the large \(g=63501\) state is no longer merely “global discriminant not square”; its primitive root coordinates are explicitly incompatible.

This does **not** close all \(h=1\) fibres, so

\[
\boxed{h=1\textbf{ remains OPEN globally}.}
\]

---

# Part XII — Reverse-CQRF

The primitive root residues were inherited before the high/boundary/reverse CQRF split.  Therefore, for every reverse state that actually reaches the root layer,

\[
Kx\equiv-Z\pmod A,
\qquad
x^2\equiv Z^2\pmod u
\]

remain unchanged in form.

The A-lift theorem likewise depends only on \(Q(x)\), \(A\), and the primitive A-root residue.  The carry theorem uses the sign-unified frozen inequality

\[
\mathcal XK<\eta uG^2
\]

and \(\ell\ge6\), so it also remains unchanged.

Hence

\[
\boxed{
\textbf{A-root / A}^2\textbf{-root / carry / U-SQ machinery is high-boundary-reverse unified.}
}
\]

The old reverse pre-DCDC family

\[
(q,N,t)=(1,7,3)
\]

was replayed at \((g,k,\ell)=(12,6,18)\).  It passes the linear/radial package but has

\[
\widetilde F\equiv3\pmod5,
\]

so it dies at DCDC before a root-layer PRCC test is logically available.  It is retained only as a scope regression.

No new exhaustive Reverse-CQRF root-layer census was obtained in this round, hence

\[
\boxed{h<0\textbf{ remains OPEN globally}.}
\]

---

# Part XIII — Zero-Tail Audit

The A-ROOT and U-SQ residues are root/primitive reconstruction statements, not consequences of the nonzero-tail CQRF quotient.  Therefore zero-tail states that reach the root layer use the same

\[
Q(x),\quad r_A,\quad A^2\text{-lift},\quad j,\quad\text{U-SQ}
\]

machinery.

What changes is only preprocessing: a zero-tail state may not admit the same nonzero-tail \((R,Y,E)\) parametrization used for CQRF bookkeeping.

The inherited boundary zero-tail ray for \(q>1\) is already impossible; the reverse zero-tail condition remains separately bounded by the prior

\[
q^3<63\cdot10^r.
\]

No concrete zero-tail DCDC/root pseudo-state was recovered in the present run, so no numeric zero-tail PRCC count is claimed.

---

# Part XIV — Global \(u>q\) / \(u\le q\) Split

The new carry theorem makes the proposed split precise.

## 14.1 \(u>q\)

Because

\[
0\le j<2.599q<3u,
\]

each fixed residue class modulo \(u\) contributes at most three carry representatives.  In the stronger chamber

\[
u>2.599q,
\]

each fixed U-square root class contributes at most one carry.

If \(\gcd(Z,u)=1\), these classes can be represented by

\[
r_{A^2}+j\equiv\eta_u Z\pmod u,
\qquad \eta_u^2\equiv1\pmod u.
\]

If \(\gcd(Z,u)>1\), use the direct congruence (J-USQ), not a false global \(\pm\) split.

## 14.2 \(u\le q\)

Since \(uq=G+1\),

\[
u\le q\Longrightarrow q^2\ge G+1.
\]

Thus this is automatically a large-\(q\) chamber.  Combining it with the inherited outer bound strengthens the \((g,\ell)\) slope, but PRCC10 does not obtain a complete extinction theorem there.

The clean global architecture is therefore now:

\[
\boxed{
\begin{array}{ll}
\text{small/intermediate }q:&
A^2\text{/}A^3\text{ root lift + }j=O(q)+\text{U-SQ},\\[1mm]
\text{large }q:&
\text{outer suppression first, then the same carry gate}.
\end{array}
}
\]

This is a lower-dimensional meeting point than the previous large-root formulation.

---

# Part XV — Computational Regression

The new scripts use exact integer arithmetic and `Fraction` only for inequalities.  No floating-point decision is used.

## 15.1 Boundary 79 cells

The old h=0 generator was reproduced with an exact modular prefilter for RCE3 before constructing huge \(N\); the prefilter is algebraically equivalent and reproduces the inherited counts exactly:

```text
q=7 : tail 221288, reconstructed 2900, linear 370, DCDC 28
q=11: tail 8713715, reconstructed 264156, linear 10214, DCDC 44
q=17: tail 413750, reconstructed 1164, linear 32, DCDC 5
q=19: tail 437896, reconstructed 969, linear 21, DCDC 2
```

The new root-carry gates then give the table in Part X.

## 15.2 Derivative degeneracy

```text
d_A=1  : 53 cells
d_A=3  : 21 cells
d_A=7  : 4 cells
d_A=11 : 1 cell
```

Of the 26 degenerate cells:

```text
20 fail d_A | T_A
 6 pass, all with d_A=3, giving three A^2 classes each
```

Every one of those six surviving degenerate cells is later killed by U-SQ.

## 15.3 Symbolic residuals

`A1_J2_PRCC10_Aroot.py` reports

```text
TA_FACTOR_RESIDUAL=0
DERIVATIVE_MOD_A_CLEARED_RESIDUAL=0
A2_EXPANSION_RESIDUAL=0
CQRF_TA_RESIDUAL=0
```

and the q=11,g=471 CQRF-\(T_A\) numerical regression also has exact residual 0.

---

# Part XVI — Counterexample / Survivor Ledger

The following conjectures are now frozen as false or corrected.

### C1 — \(\gcd(D_2,A)=1\) always

**FALSE.**  The boundary diagnostic contains 26 degenerate cells, including gcd values 3, 7, and 11.

### C2 — derivative degeneracy destroys A-adic lifting

**FALSE.**  The correct criterion is \(d_A\mid T_A\).  Six degenerate cells lift, each to three \(A^2\)-classes.

### C3 — \(x<AG\) is an already-frozen actual root window

**NOT PROVED in the recovered corpus.**  PRCC10 does not use it.  The valid exact root-necessary upper endpoint is (ROOT-UP).

### C4 — U-SQ is an independent new equation from the root quadratic

**FALSE as an independence statement.**  It is exactly \(Q(x)=0\pmod u\) in the reconstructed chart.  Its value comes from applying that modulus after the A-adic carry reduction.

### C5 — A-ROOT is always just Q modulo A

**Only true in the nondegenerate chamber.**  When \(d_A>1\), primitive A-ROOT selects a stronger canonical class than \(Q(x)\equiv0\pmod A\) alone.

### C6 — \(x^2\equiv Z^2\pmod u\) may always be written as one global sign \(x\equiv\pm Z\pmod u\)

**FALSE for composite \(u\)** and especially invalid when \(\gcd(Z,u)>1\).  Use prime-power allocation or direct J-USQ.

### C7 — q=11,g=63501 survives all primitive root residues

**FALSE.**  It has \(\gcd(Z,u)=13\), and even after bypassing that primitive-gcd gate its 28 legal A2 carries all fail U-SQ.

The remaining genuine survivor is not a specific numerical root state.  It is the **global parametric frontier**:

\[
\boxed{
\text{outer CQRF state}
\longmapsto
\text{one/finitely many }r_{A^2}
\longmapsto
0\le j<2.599q
}
\]

subject to

\[
\boxed{
(r_{A^2}+j)^2\equiv Z^2\pmod u
}
\]

and

\[
\boxed{
T_{A^2}(j)=0.
}
\]

---

# Part XVII — New Frontier

J2 is not closed this round, so no resonance-closure certificate is generated.

The frontier is, however, strictly lower-dimensional than the one inherited from GRFC9.

The old formulation was

\[
\boxed{
\text{large root }x
+\text{primitive residues}
+\text{CQRF quadratic}.
}
\]

PRCC10 replaces it by

\[
\boxed{
\textbf{small root carry }j
+\textbf{one U-square congruence}
+\textbf{one exact carry polynomial},
}
\]

where

\[
\boxed{0\le j<2.599q.}
\]

More explicitly, for every primitive-recovery-eligible A2 class,

\[
\boxed{
(r_{A^2}+j)^2\equiv Z^2\pmod u,
}
\tag{FRONT-1}
\]

\[
\boxed{
\frac{Q(r_{A^2})}{A^2}
+Q'(r_{A^2})j
+A^3H^2j^2=0,
}
\tag{FRONT-2}
\]

\[
\boxed{
0\le j<q\left(\frac{1299}{500}+10^{-\ell}\right).
}
\tag{FRONT-3}
\]

In the nondegenerate small/intermediate-q chamber one may additionally use

\[
\boxed{
\frac{Q(r_{A^2})}{A^2}+Q'(r_{A^2})j\equiv0\pmod A,
}
\tag{FRONT-4}
\]

which often determines the only possible carry before FRONT-1 is applied.

This is the recommended next terminal object.  It does **not** introduce another root quotient; it is exactly the residual carry freedom left after two A-adic digits have been fixed.

---

# File Audit

Generated and checked in PRCC10:

```text
A1_J2_PRCC10_Report.md
A1_J2_PRCC10_Aroot.py
A1_J2_PRCC10_CRT.py
A1_J2_PRCC10_search.py
A1_J2_PRCC10_dependency.py
A1_J2_PRCC10_certificate.txt
A1_J2_PRCC10_survivors.tsv
```

No `A1_J2_Resonance_Closure_Certificate.md` is generated because Full J2 remains OPEN.

FINAL_REPORT_FILE: A1_J2_PRCC10_Report.md

AROOT_SYMBOLIC_FILE: A1_J2_PRCC10_Aroot.py

CRT_SYMBOLIC_FILE: A1_J2_PRCC10_CRT.py

DEPENDENCY_FILE: A1_J2_PRCC10_dependency.py

COMPUTATION_FILE: A1_J2_PRCC10_search.py

CERTIFICATE_FILE: A1_J2_PRCC10_certificate.txt

SURVIVOR_FILE: A1_J2_PRCC10_survivors.tsv

J2_CLOSURE_CERTIFICATE_FILE: NOT_GENERATED_BECAUSE_OPEN
