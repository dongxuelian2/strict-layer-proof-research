# 105-R31 — N30 Positive Analysis and Active Witness Hunt

## 1. Exact terminal predicate retained from R30

For a fixed legal post-support architecture,

\[
N_{30}(\mathfrak a)=\sum_{U\in\mathcal U_0}\Phi_{\mathfrak a}(U),
\]

\[
\Phi_{\mathfrak a}(U)=
\#\{q\in[Q_-,Q_+]\cap\mathbb Z_{>0}:(q,FU)=1\}.
\]

R31 does not re-prove this count theorem; it opens its smallest atoms.

## 2. Unit chamber

If \(Q_-=1\) and the q-window is nonempty, then q=1 is always coprime to \(FU\). Therefore

\[
\boxed{N_{30}>0\iff\mathcal U_0\ne\varnothing.}
\]

Prime cover is completely powerless in this chamber.

## 3. Nonunit chamber

For each U, let qmin be the first integer at or above \(Q_-\) that is coprime to \(FU\). R31 proves

\[
q_{\min}\text{ prime}\quad\text{or}\quad q_{\min}<Q_-^2.
\]

Therefore the exact positive test can be reorganized as:

- scan primes in the actual q-window and test whether each divides \(FU\);
- scan only composites below \(Q_-^2\);
- ignore all larger composite candidates for existential purposes.

This is architecture-specific and exact; no generic Jacobsthal bound is introduced.

## 4. Active q=1 falsification search

The R28 complete raw-TC1 corpus through \(Q_0\le3000\) contains seven q=1 forced-scale hits, but all seven die at the source radial box with \(U_{lo}=1>U_{hi}=0\). Three of the seven already pass the q-independent shape/Smith/tail compatibility before this source-room death:

- `(48,436,75,445)` with `A=3,W=4,g1*=24,Lambda=2,C2=109,C3=25`;
- `(120,900,691,1141)` with `A=1,W=12,g1*=24,Lambda=2,C2=75,C3=691`;
- `(298,2514,1485,2935)` with `A=5,W=1,g1*=1,Lambda=1,C2=2514,C3=297`.

Each has exact q=1 denominator fit, and each still has source integer upper endpoint zero. Thus the bounded first-failure is source-room, not prime cover.

## 5. Architecture-first reverse generation

R31 then inverted the search order. For prescribed q and U, digit conditions give finite intervals for A,W,C2,C3. TC1 is linear in P1; sphere substitution yields the exact quadratic `R31-F11`. The search enumerates \(\mu\mid\Lambda\), \(g_0\mid AW\), puts \(g_1^*=\mu g_0\), solves the exact square discriminant, then replays primitive, D/H/T positivity, lambda/tau/Lambda, Smith and g1-firewall checks.

- `Q1_U1_TO_U3_L8_K1`: 350,723 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.
- `Q1_U1_L8_K2`: 3,230,116 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.
- `SMALL_Q_U1_L6_K1`: 380,912 exact configurations; integer TC1-conic solutions = 0; pre-TC4 survivors = 0.

No scope produced an integer TC1-conic solution, hence none can contain an N30-positive full architecture. These are complete finite statements only for the explicitly listed architecture boxes.

## 6. Historical R29 support survivor

For

\[
(P_1,P_2,P_3,Q_0)=(640,1420,4727,4977),
\]

\[
(A,W,u_0,g_1^*)=(1,20,1,80),
\]

R30/R31 recover

\[
\Lambda=4,\qquad Z_-=50,\qquad Z_+=9,
\]

so

\[
Q_-=13>2=Q_+.
\]

Thus its N30 value is zero before source activation.

## 7. Genuine positive status

```text
GENUINE_N30_POSITIVE_FOUND=NO
FULL_C26_PACKET_FOUND=NO
Q1_GENUINE_POST_SUPPORT_ARCHITECTURE_FOUND=NO
GLOBAL_N30_ZERO_THEOREM=NOT_PROVED
```

No positive architecture exists in the frozen replay corpus or the new exact reverse-generation scopes. This absence is not promoted to a global theorem.

## 8. Exact remaining object

For each legal TC1/TC2/post-support architecture and each \(U\in\mathcal U_0\), define the deterministic lower-edge coprime successor

\[
\boxed{
q_{\min}(\mathfrak a,U)
=
\min\{q\ge Q_-:(q,FU)=1\}.
}
\]

Then

\[
\boxed{
N_{30}(\mathfrak a)>0
\iff
\exists U\in\mathcal U_0:\ q_{\min}(\mathfrak a,U)\le Q_+.
}
\]

R31 reduces this deterministic object to the unit/prime/finite-composite trichotomy. The prime branch is the only unbounded-shaped arithmetic class that remains.
