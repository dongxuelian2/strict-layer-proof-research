# 75-R7 Interface A — USSPAL Intrinsic Lower Barrier

## Target

Prove, for the frozen R5 allowed-ruling transverse Veronese interface,
\[
\boxed{a_p\mathcal H_{\perp,\tau}\ge G^{1-o(1)}}.
\]

## L1. Exact transverse restriction

Recall
\[
Q_\tau(w)=\frac1{C_\Gamma}F_0(M_sw_1+\rho_sw_2,w_2,w_3),
\]
where \(C_\Gamma\) is the positive integral coefficient content and
\[
M_s=\frac{G}{\gcd(G,2d(q+4))}\mid G.
\]
The R5 transversal is
\[
y(t,s)=(M_st,0,s)
\]
in raw \((Z,a,x)\)-coordinates, equivalently \((w_1,w_2,w_3)=(t,0,s)\).
Therefore
\[
\boxed{
Q_{\perp,\tau}(t,s)
=\frac1{C_\Gamma}
\left[
G^3(GA+2)M_s^2t^2
-4G^3KuM_s ts
+G^2A s^2
\right].
}
\]
In particular
\[
\boxed{\mathcal H_{\perp,\tau}\ge \frac{G^2A}{C_\Gamma}}.
\]

## L2. A content coefficient that limits ten-adic cancellation

The raw coefficient of \(w_1w_2\) in the full pulled form is
\[
\boxed{
M_sB_{12},\qquad
B_{12}=2G^3(GA+2)\rho_s-4u(G^2A^2+GA-1).
}
\]
Since \(C_\Gamma\) divides every raw coefficient,
\[
C_\Gamma\mid M_sB_{12}.
\]

Put
\[
E=G^2A^2+GA-1.
\]
Because \(G=10^g\),
\[
E\equiv-1\pmod{10}.
\]
Also \(u\) is a ten-unit from \(uq=G+1\) on the live q>1 source family. Hence the second summand in \(B_{12}\) has exact valuations
\[
v_2(-4uE)=2,\qquad v_5(-4uE)=0,
\]
while the first summand is divisible by \(G^3\). Consequently, with no prime splitting of the source lattice itself,
\[
\boxed{v_2(B_{12})=2,\qquad v_5(B_{12})=0}.
\]
Therefore
\[
\boxed{v_2(C_\Gamma)\le v_2(M_s)+2},
\]
\[
\boxed{v_5(C_\Gamma)\le v_5(M_s)}.
\]

## L3. The transverse coefficient retains one full power of G

The \(s^2\)-coefficient of the primitive transverse form is the positive integer
\[
\frac{G^2A}{C_\Gamma}.
\]
Since \(A=2u+1\) is odd and \(M_s\mid G\), for \(g\ge2\),
\[
v_2\!\left(\frac{G^2A}{C_\Gamma}\right)
\ge 2g-v_2(M_s)-2\ge g-2,
\]
\[
v_5\!\left(\frac{G^2A}{C_\Gamma}\right)
\ge 2g-v_5(M_s)\ge g.
\]
Hence
\[
\boxed{
\frac{G^2A}{C_\Gamma}
\ge 2^{g-2}5^g
=\frac G4.
}
\]
Thus
\[
\boxed{\mathcal H_{\perp,\tau}\ge \frac G4\qquad(g\ge2)}.
\]
The single finite exponent \(g=1\) is irrelevant to the asymptotic survival criterion and may be handled separately.

## L4. Product barrier

For any positive integral allowed-ruling source basepoint,
\[
a_p\ge1.
\]
Therefore the R7 survival quantity obeys
\[
\boxed{
\mathfrak A_\tau
:=a_p\mathcal H_{\perp,\tau}
\ge\frac G4
=G^{1-o(1)}.
}
\]
This is uniform over all basepoints used by the **frozen R5 transversal**, because the lower bound is entirely in the transverse source-form content and is independent of \(p\).

Consequently no fixed \(\delta>0\) can satisfy
\[
\mathfrak A_\tau\le G^{1-\delta+o(1)}
\]
on this interface.

## L5. Scope of the negative theorem

This is a structural death theorem for the R5 allowed-ruling transverse Veronese interface selected and frozen by R7. It is **not** a theorem that every conceivable source-integral birational chart has distortion \(\gg G\). R7 explicitly forbids opening a third/fourth chart family; therefore this lower bound is sufficient for the mandated interface exit decision.

The mechanism is source-content/denominator quantization, not a generic height theorem:
\[
\boxed{
\text{one full power of }G\text{ survives primitive content removal in }Q_{\perp,\tau}.
}
\]

```text
LOWER_BARRIER_STATUS=PROVED
BEST_LOWER_BOUND=a_p*H_perp >= G/4 for g>=2
EXPONENT_LOWER_BOUND=1
SOURCE_CONTENT_MECHANISM=ten-adic depth of C_Gamma limited by the w1w2 coefficient
CHART_SCOPE=FROZEN_R5_ALLOWED_RULING_TRANSVERSE_VERONESE
```

---

STAGE_INPUTS=75-R4 exact F0 and source lattice; R5 frozen transverse y=(M_s t,0,s); Phase A1 exact lift
NEW_PROVED_RESULTS=Exact transverse restriction; v2(C_Gamma)<=v2(M_s)+2; v5(C_Gamma)<=v5(M_s); H_perp>=G/4 for g>=2; a_p*H_perp>=G/4
NEW_REDUCTIONS=USSPAL survival quantity has an intrinsic exponent-1 source-content floor on the frozen chart
NEGATIVE_RESULTS=Strict exponent-saving upper bound is impossible on the frozen R5 chart interface
REJECTED_ROUTES=Further refinement of a_p alone; squarefree-discriminant-only lower bound; new chart families forbidden by R7
EXTERNAL_SOURCES_USED=NONE_NEW
MIGRATION_CARDS_CREATED_OR_UPDATED=NONE
OUTPUT_DEPENDENCIES=04_USSPAL_survival_verdict.md; final dual-interface comparison
UNRESOLVED_ITEMS=Chart-independent lower bound over all possible birational source charts is not claimed and is no longer an R7 task
PHASE_STATUS=FROZEN
