# Migration Stack P2 — Source Punctured Cone -> Projective Ray -> Moving Height

## Stack goal

Supply N2 without losing source semantics.

## Components

1. **Internal R20 semantic integral model** — exact source reconstruction and finite-packet retirement.
2. **MC-002 Cao–Xu** — qualitative toric/Brauer strong-approximation skeleton at finite places.
3. **Internal R14 projective weak approximation** — actual finite primitive open + real projective sector compatibility; controls N3.
4. **MC-001 Huang** — fixed-data primitive ternary-cone counting with local conditions and reciprocity-sensitive correction.
5. **MC-003 Kelmer–Yu** — fixed-form shrinking-sector exponent \(r\asymp T^{-1/2}\) for ternary signature.
6. **New bridge USSPAL** — uniformize the projective primitive-ray estimate over the actual moving family.
7. **Internal R14 radial multiplier theorem** — convert a sufficiently small-height ray to an exact decimal radial point.
8. **Internal R20 inverse map** — reconstruct legal source row.

## Canonical composition

\[
\boxed{
\begin{array}{c}
\mathscr X_{\rm sem}(\tau)\\
\downarrow\\
X_\tau^\times\to C_\tau\simeq\mathbb P^1\\
\downarrow\\
U_{f,\tau}^{\rm proj}\times J_\tau\\
\downarrow\quad\text{USSPAL}\quad\\
\text{primitive ray }x_0,\ a_0\text{ small}\\
\downarrow\quad\text{R14}\quad\\
n x_0\in\Omega_\tau(G),\ (n,10u)=1\\
\downarrow\quad\text{R20}\quad\\
\text{legal source row.}
\end{array}}
\]

## Why quotient first

A fixed primitive affine residue can carry a reciprocity obstruction on the punctured cone. The projective source problem is naturally invariant under unit scaling and R14 already proves global projective compatibility. Thus P2 should migrate through the projective conic and only reinsert radial scale afterwards.

## Stack status

```text
SOURCE_MODEL=MIGRATED/EXACT
TORSOR_DICTIONARY=M4_COMPLETE
FINITE_BM_LAYER=CONTROLLED
PROJECTIVE_RECIPROCITY=CONTROLLED
MOVING_HEIGHT=BRIDGE_REQUIRED
N2=REDUCED_TO_USSPAL
P2=M5_B
```
