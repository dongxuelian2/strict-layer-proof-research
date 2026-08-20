# Migration Card MC-002 — Cassels Small Integral Zero

## MIGRATION_CARD_ID
`MC-002`

## STATUS
`MIGRATED`

## ROLE
`FALLBACK_BENCHMARK_FOR_SOURCE_SPLITTING_HEIGHT`

## EXTERNAL_THEOREM
J. W. S. Cassels, small integral zero theorem for isotropic integral quadratic forms.

## SOURCE
J. W. S. Cassels, “Bounds for the least solutions of homogeneous quadratic equations”, Proc. Cambridge Philos. Soc. 51 (1955), 262–264. Modern statement used for the height normalization: L. Fukshansky and S. Jeong, “Integral zeros of quadratic polynomials avoiding sublattices”, arXiv:2409.10867v2 (2024), equation (1).

## PROJECT_TARGET
`75-R4 / N2 / source-integral splitting distortion D_tau`

## OUR_OBJECT
The primitive integral ternary form Q_tau obtained by pulling the q^5-saturated source core F0(Z,a,x) to the exact source basis
Z=M w1+rho w2, a=w2, x=w3,
with w in Z^3 and M=G/gcd(G,2d(q+4)).

## EXTERNAL_OBJECT
An isotropic integral quadratic form in n variables, n>=2, with coefficient-matrix height |F|=max |f_ij|.

## OBJECT_MAP
Apply Cassels directly to Q_tau on the source-basis lattice Z^3. Rational split of the projective conic implies a nonzero rational zero; homogeneity clears denominators and gives integral isotropy. Cassels then supplies a small nonzero integral zero p in source-basis coordinates.

## HYPOTHESIS_LEDGER
- H1_INTEGRAL_FORM=PASS
- H2_DIMENSION_n=3=PASS
- H3_NONZERO_ISOTROPIC_ZERO=PASS_CONDITIONALLY_ON_N1_SPLIT
- H4_SOURCE_LATTICE=PASS_BY_WORKING_IN_SOURCE_BASIS
- H5_PRIMITIVE_OUTPUT=RECOVERED_BY_GCD_EXTRACTION

## SMALL_ZERO_BOUND
For n=3,
||p||_infty <= C_C(3) * H(Q_tau),
where C_C(3) depends only on the dimension. The exact exponent is 1.

## DIMENSION_SCOPE
`n>=2; ternary n=3 explicitly in scope`

## INTEGRAL_LATTICE_SCOPE
`Integral quadratic form on Z^3 after exact source-basis pullback.`

## SOURCE_LATTICE_COMPATIBILITY
`PASS: the theorem is applied to Q_tau in source-basis coordinates, not to ambient raw coordinates.`

## PRIMITIVE_EXTRACTION
If p=g p0 in source-basis coordinates, divide by gcd g. Homogeneity preserves Q_tau(p0)=0; p0 remains in Z^3; height does not increase.

## DISCRIMINANT_DEPENDENCE
`NONE_IN_THE_CASSeLS_BOUND_USED`

## COEFFICIENT_HEIGHT_DEPENDENCE
`LINEAR for n=3`

## BAD_PRIME_DEPENDENCE
`NONE`

## FRAME_COMPLETION_COST
`NOT_USED. R20 chord/Veronese formula constructs an integral degree-2 P1 chart directly from p.`

## DENOMINATOR_COST
`1 in source-basis coordinates`

## FINAL_DISTORTION_CONTRIBUTION
With H_tau=H(Q_tau), R20 gives D_tau <= 16 H_tau ||p||_infty, hence
D_tau <= 16 C_C(3) H_tau^2.

## MIGRATION_LIMITATION
The theorem is legally applicable and makes D_tau explicit, but its generic coefficient-height exponent is too large for the R3 clearance collision. It is therefore a migrated fallback benchmark, not the final N2 engine.

## UPDATE_LOG
- 2026-08-18 / 75-R4: created and migrated after the audit found no reusable uniformly small explicit source isotropic ray in R13/R20. Source-basis compatibility and n=3 scope checked before use.
