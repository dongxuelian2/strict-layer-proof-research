# 75-R6 Phase VI — Main-Proof External Arsenal Map

**Terminal architecture purpose:** record what external mathematics is genuinely usable, what is only reserve, and what is retired/superseded.

---

# 1. Current proof architecture after the audit

\[
\boxed{
\text{Strict J2 source proof}
=
\text{internal exact source architecture}
+
\text{small set of standard external references/reserves},
}
\]

not

\[
\text{one imported theorem stack}.
\]

The current live q>1 engine remains:

\[
\boxed{
\text{R20 source semantic model}
+
\text{R20/R5 source Veronese/ruling chart}
+
\text{R3 elementary }\mathbf P^1\text{ approximation}.
}
\]

No external quantitative theorem is an active dependency of that engine.

---

# 2. Arsenal layer A — already successful standard-theory replacements

## A1 — Dilatation / affine-modification language

**Family:** Mayeux–Richarz–Romagny and related dilatation formalism.  
**Role:** explains the old finite packet/conductor rows as integral-model change rather than an independent arithmetic obstruction.

```text
STATUS=VALID_STANDARDIZATION
LIVE_GATE=NO
FINAL_PROOF_ROLE=MODEL_LANGUAGE / BACKGROUND
```

This was a real success of 75: it identified a large internally invented construction with a mature standard object.

---

# 3. Arsenal layer B — standard local-global theorem stacks

## B1 — CT–Xu integral homogeneous spaces

Use if the final manuscript needs a standard statement explaining Brauer–Manin/local-global behavior for a homogeneous-space integral model.

```text
STATUS=RESERVE_BACKGROUND
CURRENT_MAJOR_GATE_REMOVED=NO
```

## B2 — Wei–Xu multiplicative-type torsors

Use for fixed norm-torus integral-point criteria or explicit finite Brauer/Artin obstruction if a later branch is reduced to a fixed trivial torsor.

```text
STATUS=RESERVE_BACKGROUND
Q1_QGT1_COMMON_LANGUAGE=YES
CURRENT_UNIFICATION=NO
```

## B3 — Cao–Xu toric strong approximation

Qualitative finite-place strong approximation on smooth toric varieties.

```text
STATUS=RELATED_BACKGROUND
REAL_DIGIT_GATE=NOT_CONTROLLED
```

These are standard theorem stacks, but none is an active q>1 digit-height weapon.

---

# 4. Arsenal layer C — quantitative fallback / superseded engines

## C1 — MC-001 Huang ternary-cone counting

```text
STATUS=SUPERSEDED
ROLE=PROVENANCE_ONLY
```

Fixed-fibre projective approximation is cheaper through elementary \(\mathbf P^1\).

## C2 — MC-002 Cassels small integral zero

```text
STATUS=MIGRATED
ROLE=FALLBACK_BENCHMARK_ONLY
ACTIVE_DEPENDENCY=NO
```

It gives a legal generic splitting-height bound but is too expensive for the current clearance threshold.

---

# 5. Arsenal layer D — exact-power strategic reserves

## D1 — Laurent exponential-polynomial structure

This is the **best external reserve** found in R6.

It naturally treats several independent exponent variables and makes powers of ten intrinsic characters on \(\mathbb Z^r\).

Trigger for activation:

```text
TRIGGER=N4_A_SOURCE_IMAGE_ALGEBRAICIZATION_PROVED
```

Then it can potentially reorganize both q>1 and q=1 exact-power layers.

Current status:

```text
STATUS=A_GRADE_RESERVE
FORMAL_MIGRATION=NO
SEMANTIC_VETO=ACTIVE
```

## D2 — ESS \(S\)-unit / finite-rank multiplicative-group equations

Potentially stronger once the source equations are truly linear in finite-rank multiplicative-group variables.

Trigger:

```text
TRIGGER=EXACT_FINITE_RANK_MULTIPLICATIVE_GROUP_REDUCTION
```

Current status:

```text
STATUS=A_GRADE_RESERVE
FORMAL_MIGRATION=NO
```

---

# 6. Power-ten standard object

The exact powers are now canonically represented as

\[
\boxed{
\Gamma_{10}
=
\langle(10,1),(1,10)\rangle
\subset\mathbb G_m^2.
}
\]

Equivalently the exponent pair lives on the character lattice \(\mathbb Z^2\).

This is the correct high-level external interface for future N4 work.

The unsolved part is **not** “recognize powers of ten”; it is:

\[
\boxed{
\text{construct the exact source-valid algebraic/exponential-polynomial image over }\Gamma_{10}.
}
\]

---

# 7. q=1 / q>1 common architecture

The audit found:

\[
\boxed{
\text{common norm-torus language}
}
\]

and, more importantly,

\[
\boxed{
\text{common exact-power base }\Gamma_{10}.
}
\]

It did not find a single fixed torsor/homogeneous space/integral family whose theorem closes both branches.

```text
Q1_QGT1_COMMON_BASE=Gamma_10
Q1_QGT1_SINGLE_EXTERNAL_WEAPON=NO
```

---

# 8. Active-dependency ledger

```text
ACTIVE_EXTERNAL_THEOREM_DEPENDENCIES_FOR_P2=NONE
ACTIVE_NEW_R6_WEAPONS=NONE

BACKGROUND_STANDARD_THEORY=
  MRR_DILATATION_FORMALISM
  CTX_INTEGRAL_HOMOGENEOUS_SPACES
  WEI_XU_MULTIPLICATIVE_TYPE
  CAO_XU_TORIC_SA

FALLBACK=
  MC-002_CASSELS

SUPERSEDED=
  MC-001_HUANG

HIGH_VALUE_RESERVE=
  WC-007_LAURENT
  WC-006_ESS
```

---

# 9. What 75-R6 actually achieved

R6 does **not** add another local lemma. It resolves an architecture question:

1. no currently verified mature external theorem bypasses the source denominator/digit problem at positive net complexity;
2. the local-global/torsor/counting theories mostly target parts already solved internally;
3. exact powers of ten *do* have a canonical external arithmetic object, \(\Gamma_{10}\);
4. the real N4 bridge is source-image algebraicization, not theorem discovery;
5. therefore returning to P2 is not sunk-cost behavior: it survives a whole-proof external comparison.

---

STAGE_INPUTS=all frozen Phase 0–V artifacts; candidate sheets; replacement stress tests; power-ten and q1 audits
NEW_PROVED_RESULTS=External-arsenal architecture finalized; no new source theorem
NEW_REDUCTIONS=External theory classified into standardization/background/fallback/superseded/exact-power reserve layers
REJECTED_ROUTES=Any active promotion rejected in Phase III; power-ten rearchitecture before N4-A; q1/q>1 forced torsor unification
EXTERNAL_SOURCES_USED=All verified primary sources recorded in WC sheets
MIGRATION_CARDS_CREATED_OR_UPDATED=MC-001 R6 status reaffirmed; MC-002 R6 status reaffirmed; no new card
OUTPUT_DEPENDENCIES=11_remaining_internal_mathematics.md; 12_R6_terminal_verdict.md; future R7
UNRESOLVED_ITEMS=N1,N2,N4-A,q1 closure,general-J transport
PHASE_STATUS=FROZEN
