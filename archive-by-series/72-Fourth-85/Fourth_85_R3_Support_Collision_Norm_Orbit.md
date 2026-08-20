# Fourth 85 · R3 — \(\Psi_K\)-Support Collision × Gaussian Inert Allocation × Fixed-\(\tau\) Norm Orbit × Power-of-Ten Incidence

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — \(J=2\)  
**Round:** 第四个八五计划 · R3  
**Primary inherited shell actually attacked:** q=1 negative fixed-\((K,d,\tau)\) shell  
**Completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 1. Executive Verdict

本轮没有证明

\[
q=1\Longrightarrow\varnothing,
\]

因此当然没有证明

\[
J=2\Longrightarrow\varnothing.
\]

R3 的两条中央架构均已完成 Repair-or-Kill，并得到：

\[
\boxed{\texttt{SUPPORT_COLLISION_ARCHITECTURE=DEAD}}
\]

以及

\[
\boxed{\texttt{FIXED_TAU_PELL_AS_FIXED_OBJECT_ARCHITECTURE=DEAD}}.
\]

总判决：

\[
\boxed{\texttt{R3_DUAL_ARCHITECTURE_DEAD}}.
\]

但这里第一条架构的死亡原因必须精确说明：

> **Polynomial collision 的代数部分实际上成功了。**  
> \(\Psi_K\) 与 \(S,Q_K,T_4\) 对三个 \(K\) 全部 polynomial-coprime；resultant、Bézout 与 \(G=10^g\) specialization 都给出了很强的 fixed exceptional prime set。  
> 真正死亡的是 **same-\(h\) provenance bridge**：R2 的
> \[
> h=\gcd(y,\rho)
> \]
> 与 Gaussian theorem 所控制的 \(M_0,L_0\) support 不是同一个 arithmetic quantity。

所以：

```text
POLYNOMIAL_SUPPORT_COLLISION_ALGEBRA = SUCCESS
POWER10_VALUE_GCD_UNIFORM_BOUND = PROVED
COMMON_h_TO_GLOBAL_SUPPORT_BRIDGE = NO
MOVING_ODD_SUPPORT_FROZEN = NO
FIXED_S_SUPPORT_ACHIEVED = NO

SOURCE_CASES = 24
COEFFICIENT_TEMPLATES = 12
FIXED_FIELD = NO
FIXED_ORDER = NO
FIXED_UNIT = NO
FIXED_RECURRENCE = NO
FIXED_NORM_ORBIT_EXTRACTED = NO
POWER10_ORBIT_INCIDENCE_DIMENSION_DROP = NO

Q1_BRANCH_CLOSED = NO
J2_CLOSED = NO
R3_DUAL_ARCHITECTURE = DEAD
```

---

# 2. Provenance Sources Recovered

本轮重新回收并核验的关键历史资产来自：

- `Fourth_85_R1_Fixed_Object_Extraction.md`
- `Fourth_85_R1_Lemmas.md`
- `Fourth_85_R2_Decimal_Core_Factor_Gap.md`
- `Fourth_85_R2_Factor_Gap_Lemmas.md`
- `J2-55-R11-Deterministic-u-Decimal-Cofactor-Report.md`
- `J2-55-R13-Independent-Root-Coefficient-Gaussian-Report.md`
- `J2-55-R15-Spliced-Factor-2Adic-NegativeConic-Report.md`
- `J2-65-R16-Integral-Boundary-Norm-Orbit-Report.md`（只作为“moving field/order”方法论对照；该轮本身严格属于 q>1，未被偷迁移为 q=1 theorem）

没有找到一条独立的 75 资产能够补上

\[
p\mid h\Longrightarrow p\mid M_0L_0
\]

或把 q=1 的 moving real quadratic family 变成跨 \(g\) fixed field/order。故本报告不虚构这类迁移。

---

# 3. R1–R2 Frozen Conclusions

R2 factor-gap architecture 永久冻结，不再修补。

q=1 negative shell：

\[
K=10^k,\qquad k\in\{1,2,3\},
\]

\[
G=10^g,\qquad g-k\ge2,
\]

\[
(d,\tau)\in
\{(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1)\}.
\]

定义

\[
\rho=a-\frac{\tau G}{10}>0.
\]

DCDC：

\[
\boxed{31\rho+\tau\equiv0\pmod{2K}}.
\]

primitive / source window：

\[
\gcd(\rho,10\tau)=1,
\]

\[
\boxed{
0<\rho<
\frac{10-d\tau}{10d}G
}.
\]

conic square condition 下：

\[
Y_0=2Ky,
\qquad
\gcd(y,10)=1.
\]

定义：

\[
L=y-\rho,\qquad R=y+\rho.
\]

R2 已证：

\[
0<L<R,
\]

\[
\gcd(L,R)=2h,
\qquad
h:=\gcd(y,\rho),
\]

并且剥离 decimal core 后：

\[
\gcd(\ell,r)=h.
\]

最关键的新 source destination：

\[
\boxed{h\mid\Psi_K(G)}.
\]

同时 full-\(\eta\) parameterization 精确返回 original square condition，因此不再使用。

---

# 4. Historical q=1 Fixed-\(\tau\) Conic Reconstruction

精确恢复：

\[
Y_0^2=A_2(G,K)a^2+B_1(G,K,\tau)a+C_0(G,K,\tau),
\]

其中

\[
\begin{aligned}
A_2={}&100G^6K^2-100G^6+280G^5K^2-380G^5\\
&+236G^4K^2-545G^4
+16G^3K^2-362G^3\\
&-52G^2K^2-93G^2-8GK^2+4K^2,
\end{aligned}
\]

\[
B_1=
-G^2\tau
\left(
20G^5K^2-20G^5
+48G^4K^2-68G^4
+32G^3K^2-85G^3
-46G^2-4GK^2-4G+3
\right),
\]

\[
C_0=\frac{G^5\tau^2}{4}Q_K(G).
\]

作为 \(a\) 的二次式，其 discriminant：

\[
\boxed{
\Delta_a
=
G^4\tau^2(G+1)^2(2G+3)^2T_4(G,K)
}.
\]

完成平方：

\[
\boxed{
(2A_2a+B_1)^2
-
4A_2Y_0^2
=
\Delta_a
}.
\]

这就是 R3 的 norm skeleton 出发点。

---

# 5. The 24 Cases and the Exact 12-Template Compression

8 个 \((d,\tau)\)：

\[
(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1).
\]

与三个 \(K\) 给 24 source cases。

DCDC 对每个 \((K,\tau)\) 给唯一 residue：

\[
\boxed{
a\equiv
-\tau\,31^{-1}
\pmod{2K}
}.
\]

negative source window：

\[
\boxed{
\frac{G^3\tau}{10G^2+4G-2}
<
a
<
\frac Gd
}.
\]

注意：

- \(d\) 进入 source upper window；
- \(d\) 不进入 \(A_2,B_1,C_0,\Delta_a\)。

因此：

\[
\boxed{24\longrightarrow12}
\]

是严格的 **coefficient-template compression**：

\[
3K\times4\tau=12.
\]

但它不是 fixed-field compression。

完整 24 case residue 表在：

`Fourth_85_R3_computation/source_case_templates.tsv`.

---

# 6. Explicit \(\Psi_K,Q_K,T_4,S\)

定义：

\[
\boxed{
S(X)=(X+1)(2X+3)
}.
\]

\[
\boxed{
\Psi_K(X)
=
K^2(16X^4+16X^3-12X^2-8X+4)
-
(20X^4+52X^3+53X^2+30X)
}.
\]

\[
\boxed{
Q_K(X)
=
4X^3K^2-4X^3
+8X^2K^2-12X^2
+4XK^2-13X-6
}.
\]

\[
\boxed{
T_4(X,K)
=
4X^4K^2-4X^4
+8X^3K^2-12X^3
+4X^2K^2-13X^2-6X+1
}.
\]

精确 identity：

\[
\boxed{
T_4(X,K)=1+XQ_K(X)
}.
\]

三个 \(\Psi_K\)：

\[
\Psi_{10}
=
1580X^4+1548X^3-1253X^2-830X+400,
\]

\[
\Psi_{100}
=
159980X^4+159948X^3-120053X^2-80030X+40000,
\]

\[
\Psi_{1000}
=
15999980X^4+15999948X^3-12000053X^2-8000030X+4000000.
\]

exact audit：

- \(\Psi_K,Q_K,T_4\) content 都是 \(1\)；
- 对 \(K=10,100,1000\)，它们在 \(\mathbf Q[X]\) 上没有进一步 factor；
- \(S=(X+1)(2X+3)\)；
- 所有对象均 squarefree，无 repeated factor。

详见：

- `recovered_polynomials.txt`
- `factorization_tables.tsv`

---

# 7. Polynomial gcd Audit

令

\[
F_K(X)=S(X)Q_K(X)T_4(X,K).
\]

对每个

\[
K\in\{10,100,1000\},
\]

exact SymPy / rational polynomial arithmetic 得：

\[
\boxed{
\gcd_{\mathbf Q[X]}(\Psi_K,S)=1
},
\]

\[
\boxed{
\gcd_{\mathbf Q[X]}(\Psi_K,Q_K)=1
},
\]

\[
\boxed{
\gcd_{\mathbf Q[X]}(\Psi_K,T_4)=1
},
\]

\[
\boxed{
\gcd_{\mathbf Q[X]}(\Psi_K,F_K)=1
}.
\]

因此 Conjecture A 的 polynomial 层完全通过。

---

# 8. Resultant Audit

## \(K=10\)

\[
|\operatorname{Res}(\Psi,S)|
=
230400
=
2^{10}3^25^2.
\]

\[
|\operatorname{Res}(\Psi,Q)|
=
848554803200
=
2^{14}5^2\cdot13\cdot37\cdot59\cdot73.
\]

\[
|\operatorname{Res}(\Psi,T_4)|
=
304798085725766656
=
2^{10}\cdot17252663^2.
\]

## \(K=100\)

\[
|\operatorname{Res}(\Psi,S)|
=
23040000
=
2^{12}3^25^4.
\]

\[
|\operatorname{Res}(\Psi,Q)|
=
92086088780472320000
=
2^{16}5^4\cdot149\cdot15088560583.
\]

\[
|\operatorname{Res}(\Psi,T_4)|
=
331497763496971095950227814656
=
2^8\cdot53^2\cdot678960406367^2.
\]

## \(K=1000\)

\[
|\operatorname{Res}(\Psi,S)|
=
2304000000
=
2^{14}3^25^6.
\]

\[
|\operatorname{Res}(\Psi,Q)|
=
9215926080087807967232000000
=
2^{20}5^6\cdot562495488286609373.
\]

\[
|\operatorname{Res}(\Psi,T_4)|
=
331773216776670963210121839884142720614656
\]

\[
=
2^8\cdot10343^2\cdot54821101^2\cdot63490157^2.
\]

完整 resultant 以及 overall \(F_K\) resultant 在：

`resultant_certificates.tsv`.

---

# 9. Integer-Value gcd: Bézout Layer

本轮没有停在

\[
\gcd_{\mathbf Q[X]}=1.
\]

对每一个 pair 实际计算了：

\[
A(X)\Psi_K(X)+B(X)F(X)=C
\]

其中

\[
A,B\in\mathbf Z[X],
\qquad
C\in\mathbf Z\setminus\{0\}.
\]

因此对任意整数 \(n\)：

\[
\boxed{
\gcd(\Psi_K(n),F(n))\mid C
}.
\]

完整 denominator-cleared Bézout 多项式在：

`bezout_certificates.txt`.

常数及 factorization 在：

`gcd_certificates.tsv`.

这一步把 polynomial coprimality 升级成了真正的 integer-value uniform gcd theorem。

---

# 10. Specialization \(G=10^g\)

现在利用 \(G=10^g\)。

## 10.1 Prime 5

\[
G\equiv0\pmod5.
\]

于是

\[
S(G)\equiv3,
\]

\[
Q_K(G)\equiv-6\equiv-1,
\]

\[
T_4(G,K)\equiv1
\pmod5.
\]

所以：

\[
\boxed{5\nmid F_K(10^g)}.
\]

5 从 actual gcd 中彻底删除。

---

## 10.2 Prime 3

\[
10^g\equiv1\pmod3.
\]

而

\[
S(1)=10\not\equiv0\pmod3.
\]

resultant 的 3-support 不被 power-of-ten orbit 命中，因此 3 也删除。

---

## 10.3 Prime 2

live shell 有 \(g\ge3\)。

\(S,T_4\) 为 odd，而

\[
Q_K(10^g)\equiv-6\pmod4,
\]

所以：

\[
v_2(F_K(10^g))=1.
\]

\(\Psi_K(10^g)\) 为 even，因此：

\[
\boxed{
v_2\gcd(\Psi_K(10^g),F_K(10^g))=1
}.
\]

---

# 11. Exceptional Odd Prime Period Audit

对所有 resultant exceptional odd primes：

1. exact 计算
   \[
   \gcd(\Psi_K,F\text{-component})\pmod p;
   \]
2. 得到唯一 linear common root \(r_p\)；
3. exact 计算
   \[
   \operatorname{ord}_p(10);
   \]
4. 判断
   \[
   r_p\in\langle10\rangle;
   \]
5. 若 resultant exponent 为 \(2\)，再审计 \(p^2\)-Hensel class。

关键删除：

\[
K=10:\quad p=37,73
\]

的 common roots 不在 \(\langle10\rangle\)。

\[
K=1000:\quad p=63490157
\]

同样不在 \(\langle10\rangle\)。

其余 retained primes 均给 exact \(g\)-period class。

详见：

`exceptional_prime_audit.tsv`.

---

# 12. Specialization-Sharpened Minimal Uniform gcd Constants

最终：

\[
\boxed{
\gcd(\Psi_K(10^g),F_K(10^g))
\mid C'_K
}
\]

且得到：

\[
\boxed{
C'_{10}
=
456601819827466846
=
2\cdot13\cdot59\cdot17252663^2
}.
\]

\[
\boxed{
C'_{100}
=
5822435852033633542331975248275187065334
=
2\cdot53^2\cdot149\cdot15088560583\cdot678960406367^2
}.
\]

\[
\boxed{
C'_{1000}
=
361690910889592488261208717961027874646954
=
2\cdot10343^2\cdot54821101^2\cdot562495488286609373
}.
\]

这些常数是 specialization-period audit 后的 **minimal uniform divisibility constants**：

- 所有被删除 prime 永远不会被 \(10^g\) 命中；
- 每个 retained odd prime 都有明确 \(g\)-class 命中；
- exponent \(2\) 的 retained \(T_4\)-primes 也有明确 \(p^2\)-Hensel \(g\)-class。

所以 Phase I 的 algebraic/value-gcd 部分比预期更强。

---

# 13. What Would Have Been Enough for Fixed-\(S\)

如果同一个 \(h\) 还满足：

\[
h\mid F_K(G),
\]

则由

\[
h\mid\Psi_K(G)
\]

立即得到：

\[
h\mid C'_K
\]

至少在 odd support 层得到：

\[
\operatorname{Supp}(h)
\subseteq
\operatorname{Supp}(C'_K).
\]

于是：

\[
\boxed{
\text{moving odd support}\to\text{fixed finite }S
}
\]

将真正成立。

随后 Thue–Mahler / \(S\)-unit / fixed-support norm descent 才有资格启动。

因此 R3 的第一阶段只剩一个问题：

> 历史 Gaussian/global theorem 控制的是不是 **同一个 \(h\)**？

答案：不是。

---

# 14. Gaussian / Inert Prime Assets — Exact Recovery

历史 Gaussian identity：

\[
\boxed{
M_0L_0
=
Y_0^2+(S_Ga)^2
},
\]

其中

\[
\boxed{
S_G=(G+1)(2G+3)
}.
\]

primitive：

\[
\gcd(M,a)=1.
\]

对 odd inert prime

\[
p\equiv3\pmod4
\]

历史定理是：

\[
\boxed{
p\mid M_0
\Longrightarrow
p\mid S_G
}.
\]

更强 valuation budget：

\[
\boxed{
v_p(M_0)+v_p(L_0)
=
2\min(v_p(Y_0),v_p(S_G))
\le
2v_p(S_G)
}.
\]

特别：

\[
\boxed{
(M_0)_{3\bmod4}\mid S_G^2
}
\]

在 valuation 意义下成立。

L-side external inert theorem：

\[
\boxed{
p\equiv3(4),\quad
p\mid L_0,\quad
p\nmid S_G
\Longrightarrow
p\mid\gcd(a,Q_K(G))
}.
\]

这是精确 theorem statement。

它从来没有说：

\[
p\mid h
\Longrightarrow
p\mid M_0L_0.
\]

---

# 15. Common-\(h\) Provenance Audit

设 odd prime

\[
p\mid h=\gcd(y,\rho).
\]

则

\[
p\mid y,
\qquad
p\mid\rho.
\]

因为

\[
Y_0=2Ky
\]

且 R2 已证

\[
p\nmid10KG\tau,
\]

所以：

\[
p\mid Y_0.
\]

又：

\[
a=\frac{\tau G}{10}+\rho.
\]

模 \(p\)：

\[
a\equiv\frac{\tau G}{10}\not\equiv0\pmod p.
\]

因此：

\[
\boxed{p\nmid a}.
\]

把 Gaussian identity 模 \(p\)：

\[
M_0L_0
\equiv
(S_Ga)^2
\pmod p.
\]

于是如果

\[
p\nmid S_G,
\]

就有：

\[
\boxed{
p\nmid M_0,
\qquad
p\nmid L_0
}.
\]

换言之：

\[
\boxed{
p\mid h,\ p\nmid S_G
\Longrightarrow
p\notin\operatorname{Supp}(M_0L_0)
}.
\]

这正面否定了把 Gaussian \(M_0/L_0\) inert allocation 直接迁移到 \(h\) 的合法性。

因此：

\[
\boxed{
h\mid\Psi_K(G)
}
\]

与

\[
p\mid M_0\Rightarrow p\mid S_G,
\]

\[
p\mid L_0,\ p\nmid S_G\Rightarrow p\mid Q_K(G)
\]

控制的是 **不同的 prime-support channels**。

这不是缺一两个 valuation，而是 provenance object mismatch。

---

# 16. Phase I Verdict

prompt 的 Failure C 精确触发：

\[
\boxed{
\text{the }h\mid\Psi_K(G)
\text{ theorem and the Gaussian support theorem do not control the same arithmetic quantity}.
}
\]

因此：

\[
\boxed{
\texttt{SUPPORT_COLLISION_ARCHITECTURE=DEAD}
}.
\]

同时：

\[
\boxed{
\texttt{MOVING_ODD_SUPPORT_FROZEN=NO}
}.
\]

\[
\boxed{
\texttt{FIXED_S_SUPPORT_ACHIEVED=NO}
}.
\]

重要区别：

\[
\gcd(\Psi_K(10^g),F_K(10^g))
\]

本身确实有 fixed finite support；

但

\[
h
\]

没有被证明属于这个 gcd。

所以不能生成 Fixed-\(S\) certificate。

---

# 17. Phase I Information Gain

| object | gain |
|---|---|
| polynomial gcd | STRUCTURAL |
| exact resultant | STRUCTURAL |
| integer Bézout | STRUCTURAL |
| power-ten exceptional prime pruning | FILTER / STRUCTURAL |
| \(\gcd(\Psi,F)\) fixed support | FIXED_SUPPORT — **auxiliary gcd only** |
| transfer to \(h\) | ZERO |
| same-\(h\) provenance audit | STRUCTURAL / ARCHITECTURE-KILL |
| q1 closure | NO |

---

# 18. Exact Integral Norm Skeleton for Phase II

completed-square equation：

\[
(2A_2a+B_1)^2-4A_2Y_0^2
=
G^4\tau^2S_G^2T_4(G,K).
\]

在 live specialization \(g-k\ge2\) 上：

\[
4K^2\mid A_2(G,K).
\]

定义：

\[
\boxed{
D_{K,g}:=\frac{A_2(G,K)}{4K^2}\in\mathbf Z_{>0}
}.
\]

又

\[
Y_0=2Ky.
\]

令：

\[
X_0:=2A_2a+B_1,
\]

\[
Z_0:=8K^2y.
\]

则得到精确 integral norm equation：

\[
\boxed{
X_0^2
-
D_{K,g}Z_0^2
=
\left[
G^2\tau(G+1)(2G+3)
\right]^2
T_4(G,K)
}.
\]

这就是 q=1 fixed-\(\tau\) skeleton 的正确 norm form。

---

# 19. Integrality / Order Audit

对固定 specialization \((K,d,\tau,g)\)：

- \(D_{K,g}\in\mathbf Z\)；
- \(X_0,Z_0\in\mathbf Z\)；
- 因此
  \[
  X_0+Z_0\sqrt{D_{K,g}}
  \]
  至少是 order
  \[
  \mathbf Z[\sqrt{D_{K,g}}]
  \]
  中的 integral norm element；
- 若取 \(D_{K,g}\) 的 squarefree core \(D^\mathrm{sf}_{K,g}\)，可进入对应 maximal real quadratic field；
- nonmaximal-order / conductor 只会进一步 **依赖 \(g\)**，不会恢复 fixedness。

所以单个 \(g\) 的 norm theory 完全合法。

问题不是 integrality；问题是跨 \(g\) fixedness。

---

# 20. Fixedness Audit

| object | verdict |
|---|---|
| \(K\) | FIXED_PER_K |
| \(d,\tau\) | FIXED_PER_SOURCE_CASE |
| modulus \(2K\) | FIXED_PER_K |
| DCDC residue \(a_0\) | FIXED_PER_(K,\tau) |
| symbolic conic template in \(G\) | FIXED_PER_(K,\tau) |
| \(D_{K,g}\) | MOVES_WITH_g |
| squarefree field radicand | MOVES_WITH_g |
| maximal field | MOVES_WITH_g |
| quadratic order / conductor | MOVES_WITH_g |
| fundamental unit | MOVES_WITH_g |
| unit trace | MOVES_WITH_g |
| recurrence characteristic polynomial | MOVES_WITH_g |
| RHS square class \(T_4(G,K)\) | MOVES_WITH_g |
| Gaussian field \(\mathbf Q(i)\) | ABSOLUTELY_FIXED |
| Gaussian unit rank | 0 |

因此：

\[
\boxed{
\text{fixed }(K,d,\tau)\text{ source template}
\neq
\text{fixed Pell arithmetic object}
}.
\]

---

# 21. Explicit Field-Movement Certificates

对每个 \(K\)，取两个 consecutive live \(g\)。

## \(K=10\)

\[
D_{10,3}
=
24819107640581765501,
\]

\[
D_{10,4}
=
24756905576378093676730001.
\]

两者均经 exact factorization 认证为 squarefree，且不相等。

因此：

\[
\mathbf Q(\sqrt{D_{10,3}})
\neq
\mathbf Q(\sqrt{D_{10,4}}).
\]

---

## \(K=100\)

\[
D_{100,4}
=
25004499639867739649747501,
\]

\[
D_{100,5}
=
24998199910898641490819976550001.
\]

同样为不同 squarefree radicands。

---

## \(K=1000\)

\[
D_{1000,5}
=
25000675004949990374779499567501,
\]

\[
D_{1000,6}
=
25000044999963999867749896499974750001.
\]

同样不同。

完整 prime factor certificates 在：

`quadratic_field_data.tsv`.

因此 Conjecture C：

> “24 q=1 cases 是 fixed Pell problems”

被严格处决。

---

# 22. What Is Actually Fixed Per \(g\)

固定单个

\[
(K,d,\tau,g)
\]

之后，如果 \(D_{K,g}\) nonsquare，则一个 integral norm packet 可以分成有限 many unit orbits：

\[
\alpha_n=\alpha_0\varepsilon_g^n.
\]

这点成立。

但 subscript 必须写成：

\[
\boxed{\varepsilon_g},
\]

不能写成一个与 \(g\) 无关的 \(\varepsilon\)。

所以历史说法应改写为：

\[
\boxed{
24\text{ fixed source templates}
\times
\text{a moving family of per-}g\text{ norm orbits}
}.
\]

---

# 23. Orbit Recurrence Audit

对一个固定 \(g\)，若

\[
\varepsilon_g
\]

的 trace 为 \(T_g\)，norm 为 \(N_g=\pm1\)，则 orbit coordinates 满足：

\[
\boxed{
U_{n+2}
=
T_gU_{n+1}
-
N_gU_n
}.
\]

这是合法 fixed-\(g\) recurrence。

但：

\[
T_g
\]

随 \(g\) 变化。

所以全局对象不是：

\[
U_n
\]

而是：

\[
\boxed{U_{g,n}}.
\]

这意味着以下 heavy tools 没有直接的 fixed target：

- Lucas primitive divisor；
- Lehmer primitive divisor；
- one fixed binary recurrence；
- recurrence-perfect-power intersection；
- one fixed \(p\)-adic logarithm；
- one fixed Baker form \(n\log\varepsilon-g\log10\)。

---

# 24. Power-of-Ten Incidence — Fixed Orbit Hypothesis Fails

prompt 理想结构：

\[
\alpha_0\varepsilon^n\in\mathcal S_g.
\]

实际恢复：

\[
\boxed{
\alpha_{0,g}\varepsilon_g^n\in\mathcal S_g
}.
\]

每当

\[
G=10^g
\]

改变：

- field 改变；
- order 改变；
- unit generator 改变；
- recurrence 改变；
- norm RHS square class 改变。

所以没有一个 fixed exponential orbit 被 \(10^g\)-section 穿过。

这是 Phase II 的 primary fixedness failure。

---

# 25. Multiplicative Independence Audit

若真有一个 fixed real quadratic unit \(\varepsilon\)，通常可用 degree / norm / ideal valuation 证明：

\[
\varepsilon^a\neq10^b
\]

除 trivial case。

但本轮没有 fixed \(\varepsilon\)。

因此 multiplicative-independence lemma **不是 blocker**；它是一个尚未合法激活的问题。

本轮不做无对象的 independence proof。

---

# 26. Archimedean / Baker Audit

还必须检查 prompt 的 Conjecture E：

> source window 是否真的给出 exponential precision？

由

\[
a=\frac{\tau G}{10}+\rho
\]

代入

\[
X_0=2A_2a+B_1,
\]

最高阶 \(\tau G\) 主项发生结构性消去；剩余 leading \(a\)-dependence 以

\[
G^6\rho
\]

为主。

而 source 给：

\[
0<\rho<c_{d,\tau}G.
\]

所以 \(X_0\) 的合法 section 跨越主尺度的 fixed proportion，而不是相对宽度

\[
e^{-cg}.
\]

当前没有导出：

\[
0<
|n\log\varepsilon-g\log10+\gamma|
<
e^{-cg}.
\]

因此：

\[
\boxed{
\texttt{BAKER_EXPONENTIAL_PRECISION=NO}
}.
\]

即使 fixed unit 问题不存在，当前 source window 本身也没有达到 prompt 所要求的 Baker 精度。

---

# 27. \(2\)-adic / \(5\)-adic Unit Orbit Audit

希望写：

\[
\varepsilon^n\equiv c_g\pmod{p^{g-O(1)}}
\]

并通过

\[
\exp_p(n\log_p\varepsilon)
\]

把 \(n\) 锁进深 residue，需要一个 fixed \(p\)-adic algebraic unit。

实际只有：

\[
\varepsilon_g.
\]

继续推进会变成：

\[
\text{moving field}
+
\text{moving local unit}
+
\text{new digit ladder},
\]

既不满足 fixed-object hypothesis，也违反本轮 Repair-or-Kill 纪律。

故：

\[
\boxed{
\texttt{PADIC_UNIT_ORBIT_ROUTE=NOT_ACTIVATED}
}.
\]

---

# 28. Primitive-Divisor Audit

Primitive divisor theorem 需要一条 fixed recurrence / divisibility sequence。

当前只有：

\[
U_{g,n}.
\]

所以：

\[
\boxed{
\texttt{PRIMITIVE_DIVISOR_INTERFACE_ACTIVATED=NO}
}.
\]

这不是说 primitive divisor theorem 错；而是当前对象不满足其 fixed-sequence 输入接口。

---

# 29. Gaussian Fixed Object Audit

唯一 absolutely fixed 的 quadratic object 是：

\[
\mathbf Z[i].
\]

但：

\[
\mathbf Z[i]^\times
=
\{\pm1,\pm i\}.
\]

unit rank 为 0。

因此 Gaussian layer 能做：

- inert/split allocation；
- Gaussian ideal factorization；
- sum-of-two-squares support control；

但不能产生 rank-one Pell orbit：

\[
\alpha_0\varepsilon^n.
\]

而 Phase I 已证明：

\[
h
\]

与 Gaussian \(M_0/L_0\) support 不对接。

所以 fixed \(\mathbf Z[i]\) 不能救回 Phase II。

---

# 30. Phase II Verdict

R3 没有抽出：

\[
\boxed{
\text{fixed field/order/unit orbit/recurrence}
}.
\]

因此：

\[
\boxed{
\texttt{FIXED_NORM_ORBIT_EXTRACTED=NO}
}.
\]

\[
\boxed{
\texttt{POWER10_ORBIT_INCIDENCE_DIMENSION_DROP=NO}
}.
\]

\[
\boxed{
\texttt{FIXED_TAU_PELL_AS_FIXED_OBJECT_ARCHITECTURE=DEAD}
}.
\]

这条 architecture 不允许 R4 继续“修 Pell”。

---

# 31. Counterexample Guillotine

## Conjecture A

\[
\gcd(\Psi_K(10^g),F_K(10^g))
\]

uniformly bounded。

\[
\boxed{\textbf{TRUE}}
\]

且 minimal specialization constants \(C'_K\) 已给出。

---

## Conjecture B

common \(h\) 的全部 odd support 都落在 global polynomial destination。

\[
\boxed{\textbf{NOT PROVED / THE HISTORICAL BRIDGE DOES NOT EXIST}}
\]

而且当

\[
p\mid h,\quad p\nmid S_G
\]

时，Gaussian identity 反而给：

\[
p\nmid M_0L_0.
\]

---

## Conjecture C

24 q=1 cases 是 fixed Pell problems。

\[
\boxed{\textbf{FALSE}}
\]

field/order/unit/recurrence 随 \(g\) 变化。

---

## Conjecture D

fixed unit orbit 与 \(10^g\)-section 的 intersection 稀疏到有限。

\[
\boxed{\textbf{NOT APPLICABLE}}
\]

因为没有 fixed unit orbit 被合法抽出。

---

## Conjecture E

Baker approximation 有指数级精度。

\[
\boxed{\textbf{FALSE AT CURRENT INFORMATION LAYER}}
\]

source window 没有给这种 relative thinness。

---

# 32. Novelty Guillotine

本轮没有把以下内容当新突破：

- orientation congruence；
- 新 mod \(2^r\)；
- 新 mod \(5^r\)；
- decimal tail；
- generic Pell growth；
- prime hunt；
- small-\(g\) search；
- full-\(\eta\) reparameterization。

真正新信息只有：

1. \(\Psi\)-vs-\(S,Q,T_4\) exact polynomial gcd package；
2. exact resultants；
3. denominator-cleared integer Bézout certificates；
4. \(10^g\) specialization exceptional-prime period audit；
5. minimal uniform \(C'_K\)；
6. same-\(h\) provenance-failure theorem；
7. 24→12 coefficient-template compression；
8. exact integral moving norm form；
9. explicit field-movement certificates；
10. fixed-Pell wording的严格 falsification。

---

# 33. Information Gain

| statement | class |
|---|---|
| polynomial gcd = 1 | STRUCTURAL |
| exact resultants | STRUCTURAL |
| Bézout uniform gcd | STRUCTURAL |
| exceptional-prime pruning | FILTER / STRUCTURAL |
| fixed support of auxiliary \(\gcd(\Psi,F)\) | FIXED_SUPPORT — auxiliary only |
| fixed support of \(h\) | NOT ACHIEVED |
| same-\(h\) mismatch | STRUCTURAL / ARCHITECTURE-KILL |
| 24→12 templates | STRUCTURAL |
| moving field/order theorem | STRUCTURAL / ARCHITECTURE-KILL |
| fixed norm orbit | NOT ACHIEVED |
| orbit-incidence dimension drop | NOT ACHIEVED |
| branch closure | NOT ACHIEVED |

必须明确回答：

\[
\boxed{
h\text{ 的 odd support 没有从 moving 变成 fixed}.
}
\]

以及：

\[
\boxed{
24\text{ q=1 cases 不是 24 个 fixed arithmetic Pell objects;}
}
\]

它们是：

\[
\boxed{
24\text{ fixed source cases}
\to
12\text{ fixed conic coefficient templates}
\to
\text{moving }g\text{-dependent real quadratic norm family}.
}
\]

---

# 34. Final q=1 Verdict

本轮严格攻击的 inherited central shell 是 q=1 negative 24-case system。

它仍然：

\[
\boxed{\textbf{OPEN}}.
\]

因此：

\[
\boxed{
\texttt{Q1_BRANCH_CLOSED=NO}
}.
\]

历史其他 q=1 live branch 也没有被本轮自动消灭。

所以绝不生成 q1 final closure certificate。

---

# 35. Overall R3 Verdict

Phase I：

\[
\boxed{
\texttt{SUPPORT_COLLISION_ARCHITECTURE=DEAD}
}
\]

with:

```text
POLYNOMIAL_COLLISION = SUCCESS
SAME_h_TRANSFER = FAILURE C
FIXED_h_SUPPORT = NO
```

Phase II：

\[
\boxed{
\texttt{FIXED_TAU_PELL_AS_FIXED_OBJECT_ARCHITECTURE=DEAD}
}
\]

with:

```text
FIXED_SOURCE_TEMPLATE = YES
FIXED_FIELD = NO
FIXED_ORDER = NO
FIXED_UNIT = NO
FIXED_RECURRENCE = NO
POWER10_INCIDENCE_DIMENSION_DROP = NO
```

最终：

\[
\boxed{
\texttt{R3_DUAL_ARCHITECTURE_DEAD}
}.
\]

---

# 36. R4 Decision

R4 不应再：

- 修 \(\Psi\)-support collision；
- 再找一个 polynomial destination 企图硬接 \(h\)；
- 用更多 inert-prime bookkeeping 修 same-\(h\) provenance；
- 把 moving \(D_{K,g}\) 称为 fixed Pell；
- 枚举 Pell indices；
- 做 moving-unit Baker；
- 做 moving-unit \(p\)-adic logarithm；
- 回到 R2 factor-gap / orientation / decimal-core；
- 回到 q>1 sparse-\(N_0\) legacy route。

如果第四个八五继续，必须使用 **新的 information class**。

对 q=1 negative，更自然的候选必须直接读取：

\[
\boxed{
\text{full moving conic/norm family}
+
\text{source residue/window}
+
\text{power-of-ten specialization}
}
\]

而不是先投影成 fixed support 或 fixed Pell。

可以考虑的新的 theorem 类别只能是例如：

- moving-family integral points / arithmetic surface；
- fibration + specialization theorem；
- genuinely two-exponent Diophantine equation；
- direct elimination producing fixed genus \(>0\) object；
- modular/automorphic method if a fixed compatible representation is found；
- effective global theorem directly uniform in \(g\)。

但这些只是 **R4 architecture categories**，不是 R3 已证明路线。

---

# 37. Artifact Index

主报告：

`/mnt/data/Fourth_85_R3_Support_Collision_Norm_Orbit.md`

计算目录：

`/mnt/data/Fourth_85_R3_computation/`

包含：

- `recovered_polynomials.txt`
- `factorization_tables.tsv`
- `resultant_certificates.tsv`
- `gcd_certificates.tsv`
- `bezout_certificates.txt`
- `exceptional_prime_audit.tsv`
- `common_h_provenance_audit.txt`
- `source_case_templates.tsv`
- `quadratic_field_data.tsv`
- `unit_orbit_data.tsv`
- `recurrence_data.txt`
- `finite_verification.py`
- `r3_machine_summary.json`
- `execution.log`
- `artifact_index.tsv`

由于 Phase I success predicate 为 false：

**不生成**

`Fourth_85_R3_Fixed_S_Support_Certificate.md`.

由于 Phase II fixed-orbit success predicate 为 false：

**不生成**

`Fourth_85_R3_Norm_Orbit_Certificate.md`.

由于 q=1 未闭：

**不生成**

`Fourth_85_q1_Final_Closure_Certificate.md`.
