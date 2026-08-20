# Fourth 85 · R6 — Gaussian Split-Fibre Source Embedding × Explicit Conic Isomorphism × Source-Lattice Pullback × Gaussian Primitive Collision × Repair-or-Kill

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — \(J=2\)  
**Round:** 第四个八五计划 · R6  
**Inherited target:** \(q=1\) negative, \(K=100,1000\), especially Brauer-split fibres  
**Completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 1. Executive Verdict

R6 does **not** prove

\[
K=100\Longrightarrow\varnothing,
\qquad
K=1000\Longrightarrow\varnothing,
\]
nor
\[
q=1\Longrightarrow\varnothing,
\qquad
J=2\Longrightarrow\varnothing.
\]

However R6 obtains two genuinely new results.

## 1.1 Positive source-side closure

For every actual \(G=10^g\), \(K\in\{100,1000\}\),

\[
A_2(G,K)\equiv2\pmod3.
\]

If \(3\mid\tau\), then \(B_1\equiv C_0\equiv0\pmod3\), while
\(\gcd(\rho,\tau)=1\) and
\(a=\tau G/10+\rho\) imply \(3\nmid a\). Hence

\[
Y_0^2
=
A_2a^2+B_1a+C_0
\equiv
2a^2
\equiv2
\pmod3,
\]

impossible.

Therefore, for **both** \(K=100\) and \(K=1000\),

\[
\boxed{
(d,\tau)\in\{(1,3),(1,9),(3,3)\}
\Longrightarrow\varnothing.
}
\]

Formal verdict:

```text
TAU_DIVISIBLE_BY_3_SOURCE_FAMILIES_CLOSED = YES
NEW_HISTORICAL_CASES_CLOSED = 6
```

This is not the R5 Brauer obstruction. It is a source-integral/primitive obstruction that is destroyed by the R4 normalization.

## 1.2 Gaussian source-lattice architecture is killed in its intended form

R6 recovers an exact source lattice before Gaussianization and computes

\[
\operatorname{SNF}=\operatorname{diag}(1,A_2).
\]

But:

1. the associated congruence is algebraically saturated by the completion-square identity;
2. the natural explicit Gaussianization supplied by \(A+S^2=TQ\) is defined over
   \(\mathbf Q(G,\sqrt Q)\), not \(\mathbf Q(G)\);
3. more decisively, the standard affine source conic
   \[
   x^2-A_2v^2=T_4
   \]
   and the standard affine Gaussian circle
   \[
   u^2+w^2=T_4
   \]
   are **not affine-isomorphic over \(\mathbf Q(G)\)**;
4. therefore any \(\mathbf Q(G)\)-projective descent must use a source-dependent affine denominator and cannot transport the source affine lattice to a fixed affine lattice/coset in the standard Gaussian circle;
5. passing from a canonical rational Gaussian witness to an integral Gaussian representation introduces a noncanonical norm-one integralization torsor, so Gaussian prime orientation and integral phase are not source invariants.

Thus:

```text
EXPLICIT_GAUSSIANIZATION_OVER_Q(G,sqrt(Q)) = YES
SOURCE_USEFUL_AFFINE_GAUSSIANIZATION_OVER_Q(G) = NO
SOURCE_AFFINE_GAUSSIANIZATION_IMPOSSIBLE = YES
GAUSSIAN_SOURCE_DIMENSION_DROP = NO
SOURCE_CONGRUENCE_EXACTIZED = NO
FINITE_GAUSSIAN_ORIENTATIONS_SOURCE_CANONICAL = NO
GAUSSIAN_SPLIT_SOURCE_ARCHITECTURE = DEAD
```

The qualifier on the death verdict is important: what is killed is the proposed route

\[
\text{source affine lattice}
\to
\text{fixed affine Gaussian lattice}
\to
\text{SNF/circle/prime-orientation collision}.
\]

The abstract projective Brauer equivalence remains mathematically valid.

---

# 2. R1–R5 Frozen Conclusions

R6 freezes the following.

### R1
Valuation-signature finite branching exists, but no global fixed object/dimension drop.

### R2
\[
\texttt{FACTOR_GAP_ARCHITECTURE=DEAD}.
\]

### R3
\[
\texttt{SUPPORT_COLLISION_ARCHITECTURE=DEAD},
\]
\[
\texttt{FIXED_TAU_PELL_AS_FIXED_OBJECT_ARCHITECTURE=DEAD}.
\]

### R4
The 12 q=1 coefficient templates collapse to three fixed function-field torsors

\[
x^2-A_2(G,K)v^2=T_4(G,K),
\]

and

\[
K=10,\ q=1,\text{ negative}\Longrightarrow\varnothing.
\]

### R5
\[
(A_2,T_4)=(-1,T_4)
\]
in \(\operatorname{Br}(\mathbf Q(G))[2]\), so specialized local obstruction is exactly Gaussian two-square obstruction. Genuine split fibres exist; pure Brauer/local coverage cannot close all \(g\).

The already archived file `Fourth_85_R1_R5_First_Checkpoint.md` exists and was therefore not duplicated in R6.

---

# 3. Permanent Closure of \(K=10\)

R6 does not reopen \(K=10\). The R4 certificate remains permanent:

\[
K=10,\ q=1,\text{ negative}\Longrightarrow\varnothing.
\]

---

# 4. Why Pure Local/Brauer Cover Is Dead

R5 produced exact split fibres for \(K=100,1000\), including \(g=5\). Hence the normalized conic can be locally soluble everywhere while the source shell remains empty.

R6 therefore distinguishes two notions:

- **normalized-conic locality**, already completely classified by R5;
- **source-integral locality**, which may still use primitive conditions removed by normalization.

The new \(\tau\)-prime gate belongs to the second category and does not resurrect blind Hilbert-symbol scanning.

---

# 5. Current Source-Embedding Gap

The exact problem is:

\[
\text{source integer point}
\Longrightarrow
\text{normalized rational norm point},
\]

but the reverse implication fails.

R6 asks whether this failure can be encoded as a fixed Gaussian affine lattice. The answer is negative.

---

# 6. Exact Source Norm Equation

The R4 source conic is

\[
Y_0^2=A_2a^2+B_1a+C_0,
\]

with

\[
\begin{aligned}
A_2={}&
100(K^2-1)G^6+(280K^2-380)G^5\\
&+(236K^2-545)G^4+(16K^2-362)G^3\\
&-(52K^2+93)G^2-8K^2G+4K^2,
\end{aligned}
\]

\[
B_1=-\tau G^2P(G,K),
\]

\[
\begin{aligned}
P(G,K)={}&
20(K^2-1)G^5+(48K^2-68)G^4\\
&+(32K^2-85)G^3-46G^2-4K^2G-4G+3,
\end{aligned}
\]

and

\[
C_0=\frac{\tau^2G^5}{4}Q_K(G).
\]

The source quotient is

\[
\rho=r_{K,\tau}+2Kn,
\qquad
a=\frac{\tau G}{10}+\rho,
\]

with

\[
31\rho+\tau\equiv0\pmod{2K},
\qquad
\gcd(\rho,10\tau)=1,
\]

and

\[
0<\rho<\frac{10-d\tau}{10d}G.
\]

Define

\[
D:=\tau G^2(G+1)(2G+3).
\]

R6 simplifies the R4 completed-square coordinates exactly to

\[
\boxed{
x=\frac{2A_2a+B_1}{D},
\qquad
v=\frac{2Y_0}{D}.
}
\]

Thus the exact homogeneous equation is

\[
\boxed{
X^2-A_2V^2=D^2T_4,
}
\]

with

\[
X:=2A_2a+B_1,\qquad V:=2Y_0.
\]

This is the exact source equation used in R6.

---

# 7. Primitive Norm Normalization

R1 gives

\[
Y_0=2Ky,\qquad \gcd(y,10)=1.
\]

For the live \(K=100,1000\) shell, \(4K\mid X\) and \(4K\mid D\). Define

\[
\boxed{
C:=\frac{X}{4K},
\qquad
Y:=y,
\qquad
Z:=\frac{D}{4K}.
}
\]

Then

\[
\boxed{
C^2-A_2Y^2=T_4Z^2.
}
\tag{R6-SN}
\]

This is an integral source-preserving norm model.

Let

\[
a_0:=\frac{\tau G}{10}+r_{K,\tau}.
\]

Since \(a=a_0+2Kn\),

\[
\boxed{
C=c_{K,\tau,g}+A_2n,
}
\]

where

\[
\boxed{
c_{K,\tau,g}
=
\frac{2A_2a_0+B_1}{4K}.
}
\]

Thus the source arithmetic before Gaussianization is completely explicit.

---

# 8. Source Conditions in Norm Coordinates

The source data become:

\[
C\equiv c_{K,\tau,g}\pmod{A_2},
\]

\[
Y\in\mathbf Z,\qquad \gcd(Y,10)=1,
\]

\[
Z=\frac{\tau G^2(G+1)(2G+3)}{4K}
\quad\text{fixed for }(K,\tau,g),
\]

\[
\rho=r_{K,\tau}+2Kn,
\]

\[
0<\rho<\frac{10-d\tau}{10d}G,
\]

\[
\gcd(\rho,10\tau)=1.
\]

The coordinate \(d\) does not enter \(A_2,T_4,c,Z\). It changes only the upper source window.

---

# 9. Gaussian Source-Lattice Construction Before Gaussianization

Ignoring the conic equation for one moment, possible \((C,Y)\) lie in

\[
\boxed{
(c_{K,\tau,g},0)
+
\begin{pmatrix}
A_2&0\\
0&1
\end{pmatrix}
\mathbf Z^2.
}
\]

Hence

\[
\Lambda_{K,\tau,g}
=
\langle(A_2,0),(0,1)\rangle.
\]

This is an exact affine lattice, not a heuristic.

---

# 10. Smith Normal Form

The basis matrix is

\[
M=
\begin{pmatrix}
A_2&0\\
0&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\operatorname{SNF}(M)=\operatorname{diag}(1,A_2).
}
\]

Thus

\[
\boxed{
[\mathbf Z^2:\Lambda]=A_2.
}
\]

Since

\[
A_2
=
100(K^2-1)G^6+O_K(G^5),
\]

the index is of order \(G^6\).

This initially looks much larger than the \(G^2\) affine Gaussian-circle radius, but that comparison is **not legal** after provenance-preserving Gaussianization; Section 14 explains why.

---

# 11. Source-Lattice Congruence Is Saturated

The large SNF does not create a new conic congruence.

Indeed, at \(n=0\),

\[
c=\frac{2A_2a_0+B_1}{4K},
\qquad
Z=\frac{D}{4K},
\]

and the completion-square identity gives

\[
\boxed{
c^2-T_4Z^2
=
A_2
\frac{A_2a_0^2+B_1a_0+C_0}{4K^2}.
}
\]

Hence

\[
c^2\equiv T_4Z^2\pmod{A_2}
\]

is automatic.

Since \(C\equiv c\pmod{A_2}\),

\[
C^2\equiv T_4Z^2\pmod{A_2}
\]

is not an independent gate. It is already encoded by the source completion-square construction.

Formal verdict:

```text
SOURCE_LATTICE_SNF = (1,A2)
SOURCE_LATTICE_CONGRUENCE_NEW_GATE = NO
SOURCE_LATTICE_CONGRUENCE_SATURATED_BY_COMPLETION_IDENTITY = YES
```

---

# 12. Source-Prime Primitive Gate — New R6 Closure

Let \(p\mid\tau\), \(p\nmid10K\). Since

\[
\gcd(\rho,\tau)=1
\]

and

\[
a=\frac{\tau G}{10}+\rho,
\]

we have

\[
a\equiv\rho\not\equiv0\pmod p.
\]

Also

\[
B_1\equiv0\pmod p,
\qquad
C_0\equiv0\pmod p.
\]

Therefore every source point must satisfy

\[
Y_0^2\equiv A_2a^2\pmod p.
\]

Thus a necessary condition is

\[
\boxed{
A_2(G,K)\text{ is a quadratic residue or }0\pmod p.
}
\tag{TAU-PRIME}
\]

This is a direct same-point source invariant.

## \(p=3\)

For all powers of ten \(G,K\),

\[
G\equiv K\equiv1\pmod3,
\]

and exact reduction gives

\[
A_2\equiv2\pmod3.
\]

Hence if \(3\mid\tau\),

\[
Y_0^2\equiv2a^2\equiv2\pmod3,
\]

impossible.

Therefore, for each of \(K=100,1000\),

\[
\boxed{
(1,3),(1,9),(3,3)
\text{ are closed for every live }g.
}
\]

## \(p=7,\tau=7\)

The same source gate gives a genuine exponent filter.

For \(K=100\), according to \(g\bmod6\),

\[
A_2\bmod7=(4,2,4,5,0,5),
\]

so

\[
\boxed{
g\equiv0,4\pmod6
\Longrightarrow
\tau=7\text{ source impossible}.
}
\]

For \(K=1000\),

\[
A_2\bmod7=(1,4,4,0,2,6),
\]

so

\[
\boxed{
g\equiv0\pmod6
\Longrightarrow
\tau=7\text{ source impossible}.
}
\]

This is only a filter, not \(\tau=7\) closure.

---

# 13. Current q=1 Negative Frontier Compression

Before R6, \(K=100,1000\) contributed 16 historical \((d,\tau)\) cases.

R6 closes six:

\[
3\text{ per }K.
\]

The remaining five historical cases per \(K\) are

\[
(1,1),(3,1),(7,1),(9,1),(1,7).
\]

But \(d\) changes only the upper \(\rho\)-window. For \(\tau=1\),

\[
d=3,7,9
\]

are strict subwindows of \(d=1\).

Therefore, for each \(K\), it suffices to study only two maximal source templates:

\[
\boxed{
(K,\tau,d)=(K,1,1)
}
\]

and

\[
\boxed{
(K,\tau,d)=(K,7,1).
}
\]

So the 16-case frontier compresses to four maximal templates:

\[
\boxed{
(K,\tau)\in
\{(100,1),(100,7),(1000,1),(1000,7)\}.
}
\]

This is a real source-side reduction.

---

# 14. Brauer-to-Gaussian Identity Recovery

R5 gives

\[
A+S^2=TQ,
\]

where

\[
A=A_2,\qquad T=T_4,
\]

\[
S=
1-(4K^2-3)G-(8K^2-10)G^2-(4K^2-4)G^3,
\]

\[
Q=
(4K^2+21)G^2+(8K^2+12)G+(4K^2+1).
\]

R6 does not reprove the Brauer identity. It uses this equation to construct an explicit point-level map over the quadratic extension generated by \(\sqrt Q\).

---

# 15. Explicit Conic Isomorphism Over \(\mathbf Q(G,\sqrt Q)\)

Consider the projective source conic

\[
C_A:\quad
X^2-AV^2=TZ^2
\]

and the Gaussian projective conic

\[
C_i:\quad
U^2+W^2=TZ_G^2.
\]

Over

\[
E=\mathbf Q(G,\sqrt Q)
\]

define

\[
\boxed{
U=SX+\sqrt Q\,TZ,
}
\]

\[
\boxed{
W=-AV,
}
\]

\[
\boxed{
Z_G=\sqrt Q\,X+SZ.
}
\]

Direct expansion gives

\[
\boxed{
U^2+W^2-TZ_G^2
=
-A(X^2-AV^2-TZ^2).
}
\]

The transformation matrix is

\[
M=
\begin{pmatrix}
S&0&\sqrt Q\,T\\
0&-A&0\\
\sqrt Q&0&S
\end{pmatrix},
\]

and

\[
\boxed{\det M=A^2}.
\]

Hence away from \(A=0\) it is a projective isomorphism.

---

# 16. Inverse Map and Exceptional Locus

An inverse, up to a projective scalar, is

\[
\boxed{
X=SU-\sqrt Q\,TZ_G,
}
\]

\[
\boxed{
V=W,
}
\]

\[
\boxed{
Z=SZ_G-\sqrt Q\,U.
}
\]

Indeed the inverse matrix times \(M\) is \(-A I_3\).

On the affine chart \(Z=1\),

\[
\boxed{
u=
\frac{Sx+\sqrt Q\,T}
{S+\sqrt Q\,x},
}
\]

\[
\boxed{
w=
\frac{-Av}
{S+\sqrt Q\,x}.
}
\]

Conversely,

\[
\boxed{
x=
\frac{Su-\sqrt Q\,T}
{S-\sqrt Q\,u},
}
\]

\[
\boxed{
v=
\frac{w}
{S-\sqrt Q\,u}.
}
\]

The affine denominator is source-point dependent.

There is no projective exceptional locus when \(A\ne0\); the apparent poles are changes of affine chart.

---

# 17. Why This Map Does Not Descend as a Source-Useful Affine Map

The quadratic polynomial \(Q\) has

\[
\boxed{
\operatorname{disc}_G(Q)
=
-20(8K^2-3)\ne0.
}
\]

Thus \(Q\) is not a square in \(\mathbf Q(G)\), so the explicit map above is genuinely defined over a moving quadratic extension.

Brauer equality guarantees an abstract projective equivalence over \(\mathbf Q(G)\), but R6 proves that no such descent can preserve the standard affine charts.

---

# 18. Affine-Infinity Obstruction

Let

\[
F=\mathbf Q(G).
\]

The standard affine source conic

\[
x^2-Av^2=T
\]

has projective completion

\[
X^2-AV^2=TZ^2.
\]

Its boundary at infinity is

\[
D_A:\quad Z=0,\quad X^2-AV^2=0,
\]

whose quadratic étale algebra is

\[
F(\sqrt A).
\]

The standard affine Gaussian circle

\[
u^2+w^2=T
\]

has boundary

\[
D_i:\quad Z=0,\quad U^2+W^2=0,
\]

whose quadratic algebra is

\[
F(i).
\]

Any regular affine isomorphism extends to the smooth projective completions and must identify the boundary divisors. Therefore a necessary condition is

\[
F(\sqrt A)\simeq F(i),
\]

equivalently

\[
-A\in F^{\times2}.
\]

But \(A=A_2(G,K)\) is a nonconstant squarefree sextic. Hence

\[
-A\notin F^{\times2}.
\]

Therefore

\[
\boxed{
C_A^{\rm aff}
\not\simeq_F
C_i^{\rm aff}.
}
\]

This is the decisive R6 obstruction.

It implies that no \(\mathbf Q(G)\)-projective Gaussianization can send the source affine lattice to a fixed lattice in the standard affine circle without a moving source-dependent denominator.

---

# 19. Denominator / Integrality Audit

The intended architecture required

\[
\text{source lattice}
\longrightarrow
\Lambda+\mathbf c\subseteq\mathbf Z^2
\]

inside

\[
u^2+w^2=T.
\]

R6 proves this target is not invariantly available.

A projective source point

\[
[C:Y:Z]
\]

is mapped to a homogeneous Gaussian point

\[
[U:W:Z_G]
\]

with

\[
U^2+W^2=TZ_G^2.
\]

Because the affine boundary cannot be preserved,

\[
Z_G
\]

must vary nontrivially with the source point for any base-field descent.

Normalizing to \(Z_G=1\) divides by a moving linear form. Therefore source integrality becomes rational denominator arithmetic, not a fixed affine lattice.

Formal verdict:

```text
GAUSSIAN_AFFINE_DENOMINATOR_CONSTANT = NO
GAUSSIAN_AFFINE_SOURCE_LATTICE_INTRINSIC = NO
```

---

# 20. Circle Scale vs Lattice Scale — Why the Naive Comparison Fails

The affine Gaussian equation has

\[
T_4(G,K)=4(K^2-1)G^4+O_K(G^3),
\]

so an **integral affine** Gaussian representation has radius \(O_K(G^2)\).

The pre-Gaussian source lattice has index \(A_2=O_K(G^6)\).

But this does not yield a contradiction because provenance-preserving Gaussianization does not land in \(Z_G=1\). The homogeneous image satisfies

\[
U^2+W^2=T_4Z_G^2
\]

with \(Z_G\) moving.

Thus the relevant radius is

\[
\sqrt{T_4}\,|Z_G|,
\]

not \(\sqrt{T_4}\).

The proposed \(G^6\)-index versus \(G^2\)-radius collision is therefore a chart error unless one first proves a uniform denominator bound. R6 proves no such bound can come from an affine isomorphism.

---

# 21. Coset–Circle Incidence

Before Gaussianization, the exact incidence is

\[
C=c+A_2n,
\]

\[
C^2-A_2Y^2=T_4Z^2.
\]

After honest projective Gaussianization, one obtains a homogeneous Gaussian cone intersected with an oblique source plane/coset. One does **not** obtain a fixed affine circle intersected with a fixed \(\mathbf Z^2\)-coset.

Therefore Task G does not reduce to a new binary quadratic form with a fixed affine Gaussian lattice.

Verdict:

```text
GAUSSIAN_COSET_CIRCLE_BINARY_FORM_EXTRACTED = NO
REASON = moving affine denominator / projective-boundary mismatch
```

---

# 22. Gaussian Integer Reformulation

For a split fibre, an integral Gaussian representation

\[
z_{\mathbf Z}=u+iw,\qquad N(z_{\mathbf Z})=T
\]

exists.

But R6 distinguishes:

- a source-attached rational Gaussian point, obtained after choosing a rational projective Gaussianization;
- an arbitrary integral Gaussian representation of \(T\).

These are not canonically the same point.

---

# 23. Canonical Gaussian Norm Representative and Norm-One Torus

Fix one integral representation

\[
\Theta=P+iQ_0,\qquad P^2+Q_0^2=T.
\]

Every rational Gaussian point \(z\) of norm \(T\) has

\[
z=\Theta\omega,
\qquad
N(\omega)=1.
\]

Write

\[
\omega=
\frac{s+ir}{s-ir}
=
\frac{s^2-r^2+2irs}{s^2+r^2}.
\]

Then

\[
\boxed{
u=
\frac{P(s^2-r^2)-2Q_0rs}
{s^2+r^2},
}
\]

\[
\boxed{
w=
\frac{Q_0(s^2-r^2)+2Prs}
{s^2+r^2}.
}
\]

The denominator \(r^2+s^2\) is free to contain primes not dividing \(T\).

This is the exact reason that prime orientation of an **integral** Gaussian representative is not a source invariant of a rational Gaussian point.

---

# 24. Gaussian gcd / Primitive Audit

For an integral representation \(z_{\mathbf Z}\), the usual Gaussian gcd and prime-allocation theory is valid.

But if \(z_{\rm src}\in\mathbf Q(i)\) is the source-attached rational Gaussian point and
\(z_{\mathbf Z}\in\mathbf Z[i]\) is any integral representation, then

\[
\varepsilon
=
\frac{z_{\mathbf Z}}{z_{\rm src}}
\]

has norm one.

Conversely every norm-one \(\varepsilon\) that makes \(\varepsilon z_{\rm src}\) integral is a possible integralization.

Thus

\[
\boxed{
\mathcal T_{\rm int}(z_{\rm src})
=
\{
\varepsilon\in\mathbf Q(i)^1:
\varepsilon z_{\rm src}\in\mathbf Z[i]
\}
}
\]

is the missing datum.

This reproduces, in the q=1 setting, the same type of information-loss mechanism previously isolated in the q>1 J2 Gaussian/Hermitian campaign, but here it is derived from the current R4/R5 source object.

---

# 25. Gaussian Prime Orientation

For an arbitrarily chosen integral \(z_{\mathbf Z}\), split primes of \(T\) have finite orientation choices.

However the source point does not canonically choose that \(z_{\mathbf Z}\).

Multiplication by a rational norm-one element can modify Gaussian numerator/denominator orientation before integralization.

Therefore:

```text
FINITE_GAUSSIAN_ORIENTATIONS = TRUE_FOR_A_FIXED_INTEGRAL_REPRESENTATION_PROBLEM
FINITE_GAUSSIAN_ORIENTATIONS_SOURCE_CANONICAL = NO
```

The second line is the one relevant to R6.

---

# 26. Source Residue as Gaussian Congruence

No intrinsic congruence

\[
u+iw\equiv c\pmod{\mathfrak m}
\]

is obtained on the standard integral Gaussian circle.

Any such congruence depends on:

1. a choice of projective Gaussianization;
2. a choice of affine target chart;
3. a choice of norm-one integralization.

Therefore it is not a canonical image of the source DCDC residue.

---

# 27. Source Window / Gaussian Arc

The source window

\[
0<\rho<\frac{10-d\tau}{10d}G
\]

is genuine and remains active.

Under a fixed rational Gaussianization it can be transported to a rational arc/sector.

But the arc is not invariant under target norm-one automorphisms, and integralization changes the phase again.

Therefore:

```text
RATIONAL_GAUSSIAN_ARC_MAP_DEPENDENT = YES
INTEGRAL_GAUSSIAN_ARC_SOURCE_CANONICAL = NO
```

No uniform narrow-arc exclusion is extracted.

---

# 28. Replay: \((K,g)=(100,5)\)

Exact value:

\[
T_{100}(10^5)
=
3999679988399869999400001
\]

and

\[
T
=
3^2\cdot444408887599985555488889,
\]

where the second factor is prime and \(1\bmod4\).

Cornacchia gives

\[
444408887599985555488889
=
666582072292^2+8787974675^2.
\]

Hence

\[
\boxed{
T
=
1999746216876^2
+
26363924025^2.
}
\]

The total signed/order representation count is

\[
\boxed{r_2(T)=8}.
\]

Every integral representation has rational gcd divisible by \(3\).

Exact source replay gives:

| \((d,\tau)\) | legal \(n\) | square hits |
|---|---:|---:|
| (1,1) | 450 | 0 |
| (1,3) | 233 | 0 |
| (3,1) | 117 | 0 |
| (1,7) | 129 | 0 |
| (7,1) | 21 | 0 |
| (1,9) | 34 | 0 |
| (3,3) | 11 | 0 |
| (9,1) | 5 | 0 |

Thus the R5 finite exclusion is independently reproduced.

But R6 does **not** claim that the eight integral Gaussian points are the direct source images. That identification is exactly what the affine/integrality audit disproves.

---

# 29. Replay: \((K,g)=(1000,5)\)

Exact value:

\[
T_{1000}(10^5)
=
400007600027999869999400001
\]

and

\[
T
=
3^2\cdot44445288891999985555488889,
\]

with the second factor prime and \(1\bmod4\).

Cornacchia gives

\[
44445288891999985555488889
=
5147610916308^2+4236436090195^2.
\]

Hence

\[
\boxed{
T
=
15442832748924^2
+
12709308270585^2.
}
\]

Again

\[
\boxed{r_2(T)=8}.
\]

Exact source replay gives:

| \((d,\tau)\) | legal \(n\) | square hits |
|---|---:|---:|
| (1,1) | 45 | 0 |
| (1,3) | 23 | 0 |
| (3,1) | 12 | 0 |
| (1,7) | 12 | 0 |
| (7,1) | 3 | 0 |
| (1,9) | 3 | 0 |
| (3,3) | 1 | 0 |
| (9,1) | 1 | 0 |

Again all source cases are empty at \(g=5\).

---

# 30. Uniform Invariant Extraction from the Split-Fibre Laboratory

The \(g=5\) laboratory yields one uniform invariant and one negative conclusion.

## Positive uniform invariant

The \(\tau\)-prime source gate explains all \(\tau=3,9\) failures uniformly for all \(g\), not only \(g=5\).

## Negative conclusion

The remaining \(\tau=1,7\) failures at \(g=5\) are **not** explained by a common integral Gaussian representation class, because the source-to-integral-Gaussian identification is noncanonical.

A finite scan of small source moduli also does not reveal one common killer across the remaining maximal templates.

Therefore:

```text
G5_ALL_8_FAILURES_UNIFIED_BY_ONE_GAUSSIAN_CONGRUENCE = NO
G5_TAU_3_9_FAILURES_UNIFORMLY_EXPLAINED = YES
G5_TAU_1_7_UNIFORM_SOURCE_INVARIANT = NOT_EXTRACTED
```

---

# 31. Representation Census and Counting Route

For both \(g=5\) split fibres,

\[
r_2(T)=8.
\]

This is extremely small.

Nevertheless the counting route does not close the source problem, because the source point naturally lives on a rational projective Gaussian fibre before integralization. The finite set of integral representations is reached only after a noncanonical norm-one choice.

Therefore

\[
r_2(T)\ll d(T)
\]

does not by itself bound the number of provenance-preserving rational source images.

Verdict:

```text
REPRESENTATION_COUNT_SMALL = YES_AT_G5
COUNTING_TO_SOURCE_BRIDGE = NO
```

---

# 32. Pseudo-Family Guillotine

The rational Gaussian norm fibre itself contains the full norm-one parameter family

\[
\Theta\frac{s+ir}{s-ir}.
\]

Hence the Gaussian target is intrinsically flexible before source arithmetic is reimposed.

R6 did not construct an infinite **genuine source-valid** pseudo-family. Therefore no claim of source abundance is made.

But the rational torus family is enough to falsify the idea that Gaussian splitness plus a noncanonical affine chart will automatically discretize source points into the finite integral representation set.

```text
RATIONAL_GAUSSIAN_PSEUDOFAMILY = YES
GENUINE_SOURCE_PSEUDOFAMILY = NOT_FOUND
```

---

# 33. Counterexample Guillotine

### Conjecture A
“Brauer equivalence has a source-useful integral affine conic map.”

\[
\boxed{\textbf{FALSE}.}
\]

The affine-infinity obstruction proves impossibility over \(\mathbf Q(G)\).

### Conjecture B
“Large Gaussian source-lattice index automatically kills circle points.”

\[
\boxed{\textbf{FALSE AS AN AVAILABLE ARGUMENT}.}
\]

The fixed affine Gaussian lattice does not exist provenance-preservingly.

### Conjecture C
“The \(g=5\) 8/8 failure has one uniform congruence invariant.”

\[
\boxed{\textbf{PARTIALLY FALSE}.}
\]

The \(\tau=3,9\) part has one source \(p=3\) invariant; the remaining \(\tau=1,7\) failures do not share a recovered invariant.

### Conjecture D
“Source residue fixes Gaussian prime orientation.”

\[
\boxed{\textbf{FALSE / NOT SOURCE-CANONICAL}.}
\]

### Conjecture E
“Source window gives a canonical narrow Gaussian arc.”

\[
\boxed{\textbf{FALSE AT THE INTEGRAL GAUSSIAN LEVEL}.}
\]

### Conjecture F
“Few Gaussian representations imply source extinction.”

\[
\boxed{\textbf{NO RIGOROUS BRIDGE}.}
\]

---

# 34. Novelty Audit

R6 does **not** count the following as breakthroughs:

- Brauer identity;
- two-square criterion;
- generic Gaussian factorization;
- another local-prime atlas;
- R3 support allocation;
- R2 factor-gap.

The genuine new information is:

1. exact simplified source normalization
   \[
   x=(2Aa+B_1)/D,\quad v=2Y_0/D;
   \]
2. primitive integral norm model
   \[
   C^2-AY^2=TZ^2;
   \]
3. exact source lattice and SNF
   \[
   \operatorname{SNF}(1,A);
   \]
4. proof that the SNF congruence is completion-square saturated;
5. source-\(\tau\)-prime primitive gate and six historical closures;
6. explicit Gaussianization over \(\mathbf Q(G,\sqrt Q)\);
7. affine-infinity impossibility theorem over \(\mathbf Q(G)\);
8. integralization-torsor audit showing Gaussian prime orientation is not source-canonical;
9. independent exact \(g=5\) representation/source replay certificates.

---

# 35. Information Gain

| Result | Class |
|---|---|
| exact source normalization | `STRUCTURAL` |
| primitive integral norm coordinates | `SOURCE_LATTICE` |
| SNF \((1,A_2)\) | `SOURCE_LATTICE` |
| SNF congruence saturation | `STRUCTURAL` |
| \(\tau=3,9\) closure | `FAMILY_CLOSURE` |
| \(p=7,\tau=7\) residue classes | `FILTER` |
| extension Gaussianization | `EXPLICIT_MAP` |
| affine-infinity obstruction | `STRUCTURAL` |
| norm-one integralization torsor | `STRUCTURAL` |
| g=5 census | `FILTER` |
| g=5 replay | `FILTER` |
| K=100 closure | **NO** |
| K=1000 closure | **NO** |
| q=1 closure | **NO** |

---

# 36. \(K=100\) Verdict

\[
\boxed{\texttt{K100_Q1_NEGATIVE_CLOSED=NO}.}
\]

New permanent reductions:

\[
\tau=3,9\Longrightarrow\varnothing.
\]

For \(\tau=7\),

\[
g\equiv0,4\pmod6
\Longrightarrow\varnothing.
\]

The remaining maximal templates are

\[
(K,\tau,d)=(100,1,1)
\]

and

\[
(100,7,1)
\]

on their surviving exponent classes.

---

# 37. \(K=1000\) Verdict

\[
\boxed{\texttt{K1000_Q1_NEGATIVE_CLOSED=NO}.}
\]

Again

\[
\tau=3,9\Longrightarrow\varnothing.
\]

For \(\tau=7\),

\[
g\equiv0\pmod6
\Longrightarrow\varnothing.
\]

The remaining maximal templates are

\[
(1000,1,1),
\qquad
(1000,7,1).
\]

---

# 38. q=1 Coverage Audit

Because neither \(K=100\) nor \(K=1000\) is closed, a final q=1 coverage certificate is **not authorized**.

Current negative-shell status:

- \(K=10\): closed;
- \(K=100\): open on two maximal source templates after R6 compression;
- \(K=1000\): open on two maximal source templates after R6 compression.

Therefore:

```text
Q1_BRANCH_CLOSED = NO
```

No `Fourth_85_q1_Final_Closure_Certificate.md` is generated.

---

# 39. Four Required Questions

## Q1. Is the Brauer-split conic → Gaussian circle map explicitly usable?

**Only over the quadratic extension**
\[
\mathbf Q(G,\sqrt Q).
\]

A source-useful affine map over \(\mathbf Q(G)\) is impossible because the two affine infinity divisors are non-isomorphic.

\[
\boxed{\textbf{Answer: explicit projectively over an extension; not source-useful affinely over the base.}}
\]

## Q2. Does the source lattice acquire new codimension after the map?

Before Gaussianization it has exact SNF \((1,A_2)\), but its obvious congruence is saturated. After provenance-preserving Gaussianization there is no intrinsic fixed affine Gaussian lattice.

\[
\boxed{\textbf{Answer: no new Gaussian codimension.}}
\]

## Q3. Are the known split-fibre source failures uniformly explained?

Only partially.

- \(\tau=3,9\): yes, by the new source \(p=3\) gate.
- \(\tau=1,7\): no common invariant extracted.

\[
\boxed{\textbf{Answer: partial, not complete.}}
\]

## Q4. Can this mechanism uniformly eliminate \(K=100,1000\)?

\[
\boxed{\textbf{No.}}
\]

The intended Gaussian lattice/orientation architecture is killed before family closure.

---

# 40. R7 / Reallocation Decision

The prompt required that R7 not continue indefinite Gaussian prime hunting if the architecture fails.

R6 activates that condition.

Recommended strategic verdict:

\[
\boxed{
\textbf{pause q=1 Gaussianization / Gaussian-prime hunting}.
}
\]

The remaining q=1 source problem is now much smaller—four maximal \((K,\tau)\) templates—but it requires a genuinely source-native theorem, not another Gaussian integral representation census.

Therefore q>1 should be raised in priority for the next fourth-85 round unless a new direct theorem specifically targets

\[
(K,\tau)\in
\{(100,1),(100,7),(1000,1),(1000,7)\}
\]

with the exact \(\rho\)-window and primitive source equation.

Formal R6 architecture verdict:

```text
GAUSSIAN_SPLIT_SOURCE_ARCHITECTURE = DEAD
Q1_GAUSSIAN_PRIME_HUNTING_CONTINUE = NO
Q1_SOURCE_NATIVE_FRONTIER = FOUR_MAXIMAL_TEMPLATES
Q_GT_1_PRIORITY = RAISE
```

---

# 41. Generated Artifact Index

Main report:

```text
Fourth_85_R6_Gaussian_Source_Embedding.md
```

Companion mathematical certificates:

```text
Fourth_85_R6_Explicit_Extension_Gaussianization_Certificate.md
Fourth_85_R6_Source_Lattice_Certificate.md
Fourth_85_R6_Tau39_Source_Closure_Certificate.md
Fourth_85_R6_Gaussian_Architecture_Autopsy.md
```

Computation directory:

```text
Fourth_85_R6_computation/
```

No \(K=100\), \(K=1000\), or q=1 final closure certificate is generated because those closures were not proved.

The R1–R5 checkpoint already exists in the archive and was not duplicated.

---

# 42. Terminal Ledger

```text
J2_STATUS = OPEN

K10_Q1_NEGATIVE_CLOSED = YES
K100_Q1_NEGATIVE_CLOSED = NO
K1000_Q1_NEGATIVE_CLOSED = NO
Q1_BRANCH_CLOSED = NO

TAU_DIVISIBLE_BY_3_SOURCE_FAMILIES_CLOSED = YES
NEW_HISTORICAL_CASES_CLOSED = 6
Q1_NEGATIVE_MAXIMAL_TEMPLATES_REMAINING = 4

EXACT_SOURCE_NORM_NORMALIZATION = YES
SOURCE_LATTICE_EXTRACTED = YES
SOURCE_LATTICE_SNF = (1,A2)
SOURCE_LATTICE_CONGRUENCE_SATURATED = YES

EXPLICIT_GAUSSIANIZATION_OVER_Q(G,sqrt(Q)) = YES
EXPLICIT_SOURCE_USEFUL_GAUSSIANIZATION_OVER_Q(G) = NO
SOURCE_AFFINE_GAUSSIANIZATION_IMPOSSIBLE = YES

GAUSSIAN_SOURCE_DIMENSION_DROP = NO
SOURCE_CONGRUENCE_EXACTIZED = NO
FINITE_GAUSSIAN_ORIENTATIONS_SOURCE_CANONICAL = NO
GAUSSIAN_PHASE_SOURCE_CANONICAL_AFTER_INTEGRALIZATION = NO

G5_K100_REPRESENTATION_COUNT = 8
G5_K1000_REPRESENTATION_COUNT = 8
G5_K100_SOURCE_HITS = 0
G5_K1000_SOURCE_HITS = 0

GAUSSIAN_SPLIT_SOURCE_ARCHITECTURE = DEAD
R7_GAUSSIAN_PRIME_HUNTING = NOT_AUTHORIZED
Q_GT_1_PRIORITY = RAISE
```
