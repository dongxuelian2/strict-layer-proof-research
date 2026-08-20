# Fourth 85 · R2 — Exact Decimal-Core Allocation × Additive Factor-Gap Collision × Four-Orientation Rigidity × q=1 Branch Audit

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — \(J=2\)  
**Round:** 第四个八五计划 · R2  
**Central target:** \(q=1\Rightarrow\varnothing\)

---

# 1. Executive Verdict

\[
\boxed{\textbf{q=1 NEGATIVE BRANCH REMAINS OPEN}}
\]

本轮没有证明

\[
q=1\Longrightarrow\varnothing.
\]

因此不生成 `Fourth_85_q1_Closure_Certificate.md`。

本轮最终主 verdict 为：

\[
\boxed{\texttt{FACTOR\_GAP\_ARCHITECTURE\_DEAD}}
\]

其含义不是 R1 的 valuation signature 无价值，而是：

\[
\boxed{
\text{exact }2/5\text{-allocation}
+\text{ additive gap}
+\text{ exact gcd}
+\text{ deep decimal congruences}
}
\]

仍不足以产生 orientation drop、dimension drop、fixed-\(S\) support 或 branch closure。

本轮同时获得四个可永久保留的新结构资产：

1. **正因子定理**：\(y>\rho>0\)，所以 \(0<L<R\)；
2. **exact gcd 定理**：\(\gcd(L,R)=2\gcd(y,\rho)\)；
3. **odd common-prime destination**：\(\gcd(y,\rho)\mid\Psi_K(G)\)；
4. **deep decimal-unit law**：R1 的 mod-10 结论提升到随 \(g-k\) 增长的 \(2\)-、\(5\)-幂同余。

但最关键的 negative theorem 是：

\[
\boxed{
\text{四个 orientation 在上述全部 factor-gap necessary constraints 下仍各自存在无限 CRT-lift pseudo-family.}
}
\]

并且如果进一步把 **full exact \(\eta\)** 代入 orientation-specific 参数化，得到的二次方程判别式精确回到

\[
y^2\quad\text{或}\quad(20y)^2.
\]

即：

\[
\boxed{
\texttt{FULL\_ETA\_PARAMETERIZATION=ORIGINAL\_SQUARE\_CONDITION\_RETURN}.
}
\]

所以本轮没有把原 conic 降成新的 fixed Thue–Mahler / fixed \(S\)-unit / fixed exponential equation。

机器可读总状态：

```text
Q1_BRANCH_CLOSED = NO
ORIENTATION_COUNT_BEFORE = 4
ORIENTATION_COUNT_AFTER = 4
FIXED_SOURCE_CASES = 24
COEFFICIENT_TEMPLATES_AFTER_d_COMPRESSION = 12
ORIENTATION_COEFFICIENT_TEMPLATES = 48
FIXED_S_SUPPORT = NO
DIMENSION_DROP = NO
FIXED_OBJECT = NO
FINAL_VERDICT = FACTOR_GAP_ARCHITECTURE_DEAD
```

---

# 2. R1 Assets Imported

本轮严格继承 R1 的 q=1 negative fixed shell。

\[
K=10^k,\qquad k\in\{1,2,3\},
\qquad
G=10^g,
\qquad
\boxed{g-k\ge2}.
\]

历史 8 个 \((d,\tau)\) pair：

\[
(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1).
\]

因此共有

\[
3\times8=24
\]

个 fixed \((K,d,\tau)\) source cases。

primitive/DCDC：

\[
\boxed{31a+\tau\equiv0\pmod{2K}}.
\]

定义十进制边界缺陷：

\[
\boxed{\rho=a-\frac{\tau G}{10}}.
\]

R1 已证明：

\[
\boxed{\rho>0},
\qquad
\boxed{31\rho+\tau\equiv0\pmod{2K}},
\]

\[
\boxed{\gcd(\rho,10\tau)=1},
\]

以及未经加强的 exact source window：

\[
\boxed{0<\rho<\frac{10-d\tau}{10d}G}.
\]

square condition 已压为：

\[
Y_0=2Ky,
\qquad \gcd(y,10)=1,
\]

\[
\boxed{v_2(y^2-\rho^2)=g},
\qquad
\boxed{v_5(y^2-\rho^2)=g-1},
\]

以及

\[
\boxed{(y-\rho)(y+\rho)=\frac G5\eta},
\qquad \gcd(\eta,10)=1,
\]

\[
\boxed{\eta\equiv\rho\tau\pmod{10}}.
\]

q>1 sparse-\(N_0\) elimination 继续按 R1 冻结为 legacy information class，本轮未重新攻击。

---

# 3. q>1 Route Frozen

本轮没有对

\[
m=BHz-A^2c
\]

或其 binary quadratic discriminant 再做包装。R1 已判定其 square-class 精确回到 old \(N_0\)，不产生新 codimension。

因此本报告以下全部内容只属于 q=1 negative fixed shell。

---

# 4. Exact q=1 Canonical Skeleton

定义

\[
\boxed{L:=y-\rho,\qquad R:=y+\rho}.
\]

则

\[
\boxed{LR=2^g5^{g-1}\eta},
\]

\[
\boxed{R-L=2\rho}.
\]

R1 给出：

\[
\{v_2(L),v_2(R)\}=\{1,g-1\},
\]

\[
\{v_5(L),v_5(R)\}=\{0,g-1\}.
\]

由于实际 live range 有 \(g-k\ge2\) 且 \(k\ge1\)，本轮从一开始就有

\[
\boxed{g\ge3}.
\]

这点消除了 prompt 中 \(g=1,2\) 对 actual historical shell 的技术干扰。

---

# 5. Low-g Endpoint Audit

## 5.1 g=1

不在 historical fixed shell，因为 \(g\ge k+2\ge3\)。

## 5.2 g=2

同样不在 historical fixed shell。

另外，若形式上把 R1 valuation set 外推到 \(g=2\)，则

\[
v_2(L)=v_2(R)=1.
\]

于是

\[
v_2(R-L)\ge2,
\]

但 \(\rho\) 为 odd，故

\[
v_2(2\rho)=1,
\]

矛盾。

所以一般主证明可严格固定在

\[
\boxed{g\ge3}.
\]

---

# 6. Positivity Audit: L and R Are Both Positive

R1 只从 factorization 本身还不能自动排除 \(L\le0\)。本轮直接从 full fixed-\(\tau\) conic 补齐这一点。

将

\[
a=\frac{\tau G}{10}+\rho
\]

代入

\[
Y_0^2=A_2a^2+B_1a+C_0
\]

并减去 \((2K\rho)^2\)，得到

\[
Y_0^2-(2K\rho)^2=C_2\rho^2+C_1\rho+C_0'.
\]

exact coefficients 见独立 lemma 文件；它们均可写成

\[
K^2\cdot(\text{large positive polynomial})
-(\text{much smaller positive polynomial}).
\]

在实际范围 \(K\ge10,G\ge10\) 上三者全部严格正。

特别是常数项含

\[
\boxed{
\Psi_K(G)=16G^4K^2-20G^4+16G^3K^2-52G^3-12G^2K^2-53G^2-8GK^2-30G+4K^2
}.
\]

因此

\[
Y_0^2>(2K\rho)^2.
\]

取

\[
y=\frac{|Y_0|}{2K}>0,
\]

得到

\[
\boxed{y>\rho>0}.
\]

所以：

\[
\boxed{0<L<R}.
\]

这不是 assumption，而是本轮新证明的 sign closure。

**Information Gain:** `STRUCTURAL`。

---

# 7. Four Valuation Orientations

令所有新 quotient 均为 positive ten-unit。

## Orientation A

高 \(2\)-、高 \(5\)-content 同时落在 \(L\)：

\[
\boxed{L=10^{g-1}\ell,\qquad R=2r}.
\]

于是

\[
\boxed{r=\frac G{20}\ell+\rho},
\qquad
\boxed{\eta=\ell r}.
\]

## Orientation B

高 \(2\)-content 在 \(L\)，高 \(5\)-content 在 \(R\)：

\[
\boxed{L=2^{g-1}\ell,\qquad R=2\cdot5^{g-1}r}.
\]

于是

\[
\boxed{5^{g-1}r-2^{g-2}\ell=\rho},
\qquad
\boxed{\eta=\ell r}.
\]

## Orientation C

高 \(5\)-content 在 \(L\)，高 \(2\)-content 在 \(R\)：

\[
\boxed{L=2\cdot5^{g-1}\ell,\qquad R=2^{g-1}r}.
\]

于是

\[
\boxed{2^{g-2}r-5^{g-1}\ell=\rho},
\qquad
\boxed{\eta=\ell r}.
\]

## Orientation D

高 \(2\)-、高 \(5\)-content 同时落在 \(R\)：

\[
\boxed{L=2\ell,\qquad R=10^{g-1}r}.
\]

于是

\[
\boxed{\ell=\frac G{20}r-\rho},
\qquad
\boxed{\eta=\ell r}.
\]

因此真正的四个 arithmetic shapes 已经完全显式化。

---

# 8. Immediate Orientation Deaths

结论：

\[
\boxed{\textbf{NONE}}.
\]

## 8.1 2-adic difference

\[
v_2(R-L)=v_2(2\rho)=1.
\]

因为 \(g\ge3\)，两因子的 \(2\)-adic valuations 是不相等的 \(1,g-1\)，ultrametric rule 正好给 minimum \(1\)。四个 orientation 全部兼容。

## 8.2 5-adic difference

\[
v_5(R-L)=0.
\]

两因子的 valuations 是不相等的 \(0,g-1\)，同样全部兼容。

## 8.3 sign

本轮已证明 \(0<L<R\)，所以没有负因子 branch；但四个 positive orientations 都保留。

因此：

```text
VALUATION_ORIENTATION_COLLAPSE = NO
ORIENTATION_DROP = 0
```

**Information Gain:** difference-valuation 本身为 `ZERO` beyond consistency；positivity 为 `STRUCTURAL`。

---

# 9. Exact gcd Analysis

令

\[
h:=\gcd(y,\rho).
\]

因为 \(y,\rho\) 都是 odd，除以 \(h\) 后得到一对互素 odd 数。

因此

\[
\boxed{\gcd(L,R)=2h}.
\]

从而

\[
\boxed{v_2(\gcd(L,R))=1},
\qquad
\boxed{v_5(\gcd(L,R))=0}.
\]

并且四个 orientation 中都精确有

\[
\boxed{\gcd(\ell,r)=h}.
\]

所以

\[
\boxed{h^2\mid\eta}.
\]

这回答了 prompt B3：

\[
D=\gcd(L,R)
\]

不是任意 moving decimal gcd；其 \(2/5\)-part 完全冻结为

\[
\boxed{D=2\times(\text{odd 5-unit}).}
\]

但 odd part 仍可移动。

**Information Gain:** `STRUCTURAL`。

---

# 10. Odd-Prime Support Audit

本轮确实找到一个 source-forced odd-prime destination。

若

\[
p\mid h,
\]

则 \(p\nmid10KG\tau\)。在 full conic 模 \(p\) 下，\(y\equiv\rho\equiv0\)，故

\[
a\equiv\frac{\tau G}{10}\pmod p.
\]

exact specialization 得

\[
0\equiv\frac{G^2\tau^2}{100}\Psi_K(G)\pmod p.
\]

因此

\[
\boxed{p\mid\Psi_K(G)},
\]

甚至

\[
\boxed{h\mid\Psi_K(G)}.
\]

三种 \(K\) 的 polynomial 为：

\[
\Psi_{10}=1580G^4+1548G^3-1253G^2-830G+400,
\]

\[
\Psi_{100}=159980G^4+159948G^3-120053G^2-80030G+40000,
\]

\[
\Psi_{1000}=15999980G^4+15999948G^3-12000053G^2-8000030G+4000000.
\]

这是本轮最接近 task D 的正结果：odd common primes 确实被送进了一个 source polynomial。

但：

\[
\boxed{\Psi_K(10^g)\text{ 的 prime support 随 }g\text{ 移动}.}
\]

所以没有得到

\[
\operatorname{Supp}(\eta)\subseteq S
\]

with fixed finite \(S\)。

正确 verdict：

```text
ODD_COMMON_PRIME_DESTINATION = PROVED
ODD_PRIME_SUPPORT_CONTROLLED_FIXED_S = NO
```

不能合法启动 fixed Thue–Mahler / fixed \(S\)-unit theorem。

---

# 11. Additive Gap and Decimal-Core Collision

## 11.1 Same-core orientations A/D

A：

\[
10^{g-1}\ell+2\rho=2r.
\]

D：

\[
2\ell+2\rho=10^{g-1}r.
\]

这确实形成一个 huge decimal core 与 small gap 的 nearest-multiple picture。

但它没有 size contradiction：另一个 quotient 可随 core 一起线性增长。

例如 A 直接给

\[
r=\frac G{20}\ell+\rho.
\]

这不是“两个互相独立的大 lattice 点必须靠得太近”，而是一个 quotient 被 gap **定义**出来。

D 同理。

## 11.2 Split-core orientations B/C

B：

\[
5^{g-1}r-2^{g-2}\ell=\rho.
\]

C：

\[
2^{g-2}r-5^{g-1}\ell=\rho.
\]

由于

\[
\gcd(2^{g-2},5^{g-1})=1,
\]

每一个都是标准一维 affine lattice，而不是 sparse impossible lattice。

所以 direct size separation、nearest multiple、generic lattice spacing 三个版本都没有产生 global contradiction。

这也解释了为什么本轮禁止重新包装 old root-lattice gap 是正确的：这里的 lattice spacing 在 orientation 层已经被 exact linear equation 吸收。

---

# 12. Deep Decimal-Core Law

R1 只在主报告里使用了

\[
\eta\equiv\rho\tau\pmod{10}.
\]

本轮重新读取 coefficient valuation table 后可提升为：

\[
\boxed{e_2:=g-k-1\ge1},
\]

\[
\boxed{e_5:=g-k+\min(k,2)-1\ge2}.
\]

然后

\[
\boxed{\eta\equiv\rho(\tau-10\rho)\pmod{2^{e_2}}},
\]

\[
\boxed{\eta\equiv\rho(\tau-10\rho)\pmod{5^{e_5}}}.
\]

这不是新 modulus hunting；它直接来自 R1 的 unique-lowest coefficient proof。

### A

因为

\[
r-\rho=\frac G{20}\ell
\]

已含足够深的 \(2/5\)-content，所以

\[
r\equiv\rho
\]

modulo both deep powers，进而

\[
\boxed{\ell\equiv\tau-10\rho}
\]

modulo both deep powers。

### D

同理：

\[
\boxed{r\equiv10\rho-\tau}
\]

modulo both deep powers。

### B/C

一个 prime-power condition 固定 one-parameter gap solution 的 \(2\)-adic residue，另一个固定其 \(5\)-adic residue。由于两个模数互素，CRT 总能合并。

因此这个真正增强的 decimal law 仍没有 orientation death。

**Information Gain:** `STRUCTURAL`，但不是 `ORIENTATION_DROP`。

---

# 13. Orientation-Specific Last-Digit Laws

作为 deep law 的最低 decimal shadow，可写成：

### A

\[
\boxed{r\equiv\rho\pmod{10}},
\qquad
\boxed{\ell\equiv\tau\pmod{10}}.
\]

### D

\[
\boxed{\ell\equiv-\rho\pmod{10}},
\qquad
\boxed{r\equiv-\tau\pmod{10}}.
\]

### B

\[
\ell\equiv-\rho\,2^{-(g-2)}\pmod5,
\]

\[
r\equiv-\tau\,2^{g-2}\pmod5.
\]

### C

\[
r\equiv\rho\,2^{-(g-2)}\pmod5,
\]

\[
\ell\equiv\tau\,2^{g-2}\pmod5.
\]

由于 quotient 都是 odd，mod-5 unit residue 唯一提升到 odd mod-10 unit residue。

这些 residue laws 全部可实现；没有 local extinction。

---

# 14. Full Exact η Audit: The Route Returns to the Original Square

这是本轮对 task C/G 最重要的 Repair-or-Kill 检查。

设 full conic 给出的 exact quantity 为

\[
E:=\eta.
\]

如果希望“不要只看 support，而直接把 \(E\) 当成固定 RHS”，则四个 orientation 都会得到一个 quotient quadratic。

## A

\[
E=\ell\left(\frac G{20}\ell+\rho\right)
\]

即

\[
G\ell^2+20\rho\ell-20E=0.
\]

判别式：

\[
\Delta_A=400\rho^2+80GE
=400\left(\rho^2+\frac G5E\right)
=(20y)^2.
\]

## D

同样得到

\[
\Delta_D=(20y)^2.
\]

## B

令

\[
P=2^{g-2},\qquad Q=5^{g-1}.
\]

由 gap 消去 \(r\)：

\[
P\ell^2+\rho\ell-QE=0.
\]

判别式：

\[
\Delta_B=\rho^2+4PQE
=\rho^2+\frac G5E
=y^2.
\]

## C

同理

\[
\Delta_C=y^2.
\]

所以：

\[
\boxed{
\textbf{full exact }\eta\textbf{ 并没有产生新 fixed equation；它精确回到原 square certificate }y.
}
\]

这是一次明确的 Novelty Guillotine：

```text
FULL_ETA_QUADRATIC = REPARAMETERIZATION
NEW_DISCRIMINANT_CLASS = NO
DIMENSION_DROP = NO
```

因此不能把这些 quotient quadratics 包装成新的 Thue / Pell / elliptic breakthrough。

---

# 15. 24 Fixed Cases Compression

历史 24 cases 来自：

\[
K\in\{10,100,1000\}
\]

与 8 个 \((d,\tau)\) pair。

本轮检查 full fixed-\(\tau\) conic 和 factor-gap equations 后发现：

\[
\boxed{d\text{ 不进入 conic/factor coefficients；它只进入 source upper window}.}
\]

相同 \(\tau\) 的 \(d\) groups：

\[
\tau=1:\ d\in\{1,3,7,9\},
\]

\[
\tau=3:\ d\in\{1,3\},
\]

\[
\tau=7:\ d=1,
\qquad
\tau=9:\ d=1.
\]

所以 coefficient-level arithmetic core 从

\[
24
\]

压成

\[
\boxed{3\ K\text{-values}\times4\ \tau\text{-values}=12}
\]

个 moving-\(g\) templates。

乘以四个 orientations，nominal coefficient-orientation templates 为

\[
\boxed{48}.
\]

但 source window 仍保留全部 24 个 \((K,d,\tau)\) instantiations；不能把 d 完全删除。

没有发现合法的 \(\tau\leftrightarrow-\tau\) 或 A↔D symmetry 可以在 \(\rho>0\) negative shell 内进一步商掉。

**Information Gain:** `STRUCTURAL` case compression；不是 fixed-object extraction，因为 \(g,\rho\) 仍移动。

---

# 16. Counterexample Guillotine

本轮对以下核心 conjectures 全部主动做了反例/伪族压力测试。

## Conjecture A

> huge decimal core 自动与 small gap 冲突。

**FALSE.**

A/D 直接有一自由 quotient；B/C 是一维 affine lattice。

## Conjecture B

> 四个 valuation orientation 中至少一个被 exact difference valuation 自动杀掉。

**FALSE.**

\(g\ge3\) 时 ultrametric minimum 与全部四个 orientation 完全一致。

## Conjecture C

> deep \(\eta\) congruence 会杀掉 split orientation。

**FALSE.**

B/C 中 \(2\)-adic 与 \(5\)-adic要求分别固定 exact gap 参数的两个互素 residue，CRT 产生无限 lift。

## Conjecture D

> odd common primes 会落入 fixed finite support。

**FALSE in the required fixed-S sense.**

真正定理是

\[
h\mid\Psi_K(10^g),
\]

但 RHS 的 prime support 随 \(g\) 移动。

## Strong computational certificate

本轮脚本对全部

\[
24\times4=96
\]

个 source-case/orientation combinations 构造了 exact integer **necessary-skeleton witnesses**，同时满足：

- source DCDC residue for \(\rho\)；
- exact source upper window；
- \(\gcd(\rho,10\tau)=1\)；
- exact orientation valuations；
- \(R-L=2\rho\)；
- deep \(2\)- and \(5\)-adic \(\eta\) congruences；
- \(\eta=\ell r\)；
- \(h=\gcd(\ell,r)=1\)，因此 odd-prime destination theorem 也被 vacuously satisfied。

这 **不是** 96 个原问题解；它们故意不宣称满足 full conic。它们的证明用途是：

\[
\boxed{
\text{当前从 valuation + gap + gcd + deep decimal law 抽出的全部 necessary constraints 仍允许全部四类。}
}
\]

因此不能继续把 factor-gap 本身当作 closure engine。

---

# 17. Heavy-Theorem Transfer Attempts

## 17.1 Thue–Mahler

失败原因：没有 fixed binary form with fixed \(S\)-supported RHS。full exact \(\eta\) 一代回，判别式就是 old \(y^2\)。

```text
THUE_MAHLER_TRANSFER = NOT_LEGAL
```

## 17.2 S-unit

失败原因：\(\ell,r\) 不是 fixed multiplicative group elements；odd support 没有固定。

```text
S_UNIT_TRANSFER = NOT_LEGAL
```

## 17.3 Catalan / Pillai / generalized Fermat

A/D 的

\[
10^{g-1}\ell-2r=\pm2\rho
\]

没有把 \(\ell,r,\rho\) 冻结成 perfect powers 或 fixed divisors；B/C 同理。

```text
EXPONENTIAL_DIOPHANTINE_TRANSFER = NO_FIXED_OBJECT
```

## 17.4 Elliptic / hyperelliptic

orientation-specific quotient quadratic genus 0 且判别式回到 old square；没有新 genus-one object。

```text
ELLIPTIC_TRANSFER = NO_NEW_CURVE
```

## 17.5 Pell/norm

历史 R15 已经把 q=1 negative 写成 24 exact residue-constrained Pell/norm orbit problems。factor-gap 参数化没有进一步固定其 field/order；full-eta 回返说明本轮没有生成比 R15 norm equation 更低维的新 norm object。

所以本轮不重复启动 generic Pell orbit analysis。

---

# 18. Surviving Arithmetic Templates

最终回答用户要求的两个计数：

## 18.1 四个 valuation branches 最后剩几个？

\[
\boxed{4\to4}.
\]

没有 orientation drop。

## 18.2 24 fixed cases 最后剩多少真正不同 arithmetic templates？

分两层回答：

- source-window 层：仍然 \(\boxed{24}\) 个 \((K,d,\tau)\) instantiations；
- coefficient/factor arithmetic 层：d 只控制 window，因此压成 \(\boxed{12}\) 个 \((K,\tau)\) moving templates；
- 再乘 orientation：\(\boxed{48}\) 个 coefficient-orientation templates。

它们都不是 fixed finite equations，因为 \(g\) 与 \(\rho\) 继续移动。

---

# 19. Information Gain Ledger

| Result | Score | Comment |
|---|---|---|
| historical \(g\ge3\) endpoint cleanup | `FILTER` | removes formal endpoint noise only |
| \(y>\rho>0\), hence \(0<L<R\) | `STRUCTURAL` | closes sign ambiguity |
| four explicit quotient templates | `STRUCTURAL` | exact canonicalization |
| difference valuation audit | `ZERO` | kills no orientation |
| \(\gcd(L,R)=2\gcd(y,\rho)\) | `STRUCTURAL` | exact gcd shape |
| \(h\mid\Psi_K(G)\) | `STRUCTURAL` | real odd-prime destination |
| fixed-S support | `ZERO` | not obtained |
| deep \(\eta\) congruence | `STRUCTURAL` | stronger than R1 mod10 |
| deep congruence orientation drop | `ZERO` | CRT absorbs it |
| 24→12 coefficient-template compression | `STRUCTURAL` | d survives only in window |
| full-eta quotient quadratic | `ZERO` novelty | exact return to old square |
| dimension drop | `ZERO` | none |
| fixed object | `ZERO` | none |
| q1 branch closure | `ZERO` | not achieved |
| counterexample guillotine | `STRUCTURAL` negative theorem | kills the architecture, not the branch |

因此最高新信息等级没有达到 `ORIENTATION_DROP`、`DIMENSION_DROP`、`FIXED_OBJECT` 或 `BRANCH_CLOSURE`。

---

# 20. Final q=1 Verdict

\[
\boxed{\texttt{Q1\_BRANCH\_CLOSED=NO}}
\]

\[
\boxed{\texttt{FINITE\_FACTOR\_TEMPLATES\_EXTRACTED=NO}}
\]

\[
\boxed{\texttt{VALUATION\_ORIENTATION\_COLLAPSED=NO}}
\]

\[
\boxed{\texttt{ODD\_PRIME\_SUPPORT\_CONTROLLED=NO\ (fixed\ S)}}
\]

\[
\boxed{\texttt{FACTOR\_GAP\_DIMENSION\_DROP=NO}}
\]

最终：

\[
\boxed{\texttt{FACTOR\_GAP\_ARCHITECTURE\_DEAD}}
\]

精确死因：

> Exact valuation allocation 确实把 square condition 分成四个 rigid decimal shapes；但 additive gap 在每个 shape 中只产生一条一维 affine relation。R1 coefficient expansion 能进一步给 deep decimal congruences，full conic 还能把 odd common gcd 送入 \(\Psi_K(G)\)。然而 deep congruences 可被 CRT lift 全部吸收，odd destination 是 moving support，而 full exact \(\eta\) 一代回 quotient equation，其判别式精确等于原来的 \(y^2\) / \((20y)^2\)。因此没有新 codimension。

---

# 21. R3 Strategic Consequence

R3 不应继续：

- 细化四个 orientation 的更多末位；
- 扫描更多 modulus；
- generic nearest-multiple gap；
- 继续试图把 \(\eta\) 变成 S-unit 而没有新 fixed-support theorem；
- 把 orientation-specific quadratic 当成新 curve。

q=1 若继续，必须回到一个**独立于本轮 factor-gap 回返类**的约束。

当前最值得保留的两个接口是：

1. historical fixed-\(\tau\) Pell/norm orbit + source progression/window；
2. 新的 odd common-prime destination
   \[
   h\mid\Psi_K(10^g)
   \]
   与 historical Gaussian support / norm data 做真正 independent collision。

如果下一轮不能把 \(\Psi_K(10^g)\) 的 moving support 与另一独立 source quantity 形成 resultant/gcd/fixed-support collision，则应完全离开 odd-prime allocation，转攻 R15 norm orbit 的 power-of-ten incidence。

---

# 22. Generated Artifact Index

主报告：

```text
/mnt/data/Fourth_85_R2_Decimal_Core_Factor_Gap.md
```

独立 lemma package：

```text
/mnt/data/Fourth_85_R2_Factor_Gap_Lemmas.md
```

计算目录：

```text
/mnt/data/Fourth_85_R2_computation/
```

其中实际生成并执行/写出的核心文件：

```text
r2_factor_gap_audit.py
orientation_table.tsv
counterexample_skeleton_witnesses.tsv
modular_orientation_compatibility.tsv
modular_search_summary.txt
symbolic_factorizations.txt
r2_certificate.txt
fixed_case_compression.tsv
deep_eta_congruence.txt
```

未生成：

```text
Fourth_85_q1_Closure_Certificate.md
```

原因：

\[
\boxed{q=1\text{ remains OPEN}.}
\]
