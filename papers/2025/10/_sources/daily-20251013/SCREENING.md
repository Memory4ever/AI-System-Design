# 2025-10-13 有限筛选与必要反侧

作者Mill。本窗 `[2025-10-12T09:00:00+08:00,2025-10-13T09:00:00+08:00)`；fresh适用合同、ROADMAP与最新checkpoint实际重读。原始响应只作复查依据，不证明全部正文已读。完整题摘实际51个arXiv家族，另读Meta SPG官方完整题摘1个：合计52，46具具体潜力/日期隔离，6明确排除。2026-10-05T10:14:48+08:00按Peirce R-POOL反馈，作者新读原Atom中HiLoMoE10432v1完整题摘；不回填原50题摘范围，也不把复核者的其他新增阅读计为作者阅读。正式落窗候选0，不评分，正面Evidence0，Books提案0。未将年度库存或整类标题转逐篇全文队列。

## 查询与停止

[初查](fetch_manifest.json)35请求与[普通恢复](recovery_manifest.json)10请求保存本日原始参数/时间/响应。四主题API用结构化urlencode，`submittedDate:[202510110000 TO 202510122359]`，`start=0,max_results=30,sortBy=submittedDate,sortOrder=ascending`：

- 模型训练：`(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:transformer OR ti:MoE OR ti:pretraining OR ti:RLHF OR ti:Muon)`，实际30/total38；读与本次主题对应的16个非重复潜力题摘，加sourcing/inductive综述题摘，不把其余当强制队列。
- 运行系统：`(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (ti:LLM OR ti:GPU OR ti:inference OR ti:kernel)`，实际6/total6，完整题摘6。
- 多模态：`(cat:cs.CV OR cat:cs.RO) AND (ti:"world model" OR ti:"vision language" OR ti:VLA OR ti:"diffusion model")`，实际8/total8，完整题摘8。
- Agent：`(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:"agentic memory" OR ti:"tool use" OR ti:LLM OR ti:"language model")`，实际30/total59；跨类去重后选定14题摘（含两综述），不把其余库存强制排队。以上去重共44。

官方`cs.CL/2025-10?skip=700&show=100`实际100相关位置标题有界浏览，止于第800项，未续整月；补6指定题摘09309/09738/10013/10185/10444/10452，见[定点请求](point_manifest.json)。官方first-announced搜索：title=`language model`、computer_science all/include_cross_list、日期12～13、size50，实际200原响应明确no results；只说明此窄检索结果，不证零事件。API published与HTML日名均不证明最早互联网公开；当前v2/v3题摘不能填成v1机制。

辅助搜索实际3条日期限定query：`site:openai.com OR site:anthropic.com OR site:deepmind.google "October 12, 2025" research`；`site:research.google OR site:ai.meta.com "October 13, 2025" model`；`site:qwen.ai OR site:deepseek.com OR site:seed.bytedance.com "2025-10-12" OR "2025-10-13"`。只恢复Meta SPG官方原页，不采用community结果。另2条具名/日期query：`"SPG" "Sandwiched Policy Gradient" arxiv`（arxiv.org）与`site:platform.kimi.com/blog OR site:minimax.io/blog OR site:minimaxi.com/blog OR site:mimo.xiaomi.com "2025-10-12" OR "2025-10-13" model`。结果及实际必要core原响应保存[原返回](core_web_responses.json)；未无限追索。

## 46个具体潜力家族

下表版本为本日API所返当前题摘身份；必要安全笔记另明确实际v1，二者不混用。共同缺口是本次事件的官方历史首公开或实质修订bounds，必须完全落窗才能正式准入，不把未定日名写作窗外或已审重复。贡献只表示值得继续核验，不是已支持结论。

| 精确题摘身份 | 原约束 → 具体增量 → 待核选择 |
| --- | --- |
| [CLMN 10063v2](https://arxiv.org/abs/2510.10063v2) | 二元concept瓶颈 → 连续concept embedding与fuzzy rules → 表示可解释性和表达能力取舍 |
| [ADEPT 10071v1](https://arxiv.org/abs/2510.10071v1) | continual pretraining遗忘 → competence引导选择性层复制及unit重要性非对称LR → 扩容/更新保护 |
| [Pharmacist 10085v1](https://arxiv.org/abs/2510.10085v1) | harmful finetuning破坏alignment → bilevel safety coreset选择 → 数据数量之外的鲁棒暴露 |
| [Looped Transformers 10089v3](https://arxiv.org/abs/2510.10089v3) | 循环权重共享优化不稳 → loss landscape与SHIFT分阶段训练 → 递归容量的训练条件 |
| [PermLLM 10136v1](https://arxiv.org/abs/2510.10136v1) | N:M固定channel次序损失 → 可学Sinkhorn permutation/blockwise求解 → 结构化稀疏布局 |
| [BILLY 10157v2](https://arxiv.org/abs/2510.10157v2) | 多人格多模型开销 → 单模型融合persona向量 → 创造性组合与推理代价 |
| [AoU 10252v2](https://arxiv.org/abs/2510.10252v2) | 未支持premise进入推理 → validated subset posterior约束/不完美audit风险 → 自核与形式保证交接 |
| [Backdoor Collapse 10265v2](https://arxiv.org/abs/2510.10265v2) | 未知后门定位难 → known trigger聚合再clean recovery → 白盒修复代价/威胁条件 |
| [DynaSpec 13847v3](https://arxiv.org/abs/2510.13847v3) | 大词表draft开销 → context动态cluster shortlist/full-target verifier与执行流 → 保真与加速的交接 |
| [Compositional on-device 13848v1](https://arxiv.org/abs/2510.13848v1) | 多任务adapter顺序执行 → projection组合LoRA → 端侧summary+translation复合任务 |
| [CTR-LoRA 15962v1](https://arxiv.org/abs/2510.15962v1) | 均匀rank与更新幅度 → curvature capacity/Fisher-Hessian trust region → adaptation预算 |
| [SimKey 12828v2](https://arxiv.org/abs/2510.12828v2) | 精确token key易被改写 → semantic LSH prior-context key → 稳健检测与错误归属 |
| [RefusalBench 10390v1](https://arxiv.org/abs/2510.10390v1) | refusal检测与原因混同 → 176扰动、6类×3强度、检测/分类分离 → grounded refusal评价 |
| [STEAM 10398v1](https://arxiv.org/abs/2510.10398v1) | isolated likelihood编辑 → semantic-anchor latent alignment → knowledge edit跨表述一致性 |
| [Softmax >= Linear 10425v1](https://arxiv.org/abs/2510.10425v1) | linear attention分类解释不齐 → softmax/kernel功能梯度与adaptive LR理论 → ICL成立假设 |
| [HiLoMoE 10432v1](https://arxiv.org/abs/2510.10432v1) | vertical stacking串行依赖与flat MoE层级表示取舍 → rank-1 experts、依赖前层routing scores而非outputs的hierarchical routing使多层并行，并有三阶段训练 → MoE串并行依赖与参数预算选择；CTR四数据集题摘数字未作证据审阅，不外推LLM已验证 |
| [UltraLLaDA 10481v1](https://arxiv.org/abs/2510.10481v1) | mask diffusion长上下文extension → 专用RoPE/posttraining稳定策略 → 长程生成/recall边界 |
| [LAENet 10028v2](https://arxiv.org/abs/2510.10028v2) | onboard VQA质量/资源约束 → resolution/power/trajectory联合配置 → inference预算不只模型大小 |
| [SP-MoE 10302v2](https://arxiv.org/abs/2510.10302v2) | SD与expert offload交互 → speculative-aware prefetch cutoff/async I/O → accepted-token吞吐成本 |
| [ECO 10517v1](https://arxiv.org/abs/2510.10517v1) | code optimization没有性能反馈 → ROI/bottleneck symbolic advisor+retrieval → correctness与performance prompting |
| [FPO 09976v2](https://arxiv.org/abs/2510.09976v2) | flow策略importance likelihood不可算 → flow-loss proxy与structured credit → VLA RL质量/预算 |
| [MIMO 10011v1](https://arxiv.org/abs/2510.10011v1) | 文本指令难精确空间定位 → visual-ref input/pixel-ground output → 多模态表示接口；只核通用机制，不引入医学应用绩效 |
| [Ctrl-World 10125v3](https://arxiv.org/abs/2510.10125v3) | policy rollout与场景状态不稳 → pose/memory多视角action imagined rollout/ranking/SFT → 预测与执行差别 |
| [X-VLA 10274v1](https://arxiv.org/abs/2510.10274v1) | cross-embodiment接口不同 → embodiment soft prompts/标准transformer-flow → 动作共享与特定适配 |
| [Triangular Consistency 10487v1](https://arxiv.org/abs/2510.10487v1) | synthetic自训噪声 → image/query/answer重构三角一致性过滤 → 小幅收益成立条件，不因小模型排除 |
| [AdaViewPlanner 10670v1](https://arxiv.org/abs/2510.10670v1) | 静态view规划难 → video diffusion/4D branch和camera-extrinsic规划 → 不自动等于动作world dynamics |
| [ExpandSearch 10009v1](https://arxiv.org/abs/2510.10009v1) | 单query搜索限制 → RL query variants并行与独立squeezer技能 → 小模型检索预算/收益 |
| [SLEAN 10010v1](https://arxiv.org/abs/2510.10010v1) | agreement被当修复可靠性 → 15bugs/69propositions的弱agreement-quality关联 → coordination评价负面证据 |
| [Scheming 12826v2](https://arxiv.org/abs/2510.12826v2) | 显式要求作弊与自发混同 → 两LLM游戏分propensity/conditional success → 条件风险人口 |
| [DixitWorld 10117v1](https://arxiv.org/abs/2510.10117v1) | 单任务abduction评价 → storyteller创造与listener判别角色分账 → 多模态proxy边界 |
| [Hybrid OCR-LLM 10138v1](https://arxiv.org/abs/2510.10138v1) | copy-heavy格式错误/开销 → 25配置路由OCR vs LLM → extraction资源-正确性；不以企业应用标签排除 |
| [DiffHeads 10142v3](https://arxiv.org/abs/2510.10142v3) | 公平性/utility冲突 → DA/CoT差分attention mask → latent干预评价条件 |
| [Inductive Survey 10182v2](https://arxiv.org/abs/2510.10182v2) | inductive能力归因散乱 → sandbox观测覆盖/architecture-data分析 → 保留潜力，不凭survey标签排除 |
| [SAFER 10193v3](https://arxiv.org/abs/2510.10193v3) | finite sample coverage与filter风险混同 → budget不足abstention/独立conformal filter → 联合风险可支持条件 |
| [RLFR 10201v1](https://arxiv.org/abs/2510.10201v1) | RLVR sparse输出奖励 → latent flow velocity deviation reward → expert latent reuse |
| [SyTTA 10223v2](https://arxiv.org/abs/2510.10223v2) | test-time adaptation标签依赖 → input perplexity/output entropy四token → 无标签更新；不以农业样本排通用机制 |
| [Achilles 10238v2](https://arxiv.org/abs/2510.10238v2) | 参数冗余被当任意扰动鲁棒 → 极少critical neurons联合mask collapse → 干预权限/评测判定 |
| [MetaBreak 10271v2](https://arxiv.org/abs/2510.10271v2) | 在线服务special-token sanitization/moderator差别 → wrapper primitives/semantic mimic → 模型与服务防线交接 |
| [ArtPerception 10281v1](https://arxiv.org/abs/2510.10281v1) | ASCII识别不稳 → benign recognition pretest调参再attack → one-shot不等总攻击成本 |
| [MaskKV 09309v1](https://arxiv.org/abs/2510.09309v1) | diffusion双向cache利用 → mask-query head score/adaptive budget → cache eviction与质量 |
| [Judge's Verdict 09738v1](https://arxiv.org/abs/2510.09738v1) | correlation不是agreement → Cohen-kappa/z分人类相似与super-consistent → evaluator可用边界 |
| [PathDrift 10013v1](https://arxiv.org/abs/2510.10013v1) | 長CoT被当安全增益 → first-person/override/condition-chain反侧 → refusal与harmful fulfillment分开 |
| [MedAgentAudit 10185v3](https://arxiv.org/abs/2510.10185v3) | outcome正确可能掩盖失败过程 → key evidence loss/minority assimilation日志测量 → 通用协作失效机制，不采用医学应用指标 |
| [LISTEN 10444v2](https://arxiv.org/abs/2510.10444v2) | transcript能力被当声学理解 → lexical-acoustic冲突与prediction-marginal baseline → 音频评价盲区 |
| [SafeRAG 10452v1](https://arxiv.org/abs/2510.10452v1) | RAG benign contamination触发over-refusal → density/arrangement与activation direction → utility与真正harmful拒绝必须配对 |
| [SPG官方题摘](https://ai.meta.com/research/publications/spg-sandwiched-policy-gradient-for-masked-diffusion-language-models/) | dLLM单侧ELBO梯度偏差 → 上下likelihood界结合 → RL估计替代；原页Oct13无时区/时刻，不授落窗 |

SPG对应2510.09541，由具名官方页与arxiv搜索身份恢复；`Fri Oct10 16:52:25 2025`仍是提交线索，不证最早公开。精确v1 abstract访问实际cache miss，未以当前版本填v1。官方题摘已足以记具体潜力；落窗后才按准入校准展开证据，不遍历附件。

HiLoMoE来自原`arxiv_model_train.raw`首30的既有返回，本次作者定点新读完整题摘，未新增网络请求或扩查65 unique current IDs/月库存。原published/updated均为`2025-10-12T03:54:11Z`，只是提交元数据，不授first-public或完全落窗；仅恢复具体架构潜力，不评分、不授正面Evidence/Books。原查询选定44家族加本次1为45，原标题补检6加SPG1后为52；原44阅读不静默重写为已含HiLoMoE。

## 六个明确排除

10066v2 OBsmith：用LLM sketch测试JavaScript混淆器，没有服务模型/训练/推理的核心机制；10225v2 ISAAC：CPU验证的FPGA co-simulation与LLM辅助testgen，不是AI accelerator/LLM执行方案；10818v1 ProcessJ：generic协同runtime claim/release FIFO互斥形式证明，没有AI workload机制；10342v1 Traffic：CLIP/YOLO/MOG2加ordinal confidence的应用组合，未改变通用表示/推理；10161v2 Sourcing Survey：四维/prior-posterior分类归纳，题摘未新增具体设计或评价失效边界。日期未核，但无需为不影响处置的日期继续找材料。

21757v1 Agro-Consensus：农业病害caption应用组合，既有embedding/cosine/KMeans/HITL，没有通用机制增量；额外实读§3/4及Table1必要反侧：800图、PaliGemma3B、1 greedy+20 temperature=1候选，o1-mini对synthetic reference评分>=0.8；top4是任一cluster winner正确的集合oracle，不是top1自动决策。10-15生成不等移动端实际latency/cost验收。保留此评价限定，不将领域指标引入暂缓AI-for-Science或用主题关联凑准入。

## 18项必要core的实际边界

均为日期未定材料的风险限定，不是本窗正式Evidence；除Agro明确排除外仍保留潜力。以下足够处理具体命题即停止；没有代码复现、生产安全保证或全附件审阅。原返回与定位见core_web_responses，部分返回过长而被截时只采用实际重新显示的下列范围。

1. [Pharmacist v1](https://arxiv.org/html/2510.10085v1) III-A/B Eq1–6、IV-A：bilevel selector需harmful训练与validation，二阶项/内层一步近似，3个7–9B、BeaverTails/RepNoise及SST2/GSM8K/AGNEWS。unsafe classifier HS与top1 FA分账，仍有残留harmfulness，不授对任意更新免疫。
2. [Backdoor Collapse v1](https://arxiv.org/html/2510.10265v1) §3/4.1/4.4：whitebox、clean subset、主动注入两个known triggers再clean recovery；7/8B、SST2/AGNEWS/SafeRLHF、多类攻击，ASR与clean accuracy不同。有限adaptive prefix测试不认证消除所有unknown threats，tsne不证机制普适。
3. [Scheming v1](https://arxiv.org/html/2510.12826v1) §3.3–5：CheapTalk/PeerEvaluate的显式prompt或无promptpropensity与条件success独立；20–40小样本且成功率高时减样，未测全部pairing/temperature，CoT策略标签不证内在intent或真实环境比例。
4. [SAFER v1](https://arxiv.org/html/2510.10193v1) §3.1–3.3/limitations：finite M admissibility与Clopper-Pearson upper cap决定sample不足abstention；filter calibration只在correct-attainable子集，token NLL proxy不是真semantic entropy。exchangeability/shift依赖保留，不授生产失误上界。
5. [DiffHeads v1](https://arxiv.org/html/2510.10142v1) mask公式、evaluation及limitation：DA/CoT差分z-score topk置零，2516配对项/六属性、两个开放模型；Qwen14B judge将拒绝计公平，MBPP/GSM8K/MMLUCF utility另账，需head访问，不是human公平真值或proprietary通用控制。
6. [Achilles v1](https://arxiv.org/html/2510.10238v1) §3–4/Table1/必要strict评价：Gaussian activation sensitivity K100/alpha5排序，再greedy prefix mask至log-PPL倍率阈值1；最小仅相对排序prefix，不是全subset最优。21模型PPL与三个70B任务strict格式失败分开，需内部置零权限，不当外部prompt攻击或所有架构普遍定理。按Peirce实际exact-v1 A.3 L354–387的R-METRIC裁决补记（此附录新增阅读角色为Peirce，非作者重新通读）：HumanEval是代码提取率而非执行pass@1；MGSM是六类推理符号/结构标记超过0.2而非答案正确率；SimpleQA是ground-truth词包含率。MMLU-Pro strict extraction、IFEval strict compliance、GPQA fallback、MATH symbolic grading亦非统一口径；Table2七列0不授“七任务功能正确率全归零”或数学/代码能力普遍丧失。
7. [MetaBreak v1](https://arxiv.org/html/2510.10271v1) IV primitives、V-A/E/F、VI：chat template/embedding访问与online服务不同；SORRY judge fulfillment，不只拒绝词。每方法25阳性+25阴性人工抽样有FP/FN，末段拒绝可遮早期harmful；该分层样本不直接校正全体ASR，保留190失败样本的部分攻击/benign continuation，不宣称全部成功。
8. [ArtPerception v1](https://arxiv.org/html/2510.10281v1) recognition pre-test、§6.1/7.1–2：benign字体/方向/提示调参后Top1，故one-shot不含pretest成本。AdvBench50+HexPHI110、四7–9B、max2048；NRR可含disclaimer后服从，AHS按total queries归一，ASR为HS5/total。商业transfer有限且最佳open配置，不授完备攻击。
9. [AoU v1](https://arxiv.org/html/2510.10252v1) §3.1–3.6/4/6：有限action、bounded loss、perfect validator及真实posterior决定形式trace faithfulness；unit-cost oracle不代表token成本。实际三小模型/math任务prompt无外部核验，self-audit可错；实验single decoding与SC n20预算口径未齐，不把符号约束当LLM实现保证。
10. [SimKey v1](https://arxiv.org/html/2510.12828v1) §3.1–4/5开篇：semantic embed/hash替key而非新mark，k4/b4/window8、多idx minimum-cost统计依赖null分布。Llama8B及70B INT4/top-p0.9、translation/related-unrelated replacement；synonym仍可破坏nonsemantic mark，PPL近似不证明无失真或不可错误归属。
11. [RefusalBench v1](https://arxiv.org/html/2510.10390v1) §3.3–4.2/6：unanimous generator-verifier保留共享blind spots；100基题各自生成1600/1506，expert随机180各组pass93.1/88.3%，不是全量真值。检测F1/原因分类分账，极端拒绝降低miss但增false；English/generator-only不是端到端retrieval安全。
12. [PathDrift v1](https://arxiv.org/html/2510.10013v1) §3/4.4及AppendixC指标：first-person/override/template在AdvBench520的变化，目标token logit三次生成不证明全内部cognitive机制；refusal用phrase/regex，ASR另用GPT-Fuzz fulfillment，二者不互补。局部防御prompt不认证普遍安全。
13. [MedAgentAudit v1](https://arxiv.org/html/2510.10185v1) §3.2–3.3与collaboration failure：300pilot/3600logs、两annotator、heldout200 kappa0.82；KEU retention、少数意见变动、audit observer测过程，正面outcome可来自初始一致而非interaction纠错。一般协作测量保留潜力，不采用临床有效性或v3新增论点。
14. [Judge's Verdict v1](https://arxiv.org/html/2510.09738v1) §1.2/3–5：1994×3 annotator、六RAG QA集，reference比对0/.5/1，先r>=.8再kappa/z、54judges；z阈值改变分类，三人pair差不是总体标准误，super-consistent不是独立可靠性保证。不给所有judge/开放生成任务外推。
15. [LISTEN v1](https://arxiv.org/html/2510.10444v1) §3–5：7939短音频问项、381mismatch，五音频模型/三输入模式、随机选项，micro accuracy与uniform/majority/prediction-marginal分账。Neutral text真值都是neutral使text高分，不能与audio情绪任务简单当增益；冲突下lexical依赖是局部反侧，不证所有音频理解不存在。
16. [SafeRAG v1](https://arxiv.org/html/2510.10452v1) §3–7：2970构造样本/495test、k3/5/7、benign/harmful arrangements；目标centroid减overrefusal方向。layer/alpha调参用了test中validation slice，结果只有benign ORR两7/8B，未同时证明legitimate harmful refusal保留；linear separability/shift限制，不以zero retraining宣传代认证。
17. [SLEAN v1 PDF](https://arxiv.org/pdf/2510.10010v1) p1–2协议/p7人工fix核验/p8–9统计/p12limitation：15bugs、69提案22accepted，作者人工应用测试；workflow固定不等输出确定性，convergence弱相关不证任意多模型投票更可靠；仲裁与AIA同架构有bias，未达企业大仓库/并行验收。
18. [Agro-Consensus v1](https://arxiv.org/html/2510.21757v1) §3/4/Table1：排除处的预算/oracle/LLM scorer反侧已处理，不遍历全caption提示附件。

## Books与恢复

日期合格候选0，不存在本日经独立证据复核的长期差额，提案/写入0。这不是所有潜力主题“已有覆盖”的断言，也未以Books现有范围排除上述增量。[FIRST](FIRST_INDEPENDENT_REVIEW.md)及[FINAL](FINAL_INDEPENDENT_REVIEW.md)的原六FIRST、六排除分层、18必要反侧、14有限来源与日期隔离有效复用。R-POOL/R-METRIC已按上述角色与边界窄同步；只剩Peirce实际写后回核与DAY裁决，不重跑14源或52正文，作者不填通过。

来源终态保留：Google年级pubs与DeepMind历史、Meta原页/具名SPG日期、Qwen新壳、Hunyuan2025目录、Z.aiOctober缺段、MiMo Blog和MiniMax三入口历史。已做普通恢复/news、US、page2。MiMo原SSR More是`aria-controls=blog-more`折叠展开，未证明历史分页，不能继承旧外链解释。Hunyuan本日有限Chrome尝试实际Browser is not available: chrome，无browser列表；官方POST total11全2026不是历史补证。得到本窗官方原目录/公告或完全落窗公开bounds后，仅对应身份/源重开；当前均不授正面证据、Books、无遗漏或性能安全保证。
