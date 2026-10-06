# 2025-09-12 有界筛选

窗口：2025-09-11T09:00:00+08:00～2025-09-12T09:00:00+08:00。作者Bacon；只本日原来源与精确v1，不继承别日候选。

## arXiv身份、题摘与贡献

原件`abs-<ID>v1.raw`；完整题摘派生`arxiv-v1-title-abstract.json`含URL/取得时刻/原始完整摘要。24份实际读完仅算题摘，不称全文、实现或复现。月表邻段518标题是有限发现库存，不是当日新事件或强制队列。各项v1提交时间仅原字段，公开日期尚未核，潜力不入正式候选、不给分、不进Books。

| 精确v1 | 实际增量与本项目关系 | 作者处置 |
| --- | --- | --- |
| 2509.08867 | vLLM能耗对模型大小/架构/并发的测量；补读III/IV/V后有架构收益受后端/每请求度量混杂的局部反证 | 潜力，已补决定性方法，详见下段 |
| 2509.08972 | 错误高置信度诱发坍塌，TCE重新加权；可能改变后训练置信度目标 | 潜力，置信度与正确性不可等同 |
| 2509.09001 | ANN attention的Match2与k-hop理论表达能力边界 | 潜力，须核假设，不机械要求LLM实测 |
| 2509.09055 | OPT350M局部SFT/DPO对照与组合结果可能修正选择 | 潜力，不因小模型关闭；评价/预算尚未读 |
| 2509.09088 | balanced深线性网络参数几何与熵关系 | 理论潜力，真实LLM/训练选择的桥尚待核，不以非LLM关闭 |
| 2509.09090 | VLA token剪枝与低比特量化相互干扰并共同设计 | 潜力，1.93x和4.5%仅作者结果 |
| 2509.09091 | TEE embedding/GPU后层分区与双隐私控制 | 安全潜力，威胁模型/可信边界未读，非普通排除 |
| 2509.09097 | 联邦LoRA裁剪/噪声与更新偏差、DP边界 | 安全潜力，privacy unit/邻接/聚合前提未读 |
| 2509.09112 | 字符编辑影响多token水印，两种检测器访问威胁模型 | 安全设计反证潜力，未读核心不授抗攻击保证 |
| 2509.09119 | Hessian敏感度分配LoRA rank | 潜力，预算和Hessian成本尚未核 |
| 2509.09174 | 语义表示动态生成语音训练目标，声学/语义gap | 潜力，不按ASR领域应用机械关闭 |
| 2509.09177 | sequence importance weight长度偏置与公平clip理论 | 潜力，具体分布/长度前提待读 |
| 2509.09199 | 分段语义压缩与KV编码、增量解码/稀疏采样 | 潜力，缓存identity和重建训练成本未核 |
| 2509.09245 | Notebook可执行任务提取与MCTS value/visit监督 | 潜力，需区分执行反馈契约与成熟搜索组合 |
| 2509.09265 | entropy-gradient coupling与future clarity奖励 | 潜力，置信度不是正确性，objective/预算未读 |
| 2509.09284 | tree rollout前缀条件advantage、逐阶段GRPO，包含饱和/坍塌负面结果 | 潜力，保留局部负面证据 |
| 2509.09292 | LightAgent摘要描述mem0、Tools和ToT框架集成 | 建议关闭：未建立新增执行/状态一致性机制，不是因框架规模或四人样本 |
| 2509.09360 | RAG变形测试同义/反义扰动及逻辑关系判据 | 潜力，judge/事实mutation有效性与盲区未核 |
| 2509.09372 | VLA Bridge Attention与避免robot pretrain的条件化分支 | 潜力，训练时长宣传不是准入理由 |
| 2509.09396 | self-counterfactual validity/minimality tradeoff，局部反证解释忠实性 | 潜力，不因负面结果关闭 |
| 2509.09420 | NMP MoE离线TP/EP映射与在线调度 | 潜力，硬件/模拟范围需核，不外推GPU普遍收益 |
| 2509.09424 | CKKS/BitNet协同协议，sigmoid代softmax与bootstrapping | 安全/正确性潜力，函数语义与威胁模型未核 |
| 2509.09438 | embedding similarity confidence校准及TTS提前停止 | 潜力，校准与真实正确性保证须分开 |
| 2509.09448 | TORSO摘要只明确模板的通用性与few-shot便利；补读§2/3/5/6显示token logit强制与EOS截获机制及随机模板反侧 | 潜力，已补决定性方法，详见下段 |

两项含糊贡献已窄补：`html-08867v1.raw/.txt`实际读III方法、IV结果与V完整相关讨论/限制。两块3090、HellaSwag、200warmup、一次同时到达5～5000请求、CodeCarbon每15秒估算；10次架构对照。每请求结果与既有每token/Transformers结论不同，作者也承认后端与度量共同改变，未隔离vLLM因果，未评价质量。潜力是测量/归因混杂及局部反证，不是100并发普适最优；精度、输出长度、SLO Not Disclosed，未实际看四图像或复现。

`html-09448v1.raw/.txt`实际读§2完整机制、§3条件、§5语义/随机template消融及§6限制。首步高logits强制组成`<reasoning>`的tokens，首EOS截获后插入结束reasoning和answer开始标记再生成；这是inference时序干预，不仅few-shot模板重排。三Instruct模型、最大8192、T1/topk50/topp1、六benchmark、5-shot及zero-shot CoT；GPT4o只评双方答对子集的rationale，不能证明推理忠实或所有题因果。随机tokens多数低于base、OOD/既有固定rationale模型可能失败，支持条件化干预潜力；没有预算匹配普适优越证明。贡献含糊已解除，转为日期保留，不作普通排除。均待root校准，不提前赋正式分数。

## 官方Blog明确关闭与保留

OpenAI RSS本窗两条14:00GMT法人/MOU公告为治理与商业状态，不新增本项目模型/系统机制；完整描述已读，不写零事件。Google Speculative Cascades正文方法/实验实际读完，对应2024稿2405.19261旧机制，未见本次新增方法、评价或纠错；本日再阐述关闭，不冒充已有效审阅重复。NucleoBench/AdaBeam题义明确AI for Science，ROADMAP暂缓。

PLAS：初始本日发布提案已因精确旧版与模型更新反证改判，见HANDOFF。算术错误保留：21B TTFT实际下降32.37%、E2E31.34%；47B TTFT23.37%、E2E19.40%，不采用原表48/46/30/24%降幅。原kernel386%非端到端，输入113K平均/输出长度有变化、硬件精度并发SLO Not Disclosed；不能从启动命令补benchmark配置。未作运行或复现。

VaultGemma正文真实读核心：1024-token packed sequence级epsilon≤2、delta≤1.1e-10，不是用户级/文档级保证；50-token前缀/50-token后缀未检出记忆不保证任意查询。新artifact可能贡献，不因关联旧scaling论文自动关闭。可见Sep12但无时区时刻；成功RSS仅最近100条无9月，尚不支持12日窗口采用。
