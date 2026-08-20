# 105-R29 — Architecture-Free μ-Core Derivation

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — `(A_1)`-only  
**Round:** 105-R29  
**Arithmetic:** exact integers only

## 1. Frozen definitions

Let

\[
X=10^m,\qquad Y=10^n,\qquad G=10^g,\qquad K=10^k,
\]

\[
T=Q_0-P_3>0,\qquad H=GQ_0-P_2>0,\qquad D=KP_1-Q_0>0.
\]

The R28 positive-factor TC1 normal form is

\[
\boxed{g_1^*\,[WT+AYH]=AWu_0XYG\,D.}\tag{TC1-PF}
\]

R24 gives

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3,
\]

with shape gcd conditions

\[
(A,C_2)=(W,C_3)=(A,W)=1.
\]

Define

\[
g_0=(AW,P_1),\qquad \mu=\frac{g_1^*}{g_0},\qquad a_0=\frac{AW}{g_0},
\]

\[
\ell=\frac{W+A10^{n+g}}{u_0},
\]

\[
\Xi=Q_0\ell-AW(C_3+10^nC_2)>0.
\]

Then R28 proves

\[
\boxed{\mu\Xi=a_0\,10^{m+n+g}D.}\tag{MU-CORE}
\]

Write

\[
r=m+n+g.
\]

## 2. Exact Xi recovery

Substituting the face definitions gives

\[
\boxed{
u_0\Xi=W(Q_0-P_3)+A10^n(10^gQ_0-P_2)}
\]

where the left-hand symbol is `u_0 Xi`; explicitly,

\[
\boxed{u_0\Xi=WT+AYH.}\tag{XI-OMEGA}
\]

Hence if

\[
\Omega:=WT+AYH,
\]

then

\[
\boxed{\Xi=\Omega/u_0.}
\]

Fully expanded,

\[
u_0\Xi
=WQ_0-WP_3+A10^{n+g}Q_0-A10^nP_2.
\]

Using `P2=u0 W C2`, `P3=u0 A C3`,

\[
\boxed{
u_0\Xi
=Q_0(W+A10^{n+g})-u_0AW(C_3+10^nC_2).}
\]


## 3. New architecture-free coprimality

Because

\[
g_0=(AW,P_1),
\]

we have

\[
\left(\frac{AW}{g_0},\frac{P_1}{g_0}\right)=1.
\]

Since `g1*=g0*mu` and `g1*|P1`,

\[
\mu\mid \frac{P_1}{g_0}.
\]

Therefore

\[
\boxed{(\mu,a_0)=1.}\tag{MU-A0}
\]

This is the first useful architecture-free compression of R29.

## 4. μ is supported by decimal primes plus Q0

From MU-CORE and `(mu,a0)=1`,

\[
\boxed{\mu\mid10^rD.}\tag{MU-D}
\]

Also `mu|P1`, while

\[
D=10^kP_1-Q_0\equiv -Q_0\pmod\mu.
\]

Hence

\[
\boxed{\mu\mid10^rQ_0.}\tag{MU-Q0}
\]

Thus the nondecimal part of `mu` is not free: every prime `p != 2,5` dividing `mu` must divide `Q0`.

## 5. Primitive-sphere parity

For a primitive positive sphere packet

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\]

`Q0` cannot be even: modulo 4, an even `Q0` would force all three `Pi` even. Hence

\[
\boxed{Q_0\text{ is odd}.}
\]

Modulo 4 then exactly one of `P1,P2,P3` is odd. Since `k>=1`,

\[
10^kP_1\text{ is even},
\]

so

\[
\boxed{D=10^kP_1-Q_0\text{ is odd}.}\tag{D-ODD}
\]

## 6. Architecture-free nondecimal support theorem

Let `p != 2,5` be prime and suppose `p|mu`. By MU-Q0,

\[
p\mid Q_0.
\]

Also `mu|P1`, hence `p|P1`.

If `p|C2`, then `p|P2=u0 W C2`. The sphere equation gives `p|P3`, so `p` divides all four primitive coordinates, contradiction.

If `p|C3`, then `p|P3=u0 A C3`; the sphere equation similarly gives `p|P2`, again contradicting primitivity.

Therefore

\[
\boxed{
\operatorname{supp}(\mu)\cap\operatorname{supp}(C_2C_3)
\subseteq\{2,5\}.
}\tag{DECIMAL-SUPPORT}
\]

This recovers the historical R19 reduction without architecture enumeration.

## 7. Exact 2/5-adic μ-core

For `p=2,5`, MU-CORE gives

\[
\boxed{
v_p(\mu)+v_p(\Xi)
=v_p(a_0)+r+v_p(D).
}\tag{VP}
\]

At `p=2`, D-ODD yields

\[
\boxed{
v_2(\mu)+v_2(\Xi)=v_2(a_0)+r.
}\tag{V2}
\]

Because `(mu,a0)=1`, if `mu` is even then `a0` is odd, and therefore

\[
\boxed{v_2(\mu)+v_2(\Xi)=r\qquad(2\mid\mu).}
\]

At `p=5`,

\[
\boxed{
v_5(\mu)+v_5(\Xi)
=v_5(a_0)+r+v_5(D).
}\tag{V5}
\]

There is no universal upper bound on `v5(Xi)` below the right-hand decimal budget: the R29 counterexample has

\[
v_5(\Xi)=5=r,
\]

while `v5(mu)=v5(a0)=v5(D)=0`.

## 8. Fully expanded support-core equation

Eliminating `Xi` and `ell` from MU-CORE gives

\[
\begin{aligned}
F_{\rm support-core}:={}&
\mu Q_0W
+\mu A10^{n+g}Q_0
-\mu u_0AWC_3
-\mu u_0AW10^nC_2\\
&-u_0a_0 10^{r+k}P_1
+u_0a_0 10^rQ_0
=0.
\end{aligned}
\tag{SC}
\]

No new factor occurs. After `g1*=g0 mu` and `AW=g0 a0`, this is precisely the same arithmetic content as R28 TC1 together with the face substitutions.

## 9. TC1 is exactly the old Direct-W equation

R24 Direct-W is

\[
W\,[u_0AXYGD-g_1^*T]=g_1^*AYH.
\]

Rearranging,

\[
AWu_0XYGD=g_1^*(WT+AYH),
\]

which is exactly TC1-PF. Therefore

\[
\boxed{
\texttt{TC1\_EQUALS\_DIRECT\_W\_MASTER=YES}.
}
\]

Consequently, after the post-support/master locus has already imposed Direct-W, conditioning the denominator ratio on TC1 supplies no new independent equation.

## 10. R29 counterexample to universal Smith collision

Take

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*;n,m,k,g)=(1,20,1,80;4,1,1,0).
\]

Then

\[
C_2=71,\qquad C_3=4727,
\]

\[
T=250,\quad H=3557,\quad D=1423,
\]

\[
g_0=20,\quad\mu=4,\quad a_0=1,
\]

\[
\ell=10020,\qquad \Xi=35,575,000,\qquad r=5.
\]

Exact TC1:

\[
80[20\cdot250+10^4\cdot3557]
=2,846,000,000
=20\cdot10^5\cdot1423.
\]

Exact μ-core:

\[
4\cdot35,575,000
=142,300,000
=10^5\cdot1423.
\]

But

\[
\boxed{(\mu,C_2C_3)=\gcd(4,71\cdot4727)=1.}
\]

The positive radial interval is exactly `[1,1]`, and all shape gcds pass. Hence

\[
\boxed{
\texttt{MU\_SMITH\_UNIVERSAL\_COLLISION=FALSE}.
}
\]

The same point also disproves the proposed size kills

\[
0<\Xi<10^r,
\qquad
0<\Xi<\min(C_2,C_3),
\]

because

\[
35,575,000>100,000,
\qquad
35,575,000>71.
\]

## 11. Final μ-core classification for R29

The architecture-free information obtained from μ-CORE is therefore exactly:

\[
\boxed{(\mu,a_0)=1,\quad \mu\mid10^rD,\quad\mu\mid10^rQ_0,}
\]

\[
\boxed{
\operatorname{supp}(\mu)\cap\operatorname{supp}(C_2C_3)
\subseteq\{2,5\},
}
\]

but the remaining decimal-primary collision is **not** universal.

The μ-Smith route is therefore mathematically falsified as a global killer, not merely unproved.
