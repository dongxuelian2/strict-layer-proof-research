# A1 J2 GRFC9 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** Global Square Factor-Pair × Root-Quotient Decimal Congruence × CQRF Unification  
**Inherited source:** `A1_J2_CQLRC8_Report.md`  
**Symbolic certificate:** `A1_J2_GRFC9_factor.py`  
**Dependency audit:** `A1_J2_GRFC9_dependency.py`  
**Targeted regression:** `A1_J2_GRFC9_search.py`  
**Equivalence certificate:** `A1_J2_GRFC9_equivalence_certificate.txt`  
**Master certificate:** `A1_J2_GRFC9_certificate.txt`  
**Regression ledger:** `A1_J2_GRFC9_survivors.tsv`

---

# Part I — Executive Status

\[
\boxed{\textbf{Full J2 OPEN}.}
\]

\[
\boxed{\textbf{GRFQE PROVED — in corrected form}.}
\]

\[
\boxed{h=0\ \textbf{OPEN globally}.}
\]

\[
\boxed{h=1\ \textbf{OPEN globally}.}
\]

\[
\boxed{h<0\ \textbf{/ Reverse-CQRF OPEN globally}.}
\]

The central result of this round is simultaneously positive and corrective.

The proposed factor-quotient identity is **algebraically exact**:

\[
\boxed{
A10^\ell\kappa^2-8uD_2\kappa+8\widehat\Omega=0,
\qquad
\widehat\Omega:=\frac{\widetilde F}{2K}\in\mathbf Q.
}
\tag{GRFQ}
\]

Moreover Layer S + Layer R can indeed be replaced by an exact square-root-free
positive-integer root condition.  However the resulting integer

\[
\boxed{\kappa}
\]

is **not a new small global-root quotient**.  The frozen root formula immediately gives

\[
\boxed{\kappa=a_1.}
\tag{K=A1}
\]

After clearing the decimal normalization,

\[
\boxed{
A G^2\kappa^2-8uKD_2\kappa+4\widetilde F=0
}
\tag{GRFQ-C}
\]

is exactly four times the inherited radial root quadratic

\[
AH^2a_1^2-2uKD_2a_1+\widetilde F=0,
\qquad H=G/2.
\]

Thus this round **does remove the explicit square root \(s=\sqrt{\Psi_\delta}\) from the terminal language**, but it does not create a new low-height coordinate.  The genuine gain is an exact, sign-unified, square-root-free root equation that can be spliced directly into the CQRF variables.

The strongest genuinely new terminal form is

\[
\boxed{
A G^2 M^2\kappa^2
-4uKEM\kappa
+\bigl(AY^2+2RE\bigr)=0,
\qquad M=q(q+4),
}
\tag{CQRF-GRFQ}
\]

where \(R,Y,E\) are pre-root deterministic functions of \((G,q,N,t)\).  This is the correct global replacement for the previous

\[
\text{one Hensel digit}+\text{one local square class}
\]

frontier.

No J2 Resonance Closure Certificate is issued.

---

# Part II — Dependency Audit

This audit corrects one important logical ambiguity accumulated in earlier rounds: a condition may be **safe to test before the square-root computation** without being a **pre-root theorem in provenance**.

| Identity / object | Logical status | Audit |
|---|---|---|
| RCE1–RCE3; reconstruction of \(a_3,Z,\mathcal X,D_2\) | Pre-root | frozen |
| \(\widetilde F=A\mathcal X^2+ZD_2\) | Pre-root | definition |
| root polynomial \(Q(T)=AH^2T^2-2uKD_2T+\widetilde F\) | Pre-root | coefficients defined without a root |
| \(\Psi_\delta=X_\delta^2-A\mathfrak b^2\widetilde F\) | Pre-root | definition |
| \(\Psi_\delta=s^2\) | Layer S | introduces \(s\) |
| \(AG\mathfrak b\mid2(X_\delta\pm s)\) | Layer S + R | root divisibility |
| \(a_1=2(X_\delta\pm s)/(AG\mathfrak b)\) | Full root | integral root |
| \(a_1\Lambda=\widetilde F\) | Full root | factor identity |
| \(AH^2a_1+\Lambda=2uKD_2\) | Full root | complementary factor |
| \(2K\mid\Lambda,\widetilde F\), \(\ell\ge3\) | **Root-necessary** | derived from integral-root decimal core |
| \(\widehat\Omega=\widetilde F/(2K)\in\mathbf Q\) | Pre-root rational | always definable |
| \(\Omega=\widetilde F/(2K)\in\mathbf Z\) | **Root-necessary** | equivalent to DCDC integrality gate |
| \(\Lambda=2K\lambda_0\) | Full root | post-root normalization |
| \(\lambda_0=uD_2-(A10^\ell/8)a_1\) | Full root | post-root normalization |
| \(\Omega=a_1\lambda_0\) | Full root | post-root product |
| \(\gcd(\lambda_0,10)=1\), \(\ell\ge4\) | Full root | post-root ten-unit theorem |
| \(\kappa\) from Layer R factor | Full root | and \(\kappa=a_1\) |
| \(\kappa\mid4\mathfrak a\Omega\) | Full root | integer divisibility only after \(\Omega\in\mathbf Z\) |
| RQDC | Full-root necessary | exact normalized root relation modulo decimal core |

Therefore the answer to the requested critical question is

\[
\boxed{
2K\mid\widetilde F\ \textbf{is not logically pre-root.}
}
\]

It is a **necessary consequence of an integral root** and hence a legitimate early rejection sieve.  But it may not be used as an independent assumption to prove that an integral root exists.

Likewise, the safe pre-root object is

\[
\boxed{
\widehat\Omega:=\frac{\widetilde F}{2K}\in\mathbf Q,
}
\]

not an a priori integer \(\Omega\).

This resolves the potential circularity in the prompt.

---

# Part III — Unified Root Kernel

Put

\[
\delta:=k-g,
\qquad
\mathfrak a:=10^{\max(\delta,0)},
\qquad
\mathfrak b:=10^{\max(-\delta,0)}.
\]

Then

\[
K=G\frac{\mathfrak a}{\mathfrak b},
\qquad
\boxed{\frac{G\mathfrak b}{\mathfrak a}=10^\ell}.
\]

Define

\[
X_\delta:=2u\mathfrak aD_2.
\]

The frozen square kernel is

\[
\boxed{
\Psi_\delta=X_\delta^2-A\mathfrak b^2\widetilde F.
}
\tag{PSI}
\]

The standard root discriminant satisfies

\[
\Delta_{\rm std}=
\left(\frac{G}{\mathfrak b}\right)^2\Psi_\delta.
\]

Hence Layer S is exactly

\[
\Psi_\delta=s^2,
\qquad s\in\mathbf Z_{\ge0}.
\]

The two formal roots are

\[
\boxed{
a_1=rac{2(X_\delta\pm s)}{AG\mathfrak b}.
}
\tag{ROOT}
\]

Therefore Layer R is

\[
\boxed{
AG\mathfrak b\mid2(X_\delta\pm s)
}
\tag{R}
\]

for at least one sign, with positive reconstructed root.

This normalization is exactly sign-unified for \(\delta>0,=0,<0\).

---

# Part IV — Global Factor Pair

Assume Layer S.  Then

\[
(X_\delta-s)(X_\delta+s)
=A\mathfrak b^2\widetilde F.
\tag{GF}
\]

Write

\[
F_-:=X_\delta-s,
\qquad
F_+:=X_\delta+s.
\]

For a genuine positive root state, both factors are nonnegative; in the nonzero-square case they are positive.  Layer R says one of them contains the complete divisor

\[
D:=\frac{AG\mathfrak b}{2}.
\]

This is the correct global factor allocation statement.

The factor gcd still obeys

\[
\gcd(F_-,F_+)\mid2X_\delta=4u\mathfrak aD_2,
\]

but this round does **not** prove a uniform small-factor exclusion.  No false theorem of the form

\[
F_-<D
\]

is claimed.

---

# Part V — Root-Factor Quotient and GRFQ

Choose the Layer-R factor and define

\[
\boxed{
\kappa:=\frac{2(X_\delta+\varepsilon s)}{AG\mathfrak b}
\in\mathbf Z_{>0},
\qquad \varepsilon\in\{\pm1\}.
}
\]

Then

\[
F_1:=X_\delta+\varepsilon s
=\frac{AG\mathfrak b}{2}\kappa.
\tag{F1}
\]

Using the factor product,

\[
F_2
=\frac{A\mathfrak b^2\widetilde F}{F_1}
=\frac{2\mathfrak b\widetilde F}{G\kappa}.
\]

With \(K=G\mathfrak a/\mathfrak b\) and the rational pre-root quotient

\[
\widehat\Omega=\frac{\widetilde F}{2K},
\]

this becomes

\[
\boxed{
F_2=\frac{4\mathfrak a\widehat\Omega}{\kappa}.
}
\tag{F2}
\]

Thus the candidate F2 formula is exact.  If DCDC is known so that \(\Omega\in\mathbf Z\), it additionally gives the integer divisor relation

\[
\kappa\mid4\mathfrak a\Omega.
\]

Now \(F_1+F_2=2X_\delta\) yields

\[
\boxed{
\frac{A10^\ell}{2}\kappa
+\frac{4\widehat\Omega}{\kappa}
=4uD_2.
}
\tag{GRFQ-1}
\]

Equivalently,

\[
\boxed{
A10^\ell\kappa^2-8uD_2\kappa+8\widehat\Omega=0.
}
\tag{GRFQ-Q}
\]

So C1 — “GRFQ formula as written is exact” — is **PROVED**, with the dependency correction that \(\widehat\Omega\) is rational pre-root and integer only after DCDC/root-core.

## 5.1 The decisive identification \(\kappa=a_1\)

Compare the definition of \(\kappa\) with the frozen root formula (ROOT):

\[
\boxed{\kappa=a_1.}
\]

This is not a later theorem requiring BRANCH.  It is immediate from the definitions.

Clearing GRFQ gives

\[
K\cdot\text{(GRFQ-Q)}
=
AG^2\kappa^2-8uKD_2\kappa+4\widetilde F.
\]

Since \(H=G/2\),

\[
\boxed{
AG^2\kappa^2-8uKD_2\kappa+4\widetilde F
=4\left(AH^2\kappa^2-2uKD_2\kappa+\widetilde F\right).
}
\]

Therefore GRFQ is exactly the inherited root quadratic in new notation.

Consequences:

- \(\kappa=1\) uniformly: **DISPROVED**.
- fixed finite \(\kappa\)-alphabet: **DISPROVED**.
- “\(\kappa\) is a new small quotient”: **DISPROVED**.
- explicit square-root variable \(s\) can be eliminated: **PROVED**.

The frozen DRL becomes

\[
\boxed{
\kappa=a_1>\frac{AG}{10}.
}
\tag{KLOW}
\]

So the actual root variable is necessarily large, not small.

---

# Part VI — GRFQE Converse Audit

The corrected equivalence can be stated without \(\Omega\) at all.

## Theorem — Global Root-Factor Quotient Equivalence, corrected

Under the frozen pre-root terminal conditions,

\[
\boxed{
\text{Layer S + Layer R}
\iff
\exists\kappa\in\mathbf Z_{>0}:
AH^2\kappa^2-2uKD_2\kappa+\widetilde F=0.
}
\tag{GRFQE}
\]

### Forward

Layer S + R gives a sign \(\varepsilon\) and

\[
\kappa=\frac{2(X_\delta+\varepsilon s)}{AG\mathfrak b}.
\]

This is precisely the frozen positive integral root \(a_1\), hence it satisfies the root polynomial.

### Reverse

Assume \(\kappa>0\) is an integer root.  Put

\[
D:=\frac{AG\mathfrak b}{2},
\qquad
F_1:=D\kappa,
\qquad
F_2:=2X_\delta-F_1.
\]

Using \(K=G\mathfrak a/\mathfrak b\) and the root equation gives exactly

\[
F_1F_2=A\mathfrak b^2\widetilde F.
\]

Since \(\widetilde F>0\) on a legal terminal cell and \(F_1>0\), also \(F_2>0\).  Define

\[
s:=|F_1-X_\delta|=\frac{|F_1-F_2|}{2}.
\]

No extra parity assumption is needed: \(D\), \(\kappa\), and \(X_\delta\) are integers.  Then

\[
\begin{aligned}
s^2
&=(F_1-X_\delta)^2\\
&=X_\delta^2-F_1F_2\\
&=X_\delta^2-A\mathfrak b^2\widetilde F\\
&=\Psi_\delta.
\end{aligned}
\]

Thus Layer S holds.  Moreover \(F_1=X_\delta\pm s\) and

\[
2F_1=AG\mathfrak b\,\kappa,
\]

so Layer R holds.

### \(s=0\)

If \(s=0\), then \(F_1=F_2=X_\delta\); both root signs coincide and the same proof applies.  No exceptional missing chamber remains.

Hence C2 is **PROVED** in this corrected denominator-free form.

The important interpretation is:

\[
\boxed{
\text{GRFQE removes the square-root variable, but does not reduce the root dimension.}
}
\]

---

# Part VII — Root-Quotient Decimal Congruence

Whenever the root-necessary DCDC condition makes

\[
\Omega:=\frac{\widetilde F}{2K}\in\mathbf Z,
\]

GRFQ gives the **exact equality**

\[
\boxed{uD_2\kappa-\Omega
=\frac{A10^\ell}{8}\kappa^2.
}
\tag{RQ-EXACT}
\]

Therefore for \(\ell\ge3\),

\[
\boxed{
\frac{10^\ell}{8}
\mid uD_2\kappa-\Omega.
}
\tag{RQDC}
\]

The congruence will be denoted by (RQDC) below; no new auxiliary symbol is introduced.

## 7.1 Five-adic part

Frozen legality gives

\[
\gcd(uD_2,10)=1.
\]

Hence \(uD_2\) is invertible modulo \(5^\ell\), and

\[
\boxed{
\kappa\equiv (uD_2)^{-1}\Omega\pmod{5^\ell}.
}
\tag{RQDC5}
\]

Thus C6 — “RQDC5 uniquely determines \(\kappa\)” — is **PROVED at the residue-class level**.

## 7.2 Two-adic part

Because \(uD_2\) is odd,

\[
\boxed{
\kappa\equiv (uD_2)^{-1}\Omega
\pmod{2^{\ell-3}}.
}
\tag{RQDC2}
\]

Combining the two by CRT actually gives a unique class modulo the whole modulus

\[
\boxed{
\kappa\equiv\kappa_0
\pmod{10^\ell/8}.
}
\tag{RQDC10}
\]

This is stronger than treating the 2- and 5-parts separately.

But there is a crucial limitation: since \(\kappa=a_1>AG/10\), \(\kappa\) is not known to be smaller than the modulus in the full frontier.  Therefore uniqueness of a residue class is **not** uniqueness of the integer root.

## 7.3 RQDC is not independent of the old root factor

Under full root,

\[
\Omega=a_1\lambda_0,
\qquad
\lambda_0=uD_2-\frac{A10^\ell}{8}a_1.
\]

Since \(\kappa=a_1\), RQ-EXACT is simply

\[
a_1uD_2-a_1\lambda_0
=\frac{A10^\ell}{8}a_1^2.
\]

So RQDC is a powerful **root-residue sieve**, but not a logically new equation beyond the normalized root factor system.

---

# Part VIII — \(\kappa\) Bounds, Support, and BRANCH Audit

GRFQ with positive companion factor gives

\[
\boxed{
\kappa<\frac{8uD_2}{A10^\ell}.
}
\tag{KB}
\]

At the same time DRL gives

\[
\boxed{
\kappa>\frac{AG}{10}.
}
\]

The inherited negative radial estimate gives only a scale bound for \(D_2\) large enough that these inequalities do not force a universal constant alphabet.  No theorem \(\kappa\le C\) is obtained.

### Support

After DCDC,

\[
\kappa\mid4\mathfrak a\Omega
\]

is valid, but because \(\kappa=a_1\) and \(\Omega=a_1\lambda_0\), this divisibility is automatic up to the displayed factor and does not itself rigidify the root.

### BRANCH

Comparing

\[
\Omega
=\kappa uD_2-\frac{A10^\ell}{8}\kappa^2
\]

with

\[
\Omega
=a_1uD_2-\frac{A10^\ell}{8}a_1^2
\]

gives

\[
\boxed{
(\kappa-a_1)
\left(
u D_2-\frac{A10^\ell}{8}(\kappa+a_1)\right)=0
}
\]

This factorization is exact, but it is **not a new theorem**.  It is the standard difference-of-values/Vieta relation for the same quadratic.  Since the selected Layer-R quotient is already \(\kappa=a_1\), the first branch is tautological; the second branch merely describes the other quadratic root when it exists.

Therefore C8 — “\(\kappa=a_1\) is a new nontrivial theorem from BRANCH” — is **DISPROVED as an interpretation**.  The equality itself is true earlier and more directly.

No second-branch extinction is claimed.

---

# Part IX — \(h=0\) Campaign

At \(h=0\),

\[
\delta=0,
\qquad
\mathfrak a=\mathfrak b=1,
\qquad
K=G,
\qquad
\ell=g.
\]

GRFQE becomes

\[
\boxed{
AH^2\kappa^2-2uGD_2\kappa+\widetilde F=0.
}
\]

or

\[
\boxed{
AG\kappa^2-8uD_2\kappa+8\widehat\Omega=0.
}
\]

after the normalized form.

The inherited exact boundary census through \(g\le1200\) had

\[
79\text{ DCDC/root-layer pseudo-cells},
\qquad
0\text{ global square states}.
\]

In the corrected GRFQE language this means exactly

\[
\boxed{
79\text{ DCDC cells},\qquad0\text{ positive integer }\kappa\text{ roots}.
}
\]

So GRFQE successfully explains the old square gate without an explicit square-root search, but does not promote the finite diagnostic into an infinite theorem.

Therefore

\[
\boxed{h=0\textbf{ remains OPEN globally}.}
\]

The previous boundary norm congruence remains auxiliary only.

---

# Part X — \(h=1\) Campaign and the Two \(q=11\) Regressions

Fix the historical fibre

\[
(q,h,\alpha,t)=(11,1,152510,31).
\]

## 10.1 Regression A: \(g=471\)

The exact state passes the full pre-root legality package and

\[
2K\mid\widetilde F.
\]

Hence \(\Omega\in\mathbf Z\).  Its root kernel satisfies

\[
\Psi_1\equiv8\pmod{11},
\]

and \(8\) is a quadratic nonresidue modulo \(11\).  Therefore no integer \(s\) exists, equivalently by GRFQE

\[
\boxed{\text{there is no positive integer }\kappa.}
\]

In the new pipeline its first death gate is

\[
\boxed{\texttt{KAPPA_EXISTENCE / GLOBAL_ROOT}.}
\]

The earlier mod-11 square test is simply a cheap certificate of failure of that global integer-root equation.

## 10.2 Regression B: \(g=63501\)

This state is more important.  It passes DCDC and all previously used structural odd-prime square tests.  Exact structural residues are

\[
\begin{array}{c|cccccc}
p&3&7&11&13&73&383\\ \hline
\Psi_1\bmod p&1&2&5&0&72&331
\end{array}
\]

and every entry is a residue or zero.

The new targeted regression independently certifies

\[
\boxed{
\Psi_1\equiv12\pmod{17},
}
\]

where \(12\) is a quadratic nonresidue modulo \(17\).  Hence \(\Psi_1\) is not an integer square and, equivalently,

\[
\boxed{
\text{GRFQ has no positive integer }\kappa.
}
\]

Thus the requested historical pseudo-survivor is explained exactly:

\[
\boxed{
\textbf{first death gate = global integer root / }\kappa\textbf{-existence}.
}
\]

The prime 17 is used **only as an exact regression certificate**, not as a proposed new structural killer-prime strategy.

An additional diagnostic observation is that both \(g=471\) and \(g=63501\) produce the same 12-digit projection of the RQDC residue class,

```text
430881980803  (mod 10^12).
```

So RQDC by itself can survive deep along the same quotient fibre.  This further confirms that the decisive equation is the full integer root polynomial, not one decimal suffix alone.

Therefore

\[
\boxed{h=1\textbf{ remains OPEN globally}.}
\]

---

# Part XI — Reverse-CQRF and Zero-Tail Audit

For \(\delta=-r<0\),

\[
\mathfrak a=1,
\qquad
\mathfrak b=10^r,
\qquad
K=G/10^r,
\qquad
10^\ell=G10^r.
\]

The derivation of GRFQE uses only

\[
K=G\mathfrak a/\mathfrak b,
\qquad
10^\ell=G\mathfrak b/\mathfrak a,
\]

and the frozen root quadratic.  Hence it is completely sign-unified:

\[
\boxed{
AH^2\kappa^2-2uKD_2\kappa+\widetilde F=0
}
\]

for high tail, boundary, and reverse tail alike.

Therefore C9 is answered precisely:

- **GRFQE itself covers the low-\(k\) zero-tail ray.**
- **Reverse-CQRF tail parametrization does not automatically cover zero-tail**, because the nonzero-tail equation defining \(\alpha\) is absent there.

So zero-tail is no longer exceptional at the **root algebra** level, but remains exceptional in **CQRF preprocessing**.

No reverse closure is obtained:

\[
\boxed{h<0\textbf{ remains OPEN globally}.}
\]

---

# Part XII — CQRF Splice

This is the strongest genuinely reusable formula of the round.

Set

\[
M:=q(q+4),
\qquad
R:=At-2N,
\]

\[
Y:=R+uNM,
\]

\[
E:=uq\bigl((G-1)t-qN\bigr)+GY.
\]

The frozen exact reconstruction gives

\[
Z=\frac RM,
\qquad
\mathcal X=\frac{Y}{2M},
\qquad
D_2=\frac{E}{2M},
\]

and

\[
\boxed{
4M^2\widetilde F=P:=AY^2+2RE.
}
\tag{P}
\]

Substitute these directly into the cleared GRFQ equation

\[
AG^2\kappa^2-8uKD_2\kappa+4\widetilde F=0.
\]

Multiplying by \(M^2\) gives

\[
\boxed{
A G^2 M^2\kappa^2
-4uKEM\kappa
+P=0,
\qquad
P=AY^2+2RE.
}
\tag{CQRF-GRFQ}
\]

This identity has no square root and no free \(Z,\mathcal X,D_2\).  Its coefficients are deterministic functions of

\[
(G,q,N,t),
\]

and after a nonzero CQRF tail substitution

\[
N=\frac{\alpha u+e}{d_\delta c(q)},
\]

it becomes an exact equation in the cyclotomic outer variable and the actual root digit \(\kappa=a_1\).

The pre-root rational quotient also has the explicit form

\[
\boxed{
\widehat\Omega
=\frac{P}{8KM^2}.
}
\]

Thus DCDC is

\[
\boxed{8KM^2\mid P}
\]

in the current \(\ell\ge6\) regime, and once this root-necessary sieve passes, RQDC becomes a decimal residue condition on \(\kappa\).

This is the correct CQRF × global-root splice.

---

# Part XIII — Computational Regression

This round deliberately does not enlarge the \(g\)-ceiling.  It targets mechanism validation.

## 13.1 Exact new targeted rows

| state | DCDC | \(\Omega\in\mathbb Z\) | global square | positive integer \(\kappa\) | first death |
|---|---:|---:|---:|---:|---|
| \(q=11,g=471,h=1\) | PASS | PASS | FAIL | 0 | \(\kappa\)-existence/global root |
| \(q=11,g=63501,h=1\) | PASS | PASS | FAIL | 0 | \(\kappa\)-existence/global root |

The first is certified by \(\Psi\equiv8\pmod{11}\); the second by \(\Psi\equiv12\pmod{17}\).

## 13.2 Inherited \(h=0\) replay

| \(q\) | tail-integral | reconstructed | linear-legal | DCDC | positive integer \(\kappa\) |
|---:|---:|---:|---:|---:|---:|
|7|221288|2900|370|28|0|
|11|8713715|264156|10214|44|0|
|17|413750|1164|32|5|0|
|19|437896|969|21|2|0|

Aggregate:

\[
\boxed{
\texttt{H0\_DCDC}=79,
\qquad
\texttt{H0\_KAPPA\_SURVIVOR}=0
}
\]

in the inherited exact \(g\le1200\) diagnostic.

These finite counts remain diagnostic only.

## 13.3 Gate interpretation

Because GRFQE is exact,

\[
\boxed{
\texttt{LAYER\_S+R survivor count}
=
\texttt{positive integer GRFQ-root count}.
}
\]

This is now a theorem, not merely a regression expectation.

---

# Part XIV — Counterexample / Conjecture Ledger

| Conjecture | Verdict |
|---|---|
| C1 GRFQ formula exact | **PROVED**, with rational/integer \(\Omega\) dependency correction |
| C2 GRFQ equivalent to Layer S+R | **PROVED** in denominator-free corrected form |
| C3 \(\kappa=1\) uniformly | **DISPROVED**; \(\kappa=a_1>AG/10\) |
| C4 fixed finite \(\kappa\)-alphabet | **DISPROVED** for same reason |
| C5 small-factor Layer-R branch uniformly impossible | **OPEN** |
| C6 RQDC5 uniquely determines \(\kappa\) | **PROVED modulo \(5^\ell\)**, not as an absolute integer |
| C7 \(v_5(D_2)\) uniformly bounded | **PROVED strongly on legal states: \(v_5(D_2)=0\)** from ten-unit legality |
| C8 \(\kappa=a_1\) is a new BRANCH theorem | equality **TRUE**, novelty **FALSE/tautological** |
| C9 GRFQ covers low-\(k\) zero-tail | **PROVED at root-algebra level** |
| C10 \(h=0\) pure global-factor closure | **OPEN** |

Additional falsifications:

- “GRFQ introduces a new small global variable”: false.
- “RQDC alone kills the \(g=63501\) state”: false as a demonstrated mechanism; a deep decimal residue survives while the full root equation fails.
- “DCDC is pre-root in logical provenance”: false; it is root-necessary but operationally testable early.

---

# Part XV — Closure Audit

### \(\delta>0\)

GRFQE applies.  Frozen \(q=1,h\ge1\) closure remains.  Genuine \(q>1\) high tail remains globally open.

### \(\delta=0\)

GRFQE applies.  Boundary zero-tail is absent for \(q>1\) by the inherited bound; exact \(g\le1200\) diagnostic has 79 DCDC and zero integer roots.  Infinite closure not proved.

### \(\delta<0\)

GRFQE applies without change.  Reverse nonzero-tail CQRF remains available under its frozen valuation hypotheses.  Low zero-tail remains separately preprocessed but uses the same root equation.

### \(q=1\)

High tail closed.  No illicit promotion to all \(q=1\) chambers is made.

### \(q>1\)

Open variable-\(q\) mass remains.

### Both root signs

Both are included.  GRFQE reconstructs the sign from whether

\[
D\kappa-X_\delta
\]

is positive or negative.

### \(s=0\)

Included: both root signs coincide; no parity problem.

### Decimal support

On full root, \(\lambda_0\) remains a ten-unit for \(\ell\ge4\).  \(\Omega\) itself is not assumed ten-unit.

### Primitive gcd

Not weakened.  GRFQE ends at the integral root gate; primitive residues/gcd remain later reconstruction requirements.

### Common-\(U\)

Not discarded.  Since \(\kappa=a_1=UC_1\), the root variable already carries the actual common radial scale.

### Closed deficiency layers

\[
\ell=1,2,3,4,5
\]

remain frozen closed.  No layer-by-layer extension is substituted for the requested uniform \(\ell\ge6\) work.

### Full J2

\[
\boxed{\textbf{OPEN}.}
\]

---

# Part XVI — New Frontier

The requested dream endpoint

\[
\text{small }\kappa
+\text{ huge decimal congruence}
\]

is not correct because

\[
\boxed{\kappa=a_1>AG/10.}
\]

The corrected terminal obstruction is instead

\[
\boxed{
\textbf{actual integral root digit }\kappa=a_1
\quad\times\quad
\textbf{one exact CQRF root polynomial}
\quad\times\quad
\textbf{one huge decimal residue class}.
}
\]

Concretely:

\[
\boxed{
A G^2 M^2\kappa^2
-4uKEM\kappa
+AY^2+2RE=0,
}
\tag{NEW-GLOBAL}
\]

with

\[
\boxed{
\kappa>\frac{AG}{10},
}
\]

and, once the root-necessary DCDC sieve passes,

\[
\boxed{
\kappa\equiv
(uD_2)^{-1}\Omega
\pmod{10^\ell/8}.
}
\tag{NEW-DECIMAL}
\]

The old primitive root residues may be appended:

\[
\boxed{
\kappa^2\equiv Z^2\pmod u,
\qquad
K\kappa\equiv-Z\pmod A.
}
\]

After nonzero CQRF substitution, \(N\) itself is affine in \(u\).  Hence the next genuinely new theorem should attack the **integer-root polynomial and the decimal residue simultaneously**, rather than returning to another fixed-prime square-class stack.

A particularly promising corrected target is:

\[
\boxed{
\textbf{CQRF integer-root collision:}
\quad
Q_{q,\delta,\alpha,t}(u,\kappa)=0
\quad\text{and}\quad
\kappa\equiv\kappa_0\pmod{10^\ell/8}
}
\]

with the actual-digit lower bound \(\kappa>AG/10\) and the two primitive root residues.  This is strictly more global than the previous one-Hensel-digit/local-square frontier.

No J2 closure certificate is generated.

---

# File Audit

The following files are generated and checked in this round:

```text
A1_J2_GRFC9_Report.md
A1_J2_GRFC9_factor.py
A1_J2_GRFC9_dependency.py
A1_J2_GRFC9_search.py
A1_J2_GRFC9_certificate.txt
A1_J2_GRFC9_equivalence_certificate.txt
A1_J2_GRFC9_survivors.tsv
```

No `A1_J2_Resonance_Closure_Certificate.md` is generated because J2 remains open.

FINAL_REPORT_FILE: A1_J2_GRFC9_Report.md

FACTOR_SYMBOLIC_FILE: A1_J2_GRFC9_factor.py

DEPENDENCY_FILE: A1_J2_GRFC9_dependency.py

COMPUTATION_FILE: A1_J2_GRFC9_search.py

CERTIFICATE_FILE: A1_J2_GRFC9_certificate.txt

EQUIVALENCE_CERTIFICATE_FILE: A1_J2_GRFC9_equivalence_certificate.txt

SURVIVOR_FILE: A1_J2_GRFC9_survivors.tsv

J2_CLOSURE_CERTIFICATE_FILE: NOT_GENERATED_BECAUSE_OPEN
