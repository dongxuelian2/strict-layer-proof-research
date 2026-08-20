# 105-R11 — Exact DES Quotient Residue × Positive-Lift Threshold Membership × Zero-Residue Exceptional Construction

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R11  
**Frozen input:** 105-R1--R10  
**Permitted architecture:** Route D only  
**Single responsibility:** decide, or further legally compress,
\[
[Q_i^{\rm DES}]_{d_i^*}\stackrel?{\in}\mathcal K_i^+.
\]

---

## 1. Executive Verdict

R11 does **not** prove source-wide threshold avoidance and does **not** construct a genuine positive quotient hit. Therefore neither

\[
\texttt{POST\_PSDG\_SOURCE\_RADIAL\_FIBRE\_EMPTY}
\]

nor

\[
\texttt{PLAIN\_INTEGER\_RADIAL\_GATE\_PASSED}
\]

can be signed globally.

It does, however, produce four exact reductions that are strictly stronger than R10:

1. **Exact quotient floor collapse.**
   \[
   \boxed{
   Q_2^{\rm DES}=\frac{x_2-\rho_2}{M_2}
   =\left\lfloor\frac{x_2}{M_2}\right\rfloor,
   \qquad
   Q_3^{\rm DES}=\frac{x_3-\rho_3}{M_3}
   =\left\lfloor\frac{x_3}{M_3}\right\rfloor.
   }
   \]
   The long source-native transport formulas remain essential for provenance and local division, but \(V,P_1,K_3,\ldots\) introduce no additional free quotient digit after \(M_i,\rho_i\) are fixed.

2. **Face-A \(h\)-channel elimination.**
   \[
   \boxed{\gcd(C_2,h)=1.}
   \]
   Consequently R10's
   \[
   d_2^*=\gcd(C_2,10uh)
   \]
   sharpens source-wide to
   \[
   \boxed{d_2^*=\gcd(C_2,10u).}
   \]
   Thus no prime coming only from \(h\) can ever enter the R11 modulus.

3. **Correct local quotient division firewall.**  
   If
   \[
   D_iQ_i^{\rm DES}=N_i
   \]
   is the exact R10 integer transport and \(p^e\Vert d_i^*\), put
   \[
   f=v_p(D_i).
   \]
   Exact integrality gives \(p^f\mid N_i\), and
   \[
   \boxed{
   Q_i^{\rm DES}
   \equiv
   \frac{N_i}{p^f}
   \left(\frac{D_i}{p^f}\right)^{-1}
   \pmod{p^e}.
   }
   \tag{R11-LOCAL}
   \]
   This is the correct replacement for any illegal \(D_i^{-1}\pmod{p^e}\).

4. **Single remaining local theorem schema.**  
   Once (R11-LOCAL) is used, the only source-wide arithmetic datum not fixed by existing theorems is
   \[
   \boxed{
   \Xi_{i,p}
   :=
   \left[
   \frac{N_i}{p^{v_p(D_i)}}
   \right]_{p^e},
   \qquad
   p^e\Vert d_i^*.
   }
   \]
   The unit factor \((D_i/p^f)^{-1}\) is then explicit, the local \(Q_i\)-residue is explicit, CRT reconstructs \(\kappa_i^{10}\), and the already-frozen threshold decides Avoid/Hit.

Thus the legal R11 terminal verdict is:

```text
R11_TERMINAL_VERDICT=
R11_REDUCED_TO_NORMALIZED_LOCAL_TRANSPORT_NUMERATOR_RESIDUE_GATE__
FACE_A_H_CHANNEL_ELIMINATED__
D2STAR_SHARPENED_TO_GCD_C2_10U__
EXACT_PPOWER_QUOTIENT_DIVISION_FIREWALL_PROVED__
ZERO_AND_MAXIMAL_LIFT_CONSTRUCTIONS_EXACTLY_REDUCED__
NO_GLOBAL_AVOID_THEOREM__
NO_POSITIVE_HIT
```

This is a **partial success under the R11 single-local-gate rule**, not an extinction theorem and not a hit.

---

## 2. Frozen R1–R10 State

All architecture named frozen in the R11 prompt remains frozen.

In particular this report does not reopen:

- radial interval architecture;
- broad successor theory;
- endpoint remainder distribution;
- DES redesign;
- Bézout information-loss;
- generic power-\(10\) orbit analysis;
- discriminants, PSDG, determinant packets, Gaussian packets;
- primitive parametrization;
- Smith redesign;
- broad \(2/5\)-adic architecture;
- q=1 progression or coprimality before a plain hit.

The accepted R10 facts are:

\[
d_2^*=\gcd(C_2,10b_1h),\qquad M_2=C_2/d_2^*,
\]

\[
d_3^*=\gcd(C_3,10K_3),\qquad M_3=C_3/d_3^*,
\]

\[
x_i=\rho_i+M_iQ_i^{\rm DES},
\qquad
\kappa_i^{10}=[Q_i^{\rm DES}]_{d_i^*},
\]

and the positive-lift sets \(\mathcal K_i^+\) are exact frozen threshold sets.

---

## 3. Current Exact Quotient Gate

The active gate is exactly

\[
\boxed{
[Q_i^{\rm DES}]_{d_i^*}\in\mathcal K_i^+?
}
\]

with \(i=2\) on Face A and \(i=3\) on Face B.

R11 introduces no second global gate. All local decompositions below are implementations of this single membership problem.

---

## 4. Exact Face-A DES Quotient Formula

Put

\[
x_2=10^{n_2-1},
\]

and inherit the exact R10 P-row identity

\[
10b_1P_1x_2=E_P-VC_2,
\]

where

\[
E_P=G(b_1X+b_2)Q_0+K_3.
\]

Define

\[
\boxed{
T_{2P}(\rho_2)
=
\frac{E_P-10b_1P_1\rho_2}{C_2}
\in\mathbf Z.
}
\]

Then

\[
\boxed{
Q_2^{\rm DES}
=
\frac{T_{2P}(\rho_2)-V}
{(10b_1P_1)/d_2^*}.
}
\tag{Q2-SRC}
\]

The equivalent D-row check is

\[
Q_2^{\rm DES}
=
\frac{T_{2D}(\rho_2)-KV}
{(10b_1D)/d_2^*}.
\]

### Exact numerator

\[
\boxed{
N_2:=T_{2P}(\rho_2)-V.
}
\]

### Exact denominator

\[
\boxed{
D_2:=\frac{10b_1P_1}{d_2^*}.
}
\]

### Floor collapse

Using the exact identity,

\[
\begin{aligned}
N_2
&=
\frac{E_P-10b_1P_1\rho_2-VC_2}{C_2}\\
&=
\frac{10b_1P_1(x_2-\rho_2)}{C_2}\\
&=
\frac{10b_1P_1}{d_2^*}
\frac{x_2-\rho_2}{M_2}.
\end{aligned}
\]

Hence

\[
\boxed{
D_2Q_2^{\rm DES}=N_2
}
\]

and

\[
\boxed{
Q_2^{\rm DES}
=
\frac{x_2-\rho_2}{M_2}
=
\left\lfloor\frac{x_2}{M_2}\right\rfloor.
}
\tag{Q2-FLOOR}
\]

The last equality uses \(0\le\rho_2<M_2\) and \(x_2\equiv\rho_2\pmod{M_2}\).

---

## 5. Exact Face-B DES Quotient Formula

Put

\[
x_3=10^{n_3-1}.
\]

The exact R10 identity is

\[
10K_3x_3=b_3Q_0-VC_3.
\]

Define

\[
\boxed{
T_3(\rho_3)
=
\frac{b_3Q_0-10K_3\rho_3}{C_3}
\in\mathbf Z.
}
\]

Then

\[
\boxed{
Q_3^{\rm DES}
=
\frac{T_3(\rho_3)-V}
{(10K_3)/d_3^*}.
}
\tag{Q3-SRC}
\]

### Exact numerator

\[
\boxed{N_3:=T_3(\rho_3)-V.}
\]

### Exact denominator

\[
\boxed{D_3:=\frac{10K_3}{d_3^*}.}
\]

Again,

\[
N_3
=
\frac{10K_3(x_3-\rho_3)}{C_3}
=
D_3\frac{x_3-\rho_3}{M_3}.
\]

Therefore

\[
\boxed{
Q_3^{\rm DES}
=
\frac{x_3-\rho_3}{M_3}
=
\left\lfloor\frac{x_3}{M_3}\right\rfloor.
}
\tag{Q3-FLOOR}
\]

---

## 6. Quotient Integrality Audit

R10's integer-transport lemma already proves that \(D_i\mid N_i\). R11 makes the proof transparent:

\[
N_i=D_i\frac{x_i-\rho_i}{M_i},
\]

and \(M_i\mid x_i-\rho_i\) by definition of \(\rho_i\).

Thus:

\[
\boxed{Q_i^{\rm DES}\in\mathbf Z_{\ge0}.}
\]

The sign is also exact:

\[
x_i=\rho_i+M_iQ_i^{\rm DES},
\qquad
0\le\rho_i<M_i,
\]

so \(Q_i^{\rm DES}\ge0\).

The source-native formulas do not have a hidden sign ambiguity.

---

## 7. \(d_2^*\) Source Prime-Type Decomposition

R10 had

\[
d_2^*=\gcd(C_2,10uh).
\]

R11 proves a sharper theorem.

### Theorem R11.1 — \(h\)-channel separation

Let

\[
h=\gcd(P_1,Q_0).
\]

If a prime \(p\mid C_2\) and \(p\mid h\), then:

- \(p\mid P_1,Q_0\);
- \(p\mid C_2\Rightarrow p\mid P_2\), since \(P_2=g_2C_2\);
- the primitive sphere
  \[
  P_1^2+P_2^2+P_3^2=Q_0^2
  \]
  gives \(p\mid P_3\).

Hence \(p\) divides all four primitive coordinates, contradiction.

Therefore

\[
\boxed{\gcd(C_2,h)=1.}
\tag{H-SEPARATION}
\]

Using the frozen Smith reducedness
\[
b_1=s\alpha u,\quad b_2=s\alpha\beta t,\quad \gcd(C_2,b_2)=1,
\]
we already have \(\gcd(C_2,s\alpha)=1\). Consequently

\[
\boxed{
d_2^*=\gcd(C_2,10u).
}
\tag{D2-SHARP}
\]

This removes both:

- the pure \(h\)-source component;
- any \(b_1\)-component coming only from \(s\alpha\).

The exact prime-power decomposition is therefore

\[
\boxed{
d_2^*
=
2^{e_2}5^{e_5}
\prod_{\substack{p\ne2,5\\p\mid\gcd(C_2,u)}}
p^{e_p},
}
\]

where

\[
e_2=\min(v_2(C_2),1+v_2(u)),
\]

\[
e_5=\min(v_5(C_2),1+v_5(u)),
\]

and for \(p\ne2,5\),

\[
e_p=\min(v_p(C_2),v_p(u)).
\]

---

## 8. \(d_3^*\) Source Prime-Type Decomposition

R10 gives

\[
\boxed{
d_3^*=\gcd(C_3,10K_3),
\qquad
d_3^*\mid Q_0.
}
\]

Thus every \(p\mid d_3^*\) satisfies

\[
p\mid C_3,\qquad p\mid Q_0.
\]

Because \(p\mid C_3\Rightarrow p\mid P_3\), primitive sphere gives:

- \(p\nmid P_1\);
- \(p\nmid P_2\);
- \(P_1^2+P_2^2\equiv0\pmod p\).

Hence every such prime is odd and

\[
\boxed{p\equiv1\pmod4.}
\]

In particular

\[
\boxed{v_2(d_3^*)=0.}
\]

The prime \(5\) is allowed.

Write

\[
\boxed{
d_3^*
=
\prod_{\substack{p\mid Q_0\\p\equiv1(4)}}
p^{\min(v_p(C_3),v_p(10K_3))}
}
\]

with the understanding that only primes actually dividing both factors occur.

---

## 9. Decimal \(2/5\) Quotient Components

For Face A and \(p\in\{2,5\}\), let

\[
c=v_p(C_2),\qquad a=v_p(u),\qquad \epsilon_p=v_p(10)=1.
\]

From (D2-SHARP),

\[
e=v_p(d_2^*)=\min(c,1+a).
\]

If \(p\mid C_2\), reducedness \(\gcd(C_2,b_2)=1\) forces
\[
p\nmid s\alpha\beta t.
\]
Hence
\[
v_p(b_1)=v_p(u)=a.
\]

For the P-row denominator

\[
D_2=\frac{10b_1P_1}{d_2^*},
\]

we have the exact exponent

\[
\boxed{
f_{2,p}
=
1+a+v_p(P_1)-e.
}
\tag{DEC-F}
\]

Thus the decimal local quotient is

\[
\boxed{
Q_2^{\rm DES}
\equiv
\frac{N_2}{p^{f_{2,p}}}
\left(
\frac{D_2}{p^{f_{2,p}}}
\right)^{-1}
\pmod{p^e}.
}
\]

No source-wide theorem currently forces the normalized numerator to be \(0\) modulo \(p^e\). High power-of-ten valuation alone therefore does **not** universally trivialize the \(2/5\) quotient components.

The E fixture shows why the denominator firewall is necessary: \(d_2^*=2\) but \(D_2=7450\) is even.

---

## 10. \(b_1\)-Component Quotient Audit

There is no independent \(b_1\)-only modulus source after R11.1.

Indeed

\[
b_1=s\alpha u,
\]

while

\[
\gcd(C_2,s\alpha)=1.
\]

Therefore every nondecimal prime of \(b_1\) that enters \(d_2^*\) must enter through \(u\).

So the R11 source-origin classification is:

```text
B1_ONLY_COMPONENT = EMPTY
B1_COMPONENT_THAT_SURVIVES = U_COMPONENT
```

This is stronger than treating \(\operatorname{supp}(b_1)\) as an independent type.

---

## 11. \(h\)-Component Quotient Audit

By (H-SEPARATION),

\[
\boxed{\gcd(C_2,h)=1.}
\]

Therefore:

```text
H_COMPONENT_IN_D2STAR = IMPOSSIBLE
```

No \(h\)-adic quotient residue remains to be computed.

All frozen R7C/R7D statements about \(h\mid c\), \(h^2\mid N\), and split-prime support remain valid but are irrelevant to \(d_2^*\) after this separation theorem.

---

## 12. Odd \(u\)-Component Quotient Audit

Let \(p\ne2,5\) and \(p^e\Vert d_2^*\). Then

\[
p\mid C_2,\qquad p\mid u.
\]

Because \(p\mid C_2\) and \(\gcd(C_2,b_2)=1\),

\[
p\nmid s\alpha\beta t.
\]

Hence

\[
v_p(b_1)=v_p(u)=:a.
\]

R11.1 also gives \(p\nmid h\). In fact \(p\nmid P_1\) on this support:

- if \(p\mid\gamma\), frozen \(\gamma_0\)-allocation gives \(p\mid Q_0\), and \(p\mid P_1\) would put \(p\mid h\);
- if \(p\mid u_0\) but \(p\nmid\gamma\), then \(p\mid P_2,P_3\), and primitive sphere forces \(P_1,Q_0\) to be units.

Therefore

\[
v_p(10b_1P_1)=a.
\]

Since

\[
e=\min(v_p(C_2),a),
\]

the local denominator exponent is

\[
\boxed{
f_{2,p}=a-e=\max(a-v_p(C_2),0).
}
\tag{U-F}
\]

This gives a complete p-adic division law for every odd nondecimal Face-A modulus prime.

### Two source subtypes

Write \(u=\gamma u_0\).

#### Type \(\Gamma\)

\[
p\mid\gamma,\qquad p\nmid u_0.
\]

Then:

\[
p\mid P_2,Q_0,\qquad p\nmid P_1P_3,
\]

and

\[
p\equiv1\pmod4.
\]

#### Type \(U_0\)

\[
p\mid u_0,\qquad p\nmid\gamma.
\]

Then:

\[
p\mid P_2,P_3,\qquad p\nmid P_1Q_0.
\]

If \(a=v_p(u_0)\), both \(P_2,P_3\) are divisible by \(p^a\), hence

\[
p^{2a}\mid(Q_0-P_1)(Q_0+P_1).
\]

Since \(p\) is odd and \(P_1,Q_0\) are units, exactly one factor is \(p\)-divisible, so

\[
\boxed{
P_1\equiv \pm Q_0\pmod{p^{2a}}.
}
\tag{U0-SPHERE}
\]

This is genuine local source structure, but by itself it does not determine \(\Xi_{2,p}\).

---

## 13. Face-B \(Q_0\)-Component Quotient Audit

For \(p^e\Vert d_3^*\), set

\[
c=v_p(C_3),\qquad a=v_p(10K_3).
\]

Because \(d_3^*=\gcd(C_3,10K_3)\),

\[
e=\min(c,a).
\]

For

\[
D_3=\frac{10K_3}{d_3^*},
\]

\[
\boxed{
f_{3,p}=a-e=\max(a-c,0).
}
\tag{B-F}
\]

Thus

\[
\boxed{
Q_3^{\rm DES}
\equiv
\frac{N_3}{p^{f_{3,p}}}
\left(
\frac{D_3}{p^{f_{3,p}}}
\right)^{-1}
\pmod{p^e}.
}
\]

Additionally,

\[
p\mid C_3,Q_0,P_3,\qquad p\nmid P_1P_2,\qquad p\equiv1\pmod4.
\]

No frozen theorem currently fixes the normalized numerator residue
\[
(N_3/p^{f_{3,p}})\bmod p^e.
\]

---

## 14. Local Quotient Residue Atlas

The exact universal local atlas is:

| face | \(p^e\Vert d_i^*\) | exact \(D_i\) | exact \(N_i\) | \(f=v_p(D_i)\) | local quotient |
|---|---|---|---|---:|---|
| A | any actual \(p^e\) | \((10b_1P_1)/d_2^*\) | \(T_{2P}(\rho_2)-V\) | exact | \((N_2/p^f)(D_2/p^f)^{-1}\bmod p^e\) |
| B | any actual \(p^e\) | \((10K_3)/d_3^*\) | \(T_3(\rho_3)-V\) | exact | \((N_3/p^f)(D_3/p^f)^{-1}\bmod p^e\) |

The only source-wide unknown inside each row is

\[
\boxed{
\Xi_{i,p}
=
(N_i/p^f)\bmod p^e.
}
\]

All division ambiguity has been removed.

---

## 15. CRT Reconstruction

Write

\[
d_i^*=\prod_p p^{e_p}.
\]

Once every local value

\[
q_{i,p}:=Q_i^{\rm DES}\bmod p^{e_p}
\]

is known, CRT gives one and only one

\[
\boxed{
q_i^{\rm CRT}\in\{0,\ldots,d_i^*-1\}
}
\]

such that

\[
q_i^{\rm CRT}\equiv q_{i,p}\pmod{p^{e_p}}
\]

for every \(p\mid d_i^*\).

Then

\[
\boxed{
\kappa_i^{10}=q_i^{\rm CRT}.
}
\]

No modulus larger than the actual \(d_i^*\)-prime powers is introduced in this reconstruction.

---

## 16. Exact \(\kappa_i^{10}\)

Source-wide:

\[
\boxed{
\kappa_2^{10}
=
\operatorname{CRT}_p
\left[
\frac{N_2}{p^{f_{2,p}}}
\left(\frac{D_2}{p^{f_{2,p}}}\right)^{-1}
\right]_{p^{e_p}},
}
\]

\[
\boxed{
\kappa_3^{10}
=
\operatorname{CRT}_p
\left[
\frac{N_3}{p^{f_{3,p}}}
\left(\frac{D_3}{p^{f_{3,p}}}\right)^{-1}
\right]_{p^{e_p}}.
}
\]

This is exact, but it is not yet a source-wide constant or threshold-side theorem because the normalized transport numerators remain moving.

---

## 17. Positive Threshold Sets

For \(\rho_i>0\), let

\[
W_A=C_3,\qquad W_B=C_2.
\]

The frozen exact threshold is

\[
\boxed{
\kappa_{i,\rm crit}
=
\left\lfloor
\frac{W_i(d_i^*M_i-\rho_i)-G_i}
{W_iM_i}
\right\rfloor+1.
}
\]

Then

\[
\boxed{
\mathcal K_i^+
=
\{\kappa\in\{0,\ldots,d_i^*-1\}:
\kappa\ge\kappa_{i,\rm crit}\}.
}
\]

For \(\rho_i=0\), \(\kappa=0\) is separately positive on every continuous active face; additional \(\kappa\ge1\) are tested by the affine surplus formula.

---

## 18. Quotient-Size Bounds

R11 obtains the identity

\[
Q_i^{\rm DES}=\left\lfloor\frac{x_i}{M_i}\right\rfloor.
\]

Therefore:

\[
x_i<M_i\Longrightarrow Q_i^{\rm DES}=0\Longrightarrow \kappa_i^{10}=0.
\]

More generally:

\[
x_i<tM_i\Longrightarrow 0\le Q_i^{\rm DES}\le t-1.
\]

This is a valid nonmodular avoidance route.

However, no frozen source-wide theorem proves

\[
x_i<M_i
\]

or any uniform bound strong enough to force

\[
\kappa_i^{10}<\kappa_{i,\rm crit}
\]

on all theoretically positive profiles.

For B and E, \(x_2<M_2\) holds and gives \(Q_2^{\rm DES}=0\) immediately.

---

## 19. Threshold-Avoidance Theorem Attempt

The desired theorem is

\[
[Q_i^{\rm DES}]_{d_i^*}<\kappa_{i,\rm crit}.
\]

R11 tests three legal routes:

1. quotient-size locking;
2. source-forced divisibility of \(Q_i^{\rm DES}\);
3. local prime-power locking followed by CRT.

The frozen source data do not yield a source-wide inequality of type (1), and the local audit shows that types (2)–(3) stop precisely at \(\Xi_{i,p}\).

Therefore:

```text
DES_QUOTIENT_THRESHOLD_AVOIDANCE_THEOREM = NOT_PROVED
```

This is not inferred from failed search; it is the exact theorem-interface frontier.

---

## 20. E Parity/Valuation Locking Audit

State E has

\[
(b_1,b_2,b_3)=(5,5,1),
\]

\[
(P_1,P_2,P_3,Q_0)=(298,2514,1485,2935),
\]

\[
V=5,\quad C_2=2514,\quad C_3=297,
\]

\[
d_2^*=2,\quad M_2=1257,\quad \rho_2=10,\quad x_2=10.
\]

Hence

\[
\boxed{Q_2^{\rm DES}=0,\qquad \kappa_2^{10}=0.}
\]

The source P-row denominator is

\[
\boxed{
D_2=\frac{10\cdot5\cdot298}{2}=7450.
}
\]

Thus

\[
\gcd(D_2,d_2^*)=2.
\]

A direct inverse modulo \(2\) is illegal. Instead the exact numerator is

\[
N_2=D_2Q_2^{\rm DES}=0,
\]

and the local division firewall gives \(Q_2^{\rm DES}\equiv0\pmod2\) correctly.

Therefore E is **not** evidence for a general “denominator is invertible” parity theorem. Its actual locking mechanism is stronger and simpler:

\[
\boxed{x_2<M_2\Rightarrow Q_2^{\rm DES}=0.}
\]

Threshold:

\[
\kappa_{2,\rm crit}=2,
\qquad
\mathcal K_2^+=\varnothing.
\]

Surpluses:

\[
\Sigma_A(0)=-721518,
\qquad
\Sigma_A(1)=-348189.
\]

So E is DES-coset-wide extinct independently of actual lift selection.

---

## 21. B Regression

State B has

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445),
\]

\[
V=24,\quad
(C_2,C_3)=(109,25),
\]

\[
d_2^*=1,\quad M_2=109,\quad \rho_2=x_2=10.
\]

Thus

\[
Q_2^{\rm DES}=0,\qquad\kappa_2^{10}=0.
\]

The threshold is

\[
\kappa_{2,\rm crit}=1>d_2^*-1,
\]

so

\[
\mathcal K_2^+=\varnothing,
\]

and

\[
\Sigma_A=-1635.
\]

The \(d^*=1\) machinery automatically degenerates to the singleton residue case.

As a Face-B transport regression on the same state:

\[
C_3=25,\quad d_3^*=5,\quad M_3=5,\quad \rho_3=x_3=1,
\]

\[
K_3=296,\quad b_3=8,\quad Q_0=445,\quad V=24.
\]

Then

\[
T_3(1)=24=V,
\]

\[
D_3=(10K_3)/d_3^*=592,
\]

and

\[
Q_3^{\rm DES}=0,\qquad
Q_3^{\rm DES}\bmod5=0.
\]

This is a transport regression only; B's active continuous face is A.

---

## 22. \(\rho_i=0\) Exceptional Construction

General exact equivalence:

\[
\rho_i=0
\iff
M_i\mid x_i.
\]

If in addition the actual lift is the lower lift \(\kappa_i^{10}=0\), then

\[
d_i^*\mid Q_i^{\rm DES}
=
x_i/M_i,
\]

hence

\[
\boxed{
\rho_i=0,\ \kappa_i^{10}=0
\iff
C_i\mid x_i=10^{n_i-1}.
}
\tag{ZERO-LOWER}
\]

Therefore the lower-lift construction is exactly decimal divisibility.

### Face A

A zero/lower hit requires

\[
\boxed{
C_2\mid10^{n_2-1}.
}
\]

Thus \(C_2\) must be \(2/5\)-smooth with exponents no larger than those available in the endpoint power.

### Face B

R10 also gives

\[
\rho_3=0\iff C_3\mid Q_0.
\]

Combining with (ZERO-LOWER):

\[
C_3\mid Q_0
\quad\text{and}\quad
C_3\mid10^{n_3-1}.
\]

Since \(Q_0\) is odd,

\[
\boxed{
C_3=5^a,\qquad
C_3\mid Q_0,\qquad
a\le n_3-1.
}
\tag{B-ZERO}
\]

This includes \(a=0\), i.e. \(C_3=1\).

No genuine post-PSDG profile satisfying these construction conditions is present in the frozen authoritative census.

---

## 23. Maximal-Lift Construction

The maximal lift condition is

\[
\kappa_i^{10}=d_i^*-1
\iff
Q_i^{\rm DES}\equiv-1\pmod{d_i^*}.
\]

Since

\[
x_i-\rho_i=M_iQ_i^{\rm DES},
\]

this is equivalent to

\[
\boxed{
C_i
\mid
x_i+M_i-\rho_i.
}
\tag{MAX-LIFT}
\]

This is the exact reverse-construction equation.

No genuine post-PSDG maximal-lift positive profile is currently known.

---

## 24. General Positive-Residue Construction

For any target

\[
\kappa_{\rm target}\in\mathcal K_i^+,
\]

the exact reverse target is

\[
Q_i^{\rm DES}\equiv\kappa_{\rm target}\pmod{d_i^*}.
\]

Equivalently,

\[
\boxed{
N_i
\equiv
D_i\kappa_{\rm target}
\pmod{D_id_i^*},
}
\]

interpreted through exact integer divisibility rather than modular inversion.

Primewise, after removing \(p^f\),

\[
\boxed{
\frac{N_i}{p^f}
\equiv
\frac{D_i}{p^f}\kappa_{\rm target}
\pmod{p^e}.
}
\]

This is the narrowest legal source-native construction system.

---

## 25. Targeted Quotient Search

The R11 search rule allows search only on profiles with

\[
\mathcal K_i^+\ne\varnothing.
\]

The authoritative frozen post-PSDG continuous census contains only B and E, and both have

\[
\mathcal K_2^+=\varnothing.
\]

Therefore there is **no authorized theoretically-positive frozen profile to search** in R11.

R11 does not reopen the broad R9 boxes. Historical R9 finite searches remain evidence only and are not upgraded to a theorem.

---

## 26. First Positive Quotient Hit

None.

```text
POSITIVE_DES_QUOTIENT_HIT = NO
```

This means only “no genuine hit has been constructed/proved from the available post-PSDG source profiles,” not universal nonexistence.

---

## 27. Exact Plain \(U\) Recovery

If a future Face-A hit occurs, write

\[
x_2=q_2C_2+r_2.
\]

Then

\[
\boxed{
U_{\mathbf Z}
=
\begin{cases}
q_2,&r_2=0,\\
q_2+1,&r_2>0.
\end{cases}
}
\]

Equivalently

\[
U_{\mathbf Z}=\left\lceil x_2/C_2\right\rceil.
\]

Face B is identical with \(2\to3\).

No new hit occurs in R11, so no numerical \(U\) is recovered.

---

## 28. q=1 Progression Audit

Not activated.

A q=1 affine progression is downstream of a plain integer hit. R11 produces no such hit, so the quotient gate remains upstream.

```text
Q1_PROGRESSION_ACTIVE = NO_NEW_HIT
Q1_PROGRESSION_PASS = NOT_REACHED
```

---

## 29. Coprimality Audit

Not activated.

No R11 candidate reaches

\[
(U,V)=1
\]

as a new test.

```text
COPRIMALITY_PASS = NOT_REACHED
```

---

## 30. First Source Integer \(U\)

None.

```text
SOURCE_INTEGER_U_FOUND = NO
SOURCE_INTEGER_U = NONE
```

---

## 31. Downstream Source Word Audit

Not reached:

- digit synchronization: not reached;
- actual cut: not reached;
- full word: not reached;
- outer completion: not reached.

The first failure remains before source-word reconstruction.

---

## 32. New First-Failure Gate

Define for every actual local factor

\[
p^e\Vert d_i^*,
\]

\[
D_i=
\begin{cases}
(10b_1P_1)/d_2^*,&i=2,\\
(10K_3)/d_3^*,&i=3,
\end{cases}
\]

\[
N_i=
\begin{cases}
T_{2P}(\rho_2)-V,&i=2,\\
T_3(\rho_3)-V,&i=3,
\end{cases}
\]

\[
f_{i,p}=v_p(D_i).
\]

The new exact first-failure is:

\[
\boxed{
\texttt{NORMALIZED\_LOCAL\_DES\_TRANSPORT\_NUMERATOR\_RESIDUE}
}
\]

namely determine

\[
\boxed{
\Xi_{i,p}
=
\left[
N_i/p^{f_{i,p}}
\right]_{p^e}
}
\]

strongly enough that

\[
Q_i^{\rm DES}\bmod p^e
\]

and hence the CRT lift index is forced to the negative or positive threshold side.

This is one local theorem schema; it is not a return to a generic \(10^n\bmod C_i\) orbit.

---

## 33. Failed / Falsified Routes

1. **Direct inversion of \(D_i\pmod{d_i^*}\):** false in general; E has \(\gcd(D_2,d_2^*)=2\).
2. **\(h\)-component of Face-A modulus:** eliminated exactly.
3. **Independent \(b_1\)-only modulus type:** eliminated by \(\gcd(C_2,s\alpha)=1\); only \(u\) survives.
4. **Universal E-style parity locking:** not proved; E locks because \(Q=0\), not because every \(d_2^*=2\) profile has even quotient.
5. **High endpoint \(2/5\)-valuation automatically gives \(Q\equiv0\):** not proved source-wide.
6. **Odd split support alone determines quotient residue:** false as an inference; support determines modulus type, not the normalized transport numerator.
7. **Frozen no-hit census implies avoidance:** rejected.
8. **Generic multiplicative order modulo \(C_i\):** not used.
9. **Reopening PSDG/packet/Smith/DES:** not used.
10. **Threshold criterion restatement as closure:** rejected.

---

## 34. Exact Remaining Unknowns

There is no remaining ambiguity about:

- the exact integer quotient formulas;
- numerator and denominator;
- denominator integrality;
- legal p-adic cancellation;
- Face-A \(h\)-support;
- Face-A \(b_1\)-only support;
- Face-B split-prime support;
- zero/lower-lift criterion;
- maximal-lift criterion;
- threshold comparison once \(\kappa_i^{10}\) is known.

The remaining theorem is:

\[
\boxed{
\Xi_{i,p}
=
\left[
\frac{N_i}{p^{v_p(D_i)}}
\right]_{p^e}
\quad
(p^e\Vert d_i^*)
}
\]

for the actual source-supported local factor, with enough rigidity to decide the CRT threshold side.

This is the R11 single local quotient residue gate.

---

## 35. R11 Terminal Verdict

```text
R11_TERMINAL_VERDICT=
R11_REDUCED_TO_NORMALIZED_LOCAL_TRANSPORT_NUMERATOR_RESIDUE_GATE__
NO_GLOBAL_AVOID__
NO_HIT__
FACE_A_H_CHANNEL_ELIMINATED__
D2STAR_EQUALS_GCD_C2_10U__
LOCAL_EXACT_DIVISION_FIREWALL_PROVED
```

Face A:

```text
FACE_A_STATUS=
KNOWN_CONTINUOUS_B_E_COSET_WIDE_EXTINCT__
GLOBAL_THRESHOLD_AVOIDANCE_NOT_PROVED__
NO_POSITIVE_PROFILE
```

Face B:

```text
FACE_B_STATUS=
EXACT_QUOTIENT_AND_LOCAL_GATE_FORMULATED__
NO_ACTIVE_FROZEN_CONTINUOUS_PROFILE__
GLOBAL_THRESHOLD_AVOIDANCE_NOT_PROVED
```

---

## 36. R12 Authorization Decision

R12 is authorized only under the partial-success Route D rule.

It may attack exactly:

\[
\boxed{
\textbf{Normalized Local DES Transport Numerator Residue Gate}
}
\]

for

\[
p^e\Vert d_i^*.
\]

It may not reopen broad quotient research, endpoint remainder, generic power-\(10\) orbit modulo \(C_i\), PSDG, Smith, DES, discriminant, or radial interval architecture.

Recommended R12 theorem target:

\[
\boxed{
\frac{N_i}{p^{v_p(D_i)}}
\bmod p^e
\quad\text{is source-rigid enough to force }
[Q_i^{DES}]_{d_i^*}\notin\mathcal K_i^+
}
\]

or construct one local value that CRT-synthesizes a positive hit.

---

# Machine-readable Terminal Block

```text
R11_TERMINAL_VERDICT=R11_REDUCED_TO_NORMALIZED_LOCAL_TRANSPORT_NUMERATOR_RESIDUE_GATE__NO_GLOBAL_AVOID__NO_HIT__FACE_A_H_CHANNEL_ELIMINATED__D2STAR_EQUALS_GCD_C2_10U__LOCAL_EXACT_DIVISION_FIREWALL_PROVED

R1_TO_R10_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=NORMALIZED_LOCAL_DES_TRANSPORT_NUMERATOR_RESIDUE_MOD_ACTUAL_PPOWER__THRESHOLD_CRT_MEMBERSHIP

FACE_A_STATUS=KNOWN_B_E_COSET_WIDE_EXTINCT__GLOBAL_AVOID_NOT_PROVED__NO_HIT__H_CHANNEL_ELIMINATED
FACE_B_STATUS=EXACT_GATE_FORMULATED__NO_ACTIVE_FROZEN_CONTINUOUS_PROFILE__GLOBAL_AVOID_NOT_PROVED__NO_HIT

Q2_DES_EXACT_FORM=(T2P(rho2)-V)/((10*b1*P1)/d2star)=(10^(n2-1)-rho2)/M2=floor(10^(n2-1)/M2)
Q2_NUMERATOR=N2=T2P(rho2)-V
Q2_DENOMINATOR=D2=(10*b1*P1)/d2star
Q2_INTEGRAL=YES__N2=D2*((10^(n2-1)-rho2)/M2)

Q3_DES_EXACT_FORM=(T3(rho3)-V)/((10*K3)/d3star)=(10^(n3-1)-rho3)/M3=floor(10^(n3-1)/M3)
Q3_NUMERATOR=N3=T3(rho3)-V
Q3_DENOMINATOR=D3=(10*K3)/d3star
Q3_INTEGRAL=YES__N3=D3*((10^(n3-1)-rho3)/M3)

D2_STAR=gcd(C2,10*u)__NEW_SHARPENING_FROM_gcd(C2,h)=1_AND_gcd(C2,s*alpha)=1
D3_STAR=gcd(C3,10*K3)__DIVIDES_Q0

D2_STAR_PRIME_TYPE_DECOMPOSITION=2_COMPONENT__5_COMPONENT__ODD_U_COMPONENT; H_COMPONENT=EMPTY; B1_ONLY_COMPONENT=EMPTY
D3_STAR_PRIME_TYPE_DECOMPOSITION=ODD_p_EQ_1_MOD_4_DIVIDING_Q0_AND_C3__INCLUDING_POSSIBLE_5__NO_2

Q2_LOCAL_RESIDUES=FOR_p^e||d2star: f=vp(D2); Q2=(N2/p^f)*(D2/p^f)^(-1) mod p^e
Q3_LOCAL_RESIDUES=FOR_p^e||d3star: f=vp(D3); Q3=(N3/p^f)*(D3/p^f)^(-1) mod p^e

Q2_MOD_D2STAR=CRT_OF_EXACT_LOCAL_FORMULAS__SOURCE_WIDE_VALUE_NOT_LOCKED_BECAUSE_NORMALIZED_N2_RESIDUE_OPEN
Q3_MOD_D3STAR=CRT_OF_EXACT_LOCAL_FORMULAS__SOURCE_WIDE_VALUE_NOT_LOCKED_BECAUSE_NORMALIZED_N3_RESIDUE_OPEN

KAPPA2_ACTUAL=[Q2_DES]_d2star__B=0__E=0
KAPPA3_ACTUAL=[Q3_DES]_d3star__SOURCE_WIDE_OPEN__B_FACEB_REGRESSION=0_MOD_5

KAPPA2_CRITICAL=PROFILE_DEPENDENT_FROZEN_FORMULA__B=1__E=2
KAPPA3_CRITICAL=PROFILE_DEPENDENT_FROZEN_FORMULA

POSITIVE_K2_SET=GENERAL_FROZEN_THRESHOLD_SET__B=EMPTY__E=EMPTY
POSITIVE_K3_SET=GENERAL_FROZEN_THRESHOLD_SET__NO_ACTIVE_FROZEN_FACEB_PROFILE

QUOTIENT_RESIDUE_RIGIDITY=PARTIAL__LOCAL_DIVISION_EXACT__NORMALIZED_TRANSPORT_NUMERATOR_SOURCE_WIDE_RESIDUE_OPEN

KAPPA2_UPPER_BOUND=NO_SOURCE_WIDE_BOUND_BELOW_THRESHOLD__B=0__E=0_ACTUAL
KAPPA3_UPPER_BOUND=NO_SOURCE_WIDE_BOUND_BELOW_THRESHOLD

THRESHOLD_AVOIDANCE_FACE_A=YES_FOR_FROZEN_CONTINUOUS_B_E__UNIVERSAL_NO
THRESHOLD_AVOIDANCE_FACE_B=NOT_PROVED__NO_ACTIVE_FROZEN_PROFILE
THRESHOLD_AVOIDANCE_GLOBAL=NO

RHO2_ZERO_PROFILE_EXISTS=NOT_KNOWN__NONE_IN_FROZEN_AUTHORITATIVE_CENSUS
RHO3_ZERO_PROFILE_EXISTS=NOT_KNOWN__NO_ACTIVE_FROZEN_FACEB_PROFILE

MAXIMAL_K2_PROFILE_EXISTS=NOT_KNOWN__NONE_KNOWN_POSITIVE
MAXIMAL_K3_PROFILE_EXISTS=NOT_KNOWN__NONE_KNOWN_POSITIVE

POSITIVE_DES_QUOTIENT_HIT=NO
HIT_FACE=NONE
HIT_PROFILE=NONE

PLAIN_SURPLUS=NO_NEW_POSITIVE__B=-1635__E=-721518_ACTUAL
PLAIN_INTEGER_RADIAL_GATE_PASSED=NO
PLAIN_U=NONE

Q1_PROGRESSION_ACTIVE=NO_NEW_HIT
Q1_PROGRESSION_PASS=NOT_REACHED
COPRIMALITY_PASS=NOT_REACHED

SOURCE_INTEGER_U_FOUND=NO
SOURCE_INTEGER_U=NONE

COMMON_U_INTEGER_SUCCESSOR_GATE=OPEN_AT_NORMALIZED_LOCAL_DES_TRANSPORT_NUMERATOR_RESIDUE

DIGIT_SYNCHRONIZATION=NOT_REACHED
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

NEW_FIRST_FAILURE_GATE=NORMALIZED_LOCAL_DES_TRANSPORT_NUMERATOR_RESIDUE_MOD_p^e_FOR_ACTUAL_p^e_DIVIDING_DSTAR

POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NOT_PROVED

R11_SINGLE_LOCAL_QUOTIENT_GATE=YES__UNIFORM_LOCAL_THEOREM_SCHEMA_ON_ACTUAL_p^e_DIVIDING_DSTAR

R12_AUTHORIZED=YES
R12_ARCHITECTURE=ROUTE_D__NORMALIZED_LOCAL_DES_TRANSPORT_NUMERATOR_RESIDUE_ONLY
R12_SINGLE_ATTACK_TARGET=DETERMINE_(N_i/p^vp(D_i))_MOD_p^e_FOR_ACTUAL_SOURCE_SUPPORTED_p^e||d_i^*__THEN_CRT_AND_IMMEDIATE_THRESHOLD_VERDICT
```

---

## Provenance Ledger

Primary frozen provenance used in this report:

- `105_R10_DES_Endpoint_Coset_Lift_Index.md`: exact DES quotient transports, no-Bézout-loss theorem, \(d_i^*,M_i,\rho_i\), threshold sets, B/E coset verdicts.
- `105_R9_Endpoint_Quotient_Source_Successor.md`: exact post-PSDG census, endpoint transport provenance, B/E radial regression, finite-search theorem firewall.
- `105_R8_Common_U_Integer_Source_Fibre.md`: post-PSDG rank-one source fibre and canonical successor semantics.
- `105_R7C_Prescribed_Source_Divisor_Gate.md`: \(h\)-provenance and primitive source gcd facts.
- `105_R7D_Determinant_Packet_Source_GCD_Firewall.md`: B/E exact primitive/source fixtures.
- `strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`: primitive sphere, Full Smith–radial cancellation, \(C_2,C_3\) definitions.
- `strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`: Full Smith factorization and \(\gamma_0\)-allocation.
- `95_R8_g0_Smith_Reduced_Common_U_Three_Layer_Assault.md`: exact B/E state values.

The distinction between theorem and finite evidence is retained throughout.
