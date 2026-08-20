# J2-55-R13 — Independent Root Lowest-Coefficient × 2-Adic Reverse Constant × Gaussian Full Inert-Radical Report

**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第十三轮 / 统一终端线第二十三轮

# 1. Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

\[
\boxed{\delta>0:\ \textbf{OPEN}},\qquad
\boxed{\delta=0,q>1:\ \textbf{OPEN}},
\]

\[
\boxed{q=1\text{ reverse}:\ \textbf{OPEN}},\qquad
\boxed{\delta<0,q>1:\ \textbf{OPEN}}.
\]

The inherited \(q=1,\delta=0\) boundary closure is not reopened.

R13 does **not** introduce a fourth residual, a new root quotient, or a new carry quotient.  The frozen R12 verdict remains

\[
\boxed{\texttt{FULL\_ROOT\_MOD\_CARRY\_IDEAL=NONZERO}.}
\]

The independent objects remain \(P_B,P_H,P_R,P_{K1}\), of degrees \(4,4,7,7\).

---

# 2. Coefficient Verdict

```text
BOUNDARY_LOWEST_COEFF=B0 generically; B0=0 locus requires finite C1,...,C4 descent
HIGH_LOWEST_COEFF=H0 generically; H0=0 locus requires finite C1,...,C4 descent
REVERSE_LOWEST_COEFF=R0; q∤t => R0!=0 on the legal normalized branch
REVERSE_K1_LOWEST_COEFF=S0; q∤t => S0!=0 on the legal normalized branch

GAMMA_PARITY=OPEN
GAMMA_V2_BOUND=OPEN

V2_NEWTON_BOUNDARY=OPEN
V2_NEWTON_HIGH=OPEN
V2_NEWTON_REVERSE=NEW EXACT CONSTANT-TERM THEOREM FOR k>=5
```

For \(q=1\):

```text
FULL_INERT_RADICAL_THEOREM=PROVED
INERT_VALUATION_BUDGET=PROVED
FIRST_ORDER_SUPPORT_LIFT=PROVED
NEGATIVE_GAUSSIAN_BRANCH=OPEN
K10=OPEN
K100=OPEN
K1000=OPEN
```

---

# 3. LCR-1 — statewise lowest-coefficient divisibility

Let

\[
P(T)=C_0+C_1T+\cdots+C_dT^d\in\mathbf Z[T],
\qquad T=10^m,
\]

where the coefficients may depend on the actual state.  Put

\[
j_*:=\min\{j:C_j\ne0\}.
\]

If \(P(T)=0\), then

\[
0=T^{j_*}\left(C_{j_*}+C_{j_*+1}T+\cdots+C_dT^{d-j_*}\right).
\]

Since \(T\ne0\),

\[
C_{j_*}=-T\left(C_{j_*+1}+C_{j_*+2}T+\cdots\right),
\]

hence

\[
\boxed{10^m\mid C_{j_*}.}
\tag{LCR-1}
\]

No coefficient needs to be fixed as the exponent varies.  The theorem is pointwise on each actual state.  Therefore the R12 correction

\[
\text{periodic residue cell}\not\Rightarrow\text{fixed exact coefficients}
\]

remains true, but it does not obstruct lowest-coefficient descent.

The descent depth is at most four for boundary/high and seven for reverse; no residual ladder is created.

---

# 4. NEWT-1 — p-adic Newton minimum test

For \(p=2\) or \(5\), the terms of \(P(10^m)\) have valuations

\[
v_p(C_j)+jm.
\]

If the minimum of these values occurs at exactly one index, the sum cannot vanish.  Thus

\[
\boxed{
\#\arg\min_j\{v_p(C_j)+jm\}=1
\Longrightarrow P(10^m)\ne0.
}
\tag{NEWT-1}
\]

This is the correct global form of the proposed coefficient Newton test.

---

# 5. Structural homogeneity theorem

R12's reconstruction gives a useful exact simplification that does not require expanding all coefficients.

After the tail substitution, \(\alpha\) is linear in \((e,t)\).  Hence \(N,Z,a_3,X,D_2\) are linear in \((e,t)\), while \(F=A X^2+ZD_2\) is quadratic.  The carry equation is linear in the floor carry and solves that carry linearly in \((e,t,\gamma)\).  Substituting this solution into the deterministic root makes the root candidate linear in \((e,t,\gamma)\).  Consequently the exact root expression is homogeneous quadratic in these three variables.

Dividing only structural factors in \(G\) or \(R\) does not change that degree.  Therefore

```text
HOMOGENEITY_B=QUADRATIC_HOMOGENEOUS
HOMOGENEITY_H=QUADRATIC_HOMOGENEOUS
HOMOGENEITY_R=QUADRATIC_HOMOGENEOUS
HOMOGENEITY_K1=QUADRATIC_HOMOGENEOUS
```

Moreover the combination \(D_{\rm fl}s+\chi\) (or its reverse analogue) is what enters the carry equation.  Solving for \(\chi\) and substituting into \(x=(J-\chi)/D_{\rm fl}-s\) cancels \(s\).  Thus the carry-saturated independent root polynomial has no surviving \(s\)-dependence.

Since R8 proves \(t\) odd and in particular \(t\ne0\), it is legitimate for real/rational coefficient-cone analysis to set

\[
E=e/t,\qquad Y=\gamma/t,
\]

and divide \(P\) by \(t^2\).  These are analysis variables only, not new integer campaign coordinates.

---

# 6. Boundary / High constants

The R12 executed certificate already displays nonzero constant polynomials \(B_0\) and \(H_0\).  Both have an explicit outer factor

\[
-16f^3w
\]

and an inner homogeneous quadratic form in \((e,t,\gamma)\); in particular the observed monomial types are \(e^2,et,t^2,\gamma t\).

Thus the constant coefficient is genuinely independent full-root data, not the retired R11 carry constant.

However R13 did **not** obtain a uniform theorem of the form

\[
v_2(B_0)<g\quad\text{or}\quad v_2(H_0)<g
\]

on all actual moving states.  The inner quadratic form can have 2-adic cancellation, and the exact parity/excess information needed to control that cancellation is not present in the frozen R8–R12 package.

Accordingly neither boundary nor high is closed in this round.

---

# 7. Reverse generic constant — exact 2-adic theorem

R12 certifies

\[
R_0=\gamma\,\mathcal B,
\]

where

\[
\mathcal B=
-K^2\gamma(q+2)
-64Ke f^2q^3w
+256f^3q^4(q+4)tw.
\]

Here

\[
K=10^k,
\]

and \(q,f,w,q+4,t\) are odd.  Therefore the three summands have **exact** / lower valuations

\[
\boxed{
2k+v_2(\gamma),\qquad
6+k+v_2(e),\qquad
8.
}
\tag{RV2-1}
\]

The last value is exactly eight, not merely at least eight.

## 7.1 Generic bulk \(k\ge5\)

For \(k\ge5\),

\[
2k+v_2(\gamma)\ge10,
\qquad
6+k+v_2(e)\ge11,
\]

so the third summand is the unique 2-adic minimum.  Hence

\[
\boxed{v_2(\mathcal B)=8.}
\tag{RV2-2}
\]

If \(\gamma\ne0\),

\[
\boxed{v_2(R_0)=v_2(\gamma)+8.}
\tag{RV2-3}
\]

This is R13's main uniform coefficient-valuation theorem.

For an actual root with \(R_0\ne0\), LCR-1 gives \(10^r\mid R_0\), therefore

\[
\boxed{r\le v_2(\gamma)+8.}
\tag{REV-DEPTH}
\]

The infinite reverse-depth problem has therefore been reduced sharply to one missing quantity: an absolute bound on \(v_2(\gamma)\).

## 7.2 Why the round does not claim a depth collapse

The frozen reverse carry theorem proves the normalizing divisibility \(2^{k-2}\mid\Gamma_R\), but it does not prove that the normalized quotient \(\gamma\) is odd, nor any absolute excess bound.  Neither the R8 exact carry formula nor the R9 low-\(k\) residue package fixes this parity.

Therefore

\[
\boxed{\text{GAMMA-ODD is not proved.}}
\]

and no unconditional \(r\le r_0\) theorem is claimed.

---

# 8. Low-k exact conditional consequences

These are rigorous implications, but remain conditional on the unresolved parity audit.

### \(k=2\)

The bracket valuations are

\[
4+v_2(\gamma),\quad 8+v_2(e),\quad8.
\]

If \(\gamma\) is odd, the first term is the unique minimum, so

\[
v_2(\mathcal B)=4,
\qquad
v_2(R_0)=4,
\]

and hence \(r\le4\).

The cyclotomic condition then leaves

\[
(k,q)=(2,7):\quad r=1,
\]

\[
(k,q)=(2,11):\quad r\in\{1,3\}.
\]

### Special \(k=1,b=0\)

R12 gives

\[
S_0=\gamma\,[80eq^3+5\gamma(q+2)-32q^4(q+4)t].
\]

The bracket term valuations are

\[
4+v_2(e),\qquad v_2(\gamma),\qquad5.
\]

If \(\gamma\) is odd, the middle term is the unique odd term, so

\[
\boxed{v_2(S_0)=0.}
\]

But an actual reverse root has \(r\ge1\) and requires \(2^r\mid S_0\), contradiction.  Thus

\[
\boxed{\gamma\text{ odd}\Longrightarrow(k=1,b=0)\text{ CLOSED}.}
\]

The premise remains open; consequently the requested low-k type closure is not promoted to an unconditional theorem.

---

# 9. q=1 — full inert radical theorem

Freeze

\[
M_0L_0=Y_0^2+(S_Ga)^2,
\qquad
S_G=(G+1)(2G+3),
\]

and

\[
\gcd(M,a)=1.
\]

Let \(p\equiv3\pmod4\) be an odd prime dividing \(M_0\).  Then \(p\mid M\), hence \(p\nmid a\).  Reducing the Gaussian equation modulo \(p\), if \(p\nmid S_G\) one obtains

\[
\left(\frac{Y_0}{S_Ga}\right)^2\equiv-1\pmod p,
\]

impossible because \(-1\) is a nonresidue for \(p\equiv3\pmod4\).  Therefore

\[
\boxed{
 p\equiv3\pmod4,\ p\mid M_0
 \Longrightarrow p\mid S_G.
}
\tag{GS-1}
\]

Equivalently,

\[
\boxed{\operatorname{Rad}_{3\bmod4}(M_0)\mid S_G.}
\]

This upgrades R12's odd-valuation inert-kernel statement to the **full inert radical**.

---

# 10. q=1 — linear support partition

R12 gives

\[
M\equiv-(\tau+4a)\pmod{G+1},
\]

\[
8M\equiv-(27\tau+116a)\pmod{2G+3},
\]

and

\[
\gcd(G+1,2G+3)=1.
\]

Hence every \(3\bmod4\) prime dividing \(M_0\) must satisfy one of the two corresponding linear divisibilities.  Thus

\[
\boxed{
\operatorname{Rad}_{3\bmod4}(M_0)
\mid(\tau+4a)(27\tau+116a).
}
\tag{GS-2}
\]

The primitive relation gives

\[
\gcd(\tau+4a,27\tau+116a)=1,
\]

so these inert primes are genuinely partitioned between two coprime supports.

---

# 11. q=1 — inert valuation budget

For \(p\equiv3\pmod4\), the standard exact sum-of-two-squares valuation lemma is

\[
\boxed{
v_p(X^2+Y^2)=2\min(v_p(X),v_p(Y)).
}
\tag{INERT-V}
\]

Indeed after removing the common power of \(p\), an additional factor of \(p\) would produce a nontrivial square root of \(-1\) modulo \(p\).

Apply this to \(X=Y_0\), \(Y=S_Ga\).  For a prime dividing \(M_0\), primitive gcd gives \(p\nmid a\), so

\[
v_p(M_0)+v_p(L_0)
=2\min(v_p(Y_0),v_p(S_G))
\le2v_p(S_G).
\]

Therefore

\[
\boxed{v_p(M_0)\le2v_p(S_G)}
\]

for every inert prime, and hence

\[
\boxed{
\text{the entire }3\bmod4\text{ part of }M_0\text{ divides }S_G^2.
}
\tag{GS-VAL}
\]

This is stronger than radical control alone.

---

# 12. First-order support lift

Define

\[
U_1=\frac{M+\tau+4a}{G+1}
=G^2\tau-10Ga-G\tau+6a+\tau,
\]

\[
U_2=\frac{8M+27\tau+116a}{2G+3}
=4G^2\tau-40Ga-6G\tau+44a+9\tau.
\]

On an M-side inert support prime above \(G+1\), one has \(G\equiv-1\) and \(\tau\equiv-4a\), hence

\[
\boxed{U_1\equiv4a\not\equiv0\pmod p.}
\]

On a support prime above \(2G+3\),

\[
\boxed{U_2\equiv-12a\pmod p.}
\]

Here \(p=3\) cannot divide \(S_G\) because \(G=10^g\equiv1\pmod3\), so again this is a unit.

Thus outside the equal-valuation cancellation locus, the valuation of \(M\) is exactly the minimum of the support-factor valuation and the corresponding linear-form valuation.  The equal-valuation case is the remaining support-lift exceptional locus.

---

# 13. L-side external inert theorem

Let \(p\equiv3\pmod4\), \(p\mid L_0\), and \(p\nmid S_G\).  The Gaussian equation forces \(p\mid a\).  Since \(\gcd(M,a)=1\), \(p\nmid M\).  From

\[
GL=Q_K(G)M+4S_Ga
\]

modulo \(p\), one then obtains

\[
\boxed{p\mid Q_K(G).}
\]

Therefore

\[
\boxed{
 p\equiv3(4),\ p\mid L_0,\ p\nmid S_G
 \Longrightarrow p\mid\gcd(a,Q_K(G)).
}
\tag{GS-3}
\]

This is the asymmetric external-inert obstruction requested in R13.

---

# 14. q=1 sign branch

The R12 negative witnesses remain valid only against the pre-Gaussian ratio package; they are not Gaussian roots.  Adding the Gaussian equation gives the exact negative-branch inequality proposed in the prompt, but R13 does not derive a contradiction from it uniformly on the three ratio windows.

Hence

\[
\boxed{\text{NEGATIVE GAUSSIAN BRANCH: OPEN}.}
\]

Consequently no positive-factor Gaussian ideal allocation is used as if positivity had been proved.

---

# 15. Computation / coefficient-table audit

A mandatory lightweight analyzer was generated:

`J2-55-R13-RootCoefficient-symbolic.py`.

Its design is exactly the required one: it imports the four frozen R12 root factors and extracts every coefficient, factorization, dependency profile, and homogeneity flag without rebuilding a new residual chain.

In the present runtime, however, the R12 certificate is available as a File-Library source rather than as a mounted sandbox Python file.  A separate attempt to reproduce the full R12 heavy derivation from source again hit the same aggressive symbolic factorization bottleneck already recorded in R12.  Therefore the all-\(B_j,H_j,R_j,S_j\) table is **not falsely marked executed**.

`J2-55-R13-CoefficientProfile.tsv` records the recovered constant-coefficient layer and explicitly marks the unextracted entries.  Success A is therefore not claimed.

This computational limitation does not affect LCR-1, NEWT-1, the reverse constant valuation theorem, or the q=1 Gaussian theorems above; those use expressions already certified in R12.

---

# 16. Success audit

### Success A — complete coefficient table

\[
\boxed{\textbf{NOT ACHIEVED in this runtime}.}
\]

The correct direct-import analyzer is generated, but the frozen R12 source is not mounted locally and full from-source rerun is too heavy.

### Success B — uniform coefficient valuation theorem

\[
\boxed{\textbf{ACHIEVED}.}
\]

For generic reverse \(k\ge5\),

\[
\boxed{v_2(\mathcal B)=8},
\qquad
\boxed{v_2(R_0)=v_2(\gamma)+8\ (\gamma\ne0)}.
\]

### Success C — uniform reverse depth collapse

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

It has been reduced to the single missing excess bound \(v_2(\gamma)\le C\).

### Success D — low-k closure

\[
\boxed{\textbf{NOT ACHIEVED unconditionally}.}
\]

The exact conditional collapses under \(\gamma\) odd are recorded.

### Success E — boundary/high chamber closure

\[
\boxed{\textbf{NOT ACHIEVED}.}
\]

### Success F — strong Gaussian theorem

\[
\boxed{\textbf{ACHIEVED}.}
\]

R12 inert kernel is upgraded to full inert radical plus an exponent budget.

### Success G/H/I

No \(K\) is closed; q=1 and J2 remain OPEN.

---

# 17. Exact frontier after R13

R13 does **not** return merely “degree-4/7 polynomial remains.”  The lower-dimensional frontier is now:

### Generic reverse \(k\ge5\)

\[
\boxed{
P_R(10^r)=0,
\quad R_0\ne0
\Longrightarrow
r\le v_2(\gamma)+8.
}
\]

Thus the only missing globalization datum for constant-term depth is the normalized carry excess \(v_2(\gamma)\).

### Low-k

\[
\boxed{
(k=1,b=0):\ \gamma\text{ odd would close the branch immediately},
}
\]

\[
\boxed{
(k,q)=(2,7):\ \gamma\text{ odd}\Rightarrow r=1,
}
\]

\[
\boxed{
(k,q)=(2,11):\ \gamma\text{ odd}\Rightarrow r\in\{1,3\}.
}
\]

### q=1

\[
\boxed{
\operatorname{Rad}_{3\bmod4}(M_0)\mid S_G,
\qquad
(M_0)_{3\bmod4}\mid S_G^2,
}
\]

with all M-side inert primes partitioned between two coprime linear supports and with a first-order unit lift.  The remaining q=1 obstruction is therefore genuinely the split-prime Gaussian ideal allocation / equal-valuation support-cancellation problem, together with the still-open negative-sign branch.

---

# 18. Terminal statement

The intended strategic correction of R13 is valid:

\[
\boxed{
\text{moving coefficients do not block statewise lowest-coefficient divisibility.}
}
\]

The strongest new q>1 theorem is the exact \(k\ge5\) reverse bracket depth eight.  The strongest q=1 theorem is the upgrade from inert parity-kernel support to complete inert radical and exponent-budget support.

But the campaign has not yet proved

\[
J=2\Longrightarrow\varnothing.
\]

Therefore

\[
\boxed{\textbf{J2 OPEN}.}
\]
