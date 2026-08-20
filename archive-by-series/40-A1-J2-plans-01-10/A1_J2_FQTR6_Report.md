# A1 J2 FQTR6 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Campaign:** Fixed-\(q\) Tail Reduction × Small-Divisor Slope Closure × Variable-\(q\) Staircase  
**Inherited source:** `A1_J2_DCDC5_Report.md`  
**Symbolic certificate:** `A1_J2_FQTR6_symbolic.py`  
**Exact computation:** `A1_J2_FQTR6_search.py`  
**Certificate:** `A1_J2_FQTR6_certificate.txt`

---

# Part I — Executive Status

\[
\boxed{\textbf{Full J2 OPEN}.}
\]

The live chamber remains

\[
\boxed{
J=2,\quad S_R<0,\quad g\ge4,\quad u>1,\quad \ell\ge5.
}
\]

However this round produces a genuine new dimensional collapse.

## 1. New \(q=1\) upgrade

The previous bound

\[
q=1\Longrightarrow g\le2\ell+2
\]

is strengthened to

\[
\boxed{q=1\Longrightarrow g\le\ell+3.}
\tag{Q1-SLOPE1}
\]

Thus the old \(q=1\) slope-2 theorem was not optimal: the exact \((2,5)\)-allocation in the first tail factor forces almost the whole decimal depth into its complementary linear factor.

## 2. New fixed-\(q\) valuation tail

For \(q>1\), put

\[
b:=v_5(q+4),
\]

\[
C(q):=q^4+10q^3+12q^2+8q,
\]

\[
B(q):=(q+2)(q^2-4q-4).
\]

In the nontrivial tail chamber \(\ell<g\), if \(b<g\), every DCDC survivor satisfies

\[
\boxed{
\frac{G}{2\,5^b}\mid C(q)N-B(q)t.
}
\tag{VT}
\]

Consequently

\[
\boxed{
G<30\,5^b q^4\,10^\ell.
}
\tag{FQ-SLOPE1}
\]

For every fixed \(q\), the exceptional range \(g\le b\) is already finite; hence every fixed-\(q\) chamber has asymptotic **slope 1**, strictly stronger than the requested fixed-\(q\) slope 2.

## 3. Small-\(q\) chambers

After exact order and \(A\)-unit classification, the actual set below \(23\) is

\[
\boxed{q\in\{7,11,17,19\}.}
\]

The exact exponent classes are

\[
\boxed{q=7:\ g\equiv3\pmod6,}
\]

\[
\boxed{q=11:\ g\equiv1\pmod2,}
\]

\[
\boxed{q=17:\ g\equiv8\pmod{16},}
\]

\[
\boxed{q=19:\ g\equiv9\pmod{18}.}
\]

The fixed-\(q\) slope-1 theorem gives

\[
\boxed{q=7\Longrightarrow g\le\ell+4,}
\]

\[
\boxed{q=11,17,19\Longrightarrow g\le\ell+6.}
\]

The nominal candidate \(q=13\) is impossible because \(q\equiv3\pmod5\) forces \(5\mid A\).  The values \(3,9,21\) are impossible because \(3\nmid10^g+1\).

## 4. Uniform variable-\(q\) wedge

The requested uniform slope 2 is **not** proved.  Nevertheless the old slope 3 is improved uniformly.

For \(q>1\):

\[
\boxed{
G<40\,10^{17\ell/7},
}
\tag{U17/7}
\]

and therefore

\[
\boxed{
q>1\Longrightarrow
g\le\left\lceil\frac{17\ell}{7}\right\rceil+1.
}
\tag{U-WEDGE}
\]

So the global \(q>1\) slope falls from \(3\) to

\[
\boxed{17/7\approx2.4286.}
\]

Moreover, when \(5\nmid q+4\), the stronger split gives a slope-\(7/3\) wedge.

## 5. \(\ell=5\) closure

The complete exact diagnostic census gives

\[
\boxed{\ell=5\Longrightarrow\varnothing.}
\tag{ELL5-CLOSE}
\]

There are exactly \(97\) DCDC pseudo-survivors, but every one has nonsquare discriminant; hence there are zero integral \(a_1\)-roots and zero radial survivors.

## 6. DCDC alone is not a closure engine

A genuinely large fixed-\(q\) DCDC pseudo-survivor exists at

\[
\boxed{
q=11,\quad h:=g-\ell=1,\quad g=471,\quad\ell=470,\quad t=31.
}
\]

With

\[
C(11)=29491,\qquad B(11)=949,
\]

and

\[
\mu=152510,
\]

it has

\[
N=rac{949\cdot31+152510\cdot10^{470}}{29491}.
\]

It passes the exact RCE reconstruction, digit/ten-unit/radial gates, and

\[
2K\mid\widetilde F.
\]

It dies only because its root discriminant satisfies

\[
\boxed{\Delta\equiv8\pmod{11},}
\]

and \(8\) is a quadratic nonresidue modulo \(11\).

Thus the next frontier is not “prove DCDC.”  It is the **tail-staircase + fixed local root obstruction** remaining after DCDC.

---

# Part II — Frozen Terminal Ledger

Write

\[
G=10^g,
\qquad
K=10^{2g-\ell},
\qquad
L:=10^\ell,
\]

\[
uq=G+1,
\qquad
A=2u+1,
\qquad
M=q(q+4).
\]

The actual-radial RCE system is frozen:

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

Define

\[
R:=At-2N,
\]

\[
Y:=R+uNM,
\]

\[
E:=uq((G-1)t-qN)+GY.
\]

Then

\[
Z=\frac RM,
\qquad
\mathcal X=\frac{Y}{2M},
\qquad
D_2=\frac{E}{2M},
\]

and

\[
\boxed{4M^2\widetilde F=AY^2+2RE.}
\tag{NT4}
\]

For \(\ell\ge5\),

\[
\boxed{2K\mid\widetilde F,}
\]

hence

\[
\boxed{
AY^2+2RE\equiv0\pmod{8KM^2}.
}
\tag{NT-DCDC}
\]

The exact signed-index strip remains

\[
-\left(\frac{2\eta}{K}+\frac{2A}{G}\right)<N<2\eta L,
\qquad
\eta<\frac{1299}{500}.
\tag{NSTRIP}
\]

The complementary root factor is

\[
\Lambda=2K\lambda_0,
\]

\[
\lambda_0=uD_2-\frac{AL}{8}a_1,
\]

and for the current frontier

\[
\boxed{\gcd(\lambda_0,10)=1.}
\tag{TENUNIT}
\]

The inherited outer wedge is

\[
\boxed{
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3
\qquad(q>1).
}
\tag{OUTER}
\]

---

# Part III — General Polynomial Expansion

The prompt requested the full fixed-\(q\) expansion of

\[
\mathcal P_q(G;N,t):=AY^2+2RE.
\]

Since

\[
u=\frac{G+1}{q},
\qquad
A=\frac{2G+q+2}{q},
\]

multiplication by \(q^3\) clears every denominator.  Exact symbolic expansion gives

\[
\boxed{
q^3\mathcal P_q
=C_3G^3+C_2G^2+C_1G+C_0,
}
\tag{POLY}
\]

so the exact degree in \(G\) is

\[
\boxed{3.}
\]

The coefficients are

\[
\begin{aligned}
C_3=2\big(&N^2q^4+8N^2q^3+16N^2q^2
+2Nq^3t+12Nq^2t+16Nqt\\
&+2q^2t^2+4qt^2+4t^2\big),
\end{aligned}
\]

\[
\begin{aligned}
C_2={}&N^2q^5+10N^2q^4+40N^2q^3+64N^2q^2\\
&+2Nq^4t+16Nq^3t+72Nq^2t+80Nqt\\
&+2q^3t^2+12q^2t^2+28qt^2+24t^2,
\end{aligned}
\]

\[
\begin{aligned}
C_1=2\big(&N^2q^5+9N^2q^4+20N^2q^3+20N^2q^2\\
&+Nq^4t+10Nq^3t+36Nq^2t+32Nqt\\
&+q^3t^2+5q^2t^2+16qt^2+12t^2\big).
\end{aligned}
\]

The decisive constant coefficient factors exactly:

\[
\boxed{
C_0=(qN+t)\bigl(C(q)N-B(q)t\bigr),
}
\tag{CONST-FACT}
\]

where

\[
\boxed{C(q)=q^4+10q^3+12q^2+8q,}
\]

\[
\boxed{B(q)=(q+2)(q^2-4q-4).}
\]

This is the general symbolic pattern behind the previous \(q=1\) tail factorization.

A useful exact Bézout certificate is

\[
\begin{aligned}
&(-6q^2+15q+68)(q^3+10q^2+12q+8)\\
&\qquad +(6q^2+57q+40)B(q)=224.
\end{aligned}
\tag{BEZ-CB}
\]

For odd \(q\), both factors on the left are odd, and

\[
\gcd(q,B(q))=1.
\]

Therefore

\[
\boxed{\gcd(C(q),B(q))\mid7.}
\tag{CB-GCD}
\]

All these identities are checked symbolically by `A1_J2_FQTR6_symbolic.py`.

---

# Part IV — Tail Reduction: \(\ell<g\) versus \(\ell\ge g\)

## 4.1 Large deficiency: \(\ell\ge g\)

Here

\[
k=2g-\ell\le g.
\]

The desired wedge bounds are already automatic at the exponent level:

\[
\boxed{g\le\ell.}
\]

No claim that this chamber is empty is made.  Conjecture C8 (“\(\ell<g\) uniformly”) is therefore not proved and is unnecessary for the present compression.

## 4.2 Tail chamber: \(\ell<g\)

Put

\[
h:=g-\ell\ge1.
\]

Then

\[
K=10^{g+h}=G10^h,
\]

so

\[
G\mid K.
\]

NT-DCDC therefore implies

\[
G\mid\mathcal P_q.
\]

Because \(q\) is a ten-unit,

\[
G\mid q^3\mathcal P_q.
\]

All terms containing \(G\) in (POLY) vanish modulo \(G\), leaving

\[
\boxed{
G\mid(qN+t)(C(q)N-B(q)t).
}
\tag{GEN-PRODUCT}
\]

This is the universal fixed-\(q\) tail reduction.

---

# Part V — Fixed-\(q\) Campaign

## 5.1 Exact \(t\)-size for \(q>1\)

For \(q>1\), the nontrivial divisors satisfy \(q,u\ge7\).  In the tail chamber \(\ell<g\), NSTRIP gives

\[
0<N<2\eta L<\frac{1299}{250}L.
\]

Indeed the lower strip has width less than \(1\), hence the odd integer \(N\) is positive.

From the upper third-digit inequality

\[
a_3<G
\]

and RCE2,

\[
(G-1)t<2(q+4)G+qN.
\]

Since \(L\le G/10\), \(q\ge7\), and \(G\ge10^6\),

\[
\boxed{0<t<3q+8.}
\tag{TBOUND}
\]

Thus, for fixed \(q\), \(t\) is genuinely \(O_q(1)\).

## 5.2 Nonvanishing of the complementary tail

For \(q\ge7\),

\[
B(q)>0,
\qquad
C(q)>0.
\]

Suppose

\[
C(q)N-B(q)t=0.
\]

By (CB-GCD), the reduced denominator forces

\[
t\ge\frac{C(q)}7>\frac{q^4}{7}.
\]

But for \(q\ge7\),

\[
\frac{q^4}{7}>3q+8,
\]

contradicting (TBOUND).  Therefore

\[
\boxed{C(q)N-B(q)t\ne0.}
\tag{TAIL-NZ}
\]

## 5.3 Exact valuation allocation

RCE2 gives

\[
\boxed{
qN+t=Gt-2(q+4)a_3.
}
\tag{F1}
\]

The actual digit \(a_3\) is a ten-unit.  Hence

\[
v_2(qN+t)=1.
\tag{F1-2}
\]

Let

\[
b:=v_5(q+4).
\]

If

\[
b<g,
\]

then the two terms in (F1) have distinct \(5\)-adic depths, so

\[
\boxed{v_5(qN+t)=b.}
\tag{F1-5}
\]

Combining this exact support with (GEN-PRODUCT) yields

\[
\boxed{
\frac{G}{2\,5^b}\mid C(q)N-B(q)t.
}
\tag{VT-again}
\]

This is the central theorem of the round.

## 5.4 Size theorem

For \(q\ge7\),

\[
C(q)<\frac{27}{10}q^4,
\qquad
B(q)<q^3.
\]

Using

\[
N<\frac{1299}{250}L,
\qquad
t<3q+8,
\qquad L\ge10^5,
\]

one obtains the safe bound

\[
\boxed{
|C(q)N-B(q)t|<15q^4L.
}
\tag{TAIL-SIZE}
\]

Together with nonvanishing and (VT),

\[
\boxed{
G<30\,5^bq^4L.
}
\tag{FQ1}
\]

Thus fixed \(q\) has slope 1 once \(g>b\).

If \(g\le b\), \(g\) is itself bounded by the fixed constant \(b\), so every fixed \(q\) still has only a finite exceptional prefix before the slope-1 regime.

---

# Part VI — Small-\(q\) Classification and Bounds

## 6.1 Which \(q<23\) can actually occur?

A divisor of \(10^g+1\) is coprime to \(10\).  Among the odd ten-units below \(23\), values divisible by \(3\) are impossible because

\[
10^g+1\equiv2\pmod3.
\]

This removes

\[
3,9,21.
\]

The remaining nominal list is

\[
7,11,13,17,19.
\]

But modulo \(5\),

\[
uq=G+1\equiv1,
\]

so

\[
u\equiv q^{-1}\pmod5.
\]

Therefore

\[
A=2u+1\equiv2q^{-1}+1\pmod5.
\]

Thus

\[
5\mid A
\Longleftrightarrow
q\equiv3\pmod5.
\]

Hence \(q=13\) is impossible.

Therefore

\[
\boxed{\mathcal Q_{<23}=\{7,11,17,19\}.}
\]

## 6.2 Orders of \(10\)

Exact order computation gives:

| \(q\) | \(\operatorname{ord}_q(10)\) | condition \(10^g\equiv-1\pmod q\) |
|---:|---:|:---|
| 7 | 6 | \(g\equiv3\pmod6\) |
| 11 | 2 | \(g\equiv1\pmod2\) |
| 17 | 16 | \(g\equiv8\pmod{16}\) |
| 19 | 18 | \(g\equiv9\pmod{18}\) |

## 6.3 Explicit fixed-small-\(q\) bounds

For \(q=7\), \(b=0\), and (FQ1) gives

\[
G<30\cdot7^4L=72030L<10^5L.
\]

Thus

\[
\boxed{q=7\Longrightarrow g\le\ell+4.}
\]

For \(q=11\), \(b=1\):

\[
G<30\cdot5\cdot11^4L=2196150L<10^7L,
\]

so

\[
\boxed{q=11\Longrightarrow g\le\ell+6.}
\]

For \(q=17\), \(b=0\):

\[
G<2505630L<10^7L,
\]

so

\[
\boxed{q=17\Longrightarrow g\le\ell+6.}
\]

For \(q=19\), \(b=0\):

\[
G<3909630L<10^7L,
\]

so

\[
\boxed{q=19\Longrightarrow g\le\ell+6.}
\]

The most dangerous small chamber is therefore **not** automatically \(q=7\): the \(5\)-depth in \(q+4\) makes \(q=11\) structurally less favorable, and in fact the large DCDC pseudo-survivor found this round occurs at \(q=11\).

---

# Part VII — The \(q=1\) Chamber Revisited

For \(q=1\), the constant coefficient becomes

\[
C_0=(N+t)(31N+21t).
\]

In the tail chamber \(\ell<g\),

\[
G\mid(N+t)(31N+21t).
\tag{Q1-PROD}
\]

But RCE2 gives

\[
\boxed{N+t=Gt-10a_3.}
\]

Since \(a_3\) is a ten-unit and \(g\ge6\),

\[
\boxed{v_2(N+t)=v_5(N+t)=1.}
\]

Hence

\[
\boxed{
\frac G{10}\mid31N+21t.
}
\tag{Q1-COMP}
\]

Write

\[
N+t=10r.
\]

Then

\[
31N+21t=10(31r-t),
\]

and therefore

\[
\boxed{
\frac G{100}\mid31r-t.
}
\tag{Q1-LIN}
\]

The inherited q=1 digit theorem gives

\[
1\le t\le10.
\]

NSTRIP gives \(N\ge-3\), so \(r\) cannot be negative; exact valuation excludes \(r=0\).  Thus \(r\ge1\), and

\[
31r-t\ge21>0.
\]

Also

\[
r=\frac{N+t}{10}
<\frac{1299}{2500}L+1
<\frac{13}{25}L
\qquad(L\ge10^5).
\]

Therefore

\[
\frac G{100}
\le31r-t
<\frac{403}{25}L.
\]

So

\[
G<1612L<10^4L.
\]

Hence

\[
\boxed{q=1\Longrightarrow g\le\ell+3.}
\]

This is a genuine slope-1 replacement for the previous q=1 slope-2 theorem.

---

# Part VIII — Variable-\(q\) Staircase and Uniform Wedge Compression

## 8.1 The large \(5\)-depth chamber \(b\ge g\)

If

\[
b=v_5(q+4)\ge g,
\]

then

\[
5^g\mid q+4,
\]

so

\[
q\ge5^g-4>\frac{5^g}{2}.
\]

For \(\ell<g\), \(G\ge10^6\), and OUTER gives the safe estimate

\[
G<\frac{37L^3}{q^2}
<\frac{148L^3}{25^g}.
\]

Since

\[
25^5>10^6,
\]

we have

\[
25^g>10^{6g/5}.
\]

Thus

\[
10^{11g/5}<148\,10^{3\ell}<10^{3\ell+3},
\]

so

\[
\boxed{
g<\frac{15}{11}\ell+\frac{15}{11}.
}
\tag{BIG-b}
\]

This chamber is already much stronger than slope 2.

## 8.2 The ordinary chamber \(b<g\)

From (FQ1) and

\[
5^b\le q+4\le\frac{11}{7}q,
\]

we obtain

\[
G<\frac{330}{7}q^5L.
\tag{TAIL-Q}
\]

For \(G\ge10^6\), OUTER gives

\[
G<37\frac{L^3}{q^2}.
\tag{OUTER-37}
\]

Raise (TAIL-Q) to the second power and (OUTER-37) to the fifth power.  The \(q\)-powers cancel:

\[
G^7
<\left(\frac{330}{7}\right)^2 37^5L^{17}.
\]

The exact arithmetic check

\[
\left(\frac{330}{7}\right)^2 37^5<40^7
\]

gives

\[
\boxed{G<40L^{17/7}.}
\]

Thus

\[
\boxed{
g\le\left\lceil\frac{17\ell}{7}\right\rceil+1.}
\]

Combining \(\ell\ge g\), \(b\ge g\), and \(b<g\) proves the uniform q>1 wedge (U-WEDGE).

## 8.3 The \(b=0\) refinement

If

\[
5\nmid q+4,
\]

then

\[
G<30q^4L.
\]

Combining once with two copies of OUTER-37 gives

\[
G^3<30\cdot37^2L^7<35^3L^7,
\]

hence

\[
\boxed{G<35L^{7/3}.}
\tag{U7/3}
\]

This is a slope-\(7/3\) subwedge.

## 8.4 The prompt's \(q\ge L^{1/2}\) split

If

\[
q\ge L^{1/2},
\]

then OUTER immediately yields

\[
G<37L^2,
\]

so

\[
\boxed{g\le2\ell+1.}
\]

Thus conjecture C6 is correct.  The obstruction to a global slope 2 lies in the intermediate variable-q range, not in truly large q.

---

# Part IX — Second Constraint / Final Closure Attempt

Uniform slope 2 was not reached, so the requested “second inequality after slope 2” cannot yet be used in its proposed form.  Nevertheless the valuation tail gives a more useful fixed-q secondary coordinate.

In the chamber

\[
q>1,\quad\ell<g,\quad b<g,
\]

put

\[
h:=g-\ell,
\qquad
D:=\frac{G}{2\,5^b}.
\]

Since

\[
D\mid C(q)N-B(q)t,
\]

write

\[
\boxed{
C(q)N-B(q)t=\sigma mD,
\qquad
\sigma\in\{\pm1\},
\quad m\ge1.
}
\tag{MDEF}
\]

The size theorem gives

\[
\boxed{
m<30\,5^bq^4\,10^{-h}.}
\tag{MBOUND}
\]

Hence for fixed \((q,h)\), \(m\) is finite and rapidly shrinks as \(h\) grows.

Moreover

\[
\boxed{
N=\frac{B(q)t+\sigma mG/(2\,5^b)}{C(q)}.
}
\tag{N-REC}
\]

Thus \(N\) is no longer a free terminal coordinate.

The full old chart

\[
(g,\ell,q,N,t)
\]

has therefore been reduced, in the tail chamber, to

\[
\boxed{
(q,h,\sigma,m,t;\ g\text{ in an order class}).
}
\tag{NEW-CHART}
\]

For fixed \(q\), all of \(h,m,t\) are finite.

### Fixed local DCDC modulus

Let

\[
q^3\mathcal P_q=C_3G^3+C_2G^2+C_1G+C_0.
\]

Using (MDEF),

\[
\frac{q^3\mathcal P_q}{G}
=G^2C_3+GC_2+C_1
+\sigma m\frac{qN+t}{2\,5^b}.
\tag{DQ}
\]

Because \(K=G10^h\), the remaining \((2,5)\)-part of NT-DCDC is the **fixed modulus** condition

\[
\boxed{
2^{h+3}5^{h+2b}
\mid
\frac{q^3\mathcal P_q}{G}.
}
\tag{LOCAL-DCDC}
\]

This is the preferred new terminal obstruction.  It is fixed-modulus for fixed \((q,h)\), and the only remaining infinitude is the order-residue behavior of \(G=10^g\) together with the subsequent exact root gate.

The large \(q=11\) pseudo-survivor below proves that LOCAL-DCDC can genuinely be solvable.

---

# Part X — \(\ell=5\) Diagnostic Certificate

The exact search range is the complete inherited finite wedge:

\[
q=1:\quad4\le g\le12,
\]

\[
q>1:\quad4\le g\le14,
\]

with

\[
k=2g-5.
\]

For each outer divisor, the program performs:

1. exact divisor generation for \(G+1\);
2. the \(A\)-unit gate;
3. exact NSTRIP enumeration;
4. exact digit interval for \(t\);
5. the RCE congruence;
6. the new tail divisor whenever \(\ell<g\);
7. exact RCE reconstruction;
8. digit, positivity, ten-unit and radial bounds;
9. exact DCDC \(2K\mid\widetilde F\);
10. integer discriminant and `isqrt` square test;
11. integral \(a_1\)-root divisibility.

All arithmetic is integer/Fraction arithmetic.

Totals:

```text
outer:                 85
N cells:               22,083,018
RCE congruence cells:   4,601,553
tail survivors:           981,416
reconstructed:             486,671
digit/radial legal:        155,500
DCDC survivors:                 97
disc >= 0:                     97
square discriminant:             0
integral a1 roots:                0
full radial survivors:            0
```

The \(97\) DCDC pseudo-survivors are distributed as

\[
(g,q)=(4,1):94,
\]

\[
(g,q)=(4,137):1,
\]

\[
(g,q)=(5,1):2.
\]

No DCDC survivor occurs for \(g\ge6\).

Therefore

\[
\boxed{\ell=5\Longrightarrow\varnothing.}
\]

The complete rows are saved in

`A1_J2_FQTR6_L5_survivors.tsv`.

---

# Part XI — Counterexample Ledger

## C1 — “Every fixed q has slope 2”

**TRUE but substantially weaker than the result proved.**  Fixed \(q\) has asymptotic slope 1.

## C2 — “\(\mathcal P_q\bmod K\) always reduces to \(GP_q+Q_q\)”

**TRUE in the intended \(\ell<g\) chamber in a stronger cubic-tail sense.**  Modulo \(G\), all positive \(G\)-powers die and only the exact product (CONST-FACT) remains.  The \(\ell\ge g\) chamber is handled separately.

## C3 — “The tail is quadratic in \((N,t)\)”

**TRUE.**  The constant tail is the product of two linear forms.

## C4 — “q=7 is the most dangerous fixed-small-q chamber”

**FALSE / DOWNGRADED.**  \(q=11\) carries \(v_5(q+4)=1\), has a weaker fixed constant, and supports a large exact DCDC pseudo-survivor.

## C5 — “The small set is \(\{7,11,13,17,19\}\)”

**FALSE as an admissible set.**  \(q=13\) forces \(5\mid A\).  The exact live set below 23 is

\[
\{7,11,17,19\}.
\]

## C6 — “q\ge10^{\ell/2} gives slope 2 by outer suppression”

**TRUE.**  In fact \(g\le2\ell+1\).

## C7 — “The ten-unit quotient gate kills every DCDC pseudo-survivor”

**NOT PROVED.**  A large \(q=11\) DCDC pseudo-survivor exists and reaches the discriminant gate.  Since no integral root exists, \(a_1\) and hence the final \(\lambda_0\) quotient are never instantiated for that state.

## C8 — “\(\ell<g\) uniformly”

**NOT PROVED.**  The \(\ell\ge g\) chamber is retained.  It already satisfies stronger exponent bounds, so no illicit omission is needed.

## New DCDC pseudo-survivor

Take

\[
q=11,
\quad h=1,
\quad g=471,
\quad\ell=470,
\quad t=31,
\]

\[
C=29491,
\qquad
B=949,
\qquad
b=1,
\]

and

\[
\mu=152510.
\]

Set

\[
N=\frac{949\cdot31+152510\cdot10^{470}}{29491}.
\]

The exact computation verifies:

- \(N\in\mathbf Z\);
- RCE1–RCE3 exactly;
- all actual digit and sign conditions;
- all required ten-unit conditions;
- radial bounds;
- \(2K\mid\widetilde F\);
- the valuation-tail identity
  \[
  C N-Bt=152510\frac G{10};
  \]
- discriminant nonnegativity;
- but
  \[
  \Delta\equiv8\pmod{11},
  \]
  so \(\Delta\) is not a square.

This is the minimum explicit witness retained in the new tail-counterexample ledger.

---

# Part XII — Closure Audit

## 12.1 \(q=1\)

Covered.  The previous slope-2 result is upgraded to

\[
g\le\ell+3.
\]

## 12.2 \(q>1\)

Covered by the \(b<g\) valuation tail and the \(b\ge g\) outer-suppression split.

## 12.3 Every fixed-small-\(q\) chamber

The exact admissible set below 23 is

\[
\{7,11,17,19\},
\]

with explicit order classes and slope-1 constants recorded in Part VI.

## 12.4 \(q\ge10^{\ell/2}\)

Covered directly by OUTER:

\[
g\le2\ell+1.
\]

## 12.5 \(q<10^{\ell/2}\)

Not silently identified with fixed q.  The variable-q tail/outer interpolation produces the uniform slope \(17/7\), but not slope 2.

## 12.6 \(\ell<g\)

This is the genuine tail chamber.  Full polynomial reduction, factorization, valuation allocation and the new staircase chart apply.

## 12.7 \(\ell\ge g\)

Retained explicitly.  It automatically satisfies \(g\le\ell\).  No closure claim is made.

## 12.8 Ten-unit quotient

The frozen theorem

\[
\gcd(\lambda_0,10)=1
\]

remains active.  No invalid claim that \(\Omega\) itself is a ten-unit is made.

## 12.9 DCDC cancellation

Deep cancellation is allowed.  The previous \(\ell=4\) cancellation examples are not contradicted.  The present derivation uses only the divisibility of the total \(\widetilde F\), never individual high divisibility of \(A\mathcal X^2\) and \(ZD_2\).

## 12.10 Root discriminant

Still required.  It is exactly what kills all \(97\) \(\ell=5\) DCDC pseudo-survivors and the explicit \(q=11,g=471\) pseudo-survivor.

## 12.11 Integral root divisibility

Tested after square discriminant.  In the \(\ell=5\) certificate it is vacuous because no square discriminant survives.

## 12.12 Primitive gcd

Not weakened.  Since no \(\ell=5\) integral root survives, the later primitive reconstruction gate is never reached; its survivor set is therefore vacuously empty.

## 12.13 Common-\(U\) reconstruction

Likewise retained.  No state is declared a full survivor without reconstruction.  The \(\ell=5\) root set is empty before this gate.

---

# Part XIII — New Frontier

\[
\boxed{\textbf{Full J2 remains OPEN}.}
\]

But the preferred terminal obstruction is no longer

\[
(g,\ell,q,N,t)
\]

with a raw huge DCDC modulus.

The new chart is:

\[
\boxed{
q\mid10^g+1,
\quad h=g-\ell,
\quad b=v_5(q+4),
\quad \sigma,
\quad m,
\quad t,
}
\]

subject to

\[
C(q)N-B(q)t
=\sigma m\frac{G}{2\,5^b},
\]

\[
N=\frac{B(q)t+\sigma mG/(2\,5^b)}{C(q)},
\]

\[
0<t<3q+8,
\]

\[
0<m<30\,5^bq^4\,10^{-h},
\]

and the fixed local DCDC congruence

\[
2^{h+3}5^{h+2b}
\mid
\frac{q^3\mathcal P_q}{G}.
\]

For fixed \(q\), the variables \(h,m,t\) are now finite.  The only remaining infinite motion is the arithmetic progression/order behavior of \(g\), followed by the exact root discriminant/root-divisibility gate.

This is strictly lower-dimensional than the input frontier and is the correct target for the next round.

The strongest current global wedge is

\[
\boxed{
q=1:\quad g\le\ell+3,
}
\]

and

\[
\boxed{
q>1:\quad g\le\left\lceil\frac{17\ell}{7}\right\rceil+1.
}
\]

Together with the new finite closure

\[
\boxed{\ell=5\Longrightarrow\varnothing,}
\]

the unique remaining deficiency frontier starts at

\[
\boxed{\ell\ge6.}
\]

No J2 Resonance Closure Certificate is issued this round.

---

# File Audit

The following files are generated and checked:

```text
A1_J2_FQTR6_Report.md
A1_J2_FQTR6_symbolic.py
A1_J2_FQTR6_search.py
A1_J2_FQTR6_certificate.txt
A1_J2_FQTR6_survivors.tsv
A1_J2_FQTR6_L5_survivors.tsv
A1_J2_FQTR6_L5_certificate.txt
```

Status:

```text
SYMBOLIC_STATUS=PASS
CERTIFICATE_STATUS=PASS
VERDICT_ELL5=CLOSED
VERDICT_UNIFORM_SLOPE2=NOT_PROVED
VERDICT_UNIFORM_QGT1_SLOPE=17/7
VERDICT_FULL_J2=OPEN
```

FINAL_REPORT_FILE: A1_J2_FQTR6_Report.md

SYMBOLIC_FILE: A1_J2_FQTR6_symbolic.py

COMPUTATION_FILE: A1_J2_FQTR6_search.py

CERTIFICATE_FILE: A1_J2_FQTR6_certificate.txt

SURVIVOR_FILE: A1_J2_FQTR6_survivors.tsv

L5_CERTIFICATE_FILE: A1_J2_FQTR6_L5_certificate.txt

L5_SURVIVOR_FILE: A1_J2_FQTR6_L5_survivors.tsv
