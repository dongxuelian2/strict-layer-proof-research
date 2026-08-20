# 105-R8 — Post-PSDG Common-\(U\) Integer Source Fibre

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — \(A_1\)-only  
**Round:** 105-R8  
**Scope:** Post-PSDG First-Failure Assault  
**Archive:** `105_R8_Common_U_Integer_Source_Fibre.md`

---

## 1. Executive Verdict

R8 得到一个**严格但非闭合**的结果。

\[
\boxed{\texttt{CANONICAL\_SOURCE\_SUCCESSOR\_THEOREM\_PROVED}}
\]

对每个 frozen post-PSDG source-completed profile \(p\)，absolute source fibre 确实是 rank one；其唯一剩余 semantic radial coordinate 是 \(U\)。在 regular completed strata 上，minimal A1 radial interval 精确为

\[
I_{23}(p)=
\left[
\max\!\left(\frac{10^{n_2-1}}{C_2},\frac{10^{n_3-1}}{C_3}\right),
\min\!\left(\frac{10^{n_2}}{C_2},\frac{10^{n_3}}{C_3}\right)
\right).
\]

真正 source-admissible integers 构成一个 periodic residue selector；因此存在 canonical successor

\[
U_{\min}(p)=\operatorname{Succ}_{\rm src}(L(p)),
\]

并有 exact equivalence

\[
\boxed{
\mathcal U_{\rm src}(p)\neq\varnothing
\iff
U_{\min}(p)<R(p).
}
\]

更强地，minimal \(I_{23}\) 只有两个 active faces。若

\[
L_2\ge L_3,
\]

则

\[
[L,R)=[L_2,R_3),
\]

并令

\[
G_A=C_2\,10^{n_3}-C_3\,10^{n_2-1},
\qquad
J_{{\rm src},2}=C_2U_{\min}-10^{n_2-1}.
\]

则 full source lift 精确等价于

\[
\boxed{
C_3J_{{\rm src},2}<G_A.
}
\tag{R8-A}
\]

若

\[
L_3>L_2,
\]

令

\[
G_B=C_3\,10^{n_2}-C_2\,10^{n_3-1},
\qquad
J_{{\rm src},3}=C_3U_{\min}-10^{n_3-1},
\]

则 full source lift 精确等价于

\[
\boxed{
C_2J_{{\rm src},3}<G_B.
}
\tag{R8-B}
\]

这就是 R8 的最终 canonical “interval width versus source successor delay” 形式。

但是，本轮**没有**证明对整个 post-PSDG family：

\[
U_{\min}\ge R.
\]

也没有构造出一个 \(U_{\min}<R\) 的 genuine post-PSDG integer-radial witness。因此：

\[
\boxed{
\texttt{POST\_PSDG\_SOURCE\_RADIAL\_FIBRE\_EMPTY=NOT\_PROVED}
}
\]

以及

\[
\boxed{
\texttt{SOURCE\_RADIAL\_LIFT=NO\_WITNESS\_FOUND}
}
\]

必须同时保留。

R7D exact reduced-witness registry 的四个 frozen PSDG hits \(A,B,C,E\) 经 R8 exact replay 后：

- \(A,C\)：死于 continuous fibre；
- \(B,E\)：continuous fibre 非空，但死于 positive integer successor；
- 四者均无 radial lift；
- 四者均满足 \(R\le1\)。

这只是 exact finite census，不是 universal theorem。

因此 R8 的严格终点为：

\[
\boxed{
\texttt{R8\_REDUCED\_TO\_SINGLE\_SOURCE\_SUCCESSOR\_INEQUALITY}.
}
\]

R9 仅授权 Route D：

\[
\boxed{
\textbf{Post-PSDG Endpoint Quotient / Unit Alignment}.
}
\]

---

## 2. Frozen R1–R7D State

R1–R7D 全部冻结。

R8 不重新研究：

- discriminant / square locus；
- Gaussian packets；
- determinant packet allocation；
- PSDG；
- source \(g_1\) firewall；
- primitive sphere parametrization；
- Smith redesign；
- DES redesign；
- valuation atlas；
- moving-base phase。

R8 只读取这些 frozen outputs 作为 fixed base-profile data。

---

## 3. R7D Gate-Crossing Witness

Canonical witness \(B\)：

\[
(b_1,b_2,b_3)=(1,6,8),
\]

\[
(P_1,P_2,P_3,Q_0)=(48,436,75,445),
\qquad
V=24.
\]

R7D reduced data：

\[
h=1,\quad \varepsilon=1,\quad
X_0=493,\quad Y_0=397,
\]

\[
M=195721=17\cdot29\cdot397,
\]

\[
a'=52,\quad b'=73,\quad\Delta=3345,
\]

\[
73\cdot397-52\cdot493=3345.
\]

Frozen downstream：

\[
(g_1,g_2,g_3)=(24,4,3),
\]

\[
(C_1,C_2,C_3)=(2,109,25),
\]

\[
(s,\alpha,\beta,t,u,v)=(1,1,2,3,1,4),
\]

\[
D_{\rm lead}=35,\qquad H=2320,\qquad K_3=296.
\]

其 R8 interval：

\[
L_2=\frac{10}{109},
\qquad
L_3=\frac1{25},
\]

故 active face 为 A：

\[
\boxed{
I_{23}=
\left[\frac{10}{109},\frac25\right).
}
\]

---

## 4. Post-PSDG Profile Space

定义 \(\mathscr P_{\rm post}\) 为所有已经通过 frozen：

\[
\text{sphere}
+\text{master}
+\text{primitive}
+\text{PSDG}
+\text{Smith}
+\text{DES}
+\text{source }g_1\text{ firewall}
\]

且保留 exact source-completed base data 的 profiles。

每个 \(p\in\mathscr P_{\rm post}\) 至少固定：

\[
(P_1,P_2,P_3,Q_0),
\quad
V,
\quad
g_i=\gcd(V,P_i),
\quad
C_i=P_i/g_i,
\]

\[
(n_2,n_3,m_2,m_3,g,k),
\]

以及当前 stratum 的 source affine transport data。

R8 不把 \(U\) 放进 base profile；\(U\) 是 fibre coordinate。

---

## 5. Source Fibre Rank Audit

对 fixed \(p\)：

\[
(a_1,a_2,a_3)=U(C_1,C_2,C_3).
\]

\(C_i,V,n_i\) 已固定，且所有 q>1 / H0 / resonance / transition / outer completed charts 中 source coordinate transport 为 \(U\mapsto U\)。

q=1 source-completed chart中虽然有 affine observable

\[
\rho=\frac{UC_3}{d_q}-\frac{\tau G}{10},
\]

但 \(\rho\) 是 \(U\) 的 affine image，不是第二个独立 fibre parameter。

因此：

\[
\boxed{
\texttt{POST\_PSDG\_SOURCE\_FIBRE\_RANK=1}.
}
\]

---

## 6. Exact Radial Variable \(U\)

Canonical radial variable：

\[
\boxed{
U=\gcd(a_1,a_2,a_3)\in\mathbf Z_{>0}.
}
\]

Primitive source condition：

\[
\boxed{\gcd(U,V)=1.}
\]

在 minimal A1 semantics 下，\(n_1\) 可由 \(a_1=UC_1\) existentially 恢复；因此当前 radial digit gate 只需固定 blocks 2,3。

---

## 7. Full Real Source Interval

定义

\[
L_i=\frac{10^{n_i-1}}{C_i},
\qquad
R_i=\frac{10^{n_i}}{C_i}=10L_i,
\qquad i=2,3.
\]

regular completed strata：

\[
\boxed{
I_{\mathbf R}(p)=I_{23}(p)
=[L,R)
}
\]

其中

\[
L=\max(L_2,L_3),
\qquad
R=\min(R_2,R_3).
\]

### q=1 exact boundary correction

在 historical q=1 negative source stratum，还必须保留 exact \(\rho\)-window

\[
0<\rho<
\frac{10-d_q\tau}{10d_q}G.
\]

拉回 \(U\) 后精确成为

\[
\boxed{
\frac{d_q\tau G}{10C_3}<U<\frac{G}{C_3}.
}
\tag{Q1-W}
\]

因此 q=1 的 exact real fibre 是

\[
I_{23}\cap
\left(
\frac{d_q\tau G}{10C_3},
\frac{G}{C_3}
\right).
\]

这说明一个必须保留的 exactness point：

> q=1 historical negative stratum 的 active lower boundary 可能是 **open**。  
> 不能为了形式统一把它伪写成 closed \([L,R)\)。

因此 R8 的最一般 canonical object 是一个 **decorated interval**；regular strata 才严格是 \([L,R)\)。

---

## 8. Lower Endpoint Registry

regular minimal A1：

\[
L_2=\frac{10^{n_2-1}}{C_2},
\qquad
L_3=\frac{10^{n_3-1}}{C_3}.
\]

q=1 historical negative optional branch lower：

\[
L_{q1}=\frac{d_q\tau G}{10C_3},
\qquad \text{boundary=open}.
\]

每个 digit endpoint 可 reduced：

\[
d_i=\gcd(C_i,10^{n_i-1}),
\]

\[
L_i=
\frac{10^{n_i-1}/d_i}{C_i/d_i}.
\]

故 endpoint fractional denominator 是

\[
\boxed{
B_i^{\rm red}=\frac{C_i}{\gcd(C_i,10^{n_i-1})}.
}
\]

这就是 absolute endpoint phase 的精确 denominator。

---

## 9. Upper Endpoint Registry

regular：

\[
R_2=\frac{10^{n_2}}{C_2},
\qquad
R_3=\frac{10^{n_3}}{C_3}.
\]

q=1 historical negative optional branch upper：

\[
R_{q1}=\frac{G}{C_3},
\qquad \text{boundary=open}.
\]

---

## 10. Active-Boundary Atlas

因为

\[
R_i=10L_i,
\]

只存在两个非平凡 regular active faces。

### Face A

若

\[
L_2\ge L_3,
\]

则：

\[
\boxed{
L=L_2,\qquad R=R_3.
}
\]

### Face B

若

\[
L_3>L_2,
\]

则：

\[
\boxed{
L=L_3,\qquad R=R_2.
}
\]

### Tie

若

\[
L_2=L_3,
\]

则：

\[
[L,R)=[L_2,10L_2).
\]

所以 minimal A1 不需要四对 \((L_i,R_j)\) broad branching；只有两条 cross-face。

q=1 branch factor若 active，只作为 decorated interval 的附加 lower/upper boundary，不重新制造 broad atlas。

---

## 11. Continuous Fibre Criterion

Face A 定义

\[
\boxed{
G_A=C_2\,10^{n_3}-C_3\,10^{n_2-1}.
}
\]

则：

\[
I_{23}\neq\varnothing
\iff
G_A>0.
\]

且

\[
|I_{23}|=\frac{G_A}{C_2C_3}.
\]

Face B 定义

\[
\boxed{
G_B=C_3\,10^{n_2}-C_2\,10^{n_3-1}.
}
\]

则：

\[
I_{23}\neq\varnothing
\iff
G_B>0,
\]

\[
|I_{23}|=\frac{G_B}{C_2C_3}.
\]

这与 historical DES/radial-gap bridge 相容，但 R8 不重新证明 DES。

---

## 12. Positive-Integer Fibre Criterion

对 regular half-open interval：

\[
[L,R)\cap\mathbf Z_{>0}\neq\varnothing
\]

当且仅当

\[
\boxed{
U_{\mathbf Z}:=\max(1,\lceil L\rceil)<R.
}
\]

因为 \(L>0\)，实际上

\[
U_{\mathbf Z}=\lceil L\rceil.
\]

half-open upper endpoint 的 strict inequality \(U_{\mathbf Z}<R\) 不可改为 \(\le\)。

q=1 left-open decorated lower需要使用 strict successor：

\[
\min\{u\in\mathbf Z_{>0}:u>L_{\rm open}\},
\]

不能机械使用 \(\lceil L_{\rm open}\rceil\) 当 \(L_{\rm open}\in\mathbf Z\)。

---

## 13. Plain Integer Successor

Face A：

\[
U_{\mathbf Z}
=
\left\lceil\frac{10^{n_2-1}}{C_2}\right\rceil.
\]

定义 endpoint modular jump

\[
\boxed{
\delta_2:=(-10^{n_2-1})\bmod C_2,
\qquad
0\le\delta_2<C_2.
}
\]

则：

\[
\boxed{
U_{\mathbf Z}
=
\frac{10^{n_2-1}+\delta_2}{C_2}.
}
\]

于是

\[
U_{\mathbf Z}<R_3
\]

精确等价于：

\[
\boxed{
C_3\delta_2<G_A.
}
\tag{PI-A}
\]

Face B 同理：

\[
\delta_3:=(-10^{n_3-1})\bmod C_3,
\]

\[
\boxed{
C_2\delta_3<G_B.
}
\tag{PI-B}
\]

这已经把 floor/ceil 全部消成 integer cross-product。

---

## 14. Endpoint Fractional Phase

若 active lower 为

\[
L_i=\frac{10^{n_i-1}}{C_i},
\]

Euclidean division：

\[
10^{n_i-1}=q_iC_i+r_i,
\qquad
0\le r_i<C_i.
\]

则：

\[
\lceil L_i\rceil=
q_i+\mathbf 1_{r_i>0}.
\]

plain successor delay：

\[
D_{\mathbf Z}=
\lceil L_i\rceil-L_i
=
\begin{cases}
0,&r_i=0,\\[1mm]
\dfrac{C_i-r_i}{C_i},&r_i>0.
\end{cases}
\]

亦即

\[
\boxed{
D_{\mathbf Z}=\frac{\delta_i}{C_i}.
}
\]

这是真正合法的 R8 phase：

\[
\boxed{
\textbf{absolute source endpoint phase}
=
10^{n_i-1}\bmod C_i.
}
\]

它不是 R5 moving-base mantissa phase。

---

## 15. Source Progression Recovery

### Generic / non-q1 completed strata

R2 source transport给出：

\[
\boxed{
\Lambda_{\rm src}=\mathbf Z,
\qquad h_U=1.
}
\]

Smith saturation index \(J\) 不是 \(U\)-lattice index。

### q=1 source-completed stratum

exact congruence：

\[
\boxed{
31C_3U+d_q\tau\equiv0
\pmod{2Kd_q}.
}
\tag{Q1-CONG}
\]

令

\[
N_q=2Kd_q,
\qquad
d_U=\gcd(C_3,N_q).
\]

因为 \(31\) 与 \(N_q\) 互素，solvability iff

\[
\boxed{
d_U\mid d_q\tau.
}
\]

若可解：

\[
\boxed{
h_U=\frac{2Kd_q}{d_U}.
}
\]

并有唯一 residue

\[
\boxed{
U\equiv r_{q1}\pmod{h_U},
}
\]

其中

\[
r_{q1}
\equiv
-\frac{d_q\tau}{d_U}
\left(\frac{31C_3}{d_U}\right)^{-1}
\pmod{h_U}.
\]

这就是 q=1 的 source-canonical affine \(U\)-lattice。

---

## 16. Source Residue Selector

若 base affine lattice为：

\[
U\equiv r_0\pmod h
\]

并加入

\[
\gcd(U,V)=1,
\]

取

\[
M_U=\operatorname{lcm}(h,V).
\]

定义：

\[
\boxed{
\mathcal R_{\rm adm}
=
\{r\bmod M_U:
r\equiv r_0\pmod h,\ \gcd(r,V)=1\}.
}
\]

则：

\[
\boxed{
U\text{ source-admissible}
\iff
U\bmod M_U\in\mathcal R_{\rm adm}.
}
\]

generic \(h=1\) 时：

\[
M_U=V,
\qquad
\mathcal R_{\rm adm}=(\mathbf Z/V\mathbf Z)^\times.
\]

### q=1 historical \(\gcd(\rho,10\tau)=1\)

若该 source-native predicate 在当前 q=1 stratum active，则它仍可 finite-period 化。

沿

\[
U=r_{q1}+h_Uz
\]

有：

\[
\rho(z)=\rho_0+\Delta_\rho z,
\]

\[
\Delta_\rho=
\frac{2KC_3}{\gcd(C_3,2Kd_q)}.
\]

令

\[
Q_\rho=\operatorname{rad}(10\tau),
\qquad
T_\rho=
\frac{Q_\rho}{\gcd(\Delta_\rho,Q_\rho)}.
\]

则 \(\gcd(\rho,10\tau)=1\) 对 \(z\) 的 truth value 以 \(T_\rho\) 为周期。

因此可把 selector period refinement 为：

\[
\operatorname{lcm}(V,h_UT_\rho),
\]

并显式枚举 finite admissible residue set。历史条件 `gcd(Y,10)=1` 若在该 q=1 stratum active，则它是 fixed base-profile predicate：不满足时整条 profile 直接 source-empty；满足时它不再改变 U-residue period。

---

## 17. Coprimality \((U,V)=1\)

Coprimality不是新 geometry，而是 source arithmetic selector：

\[
\boxed{
(U,V)=1.
}
\]

generic chart中，full source set：

\[
\boxed{
\mathcal U_{\rm src}
=
[L,R)\cap
\{U\in\mathbf Z_{>0}:(U,V)=1\}.
}
\]

q=1 中还需 intersect affine progression及当前 active q1 predicates。

必须区分：

1. real fibre；
2. plain integer fibre；
3. source arithmetic fibre。

---

## 18. Canonical Source Successor

设 full periodic selector有 period \(M_U\) 与 residue set

\[
\mathcal R_{\rm adm}\subseteq\mathbf Z/M_U\mathbf Z.
\]

对 regular closed lower endpoint，令

\[
\ell=\max(L,1).
\]

对 canonical residue representative \(0\le r<M_U\)，定义

\[
\boxed{
S_r(L)
=
r+
M_U
\left\lceil
\frac{\ell-r}{M_U}
\right\rceil.
}
\]

若 \(\mathcal R_{\rm adm}\neq\varnothing\)：

\[
\boxed{
U_{\min}
=
\min_{r\in\mathcal R_{\rm adm}}S_r(L).
}
\]

若 residue set empty：

\[
U_{\min}=+\infty.
\]

于是：

\[
\boxed{
\mathcal U_{\rm src}\neq\varnothing
\iff
U_{\min}<R.
}
\tag{CSS}
\]

这就是：

\[
\boxed{
\textbf{Common-}U\textbf{ Integer Successor Criterion}.
}
\]

对 left-open decorated lower，唯一修改是把每个 residue 的 closed ceiling 换成 strict successor；finite residue theorem本身不变。

---

## 19. Width vs Successor Delay

定义：

\[
W_U=R-L,
\]

\[
D_U=U_{\min}-L,
\]

\[
\sigma_U=R-U_{\min}.
\]

则：

\[
\boxed{
\sigma_U=W_U-D_U.
}
\]

source radial lift：

\[
\boxed{
\sigma_U>0.
}
\]

source radial extinction：

\[
\boxed{
\sigma_U\le0.
}
\]

### Integer cross-product form

Face A：

\[
J_{{\rm src},2}
=
C_2U_{\min}-10^{n_2-1}.
\]

则

\[
D_U=\frac{J_{{\rm src},2}}{C_2},
\qquad
W_U=\frac{G_A}{C_2C_3},
\]

所以：

\[
\boxed{
\sigma_U>0
\iff
C_3J_{{\rm src},2}<G_A.
}
\]

Face B：

\[
\boxed{
\sigma_U>0
\iff
C_2J_{{\rm src},3}<G_B.
}
\]

这是 R8 最终 single gate 的最佳 integer form。

---

## 20. Normalized Fibre Width

必须区分两个尺度。

### Affine lattice step

\[
h_U=
\begin{cases}
1,&\text{generic completed strata},\\
2Kd_q/\gcd(C_3,2Kd_q),&q=1.
\end{cases}
\]

定义：

\[
\omega_{\rm aff}=\frac{W_U}{h_U}.
\]

### Full selector period

若 coprimality/periodic predicates已经合并成 modulus \(M_U\)，定义：

\[
\omega_{\rm sel}=\frac{W_U}{M_U}.
\]

若

\[
\omega_{\rm sel}<1,
\]

每个 admissible residue class至多贡献一个 hit。

但：

\[
\boxed{
\omega_{\rm sel}<1
\not\Rightarrow
\mathcal U_{\rm src}=\varnothing.
}
\]

仍必须计算 successor。

---

## 21. \(R\le1\) Extinction Attempt

Face A：

\[
R=R_3=\frac{10^{n_3}}{C_3}.
\]

因此：

\[
\boxed{
R\le1
\iff
C_3\ge10^{n_3}.
}
\]

Face B：

\[
\boxed{
R\le1
\iff
C_2\ge10^{n_2}.
}
\]

R7D exact four-profile census全部满足 \(R\le1\)。

但是没有 recovered post-PSDG theorem universal 强制上述 active-upper carrier inequality。

因此：

\[
\boxed{
\texttt{R\_LE\_1\_UNIVERSAL=NOT\_PROVED}.
}
\]

---

## 22. \(\lceil L\rceil\ge R\) Extinction Attempt

在 Face A，假设 continuous fibre \(G_A>0\)。

\[
\lceil L_2\rceil\ge R_3
\]

精确等价于：

\[
\boxed{
C_3\delta_2\ge G_A.
}
\]

Face B：

\[
\boxed{
C_2\delta_3\ge G_B.
}
\]

所以 Level 2 并不是新的 architecture；它恰好就是：

\[
\boxed{
\text{endpoint modular jump}
\ge
\text{radial gap}.
}
\]

目前没有 universal proof。

---

## 23. Progression Successor Attempt

generic post-PSDG profiles：

\[
h_U=1,
\]

所以 progression layer不比 plain integer layer更强。

q=1 才存在 genuine finite-index source progression：

\[
U\equiv r_{q1}\pmod{h_U}.
\]

其 AP successor：

\[
\boxed{
U_{\rm AP}
=
r_{q1}
+
h_U
\left\lceil
\frac{L-r_{q1}}{h_U}
\right\rceil
}
\]

并加 positivity / strict-lower correction。

因此 progression gate 是 chart-local source semantics，不能被错误推广成所有 post-PSDG profiles 的 hidden Smith modulus。

---

## 24. Coprime Successor Attempt

generic completed strata：

\[
\operatorname{Succ}_{\rm src}(L)
=
\min\{u\in\mathbf Z_{>0}:u\ge L,\ (u,V)=1\}.
\]

若 plain successor \(U_{\mathbf Z}\) 已经满足

\[
(U_{\mathbf Z},V)=1,
\]

则：

\[
U_{\min}=U_{\mathbf Z}.
\]

否则 source delay增加到下一个 \(V\)-unit。

R8 不启动 generic Jacobsthal round。只有当 plain/AP candidate 真正在 interval 内时，coprime delay 才有必要继续估计。

R7D canonical witness B 中：

\[
U_{\mathbf Z}=1,
\qquad
(1,24)=1,
\]

所以 coprimality 不产生额外 delay；它在更早的 integer upper endpoint 已经失败。

---

## 25. R7D Witness Regression

Witness B：

\[
L=\frac{10}{109},
\qquad
R=\frac25.
\]

\[
W_U=
\frac25-\frac{10}{109}
=
\frac{168}{545}.
\]

plain/source successor：

\[
U_{\mathbf Z}=U_{\min}=1.
\]

plain delay：

\[
D_U=
1-\frac{10}{109}
=
\frac{99}{109}.
\]

surplus：

\[
\boxed{
\sigma_U=
\frac25-1
=
-\frac35.
}
\]

Face A data：

\[
G_A
=
109\cdot10-25\cdot10
=
840,
\]

\[
\delta_2=99.
\]

因此：

\[
C_3\delta_2
=
25\cdot99
=
2475
>
840
=
G_A.
\]

精确 regression：

```text
PROFILE=R7D_CANONICAL_WITNESS
L=10/109
R=2/5
REAL_FIBRE=PASS
PLAIN_INTEGER_SUCCESSOR=1
SOURCE_SUCCESSOR=1
INTEGER_FIBRE=EMPTY
SOURCE_FIBRE=EMPTY
FINAL_RADIAL_STATUS=FAIL
```

---

## 26. Post-PSDG Family Search

本轮不重新搜索 original variables，也不重开 PSDG。

使用 frozen `105_R7D_Reduced_Witness_Registry.csv` 的四个 exact reduced PSDG hits：

\[
A,B,C,E.
\]

R8 对其重新 exact 验证：

- sphere；
- primitive；
- master；
- \(g_1\) firewall；
- Smith factorization；
- DES；
- radial endpoints；
- successor。

结果：

| State | \(I_{23}\) | Real | \(U_{\min}\) | Surplus | First failure |
|---|---|---:|---:|---:|---|
| A | \([10/13,10/53)\) | FAIL | 1 | \(-43/53\) | REAL_FIBRE |
| B | \([10/109,2/5)\) | PASS | 1 | \(-3/5\) | INTEGER_SUCCESSOR |
| C | \([10/73,10/969)\) | FAIL | 1 | \(-959/969\) | REAL_FIBRE |
| E | \([5/1257,10/297)\) | PASS | 1 | \(-287/297\) | INTEGER_SUCCESSOR |

统计：

```text
POST_PSDG_PROFILES=4
REAL_FIBRE_NONEMPTY=2
R_LE_1=4
PLAIN_INTEGER_FIBRE_NONEMPTY=0
PROGRESSION_FIBRE_NONEMPTY=0
COPRIME_FIBRE_NONEMPTY=0
FULL_RADIAL_FIBRE_NONEMPTY=0

MIN_SUCCESSOR_SURPLUS=-959/969
MAX_SUCCESSOR_SURPLUS=-3/5
FIRST_POSITIVE_SURPLUS_PROFILE=NONE
```

这不是 exhaustive family theorem。

---

## 27. Prescribed-\(U\) Reverse Construction

固定 \(U_0\in\mathbf Z_{>0}\)。

block \(i\) digit condition：

\[
10^{n_i-1}\le U_0C_i<10^{n_i}
\]

等价于 finite integer carrier interval：

\[
\boxed{
\left\lceil\frac{10^{n_i-1}}{U_0}\right\rceil
\le
C_i
\le
\left\lfloor\frac{10^{n_i}-1}{U_0}\right\rfloor.
}
\tag{REV-U}
\]

因此 prescribed-\(U\) constructive lane 的正确顺序是：

1. 固定 \(U_0\)；
2. 用 (REV-U) 限制 \(C_2,C_3\)；
3. 检查 chart progression；
4. 检查 \((U_0,V)=1\)；
5. 只在 frozen \(\mathscr P_{\rm post}\) equations 内寻找 profile。

特别 \(U_0=1\) 时：

\[
C_i
\]

本身必须是 \(n_i\)-digit positive integer。

R8 当前 exact census 中无 \(U_0=1\) hit。

---

## 28. First Integer-Radial Witness Search

在 strict R7D exact post-PSDG census：

\[
\boxed{
\texttt{INTEGER\_RADIAL\_WITNESS\_FOUND=NO}.
}
\]

不能升级为：

\[
\forall p\in\mathscr P_{\rm post},\quad
\mathcal U_{\rm src}(p)=\varnothing.
\]

因此“no hit”只归档为 evidence。

---

## 29. Downstream Digit / Actual-Cut Audit

因为本轮没有 integer-radial witness：

```text
DIGIT_SYNCHRONIZATION=NOT_REACHED
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED
```

但有一个必须保留的 semantic audit：

历史 Full Interface Equivalence 已证明，在 minimal exact terminal category 中：

\[
\text{primitive sphere}
+\text{exact master}
+\text{exact gcd profile}
+\text{denominator legality}
+\text{legal coprime integer }U
+\text{numerator digit windows}
\]

已经双向恢复 original A1 candidate。

因此若未来在真正 complete \(\mathscr P_{\rm post}\) profile 上找到 \(U\)，不得凭空制造一个新的“norm gate”或重复 actual-cut architecture；应立即执行 exact reconstruction audit。

---

## 30. New First-Failure Gate

R8 没有把 first-failure 向后推进。

它把 first-failure **规范化**为：

\[
\boxed{
\texttt{POST\_PSDG\_CANONICAL\_SOURCE\_SUCCESSOR\_INEQUALITY}.
}
\]

最强 exact form：

Face A：

\[
\boxed{
C_3
\left(
C_2\operatorname{Succ}_{\rm src}(L_2)
-
10^{n_2-1}
\right)
<
G_A.
}
\]

Face B：

\[
\boxed{
C_2
\left(
C_3\operatorname{Succ}_{\rm src}(L_3)
-
10^{n_3-1}
\right)
<
G_B.
}
\]

R9 必须证明它永远失败，或构造一个真正 success。

---

## 31. Failed / Falsified Routes

1. **“interval width < 1 就等于 empty”** — FALSE as logic；必须比较 successor delay。
2. **“Smith index \(J\) 是 \(U\)-progression modulus”** — FALSE；source transport表明 generic \(U\)-step仍为 1。
3. **“DES 直接强制某个 \(p\mid U\)”** — historical radial audit未得到该 theorem；radial homogeneity阻止直接路线。
4. **“R7D 四个 profiles 没 hit，所以 universal empty”** — INVALID inference。
5. **“q=1 也可以机械写成同一个 closed \([L,R)\)”** — FALSE；historical \(\rho>0\) 可制造 open lower boundary。
6. **“coprimality必须先于 plain integer gate研究”** — 不必要；若 plain successor已经出 upper endpoint，立即停止。
7. **“\(R\le1\) universal”** — 当前仅在 exact census 中成立，未证明。
8. **“\(\lceil L\rceil\ge R\) universal”** — 当前未证明；等价于 endpoint modular jump inequality。

---

## 32. Exact Remaining Unknowns

R8 后只剩以下真正 unknown：

1. post-PSDG frozen equations 是否能 universal 控制
   \[
   (-10^{n_i-1})\bmod C_i
   \]
   与 radial gap \(G_A/G_B\) 的相对大小？
2. 若 plain candidate 进入 interval，post-PSDG source data 是否能迫使其落在 forbidden residue / non-unit class？
3. q=1 finite-index affine lattice是否在 post-PSDG survivor上产生足够大的 successor delay？
4. 是否存在任意
   \[
   p\in\mathscr P_{\rm post}
   \]
   使
   \[
   \sigma_U>0?
   \]

所有这些现在都属于同一个 successor inequality，而不是新的顶层 architecture。

---

## 33. R8 Terminal Verdict

\[
\boxed{
\texttt{
R8\_TERMINAL\_VERDICT
=
CANONICAL\_SOURCE\_SUCCESSOR\_THEOREM\_PROVED
\_\_UNIVERSAL\_EXTINCTION\_NOT\_PROVED
\_\_NO\_INTEGER\_RADIAL\_WITNESS\_IN\_R7D\_EXACT\_CENSUS
\_\_SINGLE\_SUCCESSOR\_INEQUALITY\_REMAINS
}
}
\]

R8 的信息增益不是又一轮 generic successor theory，而是：

\[
\boxed{
\text{source-completed rank-one fibre}
\to
\text{finite residue selector}
\to
\text{canonical source successor}
\to
\text{two active-face integer gap inequalities}.
}
\]

---

## 34. R9 Authorization Decision

授权：

\[
\boxed{\texttt{R9\_AUTHORIZED=YES}}
\]

仅允许：

\[
\boxed{
\textbf{Route D — Post-PSDG Endpoint Quotient / Unit Alignment}.
}
\]

唯一 attack target：

\[
\boxed{
\operatorname{Succ}_{\rm src}(L(p))<R(p)
}
\]

或等价的 (R8-A)/(R8-B)。

禁止 R9 重开：

- discriminant；
- PSDG；
- Gaussian packet；
- Smith redesign；
- DES redesign；
- broad Jacobsthal；
- broad endpoint atlas。

---

# Machine-readable Terminal Block

```text
R8_TERMINAL_VERDICT=CANONICAL_SOURCE_SUCCESSOR_THEOREM_PROVED__UNIVERSAL_EXTINCTION_NOT_PROVED__NO_INTEGER_RADIAL_WITNESS_IN_R7D_EXACT_CENSUS__SINGLE_SUCCESSOR_INEQUALITY_REMAINS

R1_R2_R3_R4_R5_R5C_R6_R7_R7B_R7C_R7D_STATE_FROZEN=YES

POST_PSDG_PROFILE_SPACE=P_post=frozen_sphere+master+primitive+PSDG+Smith+DES+source_g1_firewall+source_completed_base

SOURCE_FIBRE_RANK=1_ON_EACH_FIXED_SOURCE_COMPLETED_PROFILE
RADIAL_VARIABLE=U

SOURCE_INTERVAL=REGULAR_I23=[max(10^(n2-1)/C2,10^(n3-1)/C3),min(10^n2/C2,10^n3/C3)); Q1_NEGATIVE_INTERSECTS_OPEN_(dq*tau*G/(10*C3),G/C3)
LOWER_ENDPOINTS=L2=10^(n2-1)/C2;L3=10^(n3-1)/C3;OPTIONAL_Q1_OPEN_L=dq*tau*G/(10*C3)
UPPER_ENDPOINTS=R2=10^n2/C2;R3=10^n3/C3;OPTIONAL_Q1_OPEN_R=G/C3
ACTIVE_LOWER=REGULAR_FACE_A:L2_IF_L2>=L3__FACE_B:L3_IF_L3>L2
ACTIVE_UPPER=REGULAR_FACE_A:R3__FACE_B:R2
L=max_active_lower_with_boundary_flag
R=min_active_upper_with_boundary_flag
WIDTH=R-L; REGULAR_FACE_A=G_A/(C2*C3); FACE_B=G_B/(C2*C3)

REAL_FIBRE_NONEMPTY=REGULAR_IFF_L<R; Q1_USES_DECORATED_ENDPOINT_POLARITY

POSITIVE_INTEGER_CRITERION=REGULAR_IFF_max(1,ceil(L))<R
PLAIN_INTEGER_SUCCESSOR=max(1,ceil(L)); FACE_A=(10^(n2-1)+delta2)/C2; FACE_B=(10^(n3-1)+delta3)/C3
PLAIN_INTEGER_FIBRE_NONEMPTY=UNKNOWN_GLOBALLY__NO_ON_R7D_4_PROFILE_EXACT_CENSUS

SOURCE_PROGRESSIONS=GENERIC:U_IN_Z; Q1:31*C3*U+dq*tau==0_mod_2*K*dq
SOURCE_LATTICE_MODULUS=GENERIC:1; Q1:h_U=2*K*dq/gcd(C3,2*K*dq)
SOURCE_RESIDUE_SET=GENERIC_UNITS_MOD_V_AFTER_COPRIMALITY; Q1_CRT_RESIDUES_MOD_lcm(h_U,V)_WITH_OPTIONAL_RHO_PERIOD_REFINEMENT

COPRIMALITY_V=gcd(U,V)=1
SOURCE_SUCCESSOR=min_over_admissible_residues[r+M_U*ceil((max(L,1)-r)/M_U)]_WITH_STRICT_LOWER_CORRECTION_WHEN_NEEDED
SOURCE_SUCCESSOR_DELAY=U_min-L

SOURCE_SUCCESSOR_SURPLUS=R-U_min=(R-L)-(U_min-L)

R7D_WITNESS_REGRESSION=PASS
R7D_L=10/109
R7D_R=2/5
R7D_SUCCESSOR=1
R7D_RADIAL_STATUS=FAIL_INTEGER_SUCCESSOR; SURPLUS=-3/5

R_LE_1_UNIVERSAL=NOT_PROVED__TRUE_ON_R7D_4_PROFILE_EXACT_CENSUS
CEIL_L_GE_R_UNIVERSAL=NOT_PROVED__TRUE_ON_R7D_4_PROFILE_EXACT_CENSUS

CANONICAL_SOURCE_SUCCESSOR_THEOREM=PROVED

INTEGER_RADIAL_WITNESS_FOUND=NO_IN_CURRENT_EXACT_POST_PSDG_CENSUS__GLOBAL_EXISTENCE_UNKNOWN
WITNESS_U=NONE
WITNESS_PROFILE=NONE

SOURCE_PROGRESSION_VALID=YES_CHARTWISE; R7D_B_GENERIC_STEP_1
COPRIMALITY_VALID=R7D_B_SUCCESSOR_1_IS_COPRIME_TO_24_BUT_OUTSIDE_INTERVAL
SOURCE_RADIAL_LIFT=NO_WITNESS_FOUND__UNIVERSAL_NO_NOT_PROVED

P1_P2_P3_Q0_FROZEN=YES
SMITH_FROZEN=YES
DES_FROZEN=YES

DIGIT_SYNCHRONIZATION=NOT_REACHED_AFTER_INTEGER_GATE; I23_ALREADY_ENCODES_BLOCK_2_3_DIGIT_WINDOWS
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

NEW_FIRST_FAILURE_GATE=POST_PSDG_CANONICAL_SOURCE_SUCCESSOR_INEQUALITY

POST_PSDG_INTEGER_RADIAL_FIBRE_EMPTY=NOT_PROVED
POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NOT_PROVED

R8_SINGLE_REMAINING_GATE=YES__Succ_src(L(p))<R(p)__EQUIV_FACE_A_C3*Jsrc2<G_A_OR_FACE_B_C2*Jsrc3<G_B

R9_AUTHORIZED=YES
R9_ARCHITECTURE=ROUTE_D__POST_PSDG_ENDPOINT_QUOTIENT_UNIT_ALIGNMENT
R9_SINGLE_ATTACK_TARGET=DECIDE_THE_EXACT_SOURCE_SUCCESSOR_GAP_INEQUALITY_ON_P_post
```

---

## Provenance / Regression Sources

本报告只读取以下 frozen historical assets 的已证明接口，不重开其 architecture：

- `105_R2_Source_Section_Internalization.md`
- `105_R2_Source_Section_Transport.csv`
- `105_R7D_Determinant_Packet_Source_GCD_Firewall.md`
- `105_R7D_Reduced_Witness_Registry.csv`
- `strict_layer_A1_primitive_conic_common_U_digit_window_campaign.md`
- `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`
- `strict_layer_A1_radial_gate_scan.py`

所有新 R8 computation 仅使用 exact integer / rational arithmetic。
