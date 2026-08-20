# 75-R6 Phase VI — Remaining Internal Mathematics

R6 has separated what can be delegated to mature external theory from what remains genuinely source-specific.

---

# 1. Priority I — q>1 actual split classification

\[
\boxed{N1:\ (-1,N_0)=0?}
\]

The rational split criterion is explicit, but the actual power-ten family is not globally classified.

Possible closure modes:

- prove all surviving actual fibres nonsplit;
- isolate a smaller split subfamily;
- carry split fibres to N2.

```text
STATUS=OPEN_MAJOR
EXTERNAL_WEAPON_FOUND=NO
```

This remains a potentially high-leverage internal arithmetic test.

---

# 2. Priority II — q>1 source digit-height theorem

On a split fibre the current live theorem is now sharply localized.

## Positive form

\[
\boxed{
\text{ALLOWED_RULING_SOURCE_DENOMINATOR_THEOREM}
}
\]

Find an allowed-\(u\) source basepoint/ruling with denominator/height small enough that

\[
a_p\mathcal H_{\perp,\tau}j(u)^2
\]

falls below the radial clearance threshold.

R5 already reduced the local \(u\)-cost to

\[
j(u)^2=G^{o(1)}.
\]

The major unknown is the source-attached basepoint/denominator/transverse distortion.

## Negative dual

\[
\boxed{
\text{UNIFORM_SQUAREFREE_OR_SOURCE_CONTENT_HEIGHT_BARRIER}
}
\]

If every allowed ruling has intrinsically large source height, prove a lower-bound obstruction strong enough to contradict the digit shell or show the current P2 strategy cannot close.

```text
STATUS=OPEN_MAJOR_INTERNALLY_REDUCED
USSPAL_OPERATIONAL_RANK=1
```

---

# 3. Priority III — N4-A source-image algebraicization

R6 improves the formulation to:

\[
\boxed{
\text{construct an exact source-valid incidence over }
\Gamma_{10}
=
\langle(10,1),(1,10)\rangle\subset\mathbb G_m^2.
}
\]

Required output:

1. a fixed algebraic or exponential-polynomial object;
2. exact map from source solutions;
3. exact or controlled lift back to source solutions;
4. primitive/integral semantics retained;
5. branch degeneracies classified.

Only after this is done should Laurent/ESS be reactivated.

```text
STATUS=OPEN_MAJOR
EXTERNAL_THEOREM_AFTER_BRIDGE=LAURENT_FIRST / ESS_IF_LINEARIZED
```

This is a **reserve architecture program**, not the primary R7 gate.

---

# 4. q=1 remaining internal core

Without opening new internal subcases, the frozen q=1 core remains:

\[
\boxed{
\text{moving residue-constrained Pell/norm/support problem}
+
\text{exact power-ten/root incidence}.
}
\]

The field/order/discriminant is not fixed across the entire family, so no single fixed-torus theorem closes it.

```text
STATUS=OPEN_MAJOR
COMMON_WITH_QGT1=Gamma_10_BASE_ONLY
```

---

# 5. General-\(J\) applicability-only remainder

The source-valid reduced denominator \(u_0\) and unimodular envelope are known, but the full J2 conic/RCE machinery is not transported.

```text
STATUS=ORTHOGONAL
R7_MAIN_TASK=NO
```

External frameworks with plausible generality:

- MRR integral-model language;
- Laurent/ESS after exact source algebraicization;
- homogeneous-space/tori language if a uniform family emerges.

No general-J proof should be started from R6.

---

# 6. What is no longer internal work

Do **not** reopen as proof gates:

- moving finite packet / conductor packet classification;
- separate primitive modulo-\(u\) obstruction;
- fixed-data primitive counting on split conics;
- full integral Witt-frame construction;
- generic Cassels small-zero optimization as if it were the closure mechanism;
- general toric strong approximation for finite places.

Those have been retired, superseded, or shown nondecisive.

---

# 7. Recommended R7 internal focus

The unique main recommendation is:

\[
\boxed{
\textbf{Strategy C — USSPAL Remains Best Interface}
}
\]

with R7 centered on the source-specific denominator/basepoint survival test, not on another broad theorem search.

A disciplined R7 should begin by putting the two dual statements side by side:

\[
\boxed{
\text{construct a sufficiently cheap allowed ruling}
}
\]

versus

\[
\boxed{
\text{prove every allowed ruling is intrinsically too expensive}.
}
\]

The \(\Gamma_{10}\)/Laurent program remains a recorded reserve and should be reactivated only if a concrete N4-A elimination identity emerges from internal algebra.

---

STAGE_INPUTS=10_external_arsenal_map.md; 08_weapon_ranking.md; 09_net_complexity_audit.md; Phase-0 frozen internal gates
NEW_PROVED_RESULTS=No new theorem; remaining internal core isolated after external-theory exclusion
NEW_REDUCTIONS=N4 sharpened; R7 primary theorem reduced to positive/negative allowed-ruling source-height survival pair
REJECTED_ROUTES=Reopening retired packet/counting/Witt-frame gates; making broad N4 literature search the R7 main line without source algebraicization
EXTERNAL_SOURCES_USED=NONE_NEW
MIGRATION_CARDS_CREATED_OR_UPDATED=NONE_NEW
OUTPUT_DEPENDENCIES=12_R6_terminal_verdict.md; R7 prompt/design
UNRESOLVED_ITEMS=N1; N2 source denominator/basepoint; N4-A; q1 moving norm/support; later general-J
PHASE_STATUS=FROZEN
