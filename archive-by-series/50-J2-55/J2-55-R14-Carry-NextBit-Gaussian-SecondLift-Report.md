# J2-55-R14 — Carry Next-Bit × Low-k Parity Correction × Negative Gaussian Four-(t) × Equal-Valuation Second-Lift Report

**Scope:** Strict Layer — $A_1$-only — Exact Resonance $R=0$ — $J=2$ only  
**Campaign:** 55 第十四轮 / 统一终端线第二十四轮  
**Dependency discipline:** R12 independent full-root polynomials are frozen; R7 exact reverse carry is rederived from source; no new residual or root quotient is introduced.

# 1. Executive Status

$$\boxed{\textbf{J2 OPEN}}$$

$$\boxed{\delta>0:\ \textbf{OPEN}}$$

$$\boxed{\delta=0,q>1:\ \textbf{OPEN}}$$

The inherited $q=1,\delta=0$ boundary remains CLOSED.

$$\boxed{q=1\text{ reverse}:\ \textbf{OPEN}}$$

$$\boxed{\delta<0,q>1:\ \textbf{OPEN}}$$

No `J2-Resonance-Closure-Certificate.md` is generated.

The decisive R14 correction is that the reverse normalized carry does **not** have a bounded next-bit excess. After the legal reverse tail substitution and $G=KR$, the exact R7 carry numerator satisfies

$$\boxed{\Gamma_R=R\,\Phi_R}$$

with $\Phi_R$ an integer polynomial in the existing structural variables. Thus the R13 low-$k$ `gamma odd` branches are vacuous, and the bit ladder is retired. R14 then splices this exact cancellation locus directly into the independent R12 degree-seven root polynomial.

# 2. Bit Verdict

```text
REVERSE_GAMMA_R_EVEN=PROVED
K1_GAMMA_ODD_BRANCH=VACUOUS_RETIRED
K1_V2_GAMMA=>=r (not 1)
K2_Q7_V2_GAMMA=>=r (not 1)
K2_Q11_V2_GAMMA=>=r (not 1)
GENERIC_GAMMA_V2_BOUND=no absolute upper bound from next-bit; exact lower v2(gamma)>=r+2-k
GENERIC_REVERSE_R_BOUND=NOT_OBTAINED; explicit R-factor cancellation locus exposed
BIT_LADDER=RETIRED
```

Variable/theorem ledger update:

```text
R13_K1_GAMMA_ODD_BRANCH     = VACUOUS_RETIRED
R13_K2_Q7_GAMMA_ODD_BRANCH  = VACUOUS_RETIRED
R13_K2_Q11_GAMMA_ODD_BRANCH = VACUOUS_RETIRED
R14_K1_GAMMA_NEXT_BIT       = RETIRED_BY_EXACT_R_FACTOR
R14_REVERSE_CANCELLATION_LOCUS = CURRENT
```

# 3. q=1 Verdict

```text
NEGATIVE_FOUR_T_THEOREM=PROVED
NEGATIVE_BRANCH=OPEN_AT_24_FIXED_(K,d,tau)_CASES / 12 DCDC residue cells
EQUAL_VALUATION_SECOND_LIFT=PROVED
K10=OPEN
K100=OPEN
K1000=OPEN
```

# 4. Coefficient Verdict

```text
FULL_COEFFICIENT_TABLE=PASS_26_ROWS
BOUNDARY_B0_GAMMA_DEGREE=1
HIGH_H0_GAMMA_DEGREE=1
BOUNDARY_NEWTON=OPEN_AFTER_EXPLICIT_LINEAR_GAMMA_ZERO_LOCUS
HIGH_NEWTON=OPEN_AFTER_EXPLICIT_LINEAR_GAMMA_ZERO_LOCUS
```

The prompt counted 24 coefficients, but degrees $4,4,7,7$ give exactly

$$5+5+8+8=\boxed{26}.$$

All 26 are extracted; there is no `UNEXTRACTED` row.

# 5. Frozen R12 Full-Root Recovery

The self-contained R14 frozen source reproduces the four R12 polynomial hashes exactly:

```text
R12_HASH_B_MATCH=PASS   92af2937c40fdf2dc056472228ec1a91d7b01444dd26f6f6718e68b261a35648
R12_HASH_H_MATCH=PASS   cf7b8ef58e9e24e8a63daf29d5d78ea5184bf19052a525563c5cb0ff80f5e180
R12_HASH_R_MATCH=PASS   9b67233170bf9203917a84ec309989dbe2d87351c0210342af6912dc3455a0b3
R12_HASH_K1_MATCH=PASS  d950fb494bfb4b4e4bcae5a4054f64041170856bfc2ecc78dc8aae9ea393afd2
DEGREES=4,4,7,7
```

Therefore R14 does not rerun the heavy R12 derivation. It works entirely with the frozen certified polynomials.

# 6. GNB-1 — Universal Reverse Carry Evenness

R7 has

$$D_R=2R^2d_0q^2(q+4)c=4fR^2q^2(q+4)c,$$

hence, because $f,q,q+4,c$ are odd in the two-adic audit,

$$\boxed{v_2(D_R)=2r+2}.$$

With

$$\Gamma_R=-\mathscr B_R+2q(D_Rs+\chi_R),$$

every term of $\mathscr B_R$ carrying $R$ is even, while the $R$-free tail is $2\alpha q^3(q+6)$. Thus

$$\boxed{2\mid\Gamma_R}$$

on every legal active reverse fibre. This already makes every low-$k$ `gamma odd` branch with normalizer one impossible.

# 7. GNB-2 — Exact R-Factor Theorem

The stronger source-level calculation uses the exact R7 integer polynomial $J_R$, $\chi_R=J_R-D_R\mu$, the legal tail substitution $\alpha=2RfBt-qe$, and $G=KR$. Exact expansion and collection prove

$$\boxed{\Gamma_R=R\Phi_R},$$

with

```text
Phi_R = 16*K**2*R**2*f*q**5*t + 32*K**2*R**2*f*q**4*t - 320*K**2*R**2*f*q**3*t
        - 896*K**2*R**2*f*q**2*t - 512*K**2*R**2*f*q*t - 8*K**2*R*e*q**3
        - 32*K**2*R*e*q**2 - 8*K*R*f*q**6*t + 16*K*R*f*q**5*t + 416*K*R*f*q**4*t
        + 576*K*R*f*q**3*t - 512*K*R*f*q**2*t - 512*K*R*f*q*t + 4*K*e*q**4
        + 16*K*e*q**3 - 16*K*e*q**2 - 8*R**2*f*q**6*t - 88*R**2*f*q**5*t
        - 272*R**2*f*q**4*t - 416*R**2*f*q**3*t + 512*R**2*f*q*t + 256*R**2*f*t
        + R*e*q**4 + 10*R*e*q**3 + 12*R*e*q**2 + 8*R*e*q
        - 8*R*f*mu*q**7 - 112*R*f*mu*q**6 - 416*R*f*mu*q**5 - 448*R*f*mu*q**4
        - 256*R*f*mu*q**3 + 8*R*f*s*q**7 + 112*R*f*s*q**6 + 416*R*f*s*q**5
        + 448*R*f*s*q**4 + 256*R*f*s*q**3
```

This is the exact cancellation mechanism requested by the R14 fallback rule. It is not evidence that actual roots exist; it says that **if** a legal reverse state exists, the carry numerator already contains a decimal-depth factor that grows with $r$.

## 7.1 Low-$k$ consequence

For special $k=1,b=0$, $(k,q)=(2,7)$, and $(k,q)=(2,11)$, the R12 normalizing cofactor is exactly one. Hence

$$\boxed{\gamma=\Gamma_R},\qquad \boxed{10^r\mid\gamma},\qquad \boxed{v_2(\gamma)\ge r}.$$

So the R13 conditional `gamma odd` branches are vacuous on the legal active fibres.

## 7.2 K1 tail parity

The special TQR law $2(q+4)\eta_1=e+8Rt(3q+5)$ implies

$$\boxed{e\equiv0\pmod2}.$$

Consequently the proposed first next-bit identity reduces to zero, not one. The correct conclusion is not $v_2(\gamma)=1$, but the stronger moving-depth theorem above.

# 8. Independent Root Splice on the Cancellation Locus

R14 substitutes the **exact existing** $\Gamma_R$ directly into the R12 independent root polynomial; no variable $\gamma/R$ is introduced. For all three normalizer-one low-$k$ branches, the substituted independent root polynomial gains exact structural order $R^2$.

## 8.1 Special K1

$$\boxed{-16q^4c\,[2q(q+4)t-5e]\,[e-8q^2(q+4)(\mu-s)]}.$$

## 8.2 $(k,q)=(2,7)$

$$\boxed{C_2=14213920000\,(-25e+77t)\,[e-4312(\mu-s)]}.$$

## 8.3 $(k,q)=(2,11)$

$$\boxed{C_2=6280403360000\,(-e+33t)\,[e-72600(\mu-s)]}.$$

The cyclotomic classes are

```text
k=1,q=7:  r == 2 (mod 6)
k=2,q=7:  r == 1 (mod 6)
k=2,q=11: r == 1 (mod 2)
```

No finite upper bound for $r$ follows yet because the displayed factors move with the state. Therefore none of the three types is falsely declared closed.

# 9. Gamma-Zero Locus

If $\gamma=0$, the independent constant coefficient vanishes. R14 performs the mandated finite coefficient descent.

Generic reverse:

$$\boxed{R_1=-1024ef^4q^5w^2(q^2+4q-4)(-Ke+4fq^2t+16fqt)}.$$

K1 special:

$$\boxed{S_1=640eq^5(-5e+2q^2t+8qt)(q^2+4q-4)}.$$

Thus $\gamma=0$ is reduced to explicit lowest-coefficient divisibility, but is not globally closed.

# 10. COEF-1 — Complete Frozen Coefficient Table

`J2-55-R14-FullCoefficientProfile.tsv` contains all

$$B_0,\ldots,B_4,\quad H_0,\ldots,H_4,\quad R_0,\ldots,R_7,\quad S_0,\ldots,S_7.$$

# 11. COEF-2/3 — Boundary and High Constant Gamma-Linearity

The exact common outer factor is

$$B_0=-16f^3w\,\mathcal B_0,$$

with

```text
e**2*f*q**9*w + 22*e**2*f*q**8*w + 164*e**2*f*q**7*w + 504*e**2*f*q**6*w + 816*e**2*f*q**5*w + 800*e**2*f*q**4*w + 448*e**2*f*q**3*w + 128*e**2*f*q**2*w - 16*e*f**2*q**11*t*w - 368*e*f**2*q**10*t*w - 2976*e*f**2*q**9*t*w - 12352*e*f**2*q**8*t*w - 35840*e*f**2*q**7*t*w - 65792*e*f**2*q**6*t*w - 37888*e*f**2*q**5*t*w + 21504*e*f**2*q**4*t*w + 49152*e*f**2*q**3*t*w + 32768*e*f**2*q**2*t*w + 8192*e*f**2*q*t*w + 64*f**3*q**13*t**2*w + 1536*f**3*q**12*t**2*w + 14656*f**3*q**11*t**2*w + 83840*f**3*q**10*t**2*w + 344320*f**3*q**9*t**2*w + 897536*f**3*q**8*t**2*w + 1088512*f**3*q**7*t**2*w - 51200*f**3*q**6*t**2*w - 1638400*f**3*q**5*t**2*w - 1769472*f**3*q**4*t**2*w - 294912*f**3*q**3*t**2*w + 786432*f**3*q**2*t**2*w + 589824*f**3*q*t**2*w + 131072*f**3*t**2*w + 16*gamma*q**5*t + 64*gamma*q**4*t
```

and

$$H_0=-16f^3w\,\mathcal H_0,$$

with

```text
256*H**4*e*f**2*q**9*t*w + 2048*H**4*e*f**2*q**8*t*w + 3072*H**4*e*f**2*q**7*t*w - 4096*H**4*e*f**2*q**6*t*w - 512*H**4*f**3*q**11*t**2*w - 1024*H**4*f**3*q**10*t**2*w + 30720*H**4*f**3*q**9*t**2*w + 143360*H**4*f**3*q**8*t**2*w + 114688*H**4*f**3*q**7*t**2*w - 163840*H**4*f**3*q**6*t**2*w - 131072*H**4*f**3*q**5*t**2*w - 64*H**2*e*f**2*q**9*t*w - 896*H**2*e*f**2*q**8*t*w - 5632*H**2*e*f**2*q**7*t*w - 15872*H**2*e*f**2*q**6*t*w - 15360*H**2*e*f**2*q**5*t*w - 4096*H**2*e*f**2*q**4*t*w + 256*H**2*f**3*q**11*t**2*w + 6144*H**2*f**3*q**10*t**2*w + 57344*H**2*f**3*q**9*t**2*w + 241664*H**2*f**3*q**8*t**2*w + 458752*H**2*f**3*q**7*t**2*w + 278528*H**2*f**3*q**6*t**2*w - 294912*H**2*f**3*q**5*t**2*w - 425984*H**2*f**3*q**4*t**2*w - 131072*H**2*f**3*q**3*t**2*w - 16*H**2*gamma*q**5*t - 64*H**2*gamma*q**4*t + e**2*f*q**9*w + 22*e**2*f*q**8*w + 164*e**2*f*q**7*w + 504*e**2*f*q**6*w + 816*e**2*f*q**5*w + 800*e**2*f*q**4*w + 448*e**2*f*q**3*w + 128*e**2*f*q**2*w - 16*e*f**2*q**11*t*w - 368*e*f**2*q**10*t*w - 3168*e*f**2*q**9*t*w - 13504*e*f**2*q**8*t*w - 33280*e*f**2*q**7*t*w - 45824*e*f**2*q**6*t*w - 22528*e*f**2*q**5*t*w + 25600*e*f**2*q**4*t*w + 49152*e*f**2*q**3*t*w + 32768*e*f**2*q**2*t*w + 8192*e*f**2*q*t*w + 64*f**3*q**13*t**2*w + 1536*f**3*q**12*t**2*w + 14912*f**3*q**11*t**2*w + 78720*f**3*q**10*t**2*w + 256256*f**3*q**9*t**2*w + 512512*f**3*q**8*t**2*w + 515072*f**3*q**7*t**2*w - 165888*f**3*q**6*t**2*w - 1212416*f**3*q**5*t**2*w - 1343488*f**3*q**4*t**2*w - 163840*f**3*q**3*t**2*w + 786432*f**3*q**2*t**2*w + 589824*f**3*q*t**2*w + 131072*f**3*t**2*w
```

The structural result is

$$\boxed{\deg_\gamma\mathcal B_0=\deg_\gamma\mathcal H_0=1}.$$

More precisely,

$$[\gamma]\mathcal B_0=16q^4(q+4)t,$$

$$[\gamma]\mathcal H_0=-16H^2q^4(q+4)t.$$

There is no $\gamma^2$ term. The zero loci are single rational gamma values:

```text
B0=0 => gamma = -f*w*(e**2*q**9 + 22*e**2*q**8 + 164*e**2*q**7 + 504*e**2*q**6 + 816*e**2*q**5 + 800*e**2*q**4 + 448*e**2*q**3 + 128*e**2*q**2 - 16*e*f*q**11*t - 368*e*f*q**10*t - 2976*e*f*q**9*t - 12352*e*f*q**8*t - 35840*e*f*q**7*t - 65792*e*f*q**6*t - 37888*e*f*q**5*t + 21504*e*f*q**4*t + 49152*e*f*q**3*t + 32768*e*f*q**2*t + 8192*e*f*q*t + 64*f**2*q**13*t**2 + 1536*f**2*q**12*t**2 + 14656*f**2*q**11*t**2 + 83840*f**2*q**10*t**2 + 344320*f**2*q**9*t**2 + 897536*f**2*q**8*t**2 + 1088512*f**2*q**7*t**2 - 51200*f**2*q**6*t**2 - 1638400*f**2*q**5*t**2 - 1769472*f**2*q**4*t**2 - 294912*f**2*q**3*t**2 + 786432*f**2*q**2*t**2 + 589824*f**2*q*t**2 + 131072*f**2*t**2)/(16*q**4*t*(q + 4))
H0=0 => gamma = f*w*(256*H**4*e*f*q**9*t + 2048*H**4*e*f*q**8*t + 3072*H**4*e*f*q**7*t - 4096*H**4*e*f*q**6*t - 512*H**4*f**2*q**11*t**2 - 1024*H**4*f**2*q**10*t**2 + 30720*H**4*f**2*q**9*t**2 + 143360*H**4*f**2*q**8*t**2 + 114688*H**4*f**2*q**7*t**2 - 163840*H**4*f**2*q**6*t**2 - 131072*H**4*f**2*q**5*t**2 - 64*H**2*e*f*q**9*t - 896*H**2*e*f*q**8*t - 5632*H**2*e*f*q**7*t - 15872*H**2*e*f*q**6*t - 15360*H**2*e*f*q**5*t - 4096*H**2*e*f*q**4*t + 256*H**2*f**2*q**11*t**2 + 6144*H**2*f**2*q**10*t**2 + 57344*H**2*f**2*q**9*t**2 + 241664*H**2*f**2*q**8*t**2 + 458752*H**2*f**2*q**7*t**2 + 278528*H**2*f**2*q**6*t**2 - 294912*H**2*f**2*q**5*t**2 - 425984*H**2*f**2*q**4*t**2 - 131072*H**2*f**2*q**3*t**2 + e**2*q**9 + 22*e**2*q**8 + 164*e**2*q**7 + 504*e**2*q**6 + 816*e**2*q**5 + 800*e**2*q**4 + 448*e**2*q**3 + 128*e**2*q**2 - 16*e*f*q**11*t - 368*e*f*q**10*t - 3168*e*f*q**9*t - 13504*e*f*q**8*t - 33280*e*f*q**7*t - 45824*e*f*q**6*t - 22528*e*f*q**5*t + 25600*e*f*q**4*t + 49152*e*f*q**3*t + 32768*e*f*q**2*t + 8192*e*f*q*t + 64*f**2*q**13*t**2 + 1536*f**2*q**12*t**2 + 14912*f**2*q**11*t**2 + 78720*f**2*q**10*t**2 + 256256*f**2*q**9*t**2 + 512512*f**2*q**8*t**2 + 515072*f**2*q**7*t**2 - 165888*f**2*q**6*t**2 - 1212416*f**2*q**5*t**2 - 1343488*f**2*q**4*t**2 - 163840*f**2*q**3*t**2 + 786432*f**2*q**2*t**2 + 589824*f**2*q*t**2 + 131072*f**2*t**2)/(16*H**2*q**4*t*(q + 4))
```

Modulo $q$,

$$\boxed{B_0\equiv H_0\equiv-2^{21}f^6t^2w^2\pmod q}.$$

Hence

$$\boxed{B_0=0\ \text{or}\ H_0=0\Longrightarrow q\mid t}.$$

This replaces “constant coefficient cancellation uncontrolled” by an explicit one-value gamma locus on the $q\mid t$ branch. A uniform Newton/sign closure is not completed in R14.

# 12. NEG-1 — Negative Four-t Theorem

Primitive deflation gives $a_3=da$, $m=dn$, $t=d\tau$, with $\gcd(a,n)=1$ and $d,\tau$ ten-units. If

$$M=G^3\tau-(10G^2+4G-2)a<0,$$

then $a_3=da<G$ gives $a<G/d$, so

$$\boxed{d\tau<10+\frac4G-\frac2{G^2}<11}$$

for live $G\ge10^4$. Hence

$$\boxed{M<0\Longrightarrow t\in\{1,3,7,9\}}.$$

The only factor pairs are

$$\boxed{(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)}.$$

# 13. Negative 12-cell DCDC Table

| K | t | $a_3\pmod{2K}$ | ten-unit | $(d,\tau)$ possibilities |
|---:|---:|---:|:---:|---|
|10|1|9|PASS|(1,1)|
|10|3|7|PASS|(1,3),(3,1)|
|10|7|3|PASS|(1,7),(7,1)|
|10|9|1|PASS|(1,9),(3,3),(9,1)|
|100|1|129|PASS|(1,1)|
|100|3|187|PASS|(1,3),(3,1)|
|100|7|103|PASS|(1,7),(7,1)|
|100|9|161|PASS|(1,9),(3,3),(9,1)|
|1000|1|129|PASS|(1,1)|
|1000|3|387|PASS|(1,3),(3,1)|
|1000|7|903|PASS|(1,7),(7,1)|
|1000|9|1161|PASS|(1,9),(3,3),(9,1)|

Thus the negative q=1 frontier is no longer 888 cells. It is at most 24 fixed $(K,d,\tau)$ infinite cases, represented by 12 DCDC residue cells. A diagnostic through $g\le7$ found zero negative Gaussian square states, but this finite search is not promoted to a theorem.

# 14. GS2-1 — Equal-Valuation First Support Second Lift

For $h=v_p(G+1)=v_p(\tau+4a)\ge1$ and $p\equiv3\pmod4$, write $G+1=p^hg_1$ and $\tau+4a=p^h\ell_1$. The identity

$$M=-(\tau+4a)+(G+1)U_1$$

with $U_1\equiv4a\pmod p$ gives

$$v_p(M)>h\iff\ell_1\equiv4ag_1\pmod p,$$

or equivalently

$$\boxed{p^{h+1}\mid\tau-4aG}.$$

# 15. GS2-2 — Equal-Valuation Second Support Second Lift

For $h=v_p(2G+3)=v_p(27\tau+116a)$, use

$$8M=-(27\tau+116a)+(2G+3)U_2$$

with $U_2\equiv-12a\pmod p$. Then

$$v_p(M)>h\iff\ell_2\equiv-12ag_2\pmod p,$$

and the cleared congruence is

$$\boxed{p^{h+1}\mid27\tau+24aG+152a}.$$

The Gaussian budget remains

$$\boxed{v_p(M)\le2h}.$$

Thus the equal-valuation second lift is complete, but a global support contradiction is not yet proved.

# 16. Success Audit

| Success | Verdict | R14 result |
|---|---|---|
| A mandatory gamma-odd correction | **ACHIEVED** | all three low-k odd branches vacuous |
| B exact next-bit theorem | **SUPERSEDED** | exact $R$-factor is stronger; no bounded next bit |
| C one low-k closure | **NOT ACHIEVED** | three priority types remain on carry-spliced coefficient loci |
| D generic reverse depth bound | **NEGATIVE RESULT / NEW LOCUS** | no absolute bound; exact $\Gamma_R=R\Phi_R$ mechanism exposed |
| E coefficient artifact completion | **ACHIEVED** | all 26 coefficients, all four hashes match |
| F q1 negative finite collapse | **ACHIEVED** | $t\in\{1,3,7,9\}$, 8 pairs, 12 cells |
| G q1 negative closure | **NOT ACHIEVED** | 24 fixed infinite cases remain |
| H Gaussian equal-valuation theorem | **ACHIEVED** | both second lifts exact-certified |
| I one q1 K closure | **NOT ACHIEVED** | K=10,100,1000 open |
| J boundary/high closure | **NOT ACHIEVED** | explicit gamma-linear zero loci obtained |
| K terminal J2 | **NOT ACHIEVED** | J2 OPEN |

# 17. New Exact Frontier After R14

Reverse:

$$\boxed{\Gamma_R=R\Phi_R\quad+\quad P_R(10^r)=0}$$

with explicit carry-spliced lowest coefficients in the priority low-$k$ types. This replaces “gamma parity open”.

q=1 negative:

$$\boxed{K\in\{10,100,1000\},\quad t\in\{1,3,7,9\},\quad(d,\tau)\text{ in 8 pairs}}$$

rather than 888 cells.

q=1 support:

$$\boxed{\text{first-order support}+\text{equal-valuation second lift}+\text{Gaussian budget}}.$$

Boundary/high now have complete independent coefficient tables, with constant cancellation reduced to one explicit gamma value.

# 18. Artifact Audit

Generated and executed:

```text
J2-55-R14-GammaNextBit.py
J2-55-R14-GammaBit.tsv
J2-55-R14-FrozenRootPolynomials.py
J2-55-R14-FullCoefficientProfile.tsv
J2-55-R14-ReverseBitClosure.py
J2-55-R14-q1-NegativeBranch.py
J2-55-R14-q1-SecondSupportLift.py
J2-55-R14-certificate.txt
J2-55-R14-survivors.tsv
J2-55-R14-counterexamples.tsv
```

Additional diagnostics:

```text
J2-55-R14-ReverseBitClosure.tsv
J2-55-R14-q1-NegativeCells.tsv
J2-55-R14-q1-NegativeDiagnostic.tsv
J2-55-R14-q1-SecondSupportLift.tsv
```

No closure certificate is generated because J2 remains OPEN.

# 19. Terminal Statement

R14 does not close J2. Its decisive correction is

$$\boxed{\Gamma_R=R\Phi_R},$$

so continuing the gamma bit ladder would only rediscover growing decimal depth. The next reverse task is the explicit carry-cancellation locus against the independent degree-seven root polynomial.

For q=1, the negative branch is reduced to four possible $t$ values / 24 fixed scale cases, and the equal-valuation support lift is exact. For boundary/high, the coefficient artifact gap is repaired and the constant coefficient is linear in $\gamma$.

$$\boxed{\textbf{J2 OPEN}}.$$
