# 2026-02-09 有限筛选说明

只维护本窗实际相关身份，不把宽搜索/当前目录逐项变成队列。首批准入及普通负侧已由 root 独立校准，后续日级验收另见 README §6。

| 身份 | 已读内容/依据 | 贡献处置 |
| --- | --- | --- |
| [kimi-agent-sdk #84](https://github.com/MoonshotAI/kimi-agent-sdk/issues/84) | 完整issue核心、配置占位例、环境、CLI反侧、API created_at秒精度；stage5_0及stage9_0 | 明确目标绑定安全信号，入选；仅报告未确证观察，不能定位模型/Host/dispatch原因或授安全保证 |
| [kimi-cli #1041](https://github.com/MoonshotAI/kimi-cli/issues/1041)，转discussion #1045 | [stage2_3](./feb09_stage2_3.txt) 原始核心约1250–1323：1.9.0、Darwin25.2、hanshi.tech、一天前内容、自称复现步骤；未有response、header或对照 | 有正确性信号但没有新机制/有效性边界证据，只重述成熟freshness需求，贡献前关闭；root已独立实际核此原位置 |
| [kimi-cli #1042](https://github.com/MoonshotAI/kimi-cli/issues/1042) subagentes / Context | stage2_3原1340–1408，完整功能说明；希望不同context和指令的subagent，无实际执行/评价 | 建议而非原文实际机制增量，关闭 |
| [kimi-cli #1053](https://github.com/MoonshotAI/kimi-cli/issues/1053) Auto-generated session titles | stage2_3原1145–1224，完整问题/步骤/两可选解决建议；/yolo导致标题不能区分 | UI标题质量及未实现建议，不支持状态/权限机制变化，关闭 |
| [Protenix-v1](https://github.com/bytedance/Protenix/blob/main/docs/PTX_V1_Technical_Report_202602042356.pdf) | [stage8_1](./feb09_stage8_1.txt)：Seed id1610，题名为biomolecular structure prediction，ResearchArea/WorkingTeam AIforScience；标题已明确范围 | AI for Science 暂停，关闭；无需为不影响处置的日标签恢复时刻 |
| [How AI trained on birds is surfacing underwater mysteries](https://research.google/blog/how-ai-trained-on-birds-is-surfacing-underwater-mysteries/) | [月索引](./feb09_google_native_slice.txt) Feb09标签与[原文核心](./feb09_google_scope_originals.txt)；将鸟声模型用于水下bioacoustics | 科学应用/领域迁移暂缓范围，关闭；不借embedding owner重新引入 |
| [Accelerating Mathematical and Scientific Discovery with Gemini Deep Think](https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/) | DeepMind page4 Jan/Feb当前切片和原文明确科研发现；不是通用新模型机制论文 | AI for Science 暂停，关闭，不以领域指标或泛化Agent词语准入 |
| [SAGE 2602.08354v1](https://arxiv.org/abs/2602.08354v1) | 完整v1 AB+Submitted history，Seed id1608目录字段；stage8_1与stage9_0 | 长CoT冗余约束→SAGE采样/混合groupRL原文潜在增量→停止/预算设计可能变化；必要首公开日期未知，隔离不评分不授准入，不因后续深审成本关闭 |

当前机构目录中的其他明确窗外卡片只用于夹窗/停止，不称“重复已审”；旧论文搜索与论坛观点只作发现线索。Anthropic zero-days原页Feb06作者列表更正窗前；不把当前后加说明倒填成Feb08事件，也不沿所有revision差异展开。
