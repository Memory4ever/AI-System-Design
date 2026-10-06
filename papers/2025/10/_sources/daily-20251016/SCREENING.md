# 2025-10-16 有限发现与贡献筛选

作者Euler。仅BJT[2025-10-15T09:00:00+08:00,2025-10-16T09:00:00+08:00)。潜力不等当窗候选；不评分、不授正面Evidence。以下判断来自实际完整精确v1题摘或官方core，不来自下载成功标签。

## 查询与停止

四主题均附 `AND submittedDate:[202510141400 TO 202510151400]`，sortBy=submittedDate、ascending、max_results=60。该提交字段范围只作历史发现，不是本日报公开窗口：

| 主题 | 实际search_query主题部分 | 分页/实际条数/停止 |
| --- | --- | --- |
| 模型 | `(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")` | start0/60/120，60/60/13；total133到末页止 |
| Agent | `(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:"LLM agent" OR all:"retrieval augmented" OR all:"tool calling")` | start0/60，60/20；total80止 |
| 多模态 | `(cat:cs.CV OR cat:cs.RO) AND (all:"vision language" OR all:"world model" OR all:"foundation model" OR all:"diffusion model" OR all:"vision language action")` | start0，45；total45止 |
| 运行时 | `(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:"language model" OR all:GPU OR all:"model serving")` | start0，8；total8止 |

原响应为arxiv-model.xml、arxiv-model-60.xml、arxiv-model-120.xml、arxiv-agent.xml、arxiv-agent-60.xml、arxiv-multimodal.xml、arxiv-runtime.xml，各自 `.request.json` 保留真实起止时间、URL、HTTP/退出状态。266次出现、202个不同完整Atom ID，仅表示这个发现切片，不称266/202篇当天新论文。API其他标题只作相关线索/范围切片，未转为逐篇全文队列。

官方分类标题有界补检：CL skip975、LG skip750、CV skip1100、DC skip75，show25；原web失败，不声称读过返回列表。由已取回的四主题标题挑96份相关/含糊精确v1题摘；后续只补18个具名机制标题：12789、12931、13907、13910、13291、13481、13193、13394、12954、17858、13367、13434、13908、13898、13302、12950、13108、13163。未扩大整月/整类库存。

完整AB原件：RAW_FIRST_V1/REMAINING、RAW_AB_B～L；13个访问失败身份以本日 `abs-2510.<ID>v1.html` 恢复。末次交接核发现21个批响应未保留完整AB，实际于2026-10-05T00:03:50.067Z～00:04:03.279Z定点补存并重新完整读：12693、12721、12974、12993、13008、13212、13248、13272、13334、13344、13351、13401、13512、12796、13080、13251、13901、12548、13912、13363、13928；每项有真实request/headers。此补存不等重新扫描，也不把raw本身当阅读证明。

## 日期与身份隔离

原114份完整v1 AB中112潜力/2关闭；Cicero四页有限恢复后作者实际读九新增v1完整AB/版本史（八潜力/一关闭），与原表无重复，共123完整AB身份、120 arXiv潜力/3关闭，加Coral/Paddle=122日期潜力家族，正式当窗候选0。逐项v1 Submitted原值及版本史保留于原件：它不等首次公开。未取得本窗官方历史公告或完全落在UTC[2025-10-15T01:00,2025-10-16T01:00)的first-public bounds。所有潜力日期隔离，不采用作者性能数字、不进入Books；只有精确身份相同且可信原始公开证据完全落窗才定点重开。

Coral Oct15、Paddle Oct16只是未知时区日名，与窗口可能相交不能准入。Atom未指定版本题名不覆盖v1：12586是Pixel Space而非2026 There is No VAE；12728是Data-Model Co-Evolution而非Data-Prompt；12993不是后来的Tailored Untruths；13154不是Alignment Veto；13315为Self-Augmented Visual Contrastive Decoding；13481 v1用guidelines and receipts。12709/12712等后续v2时间本身不证明重要修订，未倒灌v2机制。轻量可见原版本页未给出可据以采用的纠错/撤回公告；不遍历全部附件证明没有标记。

## 逐项具体潜力

各行均为“旧约束 → 原文实际增量 → 应重新考虑的选择”，仅潜力/日期隔离，独立校准及具名恢复见末节；收益真实性不是初筛排除理由。链接标签保留精确ID与短身份，完整原题名在AB原件。

| 精确v1 | 具体增量与改变的选择 |
| --- | --- |
| [12633 Laminar](https://arxiv.org/abs/2510.12633v1) | 同步rollout长尾阻塞 → relay独立拉权重/repack → 异步粒度与staleness取舍 |
| [12635 Memory as Action](https://arxiv.org/abs/2510.12635v1) | 启发式记忆与policy分离 → 记忆编辑action/非prefix轨迹切段 → 编辑的RL信用分配 |
| [12966 Pyramid SD](https://arxiv.org/abs/2510.12966v1) | draft尺寸与接受率冲突 → qualifier/fuzzy接受 → 三模型成本与质量损失，非无损 |
| [13223 BanaServe](https://arxiv.org/abs/2510.13223v1) | P/D和cache热点耦合 → layer/KV迁移及global store → placement/路由拆分 |
| [12586 Pixel Space](https://arxiv.org/abs/2510.12586v1) | 像素生成训练困难 → clean语义/确定轨迹encoder预训练 → 非VAE训练路径 |
| [13237 VLA attack](https://arxiv.org/abs/2510.13237v1) | 动作受视觉扰动 → 跨模态/clean-adv双目标patch → encoder访问下攻击/防御边界 |
| [12637 COSTAR-A](https://arxiv.org/abs/2510.12637v1) | 紧token预算下小模型不决断 → 显式Answer组件且模型差异 → 输出指令是否需要模型条件化 |
| [12581 LayerSync](https://arxiv.org/abs/2510.12581v1) | 外部表示教师成本 → 内层语义互相正则 → diffusion自监督的替代依赖 |
| [12587 FUT](https://arxiv.org/abs/2510.12587v1) | 言语不确定性与重复采样分歧不合 → consistency对应hedge微调 → 表达忠实度与事实校准分开 |
| [12643 PARO](https://arxiv.org/abs/2510.12643v1) | rationale标注昂贵 → 固定模式任务的pattern监督/合成 → 标注量与模式知识分开 |
| [12668 PRAG](https://arxiv.org/abs/2510.12668v1) | 文档token上下文成本 → 参数化文档检索/组合 → 部分检索收益和组合成本分开 |
| [12672 CALM](https://arxiv.org/abs/2510.12672v1) | 固定拒绝易绕过 → 概念空间投影 → 校准数据、PPL及decode成本取舍 |
| [12689 Delegates/Trustees](https://arxiv.org/abs/2510.12689v1) | 克隆偏好被当福利 → 长短期权重模拟改变默认偏置 → 不以专家共识代理授权/福利 |
| [12693 ERA](https://arxiv.org/abs/2510.12693v1) | 小VLM具身先验不足 → 三类prior+turn RL/自总结 → prior、上下文与稀疏奖励的联合训练 |
| [12697 Judge Debate](https://arxiv.org/abs/2510.12697v1) | 静态多数投票失败 → Beta-Binomial混合/KS稳定停止 → 停止效率与正确性假设分开 |
| [12709 SAIL](https://arxiv.org/abs/2510.12709v1) | 统一embedding域差异 → 渐进内容/协作蒸馏和随机specialization → 表示学习与推荐适配边界 |
| [12712 IRIS](https://arxiv.org/abs/2510.12712v1) | 静态图像评测遗漏操作能力 → 单/多轮图像工具任务及模型收益反转 → 工具可用不等有效利用 |
| [12720 Omni-Captioner](https://arxiv.org/abs/2510.12720v1) | 细节与幻觉共增长 → 工具生成数据/Omni-Cloze → 详细度和事实性的联合评价 |
| [12721 CARVQ](https://arxiv.org/abs/2510.12721v1) | embedding占端侧内存 → group residual VQ+corrective adaptor → bitwidth与映射/硬件成本 |
| [12728 Data-Model Co-Evolution](https://arxiv.org/abs/2510.12728v1) | 固定测试集掩盖含糊政策 → edge case/rationale/指令共同迭代 → 政策精化的证据闭环 |
| [12773 Dr.LLM](https://arxiv.org/abs/2510.12773v1) | 全层固定深度 → MCTS监督skip/execute/repeat → depth预算路由，非MoE |
| [12784 SRUM](https://arxiv.org/abs/2510.12784v1) | 理解能力不转为生成质量 → 自评global/local双reward → UMM内部教师信号条件 |
| [12872 KVCOMM](https://arxiv.org/abs/2510.12872v1) | 不同prefix使cache不可直接共用 → anchor估计offset → 近似跨context复用的质量/TTFT |
| [12801 DeepMMSearch](https://arxiv.org/abs/2510.12801v1) | 固定多模态检索流程 → crop图像/迭代文字search的SFT/RL → 工具选择与查询形成 |
| [12948 SpareCodeSearch](https://arxiv.org/abs/2510.12948v1) | 默认embedding检索需GPU → keyword代码context的局部反证 → 轻量IDE检索是否需语义模型 |
| [12974 SCOPE](https://arxiv.org/abs/2510.12974v1) | 堆叠encoder冗余 → 文图instance路由/双entropy → 一共享一选择encoder，非token MoE |
| [12979 DeepPlanner](https://arxiv.org/abs/2510.12979v1) | planning token在RL中高entropy欠优化 → token/sample优势shaping → credit如何分配给规划 |
| [12993 Persona disinformation](https://arxiv.org/abs/2510.12993v1) | 通用拒绝测量漏人格化切片 → 四语言persona红队 → 安全评测必须限定人口/语言 |
| [13003 OPLoRA](https://arxiv.org/abs/2510.13003v1) | LoRA干扰dominant子空间 → 双侧正交projection → singular保持不自动等知识保持 |
| [13008 CurLL](https://arxiv.org/abs/2510.13008v1) | CL评价缺技能依赖 → 分阶段skill graph/独立联合顺序对照 → retention与transfer分开，不拟人定律 |
| [13022 PVar](https://arxiv.org/abs/2510.13022v1) | 偏好数据均匀采样 → gradient上界/PVar筛选 → 何类pair有更新信号，非低方差全无价值 |
| [13054 VLA-0](https://arxiv.org/abs/2510.13054v1) | action head/token被视必需 → 直接文字action及配方 → 架构复杂度是否必要 |
| [13079 GatePro](https://arxiv.org/abs/2510.13079v1) | load balance未消专家功能冗余 → 相似pair局部竞争 → 专家多样性与负载分开 |
| [13103 ESI](https://arxiv.org/abs/2510.13103v1) | UQ只采样输出 → 语义保持intervention不变性 → grey-box变化能否估计epistemic uncertainty |
| [13106 TRUSTVIS](https://arxiv.org/abs/2510.13106v1) | aggregate多数judge掩盖unsafe切片 → human对照暴露低TUR precision → 安全分类需分切片核 |
| [13117 Masked diffusion theory](https://arxiv.org/abs/2510.13117v1) | 并行生成表达力未知 → finite precision/log-width下PLT/CoT关系 → 理论效率的假设边界 |
| [13147 D-com](https://arxiv.org/abs/2510.13147v1) | runtime低秩分解成本抵消收益 → Lanczos/复制compute/shape保持 → activation分解的硬件可行区 |
| [13154 MENAValues](https://arxiv.org/abs/2510.13154v1) | 单语言alignment掩盖价值变化 → framings×language/解释退化 → 描述性分布不作规范目标 |
| [13183 DSCD](https://arxiv.org/abs/2510.13183v1) | 单层contrastive decoding局限 → JSD选层组合 → heuristic层选择收益与负面任务 |
| [13190 SHIELD](https://arxiv.org/abs/2510.13190v1) | 单次安全prompt缺适配 → 类别到prompt动作 → “Block”是文本策略非权限阻断 |
| [13191 Contextual Normalization](https://arxiv.org/abs/2510.13191v1) | 相同语义不同delimiter结果变化 → 密度/位置/结构控制 → 检索内容与呈现质量分开 |
| [13212 TIF preference](https://arxiv.org/abs/2510.13212v1) | 外部RM价值评分被当模型无关 → truncated influence揭模型间反号 → 数据选择需模型条件化 |
| [13248 NeTestLLM](https://arxiv.org/abs/2510.13248v1) | runtime失败被统一重试 → artifact/testcase异因分层修复和human escalation → 错误类别决定恢复层 |
| [13272 VERITAS](https://arxiv.org/abs/2510.13272v1) | 答案正确掩盖search trace不忠实 → 三类trace reward → regexp/judge代理不等因果faithfulness |
| [13276 MMLongCite](https://arxiv.org/abs/2510.13276v1) | 长多模态window被当利用率 → 长度/位置/citation fidelity测试 → window容量与grounding分开 |
| [13285 IDS](https://arxiv.org/abs/2510.13285v1) | 固定steering破坏连贯 → PCA/Mahalanobis分布调强度 → 训练分布内控制不等OOD安全 |
| [13290 MERA](https://arxiv.org/abs/2510.13290v1) | 固定steering可能退化 → 校准强度/abstain → iid保证及公式冲突限制采用 |
| [13312 ChatR1](https://arxiv.org/abs/2510.13312v1) | 固定rewrite/retrieve多轮意图漂移 → intent-aware turn reward → 动态检索的信用分配 |
| [13334 DefensiveKV](https://arxiv.org/abs/2510.13334v1) | 平均importance稳定性假设脆弱 → historical max/prior floor → cache淘汰极端风险非未来保证 |
| [13344 UniMoE-Audio](https://arxiv.org/abs/2510.13344v1) | 语音音乐冲突/不平衡 → Top-P/shared/null专家及三阶段训练 → 动态capacity与跨域干扰 |
| [13351 Protect](https://arxiv.org/abs/2510.13351v1) | 单模态guard局限 → category LoRA/teacher多模态标注 → human抽检/标签反转冲突需保留 |
| [13401 F-BFQ](https://arxiv.org/abs/2510.13401v1) | mixed BFP需reconfigure → 双变体动态MatMul → 端侧硬件可变格式取舍 |
| [13512 LDP RLHF](https://arxiv.org/abs/2510.13512v1) | KL-RLHF理论未含label privacy → offline pessimism/online optimism bounds → label-LDP与内容隐私分开 |
| [13537 K-Merge](https://arxiv.org/abs/2510.13537v1) | LoRA增量超端侧存储 → 无数据continual选取/合并 → online储存预算与旧任务保持 |
| [13543 Browserfuzz](https://arxiv.org/abs/2510.13543v1) | 网页注入测试缺动态生成 → browser内LLM引导fuzz → illustrative数字不作真实攻击率 |
| [12560 CoIRL-AD](https://arxiv.org/abs/2510.12560v1) | IL/RL顺序切换梯度冲突 → 双policy竞争交流 → world-model训练知识迁移 |
| [12691 DiffEM](https://arxiv.org/abs/2510.12691v1) | 仅噪声数据难学prior → conditional diffusion E/M迭代 → 条件假设下单调性 |
| [12710 Reflective VLA](https://arxiv.org/abs/2510.12710v1) | 生成reward被hack → failure RL/success SFT双路径 → proxy reward与task success不能混同 |
| [12747 FlashVSR](https://arxiv.org/abs/2510.12747v1) | 流式diffusion latency → 三阶段distill/局部sparse attention/decoder → 分辨率外推与实时成本 |
| [12796 DriveVLA-W0](https://arxiv.org/abs/2510.12796v1) | 稀疏action监督欠用capacity → AR/diffusion未来图像aux → 训练world objective与部署action expert |
| [13080 Count hallucinations](https://arxiv.org/abs/2510.13080v1) | FID不稳定捕获数量错误 → counting suite/solver条件 → 分布质量与结构正确性分开 |
| [13232 NegToMe](https://arxiv.org/abs/2510.13232v1) | token拆分丢否定polarity → phrase merging/LoRA → 输入结构与检测affirmative bias |
| [13251 VideoLLM flow](https://arxiv.org/abs/2510.13251v1) | 时序信息路径不明 → layer交互/抑制attention边 → 有效路径与稀疏化可行性 |
| [13315 Visual contrastive decoding](https://arxiv.org/abs/2510.13315v1) | 通用augmentation忽视query → query自增强/自适应候选阈值 → hallucination decoding条件 |
| [13375 DepthVLA](https://arxiv.org/abs/2510.13375v1) | 纯action预训练空间能力弱 → depth transformer共享attention → 3D prior与action专家融合 |
| [13418 Mask-GRPO](https://arxiv.org/abs/2510.13418v1) | AR/diffusion policy未适masked过程 → 重定义transition/unmask decision → GRPO的生成范式条件 |
| [13253 Diffusion Mamba](https://arxiv.org/abs/2510.13253v1) | 模态encoder/decoder分离 → unified VAE/Mamba多步selection diffusion → 跨模态表示/生成共用 |
| [13903 Communication bounds](https://arxiv.org/abs/2510.13903v1) | 分任务直觉缺通信下界 → 三算法族agent/bandwidth/depth bounds → 不推一般wall-clock加速 |
| [13905 Schema ICL](https://arxiv.org/abs/2510.13905v1) | free-form demonstration难抽象迁移 → structured inferential schema → 模型ICL机制，不因GPQA为科学题而排 |
| [13913 Progressive difficulty](https://arxiv.org/abs/2510.13913v1) | Web数据难度不匹配学习阶段 → progressive difficulty训练 → 数据选择随模型能力变化 |
| [13915 Readability/Learnability](https://arxiv.org/abs/2510.13915v1) | readable被当learnable → readability/ngram对照与域外失效 → 结构简单性和人类可读性分开 |
| [13900 Narrow FT traces](https://arxiv.org/abs/2510.13900v1) | 窄FT模型代理被当一般chatFT → activation diff及C4混入反例 → 安全研究proxy外推边界 |
| [13901 RAID](https://arxiv.org/abs/2510.13901v1) | 离散suffix优化受限 → continuous/refusal/coherence联合优化 → white-box访问与查询成本分开 |
| [13918 PRM aggregation](https://arxiv.org/abs/2510.13918v1) | PRM默认正权重排序 → LLM/PRM联合校准甚至负权 → evaluator pair条件化 |
| [13551 Tandem](https://arxiv.org/abs/2510.13551v1) | 强模型trace弱模型不可续 → 随机weak handoff RL → handoff robustness不等human oversight |
| [13554 Attention credit](https://arxiv.org/abs/2510.13554v1) | 统一trajectory credit → attention预规划/anchor加权 → 额外forward成本及非因果代理 |
| [12548 VISaGE](https://arxiv.org/abs/2510.12548v1) | 概念/实例priors冲突未区分 → congruent/exception平衡测试 → pragmatic匹配偏置 |
| [12608 StyleDecipher](https://arxiv.org/abs/2510.12608v1) | AI文本检测脆弱 → discrete rewrite/edit/embedding classifier → 风格概率不是身份凭证 |
| [12702 NL2Contract](https://arxiv.org/abs/2510.12702v1) | 只postcondition误报invalid input → 生成precondition+验证 → verifier可发现性和真实bug分开 |
| [12547 UAED](https://arxiv.org/abs/2510.12547v1) | 训练/部署环境分布错位 → 自适应environment distribution → 学习理论主线非泛领域应用 |
| [12864 RID](https://arxiv.org/abs/2510.12864v1) | rule rigidity → rule-intent meta-prompt → 20例author标签不授越权能力 |
| [12722 GCG generalization](https://arxiv.org/abs/2510.12722v1) | word-order/length泛化困难 → 结构归纳偏置 → 序列模型学习边界，非传统语言学排除 |
| [12925 Persona QA robustness](https://arxiv.org/abs/2510.12925v1) | persona变动影响回答 → persona QA鲁棒性对照 → 风格条件与事实正确性分开 |
| [13095 R4R](https://arxiv.org/abs/2510.13095v1) | free CoT不贴合docid → compact reasoning/约束decode交替 → 单模型retriever/reasoner复用 |
| [13909 KRLM](https://arxiv.org/abs/2510.13909v1) | 关系知识表示/生成受限 → tokenizer/dynamic memory/约束预测 → 结构知识进入模型的机制 |
| [13143 Ensemble selection](https://arxiv.org/abs/2510.13143v1) | 全ensemble成本 → representative选择/temperature → 多样性与评价配置耦合 |
| [13912 Debater beliefs](https://arxiv.org/abs/2510.13912v1) | debate正确性直觉忽视主观prior → persona冲突/顺序反转 → judge偏置非truth guarantee |
| [13214 ARE](https://arxiv.org/abs/2510.13214v1) | cascade校验成本被统一处理 → whole/step验证及正确step复用 → workload难度下收益反转 |
| [13202 LGSA](https://arxiv.org/abs/2510.13202v1) | naive swap失label语义 → LLM上下文保持/人抽检 → counterfactual augmentation的label fidelity |
| [13363 D-SMART](https://arxiv.org/abs/2510.13363v1) | static memory单路径对话衰减 → OWL动态graph/搜索/NLI → graph自洽不等现实事实 |
| [13406 Procrustes](https://arxiv.org/abs/2510.13406v1) | retrained embeddings不互通 → dot-product保持下isometry误差界 → 索引升级兼容条件 |
| [13501 CRew](https://arxiv.org/abs/2510.13501v1) | RM训练成本 → answer confidence proxy/正确性DPO → confidence不等truth且非无label |
| [13928 Brain Rot](https://arxiv.org/abs/2510.13928v1) | continual Web预训练质量不明 → M1/M2干预/剂量/控制 → training-time安全但控制组亦变化 |
| [13328 ToSFiT](https://arxiv.org/abs/2510.13328v1) | 离散acquisition优化昂贵 → 学posterior maximality/variational TS bound → Bayesian适配机制而非领域应用 |
| [12789 UniFusion](https://arxiv.org/abs/2510.12789v1) | 最后一层条件表示局限 → frozen VLM/LAP+VERIFI → unified条件encoder与生成指令重写 |
| [12931 ViZer](https://arxiv.org/abs/2510.12931v1) | caption参考指标罚真实额外细节 → 视觉语言latent zero-label → 评测blindspot和无text监督条件 |
| [13907 PromptDuelOptimizer](https://arxiv.org/abs/2510.13907v1) | prompt优化需label → pairwise judge/dueling bandit+mutation → label-free不等judge无偏 |
| [13910 RAGCapBench](https://arxiv.org/abs/2510.13910v1) | E2E RAG指标掩盖中间失败 → capability任务切片 → slow-thinking相关性不作因果 |
| [13291 WOWService](https://arxiv.org/abs/2510.13291v1) | 多步合规检查在线昂贵 → dual data/knowledge训练+在线cheap checks/离线human → latency与策略检查权限分开 |
| [13481 Tahakom](https://arxiv.org/abs/2510.13481v1) | tokenizer fertility不等下游收益 → 分布重权/固定vocab/继续预训练对照 → corpus-tokenizer匹配 |
| [13193 ReMindRAG](https://arxiv.org/abs/2510.13193v1) | KG遍历重复探索 → explore/exploit和memory replay → train-free遍历不等模型参数学习 |
| [13394 SpatialDISE](https://arxiv.org/abs/2510.13394v1) | 静态空间题掩盖动态内在推理 → intrinsic/extrinsic×static/dynamic → 多模态空间能力切片 |
| [12954 CADE ZeResFDG](https://arxiv.org/abs/2510.12954v1) | guidance频率/能量不稳 → 频率拆分、rescale/EMA/clamp → 无训练guidance控制 |
| [17858 Shortcut flow](https://arxiv.org/abs/2510.17858v1) | 多步flow distill改结构成本 → velocity self-distill无step-size embedding → 复用pretrained架构；ID大小不定日期 |
| [13367 Transformer online RL](https://arxiv.org/abs/2510.13367v1) | 部分观察下Transformer效果条件不明 → actor-critic共享/conditioning/slicing对照 → 训练组件与观察条件分开 |
| [13434 M²PO](https://arxiv.org/abs/2510.13434v1) | single reward/pair偏好信息损失 → 多perspective reward/所有pair优化 → judge/hallucination惩罚的偏好形成 |
| [13908 Operator precedence](https://arxiv.org/abs/2510.13908v1) | 运算中间值形成不明 → probe/logit lens/partial embedding swap → 小模型局部机制不是全部因果解释 |
| [13898 Attribution quality](https://arxiv.org/abs/2510.13898v1) | style metrics代理质量 → 六域600样本对照/域间反转 → aggregate非显著与切片分开 |
| [13302 One-shot authorship](https://arxiv.org/abs/2510.13302v1) | 作者风格被主题混杂 → style transferability/logprob控制 → provenance分数与identity分开 |
| [12950 EHR memorization](https://arxiv.org/abs/2510.12950v1) | 抽取量被当隐私风险 → prompt/embedding/子群测试 → 个体泄漏与群体泛化，非临床应用借壳 |
| [13108 DriveCritic](https://arxiv.org/abs/2510.13108v1) | LK/progress指标与偏好错位 → 对照trajectory/VLM critic → 单作者标签与伪标限制安全外推 |
| [13163 Graph abstract code](https://arxiv.org/abs/2510.13163v1) | 顺序代码表示掩盖结构 → JSON graph对照 → 表示方式影响模型程序理解，非因小实验排除 |

## 明确排除与未展开范围

原批完整AB排除2项：[InferA 12920v1](https://arxiv.org/abs/2510.12920v1)新增任务/评价在HACC宇宙学ensemble科学分析，不以通用Agent映射重引暂缓AI for Science；[Language Models Model Language 12766v1](https://arxiv.org/abs/2510.12766v1)完整AB提出Mańczak使用频率的概念立场，未提出能改变具体模型机制/形式边界/可核测试的增量，按贡献而非“NLP无关”关闭。另新增13170在末节完整AB关闭，合计3。已关闭身份first-public未核不影响处置，停止追日期。

Google Blog DeepSomatic Oct16标题明确基因变异科学应用、未见相关安全/纠错信号，只范围关闭；不因本月页取回就逐篇全部医学/科学条目。其余API不相关领域标题仅作线索，不声称逐项贡献已核或分层AB全量关闭；独立复核应分别抽查题摘排除2项和标题范围切片。112潜力不因主题已有、局部/负面/小模型而排除；也不因未校准而转成正面全文采用队列。

两官方core潜力：[Coral NPU](https://research.google/blog/coral-npu-a-full-stack-platform-for-edge-ai/)从MLIR/IREE progressive lowering至scalar/RVV/matrix协同，可能改变端侧compiler/hardware分工；matrix仍开发、CHERI being designed、未来模型合作不算实现。[PaddleOCR-VL](https://ernie.baidu.com/blog/posts/paddleocr-vl/)动态分辨率NaViT+0.3B语言模型、layout→element分工可能改变文档VLM的表示与资源预算。二者仅日名隔离，无性能/安全采用。

## 独立复核交接

[FIRST](FIRST_INDEPENDENT_REVIEW.md)首批实际通过；[Cicero FINAL10:05](FINAL_INDEPENDENT_REVIEW.md)原40必要/2official及来源/分层已核，新增九AB/三必要独立校准完成。作者按具名变化同步，不重审原40或扩四分类库存。当前普通返修落地后只剩Cicero变化POST/DAY，作者不自审通过。

## 九身份有限恢复与作者同步

Cicero对原四失败URL各一次curl max10秒HTTP200：CL975/LG750/CV1100/DC75各show25，实际100标题后停止，原件CICERO-arxiv-*及headers；作者复用这一实际有限标题阅读，不回填自己已独立读100标题。只下列九新增相关身份完整AB/版本史由作者实际读取：[AB1](CICERO-16ABsupp1.json)、[AB2](CICERO-16ABsupp2.json)、[AB3](CICERO-16ABsupp3.json)，13255 webmiss后读[own ABS](CICERO-abs-13255v1.html)。v1身份及后版本分开，13331 v2 Oct16提交不自动视重要修订；13293不能换2026 Cross-modal Consistency题名。首次公开仍未准入，不变100全文/全月队列。

| 精确v1 | 具体增量/关闭与Submitted原值（非公开） |
| --- | --- |
| [13161 Mirror-SD](https://arxiv.org/abs/2510.13161v1) | serial draft限制关键路径→early-exit top-k branch-complete与target suffix并行、SS/GPU-NPU分工→接受率/关键路径重比较；Oct15 05:22:57UTC，v2 Dec11不倒灌。潜力，lossless/性能不采用。 |
| [13194 StressTransfer](https://arxiv.org/abs/2510.13194v1) | 语义重点在S2ST丢失→LLM跨语言stress tags/对齐合成→声音条件接口与表达保真；Oct15 06:32:24UTC。judge不等speaker意图真值。 |
| [13255 HFTP](https://arxiv.org/abs/2510.13255v1) | 行为语言能力难定位组件→频域neuron-wise语法probe及模型升级相似性分歧→表示解释/行为提升关系；Oct15 08:04:49UTC。脑对照非临床应用、相似非因果同一。 |
| [13271 Concept](https://arxiv.org/abs/2510.13271v1) | 流畅文本不等线索/intent hypothesis更新→固定词汇层级clues/实际human logs与动态更新→推理评价盲点；Oct15 08:17:25UTC、v2 Jan2026不倒灌。预算混杂见CORE。 |
| [13293 Mismatch Aware Guidance](https://arxiv.org/abs/2510.13293v1) | TTS style与content冲突→LLM/NLI mismatch驱动adaptive CFG→强条件/语义保真取舍；Oct15 08:37:16UTC，2026 v2–4不倒灌。 |
| [13331 Group-VQ](https://arxiv.org/abs/2510.13331v1) | 码本collapse及利用/重构冲突→group独立/group内joint优化、training-free resampling→码率/利用取舍；Oct15 09:14:22UTC，v2 Oct16 05:26:09UTC不代公开时刻。 |
| [13316 Visual Interestingness](https://arxiv.org/abs/2510.13316v1) | judge自一致不等人偏好→单图/双图human对照、排序distill→偏好代理选择；Oct15 09:04:48UTC。position筛除/人一致切片见CORE。 |
| [13454 VIST3A](https://arxiv.org/abs/2510.13454v1) | video latent/3D decoder不匹配→small stitching+direct reward align→生成/重建监督及表示成本；Oct15 11:55:08UTC、v2 Mar2026不倒灌，不授通用物理状态/性能。 |
| [13170 Thinking Hats](https://arxiv.org/abs/2510.13170v1) | 关闭：完整AB只有six-hat taxonomy/CoT数据与performance overview/未来方向，未辨识新增机制或可核设计反证，不因综述体裁排；Oct15 05:54:13UTC，first-public未核不影响关闭，v2 Mar2026不倒灌。 |

40原必要加Mirror/Concept/Interestingness三组=43必要论文；作者仅实际补读CORE列出的相关段，不称与Cicero§3全节/附录全范围完全相同。DriveCritic Case1 608/663、Case2 304/503已窄校正；Pyramid对标准随机SD的top精确匹配简化不是一般lossless推导；RAID Eq18 descent与Alg3加gradient、GCG prose80/table88冲突保留。三点不改潜力计数、不授性能/安全。

源变化：Qwen本日Cicero Research/main/4323 Research route HTTP200，作者实际核CSR及articles/type:qwen_ai/language，不造文章API历史查询。Seed非置顶Publication Oct21→20→Sep21、Blog Oct22→Aug20为真实前界，Oct8/Sep8置顶另列，不混排序。MiMo十五Blog没有逐条2026日期证据，撤回“全2026”，保留目标日期未取得；Kimi26入口=25article+1release聚合，聚合原件仅[Oct27→Sep5相关段](CICERO-16KimiRelease.json)，0916-1015是促销期非本窗模型首公开。以上真实普通恢复不能授零事件/历史完整。
