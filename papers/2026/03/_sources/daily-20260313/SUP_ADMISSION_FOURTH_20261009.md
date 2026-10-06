# 有限余题名的9份完整精确v1题摘（普通准入待校准）

只Mar12 BJT补查；从既有182去重主题线索余62标题定点取9个实际含糊/可能相关题名，不把明确科学/传统数学、后公告月线索逐一变全文工作。SUP_ABS_FOURTH_MANIFEST/RESULT中9原件GET200，2026-10-09T13:00:23–26UTC；作者实际完整读SUP_ABS4_<ID>.raw v1题名/abstract/Comments可见当前说明，不用currentv2或其他日报。下列3P/3AMB/3EX不是确认日期/候选/评分。

| ID/标题 | 约束→完整题摘新增→判断 |
| --- | --- |
| 10128 HG-Lane | adverse-weather缺lane训练data→现成scene augmentation/无需reannotation benchmark提高CLRNet指标→题摘只有domain数据扩充与generation框架，没有具体新condition/语义保真验证或基础生成机制，具体EX，不因CVPR声望或30k收；不追不影响处置日期 |
| 10349 EmoStory | 视觉story一致但情绪grounding缺→emotion/writer planning与region-aware generation→决定准入事实AMB，只核region机制/主体一致与情绪条件是否有新控制资格而非prompt/module换目标；25subjects/600stories与userstudy本身不准入 |
| 10512 Amazons Graph Teacher | noisyGPT监督在resource限制下→GAAE作structural denoisefilter、MCTS/SGGA→决定事实AMB，核filter/弱teacher到strong的受限新可靠性或budget条件，而非成熟模块游戏成绩；不以Game domain自动EX，不授N50胜率泛化 |
| 10524 Multi-Turn RAG SemEval | 同retriever/多query与多retriever代价不同→五reformulations/variance-aware nestedRRF、evidence/dualanswer/multi-judge与answerability负侧→窄潜力，采用query-diversity相对heterogeneous ensemble与answerability bottleneck条件，非榜单1/2名；必要预算/校准/groundtruth待Source |
| 10538 DSFlash | embodied reasoning中完整scene relation与runtime取舍→全panoptic relation不是只salient、低延迟/训练budget对照→表示资格/资源可行性潜力；56fps/老1080硬件自身不计贡献，要必要matchedquality/关系覆盖与端到端输入条件，CVPR2026先稿信号待核 |
| 10640 Bielik Field Report | 地域LLM reasoning比较有限→声称evalmethodology与limitations，但摘要未给实际新增评价条件或具体反证→决定事实AMB，只取evaluation methodology/限制决定段，不能仅fieldreport/语言标签收或排 |
| 10814 HanMoVLM | 艺术domain VLM不匹配专家→数据/专家CoT、domain reward与best-of-N验证器→成熟domain adaptation/CoT/RL/judge组合和专家一致数字，题摘无新verifier资格、评价失效或资源成立边界，具体EX；不是因艺术否认主线，11024实际causal解释反证另按自身证据保留 |
| 10965 SSL-V3 | clinical interviewblur影响classifier→No-referencequality分数调VideoViTfeature并用classification反馈VQA→领域healthcare classifier联合目标，未建立foundation/当前模型系统主线新条件或明确可迁移证据，范围EX；不经MultiModal节点借口重新引入Science |
| 11095 Temporal Audio-Visual Alignment | utterance/fixedframeindex融合漏samplingrate异构→TaRoPE把audio/video真实time对齐并CTM约束近时pair→同步身份/表示监督接口潜力，不靠emotionaccuracy准入；小实验不排，必要时间尺度/损失/错位反侧与成本待Source；ICASSP2026先稿门必要 |

13个April arXiv ID线索先按原公告事件月处理，不拿它们早Submitted授Mar12。官方identifier说明SUP_ARXIV_ID_HELP.raw/txt已实际取得，明确newly announced identifiers与YY/月/sequence语义；这是arXiv事件窗口边界，不是已证明家族从未更早公开，不授全站第一公开排他结论。明确领域/传统数学题名余部分只作范围线索，不扩大源或读全文；具体有限停止补充仍待整理，普通待办非0。

## 三项决定事实实际窄读（待非作者校准）

原件SUP_DECIDE_10349/10512/10640.raw与SUP_FINAL_DECIDE_SOURCE_MANIFEST_RESULT，三GET200在13:04:58UTC。

- 10349 §III.B完整region method：文本subject prompt对story图crossattention阈值化出subject与complement element mask；只在subject区域mix reference value并注入prompt语义，在非subject区域提升emotion-element attention，针对主体/情绪元素相近时主体主导、cross-image localization drift。具体控制两区域的反侧/语义接口足够潜力转正，不借情绪任务或成熟MM-DiT/soft mixing计贡献；mask错位、lambda/alpha与subject/emotion可兼容性要必要Source，不授pixel级真实保证。
- 10512 §3.2.3/3.2.4/3.2.5至application和§5.2决定段：GAT-AE graph聚合root、shifted tanh输出供SGGA概率/selection，LLM棋盘rating作为训练监督；原文直接断言graph拓扑约束使GAT无法记忆teacher randomnoise，从而自动denoise。只准入这一跨结构prior→监督可靠性的受限证据/反证命题，不收game winrate；该“不可能记忆noise”的强推断尚无证明，SGGA只已有selection/mutation/crossover也不借旧方法抬分。建议潜力转正后必要对照/真实标签/预算审阅，不授普遍weak-to-strong。
- 10640 §2–3完整决定benchmarking段：从GPT4o reasoning+answer 1–5变GPT4.1 final-only 0/0.5/1，同时提示有模型wrong answer得partialcredit、Bielik途中tokenlimit失分；单步修改premise后不更新，deterministic/nondeterministic的不同oracle限制明确。这是该新评价过程的版本/裁判/预算混杂与belief-revision探针条件，建议窄潜力转正，而非Polish训练pipeline/fieldreport标签。未采语言ranking、judge升级真更准确或“在轨即应对”，要Source分开task truth与scorer代理并核Tables/样本。

拟第四9贡献门为6P/3EX，日期/必要Source/owner未授；不预先改变正式池。只有这三事实含糊才取决定原文，其余明确潜力直接走证据层，不遍历所有附件。
