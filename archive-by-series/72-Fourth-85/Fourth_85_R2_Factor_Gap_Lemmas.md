# Fourth 85 · R2 — Factor-Gap Lemma Package

## Standing q=1 negative shell

Fix one historical negative case

\[
K=10^k,\qquad k\in\{1,2,3\},\qquad G=10^g,\qquad g-k\ge2,
\]

with one of

\[
(d,\tau)\in\{(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)\}.
\]

Let

\[
\rho=a-\frac{\tau G}{10}>0,
\qquad
31\rho+\tau\equiv0\pmod{2K},
\]

\[
\gcd(\rho,10\tau)=1,
\qquad
0<\rho<\frac{10-d\tau}{10d}G.
\]

Under the R1 square condition write

\[
Y_0=2Ky,\qquad \gcd(y,10)=1,
\]

and

\[
L=y-\rho,\qquad R=y+\rho.
\]

Then

\[
LR=2^g5^{g-1}\eta=\frac G5\eta,
\qquad \gcd(\eta,10)=1.
\]

---

## Lemma 1 — Live endpoint and exact difference valuations

The historical shell already has

\[
g\ge k+2\ge3.
\]

Hence no actual \(g=1,2\) endpoint survives into this round. Moreover

\[
v_2(R-L)=v_2(2\rho)=1,
\qquad
v_5(R-L)=0.
\]

For \(g\ge3\), the R1 valuation sets

\[
\{v_2(L),v_2(R)\}=\{1,g-1\},
\qquad
\{v_5(L),v_5(R)\}=\{0,g-1\}
\]

are unequal at both primes, so the ultrametric minimum rule reproduces exactly the same difference valuations. It therefore kills none of the four orientations.

A formal \(g=2\) inspection would force \(v_2(L)=v_2(R)=1\), hence \(v_2(R-L)\ge2\), contradicting \(v_2(2\rho)=1\).

---

## Lemma 2 — Positivity of both factors

For the fixed conic

\[
Y_0^2=A_2a^2+B_1a+C_0
\]

substitute \(a=\tau G/10+\rho\). Exact symbolic expansion gives

\[
Y_0^2-(2K\rho)^2=C_2\rho^2+C_1\rho+C_0',
\]

where

\[
C_2=G\Bigl[K^2(100G^5+280G^4+236G^3+16G^2-52G-8)
-(100G^5+380G^4+545G^3+362G^2+93G)\Bigr],
\]

\[
C_1=\frac{G\tau}{5}\Bigl[K^2(40G^5+76G^4+16G^3-32G^2-8G+4)
-(40G^5+120G^4+132G^3+73G^2+15G)\Bigr],
\]

and

\[
C_0'=\frac{G^2\tau^2}{100}\Psi_K(G),
\]

\[
\boxed{\Psi_K(G)=K^2(16G^4+16G^3-12G^2-8G+4)
-(20G^4+52G^3+53G^2+30G).}
\]

For \(G\ge10\), \(K\ge10\), all three bracketed coefficients are positive. For example,

\[
16G^4+16G^3-12G^2-8G+4>16G^4,
\]

while

\[
20G^4+52G^3+53G^2+30G<26G^4,
\]

so the \(C_0'\) bracket is \(>1600G^4-26G^4>0\). The other two are even more separated by the factor \(K^2\ge100\).

Thus, since \(\rho,\tau>0\),

\[
Y_0^2>(2K\rho)^2.
\]

Taking \(y=|Y_0|/(2K)>0\),

\[
\boxed{y>\rho>0},
\]

hence

\[
\boxed{0<L<R}.
\]

---

## Lemma 3 — The four exact orientation templates

For \(g\ge3\), there are exactly four templates. Write all quotient variables below as positive ten-units.

### A — same-side high \(2\) and high \(5\) on \(L\)

\[
\boxed{L=10^{g-1}\ell,\qquad R=2r.}
\]

Then

\[
\boxed{r=\frac G{20}\ell+\rho},
\qquad
\eta=\ell r.
\]

### B — high \(2\) on \(L\), high \(5\) on \(R\)

\[
\boxed{L=2^{g-1}\ell,\qquad R=2\cdot5^{g-1}r.}
\]

Then

\[
\boxed{5^{g-1}r-2^{g-2}\ell=\rho},
\qquad
\eta=\ell r.
\]

### C — high \(5\) on \(L\), high \(2\) on \(R\)

\[
\boxed{L=2\cdot5^{g-1}\ell,\qquad R=2^{g-1}r.}
\]

Then

\[
\boxed{2^{g-2}r-5^{g-1}\ell=\rho},
\qquad
\eta=\ell r.
\]

### D — same-side high \(2\) and high \(5\) on \(R\)

\[
\boxed{L=2\ell,\qquad R=10^{g-1}r.}
\]

Then

\[
\boxed{\ell=\frac G{20}r-\rho},
\qquad
\eta=\ell r.
\]

No orientation dies from sign, parity, \(5\)-adic difference, or the source window.

---

## Lemma 4 — Exact gcd theorem

Let

\[
h:=\gcd(y,\rho).
\]

Because \(y,\rho\) are odd,

\[
\gcd(y-\rho,y+\rho)
=h\gcd(y/h-\rho/h,y/h+\rho/h)=2h.
\]

Therefore

\[
\boxed{D:=\gcd(L,R)=2\gcd(y,\rho).}
\]

In particular

\[
\boxed{v_2(D)=1,\qquad v_5(D)=0.}
\]

In every one of the four templates the forced decimal cores have no additional common \(2/5\)-part, hence

\[
\boxed{\gcd(\ell,r)=h}.
\]

Consequently

\[
\boxed{h^2\mid\eta}.
\]

---

## Lemma 5 — Source-forced destination of every odd common prime

If an odd prime \(p\mid h\), then \(p\nmid10KG\tau\). Reducing the exact conic modulo \(p\), using \(\rho\equiv y\equiv0\pmod p\) and hence \(a\equiv\tau G/10\pmod p\), gives

\[
0\equiv \frac{G^2\tau^2}{100}\Psi_K(G)\pmod p.
\]

The prefactor is invertible modulo \(p\). Thus

\[
\boxed{p\mid\Psi_K(G)}.
\]

Equivalently,

\[
\boxed{h\mid\Psi_K(G)}.
\]

For the three fixed \(K\)'s,

\[
\Psi_{10}=1580G^4+1548G^3-1253G^2-830G+400,
\]

\[
\Psi_{100}=159980G^4+159948G^3-120053G^2-80030G+40000,
\]

\[
\Psi_{1000}=15999980G^4+15999948G^3-12000053G^2-8000030G+4000000.
\]

This is a genuine odd-prime destination theorem, but it is **not fixed-\(S\) support** because \(\Psi_K(10^g)\) moves with \(g\).

---

## Lemma 6 — Deep decimal-unit law

R1 gave

\[
\eta=\frac{\sum_{j=0}^5 C_jG^j}{80K^2},
\]

with

\[
\frac{C_0}{80K^2}=\rho(\tau-10\rho).
\]

The coefficient valuation gaps imply that every \(j\ge1\) term is divisible after normalization by

\[
2^{e_2},\qquad e_2:=g-k-1\ge1,
\]

and by

\[
5^{e_5},\qquad e_5:=g-k+\min(k,2)-1\ge2.
\]

Hence

\[
\boxed{\eta\equiv\rho(\tau-10\rho)\pmod{2^{e_2}}},
\]

\[
\boxed{\eta\equiv\rho(\tau-10\rho)\pmod{5^{e_5}}}.
\]

The R1 last-digit law \(\eta\equiv\rho\tau\pmod{10}\) is the first visible decimal shadow of this stronger statement.

For A, the gap implies \(r\equiv\rho\) modulo both deep prime powers, so

\[
\boxed{\ell\equiv\tau-10\rho}
\]

modulo both. For D,

\[
\boxed{r\equiv10\rho-\tau}
\]

modulo both.

For B and C, the two prime-power requirements land on complementary quotient variables and are simultaneously soluble by one CRT lift of the exact one-parameter gap solution.

---

## Lemma 7 — Exact-eta return theorem

Let \(E\) denote the **full exact** value of \(\eta\) supplied by the conic:

\[
E=\eta=\frac{5}{4K^2G}\bigl(Y_0^2-(2K\rho)^2\bigr).
\]

Attempting to use the full \(E\), rather than merely its residues, does not create a new lower-dimensional Diophantine object.

For A,

\[
E=\ell\left(\frac G{20}\ell+\rho\right),
\]

so

\[
G\ell^2+20\rho\ell-20E=0.
\]

Its discriminant is

\[
(20\rho)^2+80GE
=400\left(\rho^2+\frac G5E\right)
=(20y)^2.
\]

D gives the same discriminant.

For B, with \(P=2^{g-2}\), \(Q=5^{g-1}\),

\[
P\ell^2+\rho\ell-QE=0,
\]

whose discriminant is

\[
\rho^2+4PQE
=\rho^2+\frac G5E
=y^2.
\]

C gives the same discriminant.

Therefore

\[
\boxed{\text{orientation parameterization + full exact }\eta
\text{ returns exactly to the original square condition}.}
\]

It is a re-coordinate, not a dimension drop or fixed-object extraction.

---

## Lemma 8 — Counterexample guillotine for the extracted factor-gap system

Fix any source-admissible \(\rho\) in one of the historical cases. Let

\[
M_{\rm deep}=2^{e_2}5^{e_5}.
\]

Each orientation has infinitely many positive ten-unit quotient pairs \((\ell,r)\) satisfying simultaneously:

1. the exact orientation valuations;
2. the exact gap \(R-L=2\rho\);
3. the deep \(2\)- and \(5\)-adic \(\eta\) congruences of Lemma 6;
4. \(\eta=\ell r\);
5. \(\gcd(\ell,r)=1\), hence \(h=1\), so the odd-prime destination theorem is vacuous but satisfied.

For A and D, choose the forced deep residue class of the one free quotient and lift by multiples of \(M_{\rm deep}\). Since \(\gcd(M_{\rm deep},\rho)=1\), finitely many residue classes can be avoided to ensure coprimality with \(\rho\).

For B and C, the exact linear gap has one integer parameter. The deep \(2\)-condition fixes that parameter modulo \(2^{e_2}\), the deep \(5\)-condition fixes it modulo \(5^{e_5}\), and CRT gives one class modulo \(M_{\rm deep}\). For each odd prime dividing \(\rho\), at most one further residue class of the lift parameter makes both quotients divisible by that prime; avoid these finitely many classes.

Thus the extracted decimal-core/factor-gap system itself has infinite pseudo-families in **all four** orientations.

This does not construct a source solution of the original conic. It proves that the extracted factor-gap consequences cannot by themselves close the branch.

---

## Terminal lemma verdict

\[
\boxed{\texttt{VALUATION\_ORIENTATION\_COLLAPSED=NO}}
\]

\[
\boxed{\texttt{FIXED\_S\_SUPPORT=NO}}
\]

\[
\boxed{\texttt{FACTOR\_GAP\_DIMENSION\_DROP=NO}}
\]

\[
\boxed{\texttt{FACTOR\_GAP\_ARCHITECTURE\_DEAD}}
\]

The exact valuation allocation remains a permanent structural asset; what dies is the claim that decimal-core allocation plus additive gap can, without an additional independent source/norm constraint, force \(q=1\) extinction.
