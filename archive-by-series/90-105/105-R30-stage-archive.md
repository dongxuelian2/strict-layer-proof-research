# 105-R30 Stage Archive — TC3 × TC4 Integer Fusion × q-Elimination × Canonical-Successor Collision

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R30  
**Campaign position:** 最后十五轮终局总攻第 5 轮  
**Terminal verdict:** **Q variable eliminated exactly, but global TC3×TC4 incompatibility not proved; no genuine full survivor found.**

---

# Part I — FILE / HASH AUDIT

## 1. Frozen inputs actually recovered

R30 began from the frozen R26/R29 artifacts, not from conversational formula guesses.

### R26

Recovered:

- `105-R26-stage-archive.md`
- `105-R26-stage-archive.sha256.txt`

The authoritative R26 ledger records

```text
41f4e2aad7720862a98349d61d22c482b7f5045b6c54bfea56651d4032d97680  105-R26-stage-archive.md
```

R26 is used only as the complete finite-predicate wrapper:

\[
\pi\text{ admits a full Strict-}A_1\text{ lift}
\iff
\mathcal C_{26}(\pi)=1,
\]

with finite selectors/exponents after fixing the primitive sphere packet.

### R29

Recovered / audited:

- `105-R29-stage-archive.md`
- `105-R29-post-radial-support-saturation-certificate.md`
- `105-R29-survivor-registry.csv`
- `105-R29-execution.log`
- `105-R29-SHA256-MANIFEST.txt`

The R29 manifest ledger records, among others:

```text
stage archive:
f21b69272157b02a810830e49c10e5a4649daf565ad24f1ff3a946275f21ec3d

post-radial support saturation certificate:
e374454c24e167a922d75c06f92e93dc1041e4d56f0f7679f80abb0fe602c8d0

survivor registry:
2c0ed6ba790c48ca2c75ecf5f56aa44655052945f63a384a06360d8c01b39186

execution log:
14a79c07efeb3ff7aa32d3b60e9cfc75be608da77ed197749bb6df9ed1004084
```

### Hash-audit limitation

The old artifacts were available through the File Library as referenced/parsed files, not as raw bytes mounted in the R30 runtime. Therefore R30 can cross-check their frozen SHA ledgers but cannot honestly claim a new byte-for-byte rehash of those inputs. Every newly generated R30 artifact **is** bytewise SHA-256 hashed locally.

## 2. Authoritative definition sources followed beyond R26/R29

R26 invokes TC3/TC4 but the exact formulas are inherited from their theorem sources. R30 therefore additionally recovered:

TC3:

- `105_R15_Master_G1_Z_Shell_Phase_Offensive.md`
- `105_R15_Z_Shell_Normalization.csv`
- `105_R15_Q_Successor_Registry.csv`

TC4:

- `105_R8_Common_U_Integer_Source_Fibre.md`
- `105_R2_Source_Section_Internalization.md`
- `105_R3_Source_Completed_Valuation_Atlas.md`

Common-dilation provenance:

- R14 variable graph / positive radial core lift fibre;
- R7/R7D decontented source row and determinant packet.

## 3. R30 files generated

Required files:

- `105-R30-stage-archive.md`
- `105-R30-stage-archive.sha256.txt`
- `105-R30-TC3-TC4-exact-definitions.md`
- `105-R30-q-elimination-derivation.md`
- `105-R30-successor-collision-proof.md`
- `105-R30-scripts/r30_q_elimination.py`
- `105-R30-execution.log`
- `105-R30-q-interval-registry.csv`
- `105-R30-TC3-TC4-survivor-registry.csv`
- `105-R30-exceptional-branch-registry.csv`
- `105-R30-complete-certificate-registry.csv`
- `105-R30-SHA256-MANIFEST.txt`

Additional R30 audit artifacts:

- `105-R30-common-dilation-regression.csv`
- `105-R30-execution-script-output.json`
- `105-R30-Q-SUCCESSOR-SATURATION-CERTIFICATE.md`
- `105-R30-Q-SUCCESSOR-SATURATION-CERTIFICATE.sha256.txt`
- `105-R30-scripts/r30_manifest_verify.py`
- `r30-script-stdout.log`

No `STRICT-A1-EXTINCTION-CERTIFICATE` is generated because extinction was not proved. No `FULL-WITNESS-CERTIFICATE` is generated because no full witness was found.

---

# Part II — EXACT TC3 / TC4 RECOVERY

## 4. TC3: exact master/tail/Smith denominator arithmetic

For one fixed finite shape let

\[
M_0=u_0AW,
\qquad
g_0=\gcd(M_0,P_1).
\]

The exact gcd corridor is

\[
g_0\mid g_1^*\mid P_1.
\]

Define

\[
\mu=\frac{g_1^*}{g_0},
\qquad
R_1=\frac{P_1}{g_1^*}.
\]

The master gcd shell is exactly

\[
\gcd(M_0z,P_1)=g_1^*
\iff
z=\mu q_0,
\quad
(q_0,R_1)=1.
\]

With

\[
Y=10^{n_3},
\qquad
T_3=Q_0-P_3,
\]

define

\[
\lambda_z=\frac{Y}{\gcd(Y,WT_3)},
\]

\[
\tau=\frac{\lambda_z}{\gcd(\lambda_z,\mu)},
\]

\[
\boxed{
\Lambda=\operatorname{lcm}(\mu,\lambda_z)=\mu\tau.
}
\]

The exact compatibility gates are

\[
(A,C_2)=1,
\quad
(W,C_3)=1,
\quad
(\tau,R_1)=1,
\quad
(\Lambda,C_2C_3)=1.
\]

After those pass, define

\[
\boxed{
F=\operatorname{rad}(R_1C_2C_3)
=\operatorname{rad}\!\left(\frac{P_1}{g_1^*}C_2C_3\right).
}
\]

Then the complete residual shell is

\[
\boxed{
z=\Lambda q,
\qquad
(q,F)=1.
}
\]

The exact integer \(z\)-window is

\[
\boxed{
Z_-=\max\left(
\left\lceil\frac{10^{m_2-1}}A\right\rceil,
\left\lceil\frac{10^{m_3-1}}W\right\rceil
\right),
}
\]

\[
\boxed{
Z_+=\min\left(
\left\lfloor\frac{10^{m_2}-1}{A}\right\rfloor,
\left\lfloor\frac{10^{m_3}-1}{W}\right\rfloor
\right).
}
\]

Therefore

\[
\boxed{
Q_-=\left\lceil\frac{Z_-}{\Lambda}\right\rceil,
\qquad
Q_+=\left\lfloor\frac{Z_+}{\Lambda}\right\rfloor.
}
\]

and TC3 is precisely

\[
\boxed{
TC3:\quad
Q_-\le q\le Q_+,
\quad q\in\mathbb Z_{>0},
\quad (q,F)=1.
}
\]

There is no extra hidden parity condition at this theorem interface.

## 5. TC4: exact source successor

For one fixed post-PSDG source-completed profile,

\[
\boxed{U=\gcd(a_1,a_2,a_3)>0}
\]

is the unique radial fibre coordinate, with primitive source condition

\[
\boxed{(U,V)=1.}
\]

Define

\[
L_i=\frac{10^{n_i-1}}{C_i},
\qquad
R_i=\frac{10^{n_i}}{C_i}=10L_i,
\qquad i=2,3.
\]

Regular source interval:

\[
\boxed{
L=\max(L_2,L_3),
\qquad
R_{\rm src}=\min(R_2,R_3),
\qquad
[L,R_{\rm src}).
}
\]

Only two active faces occur.

### Face A

If \(L_2\ge L_3\),

\[
[L,R_{\rm src})=[L_2,R_3),
\]

\[
G_A=C_2 10^{n_3}-C_3 10^{n_2-1}.
\]

### Face B

If \(L_3>L_2\),

\[
[L,R_{\rm src})=[L_3,R_2),
\]

\[
G_B=C_3 10^{n_2}-C_2 10^{n_3-1}.
\]

Generic completed strata have source progression step \(h_U=1\).

The historical **different** source chart \(q_{\rm src}=1\) has exact decorated open interval

\[
\boxed{
\frac{d_q\tau_{\rm src}G}{10C_3}<U<\frac{G}{C_3}
}
\]

and exact congruence

\[
\boxed{
31C_3U+d_q\tau_{\rm src}\equiv0\pmod{2Kd_q}.
}
\]

Writing

\[
d_U=\gcd(C_3,2Kd_q),
\]

solvability is

\[
d_U\mid d_q\tau_{\rm src},
\]

and the affine step is

\[
\boxed{
h_U=\frac{2Kd_q}{d_U}.}
\]

The unique residue is

\[
\boxed{
r_{q1}
\equiv
-\frac{d_q\tau_{\rm src}}{d_U}
\left(\frac{31C_3}{d_U}\right)^{-1}
\pmod{h_U}.
}
\]

Any additional historical source-native unit predicate is finite-period and is included in the fixed source selector.

Now write the full fixed source-native periodic condition as a finite residue set

\[
\mathcal R_0\subseteq\mathbb Z/P_0\mathbb Z.
\]

After including \((U,V)=1\), one literal R8 period is

\[
M_U=\operatorname{lcm}(P_0,V),
\]

with

\[
\mathcal R_{\rm adm}
=
\{r\bmod M_U:
 r\bmod P_0\in\mathcal R_0,
 (r,V)=1\}.
\]

For a regular closed lower endpoint, put \(\ell=\max(L,1)\) and

\[
S_r(L)=
r+M_U\left\lceil\frac{\ell-r}{M_U}\right\rceil.
\]

Then

\[
\boxed{
U_{\min}=\min_{r\in\mathcal R_{\rm adm}}S_r(L),
}
\]

with \(+\infty\) if the residue set is empty. For an open lower endpoint use

\[
r+M_U\left(\left\lfloor\frac{L-r}{M_U}\right\rfloor+1\right).
\]

Finally

\[
\boxed{
TC4:\quad U_{\min}<R_{\rm src}.
}
\]

On regular Face A this is exactly

\[
C_3J_{{\rm src},2}<G_A,
\qquad
J_{{\rm src},2}=C_2U_{\min}-10^{n_2-1},
\]

and on Face B

\[
C_2J_{{\rm src},3}<G_B,
\qquad
J_{{\rm src},3}=C_3U_{\min}-10^{n_3-1}.
\]

TC4 is therefore fully expanded; it is no longer retained as a black-box function name.

---

# Part III — q-WINDOW NORMALIZATION

## 6. Exact floor/ceiling form

Once \(Z_\pm\) and \(\Lambda\) are fixed,

\[
Q_-=\left\lceil\frac{Z_-}{\Lambda}\right\rceil,
\qquad
Q_+=\left\lfloor\frac{Z_+}{\Lambda}\right\rfloor
\]

are integers. Therefore

\[
\boxed{\lceil Q_-\rceil=Q_-,\quad\lfloor Q_+\rfloor=Q_+.}
\]

The exact width is

\[
\boxed{
L_q:=Q_+-Q_-.
}
\]

To make all floor information explicit, write Euclidean divisions

\[
Z_-=a_-\Lambda+r_-,
\qquad 0\le r_-<\Lambda,
\]

\[
Z_+=a_+\Lambda+r_+,
\qquad 0\le r_+<\Lambda.
\]

Then

\[
\boxed{
Q_-=a_-+\mathbf 1_{r_->0},
\qquad
Q_+=a_+,
}
\]

and

\[
\boxed{
Q_+-Q_-=a_+-a_--\mathbf 1_{r_->0}.
}
\]

Thus the raw integer q count is

\[
\boxed{
N_{q,\rm raw}
=
\max\left(0,a_+-a_-+1-\mathbf 1_{r_->0}\right).
}
\]

This is the complete exact floor analysis.

## 7. Universal width verdict

R30 did **not** prove

\[
0<Q_+-Q_-<1
\]

or any other architecture-uniform constant upper bound.

The correct result is weaker but exact:

\[
\boxed{
\text{each fixed R26 architecture has a finite and explicitly counted q-fibre.}
}
\]

No universal q uniqueness theorem is signed.

---

# Part IV — CANONICAL SUCCESSOR NORMALIZATION

## 8. TC4 as residue/modulus/floor data

For a fixed source-completed architecture before inserting the R15 residual q, compress every q-independent source-native congruence into

\[
\mathcal R_0\subseteq\mathbb Z/P_0\mathbb Z.
\]

The remaining residual q changes the actual denominator common scale to

\[
V(q)=V_0q,
\qquad
\boxed{V_0=\Lambda u_0AW.}
\]

R8's primitive source condition becomes

\[
(U,V_0q)=1.
\]

A literal period for the combined source selector is

\[
\operatorname{lcm}(P_0,V_0q).
\]

Since coprimality depends only on prime support, an equivalent smaller coprimality period is

\[
\boxed{
M_{\rm src}^{\rm rad}(q)
=
\operatorname{lcm}(P_0,\operatorname{rad}(V_0q)).
}
\]

with the fixed \(P_0\)-selector retained. Thus TC4 is an explicit finite residue minimum, not an opaque Jacobsthal object.

## 9. Source room

The source room itself is

\[
[L,R_{\rm src})
\]

or its exact decorated q-src=1 intersection and does not depend on numerical residual q once the R26 architecture is fixed.

This fact is decisive for the R30 elimination.

---

# Part V — q-ELIMINATION

## 10. Common-dilation theorem

R14 gives

\[
V=z\,u_0AW,
\qquad
b_2=zA,
\qquad
b_3=zW,
\]

and the frozen \(g_1\)-shell determines \(b_1\) through the same denominator scale.

With \(z=\Lambda q\),

\[
\boxed{V(q)=V_0q.}
\]

For TC3-admissible q, \((q,F)=1\) and

\[
F=\operatorname{rad}(R_1C_2C_3),
\]

so the residual q cannot alter the already decontented radial coefficients \(C_2,C_3\), nor the exact \(g_1\) shell. The R7 decontented source row is likewise invariant under the common q-dilation.

R30 machine regression checked ten exact common dilations of the frozen R7D witness B and recovered the same normalized row

\[
\boxed{(21,125,3345)}
\]

in every case.

This regression certifies the implementation of the homogeneity identity; it is not used as a global proof by enumeration.

## 11. Residual q enters TC4 only through primitive coprimality

The only remaining q-dependent source predicate is

\[
(U,V_0q)=1.
\]

Exactly,

\[
\boxed{
(U,V_0q)=1
\iff
(U,V_0)=1\text{ and }(U,q)=1.
}
\]

Define \(\mathcal U_0(\mathfrak a)\) to be the finite set of source integers satisfying:

- the exact decorated source room;
- the fixed source-native periodic selector;
- all q-independent completed-source predicates;
- \((U,V_0)=1\).

Then

\[
TC3+TC4
\]

is equivalent to

\[
\exists U\in\mathcal U_0
\ \exists q\in[Q_-,Q_+]\cap\mathbb Z_{>0}
:
(q,F)=1,
(q,U)=1.
\]

Hence

\[
\boxed{
TC3+TC4
\iff
\exists U\in\mathcal U_0
\ \exists q\in[Q_-,Q_+]\cap\mathbb Z_{>0}
:
(q,FU)=1.
}
\tag{Fusion}
\]

## 12. Exact Möbius elimination

For each \(U\in\mathcal U_0\), let

\[
\boxed{
\Phi_{\mathfrak a}(U)
=
\sum_{d\mid\operatorname{rad}(FU)}
\mu(d)
\left[
\left\lfloor\frac{Q_+}{d}\right\rfloor
-
\left\lfloor\frac{Q_--1}{d}\right\rfloor
\right].
}
\]

This is exactly the number of compatible residual q.

Now define

\[
\boxed{
N_{30}(\mathfrak a)
=
\sum_{U\in\mathcal U_0(\mathfrak a)}
\Phi_{\mathfrak a}(U).
}
\]

Then

\[
\boxed{
TC3(\mathfrak a)+TC4(\mathfrak a)
\iff
N_{30}(\mathfrak a)>0.
}
\tag{R30 terminal count}
\]

This is a true q-free terminal predicate for each fixed architecture.

### Machine verification

`r30_q_elimination.py` verified the Möbius count against direct enumeration in

\[
\boxed{540000}
\]

exact test cases and verified

\[
(U,V_0q)=1\iff(U,V_0)=(U,q)=1
\]

in

\[
\boxed{117649}
\]

exact triples.

All assertions passed.

---

# Part VI — TC3 × TC4 COLLISION

## 13. Exact collision certificate

For one fixed source candidate \(U\),

\[
\Phi_{\mathfrak a}(U)=0
\]

if and only if

\[
\boxed{
[Q_-,Q_+]\cap\mathbb Z
\subseteq
\bigcup_{p\mid FU}p\mathbb Z.
}
\]

Therefore one full architecture is TC3×TC4-dead exactly when every q-independent source candidate \(U\in\mathcal U_0\) has such a prime-cover certificate.

This is the exact joint obstruction. It uses interval + residue/coprimality + source room simultaneously.

## 14. Why generic Jacobsthal is unnecessary

The relevant quantity is not a worst-case \(j(F)\) over arbitrary intervals. For fixed \(U\) it is the exact finite count modulo \(\operatorname{rad}(FU)\).

A huge generic upper bound would discard the architecture-specific endpoint position and the source integer \(U\) itself. R30 therefore replaces Jacobsthal by exact Möbius/prime-cover arithmetic.

## 15. Why numerical q-monotonicity does not globalize

The proposed high-priority route

\[
U_{\min}(q)\nearrow,
\qquad
R_{\rm src}(q)\searrow
\]

is not the actual R30 structure. The source room is q-independent on the residual shell. Residual q only changes which prime divisors are forbidden in U.

Thus the meaningful q-class is its added radical support, not its numerical size.

No theorem

\[
q_1<q_2\Longrightarrow U_{\min}(q_1)\le U_{\min}(q_2)
\]

is inherited or proved.

This closes the numerical-q staircase route as a universal endgame mechanism.

## 16. Global collision verdict

R30 **does not** prove

\[
TC3\Longrightarrow\neg TC4
\]

for all legal post-support architectures.

Equivalently, R30 does not prove the architecture-uniform zero statement

\[
N_{30}(\mathfrak a)=0
\quad\forall\mathfrak a.
\]

The local collision theorem is complete; its global uniform sign is open.

---

# Part VII — HISTORICAL SURVIVOR AUTOPSY

## 17. Frozen R29 support survivor

The R29 genuine support survivor is

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*)=(1,20,1,80),
\]

\[
(n,m,k,g)=(4,1,1,0).
\]

In the R26 tuple notation:

\[
(n,\delta,\rho,m)=(4,-2,2,1),
\]

so

\[
n_3=4,
\quad n_2=2,
\quad m_2=1,
\quad m_3=4.
\]

The exact R30 reconstruction is

\[
C_2=71,
\qquad
C_3=4727=29\cdot163,
\]

\[
g_0=20,
\quad
\mu=4,
\quad
R_1=8,
\]

\[
\lambda_z=2,
\quad
\tau=1,
\quad
\Lambda=4,
\]

\[
\boxed{F=671234=2\cdot29\cdot71\cdot163.}
\]

The denominator block windows give

\[
\boxed{Z_-=50,\qquad Z_+=9.}
\]

Hence

\[
\boxed{Q_-=13,\qquad Q_+=2.}
\]

Thus the shortest arithmetic death certificate is

\[
\boxed{13>2.}
\]

and therefore

```text
TC3=FAIL_EMPTY_INTERVAL
TC3_Q_CANDIDATES=0
TC4=NOT_ACTIVATED
```

This is the R30 reinterpretation of the old \(Z_-=50>Z_+=9\) certificate.

## 18. Raw source room for the same packet

Ignoring the fact that TC4 is unreachable after TC3 fails, blocks 2 and 3 would give

\[
L=\max\left(\frac{10}{71},\frac{1000}{4727}\right)
=\frac{1000}{4727},
\]

\[
R_{\rm src}=\min\left(\frac{100}{71},\frac{10000}{4727}\right)
=\frac{100}{71}.
\]

This interval contains \(U=1\). Therefore it would be wrong to rewrite the historical failure as “canonical U successor misses the source room.” The actual first-failure remains TC3 empty q-window.

## 19. Mechanism extracted from the autopsy

Why could this packet pass TC1/shape/radial/Smith/tail yet die terminally?

Because after all forced denominator divisibility has been absorbed into

\[
z=\Lambda q,
\]

the two denominator digit windows are already disjoint at the \(z\)-scale:

\[
50>9.
\]

Dividing by the forced scale \(\Lambda=4\) preserves that incompatibility as

\[
13>2.
\]

This point therefore exhibits **denominator interval extinction**, not a universal successor-gap mechanism.

---

# Part VIII — COUNTEREXAMPLE SEARCH

## 20. Search strategy used

R30 obeyed the command not to sweep the primitive-sphere ocean again. The replay/search was concentrated on previously constructed post-master/post-support interfaces:

- R15 exact q-successor registries;
- R17 first master-corridor pass;
- R20 first positive \(\mu\)-Smith/support-stack pass;
- R26 finite-predicate historical complete candidate;
- R28 bounded TC1 reconnaissance;
- R29 support survivor registry;
- R8 post-PSDG source successor census.

The R30 registry records:

```text
GENUINE_TC3_TC4_PASS_COUNT=0
FULL_STRICT_A1_WITNESS_COUNT=0
STATUS=NONE_FOUND_NOT_GLOBAL_PROOF
```

## 21. Search interpretation

No finite replay hit is promoted to a theorem.

Therefore R30 signs neither

```text
TC3_TC4_UNIVERSAL_INCOMPATIBILITY=FALSE
```

(which would require a genuine pass tuple) nor

```text
TC3_TC4_GLOBAL_INCOMPATIBILITY=YES
```

(which would require an all-architecture proof).

The search has one legitimate use: it confirms that the new q-free count has not immediately exposed a frozen archived survivor that earlier rounds missed.

---

# Part IX — GLOBAL TERMINAL RESULT

## 22. What R30 actually proves

### Theorem R30-A — residual q common-dilation retirement

On a fixed TC3-ready R26 architecture, the R15 residual q multiplies the common denominator scale and does not create a new decontented source geometry. Its only TC4 effect is the extra unit condition \((U,q)=1\).

### Theorem R30-B — TC3×TC4 q-free count equivalence

For every fixed legal TC3-ready architecture \(\mathfrak a\),

\[
\boxed{TC3+TC4\iff N_{30}(\mathfrak a)>0.}
\]

This completely removes q as an independent existential coordinate.

### Theorem R30-C — architecture extinction iff exact prime cover

One architecture is terminally dead iff every \(U\in\mathcal U_0\) has its q-window covered by primes dividing \(FU\).

This is a finite exact symbolic-computational certificate.

## 23. What R30 does not prove

R30 does not prove:

- universal q uniqueness;
- a universal constant bound on q-window length;
- universal TC3×TC4 incompatibility;
- Strict \(A_1\) unliftability;
- a genuine full witness.

The missing mathematical object is now exactly

\[
\boxed{
\forall\mathfrak a\text{ legal post-support},
\quad N_{30}(\mathfrak a)=0,
}
\]

or one exact legal architecture with \(N_{30}(\mathfrak a)>0\) and full reconstruction.

## 24. Further compression of \(\mathcal C_{26}\)

R26 had, schematically,

\[
\mathcal C_{26}(\pi)=1
\iff
\exists\mathfrak a\in\operatorname{Arch}_{26}(\pi):
TC1\wedge TC2\wedge TC3\wedge TC4.
\]

R30 allows the exact replacement

\[
\boxed{
TC3\wedge TC4
\iff
N_{30}(\mathfrak a)>0.
}
\]

Therefore

\[
\boxed{
\mathcal C_{26}(\pi)=1
\iff
\exists\mathfrak a\in\operatorname{Arch}_{26}(\pi):
TC1\wedge TC2\wedge[N_{30}(\mathfrak a)>0].
}
\]

On the already post-support/TC1-TC2-ready locus, the terminal predicate is one q-free finite count.

This is the architecture deletion actually achieved by R30.

---

# Direct answers to the twelve mandatory questions

## Q1. TC3 的 exact \(Q_-,Q_+,F\) 是什么？

\[
Z_-=
\max\left(
\left\lceil\frac{10^{m_2-1}}A\right\rceil,
\left\lceil\frac{10^{m_3-1}}W\right\rceil
\right),
\]

\[
Z_+=
\min\left(
\left\lfloor\frac{10^{m_2}-1}{A}\right\rfloor,
\left\lfloor\frac{10^{m_3}-1}{W}\right\rfloor
\right),
\]

\[
Q_-=\left\lceil Z_-/\Lambda\right\rceil,
\qquad
Q_+=\left\lfloor Z_+/\Lambda\right\rfloor,
\]

\[
F=\operatorname{rad}\!\left((P_1/g_1^*)C_2C_3\right),
\]

and TC3 is \(Q_-\le q\le Q_+\), \((q,F)=1\).

## Q2. TC4 的 exact \(U_{\min},R_{\rm src}\) 是什么？

Regularly,

\[
R_{\rm src}=\min(10^{n_2}/C_2,10^{n_3}/C_3).
\]

The fixed source-native residue selector is combined with \((U,V)=1\) into a finite set \(\mathcal R_{\rm adm}\) modulo \(M_U\); then

\[
U_{\min}
=
\min_{r\in\mathcal R_{\rm adm}}
\left[
r+M_U\left\lceil\frac{\max(L,1)-r}{M_U}\right\rceil
\right]
\]

with strict-lower correction on open decorated branches, and TC4 is \(U_{\min}<R_{\rm src}\).

## Q3. TC3 的 q-window 宽度是否 universal bounded？

Each fixed architecture has finite exact width \(Q_+-Q_-\). No architecture-uniform constant bound was proved.

## Q4. 每个 post-support architecture 的 q candidates 是否 universal 有限？

For each fixed architecture: yes, exactly \(\max(0,Q_+-Q_-+1)\) before the gcd sieve. A universal absolute bound independent of architecture: not proved.

## Q5. q 能否被完全消元？

**Yes as a free integer coordinate.** Exact replacement:

\[
TC3+TC4\iff N_{30}(\mathfrak a)>0.
\]

This does not yet imply global extinction.

## Q6. TC4 的 successor modulus 和 residue 是什么？

R8 literal modulus is \(\operatorname{lcm}(P_0,V)\). After writing \(V=V_0q\), an equivalent prime-support period is

\[
\operatorname{lcm}(P_0,\operatorname{rad}(V_0q)).
\]

For the historical source-chart \(q_{\rm src}=1\),

\[
h_U=\frac{2Kd_q}{\gcd(C_3,2Kd_q)}
\]

and

\[
r_{q1}
\equiv
-\frac{d_q\tau_{\rm src}}{d_U}
\left(\frac{31C_3}{d_U}\right)^{-1}
\pmod{h_U}.
\]

## Q7. TC3 coprimality 与 TC4 successor 是否形成直接 collision？

They fuse exactly into \((q,FU)=1\), hence an exact finite prime-cover criterion. That coupling is real, but R30 did not prove it universally fatal.

## Q8. R29 historical support survivor 的最短 TC3×TC4 死亡证书？

\[
\boxed{Q_-=13>2=Q_+.}
\]

TC3 has zero integer q candidates, so TC4 is not activated.

## Q9. 是否存在 TC3-pass / TC4-pass genuine tuple？

None was found in the frozen replay corpus and current exact regression. This is not a global nonexistence theorem.

## Q10. 若不存在，最强 global obstruction 是哪一类？

No universal fatal obstruction was proved. The strongest **exact general form** is the q-free architecture count / prime-cover obstruction \(N_{30}=0\). For the R29 historical point specifically, the fatal mechanism is interval emptiness.

## Q11. \(\mathcal C_{26}\) 是否可以进一步压缩成一个 q-free terminal certificate？

Yes, architecturewise: replace TC3+TC4 by \(N_{30}(\mathfrak a)>0\). The remaining outer primitive packet / finite-architecture quantifier is not eliminated.

## Q12. 如果今天必须结束 105，剩余自由度到底还是什么？

The residual denominator q is retired. Remaining freedom is:

\[
\boxed{
\text{primitive sphere packet}
+
\text{finite R26 architecture labels}
+
\text{q-independent finite source set }\mathcal U_0,
}
\]

with the terminal q-free arithmetic count \(N_{30}\). The minimal missing theorem is an architecture-uniform zero theorem for \(N_{30}\), or one genuine positive \(N_{30}\) witness followed by reconstruction.

---

# TERMINAL VERDICT

The strongest truthful machine-readable block is:

```text
STRICT_A1_UNLIFTABILITY_PROVED=NO

TC3_TC4_GLOBAL_INCOMPATIBILITY=NOT_PROVED

GLOBAL_Q_ELIMINATION_TERMINAL_THEOREM=NO
# Reason: q is eliminated, but the requested theorem also required global impossibility.

GLOBAL_TC3_TC4_FINITE_CLASSIFICATION=NO_GLOBAL_PRIMITIVE_PACKET_CLASSIFICATION

FULL_STRICT_A1_WITNESS_FOUND=NO

TC3_TC4_UNIVERSAL_INCOMPATIBILITY=UNDECIDED
# Do not write FALSE without a genuine pass tuple.

Q_VARIABLE_ELIMINATION_EQUIVALENCE=PROVED
TC3_TC4_Q_FREE_COUNT_EQUIVALENCE=YES
ARCHITECTURE_TERMINAL_PREDICATE=N30(a)>0

R30_Q_SUCCESSOR_SATURATION_CERTIFICATE=PROVED

R30_TERMINAL_ATTACK_FAILED=YES
```

The round therefore ends with a genuine architecture deletion—**the residual denominator integer is no longer an independent variable**—but not with Strict \(A_1\) extinction.
