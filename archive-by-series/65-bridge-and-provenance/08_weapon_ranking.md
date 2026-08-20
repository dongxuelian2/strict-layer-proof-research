# 75-R6 Phase V — External Arsenal Ranking

**Rule:** at most three active external weapons.  
**Result:** zero active external weapons; two A-grade reserves.

---

# 1. Operational baseline — not an external weapon

Before ranking external candidates, the current live proof interface is:

```text
INTERFACE=P2_USSPAL
STATUS=OPEN_REDUCED
ACTIVE_THEOREM_DEPENDENCY=NONE
ACTIVE_ENGINE=R20 source Veronese + R5 allowed-ruling transverse chart + R3 elementary P1
CURRENT_BLOCKER=allowed-ruling source denominator / low-height basepoint / chart distortion
LOCAL_u_COST=G^o(1)
```

This is the baseline every candidate must beat.

---

# 2. Priority score convention

The qualitative score

\[
\mathcal W
=
P_{\rm replacement}
+
P_{\rm persistence}
+
P_{\rm generality}
+
P_{\rm exact-power}
-
C_{\rm migration}
-
R_{\rm semantic}
\]

is translated to:

- `S`: immediately architecture-changing and legally applicable;
- `A`: high-payoff theorem family, but one bounded bridge away;
- `B`: useful standard persistent theory, no live-major-gate replacement;
- `C`: related framework with poor current fit;
- `REJECT`: superseded or clearly net-negative.

A-grade does **not** imply formal migration if Semantic Preservation fails.

---

# 3. Ranking

| Rank | Weapon | Target Blocks | Cross-Gate | Migration M-level | Generality | Net Complexity now | Final-Proof Persistence | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | WC-007 Laurent exponential-polynomial | D,F | CG1/2/3/4/5 architectural PASS | M0 — not applicable yet | GENERAL_J_PLAUSIBLE | NEGATIVE now / STRONGLY_POSITIVE after N4-A | VERY_HIGH | A — RESERVE |
| 2 | WC-006 ESS S-unit/Subspace | D,F | CG3/4/5 conditional | M0 | GENERAL_J_PLAUSIBLE | NEGATIVE now / STRONGLY_POSITIVE after exact group reduction | VERY_HIGH | A — RESERVE |
| 3 | WC-002 Wei–Xu multiplicative type | B,C | CG2/CG5 | M1–M2 standard skeleton only | STRICT_LAYER_FAMILY | NEUTRAL | HIGH | B — RESERVE |
| 4 | WC-001 CT–Xu integral homogeneous spaces | A | CG2/CG5 | M1–M2 standard skeleton only | STRICT_LAYER_FAMILY | NEUTRAL/NEGATIVE current | HIGH | B — RESERVE |
| 5 | WC-009 MRR dilatations | A,C | CG2/CG5 historical | already standard-language migrated | GENERAL_J_PLAUSIBLE | NEUTRAL current | HIGH | B — BACKGROUND |
| 6 | WC-003 Cao–Xu toric SA | B,C | background CG5 | M1 | STRICT_LAYER_FAMILY | NEGATIVE as P2 engine | MEDIUM | C |
| 7 | WC-005 Universal torsor/Cox | C | none current | M0 | STRICT_LAYER_FAMILY | NEGATIVE | LOW as distinct stack | C |
| 8 | WC-008 BGT DML | D,F | power-coordinate CG4 only | M0 | GENERAL_J_PLAUSIBLE | NEGATIVE vs Laurent | MEDIUM conditional | C |
| 9 | WC-004 Huang ternary counting | A,E | none current | existing MC-001 superseded | J2_ONLY current | NEGATIVE | LOW active | REJECT |

---

# 4. Active / reserve / rejected registry

## ACTIVE

```text
ACTIVE_EXTERNAL_WEAPONS=NONE
```

## HIGH-VALUE RESERVE

```text
RESERVE_1=WC-007_LAURENT_EXPONENTIAL_POLYNOMIAL
TRIGGER=N4_A_SOURCE_IMAGE_ALGEBRAICIZATION_PROVED

RESERVE_2=WC-006_ESS_S_UNIT
TRIGGER=EXACT_FINITE_RANK_MULTIPLICATIVE_GROUP_REDUCTION_PROVED
```

## STANDARD BACKGROUND RESERVE

```text
RESERVE_3=WC-002_WEI_XU_MULTIPLICATIVE_TYPE
RESERVE_4=WC-001_CTX_HOMOGENEOUS_SPACES
RESERVE_5=WC-009_MRR_DILATATIONS
```

## NONWEAPON / REJECT

```text
WC-003=RELATED_BUT_NONWEAPON
WC-004=REJECT_SUPERSEDED
WC-005=RELATED_BUT_NONWEAPON
WC-008=RELATED_BUT_NONWEAPON
```

---

# 5. Interface ranking including the current internal proof

For the **current q>1 split-fibre live gate**, the interfaces rank:

| Relative rank | Interface | Can start from proved current state? | Removes O-Q5? | New major bridge |
|---|---|---|---|---|
| 1 | P2/USSPAL source chart | YES | not yet, but directly attacks it | allowed-ruling denominator/basepoint |
| 2 | Laurent/N4 exact-power | NO | potentially bypasses it only after N4-A | N4-A exact source-image algebraicization |
| 3 | ESS S-unit | NO | potentially | stronger exact multiplicative-group reduction |
| 4 | uniform homogeneous-space/counting | partly | NO with audited theorems | quantitative source-height uniformity |
| 5 | norm-torus / Wei–Xu | partly | NO | moving family + digit-height |
| 6 | DML orbit | NO | NO | wrong orbit object / source lift |

Hence:

```text
USSPAL_RELATIVE_RANK=1_FOR_CURRENT_QGT1_LIVE_GATE
```

At the **whole-proof architecture** level, Laurent/N4 is the most valuable reserve because it is the only audited family naturally shared by q=1 and q>1 at the exact-power base. This does not make it operationally superior today.

---

# 6. Does R6 prove P2 noncanonical?

No.

R6 proves a subtler statement:

\[
\boxed{
P2\text{ is not the only conceptually natural interface,}
}
\]

because \(\Gamma_{10}\) / exponential-polynomial algebraicization is a real higher-level alternative.

But R6 does **not** prove:

\[
P2\_INTERFACE=NONCANONICAL.
\]

No external theorem currently bypasses the source denominator/distortion without first solving an equally hard source-image algebraicization problem.

Therefore:

```text
P2_INTERFACE=CANONICAL_ENOUGH_FOR_CURRENT_QGT1_GATE
P2_INTERFACE_DEMOTION_TO_RESERVE=NO
```

---

# 7. Phase-V verdict

```text
BEST_EXTERNAL_WEAPON=WC-007_LAURENT_EXPONENTIAL_POLYNOMIAL_RESERVE
BEST_WEAPON_STACK=NONE_ACTIVE
BEST_WEAPON_SCORE=A_RESERVE
ACTIVE_EXTERNAL_WEAPON_COUNT=0
USSPAL_RELATIVE_RANK=1_OPERATIONAL
```

---

STAGE_INPUTS=all WC sheets; RP-001/RP-002; power-ten audit; q1 unification audit; frozen USSPAL baseline
NEW_PROVED_RESULTS=No new mathematical theorem; completed uniform comparative ranking
NEW_REDUCTIONS=Separated operational rank from architecture-reserve rank; USSPAL rank 1 for current q>1 gate, Laurent rank 1 among external reserves
REJECTED_ROUTES=Promoting A-grade reserve despite semantic veto; treating background standard theory as active weapon
EXTERNAL_SOURCES_USED=Sources already frozen in candidate sheets
MIGRATION_CARDS_CREATED_OR_UPDATED=NONE
OUTPUT_DEPENDENCIES=09_net_complexity_audit.md; terminal strategy selection
UNRESOLVED_ITEMS=N2 source denominator theorem; N4-A source-image algebraicization; q1 closure
PHASE_STATUS=FROZEN
