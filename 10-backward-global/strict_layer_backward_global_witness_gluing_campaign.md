# 三项十进制拼接平方和问题：Backward Strict Layer Global Recovery-Witness Gluing Campaign

**文件名：** `strict_layer_backward_global_witness_gluing_campaign.md`  
**轮次：** Backward Strict Layer — Global Witness Gluing / Synchronization  
**研究范围：** 只研究 Exact-Lift 完整恢复所需的 global witness 如何由局部 recovery constraints 同步实现；不进入任何具体 \(A_2\)、DD、\(A_1\) 分支，不推进 moving primitive-core termination，不直接证明上一轮 B1/B2/B3。

---

# 1. Executive summary

本轮得到的最重要总体简化是：

\[
\boxed{
\text{Backward Strict Layer 的自然本体不是三个 obstruction family，}
}
\]

而是

\[
\boxed{
\textbf{一个 canonical global recovery witness}
+
\textbf{若干作用在其投影上的 compatibility relations}.
}
\]

第一轮使用

\[
B_{\rm arith},\qquad B_{\rm root},\qquad B_{\rm dec}
\]

组织失败机制是有用的，但它们不是三个彼此独立的数学空间。尤其：

- root divisibility 与 denominator recovery 共享同一个既约 root；
- \(10^\ell\)-tail divisibility 同时读取 algebraic denominator 与 decimal tail；
- digit window、局部 \(p\)-进根、coefficient plane 都必须作用在**同一个整数代表 / 同一个完整候选**上；
- 一个完整候选一旦固定，大量所谓 auxiliary choices 实际只是它的投影或证明证书，而不是新的自由变量。

因此本轮把核心对象改写为：

\[
\boxed{
\mathcal W_{\rm global}(\xi)
}
\]

以及围绕它建立的 relational gluing system。

---

## 1.1 Global witness 的最自然选择

为避免与 Exact-Lift 的 tail quotient \(L\) 混淆，本报告把 T3 的 canonical common denominator 记为

\[
\Lambda.
\]

取

\[
\omega=(x_1,x_2,x_3,t,\Lambda)\in\mathbf Z_{>0}^5
\]

满足

\[
x_1^2+x_2^2+x_3^2=t^2.
\]

令

\[
d_i=\gcd(x_i,\Lambda),
\qquad
a_i=\frac{x_i}{d_i},
\qquad
b_i=\frac{\Lambda}{d_i},
\]

并要求

\[
\gcd(x_1,x_2,x_3,\Lambda)=1
\]

以及 exact decimal balance

\[
\Lambda\,\operatorname{concat}(a_1,a_2,a_3)
=
t\,\operatorname{concat}(b_1,b_2,b_3).
\]

对给定 strict state \(\xi\)，再要求该恢复候选与 \(\xi\) 相容。

定义由这些条件组成的集合为

\[
\boxed{
\mathcal W_{\rm global}(\xi).
}
\]

由既有 T3 双向重构：

\[
\boxed{
\operatorname{Liftable}(\xi)
\iff
\mathcal W_{\rm global}(\xi)\neq\varnothing.
}
\tag{GW}
\]

**等级：DERIVED FROM PROVED RESULTS。**

这里的 iff 不依赖任何新的 Exact-Lift necessary gate；它只依赖已经审计过的 canonical common-denominator reconstruction。

进一步，\(t\) 在 \((x_1,x_2,x_3)\) 固定且存在时取正根唯一，所以从“自由度”角度可把真正的 canonical witness spine 压成

\[
\boxed{
\bar\omega=(x_1,x_2,x_3,\Lambda),
}
\]

而把 \(t\) 视作由 sphere condition 唯一恢复的派生量。

---

## 1.2 本轮选择的 gluing 语言

整个 Exact-Lift 体系**不应优先写成一条长 fibre-product chain**。

最自然、最少制造假自由度的语言是：

\[
\boxed{
\textbf{common-witness constraint system}
}
\]

或等价地：

\[
\boxed{
\textbf{relational CSP / natural join}.
}
\]

理由是不同 recovery gate 通常共享不同变量子集，并形成一个 hypergraph，而不是天然的一条链。

设一组共享 recovery variables 为 \(\mathbf s\)，第 \(j\) 个 gate 只读取坐标子集 \(S_j\)，并定义关系

\[
R_j\subseteq\operatorname{Dom}(S_j).
\]

则所有 gate 的同步空间是自然连接

\[
\boxed{
\mathcal J(\xi)
=
\Join_j R_j.
}
\]

Global obstruction 就是

\[
\boxed{
\mathcal J(\xi)=\varnothing.
}
\]

当两个关系确实只通过一个共同 separator 相连时，

\[
R_1\Join R_2
\]

可以等价写成 fibre product

\[
R_1\times_S R_2.
\]

所以 fibre product 是**局部正确表示**；natural join / CSP 是整个系统更稳健的总语言。

**等级：NEW PROVED**（集合论重写；不增加任何数学假设）。

---

## 1.3 最重要的新分类：obstruction order

定义一个由当前 constraint family \(\mathfrak R=\{R_j\}\) 决定的 obstruction order：

\[
\boxed{
h_{\mathfrak R}(\xi)
=
\min
\left\{
|J|:
\Join_{j\in J}R_j=\varnothing
\right\},
}
\tag{1.1}
\]

若完整 join 非空则置 \(h_{\mathfrak R}(\xi)=\infty\)。

于是：

\[
\boxed{
h=1
\iff
\text{local emptiness},
}
\]

\[
\boxed{
h=2
\iff
\text{pairwise incompatibility 在最小层面已足够},
}
\]

而

\[
\boxed{
h\ge3
\iff
\text{存在真正 higher-order synchronization failure}.
}
\]

这比把死亡区按 arithmetic/root/decimal 三个名字分开更接近真正的逻辑结构。

**等级：NEW PROVED（定义与直接分类）。**

---

## 1.4 本轮对核心问题的回答

当前已证材料不能支持：

\[
\boxed{
\text{所有 non-liftability 都主要来自 synchronization failure}.
}
\]

因为已经存在大量 genuine local emptiness certificates。

但现有严格层开放核明确显示：

\[
\boxed{
\text{在许多局部 gates 分别可满足以后，仍缺少同一个 global witness。}
}
\]

特别是旧严格层报告已经指出：各素数局部吸收可以分别相容，但仍必须由同一个具有正确实大小的整数平方根实现；`strict_layer_final_campaign.md` 的 N4–N5 也表明单纯 valuation-position geometry 对全部位置模式仍局部相容。

所以最准确的结论是：

\[
\boxed{
\text{local emptiness 是已有 death mechanism；}
}
\]

\[
\boxed{
\text{global synchronization 是当前 surviving backward frontier 的逻辑缺口。}
}
\]

**等级：DERIVED FROM PROVED RESULTS。**

至于剩余 strict states 是否最终主要由 synchronization 排除，仍是 **OPEN / HEURISTIC**，本轮不升级为 theorem。

---

# 2. Anti-duplication boundary and source audit

## 2.1 本轮实际使用的 backward 资料

重点核对：

- `strict_layer_backward_global_obstruction_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`；
- `strict_layer_final_campaign.md`；
- `strict_layer_unified_exact_lift_campaign.md`；
- 当前 File Library 中最新的 strict-layer unified forward report；
- `proved_results_report_v3.md`；
- `final_results_index.md`。

本轮只从这些文件中读取：

1. T3 canonical reconstruction；
2. primitive recovery；
3. Exact-Lift recovery quadratics 与其严格必要 certificate；
4. 旧严格层已经确认的 local-vs-global logical gap；
5. 正向线与 backward 线的责任边界。

---

## 2.2 本轮明确冻结

以下内容不进入新的证明：

- moving primitive-core termination；
- SGR depth quadratic；
- SGR / Exact-Lift 变量桥接；
- resultant coupling；
- fixed-core finite fibre；
- moving-core \(2/5\)-adic capacity；
- \(A_2\)、DD、\(A_1\) 及任何子分支；
- 某个具体 Hensel / Gaussian / near-square / near-\(S\)-unit 分支；
- B1/B2/B3 的直接证明。

因此本报告没有建立新的 strict-layer 无解分支。

---

## 2.3 正向材料在这里的唯一作用

统一正向报告已经确认：

\[
\text{真实 candidate}
\]

必须同时通过多个 nonredundant gates，而不是分别证明每个 gate 自己无解。

本轮只吸收这一**逻辑形式**：

\[
\boxed{
\text{候选必须属于多个 necessary relation 的共同交 / natural join}.
}
\]

不使用正向报告的：

- \(Q_0\to\infty\)；
- resultant polynomial；
- depth bounds；
- moving-core height arguments

来制造 backward 结论。

---

# 3. Global recovery witness

## 3.1 Canonical complete witness

定义 ambient canonical space

\[
\Omega
=
\mathbf Z_{>0}^5
\]

中的元素

\[
\omega=(x_1,x_2,x_3,t,\Lambda).
\]

令

\[
d_i(\omega)=\gcd(x_i,\Lambda),
\]

\[
a_i(\omega)=\frac{x_i}{d_i(\omega)},
\qquad
b_i(\omega)=\frac{\Lambda}{d_i(\omega)}.
\]

定义四个 exact predicates：

### Sphere

\[
R_{\rm sph}(\omega):
\quad
x_1^2+x_2^2+x_3^2=t^2.
\]

### Canonical denominator recovery

\[
R_{\rm can}(\omega):
\quad
\gcd(x_1,x_2,x_3,\Lambda)=1.
\]

### Positive decimal block realization

恢复出的 \(a_i,b_i\) 是正整数，位数由其真实十进制表示定义；该项在当前正整数 ambient space 中不需要额外“digit representative”作为自由 witness。

### Exact balance

\[
R_{\rm bal}(\omega):
\quad
\Lambda A(\omega)=tB(\omega),
\]

其中

\[
A(\omega)=\operatorname{concat}(a_1,a_2,a_3),
\]

\[
B(\omega)=\operatorname{concat}(b_1,b_2,b_3).
\]

最后加入 strict-state compatibility：

\[
R_\xi(\omega):
\quad
\text{由 }\omega\text{ 恢复的数据满足 }\xi\text{ 所固定的信息}.
\]

于是定义

\[
\boxed{
\mathcal W_{\rm global}(\xi)
=
\{
\omega\in\Omega:
R_{\rm sph}\wedge
R_{\rm can}\wedge
R_{\rm bal}\wedge
R_\xi
\}.
}
\tag{3.1}
\]

### DERIVED FROM PROVED RESULTS

T3 给出：

\[
\boxed{
\operatorname{Liftable}(\xi)
\iff
\mathcal W_{\rm global}(\xi)\ne\varnothing.
}
\tag{3.2}
\]

---

## 3.2 哪些量是真正自由 witness？

在 canonical level：

\[
\boxed{
(x_1,x_2,x_3,\Lambda)
}
\]

可以视为最小主自由数据。

因为：

- 若 sphere 成立，\(t>0\) 唯一；
- \(d_i=\gcd(x_i,\Lambda)\) 唯一；
- \(a_i,b_i\) 唯一；
- \(n_i=\ell(a_i),m_i=\ell(b_i)\) 唯一；
- 所有 \(v_p(a_i),v_p(b_i)\) 唯一；
- denominator prime graph 唯一；
- decimal concatenations \(A,B\) 唯一；
- exact coefficient-plane residual 唯一。

因此这些都不应重复塞入 \(W\)。

---

## 3.3 哪些“choices”只是 projected search freedom？

### Gap root \([\mu:\nu]\)

Exact-Lift 的 gap quadratic 可以有两个 algebraic roots，但一个完整候选若产生某个 reduced ratio，则该 ratio 已由候选确定。

所以：

\[
\boxed{
\text{“选择 root”是 projected search freedom，}
}
\]

不是 original candidate 的额外自由度。

### Primitive tail root \(z_3\)

\[
z_3=\frac{a_3}{\delta_3}
\]

由完整候选确定。

理论二次式有多个 roots 不意味着 global witness 有独立的 tail-root choice。

### Discriminant square root \(W\)

符号

\[
W\leftrightarrow -W
\]

通常只是 certificate symmetry；若最终恢复式只读取某个定向 sign，则该 sign 必须由同一个候选/恢复公式决定。

### \(p\)-adic / Hensel branch

局部平方根分支在各个 \(p\) 上是搜索时的选择；完整整数 witness 固定以后，它们是同一个整数在各局部环中的投影。

所以不能把

\[
\forall p\,\exists w_p
\]

当成

\[
\exists w\,\forall p.
\]

### Prime allocation / Gaussian allocation

除非已建立“该 allocation 与原候选之间的 canonical bijection”，否则它只是 factorization certificate / proof coordinate，而不是 \(\mathcal W_{\rm global}\) 的基本坐标。

### Digit-window representative

若先把一个未知整数投影成 residue class，再问其是否进入十进制窗口，则“代表元”在该投影模型中是自由变量。

但在 canonical witness 中，真实整数 block 已经固定，所以代表元只是恢复投影中的临时自由度。

### Coefficient-plane realization

这是 predicate：

\[
R_{\rm plane}(w)=0,
\]

而不是新的 witness coordinate。

---

## 3.4 结论

\[
\boxed{
\text{Global witness 应尽量小；}
}
\]

\[
\boxed{
\text{局部 root / sign / prime / digit choices 应作为 projections 或 certificates。}
}
\]

这一步直接消除了第一轮 framework 中最容易产生的伪自由度。

**等级：DERIVED FROM PROVED RESULTS + NEW PROVED 的组织性结论。**

---

# 4. Local witness spaces

单纯把 global witness 分成

\[
\mathcal W_{\rm arith},
\quad
\mathcal W_{\rm root},
\quad
\mathcal W_{\rm dec}
\]

仍然过粗。

更好的定义方式是：先选定一个 common recovery spine \(\mathcal S_\xi\)，然后让每个 gate 只读取它需要的坐标。

---

## 4.1 Exact kernel relations

这三类属于真正的 recovery kernel：

\[
R_{\rm sph},
\qquad
R_{\rm can},
\qquad
R_{\rm bal}.
\]

它们共同给 T3 exact characterization。

---

## 4.2 Algebraic relations

包括已证明的：

- gap quadratic；
- primitive tail quadratic；
- 非退化 discriminant-square condition；
- 退化线性 root condition；
- positivity / sign / reduced root admissibility。

统一记为

\[
\boxed{
R_{\rm alg}.
}
\]

注意：

\[
R_{\rm alg}\ne\varnothing
\]

只表示有 admissible algebraic recovery data，不表示有完整 candidate。

---

## 4.3 Arithmetic relations

把下列条件编译为共享变量上的 predicates：

- primitive recovery gcd；
- denominator-core condition；
- denominator prime graph；
- reduced numerator / denominator；
- rational-root divisibility；
- \(p\)-adic valuation demand；
- tail denominator divisibility；
- 必要的 prime-allocation feasibility。

统一记为

\[
\boxed{
R_{\rm arith}.
}
\]

这里不应把 \(2\)-adic、\(5\)-adic tail capacity 单列成与 root/decimal 平行的第四世界，因为

\[
10^\ell\mid\kappa^2(\kappa+2G)
\]

本身就是 algebraic denominator recovery 与 decimal tail length 的 cross-projection。

---

## 4.4 Decimal relations

包括：

- exact digit cell；
- exact digit interval/window；
- decimal tail length；
- residue representative 必须落入真实窗口；
- block recovery 后无前导零；
- exact concatenation residual。

统一记为

\[
\boxed{
R_{\rm dec}.
}
\]

其中 exact concatenation balance 最终仍属于 T3 kernel，不应降格为只看近似 coefficient plane 的 necessary gate。

---

## 4.5 Local witness spaces 的正确语义

给定 projection

\[
\pi_j:\mathcal S_\xi\to S_j,
\]

令

\[
\mathcal W_j(\xi)
=
\{s_j\in S_j:R_j(s_j)\}.
\]

则完整 witness 必须投影到每个 \(\mathcal W_j\)：

\[
\boxed{
\omega\in\mathcal W_{\rm global}
\Longrightarrow
\pi_j(\omega)\in\mathcal W_j
\quad\forall j.
}
\]

但：

\[
\boxed{
\forall j,\quad \mathcal W_j\ne\varnothing
}
\]

绝不推出

\[
\boxed{
\mathcal W_{\rm global}\ne\varnothing.
}
\]

因为不同 \(\mathcal W_j\) 中被选中的元素可能来自不同 hypothetical completions。

**等级：NEW PROVED（量词展开）。**

---

# 5. Projection / compatibility architecture

## 5.1 两层模型

本轮建议同时保留两个等价但用途不同的视角。

### Level A — Common-witness pullback

所有必要 gate 都拉回 canonical ambient space：

\[
\widetilde R_j
=
\pi_j^{-1}(R_j)
\subseteq\Omega_\xi.
\]

于是同步只是一组集合的共同交：

\[
\boxed{
\bigcap_j\widetilde R_j.
}
\tag{5.1}
\]

这是**逻辑最安全**的表示，因为所有条件从一开始就要求作用于同一个 \(\omega\)。

### Level B — Projected relational join

为了证明效率，不希望一直携带五个 canonical 坐标及其所有派生值。

于是把每个 gate 编译成低维 relation：

\[
R_j(S_j).
\]

Global synchronized assignments 为：

\[
\boxed{
\mathcal J(\xi)
=
\Join_jR_j.
}
\tag{5.2}
\]

这是**证明最有用**的表示，因为能直接分析 separators、residue classes、intervals、finite root sets。

---

## 5.2 Exact join 与 relaxation join

这里必须区分两种 join。

### Exact join

若 relations 完整编码 T3 recovery，则：

\[
\boxed{
\mathcal J_{\rm exact}(\xi)\ne\varnothing
\iff
\operatorname{Liftable}(\xi).
}
\tag{5.3}
\]

### Certificate relaxation

若只使用 Exact-Lift 已证 necessary certificates，则得到一个更大的 relaxation：

\[
\mathcal J_{\rm cert}(\xi).
\]

严格关系是：

\[
\boxed{
\mathcal W_{\rm global}(\xi)
\subseteq
\mathcal J_{\rm cert}(\xi).
}
\tag{5.4}
\]

因此：

\[
\boxed{
\mathcal J_{\rm cert}(\xi)=\varnothing
\Longrightarrow
\text{not liftable}.
}
\tag{5.5}
\]

但：

\[
\boxed{
\mathcal J_{\rm cert}(\xi)\ne\varnothing
\not\Longrightarrow
\text{liftable}.
}
\tag{5.6}
\]

这是整个 backward gluing theory 最重要的安全阀之一。

**等级：NEW PROVED。**

---

# 6. Fibre-product or alternative gluing model

## 6.1 为什么不用一条固定 fibre-product 链

如果写成

\[
\mathcal W_1
\times_{\mathcal S_1}
\mathcal W_2
\times_{\mathcal S_2}
\cdots,
\]

就隐含了：

1. constraints 有天然线性顺序；
2. 每一步只有一个主要 separator；
3. 早期 glue 的选择不需要被更后面的 relation 重新约束。

当前 Exact-Lift 没有证明这三个性质。

例如：

- 一个 root 同时进入 denominator divisibility 与 digit recovery；
- 同一整数平方根同时受到多个素数的局部条件和实窗口约束；
- exact balance 又读取完整恢复块。

这是 hypergraph overlap，而不是天然 chain。

所以全局主语言选择：

\[
\boxed{
\textbf{constraint hypergraph + natural join}.
}
\]

---

## 6.2 Fibre product 仍然在哪里有用？

若两个 subproblem

\[
R_A(X,S),
\qquad
R_B(S,Y)
\]

只通过共享 separator \(S\) 通信，则：

\[
R_A\Join R_B
\cong
R_A\times_S R_B.
\]

因此未来若成功证明 recovery hypergraph 可化为 join tree，就可以大量使用 fibre products 做局部 glue。

目前尚未证明 full Exact-Lift constraint hypergraph 是 acyclic / join-tree。

**等级：OPEN。**

---

## 6.3 Compatibility hypergraph

定义顶点为真正共享 recovery variables，hyperedge 为 gate scope。

一个合理的宏观图景是：

\[
\boxed{
\text{algebraic root core}
}
\]

连接：

\[
\boxed{
\text{arithmetic / valuation relations}
}
\]

与

\[
\boxed{
\text{decimal / interval relations}
}
\]

最后再连接

\[
\boxed{
\text{exact reconstruction residual}.
}
\]

这不是声称 root 已经被证明是唯一中心变量；只是当前最有希望被进一步压缩的 separator structure。

**等级：HEURISTIC。**

---

# 7. Local emptiness vs synchronization failure

## 7.1 Individual nonexistence

若某个 relation 本身为空：

\[
R_j=\varnothing,
\]

则

\[
\Join_iR_i=\varnothing.
\]

这就是旧式 local obstruction。

例子类型包括：

- recovery quadratic 无 admissible root；
- required gcd profile 本身不可能；
- digit interval 本身为空；
- exact divisibility capacity 已经失败。

**等级：PROVED / trivial join consequence。**

---

## 7.2 Pairwise incompatibility

可能存在

\[
R_i\ne\varnothing,
\qquad
R_j\ne\varnothing,
\]

但

\[
\boxed{
R_i\Join R_j=\varnothing.
}
\]

这才是第一种真正意义上的 gluing obstruction。

典型形式是：

- arithmetic root denominator 要求一个 residue；
- decimal recovery 要求同一变量落入不相容 residue / interval；
- 两个局部 recovery maps 对同一个 block 给出不同值。

---

## 7.3 Higher-order synchronization failure

在一般 constraint systems 中，可以有：

\[
R_i\Join R_j\ne\varnothing
\quad\forall i\ne j,
\]

却有

\[
\boxed{
\Join_iR_i=\varnothing.
}
\]

### NEW PROVED — 抽象可能性

取共享 core

\[
S=\{1,2,3\},
\]

以及

\[
R_1=\{1,2\},\quad
R_2=\{2,3\},\quad
R_3=\{1,3\}.
\]

则每两个集合交非空，但

\[
R_1\cap R_2\cap R_3=\varnothing.
\]

所以：

\[
\boxed{
\text{pairwise compatibility}
\not\Rightarrow
\text{global compatibility}
}
\]

在抽象层面严格成立。

### 对当前 Exact-Lift

当前没有证据证明这种 genuine \(h\ge3\) failure 一定发生，也没有定理排除它。

因此：

\[
\boxed{
\text{Exact-Lift 是否存在 genuine higher-order synchronization failure}
}
\]

为 **OPEN**。

---

# 8. Small incompatibility certificates

本轮最有价值的新问题不是“再找一个 obstruction”，而是研究：

\[
\boxed{
\Join_jR_j=\varnothing
}
\]

能否由很少几个 relations 证出。

---

## 8.1 NEW PROVED — Single-variable CRT certificate theorem

设 fixed branch 上所有 local congruence conditions 都作用于同一个整数 \(w\)：

\[
w\equiv a_i\pmod{m_i}.
\]

则 generalized CRT 给出：

\[
\boxed{
\exists w\ \forall i
\iff
a_i\equiv a_j
\pmod{\gcd(m_i,m_j)}
\quad\forall i,j.
}
\tag{8.1}
\]

因此这一**单 residue class / 单整数**子系统若失败，必有一个 pair 已失败：

\[
\boxed{
h_{\rm CRT}\le2.
}
\tag{8.2}
\]

这说明纯粹的 congruence synchronization 在 branch 已固定后不需要高阶证书。

### 关键限制

如果某个 \(p\)-adic condition 允许：

\[
w\in C_{p,1}\cup C_{p,2}\cup\cdots,
\]

也就是多个 root branches 的并，而不同素数可以选择不同 branch，则必须先处理 branch synchronization。

所以 (8.2) 不能直接升级为 entire Exact-Lift 的 pairwise theorem。

---

## 8.2 NEW PROVED — Finite synchronization-core certificate lemma

设所有 remaining constraints 都已经被编译成同一个有限 core \(S\) 上的 subsets：

\[
R_j\subseteq S,
\qquad
|S|=K.
\]

若

\[
\bigcap_jR_j=\varnothing,
\]

则存在至多 \(K\) 个 constraints 已经交空。

### 证明

对每个 \(s\in S\)，因为全交为空，至少存在一个 relation \(R_{j(s)}\) 使

\[
s\notin R_{j(s)}.
\]

取这些至多 \(K\) 个 relations。任何 \(s\in S\) 都被其中至少一个排除，因此其交为空。证毕。

所以：

\[
\boxed{
h_{\mathfrak R}\le |S|.
}
\tag{8.3}
\]

### 对本题的意义

若未来能证明全部 surviving recovery gates 只需要在：

- 一个非退化 quadratic 的至多两个 admissible roots 上同步，

则自动得到：

\[
\boxed{
h\le2.
}
\]

若需要两个真正独立、各至多两个值的 root coordinates，则最粗得到：

\[
\boxed{
h\le4.
}
\]

目前尚未证明 Exact-Lift 可以 uniformly 压到这样的有限 core。

所以“certificate size 2–4”目前是：

\[
\boxed{\textbf{HEURISTIC / CONDITIONAL}}
\]

而不是现成 theorem。

---

## 8.3 Interval subsystem

对同一个实/整数 recovery variable，有限个区间的交若为空，则已有两个区间不相交。

因此纯 interval family 具有 pairwise certificate。

但本题真正困难不是若干 intervals 彼此求交，而是：

\[
\text{congruence class}
+
\text{integer representative}
+
\text{digit interval}
+
\text{exact residual}.
\]

所以不能把 interval Helly 性直接当成 entire recovery system 的 Helly 定理。

---

## 8.4 最可能的三件套 certificate

上一轮已经严格指出：

\[
M>|I|
\]

只给“某 residue class 在 interval 中至多一个代表”，不自动给空性。

这反而提示一个很自然的 compressed synchronization pattern：

\[
\boxed{
\text{CRT class}
+
\text{digit interval}
+
\text{exact reconstruction residual}.
}
\]

若未来能统一证明：

1. 所有 local arithmetic data 先 collapse 成一个 global residue class
   \[
   w\equiv w_0\pmod M;
   \]
2. digit window \(I\) 满足
   \[
   |I|<M;
   \]
3. 唯一可能 representative 不满足 exact residual；

则 global death 可以由三个低阶对象证出。

这给出候选：

\[
\boxed{
h_{\rm glue}\le3.
}
\]

但目前步骤 1–2 都没有全局统一证明。

**等级：HEURISTIC / OPEN。**

---

## 8.5 本轮对 small certificate 的最强严格结论

当前可以严格声称：

\[
\boxed{
\text{固定 single-class congruence branch 内，failure 有 2-certificate；}
}
\]

\[
\boxed{
\text{若 synchronization core 有限，failure 有 }|S|\text{-certificate。}
}
\]

当前不能严格声称：

\[
\boxed{
\text{整个 Exact-Lift global failure 总有 pairwise 或 triple certificate。}
}
\]

这正是下一轮最值得证明的 structural theorem。

---

# 9. Reinterpretation of \(B_{\rm arith},B_{\rm root},B_{\rm dec}\)

第一轮的三个 basis family 在新语言下应从“本体分类”降级为：

\[
\boxed{
\textbf{minimal-unsatisfiable-support 的粗标签}.
}
\]

---

## 9.1 \(B_{\rm root}\)

最纯粹的 \(B_{\rm root}\) 是：

\[
\boxed{
R_{\rm alg}=\varnothing.
}
\]

这是 obstruction order \(h=1\) 的 local emptiness。

但若“root 存在”而所有 roots 都与 denominator / sign / reducedness 不兼容，则它已经是：

\[
\boxed{
R_{\rm alg}\Join R_{\rm arith}=\varnothing
}
\]

的 pairwise/subjoin failure。

因此 \(B_{\rm root}\) 不是永远 local。

---

## 9.2 \(B_{\rm arith}\)

\(B_{\rm arith}\) 内部至少包含两层：

### Local arithmetic emptiness

某个 canonical gcd / valuation / divisibility relation 自己为空。

### Arithmetic synchronization failure

每个 prime 的局部数据分别可实现，但不存在一个共同 integer / common denominator / allocation 同时实现。

所以：

\[
\boxed{
B_{\rm arith}
}
\]

其实已经混合了 \(h=1\) 与 \(h\ge2\) 两类现象。

---

## 9.3 \(B_{\rm dec}\)

第一轮的 \(B_{\rm dec}\) 最接近本轮主题。

它内部又可拆：

- digit window 自身为空：local emptiness；
- tail divisibility 失败：algebraic × decimal cross-projection；
- residue class 不进 digit window：pairwise gluing failure；
- arithmetic、root、digit 都分别有 witness，但 exact balance 无共同 witness：真正 global synchronization failure。

因此：

\[
\boxed{
B_{\rm dec}
}
\]

不是单一机制，而是“恢复已经走到 decimal endgame 时出现的 join emptiness”。

---

## 9.4 新的统一判断

所以不再建议写：

\[
\mathfrak B_{\rm back}
=
\{B_{\rm arith},B_{\rm root},B_{\rm dec}\}
\]

作为深层本体 basis。

更自然的是：

\[
\boxed{
\mathfrak B_{\rm glue}
=
\{
\text{join-empty certificates}
\},
}
\]

并按

\[
h_{\mathfrak R}
\]

以及 minimal unsatisfiable support 所跨的 relation types 分类。

**等级：NEW PROVED（框架重分类）。**

---

# 10. Reclassification of B1 / B2 / B3

本轮不证明 B1/B2/B3，只重新分类。

---

## 10.1 B1 — admissible-root capacity

B1 的自然位置是：

\[
\boxed{
\text{root-centered subjoin emptiness}.
}
\]

它可能表现为：

\[
R_{\rm alg}=\varnothing
\]

或

\[
R_{\rm alg}\Join R_{\rm arith}=\varnothing.
\]

所以 B1 不是独立于 gluing 的 obstruction；它是 global join 在 root projection 上已经提前死亡。

---

## 10.2 B2 — global prime-demand matching

B2 的自然位置是：

\[
\boxed{
\text{arithmetic sub-CSP / matching join emptiness}.
}
\]

若未来真的建立 Hall-type criterion，则某个 Hall deficit 就是 arithmetic subjoin 的小型 unsatisfiable certificate。

所以 B2 的本质不是“另一个 obstruction family”，而是：

\[
\boxed{
\text{在 arithmetic hyperedges 内寻找低阶 join-empty certificate}.
}
\]

---

## 10.3 B3 — one-witness decimal synchronization

B3 的自然位置最清楚：

\[
\boxed{
\text{surviving subjoins 之后的 final global join emptiness}.
}
\]

也就是：

\[
R_{\rm alg}\ne\varnothing,
\quad
R_{\rm arith}\ne\varnothing,
\quad
R_{\rm dec}\ne\varnothing,
\]

甚至若干 pairwise joins 都非空，但：

\[
\boxed{
R_{\rm alg}
\Join
R_{\rm arith}
\Join
R_{\rm dec}
\Join
R_{\rm bal}
=
\varnothing.
}
\]

---

## 10.4 统一结论

\[
\boxed{
\text{B1、B2、B3 是同一个 join-empty obstruction 在不同 projection depth 的表现。}
}
\]

更精确地：

- B1：早期 root core 已死；
- B2：arithmetic subjoin 已死；
- B3：局部 subjoins 仍活，但 full synchronization 死亡。

**等级：NEW PROVED（概念重分类，不宣称三者数学条件等价）。**

---

# 11. Reduced interface \(\Sigma_{\rm glue}\)

第一轮

\[
\Xi_{\rm back}
=
(
\Gamma_{\rm arith},
\mathscr Q_{\rm rec},
\mathcal A_{\rm root},
\Theta_{10},
\Pi_{\rm dec}
)
\]

仍然带有“按证明来源分包”的痕迹。

本轮建议把 interface 改为“决定 constraint system 的最小 quotient”。

---

## 11.1 Formal minimal quotient

定义等价关系：

\[
\xi\sim_{\rm glue}\xi'
\]

当且仅当 \(\xi,\xi'\) 诱导的：

1. recovery variable domains；
2. gate scopes；
3. constraint relations；
4. deterministic recovery maps

在变量重命名下同构。

定义

\[
\boxed{
\Sigma_{\rm glue}(\xi)
=
[\xi]_{\sim_{\rm glue}}.
}
\tag{11.1}
\]

那么是否可 glue：

\[
\Join_jR_j\stackrel{?}{\ne}\varnothing
\]

只依赖 \(\Sigma_{\rm glue}\)。

并且按构造，任何还能进一步 quotient、同时保持所有 gluing decisions 的接口都只能合并 relation-isomorphic states。

所以这是一个**形式上的 coarsest gluing interface**。

**等级：NEW PROVED（按定义）。**

---

## 11.2 Concrete implementable interface

实际研究不能直接存一个抽象同构类。

建议使用：

\[
\boxed{
\Sigma_{\rm glue}^{\rm conc}
=
\left(
\mathcal S_\xi,\,
R_{\rm alg},\,
R_{\rm arith},\,
R_{\rm dec},\,
R_{\rm rec}
\right).
}
\tag{11.2}
\]

其中：

### \(\mathcal S_\xi\)

真正共享的 synchronization variables / domains。

只保留能被两个以上 relation 读取，或作为最终 exact recovery 输入的变量。

### \(R_{\rm alg}\)

编译后的：

- recovery polynomial；
- degenerate flag；
- admissible root set；
- sign / positivity / reduced root constraints。

不再把 \(\mathscr Q_{\rm rec}\) 与 \(\mathcal A_{\rm root}\) 分开存。

### \(R_{\rm arith}\)

编译后的：

- gcd；
- reducedness；
- valuation；
- congruence；
- root-denominator；
- prime-allocation feasibility。

其中 \(2/5\)-adic tail capacity 被吸收在这里，不再单列 \(\Theta_{10}\)。

### \(R_{\rm dec}\)

精确 digit intervals / decimal tail / representative conditions。

### \(R_{\rm rec}\)

deterministic block recovery maps 与 exact concatenation residual。

它取代第一轮 \(\Pi_{\rm dec}\) 中“digit cell + coefficient plane + original check”混在一起的表示。

---

## 11.3 可以 quotient 掉什么？

只要已经编译进 relations，以下 metadata 可以删除：

- chamber 名称；
- 某条局部 proof route 的名字；
- Hensel / Gaussian / near-square 标签；
- 某个 certificate 是从哪份 lemma 导出的历史信息；
- root sign 若 relation 已经对 \(\pm\) quotient；
- prime allocation label 若它不改变可实现的 arithmetic relation。

---

## 11.4 不能 quotient 掉什么？

若会改变 join emptiness，则必须保留：

1. recovery polynomial 的真实系数或等价 root locus；
2. degenerate / nondegenerate 状态；
3. exact gcd / reducedness demands；
4. 真正影响 root branch 的 congruence classes；
5. exact digit interval endpoints；
6. exact tail exponent demand；
7. deterministic block recovery map；
8. exact concatenation residual。

特别是不能用：

- 只有数量级的 coefficient plane；
- 只有 prime support、不含 valuation depth 的摘要；
- 只有“存在局部 root”而不记录是哪一个共享 root

代替这些信息。

---

## 11.5 与 \(\Xi_{\rm back}\) 的关系

新 interface 的核心压缩是：

\[
\boxed{
\text{从“按理论来源分组”}
\longrightarrow
\text{“按 shared variables 与 relations 分组”.}
}
\]

因此它更适合直接研究 synchronization，而不是继续制造 arithmetic/root/decimal 三套平行语言。

---

# 12. Global death-region consequences

## 12.1 统一死亡区域

定义：

\[
\boxed{
\mathcal D_{\rm glue}
=
\left\{
\Sigma_{\rm glue}:
\Join_jR_j=\varnothing
\right\}.
}
\tag{12.1}
\]

则任何已证 local obstruction 都只是 \(\mathcal D_{\rm glue}\) 的一个容易识别的子区。

---

## 12.2 新框架为什么可能扩大 death region？

旧框架最容易检测：

\[
R_j=\varnothing.
\]

新框架额外允许检测：

\[
R_i\ne\varnothing,\quad
R_j\ne\varnothing,
\quad
R_i\Join R_j=\varnothing,
\]

甚至：

\[
\forall |J|<k,\quad
\Join_{j\in J}R_j\ne\varnothing,
\]

但

\[
\Join_jR_j=\varnothing.
\]

所以它能扩大 death region，而**不需要任何单个 local obstruction 更强**。

---

## 12.3 Minimal unsatisfiable subsystem ledger

对每个死 state，可以记录一个 minimal set

\[
J_{\min}
\]

满足：

\[
\Join_{j\in J_{\min}}R_j=\varnothing,
\]

但对每个 proper subset \(J'\subsetneq J_{\min}\)：

\[
\Join_{j\in J'}R_j\ne\varnothing.
\]

于是 backward proof 不再只输出：

\[
\text{“root failed”}
\]

而可以输出：

\[
\boxed{
\text{“root-denominator + residue-window + exact-balance 是一个 3-edge MUS”.}
}
\]

这会显著提高未来 proof reuse，因为同一个 MUS schema 可以跨 chamber / branch 复用。

---

## 12.4 对“失败本质”的最终回答

当前最稳妥的答案是：

### PROVED / DERIVED

- local emptiness 确实存在；
- local prime/root compatibility 不足以保证同一 global integer witness；
- final exact recovery 必须同步所有 constraints；
- 当前旧 strict-layer local-position 路线已经表现出局部兼容而全局问题仍开放。

### HEURISTIC

剩余大块 strict-layer frontier 很可能更适合由：

\[
\boxed{
\textbf{synchronization failure}
}
\]

而不是“再加强一个单局部 gate”关闭。

### OPEN

是否存在一个 uniform \(h_0\) 使所有 non-liftable surviving states 都满足：

\[
\boxed{
h_{\mathfrak R}\le h_0
}
\]

尚未证明。

这就是 Global Witness Gluing Theory 下一步最值得攻的核心。

---

# 13. Next theorem targets — at most three

本轮不继续 B1/B2/B3，而把下一步 theorem targets 上提一级。

---

## Target G1 — Bounded Synchronization-Core Theorem

目标证明：

\[
\boxed{
\text{所有 backward recovery gates 在 deterministic elimination 后，}
}
\]

都只依赖一个 cardinality uniformly bounded 的 central synchronization core

\[
S_{\rm core}(\xi).
\]

理想形式：

\[
\boxed{
|S_{\rm core}(\xi)|\le K
}
\]

其中 \(K\) 为绝对常数，最好 \(K=2\) 或 \(4\)。

若成功，则由 finite-core certificate lemma 立即得到：

\[
\boxed{
\text{global failure}
\Longrightarrow
\text{至多 }K\text{ 个 compatibility relations 已经失败}.
}
\]

这是最直接的 “small obstruction certificate” 定理。

**优先级：1。**

---

## Target G2 — Global Congruence Compilation Theorem

固定一个 central algebraic core element 后，把全部局部 prime / valuation / root-denominator data 编译成：

\[
\boxed{
\varnothing
}
\]

或有限个 global congruence classes：

\[
\boxed{
w\equiv c_\alpha\pmod{M_\alpha}.
}
\]

理想状态进一步证明每个 core element 只产生 \(O(1)\) 个 classes。

这样：

- 每个 fixed branch 内可直接使用 generalized CRT 的 2-certificate；
- 多素数 local-root choices 被真正压成 global integer residue classes；
- “\(\forall p\exists w_p\)” 与“\(\exists w\forall p\)”之间的量词缺口被显式解决。

**优先级：2。**

---

## Target G3 — Uniform Gluing-Helly Bound

在 G1/G2 基础上证明一个真正的全局定理：

\[
\boxed{
\Join_jR_j=\varnothing
\Longrightarrow
\exists J,\ |J|\le h_0,\quad
\Join_{j\in J}R_j=\varnothing.
}
\]

最有希望的目标值：

\[
\boxed{
h_0\in\{3,4\}.
}
\]

一种理想的三层证书是：

\[
\boxed{
\text{global residue class}
+
\text{digit window}
+
\text{exact reconstruction residual}.
}
\]

这将把整个 backward non-liftability 搜索从“处理几十个 conditions”变成“寻找 bounded-size MUS”。

**优先级：3。**

---

# 14. Proved / heuristic / open ledger

## PROVED

继承已有证明：

1. T3 canonical common-denominator reconstruction 是原题完整恢复的双向判别。
2. primitive recovery：
   \[
   \gcd(q,y_i)=q/b_i.
   \]
3. Exact-Lift gap quadratic、primitive tail quadratic 及相应 rational-root divisibility。
4. denominator-tail certificate：
   \[
   10^\ell\mid\kappa^2(\kappa+2G).
   \]
5. denominator prime graph 的既有必要结构。
6. `strict_layer_final_campaign.md` N4–N5：现有 local valuation-position data 对允许位置模式仍可相容，不能单独形成全局终止。
7. 旧 proved report 已明确：逐素数 local absorption compatibility 不等于存在同一个具有正确实大小的 global integer square root。

---

## DERIVED FROM PROVED RESULTS

1. 对任意 strict state \(\xi\)，若 Liftable 解释为“存在与 \(\xi\) 相容的原题完整候选”，则：
   \[
   \operatorname{Liftable}(\xi)
   \iff
   \mathcal W_{\rm global}(\xi)\ne\varnothing.
   \]
2. \(t\)、\(d_i\)、\(a_i,b_i\)、digit lengths、valuation profile 在 canonical witness 固定后均为派生数据。
3. gap root、tail root、local \(p\)-adic root branch 是完整 witness 的 projections，而不能被自动当成彼此独立的 global freedoms。
4. tail divisibility 不是独立第四 obstruction species，而是 algebraic / arithmetic / decimal data 的交叉 necessary projection。
5. 当前 surviving backward logical frontier 是 one-witness synchronization，而不是“某个既有 local gate 尚未写得足够强”。

---

## NEW PROVED

1. **Global recovery witness formulation**：
   用 T3 canonical witness 定义 \(\mathcal W_{\rm global}\)。
2. **Natural-join formulation**：
   recovery system 可统一表示为 shared-variable relations 的 natural join；fibre product 是其 separator-special case。
3. **Exact join vs relaxation join distinction**：
   necessary-certificate join 非空不推出 liftable，空则推出 non-liftable。
4. **Obstruction order**：
   \[
   h_{\mathfrak R}
   =
   \min\{|J|:\Join_{j\in J}R_j=\varnothing\}.
   \]
5. **Higher-order failure 的抽象可能性**：
   pairwise compatibility 一般不推出 global compatibility。
6. **Single-variable generalized CRT certificate theorem**：
   fixed single-class congruence subsystem 的 failure 有 2-certificate。
7. **Finite synchronization-core certificate lemma**：
   若 core 大小为 \(K\)，global failure 有至多 \(K\)-constraint certificate。
8. **B1/B2/B3 reclassification**：
   三者是同一 join-empty obstruction 在不同 projection depths / sub-CSPs 上的表现，而非三个逻辑独立本体。
9. **Formal minimal gluing quotient**：
   \[
   \Sigma_{\rm glue}=[\xi]_{\sim_{\rm glue}}
   \]
   是保持 relation system 的形式最粗 quotient。

---

## HEURISTIC

1. 剩余 strict-layer obstruction 很可能主要来自 synchronization，而不是新的单局部 emptiness。
2. algebraic recovery 可能最终把 central core 压到至多 \(2\)–\(4\) 个 states。
3. global incompatibility certificate 的实际尺寸很可能是 \(2\)–\(4\)。
4. “CRT class + digit interval + exact residual” 是最值得尝试的 3-certificate schema。
5. 当前 recovery hypergraph 可能经过 deterministic elimination 变成接近 join-tree 的结构。

---

## OPEN

1. Exact-Lift full recovery hypergraph 是否存在 genuine higher-order \(h\ge3\) synchronization failure。
2. 是否存在 branch-independent bounded synchronization core。
3. 是否能把所有 local prime/root conditions uniform compile 为少数 global congruence classes。
4. 是否存在 uniform Helly-type bound
   \[
   h_{\mathfrak R}\le h_0.
   \]
5. 若存在，最优 \(h_0\) 是 \(2\)、\(3\)、\(4\) 还是更大。
6. 是否所有旧 \(B_{\rm arith},B_{\rm root},B_{\rm dec}\) death certificates 最终都能由少数 canonical MUS schemas 统一生成。

---

# Final conclusion

本轮没有得到新的局部分支无解，但得到了一次更深的 backward 抽象：

\[
\boxed{
\text{Local recovery conditions}
}
\]

不再被视作若干平行“门”，而被统一为：

\[
\boxed{
\textbf{一个 canonical candidate 的多个 projections 必须能 glue 回同一个 witness}.
}
\]

最终结构是：

\[
\boxed{
\xi
\longmapsto
\Sigma_{\rm glue}(\xi)
\longmapsto
\{R_j\}
\longmapsto
\Join_jR_j.
}
\]

严格死亡判据为：

\[
\boxed{
\Join_jR_j=\varnothing
\Longrightarrow
\text{not liftable}.
}
\]

而真正新的顶层问题不是继续制造更强的单局部 obstruction，而是：

\[
\boxed{
\textbf{Global join 为空时，最少需要多少个 compatibility relations 就能见证其为空？}
}
\]

也就是寻找一个 uniform small obstruction certificate / gluing Helly number。

因此本轮建议把 Backward Strict Layer 的下一阶段核心名称正式改为：

\[
\boxed{
\textbf{Global Recovery-Witness Gluing Theory}.
}
\]

