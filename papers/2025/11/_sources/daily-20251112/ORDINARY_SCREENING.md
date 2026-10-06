# 2025-11-12 普通有限题摘筛选

作者Noether。本轮实际读134个唯一exact-v1完整题摘；不是134篇当窗新论文或确定候选。四个窄主题列表并集151个身份仅用于范围/语义线索，模型宽查询282只取60后收窄，不续全282，月表1527不转队列。实际来源与版本边界见 [SECOND](./SECOND_CALIBRATION.md)。

原XML：16项[batch1](./arxiv-exact-v1-batch1.xml)已在SECOND逐项写理由；24项[batch2](./arxiv-exact-v1-batch2.xml)、17项[formation tail](./arxiv-exact-v1-formation-tail.xml)、38项[MM tail](./arxiv-exact-v1-multimodal-tail.xml)、20项[ambiguity tail](./arxiv-exact-v1-ambiguity-tail.xml)、10项[final ambiguous](./arxiv-exact-v1-final-ambiguous.xml)、9项[final missing](./arxiv-exact-v1-final-missing.xml)在下表。全部134个实际entry suffix为v1，无重复；final第一请求默认max10，仅返回10/19，缺9随后显式max30定点补齐，没有把第一响应称19已读。执行见[第一请求](./12-final-ambiguous-exec.json)、[缺9](./12-final-missing-exec.json)及既有各批exec。

`潜在`表示原约束→实际增量→可能改变的选择已可指出，但首次公开落窗未核，**不进入确定候选、正面Evidence或Books**；不因日期问题或没有owner算法名强造长期缺口，也不把这些条目转全实验/全owner队列。原submitted/published/updated/题名/完整AB均保留XML原字段，current v2+只作身份/纠错线索。共同日期停止和最小重开见SECOND，得到真实官方first-public bounds/公告后才定点恢复该ID。`关闭`只关闭具体贡献/范围，不对学术价值或未读正文下结论。

## Batch2：24项完整v1

| v1 ID/身份 | 实际筛选理由与边界 |
| --- | --- |
| 2511.05650 BACo | 潜在：base/aligned模型的多样性质量冲突→uncertainty/semantic-role token路由→局部多模型协作选择；3tasks/13metrics/21.3%不授普遍router保证。 |
| 2511.05722 OckBench | 潜在局部评价：同accuracy模型消耗token仍相差大→reasoning/code质量-token前沿比较→可修正只看accuracy选型；不是仅因“成本重要”计贡献，也不将model/hardware-agnostic指标当实测latency/energy。 |
| 2511.05745 MoE-SAE | 潜在：冗余SAE features→多expert分工与activation frequency scaling→稀疏特征覆盖/专门化机制；不是LLM MoE router名字即owner。 |
| 2511.05784 DRAGON | 潜在：context harmful knowledge输出→训练negative scorer并用reasoning构造动态guard→行为控制分支，**不证明参数删除**；两个原OpenReview触发均失败/challenge，保留必要public字段缺口。 |
| 2511.05797 Plugins | 潜在重要反侧：插件把非用户role/content引入高信任上下文→真实role forgery/tool instruction攻击与修补后残留→具体integration边界；必要core见[THIRD](./THIRD_CRITICAL_CALIBRATION.md)。 |
| 2511.05804 Spectral | 潜在：生成前context污染检测→谱特征/两regime门控→局部检测路径；118controlled样本及理论假设不授通用kill switch，§7必要反侧见THIRD。 |
| 2511.05814 MoE Offload | 潜在：expert访问局部性与替换/预取互相制约→trace比较LFU/LRU与prefetch策略→offload选择须依负载，非所有MoE固定策略最佳。 |
| 2511.05832 Hilbert Attention | 潜在：二维邻接window不好直接执行→Hilbert重排为连续block sparse→局部attention/执行计划接口；4x/18x是不同kernel对照，不能当全LLM端到端速度。 |
| 2511.05850 Retrieval at Context Limit | 潜在负证据：长context必有lost-in-middle这一泛化→Gemini2.5Flash factoid needle到limit仍无该模式→收窄模型/任务判断，不授所有长程推理。 |
| 2511.05852 Edits Decay | **撤回链不采用**：本日已读v2原withdraw声明/current history；不回用v1 232configs，不评分/Books。未来v3/v4不同题名/254配置不倒灌；保留精确恢复位置见THIRD。 |
| 2511.05854 LEAP | 潜在：小模型事后hallucination检测→teacher failures生成自适应计划、distill及proactive verification→前置证据验证学习，不只流程改名。 |
| 2511.05867 MCP-RiskCue | 潜在：系统log中的MCP风险与泛化false positives→9risk/1800synthetic logs、SFT与RLVR比较→局部风险识别训练选择；243servers、2421train/471test只作者AB，非真实runtime安全保证。v1题名不改为current新名。 |
| 2511.05874 Code Thinking Steps | 潜在局部反侧：减少CoT步数被当一致收益→6codeLLMs/100BigCodeBench/21humans与controlled-step budget，收益按难度变化→reasoning成本不能脱离task困难度。 |
| 2511.05933 Hierarchical Traversal | 潜在：RL仅损害memorized facts这一叙事→RL在层级recall更好、结构prompt把DeepSeekV3/R1 gap24pp降7pp、query/fact activation差异→需要区分知识可访问程序与知识本身；医学code只是recall探针，不引入诊疗研究，也不把不同checkpoint相似性当完整因果。 |
| 2511.05993 Entropy RL | 潜在：entropy collapse只归全token→positive-advantage token、off-policy/clip及正负相对权重方向→可改变GRPO探索控制；不是全模型普遍规律。 |
| 2511.06090 SWE-fficiency | 潜在评价盲区：patch正确不代表真实性能优化→498tasks/9repos有真实workload与专家performance patch，agents<.15expert speedup→功能tests与性能证据需分离。 |
| 2511.06209 UHeads | 潜在：每步large-LLM验证成本→frozen-state小uncertainty heads、自/teacher label→局部verifier表示/成本选择；v1不是current ReProbe名或后续配置。 |
| 2511.06222 SPA | 潜在：trust/helpfulness冲突→lexicographic阈值后helpfulness偏好、uncertainty-weighted loss→对齐目标排序条件；unsupervised标注不当外部安全真值。 |
| 2511.06380 AEPO | 潜在：echo反思引入无效/重复信息→information filtration与adaptive entropy优化→reflection训练目标控制，而非多写一次prompt。 |
| 2511.06419 MONICA | 潜在：最终答案监测遗漏中间sycophancy drift→step monitor与calibrator阈值→reasoning轨迹控制；12sets/3LRMs局部，不授全runtime正确性。 |
| 2511.06430 CG-TTRL | 潜在：端侧test-time RL无新label→context选择、majority pseudo-label、探索更新→context与训练反馈耦合；三步8%vs1%是不同配置局部声明，非免费在线持续学习。 |
| 2511.06446 SR-KI | 潜在：检索文本token成本→KB encoder产生KV/专用retrieval layer、supervised attention→权重外知识接口；7B/A10040GB/40KKB的Recall/压缩范围绑定，不授全面事实正确性。 |
| 2511.06512 EASE | 潜在：小模型直接refusal易过度拒绝或unsafe→teacher选择与危险reasoning/直接拒绝分支训练→小模型alignment反馈策略；安全proxy与成本仍仅摘要声明，日期hold不自动展开全部实验。 |
| 2511.07483 C2RM | 潜在：correctness-only reward忽略低信心正确→confidence-aware penalty→static/BoN/PPO评价下校准/探索选择；不能把置信度等同正确性。 |

## Formation Tail：17项完整v1

| v1 ID/身份 | 实际筛选理由与边界 |
| --- | --- |
| 2511.06852 DBDI | 潜在重要反侧：单refusal direction→harm detection/refusal execution拆分及非对称干预→white-box alignment脆弱路径；necessary条件、简化模板与对照混杂见THIRD。 |
| 2511.06161 LATTLE | 潜在：异域tabular迁移encoder不匹配→选定LLM K/V transplant与gating→Attention参数迁移分支；10pairs/12baselines范围，不因tabular一词关闭一般参数转移机制。 |
| 2511.06778 SAFENLIDB | 潜在：SQL correctness与privacy/security目标冲突→synthetic hybrid-CoT/warm-up/alternating preferences→局部稳定对齐；不授所有数据库接口安全、仅prompt防护不等enforcement。 |
| 2511.07396 C3PO | 潜在：unlabeled reasoning cascade无固定成本保证→regret/MPM与conformal probabilistic budget→统计成本边界；probability条件不等deterministic runtime SLO。 |
| 2511.05704 TabDistill | 原摘要关闭改判为潜在：few-shot Transformer teacher参数/复杂度高→蒸馏为小NN并在同等训练数据下比较质量→局部参数–质量选择边界；不能因无新反馈算法或预算未全核关闭明确局部资源证据。依据[Ohm ORDINARY](ORDINARY_INDEPENDENT_REVIEW.md)及原formation v1完整AB；日期仍held，不授普遍替代、评分、owner/Books或全methods完成。 |
| 2511.06942 HLPD | 潜在：machine-revised文本破坏完整生成检测→human preference reward改变scorer token分布/五维adversarial revision评价→检测器目标/失效边界；AUROC不同生成/修订配置不当通用鉴定。 |
| 2511.06168 Chasing Consistency | 潜在：answer准确不证明CoT与human reference路径一致→semantic alignment metric+SCOS错误类别sampling→局部faithful reasoning评价/优化；reference一致不等唯一正确解释。 |
| 2511.06294 Transolver | 关闭当前阶段：PDE PhysicsAttention slice/deslice线性operator关系服务科学计算，按ROADMAP AI for Science暂缓；不通过Attention owner重新引入科学solver。 |
| 2511.07498 LAHIS | 潜在：多语语言切换/偏离→language-specific/general heads识别、soft20参数mask→语言路由与共享表示选择；单forward/back归因不授全部跨语保证。 |
| 2511.07110 Two Heads | 潜在：LLM feature一次性整体distill→layer/task/data分解、probe与Hájek-MoE→小模型特征迁移选择；finance market-making是受控案例，不据此宣称投资/普遍性能。 |
| 2511.10676 Expert Prediction | 潜在：等待attention后才知道expert→pre-attention ranking预测/同层或首层prefetch→通信与计算重叠路径；93–97%routing accuracy不是端到端throughput。ID较晚不抹掉原submitted/未知public差别。 |
| 2511.07419 RoMA | 潜在：task变化router泛化失效→成功路由邻域manifold regularization、冻结base只调router→MoE routing训练选择，不授所有任务胜出。 |
| 2511.06818 Focal Attention | 潜在：固定attention分布与噪声→固定/learned temperature scaling局部parameter/data/long-context对照→集中度成立边界；不是因temperature原则老就关闭新局部证据，也不授无条件42%/33%资源节省。 |
| 2511.06776 DTA | 潜在：teacher synthesis与student分布错位→teacher trajectory按student bias/signals筛选、两阶段蒸馏→domain训练数据取舍；telecom math不同thinking配置的energy/latency不混成普遍率。 |
| 2511.11641 EcoSpa | 潜在：普通结构剪枝破坏矩阵乘积对应→coupled row/column sparsity→训练/模型结构低成本分支；1B/GPT2各配置收益不合并，晚ID未核first-public。 |
| 2511.06160 PRIME | 潜在负证据：biased reasoning只看答案→stereotype/anti/neutral匹配logic-grid puzzles→推理路径与偏差评价局部边界，不授所有人群/模型普遍差异。 |
| 2511.07070 RedOne2 | 潜在：domain RL/SFT只预期稳增→RL-SFT-targeted-RL受控SNS与OOD性能取舍→后训练顺序/分布选择；旧pipeline名字不单独贡献，局部反证仍保留。 |

## Multimodal/Agent Tail：38项完整v1

| v1 ID/身份 | 实际筛选理由与边界 |
| --- | --- |
| 2511.06455 Semantic Mapping MAS | 关闭贡献：多agent把关系数据映到Schema.org、mapping精度>90%是新业务应用；AB未指出新的训练、执行权限或失败控制机制，不仅因agent组合名排除。 |
| 2511.06448 Fraud | 潜在重要反侧：单对话refusal不能概括多agent诈骗链→collusion与双指标/benign模型差异→局部安全评价；原simulation/limits已核THIRD，不当真人被骗率。 |
| 2511.06202 ExpReS-VLA | 潜在：少量robot demonstrations成本/更新不稳→frozen visual feature memory、success-prioritized replay/hybrid contrastive→VLA训练与检索budget；12demos/5physical tasks/31sRTX5090只是对应配置。 |
| 2601.05265 CDTA | 潜在：跨文档topic被固定chunk切断→topic segments/aligned synthesized chunk→检索表示/索引成本与faithfulness选择；Jan2026 ID与Nov8 submitted不能互换public，不迁移至12候选。 |
| 2511.06582 TabRAG | 潜在：表格retrieval只更新embedding→structured-language parsing representation→retrieval granularity/训练成本取舍；NeurIPS AI4Tab仅身份触发线索，非首公开时刻。 |
| 2511.07410 VLM Closed-loop Planner | 潜在：一次symbolic plan难应反馈→planning horizon/warm start控制比较→VLM robot loop局部稳定边界；不外推classic controller theorem到LLM runtime。 |
| 2511.05923 FCCT | 潜在：object hallucination无法定位多modal通道→token/MHSA/FFN causal tracing与IRI干预→局部表示/输出控制；not通用事实保证。 |
| 2511.07290 CAMP-VQA | 关闭贡献：BLIP2 captions/metadata/keyframes辅助压缩UGC的MOS质量预测；核心是no-reference视频质量任务模型组合，未指明foundation形成/生成机制或改变主线的失效证据。 |
| 2511.07068 ClusterMine | 潜在：无positive ID标签下CLIP OOD难分→visual cluster+text concepts相互一致mining→表示与OOD校准条件；not所有标签-free检测可靠。 |
| 2511.06252 MrCoM | 潜在：多场景world model latent互相干扰→meta-state/value regularization与dynamics decomposition→scenario transfer约束；同engine场景不当全部世界迁移。 |
| 2511.06678 Flexible CBM | 潜在：固定concept词表受限→embedding-conditioned hypernetwork与sparsemax→concept bottleneck可扩展性；未见concept一epoch局部不等全部语义可解释。 |
| 2511.06449 FLEX | 潜在：agent experience仅静态提示→success/failure reflection library growth/inheritance→经验状态更新机制；这里只保留math方向，ProteinGym/chemistry不绕暂缓边界。 |
| 2511.05791 VLAD-Grasp | 潜在：language目标不能直接落动作→goal image/depth segmentation/PCA对应→physical grounding接口；training-free不等无失败或全场景grasp安全。 |
| 2511.05991 Ontology KG | 潜在：TextKG与DBKG只看retrieval分数→one-time ontology/构建成本与不同retrieval对照→索引质量/生命周期成本取舍；不授GraphRAG普遍优势。 |
| 2511.06125 QUEST-LOFT | 潜在重要纠错：原gold错/争议混入→人工revised gold、structured QA/verification模型分层→RAG-vs-long-context比较改变；小集/overfit/CoT非全增益已核THIRD。 |
| 2511.05931 SAGE | 潜在：经验不能重用为plan→grounded rollout abstractions复用policy refinement→plan状态/反馈学习；MiniSWE GPT5-high相对提升、73.2/74 Pass1不跨framework硬拼。 |
| 2511.05894 Open-world Scene Graph | 潜在：open-vocab objects与关系难直接给planning→3D graph/vector-RAG状态表示→grounded检索规划接口；这里只潜力，不将pipeline组合自动当长期gap。 |
| 2511.06225 MoRA | 潜在：missing-modal条件直接LoRA不足→shared/modality-specific低秩分解和双向interaction→多modal适配机制；不是将临床missing modality任务当新病理研究。 |
| 2511.06490 Comics Zoom RL | 潜在：细粒度视觉信息在全图表征丢失→region zoom作为RL行动→tool-conditioned视觉训练取舍；comic仅局部任务，不外推一般视觉runtime保证。 |
| 2511.05936 VLA Challenges | 关闭贡献：10挑战/趋势综述提供路线归纳，AB未提出新机制或可修正既有判断的具体比较反证；不是据“review”标签一律排除。 |
| 2511.06899 RPTS | 潜在：correct answer掩盖wrong multimodal reasoning→390instances/374images tree关系评分→过程faithfulness评价盲区；not树形分数就是事实正确。 |
| 2511.07328 Q-RAG | 潜在：多步retrieval bottleneck不在生成器→value-based embedder RL→10M context retrieval训练路径；未调LLM不授没有索引成本。 |
| 2511.06240 Base Placement | 潜在：语义目标到可达base pose不一致→affordance/geometry coarse-to-fine exploration→动作前约束控制；OVMM5tasks85%只局部，not全机器人保证。 |
| 2511.06262 GAIA | 潜在形式设计：授权/信息不足的B2B委派→TCI+显式state transition、四invariants、parallel feedback→commit前权限/信息控制接口；validation blueprint非实证安全。不能仅把治理术语计新算法，若日期恢复只核形式机制是否真比已有delegation多出约束，不扫全部owner。 |
| 2511.06251 WebVIA | 潜在：静态截图生成忽略可交互状态→multi-state exploration与code validation→UI-agent评价/反馈范围；未将组件接起来本身计长期贡献。 |
| 2511.06005 Intersectional VLM Bias | 潜在局部负证据：reasoning增强被当更公平→5models/32jobs/3prompts/FairFace intersectional比较→模型/推理模式偏差判断需条件化；not全社会偏见率。 |
| 2511.06651 NOVO | 潜在：VLM-SAM依专用SEG embedding→visual mask/point prompts+training-free boundary refinement→跨模型表示接口替代；not无需任何数据/所有segmentation稳增。 |
| 2511.06619 VLA inherits VLM | 潜在：emoji absent robot data仍可action transfer→freeze/PEFT/co-training/action latent控制→VLM能力到VLA不必同条件继承的评价盲区。 |
| 2511.06496 Low-rank Hallucination | 潜在：多caption voting代价/错误相关→consensus/residual low-rank选择→局部质量-cost比较；driving87%/51–67%runtime各绑定对照，consensus不是truth。 |
| 2511.06946 Gaussian World Attention | 潜在：uniform recent-window截断有用history→structured informative-history attention→partial-observation World Model memory取舍；Atari100K/UniZero HNS不授LLM上下文优劣。 |
| 2511.07238 Semantic OOD Variation | 潜在：视觉域shift只image augmentation→text semantic-distance variation训练→foundation表示/OOD augmentation分支；driving segmentation局部，不授所有OOD。 |
| 2511.07112 More Agents | 潜在负证据：更高mathaccuracy不等扰动鲁棒→same-model voting/多noise/task残留gap→协作评价需分任务与成本；必要限制已核THIRD。 |
| 2511.08637 Data Consent | 潜在数据链反侧：web availability被当consent→DataComp CommonPool12.8B的domain ToS/watermark sample测量→provenance证据可缺；122M版权/60% top50/9–13%标记是作者估计与CI，not法律许可判定。 |
| 2511.06182 OpenVLN | 潜在：aerial navigation sparsefeedback/limited demo→ruleRL/value-action长程planner→动作训练边界；TravelUAV模拟4.34SR等指标不授生产无人机安全。 |
| 2511.06146 Spatial Reference | 潜在负证据：VLM空间language答案好不等grounded细分→ambiguity/negation/category/relative expression对照→spatial grounding评价边界；not所有模型不可用。 |
| 2511.06653 HiMo-CLIP | 潜在：长text扁平matching→PCA semantic hierarchy+monotonic contrastive loss→compositional representation对齐；不改encoder并非没有训练成本。 |
| 2511.06073 Licensing Oracle | 潜在：hallucination无外部许可边界→formal KG/SHACL licensing→事实许可接口；same-v1 PDF graph completeness/time/multihop反侧本日定点复用见THIRD，not必要充分保证一切truth。 |
| 2511.05680 VLM Skill Selection | 关闭贡献：以VLM挑既有robot assembly primitives/imitation skill，AB只报告组合的assembly成功；未指出新的action闭环/机制或改变设计的控制反证。 |

## Ambiguity Tail：20项完整v1

| v1 ID/身份 | 实际筛选理由与边界 |
| --- | --- |
| 2511.05929 CoMA | 潜在：固定mask使spatial pretraining冗余→complementary uniform masks/层级dynamic multi-window→视觉训练数据与计算取舍；ImageNet12%epochs/10%per-epoch只局部。 |
| 2511.06048 SAE Visual Exploration | 潜在诊断设计：全feature UMAP出现邻接/压缩伪象→curated subset与topology-preserving encoding→解释SAE关系的测量边界；工具展示不当模型真因果结构或全部feature已核。 |
| 2511.07086 Explainable Processes | 关闭贡献：Vester/game/symbolic已有分析工具接LLM形成物流决策工作流、100runs/LLMjudge因子/role结果；没有新的foundation训练、runtime控制或具体主线失效机制，审计artifact不是可靠性证据。 |
| 2511.05924 Kernel→Attention | 潜在理论：density/score估计与Transformer关系未明→distribution-agnostic/equivariant cross-attention operator恢复KDE→attention统计表示条件；不因非language任务关闭一般模型理论。 |
| 2511.06044 Random Batch Attention | 潜在：graph attention memory/并行成本→particle random-batch近似、收敛/表示条件→attention近似成立边界；not全部图任务收益。 |
| 2511.06668 Contradictory RAG | 潜在负证据：semantic similarity不保证一致证据→时间/contradiction选择对照→RAG证据链控制；necessarycore条件/指标混杂见THIRD，not医学机制采用。 |
| 2511.06065 ScRPO | 潜在：GRPO错误样本用完即丢→error pool反思/交替训练→reasoning反馈数据/优化路径；1.5/7B math局部，不用流程名自动计贡献。 |
| 2511.06348 GazeVLM | 关闭贡献：RGB/HHAdepth与task prompts联合完成gaze/target任务，AB核心是统一新应用和评价；未识别general foundation形成/跨模态机制的新差额。 |
| 2511.05913 NILC | 潜在：embedding-first clustering缺闭环→LLM semantic-centroid、hard-sample rewriting与cluster反馈/soft mustlinks→检索/表示迭代选择；六intent benchmarks局部，不当所有聚类改进。 |
| 2511.05823 AiEDA | 关闭范围：chip design-vector extraction/iDATA/EDA七任务平台，核心是AI辅助芯片设计应用；不把“EDA系统”映到AI训练/推理硬件机制，没有实际LLM kernel/accelerator新设计证据。 |
| 2511.06006 DDP Medical Denoising | 关闭贡献：U-Net Xray DDPM+DDP/AMP已知工程组合到新任务，60/40%只是对应配置；Gaussian noise的data obfuscation**未证明DP或隐私保证**，不采用该安全措辞。非医学/隐私结论，无需全实验展开。 |
| 2511.07171 Federated Violence | 潜在局部energy-quality反侧：默认VLM比轻CNN全优→nonIID federated violence案例240/570Wh与不同semantic类别能力→资源约束下模型选择需条件化；simulation不等实际privacy/部署保证。 |
| 2511.05859 PFRP | 关闭范围/贡献：univariate forecasting Global Memory Retrieval回收过去pattern、8.4%任务收益；未识别foundation学习或LLM记忆控制的新增机制，不用通用Memory owner类比入池。 |
| 2511.05752 Feature Pyramid Text GNN | 关闭贡献：LLM multi-scale features+GNN用于text classification，新增ACC/F1/AUC任务组合，不是训练/表示成立条件或设计反证；不是因为AB缺实验明细。 |
| 2511.05820 WAR-Re | 关闭贡献：ProgrammableWeb API-set推荐的cardinality/start-stop token SFT/GRPO排名改进；不是实际tool执行、commit/enforcement或调用协议新控制；不因Web API字样引入AGENT-TOOL-CALLING。 |
| 2511.05747 CoT-X | 潜在：异模型CoT长短/表示错配→importance/budget/coherence分段压缩与Bayesian优化64modelpairs→reasoning trace转移quality-cost；medical7501是局部task，不引入临床知识、不授40%普遍率。 |
| 2511.05682 VMDT | 潜在重要反侧：video capability或低HGR被当整体安全→BR/HGR、frame sampling/judge与模态分层→安全测量条件；原necessarycore见THIRD。 |
| 2511.05963 Next-Lat | 潜在：仅next-token supervision隐藏belief state→next-latent self-supervised auxiliary目标、无arch/infer变化→compact world representation形成理论；not name缺位的Books gap。 |
| 2511.06077 STCA/Douyin | 潜在：超长history重复target计算→target/history cross-attn、same-user多个target共享RLB、short-train/long-infer→计算/状态复用分支；10K/billion recommender生产配置不外推LLM通用SLO。 |
| 2511.05980 TS Imputation | 关闭范围/贡献：time-indexed TabPFN-TS/MoTM在33组时序插补/1.3Mwindow的new-task zero-shot评测；未识别主线foundation形成的新条件/机制，不因foundation名称收全部预测。 |

## 最后19项：完整v1，不是全方法队列

| v1 ID/身份 | 实际筛选理由与边界 |
| --- | --- |
| 2511.05706 AdvisingWise | 关闭贡献：authoritative institution retrieval/draft+每回答advisor validation，20queries/8advisors评价主要utility/态度；HITL新应用不提出新授权/执行机制或主线失效边界。 |
| 2511.05766 Anchoring | 潜在负证据：输出表面bias不解释内部probability→logprob分布+exact Shapley prompt-field归因、contamination controls→局部bias测量与prompt设计稳定性；6小模型差异不外推scale因果。 |
| 2511.05849 EGG-SR | 关闭当前阶段：physical-law symbolic regression/e-graph及scientific discovery算法，虽有MCTS regret/DRLvariance证明，本项目AI for Science暂缓，不以LLM feedback通用节点重新引入。 |
| 2511.05872 TabPFN TSP | 关闭贡献：TabPFN node-predicting adaptation/fine-tune到TSP路线，AB以新应用、少样本/size-generalization指标为主；未提出改变foundation训练或系统设计的具体机制/反证。 |
| 2511.05876 MoEGCL | 潜在局部表示：coarse view graph fusion→sample ego-graph MoE融合/cluster-level contrastive→表示融合粒度取舍；不当语言MoE routing，也不因general graph一律关闭形成机制。 |
| 2511.05878 FusionLog | 潜在局部teacher/student：cross-system general knowledge与private日志错配→training-free semantic partition、private multi-round distillation/pseudolabel→zero-label迁移条件；三logsets>90%只局部，不当AI-serving可观测性新平台。 |
| 2511.05885 Speeder | 潜在：长item描述memory/compute成本→representation compression/sequence-position/progressive modality优化→多modal序列训练取舍；recommendation250/400%只是对应MLLM-SR配置，不泛化全部LLM。 |
| 2511.05903 Imperfect Learner | 潜在有限state设计：LLM准确回答难模拟渐进知识→developmental hierarchical memory/consolidation→user simulation的derived-memory状态更新；NGSS教育案例不授真实儿童心理/学习效果或全部agent memory机制。 |
| 2511.05965 Registration Agents | 关闭范围：image-pointcloud配准的IAS/RAI几何correspondence，agent指feature代表/RL选择，不是LLM agent控制；RGB-D/7Scenes SOTA不支持当前foundation/system主线新机制。 |
| 2511.06019 MiVID | 潜在局部生成训练：缺高帧率groundtruth/occlusion→3DUNet+temporal attention diffusion、progressive masking/adaptive loss→self-supervised temporal生成分支；CPU/9frames/50epochs不授通用video foundation scalability。 |
| 2511.06023 Multi-Reward GRPO | 潜在：文化-specific多维bias难单reward→Chinese-context合成English pair、DeBERTav3多维fairness/neutrality/quality reward→alignment目标标注条件；不将synthetic reward降低等同真实公平或无损能力。 |
| 2511.06247 Tetris/CDSP | 潜在：dynamic SP请求级粒度难适配stage/负载/碎片→intra-request token chunks不同SP、PD/load扩张和chunking→长context服务分配粒度改变；4.35xTTFT/40.1%TBT/45%容量均作者up-to，不授同一配置同时实现。 |
| 2511.06260 Traffic Representative | 原摘要关闭改判为潜在：逐traveler调用LLM成本→同决策上下文同质群体共享一个LLM代表、mixed strategy与外部decaying-step更新→调用聚合粒度/成本选择。依据[Ohm ORDINARY](ORDINARY_INDEPENDENT_REVIEW.md)及原final v1完整AB；只恢复此窄机制，不把交通user-equilibrium定理外推通用runtime可靠性。日期仍held，不新增确定候选、评分、owner或全收敛证明审阅。 |
| 2511.06283 TinyChemVL | 关闭当前阶段：化学视觉token/反应识别预测共同优化，核心科学领域模型/task；按AI for Science暂缓，不借token reduction owner重新引入。 |
| 2511.06441 Learned Routing | 潜在：always-premium成本→learned route及two-stage vision专家→quality-cost选择；同v1本日AB独立读，root11已核原成本表文冲突只定点复用，不把67%调用降低当可信E2E成本保证。 |
| 2511.06838 P3-LLM | 潜在：FP16 PIM area/power限制→hybrid-format量化/PIM iso-area协同/算子fusion降dequant→不同operand的memory-compute设计；4.9/2.0/3.4x不同accelerator对照，不授硅片实测/通用NPU吞吐。 |
| 2511.06973 Spreadsheet Templates | 关闭贡献：cell embedding/type/spatial+Chamfer/Hausdorff用于template clustering，FUSTE ARI1.00vs.90；RAG只是可能downstream，非本篇检索生命周期/基础模型机制证据。 |
| 2511.07166 AdaRec | 关闭贡献：narrative user profile/peer行为+preference因果提示到ecommerce recommendation，few/zero-shot与synthetic SFT任务收益；AB未给改变通用形成/推理/agent机制的具体新条件，not因无算法细节排除潜在贡献。 |
| 2511.06000 DemogSummary | 潜在局部faithfulness反侧：abstractive摘要保留内容被当保留人群属性→age-stratified summaries/DSS实体保留和hallucination比较→摘要评价遗漏的条件；仅保留LLM证据保真问题，不采纳医疗干预/领域研究。 |

## 17条明确范围标题关闭（未读AB，不冒称完整题摘）

| 发现ID | 标题层明确范围理由 |
| --- | --- |
| 2511.05696 | breast-cancer临床试验eligibility prescreening工作流应用，非当前模型/系统机制。 |
| 2511.05726 | protein-ligand/gene药物发现，AI for Science暂缓。 |
| 2511.05730 QiVC | 原标题关闭改判为潜在：Ohm新增完整exact-v1 AB明确低维旋转集成QiRE概率权重表示进入一般variational convolution、无额外参数的结构化不确定性学习，biosignal仅验证任务。依据[独立原题摘记录](ORDINARY_INDEPENDENT_REVIEW.md)，不冒称作者原134已读此AB/本地已有该API响应；仅恢复通用参数表示/训练条件方向，日期held，不采用临床/量子硬件加速、不评分或扩methods/owner。 |
| 2511.05769 | youth mental-wellbeing personalization共创体验研究，不是模型训练/运行机制。 |
| 2511.05841 | handwriting-based Alzheimer's screening跨task适配，科学/临床应用暂缓。 |
| 2511.05863 | EEG emotion V-A contrastive representation的生理信号情绪分类任务，标题未显示当前foundation/model系统切片。 |
| 2511.05901 | 医学RAG技术实现/临床应用/伦理scoping review，领域路线暂缓。 |
| 2511.05967 | breast MRI triage不同contrast协议模型适配，领域研究暂缓。 |
| 2511.05968 | radiology reporting/missing-modal VLVAE，科学/临床应用路线暂缓，不借通用representation章节回收。 |
| 2511.06036 | Parkinson management human-AI-robot/digital twins review/outlook，医疗领域研究暂缓。 |
| 2511.06051 Hate-speech classifier | 原标题关闭改判为潜在：Ohm新增完整exact-v1 AB给134M模型macro-F1 .85、约14B SafePhi质量94%、1.87M训练参数/T4约2小时，恢复局部小模型质量–资源比较；不以BERT/classifier应用标签关闭。依据[独立原题摘记录](ORDINARY_INDEPENDENT_REVIEW.md)，不冒称作者原134已读此AB/本地已有该响应；日期held，匹配人口/预算留必要Evidence，不授100x实际E2E省钱、持续学习实现或安全保证，不评分/owner。 |
| 2511.06195 | musical Xanadu沉浸演出AI intermediary，人文艺术应用。 |
| 2511.06201 | urban design推荐/共现embedding/VLM应用，不是当前形成/系统机制主题。 |
| 2511.06316 | accident地理位置推断应用，非模型驱动行动或模型系统执行机制。 |
| 2511.06418 | drug mechanisms knowledge/reasoning dataset，科学应用评价暂缓。 |
| 2511.07262 | emergent ScientificML discovery multi-agent，AI for Science暂缓。 |
| 2601.05266 | industrial part-spec extraction RAG ensemble任务应用；Jan2026 ID不推公开，未读AB/不建无影响日期请求。 |

上述标题层未见原响应纠错/撤回标记，未遍历全历史证明没有标记；将来具体相关纠错信号只重开该项。关闭贡献/范围不为日期含糊另开空路径。剩余潜在项只按身份保留可接受原公开材料，既有反侧不会因未正面采用被删除。
