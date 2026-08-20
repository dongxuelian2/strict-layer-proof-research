# 105-R39 Stage Archive — Source-Exponent Image Internalization × Production-Native Root Reconstruction

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R39  
**Arithmetic:** exact integers only  
**Status:** FROZEN / ARCHIVED

# Executive Verdict

R39 permanently removes ambient exponent freedom from root generation.

For prescribed \(q\),

\[
m_2=\operatorname{dig}(A\Lambda q),\qquad
m_3=\operatorname{dig}(W\Lambda q),
\]
\[
g=m_3-n_3,\qquad
k=n_2-m_2-g,
\]
with \(g\ge0,k\ge1\), followed by
\[
X=10^{m_2},\quad Y=10^{n_3},\quad G=10^g,\quad K=10^k.
\]

This gives

\[
L_{\rm src}=a10^{n_2+n_3},
\]
\[
B_{\rm src}=\mu(W+A10^{m_3})+a10^{m_2+m_3},
\]
\[
C_{\rm src}=\mu g_0a(C_3+10^{n_3}C_2).
\]

A new global theorem is proved:

\[
\boxed{B_{\rm src}<L_{\rm src}}
\quad\Longrightarrow\quad
\boxed{\mathcal A_N<0}.
\]

Hence the source-native \(\mathcal A_N=0\) branch is globally extinct.

However source-exponent synchronization itself is not an extinction mechanism. R39 recovers the exact production-normalized exponent-synchronized root

\[
\boxed{(P_1,P_2,P_3,Q_0)=(48,436,75,445)}
\]

with

\[
(g_0,\mu,a,s)=(12,2,1,2),
\quad
(n_2,n_3,m_2,m_3,g,k)=(2,1,1,1,0,1),
\]
\[
(X,Y,G,K)=(10,10,1,10),
\quad
(L,B,C)=(1000,168,26760).
\]

It passes selector normalization, primitive sphere, NTC1, shape, \(\mu\)-support and \(\Lambda\)-recovery. Its first downstream failure is exactly

\[
\boxed{U_{\rm lo}=1>0=U_{\rm hi}}.
\]

```text
SOURCE_EXPONENT_SYNCHRONIZATION_EXTINCTION=FALSE
GENUINE_EXPONENT_SYNCHRONIZED_ROOT=YES
SOURCE_NATIVE_LINEAR_BRANCH_EXTINCTION=PROVED
SOURCE_NATIVE_QUADRATIC_BRANCH_NONEMPTY=YES
ACTUAL_SOURCE_ROOT_EXISTS=UNDECIDED_GLOBALLY
CORRECTED_SIMULTANEOUS_LOCUS_POSITIVE=NOT_FOUND
MASTER_REFINED_TERMINAL_POSITIVE=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
STRICT_A1_UNLIFTABILITY_PROVED=NO
R39_TERMINAL_ATTACK_FAILED
R39_SOURCE_EXPONENT_IMAGE_SATURATION_CERTIFICATE=PROVED
```

# Part I — FILE / HASH AUDIT

Historical File Library objects are not mounted as raw bytes in this runtime. They are therefore recorded as `LEDGER-CROSSCHECK`, never as newly recomputed bytewise hashes. See `105-R39-input-hash-audit.csv`.

Every R39-created byte is hashed in `105-R39-SHA256-MANIFEST.txt`.

# Part II — SOURCE-EXPONENT IMAGE

R39 freezes two nested images:

\[
\mathscr E_{\exp}=\text{prescribed-q deterministic exponent image},
\]

\[
\mathscr E_{\rm src}=
\mathscr E_{\exp}\cap
\{\text{actual legal source integer }U\}.
\]

This distinction is necessary because exponent synchronization is already nonempty, while actual source-fibre intersection remains open.

The exact packet-dependent scale is

\[
\lambda_z=\frac{10^{n_3}}{(10^{n_3},W(Q_0-P_3))},
\quad
\Lambda=\operatorname{lcm}(\mu,\lambda_z).
\]

Thus \(q\) must precede coefficient construction, but \(\Lambda\) itself is packet-native.

# Part III — PRODUCTION-NATIVE COEFFICIENTS

\[
L_{\rm src}=a10^{n_2+n_3},
\]
\[
B_{\rm src}=\mu(W+A10^{m_3})+a10^{m_2+m_3},
\]
\[
C_{\rm src}=\mu g_0a(C_3+10^{n_3}C_2).
\]

The exact CORE relation is

\[
B_{\rm src}Q_0=
g_0\mu a
\left(
s10^{n_2+n_3}+C_3+10^{n_3}C_2
\right).
\]

# Part IV — R38 ROOT REGRESSION

The R38 root used \(X=1\). Its frozen source semantics force \(m_2=1\), hence \(X=10\). R39 rejects it before root construction.

```text
R38_GENUINE_ROOT_GENERATION_REGRESSION=PASS
R36_FAKE_ROOT_REGRESSION=12/12_DEAD
```

# Part V — SOURCE-NATIVE LINEAR / QUADRATIC SYSTEM

The global denominator inequalities and \(\mu\mid\Lambda\) imply

\[
B_{\rm src}<L_{\rm src}.
\]

Therefore

\[
\mathcal A_N<0
\]

on every source-native root.

The linear branch is globally empty. The quadratic branch is nonempty, witnessed by \((48,436,75,445)\).

# Part VI — INFORMATION-GAIN AUDIT

Since

\[
B_{\rm src}Q_0-C_{\rm src}=L_{\rm src}P_1,
\]

PINT, QINT and the full decimal divisibility are exact restatements of NTC1 after source synchronization.

```text
PINT_INFORMATION_GAIN=0
QINT_INFORMATION_GAIN=0
SOURCE_NATIVE_DECIMAL_DIVISIBILITY_INFORMATION_GAIN=0
```

# Part VII — GLOBAL EXTINCTION OR EXACT ROOT

Exact root found:

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445).
\]

\[
(L,B,C)=(1000,168,26760),
\quad
\mathcal A_N=-971776.
\]

\[
\delta_{\rm norm}=190913068096=436936^2.
\]

Therefore source-exponent synchronization extinction is false.

# Part VIII — DOWNSTREAM FULL REPLAY

For the exact root,

\[
D=35,\quad H=9,\quad T=370,
\]

\[
\lambda_z=1,\quad \Lambda=2.
\]

Shape, primitive, selector, \(\mu\)-support and \(\Lambda\)-recovery pass.

Then

\[
U_{\rm lo}=1,\qquad U_{\rm hi}=0.
\]

First failure:

```text
SOURCE_INTEGER_ROOM_EMPTY
```

# Part IX — TERMINAL PAIR

Not reached. The actual source fibre is empty for the first synchronized root.

# Part X — ORIGINAL STRICT-(A1) RECONSTRUCTION

Not triggered: no terminal pair.

# Part XI — SIXTEEN REQUIRED ANSWERS

1. **Authoritative source exponent iff:** prescribed \(q\), exact denominator digit windows, deterministic \(m_2,m_3,g,k\), then semantic powers; full source image further requires legal \(U\) and frozen source-completed predicates.
2. **Exact \(X,Y,G,K\):** \(X=10^{m_2},Y=10^{n_3},G=10^g,K=10^k\).
3. **Deterministic recovery:** yes, for prescribed \(q\).
4. **Must \(q\) precede root generation?** yes, it must precede coefficient construction because it fixes \(m_2,m_3\). \(\Lambda\) remains packet-native.
5. **Does \(L_N\) collapse?** yes: \(L_N=a10^{n_2+n_3}\).
6. **Source-native \(B,C\):** as in Part III.
7. **Source-native linear NTC1:** CORE above.
8. **PINT/QINT gain:** zero as standalone information.
9. **Quadratic source-native roots:** yes.
10. **Linear \(\mathcal A_N=0\) roots:** no; globally extinct.
11. **R38 genuine root removed pre-generation:** yes.
12. **First genuine exponent-synchronized root:** yes, \((48,436,75,445)\).
13. **Its next failure:** actual source integer room \(1>0\).
14. **Corrected simultaneous locus:** not reached by this root; no global positive point found.
15. **Terminal pair / full reconstruction:** none.
16. **Unique R40 object:** the intersection of the source-native strictly-negative quadratic production-root locus with the actual legal source fibre
\[
\boxed{\mathcal A_N<0\text{ production root}\ \cap\ \mathcal U_0\ne\varnothing}.
\]
If that intersection is positive, R40 must immediately continue to the denominator/terminal pair; exponent synchronization itself is retired.

# TERMINAL VERDICT

```text
R39_TERMINAL_ATTACK_FAILED
R39_SOURCE_EXPONENT_IMAGE_SATURATION_CERTIFICATE=PROVED

AMBIENT_FAKE_EXPONENT_FREEDOM=DELETED
Q_BEFORE_ROOT_COEFFICIENTS=YES
SOURCE_EXPONENT_SYNCHRONIZATION_EXTINCTION=FALSE
GENUINE_EXPONENT_SYNCHRONIZED_ROOT=YES

SOURCE_NATIVE_LINEAR_BRANCH_EXTINCTION=PROVED
SOURCE_NATIVE_QUADRATIC_BRANCH_NONEMPTY=YES

FIRST_SYNCHRONIZED_ROOT=(48,436,75,445)
FIRST_SYNCHRONIZED_ROOT_NEXT_FAILURE=SOURCE_INTEGER_ROOM_EMPTY

CORRECTED_SIMULTANEOUS_LOCUS_POSITIVE=NOT_FOUND
MASTER_REFINED_TERMINAL_POSITIVE=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
STRICT_A1_UNLIFTABILITY_PROVED=NO

R40_UNIQUE_OBJECT=
SOURCE_NATIVE_NEGATIVE_QUADRATIC_ROOT_X_ACTUAL_SOURCE_FIBRE
```
