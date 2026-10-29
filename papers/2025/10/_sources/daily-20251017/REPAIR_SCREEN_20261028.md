# Oct17 writer 有限发现差额筛选

仅A3/A4五主题实际返回题名导航，非全arXiv类别/号段。created和registered各五页207出现/173唯一，逐组集合相同；与旧157日期集合及两正式去重差额见DELTA。writer只负责>=13250；低侧由reader，不重复。下面43精确v1完整题摘已实际读，原件`REPAIR_ABS_2510.<ID>_20261028.html`及request；当前DataCite摘要不替v1，当前命中题名差额保留（13293/13315/13454等）。

## 首批准入校准提案

| 身份 | 完整题摘所见原约束→实际增量→选择 | 初筛处置 |
| --- | --- | --- |
| 13251 MapFlow | 视频时序信息路径不明→层级/跨帧信息流干预后选择有效attention边→应区分观测saliency与删边质量 | P，必要干预/对照域；不从58%边数授净加速 |
| 13253 MDM | 多模态encoder/decoder分离→Mamba多步selection diffusion+统一VAE，但摘要未说明具体选择接口或可比因果→不能只按架构组合/榜单准入 | N，只补最小机制/匹配对照后判断，不全Methods |
| 13272 VERITAS | answer正确不保证search trace faithful→info-think/think-answer/think-search三个reward读出→应独立评价/优化各界面 | P；核faithfulness代理权限，不授真实内部推理 |
| 13366 DocumentAI survey | 综述多模态/多语/检索与agent趋势，没有题摘提出的具体新机制/反证或比较控制→不改变具体设计判断 | C；完整AB已读，日期不影响关闭，不追全文 |
| 13747 InteractiveOmni | encoder/LLM/decoder组合与阶段训练、规模比较本身不足；多turn评测可能测真实记忆盲点但题摘未披露条件→只补benchmark最低门 | N，不因新模型名/97%headline准入 |
| 13543 browser fuzz | 本地browser/LLM引导测试只称framework，无具体新攻击面/反馈机制/证据→只补核心说明决定是否区别普通prompt-injection测试 | N；必要安全最低门，不先全Methods |

## 其余实际题摘的具体潜力

以下P只准入潜力，必要审阅/分数/owner未完成不冒最终。日期仍逐identity核唯一v1/原字段与信号；无日期入窗不得先正式。

- 13262：state先扰再依该状态扰action的协同威胁与critic依赖；需原权限/防御对照，不授现实漏洞。
- 13276：长多模态context长度/关键内容位置对fidelity的分轴评价，非context大即有效。
- 13281：独立ASR/VSR N-best与时变可靠提示，避免早融合损失/坏模态误导，非单榜单。
- 13285：按representation分布调steering强度，需检验代理与coherence/控制取舍。
- 13293：style-content冲突下按mismatch调AR-CFG，需对照发音/情绪与NLI代理。
- 13308：时/频/空间三轴依赖与FOA drytarget训练消费者、CLAP查询条件，不以应用音频名排机制。
- 13312：跨turn稀疏reward→intent-aware逐turn信号与交错search，需分构造label/真实意图。
- 13315：query依赖视觉扰动+logit分布阈值候选集，需保额外生成费与hallucination代理。
- 13328：直接学最大化概率而非解acquisition，变分posterior近似/探索预算有具体理论边界。
- 13329：passage embedding之上混合document/within结构attention，重新考虑crosspassage信息与encoder开销。
- 13334：均值importance聚合依赖稳定子集→worst-risk两步聚合与layer预算，直接反证旧eviction假设。
- 13344：shared/routed/null experts+topP容量与三阶段均衡，音频task冲突/数据不平衡分责。
- 13363：OWL动态memory与显式reasoning tree、NLI与qualityjudge分验，需核authoritative/验证权限。
- 13367：online model-free Transformer的actor/critic共享与sequence slicing条件，不按非LLM关闭。
- 13375：depth/VLM/action共享attention的辅助几何条件接口，需核不可观测深度与训练预算。
- 13394：intrinsic/extrinsic及static/dynamic分轴、multi-step/multiview盲点；需具体控制而非taxonomy配额。
- 13401：同accelerator运行时切换BFP格式的矩阵消费者与重配置边界，不从CPU比较授通用效率。
- 13406：pairdot保持→orthogonal对齐误差界与跨版本兼容，需假设/误差而非embedding可直接换。
- 13418：masked生成unmask transition的RL概率定义，区别AR/diffusion token目标。
- 13419：global低res与referencepatch全res双适配，分语义/局部细节预算。
- 13444：模型提出monomial basis后SDP认证/fallback边界，学习输出不直接得nonnegativity权；非AI科学领域应用指标题名排除。
- 13451：MoE共享shadow路径的diversity/alignment与攻击可比人口，需必要隐私权限/测量。
- 13454：model stitching匹配层+reward适配video latent到3Ddecoder，表示可对齐不等几何真。
- 13462：触发embedding与router敏感expert联合污染的威胁接口；需原攻击者权限，不授100%普遍ASR。
- 13512：preference-label LDP下KL目标的offline/online假设与样本/隐私取舍，不授训练数据全DP。
- 13551：强弱模型交错rollout、handoff成功作为intelligibility代理，不等人类审计真值。
- 13554：未来attention代理的credit重权/可部署时序，需核关联与干预，不能称attention即机制蓝图。
- 13558：冻结audio encoder/LLM，在中间层路由steering向量；连续表示接口不授全部旧能力保持。
- 13580：LAPE选择单语subnetwork再微调，需已知语言/参数mask与random控制/跨语反侧。
- 13598：新表自动metric变差但human/judge不随变的负面证据，重新考虑freshness与污染归因。
- 13614：时间operator检索与单调/多实体边界、trace experience复用；“verified”不授事实真值。
- 13622：NLDR重建可用而latentdiffusion差的负面结果，区分可视化邻域与生成插值支持。
- 13632：文本遗忘/跨modal对齐两压力→蒸馏+主动合成数据选择，需额外teacher/数据费及cascade反侧。
- 13680：diagonal preconditioner的basis与mini-batch噪声交互，不能把Adam当普遍GN近似。
- 13713：连续mask FW再round对组合剪枝的近似边界，需校准/恢复与实际kernel支持。
- 13744：frontier开放证明step支持/首错检测，区分数学答案正确与证明每步有支持，需500h标注/验证者预算控制。
- 13787：CLIP选旧frame/不相容则仅early diffusion注视觉，防误条件扩散与recaption混杂。

## 题名范围停止

writer片中明确应用/非本主线题名仅导航：13316 GPT4o趣味匹配、13320 ultra-low-power distributed learning（无LM系统接口线索）、13343一般multiagent动作排序应用、13358机器人鲁棒控制应用、13359电商推荐、13364姿态零样本分类、13371推荐agent模块、13390 WiFi识别、13432协作感知、13439 GPS停车点、13441 PET重建、13488四足地形、13493情绪识别、13513铁磁液晶、13582网表数据生成、13592SEEG分析、13604黑洞、13645红外探测器、13660凝视估计、13688非线性编码神经数据、13729光场相机注册、13760医学edge特定ViT、13763科学inference、13768 fMRI flatmaps、13774城市空间、13794motion imitation框架、13805三点相关科学推断。13255脑/LM共同syntax probe题名仍可能直接相关，不按脑标签关闭，尚需AB补；上述标题筛选由reader分层校准，可能有模型级歧义者定点重开，不冒全部AB。

当前43AB=39P+3N+1C（具体清单计数需独核），普通必要/最低门继续；原已有36恢复项与新发现不混计，未向Books预签。

## 题名歧义八项的定点恢复

为避免把领域名当排除，writer实际补读13255/13320/13343/13358/13371/13660/13760/13794八精确v1完整题摘，原件同前。此前title关闭仅导航，以下实际证据覆盖其初判：

- 13255 HFTP：频域probe定位LM语法层次、brain similarity与模型性能改进方向相反，新增测量盲点；P，不能因脑数据排。
- 13343 AOAD-MAT：动作序列顺序本身作为PPO子目标/下一agent选择，非只调超参；P，需权限与实际ordering收益/费用。
- 13358 Offline-online adversarial：EMA表现驱动执行action扰动概率，offline效率/online鲁棒和nominal退步分验；P，非仅robotics应用增分。
- 13320 RockNet：摘要仍仅“specialized efficient classifier+multihop”与scale数字，具体通信/训练新接口含糊；N，最小architecture/消融决定，不直接title关闭或全Methods。
- 13760 BitMedViT：ternary linear/MQA/distill多为成熟组合，但宣customCUDA消费/traffic可能有实际表示—kernel边界；N，只补该机制/对照，不因医疗自动排或直接采临床accuracy。
- 13371 MADREC：标准profile summary/rerank与缺GTitem再feedback，未给新执行机制、可靠性条件或可迁移反证，现有题摘仅推荐指标/解释说服度；具体C，不能把persuasion授解释真实，不为日期追全文。
- 13660 OmniGaze：标准pseudo-label与现有encoder/MLLM评分筛选加权，本文题摘新增仅面部数据/凝视指标，未有可辨通用训练机制或评分边界；具体C，非因眼动标签，而是贡献门未达。
- 13794 MimicKit：通用既有motion-imitation/RL实现与模块可配置软件说明，无新算法/执行语义/可靠性变化；具体C，不因开源软件体裁排。

writer原71新title导航现在51完整AB/20明确title范围；13253最低域已实际N→P且中心争议提案（必要证据另表），合43P/4最低N/4具体C；P含该争议，不提前授Evidence或Books，3新P与两最低普通继续。只重开具体误排集合，不将全部返回构成全文配额。

## 后到实际最低门收束（覆盖上文阶段计数）

writer71新title导航最终51完整AB/20明确title范围；51AB内46P/5具体C/0最低N。13320冻结特征输入分片已完整PDF必要并R31确认P5，13760表示到INT8 consumer已R28确认P6，13747多turn测量反侧已R21确认P5，13543最小决定域R21确认C，13253潜力/实际中心争议保持P6而隔离正面采用；其余既成必要域见EVIDENCE/R22–35。五C为13366、13371、13543、13660、13794，不因普通owner或Books未落缩池。

13272 VERITAS具名纠正：训练reward为EM+InfoThink+ThinkAnswer；ThinkSearch属于三类evaluation定义之一，不是此处训练reward。此后采用R24/EVIDENCE后到纠正，不继承上文初判中的ThinkSearch混用。
