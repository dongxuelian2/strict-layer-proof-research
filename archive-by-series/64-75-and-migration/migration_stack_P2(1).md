# Migration Stack P2 — Updated after 75-R3

## Stack

1. R20 exact source semantic integral model.
2. N1 split test \((-1,N_0)=0\).
3. R20 source-integral degree-2 split chart / \(\mathbf P^1\).
4. **R3 Primitive Sector-Congruence Lemma** — elementary, proved.
5. R3 moving splitting-distortion bound \(\mathfrak D_\tau\) — open.
6. R3 allowed-\(u\)-open cost \(\mathfrak E_\tau\) — fallback \(\le u\), improvement open.
7. R14 radial multiplier with modulus \(10u\).
8. R20 source reconstruction.

## Superseded stack elements

- MC-001 Huang as the P2 fixed-data quantitative engine.
- MC-003/Kelmer–Yu as a necessary shrinking-sector engine.

They remain useful provenance/comparison references but are not current proof dependencies.

## Current canonical collision

\[
\mathfrak D_\tau\mathfrak E_\tau^2j(10u)
<
G\,\mathcal C_\tau^{\max}.
\]

Using the normalized LOW component:
\[
\mathcal C_\tau^{\max}\ge\Psi(R_\tau^{\rm LOW}).
\]

## Status

```text
SOURCE_MODEL=EXACT
FINITE_PACKET=RETIRED
P1_FIXED_DATA_APPROXIMATION=PROVED_ELEMENTARY
MOVING_SPLIT_DISTORTION=OPEN
ALLOWED_u_OPEN_COST=OPEN_IMPROVEMENT
CLEARANCE=EXPLICIT_COLLISION
N2=OPEN_REDUCED
P2=M5-B_STRONGER_R3_REDUCTION
```
