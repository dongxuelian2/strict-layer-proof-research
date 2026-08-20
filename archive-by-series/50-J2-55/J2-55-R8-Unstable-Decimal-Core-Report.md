# J2-55-R8 — Unstable Carry-Residual × Actual-Digit Decimal-Core Globalization Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\) only  
**Campaign:** 55 第八轮 / 统一终端线第十八轮  
**Primary frozen source:** `J2-55-R7-CarryIndex-QDescent-Report.md`

---

# 1. Executive Status

\[
\boxed{\textbf{J2 OPEN}}
\]

\[
\boxed{\delta>0:\ \textbf{OPEN globally}\quad(q=1\text{ high inherited CLOSED})}
\]

\[
\boxed{\delta=0,\ q>1:\ \textbf{OPEN globally}}
\]

\[
\boxed{\delta=0,\ q=1:\ \textbf{CLOSED in R8}}
\]

\[
\boxed{\delta<0,\ q>1:\ \textbf{OPEN at normalized }K\textbf{-core + explicit low-}k\textbf{ types}}
\]

\[
\boxed{\delta<0,\ q=1:\ \textbf{OPEN at }k\in\{1,2,3\}}
\]

No `J2-Resonance-Closure-Certificate.md` is issued.

The main R8 gains are:

1. the undescended tail factorization collapses to an actual-digit identity (DTF1);
2. both the unstable carry residual and the actual-digit tail acquire exact all-exponent decimal cores;
3. the boundary/high/reverse \(\alpha\)-dependence is eliminated in favor of \(\omega\);
4. the moderate-\(b\) digit tail has a finite-height normalized index \(\lambda\);
5. the whole historical 79-state boundary corpus is killed by the **unstable carry decimal core**, without setting \(\Gamma_B=0\);
6. the critical \(q=11,g=471\) high state is killed at the same new gate;
7. the entire \(q=1\) boundary is closed by an absolute multiplier reduction to 17 periodic cells followed by periodic discriminant non-square certificates;
8. active reverse \(k=1,b=0\) types now satisfy \(5\mid t\), and \((k,q)=(2,7)\) satisfies \(25\mid t\).

---

# 2. R7 dependency correction frozen

R8 never assumes

\[
\Gamma_B=\Gamma_H=\Gamma_R=0
\]

as all-exponent root necessities.  Those equalities remain stabilized fixed-fibre consequences only.

The exact global interfaces are retained as

\[
G\mid 2d_0q^2t(q+4)\Gamma_{B/H},
\]

and

\[
K\mid 2d_0q^2t(q+4)\Gamma_R,
\]

with

\[
d_0=2\cdot5^b,\qquad b=v_5(q+4).
\]

The R7 full-root mod-\(q\) degeneracy is also frozen: no new positive opening is inferred from the raw root equation modulo \(q\).

---

# 3. DTF1 derivation — PROVED

Freeze

\[
c=q^3+10q^2+12q+8.
\]

R7 gives

\[
q^2Z=4a_3+t
\]

and

\[
(q+4)\bigl(q^2cZ-t(q+2)^3\bigr)
=2\frac{G}{d_\delta}(d_\delta ct-\alpha).
\]

Now

\[
c-(q+2)^3=4q^2,
\]

hence

\[
q^2cZ-t(q+2)^3
=4(ca_3+q^2t).
\]

Therefore

\[
\boxed{
G(d_\delta ct-\alpha)
=2d_\delta(q+4)(ca_3+q^2t).
}
\tag{DTF1}
\]

This is symbolically certified in `J2-55-R8-DecimalCore-symbolic.py`.

Define only as the existing tail mismatch

\[
\boxed{\omega:=d_\delta ct-\alpha.}
\]

Since \(a_3,t,c,q+4>0\), DTF1 gives

\[
\boxed{\omega>0},\qquad
\boxed{\alpha<d_\delta ct}.
\]

---

# 4. \(t\)-odd theorem — PROVED

From

\[
t=q^2Z-4a_3
\]

and the fact that \(q,Z,a_3\) are odd ten-units,

\[
\boxed{t\equiv1\pmod2},\qquad
\boxed{v_2(t)=0}.
\]

---

# 5. Carry-Residual Decimal-Core Theorem — PROVED

For high/boundary,

\[
G=2^g5^g\mid2d_0q^2t(q+4)\Gamma_{B/H}.
\]

Because

\[
v_2\bigl(2d_0q^2t(q+4)\bigr)=2,
\]

and

\[
v_5\bigl(2d_0q^2t(q+4)\bigr)=2b+v_5(t),
\]

we obtain

\[
\boxed{2^{g-2}\mid\Gamma_{B/H}},
\tag{CR-2}
\]

\[
\boxed{
5^{\max(g-2b-v_5(t),0)}\mid\Gamma_{B/H}.
}
\tag{CR-5}
\]

For reverse,

\[
\boxed{2^{\max(k-2,0)}\mid\Gamma_R},
\]

\[
\boxed{
5^{\max(k-2b-v_5(t),0)}\mid\Gamma_R.
}
\]

These are all-exponent root necessities and do not use stabilized carry equality.

---

# 6. Actual-Digit Tail Decimal-Core Theorem — PROVED

For high/boundary, DTF1 with \(d_\delta=d_0\) gives

\[
\boxed{2^{g-2}\mid ca_3+q^2t},
\tag{DT-2}
\]

\[
\boxed{
5^{\max(g-2b,0)}\mid ca_3+q^2t.
}
\tag{DT-5}
\]

For reverse,

\[
\boxed{2^{\max(k-2,0)}\mid ca_3+q^2t},
\]

\[
\boxed{5^{\max(k-2b,0)}\mid ca_3+q^2t}.
\]

Thus the carry residual and the actual-digit tail do carry parallel decimal cores, exactly as sought.

---

# 7. \(\omega\) residue, height, and the finite-height \(\lambda\) index

The inherited tail opening is

\[
\alpha\equiv-8d_\delta t\pmod q,
\]

while \(c\equiv8\pmod q\).  Hence

\[
\boxed{\omega\equiv16d_\delta t\pmod q.}
\tag{OMEGA-q}
\]

For high/boundary, DTF1 gives

\[
\omega=rac{2d_0(q+4)(ca_3+q^2t)}G.
\]

Using \(G/10\le a_3<G\),

\[
\frac{d_0(q+4)c}{5}
\le \omega
<2d_0(q+4)\left(c+\frac{q^2t}{G}\right).
\]

Since \(5^b\le q+4\), \(d_0\le2(q+4)\).  Combining the R7 global \(q^2/G\) bounds with the high/boundary \(t\)-bounds yields a safe pure polynomial upper bound of degree at most \(5\) in \(q\).  Therefore

\[
\omega=16d_0t+q\nu
\]

has a finite-height index \(\nu\) of degree at most \(4\) in \(q\) under the same chamber bounds.

A sharper normalization is available whenever \(g\ge2b\).  Put

\[
M_b:=2^{g-2}5^{g-2b}=\frac{G}{4\cdot5^{2b}},
\]

\[
\boxed{
\lambda:=\frac{ca_3+q^2t}{M_b}\in\mathbf Z_{>0}.
}
\]

Then DTF1 collapses exactly to

\[
\boxed{
\omega=\frac{q+4}{5^b}\lambda.
}
\tag{LAMBDA-OMEGA}
\]

and

\[
\boxed{
\lambda\equiv8\cdot5^{2b}t\pmod q.
}
\tag{LAMBDA-q}
\]

Moreover

\[
\frac25\,5^{2b}c
\le\lambda
<4\cdot5^{2b}\left(c+\frac{q^2t}{G}\right),
\]

so after \(5^b\le q+4\), \(\lambda\) has polynomial degree at most \(5\) in \(q\).  Explicitly, safe pure-q bounds are

\[
\lambda<4(q+4)^2\bigl[c+(3q+12)(3q+8)\bigr]
\quad\text{(high)},
\]

\[
\lambda<4(q+4)^2\bigl[c+9q(9q+4)\bigr]
\quad\text{(boundary)}.
\]

The direct DTF1 bound gives the same degree-5 upper bound for \(\omega\), and therefore \(\nu=(\omega-16d_0t)/q\) has degree at most \(4\).  This is a terminal finite-height index, not a new quotient campaign.

For \(g<2b\), R8 keeps the separate 2-core and does not illegally define \(M_b\).

---

# 8. Boundary \(\alpha\to\omega\) elimination — PROVED

Let

\[
P_\alpha=2q^4+13q^3+10q^2+12q+8,
\]

\[
P_t=5q^6+12q^5-220q^4-672q^3-368q^2+64q+64.
\]

Symbolically,

\[
\boxed{
cP_\alpha-P_t
=2q(q+4)\mathcal S(q),
}
\]

with

\[
\mathcal S(q)=q^5+10q^4+36q^3+108q^2+80q+16.
\]

Hence

\[
\boxed{
\Gamma_B
=2d_0tq(q+4)\mathcal S(q)
-\omega P_\alpha
-2q(D_{\rm fl}s+\chi).
}
\tag{GB-OMEGA}
\]

No \(\alpha\) remains.

Modulo \(q\),

\[
\boxed{
\Gamma_B\equiv-128d_0t\pmod q.
}
\tag{GB-q}
\]

---

# 9. High \(\alpha\to\omega\) elimination — PROVED, with sign correction

Write

\[
\Gamma_H=\mathscr N_H+2Hq\chi.
\]

After \(\alpha=d_0ct-\omega\), exact factorization gives

\[
\boxed{
\mathscr N_H
=-2d_0q(q+4)t\,\mathcal T_H
+\mathcal B_H\omega,
}
\]

where

\[
\begin{aligned}
\mathcal T_H={}&H^2q^5+8H^2q^4+16H^2q^3+48H^2q^2+16H^2q\\
&+2q^4+20q^3+60q^2+64q+16,
\end{aligned}
\]

and

\[
\mathcal B_H
=2H^2q^4+12H^2q^3+q^3+10q^2+12q+8.
\]

Thus

\[
\boxed{
\Gamma_H
=-2d_0q(q+4)t\mathcal T_H
+\mathcal B_H\omega
+2Hq\chi.
}
\tag{GH-OMEGA}
\]

The proposed universal negative residue in the R8 prompt is **false**.  Exact reduction gives

\[
\boxed{
\Gamma_H\equiv+128d_0t\pmod q.
}
\tag{GH-q}
\]

This is consistent with R7's original

\[
\mathscr N_H\equiv-8\alpha+64d_0t\pmod q.
\]

---

# 10. Carry–Digit collision and normalized residual frontier

R8 does not prove \(\Gamma_{B/H}=0\) globally.  Instead, an actual root must satisfy both:

\[
ca_3+q^2t\in M_b\mathbf Z
\]

and

\[
\Gamma_{B/H}\in
2^{g-2}5^{\max(g-2b-v_5(t),0)}\mathbf Z.
\]

When the latter exponent is positive define only the forced normalized residual

\[
\boxed{
\gamma_{B/H}:=
\frac{\Gamma_{B/H}}
{2^{g-2}5^{\max(g-2b-v_5(t),0)}}\in\mathbf Z.
}
\]

The R8 frontier is therefore no longer raw

\[
G\mid\text{prefactor}\cdot\Gamma.
\]

It is

\[
\boxed{
(\lambda\text{ or }\omega/\nu)
+\gamma_{B/H}
+\text{exact carry equation}.
}
\]

The rigorous boundary degree ledger is therefore

| quantity | safe q-degree |
|---|---:|
| \(d_0\) | 1 |
| \(t\) | 1 |
| \(\alpha\) | 5 |
| \(\omega\) | 5 |
| \(\nu\) | 4 |
| \(\lambda\) | 5 |
| \(D_{\rm fl}\) | 7 |
| Euclidean remainder \(r_{\rm fl}\) | 2 |
| \(\chi\) | 9 |
| full \(\Gamma_B\) | 10 |

For boundary the exact Euclidean remainder \(r_{\rm fl}=U-P\), after the frozen bounds \(|\alpha|<30\cdot5^bq^4\), \(t<9q\), satisfies the safe estimate

\[
|r_{\rm fl}|<109q^2+999q+180.
\]

Since \(\chi=D_{\rm fl}(P-\mu)\) and \(0\le U-\mu<1\),

\[
|\chi|<D_{\rm fl}(1+|r_{\rm fl}|),
\]

while \(D_{\rm fl}<3100q^7\).  Thus \(\chi\) has a rigorous degree-9 polynomial upper bound, the non-floor part of \(\Gamma_B\) has degree at most 9, and the complete \(\Gamma_B\) has degree at most \(10\).  At fixed \(H\), the high expression has the same q-degree with coefficients depending on \(H\).  R8 does not claim an \(H\)-uniform height bound independent of the high-tail depth.

---

# 11. Historical 79-state boundary replay — complete exact diagnostic

`J2-55-R8-UnstableResidual-search.py --full-boundary` exactly reproduces

```text
q=7 : 28 DCDC states
q=11: 44
q=17: 5
q=19: 2
TOTAL: 79
```

For every one of the 79 states:

\[
\boxed{
2^{g-2}5^{\max(g-2b,0)}\mid ca_3+q^2t.
}
\]

Thus

\[
\boxed{79/79\text{ pass the actual-digit decimal core}.}
\]

Now for each state, all \(s\in\{0,\ldots,20\}\) were tested against the exact carry-core necessity.  The result is

\[
\boxed{0/79\text{ have even one }s\text{ satisfying both required carry valuations}.}
\]

Hence the whole historical boundary corpus dies at the **unstable carry decimal core**, strictly before any attempt to set \(\Gamma_B=0\).

This is diagnostic, not an infinite boundary theorem.

---

# 12. \(b=0\) 5-adic theorem — PROVED

For high/boundary with \(b=0\), DT-5 is

\[
5^g\mid ca_3+q^2t.
\]

Since \(5\mid c\), while \(q,a_3\) are 5-units,

\[
\boxed{5\mid t.}
\]

Let

\[
v=v_5(c).
\]

If \(g>v\), then cancellation beyond valuation \(v\) forces

\[
\boxed{v_5(t)=v.}
\]

After division by \(5^v\), the correct lift is

\[
\boxed{
q^2\frac{t}{5^v}
\equiv
-\frac{c}{5^v}a_3
\pmod{5^{g-v}}.
}
\tag{T5-LIFT-CORRECTED}
\]

The minus sign corrects the R8 prompt.

### Exact structure of \(v_5(c)\)

If \(q\equiv4\pmod5\), put \(z=q+1\).  Then

\[
c=z^3+7z^2-5z+5\equiv5\pmod{25},
\]

so

\[
\boxed{q\equiv4\pmod5\Longrightarrow v_5(c)=1.}
\]

If \(q\equiv2\pmod5\), put \(y=q-2\).  Then

\[
c=y^3+16y^2+64y+80.
\]

This is a genuine Hensel branch; no naive LTE equality \(v_5(c)=v_5(q-2)\) is valid.  The exact counterexample is

\[
q=7,\qquad c=925,\qquad v_5(c)=2.
\]

---

# 13. \(b>0\) theorem and moderate/deep split

If \(b>0\), then \(c\) is a 5-unit.  Whenever \(g>2b\),

\[
5^{g-2b}\mid ca_3+q^2t
\]

gives

\[
\boxed{
t\equiv-ca_3q^{-2}\pmod{5^{g-2b}}.
}
\]

The tail bounds are short:

\[
t<3q+8\quad\text{(high)},
\qquad
t<9q\quad\text{(boundary)}.
\]

Also

\[
5^b\le q+4.
\]

From the global q-square bounds one obtains the simple exact size consequences

\[
q<2\sqrt G+4\quad\text{(high)},
\]

\[
q<2\sqrt G+9\quad\text{(boundary)},
\]

hence

\[
5^b<2\sqrt G+8\quad\text{(high)},
\]

\[
5^b<2\sqrt G+13\quad\text{(boundary)}.
\]

R8 therefore retains the intended split:

- **moderate \(b\):** \(g\ge2b\), use \(\lambda\) and the long 5-adic tail lift;
- **deep \(b\):** \(g<2b<2g\), keep the 2-core plus the explicit \(b\)-size bound.

No false deep-\(b\) extinction is claimed.

---

# 14. Boundary \(q>1\) campaign status

\[
\boxed{\delta=0,q>1:\ \textbf{OPEN globally}.}
\]

But the R7 frontier has been strictly sharpened:

\[
\boxed{
\lambda\equiv8\cdot5^{2b}t\pmod q,
\quad
\gamma_B\in\mathbf Z,
\quad
\Gamma_B=2d_0tq(q+4)\mathcal S-\omega P_\alpha-2q(D_{\rm fl}s+\chi).
}
\]

The historical 79-state corpus is completely dead at the new carry-core gate.

The conditional R7 theorem \(\Gamma_B=0\Rightarrow\varnothing\) remains inherited but is not invoked globally.

---

# 15. High campaign status and critical \(q=11\) regression

\[
\boxed{\delta>0:\ \textbf{OPEN globally}.}
\]

For the critical benchmark

\[
(q,\delta,\alpha,t)=(11,1,152510,31),
\]

at \(g=471\), exact replay gives

\[
\omega=678600,
\qquad
\lambda=226200,
\]

and

\[
\Gamma_H=-50347080000,
\]

with

\[
v_2(\Gamma_H)=6,
\qquad
v_5(\Gamma_H)=4.
\]

But an actual root would require at \(g=471,b=1,v_5(t)=0\)

\[
v_2(\Gamma_H)\ge469,
\qquad
v_5(\Gamma_H)\ge469.
\]

Therefore this benchmark dies immediately at the new all-exponent carry-core gate.  No global q-descent is used.

---

# 16. \(q=1\) boundary multiplier collapse — PROVED

R7 gives

\[
G\mid(N+t)(31N+21t).
\]

For \(g\ge4\),

\[
N+t=Gt-10a_3
\]

and ten-unit \(a_3\) imply

\[
v_2(N+t)=v_5(N+t)=1.
\]

Write

\[
\boxed{N+t=10r},\qquad \gcd(r,10)=1.
\]

Then

\[
\frac G{100}\mid31r-t.
\]

The frozen \(N\)-strip gives \(N\ge-3\); since \(N+t\) is a nonzero multiple of ten,

\[
\boxed{r\ge1}.
\]

Define

\[
\boxed{
m_1:=\frac{100(31r-t)}G\in\mathbf Z_{>0}.
}
\]

The \(N\)-strip plus \(a_3<G\) yields

\[
\boxed{t\le15},
\]

and in fact the multiplier bound sharpens the proposed \(1612\) to

\[
\boxed{1\le m_1\le1611}.
\]

Modulo ten,

\[
31r\equiv t\pmod{10},
\]

so \(t\) is a ten-unit.  The lower digit bound excludes \(t=1\).  Hence

\[
\boxed{t\in\{3,7,9,11,13\}.}
\]

---

# 17. \(q=1\) reconstruction, local-200 table, and complete periodic closure

From

\[
31r-t=\frac{m_1G}{100}
\]

one gets

\[
\boxed{31N=\frac{m_1G}{10}-21t.}
\]

Let

\[
\zeta:=310t-m_1.
\]

Then

\[
\boxed{31a_3=\frac{\zeta G}{100}-t,}
\]

\[
\boxed{31Z=\frac{4\zeta G}{100}+27t.}
\]

DIG3 gives

\[
\boxed{311\le\zeta\le3100.}
\]

The exact q=1 DCDC polynomial reduces modulo 200 to

\[
\boxed{
200\mid100N^2+158Nt+68t^2+m_1r.
}
\]

For live \(g\ge6\), \(G/100\equiv0\pmod{200}\), so the unique local table is

| \(t\) | \(r\bmod200\) | \(N\bmod200\) | \(m_1\bmod200\) |
|---:|---:|---:|---:|
|3|13|127|130|
|7|97|163|170|
|9|39|181|190|
|11|181|199|10|
|13|123|17|30|

Together with \(1\le m_1\le1611\) and the \(\zeta\)-window this leaves 29 candidates.

Integrality modulo 31 requires

\[
m_1 10^{g-1}\equiv21t\pmod{31}.
\]

Since \(\operatorname{ord}_{31}(10)=15\), 12 candidates die and exactly 17 periodic cells remain:

| \(t\) | \(m_1\) | \(\zeta\) | \(g\bmod15\) | periodic discriminant killer |
|---:|---:|---:|---:|---:|
|3|330|600|9|37|
|7|170|2000|10|3|
|7|370|1800|13|37|
|7|570|1600|8|3|
|7|770|1400|9|3|
|7|1170|1000|1|3|
|7|1370|800|14|3|
|9|790|2000|6|3|
|9|990|1800|9|37|
|9|1190|1600|4|3|
|9|1390|1400|5|3|
|11|410|3000|7|7|
|11|810|2600|12|3|
|11|1010|2400|5|271|
|11|1210|2200|9|3|
|13|1030|3000|4|13|
|13|1430|2600|9|3|

For each cell, substitute the reconstruction into the exact root quadratic

\[
A\frac G8x^2-uD_2x+\Omega=0.
\]

Its discriminant is

\[
\Delta=\frac{D_8(G,m_1,t)}{38440000},
\]

where \(D_8\) is an explicit degree-8 integer polynomial emitted by `J2-55-R8-q1-boundary.py` / the R8 symbolic audit.

For the displayed killer prime \(p\nmid38440000\), the script checks **every** \(g\)-residue in

\[
\operatorname{lcm}\bigl(15,\operatorname{ord}_p(10)\bigr)
\]

compatible with the cell.  In all 17 cells the discriminant is a quadratic nonresidue modulo \(p\).  In particular, the \(p=7,13\) cells require a 30-period audit and both compatible residues are checked.

Therefore

\[
\boxed{q=1,\ \delta=0\Longrightarrow\varnothing.}
\tag{Q1-B-CLOSE}
\]

This is a genuine infinite periodic theorem, not a finite \(g\)-scan.

---

# 18. Reverse DTF1 and \(\alpha\to\omega_R\) — PROVED

Let

\[
r=g-k>0,\qquad R=10^r,\qquad d_r=d_0R,\qquad G=RK.
\]

DTF1 reduces exactly to

\[
\boxed{
K(d_rct-\alpha)
=2d_0(q+4)(ca_3+q^2t).
}
\tag{R-DTF1}
\]

Define

\[
\omega_R=d_rct-\alpha.
\]

Then

\[
\omega_R\equiv16d_rt\pmod q.
\]

Substituting \(\alpha=d_rct-\omega_R\) into the exact R7 reverse numerator gives

\[
\boxed{
\Gamma_R
=-2Rd_0q(q+4)t\,\mathcal T_R
+\mathcal B_R\omega_R
+2q(D_Rs+\chi_R),
}
\tag{GR-OMEGA}
\]

where

\[
\begin{aligned}
\mathcal T_R={}&2R^2q^4+20R^2q^3+60R^2q^2+64R^2q+16R^2\\
&+q^5+8q^4+16q^3+48q^2+16q,
\end{aligned}
\]

\[
\mathcal B_R
=R^2q^3+10R^2q^2+12R^2q+8R^2+2q^4+12q^3.
\]

Modulo \(q\), the exact sign is

\[
\boxed{
\Gamma_R\equiv+128R^3d_0t\pmod q.
}
\]

Thus the prompt's proposed universal negative residue does not extend from boundary to reverse.

---

# 19. Reverse low-\(k\) types — new exact content

For the 11 active \(k=1,b=0\) types

\[
q\in\{7,17,19,29,47,49,59,77,89,97,109\},
\]

R-DT5 gives

\[
\boxed{5\mid t.}
\]

More precisely, since \(K=10\) and \(5\mid ca_3+q^2t\), define

\[
\lambda_R:=\frac{ca_3+q^2t}{5}.
\]

R-DTF1 gives

\[
\boxed{\omega_R=2(q+4)\lambda_R},
\]

and therefore

\[
\boxed{\lambda_R\equiv4t\pmod q.}
\]

For \((k,q)=(2,7)\), \(v_5(c)=2\) and

\[
25\mid ca_3+q^2t
\]

forces

\[
\boxed{25\mid t.}
\]

With

\[
\lambda_R=\frac{ca_3+q^2t}{25},
\]

one has

\[
\boxed{\omega_R=(q+4)\lambda_R},
\qquad
\boxed{\lambda_R\equiv8t\pmod q}.
\]

For \((k,q)=(2,11)\), \(k-2b=0\), so R8 obtains no new 5-content from DT-5.

These types are **not closed** in R8; they are now explicit normalized-tail types rather than an unspecified moving-fibre wedge.

---

# 20. Deep-5 \(k=1\) exceptions

The four types

\[
\boxed{q\in\{11,61,91,101\}}
\]

remain outside the active \(k>b\) reverse tail formula.  R8 does **not** apply R-DTF1 illegally to them.

Their exact frontier is the pre-valuation reverse relation plus fixed \(K=10\) DCDC/root equations.

\[
\boxed{\textbf{OPEN: four explicit deep-5 types}.}
\]

---

# 21. Reverse bulk

Whenever

\[
k\ge2,\qquad k\ge2b,
\]

put

\[
M_{K,b}:=2^{k-2}5^{k-2b}=\frac{K}{4\cdot5^{2b}},
\]

\[
\lambda_R:=\frac{ca_3+q^2t}{M_{K,b}}.
\]

Then R-DTF1 gives the exact normalized law

\[
\boxed{
\omega_R=\frac{q+4}{5^b}\lambda_R,
}
\]

with the same residue

\[
\boxed{
\lambda_R\equiv8\cdot5^{2b}t\pmod q.
}
\]

An actual reverse root also forces the normalized carry residual

\[
\boxed{
\gamma_R=
\frac{\Gamma_R}
{2^{\max(k-2,0)}5^{\max(k-2b-v_5(t),0)}}\in\mathbf Z.
}
\]

This replaces the R7 raw frontier by a two-object normalized frontier:

\[
\boxed{(\lambda_R,\gamma_R)}.
\]

R8 does not yet prove reverse bulk extinction, so the old \(qK=1169\) threshold is not claimed obsolete as a theorem, but it is no longer the conceptual terminal coordinate system.

---

# 22. \(q=1\) reverse

The three explicit exceptional types remain

\[
\boxed{(q,k)=(1,1),(1,2),(1,3)}.
\]

The generic q-tail formula is not applied.  The exact q=1 fixed-\(K\) Euclidean law and DCDC polynomial remain the correct interfaces.

The old pre-DCDC family \((N,t)=(7,3)\) is still uniformly killed by \(\widetilde F\equiv3\pmod5\), but R8 does not elevate that single family to a complete q=1 reverse theorem.

Thus

\[
\boxed{\delta<0,q=1:\ \textbf{OPEN at exactly three }k\textbf{-types}.}
\]

---

# 23. Computation and certificates

Generated and executed:

```text
J2-55-R8-DecimalCore-symbolic.py          PASS
J2-55-R8-UnstableResidual-search.py       PASS (full 79-state replay via --full-boundary)
J2-55-R8-q1-boundary.py                   PASS; 17/17 periodic cells killed
J2-55-R8-lowk-DTF.py                      PASS
```

Generated ledgers:

```text
J2-55-R8-q1-boundary-cells.tsv
J2-55-R8-lowk-ledger.tsv
J2-55-R8-UnstableResidual-diagnostics.tsv
J2-55-R8-survivors.tsv
```

All theorem gates use exact integer/Fraction/SymPy arithmetic.

---

# 24. Counterexample / correction ledger

### C1 — all-exponent \(\Gamma=0\)

**FALSE / remains retired.**  R8 works with exact divisibility.

### C2 — universal high residue \(-128d_0t\)

**FALSE.**  Correct:

\[
\Gamma_H\equiv+128d_0t\pmod q.
\]

### C3 — universal reverse residue \(-128\cdots\)

**FALSE.**  Correct:

\[
\Gamma_R\equiv+128R^3d_0t\pmod q.
\]

### C4 — proposed T5 lift sign

**CORRECTED.**  The lift has a minus sign.

### C5 — naive \(v_5(c)=v_5(q-2)\)

**FALSE.**  \(q=7\) gives \(v_5(c)=2\) while \(v_5(q-2)=1\).

### C6 — force-\(\Gamma=0\) as the only globalization route

**DISFAVORED by computation.**  The complete historical 79-state corpus is killed already because nonzero \(\Gamma_B\) lacks the required decimal depth.

---

# 25. Exact survivor frontier after R8

R8 does **not** return the R7 raw statement

\[
G/K\mid\text{prefactor}\cdot\Gamma.
\]

The surviving exact frontier is:

### High \(q>1\)

\[
\boxed{
\lambda\text{ (or deep-}b\text{ 2-core)}
+\gamma_H
+\Gamma_H(\omega,\chi)=0\pmod{\text{forced decimal core}}.
}
\]

### Boundary \(q>1\)

\[
\boxed{
\lambda\equiv8\cdot5^{2b}t\pmod q
+\gamma_B
+0\le s\le20.
}
\]

### Boundary \(q=1\)

\[
\boxed{\textbf{CLOSED}.}
\]

### Reverse active \(k=1,b=0\)

Eleven explicit types, now with

\[
5\mid t,
\qquad
\lambda_R=(ca_3+q^2t)/5,
\qquad
\lambda_R\equiv4t\pmod q.
\]

### Reverse \(k=2\)

\[
(q,k)=(7,2):\quad25\mid t,
\]

\[
(q,k)=(11,2):\quad\text{no new 5-content from R8 DT-core}.
\]

### Deep-5 reverse \(k=1\)

Exactly four explicit types

\[
q\in\{11,61,91,101\}.
\]

### Reverse \(q=1\)

Exactly

\[
k\in\{1,2,3\}.
\]

---

# 26. J2 closure audit

## I1 DTF1

\[
\boxed{\textbf{PROVED}.}
\]

## I2 \(t\) odd

\[
\boxed{\textbf{PROVED}.}
\]

## I3 carry residual decimal depth

\[
\boxed{\textbf{PROVED}.}
\]

## I4 \(b=0\Rightarrow5\mid t\) high/boundary

\[
\boxed{\textbf{PROVED}.}
\]

## I5 exact \(v_5(t)=v_5(c)\) when \(g>v_5(c)\)

\[
\boxed{\textbf{PROVED},\text{ with corrected minus-sign lift}.}
\]

## I6 global unstable residual elimination

\[
\boxed{\textbf{OPEN globally};\ 79/79 historical boundary states eliminated.}
\]

## I7 high closure

\[
\boxed{\textbf{OPEN globally}.}
\]

## I8 boundary \(q>1\) closure

\[
\boxed{\textbf{OPEN globally}.}
\]

## I9 q=1 boundary closure

\[
\boxed{\textbf{PROVED}.}
\]

## I10 reverse active \(k=1,b=0\): \(5\mid t\)

\[
\boxed{\textbf{PROVED for all 11 active types}.}
\]

## I11 reverse low-k extinction

\[
\boxed{\textbf{OPEN};\text{ frontier is now explicit type-by-type}.}
\]

## I12 reverse bulk decimal-core collision

\[
\boxed{\textbf{OPEN at }(\lambda_R,\gamma_R).}
\]

Therefore the terminal completion criterion is not yet met:

\[
\boxed{
J=2\Longrightarrow\varnothing
\quad\textbf{NOT YET PROVED}.
}
\]

No closure certificate is generated.

---

# File Audit

Generated in R8:

```text
J2-55-R8-Unstable-Decimal-Core-Report.md
J2-55-R8-DecimalCore-symbolic.py
J2-55-R8-UnstableResidual-search.py
J2-55-R8-q1-boundary.py
J2-55-R8-lowk-DTF.py
J2-55-R8-certificate.txt
J2-55-R8-survivors.tsv
J2-55-R8-q1-boundary-cells.tsv
J2-55-R8-lowk-ledger.tsv
J2-55-R8-UnstableResidual-diagnostics.tsv
```

Not generated:

```text
J2-Resonance-Closure-Certificate.md
```

because \(J2\) remains open.
