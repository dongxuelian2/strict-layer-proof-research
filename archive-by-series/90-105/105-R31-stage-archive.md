# 105-R31 Stage Archive — q=1 Forced-Scale Assault × Minimal-q Descent × N30 Positive Hunt × Strict-A1 Reconstruction Audit

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R31  
**Campaign position:** 最后十五轮终局总攻第 6 轮  
**Status:** FROZEN / ARCHIVED

# Executive Verdict

R31 did **not** prove global Strict-\(A_1\) extinction and did not find a full witness. It also did not honestly force every N30-positive survivor down to q=1.

It did, however, open the R30 count at the two places where it is actually rigid:

1. **Unit chamber:**
   \[
   q=1\iff Z_-\le\Lambda\le Z_+,
   \]
   and on any legal architecture with \(Q_-=1\le Q_+\),
   \[
   N_{30}>0\iff\mathcal U_0\ne\varnothing.
   \]
   Prime-cover arithmetic disappears completely.
2. **Minimal nonunit chamber:** for the minimal admissible residual denominator,
   \[
   q/p<Q_-\quad\forall p\mid q,
   \]
   hence a composite minimal q must satisfy
   \[
   q<Q_-^2.
   \]
   Therefore minimal q is **prime or in a finite quadratic strip**.
3. The exact q-window has universal multiplicative width
   \[
   Q_+<10Q_-.
   \]
4. In the complete R28 E27 corpus through \(Q_0\le3000\), exactly seven raw-TC1 rows admit q=1 forced scale; every one has empty source digit room. This gives a rigorous bounded q1 source-collision theorem.
5. New architecture-first searches based on the q=1/U-prescribed TC1×sphere quadratic tested over 3.9 million additional exact configurations and found zero integer TC1-conic solutions in the stated boxes.

The strongest honest terminal verdict is therefore

```text
R31_TERMINAL_ATTACK_FAILED
R31_N30_POSITIVE_SATURATION_CERTIFICATE=PROVED
```

with a strictly smaller remaining object: `ARCHITECTURE_UNIFORM_LOWER_EDGE_COPRIME_SUCCESSOR`, split into unit / prime / finite-composite branches.

---

# Part I — FILE / HASH AUDIT

## I.1 Frozen inputs actually recovered

The following authoritative inputs were read from File Library references. Raw bytes were not mounted in the active runtime, so verification is **LEDGER-CROSSCHECK**, not a new cryptographic rehash.

| file | frozen SHA-256 | method | status |
|---|---|---|---|
| `105-R26-stage-archive.md` | `41f4e2aad7720862a98349d61d22c482b7f5045b6c54bfea56651d4032d97680` | LEDGER-CROSSCHECK | FROZEN |
| `105-R30-stage-archive.md` | `ce9c0be6cf52201ef99605ea4a67b414fc14327554b51a0c58d5000f84b25ade` | LEDGER-CROSSCHECK | FROZEN |
| `105-R30-TC3-TC4-exact-definitions.md` | `4fb3b68afbd9a95b7ff8067f5a93c78d1416f82b7c4b606912fb344163fc18f3` | LEDGER-CROSSCHECK | FROZEN |
| `105-R30-q-elimination-derivation.md` | `ca536b3764ef49d593019ad7c24b3874f6b2f3b10d0f42af8218b3a966722f6e` | LEDGER-CROSSCHECK | FROZEN |
| `105-R30-Q-SUCCESSOR-SATURATION-CERTIFICATE.md` | `4137beba338eba099012337ac2e2473e2d865bb706c3a05a336783c0ea7d3dcd` | LEDGER-CROSSCHECK | FROZEN |
| `105-R30-execution.log` | `854a82ebd5b30611228ea771e992e82ff5a943be21457ab450dc98f47fba8afb` | LEDGER-CROSSCHECK | FROZEN |
| `105-R28-TC1-hit-registry.csv` | `0b325db25e2305022ac0aaae92c70cc504210f2ce5fe1ce003c01a0318f2df3e` | LEDGER-CROSSCHECK | FROZEN |
| `105-R28-stage-archive.md` | `ee1bf90f78f4317eefc3e3c341c3f15828e7e69724e2b5fa393765ab106f14a1` | LEDGER-CROSSCHECK | FROZEN |

The R30 manifest itself explicitly records the same old-artifact limitation. R31 does not pretend otherwise.

## I.2 Additional theorem sources recovered

- `105_R8_Common_U_Integer_Source_Fibre.md` for the exact rank-one source interval and canonical successor;
- `105_R14_Positive_Radial_Core_Lift_Fibre.md` for the reverse reconstruction variables and Smith/master/tail predicates;
- R28 bounded hit and fixed-architecture registries for q=1 autopsy.

## I.3 R31 generated artifacts

Required artifacts are generated under this directory. All new bytes are hashed locally after generation. No extinction or full-witness certificate is generated because neither result was proved.

---

# Part II — R30 N30 RECOVERY

For one fixed legal post-support architecture,

\[
g_0=(u_0AW,P_1),\quad \mu=g_1^*/g_0,\quad R_1=P_1/g_1^*,
\]

\[
\lambda_z=\frac{10^{n_3}}{(10^{n_3},W(Q_0-P_3))},
\qquad
\Lambda=\operatorname{lcm}(\mu,\lambda_z),
\]

\[
F=\operatorname{rad}(R_1C_2C_3).
\]

The denominator chamber is

\[
z=\Lambda q,\qquad(q,F)=1,
\]

with the exact \(Z\)- and q-windows recorded in `105-R31-q1-forced-scale-derivation.md`.

The q-independent source set is the completed periodic source selector inside the exact block interval, with \((U,V_0)=1\), where \(V_0=\Lambda u_0AW\).

R30's exact fusion remains

\[
N_{30}(\mathfrak a)=\sum_{U\in\mathcal U_0}
\#\{q\in[Q_-,Q_+]:(q,FU)=1\},
\]

\[
TC3\wedge TC4\iff N_{30}>0.
\]

No new free q coordinate is introduced in R31.

---

# Part III — q=1 FORCED SCALE

R31 proves

\[
\boxed{q=1\text{ TC3-admissible}\iff Z_-\le\Lambda\le Z_+.}
\]

The exact cleared conditions are

\[
10^{m_2-1}\le A\Lambda\le10^{m_2}-1,
\qquad
10^{m_3-1}\le W\Lambda\le10^{m_3}-1.
\]

A second new exact theorem is

\[
\boxed{Q_+<10Q_-}
\]

on every nonempty q-window. Thus the unit chamber has \(1\le Q_+\le9\).

Most importantly, because q=1 is automatically coprime to FU,

\[
\boxed{Q_-=1\le Q_+\Longrightarrow(N_{30}>0\iff\mathcal U_0\ne\varnothing).}
\]

This is the true terminal simplification of the q=1 branch.

---

# Part IV — SOURCE FIBRE OPENING

On regular completed strata,

\[
L=\max(10^{n_2-1}/C_2,10^{n_3-1}/C_3),
\]

\[
R=\min(10^{n_2}/C_2,10^{n_3}/C_3),
\]

with exact integer bounds \(U_{lo},U_{hi}\) and finite native residue selector as fully written in the q1 derivation companion.

Generic R8 completed strata have source step \(h_U=1\); special historical source-chart progression is chart-local and is not identified with residual q=1.

For U=1 the exact digit condition is simply that C2 and C3 themselves occupy their prescribed numerator digit blocks, plus the frozen source-completed predicate.

---

# Part V — q=1,U=1 ATTACK

R31 derives the exact architecture-first equation

\[
F_{11}(Q_0)=
(B^2-L^2)Q_0^2-2BCQ_0+C^2+L^2(P_2^2+P_3^2)=0,
\]

with explicit L,B,C in `105-R31-q1-forced-scale-derivation.md`.

This allows reverse generation from digit blocks instead of scanning primitive sphere packets first.

The new searches report:

- `Q1_U1_TO_U3_L8_K1`: 350,723 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.
- `Q1_U1_L8_K2`: 3,230,116 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.
- `SMALL_Q_U1_L6_K1`: 380,912 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.

No integer TC1-conic solution was found in these exact finite boxes. This is not a global q1 extinction theorem.

The complete R28 height corpus gives the stronger bounded fact: exactly 7 raw-TC1 q1 hits exist through \(Q_0\le3000\), and every one has \(U_{lo}=1>U_{hi}=0\). Hence

```text
Q1_FORCED_SCALE_SOURCE_COLLISION_Q0_LE_3000=PROVED
```

---

# Part VI — MINIMAL-q DESCENT

For a minimal admissible q and every p dividing it,

\[
\boxed{q/p<Q_-.}
\]

Hence

\[
\boxed{Q_-\le q<p_{\min}(q)Q_-.}
\]

If q is composite,

\[
\boxed{q<Q_-^2.}
\]

Thus a minimal survivor is prime or in an explicit finite quadratic strip. This is the exact limit of prime stripping reached in R31.

It is not legitimate to sign `MINIMAL_Q_DESCENT_TO_ONE=YES`: a prime q has no nontrivial prime quotient inside the positive integers, and the lower edge itself does not move under the frozen geometry.

---

# Part VII — ACTIVE COUNTEREXAMPLE SEARCH

The machine campaign was explicitly falsification-oriented:

1. recover all q1 hits in the complete R28 bounded raw-TC1 registry;
2. identify their first q-independent source/support death;
3. reverse-generate q1/U-prescribed architectures by exact TC1×sphere quadratic;
4. include a small-q lane q in {1,2,3,5,7}.

Results are machine-readable in the q1, N30-positive and exceptional-branch registries. No genuine post-support N30-positive architecture was found.

---

# Part VIII — FULL RECONSTRUCTION AUDIT

No N30-positive point existed to trigger a full numerical reverse reconstruction.

The frozen theorem chain was nevertheless audited:

\[
\mathcal C_{26}=1\iff\text{full Strict-}A_1\text{ lift},
\]

and R30 replaces only TC3×TC4 by an exact equivalent N30 predicate. R14's reverse map retains exponent chart, denominator windows, primitive sphere, D/T positivity, master, tail, Smith reconstruction, g1 firewall, frozen cell and PSDG regression.

Therefore

```text
R26_IFF_DOCUMENTARY_AUDIT=PASS
HIDDEN_TC5_FOUND=NO
POSITIVE_INSTANCE_RECONSTRUCTION=NOT_TRIGGERED
```

No proof-architecture bug was detected.

---

# Part IX — GLOBAL RESULT

## IX.1 Proved

```text
Q1_EXACT_FORCED_SCALE_EQUIVALENCE=PROVED
UNIT_CHAMBER_N30_IFF_U0_NONEMPTY=PROVED
Q_WINDOW_MULTIPLICATIVE_BOUND_LT_10=PROVED
PRIME_STRIPPING_LOWER_EDGE_RIGIDITY=PROVED
MINIMAL_Q_PRIME_OR_QUADRATIC_STRIP=PROVED
UNIT_PRIME_FINITE_COMPOSITE_TRICHOTOMY=PROVED
Q1_FORCED_SCALE_SOURCE_COLLISION_Q0_LE_3000=PROVED
R26_IFF_DOCUMENTARY_AUDIT=PASS
```

## IX.2 Not proved / not found

```text
Q1_FORCED_SCALE_EXTINCTION_GLOBAL=NOT_PROVED_NOT_FALSIFIED
MINIMAL_Q_DESCENT_TO_ONE=NOT_PROVED
GLOBAL_N30_ZERO_THEOREM=NOT_PROVED
STRICT_A1_UNLIFTABILITY_PROVED=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
GENUINE_N30_POSITIVE_FOUND=NO
```

## IX.3 Twelve mandatory answers

1. **q=1 denominator condition:** exactly \(Z_-\le\Lambda\le Z_+\), equivalently the two denominator blocks \(A\Lambda,W\Lambda\) have the prescribed digit lengths.
2. **Why equivalent:** direct ceiling/floor equivalence for positive integral \(Z_\pm,\Lambda\).
3. **q-free source condition:** finite source interval + fixed native residue selector + completed-source predicates + \((U,V_0)=1\), with canonical successor formula fully recovered.
4. **When U=1 is legal:** C2,C3 lie in their prescribed digit blocks and the fixed chart-native completed predicate accepts U=1; gcd conditions are automatic.
5. **Genuine q=1 architecture?** No genuine post-support one found; global existence remains unresolved. Seven bounded raw-TC1 q1 rows all die at TC2/source room.
6. **If q1 and U0 exists, N30 positive?** Yes, automatically and exactly.
7. **R26 iff reconstruction complete?** Documentary audit passes; no positive-instance reconstruction was triggered.
8. **Shortest q1 death mechanism?** In the complete \(Q_0\le3000\) q1 raw-TC1 corpus it is source-room emptiness. No global symbolic version is yet proved.
9. **Can minimal q descend?** Every prime stripping exits below Q-. Descent all the way to 1 is not proved.
10. **Prime / prime power / bounded?** Minimal q is prime or composite below \(Q_-^2\). Prime power is not forced; no architecture-independent absolute C is proved.
11. **Any full C26 packet?** None known/found in R31.
12. **Smallest remaining mathematical object:** the architecture-uniform lower-edge coprime successor, split into unit, prime, and finite composite branches.

---

# TERMINAL VERDICT

```text
R31_TERMINAL_ATTACK_FAILED
R31_N30_POSITIVE_SATURATION_CERTIFICATE=PROVED

Q1_GLOBAL_TRUTH=UNDECIDED
Q1_GENUINE_POST_SUPPORT_WITNESS_FOUND=NO
U0_FREEDOM=FINITE_PERIODIC_SOURCE_SUCCESSOR
MINIMAL_Q_DESCENT_TO_ONE=NOT_PROVED
MINIMAL_Q_PRIME_OR_QUADRATIC_STRIP=PROVED
GENUINE_N30_POSITIVE_FOUND=NO
R26_IFF_AUDIT=PASS_DOCUMENTARY

MINIMAL_REMAINING_OBJECT=ARCHITECTURE_UNIFORM_LOWER_EDGE_COPRIME_SUCCESSOR__UNIT_PRIME_FINITE_COMPOSITE_SPLIT
```

R31 therefore does not end 105, but it does prevent the next round from returning to generic q-floor arithmetic: the only honest nonunit obstruction left is prime support in the real q-window plus the finite composite strip; the unit chamber is purely a source-fibre problem.
