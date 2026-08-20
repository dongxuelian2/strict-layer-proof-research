# 75-R2 — Targeted Quantitative Theorem Registry

Only theorem families adjacent to B3 were audited.

## Q1 — Huang, Quantitative strong approximation for ternary quadratic forms III

**Object:** fixed nondegenerate indefinite integral ternary form, punctured cone, primitive integral points, fixed congruence condition, fixed smooth compactly supported real weight.

**Value:** closest standard theorem to the full P2 interface. It proves that primitive + congruence + real weight on a ternary cone is a mature quantitative problem and exposes the Brauer/reciprocity correction term.

**Failure for direct import:**

1. the published arXiv v1 statement of Theorem 1.3 literally defines \(\Omega=8L\Delta\) and then assumes \(\Omega\mid L\); this source anomaly must be clarified before formal use;
2. even setting that issue aside, \(F,L,w\) are fixed while P2 needs a moving family \(F_\tau,L_\tau,w_\tau\) at the coupled scale \(B=G_\tau\);
3. no uniform dependence strong enough for the power-ten family is supplied in the verified statement.

**Verdict:** `BRIDGE_REQUIRED`, not a direct imported N2 theorem.

## Q2 — Kelmer–Yu, Theorem 1.7

**Object:** primitive rational points on a fixed rational ellipsoid/light cone; all-center shrinking sectors.

For ternary signature \((2,1)\), their parameter is \(n=1\), and the paper states that there is no exceptional pole for \(n=1,2\). The all-center range therefore reaches the natural \(r\asymp T^{-1/2}\) scale.

**Value:** gives the correct fixed-form shrinking-sector exponent and shows that B3 is a quantitative approximation problem, not merely a fixed-sector problem.

**Failure for direct import:** no prescribed moving source congruence level in Theorem 1.7, and constants depend on the fixed form. Source-height normalization also moves.

**Verdict:** `PARTIAL_SHRINKING_SECTOR_ENGINE`.

## Q3 — Cao–Xu, Theorem 1.2

**Object:** any smooth toric variety over a number field.

**Conclusion:** strong approximation with Brauer–Manin obstruction off the infinite places.

**Value:** qualitative finite-place/Brauer skeleton for the split punctured cone.

**Failure for B3:** the paper explicitly notes that its proof cannot force prescribed connected components at real places; it contains no moving radial-height theorem.

**Verdict:** `MIGRATED_FOR_QUALITATIVE_FINITE_LAYER_ONLY`.

## Q4 — Huang–Schindler–Shute, projective quadrics

The verified main high-dimensional shrinking-neighborhood theorem is formulated for projective quadrics of dimension at least two (ambient \(\mathbb P^n\) with \(n\ge3\)); the P2 base is a conic. **Dimension mismatch.**

**Verdict:** `REJECTED_FOR_P2`.

## Q5 — generic well-rounded homogeneous counting / toric height counting

These frameworks require uniform control of the family of regions, forms, lattices, or height functions. That is exactly the missing P2 bridge rather than a free input.

**Verdict:** reserve only.

## Best theorem stack

\[
\boxed{
\text{Cao--Xu qualitative BM skeleton}
+\text{Huang primitive local cone template}
+\text{Kelmer--Yu shrinking-sector exponent}
+\text{internal R14 radial multiplier}.}
\]

No member alone proves N2.
