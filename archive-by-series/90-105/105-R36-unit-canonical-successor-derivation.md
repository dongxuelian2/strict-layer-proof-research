# 105-R36 — Unit Canonical-Successor Derivation

## 1. Authoritative regular source fibre
R30/R8 freeze
\[
L_i=\frac{10^{n_i-1}}{C_i},\qquad R_i=\frac{10^{n_i}}{C_i},\qquad
L=\max(L_2,L_3),\quad R_{\rm src}=\min(R_2,R_3),
\]
with the half-open interval \([L,R_{\rm src})\). The full fixed source-native periodic predicate is encoded by
\[
\mathcal R_0\subseteq\mathbf Z/P_0\mathbf Z.
\]
With \(V_0=\Lambda u_0AW\), a literal completed period is
\[
M_U=\operatorname{lcm}(P_0,V_0),
\]
\[
\mathcal R_{\rm adm}=\{r\bmod M_U:r\bmod P_0\in\mathcal R_0,\ (r,V_0)=1\}.
\]
One may replace \(V_0\) by \(\operatorname{rad}(V_0)\) in the period without changing coprimality truth.

For a regular closed lower endpoint, set
\[
\ell=\max(L,1).
\]
Then
\[
S_r(L)=r+M_U\left\lceil\frac{\ell-r}{M_U}\right\rceil,
\qquad
\boxed{U_{\min}=\min_{r\in\mathcal R_{\rm adm}}S_r(L)}.
\]
If \(\mathcal R_{\rm adm}=\varnothing\), define \(U_{\min}=+\infty\). The source fibre is nonempty exactly when
\[
\boxed{U_{\min}<R_{\rm src}},
\]
together with the frozen source-completed predicate.

## 2. Integer endpoint form and correction to the proposed delay
Because \(L\) is generally rational, \([r-L]_{M_U}\) is not an integer residue operation. The exact integer lower edge is
\[
U_{\rm lo}=\left\lceil\max(L,1)\right\rceil.
\]
For each admissible residue define the canonical integer delay
\[
d_r=[r-U_{\rm lo}]_{M_U}\in\{0,\ldots,M_U-1\}.
\]
Then
\[
U_r=U_{\rm lo}+d_r,\qquad d_{\min}=\min_r d_r,
\qquad \boxed{U_{\min}=U_{\rm lo}+d_{\min}}.
\]
Thus the exact delay criterion is
\[
\boxed{d_{\min}<R_{\rm src}-U_{\rm lo}}.
\]
Equivalently in integer form, with
\[
U_{\rm hi}=\min\left(\left\lfloor\frac{10^{n_2}-1}{C_2}\right\rfloor,\left\lfloor\frac{10^{n_3}-1}{C_3}\right\rfloor\right),
\]
source nonemptiness is \(U_{\min}\le U_{\rm hi}\). The prompt's \(d_{\min}<R-L\) is exact only in the special case where the active lower endpoint itself is the relevant integral starting point.

## 3. Face A / Face B exact final gates
Face A, \(L_2\ge L_3\):
\[
G_A=C_2 10^{n_3}-C_3 10^{n_2-1},\qquad
J_{{\rm src},2}=C_2U_{\min}-10^{n_2-1},
\]
\[
\boxed{C_3J_{{\rm src},2}<G_A.}
\]
Face B, \(L_3>L_2\):
\[
G_B=C_3 10^{n_2}-C_2 10^{n_3-1},\qquad
J_{{\rm src},3}=C_3U_{\min}-10^{n_3-1},
\]
\[
\boxed{C_2J_{{\rm src},3}<G_B.}
\]
These are the authoritative final source inequalities.

## 4. Decorated historical q_src=1 firewall
The historical source-chart label \(q_{\rm src}=1\) is not the residual denominator \(q\). Its open interval and affine congruence are chart-local:
\[
\frac{d_q\tau_{\rm src}G}{10C_3}<U<\frac{G}{C_3},\qquad
31C_3U+d_q\tau_{\rm src}\equiv0\pmod{2Kd_q}.
\]
Its step is \(h_U=2Kd_q/\gcd(C_3,2Kd_q)\) when solvable. R36 never imports this progression merely from residual \(Q_-=1\).

## 5. Unit verdict
No theorem among “no admissible residue”, “period exceeds room”, “endpoint misalignment”, or final Face A/B inequality was proved universally from \(Q_-=1\). No genuine legal unit source-complete point was found either.

```text
UNIT_CANONICAL_SUCCESSOR_EXTINCTION=NOT_PROVED_NOT_FALSIFIED
```
