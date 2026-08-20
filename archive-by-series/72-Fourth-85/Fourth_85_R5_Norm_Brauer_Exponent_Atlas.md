# Fourth 85 · R5 — Specialized Norm–Brauer Exploitation × Hilbert-Symbol Exponent Atlas × Local-Cover Audit

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — \(J=2\)  
**Round:** 第四个八五计划 · R5  
**Checkpoint:** First Five-Round Architecture Checkpoint

---

# 1. Executive Verdict

R5 **没有**证明

\[
K=100\Longrightarrow\varnothing
\qquad\text{或}\qquad
K=1000\Longrightarrow\varnothing.
\]

所以也没有证明

\[
q=1\Longrightarrow\varnothing
\quad\text{或}\quad
J=2\Longrightarrow\varnothing.
\]

但 R5 得到了比“更多 killer primes”更强的结构性结果：

\[
\boxed{
(A_2(G,K),T_4(G,K))
=
(-1,T_4(G,K))
\quad\text{in }\operatorname{Br}(\mathbf Q(G))[2].
}
\tag{R5-BR}
\]

因此 R4 的 fixed norm/Brauer class 被完整降成 **Gaussian norm class**。

对每个实际 specialization \(G=10^g\)：

\[
\boxed{
\beta_{K,g}
=
(A_{K,g},T_{K,g})
=
(-1,T_{K,g}).
}
\]

于是 specialized norm conic

\[
x^2-A_{K,g}v^2=T_{K,g}
\]

在 \(\mathbf Q\) 上有点，当且仅当

\[
T_{K,g}
\in N_{\mathbf Q(i)/\mathbf Q}(\mathbf Q(i)^\times),
\]

即当且仅当 \(T_{K,g}\) 是两个有理平方之和。由于 \(T_{K,g}\) 是正整数，这又等价于：

\[
\boxed{
v_p(T_{K,g})\equiv0\pmod2
\quad
\forall p\equiv3\pmod4.
}
\tag{SOS}
\]

所以本轮的 Hilbert-symbol atlas 被统一成：

\[
\boxed{
H_{K,p}(g)=
\begin{cases}
-1,&p\equiv3\pmod4,\ v_p(T_{K,g})\text{ odd},\\
+1,&\text{otherwise},
\end{cases}}
\]

其中 \(p=2\) 单独满足 \(H_{K,2}(g)=+1\)。

正式新判决：

\[
\boxed{\texttt{BRAUER\_CLASS\_GAUSSIAN\_REDUCTION=YES}}
\]

\[
\boxed{\texttt{UNIFORM\_SPECIALIZED\_BRAUER\_NONTRIVIALITY=FALSE}}
\]

\[
\boxed{\texttt{FINITE\_LOCAL\_COVER\_EXTRACTED=NO}}
\]

\[
\boxed{\texttt{K100\_Q1\_NEGATIVE\_CLOSED=NO}}
\]

\[
\boxed{\texttt{K1000\_Q1\_NEGATIVE\_CLOSED=NO}}.
\]

注意：本轮**没有**证明存在一个 infinite locally-soluble arithmetic progression，因此不冒充

\[
\texttt{LOCAL\_COVER\_ARCHITECTURE\_INSUFFICIENT}
\]

这一更强 verdict。准确说法是：

> fixed-prime cover 作为 R5 当前实现没有提取出来；而且存在多个 live exact split fibres，故“每个 \(g\) 必有 local obstruction”已经严格死亡。下一轮必须攻击 split fibres 的 source provenance，而不是继续盲目加 prime。

---

# 2. Imported R4 Data

R4 的 q=1 negative shell：

\[
K\in\{10,100,1000\},
\]

\[
(d,\tau)\in
\{(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)\},
\]

并有 \(G=10^g\)、\(g-k\ge2\)。

R4 已证明 \(K=10\) 的 8 个 source cases 全闭，剩余：

\[
\boxed{K=100,1000}
\]

共 16 个 historical source cases。

---

# 3. Explicit \(A_2,T_4\)

统一：

\[
\begin{aligned}
A_2(G,K)=&
100(K^2-1)G^6+(280K^2-380)G^5\\
&+(236K^2-545)G^4+(16K^2-362)G^3\\
&-(52K^2+93)G^2-8K^2G+4K^2,
\end{aligned}
\]

\[
\boxed{
T_4(G,K)=
4(K^2-1)G^4+(8K^2-12)G^3
+(4K^2-13)G^2-6G+1.
}
\]

## \(K=100\)

\[
\boxed{
A_{100}(G)=
999900G^6+2799620G^5+2359455G^4+159638G^3
-520093G^2-80000G+40000
}
\]

\[
\boxed{
T_{100}(G)=
39996G^4+79988G^3+39987G^2-6G+1.
}
\]

## \(K=1000\)

\[
\boxed{
A_{1000}(G)=
99999900G^6+279999620G^5+235999455G^4+15999638G^3
-52000093G^2-8000000G+4000000
}
\]

\[
\boxed{
T_{1000}(G)=
3999996G^4+7999988G^3+3999987G^2-6G+1.
}
\]

Both \(A_2\) are irreducible squarefree sextics over \(\mathbf Q\); both \(T_4\) are irreducible squarefree quartics.

Special values:

\[
A_2(0,K)=4K^2,\quad A_2(1,K)=8(72K^2-185),\quad A_2(-1,K)=4,
\]

\[
T_4(0,K)=1,\quad T_4(1,K)=2(8K^2-17),\quad T_4(-1,K)=2.
\]

---

# 4. Resultant / Discriminant Ledger

General resultant:

\[
\boxed{
\operatorname{Res}_G(A_2,T_4)
=
1024(K-1)^2(K+1)^2
(32K^6+348K^4-1220K^2+727)^2.
}
\]

For \(K=100\):

\[
\operatorname{Res}(A,T)
=
2^{10}3^4 11^2 73^2 101^2 81401^2 5390999^2.
\]

\[
\operatorname{disc}(T)
=
2^{10}3^5\cdot139\cdot5741\cdot412667839.
\]

For \(K=1000\):

\[
\operatorname{Res}(A,T)
=
2^{10}3^6 7^2 11^2 13^2 37^2
103699^2 308588780979373^2.
\]

\[
\operatorname{disc}(T)
=
2^{10}3^5 17^2\cdot19\cdot43\cdot109
\cdot1279200175898383.
\]

The striking fact is that the resultant is itself a square. R5 does not use this as a heuristic only; the next section gives the exact algebraic reason why the Brauer class collapses.

---

# 5. Central New Identity: \(A+S^2=TQ\)

Define

\[
\boxed{
S=
1-(4K^2-3)G-(8K^2-10)G^2-(4K^2-4)G^3
}
\]

and

\[
\boxed{
Q=
(4K^2+21)G^2+(8K^2+12)G+(4K^2+1).
}
\]

Exact symbolic division gives

\[
\boxed{
A_2+S^2=T_4Q.
}
\tag{I1}
\]

Equivalently, on \(T_4=0\),

\[
\boxed{-A_2=S^2}.
\]

Thus at every finite divisor of \(T_4\), the residue of \((-A_2,T_4)\) is trivial.

---

# 6. Second Identity: \(Q\) is a square modulo \(A_2\)

Define

\[
R=\frac{N_R}{58},
\]

where

\[
\begin{aligned}
N_R={}&
2100(K^2-1)G^5+(4180K^2-6280)G^4\\
&+(1296K^2-6085)G^3-(1376K^2+1737)G^2\\
&+(-420K^2+348)G+(172K^2+58).
\end{aligned}
\]

Then

\[
\boxed{
R^2-Q=A_2H
}
\tag{I2}
\]

with

\[
\begin{aligned}
H=\frac1{3364}\bigl(&
44100(K^2-1)G^4+(52080K^2-96180)G^3\\
&-(20744K^2+44125)G^2+(-21328K^2+14268)G\\
&+7396K^2+1624
\bigr).
\end{aligned}
\]

Hence on \(A_2=0\),

\[
\boxed{Q=R^2}.
\]

Moreover

\[
\boxed{
\operatorname{Res}_G(A_2,Q)
=
4(1152K^6+14864K^4+2016K^2+5093)^2\ne0,
}
\]

so \(Q\) does not vanish on the \(A_2\)-divisor.

Combining with (I1):

\[
S^2=T_4Q=T_4R^2
\quad\text{mod }A_2.
\]

Therefore

\[
\boxed{
T_4=(S/R)^2
\quad\text{in }\mathbf Q[G]/(A_2).
}
\]

So the residue of \((-A_2,T_4)\) at every \(A_2\)-divisor is also trivial.

At infinity:

\[
v_\infty(A_2)=-6,\qquad v_\infty(T_4)=-4,
\]

both even; hence no infinity residue.

Thus

\[
(-A_2,T_4)
\]

is unramified on the \(G\)-line and therefore comes from a constant Brauer class over \(\mathbf Q\). Specializing at \(G=0\) gives

\[
(-A_2(0,K),T_4(0,K))
=
(-4K^2,1)=0.
\]

Hence

\[
\boxed{
(-A_2,T_4)=0.
}
\]

Since

\[
(-A_2,T_4)=(-1,T_4)+(A_2,T_4)
\]

in \(\operatorname{Br}(\mathbf Q(G))[2]\),

\[
\boxed{
(A_2,T_4)=(-1,T_4).
}
\tag{BR-GAUSS}
\]

This is R5's main theorem.

**Information class:** `BRAUER_GLOBAL`.

---

# 7. Consequence: Exact Specialized Solubility Criterion

For every \(K\in\{100,1000\}\) and every \(g\) with \(T_{K,g}\ne0\),

\[
\beta_{K,g}
=
(A_{K,g},T_{K,g})
=
(-1,T_{K,g}).
\]

Therefore:

\[
\boxed{
\beta_{K,g}=0
\iff
T_{K,g}\in N_{\mathbf Q(i)/\mathbf Q}(\mathbf Q(i)^\times).
}
\]

For positive integer \(T_{K,g}\), this is equivalent to the classical two-squares valuation condition:

\[
\boxed{
\beta_{K,g}=0
\iff
v_p(T_{K,g})\text{ is even for every }p\equiv3\pmod4.
}
\]

This immediately kills Conjecture C from the prompt:

\[
\boxed{
\texttt{GENERIC\_NONTRIVIAL}
\centernot\Rightarrow
\texttt{EVERY\_POWER\_TEN\_SPECIALIZATION\_NONTRIVIAL}.
}
\]

---

# 8. Complete Hilbert-Symbol Formula

For odd \(p\), write

\[
a=p^\alpha u,\qquad b=p^\beta v,
\]

with \(u,v\in\mathbf Z_p^\times\). Then

\[
(a,b)_p
=
(-1)^{\alpha\beta (p-1)/2}
\left(\frac up\right)^\beta
\left(\frac vp\right)^\alpha.
\]

For the present class, however, (BR-GAUSS) gives a much stronger simplification:

\[
\boxed{
H_{K,p}(g)=(-1,T_{K,g})_p.
}
\]

Thus for odd \(p\):

\[
\boxed{
H_{K,p}(g)=
\begin{cases}
(-1)^{v_p(T_{K,g})},&p\equiv3\pmod4,\\
+1,&p\equiv1\pmod4.
\end{cases}}
\]

No \(A\)-valuation bookkeeping is needed anymore.

---

# 9. \(p=2\) Audit

For every actual \(G=10^g\),

\[
T_{K,g}\equiv1\pmod8.
\]

Hence

\[
\boxed{
(-1,T_{K,g})_2=+1.
}
\]

Therefore

\[
\boxed{
H_{K,2}(g)=+1
\quad\forall g.
}
\]

The original \(A\)-data were also audited:

### \(K=100\)

For live \(g\ge4\),

\[
v_2(A_{100,g})=6.
\]

At \(g=4\),

\[
A/2^6\equiv5\pmod8;
\]

for \(g\ge5\),

\[
A/2^6\equiv1\pmod8.
\]

### \(K=1000\)

For live \(g\ge5\),

\[
v_2(A_{1000,g})=8.
\]

At \(g=5\),

\[
A/2^8\equiv5\pmod8;
\]

for \(g\ge6\),

\[
A/2^8\equiv1\pmod8.
\]

But after (BR-GAUSS), all these cases automatically yield symbol \(+1\).

---

# 10. \(p=5\) Audit

Again, because \(-1\in\mathbf Q_5^{\times2}\),

\[
\boxed{
H_{K,5}(g)=+1
\quad\forall g.
}
\]

Direct specialization gives:

### \(K=100\), live \(g\ge4\)

\[
v_5(A)=4,\qquad A/5^4\equiv14\pmod{25},
\]

\[
v_5(T)=0,\qquad T\equiv1\pmod{25}.
\]

### \(K=1000\), live \(g\ge5\)

\[
v_5(A)=6,\qquad A/5^6\equiv6\pmod{25},
\]

\[
v_5(T)=0,\qquad T\equiv1\pmod{25}.
\]

So \(p=5\) is permanently frozen as a non-killer.

---

# 11. \(p=3\) Audit

For \(K=100\),

\[
\boxed{
T_{100}(10^g)\equiv18\pmod{27}
}
\]

for every \(g\ge1\).

For \(K=1000\),

\[
\boxed{
T_{1000}(10^g)\equiv9\pmod{27}
}
\]

for every \(g\ge1\).

Therefore

\[
\boxed{
v_3(T_{K,g})=2.
}
\]

Since \(3\equiv3\pmod4\) but the valuation is even,

\[
\boxed{
H_{K,3}(g)=+1
}
\]

for both \(K=100,1000\).

This explains exactly why R4's \(K=10\) 3-adic killer cannot transfer.

---

# 12. Archimedean Audit

For \(G\ge10\) and \(K\ge100\),

\[
T_4(G,K)>0.
\]

Hence

\[
(-1,T_4)_\infty=+1,
\]

so

\[
\boxed{
H_{K,\infty}(g)=+1.
}
\]

---

# 13. Global Ramification Classification

R5 can now classify the entire ramification set without any resultant-exception bookkeeping:

\[
\boxed{
\operatorname{Ram}(\beta_{K,g})
=
\{\,p\equiv3\pmod4:
v_p(T_{K,g})\text{ odd}\,\}.
}
\]

There is no ramification at:

- \(p=2\);
- any \(p\equiv1\pmod4\);
- \(p=5\);
- \(p=3\) for \(K=100,1000\);
- infinity.

Hilbert reciprocity becomes exactly the familiar statement that the number of \(3\bmod4\) primes appearing to odd exponent is even.

So reciprocity does **not** add a new contradiction after the Gaussian reduction; it only constrains the ramification set parity already visible in the two-squares theorem.

**Verdict:** reciprocity is now a bookkeeping theorem, not an independent closure engine.

---

# 14. Structural Exponent Atlas

For any fixed odd prime \(p\equiv3\pmod4\), let

\[
m_p=\operatorname{ord}_p(10).
\]

Then \(p\mid T_K(10^g)\) only on the finite set of exponent residues

\[
g\bmod m_p
\]

for which

\[
T_K(10^g)\equiv0\pmod p.
\]

If the root in \(G\) is simple and \(v_p(10^{m_p}-1)=1\), each such exponent class admits a \(p\)-adic lifting description.

## \(K=100,\ p=23\)

\[
m_{23}=22,
\qquad
p\mid T \iff g\equiv8\pmod{22}.
\]

At \(g=8\),

\[
v_{23}(T)=1,
\quad
v_{23}(10^{22}-1)=1,
\quad
T'(10^8)\not\equiv0\pmod{23}.
\]

Write

\[
g=8+22n.
\]

There is a unique \(\gamma_{23}\in\mathbf Z_{23}\) with

\[
\gamma_{23}\equiv5\pmod{23}
\]

such that

\[
\boxed{
v_{23}(T_{100}(10^{8+22n}))
=
1+v_{23}(n-\gamma_{23}).
}
\]

Therefore the \(23\)-adic killer set is the union of alternating \(23\)-adic annuli:

\[
\boxed{
H_{100,23}(g)=-1
\iff
g=8+22n,\quad
v_{23}(n-\gamma_{23})\text{ even}.
}
\]

In particular the first-level class \(g\equiv8\pmod{22}\) is almost entirely killed, but the lifted subprogression \(n\equiv5\pmod{23}\) escapes at the next level.

## \(K=1000,\ p=19\)

\[
m_{19}=18,
\qquad
p\mid T\iff g\equiv10\pmod{18}.
\]

At the root,

\[
T'(10^{10})\equiv0\pmod{19},
\qquad
v_{19}(T(10^{10}))=1.
\]

Moreover the derivative vanishing implies that moving within the exponent class changes \(T\) only by \(19^2\)-multiples. Hence

\[
\boxed{
v_{19}(T_{1000}(10^g))=1
\iff
g\equiv10\pmod{18}.
}
\]

So this is a genuine pure periodic killer:

\[
\boxed{
\mathcal E^-_{1000,19}
=
\{g:g\equiv10\pmod{18}\}.
}
\]

## \(K=1000,\ p=43\)

Similarly,

\[
\boxed{
\mathcal E^-_{1000,43}
=
\{g:g\equiv12\pmod{21}\}.
}
\]

with exact valuation \(v_{43}(T)=1\) on the whole class.

Selected further first-level roots and lifts are stored in the computation certificate.

---

# 15. Prime Scan and Marginal-Value Guillotine

An exact scan was run over all primes

\[
p<20000,\qquad p\equiv3\pmod4
\]

and exponent windows:

### \(K=100\)

live window

\[
4\le g\le200.
\]

Result:

- 197 tested exponents;
- only 68 are killed by some fixed prime \(p<20000\);
- 129 survive every such tested fixed prime.

Coverage:

\[
\boxed{34.52\%}.
\]

### \(K=1000\)

live window

\[
5\le g\le200.
\]

Result:

- 196 tested exponents;
- 79 are killed by some fixed prime \(p<20000\);
- 117 survive.

Coverage:

\[
\boxed{40.31\%}.
\]

Dominant structural primes remain sparse:

- \(K=100\): \(23,47,59,107,\ldots\)
- \(K=1000\): \(19,43,59,83,163,\ldots\)

No small finite cover is remotely visible; adding primes produces strongly diminishing marginal returns.

This activates the **practical** Local-Cover Marginal-Value Guillotine:

\[
\boxed{
\text{stop blind fixed-prime accumulation}.
}
\]

But again, this is not a theorem that *no possible finite cover exists eventually*.

---

# 16. Exact Split Specializations

The Gaussian reduction allows a decisive counterexample to uniform specialized nontriviality.

## \(K=100,\ g=5\)

\[
T_{100}(10^5)
=
3^2\cdot444408887599985555488889,
\]

and the second factor is \(1\bmod4\). Hence every \(3\bmod4\) prime occurs to even exponent:

\[
\boxed{\beta_{100,5}=0}.
\]

Further exact split fibres:

\[
\boxed{
g=9,10,11,14
}
\]

with complete factorizations stored in `survivor_classes/exact_split_fibres.md`.

## \(K=1000,\ g=5\)

\[
T_{1000}(10^5)
=
3^2\cdot44445288891999985555488889,
\]

again giving

\[
\boxed{\beta_{1000,5}=0}.
\]

Further exact split fibres include

\[
\boxed{g=8,9}.
\]

Therefore:

\[
\boxed{
\texttt{UNIFORM\_SPECIALIZED\_BRAUER\_NONTRIVIALITY=FALSE}.
}
\]

These are not failures to find a prime. The quaternion class is actually zero.

---

# 17. Live \(g=5\) Source Replay

A split norm fibre does **not** imply a source solution.

For \(g=5\), all eight historical \((d,\tau)\) templates were replayed using the exact R4 total-space equation

\[
\mathcal Y^2=\mathcal F_{K,\tau}(G,n),
\]

the source interval

\[
0<\rho=r_{K,\tau}+2Kn<
\frac{10-d\tau}{10d}G,
\]

and the primitive condition

\[
\gcd(\rho,10\tau)=1.
\]

## \(K=100,g=5\)

All 8 templates have **zero square values** of \(\mathcal F\) in the legal source range.

## \(K=1000,g=5\)

Again all 8 templates have **zero square values**.

Thus:

\[
\boxed{
K=100,\ g=5,\ q=1\text{ negative source shell}
\Longrightarrow\varnothing,
}
\]

\[
\boxed{
K=1000,\ g=5,\ q=1\text{ negative source shell}
\Longrightarrow\varnothing.
}
\]

This is a finite endpoint certificate only; it does not close either \(K\)-family.

It is nevertheless strategically important because it proves:

> on split Brauer fibres, the missing rigidity lies in the **source embedding/provenance**, not in the generic norm conic.

---

# 18. Counterexample Guillotine

### Conjecture A — single killer prime for each \(K\)

**FALSE as a uniform strategy.**

There exist exact split fibres, so no prime kills those exponents at all.

### Conjecture B — fixed finite local cover

**NOT EXTRACTED.**

The first \(p<20000\) scan has large survivor density, but no proof of an infinite survivor progression is claimed.

### Conjecture C — generic Brauer nontriviality survives every \(10^g\)

\[
\boxed{\textbf{FALSE}.}
\]

Exact split fibres above are counterexamples.

### Conjecture D — moving primes are irrelevant

\[
\boxed{\textbf{FALSE}.}
\]

After (BR-GAUSS), moving \(3\bmod4\) prime divisors of \(T_{K,g}\) are the **entire** obstruction.

### Conjecture E — reciprocity automatically closes

\[
\boxed{\textbf{FALSE}.}
\]

It only forces even ramification cardinality.

### Conjecture F — \(p=2,5\) may be the hidden uniform killers

\[
\boxed{\textbf{FALSE for }K=100,1000.}
\]

Both symbols are identically \(+1\).

---

# 19. Information Gain Audit

| Result | Grade |
|---|---|
| exact \(A_2,T_4\) recovery | `STRUCTURAL` |
| \(A+S^2=TQ\) | `BRAUER_GLOBAL` |
| \(Q\equiv R^2\pmod A\) | `BRAUER_GLOBAL` |
| \((A,T)=(-1,T)\) | `BRAUER_GLOBAL` |
| complete local-symbol formula | `EXPONENT_CLASS` |
| \(p=2,3,5,\infty\) frozen split | `LOCAL_STRUCTURAL` |
| selected exact exponent classes | `EXPONENT_CLASS` |
| \(p<20000\) local-cover scan | `FILTER` |
| exact split fibres | `BRAUER_GLOBAL` / counterexample |
| \(g=5\) full source replay | `LOCAL_STRUCTURAL` endpoint closure |
| \(K=100\) family closure | NO |
| \(K=1000\) family closure | NO |
| q=1 closure | NO |

---

# 20. Remaining Exponent Responsibility

There is no honest finite number of globally unresolved exponents.

The exact decomposition is now:

\[
\boxed{
\mathcal O_K
=
\{g:
\exists p\equiv3\pmod4,\ v_p(T_{K,g})\text{ odd}\}
}
\]

(Brauer-obstructed exponents), and

\[
\boxed{
\mathcal S_K
=
\{g:
v_p(T_{K,g})\text{ even for all }p\equiv3\pmod4\}
}
\]

(split-Brauer exponents).

R5 completely understands the norm/Brauer layer:

- \(g\in\mathcal O_K\): the entire source fibre is dead immediately;
- \(g\in\mathcal S_K\): norm/Brauer contributes no obstruction, and source provenance must be attacked.

Within the finite scan against **fixed primes \(p<20000\)**:

\[
K=100:\quad129/197\text{ exponent values survive},
\]

\[
K=1000:\quad117/196\text{ exponent values survive}.
\]

These counts are scan statistics, not claims of actual local solubility.

---

# 21. First Five-Round Architecture Checkpoint

## 21.1 Permanent assets from R1–R5

1. finite valuation-signature branching from R1;
2. rigorous autopsy of factor-gap architecture from R2;
3. rigorous provenance failure of support collision from R3;
4. fixed function-field norm torsor from R4;
5. generic nontrivial Brauer class from R4;
6. permanent \(K=10\) q1-negative closure;
7. R5 exact Gaussian identification
   \[
   (A_2,T_4)=(-1,T_4);
   \]
8. complete ramification criterion by \(3\bmod4\) prime valuations of \(T_4\);
9. exact split-fibre counterexamples;
10. finite \(g=5\) source exclusion for both remaining \(K\).

## 21.2 Architectures permanently dead

- factor-gap allocation;
- support-collision via mismatched arithmetic provenance;
- fixed specialized Pell field / fixed fundamental unit;
- “generic Brauer nontriviality implies all specializations nontrivial”;
- “one magic fixed prime should kill each remaining \(K\)” as a global principle.

## 21.3 Tools that failed while objects remain valuable

The norm/Brauer object remains **high value**, but its role changed.

It is no longer a plausible standalone closure theorem for all \(g\), because split fibres exist.

It is now a perfect **front-end classifier**:

\[
g
\longmapsto
\begin{cases}
\text{dead by Gaussian ramification},\\
\text{split fibre requiring source replay}.
\end{cases}
\]

## 21.4 Exact remaining \(J=2\) responsibility

The full \(J=2\) problem remains open.

Inside q=1 negative:

\[
K=10\quad\text{closed},
\]

\[
K=100,1000\quad\text{open except certified finite endpoint exclusions}.
\]

The remaining hard core is the split-Brauer subfamily

\[
\boxed{
g\in\mathcal S_{100}\ \text{or}\ \mathcal S_{1000}
}
\]

together with its source embedding.

## 21.5 Is q=1 still worth continuing?

\[
\boxed{\textbf{YES, but not by more fixed-prime hunting}.}
\]

R5 has reduced q=1 to a qualitatively sharper dichotomy. The split fibres now expose exactly what information the conic forgets.

## 21.6 Should q>1 be raised in priority?

Not yet above q=1.

R5 produced a genuine new information class and a clear R6 target. The q=1 marginal value is still positive.

However q>1 should remain the parallel fallback if the split-fibre source attack fails in the next architecture checkpoint.

## 21.7 Marginal value of function-field norm/Brauer architecture

\[
\boxed{\textbf{HIGH AS CLASSIFIER; MEDIUM/LOW AS STANDALONE CLOSURE ENGINE}.}
\]

This is the precise checkpoint verdict.

---

# 22. R6 Strategic Decision

R6 should **not** be:

> scan more primes.

The correct next target is:

\[
\boxed{
\textbf{Gaussian split-fibre source replay}
}
\]

on

\[
T_{K,g}=a_g^2+b_g^2.
\]

Since

\[
(A,T)=(-1,T),
\]

a split fibre can be parameterized using a Gaussian norm representation of \(T\). R6 should ask whether the **particular source point**
coming from

\[
(2A_Kn+B_{K,\tau})^2-A_2(40K\mathcal Y)^2=S^2T
\]

can coexist with a Gaussian splitting of \(T\).

High-value subquestions:

1. lift a Gaussian factorization
   \[
   T=\pi\bar\pi
   \]
   back through the exact identity \(A+S^2=TQ\);
2. compare the resulting two norm structures
   \[
   \mathbf Q(\sqrt{A})
   \quad\text{and}\quad
   \mathbf Q(i);
   \]
3. exploit the source residue quotient \(n\), \(\rho\)-interval, and primitive gcd;
4. search for a fixed biquadratic / quaternionic composition law;
5. determine whether split fibres force an extra square, Gaussian divisibility, or short-interval incompatibility.

This is not a new generic surface classification. It attacks exactly the information lost when the Brauer class becomes zero.

---

# 23. Terminal Verdict

R5 answers the central strategic question from the prompt:

> Was R4's Brauer rigidity only an accidental \(K=10\) killer?

Answer:

\[
\boxed{\textbf{No.}}
\]

It contains a stronger uniform identity:

\[
\boxed{
(A_2,T_4)=(-1,T_4).
}
\]

But:

> Does that rigidity by itself systematically eliminate all \(K=100,1000\) fibres?

Answer:

\[
\boxed{\textbf{Also no.}}
\]

because exact split fibres exist.

So the correct end-state is:

\[
\boxed{
\text{R4/R5 norm-Brauer architecture}
=
\text{complete local/global classifier}
+
\text{partial extinction engine},
}
\]

not a complete q1 closure theorem.

The next mathematical object is the **source embedding inside the Gaussian-split fibres**.
