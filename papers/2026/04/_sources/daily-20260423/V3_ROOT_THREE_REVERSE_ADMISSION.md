# 04/23 三项题摘潜在的反向准入

作者：root。只校准贡献分母；以下不是整日日期/来源 Gate，也不以单篇关闭证明本窗负侧完整。复开官方 exact-v1 的问题、方法、必要实验及限制，对照本书现有 owner。三项原来只是“潜在”，并非已完成 Source Review。

## `2604.20027v1`：视觉 attention 与人类显著性

[官方 exact-v1](https://arxiv.org/html/2604.20027v1) 的主实验是 ViT-B/16 的人眼 saliency 微调与 shuffled control，报告几项显著性指标和 ImageNet/ImageNet-C/ObjectNet 分类 parity；CNN/ResNet-50 对照没有同样结果。这个结论限定在特定视觉分类模型、标注和统计对照；“attention 更像人”没有证明任务推理更正确、解释具因果忠实性，`no cost` 也不能跨生成、多模态对齐或推理系统外推。对照 `MULTIMODAL-REPRESENTATION` Ch23 与 Evaluation Ch66，均已有表示读出/任务效果/因果解释分责，本文未改变主线的模型表示、执行或发布合同。**具名贡献前关闭**，保留 family-specific 理由，不评分、不进 Books。

## `2604.19954v1`：相机参数作为生成条件

[官方 exact-v1](https://arxiv.org/html/2604.19954v1) §3–4 把 object-centric 五参数相机坐标编码为与文本共同输入的 viewpoint token；3D render 几何监督加较少量 photorealistic augment 试图将姿态从外观相关性中分离。其控制仅在所选 3D 资产、相机取值、模型与文本到图像评价成立，且 Table 4 中所列颜色/对象一致性并非相对底座零代价。`MULTIMODAL-REPRESENTATION` Ch23 已要求 coordinate/reference-frame identity，Ch24 已区分生成提案与独立几何验收；本文给出这些原则的一个任务特定 conditioning recipe，而未迫使当前跨模态表示合同改变，也未证明世界状态或真实控制迁移。**具名贡献前关闭**，不是排除所有几何控制研究；有跨物体/跨场景可复算的通用表示/状态新证据时再重开。

## `2604.20039v1`：Blicket 假设空间动态扩张

[官方 exact-v1](https://arxiv.org/html/2604.20039v1) §3–5/§7 的 context graph 由提示引导阶段、LLM 自行判转移；dynamic behavior 用预筛、Haiku 打分和一次性通知添加状态。它在合成隐藏规则变化中把“能进入看到变化后的推理阶段”与“进入后能否推对”分开，属于有用的诊断；但主要 `reasoning-eligible accuracy` 三分法是在 Run04 观察到恰好触发切换却未见新证据的 trap 后制定，不能当完全预注册的通用 Agent 能力指标。作者自己的 stochastic、order-sensitive 负对照未见可靠优势，只测一个 API 模型家族。`AGENT-PLANNING` Ch79 已有 belief/observations，Ch80 已有反例查询与纠错，Ch81 已有外部状态机、revision 与 replan/commit 分责；本文的状态机+异常监视器是该现有路线在 toy task 的受限实例，未建立新的独立控制权或普遍任务 Gate。**具名贡献前关闭**；尤其不把作者 94% 分解写成跨任务“因果推理机制占比”。如后续可在真实工作流证明现有 state/replan 无法覆盖的结构扩张，则重开。

这三项仅修改初筛工作判断：原 `129=55 潜在+74 前关闭` 应在独立反查无反证后变为 `129=52 潜在+77 前关闭`。旧行保留初筛时序，下游 README 未更新之前不能引用新数字为正式冻结分母；日期/撤回/跨周 owner 仍须最终检查。
