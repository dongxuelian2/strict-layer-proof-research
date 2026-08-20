# 75-R7 — Main-Proof Interface Decision

## Unique decision

Interface A satisfies the R7 structural death condition on the frozen chart:
\[
\boxed{a_p\mathcal H_{\perp,\tau}\ge G/4=G^{1-o(1)}}.
\]

Interface B satisfies the R7 strict N4-A failure condition:
\[
\boxed{\texttt{N4A_FAILURE=ALGEBRAICIZATION_AS_HARD_AS_ORIGINAL}}.
\]
Laurent and ESS therefore remain reserves and cannot be activated.

Hence Decision D applies:

```text
PRIMARY_INTERFACE=NONE
SECONDARY_INTERFACE=NONE
USSPAL_INTERFACE=RETIRED
N4_INTERFACE=RETIRED_IN_75_UNTIL_NEW_ELIMINATION_BREAKTHROUGH
```

No HYBRID is allowed: there is currently no orthogonal division of labour in which N4 proves global finiteness and USSPAL realizes a finite residue. N4 has no global theorem activated, while USSPAL has already hit its exponent floor.

## R8 rearchitecture target

The recommended next architecture is
\[
\boxed{\textbf{DISCRIMINANT-FIRST }N_0\textbf{ / ACTUAL-SPLIT CLASSIFICATION}}.
\]

Start from the exact mixed invariant
\[
\boxed{N_0=4K^2G^2u^2-(AG+1)^2+2},
\qquad uq=G+1,
\]
with
\[
\boxed{-\Delta_{\rm fib}=q^2N_0}.
\]
The first R8 gate should be the already-isolated N1 problem: classify the actual q>1 power-ten/divisor family according to the rational split criterion, **before** constructing any source chart.

Why this is the correct rearchitecture:

1. USSPAL is needed only on rationally split fibres; proving the actual split family empty bypasses N2 entirely.
2. \(N_0\) is exactly the discriminant that reappeared in the R7 allowed-ruling lift, so this is not a return to an unrelated old branch.
3. Keeping \(u,q\) and \(N_0\) retains the arithmetic semantics that pure Gamma10 projection erased.
4. It avoids paying the frozen transverse \(G\)-content before the split family is known to exist.
5. If split fibres survive, their classification itself becomes the genuinely new structural input required before any future chart or external migration may be reconsidered.

The preferred R8 decision tree is therefore:

\[
\boxed{
\text{actual }N_0\text{ split classification}
\to
\begin{cases}
\text{no split fibres} & \Rightarrow \text{q>1 N2 bypassed},\\
\text{classified split subfamily} & \Rightarrow \text{build a new interface only on that subfamily}.
\end{cases}
}
\]

## Exit discipline carried forward

```text
DO_NOT_CONTINUE_USSPAL_a_p_Hperp_E_OPTIMIZATION=TRUE
DO_NOT_CONTINUE_N4A_WITH_EXISTING_65_ELIMINATION=TRUE
DO_NOT_ACTIVATE_LAURENT_ESS=TRUE_UNTIL_NEW_SOURCE_IMAGE
NEW_STRUCTURAL_INPUT_REQUIRED_BEFORE_REOPENING_EITHER_INTERFACE=TRUE
```

---

STAGE_INPUTS=10_dual_interface_comparison.md; frozen Interface A and Interface B verdicts
NEW_PROVED_RESULTS=Unique main-interface decision PRIMARY_INTERFACE=NONE; R8 rearchitecture selected around N0 actual-split classification
NEW_REDUCTIONS=Future work is redirected from chart optimization/torus projection to the common mixed discriminant invariant
NEGATIVE_RESULTS=No valid HYBRID architecture; neither current interface remains active
REJECTED_ROUTES=USSPAL continuation; current N4-A continuation; simultaneous two-interface spending
EXTERNAL_SOURCES_USED=NONE_NEW
MIGRATION_CARDS_CREATED_OR_UPDATED=NONE
OUTPUT_DEPENDENCIES=12_remaining_new_mathematics.md; 13_R7_terminal_verdict.md; 14_R7-certificate.txt
UNRESOLVED_ITEMS=Actual q>1 split classification of N0; consequences for the remaining q>1 family
PHASE_STATUS=FROZEN
