# J2-65-R14 — Adelic Primitive Digit Shell × Whole-Modulus Boundary Transference

**Scope:** Strict Layer — A1-only — Exact Resonance `R=0` — `J=2` — `q>1` only  
**Round:** 65 第十四轮 / A1 统一终端线第三十九轮  
**Status:** **J2 OPEN**

## 1. Executive verdict

R14 achieves the requested recompression. The R13 object

\[
\text{primitive source-lattice ray}\times\text{reduced-residue multiplier interval}
\]

is exactly the radial/projective decomposition of one adelic integral-point shell on the source ternary quadric. More importantly, two apparent independent gates collapse:

1. the **primitive modulo-\(u\) ray gate retires completely** on a rationally split fibre (with the relevant real projective open nonempty);
2. the **multiplier gate is automatic outside one whole-modulus boundary layer**.

The sharp multiplier-failure theorem is

\[
\boxed{
\frac{G}{a_{3,0}}\,\kappa\!\left(\frac{x_0}{Aa_{3,0}}\right)
\le j(10u).
}
\tag{BT-sharp}
\]

This is stronger than the requested `j(10u)+C_end` form. The endpoint error is exactly bounded by one integer, and the Jacobsthal convention aligns the two `-1` terms so that the sharp boundary has **no additive error**.

Using Iwaniec's unconditional Jacobsthal bound,

\[
j(m)\ll (\log m)^2,
\]

with an absolute non-explicit constant, and `u<=G+1`, multiplier failure lies in the asymptotically thin layer

\[
\boxed{
\frac{G}{a_{3,0}}\kappa(\chi)=O((\log G)^2)
}
\]

or equivalently, for \(\kappa(\chi)>0\),

\[
\boxed{
a_{3,0}\gg \frac{G\kappa(\chi)}{(\log G)^2}.}
\]

R14 does **not** close `q>1`: the LOW boundary incidence and the source-quadric primitive-height geometry are not globally excluded. The resulting q>1 frontier is no longer an arbitrary ray × arbitrary multiplier interval. It is one projective W-sector intersected with one whole-modulus thin boundary condition.

---

## 2. R13 data actually used

R14 freezes the R13 source reconstruction

\[
N=q(G-1)Z-2Aa_3,
\qquad
t=q^2Z-4a_3,
\]

\[
Gs=h_ZZ+h_aa_3,
\]

with

\[
h_Z=q^2[c(G-1)-B],\qquad h_a=4B-2qcA,
\]

and sole remaining source-integrality congruence

\[
G\mid d(h_ZZ+h_aa_3).
\]

Writing

\[
\delta=\gcd(G,2d(q+4)),\qquad M=G/\delta,
\]

R13 gives SNF `(1,1,M)` and canonical source coordinates

\[
Z=Mw_1+\rho w_2,\qquad a_3=w_2,\qquad x=w_3.
\tag{CAN}
\]

R13 also gives the exact multiplier interval

\[
n_{\min}=\max\left(
\left\lfloor\frac{AG}{10x_0}\right\rfloor+1,
\left\lceil\frac{G}{10a_{3,0}}\right\rceil,
1\right),
\]

\[
n_{\max}=\left\lceil\frac{G}{a_{3,0}}\right\rceil-1,
\]

with `gcd(n,10u)=1`.

No R13 ray enumeration, no factorization of `u`, and no fixed `(g,k,q)` fibre is used in R14.

---

## 3. Adelic shell reformulation

Define

\[
\mathscr X_{\rm src}=\{v\in\Lambda_{\rm src}:Q_{\rm prim}(v)=0\}.
\]

Let `Omega_infty` be the inherited real homogeneous shell consisting of DIG3, LOW, UP, positivity, `ct-s>0`, orientation, and the remaining global W inequalities. Let `Omega_f` be the finite unit-open consisting of the primitive/source unit conditions.

Then the actual source problem is an integral shell incidence

\[
\boxed{
\mathscr X_{\rm src}(\mathbb Z)\cap\Omega_\infty\cap\Omega_f\ne\varnothing.
}
\]

Every nonzero integral source point has a unique decomposition

\[
v=n v_0,
\]

where `v0` is the unique positive primitive lattice generator of its rational ray. Under this decomposition, the homogeneous real gates split into a projective direction condition plus a one-dimensional radial interval, while the finite multiplier condition becomes

\[
n\in(\mathbb Z/10u\mathbb Z)^\times.
\]

Thus R13's ray × multiplier description is not a second object: it is exactly the projective/radial coordinate chart of this one adelic shell.

---

## 4. The power-of-ten lattice loses no information modulo u

From

\[
uq=G+1
\]

we have

\[
\gcd(G,u)=1,
\]

because a common divisor of `G` and `u` divides `uq-G=1`. Since `M|G`,

\[
\boxed{\gcd(M,u)=1.}
\]

The CAN matrix from `(w1,w2,w3)` to `(Z,a3,x)` is upper triangular with determinant `M`. Hence modulo `u` it is invertible:

\[
\boxed{
(\mathbb Z/u\mathbb Z)^3\xrightarrow{\sim}(\mathbb Z/u\mathbb Z)^3.
}
\]

Explicitly,

\[
w_2=\bar a,
\quad w_3=\bar x,
\quad w_1=M^{-1}(\bar Z-\rho\bar a).
\]

So the SNF factor `M` creates no modulo-u loss.

---

## 5. Exact saturation of Qprim modulo u

This is the main finite-place theorem of R14.

### 5.1 Remove the global rational scalar

Substituting the R13 reconstruction for `s,t` into the actual R13 radial quadratic form gives exactly

\[
Q_{\rm rad}(Z,a_3,x)
=
\frac{(q+4)^2c^2}{G}\,F_{\rm src}(G,K,q;Z,a_3,x),
\]

where `F_src` is an integral homogeneous ternary quadratic form.

### 5.2 Consume the exact cyclotomic identity before reducing modulo u

Now substitute the exact identity

\[
G=uq-1.
\]

The gcd in `Z[u,q,K]` of the six quadratic coefficients of the specialized `F_src` is exactly

\[
\boxed{q^5.}
\]

Define

\[
F_0:=q^{-5}F_{\rm src}|_{G=uq-1}.
\]

This is again integral. Its six coefficients are recorded and symbolically checked in `J2-65-R14-ModUAutomaticity.py`.

Reduction modulo `u` is now exact and primitive:

\[
\boxed{F_0\equiv x^2-Z^2\pmod u.}
\tag{F0-USQ}
\]

The coefficient of `x^2` in `F0` is

\[
(2u+1)(qu-1)^2\equiv1\pmod u.
\]

Therefore any further coefficient content introduced after substituting the CAN lattice coordinates is automatically coprime to `u`. Consequently the R13 primitive integral form satisfies

\[
\boxed{
Q_{\rm prim}\equiv\varepsilon\,[x^2-Z^2]\pmod u,
\qquad
\varepsilon\in(\mathbb Z/u\mathbb Z)^\times.
}
\tag{QPRIM-USQ}
\]

This is **EQUIVALENT**, not merely partial.

---

## 6. Composite primitive-open approximation: finite obstruction retired

Because `G=10^g` is even, `u|G+1` is odd. By (QPRIM-USQ), the composite residue class

\[
Z=1,\qquad x=1
\]

(with arbitrary `a3` residue) lies on the reduced conic modulo `u`. At such a residue point,

\[
\frac{\partial Q_{\rm prim}}{\partial x}
\equiv2\varepsilon x
\]

is a unit modulo `u`.

### Composite Hensel lemma

No factorization of `u` is required. Suppose a quadratic polynomial equation has a solution `r_k` modulo `u^k`, and one partial derivative is a unit modulo `u`. Write

\[
Q(r_k)=u^kE_k.
\]

Choose `t mod u` solving

\[
E_k+t\,Q_x(r_k)\equiv0\pmod u,
\]

and replace the `x` coordinate by `x+u^k t`. The quadratic remainder has a factor `u^{2k}`, hence is divisible by `u^{k+1}` for `k>=1`. This recursively gives a compatible solution modulo every `u^k` with `Z` remaining a unit.

Thus the finite primitive local open is nonempty **as one composite object**.

Now condition on the rational/Brauer layer being split. The smooth projective source conic then has a rational point and is Q-isomorphic to `P^1`. Weak approximation on `P^1` simultaneously at the real place and at the finite places supporting `u` gives a rational source-conic point inside:

- any prescribed nonempty real projective W-sector;
- the composite finite primitive unit-open just constructed.

Finally clear source-lattice denominators and divide by the global gcd. Projective unit-openness is invariant under local unit rescaling, so the canonical primitive lattice generator satisfies

\[
\gcd(Z_0,u)=1.
\]

Then U-SQ gives

\[
\gcd(x_0,u)=1.
\]

Hence

\[
\boxed{
\texttt{PRIMITIVE_MODULO_u_OBSTRUCTION=RETIRED}.
}
\]

Strong approximation is not used; ordinary weak approximation on the split projective conic plus the exact primitive lattice lift is sufficient.

---

## 7. Radial Window Projectivization

Assume a legal multiplier `n` exists. LOW and the strict DIG3 upper bound are

\[
nx_0>\frac{AG}{10},
\qquad
na_{3,0}<G.
\]

Therefore

\[
10nx_0>AG>A n a_{3,0}.
\]

Since `n>0`,

\[
\boxed{10x_0>Aa_{3,0}.}
\tag{PROJ-LOW}
\]

Define

\[
\chi=\frac{x_0}{Aa_{3,0}},
\qquad
H=\frac{G}{a_{3,0}},
\]

\[
\theta(\chi)=\max\left(\frac1{10},\frac1{10\chi}\right),
\qquad
\kappa(\chi)=1-\theta(\chi).
\]

Then

\[
\kappa(\chi)>0\iff\chi>\frac1{10}.
\]

Ignoring endpoint inclusivity only for the purpose of measuring length, the continuous radial window has width

\[
\boxed{W_{\mathbb R}=H\kappa(\chi).}
\]

The single scalar `kappa` therefore replaces the two lower endpoints as the global frontier variable.

---

## 8. Exact floor/ceil correction

The exact count of integers satisfying LOW, DIG3, and `n>=1` before the coprimality condition is

\[
N_I=
\max\left(
0,
\left\lceil H\right\rceil-
\max\left(
\left\lfloor\frac{H}{10\chi}\right\rfloor+1,
\left\lceil\frac H{10}\right\rceil,
1
\right)
\right).
\]

The elementary inequalities for floor and ceiling give the uniform sharp endpoint estimate

\[
\boxed{
H\kappa(\chi)-1\le N_I < H\kappa(\chi)+1.
}
\tag{INT-WIDTH}
\]

Thus

\[
\boxed{C_{\rm end}=1.}
\]

The exact left-endpoint inclusion differs depending on which lower inequality is active, but this is an endpoint convention only; it does not create a second global branch and does not alter the width functional.

---

## 9. Whole-modulus covering radius

Fix

\[
m=10u.
\]

Use the convention

\[
\boxed{
 j(m)=\min\{J:\text{every block of }J\text{ consecutive integers contains an }n\text{ with }(n,m)=1\}.
}
\]

Coprimality depends only on the radical, so prime powers do not require a new definition; no factorization is performed.

Iwaniec's 1978 theorem for Jacobsthal's problem proves, for the maximum bad run covered by `r` arbitrary primes,

\[
C(r)\ll r^2(\log r)^2.
\]

Together with the standard lower growth of the product of the first `r` primes, this gives the unconditional whole-modulus bound

\[
\boxed{j(m)\ll(\log m)^2.}
\tag{IW}
\]

The implied constant is absolute but non-explicit in the theorem used here. The theorem is asymptotic/uniform; R14 does not invent a numerical constant.

Since `u<=G+1`,

\[
\boxed{j(10u)=O((\log G)^2)=o(G).}
\]

This establishes Success F in an unconditional but non-explicit-constant form.

---

## 10. Radial Window Boundary Transference

If the exact integer interval contains no integer coprime to `m=10u`, then by the chosen Jacobsthal convention its number of consecutive integers satisfies

\[
N_I\le j(10u)-1.
\]

Combine this with (INT-WIDTH):

\[
H\kappa-1\le N_I\le j(10u)-1.
\]

The endpoint errors cancel exactly:

\[
\boxed{H\kappa\le j(10u).}
\]

Hence

\[
\boxed{
\frac{G}{a_{3,0}}
\kappa\left(\frac{x_0}{Aa_{3,0}}\right)
\le j(10u).
}
\tag{BT}
\]

Equivalently, the complement is automatic:

\[
\boxed{
\frac{G}{a_{3,0}}\kappa(\chi)>j(10u)
\Longrightarrow
\exists n\in I_{\mathbb Z},\ (n,10u)=1.
}
\]

So multiplier failure is no longer an independent residue problem. It is one arithmetic/projective boundary inequality.

With (IW), every failing ray with positive clearance obeys

\[
\boxed{
a_{3,0}\gg\frac{G\kappa(\chi)}{(\log G)^2}.}
\]

This is the requested arithmetic-to-height transference.

---

## 11. LOW boundary incidence with the source conic

The projective LOW boundary is

\[
\boxed{10x=Aa_3.}
\]

Set `a3=1` projectively and eliminate `x`. Substitution into the saturated source conic produces a genuine quadratic polynomial in

\[
z=Z/a_3.
\]

After removing harmless content, its leading coefficient is

\[
\boxed{
100G^3q^4(2G^2+Gq+2G+2q)>0.
}
\]

Its discriminant is exactly

\[
\boxed{-400q^6\,\mathfrak D_{\rm LB}(G,K,q),}
\]

where the full polynomial `D_LB` is written in `J2-65-R14-ProjectiveBoundary.tsv` and generated independently by `J2-65-R14-ProjectiveBoundary.py`.

The current global identities do not fix the sign of `D_LB` after simultaneously imposing the inherited W-sector inequalities. Therefore R14 does **not** assert that the LOW boundary is empty, nor does it assert a uniform positive clearance. The correct verdict is

```text
LOW_BOUNDARY_CONIC_INTERSECTION=OPEN
UNIFORM_PROJECTIVE_CLEARANCE=UNRESOLVED
```

Crucially, the incidence has nevertheless been compressed to **one boundary divisor/discriminant object**, not a list of intersections.

---

## 12. Primitive height audit

The digit gauge makes

\[
a_{3,0}=w_2>0
\]

a canonical arithmetic height coordinate of the primitive ray. R14 finds no contradiction between large `a3_0` and primitive isotropy from the SNF factor `M` alone. In particular, neither

- `SNF=(1,1,M)`, nor
- primitivity of `(w1,w2,w3)`

provides a global upper bound on `a3_0`.

The new information is instead a **lower bound on every multiplier-failing primitive ray**:

\[
a_{3,0}\ge \frac{G\kappa(\chi)}{j(10u)}.
\]

Thus the remaining height question is exactly the one proposed for the next global round: can the source conic and its discriminant/covolume geometry exclude primitive isotropic rays whose canonical digit-height is this large while remaining in the projective W-sector?

No arbitrary Euclidean norm replaces `a3_0`.

---

## 13. Gate retirement ledger

### Automatic / retired in R14

- `gcd(M,u)=1`;
- canonical source-coordinate map modulo `u`;
- `Qprim mod u` versus U-SQ: equivalent up to a unit;
- nonemptiness of the composite primitive local open;
- primitive `Z0`-unit obstruction on a split conic with nonempty real sector;
- `x0`-unit once `Z0`-unit holds;
- multiplier existence whenever `H*kappa > j(10u)`.

### Still genuine

- projective feasibility `chi>1/10`;
- inherited UP/positivity/`ct-s`/W-sector geometry;
- the LOW-boundary divisor incidence;
- the thin Jacobsthal boundary `H*kappa<=j(10u)`;
- primitive source-height geometry inside that boundary.

Thus the finite primitive layer has retired; the remaining q>1 problem is real/projective plus one whole-modulus height boundary.

---

## 14. Three reusable general tools extracted

### Tool A — Radial Window Projectivization Lemma

For a homogeneous ray `v=n v0`, a radial lower inequality and a radial upper digit inequality can be divided by the common positive multiplier to give a projective feasibility inequality. The residual radial freedom is a one-dimensional interval whose width is primitive height times a projective clearance functional.

Here:

\[
LOW+DIG3\Rightarrow10x_0>Aa_{3,0},
\]

and

\[
W_{\mathbb R}=\frac{G}{a_{3,0}}\kappa(\chi).
\]

### Tool B — Whole-Modulus Boundary Transference

If a one-dimensional integer interval must hit `(Z/mZ)^x`, then failure implies an Archimedean boundary inequality controlled by the whole-modulus reduced-residue covering radius. With the aligned convention used here:

\[
\text{failure}\Rightarrow W_{\mathbb R}\le j(m).
\]

No residue tree is required.

### Tool C — Primitive-Open Approximation on a Split Integral Conic

If an integral conic model has a composite-modulus smooth primitive residue point and its projective conic is split over Q, composite Hensel creates the finite adelic open and weak approximation creates a rational point simultaneously in that open and any prescribed nonempty real projective sector. Primitive lattice normalization then preserves the local unit property.

The R14 source conic realizes this tool because its saturated reduction is `x^2-Z^2` modulo `u`.

---

## 15. Direct answers to Q1–Q15

### Q1. Can R13 ray × multiplier be completely rewritten as one adelic integral-point shell?

**Yes.** The ray/multiplier pair is precisely the projective/radial decomposition of `X_src(Z) ∩ Omega_infty ∩ Omega_f`.

### Q2. Why is `M=G/delta` necessarily a unit modulo u?

`uq=G+1` gives `gcd(G,u)=1`; since `M|G`, `gcd(M,u)=1`.

### Q3. Do canonical source coordinates give a full isomorphism modulo u?

**Yes.** Their determinant is `M`, a unit modulo `u`; the inverse is `w2=a`, `w3=x`, `w1=M^{-1}(Z-rho a)`.

### Q4. Does `Qprim mod u` reduce exactly to U-SQ?

**Yes, up to a unit.** Exact saturation gives `F0 mod u=x^2-Z^2`; all later primitive content is a unit modulo `u`, so `Qprim ≡ epsilon(x^2-Z^2)`.

### Q5. On a rationally split fibre, is a primitive Z0-unit ray automatic?

**Yes, provided the target real projective sector is nonempty.** The finite primitive open itself is proved nonempty by composite Hensel; weak approximation then meets it together with the real sector.

### Q6. Can the R13 primitive modulo-u obstruction be permanently retired?

**Yes.** `PRIMITIVE_MODULO_u_OBSTRUCTION=RETIRED`.

### Q7. Do LOW and DIG3 strictly imply `10x0>Aa3_0`?

**Yes**, by comparing `10 n x0 > AG` with `A n a3_0 < AG` and cancelling positive `n`.

### Q8. Can the continuous multiplier window be described by one projective clearance functional?

**Yes.** `kappa(chi)=1-max(1/10,1/(10chi))`, and the continuous width is `(G/a3_0)kappa(chi)`.

### Q9. How large is the exact floor/ceil endpoint error?

**One integer.** Precisely `H*kappa-1 <= #I_Z < H*kappa+1`; therefore `C_end=1`.

### Q10. Does multiplier failure imply a whole-modulus boundary-transference inequality?

**Yes, in sharper form:**

\[
(G/a_{3,0})\kappa(\chi)\le j(10u).
\]

### Q11. What is the strongest global bound used for j(10u)?

The unconditional Iwaniec bound used here is

\[
j(m)\ll(\log m)^2,
\]

with an absolute non-explicit constant. Thus `j(10u)=O(log^2 G)=o(G)`.

### Q12. Does the LOW projective boundary intersect the admissible source conic?

**Globally unresolved.** Exact elimination reduces the question to one quadratic incidence with discriminant `-400q^6 D_LB(G,K,q)`. Current global W inequalities do not yet fix its admissible sign/incidence.

### Q13. If no multiplier exists, where is the primitive ray forced?

Into the single boundary layer

\[
\boxed{
\mathscr B_{\rm Jac}=\{[v_0]:(G/a_{3,0})\kappa(\chi)\le j(10u)\}.
}
\]

Asymptotically this is `(G/a3_0)kappa=O(log^2 G)`.

### Q14. Which primitive/multiplier gates are automatic and which remain independent?

The modulo-u primitive gate is automatic/retired on split fibres; `x0`-unit follows from U-SQ; multiplier coprimality is automatic outside `B_Jac`. The genuinely independent remainder is the real projective W geometry together with the thin height/clearance boundary.

### Q15. Can the R14 q>1 frontier be compressed to one thin adelic/projective boundary layer, or is it empty?

It is compressed to **one thin whole-modulus/projective boundary layer intersected with the inherited real W-sector**, but it is **not proved empty**. The remaining unresolved incidence is precisely the LOW/projective divisor plus primitive source-height geometry inside

\[
(G/a_{3,0})\kappa(\chi)\le j(10u)=O(\log^2G).
\]

Therefore

\[
\boxed{\textbf{J2 OPEN}.}
\]

The correct next global object is

\[
\boxed{
\textbf{Source-Quadric Height Geometry}
\times
\textbf{Primitive Lattice Discriminant}
\times
\textbf{LOW-Boundary Incidence}.
}
\]

No return to ray-by-ray, residue-by-residue, or prime-by-prime analysis is justified.
