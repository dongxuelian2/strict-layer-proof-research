# 85 第三轮：Source-Cut Residual Exclusion × Canonical Root Factor Allocation × Primitive Nonabsorption × (2/5)-Capacity Collision × Regular-J2 Closure Campaign

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Round:** 85-R3  
**Target:** \(q>1,\ d_A=1,\ x=x_*\Rightarrow \varepsilon_*\neq0\)  
**Status:** **REGULAR J2 STILL OPEN**  
**Highest rigorously achieved level:** **R3-S1**, with a strengthened canonical radial-overlap theorem and a negative architecture theorem.

---

# 1. Executive Summary

85-R3 did **not** prove

\[
\boxed{
q>1,\qquad d_A=1
\Longrightarrow
\varepsilon_*\ne0.
}
\]

Hence

\[
\boxed{\textbf{REGULAR J2 IS NOT CLOSED}.}
\]

No high, boundary, or reverse regular tail chamber is closed in this round.

However, the round does produce three exact structural results and two decisive negative architecture verdicts.

## 1.1 Canonical root factorization is genuinely source-labelled

On a genuine regular source solution, the unique canonical root is not an anonymous quadratic root:

\[
\boxed{x_*=a_1.}
\]

The normalized complementary factor is the old source complementary factor after removing the forced decimal core:

\[
\boxed{
\Lambda=2K\lambda_*,
\qquad
\lambda_*=uD_2-AMx_*.
}
\]

Therefore

\[
\boxed{
\varepsilon_*=0
\iff
\mathscr R(x_*)=0
\iff
\Omega=x_*\lambda_*
}
\]

is a genuine source-labelled factor allocation.

This identification is inherited from the GRFQ/root-factor audit, where the canonical \(\kappa\) was proved to equal the actual \(a_1\), and where
\(\widetilde F=a_1\Lambda\), \(\Lambda=2K\lambda_0\), \(\Omega=a_1\lambda_0\) were provenance-audited.  
Source: fileciteturn24file0 fileciteturn24file15

## 1.2 Primitive nonabsorption extends beyond \(u\)

The two requested automatic facts are proved:

\[
\boxed{\gcd(x_*,u)=1},
\qquad
\boxed{\gcd(\lambda_*,u)=1}.
\]

In the regular branch one also has

\[
\boxed{\gcd(\lambda_*,A)=1},
\qquad
\boxed{\gcd(\lambda_*,10)=1},
\]

and hence

\[
\boxed{\gcd(\lambda_*,GK)=1}.
\]

More strongly, if \(\mathcal U\) denotes the actual common radial scale
(\(a_i=\mathcal U C_i\)), then

\[
\boxed{
\gcd(C_1,d_2)=1
}
\]

and therefore

\[
\boxed{
\gcd(x_*,D_2)
=
\gcd(x_*,\lambda_*)
=
\mathcal U.
}
\tag{R3-GCD}
\]

Thus every common prime of the two root factors is **exactly radial content**.  After removing that content,

\[
x_*=\mathcal U C_1,
\qquad
\lambda_*=\mathcal U\lambda^\flat,
\]

with

\[
\boxed{\gcd(C_1,\lambda^\flat)=1},
\]

and

\[
\boxed{
\Omega
=
\mathcal U^2C_1\lambda^\flat.
}
\tag{R3-COPRIME-FACTOR}
\]

This is the strongest positive theorem of R3.

## 1.3 The attempted DD capacity transfer fails at a precise place

For \(\ell\ge6\), the normalized complementary factor is a ten-unit:

\[
\boxed{
v_2(\lambda_*)=v_5(\lambda_*)=0.
}
\]

Hence, under \(\varepsilon_*=0\),

\[
v_p(\Omega)
=
v_p(x_*)+v_p(\lambda_*)
=
v_p(x_*),
\qquad p\in\{2,5\}.
\]

Equivalently, all \(2/5\)-depth beyond the forced \(2K\) core is assigned to \(x_*=a_1\).  This is already an inherited exact root-factor theorem.  
Source: fileciteturn24file9

But the actual first denominator in the J2 radial normalization is a ten-unit divisor of \(V=uGH\); reducedness therefore does **not** put a uniform upper bound on \(v_2(a_1)\) or \(v_5(a_1)\).  Thus the required decimal load can legally be absorbed by \(x_*\).

So the desired inequality

\[
v_p(\Omega)
>
v_p(x_*)+v_p(\lambda_*)
\]

cannot be obtained from this allocation: under an exact root the right-hand side equals the left-hand side identically.

Therefore

```text
PRIMITIVE_CAPACITY_ROUTE=FAILED
J2_DD_CAPACITY_TRANSFER=FAILED
```

The failure is not “valuation did not look strong enough”; the failure is that the source has no \(2/5\)-capacity ceiling on the first factor.

## 1.4 Actual-cut re-entry is semantically redundant at the full source level

The backward line proves that, for fixed denominator trace and full numerator word, legal first-two cuts form a fibre of size at most two.  
Source: fileciteturn23file1 fileciteturn23file3

But in Exact Resonance \(R=0\), J2 gives

\[
d=0,\qquad n_2=2g+k,
\]

so the current specialization already fixes the first-two cut exponent.  There is no surviving abstract \(\omega_+/\omega_-\) choice to collide with \(x_*\).

More importantly, the forward/common-\(\mathcal U\) reconstruction theorem has already proved that same-cut norm, exact word equality and reducedness are derived invariants of a complete exact forward state.  
Source: fileciteturn23file4 fileciteturn23file17

Thus source-cut data remain useful as **derived elimination language**, but they do not supply a second independent semantic equation after full source reconstruction.

Therefore the requested source-cut architecture hits K1:

```text
SOURCE_CUT_RESIDUAL_ARCHITECTURE=INFORMATION_REDUNDANT
```

No fake “two-cut collision” is asserted.

## 1.5 One-quantum remains unproved

The desired theorem

\[
0<
|\mathscr R(x_*)|
<
A^3uM
\]

is still not obtained.

The divisibility

\[
A^3uM\mid\mathscr R(x_*)
\]

quantizes the residual, but the actual cut does not produce a new metric estimate locating \(x_*\) within less than one residual quantum of the real root.  This was already the historical stopping point of the decimal-residual line.  
Source: fileciteturn24file11

Hence

```text
ONE_QUANTUM_SEPARATION=UNKNOWN
```

and not `FALSE`.

---

# 2. R2 Frozen Verdict

The following R2 terminal verdict is frozen without reopening quotient/carry architecture:

```text
J2_STATUS=OPEN

FIXED_FIBRE_QUOTIENT_EXPLICITIZATION=PROVED
FIXED_FIBRE_FINITE_PERIODIC_CARRY=PROVED
EXACT_INTEGER_CARRY=PROVED
GLOBAL_UNIFORM_O1_CARRY_ALPHABET=NOT_PROVED
DETERMINISTIC_DEFECT_FLOOR_FREE=PROVED

ONE_TAIL_REGION_CLOSED=NO

DD_STYLE_COMMON_GAP_FOUND=NO

N0_QUOTIENT_COUPLING=NO_PROMOTED_COUPLING

R2_TERMINAL_VERDICT=
QUOTIENT_EXPLICITIZATION_NOT_CLOSURE_CAPABLE
```

Accordingly, \(\mu,\chi,\varrho\) are not reopened as frontier coordinates.

---

# 3. Regular Minimal Survivor

Throughout R3:

\[
J=2,\qquad
S_R<0,\qquad
g\ge4,\qquad
u>1,\qquad
\ell\ge6,
\]

\[
G=10^g,\qquad
K=10^k,\qquad
L=10^\ell,\qquad
k=2g-\ell,
\]

\[
uq=G+1,
\qquad
A=2u+1.
\]

Use

\[
\boxed{M:=L/8.}
\]

The determinant identities are

\[
qA-(2G+q)=2,
\]

\[
u(2G+q)-GA=1.
\]

RCE reconstruction is

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
D_2=ua_3+G\mathcal X.
\]

Useful reconstructed source coordinates are also

\[
h=\frac{N+qZ}{2},
\]

\[
m=\frac{AN+(q+2)Z}{2},
\]

\[
r=\frac G2h-ua_3.
\]

These are the exact RCE quantities used in the historical reconstruction code.  
Source: fileciteturn25file7

---

# 4. Canonical \(x_*\) Construction

Define

\[
d_A:=\gcd(A,D_2).
\]

R3 treats only

\[
\boxed{d_A=1.}
\]

The regular branch has a unique source-selected integer \(x_*\) in

\[
\boxed{
I_x=
\left(
\frac{AG}{10},
\frac{8uD_2}{AL}
\right)
}
\]

after A-adic and decimal synchronization, and it must satisfy

\[
\boxed{x_*^2\equiv Z^2\pmod u.}
\]

The lower endpoint

\[
x_*>\frac{AG}{10}
\]

is not an ambient size guess: it is obtained by combining the actual second numerator digit window with the radial J2.5 equation.  The upper endpoint comes from positivity of the complementary factor.  
Source: fileciteturn24file13

The dependency audit also identifies the selected root with the actual first numerator block:

\[
\boxed{x_*=a_1}
\]

on any genuine source solution.  
Source: fileciteturn24file0

Thus every theorem below acts on the source-selected \(a_1\), not on an arbitrary quadratic root.

---

# 5. Exact Root Factorization

Define

\[
\widetilde F=A\mathcal X^2+ZD_2.
\]

On a root-eligible state,

\[
2K\mid\widetilde F,
\]

so

\[
\Omega:=\frac{\widetilde F}{2K}\in\mathbb Z.
\]

Define

\[
\mathscr R(x)=AMx^2-uD_2x+\Omega,
\]

\[
\lambda(x)=uD_2-AMx.
\]

Then

\[
\boxed{
\mathscr R(x)=\Omega-x\lambda(x).
}
\]

Hence

\[
\boxed{
\mathscr R(x)=0
\iff
\Omega=x\lambda(x).
}
\]

For the canonical source candidate,

\[
\lambda_*:=\lambda(x_*).
\]

Regular source synchronization gives

\[
\boxed{
\mathscr R(x_*)=A^3uM\,\varepsilon_*,
\qquad
\varepsilon_*\in\mathbb Z.
}
\]

Thus

\[
\boxed{
\varepsilon_*=0
\iff
\Omega=x_*\lambda_*.
}
\]

The normalized historical root factor is exactly the same object:

\[
\Lambda=2K\lambda_*,
\]

and full root gives

\[
\widetilde F=x_*\Lambda.
\]

This is source-labelled, not an ambient factorization.  
Source: fileciteturn24file2

---

# 6. Root Factor Ledger

Assume from now on, for contradiction,

\[
\boxed{\varepsilon_*=0.}
\]

Let \(\mathcal U\) denote the actual common radial scale in

\[
a_i=\mathcal U C_i.
\]

To avoid collision with the cyclotomic variable \(u\), \(\mathcal U\) is used only for this source scale.

| Object | Source meaning | Sign | Exact / interval data | \(v_2\) | \(v_5\) | gcd with \(u\) | gcd with \(A\) | cut dependence |
|---|---|---:|---|---:|---:|---:|---:|---|
| \(x_*\) | actual \(a_1=\mathcal U C_1\) | \(+\) | \(AG/10<x_*<uD_2/(AM)\) | unrestricted by present source ceiling | unrestricted | \(1\) | \(\gcd(Z,A)\) via A-root | actual second-block digit used in DRL |
| \(\lambda_*\) | normalized complementary source factor | \(+\) | \(uD_2-AMx_*\) | \(0\) | \(0\) | \(1\) | \(1\) | derived from selected source root |
| \(\Omega\) | normalized product | \(+\) | \(x_*\lambda_*\) | \(v_2(x_*)\) | \(v_5(x_*)\) | \(1\) | depends on \(x_*\) | root-derived |
| \(Z\) | RCE radial source coordinate | \(+\) on live states | \((At-2N)/(q(q+4))\) | \(0\) historically on legal linear states | \(0\) historically | \(1\) | no global unit theorem | source/RCE |
| \(D_2\) | radial weighted coordinate | \(+\) | \(ua_3+G\mathcal X\) | \(0\) | \(0\) | \(1\) | \(1\) in regular branch | source/RCE |

The ten-unit status of the RCE linear coordinates is part of the frozen legal RCE gate.  
Source: fileciteturn25file3

The normalized complement satisfies

\[
\boxed{\gcd(\lambda_*,10)=1}
\]

for \(\ell\ge4\), hence certainly in the current \(\ell\ge6\) chamber.  
Source: fileciteturn24file1

---

# 7. Primitive Nonabsorption

## Lemma 7.1 — PN-1

\[
\boxed{\gcd(x_*,u)=1.}
\]

### Proof

We know

\[
x_*^2\equiv Z^2\pmod u
\]

and

\[
\gcd(Z,u)=1.
\]

If a prime \(p\mid(x_*,u)\), then modulo \(p\),

\[
0\equiv x_*^2\equiv Z^2,
\]

so \(p\mid Z\), contradicting \(\gcd(Z,u)=1\).  Therefore

\[
\gcd(x_*,u)=1.
\qquad\square
\]

The primitive origin of \(\gcd(Z,u)=1\) is inherited from the J2 primitive radial chart.  
Source: fileciteturn20file2

## Lemma 7.2 — \(u\) is a ten-unit

Since

\[
uq=G+1=10^g+1,
\]

every prime divisor of \(u\) divides \(10^g+1\).  Hence neither \(2\) nor \(5\) divides \(u\):

\[
\boxed{\gcd(u,10)=1.}
\]

Because \(M=10^\ell/8\) has only \(2,5\)-support,

\[
\boxed{\gcd(u,M)=1.}
\]

## Lemma 7.3 — PN-2

\[
\boxed{\gcd(\lambda_*,u)=1.}
\]

### Proof

Modulo \(u\),

\[
A=2u+1\equiv1\pmod u,
\]

and

\[
\lambda_*
=
uD_2-AMx_*
\equiv
-Mx_*
\pmod u.
\]

By Lemmas 7.1–7.2,

\[
\gcd(Mx_*,u)=1.
\]

Hence

\[
\boxed{\gcd(\lambda_*,u)=1}.
\qquad\square
\]

This proves the first requested J2 primitive nonabsorption theorem.

---

## Lemma 7.4 — regular \(A\)-nonabsorption of the complementary factor

\[
\boxed{\gcd(\lambda_*,A)=1.}
\]

### Proof

Modulo \(A\),

\[
\lambda_*
\equiv
uD_2
\pmod A.
\]

Now

\[
\gcd(u,A)=1
\]

because \(A=2u+1\), and regularity gives

\[
\gcd(D_2,A)=1.
\]

Therefore

\[
\gcd(\lambda_*,A)=1.
\qquad\square
\]

No analogous theorem is asserted for \(x_*\): A-root gives

\[
Kx_*\equiv-Z\pmod A,
\]

with \(K\) invertible modulo \(A\), so only

\[
\boxed{\gcd(x_*,A)=\gcd(Z,A)}
\]

is justified.  There is no frozen global theorem \(\gcd(Z,A)=1\).

---

## Lemma 7.5 — \(D_2\) is a \(u\)-unit

The primitive chart gives

\[
d_2\equiv-\frac z2\pmod u,
\]

with \(\gcd(z,u)=1\).  After multiplying by the common radial scale, which is also coprime to \(u\), one gets

\[
\boxed{\gcd(D_2,u)=1.}
\]

This is consistent with the direct legal RCE ten-unit/gcd audit.  
Source: fileciteturn19file5

---

## Lemma 7.6 — primitive decontenting of \((C_1,d_2)\)

On a genuine regular source state,

\[
\boxed{\gcd(C_1,d_2)=1.}
\tag{PCD}
\]

### Proof

Work in the frozen negative J2 normal form

\[
C_3=2r-qw,
\]

\[
d_2=2ur-w,
\]

\[
Ar-w=mH,
\]

\[
GKC_1=AC_2+m,
\]

\[
H^2C_1^2+w^2=T d_2,
\]

with \(H=G/2\), and with the primitive sphere

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

\[
P_1=GHC_1,\qquad
P_2=uGC_2,\qquad
P_3=uC_3,\qquad
Q_0=P_2+d_2.
\]

These are frozen J2 identities.  
Source: fileciteturn21file9

Suppose a prime

\[
p\mid C_1,\qquad p\mid d_2.
\]

Because \(d_2\) is a ten-unit,

\[
p\ne2,5.
\]

Because \(\gcd(C_1,u)=1\),

\[
p\nmid u.
\]

Because \(D_2=\mathcal U d_2\) and \(d_A=\gcd(A,D_2)=1\),

\[
p\nmid A.
\]

From

\[
H^2C_1^2+w^2=T d_2
\]

we obtain

\[
p\mid w.
\]

From

\[
d_2=2ur-w
\]

and \(p\nmid2u\),

\[
p\mid r.
\]

Then

\[
Ar-w=mH
\]

gives \(p\mid mH\).  Since \(H=G/2\) has only \(2,5\)-support and \(p\ne2,5\),

\[
p\mid m.
\]

Now

\[
GKC_1=AC_2+m
\]

forces

\[
p\mid AC_2,
\]

and \(p\nmid A\), hence

\[
p\mid C_2.
\]

Finally

\[
C_3=2r-qw
\]

gives

\[
p\mid C_3.
\]

Therefore \(p\) divides

\[
P_1,\quad P_2,\quad P_3,
\]

and because

\[
Q_0=P_2+d_2,
\]

also \(p\mid Q_0\).  This contradicts primitive normalization

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

Hence no such \(p\) exists:

\[
\boxed{\gcd(C_1,d_2)=1}.
\qquad\square
\]

---

## Theorem 7.7 — Canonical Radial Overlap Theorem

Let

\[
x_*=\mathcal U C_1,
\qquad
D_2=\mathcal U d_2
\]

be the source radialization.  Then

\[
\boxed{
\gcd(x_*,D_2)=\mathcal U.
}
\]

Moreover,

\[
\boxed{
\gcd(x_*,\lambda_*)=\mathcal U.
}
\]

### Proof

By Lemma 7.6,

\[
\gcd(C_1,d_2)=1,
\]

so

\[
\gcd(x_*,D_2)
=
\mathcal U\gcd(C_1,d_2)
=
\mathcal U.
\]

Next,

\[
\lambda_*=uD_2-AMx_*.
\]

Thus

\[
\gcd(x_*,\lambda_*)
=
\gcd(x_*,uD_2).
\]

By PN-1,

\[
\gcd(x_*,u)=1,
\]

hence

\[
\gcd(x_*,uD_2)=\gcd(x_*,D_2)=\mathcal U.
\qquad\square
\]

This is stronger than the requested “controlled by an explicit source divisor”: the gcd is exactly the actual common radial scale.

---

## Corollary 7.8 — primitive coprime factor allocation

Write

\[
\lambda_*=\mathcal U\lambda^\flat.
\]

Then

\[
\boxed{\gcd(C_1,\lambda^\flat)=1}
\]

and, under \(\varepsilon_*=0\),

\[
\boxed{
\Omega
=
\mathcal U^2 C_1\lambda^\flat.
}
\]

Thus the root product has a canonical source orientation:

- \(\mathcal U^2\): common radial content;
- \(C_1\): primitive first-root factor;
- \(\lambda^\flat\): primitive complementary factor;
- \(C_1\) and \(\lambda^\flat\) are coprime.

---

## Corollary 7.9 — overlap-prime propagation is legal, not contradictory

If a prime

\[
p\mid x_*,
\qquad
p\mid\lambda_*,
\]

then by Theorem 7.7,

\[
p\mid\mathcal U.
\]

Hence \(p\) is a legitimate source radial-content prime.

This kills the hoped-for universal argument

\[
p\mid x_*,\lambda_*
\Longrightarrow
p\mid u
\text{ or another forbidden primitive factor}.
\]

The overlap is not accidental: it is exactly the source scale.

Therefore the “forced-overlap prime” closure route does not close regular J2.

---

## Source-factor audit

The rigorously justified status is:

| factor | \(x_*\) absorption | \(\lambda_*\) absorption | verdict |
|---|---|---|---|
| \(u\) | forbidden | forbidden | **PROVED** |
| \(A\) | may share through \(Z\) | forbidden | partial |
| \(K\) | allowed in principle | forbidden because ten-unit | asymmetric |
| \(G\) | allowed in principle | forbidden because ten-unit | asymmetric |
| \(D_2\) | overlap exactly \(\mathcal U\) | overlap exactly \(\mathcal U\) with \(D_2\) as well | **PROVED** |
| \(Z\) | no global extra gcd theorem | no global extra gcd theorem | OPEN |
| \(q\) | no uniform exclusion theorem | no uniform exclusion theorem | OPEN |
| \(q+4\) | no uniform exclusion theorem | no uniform exclusion theorem | OPEN |

No unsupported coprimality with \(q,q+4,Z\) is inserted.

---

# 8. Actual-Cut Reconstruction

The backward exact cut theorem uses fixed denominator trace \(T\), full numerator word \(\mathbf A\), and legal cut exponent \(n\).  If

\[
P=\left\lfloor\frac{\mathbf A}{10^{n_3}}\right\rfloor,
\]

then a legal first-two cut \(n\) gives

\[
a_1=\left\lfloor\frac{P}{10^n}\right\rfloor,
\qquad
a_2=P\bmod10^n,
\]

and weighted prefix norm

\[
\boxed{
N_{\rm cut}
=
b_2^2a_1^2+b_1^2a_2^2.
}
\]

For fixed \((T,\mathbf A)\), the legal cut fibre has size at most two.  
Source: fileciteturn23file0 fileciteturn23file3

## 8.1 J2 resonance fixes the cut exponent

Exact denominator resonance gives

\[
d=0,
\]

hence

\[
\boxed{n_2=2g+k.}
\]

Therefore in the present J2 chamber the relevant first-two cut exponent is not an independent binary parameter.

This is an important specialization:

\[
\boxed{
\text{general backward fibre }\le2
\not\Rightarrow
\text{two live J2 cut labels}.
}
\]

---

## 8.2 RCE-to-source reconstruction map

The RCE reconstruction already supplies

\[
m=\frac{AN+(q+2)Z}{2}.
\]

The radialized J2.5 equation is

\[
GKa_1=Aa_2+m.
\]

Hence for a candidate \(x\),

\[
\boxed{
a_{2,\rm src}(x)
=
\frac{GKx-m}{A}.
}
\tag{CUT-SRC-a2}
\]

The corresponding first-two source word is

\[
\boxed{
P_{12,\rm src}(x)
=
x\,10^{n_2}+a_{2,\rm src}(x),
\qquad
n_2=2g+k.
}
\tag{CUT-SRC-WORD}
\]

Thus the canonical root gives an exact source-image candidate

\[
x_*
\longmapsto
\left(
P_{12,\rm src}(x_*),
N_{\rm src}(x_*)
\right).
\]

If one uses the specialized denominator normalization
\(b_1=u,\ b_2=H=G/2\), the weighted prefix norm is

\[
\boxed{
N_{\rm src}(x)
=
H^2x^2
+
u^2 a_{2,\rm src}(x)^2.
}
\tag{CUT-SRC-NORM}
\]

The denominator identification follows from the common-\(V\) gcd profile in the J2 normal form.

---

## 8.3 Exact same-cut integer tests

Let \(P_{12,\rm word}\) be the first-two prefix extracted from the full numerator word at the prescribed \(n_3\).

Define

\[
\boxed{
\mathfrak D_{\rm word}(x)
:=
A\left(
P_{12,\rm word}-10^{n_2}x
\right)
-
(GKx-m).
}
\tag{D-WORD}
\]

Then

\[
\mathfrak D_{\rm word}(x)=0
\]

is exactly the same-cut word realization equation.

Likewise define

\[
\boxed{
\mathfrak D_{\rm norm}(x)
:=
b_2^2x^2
+
b_1^2a_{2,\rm src}(x)^2
-
N_{\rm cut}.
}
\tag{D-NORM}
\]

Then

\[
\mathfrak D_{\rm norm}(x)=0
\]

is exactly the same-cut weighted-norm condition.

These are the requested concrete integer cut invariants.

---

# 9. Source-Cut Image Collision

The key question is whether

\[
\varepsilon_*=0
\]

forces either

\[
\mathfrak D_{\rm word}(x_*)\ne0
\]

or

\[
\mathfrak D_{\rm norm}(x_*)\ne0.
\]

R3 finds no such theorem.

Instead, the full forward/common-\(\mathcal U\) reconstruction theorem proves that once the exact primitive state, gcd profile, legal common radial scale and numerator digit windows are all retained, actual word equality, individual reducedness and same-cut norm are automatic consequences.  
Source: fileciteturn23file4 fileciteturn23file17

Therefore:

### Semantic level

\[
\boxed{
\mathfrak D_{\rm word}
\text{ and }
\mathfrak D_{\rm norm}
\text{ do not add a new source predicate after full forward reconstruction.}
}
\]

### Proof-theoretic level

They remain valid derived identities and could still be useful if one can rewrite them in reduced RCE parameters and obtain a contradiction **before** assuming full source realization.

R3 does not obtain such a reduced contradiction.

Thus the requested new independent collision does not materialize.

```text
SOURCE_CUT_RESIDUAL_EXCLUSION=
INFORMATION_REDUNDANT_AT_FULL_SOURCE_LEVEL;
RCE_TO_SOURCE_IMAGE_MEMBERSHIP_FORMULATED_ONLY

SOURCE_CUT_RESIDUAL_ARCHITECTURE=
INFORMATION_REDUNDANT
```

This is K1.

No R3-S2 claim is made.

---

# 10. \(2\)-adic Capacity

For \(\ell\ge4\),

\[
\gcd(\lambda_*,10)=1.
\]

Therefore

\[
\boxed{v_2(\lambda_*)=0.}
\]

Under exact root,

\[
\Omega=x_*\lambda_*,
\]

hence

\[
\boxed{
v_2(\Omega)=v_2(x_*).
}
\tag{V2-OMEGA}
\]

For the raw factors,

\[
\Lambda=2K\lambda_*,
\]

so

\[
\boxed{
v_2(\Lambda)=k+1.
}
\]

And

\[
\widetilde F
=
2K\Omega
=
2Kx_*\lambda_*,
\]

so

\[
\boxed{
v_2(\widetilde F)=k+1+v_2(x_*).
}
\]

This is not merely a bound; it is the exact load allocation.

## Capacity comparison

The desired contradiction would require a source theorem

\[
v_2(x_*)\le C_2
\]

with

\[
v_2(\Omega)>C_2.
\]

But the source reducedness condition on the first block has denominator \(b_1\) coprime to \(10\).  Therefore reducedness does not prohibit an arbitrarily deep factor \(2^\alpha\) in \(a_1=x_*\).

Neither

\[
x_*^2\equiv Z^2\pmod u
\]

nor A-root acts at the prime \(2\), since \(u,A\) are odd ten-units.

Therefore no uniform source ceiling for \(v_2(x_*)\) is available.

Conclusion:

```text
TWO_ADIC_CAPACITY_OVERLOAD=FALSE_AS_CURRENT_ARCHITECTURE
```

meaning: the proposed overload inequality cannot follow from the present source constraints.

---

# 11. \(5\)-adic Capacity

The normalized complement satisfies already for \(\ell\ge3\)

\[
\boxed{v_5(\lambda_*)=0.}
\]

Thus, under exact root,

\[
\boxed{
v_5(\Omega)=v_5(x_*).
}
\tag{V5-OMEGA}
\]

For the raw complementary factor,

\[
\boxed{
v_5(\Lambda)=k.
}
\]

For the raw root product,

\[
\boxed{
v_5(\widetilde F)=k+v_5(x_*).
}
\]

Again the first factor is allowed to carry the entire residual \(5\)-depth: \(b_1\) is a \(5\)-unit, and neither the \(u\)-square nor the A-root congruence imposes a \(5\)-adic ceiling on \(x_*\).

Therefore

```text
FIVE_ADIC_CAPACITY_OVERLOAD=FALSE_AS_CURRENT_ARCHITECTURE
```

for the same structural reason.

---

## 11.1 Exact capacity verdict

For \(p\in\{2,5\}\),

\[
\boxed{
v_p(\Omega)
=
v_p(x_*)+v_p(\lambda_*)
=
v_p(x_*).
}
\]

Thus the source absorption capacity is exactly large enough to absorb all required \(2/5\)-load.

This triggers K2:

```text
PRIMITIVE_CAPACITY_ROUTE=FAILED
```

and the coefficient-bit ladder is stopped here.

---

# 12. Archimedean Factor Capacity

From the root interval,

\[
\frac{AG}{10}<x_*<\frac{uD_2}{AM}.
\]

Therefore

\[
x_*>0
\]

and

\[
\lambda_*
=
uD_2-AMx_*
>0.
\]

Also

\[
\lambda_*
<
uD_2-\frac{A^2MG}{10}.
\]

Hence any exact root has

\[
\Omega=x_*\lambda_*>0.
\]

The product

\[
f(x)=x(uD_2-AMx)
\]

is a concave quadratic, with formal maximum

\[
\frac{(uD_2)^2}{4AM}
\]

at its vertex.

However, no uniform source inequality of the form

\[
x_*\lambda_*<\Omega
\]

or

\[
x_*\lambda_*>\Omega
\]

can be obtained from the same data, because under the assumed root

\[
\Omega=x_*\lambda_*
\]

is precisely the equality being tested.

A useful Archimedean attack therefore requires an **independent** source location theorem for \(x_*\) or \(\lambda_*\).  The recovered cut equations do not supply one after full source reconstruction.

Thus

```text
ARCHIMEDEAN_FACTOR_CAPACITY=OPEN_NO_NEW_INDEPENDENT_BOUND
```

---

# 13. One-Quantum Separation Audit

The quantization theorem is

\[
\boxed{
A^3uM\mid\mathscr R(x_*).
}
\]

Hence if \(\mathscr R(x_*)\ne0\),

\[
|\mathscr R(x_*)|
\ge A^3uM.
\]

To prove residual nonvanishing by one-quantum separation one would need

\[
\boxed{
0<
|\mathscr R(x_*)|
<
A^3uM.
}
\]

The historical decimal-residual campaign explicitly left this as open.  
Source: fileciteturn24file11

R3 tests whether the actual-cut fibre and the unique canonical \(x_*\) supply the missing strict upper bound.

They do not:

1. in Exact Resonance the cut exponent \(n_2=2g+k\) is already fixed;
2. the lower root endpoint \(x_*>AG/10\) already consumed the actual second-digit window;
3. same-cut norm is semantically derived on the complete source state;
4. no new bound on the distance from \(x_*\) to a real zero of \(\mathscr R\) is produced.

Therefore

```text
ONE_QUANTUM_SEPARATION=UNKNOWN
```

not `PROVED`, not `FALSE`.

---

# 14. Discrete / Non-square Audit

A possible final route was:

\[
\varepsilon_*=0
\Longrightarrow
\text{explicit square / norm-square / exact-divisor condition}.
\]

But the old discriminant square condition is already equivalent to the integral-root factor system once root divisibility is retained.  Reintroducing it without a new independent cut invariant merely rewrites

\[
\Omega=x_*\lambda_*.
\]

R3 finds no new explicit integer

\[
\mathfrak D_{\rm cut}
\]

such that

\[
\varepsilon_*=0
\Longrightarrow
\mathfrak D_{\rm cut}=Y^2
\]

and whose nonsquareness is independently forced by source data.

No resultant or Gröbner calculation is promoted, because without a second independent source equation it would only eliminate variables inside a tautologically equivalent root system and risk K4.

Therefore

```text
DISCRETE_NONSQUARE_ROUTE=
NO_NEW_INDEPENDENT_SQUARE_CONDITION
```

and remains open as a future derived tool only if a genuinely new source invariant is first found.

---

# 15. High-Tail Regular Branch

Branch H:

\[
d_A=1,\qquad
\delta>0,
\qquad
q>1.
\]

R2 gives

\[
s=0.
\]

This makes the Euclidean defect especially simple, but R3 deliberately does not reopen the carry quotient.

The new root-factor facts remain valid:

\[
\gcd(x_*,u)=\gcd(\lambda_*,u)=1,
\]

\[
\gcd(x_*,\lambda_*)=\mathcal U,
\]

\[
v_2(\lambda_*)=v_5(\lambda_*)=0.
\]

Nevertheless:

- the overlap \(\mathcal U\) is legal radial content;
- the entire \(2/5\)-load may sit in \(x_*\);
- no independent cut equation survives at the full source level;
- no one-quantum strict upper bound is proved.

Therefore

\[
\boxed{
d_A=1,\ \delta>0,\ q>1:
\quad
\textbf{REDUCED / OPEN}.
}
\]

No `REGULAR_HIGH_TAIL=CLOSED` certificate is issued.

---

# 16. Boundary Regular Branch

Branch B:

\[
d_A=1,\qquad
\delta=0,\qquad
q>1.
\]

This is the chamber where the historical finite diagnostic corpus is richest, but finite extinction is not a global theorem.

The exact cut exponent is still fixed by \(d=0\), and the backward same-cut norm is still semantically derived on a full source state.

The one-quantum route was specifically tested here historically and remains open.

The new factor theorem strengthens the boundary description but does not kill it:

\[
\Omega
=
\mathcal U^2C_1\lambda^\flat,
\qquad
\gcd(C_1,\lambda^\flat)=1.
\]

Therefore

\[
\boxed{
d_A=1,\ \delta=0,\ q>1:
\quad
\textbf{REDUCED / OPEN}.
}
\]

---

# 17. Reverse Regular Branch

Branch R:

\[
d_A=1,\qquad
\delta<0,\qquad
q>1.
\]

The reverse zero-tail route remains retired as required.  R3 treats only the reverse nonzero-tail survivor.

The canonical factor and primitive nonabsorption lemmas are sign-independent once one is inside the same regular root chart.  The same obstruction to capacity closure remains:

\[
v_p(\Omega)=v_p(x_*),
\qquad p=2,5,
\]

with no source ceiling on \(v_p(x_*)\).

No reverse-specific source-cut invariant becomes independent.

Therefore

\[
\boxed{
d_A=1,\ \delta<0,\ q>1:
\quad
\textbf{REDUCED / OPEN}.
}
\]

---

# 18. \(N_0\) Secondary Prefilter Audit

Use

\[
B=2G+q,
\]

\[
C_-=2GK-B,
\qquad
C_+=2GK+B,
\]

\[
N_0=2+u^2C_- - C_+.
\]

Frozen properties include

\[
\gcd(C_-,C_+)=1,
\]

\[
N_0\equiv2\pmod{C_\pm},
\]

\[
N_0\equiv2\pmod{u^2},
\]

\[
N_0\equiv1\pmod G,
\]

\[
v_5(N_0-1)=g,
\qquad
v_2(N_0-1)=g+1.
\]

85-R1 already classified \(N_0\) as an outer Gaussian/split prefilter rather than a terminal source freedom.  
Source: fileciteturn19file6

R3 finds no direct implication

\[
N_0\text{ condition}
\Longrightarrow
\Omega\ne x_*\lambda_*.
\]

Nor does \(N_0\) create a new cut-image equation.

Therefore

```text
N0_STATUS=OUTER_PREFILTER_ONLY
N0_PROMOTED_IN_R3=NO
```

No general \(N_0\) split classification is reopened.

---

# 19. Computational Reconnaissance

R3 uses computation only as regression/provenance support; no finite census is promoted to a global theorem.

Historical exact computation establishes:

1. root-layer boundary diagnostic states exist before the final gates;
2. \(d_A=1\) is a genuinely populated regular chamber;
3. singular \(d_A>1\) also occurs, so regularity cannot be assumed globally;
4. historical regular finite corpora die before/full root, but this is not a uniform proof.

For example, the PRCC10 boundary diagnostic recorded

```text
d_A=1  : 53 cells
d_A=3  : 21 cells
d_A=7  : 4 cells
d_A=11 : 1 cell
```

and explicitly falsified the old conjecture \(\gcd(D_2,A)=1\) globally.  
Source: fileciteturn20file12

R3 does **not** use these counts as evidence for regular closure.

The new R3 statements are symbolic:

- PN-1 / PN-2;
- \(\gcd(C_1,d_2)=1\);
- \(\gcd(x_*,D_2)=\gcd(x_*,\lambda_*)=\mathcal U\);
- exact \(2/5\) load identities;
- cut semantic redundancy audit.

---

# 20. Counterexamples / Failed Routes

## 20.1 Forced overlap prime

Desired pattern:

\[
p\mid x_*,
\qquad
p\mid\lambda_*
\Longrightarrow
p\mid u
\text{ or another forbidden source factor}.
\]

Actual theorem:

\[
p\mid x_*,\lambda_*
\Longrightarrow
p\mid\mathcal U.
\]

This is legal radial content.

**Verdict: FAILED as closure route.**

---

## 20.2 \(2/5\)-capacity overload

Desired:

\[
v_p(\Omega)
>
v_p(x_*)+v_p(\lambda_*).
\]

Actual root allocation:

\[
v_p(\Omega)
=
v_p(x_*)+v_p(\lambda_*)
=
v_p(x_*).
\]

No source ceiling on \(v_p(x_*)\).

**Verdict: FAILED structurally.**

---

## 20.3 Cut fibre \(2\to0\)

The general backward fibre is \(\le2\), but current resonance fixes \(n_2=2g+k\).  There is no universal two-point pair left to test.

**Verdict: proposed two-case collision is not the current specialized geometry.**

---

## 20.4 Same-cut norm as independent gate

Backward-on-forward redundancy proves it is derived on a full source state.

**Verdict: SEMANTICALLY REDUNDANT.**

---

## 20.5 One quantum

No independent metric separation is obtained.

**Verdict: UNKNOWN, not falsified.**

---

## 20.6 Reopened discriminant

Without a new independent source condition, the square discriminant only repackages the root equation.

**Verdict: NO LEVERAGE.**

---

## 20.7 Elimination

No elimination was promoted because the available equations are already equivalent/derived; a high-degree resultant would not reduce semantic dimension.

```text
ELIMINATION_NO_LEVERAGE
```

---

# 21. Proven vs Computational Statements

## NEW PROVED

1. PN-1:
   \[
   \gcd(x_*,u)=1.
   \]

2. PN-2:
   \[
   \gcd(\lambda_*,u)=1.
   \]

3. Regular complementary \(A\)-unit:
   \[
   \gcd(\lambda_*,A)=1.
   \]

4. Primitive decontenting:
   \[
   \gcd(C_1,d_2)=1.
   \]

5. Canonical Radial Overlap:
   \[
   \gcd(x_*,D_2)
   =
   \gcd(x_*,\lambda_*)
   =
   \mathcal U.
   \]

6. Coprime primitive factor allocation:
   \[
   \Omega
   =
   \mathcal U^2C_1\lambda^\flat,
   \qquad
   \gcd(C_1,\lambda^\flat)=1.
   \]

7. Exact \(2/5\)-load identities:
   \[
   v_2(\Omega)=v_2(x_*),
   \qquad
   v_5(\Omega)=v_5(x_*).
   \]

8. Current source capacity has no \(2/5\) ceiling on \(x_*\).

9. RCE-to-source actual-cut map:
   \[
   a_{2,\rm src}(x)=\frac{GKx-m}{A},
   \]
   with exact word/norm membership equations.

10. Source-cut semantic independence fails after full source reconstruction.

## FROZEN / INHERITED

1. \(x_*=a_1\) on genuine root.
2. \(\Lambda=2K\lambda_*\).
3. \(\gcd(\lambda_*,10)=1\) for \(\ell\ge4\).
4. canonical \(x_*\) uniqueness.
5. residual quantum
   \[
   A^3uM\mid\mathscr R(x_*).
   \]
6. backward cut fibre \(\le2\).
7. Backward-on-Forward Redundancy Theorem.

## COMPUTATIONAL ONLY

1. historical 53 regular boundary root-layer diagnostic cells;
2. historical finite-corpus extinction;
3. numerical distributions of singular gcd content.

No global statement depends on those finite counts.

## OPEN

1. \(\varepsilon_*\ne0\) globally in regular J2;
2. one-quantum separation;
3. an independent reduced source-cut contradiction;
4. an odd-prime capacity theorem beyond \(u,A,10\);
5. a new same-cut nonsquare theorem;
6. all three regular tail closures.

---

# 22. Regular Tail Closure Table

| Regular region | status |
|---|---|
| \(d_A=1,\ \delta>0,\ q>1\) | **REDUCED / OPEN** |
| \(d_A=1,\ \delta=0,\ q>1\) | **REDUCED / OPEN** |
| \(d_A=1,\ \delta<0,\ q>1\) | **REDUCED / OPEN** |

No regular tail region is closed in R3.

---

# 23. R3 Terminal Verdict

The most accurate architecture ledger is:

```text
J2_STATUS=OPEN
REGULAR_J2_STATUS=OPEN

CANONICAL_ROOT_FACTOR_ALLOCATION=PROVED
PRIMITIVE_NONABSORPTION_U=PROVED
CANONICAL_RADIAL_OVERLAP_THEOREM=PROVED
PRIMITIVE_DECONTENTED_FACTOR_COPRIMALITY=PROVED

SOURCE_CUT_RESIDUAL_EXCLUSION=
INFORMATION_REDUNDANT_AT_FULL_SOURCE_LEVEL;
RCE_TO_SOURCE_IMAGE_TEST_FORMULATED_ONLY

SOURCE_CUT_RESIDUAL_ARCHITECTURE=
INFORMATION_REDUNDANT

PRIMITIVE_CAPACITY_ROUTE=
FAILED_NO_2_5_CEILING_ON_X_STAR

J2_DD_CAPACITY_TRANSFER=
FAILED_AT_SOURCE_CAPACITY_STEP

TWO_ADIC_CAPACITY_OVERLOAD=FAILED
FIVE_ADIC_CAPACITY_OVERLOAD=FAILED

ONE_QUANTUM_ROUTE=
UNKNOWN_NOT_PROVED

ONE_QUANTUM_SEPARATION=
UNKNOWN

DISCRETE_NONSQUARE_ROUTE=
NO_NEW_INDEPENDENT_CONDITION

ELIMINATION_STATUS=
NO_LEVERAGE

REGULAR_HIGH_TAIL=OPEN
REGULAR_BOUNDARY=OPEN
REGULAR_REVERSE=OPEN

R3_SUCCESS_LEVEL=R3-S1

R3_TERMINAL_VERDICT=
SOURCE_CUT_RESIDUAL_ARCHITECTURE_FAILS
```

The failure is rigorous and localized:

\[
\boxed{
\text{Source labels are recovered;}
}
\]

\[
\boxed{
\text{primitive nonabsorption is recovered;}
}
\]

but

\[
\boxed{
\text{source capacity is not smaller than required factor load.}
}
\]

Hence the DD mechanism does **not** transfer far enough to close J2.

---

# 24. R4 Attack Target

Because

```text
REGULAR_J2_CLOSED=NO
```

R4 is **not allowed** to enter the singular \(d_A>1\) line.

Because

```text
SOURCE_CUT_RESIDUAL_ARCHITECTURE=INFORMATION_REDUNDANT
```

R4 must also **not** perform a fourth repackaging of \(\varepsilon_*\), carry, quotient, or same-cut norm.

The strongest new object produced by R3 is the primitive-decontented factorization

\[
\boxed{
\Omega
=
\mathcal U^2C_1\lambda^\flat,
\qquad
\gcd(C_1,\lambda^\flat)=1.
}
\]

Therefore the natural R4 target is a genuinely different architecture:

\[
\boxed{
\textbf{Primitive Odd-Prime Factor Allocation}
\times
\textbf{Radial-Content Recovery}
\times
\textbf{Source Divisor Image}.
}
\]

More concretely, R4 should ask whether after removing the now-understood legal radial square \(\mathcal U^2\), some **odd ten-free source divisor** of the explicit RCE quantity

\[
\frac{\Omega}{\mathcal U^2}
=
C_1\lambda^\flat
\]

is forced simultaneously into two coprime source-labelled factors, or is forced into the wrong factor by one of:

\[
GKC_1=AC_2+m,
\]

\[
H^2C_1^2+w^2=T d_2,
\]

\[
C_3=2r-qw,
\]

the RCE expressions for \(N,t,Z,a_3,\mathcal X,D_2\), or the exact cyclotomic relation \(uq=G+1\).

The new question is **not**

> why is the residual not zero?

but rather

\[
\boxed{
\text{if the residual is zero, can the primitive coprime product }
C_1\lambda^\flat
\text{ carry the required odd source divisor allocation?}
}
\]

This attacks the only part of the factor load not already shown to be harmless.

A second admissible R4 architecture is to derive a genuinely new **reduced RCE source-image divisor** before full common-\(\mathcal U\) reconstruction.  Such a divisor must not be a reformulation of same-cut norm, U-square, A-root, decimal residue, or the root equation.

Until one of these new source constraints is found, the regular branch remains open.

---

# Final statement

85-R3 does **not** end with

\[
q>1,\ d_A=1
\Longrightarrow
\varepsilon_*\ne0.
\]

It ends with a sharper explanation of why the proposed closure mechanism stops:

\[
\boxed{
\Omega=x_*\lambda_*
=
\mathcal U^2C_1\lambda^\flat,
\qquad
\gcd(C_1,\lambda^\flat)=1,
}
\]

\[
\boxed{
\gcd(x_*,\lambda_*)=\mathcal U,
}
\]

\[
\boxed{
\gcd(x_*,u)=
\gcd(\lambda_*,u)=1,
}
\]

but

\[
\boxed{
v_p(\Omega)=v_p(x_*),
\qquad p=2,5,
}
\]

and the actual source imposes no uniform \(2/5\)-capacity ceiling on \(x_*\).

At the same time, the actual-cut equations are semantically derived once the exact forward/common-radial source is retained.

Thus the precise R3 lesson is:

\[
\boxed{
\textbf{primitive nonabsorption survives the DD transfer,}
}
\]

\[
\boxed{
\textbf{source-capacity overload does not.}
}
\]

The regular J2 branch remains the only permitted target for R4.
