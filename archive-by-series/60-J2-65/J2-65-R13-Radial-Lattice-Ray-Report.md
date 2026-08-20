# J2-65-R13 — Radial Homogenization × Saturated Source Lattice × Primitive Ray × Multiplier Interval

**Scope:** Strict Layer — A1-only — Exact Resonance \(R=0\) — \(J=2\) — \(q>1\) only  
**Status:** **J2 OPEN**

## Executive verdict

R13 succeeds at the requested recompression through the source lattice, but the
`FREE_MULTIPLIER` branch is **not** the actual source verdict.

The decisive source-global gate missed by a LOW/UP-only audit is the actual third-digit window
\[
\boxed{\frac G{10}\le a_3<G.}
\]
For \(v=n v_0\), this becomes
\[
\boxed{\frac G{10}\le n a_{3,0}<G,}
\]
so a genuine radial upper endpoint survives.  Therefore the multiplier cannot be retired.

The correct q>1 frontier after R13 is
\[
\boxed{
\text{primitive integral isotropic source-lattice ray}
\times
\text{one reduced-residue multiplier interval}
\times
\text{projective digit cone}
\times
\text{power-of-ten base}.
}
\]

No Hermitian/continuant layer is reopened.

## 1. Exact radial homogenization

Reload the R2 source reconstruction and the R7 decomposition
\[
Q_{\rm sat}=G\,P+K\,S,
\]
where
\[
P=A_c\alpha^2+B_c\alpha T+C_cT^2+D_cY^2,\qquad
S=E_c\alpha Y+F_cTY.
\]
Set \(\alpha=ds,\ T=dt,\ Y=dx\).  Since \(P,S\) are quadratic homogeneous,
the common \(d^2\) cancels and the actual fibre is
\[
\boxed{
Q_{\rm rad}(s,t,x)
=
A_cs^2+B_cst+C_ct^2+D_cx^2+\frac KGx(E_cs+F_ct)=0.
}
\]
Putting \(r=t/s,\ y=x/s\) recovers R7 exactly after division by \(s^2\).

`J2-65-R13-RadialHomogenization.py` derives all six coefficients from the R2
source formulas rather than guessing them and regresses
\[
D_c=Gq^4(q+4)^2(2G+q+2)c^2
\]
and the exact R7 factor of \(E_c\).

## 2. Source integrality compression

The full source replay requires integer source objects, but their integrality is highly redundant.
Use RCE1 and TDEF in the direction
\[
\boxed{N=q(G-1)Z-2Aa_3,\qquad t=q^2Z-4a_3.}
\]
If \(Z,a_3\in\mathbf Z\), then \(N,t\in\mathbf Z\).  On the actual J2 locus
\(G\) is even and \(q,u,A\) are odd, so the parity halves defining
\(X,h,m\) are automatic; \(D_2,r_{\rm rem},F\) are then integral by definition.

Thus the independent source-integrality generators reduce to
\[
\boxed{\alpha=ds,\quad x,\quad Z,\quad a_3.}
\]
All other recovered integer quantities are derived rows of the same rational linear map
(except the quadratic \(F\), which is derived after linear reconstruction).

## 3. One saturated source lattice

With integer coordinates \((Z,a_3,x)\),
\[
N=q(G-1)Z-2Aa_3,\qquad t=q^2Z-4a_3
\]
and
\[
Gs=qcN-Bt=h_ZZ+h_aa_3,
\]
where
\[
\boxed{h_Z=q^2(c(G-1)-B),\qquad h_a=4B-2qcA.}
\]
The remaining condition \(\alpha=ds\in\mathbf Z\) is the single composite congruence
\[
\boxed{G\mid d(h_ZZ+h_aa_3).}
\]
Hence \(\Lambda_{\rm src}\) is rank 3 without any denominator tree.

Let
\[
\delta=\gcd(G,dh_Z,dh_a),\qquad M=G/\delta.
\]
The congruence quotient is cyclic, so its Smith factors are
\[
\boxed{1\mid1\mid M.}
\]
An explicit basis is recorded in `J2-65-R13-SourceLatticeBasis.txt`.

## 4. Power-of-ten source-lattice collapse

Modulo \(G\),
\[
h_Z\equiv-2q^4(q+4),
\qquad
h_a\equiv-2(q+2)^3(q+4).
\]
On the live q>1 locus both \(q\) and \(q+2\) are ten-units.  Therefore, as a
single whole-modulus gcd identity,
\[
\boxed{\delta=\gcd(G,2d(q+4)).}
\]
No \(2/5\)-valuation split is used.

Consequently
\[
\boxed{M=\frac{G}{\gcd(G,2d(q+4))}}
\]
is the unique nontrivial saturation Smith factor and
\[
\boxed{\det B_\Lambda=\frac{2q^2(q+4)c}{\delta}.}
\]

## 5. Integral ternary form

Pull the homogeneous conic to \(w\in\mathbf Z^3\) by \(v=B_\Lambda w\).
The uniform clearing
\[
Q_{\rm clear}(w)=d^2G\,Q_{\rm rad}(B_\Lambda w)
\]
has integral coefficients.  Divide by its one composite content \(C_Q\) to obtain
\(Q_{\rm prim}\).

With Gram convention \(\mathrm{Gram}(Q)=\mathrm{Hess}(Q)/2\),
\[
\det\mathrm{Gram}(Q_{\rm prim})
=
\frac{
4d^6G^4q^{10}(G+1)^2(q+4)^6(2G+q+2)c^6\Delta_{\rm fib}
}{
\delta^2C_Q^3
},
\]
where
\[
\Delta_{\rm fib}=R(G,q)-4K^2G^2(G+1)^2.
\]
R7 already proves \(\Delta_{\rm fib}\ne0\) and signature \((2,1)\) on every actual q>1 fibre.

## 6. Canonical primitive-ray theorem

Choose the basis \(B_\Lambda\).  Every nonzero lattice point is \(B_\Lambda w\) with
\(w\in\mathbf Z^3\).  Dividing \(w\) by the gcd of its three coordinates gives a unique
primitive generator up to sign.  Positive orientation fixes the sign.  Thus for every
positive rational ray meeting \(\Lambda_{\rm src}\),
\[
\boxed{\ell\cap\Lambda_{\rm src}=\{nv_0:n\ge1\}.}
\]

## 7. Primitive-gcd factorization

For \(v=nv_0\),
\[
\gcd(nx_0,u)=1
\iff
\gcd(n,u)=\gcd(x_0,u)=1,
\]
and identically for \(Z_0\).  Hence the requested factorization is exact.

Moreover the inherited U-SQ shadow descends, after \((n,u)=1\), to
\[
\boxed{x_0^2\equiv Z_0^2\pmod u.}
\]
Therefore \(Z_0\) being a unit modulo \(u\) already forces \(x_0\) to be a unit.
The x-unit ray condition is redundant after U-SQ + Z-unit, although the multiplier
condition \((n,u)=1\) remains.

## 8. Radial homogeneity audit

The branch-independent global source gates recovered without reopening old charts are:

- projective: orientation, \(ct-s>0\), UP \(ALx<8uD_2\), and the common source positivity bundle;
- radial lower: LOW \(nx_0>AG/10\);
- radial interval: the actual third-digit window \(G/10\le n a_{3,0}<G\);
- arithmetic nonhomogeneous: primitive \(u\)-coprimality and inherited source ten-unit bundle.

Old sign/high/boundary/reverse deficiency inequalities are **not** silently reimported.

Thus
\[
\boxed{\texttt{GENUINE\_RADIAL\_UPPER\_GATE=PRESENT}.}
\]

## 9. Multiplier interval

For a ray with \(x_0>0,\ a_{3,0}>0\),
\[
n_{\min}
=
\max\!\left(
\left\lfloor\frac{AG}{10x_0}\right\rfloor+1,\,
\left\lceil\frac{G}{10a_{3,0}}\right\rceil,\,
1
\right),
\]
\[
n_{\max}
=
\left\lceil\frac{G}{a_{3,0}}\right\rceil-1.
\]
The source ten-unit bundle forces \((n,10)=1\), while the primitive gate forces
\((n,u)=1\). Since \(u\) is a ten-unit,
\[
\boxed{(n,10u)=1.}
\]
Hence the exact remaining multiplier object is one finite interval intersected with the
reduced residues modulo \(10u\).

The correct whole-modulus gap object is therefore
\[
\boxed{j(10u)}
\]
(Jacobsthal's function), not \(j(u)\).  No prime factor decomposition is performed.

## 10. Primitive modulo-u locus

Using the canonical congruence-lattice basis,
\[
Z_0=Mw_1+\rho w_2,\qquad a_{3,0}=w_2,\qquad x_0=w_3.
\]
Thus
\[
\Lambda_{\rm src}/u\Lambda_{\rm src}\cong(\mathbf Z/u\mathbf Z)^3
\]
with two explicit composite linear functionals \(Z_0,x_0\).
No whole-modulus incompatibility between isotropy, the digit cone, and \(Z_0\in
(\mathbf Z/u\mathbf Z)^\times\) is proved in R13.  This remains a genuine next obstruction.

## 11. Universal section / torsor audit

R7 proved that the generic source conic has no universal rational section over the symbolic base.
A lattice basis change cannot create a rational section that the projective conic lacks.
Therefore
\[
\boxed{\texttt{SOURCE\_LATTICE\_UNIVERSAL\_ISOTROPIC\_SECTION=FALSE}.}
\]
No fake universal binary parameterization is generated.

## 12. Exact information-loss invariant

R12's one-dimensional radial kernel becomes precise only **after** restoring
\(\Lambda_{\rm src}\): on each rational ray it is the positive lattice index \(n\) relative to
the canonical primitive generator \(v_0\).

So the sharpened statement is:

\[
\boxed{
\text{source lattice + primitive ray}
\quad+\quad
\text{positive multiplier }n.
}
\]

Bare Hermitian moduli do not know \(v_0\), because they also forgot the source-lattice embedding.
After that embedding is restored, the remaining one-dimensional loss is exactly the multiplier.

Because DIG3 gives an upper endpoint, that multiplier is not semantically disposable.

## 13. Discriminant-module audit

The raw rational lattice \(\Lambda_{\rm src}\subset\mathbf Q^3\) has no canonical finite
quotient \(\Lambda^\vee/\Lambda\) under the standard dot product unless integrality is specified.
The canonical arithmetic object here is the integral quadratic lattice of \(Q_{\rm prim}\).
Using its Hessian bilinear form gives a finite discriminant module whose order is
\(|\det\mathrm{Hess}(Q_{\rm prim})|\); its invariant factors are obtained by one composite SNF.

R13 does not prove that this module kills the primitive isotropic locus:
`SOURCE_DISCRIMINANT_MODULE_OBSTRUCTION=NOT_ESTABLISHED`.

## 14. Fifteen requested answers

1. **Q1:** YES. Exact homogeneous ternary quadratic cone obtained.
2. **Q2:** YES. All source integrality is controlled by finitely many rational linear forms; after saturation four generators suffice.
3. **Q3:** YES. They form a rank-3 saturated lattice.
4. **Q4:** Saturation SNF is \(1|1|M\), \(M=G/\gcd(G,2d(q+4))\); lattice determinant/covolume is \(2q^2(q+4)c/\delta\). Quadratic determinant is the formula in §5.
5. **Q5:** YES. Unique canonical primitive generator up to sign; positive orientation fixes it.
6. **Q6:** YES. Every integral radial lift is exactly \(nv_0\).
7. **Q7:** YES. Exact ray + multiplier coprimality factorization; U-SQ further makes x-unit redundant once Z-unit holds.
8. **Q8:** LOW radial-lower; UP projective; DIG3 radial-interval; source ten-unit gates arithmetic nonhomogeneous; positivity/slope projective.
9. **Q9:** **YES, PRESENT.** DIG3 supplies the genuine radial upper endpoint.
10. **Q10:** NOT APPLICABLE. LOW is not automatically satisfiable independently because the legal multiplier interval is bounded above.
11. **Q11:** YES after restoring the source-lattice embedding: the 1-D kernel is the positive lattice index \(n\); Hermitian moduli alone also fail to identify \(v_0\).
12. **Q12:** NO in general. DIG3 prevents safe retirement of the multiplier.
13. **Q13:** No composite-lattice extinction theorem is proved; the surviving condition is the isotropic locus with \(Z_0\) a unit modulo \(u\) and U-SQ.
14. **Q14:** NO universal symbolic binary/torsor parameterization; R7's no-universal-section theorem blocks it.
15. **Q15:** The correct R13 frontier is slightly larger than the proposed ideal:
\[
\boxed{
\text{primitive integral isotropic source-lattice ray}
\times
\text{one reduced-residue multiplier interval}
\times
\text{projective digit cone}
\times
\text{power-of-ten base}.
}
\]

## 15. Status

\[
\boxed{\textbf{J2 OPEN}.}
\]

The next global object is not an integral-orthogonal cusp yet.  The first unresolved
independent obstruction is the **whole-modulus reduced-residue interval attached to each
primitive isotropic ray**, together with the remaining composite \(Z_0\)-unit incidence.
