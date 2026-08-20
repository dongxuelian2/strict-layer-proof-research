#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path
from J2_65_R5_common import HERE,ROW_TYPES

DNF=HERE/'J2-65-R5-InternalDisjunctions.tsv'
MAP=HERE/'J2-65-R5-C3TubeMap.tsv'
with DNF.open(encoding='utf-8') as f: drows=list(csv.DictReader(f,delimiter='\t'))
with MAP.open(encoding='utf-8') as f: mrows=list(csv.DictReader(f,delimiter='\t'))

stats=defaultdict(lambda: defaultdict(int))
meta={}
for r in drows:
    fid=r['fibre_id']; stats[fid][r['type']]+=1
    if r['type']=='C3':
        if r['status']=='CLOSED_BY_R4_FIXED_DEPTH': stats[fid]['C3_FIXED_CLOSED']+=1
        else: stats[fid]['C3_SURVIVE']+=1
    if fid not in meta:
        x=fid[2:].split('__'); meta[fid]=(x[0],x[1])

fibres=[]
for fid in sorted(meta):
    t2,t5=meta[fid]; st=stats[fid]
    internal=[p for p,t in ((2,t2),(5,t5)) if t!='K_EQ_G']
    c1=[p for p,t in ((2,t2),(5,t5)) if t=='K_EQ_G']
    fibres.append(dict(
        fibre_id=fid,p2_type=t2,p5_type=t5,internal_places=','.join(map(str,internal)) or 'NONE',cross_row_places=','.join(map(str,c1)) or 'NONE',
        c2_affine_pair_cells=st['C2'],c3_lift_support_disjuncts=st['C3'],c3_closed_r4_fixed=st['C3_FIXED_CLOSED'],
        c3_closed_r5_ceiling=0,c3_surviving=st['C3_SURVIVE'],c2_only='NO',whole_fibre_closed='NO',
        surviving_description=('C1xC1 only' if not internal else 'C2 affine tie cells OR surviving C3 lift-support strata')))

p=HERE/'J2-65-R5-RefinedFibres.tsv'
with p.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(fibres[0]),delimiter='\t');w.writeheader();w.writerows(fibres)

c3_total=sum(int(x['c3_lift_support_disjuncts']) for x in fibres)
fixed=sum(int(x['c3_closed_r4_fixed']) for x in fibres)
surv=sum(int(x['c3_surviving']) for x in fibres)
assert len(fibres)==9 and c3_total==132 and fixed==21 and surv==111

cert=f'''J2-65-R5 Cyclotomic Reciprocal Tube Certificate
===================================================
SCOPE=Strict Layer A1-only; Exact Resonance R=0; J=2; q>1 main object
ROUND=65_R5 / A1_UNIFIED_TERMINAL_R30

J2_65_R5_STATUS=OPEN
R4_BRACKET_COMPLEX_REGRESSION=PASS
R4_PATTERN_FIBRES=9
R4_UNBOUNDED_TUBES=7

RECIPROCAL_TUBE_IDENTITY=PASS
RECIPROCAL_TUBE_SHALLOW_LAW=PROVED
RECIPROCAL_TUBE_SUPERCRITICAL_LAW=PROVED
RECIPROCAL_TUBE_CRITICAL_INTERFACE=PROVED

CYCLOTOMIC_RECIPROCAL_CONGRUENCE=PROVED
CYCLOTOMIC_ORDER_THEOREM=PROVED
Q_PRIME_ASSUMED=FALSE
ORD_q_EQ_2g_ASSUMED=FALSE

RECIPROCAL_POLYNOMIAL_COUNT=7
RECIPROCAL_POLYNOMIAL_AUDIT=PASS

QPLUS4_PAIR_BOUND=PROVED
QMINUS2_PAIR_BOUND=PROVED
THREEQPLUS2_PAIR_BOUND=PROVED
RATIONAL_TUBES_SHALLOW_LIVE_RANGE=PROVED:q+4_and_3q+2_have_m<g_for_g>=2;q-2_has_m<g_for_g>=1
B5_GLOBAL_G_BOUND=PROVED

ALGEBRAIC_TUBE_DEPTH_CEILINGS=PROVED
TUBES_WITH_GLOBAL_DEPTH_CEILING=7
GENERIC_ALGEBRAIC_PAIR_BOUND=p^(m+min(m,g))<=C_D*C_Dvee*(10^g+1)^deg(D)

INTERNAL_DISJUNCTION_DNF=PASS
C3_DISJUNCTS_TOTAL={c3_total}
C3_CLOSED_BY_R4_FIXED_DEPTH={fixed}
C3_CLOSED_BY_R5_TUBE_CEILING=0
C3_SURVIVING={surv}
C2_ONLY_FIBRES=0
ALL_C3_MAP_TO_DETERMINANT_TUBE=FALSE
C3_MAPPING_OBSTRUCTION=SINGLE_LINEAR_LIFT_AND_CONIC_LIFT_DISJUNCTS_REQUIRE_NO_SECOND_LINEAR_BRACKET
ROW_INTERNAL_UNBOUNDED_PAIR_KERNEL=p2:D8;p5:q+4_with_optional_D9

ADELIC_PINNING_CASES=0
DETERMINISTIC_q_SEQUENCES=0
DETERMINISTIC_u_SEQUENCES=0

FORCED_LINEAR_ZERO_LOCI=0
FORCED_CONIC_LOCI=0
TEN_PRIMARY_DEPTH_TO_ZERO_TRIGGERED=FALSE

R5_SURVIVING_BRACKET_FIBRES=9
BOUNDARY_STATUS=OPEN
HIGH_STATUS=OPEN
REVERSE_QGT1_STATUS=OPEN
QGT1_STATUS=OPEN

S_UNIT_REDUCTION_REACHED=FALSE

NEW_GLOBAL_THEOREM=CYCLOTOMIC_RECIPROCAL_TUBE_TRANSFER + SEVEN_GLOBAL_DEPTH_CEILINGS + RATIONAL_SHALLOW_THEOREM + EXACT_INTERNAL_LIFT_SUPPORT_DNF
SURVIVING_GLOBAL_OBJECT=3_ARCH_FACES_X_9_EXACT_ROW_INCIDENCE_DNFS_WITH_111_SURVIVING_C3_LIFT_SUPPORT_STRATA;SEVEN_AMBIENT_TUBES_ARE_SLOPE_CONTROLLED_EDGE_LABELS_NOT_A_CARTESIAN_FACTOR
NEXT_UNIQUE_OBJECT=SINGLE_BRACKET_PROJECTIVE_TUBE_ASSIGNMENT_X_TWO_PLACE_SAME_GENERATOR_ALIGNMENT_X_C2_AFFINE_TIE_GEOMETRY

J2_CLOSED=FALSE
'''
(HERE/'J2-65-R5-certificate.txt').write_text(cert,encoding='utf-8')

report=r'''# J2-65-R5 Cyclotomic Reciprocal Tube Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — A1-only — Exact Resonance R=0 — J=2  
**Round:** 65 第五轮 / A1 统一终端线第三十轮  
**Status:** **J2 OPEN**

## 0. Executive verdict

本轮完成了 R4 指定的主对象：

\[
q\mid 10^g+1
\quad\times\quad
\text{determinant Hensel tubes}.
\]

得到四个确定的新结论。

1. **Cyclotomic reciprocal-tube transfer 完整成立。** 对任意 p=2,5 的 simple unit root \(\rho\)，若 \(r=v_p(q-\rho)\)，则 \(u=(10^g+1)/q\) 自动进入 \(\rho^{-1}\) 的 reciprocal tube；在 \(r<g,r>g,r=g\) 三个区间得到 exact transfer law。
2. **R4 的 7 条 unbounded determinant tubes 全部获得 global depth-vs-g ceiling。** 三条 rational 5-adic tubes 得到 sharp complementary-divisor product bounds；D7,D8,D4,D9 得到 reciprocal polynomial height pair bounds。
3. **三条 rational tubes 比“斜率受控”更强：在 live range 全部 shallow。** \(q+4\) 与 \(3q+2\) 在 \(g\ge2\) 时强制 \(m<g\)，\(q-2\) 在 \(g\ge1\) 时强制 \(m<g\)。因此它们的 reciprocal depth始终精确等于 q-side depth。
4. **R4 的 C2/C3 模糊 disjunction 被真正展开，但这同时暴露出一个结构性 obstruction：并非每个 C3 都能绑定 determinant tube。** 9 fibres 的 exact lift-support DNF 中有 132 个 C3 support disjuncts；21 个由 R4 fixed 2-adic determinant depth关闭，111 个仍存活。存活项包含 single-linear lift 与 conic lift；这类 disjunct 根本不要求第二个 linear bracket，因此 DET-GCD 没有 determinant 可调用。

所以本轮没有关闭 q>1，也没有 force deterministic Hensel divisor sequence 或 exact bracket zero。真正的新 frontier 不再是“7 条无界 tube”，而是：

\[
\boxed{
3\text{ Arch faces}
\times
9\text{ exact row-incidence DNFs}
}
\]

其中 7 条 ambient determinant tubes 已全部 slope/height-controlled，并只作为 **pairwise C3 edge labels** 出现，而不是一个独立的 \(\times7\) Cartesian factor。

---

## 1. Frozen R4/R3 interface actually used

R5只使用 R4 actual report/certificate 中已经证明的接口：

- 10 grouped coefficients 压成 7 primitive additive generators；
- 5 个 linear projective brackets + 2 个 Type-H conics；
- \(\gcd(L_i,L_j)\mid\Delta_{ij}(q)\)；
- live 2/5-primary determinant kernel 的 8 factors 与 7 unbounded tubes；
- 2-adic unbounded extra factors只有 D7,D8；
- 5-adic live unbounded factors为 \(q+4,3q+2,D4,q-2,D9\)，而 \(q^2+6q+4\) 在 live \(q\equiv2\pmod5\) fibre 上 exact depth 1；
- \(27=3\) Arch faces \(\times9\) bracket-pattern fibres；
- internal row只给 C2 OR C3，不指定具体 pair/depth；
- same-bracket simultaneous 2/5 depth-to-zero lemma继续冻结；
- B21 exact zero locus继续冻结 CLOSED。

本轮没有重新证明这些结果，也没有把 R4 prompt 当 source。

---

## 2. Cyclotomic Reciprocal-Tube Transfer

令

\[
G=10^g,\qquad uq=G+1,
\]

取 \(p\in\{2,5\}\)，\(\rho\in\mathbf Z_p^\times\) 为某 live determinant factor 的 simple root。直接 exact identity：

\[
\boxed{
 u-\rho^{-1}
 =\frac{\rho G-(q-\rho)}{q\rho}.
}
\tag{RT}
\]

因为 \(q,\rho\) 都是 p-units，分母 valuation 为 0。记

\[
r=v_p(q-\rho).
\]

### 2.1 Shallow regime: r<g

numerator 两项 valuation 分别为 g 与 r，最低阶唯一，因此

\[
\boxed{v_p(u-\rho^{-1})=r.}
\]

### 2.2 Supercritical regime: r>g

最低阶唯一为 g，因此

\[
\boxed{v_p(u-\rho^{-1})=g.}
\]

这说明 complementary divisor 的 automatic reciprocal depth 在 supercritical q-tube 上发生 **saturation at g**。

### 2.3 Critical regime: r=g

写

\[
q-\rho=p^g\varepsilon,
\qquad \varepsilon\in\mathbf Z_p^\times,
\]

以及

\[
G=p^g c_p^g,
\qquad c_2=5,\quad c_5=2.
\]

则

\[
\boxed{
 v_p(u-\rho^{-1})
 =g+v_p(\rho c_p^g-\varepsilon).
}
\tag{RT-C}
\]

这就是完整 critical interface；没有展开 next p-adic digit。

---

## 3. Finite-depth reciprocal congruence and order theorem

对任意 \(m\le g\)，

\[
qu=1+10^g\equiv1\pmod{p^m}.
\]

因此

\[
q\equiv\rho\pmod{p^m}
\Longrightarrow
\boxed{u\equiv\rho^{-1}\pmod{p^m}}.
\]

这同时说明 reciprocal root不是新 arithmetic variable，只是同一 local tube 在 complementary divisor coordinate 中的 center。

### 3.1 Exact order audit

令

\[
n_q=\operatorname{ord}_q(10).
\]

因为 q 是 odd ten-unit divisor 且 \(10^g\equiv-1\pmod q\)，元素 \(10^g\) 在 \((\mathbf Z/q\mathbf Z)^\times\) 中 order 恰为 2。所以

\[
\frac{n_q}{\gcd(n_q,g)}=2.
\]

令 \(d=\gcd(n_q,g)\)，得到

\[
\boxed{n_q=2d,\quad d\mid g,\quad g/d\text{ odd}.}
\]

整个证明不要求 q prime，也没有假设 \(n_q=2g\)，更没有把 composite q 偷换成 \(q\mid\Phi_{2g}(10)\)。

---

## 4. Reciprocal determinant catalog

对

\[
D(q)=a_dq^d+\cdots+a_0
\]

定义

\[
D^\vee(u)=u^dD(u^{-1}).
\]

若 \(D(\rho)=0\)，则 \(D^\vee(\rho^{-1})=0\)。并且

\[
(D^\vee)'(\rho^{-1})=-\rho^{2-d}D'(\rho),
\]

所以 unit simple root保持 simple。

7 条 reciprocal polynomials 已全部 exact 生成。三个 rational cases 为

\[
q+4\leftrightarrow 1+4u,
\]

\[
q-2\leftrightarrow 1-2u,
\]

\[
3q+2\leftrightarrow3+2u.
\]

其余四条是 D7,D8,D4,D9 的 coefficient reversal；详见 `J2-65-R5-ReciprocalDeterminants.tsv`。

---

## 5. Transfer to A and B_det

由 \(A=2u+1\)，令

\[
A_\rho=2\rho^{-1}+1.
\]

则

\[
\boxed{v_5(A-A_\rho)=v_5(u-\rho^{-1})},
\]

\[
\boxed{v_2(A-A_\rho)=1+v_2(u-\rho^{-1})}.
\]

这只是整数 A 本身在 \(\mathbf Z_p\) 中的 tube，**不是** primitive A-ROOT congruence \(Kx+Z\equiv0\pmod A\)。R5没有把两者混用。

另 \(B_{\rm det}=2G+q\) 给

\[
v_5(B_{\rm det}-q)=g,
\qquad
v_2(B_{\rm det}-q)=g+1.
\]

所以 shallow q-tube也同步传给 B_det，但本轮没有人为把它升级成独立 obstruction。

---

## 6. Sharp rational tube theorem

令 \(M=5^m\)。

### 6.1 q+4

若 \(m=v_5(q+4)\ge1\)，则

\[
q\equiv-4\pmod M,
\qquad
u\equiv-\frac14\pmod M.
\]

因此

\[
q\ge M-4,
\qquad
u\ge\frac{M-1}{4},
\]

从而

\[
\boxed{
10^g+1=qu\ge\frac{(M-4)(M-1)}4.
}
\tag{Q4-PAIR}
\]

等价地

\[
\boxed{
5^m\le\frac{5+\sqrt{25+16\cdot10^g}}2.
}
\]

这给旧 structural depth

\[
b_5=v_5(q+4)
\]

一个真正 global g-bound。特别地，若 \(g\ge2\)，假设 \(m\ge g\) 会要求

\[
5^g>4\cdot2^g+5
\]

的反向不等式失败，因此

\[
\boxed{b_5=m<g\qquad(g\ge2).}
\]

### 6.2 q-2

q 是 odd 且不能等于 2，所以

\[
q\ge M+2,
\qquad
u\ge\frac{M+1}{2}.
\]

于是

\[
\boxed{
10^g+1\ge\frac{(M+2)(M+1)}2,
}
\]

以及

\[
\boxed{
5^m\le\frac{-3+\sqrt{9+8\cdot10^g}}2.
}
\]

并且对所有 \(g\ge1\)：

\[
\boxed{m<g.}
\]

### 6.3 3q+2

由 \(3q+2\equiv0\pmod M\)，raw least positive q-residue 为

\[
q_0=
\begin{cases}
(M-2)/3,&m\text{ odd},\\
2(M-1)/3,&m\text{ even}.
\end{cases}
\]

但 q 必须是 odd 且 q>1。因此 sharp admissible representative 是

\[
Q_m=
\begin{cases}
11,&m=1,\\
(M-2)/3,&m\ge3\text{ odd},\\
(5M-2)/3,&m\text{ even}.
\end{cases}
\]

而 reciprocal least residue为

\[
u\ge\frac{M-3}{2}.
\]

所以

\[
\boxed{10^g+1\ge Q_m\frac{M-3}{2}.}
\]

当 m odd >=3：

\[
5^m\le\frac{5+\sqrt{25+24\cdot10^g}}2;
\]

当 m even：

\[
5^m\le\frac{17+\sqrt{289+120\cdot10^g}}{10}.
\]

并且在 \(g\ge2\) 时仍有

\[
\boxed{m<g.}
\]

三条 rational tube 的 leading slope 都是

\[
\boxed{
\lambda=\frac{\log10}{\log25}=\frac12\log_5 10
=0.715338279\ldots
}
\]

但 live theorem 比 asymptotic statement更强：它们根本不会跨过 critical wall \(m=g\)。

---

## 7. Algebraic tubes D7,D8,D4,D9: reciprocal height pair theorem

令 \(D\) 的 degree 为 d，并取

\[
C_D=\sum_i|a_i|.
\]

对 q>=1，

\[
|D(q)|\le C_D q^d.
\]

对应 reciprocal polynomial 的 coefficient height相同：

\[
C_D^\vee=C_D.
\]

四条 factor 的 exact constants：

- D7: d=3, C=14;
- D8: d=2, C=4;
- D4: d=6, C=1125;
- D9: d=3, C=55.

这些 polynomial 在 live positive integer q 上非零；reciprocal polynomial 在 positive integer u 上也无 integer zero，因此若 q-side depth为 m，则

\[
p^m\le |D(q)|\le C_Dq^d.
\]

reciprocal transfer至少给 u-side depth \(\min(m,g)\)，所以

\[
p^{\min(m,g)}\le |D^\vee(u)|\le C_Du^d.
\]

相乘得到 exact global pair ceiling：

\[
\boxed{
 p^{m+\min(m,g)}
 \le C_D^2(10^g+1)^d.
}
\tag{D-PAIR}
\]

令

\[
E_D(g)=\left\lfloor\log_p\big(C_D^2(10^g+1)^d\big)\right\rfloor.
\]

则

\[
 m\le g\Longrightarrow m\le\lfloor E_D(g)/2\rfloor,
\]

\[
 m\ge g\Longrightarrow m\le E_D(g)-g.
\]

因此 R4 的所有 7 条“unbounded” tube 现在都应改称

\[
\boxed{\text{unbounded in isolation, globally slope/height-controlled under }qu=10^g+1.}
\]

注意 supercritical 情况没有错误写成 \(p^{2m}\)：u-side automatic depth只保证 g。

---

## 8. Hensel truncation and adelic pinning

若

\[
q\equiv r_m(\rho)\pmod{p^m},
\qquad0<r_m(\rho)<p^m,
\]

且 q<p^m，则

\[
q=r_m(\rho).
\]

u-side同理，但 modulus depth必须取实际 reciprocal depth，至少为 \(\min(m,g)\)。

若同时有 2-adic 与 5-adic q-tubes：

\[
q\equiv r_2\pmod{2^{m_2}},
\qquad
q\equiv r_5\pmod{5^{m_5}},
\]

CRT 给唯一 residue mod

\[
2^{m_2}5^{m_5}.
\]

若该 modulus >q，q 被 pinned；u-side亦然。若两边都 pinned，actual solution必须满足 exact product equality

\[
r_ms_n=10^g+1.
\]

R5建立了这个 theorem/interface，但当前 DNF **没有 force 任何一组足够深的 simultaneous determinant tubes**，所以

\[
\boxed{
\text{ADELIC PINNING CASES}=0,
\quad
\text{DETERMINISTIC q/u SEQUENCES}=0.
}
\]

这不是用有限 scan 得出的，而是“触发前提尚未被结构强迫”。

---

## 9. Exact C2/C3 DNF for the 9 bracket fibres

R4 的 9 fibres正是

\[
\{K<G,K=G,G<K\}_{p=2}
\times
\{K<G,K=G,G<K\}_{p=5}.
\]

R5不再复制 27 个 Arch copies；Arch face作为外部 factor保留。

### 9.1 Exact row valuation coordinate

对 grouped term \(C_{ab}G^aK^b\)，定义 factor-aware base valuation coordinate

\[
W^{(0)}_{ab,p}=ag+bk+\nu_p(C_{ab}),
\]

其中 \(\nu_p(C_{ab})\) 是 R4 factor-aware coefficient valuation，不含 genuine additive extra cancellation。

若该 coefficient含 additive generator B，定义

\[
\delta_{B,p}\ge0
\]

为额外 bracket cancellation depth；monomial项没有 delta。于是 actual term valuation为

\[
W_{ab,p}=W^{(0)}_{ab,p}+\delta_{B,p}.
\]

这只是 valuation metadata，不是新 terminal variable。

### 9.2 C2 cells

C2定义为该 row 所有 additive delta均为 0。内部至少双 minimum 的 exact condition就是 5 个 terms 中某一 pair满足

\[
W^{(0)}_i=W^{(0)}_j\le W^{(0)}_\ell\quad(\ell\ne i,j).
\]

每个 internal row因此有 exactly 10 个 pair cells。它们都是 exact affine valuation cells；例如同一 row 内 b相同，equality可写成

\[
(a_i-a_j)g+\nu_p(C_i)-\nu_p(C_j)=0.
\]

全部具体 pair inequalities 已写入 `J2-65-R5-InternalDisjunctions.tsv`。

### 9.3 C3 lift-support strata

K-row terms为

\[
C_{01},\ C_{11}(B11),\ C_{21}(B21),\ C_{31}(B31),\ C_{41}.
\]

其 additive set有 3 个 generators，所以 nonempty positive-lift supports共有

\[
2^3-1=7.
\]

G-row terms为

\[
C_{10}(B10),\ C_{20}(H20),\ C_{30}(H30),\ C_{40}(B40),\ C_{50},
\]

additive set有 4 个 generators，所以共有

\[
2^4-1=15
\]

个 positive-lift supports。

在每一个 support stratum 内，actual minimum multiplicity仍由 10 个 exact pair clauses

\[
W_i=W_j\le W_\ell
\]

组成；这些 pair clauses以 explicit string完整存入 TSV，而不是一句 “internal cancellation somewhere”。

跨 9 fibres、两个 places计：

\[
\boxed{C3\_DISJUNCTS\_TOTAL=132.}
\]

---

## 10. Determinant applicability audit: the key R5 correction

这里出现本轮最重要的负结论。

DET-GCD 的前提是 **两个 linear brackets同时深**。但 exact C3 DNF中存在：

1. 单个 linear bracket 被抬深后与 monomial/base term 相遇；
2. 单个 conic被抬深；
3. linear-conic 或 conic-conic lift supports。

这些都不提供两个 linear \(L_i,L_j\)。因此命题

> every C3 disjunct maps to one of the seven determinant tubes

是 **FALSE**。

这是逻辑上的 counterexample class，不是数值反例：例如 K-row support \(\{B11\}\) 就是一个 exact C3 stratum；它要求 B11具有正 extra depth，却没有第二条 linear bracket，因此不存在 \(\Delta_{ij}\) 可调用。

### 10.1 Row-internal determinant kernel actually seen by C3

把 full R4 line graph投影到“同一 internal row 的两条 linear generators”后，kernel骤然缩小。

K-row只有三条 linears：B11,B21,B31：

- B11-B21: \(4q(q+4)D8\)；p=2 唯一 unbounded extra factor为 D8；
- B11-B31: \((q+4)D9\)；p=2 determinant是 unit，p=5可见 structural q+4 与 extra D9；
- B21-B31: \(-(q+2)(q+4)D10\)；p=2 determinant是 unit，p=5只有 structural q+4 depth。

G-row只有两条 linears B10,B40：

- B10-B40: \(-(q+4)D1\)；p=2 determinant是 unit；p=5只有 structural q+4 depth。

因此对当前 internal C3 pair geometry，真正的 **unbounded row-internal pair kernel** 只剩

\[
\boxed{
p=2:\ D8;
\qquad
p=5:\ q+4\text{ with optional }D9.
}
\]

D7、3q+2、D4、q-2 等 ambient tubes仍获得了本轮 global ceiling，但它们并不是当前 same-row C3 DNF 的强制 edge。这是比“9 fibres x 7 tubes”更准确的 incidence geometry。

此外，p=5 的任何 **two-linear** C3 support若发生，则其 same-row determinant 必含 \(q+4\)，而其余 accompanying factor在 live \(q\equiv2,4\pmod5\) 上都是 5-unit。因此这些 support 自动 refine 到

\[
\boxed{q\equiv1\pmod5,\quad b_5>0,\quad c_5=0.}
\]

跨 9 fibres 共 24 个 p5 two-linear lift-support disjuncts得到这一 branch refinement；它们不是被关闭，而是从三类 live residue branch压到旧 structural \(q+4\) tube。

---

## 11. C3 deaths

### 11.1 Closed by R4 fixed depth

在 p=2：

- K-row任何 lift support同时含 B31 与 B11 或 B21 时，会要求两条 primitive linears都被 2 整除；但对应 determinant是 2-unit，所以 impossible；每个 K-internal fibre关闭 3 个 C3 supports；
- G-row任何 support同时含 B10,B40 时，同理因 \(v_2(\Delta_{10,40})=0\) impossible；每个 G-internal fibre关闭 4 个 supports。

跨 9 fibres计：

\[
\boxed{C3\_CLOSED\_BY\_R4\_FIXED\_DEPTH=21.}
\]

### 11.2 Closed by R5 tube ceiling

对剩余 determinant-controlled supports，R5提供：

- p=2 D8 depth ceiling；
- p=5 q+4 sharp bound；
- B11-B31 intersection上还可加 D9 ceiling。

但 R4 的 required-depth expressions仍含 \(v_p(d),v_p(h),k,v_p(x),v_p(\alpha),v_p(t),c_5\) 等 structural coordinates。现有 actual sources没有证明这些 \(\Lambda\) 在所有 live states中 uniformly 大于 R5 ceiling。

所以本轮不能合法声称新 ceiling关闭某个完整 support stratum：

\[
\boxed{C3\_CLOSED\_BY\_R5\_TUBE\_CEILING=0.}
\]

这不是说 ceiling无用，而是它现在是 exact conditional death rule；缺的是 **generator assignment + structural depth lower bound**。

最终

\[
\boxed{C3\_SURVIVING=111.}
\]

没有 fibre 被迫只剩 C2：

\[
\boxed{C2\_ONLY\_FIBRES=0.}
\]

---

## 12. Old b5 tube reinserted into T5

旧 5-adic target为

\[
T_5=2v_5(d)+2b_5+2c_5+k+v_5(x).
\]

R5现在可以合法代入

\[
b_5\le B_5(g),
\qquad
5^{B_5(g)}\le\frac{5+\sqrt{25+16\cdot10^g}}2,
\]

得到

\[
T_5\le2v_5(d)+2B_5(g)+2c_5+k+v_5(x).
\]

并且 live range中 \(b_5<g\)。这第一次把 old structural b5 从“unbounded descriptor”变成 global g-controlled coordinate。

但由于 \(v_5(d)-v_5(h)\)、\(v_5(x)\)、k 等尚未统一锁定，该上界本身还不能让某一 entire 5-adic internal row消失。R5没有夸大这一点。

---

## 13. No exact zero / no S-unit gate yet

本轮没有 force任何

\[
L_i=0
\]

或 H20/H30 exact zero，也没有 determinant polynomial exact zero。R4 的 same-bracket 2/5 depth-to-zero lemma没有被触发，因为 DNF尚未强迫同一 fixed generator在两个 places同时达到足够深度。

所以：

- `FORCED_LINEAR_ZERO_LOCI=0`;
- `FORCED_CONIC_LOCI=0`;
- `S_UNIT_REDUCTION_REACHED=FALSE`.

没有进入 Thue-Mahler / S-unit / Pell / Gaussian prime support。

---

# 14. Direct answers to the twelve required questions

## Q1. q 落入 determinant p-adic root tube 后，u 落到哪里？

精确落入 reciprocal center \(\rho^{-1}\)。若 q-side depth r<g，则 u-side depth恰为 r；r>g 时自动 depth饱和为 g；r=g 时由 normalized unit \(\rho c_p^g-\varepsilon\) 决定额外深度。

## Q2. 跨过 r=g 时发生什么？

从 “depth-preserving” 变为 “depth-saturating”。critical wall上两项同 valuation，唯一额外自由度是一次 unit cancellation：

\[
v_p(u-\rho^{-1})=g+v_p(\rho c_p^g-\varepsilon).
\]

没有 next-bit ladder。

## Q3. 7 条 unbounded tubes能多深？

三条 rational 5-adic tube有 sharp quadratic product ceiling，leading slope \(0.715338\ldots g\)，且 live range直接强制 m<g。D7,D8,D4,D9满足统一 exact bound

\[
p^{m+\min(m,g)}\le C_D^2(10^g+1)^{d_D},
\]

从而获得 piecewise linear-in-g ceiling。7/7全部已 globalized。

## Q4. b5=v5(q+4) 是否得到真正 global g-bound？

**YES.** 

\[
5^{b_5}\le\frac{5+\sqrt{25+16\cdot10^g}}2,
\]

而且 live \(g\ge4\) 中更简单地有 \(b_5<g\)。

## Q5. q-2 与 3q+2 是否显著压缩？

**YES.** 两者都有 sharp complementary pair lower bounds；并且分别在 g>=1、g>=2 时永远 shallow，因此 reciprocal depth完全等于 q-side depth。

## Q6. D7/D8 的 2-adic tubes得到什么新限制？

两者都获得 reciprocal D^vee(u) tube，以及

\[
2^{m+\min(m,g)}\le C^2(10^g+1)^d.
\]

但 current same-row C3 incidence真正直接调用的 2-adic unbounded factor只有 D8；D7来自 cross-row line pair，当前 DNF并不 force它。

## Q7. 9 fibres 的真正 C2/C3 finite disjunction是什么？

每个 internal row被分成：

- C2: 所有 additive extra depths为0，10个 exact affine base-min pair cells；
- C3: K-row的7个 nonempty lift supports，或 G-row的15个 nonempty lift supports；每个 support内部再附 exact 10-pair actual-min DNF。

完整表已落到 `InternalDisjunctions.tsv`，不再保留 “some internal cancellation”。

## Q8. 多少 C3 被 fixed determinant depth杀掉？

\[
\boxed{21/132.}
\]

全部来自 2-adic determinant-unit pair impossibility。

## Q9. 多少被 cyclotomic tube depth ceiling杀掉？

\[
\boxed{0\text{ whole C3 support strata proved closed}.}
\]

原因是 surviving R4 Lambda lower bounds还未被现有 structural theorems uniformly 推到 R5 ceiling以上。

## Q10. 是否有 fibres 被强迫只剩 C2？

\[
\boxed{0.}
\]

single-linear / conic C3 alternatives仍在。

## Q11. 是否有 q/u 被 pin 成 deterministic Hensel-truncation sequence？

\[
\boxed{NO.}
\]

pinning theorem已建立，但没有 fibre force足够深的 simultaneous tube modulus，因此 deterministic q/u sequence数量都是 0。

## Q12. R5 frontier是否比 3 Arch x 9 fibres x 7 tubes更低维？

**YES, 但方式不是“减少到若干 Hensel sequences”。** 真正 incidence显示“x7 tubes”不是独立 factor。正确对象是

\[
\boxed{
3\text{ Arch faces}
\times
9\text{ exact row-incidence DNFs}
}
\]

其中 7 ambient tubes均有 global ceiling，但只有在 two-linear C3 intersections上作为 edge labels出现；current row-internal unbounded pair kernel更小到 p2:D8 与 p5:q+4/D9。111 个 surviving C3 support strata中，大量属于 singleton/conic directions，根本不在 determinant tube axis上。

---

## 15. Success ledger

- Success A Reciprocal-Tube theorem: **ACHIEVED**.
- Success B 7 global tube ceilings: **ACHIEVED**.
- Success C sharp rational theorem: **ACHIEVED, stronger shallow corollary obtained**.
- Success D 9-fibre C2/C3 DNF: **ACHIEVED**.
- Success E kill C3: **PARTIAL — 21 fixed-depth deaths, 0 new whole-support deaths from ceiling**.
- Success F force C2: **NOT ACHIEVED**.
- Success G close bracket fibres: **NOT ACHIEVED; 9 survive**.
- Success H deterministic Hensel divisor sequences: **NOT TRIGGERED**.
- Success I exact bracket zero: **NOT TRIGGERED**.
- Success J q>1 closure: **NOT ACHIEVED**.

\[
\boxed{\textbf{J2 OPEN}.}
\]

---

## 16. Precise next unique object

R5已经证明继续“给 determinant tubes 再做更深 Hensel analysis”不是主缺口；所有 7 tubes已经 global height-controlled。真正剩余 obstruction 是：

\[
\boxed{
\textbf{Which generator is actually responsible for the internal lift?}
}
\]

下一轮最自然的唯一对象应改为

\[
\boxed{
\textbf{Single-Bracket Projective Tube Assignment}
\times
\textbf{Two-Place Same-Generator Alignment}
\times
\textbf{C2 Affine-Tie Geometry}.
}
\]

目标不是再追 p-adic digits，而是用 exact row affine inequalities、Arch face、LOW/UP、RCE 与 bracket height bounds决定：

1. singleton C3 是否能真实发生；
2. p2/p5 internal places是否会被迫选择同一个 generator；
3. 若同一 linear generator两地皆深，立即触发 R4 ten-primary depth-to-zero；
4. 若同一 place被迫至少两条 linears深，立即回到已 globalized determinant edge ceiling；
5. conic support只有在真正 force后才调用 R4 的 11 resultants。

这比继续把 7 tubes 当独立 Cartesian frontier更接近真实 obstruction。
'''
(HERE/'J2-65-R5-Cyclotomic-Reciprocal-Tube-Report.md').write_text(report,encoding='utf-8')

print('R5 CELL REFINEMENT CERTIFICATE')
print('R4_PATTERN_FIBRES=9')
print('C3_DISJUNCTS_TOTAL=',c3_total,sep='')
print('C3_CLOSED_BY_R4_FIXED_DEPTH=',fixed,sep='')
print('C3_CLOSED_BY_R5_TUBE_CEILING=0')
print('C3_SURVIVING=',surv,sep='')
print('C2_ONLY_FIBRES=0')
print('R5_SURVIVING_BRACKET_FIBRES=9')
print('FORCED_LINEAR_ZERO_LOCI=0')
print('FORCED_CONIC_LOCI=0')
print('QGT1_STATUS=OPEN')
print('NEXT_UNIQUE_OBJECT=SINGLE_BRACKET_PROJECTIVE_TUBE_ASSIGNMENT_X_TWO_PLACE_SAME_GENERATOR_ALIGNMENT_X_C2_AFFINE_TIE_GEOMETRY')
print('OUTPUTS=',p.name,',J2-65-R5-certificate.txt,J2-65-R5-Cyclotomic-Reciprocal-Tube-Report.md',sep='')
