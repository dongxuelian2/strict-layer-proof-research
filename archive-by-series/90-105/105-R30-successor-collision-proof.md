# 105-R30 — Canonical Successor Collision: Exact Local Theorem and Global Audit

**Warning:** the filename is historical/requested. This file proves the exact q/source fusion and prime-cover collision criterion. It does **not** claim a global TC3 \(\Rightarrow\neg\)TC4 theorem, because that stronger statement was not proved.

---

## 1. R30 successor collision theorem

Fix a legal TC3-ready R26 architecture \(\mathfrak a\). Let

\[
I_q=[Q_-,Q_+]\cap\mathbb Z_{>0},
\]

let \(F\) be the R15 canonical forbidden factor, and let \(\mathcal U_0(\mathfrak a)\) be the finite q-independent source set defined in `105-R30-q-elimination-derivation.md`.

For each \(U\in\mathcal U_0\), define

\[
\Phi_{\mathfrak a}(U)
=
\#\{q\in I_q:\gcd(q,FU)=1\}.
\]

Then

\[
\boxed{
TC3+TC4
\iff
\exists U\in\mathcal U_0:\Phi_{\mathfrak a}(U)>0.
}
\]

Equivalently, define

\[
N_{30}(\mathfrak a)=\sum_{U\in\mathcal U_0}\Phi_{\mathfrak a}(U).
\]

Then

\[
\boxed{TC3+TC4\iff N_{30}(\mathfrak a)>0.}
\]

Therefore the exact collision certificate for one architecture is

\[
\boxed{N_{30}(\mathfrak a)=0.}
\]

---

## 2. Prime-cover certificate

For one source candidate \(U\), the following are equivalent:

1. no TC3 residual \(q\) is compatible with this TC4 source integer;
2. \(\Phi_{\mathfrak a}(U)=0\);
3. the entire q-window is covered by primes dividing \(FU\):

\[
\boxed{
I_q\subseteq\bigcup_{p\mid FU}p\mathbb Z.
}
\]

Thus an architecture dies exactly when this prime cover holds for every
\(U\in\mathcal U_0\).

This is the requested `TC3 coprimality makes TC4 successor fail` mechanism in its exact form. It is stronger and more precise than a density heuristic, but it is not automatically true on every architecture.

---

## 3. Canonical successor modulus after the fusion

R8 represents the fixed source-native progression by a finite residue set modulo a q-independent period \(P_0\). The R15 residual \(q\) changes only the primitive coprimality factor from

\[
\gcd(U,V_0)=1
\]

to

\[
\gcd(U,V_0q)=1.
\]

The literal R8 modulus may therefore be taken as

\[
M_U(q)=\operatorname{lcm}(P_0,V_0q).
\]

For the **truth value of coprimality**, only prime support matters, so an equivalent smaller period is

\[
\boxed{
M_U^{\rm rad}(q)=\operatorname{lcm}\bigl(P_0,\operatorname{rad}(V_0q)\bigr),
}
\]

with the fixed source-native selector encoded in the \(P_0\)-component.

The admissible residue set is

\[
\mathcal R_{\rm adm}(q)
=
\{r\bmod M_U^{\rm rad}(q):
 r\bmod P_0\in\mathcal R_0,
 \gcd(r,V_0q)=1\}.
\]

For a closed lower endpoint \(L\),

\[
U_{\min}(q)
=
\min_{r\in\mathcal R_{\rm adm}(q)}
\left[
 r+M_U^{\rm rad}(q)
 \left\lceil\frac{\max(L,1)-r}{M_U^{\rm rad}(q)}\right\rceil
\right].
\]

For an open lower endpoint, replace the bracketed successor by the strict floor version.

This fully expands the `canonical successor` black box.

---

## 4. Why monotonicity in numerical \(q\) is the wrong axis

The source interval \([L,R_{\rm src})\), its endpoint phases, and the fixed source-native progression do not move with the R15 residual \(q\). Numerical growth of \(q\) therefore does not shrink the source room.

What changes is only the set of newly forbidden primes in \(\gcd(U,q)=1\).

Hence two residual integers with the same added radical support have the same TC4 coprimality selector, while a larger integer can in principle have fewer or different forbidden small primes than a smaller integer. There is therefore no source-justified theorem of the form

\[
q_1<q_2\Longrightarrow U_{\min}(q_1)\le U_{\min}(q_2)
\]

available from the frozen architecture.

This kills the proposed continuous `q grows / room shrinks` strategy at the information-class level. The correct axis is prime-support cover, not numerical monotonicity.

---

## 5. Historical R29 support survivor autopsy

Frozen data:

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*)=(1,20,1,80),
\]

\[
(n,\delta,\rho,m)=(4,-2,2,1).
\]

Therefore

\[
n_3=4,
\quad n_2=2,
\quad m_2=1,
\quad m_3=4,
\quad k=1,
\quad g=0.
\]

Further,

\[
C_2=71,
\qquad C_3=4727,
\]

\[
g_0=20,
\quad \mu=4,
\quad R_1=8,
\]

\[
\lambda_z=2,
\quad \tau=1,
\quad \Lambda=4.
\]

Since

\[
4727=29\cdot163,
\]

\[
\boxed{
F=\operatorname{rad}(8\cdot71\cdot4727)
=2\cdot29\cdot71\cdot163
=671234.
}
\]

The exact denominator window is

\[
Z_-=50,
\qquad Z_+=9.
\]

Hence

\[
\boxed{Q_-=\left\lceil\frac{50}{4}\right\rceil=13,}
\]

\[
\boxed{Q_+=\left\lfloor\frac9{4}\right\rfloor=2.}
\]

So the shortest R30 certificate is simply

\[
\boxed{13>2.}
\]

Equivalently,

```text
R29_SUPPORT_SURVIVOR_TERMINAL_DEATH=TC3_Q_INTERVAL_EMPTY
TC3_INTEGER_Q_COUNT=0
TC4=NOT_ACTIVATED
```

For reference, the raw regular source interval that would have arisen from blocks 2 and 3 is

\[
L=\max\left(\frac{10}{71},\frac{1000}{4727}\right)
=\frac{1000}{4727},
\]

\[
R_{\rm src}=\min\left(\frac{100}{71},\frac{10000}{4727}\right)
=\frac{100}{71}.
\]

It contains the integer \(U=1\), but this is **not** a TC4 pass certificate because the frozen pipeline never activates TC4 once TC3 is empty. The exact terminal death is therefore interval emptiness on the residual denominator side, not a source-successor gap.

---

## 6. Counterexample search audit

R30 searched the frozen replay corpus rather than sweeping new primitive spheres indiscriminately. The inspected evidence classes include:

- R15 post-corridor / z-selector registries;
- R17 first corridor witness and its q-window state;
- R20/R29 first full support-stack survivor;
- R26 historical packet's complete finite predicate;
- R28 bounded TC1 reconnaissance up to its recorded bound;
- R8 frozen post-PSDG source-successor witness census.

No genuine tuple with both

\[
TC3=PASS,
\qquad
TC4=PASS
\]

was found in that replay corpus.

This is **not** promoted to a global theorem. In particular, R30 does not sign

```text
TC3_TC4_UNIVERSAL_INCOMPATIBILITY=FALSE
```

because no genuine pass tuple was found, and it does not sign

```text
TC3_TC4_GLOBAL_INCOMPATIBILITY=YES
```

because no all-architecture zero theorem was proved.

---

## 7. Global status of the collision

The R30 local collision theorem is exact:

\[
\boxed{
\text{architecture extinct at TC3+TC4}
\iff
N_{30}(\mathfrak a)=0.
}
\]

The missing global statement is precisely

\[
\boxed{
\forall\mathfrak a\text{ legal post-support},\quad N_{30}(\mathfrak a)=0.
}
\]

No weaker phrase such as “further study of TC3/TC4 is needed” is used in the archive. The missing object is the **architecture-uniform zero theorem for the q-free finite count \(N_{30}\)**, or a genuine architecture with positive count.
