# 105-R32 Stage Archive — Unit-Chamber Digit-Level Terminal Assault

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R32  
**Campaign position:** 最后十五轮终局总攻第 7 轮  
**Status:** FROZEN / ARCHIVED

# Executive Verdict

R32 did **not** prove global q=1 extinction, global \(N_{30}=0\), or Strict-\(A_1\)
unliftability, and it did not find a full witness.

It did produce a genuine variable deletion and a sharp negative architecture
result:

\[
\boxed{
(m_3-m_2)-(n_3-n_2)=2g+k
}
\]

and, in q=1,

\[
\boxed{
m_2=\operatorname{dig}(A\Lambda),\quad
m_3=\operatorname{dig}(W\Lambda),\quad
g=m_3-n_3,\quad
k=n_2-m_2-g.
}
\]

So once the source digit pair is fixed, the complete denominator/exponent scale
is deterministic. This is strictly stronger than R31's forced-scale statement.

The hoped-for pure digit theorem

\[
J_2\cap J_3\ne\varnothing\Longrightarrow I_2\cap I_3=\varnothing
\]

does **not** follow from the digit/exponent/carrier identities. The exact
elimination leaves the packet invariant

\[
\boxed{
\mathfrak R=\frac{P_2}{10^{2g+k}P_3}
}
\]

with only

\[
10^{-2}<\mathfrak R<10^2.
\]

An exact structural countermodel
\((P_1,P_2,P_3,Q_0)=(50,10,1,51)\) passes primitive sphere, q1 denominator
digits, source room, shape/Smith/tail, and positivity, but fails TC1/master with
residual \(-4444\). Hence a global q1 kill, if true, must use TC1/master (or an
equivalent stronger frozen relation); digit intersection alone is saturated.

The complete R28 \(Q_0\le3000\) q1 raw-TC1 autopsy is stronger than R31's count:
all seven have \(U_{\rm lo}=1,U_{\rm hi}=0\), all seven are killed by Face 3
alone, five are also killed by Face 2, and every gap is exactly one.

The strongest honest terminal verdict is therefore

```text
R32_TERMINAL_ATTACK_FAILED
R32_UNIT_CHAMBER_SATURATION_CERTIFICATE=PROVED
```

with the unit first-failure sharpened to

```text
MASTER_CONDITIONED_UNIT_SOURCE_ROOM_COLLISION
```

rather than generic q arithmetic.

# Part I — FILE / HASH AUDIT

All prior frozen inputs were File Library references, not raw mounted bytes.
Therefore every old digest below is **LEDGER-CROSSCHECK**, never a claimed new
bytewise hash. See `105-R32-input-hash-audit.csv`.

Key authoritative digests include:

- R31 stage: `4bcbe12605a46e69051b0bff435aa88637411bbb63ac9d644f7671254884804d`
- R31 q1 derivation: `5dce481eb346bd2e67f4f46129248d1bfb9dc9f450c81f23ae4b033b7a7483ad`
- R30 TC3/TC4 definitions: `4fb3b68afbd9a95b7ff8067f5a93c78d1416f82b7c4b606912fb344163fc18f3`
- R30 q elimination: `ca536b3764ef49d593019ad7c24b3874f6b2f3b10d0f42af8218b3a966722f6e`
- R26 stage: `41f4e2aad7720862a98349d61d22c482b7f5045b6c54bfea56651d4032d97680`
- R24 source-carrier image: `e6768ee326b9796130e4ea63933ed72238f1c327c63759b70c9662e0590deedf`

Every R32 artifact is hashed from actual runtime bytes in the R32 manifest.

# Part II — UNIT-CHAMBER EXACT SYSTEM

The exact system is frozen in `105-R32-unit-chamber-exact-system.md`.

q=1:

\[
10^{m_2-1}\le A\Lambda\le10^{m_2}-1,
\qquad
10^{m_3-1}\le W\Lambda\le10^{m_3}-1.
\]

Coarse source room:

\[
10^{n_2-1}\le C_2U\le10^{n_2}-1,
\qquad
10^{n_3-1}\le C_3U\le10^{n_3}-1.
\]

The exact coarse integer-room iff is \(U_{\rm lo}\le U_{\rm hi}\); full
\(\mathcal U_0\) additionally carries the frozen residue/completed-source
predicates.

# Part III — DIGIT-RATIO ELIMINATION

Using

\[
\frac{P_2}{P_3}=\frac WA\frac{C_2}{C_3}
\]

and the exact R26 exponent identity gives

\[
10^{2g+k-2}<P_2/P_3<10^{2g+k+2}.
\]

No contradiction appears. Exact mantissas satisfy

\[
\frac{P_2}{10^{2g+k}P_3}
=\frac{\beta_3}{\beta_2}\frac{\alpha_2}{\alpha_3}.
\]

Thus the four digit blocks alone are saturated at a factor-100 packet window.

# Part IV — SOURCE-ROOM COLLISION

The universal ROOM-KILL theorem

\[
q=1\Longrightarrow C_2\ge10^{n_2}\ \vee\ C_3\ge10^{n_3}
\]

is **not proved**.

It is also **not falsified under all frozen preconditions**, because no genuine
TC1/master q1 source-room survivor was found.

The structural packet \((50,10,1,51)\) proves only that the digit/support
subsystem can have a room survivor; TC1/master is the exact missing condition.

# Part V — SEVEN-HIT AUTOPSY

Exact replay gives:

```text
raw-TC1 q1 hits = 7
Face-3 room kill = 7
Face-2 room kill = 5
Ulo-Uhi = 1 for 7/7
g=0,k=1,lambda_z=tau=1 for 7/7
```

Full rows are in `105-R32-q1-seven-hit-autopsy.csv`.

# Part VI — ACTIVE q1 COUNTEREXAMPLE HUNT

Two falsification modes were used:

1. an exact structural countermodel to falsify digit-only mutual exclusion;
2. a restricted master+sphere search over 899,910 exact configurations.

The restricted lane found zero square discriminants and zero integer TC1-conic
roots. This is not promoted to a global theorem.

No genuine q1 source-room survivor satisfying TC1/master was found.

# Part VII — FULL RECONSTRUCTION IF POSITIVE

No \(N_{30}>0\) unit point was obtained, so the R26 iff reconstruction was not
triggered. The structural countermodel dies before N30 at TC1/master; the seven
historical q1 TC1 rows die at coarse source room.

# Part VIII — PRIME BRANCH IMMEDIATE PURSUIT

Because unit extinction was **not proved**, the campaign rule “if q1 dies, make
prime the unique frontier” did not trigger.

Still, the q1 variable deletion extends exactly to prescribed prime p:

\[
m_2=\operatorname{dig}(A\Lambda p),\quad
m_3=\operatorname{dig}(W\Lambda p),\quad
g=m_3-n_3,\quad
k=n_2-m_2-g.
\]

For minimal prime p, retain

\[
Q_-\le p\le Q_+,\qquad p\nmid FU,\qquad Q_+<10Q_-.
\]

The restricted one-digit lanes \(p=2,3,5,7\) inherit the same zero-TC1-conic
search in the stated box. No global prime extinction is claimed.

# Part IX — MANDATORY 12 ANSWERS

1. **Lowest-complexity q1 denominator normal form:**  
   \(m_2=\mathrm{dig}(A\Lambda)\), \(m_3=\mathrm{dig}(W\Lambda)\), with
   \(\Lambda=\mathrm{lcm}(\mu,\lambda_z)\).

2. **Coarse source-digit necessary and sufficient condition:**  
   exactly \(U_{\rm lo}\le U_{\rm hi}\) for existence of a positive integer
   satisfying S2/S3; full \(\mathcal U_0\) adds frozen residue/completed gates.

3. **Does q1 universally force \(U_{\rm hi}=0\)?**  
   **Undecided globally.** True for all seven complete-bounded q1 raw-TC1 hits.

4. **Which face dies?**  
   In the seven-hit complete \(Q_0\le3000\) corpus, Face 3 kills 7/7 and Face 2
   kills 5/7. No global Face-3 theorem is proved.

5. **Can denominator/source interval intersections be proved mutually exclusive directly?**  
   **No from digit/exponent identities alone.** Exact elimination leaves a
   nonempty factor-100 invariant window; a structural countermodel confirms the
   need for TC1/master.

6. **Packet-only ratio after eliminating A/W:**  
   \[
   \boxed{\mathfrak R=P_2/(10^{2g+k}P_3)}.
   \]

7. **Exact exponent difference:**  
   \[
   \boxed{(m_3-m_2)-(n_3-n_2)=2g+k}.
   \]

8. **Can \(U=1\) occur?**  
   Yes in the digit/support subsystem; the explicit \((50,10,1,51)\) packet has
   U=1. No genuine q1+TC1/master+completed-source U=1 survivor is known.

9. **Genuine q1 source-room survivor?**  
   **Not found.**

10. **If q1 dead, genuine minimal-prime survivor?**  
    q1 was not proved dead, so this implication was not activated. No genuine
    prime survivor was found in the bounded lanes attacked.

11. **Full \(N_{30}>0\) architecture?**  
    **No.**

12. **Has the global remainder collapsed to prime/composite only?**  
    **No.** Unit is sharply reduced but still logically open. The minimal
    unresolved unit object is `MASTER_CONDITIONED_UNIT_SOURCE_ROOM_COLLISION`.

# TERMINAL VERDICT

```text
R32_TERMINAL_ATTACK_FAILED
R32_UNIT_CHAMBER_SATURATION_CERTIFICATE=PROVED

UNIT_CHAMBER_SOURCE_ROOM_EXTINCTION=NOT_PROVED_NOT_FALSIFIED
GLOBAL_N30_ZERO_THEOREM=NOT_PROVED
STRICT_A1_UNLIFTABILITY_PROVED=NO
FULL_STRICT_A1_WITNESS_FOUND=NO

UNIT_CHAMBER_DIGIT_DETERMINIZATION_THEOREM=PROVED
PRESCRIBED_Q_DIGIT_DETERMINIZATION_THEOREM=PROVED
DIGIT_ONLY_UNIT_ROOM_KILL=SATURATED_AND_INSUFFICIENT
MASTER_CONDITIONED_UNIT_SOURCE_ROOM_COLLISION=OPEN

MINIMAL_PRIME_DENOMINATOR_EXTINCTION=NOT_PROVED
GENUINE_PRIME_Q_SURVIVOR_FOUND=NO
```
