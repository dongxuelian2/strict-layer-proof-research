# J2-55 R15 — Carry-Spliced Lowest-Factor × Independent 2-Adic Coefficient × Negative Fixed-Conic Report

**Scope:** Strict Layer — $A_1$-only — Exact Resonance $R=0$ — $J=2$ only  
**Campaign:** 55 第十五轮 / 统一终端线第二十五轮  
**Dependency discipline:** R14 exact $\Gamma_R=R\Phi_R$ is frozen and the gamma-bit ladder remains retired. All new q>1 statements use the independent R12 root polynomials or their R14 carry splice.

# 1. Executive Status

$$\boxed{\textbf{J2 OPEN}}$$

```text
HIGH=OPEN
BOUNDARY=OPEN
REVERSE_K1_Q7=OPEN
REVERSE_K2_Q7=OPEN
REVERSE_K2_Q11=OPEN
Q1_NEGATIVE=OPEN
Q1_POSITIVE=OPEN
FULL_J2=OPEN
```

No `J2-Resonance-Closure-Certificate.md` is generated.

R15 does **not** obtain the requested K2 finite-$r$ theorem. The reason is structural rather than computational: the inherited primitive theorem gives $\gcd(x,u)=1$, not $\gcd(x,10)=1$, so the moving factor $e-cx$ may carry arbitrarily deep $2$/$5$ content under the currently frozen low-$k$ information. Reduced-gate pseudo-families certify that parity + TQR + LOW/height alone cannot imply an absolute $r$ bound. These pseudo-families are **not** admissible J2 states and are not counterexamples to the theorem being sought.

The strongest new positive result is instead the independent-coefficient binary descent:

$$\boxed{\text{every live Boundary/High actual root forces }4\mid e.}$$

Moreover

$$\boxed{\text{High and }g\ge9\Longrightarrow 8\mid e.}$$

The $g=6$ Boundary edge required by the $v_2(e)=1$ analysis is closed exactly by the inherited DCDC/RCE system.

# 2. Low-k Factor Verdict

```text
K2_Q7_C2_FACTOR_PARITY=EXACTLY_ONE_ODD_ONE_EVEN
K2_Q7_R_BOUND=NOT_PROVED
K2_Q7_STATUS=OPEN

K2_Q11_C2_FACTOR_PARITY=EXACTLY_ONE_ODD_ONE_EVEN
K2_Q11_R_BOUND=NOT_PROVED
K2_Q11_STATUS=OPEN

K1_GCD2_FACTOR=v2(gcd(F1,F2))=1 PROVED
K1_GCD5_FACTOR=CONDITIONAL_ONLY; global theorem NOT proved
K1_Q7_STATUS=OPEN
```

# 3. Boundary/High Bit Verdict

```text
B0_MOD2=e^2
H0_MOD2=e^2
BH_E_EVEN=PROVED
HIGH_E_DIV4=PROVED
BOUNDARY_G_GT6_E_DIV4=PROVED
BOUNDARY_G6_EDGE=CLOSED_BY_DCDC
BOUNDARY_ALL_LIVE_E_DIV4=PROVED
HIGH_G_GE_9_E_DIV8=PROVED
BINARY_AUTOMATON=PARTIAL; explicit stable cells remain
HIGH_STATUS=OPEN
BOUNDARY_STATUS=OPEN
```

A prompt-level candidate is corrected:

$$\boxed{\mathcal B_0/16\equiv e/4+\gamma\pmod2}$$

but

$$\boxed{\mathcal H_0/16\equiv e/4\pmod2,}$$

not $e/4+\gamma$. The High gamma term carries an $H^2$ factor and vanishes at this bit.

# 4. q=1 Negative Verdict

```text
NEGATIVE_FIXED_CASES=24
NEGATIVE_CONIC_LOCAL=NO_ALL_A_KILLER_PRIME_p<200 (diagnostic, not theorem)
NEGATIVE_LATTICE=EXACT; uniform one-step squeeze FALSE
K10_NEG=OPEN_FIXED_NORM_ORBIT
K100_NEG=OPEN_FIXED_NORM_ORBIT
K1000_NEG=OPEN_FIXED_NORM_ORBIT
NEGATIVE_BRANCH=OPEN_FIXED_TAU_PELL_NORM_ORBITS
```

The branch is nevertheless strictly below R14's mere “24 fixed cases”: every case now has one explicit residue lattice and one exact dehomogenized norm equation.

# 5. Frozen Carry-Spliced Coefficients

For the two priority $k=2$ types R14 gives

$$C_{2,7}=14213920000(-25e+77t)(e-4312x),$$

$$C_{2,11}=6280403360000(-e+33t)(e-72600x),$$

with $x=\mu-s$. The outer constants have exact valuations

$$v_2=8,\qquad v_5=4.$$

Because $t$ is odd,

$$-25e+77t\equiv e+1\pmod2,\qquad e-4312x\equiv e\pmod2,$$

and similarly

$$-e+33t\equiv e+1\pmod2,\qquad e-72600x\equiv e\pmod2.$$

Hence in each type

$$\boxed{\text{exactly one factor is odd and the other is even}.}$$

This corrects any “product odd” wording.

## 5.1 Why the desired finite $r$ bound is not yet legal

The proposed shortcut $v_2(4312x)=3$ or $v_5(4312x)=0$ requires $x$ to be a ten-unit. The frozen primitive recovery supplies only

$$\gcd(x,u)=1.$$

Since $u=(G+1)/q$ is itself coprime to $10$, this does not constrain $v_2(x)$ or $v_5(x)$. Therefore no absolute bound for the even factor follows from the current provenance.

The same obstruction affects the $5$-content.

## 5.2 $F_2=0$ is nevertheless impossible for both K2 types

For $k=2$, $G=100R$ and

$$A=2(G+1)/q+1>\frac{200R}{q},$$

so the actual root lower bound gives

$$x>\frac{AG}{10}>\frac{2000}{q}R^2.$$

The reverse tail relation and $|\alpha|<30fq^4R^2$, $t<9qR$ give the safe bound

$$|e|<(18fB+30fq^3)R^2.$$

For $q=7$, $f=1,B=153$, $F_2=0$ would imply

$$e>\frac{4312\cdot2000}{7}R^2>1.23\times10^6R^2,$$

whereas the safe upper coefficient is $13044$. Contradiction.

For $q=11$, $f=5,B=949$, $F_2=0$ implies

$$e>\frac{72600\cdot2000}{11}R^2=13.2\times10^6R^2,$$

whereas the safe upper coefficient is $285060$. Contradiction.

Thus

$$\boxed{F_{7,2}\ne0,\qquad F_{11,2}\ne0.}$$

This is a genuine shrink of the splice-factor frontier, although it does not bound its valuation.

## 5.3 Reduced-gate pseudo-families disprove the proposed proof route

The executable ledger contains exact families satisfying the specific ingredients used by the proposed finite-depth route: cyclotomic class, odd $t$, tail height, TQR, LOW, and $R\mid C_2$. For example:

- $q=7$, $r\equiv1\pmod6$: $x=300R^2$, $e=10000R^2$, $t=175$;
- $q=11$, odd $r$: $x=200R^2$, $e=100000R^2$, $t=1$.

The even splice factor then absorbs growing powers of $R$. These states deliberately do **not** assert RCE, DCDC, primitive reconstruction, or the full root equation. Their logical role is only:

$$\boxed{\text{parity + TQR + LOW/height }\not\Rightarrow\text{ absolute }r\text{-bound}.}$$

Accordingly K2-1 and K2-2 are downgraded rather than falsely declared.

The surviving cyclotomic classes remain

$$q=7,k=2:\quad r\equiv1\pmod6,\quad r=1\text{ already frozen dead},$$

so the live sequence begins $7,13,19,\ldots$, while

$$q=11,k=2:\quad r\equiv1\pmod2,$$

with $r=1$ frozen dead and live $3,5,7,\ldots$.

# 6. K1 Factor Allocation

For special $k=1,b=0$ let

$$F_1=2q(q+4)t-5e,\qquad F_2=e-8q^2(q+4)x.$$

Exact algebra gives

$$\boxed{F_1+5F_2=2q(q+4)(t-20qx).}$$

The special TQR forces $e$ even and the inherited theorem has $t$ odd. Thus both $F_1,F_2$ are even, while $t-20qx$ is odd. Hence

$$v_2(F_1+5F_2)=1$$

and therefore

$$\boxed{\min(v_2(F_1),v_2(F_2))=1}$$

or equivalently

$$\boxed{v_2(\gcd(F_1,F_2))=1.}$$

This is the requested exact two-factor $2$-allocation theorem.

The analogous global $5$-adic statement is **not** certified. Two provenance blockers intervene:

1. the R8 equality $v_5(t)=v_5(c)$ was proved only in its stated applicable scope and cannot be promoted to all $k=1$ branches;
2. $x$ is not known to be a $5$-unit.

Conditionally, if $x$ is a $5$-unit and $v_5(t)\ge2$, then

$$v_5(t-20qx)=1.$$

If $v_5(t)=1$, the possible deeper overlap is exactly

$$t/5\equiv4qx\pmod5.$$

For $q=7$, the current safe height comparison does not kill $F_2=0$: the required lower coefficient is $86240/7\approx12320$, while the safe upper coefficient is $13044$. The live cyclotomic class remains

$$r\equiv2\pmod6,$$

with $r=2$ frozen in the old $\ell=5$ closure and hence $r\ge8$ live. No absolute $r$ bound is obtained.

# 7. Boundary/High Independent Coefficient Descent

Write

$$B_0=-16f^3w\,\mathcal B_0,\qquad H_0=-16f^3w\,\mathcal H_0,$$

where $f,w$ are odd. Exact reduction of the frozen R14 constant coefficients gives

$$\boxed{\mathcal B_0\equiv e^2\pmod2,\qquad \mathcal H_0\equiv e^2\pmod2.}$$

If $e$ were odd, $v_2(B_0)=v_2(H_0)=4$. This is incompatible with $G=10^g$ for every live Boundary ($g\ge6$) or High ($g\ge7$) root. The same congruence also handles the coefficient-zero locus. Therefore

$$\boxed{\text{BH actual root}\Longrightarrow 2\mid e.}$$

Set temporarily $e=2E$. Exact division gives

$$\frac{\mathcal B_0}{4}\equiv E^2\pmod2,\qquad
\frac{\mathcal H_0}{4}\equiv E^2\pmod2.$$

Thus $v_2(e)=1$ gives exact $v_2(B_0)=v_2(H_0)=6$. High is immediately impossible. Boundary can only have $g=6$.

## 7.1 Exact closure of the Boundary $g=6$ edge

For $G=10^6$,

$$G+1=1000001=101\cdot9901.$$

The $q=1$ boundary is frozen closed and the $u=1$ endpoint $q=G+1$ is frozen closed. The two proper $q$ values were replayed through the exact inherited N-strip, digit congruence, reconstruction, linear legality, and DCDC gates:

```text
q=101:
  N=2,598,000
  congruence=46,311
  reconstructed=23,089
  linear_legal=7,398
  DCDC=0

q=9901:
  N=2,598,000
  congruence=0
```

Hence

$$\boxed{g=6\text{ Boundary is empty}.}$$

Combining this with the coefficient theorem yields the stronger global statement

$$\boxed{\text{every live Boundary actual root forces }4\mid e.}$$

Thus both nonnegative chambers are now content-deflated to $e=4E$.

## 7.2 Third bit: Boundary and High separate

For $e=4E$,

$$\boxed{\mathcal B_0/16\equiv E+\gamma\pmod2,}$$

but

$$\boxed{\mathcal H_0/16\equiv E\pmod2.}$$

Consequently, if $v_2(e)=2$, High has exact $v_2(H_0)=8$. Therefore

$$\boxed{\text{High},\ g\ge9\Longrightarrow 8\mid e.}$$

For Boundary, $v_2(e)=2$ with $\gamma$ even also has exact $v_2(B_0)=8$ and is killed for $g\ge9$; the $\gamma$-odd cell lifts.

At the next High bit, with $e=8E$,

$$\mathcal H_0/64\equiv E+\gamma\pmod2\quad(\delta=1,H=10),$$

while

$$\mathcal H_0/64\equiv E\pmod2\quad(\delta\ge2).$$

These are explicit finite binary cells, but a no-infinite-accepting-branch theorem is not yet proved.

## 7.3 Boundary constant-zero $q\mid t$ locus: next independent coefficient

On $t=q\tau$ and $\gamma=q\gamma_1$, the exact $G^1$ coefficient factors as

$$\boxed{B_1=-8f^2q^2w\,J.}$$

After the already-proved $e=4E$ and with the odd structural variables,

$$\boxed{J/4\equiv E\gamma_1\pmod2.}$$

Thus if both $E=e/4$ and $\gamma/q$ are odd, then $v_2(B_1)=5$, far below every live $g\ge6$, and the root is impossible. The constant-zero branch therefore survives only on the explicit thinner locus

$$\boxed{(e/4)(\gamma/q)\equiv0\pmod2.}$$

This is independent-coefficient descent, not a restart of R7 q-descent.

# 8. q=1 Negative Fixed Cases

R14 freezes

$$K\in\{10,100,1000\},\qquad
(d,\tau)\in\{(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)\}.$$

For each of the 24 cases the DCDC cell is

$$\boxed{31a+\tau\equiv0\pmod{2K},}$$

so there is a unique residue $a\equiv a_0\pmod{2K}$. The negative window is

$$\boxed{\frac{G^3\tau}{A_G}<a<\frac Gd},\qquad A_G=10G^2+4G-2.$$

For

$$m_-=A_Ga-G^3\tau>0,$$

the arithmetic progression is exactly

$$\boxed{m_-\equiv A_Ga_0-G^3\tau\pmod{2KA_G}.}$$

## 8.1 The proposed uniform one-step lattice squeeze is false

The number of lattice steps across the full $a$-window is exactly

$$\boxed{
\frac{\text{window width}}{2K}
=\frac{R\big((10-t)G^2+4G-2\big)}{2d(10G^2+4G-2)},
\qquad t=d\tau.
}$$

Since $t\in\{1,3,7,9\}$, this is asymptotic to

$$\frac{R(10-t)}{20d},$$

and hence grows linearly with $R=G/K$. For example $K=1000,d=9,\tau=1,G=10^7$ gives approximately $55.56$ steps. Thus no uniform “at most one lattice candidate” theorem exists from the raw window, even for $K=1000$.

## 8.2 Exact NEG-G radical lower bound

With $S=(G+1)(2G+3)$, $C=G^3\tau$ and the frozen $Q_K(G)$, substituting $a=(m_-+C)/A_G$ into NEG-G and clearing $A_G^2$ gives an exact quadratic inequality

$$a_2m_-^2+b_2m_-+c_2\ge0,$$

where

$$a_2=Q_KA_G^2-4SA_G-4GS^2,$$

$$b_2=-4SA_GC-8GS^2C,$$

$$c_2=-4GS^2C^2.$$

Whenever $a_2>0$, the exact positive-root lower bound is

$$\boxed{m_-\ge\frac{-b_2+\sqrt{b_2^2-4a_2c_2}}{2a_2}.}$$

This is recorded casewise but does not make the full interval uniformly shorter than one lattice step.

# 9. Fixed-$\tau$ Dehomogenized Conic / Norm Form

For every fixed $(K,d,\tau)$, the q=1 discriminant becomes

$$Y_0^2=A_2(G,K)a^2+B_1(G,K,\tau)a+C_0(G,K,\tau),$$

with

$$\begin{aligned}
A_2={}&100G^6K^2-100G^6+280G^5K^2-380G^5+236G^4K^2-545G^4\\
&+16G^3K^2-362G^3-52G^2K^2-93G^2-8GK^2+4K^2,
\end{aligned}$$

$$B_1=-G^2\tau(20G^5K^2-20G^5+48G^4K^2-68G^4+32G^3K^2-85G^3-46G^2-4GK^2-4G+3),$$

$$C_0=\frac{G^5\tau^2}{4}Q_K(G).$$

Its discriminant as a quadratic in $a$ factors exactly:

$$\boxed{\Delta_a=G^4\tau^2(G+1)^2(2G+3)^2T_4(G,K),}$$

where

$$T_4=4G^4K^2-4G^4+8G^3K^2-12G^3+4G^2K^2-13G^2-6G+1.$$

Completing the square gives the exact norm equation

$$\boxed{(2A_2a+B_1)^2-4A_2Y_0^2=\Delta_a.}$$

Therefore the 24 negative cases are no longer merely “fixed conics”; each is a fixed-$\tau$ Pell/norm orbit constrained by one arithmetic progression and the negative interval. This is the correct next global object.

A bounded search for a single prime $p<200$, $p\nmid10K$, that makes the right-hand side nonsquare for **all** free $a\bmod p$ and all $G$ phases found none in any of the 24 cases. This is diagnostic only; per the campaign discipline the prime hunt is stopped rather than extended.

# 10. Gamma-Zero Reverse Locus

R14's $\gamma=0$ lowest coefficients are

$$R_1=-1024ef^4q^5w^2(q^2+4q-4)(-Ke+4fq(q+4)t),$$

$$S_1=640eq^5(q^2+4q-4)(-5e+2q(q+4)t).$$

On the three priority normalizer-one low-$k$ types, the last linear factor is exactly the same $F_1$ already occurring in the carry-spliced $C_2$, up to a fixed scalar:

```text
K1:     L = F1
K2 q=7: L = 4 F1
K2 q=11:L = 100 F1
```

Hence:

- $e=0$: $C_1=0$, but $C_2$ is a nonzero multiple of $tx$ for $t,x>0$, so the lowest coefficient is $j=2$;
- $e\ne0$, $F_1\ne0$: the $j=1$ coefficient is active;
- $e\ne0$, $F_1=0$: **both $C_1$ and $C_2$ vanish**, so the descent reaches $j\ge3$.

Thus

$$\boxed{\gamma=0\text{ remains OPEN on an explicit double-cancellation locus}.}$$

This is a stricter frontier than R14's generic “$C_1$ divisibility”, but GZ-1 is not proved.

# 11. Conjecture / Success Ledger

| Target | R15 verdict |
|---|---|
| K2-1 $(2,7)\Rightarrow r\le8$ | **DOWNGRADED / NOT PROVED**; reduced-gate unbounded family blocks proposed route |
| K2-2 $(2,11)\Rightarrow r\le8$ | **DOWNGRADED / NOT PROVED** |
| K2-3/4 type closures | **OPEN** |
| K1-1 $v_2(\gcd(F_1,F_2))=1$ | **PROVED** |
| K1-2 common $5$-depth | **CONDITIONAL ONLY**; provenance blockers recorded |
| K1-3 $F_2\ne0$ | **K2 PROVED; K1 q7 NOT PROVED** |
| K1-4 $(1,7)$ closure | **OPEN** |
| BH-1 BH root $\Rightarrow2\mid e$ | **PROVED** |
| BH-2 High $\Rightarrow4\mid e$ | **PROVED** |
| BH-3 Boundary $g\ge7\Rightarrow4\mid e$ | **PROVED**, strengthened to all live Boundary after exact $g=6$ closure |
| BH-4 no infinite binary accepting branch | **OPEN / PARTIAL AUTOMATON** |
| BH-5 High closure | **OPEN** |
| BH-6 Boundary closure | **OPEN** |
| NEG-1/2 negative closure | **OPEN**, but converted to 24 exact Pell/norm orbit problems |
| GZ-1 gamma-zero closure | **OPEN**, explicit double cancellation isolated |
| Full J2 | **OPEN** |

Success-standard audit:

```text
Success A BH=>2|e                         = ACHIEVED
Success B two K2 explicit finite r bound = NOT ACHIEVED; proposed route falsified
Success C one K2 closure                  = NOT ACHIEVED
Success D K1 exact 2/5 allocation         = PARTIAL: 2-adic PROVED, 5-adic conditional only
Success E High=>4|e + next bit            = ACHIEVED; strengthened to High g>=9=>8|e
Success F nonnegative infinite closure    = NOT ACHIEVED
Success G q1 negative closure             = NOT ACHIEVED
Success H one q1 K closure                = NOT ACHIEVED
Success I gamma-zero closure              = NOT ACHIEVED
Success J terminal J2                     = NOT ACHIEVED
```

# 12. Frontier Strictly After R15

R15 does not return the R14 frontier unchanged.

### High

$$\boxed{e=4E,\quad g\ge9\Rightarrow 2\mid E,}$$

with an explicit next-bit split at $\delta=1$ versus $\delta\ge2$.

### Boundary

$$\boxed{e=4E\text{ for every live root};\quad g=6\text{ retired},}$$

and on the $q\mid t$ constant-zero locus

$$\boxed{(e/4)(\gamma/q)\equiv0\pmod2}$$

is required by $B_1$.

### Reverse K2

$$\boxed{R\mid C_2,\quad\text{exactly one factor odd},\quad F_2\ne0,}$$

but the missing theorem is now explicitly identified as a valuation-control theorem stronger than current TQR/LOW, not another carry bit.

### Reverse K1

$$\boxed{v_2(\gcd(F_1,F_2))=1}$$

is frozen; the next work must resolve the $5$-scope issue or use a different allocation mechanism.

### q=1 negative

$$\boxed{24\text{ fixed residue-constrained Pell/norm orbit problems}}$$

replace the bare 24-case label.

### gamma-zero

$$\boxed{e=0\to j=2;\quad e\ne0,F_1\ne0\to j=1;\quad e\ne0,F_1=0\to j\ge3.}$$

# 13. Artifact Audit

Generated and executed:

```text
J2-55-R15-K2FactorClosure.py
J2-55-R15-K2FactorClosure.tsv
J2-55-R15-K1FactorAllocation.py
J2-55-R15-BH2AdicCoefficient.py
J2-55-R15-BH2AdicCells.tsv
J2-55-R15-q1-NegativeFixed.py
J2-55-R15-q1-NegativeFixed.tsv
J2-55-R15-q1-NegativeConic.py
J2-55-R15-q1-NegativeConic-certificate.txt
J2-55-R15-GammaZero.py
J2-55-R15-survivors.tsv
J2-55-R15-counterexamples.tsv
J2-55-R15-certificate.txt
```

No closure certificate is generated because

$$\boxed{\textbf{J2 OPEN}.}$$
