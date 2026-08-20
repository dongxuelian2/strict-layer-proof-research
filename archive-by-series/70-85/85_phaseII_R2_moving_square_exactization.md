# 第二个 85 · 第二轮
## Moving-Square Exactization × Counterexample Guillotine × Source-Compatible Representation 定型

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 第二个 85 · 第二轮 / Phase-II Central Assault  
**Global completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 1. Executive Verdict

```text
J2_STATUS = OPEN

THEOREM_A = FALSE
THEOREM_B = PLAUSIBLE
THEOREM_C = PLAUSIBLE

MOVING_INFORMATION_ACTIVATED = YES

CLASS_INTERFACE = NOT_VISIBLE
DESCENT_INTERFACE = NOT_VISIBLE

PHASE_II_ARCHITECTURE = ALIVE

DISCRIMINANT_ALONE = OLD_INFORMATION_CLASS

PHASE_II_PRIMARY_SOURCE_GATE =
SQUARE_CONDITIONED_COMMON_U_RADIAL_DIGIT_LIFT
```

本轮最重要的结论不是一个 closure theorem，而是对 theorem target 的精确校准：

\[
\boxed{
\text{ambient square representation}
\;\not\Rightarrow\;
\text{source-compatible square representation}.
}
\]

更强地，本轮构造了 live \(g=4\) exact-root countermodel，它同时通过：

- moving outer relation \(uq=10^g+1\)；
- exact root conic；
- integral source-lattice reconstruction；
- positivity；
- ten-unit package；
- regularity；
- common-\(V\) gcd profile；
- full primitive normalization；

但在第一条真正非齐次 radial source gate 上死亡：

\[
\boxed{
U_{\rm lo}=1,\qquad U_{\rm hi}=0.
}
\]

因此当前最精确的信息差是：

\[
\boxed{
\text{projective/root-conic arithmetic}
\quad\text{vs}\quad
\text{absolute decimal radial height realization}.
}
\]

这使 Phase-II 架构继续存活，但主目标必须读取 common-\(U\) 的绝对 moving digit shell；不能再退回判别式、固定模、primitive/common-\(V\) 单独攻击。

> **Scope firewall.** 本报告的 exact reverse semantics 仅对 Phase-I 已审计的 central regular \(q>1\) shell 使用。它不声称 singular \(d_A>1\) 已自动由同一 chart 全局覆盖。因此 `J2_STATUS=OPEN` 仍是全局判决。

---

# 2. Genuine Moving Form

## 2.1 Outer moving data

令

\[
G=10^g,\qquad K=10^k,\qquad H=\frac G2,
\]

\[
u\mid G+1,\qquad q=\frac{G+1}{u},
\]

\[
A=2u+1,\qquad B=2G+q.
\]

当前 fully audited central regular live scope 为

\[
g\ge4,\qquad k\ge1,\qquad \ell:=2g-k\ge6,
\]

\[
u>1,\qquad q>1,
\]

并保留 negative regular orientation 与

\[
\gcd(A,d_2)=1.
\]

## 2.2 Exact PRE_ROOT chart

取

\[
C_3=c,
\qquad
C_2=Ac+H\lambda,
\]

\[
2KC_1=Bz+A\lambda,
\qquad
T=Gz+u\lambda.
\]

派生：

\[
h=qHz-Ac,
\]

\[
m=Ah-Gz,
\]

\[
r=Hh-uc,
\]

\[
w=GHz-uAc,
\]

\[
d_2=uc+Gw.
\]

full root equation为

\[
\boxed{
H^2C_1^2+w^2-Td_2=0.
}
\tag{ROOT}
\]

固定 outer tuple 后，这与 old NRSEC 可逆仿射等价：

\[
\boxed{
AH^2C_1^2-2uKd_2C_1+Aw^2+zd_2=0.
}
\tag{NRSEC}
\]

其 \(C_1\)-判别式：

\[
\boxed{
\Delta_0
=
u^2K^2d_2^2
-
AH^2(Aw^2+zd_2).
}
\]

## 2.3 Clear the half-integral coordinates

定义

\[
\boxed{
W:=2w=G^2z-2uAc,
}
\]

\[
\boxed{
D:=2d_2=GW+2uc.
}
\]

则

\[
\boxed{
\mathscr Q_{g,k,u}(c,z)
=
4u^2K^2D^2
-
AG^2(AW^2+2zD).
}
\tag{Q}
\]

且 exact-root discriminant condition 是

\[
\boxed{
\mathscr Q_{g,k,u}(c,z)=16Y_0^2.
}
\tag{MS}
\]

为了严格匹配标准表示

\[
Q_g(X,Y)=Z^2,
\]

本报告取

\[
\boxed{
X:=c,\qquad Y:=z,\qquad Z:=4Y_0.
}
\]

于是：

\[
\boxed{
Q_{g,k,u}(X,Y)=Z^2,
}
\]

其中

\[
Q_{g,k,u}=\mathscr Q_{g,k,u}.
\]

注意：真正 canonical 的 moving object 是 \(Q_{g,k,u}\)，而不是只写 \(Q_g\)。把 \(k,u\) 隐掉会丢失

\[
K=10^k,
\qquad
uq=10^g+1
\]

所携带的 moving arithmetic。

若一定只按 \(g\) 分层，可定义：

\[
\mathcal Q_g
=
\{Q_{g,k,u}:
(k,u)\text{ admissible at }g\}.
\]

## 2.4 Binary quadratic coefficients

写成

\[
Q_{g,k,u}(c,z)
=
\alpha c^2+\beta cz+\gamma z^2.
\]

定义

\[
\boxed{
N_0
=
4u^2G^2K^2-(GA+1)^2+2.
}
\]

则：

\[
\boxed{
\alpha
=
4u^2
\left(
4K^2u^2(GA-1)^2-G^2A^4
\right),
}
\]

\[
\boxed{
\beta
=
-4G^2u
\left(
AN_0+GA^2-4GK^2u^2
\right),
}
\]

\[
\boxed{
\gamma
=
G^4(N_0-1).
}
\]

因此：

\[
\boxed{
\Delta_{g,k,u}
=
\beta^2-4\alpha\gamma
=
(4G^2uA)^2N_0.
}
\]

square class 精确为：

\[
\boxed{
[\Delta_{g,k,u}]=[N_0].
}
\]

故永久记录：

```text
DISCRIMINANT_ALONE=OLD_INFORMATION_CLASS
```

判别式本身不提供新的 Phase-II moving information。

---

# 3. Source-to-Form Logic Audit

## 3.1 哪些是 equivalent

在 fixed audited outer tuple 与 exact PRE_ROOT chart 内：

\[
\text{ROOT}
\Longleftrightarrow
\text{NRSEC}
\]

通过

\[
C_1=\frac{Bz+A\lambda}{2K},
\qquad
\lambda=\frac{2KC_1-Bz}{A}
\]

可逆。

若已知 square witness

\[
\Delta_0=Y_0^2,
\]

并存在

\[
\sigma\in\{\pm1\}
\]

使

\[
\boxed{
C_1
=
\frac{uKd_2+\sigma Y_0}{AH^2}
\in\mathbf Z_{>0},
}
\tag{REC1}
\]

且

\[
\boxed{
\lambda
=
\frac{2KC_1-Bz}{A}
\in\mathbf Z_{>0},
}
\tag{REC2}
\]

并恢复到同一 source chart，则 square + reconstruction 与 exact root 等价。

## 3.2 哪些只是 necessary

单独

\[
Q_{g,k,u}(c,z)=Z^2
\]

只是 necessary。

它没有自动编码：

- \(4\mid Z\)；
- 正确 root sign \(\sigma\)；
- \(AH^2\mid uKd_2+\sigma Z/4\)；
- \(\lambda\in\mathbf Z_{>0}\)；
- source lattice；
- primitive/common-\(V\)；
- common-\(U\)；
- digit windows。

所以禁止写：

\[
Q=\square
\Longleftrightarrow
\text{genuine source state}
\]

而不带 reconstruction predicates。

## 3.3 Division / cancellation / square extraction ledger

1. \(H=G/2\)：合法，因为 \(g\ge1\)。
2. \(w=W/2,\ d_2=D/2\)：只是清除固定二分母。
3. \(C_1=(Bz+A\lambda)/(2K)\)：需要 source lattice congruence。
4. discriminant extraction \(\Delta_0=Y_0^2\)：necessary；不能单独 reverse。
5. \(C_1=(uKd_2\pm Y_0)/(AH^2)\)：reverse 时需要 exact divisibility。
6. \(\lambda=(2KC_1-Bz)/A\)：reverse 时需要 integer + positivity。
7. projective gcd reduction：只对 ambient conic合法；**不**保持 source digit/common-\(U\) semantics。

## 3.4 Primitive/content change

\(Q\) 是 homogeneous degree \(2\)：

\[
(c,z,Z)\mapsto d(c,z,Z)
\]

保持 ambient square equation。

但 source semantics 不是 homogeneous：

\[
\frac G{10}\le Uc<G,
\qquad
\frac{G^2K}{10}\le UC_2<G^2K.
\]

因此“先除 \(\gcd(c,z)\)”只可作为 ambient/projective diagnostic，不能作为 source-equivalent normalization。

---

# 4. Exact Source-Compatible Set

由于 form 真实依赖 \((g,k,u)\)，先定义 fixed outer fibre：

\[
\boxed{
\mathcal S_{g,k,u}.
}
\]

再定义

\[
\boxed{
\mathcal S_g
=
\bigcup_{(k,u)\in\mathcal O_g}
\mathcal S_{g,k,u},
}
\]

其中 \(\mathcal O_g\) 是满足当前 audited branch 条件的 outer data。

## 4.1 B1 — Exact source conditions

\((c,z)\in\mathcal S_{g,k,u}\) 要求存在整数

\[
\lambda,\ C_1,C_2,T,h,m,r,w,d_2,U
\]

满足：

\[
c,z,\lambda\in\mathbf Z_{>0},
\]

\[
C_1=\frac{Bz+A\lambda}{2K}\in\mathbf Z_{>0},
\]

以及上述全部 exact PRE_ROOT linear identities。

要求：

\[
C_1,C_2,c,T,h,m,r,w,d_2>0.
\]

Exact Resonance / \(J=2\) outer semantics 通过当前 frozen chart 与

\[
uq=G+1
\]

保留；historical non-root master 在此 chart 上自动成立，不再增加 independent equality codimension。

## 4.2 B2 — Derived necessary conditions

由 source + exact root 可推出但不作为 source 定义的条件包括：

\[
Q_{g,k,u}(c,z)=16Y_0^2,
\]

\[
[\operatorname{disc}Q]=[N_0],
\]

以及已冻结的若干 root-derived gcd / support consequences。

这些条件不能反过来替代 source image。

## 4.3 B3 — Primitive / common-scale

要求 ten-unit：

\[
\boxed{
\gcd(cz\lambda,10)=1,
}
\]

\[
\boxed{
\gcd(hmrwTd_2,10)=1.
}
\]

令

\[
V=uGH.
\]

common-\(V\) profile：

\[
\boxed{
\gcd(C_1,u)=1,
}
\]

\[
\boxed{
\gcd(C_2,H)=1,
}
\]

\[
\boxed{
\gcd(c,GH)=1.
}
\]

令

\[
P_1=GHC_1,
\qquad
P_2=uGC_2,
\qquad
P_3=uc,
\qquad
Q_0=P_2+d_2.
\]

full primitive normalization：

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

## 4.4 B4 — Decimal-moving conditions

定义：

\[
\boxed{
U_{\rm lo}
=
\max\left(
\left\lceil\frac{G^2K}{10C_2}\right\rceil,
\left\lceil\frac G{10c}\right\rceil,
1
\right),
}
\]

\[
\boxed{
U_{\rm hi}
=
\min\left(
\left\lfloor\frac{G^2K-1}{C_2}\right\rfloor,
\left\lfloor\frac{G-1}{c}\right\rfloor
\right).
}
\]

要求：

\[
\boxed{
\exists U\in[U_{\rm lo},U_{\rm hi}]
\cap\mathbf Z_{>0}
:
\gcd(U,uGH)=1.
}
\tag{SRC-U}
\]

它精确编码：

\[
\frac{G^2K}{10}\le UC_2<G^2K,
\]

\[
\frac G{10}\le Uc<G.
\]

这是真正非齐次、读取 \(10^g\) 绝对大小而非仅模类的 moving datum。

## 4.5 \(\mathcal S_{g,k,u}\) 相比 ambient \(\mathbf Z^2\) 薄在哪里

ambient conic/projective layer拥有 homogeneous scaling freedom。

source image 依次施加：

1. source lattice congruence；
2. positivity / orientation cone；
3. ten-unit / gcd reducedness；
4. full primitive normalization；
5. **absolute radial digit-height interval**；
6. 同一个 \(U\) 对 block 2、3 同时实现；
7. \(\gcd(U,uGH)=1\)。

其中前四类仍主要是 projective / arithmetic restrictions；第五、六类直接破坏 projective invariance。

本轮 countermodel differential 显示：

\[
\boxed{
\text{在已找到的最深 exact-root countermodels 上，
前四层可以全部修复，
第五/六层首先失败。}
}
\]

---

# 5. A/B/C Theorem Ladder

本报告严格按本轮 prompt 的 A/B/C 命名，不沿用旧 R11 文件中曾使用的字母顺序。

## 5.1 Theorem A — Ambient Primitive Nonrepresentation

### Statement

对 admissible moving outer data，若

\[
c,z>0,\qquad \gcd(c,z)=1,
\]

则

\[
Q_{g,k,u}(c,z)=Z^2
\]

无解。

### Verdict

```text
THEOREM_A=FALSE
```

不仅旧 R10 已有 ambient/root-compatible live counterexample，本轮还得到一个更强 live counterexample：

- \(g=4,k=1,u=73,q=137\)；
- \(\gcd(c,z)=1\)；
- exact root；
- common-\(V\)；
- full primitive；
- regular；
- ten-unit；

全部通过。

因此 ambient / primitive ambient theorem 永久退出。

---

## 5.2 Theorem B — Intermediate Restricted Nonrepresentation

为避免人为选择一个过弱的 B，本轮把 \(\mathcal P_{g,k,u}\) 定义成**尽可能接近 source、同时确实比 full source 少一层**的 reduced set。

\(\mathcal P_{g,k,u}\) 要求：

- live moving outer data；
- square equation；
- exact positive integral root/source-lattice reconstruction；
- source positivity/orientation；
- ten-unit package；
- regularity；
- common-\(V\) reducedness；
- exact common-\(U\) digit realization；

但**不要求 full primitive tuple**

\[
\gcd(P_1,P_2,P_3,Q_0)=1.
\]

因此：

\[
\boxed{
\mathcal S_{g,k,u}\subseteq\mathcal P_{g,k,u}.
}
\]

Theorem B 为：

\[
\boxed{
(c,z)\in\mathcal P_{g,k,u}
\Longrightarrow
Q_{g,k,u}(c,z)\notin\square.
}
\]

### Verdict

```text
THEOREM_B=PLAUSIBLE
```

本轮没有找到 B-counterexample。

注意：本轮新 live countermodel **不能**杀 B，因为它恰恰死在 common-\(U\)；把 B 偷换成“不含 common-\(U\)”再宣布 B false 会违背本轮对 intermediate primitive/common-scale theorem 的要求。

---

## 5.3 Theorem C — Full Source-Compatible Nonrepresentation

\[
\boxed{
(c,z)\in\mathcal S_{g,k,u},
\qquad
Q_{g,k,u}(c,z)=Z^2
\Longrightarrow\bot.
}
\]

等价地：

\[
\boxed{
Q_{g,k,u}(\mathcal S_{g,k,u})
\cap\square
=
\varnothing.
}
\]

### Verdict

```text
THEOREM_C=PLAUSIBLE
```

没有 genuine full source-compatible square representation 被构造。

C 仍是 Phase-II 最终有效 theorem target。

---

# 6. Counterexample Guillotine

## 6.1 Counterexample 0 — inherited live ambient/root-compatible point

Outer data：

\[
(g,k,u,q)=(4,1,73,137).
\]

旧 R10 point：

\[
c=
44166648285459361797000000,
\]

\[
z=
9530621959721527629285,
\]

\[
\lambda=
84945551173868016406925.
\]

它位于 exact root conic 且满足 outer moving relation，但：

\[
\gcd(C_1,u)=73,
\]

\[
\gcd(C_2,H)=5000,
\]

并且：

\[
U_{\rm lo}=1,\quad U_{\rm hi}=0.
\]

所以它同时死于 primitive/common-\(V\) 与 radial digit lift。

---

## 6.2 Counterexample 1 — 本轮新 live deep countermodel

固定：

\[
G=10000,\quad K=10,\quad
u=73,\quad q=137,
\]

\[
A=147,\quad B=20137,\quad H=5000.
\]

取：

\[
\boxed{
c=
33924239254903883018463510772486609118378145469,
}
\]

\[
\boxed{
z=
7320435422750314882891089365044594394569109,
}
\]

\[
\boxed{
\lambda=
65244544113530337755581044004304642533979621.
}
\]

则：

\[
C_1=
7850127804630602522342414000626788988796657611,
\]

\[
C_2=
5313085891038522492492041303577054753071485488943,
\]

\[
T=
77967205947790863485068309862760182850671602333,
\]

\[
h=
27635094113094891066260131500015619878252281057,
\]

\[
m=
3989154480397445837911328436851850178157394225379,
\]

\[
r=
135699001099866471870952821213686576925619800665763,
\]

\[
w=
1980759693142175473422534152675917279139570972161,
\]

\[
d_2=
19810073400887362717685689363045564313861351326229237.
\]

exact root：

\[
\boxed{
H^2C_1^2+w^2-Td_2=0.
}
\]

square witness：

\[
Y_0=
14387866099369689485697818217280187584708930252277656990,
\]

\[
\boxed{
Z=4Y_0
=
57551464397478757942791272869120750338835721009110627960.
}
\]

于是：

\[
\boxed{
Q_{4,1,73}(c,z)=Z^2.
}
\]

且 root reconstruction 使用 \(\sigma=+1\)：

\[
\boxed{
C_1=
\frac{uKd_2+Y_0}{AH^2}.
}
\]

### Source-Compatibility Ledger

| Gate | Status |
|---|---|
| \(uq=10^g+1\) | PASS |
| \(Q(c,z)=Z^2\) | PASS |
| exact full root | PASS |
| source lattice \(2K\mid Bz+A\lambda\) | PASS |
| \(c,z,\lambda>0\) | PASS |
| all derived positivity | PASS |
| \(\gcd(cz\lambda,10)=1\) | PASS |
| \(\gcd(hmrwTd_2,10)=1\) | PASS |
| regular \(\gcd(A,d_2)=1\) | PASS |
| \(\gcd(C_1,u)=1\) | PASS |
| \(\gcd(C_2,H)=1\) | PASS |
| \(\gcd(c,GH)=1\) | PASS |
| full primitive tuple gcd | PASS |
| common-\(U\) interval nonempty | **FAIL** |
| full pre-root/source lift | FAIL at common-\(U\) only |

full primitive blocks：

\[
P_1=
392506390231530126117120700031339449439832880550000000,
\]

\[
P_2=
3878552700458121419519190151611249969742184406928390000,
\]

\[
P_3=
2476469465607983460347836286391522465641604619237,
\]

\[
Q_0=
3898362773859008782236875840974295534056045758254619237,
\]

并且：

\[
\boxed{
\gcd(P_1,P_2,P_3,Q_0)=1.
}
\]

但：

\[
\boxed{
U_{\rm lo}=1,\qquad U_{\rm hi}=0.
}
\]

更细地：

\[
U_{\rm hi}^{(2)}=0,
\qquad
U_{\rm hi}^{(3)}=0.
\]

即第二、第三 actual block upper bounds 都已经失败。

---

# 7. How Counterexample 1 Was Found

## 7.1 Exact conic parameterization

固定 outer data 后定义 integral homogeneous conic polynomial：

\[
\Phi(c,z,\lambda)
=
G^2(Bz+A\lambda)^2
+
16K^2w^2
-
16K^2Td_2.
\]

则：

\[
\boxed{
\Phi=16K^2\cdot
(H^2C_1^2+w^2-Td_2).
}
\]

已知一个 isotropic point \(p\) 后，对任意向量 \(y\)，令 polar form

\[
\mathcal B_\Phi(p,y)
=
\Phi(p+y)-\Phi(p)-\Phi(y).
\]

则 chord/Veronese identity 给：

\[
\boxed{
P(y)
=
\Phi(y)p-\mathcal B_\Phi(p,y)y,
}
\]

满足：

\[
\boxed{
\Phi(P(y))=0.
}
\]

因此 ambient exact-root points 并不稀缺；它们位于一条 rational conic 上。

## 7.2 Tangent/source-lattice direction

使用旧 live point

\[
p=
(44166648285459361797000000,\,
9530621959721527629285,\,
84945551173868016406925)
\]

并找到 source-lattice tangent vector：

\[
\boxed{
t_0=
(
23670799965621880000,\,
5106933501050287,\,
20440414109336223
).
}
\]

它满足：

\[
\mathcal B_\Phi(p,t_0)=0
\]

以及

\[
B(t_0)_z+A(t_0)_\lambda
\equiv0\pmod{2K}.
\]

新 witness 由：

\[
M=40,
\]

\[
e=(-5,0,-40),
\]

\[
y=Mt_0+e
\]

代入 \(P(y)\)，再做 projective gcd reduction 得到。

## 7.3 Deterministic guillotine diagnostic

执行有限 exact scan：

\[
1\le M\le80,
\]

\[
(e_c,e_z,e_r)\in[-5,5]^3\setminus\{0\},
\]

取 source-lattice preserving perturbation：

\[
e=
(e_c,e_z,9e_z+20e_r).
\]

结果：

```text
UNIQUE_EXACT_ROOT_POINTS = 100348
PASS_THROUGH_COMMON_V_TENUNIT_REGULAR = 36
PASS_FULL_PRIMITIVE = 36
PASS_COMMON_U = 0
```

所有判定均为 exact integer arithmetic。

这不是无穷族证明，也不能把 `PASS_COMMON_U=0` 升格为 Theorem B/C。

它的合法用途只有两个：

1. counterexample guillotine；
2. failure differential。

---

# 8. Source-Freedom Differential

旧 R10 live root point failure set：

\[
\mathfrak F_{\rm old}
=
\{
\text{common-}V,
\text{primitive-type},
\text{common-}U
\}.
\]

本轮新 deep countermodel：

\[
\mathfrak F_{\rm new}
=
\{
\text{common-}U\text{ radial digit lift}
\}.
\]

因此本轮真正完成了：

\[
\boxed{
\mathfrak F_{\rm old}
\longrightarrow
\mathfrak F_{\rm new}
}
\]

并严格修复了：

- \(\gcd(C_1,u)\)；
- \(\gcd(C_2,H)\)；
- \(\gcd(c,GH)\)；
- full primitive tuple gcd；
- ten-unit；
- regularity；

同时保持：

\[
Q=\square
\]

和 exact root。

所以：

```text
PHASE_II_PRIMARY_SOURCE_GATE =
SQUARE_CONDITIONED_COMMON_U_RADIAL_DIGIT_LIFT
```

这里必须强调：

\[
\boxed{
\text{common-}U\text{ alone 不是新 obstruction}.
}
\]

R7 已证明 PRE_ROOT common-scale + coprimality 可以很大。

新对象是：

\[
\boxed{
\text{EXACT SQUARE/ROOT CONIC}
\cap
\text{PRIMITIVE SOURCE RAY}
\cap
\text{MOVING RADIAL DIGIT INTERVAL}.
}
\]

---

# 9. Why Ambient Square Representation Is Rich

Theorem A 的失败不是偶然小数值现象。

固定一个 rational isotropic point 后，\(\Phi=0\) 是 rational conic。

chord/Veronese 参数化给出：

\[
\mathbb P^1(\mathbb Q)
\dashrightarrow
\{\Phi=0\}.
\]

因此 ambient level 的 rational points 具有一维参数自由。

清分母后可得到 integral representatives。

这解释了：

\[
\boxed{
\text{ambient representation 丰富}.
}
\]

而 source shell 要求绝对 radial scale：

\[
Uc\asymp G,
\qquad
UC_2\asymp G^2K,
\]

并要求同一个 \(U\) 同时满足两块窗口和 coprimality。

这不是 projective invariant。

因此：

\[
\boxed{
\text{ambient conic orbit}
\setminus
\text{source image}
}
\]

可以非常大。

这也解释了为何 naive small-box projective scan 可能给出“0 square”却不能作为强证明信号：positive/source-relevant branch 可以位于一个极窄的 rational sector，而 tangent-directed parameterization 能直接进入该 sector。

---

# 10. Moving Information Audit

## 10.1 Fixed-fibre / old information

以下属于 old/fixed-fibre class：

- fixed outer conic；
- NRSEC；
- discriminant square class；
- \(N_0\)；
- ordinary binary quadratic form class；
- fixed \(2^a5^b\) residue behavior。

特别：

\[
[\Delta]=[N_0]
\]

不能算 Phase-II 新 moving information。

## 10.2 Genuine moving-family information

当前最强候选 obstruction 真实读取：

\[
G=10^g,
\qquad
K=10^k,
\qquad
uq=G+1,
\]

以及 absolute endpoints：

\[
G-1,
\qquad
G^2K-1.
\]

具体通过：

\[
U_{\rm hi}
=
\min
\left(
\left\lfloor\frac{G^2K-1}{C_2}\right\rfloor,
\left\lfloor\frac{G-1}{c}\right\rfloor
\right).
\]

这不是固定模类，也不是 discriminant square class。

因此：

```text
MOVING_INFORMATION_ACTIVATED=YES
```

当前 candidate obstruction 读取的 moving datum 是：

\[
\boxed{
\text{power-of-ten absolute digit-height shell}.
}
\]

---

# 11. Class / Descent Readiness Audit

## 11.1 Class interface

形式上 \(Q_{g,k,u}\) 当然有 binary-form / quadratic-order class language。

但本轮没有得到任何新的 source-labelled implication：

\[
[Q]\in2\operatorname{Cl}(\Delta),
\]

\[
[Q]^2=1,
\]

或 forbidden principal/ambiguous/genus state。

反而：

\[
[\Delta]=[N_0]
\]

精确退化为旧信息。

而 class equivalence 不保持 common-\(U\) absolute digit shell。

因此：

```text
CLASS_INTERFACE=NOT_VISIBLE
```

这里的 `NOT_VISIBLE` 指 **source-compatible new interface**；不是说 classical class group 不存在。

## 11.2 Descent interface

本轮 chord map 是参数化，不是 descent。

没有构造：

\[
(g,c,z,\lambda)
\mapsto
(g',c',z',\lambda')
\]

满足：

- source-compatible；
- \(g'<g\) 或 natural height 严格下降；
- digit/common-\(U\) 保持。

因此：

```text
DESCENT_INTERFACE=NOT_VISIBLE
```

---

# 12. Counterexample Table

| Witness | Live outer? | Square/root | common-\(V\) | full primitive | common-\(U\) | Role |
|---|---:|---:|---:|---:|---:|---|
| old R10 huge point | YES | PASS | FAIL | not source-valid | FAIL | kills ambient / outer-only theorem |
| relaxed \(g=1\) R11 point | NO live \(g\ge4\) | PASS | basic PASS | diagnostic | FAIL | shows primitive-type not ambient universal killer |
| new tangent witness | **YES** | **PASS** | **PASS** | **PASS** | **FAIL** | isolates radial digit gate |
| 100348-point tangent scan | YES fixed fibre | exact-root family | 36 PASS | 36 PASS | 0 PASS | falsification audit only |

---

# 13. What Is and Is Not Killed

Permanently killed：

\[
\boxed{
\text{Ambient nonrepresentation}.
}
\]

本轮新数据进一步 kills：

\[
\boxed{
\text{Square + root + primitive/common-}V
\Longrightarrow\bot
}
\]

作为一个过强 theorem。

也就是说，若定义一个“pre-B” theorem，省略 common-\(U\) radial digit lift，则它是 FALSE。

但本轮**不能**宣布 prompt-defined Theorem B false，因为 B 被要求保留 common-scale/moving restrictions。

因此正确 ladder 是：

```text
A = FALSE
B = PLAUSIBLE
C = PLAUSIBLE
```

---

# 14. Phase-II Primary Candidate — ONE theorem only

下一轮只攻击：

\[
\boxed{
\textbf{Square-Conditioned Common-}U\textbf{ Radial Extinction Theorem}.
}
\]

精确 statement：

> 对所有当前 audited central regular \(q>1\) live outer data，设
> \[
> Q_{g,k,u}(c,z)=16Y_0^2
> \]
> 且存在正 integral root/source-lattice reconstruction，并满足 source positivity、ten-unit、regularity 与 common-\(V\) reducedness。则
> \[
> \boxed{
> [U_{\rm lo},U_{\rm hi}]
> \cap
> \{U\in\mathbf Z_{>0}:\gcd(U,uGH)=1\}
> =
> \varnothing.
> }
> \]

这是唯一 primary theorem。

若它为真，则直接证明 Theorem B，从而推出 full-source Theorem C 在 audited regular shell 成立。

若它为假，必须立即把 counterexample 推到 full primitive tuple；若 full primitive 也通过，则继续到 genuine full source reconstruction，不允许补丁式更换 theorem。

当前新 countermodels 显示一个可能的 **mechanism candidate**：

\[
c\ge G
\quad\text{或}\quad
C_2\ge G^2K
\Longrightarrow
U_{\rm hi}=0.
\]

但本轮**不把**

\[
\text{exact root + common-}V\Longrightarrow c\ge G
\]

升级成 theorem；它尚未通过 counterexample guillotine。

---

# 15. Final Answer to the Core Question

本轮问题是：

\[
\boxed{
\text{在真正的 }J=2\text{ source image 中，
square representation 第一次在哪里失效？}
}
\]

当前最强、最诚实的回答是：

\[
\boxed{
\textbf{我们还没有证明所有 genuine source states 都在同一处失效。}
}
\]

但 countermodel differential 已把已知失败点从：

\[
\text{primitive/common-}V
+
\text{digit/common-}U
\]

严格推进为：

\[
\boxed{
\textbf{common-}U\textbf{ radial digit lift alone}.
}
\]

因此当前第一条被反复观察到、且在更深 exact-root states 上仍无法修复的 genuine source gate 是：

\[
\boxed{
\exists U
\text{ simultaneously realizing block 2 and block 3
inside their moving decimal height windows}.
}
\]

这就是第二个 85 下一轮唯一值得中央攻击的接口。

---

# 16. Provenance / Freeze Anchors

本轮恢复与核验主要依赖以下 frozen artifacts：

- `85_R9_Joint_FullRoot_x_ExactSource_Incidence_Central_Assault.md`
- `85_R10_MovingBase_Globalization_and_Gamma10_Activation_Audit.md`
- `85_R11_R1_R10_Full_Architecture_Autopsy_and_PhaseI_Freeze.md`
- `85_R11_PhaseII_Moving_Square_Theorem_and_Launch_Plan.md`
- `85_R7_J2_Endpoint_Modular_Jump_and_CommonScale_Integer_Extinction.md`
- `J2-65-R13-Radial-Lattice-Ray-Report.md`
- `00_65_terminal_recompression.md`
- `7_15_Audit_Report.md`

No new external theorem is promoted.

```text
NEW_MIGRATION_CARDS = NONE
```

---

# 17. Artifact Audit

Generated with this report:

```text
85_phaseII_R2_moving_square_exactization.md
85_phaseII_R2_counterexample_certificate.py
85_phaseII_R2_counterexample_certificate.txt
```

The certificate verifies the displayed live deep countermodel by exact integer arithmetic.

FINAL_REPORT_FILE: 85_phaseII_R2_moving_square_exactization.md
