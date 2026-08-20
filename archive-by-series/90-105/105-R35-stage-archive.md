# 105-R35 Stage Archive — Terminal Predicate Extinction × MASTER Cutoff Domination × Source-First Search

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R35  
**Campaign position:** 最后十五轮终局总攻第 10 轮  
**Status:** FROZEN / ARCHIVED

# Executive verdict

R35 does **not** prove Strict-A1 extinction and does **not** find a full witness. Its strongest valid terminal verdict is:

```text
R35_TERMINAL_ATTACK_FAILED
R35_TERMINAL_PREDICATE_SATURATION_CERTIFICATE=PROVED
```

The round nevertheless deletes two important ambiguities.

First, the MASTER cutoff is exactly floor-free:
\[
\boxed{Q_{master}<Q_-\iff Q_-b_1D\ge Q_0.}
\]
Second, on \(Q_-=1\), R33's \(0<b_1D<Q_0\) forces \(Q_{master}\ge1\). Therefore MASTER cutoff can never kill an already denominator-admissible q=1 candidate. The unit branch is a pure source-existence decision after the denominator/master gates.

The exact frozen replay also shows a gate complementarity:
- seven q1 MASTER hits: denominator/master side nonempty, source room empty;
- R8 A/B/C/E: source-completed base profiles but source radial fibre empty;
- historical R29 support survivor: raw U=1 source room nonempty, denominator/master-truncated window empty.

No genuine architecture in the frozen/replayed set makes both terminal sides nonempty. But there is no global theorem that this cannot happen. Hence the final rectangle cannot be declared covered or empty globally.

# Part I — FILE / HASH AUDIT
Historical inputs were retrieved as File Library references. Their ledger hashes are recorded in `105-R35-input-hash-audit.csv` with verification mode `LEDGER-CROSSCHECK`; no historical bytewise rehash is claimed. Every R35 output in the manifest is hashed from local runtime bytes.

# Part II — TERMINAL PREDICATE RECOVERY
See `105-R35-terminal-predicate-exact-system.md`.

The current exact predicate is
\[
\exists U\in\mathcal U_0,\quad \exists q\in[Q_-,Q_*],\quad(q,FU)=1,
\qquad Q_*=\min(Q_+,Q_{master}).
\]
R35 also freezes the naming correction: the literal R30 N30 used Q+ and must be master-refined after R33. The master-refined count is exactly equivalent to TP.

# Part III — MASTER CUTOFF DOMINATION
See `105-R35-master-cutoff-domination.md`.

Universal source-implies-cutoff extinction is neither proved nor falsified. No genuine source-complete counterexample exists in the frozen corpus. However, the unit-chamber non-kill lemma proves the cutoff is not an independent unit killer.

# Part IV — SOURCE-FIRST SEARCH
See `105-R35-source-first-witness-search.md` and registries.

No genuine source-complete + denominator-nonempty architecture was found. This is not promoted to a global theorem.

# Part V — TERMINAL RECTANGLE
See `105-R35-terminal-rectangle-analysis.md`.

No architecture-uniform absolute bound for \(|Q|\), \(|Q_F|\), or \(|U_0|\) is proved. No terminal zero/one theorem is proved.

# Part VI — COPRIME COVER / EXISTENCE
See `105-R35-coprime-cover-analysis.md`.

No genuine nonempty rectangle was reached in the exact replay, so neither a global prime cover nor a genuine coprime pair can be certified.

# Part VII — ACTIVE N30>0 HUNT
No genuine master-refined positive point found.

# Part VIII — FULL RECONSTRUCTION AUDIT
See `105-R35-full-reconstruction-audit.md`. R26 documentary iff audit remains intact; no positive numerical reconstruction was triggered and no iff bug was found.

# Part IX — GLOBAL TERMINAL RESULT

## Fifteen required answers
1. **Exact TP:** \(\exists U\in U_0,\exists q\in[Q_-,Q_*],(q,FU)=1\), with the historical-N30 naming qualification above.
2. **Qstar:** \(\min(Q_+,Q_{master})\), \(Q_{master}=\lfloor(Q_0-1)/(b_1D)\rfloor\).
3. **U0:** exact digit interval + frozen periodic residue + \((U,V_0)=1\) + SrcComp, with decorated R8 branch corrections.
4. **Source⇒cutoff?** NOT PROVED, NOT FALSIFIED.
5. **First genuine counterexample?** NONE FOUND.
6. **Source lower bound on b1D?** No source-dependent scale bound proved; current global arithmetic bound is \(b_1D\ge1\), while R33 gives \(b_1D<Q_0\).
7. **Maximum terminal denominator integers?** Per architecture \(\max(0,Q_*-Q_-+1)\); inherited bound \(\le9Q_-\) when nonempty. No absolute global constant proved.
8. **Maximum F-coprime fibre?** At most terminal window size; no smaller global bound proved.
9. **Maximum source fibre?** At most \(U_{hi}-U_{lo}+1\); no absolute global constant proved.
10. **Zero/one theorem?** NO for terminal source/q fibres.
11. **U=1 terminal survivor?** NONE KNOWN; NOT GLOBALLY EXCLUDED.
12. **q=1 terminal survivor?** NONE KNOWN; NOT GLOBALLY EXCLUDED. MASTER cannot kill it once denominator-admissible.
13. **Genuine N30>0?** NO.
14. **R26 reverse reconstruction?** Documentary audit PASS; positive-instance run NOT TRIGGERED.
15. **Endgame diagnosis:** neither “extinction theorem one algebraic step away” nor existing witness is justified. The single unresolved incidence is simultaneous nonemptiness of completed source fibre and master-truncated denominator window; if achieved, the remaining finite rectangle is explicit.

# Terminal machine block
```text
R35_TERMINAL_ATTACK_FAILED
R35_TERMINAL_PREDICATE_SATURATION_CERTIFICATE=PROVED
STRICT_A1_UNLIFTABILITY_PROVED=NO
GLOBAL_N30_ZERO_THEOREM=NOT_PROVED
SOURCE_IMPLIES_MASTER_CUTOFF_EXTINCTION=NOT_PROVED_NOT_FALSIFIED
TERMINAL_COPRIME_RECTANGLE_EXTINCTION=NOT_PROVED
GLOBAL_TERMINAL_FINITE_CLASSIFICATION=NO
N30_POSITIVE_GENUINE_POINT_FOUND=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
QMASTER_LT_QMINUS_IFF_QMINUS_B1D_GE_Q0=PROVED
UNIT_CHAMBER_MASTER_CUTOFF_NONKILL=PROVED
R26_IFF_ARCHITECTURE_BUG_FOUND=NO
```
