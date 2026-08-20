# 75-R2 — Moving Archimedean Digit Region (B3 geometry)

## 1. Exact radial inequalities

For an actual source point on one positive ray, with source homogeneous coordinates \(a,h,x\) and
\[
10x=(A+\eta)a,\qquad \eta=h/a,
\]
the inherited third-digit and LOW inequalities are
\[
\frac G{10}\le a<G,
\qquad x>\frac{AG}{10}.
\]
The LOW inequality becomes
\[
a>\frac{AG}{A+\eta}.
\]
Hence the exact continuous radial lower factor is
\[
\theta_\tau(\eta)=\max\left(\frac1{10},\frac{A}{A+\eta}\right),
\]
and the radial relative width is
\[
\boxed{
\kappa_\tau(\eta)=1-\theta_\tau(\eta)
=\min\left(\frac9{10},\frac{\eta}{A+\eta}\right).}
\]

Let \(\mathscr I_{\eta,\tau}\) denote the exact W-admissible projective sector from R15. Then, before the discrete multiplier condition, the real source region is
\[
\boxed{
\Omega_\tau(G)=
\{x\in X_\tau^\times(\mathbb R)_{\rm src,+}:
\eta(x)\in\mathscr I_{\eta,\tau},\ 
G\theta_\tau(\eta(x))<a(x)<G\}.}
\]
Endpoint conventions can be restored from the exact floor/ceil formulas; they do not change the geometric classification.

## 2. Shape

This is a two-dimensional annular sector on the real cone:

- radial scale: \(a\asymp G\);
- radial thickness at projective coordinate \(\eta\): \(G\kappa_\tau(\eta)\);
- angular/projective set: \(\mathscr I_{\eta,\tau}\);
- real component: fixed by the source sign/W-sector;
- family parameters: \(A,u,K,q,D_0,F_0,N_0\) all move with the actual tuple.

It is **not** in general one fixed dilation \(G\Omega\).

## 3. Invariant volume

On a smooth two-dimensional quadratic cone the Leray/invariant measure has, in radial/projective coordinates, the form
\[
d\mu_\tau=J_\tau(\eta)\,da\,d\eta,
\]
with \(J_\tau\) smooth and positive on compact source charts. Therefore
\[
\boxed{
\mu_\tau(\Omega_\tau(G))
=G\int_{\mathscr I_{\eta,\tau}}
J_\tau(\eta)\kappa_\tau(\eta)\,d\eta.}
\]

For a fixed fibre and a fixed compact subarc \(J\Subset\mathscr I_\eta\) with \(\inf_J\kappa>0\), the volume grows linearly in \(G\).

## 4. The degeneration that blocks a direct import

R15 proves that the admissible projective region can approach the LOW boundary \(\eta=0\). There
\[
\kappa_\tau(\eta)\sim \frac{\eta}{A}.
\]
Thus the radial width can shrink even while the radius is \(\asymp G\). Across the moving power-ten family there is currently no proved uniform lower bound for

- the weighted angular mass \(\int J\kappa\),
- the inradius of a compact admissible subarc,
- the source-height distortion of a split coordinate,
- or the theorem threshold as the form/lattice/local level move.

Hence `volume -> infinity` is true on any fixed nondegenerate subarc, but is **not yet uniform across the actual family**.

## 5. Power-ten sequence

A theorem valid uniformly for every sufficiently large real scale \(T\) would automatically cover \(T=G=10^g\). The present obstacle is not discreteness of powers of ten; it is that the *object itself* changes with \(g\).

```text
ARCHIMEDEAN_REGION_STATUS=EXACT_MOVING_ANNULAR_SECTOR_DEFINED
UNIFORM_WELL_ROUNDEDNESS=OPEN
```
