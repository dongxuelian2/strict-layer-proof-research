# 三项十进制拼接平方和问题：Backward Strict Layer Canonical Recovery Dependency Skeleton

**文件名：** `strict_layer_backward_canonical_dependency_skeleton.md`  
**研究范围：** Backward Strict Layer 的宏观结构层；只研究 Exact-Lift 完整恢复系统的规范化变量、确定性消元、canonical gate、dependency skeleton、separator 与 presentation-invariant complexity。  
**明确冻结：** moving primitive core、square / deflated quadratic gate、square-spacing、height、\(2/5\)-adic moving-core capacity、resultant / polynomial coupling，以及任何具体 carrier / local obstruction 分支。

---

# 1. Executive summary

本轮的核心结论可以压成四句话。

第一，上一轮的 global witness 方向是正确的，但 recovery system 中绝大多数“变量”并不是真正自由变量。由 T3 的双向公共分母重构，一个完整候选可以用

\[
\boxed{
\bar\omega=(x_1,x_2,x_3,\Lambda)
}
\]

作为 canonical spine；一旦这四个正整数固定，并且 sphere gate 成立，则

\[
t,
\quad d_i,
\quad a_i,b_i,
\quad n_i,m_i,
\quad q,y_i,H,
\quad Q_{12},G,\mathcal N_{12},C,D,\kappa,
\quad \text{全部 valuation / digit / tail data}
\]

都由严格定义唯一恢复。Exact-Lift 中出现的 gap root、primitive-tail root、discriminant square root、Hensel branch、prime-allocation label 等，不应自动计作新的 candidate freedom。

第二，经过 deterministic elimination，当前已经严格得到

\[
\boxed{
\mathcal V_{\rm red}
=
\{x_1,x_2,x_3,\Lambda\}.
}
\]

这里的“四维”只表示 **canonical unbounded integer coordinates 的数量**，不是实代数几何意义上的维数，也不是说存在四个彼此独立的连续自由参数。对给定 partial state \(\xi\)，若其中某些坐标已被固定，则相对 recovery dimension 还会进一步下降。

第三，上一轮的

\[
h_{\mathfrak R}
=
\min\{|J|:\Join_{j\in J}R_j=\varnothing\}
\]

不是内在复杂度。把完整 exact kernel 打包成一个 relation，可使所有 non-liftability 都有 \(h=1\)；按 T3 写成 sphere / canonical recovery / exact balance 三条 relation，则自动 \(h\le3\)；继续把某一数学 gate 拆成许多标量、素数或 valuation 条件，又可人为增大 \(h\)。因此本报告废弃“raw relation count”作为 intrinsic invariant。

第四，本轮提出并规范化真正应该追踪的量：

\[
\boxed{
\kappa_{\rm rec}
=
\textbf{canonical synchronization width}.
}
\]

它不是数 relation，也不是数某个整数变量有多少候选值，而是衡量：在一个允许的 canonical recovery decomposition 中，为了把各 recovery blocks 做 natural join，最坏情况下必须同时传递多少个 **canonical unbounded coordinates**。

当前材料严格给出：

\[
\boxed{
\kappa_{\rm rec}\le4.
}
\]

更精确地，T3 当前显式 canonical presentation 的 synchronization width 恰为 \(4\)，因为 canonical denominator gate 与 exact balance gate 都读取全部

\[
(x_1,x_2,x_3,\Lambda).
\]

但本轮**没有证明内在最小值就是 4**；若未来找到一个真实 recovery factorization，把这两个 full-scope gates 经一个更小的 functional separator 分解，则 \(\kappa_{\rm rec}\) 可以下降。因此真正新的 Backward frontier 不是“证明只有 2 或 4 个 global states”，而是：

\[
\boxed{
\text{能否把当前四坐标同步宽度严格降到 }3\text{ 或 }2？
}
\]

本轮对最初问题的回答是：

\[
\boxed{
\text{当前可见困难主要不是 auxiliary candidate values 太多，}
}
\]

而是

\[
\boxed{
\text{少数无界的 canonical integer coordinates 被多个 recovery gates 共同读取。}
}
\]

换言之，Backward system 更像 **bounded structural width + unbounded assignment sets**，而不是一个 uniformly finite synchronization automaton。

**本轮等级：CANONICALIZATION + NEW STRUCTURAL FORMALISM；没有产生新的 death region。**

---

# 2. Anti-duplication boundary

## 2.1 本轮使用的 backward / Exact-Lift 材料

重点审计：

- `strict_layer_backward_global_witness_gluing_campaign.md`；
- `strict_layer_backward_global_obstruction_campaign.md`；
- `exact_lift_research_synthesis_2026-08-10.md`；
- `strict_layer_final_campaign.md`；
- T3 / T4 的已审计结果索引与后续回查材料。

特别回查了：

- T3 canonical common-denominator reconstruction；
- Exact primitive recovery
  \[
  \gcd(q,y_i)=q/b_i;
  \]
- gap quadratic；
- primitive tail quadratic；
- rational-root divisibility；
- denominator-tail certificate
  \[
  10^\ell\mid\kappa^2(\kappa+2G).
  \]

## 2.2 正向材料仅用于划界

当前最新正向 strict-layer 报告是 moving-core square-spacing 线。它继续负责：

- moving primitive core；
- uniform termination；
- square / square-spacing；
- height；
- actual-lift \(2/5\)-adic capacity；
- resultant / polynomial coupling；
- 从 reachable states 正向推进到 contradiction。

本报告不使用这些结论建立任何新的 backward theorem。

最新正向报告还修正了 strict-scope：严格层只保留其当前定义下真正 strict 的 carrier 区域；本报告不进入任何 carrier 分支，因此这一修正只作为范围检查，不影响下面的 chamber-free skeleton。

---

# 3. Raw recovery variable inventory

先故意把 Exact-Lift / T3 / backward gluing 中曾出现的对象全部列入 raw inventory：

\[
\begin{aligned}
\mathcal V_{\rm raw}=
\{&a_i,b_i,r_i,
\alpha_i,\beta_i,s_i,
A,B,\Lambda,
 x_i,t,d_i,\\
&q,y_i,H,
Q_{12},G,\mathcal N_{12},C,D,\kappa,K_{C,D},\\
&\mu,\nu,W,
\ell,\delta_3,L,\tau,z_3,\mathcal C_3,\\
&\{v_p(\cdot)\}_p,
\text{prime-support / allocation data},\\
&\text{Hensel labels},
\text{Gaussian labels},
\text{CRT representatives},
\text{enumeration indices},\ldots\}.
\end{aligned}
\]

这里把原报告中同名但不同用途的 \(L\) 分开：

- 本报告的 canonical common denominator 始终写作 \(\Lambda\)；
- Exact-Lift tail normalization 中的 quotient 继续写作 \(L\)。

下面不按“它在哪份报告里出现”分类，而按它是否真正增加 recovery freedom 分类。

---

# 4. Candidate / deterministic / branching / unbounded / artifact classification

## 4.1 A. Canonical candidate variables

### 原始 candidate level

原题完整候选可写成六个既约正整数块：

\[
(a_1,b_1,a_2,b_2,a_3,b_3),
\qquad
\gcd(a_i,b_i)=1.
\]

它们当然属于 candidate data，但不是最小的 recovery representation。

### T3 canonical level

令

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),
\qquad
x_i=\frac{\Lambda a_i}{b_i}.
\]

T3 给出反向恢复

\[
d_i=\gcd(x_i,\Lambda),
\qquad
a_i=\frac{x_i}{d_i},
\qquad
b_i=\frac{\Lambda}{d_i},
\]

并用

\[
\gcd(x_1,x_2,x_3,\Lambda)=1
\]

保证 canonical minimality。

因此，本报告选择

\[
\boxed{
\mathcal V_{\rm cand}^{\rm can}
=
(x_1,x_2,x_3,\Lambda).
}
\]

**等级：DERIVED FROM PROVED RESULTS。**

这里不把 \(t\) 算作额外自由坐标，因为若

\[
x_1^2+x_2^2+x_3^2=t^2
\]

有正整数解，则

\[
t=\sqrt{x_1^2+x_2^2+x_3^2}>0
\]

唯一。

---

## 4.2 B. Deterministic derived variables

一旦

\[
(x_1,x_2,x_3,\Lambda)
\]

固定，以下对象不增加 recovery state dimension。

### 第一层：T3 exact recovery

\[
t,
\qquad
d_i=\gcd(x_i,\Lambda),
\]

\[
a_i=x_i/d_i,
\qquad
b_i=\Lambda/d_i.
\]

依据分别是：

- positive-square unique recovery；
- gcd normalization；
- exact T3 recovery formulas。

### 第二层：decimal data

\[
\alpha_i=\ell(a_i),
\qquad
\beta_i=\ell(b_i),
\qquad
s_i=\alpha_i-\beta_i,
\]

以及

\[
A=\operatorname{concat}(a_1,a_2,a_3),
\qquad
B=\operatorname{concat}(b_1,b_2,b_3).
\]

这些由真实十进制表示唯一决定，不需要另加 digit representative。

### 第三层：Exact integer-sphere variables

由 T3 / Exact-Lift bridge：

\[
q=\Lambda,
\qquad
y_i=x_i,
\qquad H=t
\]

在 canonical witness 语言下只是同一对象的改名；在 primitive-profile 语言中的进一步 content quotient 也不增加 backward candidate freedom。

### 第四层：Exact-Lift block coefficients

一旦原始块及其 digit profile 固定，

\[
Q_{12},
\quad G,
\quad \mathcal N_{12},
\quad C,D,
\quad \kappa,
\quad K_{C,D}
\]

都由 Exact-Lift 的定义唯一计算。

例如：

\[
Q_{12}=b_1 10^{\beta_2}+b_2,
\]

\[
G=b_1b_2,
\]

\[
\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2.
\]

不同 carrier normalization 对 \(C,D\) 有不同显式公式，但 carrier label 本身由 digit profile 决定；它不是额外 independent choice。

### 第五层：valuation / prime / tail metadata

全部

\[
v_p(a_i),\quad v_p(b_i),\quad v_p(\kappa),\ldots
\]

以及 prime support、denominator graph、digit windows、tail demand 均为上述整数的函数。

只要某个 tail normalization

\[
10^\ell=\delta_3L,
\qquad
b_3=\delta_3\tau,
\qquad
z_3=a_3/\delta_3
\]

在对应 Exact-Lift recovery map 中已被定义，则 \(\ell,\delta_3,L,\tau,z_3\) 也是完整候选的投影数据，而不是新的 original-candidate freedom。

**等级：DERIVED FROM PROVED RESULTS。**

---

## 4.3 C. Genuine branching witnesses

这里必须区分：

\[
\boxed{
\text{candidate freedom}
\neq
\text{projected search branching}.
}
\]

### Gap quadratic root

Exact-Lift gap quadratic理论上至多给出两个 algebraic roots，但完整候选若存在，其实际 reduced ratio

\[
[\mu:\nu]
\]

已经由该候选决定。

因此：

\[
\boxed{
\text{root choice 是 compressed search space 的有限分支，}
}
\]

而不是 canonical candidate 的新增自由坐标。

### Primitive tail root

同理，

\[
z_3=a_3/\delta_3
\]

由完整候选决定。二次方程有两个理论 roots 不等于 global witness 多了一个独立二值变量。

### Discriminant square root

若

\[
\Delta=W^2,
\]

则 \(|W|\) 由 \(\Delta\) 决定，\(W\leftrightarrow-W\) 通常只是 certificate symmetry。只有当后续恢复公式确实区分方向，符号才应作为局部 branch label；即便如此，它仍需与同一 canonical candidate 一致。

### Prime / Gaussian allocation

若某个 allocation label 仅表示同一整数因子的证明分配、associate / conjugate 选择或搜索路径，则应删除。

只有当两个 allocation choices 真正对应不同 completion fibres 时，才可暂时保留为 **finite projected branch variable**；在完整 candidate level，它仍不是独立于候选的数据。

### 本轮结论

当前已审计材料没有证明存在一个必须额外附加到

\[
(x_1,x_2,x_3,\Lambda)
\]

之后、才能描述原题完整候选的 intrinsic branch coordinate。

所以：

\[
\boxed{
\text{known intrinsic branching dimension}=0
}
\]

是对**当前 canonical complete-candidate representation** 的陈述。

这不表示 projected search 没有有限 branching。

**等级：NEW PROVED（由 T3 completeness + 已审计 projection 性质直接推出的组织性结论）。**

---

## 4.4 D. Unbounded shared witnesses

这是本轮最重要的分类。

虽然 intrinsic auxiliary branching 没有增加 canonical dimension，但

\[
\boxed{
(x_1,x_2,x_3,\Lambda)
}
\]

本身是无界整数数据。

特别是：

- \(\Lambda\) 同时控制逐坐标 gcd、reduced denominators、prime support、valuation、digit lengths 和 tail arithmetic；
- \((x_1,x_2,x_3)\) 同时进入 sphere gate、T3 recovery、numerator blocks、digit data 和 exact balance；
- Exact-Lift 的 root / tail / congruence certificates最终都必须是**这同一组整数的投影**。

因此系统确实存在：

\[
\boxed{
\text{取值范围随总体参数无界增长的共享整数状态。}
}
\]

这立刻排除一种过强期待：

\[
\boxed{
\text{不能仅凭“quadratic 每次至多两个 roots”推出 global state 数 uniformly finite。}
}
\]

---

## 4.5 E. Proof artifacts

下列对象原则上全部从最终 skeleton 删除，除非未来证明它们编码了真正不同的 completion fibre：

- Hensel path / lift-depth label；
- Gaussian flip label；
- Gaussian associate / conjugate 的纯表示选择；
- enumeration index；
- finite-search representative ID；
- CRT 合并顺序；
- proof route 名称；
- near-square / near-\(S\)-unit 等现象标签；
- discriminant sign，若后续 relation 只读取 \(W^2\)；
- carrier 名称，若 digit profile 已在 ambient state 中确定。

这些对象可以影响证明工程，但不应影响数学 recovery state dimension。

---

# 5. Deterministic elimination chain

本节把整个 raw system 做一次严格、可审计的 elimination。

## 5.1 Stage E0 — remove aliases and redundant ratios

原始

\[
r_i=a_i/b_i
\]

是 \((a_i,b_i)\) 的确定函数；\(A,B\) 是 block tuples 的确定函数。

因此先做

\[
\mathcal V_{\rm raw}
\to
\mathcal V_0
\]

删除所有纯 alias / deterministic concat objects。

**依据：exact equality / definition。**

---

## 5.2 Stage E1 — T3 canonicalization

用

\[
\Lambda=\operatorname{lcm}(b_i),
\qquad
x_i=\Lambda a_i/b_i
\]

及 T3 的逆恢复

\[
d_i=\gcd(x_i,\Lambda),
\qquad
a_i=x_i/d_i,
\qquad
b_i=\Lambda/d_i
\]

把六个原始 block integers 换成

\[
(x_1,x_2,x_3,\Lambda)
\]

与 deterministic recovery map。

于是

\[
\mathcal V_0
\to
\mathcal V_1
=
\{x_1,x_2,x_3,t,\Lambda;\text{derived Exact data}\}.
\]

**依据：T3 exact bidirectional reconstruction + gcd normalization。**

---

## 5.3 Stage E2 — eliminate \(t\)

把

\[
x_1^2+x_2^2+x_3^2=t^2,
\qquad t>0
\]

改写为 predicate

\[
\boxed{
x_1^2+x_2^2+x_3^2\in\square_{>0}
}
\]

并在 gate 通过时唯一恢复

\[
t=\sqrt{x_1^2+x_2^2+x_3^2}.
\]

于是

\[
\mathcal V_1
\to
\mathcal V_2
=
\{x_1,x_2,x_3,\Lambda;\text{derived Exact data}\}.
\]

**依据：unique positive recovery。**

---

## 5.4 Stage E3 — eliminate gcd / reduced / digit variables

全部

\[
d_i,
\quad a_i,b_i,
\quad \alpha_i,\beta_i,s_i,
\quad v_p(a_i),v_p(b_i)
\]

由 \(\mathcal V_2\) 唯一计算。

将所有 relation pull back：若

\[
z=f(x_1,x_2,x_3,\Lambda),
\]

则

\[
R(x_1,x_2,x_3,\Lambda,z)
\]

改写为

\[
R'(x_1,x_2,x_3,\Lambda)
=
R(x_1,x_2,x_3,\Lambda,f(\cdot)).
\]

**依据：gcd normalization + deterministic digit length + valuation identity。**

---

## 5.5 Stage E4 — eliminate Exact-Lift coefficient objects

将

\[
Q_{12},G,\mathcal N_{12},C,D,\kappa,K_{C,D},\mathcal C_3,\ldots
\]

全部替换为其已证定义式。

这些量仍然非常有用，因为它们能把一个复杂 pullback predicate 写短；但从 dependency skeleton 角度，它们只是 **named deterministic summaries**。

因此允许在公式中继续使用名字，却不给它们新增 vertex。

**依据：exact definitions / branch normalization determined by digit profile。**

---

## 5.6 Stage E5 — existential elimination of projected roots

对 gap root、tail root、square root 等对象采用：

\[
\exists r\in\mathcal R(x):
\Phi(x,r)
\]

而不是把 \(r\) 永久扩张成 candidate coordinate。

更具体地：

- gap quadratic 的 theoretical root variable被编译成“存在 admissible actual gap projection”；
- primitive tail root被编译成“候选的 actual \(z_3\) 满足 tail recovery relation”；
- \(W\) 被编译为 discriminant-square predicate；
- root sign若只是 \(\pm\) symmetry则 quotient 掉。

在需要研究 low-dimensional separator 时，可以**重新引入** root 作为 functional separator coordinate；但这是一种 factorization device，不改变 intrinsic complete-witness dimension。

**依据：candidate \(\to\) root projection is deterministic；theoretical root multiplicity is search branching。**

---

## 5.7 Stage E6 — remove proof artifacts

删除 Hensel / Gaussian / enumeration / route labels，只保留它们真正推出的 mathematical predicate。

**依据：这些 label 不改变 completion set。**

---

## 5.8 Final reduced witness space

最终：

\[
\boxed{
\mathcal V_{\rm raw}
\to
\mathcal V_0
\to
\mathcal V_1
\to
\mathcal V_2
\to
\cdots
\to
\mathcal V_{\rm red}
=
\{x_1,x_2,x_3,\Lambda\}.
}
\]

对 partial strict state \(\xi\)，定义

\[
\mathcal V_{\rm red}(\xi)
\subseteq
\{x_1,x_2,x_3,\Lambda\}
\]

为尚未被 \(\xi\) 固定的坐标。

本轮没有找到任何依据允许继续 **deterministically** 删除 \(x_i\) 中的一个或 \(\Lambda\)。

注意这不等于证明四个坐标是任何可能参数化下的绝对最小值；只是：

\[
\boxed{
\text{在当前 exact recovery maps 下，确定性消元到这里停止。}
}
\]

---

# 6. Reduced witness space

定义

\[
\Omega_{\rm red}
=
\mathbf Z_{>0}^4,
\qquad
v=(x_1,x_2,x_3,\Lambda).
\]

对 strict state \(\xi\)，先把所有 state-fixed information 编译进 ambient fibre

\[
\Omega_\xi\subseteq\Omega_{\rm red}.
\]

这样 digit-cell、已固定 profile、已固定 sign / normalization 等**状态描述**不需要重复成为 recovery relation。

定义 deterministic reconstruction map

\[
\mathfrak R_{\rm T3}:\Omega_{\rm red}
\dashrightarrow
(a_1,b_1,a_2,b_2,a_3,b_3,t,\ldots).
\]

它只在 sphere-square 与 canonical normalization 等条件满足时落入合法完整候选空间。

Backward liftability 的 exact terminal form 是

\[
\boxed{
\operatorname{Liftable}(\xi)
\iff
\exists v\in\Omega_\xi
:\
G_{\rm sph}(v)
\wedge
G_{\rm can}(v)
\wedge
G_{\rm bal}(v).
}
\tag{6.1}
\]

这是后面所有 certificate gates 的母空间。

---

# 7. Canonical atomic recovery gates

## 7.1 为什么不存在绝对唯一的 atomic presentation

一个数学条件永远可以被：

- 与别的条件合取；
- 拆成多个标量等式；
- 按素数拆成无限族 valuation inequalities；
- 加入中间变量再改写；
- 消去中间变量后重新打包。

因此不存在不加规则就自动唯一的“relation 原子”。

本报告不强行声称唯一，而定义允许的 presentation class

\[
\boxed{
\mathfrak P_{\rm can}.
}
\]

---

## 7.2 \(\mathfrak P_{\rm can}\) 的规则

一个 presentation 属于 \(\mathfrak P_{\rm can}\)，要求：

### P1. Canonical-variable rule

真正 free vertices 只能来自

\[
\mathcal V_{\rm red}.
\]

允许使用 deterministic summary，但 summary 不增加 vertex dimension。

### P2. Recovery-map rule

一个 atomic gate 必须对应一个数学上已有意义的 recovery map / admissible fibre，而不是为了调节 relation 数量临时构造的 conjunction。

### P3. Equivalent-test compilation

同一 recovery map 上彼此等价的测试必须编译成同一 gate。

典型例：对非退化整系数二次式，

\[
\text{存在有理根}
\iff
\text{discriminant 是整数平方}
\]

在 pure algebraic-root-existence 层是一个 gate 的两种写法，不计作两个 atoms。

### P4. Necessary-projection rule

rational-root theorem divisibility、单个 \(p\)-adic inequality、prime-position condition 等若只是 parent recovery gate 的必要投影，则只作为 certificate / internal test，不升级成独立 atom。

### P5. Cross-certificate rule

例如

\[
10^\ell\mid\kappa^2(\kappa+2G)
\]

是 tail root denominator recovery 与 decimal tail realization 的交叉必要投影；它是强 certificate，但不应为了 relation counting 被当成一个与两端完全独立的新世界。

### P6. No artificial packing

不能为了把 \(h\) 变小，把互相独立的 recovery maps 任意合并为

\[
R_{\rm mega}=R_1\wedge\cdots\wedge R_m.
\]

### P7. No artificial scalarization

不能为了把 \(h\) 变大，把一个单一 recovery requirement 拆成几十个系数相等、素数坐标或 proof steps。

### P8. Branch quotient rule

若 branch label 由 digit profile决定，或 \(\pm\) / Gaussian associate 只表示同一 completion，则在 atomic presentation 中 quotient 掉。

---

## 7.3 Exact kernel 的 canonical atoms

最小而不失 exact equivalence 的 T3 kernel 保留三个数学 gate。

### \(G_{\rm sph}\) — sphere-square realization

\[
\boxed{
x_1^2+x_2^2+x_3^2\in\square_{>0}.
}
\]

scope：

\[
\{x_1,x_2,x_3\}.
\]

### \(G_{\rm can}\) — canonical denominator normalization

\[
\boxed{
\gcd(x_1,x_2,x_3,\Lambda)=1.
}
\]

以及其 T3 deterministic recovery map。

scope：

\[
\{x_1,x_2,x_3,\Lambda\}.
\]

### \(G_{\rm bal}\) — exact decimal reconstruction / balance

恢复 \(a_i,b_i,t\) 后要求

\[
\boxed{
\Lambda\,\operatorname{concat}(a_1,a_2,a_3)
=
t\,\operatorname{concat}(b_1,b_2,b_3).
}
\]

scope：

\[
\{x_1,x_2,x_3,\Lambda\}.
\]

这三个 gate 与 ambient state fibre \(\Omega_\xi\) 联立，就是 exact liftability；任何其他 Exact-Lift obstruction certificate 都是该 exact candidate set 的必要 projection / relaxation。

---

## 7.4 Canonical certificate blocks

为了实际做 backward obstruction 搜索，仍然值得保留若干 parent recovery maps：

- \(C_{\rm gap}\)：完整 admissible gap-root recovery；
- \(C_{\rm tail}\)：完整 admissible primitive-tail recovery；
- \(C_{\rm den}\)：canonical denominator / gcd / prime-demand feasibility；
- \(C_{\rm dec}\)：digit / tail / representative realizability；
- \(G_{\rm bal}\)：最终 exact reconstruction residual。

但这里的“block”不是说它们互相独立；它们都通过同一个 \(\mathcal V_{\rm red}\) 取值。

其内部：

- discriminant square 不再与 rational-root existence 分列；
- RRT divisibility不单列；
- \(v_2\) 与 \(v_5\) tail capacity不分成两个 atoms；
- Hensel / near-square / near-\(S\)-unit 只作为证明方法或内部 certificate。

---

# 8. Reduced dependency hypergraph

## 8.1 Vertices

真正的 vertices 只有

\[
\boxed{
V(\mathscr H_{\rm rec})
=
\{x_1,x_2,x_3,\Lambda\}.
}
\]

---

## 8.2 Exact hyperedges

T3 exact kernel 给出：

\[
E_{\rm sph}
=
\{x_1,x_2,x_3\},
\]

\[
E_{\rm can}
=
\{x_1,x_2,x_3,\Lambda\},
\]

\[
E_{\rm bal}
=
\{x_1,x_2,x_3,\Lambda\}.
\]

因此最短 exact hypergraph 是：

```text
              G_sph
          {x1,x2,x3}
                |
                |
      -----------------------
      |                     |
    G_can                 G_bal
{x1,x2,x3,Λ}          {x1,x2,x3,Λ}
```

这张图刻意很短，因为所有 gcd、digit、valuation、quadratic coefficient 等 deterministic summaries 都已经被消去。

---

## 8.3 Certificate hyperedges

Gap / tail / denominator / decimal certificates可以作为 exact hypergraph 的“挂载块”，但不增加 vertex：

```text
                 {x1,x2,x3,Λ}
                        |
       ------------------------------------
       |          |          |            |
     C_den      C_gap      C_tail        C_dec
       \          |          |            /
        \         |          |           /
                 G_bal
```

在没有新的 factorization theorem 前，保守地说这些 block 的 source support 均包含于四坐标 spine；不能因为它们的输出 summary 只有一个整数 root / 一个 residue class，就把 support dimension 误计为 1。

---

## 8.4 真正传播 dependency 的 shared variables

### \(\Lambda\)

它是最显眼的全局 shared integer：

\[
\Lambda
\to
\gcd(x_i,\Lambda)
\to
b_i
\to
\text{valuation / prime / digit / tail data}.
\]

但固定 \(\Lambda\) 后，三个 \(x_i\) 仍被 sphere 与 exact balance 强耦合，所以 \(\Lambda\) **不是** 完整 separator。

### \((x_1,x_2,x_3)\)

它们共同决定 sphere，同时经 gcd recovery 进入全部 numerator blocks 与 exact balance。

因此当前 recovery difficulty 不是一个“只剩公共分母”的一维问题。

### Projected roots

actual gap root / tail root可以横跨 algebraic、denominator、digit gates，但它们是四坐标 spine 的 deterministic projection。它们可能成为未来低维 separator 的好坐标，却不是已经证明的 complete separator。

---

# 9. Relation-granularity problem and resolution

## 9.1 为什么旧 \(h_{\mathfrak R}\) 不是 intrinsic

设完整 exact feasible set 为

\[
\mathcal J
=
R_1\Join\cdots\Join R_m.
\]

如果定义

\[
R_{\rm all}:=\mathcal J,
\]

则每个 non-liftable state 都满足

\[
h_{\{R_{\rm all}\}}=1.
\]

若采用 T3 exact kernel：

\[
\{G_{\rm sph},G_{\rm can},G_{\rm bal}\},
\]

则任何 empty exact join 自动有

\[
h\le3.
\]

反之，把 \(G_{\rm bal}\) 或 \(C_{\rm den}\) 按十进制位、素数、valuation、系数逐条拆开，minimal empty subfamily 的 relation 数又可能增加。

所以：

\[
\boxed{
h_{\mathfrak R}
\text{ 只能作为 fixed presentation 下的 diagnostic，不能作为 recovery invariant。}
}
\]

**等级：NEW PROVED。**

---

## 9.2 规范化解决方案

本报告采用两步：

1. relation 层面只允许 \(\mathfrak P_{\rm can}\)；
2. 真正 complexity 不数 relations，而数 canonical separator support。

于是 arbitrary merge / split 不再直接改变主 invariant。

---

# 10. Presentation-invariant complexity candidate

## 10.1 Essential canonical support

对一个 normalized gate \(G\)，定义

\[
\operatorname{EssSupp}(G)
\subseteq
\mathcal V_{\rm red}
\]

为：gate 的真值真正依赖的 canonical coordinates。

重要的是：如果一个 scalar summary

\[
s=f(x_1,x_2,\Lambda)
\]

只有一个输出整数，仍然不能说它的 synchronization dimension 是 1；它的 canonical support 是

\[
\{x_1,x_2,\Lambda\}.
\]

这阻止了用“把四个整数编码成一个大整数”之类纯表示技巧伪造低维 separator。

---

## 10.2 Canonical separator tree

把 normalized recovery blocks 放在一棵 join tree 上。

删去任一 tree edge \(e\) 后，blocks 分成左右两组 \(L_e,R_e\)。令

\[
S_e
=
\operatorname{Vars}(L_e)
\cap
\operatorname{Vars}(R_e)
\]

为两侧必须共同携带的 canonical information。

定义该 decomposition 的 width：

\[
\operatorname{width}(T)
=
\max_e |S_e|.
\]

这里 \(|S_e|\) 只数 canonical unbounded coordinates；finite branch labels、proof labels、deterministic summaries不另加维数。

---

## 10.3 定义 \(\kappa_{\rm rec}\)

定义

\[
\boxed{
\kappa_{\rm rec}
:=
\inf_{\mathcal P\in\mathfrak P_{\rm can}}
\inf_{T\text{ canonical separator decomposition of }\mathcal P}
\operatorname{width}(T).
}
\tag{10.1}
\]

语义：

> 在不使用人为打包、拆分或编码的前提下，实现完整 recovery synchronization 时，最坏情况下最少必须同时共享多少个 canonical unbounded coordinates。

这是本报告建议替代 \(h_{\mathfrak R}\) 的主 complexity。

---

## 10.4 当前严格可得的 bound

使用 T3 presentation：

\[
E_{\rm sph}=\{x_1,x_2,x_3\},
\]

\[
E_{\rm can}=E_{\rm bal}
=\{x_1,x_2,x_3,\Lambda\}.
\]

任意连接 \(G_{\rm can}\) 与 \(G_{\rm bal}\) 的 separator 在该 presentation 中都必须携带四个 canonical coordinates。

所以当前 presentation width 为

\[
\boxed{4}.
\]

因此 intrinsic infimum 满足

\[
\boxed{
\kappa_{\rm rec}\le4.
}
\tag{10.2}
\]

**等级：NEW PROVED。**

本轮没有证明

\[
\kappa_{\rm rec}=4.
\]

因为未来可能发现 \(G_{\rm can}\) 或 \(G_{\rm bal}\) 的 genuine recovery factorization，通过一个 essential support 更小的 separator 完成相同 exact synchronization。

所以：

\[
\boxed{
\kappa_{\rm rec}\le3\ ?
\qquad
\kappa_{\rm rec}\le2\ ?
}
\]

都是新的、非平凡的 **OPEN structural questions**。

---

## 10.5 Separator-projection certificate lemma

这里可以得到一个纯结构性的 NEW PROVED lemma。

设 canonical recovery system 已有一棵合法 separator tree。对某条 edge \(e\)，左、右两侧完整 join 分别记为

\[
\mathcal J_L,
\qquad
\mathcal J_R,
\]

公共 separator 为 \(S_e\)。则

\[
\mathcal J_L\Join\mathcal J_R=\varnothing
\]

当且仅当：

- \(\mathcal J_L=\varnothing\)，或
- \(\mathcal J_R=\varnothing\)，或
- 两侧在 separator 上的可实现投影不相交：

\[
\boxed{
\pi_{S_e}(\mathcal J_L)
\cap
\pi_{S_e}(\mathcal J_R)
=
\varnothing.
}
\tag{10.3}
\]

证明只是 natural join 定义：两侧能 glue 当且仅当存在一对 assignments 在全部共享变量上取同值。递归沿 tree 应用，就得到：

\[
\boxed{
\text{global emptiness}
\Rightarrow
\text{某 canonical block locally empty，或某 separator 上两大块投影不兼容。}
}
\tag{10.4}
\]

这才是 presentation-invariant small-certificate 的正确雏形。

它数的是：

- canonical blocks；
- separator support dimension；

而不是 raw relation 条数。

---

# 11. Finite core vs bounded width

本轮必须把三个概念彻底分开。

## 11.1 Finite number of variables

当前 canonical complete-witness spine 只有

\[
\boxed{4}
\]

个整数坐标。

这是 **PROVED / DERIVED**。

---

## 11.2 Finite number of assignments

完全不同。

\[
(x_1,x_2,x_3,\Lambda)
\]

的 ambient ranges 随问题尺度无界。

现有材料没有证明存在常数 \(K\) 使所有 strict state 的完整 separator 只有 \(K\) 个 possible assignments。

尤其不能从：

\[
\text{fixed quadratic has at most two roots}
\]

推出：

\[
\text{global recovery has at most two states}.
\]

因为 quadratic coefficients 本身随 canonical integer data 变化；而 actual root 只是这些 data 的 projection。

所以旧“finite synchronization core”若含义是

\[
|\operatorname{Assign}(S_{\rm core})|\le K,
\]

当前应标为：

\[
\boxed{
\textbf{UNSUPPORTED / likely too strong as a first target}.
}
\]

---

## 11.3 Bounded structural width

这才是目前严格成立的 bounded statement：

\[
\boxed{
\kappa_{\rm rec}\le4.
}
\]

也就是说，assignment 数量可能无界，但 global constraints 并没有引入无界多个彼此独立的 recovery coordinates。

因此 Backward line 当前最有希望 bounded 的对象是：

\[
\boxed{
\text{separator support dimension / synchronization width},
}
\]

而不是：

\[
\boxed{
\text{separator assignment cardinality}.
}
\]

---

# 12. Separator analysis

## 12.1 一个严格存在但平凡的 separator

取

\[
\boxed{
S_{\rm sep}^{(4)}
=(x_1,x_2,x_3,\Lambda).
}
\]

固定它以后：

- \(t\) 唯一；
- \(a_i,b_i\) 唯一；
- 所有 Exact-Lift coefficients 唯一；
- root / tail / valuation / digit / residual predicates 的真值全部确定。

所以所有 recovery blocks 在该 separator value 下都没有剩余 candidate freedom。

因此它确实是 complete separator。

但：

\[
\boxed{
|S_{\rm sep}^{(4)}|_{\rm coordinates}=4,
\qquad
|\operatorname{Dom}_{\rm global}(S_{\rm sep}^{(4)})|
\text{ 不 uniformly finite；同时没有 theorem 给出 feasible assignments 的 uniform bound}.
}
\]

这正好展示了“finite variable count”和“finite assignments”的差别。

---

## 12.2 \(\Lambda\) 单独不是 separator

固定 \(\Lambda\) 后：

- sphere 仍耦合三个 \(x_i\)；
- gcd patterns 仍随 \(x_i\) 变化；
- numerator blocks 与 digit lengths 仍变化；
- exact concatenation balance 仍同时读取三个 \(x_i\)。

因此没有严格依据写成

\[
\mathcal J
=
\mathcal J_1
\times_\Lambda
\mathcal J_2
\times_\Lambda
\mathcal J_3.
\]

**结论：不存在“公共分母一维 separator 已经证明”的情况。**

---

## 12.3 一个 algebraic root 单独也不是 separator

固定 gap root 或 tail root，只固定了某个 Exact-Lift projection。

目前没有定理说明：

\[
\text{root}
\Longrightarrow
(x_1,x_2,x_3,\Lambda)
\text{ 的其余 recovery data 唯一}.
\]

特别是 denominator / digit / exact-balance information 不会自动从“有一个 admissible root”恢复。

所以：

\[
\boxed{
\text{root 是 promising separator coordinate，}
\text{但尚不是 proved separator。}
}
\]

---

## 12.4 \((\Lambda,\text{root})\) 是否足够？

这是本轮最自然出现的非平凡候选。

设

\[
S_*=(\Lambda,r_{\rm rec}),
\]

其中 \(r_{\rm rec}\) 表示一个真正 global admissible recovery root，而非某个局部 \(p\)-adic root label。

若能证明固定 \(S_*\) 后：

- denominator / prime block；
- algebraic block；
- decimal / tail block；
- exact reconstruction block

彼此只剩 deterministic 或 uniformly finite fibres，则可把 synchronization width 从 \(4\) 真正降到 \(2\)（或至多再加一个 canonical coordinate）。

但当前 proof library 没有这一定理。

**等级：OPEN / high-value hypothesis。**

---

## 12.5 当前 separator tree

以已证 T3 exact atoms为准，最保守 join tree 必须包含一个 full four-coordinate overlap：

```text
G_sph {x1,x2,x3}
          |
          |
G_can {x1,x2,x3,Λ}
          |
          |  separator = {x1,x2,x3,Λ}
          |
G_bal {x1,x2,x3,Λ}
```

各 certificate blocks只能作为 deterministic pullbacks / leaves 挂在其上。

所以当前真正已证的是：

\[
\boxed{
\text{separator tree exists with width }4.
}
\]

不是：

\[
\boxed{
\text{存在一个只有 2 个值或 4 个值的 finite core}.
}
\]

---

## 12.6 旧 obstruction 的 separator 解释

在一个未来更小的 separator tree 中，旧 obstruction 应被重新解释为：

- **root obstruction**：某 separator value 下 algebraic recovery fibre 为空；
- **prime / denominator obstruction**：某 separator value 下 denominator-completion fibre 为空；
- **tail / digit obstruction**：某 separator value 下 decimal-completion fibre 为空；
- **global synchronization obstruction**：左右两个非空 block 在 separator 上允许的 values 不相交。

这比“arith/root/dec 是三个平行世界”更准确。

---

# 13. Reassessment of previous G1 / G2 / G3

## 13.1 G1 — finite synchronization core

旧表述若指：

\[
|S_{\rm core}|\le2\text{ or }4
\]

必须先问 \(|\cdot|\) 是什么。

### 若表示 variable / coordinate count

当前已经有：

\[
\boxed{
|\mathcal V_{\rm red}|=4
}
\]

作为 canonical upper bound。

但这只是 structural statement，不是 terminal theorem。

### 若表示 assignment count

当前没有支持：

\[
|\operatorname{Assign}(S_{\rm core})|\le4.
\]

应废弃为当前首要目标。

### 改写后的 G1

\[
\boxed{
\textbf{G1'}:
\quad
\kappa_{\rm rec}\le k
\text{，优先尝试 }k=3\text{ 或 }2.
}
\]

这是合理且 presentation-resistant 的目标。

---

## 13.2 G2 — pairwise incompatibility

旧“pairwise relation incompatibility 是否足够”没有规范化意义。

原因：

- 一条大 relation 与另一条 relation 的 pairwise conflict 可以吞掉任意多内部条件；
- 把它们拆开后，同一冲突又会变成 higher-order。

因此 raw pairwise theorem 不应继续追。

真正有意义的是 separator-tree 版本：

\[
\boxed{
\pi_{S_e}(\mathcal J_L)
\cap
\pi_{S_e}(\mathcal J_R)
=
\varnothing.
}
\]

这里的“pairwise”是两个 **canonical compiled blocks** 的 incompatibility，而不是两条任意 relation 的 incompatibility。

当前是否总能把 non-liftability 降成低维 separator 上的 two-block conflict：

\[
\boxed{
\text{OPEN。}
}
\]

Generic separator lemma 说明：**一旦**有 bounded-width canonical separator tree，这种 two-block certificate 自动成立。

---

## 13.3 G3 — uniform small-certificate theorem

旧形式

\[
\Join_jR_j=\varnothing
\Rightarrow
\exists J,
\ |J|\le h_0
\]

应废弃作为 intrinsic theorem。

因为 \(|J|\) 受 relation granularity 控制。

### 改写后的 G3

真正 presentation-invariant 的版本应是：

\[
\boxed{
\textbf{G3'}:
\text{global emptiness 可在一个 bounded-support separator 上，}
\text{由两个 canonical block projections 的不相交证实。}
}
\]

其 certificate size 应记录：

1. separator 的 canonical support dimension；
2. 两侧 canonical block 类型；
3. 必要时一个有限 branch label；

而不是 raw relation 数量。

---

# 14. New backward theorem frontier

本轮不进入任何具体 obstruction theorem。基于 canonical skeleton，下一阶段最多保留三个结构型 target。

## Target CDS-1 — Nontrivial Canonical Separator Theorem

### 目标

在不使用 moving-core 正向信息的前提下，证明 Exact-Lift recovery maps存在一个 genuine factorization，使

\[
\boxed{
\kappa_{\rm rec}\le3
}
\]

最好进一步得到

\[
\boxed{
\kappa_{\rm rec}\le2.
}
\]

### 成功含义

这将首次证明：T3 的四坐标 full overlap 不是 intrinsic，而只是当前 recovery presentation 尚未充分因子化。

### 当前状态

\[
\boxed{
\text{OPEN；最高优先级。}
}
\]

---

## Target CDS-2 — Deterministic-after-Global-Root-and-Denominator Theorem

### 目标

寻找一个真正 global 的 recovery root \(r\) 与最小 denominator summary \(D_{\rm can}\)，证明 completion map

\[
(D_{\rm can},r)
\longmapsto
\mathcal W_{\rm global}
\]

的 fibre：

- 理想地至多一个；或
- 至少有 uniform \(O(1)\) bound；或
- 剩余自由度可分解为互不共享的 recovery blocks。

### 关键纪律

不能把“quadratic 只有两个 roots”当作这个定理的证明。必须证明：

\[
\boxed{
\text{同一个 global root 真正控制 denominator、decimal 与 exact reconstruction。}
}
\]

### 当前状态

\[
\boxed{
\text{OPEN。}
}
\]

---

## Target CDS-3 — Canonical Separator Incompatibility Theorem

### 目标

在 CDS-1 给出的低宽度 separator tree 上，证明所有 global non-liftability 都能被写成：

\[
\boxed{
\pi_S(\mathcal J_L)
\cap
\pi_S(\mathcal J_R)
=\varnothing,
\qquad |S|\le k,
}
\]

其中 \(L,R\) 是 canonical compiled recovery blocks，而不是任意 relation subfamilies。

这会成为旧 G3 “small certificate”真正稳定的替代品。

### 当前状态

抽象 separator lemma 已 **NEW PROVED**；真正的低维 arithmetic separator 仍 **OPEN**。

---

# 15. Proved / heuristic / open ledger

## PROVED — inherited

1. T3 canonical common-denominator reconstruction 是原题候选的双向恢复框架。
2. sphere integerization 与 positive \(t\) recovery。
3. Exact primitive recovery：
   \[
   \gcd(q,y_i)=q/b_i.
   \]
4. gap quadratic、primitive tail quadratic及相应 rational-root divisibility。
5. nondegenerate quadratic 的 rational-root existence 与 integer-square discriminant 等价。
6. denominator-tail certificate：
   \[
   10^\ell\mid\kappa^2(\kappa+2G).
   \]
7. strict-layer 旧报告已经证明：纯 local valuation-position compatibility 不足以完成 global recovery obstruction。

---

## DERIVED FROM PROVED RESULTS

1. 完整候选可由
   \[
   (x_1,x_2,x_3,\Lambda)
   \]
   作为 canonical spine 表示。
2. \(t,d_i,a_i,b_i\)、digit lengths、valuations、Exact-Lift coefficients 均为 deterministic derived data。
3. gap root、tail root、local Hensel branch 等不能自动计作彼此独立的 global candidate freedoms。
4. denominator-tail certificate 是 root / arithmetic / decimal recovery 的交叉投影，不是额外独立 candidate coordinate。

---

## NEW PROVED

1. **Canonical deterministic elimination theorem（当前 proof library 相对版本）**：
   \[
   \mathcal V_{\rm raw}
   \rightsquigarrow
   \mathcal V_{\rm red}
   =\{x_1,x_2,x_3,\Lambda\}.
   \]
2. **Intrinsic-branching clarification**：当前 complete-candidate representation 不需要额外 root / sign / Hensel / Gaussian branch coordinate；这些只在 compressed search fibres 中出现。
3. **Granularity failure of \(h_{\mathfrak R}\)**：raw obstruction order 不是 presentation-invariant object。
4. **Canonical presentation class \(\mathfrak P_{\rm can}\)**：用 recovery-map、no-packing、no-scalarization、projection compilation 规则规范 relation granularity。
5. **Canonical synchronization width \(\kappa_{\rm rec}\)** 的定义。
6. 当前 T3 presentation 有 width \(4\)，故
   \[
   \kappa_{\rm rec}\le4.
   \]
7. **Separator-projection certificate lemma**：在任何合法 separator tree 中，global join emptiness 可递归归结为 local block emptiness 或某 separator 上两侧 feasible projections 不相交。

---

## HEURISTIC

1. 真正可进一步压缩的 separator 很可能由“global algebraic root + canonical denominator summary”组成，而不是四个原始 canonical coordinates全部保留。
2. 当前 root / denominator / decimal gates 的大量表面复杂性，可能主要来自它们对同一少数无界 integers 的不同投影，而非高 intrinsic dimension。
3. \(\kappa_{\rm rec}=2\) 是值得尝试的目标，但现有材料完全不足以宣称它成立。

---

## OPEN

1. \(\kappa_{\rm rec}\) 的内在最小值究竟是 \(4,3,2\) 还是其他值。
2. 是否存在 root-only 或 \((\Lambda,\text{root})\)-type complete separator。
3. 固定一个 global admissible root 后，其余 recovery data 是否 deterministic / uniformly finite。
4. 是否能构造 width \(<4\) 的 canonical separator tree。
5. 是否存在基于 separator projections、而非 relation counts 的 uniform effective obstruction certificate theorem。

---

# 16. Final structural answer

本轮对

\[
\boxed{
\text{Exact-Lift 的 global synchronization 到底有多少真正自由度？}
}
\]

的最严格回答是：

\[
\boxed{
\text{当前 canonical deterministic spine 有四个无界整数坐标：}
(x_1,x_2,x_3,\Lambda).
}
\]

并且：

\[
\boxed{
\text{没有证据需要额外加入独立的 root / Hensel / prime-allocation freedom。}
}
\]

但这四个坐标的 **global ambient assignment domain** 是无界的；现有材料也没有给出 strict completion fibres 的 uniform finite assignment bound。

因此，当前 recovery difficulty 最准确的描述是：

\[
\boxed{
\textbf{few shared unbounded coordinates + many deterministic projections},
}
\]

而不是：

\[
\boxed{
\textbf{many independent witness variables}.
}
\]

所以 Backward Strict Layer 下一阶段不应继续追“有几个 relation 才能冲突”，也不应先追“全局只有几个 candidate states”。

真正值得攻击的是：

\[
\boxed{
\textbf{把 canonical synchronization width 从 4 降到 3 或 2。}
}
\]

这就是本轮得到的

\[
\boxed{
\textbf{Canonical Recovery Dependency Skeleton}.
}
\]
