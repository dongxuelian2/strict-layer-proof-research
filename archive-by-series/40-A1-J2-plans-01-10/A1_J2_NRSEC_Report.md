# A1 J2 NRSEC Report

**Campaign:** J2 Double-Euclidean Compression × Narrow-\(r\) Strip × Endpoint Collision  
**Scope:** Strict Layer — \(A_1\)-only, Exact Resonance, \(J=2,\ g\ge2\)  
**Main target:** \(S_R<0\), with \(S_R>0\) touched only after substantial negative-branch compression  
**Computation:** exact integer arithmetic only; no floating-point decision is used in the certificate

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 }(g\ge2)\textbf{ remains OPEN globally}.}
\]

\[
\boxed{S_R<0\textbf{ remains OPEN globally}.}
\]

Hence

\[
\boxed{\textbf{Exact Resonance remains OPEN}.}
\]

This round nevertheless reaches a strong **Success C** and closes several infinite / complete finite subchambers.

The main new theorem is a third Euclidean compression.  After the frozen J2 Double-Euclidean normal form, the negative branch can be reduced from

\[
(u,q,m,r,w,C_1,C_2,T)
\]

to a two-core arithmetic chart

\[
\boxed{(C_3,z)}
\]

for fixed \((g,u,k)\), with every other terminal quantity recovered exactly.

More strongly, the same chart admits a sign-unified form.  Put

\[
G=10^g,\qquad H=G/2,\qquad q=(G+1)/u,
\]

\[
A=2u+1,\qquad B=2G+q,\qquad K=10^k,
\]

and write

\[
c:=C_3.
\]

Then every admissible J2 state has a positive ten-unit \(z\) such that

\[
\boxed{
\begin{aligned}
h&=qHz-Ac,\\
m&=Ah-Gz,\\
r&=Hh-uc,\\
X&=GHz-uAc,\\
d_2&=uc+GX,
\end{aligned}}
\tag{CZ-NF}
\]

where

\[
\boxed{
X>0\iff S_R<0,
\qquad
X<0\iff S_R>0,
\qquad
w=|X|.
}
\]

The remaining sphere / word compatibility is the exact quadratic

\[
\boxed{
AH^2C_1^2-2uKd_2C_1+A X^2+zd_2=0.
}
\tag{CZ-Q}
\]

Therefore, defining

\[
\boxed{
\Delta_0
:=u^2K^2d_2^2-AH^2(A X^2+zd_2),
}
\]

any survivor must satisfy simultaneously

\[
\boxed{\Delta_0=R_0^2}
\]

and the integral-root divisibility

\[
\boxed{
AH^2\mid uKd_2\pm R_0.
}
\tag{ROOT}
\]

Thus the last J2 obstruction is no longer a wide Euclidean system and no longer an \((m,r)\)-strip.  It is a **finite \((c,z)\) square-plus-root-divisibility problem for every fixed \(g\)**.

A second new theorem radially bounds \(z\) in the negative branch:

\[
\boxed{
Uz<
\frac{2\eta u}{K}
+
\frac{2uA}{G},
\qquad
\eta:=2.532\sqrt{\frac{101}{96}}<2.598.
}
\tag{UZ-}
\]

Consequently

\[
\boxed{
J=2,\ g\ge2,\ S_R<0,\ u=1
\Longrightarrow\varnothing.
}
\tag{U1-}
\]

The inherited positive RRGS bound already kills \(u=1\) for \(S_R>0\), so in fact

\[
\boxed{
J=2,\ g\ge2,\ u=1
\Longrightarrow\varnothing.
}
\tag{U1}
\]

Finally, the exact computation certificate proves the complete low-depth closures

\[
\boxed{
J=2,\ g=2\Longrightarrow\varnothing,
}
\]

\[
\boxed{
J=2,\ g=3\Longrightarrow\varnothing.
}
\]

Both signs are covered in these two statements.

So the true remaining J2 frontier is now

\[
\boxed{
J=2,\quad g\ge4,\quad u>1,
}
\]

inside the sign-unified \((c,z)\) discriminant/root chart above.

---

# Part II — Frozen J2 Ledger

Only the identities actually used in this round are listed.

Let

\[
G=10^g,\qquad H=G/2,\qquad K=10^k,
\]

with

\[
g\ge2,\qquad k\ge1.
\]

For \(J=2\), the previous round established

\[
s=d_*=\beta_0=1,
\qquad
\beta=H,
\qquad
n_3=g,
\]

\[
\boxed{u\mid G+1.}
\]

Define

\[
q:=\frac{G+1}{u},
\qquad
A:=2u+1,
\qquad
B:=2G+q.
\]

Then

\[
uq=G+1,
\]

and the determinant identities are

\[
\boxed{qA-B=2,}
\tag{DET2}
\]

\[
\boxed{uB-GA=1.}
\tag{DET1}
\]

The frozen J2 normal form is

\[
C_3=2r+\varepsilon q w,
\tag{J2.1}
\]

\[
d_2=2ur+\varepsilon w,
\tag{J2.2}
\]

\[
D=HC_2+r,
\tag{J2.3}
\]

\[
Ar+\varepsilon w=mH,
\tag{J2.4}
\]

\[
GKC_1=AC_2+m,
\tag{J2.5}
\]

\[
uC_2-\varepsilon w=HT,
\tag{J2.6}
\]

\[
H^2C_1^2+w^2=T d_2.
\tag{J2.7}
\]

Here

\[
\varepsilon=
\begin{cases}
-1,&S_R<0,\\
+1,&S_R>0,
\end{cases}
\]

and

\[
\gcd(mrTw,10)=1.
\]

The primitive coordinates are

\[
P_1=GH C_1,
\qquad
P_2=uG C_2,
\qquad
P_3=uC_3,
\]

and

\[
Q_0=P_2+d_2.
\]

The actual common radial scale obeys

\[
a_i=UC_i,
\qquad
\gcd(U,V)=1,
\qquad
V=uGH.
\]

Therefore the exact numerator digit windows used below are

\[
\boxed{
\frac{G^2K}{10}\le UC_2<G^2K,
}
\tag{DIG2}
\]

\[
\boxed{
\frac G{10}\le UC_3<G.
}
\tag{DIG3}
\]

The frozen axis estimate is

\[
\boxed{
\frac{d_2}{Q_0}<2.532\,K^{-2},
}
\tag{AX}
\]

and the strong \(P_2\)-axis theorem is

\[
\boxed{
P_2>\sqrt{\frac{96}{101}}\,Q_0.
}
\tag{P2AX}
\]

For \(S_R>0\), the previous RRGS result gives

\[
\boxed{0<Uw<u.}
\tag{RRGS+}
\]

Finally, the frozen sign/face exponent bounds imply

\[
S_R<0:
\qquad
1\le k\le2g+1
\]

after taking the union of Face A and Face B, whereas

\[
S_R>0:
\qquad
2g-1\le k\le3g-1.
\]

These finite \(k\)-ranges are used only in the fixed-\(g\) certificate.

---

# Part III — E2 / E3 / E4 Verification

## 3.1 E2

From

\[
Ar+\varepsilon w=mH
\]

we have

\[
\varepsilon w=mH-Ar.
\]

Substitute into

\[
d_2=2ur+\varepsilon w:
\]

\[
\begin{aligned}
d_2
&=2ur+mH-Ar\\
&=mH+(2u-A)r\\
&=mH-r,
\end{aligned}
\]

because \(A=2u+1\). Hence

\[
\boxed{d_2=mH-r.}
\tag{E2}
\]

This is sign-independent.

## 3.2 E3

From J2.6,

\[
uC_2-\varepsilon w=HT.
\]

Using \(\varepsilon w=mH-Ar\),

\[
\begin{aligned}
uC_2-mH+Ar&=HT,\\
uC_2+Ar&=H(T+m).
\end{aligned}
\]

Thus

\[
\boxed{uC_2+Ar=H(T+m).}
\tag{E3}
\]

Again sign-independent.

## 3.3 E4

From J2.1,

\[
C_3=2r+\varepsilon q w.
\]

Substitute \(\varepsilon w=mH-Ar\):

\[
C_3=2r+qmH-qAr.
\]

Since

\[
qA=q(2u+1)=2uq+q=2(G+1)+q=2G+q+2,
\]

we obtain

\[
2-qA=-(2G+q).
\]

Hence

\[
\boxed{
C_3=qmH-(2G+q)r=qmH-Br.
}
\tag{E4}
\]

All three proposed simplifications are therefore correct and are frozen.

---

# Part IV — Negative Narrow-\(r\) Strip

Assume now

\[
S_R<0,
\qquad
\varepsilon=-1.
\]

Then

\[
Ar-w=mH,
\]

so

\[
w=Ar-mH>0.
\]

Therefore

\[
\boxed{
r>\frac{mH}{A}
=\frac{mG}{2A}.
}
\tag{L}
\]

Also E4 and \(C_3>0\) give

\[
qmH-Br>0,
\]

hence

\[
\boxed{
r<\frac{qmH}{B}
=\frac{qmG}{2B}.
}
\tag{R}
\]

Thus

\[
\boxed{
\frac{mG}{2A}<r<\frac{qmG}{2B}.
}
\tag{STRIP}
\]

Using \(qA-B=2\), the width is

\[
\begin{aligned}
\Delta_r
&=\frac{mG}{2}
\left(\frac qB-\frac1A\right)\\
&=\frac{mG}{2}
\frac{qA-B}{AB}\\
&=\boxed{\frac{mG}{AB}}.
\end{aligned}
\tag{WIDTH}
\]

So the proposed WIDTH formula is also correct.

## 4.1 Uniform \(\Delta_r<1\) is false

The strip itself does **not** force \(m\) small.

For example take

\[
G=100,
\quad
u=1,
\quad
q=101,
\quad
A=3,
\quad
B=301,
\]

and

\[
m=53,
\quad
r=889.
\]

Then

\[
w=Ar-mH=3\cdot889-53\cdot50=17,
\]

\[
C_3=2r-qw=1778-1717=61,
\]

\[
d_2=mH-r=2650-889=1761.
\]

All \(m,r,w,C_3,d_2\) are positive and the relevant unit conditions hold; even \(C_3<G\).

But

\[
\Delta_r=\frac{53\cdot100}{3\cdot301}
=\frac{5300}{903}>5.
\]

So the conjecture

\[
\Delta_r<1
\]

is false at the strip/E1--E4 level.

Crucially, this pseudo-state dies immediately at the next Euclidean condition derived below:

\[
um-Aw=53-51=2
\]

is not divisible by

\[
H=50.
\]

This is a useful diagnosis: the correct next gate is not another real-width estimate.

## 4.2 Exact successor form in \(w\)

The negative strip is equivalently

\[
w=Ar-mH>0.
\]

Therefore

\[
\boxed{
w\equiv-mH\pmod A.
}
\]

Using E4 and eliminating \(r=(mH+w)/A\),

\[
\boxed{
AC_3=mG-Bw.
}
\tag{W-C3}
\]

Hence \(C_3>0\) is exactly

\[
\boxed{
0<w<\frac{mG}{B}.
}
\tag{W-STRIP}
\]

Let

\[
w_0:=A-(mH\bmod A),
\qquad
1\le w_0\le A.
\]

Then all integer candidates in the strip are precisely

\[
w=w_0+jA,
\qquad
j\ge0,
\qquad
w<\frac{mG}{B}.
\]

This is the exact successor statement.  In particular it remains valid when the strip has width greater than one.

There is also an explicit cyclotomic residue form.  Since

\[
2G\equiv-(q+2)\pmod A,
\]

we have

\[
4H=2G\equiv-(q+2)\pmod A.
\]

Multiplying \(w\equiv-mH\pmod A\) by \(4\) gives

\[
\boxed{
4w\equiv m(q+2)\pmod A.
}
\tag{W-RES}
\]

This is the determinant-2 endpoint residue, but by itself it still does not close the chamber.

---

# Part V — Main Closure Attempt: Third Euclidean Collapse

## 5.1 First auxiliary lemma: \(A\) is a ten-unit

In J2.5,

\[
GKC_1=AC_2+m.
\]

The left side is divisible by \(10\).  Moreover \(m\) is a ten-unit, and J2.6 shows that \(C_2\) is also a ten-unit.  Since \(A\) is odd, if \(5\mid A\), then modulo \(5\)

\[
0\equiv AC_2+m\equiv m\not\equiv0,
\]

contradiction.

Thus

\[
\boxed{\gcd(A,10)=1.}
\tag{A-UNIT}
\]

This removes, for example, the \(g=3\) divisors \(u=7,77\), for which \(A\) is divisible by \(5\).

## 5.2 Negative branch: define the hidden Euclidean remainder \(z\)

Continue with \(S_R<0\).  Put

\[
\boxed{h:=m-2w.}
\]

From (W-C3),

\[
AC_3=mG-Bw
=G(m-2w)-qw
=Gh-qw.
\]

Because \(C_3>0\) and \(w>0\), this forces

\[
\boxed{h>0.}
\]

Now multiply J2.5 by \(u\).  Since the negative J2.6 is

\[
uC_2+w=HT,
\]

we have

\[
uC_2=HT-w.
\]

Therefore

\[
\begin{aligned}
uGKC_1
&=AuC_2+um\\
&=AHT-Aw+um.
\end{aligned}
\]

Using \(G=2H\),

\[
2uHKC_1=AHT+(um-Aw).
\]

Hence

\[
\boxed{H\mid um-Aw.}
\tag{H-DIV}
\]

Define

\[
\boxed{
z:=\frac{um-Aw}{H}.
}
\tag{ZDEF}
\]

Since \(A=2u+1\) and \(h=m-2w\),

\[
um-Aw=u(m-2w)-w=uh-w.
\]

Thus

\[
Hz=uh-w.
\]

The identity \(AC_3=Gh-qw\) now becomes

\[
AC_3=qHz-h.
\]

Since \(C_3>0\), this forces \(z>0\).

Moreover

\[
2uKC_1=AT+z.
\tag{Z-EUCLID}
\]

The left side is divisible by \(10\), while \(A,T\) are ten-units, so

\[
\boxed{\gcd(z,10)=1.}
\]

This is the third Euclidean remainder.

## 5.3 Exact negative \(c\)-\(z\) normal form

Write

\[
c:=C_3.
\]

From

\[
Ac=qHz-h
\]

we get

\[
\boxed{h=qHz-Ac.}
\tag{CZ1}
\]

Then

\[
\begin{aligned}
w&=uh-Hz\\
&=u(qHz-Ac)-Hz\\
&=(uq-1)Hz-uAc\\
&=GHz-uAc.
\end{aligned}
\]

So

\[
\boxed{w=GHz-uAc>0.}
\tag{CZ2-}
\]

Further,

\[
\boxed{m=Ah-Gz,}
\tag{CZ3}
\]

because

\[
Ah-Gz-h=2uh-2Hz=2w.
\]

And

\[
\boxed{r=Hh-uc.}
\tag{CZ4}
\]

Finally, since \(S_R=-Gw=P_3-d_2\) and \(P_3=uc\),

\[
\boxed{d_2=uc+Gw.}
\tag{CZ5-}
\]

Thus \(m,r,w\) have disappeared as independent variables.

Also, because \(G,H\equiv0\pmod{10}\) and \(A,u,c,z\) are ten-units, the formulas imply automatically that

\[
h,m,r,w,d_2
\]

are ten-units.  No separate residue scan for them is needed.

## 5.4 Sign-unified extension

After the negative compression was obtained, the same calculation was checked for \(S_R>0\).

For the positive sign define

\[
h:=m+2w.
\]

Then the identical variables \(h,z,c\) satisfy

\[
h=qHz-Ac,
\]

\[
m=Ah-Gz,
\]

\[
r=Hh-uc,
\]

but now

\[
w=uAc-GHz.
\]

Hence it is natural to define the signed gap

\[
\boxed{X:=GHz-uAc.}
\]

Then the two signs are unified as

\[
\boxed{
X>0\iff S_R<0,
\qquad
X<0\iff S_R>0,
\qquad
w=|X|.
}
\]

And in both cases

\[
\boxed{d_2=uc+GX.}
\tag{CZ5}
\]

The condition \(d_2>0\) is retained explicitly; for \(X<0\) it is nontrivial.

This proves the sign-unified normal form stated in Part I.

## 5.5 Fourth Euclidean coordinate and \(\ell\)-classification

From

\[
2uKC_1=AT+z
\]

and \(A=2u+1\),

\[
A(KC_1-T)=KC_1+z>0.
\]

Define

\[
\boxed{p:=KC_1-T>0.}
\]

Then

\[
\boxed{KC_1=Ap-z,}
\]

\[
\boxed{T=2up-z.}
\]

Because \(T\equiv-p\pmod{10}\), \(p\) is a ten-unit.

Now define

\[
\boxed{\ell:=2p-qz.}
\]

Then direct elimination gives

\[
\boxed{C_2=Ac+H\ell,}
\tag{ELL1}
\]

\[
\boxed{2KC_1=Bz+A\ell,}
\tag{ELL2}
\]

\[
\boxed{T=Gz+u\ell.}
\tag{ELL3}
\]

Since \(T\equiv u\ell\pmod{10}\), \(\ell\) is a nonzero ten-unit.

There is a useful exact sign classification.

### Lemma — negative \(\ell\) is extremal

If

\[
\ell<0,
\]

then from (ELL1)

\[
C_2<Ac.
\]

Use the actual digit windows:

\[
\frac{G^2K}{10}\le UC_2<A(Uc)<AG.
\]

Therefore

\[
GK<10A.
\]

Since \(K\ge10\),

\[
G<A=2u+1,
\]

so

\[
u>\frac{G-1}{2}.
\]

But \(u\mid G+1\), hence

\[
q=\frac{G+1}{u}<\frac{2(G+1)}{G-1}<3
\]

for \(G\ge100\).  Since \(q\) is odd,

\[
q=1,
\qquad
u=G+1.
\]

Then \(GK<10(2G+3)\), and because \(K\) is a power of ten with \(K\ge10\), necessarily

\[
K=10,
\qquad
k=1.
\]

Thus

\[
\boxed{
\ell<0
\Longrightarrow
(q,u,k)=(1,G+1,1).
}
\tag{ELL-EX}
\]

Every other J2 cell has

\[
\boxed{\ell>0.}
\]

In particular the positive branch, where \(k\ge2g-1\ge3\), automatically has \(\ell>0\).

## 5.6 Sphere elimination: exact discriminant and root divisibility

The third Euclidean equation is

\[
2uKC_1=AT+z,
\]

so

\[
T=\frac{2uKC_1-z}{A}.
\]

Substitute into

\[
H^2C_1^2+X^2=T d_2.
\]

Multiplying by \(A\) yields

\[
\boxed{
AH^2C_1^2-2uKd_2C_1+A X^2+zd_2=0.
}
\tag{CZ-Q}
\]

Its reduced discriminant is

\[
\boxed{
\Delta_0
=u^2K^2d_2^2-AH^2(A X^2+zd_2).
}
\tag{DISC}
\]

Any integer root therefore requires

\[
\boxed{
\Delta_0=R_0^2
}
\]

and

\[
\boxed{
C_1=
\frac{uKd_2\pm R_0}{AH^2}
\in\mathbf Z_{>0}.
}
\tag{ROOT}
\]

This is exactly the same lesson previously seen in the J5 near-survivor: square discriminant alone is insufficient; root divisibility is part of the theorem.

There is an equivalent factor/divisor form.  Let

\[
N_*:=A X^2+zd_2.
\]

For any integral root,

\[
\boxed{C_1\mid N_*}
\]

and

\[
\boxed{
AH^2C_1+\frac{N_*}{C_1}=2uKd_2.
}
\tag{DIVROOT}
\]

This is the lowest-dimensional exact arithmetic gate found in this round.

---

# Part VI — Endpoint / Congruence / Radial Splice

## 6.1 QH congruence

The proposed congruence is correct.

In the negative branch, from

\[
w=Ar-mH
\]

we have modulo \(H\)

\[
w\equiv Ar\pmod H.
\]

The sphere gives

\[
H^2C_1^2+w^2=T(mH-r).
\]

Modulo \(H\),

\[
A^2r^2\equiv-Tr\pmod H.
\]

Because \(r\) is a ten-unit and \(H\) has only primes \(2,5\),

\[
\gcd(r,H)=1.
\]

Hence

\[
\boxed{
T\equiv-A^2r\pmod H.
}
\tag{QH}
\]

It is a valid exact congruence, although after the \((c,z)\) compression it is not the final closure mechanism.

## 6.2 Negative radial \(Uz\) theorem

Let

\[
x_0:=\sqrt{\frac{96}{101}}.
\]

From the strong axis theorem

\[
P_2>x_0Q_0,
\]

and

\[
P_2=uG C_2,
\]

we get

\[
Q_0<\frac{uG C_2}{x_0}.
\]

The actual second digit window gives

\[
UC_2<G^2K,
\]

hence

\[
Q_0<\sqrt{\frac{101}{96}}\,
\frac{uG^3K}{U}.
\]

Combine this with

\[
\frac{d_2}{Q_0}<2.532K^{-2}.
\]

Define

\[
\eta:=2.532\sqrt{\frac{101}{96}}.
\]

Then

\[
\boxed{
Ud_2<\eta\frac{uG^3}{K}.
}
\tag{UD2}
\]

In the negative branch,

\[
d_2=uc+Gw>Gw,
\]

so

\[
\boxed{
Uw<\eta\frac{uG^2}{K}.
}
\tag{UW-}
\]

But the \((c,z)\) normal form gives

\[
w=GHz-uAc.
\]

Multiplying by \(U\),

\[
GH(Uz)=Uw+uA(Uc).
\]

Since \(Uc<G\),

\[
GH(Uz)
<
\eta\frac{uG^2}{K}+uAG.
\]

As \(GH=G^2/2\),

\[
\boxed{
Uz<
\frac{2\eta u}{K}
+
\frac{2uA}{G}.
}
\tag{UZ-}
\]

This is an actual-radial inequality: \(U\) appears explicitly.

For the deterministic certificate we use the rational majorant

\[
\boxed{\eta<2.598=\frac{1299}{500}.}
\]

Indeed

\[
2.598^2-2.532^2\frac{101}{96}
=\frac{1869}{400000}>0.
\]

### Corollary — \(u=1\) negative extinction

If \(u=1\), then \(A=3\), \(K\ge10\), \(G\ge100\).  Thus

\[
Uz
<
\frac{2(2.598)}{10}
+
\frac6{100}
=0.5796<1.
\]

But \(U,z\in\mathbf Z_{>0}\). Contradiction.

Therefore

\[
\boxed{
S_R<0,\ u=1\Longrightarrow\varnothing.
}
\]

## 6.3 Positive radial \(z\) bound

For \(S_R>0\), the unified signed gap has

\[
X=-w,
\]

so

\[
w=uAc-GHz.
\]

The inherited RRGS theorem gives

\[
0<Uw<u.
\]

Therefore

\[
GH(Uz)=uA(Uc)-Uw<uAG,
\]

and hence

\[
\boxed{
Uz<\frac{2uA}{G}.
}
\tag{UZ+}
\]

In particular

\[
\boxed{
z<\frac{2uA}{G}.}
\]

This is enough to make the positive branch finite for every fixed \(g\).

## 6.4 Fixed-\(g\) finiteness theorem

For a fixed \(g\ge2\):

1. \(G=10^g\) is fixed.
2. \(u\mid G+1\), hence only finitely many \(u\).
3. \(A=2u+1\) must be a ten-unit.
4. Actual digit legality gives
   \[
   1\le c=C_3<G,
   \qquad
   \gcd(c,10)=1.
   \]
5. For \(S_R<0\), the union of the two faces gives
   \[
   1\le k\le2g+1,
   \]
   and (UZ-) gives an explicit finite upper bound for \(z\).
6. For \(S_R>0\),
   \[
   2g-1\le k\le3g-1,
   \]
   and (UZ+) gives an explicit finite upper bound for \(z\).
7. Each cell \((u,k,c,z)\) is decided by the exact quadratic (CZ-Q), integer-square discriminant, root divisibility, primitive reconstruction, and the common-\(U\) digit/coprimality gate.

Hence:

\[
\boxed{
\textbf{For every fixed }g\ge2,
\textbf{ the entire J2 chamber is an exact finite problem.}
}
\tag{FIXED-g-FINITE}
\]

This is stronger than the previous positive-only finite-width exponent wedge.  The only remaining infinitude in J2 is now the outer parameter \(g\).

---

# Part VII — Computational Certificate

The computation is **not** an enumeration of original concatenation states.

It enumerates only the exact \((u,k,c,z)\) terminal cells certified by Part VI, using integer arithmetic throughout.

Files:

- `A1_J2_NRSEC_search.py`
- `A1_J2_NRSEC_certificate.txt`

The script uses the rigorous rational majorant

\[
\eta<\frac{1299}{500}
\]

and computes the strict integer \(z\)-ceiling with `Fraction`, so no floating-point comparison is used to decide coverage.

For every cell it applies, in order:

1. \(u\mid G+1\);
2. \(\gcd(A,10)=1\);
3. exact sign/face \(k\)-range;
4. exact radial \(z\)-bound;
5. \(1\le c<G\), \(c,z\) ten-units;
6. sign condition on \(X=GHz-uAc\);
7. positivity of \(h,m,r,d_2\);
8. exact discriminant \(\Delta_0\);
9. perfect-square test with integer `isqrt`;
10. root divisibility by \(AH^2\);
11. exact reconstruction of \(C_2,T,P_i,Q_0,D\);
12. primitive sphere and primitive gcd;
13. actual common-\(U\) digit interval;
14. \(\gcd(U,V)=1\);
15. for the positive branch, the inherited \(Uw<u\) gate.

## 7.1 Complete \(g=2\) audit

Here

\[
G=100,
\qquad
G+1=101.
\]

Allowed \((u,q,A,B)\) after the \(A\)-unit gate are

\[
(1,101,3,301),
\qquad
(101,1,203,201).
\]

### Negative \(S_R<0\)

The complete face-union range is

\[
1\le k\le5.
\]

The exact certificate examined

\[
\boxed{17,320}
\]

\((c,z)\)-cells allowed by the proven bounds.

All 17,320 reached a nonnegative reduced discriminant, but

\[
\boxed{0}
\]

had square \(\Delta_0\).

Thus

\[
\boxed{g=2,\ S_R<0\Longrightarrow\varnothing.}
\]

### Positive \(S_R>0\)

The complete range is

\[
3\le k\le5.
\]

The certificate examined 99 sign-compatible \((c,z)\)-cells.  None survived the exact linear positivity package \((m,r,d_2)>0\).

Thus

\[
\boxed{g=2,\ S_R>0\Longrightarrow\varnothing.}
\]

Combining signs:

\[
\boxed{J=2,\ g=2\Longrightarrow\varnothing.}
\tag{G2-CLOSED}
\]

## 7.2 Complete \(g=3\) audit

Here

\[
G=1000,
\qquad
G+1=1001.
\]

After removing the divisors for which \(5\mid A\), the allowed tuples are

\[
\begin{aligned}
&(1,1001,3,3001),\\
&(11,91,23,2091),\\
&(13,77,27,2077),\\
&(91,11,183,2011),\\
&(143,7,287,2007),\\
&(1001,1,2003,2001).
\end{aligned}
\]

The divisors \(u=7,77\) are rejected exactly because \(A=2u+1\) is divisible by \(5\).

### Negative \(S_R<0\)

The full face-union range is

\[
1\le k\le7.
\]

The certificate examined

\[
\boxed{2,428,113}
\]

exact \((c,z)\)-cells.

Again

\[
\boxed{0}
\]

had square \(\Delta_0\).

Hence

\[
\boxed{g=3,\ S_R<0\Longrightarrow\varnothing.}
\]

### Positive \(S_R>0\)

The full range is

\[
5\le k\le8.
\]

The certificate examined 1,400 sign-compatible \((c,z)\)-cells, and none survived the linear positivity package.

Hence

\[
\boxed{g=3,\ S_R>0\Longrightarrow\varnothing.}
\]

Combining signs:

\[
\boxed{J=2,\ g=3\Longrightarrow\varnothing.}
\tag{G3-CLOSED}
\]

## 7.3 Certificate verdict

The recorded global count is

\[
\boxed{\texttt{GLOBAL\_RADIAL\_SURVIVOR\_COUNT}=0.}
\]

and the file ends with

```text
CERTIFICATE_STATUS=PASS
```

The computational conclusions are used only for \(g=2,3\).  No finite scan is extrapolated to \(g\ge4\).

---

# Part VIII — Closure Audit

## 8.1 \(u=1\)

New negative theorem (UZ-) gives

\[
S_R<0,\ u=1\Longrightarrow\varnothing
\]

for every \(g\ge2\).

The inherited positive RRGS bound gives

\[
0<Uw<u=1,
\]

also impossible.

Therefore

\[
\boxed{u=1\text{ is completely closed in J2}.}
\]

## 8.2 \(q=1\), equivalently \(u=G+1\)

This extremal cyclotomic divisor is **not** globally closed.

It is additionally singled out by the new \(\ell\)-theorem:

\[
\ell<0
\Longrightarrow
q=1,
\quad
u=G+1,
\quad
k=1.
\]

Thus any non-extremal cell has \(\ell>0\).

## 8.3 \(S_R<0\)

Globally still OPEN, but now:

- \(u=1\) is closed for all \(g\ge2\);
- \(g=2\) is closed;
- \(g=3\) is closed;
- every fixed \(g\) is finite;
- \(m,r,w\) are no longer independent search variables.

The surviving negative region is therefore

\[
\boxed{g\ge4,\quad u>1.}
\]

## 8.4 \(S_R>0\)

The previous exponent ceiling remains frozen.  This round adds the positive \((c,z)\) normal form and the finite bound

\[
z<2uA/G.
\]

Thus positive J2 is also finite for each fixed \(g\).

The complete \(g=2,3\) positive branches are closed by the certificate.

For \(g\ge4\), positive J2 remains OPEN.

## 8.5 Small \(m\) / large \(m\)

This distinction is no longer the right frontier.

The strip-only conjecture \(\Delta_r<1\) is false because \(m\) can be large at that level.

After the third Euclidean collapse,

\[
m=Ah-Gz
\]

is derived from \((c,z)\).  Hence there is no independent large-\(m\) escape parameter left.

## 8.6 \(g=2\)

Both signs CLOSED by complete exact certificate.

## 8.7 \(g=3\)

Both signs CLOSED by complete exact certificate.

## 8.8 Endpoint equality

The \((c,z)\) derivation does not assume that the common-\(U\) radial point lies strictly away from a lower digit endpoint.  The actual digit intervals are used with their correct half-open convention.

The positive inequality \(Uw<u\) is inherited as a strict theorem and is not replaced by a heuristic margin.

Thus no endpoint-equality case is silently discarded.

## 8.9 Face A / Face B

The analytic compression does not depend on the active face.

For the finite certificate, the union of the exact face ranges is used:

\[
S_R<0:\quad1\le k\le2g+1,
\]

\[
S_R>0:\quad2g-1\le k\le3g-1.
\]

Therefore both faces are covered.

## 8.10 \(\gcd(U,V)=1\)

The new negative UZ bound uses only the fact that \(U\ge1\), so its analytic extinction of \(u=1\) is stronger than a coprimality-only argument.

The finite certificate nevertheless performs the full

\[
\gcd(U,V)=1
\]

check for reconstructed radial candidates.

No state is declared dead merely because a coprime \(U\) was not guessed.

## 8.11 Sign convention

Throughout this report

\[
\varepsilon=-1\iff S_R<0,
\qquad
\varepsilon=+1\iff S_R>0.
\]

The signed \(X\)-coordinate is

\[
X=GHz-uAc=-\varepsilon w.
\]

Thus

\[
X>0\iff S_R<0,
\qquad
X<0\iff S_R>0.
\]

No sign swap occurs in the computation.

## 8.12 Full J2 status

Despite the low-depth and \(u=1\) closures, no theorem in this round eliminates every \(g\ge4\) divisor cell.

Therefore no J2 closure certificate is issued.

\[
\boxed{\textbf{J2 }(g\ge2)\textbf{ remains OPEN}.}
\]

Consequently Exact Resonance also remains OPEN.

---

# Part IX — New Frontier

The old frontier

\[
(u,q,m,r)
\]

should be retired.

The new exact J2 frontier is the following.

## J2-CZDR — \(C_3\)-\(z\) Discriminant-Root Exclusion

Fix

\[
g\ge4,
\qquad
G=10^g.
\]

Choose

\[
u\mid G+1,
\qquad
u>1,
\qquad
q=(G+1)/u,
\]

with

\[
A=2u+1,
\qquad
\gcd(A,10)=1.
\]

Choose \(k\) in the appropriate exact sign/face range and ten-units

\[
1\le c<G,
\qquad
z>0,
\]

subject to the sign-appropriate proven \(z\)-bound.

Define

\[
\boxed{
\begin{aligned}
h&=qHz-Ac,\\
m&=Ah-Gz,\\
r&=Hh-uc,\\
X&=GHz-uAc,\\
d_2&=uc+GX.
\end{aligned}}
\]

Require

\[
h,m,r,d_2>0,
\qquad
X\ne0,
\]

and let the sign be determined by \(X\).

Then prove that it is impossible to satisfy

\[
\boxed{
\Delta_0
=u^2K^2d_2^2-AH^2(A X^2+zd_2)
=R_0^2
}
\]

with

\[
\boxed{
AH^2\mid uKd_2\pm R_0.
}
\]

If this square-plus-root-divisibility gate survives, reconstruct \(C_1,C_2,T\) and only then apply the actual common-\(U\) digit/coprimality endpoint.

This is a genuine dimensional reduction:

- \(m\) is derived;
- \(r\) is derived;
- \(w\) is derived;
- \(d_2\) is derived;
- \(T\) is derived after the root;
- \(C_2\) is derived after the root;
- for each fixed \(g\), all ranges are finite.

The remaining infinite problem is therefore no longer “does the narrow strip contain an integer?”  It is:

\[
\boxed{
\textbf{Can the }(c,z)\textbf{ near-square quadratic admit an integral root for arbitrarily large }g?
}
\]

That is the unique lowest-dimensional J2 obstruction produced by this round.

---

# Final Status Ledger

## NEW PROVED

1. E2:
   \[
   d_2=mH-r.
   \]
2. E3:
   \[
   uC_2+Ar=H(T+m).
   \]
3. E4:
   \[
   C_3=qmH-Br.
   \]
4. Negative strip and exact width:
   \[
   \frac{mG}{2A}<r<\frac{qmG}{2B},
   \qquad
   \Delta_r=\frac{mG}{AB}.
   \]
5. Exact \(w\)-successor residue:
   \[
   w\equiv-mH\pmod A,
   \qquad
   0<w<mG/B,
   \]
   and
   \[
   4w\equiv m(q+2)\pmod A.
   \]
6. \(A\) is a ten-unit.
7. Third Euclidean divisor:
   \[
   H\mid um-Aw
   \]
   in the negative branch.
8. Positive ten-unit third remainder \(z\).
9. Sign-unified \((c,z)\) normal form (CZ-NF).
10. Fourth Euclidean \(\ell\)-form:
    \[
    C_2=Ac+H\ell,
    \quad
    2KC_1=Bz+A\ell,
    \quad
    T=Gz+u\ell.
    \]
11. Extremal negative-\(\ell\) theorem:
    \[
    \ell<0\Rightarrow(q,u,k)=(1,G+1,1).
    \]
12. Exact \((c,z)\) sphere quadratic and discriminant/root divisibility.
13. QH congruence:
    \[
    T\equiv-A^2r\pmod H.
    \]
14. Negative actual-radial UZ bound.
15. Complete negative \(u=1\) extinction.
16. Positive finite \(z\)-bound.
17. Entire J2 is finite for every fixed \(g\ge2\).

## DISPROVED / DOWNGRADED

1. Uniform strip theorem \(\Delta_r<1\): **false at the strip level**.
2. “Narrow strip alone should close negative J2”: **false as a proof strategy**; the missing exact gate is the third Euclidean remainder / discriminant-root system.

## COMPUTATIONALLY CLOSED, WITH EXACT COVERAGE

\[
J=2,\ g=2\Longrightarrow\varnothing,
\]

\[
J=2,\ g=3\Longrightarrow\varnothing.
\]

## OPEN

\[
\boxed{
J=2,\quad g\ge4,\quad u>1.
}
\]

Both signs remain globally open there, but only through J2-CZDR.

---

FINAL_REPORT_FILE: A1_J2_NRSEC_Report.md
COMPUTATION_FILE: A1_J2_NRSEC_search.py
CERTIFICATE_FILE: A1_J2_NRSEC_certificate.txt
