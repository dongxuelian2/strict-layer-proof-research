# J2-65-R12 — Independent-Gate Reintegration × Brauer-to-Gaussian Witness × Radial Source-Conic Incidence

**Scope:** Strict Layer — A1-only — Exact Resonance \(R=0\) — \(J=2\) — \(q>1\) main line  
**Round:** 65 第十二轮 / A1 统一终端线第三十七轮  
**Status:** \(\boxed{\mathbf{J2\ OPEN}}\)

## 1. Executive verdict

R12 gives a decisive **positive witness result** and an equally decisive **negative information-retention result**.

### 1.1 Explicit rational source-attached Gaussian witness exists

The R8 fixed-norm identity is point-level, not merely Brauer-level. After the R9 structural norm quotient, every actual rational source point on a split fibre determines

\[
\theta=a+b\sqrt{-\rho},\qquad a^2+\rho b^2=N.
\]

Since

\[
S=2KuG,\qquad N=S^2-\rho,
\]

define

\[
\boxed{
z_{\mathbf Q}
=
\frac{a+iSb}{1+ib}
\in\mathbf Q(i).
}
\]

Then

\[
\boxed{N_{\mathbf Q(i)/\mathbf Q}(z_{\mathbf Q})=N.}
\]

Writing \(z_{\mathbf Q}=x_G+iy_G\), the inverse formulas are

\[
\boxed{
b=\frac{y_G}{S-x_G},
\qquad
a=\frac{Sx_G-N}{S-x_G}.
}
\]

The denominator \(S-x_G\) cannot vanish on an actual \(q>1\) fibre because
\(\rho=S^2-N>0\).

Therefore

```text
BRAUER_TO_GAUSSIAN_WITNESS_TYPE=EXPLICIT_RATIONAL
```

### 1.2 R10 integral Gaussian witness is not source-canonical

R10 requires

\[
z_{\mathbf Z}\in\mathbf Z[i],\qquad z_{\mathbf Z}\bar z_{\mathbf Z}=N
\]

to form

\[
H=
\begin{pmatrix}
D_+&z_{\mathbf Z}\\
\bar z_{\mathbf Z}&D_-
\end{pmatrix}.
\]

Starting from the source-attached \(z_{\mathbf Q}\), define

\[
\boxed{
\mathcal T_{\rm int}(z_{\mathbf Q})
=
\{\varepsilon\in\mathbf Q(i)^\times:
\varepsilon\bar\varepsilon=1,\ 
\varepsilon z_{\mathbf Q}\in\mathbf Z[i]\}.
}
\]

If \(z_{\mathbf Z}\) is any integral representation of \(N\), then
\(\varepsilon=z_{\mathbf Z}/z_{\mathbf Q}\) has norm one. Conversely every
\(\varepsilon\in\mathcal T_{\rm int}\) gives an integral representation.

Hence the unspecified integralization step ranges over the full integral Gaussian
norm fibre. The integral \(z\), its phase, the R11 first-shell type and the
continuant word are not source-attached invariants unless this torsor choice is retained.

This is the central R12 theorem:

\[
\boxed{
\textbf{Brauer/Hermitian compression forgets the radial source-lattice data
needed by }\mathcal I_{\rm primitive}+\mathcal W_{\rm digit}.
}
\]

Consequently

```text
PURE_CONTINUANT_LAYER_ADDS_NEW_INDEPENDENT_GATE=FALSE
PRIMITIVE_DIGIT_GATES_VISIBLE_IN_HERMITIAN_MODULI=FALSE
```

and no second Gaussian digit is analyzed.

---

## 2. Frozen actual inputs

R11 is frozen as terminal coordinate theory:

- one primitive determinant-\(-2\) Hermitian class;
- one cusp;
- full automorphism/cusp stabilizer;
- terminating halving reduction;
- Hermitian continuant recurrence;
- diagonal map
  \[
  D_+=\Phi(p_c,r_c),\qquad D_-=\Phi(q_c,s_c);
  \]
- level-\(u\) isotropic basis obstruction = FALSE;
- first shell = norm 1 or norm 2, both OPEN.

R1 is frozen as four independent classes

\[
\mathcal S,\qquad\mathcal E,\qquad\mathcal I,\qquad\mathcal W.
\]

The independent gates restored here are

\[
\gcd(Z,u)=1,\qquad\gcd(x,u)=1,
\]

and LOW/UP.

No R3/R4/R5 cell, tube, bracket or residual campaign is reopened.

---

## 3. R7 → R8 point-level witness

Use

\[
T=dt,\qquad Y=dx,\qquad r=T/\alpha,\quad y=Y/\alpha.
\]

R7 writes the conic as

\[
A_c(r)+D_cy^2+\lambda yL_c(r)=0,\qquad\lambda=K/G.
\]

The moving completed square is

\[
z_1=2D_cy+\lambda L_c(r),
\qquad
w=2ar+b,
\]

with

\[
w^2-4az_1^2=\Delta_B.
\]

For R8's fixed presentation define

\[
H_c=4A_cC_c-B_c^2,
\qquad
J_A=2A_cF_c-B_cE_c,
\]

\[
V=2A_c\alpha+B_cT+\lambda E_cY,
\qquad
W=H_cT+\lambda J_AY.
\]

R8 proves

\[
W^2+H_cV^2=-16A_c\det(M)Y^2.
\]

Put

\[
s_H=2q(X+1)(q+4)c,
\qquad H_c=s_H^2R,
\]

and

\[
Q_0=4Xq^3(X+1)(q+4)^2c^2.
\]

Then

\[
\boxed{
\eta=
\frac{W/Y+s_H(V/Y)\sqrt{-R}}{Q_0}
}
\]

satisfies

\[
N_{\mathbf Q(\sqrt{-R})/\mathbf Q}(\eta)
=
-A_1(2X+q+2)\Xi.
\]

On

\[
X=G=uq-1,\quad
R=q^2\rho,\quad
A_1=q\sigma,\quad
2X+q+2=q(2u+1),\quad
\Xi=q^2\Phi,
\]

and \(N=-\Phi\),

\[
N(\eta/q^2)=\sigma(2u+1)N.
\]

R9 supplies

\[
\boxed{
\xi=\frac{m+e\sqrt{-\rho}}{G^2},
\qquad
N(\xi)=\sigma(2u+1).
}
\]

Identifying \(\sqrt{-R}=q\sqrt{-\rho}\), let

\[
\boxed{
\theta=(\eta/q^2)/\xi=a+b\sqrt{-\rho}.
}
\]

Then

\[
\boxed{a^2+\rho b^2=N.}
\]

Thus the source-point witness is explicit before any integral Gaussian choice.

---

## 4. Fixed-norm conic → Gaussian conic

With \(S^2=N+\rho\),

\[
\boxed{
z_{\mathbf Q}=\frac{a+iSb}{1+ib}.
}
\]

Indeed

\[
|z_{\mathbf Q}|^2
=
\frac{a^2+S^2b^2}{1+b^2}
=
N.
\]

The real coordinates are

\[
x_G=\frac{a+Sb^2}{1+b^2},
\qquad
y_G=\frac{b(S-a)}{1+b^2}.
\]

The inverse is

\[
b=\frac{y_G}{S-x_G},
\qquad
a=\frac{Sx_G-N}{S-x_G}.
\]

The forward denominator has norm \(1+b^2>0\); the inverse denominator cannot
vanish on the actual \(\rho>0\) locus. Hence this is a birational actual-state map.

---

## 5. Integralization torsor and information loss

The point-level chain ends naturally in \(z_{\mathbf Q}\in\mathbf Q(i)\), not
automatically in \(\mathbf Z[i]\).

For each integralization choice

\[
z_{\mathbf Z}=\varepsilon z_{\mathbf Q},
\qquad \varepsilon\in\mathcal T_{\rm int}(z_{\mathbf Q}),
\]

R10 gives

\[
H_\varepsilon=
\begin{pmatrix}
D_+&z_{\mathbf Z}\\
\bar z_{\mathbf Z}&D_-
\end{pmatrix},
\qquad
\det H_\varepsilon=-2.
\]

Thus an original actual root produces

\[
\boxed{
\text{source point}
\to
\text{canonical rational }z_{\mathbf Q}
\to
\textbf{choice-dependent norm-one integralization}
\to
H_\varepsilon
\to
\text{canonical R11 word for the chosen }H_\varepsilon.
}
\]

The logical gap between a source point and a concrete R10 matrix is therefore exactly
identified.

---

## 6. Shared-\(d\) and radial coordinates

Set

\[
s:=\alpha/d.
\]

Then

\[
r=\frac{T}{\alpha}=\frac{t}{s},
\qquad
y=\frac{Y}{\alpha}=\frac{x}{s},
\]

so

\[
\boxed{
\alpha=ds,\qquad t=sr,\qquad x=sy.
}
\]

The common \(d\) in \(T=dt,Y=dx\) is completely consumed by projectivization:

```text
SHARED_D_PROJECTIVE_CONTENT=NONE
```

The information that survives source semantics is the radial integral lift \(s\),
not the tautological common factor \(d\).

---

## 7. Exact radial source reconstruction

Let

\[
c(q)=q^3+10q^2+12q+8,
\qquad
B_t=(q+2)(q^2-4q-4).
\]

The R2 source reconstruction scales linearly with \(s\):

\[
\mathcal N_{\rm tail}=s\,\widehat N(r),
\qquad
\widehat N(r)=\frac{B_tr+G}{qc(q)},
\]

\[
Z=s\,\widehat Z(r),
\qquad
\widehat Z(r)=\frac{Ar-2\widehat N(r)}{q(q+4)},
\]

\[
a_3=s\,\widehat a_3(r),
\qquad
\widehat a_3(r)
=
\frac{(G-1)r-q\widehat N(r)}{2(q+4)},
\]

\[
\mathcal X=s\,\widehat X(r),
\qquad
\widehat X(r)=\frac{\widehat Z(r)+u\widehat N(r)}2,
\]

\[
D_2=s\,\widehat D_2(r),
\qquad
\widehat D_2(r)=u\widehat a_3(r)+G\widehat X(r).
\]

Therefore the information-preserving object is

\[
\boxed{(r,y;s)}
\]

rather than the bare projective conic \((r,y)\).

---

## 8. Primitive-gate pullback

The source primitive gates become exactly

\[
\boxed{\gcd(sy,u)=1}
\]

and

\[
\boxed{\gcd(s\widehat Z(r),u)=1},
\]

with source integrality of \(sy\) and \(s\widehat Z(r)\).

Hence

```text
PRIMITIVE_GATE_FIRST_VISIBLE_LAYER=RADIAL_SOURCE_CONIC_LIFT
```

They are not invariants of the projective conic point alone.

The rational Gaussian coordinate can carry them only through its inverse map
**plus the retained \(s\)**. No source theorem yields a clean R10 condition such as

\[
(z_{\mathbf Z},u)=1.
\]

Therefore

```text
PRIMITIVE_GATE_GAUSSIAN_VISIBILITY=PARTIAL
```

at the rational source-attached level, and source visibility is lost after quotienting
by the integralization torsor.

---

## 9. LOW/UP pullback

LOW:

\[
x>\frac{AG}{10}
\]

becomes

\[
\boxed{
sy>\frac{AG}{10}.
}
\]

It is a radial lower bound.

UP:

\[
ALx<8uD_2
\]

becomes, because \(x=sy\) and \(D_2=s\widehat D_2(r)\),

\[
\boxed{
ALy<8u\widehat D_2(r).
}
\]

This is a genuine projective semi-algebraic half-plane condition, since
\(\widehat D_2(r)\) is affine in \(r\).

Together with positivity and the frozen real half-space

\[
s>0,\qquad y>0,\qquad r>1/c(q),
\]

the digit gate is one global fixed-complexity region. No old chamber/cell
decomposition is required.

Thus:

\[
\boxed{
\textbf{UP survives projectivization; LOW requires the radial scale.}
}
\]

---

## 10. Gaussian phase and first shell

For the canonical rational witness \(z_{\mathbf Q}=\Psi(r,y)\), the source region can
be transported birationally to a semi-algebraic arc/sector on the rational Gaussian
norm conic. So rational source-attached phase is meaningful.

But

\[
z_{\mathbf Q}\mapsto z_{\mathbf Z}=\varepsilon z_{\mathbf Q}
\]

changes phase with the norm-one integralization choice. Therefore the phase of an
arbitrary R10/R11 integral witness is not a source invariant.

Certificate interpretation:

```text
GAUSSIAN_PHASE_SOURCE_INVARIANT=PARTIAL
```

meaning:

- rational source-attached \(z_{\mathbf Q}\): TRUE;
- R10 integral \(z_{\mathbf Z}\): FALSE.

R11's norm-1 / norm-2 first-shell theorem applies only after a particular integral
\(H_\varepsilon\) has been chosen. R12 therefore cannot source-invariantly kill either
shell:

```text
FIRST_SHELL_REFINED_BY_SOURCE_GATE=NOT_VISIBLE
SECOND_GAUSSIAN_DIGIT_ANALYZED=FALSE
```

---

## 11. Dimension and category audit

Treat \((q,G,K,u)\) algebraically with \(uq=G+1\). The base has dimension \(3\).

The smooth projective source conic has dimension \(1\), so

\[
\boxed{\dim\mathscr V_{\rm src}^{\rm proj}=4.}
\]

Restoring \(s\) gives

\[
\boxed{\dim\mathscr V_{\rm src}^{\rm radial}=5.}
\]

The rational Gaussian norm-conic family has dimension \(4\). The source-projective
map is birational fibrewise, hence dominant, and forgets exactly one radial dimension:

\[
\boxed{\dim(\text{radial information kernel})=1.}
\]

That missing dimension is precisely where LOW and primitive integrality live.

By contrast,

\[
\Gamma\backslash GL_2(\mathbf Z[i])
\]

in R11 is a discrete arithmetic coset set, not an algebraic modular surface. Assigning
it a positive Zariski dimension would be a category error. R12 therefore does not
invent a “Hermitian image curve dimension”.

No source-attached modular curve/geodesic is proved.

---

## 12. Elimination verdict

The restored gates are of three types:

- primitive gcd: arithmetic/localization condition;
- LOW/UP: strict semi-algebraic inequalities;
- radial scale \(s\): an essential lifted variable.

They do not legitimately add a polynomial generator to the Zariski ideal after
forgetting \(s\).

Therefore no new relation

\[
F(p_c,q_c,r_c,s_c;G,K,q,u)=0
\]

is obtained beyond the frozen determinant/diagonal equations.

This is an exact negative result:

\[
\boxed{
\textbf{the independent gates shrink the arithmetic/real incidence, not its
Zariski closure after radial forgetting.}
}
\]

---

## 13. Continuant verdict

R11 gives

\[
\Phi(p_c,r_c)=u(2KG+B),
\qquad
\Phi(q_c,s_c)=u(2KG-B).
\]

R12 adds no source-attached continuant relation because the norm-one integralization
torsor intervenes before the canonical word is defined.

Hence

```text
PURE_CONTINUANT_LAYER_ADDS_NEW_INDEPENDENT_GATE=FALSE
CONTINUANT_SOURCE_IMAGE=FAIL_AS_SOURCE_ATTACHED
```

and pure continuant refinement is retired as the sole J2 frontier.

---

## 14. Power-of-ten incidence

The base section remains

\[
G=10^g,\qquad K=10^k,\qquad uq=G+1.
\]

No extra source gate survives as an invariant on the R11 integral quotient, so the
R11 continuant/power-ten intersection is not shrunk by R12.

Therefore

```text
POWER_TEN_TORIC_SECTION_INTERSECTION=OPEN
q_GT_1_CLOSED=FALSE
RATIONAL_LAYER_RETIRED=FALSE
```

---

## 15. Minimal surviving global object

The correct next object is

\[
\boxed{
\textbf{Primitive Radial Conic-Source Incidence}
\times
\textbf{One Global Digit Sector}
\times
\textbf{Power-of-Ten Base}.
}
\]

A minimal presentation is

\[
\mathscr I_{\rm rad}
=
\left\{
(q,G,K,u;r,y,s):
\begin{array}{l}
uq=G+1,\\
\mathcal C_{q,G,K}(r,y)=0,\\
s>0,\ r>1/c(q),\ y>0,\\
t=sr\in\mathbf Z,\ x=sy\in\mathbf Z,\\
Z=s\widehat Z(r)\in\mathbf Z,\\
\gcd(sy,u)=1,\\
\gcd(s\widehat Z(r),u)=1,\\
sy>AG/10,\\
ALy<8u\widehat D_2(r)
\end{array}
\right\}.
\]

The rational \(z_{\mathbf Q}\) may be retained as a birational auxiliary. The R10
integral \(z\) and R11 word should not be the frontier unless the integralization
torsor is retained.

---

## 16. General tools extracted

### Independent-Gate Reintegration Principle

If structural/full-equation data have been quotient-compressed while primitive and
Archimedean gates remain dependency-independent, closure must analyze the image of
those gates before refining internal moduli coordinates.

R12 is an explicit example: no amount of further continuant refinement can reconstruct
the forgotten radial scale.

### Radial Information-Loss Theorem

For the J2 chain

\[
\text{source conic}
\to
\text{Brauer class}
\to
\text{rational Gaussian norm}
\to
\text{integral Hermitian quotient},
\]

one radial source-lattice dimension is forgotten before the final integral Hermitian
choice. Primitive gcd and LOW depend essentially on that radial lift.

---

## 17. Fifteen direct answers

### Q1
R11's continuant word is a coordinate system for a chosen integral Hermitian witness.
It adds **no new independent arithmetic gate** beyond Gaussian split plus prescribed
diagonals.

### Q2
**Yes.** R7→R8→R9 upgrades to an explicit rational source-point → Gaussian witness:
\[
\theta=a+b\sqrt{-\rho}
\mapsto
z_{\mathbf Q}=(a+iSb)/(1+ib).
\]

### Q3
At rational level no twist is missing. The missing datum occurs only in passing to
R10's integral \(z\): a norm-one integralization choice
\[
\varepsilon\in\mathcal T_{\rm int}(z_{\mathbf Q}).
\]

### Q4
An original root gives canonical rational \(z_{\mathbf Q}\). A concrete R10 matrix
requires choosing \(\varepsilon\) with
\(z_{\mathbf Z}=\varepsilon z_{\mathbf Q}\in\mathbf Z[i]\), then
\[
H_\varepsilon=
\begin{pmatrix}
D_+&z_{\mathbf Z}\\
\bar z_{\mathbf Z}&D_-
\end{pmatrix}.
\]
The integral matrix is source-attached only after this choice.

### Q5
Shared \(d\) has **no projective content**.

### Q6
\(\gcd(x,u)=1\) first becomes visible on the radial source-conic lift:
\[
x=sy,\quad \gcd(sy,u)=1.
\]

### Q7
Likewise
\[
Z=s\widehat Z(r),\quad \gcd(s\widehat Z(r),u)=1.
\]

### Q8
LOW/UP become
\[
sy>AG/10,
\qquad
ALy<8u\widehat D_2(r).
\]
UP is projective; LOW is radial. Together with
\(s>0,y>0,r>1/c(q)\) they form one fixed-complexity region.

### Q9
The rational source-attached Gaussian phase is controlled in principle by the
pulled-back source sector. The phase of an arbitrary R10 integral witness is **not**
source invariant because of norm-one integralization.

### Q10
No source-invariant refinement of the two first shells is obtained. The verdict is
**NOT_VISIBLE**, not an occurrence theorem asserting BOTH.

### Q11
\[
\dim\mathscr V_{\rm src}^{\rm radial}=5,\quad
\dim\mathscr V_{\rm src}^{\rm proj}=4,\quad
\dim\mathscr M_{\rm Gauss}^{\rm rat}=4.
\]
The projective source image is dominant/birational fibrewise and one radial dimension
is forgotten. R11's integral coset quotient is discrete.

### Q12
No source-attached modular curve/geodesic/toric subvariety is proved. Fibrewise the
source image is the full rational norm conic before radial reintegration.

### Q13
No new **polynomial** Zariski relation is generated by primitive+digit gates. They add
arithmetic-open/radial and semi-algebraic constraints instead.

### Q14
The source image × power-of-ten section remains **OPEN**; emptiness is not proved.

### Q15
The minimal global object after R12 is
\[
\boxed{
\textbf{primitive radial conic-source incidence}
\times
\textbf{digit sector}
\times
\textbf{power-of-ten base}.
}
\]

---

## 18. Terminal status

\[
\boxed{\mathbf{J2\ OPEN}}.
\]

But the frontier has changed decisively:

\[
\boxed{
\textbf{arbitrary Hermitian reduction word is no longer the frontier.}
}
\]

The highest information-preserving global object is

\[
\boxed{
\textbf{Primitive Radial Conic Incidence}
\times
\textbf{Global Digit Sector}.
}
\]
