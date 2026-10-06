# Daily Research — 2025-12-17

**规范：** V3
**窗口：** 2025-12-16T09:00:00+08:00 ～ 2025-12-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T19:05:13+08:00

## 1. 结论

现有日期证据支持一个确定当窗家族：Seedance 1.5 pro **官网Blog发布事件**，不是arXiv首公开事件；标准审阅和非作者复核完成，Books决定为仅报告。Anthropic与PE-AV首公开时刻经有限官方恢复仍缺，安全隔离；SAM官方X公告落窗，但没有独立新贡献证据，不把普通公告重新计为论文首发。必要正文已实际阅读，不用日期失败掩盖普通读文待办。有界来源检查及收窄arXiv初筛已记录，普通待办0；外部隔离项不支持覆盖通过或无遗漏断言。

FrontierScience、湿实验科研应用和 GPT-Image-1.5 当前产品发布正文已按各自原文范围关闭；前两项属于暂缓的 AI for Science，后一项未披露足以归因产品改善的新增机制。独立安全材料未因此被关闭。无 Books 写入；现有段落的具体对读不冒称新路线全部已有覆盖，日期隔离中的训练干预增量也未采用。

## 2. 来源覆盖

所有当前首页都只提供发现入口，不用首页或空搜索证明历史窗口已查完。首批记录见 [准入记录](../_sources/daily-20251217/ADMISSION_CALIBRATION.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research首入口、Research news仅当前9项+Load more；定点Dec16 FrontierScience/wet lab/Images完整核心说明，正文链接无独立该版本card；精确日期/主题补检返回已读条目，官方RSS有限替代403 | 受阻 | 历史目录邻接段未恢复，隔离不作零事件；独立安全材料未恢复，不将当前正文排除扩大到其安全证明 |
| SRC-ANTHROPIC | Research首入口与Alignment Blog December相邻段；alignment-faking的Background/Metrics/Training details、三类Mitigation Setup/Results、Limitations/Methodological Lessons已读，root必要源审已记录 | 受阻 | alignment-faking首公开日期已有限恢复后隔离；主Research历史publicationList原始恢复SSL EOF，有限停止与具体重开条件见§5，不据此授全机构覆盖 |
| SRC-GOOGLE-AI | Google Research2025 Blog第1页Dec18→Dec15→Nov12；DeepMind正确 `/blog/page/4/` December/November切片，五研究/政策页和GeminiFlash/audio外链各核官方datePublished：最近Flash Dec17 16Z、audio Dec12 17Z均窗外 | 受阻 | Blog切片已检查；publications首屏只有年份、精确历史首发段未恢复，不以Blog或月归属给全部论文覆盖通过 |
| SRC-META-AI | Research入口与官方搜索相邻Dec16/18段，SAM/PE-AV完整题摘；官网PDF各有限失败后实际读2512.18099v1与2512.19687v1的必要方法/消融 | 受阻 | 两研究页首公开及12/16精确PDF缺失；较晚arXiv正文不自动等于12/16版。SAM X公告仅用于该公告时刻 |
| SRC-QWEN | 旧Blog尾部最新Sep23并明确迁移qwen.ai/research；新目录动态壳与公开前端有限恢复未取得2025目录；Qwen3精确本窗commits空数组 | 受阻 | 历史研究目录不可恢复；空提交不证明全源零事件。只在官方历史目录/事件记录到达时重开 |
| SRC-DEEPSEEK | 原始Change Log顺序越过本窗，邻接2026Apr24/2025Dec1，无分页；DeepSeek-V3本窗commits空；Speciale endpoint Dec15 15:59UTC到期，早于本窗 | 已检查 | 无本窗变更表/指定repo命中；不扩成互联网无遗漏声明 |
| SRC-MOONSHOT | Platform Blog26条无Next；持续更新记录全文最新Nov6 K2 Think→Oct27→Sep5，向下May2024；Kimi-K2本窗commits空 | 已检查 | 指定原始入口未发现本窗研究条目，不据空提交作全源零事件 |
| SRC-TENCENT-HUNYUAN | 官方Research/浏览器有限失败；实际公开API `POST /api/blog/publicList` 全部renderType0共11条仅2026，历史2025目录未恢复；官方repo精确窗口补检T1/Avatar/Video1.5/WorldPlay，必要变化题摘/历史README/patch已读 | 受阻 | WorldPlay历史README Dec17无时区，commit不证明public；Video1.5 all_gather backward修订需公开revision事件。2025目录缺口、两具名事件日期隔离，不称普通维护或零事件 |
| SRC-ZAI | Research第2页累计18条、底部没有更多；Dec21 GLM4.7→Dec10TTS→Dec9ASR→Dec7GLM4.6V已越窗；release notes Dec22/Dec11相邻段 | 已检查 | 本窗目录未发现条目；不以release notes替论文目录 |
| SRC-BYTEDANCE-SEED | 官方API Blog类型2/论文类型1，2025第一页的精确邻接段：Blog Dec24/18/16/2/Nov27，论文置顶Seedance、GR-RL后Oct21以下。Blog事件ID1817；必要Blog正文及链接2512.13507v1 p2–8已读 | 已检查 | 声明发布时间可用，但未取不可变2025 Blog上线日志；不授论文个体公告时间 |
| SRC-BAIDU-ERNIE | 中文技术Blog第1页10条，Dec23 Preview1203→Dec9 Preview1103→Nov21 Preview1120，下页2/2；本页已越过本窗 | 已检查 | 未发现该目录本窗条目，非全网无遗漏 |
| SRC-XIAOMI-MIMO | 官方首页及MiMo-V2-Flash发布页；精确release commit65f0e738的README与31页paper必要方法/对照/安全反证已读；发布页December16无时区时刻、原始HTML无日期meta | 受阻 | 首公开时刻仍缺；commit不授public，明确隔离，不用2026 arXiv代替历史版 |
| SRC-MINIMAX | 官方研究Blog12条，Dec23 M2.1与Oct27 M2/Agent邻接，无Next/load-more | 已检查 | 未发现该目录本窗条目；Dec23仅后续恢复线索 |
| SRC-ARXIV | 官方语言模型、音视频/世界模型查询为提交缓冲 [Dec12,Dec15)、语言 [Dec15,Dec16)；系统收窄到具体GPU kernel/collective/LLM inference等14条及ML语义compute46条，[Dec14,Dec16)均到页尾；cs.CL官方长格式仅2512.12000–14000段标题补检。新增有效题摘与SIGMA定点§3–4保留，不把宽库存变队列 | 受阻 | 本轮有界发现/收窄已执行；提交缓冲不是公告池，个体first-public不可恢复的具名项隔离。日精度announcement空响应不证明零事件；没有全学科/全月召回保证 |

arXiv 查询与实际页尾分别保留在 [语言模型缓冲](../_sources/daily-20251217/ARXIV_LANGUAGE.md)、[Dec 15 语言模型线索](../_sources/daily-20251217/ARXIV_LANGUAGE_MON.md)、[多模态线索](../_sources/daily-20251217/ARXIV_MULTIMODAL.md)。[原系统查询](../_sources/daily-20251217/ARXIV_SYSTEM.md) 的裸 `kernel OR transformer` 引入纯统计与物理，240 项宽库存只留作历史发现线索，已撤销其覆盖资格，不转成逐项关闭队列。后续 GPU/kernel/collective/compiler 必须带大模型/ML 系统语义或相关系统分类，不扩全月扫描。

## 3. 候选与判断

确定当窗候选1个家族、1个官网Blog发布事件；不能用本事件的时间给链接论文另授首公开归属。其余日期保留项不计分母，亦不因外部缺口改成低分或零命中。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Seedance 1.5 pro 官网Blog](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro) | 2025-12-16T18:47:38+08:00 | 独立音画条件难以保证一致→联合MMDiT、coherence数据与联合reward链→须从联合分布/训练信号解释；2+2+2=6 | 标准完成 | 仅报告：联合路线真实，但模块细部与机制级归因不足，不能超出现有Ch24一致性约束；非作者具体对读通过 |

## 4. 证据与知识整合

### [Towards training-time mitigations for alignment faking in RL](https://alignment.anthropic.com/2025/alignment-faking-mitigations/)

已读证据支持收窄的研究问题：在构造的model organisms中，降低被监控的alignment-faking行为不一定降低训练内外compliance gap；interrogation可能产生反效果。必要方法/对照/限制已读且root已独立核验明确位置：interrogation turn产生reward但梯度mask，组采样8、1024 episodes/step，干预15/30步并不一致，高seed方差；虚构free/paid监控设定不能当生产安全证明。日期暂缓不抹去这个训练增量，见[Ch31局部提案](../_sources/daily-20251217/BOOKS_ALIGNMENT_PROPOSAL.md)。

具体 Books 对读：`TRAIN-RLHF` [Ch31 开头](../../../../books/part-04-training-system/31-rlhf.md) 已把偏好学习解释为代理目标，明确 reward hacking、标注偏差与 pipeline 成本；这还不等于覆盖“用 interrogation 或 scratchpad 奖励干预，可能降低可监控表现却保留/扩大训练外差距”的比较机制。相邻 PPO 的目标/梯度承载仍须对读。

`PLATFORM-EVALUATION-SYSTEM` [Ch66 的 Observed Capability 与 Elicitation Ceiling](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#observed-capability-与-elicitation-ceiling-必须分开) 已具体承载自然行为、elicitation probe、监督者识别上限，以及无监控/声明监控配对条件和 model-organism 外推边界。该评价边界已有覆盖，不为相同原则再增一段；训练干预的具体反效果是否新增，由 Ch31 必要证据决定。以上是局部对读，不是 Books 整合完成或整篇已有覆盖。

### [SAM Audio](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/) 与 [PE-AV](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)

完整题摘分别支持统一提示分离及整体/帧级对齐区分。官网PDF有限失败后，可得的较晚arXiv精确v1必要正文已读，详见[Meta必要证据](../_sources/daily-20251217/META_NECESSARY_EVIDENCE.md)。SAM span-only在持续声/音乐中退步，SAJ与人工相关不等于逐例或分布外正确；PEA-Frame local/global目标在边界与误报间取舍，八种pretrain pair与stage2两种joint pair不能混作相同十项消融。Ch23全局≠局部对齐原则已有具体覆盖，不宣称全部新机制已覆盖。两研究首公开日期和12/16精确正文均未恢复，暂缓Books；SAM普通X公告不新增独立论文候选。

### [Seedance 1.5 pro 官网Blog](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)

Blog 披露联合生成、数据调度、后训练及 distillation/quantization/parallelism 的组合；[2512.13507v1 题摘/版本史原始记录](../_sources/daily-20251217/SEEDANCE_V1_ABS.md) 明确 dual-branch DiT 与 cross-modal joint module。拟采用范围是联合音画条件建模，不能从 Blog 的 10× 声称配置无关加速。v1 提交 `2025-12-15T16:36:52Z`、v2 提交 `2025-12-16T16:58:55Z`，均不是个体公开时刻；必须读精确公开事件版本而非静默采用当前 v3。

本次明确采用Blog发布事件；必要原文与v1 p2–8已读，具体披露/反证及Ch24现有音画共享条件段对比见[Blog证据](../_sources/daily-20251217/SEEDANCE_BLOG_EVIDENCE.md)。Blog当前UpdateTime较晚，未声称取得不可变2025正文；只采用与早期精确v1相容的联合设计轮廓。模型卡没有联合模块方程/消融与可比加速配置，不从模型声望或recipe名称推导长期知识写入。

## 5. 缺口与下一步

**普通待办：** 0。最后相关题名对照已补两项可得PDF：2512.12595v1按具体新增机制未成立关闭，2512.13352v1保留ranking与confirmation不同的评价增量；不是日期失败豁免题摘/准入判断。非作者已定点核验这些判断与完整停止点，并纠正SIGMA Effective Utilization/MFU的指标混淆。新增potential及停止依据见[原始准入记录](../_sources/daily-20251217/ADMISSION_ADDITIONS.md)与[SOURCE_STOPS](../_sources/daily-20251217/SOURCE_STOPS.md)，不是覆盖通过或零事件证明。

**已隔离的外部日期/版本保留项：** Anthropic alignment-faking、Meta PE-AV的首公开时刻经[四事件日期恢复](../_sources/OFFICIAL_EVENT_DATE_RECOVERY.md)有限官方路径穷尽，保留潜在贡献与已读必要证据，暂缓当窗采用与Books。SAM官方X `2000980784425931067` 发布时间12/17 01:26:10+08，只证明公告；没有独立新贡献不重收为论文，原研究页首公开仍隔离。Meta官网12/16 PDF不可得，较晚arXivv1可读但历史同一性未证，需官网原PDF或官方版本一致说明。每项重开条件与精确原始链接在sidecar/Meta证据文件；不用转载、提交、OAIupdated补时刻。Seedance声明的Blog事件日期已通过root独立JSON核验，不再列作日期受阻。

**arXiv与仓库具名保留项：** [新增准入线索](../_sources/daily-20251217/ADMISSION_ADDITIONS.md)保存精确v1题摘、增量、反证/安全信号与范围排除理由。普通题摘读取和SIGMA决定准入的§3–4补读已执行。必要个体first-public历史记录不可恢复的项，不计确定候选、不评分、不写Books；重开需要官方new公告/RSS或首次正文上下界，不能用常规EST20:00排期批量授日期。WorldPlay与Video1.5修订还需公开release/push记录，不以commit时间证明上线。日期隔离不证明覆盖通过，也不把已发现有效贡献删掉。

MiMo历史release的[必要正文与反证](../_sources/daily-20251217/MIMO_NECESSARY_EVIDENCE.md)已读；MOPD Table7反驳全领域保住best teacher，AppendixB记录SWE-Bench未来commit泄漏。日期保留项需要官方first-public上下界，非普通读文受阻，不采用其完整模型/安全保证，不据此写Books。

**历史目录保留项：** OpenAI原始目录/RSS、Anthropic主Research历史部分、Google publications首发段、Qwen迁移后历史目录、Hunyuan2025目录，经本轮有界原始/替代入口仍不可恢复。恢复条件是相关官方历史邻接段/可读分页或真实窗口发布记录，只重开该来源/身份；各来源已知有效材料均保留。这些限制不支持“本窗无遗漏”。

以上均为本窗终态保留项；重开条件是对应身份的官方首次公开范围、历史版本同一性或来源原始邻接证据。隔离不支持正面证据、Books或无遗漏断言，不计Coverage/Evidence通过。

**必要源审与Books交接：** Anthropic必要正文及Seedancev1明确位置已由root独立读过，复用其源审，不重复全篇抓取。Seedance具体Ch24差异“仅报告”已获非作者定点校准；Anthropic训练干预具体增量的Ch31局部草案在日期隔离期间不请求实际写书，不宣称已有覆盖。Meta必要可得替代正文已读，不能把它们称为尚未读完的外部受阻。

**已关闭负侧：** 三项具体理由与读取位置见 [准入记录](../_sources/daily-20251217/ADMISSION_CALIBRATION.md)。非作者已实际读湿实验核心，与先前FrontierScience/Images共3项官方负侧抽检；GPT-Image-1.5 独立安全材料若有实质变化须定点重开。

## 6. 复核

复核者：主线程（独立于报告作者 Nash）。

结论：通过

[实际复核记录](../_sources/daily-20251217/ROOT_ADMISSION_REVIEW.md)覆盖唯一拟入选事件的原文、声明日期与Ch24具体差异，相关安全/纠错/设计反证的完整题摘及必要正文，14源有限停止点和外部保留。普通负侧抽检3项官方核心与2项arXiv机制/任务样本，不授全量正文验证；SIGMA指标混淆已更正。无Books写入后待办，日期和历史缺口不计正面通过。结构校验另行执行，不替代语义复核。
