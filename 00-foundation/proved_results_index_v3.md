# 三项十进制拼接平方和问题：审计后结果快速索引（v3）

> 本索引只列统一符号、最终有效定理、依赖、计算状态和未解决部分。  
> 完整陈述及证明概要见 `proved_results_report_v3.md`。v2 文件保持不变。

## 1. 统一符号

\[
A=\operatorname{concat}(a_1,a_2,a_3),\qquad
B=\operatorname{concat}(b_1,b_2,b_3),
\]

\[
\alpha_i=\ell(a_i),\qquad
\beta_i=\ell(b_i),\qquad
\delta_i=\alpha_i-\beta_i,
\]

\[
\Delta=\delta_1+\delta_2+\delta_3,\qquad
m=\max_i\delta_i,
\]

\[
q_i=\frac{a_i}{b_i},\qquad
R=\frac AB,
\]

\[
L=\operatorname{lcm}(b_1,b_2,b_3),\qquad
x_i=\frac{La_i}{b_i},\qquad
t=\frac{LA}{B},
\]

\[
G=\gcd(A,B).
\]

分母核：

\[
H=\gcd(B,L),\qquad
B=HM,\qquad
L=HN_L,\qquad
\gcd(M,N_L)=1.
\]

临界层：

\[
n=\beta_2,\quad T=10^n,\quad S=10^{\beta_3},
\quad a=a_1,\quad b=b_1,
\]

\[
F=aT+10a_2,\quad
D=bT+b_2,\quad
s=bb_2,\quad
N_0=(ab_2)^2+(ba_2)^2.
\]

## 2. 证明等级总表

| 状态 | 当前项目 |
|---|---|
| 纯数学严格证明 | T1–T18 及已经逐正文证明的分支定理，包括 GE2-1、GALMB-3 |
| 项目内精确机器辅助证明 | O1；周期证书叶节点 LC2、P3-1、P4-1、P5-1、P6-1；GA1-1 的低层有限证书；GC3-1 的 C3 因子证书 |
| 项目外独立复运行 | O1 证书包尚待完成；GA1-1 低层已在项目内独立重建，但尚非第三方复现 |
| 有限计算观察 | E1–E7 |
| 已撤回 | “E1 已机器排除临界 \(n\le4\)”；“E4 覆盖整个 \(b_i\le100,\ t<100000\) 盒”；“E6 覆盖两个完整有限盒” |
| 开放问题 | 临界 G 的 A2 主二进室（高 \(\varphi\) 为 GFPmB-4 比例长度禁字，低 \(\varphi\) 为移动模数残余）、B、C1/C2、\(\gamma>1\)、非本原 C2/C5，临界 Q；严格层四大类开放叶节点 |

T10、T12、T18 经本轮独立补证后仍列为纯数学已证明。`audit_response.md`
给出三条完整证明。

O1 的规范等级表述为

\[
\boxed{\text{项目内已完成的精确机器辅助定理；项目外独立复运行尚未完成。}}
\]

## 3. 最终定理清单

| 编号 | 最终结论 | 性质 |
|---|---|---|
| T1 | \(x_1^2+x_2^2+x_3^2=t^2\)，且 \(t=LA/B\in\mathbb Z_{>0}\) | 必要结论 |
| T2 | \(\displaystyle B/G=L/\gcd(t,L)\)，特别地 \(B/G\mid L\) | 必要条件 |
| T3 | \(d_i=\gcd(x_i,L)\)、\(a_i=x_i/d_i\)、\(b_i=L/d_i\) 给出双向重构；规范化需 \(\gcd(x_1,x_2,x_3,L)=1\) | 双向构造 |
| T4 | 本原勾股四元组 \(p_1^2+p_2^2+p_3^2=q^2\) 与互素尺度 \(U,V\) 的剖面参数化 | 双向等价 |
| T5 | \(m-1\le\Delta\le m+2\) | 必要条件 |
| T6 | \(\delta_2+\delta_3\ge0\) | 必要条件 |
| T7 | \(G\ge3\) 且 \(\gcd(G,10)=1\) | 必要条件 |
| T8 | 若 \(v_2(L)>0\)，最大 \(v_2(b_i)\) 恰出现一次，\(t\) 为奇数，且 \(v_2(b_3)\ge\min(v_2(L),\beta_3)\) | 必要条件 |
| T9 | \(M\mid A\)；\(N_L\) 为奇数；\(p\mid N_L\) 时最大 \(v_p(b_i)\) 恰出现两次，且 \(p\equiv1\pmod4\) | 必要条件 |
| T10 | \(b_1=b_2=b_3\) 时无解；下降发生在固定拼接权的齐次整数方程组内，不要求商继续是十进制块 | 分支无解 |
| T11 | 临界层只可能有 \((\delta_2,\delta_3)=(-1,1)\) | 临界必要条件 |
| T12 | 临界层 \(b_1\in\{1,2\}\)，第一块仅十三种；枚举已用精确不等式独立封闭 | 临界必要条件 |
| T13 | 临界层 \(N_L\) 是 \(\gcd(b_2,b_3)\) 的最大与 \(10\) 互素因子 | 临界必要条件 |
| T14 | 临界层的 \(\rho,w,\sigma\) 判别及 \(a_3,b_3\) 重构 | 双向等价 |
| T15 | 临界平方条件的 Pell 形式；\(\rho^{(10)}\mid sD\)；\(\beta_3\le6n+5\) | 等价或必要条件 |
| T16 | 严格层第一坐标最大时的支配不等式 | 必要条件 |
| T17 | 严格层第一坐标最大时只剩六射线 | 子分支完整分类 |
| T18 | 四条指定射线分别满足 \(b_1+1>(49/50)10^{\beta_1}\) 或 \(b_1+1>(99/100)10^{\beta_1}\) | 必要条件 |
| GA1-1 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{A1}\Rightarrow\) 无候选 | 完整交分支无解；低层精确整数证书加纯符号终端删除 |
| GE2-1 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{A2},\mathrm E_2\Rightarrow\) 无完整候选；全部完整 A2 候选满足 \(v_2(k^2-1)=2a\) | 纯数学分支无解与尺度升级定理 |
| GALMB-3 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{A2},1\le\varphi<a\) 的两个符号、任意深度均有统一多块递归、正缺陷下降及逐状态唯一有限指数段 | 纯数学双向结构定理；移动 \(r\) 与 \(\operatorname{ord}_r(10)\) 仍开放 |
| GC3-1 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{C3}\Rightarrow\) 无完整候选 | 精确有限因子证书加纯二进判别式/尺度删除 |

## 4. 临界层完整判别

临界层必有

\[
\alpha_2=n-1,\qquad \beta_2=n,\qquad
\alpha_3=\beta_3+1,
\]

以及 T12 的十三种 \((a,b)\)。

定义

\[
\Omega(\rho)=
\rho\left[
\rho(s^2F^2-D^2N_0)-2sD^2N_0
\right],
\]

\[
P_\sigma=\rho Fs^2+\sigma(\rho+s)w,\qquad
Q=sD\rho(\rho+2s),
\]

\[
g_\sigma=\gcd(P_\sigma,Q),\qquad
K_\rho=\rho^2(\rho+2s).
\]

存在合法第三块，当且仅当存在

\[
\rho\in\mathbb Z_{>0},\quad
w\in\mathbb Z_{\ge0},\quad
\sigma\in\{-1,1\}
\]

满足

\[
sD<\rho\le10sD,
\]

\[
\Omega(\rho)=w^2,
\]

\[
P_\sigma>0,
\]

\[
\frac{K_\rho}{g_\sigma}=10^{\beta_3},\qquad \beta_3\ge1,
\]

\[
K_\rho\le P_\sigma<10K_\rho.
\]

重构：

\[
a_3=\frac{P_\sigma}{g_\sigma},\qquad
b_3=\frac{Q}{g_\sigma}.
\]

\(\Omega(\rho)\) 为平方本身不充分。

Pell 形式：

\[
A_0=s^2F^2-D^2N_0,\qquad
C_0=2sD^2N_0,
\]

\[
\rho=d_0u^2,\qquad w=d_0uv,\qquad
v^2-A_0u^2=-C_0/d_0,
\]

其中 \(d_0\mid C_0\) 平方自由、\(u>0\)、\(v\ge0\)。还必须保留纯 \(10\) 次幂和位数条件。

## 5. 位数分支

### 临界层

\[
\delta_2+\delta_3=0
\Longrightarrow
(\delta_2,\delta_3)=(-1,1).
\]

### 严格层

\[
\delta_2+\delta_3\ge1.
\]

若 \(\delta_1=m\)，当 \(m\ge2\) 只可能有

\[
(m,m,1-m),\ (m,1-m,m),
\]

\[
(m,m-1,2-m),\ (m,2-m,m-1),
\]

\[
(m,m,2-m),\ (m,2-m,m).
\]

当 \(m=1\) 退化为

\[
(1,1,0),\quad(1,0,1),\quad(1,1,1).
\]

若第二坐标唯一最大：

\[
(\delta_1,\delta_2,\delta_3)=(k-r,m,r),
\]

\[
k\in\{-1,0,1,2\},\qquad
m>\max(r,k-r),\qquad m+r\ge1.
\]

若第三坐标唯一最大：

\[
(\delta_1,\delta_2,\delta_3)=(k-r,r,m)
\]

并满足同样限制。

若第二、第三坐标共同最大且第一坐标较小，只可能有

\[
(-m-1,m,m),\quad(-m,m,m),\quad(1-m,m,m),\quad(2-m,m,m),
\]

其中 \(m=1\) 时删去最后一个重复点。

## 6. 机器辅助结论

当前已接受的项目内精确机器辅助结论为 O1；其周期证书叶节点如下：

| 定理 | 种子数 | 实际标签数 | 最终残余 | 证书类型 |
|---|---:|---:|---:|---|
| LC2 | 188 | 8,744 | 0 | P1/SP/CRT |
| P3-1 | 868 | 443,208 | 0 | P1/SP/CRT |
| P4-1 | 6,932 | 33,979,575 | 0 | 流式 P1/SP/CRT |
| P5-1 | 24,288 | 1,219,914,182 | 0 | 二维周期筛 |
| P6-1 | 161,230 | 71,356,340,660 | 0 | 二维周期筛 |

这些证书覆盖 \(m=m_*+\ell M\)、\(\ell\ge0\) 的全部无界指数周期，不是有限
试验 \(\ell\)。“实际标签数”不是原题六元组枚举数。各验证器属于项目内独立实现；
项目外第三方复运行尚未完成。

旧程序的等级不随 O1 改变。特别地：

`critical_support_search.cpp` 的 \(n=2,3,4\) 输出不列为机器证明，因为：

1. 当前代码跳过 \(\Omega(\rho)=0\)；
2. 阿基米德剪枝使用未附定向舍入证书的 `long double` 常量。

因此相关数据只属于计算观察。

`direct_conic_solution_search.cpp` 还跳过二次项系数为零的一次方程分支；
`coprime_denominator_ray_search.cpp` 实际只覆盖 \(L\mid B\) 的特定分母子族。

## 7. 主要计算观察

| 编号 | 范围 | 输出性质 |
|---|---|---|
| E1 | 临界 \(n=2,3,4\)，理论消去 \(\beta_3,a_3,b_3\) 后搜索 \(\rho\) | 检查到的候选中未命中纯 \(10\) 次幂 |
| E2 | 临界本原球面参数化的外层源码参数不超过 \(200\) | 未发现完整拼接命中 |
| E3 | 外层参数 \(\tau\le50\)、\(V\le2000\)，并逐一循环 \(1\le\alpha_3\le18\) | 未发现剖面命中 |
| E4 | \(b_i\le100,\ t<100000\)，且只限 \(L\mid B,\ \gcd(B/L,10)=1\) 的分母子族 | 未发现完整命中 |
| E5 | 严格层特殊 Pell 子族 \(j\le3\) | 未发现命中 |
| E6 | 两个固定分子位数、有限分母盒中的二次项系数非零分支 | 出现代数整数点，但没有逐项既约解；退化一次方程未覆盖 |
| E7 | 公共尺度与剖面相容性诊断及显式失败候选 | 只满足部分代数条件，没有原题解 |

所有这些都是有限计算结果，不是全局证明。

## 8. 未解决部分

临界层当前必须分模板记录：

\[
\boxed{
O\text{ 已关闭},\qquad
G\text{ 的 A1 与 A2 异常二进室已关闭；低 }\varphi
\text{ 已统一正规化而移动模数残余开放},\qquad
Q\text{ 开放}.
}
\]

1. 临界 G：\(G_{\mathrm{prim}},\gamma=1,\mathrm{A1}\) 已由 GA1-1 关闭；A2 的 \(a=2\) 与整个异常二进室已关闭，全部完整 A2 候选只允许 \(v_2(k^2-1)=2a\)。高 \(\varphi\) 的 \(\mathcal F_{P-}\) 已由 GFPmB-4 统一为同一二进 inverse–Bezout 塔，但比例长度禁字仍开放；低 \(\varphi\) 已由 GALMB-3 对两个符号和任意深度压成有限块 involution、统一正缺陷下降和逐状态唯一有限指数段，但移动 \(r\) 与 \(\operatorname{ord}_r(10)\) 仍开放。B 及 C1/C2 的 \(\gamma=1\) 状态仍开放，C3 已由 GC3-1 关闭；全部 \(\gamma>1\) 和非本原 C2/C5 也仍开放。
2. 临界 Q：K5–E4 移动系数系统仍含无界 \(m,n,a,q_0,g,e\)。
3. 严格层：第一最大六射线尚未排除。
4. 严格层：第二唯一最大、第三唯一最大以及第二第三共同最大分支仍含无限族。
5. 逐素数局部吸收条件尚不能推出同一个全局整数 \(w\) 不存在。
6. 尚未找到满足原题全部条件的合法解，也尚未证明原题全局无解。

> **截至本报告，尚未证明原命题有解或无解。**

等分母条件不在开放列表中，因为 T10 经独立补证后仍成立。
O 也不在开放列表中，因为 O1 已关闭整个临界 O 模板。

## 9. 依赖表

| 编号 | 类型 | 依赖 |
|---|---|---|
| T1 | 纯数学证明 | 原命题 |
| T2 | 纯数学证明 | T1 |
| T3 | 纯数学证明 | T1 |
| T4 | 纯数学证明 | 有理球面表示 |
| T5 | 纯数学证明 | 原命题 |
| T6 | 纯数学证明 | T4 |
| T7 | 纯数学证明 | T2 |
| T8 | 纯数学证明 | T1、T2 |
| T9 | 纯数学证明 | T1、T2 |
| T10 | 纯数学证明 | 原命题 |
| T11 | 纯数学证明 | T4、T6 |
| T12 | 纯数学证明 | T11 |
| T13 | 纯数学证明 | T9、T12 |
| T14 | 纯数学证明 | T11、T12 |
| T15 | 纯数学证明 | T14 |
| T16 | 纯数学证明 | T5、T6 |
| T17 | 纯数学证明 | T5、T6、T16 |
| T18 | 纯数学证明 | T16、T17 |
| CKD、CKA、CKO | 纯数学结构定理 | T1–T18、K5 |
| OP5 | 精确有限计算支持的结构结果 | CKO |
| OSC | 纯数学结构定理 | OP5 |
| UB1、OD1、OR2、ON1 | 分支无解定理 | OSC 及前序分支正规化 |
| OPF4 | 精确整数计算支持的双向结构定理 | ON1、OSC |
| LC2 | 项目内精确机器辅助证明 | OPF4 |
| P3-1 | 项目内精确机器辅助证明 | OPF4、LC2 |
| P4-1 | 项目内精确机器辅助证明 | OPF4、P3-1 |
| P5-1 | 项目内精确机器辅助证明 | OPF4、P4-1 |
| P6-1 | 项目内精确机器辅助证明 | OPF4、P5-1 |
| O1 | 项目内精确机器辅助定理；项目外复运行待完成 | UB1、OD1、OR2、ON1、LC2、P3-1–P6-1 |
| GP3 | 纯数学分支定理与结构定理 | VA1、GD1、K5、E4（G 二进分支） |
| CD6 | 纯数学结构定理 | GP3 |
| PR6 | 纯数学结构定理 | GP3、CD6 |
| SD6 | 纯数学结构定理 | PR6 |
| GA1-3 | 精确有限计算支持的双向结构定理 | PR6、SD6、E4（G 二进分支） |
| GA1-1 | 项目内精确机器辅助分支定理；高层与终端删除为纯符号证明 | GA1-3 |
| GA2-6 | 纯数学结构定理；\(a=2\) 关闭含精确有限证书 | PR6、SD6、GA1-1、E4（G 二进分支） |
| GA2H-2 | 纯数学双向递推结构定理 | GA2-6 |
| GFPmZ-6 | 纯数学结构推进；六条零商族仍开放 | GA2H-2、GFPmR-3 |
| GFPmP0-3、GFPmP1-3 | 纯数学结构推进；两个正商族仍开放 | GFPmR-3、GFPmZ-6 |
| GFPmB-4 | 纯数学统一二进塔结构；比例长度禁字仍开放 | GFPmZ-6、GFPmP0-3、GFPmP1-3 |
| GE2-1 | 纯数学分支无解与尺度升级定理 | SD6、GA2-6 |
| GAL-2 | 纯数学双向结构定理 | PR6、SD6、GA2-6、GE2-1 |
| GALS\((\pm)\)-3 | 纯数学浅区反射终端定理 | GAL-2 |
| GALD1\((\pm)\)-3 | 纯数学第一深带低块—商终端定理 | GAL-2、GALS\((\pm)\)-3 |
| GALMB-3 | 纯数学任意深度多块终端定理；移动模数残余开放 | GAL-2、GALS\((\pm)\)-3、GALD1\((\pm)\)-3 |
| GCU-2 / GC3-1 | C1/C2/C3 的统一因子走廊；C3 的精确有限证书关闭 | PR6、SD6、E4（G 二进分支） |

这里的“E4（G 二进分支）”指 `critical_even_edge_2adic_campaign.md`，
不是旧有限计算观察 E4。

## 10. 相关程序

- [critical_support_search.cpp](critical_support_search.cpp)：E1。
- [critical_b1_2_pyth_search.cpp](critical_b1_2_pyth_search.cpp)：E2。
- [pyth_profile_search.cpp](pyth_profile_search.cpp)：E3。
- [coprime_denominator_ray_search.cpp](coprime_denominator_ray_search.cpp)：E4；只覆盖 \(L\mid B\) 的分母子族。
- [strict_pell_subfamily.cpp](strict_pell_subfamily.cpp)：E5。
- [direct_conic_solution_search.cpp](direct_conic_solution_search.cpp)：E6；只覆盖二次项系数非零分支。
- [global_gcd_profile_search.cpp](global_gcd_profile_search.cpp)：E7。

## 11. O1 正式冻结

| 编号 | 最终结论 | 性质 | 依赖 |
|---|---|---|---|
| O1 | \(\mathrm O\Rightarrow\) 无候选 | 完整模板无解；项目内精确机器辅助定理 | UB1、OD1、OR2、ON1、OPF4、LC2、P3-1–P6-1 |

分支闭合表：

| 结果 | 关闭范围 |
|---|---|
| UB1 | \(10Y<c<11Y\) |
| OD1 | \(T-Jb_2=0\) |
| OR2 | \(q=1\) 或 \(5\mid q\) |
| ON1 | \(h>1\) |
| LC2 | \(h=1,n\le2\) |
| P3-1 | \(h=1,n=3\) |
| P4-1 | \(h=1,n=4\) |
| P5-1 | \(h=1,n=5\) |
| P6-1 | \(h=1,n=6\) |

OPF4/OSC 的尾窗给出 \(n\le6\)。各叶节点互斥且穷尽 O，故关闭的是整个 O，
而非只关闭本原核心。

P6-1 的规模与筛链：

\[
790{,}252\text{ 个终端种子},\quad
161{,}230\text{ 个存活种子},\quad
71{,}356{,}340{,}660\text{ 个标签},
\]

\[
71{,}356{,}340{,}660\to5{,}000{,}701{,}696\to1{,}820{,}851{,}307
\to298\text{ 标签、}325\text{ 状态}\to0.
\]

证书包 SHA-256：

```text
1ef4b80fee7dac6a65a63855c93793d10f0dfe93226ae246056470b36aa3cb4a
```

复核：

```bash
python3 verify_O_n6_bivariate_period_certificates.py \
  critical_O_n6_bivariate_period_certificates.tar.gz --destruction-tests
```

开放列表中的临界 O 叶节点据此删除；G、Q 与严格层仍开放，原题全局状态不变。

证明等级：项目内独立生成器与验证器已经通过；这不表示第三方已经独立复现。
项目外独立复运行尚未完成。

## 12. GA1-1 正式冻结

| 编号 | 最终结论 | 性质 | 依赖 |
|---|---|---|---|
| GA1-1 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{A1}\Rightarrow\) 无候选 | 完整交分支无解；低层精确整数证书与纯符号终端删除 | PR6、SD6、GA1-3 |

GA1-3 的完备二分为

\[
\mathscr S=\mathscr S_{\mathrm{lo}}\cup\mathscr S_{\mathrm{hi}}.
\]

高层只允许偶数 \(E\ge6\)。此时

\[
r=k-2\cdot5^E\equiv15\pmod{16},
\]

\[
\left(\frac{-1}{r}\right)=-1,
\qquad
\left(\frac2r\right)=1.
\]

又由 \(v_5(k^2-1)\ge2\) 得 \(r\equiv\pm1\pmod5\)，故广义二次互反律给出

\[
\left(\frac5r\right)=1.
\]

对 \(B=1,5\) 均有

\[
\left(\frac{4B10^m}{r}\right)=1,
\]

与 \(qr=1+4B10^m\) 模 \(r\) 后的 \((-1/r)=-1\) 矛盾，所以高层为空。

低层完整有限证书已从 GA1-3 的枚举条件独立重建，恰为

\[
(\delta,e,E,J,r,k,n,m_*,M_r)
=(0,3,3,4,2251,2501,5,2229,2250),
\]

\[
(1,2,3,4,2251,2501,5,551,2250).
\]

两行共有

\[
A=125,\quad d=200,\quad k=2501,\quad Y=10^5,
\quad U\in\{125,25\}.
\]

恢复方程关于 \(y=a_2\) 的必要判别式为

\[
\operatorname{Disc}_y
=16d^2k^2\left[
(Ya_1X+a_3)^2
-5001\bigl((dUa_1)^2+a_3^2\bigr)
\right].
\]

若整数根存在，则方括号为平方。差平方分解强迫

\[
Ya_1X+a_3
\le5001\bigl((dUa_1)^2+a_3^2\bigr).
\]

右边由真实窗口小于 \(6\times10^{15}\)，左边因 \(m\ge551\) 大于
\(5\times10^{556}\)，矛盾。该结论统一覆盖两条级数的全部 \(\ell\ge0\)、
两个恢复符号和全部真实数字块窗口。

更新后的 G 开放表：

- 已关闭：本原、\(\gamma=1\)、A1；
- A2：\(a=2\) 已关闭；异常二进室由 GE2-1 关闭；全部完整候选只允许
  \(v_2(k^2-1)=2a\)。高 \(\varphi\) 只剩 \(\mathcal F_{P-}\)；低
  \(\varphi\) 已由 GALMB-3 统一正规化，但移动模数残余仍开放；
- 仍开放：B 及 C1/C2 的 \(\gamma=1\) 状态；C3 已由 GC3-1 关闭；
  全部 \(\gamma>1\)；非本原 C2、C5。

不得把 GA1-1 或 GE2-1 解释为整个 G 无解。

## 13. GE2-1 正式冻结

| 编号 | 最终结论 | 性质 | 依赖 |
|---|---|---|---|
| GE2-1 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{A2},\mathrm E_2\Rightarrow\) 无完整候选；全部完整 A2 候选满足 \(v_2(k^2-1)=2a\) | 纯数学分支无解与尺度升级定理 | SD6、GA2-6 |

记

\[
\mathcal A=2ZH_1,\qquad
R=(5^ea_1)^2+(2a_2)^2,\qquad
K=k^2-1,
\]

\[
w_0^2=\mathcal A^2-KR,\qquad
L_\varepsilon=\mathcal A+\varepsilon kw_0,
\]

\[
\alpha=v_2(K),\qquad
u_2=v_2(H_1)\ge1,\qquad
A_2=v_2(\mathcal A)=2a+u_2.
\]

异常室 \(\alpha\ge2A_2\) 使判别式两项都被 \(2^{2A_2}\) 整除，故

\[
v_2(L_+)\ge A_2,\qquad v_2(L_-)\ge A_2.
\tag{13.1}
\]

若 \(L_\varepsilon\) 完成恢复，则

\[
d=\frac K{\gcd(K,L_\varepsilon)}=2^a5^\varphi
\]

精确强迫

\[
v_2(L_\varepsilon)=\alpha-a.
\tag{13.2}
\]

共轭乘积

\[
L_+L_-=K(k^2R-\mathcal A^2)
\]

的第二因子为奇数，所以

\[
v_2(L_+)+v_2(L_-)=\alpha.
\]

由 (13.2) 得 \(v_2(L_{-\varepsilon})=a\)，与 (13.1) 及
\(A_2=2a+u_2>a\) 矛盾。该证明同时覆盖
\(\alpha=2A_2\)、\(\alpha>2A_2\)、\(w_0=0\)、负共轭因子和零因子攻击。

GA2-6 原二分

\[
\alpha=2a
\qquad\text{或}\qquad
\alpha\ge2A_2
\]

本身正确；GE2-1 删除第二个过宽必要室，故升级为

\[
\boxed{v_2(k^2-1)=2a.}
\]

该证明不依赖 \(\varphi\ge a\)。因此高 \(\varphi\) 的
\(\mathcal F_{E-}\) 被一并关闭；联合既有 \(\mathcal F_+\) 关闭后，只剩
\(\mathcal F_{P-}\)。其六条零商族仍含移动高位 Bezout 正规形，
\(\mathscr P_0,\mathscr P_1\) 每个递推状态至多一个显式候选，但尚未统一
关闭。不得把 GE2-1 解释为整个高 \(\varphi\) 区或整个 A2 无解。

完整证明见 `critical_G_A2_exceptional_binary_resolution.md`。

## 14. GALMB-3 正式冻结

| 编号 | 最终结论 | 性质 | 依赖 |
|---|---|---|---|
| GALMB-3 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{A2},a\ge3,1\le\varphi<a,\sigma=\pm1\) 的任意深度均有统一多块递归、正缺陷下降和逐状态唯一有限指数段 | 纯数学双向结构定理；移动模数残余开放 | GAL-2、GALS\((\pm)\)-3、GALD1\((\pm)\)-3 |

置

\[
\Delta=a-\varphi,\quad M=2^{2a},\quad C=5^{2\varphi},\quad
\Lambda=5^{3\Delta},\quad B=MC,
\]

\[
3\Delta=\nu(2\varphi)+r_0,\quad
0<r_0\le2\varphi,\quad R=5^{r_0},\quad \Lambda=C^\nu R.
\]

整除时采用 \(r_0=2\varphi\) 的正余数约定。\(\nu=0\) 是浅区，
\(\nu=1\) 是第一深带，\(\nu\ge2\) 覆盖全部更深带。

若

\[
G_j(X,Y)=\eta_j+\alpha_jX+\beta_jY+\gamma_jXY,
\]

则第 \(j\) 个输入块 \(u_j\) 唯一决定

\[
\theta_j=\langle-\sigma\eta_j\rangle_C,\qquad
v_j=\langle\theta_j-u_j\rangle_C,
\]

并保持

\[
\alpha_j\beta_j-\gamma_j\eta_j=1,\qquad
\alpha_j\equiv\beta_j\equiv\sigma\pmod C,\qquad C\mid\gamma_j.
\]

末块模 \(R\) 也唯一反射，整个递归与原模 \(\Lambda\) 图严格双向等价；
不存在逐位 Hensel 输出树。这里无输出分支不表示输入块字数绝对有界。

每个允许块字唯一恢复 \(q_0,r,s_0,N_0\)，且

\[
q_0r=1+B\Lambda N_0,\qquad
0<s_0<q_0,\quad 0<N_0<r,\quad \gcd(N_0,r)=1.
\]

以

\[
A^\sharp=1+\langle N_0-1\rangle_M,\qquad
\mathcal D^\sharp=\frac{A^\sharp r-N_0}{M}
\]

规范化后，

\[
0<\mathcal D^\sharp<r,\qquad
\gcd(\mathcal D^\sharp,r)=1,\qquad
2^\delta10^\mu=zr-\mathcal D^\sharp,\quad z\ge1.
\]

全部符号与深度共有离散对数门

\[
\boxed{2^{2a+h}10^{\mu+2a+\Delta}\equiv-1\pmod r.}
\]

若目标在 \(\langle10\rangle\) 中，每个固定块状态的全部指数恰为一条完整
有限段

\[
\mu=\mu_0+t\operatorname{ord}_r(10),\qquad
t_{\min}\le t\le t_{\max};
\]

否则为空。

全部深度还统一满足

\[
v_2(q-r)=2a+1,\quad v_5(q-r)=2\varphi,
\qquad
v_2(q+r)=1,\quad v_5(q+r)=0.
\]

允许状态中 \(q\ne r\)；\(q<r\) 只可能在最小 \(z=1\)，而
\(A^\sharp=M,z=1\) 给 \(y=0\) 与 \(q<r\)。

计数需保留一个端点修正。根门对每个符号恰有 \(2\Lambda/5\) 个有向状态；
正根固定 \(J\) 后恰为 \(\Lambda/5\)。负根令

\[
\alpha_{-,d}=\langle M^{-1}(d-x)\rangle_5,\quad d=2,3,\qquad
p_{-,J}\equiv1-c-J\pmod2,
\]

则

\[
\#_{-,J}=
\begin{cases}
\Lambda/5,&\{\alpha_{-,2},\alpha_{-,3}\}\ne\{0,4\},\\
\Lambda/5+(-1)^{p_{-,J}},
&\{\alpha_{-,2},\alpha_{-,3}\}=\{0,4\}.
\end{cases}
\]

因此负根逐 \(J\) 计数不恒为 \(\Lambda/5\)；旧负根报告原用 floor-sum
公式正确，不构成继承错误。

对 \(J=1,\ldots,9\) 求和后，两个符号合计为

\[
\sum_{\sigma,J}\#_{\sigma,J}=
\begin{cases}
18\Lambda/5,&\{\alpha_{-,2},\alpha_{-,3}\}\ne\{0,4\},\\
18\Lambda/5+(-1)^c,&\{\alpha_{-,2},\alpha_{-,3}\}=\{0,4\}.
\end{cases}
\]

最后，

\[
\frac{2^{2a+h}10^{\mu+2a+\Delta}+1}{r}=q,
\]

故统一商只是终端乘积恒等式回代。Jacobi、固定外部素数、窗口、大小门和当前
阶估计没有关闭移动模数。开放障碍只在移动 \(r\)、离散对数成员性及
\(\operatorname{ord}_r(10)\)，不再在五进深度。分类为 GALMB-3，不是整个低
\(\varphi\) 区无解。

完整证明见 `critical_G_A2_low_phi_full_multiblock_campaign.md`。

## 15. GCU-2 / GC3-1 正式冻结

| 编号 | 最终结论 | 性质 | 依赖 |
|---|---|---|---|
| GC3-1 | \(G_{\mathrm{prim}},\gamma=1,\mathrm{C3}\Rightarrow\) 无完整候选 | 精确有限因子证书加纯二进终端删除 | PR6、SD6、E4（G 二进分支） |

本原 C、\(\gamma=1\) 的统一尺度为

\[
N=5^R,\qquad Z=2^A5^{A+S-R},\qquad
m=A+H(S),
\]

且单位行列式终端与

\[
q\mid1+10^A5^S,qquad
\frac{5^R}{J+1}<q<\frac{5^R}{J}
\]

中的奇因子严格一一对应。C1、C3、C2 分别为 \(A<a,A=a,A>a\)。

C3 中完整尺度恢复迫使

\[
q^2\equiv1\pmod{2^a},\qquad
2^{a-3}\mid R,qquad3R<17a,
\]

故 \(2\le a\le8\)。规范筛链为

\[
2106\to49\to26\to11\to0.
\]

最后 11 个状态中，九个的判别式二进赋值为奇数，一个违反互补二进尺度门，
一个的归一化判别式为 \(7\bmod8\)。因此整个 C3 关闭。

C2 只剩

\[
(\eta_2,A)=(1,2a-2)
\quad\text{或}\quad
(2+v_2(R),2a-3-v_2(R)),
\]

C1 获得 \(\eta_2=A+d\) 的有限 \(d\)–奇 \(W\)–CRT 走廊；两室仍开放。
总分类为 GCU-2。

证书 SHA-256：

```text
c0e67cbd97bd5b0dc4471b491cf380d0379813384f29a4af9a170119f0856e9d
```

复核：

```bash
python3 verify_G_C3_factor_certificate.py --destruction-tests
```

完整证明见 `critical_G_C_gamma1_unit_determinant_campaign.md`。
