# 三项十进制拼接平方和问题：审计后结果快速索引（v2）

> 本索引只列统一符号、最终有效定理、依赖、计算状态和未解决部分。  
> 完整陈述及证明概要见 `proved_results_report_v2.md`。

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
| 纯数学已证明 | T1–T18 |
| 待独立机械复核 | 无已升级项目 |
| 有限计算观察 | E1–E7 |
| 已撤回 | “E1 已机器排除临界 \(n\le4\)”；“E4 覆盖整个 \(b_i\le100,\ t<100000\) 盒”；“E6 覆盖两个完整有限盒” |
| 开放问题 | 临界层 T14–T15 联合系统；严格层四大类开放叶节点 |

T10、T12、T18 经本轮独立补证后仍列为纯数学已证明。`audit_response.md`
给出三条完整证明。

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

最终清单为空。特别地：

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

1. 临界层：尚未判定 T14 的完整充要系统对任意 \(n\ge2\) 是否有解。
2. 严格层：第一最大六射线尚未排除。
3. 严格层：第二唯一最大、第三唯一最大以及第二第三共同最大分支仍含无限族。
4. 逐素数局部吸收条件尚不能推出同一个全局整数 \(w\) 不存在。
5. 尚未找到满足原题全部条件的合法解。
6. 尚未证明原题全局无解。

> **截至本报告，尚未证明原命题有解或无解。**

等分母条件不在开放列表中，因为 T10 经独立补证后仍成立。

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

## 10. 相关程序

- [critical_support_search.cpp](critical_support_search.cpp)：E1。
- [critical_b1_2_pyth_search.cpp](critical_b1_2_pyth_search.cpp)：E2。
- [pyth_profile_search.cpp](pyth_profile_search.cpp)：E3。
- [coprime_denominator_ray_search.cpp](coprime_denominator_ray_search.cpp)：E4；只覆盖 \(L\mid B\) 的分母子族。
- [strict_pell_subfamily.cpp](strict_pell_subfamily.cpp)：E5。
- [direct_conic_solution_search.cpp](direct_conic_solution_search.cpp)：E6；只覆盖二次项系数非零分支。
- [global_gcd_profile_search.cpp](global_gcd_profile_search.cpp)：E7。

## 11. 后续升级：O1

| 编号 | 最终结论 | 性质 | 依赖 |
|---|---|---|---|
| O1 | \(\mathrm O\Rightarrow\) 无候选 | 完整模板无解；纯数学分支闭包加独立机器证书 | UB1、OD1、OR2、ON1、OPF4、LC2、P3-1–P6-1 |

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
