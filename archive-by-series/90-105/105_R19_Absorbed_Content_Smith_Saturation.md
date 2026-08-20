# 105-R19 — Absorbed-Content Saturation × Radial Smith Support × Prime-Power Defect × First μ-Smith Pass-or-Universal Collision

**Project:** 三项十进制拼接平方和问题  
**Layer:** Strict Layer — A1-only  
**Round:** 105-R19  
**Arithmetic:** exact integers / exact valuations only  
**Terminal class:** **Outcome C — single source-defined Face-2 decimal-primary absorption-defect gate**

## 1. Executive Verdict

R19 没有证明 universal μ-Smith obstruction，也没有找到第一次 μ-Smith pass。它完成了更尖锐、且满足 R19 Outcome C 的 reduction：

\[
\boxed{
\text{所有未决 radial Smith failure 只可能来自 }
\ell\in\{2,5\},\ \ell\mid C_2,\ \ell\mid P_1.
}
\]

其余 radial support 全部已经 theoremically 决定：

- shared primes \(\ell\mid(C_2,C_3)\) 自动安全；
- 所有 \(\ell\notin\{2,5\}\) 的 Face-2/Face-3 radial primes 自动安全；
- Face-3 的 \(2/5\) support 完全分类：若 \(\ell\mid P_1\) 则必有 defect，若 \(\ell\nmid P_1\) 则因 \(\mu\mid P_1\) 自动安全。

因此唯一 remaining gate 是：

\[
\boxed{
\ell\in\{2,5\},\quad \ell\mid C_2,\quad \ell\mid P_1,
\qquad
v_\ell(\Omega)=e_10+v_\ell(W)-\min(v_\ell(W),v_\ell(P_1)),
}
\tag{R19-F2-DEC}
\]

其中
\[
e_{10}:=v_\ell(XYG)=m_2+n_3+g
\]
对 \(\ell=2,5\) 相同。

构造侧找到第二条 genuine full-master-corridor shape，但仍在 μ-Smith 失败：
\[
(C_2,C_3,A,W)=(310,71549,1,60),
\]
\[
(P_1,P_2,P_3,Q_0)=(54000,18600,71549,91549),
\]
\[
R_M=100,\quad m_{\rm src}=2,\quad \mu=50,\quad \Delta_{\rm rad}=50.
\]

当前最小已知 \(\Delta_{\rm rad}\) 仍是 R17 witness 的 32；没有 \(\Delta_{\rm rad}=1\) hit。

## 2. Frozen R1–R18 State

R1–R18 全部冻结。R19 没有重开 master complement、post-D source excess、alignment、DES、carrier image、sphere、PSDG、tail、denominator window 或 residual q。R17 已证明 master corridor 可穿；R18 已把 current first-failure 精确锁定为 \(\gcd(\mu,C_2C_3)=1\)。

## 3. R18 Single-Gate Reduction

full corridor 上：
\[
\boxed{\mu=R_M/m_{\rm src}}.
\]
因此 Smith Gate 1 是：
\[
\boxed{\gcd(R_M/m_{\rm src},C_2C_3)=1}.
\]

## 4. Definition of \(R_M,m_{\rm src},\mu\)

写
\[
P_1=hp,\qquad D=h\delta,\qquad L=u_0AWXYG,
\]
其中 \(h=(P_1,Q_0)\)。由
\[
\delta=Kp-Q_0/h
\]
及 \((p,Q_0/h)=1\)，得到
\[
\boxed{(p,\delta)=1}.
\]
又
\[
N_M=LD=Lh\delta.
\]
令 \(s=(L,p)\)。则
\[
(N_M,P_1)=h(L\delta,p)=h(L,p)=hs.
\]
因此 canonical form 为
\[
\boxed{R_M=\frac{h(L,p)}{g_0}},\qquad g_0=(u_0AW,P_1).
\tag{RM}
\]
这严格证明了 prompt 中两个 \(R_M\) expression 的 equivalence；这里只把 gcd-definition 视为原始定义，把上式作为 theorem。

## 5. Proof of \(\mu=R_M/m_{\rm src}\)

\[
E_{\rm src}=\frac L{(L,p)},\qquad \Omega_D=\frac\Omega\delta,
\]
lower corridor 给
\[
m_{\rm src}=\frac{\Omega_D}{E_{\rm src}}.
\]
同时
\[
E_M=\frac{N_M}{(N_M,P_1)}
=\delta E_{\rm src},
\qquad
\Omega=E_Mm_{\rm src}.
\]
故
\[
g_1^*=\frac{N_M}\Omega
=\frac{(N_M,P_1)}{m_{\rm src}},
\]
从而
\[
\boxed{
\mu=\frac{g_1^*}{g_0}
=\frac{R_M}{m_{\rm src}}.
}
\]

## 6. Source-native formula for \(m_{\rm src}\)

R19 去掉 quotient nesting：
\[
\boxed{
m_{\rm src}
=\frac{\Omega (N_M,P_1)}{N_M}
=\frac{(N_M,P_1)}{g_1^*}.
}
\tag{MSRC-NATIVE}
\]
这不再显式出现 \(E_{\rm src}\)。

## 7. Direct formula for \(\mu\)

把 \(m_{\rm src}=\Omega_D(L,p)/L\) 代回：
\[
\boxed{
\mu
=\frac{hL}{g_0\Omega_D}
=\frac{LD}{g_0\Omega}
=\frac{N_M}{g_0\Omega}.
}
\tag{MU-DIRECT}
\]
所以 prompt Task C 的 candidate formula **exactly true**。

## 8. Radial Support Definition

\[
\mathcal P_{\rm rad}=\operatorname{supp}(C_2C_3),\quad
\mathcal P_2=\operatorname{supp}(C_2),\quad
\mathcal P_3=\operatorname{supp}(C_3).
\]

## 9. Absorbed-Content Smith Saturation Theorem

full corridor 已有 \(m_{\rm src}\mid R_M\)。定义
\[
\delta_\ell=v_\ell(R_M)-v_\ell(m_{\rm src})=v_\ell(\mu)\ge0.
\]
于是：
\[
\boxed{
(\mu,C_2C_3)=1
\iff
v_\ell(m_{\rm src})=v_\ell(R_M)
\quad\forall\ell\mid C_2C_3.
}
\tag{ABS-SAT}
\]
正式签：
```text
ABSORBED_CONTENT_SMITH_SATURATION_THEOREM_PROVED=YES
```

## 10. Primewise Defect \(\delta_\ell\)

令
\[
a=v_\ell(L),\qquad b=v_\ell(p).
\]
则
\[
v_\ell(R_M)=v_\ell(h)+\min(a,b)-v_\ell(g_0),
\]
\[
v_\ell(E_{\rm src})=\max(a-b,0),
\]
\[
v_\ell(m_{\rm src})=v_\ell(\Omega_D)-\max(a-b,0).
\]

## 11. Closed Defect Formula

用恒等式 \(\min(a,b)+\max(a-b,0)=a\)：
\[
\boxed{
\delta_\ell
=v_\ell(h)+v_\ell(L)-v_\ell(g_0)-v_\ell(\Omega_D).
}
\]
再用 \(D=h\delta\)、\(\Omega=\delta\Omega_D\)：
\[
\boxed{
\delta_\ell
=v_\ell(D)+v_\ell(L)-v_\ell(g_0)-v_\ell(\Omega)
=v_\ell(N_M/g_0)-v_\ell(\Omega).
}
\tag{DEF-CLOSED}
\]
这是 R19 最短 local normal form。

## 12. Radial Supported Parts

\[
R_M^{\rm rad}=\prod_{\ell\mid C_2C_3}\ell^{v_\ell(R_M)},
\qquad
m_{\rm src}^{\rm rad}=\prod_{\ell\mid C_2C_3}\ell^{v_\ell(m_{\rm src})}.
\]
则
\[
\boxed{
\mu\text{-Smith pass}
\iff R_M^{\rm rad}=m_{\rm src}^{\rm rad}
\iff R_M^{\rm rad}\mid m_{\rm src}.
}
\]

## 13. Radial Absorption Defect \(\Delta_{\rm rad}\)

\[
\boxed{
\Delta_{\rm rad}
=\frac{R_M^{\rm rad}}{\gcd(R_M^{\rm rad},m_{\rm src})}
=\prod_{\ell\mid C_2C_3}\ell^{\delta_\ell}
=\mu^{\rm rad}.
}
\]
因此 pass iff \(\Delta_{\rm rad}=1\)。

## 14. Radial Valuation Budget Theorem

因为
\[
m_{\rm src}=\frac\Omega{(D/h)E_{\rm src}},
\]
所以 saturation 等价于
\[
v_\ell(\Omega)
=v_\ell(D/h)+v_\ell(E_{\rm src})+v_\ell(R_M).
\]
定义右侧为 \(B_\ell\)。R19 进一步证明：
\[
\boxed{
B_\ell=v_\ell(D)+v_\ell(L)-v_\ell(g_0)=v_\ell(N_M/g_0).
}
\tag{BUDGET}
\]
而 upper corridor \(\Omega\mid N_M/g_0\)，故必有
\[
v_\ell(\Omega)\le B_\ell.
\]
因此 equality 而不是 merely \(\ge\)；并且
\[
\boxed{\delta_\ell=B_\ell-v_\ell(\Omega)}.
\]
正式签：
```text
RADIAL_ABSORPTION_VALUATION_BUDGET_THEOREM=PROVED
```

## 15. R17 Witness Exact Autopsy

R17 witness：
\[
(C_2,C_3)=(60,13683),\quad R_M=160,\quad m_{\rm src}=5,\quad\mu=32.
\]
其
\[
L=35,000,000=2^6 5^7\cdot7,
\quad
p=5600=2^5 5^2\cdot7.
\]
所以 \((L,p)\) 含完整 \(2^5\)，这五层全部进入 \(R_M\)。

另一方面
\[
E_{\rm src}=6250=2\cdot5^5,
\qquad
\Omega_D=31250=2\cdot5^6.
\]
在 \(\ell=2\)：
\[
v_2(D/h)=0,
\quad v_2(E_{\rm src})=1,
\quad v_2(R_M)=5,
\]
所以
\[
B_2=0+1+5=6.
\]
但
\[
v_2(\Omega)=1.
\]
因此
\[
\boxed{\delta_2=6-1=5}.
\]
这精确解释了为什么 full master absorption “一层 2 都没留给 \(m_{\rm src}\)”：\(\Omega_D\) 唯一的 \(2\)-层已经全部支付给 \(E_{\rm src}\)，而 \(R_M\) 还要求额外五层 saturation。

在 \(5\) 上则
\[
v_5(\Omega)=6=B_5,
\]
故 \(\delta_5=0\)。这同时严格否定“Face-2 的 5-adic radial support 必然 fail”。

R17：
\[
R_M^{\rm rad}=160,\quad m_{\rm src}^{\rm rad}=5,
\quad\boxed{\Delta_{\rm rad}=32}.
\]

## 16. Face-2 Radial Support — nondecimal theorem

**Theorem.** 若 \(\ell\notin\{2,5\}\)、\(\ell\mid C_2\)，则 full corridor 上 \(v_\ell(\mu)=0\)。

反设 \(\ell\mid\mu\)。因为 \(g_1^*=g_0\mu\mid P_1\)，有 \(\ell\mid P_1\)。又 \(\ell\mid C_2\Rightarrow\ell\mid P_2\)。primitivity 迫使 \(\ell\nmid u_0,P_3,Q_0\)；\((A,C_2)=1\) 给 \(\ell\nmid A\)；\(\ell\nmid10\) 给 \(\ell\nmid XYG\)；而
\[
D=KP_1-Q_0\not\equiv0\pmod\ell.
\]
故 \(N_M\) 的全部 \(\ell\)-content 只能来自 \(W\)。令
\[
a=v_\ell(W),\qquad b=v_\ell(P_1).
\]
则 \(v_\ell(g_0)=\min(a,b)\)。一方面从 \(\mu=N_M/(g_0\Omega)\)：
\[
v_\ell(\mu)\le a-\min(a,b).
\]
另一方面从 \(g_0\mu=g_1^*\mid P_1\)：
\[
v_\ell(\mu)\le b-\min(a,b).
\]
若 \(a\le b\)，第一上界为 0；若 \(a>b\)，第二上界为 0。故总有 \(v_\ell(\mu)=0\)，矛盾。

## 17. Face-3 Radial Support — nondecimal theorem

完全类似。若 \(\ell\notin\{2,5\}\)、\(\ell\mid C_3\) 且 \(\ell\mid\mu\)，primitivity 与 \((W,C_3)=1\) 迫使除 \(A\) 外的 \(N_M\) factors 全部是 \(\ell\)-units。令 \(a=v_\ell(A),b=v_\ell(P_1)\)，同一对 min-bound 强迫 \(v_\ell(\mu)=0\)。

因此：
\[
\boxed{
\operatorname{supp}(\mu)\cap\operatorname{supp}(C_2C_3)
\subseteq\{2,5\}.
}
\tag{DECIMAL-PRIMARY}
\]

## 18. Shared Radial Support

若 \(\ell\mid C_2\) 且 \(\ell\mid C_3\)，再假设 \(\ell\mid\mu\)，则 \(\ell\mid P_1,P_2,P_3\)，sphere 强迫 \(\ell\mid Q_0\)，直接违反 primitive sphere。故
\[
\boxed{\ell\mid(C_2,C_3)\Longrightarrow\delta_\ell=0}
\]
对包括 \(2,5\) 在内的所有 primes 成立。

## 19. 2-adic Radial Support

2-adic 不再是 broad atlas。R19 已将其全部 unresolved content 压到：
\[
2\mid C_2,\quad2\mid P_1,
\]
且要求 Face-2 budget equality (R19-F2-DEC)。

若 \(2\mid C_3\)：见 §21，已完全分类。若 \(2\nmid P_1\)：因 \(\mu\mid P_1\) 自动安全。

R17 witness 处于 live Face-2 class，并有 \(\delta_2=5\)。第二 full-corridor shape 也处于 live Face-2 class，并有 \(\delta_2=1\)。

## 20. 5-adic Radial Support

同样只剩 Face-2 decimal-primary class。R17 witness 在该 class 上达到 exact saturation \(\delta_5=0\)，因此 general 5-adic radial obstruction 已被 falsify。第二 full-corridor shape 有 \(\delta_5=2\)，说明 Face-2 5-support 既能 pass primewise，也能 fail primewise；真正对象只能是 exact budget equality，而不是 parity-style slogan。

## 21. Face-3 Decimal-Primary Theorem

取 \(\ell\in\{2,5\}\)、\(\ell\mid C_3\)。

若 \(\ell\nmid P_1\)，因为 \(\mu\mid P_1\)，立即有 \(v_\ell(\mu)=0\)。

若 \(\ell\mid P_1\)，则 \(\ell\mid P_3\)。primitivity 迫使 \(P_2,Q_0,u_0,W\) 都是 \(\ell\)-units。又 \(Y=10^{n_3}\) 含 \(\ell\)，故
\[
\Omega=W(Q_0-P_3)+AY(GQ_0-P_2)
\equiv WQ_0\not\equiv0\pmod\ell.
\]
所以
\[
v_\ell(\Omega)=0.
\]
同时 \(D=KP_1-Q_0\) 是 unit，而 \(XYG\) 自带
\[
e_{10}=m_2+n_3+g\ge2
\]
层 decimal content。因此 budget \(B_\ell>0\)，从而
\[
\boxed{\delta_\ell>0}.
\]
于是 exact classification：
\[
\boxed{
\ell\in\{2,5\},\ \ell\mid C_3:
\quad
\delta_\ell>0\iff \ell\mid P_1.
}
\tag{F3-DEC}
\]

## 22. \(\Omega\) mod Radial Prime Reduction

用
\[
M_r=u_0C_2,\quad N_r=u_0C_3,
\]
\[
\Omega=Q_0(W+AYG)-AW(N_r+YM_r).
\]
若 \(\ell^e\mid C_2\)：
\[
\boxed{
\Omega\equiv W(Q_0-P_3)+AYGQ_0\pmod{\ell^e}.
}
\]
若 \(\ell^e\mid C_3\)：
\[
\boxed{
\Omega\equiv WQ_0+AY(GQ_0-P_2)\pmod{\ell^e}.
}
\]
若 shared，则两 radial terms同时消失。

## 23. \((D/h)\) Radial Overlap

一般 budget 已精确扣除
\[
v_\ell(D/h).
\]
在唯一 live Face-2 decimal class \(\ell\in\{2,5\},\ell\mid C_2,\ell\mid P_1\) 中，primitivity 给 \(Q_0\) unit，而 \(K P_1\equiv0\pmod\ell\)，故
\[
\boxed{v_\ell(D)=0}.
\]
所以此 live gate 中 \((D/h)\) 不再消耗 decimal-primary budget；真正竞争发生在 \(\Omega\) 自身。

## 24. \(E_{\rm src}\) Radial Overlap

一般：
\[
v_\ell(E_{\rm src})=\max(v_\ell(L)-v_\ell(p),0).
\]
R17 的 2-adic autopsy 正是 \(E_{\rm src}\) 先消费一层 2，留下 \(m_{\rm src}\) 的 2-content 为 0。

## 25. Full Absorption Budget

一般：
\[
B_\ell=v_\ell(D/h)+v_\ell(E_{\rm src})+v_\ell(R_M)=v_\ell(N_M/g_0).
\]
在 live Face-2 decimal class，\(u_0,A,D\) 都是 \(\ell\)-units，令
\[
e_{10}=m_2+n_3+g,
\]
则
\[
\boxed{
B_\ell=e_{10}+v_\ell(W)-\min(v_\ell(W),v_\ell(P_1)).
}
\tag{F2-BUDGET}
\]
当前唯一 remaining question 就是 \(v_\ell(\Omega)=B_\ell\) 是否发生。

## 26. Full-Corridor Registry

R19 registry 现在有两条 exact shapes：R17 witness 与 R19 新发现 shape。详见 `105_R19_Full_Corridor_Registry.csv`。

## 27. \(\Delta_{\rm rad}\) Construct Objective

R17：32。R19 第二 shape：50。当前
\[
\boxed{\min\Delta_{\rm rad}=32}.
\]
没有找到 \(<32\) 的 full-corridor shape。

## 28. \(R_M^{\rm rad}=1\) Search

没有 hit。finite no-hit，不作 theorem。

## 29. \(\mu=1\) Search

没有 full-corridor \(\mu=1\) shape。finite no-hit，不作 theorem。

## 30. Odd/Ten-Unit Support Construct Search

由 DECIMAL-PRIMARY theorem，若
\[
(C_2C_3,10)=1,
\]
则 μ-Smith 自动 pass。R19 因而专门运行 standard + all-permutation ten-unit radial searches；在已执行的 exact finite scopes内没有 full corridor hit。此只作 discovery evidence，不作 emptiness theorem。

## 31. Alignment-Based Construct Family

未重新研究 alignment obstruction。R19 保持 alignment 退休，只允许其作为潜在 construct family；本轮没有新增 alignment family theorem。

## 32. Reverse-\(\mu\) Construct Attempt

R19 不 arbitrary assign \(\mu\)。实际采用 master inversion / W-first source-semantic construct。第二 full-corridor shape由 source equations直接产生 \(\mu=50\)，不是预设。

## 33. First Reduced-Defect Shape

没有 \(\Delta_{\rm rad}<32\) hit。第二 full-corridor shape反而为 50。

## 34. First \(\Delta_{\rm rad}=1\) Shape

```text
NONE
```

## 35. First μ-Smith Pass

```text
FIRST_POSITIVE_MU_SMITH_PASS=NO
```

因此 R19 按 first-failure firewall 不继续 tail/window/q。

## 36. Tail-Extra Reactivation

```text
NOT_ACTIVATED
```

## 37. First Support-Stack Pass

```text
NO_NOT_REACHED
```

## 38. Denominator Ratio Regression

R18 theorem保持冻结；R19 没有合法资格把 ratio 变成 current gate。

## 39. First Pre-q Pass

```text
NO_NOT_REACHED
```

## 40. Residual Selector

```text
NOT_ACTIVATED
```

## 41. First z Pass

```text
NO_NOT_REACHED
```

## 42. Full Source Reconstruction

```text
NOT_REACHED
```

## 43. Exact U

```text
NOT_REACHED
```

## 44. Downstream Audit

没有越级：Smith reconstruction、PSDG regression、plain U、digit synchronization、actual cut、full word、outer completion全部保持冻结。

## 45. New First-Failure Gate

\[
\boxed{
\textbf{FACE-2 DECIMAL-PRIMARY ABSORPTION BUDGET}
}
\]
即 (R19-F2-DEC)。这是一个 single source-defined prime class：
\[
\boxed{\ell\in\{2,5\},\ \ell\mid C_2,\ \ell\mid P_1}.
\]
所有其他 radial prime classes 已解决。

## 46. R19 Information-Gain Certificate

R19 新增并 exact regression：

1. \(R_M=h(L,p)/g_0\) exact equivalence；
2. \(m_{\rm src}=\Omega(N_M,P_1)/N_M\) source-native formula；
3. \(\mu=hL/(g_0\Omega_D)=N_M/(g_0\Omega)\) direct formula；
4. closed defect formula \(\delta_\ell=v_\ell(N_M/g_0)-v_\ell(\Omega)\)；
5. radial valuation budget theorem；
6. nondecimal Face-2/Face-3 automatic saturation theorem；
7. shared radial automatic saturation theorem；
8. exact Face-3 decimal-primary classification；
9. live Face-2 decimal budget normal form；
10. 第二条 genuine full-corridor shape；
11. exact construct extensions与 ten-unit targeted no-hit evidence；
12. current gate 从 arbitrary radial support 降维到 one source-defined decimal-primary Face-2 class。

## 47. R19 Terminal Verdict

```text
R19_TERMINAL_VERDICT=R19_REDUCED_TO_SINGLE_FACE2_DECIMAL_PRIMARY_ABSORPTION_DEFECT_GATE
```

没有 universal collision；没有 first μ-Smith pass；但符合 Outcome C，因为所有 failure 已集中到一个 source-defined prime class。

## 48. R20 Authorization Decision

按 Route B：

```text
R20_AUTHORIZED=YES
R20_ARCHITECTURE=FACE2_DECIMAL_PRIMARY_ABSORPTION_ONLY
R20_SINGLE_ATTACK_TARGET=FOR_ELL_IN_{2,5}_WITH_ELL_DIVIDES_C2_AND_P1_DECIDE_EXACT_OMEGA_BUDGET_EQUALITY
```

R20 不得重开 nondecimal radial primes、Face-3 decimal support、master corridor、tail/window 或 q。

---

## Machine-readable terminal block

```text
R19_TERMINAL_VERDICT=R19_REDUCED_TO_SINGLE_FACE2_DECIMAL_PRIMARY_ABSORPTION_DEFECT_GATE

R1_TO_R18_STATE_FROZEN=YES

CURRENT_FIRST_FAILURE_GATE=FACE2_DECIMAL_PRIMARY_ABSORPTION_BUDGET

FULL_MASTER_CORRIDOR_PRECONDITION=PASS__2_EXACT_SHAPES_IN_R19_REGISTRY

RM=SHAPE_DEPENDENT__R17=160__R19_SECOND=100
MSRC=SHAPE_DEPENDENT__R17=5__R19_SECOND=2
MU=SHAPE_DEPENDENT__R17=32__R19_SECOND=50

MU_EQUALS_RM_OVER_MSRC=YES

C2=SHAPE_DEPENDENT__R17=60__R19_SECOND=310
C3=SHAPE_DEPENDENT__R17=13683__R19_SECOND=71549
RADIAL_SUPPORT=R17={2,3,5,4561}__R19_SECOND={2,5,31,71549}

ABSORBED_CONTENT_SMITH_SATURATION_THEOREM=PROVED

RM_RADIAL_PART=R17=160__R19_SECOND=100
MSRC_RADIAL_PART=R17=5__R19_SECOND=2
RADIAL_ABSORPTION_DEFECT=R17=32__R19_SECOND=50

RADIAL_ABSORPTION_DEFECT_EQUALS_MU_RADIAL_PART=YES

PRIMEWISE_DEFECT_FORMULA=DELTA_l=v_l(RM)-v_l(MSRC)=v_l(NM/g0)-v_l(Omega)=v_l(MU)

RADIAL_VALUATION_BUDGET_THEOREM=PROVED__B_l=v_l(D/h)+v_l(Esrc)+v_l(RM)=v_l(NM/g0);_DELTA_l=B_l-v_l(Omega)

FIRST_BAD_RADIAL_PRIME=R17=2__R19_SECOND=2

TWO_ADIC_RADIAL_SUPPORT_STATUS=RESOLVED_EXCEPT_FACE2_DECIMAL_PRIMARY_CLASS
FIVE_ADIC_RADIAL_SUPPORT_STATUS=RESOLVED_EXCEPT_FACE2_DECIMAL_PRIMARY_CLASS__R17_PROVIDES_PRIMEWISE_5_SATURATION_COUNTEREXAMPLE_TO_UNIVERSAL_FAIL
ODD_C2_SUPPORT_STATUS=ALL_ODD_PRIMES_EXCEPT_5_AUTOMATICALLY_SATURATED__5_ONLY_IN_LIVE_DECIMAL_CLASS
ODD_C3_SUPPORT_STATUS=ALL_NONDECIMAL_AUTOMATICALLY_SATURATED__5_DECIMAL_FACE3_EXACTLY_CLASSIFIED

R17_WITNESS_REGRESSION=PASS__RM=160__MSRC=5__MU=32__DELTA2=5__DELTA_RAD=32

FULL_CORRIDOR_SHAPES_FOUND=2
FULL_CORRIDOR_REGISTRY=105_R19_Full_Corridor_Registry.csv

MIN_RADIAL_ABSORPTION_DEFECT=32

MU_EQUALS_ONE_SHAPE_FOUND=NO
RM_RADIAL_PART_ONE_SHAPE_FOUND=NO

FIRST_POSITIVE_MU_SMITH_PASS=NO
MU_SMITH_PASS_SHAPE=NONE

LAMBDA_Z=NOT_ACTIVATED
TAU=NOT_ACTIVATED
R1_RESIDUAL=SHAPE_DATA_AVAILABLE_BUT_DOWNSTREAM_NOT_ACTIVATED

TAIL_G1_SUPPORT_PASS=NOT_ACTIVATED
TAIL_SMITH_SUPPORT_PASS=NOT_ACTIVATED

FIRST_POST_MASTER_SUPPORT_STACK_PASS=NO_NOT_REACHED

DENOMINATOR_RATIO_PASS=NOT_ACTIVATED
INTEGER_WINDOW_PASS=NOT_ACTIVATED
FORCED_SCALE_FIT=NOT_ACTIVATED

FIRST_POST_MASTER_PREQ_SHELL_PASS=NO_NOT_REACHED

RESIDUAL_SUCCESSOR_PASS=NOT_ACTIVATED

Z_SELECTOR_PASS=NO_NOT_REACHED
Z=NONE

FULL_SMITH_RECONSTRUCTION=NOT_REACHED
FULL_POST_PSDG_LIFT=NO_NOT_REACHED

PLAIN_U=NOT_REACHED
SOURCE_SELECTOR_PASS=NOT_REACHED
SOURCE_INTEGER_U_FOUND=NO

COMMON_U_INTEGER_SUCCESSOR_GATE=NOT_REACHED

DIGIT_SYNCHRONIZATION=NOT_REACHED
ACTUAL_CUT=NOT_REACHED
FULL_WORD=NOT_REACHED
OUTER_COMPLETION=NOT_REACHED

ABSORBED_CONTENT_RESIDUAL_SMITH_SUPPORT_OBSTRUCTION_PROVED=NO
RADIAL_ABSORPTION_VALUATION_BUDGET_OBSTRUCTION=NO_GLOBAL__FACE3_DECIMAL_ACTIVE_CLASS_OBSTRUCTION_PROVED

POST_MASTER_TRANSVERSE_SHELL_UNLIFTABILITY_PROVED=NO
POSITIVE_RADIAL_CORE_UNLIFTABILITY_PROVED=NO

R19_SINGLE_RADIAL_ABSORPTION_DEFECT_GATE=YES__ELL_IN_{2,5}__ELL_DIVIDES_C2__ELL_DIVIDES_P1__OMEGA_BUDGET_EQUALITY

DEEPEST_POST_CORRIDOR_PASS=DEPTH_0_FULL_MASTER_CORRIDOR

NEW_FIRST_FAILURE_GATE=FACE2_DECIMAL_PRIMARY_ABSORPTION_BUDGET_EQUALITY

R19_INFORMATION_GAIN_CERTIFICATE=RM_MSRC_MU_DIRECT_NORMALIZATION_PLUS_CLOSED_DEFECT_PLUS_BUDGET_THEOREM_PLUS_NONDECIMAL_SATURATION_PLUS_SHARED_SATURATION_PLUS_FACE3_DECIMAL_CLASSIFICATION_PLUS_SECOND_FULL_CORRIDOR_SHAPE_PLUS_TARGETED_CONSTRUCT_CAMPAIGN

R20_AUTHORIZED=YES
R20_ARCHITECTURE=FACE2_DECIMAL_PRIMARY_ABSORPTION_ONLY
R20_SINGLE_ATTACK_TARGET=DECIDE_v_l(Omega)=m2+n3+g+v_l(W)-min(v_l(W),v_l(P1))_FOR_l_IN_{2,5}_WITH_l_DIVIDES_C2_AND_P1
```
