# J2-55-R4 — Content-Deflated Complementary Factor × Global Euclidean-Defect CRT × Exact Product Collision Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第四轮 / 统一终端线第十四轮  
**Frozen primary source:** `J2-55-R3-Decimal-Residual-Collision-Report.md`  
**Inherited support:** `A1_J2_DCDC5_Report.md`, `A1_J2_CQLRC8_Report.md`, `A1_J2_GRFC9_Report.md`, `A1_J2_PRCC10_Report.md`, `J2-55-R1-A-Root-Lift-Report.md`, `J2-55-R2-USquare-Carry-Collision-Report.md`  
**New symbolic audit:** `J2-55-R4-EuclideanDefect-symbolic.py`  
**New exact replay/search:** `J2-55-R4-EuclideanDefect-search.py`  
**New ledger:** `J2-55-R4-EuclideanDefect-survivors.tsv`  
**New certificate:** `J2-55-R4-EuclideanDefect-certificate.txt`

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

\[
\boxed{\delta>0\ \textbf{OPEN globally}}
\]

\[
\boxed{\delta=0\ \textbf{OPEN globally}}
\]

\[
\boxed{\delta<0\ \textbf{OPEN globally}}
\]

No valid proof of

\[
J=2\Longrightarrow\varnothing
\]

has been obtained, so **no** `J2-Resonance-Closure-Certificate.md` is issued.

This round nevertheless proves the main structural target of the campaign and removes the regular/singular root-multiplicity split from the terminal chart.

The principal new theorem is:

\[
\boxed{\textbf{Global Euclidean-Defect One-Candidate Theorem}.}
\]

For every actual-root-eligible J2 structural profile, after DCDC there is a single structural Euclidean division and the primitive \(A\)-root plus decimal root select **at most one** Euclidean defect \(s\), hence at most one actual-root candidate.  This statement is independent of whether

\[
d=\gcd(A,D_2)=1,
\qquad 1<d<A,
\qquad d=A.
\]

Thus the old terminal coordinates

- regular \(A^3\) carry,
- singular \(A^2\)-fibres,
- singular content index \(m\),
- U-cell \(+j\) multiplicity bookkeeping,

are no longer required as root coordinates.  They survive only as optional verification gates.

The second global theorem is the high-tail defect collapse:

\[
\boxed{\delta\ge1\Longrightarrow s=0}
\]

for every live high-tail actual root.  The frozen \(q=1,\delta\ge1\) chamber was already closed, and in the live \(q>1\) chamber the new defect bound is strictly below \(1\).

The boundary also acquires an absolute defect alphabet:

\[
\boxed{\delta=0\Longrightarrow 0\le s\le146.}
\]

For the genuine \(q>1\) boundary, where \(q\ge7\), this sharpens immediately to

\[
\boxed{0\le s\le20.}
\]

The strongest finite result is the complete replay of the inherited boundary corpus.  The same 79 DCDC states are reproduced.  Four die at primitive gcd, and **all remaining 75/75 die immediately because the unique CRT defect satisfies**

\[
\boxed{s_\star\ge\mathcal B.}
\]

In particular, the six historical \(d=3\) singular states at

\[
q=11,
\qquad
 g\in\{259,359,435,481,669,1025\}
\]

all die at the single unified defect-bound gate.  No \(A^2\)-fibre, \(j\)-carry, U-cell, or singular content enumeration is required.

A new reverse diagnostic also reaches the requested layer genuinely: in the targeted nonzero Reverse-CQRF slice \(r=1\), \(g\le12\), the exact search finds **50 post-DCDC states**.  Six die at primitive gcd and the remaining **44/44 die at the same unique defect-bound gate**.  This replaces the old useless pre-DCDC reverse pseudo-state as a diagnostic.

However, these computations are finite diagnostics.  No uniform proof of either

\[
\delta=0\Longrightarrow\varnothing
\]

or

\[
\delta<0\Longrightarrow\varnothing
\]

is claimed.

The new exact frontier is therefore:

\[
\boxed{
\textbf{one structural Euclidean division}
+
\textbf{one CRT-selected defect }s_\star
+
\textbf{one exact product equality}.
}
\]

A further simplification discovered in this round is stronger than the requested content-deflated chart: after the content audit, the Euclidean quotient is **content invariant**, and the final exact product can be written with no \(d\) at all.  If

\[
uD_2=A\mathfrak M\mu+\varrho,
\qquad
0<\varrho<A\mathfrak M,
\]

then

\[
\boxed{\varrho=d\rho,\qquad \gcd(\varrho,A\mathfrak M)=d,}
\]

and the actual-root equation is equivalently

\[
\boxed{
\Omega=(\mu-s)(\varrho+A\mathfrak M s).
}
\tag{RAW-PRODUCT}
\]

Hence polynomial singularity is literally reduced to recoverable content metadata; it no longer appears in the preferred terminal product equation.

---

# Part II — R3 Frozen Ledger and Notation Disambiguation

Freeze

\[
G=10^g,
\qquad
K=10^k,
\qquad
L=10^\ell,
\qquad
k=2g-\ell,
\]

\[
uq=G+1,
\qquad
A=2u+1,
\qquad
\gcd(A,10)=1.
\]

This report uses

\[
\boxed{\mathfrak M:=\frac{L}{8}}
\]

for the decimal modulus and

\[
\boxed{M_q:=q(q+4)}
\]

for the RCE/CQRF denominator.  They are never conflated.

The tail offset is

\[
\boxed{\delta:=k-g=g-\ell.}
\]

Thus

\[
\delta>0\iff k>g,
\qquad
\delta=0\iff k=g,
\qquad
\delta=-r<0\iff r=g-k=\ell-g>0.
\]

The frozen radial root data are

\[
\widetilde F=A\mathcal X^2+ZD_2,
\]

\[
Q(x)=AH^2x^2-2uKD_2x+\widetilde F,
\qquad H=G/2.
\]

DCDC gives the actual-root necessity

\[
\boxed{2K\mid\widetilde F}
\]

and therefore

\[
\boxed{\Omega:=\frac{\widetilde F}{2K}\in\mathbb Z.}
\]

R3 normalized the exact root equation to

\[
\boxed{
\mathscr R(x)=A\mathfrak Mx^2-uD_2x+\Omega
=\Omega-x\lambda_0(x),
}
\]

where

\[
\boxed{\lambda_0(x):=uD_2-A\mathfrak Mx.}
\]

Thus

\[
\boxed{x\text{ is an actual root}\iff\Omega=x\lambda_0(x).}
\]

The actual root interval is

\[
\boxed{
\frac{AG}{10}<x<\frac{8uD_2}{AL},
}
\]

and the upper endpoint is exactly \(\lambda_0(x)>0\).

The two primitive/decimal residues used later are

\[
\boxed{x\equiv r_A:=-K^{-1}Z\pmod A}
\]

and

\[
\boxed{x\equiv x_{10}\pmod{\mathfrak M}},
\qquad
x_{10}\equiv (uD_2)^{-1}\Omega\pmod{\mathfrak M}.
\]

The latter is equivalent to the sharp version below because \(d\) is a ten-unit.

---

# Part III — CDF-1: Exact Content Deflation

Define

\[
\boxed{d:=\gcd(A,D_2)},
\]

and write

\[
\boxed{A=de,\qquad D_2=dD^\sharp,}
\]

so

\[
\boxed{\gcd(e,D^\sharp)=1.}
\]

Then

\[
\begin{aligned}
\widetilde F
&=A\mathcal X^2+ZD_2\\
&=d\left(e\mathcal X^2+ZD^\sharp\right).
\end{aligned}
\]

Define

\[
\boxed{
\widetilde F^\sharp:=e\mathcal X^2+ZD^\sharp.
}
\]

Hence

\[
\boxed{\widetilde F=d\widetilde F^\sharp.}
\tag{CDF-1}
\]

Because \(d\mid A\) and \(\gcd(A,10)=1\),

\[
\boxed{\gcd(d,2K)=1.}
\]

DCDC gives

\[
2K\mid d\widetilde F^\sharp.
\]

Euclid's lemma therefore yields

\[
\boxed{2K\mid\widetilde F^\sharp.}
\]

Define

\[
\boxed{
\Omega^\sharp:=\frac{\widetilde F^\sharp}{2K}\in\mathbb Z.
}
\]

Then

\[
\boxed{\Omega=d\Omega^\sharp.}
\tag{CDF-OMEGA}
\]

This is an exact theorem, not a regular-branch assumption.

---

# Part IV — CDF-2: Deflated Root Polynomial and Complementary Factor

Substituting

\[
A=de,\qquad D_2=dD^\sharp,\qquad \Omega=d\Omega^\sharp
\]

into \(\mathscr R\) gives

\[
\boxed{\mathscr R(x)=d\mathscr R^\sharp(x),}
\]

with

\[
\boxed{
\mathscr R^\sharp(x)
=e\mathfrak Mx^2-uD^\sharp x+\Omega^\sharp.
}
\tag{R-SHARP}
\]

Define

\[
\boxed{
\lambda^\sharp(x):=uD^\sharp-e\mathfrak Mx.
}
\]

Then

\[
\boxed{
\mathscr R^\sharp(x)
=\Omega^\sharp-x\lambda^\sharp(x).
}
\tag{FACTOR-SHARP}
\]

Therefore

\[
\boxed{
x\text{ actual root}
\iff
\Omega^\sharp=x\lambda^\sharp(x).
}
\tag{PRODUCT-SHARP}
\]

and the root interval implies

\[
\boxed{\lambda^\sharp(x)>0.}
\]

Moreover

\[
\lambda^\sharp\equiv uD^\sharp\pmod{e\mathfrak M}.
\]

We have

\[
\gcd(u,e)=1,
\qquad
\gcd(D^\sharp,e)=1,
\]

and the inherited ten-unit conditions give

\[
\gcd(uD^\sharp,\mathfrak M)=1.
\]

Hence

\[
\boxed{
\gcd(uD^\sharp,e\mathfrak M)=1,
}
\]

so every actual complementary factor obeys

\[
\boxed{
\gcd(\lambda^\sharp,e\mathfrak M)=1.
}
\tag{LAM-UNIT}
\]

---

# Part V — EDF-0: Content-Invariant Euclidean Quotient

The prompt asks to divide

\[
uD^\sharp
\]

by

\[
e\mathfrak M.
\]

Do so:

\[
\boxed{
uD^\sharp=e\mathfrak M\mu+\rho,}
\]

with

\[
\boxed{1\le\rho<e\mathfrak M.}
\]

The lower bound \(\rho\ne0\) follows from

\[
\gcd(uD^\sharp,e\mathfrak M)=1
\]

and \(e\mathfrak M>1\).

Now multiply the Euclidean division by \(d\):

\[
\boxed{
uD_2=A\mathfrak M\mu+\varrho,}
\tag{RAW-ED}
\]

where

\[
\boxed{\varrho:=d\rho.}
\]

Thus

\[
\boxed{
\mu
=\left\lfloor\frac{uD^\sharp}{e\mathfrak M}\right\rfloor
=\left\lfloor\frac{uD_2}{A\mathfrak M}\right\rfloor.
}
\tag{MU-INVARIANT}
\]

This is a stronger unification than originally requested: **the Euclidean quotient itself is independent of the singular content**.

Since

\[
A\mathfrak M=de\mathfrak M,
\qquad
\varrho=d\rho,
\qquad
\gcd(\rho,e\mathfrak M)=1,
\]

we also obtain

\[
\boxed{
\gcd(\varrho,A\mathfrak M)=d.
}
\tag{RAW-CONTENT}
\]

So the old singularity can be recovered after the fact simply as the gcd of the structural Euclidean remainder with the raw modulus.

---

# Part VI — EDF-1/2: Euclidean Defect

For an actual root, \(\lambda^\sharp>0\), hence

\[
e\mathfrak Mx<uD^\sharp.
\]

Thus

\[
\boxed{x\le\mu.}
\]

Define

\[
\boxed{s:=\mu-x\in\mathbb Z_{\ge0}.}
\]

Then

\[
\boxed{x=\mu-s}
\]

and

\[
\begin{aligned}
\lambda^\sharp
&=uD^\sharp-e\mathfrak M(\mu-s)\\
&=\rho+e\mathfrak M s.
\end{aligned}
\]

Therefore

\[
\boxed{
\lambda^\sharp=\rho+e\mathfrak M s.
}
\tag{EDF-LAM}
\]

In raw variables,

\[
\boxed{
\lambda_0=\varrho+A\mathfrak M s.
}
\tag{RAW-LAM}
\]

This is important: the defect coordinate can be defined entirely before any regular/singular split.

---

# Part VII — EPC-1: Exact Euclidean Product Collision

The sharp root equation becomes

\[
\boxed{
\Omega^\sharp
=(\mu-s)(\rho+e\mathfrak M s).
}
\tag{EPC-SHARP}
\]

Define

\[
\boxed{
\Phi(s):=
\Omega^\sharp-(\mu-s)(\rho+e\mathfrak M s).
}
\]

Then

\[
\boxed{x\text{ actual root}\iff\Phi(s)=0.}
\]

Expanding,

\[
\boxed{
\Phi(s)
=\Omega^\sharp-\mu\rho
-(\mu e\mathfrak M-\rho)s
+e\mathfrak M s^2.
}
\tag{PHI2}
\]

The symbolic audit checks exactly that

\[
\Phi(s)=\mathscr R^\sharp(\mu-s)
\]

under the Euclidean division relation.

Therefore

\[
\boxed{
\Phi\text{ is an exact re-expression of the root equation, not an independent condition.}
}
\]

Multiplying the sharp product by \(d\) gives the stronger operational form

\[
\boxed{
\Omega=(\mu-s)(\varrho+A\mathfrak M s).
}
\tag{EPC-RAW}
\]

The terminal product equation is thus **content free**.  The sharp chart remains useful for provenance and unit/support audits, but the raw chart is the preferred final coordinate system.

---

# Part VIII — EDF-3: Global Defect Height

The frozen DCDC5 complementary-factor bound is

\[
\boxed{
0<\lambda_0
<\frac{73}{2}\frac{L^3u^2}{G^3}.
}
\tag{LAM-UP}
\]

Since

\[
\frac{\lambda^\sharp}{e\mathfrak M}
=\frac{\lambda_0}{A\mathfrak M}
\]

and

\[
\lambda^\sharp=\rho+e\mathfrak M s>e\mathfrak M s,
\]

we obtain

\[
0\le s
<\frac{\lambda_0}{A\mathfrak M}.
\]

Using

\[
\mathfrak M=\frac L8,
\]

this gives

\[
\boxed{
0\le s<\mathcal B,
}
\]

where

\[
\boxed{
\mathcal B:=\frac{292L^2u^2}{AG^3}.
}
\tag{BDEF}
\]

The constant \(292\) is exact:

\[
\frac{73}{2}\cdot8=292.
\]

**Dependency audit.**  This is an actual-root necessary bound.  It is not asserted for arbitrary DCDC pseudo-states.  In computation, \(s_\star\ge\mathcal B\) is therefore a contradiction to actual-root existence, not a claim that DCDC itself forces a small CRT residue.

---

# Part IX — EDF-4: Global Shortness

Compare \(\mathcal B\) with \(A\mathfrak M=AL/8\):

\[
\frac{\mathcal B}{A\mathfrak M}
=
\frac{2336Lu^2}{A^2G^3}.
\]

Because

\[
A=2u+1>2u,
\]

we have

\[
\frac{u^2}{A^2}<\frac14,
\]

so

\[
\frac{\mathcal B}{A\mathfrak M}
<\frac{584L}{G^3}.
\]

Now

\[
3g-\ell=g+k
\]

because \(\ell=2g-k\).  Hence

\[
\frac{L}{G^3}=10^{-(g+k)}.
\]

The live chamber has \(g\ge4\) and \(k\ge1\), therefore

\[
\boxed{
\frac{\mathcal B}{A\mathfrak M}
<\frac{584}{10^{g+k}}
<1.
}
\]

Thus

\[
\boxed{\mathcal B<A\mathfrak M.}
\tag{SHORT-S}
\]

This proves the required independent height control that legitimizes \(s\) as a terminal coordinate.

---

# Part X — EDF-5: A + Decimal Defect CRT

The primitive \(A\)-root gives

\[
x\equiv r_A\pmod A.
\]

Since \(x=\mu-s\),

\[
\boxed{
s\equiv\mu-r_A\pmod A.
}
\tag{S-A}
\]

The decimal root gives

\[
x\equiv x_{10}\pmod{\mathfrak M},
\]

hence

\[
\boxed{
s\equiv\mu-x_{10}\pmod{\mathfrak M}.
}
\tag{S-M}
\]

Because

\[
\gcd(A,\mathfrak M)=1,
\]

CRT gives a unique canonical residue

\[
\boxed{
s\equiv s_\star\pmod{A\mathfrak M},
\qquad
0\le s_\star<A\mathfrak M.
}
\tag{S-CRT}
\]

But every actual root has

\[
0\le s<\mathcal B<A\mathfrak M.
\]

Therefore any actual root must have

\[
\boxed{s=s_\star.}
\]

If

\[
\boxed{s_\star\ge\mathcal B,}
\]

then the structural profile has no actual root.

If

\[
\boxed{s_\star<\mathcal B,}
\]

then there is exactly one possible root integer

\[
\boxed{x_\star=\mu-s_\star.}
\]

---

# Part XI — Global Euclidean-Defect One-Candidate Theorem

## Theorem EDF-5G

For every actual-root-eligible J2 structural profile after DCDC, regardless of

\[
d=1,
\qquad1<d<A,
\qquad d=A,
\]

the primitive \(A\)-root and decimal-root conditions select at most one Euclidean defect \(s\), and hence at most one actual-root candidate \(x_\star\).

### Proof

CDF-1/2 provide the common deflated chart for every \(d\).  EDF-3 gives

\[
0\le s<\mathcal B,
\]

EDF-4 gives

\[
\mathcal B<A\mathfrak M,
\]

and EDF-5 gives one CRT class modulo \(A\mathfrak M\).  An interval shorter than the CRT modulus contains at most one member of that class.  QED.

### Stronger operational corollary

Because \(\mu\), \(\varrho\), \(r_A\), and the original decimal residue can all be computed without splitting by \(d\), the terminal root pipeline may be written

\[
\text{structural profile}
\to
(uD_2=A\mathfrak M\mu+\varrho)
\to
s_\star
\to
x_\star
\to
\Omega=(\mu-s_\star)(\varrho+A\mathfrak M s_\star).
\]

Thus

\[
\boxed{
\textbf{regular/singular root multiplicity is retired.}
}
\]

---

# Part XII — EDF-6: High-Tail Zero Defect

From

\[
u=\frac{G+1}{q}
\]

and \(A>2u\),

\[
\begin{aligned}
\mathcal B
&=\frac{292L^2u^2}{AG^3}\\
&<\frac{146L^2u}{G^3}\\
&=\frac{146}{q}\left(1+\frac1G\right)\left(\frac LG\right)^2.
\end{aligned}
\]

Since

\[
\frac LG=10^{-\delta},
\]

we obtain

\[
\boxed{
\mathcal B
<\frac{146}{q}\left(1+\frac1G\right)10^{-2\delta}.
}
\tag{B-DELTA}
\]

For \(\delta\ge1\), the frozen \(q=1\) high-tail chamber is already closed.  Every live high-tail profile has \(q>1\), in fact \(q\ge7\).  Since \(G\ge10^4\) is more than sufficient,

\[
\mathcal B<\frac{1.461}{q}<1.
\]

Therefore the nonnegative integer defect must be

\[
\boxed{s=0.}
\tag{HIGH-S0}
\]

Thus every live high-tail actual root would have

\[
\boxed{x=\mu,}
\qquad
\boxed{\lambda^\sharp=\rho,}
\qquad
\boxed{\lambda_0=\varrho.}
\]

The exact product reduces to

\[
\boxed{
\Omega^\sharp=\mu\rho
}
\]

or, equivalently and more cleanly,

\[
\boxed{
\Omega=\mu\varrho.
}
\tag{HIGH-PROD}
\]

This proves Conjecture E2.  Conjecture E3 — uniform high-tail product extinction — remains open.

---

# Part XIII — High-Tail Exact Collision Audit

With \(s=0\), a hypothetical actual root must satisfy all of

\[
\mu\equiv r_A\pmod A,
\]

\[
\mu\equiv x_{10}\pmod{\mathfrak M},
\]

\[
\mu^2\equiv Z^2\pmod u,
\]

and

\[
\Omega=\mu\varrho.
\]

The first two congruences are not probabilistically independent equations; they are root residues used to select the defect.  U-SQ is likewise a root compatibility gate, not a second root polynomial.

The high product implies the interval

\[
\mu\le\Omega<\mu A\mathfrak M,
\]

because \(0<\varrho<A\mathfrak M\).  No uniform contradiction with existing structural bounds was proved.

The floor identity is exact:

\[
\boxed{
\mu=\left\lfloor\frac{uD_2}{A\mathfrak M}\right\rfloor.
}
\]

Thus high-tail existence would force

\[
\frac{uD_2}{A\mathfrak M}-1
<\mu
<\frac{uD_2}{A\mathfrak M}.
\]

Combining this with \(\mu>AG/10\) gives a valid lower restriction on \(D_2\), but the inherited upper bounds on \(D_2=u a_3+G\mathcal X\) are still too wide for an interval contradiction.  No false floor closure is claimed.

---

# Part XIV — Complementary-Factor / Primitive-A Euclidean Collision

Although it does not yet close a chamber, there is an exact elimination identity worth retaining.

For a primitive \(A\)-root define the temporary carry

\[
\boxed{
Kx+Z=A\nu.
}
\]

This \(\nu\) is used only for elimination.

Starting from

\[
\widetilde F=2Kx\lambda_0,
\qquad
\widetilde F=A\mathcal X^2+ZD_2,
\]

multiply by \(u\) and use

\[
uD_2=A\mathfrak Mx+\lambda_0.
\]

Then

\[
A(u\mathcal X^2+Z\mathfrak Mx)
=\lambda_0(2uKx-Z).
\]

Because \(A=2u+1\) and \(Kx+Z=A\nu\),

\[
2uKx-Z
=A\bigl((A-1)\nu-Z\bigr).
\]

Cancelling \(A\) gives

\[
\boxed{
 u\mathcal X^2+Z\mathfrak Mx
=\lambda_0\bigl((A-1)\nu-Z\bigr).
}
\tag{A-EUCLID-COLLISION}
\]

Since

\[
(A-1)\nu-Z=Kx-\nu,
\]

this can also be written

\[
\boxed{
 u\mathcal X^2+Z\mathfrak Mx
=\lambda_0(Kx-\nu).
}
\]

The decimal power identity

\[
\boxed{K\mathfrak M=G^2/8}
\]

was checked in this elimination.  At present the resulting expression remains algebraically equivalent to the factor equation once A-ROOT is imposed; it has not produced an independent uniform contradiction.  It is retained as a possible exact divisibility interface, not advertised as a killer theorem.

---

# Part XV — EDF-7: Boundary Defect Alphabet

For \(\delta=0\),

\[
L=G,
\]

so

\[
\boxed{
\mathcal B
<\frac{146}{q}\left(1+\frac1G\right).
}
\]

Uniformly over \(q\ge1\), this gives

\[
\boxed{0\le s\le146.}
\]

This proves Conjecture E4.

For the genuine \(q>1\) boundary, inherited divisor arithmetic gives \(q\ge7\).  Therefore

\[
\mathcal B<\frac{146}{7}\left(1+\frac1G\right)<21,
\]

and hence

\[
\boxed{q>1,\ \delta=0\Longrightarrow 0\le s\le20.}
\tag{BOUND-21}
\]

For the historical fixed values this further reads

\[
q=7:\ s\le20,
\qquad
q=11:\ s\le13,
\qquad
q=17:\ s\le8,
\qquad
q=19:\ s\le7.
\]

Per profile, however, one never enumerates this alphabet: EDF-5 selects one canonical \(s_\star\), and the only question is whether it lies below \(\mathcal B\).

---

# Part XVI — Boundary 79-State Exact Replay

The new search reconstructs the inherited \(g\le1200\) boundary corpus exactly:

| q | reconstructed tail/RCE | linear-legal | DCDC |
|---:|---:|---:|---:|
| 7 | 2,900 | 370 | 28 |
| 11 | 264,156 | 10,214 | 44 |
| 17 | 1,164 | 32 | 5 |
| 19 | 969 | 21 | 2 |
| **total** |  |  | **79** |

The unified first-death distribution is

\[
\boxed{
\texttt{PRIMITIVE\_GCD\_FAIL}=4,
\qquad
\texttt{DEFECT\_BOUND\_FAIL}=75.
}
\]

No profile reaches A²/A³, U-SQ, or exact product after the defect gate.

Among the 75 primitive-pass profiles, the structural content distribution is

\[
\boxed{
 d=1:50,
\quad d=3:20,
\quad d=7:4,
\quad d=11:1.
}
\]

This is a useful audit: content values greater than one certainly occur, but they no longer induce a root-fibre branch.

The result is finite and diagnostic only.  It does **not** prove the infinite boundary empty.

---

# Part XVII — Historical Six Singular States Replayed Without Fibres

The old six A²-singular states were

\[
q=11,
\qquad
 g\in\{259,359,435,481,669,1025\},
\qquad d=3.
\]

Under the new pipeline there is one structural division and one \(s_\star\) for each state.  All six die at

\[
\boxed{s_\star\ge\mathcal B.}
\]

For \(q=11,\delta=0\), the bound is approximately

\[
\mathcal B<13.273,
\]

whereas the canonical CRT defects have the following decimal lengths:

| g | d | digits of \(s_\star\) | first failure |
|---:|---:|---:|:--|
| 259 | 3 | 517 | DEFECT_BOUND_FAIL |
| 359 | 3 | 716 | DEFECT_BOUND_FAIL |
| 435 | 3 | 868 | DEFECT_BOUND_FAIL |
| 481 | 3 | 961 | DEFECT_BOUND_FAIL |
| 669 | 3 | 1337 | DEFECT_BOUND_FAIL |
| 1025 | 3 | 2048 | DEFECT_BOUND_FAIL |

Thus the old 18 \(A^2\) fibres and 333 legal singular carries never need to be constructed in the R4 terminal chart.

This is the requested operational retirement of singular root-fibre bookkeeping.

---

# Part XVIII — High-Tail Exact Diagnostic

The inherited \(\delta=1\), \(q\in\{7,11,17,19\}\), \(g\le1200\) exact tail search is reproduced:

- \(q=7\): no DCDC state;
- \(q=11\): one DCDC state, at \(g=471\);
- \(q=17\): no DCDC state;
- \(q=19\): no DCDC state.

The unique DCDC state has

\[
\gcd(Z,u)=13
\]

and therefore dies at the inherited primitive-gcd gate before the Euclidean defect is invoked.

Consequently the finite high-tail diagnostic contains no primitive-eligible state on which to observe the \(s=0\) product test.  The theorem \(s=0\) is nevertheless global and does not depend on this census.

---

# Part XIX — Reverse-CQRF Interface and Genuine Post-DCDC Diagnostic

For \(r=g-k>0\), the same Euclidean chart applies without modification:

\[
\ell=g+r,
\qquad
\mathcal B
<\frac{146}{q}\left(1+\frac1G\right)10^{2r}.
\]

The defect interval is not absolutely bounded as \(r\to\infty\), but this no longer creates a quotient fibre: A+decimal CRT still selects at most one \(s_\star\) because

\[
\mathcal B<A\mathfrak M
\]

globally.

The old Reverse-CQRF nonzero-tail parameterization is used only as an outer generator.  To ensure that the diagnostic actually reaches the new layer, the R4 search targets

\[
\boxed{r=1,\qquad q\in\{7,11,17,19\},\qquad g\le12.}
\]

This produces **50 genuine DCDC states**:

| q | DCDC states |
|---:|---:|
| 7 | 14 |
| 11 | 26 |
| 17 | 4 |
| 19 | 6 |
| **total** | **50** |

Their unified first deaths are

\[
\boxed{
\texttt{PRIMITIVE\_GCD\_FAIL}=6,
\qquad
\texttt{DEFECT\_BOUND\_FAIL}=44.
}
\]

Thus all 44 primitive-pass reverse diagnostics die before A²/A³/U/product.

This is the first reverse diagnostic in the 55 campaign that genuinely reaches DCDC + defect CRT; it is not the old \((q,N,t)=(1,7,3)\) pre-DCDC pseudo-state.

No infinite reverse closure is inferred from this finite slice.

---

# Part XX — Reverse Zero-Tail Scope Regression

The inherited zero-tail condition is

\[
q^3<63\cdot10^r.
\]

For the four historical small \(q\) values, the first \(r\) satisfying this is

\[
(q,r)=(7,1),(11,2),(17,2),(19,3).
\]

At these minimal \(r\), zero-tail integrality would require \(t\) to be a multiple of

\[
\frac{C(q)}{\gcd(C(q),B(q))}.
\]

The exact values are:

| q | r | required step | inherited upper \(t\)-bound |
|---:|---:|---:|---:|
| 7 | 1 | 6475 | 629 |
| 11 | 2 | 29491 | 9899 |
| 17 | 2 | 19465 | 15299 |
| 19 | 3 | 203395 | 170999 |

Hence no zero-tail \(t\) candidate exists at these minimal rays in the targeted regression.

This is **not** a global zero-tail closure: increasing \(r\) enlarges the inherited \(t\)-range, so the full zero-tail family remains part of the reverse frontier.

---

# Part XXI — A²/A³ and U-SQ as Verification Gates

After EDF-5G, the correct order is

\[
s_\star
\to x_\star
\to A^2/A^3
\to U\text{-SQ}
\to \Phi(s_\star).
\]

No A² root fibre is enumerated.

The direct candidate checks are

\[
Q(x_\star)\equiv0\pmod{A^2},
\]

\[
Q(x_\star)\equiv0\pmod{A^3},
\]

and

\[
x_\star^2\equiv Z^2\pmod u.
\]

In the new boundary and reverse diagnostics, every primitive-pass profile already dies at the defect bound, so none of these later gates is reached.  This concentration is computational evidence for a future uniform CRT-extinction theorem, but it is not itself that theorem.

---

# Part XXII — Factor-Support Audit

Under an actual root,

\[
\Omega^\sharp=x\lambda^\sharp
\]

and

\[
\gcd(\lambda^\sharp,e\mathfrak M)=1.
\]

Therefore

\[
\boxed{
\gcd(\Omega^\sharp,e\mathfrak M)
=\gcd(x,e\mathfrak M).
}
\tag{SUPPORT}
\]

This identity is correct, but it is a direct consequence of the exact product equality plus LAM-UNIT.  It is therefore classified as

\[
\boxed{\textbf{DEPENDENT / REDUNDANT AS AN INDEPENDENT KILLER}.}
\]

It may be used as a cheap mismatch check on a candidate, but it is not a fourth root condition.

Also

\[
\boxed{
\gcd(x,\lambda^\sharp)=\gcd(x,uD^\sharp).
}
\]

Primitive reconstruction gives \(\gcd(x,u)=1\), but there is **no** inherited theorem proving \(\gcd(x,D^\sharp)=1\).

In fact the common-radial reconstruction has

\[
x=UC_1,
\qquad
D_2=Ud_2.
\]

Let \(h=\gcd(U,d)\).  Writing \(U=hU_1\) and \(d=hd_1\), the divisibility \(d\mid D_2=Ud_2\) and \(\gcd(U_1,d_1)=1\) imply \(d_1\mid d_2\).  Consequently

\[
D^\sharp=\frac{D_2}{d}
=U_1\frac{d_2}{d_1},
\]

so

\[
\boxed{
\frac{U}{\gcd(U,d)}
\mid
\gcd(x,D^\sharp).
}
\]

Therefore a blanket coprimality assertion

\[
\gcd(x,uD^\sharp)=1
\]

would require additional control such as \(U\mid d\), which is not available.  No coprime factor allocation is assumed.

---

# Part XXIII — Redundancy Audit of Small-Modulus Product Reductions

Several tempting reductions of the exact product are not new killers.

- Modulo \(\mathfrak M\), the product reduces to the already used decimal root residue.
- Modulo \(e\), using A-ROOT and \(A=2u+1\), the sharp product congruence reduces algebraically to the same primitive A-root relation.
- Modulo \(A\) in the raw chart, the product is the normalized root polynomial modulo \(A\); in the regular case this is already recovered by A-ROOT, while in singular content A-ROOT is stronger.

Thus the next successful extinction theorem must use either the **integer/floor nature** of \(\mu\), an outer modulus such as \(q\)/CQRF data, a size interval, or an exact resultant after the deterministic \(s_\star\) has been substituted.  Repackaging the same A/decimal residues is not progress.

---

# Part XXIV — Outerization Status

The frozen RCE/CQRF quantities are

\[
M_q=q(q+4),
\qquad
R=At-2N,
\]

\[
Y=R+uNM_q,
\]

\[
E=uq((G-1)t-qN)+GY,
\]

with

\[
Z=\frac{R}{M_q},
\qquad
\mathcal X=\frac{Y}{2M_q},
\qquad
D_2=\frac{E}{2M_q}.
\]

Hence

\[
D^\sharp=\frac{E}{2M_qd}.
\]

Also

\[
4M_q^2\widetilde F=AY^2+2RE,
\]

so

\[
\boxed{
8KM_q^2\,\Omega
=AY^2+2RE.
}
\]

Using \(\Omega=d\Omega^\sharp\),

\[
\boxed{
8KM_q^2d\,\Omega^\sharp
=AY^2+2RE.
}
\]

This gives a complete polynomial numerator for \(\Omega^\sharp\) in the outer variables once the structural divisor \(d\) is fixed by gcd.

No new resultant was promoted to a theorem in this round because every tested primitive-pass boundary/reverse state dies before the product layer.  A future resultant should only be applied to a genuine \(s_\star<\mathcal B\) survivor.

---

# Part XXV — Conjecture Ledger

| Conjecture | Verdict |
|---|---|
| E1 Global One-Defect Theorem | **PROVED** |
| E2 High-tail defect zero | **PROVED** |
| E3 High-tail Euclidean-product extinction | **OPEN** |
| E4 Boundary 147 alphabet | **PROVED**, strengthened to \(s\le20\) for \(q>1\) |
| E5 Boundary CRT extinction | **TRUE on all 79 historical DCDC states**, **OPEN uniformly** |
| E6 Global factor-product mismatch | **OPEN**; tested profiles die before product |
| E7 Reverse factor/CQRF incompatibility | **44/44 primitive-pass r=1 diagnostics die at defect bound**, **OPEN uniformly** |
| \(\gcd(x,\lambda^\sharp)=1\) globally | **NOT AVAILABLE / structurally obstructed by common radial scale** |
| SUPPORT identity as independent killer | **REDUNDANT** |

---

# Part XXVI — New Unified Terminal Pipeline

The preferred R4 pipeline is now

\[
\boxed{\text{structural profile}}
\]

\[
\Downarrow
\]

\[
\boxed{
\Omega=\widetilde F/(2K),
\qquad
uD_2=A\mathfrak M\mu+\varrho
}
\]

\[
\Downarrow
\]

\[
\boxed{
s\equiv\mu-r_A\pmod A,
\qquad
s\equiv\mu-x_{10}\pmod{\mathfrak M}}
\]

\[
\Downarrow
\]

\[
\boxed{\text{one }s_\star\pmod{A\mathfrak M}}
\]

\[
\Downarrow
\]

\[
\boxed{s_\star<\mathcal B?}
\]

\[
\Downarrow
\]

\[
\boxed{x_\star=\mu-s_\star}
\]

\[
\Downarrow
\]

\[
\boxed{A^2/A^3,\ U\text{-SQ verification}}
\]

\[
\Downarrow
\]

\[
\boxed{
\Omega\stackrel{?}{=}(\mu-s_\star)(\varrho+A\mathfrak M s_\star).
}
\]

The sharp variables

\[
d,e,D^\sharp,\Omega^\sharp,\rho
\]

remain in the archive as the exact proof that singularity is polynomial content, but they are not needed to branch the terminal search.

---

# Part XXVII — Closure Audit

### \(\delta>0\)

- frozen \(q=1\) high tail: **CLOSED**;
- live \(q>1\): **OPEN**;
- new theorem: \(s=0\) globally;
- remaining exact equality: \(\Omega=\mu\varrho\).

### \(\delta=0\)

- chamber: **OPEN globally**;
- all actual roots satisfy \(s\le146\);
- \(q>1\) sharpens to \(s\le20\);
- historical 79 DCDC corpus: **0 defect-eligible survivors** after primitive gcd.

### \(\delta<0\)

- chamber: **OPEN globally**;
- one deterministic defect candidate per profile;
- targeted \(r=1,g\le12\) diagnostic: 50 DCDC states, 0 defect-eligible survivors after primitive gcd;
- zero-tail retained globally.

### Regular/singular split

\[
\boxed{\textbf{RETIRED as terminal root bookkeeping}.}
\]

### Full J2

\[
\boxed{\textbf{OPEN}.}
\]

No closure certificate is issued.

---

# Part XXVIII — New Frontier

The R3 frontier

\[
\text{regular branch} + \text{singular branch}
\]

is obsolete.

The new frontier is

\[
\boxed{
\textbf{one structural Euclidean quotient/remainder}
+
\textbf{one deterministic CRT defect}
+
\textbf{one exact integer product equality}.
}
\]

More explicitly:

\[
\boxed{
\mu=\left\lfloor\frac{uD_2}{A\mathfrak M}\right\rfloor,
\qquad
\varrho=uD_2-A\mathfrak M\mu,
}
\]

\[
\boxed{
s=s_\star,}
\]

and

\[
\boxed{
\Omega=(\mu-s_\star)(\varrho+A\mathfrak M s_\star).
}
\]

For high tail this is further reduced to

\[
\boxed{
\Omega=\mu\varrho.
}
\]

The next theorem should therefore attack **exact quotient/remainder product mismatch**, preferably after outerizing \(\mu,\varrho,\Omega\) through CQRF/Reverse-CQRF, rather than reopening local-root multiplicity or inventing another root quotient.

---

# Part XXIX — File Audit

Generated and checked:

```text
J2-55-R4-Complementary-Factor-Euclidean-Report.md
J2-55-R4-EuclideanDefect-symbolic.py
J2-55-R4-EuclideanDefect-search.py
J2-55-R4-EuclideanDefect-search-certificate.txt
J2-55-R4-EuclideanDefect-certificate.txt
J2-55-R4-EuclideanDefect-survivors.tsv
```

No `J2-Resonance-Closure-Certificate.md` is generated because J2 remains open.

