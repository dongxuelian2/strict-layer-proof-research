# Known Referenced Artifacts Not Archived

以下文件被当前 Strict-Layer 报告明确引用，但本次归档时未能取得可提交的原始字节，因此没有伪造或用摘要替代。

## `strict_layer_backward_exact_root_pair_fibre_campaign.md`

- 后续 `strict_layer_post_DD_consolidation_A1_frontier.md` 等报告明确引用。
- 文件库元数据曾显示该名称，但 raw materialization 返回不可见/不可解析错误。
- 若之后重新取得原文件，应放入 `10-backward-global/`，并更新 `MANIFEST.tsv`。

## `strict_layer_global_reduction_campaign.md`

- 后续 Unified Exact-Lift / SGR 报告引用其作为较早 reduction 节点。
- 本次按精确文件名未检索到独立、可可靠取回的 artifact。
- 未用模糊命中的大型“粘贴 markdown”文件冒充该报告。

## Policy

缺失 artifact 只按“已知引用但当前未归档”登记；仓库不根据后续摘要逆向重构原始文件，以免污染 provenance。
