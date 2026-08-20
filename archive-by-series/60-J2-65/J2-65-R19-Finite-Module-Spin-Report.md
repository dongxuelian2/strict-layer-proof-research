# J2-65-R19 — Spin Homogeneous Space × Composite Finite Module × Integral Isotropic Veronese × Digit-Shell Approximation

**Scope:** Strict Layer — A1-only — Exact Resonance `R=0` — `J=2` — `q>1`  
**Round:** 65 第十九轮 / A1 统一终端线第四十四轮  
**Status:** **J2 OPEN**

## 0. Executive verdict

R19 does **not** prove that the R18 cyclic packet is automatic.  It does, however, identify exactly why the tempting `Spin ~= SL2 => one orbit => automatic` argument is invalid.

The moving R18 packet is an exact **kernel**, not an unknown affine class.  In the R18 semantic ambient lattice `L0` let

\[
\ell_M^{\rm sem}
\]

be the transported source row coming from

\[
\ell_M(Z,a,h)=Z+\beta_0a,\qquad \beta_0=u(1+2u)^3.
\]

Then

\[
\widetilde\pi_{\rm src}(v)
=
\bigl(\ell_M^{\rm sem}(v)\bmod M_0,\;V(v)\bmod q^2\bigr)
\]

has kernel equal to the actual moving source lattice.  Since `(M0,q)=1`, CRT gives one exact cyclic quotient map

\[
\boxed{
\pi_{\rm src}(v)
=e_M\ell_M^{\rm sem}(v)+e_qV(v)
\pmod{M_0q^2},
}
\]

where

\[
e_M=q^2(q^2)^{-1}_{M_0},\qquad
e_q=M_0M_0^{-1}_{q^2}.
\]

Thus

\[
\boxed{c_{\rm src}=0},\qquad
\boxed{\Gamma_{\rm src}=\ker\pi_{\rm src}}.
\]

The decisive new fact is **bad reduction at the M0 part of the packet**.  Since `M0|G`,

\[
F_0=GA(GA+2)\equiv0\pmod{M_0},
\]

and because

\[
D_0=S_0^2-F_0W_0,\qquad S_0\equiv20u\pmod{M_0},
\]

we get the exact whole-module degeneration

\[
\boxed{
Q_0(R,V,H)
\equiv
(R-20uV)(R+20uV)
\pmod{M_0}.
}
\tag{M0-DEG}

The `H`-direction disappears and the ternary quadratic module is no longer nondegenerate.  Therefore the standard smooth split rank-3 Spin transitivity paradigm is **not applicable to the very modulus that carries the M0 source packet**.  The natural whole-module invariant is the ordered ruling-ideal pair

\[
\boxed{
\mathfrak r_{M_0}(v)
=
\bigl((R-20uV),(R+20uV)\bigr)
\quad\text{in }\operatorname{Ideals}(\mathbf Z/M_0\mathbf Z).
}
\tag{RUL}

R19 does not factor `M0`, and consequently does not explode this ideal pair into prime-power valuations.  It also cannot certify that the number of semantic Spin orbits is a fixed `O(1)` constant.

On the rationally split generic fibre, the rational group side behaves as expected: the even Clifford algebra of the nondegenerate ternary form is a quaternion algebra; isotropy splits it, and

\[
\boxed{\operatorname{Spin}(Q_0)\simeq SL_2\quad\text{over }\mathbf Q}
\]

conditionally on `X0(Q) != empty`.  But the integral group is the norm-one group of the actual even-Clifford order stabilizing `L0`, not automatically `SL2(Z)`, and its reduction at the packet modulus inherits the bad-reduction problem.

The conic nevertheless admits a clean witness-dependent degree-2 Veronese chart.  For a rational isotropic base point

\[
p=(p_R,p_V,p_H),\qquad p_R^2-D_0p_V^2-F_0N_0p_H^2=0,
\]

one valid transverse chart is

\[
\boxed{
\begin{aligned}
F_R(s,t)&=-p_Rs^2-D_0p_Rt^2+2D_0p_Vst,\\
F_V(s,t)&= p_Vs^2+D_0p_Vt^2-2p_Rst,\\
F_H(s,t)&= p_H(s^2-D_0t^2),
\end{aligned}}
\tag{VER}
\]

and exactly

\[
\boxed{
Q_0(\mathbf F(s,t))=(s^2-D_0t^2)^2Q_0(p)=0.
}
\]

Hence the entire source packet pulls back to **one degree-2 projective congruence condition** on `P1(Z/m_src)`.  In particular,

\[
\boxed{F_V(s,t)\equiv0\pmod{q^2}}
\]

is the conductor part, while

\[
\boxed{(\ell_M^{\rm sem}\circ\nu_p)(s,t)\equiv0\pmod{M_0}}
\]

is the M0 part.  CRT recombines them without factorizing either modulus.

The Archimedean side is no longer the essential difficulty.  R14 already established the relevant mechanism on a split conic: after a finite congruence class is known to be admissible, weak approximation on `P1` hits it simultaneously with any nonempty real projective open.  The same argument applies here to the degree-2 packet pullback.  Thus

\[
\boxed{
\text{finite admissibility}
+\text{nonempty digit arc}
\Longrightarrow
\text{simultaneous finite + real realization}.
}
\tag{CAI}

What remains unknown is finite **admissibility/liftability itself** for the semantic integral Spin orbit.  Strong approximation for the rationally split simply connected group cannot manufacture a class which is absent from, or separated inside, the bad-reduction finite orbit.

Accordingly the mandatory verdict is

```text
FINITE_PACKET_VERDICT=UNRESOLVED_GROUP_THEOREM
FINITE_PACKET_AUTOMATIC_ON_AMBIENT_ISOTROPIC_LOCUS=UNRESOLVED
```

and the unique missing theorem is:

> **Semantic Conductor–Ruling Lifting Theorem.**  On every rationally split actual power-of-ten fibre, classify the orbit of the semantic integral Spin group on the bad-reduction finite module and decide whether the kernel class `pi_src=0` is reached; equivalently, prove or disprove that the degree-2 projective packet pullback contains an admissible primitive class.  The theorem must work over the whole composite modulus `M0*q^2` without prime decomposition.

This is a much sharper terminal object than “finite packet remains”.

---

## 1. Exact source quotient map

R18 gives two independent moving rows before CRT:

1. the pre-Schur source row `M0 | Z+beta0*a`;
2. the post-Schur conductor row `q^2 | V`.

Both are zero-class conditions.  There is no translation term in either construction.  Let

\[
C_M=\mathbf Z/M_0\mathbf Z,
\qquad
C_q=\mathbf Z/q^2\mathbf Z.
\]

The direct quotient map is

\[
\widetilde\pi_{\rm src}:L_0\to C_M\oplus C_q,
\qquad
v\mapsto(\ell_M^{\rm sem}(v),V(v)).
\]

The phrase `ell_M^sem` is important: R18's canonical ambient is **not raw Z^3_RVH**.  It retains the decimal chart/contact line as semantic integral structure.  Transporting the exact pre-Schur row through that source-preserving coordinate dictionary is therefore an exact integral functional on `L0`, even though R18 did not print a single expanded polynomial row in `(R,V,H)`.

Using the CRT idempotents above yields the requested cyclic map.  Hence:

```text
SOURCE_PACKET_MODULUS=m_src=M0*q^2
SOURCE_CLASS=0
SOURCE_LATTICE_IS_KERNEL_OR_COSET=KERNEL
SOURCE_QUOTIENT_CYCLIC=TRUE
```

No affine ambiguity survives R19.

---

## 2. Spin group of the q-free rational fibre

Write

\[
Q_0=R^2-D_0V^2-C_0H^2,
\qquad C_0:=F_0N_0.
\]

On actual smooth fibres, R7/R13 give signature `(2,1)`.  For a nondegenerate ternary quadratic space in characteristic zero, its even Clifford algebra `C^0(Q0)` is a quaternion algebra.  The Spin group is the norm-one group of this quaternion algebra.

If the conic has a rational point, the ternary space is isotropic.  Then the quaternion algebra splits and one obtains a rational identification

\[
C^0(Q_0)\simeq M_2(\mathbf Q),
\qquad
\operatorname{Spin}(Q_0)\simeq SL_2.
\]

An explicit conjugating matrix is necessarily witness-dependent in this campaign because R13/R17 proved that there is no universal rational isotropic section.  Given one rational isotropic vector `p`, choose `e` with `B(p,e)=1`, replace `e` by `e-Q(e)p/2`, and complete by a vector orthogonal to the resulting hyperbolic plane.  This gives a rational Witt basis and then the standard traceless-`2x2` determinant model.

At the integral level define the even-Clifford order

\[
\mathcal O_{L_0}:=C^0(L_0,Q_0)
\]

and

\[
\Gamma_{\rm Spin}
=
\{x\in\mathcal O_{L_0}^{\times}:\operatorname{nrd}(x)=1,\ xL_0x^{-1}=L_0\}.
\]

R19 deliberately does **not** identify this group with `SL2(Z)`.

---

## 3. Why composite one-orbit transitivity fails as a theorem template

The requested transitivity theorem would require a nondegenerate rank-3 quadratic module over the finite ring.  The actual coefficient structure violates that hypothesis at `M0`.

Because `M0|G`,

\[
F_0\equiv0\pmod{M_0}.
\]

Also

\[
S_0=2uG^3AK+20u\equiv20u\pmod{M_0}
\]

and

\[
D_0-S_0^2=-F_0W_0\equiv0\pmod{M_0}.
\]

Therefore

\[
D_0\equiv400u^2\pmod{M_0},
\]

which gives (M0-DEG).  In particular the gradient has no `H` contribution modulo `M0`, and the discriminant of the ternary form is not a unit in `Z/M0Z`.

Thus:

```text
SPIN_ACTION_TRANSITIVE=NOT_PROVED
REASON=SMOOTH_NONDEGENERATE_FINITE_QUADRATIC_MODULE_HYPOTHESIS_FAILS_ON_M0
```

The correct finite object is a degenerate homogeneous-space problem, not the usual smooth split conic over a finite ring.

### Ruling ideal invariant

Set

\[
L_-=R-20uV,
\qquad
L_+=R+20uV.
\]

Every isotropic state modulo `M0` obeys

\[
L_-L_+=0.
\]

Over a ring with zero divisors this does **not** force one factor to vanish globally.  The factor-allocation information can be retained without prime splitting by the ordered ideal pair

\[
((L_-),(L_+)).
\]

This is the R19 whole-module replacement for a residue table.  No theorem in the actual artifacts proves that this invariant has only a fixed number of semantic Spin values independent of the modulus.

---

## 4. Integral isotropic Veronese map

Let `p` be any rational isotropic basepoint and let

\[
x(s,t)=(s,t,0).
\]

For the polar form

\[
B((R,V,H),(R',V',H'))=RR'-D_0VV'-C_0HH',
\]

define

\[
\mathbf F(s,t)=Q_0(x)p-2B(p,x)x.
\]

A direct identity gives

\[
Q_0(\mathbf F)=Q_0(x)^2Q_0(p),
\]

which yields (VER).  This is an exact degree-2 parametrization on the transverse chart.

After multiplying the basepoint by one common denominator, all three forms are integral.  A primitive integral vector is recovered by dividing by the global content

\[
c(s,t)=\gcd(F_R,F_V,F_H).
\]

R19 does not decompose `c(s,t)` prime-by-prime.  Projective surjectivity is proved on the chart; a second transverse chart handles the exceptional tangent direction if needed.

Hence:

```text
RATIONAL_ISOTROPIC_BASEPOINT=WITNESS_DEPENDENT
VERONESE_DEGREE=2
INTEGRAL_PARAMETERIZATION=PROVED_PROJECTIVELY_AFTER_ONE_DENOMINATOR_CLEARING
PRIMITIVE_CONTENT_FUNCTION=gcd(F_R,F_V,F_H)
```

---

## 5. Packet pullback to P1

Because `pi_src` is linear on the semantic ambient and `nu_p` is degree two,

\[
\Phi_m:=\pi_{\rm src}\circ\nu_p
\]

is a homogeneous quadratic map modulo `m_src`.  The source parameter scheme is

\[
\mathcal P_{\rm src}
=
\{[s:t]\in\mathbf P^1(\mathbf Z/m):\Phi_m(s,t)=0\}.
\]

The two structural projections are:

\[
F_V(s,t)\equiv0\pmod{q^2},
\]

and

\[
(\ell_M^{\rm sem}\circ\nu_p)(s,t)\equiv0\pmod{M_0}.
\]

They are recombined only at the end by CRT.  No factor of `M0` or `q` is inspected.

R19 finds no identity making either polynomial vanish identically on `P1`.  Therefore `P_src=ALL_P1` is not proved.

---

## 6. q^2 conductor audit

The conductor row is exactly

\[
V\equiv0\pmod{q^2}.
\]

Under (VER) this becomes

\[
\boxed{
p_Vs^2-2p_Rst+D_0p_Vt^2\equiv0\pmod{q^2}.
}
\tag{COND-P1}

This is a genuine degree-2 finite incidence.  It is not a formal consequence of `Q0=0`.

A subtlety is that the semantic contact line is already built into `L0`, so raw `(R,V,H)` reduction can look more singular than reduction in a primitive basis of `L0`.  R19 therefore does not infer non-liftability merely from a singular raw residue.  Conversely, the existence of a raw residue with `V=0` is also insufficient: it must lie in the reduction of an actual integral/rational Spin orbit.

Thus:

```text
q2_CONDUCTOR_PACKET=UNRESOLVED
V_DIVISIBLE_BY_q2_CAN_BE_FORCED_BY_SPIN_ACTION=UNRESOLVED
q2_PACKET_RETIRED=FALSE
```

The exact missing statement is conductor-divisibility lifting in the semantic integral Spin orbit.

---

## 7. M0 packet audit

The M0 source row remains linear before the Veronese pullback, but the ambient quadratic form degenerates exactly at the same modulus.  Consequently the M0 packet cannot be dismissed by smooth finite-conic transitivity.

The natural terminal invariant is (RUL).  R19 does not prove that the source hyperplane `ell_M^sem=0` is one of the two rulings; such an identification would require an exact expanded Schur transport not present in the R18 printed artifacts and must not be guessed.

Hence:

```text
M0_SOURCE_PACKET=UNRESOLVED
M0_PACKET_GROUP_THEOREM=SEMANTIC_BAD_REDUCTION_RULING_ORBIT_CLASSIFICATION
M0_PRIME_DECOMPOSITION_USED=FALSE
```

---

## 8. Strong approximation: what it does and does not solve

On a rationally split fibre, the rational Spin group is simply connected and isotropic of type A1.  Abstract strong approximation therefore supplies the expected density/surjectivity behavior for the group away from the excluded places.

But this theorem acts on the **group**.  To deduce packet automaticity one must already know that the required finite source state lies in the same finite homogeneous orbit under the integral semantic model.  The bad M0 reduction and q2 conductor section are precisely where that implication is missing.

Therefore:

```text
STRONG_APPROXIMATION_APPLICABLE=PARTIAL
ABSTRACT_SPLIT_GROUP_THEOREM=YES
SEMANTIC_FINITE_ORBIT_CONSEQUENCE=NOT_PROVED
```

This is not a failure of the classical theorem; it is a failure of its hypotheses/bridge at the integral homogeneous-space level.

---

## 9. Congruence–Archimedean independence and the digit shell

Once a nonempty admissible projective packet class is available, R14's mechanism generalizes cleanly from the old primitive-`u` open to the present whole-modulus congruence neighborhood.

On a split conic `C0 ~= P1`, a residue class modulo a fixed integer determines a finite adelic open neighborhood of any liftable local point.  A nonempty real digit arc is another open.  Weak approximation on `P1` simultaneously hits both.  Clearing denominators by finite-place units and primitive normalization preserves the projective finite class.

Thus R19 proves the conditional theorem

\[
\boxed{
\mathcal P_{\rm src}(m)\ne\varnothing
\ +\ I_{\rm digit}\ne\varnothing
\Longrightarrow
\mathbf P^1(\mathbf Q)\text{ hits both.}
}
\]

The radial/contact scale must still be reconstructed with R18's exact formulas

\[
h=H/\mu_0,
\qquad
 a=(R-\lambda_hH/\mu_0)/(q^5D_0),
\]

and the inherited multiplier/height theorems.  R19 does not reopen Jacobsthal or primitive-`u` analysis.

The key strategic consequence is:

\[
\boxed{
\text{the real digit shell is not the current independent R19 obstruction.}
}
\]

The finite admissibility theorem must be settled first.

---

## 10. Semantic stabilizer

The correct group is not the full rational orthogonal group of raw `Z^3`.  Define

\[
\Gamma_{\rm sem}:=
\{g\in\operatorname{Spin}(Q_0)(\mathbf Q):gL_0=L_0\}.
\]

Because R18's `L0` already includes the fixed decimal/contact integral structure, no second arbitrary subgroup is introduced merely to remember those fixed conditions.

The digit-height inequalities themselves are not group-invariant.  They are attached after orbit admissibility by the projective approximation theorem.

This separation prevents the false inference

\[
\text{full rational Spin transitivity}
\Rightarrow
\text{source semantic automaticity}.
\]

---

## 11. Four reusable general tools

### Tool A — Finite-Packet Homogeneous-Space Principle

A finite-index source lattice inside an integral homogeneous space is encoded by an exact quotient map.  Automaticity is an orbit-incidence question for the kernel class, not a residue-list problem.

### Tool B — Bad-Reduction Ruling Principle for Ternary Packets

If a source modulus divides a coefficient-discriminant factor so that a ternary conic reduces to

\[
L_-L_+=0,
\]

then smooth Spin transitivity cannot be invoked.  The factor-allocation data should be retained as an ideal pair over the whole composite ring rather than prime-split valuations.

### Tool C — Integral Isotropic Veronese Pullback

Given one rational isotropic witness, the formula

\[
F(x)=Q(x)p-2B(p,x)x
\]

organizes the conic by homogeneous binary quadratic forms.  Every linear finite packet pulls back to a fixed degree-2 projective condition.

### Tool D — Congruence–Archimedean Independence on a Split Conic

Once the finite parameter condition has a liftable point, weak approximation on `P1` independently imposes any nonempty real arc.  Thus a digit shell does not create a new obstruction after finite admissibility.

---

## 12. Mandatory sixteen answers

### Q1. Exact quotient map?

\[
\pi_{\rm src}=e_M\ell_M^{\rm sem}+e_qV\pmod{M_0q^2}.
\]

### Q2. Kernel or affine coset?

**Kernel.**  `c_src=0`.

### Q3. Spin group?

Type `A1`; even Clifford algebra is quaternionic, and on a rationally isotropic fibre `Spin(Q0) ~= SL2` over `Q`.

### Q4. Explicit split homogeneous space?

**Yes, conditionally on a rational isotropic witness.**  The conjugacy/Witt basis and Veronese chart are witness-dependent because there is no universal rational section.

### Q5. Orbit count modulo whole m?

**Not classified.**  A smooth one-orbit theorem is inapplicable because the `M0` reduction is degenerate.

### Q6. Uniformly bounded independent of factorization?

**Not proved.**  The whole-module ruling ideal pair is identified instead; no prime decomposition is used.

### Q7. Integral isotropic Veronese map?

**Projectively yes.**  Formula (VER) is degree 2; after one denominator clearing it is integral, with global content `c(s,t)` for primitive normalization.

### Q8. Packet pullback to P1?

One homogeneous degree-2 condition `Phi_m(s,t)=0`, whose q2 component is (COND-P1) and whose M0 component is `ell_M^sem(nu_p)=0`.

### Q9. q2 conductor automatic?

**UNRESOLVED.**  It is not an algebraic identity; conductor-divisibility lifting in the semantic Spin orbit is missing.

### Q10. M0 packet automatic?

**UNRESOLVED.**  The ambient form has the exact bad reduction (M0-DEG), so smooth finite-conic transitivity cannot decide it.

### Q11. Entire packet one Spin orbit condition?

It is one **kernel-orbit incidence condition**, but R19 cannot prove that the kernel is one orbit representative under the semantic integral group.

### Q12. Finite congruence + real shell simultaneous approximation?

**Yes, conditionally on finite admissibility.**  Weak approximation on the split `P1` gives Congruence–Archimedean Independence.

### Q13. Does fixed contact-height semantic lattice break full Spin transitivity?

It invalidates use of the raw rational group as the integral actor.  The correct actor is the stabilizer of `L0`.  More decisively, the `M0` reduction of that integral model is singular.

### Q14. How many semantic finite orbits remain?

No fixed number is proved.  Their whole-module invariant is compressed to the ruling ideal pair plus the q2 conductor condition.

### Q15. R18 packet verdict?

\[
\boxed{\texttt{UNRESOLVED\_GROUP\_THEOREM}.}
\]

The unresolved theorem is `SEMANTIC_CONDUCTOR_RULING_LIFTING`.

### Q16. Can the frontier be reduced to binary/projective parameter space × digit shell?

**Yes at the geometric level, but not with the packet erased.**  The correct R19 terminal form is

\[
\boxed{
\mathbf P^1(\mathbf Q)
\times
\{\Phi_{m_{\rm src}}=0\}
\times
I_{\rm digit}
\times
\text{radial/contact height reconstruction}.
}
\]

After finite admissibility is proved, the `I_digit` factor is independent by weak approximation.  The remaining finite object is one degree-2 projective packet, not a residue list.

---

## 13. Terminal certificate

```text
SOURCE_PACKET_MODULUS=m_src=M0*q^2
SOURCE_CLASS=0
SOURCE_LATTICE_IS_KERNEL_OR_COSET=KERNEL
SOURCE_QUOTIENT_CYCLIC=TRUE

Q0_DIMENSION=3
Q0_SIGNATURE=(2,1)
SPIN_Q0_TYPE=A1
SPIN_Q0_RATIONAL_SPLIT=CONDITIONAL_ON_ISOTROPY
INTEGRAL_SPIN_LATTICE=EVEN_CLIFFORD_ORDER_NORM_ONE_STABILIZER_OF_L0

COMPOSITE_MODULUS=m_src
PRIME_FACTORIZATION_USED=FALSE
SPIN_ORBIT_COUNT=UNCLASSIFIED_BAD_REDUCTION
SPIN_ACTION_TRANSITIVE=PARTIAL
ORBIT_INVARIANT=M0_RULING_IDEAL_PAIR_PLUS_q2_CONDUCTOR

RATIONAL_ISOTROPIC_BASEPOINT=WITNESS_DEPENDENT
VERONESE_DEGREE=2
INTEGRAL_PARAMETERIZATION=PROVED_PROJECTIVELY/PARTIAL_PRIMITIVE_CONTENT

q2_CONDUCTOR_PACKET=UNRESOLVED
V_DIVISIBLE_BY_q2_CAN_BE_FORCED_BY_SPIN_ACTION=UNRESOLVED
q2_PACKET_RETIRED=FALSE

M0_SOURCE_PACKET=UNRESOLVED
M0_PACKET_GROUP_THEOREM=SEMANTIC_BAD_REDUCTION_RULING_ORBIT_CLASSIFICATION
M0_PRIME_DECOMPOSITION_USED=FALSE

STRONG_APPROXIMATION_APPLICABLE=PARTIAL
EXPLICIT_P1_APPROXIMATION_USED=TRUE
CONGRUENCE_ARCHIMEDEAN_INDEPENDENCE=PROVED_CONDITIONAL_ON_FINITE_ADMISSIBILITY

FINITE_PACKET_VERDICT=UNRESOLVED_GROUP_THEOREM
FINITE_PACKET_AUTOMATIC_ON_AMBIENT_ISOTROPIC_LOCUS=UNRESOLVED
UNIQUE_MISSING_THEOREM=SEMANTIC_CONDUCTOR_RULING_LIFTING
J2_STATUS=OPEN
```

## 14. Strategic terminal statement

R19 rules out the most optimistic automaticity argument for a precise reason:

\[
\boxed{
\text{the source modulus }M_0\text{ is also a bad-reduction modulus of }Q_0.
}
\]

Therefore the cyclic defect is **not yet retired**, but it has been transformed from an abstract SNF packet into a single explicit geometric/group-theoretic object:

\[
\boxed{
\text{degenerate ruling ideal pair over }\mathbf Z/M_0
\quad\times\quad
\text{q}^2\text{ conductor quadratic section}
}
\]

pulled back to one degree-2 condition on `P1(Z/m_src)`.

The next round must not return to source algebra, residues, Pell, Gaussian/Hermitian theory, or prime localization.  The only justified target is the **Semantic Conductor–Ruling Lifting Theorem**.  If it proves the kernel orbit admissible, R14/R19 approximation immediately attaches the real digit shell and the entire R15–R19 finite-source route retires.  If it fails, the ruling/conductor invariant is the genuine global finite obstruction.

\[
\boxed{\mathbf{J2\ OPEN}.}
\]
