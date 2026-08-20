# Fourth 85 · R1 — Fixed-Object Extraction Audit × Valuation-Signature Compression × Sparse Elimination

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — \(J=2\)  
**Round:** 第四个八五计划 · R1  
**Global completion criterion:** \(J=2\Rightarrow\varnothing\)

---

# 1. Executive Verdict

\[
\boxed{\textbf{J2 STATUS = OPEN}}
\]

本轮没有证明

\[
J=2\Longrightarrow\varnothing.
\]

也没有把整个 \(J=2\) moving family 压成有限个 fixed Thue–Mahler / fixed curve / fixed recurrence 对象。

本轮主 verdict 为：

\[
\boxed{\texttt{VALUATION\_SIGNATURE\_FINITE\_BRANCHING\_ACHIEVED}}
\]

同时必须并列写明：

```text
GLOBAL_FIXED_OBJECT_EXTRACTED = NO
GLOBAL_DIMENSION_DROP = NO
Q_GT_1_SPARSE_ELIMINATION = OLD_N0_SQUARECLASS_RETURNS
Q1_NEGATIVE_NEW_SIGNATURE = PROVED
INFORMATION_GAIN = STRUCTURAL
```

本轮真正的新结果位于历史 \(q=1\) negative 24 fixed cases：引入十进制边界缺陷

\[
\boxed{\rho:=a-\frac{\tau G}{10}}
\]

后，负支条件、DCDC 与 fixed-\(\tau\) conic 同时发生刚性压缩，并最终得到：

\[
\boxed{
Y_0=2K y,
\qquad \gcd(y,10)=1,
}
\]

以及 exact valuation signature

\[
\boxed{
 v_2(y^2-\rho^2)=g,
 \qquad
 v_5(y^2-\rho^2)=g-1.
}
\]

等价地：

\[
\boxed{
(y-\rho)(y+\rho)=\frac{G}{5}\,\eta,
\qquad \gcd(\eta,10)=1,
}
\]

并且还有 next decimal-unit law

\[
\boxed{
\eta\equiv \rho\tau\pmod{10}.
}
\]

因此 square condition 被压成恰好四个 \((2,5)\)-valuation allocation branches。这不是普通 residue filter；它冻结了乘法分解的 valuation shape。但由于 \(\eta\) 的 odd-prime support 目前没有被固定，所以尚未进入合法的 Thue–Mahler / \(S\)-unit theorem。

另一方面，在 central regular \(q>1\) negative shell 中，本轮找到一个很自然的 sparse elimination：

\[
\boxed{m=BH z-A^2c.}
\]

它把 \((c,z)\) 双向换成 \((c,m)\)，并把 root-square condition 化为一个 q-free binary quadratic form。然而其 discriminant 精确为

\[
\boxed{
(2GA(GA+1))^2N_0,
}
\]

所以它只是 old \(N_0\) square-class 的重新出现，不产生新 codimension。按 Novelty Guillotine，本路线必须标记：

\[
\boxed{\texttt{LEGACY\_INFORMATION\_CLASS}}.
\]

因此 R1 的结论不是“fixed-object extraction 已完成”，而是：

\[
\boxed{
\text{global fixed-object route failed in the regular }q>1\text{ chart,}
\quad
\text{but }q=1\text{ gained a new finite valuation template.}
}
\]

---

# 2. Historical Assets Imported

本轮按“永久数学资产 / 已死证明架构”分离原则恢复以下历史层。

## 2.1 J2 determinant skeleton

在 actual \(J=2\) chart：

\[
G=10^g,\qquad K=10^k,
\]

\[
uq=G+1,
\qquad
A=2u+1,
\qquad
B=2G+q,
\qquad
H=\frac G2.
\]

永久 Bézout identities：

\[
\boxed{qA-B=2},
\qquad
\boxed{uB-GA=1}.
\]

这些是真正 source-proved 的 \(J=2\) identities，不是 general-\(J\) extrapolation。

## 2.2 Central regular PRE_ROOT chart

沿用：

\[
C_3=c,
\qquad
C_2=Ac+H\lambda,
\]

\[
2KC_1=Bz+A\lambda,
\qquad
T=Gz+u\lambda,
\]

以及 sign-unified Euclidean variables

\[
h=qHz-Ac,
\]

\[
m=Ah-Gz,
\]

\[
r=Hh-uc,
\]

negative branch 中

\[
w=GHz-uAc,
\qquad
d_2=uc+Gw.
\]

full root / sphere：

\[
H^2C_1^2+w^2=Td_2.
\]

root quadratic：

\[
AH^2C_1^2-2uKd_2C_1+Aw^2+zd_2=0.
\]

其 discriminant：

\[
\boxed{
\Delta_0
=u^2K^2d_2^2-AH^2(Aw^2+zd_2)=Y^2.
}
\]

## 2.3 Cleared moving square template

令

\[
W=2w=G^2z-2uAc,
\qquad
D=2d_2=GW+2uc,
\]

则历史已得到：

\[
\boxed{
4u^2K^2D^2-AG^2(AW^2+2zD)=16Y^2.
}
\]

## 2.4 Primitive/common-scale source gate

历史 common-scale gate 不是“又一个 congruence”，而是 actual full-word existence：存在 \(U\in\mathbb Z_{>0}\) 使

\[
\gcd(U,V)=1,
\]

并同时满足 third/second digit windows，例如：

\[
\frac G{10}\le Uc<G,
\]

\[
\frac{G^2K}{10}\le UC_2<G^2K.
\]

这仍是 q>1 source realization 的独立非齐次层。

## 2.5 Historical \(q=1\) negative fixed cases

历史 55-R14/R15 已把 \(q=1\) negative branch 压到：

\[
K\in\{10,100,1000\},
\]

\[
t\in\{1,3,7,9\},
\]

以及 8 个 \((d,\tau)\) pairs：

\[
(1,1),(1,3),(3,1),(1,7),(7,1),(1,9),(3,3),(9,1),
\]

其中 \(t=d\tau\)。总计 24 个 fixed \((K,d,\tau)\) infinite cases。

primitive recovery 中：

\[
a_3=da,
\qquad
m=dn,
\qquad
\gcd(a,n)=1,
\]

以及：

\[
\tau=-31a+2Kn,
\]

故 DCDC：

\[
\boxed{31a+\tau\equiv0\pmod{2K}}.
\]

R15 fixed-\(\tau\) dehomogenized conic：

\[
\boxed{
Y_0^2=A_2(G,K)a^2+B_1(G,K,\tau)a+C_0(G,K,\tau).
}
\]

这是本轮 q=1 新攻击的唯一历史起点；本轮不把“24 fixed cases”重新计为新 fixed-object extraction。

## 2.6 Provenance files actually used

核心恢复来源：

- `85_R11_R1_R10_Full_Architecture_Autopsy_and_PhaseI_Freeze.md`
- `85_phaseII_R1_R10_final_architecture_autopsy.md`
- `第三个八五计划_R1_归档.md`
- `85_R1_J2_Terminal_Recompression_and_Minimal_Survivor.md`
- `J2-55-R14-Carry-NextBit-Gaussian-SecondLift-Report.md`
- `J2-55-R15-Spliced-Factor-2Adic-NegativeConic-Report.md`
- `J2-55-R15-certificate.txt`
- `J2-55-R12-q1-GaussianSupport.py`
- `7_15_Audit_Report.md`

---

# 3. Dead Architectures Kept Frozen

以下历史死亡结论继续有效；本轮不以换名字方式重开：

1. floor/carry 本身不能闭合 full root；
2. source-cut second residual = redundant；
3. generic \((2,5)\)-capacity overload architecture 已失败；
4. generic primitive odd-prime allocation 缺少 source-forced load；
5. canonical real-root order / absolute window collision 已被反例穿透；
6. common-\(U\) endpoint jump / generic spacing 不产生 uniform killer；
7. source-conic / root-lattice / full-root quadratic 的多次重参数化不算新 codimension；
8. moving discriminant square-class 已知回到 \(N_0\)；
9. third-85 moving primitive-core / GSYNC / power-orbit incidence 已在 R1 死亡；
10. “没有 coherent cross-fibre section”不能代替逐 fibre 无解。

因此本轮判新标准始终是：

\[
\boxed{
\text{Does the new statement actually remove moving freedom?}
}
\]

---

# 4. Canonical J2 Skeleton and Moving-Parameter Dependency Map

## 4.1 Central regular \(q>1\) shell

可把独立 moving data 分层写成：

### Outer decimal layer

\[
(g,k,u),
\]

其中

\[
G=10^g,
\qquad K=10^k,
\qquad u\mid G+1,
\qquad q=\frac{G+1}{u}.
\]

因此 \(q\) 本身不是在给定 \((G,u)\) 后的独立参数。

### Primitive/root fibre

可以用 \((c,z)\)，或本轮新换成 \((c,m)\)。这是二维 primitive fibre。

### Full-word scale

actual source 还需要 common scale \(U\) / digit-shell realization。

### Square certificate

\(Y\) 是“当前 binary quadratic value 是否为平方”的 certificate；一旦前面的状态固定，\(Y\) 不是新的自由 source coordinate。

因此一个强 theorem 若想真正降维，至少必须杀掉以下之一：

\[
\boxed{
 u,
\quad
\text{one primitive-fibre coordinate},
\quad
U.
}
\]

单独消掉 \(q\) 不计，因为 \(q=(G+1)/u\) 本来就是 derived。

## 4.2 \(q=1\) negative fixed shell

历史 24-case freeze 已经消掉：

- \(q\)；
- \(K\) 的无限移动（只剩三个 fixed values）；
- \(d,\tau\) 的无限移动（只剩 8 fixed pairs）。

每个 fixed case 的主要 moving variables 仍是：

\[
(g,a,Y_0),
\]

其中 \(Y_0\) 是平方 certificate。

本轮将 \(a\) 换成 boundary defect \(\rho\)。这一步冻结 residue shape，但没有消灭 \(g\) 或 \(\rho\)，所以不是 dimension drop。

---

# 5. Valuation-Signature Audit

# 5.1 q>1 verdict

在 regular q>1 shell，现有 \(v_2,v_5\) 资产多数属于：

```text
FILTER
or
LEGACY_INFORMATION_CLASS
```

原因是它们已被历史 root/carry/source-capacity programmes 测试，并没有统一移除 \(u,c,z,U\) 中的任何一个 moving parameter。

本轮没有在 q>1 上重新奖励“新 modulus / 新 residue / 新 bit”。

# 5.2 q=1 decimal-boundary defect

固定一个历史 negative case \((K,d,\tau)\)。写

\[
K=10^k,
\qquad
G=10^g,
\qquad
g-k\ge2.
\]

定义

\[
\boxed{
\rho:=a-\frac{\tau G}{10}.
}
\tag{D1}
\]

因为 \(g-k\ge2\) 且 \(k\ge1\)，\(G/10\) 是整数并且含至少一个完整十进制因子；故 \(\tau G/10\equiv0\pmod{10}\)。历史中 \(a\) 是 ten-unit，因此

\[
\boxed{\gcd(\rho,10)=1.}
\tag{D2}
\]

## 5.3 Negative sign becomes \(\rho>0\)

R15 的 q=1 Gaussian factor：

\[
M=G^3\tau-(10G^2+4G-2)a.
\]

令

\[
A_G:=10G^2+4G-2.
\]

代入 \(a=\tau G/10+\rho\)：

\[
\boxed{
10M
=-(4G^2-2G)\tau-10A_G\rho.
}
\tag{D3}
\]

若 \(\rho>0\)，显然 \(M<0\)。

反之若 \(M<0\)，则

\[
\rho>
-\frac{(4G^2-2G)\tau}{10A_G}.
\]

右端绝对值严格小于 \(0.04\tau<1\)（这里 \(\tau\le9\)）。故整数 \(\rho\ge0\)。若 \(\rho=0\)，则

\[
a=\frac{\tau G}{10}
\]

被 10 整除，与 \(a\) ten-unit 矛盾。因此：

\[
\boxed{
M<0\iff \rho>0.
}
\tag{D4}
\]

这是一个 genuine sign exactization。

## 5.4 Fixed residue class

由 DCDC：

\[
31a+\tau\equiv0\pmod{2K}.
\]

而 \(2K\mid G/10\)（由 \(g-k\ge2\)），所以：

\[
\boxed{
31\rho+\tau\equiv0\pmod{2K}.
}
\tag{D5}
\]

因为 \(\gcd(31,2K)=1\)，每个 fixed \((K,\tau)\) 上 \(\rho\) 落在唯一 residue class modulo \(2K\)。

此外历史 \(\gcd(a,\tau)=1\) 给出：

\[
\boxed{\gcd(\rho,\tau)=1.}
\tag{D6}
\]

源窗口 \(a<G/d\) 给：

\[
\boxed{
0<\rho<\frac{10-d\tau}{10d}G.
}
\tag{D7}
\]

因此 q=1 fixed case 已经被重新写成：

\[
\boxed{
\rho\in \rho_0+2K\mathbb Z,
\qquad
0<\rho<c_{d,\tau}G,
\qquad
\gcd(\rho,10\tau)=1.
}
\]

这冻结了 coefficient/residue shape，但尚未消灭 \(g\) 或 \(\rho\)。

---

# 6. Sparse Elimination Results — q>1

本节只在 central regular q>1 negative chart 内成立，不偷渡到未证明等价的 singular branch。

## 6.1 Exact elimination identity

从

\[
h=qHz-Ac,
\qquad
m=Ah-Gz
\]

得到

\[
m=(AqH-G)z-A^2c.
\]

由 \(qA=B+2\) 与 \(2H=G\)：

\[
AqH-G=BH.
\]

故：

\[
\boxed{
m=BH z-A^2c.
}
\tag{E1}
\]

## 6.2 Exact inverse map

利用 Bézout identity \(uB-GA=1\)，可验证：

\[
\boxed{
z=\frac{2(m+A^2c)}{BG},
}
\tag{E2}
\]

\[
\boxed{
w=\frac{Gm-Ac}{B},
}
\tag{E3}
\]

\[
\boxed{
d_2=\frac{G^2m+c}{B}.
}
\tag{E4}
\]

所以 \((c,z)\leftrightarrow(c,m)\) 在 legal lattice image 上是双向 exact re-coordinate，不是 dimension drop。

## 6.3 q-free binary quadratic

把 (E2)–(E4) 代入

\[
\Delta_0
=u^2K^2d_2^2-AH^2(Aw^2+zd_2)=Y^2,
\]

清掉 \(B^2\) denominator，得到：

\[
\boxed{
Q_{mc}(m,c)=(2BY)^2,
}
\tag{E5}
\]

其中

\[
\boxed{
\begin{aligned}
Q_{mc}
={}&G^2(N_0-1)m^2\\
&+2G(4GK^2u^2-A)mc\\
&+\left(4K^2u^2-GA^3(GA+2)\right)c^2.
\end{aligned}
}
\tag{E6}
\]

注意：\(q\) 在这个 binary form 的 coefficient block 中完全消失。

这看上去像 fixed-object extraction 的好候选，但必须继续做 discriminant guillotine。

## 6.4 Discriminant returns exactly to old \(N_0\)

对 \(Q_{mc}=am^2+bmc+cc^2\)：

\[
\boxed{
 b^2-4ac
 =\left(2GA(GA+1)\right)^2N_0.
}
\tag{E7}
\]

因此 binary form 的 square-class：

\[
\boxed{
[\operatorname{disc}(Q_{mc})]=[N_0].
}
\]

这与历史 75 / first-85 / second-85 对 moving \(N_0\) 的结论完全同一信息类。

**Novelty verdict:**

\[
\boxed{
\texttt{QGT1\_SPARSE\_ELIMINATION=LEGACY\_INFORMATION\_CLASS}.
}
\]

**Information gain:** `ZERO` beyond a cleaner q-free coordinate package.

它可以作为未来计算的好坐标，但不能作为 485-R1 的数学突破。

---

# 7. Square-to-Factorization Results

# 7.1 q>1 root discriminant factorization — legacy

由 \(\Delta_0=Y^2\)：

\[
(uKd_2-Y)(uKd_2+Y)
=AH^2(Aw^2+zd_2).
\]

结合历史 root factor package，可把两因子识别为：

\[
AH^2C_1
\quad\text{与}\quad
2K\lambda^\flat,
\]

其中

\[
\lambda^\flat=ud_2-AMC_1,
\qquad
H^2=2KM.
\]

历史 primitive firewall 给出相应 coprimality，因此这条 factorization 本质上就是旧 \(C_1\lambda^\flat\) package 的 square-language 重写。

结论：

```text
QGT1_SQUARE_FACTORIZATION = LEGACY_INFORMATION_CLASS
```

不得再把它包装成新 Thue–Mahler bridge。

# 7.2 q=1 new decimal-defect square factorization

现在回到 fixed \((K,d,\tau)\) negative cases。

把 (D1) 代入 R15 fixed-\(\tau\) conic，exact symbolic expansion 给：

\[
\boxed{
100\left(Y_0^2-(2K\rho)^2\right)
=G\sum_{j=0}^{5}C_jG^j.
}
\tag{F1}
\]

其中常数系数：

\[
\boxed{
C_0=-80K^2\rho(10\rho-\tau).
}
\tag{F2}
\]

令

\[
31\rho+\tau=2Kn_*.
\]

将 DCDC defect 关系代入其余 coefficients 后，得到以下足够的 exact valuation table（\(K=10^k\)，\(k=1,2,3\)）：

| coefficient | \(v_2\) | \(v_5\) |
|---|---:|---:|
| \(C_0\) | \(2k+4\) exact | \(2k+1\) exact |
| \(C_1\) | \(\ge k+3\) | \(\ge k+\min(k,2)\) |
| \(C_2\) | \(1\) exact | \(1\) exact |
| \(C_3\) | \(0\) exact | \(0\) exact |
| \(C_4\) | \(2\) exact | \(0\) exact |
| \(C_5\) | \(2\) exact | \(1\) exact |

这里 \(C_0\) 的 exactness 来自：\(\rho,\tau\) 都是 ten-unit，因此 \(10\rho-\tau\) 同时是 2-unit 与 5-unit。

## 7.3 Unique lowest decimal valuation term

(F1) 中第 \(j\) 项实际含 \(G^{j+1}/100\)。

对 \(p=2\)，各项 lower valuations 为：

\[
\begin{aligned}
j=0:&\quad g+2k+2,\\
j=1:&\quad \ge2g+k+1,\\
j=2:&\quad 3g-1,\\
j=3:&\quad 4g-2,\\
j=4:&\quad 5g,\\
j=5:&\quad 6g.
\end{aligned}
\]

对 \(p=5\)：

\[
\begin{aligned}
j=0:&\quad g+2k-1,\\
j=1:&\quad \ge2g+k+\min(k,2)-2,\\
j=2:&\quad 3g-1,\\
j=3:&\quad 4g-2,\\
j=4:&\quad 5g-2,\\
j=5:&\quad 6g-1.
\end{aligned}
\]

由于 live range：

\[
\boxed{g\ge k+2},
\]

对 \(p=2,5\)，\(j=0\) 都严格是唯一 lowest-valuation term。因此不存在 cancellation：

\[
\boxed{
 v_2\left(Y_0^2-(2K\rho)^2\right)=g+2k+2,
}
\tag{F3}
\]

\[
\boxed{
 v_5\left(Y_0^2-(2K\rho)^2\right)=g+2k-1.
}
\tag{F4}
\]

## 7.4 Forced decimal valuation of the square root

\((2K\rho)^2\) 的 valuations 为：

\[
v_2=2k+2,
\qquad
v_5=2k.
\]

(F3)/(F4) 的 correction depth 严格更大，所以：

\[
\boxed{v_2(Y_0^2)=2k+2},
\qquad
\boxed{v_5(Y_0^2)=2k}.
\]

平方 valuation 必须为偶数，因此：

\[
\boxed{
v_2(Y_0)=k+1,
\qquad
v_5(Y_0)=k.
}
\tag{F5}
\]

定义

\[
\boxed{Y_0=2Ky.}
\tag{F6}
\]

则

\[
\boxed{\gcd(y,10)=1.}
\tag{F7}
\]

除以 \(4K^2\)：

\[
\boxed{
v_2(y^2-\rho^2)=g,
\qquad
v_5(y^2-\rho^2)=g-1.
}
\tag{F8}
\]

这就是本轮核心新 theorem。

## 7.5 Multiplicative factorization

由 (F8)：

\[
y^2-\rho^2=2^g5^{g-1}\eta=\frac G5\eta,
\]

其中

\[
\boxed{\gcd(\eta,10)=1.}
\]

故：

\[
\boxed{
(y-\rho)(y+\rho)=\frac G5\eta.
}
\tag{F9}
\]

进一步，把 (F1) 除到 normalized quotient：

\[
\eta=\frac{5(y^2-\rho^2)}G
=\frac{\sum C_jG^j}{80K^2}.
\]

由 coefficient valuation gaps，所有 \(j\ge1\) 项在除以 \(80K^2\) 后均为 10 的倍数；而常数项给

\[
\frac{C_0}{80K^2}
=-\rho(10\rho-\tau)
\equiv \rho\tau\pmod{10}.
\]

因此：

\[
\boxed{
\eta\equiv\rho\tau\pmod{10}.
}
\tag{F10}
\]

## 7.6 Exactly four valuation branches

\(y,\rho\) 都为 odd 5-units。

对于 2-adic factorization，\(y-\rho\) 与 \(y+\rho\) 都偶，且其中一个恰有 \(v_2=1\)，另一个承担剩余 \(g-1\)：

\[
\boxed{
\{v_2(y-\rho),v_2(y+\rho)\}
=\{1,g-1\}.
}
\tag{F11}
\]

对于 5-adic factorization，两因子不可能同时被 5 整除；总 valuation 为 \(g-1\)，故：

\[
\boxed{
\{v_5(y-\rho),v_5(y+\rho)\}
=\{0,g-1\}.
}
\tag{F12}
\]

于是只有四个 orientation pairs：

\[
(\epsilon_2,\epsilon_5)\in\{\pm1\}^2,
\]

使：

\[
\boxed{
v_2(y-\epsilon_2\rho)=g-1,
\quad
v_2(y+\epsilon_2\rho)=1,
}
\]

\[
\boxed{
v_5(y-\epsilon_5\rho)=g-1,
\quad
v_5(y+\epsilon_5\rho)=0.
}
\]

这是 finite branching，且不是单纯排除 residue class。

---

# 8. Hidden Recurrence Audit

本轮专门检查“消元后指数是否生成 fixed recurrence”。

## 8.1 q>1

\(N_0\) 对固定 \((G,u)\) 而言随 \(k\) 确有平凡 affine-exponential evolution，因为 \(K^2=100^k\)。但：

1. \(G,u\) 本身跨 fibre 移动；
2. actual source primitive fibre 与 common-\(U\) gate 不由该 recurrence 读取；
3. 第三个八五已证明当前 cross-fibre family organization 不自动增加 codimension。

所以这不是可调用 Lucas/Lehmer primitive-divisor theorem 的 fixed recurrence。

```text
QGT1_FIXED_RECURRENCE = NOT EXTRACTED
```

## 8.2 q=1

固定 \((K,d,\tau)\) 后，\(G=10^g\) 的确只剩一个 exponential base，但 \(\rho\) 仍在一个随 \(G\) 扩张的 arithmetic progression window 中自由移动。没有得到

\[
T_{g+r}=c_1T_{g+r-1}+\cdots+c_rT_g
\]

且 \(T_g\) 同时编码全部 source roots 的 fixed recurrence。

```text
Q1_FIXED_RECURRENCE = NOT EXTRACTED
```

---

# 9. Fixed-Object Candidates

| Candidate | Fixed? | New? | Source-compatible? | Verdict |
|---|---|---|---|---|
| q>1 \(Q_{mc}(m,c)=(2BY)^2\) | coefficients still move with \((G,u,K)\) | no | yes on regular chart | OLD \(N_0\) class |
| q>1 norm after completing square | radicand \(N_0\) moves | no | yes | LEGACY |
| q>1 root factor \(C_1\lambda^\flat\) | moving factors | no | yes | LEGACY |
| q=1 24 fixed \((K,d,\tau)\) conics | finite fixed coefficient templates in \(K,d,\tau\), but still \(G\)-polynomial | historical | yes | HISTORICAL ASSET |
| q=1 defect lattice \(\rho\equiv\rho_0\pmod{2K}\) | fixed modulus per case | **new recentering** | yes | STRUCTURAL |
| q=1 four factor-allocation templates | finite 4 branches | **new** | yes | STRUCTURAL / FINITE BRANCHING |
| q=1 \((y-\rho)(y+\rho)=G\eta/5\) | \(\eta\) odd support not fixed | new | yes | NOT YET S-UNIT |

本轮没有得到符合“finite fixed arithmetic objects + fixed prime support”的 global target。

---

# 10. Heavy-Theorem Applicability Matrix

| Theorem class | Required bridge | R1 status | Can invoke? |
|---|---|---|---|
| Thue / Thue–Mahler | fixed irreducible binary form = fixed \(S\)-unit RHS | q>1 coefficients move；q1 \(\eta\) odd support unfixed | **NO** |
| \(S\)-unit | finitely generated multiplicative group | q1 \(\eta\) only ten-unit, not fixed \(S\)-unit | **NO** |
| Lucas / Lehmer primitive divisor | fixed nondegenerate recurrence | no fixed recurrence | **NO** |
| Baker / linear forms | fixed \(a\alpha^m-b\beta^n=c\) | extra \(u,\rho,U\) move | **NO** |
| fixed elliptic/hyperelliptic curve | finite fixed curves after specialization | not reached globally | **NO** |
| modular method | generalized Fermat fixed exponent shape | not reached | **NO** |
| algebraic norm/class group | fixed number field + fixed prime support | q>1 radicand moves; q1 odd support moves | **NO** |
| computational finite verification | finite survivor set | no global finite set | **NO** as closure |

因此本轮正确行为不是“强行调用大定理”，而是精确记录 activation assumptions 尚缺哪一条。

---

# 11. Counterexample Guillotine

## 11.1 Conjecture A

> \(m=BH z-A^2c\) eliminates one primitive free parameter.

**Killed exactly.**

(E2)–(E4) 给双向 inverse。它只是 lattice re-coordinate。

Verdict：

```text
CONJECTURE_A = FALSE_AS_DIMENSION_DROP
```

## 11.2 Conjecture B

> q disappears from \(Q_{mc}\), so a new q-free fixed-object obstruction has appeared.

**Killed exactly.**

(E7) 给：

\[
\operatorname{disc}(Q_{mc})
=(\text{square})\cdot N_0.
\]

这严格返回 old \(N_0\) square-class。

Verdict：

```text
CONJECTURE_B = LEGACY_REPACKAGING
```

## 11.3 Conjecture C

> q=1 defect factorization is already Thue–Mahler / S-unit.

**Rejected before theorem invocation.**

(F9) 的 \(\eta\) 只满足：

\[
\gcd(\eta,10)=1,
\qquad
\eta\equiv\rho\tau\pmod{10}.
\]

没有证明其 odd-prime support 落在固定 finite set。

Verdict：

```text
CONJECTURE_C = NOT_LEGAL
```

## 11.4 Conjecture D

> exact valuation signature is only another residue filter.

**False.**

它不仅排除 residue：它证明 square root 自身的 exact \(2/5\)-content，并把两个乘法因子的 valuation load 压成四个固定 allocation templates。

Verdict：

```text
CONJECTURE_D = FALSE
SIGNATURE_CLASS = STRUCTURAL_FINITE_BRANCHING
```

---

# 12. Novelty Audit

## 12.1 q>1 sparse elimination

N1 已测试过同信息类？**YES**，moving discriminant / \(N_0\)。  
N2 只是旧信息重坐标？**YES**。  
N3 fixed fibre trick？不是，但无新 codimension。  
N4 读取 moving \(G\)？YES。  
N5 与 full root 联立？YES。  
N6 deep countermodel / old split family 穿透？YES。  
N7 closure potential？当前无。

\[
\boxed{\texttt{NOVELTY=NONE}}.
\]

## 12.2 q=1 boundary defect recentering

N1 旧 q1 R12–R15 是否已有 \(\rho=a-\tau G/10\) 及其 negative equivalence？在恢复档案中未发现。  
N2 是否只是任意坐标？不是：它把 sign boundary 精确化成 \(\rho>0\)，同时把 DCDC 模数变成固定 \(\rho\)-class。  
N3 fixed fibre？在 24 个 fixed template 上 uniform。  
N4 读取 moving \(G\)？YES，通过 decimal boundary。  
N5 与 square conic 联立？YES。  
N6 已被历史 countermodel 穿透？未发现针对该 exact signature 的历史 countermodel。  
N7 closure potential？中等，取决于 odd gcd/support firewall。

\[
\boxed{\texttt{NOVELTY=HIGH\ within\ q1\ fixed\ branch}}.
\]

## 12.3 q=1 valuation signature

这是 R15 fixed-\(\tau\) conic + DCDC + negative boundary defect 的联合后果，不是 R12 Gaussian inert-support theorem 的简单重述。

新信息：

\[
Y_0=2K\cdot(\text{ten-unit}),
\]

\[
(y-\rho)(y+\rho)=G\eta/5,
\]

并且十进制 prime load 只有四种 allocation。

\[
\boxed{\texttt{NOVELTY=HIGH}}.
\]

---

# 13. Information Gain Classification

| Result | Class | Reason |
|---|---|---|
| \(m=BH z-A^2c\) | `ZERO` | 双向可逆重坐标 |
| q-free \(Q_{mc}\) | `ZERO` | discriminant 精确回到 \(N_0\) |
| q1 \(M<0\iff\rho>0\) | `STRUCTURAL` | sign exactization |
| q1 \(\rho\bmod2K\) unique | `STRUCTURAL` | coefficient/residue shape freeze |
| q1 \(v_2(Y_0),v_5(Y_0)\) | `STRUCTURAL` | exact square-root content |
| q1 four factor-allocation branches | `STRUCTURAL` | finite branching, not filter-only |
| global moving freedom removed? | **NO** | \(g,\rho\) remain in q1; \(u\)+2D fibre+\(U\) remain q>1 |
| fixed arithmetic object globally? | **NO** | no fixed prime support / fixed field / fixed recurrence |
| J2 closure | `NO` | open |

因此总分类：

\[
\boxed{
\textbf{Information Gain = STRUCTURAL}.
}
\]

必须直接回答本轮最重要的问题：

\[
\boxed{
\textbf{我们没有真正减少全局 moving freedom 的维数。}
}
\]

但 q1 中把平方的 decimal-prime allocation 从“moving unknown”压成四个 fixed templates，是真实的 finite branching，而不是 `FILTER_ONLY`。

---

# 14. Proof / Partial Proof Package

本轮可正式冻结以下三个 lemma。

## Lemma 1 — q>1 Sparse Recoordinate / N0 Return

在 central regular q>1 negative J2 chart：

\[
m=BH z-A^2c,
\]

且 legal image 上 \((c,z)\leftrightarrow(c,m)\) 双向恢复；square condition 等价于

\[
Q_{mc}(m,c)=(2BY)^2,
\]

其中 (E6)，且

\[
\operatorname{disc}Q_{mc}
=(2GA(GA+1))^2N_0.
\]

所以该 elimination 不产生新 square-class。

## Lemma 2 — q1 Negative Decimal-Defect Lemma

在每个历史 q=1 negative fixed \((K,d,\tau)\) case，定义

\[
\rho=a-\tau G/10.
\]

则：

\[
M<0\iff\rho>0,
\]

\[
31\rho+\tau\equiv0\pmod{2K},
\]

\[
\gcd(\rho,10\tau)=1,
\]

\[
0<\rho<\frac{10-d\tau}{10d}G.
\]

## Lemma 3 — q1 Exact Decimal Valuation Signature

若该 fixed case 还满足 R15 conic square condition，则：

\[
Y_0=2Ky,
\qquad \gcd(y,10)=1,
\]

以及：

\[
v_2(y^2-\rho^2)=g,
\qquad
v_5(y^2-\rho^2)=g-1,
\]

故：

\[
(y-\rho)(y+\rho)=\frac G5\eta,
\qquad
\gcd(\eta,10)=1,
\qquad
\eta\equiv\rho\tau\pmod{10},
\]

并只有四个 \((2,5)\)-valuation orientation branches。

---

# 15. Surviving Obstruction

# 15.1 q>1

fixed-object extraction 的中央 blocker 现在可以更精确地写成：

\[
\boxed{
(G,u,K)
+\text{2D primitive fibre}
+\text{actual common-}U\text{ decimal scale}.
}
\]

所有自然消元只把 root part 压回：

\[
\boxed{N_0\text{ / moving norm / old quadratic class}.}
\]

真正未被消掉的是 source-attached nonhomogeneous decimal scale，而不是缺一个更漂亮的 discriminant formula。

# 15.2 q=1

new factorization 的 blocker 现在非常具体：

\[
\boxed{
\gcd(y-\rho,y+\rho)
\mid2\gcd(y,\rho),
}
\]

而当前尚未证明 \(\gcd(y,\rho)\) 的 odd support 属于固定有限集合。

只要能把 odd common support 固定，(F9) 就有机会进入：

- coprime factor assignment；
- fixed \(S\)-unit；
- Thue–Mahler；
- norm equation with fixed support。

反之，如果可以构造 source-compatible family 让 \(\gcd(y,\rho)\) 吸收任意 moving odd primes，则这条 q1 architecture 应立即处决。

这是一个清晰的 Repair-or-Kill interface。

---

# 16. R2 Decision

本轮不建议把下一轮机械称为“继续 fixed-object extraction”。

q>1 当前坐标的 fixed-object extraction 已被 exact \(N_0\)-return guillotine 杀死。

下一轮最有价值的新接口来自 q1：

\[
\boxed{
\textbf{q=1 Decimal-Defect Factor Allocation × Odd-Support Firewall Repair-or-Kill}
}
\]

唯一中央问题应是：

\[
\boxed{
\textbf{actual source primitiveness / Gaussian support / fixed-}\tau\textbf{ identities}
\Longrightarrow
\textbf{finite odd support for }\gcd(y,\rho)\textbf{ or for }\eta\ ?
}
\]

### Success condition

若证明存在 fixed finite set \(S=S(K,d,\tau)\) 使：

\[
\operatorname{Supp}\gcd(y,\rho)\subseteq S
\]

并进一步把 \(\eta\) 或两个 factors 的 odd support 压到 fixed \(S\)，则下一步立即进入：

\[
\boxed{\text{Thue–Mahler / }S\text{-unit / fixed norm exploitation}.}
\]

### Kill condition

若能证明 source-compatible states 允许 arbitrarily moving odd support，而 four-branch signature 不再增加 codimension，则：

\[
\boxed{\texttt{Q1\_DEFECT\_ARCHITECTURE=DEAD}}.
\]

然后 485 必须回到 q>1 重新选完全不同理论领域；不得继续做 \(N_0\) / root-lattice / common-\(U\) congruence polishing。

---

# 17. Generated Artifact Index

本轮实际生成：

```text
/mnt/data/Fourth_85_R1_Fixed_Object_Extraction.md
/mnt/data/Fourth_85_R1_Lemmas.md

/mnt/data/Fourth_85_R1_computation/qgt1_sparse_elimination.py
/mnt/data/Fourth_85_R1_computation/qgt1_sparse_elimination.txt

/mnt/data/Fourth_85_R1_computation/q1_defect_signature.py
/mnt/data/Fourth_85_R1_computation/q1_defect_signature.txt
/mnt/data/Fourth_85_R1_computation/q1_defect_signature_summary.json
/mnt/data/Fourth_85_R1_computation/q1_defect_cases.tsv

/mnt/data/Fourth_85_R1_computation/result_summary.json
/mnt/data/Fourth_85_R1_computation/execution.log
```

计算只用于 symbolic identity / valuation-support certificate；没有把有限搜索无反例升级成证明。

---

# 18. Terminal Ledger

```text
J2_STATUS = OPEN

R1_MAIN_VERDICT = VALUATION_SIGNATURE_FINITE_BRANCHING_ACHIEVED

GLOBAL_FIXED_OBJECT_EXTRACTED = NO
GLOBAL_DIMENSION_DROP = NO
GLOBAL_MOVING_FREEDOM_REDUCED = NO

Q_GT_1_M_C_RECOORDINATE = PROVED
Q_GT_1_Q_FREE_BINARY_FORM = PROVED
Q_GT_1_BINARY_DISCRIMINANT = SQUARE * N0
Q_GT_1_FIXED_OBJECT_ROUTE = KILLED_BY_OLD_N0_RETURN

Q1_DECIMAL_DEFECT = PROVED
Q1_NEGATIVE_SIGN_EXACTIZATION = PROVED
Q1_FIXED_RESIDUE_DEFECT = PROVED
Q1_Y0_2ADIC_5ADIC_SIGNATURE = PROVED
Q1_FOUR_FACTOR_ALLOCATION_BRANCHES = PROVED
Q1_ETA_LAST_DIGIT = PROVED
Q1_FIXED_S_UNIT_SUPPORT = NOT_PROVED
Q1_THUE_MAHLER = NOT_ACTIVATED

INFORMATION_GAIN = STRUCTURAL
NOVELTY_Q_GT_1 = NONE
NOVELTY_Q1_SIGNATURE = HIGH

R2_DECISION = Q1_DECIMAL_DEFECT_ODD_SUPPORT_REPAIR_OR_KILL
```

最终：

\[
\boxed{
J=2\Rightarrow\varnothing
\quad\textbf{尚未闭合。}
}
\]

但 485-R1 已得到一个可以严格冻结的新接口：

\[
\boxed{
\text{q1 fixed negative conic}
\longrightarrow
\text{decimal boundary defect}
\longrightarrow
\text{exact }(2,5)\text{-factor allocation}
\longrightarrow
\text{four branches}.
}
\]

它是否能继续变成 fixed \(S\)-unit / Thue–Mahler 对象，取决于下一轮能否控制 odd common support。
