# 105-R9 — Endpoint Quotient / Unit Alignment × Canonical Source Successor Inequality × DES-to-Endpoint Transport

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — (A_1)-only  
**Round:** 105-R9  
**Frozen input:** 105-R1--R8  
**Required output:** decide source successor gap if possible; otherwise isolate one exact endpoint-residue gate.

---

## 1. Executive Verdict

本轮没有证明 universal radial extinction，也没有构造出 positive plain/source surplus。因此不能签 `POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY`，也不能签 `COMMON_U_INTEGER_SUCCESSOR_GATE_PASSED`.

但是 R9 得到了一条此前没有的 **source-native exact transport theorem**：frozen DES rows 可以直接传输到 active decimal lower endpoint 的模剩余类。于是 endpoint remainder 不再是“任意 remainder”，而是落在一个由 post-PSDG source data 决定的 residue coset。

正式 verdict：

```text
R9_TERMINAL_VERDICT=R9_REDUCED_TO_SINGLE_ENDPOINT_RESIDUE_GATE__DES_TO_ENDPOINT_TRANSPORT_PROVED__NO_UNIVERSAL_EXTINCTION__NO_POSITIVE_SURPLUS_WITNESS
```

新的唯一 first-failure 不是 abstract successor criterion，而是：

> **DES-transported endpoint residue lift selection:** 在 continuous post-PSDG survivor 上，DES 所允许的 endpoint residue coset 中，实际 power-of-ten endpoint 选中的 full residue lift 是否必然落入 nonpositive-surplus 区；若否，构造第一个落入 positive-surplus 区的 source profile。

因此 R10 只授权 Route D，不能重新研究 interval / PSDG / phase architecture。

---

## 2. Frozen R1–R8 State

- R1: `SOURCE_AFFINE_SECTION_LOSS` frozen.
- R2: canonical absolute source section / source-completed lift object frozen.
- R3: valuation atlas semantically saturated; no broad 2/5/J/carry reopen.
- R4–R6: fixed-incidence, moving-base obstruction, sphere×master lift, complementary discriminant and exceptional square locus frozen.
- R7–R7D: square-class, orientation, PSDG, determinant packet and source g1 firewall frozen; `PSDG_WITNESS_CONSTRUCTED` is accepted.
- R8: post-PSDG source fibre has rank one with radial variable U; generic source lattice is Z; q=1 progression is chart-local special semantics only; source lift iff `Succ_src(L)<R`.

No theorem below changes any of these objects.

## 3. Current First-Failure Gate

R8 input gate is `POST_PSDG_CANONICAL_SOURCE_SUCCESSOR_INEQUALITY`. R9 replaces only its arithmetic representation. The active quantity is the exact Euclidean division of the active decimal lower endpoint by the source carrier C2 or C3.

For Face A define `x2=10^(n2-1)`; for Face B define `x3=10^(n3-1)`.

## 4. Two-Face Canonical Successor Equations

Face A (`L2>=L3`):

$$G_A=C_2 10^{n_3}-C_3 10^{n_2-1},\qquad \Sigma_A=G_A-C_3\delta_2.$$

Face B (`L3>L2`):

$$G_B=C_3 10^{n_2}-C_2 10^{n_3-1},\qquad \Sigma_B=G_B-C_2\delta_3.$$

Continuous consistency is `G_A>0` on A and `G_B>0` on B. Successor arithmetic is not evaluated as a live gate before this consistency check.

## 5. Exact Source Forms of C2,C3

The canonical definition is

$$g_i=\gcd(V,P_i),\qquad C_i=P_i/g_i,\qquad b_i=V/g_i.$$

Hence the elementary but important exact reducedness identity is

$$\boxed{\gcd(b_i,C_i)=1}. $$

Using the frozen Full Smith chart

$$b_1=s\alpha u,\quad b_2=s\alpha\beta t,\quad b_3=s\beta v,$$
$$\gamma=\gcd(u,v),\quad u=\gamma u_0,\quad v=\gamma v_0,$$

and Full Smith–Radial Cancellation,

$$g_2=u_0v,\qquad g_3=u_0\alpha t,$$
$$P_2=vM,\qquad P_3=\alpha tN,\qquad u_0\mid M,N,$$

we recover the stronger source form

$$\boxed{C_2=M/u_0,\qquad C_3=N/u_0}. $$

Thus

$$\gcd(C_2,C_3)=\gcd(M/u_0,N/u_0),$$

with no frozen theorem forcing this gcd to 1. The exact census already contains gcd 1 and 3.

## 6. Decimal gcd classification

Write `C_i=2^{alpha_i}5^{beta_i}C_i^o`. Source-wide, the only unconditional law is `gcd(C_i,b_i)=1`. Therefore a 2- or 5-factor present in the corresponding denominator block is forbidden from C_i, but if the denominator block is a ten-unit then C_i may carry decimal factors. There is no universal `(C_i,10)=1` theorem.

| state | C2 | decimal type C2 | C3 | decimal type C3 | gcd(C2,C3) |
|---|---:|---|---:|---|---:|
| A | 13 | 2^0 5^0 · 13 | 53 | 2^0 5^0 · 53 | 1 |
| B | 109 | 2^0 5^0 · 109 | 25 | 2^0 5^2 · 1 | 1 |
| C | 73 | 2^0 5^0 · 73 | 969 | 2^0 5^0 · 969 | 1 |
| E | 2514 | 2^1 5^0 · 1257 | 297 | 2^0 5^0 · 297 | 3 |

This immediately falsifies any attempted R9 theorem that assumes a fixed decimal gcd type.

## 7. Exponent-Difference Audit

Frozen A1 exponent skeleton gives

$$m_2=g+d,\quad n_2=2g+k+d=g+k+m_2,\quad m_3=n_3+g.$$

Therefore

$$n_2-n_3=g+k+m_2-n_3.$$

No frozen post-PSDG theorem makes this difference finite. In particular the historical H0 chart has `g=0`, `n2=m2+k`, `m3=n3`, so `n2-n3=m2+k-m3` remains moving. The earlier A1 mantissa/sector bounds do not provide the requested global finite `n3-n2` atlas under the present hypotheses.

Status: `N2_MINUS_N3_RANGE=NOT_FINITE_FROM_FROZEN_THEOREMS`.

## 8. Face A Quotient–Remainder Form

Let

$$x_2=10^{n_2-1}=q_2C_2+r_2,\qquad 0\le r_2<C_2.$$

Then

$$U_{\mathbb Z,2}=\left\lceil x_2/C_2\right\rceil,$$

and

$$\delta_2=C_2U_{\mathbb Z,2}-x_2=\begin{cases}0&r_2=0,\C_2-r_2&r_2>0.\end{cases}$$

Exact substitution into the cross-gap gives the quotient identity

$$\boxed{\Sigma_A=C_2\bigl(10^{n_3}-C_3U_{\mathbb Z,2}\bigr)}. $$

For `r2>0`, this is

$$\Sigma_A=C_2\bigl(10^{n_3}-C_3(q_2+1)\bigr).$$

For `r2=0`, it is `C2(10^{n3}-C3 q2)`. This is exact quotient language; R9 does not count it alone as a solution.

## 9. Face B Quotient–Remainder Form

Similarly

$$x_3=10^{n_3-1}=q_3C_3+r_3,\qquad 0\le r_3<C_3,$$

$$\delta_3=C_3U_{\mathbb Z,3}-x_3,$$

and

$$\boxed{\Sigma_B=C_3\bigl(10^{n_2}-C_2U_{\mathbb Z,3}\bigr)}. $$

For `r3>0`, `U_Z,3=q3+1`; for `r3=0`, `U_Z,3=q3`.

## 10. Plain Modular Jumps δ2,δ3

The modular jump is exactly the complement of the power-of-ten remainder. The R8 exact census gives:

| state | q2 | r2 | δ2 | q3 | r3 | δ3 |
|---|---:|---:|---:|---:|---:|---:|
| A | 0 | 10 | 3 | 0 | 1 | 52 |
| B | 0 | 10 | 99 | 0 | 1 | 24 |
| C | 0 | 10 | 63 | 0 | 1 | 968 |
| E | 0 | 10 | 2504 | 0 | 1 | 296 |

All four happen to have q2=q3=0 because the frozen census has n2=2,n3=1 and carriers larger than the lower powers. This is census data, not a theorem.

## 11. Cross-Gaps G_A,G_B

With `d23=n3-n2`, Face A can be rewritten

$$G_A=10^{n_2-1}\bigl(10^{d_{23}+1}C_2-C_3\bigr).$$

Face B analogously is

$$G_B=10^{n_3-1}\bigl(10^{1-d_{23}}C_3-C_2\bigr).$$

Because d23 is not frozen finite, this does not become a finite face table source-wide.

## 12. Plain Surplus Σ_A,Σ_B

Formal exact-census values:

| state | face | continuous? | active gap | weighted plain jump | formal plain surplus |
|---|---|---|---:|---:|---:|
| A | A | NO | -400 | 159 | -559 |
| B | A | YES | 840 | 2475 | -1635 |
| C | A | NO | -8960 | 61047 | -70007 |
| E | A | YES | 22170 | 743688 | -721518 |

Only B and E enter the live successor comparison because A and C already fail continuous overlap. B and E both have strictly negative plain surplus.

## 13. Endpoint Quotient / Unit Alignment

The normalized phase picture is exact but secondary:

$$\eta_A=\delta_2/C_2,\quad \gamma_A=R_3-L_2,$$

and `eta_A<gamma_A` iff `Sigma_A>0`; similarly on B. The integer cross-product form remains canonical for proofs.

The new R9 object is not the real phase itself, but the **source transport of the endpoint residue**.

## 14. DES-to-Endpoint Residue Transport

### 14.1 Frozen DES input

Put

$$G=10^g,\quad K=10^k,\quad X=10^{m_2},\quad Y=10^{n_3},$$
$$D=KP_1-Q_0,$$
$$H=b_2Q_0-b_1XD,$$
$$K_3=\frac{b_3(Q_0-P_3)}Y\in\mathbb Z,$$
$$b_2P_2=GH+K_3.$$

Since `b2 P2=V C2` and `b3 P3=V C3`, these rows carry C2,C3 source semantics exactly.

### 14.2 Face-A endpoint transport theorem

Because `n2=g+k+m2`,

$$10^{n_2-1}=\frac{GKX}{10}=x_2.$$

From `GH+K3=VC2` and the definition of H,

$$G b_1XD=Gb_2Q_0+K_3-VC_2.$$

Multiplying by K yields

$$\boxed{10b_1D\,x_2\equiv K(Gb_2Q_0+K_3)\pmod{C_2}.}\tag{T2-D}$$

A second form follows from `KP1=Q0+D`:

$$b_1XKP_1=(b_1X+b_2)Q_0-H,$$

hence

$$\boxed{10b_1P_1\,x_2\equiv G(b_1X+b_2)Q_0+K_3\pmod{C_2}.}\tag{T2-P}$$

Let

$$h=\gcd(P_1,Q_0)=\gcd(P_1,D).$$

Choose Bezout coefficients `sD+tP1=h` and define

$$E_2=sK(Gb_2Q_0+K_3)+t\bigl(G(b_1X+b_2)Q_0+K_3\bigr).$$

Then

$$\boxed{10b_1h\,x_2\equiv E_2\pmod{C_2}.}\tag{T2}$$

Define

$$d_2^*=\gcd(C_2,10b_1h),\qquad M_2=C_2/d_2^*.$$

Consistency forces `d2*|E2`, and modulo M2 the endpoint has a unique source-determined residue

$$\boxed{\rho_2^{DES}\equiv \frac{E_2}{d_2^*}\left(\frac{10b_1h}{d_2^*}\right)^{-1}\pmod{M_2}.}$$

Therefore the full remainder `r2=x2 mod C2` lies in exactly one coset with `d2*` lifts modulo C2. This is the first exact DES→endpoint remainder bridge in the 105 line.

By R7 prime-support audit, h is odd and all odd primes dividing h are `1 mod 4`. Also `gcd(C2,b2)=1`; in the Smith chart this removes all common `s alpha beta t` content from C2 and b1, so the nondecimal part of `d2*` can only come from genuinely residual b1/h support, not from the common denominator content.

### 14.3 Face-B endpoint transport theorem

Since `Y=10x3`, the frozen K3 row gives

$$YK_3=b_3(Q_0-P_3)=b_3Q_0-VC_3,$$

and hence

$$\boxed{10K_3x_3\equiv b_3Q_0\pmod{C_3}.}\tag{T3}$$

Put

$$d_3^*=\gcd(C_3,10K_3),\qquad M_3=C_3/d_3^*.$$

Because `gcd(b3,C3)=1`, consistency implies `d3*|Q0`. Thus

$$\boxed{\rho_3^{DES}\equiv \frac{b_3Q_0}{d_3^*}\left(\frac{10K_3}{d_3^*}\right)^{-1}\pmod{M_3}.}$$

Again the full endpoint remainder is restricted to the `d3*` lifts of one class mod M3. Moreover every prime dividing `gcd(C3,Q0)` is odd and `1 mod 4` by the primitive sphere argument, so the transport defect cannot contain 2 or an inert `3 mod 4` prime from this common endpoint/source channel.

### 14.4 Regression of the transport theorem

| state | r2 | d2* | M2 | rho2 mod M2 | r3 | d3* | M3 | rho3 mod M3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 10 | 1 | 13 | 10 | 1 | 1 | 53 | 1 |
| B | 10 | 1 | 109 | 10 | 1 | 5 | 5 | 1 |
| C | 10 | 1 | 73 | 10 | 1 | 1 | 969 | 1 |
| E | 10 | 2 | 1257 | 10 | 1 | 1 | 297 | 1 |

For B, `d2*=1`, so the DES row completely determines the Face-A remainder modulo C2: `r2=10 mod 109`. For E, DES determines `r2=10 mod 1257`, leaving two lifts modulo 2514; the actual decimal endpoint selects the lift 10. Thus DES transport is genuine rigidity, but not source-wide fixed rigidity.

## 15. Post-PSDG Phi23 Re-audit

Define

$$\Phi_{23}=10^{n_2-n_3}\frac{C_3}{C_2}=\frac{L_2}{L_3}.$$

This gives an exact face dictionary:

- continuous Face A iff `1 <= Phi23 < 10`;
- continuous Face B iff `1/10 < Phi23 < 1`.

Frozen exact census:

| state | Phi23 | face | continuous |
|---|---|---|---|
| A | 530/13 | A | NO |
| B | 250/109 | A | YES |
| C | 9690/73 | A | NO |
| E | 495/419 | A | YES |

B and E already give two different post-PSDG continuous phase values (`250/109` and `495/419`), so **fixed phase rigidity is false after PSDG**. No theorem in R1–R8 proves a finite phase atlas. R9 therefore does not resurrect R5 moving-phase architecture.

## 16. Exact Integer-Lower-Endpoint Construction

If `C2|10^(n2-1)` on continuous Face A, then `delta2=0`, so `Sigma_A=G_A>0` automatically. The analogous statement holds on B. This is an exact construction lemma.

However, no frozen post-PSDG theorem or exact profile found in R9 realizes such a divisible active lower endpoint. R9 therefore records this as a valid construction target, not a witness.

## 17. Positive-Surplus Construction

Two construction routes were executed:

1. Re-audit of the four frozen exact post-PSDG hits A,B,C,E: no positive plain surplus.
2. H0 fixed-chart exact source-box search described in Section 21: no new source integer U in the searched finite range.

Therefore `FIRST_POSITIVE_PLAIN_PROFILE=NONE` in current exact evidence. This is not a no-existence theorem.

## 18. q=1 Source Progression

No positive plain hit was found. By the R9 hierarchy, q=1 affine progression is therefore **not activated as a new first failure**. The frozen chart-local formula remains valid but is not broadened to generic profiles.

## 19. Coprimality Successor

Likewise no new plain hit reaches coprimality. R7D B remains the regression: its plain successor is U=1 and `(1,24)=1`, but U=1 lies above the active upper endpoint. Hence gcd is not the current first failure.

## 20. Full Source Surplus

No profile with `Sigma_plain>0` was found, so `J_src` is never larger than delta because of a newly tested selector in this round. The full-source surplus remains unentered on new profiles. Current exact B/E source interval surpluses are `-3/5` and `-287/297`.

## 21. Expanded Post-PSDG Exact Census

### 21.1 Frozen authoritative census

The authoritative R7D/R8 reduced registry has four exact post-PSDG profiles: A,B,C,E. Counts:

```text
POST_PSDG_PROFILES=4
FACE_A_COUNT=4
FACE_B_COUNT=0
CONTINUOUS_SURVIVORS=2
CONTINUOUS_PLAIN_SURPLUS_POSITIVE=0
CONTINUOUS_PLAIN_SURPLUS_ZERO=0
CONTINUOUS_PLAIN_SURPLUS_NEGATIVE=2
SOURCE_SURPLUS_POSITIVE=0
FIRST_POSITIVE_PLAIN_PROFILE=NONE
FIRST_POSITIVE_SOURCE_PROFILE=NONE
```

### 21.2 R9 finite expansion, theorem firewall

A direct exact H0 post-PSDG chart search with `g=0,k=1,m2=n3=1`, `b2,b3<=9`, `b1<=30`, `C2<=400`, `C3<=150` examined **61,092,600** source states. It found only A and B again; no new profile and no Face B. This is computational evidence only.

A second source-integer construction scan imposed U=1,...,9, `b2,b3<=9`, `b1<=1000`, and the corresponding exact U digit boxes. It examined **33,456,365** states; 46 had square discriminant at the rational quadratic stage, but **0** had an integral positive C1 root, hence 0 source hits. Again: finite negative control, not extinction theorem.

## 22. R7D/R8 Regression

Canonical witness B:

$$C_2=109,\ C_3=25,\ x_2=10,\ q_2=0,\ r_2=10,\ \delta_2=99.$$

$$G_A=840,\qquad C_3\delta_2=2475,\qquad \Sigma_A=-1635.$$

Equivalently normalized `U_Z=1`, `R=2/5`, source surplus `R-U=-3/5`. The new DES transport gives `d2*=1,M2=109,rho2=10`, exactly reproducing the endpoint residue.

## 23. First Plain Integer Hit

None found. `PLAIN_INTEGER_HIT_FOUND=NO`.

## 24. First Source Integer Hit

None found. `SOURCE_INTEGER_U_FOUND=NO`.

## 25. Downstream Source Reconstruction

Not reached because no integer U crossed the active upper endpoint. No actual `a_i=UC_i` reconstruction is claimed in R9.

## 26. Digit Synchronization Audit

Not reached after integer gate. The two active radial windows already encode block-2/block-3 digit legality, but no full post-radial synchronization is entered.

## 27. Actual Cut Audit

Not reached. R9 does not move actual cut ahead of the integer successor gate.

## 28. New First-Failure Gate

The first failure is sharpened from a raw inequality to one source-native arithmetic object:

$$\boxed{\textbf{DES-TRANSPORTED ENDPOINT RESIDUE LIFT / SURPLUS SIGN GATE}.}$$

Face A: the actual `r2=x2 mod C2` is constrained by `(T2-D),(T2-P)` to the DES coset `rho2^DES mod M2`; prove every source-legal continuous profile chooses a lift satisfying `C3(C2-r2)>=G_A` (with the `r2=0` case explicitly excluded by such a theorem), or construct a profile violating it.

Face B: analogously use `(T3)` and the `rho3^DES mod M3` coset.

This is the single endpoint-residue theorem permitted by the R9 partial-success rule.

## 29. Failed / Falsified Routes

1. **Universal decimal-unit carrier:** false/unsupported; exact census has C3=25 and C2 even in E.
2. **Finite exponent-difference atlas from frozen hypotheses:** not obtained; H0 leaves n2-n3 moving.
3. **DES directly fixes full remainder source-wide:** false as stated; it fixes a reduced residue coset, with defect d_i* that can vary. E already has d2*=2.
4. **Post-PSDG phase becomes fixed:** false; B and E have different continuous Phi23.
5. **R<=1 universal:** still not proved; only current exact census.
6. **No-hit computation as theorem:** explicitly rejected; both R9 searches are finite evidence only.
7. **Generic multiplicative-order / random-remainder route:** not used.
8. **q=1 progression as global modulus:** not used and remains forbidden.

## 30. Exact Remaining Unknowns

There is one structural unknown:

> Given the DES transport coset for the active endpoint, does post-PSDG source provenance force the actual power-of-ten lift into the nonpositive-surplus side, or can one realize an early enough lift to make Sigma positive?

All other R9 unknowns (generic phase movement, exponent difference, decimal gcd type) are subordinate data inside this single gate, not parallel architectures.

## 31. R9 Terminal Verdict

R9 obtains genuine information gain but not the requested truth value. The exact gain is a DES→endpoint residue transport theorem on both faces, plus a proof that the post-PSDG phase is not fixed and that the active exponent difference is not frozen finite by inherited hypotheses. Current exact census and two finite searches produce no positive surplus.

Therefore the only legally signable partial verdict is:

```text
R9_REDUCED_TO_SINGLE_ENDPOINT_RESIDUE_GATE=YES
ENDPOINT_QUOTIENT_RIGIDITY=PARTIAL__DES_REDUCED_RESIDUE_COSET_PROVED__FULL_LIFT_SIGN_OPEN
DES_TO_ENDPOINT_RESIDUE_BRIDGE=PROVED
POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NOT_PROVED
COMMON_U_INTEGER_SUCCESSOR_GATE=OPEN
```

## 32. R10 Authorization Decision

Only Route D is authorized:

$$\boxed{\textbf{R10 = DES-Transported Endpoint Residue Lift Selection × Surplus Sign}.}$$

R10 must not reopen endpoint criterion, interval geometry, PSDG, discriminant, Smith redesign, moving-base phase, or generic coprime gaps. Its single attack target is to control the lift index inside the DES residue coset strongly enough to sign the surplus, or to construct the first positive transported residue.

---

## Machine-readable terminal block

```text
R9_TERMINAL_VERDICT=R9_REDUCED_TO_SINGLE_ENDPOINT_RESIDUE_GATE__DES_TO_ENDPOINT_TRANSPORT_PROVED__NO_UNIVERSAL_EXTINCTION__NO_POSITIVE_SURPLUS_WITNESS

R1_TO_R8_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=DES_TRANSPORTED_ENDPOINT_RESIDUE_LIFT__SURPLUS_SIGN

FACE_A_VALID=YES__B_AND_E_CONTINUOUS_EXACT_POST_PSDG_SURVIVORS
FACE_B_VALID=NOT_ESTABLISHED__NO_EXACT_POST_PSDG_FACE_B_IN_CURRENT_CENSUS_OR_R9_FINITE_H0_SEARCH

C2_SOURCE_FORM=C2=P2/gcd(V,P2)=M/u0
C3_SOURCE_FORM=C3=P3/gcd(V,P3)=N/u0
GCD_C2_C3=SOURCE_MOVING__FROZEN_CENSUS_VALUES_1_1_1_3
DECIMAL_GCD_TYPE_C2=SOURCE_MOVING__gcd(C2,b2)=1_ONLY_UNIVERSAL_LAW
DECIMAL_GCD_TYPE_C3=SOURCE_MOVING__gcd(C3,b3)=1_ONLY_UNIVERSAL_LAW

N2_MINUS_N3_RANGE=NOT_FINITE_FROM_FROZEN_THEOREMS

FACE_A_GAP=G_A=C2*10^n3-C3*10^(n2-1)
FACE_B_GAP=G_B=C3*10^n2-C2*10^(n3-1)

Q2=floor(10^(n2-1)/C2)__FROZEN_CENSUS_ALL_ZERO
R2_REMAINDER=10^(n2-1)-Q2*C2__FROZEN_CENSUS_ALL_10
DELTA2=(-10^(n2-1)) mod C2__FROZEN_A_B_C_E=3,99,63,2504

Q3=floor(10^(n3-1)/C3)__FROZEN_CENSUS_ALL_ZERO
R3_REMAINDER=10^(n3-1)-Q3*C3__FROZEN_CENSUS_ALL_1
DELTA3=(-10^(n3-1)) mod C3__FROZEN_A_B_C_E=52,24,968,296

PLAIN_SURPLUS_A=G_A-C3*DELTA2=C2*(10^n3-C3*ceil(10^(n2-1)/C2))
PLAIN_SURPLUS_B=G_B-C2*DELTA3=C3*(10^n2-C2*ceil(10^(n3-1)/C3))

PLAIN_SURPLUS_UNIVERSALLY_NONPOSITIVE=NOT_PROVED

ENDPOINT_QUOTIENT_RIGIDITY=PARTIAL__DES_REDUCED_RESIDUE_COSET_PROVED__FULL_LIFT_SIGN_OPEN
ENDPOINT_RESIDUE_CLASSES=FACE_A:r2=rho2_DES_mod_M2_WITH_d2star_LIFTS__FACE_B:r3=rho3_DES_mod_M3_WITH_d3star_LIFTS

DES_TO_ENDPOINT_RESIDUE_BRIDGE=PROVED__T2_D__T2_P__T2_BEZOUT__T3

POST_PSDG_PHASE_23=Phi23=10^(n2-n3)*C3/C2=L2/L3__B=250/109__E=495/419
PHASE_23_RIGID_AFTER_PSDG=FIXED_RIGIDITY_FALSE__FINITE_ATLAS_UNKNOWN

PLAIN_INTEGER_HIT_FOUND=NO
PLAIN_HIT_FACE=NONE
PLAIN_HIT_U=NONE
PLAIN_HIT_PROFILE=NONE

Q1_AFFINE_PROGRESSION_ACTIVE=NO_NEW_HIT_REACHES_THIS_LAYER__CHART_LOCAL_SPECIAL_ONLY
SOURCE_PROGRESSION=NOT_REACHED_ON_NEW_PROFILE
SOURCE_SUCCESSOR=NO_POSITIVE_CANDIDATE_REACHES_SELECTOR_LAYER

COPRIMALITY_V=NOT_REACHED_ON_NEW_HIT__R7D_B_U1_COPRIME_24_BUT_OUTSIDE_INTERVAL
COPRIMALITY_PASS=NOT_APPLICABLE_TO_NEW_HIT

SOURCE_SURPLUS=NO_POSITIVE_WITNESS__R7D_B=-3/5__E=-287/297
SOURCE_INTEGER_U_FOUND=NO
SOURCE_INTEGER_U=NONE

COMMON_U_INTEGER_SUCCESSOR_GATE=OPEN__REDUCED_TO_DES_TRANSPORTED_ENDPOINT_RESIDUE_LIFT_SIGN

DIGIT_SYNCHRONIZATION=NOT_REACHED_AFTER_INTEGER_GATE
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

NEW_FIRST_FAILURE_GATE=DES_TRANSPORTED_ENDPOINT_RESIDUE_LIFT__SURPLUS_SIGN

POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NOT_PROVED

R9_SINGLE_ENDPOINT_RESIDUE_GATE=YES

R10_AUTHORIZED=YES
R10_ARCHITECTURE=ROUTE_D__DES_TRANSPORTED_ENDPOINT_RESIDUE_LIFT_SELECTION_X_SURPLUS_SIGN
R10_SINGLE_ATTACK_TARGET=CONTROL_THE_FULL_REMAINDER_LIFT_INSIDE_THE_DES_COSET_AND_SIGN_THE_ACTIVE_SURPLUS__OR_CONSTRUCT_FIRST_POSITIVE_TRANSPORTED_RESIDUE
```

---

## Provenance / theorem-vs-computation ledger

**Frozen theorem inputs:** `105_R8_Common_U_Integer_Source_Fibre.md`; `105_R7D_Determinant_Packet_Source_GCD_Firewall.md`; `105_R7_GCD_Audit.csv`; `105_R6_General_Moving_Profile_Sphere_Master_Lift.md`; `95_R1_Full_A1_Historical_Recovery_and_NonJ2_Canonical_Frontier.md`; `95_R6_T0_Transition_Finite_Borrow_Affine_Boundary_Margin_Assault.md`.

**New proved in R9:** quotient surplus identities; DES endpoint transports (T2-D), (T2-P), (T2), (T3); reduced residue-coset formulas; exact post-PSDG phase/face dictionary; fixed phase rigidity falsified by B/E exact survivors.

**Computational evidence only:** 61,092,600-state H0 post-PSDG finite expansion (A/B rediscovered only); 33,456,365-state U=1..9 H0 source-box scan (0 integral C1 roots/hits).

**Open:** universal surplus sign; positive transported endpoint construction; existence of genuine Face-B post-PSDG survivor; full remainder-lift selection theorem.
