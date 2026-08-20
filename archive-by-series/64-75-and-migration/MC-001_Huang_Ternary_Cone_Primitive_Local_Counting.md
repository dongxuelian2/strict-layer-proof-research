# Migration Card MC-001 — Huang Ternary Cone Primitive Local Counting

## MIGRATION_CARD_ID
`MC-001`

## STATUS
`BRIDGE_REQUIRED`

Initial creation state in 75-R2 was `ACTIVE_MIGRATION`; after applicability audit it was updated to `BRIDGE_REQUIRED` rather than silently replaced.

## EXTERNAL_THEOREM
Zhizhong Huang, *Quantitative strong approximation for ternary quadratic forms III*, Theorem 1.3, with §§3–4 used for projective/Brauer interpretation.

## THEOREM_CARD_REF
`75_R2/THEOREM_CARDS/TC-001_Huang_Theorem_1_3.md`

## SOURCE
arXiv:2512.13091v1, 15 Dec 2025, Theorem 1.3; Proposition 3.1; §4.

## PROJECT_TARGET
`B3 / N2`, with B2 diagnostics.

## OUR_OBJECT
For an actual split q>1 fibre \(\tau\): R20 source semantic integral model \(\mathscr X_{{\rm sem},\tau}\), punctured generic cone \(X_\tau^\times\), source lattice \(\Gamma_{\rm src,\tau}\), finite projective open \(U_f^{\rm proj}\), moving region \(\Omega_\tau(G)\).

## EXTERNAL_OBJECT
Punctured affine cone \(W^o=(F=0)\setminus0\) of a fixed nondegenerate indefinite integral ternary quadratic form, primitive integral points, fixed congruence residue, fixed smooth real weight.

## OBJECT_MAP
\[
\Phi_\tau:\quad
Q_\tau|_{\Gamma_{\rm src}}\mapsto F,
\quad x_0\mapsto\text{primitive vector},
\quad U_f\mapsto(L,\Gamma)\text{ or finite union thereof},
\quad J\mapsto w_J.
\]
Inverse reconstruction is not taken through Huang coordinates: output ray -> R14 multiplier -> R20 inverse source reconstruction.

## HYPOTHESIS_LEDGER
- H1 nondegenerate indefinite ternary form: **PASS** (R13/R20).
- H2 rationally split/isotropic fibre: **PASS CONDITIONALLY** under N1 criterion.
- H3 fixed integral model/form during one theorem application: **PASS only after freezing \(\tau\)**.
- H4 fixed local level/residue: **PASS only after freezing \(\tau\)**; actual family level moves.
- H5 fixed smooth compactly supported weight: **PASS only after freezing \(\tau\)**; target weight moves.
- H6 v1 literal `Omega | L` assumption after `Omega=8 L Delta`: **UNKNOWN / SOURCE-STATEMENT ANOMALY**.
- H7 uniform constants as \(\tau\) varies with \(G\): **UNKNOWN -> B3-U**.
- H8 theorem threshold guaranteed below coupled scale \(B=G\): **UNKNOWN -> B3-T**.

## LOCAL_PLACE_LEDGER
- p=2: source/contact model retained; include in theorem level if needed.
- p=5: same.
- p|Delta: theorem bad set; must be included in uniform level audit.
- p|conductor/q/M0: use R20 semantic integral model; no ambient smoothness assumption.
- p|u: actual primitive projective unit-open from R14.

## ARCHIMEDEAN_LEDGER
- real component: fixed source W-component.
- sector: \(J\subset\mathscr I_\eta\).
- radial condition: \(G\theta(\eta)<a<G\).
- moving window: yes.
- uniformity: **BRIDGE_REQUIRED**.

## PRIMITIVITY_LEDGER
The theorem natively counts primitive affine vectors via Möbius inversion. Project semantics use it only for the primitive ray; final row primitivity is not required.

## SEMANTIC_PRESERVATION
```text
SOURCE_ROW=PRESERVED_BY_R20_RECONSTRUCTION
SOURCE_LATTICE=PRESERVED_AFTER_SOURCE_BASIS_MAP
PRIMITIVITY=PRESERVED_AT_RAY_LEVEL
DIGIT_REGION=BRIDGE_REQUIRED
POWER_TEN_PARAMETER=BRIDGE_REQUIRED
ORIGINAL_RECONSTRUCTION=PRESERVED
```

## BRAUER_RECIPROCITY_STATUS
`CONTROLLED`

Reason: actual projective ray opens already contain a global rational point by R14; Huang's §3–4 explains why fixed affine residues can have reciprocity while projective unit-scaling removes that correction.

## REQUIRED_BRIDGES
- `B3-U`: uniform dependence on moving form/source lattice/local level/weight.
- `B3-T`: prove theorem threshold fits the one-shot scale \(B=G\).
- `SRC-1`: clarify/correct the literal v1 Theorem 1.3 `Omega | L` statement before formal theorem quotation.

## BRIDGE_DIFFICULTY
- B3-U: `MAJOR`
- B3-T: `MAJOR`
- SRC-1: `ROUTINE` as source clarification, but hard veto until resolved.

## IMPORTED_CONCLUSION
Safe imported conclusion at R2:

> For a **fixed** ternary cone with fixed local data and fixed smooth real weight, primitive integral point distribution with congruence restrictions is governed by a linear height asymptotic with an explicit reciprocity-sensitive secondary term; thus primitive+local counting is standard fixed-data mathematics.

Not imported: the moving-family existence statement N2.

## M_LEVEL
`M3_FIXED_DATA / P2_M5_B_AFTER_REDUCTION`

## G_LEVEL
`G2`

## DEPENDENCY_GRAPH_POSITION
`R20 semantic model + N1(split) + R14 local ray open -> MC-001 fixed-data engine -> USSPAL bridge -> R14 radial multiplier -> R20 reconstruction`

## REPLACED_INTERNAL_MACHINERY
None by itself; together with the P2 stack it prevents rebuilding primitive cone counting from scratch.

## CURRENT_BLOCKER
`UNIFORM_MOVING_FAMILY_CONSTANTS_AT_B=G`

## NEXT_ACTION
Trace or prove a uniform primitive-ray estimate in source height for the actual \(Q_\tau,\Gamma_\tau,U_{f,\tau}\) family.

## UPDATE_LOG
- **2026-08-18 / 75-R2:** created with `STATUS=ACTIVE_MIGRATION`. Supporting artifacts: R20 actual report; 75-R1 terminal verdict.
- **2026-08-18 / 75-R2:** `STATUS -> BRIDGE_REQUIRED`; added source-statement anomaly, moving-family uniformity blockers, projective reciprocity control. Supporting artifacts: `08_quantitative_theorem_registry.md`, `09_height_bridge_analysis.md`, Huang arXiv:2512.13091v1.
