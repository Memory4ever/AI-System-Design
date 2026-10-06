# 2025-11-20 arXiv 窄主题首批校准

作者 Dalton。完整exact-v1题摘已实际逐项读取，原始 [arxiv_batch_v1.xml](arxiv_batch_v1.xml) 含14份完整标题、摘要与原日期字段，不是改写摘要。以下是待独立校准的潜在方向，不是14个确定当窗候选、不评分、不授Evidence/Books。仅已明白的潜在贡献继续；未确认落窗前不把每项展开全实验/owner。

## 入口与实际停止

所有实际query/start/max_results/sort在各XML同名receipt中保留。初查 [system](arxiv_system_p0.xml) 13条全部标题、[agent](arxiv_agent_p0.xml)22条全部标题；[learning](arxiv_learning_p0.xml)总107只读首25标题、[multimodal](arxiv_multimodal_p0.xml)总45只读首25标题后停止，因应用噪声收窄。learning改为LLM限定及Nov18切片 [narrow](arxiv_learning_narrow.xml)44条只首25，多模态 [narrow](arxiv_multimodal_narrow.xml)22条只作相关标题线索。不是把107/45/44条变为全量题摘关闭队列；进一步pre-training/优化稳定性/理论表达focus仍普通待办。

选14个身份的依据是TP故障/状态恢复、分层训练内存、partition/scheduling耦合、同步RL rollout、预训优化/概率行为、VLA动作生成及交互训练、生成表示塌缩、语义路径检索和有待辨明的新runtime hook。传统医学、语料情感分类、纯领域科学应用标题没有转全文队列；不能按神经生物、电影或小模型名称自动排除通用模型机制。跨查询去重后精确下载14个v1，不把搜索当前v2/v3/v5回填旧事件。

## 14项准入命题与最小核验

| exact-v1身份 | 旧约束 → 实际潜在增量 → 需重考虑的选择 | 最小核验与非采用边界 |
| --- | --- | --- |
| [2511.14116 FailSafe](https://arxiv.org/abs/2511.14116v1) | TP紧耦合单GPU失效使KV重算/残余设备失衡 → cyclic KV placement、hybrid attention、backup与按需权重恢复 → 失效后不只全组重启 | 恢复状态正确性与备份成本、可比故障trace；不只采用2×/两个数量级数字 |
| [2511.14124 10Cache](https://arxiv.org/abs/2511.14124v1) | GPU/CPU/NVMe offload迁移等待及buffer碎片 → tensor顺序profile和尺寸分布驱动pinned buffer分配/复用 → prefetch与内存预算耦合 | 若只是成熟prefetch原则不够，核尺寸分布分配/复用真实差额与端到端对照；不采86.6×宣传 |
| [2511.14450 Hyperion](https://arxiv.org/abs/2511.14450v1) | 跨tier partition与实时队列相互抵消 → 慢尺度BSDP partition与快尺度ARTS调度 → 静态划分何时需实时负载修正 | 控制异构带宽、memory及比较的调度预算；小Phi模型不自动排除，未证明所有云推理更优 |
| [2511.14617 Seer](https://arxiv.org/abs/2511.14617v1) | 同步RL被rollout长尾阻塞 → 同prompt输出长度/生成模式关联驱动分段rollout、context调度与group speculation → prompt组统计是否可调度 | 核同prompt关联及各组件对照、额外profile/speculator成本；不把rollout收益直接写完整训练收益 |
| [2511.14721 AdamHD](https://arxiv.org/abs/2511.14721v1) | 二次weight decay对大权重压力 → decoupled smooth Huber decay的分段更新 → regularizer梯度边界可改变训练选择 | 原文将参数regularization与极端梯度联系，须核推导假设，不能照搬“抵抗outlier gradient”因果；小模型/理论可准入 |
| [2511.14630 Failure to Mix](https://arxiv.org/abs/2511.14630v1) | 提示目标概率分布并不保证随机执行 → 二元分布请求出现近阶跃输出的局部负证据 → 概率指令遵循与采样实现分账 | 开篇科学动机不使后续通用LM概率实验自动退出；核temperature/重复样本/统计范围，不证明RL是原因或所有模型失效 |
| [2511.14759 pi-star-0.6](https://arxiv.org/abs/2511.14759v1) | 部署经验与专家纠正来源异质 → advantage-conditioned RECAP把demonstration/on-policy/intervention纳入VLA更新 → 如何使用纠正而非只模仿 | reward/advantage来源、专家介入和独立任务人口；不将真实场景演示当自治安全保证 |
| [2511.14659 NORA-1.5](https://arxiv.org/abs/2511.14659v1) | VLA架构改进和posttrain奖励收益混杂 → action-conditioned WM及GT偏离分别构造偏好后DPO → imagined goal reward可信范围 | 分离action expert架构收益与reward收益、WM误差；不称WM分数即物理事实 |
| [2511.14148 AsyncVLA](https://arxiv.org/abs/2511.14148v1) | 同步FM统一时间表难局部纠错 → 非均匀action-token schedule与confidence选择执行前修正 → 哪些token需重算/何时commit | confidence资格、纠错消融、KV复用与时延成本；不外推执行后闭环纠错 |
| [2511.14716 Diffusion As Self-Distillation](https://arxiv.org/abs/2511.14716v1) | encoder/decoder/diffusion朴素联合训练latent collapse → self-distillation解释及修改objective稳定latent → 何时可共享单网络训练 | 核塌缩反证、目标/梯度处理与预算；不按单网络名称或FID自动采纳 |
| [2511.14096 NeuroPath](https://arxiv.org/abs/2511.14096v1) | graph-RAG节点匹配污染语义路径 → goal-directed路径剪枝与基于中间推理的completion → noise控制与补召回取舍 | 路径机制而非神经生物类比，核recall与token预算可比、剪枝漏召回；小模型不排除 |
| [2511.14460 Agent-R1](https://arxiv.org/abs/2511.14460v1) | 多轮trajectory含工具反馈，loss mask不等于advantage alignment → 两种mask分离及局部消融 → 环境token如何影响credit | 摘要仅MDP/framework不足，已定点读§3.2/4.3确认真实差额；PPO逐步移除是非全因子消融，GRPO未独立ablate advantage，不作普遍机理 |
| [2511.14299 DataSage](https://arxiv.org/abs/2511.14299v1) | 代码修正可能引入新错 → 保留各code/insight版本给final judge回选 → 非单调修正是否需要checkpoint选择 | 仅retrieval+debate+multi-path组合不准入；决定性§3.5真实hook已读，需核是否有回选必要证据。可被校准关闭，不把组合提分/G-Eval当机理 |
| [2511.14249 Authentic-Dubber](https://arxiv.org/abs/2511.14249v1) | emotion/timbre/lipsync条件对齐不足 → emotion-similarity跨模态检索与progressive graph条件生成 → 情绪参考怎样改变speech生成 | 电影角色模拟/场景指标本身不足；摘要已指实际表示/条件生成潜力，最小核其训练路径与条件消融，不预称通用speech基础模型突破 |

Agent-R1决定性核心见 [WEB_NARROW_ANCHOR_AND_CORE.json](WEB_NARROW_ANCHOR_AND_CORE.json) L166–184/217–228；DataSage见 [WEB_DATASAGE_ADMISSION_CORE.json](WEB_DATASAGE_ADMISSION_CORE.json) L133–164/209–231。二者只为决定准入的含糊事实定点补读，不是日期hold后全附件深审。DataSage同base/temperature和相同QA轮数不证明调用token预算匹配，额外modules对简单任务冗余是作者限制；保留而不靠降分回避争议。

## 日期保留与轻量纠错

14份API `published`/`updated`原值均是Nov18的v1时间，完整原字段在XML；不能把字段名published自动当首次公开，不能用submitted或常规20ET schedule补造BJT09。当前无确定当窗arXiv家族。最小请求为官方公开事件/具名作者首次公开上下界完全落窗；API恢复上界跨截止不证明窗外。先有限恢复与current页具名纠错/撤回检查，再把真实不可得隔离，不展开所有实验以代替日期。

## root请求与普通停点

请先校准上述具体方向，尤其10Cache是否仅成熟原则、DataSage实际回选hook是否有增量、Authentic-Dubber是否通用生成机制、Failure to Mix是否被科学动机误排。代表性负侧已有 [RSS单项包](RSS_DATE_AND_INCREMENT.md) 的商业产品/最佳实践与 [首批包](FIRST_BATCH_CALIBRATION.md) 的应用及晚版分层，不补造arXiv关闭数量。

还可执行：focus查询标题、官方有限片段标题补检、selected current页的纠错信号与日期有限恢复。未读各owner不叫Books缺口；任何名称未收录不请求整合；不等root校准开展无关source收口。
