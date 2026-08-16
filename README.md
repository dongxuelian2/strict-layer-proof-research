# Strict Layer Proof Research Archive

三项十进制拼接平方和问题（three-term decimal-concatenation square-sum problem）的 **Strict Layer / 严格层** 证明研究档案。

本仓库整理截至 **2026-08-16 (Asia/Tokyo)** 已形成的严格层主证明链、DD closure、A1 正/反向研究报告、状态快照与少量终端计算输出。目标是保留 theorem provenance 与研究演化，而不是把历史失败路线抹平后只留一份“最终稿”。

## 当前证明状态

- **DD：closed**，当前 Strict-Layer 主链中作为 `DD = ∅` 使用。
- **A1：open**。
- 因此 **Strict Layer 尚未 closed**。
- 最新正向报告 `strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md` 已把剩余正向 frontier 压到 **两个 explicit active-face successor cases**，并建立
  `DES / Iterated Smith -> exact radial gap -> common-U successor interval`
  的精确桥；尚缺的是两类 successor interval 的统一排除。
- 若要求 DD closure 对旧 External Exact-Lift 完全独立，`strict_layer_DD_independence_audit.md` 目前把遗留依赖压缩为一个 minimal terminal-height localization lemma（LH）。这不改变当前研究链中 `DD = ∅` 的 operational status，但应保留 provenance 区分。

## 原问题

设

\[
A=\operatorname{concat}(a_1,a_2,a_3),\qquad
B=\operatorname{concat}(b_1,b_2,b_3),
\]

其中 `a_i,b_i` 为正整数且逐项既约：

\[
\gcd(a_i,b_i)=1\quad(i=1,2,3).
\]

研究

\[
\left(\frac{a_1}{b_1}\right)^2+
\left(\frac{a_2}{b_2}\right)^2+
\left(\frac{a_3}{b_3}\right)^2
=
\left(\frac{A}{B}\right)^2.
\]

本仓库只聚焦其中的 **Strict Layer** 证明工作；Critical Layer 的专门 O/G/Q 研究不作为本仓库主体。

## 目录

- `00-foundation/`：全局已证结果、早期严格层报告、Exact-Lift synthesis、统一 Exact-Lift。
- `10-backward-global/`：Backward Strict Layer 的总体 obstruction / witness gluing / canonical synchronization / denominator-algebraic interface。
- `20-DD/`：DD 从 error closure、post-deflation、phase/source orientation 到 oriented-tail closure，以及 independence audit 与 post-DD consolidation。
- `30-A1-forward/`：A1 正向主线，从 moving-core / decimal translation 一路到 Smith / common-U / radial successor。
- `40-A1-backward/`：A1 反向主线，从 exact word recovery 到 5-phase、same-cut norm excess、2x5 synchronization、common-U pullback。
- `50-state-and-computation/`：关键状态快照和 radial-gate scan 输出。
- `MISSING_ARTIFACTS.md`：已被后续报告引用、但当前无法从文件库取回原始字节的材料。
- `MANIFEST.tsv`：仓库文件路径、字节数、SHA-256。

## 推荐阅读顺序

1. `00-foundation/proved_results_report_v2.md` / `proved_results_report_v3.md` 与索引；
2. `00-foundation/audit_response.md`；
3. `00-foundation/strict_layer_round1.md`；
4. `00-foundation/strict_layer_final_campaign.md`；
5. `00-foundation/exact_lift_research_synthesis_2026-08-10.md`；
6. `00-foundation/strict_layer_unified_exact_lift_campaign.md`；
7. `10-backward-global/` 的总体反向架构；
8. `20-DD/` 按证明推进顺序阅读，直到 `strict_layer_DD_independence_audit.md`；
9. `20-DD/strict_layer_post_DD_consolidation_A1_frontier.md`；
10. `30-A1-forward/` 与 `40-A1-backward/` 按日期交叉阅读；
11. 最后阅读：
   - `30-A1-forward/strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md`
   - `30-A1-forward/strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md`
   - `30-A1-forward/strict_layer_A1_iterated_smith_coprime_radial_exclusion_campaign.md`
   - `50-state-and-computation/strict_layer_A1_SRCU_state_after_campaign.md`

## A1 正向压缩链（当前）

概念上目前的正向压缩可以概括为：

```text
A1 huge Exact-Lift state
  -> moving primitive core
  -> decimal translation line
  -> flat locus eliminated (a != 0)
  -> primitive-defect synchronization
  -> synchronized primitive conic
  -> common integer radial scale U
  -> moving-profile reduction
  -> exact mantissa / defect quotient
  -> Double Euclidean Word Synchronization
  -> Iterated Smith / gcd allocation
  -> exact Smith-radial gap identities
  -> two active-face V-unit successor exclusions   [OPEN]
```

## 文件保真与版本处理

材料来自当前项目的 ChatGPT File Library / 会话附件。正式命名的 `strict_layer_*` 报告优先纳入；重复的“粘贴的 markdown”中间副本未进入主仓库。

`strict_layer_unified_exact_lift_campaign.md` 在文件库中存在多个修订版本。本仓库将较晚取得、内容更完整的 `(1)` 版本放在 canonical 路径：

`00-foundation/strict_layer_unified_exact_lift_campaign.md`

较早版本原字节保留为：

`00-foundation/archive/strict_layer_unified_exact_lift_campaign_initial.md`

除这一文件名归档处理外，研究报告主体均按取回的原始内容保存。

## 状态标记原则

本仓库区分：

- **PROVED / CLOSED**：报告内已给出并被后续主链冻结使用；
- **OPEN**：尚缺统一证明；
- **HEURISTIC / FAILED**：探索性或已被反例/审计否定的路线；
- **LEGACY-DEPENDENT**：结论当前仍需某个更早来源节点；
- **COMPUTATIONAL TRACE**：用于发现或核对，不自动升级为理论证明。

历史报告中的状态以其产生时点为准，因此早期文件写“Strict Layer open”并不与后续 DD closure 冲突；判断当前状态应以最新 consolidation / state / terminal reports 为准。
