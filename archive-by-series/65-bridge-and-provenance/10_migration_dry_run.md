# 75-R2 — P2 Migration Dry Run

This is a symbolic admissible configuration test, not a numerical existence proof.

## Input datum

Take one actual tuple
\[
\tau=(G=10^g,K=10^k,u,q),\qquad q>1,\ uq=G+1,
\]
satisfying the already-proved source equations and the split criterion \((-1,N_0)=0\). Choose one nonempty compact subarc
\[
J\Subset\mathscr I_{\eta,\tau}
\]
inside the required real component, and take the actual composite finite primitive projective open \(U_f^{\rm proj}\) from R14.

## Step 1 — model

Use \(\mathscr X_{{\rm sem},\tau}\), not raw \(\mathbb Z^3\). PASS.

## Step 2 — generic object map

Project
\[
X_\tau^\times\to C_\tau\simeq\mathbb P^1.
\]
PASS on the assumed split fibre.

## Step 3 — finite local data

Map source unit/gcd conditions to \(U_f^{\rm proj}\). The q² and M0 rows remain internal to the source model. PASS.

## Step 4 — primitive semantics

Ask the quantitative theorem for a primitive source **ray representative**, not a primitive final row. PASS at interface level.

## Step 5 — reciprocity

R14 weak approximation already gives a global rational projective point in \(U_f^{\rm proj}\times J\); hence the actual ray local conditions are reciprocity-compatible. PASS.

## Step 6 — moving real target

Use
\[
\Omega_\tau(G)=\{\eta\in\mathscr I_\eta,\;G\theta_\tau(\eta)<a<G\}.
\]
PASS as an exact source region.

## Step 7 — external quantitative theorem

- Cao–Xu: insufficient; finite/BM only.
- Huang Thm. 1.3: after freezing \(\tau\), it has almost the correct primitive+local+weight shape, but the verified v1 statement has a source-condition anomaly and in any case its constants/data are fixed while P2 couples \(B=G\) to a changing \(F,L,w\). **STOP: uniformity not supplied.**
- Kelmer–Yu Thm. 1.7: supplies fixed-form shrinking-sector exponent, but not the moving local congruence/source-lattice level. **STOP: uniformity/local-level bridge not supplied.**

Thus the migration fails at one specific interface rather than at source semantics.

## Step 8 — conditional completion with USSPAL

Assume USSPAL and choose \(x_0\in U_f^{\rm proj}\cap J\) satisfying USSPAL-CLEAR. Then R14 yields \(n\) coprime to \(10u\) in the exact radial interval. Put \(x=nx_0\). The source height inequalities give DIG3 + LOW; the source graph coordinates satisfy the semantic rows automatically; R20 inverse reconstruction returns the original source row.

## Dry-run verdict

```text
MODEL_INTERFACE=PASS
LOCAL_INTERFACE=PASS
PRIMITIVE_INTERFACE=PASS
RECIPROCITY_INTERFACE=PASS
ARCHIMEDEAN_REGION_INTERFACE=PASS
EXTERNAL_FIXED_DATA_THEOREM_INTERFACE=PASS
MOVING_FAMILY_UNIFORMITY=FAIL_CURRENTLY
RECONSTRUCTION_IF_USSPAL=PASS
UNIQUE_BLOCKER=UNIFORM_SOURCE_SECTOR_PRIMITIVE_APPROXIMATION
```
