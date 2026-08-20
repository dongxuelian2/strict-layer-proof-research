# 7.15 Legacy Migration Alias Quarantine Ledger
## 75 历史 Migration Card / Stack 身份隔离与 authority 修复

**状态：** `FROZEN_FOR_85_IMPORT`  
**目的：** 消除 75 历史档案中的 Migration Card 编号复用、非卡文件占用 MC namespace、以及旧 stack 看似 canonical 的 authority 风险。

---

# 1. 根问题

75 历史档案中的裸编号：

```text
MC-001
MC-002
MC-003
...
```

并非从 R1 起就是 immutable theorem identity。

因此从 7.15 起：

\[
\boxed{
\texttt{BARE LEGACY MC ID IS NOT A STABLE THEOREM ID}
}
\]

任何 theorem identity 至少必须通过：

```text
(round, theorem/source identity, canonical filename, frozen hash if available)
```

解析。

---

# 2. Canonical 75 terminal Migration Card registry

以下 registry 以 **75-R8 certificate** 为终局 canonical identity。

## CANONICAL-MC-001

```text
ID=MC-001
THEOREM=HUANG_TERNARY_CONE_PRIMITIVE_LOCAL_COUNTING
CURRENT_STATUS=SUPERSEDED
ACTIVE_DEPENDENCY=NO
CANONICAL_R8_FILE=75_MIGRATIONS/MC-001_R8_Update.md
R8_SHA256=e9e369fbdfe62f3075cc4b31afad24f0a4be11f2956a25727eb78f0dde28cdf8
```

## CANONICAL-MC-002

```text
ID=MC-002
THEOREM=CASSELS_SMALL_INTEGRAL_ZERO
CURRENT_STATUS=MIGRATED_FALLBACK
ACTIVE_DEPENDENCY=NO
CANONICAL_R8_FILE=75_MIGRATIONS/MC-002_R8_Update.md
R8_SHA256=3db197f722d7402cdb68fe1729e037b46205bf0379d7c5449d653ab983fb9782
```

## CANONICAL-MC-003

```text
ID=MC-003
THEOREM=LAURENT_EXPONENTIAL_DIOPHANTINE_N0
CURRENT_STATUS=REJECTED
PROMOTED=NO
ACTIVE_DEPENDENCY=NO
ROLE=NEGATIVE_APPLICABILITY_RECORD
CANONICAL_R8_FILE=75_MIGRATIONS/MC-003_Laurent_N0_R8.md
R8_SHA256=af79235a3272c132fb946b3f6a693b0694cf4c7b2c698929d47e900459aa0ffb
```

## CANONICAL-MC-004

```text
ID=MC-004
THEOREM=ESS_SUNIT_N0
CURRENT_STATUS=REJECTED
PROMOTED=NO
ACTIVE_DEPENDENCY=NO
ROLE=NEGATIVE_APPLICABILITY_RECORD
CANONICAL_R8_FILE=75_MIGRATIONS/MC-004_ESS_N0_R8.md
R8_SHA256=62325932f8a6aa6f18ed42cf601d1f50850d546ee930dce171a708630e17a571
```

---

# 3. Canonical terminal migration stack

```text
CANONICAL_STACK=75_MIGRATIONS/migration_stack_main_proof_R8.md
R8_SHA256=dd66b151f03cd69965df90adf933d90b93aa1ecb48cf0511f97d11bd57821ed1
STATUS=CURRENT_75_TERMINAL_AUTHORITY
```

---

# 4. Legacy aliases — quarantine

## LEGACY-R2-MC-002

历史 R2 stack 使用：

```text
MC-002=CAO_XU_TORIC_STRONG_APPROXIMATION
```

处理：

```text
QUARANTINE_ALIAS=LEGACY_R2_MC-002_CAO_XU
STATUS=ARCHIVE_ONLY
CANONICAL_MC_ID=NONE
FORBIDDEN_AS_CURRENT_MC-002=TRUE
```

任何看到旧 `MC-002 Cao–Xu` 的流程必须解释为：

> R2 历史命名，而非 R8 canonical MC-002。

---

## LEGACY-R2-MC-003

历史 R2 stack 使用：

```text
MC-003=KELMER_YU_SHRINKING_SECTOR
```

处理：

```text
QUARANTINE_ALIAS=LEGACY_R2_MC-003_KELMER_YU
STATUS=ARCHIVE_ONLY
CANONICAL_MC_ID=NONE
FORBIDDEN_AS_CURRENT_MC-003=TRUE
```

---

# 5. MC-003 namespace 中的 non-card 文件

## R5 note

```text
FILE=75_MIGRATIONS/MC-003_rejected_candidate_note.md
TYPE=REGISTRY_OR_REJECTION_NOTE
IS_MIGRATION_CARD=NO
CANONICAL_MC_ID=NONE
STATUS=ARCHIVE_ONLY
```

## R6 note

```text
FILE=75_MIGRATIONS/MC-003_R6_registry_note.md
TYPE=REGISTRY_NOTE
IS_MIGRATION_CARD=NO
CANONICAL_MC_ID=NONE
STATUS=ARCHIVE_ONLY
```

它们不能用于证明：

```text
MC-003 existed as a canonical theorem card before R8
```

---

# 6. Legacy stack quarantine

## Old stack

```text
FILE=migration_stack_P2.md
ROUND=75-R2
STATUS=LEGACY_STRATEGIC_SNAPSHOT
CURRENT_AUTHORITY=NO
```

它包含的历史信息（例如 `MC-002=Cao-Xu`, `MC-003=Kelmer-Yu`, `P2=M5_B`）只能用于 provenance。

禁止：

```text
USE_OLD_STACK_AS_CURRENT_75_STATE=TRUE
```

正确状态：

```text
USE_OLD_STACK_AS_CURRENT_75_STATE=FALSE
```

---

# 7. Authority resolution algorithm

当 85 / Agent / 人工检索遇到 Migration Card 引用时：

### Step 1
若有 R8 canonical filename + hash，直接按 R8 registry 解释。

### Step 2
若只有裸 `MC-00X`，检查 round / surrounding theorem name。

### Step 3
如果来源为 R2/R3/R5/R6 且 identity 与 R8 registry 冲突，标：

```text
LEGACY_ALIAS
```

不得覆盖 canonical identity。

### Step 4
如果文件名包含：

```text
registry_note
rejected_candidate_note
candidate_note
```

不得仅凭 `MC-003` prefix 视为 Migration Card。

### Step 5
若 strategic status 冲突：

```text
7.15 certificate
> R8 terminal/certificate
> R7 terminal
> earlier terminal strategic recommendation
```

但数学 lemma 的真假仍按 lemma 本身及后续是否被反证判断。

---

# 8. R8 terminal authority anchors

```text
R8_TERMINAL_FILE=75_R8/13_R8_terminal_verdict.md
R8_TERMINAL_SHA256=403c7fb8d4ddfb68fc943d7187617f91a43c5cd79e7fef3db181bfd0601b68eb

R8_REMAINING_FILE=75_R8/12_remaining_internal_mathematics.md
R8_REMAINING_SHA256=64a4bbafca678513e2c9eb1c56aa061fa9072e8019b362a177451ed89ab73dbf

R8_STACK_FILE=75_MIGRATIONS/migration_stack_main_proof_R8.md
R8_STACK_SHA256=dd66b151f03cd69965df90adf933d90b93aa1ecb48cf0511f97d11bd57821ed1
```

---

# 9. 85 import policy

```text
ALLOW_DIRECT_IMPORT:
  CANONICAL_R8_MC_REGISTRY
  R8_TERMINAL_VERDICT
  R8_CERTIFICATE
  R8_REMAINING_INTERNAL_MATHEMATICS
  7.15_INHERITANCE_CERTIFICATE

ALLOW_PROVENANCE_ONLY:
  migration_stack_P2.md
  LEGACY_R2_MC-002_CAO_XU
  LEGACY_R2_MC-003_KELMER_YU
  MC-003_rejected_candidate_note
  MC-003_R6_registry_note

FORBID:
  resolving theorem identity from bare legacy MC number alone
  treating a rejected card as promoted theorem
  treating a registry note as a Migration Card
  treating an old strategic stack as current authority
```

---

# 10. Final quarantine status

```text
LEGACY_MIGRATION_NAMESPACE_STATUS=QUARANTINED
CURRENT_MC_NAMESPACE_STATUS=R8_CANONICAL
STALE_STACK_AUTHORITY_STATUS=DISABLED
85_ARCHIVE_IMPORT_SAFE=YES_UNDER_THIS_LEDGER
```
