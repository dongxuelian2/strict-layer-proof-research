# 第二个八五计划·第四轮
## Uniform Two-Prime Primitive-Content Height Transfer × Full-Primitive Residue Filtering × Archimedean Packet Separation

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Round:** 第二个八五计划·R4  
**Frozen inputs:** R1–R3  
**Global completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 0. Executive Verdict

本轮**没有关闭 \(J=2\)**，也**没有构造出 full-primitive small-height countermodel**。

但 R4 得到了三个可以冻结的新结论。

第一，R3 的 “necessary \(2/5\)-residue packet” 可以进一步 exact 化。对 R3 的五个 \(g=5\) live fibres，完整 PCS valuation equality 会删除所有零余数分支，最终每个 fibre **只剩一个 affine projective packet**：

\[
\boxed{a\equiv r b\pmod M,\qquad (b,10)=1.}
\]

第二，**Full-Primitive Packet Guillotine 是假的。**  
同一个 exact PCS packet 内既存在
\[
\gcd(C_1,u)>1
\]
的 near-countermodel，也存在
\[
\gcd(C_1,u)=1,\qquad
\gcd(P_1,P_2,P_3,Q_0)=1
\]
的 full-primitive survivor。因此 full primitive 不是“删除整个 \(2^e5^f\)-packet”的规则，而是 packet 内部的额外 odd/content state。

第三，primitive decontent 得到一个新的 exact chord-content bound。若 source-basis chord parameterization 写成

\[
F(a,b)
=
Q(a,b)p-L(a,b)(a,b,0),
\]

即

\[
F_1=Qp_1-La,\qquad
F_2=Qp_2-Lb,\qquad
F_3=Qp_3,
\]

且 \((a,b)=1\)，则

\[
\boxed{
D_\Lambda(a,b)
\mid
|p_3|\gcd(Q(a,b),L(a,b)).
}
\tag{R4-CONT}
\]

所以在**固定 fibre** 上，decontent 不可能无限以 quadratic scale 吞掉 parameter height。真正仍未解决的是 moving constant：

\[
|p_3|\times
\operatorname{Res}(Q,L)
\]

怎样随 \(G,K,u,q\) 统一增长。

因此本轮的严格终点是：

\[
\boxed{\textbf{UNIFORMIZATION REQUIRED}.}
\]

不是 closure，也不是 architecture-killing small-height countermodel。

---

# 1. R1–R3 Frozen Verdicts

以下全部冻结，不重新打开：

```text
THEOREM_A = FALSE
DISCRIMINANT_ALONE = OLD_INFORMATION_CLASS
CLASS_INTERFACE = NOT_VISIBLE
DESCENT_INTERFACE = NOT_VISIBLE

REAL_RADIAL_INCOMPATIBILITY = FALSE
```

R2 的 real radial theorem：

\[
\boxed{
I_2\cap I_3\neq\varnothing
\iff
\frac1{10}<\rho<10,
}
\qquad
\rho=\frac{C_2}{GKc}.
\]

R3 的唯一 surviving height target：

\[
\boxed{
\mathfrak H_{\rm rad}
=
\max\left(\frac cG,\frac{C_2}{G^2K}\right)
\ge1\ ?
}
\]

以及 R3-PCS：

\[
\boxed{
p\nmid c_0z_0\lambda_0
\iff
v_p(X)=v_p(Y)=
\min(v_p(X),v_p(Y),v_p(N)),
\quad p=2,5.
}
\tag{PCS}
\]

---

# 2. R3 Exact Parameter Model Restored

固定

\[
G=10^g,\qquad K=10^k,\qquad H=\frac G2,
\]

\[
uq=G+1,\qquad
A=2u+1,\qquad
B=2G+q.
\]

定义

\[
C_2=Ac+H\lambda,
\qquad
2KC_1=Bz+A\lambda,
\]

\[
T=Gz+u\lambda,
\quad
h=qHz-Ac,
\quad
m=Ah-Gz,
\]

\[
r=Hh-uc,
\quad
w=GHz-uAc,
\quad
d_2=uc+Gw.
\]

exact root 为

\[
H^2C_1^2+w^2-Td_2=0.
\]

清分母后：

\[
\boxed{
\Phi(c,z,\lambda)
=
G^2(Bz+A\lambda)^2
+16K^2w^2
-16K^2Td_2
=0.
}
\tag{2.1}
\]

source lattice：

\[
r_0\equiv-A^{-1}B\pmod{2K},
\]

\[
\boxed{
(c,z,\lambda)
=
(x,y,r_0y+2Kn).
}
\tag{2.2}
\]

source basis：

\[
e_1=(1,0,0),\quad
e_2=(0,1,r_0),\quad
e_3=(0,0,2K).
\]

令 \(Q_\Lambda\) 为 \(\Phi\) 拉回该 basis 后的 integral ternary quadratic form。取 integral isotropic basepoint

\[
p=(p_1,p_2,p_3),
\qquad
Q_\Lambda(p)=0,
\]

以及 transverse plane

\[
y(a,b)=(a,b,0).
\]

令

\[
Q(a,b):=Q_\Lambda(a,b,0),
\]

\[
L(a,b):=
\mathcal B_{Q_\Lambda}(p,(a,b,0)).
\]

则 R3 chord map 在 source basis 中精确为

\[
\boxed{
\begin{aligned}
F_1(a,b)&=Q(a,b)p_1-L(a,b)a,\\
F_2(a,b)&=Q(a,b)p_2-L(a,b)b,\\
F_3(a,b)&=Q(a,b)p_3.
\end{aligned}}
\tag{2.3}
\]

标准坐标恢复：

\[
\boxed{
c=F_1,\qquad
z=F_2,\qquad
\lambda=r_0F_2+2KF_3.
}
\tag{2.4}
\]

因此：

- \(F_i\) 全部 degree \(2\)；
- \(Q\) degree \(2\)；
- \(L\) degree \(1\)；
- \((a,b)\sim(-a,-b)\)；
- \((a,b)=(0,0)\) 被排除；
- five-\(g=5\) charts 均由 R3 certificate exact 验证 transverse / isotropic / source-compatible。

primitive source-basis content：

\[
\boxed{
D_\Lambda(a,b)=\gcd(F_1,F_2,F_3).
}
\tag{2.5}
\]

primitive source ray：

\[
\boxed{
(c_0,z_0,\lambda_0)
=
\frac1{D_\Lambda}
(F_1,F_2,r_0F_2+2KF_3),
}
\tag{2.6}
\]

再固定 \(c_0>0\) 的 orientation。

---

# 3. PCS Exactization: R3 Necessary Packets \(\to\) Exact Packets

R3 只列出了“为了让 \(Y,N\) 至少达到 \(X\) 的 coefficient depth”所得 necessary packets。

R4 进一步使用完整 PCS equality：

\[
v_p(X)=v_p(Y)=\min(v_p(X),v_p(Y),v_p(N)).
\]

对五个 \(g=5\) fibres 得到：

| fibre \((g,k,u,q)\) | \(p=2\) necessary | exact PCS\(_2\) | \(p=5\) necessary | exact PCS\(_5\) |
|---|---|---|---|---|
| \((5,1,11,9091)\) | \(0,3\bmod16\) | \(3\bmod16\) | \(0,957\bmod3125\) | \(957\bmod3125\) |
| \((5,3,11,9091)\) | \(0,11\bmod16\) | \(11\bmod16\) | \(0,1727\bmod3125\) | \(1727\bmod3125\) |
| \((5,4,11,9091)\) | \(0,11\bmod16\) | \(11\bmod16\) | \(0,2227\bmod3125\) | \(2227\bmod3125\) |
| \((5,1,9091,11)\) | \(0,3\bmod16\) | \(3\bmod16\) | \(0,1352\bmod3125\) | \(1352\bmod3125\) |
| \((5,3,9091,11)\) | \(0,3\bmod16\) | \(3\bmod16\) | \(14722\bmod15625\) | \(14722\bmod15625\) |

零余数 branch 的失败不是数值偶然：在该 residue class 上 \(X/p^e\) 仍为 \(0\bmod p\)，而 \(Y/p^e\) 已是 unit，故

\[
v_p(X)>e=v_p(Y),
\]

直接违反 PCS equality。

同时 exact projective enumeration 没有产生 \(p\mid b\) 的 surviving branch。故在这五个 fibres 中：

\[
\boxed{(b,10)=1.}
\]

---

# 4. CRT / Projective Residue Packets

CRT 合并后：

| fibre | exact packet |
|---|---|
| \((5,1,11,9091)\) | \(\boxed{a\equiv44707b\pmod{50000}}\) |
| \((5,3,11,9091)\) | \(\boxed{a\equiv39227b\pmod{50000}}\) |
| \((5,4,11,9091)\) | \(\boxed{a\equiv27227b\pmod{50000}}\) |
| \((5,1,9091,11)\) | \(\boxed{a\equiv48227b\pmod{50000}}\) |
| \((5,3,9091,11)\) | \(\boxed{a\equiv155347b\pmod{250000}}\) |

所以对这五个 fibres：

\[
\boxed{s=1}
\]

即每个 fibre 只有一个 complete PCS packet。

但：

\[
\boxed{
M\text{ 并不 uniform across fibres}.
}
\]

当前 \(M\) 由真实 coefficient depths \(e_2,e_5\) 决定；尚无 all-\(g\) theorem 把 \(e_2,e_5\) 写成统一的 \(g,k,u,q\) 公式。

因此：

```text
PCS_PACKET_COMPLETE_ON_R3_G5_CORPUS = YES
PCS_PACKET_UNIFORM_ALL_G = NOT_PROVED
DENOMINATOR_DIVISIBLE_BRANCH_ON_R3_G5_CORPUS = NONE
```

projective congruence 是 invariant object；affine \(a/b\) 表示在这里合法，因为 \(b\) 是 \(2,5\)-unit。

---

# 5. Full-Primitive Filtering Pulled Back to \((a,b)\)

所有 source-derived linear quantity在 raw chord vector 上都是 binary quadratic form。

例如设 raw form 为

\[
\mathcal C_1(a,b),
\]

则 primitive 后

\[
C_{1,0}
=
\frac{\mathcal C_1(a,b)}{D_\Lambda(a,b)}.
\]

因此对 \(p\mid u\)：

\[
\boxed{
p\nmid C_{1,0}
\iff
v_p(\mathcal C_1(a,b))
=
v_p(D_\Lambda(a,b)).
}
\tag{5.1}
\]

同理：

\[
p\nmid C_{2,0}
\iff
v_p(\mathcal C_2)=v_p(D_\Lambda)
\quad (p\mid H),
\]

以及 full block condition：

\[
\boxed{
\min_i v_p(\mathcal P_i/D_\Lambda)=0
}
\]

对每个 prime \(p\) 成立，其中 \(\mathcal P_i\) 是 raw block forms。

这说明 full primitive 的自然 pullback 不是单纯的

\[
m\bmod 2^e5^f.
\]

而是：

\[
\boxed{
\text{PCS packet}
+
\text{odd/source-content valuation state}.
}
\]

---

# 6. Near-Countermodel Differential: First-Hit \(u\)-Pollution

R3-TU1：

\[
(5,1,11,9091),
\qquad
(a,b)=(224277651577,11411)
\]

不仅是一个 PCS-compatible example；R4 certificate 证明它实际上是该 exact PCS packet 与 radial band 中 **最小 reduced denominator** 的 rational。

其：

\[
D_\Lambda=80000000,
\]

并且：

\[
\gcd(C_1,11)=11,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=11.
\]

R3-TU2：

\[
(5,3,11,9091),
\qquad
(a,b)=(5982784950483,302729)
\]

同样是该 fibre 的 exact first admissible PCS-band rational，并且：

\[
D_\Lambda=800000000000,
\]

\[
\gcd(C_1,11)=11,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=11.
\]

更强地，在五个代表 fibres 的**第一个** PCS-band rational 上，全部出现：

\[
\boxed{
\gcd(C_1,u)=u,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=u.
}
\tag{6.1}
\]

这说明 R3 near-countermodels 的 failure 不是随便选点造成的；它们正落在 packet-band 的第一批 arithmetic hits 上。

但是这一污染**不是整个 packet 的 theorem**。

---

# 7. Full-Primitive Packet Guillotine: Exact Falsification

考察 fibre：

\[
(g,k,u,q)=(5,3,11,9091).
\]

exact PCS packet：

\[
\boxed{
a\equiv39227b\pmod{50000}.
}
\]

R3-TU2：

\[
(a,b)=(5982784950483,302729)
\]

在该 packet 中，且 full primitive FAIL：

\[
v_{11}(D_\Lambda)=0,
\qquad
v_{11}(\mathcal C_1)=1.
\]

但同一个 packet 中存在：

\[
\boxed{
(a,b)=(6300650477551,318813),
}
\tag{7.1}
\]

满足：

- exact root；
- source lattice；
- positive branch；
- radial band；
- PCS\(_2\)；
- PCS\(_5\)；
- raw/derived ten-unit；
- regular；
- common-\(V\)；
- full primitive。

这里：

\[
v_{11}(D_\Lambda)=3,
\qquad
v_{11}(\mathcal C_1)=3,
\]

所以 primitive decontent 后：

\[
11\nmid C_1.
\]

因此同一个 \((r,M)\)-packet 内同时有：

\[
\boxed{\text{FULL PRIMITIVE FAIL}}
\]

和：

\[
\boxed{\text{FULL PRIMITIVE PASS}}.
\]

严格得到：

\[
\boxed{
\texttt{FULL\_PRIMITIVE\_PACKET\_GUILLOTINE=FALSE}.
}
\tag{7.2}
\]

于是 R3 near-countermodel cause 的最佳分类是：

\[
\boxed{\textbf{MIXED}.}
\]

“first-hit pollution” 很强，但不是 whole-packet structural deletion。

---

# 8. Exact Band Interval at Slope Level

令 primitive coefficient forms 中：

\[
f_c(a,b)=F_1(a,b),
\]

\[
f_{C_2}(a,b)
=
A f_c(a,b)
+
H\bigl(r_0F_2(a,b)+2KF_3(a,b)\bigr).
\]

band：

\[
\frac1{10}<\frac{C_2}{GKc}<10
\]

在 projective parameter中等价于：

\[
\boxed{
P_{10}(a,b):=
10GK f_c-f_{C_2}>0,
}
\tag{8.1}
\]

\[
\boxed{
P_{01}(a,b):=
10f_{C_2}-GKf_c>0.
}
\tag{8.2}
\]

令 \(x=a/b\)。在五个 R3 live \(g=5\) charts 中，positive source branch 上的 band 是一个 interval：

\[
\boxed{\alpha<x<\beta}
\]

其中：

- \(\alpha\) 是 \(P_{10}(x,1)=0\) 的正根（\(\rho=10\) boundary）；
- \(\beta\) 是 \(P_{01}(x,1)=0\) 的正根（\(\rho=1/10\) boundary）。

若

\[
P_{10}(x,1)=A_{10}x^2+B_{10}x+C_{10},
\]

\[
P_{01}(x,1)=A_{01}x^2+B_{01}x+C_{01},
\]

则 exact：

\[
\boxed{
\alpha=
\frac{-B_{10}+\sqrt{\Delta_{10}}}{2A_{10}},
\qquad
\beta=
\frac{-B_{01}+\sqrt{\Delta_{01}}}{2A_{01}},
}
\tag{8.3}
\]

\[
\boxed{
W=\beta-\alpha.
}
\tag{8.4}
\]

R3 的 numerical diagnostics：

| fibre | approximate band | \(W\) | \(MW\) | \(M^2W\) |
|---|---|---:|---:|---:|
| \((5,1,11,9091)\) | \(19654513.32647\ldots<x<19654513.32808\ldots\) | \(1.606\times10^{-3}\) | \(8.03\times10^1\) | \(4.015\times10^6\) |
| \((5,3,11,9091)\) | \(19762840.52893149\ldots<x<19762840.52893615\ldots\) | \(4.655\times10^{-6}\) | \(2.3275\times10^{-1}\) | \(1.16375\times10^4\) |
| \((5,4,11,9091)\) | \(19762848.89552296\ldots<x<19762848.89552461\ldots\) | \(1.647\times10^{-6}\) | \(8.235\times10^{-2}\) | \(4.1175\times10^3\) |
| \((5,1,9091,11)\) | \(30.0547405150834\ldots<x<30.0547405172120\ldots\) | \(2.129\times10^{-9}\) | \(1.0645\times10^{-4}\) | \(5.3225\) |
| \((5,3,9091,11)\) | \(30.2454020605150\ldots<x<30.2454020608925\ldots\) | \(3.775\times10^{-10}\) | \(9.4375\times10^{-5}\) | \(2.3594\times10^1\) |

这些 decimals 只用于阅读；certificate 的 PASS/FAIL 使用 exact quadratic-root integer comparison。

---

# 9. Packet × Archimedean Separation

exact packet：

\[
a\equiv rb\pmod M
\]

写成：

\[
\boxed{
a=rb+M\ell.
}
\tag{9.1}
\]

因为 \((b,M)=1\)：

\[
(a,b)=1
\iff
(\ell,b)=1.
\tag{9.2}
\]

band：

\[
\alpha<\frac ab<\beta
\]

等价于：

\[
\boxed{
(\alpha-r)b
<
M\ell
<
(\beta-r)b.
}
\tag{9.3}
\]

即：

\[
\boxed{
\left\lfloor
\frac{b(\alpha-r)}M
\right\rfloor+1
\le\ell\le
\left\lfloor
\frac{b(\beta-r)}M
\right\rfloor.
}
\tag{9.4}
\]

若 \(\theta\) 是

\[
Ax^2+Bx+C=0
\]

的正 irrational root，\(\Delta=B^2-4AC\)，则 certificate 使用：

\[
\boxed{
\left\lfloor
\frac{b(\theta-r)}M
\right\rfloor
=
\left\lfloor
\frac{
\lfloor b\sqrt\Delta\rfloor
-b(B+2Ar)
}{
2AM
}
\right\rfloor.
}
\tag{9.5}
\]

并通过：

\[
\lfloor b\sqrt\Delta\rfloor
=
\operatorname{isqrt}(\Delta b^2)
\]

完成纯整数判决。

这给出了 exact packet-spacing theorem，不使用“band 很窄”的定性论证。

---

# 10. Exact First-Admissible Rational Heights on the \(g=5\) Corpus

R4 certificate 对五个 exact PCS packets 从 \(b=1\) 开始按 (9.4) exact 扫描，并要求：

\[
(b,M)=1,\qquad
(\ell,b)=1.
\]

得到：

| fibre | \(M,r\) | exact minimal \(b\) | \(\ell\) | \(a\) | \(H(a/b)\) |
|---|---|---:|---:|---:|---:|
| \((5,1,11,9091)\) | \(50000,44707\) | \(\boxed{11411}\) | 4475350 | 224277651577 | 224277651577 |
| \((5,3,11,9091)\) | \(50000,39227\) | \(\boxed{302729}\) | 119418196 | 5982784950483 | 5982784950483 |
| \((5,4,11,9091)\) | \(50000,27227\) | \(\boxed{1059559}\) | 418221116 | 20939904412893 | 20939904412893 |
| \((5,1,9091,11)\) | \(50000,48227\) | \(\boxed{9907159}\) | -9549896 | 297757093 | 297757093 |
| \((5,3,9091,11)\) | \(250000,155347\) | \(\boxed{17795527}\) | -11055774 | 538232869 | 538232869 |

所以对这五个 fixed fibres：

\[
\boxed{
\text{PCS + band 确实产生了严格的 rational-height explosion.}
}
\]

这回答了 representative-fibre 版本的 Q3。

但这仍不是 all-\(g\) lower bound：

\[
H_{\min}(g,k,u)\ge C G^\gamma.
\]

当前没有 uniform \(\gamma\)。

---

# 11. Decontent Capacity: Exact Chord-Content Theorem

这是 R4 后半段最重要的新 algebraic theorem。

从 (2.3)：

\[
F_1=Qp_1-La,
\quad
F_2=Qp_2-Lb,
\quad
F_3=Qp_3.
\]

令：

\[
D=D_\Lambda=\gcd(F_1,F_2,F_3).
\]

则：

\[
p_3F_1-p_1F_3=-p_3La,
\]

\[
p_3F_2-p_2F_3=-p_3Lb.
\]

因为：

\[
(a,b)=1,
\]

存在 \(x,y\in\mathbb Z\) 使：

\[
xa+yb=1.
\]

于是：

\[
D\mid p_3L.
\]

同时：

\[
D\mid F_3=p_3Q.
\]

所以：

\[
\boxed{
D_\Lambda(a,b)
\mid
|p_3|\gcd(Q(a,b),L(a,b)).
}
\tag{11.1}
\]

这比 “generic resultant exists” 更贴近本 chord map。

若 \(Q\) 与 \(L\) 在 \(\mathbf P^1\) 上无共同 zero（合法 complete chart 的非零性条件），则 homogeneous resultant 给 fixed-fibre constant：

\[
\boxed{
\gcd(Q(a,b),L(a,b))
\mid
\mathcal R_{g,k,u,p}
}
\]

对所有 reduced \((a,b)\)。

因此：

\[
\boxed{
D_\Lambda(a,b)
\mid
|p_3|\mathcal R_{g,k,u,p}.
}
\tag{11.2}
\]

结论：

\[
\boxed{
\text{fixed fibre 内 }D_\Lambda
\text{ 不能随 }H(a/b)^2\text{ 无限增长。}
}
\]

如果只用 (11.1) 而不 resultant，则 \(L\) linear 还给出：

\[
D_\Lambda=O_{g,k,u,p}(H).
\]

特殊 \(L=0\) branch 退化回 basepoint ray \(F=Qp\)，是单独的 projective exceptional/basepoint state，不形成新的 unbounded slope family。

---

# 12. Two-Prime / Odd-Content Decomposition

写：

\[
D_\Lambda
=
D_{2,5}D_{\rm odd}.
\]

PCS 精确控制 \(D_{2,5}\) 与 primitive ten-unit 的 equality depth。

对 odd part，由 (11.2)：

\[
\boxed{
D_{\rm odd}
\mid
\bigl(|p_3|\mathcal R_{g,k,u,p}\bigr)_{\rm odd}
}
\tag{12.1}
\]

在 fixed fibre 成立。

所以：

```text
ODD_CONTENT_CAN_GROW_QUADRATICALLY_IN_H_ON_A_FIXED_FIBRE = NO
```

但是：

```text
UNIFORM_MOVING_ODD_CONTENT_BOUND = NOT_PROVED
```

原因是：

\[
p_3
\]

与：

\[
\mathcal R_{g,k,u,p}
\]

都依赖 moving fibre 与 basepoint/chart。

本轮没有证明：

\[
|p_3|\mathcal R
\ll G^\delta
\]

with controlled universal \(\delta\)。

因此 moving modulus growth 是否能战胜 moving content constant，仍未决。

---

# 13. Full-Primitive Survivor and Strongest R4 Full-Deep Witness

同一个 \((5,3,11,9091)\) packet 中的 full survivor：

\[
\boxed{
(a,b)=(6300650477551,318813).
}
\]

exact primitive data：

\[
\boxed{
c=
2844241425759278313791310157183552723,
}
\]

\[
\boxed{
C_2=
54695636408717919553598977546465994745062629.
}
\]

\[
\boxed{
D_\Lambda=
52175200000000000.
}
\]

parameter height：

\[
\boxed{
H(m)=6300650477551.
}
\]

\[
\boxed{
\frac{H(m)^2}{D_\Lambda}
=
\frac{
39698196440263644354957601
}{
52175200000000000
}
\approx7.6086\times10^8.
}
\]

radial ratio：

\[
\boxed{
\rho
=
\frac{
2878717705721995765978893555077157618161191
}{
14969691714522517441006895564123961700000000
}
\approx0.1923030721.
}
\]

因此：

\[
\frac1{10}<\rho<10.
\]

radial height：

\[
\boxed{
\mathfrak H_{\rm rad}
=
\frac cG
=
\frac{
2844241425759278313791310157183552723
}{
100000
}
\approx2.84424\times10^{31}.
}
\tag{13.1}
\]

它比此前 R2-CM1 的记录 radial height 更低，但仍然极度 oversize。

于是：

\[
c<G
\]

FAIL，且：

\[
C_2<G^2K
\]

也 FAIL。

common-\(U\) integer window仍为：

\[
U_{\rm lo}=1,
\qquad
U_{\rm hi}=0.
\]

所以没有进入 integer-\(U\) 层。

---

# 14. Why Full Primitive Does Not Rescue Packet Elimination

R4 的最关键 differential 是：

\[
\boxed{
\text{same }(r,M)
\quad+\quad
\text{same radial band}
}
\]

可以出现两种状态。

Near-countermodel：

\[
v_{11}(D_\Lambda)=0,
\qquad
v_{11}(\mathcal C_1)=1,
\]

所以：

\[
11\mid C_1.
\]

Full survivor：

\[
v_{11}(D_\Lambda)=3,
\qquad
v_{11}(\mathcal C_1)=3,
\]

所以 decontent 后：

\[
11\nmid C_1.
\]

也就是说 full primitive 读取的是：

\[
\boxed{
\text{odd raw-value depth}
-
\text{primitive content depth},
}
\]

而不是只读取：

\[
a/b\bmod 2^e5^f.
\]

这解释了为什么 Mechanism 1 很强但不能单独 closure。

---

# 15. Radial Height Transfer: What Is Proved and What Is Not

exact radial formula：

\[
\mathfrak H_{\rm rad}(a,b)
=
\max\left(
\frac{|f_c(a,b)|}{GD_\Lambda(a,b)},
\frac{|f_{C_2}(a,b)|}{G^2KD_\Lambda(a,b)}
\right).
\]

在 fixed fibre：

1. PCS + band 给 \(H(a/b)\ge H_{\min}\)；
2. \(D_\Lambda\) 由 (11.2) fixed-fibre bounded；
3. 在 closed sub-band 内，至少一个 branch-adapted quadratic height coordinate \(f_c,f_{C_2}\) 不能同时 quadratic-cancel。

因此 fixed-fibre asymptotic mechanism 已经严格可见：

\[
\boxed{
H\to\infty
\Longrightarrow
\mathfrak H_{\rm rad}\to\infty.
}
\]

但要把它变成所需的 finite threshold：

\[
\mathfrak H_{\rm rad}\ge1
\]

必须比较：

\[
H_{\min}
\]

与：

\[
|p_3|\mathcal R
\]

以及 band 上 quadratic coordinate 的 exact minimum。

R4 尚未得到一个 all-\(g\) inequality：

\[
H_{\min}(g,k,u)
\ge C G^\gamma,
\]

\[
D_\Lambda
\le C'G^\delta H^\eta
\]

with：

\[
2\gamma-\delta-\eta\gamma\ge1.
\]

当前 fixed-fibre resultant form实际上可取 \(\eta=0\)，但 \(\delta\) 没有统一控制。

所以 Q4 的严格答案是：

\[
\boxed{
\text{decontent 在 fixed fibre 不能无限吞掉 slope explosion，}
}
\]

但：

\[
\boxed{
\text{moving fibres 上能否吞掉 enough height 尚未被 uniform 排除。}
}
\]

---

# 16. Fixed-Fibre vs Uniform Audit

已知：

- \(g=4,(u,q)=(73,137)\) 的 fixed-fibre oversize theorem 由 R2 exact 证明；
- 本轮五个 \(g=5\) fibres 全部出现强 PCS packet spacing；
- 五个 first PCS-band hits 全部被 \(u\)-pollution 杀死；
- 同 packet 内已有 full-primitive survivor，但其 radial height 仍巨大。

R6 的 finite live split-base scan 在 \(4\le g\le8\) 还包含 \(g=6,7,8\) 多个 fibres，因此 \(g=5\) 的：

\[
M=50000\text{ or }250000
\]

不能被偷升格为 general law。

当前没有证明：

\[
M\asymp G^\alpha,
\qquad
W\asymp G^{-\beta},
\qquad
H_{\min}\gtrsim G^\gamma
\]

对所有 live fibres成立。

所以：

\[
\boxed{
\texttt{MOVING\_MODULUS\_BEATS\_DECONTENT=UNRESOLVED}.
}
\]

---

# 17. Counterexample Guillotine Result

R4 主动寻找：

\[
\rho\in(1/10,10),
\]

\[
\text{PCS}_{2,5},
\]

\[
\text{full primitive/common-}V,
\]

\[
c<G,
\qquad
C_2<G^2K.
\]

在当前 exact representative search/certificate 中：

\[
\boxed{
\texttt{SMALL\_HEIGHT\_FULL\_PRIMITIVE\_COUNTERMODEL=NOT\_FOUND}.
}
\]

但这不是 all-\(g\) finite exhaustion theorem。

因此不能写：

```text
UNIFORM_HEIGHT_TRANSFER = PROVED
```

也不能写：

```text
UNIFORM_HEIGHT_TRANSFER = FALSE
```

严格状态仍为：

\[
\boxed{\texttt{OPEN}.}
\]

---

# 18. Strongest Countermodel Ledger

对 R4 full survivor：

```text
FIBRE = (g,k,u,q) = (5,3,11,9091)
PARAMETER = (6300650477551, 318813)

EXACT_ROOT = PASS
SOURCE_LATTICE = PASS
POSITIVE_BRANCH = PASS
RADIAL_BAND = PASS

PCS_2 = PASS
PCS_5 = PASS

FULL_PRIMITIVE = PASS
COMMON_V = PASS
REGULAR = PASS

PACKET_CONGRUENCE = PASS

c < G = FAIL
C2 < G^2 K = FAIL

REAL_COMMON_U = PASS
INTEGER_COMMON_U = FAIL
COPRIME_COMMON_U = FAIL

FULL_SOURCE_LIFT = FAIL
```

first failure：

\[
\boxed{\textbf{absolute primitive radial height}.}
\]

reported invariants：

\[
\boxed{
D_\Lambda=52175200000000000,
}
\]

\[
\boxed{
H(m)=6300650477551,
}
\]

\[
\boxed{
H(m)^2/D_\Lambda
\approx7.6086\times10^8,
}
\]

\[
\boxed{
\mathfrak H_{\rm rad}
\approx2.84424\times10^{31}.
}
\]

---

# 19. Answers to the Five R4 Audit Questions

## Q1 — PCS\(_{2,5}\) 是否真的产生 uniform high-modulus packets？

**Representative-fibre YES; all-\(g\) UNPROVED.**

五个 \(g=5\) fibres 全部被 exact 化成一个 single affine packet，模数 \(50000\) 或 \(250000\)。但尚无统一 \(M(g,k,u,q)\) growth theorem。

---

## Q2 — common-\(V\)/full primitive 是否系统消灭大部分 packet？

**它强力过滤 first hits，但不能删除整个 packet。**

同一个 \((5,3,11)\) packet 已有 exact FAIL 与 PASS。故：

\[
\boxed{
\texttt{FULL\_PRIMITIVE\_PACKET\_GUILLOTINE=FALSE}.
}
\]

---

## Q3 — 剩余 packet × narrow band 是否迫使 rational slope height 爆炸？

**对五个 \(g=5\) representative fibres：YES，且 exact minimum denominator 已 certified。**

最小 \(b\) 从 \(11411\) 到 \(17795527\)。

**对 all-\(g\)：PARTIAL。**

尚无统一 exponent law。

---

## Q4 — primitive decontent 能否吞掉 slope-height explosion？

**Fixed fibre：不能无限吞掉。**

\[
D_\Lambda
\mid
|p_3|\gcd(Q,L)
\]

并由 resultant 得 fixed constant。

**Moving fibres：尚未排除。**

因为 \(|p_3|\mathcal R\) 的 moving growth 未统一控制。

---

## Q5 — 最终是否严格推出 \(\mathfrak H_{\rm rad}\ge1\)？

\[
\boxed{\textbf{NO — not uniformly yet}.}
\]

没有 counterexample，但也没有 all-\(g\) theorem。

---

# 20. Terminal Ledger

```text
J2_STATUS = OPEN

PCS_25 = PROVED / FROZEN

PCS_RESIDUE_PACKET = PARTIAL
# COMPLETE on the five R3 g=5 live fibres;
# all-g uniform packet theorem not proved.

FULL_PRIMITIVE_PACKET_FILTER = PARTIAL
FULL_PRIMITIVE_PACKET_GUILLOTINE = FALSE

NEAR_COUNTERMODEL_CAUSE = MIXED

PACKET_BAND_SPACING = PROVED
# exact inequality and exact integer-floor certificate;
# uniform all-g lower-bound law remains open.

MIN_ADMISSIBLE_SLOPE_HEIGHT =
EXACTLY COMPUTED ON FIVE G5 FIBRES:
224277651577
5982784950483
20939904412893
297757093
538232869

CONTENT_BOUND = PROVED
# exact fixed-fibre chord-content divisor theorem.

ODD_CONTENT_CONTROL = PARTIAL
# fixed-fibre bounded; moving uniform constant not controlled.

HEIGHT_TRANSFER = PARTIAL

UNIFORM_HEIGHT_TRANSFER = OPEN

SMALL_HEIGHT_FULL_PRIMITIVE_COUNTERMODEL = NOT_FOUND

INTEGER_COMMON_U_CANDIDATE = NOT_REACHED

FULL_COMMON_U_COUNTERMODEL = NOT_FOUND

MOVING_INFORMATION_ACTIVATED = YES

MOVING_HEIGHT_MECHANISM =
PCS SINGLE PACKET
+ EXACT PACKET-BAND RATIONAL SPACING
+ CHORD-CONTENT DIVISOR
D_LAMBDA | |p3| gcd(Q,L)

R4_TERMINAL_VERDICT = UNIFORMIZATION_REQUIRED
```

---

# 21. R5 唯一主 Interface

R5 不应继续增加 congruence，也不应继续 packet-by-packet odd-prime hunting。

唯一主接口应冻结为：

\[
\boxed{
\textbf{Uniform Source-Chord Content Capacity}.
}
\]

具体目标：

把 fixed-fibre theorem

\[
D_\Lambda
\mid
|p_3|\mathcal R_{g,k,u,p}
\]

改造成 basepoint/chart-independent 或 canonical-basepoint 的 moving bound：

\[
\boxed{
D_\Lambda
\le
C\,G^\delta H^\eta,
\qquad
\eta<2,
}
\]

并同步证明 PCS packet spacing：

\[
H_{\min}(g,k,u)\ge C'G^\gamma
\]

使：

\[
2\gamma-\delta-\eta\gamma\ge1.
\]

更理想的 invariant 形式是找到 source-chord minors / Plücker-content / canonical primitive isotropic basepoint，使：

\[
|p_3|\mathcal R
\]

被一个真正 source-semantic moving quantity替代，而不是 parameterization artifact。

R5 只需回答：

\[
\boxed{
\textbf{moving content capacity 是否小于 moving packet-height supply？}
}
\]

若 YES，height transfer closure。

若 NO，并构造：

\[
c<G,\quad C_2<G^2K
\]

的 full-primitive band ray，则立即进入 integer-\(U\)。

---

# 22. Computation Certificate

本轮生成：

```text
85_phaseII_R4_two_prime_height_transfer_certificate.py
85_phaseII_R4_two_prime_height_transfer_certificate.txt
```

certificate responsibilities：

1. 重建 R3 五个 \(g=5\) source-adapted chord parameterizations；
2. 从 valuation equality 本身 exact 删除 necessary zero branches；
3. CRT 得到五个 unique PCS packets；
4. exact 构造 radial boundary quadratics；
5. 使用 `isqrt(Delta*b*b)` 完成 packet-band integer comparison；
6. exact 证明五个 representative packets 的 minimal reduced denominator；
7. 验证五个 first hits 均死于 \(\gcd(C_1,u)=u\) / primitive gcd \(=u\)；
8. 验证同一个 \((5,3,11)\) packet 中存在 full-primitive/common-\(V\) survivor；
9. 因而 exact falsify `FULL_PRIMITIVE_PACKET_GUILLOTINE`.

所有 PASS/FAIL：

```text
FLOAT_GATE_DECISIONS = 0
CERTIFICATE_STATUS = PASS
```

---

# 23. Provenance / Frozen Inputs

主要承接：

- `85_phaseII_R1_moving_square_exactization.md`
- `85_phaseII_R2_radial_extinction.md`
- `85_phaseII_R3_primitive_height.md`
- `85_phaseII_R3_primitive_height_certificate.py`
- `85_R6_live_N0_split_base_scan_certificate.txt`
- `J2-65-R20-Semantic-Conductor-Ruling-Report.md`

---

# 24. Final R4 Verdict

R4 对中央命题：

\[
\begin{gathered}
\rho\in(1/10,10),\\
\text{exact root/source},\\
\text{PCS}_{2,5},\\
\text{full primitive/common-}V
\end{gathered}
\Longrightarrow
\left(
c\ge G
\ \lor\
C_2\ge G^2K
\right)
\]

的严格判决是：

\[
\boxed{
\textbf{OPEN — not proved, not falsified.}
}
\]

但本轮已经杀掉一个更便宜的候选 closure：

\[
\boxed{
\textbf{full primitive does NOT eliminate an entire PCS packet}.
}
\]

同时建立了真正可向 uniform theorem 迁移的后半桥：

\[
\boxed{
D_\Lambda
\mid
|p_3|\gcd(Q,L).
}
\]

所以 R5 不再需要问 “packet 有没有高度”。

packet height 已经 exact 出现。

R5 只需要问：

\[
\boxed{
\textbf{
这种 packet height 是否能统一战胜 source-chord 的 moving content capacity？
}}
\]

这就是第二个八五计划下一轮唯一值得中央攻击的对象。
