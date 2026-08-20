# Primitive Sector-Congruence Lemma — PROVED

## Statement

Let \(m\ge1\). Let \([r_1:r_2]\in\mathbf P^1(\mathbf Z/m\mathbf Z)\) be unimodular:
\[
\gcd(r_1,r_2,m)=1.
\]

Let
\[
I=(\alpha,\beta)
\]
be an affine projective interval with
\[
\delta=\beta-\alpha>0,
\qquad
B=\max(1,|\alpha|,|\beta|).
\]

Then there exists a primitive integer pair \((s,t)\) such that

\[
[s:t]\in I,
\]
\[
[s:t]\equiv[r_1:r_2]\pmod m,
\]
and, for \(0<\delta\le1\),
\[
\boxed{
H(s,t)
\le
3(B+1)\,m\,\delta^{-1}.
}
\tag{PSC}
\]

Hence the modulus exponent needed here is
\[
\boxed{\alpha_{\rm modulus}=1}.
\]

## Proof

Choose a positive integer
\[
t\equiv r_2\pmod m
\]
with
\[
\frac{2m}{\delta}\le t<\frac{2m}{\delta}+m.
\]

Then
\[
|tI|=\delta t\ge2m.
\]
Integers congruent to \(r_1\pmod m\) have spacing \(m\), so there exists
\[
s\equiv r_1\pmod m
\]
with
\[
\alpha t<s<\beta t.
\]

Therefore \([s:t]\in I\), and
\[
|s|\le Bt+m.
\]
For \(\delta\le1\),
\[
H(s,t)\le3(B+1)m\delta^{-1}.
\]

Now let
\[
d=\gcd(s,t).
\]
If a prime \(p\mid d\) also divided \(m\), then
\[
p\mid r_1,\qquad p\mid r_2,
\]
contradicting unimodularity modulo \(m\). Hence
\[
\gcd(d,m)=1.
\]

Divide:
\[
(s',t')=(s/d,t/d).
\]
This pair is primitive; its real projective point is unchanged; modulo \(m\) it is multiplied by the unit \(d^{-1}\), so it represents the same point of
\(\mathbf P^1(\mathbf Z/m\mathbf Z)\); and its height only decreases.

This proves (PSC).

## Consequence

The primitive requirement has **zero additional asymptotic cost** beyond projective congruence approximation.

The theorem also shows why the exponent \(\rho^{-2}\) for source height is elementary:
\[
H(s,t)\ll m\rho^{-1}
\quad\Longrightarrow\quad
a_0\ll m^2\rho^{-2}.
\]

If the target interval crosses the affine point at infinity, use the other standard affine chart. No homogeneous dynamics is needed.
