# 三项十进制拼接平方和问题：Backward Strict Layer Canonical Synchronization Quotient

**文件名：** `strict_layer_backward_canonical_synchronization_quotient.md`  
**研究范围：** Backward Strict Layer 宏观结构层的最后收束；只研究 Exact-Lift recovery blocks 之间真正需要共享的 deterministic information，以及由此得到的 canonical synchronization quotient / relation。  
**明确冻结：** moving primitive core、square / deflated quadratic gate、square-spacing、height、\(2/5\)-adic moving-core capacity、resultant / polynomial coupling、DD post-deflation small factor，以及任何 carrier/local branch 的具体攻击。

---

# 1. Executive summary

本轮修正上一轮 `strict_layer_backward_canonical_dependency_skeleton.md` 中两个 presentation-dependent 点，并把 Backward Strict Layer 的宏观抽象收束到一个真正稳定的对象。

第一，

\[
\gcd(x_1,x_2,x_3,\Lambda)=1
\]

不应作为读取四坐标的独立 synchronization gate。它属于 canonical ambient state 的定义。故上一轮由 raw gate support 得到的

\[
\kappa_{\rm rec}\le 4
\]

只能保留为旧 presentation 下的 diagnostic，不能再作为 intrinsic recovery complexity。

第二，separator 不应限制为 canonical coordinates 的子集。任何真正的 shared deterministic information 都允许通过一个函数

\[
\sigma:\Omega_{\rm can}\to\Sigma
\]

传递。因此 “某 gate 读取几个原始坐标” 与 “global recovery 需要共享多少信息” 是两个不同问题。

本轮进一步得到一个更重要的结构修正：

\[
\boxed{
(\Lambda,r_{\rm rec})
\text{ 目前不能作为已证 canonical separator。}
}
\]

原因不是坐标数不漂亮，而是现有 Exact-Lift 中没有一个已经证明的单一 global recovery root。统一 gap quadratic 的实际 root 是 projective ratio

\[
[\mu:\nu],
\]

primitive-tail quadratic 的实际 root 是

\[
z_3=\frac{a_3}{\delta_3},
\]

二者来自不同消元方向。一个完整 canonical candidate 固定后，它们都是 deterministic projections；但当前没有 theorem 把二者识别成同一个 root，也没有 theorem 证明 decimal recovery 只读取其中一个统一 root。

因此，本轮不再追求“找两个变量做 separator”，而改用 **semantic recovery blocks + maximal common factor + lossless join**。

设经过 proof-artifact elimination 后的数学 recovery blocks 为

\[
\mathcal R_{\rm alg},\qquad
\mathcal R_{\rm den},\qquad
\mathcal R_{10},
\]

分别表示：

1. algebraic/root recovery；
2. reduced denominator / arithmetic recovery；
3. decimal realization / exact reconstruction。

对每个 block 取 presentation-independent semantic map

\[
\lambda_j:\Omega_{\rm rec}\to L_j,
\]

其中 \(L_j\) 只记录该 block 数学上能区分的 local recovery state，Hensel label、Gaussian route、enumeration index、任意变量命名等全部 quotient 掉。

令

\[
J_{\rm rec}
=
\operatorname{Im}
(\lambda_{\rm alg},\lambda_{\rm den},\lambda_{10})
\subseteq
L_{\rm alg}\times L_{\rm den}\times L_{10}.
\]

这是真正的 **canonical joint recovery image**。

本轮得到以下抽象定理。

## CSQ-0 — Maximal deterministic common-factor theorem — **NEW PROVED**

令

\[
E_j=\ker(\lambda_j),
\]

并令 \(E_{\rm com}\) 为包含全部 \(E_j\) 的最小等价关系：

\[
E_{\rm com}
=
\operatorname{EqCl}
\left(
E_{\rm alg}\cup E_{\rm den}\cup E_{10}
\right).
\]

定义

\[
\boxed{
\Sigma_{\rm com}
:=
\Omega_{\rm rec}/E_{\rm com},
\qquad
\sigma_{\rm com}:\Omega_{\rm rec}\to\Sigma_{\rm com}.
}
\]

则：

1. \(\sigma_{\rm com}\) factor through 每一个 recovery block；
2. 若某 deterministic map \(\tau\) 也能由每个 block 单独恢复，即
   \[
   \tau=\tau_j\circ\lambda_j
   \quad\forall j,
   \]
   则 \(\tau\) 必进一步 factor through \(\sigma_{\rm com}\)。

因此 \(\Sigma_{\rm com}\) 是全部 blocks 能共同确定的 **最大 deterministic common information**，并且在 block semantic equivalence 固定后 presentation-invariant。

但这还不等于 sufficient synchronization quotient。

永远只有

\[
\boxed{
J_{\rm rec}
\subseteq
L_{\rm alg}
\times_{\Sigma_{\rm com}}
L_{\rm den}
\times_{\Sigma_{\rm com}}
L_{10}.
}
\tag{CSQ-1}
\]

要得到真正的单一 quotient gluing，必须证明 **lossless join / rectangularity**：

\[
\boxed{
J_{\rm rec}
=
L_{\rm alg}
\times_{\Sigma_{\rm com}}
L_{\rm den}
\times_{\Sigma_{\rm com}}
L_{10}.
}
\tag{RECT}
\]

并且有一个关键的否定性结论：

> 若 (RECT) 对 \(\Sigma_{\rm com}\) 失败，则任何更粗的、仍要求“所有 blocks 只比较同一个 quotient value”的 deterministic common quotient 都不可能恢复 exact gluing。

因为所有更粗 quotient 都会允许更多 cross-fibre combinations，而不能删除已经在 \(\Sigma_{\rm com}\)-fibre 中出现的 spurious combinations。

所以本轮真正得到的 canonical verdict 是：

\[
\boxed{
\text{单一 synchronization quotient 是否存在，}
\text{已经被严格化成一个 lossless-join theorem。}
}
\]

当前 proof library 尚未证明 (RECT)。因此本报告 **不宣称** 已经得到一个 proper、low-information、显式坐标的 sufficient quotient。

然而，presentation-invariant 的 synchronization object 已经存在：

\[
\boxed{
\mathfrak S_{\rm can}
=
\left(
J_{\rm rec},
\Sigma_{\rm alg,den},
\Sigma_{\rm den,10},
\Sigma_{\rm alg,10}
\right),
}
\]

其中三个 \(\Sigma_{ij}\) 是相应两个 semantic blocks 的 maximal common factors。等价地，可以使用 pairwise-overlap 的 Čech/join diagram。它自动删除 local-only information，又不会假装所有 pairwise overlap 都能压成一个单一 root 或 denominator coordinate。

**最终结论：**

\[
\boxed{
\textbf{Backward Strict Layer 的宏观抽象阶段可以结束。}
}
\]

剩余工作已经不是“继续找更好看的抽象”，而是第一个具体 theorem：证明上述 canonical overlap diagram 是否 lossless，或精确找出唯一剩余的 non-rectangular coupling。

---

# 2. Anti-duplication boundary

本轮使用的 backward / Exact-Lift 材料仅用于 recovery semantics：

- `strict_layer_backward_canonical_dependency_skeleton.md`；
- `strict_layer_backward_global_witness_gluing_campaign.md`；
- `strict_layer_backward_global_obstruction_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`；
- `strict_layer_final_campaign.md`。

正向 strict-layer 最新材料只用于责任划界。当前正向线继续研究：

- moving primitive core；
- uniform termination；
- square / deflated square gate；
- square-spacing；
- height；
- actual-lift \(2/5\)-adic capacity；
- polynomial/resultant coupling；
- DD 中的 post-deflation small factor \(J=M-Y\)。

这些内容不进入本报告的新 theorem。

本报告也不进入 DD / \(A_1\) 或旧临界 \(A_2\) 的任意局部 geometry。

本轮只问：

\[
\boxed{
\text{如果若干 recovery blocks 都局部存活，}
\text{它们究竟通过什么 deterministic information 才能属于同一个 witness？}
}
\]

---

# 3. Canonical ambient state

定义

\[
\boxed{
\Omega_{\rm can}
=
\left\{
(x_1,x_2,x_3,\Lambda)\in\mathbf Z_{>0}^4:
\gcd(x_1,x_2,x_3,\Lambda)=1
\right\}.
}
\]

canonical minimality 已经吸收到 ambient space。

因此不再有独立的

\[
G_{\rm can}
\]

gate。

对

\[
v=(x_1,x_2,x_3,\Lambda)\in\Omega_{\rm can}
\]

定义

\[
d_i(v)=\gcd(x_i,\Lambda),
\]

\[
a_i(v)=\frac{x_i}{d_i(v)},
\qquad
b_i(v)=\frac{\Lambda}{d_i(v)}.
\]

这些全部 deterministic。

sphere condition 仍是一个真正数学条件：

\[
x_1^2+x_2^2+x_3^2\in\square_{>0}.
\]

若成立，正根

\[
t(v)=\sqrt{x_1^2+x_2^2+x_3^2}
\]

唯一。

为了只研究 synchronization frontier，可以先剔除 sphere-local emptiness，定义

\[
\boxed{
\Omega_{\rm rec}
=
\left\{
v\in\Omega_{\rm can}:
 x_1^2+x_2^2+x_3^2\in\square_{>0}
\right\}.
}
\]

这是一个 **local prefilter**，不是新的 synchronization assumption。

若 sphere 失败，则 state 已由 local obstruction 排除，不属于本轮“多个 blocks 如何 glue”的剩余问题。

由 T3，完整候选在 \(\Omega_{\rm rec}\) 中进一步要求 exact balance：

\[
\boxed{
\Lambda A(v)=t(v)B(v),
}
\]

其中

\[
A(v)=\operatorname{concat}(a_1,a_2,a_3),
\qquad
B(v)=\operatorname{concat}(b_1,b_2,b_3).
\]

---

# 4. Removal of normalization gates and old width

上一轮定义 raw synchronization width 的主要问题是：

\[
\operatorname{EssSupp}(G)
\]

仍依赖 gate 如何 presentation。

例如 canonical normalization 若写成 predicate，就读取四个坐标；若吸收到 ambient space，则 support 为零。

同样，若把某个 derived quantity

\[
s=f(x_1,x_2,x_3,\Lambda)
\]

显式加入变量表，某些 gate 看起来只读取 \(s\)；若把 \(s\) 展开，则又读取多个 canonical coordinates。

所以：

\[
\boxed{
\text{hyperedge cardinality / coordinate support}
\text{ 不是 presentation-invariant synchronization complexity。}
}
\]

上一轮的

\[
\kappa_{\rm rec}\le4
\]

应降级为：

> 当前 T3 原始坐标 presentation 中，某些 predicates 形式上读取四坐标。

不能再从这里推出任何 intrinsic “width = 4/3/2”。

同理，旧

\[
h_{\mathfrak R}
\]

relation-count obstruction order 已经因为 merge/split granularity 而失去 intrinsic 含义。

本轮完全停止以 “relation 数量” 或 “原始坐标 support 数量” 作为主复杂度。

---

# 5. Recovery block decomposition

本轮不按报告章节、证明方法、Hensel/Gaussian route 切块，而按 **完整恢复中的数学角色** 切成三类。

## 5.1 Algebraic/root recovery block \(\mathcal R_{\rm alg}\)

该 block 负责：

- Exact-Lift gap quadratic；
- primitive-tail quadratic；
- 非退化 quadratic 的 rational-root / discriminant-square existence；
- root positivity/sign/reduced form 中真正属于 algebraic admissibility 的部分。

典型统一 gap quadratic 为

\[
D(\kappa+2G)\mu^2
-2G\kappa C\mu\nu
+\kappa D\mathcal N_{12}\nu^2
=0,
\qquad
\gcd(\mu,\nu)=1.
\]

primitive-tail quadratic 为

\[
-\kappa(\kappa+2G)z_3^2
+2G^2LCz_3
+\mathcal C_3
=0,
\qquad
z_3=\frac{a_3}{\delta_3}.
\]

这里有两个不同 typed roots：

\[
\boxed{
[\mu:\nu]
\quad\text{与}\quad
z_3.
}
\]

一个完整 canonical candidate 若存在，它们都是该 candidate 的 deterministic projections。

理论 quadratic 有两个 roots，只表示 projected search branching，不表示 complete witness 多了两个独立自由变量。

---

## 5.2 Denominator/arithmetic recovery block \(\mathcal R_{\rm den}\)

canonical gcd normalization 已移入 ambient。

本 block 保留真正 arithmetic recovery：

- reduced numerator/denominator；
- primitive recovery gcd；
- root numerator/denominator divisibility；
- denominator prime graph；
- prime-power demand/supply；
- tail denominator split；
- 必要的 valuation / reducedness conditions。

典型 rational-root consequences：

\[
\nu\mid D(\kappa+2G),
\qquad
\mu\mid\kappa D\mathcal N_{12},
\]

\[
\delta_3\mid\kappa(\kappa+2G),
\qquad
a_3\mid\mathcal C_3.
\]

以及 denominator-tail certificate

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G).
}
\]

该 certificate 本身已经表明：arithmetic 与 decimal tail 并非两套独立世界。

---

## 5.3 Decimal realization block \(\mathcal R_{10}\)

该 block 负责：

- actual digit lengths；
- tail length / decimal split；
- residue class 的真实整数代表；
- digit interval/window；
- 无前导零等 block realization；
- exact coefficient-plane residual；
- T3 terminal exact balance
  \[
  \Lambda A=tB.
  \]

重要的是：

\[
A,B,n_i,m_i
\]

在 complete canonical state 固定后全部 deterministic。

因此“选择一个 digit representative”只存在于 compressed/local search fibre；它不是新的 global candidate coordinate。

---

## 5.4 为什么不把 sphere 当第四 synchronization block？

sphere failure 是 genuine local emptiness。

本轮研究的是 surviving states 上的 global synchronization，因此先限制到 \(\Omega_{\rm rec}\) 后，\(t\) 已唯一恢复。

把 sphere 继续作为一个并行 gluing block 会人为要求所有其他 blocks 都只能通过 sphere 能看见的信息共享，从而把 denominator/decimal 之间真实存在的 pairwise overlap 错误抹掉。

所以 sphere 在本轮作为 local exact precondition，而不是 synchronization node。

---

# 6. Local-only vs shared recovery information

下表给出本轮的 semantic classification。它不是 raw variable inventory，而是“是否需要跨 recovery blocks 一致”的分类。

| 信息 | 分类 | 当前严格判断 |
|---|---|---|
| Hensel branch label | proof/search-only | complete candidate 固定后只是 projected branch/certificate |
| Gaussian route / associate label | proof/search-only | 除非证明对应不同 completion fibre，否则不得作为 global state |
| enumeration index | proof-only | 删除 |
| discriminant root 的纯 \(\pm\) sign | 通常 local/proof-only | 若后续 oriented recovery 真读取 sign 才保留 typed local branch |
| \([\mu:\nu]\) | shared deterministic projection | algebraic block产生；denominator divisibility读取；某些 decimal representative constraints 可能读取其投影 |
| \(z_3=a_3/\delta_3\) | shared deterministic projection | algebraic tail root；其 reduced denominator 与 decimal tail split 直接相连 |
| \(\delta_3\) | shared deterministic | root denominator + denominator arithmetic + decimal tail |
| \(\ell\) | shared deterministic | decimal tail demand，并进入 denominator-tail certificate |
| \(L\mid\kappa\) 中的 tail quotient \(L\) | shared deterministic | arithmetic/tail bridge；不是新的自由变量 |
| \(\mu,\nu\) 的 divisibility data | shared deterministic | root ↔ arithmetic |
| denominator valuation profile | shared deterministic where reused | arithmetic ↔ decimal/tail；但不能把全部 local prime labels都升级为 shared state |
| \(a_i,b_i\) | shared deterministic | arithmetic reducedness 与 exact decimal reconstruction 都读取；当前不能证明可全部 quotient 掉 |
| \(\Lambda\) | ambient canonical datum | 不是 normalization gate；是否必须进入最小 synchronization interface **OPEN** |
| exact concatenation residual | decimal block output / global acceptance predicate | 不作为新的 free coordinate |

最重要的三点：

### 6.1 当前没有 intrinsic shared branching coordinate — **DERIVED FROM PROVED RESULTS**

complete canonical state 固定后，actual gap root、actual tail root、digit representative 等均由 candidate 决定。

所以：

\[
\boxed{
\text{global synchronization 的难点不是多个独立 branch variables，}
}
\]

而是：

\[
\boxed{
\text{不同 compressed blocks 必须重新指向同一个 canonical completion。}
}
\]

### 6.2 full \(\Lambda\) 不是自动的 shared separator

\(\Lambda\) 会通过

\[
\gcd(x_i,\Lambda)\to b_i
\]

影响多个 blocks。

但 “影响多个 blocks” 只说明它是 source datum，不说明 global synchronization 必须显式传递完整 \(\Lambda\)。

某些接口只需要 \(\delta_3\)、root denominator、valuation trace、tail quotient 等更粗投影。

因此：

\[
\boxed{
\Lambda\text{ 是否属于 minimal shared information 是 OPEN，}
}
\]

不能因为它是 canonical coordinate 就预设“必须共享”。

### 6.3 但 exact decimal reconstruction 当前仍阻止我们随意删掉全部 denominator/block data

T3 terminal balance

\[
\Lambda A=tB
\]

读取真实 recovered blocks。

因此，若要证明一个显式 quotient 可以忘掉大部分 \(a_i,b_i,\Lambda\) 而仍 losslessly glue，必须有新的 factorization theorem。

当前 proof library 没有这条 theorem。

---

# 7. Synchronization equivalence relation

## 7.1 Semantic block maps

对每个 recovery block，不选某份报告中的 raw variable list，而取其 **semantic local state**。

形式上，令

\[
\lambda_j:\Omega_{\rm rec}\to L_j,
\qquad
j\in\{\mathrm{alg},\mathrm{den},10\},
\]

满足：

- 两个 canonical states 若只在变量命名、proof route、Hensel/Gaussian label、enumeration artifact 上不同，但对该 block 的全部数学 completion/certificate 行为相同，则它们在 \(L_j\) 中相同；
- 若该 block 的某个真正 mathematical output / admissibility behaviour 不同，则它们在 \(L_j\) 中不同。

因此 \(L_j\) 是 semantic quotient，不是 report-schema。

记

\[
E_j=\ker\lambda_j.
\]

---

## 7.2 Maximal deterministic common factor

定义

\[
\boxed{
E_{\rm com}
=
\operatorname{EqCl}
(E_{\rm alg}\cup E_{\rm den}\cup E_{10}).
}
\]

等价地，

\[
v\sim_{\rm com}v'
\]

当且仅当存在链

\[
v=v_0,v_1,\ldots,v_k=v'
\]

使每一步 \(v_{r-1},v_r\) 对至少一个 recovery block 完全不可区分。

取 quotient：

\[
\boxed{
\Sigma_{\rm com}=\Omega_{\rm rec}/\!\sim_{\rm com}.
}
\]

这不是“把四个整数编码成一个整数”。

它由 block kernels 决定，因此对 block 内部任意双射重参数化 invariant。

---

## 7.3 CSQ-0 proof

因为

\[
E_j\subseteq E_{\rm com},
\]

\(\sigma_{\rm com}\) 在每个 \(\lambda_j\)-fibre 上常值。

所以存在唯一

\[
\rho_j:L_j\to\Sigma_{\rm com}
\]

使

\[
\boxed{
\sigma_{\rm com}=\rho_j\circ\lambda_j.
}
\]

反过来，若

\[
\tau:\Omega_{\rm rec}\to T
\]

对每个 block 都可恢复，即

\[
\tau=\tau_j\circ\lambda_j,
\]

则

\[
E_j\subseteq\ker\tau
\quad\forall j.
\]

因此

\[
E_{\rm com}\subseteq\ker\tau.
\]

于是存在唯一

\[
h:\Sigma_{\rm com}\to T
\]

使

\[
\boxed{
\tau=h\circ\sigma_{\rm com}.
}
\]

证毕。

### 解释

\(\Sigma_{\rm com}\) 是“所有 blocks 都能单独知道的 deterministic information”的 canonical maximal factor。

它完全取代“大家共同读取几个原始坐标”的旧问题。

---

# 8. Candidate quotient \(\Sigma_{\rm sync}\)

## 8.1 为什么 \(\Sigma_{\rm com}\) 还不能直接命名为 sufficient synchronization quotient

定义 joint image

\[
\boxed{
J_{\rm rec}
=
\left\{
(\lambda_{\rm alg}(v),\lambda_{\rm den}(v),\lambda_{10}(v)):
 v\in\Omega_{\rm rec}
\right\}.
}
\]

因为同一个 \(v\) 在三个 blocks 上给出的 common-factor value 必相同，所以必有

\[
J_{\rm rec}
\subseteq
L_{\rm alg}
\times_{\Sigma_{\rm com}}
L_{\rm den}
\times_{\Sigma_{\rm com}}
L_{10}.
\]

但反包含意味着：

> 任取三个 local block states，只要它们拥有相同 common-factor value，就一定来自某个同一 canonical state。

这正是一个强的 **rectangularity / lossless join theorem**。

当前材料没有证明它。

所以：

\[
\boxed{
\Sigma_{\rm com}
\text{ 是 canonical common quotient，}
\text{但尚未证明是 sufficient synchronization quotient。}
}
\]

---

## 8.2 Lossless-join criterion — **NEW PROVED**

以下两条等价：

1. 不同 recovery blocks 的 global compatibility 只需比较 \(s\in\Sigma_{\rm com}\)；
2. joint image 满足
   \[
   \boxed{
   J_{\rm rec}
   =
   L_{\rm alg}
   \times_{\Sigma_{\rm com}}
   L_{\rm den}
   \times_{\Sigma_{\rm com}}
   L_{10}.
   }
   \]

若成立，则可严格写成

\[
\boxed{
\mathcal W_{\rm global}
\simeq
\mathcal W_{\rm alg}
\times_{\Sigma_{\rm com}}
\mathcal W_{\rm den}
\times_{\Sigma_{\rm com}}
\mathcal W_{10},
}
\]

在相应 exact/relaxation语义下。

若不成立，则说明存在 genuine residual synchronization：

\[
\boxed{
\text{same common quotient}
\not\Rightarrow
\text{same global completion fibre}.
}
\]

---

## 8.3 为什么“再 quotient 得更粗”不能修复 rectangularity — **NEW PROVED**

设 \(\tau\) 是另一个所有 blocks 都可计算的 common quotient。

由 CSQ-0，必有

\[
\tau=h\circ\sigma_{\rm com}.
\]

因此 \(\tau\) 的 fibre 至少和 \(\sigma_{\rm com}\) 一样大。

所以

\[
L_{\rm alg}
\times_{\tau}
L_{\rm den}
\times_{\tau}
L_{10}
\]

包含

\[
L_{\rm alg}
\times_{\Sigma_{\rm com}}
L_{\rm den}
\times_{\Sigma_{\rm com}}
L_{10}.
\]

若后者已经严格大于 \(J_{\rm rec}\)，更粗 quotient 只会产生更多 spurious combinations。

故：

\[
\boxed{
\text{若 maximal common factor 不 lossless，}
\text{则不存在更粗的 single-key sufficient quotient。}
}
\]

这是一条非常重要的停止规则：

> 以后不能在 lossless-join 失败时继续通过“再删一个变量”寻找更漂亮的 separator；正确动作应是承认存在 multi-interface / higher-order synchronization relation。

---

## 8.4 Canonical structured synchronization quotient

单一 common key 尚未证明 sufficient，但 pairwise shared information 仍可 canonicalize。

对每对 blocks \(i,j\)，定义其 maximal common factor：

\[
\Sigma_{ij}
=
\Omega_{\rm rec}/
\operatorname{EqCl}(E_i\cup E_j).
\]

特别：

\[
\Sigma_{\rm alg,den},
\qquad
\Sigma_{\rm den,10},
\qquad
\Sigma_{\rm alg,10}.
\]

定义 deterministic map

\[
\boxed{
\sigma_{\rm Cech}(v)
=
\bigl(
\sigma_{\rm alg,den}(v),
\sigma_{\rm den,10}(v),
\sigma_{\rm alg,10}(v)
\bigr).
}
\]

令

\[
\boxed{
\Sigma_{\rm sync}^{\rm can}
:=
\operatorname{Im}(\sigma_{\rm Cech}).
}
\]

这里 \(\Sigma_{\rm sync}^{\rm can}\) 应理解为带三种 typed overlap projections 的 structured quotient，而不是一个可任意 scalar-encode 的“单整数状态”。

它具有两个优点：

1. 任意只属于单个 block 的 local-only information 自动不进入任何 pairwise common factor；
2. root–denominator、denominator–decimal、root–decimal 可以保留不同的真实接口，不需要伪造一个所有 blocks 都共享的单一 root。

### 当前等级

\[
\boxed{
\Sigma_{\rm sync}^{\rm can}
\text{ 作为 canonical structured synchronization object：NEW PROVED。}
}
\]

但：

\[
\boxed{
\text{它是否能进一步 collapse 为单一 sufficient quotient：OPEN。}
}
\]

---

# 9. Factorization of recovery blocks

本节区分 **semantic factorization** 与 **explicit arithmetic factorization**。

## 9.1 Semantic factorization — **NEW PROVED**

由 pairwise maximal common-factor construction，可将每个 block 的 semantic state 写成：

\[
\lambda_{\rm alg}(v)
=
F_{\rm alg}
\bigl(
\sigma_{\rm alg,den}(v),
\sigma_{\rm alg,10}(v),
\lambda_{\rm alg}^{\rm loc}(v)
\bigr),
\]

\[
\lambda_{\rm den}(v)
=
F_{\rm den}
\bigl(
\sigma_{\rm alg,den}(v),
\sigma_{\rm den,10}(v),
\lambda_{\rm den}^{\rm loc}(v)
\bigr),
\]

\[
\lambda_{10}(v)
=
F_{10}
\bigl(
\sigma_{\rm alg,10}(v),
\sigma_{\rm den,10}(v),
\lambda_{10}^{\rm loc}(v)
\bigr).
\]

这里 local variables 只属于一个 block。

所以：

\[
\boxed{
\text{不同 blocks 之间的 deterministic overlap
可以 canonical 地限制在 pairwise common factors。}
}
\]

这不等于已经找到了这些 factors 的短坐标公式。

---

## 9.2 Explicit root ↔ denominator interface — **PARTIALLY DERIVED**

已证公式明确表明：

- \([\mu:\nu]\) 的 reduced denominator/numerator 进入
  \[
  \nu\mid D(\kappa+2G),
  \qquad
  \mu\mid\kappa D\mathcal N_{12};
  \]
- \(z_3=a_3/\delta_3\) 的 reduced denominator/numerator 进入
  \[
  \delta_3\mid\kappa(\kappa+2G),
  \qquad
  a_3\mid\mathcal C_3.
  \]

因此 actual reduced root traces 确实属于

\[
\Sigma_{\rm alg,den}.
\]

但是否只靠 roots 就足够，不成立于当前证明：divisibility 还读取 recovery polynomial coefficients \(C,D,G,\kappa,\mathcal N_{12}\) 等。

所以

\[
\boxed{
\Sigma_{\rm alg,den}
\cong
\text{“root only”}
}
\]

当前是 **OPEN / unsupported**。

---

## 9.3 Explicit denominator ↔ decimal interface — **PARTIALLY DERIVED**

已证 tail normalization：

\[
10^\ell=\delta_3L,
\qquad
b_3=\delta_3\tau,
\]

以及

\[
L\mid\kappa
\]

把 denominator arithmetic 与 decimal tail 直接连接起来。

所以至少

\[
(\ell,\delta_3,L,\tau)
\]

的相关 semantic trace 属于

\[
\Sigma_{\rm den,10}.
\]

此外 exact decimal reconstruction 同时读取真实 \(a_i,b_i\)。

当前没有 theorem 证明这些完整 reduced block data 可以全部压成仅 valuation/gcd/residue summary。

所以：

\[
\boxed{
\text{“只需一个小 denominator summary”仍是 OPEN。}
}
\]

---

## 9.4 Explicit algebraic ↔ decimal interface — **PARTIALLY DERIVED**

现有 backward obstruction 已明确：

- local congruence/Hensel roots 必须由同一个 global representative 实现；
- representative 必须落入真实 digit interval；
- recovered root 还必须满足 exact coefficient plane / concatenation residual。

因此 root actual representative 的某些 projections 属于

\[
\Sigma_{\rm alg,10}.
\]

但 decimal block 并不已证读取“完整 gap root + 完整 tail root”的全部 algebraic data。

所以这里也只能保留 semantic quotient，不能虚构显式最小坐标。

---

# 10. Sufficiency / coarseness audit

## 10.1 Soundness

对 canonical structured quotient \(\Sigma_{\rm sync}^{\rm can}\)：

若

\[
\sigma_{\rm Cech}(v)=\sigma_{\rm Cech}(v'),
\]

则 \(v,v'\) 在每一对 recovery blocks 的全部 maximal deterministic common information 上相同。

这是 construction 本身保证的。

因此它不会把某个只因变量命名不同而不同的 state 错认为不同 synchronization state。

**状态：NEW PROVED。**

---

## 10.2 Sufficiency

若“sufficiency”要求：固定 synchronization state 后，各 blocks 的 local fibres 可以独立选择并自动 glue，当前 **未证明**。

精确缺口就是 rectangularity / lossless join：

\[
J_{\rm rec}
\stackrel{?}{=}
L_{\rm alg}
\Join_{\Sigma_{ij}}
L_{\rm den}
\Join_{\Sigma_{ij}}
L_{10}.
\]

**状态：OPEN。**

---

## 10.3 Minimality / maximal coarseness

必须分两层。

### 单一 common-key 模型

若 (RECT) 成立，则 \(\Sigma_{\rm com}\) 是 canonical sufficient common quotient；任何进一步真正 coarsening 都会把两个 nonempty common-factor fibres 合并，并引入 cross combinations，因此不再 lossless。

所以在该模型下，它具有 canonical minimal-shared-information 意义。

### 若 (RECT) 不成立

则不存在任何更粗 single-key quotient 能修复问题。

此时“最小 quotient”问题本身设错了；正确对象是 multi-interface synchronization relation。

---

## 10.4 Properness

当前不能证明

\[
\Sigma_{\rm sync}^{\rm can}
\]

严格比 \(\Omega_{\rm rec}\) 粗多少。

尤其不能写：

\[
\dim \Sigma_{\rm sync}=2,
\]

也不能写：

\[
\Sigma_{\rm sync}\cong(\Lambda,r).
\]

**状态：OPEN。**

---

# 11. Root–denominator–decimal synchronization audit

本节逐条回答本轮指定的六个问题。

## 11.1 recovery root 是否真的是 global shared witness？

### 结论

\[
\boxed{
\text{当前不存在已经证明的单一 “the recovery root”。}
}
\]

Exact-Lift 至少有两个 typed root projections：

\[
[\mu:\nu]
\]

与

\[
z_3=a_3/\delta_3.
\]

它们分别来自 gap elimination 与 primitive-tail elimination。

不能因为两者都是 quadratic root 就把它们识别。

**状态：DERIVED FROM PROVED RESULTS。**

---

## 11.2 root 一旦 canonical state 固定，是否只是 deterministic projection？

是。

完整 candidate 若产生实际 gap ratio、actual tail ratio，则它们由 candidate 唯一决定。

quadratic 的“两个 theoretical roots”是 projected search branching。

所以：

\[
\boxed{
\text{root 不是新的 complete-witness freedom。}
}
\]

**状态：DERIVED FROM PROVED RESULTS。**

---

## 11.3 denominator information 需要完整 \(\Lambda\) 吗？

### 当前严格答案

\[
\boxed{
\text{没有证明需要完整 }\Lambda，
\text{也没有证明可以完全删除 }\Lambda。
}
\]

对于 tail/root certificate，真实共享信息明显可以比完整 \(\Lambda\) 更粗，例如：

\[
\delta_3,\quad \ell,\quad L,\quad
v_p(\kappa),\quad
v_p(\kappa+2G),\ldots
\]

但 exact T3 decimal reconstruction 又读取完整 recovered denominators \(b_i\)，而这些与 canonical \(\Lambda\) 之间存在严格恢复关系。

因此需要一个新的 lossless factorization theorem 才能决定最小 denominator trace。

**状态：OPEN。**

---

## 11.4 decimal realization 读取完整 root 吗？

当前不能这样说。

已证的是 decimal synchronization 会读取：

- actual representative / residue；
- root denominator 与 tail split；
- sign/interval class 中真正影响 digit window 的部分；
- exact coefficient-plane residual。

这一般是 root 的某些 projections，而不是已证的“完整统一 root”。

**状态：DERIVED + OPEN for minimal trace。**

---

## 11.5 arithmetic recovery 与 decimal recovery 共享完整整数 witness，还是较小投影？

必须区分层级。

### Exact T3 terminal level

两者最终必须属于同一个 recovered block tuple：

\[
(a_1,b_1,a_2,b_2,a_3,b_3).
\]

这个 tuple 与 canonical state 等价到 deterministic recovery。

所以 exact terminal compatibility 不能在没有新 theorem 的情况下随意忘掉这些数据。

### Necessary-certificate level

大量 obstruction 只需要更小投影：

- root reduced denominator；
- valuation profile；
- tail split；
- residue / interval；
- coefficient-plane trace。

因此 backward certificate synchronization 的实际 quotient 很可能严格小于 full candidate state，但 **properness 尚未证明**。

---

## 11.6 是否存在比 \((\Lambda,r_{\rm rec})\) 更粗的 synchronization statistic？

严格地说，问题需要先修正：当前没有 canonical single \(r_{\rm rec}\)。

因此 \((\Lambda,r_{\rm rec})\) 不是一个已定义好的 baseline quotient。

本轮给出的真正 replacement 是：

\[
\boxed{
\Sigma_{\rm sync}^{\rm can}
=
\text{typed maximal pairwise common-factor diagram}.
}
\]

它在语义上自动删除：

- local-only data；
- proof-only data；
- block 内 deterministic redundancy。

但是否能进一步写成一个漂亮短坐标 tuple，仍 **OPEN**。

---

# 12. Quotient-based obstruction formulation

过去的 arithmetic / root / decimal obstruction 可以统一写成 synchronization-image emptiness，但必须保留“one-way necessary”纪律。

设每个 block 在某 strict partial state \(\xi\) 下的 admissible local subset 为

\[
F_{\rm alg}(\xi)\subseteq L_{\rm alg},
\]

\[
F_{\rm den}(\xi)\subseteq L_{\rm den},
\]

\[
F_{10}(\xi)\subseteq L_{10}.
\]

真正 global compatible local tuple 必须属于

\[
\boxed{
J_{\rm rec}
\cap
\left(
F_{\rm alg}(\xi)
\times
F_{\rm den}(\xi)
\times
F_{10}(\xi)
\right).
}
\tag{12.1}
\]

因此：

\[
\boxed{
J_{\rm rec}
\cap
\prod_jF_j(\xi)
=\varnothing
\Longrightarrow
\text{not liftable}.
}
\tag{12.2}
\]

这是最稳定的 quotient/join-based obstruction statement。

---

## 12.1 Common-factor image separation

令

\[
S_j(\xi)=\rho_j(F_j(\xi))\subseteq\Sigma_{\rm com}.
\]

则必有：

\[
\boxed{
S_{\rm alg}(\xi)
\cap
S_{\rm den}(\xi)
\cap
S_{10}(\xi)
=\varnothing
\Longrightarrow
\text{not liftable}.
}
\tag{12.3}
\]

这是严格充分 obstruction。

但反向不成立于当前材料：

\[
S_{\rm alg}\cap S_{\rm den}\cap S_{10}\neq\varnothing
\]

仍可能因为 \(J_{\rm rec}\) 在某 common-factor fibre 内 non-rectangular 而无法 glue。

所以：

\[
\boxed{
\text{quotient-image intersection nonempty}
\not\Rightarrow
\text{global witness exists}.
}
\]

这正是 one-witness synchronization 的剩余逻辑缺口。

---

## 12.2 Pairwise overlap obstruction

若在某 pairwise common factor 上已有

\[
\pi_{ij}(F_i)
\cap
\pi_{ij}(F_j)
=
\varnothing,
\]

则立即 non-liftable。

这重新解释旧的：

- root-denominator mismatch；
- root-window mismatch；
- denominator-tail mismatch；
- prime matching failure；
- unique residue 不进入 digit interval。

它们不是“有几个 relation 冲突”，而是：

\[
\boxed{
\text{某 canonical overlap quotient 上两个 feasible images 不相交。}
}
\]

---

## 12.3 Higher-order residual obstruction

即使所有 pairwise overlap images 非空，也可能有

\[
J_{\rm rec}
\cap
\prod_jF_j
=
\varnothing.
\]

这才是 presentation-invariant 的 higher-order synchronization failure。

因此以后若要讨论 “pairwise compatibility 仍不够”，应直接以

\[
J_{\rm rec}
\]

的 non-rectangularity / empty restricted fibre 为对象，而不是恢复旧 \(h_{\mathfrak R}\) relation count。

---

# 13. Replacement of old width / certificate notions

本轮不再定义一个未经证明的数值

\[
\kappa_{\rm sync}=2,3,4.
\]

建议把 Backward complexity 改成一个 **refinement hierarchy / synchronization type**：

\[
\boxed{
\Omega_{\rm rec}
\longrightarrow
(L_{\rm alg},L_{\rm den},L_{10})
\longrightarrow
\Sigma_{ij}
\longrightarrow
J_{\rm rec}.
}
\]

真正需要记录的是：

1. block semantic quotients；
2. pairwise maximal common factors；
3. joint image 是否 lossless rectangular；
4. 若不 rectangular，residual fibre relation 的结构。

可以把这一整体记为

\[
\boxed{
\mathfrak K_{\rm sync}
:=
\left(
\{L_j\},
\{\Sigma_{ij}\},
J_{\rm rec}
\right).
}
\]

它不是一个数字，但比 raw width 更 intrinsic。

若未来证明 single-key rectangularity，则 hierarchy 可以收缩为：

\[
\Omega_{\rm rec}
\to
\Sigma_{\rm sync}
\to
\{\text{independent local fibres}\}.
\]

到那时再讨论 \(\Sigma_{\rm sync}\) 的 arithmetic complexity 才有意义。

---

## 13.1 不要混淆 quotient complexity 与 fibre cardinality

即使未来得到一个很短的显式 tuple，例如

\[
\Sigma_{\rm sync}\cong(s_1,s_2),
\]

也不能推出：

\[
|\Sigma_{\rm sync}|<\infty,
\]

或

\[
|\sigma^{-1}(s)|=O(1).
\]

必须分别研究：

\[
\text{shared-information structure},
\]

\[
\text{completion fibre size},
\]

\[
\text{family-dependent image size}.
\]

当前三者均可能无界。

这与 SGR fixed-core finite-fibre 是不同层次的问题，本报告不调用该正向 theorem 来制造 backward conclusion。

---

# 14. Is the macro abstraction now complete?

\[
\boxed{
\textbf{是。}
}
\]

理由不是“已经找到了 width = 2”，而恰恰是已经知道以后不应再追这种 presentation-dependent 数字。

当前 Backward Strict Layer 的宏观对象已经稳定为：

\[
\boxed{
\text{canonical complete state}
\to
\text{semantic recovery blocks}
\to
\text{canonical overlap quotients}
\to
\text{joint recovery image}.
}
\]

所有旧抽象问题都被定位到明确 theorem：

- “是否存在真正小 separator？”
  \(\Rightarrow\) lossless-join / explicit common-factor theorem；
- “root 是否 global？”
  \(\Rightarrow\) typed root-interface identification theorem；
- “local compatibility 是否足够？”
  \(\Rightarrow\) rectangularity；
- “global obstruction 如何表达？”
  \(\Rightarrow\) quotient-image separation / restricted joint-image emptiness。

因此继续做新的 variable inventory、relation counting、hyperedge width、separator coordinate guessing 已经没有必要。

下一轮应开始攻击第一个 concrete theorem。

---

# 15. Next theorem targets — at most three

## Q1. Lossless Synchronization / Rectangularity Theorem — **最高优先级**

### 目标

对 semantic blocks

\[
\mathcal R_{\rm alg},
\mathcal R_{\rm den},
\mathcal R_{10}
\]

证明 canonical pairwise overlap diagram 是 lossless：

\[
\boxed{
J_{\rm rec}
=
L_{\rm alg}
\Join_{\Sigma_{\rm alg,den}}
L_{\rm den}
\Join_{\Sigma_{\rm den,10}}
L_{10}
\Join_{\Sigma_{\rm alg,10}}
.
}
\]

若完整 equality 太强，第一目标改成：

> 找到一个严格描述 residual non-rectangularity 的唯一额外 compatibility relation。

### 成功意义

它直接决定：

- 是否存在真正的 sufficient synchronization quotient；
- 是否需要 higher-order relation；
- 哪些所谓 shared variables 只是 presentation artifact。

---

## Q2. Deterministic / finite fibre after synchronization trace

### 目标

固定

\[
s\in\Sigma_{\rm sync}^{\rm can}
\]

后，研究 global completion fibre：

\[
\mathcal F(s)
=
\{v\in\Omega_{\rm rec}:\sigma_{\rm Cech}(v)=s\}.
\]

目标优先级：

1. deterministic；或
2. uniformly \(O(1)\)；或
3. 可分解为彼此不共享的 local fibres。

### 纪律

不能用“quadratic 至多两个 roots”代替该 theorem。

必须控制的是 canonical completions，而不是 projected algebraic roots。

---

## Q3. Quotient Image Separation Theorem

### 目标

在 strict backward states 中证明：

\[
\boxed{
J_{\rm rec}
\cap
\prod_jF_j(\xi)
=
\varnothing,
}
\]

最好先在某 canonical overlap 上得到：

\[
\boxed{
\pi_{ij}(F_i(\xi))
\cap
\pi_{ij}(F_j(\xi))
=
\varnothing.
}
\]

这会把旧 arithmetic/root/decimal obstruction 统一成真正的 synchronization-image separation。

本 target 不使用 moving-core、height、square-spacing 或 valuation-growth theorem。

---

# 16. Proved / heuristic / open ledger

## PROVED — inherited

1. T3 canonical common-denominator reconstruction 是原题候选的双向恢复框架。
2. sphere integerization 与 positive \(t\) unique recovery。
3. Exact primitive recovery：
   \[
   \gcd(q,y_i)=q/b_i.
   \]
4. unified gap quadratic 与 primitive-tail quadratic。
5. 非退化整系数二次式的 rational-root existence 与 integer-square discriminant 等价。
6. rational-root divisibility：
   \[
   \nu\mid D(\kappa+2G),
   \qquad
   \mu\mid\kappa D\mathcal N_{12},
   \]
   \[
   \delta_3\mid\kappa(\kappa+2G),
   \qquad
   a_3\mid\mathcal C_3.
   \]
7. denominator-tail certificate：
   \[
   10^\ell\mid\kappa^2(\kappa+2G).
   \]
8. `strict_layer_final_campaign.md` N4–N5：现有 local valuation-position conditions 对允许位置模式仍局部相容，因此不能把 local prime-position data 当成 global synchronization theorem。

---

## DERIVED FROM PROVED RESULTS

1. canonical normalization 应吸收进 \(\Omega_{\rm can}\)，不应计作 synchronization gate。
2. complete canonical state 固定后，actual gap root、actual tail root、digit lengths、valuations、Exact-Lift coefficients 都是 deterministic projections。
3. 当前没有额外 intrinsic global branch coordinate。
4. gap root \([\mu:\nu]\) 与 tail root \(z_3\) 是不同 typed projections；现有 proof library 不支持把它们称作同一个 global root。
5. denominator-tail certificate 是 root/arithmetic/decimal 的 cross-projection，而不是独立第四 recovery world。
6. full \(\Lambda\) 不能仅因它是 canonical coordinate 就自动被宣布为 minimal synchronization datum。

---

## NEW PROVED

1. **Ambient-normalization correction**：删除独立 \(G_{\rm can}\) synchronization gate。
2. **Semantic recovery-block formalism**：root / denominator / decimal blocks 先 quotient 掉 proof-only representation。
3. **Maximal deterministic common-factor theorem (CSQ-0)**：
   \[
   \Sigma_{\rm com}
   =
   \Omega_{\rm rec}/\operatorname{EqCl}
   \left(\bigcup_j\ker\lambda_j\right)
   \]
   具有 universal property。
4. **Lossless-join criterion**：single-key synchronization quotient sufficient 当且仅当 joint image 在 \(\Sigma_{\rm com}\) 上 rectangular。
5. **No-coarser-rescue theorem**：若 maximal common factor 不 lossless，则任何更粗 deterministic common quotient 都不能修复 exact gluing。
6. **Canonical pairwise overlap quotients**：
   \[
   \Sigma_{\rm alg,den},
   \Sigma_{\rm den,10},
   \Sigma_{\rm alg,10}.
   \]
7. **Canonical structured synchronization object**：
   \[
   \Sigma_{\rm sync}^{\rm can}
   =
   \operatorname{Im}(\sigma_{\rm Cech})
   \]
   连同 joint image incidence，作为旧 width / relation-count formalism 的 presentation-invariant replacement。
8. quotient-image emptiness 与 restricted joint-image emptiness 给出稳定的 backward obstruction formulation。

---

## HEURISTIC

1. \(\Sigma_{\rm alg,den}\) 很可能可以显式写成“typed actual roots + recovery-coefficient arithmetic trace”的较小 package。
2. \(\Sigma_{\rm den,10}\) 很可能可显著小于完整 canonical state，但 exact balance 是否允许丢掉大部分 \(a_i,b_i\) 尚不清楚。
3. 在真正困难的 surviving states 上，固定 canonical synchronization trace 后 completion fibre 可能很小；但当前没有 uniform bound。
4. 一个单一 \((\Lambda,r)\)-type separator 即使最终存在，也必须作为 lossless-join theorem 的结果，而不能作为坐标猜测起点。

---

## OPEN

1. canonical joint image 是否在 maximal common factor / pairwise overlap diagram 上 lossless rectangular。
2. 是否存在 single-key sufficient synchronization quotient。
3. 若存在，能否给出显式 arithmetic coordinates。
4. full \(\Lambda\) 是否可以 quotient 成较小 denominator trace。
5. root ↔ denominator overlap 的最小显式 trace。
6. denominator ↔ decimal overlap 的最小显式 trace。
7. algebraic ↔ decimal overlap 的最小显式 trace。
8. 固定 synchronization state 后 completion fibre 是否 deterministic / uniformly finite。
9. 是否能在 \(\Sigma_{ij}\) 或 \(J_{\rm rec}\) 上证明 global image separation。

---

# 17. Final structural verdict

本轮最重要的结论不是

\[
\boxed{\text{width}=2}
\]

而是把“width”问题本身替换掉。

上一轮的问题是：

\[
\text{哪些 canonical coordinates 被多个 gates 读取？}
\]

本轮之后，正确问题是：

\[
\boxed{
\text{哪些 semantic recovery distinctions
能够被多个数学 blocks 共同观测？}
}
\]

以及：

\[
\boxed{
\text{这些 common observations 是否已经足以 losslessly glue？}
}
\]

canonical shared information 由 block kernels 的 common-factor lattice 决定，而不是由变量列表决定。

因此最终结构为：

\[
\boxed{
\Omega_{\rm rec}
\xrightarrow{\ \lambda_j\ }
L_j
\xrightarrow{\text{common-factor}}
\Sigma_{ij}
\quad\text{with joint image }J_{\rm rec}.
}
\]

若未来证明 rectangularity，则进一步收缩为

\[
\boxed{
\Omega_{\rm rec}
\longrightarrow
\Sigma_{\rm sync}
\longrightarrow
\text{independent local recovery fibres}.
}
\]

若 rectangularity 失败，则该失败本身就是新的、真正 presentation-invariant 的 global synchronization obstruction。

所以本轮可以正式宣布：

\[
\boxed{
\textbf{Backward Strict Layer 的宏观抽象阶段结束。}
}
\]

下一轮不再做结构 inventory；直接攻击：

\[
\boxed{
\textbf{Q1 — Lossless Synchronization / Rectangularity Theorem.}
}
\]

