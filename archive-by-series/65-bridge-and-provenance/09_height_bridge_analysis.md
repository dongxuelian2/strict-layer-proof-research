# 75-R2 — Source-Semantic Moving Height Bridge

## 1. Cheapest-route audit

### H1 — Explicit source parameterization

R20 supplies an integral degree-two parameterization after choosing one semantic integral basepoint. For a **fixed** fibre this can turn the ray problem into a two-variable lattice problem.

It does not close the family problem because the basepoint, parameterization coefficients, source-height distortion and finite unit level all move with \(\tau\). A uniform small-height basepoint theorem would already contain most of B3.

**Verdict:** useful local chart, not closure.

### H2 — Classical ternary quadratic counting

This is the closest route. Huang gives primitive local counting for a fixed cone; Kelmer–Yu gives shrinking-sector control for a fixed ternary light cone.

**Verdict:** best external engine after a uniform-family bridge.

### H3 — Toric parameter counting

The split punctured cone is toric, but the source integral model and decimal height are not a fixed toric model/height pair. Passing to monomial coordinates does not remove the moving source-height distortion.

**Verdict:** no gain over H2 at present.

### H4 — Homogeneous dynamics

Only needed for the quantitative shrinking-sector component. Kelmer–Yu already provides the relevant fixed-form exponent, so a broader mixing campaign is not justified until the precise family-uniformity gap is attacked.

## 2. Reduction to a smaller theorem

Choose a compact projective subarc
\[
J_\tau\Subset\mathscr I_{\eta,\tau}
\]
inside the correct real component and put
\[
\kappa_\tau(J)=\inf_{\eta\in J_\tau}\kappa_\tau(\eta)>0.
\]
Let \(\rho_\tau(J)\) be the intrinsic projective inradius after a normalized split-conic metric is chosen.

R14 implies that a primitive ray \(x_0\) with source height \(a_0\) is radially realizable whenever the exact multiplier interval contains an integer prime to \(10u\). A sufficient coarse condition is
\[
\frac{G}{a_0}\kappa_\tau(J)>j(10u).
\]
Thus it is enough to find a primitive source ray in \(U_f^{\rm proj}\cap J_\tau\) with
\[
a_0<\frac{G\kappa_\tau(J)}{j(10u)}.
\]

Kelmer–Yu's fixed-form theorem shows that, after normalizing a fixed split conic, an angular ball of radius \(\rho\) contains a primitive rational ray of height \(\ll C_Q\rho^{-2}\). This isolates the right exponent.

## 3. New explicit bridge theorem — USSPAL

### Uniform Source-Sector Primitive Approximation Lemma (USSPAL)

For every actual rationally split q>1 fibre \(\tau\), every nonempty admissible finite projective source open \(U_{f,\tau}^{\rm proj}\), and every compact interval \(J_\tau\Subset\mathscr I_{\eta,\tau}\), there exists a primitive source isotropic ray \(x_0\in U_{f,\tau}^{\rm proj}\cap J_\tau\) with
\[
 a_0(x_0)\le C_{\rm fam}(\tau,U_f)\,\rho_\tau(J)^{-2},
\]
where the family constant is explicit enough to verify, for at least one admissible \(J_\tau\),
\[
\boxed{
C_{\rm fam}(\tau,U_f)\rho_\tau(J)^{-2}
<\frac{G\kappa_\tau(J)}{j(10u)}.}
\tag{USSPAL-CLEAR}
\]

Equivalent counting formulations are allowed, provided their error terms imply the same existence inequality.

## 4. Why this is strictly smaller than N2

USSPAL no longer contains:

- conductor or M0 packet lifting;
- bad-reduction ruling classification;
- source reconstruction;
- primitive radial multiplier search;
- Brauer compatibility of the actual ray open;
- power-ten discreteness.

All those interfaces are already closed or separated. USSPAL asks only for **uniform quantitative distribution of primitive rational rays in a moving projective sector/local level**, with an explicit source-height distortion constant.

If USSPAL-CLEAR holds, R14 gives the multiplier and R20 reconstructs the source row. Therefore USSPAL implies N2.

## 5. M5-B certificate

```text
N2_REDUCED_TO=USSPAL_PLUS_EXPLICIT_CLEARANCE_INEQUALITY
REDUCTION_STRICTLY_SMALLER_THAN_ORIGINAL_FRONTIER=TRUE
M5_B=ACHIEVED
```

The lemma itself is not proved in R2.
