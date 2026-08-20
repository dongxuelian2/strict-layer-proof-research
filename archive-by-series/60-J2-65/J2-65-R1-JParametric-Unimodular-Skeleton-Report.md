# J2-65-R1 — J-Parametric Provenance × Reduced-Denominator Unimodular Envelope × Shadow-Dependency Reconstruction

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — A1-only — Exact Resonance R=0; temporary symbolic J only as a structural probe  
**Campaign:** 65 第一轮 / A1 统一终端线第二十六轮  
**Completion criterion:** `J=2 => empty`  
**Final status:**

\[
\boxed{\textbf{J2 OPEN}.}
\]

This round does **not** continue the R15 coefficient/bit/residual descent. Its task is source reconstruction, exact re-specialization, and dependency re-axiomatization.

---

## 1. Executive verdict

The central provenance result is a **correction** to the proposed full-u generalization.

The parameter J is genuinely pre-J2. It is first recovered in the Double Smith–Euclidean core as

\[
J=\Lambda_\beta/\delta_v,
\qquad
\delta_v=\gcd(v,\Lambda_\beta),
\]

with

\[
tM10^{n_3}-A_3=JZ.
\]

On Exact Resonance,

\[
S_3=\alpha JZ-M\widehat R
\]

specializes through \(\alpha=1,\widehat R=0\) to

\[
S_3=JZ,
\]

and the source then identifies

\[
\boxed{J=L_R>1.}
\]

A later resonance source gives the equivalent decimal-overlap form

\[
\boxed{J=\frac{G}{\gcd(G,\beta)}}
\]

(after its exact deflation dictionary). Thus J is structurally the **unabsorbed 2/5-primary decimal cofactor** left after the resonance denominator coefficient has absorbed its common decimal content. It is not originally introduced as a determinant parameter.

However, the general resonance source proves only

\[
\boxed{u_0\mid G+1,}
\]

where \(u_0\) is the reduced/cyclotomic radial denominator. It does **not** prove \(u\mid G+1\) uniformly. In fact the source-level surviving J=5 exceptional description explicitly permits

\[
u=5^r u_0,
\qquad u_0\mid11,
\]

in its \(g=1\) family. Therefore the J2 coordinate

\[
q=(G+1)/u
\]

is not a legal pre-specialization coordinate in the currently proved general resonance skeleton.

Hence, in the sense required by this campaign:

```text
J_PARAMETRIC_UNIMODULAR_CANDIDATE = FALSE_AS_SOURCE_THEOREM
```

That verdict means **the proposed provenance is false / not currently a theorem**; it does not claim that a future stronger theorem could never force the same formulas on all exact solutions.

The correct replacement is a reduced-denominator envelope.

---

## 2. Source-of-truth chain

```text
GENERAL_J_SOURCE_OF_TRUTH =
  strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md
  -> strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md
  -> strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md

J2_SPECIALIZATION_SOURCE =
  strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md
  -> A1_J2_NRSEC_Report.md
  -> A1_J2_CZDR_Report.md
```

The logical chain is:

1. **Double Smith–Euclidean core:** defines J before any J=2 specialization.
2. **Exact Resonance R=0:** gives \(S_3=JZ\) and identifies \(J=L_R\).
3. **RGCD / cyclotomic radial theorem:** gives \(u_0\mid G+1\) and a decimal-overlap dictionary for J.
4. **J=2 specialization:** proves \(s=d_*=\beta_0=1\), \(\beta=G/2\), \(n_3=g\), and crucially \(u=u_0\mid G+1\).
5. Only now define
   \[
   q=(G+1)/u,
   \quad A=2u+1,
   \quad B=2G+q.
   \]

This ordering is essential. Reversing steps 3 and 4 would silently assume away the general decimal overlap of u.

---

## 3. J-PROVENANCE TABLE

| identity / variable | general resonance? | J2 only? | exact provenance verdict |
|---|---:|---:|---|
| \(J=\Lambda_\beta/\delta_v\) | YES | no | source-defined in Double Smith–Euclidean core |
| \(S_3=\alpha JZ-M\widehat R\) | YES | no | exact pre-specialization affine defect identity |
| \(R=0\Rightarrow S_3=JZ\) | YES | no | \(\alpha=1,\widehat R=0\) in resonance |
| \(J=L_R>1\) | YES | no | exact resonance identification by 2/5 valuations |
| \(J=G/\gcd(G,\beta)\) | YES in later resonance chart | no | exact RGCD decimal-overlap dictionary |
| \(u_0\mid G+1\) | YES | no | cyclotomic radial denominator theorem |
| \(u\mid G+1\) | **NO as current general theorem** | YES after J=2 | J=2 proves \(u=u_0\); general source retains decimal-overlap factors |
| \(q=(G+1)/u\) | not recovered generally | YES | legal J2 coordinate after \(u=u_0\) |
| \(A=2u+1\) | not sourced generally | YES | frozen J2 normal form |
| \(B=2G+q\) | not sourced generally | YES | frozen J2 normal form |
| \(qA-B=2\) | not sourced generally | YES | exact J2 determinant identity |
| \(uB-GA=1\) | not sourced generally | YES | exact J2 Bézout identity |
| \(A_J=Ju+1\) | **FALSE as source theorem** | recovers A at J=2 if imposed | blocked before q/A construction by full-u issue |
| \(B_J=JG+q\) | **FALSE as source theorem** | recovers B at J=2 if imposed | q is not a general-resonance coordinate |

The full machine-readable version is `J2-65-R1-Provenance.tsv`.

---

## 4. Earliest failure of the proposed full-u lift

The candidate asked for

\[
A_J\stackrel?=Ju+1,
\qquad
B_J\stackrel?=JG+q,
\]

with

\[
uq=G+1.
\]

The **earliest failure is not a determinant computation**. It occurs one level earlier:

\[
\boxed{\text{general resonance proves }u_0\mid G+1,\ \text{not }u\mid G+1.}
\]

Writing the source Smith decomposition schematically as

\[
u=\gamma u_0,
\]

one would have

\[
\frac{G+1}{u}=\frac{q_0}{\gamma},
\qquad
q_0:=\frac{G+1}{u_0}.
\]

There is no current source theorem forcing \(\gamma=1\) before J=2. Thus the proposed q may fail even to be an integer general-resonance coordinate. This is the exact provenance obstruction.

Consequently:

```text
A_J_EQUALS_Ju_PLUS_1 = FALSE_AS_SOURCE_THEOREM
B_J_EQUALS_JG_PLUS_q = FALSE_AS_SOURCE_THEOREM
GENERAL_J_RCE = NOT_RECOVERED
```

---

## 5. NEW THEOREM — Reduced-Denominator Unimodular Envelope

Although the full-u candidate is not source-valid, the source theorem \(u_0\mid G+1\) gives a canonical complementary divisor

\[
\boxed{q_0:=\frac{G+1}{u_0}\in\mathbb Z_{>0}.}
\]

Now define, **as a new structural envelope** rather than as recovered old coordinates,

\[
\boxed{\bar A_J:=Ju_0+1,}
\]

\[
\boxed{\bar B_J:=JG+q_0.}
\]

Then the complementary-divisor relation \(u_0q_0=G+1\) gives exactly

\[
\boxed{q_0\bar A_J-\bar B_J=J,}
\tag{E-DET-J}
\]

and

\[
\boxed{u_0\bar B_J-G\bar A_J=1.}
\tag{E-BEZ-J}
\]

Therefore

\[
\boxed{
\bar M_J=
\begin{pmatrix}
G&u_0\\
\bar B_J&\bar A_J
\end{pmatrix}
\in GL_2(\mathbb Z),
\qquad
\det\bar M_J=-1.
}
\tag{E-GL2}
\]

This is exact-symbolically certified in `J2-65-R1-UnimodularSkeleton-symbolic.py`.

### 5.1 Exact inverse

Because the determinant is -1,

\[
\boxed{
\bar M_J^{-1}
=
\begin{pmatrix}
-\bar A_J&u_0\\
\bar B_J&-G
\end{pmatrix}.
}
\]

Both left and right inverse products are symbolically verified.

### 5.2 Primitive consequences

The Bézout identity

\[
u_0\bar B_J-G\bar A_J=1
\]

immediately implies

\[
\boxed{\gcd(G,u_0)=1.}
\]

It also implies

\[
\boxed{\gcd(\bar A_J,\bar B_J)=1,}
\]

since any common divisor of \(\bar A_J,\bar B_J\) divides the displayed integer 1. Thus the two rows and two columns of the envelope define primitive lattice directions.

### 5.3 Why this is not merely decorative

The envelope cleanly separates two mechanisms that the J2 chart had fused:

- **cyclotomic complementarity:** \(u_0q_0=G+1\);
- **residual decimal index:** J.

The J2 determinant pair is the case where the source itself proves that the reduced denominator is the full denominator coordinate: \(u_0=u\). That fact, not a formal replacement \(2\mapsto J\), is what allows the envelope to become the actual J2 coordinate system.

The envelope does **not** by itself derive the RCE variables \((N,Z,a_3,t,\mathcal X,D_2)\). Those also encode radial digits, primitive recovery, and Euclidean normalization. Therefore the inverse matrix is a genuine lattice coordinate map, but the existing RCE is not merely its coordinate transform.

---

## 6. Exact J=2 re-specialization

The source-proved J2 resonance state has

\[
J=2,
\qquad
u_0=u,
\qquad
q_0=q=(G+1)/u.
\]

The envelope then gives

\[
\bar A_2=2u+1=A,
\]

\[
\bar B_2=2G+q=B.
\]

Therefore

\[
qA-B=2,
\]

\[
uB-GA=1,
\]

and

\[
\det\begin{pmatrix}G&u\\B&A\end{pmatrix}=-1.
\]

All four identities are symbolically checked, not asserted by inspection.

Thus:

```text
J2_RESPECIALIZATION = PASS
```

The important logical direction is:

\[
\boxed{
\text{general resonance }(J,u_0)
\to
\text{canonical envelope}
\xrightarrow[J=2]{u_0=u}
\text{actual J2 determinant chart}.
}
\]

It is **not**

\[
\text{J2 chart}\to\text{guess }2\mapsto J.
\]

---

## 7. General-J RCE audit

No source was recovered that gives a pre-J2 RCE of the form requested in the prompt.

The recovered J2 derivation is exact:

\[
2Aa_3=q(G-1)Z-N,
\tag{RCE1}
\]

then define

\[
\boxed{t=q^2Z-4a_3,}
\tag{TDEF}
\]

and use

\[
\boxed{2Aq=4(G-1)+2(q+4)}
\]

(which follows from the J2 relations) to derive

\[
(G-1)t=2(q+4)a_3+qN,
\tag{RCE2}
\]

\[
q(q+4)Z=At-2N.
\tag{RCE3}
\]

`J2-65-R1-UnimodularSkeleton-symbolic.py` verifies RCE2 and RCE3 from RCE1+TDEF+the J2 determinant relation.

But the provenance enters **after** J2 specialization. There is no source-legal step replacing

\[
q+4
\]

by

\[
q+2J.
\]

Therefore:

```text
GENERAL_J_RCE_NOT_RECOVERED
q_PLUS_4_EQUALS_q_PLUS_2J = NOT_RECOVERED
```

and no `J2-65-R1-JParametric-RCE-symbolic.py` is generated.

---

## 8. Audit of the 2s and 4s in J2

The main result of this audit is negative but important:

\[
\boxed{\text{not every 2 in the J2 chart is J.}}
\]

| occurrence | provenance class | verdict |
|---|---|---|
| the statement \(J=2\) | J-dependent | literal specialization |
| \(c_R=1\), \(\beta=G/2\), source equality \(u=u_0\) | J-dependent specialization consequences | obtained only after J=2 analysis |
| \(A=2u+1\), \(B=2G+q\) | specialization artifact | actual J2 coordinates; **not** source-proved by general \(A_J,B_J\) |
| \(qA-B=2\) | specialization artifact | actual J2 determinant difference |
| \(uB-GA=1\) | lattice/Bézout | RHS 1 is structural; coefficient 2 is inside the J2 A,B definitions |
| root quadratic term \(-2uKD_2x\) | Pythagorean/quadratic fixed 2 | part of exact root geometry, not J |
| \(2X-z=uj\), hence \(X=(Z+uN)/2\) | linear/parity fixed 2 | recovered inside J2 radialization; no general-J lift proved |
| RCE1 leading \(2Aa_3\) | J2 radial algebra / fixed 2 | not certified as J |
| \(t=q^2Z-4a_3\) | Euclidean normalization | the 4 is built into the J2 remainder definition |
| \(q+4\) in RCE2/RCE3 | J2 Euclidean-algebra artifact | produced from TDEF plus J2 \(Aq\) identity; **not** proven \(q+2J\) |
| factors 4,8 in cleared root / \(L/8\) normalization | decimal/root normalization | not J |

Therefore the correct statement is not “replace every 2 by J”, but:

> J=2 changes the **resonance denominator content**, which then makes a particular determinant chart legal. Other 2s and 4s come from quadratic polarization, parity, Euclidean remainder definitions, or decimal clearing.

---

## 9. Shadow / Dependency Dictionary

The A–E categories requested in the prompt are used below. Some objects naturally carry a primary and a secondary tag.

| object | class | exact dependency verdict |
|---|---|---|
| full exact root \(Q(x)=0\) | **D / MASTER** | independent modulo old carry ideal; master root equality |
| \(Q\bmod q\) | **A + C** | modular shadow; R7 shows it degenerates to old RCE square and is consumed |
| \(Q\bmod u\) | **A** | modular shadow of full root |
| U-SQ \(x^2\equiv Z^2\pmod u\) | **A + D** | exactly \(Q\bmod u\); not second root equation, but not consumed by carry ideal |
| \(Q\bmod A\) | **A** | \(D_2(Kx+Z)\) mod A |
| A-ROOT | **D / primitive projection** | equals the Q-mod-A root in nondegenerate case; stronger when \(\gcd(D_2,A)>1\) |
| A²/A³ lift | **D** | Taylor/Hensel expansion of Q plus primitive A-root, not carry information |
| decimal root | **B + C (partial)** | pre-root modular information feeding floor/carry; not an independent full equality |
| RCE | **B + C** | pre-root structural; included in carry saturation |
| DCDC | **B + C** | pre-root structural; included in carry saturation |
| tail quotient | **B + C** | pre-root structural; consumed by R8–R11 chain |
| floor carry | **C** | old carry layer |
| \(\lambda\), \(\gamma\), \(\zeta\) | **C** | retired carry coordinates |
| second / third residual | **C** | eliminated/definitional after projection; no new independent relation |
| R11 constant-term route | **C** | exactly old carry: \(D_u=\gamma\), \(\mathcal C\propto\Gamma\) |
| R12 \(P_B\) | **D** | degree 4 in G; independent modulo carry ideal |
| R12 \(P_H\) | **D** | degree 4 in G; independent modulo carry ideal |
| R12 \(P_R\) | **D** | degree 7 in R; independent modulo carry ideal |
| R12 \(P_{K1}\) | **D** | degree 7 in R; special reverse normalization; independent modulo carry ideal |
| LOW | **E** | root/digit inequality, not carry consequence |
| UP | **E** | complementary-factor positivity inequality, not carry consequence |
| \(\gcd(Z,u)=1\) | **E** | primitive recovery |
| \(\gcd(x,u)=1\) | **E** | primitive support consequence; not carry consequence |
| common-U primitive recovery | **E** | primitive semantic gate, not carry consequence |

Two distinctions are now permanent:

\[
\boxed{
\text{U-SQ is not an independent root equation}
}
\]

but simultaneously

\[
\boxed{
\text{U-SQ is independent modulo the R8--R11 carry ideal}.
}
\]

Likewise, R12's four polynomials are not four independent physical root equations; they are four nonzero carry-saturated **charts/remainders of the same full-root layer**.

---

## 10. Dependency DAG

The machine-readable graph is written to

```text
J2-65-R1-DependencyDAG.tsv
```

with columns

```text
source,target,relation,scope,provenance
```

and relation alphabet

```text
DERIVES
SPECIALIZES_TO
MODULAR_SHADOW
USES
CONSUMED_BY
INDEPENDENT_MOD_IDEAL
```

`J2-65-R1-DependencyDAG.py` verifies all mandatory corrections:

```text
R11_CONSTANT_NOT_INDEPENDENT_ROOT = PASS
U_SQ_NOT_INDEPENDENT_FULL_EQUATION = PASS
R12_ALL_INDEPENDENT_MOD_CARRY_IDEAL = PASS
LOW_UP_NOT_CARRY_CONSEQUENCE = PASS
```

Thus the graph cannot silently recreate the historical independence mistakes.

---

## 11. Minimal independent gate basis for J2

After quotienting historical auxiliary variables, the current J2 information is best organized into **four** mathematically distinct classes, not dozens of named residues.

### S — Structural / pre-root variety

\[
\boxed{\mathcal S_{\rm structural}}
\]

contains:

- Exact Resonance J=2 specialization;
- \(u q=G+1\), \(A=2u+1\), determinant/Bézout chart;
- RCE and DCDC;
- tail/floor/carry reconstruction and all already-consumed residual definitions.

All R8–R11 carry coordinates live inside this class after elimination.

### E — One full-root equality

\[
\boxed{\mathcal E_{\rm full-root}: Q(x)=0}
\]

or, after carry saturation, its branch charts

\[
P_B,
P_H,
P_R,
P_{K1}.
\]

U-SQ and \(Q\bmod q\) are shadows of this one equality, not new equalities.

### I — Primitive / common-U gate

\[
\boxed{\mathcal I_{\rm primitive}}
\]

contains primitive recovery, common-U coprimality, \(\gcd(Z,u)=1\), \(\gcd(x,u)=1\), and the extra strength of A-ROOT on derivative-content-degenerate components.

### W — Digit / interval / positivity gate

\[
\boxed{\mathcal W_{\rm digit/interval}}
\]

contains LOW, UP, actual digit windows, and inherited Archimedean/deficiency inequalities.

Therefore the answer to “how many genuinely independent information types remain?” is:

\[
\boxed{4\text{ classes}.}
\]

This does **not** mean four scalar equations. It means four non-redundant logical sources of information after the historical coordinate quotient.

---

## 12. R12 four-polynomial interface and master-root feasibility

### 12.1 Why boundary/high use G

Boundary and high retain the natural exponent variable

\[
G=10^g.
\]

After branch-specific tail reconstruction and deterministic floor/carry substitution, the saturated full root becomes a degree-4 polynomial in G.

### 12.2 Why reverse uses R

Reverse fixes the low-k decimal scale \(K=10^k\) and writes

\[
G=KR,
\qquad
R=10^r.
\]

After removing structural powers of R, the natural residual power-of-ten equation is degree 7 in R. Thus the change from G to R is a **monomial chart adapted to reverse scaling**, not evidence by itself of a separate algebraic component.

### 12.3 Where branch splitting first occurs

The split occurs **before** the final R12 primitive polynomial:

1. high/boundary/reverse have different L/K/G scale relations;
2. the deterministic floor/carry candidate x is reconstructed branch-wise;
3. reverse substitutes \(G=KR\) and removes structural R powers;
4. \(k=1,b=0\) has a separately legal normalization, so \(P_{K1}\) is not obtained by blindly substituting into the generic reverse formula.

Therefore the current evidence points primarily to

\[
\boxed{\text{monomial/floor-normalization chart splitting},}
\]

not to a proved decomposition of the original full-root variety into four irreducible components.

### 12.4 Common pre-polynomial

A common pre-polynomial unquestionably exists at the unsaturated level: the exact root quadratic (or its cleared R12 normalization), with G and K retained before substituting the branch floor candidate.

What is **not** yet proved is that carry saturation and elimination commute with all four branch substitutions so as to produce one single polynomial \(\mathcal P(G,K)\) whose literal chart restrictions are exactly \(P_B,P_H,P_R,P_{K1}\).

The obstruction is not polynomial size alone. It is the presence of moving parameters and piecewise floor/carry normalizations. In particular, the R12/R15 history proves that a fixed residue cell does not freeze \((e,t,\gamma)\) as coefficients.

Hence:

```text
MASTER_BIVARIATE_ROOT_FEASIBILITY = PARTIAL
```

### 12.5 What may be eliminated next

A 65-R2 construction should first eliminate only variables already known to be structural/definitional under the common pre-root ideal. It should **retain** moving parameters whose elimination would require dividing by an unproved nonzero factor. The safe order is:

1. keep \((G,K)\) as monomial coordinates;
2. keep the exact cleared root before floor specialization;
3. saturate branch-independent structural/RCE/DCDC relations;
4. externalize floor/carry strata as charts, not as a new residual ladder;
5. compute the saturated Newton support / initial forms;
6. only then compare the four R12 chart polynomials.

---

## 13. R15 frontier frozen unchanged

This round does not claim closure from the abstraction.

Frozen after R15:

\[
\boxed{\textbf{HIGH=OPEN}},
\]

\[
\boxed{\textbf{BOUNDARY=OPEN}},
\]

\[
\boxed{\textbf{REVERSE }(k,q)=(1,7),(2,7),(2,11)\textbf{ OPEN}},
\]

\[
\boxed{\textbf{q=1 positive/negative OPEN}},
\]

\[
\boxed{\textbf{FULL J2 OPEN}}.
\]

Also frozen:

\[
\text{Boundary/High actual root}\Rightarrow4\mid e,
\]

and in large high,

\[
g\ge9\Rightarrow8\mid e.
\]

No use is made of the false stronger assumptions \(\gcd(x,10)=1\), absolute reverse-depth bounds from parity+TQR+LOW, fixed-coefficient periodic fibres, or local killer-prime searches.

The q=1 negative frontier remains the 24 exact residue-constrained Pell/norm orbit problems; it is not attacked here.

---

## 14. New structural theorem ledger

### NEW PROVED / DERIVED

1. **J provenance theorem:** J is pre-specialization Double-Smith data and equals \(L_R\) on resonance.
2. **Full-u candidate provenance failure:** current general resonance does not supply \(u q=G+1\); the legal general coordinate is \(u_0\).
3. **Reduced-Denominator Unimodular Envelope:**
   \[
   \bar A_J=Ju_0+1,
   \quad
   \bar B_J=JG+q_0,
   \quad
   \det\bar M_J=-1.
   \]
4. **Exact J2 realization:** source J=2 gives \(u_0=u\), so the envelope becomes the actual \(A,B\) chart.
5. **RCE provenance correction:** general-J RCE is not currently sourced; \(q+4=q+2J\) is not promoted.
6. **Shadow Equivalence:** U-SQ is exactly Q mod u, while Q mod q is consumed by old RCE/carry.
7. **Four-class minimal gate basis:** structural + full-root + primitive + digit/interval.
8. **Master-root feasibility:** PARTIAL, with branch split located at monomial/floor normalization rather than proved algebraic-component splitting.

### NOT PROVED / REJECTED

- source theorem \(A_J=Ju+1\) on full u;
- source theorem \(B_J=JG+q\) on full u;
- general \(u q=G+1\);
- general-J RCE;
- \(q+4=q+2J\);
- single saturated bivariate master polynomial already constructed;
- any new J2 branch closure.

---

# 15. Seven terminal questions

## Q1. What is J structurally in Exact Resonance?

\[
\boxed{
J\text{ is the residual 2/5-primary decimal/Smith cofactor left after common overlap is removed.}
}
\]

Source-equivalently it appears as \(\Lambda_\beta/\delta_v\), becomes \(L_R\) on R=0, and in the later RGCD chart is \(G/\gcd(G,\beta)\). Its operational role is to measure the remaining decimal divisibility in \(S_R=JZ\) and to bound the integerized resonance mantissa. It was **not** originally a determinant parameter.

## Q2. Do A=2u+1 and B=2G+q come from source-proved A_J=Ju+1, B_J=JG+q?

\[
\boxed{\textbf{No, not as a currently proved general-resonance theorem.}}
\]

The earliest obstruction is that general resonance only gives \(u_0\mid G+1\). The actual J2 source later proves \(u=u_0\). A reduced-denominator envelope \(\bar A_J=Ju_0+1,\bar B_J=JG+q_0\) is valid and re-specializes exactly, but this is a new derived envelope, not recovered provenance for full u.

## Q3. Is uB-GA=1 a general unimodular theorem?

For the **actual full-u variables A,B**, no current source proves that statement generally.

For the source-valid reduced denominator, yes:

\[
\boxed{u_0\bar B_J-G\bar A_J=1}
\]

is an exact general-resonance envelope theorem. J2 realizes it with \(u_0=u\), giving the familiar \(uB-GA=1\).

## Q4. Which J2 2s/4s come from J=2?

Only the specialization-specific denominator/determinant chart may be attributed to the J=2 layer. The quadratic/root 2s, the parity halves, the \(4a_3\) in the Euclidean t-definition, and therefore the current \(q+4\) algebra are not source-proved replacements of J. In particular

\[
\boxed{q+4\ne\text{ currently proved }q+2J.}
\]

## Q5. What is the real dependency DAG among RCE/DCDC/U-SQ/A-root/carry/full-root?

At the top:

\[
\mathcal S_{\rm structural}
\quad\text{and}\quad
Q(x)=0
\]

are separate layers. RCE/DCDC/tail/floor/carry are in the structural/pre-root chain. Q mod q is a consumed modular shadow. U-SQ is Q mod u: not a second root equation, but not consumed by carry. A-root is a primitive projection of Q mod A and is strictly stronger on content-degenerate A-components. R12's P-polynomials are nonzero images of Q after quotienting the carry ideal. LOW/UP and primitive/common-U are external gates.

The exact machine graph is `J2-65-R1-DependencyDAG.tsv`.

## Q6. What is the minimal independent gate basis after quotienting historical auxiliaries?

\[
\boxed{
\mathcal S_{\rm structural}
+
\mathcal E_{\rm full-root}
+
\mathcal I_{\rm primitive}
+
\mathcal W_{\rm digit/interval}.
}
\]

Thus there are **four information classes**, not a ladder of lambda/gamma/zeta/residual variables.

## Q7. Should P_B,P_H,P_R,P_K1 be lifted in 65-R2 to one (G,K)-bivariate master root / Newton-polytope object?

\[
\boxed{\textbf{YES as the next research direction, with feasibility = PARTIAL.}}
\]

There is a common exact pre-root quadratic and the G/R distinction is largely a monomial-chart choice. But the four R12 outputs are not yet proved to be literal restrictions of one already-saturated polynomial because floor/carry normalization and the special K1 legality split occur before final saturation. The correct next object is therefore the **pre-floor, carry-saturated bivariate master root normal form**, followed by its saturated Newton polytope and chart comparison—not another coefficient-bit or residual descent.

---

# 16. Terminal status and unique next target

No present open branch is closed by the new envelope alone.

\[
\boxed{\textbf{J2 OPEN}.}
\]

The unique highest-value object for 65 第二轮 is

\[
\boxed{
\textbf{Bivariate Master Root Polynomial}
\times
\textbf{Saturated Newton Polytope},
}
\]

constructed **before branch-specific floor specialization**, with \((G,K)\) retained and with R12's four polynomials treated as candidate charts to be derived—not assumed.

The campaign should not return to coefficient-bit ladders, new residuals, or fixed-q prime hunting unless that master object itself later forces such a local specialization.

---

## 17. Artifact audit

Generated and executed:

```text
J2-65-R1-UnimodularSkeleton-symbolic.py
J2-65-R1-DependencyDAG.py
```

Generated:

```text
J2-65-R1-JParametric-Unimodular-Skeleton-Report.md
J2-65-R1-UnimodularSkeleton-symbolic.py
J2-65-R1-DependencyDAG.py
J2-65-R1-DependencyDAG.tsv
J2-65-R1-Provenance.tsv
J2-65-R1-certificate.txt
J2-65-R1-execution.log
```

Not generated, deliberately:

```text
J2-65-R1-JParametric-RCE-symbolic.py
```

because `GENERAL_J_RCE=NOT_RECOVERED`.
