# J2-55-R2 — Primitive U-Square Carry Synchronization Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第二轮 / 统一终端线第十二轮 — Primitive \(u\)-Square Synchronization × Singular-Content-to-\(u\) Bridge × Third-\(A\)-Digit Collision  
**Inherited primary source:** `J2-55-R1-A-Root-Lift-Report.md`  
**Exact symbolic audit:** `J2-55-R2-USquare-symbolic.py`  
**Exact regression:** `J2-55-R2-USquare-search.py`  
**Regression ledger:** `J2-55-R2-USquare-survivors.tsv`

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

No valid uniform proof of

\[
J=2\Longrightarrow\varnothing
\]

was obtained, so **no J2 Resonance Closure Certificate is issued**.

This round nevertheless produces four structural reductions that are genuinely stronger than the R1 frontier.

First, the primitive provenance is now closed:

\[
\boxed{\gcd(Z,u)=1}
\]

for every **admissible primitive-recovered J2 root state**. Therefore U-SQ admits the exact complementary-unitary-divisor allocation; historical pseudo-root states with \(\gcd(Z,u)>1\) die before this theorem is invoked.

Second, singular content multiplicity is no longer an uncontrolled factor of \(d_A\). If

\[
d=d_A>1,\qquad e=A/d,
\]

then

\[
r_m\equiv r_0+me\pmod u,
\]

and for every fixed U-square root cell and carry \(j\), the content index \(m\) has multiplicity

\[
\boxed{
\begin{cases}
\le1,&1<d<A,\\
\le3,&d=A.
\end{cases}}
\]

Third, the regular non-singleton sector has a new outer suppression. In the live \(\ell\ge6\) chamber,

\[
\boxed{
d_A=1,\ A\le C_\ell q
\Longrightarrow
2g\le3\ell+1.}
\tag{R2-LQ-WEDGE}
\]

Thus the genuinely large-\(q\) regular remainder is forced into an approximately slope-\(3/2\) deficiency wedge.

Fourth, once the A³ digit and U-square gate are simultaneously imposed, every surviving regular candidate has an exact residual divisible by both neighboring moduli:

\[
\boxed{Au\mid E_*}
\]

unless \(E_*=0\). Hence the remaining singleton obstruction is one **single candidate excess**, not an \(O(q)\) carry family.

The precise surviving obstruction is therefore:

\[
\boxed{
\begin{array}{ll}
\text{regular singleton:}&
\text{one }c_3\text{ candidate}+\text{one exact excess};\\[1mm]
\text{regular large-}q:&
2g\le3\ell+1+\text{one shorter }n\text{-interval}+\text{one exact excess};\\[1mm]
\text{singular:}&
\text{one unitary root cell}+j+\le3\text{ content choices}+\text{one exact excess}.
\end{array}}
\]

This is strictly lower-dimensional than the inherited

\[
A^2\text{-root fibres}\times j=O(q)\times\text{U-SQ}\times T_{A^2}(j).
\]

---

# Part II — Inherited R1 Theorem Ledger

Freeze the R1 setup:

\[
G=10^g,\qquad H=G/2,\qquad K=10^k,\qquad \ell=2g-k,\qquad L=10^\ell,
\]

\[
uq=G+1,\qquad A=2u+1,
\]

and

\[
Q(x)=AH^2x^2-2uKD_2x+\widetilde F,
\qquad
\widetilde F=A\mathcal X^2+ZD_2.
\]

The primitive A-root residue is

\[
Kx\equiv-Z\pmod A,
\qquad \gcd(K,A)=1,
\]

hence

\[
\boxed{x\equiv r_A:=-K^{-1}Z\pmod A}
\]

uniquely.

Put

\[
T_A=Q(r_A)/A,
\qquad
d_A=\gcd(Q'(r_A),A)=\gcd(D_2,A).
\]

The A² classification is frozen:

\[
\boxed{
\begin{array}{ll}
d_A=1:&\text{one canonical }r_{A^2};\\
d_A>1,\ d_A\nmid T_A:&\text{no A² lift};\\
d_A>1,\ d_A\mid T_A:&\text{exactly }d_A\text{ canonical A² classes}.
\end{array}}
\]

Every actual root is

\[
\boxed{x=r_{A^2}+A^2j}
\]

with

\[
\boxed{0\le j<C_\ell q},
\qquad
C_\ell=\frac{1299}{500}+10^{-\ell}<2.599,
\qquad \ell\ge6.
\]

In the regular branch the next A-digit has the **negative sign**

\[
\boxed{
c_3\equiv-
\frac{Q(r_{A^2})}{A^2}
Q'(r_{A^2})^{-1}
\pmod A.}
\tag{C3-correct}
\]

This sign is inherited from the exact elementary A-adic lift and is used throughout this report.

---

# Part III — Primitive U-Coprimality Audit

## Theorem USQ-1 — Primitive U-Coprimality

For every admissible primitive-recovered J2 state,

\[
\boxed{\gcd(Z,u)=1.}
\]

### Proof

Primitive recovery gives

\[
C_1^2\equiv z^2\pmod u
\]

and the primitive gcd condition includes

\[
\gcd(C_1,u)=1.
\]

If a prime \(p\mid\gcd(z,u)\), then the square congruence gives \(p\mid C_1\), contradiction. Hence

\[
\gcd(z,u)=1.
\]

The common-radial reconstruction is

\[
a_1=UC_1,\qquad Z=Uz,
\]

while the common denominator scale has

\[
V=uGH,
\qquad
\gcd(U,V)=1.
\]

Thus \(\gcd(U,u)=1\). Therefore

\[
\gcd(Z,u)=\gcd(Uz,u)=1.
\qquad\square
\]

### Scope warning

This is **not** a pre-root identity. It is a primitive-recovery theorem. A pseudo-state may satisfy the reconstructed algebraic equations and U-SQ while failing this gate. Such a state cannot be used to falsify the coprime root allocation below.

The historical \(q=11\) pseudo-fibre at

\[
g=471,\qquad g=63501
\]

has

\[
\gcd(Z,u)=13
\]

in both cases and therefore dies here.

---

# Part IV — U-Square Factor Allocation Theorem

The U-square condition is

\[
\boxed{x^2\equiv Z^2\pmod u.}
\]

Because \(u\) is odd and \(\gcd(Z,u)=1\), for every prime power \(p^a\Vert u\), the factors

\[
x-Z,\qquad x+Z
\]

cannot both be divisible by \(p\): otherwise \(p\mid2Z\), contradiction. Since

\[
p^a\mid(x-Z)(x+Z),
\]

the whole prime power is allocated to exactly one side.

Therefore there exist unique complementary unitary divisors

\[
\boxed{u=u_+u_-,\qquad \gcd(u_+,u_-)=1}
\]

such that

\[
\boxed{u_+\mid x-Z,\qquad u_-\mid x+Z.}
\tag{USQ-ALLOC}
\]

Equivalently,

\[
x\equiv Z\pmod{u_+},
\qquad
x\equiv-Z\pmod{u_-}.
\]

This is the correct global replacement for the false two-root statement \(x\equiv\pm Z\pmod u\).

An equivalent root-of-unity notation is

\[
x\equiv\eta Z\pmod u,
\qquad
\eta^2\equiv1\pmod u.
\]

No explicit enumeration of \(2^{\omega(u)}\) sign vectors is needed for the theorem.

---

# Part V — Short-Carry CRT and Baseline Counts

Since

\[
A=2u+1\equiv1\pmod u,
\qquad A^2\equiv1\pmod u,
\]

substitution of

\[
x=r_{A^2}+A^2j
\]

gives

\[
\boxed{(r_{A^2}+j)^2\equiv Z^2\pmod u.}
\tag{J-USQ}
\]

For a fixed unitary cell \((u_+,u_-)\),

\[
\boxed{
r_{A^2}+j\equiv Z\pmod{u_+},
\qquad
r_{A^2}+j\equiv-Z\pmod{u_-}.}
\]

CRT gives one residue

\[
\boxed{j\equiv j_{u_+,u_-}\pmod u.}
\]

Intersect it directly with \(0\le j<C_\ell q\).

## U1

If

\[
u>C_\ell q,
\]

the interval is shorter than one modulus, so a fixed U-root class contributes at most one carry.

## U2

If \(u>q\), then

\[
C_\ell q<2.599u<3u,
\]

so a fixed class contributes at most three carries.

## U3

If \(u\le q\), then

\[
q^2\ge uq=G+1.
\]

Thus this is automatically a large-\(q\) outer chamber.

These are counting lemmas only; no closure is claimed from them alone.

---

# Part VI — Root-of-Unity Spacing: Exact Correction

The naive conjecture “two U-square roots in a short interval force a small nontrivial unitary divisor” is false because of the global antipodal pair.

A cyclotomic modular counterexample already occurs at

\[
u=11,\qquad 11\mid10+1,\qquad Z=5.
\]

The roots

\[
5,\ 6\pmod{11}
\]

are adjacent because \(6\equiv-5\pmod{11}\), while \(11\) has no proper nontrivial unitary divisor.

So Candidate Spacing A/C, as originally stated, are false.

The exact corrected theorem is the following.

## Corrected Spacing Lemma

Let \(b_1,b_2\) be two coprime U-square roots of \(Z^2\pmod u\). Partition the prime-power factors of \(u\) according to whether the two sign vectors agree or flip. Let

\[
u_{\rm same}u_{\rm flip}=u,
\qquad
\gcd(u_{\rm same},u_{\rm flip})=1.
\]

Then

\[
\boxed{u_{\rm same}\mid b_1-b_2,}
\qquad
\boxed{u_{\rm flip}\mid b_1+b_2.}
\]

For distinct cells \(u_{\rm flip}>1\). Therefore if

\[
0<|b_1-b_2|<W,
\]

then either

\[
\boxed{1<u_{\rm same}<W}
\]

or

\[
\boxed{u_{\rm same}=1,\quad b_2\equiv-b_1\pmod u.}
\]

Thus the correct statement is

\[
\boxed{
\text{nearby distinct roots}
\Rightarrow
\text{small same-sign unitary factor OR global antipode}.}
\]

This is useful for pruning multiple-cell collisions but cannot by itself kill a **single** translated hit: the translation \(r_{A^2}\) can place an arbitrary root cell inside a short carry interval.

---

# Part VII — Outerized K Splice

The exact identities

\[
10^\ell K=G^2,
\qquad
2G=qA-q-2
\]

give

\[
\boxed{4\cdot10^\ell K=(qA-q-2)^2.}
\]

Hence

\[
4\cdot10^\ell K\equiv(q+2)^2\pmod A,
\]

and

\[
4\cdot10^\ell K
\equiv(q+2)^2-2q(q+2)A
\pmod{A^2}.
\]

Modulo \(u\),

\[
\boxed{10^\ell K\equiv1\pmod u.}
\]

Since \(4\cdot10^\ell K\) is an A-unit,

\[
\boxed{\gcd(q+2,A)=1.}
\]

Therefore A-ROOT can be written without a black-box \(K\)-inverse:

\[
\boxed{
r_A\equiv
-4\cdot10^\ell Z\,(q+2)^{-2}
\pmod A.}
\tag{AROOT-OUT}
\]

In the regular branch,

\[
Q'(r_{A^2})\equiv KD_2\pmod A,
\]

so

\[
\boxed{
c_3\equiv
-4\cdot10^\ell
\frac{Q(r_{A^2})}{A^2}
D_2^{-1}(q+2)^{-2}
\pmod A.}
\tag{C3-OUT}
\]

This is a genuine simplification, but it still contains the exact A² residual \(Q(r_{A^2})/A^2\). No uniform contradiction follows merely from outerizing \(K\).

---

# Part VIII — D2 Form of U-Square

From the frozen RCE reconstruction,

\[
2\mathcal X=Z+uN,
\]

hence

\[
2\mathcal X\equiv Z\pmod u.
\]

Also

\[
D_2=ua_3+G\mathcal X
\equiv-\mathcal X
\equiv-\frac Z2\pmod u.
\]

Therefore the U-square root cell can equivalently be written

\[
\boxed{
r_{A^2}+j\equiv-2\eta D_2\pmod u,
\qquad \eta^2\equiv1\pmod u.}
\tag{D2-USQ}
\]

This exposes a useful conceptual limit: the singular content

\[
d_A=\gcd(A,D_2)
\]

lives on prime support dividing \(A\), while the U-square sign allocation lives on prime support dividing \(u\). Since

\[
\gcd(A,u)=1,
\]

these are disjoint prime supports. Thus no same-prime valuation collision exists between the two mechanisms; the real bridge is the **movement of the A² classes modulo \(u\)**, developed below.

---

# Part IX — Regular Third-A-Digit Synchronization

Assume

\[
d_A=1.
\]

There is one canonical \(r_{A^2}\) and one next digit \(c_3\in[0,A)\) satisfying (C3-correct).

Every actual root must satisfy

\[
j\equiv c_3\pmod A.
\]

## 9.1 Singleton chamber

If

\[
A>C_\ell q,
\]

then \(0\le j<C_\ell q<A\). Therefore an actual root exists only if

\[
\boxed{c_3<C_\ell q}
\]

and in that event

\[
\boxed{j=c_3.}
\]

So the entire regular singleton branch has no carry freedom. Its remaining conditions are

\[
\boxed{(r_{A^2}+c_3)^2\equiv Z^2\pmod u}
\tag{REG-USQ}
\]

and

\[
\boxed{E_*:=T_{A^2}(c_3)=0.}
\tag{REG-EX}
\]

## 9.2 Exact candidate-excess divisibility

Because \(c_3\) is the A³ digit,

\[
A\mid E_*.
\]

If REG-USQ holds, the reconstructed identity

\[
Q(x)\equiv4^{-1}(x^2-Z^2)\pmod u
\]

gives \(u\mid Q(r_{A^2}+A^2c_3)\). Since \(\gcd(A,u)=1\), division by \(A^2\) modulo \(u\) is legal, hence

\[
u\mid E_*.
\]

Therefore

\[
\boxed{Au\mid E_*.}
\tag{EX-DIV}
\]

Consequently a U-square-passing singleton candidate satisfies the exact dichotomy

\[
\boxed{E_*=0\quad\text{or}\quad |E_*|\ge Au.}
\]

This does not yet prove \(E_*\ne0\) uniformly, but it is the correct first-candidate-excess interface.

## 9.3 Status of Conjecture U1

The desired uniform theorem

\[
d_A=1,\ A>C_\ell q
\Longrightarrow
\text{REG-USQ fails}
\]

was **not proved**.

The exact finite regression is much stronger empirically: all 50 regular primitive A² fibres in the inherited 79-cell ledger satisfy the singleton condition; one has an empty actual carry interval, and the other 49 have \(c_3\) outside their exact legal carry interval. Thus none even reaches REG-USQ. This is diagnostic evidence, not a global theorem.

---

# Part X — Regular Large-q Chamber

Assume

\[
d_A=1,
\qquad
A\le C_\ell q.
\]

Then

\[
2(G+1)+q\le C_\ell q^2,
\]

so

\[
\boxed{q^2>\frac{2(G+1)}{C_\ell}.}
\tag{LQ-LOW}
\]

In particular \(q\gtrsim0.877\sqrt{G+1}\).

The inherited outer theorem in the nontrivial tail chamber \(\ell<g\), where \(\ell\ge6\) implies \(G\ge10^7\), gives

\[
G<37\frac{L^3}{q^2}.
\]

Combining with (LQ-LOW),

\[
G(G+1)
<\frac{37C_\ell}{2}L^3.
\]

For \(\ell\ge6\),

\[
C_\ell\le\frac{2598001}{1000000},
\qquad
\frac{37C_\ell}{2}<50.
\]

Hence

\[
G^2<50L^3<100L^3.
\]

Thus

\[
10^{2g}<10^{3\ell+2},
\]

and since the exponents are integers,

\[
\boxed{2g\le3\ell+1.}
\tag{LQ-3/2}
\]

If \(\ell\ge g\), this conclusion is automatic. Therefore (LQ-3/2) is valid throughout the live regular non-singleton chamber.

This is the principal new uniform suppression of the round.

## 10.1 Shorter n-index

Write

\[
j=c_3+An.
\]

This is permitted because it is strictly shorter than the inherited carry. From \(0\le j<C_\ell q\),

\[
\boxed{
0\le n<\frac{C_\ell q-c_3}{A}
}
\]

whenever \(c_3<C_\ell q\); if \(c_3\ge C_\ell q\), the branch dies immediately.

Since \(A\equiv1\pmod u\), U-SQ becomes

\[
\boxed{(r_{A^2}+c_3+n)^2\equiv Z^2\pmod u.}
\tag{N-USQ}
\]

Let

\[
x_n=r_{A^2}+A^2c_3+A^3n.
\]

Then the exact residual

\[
E(n)=Q(x_n)/A^2
\]

is divisible by \(A\), and if N-USQ holds it is also divisible by \(u\). Thus

\[
\boxed{Au\mid E(n)}
\]

for every U-square-passing candidate, with exact root iff \(E(n)=0\).

No true large-\(q\) root fibre occurs in the inherited 79-cell PRCC10 ledger because that ledger contains only \(q\in\{7,11,17,19\}\). A separate outer census for \(6\le g\le12\) finds 28 structural pairs with \(A\le C_\ell q\), confirming that the large-\(q\) outer chamber itself is nonempty and cannot be dismissed by the old small-\(q\) regression.

---

# Part XI — Singular Content-to-u Bridge

Assume

\[
d=d_A>1,
\qquad d\mid T_A.
\]

Put

\[
A=de,
\qquad e=A/d.
\]

The A² classes can be indexed as

\[
\boxed{r_m=r_0+m\frac{A^2}{d},\qquad 0\le m<d.}
\]

Since

\[
de=A=2u+1\equiv1\pmod u,
\]

both \(d\) and \(e\) are U-units and

\[
e\equiv d^{-1}\pmod u.
\]

Also

\[
\frac{A^2}{d}=Ae\equiv e\pmod u.
\]

Therefore

\[
\boxed{r_m\equiv r_0+me\pmod u.}
\tag{CSU-1}
\]

This proves the requested **Content-to-U Bridge**.

U-SQ is now

\[
\boxed{(r_0+me+j)^2\equiv Z^2\pmod u.}
\tag{CSU-2}
\]

No additional root quotient has been introduced.

---

# Part XII — New Singular Multiplicity Collapse

Fix a U-square root cell

\[
\rho\equiv\eta Z\pmod u,
\qquad \eta^2\equiv1\pmod u.
\]

Then CSU-2 is equivalent to the linear congruence

\[
r_0+me+j\equiv\rho\pmod u.
\]

Multiplying by \(d\) and using \(de\equiv1\pmod u\),

\[
\boxed{
m\equiv d(\rho-r_0-j)\pmod u.}
\tag{M-SELECT}
\]

## 12.1 Proper content: \(1<d<A\)

Because \(A\) is odd, \(e=A/d>1\) implies \(e\ge3\). Hence

\[
d=\frac Ae\le\frac{2u+1}{3}<u
\qquad(u>1).
\]

Since \(0\le m<d<u\), the residue (M-SELECT) selects **at most one** legal \(m\).

\[
\boxed{
1<d<A
\Longrightarrow
\#m(\rho,j)\le1.}
\tag{CSU-3a}
\]

## 12.2 Maximal content: \(d=A\)

Now \(e=1\) and

\[
0\le m<A=2u+1.
\]

A fixed residue modulo \(u\) occurs at most three times in this interval. Thus

\[
\boxed{
d=A\Longrightarrow\#m(\rho,j)\le3.}
\tag{CSU-3b}
\]

### Consequence

The singular A² multiplicity \(d\) has disappeared as a combinatorial branching factor once a U-root cell and one carry are fixed:

\[
\boxed{
\text{fixed }(\eta,j)
\Longrightarrow
\le3\text{ singular A² fibres globally}.}
\]

For proper content the bound is one.

This is stronger than the proposed small-\(d\)/large-\(d\) heuristic split: the exact relation \(de=2u+1\) itself supplies a uniform multiplicity theorem.

---

# Part XIII — Singular Prime Alignment Audit

## 13.1 \(p\equiv3\pmod4\)

R1 proved that if

\[
p^s\mid d_A,
\qquad p\equiv3\pmod4,
\]

then with \(r_p=\lceil s/2\rceil\),

\[
p^{r_p}\mid a_1,a_3,Z,\mathcal X,N,
\]

and, under the stated extra condition, also \(t\).

The suggested scale-extraction route was audited carefully. The current theorems do **not** justify

\[
p^{r_p}\mid U
\]

from these divisibilities alone. More importantly, even if an additional argument forced \(p\mid U\), it would not contradict common-scale coprimality: \(p\mid A\) implies

\[
p\nmid u,
\]

and \(p\notin\{2,5\}\) implies \(p\nmid GH\). Thus for

\[
V=uGH
\]

we have \(p\nmid V\), so \(p\mid U\) is compatible with \(\gcd(U,V)=1\).

Therefore Conjecture U3 is **not proved** by the available common-U gcd mechanism. The BADP theorem remains useful divisibility information, but no uniform extinction follows from this route in R2.

## 13.2 \(p\equiv1\pmod4\)

The singular sum-of-two-squares congruence forces a local \(\sqrt{-1}\) choice at primes \(p\mid A\). But U-square sign choices occur at primes dividing \(u\). Since

\[
\gcd(A,u)=1,
\]

there is no same-prime sign variable to identify. No valid direct \(\sqrt{-1}\)-versus-U-sign collision was found, and this direction is stopped here rather than expanded into a generic Gaussian campaign.

---

# Part XIV — Exact Carry Polynomial Collision

For every canonical A² fibre,

\[
x=r_{A^2}+A^2j,
\]

the exact Taylor identity is

\[
\boxed{
T_{A^2}(j)
=
\frac{Q(r_{A^2})}{A^2}
+Q'(r_{A^2})j
+A^3H^2j^2.}
\tag{CARRY-Q}
\]

An actual root requires

\[
\boxed{T_{A^2}(j)=0.}
\]

U-SQ is not probabilistically independent of this equation: it is exactly the reduction of \(Q(x)=0\) modulo \(u\) in reconstructed coordinates. Its value is that A-adic lifting has already collapsed \(x\) to a small carry before this modulus is read.

For any U-square-selected candidate,

\[
u\mid T_{A^2}(j).
\]

In the regular A³-synchronized branch one additionally has

\[
A\mid T_{A^2}(j),
\]

hence \(Au\mid T_{A^2}(j)\).

No uniform sign theorem for the resulting excess was found. The exact residual, rather than another congruence, is therefore the correct terminal object.

---

# Part XV — Computational Regression

The exact replay uses integer arithmetic and `Fraction` only. The inherited historical root-layer corpus has 79 DCDC states with

\[
q\in\{7,11,17,19\},\qquad g\le1200.
\]

R2 deliberately applies the primitive gcd gate **before** the coprime U-square theorem.

The exact gate census is:

```text
INPUT_STATES=79
PRIMITIVE_GCD_FAIL_STATES=4
PRIMITIVE_GCD_PASS_STATES=75
A2_LIFT_FAIL_STATES=19
A2_SOLVABLE_STATES=56
INPUT_ROOT_FIBRES=68
REGULAR_FIBRES=50
REGULAR_SINGLETON_FIBRES=50
SINGULAR_SOLVABLE_STATES=6
J_INTERVAL_FAIL_FIBRES=1
A3_DIGIT_FAIL_FIBRES=49
U_SQUARE_FAIL_FIBRES=18
U_SQUARE_SURVIVE_FIBRES=0
EXACT_CARRY_FAIL_FIBRES=0
EXACT_ROOT_SURVIVE_FIBRES=0
```

Thus the 68 A² fibres remaining after state-level primitive/A² gates split exactly into:

- 50 regular singleton fibres: one has empty actual carry interval; the remaining 49 fail the A³ digit/interval collision;
- 18 singular fibres from six \(d_A=3\) states: every fibre has a legal carry interval but none has a U-square carry.

The six singular states occur at

\[
\boxed{g\in\{259,359,435,481,669,1025\},\qquad q=11.}
\]

Their content bridge was checked class by class with exact full integers. The compact view is below; the complete values of \(e,r_0,r_1,r_2\) are stored in `J2-55-R2-USquare-survivors.tsv`.

| g | q | d | e suffix | exact j ranges | \(r_m\bmod u\) suffixes | \((r_m-r_0)\bmod u\) suffixes | result |
|---:|---:|---:|:--|:--|:--|:--|:--|
| 259 | 11 | 3 | …606060606060606060606061 | m=0:j=1..25; m=1:j=1..25; m=2:j=0..25 | …267408541862865460845642,964378238832562430542612,570438844893168491148673 | …0,606060606060606060606061,303030303030303030303031 | all fail U-SQ |
| 359 | 11 | 3 | …606060606060606060606061 | m=0:j=1..12; m=1:j=1..12; m=2:j=0..12 | …180442925167331580270715,786503531227937640876776,483473228197634610573746 | …0,606060606060606060606061,303030303030303030303031 | all fail U-SQ |
| 435 | 11 | 3 | …606060606060606060606061 | m=0:j=1..16; m=1:j=1..15; m=2:j=0..15 | …595135271259135575371677,292104968228832545068647,898165574289438605674708 | …0,606060606060606060606061,303030303030303030303031 | all fail U-SQ |
| 481 | 11 | 3 | …606060606060606060606061 | m=0:j=1..19; m=1:j=1..19; m=2:j=0..19 | …773555082386670852842987,470524779356367822539957,167494476326064792236927 | …0,606060606060606060606061,303030303030303030303031 | all fail U-SQ |
| 669 | 11 | 3 | …606060606060606060606061 | m=0:j=1..13; m=1:j=1..13; m=2:j=0..13 | …132099596068989161682858,829069293038686131379828,526038990008383101076798 | …0,606060606060606060606061,303030303030303030303031 | all fail U-SQ |
| 1025 | 11 | 3 | …606060606060606060606061 | m=0:j=1..25; m=1:j=1..25; m=2:j=0..24 | …145144421664010311724740,842114118633707281421710,448174724694313342027771 | …0,606060606060606060606061,303030303030303030303031 | all fail U-SQ |

For all 18 classes,

\[
(r_m-r_0)\bmod u=(me)\bmod u
\]

exactly.

### Historical q=11 primitive-gcd regressions

```text
q=11, g=471:   gcd(Z,u)=13, exact j range 1..28, U-SQ candidates 0
q=11, g=63501: gcd(Z,u)=13, exact j range 1..28, U-SQ candidates 0
```

Their **first logical death** is primitive gcd. The later U-SQ failure is only a secondary diagnostic and is not used to justify coprime factor allocation.

### Regular singleton diagnostic

All 50 regular A² fibres in this inherited corpus satisfy \(A>C_\ell q\). None has a legal third-A-digit carry. Thus Conjecture U1 receives strong finite support, but no global proof is claimed.

### Large-q diagnostic

The inherited 79-cell corpus contains no true large-\(q\) root fibre. A separate outer-pair census for \(6\le g\le12\) finds 28 pairs satisfying \(A\le C_\ell q\); these are **outer structural pairs, not promoted to admissible root states**. Their role is only to prevent a false inference from “none in the small-q regression” to “the chamber is empty.”

---

# Part XVI — Falsified / Corrected Conjecture Ledger

### Spacing A/C

**FALSE as stated.** The antipodal exception \(u=11,Z=5,5\leftrightarrow6\) shows that adjacent roots need not yield a proper small unitary divisor.

**Correct replacement:** small same-sign unitary factor **or global antipode**.

### U1 — Regular Third-Digit Mismatch

**OPEN uniformly.** Exact finite ledger: all 50 regular diagnostic fibres die at the A³/interval gate.

### U2 — Singular Content/U Incompatibility

**OPEN uniformly.** Exact finite ledger: all six solvable singular states / 18 fibres die at U-SQ. New theorem CSU-3 collapses the content multiplicity to at most 1 or 3 once \((\eta,j)\) is fixed.

### U3 — 3 mod 4 singular-prime extinction by common-U gcd

**NOT DERIVED.** The proposed common-scale contradiction is unavailable because primes dividing \(A\) do not divide \(V=uGH\).

### U4 — Mixed-sign roots force a small outer factor

**NOT TRUE from U-SQ alone.** A single translated hit does not control the unitary factors; the A² translation can place a chosen root cell at a small carry. Only the two-cell spacing theorem is valid without extra A-adic input.

### U5 — Large-q regular branch dies after one extra A-digit

**OPEN uniformly.** New result: the branch is first forced into \(2g\le3\ell+1\), then into the shorter \(n\)-interval and exact residual problem.

### U-SQ as an independent equation

**FALSE as an independence claim.** It is \(Q=0\pmod u\). The valid gain is dimensional: U-SQ acts after A-adic compression.

---

# Part XVII — Survivor Classification / Precise Next Frontier

J2 remains open, but the inherited obstruction is not repeated unchanged.

## Frontier R-S — Regular singleton

For fixed structural profile:

1. unique \(r_{A^2}\);
2. unique \(c_3\in[0,A)\);
3. if \(c_3\notin I_j\), death;
4. otherwise the only candidate is \(j=c_3\);
5. require
   \[
   (r_{A^2}+c_3)^2\equiv Z^2\pmod u;
   \]
6. define
   \[
   E_*=T_{A^2}(c_3).
   \]
   Then
   \[
   Au\mid E_*,
   \]
   and the exact root condition is \(E_*=0\).

Thus the survivor is

\[
\boxed{\textbf{one candidate + one exact zero test}.}
\]

## Frontier R-L — Regular large-q

Necessarily

\[
\boxed{2g\le3\ell+1.}
\]

Write

\[
j=c_3+An,
\qquad
0\le n<\frac{C_\ell q-c_3}{A}.
\]

Then

\[
(r_{A^2}+c_3+n)^2\equiv Z^2\pmod u,
\]

and every surviving candidate has

\[
Au\mid E(n),
\qquad E(n)=0\text{ iff exact root}.
\]

This is the only regular non-singleton frontier.

## Frontier S — Singular

Choose one unitary root cell

\[
\rho=\eta Z\pmod u.
\]

For each legal carry \(j\), set

\[
\boxed{m\equiv d(\rho-r_0-j)\pmod u.}
\]

Then:

- if \(1<d<A\), there is at most one \(m\in[0,d)\);
- if \(d=A\), there are at most three.

For each selected \(m\), the only remaining condition is

\[
\boxed{T_{r_m}(j)=0.}
\]

with U-SQ already built into the selection. If the residual is nonzero, it is a nonzero multiple of \(u\).

So the singular obstruction is now exactly

\[
\boxed{
\textbf{one unitary cell}
+\textbf{one carry }j
+\le3\textbf{ selected content fibres}
+\textbf{one exact residual}.}
\]

No new long-lived quotient is introduced.

---

# Part XVIII — J2 Closure Status and File Audit

\[
\boxed{\textbf{J2 OPEN}}
\]

No file named `J2-Resonance-Closure-Certificate.md` is generated, because a global extinction theorem has not been proved.

The new theorem package is:

```text
USQ-1  Primitive U-Coprimality: PROVED
USQ-2  Complementary Unitary Sign Allocation: PROVED
USQ-3  Short-Carry CRT: PROVED
USQ-4  Regular Third-A-Digit Synchronization: PROVED as synchronization, not extinction
CSU-1  Content-to-U Bridge: PROVED
CSU-2  Singular U-SQ Progression: PROVED
CSU-3  Fixed-(root cell,j) content multiplicity <=1 proper / <=3 maximal: PROVED
LQ-1   Regular non-singleton => 2g <= 3ell+1: PROVED from inherited OUTER
ROOT-EX Candidate excess Au-divisibility after A3+U-SQ: PROVED
FULL-J2 Extinction: NOT PROVED
```

Generated files:

```text
J2-55-R2-USquare-Carry-Collision-Report.md
J2-55-R2-USquare-symbolic.py
J2-55-R2-USquare-search.py
J2-55-R2-USquare-certificate.txt
J2-55-R2-USquare-survivors.tsv
J2-55-R2-USquare-search-certificate.txt
```

`J2-Resonance-Closure-Certificate.md` is intentionally absent.

FINAL_REPORT_FILE: `J2-55-R2-USquare-Carry-Collision-Report.md`  
SYMBOLIC_FILE: `J2-55-R2-USquare-symbolic.py`  
COMPUTATION_FILE: `J2-55-R2-USquare-search.py`  
CERTIFICATE_FILE: `J2-55-R2-USquare-certificate.txt`  
SURVIVOR_FILE: `J2-55-R2-USquare-survivors.tsv`  
J2_CLOSURE_CERTIFICATE_FILE: `NOT_GENERATED_BECAUSE_OPEN`
