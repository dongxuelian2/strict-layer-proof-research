# A1 J2 DCDC5 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Campaign:** \(\ell=2\) Exact Closure × Deficiency-Core Decimal Congruence × Wedge-Slope Compression  
**Inherited source:** `A1_J2_RCRF4_Report.md`  
**Computation:** `A1_J2_DCDC5_search.py`  
**Certificate:** `A1_J2_DCDC5_certificate.txt`

---

# Part I — Executive Status

\[
\boxed{\ell=2\ \textbf{CLOSED}}
\]

\[
\boxed{q=1\ \textbf{OPEN globally, but compressed to }g\le2\ell+2}
\]

\[
\boxed{
q>1,\ \ell\ge3
\Longrightarrow
g\le3\ell-1
}
\]

and the outer-divisor-sensitive refinement is

\[
\boxed{
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2 10^{3\ell}.
}
\tag{OW}
\]

The finite DCDC census also gives, as extra closures,

\[
\boxed{\ell=3\Longrightarrow\varnothing,\qquad \ell=4\Longrightarrow\varnothing.}
\]

Hence the full \(J=2\) chamber is still open, but its unique live deficiency frontier has moved to

\[
\boxed{
J=2,\quad S_R<0,\quad g\ge4,\quad u>1,\quad \ell\ge5,
}
\]

with

\[
\boxed{
q=1\Rightarrow g\le2\ell+2,
\qquad
q>1\Rightarrow g\le3\ell-1.
}
\tag{NEW-WEDGE}
\]

This round therefore achieves the required \(\ell=2\) exact closure, a genuine \((N,t)\)-only DCDC congruence, and a structural wedge improvement.  The main new uniform gain is the slope-2 theorem in the previously dangerous \(q=1\) chamber.

---

# Part II — Frozen Deficiency Ledger

Let

\[
G=10^g,\qquad H=G/2,\qquad K=10^k,\qquad \ell=2g-k,\qquad L=10^\ell,
\]

\[
uq=G+1,\qquad A=2u+1.
\]

The frozen radial-cyclotomic system is

\[
2Aa_3=q(G-1)Z-N,
\tag{RCE1}
\]

\[
(G-1)t=2(q+4)a_3+qN,
\tag{RCE2}
\]

\[
q(q+4)Z=At-2N.
\tag{RCE3}
\]

Thus

\[
a_3=\frac{(G-1)t-qN}{2(q+4)},\qquad
Z=\frac{At-2N}{q(q+4)},
\]

\[
\mathcal X=\frac{Z+uN}{2},\qquad
D_2=ua_3+G\mathcal X.
\]

The negative signed-index strip is

\[
-\left(\frac{2\eta}{K}+\frac{2A}{G}\right)<N<\frac{2\eta G^2}{K}=2\eta L,
\qquad \eta<2.598.
\tag{NSTRIP}
\]

This is crucial: after passing to deficiency coordinates, the upper size of \(N\) depends on \(\ell\), not on \(g\).

The root-factor system is

\[
a_1\Lambda=\widetilde F,
\qquad
AH^2a_1+\Lambda=2uKD_2,
\]

\[
\widetilde F=A\mathcal X^2+ZD_2,
\qquad
a_1>\frac{AG}{10}.
\tag{DRL}
\]

The exact decimal core is

\[
D_{g,k}=2^{\min(k+1,2g-2)}5^{\min(k,2g)}\mid\Lambda,\widetilde F.
\]

In deficiency coordinates:

\[
\ell=2:\quad D_{g,k}=K=\frac{G^2}{100},
\]

\[
\ell\ge3:\quad D_{g,k}=2K=\frac{2G^2}{L}.
\]

The inherited radial upper bound is

\[
\widetilde F<\frac{73}{10}L^2Au^2.
\tag{UP}
\]

---

# Part III — \(\ell=2\) Exact Closure

For \(\ell=2\), \(D=K=G^2/100\).  Combining DRL with the exact core gives

\[
\widetilde F>\frac{AG}{10}\frac{G^2}{100},
\]

hence with (UP)

\[
G^3<73L^3u^2,\qquad L=100.
\]

For \(q>1\), \(q\ge7\), so this leaves \(g\le6\).  For \(q=1\), the stronger q=1 tail theorem proved in Part VII also gives \(g\le2\ell+2=6\).  Therefore the **complete** \(\ell=2\) residual is only

\[
g\in\{4,5,6\}.
\]

| g | q values | outer | N cells | congruence | reconstructed | digit-legal | DCDC | square disc | integral roots |
|---:|:--|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 137, 1 | 2 | 522 | 476 | 212 | 69 | 0 | 0 | 0 |
| 5 | 9091, 11, 1 | 3 | 782 | 515 | 231 | 76 | 0 | 0 | 0 |
| 6 | 9901, 101, 1 | 3 | 782 | 477 | 213 | 69 | 0 | 0 | 0 |

Totals:

```text
{'outer': 8, 'N_cells': 2086, 'congruence': 1468, 'reconstructed': 656, 'digit_legal': 214, 'dcdc': 0, 'disc_nonnegative': 0, 'disc_square': 0, 'integral_a1_roots': 0, 'full_radial_survivors': 0}
```

There are **214** fully digit-legal linear RCE cells and **zero** decimal-core survivors.  Thus no discriminant/root/common-\(U\) reconstruction is even reached:

\[
\boxed{\ell=2\Longrightarrow\varnothing.}
\]

This is the requested **Deficiency-2 Closure Certificate**.

---

# Part IV — Explicit Root-Factor Expansion in \((N,t)\)

Set

\[
M:=q(q+4),\qquad R:=At-2N,
\]

\[
Y:=R+uNM,
\]

\[
E:=uq\bigl((G-1)t-qN\bigr)+GY.
\]

Then the frozen reconstruction becomes exactly

\[
Z=\frac RM,
\qquad
\mathcal X=\frac{Y}{2M},
\qquad
D_2=\frac{E}{2M}.
\]

Therefore

\[
\boxed{
4M^2\widetilde F
=AY^2+2RE.
}
\tag{NT-F}
\]

This is the desired complete elimination of \(Z,\mathcal X,D_2\): the root-product term is now an explicit function of

\[
(g,\ell,u,q,N,t)
\]

and, after \(u=(G+1)/q\), of the outer divisor and the two terminal integers \((N,t)\).

Consequently DCDC becomes the genuine \((N,t)\)-only congruence

\[
\ell=2:\qquad
\boxed{
AY^2+2RE\equiv0\pmod{4KM^2},
}
\tag{NT-DCDC2}
\]

and for \(\ell\ge3\),

\[
\boxed{
AY^2+2RE\equiv0\pmod{8KM^2}.
}
\tag{NT-DCDC}
\]

This is stronger than merely recording \(2K\mid\widetilde F\): no \(Z,\mathcal X,D_2\) variables remain.

---

# Part V — Deficiency-Core Decimal Congruence

For \(\ell\ge3\), write

\[
\Lambda=2K\lambda_0.
\]

The second root-factor equation gives an exact scale-free normalization:

\[
AH^2a_1+2K\lambda_0=2uKD_2.
\]

Since

\[
\frac{H^2}{2K}=\frac L8,
\]

we get

\[
\boxed{
\lambda_0=uD_2-\frac{AL}{8}a_1.
}
\tag{NCF}
\]

Now \(u,D_2,A\) are ten-units.  Because \(5^\ell\mid L/8\),

\[
\lambda_0\equiv uD_2\pmod5,
\]

hence

\[
\boxed{v_5(\lambda_0)=0\qquad(\ell\ge3).}
\tag{NCF5}
\]

For \(\ell\ge4\), \(2\mid L/8\), so

\[
\lambda_0\equiv uD_2\equiv1\pmod2
\]

in parity, and therefore

\[
\boxed{\gcd(\lambda_0,10)=1\qquad(\ell\ge4).}
\tag{NCF10}
\]

This is an exact allocation theorem for the complementary root factor.  In particular, any extra \(2\)- or \(5\)-adic depth of

\[
\widetilde F=2K\,a_1\lambda_0
\]

beyond the forced core comes entirely from \(a_1\) once \(\ell\ge4\).  No generic local-phase machinery is needed.

The computational census also shows that DCDC can be achieved by genuine cancellation on the RCE side: two \(\ell=4,q=1,g=4\) states satisfy the whole decimal core even though both summands are individually \(2\)- and \(5\)-adic units.  They die only at the square-discriminant gate; see Part IX.

---

# Part VI — Decimal-Core Quotient

For \(\ell\ge3\), define

\[
\Omega:=\frac{\widetilde F}{2K}=a_1\lambda_0.
\]

The normalized complementary factor itself satisfies

\[
1\le\lambda_0
<\frac{73}{2}\frac{L^3u^2}{G^3}.
\tag{LAM-UP}
\]

Indeed, divide (UP) by \(2K a_1\) and use DRL.

This is the cleanest form of the new wedge mechanism.  Since \(uq=G+1\), for \(q>1\)

\[
1
<\frac{73}{2q^2}\frac{L^3}{G}\left(1+\frac1G\right)^2,
\]

so

\[
\boxed{
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3.
}
\tag{OW-again}
\]

The point is not just that \(\Omega\) is integral.  The complementary quotient \(\lambda_0\) is a positive integer with tightly controlled local support, and its positivity alone yields an outer-divisor-sensitive wedge.

---

# Part VII — The \(q=1\) Chamber: Decimal Tail and Slope 2

Now set

\[
q=1,\qquad u=G+1,\qquad A=2G+3.
\]

The RCE formulas become

\[
Z=\frac{(2G+3)t-2N}{5},
\]

\[
a_3=\frac{(G-1)t-N}{10},
\]

\[
\mathcal X=\frac{5GN+2Gt+3N+3t}{10},
\]

\[
D_2=\frac{5G^2N+3G^2t+2GN+3Gt-N-t}{10}.
\]

A direct exact expansion gives

\[
\begin{aligned}
100\widetilde F={}&
G^3(50N^2+60Nt+20t^2)\\
&+G^2(115N^2+170Nt+66t^2)\\
&+G(100N^2+158Nt+68t^2)\\
&+(N+t)(31N+21t).
\end{aligned}
\tag{Q1-POLY}
\]

For \(\ell=2\), put \(c=1\); for \(\ell\ge3\), put \(c=2\).  Then the decimal core is \(cK\mid\widetilde F\).  Since

\[
\frac{G^2}{100cK}=\frac{L}{100c}\in\mathbf Z
\qquad(\ell\ge2),
\]

all \(G^2,G^3\) terms disappear modulo \(100cK\).  Hence

\[
G(100N^2+158Nt+68t^2)+(N+t)(31N+21t)
\equiv0\pmod{100cK}.
\tag{Q1-TAIL}
\]

RCE3 gives

\[
At\equiv2N\pmod5.
\]

Since \(A\equiv3\pmod5\),

\[
N+t\equiv0\pmod5.
\]

Write

\[
N=-t+5s.
\]

Then

\[
100N^2+158Nt+68t^2
=10(250s^2-21st+t^2),
\]

\[
(N+t)(31N+21t)=25s(31s-2t).
\]

Thus (Q1-TAIL) is equivalent to

\[
\boxed{
20cK\mid
2G(250s^2-21st+t^2)+5s(31s-2t).
}
\tag{Q1-S}
\]

Assume first \(\ell<g\).  Then \(L\le G/10\).  NSTRIP gives

\[
N\ge-3,
\qquad
N<2\eta L<5.196L,
\]

and the exact digit window for \(a_3\) forces

\[
1\le t\le10.
\]

Therefore \(s=(N+t)/5\ge0\).  The case \(s=0\) would make (Q1-S) require a divisor at least \(100\) of the odd square \(t^2\le81\), impossible.  Hence \(s\ge1\).

Moreover

\[
s<\frac{5.196L+10}{5}<\frac{53}{50}L.
\]

Because \(G\mid20cK\), reducing (Q1-S) modulo \(G\) gives

\[
\frac G5\mid s(31s-2t).
\]

But \(s\ge1\), \(t\le10\), so

\[
0<s(31s-2t)<31s^2<35L^2.
\]

Consequently

\[
G<175L^2.
\]

As \(175<10^3\),

\[
\boxed{g\le2\ell+2.}
\tag{Q1-SLOPE2}
\]

If \(\ell\ge g\), the same conclusion is trivial.  Therefore (Q1-SLOPE2) is uniform for every \(q=1,\ell\ge2\) root/DCDC survivor.

This is the main slope compression of the round.

---

# Part VIII — Wedge-Slope Compression

The old wedge was

\[
q>1:\ g\le3\ell,
\qquad
q=1:\ g\le3\ell+2.
\]

The exact deficiency core improves it as follows.

## 8.1 \(q>1,\ell\ge3\)

Since \(D=2K\), DRL and (UP) give

\[
G^3<\frac{73}{2}L^3u^2.
\]

Using \(u=(G+1)/q\),

\[
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3.
\]

For the worst possible \(q=7\) and \(G\ge10^4\), the coefficient is already \(<1\).  Hence

\[
\boxed{q>1,\ \ell\ge3\Longrightarrow g\le3\ell-1.}
\]

More strongly,

\[
q\ge23\Longrightarrow g\le3\ell-2,
\]

\[
q\ge61\Longrightarrow g\le3\ell-3.
\]

So the dangerous q>1 outer chambers are forced toward genuinely small complementary divisors.

## 8.2 \(q=1\)

Part VII gives the strictly better slope

\[
\boxed{q=1\Longrightarrow g\le2\ell+2.}
\]

Thus the previously most dangerous maximal-\(u\) chamber is no longer slope 3 at all.

## 8.3 \(\ell=2\)

For \(q>1\), the exact \(D=K\) size inequality gives \(g\le6\); for \(q=1\), slope 2 also gives \(g\le6\).  Hence Part III is a genuinely complete finite closure.

---

# Part IX — Computational Census

All searches use the exact NSTRIP, the exact RCE congruence

\[
At\equiv2N\pmod{q(q+4)},
\]

the exact half-open digit window for \(a_3\), ten-unit/positivity conditions, DCDC, and then the exact quadratic discriminant/integral-root test.

## 9.1 \(\ell=2\)

| g | q values | outer | N cells | congruence | reconstructed | digit-legal | DCDC | square disc | integral roots |
|---:|:--|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 137, 1 | 2 | 522 | 476 | 212 | 69 | 0 | 0 | 0 |
| 5 | 9091, 11, 1 | 3 | 782 | 515 | 231 | 76 | 0 | 0 | 0 |
| 6 | 9901, 101, 1 | 3 | 782 | 477 | 213 | 69 | 0 | 0 | 0 |

```text
{'outer': 8, 'N_cells': 2086, 'congruence': 1468, 'reconstructed': 656, 'digit_legal': 214, 'dcdc': 0, 'disc_nonnegative': 0, 'disc_square': 0, 'integral_a1_roots': 0, 'full_radial_survivors': 0}
```

Result: zero DCDC survivor, hence

\[
\boxed{\ell=2\text{ CLOSED}.}
\]

## 9.2 \(\ell=3\)

| g | q values | outer | N cells | congruence | reconstructed | digit-legal | DCDC | square disc | integral roots |
|---:|:--|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 137, 1 | 2 | 5198 | 4717 | 2099 | 683 | 0 | 0 | 0 |
| 5 | 9091, 11, 1 | 3 | 7796 | 5108 | 2287 | 743 | 0 | 0 | 0 |
| 6 | 9901, 101, 1 | 3 | 7796 | 4727 | 2103 | 685 | 0 | 0 | 0 |
| 7 | 909091, 11, 1 | 3 | 7796 | 5107 | 2287 | 742 | 0 | 0 | 0 |
| 8 | 17, 1 | 2 | 5198 | 4958 | 2220 | 721 | 0 | 0 | 0 |

```text
{'outer': 13, 'N_cells': 33784, 'congruence': 24617, 'reconstructed': 10996, 'digit_legal': 3574, 'dcdc': 0, 'disc_nonnegative': 0, 'disc_square': 0, 'integral_a1_roots': 0, 'full_radial_survivors': 0}
```

There are **3574** digit-legal linear cells and zero DCDC survivors.  Thus

\[
\boxed{\ell=3\text{ CLOSED}.}
\]

## 9.3 \(\ell=4\)

| g | q values | outer | N cells | congruence | reconstructed | digit-legal | DCDC | square disc | integral roots |
|---:|:--|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 137, 1 | 2 | 51962 | 47126 | 23162 | 7384 | 2 | 0 | 0 |
| 5 | 9091, 11, 1 | 3 | 77942 | 51017 | 22907 | 7429 | 0 | 0 | 0 |
| 6 | 9901, 101, 1 | 3 | 77942 | 47231 | 21016 | 6828 | 0 | 0 | 0 |
| 7 | 909091, 11, 1 | 3 | 77942 | 51020 | 22834 | 7414 | 0 | 0 | 0 |
| 8 | 17, 1 | 2 | 51962 | 49533 | 22168 | 7197 | 0 | 0 | 0 |
| 9 | 90909091, 76923077, 52631579, 10989011, 7518797, 6993007, 4784689, 999001, 683527, 578369, 52579, 19019, 2717, 1729, 1001, 247, 209, 91, 77, 19, 11, 7, 1 | 23 | 597542 | 61895 | 28270 | 9156 | 0 | 0 | 0 |
| 10 | 99009901, 2824061, 357641, 27961, 3541, 101, 1 | 7 | 181862 | 47246 | 21025 | 6828 | 0 | 0 | 0 |
| 11 | 9090909091, 4347826087, 826446281, 395256917, 35932447, 24431957, 11390819, 2221087, 1062259, 1035529, 201917, 96569, 94139, 8779, 121, 11 | 16 | 415680 | 4643 | 2243 | 729 | 0 | 0 | 0 |

```text
{'outer': 59, 'N_cells': 1532834, 'congruence': 359711, 'reconstructed': 163625, 'digit_legal': 52965, 'dcdc': 2, 'disc_nonnegative': 2, 'disc_square': 0, 'integral_a1_roots': 0, 'full_radial_survivors': 0}
```

Exactly two DCDC pseudo-survivors occur, both in

\[
(g,q)=(4,1).
\]

They are:

```text
ell=4 g=4 q=1 N=33217 t=13 core_quotient=27603532140340804 v2=(0,0->7) v5=(0,0->4) disc_square=False
ell=4 g=4 q=1 N=38381 t=9 core_quotient=36846366709935889 v2=(0,0->5) v5=(0,0->4) disc_square=False
```

For both states,

\[
v_5(A\mathcal X^2)=v_5(ZD_2)=0,
\qquad
v_5(\widetilde F)=4,
\]

so the required \(5\)-adic depth is produced by **genuine cancellation**, not by individual divisibility.  The 2-adic cancellation is also genuine.  Nevertheless neither discriminant is a square, so no integral \(a_1\) root exists and the radial gate is never reached.

Therefore

\[
\boxed{\ell=4\text{ CLOSED}.}
\]

This \(\ell=4\) computation is useful primarily as a DCDC diagnostic: it falsifies any claim that the decimal core forces individual high divisibility of the two summands, while confirming that deep cancellation can occur but still be killed at the exact root gate.

---

# Part X — New Frontier

Full \(J=2\) is still open.  The new unique frontier is

\[
\boxed{
J=2,\quad S_R<0,\quad \ell\ge5,
}
\]

with frozen

\[
g\ge4,\qquad u>1,
\]

and the new uniform restrictions

\[
\boxed{
q=1\Rightarrow g\le2\ell+2,
}
\]

\[
\boxed{
q>1\Rightarrow
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3
\Rightarrow g\le3\ell-1.
}
\]

The preferred terminal obstruction is no longer merely

\[
2K\mid\widetilde F.
\]

It is the combined package

\[
\boxed{
\textbf{NT-DCDC}
:
AY^2+2RE\equiv0\pmod{8Kq^2(q+4)^2},
}
\]

plus

\[
\boxed{
\lambda_0=uD_2-\frac{AL}{8}a_1,
\qquad
v_5(\lambda_0)=0,
\qquad
\ell\ge4\Rightarrow\gcd(\lambda_0,10)=1,
}
\]

and, in the \(q=1\) chamber, the much lower-dimensional decimal-tail congruence (Q1-S).

The next highest-value target is therefore **not** \(\ell=5\) enumeration.  It is to generalize the q=1 tail-factor mechanism to the remaining small fixed \(q>1\) chambers, or to use NT-DCDC plus the outer-sensitive bound to force a similar slope-2 product divisibility.

---

# Status Ledger

## NEW PROVED

1. \(\ell=2\) exact closure.
2. Explicit \((N,t)\)-only root-product identity (NT-F).
3. Exact \((N,t)\)-only DCDC congruence modulo \(4KM^2\) / \(8KM^2\).
4. Normalized complementary factor
   \[
   \lambda_0=uD_2-(AL/8)a_1.
   \]
5. \(v_5(\lambda_0)=0\) for \(\ell\ge3\).
6. \(\gcd(\lambda_0,10)=1\) for \(\ell\ge4\).
7. Outer-sensitive wedge (OW).
8. \(q>1,\ell\ge3\Rightarrow g\le3\ell-1\).
9. \(q\ge23\Rightarrow g\le3\ell-2\); \(q\ge61\Rightarrow g\le3\ell-3\).
10. q=1 exact decimal-tail polynomial and congruence.
11. Uniform q=1 slope-2 theorem
    \[
    g\le2\ell+2.
    \]
12. Extra exact closures \(\ell=3,4\).

## FALSIFIED / DOWNGRADED

- DCDC does **not** force the two summands \(A\mathcal X^2\) and \(ZD_2\) to be individually highly divisible: the two \(\ell=4\) pseudo-survivors achieve the required core by genuine cancellation.
- No claim is made that \(\Omega\) itself is a ten-unit; only \(\lambda_0\) is forced to be a ten-unit for \(\ell\ge4\).

## OPEN

\[
\boxed{\textbf{Full J2 OPEN}.}
\]

The remaining uniform problem begins at \(\ell\ge5\).

---

# File Audit

The following files are generated and checked by the executable certificate:

```text
A1_J2_DCDC5_Report.md
A1_J2_DCDC5_search.py
A1_J2_DCDC5_certificate.txt
A1_J2_DCDC5_survivors.tsv
A1_J2_L2_certificate.txt
```

The report/certificate agree on:

```text
VERDICT_ELL2=CLOSED
VERDICT_ELL3=CLOSED
VERDICT_ELL4=CLOSED
VERDICT_Q1=OPEN_BUT_SLOPE2
VERDICT_FULL_J2=OPEN
```

FINAL_REPORT_FILE: A1_J2_DCDC5_Report.md

COMPUTATION_FILE: A1_J2_DCDC5_search.py

CERTIFICATE_FILE: A1_J2_DCDC5_certificate.txt

SURVIVOR_FILE: A1_J2_DCDC5_survivors.tsv

L2_CERTIFICATE_FILE: A1_J2_L2_certificate.txt
