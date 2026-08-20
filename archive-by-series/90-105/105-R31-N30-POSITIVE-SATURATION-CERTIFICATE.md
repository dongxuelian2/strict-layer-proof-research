# 105-R31 — N30 Positive Saturation Certificate

## Frozen status

R30 already eliminated residual q as an independent existential coordinate. R31 opens the resulting count at its lower edge.

## New exact theorems

```text
Q1_EXACT_FORCED_SCALE_EQUIVALENCE=PROVED
UNIT_CHAMBER_N30_IFF_U0_NONEMPTY=PROVED
Q_WINDOW_MULTIPLICATIVE_BOUND_LT_10=PROVED
PRIME_STRIPPING_LOWER_EDGE_RIGIDITY=PROVED
MINIMAL_Q_PRIME_OR_QUADRATIC_STRIP=PROVED
UNIT_PRIME_FINITE_COMPOSITE_TRICHOTOMY=PROVED
Q1_SOURCE_COLLISION_Q0_LE_3000=PROVED
```

The core formulas are

\[
q=1\iff Z_-\le\Lambda\le Z_+,
\]

\[
Q_-=1\le Q_+\Longrightarrow (N_{30}>0\iff\mathcal U_0\ne\varnothing),
\]

and for a minimal admissible q>1,

\[
\forall p\mid q:\quad q/p<Q_-,
\]

hence

\[
q\text{ prime}\quad\text{or}\quad q<Q_-^2.
\]

## Search saturation

R28 complete q1 autopsy through \(Q_0\le3000\): 7 forced-scale raw-TC1 hits, all source-room dead.

New architecture-first exact reverse searches: no integer TC1-conic solution in the recorded scopes.

No genuine N30-positive architecture was found.

## What is not proved

```text
Q1_FORCED_SCALE_EXTINCTION_GLOBAL=NOT_PROVED_NOT_FALSIFIED
MINIMAL_Q_DESCENT_TO_ONE=NOT_PROVED
GLOBAL_N30_ZERO_THEOREM=NOT_PROVED
STRICT_A1_UNLIFTABILITY=NOT_PROVED
FULL_STRICT_A1_WITNESS_FOUND=NO
```

## Minimal remaining object

The remaining object is no longer a free denominator integer. It is the deterministic **architecture-uniform lower-edge coprime successor**:

\[
q_{\min}(\mathfrak a,U)=\min\{q\ge Q_-:(q,FU)=1\},
\]

subject to \(q_{\min}\le Q_+\), split exactly into:

1. the unit chamber \(Q_-=1\), where only source-fibre nonemptiness remains;
2. a prime q in the real architecture window not dividing FU;
3. a finite composite strip below \(Q_-^2\).

Any further attack that does not use one of these three exact classes is information-regressive relative to R31.
