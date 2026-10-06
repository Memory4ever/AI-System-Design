# 12/18 相关题摘的具体处置

2026-10-02补正：本文件RUNE/VibeSpace/SeBERTis/C-ingClearly/RepGen/NNCaption原负侧判断撤销，7个系统遗漏补入potential；以[逐项作者差额同步](./AUTHOR_REVIEW_RECONCILIATION.md)为当前具体处置，原理由保留供检查误判。不把日期未知当贡献关闭。非作者已明确读取的题摘/必要正文层按合同复用，非我新增全篇阅读。

实际读取2026-10-02，窗口[12/17 09:00,12/18 09:00)+08。作者记录，不是独立验收。所有arXiv身份链接为`https://arxiv.org/abs/<ID>v1`，以下完整精确v1题摘已读；submitted缓冲不是公开事件池，potential不评分、不计本窗确定候选、不写Books。日期缺口不替代贡献判断。首次一批见ADMISSION_CALIBRATION.md。

## 继续保留的具体潜力

| v1身份 | 约束 → 原文增量 → 需要核验的选择 |
| --- | --- |
| 2512.14448 Reasoning Style Poisoning | 文档无显式攻击触发不等于推理安全→GSI用改写诱发analysis paralysis/cognitive haste、RSV监测推理风格→需核语义保持与可靠检测条件，保留安全反证 |
| 2512.14481 SASQ | QAT通常更新权重→固定预训练权重仅学习量化因子并截断outlier→量化质量/训练预算选择，不外推静态推理通用收益 |
| 2512.14527 GreedyLR | 固定schedule适应损失轨迹不足→按当前loss自适应LR及条件收敛分析→优化边界，待核噪声/证明假设 |
| 2512.14600 PerProb | membership真标签难得→受害/对抗生成文本perplexity与logprob代理记忆→保留隐私评价机制，代理不自动是membership真值 |
| 2512.14661 Focus | 视频token冗余与硬件流水不匹配→语义/时空block和运动冗余递进筛选、systolic GEMM tiling→精度/流水联合成本 |
| 2512.14666 EVOLVE-VLA | 执行反馈噪声与固定horizon→学习progress、累计估计并逐渐调节horizon→VLA闭环控制边界 |
| 2512.14681 Jacobi Forcing | 并行draft不易保持causal KV→自并行轨迹蒸馏与multi-block rejection recycling→并行/缓存取舍，不先授精确AR分布保证 |
| 2512.14879 ERBP | 递归合成训练支持集萎缩→stochastic Bregman empirical support与entropy reservoir、条件误差界→保留学习理论，不写普遍熵定律 |
| 2512.14880 Task Matrices | finetuned表示迁移成本→base到task embedding的线性变换跨任务实验→表示复用条件，相关拟合不证明普遍线性 |
| 2512.14895 On-Policy Expert Corrections | 专家离线轨迹与学生访问状态偏移→学生prefix后专家续写纠正→训练数据/Agent covariate shift选择 |
| 2512.14946 EVICPRESS | 分开eviction/compression不能最优化整体→多存储层联合质量/延迟utility、周期profiling与placement heuristic→按context敏感性保守压缩；完整题摘已补读，不采用2.19x无配置数字 |
| 2512.15000 DreamPRM-Code | 代码中间step标签噪声→function-as-step PRM及最终unit-test标签的bi-level修正→过程/最终验证证据分工 |
| 2512.14217 DRAW2ACT | 视频外观不直接授控制→depth/semantic shape/motion trajectory表示、RGB-depth cross-attention与joint-angle policy→VLA表示/动作衔接 |
| 2512.14284 SS4D | 3D空间基础不能独立描述时间→保留预训练空间表征、专用时间层与factorized4D卷积/时间下采样→时空生成latent取舍 |
| 2512.14699 MemFlow | 固定历史压缩不顾文本query→按query检索帧并为chunk构建memory tokens→条件记忆与流式成本，不忽略速度代价 |
| 2512.14938 TalkVerse | 单说话人/长窗耦合困难→高下采样VAE、滑窗motion-frame director与噪声注入dubbing→上下文一致性/latent编辑机制，不仅数据规模 |
| 2512.14614 WorldPlay | 实时world长历史压力→dual action/context重构、时间重框与context-forcing teacher/student memory alignment→交互/记忆一致性，不把提交当公开 |
| 2512.14691 MMGR | 感知总分遮蔽关系推理→physical/logical/spatial/temporal切片揭示ARC/navigation不足→多模态评价盲区，未证明训练objective是因果原因 |
| 2512.14141 TorchTraceAP | profiler trace复杂→分层定位后LLM分类、跨硬件trace分析→性能诊断错误定位边界，不是仅增加数据 |
| 2512.14257 EVPG | 离散视觉程序难反传→依赖图上可微精确概率推断、最终任务标签训练模块→组合梯度的条件，不把概率推断当感知真值 |
| 2512.14320 SIFM | 图像distance指标不等于编辑失败→中间feature divergence/norm与MLLM ISR→编辑防护评价/安全边界 |
| 2512.14766 GR-Agent | KG不完整导致静态推理失效→graph tool action与潜在证据memory闭环→不完整知识下训练免除的执行选择 |
| 2512.20649 AIAuditTrack | 分散Agent事件不易追溯→DID/VC身份、时间交互图与risk diffusion→可追溯/风险传播潜力；链上TPS不证明责任语义正确 |
| 2512.14252 Godel's Poetry | 复杂证明整段生成不易验证→Lean AST解析支持递归分解与子命题证明→形式工具可验证分解机制；数学推理属模型/Agent，不作为科学应用重引入 |
| 2512.14336 Vector Prism | SVG底层形状碎片不对应运动对象→多弱part预测统计聚合为semantic groups→VLM表示与生成稳定性选择 |
| 2512.14792 IaC | syntax/cloud validation不等于意图满足→dependency graph知识注入提高技术正确而意图plateau→Correctness-Congruence Gap反证，保留Agent评价而非只Terraform应用 |
| 2512.14474 Model-First Reasoning | 隐式state易违反约束→先构造entities/state/actions/constraints再plan并有消融→显式建模贡献潜力，不由术语改写准入 |
| 2512.14565 Pairwise Comparison | 主观annotation成本/噪声→severity、distance noise、annotator bias模拟与cost-aware matchmaking/真实数据对照→标注比较设计条件 |
| 2512.19720 Per-Axis Deltas | 多变体冷启动/存储→1bit符号+row/column FP16 scale、小校准集和module packed loader→权重delta加载与质量取舍 |
| 2512.14806 ADRS | verifier反馈可能只优化给定负载→十系统案例跨OpenEvolve/GEPA/ShinkaEvolve扩展及prompt/feedback/robust eval分析→AI系统优化评价边界，原文承认prior work extension，不能当新范式首发 |
| 2512.14244 EDU Compression | token删减破坏连贯/latent压缩API不兼容→source-index anchored EDU tree后query subtree选择→显式结构/来源约束，不把anchoring称完全无幻觉 |
| 2512.14531 VersatileFFN | 参数memory预算固定→共享FFN的width subexperts与depth递归、difficulty gate→容量来自compute而非新增权重，需核实际成本/归因 |
| 2512.14332 Step-Tagging | reflection过量→sentence step分类在线计数早停→解释性停止准则/准确率成本条件 |
| 2512.14856 T5Gemma2 | encoder-decoder复制参数/attention成本→UL2适配多模态、tied embedding与合并self/cross attention→architecture效率及长上下文选择，不因小模型排除 |
| 2512.14652 Segmental Attention | segmented音频学隐式绝对位置、长段cross-attention排列失效→显式位置/扩展context/拼接/semantic segmentation→声学位置泛化边界 |
| 2512.14754 Instruction Reliability | IFEval接近满分不授同意图稳健→cousin prompts与reliable@k揭示大幅下降→评价协议切片/发布条件反证 |

## 已读核心后的负侧与普通待判

- 2512.14138 LAPPI：完整摘要是LLM对话把旅行/饮食偏好实例化给现有solver、用户研究更好；没有新增约束编译/执行验证机制或修正基本设计的证据，关闭贡献，不用日期失败关闭。
- 2512.14620 JMMMU-Pro：现有MMMU-Pro image-only迁移到日语、生成候选后人工审核/重生成；题摘只说明低成本新benchmark和整体较差，未定位新盲区或协议反证，关闭贡献。
- 2512.14706 NN-Caption：已知Net API下LLM组合encoder/decoder、prompt规则与代码修补，更多snippet略降低成功；未定义新的约束执行/搜索机制或可复用失效条件，关闭本项目贡献。
- 2512.14720 SoMe：题摘定义8任务及新社交数据、只说整体不足；无具体评价混杂/执行失效机制，关闭贡献，不将9M数据量计增量。
- 2512.14427 Docpacking：决定准入的原始HTML §3/4.3已补读。Table3同文档数batch仍有packing差异，关闭cross-document attention后收益消失；Table4固定pack比repack差，重排doc order部分恢复。原文按收敛训练且更付compute，不说packing普遍更省算力；保留数据组织/训练机制潜力，准入普通补读已处理。
- 2512.14442 A4Agent：原始HTML §4.3–4.5已补读，Dreamer用原图/指令生成接触/交互图，Thinker把原图与imagined contact cues结合，输出object part再回原图用Rex-Omni/SAM定位；具体增量不只是三个角色名称，保留生成先验辅助affordance的潜力，但imagined interaction不是环境事实/执行安全证明。

## 有界补检身份

最后定点完整题摘：2601.08837 Adversarial Tales用文化叙事/结构分解绕过拒绝，跨26模型有反证，保留surface-form防护边界潜力；不扩写攻击prompt，不把平均ASR当所有输入保证。其余关闭：2512.14562 PolyPersona既有LoRA/4bit加persona survey数据，仅任务指标；2512.14585 Nepali GPT2/BPE/FlashAttention既有recipe无新条件；2512.14673 sustainability vision仅token/context/latency成熟压力无新机制或实证；2512.15804 XBIDetective截图+VLM/finetune浏览器bug检测，未新增可靠性机制/基础边界；2512.15031 GitHub toxicity LtM summaries+预测是已知prompt在moderation任务应用；2512.15042 DASH handshake/example-selection用于VHF分段，未给通用attention/执行/模型贡献；2601.02377机器人安全survey整理既有taxonomy/defenses，未给新反证；2512.14561 essay-rating synthesis观察跨研究协议差异，但只汇总agreement范围，无具体新混杂裁决；2512.14926 Romanian翻译数据+LoRA，只有任务/语言改善，不构成新模型机制。上述均不是按日期关闭。

标题明确范围负侧无需全文：2512.14102遥感领域检索、14112 supply-chain ordering、14130 mobile malware、14179 Bengali翻译应用、14228 geography、14239 Nahuatl corpora、14278 health-advice心理量表、14288 Parkinson、14306 inflation attitudes、14312 wastewater、14321 oncology、14373 sustainable-city advice、14417 port dispatch、14429 seismology、14490 push-notifications、14499 retina、14500 binary-code explanation、14796 pathology、14594 cancer、14604 sparse-text PCA、14876 sign-language recognition、14884 creative visual-concept界面、14887政治观点、14922 prostate、14989 chemistry olympiad、14993 elastic-band科学模拟、15003 security-issue classifier、14358 database-cardinality、14687 emotional dialogue dataset、14121 sports、23719 geometry/mesh科学综述、14106 hydro、14640 lymphoma、14554法律领域benchmark、14896 pharmacy、14277现成SPARQL生成。标题/具体任务足以识别当前范围外或仅领域应用/数据，未借通用Data/Eval重新纳入AI-for-Science；这不是相关理论/小模型的一概排除。compute30中14153Langevin物理kernel、14914数值FFT gridding、其余明确sensor/临床/PV/水文应用同理；原始身份保留在查询文件。

## 后续完整v1题摘

以下仍为潜在贡献、待first-public恢复，不授本窗日期：

- 2512.14865 Audio MultiChallenge：synthetic/single-turn评价盲区→自然多轮voice editing/backtracking/audio cues与长context coherence退化→保留音频评价反证。
- 2512.14982 Prompt Repetition：非reasoning生成重复prompt局部提高表现而输出tokens不增→保留输入重访/计算分配的实验证据潜力；摘要极短但增量明确，未采用“latency不增”无配置结论。
- 2512.15047 HERO：静态不可穿越障碍假设→可操作障碍作为path的层级scene graph→embodied action-conditioned traversability。
- 2512.15068 Semantic Illusion：synthetic calibration成功不能授真实hallucination检测→embedding方法跨真实集FPR大增而judge不同→保留RAG检测反证；conformal coverage依校准分布，题摘的“proved reasoning solves”不是采用定理。
- 2512.14237 Ladder：PEFT少训练参数仍有backward激活memory→side net切断full-backbone backward、depth cross-connections→低memory/compute scaling选择，不因复访旧LST排除。
- 2512.14549 Dual-objective：AR训练效率/重复数据overfit与masked-diffusion成本→50模型变化数据重复度比较objective混合比→保留训练有效性条件。
- 2512.14954 Cross-tokenizer：不同BPE probability space难比likelihood→递归BPE subset exact与general lossless/approximation→蒸馏tokenizer对齐机制，待核假设。
- 2512.15052 SGM：跨模态毒性activation→expertise-weighted neuron soft suppression无参数更新→白盒干预/效用安全取舍，保留安全潜力而非保证。
- 2512.14391 RePo：固定位置索引→可微token位置分配与OLMo2持续预训练→非线性context位置及噪声/长窗条件；认知比喻不计增量。
- 2512.14698 TimeLens：既有grounding benchmark标注不可靠→严格重标后model重新排序、时间表示/RLVR细节→评价盲区与训练选择，原文声明incremental不等于无贡献。
- 2512.14925 MAHA：单尺度attention→learnable层级下采样与convex/Nash融合、可微优化层→attention计算/全局依赖取舍；81% FLOPs不是端到端保证。
- 2512.14645 TiME：多语言大teacher/相对位置→蒸馏到单语言小encoder/绝对位置、质量延迟能源比较→表示/蒸馏适用条件，不以小模型关门。
- 2512.14801 Incentives or Ontology：以Licensing Oracle实验挑战仅激励修复幻觉→保留具体设计反证潜力，摘要的架构必然/唯一消除不获证明；不能照录pseudo-ontology推成定理。
- 2512.15033 Chess Stability：scalar准确率不授不变变换稳健→rotation/mirror/color/format比较反差→保留几何评价边界，需核棋规保持条件，不能把准确率下降当memorizaton因果证明。
- 2512.15641 ComMark：黑盒水印隐蔽/robustness冲突→频域压缩sample+模拟攻击与similarity loss→模型归属验证取舍，非只版权宣传。
- 2512.14770 DAVR：自置信不可靠→latent/QA dual selectors与跨模型事实check双路径→保留选择性VQA可靠性机制，不以榜首计贡献。
- 2512.14166 IntentMiner：MCP第三方tool log位于信任边界外→分层信息隔离/三维call分析重建私有intent→保留协议metadata隐私反证，不提供攻击操作扩展。
- 2512.14177 SGPU：semantic clustering易受措辞扰动→embedding Gram eigenspectrum+GP classifier→语义uncertainty校准设计，不把一致性自动当正确性。
- 2512.14395 MeG：大量编辑locality冲突→query条件diffusion动态生成附加neuron权重→知识编辑/参数状态替代机制。
- 2512.14420 DISCODE：caption evaluator domain shift→Gaussian prior ATT loss解析test-time score解→跨domain评价适用条件。
- 2512.14654 ViRC：单静态图CoT不更新视觉证据→CRU跨块visual tool/reason chunk、阶段SFT/RL→多模态推理证据更新，而Miller比喻不计贡献。
- 2512.14944 PC-GRPO：flat reward/group-relative advantage退化→自监督puzzle环境、medium difficulty curriculum与RAC早升晚退→保留credit/curriculum及推理答案反证；新旧题名身份仍同ID，不按当前名多计。
- 2512.14805 Sharing State：prompt/程序对象桥接人工成本→natural function interface可直接写Python program state与control flow→Agent共享状态/执行边界，同时0.4–4.3x runtime代价不能忽略。
- 2512.14870 HERBench：单cue捷径→MRFS多不重叠证据、区分selector漏检与充分frame仍融合失败→多模态评价盲区。
- 2512.15011 Epistemic Diversity：自训练collapse不能仅增模型数→按训练数据分割的生态十轮实验出现最佳diversity、过多模型能力不足→模型数据反馈条件，不采用政策普适因果。
- 2512.14860 Agentic Penetration：chat拒绝不授执行安全→跨5模型/2框架130case并发现hallucinated compliance→保留拒绝/伪执行/真实执行分离的安全评价增量。
- 2601.19910 KV Offloading：仅扩CPU memory掩盖PCIe→cached-to-prefill critical ratio分析与transfer主导实测→保留通信/调度边界，后编号不等于v1date，不能用ID代日期。
- 2602.22225 SmartChunk：静态chunk granularity→query abstraction planner+压缩embedding+STITCH RL→检索质量/成本机制。
- 2601.03263 Thermodynamic Sycophancy：CoT内部与RCA外部控制跨模型比较→保留受限反例；摘要从N500推出“strictly necessary guarantee”不足，不采用热力学普遍定律。
- 2512.15076 BODE-GEN：离散prompt搜索→LLM bridge continuous embedding、random projection与dimension-scaled GP priors→搜索预算/代码验证机制。
- 2512.15793 ClarityEthic：显式冲突norms生成+contrastive学习→保留道德表示可解释性/训练机制，不把人类plausibility当norm truth。
- 2512.14917 RE2-Bench：primitive/simple code评测盲区→静/动态分析序列化complex types、九complexity metrics及easy/hard骤降→真实代码评价边界。
- 2512.14253 FLAME：LegT/LegS memory与normalizing-flow head→长程表示/分布预测效率机制，不作为单领域科学应用收录。
- 2512.15002 DenseAM Analog：energy landscape数值solver成本→RC/crossbar/amplifier并行动态、XOR/code/simple binary LM分析→计算实现潜力；constant-time必须绑定hardware/precision/规模假设。
- 2512.14234 ViBES：语音/动作分离→modality-hard-routing experts、cross-expert attention及mid-dialogue hooks→联合生成/执行时序机制。

已读完整题摘后关闭：

- 2512.15053 Meta-Prompting Protocol：Generator/Auditor/Optimizer与既有DSPy/TextGrad概念重组，未定义新可验证控制或证明条件；把自然指令称可微/critique称gradient不能授deterministic guarantees。关闭贡献，保留其过度保证信号供非作者抽检。
- 2512.14738 NoveltyRank：Qwen/SciBERT对论文新颖性作binary/pairwise classifier，题摘无新model/evaluator blindspot或可靠性边界，关闭本项目贡献。
- 2512.14083 AVSR dissertation：三层组织既有研究、题摘未给具名机制/新边界，不用宽纲要作新贡献；关闭当前事件贡献，不否定其内部论文价值。
- 2512.14506：语言学观点文章，鼓励audio模型而无新机制/证据，关闭。
- 2512.14846 MALCDF：四角色、加密ontology消息及50-record安全应用对照，没有新的协同/授权/验证机制或基本边界证据，关闭贡献，不照录90%保证。
- 2601.03262：VRD三角色survey与已知granularity/fidelity/cost分类，无新修正证据，关闭贡献。
- 2512.14622 DAR：BigQuery native已有功能下三层agent查询/验证/报告组合、单企业数据与人工时间比较，没有新执行机制或归因边界，关闭贡献，不把治理宣传当权限保证。
- 2512.14990 RepGen：题摘为context/plan/generate-validate-refine常规组合及bug复现率；无新增复现环境/状态验证机制或具体可靠性反证，关闭贡献。
- 2512.15798 DP-Bench：已有ELT/text-to-SQL基础形成任务benchmark与baseline，未揭示新盲区/混杂或执行机制，关闭贡献。
- 2512.14657：既有token/multistream/flow/vocoder迁移到singing、135h训练可比性能，未增加一般模型机制/适用性修正证据，关闭贡献。
- 2602.22223 SQaLe：真实schema扩展的合成SQL数据/执行有效性，摘要未给新生成/校验机制或修正数据/模型判断的证据，关闭贡献。
- 2512.14503 RecGPT-V2：已补原始HTML §3.2/4.1/4.2，main alignment reward乘diversity threshold indicator的CRS硬门控，而非泛泛multi-reward加权；S/A/B agent标签用listwise contrastive scalar RM蒸馏。保留reward冲突/评价到训练机制潜力，不因推荐应用关闭。Table4部分GPT5-mini F1及Qwen3-Base accuracy退步，非全配置更强；门控不证明“eliminates gradient interference”普遍保证，judge flywheel也不授自动保证alignment。


官方`https://arxiv.org/list/cs.CL/2025-12?skip=0&show=2000`可得1302月条目；只浏览2512.14080–2512.15080身份/标题段，不是全月扫描或真实每日公告。由此触发上述Step-Tagging/T5Gemma2等具体题摘；当前继续相关余项，未把宽库存转逐项队列。ARXIV_COMPUTE_CONTEXT.md 30行额外查询已加large-language/foundation/deep-learning/ML语义，纯物理/数值HPC领域仅线索关闭。
