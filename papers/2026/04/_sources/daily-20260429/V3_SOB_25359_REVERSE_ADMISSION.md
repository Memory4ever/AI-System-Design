# 2604.25359v1 SOB：从潜在评价候选转具名前分母关闭（作者侧）

本项原在旧 60 条题摘的 41 个潜在线索内；重开[官方 exact-v1](https://arxiv.org/html/2604.25359v1) §3–4、§6 Tables 3–6、§7，实际对照 [Ch66 五层成功事件](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)与 [Ch78 parse→schema→semantic/authorization](../../../../../books/part-07-agent/78-tool-calling.md)。这是贡献准入反向核，不以已有章节映射单独排除，也不为前关闭硬追 submitted/DOI created 的单篇日期。

原题摘可能被误认为跨原生文本、视觉、音频的通用结构化输出反证。但 §3 明说 209 个 image 记录输入是 **OCR-rendered markdown**、115 个 audio 记录输入是带 speaker/timestamp 的**文本 transcript**，模型没有看到原始像素或声学波形。因此表 4–6 的 0.830/0.672/0.237 顶部 Value Accuracy 与跨源排名变化，测的是三种**文本来源/格式和任务集**，不能改写原生多模态 encoder 能力排序。5,000 个 text 来自 HotpotQA；image/audio 样本量小且任务/长度/难度分布不同，三组冠军数字不能用作同难度 source-modality 因果差。

§4 的七个指标把 JSON/schema pass、路径覆盖、exact leaf value、soft token-F1 分开，§6 的近高格式合规／较低值准确是可信的受限测量。可是这一分账正是 Ch66 现文 `Contract ≠ Semantic Quality ≠ Outcome`、Ch78 现文 `schema validation → semantic/business validation` 的既有设计边界；该论文未提出新的 verifier authority、可迁移执行条件或会推翻现有合同的受控反证。新数据量与多源榜单本身不足以准入。Table 3 的三模型×115 audio 结构约束实验也不能重写“真正 deterministic grammar 可阻止语法错误”的命题：论文只是把 schema 交 provider enforcement，GPT-5.4 JSON pass 从 0.869 到 0.808、value 从 0.180 到 0.173，未证明后端为同一硬 grammar、也未定位下降机制。保留它为配置敏感的局部负例，不当通用反证。

原文额外限制强化关闭范围：§3 的 exact leaf value 会把语义可接受但措辞不同的值判零；§4 让 schema 失败的 semantic 指标硬归零；§7 承认 text 仅五组百条抽查估约 3% 残余标签错误，gold OCR/transcript 也不是端到端视觉/语音性能。因此本项目所需的“格式合法但值错应另验”已经是稳定原则，本文只在新题集再次观察，**作者侧改为具名前分母关闭**，不评分、不入本日报候选、不写 Books；不是因其为 benchmark 或仅文本输入就机械拒绝。若后续原始受控研究在相同任务/文本内容下隔离 source provenance 或 schema enforcement 引出 Ch66/78 现有合同不能覆盖的新错误机制，再按真实公开事件具名重开。此项待非作者负侧抽样，不能据此宣称日级 Gate。
