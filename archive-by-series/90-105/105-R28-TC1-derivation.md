# 105-R28 — TC1 Derivation and Global Lemmas

## 1. Clearing denominators

Starting from

\[
\frac{Wg_1^*T}{AY}-g_1^*P_2
=G\{Wu_0P_1XK-Q_0(Wu_0X+g_1^*)\},
\]

multiply by `AY` and move all terms to one side.  This gives the five-term integral equation `F-TC1` recorded in `105-R28-TC1-normal-form.md`.  Regrouping the first two and the middle two terms gives `PF-TC1`.

The positivity assertion `D>0` is exact: `T>0`, `H=GQ0-P2>0`, and all selectors/powers are positive, so the left side of PF-TC1 is positive.

## 2. Primitive selector gcd theorem

Because

\[
u_0\mid P_2/W,\qquad u_0\mid P_3/A,
\]

we have `u0|P2` and `u0|P3`.  If a prime divides both `u0` and `P1`, it divides `P1,P2,P3`; the sphere equation then makes it divide `Q0`, contradicting primitivity.  Thus

\[
(u_0,P_1)=1.
\]

The same argument with `Q0` in place of `P1` gives `(u0,Q0)=1`.  Since `g1*|P1`, it follows that

\[
\boxed{(u_0,g_1^*)=1.}
\]

This proves that the fraction in `RATIO` is already the selector pair after ordinary gcd reduction.

## 3. Support allocation theorem

Substitute

\[
P_2=u_0WC_2,\qquad P_3=u_0AC_3
\]

into PF-TC1.  One obtains

\[
g_1^*Q_0(W+A10^{n+g})
=AWu_0\{g_1^*(C_3+10^nC_2)+10^{m+n+g}D\}.
\tag{3.1}
\]

The right side is divisible by `u0`; the factor `g1*Q0` on the left is an `u0`-unit.  Hence

\[
u_0\mid W+A10^{n+g}.
\]

Let `ell=(W+A10^(n+g))/u0`.  Under `(A,W)=1`, if `d|(u0,A)`, then `d` divides both `A` and `W`, so `d=1`.  Therefore `(u0,A)=1`.  Since

\[
u_0\ell\equiv W\pmod A
\]

and both `u0,W` are `A`-units, `(ell,A)=1`.  Dividing (3.1) by `u0` then gives `A|g1*Q0`.

Also

\[
\gcd(u_0,W)=\gcd(u_0,A10^{n+g})=\gcd(u_0,10^{n+g}),
\]

so common support of `u0` and `W` is decimal only.  For a prime power `p^e||W` with `p notin {2,5}`, the same identity shows `p` divides neither `u0` nor `ell`; since the divided equation has a factor `W` on its right side, `p^e|g1*Q0`.  Hence `W^(10')|g1*Q0`.

## 4. Mu-core

Since `(u0,P1)=1`,

\[
g_0=(u_0AW,P_1)=(AW,P_1),
\]

so `g0|AW`.  Write `g1*=g0 mu` and `AW=g0 a0`.  Divide PF-TC1 by `g0`, substitute the expression in braces from (3.1), and then cancel `u0`.  This gives

\[
\boxed{\mu\Xi=a_0 10^{m+n+g}D},
\]

where

\[
\Xi=Q_0\ell-AW(C_3+10^nC_2)>0.
\]

This is equivalent to TC1 after the displayed selector/support definitions; it is not a relaxation.

## 5. TC1-support 2-adic extinction on the C3-even branch

### Theorem R28-C3-ODD

Every tuple satisfying TC1, the R24 shape gcds, and mu-Smith must have

\[
\boxed{C_3\text{ odd}.}
\]

### Proof

Assume `C3` even.  Shape gives `W` odd.  Since `10^(n+g)` is even and

\[
u_0\mid W+A10^{n+g},
\]

the divisor `u0` is odd and therefore `ell` is odd.  Primitive sphere packets have `Q0` odd.  Hence

\[
\Xi=Q_0\ell-AW(C_3+10^nC_2)
\]

is odd: its first term is odd and the second is even.

Mu-Smith and `2|C3` force `mu` odd.  Thus the left side `mu Xi` of MU-CORE is odd.  Its right side contains `10^(m+n+g)` with `m,n>=1`, hence is even.  Contradiction.  QED.

This directly globalizes the 2-adic reason behind the deepest historical `C3=8` TC1 hits.

## 6. Exact recurrence / monotonicity identities

Let

\[
C=\frac{Wg_1^*T}{A},\qquad D_2=g_1^*P_2.
\]

Then `R_n=C/10^n-D2`, so

\[
\boxed{R_n-10R_{n+1}=9g_1^*P_2.}
\]

For fixed `k=rho-m`, the legal diagonal shift `(m,rho)->(m+1,rho+1)` satisfies

\[
\boxed{S_{m+1,\rho+1}=10S_{m,\rho}+9Q_0g_1^*.}
\]

Also TC1 is affine-linear in `G`:

\[
\boxed{
A10^nG\bigl(g_1^*Q_0-Wu_0 10^mD\bigr)
=g_1^*\bigl(A10^nP_2-WT\bigr).
}
\]

Thus, outside the simultaneous zero branch, fixed packet/selectors/`m,n,k` admit at most one `G=10^g`.  The simultaneous zero branch is exactly the R26 frozen `R_n=S_{m,rho}=0` branch and does not restore an infinite scale because the exponent simplex remains finite for a fixed packet.

## 7. Resultant and T-minus discriminant

TC1 is the hyperplane `BQ0=c.P`.  Eliminating `Q0` against the sphere gives, up to an irrelevant sign,

\[
(c_1P_1+c_2P_2+c_3P_3)^2-B^2(P_1^2+P_2^2+P_3^2)=0.
\]

No new factor is produced, so the strict R28 audit is

```text
RESULTANT_INFORMATION_GAIN=0
```

although the conic is a useful exact geometry for fixed architectures.

For the forced `T=Q0-P3` route, set

\[
L_0=A10^nG(g_1^*+Wu_0 10^m),
\]

\[
N_0=AWu_0 10^{m+n}GK P_1+g_1^*A10^nP_2.
\]

TC1 gives

\[
Q_0=\frac{N_0-g_1^*WT}{L_0}.
\]

Substitution in

\[
P_1^2+P_2^2=T(2Q_0-T)
\]

gives

\[
(L_0+2g_1^*W)T^2-2N_0T+L_0(P_1^2+P_2^2)=0.
\]

The discriminant core is

\[
\Delta_0=N_0^2-L_0(L_0+2g_1^*W)(P_1^2+P_2^2).
\]

On TC1+sphere,

\[
\boxed{\Delta_0=(L_0P_3-g_1^*WT)^2.}
\]

Hence the square-discriminant route is exact but tautological here:

```text
DISCRIMINANT_INFORMATION_GAIN=0
```

## 8. Infinite raw-TC1 conic family

The first R27 hit has fixed architecture

\[
(A,W,u_0,g_1^*,n,\delta,m,k,g)=(1,2,1,10,2,0,1,1,0),
\]

and primitive hyperplane

\[
\boxed{1000P_1+50P_2+P_3=151Q_0.}
\tag{F1-H}
\]

A rational parameterization of its sphere intersection is

\[
\begin{aligned}
P_1&=60(6767r^2-80999rs+529833s^2),\\
P_2&=-20(21191r^2-1966698rs+5863194s^2),\\
P_3&=123(20301r^2-100000rs-977199s^2),\\
Q_0&=2565073r^2-19242000rs+170904573s^2.
\end{aligned}
\tag{F1-PAR}
\]

Symbolic expansion verifies both the sphere equation and F1-H identically, and

\[
Q_0-P_3=50(1361r^2-138840rs+5822001s^2).
\]

Take `N=10j+3`, `r=16998N+1`, `s=947N+1`.  Then `r,s` have opposite parity and

\[
r\equiv0\pmod5,\qquad s\equiv2\pmod5.
\]

Thus the common content of the four coordinates is coprime to 10.  Primitive normalization therefore preserves `10|P1`, `2|P2`, and the factor 50 in `T`.  The explicit quadratic polynomials stored in `105-R28-symbolic-elimination.txt` are positive for `N>=3`, and satisfy

\[
5P_2-P_3>0,\qquad20P_3-P_2>0,
\]

which is exactly the `delta=0` window for `(P2/2)/P3`.  The slopes are distinct, so this gives infinitely many distinct primitive raw-TC1 packets.

Therefore

\[
\boxed{\mathfrak T_{28}\ne\varnothing\text{ and is infinite}.}
\]

In particular, global raw-TC1 extinction and global finite raw-TC1 classification are false.

## 9. Why the infinite family does not survive support

For the F1 architecture, `n2=n+delta=2` and `n=2`, while `C2=P2/2`, `C3=P3`.  Any positive radial `U>=1` would force

\[
1\le C_2,C_3\le99.
\]

Equivalently `P2<=198` and `P3<=99`.  The complete exact conic classifier in `r28_architecture_cert.py` checks this finite domain via the exact quadratic discriminant and finds no integral primitive F1 point in the radial box.  This is a global extinction theorem for the entire F1 conic architecture, not a height-bounded search.

## 10. Exact remaining obstruction

After TC1 ratio elimination, W-reconstruction fusion, support allocation, and C3-even extinction, the unresolved global object is the union over still-unbounded selector/exponent architectures of finite radial sections of the conic `CONIC`, subject to

\[
\mu\Xi=a_0 10^{m+n+g}D,
\qquad (\mu,C_2C_3)=1,
\qquad C_3\text{ odd},
\]

plus the frozen tail gates.  A proof that all such architectures are impossible is not obtained in R28.
