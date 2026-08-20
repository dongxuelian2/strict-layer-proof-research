# 105-R37 — Corrected Source-First Search

## 1. Arithmetic and implementation
All acceptance/rejection decisions use exact integer arithmetic. The main census uses C++ `__int128` plus an exact bitwise integer square root; no floating-point test participates in square/root acceptance. Every emitted root is independently replayed in Python from NTC1 and the sphere equation.

`r37_root_replay_verify.py` reports:

```text
ROOT_ROWS=36
R36_REGRESSION_ROOTS=12
AUTOPSY_ROWS=12
ERRORS=0
INDEPENDENT_ROOT_REPLAY=PASS
```

## 2. Exact R36 regression
The uncorrected R36 shell is reproduced exactly:

| quantity | count |
|---|---:|
| source coarse architectures | 753,662 |
| F11 configurations | 8,922,022 |
| square discriminants | 297 |
| raw integer MASTER/sphere roots | 12 |
| selector-consistent roots | 0 |

The 12 split as 6 `g0 does not divide P1` and 6 `mu does not divide r`.

## 3. Same shell with primitive g0 allocation restored
Restoring the R31/R28 necessary condition \(g_0\mid AW\), while keeping the same R36 source superset, gives:

| quantity | count |
|---|---:|
| source coarse architectures | 753,662 |
| prefilter input configs | 8,922,022 |
| pre-discriminant normalized rejects | 5,601,083 |
| square discriminants after prefilter | 73 |
| raw integer roots | 2 |
| selector-consistent roots | 0 |

The two remaining raw roots are exactly the t=1 representatives of F_A and F_B: one fails \(g_0\mid P_1\), the other fails \(\mu\mid r\).

## 4. Production shape + normalized expansion, n2=2,n3=1
With full shape gcd `(A,W)=1` and the primitive `g0 | AW` prefilter, q=1 through \(u_0\le60\) gives:

```text
source=1,768,988
configs=25,929,293
pre-normalized-reject=18,393,251
disc_sq=30
raw_integer_roots=1
selector_consistent=0
post_basic=0
simultaneous=0
```

The sole raw root is
\[
(u_0,\Lambda,A,W,C_2,C_3,\mu,g_0,a)=(3,5,1,1,58,9,5,1,3),
\]
\[
(P_1,P_2,P_3,Q_0)=(18,174,27,177),
\]
and it dies deterministically because \(r=18\) but \(5\nmid18\).

## 5. Nonunit stress in the same exponent cell
Prescribed one-digit residual scales q=2,3,5,7, all with \(u_0\le60\):

| q | source | configs | square discriminants | raw integer roots | selector-consistent |
|---:|---:|---:|---:|---:|---:|
| 2 | 368,102 | 3,419,744 | 12 | 0 | 0 |
| 3 | 239,291 | 1,803,893 | 7 | 0 | 0 |
| 5 | 49,850 | 216,147 | 0 | 0 | 0 |
| 7 | 49,850 | 216,147 | 0 | 0 | 0 |

These are bounded stress lanes, not a global nonunit theorem.

## 6. New source digit cell n2=3,n3=1
For q=1, m2=m3=1, g=0, k=2, \(u_0\le20\), the complete source-coarse box gives

```text
source=5,912,791
configs=67,546,418
square_discriminants=40
raw_integer_roots=0
selector_consistent=0
post_basic=0
simultaneous=0
```

This lane was searched in a normalized superset using `(a,mu)=1`; because it already has zero raw roots, adding the stronger `g0 | AW` primitive prefilter cannot create a root.

## 7. Combined bounded evidence
Across the expanded production/stress lanes (excluding the duplicate uncorrected R36 regression), 99,131,642 exact normalized F11 configurations were inspected after source-coarse generation. No selector-consistent integer MASTER/sphere root was found.

This is a strong bounded saturation result. It is NOT promoted to a global extinction theorem.
