# 2025-10-14 有限筛选与采用边界

作者 Euler。本文件记录判断，不是 raw 下载收据或独立复核。确认落窗候选0，正式证据审阅完成0，Books提案0。首批六项潜力由root独立校准通过，日期仍隔离，见 FIRST_INDEPENDENT_REVIEW.md。

## 范围与停止

arXiv 正确发现范围 submittedDate=[202510110000 TO 202510132359]，只用于恢复可能在周末提交、周一公开的线索，不能证明公开事件落窗。五组 start=0 返回 DC5/model70/multimodal21/runtime4/agent67，共167个标题出现次数，跨组未作全量家族统计，绝不是167份本日论文或全文队列。原响应为 arxiv-*-corrected.xml。DC限定GPU/inference/training；model限定Transformer/diffusion/calibration/MoE/alignment；CV/RO限定world model/vision language/VLA/video generation；AR/PL/OS/PF限定GPU/kernel/compiler/Transformer/inference/language model；AI/IR/MA限定RAG/agent/memory/tool calling。model与agent仍混入领域或传统学习研究，只作查漏标题，按foundation model实际机制收窄后选择下列题摘，不逐项关闭库存。

官方CL历史标题补检实际打开 skip700、800、900；700/900仅日期定位时可见部分，800/show100实际801～884标题。这些不是整个分类的筛选完成声明。LG/CV skip600/show25、AR/IR skip0/show25补检失败；历史day list也失败，保留缺口。不因月列表可读把整类变成队列。编码错误的初返回上界为2510132359，已停止使用；不由错误宽池产生覆盖或全文工作量。

## 完整题摘与潜力

以下共29个独立家族，其中28个arXiv精确v1与Meta官方SPG摘要。前六项见 FIRST_CALIBRATION.md；新增23项只保留可核验的实际增量，不评分、不授正面Evidence。除SPG官方日名外，均只有提交字段，未有首次公开公告或完全落窗bounds。恢复条件统一为官方历史发布记录/可靠原始公告或完全落窗的上下界；收到后只重开具体家族，不重扫库存。下列 arXiv ID 链接均为 https://arxiv.org/abs/<ID>v1。

| 身份 | 原文实际潜力与限制 |
| --- | --- |
| 2510.10457 EssenceBench | 子集重构与排名一致性评价，遗传搜索粗细两阶段；可能改变小评测集可信度判断，不采用25x为普遍收益。 |
| 2510.10539 AuthenHallu | 检测LLM/人类来源的真实性与诱发幻觉的差别，可暴露评价目标混淆。 |
| 2510.10677 ConsistentGuard | 失败语言样本与成功语言anchor配对，CAO及KL约束；3B/1000样本/六语言不自动外推通用安全。 |
| 2510.10846 DUAL-Bench | 固定Describe-the-image良性任务与含有危险内容的图像，分别检查有用安全完成与拒答；评价协议不是运行安全保证。 |
| 2510.10994 DeepResearchGuard | 严重度3终止、1/2修复，加记忆升级与人审阈值；各步骤收益和代价尚未作受控核验。 |
| 2510.11238 Attacks by Content | 区分数据内容攻击与指令攻击，提出真实性核实缺口；position paper不当实现有效性证据。 |
| 2510.11288 EM-ICL | 窄风险示例通过条件上下文诱发跨任务失配；abs标称3数据集/3模型，HTML标称v1写4/4，内容身份未一致，不采用实验结论。 |
| Meta SPG | 官方Oct13完整摘要以log-likelihood上下界修正masked diffusion policy gradient；日名时区不明，arXiv09541v1恢复失败。 |
| 2510.10620 DCP | 随序列/attention负载划分数据与计算block并映射设备，具体动态并行替代；attention微基准与端到端0.94～1.16x不可混为统一加速。 |
| 2510.10932 TabVLA | 视觉语言动作模型的攻击目标、注入步与episode边界；精确v1名称TabVLA，不能继承latest DropVLA内容。 |
| 2510.10085 Pharmacist | 有毒LoRA的双层目标及近似优化，参数增量的安全边界；所述pass数与列举不一致，不采用效率数字。 |
| 2510.11235 AI Alignment / Shared Failures | 模块失败相关性使独立假设失效；玩具风险概率不是实际部署事故率。 |
| 2510.11195 RAG-Pull | 检索几何与Unicode扰动下的内容污染，威胁目标与可见输入区分；v1 Imperceptible Attacks与latest标题不得混用。 |
| 2510.10931 PoU | 输出和检索证据ID建立显式关联并奖励其形式；形式关联不能证明因果使用或答案真值。 |
| 2510.10302 SP-MoE | 读取完整v1摘要后的稀疏专家训练/通信线索；仍需公开时间及具体对照，不因端侧或局部负载排除。 |
| 2511.11585 FedGenEdge | 已读v1完整摘要，跨设备模型学习线索；当前Atom时间与ID月份不一致，ID月份或注册时间均不能给首公开定时。 |
| 2510.11211 Explorative DC | 完整v1摘要有metaheuristic调度提议，决定机制增量仍需定点定义；不因概述性写法或领域标签直接排除。日期先隔离。 |
| 2510.13842 ADMIT | 可信上下文下仍可污染决策，是信任输入仍需验证的反侧；未把intro当完整方法/实验。 |
| 2510.11108 AAC | 外部推理器/集成的概念框架，原文保留未来benchmark与挑战；不当已实现安全架构。 |
| 2510.10185 MedAgentAudit | 3600轨迹日志、300试标注及两标注者，对最终正确率之外的推理失效作审计；不采用临床安全结论。v1与latest标题/体积不同。 |
| 2510.10460 Testing and Enhancing MAS | 对代码与计划施加语义扰动及多次测试fitness，可能修正多Agent终值评价；不能继承latest改名版本。 |
| 2510.11370 MiMo R3 | 记录rollout路由并训练重放，针对同条件重复forward专家选择不同及训练/推理失配；不借通用off-policy原则评分，官方Oct21索引不证明其首次公开只在Oct21。 |
| 2510.10028 UAV VLM serving | root实际完整v1题摘及HTML I L81–108辨识实测resolution→accuracy/runtime/payload lookup参与多用户VLM服务资源分配；原离线奖励/领域标签误排撤销，仅恢复此家族。Submitted 2025-10-11T05:11:21Z不等first-public，2026-06-07 v2不倒灌；局部收益未采用。原件ROOT-UAV-exact-v1.json，独立判断见FINAL。 |

实际完整题摘响应：RAW_FIRST_ABSTRACTS、RAW_FIRST_ABSTRACTS_TAIL、RAW_SECOND_ABSTRACTS、RAW_SAFETY_IDENTITY_FINAL、RAW_COUNTEREVIDENCE_IDENTITY、RAW_AUTHOR_CLOSE_RECOVERY，以及DC五项的官方Atom。此列不是“全部raw已读”声明。

## 必要反侧读取

RAW_SAFETY_CORE_C：DRGuard §3.1～3.3；DUAL §3.1～3.4；ConsistentGuard §2.3/§3；Attacks-by-Content威胁区分；EM-ICL §3。RAW_SAFETY_CORE_D/E：TabVLA §III-B；Pharmacist §III-B；Shared-failures §3.2；RAG-Pull威胁模型；PoU §3.1.3～3.2。RAW_COUNTEREVIDENCE_FINAL：ADMIT intro/core，AAC §4～5，MedAgentAudit §3.1～3.2，Testing-MAS §4.1。只读影响拟采用命题的必要段，没有复现或正式Evidence完成声明。后续日期恢复且正式准入后，需按具体命题继续方法/实验、直接反证与owner比较。

## 有界贡献排除

- OpenAI/Broadcom：官方核心及RSS实际读取；10GW、2026下半年至2029计划、Ethernet选型，没有披露设计机制或受控效益，合作事实不构成长久机制增量，不评分。
- Kimi CLI 0.28（2025-10-13）：官方changelog该段实际读取，/init生成AGENTS、/clear清context、ReadFile输出修复；未提供新的状态机制、可靠性条件或改变已采用判断的纠错证据，操作入口新增本身不足准入。日期日名未核精确时刻，但不为已明确贡献排除另建时间请求。
- ERNIE v1.4（2025-10）：官方Recent updates的VL训练支持、padding-free pack说明实际读取；仅月精度，未披露packing机制的新条件或比较。作为版本能力事实关闭贡献筛选，不将它说成Books已有覆盖，也不把后续修复倒灌本日。
- DC的2510.10028原按UAV轨迹/离线奖励范围关闭的理由撤销，改为上表第29日期潜力；不是因看见领域应用就排除服务质量/资源增量。仅重开此具体误排，不重跑无关库存。
- 首批四项CL原排除见FIRST_CALIBRATION；root DAY实际完整AB核10474/10475支持领域应用排除，10776/10951访问Cache miss，未称4/4全核；独立范围见ROOT-exclusion-samples.json与FINAL_INDEPENDENT_REVIEW.md。

## Google有限恢复与写后停点

root本日实际定点正确`https://research.google/pubs/?category=2025&search=language%20model`：curl20秒exit28超时、web不可读，停止两次尝试。原year参数失败不当正确过滤执行，其他日成功不授本日历史覆盖；原失败见ROOT-google-corrected-web.json、真实执行记录见FINAL。此缺口终态隔离，得到官方可核本窗主题历史段后仅补该源，不由Blog替代或转全年37项等宽目录全文队列。

首批六项已通过。root DAY三处窄同步现已写入报告/本文件/CURRENT_STOP，尚待root写后确认，作者不标完成。29日期潜力与内容身份/目录保留项不支持正面Evidence、Books、无遗漏或安全性能保证；普通扫描/必要反侧待办0，无Books提案/实际写入。

## SongGeneration原身份

官方HF当前card搜索能恢复Code为 tencent-ailab/songgeneration，不采用fork日期。原官方GitHub返回404；官方HF blob返回401，resolve原件请求20秒超时。当前原身份关联可恢复，但必要原card历史/版本变更及首次公開时间仍不可读。不得由fork Oct13声明、当前长度/显存对比或search摘要推断本窗release或机制。重开位置仅官方原repo/card对应历史提交；不扩全组织。失败原响应与真实请求为 RAW_AUTHOR_CLOSE_RECOVERY.json、songgeneration-readme.md.request.json。
