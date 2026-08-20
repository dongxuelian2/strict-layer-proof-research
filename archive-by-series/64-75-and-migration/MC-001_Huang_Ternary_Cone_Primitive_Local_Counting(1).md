# Migration Card MC-001 — Huang Ternary Cone Primitive Local Counting

## MIGRATION_CARD_ID
`MC-001`

## STATUS
`SUPERSEDED`

The card is retained for provenance. The external theorem remains a valid fixed-data template, but 75-R3 proves that its role in the P2/USSPAL fixed-data approximation layer can be replaced by an elementary \(\mathbf P^1\) argument.

## UPDATE_ROUND
`75-R3`

## CURRENT_TARGET
`USSPAL uniformity audit`

## CURRENT_BLOCKER
`C_fam dependence and clearance inequality`

Refined blocker:
`SOURCE-INTEGRAL SPLITTING-FRAME DISTORTION + ALLOWED-u-OPEN QUANTITATIVE COST`

## EXTERNAL_THEOREM
Zhizhong Huang, *Quantitative strong approximation for ternary quadratic forms III*, Theorem 1.3.

## PRIOR_R2_ROLE
Fixed ternary cone + primitive integral points + fixed local data + fixed real weight; used as the closest quantitative template.

## R3_SUPERSEDING_RESULT

For a fixed source-integral split chart
\[
\Phi:\mathbf P^1\to C_\tau,
\]
75-R3 proves the Primitive Sector-Congruence Lemma
\[
H(s,t)\ll m\rho^{-1}
\]
for any unimodular projective residue class, with primitive normalization preserving the projective class and decreasing height.

Composing with R20's degree-2 source parameterization gives
\[
a_0\ll
\mathcal A_{\tau,\Phi}
\Lambda_{\tau,\Phi}^2
m^2\rho^{-2}.
\]

Therefore the fixed-data existence exponent and primitive-congruence mechanism no longer require MC-001.

## HYPOTHESIS_CHANGES

```text
H1_NONDEGENERATE_FORM=NO_LONGER_EXTERNAL_ENGINE_REQUIREMENT
H2_SPLIT_FIBRE=STILL_REQUIRED_BY_N1
H3_FIXED_FORM=REPLACED_BY_EXPLICIT_SOURCE_SPLIT_CHART
H4_FIXED_LOCAL_LEVEL=REPLACED_BY_PROJECTIVE_CLASS_LEMMA
H5_FIXED_WEIGHT=REPLACED_BY_REAL_INTERVAL
H6_SOURCE_STATEMENT_ANOMALY=RETAINED_FOR_PROVENANCE_ONLY
H7_UNIFORM_CONSTANT=REPLACED_BY_EXPLICIT_D_split_AUDIT
H8_THRESHOLD_B=G=REPLACED_BY_DIRECT_CLEARANCE_INEQUALITY
```

## BRIDGE_CHANGES

Old:
`moving form/source lattice/local level/weight -> opaque B3-U/B3-T`

New:
\[
\boxed{
C_{\rm fam}\le \mathfrak D_\tau\mathfrak E_\tau^2
}
\]
with separately auditable
- source splitting-frame height/distortion;
- parameter saturation;
- allowed \(u\)-open cost.

## SOURCE_STATUS
The v1 source-statement anomaly remains recorded, but it is no longer a P2 blocker because the theorem is not used as the USSPAL engine.

## M_LEVEL
`M3_FIXED_DATA / SUPERSEDED_FOR_P2_USSPAL_ENGINE`

## G_LEVEL
`G2`

## NEXT_ACTION
Bound \(\mathfrak D_\tau\) in the actual power-ten source family and improve the allowed-class cost \(\mathfrak E_\tau\le u\).

## UPDATE_LOG

- 75-R2: created `ACTIVE_MIGRATION`.
- 75-R2: changed to `BRIDGE_REQUIRED` after moving-family audit.
- 75-R3: changed to `SUPERSEDED` for the P2 USSPAL engine by the internal R3 primitive sector-congruence theorem plus R20 source-adapted \(\mathbf P^1\) parameterization. Card retained; no deletion.
