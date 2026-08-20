# 三项十进制拼接平方和问题：DD Oriented Tail-Window Campaign

**文件名：** `strict_layer_DD_oriented_tail_window_campaign.md`  
**研究范围：** Strict Layer，仅研究当前开放的 **DD chamber / top DD**  
**本轮等级：**

\[
\boxed{\textbf{SGR-9A — DD CLOSED}}
\]

**最终状态：** 在冻结 SGR-8 与此前 Exact-Lift / DD reduction 的前提下，当前 DD 的唯一开放尖角被严格排除，因此 DD chamber 从 strict-layer frontier 中删除。

本轮真正的 decisive mechanism 不是新的 near-square，也不是恢复旧 Hensel branch，而是：

\[
\boxed{
\text{source orientation}
+\text{source-labelled division}
+\gcd(a_3,b_3)=1
+5\text{-adic double resonance}
\Longrightarrow
\text{quotient-factor valuation overload}.
}
\]

更具体地，SGR-8 的 oriented factors

\[
uv=Nc^2,
\qquad
v-u=2ha_3,
\qquad
b_3=cD
\]

在顶部 DD 中同时强迫

\[
2m_3\le 9S_{12}+9,
\]

而旧顶部区间又强迫

\[
2m_3\ge 10S_{12}+22.
\]

二者直接矛盾。

所有陈述按 **PROVED / DERIVED / HEURISTIC / COMPUTATIONAL EVIDENCE / FAILED / OPEN** 分类。

---

# 1. Source audit 与冻结输入

本轮重点依赖并交叉核对：

- `strict_layer_DD_orientation_recovery_campaign.md`；
- `strict_layer_DD_source_phase_information_audit.md`；
- `strict_layer_DD_post_deflation_campaign.md`；
- `strict_layer_DD_error_closure_campaign.md`；
- `strict_layer_moving_core_square_spacing_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`。

本轮不重新研究：

- Hensel branch naming；
- source orientation bit 是否为 gauge；
- resultant；
- old ordinary square-spacing；
- projected phase CRT；
- source higher Hensel digits。

这些对象的当前地位均继承前轮结论。

## 1.1 SGR-8 orientation theorem

**PROVED — inherited.**

对任何当前顶部 DD 的合法 original candidate：

\[
\boxed{
\omega_{\rm src}=+1,
\qquad
F_-=\Lambda D_0J^\sharp,
\qquad
F_+=\Lambda D_0K^\sharp,
\qquad
J^\sharp<K^\sharp.
}
\]

Vieta 共轭支恢复出负的第三分子，因此不是原题合法 candidate。

同时已有 exact tail recovery：

\[
\boxed{
2a_3
=
\frac{F_+}{\kappa}
-
\frac{F_-}{\kappa+2G}.
}
\]

orientation 从本轮起不再是变量，而是 theorem。

---

# 2. DD 主变量与 oriented source divisors

统一记

\[
S:=S_{12}=m_1+m_2,
\]

\[
Q:=Q_{12}=b_1 10^{m_2}+b_2,
\]

\[
G:=b_1b_2,
\]

\[
N:=\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
A:=A_{12}=a_1 10^{n_2}+a_2,
\]

\[
C:=10^{d_3}A,
\qquad
T:=10^{m_3},
\]

以及尾权

\[
\boxed{
\kappa=\frac{TQG}{b_3}
\in\mathbf Z_{>0},
\qquad
QG<\kappa\le10QG.
}
\]

定义

\[
\boxed{h:=\gcd(\kappa,G)},
\]

\[
\boxed{
A_\kappa:=\frac{\kappa}{h},
\qquad
D:=\frac Gh,
\qquad
B_\kappa:=\frac{\kappa+2G}{h}=A_\kappa+2D.
}
\]

于是

\[
\gcd(A_\kappa,D)=1,
\]

且

\[
\boxed{
\gcd(A_\kappa,B_\kappa)
=
\gcd(A_\kappa,2)
\in\{1,2\}.
}
\]

此外

\[
\frac{B_\kappa}{A_\kappa}
=
1+\frac{2G}{\kappa}
<1+\frac2Q.
\]

**PROVED — inherited from SGR-8.**

source-labelled divisibility 为

\[
\boxed{
B_\kappa\mid F_-,
\qquad
A_\kappa\mid F_+.
}
\]

且 denominator normalization 给出

\[
A_\kappa\mid TQ.
\]

因此定义

\[
\boxed{
c:=\frac{TQ}{A_\kappa}\in\mathbf Z_{>0}.
}
\]

由 \(\kappa b_3=TQG\) 立即得到

\[
\boxed{b_3=cD.}
\]

---

# 3. Canonical oriented factor system

定义

\[
\boxed{
u:=\frac{F_-}{B_\kappa}\in\mathbf Z_{>0},
\qquad
v:=\frac{F_+}{A_\kappa}\in\mathbf Z_{>0}.
}
\]

> 为避免与其他报告的公共尺度字母混淆，本文件的 \(u,v\) 始终只表示上述 oriented quotient factors。

由旧 factor product

\[
F_-F_+
=N\,TQ(TQ+2b_3)
\]

以及

\[
TQ=A_\kappa c,
\qquad
TQ+2b_3
=c(A_\kappa+2D)=cB_\kappa,
\]

得到

\[
\boxed{uv=Nc^2.}
\tag{3.1}
\]

另一方面 SGR-8 已证明

\[
t:=\frac\mu\nu=\frac uc,
\qquad
\frac Nt=\frac vc,
\]

从球面 gap recovery 得

\[
\boxed{v-u=2ha_3.}
\tag{3.2}
\]

所以

\[
\boxed{
a_3=\frac{v-u}{2h},
\qquad
u<v.
}
\tag{3.3}
\]

以及

\[
\boxed{b_3=cD.}
\tag{3.4}
\]

因此 current top DD 的 oriented tail-native system 是

\[
\boxed{
uv=Nc^2,
\qquad
v-u=2ha_3,
\qquad
b_3=cD,
\qquad
\gcd(a_3,cD)=1.
}
\tag{3.5}
\]

**状态：PROVED / inherited + exact derivation.**

---

# 4. 第三块既约性转成 exact gcd identities

原题要求

\[
\gcd(a_3,b_3)=1.
\]

由 \(b_3=cD\)：

\[
\boxed{\gcd(a_3,cD)=1.}
\tag{4.1}
\]

代入 \(v-u=2ha_3\)，得到两个精确 gcd identity。

## 4.1 Difference–denominator gcd

**PROVED.**

\[
\boxed{
\gcd(v-u,cD)
=
\gcd(2h,cD).
}
\tag{4.2}
\]

因为 \(\gcd(a_3,cD)=1\)，对任意整数 \(M\)：

\[
\gcd(Ma_3,cD)=\gcd(M,cD).
\]

取 \(M=2h\) 即得。

## 4.2 完整 scaled gcd

**PROVED.**

\[
\boxed{
\gcd(v-u,2hcD)=2h.
}
\tag{4.3}
\]

因为

\[
\gcd(2ha_3,2hcD)
=2h\gcd(a_3,cD)
=2h.
\]

特别地，对任意素数 \(p\mid cD\)：

\[
\boxed{
v_p(v-u)=v_p(2h).
}
\tag{4.4}
\]

这条 valuation equality 后面在 \(p=5\) 处成为 closure 的核心。

---

# 5. Canonical common-gcd decomposition

令

\[
\boxed{d:=\gcd(u,v).}
\]

则

\[
d\mid(v-u)=2ha_3,
\qquad
d^2\mid uv=Nc^2.
\]

单独从这两式不能证明 \(d\mid2h\)。真正正确的结论如下。

## 5.1 Denominator-supported common part

定义 \(d_{\rm den}\) 为 \(d\) 中所有素因子属于 \(\operatorname{supp}(cD)\) 的最大因子。

由 (4.4)，若 \(p\mid cD\)，则

\[
v_p(d)\le v_p(v-u)=v_p(2h).
\]

因此

\[
\boxed{d_{\rm den}\mid2h.}
\tag{5.1}
\]

## 5.2 Prefix-square common part

令

\[
\boxed{d_N:=d/d_{\rm den}.}
\]

则

\[
\gcd(d_N,cD)=1.
\]

因为 \(d_N^2\mid Nc^2\) 且 \(d_N\) 与 \(c\) 互素：

\[
\boxed{d_N^2\mid N.}
\tag{5.2}
\]

所以

\[
\boxed{
\gcd(u,v)
=
 d_{\rm den}d_N,
\qquad
 d_{\rm den}\mid2h,
\qquad
 d_N^2\mid N,
\qquad
\gcd(d_N,cD)=1.
}
\tag{5.3}
\]

**状态：PROVED.**

这精确定位了为什么“\(\gcd(u,v)\mid2h\)”过强：所有未被第三分母既约性消灭的 common factor freedom，被压缩到前缀二平方和 \(N\) 的 square supply。

---

# 6. 非异常 \(c\)-prime 的整块单侧分配

设

\[
p^e\parallel c,
\qquad
p\nmid2h.
\]

因为 \(p\mid b_3\)，由第三块既约性

\[
p\nmid a_3.
\]

若同时 \(p\mid u\) 与 \(p\mid v\)，则

\[
p\mid(v-u)=2ha_3,
\]

与 \(p\nmid2ha_3\) 矛盾。

所以二者恰有一边含 \(p\)。而

\[
v_p(uv)=v_p(N)+2e.
\]

故总的 \(p\)-power 必须完整落到同一侧：

\[
\boxed{
\{v_p(u),v_p(v)\}
=
\{0,\ v_p(N)+2e\}.
}
\tag{6.1}
\]

**状态：PROVED — Canonical nonexceptional prime-allocation theorem.**

定义 exceptional part

\[
c_0:=\prod_{\substack{p^e\parallel c\\p\mid2h}}p^e,
\]

以及

\[
c_*=c/c_0.
\]

按 source orientation 唯一分配

\[
c_-=\prod_{\substack{p^e\parallel c_*\\p\mid u}}p^e,
\qquad
c_+=\prod_{\substack{p^e\parallel c_*\\p\mid v}}p^e.
\]

则

\[
\boxed{
c=c_0c_-c_+,}
\]

\[
\boxed{
\gcd(c_-,c_+)=1,
\qquad
\gcd(c_-c_+,2h)=1,
}
\]

并且

\[
\boxed{c_-^2\mid u,
\qquad
c_+^2\mid v.}
\tag{6.2}
\]

更强地，\(p\mid c_-\) 时 \(N\) 的全部该 \(p\)-power 也被拖入 \(u\)-side；\(p\mid c_+\) 时对称。

这已经是 SGR-9C 意义上的 canonical factor-splitting breakthrough；但本轮随后得到更强的 full closure，因此最终等级升级为 SGR-9A。

---

# 7. 一个不能成立的过强猜想：\(\gcd(u,v)\mid2h\)

本轮曾优先尝试

\[
\gcd(u,v)\mid2h.
\]

它对 abstract terminal system 是假的。

取

\[
h=c=D=1,
\qquad
u=5,
\qquad
v=25,
\]

则

\[
uv=125,
\qquad
v-u=20=2\cdot1\cdot10.
\]

所以可取

\[
N=125=2^2+11^2,
\qquad
a_3=10,
\qquad
b_3=1.
\]

此时

\[
\gcd(a_3,b_3)=1,
\]

但

\[
\gcd(u,v)=5\nmid2.
\]

因此：

\[
\boxed{
uv=Nc^2,
\quad
v-u=2ha_3,
\quad
\gcd(a_3,cD)=1,
\quad
N\text{ 为两平方和}
}
\]

本身仍不足以推出 \(\gcd(u,v)\mid2h\)。

**状态：FAILED AS A GENERAL LEMMA.**

Section 5 的 \(d_{\rm den}d_N\) 分解是正确替代物。

---

# 8. Squarefree splitting：得到结构，但不是 finite state

将

\[
d=\gcd(u,v),
\qquad
u=dx,
\qquad
v=dy,
\qquad
\gcd(x,y)=1.
\]

则

\[
xy=\frac{Nc^2}{d^2}=:M_*.
\]

任意正整数可唯一写成 squarefree part 乘平方，因此存在

\[
x=rX^2,
\qquad
y=sY^2,
\]

其中 \(r,s\) squarefree，且因 \(x,y\) 互素：

\[
\gcd(rX,sY)=1.
\]

差式变成

\[
\boxed{
d(sY^2-rX^2)=2ha_3.}
\tag{8.1}
\]

另外因为

\[
N=(a_1b_2)^2+(a_2b_1)^2,
\]

两平方和定理说明 \(\operatorname{sqf}(N)\) 不含任何 \(3\bmod4\) 素数。

但这并没有把 \((r,s)\) 压成固定有限状态：

- \(N\) 随 moving prefix 变化；
- 任意多个新的 \(1\bmod4\) 素数仍可进入 \(\operatorname{sqf}(N)\)；
- primitive-profile 中 \(N\) 本身还含有自然 moving square scale。

所以若继续写成 Pell / quadratic-form family，仍然会得到 moving coefficient field。

**状态：FAILED AS A UNIFORM CLOSURE ROUTE.**

---

# 9. Oriented geometric ratio：factor pair 并不趋于平方根

SGR-8 给出

\[
t=\frac uc,
\qquad
\frac Nt=\frac vc.
\]

而

\[
t=G(\mathcal R-r_3),
\]

且

\[
N=t\,G(\mathcal R+r_3).
\]

所以

\[
\boxed{
u=cG(\mathcal R-r_3),
\qquad
v=cG(\mathcal R+r_3).
}
\tag{9.1}
\]

因此

\[
\boxed{
\frac vu
=
\frac{\mathcal R+r_3}{\mathcal R-r_3}.
}
\tag{9.2}
\]

定义 normalized gap

\[
\delta
:=
\frac{v-u}{\sqrt{uv}}.
\]

则

\[
\boxed{
\delta
=
\frac{2ha_3}{c\sqrt N}
=
\frac{2r_3}{\sqrt{r_1^2+r_2^2}}
=
\sqrt{\frac vu}-\sqrt{\frac uv}.
}
\tag{9.3}
\]

当前 top DD 有

\[
d_3=s_3=\max(s_1,s_2,d_3).
\]

对任意正既约块，digit bounds 给

\[
10^{s_i-1}<r_i<10^{s_i+1}.
\]

故

\[
r_3>10^{d_3-1},
\]

而

\[
r_1,r_2<10^{d_3+1}.
\]

于是

\[
\boxed{
\delta>
\frac{2\cdot10^{d_3-1}}
{\sqrt2\,10^{d_3+1}}
=
\frac{\sqrt2}{100}.
}
\tag{9.4}
\]

**状态：DERIVED.**

因此 source-labelled factor pair **uniformly bounded away from the balanced ratio \(v/u=1\)**。

这直接解释为什么“closest divisor around \(\sqrt{Nc^2}\)”不是当前 DD 的自然 closing geometry。

---

# 10. Decimal window 作为 divisor interval：精确但不渐近变窄

设

\[
X:=Nc^2,
\qquad
L:=2h10^{n_3-1},
\qquad
U:=2h10^{n_3}.
\]

合法 tail window 等价于

\[
L\le \frac Xu-u<U.
\]

函数

\[
f(z)=X/z-z
\]

在 \((0,\sqrt X)\) 严格递减，所以可精确解为

\[
\boxed{
\frac{\sqrt{U^2+4X}-U}{2}
< u
\le
\frac{\sqrt{L^2+4X}-L}{2}.
}
\tag{10.1}
\]

这是一个完全正确的 divisor interval。

然而其 multiplicative width 取决于

\[
\lambda:=L/\sqrt X,
\]

而 window 本身跨一个十倍区间 \([L,10L)\)。Section 9 又说明 actual normalized gap 并不趋于 \(0\)。现有 DD top inequalities 没有给出

\[
\frac{U_u-L_u}{L_u}\to0.
\]

所以“随着高度增长，合法 divisor interval 自动变成极窄乘法区间”的猜想没有得到支持。

**状态：FAILED AS A UNIFORM SHRINKING-INTERVAL ROUTE.**

---

# 11. Source determinant / center identities

令

\[
A:=A_\kappa,
\qquad
B:=B_\kappa=A+2D.
\]

则

\[
F_+=Av,
\qquad
F_-=Bu.
\]

由 old factor sum：

\[
\boxed{Av+Bu=2TCG.}
\tag{11.1}
\]

差则为

\[
\boxed{
Av-Bu
=
A(v-u)-2Du
=
2\kappa a_3-2Du.
}
\tag{11.2}
\]

这些 linear combinations 没有自动产生一个大模数整除 \(a_3\)；直接 Bezout / determinant attack 退化为 source identities。

但是把

\[
W:=\frac{u+v}{2}
\]

代入 (11.1) 并利用 \(v-u=2ha_3\)，得到一个新的 exact decimal center identity：

\[
\boxed{
(A+D)W
=G(TC+a_3).
}
\tag{11.3}
\]

定义完整 numerator word

\[
\alpha:=TC+a_3.
\]

则

\[
\boxed{
(A+D)W=G\alpha.
}
\tag{11.4}
\]

又因为

\[
\gcd(A+D,D)=1,
\qquad
G=hD,
\]

有

\[
\gcd(A+D,G)=\gcd(A+D,h).
\]

故

\[
\boxed{
\frac{A+D}{\gcd(A+D,h)}\mid\alpha.
}
\tag{11.5}
\]

另一方面完整 denominator word

\[
\beta=TQ+b_3
\]

满足

\[
\boxed{
\beta=c(A+D).
}
\tag{11.6}
\]

所以同一 source-center divisor 还自动进入 \(\beta\)。

**状态：PROVED / DERIVED.**

这是一条此前没有显式写在 terminal \((u,v)\) 坐标中的 exact decimal recovery consequence；但原拼接分子、分母不要求彼此既约，因此它本身不产生 contradiction。

---

# 12. 大模数 quadratic-residue gate

因为

\[
v\equiv u\pmod{a_3},
\]

且

\[
uv=Nc^2,
\]

所以

\[
\boxed{
u^2\equiv Nc^2\pmod{a_3}.}
\tag{12.1}
\]

而 \(\gcd(a_3,c)=1\)，所以 \(c\) 在模 \(a_3\) 下可逆。于是存在

\[
z\equiv uc^{-1}\pmod{a_3}
\]

满足

\[
\boxed{
N\equiv z^2\pmod{a_3}.
}
\tag{12.2}
\]

**状态：PROVED — NEW DECIMAL RECOVERY GATE.**

因此每个奇素数 \(p\mid a_3\) 且 \(p\nmid N\) 都必须满足

\[
\left(\frac Np\right)=1.
\]

本轮尝试把它与 \(N\) 的两平方和 prime classes 做 reciprocity closure；但 decimal window / source structure 并没有给 \(a_3\) 的素因子类别提供 uniform negative character。因此该路线没有单独闭合。

**状态：FAILED AS A UNIFORM RECIPROCITY CLOSURE, 但 gate 本身 PROVED.**

---

# 13. Decisive new observation：顶部 DD 强迫 \(5\mid c\)

本节开始进入最终 closure。

记

\[
m:=m_3.
\]

旧 top DD 已证：

\[
10S+11\le n_3,
\]

\[
d_3\le5S,
\]

且

\[
n_3=m+d_3.
\]

因此

\[
\boxed{m\ge5S+11.}
\tag{13.1}
\]

另一方面

\[
Q<10^S,
\qquad
G<10^S,
\]

故

\[
\kappa\le10QG<10^{2S+1}.
\tag{13.2}
\]

并且

\[
\kappa+2G
<11QG
<11\cdot10^{2S}.
\tag{13.3}
\]

定义

\[
k:=v_5(\kappa),
\qquad
f:=v_5(\kappa+2G).
\]

因为

\[
11\cdot10^{2S}
<5^{3S+4},
\]

（事实上
\(5^{3S+4}/10^{2S}=625(5/4)^S>11\)），所以

\[
\boxed{k,f\le3S+3.}
\tag{13.4}
\]

再记

\[
a:=v_5(A_\kappa),
\qquad
q:=v_5(Q).
\]

因为

\[
\kappa=hA_\kappa,
\]

有

\[
a\le k\le3S+3.
\tag{13.5}
\]

而

\[
c=\frac{TQ}{A_\kappa},
\qquad
T=10^m,
\]

故

\[
\boxed{
v_5(c)=m+q-a.
}
\tag{13.6}
\]

由 (13.1)、(13.5)：

\[
v_5(c)
\ge m-a
\ge(5S+11)-(3S+3)
=2S+8>0.
\]

所以

\[
\boxed{5\mid c.}
\tag{13.7}
\]

而且更强：

\[
\boxed{v_5(c)\ge2S+8.}
\tag{13.8}
\]

**状态：PROVED.**

这已经表明：第三分母 normalized scale \(c\) 必须携带一个随高度线性增长的巨大 \(5\)-power。

---

# 14. 既约性精确固定 quotient gap 的 \(5\)-进深度

由

\[
5\mid c\mid b_3
\]

与

\[
\gcd(a_3,b_3)=1
\]

得到

\[
\boxed{v_5(a_3)=0.}
\tag{14.1}
\]

又

\[
v-u=2ha_3.
\]

因为 \(v_5(2)=0\)：

\[
\boxed{
v_5(v-u)=v_5(h).
}
\tag{14.2}
\]

记

\[
\boxed{H:=v_5(h).}
\]

于是

\[
\boxed{v_5(v-u)=H.}
\tag{14.3}
\]

**状态：PROVED.**

这条 equality 与旧 Hensel phase 完全不同：

- 它发生在已经除去 source divisors 的 oriented quotient factors \(u,v\) 上；
- 它来自 original third-block reducedness；
- 模数不是 projected square-root target，而是 actual quotient difference 本身。

---

# 15. Double resonance 传入 oriented quotients

顶部 DD 已经严格证明 \(5\)-adic resonance，因此

\[
\boxed{
v_5(F_-)=v_5(F_+).
}
\tag{15.1}
\]

记共同赋值为

\[
\boxed{j:=v_5(F_-)=v_5(F_+).}
\]

再记

\[
a:=v_5(A_\kappa),
\qquad
b:=v_5(B_\kappa),
\]

以及

\[
x:=v_5(u),
\qquad
y:=v_5(v).
\]

由

\[
F_-=B_\kappa u,
\qquad
F_+=A_\kappa v
\]

得到

\[
\boxed{x=j-b,
\qquad
y=j-a.}
\tag{15.2}
\]

而

\[
\gcd(A_\kappa,B_\kappa)\in\{1,2\}
\]

说明 \(5\) 不可能同时整除二者，因此

\[
\boxed{\min(a,b)=0.}
\tag{15.3}
\]

所以

\[
\boxed{|x-y|=|a-b|=a+b.}
\tag{15.4}
\]

另一方面 product equation 给

\[
\boxed{x+y=v_5(N)+2v_5(c).}
\tag{15.5}
\]

至此所有参与最终矛盾的量都已经进入 oriented quotient coordinates。

---

# 16. Oriented 5-adic Tail-Overload Lemma

这是本轮 decisive theorem。

## Theorem SGR-9.1 — Oriented 5-adic Quotient Overload

**PROVED.**

当前 top DD 不存在合法 original candidate。

### 证明

继续沿用

\[
H=v_5(h),
\quad
x=v_5(u),
\quad
y=v_5(v),
\quad
a=v_5(A_\kappa),
\quad
b=v_5(B_\kappa).
\]

由 Section 14：

\[
v_5(v-u)=H.
\tag{16.1}
\]

考虑 \(x,y\)。

### 情形 I：\(x\ne y\)

基本 valuation lemma 给

\[
v_5(v-u)=\min(x,y).
\]

所以

\[
\min(x,y)=H.
\]

于是

\[
x+y
=2H+|x-y|
=2H+a+b.
\tag{16.2}
\]

### 情形 II：\(x=y\)

由 (15.4) 必有

\[
a=b=0.
\]

而

\[
v_5(v-u)\ge x.
\]

所以

\[
x\le H,
\]

从而

\[
x+y=2x\le2H=2H+a+b.
\tag{16.3}
\]

### 合并

无论哪一种情形，都有

\[
\boxed{x+y\le2H+a+b.}
\tag{16.4}
\]

再由 product valuation (15.5)：

\[
v_5(N)+2v_5(c)
\le2H+a+b.
\tag{16.5}
\]

利用

\[
v_5(c)=m+q-a,
\qquad
q=v_5(Q),
\]

得到

\[
v_5(N)+2m+2q-2a
\le2H+a+b,
\]

即

\[
\boxed{
v_5(N)+2m+2q
\le
2H+3a+b.
}
\tag{16.6}
\]

现在使用 source divisors 的 near-coprime \(5\)-adic structure。

因为

\[
\kappa=hA_\kappa,
\qquad
\kappa+2G=hB_\kappa,
\]

所以

\[
k:=v_5(\kappa)=H+a,
\]

\[
f:=v_5(\kappa+2G)=H+b.
\]

又因 \(\min(a,b)=0\)：

- 若 \(b=0\)，则
  \[
  2H+3a+b=2H+3a\le3(H+a)=3k;
  \]
- 若 \(a=0\)，则
  \[
  2H+3a+b=2H+b\le2(H+b)=2f\le3f.
  \]

所以统一有

\[
\boxed{
2H+3a+b
\le3\max(k,f).
}
\tag{16.7}
\]

Section 13 已证

\[
k,f\le3S+3.
\]

因此

\[
\boxed{
v_5(N)+2m+2q\le9S+9.}
\tag{16.8}
\]

丢掉非负项 \(v_5(N),2q\)：

\[
\boxed{2m\le9S+9.}
\tag{16.9}
\]

可是 top DD 同时要求

\[
m\ge5S+11.
\]

所以

\[
\boxed{2m\ge10S+22.}
\tag{16.10}
\]

合并 (16.9)–(16.10)：

\[
10S+22
\le2m
\le9S+9,
\]

即

\[
S\le-13,
\]

与

\[
S=m_1+m_2\ge2
\]

矛盾。

故 current top DD 无合法 candidate。

证毕。

---

# 17. 为什么这不是旧 Hensel / old valuation route 的重跑

旧 error-closure 已经解释：tail certificate

\[
10^{m_3}\mid\kappa^2(\kappa+2G)
\]

直接传到 unified error \(E\) 时会出现 \(3v_p(\kappa)\) valuation sink；所以单纯“tail valuation 很深”不能压死 \(E\)。

本轮完全没有试图逆转那个负结论。

新的逻辑链是：

\[
\boxed{
F_-,F_+\text{ 等 }5\text{-进赋值}
}
\]

经过已经固定方向的 source division

\[
F_-=B_\kappa u,
\qquad
F_+=A_\kappa v
\]

变成对 \(u,v\) 两个赋值差的精确控制；同时

\[
c=\frac{10^{m_3}Q}{A_\kappa}
\]

保留了一个至少 \(2S+8\) 深的 \(5\)-power，而

\[
\gcd(a_3,b_3)=1
\]

又把 quotient difference 的 \(5\)-进深度锁死在

\[
v_5(h).
\]

因此发生的不是“valuation supply 太大”这种旧论证，而是：

\[
\boxed{
\text{product 强迫 }u,v\text{ 合计携带巨大 }5\text{-load},
\quad
\text{difference/reducedness 又禁止两边共同携带这么多。}
}
\]

source-labelled near-coprime divisors \(A_\kappa,B_\kappa\) 最后保证二者的 valuation imbalance 本身也只能由一个 \(O(S)\) 的 source integer 提供。

这是 SGR-8 后才成立的 quotient-level closure。

---

# 18. DD chamber closure

SGR-8 把 DD 的唯一 frontier 定义为 current top-DD oriented tail-window：只要证明该 top state 不可能完成第三分子 recovery，DD 随即闭合。

此前 synthesis / error-closure 已将 DD 的真正开放核压到：

\[
10S+11\le n_3\le11S+3,
\]

并带

\[
d_3\le5S,
\qquad
m_3\le6S+2,
\]

以及 top \(2/5\)-adic double resonance。

Theorem SGR-9.1 证明这一开放核为空。

因此在当前 strict-layer proof ledger 中：

\[
\boxed{DD=\varnothing.}
\tag{18.1}
\]

**状态：PROVED RELATIVE TO THE FROZEN PRE-SGR-9 REDUCTIONS.**

这正是本研究项目中“chamber closure”的标准含义：本文件不重新证明所有早期 carrier / Exact-Lift reductions，而是在它们已经冻结的 theorem chain 上关闭最后 surviving DD state。

---

# 19. Decimal tail-window 的最终命运

SGR-8 的 open condition 是

\[
2\cdot10^{n_3-1}
\le
\Lambda D_0
\left(
\frac{K^\sharp}{\kappa}
-
\frac{J^\sharp}{\kappa+2G}
\right)
<
2\cdot10^{n_3}.
\]

左边精确等于

\[
2a_3.
\]

SGR-9 并不是通过直接比较这三个实数项把 window 挤空，而是把同一个 exact tail recovery 改写为

\[
uv=Nc^2,
\qquad
v-u=2ha_3,
\qquad
b_3=cD,
\]

然后在 \(p=5\) 上证明：

\[
\boxed{
\text{任何能让 }a_3\text{ 进入合法 digit window 的 top DD state，}
\text{首先已经在 reducedness / valuation level 不存在。}
}
\]

所以 oriented decimal window 被 **strictly precluded before any leading-digit analysis is needed**。

---

# 20. Failed / Redundant Attempts

本节只记录以后值得避免原样重试的路线。

## 20.1 Ordinary factor spacing around \(\sqrt{Nc^2}\)

**最初希望：** digit window 把 \(u\) 压入越来越窄的 divisor interval。  
**实际结果：** interval (10.1) 虽精确，但 relative width 没有随 height 被证明趋零；而 Section 9 反而证明 factor ratio uniformly away from \(1\)。  
**结论：** **FAILED AS UNIFORM CLOSURE.**

## 20.2 证明 \(\gcd(u,v)\mid2h\)

**最初希望：** reducedness 直接把 product 变成 coprime factorization。  
**失败机制：** common primes 可来自 \(N\) 的 square supply，而不接触第三分母。Section 7 给出显式 abstract counterexample。  
**正确替代：** \(d=d_{\rm den}d_N\)，其中 \(d_{\rm den}\mid2h\)、\(d_N^2\mid N\)。  
**结论：** **FAILED IN STRONG FORM; REPAIRED BY A PROVED DECOMPOSITION.**

## 20.3 Pell / squarefree-state reduction

**最初希望：** \(u=rx^2,v=sy^2\) 后只剩有限 \((r,s)\)。  
**失败机制：** \(\operatorname{sqf}(N)\) 随 moving prefix 带任意新的 \(1\bmod4\) primes；没有 fixed finite kernel set。  
**结论：** **FAILED AS A UNIFORM FINITE-STATE ROUTE.**

## 20.4 Determinant / Bezout direct contradiction

**最初希望：** \(A_\kappa,B_\kappa\) 极近且近互素，某个 determinant 会落入小区间又被大数整除。  
**实际结果：** \(Av\pm Bu\) 主要退化为 old factor sum/difference；得到 center identity (11.4)，但没有 small nonzero multiple contradiction。  
**结论：** **FAILED FOR DIRECT CLOSURE; PRODUCED A VALID DECIMAL DIVISOR GATE.**

## 20.5 Normalized square

\[
h^2a_3^2+Nc^2=W_3^2
\]

仍是 integer-sphere / factorization 的重写。  
**结论：** **REDUNDANT AS AN INDEPENDENT SQUARE GATE.**

## 20.6 Quadratic reciprocity

\[
N\equiv z^2\pmod{a_3}
\]

是真正的新 large-modulus consequence，但没有 source theorem 强制 \(N\) 对所有 \(p\mid a_3\) 取 negative character。  
**结论：** **PROVED GATE, FAILED AS NEEDED CLOSURE.**

## 20.7 Vieta-jump / descent

没有找到同时保持：

- source labels；
- \(b_3=cD\)；
- individual reducedness；
- digit window；
- DD state

的非平凡 descent。既然 Section 16 已直接关闭 DD，不应再为该 chamber 发展 descent machinery。

**结论：FAILED / NOW UNNECESSARY.**

---

# 21. Surviving information table

| Structure | Status after SGR-9 |
|---|---|
| ordinary square spacing | **exhausted / absorbed** |
| projected Hensel phase | **redundant** |
| source higher Hensel digits | **collapsed** |
| source orientation | **solved and decisively used** |
| residual supply | **partial, no longer needed for DD closure** |
| source-labelled divisibility | **decisive** |
| \(\gcd(a_3,b_3)=1\) | **decisive** |
| factor product \(uv=Nc^2\) | **decisive** |
| factor difference \(v-u=2ha_3\) | **decisive** |
| canonical \(c\)-prime allocation | **proved** |
| decimal tail window | **closed indirectly by quotient 5-adic overload** |
| \(5\)-adic double resonance of \(F_\pm\) | **decisive after source division** |
| \(2\)-adic double resonance | **not needed in final contradiction** |
| near-\(S\)-unit | **not needed in final contradiction** |
| extreme denominator asymmetry | **not directly needed beyond inherited top reduction** |
| normalized square \(h^2a_3^2+Nc^2=W_3^2\) | **absorbed / redundant** |
| quadratic-residue gate \(N\equiv\square\pmod{a_3}\) | **proved but unnecessary for closure** |

关键更新是：

\[
\boxed{
\text{DD closure 真正需要的是}
\quad
\text{orientation}+\text{source division}+\text{reducedness}+5\text{-resonance}.
}
\]

near-square、near-\(S\)-unit 与 higher phase 都不再属于 DD frontier。

---

# 22. Proof-status ledger

## PROVED

### Inherited

1. DD 的 current open core 为 top chamber；
2. \(d_3\le5S\)；
3. \(10S+11\le n_3\le11S+3\)；
4. top \(5\)-adic double resonance；
5. orientation
   \[
   F_-\to J^\sharp,
   \quad
   F_+\to K^\sharp;
   \]
6. source-labelled divisibility
   \[
   B_\kappa\mid F_-,
   \quad
   A_\kappa\mid F_+;
   \]
7. \(c=TQ/A_\kappa\in\mathbf Z\)、\(b_3=cD\)；
8. canonical factors
   \[
   uv=Nc^2,
   \quad
   v-u=2ha_3.
   \]

### New in SGR-9

9. exact difference gcd
   \[
   \gcd(v-u,cD)=\gcd(2h,cD);
   \]
10. exact scaled gcd
   \[
   \gcd(v-u,2hcD)=2h;
   \]
11. common-gcd decomposition
   \[
   d=d_{\rm den}d_N,
   \quad
   d_{\rm den}\mid2h,
   \quad
   d_N^2\mid N;
   \]
12. nonexceptional \(c\)-prime full one-sided allocation；
13. source geometry
   \[
   u=cG(\mathcal R-r_3),
   \quad
   v=cG(\mathcal R+r_3);
   \]
14. normalized gap uniformly bounded away from \(0\)；
15. source-center decimal divisor identity；
16. quadratic-residue gate
   \[
   N\equiv\square\pmod{a_3};
   \]
17. top DD forces
   \[
   v_5(c)\ge2S+8;
   \]
18. reducedness forces
   \[
   v_5(v-u)=v_5(h);
   \]
19. quotient-resonance inequality
   \[
   2m_3\le9S+9;
   \]
20. top lower bound
   \[
   2m_3\ge10S+22;
   \]
21. contradiction；
22. current top DD empty；
23. inherited DD frontier therefore empty。

## DERIVED

1. normalized factor ratio formula；
2. explicit divisor interval；
3. \(A+D\) center identity and full decimal word factorization。

## HEURISTIC

None needed for the final theorem.

## COMPUTATIONAL EVIDENCE

None used in the final proof. No finite search, CAS identity, or probabilistic experiment is required for SGR-9.1.

## FAILED

- full \(\gcd(u,v)\mid2h\)；
- shrinking divisor interval；
- finite squarefree kernel / uniform Pell；
- direct determinant contradiction；
- normalized-square reopening；
- reciprocity closure；
- oriented descent。

## OPEN

\[
\boxed{\textbf{None inside DD.}}
\]

本轮完成后，不应再为 DD 保留新的 terminal target。

---

# 23. 最终裁决

\[
\boxed{\textbf{SGR-9A — DD CLOSED}.}
\]

在 SGR-8 之后，orientation 首次真正发挥了 closure 作用：

\[
F_-=B_\kappa u,
\qquad
F_+=A_\kappa v
\]

把旧 double resonance 从 unordered / common-factor 信息转成了 **有方向的 quotient valuation relation**。

第三块既约性又把

\[
v-u=2ha_3
\]

的 \(5\)-进深度精确固定。

与此同时，denominator normalization

\[
c=\frac{10^{m_3}Q}{A_\kappa}
\]

把至少 \(2S+8\) 个 \(5\)-adic units 强制放入 product

\[
uv=Nc^2.
\]

最终这三件事无法同步：

\[
\boxed{
10S+22
\le2m_3
\le9S+9.
}
\]

所以：

\[
\boxed{
\text{不存在 current top-DD original candidate.}
}
\]

而此前 proof ledger 已把 DD 的唯一开放核压到该 top chamber，因此：

\[
\boxed{DD=\varnothing.}
\]

从 strict-layer frontier 中删除 DD。

