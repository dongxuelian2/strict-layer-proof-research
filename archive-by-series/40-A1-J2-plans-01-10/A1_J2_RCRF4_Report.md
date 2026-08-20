# A1 J2 RCRF4 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** Positive Bézout-Cell Extinction × Negative \(k=2g\) Boundary Closure × Deficiency-Layer Launch  
**Status date:** 2026-08-16  
**Inherited source:** `A1_J2_CZDR_Report.md`  
**Computation:** `A1_J2_RCRF4_search.py`  
**Certificate:** `A1_J2_RCRF4_certificate.txt`  
**Linear-survivor ledger:** `A1_J2_RCRF4_survivors.tsv`

---

# Part I — Executive Status

\[
\boxed{\textbf{Positive J2 CLOSED}}
\]

\[
\boxed{\textbf{Negative }k=2g\textbf{ CLOSED}}
\]

\[
\boxed{\ell=1\textbf{ CLOSED}}
\]

but

\[
\boxed{\textbf{Full J2 OPEN}}.
\]

This round therefore attains **Success B**, **Success C1**, **Success C2**, and a stronger form of **Success C3**.

The main surprise is that the requested linear-first strategy was necessary but **linear extinction itself is false**.

Two exact linear survivors were found:

\[
\boxed{
(g,q,N,t)=(2385,19,-1,45)
}
\]

in the positive branch, and

\[
\boxed{
(g,q,N,t)=(39,7,3,17)
}
\]

in the negative \(k=2g\) boundary.

Both pass the complete linear RCE package, the actual digit conditions, sign conditions, ten-unit conditions, and the inherited radial bounds.  Thus:

\[
\boxed{
\text{PBZ/NBZ + digit window alone is not a uniform closure engine.}
}
\]

What closes the chambers is the next gate, but not by returning to a generic discriminant search.  The decisive new splice is

\[
\boxed{
a_1>\frac{AG}{10},
}
\tag{DRL}
\]

obtained by combining the **second actual numerator digit window** with the radialized J2.5 equation.  Once this is multiplied by the forced decimal core in the complementary root factor \(\Lambda\), the root-factor lower bound becomes too large to coexist with the inherited radial upper bound on

\[
\widetilde F=A\mathcal X^2+ZD_2.
\]

The resulting closures are:

\[
\boxed{
J=2,\quad S_R>0\Longrightarrow\varnothing,
}
\tag{POS-CLOSE}
\]

\[
\boxed{
J=2,\quad S_R<0,\quad k=2g\Longrightarrow\varnothing.
}
\tag{B-CLOSE}
\]

Therefore the negative remainder satisfies

\[
\boxed{
k\le2g-1.
}
\]

After defining

\[
\ell:=2g-k\ge1,
\]

the same root-factor/digit splice yields the new **Deficiency Wedge Theorem**:

\[
\boxed{
q>1\Longrightarrow g\le3\ell,
}
\tag{DW+}
\]

\[
\boxed{
q=1\Longrightarrow g\le3\ell+2.
}
\tag{DW1}
\]

Consequently fixed deficiency is automatically finite.

In particular:

\[
\boxed{
\ell=1\Longrightarrow\varnothing.
}
\tag{ELL1-CLOSE}
\]

Hence the new unique J2 frontier is

\[
\boxed{
J=2,\qquad
S_R<0,\qquad
\ell\ge2,
}
\]

with the stronger wedge

\[
\boxed{
\begin{cases}
q>1:& g\le3\ell,\\
q=1:& g\le3\ell+2.
\end{cases}}
\tag{NEW-WEDGE}
\]

Together with the inherited \(g=2,3\) and \(u=1\) closures, the live bulk may be written as

\[
\boxed{
J=2,\quad S_R<0,\quad g\ge4,\quad u>1,\quad \ell\ge2,
}
\]

subject to (NEW-WEDGE).

---

# Part II — Frozen RCE Ledger

Throughout,

\[
G=10^g,\qquad
H=\frac G2,\qquad
K=10^k,
\]

\[
u\mid G+1,\qquad
q=\frac{G+1}{u},\qquad
uq=G+1,
\]

\[
A=2u+1.
\]

The inherited J2 determinant identity is

\[
\boxed{
qA=2G+q+2.
}
\tag{AQ}
\]

The actual-radial variables are

\[
N=Uj,\qquad
Z=Uz,\qquad
a_3=Uc,
\]

and the frozen Radial Cyclotomic Euclidean system is

\[
\boxed{
2Aa_3=q(G-1)Z-N,
}
\tag{RCE1}
\]

\[
\boxed{
(G-1)t=2(q+4)a_3+qN,
}
\tag{RCE2}
\]

\[
\boxed{
q(q+4)Z=At-2N.
}
\tag{RCE3}
\]

Thus

\[
\boxed{
a_3=
\frac{(G-1)t-qN}{2(q+4)},
}
\tag{RA3}
\]

\[
\boxed{
Z=
\frac{At-2N}{q(q+4)}.
}
\tag{RZ}
\]

Also

\[
\boxed{
\mathcal X=UX=\frac{Z+uN}{2},
}
\tag{RX}
\]

\[
\boxed{
D_2=Ud_2=ua_3+G\mathcal X.
}
\tag{RD2}
\]

The exact third actual digit window is

\[
\boxed{
\frac G{10}\le a_3<G.
}
\tag{DIG3}
\]

The exact second actual digit window is

\[
\boxed{
\frac{G^2K}{10}\le a_2<G^2K,
\qquad a_2:=UC_2.
}
\tag{DIG2}
\]

The root-factor system is

\[
\boxed{
a_1\Lambda=\widetilde F,
}
\tag{RLR2}
\]

\[
\boxed{
AH^2a_1+\Lambda=2uKD_2,
}
\tag{RLR1}
\]

where

\[
a_1:=UC_1,
\qquad
\widetilde F:=A\mathcal X^2+ZD_2.
\]

The forced decimal root core is

\[
\boxed{
D_{g,k}
=
2^{\min(k+1,2g-2)}
5^{\min(k,2g)}
\mid\Lambda,\widetilde F.
}
\tag{DC}
\]

The inherited J2 equations also force

\[
\boxed{
\gcd(A,10)=1.
}
\tag{A10}
\]

Hence the nominal \(5\mid A\) chamber is not live.

Finally, inherited complete closures remain frozen:

\[
\boxed{
g=2\Longrightarrow\varnothing,
\qquad
g=3\Longrightarrow\varnothing,
}
\]

\[
\boxed{
u=1\Longrightarrow\varnothing.
}
\]

So all new uniform arguments below may assume

\[
g\ge4,\qquad G\ge10^4.
\]

---

# Part III — Positive Bézout Cell

Assume

\[
S_R>0.
\]

The previous round gives, after removing \(q=1\),

\[
U=1,\qquad N=-1.
\]

Thus RCE3 becomes

\[
q(q+4)Z=At+2,
\]

and the positive Bézout congruence is

\[
\boxed{
At\equiv-2\pmod{q(q+4)}.
}
\tag{PBZ}
\]

## 3.1 Exact gcd solvability lemma

First,

\[
\gcd(A,u)=1
\]

because \(A=2u+1\).  Since

\[
G+1=uq,
\]

we obtain

\[
\boxed{
\gcd(A,q)=\gcd(A,G+1).
}
\tag{GQ}
\]

Next, from (AQ),

\[
q+4\equiv2(1-G)\pmod A.
\]

Because \(A\) is odd,

\[
\boxed{
\gcd(A,q+4)=\gcd(A,G-1).
}
\tag{GQ4}
\]

Also

\[
\gcd(q,q+4)=1
\]

because both are odd and their difference is \(4\).  Similarly the two odd \(A\)-parts of \(G-1\) and \(G+1\) are coprime.

Therefore

\[
\boxed{
d:=\gcd(A,q(q+4))
=
\gcd(A,G^2-1).
}
\tag{GCD}
\]

Since \(d\) is odd, PBZ is solvable iff

\[
d\mid2,
\]

hence iff

\[
\boxed{d=1.}
\tag{PBZ-SOLV}
\]

So the positive congruence is either dead immediately or has exactly one residue class modulo

\[
M=q(q+4).
\]

When \(d=1\), define

\[
\boxed{
t_0\equiv-2A^{-1}\pmod{q(q+4)},
\qquad
1\le t_0\le q(q+4).
}
\]

This is the exact unique Bézout residue.

## 3.2 Exact digit window and the \(r>0\) refinement

With \(N=-1\),

\[
a_3=
\frac{(G-1)t+q}{2(q+4)}.
\]

The raw digit window gives the exact half-open interval

\[
\boxed{
\frac{(q+4)G/5-q}{G-1}
\le t
<
\frac{2(q+4)G-q}{G-1}.
}
\tag{P-TDIG}
\]

However the positive primitive remainder \(r\) gives a sharper lower endpoint.

Eliminating \(Z,a_3\) from the radial formulas gives

\[
\boxed{
4q(q+4)r
=
G\bigl((q+2)t-q(q+4)\bigr)
+
2(t-q).
}
\tag{P-R}
\]

The right side is strictly increasing in \(t\).

At \(t=q+1\),

\[
G(2-q)+2<0
\]

for \(q\ge7\), whereas at \(t=q+2\),

\[
4G+4>0.
\]

Hence

\[
\boxed{
r>0
\Longleftrightarrow
t\ge q+2.
}
\tag{P-LOW}
\]

For the remaining nonextreme chamber \(u>1,q>1\), both \(u\) and \(q\) are nontrivial divisors of \(G+1\), hence at least \(7\).  Thus \(q\ll G\), and the strict digit upper endpoint yields

\[
\boxed{
t\le2q+8.
}
\tag{P-UP}
\]

Therefore the actual effective positive Bézout cell is

\[
\boxed{
q+2\le t\le2q+8,
\qquad
At\equiv-2\pmod{q(q+4)}.
}
\tag{P-CELL}
\]

The window is much shorter than one full modulus, so there is at most one candidate, but this round does **not** stop at that statement.

## 3.3 Linear extinction conjecture is false

The candidate does sometimes exist.

The exact computation certifies

\[
\boxed{
g=2385,\quad q=19,\quad N=-1,\quad t=45.
}
\tag{P-WIT}
\]

Here

\[
q+2=21\le45\le46=2q+8,
\]

PBZ holds, and the reconstructed state satisfies all of:

- \(a_3\) is a legal actual digit and a ten-unit;
- \(Z\) is a positive ten-unit;
- \(\mathcal X<0\), with \(W:=-\mathcal X\) a ten-unit;
- \(D_2,h,m,r>0\) and are ten-units;
- \(0<W<u\);
- \(ZG<2uA\);
- RCE1, RCE2, RCE3 exactly.

Its last two decimal digits are

\[
a_3\equiv69,\quad
Z\equiv61,\quad
W\equiv09,\quad
D_2\equiv51,
\]

\[
h\equiv29,\quad
m\equiv11,\quad
r\equiv49
\pmod{100}.
\]

So both conjectures

\[
\text{“PBZ is never solvable”}
\]

and

\[
\text{“the unique PBZ residue never enters the digit window”}
\]

are false as uniform closure principles.

This is why the root-factor gate is genuinely necessary.

## 3.4 The decisive digit-root lower splice

Radialize J2.5:

\[
GKC_1=AC_2+m.
\]

Multiplying by \(U\) gives

\[
\boxed{
GKa_1=Aa_2+M,
\qquad
M:=Um>0.
}
\tag{J25-R}
\]

Using the actual second digit lower bound

\[
a_2\ge\frac{G^2K}{10},
\]

we get

\[
GKa_1
>
A\frac{G^2K}{10}.
\]

Therefore

\[
\boxed{
a_1>\frac{AG}{10}.
}
\tag{DRL}
\]

This inequality is independent of sign and independent of \(k\).  It is the key new splice of this round.

## 3.5 Positive root-factor lower bound

For \(S_R>0\),

\[
k\ge2g-1.
\]

Hence the decimal core always contains

\[
\boxed{
\frac{H^2}{5}\mid\Lambda.
}
\]

Since \(\Lambda>0\),

\[
\Lambda\ge\frac{H^2}{5}.
\]

Using

\[
\widetilde F=a_1\Lambda
\]

and (DRL),

\[
\widetilde F
>
\frac{AG}{10}\cdot\frac{H^2}{5}.
\]

As

\[
H^2=\frac{G^2}{4},
\]

we obtain

\[
\boxed{
\widetilde F>\frac{AG^3}{200}.
}
\tag{P-LOWF}
\]

## 3.6 Positive radial upper bound

In the positive branch,

\[
0<W<u,
\]

\[
Z<\frac{2uA}{G},
\]

and

\[
D_2=ua_3-GW<ua_3<uG.
\]

Therefore

\[
\begin{aligned}
\widetilde F
&=AW^2+ZD_2\\
&<Au^2+
\frac{2uA}{G}\cdot uG\\
&=3Au^2.
\end{aligned}
\]

Thus

\[
\boxed{
\widetilde F<3Au^2.
}
\tag{P-UPF}
\]

Combining (P-LOWF) and (P-UPF),

\[
\frac{AG^3}{200}<3Au^2,
\]

so

\[
\boxed{
G^3<600u^2.
}
\tag{P-SIZE}
\]

For \(q>1\), the cyclotomic divisor restrictions give \(q\ge7\), hence

\[
u=\frac{G+1}{q}\le\frac{G+1}{7}.
\]

Thus

\[
G^3
<
\frac{600}{49}(G+1)^2.
\]

Since \(G+1<2G\),

\[
G<\frac{2400}{49}<49,
\]

contradicting \(G\ge10^4\).

Therefore

\[
\boxed{
g\ge4,\quad S_R>0,\quad q>1
\Longrightarrow\varnothing.
}
\]

The \(q=1\) positive chamber was already uniformly closed in the previous round, while \(g=2,3\) are frozen complete closures.

Hence

\[
\boxed{
J=2,\quad S_R>0
\Longrightarrow\varnothing.
}
\tag{POSITIVE-CLOSED}
\]

This is **Success C1**.

---

# Part IV — Positive Alternative \(Z\)-Coordinates

The proposed double divisibility is

\[
A\mid q(q+4)Z-2,
\tag{Z1}
\]

\[
2A\mid q(G-1)Z+1.
\tag{Z2}
\]

It does **not** give an independent contradiction.

From (AQ),

\[
q+4\equiv2(1-G)\pmod A.
\]

Therefore

\[
\begin{aligned}
q(q+4)Z-2
&\equiv
2q(1-G)Z-2\\
&=
-2\bigl(q(G-1)Z+1\bigr)
\pmod A.
\end{aligned}
\]

Since \(A\) is odd,

\[
\boxed{
A\mid q(q+4)Z-2
\Longleftrightarrow
A\mid q(G-1)Z+1.
}
\tag{Z-EQ1}
\]

Moreover \(q,G-1,Z\) are odd, so

\[
q(G-1)Z+1
\]

is automatically even.  Because \(\gcd(A,2)=1\),

\[
\boxed{
A\mid q(G-1)Z+1
\Longleftrightarrow
2A\mid q(G-1)Z+1.
}
\tag{Z-EQ2}
\]

Thus the two \(Z\)-divisibilities are exactly the same arithmetic condition in disguise.

So:

\[
\boxed{
\textbf{Double divisibility in }Z
\textbf{ has no independent killing power.}
}
\]

This route is retired.

---

# Part V — Negative \(k=2g\) Bézout Cells

Now assume

\[
S_R<0,\qquad k=2g.
\]

The inherited \(q=1\) chamber is already closed, so consider \(q>1\).

The previous round gives

\[
N\in\{1,3,5\}.
\]

RCE3 becomes

\[
q(q+4)Z=At-2N,
\]

hence

\[
\boxed{
At\equiv2N\pmod{q(q+4)}.
}
\tag{NBZ}
\]

## 5.1 Unified gcd classification

The same exact gcd lemma applies:

\[
d=\gcd(A,q(q+4))
=\gcd(A,G^2-1).
\]

NBZ is solvable iff

\[
d\mid2N.
\]

Since \(d\) is odd,

\[
\boxed{
d\mid N.
}
\tag{NBZ-SOLV}
\]

Thus:

- \(N=1\): necessarily \(d=1\);
- \(N=3\): \(d\in\{1,3\}\);
- \(N=5\): since \(5\nmid A\), again necessarily \(d=1\).

So the suggested \(5\mid A\) split disappears entirely: that chamber was already impossible.

The exact digit interval is

\[
\boxed{
\frac{(q+4)G/5+qN}{G-1}
\le t
<
\frac{2(q+4)G+qN}{G-1}.
}
\tag{N-TDIG}
\]

## 5.2 Negative linear extinction conjecture is false

There is a genuine boundary linear survivor:

\[
\boxed{
g=39,\quad
q=7,\quad
N=3,\quad
t=17.
}
\tag{N-WIT}
\]

It passes:

- NBZ;
- the exact digit interval;
- RCE1–RCE3;
- \(a_3,Z,\mathcal X,D_2,h,m,r\) positivity;
- all corresponding ten-unit checks;
- the inherited \(k=2g\) UW/UZ inequalities.

Its last two decimal digits are

\[
a_3\equiv71,\quad
Z\equiv49,\quad
\mathcal X\equiv89,\quad
D_2\equiv53,
\]

\[
h\equiv23,\quad
m\equiv01,\quad
r\equiv47
\pmod{100}.
\]

Therefore

\[
\boxed{
\text{Negative }k=2g
\text{ is not linearly empty.}
}
\]

So the root-factor gate is again genuinely required.

---

# Part VI — Boundary Root-Factor Reduction

## 6.1 Exact \(H^2\)-core

At

\[
k=2g,
\]

the decimal core is

\[
D_{g,2g}
=
2^{2g-2}5^{2g}
=
H^2.
\]

Hence

\[
\boxed{
H^2\mid\lambda,F
}
\]

in primitive coordinates, and

\[
\boxed{
H^2\mid\Lambda,\widetilde F
}
\]

in actual-radial coordinates.

Thus C4 from the prompt is confirmed.

## 6.2 Scale cancellation identity

Write

\[
\lambda=H^2\mu.
\]

The primitive root-factor equation

\[
AH^2C_1+\lambda=2uKd_2
\]

becomes

\[
AH^2C_1+H^2\mu=2uG^2d_2.
\]

Since

\[
G^2=4H^2,
\]

division by \(H^2\) gives

\[
\boxed{
AC_1+\mu=8ud_2.
}
\tag{B-RF}
\]

Also

\[
\boxed{
F=H^2C_1\mu.
}
\]

Thus C5 from the prompt is algebraically correct.

The radial version is obtained by writing

\[
\Lambda=H^2M:
\]

\[
\boxed{
Aa_1+M=8uD_2,
}
\tag{B-RF-R}
\]

\[
\boxed{
\widetilde F=H^2a_1M.
}
\]

The large decimal powers have indeed disappeared from the normalized sum equation.

## 6.3 The decisive boundary lower bound

Because

\[
H^2\mid\Lambda
\]

and \(\Lambda>0\),

\[
\Lambda\ge H^2.
\]

Then

\[
\widetilde F=a_1\Lambda
\ge a_1H^2.
\]

Using the universal digit-root lower splice

\[
a_1>\frac{AG}{10},
\]

we get

\[
\boxed{
\widetilde F>\frac{AG^3}{40}.
}
\tag{B-LOWF}
\]

## 6.4 Frozen boundary upper bound

At \(k=2g\), the previous radial estimates give

\[
\mathcal X<\eta u,
\]

\[
Z<
\frac{2\eta u}{G^2}
+
\frac{2uA}{G},
\]

\[
D_2<(1+\eta)uG,
\]

with

\[
\eta<\frac{1299}{500}=2.598.
\]

The previous round already proved from these that

\[
\boxed{
\widetilde F<14Au^2
\qquad(G\ge10^4).
}
\tag{B-UPF}
\]

Combining (B-LOWF) and (B-UPF),

\[
\frac{AG^3}{40}<14Au^2,
\]

so

\[
\boxed{
G^3<560u^2.
}
\tag{B-SIZE}
\]

For \(q>1\), again \(q\ge7\), hence

\[
u\le\frac{G+1}{7}.
\]

Therefore

\[
G^3
<
\frac{560}{49}(G+1)^2
<
\frac{2240}{49}G^2,
\]

so

\[
G<\frac{2240}{49}<46,
\]

contradicting \(G\ge10^4\).

Therefore

\[
\boxed{
S_R<0,\quad k=2g,\quad q>1
\Longrightarrow\varnothing.
}
\]

Together with the inherited \(q=1\) closure,

\[
\boxed{
J=2,\quad S_R<0,\quad k=2g
\Longrightarrow\varnothing.
}
\tag{NEG-2G-CLOSED}
\]

This is **Success C2**.

Both high-depth linear witnesses recorded in this report fail the forced decimal core before any square-root search is needed.  In particular, the negative witness has

\[
v_5(\widetilde F)=0
\]

while the \(k=2g\) root core requires

\[
v_5(\widetilde F)\ge2g.
\]

---

# Part VII — Deficiency Launch

Because both principal boundary chambers are now closed, the deficiency layer is legitimately activated.

Define

\[
\boxed{
\ell:=2g-k\ge1.
}
\]

Put

\[
L:=10^\ell.
\]

Then

\[
K=\frac{G^2}{L}.
\]

## 7.1 Exact decimal-core ledger

For \(k=2g-\ell\),

\[
v_5(D_{g,k})=2g-\ell.
\]

For \(v_2\),

\[
v_2(D_{g,k})
=
\min(2g-\ell+1,2g-2).
\]

Hence:

### \(\ell=1\)

\[
\boxed{
D_{g,2g-1}
=
2^{2g-2}5^{2g-1}
=
\frac{H^2}{5}
=
\frac{G^2}{20}.
}
\tag{D1}
\]

### \(\ell=2\)

\[
\boxed{
D_{g,2g-2}
=
2^{2g-2}5^{2g-2}
=
10^{2g-2}
=
\frac{G^2}{100}.
}
\tag{D2}
\]

### \(\ell\ge3\)

\[
\boxed{
D_{g,2g-\ell}
=
2^{2g-\ell+1}5^{2g-\ell}
=
2\cdot10^{2g-\ell}
=
2K.
}
\tag{D3}
\]

In particular, uniformly for every \(\ell\ge1\),

\[
\boxed{
D_{g,2g-\ell}
\ge
\frac{G^2}{2L}.
}
\tag{D-UNIF}
\]

## 7.2 Canonical \(\ell=1\) factor pair

At \(\ell=1\),

\[
\lambda=\frac{H^2}{5}\mu.
\]

Then

\[
AH^2C_1+\frac{H^2}{5}\mu
=
2u\frac{G^2}{10}d_2.
\]

Dividing by \(H^2/5\) gives

\[
\boxed{
5AC_1+\mu=4ud_2.
}
\tag{ELL1-RF}
\]

Also

\[
\boxed{
F=\frac{H^2}{5}C_1\mu.
}
\]

The radial form is

\[
\boxed{
5Aa_1+M=4uD_2,
}
\]

\[
\boxed{
\widetilde F=\frac{H^2}{5}a_1M.
}
\]

Thus the \(\ell=1\) root gate is already a scale-free factor-pair problem.

## 7.3 General negative deficiency upper bound

For \(K=G^2/L\), the inherited negative radial estimates become

\[
\boxed{
\mathcal X<\eta Lu,
}
\tag{DEF-W}
\]

\[
\boxed{
Z<
\frac{2\eta Lu}{G^2}
+
\frac{2uA}{G}.
}
\tag{DEF-Z}
\]

Since \(a_3<G\),

\[
D_2=ua_3+G\mathcal X
<
(1+\eta L)uG.
\]

Hence

\[
\begin{aligned}
\widetilde F
&=
A\mathcal X^2+ZD_2\\
&<
A\eta^2L^2u^2
+
\left(
\frac{2\eta Lu}{G^2}
+
\frac{2uA}{G}
\right)
(1+\eta L)uG.
\end{aligned}
\]

Therefore

\[
\widetilde F
<
Au^2
\left[
\eta^2L^2+2(1+\eta L)
\right]
+
\frac{2\eta L(1+\eta L)}{G}u^2.
\]

Using

\[
A\ge3,\qquad
G\ge10^4,\qquad
L\ge10,\qquad
\eta<2.598,
\]

the coefficient divided by \(L^2\) is maximized at \(L=10,G=10^4\), and the exact rational audit gives

\[
\eta^2
+\frac{2\eta}{L}
+\frac{2}{L^2}
+
\frac{2\eta(1+\eta L)}{3GL}
<
\frac{73}{10}.
\]

Thus

\[
\boxed{
\widetilde F
<
\frac{73}{10}L^2Au^2.
}
\tag{DEF-UPF}
\]

## 7.4 General deficiency root lower bound

For every root survivor,

\[
D_{g,k}\mid\Lambda
\]

and \(\Lambda>0\), so

\[
\Lambda\ge D_{g,k}.
\]

By (D-UNIF),

\[
\Lambda\ge\frac{G^2}{2L}.
\]

Using again

\[
a_1>\frac{AG}{10},
\]

we obtain

\[
\boxed{
\widetilde F
=a_1\Lambda
>
\frac{AG^3}{20L}.
}
\tag{DEF-LOWF}
\]

Combine (DEF-LOWF) and (DEF-UPF):

\[
\frac{AG^3}{20L}
<
\frac{73}{10}L^2Au^2.
\]

Cancel \(A\):

\[
\boxed{
G^3<146L^3u^2.
}
\tag{DEF-MASTER}
\]

This is the main new deficiency theorem.

## 7.5 Deficiency Wedge Theorem

### Case \(q>1\)

Since \(q\mid G+1\), \(q\) is odd, \(5\nmid q\), and \(3\nmid q\).  Therefore

\[
q>1\Longrightarrow q\ge7.
\]

Thus

\[
u=\frac{G+1}{q}
\le\frac{G+1}{7}.
\]

From (DEF-MASTER),

\[
G
<
\frac{146}{49}
L^3
\left(1+\frac1G\right)^2.
\]

For \(G\ge10^4\),

\[
\frac{146}{49}
\left(\frac{10001}{10000}\right)^2
<3.
\]

Hence

\[
\boxed{
G<3L^3.
}
\]

Since

\[
G=10^g,\qquad
L^3=10^{3\ell},
\]

an integer exponent must satisfy

\[
\boxed{
g\le3\ell.
}
\tag{DW+}
\]

### Case \(q=1\)

Here

\[
u=G+1.
\]

Then (DEF-MASTER) gives

\[
G
<
146L^3
\left(1+\frac1G\right)^2.
\]

For \(G\ge10^4\),

\[
146
\left(\frac{10001}{10000}\right)^2
<147.
\]

Hence

\[
\boxed{
G<147L^3.
}
\]

Because \(147<10^3\),

\[
\boxed{
g\le3\ell+2.
}
\tag{DW1}
\]

Therefore:

\[
\boxed{
\textbf{For every fixed deficiency }\ell,
\textbf{ only finitely many }g\textbf{ remain.}
}
\tag{FIXED-ELL}
\]

This is substantially stronger than merely defining \(\ell\).

## 7.6 Full \(\ell=1\) closure

For \(q>1\), (DW+) gives

\[
g\le3.
\]

But the live frontier has \(g\ge4\).  Hence

\[
\boxed{
\ell=1,\ q>1
\Longrightarrow\varnothing.
}
\]

For \(q=1\), (DW1) gives

\[
g\le5.
\]

The frozen \(g=2,3\) closures remove those depths.  Only

\[
g=4,5
\]

remain.

The exact certificate scans the complete \(\eta\)-majorized \(N\)-strip and exact RCE digit cells at

\[
q=1,\quad k=2g-1,\quad g=4,5.
\]

It finds:

\[
\boxed{
g=4:\ 6\text{ linear cells},\quad0\text{ root-core cells},
}
\]

\[
\boxed{
g=5:\ 6\text{ linear cells},\quad0\text{ root-core cells}.
}
\]

Therefore

\[
\boxed{
J=2,\quad S_R<0,\quad\ell=1
\Longrightarrow\varnothing.
}
\tag{ELL1-CLOSED}
\]

This completes **Success C3**.

## 7.7 Immediate consequence for \(\ell=2\)

Although this round does not exhaust \(\ell=2\), the wedge already gives:

\[
q>1,\ \ell=2
\Longrightarrow
g\le6,
\]

and

\[
q=1,\ \ell=2
\Longrightarrow
g\le8.
\]

Thus the next deficiency layer is already a finite-depth problem.

---

# Part VIII — Computational Census

The executable certificate is

```text
A1_J2_RCRF4_search.py
```

and its output is

```text
A1_J2_RCRF4_certificate.txt
```

All comparisons use exact integers or `Fraction`; no floating-point decision is used.

## 8.1 Low-depth linear-cell census

The diagnostic range is

\[
4\le g\le10.
\]

Only the already-proved outer bound

\[
q^3<216G
\]

is used to restrict the positive and \(k=2g\) q>1 diagnostic census.

Totals:

```text
positive_outer = 16
positive_pbz_solvable_outer = 4
positive_interval_residue = 0
positive_linear = 0
positive_root_core = 0

negative_outer = 16
negative_nbz_solvable_N_cells = 18
negative_interval_residue = 2
negative_linear = 0
negative_root_core = 0
```

This low-depth zero count is **not** used as a uniform theorem.  The two high-depth witnesses explicitly show why that would be invalid.

## 8.2 High-depth linear witnesses

Positive:

```text
g=2385, q=19, N=-1, t=45
root_core_pass=False
v2(Ftilde)=1
v5(Ftilde)=1
required core at k=2g-1:
v2 >= 4768
v5 >= 4769
```

Negative boundary:

```text
g=39, q=7, N=3, t=17
root_core_pass=False
v2(Ftilde)=2
v5(Ftilde)=0
required core at k=2g:
v2 >= 76
v5 >= 78
```

These are genuine **linear** survivors but not root survivors.

## 8.3 \(\ell=1,\ q=1\) finite residual

The only finite residual left by the uniform size theorem is

\[
g=4,5.
\]

The exact counts are

```text
g=4: linear=6, root_core=0
g=5: linear=6, root_core=0
```

Thus

```text
ELL1_Q1_LINEAR_TOTAL=12
ELL1_Q1_ROOT_CORE_TOTAL=0
```

## 8.4 Survivor ledger

Because linear survivors exist, the required file

```text
A1_J2_RCRF4_survivors.tsv
```

is generated.

It contains 14 rows:

- 1 positive high-depth linear witness;
- 1 negative \(k=2g\) high-depth linear witness;
- 12 finite \(\ell=1,q=1\) linear cells.

Every recorded row has

```text
root_core_pass=False
```

and therefore

```text
ROOT_SURVIVOR_COUNT=0
```

in the audited slices.

---

# Part IX — Closure Audit

## 9.1 \(g=2,3\)

Frozen complete closures remain active:

\[
g=2,3\Longrightarrow\varnothing.
\]

No new argument reopens them.

## 9.2 \(u=1\)

Frozen full J2 closure remains active.

## 9.3 \(q=1\)

- Positive: frozen uniformly closed.
- Negative \(k=2g\): frozen uniformly closed.
- Negative \(\ell=1\): this round reduces to \(g\le5\), then closes \(g=4,5\) by exact certificate.
- Negative \(\ell\ge2\): remains part of the new deficiency frontier, subject to
  \[
  g\le3\ell+2.
  \]

So no global \(q=1\) claim is silently assumed.

## 9.4 \(q>1\)

Because \(q\mid10^g+1\),

\[
q\text{ odd},\quad5\nmid q,\quad3\nmid q,
\]

hence

\[
q\ge7.
\]

This is the only outer-divisor lower bound used in the new size contradictions.

## 9.5 Positive sign

Completely closed this round.

The linear survivor at \(g=2385\) proves that the closure genuinely occurs at the root-factor layer, not at PBZ.

## 9.6 Negative sign

- \(k=2g+1\): frozen closed.
- \(k=2g\): newly closed.
- \(k=2g-1\), i.e. \(\ell=1\): newly closed.
- remaining:
  \[
  k\le2g-2.
  \]

## 9.7 \(N=-1\)

Handled by the exact positive PBZ cell and the positive root-factor size contradiction.

## 9.8 \(N=1,3,5\)

Handled in the negative \(k=2g\) NBZ classification.

The exact gcd condition is

\[
d=\gcd(A,G^2-1)\mid N.
\]

## 9.9 \(\gcd(A,q(q+4))>1\)

Fully classified by

\[
d=\gcd(A,G^2-1).
\]

Positive PBZ requires \(d=1\).

Negative NBZ requires \(d\mid N\).

## 9.10 \(5\mid A\)

Impossible by the frozen J2.5 ten-unit argument.

Thus the \(5\mid A\) chamber is not omitted; it is empty.

## 9.11 \(5\nmid A\)

This is the only admissible chamber and is used throughout.

## 9.12 Both root signs

The factor system

\[
a_1\Lambda=\widetilde F,
\qquad
AH^2a_1+\Lambda=2uKD_2
\]

is exactly equivalent to square discriminant plus integral-root divisibility after choosing either near-square factor as the root factor.

The size contradiction depends only on the positive complementary factor \(\Lambda\), so neither root sign is omitted.

## 9.13 Primitive gcd

No primitive-gcd theorem is weakened.

The new closure uses only consequences already frozen in the RCE/root-factor chart plus the actual second digit window.

## 9.14 Common-\(U\) gate

The new lower bound is explicitly radial:

\[
a_1=UC_1,\qquad
a_2=UC_2,\qquad
M=Um.
\]

Thus common-\(U\) is not discarded; it is precisely what allows J2.5 and the actual digit window to combine into

\[
a_1>\frac{AG}{10}.
\]

## 9.15 Endpoint equality

The actual digit convention

\[
\frac{G^2K}{10}\le a_2<G^2K
\]

is used with the correct inclusive lower endpoint.

Because \(M=Um>0\), the resulting \(a_1>AG/10\) is strict even when \(a_2\) is exactly on its lower digit endpoint.

No extra endpoint-equality chamber remains.

---

# Part X — New Frontier

The old positive Bézout-cell frontier is retired because the positive branch is closed.

The old negative \(k=2g\) boundary is retired because it is closed.

The \(\ell=1\) layer is also retired.

Therefore the unique remaining J2 resonance frontier is

\[
\boxed{
J=2,\quad
S_R<0,\quad
\ell:=2g-k\ge2.
}
\tag{FRONTIER}
\]

Together with the frozen reductions,

\[
\boxed{
g\ge4,\qquad u>1.
}
\]

The permanent new deficiency wedge is

\[
\boxed{
q>1
\Longrightarrow
g\le3\ell,
}
\]

\[
\boxed{
q=1
\Longrightarrow
g\le3\ell+2.
}
\]

Equivalently,

\[
\boxed{
q>1
\Longrightarrow
\ell\ge\left\lceil\frac g3\right\rceil,
}
\]

\[
\boxed{
q=1
\Longrightarrow
\ell\ge\left\lceil\frac{g-2}{3}\right\rceil.
}
\]

For \(q>1\), this improves the surviving exponent ceiling from roughly

\[
k\le2g-1
\]

to

\[
\boxed{
k
=
2g-\ell
\le
2g-\left\lceil\frac g3\right\rceil
\approx\frac{5g}{3}.
}
\]

The most valuable next target is therefore not generic negative \(k\), but

\[
\boxed{\ell=2.}
\]

It is already finite-depth:

\[
q>1:\quad4\le g\le6,
\]

\[
q=1:\quad4\le g\le8.
\]

After \(\ell=2\), the same deficiency theorem guarantees finite depth for every fixed \(\ell\), so the natural continuation is a layer-by-layer exact closure combined with attempts to improve the slope \(g\le3\ell\).

---

# Final Status Ledger

## NEW PROVED

1. Exact gcd lemma:
   \[
   \gcd(A,q(q+4))=\gcd(A,G^2-1).
   \]

2. Positive effective integer cell:
   \[
   q+2\le t\le2q+8.
   \]

3. Positive linear-only extinction is false:
   \[
   (g,q,N,t)=(2385,19,-1,45)
   \]
   is an exact linear survivor.

4. Negative \(k=2g\) linear-only extinction is false:
   \[
   (g,q,N,t)=(39,7,3,17)
   \]
   is an exact linear survivor.

5. The two proposed \(Z\)-divisibilities are equivalent, not independent.

6. Universal digit-root lower splice:
   \[
   a_1>\frac{AG}{10}.
   \]

7. Positive root-factor extinction:
   \[
   S_R>0\Longrightarrow\varnothing.
   \]

8. Boundary scale cancellation:
   \[
   AC_1+\mu=8ud_2
   \qquad(k=2g).
   \]

9. Negative boundary root-factor extinction:
   \[
   S_R<0,\ k=2g\Longrightarrow\varnothing.
   \]

10. Exact deficiency decimal-core formulas:
    \[
    \ell=1:\ D=G^2/20,
    \]
    \[
    \ell=2:\ D=G^2/100,
    \]
    \[
    \ell\ge3:\ D=2G^2/10^\ell.
    \]

11. Deficiency master inequality:
    \[
    G^3<146\cdot10^{3\ell}u^2.
    \]

12. Deficiency Wedge Theorem:
    \[
    q>1\Rightarrow g\le3\ell,
    \]
    \[
    q=1\Rightarrow g\le3\ell+2.
    \]

13. Full first-deficiency closure:
    \[
    \ell=1\Longrightarrow\varnothing.
    \]

## DISPROVED

1. PBZ is never solvable.
2. The unique positive Bézout residue never enters the actual digit window.
3. Negative \(k=2g\) is linearly empty.
4. The two \(Z\)-divisibilities provide independent constraints.

## COMPUTATIONAL EVIDENCE / CERTIFICATE

- low-depth linear census \(4\le g\le10\);
- exact high-depth positive linear witness;
- exact \(g=39\) negative-boundary linear witness;
- complete \(q=1,\ell=1,g=4,5\) finite residual;
- 14 linear survivor rows;
- 0 root-core survivors in all recorded targeted slices.

## OPEN

\[
\boxed{
J=2,\quad
S_R<0,\quad
g\ge4,\quad
u>1,\quad
\ell\ge2,
}
\]

subject to the Deficiency Wedge Theorem.

No full J2 Resonance Closure Certificate is issued.

---

# File Audit

The following files were actually generated and checked:

```text
A1_J2_RCRF4_Report.md
A1_J2_RCRF4_search.py
A1_J2_RCRF4_certificate.txt
A1_J2_RCRF4_survivors.tsv
```

The certificate records:

```text
VERDICT_POSITIVE_J2=CLOSED
VERDICT_NEGATIVE_K_2G=CLOSED
VERDICT_ELL1=CLOSED
VERDICT_FULL_J2=OPEN
CERTIFICATE_STATUS=PASS
```

and

```text
LINEAR_SURVIVOR_ROWS=14
ROOT_SURVIVOR_COUNT=0
```

FINAL_REPORT_FILE: A1_J2_RCRF4_Report.md

COMPUTATION_FILE: A1_J2_RCRF4_search.py

CERTIFICATE_FILE: A1_J2_RCRF4_certificate.txt

SURVIVOR_FILE: A1_J2_RCRF4_survivors.tsv
