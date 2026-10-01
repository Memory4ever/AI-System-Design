# 2604.15663v1 CodeMMR：跨模态代码检索的方向与负载边界

作者 `apr20_resume`。原完整题摘表将本篇以“成熟 shared embedding/RAG 迁移到五域、无新选择边界”拟前关闭。否定侧成熟组合层抽检定点读[官方 exact-v1](https://arxiv.org/html/2604.15663v1) §4.1–4.2/Tables 2–3、§6–7 后，发现该概括遗漏了**同一图像↔代码检索在方向、结构长度、未见任务上的不同失败条件**，暂撤销前关闭，交非作者按当前§3有界准入；不先列正式候选。

后续状态：[root 有界非作者核](./V3_ROOT_15663_FINITE_INDEPENDENT.md)已通过 `2+1+2=5` 标准／仅报告及 Ch76 实际责任对照；具名[首次公开联合链](./V3_DATE_RECONCILIATION.md)、本日正式 §3–4 已同步。上一段“待核”只记录提案时状态；整日 Gate 尚未完成。

MMCoIR 把截图、图表、SVG、示意图、UML 对应的自然语言/代码/图像请求与返回对象作为不同 typed retrieval 任务；§4.2 的 `text+code→image`、`text+image→code` 等 ChartEdit/DiagramGen 组合被明确作为未在训练集出现的设置。Table 2 中 CodeMMR 2B 在 WebUI 与 UML 的部分 Hit@1 极高，却在 SVG 若干 image→code 列仅个位/十几；§6 明言长且组合性的 SVG 映射比反方向更难。Table 3 的未见任务与草图还有明显退步。故“统一 embedding 平均 nDCG”不能替代按 query/return 模态、代码结构长度和 corpus 任务分层验收；这对 coding-agent 或多模态 RAG 选择单一共享索引还是 typed operator 有局部影响。实际[Ch76](../../../../../books/part-07-agent/76-rag.md) 已要求 heterogeneous corpus 的 typed query/operator、证据 identity、retriever 与最终生成效果分账；本篇不改长期 owner，但受限方向性反证不应仅因用了成熟 embedding 就在贡献前关闭。

§7 在两个 image→code 生成任务中把 No RAG、GME 与 CodeMMR 对同一 backbone 比较；ChartMimic Direct 的平均 Execution Rate 相对无检索 +10 点、WebCode2M-Mid Visual Accuracy +9.4 点，但两个下游任务和训练子集检索并不证明所有编码任务/生产仓库改善，也不能把训练语料、模型、retriever 成本当匹配无关。Table 2/3 还有 SVG/草图反证，未提供完整 corpus/index 更新、ACL、精度、时延/SLO/CI。作者只拟 `2+1+2=5` 标准、`Only`，不采“统一 embedding 普遍跨代码与视觉泛化”或将 benchmark 平均提升写入 Books。请非作者只核题摘/§4.2 typed 任务、Table 2/3 的方向反证、§7 两个下游对照和 Ch76 现有具体命题；若认为成熟组合仍可前闭，请以具体已有分层证据而非“可映射 RAG/已有 embedding”作否定。
