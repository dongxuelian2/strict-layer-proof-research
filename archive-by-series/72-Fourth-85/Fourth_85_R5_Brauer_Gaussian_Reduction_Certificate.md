# Fourth 85 · R5 — Brauer-to-Gaussian Reduction Certificate

Let

\[
A=A_2(G,K),\qquad T=T_4(G,K).
\]

Define

\[
S=1-(4K^2-3)G-(8K^2-10)G^2-(4K^2-4)G^3,
\]

\[
Q=(4K^2+21)G^2+(8K^2+12)G+(4K^2+1).
\]

Then direct expansion gives

\[
\boxed{A+S^2=TQ}.
\]

Define

\[
R=\frac1{58}\Big(
2100(K^2-1)G^5+(4180K^2-6280)G^4
+(1296K^2-6085)G^3
-(1376K^2+1737)G^2
+(-420K^2+348)G
+(172K^2+58)\Big).
\]

Then

\[
R^2-Q=A H
\]

for

\[
H=\frac1{3364}\Big(
44100(K^2-1)G^4+(52080K^2-96180)G^3
-(20744K^2+44125)G^2
+(-21328K^2+14268)G
+7396K^2+1624\Big).
\]

Also

\[
\operatorname{Res}_G(A,Q)
=
4(1152K^6+14864K^4+2016K^2+5093)^2\ne0.
\]

Hence:

- at every \(T\)-zero, \(-A=S^2\), so the residue of \((-A,T)\) is trivial;
- at every \(A\)-zero, \(Q=R^2\ne0\) and \(S^2=TQ\), hence \(T=(S/R)^2\), so the residue is trivial;
- at infinity, the valuations \(-6,-4\) are both even.

Therefore \((-A,T)\) is an unramified class on \(\mathbf P^1_{\mathbf Q}\), hence constant. At \(G=0\),

\[
(-A(0),T(0))=(-4K^2,1)=0.
\]

Thus

\[
\boxed{(-A,T)=0}
\]

and finally

\[
\boxed{
(A,T)=(-1,T)
\in\operatorname{Br}(\mathbf Q(G))[2].
}
\]

For \(G=10^g\), this specializes to

\[
\boxed{
(A_{K,g},T_{K,g})=(-1,T_{K,g}).
}
\]

So the specialized class vanishes iff \(T_{K,g}\) is a norm from \(\mathbf Q(i)\), equivalently iff every prime \(p\equiv3\pmod4\) occurs in \(T_{K,g}\) to even exponent.
