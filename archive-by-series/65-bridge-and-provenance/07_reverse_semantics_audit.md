# 75-R7 Interface B — Reverse Source Semantics Audit

## Forward map actually available

For a genuine q>1 source solution, the existing 65 machinery gives
\[
\Phi_{\rm fwd}:
\text{source data}
\longmapsto
\bigl((G,K),q,u,[\alpha:T:Y]\bigr)
\]
with
\[
(G,K)\in\Gamma_{10},
\qquad uq=G+1,
\qquad \mathcal Q_{G,K,q}([\alpha:T:Y])=0,
\]
and the coefficient-vector Veronese syzygies automatically satisfied.

Thus
```text
FORWARD_MAP_STATUS=EXACT
```

## Image conditions not retained by the algebraic incidence

The mixed algebraic incidence does **not** by itself retain:

1. \(q,u\) positive integral divisor semantics;
2. rationality/integrality of the projective conic point;
3. the saturated source lattice;
4. primitive gcd / ten-unit conditions;
5. the actual digit inequalities and radial multiplier interval;
6. exact reconstruction of \(N,Z,a_3,x,d,t,\ldots\);
7. the original concatenation variables.

These conditions are not decorative. R13/R20 show that source-lattice and multiplier semantics are precisely what remain after projective compression.

## Spurious-point theorem

Because the algebraic conic incidence is dominant over \((G,K,q)\) after base change to an algebraic closure, it supplies algebraic incidence points for generic power pairs regardless of whether a legal source solution exists.

Hence the projection
\[
\text{mixed incidence}\to\Gamma_{10}
\]
has systematic spurious points unless the missing arithmetic conditions are restored.

```text
SPURIOUS_POINT_STATUS=GENERIC_AT_ALGEBRAIC_LEVEL
```

This is not merely a finite exceptional set that could be removed before applying Laurent/ESS.

## Reverse map status

Given only \((G,K)\in\Gamma_{10}\) and an algebraic incidence point, there is no certified procedure that recovers a legal integral primitive source state. To do so one must reimpose exactly the live arithmetic gates:

\[
\text{integral divisor choice }q\mid G+1,
\]
\[
\text{rational/source-lattice point on the conic},
\]
\[
\text{primitive/digit/radial realization}.
\]

Those are not consequences of the algebraic incidence and include the same source-realization difficulty the N4 architecture was supposed to replace.

Therefore
\[
\boxed{
\texttt{N4A_FAILURE=ALGEBRAICIZATION_AS_HARD_AS_ORIGINAL}.
}
\]
Supporting diagnostics are

```text
UNBOUNDED_AUXILIARY_VARIABLES=TRUE
REVERSE_SEMANTICS_LOST=TRUE_UNLESS_ORIGINAL_ARITHMETIC_GATES_ARE_REINTRODUCED
FORWARD_MAP_STATUS=EXACT
REVERSE_MAP_STATUS=FAIL
SPURIOUS_POINT_STATUS=UNCONTROLLED_GENERIC
```

## q=1 audit

The two-row coefficient map remains rank 6 at \(q=1\), but \(\alpha=0\) adds a special projective stratum. More importantly, the same algebraic-closure dominance persists: a projective quadratic fibre does not impose a proper equation on \((G,K)\) merely because q is fixed.

Thus q=1 and q>1 share only the power base
\[
\Gamma_{10},
\]
not a common source-image characterization.

```text
Q1_QGT1_COMMON_BASE_STATUS=POWER_BASE_ONLY_NOT_SOURCE_IMAGE
```

---

STAGE_INPUTS=05_existing_elimination_reaudit.md; 06_Gamma10_source_image_candidates.md; R13/R20 frozen source reconstruction semantics
NEW_PROVED_RESULTS=Generic spurious algebraic points are unavoidable under the current projection; reverse source map fails without reinstating the original arithmetic gates
NEW_REDUCTIONS=N4-A failure isolated specifically to reverse arithmetic semantics, not to lack of a forward algebraic map
NEGATIVE_RESULTS=Exact Gamma10 source-image equivalence not achieved; q=1/q>1 not unified beyond power coordinates
REJECTED_ROUTES=Necessary-condition projection treated as equivalence; Zariski closure used as source image
EXTERNAL_SOURCES_USED=NONE_NEW
MIGRATION_CARDS_CREATED_OR_UPDATED=NONE
OUTPUT_DEPENDENCIES=08_Laurent_activation_test.md; 09_ESS_activation_test.md; final comparison
UNRESOLVED_ITEMS=No R7 work remains on N4-A after the mandated failure/exit rule
PHASE_STATUS=FROZEN
