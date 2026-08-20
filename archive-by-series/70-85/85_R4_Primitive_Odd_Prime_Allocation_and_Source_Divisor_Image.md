# 85 第四轮：Primitive Odd-Prime Factor Allocation × Forced Odd Divisor Discovery × Radial-Content Recovery × Source Divisor Image

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Round:** 85-R4  
**Primary target:** \(q>1,\ d_A=1\) regular branch  
**Completion criterion:** \(J=2\Longrightarrow\varnothing\)  
**Status:** **REGULAR J2 STILL OPEN**  
**R4 success level:** **R4-S1**  
**Terminal verdict:** `ODD_PRIME_ALLOCATION_ARCHITECTURE_FAILS`

---

# 1. Executive Summary

85-R4 does **not** close the regular \(J=2\) branch.

The round does, however, settle the proposed odd-prime allocation architecture decisively.

The main positive theorem is the completed primitive firewall:

\[
\boxed{
\gcd(C_1,d_2)
=
\gcd(C_1,\lambda^\flat)
=
\gcd(\lambda^\flat,d_2)
=1,
}
\]

together with

\[
\boxed{
\gcd(C_1,u)
=
\gcd(\lambda^\flat,u)
=
\gcd(d_2,u)
=1,
}
\]

and the regular \(A\)-relations

\[
\boxed{
\gcd(\lambda^\flat,A)
=
\gcd(d_2,A)
=
\gcd(u,A)
=1.
}
\]

The only unresolved pair among

\[
C_1,\ \lambda^\flat,\ d_2,\ u,\ A
\]

is

\[
\boxed{
\gcd(C_1,A)=\gcd(z,A),
}
\]

which is not known to be \(1\) globally.

More importantly, the highest-priority divisor candidate \(d_2\) behaves in the **opposite** way from the desired load mechanism.

Define the primitive normalized root product

\[
\boxed{
\Omega^\flat:=\frac{\Omega}{\mathcal U^2}.
}
\]

Then the radial source formula gives

\[
\boxed{
\Omega^\flat
=
\frac{Aw^2+zd_2}{2K}
\in\mathbf Z.
}
\]

Using the sphere identity

\[
H^2C_1^2+w^2=T d_2
\]

and

\[
H^2=2KM,
\]

one gets

\[
\boxed{
\Omega^\flat
\equiv
-AMC_1^2
\pmod{d_2}.
}
\]

Since

\[
\gcd(AMC_1,d_2)=1,
\]

this yields the **Sphere Anti-Transfer Theorem**

\[
\boxed{
\gcd(\Omega^\flat,d_2)=1.
}
\]

Thus no prime dividing \(d_2\) can enter the primitive root product at all.

In particular, the proposed theorem

\[
\operatorname{odd}(d_2)\mid\Omega^\flat
\]

is not merely unproved: for \(d_2>1\) it is impossible.

The sphere identity also gives the expected quadratic-residue information. For every prime

\[
p\mid d_2,
\]

one has

\[
-1
\]

a quadratic residue modulo \(p\), hence

\[
\boxed{p\equiv1\pmod4.}
\]

But this Gaussian splitting information is useless for allocation, because the same prime is already excluded from \(\Omega^\flat\).

Even more decisively, the sphere-to-root transfer is information-redundant. The inherited third Euclidean identity is

\[
\boxed{
2uKC_1=AT+z.
}
\]

Then

\[
\begin{aligned}
2K\Omega^\flat
&=Aw^2+zd_2\\
&=A(Td_2-H^2C_1^2)+zd_2\\
&=(AT+z)d_2-AH^2C_1^2\\
&=2uKC_1d_2-2KAMC_1^2\\
&=2KC_1(ud_2-AMC_1).
\end{aligned}
\]

Therefore

\[
\boxed{
\Omega^\flat=C_1\lambda^\flat
}
\]

with

\[
\lambda^\flat=ud_2-AMC_1.
\]

So the sphere relation does not provide a second divisor constraint against the root factorization; after the exact source linear identities are retained, it reconstructs that factorization.

The decimal-linear identity

\[
GKC_1=AC_2+m
\]

does not produce a nontrivial divisor load either. Its odd-prime content is a congruence

\[
GKC_1\equiv AC_2+m\pmod p,
\]

not a divisibility statement. The source coordinate \(m\) is a positive ten-unit derived coordinate, not a uniformly smaller Euclidean remainder whose odd part must divide the root product.

The cyclotomic candidate \(u\) behaves like \(d_2\): it is explicitly excluded,

\[
\boxed{
\gcd(\Omega^\flat,u)=1.
}
\]

For \(A\), the exact orientation is

\[
\boxed{
\gcd(\Omega^\flat,A)
=
\gcd(C_1,A)
=
\gcd(z,A),
}
\]

because the complementary factor is an \(A\)-unit. Hence any \(A\)-prime occurring in the root product is allowed to sit entirely in the \(C_1\)-side; no nontrivial \(A\)-part is source-forced.

Finally, radial-content recovery is exact but does not create an extra odd load:

\[
\boxed{
\Omega=\mathcal U^2\Omega^\flat
}
\]

already follows from the source formula before the exact-root equality is used. Hence for any odd prime \(p\mid\mathcal U\),

\[
\boxed{
v_p(\Omega)
=
2v_p(\mathcal U)+v_p(\Omega^\flat).
}
\]

The excess term is exactly the primitive product content; R4 finds no source theorem forcing it to be positive.

Therefore after auditing the three permitted structural sources

1. sphere/radial \(d_2,T,w\);
2. decimal-linear \(m,A,C_2\);
3. cyclotomic/radial-content \(u,q,G+1,\mathcal U\);

there is no nontrivial composite

\[
D_{\rm source}>1
\]

for which R4 can prove

\[
D_{\rm source}\mid\Omega^\flat.
\]

By the explicit R4 kill criterion,

```text
FORCED_ODD_DIVISOR_DISCOVERY=FAILED
ODD_FACTOR_ALLOCATION=NOT_REACHED
ODD_PRIME_ALLOCATION_ARCHITECTURE=RETIRED
```

and no further prime-by-prime expansion is permitted.

---

# 2. R3 Frozen Terminal State

85-R3 is accepted without reopening source-cut, carry, floor, \(2/5\)-capacity, or one-quantum architecture.

The frozen regular state is

\[
\boxed{
q>1,\qquad d_A=1,
}
\]

with all three regular tail chambers still open:

\[
\delta>0,\qquad
\delta=0,\qquad
\delta<0.
\]

The source-selected root is

\[
\boxed{x_*=a_1}.
\]

Define

\[
\lambda_*
=
uD_2-AMx_*.
\]

Under an exact root,

\[
\boxed{
\Omega=x_*\lambda_*.
}
\]

The radial decomposition is

\[
\boxed{
x_*=\mathcal U C_1,
\qquad
D_2=\mathcal U d_2,
\qquad
\lambda_*=\mathcal U\lambda^\flat.
}
\]

Therefore

\[
\boxed{
\lambda^\flat=ud_2-AMC_1
}
\]

and, under exact root,

\[
\boxed{
\Omega
=
\mathcal U^2C_1\lambda^\flat.
}
\]

R3 proved

\[
\boxed{
\gcd(C_1,d_2)=1,
}
\]

\[
\boxed{
\gcd(C_1,\lambda^\flat)=1,
}
\]

\[
\boxed{
\gcd(C_1,u)=1,
\qquad
\gcd(\lambda^\flat,u)=1.
}
\]

It also proved the exact common-content theorem

\[
\gcd(x_*,D_2)
=
\gcd(x_*,\lambda_*)
=
\mathcal U.
\]

The current live negative J2 source chart contains

\[
\boxed{
H^2C_1^2+w^2=T d_2,
}
\tag{S}
\]

\[
\boxed{
GKC_1=AC_2+m,
}
\tag{L}
\]

with

\[
\gcd(mTw d_2,10)=1,
\]

and the third Euclidean identity

\[
\boxed{
2uKC_1=AT+z.
}
\tag{E}
\]

The decimal scale is

\[
M=L/8
\]

and

\[
\boxed{
H^2=2KM.
}
\tag{HKM}
\]

---

# 3. Regular Root-Factor Package

The regular root polynomial is

\[
\mathscr R(x)
=
AMx^2-uD_2x+\Omega.
\]

For the canonical root candidate \(x_*\),

\[
\mathscr R(x_*)
=
A^3uM\,\varepsilon_*,
\qquad
\varepsilon_*\in\mathbf Z.
\]

Thus a genuine regular source solution requires

\[
\boxed{\varepsilon_*=0}.
\]

Equivalently,

\[
\Omega=x_*\lambda_*.
\]

After radial decontenting,

\[
x_*=\mathcal U C_1,
\qquad
\lambda_*=\mathcal U\lambda^\flat,
\]

so

\[
\boxed{
\Omega^\flat
:=
\frac{\Omega}{\mathcal U^2}
=
C_1\lambda^\flat
}
\tag{PRIM-ROOT}
\]

on an exact root.

The R4 question is whether an independent source divisor must enter the right-hand side but is forbidden from both primitive factors.

---

# 4. Radial Decontenting

The common radial scale satisfies

\[
\gcd(\mathcal U,uGH)=1.
\]

Hence

\[
\boxed{
\gcd(\mathcal U,10)=1,
\qquad
\gcd(\mathcal U,2K)=1.
}
\]

Write the primitive signed source coordinates as

\[
\mathcal X=\mathcal U w,
\qquad
Z=\mathcal U z,
\qquad
D_2=\mathcal U d_2
\]

in the live negative branch.

Then

\[
\widetilde F
=
A\mathcal X^2+ZD_2
=
\mathcal U^2(Aw^2+zd_2).
\]

DCDC gives

\[
2K\mid\widetilde F.
\]

Since

\[
\gcd(\mathcal U^2,2K)=1,
\]

Euclid's lemma gives

\[
\boxed{
2K\mid Aw^2+zd_2.
}
\]

Therefore

\[
\boxed{
\Omega^\flat
=
\frac{Aw^2+zd_2}{2K}
\in\mathbf Z,
}
\tag{RDC}
\]

and

\[
\boxed{
\Omega
=
\mathcal U^2\Omega^\flat
}
\tag{U2-EXACT}
\]

already at the source/DCDC level.

This is stronger than merely reading \(\mathcal U^2\) from an assumed root factorization.

---

# 5. Primitive Firewall Ledger

The R4 firewall is:

| pair | status | proof/source |
|---|---|---|
| \((C_1,d_2)\) | \(1\) | R3 primitive decontenting |
| \((C_1,\lambda^\flat)\) | \(1\) | R3 canonical radial overlap |
| \((\lambda^\flat,d_2)\) | \(1\) | R4-P4 below |
| \((C_1,u)\) | \(1\) | primitive sphere/source gcd |
| \((\lambda^\flat,u)\) | \(1\) | R3 PN-2 after decontenting |
| \((d_2,u)\) | \(1\) | frozen \(d_2\equiv-z/2\pmod u\), \((z,u)=1\) |
| \((u,A)\) | \(1\) | \(A=2u+1\) |
| \((d_2,A)\) | \(1\) | regular \(d_A=(A,D_2)=1\) |
| \((\lambda^\flat,A)\) | \(1\) | \(\lambda^\flat\equiv ud_2\pmod A\) |
| \((C_1,A)\) | **not globally \(1\)** | exactly \((C_1,A)=(z,A)\) |

Additional support facts are

\[
\gcd(d_2,M)=1,
\qquad
\gcd(\lambda^\flat,M)=1,
\qquad
\gcd(u,M)=1,
\qquad
\gcd(A,M)=1,
\]

because \(M\) has only \(2,5\)-support and all four displayed quantities are ten-units.

Thus the primitive firewall is complete except for the deliberately allowed \(C_1\)-\(A\) overlap.

---

# 6. Proof of \(\gcd(\lambda^\flat,d_2)=1\)

We have

\[
\lambda^\flat
=
ud_2-AMC_1.
\]

Hence

\[
\gcd(\lambda^\flat,d_2)
=
\gcd(AMC_1,d_2).
\]

Now:

1. regularity gives
   \[
   \gcd(A,D_2)=1;
   \]
   since \(D_2=\mathcal U d_2\),
   \[
   \boxed{\gcd(A,d_2)=1};
   \]

2. \(d_2\) is a ten-unit and \(M\) has only \(2,5\)-support, so
   \[
   \boxed{\gcd(M,d_2)=1};
   \]

3. R3 gives
   \[
   \boxed{\gcd(C_1,d_2)=1}.
   \]

Therefore

\[
\boxed{
\gcd(AMC_1,d_2)=1,
}
\]

hence

\[
\boxed{
\gcd(\lambda^\flat,d_2)=1.
}
\tag{P4}
\]

This attains R4-S1.

---

# 7. Sphere / Radial Odd-Divisor Audit

## 7.1 Prime propagation from \(p\mid d_2\)

Let \(p\mid d_2\) be prime.

Since \(d_2\) is a ten-unit,

\[
p\ne2,5.
\]

By

\[
\gcd(C_1,d_2)=1,
\]

we have \(p\nmid C_1\). Also \(p\nmid H\).

Reducing

\[
H^2C_1^2+w^2=T d_2
\]

modulo \(p\),

\[
w^2
\equiv
-H^2C_1^2
\pmod p.
\]

If \(p\mid w\), then \(p\mid HC_1\), impossible. Thus \(w\) is also a unit mod \(p\), and

\[
\left(\frac{w}{HC_1}\right)^2
\equiv
-1
\pmod p.
\]

Therefore

\[
\boxed{
-1\text{ is a quadratic residue mod }p,
}
\]

and hence

\[
\boxed{
p\equiv1\pmod4.
}
\tag{D2-QR}
\]

Consequently

\[
\boxed{
\gcd(w,d_2)=1.
}
\]

This is a genuine odd-prime structural theorem, but it will not produce allocation load.

---

## 7.2 Sphere Anti-Transfer Theorem

From radial decontenting,

\[
2K\Omega^\flat
=
Aw^2+zd_2.
\]

Modulo \(d_2\),

\[
2K\Omega^\flat
\equiv
Aw^2
\pmod{d_2}.
\]

By the sphere equation,

\[
w^2
\equiv
-H^2C_1^2
\pmod{d_2}.
\]

Therefore

\[
2K\Omega^\flat
\equiv
-AH^2C_1^2
\pmod{d_2}.
\]

Using

\[
H^2=2KM,
\]

\[
2K\Omega^\flat
\equiv
-2KAMC_1^2
\pmod{d_2}.
\]

Because \(d_2\) is a ten-unit,

\[
\gcd(2K,d_2)=1.
\]

Cancel \(2K\):

\[
\boxed{
\Omega^\flat
\equiv
-AMC_1^2
\pmod{d_2}.
}
\tag{D2-ANTI}
\]

The right-hand side is a unit modulo \(d_2\). Hence

\[
\boxed{
\gcd(\Omega^\flat,d_2)=1.
}
\tag{D2-ANTI-GCD}
\]

This directly destroys the intended D2-LOAD architecture.

For \(d_2>1\),

\[
\boxed{
d_2\nmid\Omega^\flat.
}
\]

Since \(d_2\) is already odd and coprime to \(5\),

\[
\operatorname{odd}(d_2)=d_2,
\]

so also

\[
\boxed{
\operatorname{odd}(d_2)\nmid\Omega^\flat
\qquad(d_2>1).
}
\]

Thus the first ideal R4 theorem has the wrong sign: sphere gives **anti-transfer**, not transfer.

---

## 7.3 Sphere-to-root dependency collapse

Use the exact third Euclidean identity

\[
2uKC_1=AT+z.
\]

Then

\[
\begin{aligned}
2K\Omega^\flat
&=Aw^2+zd_2\\
&=A(Td_2-H^2C_1^2)+zd_2\\
&=(AT+z)d_2-AH^2C_1^2\\
&=2uKC_1d_2-2KAMC_1^2\\
&=2KC_1(ud_2-AMC_1).
\end{aligned}
\]

Hence

\[
\boxed{
\Omega^\flat
=
C_1(ud_2-AMC_1)
=
C_1\lambda^\flat.
}
\tag{SPHERE-ROOT}
\]

This is the crucial dependency theorem of R4:

\[
\boxed{
\text{sphere + third Euclidean identity}
\Longrightarrow
\text{the primitive root factorization itself}.
}
\]

Therefore the sphere cannot be counted as a second independent divisor source against the same factorization.

---

## 7.4 \(T\)-audit

The sphere identity does not force \(T\mid\Omega^\flat\).

Modulo \(T\),

\[
w^2\equiv-H^2C_1^2.
\]

Also

\[
z\equiv2uKC_1\pmod T
\]

from \(2uKC_1=AT+z\).

Thus

\[
\begin{aligned}
2K\Omega^\flat
&\equiv
-AH^2C_1^2+2uKC_1d_2\\
&=
2KC_1(ud_2-AMC_1)
\pmod T.
\end{aligned}
\]

That is exactly the root identity modulo \(T\), not a zero residue.

So

```text
T_TO_ROOT_DIVISOR_TRANSFER=NO_INDEPENDENT_LOAD
```

and no prime factorization of \(T\) is opened.

---

# 8. Decimal Linear Identity Audit

The exact primitive decimal-linear identity is

\[
\boxed{
GKC_1=AC_2+m.
}
\]

Because \(GK\) has only \(2,5\)-support, for every odd prime \(p\ne5\),

\[
\boxed{
C_1
\equiv
(GK)^{-1}(AC_2+m)
\pmod p.
}
\]

This is an additive congruence, not a divisor transfer.

In particular, if

\[
p\mid m,
\]

then

\[
GKC_1\equiv AC_2\pmod p.
\]

This does **not** force

\[
p\mid C_1
\]

and does **not** force

\[
p\mid AC_2.
\]

Both sides may simply be nonzero equal residues modulo \(p\).

Hence the implication schema

\[
p\mid m
\Longrightarrow
p\mid C_1
\]

fails already at the exact linear-algebra level; one would need a further independent source theorem.

---

## 8.1 Exact source meaning of \(m\)

The primitive \(c,z\) chart gives

\[
\boxed{
m=Ah-Gz,
}
\]

with \(m>0\) and

\[
\gcd(m,10)=1.
\]

Equivalently, in the radialized RCE coordinates the corresponding source coordinate is reconstructed by

\[
\boxed{
m_{\rm RCE}
=
\frac{AN+(q+2)Z}{2}.
}
\]

Thus \(m\) is not an anonymous free integer.

But it is also not a source remainder with a theorem of the form

\[
0<m<D_{\rm source}
\]

for some candidate odd divisor \(D_{\rm source}\) that would force Euclidean nonabsorption.

The historical narrow-\(r\) analysis already showed that treating \(m\) as intrinsically small is not legitimate; after the \(c,z\) compression it is a derived coordinate, not an independent “small carry”.

Therefore no \(m\)-based odd divisor is promoted.

---

## 8.2 Root product modulo \(m\)

Using

\[
d_2=mH-r,
\]

one has

\[
\lambda^\flat
=
u(mH-r)-AMC_1.
\]

Hence

\[
\boxed{
\Omega^\flat
=
C_1\lambda^\flat
\equiv
-C_1(ur+AMC_1)
\pmod m.
}
\tag{M-ROOT}
\]

No frozen source identity forces

\[
ur+AMC_1\equiv0\pmod m.
\]

Thus the exact \(m\)-residue is not a divisor law.

So

```text
M_ODD_DIVISOR_SOURCE=NO_USABLE_LOAD
```

---

# 9. Cyclotomic Secondary Audit

The cyclotomic identity is

\[
uq=G+1.
\]

R4 does not reopen any prime-by-prime analysis of \(q\) or \(G+1\).

The only guaranteed nontrivial odd divisor in this family is \(u>1\) in the current live chamber.

But R3 gives

\[
\gcd(C_1,u)=1,
\qquad
\gcd(\lambda^\flat,u)=1.
\]

Therefore, under exact root,

\[
\boxed{
\gcd(\Omega^\flat,u)=1.
}
\tag{U-ANTI}
\]

Thus \(u\) is another **forbidden** odd source divisor, not a forced load.

If some genuinely independent source theorem had implied

\[
p\mid u,\qquad p\mid\Omega^\flat,
\]

closure would have been immediate. R4 finds no such theorem; the existing source identities instead prove the opposite gcd.

Hence

```text
CYCLOTOMIC_ODD_LOAD=NOT_PRESENT
```

and the cyclotomic audit terminates without classifying primes of \(q\).

---

# 10. \(A\)-orientation audit

Regularity gives

\[
\gcd(\lambda^\flat,A)=1.
\]

Therefore

\[
\gcd(\Omega^\flat,A)
=
\gcd(C_1,A).
\]

The primitive \(A\)-root is

\[
KC_1\equiv-z\pmod A,
\]

because the radial scale \(\mathcal U\) is an \(A\)-unit and can be cancelled from the radialized \(A\)-root.

Since

\[
\gcd(K,A)=1,
\]

\[
\boxed{
\gcd(C_1,A)=\gcd(z,A).
}
\]

Hence

\[
\boxed{
\gcd(\Omega^\flat,A)
=
\gcd(z,A).
}
\tag{A-ORIENT}
\]

This gives an exact orientation law:

- any \(A\)-prime in the primitive root product must lie in \(C_1\);
- none may lie in \(\lambda^\flat\);
- but there is no global theorem that a nontrivial \(A\)-prime must occur.

Therefore \(A\) has orientation but no forced load.

---

# 11. Radial-Content Recovery

From Section 4,

\[
\boxed{
\Omega
=
\mathcal U^2\Omega^\flat
}
\]

is an exact source/DCDC identity.

Let \(p\mid\mathcal U\) be an odd prime. Since \(\mathcal U\) is a ten-unit,

\[
p\ne2,5.
\]

Then

\[
\boxed{
v_p(\Omega)
=
2v_p(\mathcal U)
+
v_p(\Omega^\flat).
}
\tag{U-DEPTH}
\]

Thus the prompt's possible extra depth is

\[
\eta_p=v_p(\Omega^\flat).
\]

R4 cannot prove

\[
\eta_p>0
\]

for all \(p\mid\mathcal U\), or for any source-forced nontrivial subset of such primes.

Under an exact root,

\[
\Omega^\flat=C_1\lambda^\flat
\]

with

\[
\gcd(C_1,\lambda^\flat)=1.
\]

Therefore an odd \(p\mid\mathcal U\), if it reappears after decontenting, can occur in at most one primitive root factor. But R3's maximal common-content theorem does not forbid such one-sided reappearance.

Hence radial-content recovery yields:

\[
\boxed{
\text{exact } \mathcal U^2\text{ extraction},
}
\]

but not

\[
\boxed{
\text{forced extra odd load after extraction}.
}
\]

So

```text
RADIAL_CONTENT_EXTRA_ODD_LOAD=NOT_FORCED
```

---

# 12. Source Divisor Image Search

R4 sought a nontrivial composite

\[
D_{\rm source}>1
\]

such that

\[
D_{\rm source}\mid\Omega^\flat.
\]

No such uniform source divisor is obtained from the permitted three source classes.

Instead, the strongest uniform composite theorem is an exclusion theorem:

\[
\boxed{
\gcd(\Omega^\flat,ud_2)=1.
}
\tag{ANTI-IMAGE}
\]

Indeed,

\[
\gcd(\Omega^\flat,u)=1
\]

and

\[
\gcd(\Omega^\flat,d_2)=1.
\]

For \(A\),

\[
\gcd(\Omega^\flat,A)=\gcd(z,A)
\]

is variable and may be \(1\).

For \(m\) and \(T\), no divisibility law is obtained.

Therefore the requested positive source divisor image

\[
\mathcal D_{\rm source}
\]

is empty at the current theorem level.

It is useful to record the result as

\[
\boxed{
\mathcal D_{\rm source}^{\rm forced\ load}=1.
}
\]

This notation does **not** assert that \(\Omega^\flat=1\); it asserts that among the audited source-divisor mechanisms, no nontrivial uniform divisor is proved to be forced into \(\Omega^\flat\).

---

# 13. Odd Divisor Ledger

| candidate divisor | source | divides \(\Omega^\flat\)? | coprime to \(C_1\)? | coprime to \(\lambda^\flat\)? | verdict |
|---|---|---|---|---|---|
| \(d_2=\operatorname{odd}(d_2)\) | sphere/radial | **NO for \(d_2>1\)**; in fact \((d_2,\Omega^\flat)=1\) | yes | yes | **anti-transfer; unusable** |
| \(T=\operatorname{odd}(T)\) | sphere/radial | not forced | not globally known | not globally known | root identity mod \(T\); no load |
| \(u=\operatorname{odd}(u)\) | cyclotomic | **NO**; \((u,\Omega^\flat)=1\) | yes | yes | forbidden source, no load |
| \(A=\operatorname{odd}(A)\) | source/root | not forced; overlap \(=(A,z)\) | not globally | yes | oriented to \(C_1\), capacity sufficient |
| \(m=\operatorname{odd}(m)\) | decimal linear | not forced | not globally | not globally | additive congruence only |

No sixth candidate is opened.

---

# 14. Composite Allocation Analysis

The ideal composite mechanism would require

\[
D_{\rm source}>1,
\]

\[
D_{\rm source}\mid C_1\lambda^\flat,
\]

while

\[
\gcd(D_{\rm source},C_1)
=
\gcd(D_{\rm source},\lambda^\flat)
=1.
\]

R4 finds no such \(D_{\rm source}\).

For the strongest candidate \(d_2\), the two firewall gcds are available,

\[
\gcd(d_2,C_1)
=
\gcd(d_2,\lambda^\flat)
=1,
\]

but the required load hypothesis fails maximally:

\[
\gcd(d_2,\Omega^\flat)=1.
\]

For \(u\), the same phenomenon occurs.

For \(A\), load can occur only through \(C_1\), so there is a perfectly legal orientation.

For \(m,T\), no uniform load is established.

Thus composite factor allocation never reaches a contradiction stage.

---

# 15. Prime Overlap Analysis

R4 searched for a prime

\[
p\mid\Omega^\flat
\]

that source identities force simultaneously into

\[
C_1
\]

and

\[
\lambda^\flat.
\]

No such prime is produced.

The two strongest locked source-prime families behave oppositely:

- if \(p\mid d_2\), then
  \[
  p\nmid\Omega^\flat;
  \]
- if \(p\mid u\), then
  \[
  p\nmid\Omega^\flat.
  \]

An \(A\)-prime occurring in the product is forced only into \(C_1\), because

\[
\gcd(A,\lambda^\flat)=1.
\]

Thus no forced-overlap prime exists in the audited architecture.

---

# 16. Square-Class / Parity Analysis

Because

\[
\gcd(C_1,\lambda^\flat)=1,
\]

the odd squarefree kernel of

\[
\Omega^\flat
\]

splits uniquely between the two primitive factors.

But R4 obtains no source theorem forcing the same odd prime parity into both sides.

The only locked square-class information is attached to primes of \(d_2\):

\[
p\mid d_2
\Longrightarrow
p\equiv1\pmod4.
\]

Yet those primes satisfy

\[
p\nmid\Omega^\flat.
\]

Therefore the Gaussian/square-class information has no allocation target.

Accordingly,

```text
ODD_SQUARE_CLASS_ROUTE=NO_LOCKED_ROOT_PRIME
GAUSSIAN_SPLITTING=NOT_REOPENED
```

---

# 17. Exact Computational Reconnaissance

R4 uses symbolic exact computation only as a regression check on the algebraic identities; no finite sample is promoted to a global theorem.

The exact symbolic substitutions checked are:

1. \(H^2=2KM\);
2. sphere:
   \[
   w^2=T d_2-H^2C_1^2;
   \]
3. third Euclidean identity:
   \[
   z=2uKC_1-AT;
   \]
4. primitive complement:
   \[
   \lambda^\flat=ud_2-AMC_1.
   \]

Substituting (2) and (3) into

\[
Aw^2+zd_2
\]

and then using (1) gives exactly

\[
\boxed{
Aw^2+zd_2
=
2KC_1\lambda^\flat.
}
\]

The symbolic residual is identically zero.

Likewise the \(d_2\)-residue reduces exactly to

\[
\boxed{
\Omega^\flat+AMC_1^2
\equiv0\pmod{d_2}.
}
\]

No floating-point calculation is used.

Historical finite root-layer corpora contain no full exact regular root survivor, so R4 does not fabricate “legal source samples” for divisor statistics. The absence of a finite survivor is not used as a theorem.

The central D2-LOAD conjecture does not need a numerical counterexample because it is symbolically refuted:

\[
d_2>1
\Longrightarrow
d_2\nmid\Omega^\flat.
\]

---

# 18. Counterexamples to Candidate Divisor Laws

## Candidate law D2-LOAD

Conjecture:

\[
d_2\mid\Omega^\flat.
\]

Status:

\[
\boxed{\textbf{FALSE for every }d_2>1.}
\]

Reason:

\[
\gcd(d_2,\Omega^\flat)=1.
\]

This is stronger than a computational counterexample.

---

## Candidate law ODD-D2-LOAD

Conjecture:

\[
\operatorname{odd}(d_2)\mid\Omega^\flat.
\]

Since \(d_2\) is already a ten-unit,

\[
\operatorname{odd}(d_2)=d_2.
\]

Hence the same symbolic refutation applies.

---

## Candidate law \(u\)-LOAD

Conjecture:

\[
u\mid\Omega^\flat.
\]

Status:

\[
\boxed{\textbf{FALSE since }u>1\text{ and }(u,\Omega^\flat)=1.}
\]

---

## Candidate \(T\)-LOAD

No conjecture is promoted after the exact modulo-\(T\) audit, because the sphere/Euclidean data only reproduce the root identity modulo \(T\).

---

## Candidate \(m\)-LOAD

No conjecture is promoted after recovering the exact source meaning of \(m\), because \(m\) is not a forced divisor and the decimal-linear identity is additive rather than multiplicative.

---

# 19. Proven vs Computational Claims

## NEW PROVED IN R4

1. Primitive firewall completion:
   \[
   \boxed{\gcd(\lambda^\flat,d_2)=1}.
   \]

2. Exact primitive source integrality:
   \[
   \boxed{
   \Omega^\flat
   =
   \frac{Aw^2+zd_2}{2K}
   \in\mathbf Z.
   }
   \]

3. Exact radial square extraction:
   \[
   \boxed{\Omega=\mathcal U^2\Omega^\flat}.
   \]

4. Sphere prime propagation:
   \[
   p\mid d_2\Rightarrow p\equiv1\pmod4.
   \]

5. Sphere anti-transfer:
   \[
   \boxed{\gcd(d_2,\Omega^\flat)=1}.
   \]

6. Sphere-to-root dependency:
   \[
   \boxed{
   \text{sphere}+\text{third Euclidean identity}
   \Rightarrow
   \Omega^\flat=C_1\lambda^\flat.
   }
   \]

7. Composite exclusion:
   \[
   \boxed{\gcd(ud_2,\Omega^\flat)=1}.
   \]

8. Exact \(A\)-orientation:
   \[
   \boxed{
   \gcd(\Omega^\flat,A)
   =
   \gcd(C_1,A)
   =
   \gcd(z,A).
   }
   \]

9. Radial \(p\)-depth identity:
   \[
   \boxed{
   v_p(\Omega)
   =
   2v_p(\mathcal U)+v_p(\Omega^\flat)
   \quad(p\mid\mathcal U).
   }
   \]

## FROZEN / INHERITED

1. \(x_*=a_1\).
2. \(\lambda^\flat=ud_2-AMC_1\).
3. \((C_1,d_2)=1\).
4. \((C_1,\lambda^\flat)=1\).
5. \((C_1,u)=(\lambda^\flat,u)=1\).
6. \(d_A=1\).
7. \(d_2,m,T,w,z,u,A,\mathcal U\) ten-unit where used.
8. \(2uKC_1=AT+z\).
9. \(GKC_1=AC_2+m\).
10. \(H^2C_1^2+w^2=T d_2\).

## COMPUTATIONAL ONLY

Only symbolic regression was performed in R4. No finite search result is promoted to a theorem.

---

# 20. Regular Closure Table

| region | status after R4 |
|---|---|
| \(d_A=1,\ \delta>0,\ q>1\) | **REDUCED / OPEN** |
| \(d_A=1,\ \delta=0,\ q>1\) | **REDUCED / OPEN** |
| \(d_A=1,\ \delta<0,\ q>1\) | **REDUCED / OPEN** |

The new theorems are tail-sign independent inside the common regular source chart, but none produces a contradiction in any one chamber.

No `REGULAR_HIGH_TAIL=CLOSED`, `REGULAR_BOUNDARY=CLOSED`, or `REGULAR_REVERSE=CLOSED` certificate is issued.

---

# 21. Retired Subroutes

The following routes are retired at the end of R4:

```text
D2_ODD_TRANSFER=REFUTED_BY_ANTI_TRANSFER
T_ODD_TRANSFER=INFORMATION_REDUNDANT
M_ODD_TRANSFER=NO_DIVISOR_SEMANTICS
U_ODD_TRANSFER=REFUTED_BY_PRIMITIVE_FIREWALL
A_ODD_TRANSFER=ORIENTED_BUT_NOT_FORCED
RADIAL_U_EXTRA_LOAD=NOT_FORCED
FORCED_OVERLAP_PRIME=NOT_FOUND
ODD_SQUARE_CLASS_ROUTE=NO_LOCKED_ROOT_PRIME
GAUSSIAN_SPLITTING=RETIRED_FOR_R5
PRIME_BY_PRIME_EXTENSION=FORBIDDEN
```

Most importantly,

\[
\boxed{
\text{the source supplies primitive nonabsorption but no nontrivial odd load.}
}
\]

This is the odd-prime analogue of the R3 lesson for \(2/5\)-capacity.

---

# 22. R4 Terminal Verdict

The exact ledger is:

```text
J2_STATUS=OPEN
REGULAR_J2_STATUS=OPEN

PRIMITIVE_FIREWALL=PROVED
P4_GCD_LAMBDAFLAT_D2=PROVED

RADIAL_U2_DECONTENTING=PROVED
OMEGA_FLAT_INTEGRAL=PROVED

D2_ODD_TRANSFER=REFUTED
D2_SPHERE_PRIME_CLASS=p == 1 (mod 4)
SPHERE_TO_ROOT_TRANSFER=INFORMATION_REDUNDANT
SPHERE_ANTI_TRANSFER=gcd(d2,OmegaFlat) == 1

DECIMAL_LINEAR_ODD_LOAD=NOT_FOUND
CYCLOTOMIC_U_ODD_LOAD=EXCLUDED
A_ODD_LOAD=ORIENTED_NOT_FORCED
RADIAL_CONTENT_EXTRA_ODD_LOAD=NOT_FORCED

SOURCE_DIVISOR_IMAGE_NONTRIVIAL=NO
FORCED_ODD_DIVISOR_DISCOVERY=FAILED
ODD_FACTOR_ALLOCATION=NOT_REACHED

R4_SUCCESS_LEVEL=R4-S1

R4_TERMINAL_VERDICT=
ODD_PRIME_ALLOCATION_ARCHITECTURE_FAILS
```

This is not a weak “nothing found” verdict.

The architecture is killed for a specific reason:

\[
\boxed{
\text{the strongest natural forbidden divisors }d_2\text{ and }u
\text{ are not loaded into the primitive root product;}
}
\]

indeed,

\[
\boxed{
\gcd(ud_2,\Omega^\flat)=1.
}
\]

Meanwhile the only source modulus with possible root-product overlap, \(A\), has a legal one-sided allocation into \(C_1\) and no forced nontrivial overlap.

Thus no divisor-capacity contradiction exists in the audited information class.

---

# 23. R5 Attack Target

By the R4 kill rule, 85-R5 must **not** continue with

- gcd amplification;
- odd divisor discovery;
- prime allocation;
- Gaussian splitting;
- squarefree-kernel bookkeeping;
- another variant of \(d_2/T/m/u/A\) factor support.

The next round must switch information class.

The cleanest remaining class is:

\[
\boxed{
\textbf{additive / ordered source geometry}
}
\]

rather than multiplicative support.

A suitable R5 target is therefore:

\[
\boxed{
\textbf{Canonical Root Order Collision}
\times
\textbf{Actual Digit-Window Orientation}
\times
\textbf{Signed Source Affine Mismatch}.
}
\]

The object to attack remains

\[
\varepsilon_*=0,
\]

but the question must become:

\[
\boxed{
\text{does the unique source-selected }C_1
\text{ place }
\lambda^\flat=ud_2-AMC_1
\text{ in an impossible sign/size/order cell?}
}
\]

Any R5 theorem must use genuinely new additive or ordered information from the source/digit windows; it may not repackage the factor support proved insufficient in R4.

---

# 24. Final Assessment

85-R4 began from

\[
\boxed{
\Omega^\flat
=
C_1\lambda^\flat,
\qquad
(C_1,\lambda^\flat)=1.
}
\]

The hoped-for third fact was

\[
D_{\rm source}>1,
\qquad
D_{\rm source}\mid\Omega^\flat,
\]

with no legal primitive destination.

What the exact audit gives instead is

\[
\boxed{
(d_2,\Omega^\flat)=1,
\qquad
(u,\Omega^\flat)=1,
}
\]

\[
\boxed{
(A,\Omega^\flat)=(A,z),
}
\]

and no \(m\)- or \(T\)-load.

The most attractive source divisor \(d_2\) is not merely harmless. It is **anti-loaded**:

\[
\boxed{
\Omega^\flat
\equiv
-AMC_1^2
\pmod{d_2}.
}
\]

Thus the primitive factorization has enough odd-prime capacity because the source does not ask it to absorb the forbidden odd primes in the first place.

The final R4 lesson is therefore:

\[
\boxed{
\textbf{primitive firewall exists,}
}
\]

but

\[
\boxed{
\textbf{there is no source-forced odd divisor to fire at it.}
}
\]

Hence, by the predeclared kill criterion,

\[
\boxed{
\textbf{Primitive Odd-Prime Factor Allocation is retired.}
}
\]

The regular \(J=2\) branch remains open, and R5 must change information class.

---

# Provenance Anchors

The R4 derivations use the frozen exact identities and status ledgers from:

- `85_R3_Source_Cut_Residual_Exclusion_and_Regular_J2_Closure.md`
- `A1_J2_NRSEC_Report.md`
- `A1_J2_CZDR_Report.md`
- `A1_J2_DCDC5_Report.md`
- `J2-55-R1-A-Root-Lift-Report.md`
- `85_R1_J2_Terminal_Recompression_and_Minimal_Survivor.md`

No external literature theorem is needed in R4.

---

**FINAL_REPORT_FILE:** `85_R4_Primitive_Odd_Prime_Allocation_and_Source_Divisor_Image.md`
