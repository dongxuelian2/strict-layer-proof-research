# 105-R18 — Post-Corridor μ-Smith Compatibility × Tail-Extra Support × Denominator Window Overlap × Forced-Scale-or-q

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — A1-only  
**Round:** 105-R18  
**Arithmetic:** exact integers / exact rationals only  
**Terminal class:** **SINGLE SHARPER POST-CORRIDOR FIRST-FAILURE GATE (Outcome D, first-failure sense)**

## 1. Executive Verdict

R18 没有证明 post-master transverse shell universally empty，也没有构造第一个 pre-q shell pass 或 z-selector pass。R17 唯一已归档 full-corridor witness 仍在 post-master Gate 1 死亡；R18 的多个 exact targeted construct chambers 没有找到第二条 full-corridor shape，更没有找到 μ-Smith pass。

但本轮取得了三项正式结构增益：

1. **μ 被完全 source-native 化：**
   \[
   \boxed{\mu=\frac{R_M}{m_{\rm src}}}
   \]
   在 full corridor 上是精确恒等式，不是 heuristic。
2. **R15 的旧 \((\Lambda,C_2C_3)\) collision 被严格拆源：** master-forced μ support 与 tail-extra τ support 成为两个 exact first-failure layers。
3. **两个 denominator digit windows 的实交被完全正规化：**
   \[
   \boxed{10^{d-1}<\frac WA<10^{d+1}},\qquad d=m_3-m_2=n_3-n_2+2g+k,
   \]
   且两端严格。

当前没有任何已知/本轮搜索到的 full-corridor shape 穿过 Gate 1，因此 residual q 层没有被合法激活。R19 若继续，只允许攻击：
\[
\boxed{\gcd\!\left(\frac{R_M}{m_{\rm src}},C_2C_3\right)=1}.
\]

这里的 Outcome D 是 **first-failure 意义**：ratio/window theorem 已经建立，但在出现 Gate-1 survivor 前它们不得升级为当前攻击目标。这不宣称 ratio obstruction 已经 universal proved。

## 2. Frozen R1–R17 State

R1–R17 全部冻结。R18 不重开 master complement、post-D excess、5-adic deficit、alignment、DES、carrier image、sphere、PSDG broad packet 或 generic successor。

R17 已正式提供首个 full master corridor pass，并确认旧 master corridor 不是 universal obstruction。

## 3. R17 First Full Master-Corridor Witness

固定回归：
\[
(C_2,C_3,A,W)=(60,13683,1,35),
\]
\[
(P_1,P_2,P_3,Q_0)=(5600,2100,13683,14933),\qquad D=41067.
\]

其
\[
g_0=35,\qquad g_1^*=1120,\qquad 35\mid1120\mid5600.
\]

## 4. Post-Corridor Gate Hierarchy

R18 严格使用：Gate 1 μ-Smith → Gate 2 τ/R1 → Gate 3 τ-Smith → Gate 4 real ratio → Gate 5 integer/forced-scale eligibility → only then residual successor。每条 shape 只按最早 failure 归档。

## 5. Definition of μ, R1, τ, Λ

\[
\mu=\frac{g_1^*}{g_0},\qquad R_1=\frac{P_1}{g_1^*},
\]
\[
\lambda_z=\frac{Y}{(Y,WT_3)},\qquad
\tau=\frac{\lambda_z}{(\lambda_z,\mu)},\qquad
\Lambda=\mu\tau=\operatorname{lcm}(\mu,\lambda_z).
\]
R15 normal form 保持：
\[
z=\mu q,\quad(q,R_1)=1,\qquad q=\tau r,\qquad z=\Lambda r.
\]

## 6. Master-Forced Scale / Smith Theorem

在冻结 shape-level Smith 条件 \((A,C_2)=1,(W,C_3)=1\) 后，z-dependent Smith 恰为
\[
(z,C_2C_3)=1.
\]
master shell 强制 \(\mu\mid z\)。因此
\[
\boxed{(\mu,C_2C_3)=1}
\]
是 master-forced factor 与 Smith 的**完整 compatibility condition**：若 gcd>1，则任何 residual q 都不能修复；若 gcd=1，则 master-forced factor 自身不再造成 Smith collision，剩余只由 q/tail support 决定。

正式签：
```text
MASTER_FORCED_SCALE_SMITH_COMPATIBILITY_THEOREM=PROVED
```

## 7. Source Formula for μ

令
\[
d_M=(N_M,P_1),\qquad E_M=N_M/d_M,\qquad R_M=d_M/g_0.
\]
R16 post-D lower pass 写成
\[
\Omega=E_Mm_{\rm src}.
\]
于是
\[
g_1^*=\frac{N_M}{\Omega}
=\frac{d_ME_M}{E_Mm_{\rm src}}
=\frac{d_M}{m_{\rm src}}.
\]
再除以 \(g_0\)：
\[
\boxed{\mu=\frac{R_M}{m_{\rm src}}}.
\]
full upper corridor 正好保证 \(m_{\rm src}\mid R_M\)。

## 8. (R_M/m_src) Reduction

进一步，写
\[
P_1=hp,\quad L=u_0AWXYG,\quad s=(L,p),
\]
R16 有
\[
d_M=hs,\qquad R_M=\frac{hs}{g_0}.
\]
故
\[
\boxed{\mu=\frac{h(L,P_1/h)}{g_0m_{\rm src}}}.
\]
primewise：
\[
v_\ell(\mu)=v_\ell(R_M)-v_\ell(m_{\rm src})\ge0.
\]
这就是 absorbed-content residual divisor。

## 9. Master/Smith Prime-Support Atlas

对首 witness：
\[
R_M=160=2^5\cdot5,\qquad m_{\rm src}=5,
\]
故
\[
\mu=32=2^5.
\]
而
\[
C_2=60=2^2\cdot3\cdot5,\qquad C_3=13683=3\cdot4561.
\]
唯一 μ-support prime 是 2，并与 C2 的 \(2^2\) 发生 collision。

## 10. First Witness μ-Smith Autopsy

本 witness 的 source chain 为
\[
h=1,\quad L=35,000,000,\quad s=(L,5600)=5600,
\]
\[
d_M=5600,\quad g_0=35,\quad R_M=160,
\]
\[
E_{\rm src}=6250,\quad \Omega_D=31250,\quad m_{\rm src}=5.
\]
所以 m_src 只吸收一个 5，不吸收任何 2；R_M 中的 \(2^5\) 全部留到 μ。于是
\[
\boxed{(\mu,C_2C_3)=(32,60\cdot13683)=4}.
\]
这解释了“哪部分 source content 强制这两个 2 进入 μ”：它们来自 \(R_M/m_{\rm src}\) 的未吸收 2-adic residual，而不是 tail。

## 11. μ=1 Construct Route

\[
\mu=1\iff g_1^*=g_0\iff m_{\rm src}=R_M.
\]
这是 Gate 1 最廉价 regime。R18 的 targeted chambers 中没有找到 μ=1 full-corridor shape。此为 finite no-hit，不作 theorem。

## 12. Tail Excess Scale

正式命名：
\[
\boxed{\tau=\lambda_z/(\lambda_z,\mu)}
\]
为 **Tail Excess Scale**：它是 tail 在 master 已强制 μ 之外仍要求进入 q 的 prime-power content。

## 13. Tail/(g1) Residual Compatibility

由 \(q=\tau r\) 与 \((q,R_1)=1\)：
\[
(\tau r,R_1)=1
\iff
(\tau,R_1)=1\ \text{and}\ (r,R_1)=1.
\]
故 Gate 2 是 exact compatibility；通过后没有隐藏的 tail/g1 residual collision。

```text
TAIL_EXCESS_G1_RESIDUAL_COMPATIBILITY_THEOREM=PROVED
```

## 14. Tail/Smith Compatibility

Gate 1 通过后，Smith 为
\[
(\mu\tau r,C_2C_3)=1.
\]
因此 Gate 3 exact 为
\[
\boxed{(\tau,C_2C_3)=1},
\]
通过后 residual 只需 \((r,C_2C_3)=1\)。

注意一个重要校正：Gates 1–3 **不推出** \((\Lambda,R_1C_2C_3)=1\)。精确结论是
\[
(\Lambda,C_2C_3)=1,\qquad(\tau,R_1)=1.
\]
μ 与 R1 可以共享素数；R15 的 shell 本来只禁止 residual q 与 R1 共享素数。

## 15. Λ-Collision Decomposition

因为 \(\operatorname{supp}\Lambda=\operatorname{supp}\mu\cup\operatorname{supp}\tau\)，
\[
\boxed{(\Lambda,C_2C_3)>1}
\iff
\boxed{(\mu,C_2C_3)>1\ \text{or}\ (\tau,C_2C_3)>1}.
\]
旧 R15 collision 因此完成 first-failure attribution。

## 16. Raw Denominator Windows

\[
I_A=\left[\frac{10^{m_2-1}}A,\frac{10^{m_2}}A\right),\qquad
I_W=\left[\frac{10^{m_3-1}}W,\frac{10^{m_3}}W\right).
\]
先研究实交，完全不使用 integrality、μ、τ、Λ 或 coprimality。

## 17. Exact Real-Overlap Criterion

两个 half-open interval 相交 iff
\[
\frac{10^{m_2-1}}A<\frac{10^{m_3}}W
\quad\text{and}\quad
\frac{10^{m_3-1}}W<\frac{10^{m_2}}A.
\]
令 \(d=m_3-m_2\)，整理为
\[
\boxed{10^{d-1}<\frac WA<10^{d+1}}.
\]
两端必须严格：若等号成立，只发生在一个 interval 的 open upper endpoint 与另一个 lower endpoint 接触，交集仍为空。

本轮 exact small regression 共检查 3249 组 \((A,W,m_2,m_3)\)，与直接 Fraction interval 判定完全一致。

## 18. (W/A) Ratio Corridor

定义
\[
\boxed{\mathscr R_d=(10^{d-1},10^{d+1})}.
\]
称为 **Denominator Shape Ratio Corridor**。这是 finite-shape gate，与 z 的整数选择无关。

## 19. (m3-m2) Source Formula

A1 frozen exponent normal form：
\[
g=m_3-n_3,\qquad n_2=m_2+g+k.
\]
故
\[
m_2=n_2-g-k,\qquad m_3=n_3+g,
\]
\[
\boxed{d=m_3-m_2=n_3-n_2+2g+k}.
\]
所以 d 由 source digit counts 与 A1 exponent chart 决定，不是自由 decimal index。

## 20. First Witness Ratio Autopsy

首 witness：
\[
(m_2,m_3)=(1,5),\quad d=4,\quad W/A=35.
\]
ratio corridor 是
\[
\mathscr R_4=(10^3,10^5)=(1000,100000),
\]
而 \(35<1000\)。因此它在实数层就死。

更直接：
\[
I_A=[1,10),\qquad I_W=[10000/35,100000/35)=[2000/7,20000/7),
\]
显然 disjoint。

## 21. Real vs Integer Window Gap

令
\[
L_z=\max(I_A^-,I_W^-),\qquad U_z=\min(I_A^+,I_W^+).
\]
实交 iff \(L_z<U_z\)。整数交 iff
\[
\boxed{\lceil L_z\rceil\le\lceil U_z\rceil-1}.
\]
等价于 R15 的 exact \(Z_-\le Z_+\)。若 \(U_z-L_z\ge1\)，整数交自动存在；若长度在 \((0,1)\) 内，则需要 fractional endpoint positioning。

## 22. Integer z-Window

\[
Z_-=\max\left(\left\lceil\frac{10^{m_2-1}}A\right\rceil,\left\lceil\frac{10^{m_3-1}}W\right\rceil\right),
\]
\[
Z_+=\min\left(\left\lfloor\frac{10^{m_2}-1}A\right\rfloor,\left\lfloor\frac{10^{m_3}-1}W\right\rfloor\right).
\]
首 witness：\(Z_-=286,Z_+=9\)。本轮 exact integer-window regression 共检查 3249 组小参数，与 brute integer membership 完全一致。

## 23. Window Length Audit

定义
\[
\ell_z=U_z-L_z.
\]
首 witness：
\[
L_z=2000/7,\quad U_z=10,\quad \ell_z=-1930/7<0.
\]
所以不是“短 interval 错过整数”，而是实 interval 根本不相交。

## 24. Forced-Scale Fit

所有 legal z 都满足 \(z=\Lambda r,r\ge1\)。因此
\[
\Lambda>Z_+\Rightarrow\text{dead}.
\]
反之 \(\Lambda<Z_-\) 不构成 failure，只把 residual lower bound 推到
\[
R_-=\left\lceil Z_-/\Lambda\right\rceil.
\]
首 witness 诊断上还有 \(32>9\) 的 forced-scale overflow，但 first-failure 已经在 Gate 1。

## 25. z=Λ Construct Route

最便宜 candidate \(r=1\) 要求
\[
Z_-\le\Lambda\le Z_+.
\]
且必须先通过 Gates 1–3。R18 没有找到进入此 route 的 full-corridor shape。

## 26. Full-Corridor Shape Registry

R17 archive 中 full-corridor registry 只有首 witness。R18 所有新 exact construct chamber 均未产生第二条 full-corridor shape。详见 `105_R18_Full_Corridor_Shapes.csv` 与 `105_R18_Deep_Construct_Search.csv`。

## 27. Post-Corridor First-Failure Attribution

首 witness 的 ordered attribution：
```text
Gate 0 FULL MASTER CORRIDOR = PASS
Gate 1 MU-SMITH             = FAIL (gcd=4)
```
Gate 2/3、ratio、integer、overflow 只作 diagnostic，不改变 first failure。

## 28. Targeted Deep-Pass Construct Search

R18 进行了四组 exact finite discovery scans：

- **S1:** standard primitive Pythagorean-quadruple orientation，\(p\le80\)，访问 27,007,472 个 D-positive parameter triples；固定 n2=2 chart，A≤9，并对每个 \(g_1^*\mid P_1\) 反解唯一 W。full corridor 仅 1 条，即 R17 witness。
- **S2:** 六个 coordinate permutations，\(p\le50,m\le200,n\le100\)，423,770 个 primitive parameter triples；full corridor 仍仅 1 条。
- **S3:** standard orientation 的 general A1 chart local scan；full corridor 仍仅 R17 witness。
- **S4:** 把 odd Pythagorean leg 指派给 P1，专门寻找 odd-μ route；未找到 full corridor pass。

所有搜索只作 construct/discovery evidence；**finite no-hit 不冒充 universal theorem**。

## 29. First μ-Smith Pass

```text
FIRST_MU_SMITH_PASS=NO
```
当前已知 full-corridor locus 上没有 \((\mu,C_2C_3)=1\) witness。未证明 universal obstruction。

## 30. First Gate-1–3 Pass

不存在，因为尚无 Gate-1 survivor。

## 31. First Real-Window Pass

在 full-corridor survivors 中不存在；唯一 survivor 的 ratio 失败。此为当前 registry/targeted-search 结论，不是 universal theorem。

## 32. First Integer-Window Pass

不存在于 full-corridor survivors。

## 33. First Pre-q Shell Pass

```text
FIRST_POST_MASTER_PREQ_SHELL_PASS=NO
```
没有 shape 有资格激活 residual q。

## 34. Residual q-Selector

未激活。定义保留：
\[
R_-=\lceil Z_-/\Lambda\rceil,\quad R_+=\lfloor Z_+/\Lambda\rfloor,
\]
\[
F=\operatorname{rad}(R_1C_2C_3),\qquad
r_{\min}=\min\{r\ge R_-:(r,F)=1\}.
\]
但 R18 不计算 generic successor，也不调用 Jacobsthal。

## 35. First z-Selector Pass

不存在；`105_R18_Z_Selector_Passes.csv` 只保存 no-pass certificate。

## 36. Smith Reconstruction

未到达。不存在 z，因此不启动 canonical Smith reconstruction。

## 37. Full Post-PSDG Reconstruction

未到达。

## 38. Exact Plain U

未到达。

## 39. Source Selector

未到达。

## 40. Downstream Digit/Cut/Word

未到达；digit synchronization / actual cut / full word / outer completion 均冻结。

## 41. Deepest Post-Corridor Pass

\[
\boxed{\text{DEPTH}_0=\text{FULL MASTER CORRIDOR}}
\]
是当前 deepest pass。尚无 DEPTH_1 μ-Smith pass。

## 42. Architecture Saturation Audit

`POST_MASTER_Z_SHELL_SOURCE_INTERFACE_SATURATED=NO`。原因：当前甚至尚未穿过 μ-Smith support，问题没有退化为 generic residual coprime interval；因此不存在触发 generic-successor saturation 的条件。

## 43. Information-Gain Certificate

R18 的信息增益不是“又搜索了一盒”：

1. 证明 \(\mu=R_M/m_{\rm src}\)；
2. 将 master-forced support 从旧 Λ-collision 中拆出并 source-native 化；
3. 证明 tail excess 的两个 exact compatibility theorem；
4. 证明 denominator real-overlap 的 exact open ratio corridor；
5. 将 \(d\) 写成 \(n_3-n_2+2g+k\)；
6. 精确分离 real overlap / integer overlap / forced scale fit / residual successor；
7. 大规模 construct campaign 没有找到 Gate-1 survivor，因此当前 first-failure 被稳定锁到 absorbed-content residual Smith support。

## 44. New First-Failure Gate

\[
\boxed{\textbf{ABSORBED-CONTENT RESIDUAL SMITH SUPPORT}}
\]
即
\[
\boxed{\gcd\!\left(\frac{R_M}{m_{\rm src}},C_2C_3\right)=1}.
\]
R19 只能证明它 universal fail，或构造第一个 pass。不得越级到 ratio 或 q。

## 45. R18 Terminal Verdict

```text
R18_TERMINAL_VERDICT=R18_REDUCED_TO_SINGLE_POST_CORRIDOR_SHELL_GATE

R1_TO_R17_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=ABSORBED_CONTENT_RESIDUAL_SMITH_SUPPORT

FULL_MASTER_CORRIDOR_PRECONDITION=PASS_ON_R17_WITNESS

G0=35
G1_STAR=1120
P1=5600
MU=32
R1_RESIDUAL=5

MU_SOURCE_FORM=MU=R_M/M_SRC=H*GCD(L,P1/H)/(G0*M_SRC)
MU_EQUALS_RM_OVER_MSRC=YES

C2=60
C3=13683

MASTER_SMITH_SUPPORT_GCD=4
MASTER_SMITH_SUPPORT_PASS=NO

LAMBDA_Z=16
TAU=1

TAIL_G1_SUPPORT_GCD=1
TAIL_G1_SUPPORT_PASS=YES_DIAGNOSTIC_NOT_REACHED_BY_FIRST_FAILURE_ORDER

TAIL_SMITH_SUPPORT_GCD=1
TAIL_SMITH_SUPPORT_PASS=YES_DIAGNOSTIC_NOT_REACHED_BY_FIRST_FAILURE_ORDER

LAMBDA=32

M2_EXPONENT=1
M3_EXPONENT=5
DENOMINATOR_EXPONENT_DIFFERENCE=4

AW_RATIO=35/1
REAL_RATIO_CORRIDOR=(1000,100000)
REAL_WINDOW_OVERLAP=NO

Z_LOWER=286
Z_UPPER=9
INTEGER_WINDOW_OVERLAP=NO

FORCED_SCALE_FIT=NO_DIAGNOSTIC_LAMBDA_GT_ZUPPER

RESIDUAL_LOWER=NOT_ACTIVATED
RESIDUAL_UPPER=NOT_ACTIVATED
FORBIDDEN_FACTOR=NOT_ACTIVATED
RESIDUAL_SUCCESSOR=NOT_ACTIVATED

FIRST_POST_MASTER_PREQ_SHELL_PASS=NO
PREQ_PASS_SHAPE=NONE

Z_SELECTOR_PASS=NO
Z_SELECTOR_SHAPE=NONE
Z=NONE

FULL_SMITH_RECONSTRUCTION=NOT_REACHED
FULL_POST_PSDG_LIFT=NO
FULL_LIFT_DATA=NONE

PLAIN_U=NOT_REACHED
SOURCE_SELECTOR_PASS=NOT_REACHED
SOURCE_INTEGER_U_FOUND=NO

COMMON_U_INTEGER_SUCCESSOR_GATE=NOT_REACHED

DIGIT_SYNCHRONIZATION=NOT_REACHED
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

MASTER_FORCED_SCALE_SMITH_OBSTRUCTION=NOT_PROVED_UNIVERSALLY
DENOMINATOR_RATIO_CORRIDOR_OBSTRUCTION=NOT_PROVED_UNIVERSALLY
POST_MASTER_TRANSVERSE_SHELL_UNLIFTABILITY_PROVED=NO

POSITIVE_RADIAL_CORE_UNLIFTABILITY_PROVED=NO
POST_PSDG_SOURCE_RADIAL_FIBRE_EMPTY=NO

POST_MASTER_Z_SHELL_SOURCE_INTERFACE_SATURATED=NO

DEEPEST_POST_CORRIDOR_PASS=DEPTH_0_FULL_MASTER_CORRIDOR

R18_SINGLE_POST_CORRIDOR_SHELL_GATE=YES__GCD(R_M/M_SRC,C2*C3)=1

NEW_FIRST_FAILURE_GATE=ABSORBED_CONTENT_RESIDUAL_SMITH_SUPPORT_ON_FULL_MASTER_CORRIDOR_LOCUS

R18_INFORMATION_GAIN_CERTIFICATE=MU_SOURCE_IDENTITY_PLUS_SUPPORT_DECOMPOSITION_PLUS_EXACT_RATIO_CORRIDOR_PLUS_TARGETED_NO_GATE1_HIT

R19_AUTHORIZED=YES
R19_ARCHITECTURE=ABSORBED_CONTENT RESIDUAL SUPPORT ONLY
R19_SINGLE_ATTACK_TARGET=PROVE_UNIVERSAL_MU_SMITH_COLLISION_OR_CONSTRUCT_FIRST_MU_SMITH_PASS
```

## 46. R19 Authorization Decision

R19 按 Route B 授权，但只允许：
\[
\gcd(R_M/m_{\rm src},C_2C_3)=1.
\]

若 R19 构造第一个 pass，才重新激活 τ-support 与 denominator ratio；若 R19 证明 universal collision，则 post-master shell 直接 extinction。不得在 R19 提前研究 residual q/Jacobsthal。
