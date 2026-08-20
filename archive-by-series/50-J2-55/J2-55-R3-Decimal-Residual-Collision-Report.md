# J2-55-R3 — Decimal-Core Candidate Quantization × Exact-Residual Collision Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第三轮 / 统一终端线第十三轮  
**Frozen primary sources:** `J2-55-R2-USquare-Carry-Collision-Report.md`, `A1_J2_DCDC5_Report.md`, `A1_J2_GRFC9_Report.md`, `A1_J2_GRFC9_dependency.py`, `A1_J2_PRCC10_Report.md`  
**New symbolic audit:** `J2-55-R3-DecimalResidual-symbolic.py`  
**New exact replay/search:** `J2-55-R3-DecimalResidual-search.py`  
**New ledger:** `J2-55-R3-DecimalResidual-survivors.tsv`

---

# Part I — Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

No uniform proof of

\[
J=2\Longrightarrow\varnothing
\]

has been obtained, so **no** `J2-Resonance-Closure-Certificate.md` is issued.

This round nevertheless makes two global reductions that are strictly stronger than the R2 frontier.

First, after DCDC the exact quadratic really does normalize to

\[
\boxed{Q(x)=2K\,\mathscr R(x)},
\qquad
\boxed{\mathscr R(x)=AMx^2-uD_2x+\Omega=\Omega-x\lambda(x)},
\]

where throughout this report

\[
\boxed{M:=M_{10}:=\frac{L}{8}=\frac{10^\ell}{8}},
\qquad
\lambda(x):=uD_2-AMx.
\]

For every regular candidate which has passed the \(A^3\)-lift, U-SQ and decimal root residue,

\[
\boxed{A^3uM\mid\mathscr R(x)}.
\tag{DCQ-2}
\]

For a singular \(A^2\)-candidate the corresponding baseline is

\[
\boxed{A^2uM\mid\mathscr R(x)},
\tag{DCQ-S2}
\]

upgraded to \(A^3uM\) whenever the content-deflated next-\(A\)-digit also passes.

Second, and more importantly, the prospective failure chamber of the decimal carry width disappears completely.  For every **actual-root-eligible** live J2 state,

\[
\boxed{uM>C_\ell q},
\qquad
C_\ell=\frac{1299}{500}+10^{-\ell}<2.599.
\tag{UM-WIDTH}
\]

This is stronger than the requested “failure forces slope-1” alternative: **UM-width failure is impossible**.

Consequently the old regular split into “singleton” and “large-\(q\)” is no longer needed at the final decimal stage.  In the regular branch, \(A^3\)-synchronization plus the decimal class gives a single CRT residue modulo \(A^3M\), while the entire legal root interval has width less than \(A^2C_\ell q\).  Since \(AM>C_\ell q\), there is at most one actual candidate:

\[
\boxed{
\textbf{regular J2 frontier}
=
\textbf{one }(A^3,M)\textbf{-CRT candidate }x_*
+\textbf{one U-test}
+\textbf{one residual quantum}.
}
\tag{REG-FRONT}
\]

The singular branch is also reduced, though not closed:

\[
\boxed{
\textbf{one U-root cell}+j
\Longrightarrow
\textbf{at most one decimal/U-compatible content }m
\Longrightarrow
\textbf{deflated }A^3\textbf{ test}
+\textbf{one residual quantum}.
}
\tag{SING-FRONT}
\]

So the R2 obstruction is **not** left unchanged.

---

# Part II — Frozen R2 theorem ledger and sign correction

The live chamber remains

\[
J=2,\quad S_R<0,\quad \ell\ge6,\quad g\ge4,\quad u>1,
\]

with

\[
G=10^g,\quad H=G/2,\quad K=10^k,\quad L=10^\ell,\quad k=2g-\ell,
\]

\[
uq=G+1,\qquad A=2u+1.
\]

The following R2 results are frozen and not reproved here:

1. \(\gcd(Z,u)=1\) for every admissible primitive-recovered root state.
2. Primitive \(A\)-root:
   \[
   Kx\equiv-Z\pmod A,
   \qquad x\equiv r_A\pmod A.
   \]
3. Complete \(A^2\)-lift classification with \(d_A=\gcd(A,D_2)\).
4. Carry representation
   \[
   x=r_{A^2}+A^2j,
   \qquad0\le j<C_\ell q.
   \]
5. Exact root interval
   \[
   I_x=\left(\frac{AG}{10},\frac{8uD_2}{AL}\right).
   \]
6. Singular content bridge
   \[
   r_m=r_0+m\frac{A^2}{d},\qquad
   r_m\equiv r_0+m\frac Ad\pmod u.
   \]
7. U-SQ is \(Q(x)=0\pmod u\), **not** an independent second root polynomial.

There is one mandatory sign correction to the prompt.  In the regular branch the third \(A\)-digit is

\[
\boxed{
 c_3\equiv-
 \frac{Q(r_{A^2})}{A^2}
 Q'(r_{A^2})^{-1}
 \pmod A,
}
\tag{C3-SIGN}
\]

not the positive-sign version appearing in two displays of the campaign prompt.  This is the sign already frozen by PRCC10/R2.

---

# Part III — DCDC / RQDC dependency audit

The logical direction is kept one-way:

\[
\boxed{
\text{actual integral root}
\Longrightarrow
2K\mid\widetilde F
\Longrightarrow
\Omega:=\frac{\widetilde F}{2K}\in\mathbb Z.
}
\]

Likewise the decimal root relation

\[
M\mid uD_2x-\Omega
\tag{RQDC}
\]

is a **root-necessary sieve**.  Neither DCDC nor RQDC is used to infer the existence of a root.

Because \(\gcd(uD_2,10)=1\) and \(M\) is a pure \(2,5\)-integer,

\[
\boxed{
 x\equiv x_{10}:=(uD_2)^{-1}\Omega\pmod M.
}
\tag{DCQ-1}
\]

Also

\[
\gcd(A,u)=\gcd(A,M)=\gcd(u,M)=1.
\]

Thus the decimal modulus is genuinely coprime to the already-frozen \(A\)-adic and \(u\)-adic resolutions, even though all three are still necessary readings of the same exact root relation.

---

# Part IV — Normalized exact residual

Since

\[
H^2=\frac{G^2}{4}=\frac{KL}{4}
\]

and \(\widetilde F=2K\Omega\),

\[
\begin{aligned}
Q(x)
&=AH^2x^2-2uKD_2x+\widetilde F\\
&=2K\left(\frac{AL}{8}x^2-uD_2x+\Omega\right).
\end{aligned}
\]

With \(M=L/8\), this gives the exact identity

\[
\boxed{Q(x)=2K\mathscr R(x)},
\qquad
\boxed{\mathscr R(x)=AMx^2-uD_2x+\Omega}.
\tag{EXR-1}
\]

No new root quotient has been introduced.

The symbolic file verifies this identity exactly.

---

# Part V — Complementary-factor Euclidean form

Define

\[
\boxed{\lambda(x)=uD_2-AMx}.
\]

Then

\[
\boxed{\mathscr R(x)=\Omega-x\lambda(x)}.
\tag{EUCLID}
\]

Thus an actual root is equivalent to

\[
\boxed{\Omega=x\lambda(x)}.
\tag{FACT}
\]

and hence requires

\[
\boxed{x\mid\Omega}.
\]

One useful redundancy is now explicit.  If a candidate has already passed the exact root interval,

\[
x<\frac{8uD_2}{AL}=\frac{uD_2}{AM},
\]

then automatically

\[
\boxed{\lambda(x)>0}.
\]

Therefore `LAMBDA_POSITIVITY_FAIL` is an audit field, not an independent death gate after exact interval intersection.

Also, because \(\ell\ge6\), \(10\mid M\), so every integral candidate has

\[
\lambda(x)\equiv uD_2\pmod{10},
\]

hence \(\lambda(x)\) is automatically a ten-unit whenever the frozen ten-unit hypotheses on \(u,D_2\) hold.

---

# Part VI — Triple-modulus residual quantization

Assume a regular candidate has passed:

1. \(A^3\mid Q(x)\);
2. U-SQ, so \(u\mid Q(x)\);
3. DCDC, so \(\mathscr R\in\mathbb Z\);
4. RQDC, so \(M\mid uD_2x-\Omega\).

Because

\[
\mathscr R(x)=AMx^2-(uD_2x-\Omega),
\]

RQDC implies

\[
M\mid\mathscr R(x).
\]

Moreover \(\gcd(AuM,2K)=1\), so from \(Q=2K\mathscr R\),

\[
A^3\mid\mathscr R,
\qquad
u\mid\mathscr R.
\]

Pairwise coprimality gives

\[
\boxed{A^3uM\mid\mathscr R(x)}.
\tag{TRIPLE-Q}
\]

Hence

\[
\boxed{
\mathscr R(x)=0
\quad\text{or}\quad
|\mathscr R(x)|\ge A^3uM.
}
\tag{TRIPLE-GAP}
\]

For a singular candidate known only modulo \(A^2\), exactly the same argument gives

\[
\boxed{A^2uM\mid\mathscr R(x)}.
\tag{SING-Q}
\]

If its content-deflated next \(A\)-digit succeeds, \(A^3\mid Q(x)\) and the divisor upgrades again to \(A^3uM\).

This establishes the requested Success-A theorem in corrected normalized form.

---

# Part VII — Global UM-width theorem

We now prove the strongest new theorem of the round.

## Theorem UM-WIDTH

For every actual-root-eligible live J2 state,

\[
\boxed{uM>C_\ell q}.
\]

### Step 1 — suppose failure

Assume

\[
uM\le C_\ell q.
\]

Since \(M=L/8\) and \(uq=G+1\),

\[
\frac{uL}{8}\le C_\ell q
\]

gives

\[
\boxed{
q^2\ge\frac{(G+1)L}{8C_\ell}.
}
\tag{UM-LB}
\]

For \(q=1\), \(u=G+1\) and \(M\ge125000\), so the failure inequality is immediately impossible.  Hence only \(q>1\) needs the inherited DCDC outer theorem.

### Step 2 — combine with OUTER

The frozen DCDC5 outer inequality is

\[
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3.
\]

Using (UM-LB),

\[
G^2<292C_\ell\left(1+\frac1G\right)L^2.
\]

For \(\ell\ge6\),

\[
C_\ell\le2.598001,
\]

and for \(g\ge4\),

\[
292C_\ell\left(1+\frac1G\right)<759<100^2.
\]

Thus

\[
\frac GL<100.
\]

Since \(G/L=10^{g-\ell}\),

\[
\boxed{g-\ell\le1}.
\tag{SLOPE-1}
\]

This is already the requested slope-1 collapse.

### Step 3 — eliminate \(h=g-\ell\le-1\)

The failure inequality itself may be rewritten

\[
\boxed{
u^2\le8C_\ell10^{g-\ell}\left(1+\frac1G\right)}.
\tag{U2}
\]

If \(h\le-1\), the right-hand side is below \(2.079\), contradicting \(u>1\).

### Step 4 — eliminate \(h=0\)

If \(h=0\), (U2) gives

\[
u^2<21.
\]

Since \(u>1\) and \(\gcd(u,10)=1\), this forces \(u=3\).  But

\[
10^g+1\equiv2\pmod3,
\]

so \(u\nmid G+1\), contradiction.

### Step 5 — eliminate \(h=1\)

Now \(\ell=g-1\ge6\), so \(g\ge7\).  From (U2),

\[
u^2<208,
\]

hence \(u\le14\).  Combining \(u\mid G+1\), \(\gcd(u,10)=1\), and \(\gcd(A,10)=1\) leaves only

\[
\boxed{u\in\{11,13\}}.
\]

Thus \(A\le27\) and

\[
q=\frac{G+1}{u}>\frac G{13}>7\times10^5.
\]

For \(h=1\), \(K=10G\).  The frozen signed-index strip gives

\[
-\left(\frac{2\eta}{K}+\frac{2A}{G}\right)<N<\frac{2\eta G^2}{K}
=\frac{\eta G}{5},
\]

so for \(G\ge10^7\),

\[
N\ge0,
\qquad
N<\frac{1299}{2500}G.
\]

Using DIG3 \(a_3<G\) in RCE2,

\[
(G-1)t=2(q+4)a_3+qN,
\]

gives, by an exact rational comparison recorded in the symbolic certificate,

\[
\boxed{t<3q}.
\]

RCE3 now yields

\[
q(q+4)Z=At-2N.
\]

Since \(Z\ge1\) and \(N\ge0\),

\[
q(q+4)\le At<3Aq,
\]

so

\[
q+4<3A\le81,
\]

hence \(q<77\), contradicting \(q>7\times10^5\).

All possible values of \(h\le1\) have been eliminated.  Therefore the assumed failure is impossible, proving

\[
\boxed{uM>C_\ell q}.
\]

---

# Part VIII — Regular branch: A³ + decimal gives one candidate globally

This is the main dimensional consequence of UM-WIDTH.

In the regular branch \(d_A=1\), the \(A^3\)-lift fixes one residue

\[
x\equiv r_{A^3}\pmod{A^3}.
\]

RQDC fixes

\[
x\equiv x_{10}\pmod M.
\]

Since \(\gcd(A^3,M)=1\), there is one CRT residue modulo \(A^3M\).

Meanwhile every actual root is of the form

\[
x=r_{A^2}+A^2j,
\qquad0\le j<C_\ell q,
\]

so the entire legal root interval has \(x\)-width less than

\[
A^2C_\ell q.
\]

From UM-WIDTH and \(A>u\),

\[
AM>C_\ell q,
\]

hence

\[
A^3M>A^2C_\ell q.
\]

Therefore:

\[
\boxed{
\#\left\{
 x\in I_x:
 x\equiv r_{A^3}\pmod{A^3},
 x\equiv x_{10}\pmod M
\right\}
\le1.
}
\tag{REG-ONE}
\]

This theorem **unifies** the old R2 regular singleton and regular large-\(q\) frontiers at the decimal stage.

The unique CRT representative, if it falls in \(I_x\), is denoted \(x_*\).  It then receives only three terminal checks:

\[
\boxed{x_*^2\equiv Z^2\pmod u},
\]

\[
\boxed{x_*\mid\Omega\quad\text{and}\quad\Omega/x_*=\lambda(x_*)},
\]

or equivalently

\[
\boxed{\mathscr R(x_*)=0}.
\]

If U-SQ passes and \(\mathscr R(x_*)\ne0\), then

\[
\boxed{
\varepsilon_*:=\frac{\mathscr R(x_*)}{A^3uM}\in\mathbb Z\setminus\{0\}.
}
\]

No magnitude theorem proving \(|\varepsilon_*|<1\) was obtained.

---

# Part IX — Regular singleton exact interval attack

The R2 historical diagnostic remains unchanged:

- all 50 regular \(A^2\)-fibres satisfy the old singleton condition \(A>C_\ell q\);
- one has empty exact carry interval;
- the remaining 49 have their corrected \(c_3\) outside the exact interval.

Thus Conjecture D1 continues to have 50/50 finite support.

However no uniform proof of

\[
d_A=1,\quad A>C_\ell q
\Longrightarrow
c_3\notin I_j
\]

was found.  This round therefore does **not** promote the historical 50/50 pattern to a theorem.

The strategic importance of D1 is reduced by (REG-ONE): even if a future regular singleton candidate lies inside the interval, decimal synchronization still leaves at most one candidate globally.

---

# Part X — Regular large-q: n-decimal collapse

Retain the R2 parametrization

\[
j=c_3+An,
\qquad
0\le n<\frac{C_\ell q-c_3}{A}.
\]

The decimal class gives

\[
\boxed{
 n\equiv n_{10}:=
 (x_{10}-r_{A^2}-A^2c_3)(A^3)^{-1}
 \pmod M.
}
\tag{N-DEC}
\]

UM-WIDTH implies

\[
M>\frac{C_\ell q}{u}>\frac{C_\ell q}{A}
>\frac{C_\ell q-c_3}{A}.
\]

Therefore the entire legal \(n\)-interval contains **at most one** decimal residue:

\[
\boxed{\#n\le1.}
\tag{N-ONE}
\]

This is stronger than merely obtaining one \(n\)-class modulo \(uM\).  U-SQ is now a direct yes/no test on that single \(n\); there is no need to enumerate unitary U-root cells in the regular large-\(q\) branch.

The old R2 bound

\[
2g\le3\ell+1
\]

remains true but is no longer the main terminal compression.

---

# Part XI — Singular decimal content selection

Let

\[
d=d_A>1,\qquad e=A/d,
\]

and

\[
x=r_0+m\frac{A^2}{d}+A^2j,
\qquad0\le m<d.
\]

For fixed \(j\), the decimal root class gives

\[
\boxed{
 m\equiv
 m_{10}(j):=
 (x_{10}-r_0-A^2j)
 \left(\frac{A^2}{d}\right)^{-1}
 \pmod M.
}
\tag{M-DEC}
\]

For a fixed U-root cell \(\rho\equiv\eta Z\pmod u\), R2 gives

\[
\boxed{
 m\equiv d(\rho-r_0-j)\pmod u.
}
\tag{M-U}
\]

Since \(\gcd(u,M)=1\), these combine to one class modulo \(uM\):

\[
\boxed{m\equiv m_{\eta,j}\pmod{uM}.}
\tag{M-CRT}
\]

But

\[
0\le m<d\le A=2u+1
\]

and, because \(M\ge125000\),

\[
uM>A\ge d.
\]

Hence:

\[
\boxed{
\text{for every fixed }(\eta,j),
\text{ there is at most one legal content index }m.
}
\tag{DCQ-4}
\]

This includes the maximal-content case \(d=A\).  Thus the old R2 multiplicity bound “\(\le3\)” is globally sharpened to “\(\le1\)” once the decimal class is imposed.

This is a selection theorem, not a singular extinction theorem.

---

# Part XII — Singular content-deflated next-A-digit

For a singular \(A^2\)-class \(r_m\), put

\[
T_{2,m}:=\frac{Q(r_m)}{A^2}.
\]

Because

\[
\gcd(Q'(r_m),A)=d,
\]

an actual root must first satisfy

\[
\boxed{d\mid T_{2,m}}.
\]

If so, division by \(d\) yields the exact deflated congruence modulo

\[
e=A/d:
\]

\[
\boxed{
 j\equiv c_m^\sharp
 :=-
 \frac{T_{2,m}}{d}
 \left(\frac{Q'(r_m)}{d}\right)^{-1}
 \pmod e.
}
\tag{S-A3}
\]

This is not a new Hensel campaign; it is the one next digit needed after content selection.

If a selected \((\eta,j,m)\) passes (S-A3), then \(A^3\mid Q(x)\), and its normalized residual quantum upgrades from

\[
A^2uM
\]

to

\[
\boxed{A^3uM}.
\]

---

# Part XIII — Maximal content d=A audit

The branch

\[
d=A\iff A\mid D_2
\]

is **not** silently discarded.

Writing \(D_2=A D_2^\sharp\), one has

\[
\widetilde F
=A\left(\mathcal X^2+Z D_2^\sharp\right).
\]

Since \(\gcd(A,2K)=1\), DCDC implies

\[
2K\mid \mathcal X^2+Z D_2^\sharp.
\]

This is compatible with the primitive \(A\)-root and does not produce a contradiction by itself.  Also the prime supports of \(A\) and \(u\) remain disjoint, so there is no hidden same-prime U/content valuation collision.

What R3 does prove is:

- decimal + U selects at most one \(m\) for each \((\eta,j)\), even when \(d=A\);
- here \(e=A/d=1\), so the deflated next-digit congruence gives no extra modulus.

Therefore

\[
\boxed{d=A\text{ remains OPEN as an explicit structured exception}.}
\]

Conjecture D6 is not proved.

---

# Part XIV — Residual sign / Euclidean remainder attempts

Several exact identities were tested:

\[
\mathscr R'(x)=2AMx-uD_2=AMx-\lambda(x),
\]

\[
\mathscr R(x)=\Omega-x\lambda(x).
\]

The exact interval supplies \(\lambda(x)>0\), but it does not fix the sign of

\[
AMx-\lambda(x).
\]

No uniform theorem of the form

\[
0<|\mathscr R(x_*)|<A^3uM
\]

or

\[
0<|\mathscr R(x_*)|<x_*
\]

was obtained.

Likewise no uniform proof of

\[
\boxed{x_*\nmid\Omega}
\]

was found.  Consequently Conjectures D2 and D7 remain open.

The important negative conclusion is precise: the modular synchronization is now strong enough to make \(x_*\) unique in the regular branch, but **quantization alone does not prove nonzero residual**.  The missing theorem is genuinely an exact factor/remainder theorem, not another congruence.

---

# Part XV — First nonzero quotient digit audit

For a regular triple-gate candidate define only after divisibility is proved

\[
\varepsilon_x:=\frac{\mathscr R(x)}{A^3uM}\in\mathbb Z.
\]

The symbolic audit verifies the divisor, but no universally forced value of

\[
\varepsilon_x\pmod2,
\quad
\varepsilon_x\pmod5,
\quad
\varepsilon_x\pmod A,
\quad
\varepsilon_x\pmod u
\]

was derived without re-importing the same root equation in disguised form.

Therefore no generic 2/5-adic campaign is reopened.

---

# Part XVI — Exact computation

`J2-55-R3-DecimalResidual-search.py` exactly reconstructs the inherited h=0 corpus rather than hard-coding the 79 states.  It reproduces the frozen upstream counts:

```text
q=7 : tail_integral=221288, reconstructed=2900, linear_legal=370, DCDC=28
q=11: tail_integral=8713715, reconstructed=264156, linear_legal=10214, DCDC=44
q=17: tail_integral=413750, reconstructed=1164, linear_legal=32, DCDC=5
q=19: tail_integral=437896, reconstructed=969, linear_legal=21, DCDC=2
```

Thus the historical DCDC root-layer input is again exactly 79 states.

The R3 gate replay gives:

```text
INPUT_STATES=79
PRIMITIVE_GCD_FAIL_STATES=4
PRIMITIVE_GCD_PASS_STATES=75
A2_FAIL_STATES=19
A2_PASS_STATES=56
ROOT_FIBRES=68
REGULAR_FIBRES=50
A3_INTERVAL_FAIL_FIBRES=50
SINGULAR_STATES=6
SINGULAR_FIBRES=18
SINGULAR_LEGAL_CARRIES=333
DECIMAL_ROOT_FAIL_SINGULAR_FIBRES=18
DECIMAL_ROOT_PASS_SINGULAR_CARRIES=0
FULL_ROOT_SURVIVE_FIBRES=0
```

Thus, in the requested gate order:

- all 50 historical regular fibres die before decimal, at the exact A³/interval gate;
- all 18 singular fibres, containing 333 legal carries in total, die at the **new decimal root gate before U-SQ**.

The six singular states are again

\[
\boxed{g\in\{259,359,435,481,669,1025\},\qquad q=11,\qquad d=3.}
\]

An independent deflated-A³ replay on the same 18 singular fibres gives

```text
12 fibres: d does not divide T_{2,m}
 6 fibres: c_m^sharp exists but lies outside the exact carry interval
 0 fibres: deflated A^3 pass
```

So the historical singular corpus now has **two** later exact explanations of death: decimal incompatibility in the requested order, and content-deflated A³ incompatibility in an independent diagnostic.  Neither is promoted to a global singular theorem.

---

# Part XVII — Targeted regular large-q search

The R2 outer census for \(6\le g\le12\) is reproduced exactly:

\[
\boxed{28\text{ outer pairs satisfy }A\le C_\ell q.}
\]

These are outer structural pairs, not root states.

A targeted exact h=0 RCE/tail scan was run on the smallest such pair

\[
(g,u,q,A)=(6,101,9901,203).
\]

It processed

```text
26,705,427 tail-integral alpha/t instances,
2 reconstructed RCE states,
0 linear-legal states,
0 DCDC states.
```

Hence this pair never reaches the root layer.

No structural \(A^3+\)decimal\(+\)U triple-gate pseudo-survivor was produced in the historical corpus or this targeted outer probe.  Therefore Conjecture D2 is **not falsified**, but neither is it empirically tested on a genuine triple-gate survivor.

This absence is not promoted to a theorem.

---

# Part XVIII — Counterexample / conjecture ledger

### D1 — regular singleton interval extinction

**OPEN uniformly.** Historical support remains 50/50 fibres dead at the A³/interval gate.

### D2 — triple-modulus singleton extinction by \(0<|\mathscr R|<A^3uM\)

**OPEN.** Triple quantization is proved; the required nonzero/magnitude squeeze is not.

### D3 — decimal/U carry uniqueness via \(uM>C_\ell q\)

\[
\boxed{\textbf{PROVED globally as a root-necessary theorem}.}
\]

Indeed UM-width failure is impossible.

### D4 — UM-width failure forces slope-1

**SUPERSEDED by stronger theorem.**  Failure first implies \(g\le\ell+1\), then every remaining \(h\le1\) layer is eliminated, so the failure chamber is empty.

### D5 — proper singular U/decimal content extinction

**OPEN uniformly.**  What is proved is uniqueness/absence of \(m\) for fixed \((\eta,j)\).  Historical 18 fibres all have absence already at the decimal gate.

### D6 — maximal content impossible

**OPEN.**  The branch is explicitly audited; decimal reduces multiplicity but no contradiction is proved.

### D7 — candidate factor mismatch \(x\nmid\Omega\)

**OPEN.**  It is now a sharply posed one-candidate test in the regular branch, but no uniform divisibility exclusion was derived.

### Fake common-root collision

**PERMANENTLY RETIRED.**  No resultant between equivalent forms of \(Q\) is used anywhere in R3.

---

# Part XIX — Survivor classification / precise next frontier

The R2 frontier has changed materially.

## Regular branch — unified

For every regular profile that is actual-root eligible:

1. compute the unique \(A^3\) class;
2. combine it with \(x\equiv x_{10}\pmod M\);
3. by (REG-ONE), there is at most one \(x_*\in I_x\);
4. test
   \[
   x_*^2\equiv Z^2\pmod u;
   \]
5. if it passes, then
   \[
   \mathscr R(x_*)=A^3uM\,\varepsilon_*,
   \qquad\varepsilon_*\in\mathbb Z;
   \]
6. exact root iff
   \[
   \varepsilon_*=0
   \iff
   \Omega=x_*\lambda(x_*).
   \]

Thus

\[
\boxed{
\textbf{REGULAR FRONTIER}
=
\textbf{one CRT candidate}
+\textbf{one U-square test}
+\textbf{one normalized residual quantum}.
}
\]

There is no longer a terminal need to distinguish R-S from R-L.

## Singular branch

For each U-root cell and legal carry \(j\):

1. decimal + U determines at most one
   \[
   m_{\eta,j}\in[0,d);
   \]
2. that content must pass
   \[
   d\mid T_{2,m}
   \]
   and
   \[
   j\equiv c_m^\sharp\pmod{A/d};
   \]
3. then
   \[
   \mathscr R=A^3uM\,\varepsilon
   \]
   after the deflated A³ pass;
4. exact root iff \(\varepsilon=0\).

Thus

\[
\boxed{
\textbf{SINGULAR FRONTIER}
=
\textbf{one U-cell}+j
+\textbf{unique/absent CRT content}
+\textbf{deflated A-digit}
+\textbf{one residual quantum}.
}
\]

This is strictly smaller than R2's “\(\le3m\)” frontier, but singular \(j\) has not yet been removed globally.

---

# Part XX — J2 closure audit

### Frozen closed and not reopened

\[
S_R>0,
\qquad
k=2g+1,
\qquad
k=2g,
\qquad
\ell=1,2,3,4,5,
\qquad
u=1,
\qquad
g=2,3.
\]

### New proved package

```text
DCQ-1   Decimal Root Class: PROVED as root-necessary sieve
EXR-1   Normalized Residual Q=2K*R: PROVED
EXR-E   Euclidean form R=Omega-x*lambda(x): PROVED
DCQ-2   Regular A^3*u*M residual quantization: PROVED
DCQ-S2  Singular A^2*u*M residual quantization: PROVED
UM-1    Global root-necessary u*M > C_ell*q: PROVED
REG-1   Regular A^3 + decimal interval contains at most one candidate: PROVED
N-1     Regular large-q decimal n-class has at most one legal n: PROVED
DCQ-4   Fixed-(eta,j) singular content multiplicity <=1 after decimal+U: PROVED
SA3-1   Singular content-deflated next-A-digit modulo A/d: PROVED
FULL-J2 Extinction: NOT PROVED
```

### Success assessment

- **Success A:** achieved.
- **Success B:** not achieved; no infinite regular or singular branch is proved empty.
- **Success C:** not achieved.
- **Success D-type compression:** exceeded on the UM-failure side; the failure chamber is empty, and regular large-\(q\) is reduced directly to one decimal candidate.
- **Success E:** not achieved.

Therefore

\[
\boxed{\textbf{J2 OPEN}}.
\]

No closure certificate is generated.

The exact next mathematical target is no longer “another modulus.”  It is:

\[
\boxed{
\textbf{Regular: prove the unique CRT candidate cannot satisfy }
\Omega=x_*\lambda(x_*),
}
\]

and, independently,

\[
\boxed{
\textbf{Singular: eliminate the remaining }(\eta,j)\textbf{ line after unique content selection.}
}
\]

---

# File audit

Generated in this round:

```text
J2-55-R3-Decimal-Residual-Collision-Report.md
J2-55-R3-DecimalResidual-symbolic.py
J2-55-R3-DecimalResidual-search.py
J2-55-R3-DecimalResidual-certificate.txt
J2-55-R3-DecimalResidual-survivors.tsv
```

Not generated:

```text
J2-Resonance-Closure-Certificate.md
```

because J2 remains open.
