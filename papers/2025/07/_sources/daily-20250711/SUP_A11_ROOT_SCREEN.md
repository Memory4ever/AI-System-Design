# July11新增arXiv题摘判断

作者root，2026-10-11。新补窗July10完整自然日；下面是发现与贡献判断，未确认公开日的潜力不是正式候选，不评分、不用于Books。原65潜力/158关闭及原小时窗口不重算、不迁日。精确题摘原件在`SUP_A11_EXACT_ROOT.json`与每个`SUP_A11_abs-*v1.html`；初始API latest只作题名线索。

## 入口

五组分类加ti/abs主题（模型、训练/推理系统、Agent/RAG、多模态、kernel/compiler）first-submitted UTC July8 18:00～July9 18:00，实际各107/4/37/60/3项、start0/max200，total均小于200，返回页读完后停止；跨组154身份，仅主题发现，不代表July10公开数。初始Jul8/9宽日期model226只返回200，此响应保留但不授页完整覆盖；校准后只使用收窄页。具体请求/时间/全返回在`SUP_A11_NARROW.json`与`SUP_A11_narrow_*.xml`。

原日级公告恢复失败不能无限扩追。新增Jul10 announcement advanced probe实际返回表单，明确year/month granularity；submission、月ID、updated和默认公告排期均不证明单篇首公开日。不使用catchup。新材料只需官方公开日，不追时分秒；旧小时请求仅历史保留。

## root首批完整精确v1题摘（58项；普通歧义项尚待必要core）

P=具体贡献潜力，必要首公开日待核；C=本项目贡献关闭；N=决定准入的必要事实尚含糊，属于普通可执行工作，不是外部受阻。尚未独立校准，不授候选Evidence/Books完成。

| arXiv v1 | 初判 | 具体增量或关闭理由 |
| --- | --- | --- |
| 2507.06306 | P | 五语言epistemic markers与人依赖差异，质疑跨语言沿用英文confidence校准 |
| 2507.06310 | P | Bass到LLM转换的五个具体抽象/角色/时间粒度冲突，限制逼真对话等同可解释模拟 |
| 2507.06313 | P | 测试时overlap chunks写权重与FFN第二矩阵选择，替代长序列显式状态 |
| 2507.06323 | P | Function Calling/MCP系统与模型漏洞组成、链式攻击/推理能力反侧，不能照录成功率 |
| 2507.06329 | C | 音乐协作对话数据与Qwen-Audio微调的领域效果，题摘未提出新协作机制/评价失效条件 |
| 2507.06335 | N | words-as-classifiers综述加small experiment，需局部核是否实际新条件而非已有语义路线重述 |
| 2507.06376 | P | component RTL能力不覆盖SoC集成/参数组合，具体评价对象与可执行环境缺口 |
| 2507.06378 | P | 70语言形态边界分数不能解释下游表现，tokenizer指标有效性反证 |
| 2507.06396 | N | PDL declarative prompt composition/可优化，与已有DSL组合的实际差额待局部核 |
| 2507.06415 | P | 双层meta-learning用LoRA写上下文，训练内存与推理记忆取舍 |
| 2507.06419 | P | reward模型自引导controlled decoding挖错误高分回答再修补，不只换数据集 |
| 2507.06427 | N | SAE解释误解再改prompt，需核是否新增干预/失效条件而非成熟诊断步骤组合 |
| 2507.06445 | P | attention观测可预测OOD规则，却不是ablation支持的因果实现，相关/因果分开 |
| 2507.06448 | P | perception KL进入GRPO及loss hacking/双熵对策，是多模态RL目标反侧 |
| 2507.06449 | P | 异构client同质性聚合/选择与structured pruning协同的通信质量条件待核 |
| 2507.06450 | C | 已有SCATE组合算子+code generation/执行验证的数据增强用于时间归一，未提出新语义/验证机制 |
| 2507.06457 | P | 72小模型显示单独linear最佳不保证hybrid最佳，LM/recall与full层比例须分开 |
| 2507.06461 | P | binary stochastic forward-forward以索引替代matmul、tied biases补二值瓶颈，硬件估算不是实测 |
| 2507.06466 | P | FM代码策略self-play跳局部最优、quality diversity population与攻防修补 |
| 2507.06483 | C | 日语persona/voice的用户参与与体验研究，题摘未给模型/运行机制或可靠性新边界 |
| 2507.06485 | P | pure-RL省SFT与consistency触发sparse-to-dense视频TTS，对训练/在线预算不同贡献 |
| 2507.06489 | P | 意义保持扰动也改变verbal confidence/answer、常规防御反侧，安全评价潜力 |
| 2507.06506 | C | pun翻译的CoT/phonetic-semantic/生成判别反馈组合及竞赛表现，没有新的组合有效性边界 |
| 2507.06507 | C | GR-LLM preliminaries/应用/工业考量与方向综述，题摘没有新的评价反例/原机制 |
| 2507.06512 | C | 34 hardware bug场景pass@5/RAG效果，题摘仅任务表现，无新失败类别或验证机制 |
| 2507.06516 | P | 保概率排序的可解释受约束posthoc map，表达能力与校准成本权衡 |
| 2507.06517 | P | 浅层codebook合并/深层attention eviction分工及GQA冲突，不能统一所有层淘汰 |
| 2507.06520 | N | MCP/ReAct/async/retry/SSE功能齐全不等新调度语义；需局部核容量/恢复不变量差额 |
| 2507.06523 | P | 开放生成事实依赖图联合V2T/T2V核实，弥补只单任务/单句的faithfulness评价 |
| 2507.06528 | P | 理论简单问题解生成SFT向复杂投资决策迁移与收敛命题，假设和域边界待核 |
| 2507.06529 | P | 多步regret目标distill GP/acquisition轨迹进decision Transformer，非只换BO启发式 |
| 2507.06539 | C | clustering、GPT标注/合成、LoRA及data balancing的合同抽取成熟组合，未提供新机制或条件 |
| 2507.06554 | N | subset评价+自动groundtruth/最少事实，是否新增可验证低成本评价条件需局部方法 |
| 2507.06564 | N | 空间verbalizer/history backtrack+NMPC，需区分VLA执行边界机制与普通导航组合 |
| 2507.06565 | P | drift/self-repair/fabrication/peer-review hazard模型及协同循环，可靠性假设待核 |
| 2507.06567 | P | expert coactivation破坏top1 submodularity，greedy/decomposition/max-convolution不同适用假设 |
| 2507.06573 | P | expert prefix采样和pass-rate EMA learning-progress重权，改变RL每题影响而非扩数据 |
| 2507.06607 | P | GMU跨层SSM readout共享与decoder-hybrid-decoder，计算/状态及scaling边界 |
| 2507.06608 | P | 同GPU PD动态资源分割与饱和收益，替代chunked phase干扰/整GPU分离 |
| 2507.06622 | N | LLM embedding/KG+Bayesian fusion是否新可迁移投影条件，不能仅因6任务获益准入 |
| 2507.06623 | P | 复杂主观抽取及deliberate errors低检测率，反驳自核反馈等同证据验证 |
| 2507.06650 | C | observational treatment effect的MoE/MHA/orthogonal/importance组合，未建立基础模型/运行主线新机制 |
| 2507.06658 | C | LLM actor/subject抽取生成政治polarization指标，非模型能力/系统机制研究 |
| 2507.06674 | P | RVQ单codebook/SiMBA decoder对有限预算收敛的局部机制与对照，不因音乐领域关闭 |
| 2507.06715 | N | clinical两级RAG/chunking及deterministic claim需要定点核心确认，不由医学标签关闭 |
| 2507.06722 | P | wrong-output代理uncertainty的跨层Tuned Lens轨迹对齐，简单检测器可行性反证 |
| 2507.06774 | N | checklist multilingual judge是否新blindspot/机制而非prompt成熟移植 |
| 2507.06795 | N | DACP商业smallmodel维持general能力，需实际条件/混杂证据而非仅宣称domain提高 |
| 2507.06802 | P | semantic/acoustic共同speech units保prosody/emotion，跨任务输入表示取舍 |
| 2507.06803 | N | SysML中介/自动codegen+LLM validation，需局部核新执行/验证条件，不以符号词准入 |
| 2507.06829 | P | semantic diversity动态协同/终止替代任意token budget；v1摘要末尾作者ellipsis，必要原证待核 |
| 2507.06838 | P | multi-hop从单passage ranking改query needs驱动set选择，互补信息优化对象不同 |
| 2507.06850 | P | peer请求可信路径使可拒绝direct恶意命令被执行，Agent trust边界安全反证 |
| 2507.06892 | P | offpolicy混数据/UTD、KL-convex、reincarnation及短答/反思坍塌边界 |
| 2507.06893 | P | 跨模型resampling不确定性与复现维护的具体统计条件，非单repo列表 |
| 2507.06895 | P | CSD/P@R评价结构与复杂度反侧，not更大RE模型自动更好 |
| 2507.06899 | P | 正确textplan仍可被visual grounding后门劫持，clean finetune/跨GUI迁移边界 |
| 2507.06909 | N | 多被告/多charge场景是否具体推理分解blindspot或仅任务复杂度dataset，应局部核 |

## root后批完整精确v1题摘（38项）

下表与首批合计96项实际完整精确题摘。最新页Comment只作当前可见撤回/修订轻核；没有检出的标记不证明全历史无勘误。先前API title与v1 title差异保留，不把新版方法当历史v1贡献。

| arXiv v1 | 初判 | 具体增量或关闭理由 |
| --- | --- | --- |
| 2507.06910 | P | tutor策略影响学生结果但LLM难预测未来策略，局部行为/评价有效性反侧 |
| 2507.06920 | P | homogeneous tests漏bug同时污染RLVR reward，test充分性/检测率与code能力分离 |
| 2507.06956 | P | query微扰到retrieval/generation及端到端的分组件robustness归因 |
| 2507.06959 | P | SFT failure confidence/similarity偏好采样与counterfactual rationale，样本分布目标与成本界限 |
| 2507.06992 | C | pathology/anatomy banks、contrastive/matching/gate用于radiology的成熟概念对齐组合；题摘无新的通用机制/失效条件，不因医疗标签关闭 |
| 2507.06993 | C | 三agent travel/map/RAG/disruption的功能流程组合，未提出新控制/恢复语义或成立条件 |
| 2507.06999 | P | train deliberate而test intuitive、仅format reward的模态对齐迁移，思考深度不必在线复用 |
| 2507.07006 | C | patch clustering+GNN+linear projection+caption SFT用于WSI，未有主线新机制/对照失效边界 |
| 2507.07017 | P | 针对trajectory高不确定点rollout构造中间feedback，非只最终reward |
| 2507.07024 | P | experts独立闭源数据训练、domain-informed routing且不joint training、可退出数据贡献 |
| 2507.07030 | P | dense retrieval/response共模型联合目标及inconsistency/data discrepancy处理 |
| 2507.07044 | P | 近sensor SiPh matmul/电子非线性、ROI preprune及QAT/decomposition硬件约束协同 |
| 2507.07101 | P | Adam超参随batch缩放、SGD稳定条件、gradient accumulation并非固定应当，通信约束例外 |
| 2507.07106 | P | query-conditioned diffusion visual features会leak原prompt，改多模态encoder同时需防泄漏 |
| 2507.07129 | P | 固定Unicode substrate/logit平均的专家组合与逐层生长；所谓MoE名称不证明token sparse routing |
| 2507.07130 | P | 单向local-loss分块训练不回传梯度、aux net生成/聚合activations，通信换优化语义 |
| 2507.07135 | C | 两阶段自动fashion标注、adapter和querycandidate matching领域数据/效果，未显示新评价盲区或机制 |
| 2507.07137 | P | unlearn目标周边损伤与synthetic prompt恢复同时测，语义近邻量化和清除claim不同 |
| 2507.07145 | P | 2bit convolutional bitcode/lookupfree映射与GPU解码，精度容量带宽需共同评估 |
| 2507.07146 | P | entity graph把历史harmful references带入本次判断/相似singleturn有标签node，是多轮威胁表示差额 |
| 2507.07147 | P/身份待核 | descriptionfree LLM到continuous prompt蒸馏与multi-prompt权重；Comment ICLR2025触发先前公开同身份窄核，不默认July新事件 |
| 2507.07151 | P/身份待核 | 图文输入本身冲突与prompt/SFT/RL对策对照；ICML2025触发先前公开核，不因新版arXivID判本窗 |
| 2507.07155 | C | astrophysics autonomous scientific discovery/RAG配置选择，AI for Science当前暂缓 |
| 2507.07157 | C | EEG语义caption中介/contrastive/latent diffusion脑信号重建，AI for Science当前暂缓，无当前主线额外新机制 |
| 2507.08027 | P | base/finetuned政治倾向及自报/行为区别；不能由观察宣称四因素因果归因 |
| 2507.08029 | P | 随机流程干预、blinded末轮及后续就业/年龄credential对照，任务得分与人类结果分开 |
| 2507.08030 | P | 多代模型medical safety disclaimer下降；仅warning有无不证明医疗安全，属于模型安全评价而非医学发现 |
| 2507.08031 | P | small/large在binary与severity类别不同失效、fewshot幅度条件，不能拿能力相近推出privacy保证 |
| 2507.08034 | C | external API/calculator/calendar调用与MMLU效果的成熟组合；Comment extended新增对照不是机制修订信号，不以版本自动深审 |
| 2507.08037 | P | 高层plan训练而非fewshot即可、跨math/code迁移的局部评价边界 |
| 2507.08038 | P | empirical AI实验的ablation规划blindspot、CoT反胜agent，对模型研究自动化不是暂停科学发现范围 |
| 2507.08862 | P | KG triple/inference chain poisoning与text RAG威胁对象不同，结构知识不是天然可信 |
| 2507.08865 | C | spatial ModernBERT三token分类头/B-I-IB金融layout提取，常规多head/空间输入组合未有新通用执行条件 |
| 2507.08870 | N | literature compression/reasoning/confidence条件选择，需core区分可迁移评价条件与普通RAG推荐流程 |
| 2507.11544 | P | safeguard移除前后的危险能力gap随scale变化，不等原始拒绝率能覆盖openweight攻击风险 |
| 2507.13369 | C | PostgreSQL/RTL抓取syntax/synthesis验证数据流水线，题摘仅新的领域库存与规模，无新数据验证语义 |
| 2507.21107 | P | unembedding pullback metric计算residual轨迹curvature/salience，匹配prompt小实验仅局部解释证据 |
| 2507.21108 | C | legal contract任务/数据/方法taxonomy及现有评价综述，未给新的主线机制或反例 |

## root明确范围题名（15项，不计完整题摘）

下面明确是领域应用/科学研究或一般统计/控制问题，没有含糊基础模型机制题名；只按题名范围关闭。当前Atom题名/摘要/原comment的撤回纠错关键词轻核若出现实际信号会局部重开，不能由此宣称全站无标记。

| arXiv身份 | 停止理由 |
| --- | --- |
| 2507.06399 | 小型核反应堆thermal-fluid testbed与digital twin，AI for Science暂缓 |
| 2507.06402 | ECG无线信号tamper的传统hybrid ML检测，非基础模型安全威胁 |
| 2507.06458 | protein模型神经元生物解释与steering，AI for Science暂缓 |
| 2507.06502 | frequency expert时间序列forecasting，题名明确领域预测而非LM MoE机制 |
| 2507.06538 | AMS circuit parasitic capacitance小样本预测，科学/电路应用范围 |
| 2507.06712 | PINN nonlinear observer，非worldmodel或基础模型policy |
| 2507.06752 | operator learning数学人工数据，AI for Science暂缓 |
| 2507.06817 | adaptive sliding-mode control的软件sensor，非基础模型runtime |
| 2507.06853 | 分子谱结构发现，AI for Science暂缓 |
| 2507.06938 | 时空Gaussian Processes加速建模，未有基础模型计算或训练主题 |
| 2507.06994 | 免疫治疗NSCLC生存预测，AI for Science暂缓 |
| 2507.07034 | jet heat transfer surrogate预测，AI for Science暂缓 |
| 2507.07143 | 科学建模malware propagation，非LLM Agent威胁模型 |
| 2507.07148 | biomedical image XAI综述，AI for Science暂缓 |
| 2507.14167 | GNSS jammer signal定位fusion，明确领域信号应用无基础模型机制题名 |

## 精确请求与恢复边界

P逐身份对应表内精确v1 URL `https://arxiv.org/abs/<ID>v1`。缺的是官方首公开日/当期公告或作者带可核公开日期的首次正文，不是submission或updated；可接受同身份同v1的当期原始公开列表/官方首发全文。缺该材料不能将潜力计为July10正式候选，不能评分/据此改Books；只重开对应身份日期门，再按最低投入审必要核心。C不因日期未核另追日期；N和未读题摘继续实际处理，不作为安全终态。

## 2026-10-11 准入歧义的必要核心处置

上表保留最初判断，不作为最新未读队列。Ptolemy完整96题摘独核将06449/06802/06829/07030从P转为必要N，与原13项合计17个N；原因和身份见[独核§7–8](SUP_INDEPENDENT_20261011.md)。随后作者实际局部核心已作明确处置：

- [原13项核心包](SUP_A11_NCORE_SCREEN.md)：06335/06396/06427/06554/06564/06622/06774/06795/08870保留P；06520/06715/06803/06909明确C，9P/4C；不是因日期或领域标签关闭。
- [额外4项核心包](SUP_A11_EXTRA_CORE.md)：06449/06802/06829/07030均明确P，保留各自公式域、校准、对照及privacy反侧，不把局部读取计为候选Evidence完成。

作者17项普通准入决定已读，[非作者实际决定核心校准§9/11](SUP_INDEPENDENT_20261011.md#9-n13决定核心的分层独核)也已完成；root96为73P/23C/0N，15明确题名关闭另计，不含MM43。07147/07151及MM06952的会议同核心已核、首公开日期未证，见[具名身份§12](SUP_INDEPENDENT_20261011.md#12-本人三项具名会议身份同核心已证首公开日未证)，继续P，不从会议名猜窗前。所有日期潜力不评分、不用于Books。

MM的08036题名误排、06441安全组合关闭与CoPT/FreeTTA窗前证明见[同日侧支修正](SUP_A11_MULTIMODAL_SCREEN.md#2026-10-11-局部补正)，并经[非作者原件校准§10](SUP_INDEPENDENT_20261011.md#10-mm43与局部补正的实际独核)，不是新增身份。当前总体154=132完整AB+22题名；处置为97P/55C/2O：root73P/23C+15题名C，MM24P/17C/2O（17C含其7题名）。97全是必要公开日/先稿身份潜力；2O最迟2024-10-31 CoPT及2025-06-12 FreeTTA公开同核心，退出July10首次事件。候选Evidence/日级DAY仍不可由上述计数代替，正式新增只有独立受限标准审阅的GFM Blog1。
