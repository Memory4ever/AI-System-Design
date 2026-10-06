# 2025-07-04 独立初筛与停止记录

执行窗：2025-07-03T09:00:00+08:00 ～ 2025-07-04T09:00:00+08:00。检查于 2026-10-07；仅本窗判断。

## 题摘读取与贡献判断

八项精确版本的完整题名、摘要、身份、comments、submission history 原值保存在 [precise-abstracts.json](./precise-abstracts.json)。摘要不是证据审阅，不采用作者宣传数字。当前官方事件页未看到撤回标记；后来的普通版本存在不构成本窗重要修订依据，未遍历完整版本正文。

| 精确材料 | 原有约束 → 实际增量 → 需要重考虑的选择 | 处置 |
| --- | --- | --- |
| [ABC 2507.02825v1](https://arxiv.org/abs/2507.02825v1) | 将结果匹配视为真实任务成功 → 检查出空响应通过等任务/结果有效性漏洞 → Agent 成功率需依赖判定器与任务可解性的独立检查 | 潜在贡献清楚；firstpublic 未确认，保留而非评分候选 |
| [DeSTA2.5 2507.02768v1](https://arxiv.org/abs/2507.02768v1) | 外部音频指令监督可能损伤原语言能力 → 用骨干自生成训练目标做跨模态对齐 → 重新考虑监督分布与能力保留的关系 | 同上 |
| [AsyncFlow 2507.01663v1](https://arxiv.org/abs/2507.01663v1) | RL 阶段分离后存在复杂数据依赖与空转 → 流式细粒度数据管理及 staleness 阈值内延后参数更新 → 重新考虑任务重叠与策略陈旧的约束 | 同上；不是因采用 producer-consumer 的成熟名字准入 |
| [LogitSpec 2507.01449v1](https://arxiv.org/abs/2507.01449v1) | 纯历史匹配无法找到准确草稿 → 用最后 logit 猜测 next-next token 并扩大双 token 检索 → 改变无独立 draft 模型的候选检索范围 | 同上；加速收益尚未审阅 |
| [EBT 2507.02092v1](https://arxiv.org/abs/2507.02092v1) | 推理加算力依赖特定模态/外部验证监督 → 学习输入与候选的能量并用梯度最小化求预测 → 重新考虑预测算子与推理迭代的统一设计 | 同上；不得照录更优 scaling 结论 |
| [REG 2507.01467v1](https://arxiv.org/abs/2507.01467v1) | REPA 外部表示对齐不参与推理过程 → 联合去噪图像 latent 与高层语义 class token → 重新考虑判别表示仅作训练辅助或进入生成状态的区别 | 同上；准确简称 REG，不是 REPA-E |
| [GPI 2410.00903v3](https://arxiv.org/abs/2410.00903v3) | 利用 LLM 内部表示做文本处理的因果估计，贡献是识别/估计条件与统计推断，不改变模型训练、推理或 Agent 系统机制 | 当前项目范围关闭；公开日期未核实，不为此另请求日期 |
| [Posterior Transition 2507.02391v1](https://arxiv.org/abs/2507.02391v1) | 近似likelihood score需guidance超参数 → 直接构建条件reverse transition，先验/观测整合去掉超参数，另一分支给exact likelihood score → 可能改变条件采样有效性假设，但须核原观测模型假设 | 按root校准改为潜在贡献清楚、日期保留；不泛化到所有多模态生成 |

FIRST 独立校准：root 首先检查 ABC、DeSTA 两项拟保留与 GPI、Posterior Transition 两项代表关闭；后续独立读完整8份精确题摘，认可7项潜在方向及GPI范围关闭。依据PTM直接建立条件reverse transition的具体机制，改正先前仅按去噪逆问题范围关闭的误判，将其恢复为日期保留；不是泛化所有逆采样理论。全部数字及普适保证未采用。未把“已有章可映射”用作准入依据。

ABC 曾定点打开 v1 HTML 的 Introduction/Overview/§4 起始，澄清具体判定器漏洞而非只是一份术语清单。此为贡献澄清；未完成 §5 实验/附录反证审阅，不算深入完成。其余七项没有开展新全文审阅。已停止新增论文池。

## 有界查漏

[topic-title-discovery.json](./topic-title-discovery.json) 保存四组 API 原查询、总结果与实际首 20 标题：模型 52、训练 49、推理/Agent 65、多模态 51 是两天 submitted 范围的 API 总量，彼此重叠且不是当窗新事件数量。实际读取 80 次标题、72 个去重身份；仅作有界发现，不形成逐项题摘队列或关闭清单。

查询覆盖 cs.CL/cs.LG、cs.DC、cs.AI/cs.IR/cs.MA、cs.CV/cs.RO；实际关键词和停止 start=0/max_results=20 见原文件。搜索的原 published 字段是 submitted，不是 firstpublic。API 含不匹配主题及后来更新标题，不能支撑完整题摘筛选或首公开批次。未覆盖各主题后续页、官方历史分类公开标题补检。DAY反馈后补做 cs.AR/cs.PL/cs.OS/cs.PF 硬件/编译/runtime主题一次首20标题请求，20秒读取超时，见[DAY恢复](./DAY-RECOVERY.md)及原请求；不得把访问失败写成零。重开限定可读主题响应或历史公告，不扩为全分类队列。

[initial-search.json](./initial-search.json) 保存模型/推理/Agent/diffusion 的 Jul3 发现搜索；搜索会漂移到镜像与无关项，不作为证据。[author-date-search.json](./author-date-search.json) 是四项具体作者/项目公告定点搜索；仅找到后日 RFC、非作者的日级汇编等，不证明六项 firstpublic。未扫描该 RFC 的 release 或历年材料。

## 日期请求与停止

为七项合并请求：每项准确 v1 首次公开正文的官方历史公告/作者原始公开证明，含时区和可将事件完全放入或排除本窗的时间精度。具体身份与原始 submitted 原值见报告 §5。本月已知不可得的历史公告、schedule、OAI/DataCite 路径不再重复检索。submitted + 常规排期不组成公开事实。

收到原件后仅重开受影响身份：先确认日期；落窗才进入候选评分与标准/深入证据审阅、owner 对照及 Books 决定。窗外恢复到真实归属日，不按本日发现移动日期。当前七项都不支持本窗正面结论、Books 写入、性能或无事件保证。
