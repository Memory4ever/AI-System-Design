# 2025-10-14 首批准入与日期校准包

作者：Euler；root 已实际完成[首批独立校准](FIRST_INDEPENDENT_REVIEW.md)，潜力通过，日期隔离成立；不授 DAY。窗口为 BJT [2025-10-13 09:00, 2025-10-14 09:00)。
已实际读六份精确 v1 的完整题摘与事件页，原响应见 [首批](RAW_FIRST_ABSTRACTS.json) 和 [补齐](RAW_FIRST_ABSTRACTS_TAIL.json)。
以下是潜在贡献，不是已确认落窗候选，不评分、不授 Evidence、不写 Books。

| 身份 | 原文实际增量与待校准理由 | 日期原值与隔离 |
| --- | --- | --- |
| [2510.10481v1](https://arxiv.org/abs/2510.10481v1) UltraLLaDA | dLLM 长上下文不能直接假定 AR RoPE 扩展保持有效；按 diffusion 概率过程修改位置扩展并比较训练 mask，有可能改变长上下文后训练选择。owner 候选 MODEL-LONG-CONTEXT；不是借 128K 数字准入。 | Submitted Sun, 12 Oct 2025 07:26:56 UTC；缺首次公开公告或完全落窗 bounds。 |
| [2510.10618v1](https://arxiv.org/abs/2510.10618v1) Calibration Data Curation | 校准来源/数量不能充分解释压缩后复杂推理保留；以 activation 代表性和多样性组织数据，潜在改变量化校准选择。owner 候选 INFER-TENSORRT-LLM。 | Submitted Sun, 12 Oct 2025 14:00:23 UTC；日期隔离。 |
| [2510.10666v1](https://arxiv.org/abs/2510.10666v1) BrowserAgent | 静态网页转文本限制交互；raw page 动作配 SFT/RFT 与跨步显式记忆，潜在改变浏览工具的观察/动作设计；收益归因未读。owner 候选 AGENT-TOOL-CALLING。 | Submitted Sun, 12 Oct 2025 15:43:37 UTC；v2 Submitted 14 Oct 08:54:57 UTC 已晚于本窗，但不以提交时刻当公开事件；仅 v1 线索。 |
| [2510.10974v1](https://arxiv.org/abs/2510.10974v1) CFT | 统一监督可能压低非关键 token 多样性；反事实扰动识别必要 token，只在所选 token 位置施加监督，潜在改变 SFT 与后续 RL 初始化。少于12%监督 token 不等于仅更新12%参数或训练成本下降。owner 候选 TRAIN-SFT。 | Submitted Mon, 13 Oct 2025 03:25:36 UTC，仅证明提交下界，不冒充首公开时刻。 |
| [2510.11001v1](https://arxiv.org/abs/2510.11001v1) DND | 给难 token 路由回当前层重复处理，router 控制损失和阈值控制选择；即使两个模型增益局部，也可能提供动态深度替代设计。owner 候选 MODEL-TRANSFORMER-LAYER。 | Submitted Mon, 13 Oct 2025 04:22:57 UTC；v2/v3 窗外，不把当前版改进带回 v1。 |
| [2510.11052v1](https://arxiv.org/abs/2510.11052v1) LRD | diffusion 解码丢弃未最终化分布和过早 commit；保留预测 token/mask 混合 belief 并反馈，再最终化高置信 token，潜在改变生成路径。owner 候选 MULTIMODAL-GENERATIVE-PARADIGMS。 | Submitted Mon, 13 Oct 2025 06:38:13 UTC；v2 窗外；日期隔离。 |

首批代表范围排除：官方 CL 列表 2510.10474 消费平台参与行为、2510.10475 医疗医嘱抽取、2510.10776 Hiligaynon NER、2510.10951 treebank binarization。标题已明确是领域应用/传统 NLP，不与大模型形成及系统主线建立机制差额；未将其当日期确认项，未作证据审阅。

检查点：不以小模型、局部收益、已有 owner 排除上面六项；不以主线映射或成熟原则给分。后续安全/反侧仍须读必要 core；当前校准不代表整个来源或整日报验收。
