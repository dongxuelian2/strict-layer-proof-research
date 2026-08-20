# 三项十进制拼接平方和问题：DD Error-Closure Campaign

**文件名：** `strict_layer_DD_error_closure_campaign.md`  
**本轮范围：** Strict Layer，仅研究 **DD chamber**  
**本轮等级：** **SGR-4D — STRUCTURAL PARTIAL**  
**最终状态：** **DD 尚未闭合**

---

# 0. 结论摘要

本轮把旧 DD 顶部的 near-square、double resonance、near-\(S\)-unit 与 tail divisibility
完整传递到了 SGR-3 的统一误差坐标

\[
\varepsilon M^2-E=\varepsilon Y^2,
\qquad
Y\in\mathbf Z_{\ge0},
\qquad
0\le Y<M.
\]

最重要的新结果不是一个新的粗估计，而是一条**精确整数格点缩放**。

令

\[
X_{\rm old}:=GA_{12}10^{n_3},
\]

\[
\Delta_{\rm old}
:=
\mathcal N_{12}10^{m_3}Q_{12}
\left(10^{m_3}Q_{12}+2b_3\right),
\]

并定义

\[
\boxed{
\Lambda
:=
UR^2\,10^{\lceil m_3/2\rceil}.
}
\]

则 DD 中严格有

\[
\boxed{
X_{\rm old}=\Lambda M,
}
\]

\[
\boxed{
\Delta_{\rm old}
=
\frac{\Lambda^2}{\varepsilon}E,
}
\]

以及

\[
\boxed{
\rho
=
\frac{E}{\varepsilon M^2}
=
\frac{\Delta_{\rm old}}{X_{\rm old}^2}.
}
\]

因此旧 DD near-square

\[
Y_{\rm old}^2
=
X_{\rm old}^2-\Delta_{\rm old}
\]

与 SGR-3 的平方

\[
Y^2=M^2-\frac E\varepsilon
\]

不是两个相似现象，而是同一整数平方门的精确缩放：

\[
\boxed{
Y_{\rm old}=\Lambda Y.
}
\]

更强地，旧 double-resonance 分析中的两个正因子

\[
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
\qquad
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0}
\]

满足

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda(M-Y),\,
\Lambda(M+Y)
\}.
}
\]

这给出了旧 DD arithmetic structure 到新误差 \(E\) 的真正精确桥。

在顶部 double resonance 区，对 \(p=2,5\) 两个旧因子具有相同 \(p\)-进赋值，因此除去共同格点尺度 \(\Lambda\) 后，

\[
\boxed{
v_p(M-Y)=v_p(M+Y)=:j_p.
}
\]

于是

\[
\boxed{
v_p(E)=v_p(\varepsilon)+2j_p,
\qquad p=2,5.
}
\]

换言之，double resonance 对 \(E\) 的实际贡献不是“产生一个异常高的单边赋值”，而是：

\[
\boxed{
\text{把 }E/\varepsilon\text{ 的 }2\text{-进和 }5\text{-进赋值强制成偶数，}
}
\]

并将对应 \(2,5\)-smooth 因子**平均分配**到

\[
M-Y,\qquad M+Y
\]

两边。

这反而解释了为什么旧 tail divisibility 不能直接升级成 DD-T2 / DD-T3：
旧尾部证书控制

\[
2v_p(\kappa)+v_p(\kappa+2G),
\]

而 \(E\) 真正读取的是

\[
v_p(\kappa+2G)-v_p(\kappa).
\]

两者之间恰好存在一个

\[
\boxed{3v_p(\kappa)}
\]

的 valuation sink。

因此本轮没有闭合 DD。

但是三种攻击现在全部压到同一个最小整数：

\[
\boxed{
J:=M-Y
=
\frac{\min(F_-,F_+)}{\Lambda}
\in\mathbf Z_{\ge1}.
}
\]

因为

\[
E=\varepsilon J(2M-J),
\]

DD-T1 等价于把 \(J\) 压到 \(0<J<1\)；
DD-T3 等价于找到一个由旧 resonance 强制的整数 \(D\mid J\) 且 \(D>J\)；
DD-T2 在顶部 resonance 下同样必须最终控制这个 deflated small factor。

所以本轮留下的**唯一 terminal gap**是：

\[
\boxed{
\textbf{对 }
J=\frac{\min(F_-,F_+)}{\Lambda}=M-Y
\textbf{ 建立一个真正的 post-deflation size/valuation overload。}
}
\]

现有顶部尖角、double resonance、near-\(S\)-unit 与 tail certificate
都还没有给出这一最后一步。

---

# 1. 来源审计与范围冻结

本轮重点使用并交叉核对：

- `strict_layer_moving_core_square_spacing_campaign.md`；
- `strict_layer_unified_exact_lift_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`。

后者当前 File Library 中可检索到的正文已经包含 DD 的：

- 公共商正规化；
- surplus simplex；
- near-square；
- \(d_3\le5S_{12}\)；
- \(2/5\)-adic double resonance；
- near-\(S\)-unit；
- square-part 上下界与 extreme asymmetry；
- 最大 denominator-tail 层排除；
- 最终顶部尖角

等实际证明链。

本轮额外检索了 DD resonance / \(R_5\) / Hensel phase 等关键词，
没有重新暴露一个独立命名的、晚于 synthesis 的 DD 专门证明文件。
因此本文不虚构“已重新读取”不可见的独立报告；
涉及顶部 DD 的已证输入均以 synthesis 中实际展开的 §§17–26 为准。

早期 `exact_lift_preprint.pdf` 中存在后来已经被研究综述降级或废弃的旧 closure，
本轮不使用其中“DD 已关闭”之类的过期结论。

范围严格冻结为

\[
\boxed{\text{DD only}.}
\]

不研究 \(A_1\)，不研究临界 \(A_2\)，不做 resultant 形式消元。

---

# 2. 先修正 SGR-3 的 \(Y=0\) 边界

SGR-3 给出

\[
\boxed{
\varepsilon M^2-E=\varepsilon Y^2,
}
\]

其中本轮按安全版本取

\[
\boxed{
Y\in\mathbf Z_{\ge0},
\qquad
0\le Y<M.
}
\]

不能默认 \(Y>0\)。

由于 \(E>0\)，确有 \(Y<M\)。

如果

\[
Y=0,
\]

则

\[
E=\varepsilon M^2.
\]

又因为

\[
M^2-(2M-1)=(M-1)^2\ge0,
\]

仍有

\[
E\ge\varepsilon(2M-1).
\]

如果

\[
1\le Y<M,
\]

则

\[
E
=
\varepsilon(M-Y)(M+Y)
\]

且

\[
M-Y\ge1,\qquad M+Y\ge2M-1,
\]

所以同样得到

\[
\boxed{
E\ge\varepsilon(2M-1).
}
\]

因此 SGR-3 square-spacing lemma 在允许 \(Y=0\) 后仍然成立，
但证明必须分开处理零根。

---

# 3. DD 旧变量到 \(E,M,\rho\) 的精确字典

## 3.1 旧 DD 主变量

统一记

\[
S_{12}=m_1+m_2,
\]

\[
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0,
\]

\[
Q_{12}
=
b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\]

\[
\mathcal N_{12}
=
(a_1b_2)^2+(a_2b_1)^2,
\]

\[
A_{12}
=
a_1 10^{n_2}+a_2.
\]

DD 中

\[
n_3=m_3+d_3.
\]

尾权为

\[
\boxed{
\kappa
=
\frac{10^{m_3}Q_{12}G}{b_3}
\in\mathbf Z,
}
\]

并满足

\[
Q_{12}G<\kappa\le10Q_{12}G.
\]

---

## 3.2 primitive-profile scale

SGR / Exact-Lift 统一坐标写成

\[
a_i=UC_i,
\qquad
b_i=Rh_i,
\]

其中

\[
\gcd(U,V)=1
\]

且

\[
R=\frac{V}{L_g}.
\]

于是

\[
Q_{12}=R\widehat Q,
\]

\[
G=R^2\widehat G,
\]

\[
\mathcal N_{12}
=
U^2R^2\widehat{\mathcal N},
\]

\[
A_{12}=U\widehat A_{12}.
\]

DD coefficient 满足

\[
\widehat C
=
10^{d_3}\widehat A_{12}.
\]

---

## 3.3 \(M\) 的旧变量表达式

SGR-3 定义

\[
M
=
10^{\lfloor m_3/2\rfloor}
\widehat G\widehat C.
\]

代入 DD 的尺度分解：

\[
\boxed{
M
=
10^{\lfloor m_3/2\rfloor+d_3}
\frac{GA_{12}}{UR^2}.
}
\tag{3.1}
\]

---

## 3.4 \(E\) 的旧变量表达式

DD 中 \(\chi=1\)，因此

\[
E
=
\widehat Q\widehat{\mathcal N}
\left(
10^{m_3}\widehat Q+2h_3
\right).
\]

换回旧变量：

\[
\boxed{
E
=
\frac{
Q_{12}\mathcal N_{12}
\left(
10^{m_3}Q_{12}+2b_3
\right)
}{
U^2R^4
}.
}
\tag{3.2}
\]

再用

\[
b_3
=
\frac{10^{m_3}Q_{12}G}{\kappa}
\]

可写成

\[
\boxed{
E
=
\frac{
10^{m_3}Q_{12}^2\mathcal N_{12}
(\kappa+2G)
}{
U^2R^4\kappa
}.
}
\tag{3.3}
\]

这已经明确显示：

\[
E
\text{ 读取的是 }
\frac{\kappa+2G}{\kappa},
\]

而不是旧 tail certificate 中的乘积

\[
\kappa^2(\kappa+2G).
\]

---

## 3.5 \(\rho\) 的精确表达式

由

\[
\rho=\frac{E}{\varepsilon M^2}
\]

得到

\[
\boxed{
\rho_{DD}
=
10^{-2d_3}
\frac{
Q_{12}^2\mathcal N_{12}
}{
G^2A_{12}^2
}
\left(
1+
\frac{2b_3}{10^{m_3}Q_{12}}
\right).
}
\tag{3.4}
\]

也可写成

\[
\boxed{
\rho_{DD}
=
10^{-2d_3}
\frac{
Q_{12}^2\mathcal N_{12}
}{
G^2A_{12}^2
}
\frac{\kappa+2G}{\kappa}.
}
\tag{3.5}
\]

所以旧 DD 中的 \(10^{-2d_3}\) near-square 因子确实精确进入统一误差。

但这还不是最紧的字典。
下一节给出真正的整数格点等价。

---

# 4. 新核心：旧 near-square 与 SGR-3 是同一平方格点

旧 DD near-square 定义

\[
\boxed{
X_{\rm old}
:=
GA_{12}10^{n_3},
}
\tag{4.1}
\]

以及

\[
\boxed{
\Delta_{\rm old}
:=
\mathcal N_{12}10^{m_3}Q_{12}
\left(
10^{m_3}Q_{12}+2b_3
\right).
}
\tag{4.2}
\]

旧判别平方写成

\[
\boxed{
Y_{\rm old}^2
=
X_{\rm old}^2-\Delta_{\rm old}.
}
\tag{4.3}
\]

这里允许

\[
Y_{\rm old}=0.
\]

---

## 4.1 精确格点尺度

定义

\[
\boxed{
\Lambda
=
UR^2\,10^{\lceil m_3/2\rceil}.
}
\tag{4.4}
\]

由 \(n_3=m_3+d_3\) 与 (3.1)，

\[
\begin{aligned}
\Lambda M
&=
UR^2 10^{\lceil m_3/2\rceil}
\cdot
10^{\lfloor m_3/2\rfloor+d_3}
\frac{GA_{12}}{UR^2}\\
&=
GA_{12}10^{m_3+d_3}\\
&=
GA_{12}10^{n_3}.
\end{aligned}
\]

所以

\[
\boxed{
X_{\rm old}=\Lambda M.
}
\tag{4.5}
\]

另一方面，由 (3.2)，

\[
\Delta_{\rm old}
=
U^2R^4 10^{m_3}E.
\]

而

\[
\frac{\Lambda^2}{\varepsilon}
=
U^2R^4 10^{m_3}
\]

无论 \(m_3\) 奇偶均成立：

- \(m_3=2r\)：\(\varepsilon=1\)，\(\Lambda^2=U^2R^4 10^{2r}\)；
- \(m_3=2r+1\)：\(\varepsilon=10\)，\(\Lambda^2/10=U^2R^4 10^{2r+1}\)。

因此

\[
\boxed{
\Delta_{\rm old}
=
\frac{\Lambda^2}{\varepsilon}E.
}
\tag{4.6}
\]

于是

\[
\boxed{
\rho
=
\frac{E}{\varepsilon M^2}
=
\frac{\Delta_{\rm old}}{X_{\rm old}^2}.
}
\tag{4.7}
\]

这比“旧 near-square 对应新 \(\rho\)”更强：
它证明两者是完全相同的无量纲平方缺口。

---

## 4.2 平方根也精确缩放

由

\[
\varepsilon M^2-E=\varepsilon Y^2
\]

与 (4.5)–(4.6)，

\[
\begin{aligned}
X_{\rm old}^2-\Delta_{\rm old}
&=
\Lambda^2M^2
-
\frac{\Lambda^2}{\varepsilon}E\\
&=
\Lambda^2Y^2.
\end{aligned}
\]

因此可以取

\[
\boxed{
Y_{\rm old}=\Lambda Y.
}
\tag{4.8}
\]

所以：

\[
\boxed{
(X_{\rm old},Y_{\rm old})
=
\Lambda(M,Y).
}
\]

旧 DD near-square 不是一个独立于 SGR-3 的第二平方现象；
它就是 SGR-3 平方格点经过整数尺度 \(\Lambda\) 的放大。

---

# 5. 旧两个 resonance 因子也恰好缩放为 \(M\pm Y\)

旧 DD 定义

\[
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
\]

\[
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0}.
\]

已有

\[
\boxed{
F_-+F_+
=
2GA_{12}10^{n_3}
=
2X_{\rm old}.
}
\tag{5.1}
\]

同时 primitive recovery 给出

\[
10^{m_3}Q_{12}G_0
=
2\kappa\mu\nu.
\]

因此

\[
\begin{aligned}
F_-F_+
&=
\frac{
4\kappa(\kappa+2G)
\mathcal N_{12}\mu^2\nu^2
}{
G_0^2
}\\
&=
\mathcal N_{12}10^{2m_3}Q_{12}^2
\frac{\kappa+2G}{\kappa}\\
&=
\mathcal N_{12}10^{m_3}Q_{12}
\left(
10^{m_3}Q_{12}+2b_3
\right)\\
&=
\Delta_{\rm old}.
\end{aligned}
\]

所以

\[
\boxed{
F_-F_+=\Delta_{\rm old}.
}
\tag{5.2}
\]

由 (5.1)–(5.2)，\(F_-,F_+\) 是二次式

\[
T^2-2X_{\rm old}T+\Delta_{\rm old}=0
\]

的两个正根。

而该二次式的根是

\[
X_{\rm old}\pm Y_{\rm old}.
\]

故得到本轮最重要的 exact bridge：

\[
\boxed{
\{F_-,F_+\}
=
\{
X_{\rm old}-Y_{\rm old},
X_{\rm old}+Y_{\rm old}
\}.
}
\tag{5.3}
\]

再代入 (4.5)、(4.8)：

\[
\boxed{
\{F_-,F_+\}
=
\{
\Lambda(M-Y),
\Lambda(M+Y)
\}.
}
\tag{5.4}
\]

这一步把旧 DD 的：

- near-square；
- two-factor decomposition；
- double resonance；

全部直接接到了 SGR-3 的两个平方差因子。

---

# 6. Square-spacing 在旧 DD 坐标中的加强形式

SGR-3 的完整候选必要条件为

\[
E\ge\varepsilon(2M-1).
\]

乘以 \(\Lambda^2/\varepsilon\)，并使用 (4.5)–(4.6)：

\[
\boxed{
\Delta_{\rm old}
\ge
\Lambda^2(2M-1)
=
\Lambda(2X_{\rm old}-\Lambda).
}
\tag{6.1}
\]

这严格加强了旧 near-square 只利用普通整数平方间距得到的

\[
\Delta_{\rm old}\ge2X_{\rm old}-1.
\]

原因是旧平方根并不是任意整数；
它被强制落在子格

\[
\Lambda\mathbf Z
\]

上。

因此真正的 DD square spacing 是：

\[
\boxed{
\text{相邻可允许平方不是间距 }2X_{\rm old}-1,
\text{而是 }\Lambda(2X_{\rm old}-\Lambda).
}
\]

这是本轮最强的 Archimedean 新不等式。

---

## 6.1 为什么它仍未闭合顶部 DD

旧顶部已经有

\[
10S_{12}+11
\le n_3\le11S_{12}+3,
\]

\[
d_3=\max(s_1,s_2,d_3),
\]

\[
d_3\le5S_{12},
\]

\[
m_3\le6S_{12}+2,
\]

以及 extreme asymmetry。

SGR-3 已有的显式 bound 是

\[
\rho_{DD}
<
143
\left[
10^{-2k_{12}}
+
10^{2(1-d_3-s_1)}
\right].
\]

本轮的 (4.7) 证明这正是

\[
\Delta_{\rm old}/X_{\rm old}^2
\]

的上界。

但要真正排除候选，仍必须与

\[
\frac{2}{M}-\frac1{M^2}
\]

比较。

问题在于：

\[
M
=
10^{\lfloor m_3/2\rfloor+d_3}
\frac{GA_{12}}{UR^2}
\]

仍读取完整 moving-core scale 与 prefix arithmetic；
顶部 extreme asymmetry 同时会使

\[
\frac{\mathcal N_{12}}{A_{12}^2}
\]

中的非主项可能放大。

现有已证 DD inequalities 尚不能统一推出

\[
\rho<
\frac2M-\frac1{M^2}.
\]

因此 (6.1) 是严格的新 lattice-spacing 加强，
但目前还不能变成 DD-T1。

---

# 7. Double resonance 对 \(v_2(E),v_5(E)\) 的精确贡献

对 \(p=2,5\)，旧 DD 记

\[
r_p=v_p(\mu),
\qquad
s_p=v_p(\nu),
\]

\[
k_p=v_p(\kappa),
\qquad
f_p=v_p(\kappa+2G),
\]

\[
n_p=v_p(\mathcal N_{12}),
\qquad
c_p=v_p(G_0).
\]

并有

\[
v_p(F_-)
=
v_p(2)+f_p+2r_p-c_p,
\]

\[
v_p(F_+)
=
v_p(2)+k_p+n_p+2s_p-c_p.
\]

顶部 DD 满足 double resonance：

\[
\boxed{
f_p+2r_p
=
k_p+n_p+2s_p,
\qquad
p=2,5.
}
\tag{7.1}
\]

所以

\[
\boxed{
v_p(F_-)=v_p(F_+).
}
\tag{7.2}
\]

---

## 7.1 除去 \(\Lambda\) 后 resonance 变成两个 SGR 因子的等赋值

令

\[
\lambda_p:=v_p(\Lambda)
=
v_p(U)+2v_p(R)+\left\lceil\frac{m_3}{2}\right\rceil.
\]

由 (5.4)，

\[
v_p(M-Y)
=
v_p(F_{\min})-\lambda_p,
\]

\[
v_p(M+Y)
=
v_p(F_{\max})-\lambda_p.
\]

结合 resonance：

\[
\boxed{
v_p(M-Y)
=
v_p(M+Y)
=:j_p.
}
\tag{7.3}
\]

其中可以显式写为

\[
\boxed{
j_p
=
v_p(2)+f_p+2r_p-c_p
-
v_p(U)-2v_p(R)
-
\left\lceil\frac{m_3}{2}\right\rceil.
}
\tag{7.4}
\]

也等价于

\[
\boxed{
j_p
=
v_p(2)+k_p+n_p+2s_p-c_p
-
v_p(U)-2v_p(R)
-
\left\lceil\frac{m_3}{2}\right\rceil.
}
\tag{7.5}
\]

这就是 requested old-resonance \(\to\) SGR factor valuation 的精确字典。

---

## 7.2 \(E\) 的赋值因此完全确定

因为

\[
E
=
\varepsilon(M-Y)(M+Y),
\]

由 (7.3)：

\[
\boxed{
v_p(E)
=
v_p(\varepsilon)+2j_p,
\qquad
p=2,5.
}
\tag{7.6}
\]

特别地：

\[
\boxed{
v_p(E)-v_p(\varepsilon)
\equiv0\pmod2,
\qquad p=2,5.
}
\tag{7.7}
\]

所以顶部 double resonance 的真正传递结果是：

\[
\boxed{
(E/\varepsilon)_{(2,5)}
\text{ 的 }2,5\text{-primary part 是完全平方。}
}
\]

定义

\[
\boxed{
D_0:=2^{j_2}5^{j_5}.
}
\tag{7.8}
\]

则

\[
\boxed{
D_0\mid(M-Y),
\qquad
D_0\mid(M+Y),
}
\tag{7.9}
\]

并且

\[
\boxed{
D_0^2
\mid
\frac E\varepsilon.
}
\tag{7.10}
\]

事实上 \(D_0^2\) 正是 \(E/\varepsilon\) 的完整 \(2,5\)-primary part。

---

# 8. 一个重要的负结论：resonance 没有把赋值集中到小因子

本轮原本第三攻击面希望：

\[
v_p(M-Y)+v_p(M+Y)
=
v_p(E/\varepsilon)
\]

中绝大部分赋值被迫落到较小因子 \(M-Y\)。

但顶部 DD 的旧 resonance 恰好给出相反结论：

\[
\boxed{
v_p(M-Y)=v_p(M+Y),
\qquad p=2,5.
}
\]

即 \(2\)-进和 \(5\)-进负载被**完全均分**。

因此旧 double resonance 本身不会产生：

\[
\text{“小因子承担绝大部分 }2/5\text{-adic valuation”}.
\]

相反，

\[
D_0\mid\gcd(M-Y,M+Y).
\]

于是自动有

\[
D_0\mid2M,
\qquad
D_0\mid2Y.
\]

特别

\[
j_5\le v_5(M),
\]

\[
j_2\le v_2(M)+1.
\]

这说明 DD-T3 若要成立，必须得到一个**独立于这种共同分配恒等式之外的**
\(D_0\) 下界。

现有 resonance 本身没有提供这个 overload。

---

# 9. Tail divisibility 与 near-\(S\)-unit 到 \(E\) 的精确传递

旧 DD tail certificate 为

\[
\boxed{
10^{m_3}\mid\kappa^2(\kappa+2G).
}
\tag{9.1}
\]

定义

\[
\boxed{
\mathscr T
=
\frac{
\kappa^2(\kappa+2G)
}{
10^{m_3}
}
\in\mathbf Z_{>0}.
}
\tag{9.2}
\]

顶部区域已有

\[
\boxed{
1\le\mathscr T<10^{S_{12}-7}.
}
\tag{9.3}
\]

由 (3.3) 和

\[
\kappa+2G
=
\frac{10^{m_3}\mathscr T}{\kappa^2}
\]

得到

\[
\boxed{
E
=
\frac{
10^{2m_3}Q_{12}^2\mathcal N_{12}\mathscr T
}{
U^2R^4\kappa^3
}.
}
\tag{9.4}
\]

这是 near-\(S\)-unit 到 \(E\) 的精确乘商表达式。

它揭示一个此前在 \(E\)-语言中不明显的事实：

\[
\boxed{
\text{tail 的巨大 }10^{m_3}\text{ 因子进入 }E
\text{ 时，被 }\kappa^3\text{ 抵消。}
}
\]

---

## 9.1 逐素数 valuation sink

令

\[
t_p:=v_p(\mathscr T)
=
2k_p+f_p-m_3
\ge0.
\]

由 (3.3)：

\[
\boxed{
v_p(E)
=
m_3
+
2v_p(Q_{12})
+
v_p(\mathcal N_{12})
+
f_p-k_p
-
2v_p(U)-4v_p(R).
}
\tag{9.5}
\]

而

\[
f_p-k_p
=
m_3+t_p-3k_p.
\]

所以

\[
\boxed{
\begin{aligned}
v_p(E)
={}&
2m_3
+
2v_p(Q_{12})
+
v_p(\mathcal N_{12})
+
t_p\\
&-
3k_p
-
2v_p(U)
-
4v_p(R).
\end{aligned}
}
\tag{9.6}
\]

这就是 tail divisibility 到 \(E\) 的精确 valuation transfer。

核心是负项

\[
\boxed{-3k_p.}
\]

旧 tail certificate 控制的是

\[
2k_p+f_p,
\]

而 \(E\) 需要的是

\[
f_p-k_p.
\]

所以两者之间相差整整

\[
\boxed{3k_p.}
\]

near-\(S\)-unit 只说明 \(\kappa,\kappa+2G\) 去掉 \(2,5\) 后的部分很小；
它并不限制 \(\kappa\) 自身储存大量 \(2\)-、\(5\)-进赋值。

因此旧 tail 的高 valuation 可以主要储存在

\[
\kappa^2
\]

中，并在传入 \(E\) 时被 \(\kappa^3\) 的分母消耗。

这正是当前 DD-T2 无法直接形成的原因。

---

## 9.2 resonance 下的另一种精确写法

由

\[
f_p+2r_p
=
k_p+n_p+2s_p
\]

得

\[
f_p-k_p
=
n_p+2(s_p-r_p).
\]

代入 (9.5)：

\[
\boxed{
\begin{aligned}
v_p(E)
={}&
m_3
+
2v_p(Q_{12})
+
2v_p(\mathcal N_{12})\\
&+
2(s_p-r_p)
-
2v_p(U)
-
4v_p(R).
\end{aligned}
}
\tag{9.7}
\]

这与 (7.6) 完全兼容。

它再次表明：
resonance 消掉了 \(k_p,f_p\) 的单独自由度，
但没有自动产生一个随 \(S_{12}\) 线性增长、且足以超过 \(E\) Archimedean 大小的正 valuation gap。

---

# 10. 顶部 interval 与 near-\(S\)-unit 的增长率比较

当前真正开放的 DD 顶部满足

\[
\boxed{
10S_{12}+11
\le n_3
\le11S_{12}+3,
}
\]

\[
\boxed{
d_3=\max(s_1,s_2,d_3),
}
\]

\[
\boxed{
d_3\le5S_{12},
}
\]

\[
\boxed{
m_3\le6S_{12}+2,
}
\]

以及

\[
\boxed{
|s_1-s_2|
>
1.466872S_{12}+4.826675,
}
\]

\[
\boxed{
|m_1-m_2|
>
0.466872S_{12}+4.826675.
}
\]

由顶部下界与 \(d_3\le5S_{12}\)：

\[
\boxed{
m_3\ge5S_{12}+11.
}
\]

所以

\[
m_3
=
5S_{12}+O(S_{12})
\]

并且 near-\(S\)-unit quotient 满足

\[
\log_{10}\mathscr T<S_{12}-7.
\]

另一方面

\[
Q_{12}
\]

恰有 \(S_{12}\) 位，而

\[
10^{S_{12}-2}
\le G<10^{S_{12}},
\]

故

\[
2S_{12}-3
<
\log_{10}\kappa
<
2S_{12}+1.
\]

所以：

\[
\boxed{
\log_{10}\kappa\asymp2S_{12},
\qquad
m_3\asymp5\text{--}6S_{12}.
}
\]

于是 tail product

\[
\kappa^2(\kappa+2G)
\]

的自然 Archimedean 尺度本来就是约

\[
10^{6S_{12}},
\]

正好足以容纳 \(10^{m_3}\)。

这说明 near-\(S\)-unit 的“小 quotient”

\[
\mathscr T
\]

本身并不会强制一个比 \(E\) 更大的 \(2,5\)-adic 模数；
它主要说明 tail product 已经逼近自身的最大 smooth capacity。

而 (9.6) 说明这部分 capacity 在映射到 \(E\) 时还必须减去 \(3k_p\)。

因此目前没有得到

\[
\log_{10}D_E-\log_{10}E
\ge cS_{12}-O(1),
\qquad c>0.
\]

这正是用户要求检查的 valuation-growth vs Archimedean-growth 比较：
**现有证明库在传入 \(E\) 后没有留下正指数缺口。**

---

# 11. 三种终止攻击现在如何统一

定义

\[
\boxed{
J:=M-Y.
}
\tag{11.1}
\]

因为

\[
0\le Y<M,
\]

所以

\[
\boxed{
1\le J\le M.
}
\tag{11.2}
\]

并且

\[
\boxed{
E
=
\varepsilon J(2M-J).
}
\tag{11.3}
\]

由 (5.4)：

\[
\boxed{
J
=
\frac{\min(F_-,F_+)}{\Lambda}.
}
\tag{11.4}
\]

这就是 DD 当前最小的 terminal integer。

---

## 11.1 DD-T1 — Square gap

在

\[
1\le J\le M
\]

上，

\[
J(2M-J)
\]

严格单调增加直到 \(J=M\)，因此最小正值在 \(J=1\)：

\[
J(2M-J)\ge2M-1.
\]

所以

\[
E<\varepsilon(2M-1)
\]

本质上就是要从旧 DD 数据推出

\[
\boxed{
0<J<1.
}
\]

等价地：

\[
\boxed{
0<\min(F_-,F_+)<\Lambda.
}
\]

---

## 11.2 DD-T3 — Small-factor overload

double resonance 给出

\[
D_0=2^{j_2}5^{j_5}\mid J.
\]

所以 DD-T3 的真正目标是

\[
\boxed{
D_0>J.
}
\]

这同样只作用于 \(J\)。

---

## 11.3 DD-T2 — Divisibility gap

顶部 resonance 下

\[
v_p(E/\varepsilon)=2j_p.
\]

因此由 resonance 直接产生的 \(2,5\)-primary modulus 是

\[
D_0^2.
\]

但

\[
E/\varepsilon
=
J(2M-J),
\]

且

\[
D_0\mid J,\qquad D_0\mid(2M-J).
\]

所以不额外控制 \(J\) 的大小，
仅凭这个共同 smooth factor 不能推出 modulus-over-size。

---

# 12. 最强攻击面的裁决

三条路线中，本轮最强的是：

\[
\boxed{
\textbf{Exact lattice transfer + deflated small-factor reduction}.
}
\]

其核心新结论可以浓缩为：

\[
\boxed{
\{F_-,F_+\}
=
\{\Lambda J,\Lambda(2M-J)\},
}
\]

\[
\boxed{
D_0\mid J,\qquad
v_p(E)=v_p(\varepsilon)+2j_p,
}
\]

以及

\[
\boxed{
\Delta_{\rm old}
\ge
\Lambda(2X_{\rm old}-\Lambda).
}
\]

相比继续在

\[
\rho,\quad
E,\quad
F_\pm,\quad
\kappa
\]

之间并行追条件，
现在所有死亡机制都只差对一个正整数

\[
J
\]

做最后控制。

---

# 13. 为什么本轮不能标 SGR-4C

SGR-4C 要求已经得到 DD-T1 / T2 / T3 中某个统一 terminal lemma，
只剩一个小证明缺口。

本轮尚未得到：

\[
E<\varepsilon(2M-1),
\]

也没有得到某个外部强制模数

\[
D_E>E,
\]

更没有得到

\[
2^a5^b>M-Y.
\]

得到的是这些目标之前的**精确规范化与统一缩减**：

\[
\text{old DD structure}
\longrightarrow
J=M-Y.
\]

因此不能把结果抬高为 SGR-4C。

---

# 14. 为什么也不应标 SGR-4E

本轮并没有证明“旧 DD arithmetic 完全无法传递到 \(E\)”。

相反，已经得到：

\[
\rho=\frac{\Delta_{\rm old}}{X_{\rm old}^2},
\]

\[
Y_{\rm old}=\Lambda Y,
\]

\[
\{F_-,F_+\}
=
\{\Lambda(M-Y),\Lambda(M+Y)\},
\]

\[
v_p(E)
=
v_p(\varepsilon)+2j_p.
\]

所以 transfer 本身是成功且非常精确的。

失败的是：

\[
\boxed{
\text{现有 old DD bounds 尚不足以把 transfer 后的 }J
\text{ 压成整数矛盾。}
}
\]

因此正确等级是：

\[
\boxed{
\textbf{SGR-4D — STRUCTURAL PARTIAL}.
}
\]

---

# 15. 唯一剩余 terminal gap

从现在起，不建议再把 DD 的剩余问题拆成：

- square-spacing gap；
- valuation gap；
- near-\(S\)-unit gap；
- factor-overload gap；

四个平行目标。

它们已经统一为：

\[
\boxed{
\textbf{DD Post-Deflation Small-Factor Gap}.
}
\]

精确定义：

\[
\boxed{
J
=
M-Y
=
\frac{\min(F_-,F_+)}{
UR^2\,10^{\lceil m_3/2\rceil}
}.
}
\]

完整候选要求

\[
J\in\mathbf Z_{\ge1}.
\]

旧 DD 顶部已知：

1. \(F_-,F_+\) 同时具有 \(2\)-、\(5\)-进 resonance；
2. 去掉共同赋值后存在深 Hensel phase；
3. \(\kappa,\kappa+2G\) near-\(S\)-unit；
4. denominator / numerator 极端不对称；
5. \(n_3\) 落在
   \[
   10S_{12}+11\le n_3\le11S_{12}+3.
   \]

但目前尚未证明其中任一项能在除掉巨大公共格点尺度

\[
\Lambda
=
UR^2\,10^{\lceil m_3/2\rceil}
\]

之后继续留下足够强的 size/valuation surplus。

下一步只需要证明以下两个等价风格中的任意一个：

### Archimedean form

\[
\boxed{
0<
\min(F_-,F_+)
<
\Lambda.
}
\]

### Valuation-overload form

令

\[
D_0=2^{j_2}5^{j_5},
\]

证明

\[
\boxed{
D_0\mid J,
\qquad
D_0>J.
}
\]

任一成立即关闭 DD 顶部。

这就是本轮唯一保留的 gap。

---

# 16. 最终 ledger

## NEW PROVED / DERIVED

1. DD 的 old/new exact scale：
   \[
   X_{\rm old}=\Lambda M.
   \]

2. old perturbation 与 unified error：
   \[
   \Delta_{\rm old}=\Lambda^2E/\varepsilon.
   \]

3. 无量纲误差完全一致：
   \[
   \rho=\Delta_{\rm old}/X_{\rm old}^2.
   \]

4. old square root 处于子格：
   \[
   Y_{\rm old}=\Lambda Y.
   \]

5. old resonance factors 精确对应：
   \[
   \{F_-,F_+\}
   =
   \{\Lambda(M-Y),\Lambda(M+Y)\}.
   \]

6. 修正后的 \(Y=0\) square-spacing：
   \[
   E\ge\varepsilon(2M-1).
   \]

7. 强化后的 old-coordinate square gap：
   \[
   \Delta_{\rm old}
   \ge
   \Lambda(2X_{\rm old}-\Lambda).
   \]

8. top double resonance 的实际 \(E\)-valuation：
   \[
   v_p(E)
   =
   v_p(\varepsilon)+2j_p,
   \quad p=2,5.
   \]

9. resonance smooth factor：
   \[
   D_0\mid(M-Y),\qquad
   D_0\mid(M+Y).
   \]

10. tail-to-error valuation sink：
    \[
    v_p(E)
    =
    2m_3+2v_p(Q_{12})+v_p(\mathcal N_{12})
    +t_p-3k_p-2v_p(U)-4v_p(R).
    \]

11. 三类 terminal attack 全部压到
    \[
    J=M-Y.
    \]

---

## NOT PROVED

没有证明：

\[
J=0,
\]

没有证明：

\[
0<J<1,
\]

没有证明：

\[
D_0>J,
\]

也没有得到有效有限高度界。

所以 DD 仍开放。

---

# 17. 最终裁决

\[
\boxed{
\textbf{SGR-4D — STRUCTURAL PARTIAL}
}
\]

\[
\boxed{
\textbf{DD NOT CLOSED}.
}
\]

本轮的真正推进是：

\[
\boxed{
\text{“DD 很尖”}
\quad\Longrightarrow\quad
\text{“所有旧尖角结构都作用于同一个整数 }J=M-Y\text{”。}
}
\]

但还没有完成最后一步：

\[
\boxed{
\text{把 }J\ge1\text{ 变成不可能。}
\]

下一轮若继续 DD，不应再扩张分类；
只应攻击

\[
\boxed{
J
=
\frac{\min(F_-,F_+)}{
UR^2\,10^{\lceil m_3/2\rceil}
}.
}
\]

