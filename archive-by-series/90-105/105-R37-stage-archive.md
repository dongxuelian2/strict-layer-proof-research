# 105-R37 Stage Archive

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — (A1)-only  
**Round:** 105-R37  
**Arithmetic:** exact integers only

# Part I — FILE / HASH AUDIT
R36's SHA-256 manifest was read as the authoritative byte-hash ledger. File Library references are not mounted as local bytes in this runtime, so R36 input verification is explicitly recorded as `LEDGER-CROSSCHECK`, not falsely labeled bytewise recomputation. The full twelve-root registry and the R36 source-first generator were separately read and replayed. R37-created files are hashed bytewise locally.

See `105-R37-input-hash-audit.csv` and `105-R37-SHA256-MANIFEST.txt`.

# Part II — GCD-NORMALIZED COORDINATES
Exact equivalence:
\[
\boxed{g_0=(u_0AW,P_1)}
\iff
\boxed{u_0AW=g_0a,\ P_1=g_0r,\ (a,r)=1}.
\]
Because \(g_1^*=\mu g_0\mid P_1\),
\[
\boxed{r=\mu s,\qquad(a,\mu s)=1.}
\]
No condition \((\mu,s)=1\) is added.

Frozen primitivity gives \((u_0,P_1)=1\), hence the stronger production identity
\[
\boxed{g_0=(AW,P_1),\quad g_0\mid AW,\quad a=u_0\alpha,\quad \alpha=AW/g_0.}
\]
This exposes the R36 generator regression: R31 had enumerated \(g_0\mid AW\), while R36 relaxed to \(g_0\mid u_0AW\).

# Part III — TWELVE-ROOT AUTOPSY
The twelve R36 roots collapse to one primitive ray
\[
\boxed{(6,58,9,59)}.
\]
They split into two exact scaling templates:

- F_A(t): \(g_{0,sel}=25t\), \(P_1=90t\), so \(P_1/g_{0,sel}=18/5\notin\mathbb Z\). Six roots die at `g0 does not divide P1`.
- F_B(t): \(g_{0,sel}=t\), \(P_1=18t\), \(r=18\), \(\mu=5\), so \(\mu\nmid r\). Six roots die at `g1star does not divide P1`; here \((a,r)=3\).

Therefore the prompt's proposed universal integer mismatch gcd does not exist across all 12; half die before \(r\) exists.

# Part IV — NORMALIZED MASTER / SPHERE SYSTEM
With \(\Lambda=\mu\ell\), \(\ell=\tau\),
\[
\boxed{\bar b_1=\ell a},
\]
and MASTER becomes
\[
\boxed{a10^{m+n+g}D=\mu(WT+A10^nH)}.
\]
For
\[
L_N=aXYGK,
\]
\[
B_N=\mu(W+AYG)+aXYG,
\]
\[
C_N=\mu(WP_3+AYP_2),
\]
TC1+sphere is
\[
\boxed{(B_N^2-L_N^2)Q_0^2-2B_NC_NQ_0+C_N^2+L_N^2(P_2^2+P_3^2)=0.}
\]

# Part V — NORMALIZED DISCRIMINANT
\[
\boxed{\Delta_{norm}=4L_N^2\delta_{norm}},
\]
\[
\boxed{\delta_{norm}=C_N^2+(L_N^2-B_N^2)(P_2^2+P_3^2)}.
\]
If \(R^2=\delta_{norm}\), then
\[
Q_0=\frac{B_NC_N\pm L_NR}{B_N^2-L_N^2},
\]
\[
P_1=\frac{C_NL_N\pm B_NR}{B_N^2-L_N^2}.
\]
The true selector gate after the square condition is
\[
\boxed{\mu g_0(B_N^2-L_N^2)\mid C_NL_N\pm B_NR}
\]
plus \(\gcd(a,P_1/g_0)=1\). No global factorization proving this impossible was found.

# Part VI — SOURCE-FIRST NORMALIZED GENERATOR
The old R36 shell was reproduced exactly: 753,662 source coarse architectures, 8,922,022 F11 configurations, 297 square discriminants, 12 raw integer roots.

Correcting only the primitive \(g_0\mid AW\) allocation reduces the same shell to 73 square discriminants and 2 raw roots, with 0 selector-consistent roots. Adding full shape leaves only the F_B(1) raw root; it dies at \(\mu=5\nmid18\).

Expanded exact searches:

- q=1, (n2,n3)=(2,1), u0<=60: 25,929,293 configs; 30 squares after primitive prefilter; 1 raw root; 0 selector-consistent.
- q=2: 3,419,744 configs; 12 squares; 0 raw roots.
- q=3: 1,803,893 configs; 7 squares; 0 raw roots.
- q=5: 216,147 configs; 0 squares.
- q=7: 216,147 configs; 0 squares.
- q=1, (n2,n3)=(3,1), u0<=20: 67,546,418 configs; 40 squares; 0 raw roots.

Across expanded/stress lanes: 99,131,642 exact F11 configurations and zero selector-consistent roots.

# Part VII — CORRECTED SIMULTANEOUS LOCUS
No selector-consistent root reached post-basic legal, hence no searched architecture entered
\[
\mathscr T=\{\mathcal U_0\ne\varnothing,\ Q_-\le Q_+,\ Q_-\bar b_1D<Q_0\}.
\]
Bounded result: \(\mathscr T\cap\mathscr B_{R37}=\varnothing\). Global \(\mathscr T=\varnothing\) is NOT proved.

# Part VIII — TERMINAL RECTANGLE
Not triggered. No terminal pair exists in the R37 registries.

# Part IX — FULL RECONSTRUCTION
Not triggered because no terminal pair exists. The frozen documentary iff remains consistent; normalization introduced no hidden gate.

# Part X — FIFTEEN REQUIRED ANSWERS
1. Natural parameterization: \(M_0=g_0a,P_1=g_0\mu s,(a,\mu s)=1\); primitive strengthening \(g_0\mid AW,a=u_0AW/g_0\).
2. Yes, \(g_0=(M_0,P_1)\) is strictly equivalent to \(M_0=g_0a,P_1=g_0r,(a,r)=1\).
3. Yes, \(g_1^*=\mu g_0\mid P_1\) gives exactly \(r=\mu s\). No \((\mu,s)=1\) theorem.
4. Yes, base \(\bar b_1=\Lambda a/\mu=\tau a\).
5. Twelve roots: six have nonintegral \(r=P_1/g_0\); six have integral \(r=18\) but \(5\nmid18\).
6. No universal integer \((a,r)>1\) across all twelve; only the second family has \((3,18)=3\).
7. R36 twelve roots have one primitive sphere ray and two selector templates. The expanded n2=2,n3=1 raw locus has two primitive rays. Global finiteness of root templates is NOT proved.
8. Exact normalized discriminant is the \(\Delta_{norm}\) formula in Part V.
9. Square discriminant forcing selector mismatch is NOT proved globally; the exact stronger unresolved object is root-numerator divisibility.
10. No genuine selector-consistent integer root was found in the normalized searches. Raw roots exist but are rejected before legal root acceptance.
11. Post-basic legal roots: 0.
12. Corrected simultaneous locus points: 0 in searched cells; global emptiness not proved.
13. Genuine terminal pair: none.
14. Full original Strict-(A1) reconstruction: not triggered.
15. If 105 had to stop today, the last surviving object is the global normalized root-numerator divisibility/coprimality incidence (NRDG) on the full frozen source-complete cells, not a fake-selector or raw-discriminant locus.

# TERMINAL VERDICT
```text
GCD_NORMALIZATION_EQUIVALENCE=YES
R36_FAKE_G0_GENERATOR_REGRESSION=LOCATED_AND_FIXED
R36_CORRECTED_SHELL_SELECTOR_CONSISTENT_ROOTS=0
EXPANDED_R37_SELECTOR_CONSISTENT_ROOTS=0
SELECTOR_CONSISTENCY_EXTINCTION=NOT_PROVED
GCD_NORMALIZED_SIMULTANEOUS_LOCUS_EXTINCTION=NOT_PROVED
GENUINE_SELECTOR_CONSISTENT_SOURCE_MASTER_ROOT=NO_IN_SEARCHED_CELLS
MASTER_REFINED_TERMINAL_POSITIVE=NO
FULL_STRICT_A1_WITNESS_FOUND=NO
R37_GCD_NORMALIZED_SATURATION_CERTIFICATE=YES
R37_TERMINAL_ATTACK_FAILED
```

No global extinction certificate and no witness certificate are generated, because neither theorem was proved.
