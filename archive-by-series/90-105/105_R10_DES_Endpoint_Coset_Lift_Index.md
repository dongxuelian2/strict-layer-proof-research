# 105-R10 — DES Endpoint Coset Lift Index × Coset-Wide Surplus Sign × Exact DES Quotient Selection

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R10  
**Frozen input:** 105-R1--R9  
**Single responsibility:** decide the DES endpoint coset lift index / surplus-sign gate, or reduce it to one exact quotient-residue membership statement.

---

## 1. Executive Verdict

R10 obtains a genuine additional compression, but it does **not** prove source-wide post-PSDG radial extinction and it does **not** construct a positive-lift witness.

The two main structural results are:

1. **R9 Bézout compression loses no endpoint-residue information.** For Face A, the simultaneous solution set of `(T2-D),(T2-P)` is exactly the solution set of the Bézout row `(T2)`. Hence the \(d_2^*\) lifts seen in R9 are genuine DES-compatible lifts, not an artifact of the gcd compression.
2. **The actual lift index has an exact source/DES quotient formula.** Keeping the integer quotient in the frozen DES transport gives
   \[
   Q_2^{\rm DES}
   =\frac{T_{2P}(\rho_2)-V}{(10b_1P_1)/d_2^*},
   \qquad
   \kappa_2^{10}=[Q_2^{\rm DES}]_{d_2^*},
   \]
   and on Face B
   \[
   Q_3^{\rm DES}
   =\frac{T_3(\rho_3)-V}{(10K_3)/d_3^*},
   \qquad
   \kappa_3^{10}=[Q_3^{\rm DES}]_{d_3^*}.
   \]
   Thus R10 does **not** need to reopen a generic multiplicative-order problem modulo \(C_i\).

On the frozen exact continuous census, both live profiles are already DES-coset-wide extinct:

- B: \(d_2^*=1\), \(\Sigma_{A,\max}^{\rm DES}=-1635\);
- E: \(d_2^*=2\), lifts \(\kappa_2\in\{0,1\}\), but even the best lift has
  \[
  \Sigma_A(1)=-348189<0.
  \]

Therefore E is now killed **before** actual power-of-ten selection; R9 only knew its actual lower lift failed.

The remaining source-wide unknown is a single explicit membership gate:

\[
\boxed{
[Q_i^{\rm DES}]_{d_i^*}\in\mathcal K_i^+\ ?
}
\]

for a post-PSDG profile whose DES coset is theoretically positive. No such profile occurs in the frozen exact continuous census, but no theorem yet excludes it globally.

Formal terminal verdict:

```text
R10_TERMINAL_VERDICT=R10_REDUCED_TO_SINGLE_EXACT_DES_QUOTIENT_THRESHOLD_GATE__BEZOUT_NO_INFORMATION_LOSS__FULL_DES_LIFT_SET_EXACT__LIFT_INDEX_SOURCE_FORMULA_PROVED__FROZEN_CONTINUOUS_CENSUS_COSET_WIDE_EXTINCT__NO_UNIVERSAL_EXTINCTION__NO_POSITIVE_LIFT_WITNESS
```

---

## 2. Frozen R1–R9 State

All R1–R9 architecture is frozen.

In particular R10 does not reopen:

- source affine section reconstruction;
- valuation atlas / broad \(2/5\)-adic refinement;
- fixed incidence / moving base;
- discriminant / square locus;
- PSDG / determinant packets / source \(g_1\) firewall;
- Smith redesign;
- DES redesign;
- interval architecture;
- broad endpoint-remainder distribution;
- generic multiplicative-order or Jacobsthal analysis.

The accepted input is:

\[
\boxed{\texttt{POST\_PSDG\_SOURCE\_FIBRE\_RANK=1}},
\]

with unique radial variable \(U\), two active faces, and R9's exact DES-to-endpoint transport.

---

## 3. Current First-Failure Gate

R9 ended at

\[
\boxed{
\texttt{DES\_TRANSPORTED\_ENDPOINT\_RESIDUE\_LIFT\_\_SURPLUS\_SIGN}.
}
\]

R10 refines this to:

\[
\boxed{
\textbf{DES endpoint quotient residue modulo }d_i^*
\quad\text{vs}\quad
\textbf{critical positive-lift threshold}.
}
\]

The endpoint remainder itself is no longer treated as a free residue modulo \(C_i\).

---

## 4. R9 DES Endpoint Transport Recap

Put

\[
G=10^g,\quad K=10^k,\quad X=10^{m_2},\quad Y=10^{n_3},
\]
\[
D=KP_1-Q_0,\qquad
H=b_2Q_0-b_1XD,
\]
\[
K_3=\frac{b_3(Q_0-P_3)}Y\in\mathbf Z,
\qquad
b_2P_2=GH+K_3.
\]

Also

\[
b_2P_2=VC_2,\qquad b_3P_3=VC_3.
\]

For Face A, with \(x_2=10^{n_2-1}=GKX/10\), R9 proved

\[
10b_1D\,x_2\equiv K(Gb_2Q_0+K_3)\pmod{C_2},
\tag{T2-D}
\]

\[
10b_1P_1\,x_2\equiv G(b_1X+b_2)Q_0+K_3\pmod{C_2}.
\tag{T2-P}
\]

With

\[
h=\gcd(P_1,Q_0)=\gcd(P_1,D),
\]

Bézout combination gives

\[
10b_1h\,x_2\equiv E_2\pmod{C_2}.
\tag{T2}
\]

Define

\[
d_2^*=\gcd(C_2,10b_1h),\qquad M_2=C_2/d_2^*,
\]

and the unique reduced residue

\[
x_2\equiv\rho_2\pmod{M_2},\qquad 0\le\rho_2<M_2.
\]

For Face B, with \(x_3=10^{n_3-1}\),

\[
10K_3x_3\equiv b_3Q_0\pmod{C_3},
\tag{T3}
\]

\[
d_3^*=\gcd(C_3,10K_3),\qquad M_3=C_3/d_3^*,
\]

\[
x_3\equiv\rho_3\pmod{M_3}.
\]

---

## 5. Bézout Compression Information-Loss Audit

### Theorem R10.1 — Pair/Bézout equality

Let

\[
a_1x\equiv e_1\pmod C,
\qquad
a_2x\equiv e_2\pmod C
\]

be a consistent pair. Put

\[
g_j=\gcd(C,a_j).
\]

Each individual congruence has \(g_j\) solutions modulo \(C\), forming one coset with step \(C/g_j\). Therefore their nonempty intersection is one coset with step

\[
\operatorname{lcm}(C/g_1,C/g_2)
=\frac{C}{\gcd(g_1,g_2)},
\]

and hence contains exactly

\[
\gcd(g_1,g_2)=\gcd(C,a_1,a_2)
\]

solutions modulo \(C\).

For Face A take

\[
a_1=10b_1D,\qquad a_2=10b_1P_1.
\]

Then

\[
\gcd(C_2,a_1,a_2)
=\gcd(C_2,10b_1\gcd(D,P_1))
=\gcd(C_2,10b_1h)
=d_2^*.
\]

Every pair solution satisfies the Bézout row. The Bézout row itself has exactly \(d_2^*\) solutions modulo \(C_2\). Since the pair set is a subset of a set with the same finite cardinality,

\[
\boxed{
\mathcal S_{\rm pair}=\mathcal S_{\rm Bezout}.
}
\]

Therefore

\[
\boxed{
\texttt{BEZOUT\_COMPRESSION\_INFORMATION\_LOSS=NO}.
}
\]

### Dependency identity

The two Face-A rows are also algebraically linked:

\[
K(10b_1P_1)-10b_1D=10b_1Q_0,
\]

and their right-hand sides differ by exactly

\[
KGb_1XQ_0=10b_1Q_0x_2.
\]

Thus they are not two unrelated independent modular measurements; the exact pair/Bézout theorem above identifies precisely how much information they jointly carry.

---

## 6. Full Pair-Congruence Solution Set

The preceding theorem gives the exact Face-A DES-compatible residue set:

\[
\boxed{
\mathcal S_2^{\rm DES}
=
\{\rho_2+\kappa M_2\pmod{C_2}:0\le\kappa<d_2^*\}.
}
\]

Equivalently,

\[
\boxed{
\mathcal K_2^{\rm DES}
=
\{0,1,\ldots,d_2^*-1\}.
}
\]

So the R9 upper bound on lift multiplicity is exact:

\[
\boxed{m_2^{\rm lift}=d_2^*.}
\]

For Face B there is one frozen transport row `(T3)`, whose consistent solution set already has exactly \(d_3^*\) residues modulo \(C_3\). Hence similarly

\[
\boxed{
\mathcal K_3^{\rm DES}
=
\{0,1,\ldots,d_3^*-1\},
\qquad
m_3^{\rm lift}=d_3^*.
}
\]

Thus Level 1 and Level 2 of the prompt coincide:

\[
\boxed{
\mathcal K_i^{\rm coarse}=\mathcal K_i^{\rm DES}.
}
\]

This is not failure of DES; it is the exact statement of the information content of the frozen rows.

---

## 7. Definition of \(d_i^*,M_i,\rho_i\)

Face A:

\[
\boxed{d_2^*=\gcd(C_2,10b_1h)},
\qquad
\boxed{M_2=C_2/d_2^*}.
\]

The reduced row has an invertible coefficient modulo \(M_2\), so \(\rho_2\) is uniquely determined in \([0,M_2)\).

Face B:

\[
\boxed{d_3^*=\gcd(C_3,10K_3)},
\qquad
\boxed{M_3=C_3/d_3^*},
\]

with unique \(\rho_3\in[0,M_3)\).

These are source-canonical at the frozen-profile level. On Face A, changing Bézout coefficients does not change the solution set by Theorem R10.1, hence cannot change \(M_2\) or the unique reduced class \(\rho_2\).

---

## 8. DES Endpoint Lift Index

Write

\[
x_i=\rho_i+M_iQ_i^{\rm DES}.
\]

Since \(C_i=d_i^*M_i\), Euclidean reduction modulo \(C_i\) gives

\[
r_i=\rho_i+M_i\kappa_i,
\]

where

\[
\boxed{
\kappa_i
=
[Q_i^{\rm DES}]_{d_i^*}
=
\left[
\frac{x_i-\rho_i}{M_i}
\right]_{d_i^*}.
}
\]

The numerator is divisible by \(M_i\) by construction of \(\rho_i\).

This observable is normalization-independent once the canonical representative \(0\le\rho_i<M_i\) is fixed.

---

## 9. Coarse Lift Set

The coarse set is

\[
\boxed{
\mathcal K_i^{\rm coarse}=
\{0,\ldots,d_i^*-1\}.
}
\]

No lift outside this finite set can occur because it would change the reduced residue modulo \(M_i\).

---

## 10. Full DES-Compatible Lift Set

By Section 6,

\[
\boxed{
\mathcal K_i^{\rm DES}
=
\mathcal K_i^{\rm coarse}.
}
\]

Therefore R10 does **not** obtain an additional narrowing merely by keeping both Face-A congruences. The remaining narrowing must come from the actual integer quotient / decimal endpoint, not from a hidden second modular row.

`FULL_DES_ENDPOINT_RESIDUE_RECOVERED` by congruences alone holds precisely on \(d_i^*=1\) strata. It does not hold source-wide because E has \(d_2^*=2\).

---

## 11. Source Prime Support of \(d_i^*\)

### Face A

The frozen Smith chart gives

\[
b_1=s\alpha u,
\qquad
b_2=s\alpha\beta t.
\]

Since \(\gcd(C_2,b_2)=1\), in particular \(\gcd(C_2,s\alpha)=1\). Therefore

\[
\boxed{
 d_2^*
 =\gcd(C_2,10b_1h)
 =\gcd(C_2,10uh).
}
\]

Hence

\[
\boxed{
\operatorname{supp}(d_2^*)
\subseteq
\{2,5\}\cup\operatorname{supp}(u)\cup\operatorname{supp}(h).
}
\]

Frozen R7 arithmetic gives: \(h\) is odd and every odd prime divisor of \(h\) is \(1\pmod4\).

In particular

\[
v_2(d_2^*)=\min\bigl(v_2(C_2),1+v_2(u)\bigr),
\]

\[
v_5(d_2^*)=\min\bigl(v_5(C_2),1+v_5(u)+v_5(h)\bigr).
\]

This is lift-index-local arithmetic, not a reopening of the old valuation architecture.

### Face B

From consistency of `(T3)`,

\[
d_3^*\mid b_3Q_0.
\]

Since \(\gcd(b_3,C_3)=1\) and \(d_3^*\mid C_3\),

\[
\boxed{d_3^*\mid Q_0.}
\]

Thus every prime \(p\mid d_3^*\) divides \(\gcd(C_3,Q_0)\). The frozen primitive-sphere gcd theorem implies such primes are odd and satisfy

\[
\boxed{p\equiv1\pmod4.}
\]

Consequently

\[
\boxed{v_2(d_3^*)=0.}
\]

The prime \(5\) is allowed because \(5\equiv1\pmod4\).

---

## 12. \(d_i^*\) Size / Bound Audit

A source-wide theorem \(d_i^*=1\) is false: profile E has

\[
\boxed{d_2^*=2}.
\]

No frozen theorem supplies an absolute source-wide constant \(D_0\) with \(d_i^*\le D_0\). The available statements only give profilewise finite bounds such as

\[
d_2^*\le 10|u h|,
\qquad
 d_3^*\le 10|K_3|,
\]

while \(u,h,K_3\) remain source-moving.

Therefore

```text
DSTAR_UNIFORMLY_ONE=NO
DSTAR_UNIFORMLY_BOUNDED=NOT_PROVED
```

The frozen four-profile Face-A census has \(d_2^*=1,1,1,2\), but this is finite evidence only.

---

## 13. Face A Surplus as Function of \(\kappa_2\)

Assume first \(\rho_2>0\). Then every lift has positive remainder

\[
r_2=\rho_2+\kappa_2M_2>0.
\]

Therefore

\[
\delta_2=C_2-r_2
=d_2^*M_2-\rho_2-\kappa_2M_2,
\]

and

\[
\boxed{
\Sigma_A(\kappa_2)
=G_A-C_3(d_2^*M_2-\rho_2-\kappa_2M_2).
}
\]

Equivalently

\[
\boxed{
\Sigma_A(\kappa_2)
=\Sigma_{A,0}+C_3M_2\kappa_2,
}
\]

where

\[
\Sigma_{A,0}=G_A-C_3(d_2^*M_2-\rho_2).
\]

---

## 14. Face B Surplus as Function of \(\kappa_3\)

For \(\rho_3>0\),

\[
\delta_3=d_3^*M_3-\rho_3-\kappa_3M_3,
\]

hence

\[
\boxed{
\Sigma_B(\kappa_3)
=G_B-C_2(d_3^*M_3-\rho_3-\kappa_3M_3)
}
\]

and

\[
\boxed{
\Sigma_B(\kappa_3)
=\Sigma_{B,0}+C_2M_3\kappa_3.
}
\]

---

## 15. Lift-Index Monotonicity Lemma

### Regular nonzero-residue regime

If \(\rho_i>0\), then

\[
\Sigma_i(\kappa+1)-\Sigma_i(\kappa)
=W_iM_i>0,
\]

where

\[
W_A=C_3,\qquad W_B=C_2.
\]

Thus

\[
\boxed{
\rho_i>0
\Longrightarrow
\Sigma_i(\kappa)\text{ strictly increases in }\kappa.
}
\]

### Necessary correction at \(\rho_i=0\)

The prompt's affine formula cannot be used at \(\kappa=0\) when \(\rho_i=0\), because then the actual remainder is \(r_i=0\) and the Euclidean successor jump is

\[
\delta_i=0,
\]

not \(C_i\).

Hence

\[
\boxed{\Sigma_i(0)=G_i.}
\]

For \(\kappa\ge1\), the affine formula resumes and is strictly increasing. Therefore the full sequence has a special zero-remainder branch at \(\kappa=0\); global monotonicity across \(0\to1\) must not be claimed.

This is an R10 boundary correction to the proposed monotonicity lemma.

---

## 16. Coset-Wide Best Surplus

If \(\rho_i>0\), strict monotonicity gives best lift

\[
\kappa_i=d_i^*-1,
\]

with

\[
r_{i,\max}=\rho_i+(d_i^*-1)M_i,
\]

\[
\delta_{i,\min}=M_i-\rho_i.
\]

Therefore

\[
\boxed{
\Sigma_{A,\max}^{\rm coset}
=G_A-C_3(M_2-\rho_2)
}
\]

and

\[
\boxed{
\Sigma_{B,\max}^{\rm coset}
=G_B-C_2(M_3-\rho_3).
}
\]

If \(\rho_i=0\), the best lift is automatically \(\kappa=0\) because

\[
\boxed{
\Sigma_{i,\max}^{\rm coset}=G_i>0
}
\]

on a continuous active face.

---

## 17. Coset-Wide Extinction Criterion

For \(\rho_2>0\), Face A is DES-coset-wide extinct if

\[
\boxed{
C_3(M_2-\rho_2)\ge G_A.
}
\]

For \(\rho_3>0\), Face B is extinct if

\[
\boxed{
C_2(M_3-\rho_3)\ge G_B.
}
\]

Because Section 6 proved \(\mathcal K_i^{\rm DES}=\mathcal K_i^{\rm coarse}\), these are not merely coarse-coset sufficient criteria: they are the exact **DES-wide** maximum tests for nonzero \(\rho_i\).

At \(\rho_i=0\), DES-wide extinction is impossible on a continuous face because \(\kappa=0\in\mathcal K_i^{\rm DES}\) yields positive surplus \(G_i\).

---

## 18. \(\rho_i=0\) Exceptional Regime

### Face A characterization

Let the two original right-hand sides be

\[
E_D=K(Gb_2Q_0+K_3),
\]

\[
E_P=G(b_1X+b_2)Q_0+K_3.
\]

Because the full pair set equals the Bézout set,

\[
\boxed{
\rho_2=0
\iff
C_2\mid E_D\ \text{and}\ C_2\mid E_P.
}
\]

Equivalently, for any valid Bézout combination \(E_2\),

\[
\boxed{\rho_2=0\iff C_2\mid E_2.}
\]

### Face B characterization

From `(T3)`,

\[
\rho_3=0
\iff
C_3\mid b_3Q_0.
\]

Since \(\gcd(b_3,C_3)=1\),

\[
\boxed{
\rho_3=0\iff C_3\mid Q_0.
}
\]

### Consequence

If \(\rho_i=0\) and the actual selector chooses \(\kappa_i^{10}=0\), then

\[
r_i=0,\qquad \delta_i=0,\qquad \Sigma_i=G_i>0.
\]

If additionally \(d_i^*=1\), \(\kappa=0\) is the only DES lift, so a continuous profile would automatically pass the plain radial gate.

No frozen exact post-PSDG profile A/B/C/E has \(\rho_2=0\), and no universal theorem excludes the regime.

---

## 19. Critical Lift Threshold

For \(\rho_i>0\), write \(W_A=C_3\), \(W_B=C_2\). Then

\[
\Sigma_i(\kappa)>0
\iff
W_i(d_i^*M_i-\rho_i-\kappa M_i)<G_i.
\]

Thus

\[
\kappa>
\frac{W_i(d_i^*M_i-\rho_i)-G_i}{W_iM_i}.
\]

The exact first integer lift is

\[
\boxed{
\kappa_{i,\rm crit}
=
\left\lfloor
\frac{W_i(d_i^*M_i-\rho_i)-G_i}{W_iM_i}
\right\rfloor+1.
}
\]

Interpretation:

- \(\kappa_{i,\rm crit}\ge d_i^*\): no positive lift;
- \(\kappa_{i,\rm crit}\le0\): all DES lifts positive;
- otherwise positive lifts begin at \(\kappa_{i,\rm crit}\).

For \(\rho_i=0\), \(\kappa=0\) must be treated separately and is always positive on a continuous face; the threshold formula applies only to \(\kappa\ge1\).

---

## 20. Positive Lift-Index Set

For \(\rho_i>0\), because full DES and coarse sets coincide,

\[
\boxed{
\mathcal K_i^+
=
\{\kappa\in\{0,\ldots,d_i^*-1\}:\kappa\ge\kappa_{i,\rm crit}\}.
}
\]

with the obvious clipping at \(0\) and \(d_i^*\).

For \(\rho_i=0\),

\[
\boxed{
0\in\mathcal K_i^+
}
\]

on every continuous face, and possible additional positive lifts \(\kappa\ge1\) are tested by their affine formula.

The actual plain gate is now exactly

\[
\boxed{
\kappa_i^{10}\in\mathcal K_i^+.
}
\]

---

## 21. DES Quotient \(Q_i^{\rm DES}\)

Define

\[
\boxed{
Q_i^{\rm DES}=\frac{x_i-\rho_i}{M_i}\in\mathbf Z.
}
\]

Then

\[
\boxed{
Q_i^{\rm DES}=d_i^*q_i+\kappa_i
}
\]

for the ordinary Euclidean quotient \(x_i=q_iC_i+r_i\). Hence

\[
\boxed{
\kappa_i=[Q_i^{\rm DES}]_{d_i^*}.
}
\]

The important R10 advance is that \(Q_i^{\rm DES}\) can be recovered from the **integer** DES transport without computing \(10^{n_i-1}\bmod C_i\) by a new orbit argument.

---

## 22. Actual Power10 Lift Selection

### Lemma R10.2 — Exact quotient recovery from an integer transport

Suppose

\[
Ax=E-\lambda C,
\qquad
C=dM,
\qquad
x=\rho+MQ,
\]

and \(\rho\) is a DES-compatible reduced representative so that

\[
T_\rho:=\frac{E-A\rho}{C}\in\mathbf Z.
\]

Then

\[
A(\rho+MQ)=E-\lambda dM.
\]

Subtract \(A\rho\) and divide by \(dM\):

\[
\boxed{
T_\rho=\lambda+\frac Ad Q.
}
\]

Therefore

\[
\boxed{
Q=\frac{T_\rho-\lambda}{A/d}.
}
\]

The divisibility of the numerator by \(A/d\) is a theorem, not an assumption.

### Face A

The exact `(T2-P)` identity is

\[
\boxed{
10b_1P_1x_2
=
E_P-VC_2,
}
\tag{I2-P}
\]

where

\[
E_P=G(b_1X+b_2)Q_0+K_3.
\]

Define

\[
T_{2P}(\rho_2)
:=
\frac{E_P-10b_1P_1\rho_2}{C_2}.
\]

Because \(\rho_2\) is in the full pair solution set, this is integral. Lemma R10.2 gives

\[
\boxed{
Q_2^{\rm DES}
=
\frac{T_{2P}(\rho_2)-V}{(10b_1P_1)/d_2^*}.
}
\tag{Q2}
\]

Hence

\[
\boxed{
\kappa_2^{10}
=
\left[
\frac{T_{2P}(\rho_2)-V}{(10b_1P_1)/d_2^*}
\right]_{d_2^*}.
}
\tag{K2}
\]

The `(T2-D)` exact identity gives the equivalent check

\[
Q_2^{\rm DES}
=
\frac{T_{2D}(\rho_2)-KV}{(10b_1D)/d_2^*}.
\]

### Face B

The exact `(T3)` identity is

\[
\boxed{
10K_3x_3=b_3Q_0-VC_3.
}
\tag{I3}
\]

Set

\[
T_3(\rho_3)
=
\frac{b_3Q_0-10K_3\rho_3}{C_3}.
\]

Then

\[
\boxed{
Q_3^{\rm DES}
=
\frac{T_3(\rho_3)-V}{(10K_3)/d_3^*},
}
\tag{Q3}
\]

\[
\boxed{
\kappa_3^{10}=[Q_3^{\rm DES}]_{d_3^*}.
}
\tag{K3}
\]

This proves an exact **DES Endpoint Lift-Index Rigidity formula**. It does not prove that the resulting \(\kappa_i\) has a source-wide constant value or sign.

---

## 23. Local / CRT Lift Components

Factor

\[
d_i^*=\prod p^{e_p}.
\]

The actual lift is now locally

\[
\boxed{
\kappa_i^{10}\equiv Q_i^{\rm DES}\pmod{p^{e_p}}.
}
\]

CRT reconstructs \(\kappa_i\) uniquely modulo \(d_i^*\).

Crucially this does not require dividing \(M_i\) modulo \(d_i^*\), so the possible coupling \(\gcd(M_i,d_i^*)>1\) is harmless at this stage. The exact integer quotient has already performed the division legitimately.

No generic multiplicative-order analysis is activated in R10.

---

## 24. Second-Order DES Transport

The lift index is the “second residue digit” above the reduced class \(\rho_i\). Lemma R10.2 shows that the relevant second-order information is not a blind lift from modulus \(M_i\) to \(C_i\), but the integer quotient carried by the exact DES identity:

\[
T_\rho-\lambda=\frac Ad Q_i^{\rm DES}.
\]

Thus the second-order transport object is

\[
\boxed{
T_\rho
=
\frac{E-A\rho}{C},
}
\]

not a generic modulus-\(C^2\) Hensel lift.

This is source-native and avoids an artificial modulus escalation.

---

## 25. Full Integer Transport Audit

The R9 congruences come from stronger exact identities:

### Face A, D-row

\[
\boxed{
10b_1D\,x_2
=
K(Gb_2Q_0+K_3)-KV C_2.
}
\tag{I2-D}
\]

### Face A, P-row

\[
\boxed{
10b_1P_1\,x_2
=
G(b_1X+b_2)Q_0+K_3-VC_2.
}
\tag{I2-P}
\]

### Face B

\[
\boxed{
10K_3x_3=b_3Q_0-VC_3.
}
\tag{I3}
\]

The coefficients of \(C_i\) are explicit integers \(-KV,-V,-V\). These quotient terms are exactly the data erased by reducing modulo \(C_i\), and they supply the quotient-recovery formulas of Section 22.

Thus R10's “second transport” is not a new DES equation; it is the retained integer part of the already frozen DES transport.

---

## 26. B/E Regression Fixtures

### B

Frozen data:

\[
C_2=109,\qquad C_3=25,
\]
\[
d_2^*=1,\qquad M_2=109,\qquad\rho_2=10.
\]

Thus

\[
\mathcal K_2^{\rm DES}=\{0\}.
\]

The exact quotient transport gives

\[
T_{2P}(10)=24=V,
\]

hence

\[
Q_2^{\rm DES}=0,
\qquad
\boxed{\kappa_2^{10}=0}.
\]

Actual remainder:

\[
r_2=10,
\]

and

\[
\boxed{\Sigma_A=-1635}.
\]

Since \(d_2^*=1\), this is already the coset maximum. Critical index:

\[
\boxed{\kappa_{A,\rm crit}=1>d_2^*-1=0}.
\]

Therefore B is DES-coset-wide extinct.

### E

Frozen data:

\[
C_2=2514,\qquad C_3=297,
\]
\[
d_2^*=2,\qquad M_2=1257,\qquad\rho_2=10.
\]

Full DES lifts:

\[
\boxed{\mathcal K_2^{\rm DES}=\{0,1\}},
\]

corresponding to

\[
r_2\in\{10,1267\}.
\]

The actual integer transport gives

\[
T_{2P}(10)=5=V,
\]

so

\[
Q_2^{\rm DES}=0,
\qquad
\boxed{\kappa_2^{10}=0}.
\]

This explains **why E chooses the lower lift**: not by a guessed parity/orbit heuristic, but because the exact DES quotient equals zero.

Actual surplus:

\[
\Sigma_A(0)=-721518.
\]

The best theoretical DES lift is \(\kappa=1\):

\[
\boxed{
\Sigma_A(1)
=22170-297(1257-10)
=-348189<0.
}
\]

Hence

\[
\boxed{\kappa_{A,\rm crit}=2=d_2^*},
\qquad
\boxed{\mathcal K_2^+=\varnothing}.
\]

This is a genuine R10 strengthening over R9: **the entire E DES coset is extinct.**

The equality \(T_{2P}(\rho)=V\) and hence \(Q=0\) also occurs in B, but R10 does not promote this finite-census pattern to a universal theorem.

---

## 27. Targeted Positive-Lift Search

R10 does not repeat R9's large parameter boxes. The lift-index-targeted checks are:

1. **\(\rho=0\) target:** none among frozen A/B/C/E; all Face-A \(\rho_2=10\).
2. **Maximal lift target:** B has no nontrivial lift; E's maximal \(\kappa=1\) still has \(-348189\) surplus.
3. **Threshold-near target:** B requires \(\kappa\ge1\) but only \(0\) exists; E requires \(\kappa\ge2\) but only \(0,1\) exist.
4. **Actual-positive target:** none in the frozen exact continuous census.

These are exact finite regressions, not a universal nonexistence theorem.

The first untested constructive regime remains a genuine post-PSDG profile with either

\[
\rho_i=0
\]

or, for \(\rho_i>0\),

\[
[Q_i^{\rm DES}]_{d_i^*}\ge\kappa_{i,\rm crit}.
\]

---

## 28. First Plain Positive Surplus

No new positive plain surplus is found.

```text
FIRST_POSITIVE_PLAIN_SURPLUS=NONE_IN_FROZEN_EXACT_CONTINUOUS_CENSUS
```

This cannot be upgraded to universal extinction.

---

## 29. Exact \(U\) Recovery

No active profile reaches \(\Sigma_i>0\), so no new integer successor lies inside the active upper endpoint.

Therefore R10 does not claim a new

\[
U=\operatorname{Succ}_{\mathbf Z}(L).
\]

For regression, B/E still have plain successor \(U=1\), but it lies outside their upper endpoints and is not a radial witness.

---

## 30. q=1 Progression Audit

No new plain hit reaches the q=1 affine-progression layer.

The endpoint lift-index observable is defined on each fixed post-PSDG profile before the downstream source progression is applied. The q=1 exceptional progression can change the source successor after a plain hit, but it does not alter the exact endpoint identity

\[
\kappa_i=[Q_i^{\rm DES}]_{d_i^*}.
\]

Therefore q=1 remains downstream in R10.

---

## 31. Coprimality Audit

Likewise, no new plain hit reaches

\[
\gcd(U,V)=1.
\]

Coprimality remains downstream and is not the current family-level first failure.

---

## 32. First Source Integer \(U\)

None is constructed in R10.

```text
SOURCE_INTEGER_U_FOUND=NO
SOURCE_INTEGER_U=NONE
```

---

## 33. Downstream Digit / Actual-Cut Audit

Because no source integer \(U\) is produced, R10 does not enter:

- post-radial digit synchronization;
- actual-cut exact gate;
- full-word legality;
- outer completion.

The R8/R9 digit windows remain frozen as the definitions of the radial interval, not as newly audited downstream words.

---

## 34. New First-Failure Gate

R10 retires two possible false interpretations:

1. there is no hidden information loss in R9 Bézout compression;
2. actual lift selection does not require a generic endpoint orbit modulo \(C_i\).

The exact remaining source-wide gate is

\[
\boxed{
\texttt{EXACT\_DES\_QUOTIENT\_MOD\_DSTAR
\_\_POSITIVE\_LIFT\_THRESHOLD\_MEMBERSHIP}.
}
\]

Face A:

\[
\boxed{
\left[
\frac{T_{2P}(\rho_2)-V}{(10b_1P_1)/d_2^*}
\right]_{d_2^*}
\in\mathcal K_2^+.
}
\]

Face B:

\[
\boxed{
\left[
\frac{T_3(\rho_3)-V}{(10K_3)/d_3^*}
\right]_{d_3^*}
\in\mathcal K_3^+.
}
\]

This is a single arithmetic membership problem, not a reopening of endpoint architecture.

---

## 35. Failed / Falsified Routes

1. **“Bézout compression created fake lifts.”** False. Pair set equals Bézout set exactly.
2. **“Two Face-A transports automatically recover the full residue.”** False source-wide; E retains two genuine DES-compatible lifts.
3. **“\(d_i^*=1\) universally.”** False; E has \(d_2^*=2\).
4. **“Frozen data prove a uniform small \(d_i^*\) bound.”** Not proved.
5. **“Surplus is globally affine/monotone in \(\kappa\) even at \(\rho=0\).”** False at \(\kappa=0\); zero remainder has \(\delta=0\).
6. **“E survives at the upper DES lift.”** False; \(\Sigma_A(1)=-348189\).
7. **“E's lower lift is explained by heuristic parity/distribution.”** Unnecessary; exact integer DES quotient gives \(Q_2^{\rm DES}=0\).
8. **Generic multiplicative order modulo \(C_i\).** Not needed after quotient recovery.
9. **Blind Hensel lift to modulus \(C_i^2\).** Not needed; integer quotient is source-native second-order data.
10. **q=1 progression / coprimality as current first failure.** Not reached.

---

## 36. Exact Remaining Unknowns

After R10, the remaining unknowns are subordinate to one gate:

1. Does there exist a genuine post-PSDG continuous profile with
   \[
   \Sigma_{i,\max}^{\rm DES}>0?
   \]
   The frozen continuous census has none.
2. In particular, can \(\rho_i=0\) occur on a genuine post-PSDG continuous profile?
3. If a theoretically positive DES coset exists, does its exact source quotient satisfy
   \[
   [Q_i^{\rm DES}]_{d_i^*}\in\mathcal K_i^+?
   \]
4. Can source provenance bound \(d_i^*\) more strongly than the current support theorem?

These are not four parallel architectures. They are inputs to one quotient-residue membership statement.

---

## 37. R10 Terminal Verdict

### Lift-Index Shock Checkpoint

**Q1. Did Bézout compression lose endpoint-residue information?**  
**NO.** Pair and Bézout solution sets are identical.

**Q2. Is \(\mathcal K_i^{\rm DES}\) exact?**  
**YES.** It equals \(\{0,\ldots,d_i^*-1\}\).

**Q3. What is the source prime support of \(d_i^*\)?**  
Face A: \(\{2,5\}\cup\operatorname{supp}(u)\cup\operatorname{supp}(h)\), with the \(h\)-part odd split. Face B: only odd split primes \(p\equiv1\pmod4\).

**Q4. Is \(d_i^*=1\) or uniformly bounded?**  
Uniform one is false; a uniform absolute bound is not proved.

**Q5. How many frozen continuous profiles are coset-wide extinct?**  
\(2/2\): B and E.

**Q6. Does a positive DES lift exist?**  
Not in the frozen continuous census. The \(\rho=0\) regime would produce one theoretically, but no genuine profile is known.

**Q7. Is the actual power10 lift canonical?**  
**YES.** It is recovered by the exact DES quotient formula.

**Q8. Is any frozen actual \(\kappa_i^{10}\) in a positive set?**  
**NO.** B/E positive sets are empty.

**Q9. Is a plain integer \(U\) obtained?**  
**NO new hit.**

**Q10. Did progression/coprimality become first failure?**  
**NO.** The family-level first failure remains the exact lift-index threshold membership gate.

### Terminal decision

R10 cannot honestly sign universal `EXTINCTION`, because B/E are a finite exact census and no theorem excludes a future theoretically positive DES coset. It also cannot sign `POSITIVE LIFT`.

The legally permitted partial success is therefore:

\[
\boxed{
\texttt{R10\_REDUCED\_TO\_SINGLE\_POWER10\_LIFT\_INDEX\_GATE=YES}.
}
\]

But the gate is now more precise than R9 anticipated: it is an **exact source quotient modulo \(d_i^*\)**, not a generic power-of-ten orbit problem.

---

## 38. R11 Authorization Decision

R11 is authorized only by the partial-success Route D.

\[
\boxed{
\textbf{R11 = Exact DES Quotient Residue}
\times
\textbf{Positive-Lift Threshold Membership}.
}
\]

R11 may only attack

\[
\boxed{
[Q_i^{\rm DES}]_{d_i^*}\in\mathcal K_i^+.
}
\]

The preferred order is:

1. source-wide elimination or construction of theoretically positive DES cosets;
2. first priority to \(\rho_i=0\);
3. only on surviving cosets, use the explicit quotient formula modulo \(d_i^*\);
4. if a positive actual lift is found, recover exact \(U\) and immediately move downstream.

R11 must not reopen broad endpoint residue, DES, PSDG, discriminant, Smith, or generic multiplicative-order architecture.

---

# Machine-readable Terminal Block

```text
R10_TERMINAL_VERDICT=R10_REDUCED_TO_SINGLE_EXACT_DES_QUOTIENT_THRESHOLD_GATE__BEZOUT_NO_INFORMATION_LOSS__FULL_DES_LIFT_SET_EXACT__LIFT_INDEX_SOURCE_FORMULA_PROVED__FROZEN_CONTINUOUS_CENSUS_COSET_WIDE_EXTINCT__NO_UNIVERSAL_EXTINCTION__NO_POSITIVE_LIFT_WITNESS

R1_TO_R9_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=DES_ENDPOINT_COSET_LIFT_INDEX__SURPLUS_SIGN

FACE_A_ACTIVE=YES__B_E_ARE_EXACT_CONTINUOUS_POST_PSDG_FACE_A_SURVIVORS
FACE_B_ACTIVE=THEORETICAL_FACE_FROZEN__NO_EXACT_CONTINUOUS_FACE_B_SURVIVOR_IN_CURRENT_CENSUS

T2_TRANSPORT_FROZEN=YES__T2_D__T2_P__T2_BEZOUT
T3_TRANSPORT_FROZEN=YES

BEZOUT_COMPRESSION_INFORMATION_LOSS=NO__PAIR_SOLUTION_SET_EQUALS_BEZOUT_SOLUTION_SET

D2_STAR=gcd(C2,10*b1*h)=gcd(C2,10*u*h)_USING_gcd(C2,s*alpha)=1
M2=C2/D2_STAR
RHO2=UNIQUE_REDUCED_DES_RESIDUE_IN_[0,M2)__RHO2_ZERO_IFF_C2_DIVIDES_BOTH_ORIGINAL_FACE_A_RHS
COARSE_K2_SET={0,...,D2_STAR-1}
FULL_DES_K2_SET=COARSE_K2_SET__EXACT

D3_STAR=gcd(C3,10*K3)__AND_D3_STAR_DIVIDES_Q0
M3=C3/D3_STAR
RHO3=UNIQUE_REDUCED_T3_RESIDUE__RHO3_ZERO_IFF_C3_DIVIDES_Q0
COARSE_K3_SET={0,...,D3_STAR-1}
FULL_DES_K3_SET=COARSE_K3_SET__EXACT

DSTAR_SOURCE_PRIME_SUPPORT=FACE_A:{2,5}_U_supp(u)_U_supp(h)_WITH_h_ODD_SPLIT__FACE_B:ODD_p_EQ_1_MOD_4_ONLY
DSTAR_UNIFORMLY_ONE=NO__E_HAS_D2_STAR_2
DSTAR_UNIFORMLY_BOUNDED=NOT_PROVED

RHO_ZERO_POSSIBLE=NOT_EXCLUDED_BY_FROZEN_THEOREMS__NONE_IN_FROZEN_A_B_C_E_FACE_A_CENSUS

COSET_MAX_REMAINDER=rho+(dstar-1)*M_FOR_rho_GT_0__RHO_ZERO_SPECIAL
COSET_MIN_JUMP=M-rho_FOR_rho_GT_0__ZERO_AT_kappa_0_IF_rho_ZERO

FACE_A_COSET_MAX_SURPLUS=G_A-C3*(M2-rho2)_IF_rho2_GT_0__G_A_IF_rho2_ZERO
FACE_B_COSET_MAX_SURPLUS=G_B-C2*(M3-rho3)_IF_rho3_GT_0__G_B_IF_rho3_ZERO

FACE_A_COSET_WIDE_EXTINCT=YES_FOR_FROZEN_CONTINUOUS_B_E__UNIVERSAL_NOT_PROVED
FACE_B_COSET_WIDE_EXTINCT=NO_ACTIVE_EXACT_PROFILE__UNIVERSAL_NOT_PROVED

K2_CRITICAL=floor((C3*(D2_STAR*M2-rho2)-G_A)/(C3*M2))+1_FOR_rho2_GT_0__RHO_ZERO_PIECEWISE
K3_CRITICAL=floor((C2*(D3_STAR*M3-rho3)-G_B)/(C2*M3))+1_FOR_rho3_GT_0__RHO_ZERO_PIECEWISE

POSITIVE_K2_SET=GENERAL:FULL_DES_K2_INTERSECT_[K2_CRITICAL,D2_STAR-1]_FOR_rho2_GT_0__RHO_ZERO_CONTAINS_0__B=EMPTY__E=EMPTY
POSITIVE_K3_SET=GENERAL_THRESHOLD_FORM__NO_ACTIVE_FACE_B_CENSUS_PROFILE

Q2_DES_QUOTIENT=(T2P(rho2)-V)/((10*b1*P1)/D2_STAR)__EQUIV_D_ROW_FORMULA
K2_POWER10_ACTUAL=[Q2_DES_QUOTIENT]_D2_STAR__B=0__E=0

Q3_DES_QUOTIENT=(T3(rho3)-V)/((10*K3)/D3_STAR)
K3_POWER10_ACTUAL=[Q3_DES_QUOTIENT]_D3_STAR

FULL_DES_ENDPOINT_RESIDUE_RECOVERED=NO_BY_CONGRUENCES_ALONE_SOURCE_WIDE__YES_ON_DSTAR_1_STRATA__PROFILEWISE_RECOVERABLE_AFTER_QUOTIENT_SELECTOR
LIFT_INDEX_RIGIDITY_PROVED=YES__EXACT_SOURCE_DES_QUOTIENT_FORMULA__NOT_A_SOURCE_WIDE_CONSTANT_SIGN

ACTUAL_PLAIN_SURPLUS=B:-1635__E:-721518__NO_POSITIVE_FROZEN_CONTINUOUS_PROFILE
PLAIN_INTEGER_RADIAL_GATE_PASSED=NO_NEW_HIT

PLAIN_U=NONE

Q1_AFFINE_PROGRESSION=DOWNSTREAM_NOT_REACHED_ON_NEW_HIT
COPRIMALITY_V=DOWNSTREAM_NOT_REACHED_ON_NEW_HIT
SOURCE_SELECTOR_PASS=NO_NEW_PLAIN_HIT_REACHES_SELECTOR

SOURCE_INTEGER_U_FOUND=NO
SOURCE_INTEGER_U=NONE

COMMON_U_INTEGER_SUCCESSOR_GATE=OPEN__REDUCED_TO_EXACT_DES_QUOTIENT_THRESHOLD_MEMBERSHIP

DIGIT_SYNCHRONIZATION=NOT_REACHED_AFTER_INTEGER_GATE
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

NEW_FIRST_FAILURE_GATE=EXACT_DES_QUOTIENT_MOD_DSTAR__POSITIVE_LIFT_THRESHOLD_MEMBERSHIP

POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NOT_PROVED

R10_SINGLE_POWER10_LIFT_INDEX_GATE=YES__NOW_SOURCE_NATIVE_EXACT_QUOTIENT_RESIDUE_GATE

R11_AUTHORIZED=YES
R11_ARCHITECTURE=ROUTE_D__EXACT_DES_QUOTIENT_RESIDUE_X_POSITIVE_LIFT_THRESHOLD
R11_SINGLE_ATTACK_TARGET=PROVE_SOURCE_WIDE_[Q_DES]_DSTAR_AVOIDS_POSITIVE_K_SET_OR_CONSTRUCT_FIRST_POST_PSDG_PROFILE_ENTERING_IT
```

---

## Companion artifacts

Generated with exact integer/Fraction arithmetic:

- `105_R10_DES_Pair_Congruence_Audit.csv`
- `105_R10_Lift_Index_Registry.csv`
- `105_R10_Coset_Surplus_Registry.csv`
- `105_R10_Dstar_Source_Support.csv`
- `105_R10_Critical_Kappa_Registry.csv`
- `105_R10_Power10_Lift_Selection.csv`
- `105_R10_Positive_Lift_Search.csv`
- `105_R10_First_Failure_Registry.csv`
- `105_R10_scripts/verify_r10_lift_index.py`
- `105_R10_scripts/verify_r10_lift_index.log`
- `105_R10_scripts/build_r10_artifacts.py`

The scripts treat the A/B/C/E post-PSDG states as frozen exact regression inputs and do not promote finite-census results to universal theorems.
