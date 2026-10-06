# 2025-10-09 有界第二12题摘

仅本日102主题实际返回中的具名系统/模型/Agent/安全差额12，abs exact-v1均200/exit0，原件在[supplement](supplement-20261013/)；完整标题/摘要实际已读。以下6P6N为原作者提案，现由[root实际§5–6](SUP_INDEPENDENT_20261013.md)完成六项决定事实及必要反侧，当前**11窄P1C/N0**。第一14的有效12P2C与五局部沿root§3复用；两批无交集，累计26完整题摘为23P3C，仅准入层，不评分、不授当窗资格/Evidence/Books，不构造102全文队列。

| 精确v1 | 初判 | 具体增量/所需决定与采用界 |
| --- | --- | --- |
| [07356 ConCuR](https://arxiv.org/abs/2510.07356v1) | N | concise/informative reasoning及kernel数据curation可能改变训练信号/效率选择；需最小长度/筛选条件是否区别成熟kernel-SFT数据构造或只是KernelBench榜单。不能硬件标题自动P，也不能因AB未写因果实验直接C；正确kernel/性能/推理长度分责。 |
| [07358 Encode-Think-Decode](https://arxiv.org/abs/2510.07358v1) | P | 固定逐层计算 → midtraining选reasoning-relevant层递归、推理自适应深度 → latent计算/消费者接口改变。参数/数据/超参不变不等总训练/推理budget相同，17任务小模型不授普遍无代价扩展。 |
| [07019 Native Hybrid Attention](https://arxiv.org/abs/2510.07019v1) | P | 线性/full attention二分 → RNN KVslots与local tokens一起softmax、window连续调节 → 历史压缩/当前精确KV消费接口改变。不以hybrid名称准入，不授slot保所有long-context信息或所有负载E2E胜。 |
| [06751 OBS-Diff](https://arxiv.org/abs/2510.06751v1) | P | 一次网络prune忽略逐步denoise误差累积 → timestep-aware weighted Hessian/group sequential校准 → 压缩产物/误差与成本消费者条件改变。沿用OBS本身不另计贡献，trainingfree不等无需校准/硬件稀疏kernel，未采所有granularity加速。 |
| [06730 PTEB](https://arxiv.org/abs/2510.06730v1) | P | 静态embedding榜单当鲁棒 → eval-time随机paraphrase/多run、token变化与semantic目标分责 → 评价输入/重复调参盲点可核。STS gold与LLM不自动认证全部语义保持，十语言/七任务不授部署公平/无污染，statisticallyrobust需原协议。 |
| [06750 Gold-Switch](https://arxiv.org/abs/2510.06750v1) | N | deployment superposition/inference unlearning、SVD energy只概述，需最小权重投影/开关条件区别成熟task arithmetic或两模型route；不是slow/fast-thinking标题P。trainingfree不等零compute/所有任务reasoning保真。 |
| [06664 ToolMem](https://arxiv.org/abs/2510.06664v1) | N | neural tool能力由交互汇总memory再retrieval选tool；需实际更新/选择/失效接口或受控反侧是否区别成熟工具profile＋memory/RAG组合。不能用summarize-strengths词或21/24%直接P；learned capability不授最优/可靠工具。 |
| [06587 WebDART](https://arxiv.org/abs/2510.06587v1) | N | navigation/extraction/execution拆分与动态replan是一般agent流程，需具体状态/动作或新失败条件决定增量，不能只靠成功率/少steps。域WebChoreArena不自动C，执行确认/permission未授。 |
| [07248 PA-Tool](https://arxiv.org/abs/2510.07248v1) | P | SLM命名先验与tool schema错配 → output peakedness挑命名并适配schema而非重训 → 模型/tool协议消费者边界改变。不把concentration等同真pretraining污染/能力或后端语义同一，rename需映射/授权分责，80%仅所评错类。 |
| [13825 A2AS](https://arxiv.org/abs/2510.13825v1) | N | BASIC certificates/authenticated prompts/context boundaries强enforce/integrity/zerooverhead；需最小实际验证/授权/证书机制还是in-context policy建议，必要安全反侧不能按框架名/HTTPS类比授保证。不执行攻击或部署；late ID不自动窗外。 |
| [06492 Latent Safety Filters](https://arxiv.org/abs/2510.06492v1) | P | learned RGB latent被当安全状态充分 → hidden-temperature/避看failure反侧及train-time额外sensor → 表示可观测性/安全filter消费条件改变。MI代理与RGB-only部署不造隐藏信息，真实wax/Franka仅具体受控设置，安全/恢复条件需必要局部。 |
| [06719 DP-SynRAG](https://arxiv.org/abs/2510.06719v1) | N | 从query-timeDP转一次syntheticDB复用有潜力，但postprocess不增budget是成熟属性；需private-prediction extension的具体生成/保护对象/选择条件是否新增机制，不能借DP名称或榜单直接P。正式DP/任意RAG泄漏保护需必要sensitivity/accounting边界。 |

## 实际校准后的决定与限制

root实际完整exact-v1题摘及具名局部已通过；不重读有效core，原提案改判依据如下：

- ConCuR转P：正确kernel中联合trace长度、执行速度与单/融合算子人口平衡，改变数据选择；最短trace不独立更好/快，四消融任务人口不平衡，随机输入正确不授全shape或编译最优基线。
- WebDART转P：默认执行数据约束，发现filter/sort才改由navigation消费，是真实阶段控制选择；Admin步骤反增、导航步骤不等总token/工具成本。
- ToolMem转P：四能力分类、反馈、逐类检索及merge/update/remove路径区别静态描述/原经验few-shot；LLM总结不授能力真值，checkpoint仍有描述歧义。
- A2AS转C：必要安全域仍为成熟manifest/hash/tag/policy模块组织，没有独特执行/安全成立机制。不是因为无benchmark关闭；hash不授语义可信，额外token及小模型/多模态/配置限制不支持普适零开销。封面Sep29仅文稿日期，不作first-public或窗前O。
- DP-SynRAG转窄P：实际增量是私有局部聚类的受控L重叠、noisy关键词/中心及私有threshold、clipped logits生成，不是成熟DP后处理性质。正式隐私仍需邻接、附录证明与composition核验；record-DP不等所有秘密匿名化，新版本生成仍消耗预算。
- Gold-Switch转窄P：仅单reasoning模型加低秩delta的部署分支。Eq1与反delta描述方向不一、Eq8条件重叠、Eq5/6尺度不齐、最小rank文字不清均保留；未核代码，不能静默修公式后采用无损reasoning/只删overthinking。复杂任务always-on与soft-scaling反侧不删。

Latent safety必要§V–VII沿root§6实际层：MI是冻结encoder/linear-probe下界，低下界不证明真实MI低；40轨迹32/4/4为有限人口。多模态部署与RGB编码＋IR训练监督两设置分开，后者不增加部署信息，相关性失效仍有可观测gap；五步history和16步open-loop不同对象，不授安全认证。

07019当前官方abs的v3有效、旧v2撤回；不写当前家族撤回，不以v3代v1或把复活作Oct08事件。当前必要公开日/机构来源与未采用命题的后续事实仍普通工作；PA-Tool若采用具体调用正确性，定点读schema映射，不为每个P机械扩全文。本批没有formal/DAY。
