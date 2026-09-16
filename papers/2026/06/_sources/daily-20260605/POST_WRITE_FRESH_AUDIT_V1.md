# 2026-06-05 Books Post-write Fresh Audit

**状态：** 通过

恢复候选的独立反例审计形成两项纠正：

- `2606.05169` 从 `Only report` 改判 `No Change — Existing Coverage`；Ch66 的“从‘已见切片均值’到 Blind-spot Mass”与“平均值、切片与不确定性”是 Review notes 前的命题级锚点。
- `2606.06203` 从 `No Change — Existing Coverage` 改判 `Integrate`；Ch22 已在 Review notes 前新增“相同 Token Length 仍可能承载不同 Information Load”。

fresh-context post-write audit 重新读取该段与相邻“生产评估不能只看最大长度”“条件化机制分支与共存边界”：

- **机制链完整：** 旧 length/position/task 切片为何合理 → 固定 token length 下 lexical density 改变关系与事实竞争 → EvalSpec 冻结 density/content structure → density-conditioned quality curve → 数据构造与切片成本 → tokenizer/language/metric 与 task-difficulty 混杂 → 人工任务/内容结构分层 fallback。
- **owner 与 handoff：** `MODEL-LONG-CONTEXT` 拥有 effective-context 能力与评测身份；调度器仍只用 token 数估算显存/计算，不接管质量判断；未与后续稀疏 Attention 机制分支重复。
- **证据边界：** 正文只吸收“固定长度不等于固定 information load”的长期命题，明确不外推到所有模型、语言、硬件、并发或生产 SLO。
- **反例：** 若 lexical-density metric 与任务难度混杂，正文要求回退人工定义的任务/内容结构分层；若只关心资源容量，原 token-length 估算继续成立。

结论：正文写回真实存在、位于顶层 Review notes 之前，语义增量、代价、failure 与 fallback 均可定位。06-05 最终 Books disposition 为 Existing 66 / Only report 4 / Integrate 1，正文缺口 0；Books Gate 通过。
