# Daily Research — 2026-02-10

**规范：** V3
**窗口：** 2026-02-09T09:00:00+08:00 ～ 2026-02-10T09:00:00+08:00
**补充窗口：** 2026-02-09 ～ 2026-02-09
**窗口说明：** 用户于2026-10-08要求现存2026 Daily只补来源遗漏，保留既有窗口、候选公开时间、日期归属与有效审阅；新增按北京前一完整自然日date-only检查，不迁移旧候选。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T13:29:40+08:00

## 1. 结论

2026-10-08增量补查：14个每日来源已按实际入口有限检查，未扫描Weekly或90天catchup；未确认新的当窗候选，原135家族及36整合/3已有覆盖/有效审阅全部保留。root实际独立校准读10个旧身份完整题摘和3个新身份完整题摘：HQP/PointViT/LAAFD/comparIA/DiTS关闭成立，PlanViz和ILA-agent贡献不足具名关闭，RAIGen已有候选有效复用；DAVE/ABR的旧泛模板“无机制信号”与具体梯度分解/label-flip重置相矛盾，只撤销这两项关闭理由并转必要日期保留，新pixel-text负面设计信号也按日期隔离。Seed有限后页恢复新增SAGE采样+RL效率迁移信号，经root校准成立但首次公开日未核。共4项日期保留（2既存+2新），不新增确定候选/评分/Books，不深审绕日期门。本轮SOURCE、13个完整题摘准入校准与六部分独立DAY均实际通过；扫描/筛选/审阅/Books修改/独立复核的普通待办为0，有限外部保留不授无遗漏；下列原完成结论只陈述此前有效成果，不代替补查验收。

来源发现与有限贡献筛选已停止，候选清单冻结为135个唯一家族，均获单项独立终裁：111项必要标准/深入证据审阅（36项实际整合并获root POST、06181/RelayGen/FCDP三项具体已有覆盖、72项仅报告），17项低分关闭仅报告，7项中心争议安全隔离。PKA与RFDM因实际依赖/生成机制变化改为5分标准审阅，非因Only或费时降分。有效36项POST保留，不把局部recipe缺位自动写成长期gap。普通扫描、筛选、审阅及Books待办为0；root已通过当前六部分日级Gate，本日按安全终态完成；完成不把外部保留项升级为正面证据。

本轮实际读过170个论文完整题摘，另核06049广告条目；这是已有主题线索的语义筛选范围，不是170个候选，也不是整个arXiv分类全量审计。旧库存496、旧报告13个retained与完成标签不授本轮V3结论。[逐身份记录](../_sources/daily-20260210/feb10_v3_screening.md)中旧162个“潜在增量”不是准入结论：150个正常Submitted身份仅在官方最早公告下界、注册上界与无更早同正文公开信号的条件下落窗，12个早期Submitted身份保留日期缺口。必要工作只来自已校准的具体贡献或决定准入的含糊事实，不要求逐项评分/正文审阅全部日期身份。06549通用学习纠错保留；有限入口已停止，135实际候选冻结，不因宽库存存在继续扩池。15项有具体贡献前关闭依据，12个早期Submitted日期保留身份不评分/不入候选；其余主题线索不是强制逐项正文队列。外部来源切片限制仍隔离，不支持完整Coverage或无遗漏断言。

## 2. 来源覆盖

[此前来源检查原记录](../_sources/daily-20260210/supplement-20261008-original-source-record.md)完整保留2026-10-04有效事实；本节仅下表维护当前实际范围，不将历史旧行重复计为本轮覆盖。

Daily 未扫描 Weekly 来源。GitHub 仅为实际发现 Kimi 发布及必要受影响实现，不作通用软件发布巡检。错误的 arXiv /2602 URL 与空 native_final_0 不证明零命中。

2026-10-08增量实际入口与停止范围（此前原记录已保留；当前恢复不否认旧检查事实）：[首查A](../_sources/daily-20260210/supplement-20261008-nativeA.json)、[首查B](../_sources/daily-20260210/supplement-20261008-nativeB.json)、[有限查询/后续原源](../_sources/daily-20260210/supplement-20261008-queries.json)、[原生metadata](../_sources/daily-20260210/supplement-20261008-native-metadata.json)、[有界标题响应](../_sources/daily-20260210/supplement-20261008-bounded-titles.json)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | web入口XML不支持后直接提官方RSS metadata1255项，有限读取Feb08–11北京邻日title/pubDate/link，Feb09 GenAI.mil是旧有效关闭、Feb11Harness窗外；广告旧原件定点复用，不扩产品目录 | 已检查 | 全RSS现目录的元数据提取不是1255项题摘/正文筛选；无其他可见本窗项不证明历史全站发布为0 |
| SRC-ANTHROPIC | Research原页首10条，现为Sep04–Oct01；Feb09日期主题补检后停止 | 受阻 | 未恢复Feb09原目录；官方当日分页/快照到达只重开该切片 |
| SRC-GOOGLE-AI | DeepMind research当前页、Research pubs首屏；官方2026/02 Blog实际7条，Feb09 Perch与Feb10后项相邻；复用Perch科学应用旧关闭 | 受阻 | Blog暴露7条不是此前8条全量否定；pubs/DeepMind历史切片有限 |
| SRC-META-AI | Research原页空文本，保留此前窗口主题补检限制，本轮原入口后停止 | 受阻 | 空文本不证明无发布；需带日期官方当窗目录 |
| SRC-QWEN | qwenlm旧页转动态入口；官方retrieval API一响应40项，仅抽id/title/extra.date，Feb03CoderNext→Feb10Image2.0；不按40项读正文 | 已检查 | 可见日期metadata无Feb09，不证明删页/非目录发布无遗漏；API不是独立首次公开日志 |
| SRC-DEEPSEEK | 官网及/news原生5动态+10研究标题，研究相邻Jan28OCR2→Feb25DualPath，停止首屏；未读取Next隐藏库存 | 已检查 | 可见目录无Feb09，不能代表未暴露历史；不借用户issue授新根因机制 |
| SRC-MOONSHOT | Platform Blog当前旧列表；Kimi1.10.0已核release/受影响文件的旧事件与证据定点复用 | 已检查 | 本轮无已证新修订；Platform完整历史有限，不巡检整个GitHub软件发布 |
| SRC-TENCENT-HUNYUAN | Research空文本；本轮浏览器一次timeout约94.2秒后停止；官方publicList page1/pageSize12/renderType0实际11条metadata，首Sep21、尾Feb03，相邻Feb13/Feb03 | 已检查 | publicAt/publishedAt/displayPublishTime分别保存，不把展示或回填日期当first-public；只查11条暴露目录，无Feb09条目不等历史全站0 |
| SRC-ZAI | 官方Research恢复175行当前16标题，Feb02GLMOCR→Feb11GLM5相邻；停止该原页 | 已检查 | 恢复的是可见研究切片，不推翻旧空页记录、不证明机构全历史无遗漏 |
| SRC-BYTEDANCE-SEED | 原页10papers+5blog及public_papers首20/242只定位；官方get_article_list_v2 type1,count20,publish_year2026,order_desc=true,token60,localeus+US header实际19项，Feb26→Jan26跨Feb09，next80未取即STOP；type2 token60空后回token0实得14、next空/has_morefalse | 受阻 | type1 total82并非本窗82；type2 total19但仅14可见，限制覆盖权限。Feb09 Protenix-v1标题科学应用暂缓范围外，SAGE08354具体采样/停止增量待日期；PublishDate可能回填且不同于历史公开证明，不把后来的ArticleID/UpdateTime当首次公开 |
| SRC-BAIDU-ERNIE | 原Blog暴露10条，Feb06→Apr15相邻，停止该页 | 已检查 | 本窗可见切片无项，未证明其他官方原件不存在 |
| SRC-XIAOMI-MIMO | Paper8项日期切片Jan08/Feb03→Mar13；当前15个undated Blog标题，停止原页 | 受阻 | Paper无本窗条目；undated Blog缺首次公开日不能批量落窗 |
| SRC-MINIMAX | EN Blog12项Jan27→Feb12→Feb14相邻；Agent Tech Blog仅15行导航，停止可见页 | 受阻 | EN切片无本窗项；Agent历史内容未恢复，空导航非0 |
| SRC-ARXIV | 四主题窗口搜索：模型/训练（foundation/language model、Transformer/MoE、optimization）、推理/系统（inference/GPU/parallel/kernel）、多模态（world/VLA/generative）、Agent（tools/planning/memory/RAG）。exact-date搜索空召回、Advanced cache miss、API失败、直连15秒timeout；改以CL351–450、CV601–650、AI301–350、LG1001–1050、DC1–50与AR默认页L122–214（含第17项D-Legion及其后窗外标题）标题有界查漏，完整AB只读具体相关身份 | 受阻 | 月标题仅身份线索不证明当日公告；未展开全类/整月。CL301–350、CV401–450/551–600、AI701–750、LG651–700/1101–1150、AR/DC首屏只定位段，月份/段位错误未进入题摘队列；必要公开日4项单独隔离，搜索失败不记0 |
| 补检：[学术搜索](https://arxiv.org/) | 固定本窗日期+四主题、2602.06身份/主题有限恢复；二手索引只负责线索，08329/08335/09017与05386v2均回abs核事件 | 检索受限 | 第三方Feb09标签不授首次公开日；不继续月库存或90天catchup |

本轮按需清单没有新的实际触发事件；Kimi旧release证据复用是既存事件去重，不据此扫描其他按需或Weekly来源。原先DataCite/PersonaPlex定点证据有效保留，只用于已有具体身份，不反推发现新候选。完整题摘新读身份中8项加ABR/CER均是旧170筛选的定点重复；06973/06976/08354为本轮3个新完整题摘身份，不把宽标题段数当新论文数。

独立Source检查发现RSS可直取、Seed官方后页尚未实际尝试，故只补两处有限差额：[RSS/Seed恢复原件](../_sources/daily-20260210/supplement-20261008-rss-seed-gap-recovery.json)。RSS元数据邻日定位未新增确定候选；Seed token60跨本日，不取next80及月份更早条目，Blog token0已到empty-next但14/19限制明确。SAGE2602.08354v1不把期初/月目录全量转为队列；必要首公开日未核不得读核心代替日期门。SOURCE及SAGE完整题摘已获root独立复核通过，当前六部分DAY亦实际通过，到此STOP，本日普通待办为0。

## 3. 候选与判断

本轮补查不新增确定候选行，不重排或改写以下原135行。4项公开日必要缺口见§5；DAVE/ABR仅撤销具体错误关闭理由，未改旧ledger/日期/原候选。PlanViz题摘只给新任务、human-QA和宽泛limitations，没有具体评价盲区/条件差额，贡献不足关闭，不以“局部”本身拒绝；ILA-agent只给行为工具组合与宽泛trajectory patterns，也未展示新的执行控制/可靠性边界，贡献不足关闭而非日期hold。其他代表关闭及RAIGen重复均经root校准，不把所有旧筛选/月份标题变成待深审队列。[完整题摘原件](../_sources/daily-20260210/supplement-20261008-abstracts.json)。

日期依据补核：[arXiv官方公告与ID规则](https://info.arxiv.org/help/availability.html)明确正文随scheduled announcement公开，final arXiv ID在公告时分配、不能提前提供ID/DOI。因此专属DOI注册已含finalID可作为公告发生的上界，与Submitted后的最早公告建立本日包络；这是有限推定，不是把注册时刻伪装精确正文公开，也不以当前findable倒推历史。保留每项Submitted/Updated/Created/Registered原值及无更早同正文公开信号条件，12个早期Submitted缺口不因此解决。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi CLI 1.10.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.10.0) | 2026-02-09T23:03:56+08:00 | CLI/Web 能力配置不一致及 processing 时输入状态 → Web worker 传递全局 MCP 配置、ready 后消费当前会话文本队列 → 需验证配置失败降级与 session 切换时队列清理；1 + 2 + 2 = 5 | 深入完成 | 仅报告：版本特定接口变化，不新增配置来源/连接/动作执行分责的长期论点 |
| [Compressing LLMs with MoP: Mixture of Pruners](https://arxiv.org/html/2602.06127v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:34:48+08:00 | 单轴结构剪枝限制搜索空间 → 以当前层参数数匹配width删除量、混合深宽路径且random≈proxy → 分开检验结构互补与选择器成本；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)稀疏段前两段；root实际写后复核通过 |
| [MoSE: Mixture of Slimmable Experts for Efficient and Adaptive Language Models](https://arxiv.org/html/2602.06154v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:35:26+08:00 | 异宽expert组不是同expert多宽 → nested prefix与full/random双宽训练、router概率映射width → 分开验收切片训练与裁剪后的实际预算；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)异宽group与elastic path之间两段，实际POST通过 |
| [Stop the Flip-Flop: Context-Preserving Verification for Fast Revocable Diffusion Decoding](https://arxiv.org/html/2602.06161v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:35:36+08:00 | remask验证抽走draft context → cache override与own-diagonal correction两视图 → 局部attention校正与全网泄漏/采样exactness须分开；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)Self-revision内两段，实际POST通过 |
| [Uncertainty Drives Social Bias Changes in Quantized Large Language Models](https://arxiv.org/html/2602.06181v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:03+08:00 | aggregate不变可相抵逐例/子群flip → paired分层实测并核judge误报 → 不以平均bias或单一entropy关系授安全precision；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)“量化验收不能只看平均分：逐例一致性与分布漂移”，具体Existing独立通过，无新写 |
| [To 2:4 Sparsity and Beyond: Neuron-level Activation Function to Accelerate LLM Pre-Training](https://arxiv.org/html/2602.06183v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:06+08:00 | activation自然稀疏不等硬件pattern → 六FFN GEMM按operand选择、cluster/router/row permutation配布局 → sparse阶段与dense恢复/总成本分账；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)Dynamic Sparsity后两段，实际POST通过 |
| [Is my model "mind blurting"? Interpreting the dynamics of reasoning tokens with Recurrence Quantification Analysis (RQA)](https://arxiv.org/abs/2602.06266v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:38:02+08:00 | hidden trajectory的RQA重复/laminarity是局部complexity诊断，未给有效stop/budget校准；1 + 1 + 1 = 3 | 已关闭 | 仅报告：局部proxy应用未改变可执行推理预算策略，无书稿增量 |
| [RoPE-LIME: RoPE-Space Locality + Sparse-K Sampling for Efficient LLM Attribution](https://arxiv.org/abs/2602.06275v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:38:15+08:00 | 固定closed-model output、open surrogate RoPE locality/NLL fitting与Sparse-K是局部替代，未建立closed-model faithfulness新边界；2 + 1 + 1 = 4 | 已关闭 | 仅报告：局部归因配方不授替身忠实性，未改变现有owner论点 |
| [Accelerating Vision Transformers on Brain Processing Unit](https://arxiv.org/abs/2602.06300v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:38:49+08:00 | 固定weight将linear/LN改conv适配CNN型BPU是局部lowering，受测速度数字不添通用编译保证；1 + 1 + 2 = 4 | 已关闭 | 仅报告：器件/算子适配是既有lowering原则局部实现，不新增长期机制 |
| [Self-Improving World Modelling with Latent Actions](https://arxiv.org/html/2602.06130v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:34:52+08:00 | 单inverse辅助目标不能同时验证可辨与观测保真 → 冻结FWM/IDM交替likelihood feedback → state-only后阶段与物理真值/ELBO身份分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)Inverse Dynamics后两段，实际POST通过 |
| [Learning Rate Scaling across LoRA Ranks and Transfer to Full Finetuning](https://arxiv.org/html/2602.06204v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:36+08:00 | 统一LR混淆factor初始化/scale → 受限rank-width scaling与FFT必要迁移条件 → 用参数化缩小search而不授有限最优常数相同；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)同LR公平对照段后两段，实际POST通过 |
| [DeDPO: Debiased Direct Preference Optimization for Diffusion Models](https://arxiv.org/html/2602.06195v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:23+08:00 | 全池pseudo criterion有标签偏差 → 代表性标注子集true-minus-pseudo loss residual → 分开估计器身份、采样/independence条件与训练policy保证；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md)clean-anchor后两段，实际POST通过；符号/收敛子命题隔离 |
| [SOCKET: SOft Collision Kernel EsTimator for Sparse Attention](https://arxiv.org/html/2602.06283v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:38:26+08:00 | hard hash无分级排序 → soft query/hard key概率聚合rank → 选择接口与全N扫描/最终attention契约分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)trained selector至pyramid之间两段，实际POST通过；权重冲突不采用 |
| [When Agents Say One Thing and Do Another: Validating Elicited Beliefs from LLMs](https://arxiv.org/html/2602.06286v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:38:30+08:00 | 输出概率未必足以解释选择 → unknown utility条件下decision-sufficiency否证 → 分开可拒绝条件、truthfulness与utility alternatives；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)confidence三层后两段，实际POST通过 |
| [Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math](https://arxiv.org/html/2602.06291v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:38:37+08:00 | 原答案oracle不足 → 作为工作假设测verified邻题迁移utility → 检查邻域/solver辨别力而不授正确概率；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)active judge至panel之间两段，实际POST通过 |
| [Can Post-Training Transform LLMs into Causal Reasoners?](https://arxiv.org/abs/2602.06337v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:39:42+08:00 | 定向causal人口+五现成posttrain配方是局部训练比较，未声明新失效条件；1 + 1 + 2 = 4 | 已关闭 | 仅报告：不从成绩/robust标签採普遍因果推理保证，无新owner机制 |
| [Cost-Aware Model Selection for Text Classification: Multi-Objective Trade-offs Between Fine-Tuned Encoders and LLM Prompting in Production](https://arxiv.org/abs/2602.06370v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:29+08:00 | 四固定label集的encoder/LLM成本质量比较为局部现成Pareto应用，未新增归因/失败边界；1 + 1 + 2 = 4 | 已关闭 | 仅报告：不为成熟model-choice原则借分，不改变长期论点 |
| [The Condensate Theorem: Transformers are O(n), Not O(n²)](https://arxiv.org/html/2602.06317v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:39:13+08:00 | 全AR有限support/无损与总线性claim → 核greedy/attention identity及全QK扫描冲突 → 不采用exactness或固定KV保证；3 + 1 + 2 = 6 | 争议 | 暂缓：中心恒等/复杂度及未来TopK状态不足，精确重开见§5，无Books写入 |
| [Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems](https://arxiv.org/html/2602.06319v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:39:16+08:00 | graph难度与文本长度耦合 → 固定topology/node-name扩长及正确trace观察 → 分开表示长度混杂与selfverify因果；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部lexical扩长与trace观察不构成通用停止策略，非主题式Existing |
| [Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigating Replay and Context-Binding Failures in AP2](https://arxiv.org/html/2602.06345v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:39:53+08:00 | 签名不阻runtime replay → 作者mock context/nonce gate → 有限trace不证明并发state上界或副作用exactly-once；1 + 2 + 1 = 4 | 深入完成 | 仅报告：版本未锁的局部模拟，成熟binding已有承载，不授正式协议漏洞或生产安全 |

| [Action Hallucination in Generative Visual-Language-Action Models](https://arxiv.org/html/2602.06339v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:39:45+08:00 | fixedstate连通latent到分离safe modes/薄contact tube的支持几何条件，不授所有VLA危险；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 L176/178](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际POST通过 |
| [FlowConsist: Make Your Flow Consistent with Real Trajectory](https://arxiv.org/html/2602.06346v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:39:54+08:00 | real/fake双估计器stopgrad整流是FM额外分支，Eq9/残差积分不授exactKL或单调；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24 L436/438](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，实际POST通过 |
| [Di3PO - Diptych Diffusion DPO for Targeted Improvements in Image Generation](https://arxiv.org/html/2602.06355v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:07+08:00 | 同次diptych+边缘控制/VLM过滤提出局部pair，不授pixel/sharednoise网络梯度取消；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-DPO` [Ch34 L277/279](../../../../books/part-04-training-system/34-dpo.md)，实际POST通过 |
| [SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass](https://arxiv.org/html/2602.06358v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:11+08:00 | 跨layer/token memory到generated LoRA为两阶段，省testtimeoptimizer不等无成本/反传等价；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-LORA` [Ch30 L705/707](../../../../books/part-04-training-system/30-lora.md)，实际POST通过 |
| [Training Data Selection with Gradient Orthogonality for Efficient Domain Adaptation](https://arxiv.org/html/2602.06359v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:13+08:00 | Navigator固定meananchor几何选mixture而非投影Target更新，不授naturallysafe/Pareto最优；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DATA` [Ch27 L1029/1031](../../../../books/part-04-training-system/27-data.md)，实际POST通过 |

| [ReBeCA: Unveiling Interpretable Behavior Hierarchy behind the Iterative Self-Reflection of Language Models with Causal Analysis](https://arxiv.org/html/2602.06373v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:33+08:00 | reflection时点混合 → stage-specific行为提案与单项/联合负侧 → 分开行为选择与因果识别；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80 L64/66](../../../../books/part-07-agent/80-reflection.md)，实际POST通过 |
| [Difficulty-Estimated Policy Optimization](https://arxiv.org/html/2602.06375v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:36+08:00 | rollout后零组丢弃已付成本 → warmup后估难并在rollout前筛题 → 预测极端不等真实零variance，核误拒/总成本；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33 L128/130](../../../../books/part-04-training-system/33-grpo.md)，实际POST通过 |
| [Uniform Spectral Growth and Convergence of Muon in LoRA-Style Matrix Factorization](https://arxiv.org/html/2602.06385v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:40:50+08:00 | factor分别正交化与product谱变化不同 → 受限连续动力学的active sqrt谱增长 → 核boundedness/过多mode及离散实现边界；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-LORA` [Ch30 L115/117](../../../../books/part-04-training-system/30-lora.md)，实际POST通过 |

| [Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution](https://arxiv.org/html/2602.06413v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:29+08:00 | strict-contraction条件的平均Bayes界与AR必然cliff/DAG必要性不是同结论；2 + 2 + 2 = 6 | 争议 | 暂缓：中心必然性未建立，精确重开见§5；不进入Books |
| [TrailBlazer: History-Guided Reinforcement Learning for Black-Box LLM Jailbreaking](https://arxiv.org/html/2602.06440v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:09+08:00 | currentprompt state忽略历史 → K步response/reward/mutator与attentionselector → 只保局部红队预算实证、不授全成本效率；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部attack selector经验不改变长期安全authority/验收分工，非主题式Existing |

| [MuCo: Multi-turn Contrastive Learning for Multimodal Embedding Model](https://arxiv.org/pdf/2602.06393v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:01+08:00 | causal多轮共享image forward与same-image counterpart mask改变监督/negative人口；相关pair非独立image，不授future可见；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)InfoNCE负例后L515/517，实际POST通过 |
| [Is Gradient Ascent Really Necessary? Memorize to Forget for Machine Unlearning](https://arxiv.org/html/2602.06441v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:10+08:00 | retain约束memorization→negative edit局部分支与GD普遍no-collapse/θfor保持claim不同；2 + 1 + 2 = 5 | 争议 | 暂缓：CE/NPO方向与中心安全论证未解析；仅描述局部作者结果，无Books新写，重开见§5 |

| [Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding](https://arxiv.org/html/2602.06412v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:28+08:00 | revision重开与永久compute-deactivation不同 → confidence/localKL停Q/FFN仍缓存可读KV → 分开固定row条件与全网/runtime边界；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)revision budget后L577/579，实际POST通过 |
| [Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters](https://arxiv.org/html/2602.06427v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:49+08:00 | fullfuture监督偏背景 → motion-region辅助重建训练 → 不改controller真值/目标近邻先验，核aux目标对照；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)fullfuture重建后L232/234，实际POST通过 |

| [Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO](https://arxiv.org/html/2602.06422v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:42+08:00 | terminal广播粗 → ODE-completed endpoint increment与sign-selected terminal替换 → 不授条件均值/因果或全成本优势；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)innercritic后L265/267，实际POST通过 |
| [Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization](https://arxiv.org/html/2602.06394v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:03+08:00 | 同频质量不同 → externalproxy/merge学习/固定artifact → 不采应用收益、通用optimality或免成本；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)BPE频率说明后L91/93，实际POST通过 |
| [VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems](https://arxiv.org/html/2602.06409v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:41:24+08:00 | jointfeature方向与interactive文本/视觉编辑的局部poison观察 → 不授pixel-feasible上传路径/consensus因果或普遍防线失败；2 + 2 + 2 = 6 | 深入完成 | 仅报告：feature-space局部实验、累加预算对照与必要附录未披露，不能转长期安全配方/生产保证 |

| [STACodec: Semantic Token Assignment for Balancing Acoustic Fidelity and Semantic Information in Audio Codecs](https://arxiv.org/html/2602.06180v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:02+08:00 | RVQ自发分层 → 首层teacher index固定但codevector自由、量化前SPD预测 → 核semantic重建取舍与teacher撤除边界；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)分层codec→混合codec间L182/184，实际POST通过 |
| [Multi-Way Representation Alignment](https://arxiv.org/html/2602.06205v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:37+08:00 | 独立pair maps → 正交共同参考后共享非线性corrector → 软几何代价与错误对应决定是否保留GPA；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)English pair-map后L67/69，实际POST通过 |
| [Emergent Low-Rank Training Dynamics in MLPs with Smooth Activations](https://arxiv.org/html/2602.06208v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:41+08:00 | 随机低维方向 → 受限任务初始梯度导出可训练basis → block外逐step界不等权重恒rank或LLM最小rank；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)谱optimizer→random scaffold间L119/121，实际POST通过 |

| [Coupled Local and Global World Models for Efficient First Order RL](https://arxiv.org/html/2602.06219v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:57+08:00 | 高保真rollout反向图昂贵 → global observation forward与当前policy刷新local latent/reward backward分责 → 一步accuracy不授导数/真实无偏；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)Imagined rollout机制后L314/316，实际POST通过 |

| [Cross-Modal Redundancy and the Geometry of Vision-Language Embeddings](https://arxiv.org/html/2602.06218v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:36:55+08:00 | 硬子空间净化→matching pairs共同SAE与soft code约束、energy mask→分开learned basis选择与语义/排名保持；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)SVD净化后L838/840，实际POST通过 |

| [BenchMarker: An Education-Inspired Toolkit for Highlighting Flaws in Multiple-Choice Benchmarks](https://arxiv.org/html/2602.06221v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:37:00+08:00 | 单轴repair可新增其它缺陷/多correct → 冻结原/修题人口并复验所有轴与uniqueanswer → 不以filtered排名代修复因果；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)MCQ contract后L423/425，实际POST通过 |

| [CORE: Comprehensive Ontological Relation Evaluation for Large Language Models](https://arxiv.org/pdf/2602.06446v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:17+08:00 | 无关系negative/control置信度评价→核relation映射与SCR分母→中心指标冲突不授架构幻觉机制；2 + 1 + 2 = 5 | 争议 | 暂缓：同题label映射/分母与selfreport读取未解析，不进Books；重开见§5 |

| [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/html/2602.06443v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:13+08:00 | 终局失败难定位→注入受控中间错误与过程监督→局部索引识别不等自然首个因果失效或live rollback；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受控数据/局部训练经验未改变现有诊断到执行恢复的长期接口，不授语义oracle或外部副作用恢复 |

| [BrokenBind: Universal Modality Exploration beyond Dataset Boundaries](https://arxiv.org/html/2602.06451v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:24+08:00 | 两集合仅共享pivot、缺完整配对→batch伪逆双pseudo-path训练约束→代理不替缺失观测真值；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)共同坐标后onlypivot两段L71/73，实际POST通过 |
| [On the Plasticity and Stability for Post-Training Large Language Models](https://arxiv.org/html/2602.06453v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:27+08:00 | noisy reward/KL梯度冲突→uncertainty softprojection→最终MLP更新与文字不一致，未授可执行配方或普遍稳定；2 + 2 + 2 = 6 | 争议 | 暂缓：中心更新/β与variance估计未解析，缺引用的AppD，不进Books，重开见§5 |
| [RelayGen: Intra-Generation Model Switching for Efficient Reasoning](https://arxiv.org/html/2602.06454v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:28+08:00 | 整输出固定模型→离线margin校准后segment handoff→换模型的context/KV身份及分布边界须验收；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)Model Switch Point正文L262–280，具体接口/退路已承载，非旧标签验收 |
| [Diffusion-State Policy Optimization for Masked Diffusion Language Models](https://arxiv.org/html/2602.06462v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:40+08:00 | 完整trajectory终奖缺冻结state内对照 → 缓存masked-state logits、全填支路终端评价且仅新actionpositions更新 → 分开局部候选credit与原rollout延续/理论无偏；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)diffusion credit分支后两段，root实际POST通过；未采用理论子命题精确隔离 |
| [Latent Structure Emergence in Diffusion Models via Confidence-Based Filtering](https://arxiv.org/html/2602.06155v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:35:27+08:00 | 后验生成filter→学习seed到同classifier label/confidence的proxy→生成前选择；2 + 1 + 2 = 5 | 标准完成 | 仅报告：同h标签/评估与监督probe、条件人口和未计净成本尚不足改变长期生成选择 |
| [Refining the Information Bottleneck via Adversarial Information Separation](https://arxiv.org/html/2602.06549v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:42+08:00 | task/noise分解→joint/shuffled依赖critic与跨层回收→比较独立性/有用残余的取舍；2 + 1 + 2 = 5 | 标准完成 | 仅报告：有通用增量但有限recipe未建立训练严格独立/唯一因果或普适优势，不因materials范围排除 |
| [Improve Large Language Model Systems with User Logs](https://arxiv.org/html/2602.06470v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:51+08:00 | 固化经验失败不应继续强发Expert→gap/checkpoint评价分流Expert与运行时Critic→分开回答者和反馈者的采用及调用成本；2 + 1 + 2 = 5 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)weight-memory后L644/646及末注2065，实际POST通过 |
| [Provably avoiding over-optimization in Direct Preference Optimization without knowing the data distribution](https://arxiv.org/html/2602.06239v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:37:25+08:00 | 二元胜负无法同时下估两侧→tie mass与disjoint-policy whole-response最小概率聚合→限定未知数据分布下保守偏好约束及token近似边界；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md)overoptimization后L285/287及末注507，实际POST通过 |
| [REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop](https://arxiv.org/html/2602.06248v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:37:37+08:00 | benign/relearning评价不能替代adaptive extraction→进化测试隐藏答案恢复→限定遗忘评价的攻击预算、访问及judge人口；2 + 1 + 2 = 5 | 深入完成 | 仅报告：known-answer/局部judge与预算不匹配不足改变长期擦除判断，不授全模型危险能力恢复或总体noFP |
| [Steering Safely or Off a Cliff? Rethinking Specificity and Robustness in Inference-Time Interventions](https://arxiv.org/html/2602.06256v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:37:48+08:00 | 无关能力回归不替代相关控制→target/related-control ID/same-control shifted三分→ID保留不授OOD保持；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)actuator效果后L502/504及末注1252，实际POST通过 |
| [D-Legion: A Scalable Many-Core Architecture for Accelerating Matrix Multiplication in Quantized LLMs](https://arxiv.org/html/2602.06252v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:37:43+08:00 | 量化投影shape难充满大阵列→细粒度core及spatial partial-sum聚合→受限布局与输入带宽取舍；2 + 1 + 2 = 5 | 标准完成 | 仅报告：cycle-accurate局部仿真与资源不等对照不授普遍布局或端到端低比特收益 |
| [GRP-Obliteration: Unaligning LLMs With a Single Unlabeled Prompt](https://arxiv.org/html/2602.06258v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:37:51+08:00 | prompt数量不能界定安全训练影响→故意不安全单prompt多rollout优化→分开alignment与逐能力回归；2 + 1 + 2 = 5 | 深入完成 | 仅报告：有限攻击实证未提供新防御或永久安全机制，utility平均保持不授每项能力保持 |
| [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/html/2602.06521v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:03+08:00 | world/planner共享状态不足→双BEV imagination与simulator监督reward加权action-head→核想象评价proxy而非真实控制保证；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受限proxy/阶段配方及inference扰动不改变长期动作验收机制，不授真实物理或唯一因果 |
| [AgentCPM-Report: Interleaving Drafting and Deepening for Open-Ended Deep Research](https://arxiv.org/html/2602.06540v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:30+08:00 | 直接模仿teacher停止有偏→over-expand后judge选draft截断并重标Terminate→改变停止监督来源但非最优停止；2 + 1 + 2 = 5 | 标准完成 | 仅报告：judge-defined停止标签与局部质量增益未建立真实饱和、成本最优或通用训练配方 |
| [Code vs Serialized AST Inputs for LLM-Based Code Summarization: An Empirical Study](https://arxiv.org/html/2602.06671v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:47:32+08:00 | 显式结构有token成本→raw/SBT/NIT/preorder的局部负侧比较→结构编码不自动值得预算；2 + 1 + 2 = 5 | 标准完成 | 仅报告：同epoch非等总预算、有限输入与pretraining重叠不能转通用结构选择规则 |
| [FCDP: Fully Cached Data Parallel for Communication-Avoiding Large-Scale Training](https://arxiv.org/html/2602.06499v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:32+08:00 | 重复跨节点参数AG→per-node host generation缓存与本地GPU shard重建→以主存及一致性成本换跨节点参数通信；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-ZERO` [Ch39 L263–269](../../../../books/part-04-training-system/39-zero.md)已具备同一exact-FCDP核心论点与条件，不重复写书 |
| [DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving](https://arxiv.org/html/2602.06502v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:36+08:00 | 单hash热点/逐请求漂移→动态prefix固定双候选与候选内待请求迁移→有限trace下locality/queue取舍；2 + 2 + 2 = 6 | 标准完成 | 仅报告：非uniform重复prefix与局部实测不授PoTC定理、一般SLO或新通用状态合同 |
| [Revisiting the Shape Convention of Transformer Language Models](https://arxiv.org/html/2602.06471v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:52+08:00 | 固定FFN扩张惯例→bottleneck内部残差与维度/层数再分配→局部同budget下shape取舍；2 + 1 + 2 = 5 | 标准完成 | 仅报告：联合再分配及有限quality反侧不授普遍更优或新的通用shape规则 |
| [Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning](https://arxiv.org/html/2602.06475v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:42:58+08:00 | episode潜状态扰动稳定性奖励→surprise token credit→范数/答案稳定不自动识别causal block；2 + 1 + 2 = 5 | 争议 | 暂缓：中心block识别/收敛与必要B/F实现缺失，不正面采用、不Books；重开见§5 |
| [Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention](https://arxiv.org/html/2602.06478v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:03+08:00 | 输入视图与目标计算耦合→独立input KV及层间cross co-refinement→新视图增量编码但target读取仍增长；2 + 2 + 2 = 6 | 标准完成 | 仅报告：局部NVS模型/训练/容量不同及品质反侧不授通用跨模态状态机制 |

| [JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks](https://arxiv.org/html/2602.06486v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:14+08:00 | 开放任务rubric难固定→expert skills与claim dependency门控→核生成checklist与证据可靠性；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部taxonomy及约15pp残余inflation未改变长期评价治理，不授sound score |
| [Adaptive Uncertainty-Aware Tree Search for Robust Reasoning](https://arxiv.org/html/2602.06493v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:24+08:00 | 固定PRM开销与proxy误差→MC-dropout筛选及controller分配→核质量/验证预算取舍；2 + 2 + 2 = 6 | 标准完成 | 仅报告：iid无偏假设与局部18:1校准不授dropout认证或E2E保证，未改变长期verifier接口 |
| [Subgraph Reconstruction Attacks on Graph RAG Deployments with Practical Defenses](https://arxiv.org/html/2602.06495v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:26+08:00 | query-only可恢复typed关系→核ID/decoy防线与utility→局部组合不单调且文本指标非安全认证；2 + 2 + 2 = 6 | 深入完成 | 仅报告：有限prompt防线反证未建立新硬保密机制，不授授权绕过或总体风险率 |

| [World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy](https://arxiv.org/html/2602.06508v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:44+08:00 | joint latent video/reward与闭环数据刷新→核共享reward与第二轮重初始化→不据co-evolving授独立真实observer；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限joint/data配方未建立新的真实闭环验收规则 |
| [HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction](https://arxiv.org/html/2602.06527v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:11+08:00 | 当前token双遍expert扰动与clean-prefix KV共享→核手工controller和预算→cache无K复制不授全E2E免费；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限路由/search实验未改变长期verifier或可靠性接口 |
| [LogicSkills: A Structured Benchmark for Formal Reasoning in Large Language Models](https://arxiv.org/html/2602.06533v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:19+08:00 | 分离symbolization/validity/countermodel→Z3输出核验及负迁移→不把行为成绩当模型内formal机制；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受控语言及非同训练预算不授普遍形式化选择规则 |
| [Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study](https://arxiv.org/html/2602.06547v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:39+08:00 | static→短动态→双作者有限确认→核未触发/漏检与balanced评价→不把全池未命中当安全；2 + 2 + 2 = 6 | 深入完成 | 仅报告：有限安全测量反证未建立新硬执行防线，不授全生态precision/recall |
| [Fine-Grained Model Merging via Modular Expert Recombination](https://arxiv.org/html/2602.06552v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:46+08:00 | 单task模型storage→同源component离线分组/搜索及task-router→核质量/storage与离线标签成本；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限library/search配方未形成新的通用坐标或运行时发布规则 |
| [SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees](https://arxiv.org/html/2602.06554v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:49+08:00 | 独立turn逆序更新→共享θ与suffix ratio实际训练→核理论桥梁和经验预算身份；2 + 2 + 2 = 6 | 深入完成 | 仅报告：限定经验分支，不采共享参数monotonic/global保证，非新通用顺序规则 |

| [Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks](https://arxiv.org/html/2602.06526v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:10+08:00 | corpus冻结不等qrel完整→旧pool未标相关造成假负与归因偏差→冻结judged pool/Unknown并补核topK重评价；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-RAG` [Ch76 L1166/1168](../../../../books/part-07-agent/76-rag.md)Corpus评价两段与末注1463，root实际POST通过 |
| [LIBERO-X: Robustness Litmus for Vision-Language-Action Models](https://arxiv.org/html/2602.06556v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:44:51+08:00 | 单一任务均分→累计扰动层级与重训测量→核混杂、deadline及成功谓词边界；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限压力测量不授独立能力因果或新通用验收机制 |
| [SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs](https://arxiv.org/html/2602.06566v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:45:05+08:00 | 视觉search与reasoning分开→多框合并/局部读取和专用SFT→核预算、负侧与行为回归；2 + 2 + 2 = 6 | 标准完成 | 仅报告：局部WBF/adapter替代不授新通用权责、OOD或E2E保证 |
| [AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/html/2602.06485v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:43:12+08:00 | 强summary并非足够→policy intent与task-reward端到端适配receiver接口→核局部summary消费而非能力ceil；2 + 1 + 2 = 5 | 标准完成 | 仅报告：有限policy-summary配方未改变长期可信context接口，不授pass@64生产或inference-stability因果 |

| [Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies](https://arxiv.org/html/2602.06575v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:45:18+08:00 | 被动state输入→instruction/proprio主动视觉vote与global context→核保留预算及动作侧成本；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部选择配方与不同保留率不建立新长期安全/表示机制 |
| [Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning](https://arxiv.org/html/2602.06584v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:45:31+08:00 | 一次latent生成→posterior局部优化与多轮ELBO/likelihood选轨迹→核自生成与真值分责；2 + 2 + 2 = 6 | 标准完成 | 仅报告：清洁示范依赖与非等预算局部替代不授自纠错/最优保证 |
| [Degradation of Feature Space in Continual Learning](https://arxiv.org/html/2602.06586v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:45:34+08:00 | 高isotropy期待保持能力→非平稳经验中几何与accuracy解耦→限制几何proxy采用；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部负侧与不同epoch不授唯一因果或全部正则失败 |
| [Echoes as Anchors: Probabilistic Costs and Attention Refocusing in LLM Reasoning](https://arxiv.org/html/2602.06600v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:45:53+08:00 | 重复prompt被视为开销→受控wrong-prefix提醒与paired teacher编辑→核likelihood/正确性及局部恢复；2 + 1 + 2 = 5 | 深入完成 | 仅报告：直接反侧与probe标签不授唯一layer因果或普遍提升 |
| [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:46:28+08:00 | point/pair跨mode监督与curriculum为局部judge训练替代；1 + 1 + 2 = 4 | 已关闭 | 仅报告：不采用debiased/性能宣传，不借成熟一致性原则加分，无Books增量 |
| [Trust Regions Sell, But Who's Buying? Overlap Geometry as an Alternative Trust Region for Policy Optimization](https://arxiv.org/html/2602.06627v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:46:31+08:00 | likelihood-ratio约束→sqrt-ratio overlap局部surrogate→核支持/Taylor及失败条件；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部替代与β敏感反侧不授全局单调/LLM保证，无长期改写 |

| [Scaling Speech Tokenizers with Diffusion Autoencoders](https://arxiv.org/html/2602.06602v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:45:56+08:00 | 低rate单码本CTC直接语义监督与理解/重建取舍；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Confundo: Learning to Generate Robust Poison for Practical RAG Systems](https://arxiv.org/html/2602.06616v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:46:15+08:00 | RAG分片/query shift及max两片reward的有限污染测量；2 + 2 + 2 = 6 | 深入完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [TrapSuffix: Proactive Defense Against Adversarial Suffixes in Jailbreaking](https://arxiv.org/html/2602.06630v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:46:35+08:00 | suffix tracing与harm AND evade指标的漏trace反侧；2 + 2 + 2 = 6 | 深入完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](https://arxiv.org/html/2602.06643v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:46:53+08:00 | tracking lag下scheduled参照与blind relative chunk接口替代；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Beyond Static Alignment: Hierarchical Policy Control for LLM Safety via Risk-Aware Chain-of-Thought](https://arxiv.org/html/2602.06650v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:47:02+08:00 | 层级CoT策略与Label2Action的局部拒绝/引导取舍；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Same Answer, Different Representations: Hidden instability in VLMs](https://arxiv.org/html/2602.06652v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:47:05+08:00 | 答案不变的五位置hidden drift与干扰对照；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [PrefIx: Understand and Adapt to User Preference in Human-Agent Interaction](https://arxiv.org/abs/2602.06714v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:48:32+08:00 | interaction-as-tool与31偏好的局部交互评价；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling](https://arxiv.org/abs/2602.06795v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:50:26+08:00 | 错误trace生成rubric的局部reward实现，20%非总gold/teacher预算；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [RAIGen: Rare Attribute Identification in Text-to-Image Generative Models](https://arxiv.org/abs/2602.06806v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:50:41+08:00 | MSAE频率/distinctiveness的局部rarity score；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing](https://arxiv.org/abs/2602.06862v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:00+08:00 | 共享parameter centers/input router的局部PEFT替代；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Robustness Beyond Known Groups with Low-rank Adaptation](https://arxiv.org/abs/2602.06924v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:24+08:00 | error subspace classifier logits局部鲁棒替代；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay](https://arxiv.org/abs/2602.06942v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:49+08:00 | 受控corpus/tokenizer的局部资源诊断，固定steps非matchedcompute；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [The Representational Geometry of Number](https://arxiv.org/abs/2602.06843v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:34+08:00 | 数字任务subspace间的局部关系几何测量，非计算因果；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |
| [CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/html/2602.06959v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:54:14+08:00 | ordered pano shortcut下context shuffle/条件分解和非单调反侧；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部实现/有限反侧，不授通用性能、安全或新的长期机制；具体边界见§4 |

| [Not All Layers Need Tuning: Selective Layer Restoration Recovers Diversity](https://arxiv.org/html/2602.06665v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:47:23+08:00 | CRC合法mass与条件entropy分账，整层恢复是局部checkpoint替代，非质量/行为普保；2 + 1 + 2 = 5 | 标准完成 | 仅报告：有限局部证据，不改变长期机制或保证 |
| [Pruning at Initialisation through the lens of Graphon Limit: Convergence, Expressivity, and Generalisation](https://arxiv.org/html/2602.06675v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:47:37+08:00 | factorised saliency的graphon极限与稀疏active-k条件，非任意剪枝或硬件加速保证；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限局部证据，不改变长期机制或保证 |
| [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/html/2602.06687v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:47:53+08:00 | verdict与rootcause分账及结构DAG训练；特殊TN定义和judge限制不认证程序因果；2 + 2 + 2 = 6 | 深入完成 | 仅报告：有限局部证据，不改变长期机制或保证 |

| [NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models](https://arxiv.org/html/2602.06694v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:48:03+08:00 | binary低rank/PTQ补偿与packed factor执行的局部质量资源取舍；2 + 2 + 2 = 6 | 标准完成 | 仅报告：局部证据与直接反侧不改变长期机制/保证 |
| [Explaining Grokking in Transformers through the Lens of Inductive Bias](https://arxiv.org/html/2602.06702v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:48:14+08:00 | LN路径与readout尺度/LR联动的grokking混杂反侧；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部证据与直接反侧不改变长期机制/保证 |

| [F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare](https://arxiv.org/html/2602.06717v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:48:36+08:00 | mixed-update availability与同prompt稀有正确轨迹coverage的概率区别；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)group-size内两段，实际POST通过 |

| [A Unified Framework for LLM Watermarks](https://arxiv.org/html/2602.06754v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:49:29+08:00 | hard/soft检测score约束与固定key重复多样性的有限理论边界；2 + 2 + 2 = 6 | 标准完成 | 仅报告：限定作者事实/条件结论，不新增长期保证或Books |
| ["Tab, Tab, Bug": Security Pitfalls of Next Edit Suggestions in AI-Integrated IDEs](https://arxiv.org/html/2602.06759v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:49:36+08:00 | recent-view/undo与transaction配置的版本特定安全failure路径；2 + 2 + 2 = 6 | 深入完成 | 仅报告：限定作者事实/条件结论，不新增长期保证或Books |
| [R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging](https://arxiv.org/html/2602.06763v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:49:41+08:00 | 正确verdict与judge对齐rationale的评价分解及能力反侧；2 + 2 + 2 = 6 | 深入完成 | 仅报告：限定作者事实/条件结论，不新增长期保证或Books |

| [Towards Understanding What State Space Models Learn About Code](https://arxiv.org/html/2602.06774v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:49:57+08:00 | CodeSSM频率行为未隔离容量 → probing/频率测量与小kernel/CNN替代 → 只支持有限组件选择；2 + 1 + 2 = 5 | 标准完成 | 仅报告：频率相关不授所有SSM能力或因果新诊断 |
| [Displacement-Resistant Extensions of DPO with Nonconvex $f$-Divergences](https://arxiv.org/html/2602.06788v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:50:17+08:00 | 偏好最优目标可移走in-sample mass → f最小点与outside reward条件界 → 区分抽象最优点和实际训练winner保持；2 + 2 + 2 = 6 | 标准完成 | 仅报告：限定理论/实例，不授优化器或能力普保 |
| [Optimal Learning-Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay](https://arxiv.org/html/2602.06797v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:50:29+08:00 | 固定预算schedule缺条件区分 → one-pass linear/FSL easy与hard区间最优shape/rate → 不能直接迁移LLM生产配方；2 + 2 + 2 = 6 | 标准完成 | 仅报告：假设下理论，不授全estimator或LLM保证 |
| [On the Non-Identifiability of Steering Vectors in Large Language Models](https://arxiv.org/html/2602.06801v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:50:35+08:00 | steering参数辨识的等价方向 → 原Prop1全prompt严格同分布命题缺共同非零ker/冻结模型桥梁 → 中心保证不能由局部近似替代；2 + 2 + 2 = 6 | 争议 | 暂缓：中心保证隔离，局部经验不写Books；重开条件见§5 |

| [ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training](https://arxiv.org/html/2602.06820v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:00+08:00 | 生成环境无独立任务真值 → 可执行seed/BFS与DB规则验证 → 只支持有限可行性/修复链；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限局部替代/关键反侧，不改长期机制或新保证 |
| [POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models](https://arxiv.org/html/2602.06822v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:03+08:00 | 静态剪枝难适应decode → R/C/P三分与online C重选 → 有条件的FFN质量/在线成本替代；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限局部替代/关键反侧，不改长期机制或新保证 |
| [Improved Sampling Schedules for Discrete Diffusion Models](https://arxiv.org/html/2602.06849v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:42+08:00 | uniform schedule未反映局部rate → entropy积分反函数替代 → 严格界与校准proxy必须区分；2 + 1 + 2 = 5 | 深入完成 | 仅报告：有限局部替代/关键反侧，不改长期机制或新保证 |
| [Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/html/2602.06869v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:09+08:00 | scalar reward权重可跨目标干扰 → 分布cov诊断与EMA控制 → 不等普通参数更新逐目标保证；2 + 2 + 2 = 6 | 深入完成 | 仅报告：有限局部替代/关键反侧，不改长期机制或新保证 |
| [NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices](https://arxiv.org/html/2602.06879v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:23+08:00 | mobile T2I受表示/计算约束 → 分阶段蒸馏与codec/prompt替代 → 只保留所测质量资源工作点；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限局部替代/关键反侧，不改长期机制或新保证 |

| [Decoupling Variance and Scale-Invariant Updates in Adaptive Gradient Descent for Unified Vector and Matrix Optimization](https://arxiv.org/html/2602.06880v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:24+08:00 | matrix scale与direction耦合 → variance谱及direction预调 → 必须区分局部loss工作点与更新/运行保证；2 + 2 + 2 = 6 | 深入完成 | 仅报告：局部设计/评价反侧，不授通用正确性、安全或资源保证 |
| [Vision Transformer Finetuning Benefits from Non-Smooth Components](https://arxiv.org/html/2602.06883v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:28+08:00 | 下游adapter选择缺诊断 → input sensitivity与子模块受控tuning → 局部plasticity指标不能替参数adaptability因果；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部设计/评价反侧，不授通用正确性、安全或资源保证 |
| [Prompt Reinjection: Alleviating Prompt Forgetting in Multimodal Diffusion Transformers for Text-to-Image Generation](https://arxiv.org/html/2602.06886v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:33+08:00 | 深层prompt信号弱 → 分布对齐与prompt reinjection → 有限probe/干预不等全部语义恢复；2 + 2 + 2 = 6 | 深入完成 | 仅报告：局部设计/评价反侧，不授通用正确性、安全或资源保证 |
| [When RL Meets Adaptive Speculative Training: A Unified Training-Serving System](https://arxiv.org/html/2602.06932v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:35+08:00 | traffic shift令draft陈旧 → verifier trace在线shadow训练/lazy sync → 净服务收益需计额外GPU与刷新代价；2 + 2 + 2 = 6 | 标准完成 | 仅报告：局部设计/评价反侧，不授通用正确性、安全或资源保证 |
| [Endogenous Resistance to Activation Steering in Language Models](https://arxiv.org/html/2602.06941v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:48+08:00 | 持续steer可被恢复行为抵抗 → matched-latent干预与attempt/success分账 → 表面restart非唯一有效monitor机制；2 + 2 + 2 = 6 | 深入完成 | 仅报告：局部设计/评价反侧，不授通用正确性、安全或资源保证 |
| [Agentic Uncertainty Reveals Agentic Overconfidence](https://arxiv.org/html/2602.06948v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:58+08:00 | 更多trace仍可能自信误判 → pre/mid/post与adversarial shift对照 → 校准平移和失败区分不混为安全路由；2 + 2 + 2 = 6 | 深入完成 | 仅报告：局部设计/评价反侧，不授通用正确性、安全或资源保证 |

| [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/html/2602.06949v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:59+08:00 | 两帧latent action与蒸馏工作点 → human-video迁移与短窗teacher → 需分开重建proxy和真实控制因果；2 + 2 + 2 = 6 | 标准完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [DAWN: Dependency-Aware Fast Inference for Diffusion LLMs](https://arxiv.org/html/2602.06953v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:54:05+08:00 | dense逐步unmask → attention依赖图与greedy independent set → 条件独立proxy须绑定质量/搜索成本；2 + 2 + 2 = 6 | 标准完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning](https://arxiv.org/html/2602.06960v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:54:15+08:00 | 固定摘要停时 → learnt boundary与跨轮RL → task reward不等摘要真值或无限horizon保证；2 + 2 + 2 = 6 | 标准完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/html/2602.06964v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:54:21+08:00 | 线性steer可偏离activation分布 → learned flow prior与denoise干预 → 局部fluency不等真投影/保语义；2 + 2 + 2 = 6 | 标准完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [Plato's Form: Toward Backdoor Defense-as-a-Service for LLMs with Prototype Representations](https://arxiv.org/html/2602.06887v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:34+08:00 | 无prior的backdoor抑制难辨 → paired prototype与SVD过滤 → 需分清已知base条件和benign代价；2 + 2 + 2 = 6 | 深入完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering](https://arxiv.org/html/2602.06911v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:07+08:00 | 单次attack排名漏调参 → utility约束下逐model最坏tamper sweep → finite代理不等全开权重安全；2 + 2 + 2 = 6 | 深入完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [Seeing Beyond Redundancy: Task Complexity's Role in Vision Token Specialization in VLLMs](https://arxiv.org/html/2602.06914v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:11+08:00 | 视觉token可probe不等可执行 → 删token/不同任务tuning反侧 → recoverability不等decoder可用因果；2 + 1 + 2 = 5 | 深入完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models](https://arxiv.org/html/2602.06771v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:49:53+08:00 | retention数据依赖 → concept-center AET与逐层参数惩罚 → 局部erasure替代不认证全部无关概念保留；1 + 1 + 2 = 4 | 已关闭 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models](https://arxiv.org/html/2602.06825v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:07+08:00 | uniform rollout → attention-entropy差与分组/峰值branch → 局部budget proxy不授最优/净免费；1 + 1 + 2 = 4 | 已关闭 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping](https://arxiv.org/html/2602.06850v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:43+08:00 | condition与image反馈耦合限制cache → condition-only KV与位置/keyword隔离 → 新依赖设计须评保留质量和失效；2 + 1 + 2 = 5 | 标准完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks](https://arxiv.org/html/2602.06854v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:51:49+08:00 | 多轮攻击reward忽略intent → intent×risk/detail → 局部reward不等独立安全判断或免feedback训练；1 + 1 + 2 = 4 | 已关闭 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/html/2602.06871v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:52:12+08:00 | concat条件不能控制forward residual → noise均值与keyframe更新 → 局部生成替代须评帧间误差/质量代价；2 + 1 + 2 = 5 | 标准完成 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |
| [Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models](https://arxiv.org/html/2602.06909v1) | 2026-02-09T09:00:00+08:00 ～ 2026-02-09T10:53:04+08:00 | 时序Transformer baseline配置混杂 → clean/leaky数据和深宽局部ablation → 不能唯一归因feature/diversity；1 + 1 + 2 = 4 | 已关闭 | 仅报告：限定局部实现/反侧，不授普遍性能、安全或新长期机制；具体边界见§4 |

## 4. 证据与知识整合

### [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/html/2602.06949v1)

[v1](https://arxiv.org/html/2602.06949v1) §3.3.1–4/Eq3–8、§4.1–7/T2–7实际必要源读。两帧VAE瓶颈32维proxy含未来frame，重建/KL不认证唯一action因果；target action MLP首层reset后全部权重finetune，不是latent天然grounded。chunk4/relative action/temporal差分局部可执行替代；data skill由GPT估算、scene表/正文口径不同，不采largest全面召回。700M latent model400k/b256，Cosmos2B/14B pre140k/b1024/256H100，post50k/b512/128H100；action对照pre50k/post25k同step但不是净资源同预算。T2 latent不胜MANO/retarget全部指标；T3更多data Counterfactual SSIM/LPIPS有反侧，T6 student PSNR/SSIM/LPIPS均降，T7 Counterfactual LPIPS .232→.234。self-forcing滑窗12/35→4denoise、student13–49frames截窗teacher监督不授无限horizon正确。50背景edit样本12人偏好不独立物理真值，20scene水果policy相关和10scene五checkpoint+externalvalue非通用simulator认证；§4.6/T6 FPS明确single H100，RTX5090 teleop是另一运行场景，不能合并性能配置，precision/batch/SLO/净模型价值成本与独立seedCI ND。有限跨embodiment/蒸馏工作点Only，不造新WorldModel长期因果保证/缺口。 root已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [DAWN: Dependency-Aware Fast Inference for Diffusion LLMs](https://arxiv.org/html/2602.06953v1)

[v1](https://arxiv.org/html/2602.06953v1) §3.1–2/4.1–3/Alg1、§5.1–3/T1–2/AppA原源必要读。last4layer attention去sink/diag/threshold形成每step依赖proxy，anchor放宽induced阈值、greedy conflict独立集（不是maximum最优独立集），不认证真实条件独立或生成同分布。观测consistency以最终decoded output为参照非外部任务correct；attention sink标记不能保证剔除真实依赖。H10080G、len256/block32（KLASS例外bestblock），LLaDA8/1.5与Dream7B；baseline default对比HumanEval选τedge/induced/sink，τlow按16model×benchmark逐项调，不是同search预算或独立holdout。T1 DreamGSM accuracy反退、LLaDA1.5 math/MBPP反退，LLaDAHumanEval TPS108.99低LocalLeap109.8；T2去CBS质量更高，len/block/threshold显式quality-speed取舍。precision/batch并发/SLO/CI与取attention/graph净cost ND，不授headline质量不损普保。局部dependency-guided unmask替代Only，不新增通用joint正确性机制或Books。 root已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning](https://arxiv.org/html/2602.06960v1)

[v1](https://arxiv.org/html/2602.06960v1) §3.1–3.3/Eq1–8、§4.1–2/T1、§5.1/T2–3与AppH1–2最低配置实际读，不遍历全理论proof。Qwen4B生成cold-start summary、特殊token/SFT3epochs，GRPO同trajectory reward/adv共享全轮、max5训练和max10评估，不是无界完成保证；summary边界由模型选，端任务reward不认证每摘要事实。8/32H200两模型RL1000/500step b128/G8/lr1e-6，同steps非同teacher/总token预算，vanilla train30720 vs迭代每轮10240，eval32k vs每轮8k×10 cap。8H200 TP1/DP8 Semaphore1024，temp.7/p.95×32采样不是32独立训练；CompassVerifier7B correctness代理和PRIME训练timeout判0分开。T2冷启动AMC fixed/random更高，不采alwaysadaptive；T3外summary冷启动更好/RL更差支持有限policy相容而非内部语义真值。T+E精度低于T，latency合所有round但无same-compute/cold-startteacher摊销/SLO验收。precision/独立seedCI ND；不授O(nℓ²)为全服务cost、信息瓶颈理论普保，有限summary/continuation训练Only，不按缺此配方增Books。 root已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/html/2602.06964v1)

[v1](https://arxiv.org/html/2602.06964v1) §2.1–3/§3.1–2/T1–2、§4.1–3/图4、§5.1–2/T4与AppB1/C2–3/C5必要读。单token residual的无条件flow MLP prior；先steer再加噪/20step denoise，非真实manifold精确投影或语义不变保证。FineWeb1B/中层Llama1B l7与8B l15；b4096/lr5e-5/单A10080GB最长5.6天，mixed precision未给格式，baseline SAE维度/预算不同。FD50k来自训练activations、低二维PCA和Gaussian moment不能认证alljoint分布；2048 OWT heldout ΔLM loss非任务保留真值。500SAE×5指令/3persona×20题及100 sentimentprefix由LLM评分，C2 1k扩评用sentimentclassifier+同LLM NLL，仍有限fluency/concept代理非relatedcontrol/OOD保证。113test probing有train筛512/val选/neuron搜索成本，1D可分不认证内部causal；loss scaling仅compute-efficient envelope/大steer r≥1，B1 multi-layer更差FD .66 vs .55，不授一切layer/范围无结构假设。20step净推理成本/serving配置CI ND。新增learned-prior局部干预替代可Only，不能仅owner缺此recipe造长期gap；不执行有害persona生成。 root已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [Plato's Form: Toward Backdoor Defense-as-a-Service for LLMs with Prototype Representations](https://arxiv.org/html/2602.06887v1)

[v1](https://arxiv.org/html/2602.06887v1) §3/4.2–5/Alg2–4、§5.1/T2与§6.1–3/T6/AppA必要读。已知base和同架构paired clean/backdoor训练才建离线vectorpool，target w对base而非无先验malicious-only；cosine挑prototype、lower-m均值/方差阈值找boundary，再SVD抑制prototype高投影singularcomponent，不认证其唯一backdoor因果或所有benign留存。Llama3-8B/Mistral7B、五分类+ChatBackdoor；main四attack与AB六口径保留。T2多行ASR>10%，EmotionVPI Llama CDA.949→.861；T6clean.910→.894/.928→.902不是零副作用。adaptive只有限pre-amplification1.2与两个prototype knowledge条件，不认证所有自适应敌手；α>1 utility collapse。离线pool训练+5–10min/model含SVD不free，hardware/precision/训步与净pool/seedCI ND；不按BDaaS名称授生产。具体局部抑制可Only，paired差额不授安全可识别性，不新增Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering](https://arxiv.org/html/2602.06911v1)

[v1](https://arxiv.org/html/2602.06911v1) §3.1–5/4.1–3/5、A2.1/A3/A4/A6.3/A7必要读。新增每model×attack调参后utility约束下最坏harm测量，有限21个.6–8B与五Llama3-8B防御，不是全开权重安全定理。40trial Optuna只fine-tuning，embedding因成本约3A100hours/model未sweep；A7 completion-only/AdamW/BF16/checkpointing/2048，search表HTML字段未展开不补造。utility140 MMLUPro/5shot-CoT且10%相对drop是代理，A4跨16checkpoint与MATH弱相关；10response/condition人审有限，StrongREJECT是convincingness/specificity而非事实正确或真实harm uplift。同一评估上择极值未授独立test/全utility留存；TARuntampered.16vs.44及去utility约束时ReFAT归零直接反侧，不能把低hazard只判强安全。模型family统计差不确定、netcost/seedCI/生产SLO ND。不执行attack/复制payload。具体finite评估反证可Only，不按已有攻击/critic原则造Books新gap。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [Seeing Beyond Redundancy: Task Complexity's Role in Vision Token Specialization in VLLMs](https://arxiv.org/html/2602.06914v1)

[v1](https://arxiv.org/html/2602.06914v1) §3.1–4.2与A5/T1–2必要读。hiddenstate norms/rank、topk5SVD与每位置twohiddenMLP的可恢复性不是执行因果；CLIP后随机删visualtokens，在synthetic count至200时50%删就大退、75%接近零，与多数token count probe好不能合并为‘都可独立供decoder使用’。‘attention specialization’及只改text更佳只是解释/设计推断，未做对应单因素因果训练。Molmo7B-O全模块LoRA16/32，六数据各3epoch/8H100/b32、base5e-5/vision2e-6/proj1e-5，任务输出/保语言captionpopulation不同，不能只归因complexity；GQA row三模型.94/.93/.95都低baseline.97，W2≈chance，不授复杂数据普遍收益。precision/probe完整训练预算/seedCI/净SVD+probecost ND；不给基于norm/rank的通用无损压缩率或新长期guarantee，不改Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models](https://arxiv.org/html/2602.06771v1)

exact-v1 §4.1–2，决定性缓存`feb10_admission_06771_v1.json`。随当前/原concept-center变化做一步AET更新、layerwise parameter penalty与冲突gradient修正，是局部生成模型erasure实现。借用成熟fast adversarial training/PR/投影不计新增分数；接近原θ不证明无关concept保持，retention-data-free只不另取retention集，不等无监督、无重新学习或完整安全保证。完整题摘/身份与实际局部差额1+1+2=4最低关闭Only，不采用安全headline，无新Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models](https://arxiv.org/html/2602.06825v1)

exact-v1 §3/Eq5–6、§4.1–2、§5.4。绝对attention entropy差不是KL；batch median分高低组分8/16，Top4峰branch是局部rollout proxy替换，非budget最优/learning-value定律。作者FLUX配置469→521s/step（+11.1%）、33.5→34.5GB说明entropy处理非免费；不能只写cost ND，更不能把局部收益授净普遍加速。保留1000prompt有限对照，评分1+1+2=4最低关闭Only，不正面采用headline性能，不新增Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping](https://arxiv.org/html/2602.06850v1)

exact-v1 §3.2/Eq2–4/3.3、§4.1–4.3/T1及必要消融。condition-only self-attention改变condition→image反馈依赖，使首步KV可缓存；one-to-one位置对应和keyword阈值.2/前步mask限制interaction，是实际机制变化，而不只是proxy。纠正原1+1+2为2+1+2=5，按标准审阅必要评价直接反侧后Only，不因费时/Only降分。10×16 conditions、attention模块memory不等全模型E2E，PixelPonder因memory排除；SubjectCanny F1 .414<.551、CLIP-T .349<.352，Depth/Multi CLIP-T亦未全面领先，threshold可丢外围条件。one-element softmax非dense等价；CSAS shifted-logitnormal改变采样分布，不授10×/5.1×或任意条件无损。具体局部依赖替代可记录，非owner未写recipe的长期gap，不新增Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks](https://arxiv.org/html/2602.06854v1)

exact-v1 §3.3/Eq8–9/§4.1，必要安全角色定点核。非自适应生成script不读victim回复，但训练阶段真实执行victim与GPT4.1mini judge；intent-alignment×risk/detail reward是具体局部替代，非免反馈训练或独立安全判定。80%AdvBench训练与520主表、159HarmBench评价人口分清。1+1+2=4最低关闭Only，不采ASR安全headline，不执行攻击/复制payload，不新增Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/html/2602.06871v1)

exact-v1 §3.2/Eq4–6/Alg1–2、§4.1–4.5/T1–2与必要直接消融。previous prediction进入forward noise均值，不只是concat，是明确局部生成机制；纠正原4为2+1+2=5，标准完成Only。推理默认每Δ=3帧更新conditioning keyframe，而非每步紧前一帧；Δ=1 ErrAccu .16对Δ=3 .07，Δ=0参考首帧虽.04但TempCon .018对.009，存在取舍。TeacherForcing ErrAccu .06优DiffusionForcing .07而ViDreamSim .38劣.35，不授后者全指标优。ErrAccu相对首帧混合法motion，不认证真实无误差累积或因果推断。SD1.5/SD3.5M、Señorita2M/五编辑、8A100/45k/b8梯累积2/AdamW1e-4；§4.1 val/test15%/5%与5%/15%冲突保留，部分baseline引入原结果。单A100/16帧延迟RAM是有限作者工作点，EVE模型/数据量不同非matchedcompute；不授长视频质量/净总成本恒定，不新增Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models](https://arxiv.org/html/2602.06909v1)

exact-v1 §5.1–2与决定性缓存`feb10_admission_06909_v1_ablation.json`。real+synthetic、leakyTSMixup对74非leakedcase及depth-vs-width是baseline局部设计差额。clean4M对leaky10M同时改变数据量和population，74 clean并未隔离diversity/feature-learning唯一因果；排23测试只消除已知直接leak，不保证全部污染不存在。1+1+2=4最低关闭Only，不计借用成熟更多数据/预算原则，不授controlled-allvariables/SOTA或全部Transformer规律，不因时序应用拒绝模型机制研究，不新增Books。 fresh独立复核者feb10_finite_review（root接受其终裁）已实际核必要原源与直接反侧/关闭依据，通过单项终处置，不新增Books。

### [Decoupling Variance and Scale-Invariant Updates in Adaptive Gradient Descent for Unified Vector and Matrix Optimization](https://arxiv.org/html/2602.06880v1)

[exact-v1](https://arxiv.org/html/2602.06880v1) §3.1–3.3/Alg1–2、§4必要假设/Th4.12/4.15、§5/T2与AppE实际读。新增方差因子与scale-invariant方向分离、矩阵旋转基row/column代理；Kronecker期望分解与稳定eigenbasis条件不能推出实际EMA精确协方差。Alg2末行缺Eq14的回转，不静默修复为已核实现；矩阵smoothness及自适应权重说明亦不直接授praktical有momentum全局收敛。理论只零momentum/unbiased有界variance、batch=T和eta=1/sqrtT。Single A10040GB；NanoGPT T2 loss3.271对Muon3.305但16.49s对10.72s，表头ms/1ktokens与行s矛盾保留，不授端到端更快。主文270/274M、FineWeb-Edu与AppE276M/FineWeb10B口径不同，不合并；AppE b49152/lr.001/WD.1/beta1/2/3=.95/eigenfreq10及warmup60%披露，precision/seedCI/部署SLO/净搜索ND。新增局部优化替代可报告，不为owner未有此配方造长期缺口；理论与伪代码受影响子命题不采用。 root已实际必要原源及直接反侧复核，限定Only终裁通过，无新Books。

### [Vision Transformer Finetuning Benefits from Non-Smooth Components](https://arxiv.org/html/2602.06883v1)

[exact-v1 PDF](https://arxiv.org/pdf/2602.06883v1) §3/4/5.1–2、AppC.1–4与D.2/T6必要部分实际读；HTML不可用后只定点PDF而非52页全遍历。平均输入变化率P(f)是输入敏感度代理，不是参数更新adaptability的因果定理；LN Prop1须同位置跨输入mean/std相同，ImageNet像素归一化不证明embedding后满足。MHA bounded token/image energy与FFN operator norm给上界，不以不同上界大小证明实际P排序。经验12800 pretrain图像对downstream、FC2 zero-pad输入的测量人口与真实中间activation不等；保留有限测量排序。ViTBase86M/224²/11分类，MHA/FC1/FC2各28M可训对LN18K，SGD momentum.9/noWD/cosine/b512/clip1，4LR×3seed、4k–20ksteps，验证选checkpoint后test；不是matchedmemory。T6 GaussianNoise LN2更高，Cifar10/100 FC1更高，Sketch FC2更高，MHA平均与FC1差.07未显著，不能授MHA所有任务最好/低smooth必更好；默认FP32只memory表，实际hardware/全runtime精度/测量+搜索净成本ND。保留局部模块选择证据，不改Books通用适应保证。 root已实际必要原源及直接反侧复核，限定Only终裁通过，无新Books。

### [Prompt Reinjection: Alleviating Prompt Forgetting in Multimodal Diffusion Transformers for Text-to-Image Generation](https://arxiv.org/html/2602.06886v1)

[exact-v1](https://arxiv.org/html/2602.06886v1) §3–5/Eq8–11、§6/T1–7、AppB.2/C/D必要方法/对照实际读。CKNNA/PCA及固定MLP五token类别499train/54test、一次denoise、Adam1e-4/b64/50epoch只测有限recoverability，不证明所有prompt语义丢失或image-only loss唯一因果。等长minimal-pair浅层残差介入支持有限属性传递；LN统计回锚+COCO5K一次SVD Procrustes校准后推理注入，training-free不等无校准/搜索成本。H200，1024²，SD3/3.5分别28steps CFG7，FLUX/Qwen50steps CFG3.5/4；w=.025与origin1/2/2/30由本消融择优，Qwen搜索不充分、SD3.5 target表含origin2的文本边界保留。T2 FLUX PickScore与Qwen CLIP下降，T3 QwenOther下降；w=.1部分大幅退化。T7 SD3每targetblock2.118→2.291ms和rotation8.83%FLOPs不授全模型E2E小开销，FP16/BF16仅memory估算、实际runtimeprecision/batch/多seedCI ND。可报告局部推理干预，不把统计回锚授生成稳定/全信息保持，也不因owner无该配方改书。 root已实际必要原源及直接反侧复核，限定Only终裁通过，无新Books。

### [When RL Meets Adaptive Speculative Training: A Unified Training-Serving System](https://arxiv.org/html/2602.06932v1)

[v1](https://arxiv.org/html/2602.06932v1) §2/Eq1–2、§3.1–3.3/Eq3、§4.1–2、§5.1/§6/T1、AppA1–3与B1–2实际必要读。SGLang验证产生accepted/rejected branches与hidden/logits，经GPU RPC供独立draft learner，再lazy sync；拒绝分支同target分布KL监督不是外部任务真值，正文称reverse KL但写KL(target||draft)的方向命名冲突保留。条件代理accept length不独自授净服务收益：sync48–1600 sweep中频繁同步反降throughput，图注48与正文80最佳口径不合；lookahead5 discard增益小，10仅Llama coding局部。Qwen8B/H100，BF16+FP32、AdamW、b8、最大2048、TTT5；frontier FP8四H200+额外训练GPU，per-request TPS含prompt+output不是aggregate容量/同GPU预算，Qwen BS32反退。A2缓存隐藏态与logit非零内存/传输，topK/32k词表有条件，不授所有backend无改动或atomic hot-swap；40k与表44k、T1 FP8与App表BF16口径保留。SLO/实际同步p99、同成本capacity/seedCI ND。局部shadow learner可行性与服务反侧值得记录，不把缺此recipe当长期gap，不新Books。 root已实际必要原源及直接反侧复核，限定Only终裁通过，无新Books。

### [Endogenous Resistance to Activation Steering in Language Models](https://arxiv.org/html/2602.06941v1)

[v1](https://arxiv.org/html/2602.06941v1) §2.1–3、§3.1–6与AppA3.4–5实际必要读。38 explain-how prompts、过滤约半SAE词表、逐feature/模型阈值及每token持续steer；明确verbal restart由Claude Haiku切段、LLM评分同topic，不认证隐式自纠错或外部真值。26 OTD来自正确/打乱prompt-response差异，约半不符合预期方向；clamp26的局部干预与三组频率/幅度匹配random同prompt/seed控制支持有限因果贡献，不能唯一meta-cognitive机制或免疫证明。Llama70B layer33/SAE50与其他模型设置不同，不归因纯scale。meta-prompt/SFT主要增加尝试频率，条件成功率不提升；uniform10boost与逐feature校准分母不同，强boost退为重复。LoRA32/alpha16/BF16/4epochs、38原题synthetic混比10–90%、checkpoint重校阈值非等原steer量/holdout任务证据，硬件/完整teacher与校准成本ND。保留持续干预下有限恢复与残留偏题，不授SFT提高真实monitoring，局部有限协议Only，不新增Books机制。 root已实际必要原源及直接反侧复核，限定Only终裁通过，无新Books。

### [Agentic Uncertainty Reveals Agentic Overconfidence](https://arxiv.org/html/2602.06948v1)

[v1](https://arxiv.org/html/2602.06948v1) §2.1–2、§3.1–6/T1–2与§5实际必要读。100随机SWE-bench Pro任务，三模型同family solver/uncertainty但不同prompt、mini-swe-agent read-only不看test；pre任务/repo、mid按最终总轨迹25/50/75%选点（不是可上线已知停时）、post已apply patch。成功用benchmark tests，非reviewer自评。有限负侧：pre/post AUROC区间重叠不授普遍前验更佳；中途confidence降不等区分失败。adversarial降confidence的校准和信号须分账：GPT近uniform shift/AUROC不增，Platt的ECE.01未披露独立校准切分不能作为跨任务保证；Gemini/Claude差分两两p=.18/.09不显著。bug-find平均23.4步/.52$ vs12.7/.23$非免费，100中最少22positive、无行为rollout停止/人工路由策略实测。硬件/precision/完整trajectory token-budget及独立seedCI ND；不授去人工/自动accept安全。该有限提示评价反证Only，不造通用自评失效全称或新增Books。 root已实际必要原源及直接反侧复核，限定Only终裁通过，无新Books。


### [ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training](https://arxiv.org/html/2602.06820v1)

[exact-v1](https://arxiv.org/html/2602.06820v1) §4.1–4.2/5.1–5.4/T1–5、AppA/B2/C实际必要源已读。schema/code/tests同生成链，success/rejection检查可修tool或DB；BFS扩依赖并执行、Oracle BoN16估feasibility及LLM过滤不等全部可行路径/独立真值。DB终态规则与动态ID/文字例外为有限可验证task设计，不授生成环境真实正确性。Qwen3-8B/32B、1024/2048 rollout、48steps/lr1e-6，16domain约50tool/5–20tables；AppB2披露每domain约546k、每task93.2k token，不能称零生成/净teacher成本。相同1024task的domain数量比较未配平难度/生成成本；T1 32B Airline48持平，T3去EV也去迭代修复，t-SNE不证明污染排除或独一机制。四次pass不是生产guarantee；hardware/precision/seedCI/净预算ND。局部生成与规则验证取舍可报告，未新增独立执行正确性/长期外部事实机制，Only，不因recipe未列造gap。 root已实际必要原源/反侧复核，仅报告终裁通过；无新Books。

### [POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models](https://arxiv.org/html/2602.06822v1)

[exact-v1](https://arxiv.org/html/2602.06822v1) §3.1–3.4/4–5/T2–7与A1–2实际必要源已读。prefill分R/C/P、decode仅C重选，P永久不恢复；两阶段up/gate再selected-down计算不是免费mask。FFN-only保留attention、较高FFN sparsity对齐总参数；A1混称FLOPs，不能授匹配全部成本。A6000、quality b10 LLM/b1VLM，T5 Llama2-7B128input/128output CUDA event有限E2E：40%时POP2.21s慢于PP2.14；T6全channel重选质量更好但开销更大，γ .1仅所选取舍，2.85%分母是dense FFN非整服务。A2 baseline C4 2k×1024/4096、Týr FineWeb1k×4k，POP无离线校准仍有在线prefill/候选成本；T2/3质量非普保。precision/latency batch/并发SLO/独立seedCI ND，不采摘要1.29×为通用E2E。新增局部三分执行替代可报告，未建立一般后续token安全裁剪/新生产合同，Only无Books。 root已实际必要原源/反侧复核，仅报告终裁通过；无新Books。

### [Improved Sampling Schedules for Discrete Diffusion Models](https://arxiv.org/html/2602.06849v1)

[exact-v1](https://arxiv.org/html/2602.06849v1) §3–5.5/Alg1、A4/A6实际读。采样网格由经验entropy积分/反函数替代uniform；需非负rate与严格增累计，τ-leaping段内rate近似不授任意sampler exactness。uniform有限total-EPR bound与masked奇异分开；A4Eq25是两积分乘积sqrt界，改成积分sqrt(AHna)只称实用proxy，没有推出该更小量仍为严格W1上界，不能采普遍最优transport。NFE不计离线1024时间格×64/1024训练样本校准；主文文本1024sample与A6表64冲突保留。OWT三预训模型1024×1024/GPT2Large生成PPL，EDS在SEDD反差、MDLM64NFE后局部好；无JYS-compatible MDLM/CIFAR参照，不授全SOTA覆盖。硬件/precision/seedCI/校准摊销成本ND。有限schedule替代可报告，不用entropy命名授语义信息/质量普保；无新Books。 root已实际必要原源/反侧复核，仅报告终裁通过；无新Books。

### [Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/html/2602.06869v1)

[exact-v1](https://arxiv.org/html/2602.06869v1) §3/4.1/4.3/5/6及B1–2必要源已读。分布空间KL近端tilt的一阶covariance law与共享θ更新不同；Fisher/natural方向需可逆、positive margin及小步长，clipping需distortion界，简单cov(r,w)不等普通Adam/共享θ无退步。Lemma4.4内积仅≥0未足抵非零二阶误差，不采零margin的有限步guarantee；Th6.5还需boundedscore/non-saturation/token-gradient对齐且μ正，scalarized收敛不保各objective。EMA cov阈值调整lambda是下一步诊断controller非硬约束。Math500三小Qwen、accuracy/clarity二值规则与length代理；4L40/FSDP/vLLM、90epoch/b32/K16/1024in-out/lr1e-6、GRPOclip.2/KL.001，MGDA与Lagrangian KL0不同。B1明确部分baseline accuracy更高，以balanced描述不称全部普胜；precision/独立seedCI/控制器净成本ND，不采negligible证明。只限定理论条件与有限控制替代，不自动新增多目标长期guarantee或recipe gap。 root已实际必要原源/反侧复核，仅报告终裁通过；无新Books。

### [NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices](https://arxiv.org/html/2602.06879v1)

[exact-v1](https://arxiv.org/html/2602.06879v1) §4.1–4.5/T2–7及C/D/T10–11必要源实际读。逐阶段head/dim/SSmerge/staticLN、ResNet T/4 hybrid RoPE/PTD，再以冻结denoiser前三层prompt-state蒸馏T5；superweight解释是假说非因果。训练480k双caption再teacher生成/recaption、多阶段调step4→8→10，不同模型参数与生成步数不是iso-quality/budget；C每阶段80epoch+20E2E、48H100×10h/iteration。PTD全时质量反退，textcodec T6 DPG/Geneval下降与T5多指标低于teacher，OneIG排text/reasoning两项不称完整能力保留。§4.2 block数/原depth文字不一致与主文2.4/结论2.3B保留，不抄广headline。S25U/SM8750Hexagon、512²/10step，T7仅denoise；§4.5另加T5Large15ms与VAE160ms，作者合计估算约2.5s E2E非同条件实测验收；precision/batch/冷启与峰memory/CI ND，非任意手机SLO。新增有限视觉蒸馏/资源工作点可报告，非一般表示同一性/质量守恒，无新Books。 root已实际必要原源/反侧复核，仅报告终裁通过；无新Books。


### [Towards Understanding What State Space Models Learn About Code](https://arxiv.org/html/2602.06774v1)

exact-v1 §3–5/T1/6及AppA4：12层双向S4D的AST/DFG probing、FFT centroid/LHFR是有限表征测量，阈值按所见profiles定；RoCoder末两层不收敛不能当完整因果机制。highfreq CNN k3/group8同时减11层、8/1024kernel同时变capacity，small-data搜索不免费。四A10080GB预训/继续训练与必要配置见[核心笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)；1024kernel SQA76.01低于baseline76.08，precision/完整fine-tune/seedCI/净搜索ND。root实际方法/直接反侧通过5标准Only，有限频率诊断不授所有SSM比Transformer普优或新的长期可靠性合同。

### [Displacement-Resistant Extensions of DPO with Nonconvex $f$-Divergences](https://arxiv.org/html/2602.06788v1)

exact-v1 §3.1–3.2/4/5/T1–2/Limitations及必要AppB：DPO-inducing的continuous/C1正域和边界导数条件不要求convex。Lemma2须unique min c≤1与outside更高reward；min点≥1只抵抗抽象最优点的in-sample退化，不授实际optimizer/winner保持。Llama3-8B/TLDR92.9k、LoRA16/32/.05、lr5e-7/b64/len2048/β.01/4epoch/BF16/4A10040GB；实际exp clip50与无限公式区分，10seed具体角色不额外推定。T1首epoch/T2及STEM直接反侧保留，winner仍下降只更少。root6标准Only通过，不授能力或安全保留，不造配方Books缺口。

### [Optimal Learning-Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay](https://arxiv.org/html/2602.06797v1)

exact-v1 §3.1–3.2/4–6：linear feature/iid one-pass/Gaussian noise/zero-init、hypercontractivity与powerlaw spectrum-target、noise-dominant及小LR稳定条件。Th4.1固定N变分：easy powerdecay、hard prolongedstable+vanishingtail；fractional γ尾与capacity/log边界不把exactshape和optimalrate合并。Th6.3 easy匹配minimax、hard只one-pass SGD最优，非全estimator。硬件/precision/LLM预算对此理论不适用，不据kernel条件发生产schedule。root实际必要条件与直接反侧核后6理论Only通过，未改变真实长期LLM配置判断。

### [On the Non-Identifiability of Steering Vectors in Large Language Models](https://arxiv.org/html/2602.06801v1)

exact-v1 §3–6/8及B2/B3：A3 rank≥k和effective rank小不能保证全部prompt Jacobian共同非零kernel，B2自身还需dimN≥1；random orthogonal于v不等kerJ，lexical相似仅局部代理。B3同时修改下游W的reparameterization不是原固定θ steering vector等价。Qwen2.5-3B/Llama3.1-8B中层、50pair/100heldout×10generation和有限trait/α测量保留为作者经验，不授原Prop1任意α全prompt严格同分布。root实际B2/B3必要源判中心保证Disputed/暂缓，无正面Evidence或Books；不为结束改成经验通过，不遍历无关proof。


### [Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies](https://arxiv.org/html/2602.06575v1)

exact-v1 §3.2–5/T6–8，[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。题摘State-Grounded与HTML Embodied Visual Reasoning题名差异为同一身份，不重计。instruction+proprio查询视觉vote、Gumbel/STE及globalmean context构成局部选择替代；50k步/RTX4090/BF16为作者实际配置，selector平方成本及VRAM略增保留。联合/单条件token保留率不同，不授同预算因果；无globaltoken反退与真实任务preliminary边界保留。root必要方法/反侧核后5标准Only通过，局部配方不新增安全/表示长期判断，无Books写入。

### [Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning](https://arxiv.org/html/2602.06584v1)

exact-v1 §2–4/T1，[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。64latent、16步局部posterior优化、30轮Gibbs-style生成与ELBO拟合后按likelihood选trace，未提供外部真值或独立verifier。0.2B从scratch/385k GSM8K-Aug、借用baseline非本轮同训练，30轮非等推理预算；硬件/精度/全成本ND。清洁近专家示范条件与不授自纠错/全局最优保留；root实际必要源核后6标准Only通过，不造latent配方长期gap。

### [Degradation of Feature Space in Continual Learning](https://arxiv.org/html/2602.06586v1)

exact-v1 III–IV/TI–II，[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。ResNet18/128d与CIFAR10/100的不同epoch/经验划分，IsoScore*或NCI几何读数与accuracy局部解耦；不授唯一因果或全部正则失败，CIFAR100轻改善/不确定性例外保留。batch512/lr.5/buffer200或800及100epoch线性评价不等净成本匹配，hardware/precision/repeat数ND。root方法与直接反侧核后5必要深入Only通过，负结果不因小模型排除，亦不冒充exact-Existing。

### [Echoes as Anchors: Probabilistic Costs and Attention Refocusing in LLM Reasoning](https://arxiv.org/html/2602.06600v1)

exact-v1 §3–4/T1/4/5及必要A4，[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。wrong-prefix paired reminder支持有限恢复，suffix likelihood不等正确性；teacher编辑后175vs136token不等训练预算，DeepSeek GSM8K ED78.2低于普通SFT80.5。EOP probe的first32word/GPT4.1标签与200人审只识别echo，不认证真值/span oracle，attention关联不识别唯一layer原因。root支持/直接反侧核后5必要深入Only通过，不授普遍提升或新增context可信性机制。

### [Trust Regions Sell, But Who's Buying? Overlap Geometry as an Alternative Trust Region for Policy Optimization](https://arxiv.org/html/2602.06627v1)

exact-v1 §2–4/T1–3及必要AppJ，[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。sqrt-ratio局部surrogate以overlap代替常见trust-region罚项，绝对连续/支持重叠、near-q1 Taylor和有限advantage条件不授全局单调或tail保证。MuJoCo/DM九seed与Procgen三seed局部实证；Ant PPO反侧、β过小或大epsilon/LR崩溃保留。MountainCar与Table CartPole身份冲突不静默统一，hardware/precision/fullstep净成本ND；未测LLM不排除优化主线，也不采LLM收益。root必要原源核后5标准Only通过，无Books改写。

### [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625v1)

exact-v1官方题摘/身份与版本说明核验，[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。point/pair跨mode数据与SFT-DPO-GRPO curriculum是局部judge训练替代，4分关闭，不将成熟一致性/正确性原则借分；不采用性能、debiased或遗忘保证。Submitted Feb06 11:35:32Z、registered Feb09 02:46:27Z按本日共同公告包络推定；Jun30 v2窗外，不采后版结论。root v1 AB/身份关闭复核通过，无Books写入或实现验证。

### [AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/html/2602.06485v1)

exact-v1 §2.2–2.4/3.1/3.3–3.5；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。DELLA融合与noise/format/长度过滤不当新原则，固定agent换强summary及summary-SFT、joint task-reward RL支持有限receiver-policy适配，但未独立隔离intent因果。summary不带原问题防代答，另带原问题显著改变任务分工，不能直接比接口收益。SFT8A800/BF16/context128K/4epoch、RL32A800/mixedprecision，train/infer presence参数不同，pass@64付多尝试与oracle选择，不授97%生产成功或edge能力ceil/stability因果；seedCI、完整teacher/训练净成本未充分披露。root实际§2.4/3.3直接原源及反侧终裁5标准Only通过，不是exact-Existing、不新增Books。

### [LIBERO-X: Robustness Litmus for Vision-Language-Action Models](https://arxiv.org/html/2602.06556v1)

exact-v1 III-A/B、IV-A–D/TII–IV与必要AppB/C/D1；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。MuJoCo/Quest3/20Hz、100scene/600task/2520示教；L1–L5累计扰动、模型各自重训预算与成功谓词同时变化，不能独立归因spatial/logic能力或旧benchmark盲区。每任务10rollouts、1.1倍人均期限及更宽期限反侧；OpenVLA/pi0/pi0.5/X/GR00T训练硬件、step、batch/actionchunk不同，未披露precision/重复CI/总成本不补造。AppD1位置/角度代理不等接触稳定与真实安全；TableI自列2026.01非可核首公开。6标准完成，root实际III-B/IV-A/B及直接反侧终裁通过；仅报告有限累计压力测量，不授新的独立能力验收规则、不造Ch26 recipe缺口，未核实现或复现。

### [SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs](https://arxiv.org/html/2602.06566v1)

exact-v1 §3–6/T1–3与必要AppA2/A3/T4；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。IRD先bbox/point再原图+crop读取，Qwen3VL/Molmo2 4/8B、256/512/full、greedy；WBF temp.7/N4/8/IoU.5仍保留非重叠crop并付二次读取成本，Molmo8B full/512负侧不授普遍单调或200倍E2E。实际§6为成功trace筛选后LoRA SFT而非摘要RL，冻结reasoning权重不等输入行为守恒；主文2epoch与T4为5冲突保留，16bit/rank16/alpha32/context2048、单A10080GB Qwen约12h/Molmo约双成本，推理硬件/precision/全成本/seedCI ND。6标准完成，root实际§5/6/T2/3终裁通过；Ch23已有proposal充分性与预算回退，不等此配方实际Existing，局部替代仅报告，不授脑机制因果或exact-KV分布保证。

### [Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks](https://arxiv.org/html/2602.06526v1)

exact-v1 §3.1–3.2/4.1–4.3/5.2、AppI与必要B/E/F/H/J/K；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。25retriever top10池及三LLM预过滤有残余漏标，模型同意/人工分歧升级不授全体自动准确或未来无偏。20/25排名变化与AppI nDCG反侧表明qrel变化不等系统改善，正确生成/旧gold未中亦非参数知识因果。700gold与3657query池分开，Llama3.3-70B/temp0及L40S/BF16，generator版本冲突与人审/全pool成本边界保留，未核实现/复现。6分具体评价身份反证深入；root必要原源、现owner写前及Ch76 L1166/1168、1156–1179邻接与1463末注实际POST通过，锁释放。仅采用judged pool/qrel/Unknown、未标topK补核和归一分母/排名复验，非DREAM标签准确配方或headline推广。

### [World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy](https://arxiv.org/html/2602.06508v1)

exact-v1 §3.1–3.3/4.1–4.5/T1–5及必要A/B；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。joint video/reward MSE不是独立真实observer，第二轮world从ManiSkill初始化、policy从baseSFT起，不授持续online权重演化。23任务/35k轨迹，真实单任务30rollout、reward hacking与>200frame未测保留；H100 node24frames约7s/50updates约30h，precision/nodeGPU数/seedCI/净真实成本ND。root必要方法、T2/3及失效已核，6标准Only；Ch25短horizon/漏洞及真实刷新已有通用分责，非此具体recipe Existing，不造新gap。

### [HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction](https://arxiv.org/html/2602.06527v1)

exact-v1 §3.1–3.3/Eq1–6、4.1–4.5/T2–4与必要AppA/D/E/F/G；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。两遍expert route复用后confidence混logits，clean deterministic prefix KV共享只免K份cache；不授原分布、全memory/latency或Bayes最优。四手工controller/四MoE×八dataset，Ninst与token实际预算不等；硬件/precision/主decode全配置/seed及±定义/E2E成本ND。保留局部错误多数、manual/强制tree反侧而不全proof审阅。root必要方法/KV/预算实源核后6标准Only；有限controller经验不改变Ch79长期预算与verifier责任，不按recipe缺位改书。

### [LogicSkills: A Structured Benchmark for Formal Reasoning in Large Language Models](https://arxiv.org/html/2602.06533v1)

exact-v1 §3–5.3/T1、Limits与AppB/C/D/T3；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。FO2 controlled English/nonce的600/600/300任务，Z3核formal gold/输出不认证原自然语言或内部机制。Llama3.2-3B单epochLoRA100k/100k/200k，validity负迁移及联合训练非同budget；AppD人审五flag/十随机unflag不授全量独立准确率。API Jul–Aug2025，API精确revision/hardware/precision/完整decode/seedCI ND。root实际方法/主要结果/负侧核后5标准Only；保留负面贡献，不授内部没有符号推理或普遍强制形式化。

### [Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study](https://arxiv.org/html/2602.06547v1)

exact-v1 §3.1–3.6/5.4及必要AppA/D/F/J/K；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。库存引号题同family，不重计；98380两community条目是否去重ND，4287 static→762短dynamic→157双作者确认不是全池真值。60s/2GB/fakecredentials与3–5测试输入会漏触发，balanced300五fold不授自然全池precision/recall；147/157removed不等独立因果验证。Ubuntu/Python配置差异保留，未执行攻击、不复制payload/打开攻击附件。root必要漏检、验证与伦理源核后6安全深入Only；Ch72已有观察未命中不等安全，局部测量不造新hard effectgate。

### [Fine-Grained Model Merging via Modular Expert Recombination](https://arxiv.org/html/2602.06552v1)

exact-v1 III-A–D/Eq4–10/Alg1–2、IV-A/C/D/TI/VI/VII及E/F；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。同源component分组/条件8bit、offline NSGAII后先选G，task-router聚同chain batch，非任意输入在线merge。search用validation labels与300real eval×5run，router最多1000/task、30epochs，非无标签/训练免费。单RTXA6000/48GB与有限ViT/LM/PEFT；TI代表Pareto点不是equalstorage/quality，部分G2反侧保留；storage计metadata非峰HBM，完整source/search/router/rebatch/E2E ND。root实际方法/Alg1–2/预算对照核后6标准Only，非Ch30泛component主题Existing，不造recipe gap。

### [SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees](https://arxiv.org/html/2602.06554v1)

exact-v1 §3.1–4.2/Eq3–9、5.1–5.3/T2–5及必要AppA/B Eq24–33；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。逆序teamreward更新及suffix ratio实际共享θ，与独立turn/frozen suffix/accurate advantage理论条件不同，作者Limits亦承认桥梁；Eq8跨turn不同时点ratio不自动等于末态joint suffix。不采实际训练monotonic/global guarantee，无需全proof重读。Qwen14B/AppWorld/BFCLv4、max10turn、b32/roll8/lr1e-6/8H20-96GB与PPO16，相同samples非同GPUtime；precision/seedCI/全decode成本ND，normalization与顺序有限反侧保留。root实际4.1/4.2/Limits和主要配置核后6必要深入经验Only，不把子保证争议改成全family Disputed或新的通用顺序规则；未核实现/复现。

### [JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks](https://arxiv.org/html/2602.06486v1)

exact-v1 §3.1–3.6/Eq3/9–12、§5.1/T3/§5.4/AppG/§7；必要证据见[作者笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。expert skills选择不等LLM checklist确定；Eq9对负权flaw也门控，不授单调sound score。Biz150与180reports/30tasks/6models/5experts人审，GPT5-0807/search/url verifier，三次运行；相关性改善仍约15pp inflation，全验证成本/seedCI ND。root实际方法/负侧人审核后5标准Only通过，不借Ch66主题称具体Existing，不把局部配方缺失变长期gap。

### [Adaptive Uncertainty-Aware Tree Search for Robust Reasoning](https://arxiv.org/html/2602.06493v1)

exact-v1 §4.1–2/§5.1–3/§6.1–3、AppA/B/D/E/T2/F1–3；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。MC-dropout PRM均值/方差筛选与controller分配；Prop4.2的iid无偏bounded posterior不能据dropout满足，同K共同bonus不改变均值排序。MATH500/AIME24、五policy/三PRM、max256/K0=7；A100固定56token/b4生成571ms与PRM32ms的18:1仅局部校准。T2某H-UATS低于DoRA，F1同时改feature/valuation，precision/逐预算CI/全训练成本 ND。root实际必要方法/成本/直接反侧核后6标准Only通过；局部proxy校准未改变Ch79长期预算/真正verifier分责，不造recipe gap。

### [Subgraph Reconstruction Attacks on Graph RAG Deployments with Practical Defenses](https://arxiv.org/html/2602.06495v1)

exact-v1 §3/§5.1–4/§6.1–3/§7.2–3/T3/5与AppB/T7–8/C/T9；[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。库存标题Graphs Don't Stay Secret为同家族，不重计。query-only、已可访问/已知目标身份、一跳typed关系/10query预算不等授权绕过；两5000doc KG、各50个degree≥5目标、四chatmodels，GraphRAG top10、chunk1500/overlap100/context12000/output2048/temp0。T5叠ID+decoy对GPT4mini恢复F1反而增加，Qwen降低，不授单调组合；utility为200合成QA的ROUGE-L，不认证语义/安全。hardware/precision/seedCI/全攻击成本 ND；未执行攻击、不抄prompt。root实际必要安全反侧核后6深入Only通过，不把有限防线配方当Ch72新保密机制。

### [Diffusion-State Policy Optimization for Masked Diffusion Language Models](https://arxiv.org/html/2602.06462v1)

exact-v1 §3/Alg1、§4与A1.1必要条件、§5.1–5.6/Tables1–3及AppB配置；[主机制与评价](../_sources/daily-20260210/feb10_core_06462_v1.json)、[归一化/采样条件](../_sources/daily-20260210/feb10_core_06462_v1_norm.json)。SubmittedFeb06 07:47:22Z、UpdatedFeb09 01:27:53Z、registered02:42:39Z按共同条件包络落窗，右端+1s，不倒填精确public。缓存冻结masked-state原logits、branch只新填位置并一次全填，用同terminal evaluator形成state内相对reward；不是继续原rollout，已有tokens仅context。Exp(Elog) surrogate归一化与mainπold/证明tildeπold、组内baseline条件未桥接，不授实际policygradient无偏或普遍variance保证。更多Z与α并非单调，部分Countdown/GSM反退；同rollout/update非总compute，额外reward/surrogate费用与实际约0.4倍throughput保留，wallclock比较仅Sudoku。LoRA128/alpha64、4H10094GB、batch6accum4、256tokens/AdamW5e-6，任务update3800/5000/7700/6600；主文binary与AppBformat/correct/fractionreward分别保留，seed/precision/完整配置未披露。6=2+2+2，因Ch33完整trajectory至fixed-stateaction对照的具体gap深入，只采用Experimental经验接口。root必要原源/当前owner写前通过，实际Ch33 L2269/2271、前后2258–2277与note2741非作者POST通过，锁释放；未核实现/复现，不授日Gate。

### [BrokenBind: Universal Modality Exploration beyond Dataset Boundaries](https://arxiv.org/html/2602.06451v1)

exact-v1 §3 Eq5–12/Algorithm1、§4.3/Table9及§5必要范围见[缓存](../_sources/daily-20260210/feb10_core_06451_v1.json)。Submitted2026-02-06T07:26:49Z与registered2026-02-09T02:42:23Z依共同条件包络，秒精度右界加1s。D1(a,b)/D2(b,c)只共享pivot，per-batch Moore–Penrose inverse stopgrad且重算，跨modality/data双pseudo-path经Fro约束后进入对比训练；代理不是missing raw truth，矩阵记号/对应batch须实现另核，不授可执行公式、biasfree或数值稳定。冻结encoder下projector线性探测与LoRA、50epochs/前25一致性后25MOX、AdamW5e-4/wd.2均付费；Table9联合训练优于单阶段，收益非MOX独有。隐藏target模态测试mAP（因Recall低改口径）、局部消融/tSNE不授真正缺模态重建或生成质量，text-tactile等稀有切片仍差；hardware/precision/batchrank/独立seedCI/全成本ND，未核实现或复现。5分confirmed onlypivot-gap定点深入，实际Ch23共同English锚/GCPA matchedcorrespondence后L71/73写双代理约束与真实pair/纯map退路，root必要源/owner及L59–83/末注1135 actualPOST通过，锁释放。

### [On the Plasticity and Stability for Post-Training Large Language Models](https://arxiv.org/html/2602.06453v1)

exact-v1 §4.1–4.5 Eq14–16、Theorem5.1及§6.1–6.5必要反侧见[缓存](../_sources/daily-20260210/feb10_core_06453_v1.json)。Submitted2026-02-06T07:31:26Z与registered2026-02-09T02:42:26Z依共同条件包络。Gaussian独立query/isotropicvariance及两梯度误差conditional independence为假设，不由同组采样自证；scalar Gaussian prior下MMSE不是LLM收敛、安全或全能力保持。Eq15在α0只回μpla，却称standard gradient addition；Eq16 MLP错指Eq17，是否保留βgsta与实际variance estimator不明，所引complete AppD在当前HTML/PDF未提供。不能静默补成实施配方。四模型数学/HumanEval、fixedα/all-layer消融与WikiTextPPL只有限支持，不授MLP独占知识/全能力保持或negligible全成本，训练数据/seed/精度/全部成本未充分披露。actualCh33 L137–165 KL分账与Ch27 projection/selector分支核对后，root6分中心争议受影响深入终裁暂缓NoBooks；只重开明确最终更新/variance及必要algorithm配置，未核实现/复现。

### [RelayGen: Intra-Generation Model Switching for Efficient Reasoning](https://arxiv.org/html/2602.06454v1)

exact-v1 §3.2–3.3/4.2–4.3/5.1–5.4/Limits及[AppB/C必要缓存](../_sources/daily-20260210/feb10_core_06454_v1_profile.json)，[主文缓存](../_sources/daily-20260210/feb10_core_06454_v1.json)。Submitted2026-02-06T07:35:01Z与registered2026-02-09T02:42:27Z依共同条件包络。AppB把large模型160条trace输入small估margin，main的高于global均值+1SE与AppB仅mean条件不静默统一。cue后small至sentence-end再回large，thinking终止后small到底；独立engine各用自己的prefix cache补其unseen tokens，不能跨模型复制KV或授target-law exactness。AMC40×4、2A10080GB/vLLM0.13、temp.6/top-p.95/Qwen top-k20/cap32768，latency仅AIME5题×5run，precision/concurrency/SLO/完整成本ND；校准约100分钟不是免费，728答案匹配不证明正确性。all-cue/小模型能力及10/40/160校准规模非单调反侧保留，不采用headline通用加速。root6分标准必要审阅与actualCh56 L262–280、末注1558具体Existing通过：margincue→segment handoff/context与KV identity/nonexact/质量退路正文已承载，不因旧完成标签通过，不新增Books；未核实现/复现。


### [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/html/2602.06443v1)

exact-v1 §3.3/4/5/6.1/6.3–4必要方法、评价及反侧，原[缓存](../_sources/daily-20260210/feb10_core_06443_v1.json)。Submitted2026-02-06T07:13:49Z与registered2026-02-09T02:42:12Z依共同条件包络，秒精度右界加1s，不倒填精确public。AgentBank过滤后34436/37625，强制注入中间错误的索引标签不识别自然轨迹最早因果关键步；63484 balanced pairs/13 tasks，500 audit/100 domain，JEM用exact index与difflib相似阈值，不是语义正确oracle。Qwen3-4B QLoRA8/alpha16、A10080GB、lr2e-5/warm10%，per-task10% split未明确seed-pair隔离，batch/epochs/context/precision/完整cost未披露。Embodied-domain OOD定位退步、50k→60k及8B反侧保留，不采普遍scale或OOD保证。所谓CheckAndAct rollback仅offline评价，没有live environment/外部副作用恢复验证。root5分标准终裁OnlyReport通过；实际Ch80 L137–161的evidence-backed criticalstep→bounded rootcause→repair/state已经有该长期采用接口，本项局部process-supervision数据不授权新增执行机制，不以泛主题Existing强写Books，未核实现/复现。

### [CORE: Comprehensive Ontological Relation Evaluation for Large Language Models](https://arxiv.org/pdf/2602.06446v1)

exact-v1 PDF §3–8及AppA实际必要范围。原§4.3 semantic relation y/ŷ、h与SCR定义同unrelated分母；Table3 accuracy0–41.35%对应错误至少58.65%，§5.3却写meanSCR37.6%，未披露同题letter→relation或不同人口映射。AppA选项置信度是独立0–100 selfreport而非归一logits；原例的broccoli是匹配无关系pair，不是明确None/abstain出口。203题由250中perfect agreement选出、102公开/101blind、人类>1000响应未给每题均衡信息，API推荐确定性与open default/hardware精确配置ND，英文MCQ不能证明结构因果。5分中心争议受影响必要深入，root actual metrics/results/AppA及具体Ch66 confidence owner终裁隔离通过，无正面Existing/Books；未核实现/复现，HTML404后PDF文本足，不授截图visualQA。原指标/提示缓存见[必要raw](../_sources/daily-20260210/feb10_core_06446_v1_conflict.txt)。


### [BenchMarker: An Education-Inspired Toolkit for Highlighting Flaws in Multiple-Choice Benchmarks](https://arxiv.org/html/2602.06221v1)

exact-v1 §3.2/4.3/4.5 Table6/7/8及A4/A5，Submitted2026-02-05T21:57:50Z/registered2026-02-09T02:36:59Z依共同条件包络，原字段已逐项核对，秒精度右界加1s；不充当精确public时刻。GoldenSwag多correct减少但grammar flags增、MMLUPro其它轴及uniqueanswer反退，judge flags非真值；人工人口按初始GPT预测分层抽选不代表全库prevalence。Filtered与同N random100seeds排名差异未matched difficulty，不采纯修复因果；§7主要flag→human/discard而rewrite为局部case，不说完整remediation已实现。A11 contamination映射与主文冲突不采用、不静默更正。5分specific gap深入，root实际Ch66 L423/425及邻接/note4392 POST通过，保留原题/修复版本/人口、人工退路与成本；API默认单run/24h，<8B RTX A6000/更大8×RTX A5000，temperature/precision/fullcost ND，未核实现或复现。必要原raw与具体反侧见[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。


### [Cross-Modal Redundancy and the Geometry of Vision-Language Embeddings](https://arxiv.org/html/2602.06218v1)

exact-v1 §3–6与AppC/E/H/I/J/K必要范围，Submitted2026-02-05T21:56:26Z/registered2026-02-09T02:36:54Z依共同条件包络。Matching image-caption共训SAE/normalized-code cosine软约束与两模态energy ratio mask，不授无配对、可辨trueconcept或无损语义。LAION/COCO mask召回退步与center baseline、β退化、原encoder/reconstruction不同人口及AppK constant projection/排序margin条件保留。6分具体owner差额深入，root必要原源、Ch23 L838/840实际两段/邻接/note974 POST通过；六dualencoders、1M matching LAION/exp8/l0=20，hardware/precision/完整搜索与训练成本/CI ND。未核artifact或复现，不授无条件ranking invariant；详细raw与反侧见[必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。


### [Coupled Local and Global World Models for Efficient First Order RL](https://arxiv.org/html/2602.06219v1)

exact-v1 III-B/E/F、Algorithm1、IV-A–E/TablesI–II与V，Submitted2026-02-05T21:57:41Z/registered2026-02-09T02:36:56Z依共同包络。DMO先前解耦不是本文新数学，diffusion global forward的观测编码处由当前policy刷新local RSSM/reward提供Jacobian，梯度不穿imageencoder；局部reward继承global目标，不授一步accuracy→导数accuracy/真实无偏。Flexiv5/100Hz与Go2 5/50Hz、PushT4h/Cube12hplay+intent，N10/N3和PPO128vsDMO64、宽松criterion分账。6分specific gap深入，root必要源/owner及Ch25新增两段、ensemble/gradient身份邻接及note actualPOST通过，保留shortrollout/真实反馈/simulator/controller；hardware/precision/总offline+refreshcost/seedCI ND，未核artifact或复现，不授safeproxy/总体预算保证。


### [STACodec: Semantic Token Assignment for Balancing Acoustic Fidelity and Semantic Information in Audio Codecs](https://arxiv.org/html/2602.06180v1)

exact-v1 §2.1–2.3 Eq6–14、§3与§4/Tables1–2，Submitted2026-02-05T20:36:24Z/registered2026-02-09T02:36:01Z依共同条件包络，秒精度右界加1s。固定首层离散teacher index不冻结码向量，后续RVQ补残差；SPD在量化前从acoustic encoder预测index并撤去SSL推理路径，不授完全解耦。LibriSpeech960h/50Hz/8×1024、A6000/b32；STA280K与SPD90K+160K非相同总预算，语义约束损部分重建，baseline checkpoint/HASRD口径分开。6分具体gap深入，root源/owner及Ch23分层→混合两段与note actualPOST通过；precision/独立重复统计未披露，未核artifact或复现。

### [Multi-Way Representation Alignment](https://arxiv.org/html/2602.06205v1)

exact-v1 §3–4与AppA1/C1–2/E，Submitted2026-02-05T21:33:45Z/registered2026-02-09T02:36:36Z依共同条件包络。GPA成熟共同坐标与共享row-normalized residualMLP校正分开；soft angular trust不是硬isometry/cycle，PCA丢失不恢复。MASSIVE五seed但表std跨models，TED ordered pairs/noise shuffle与Flickr8k强pivot前提；弱anchor/错对应会强化失配，GPA部分反侧跌幅更小。5分specific gap深入，root source/owner及Ch23 L52–82邻接/末注actualPOST通过，保留GPA/pair/原encoder退路；完整MLP/optimizer/hardware/precision/totalcost ND，未核artifact或复现。

### [Emergent Low-Rank Training Dynamics in MLPs with Smooth Activations](https://arxiv.org/html/2602.06208v1)

exact-v1 Ass3.2–3.4/Theorem3.5、§4–5和AppF1–2，Submitted2026-02-05T21:38:17Z/registered2026-02-09T02:36:40Z依共同条件包络。Whitened、小K/smooth/小semiorth初始化、固定W2/平方loss GD且额外gradient decay/gap条件；block外逐step界不等W1恒rank或任意Transformer保证。初始化gradient/SVD导出窄MLP首尾basis仍可训练，非冻结LoRA。FashionMNIST fullbatch/1500epoch五trial、缩pool VGG16/ImageNethead CE/SGD250epoch/A100；headonly仍差5–10%、4K仍差2–3%、角度失败属局部。5分task-init gap定点深入，root源/owner及Ch30 L110–135正文邻接/末注actualPOST通过；初始梯度/分解/长训练与matchedsearch成本保留，precision/总预算ND，未核artifact或复现。


### [Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO](https://arxiv.org/html/2602.06422v1)

exact-v1 §5.1–5.3/§6.1–6.3与AppB/C/D，Submitted2026-02-06T06:37:10Z/registered2026-02-09T02:41:41Z依共同包络。缓存SDE latent，以ODE completed端点评分差形成increment，在符合sign条件的位置用terminal-minus-prefix替换；AppC只证明selection符号/幅度身份，不授ODE条件均值/unbiased/causal credit。SD3.5M LoRA/512/G24/train10-test40、32H20与reward版本；主表KL及无KL曲线分开，AppD平衡删小magnitude改变人口，window4/噪声过大过小反退。额外ODE/reward与latent预算、700vs2300steps非totalcompute。6分specific gap深入，root必要源/owner与Ch33 L255–274正文邻接、note2711 actualPOST通过；precision/seed/SLO ND，未核artifact或复现。

### [Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization](https://arxiv.org/html/2602.06394v1)

exact-v1 §3.3/§4/Table2及必要C.6–7/G.3/H.1/H.4，Submitted2026-02-06T05:26:59Z/registered2026-02-09T02:41:02Z依共同包络。external quality proxy×频率关联的merge，先PPO候选再Gumbel调参数、最终固定greedyartifact；不把q代理当真实质量，不采globalconv/全LMsubmodular bound，C7本身承认LMloss一般非submodular。作者10runs/CI与Table2局部消融支持通用受限接口，应用指标/科学金融路线不纳Books；rawexposure与steps分开，A100词表50–60GPUh vsCPU BPE分钟、freqtable/模型重训另计。5分具体gap深入，root必要source/owner及Ch11 L85–100正文邻接、note445 actualPOST通过；完整foundation训练配置/precision/seed/SLO ND，未核实现或复现。

### [VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems](https://arxiv.org/html/2602.06409v1)

exact-v1 §3/§4.1–4.3/§5 Tables1–3、必要PDF p12附录尾，Submitted2026-02-06T06:02:57Z/registered2026-02-09T02:41:23Z依共同包络。publicCLIP/T5 surrogate jointcentroid与每轮saliency-guided feature/text编辑，VIP5 frozenT5small/CLIPViTB32+PEFT/三Amazon集；直接改projectedfeature不证明可上传pixel poison。Tab3累计Tab→Img→Txt→interactive未单独控制循环/搜索预算，FID/Rouge/CLIP不授人眼imperceptible或真实consensus因果，ρ提高也可损utility。HTML与exactPDF A1–A5均只有空标题（[必要尾段raw](../_sources/daily-20260210/feb10_core_06409_pdf_appendix_raw.txt)），不能称T5base/defensivefilter已核。6分安全必要深入OnlyReport通过；现Ch72 provenance/sensor责任边界不等该实验具体Existing，不制造成熟原则书段。hardware/precision/seed/searchbudget/SLO ND；未核artifact/复现，不授生产attack或防线保证，材料到达只按§5定点重开。

### [Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding](https://arxiv.org/html/2602.06412v1)

exact-v1 §2 Alg1/Thm1、§3 Tables2–4/§5/AppC/D必要审阅，Submitted2026-02-06T06:08:51Z/registered2026-02-09T02:41:27Z依共同包络。confidence+localKL锁已预测位置，永久停Q/FFN但每层KV仍被读取；active-set文字/算法含糊不采用，A1–4固定row条件界不能外推全网/ARexactness，平均KL不是逐row未来tail。LLaDA8B/Base-Instruct、WikiText/GenPPL与singleturn MTBench/GPT4o，Table2短序列PPL反退、Ng64/B1无runtimegain，packing成本与FLOPs分开。6分specific gap深入，root源/owner与Ch24 L571–589正文邻接、note1816实际POST通过；保留全量/允许reopen回退，hardware/precision/seed/SLO ND，未核artifact/复现。

### [Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters](https://arxiv.org/html/2602.06427v1)

exact-v1 §3–5/Table3与AppC/D/F，Submitted2026-02-06T06:52:23Z/registered2026-02-09T02:41:48Z依共同包络。上游P2P先到近邻，再bbox intent与未来RAFT top10%辅助区域重建、冻结骨干训waypoint；aux decoder训练only删除。Table3保tokens只删aux监督支持局部目标差额，运动幅度非目标salience/causalaction；合成55K streetview轨迹与20K入口标注、A*/MoGe derivedGT非实机transition。两阶段H20预算、lowres/畸变退步与quadruped范围保留，不采A10频率为完整SLO或碰撞保证。5分specific gap深入，root必要源/owner及Ch26 L226–239正文邻接、note1808 actualPOST通过；完整配置/precision/seed/真机trials ND，未核实现或复现。

### [MuCo: Multi-turn Contrastive Learning for Multimodal Embedding Model](https://arxiv.org/pdf/2602.06393v1)

exact-v1 PDF §4.1–4.2/§5.1–5.3与Tables5–7实际必要审阅，Submitted2026-02-06T05:18:33Z/registered2026-02-09T02:41:00Z依共同条件包络落窗。共享一次image编码的causal多轮监督，后turn梯度能回流不等前向读取未来；same-image/augmentation counterpart排除不能自动扩为所有同图答案等价。Table5相关pairs/独立images及negative人口不同，PFLOPs非完整walltime；Table7无mask反退支持局部监督边界。Qwen2VL2B/7B、LoRA64、32A10080GB/global1024/一epoch与合成35Mpairs预算分账，precision/seed/SLO未披露；Table2/正文headline数字冲突不采用。6分具体长期gap深入，root必要原源/owner及Ch23 L509–525正文邻接、末注1093实际POST通过。保留singlepair/heldout与完整成本，未截图视觉核验、代码核验或复现，详见作者必要笔记。

### [Is Gradient Ascent Really Necessary? Memorize to Forget for Machine Unlearning](https://arxiv.org/html/2602.06441v1)

exact-v1 §2.3 Eq4/5/8、§3/α反侧及AppB/C；Submitted2026-02-06T07:11:27Z/registered2026-02-09T02:42:09Z依共同条件包络。仅记录先forgetset memorization并约束θmem retained预测，再θref−α(θmem−θref)编辑的作者局部选择；负taskvector成熟原则不计新增。CE定义logp与正CE证明方向冲突，negativeNPO的lower-bound/目标人口未解析，不能自行修公式；对θmem的条件GD终点不证明θfor保留能力或普遍无collapse。TOFU/MUSE/Phi1.5B/Llama2-7B有限gridα、极端αutility下降、三weights/调参/offload成本保留。原5分安全必要深入不降分，root实际必要源及Ch72 deletion邻段终裁中心隔离，无新Books配方；局部作者实证不是正面安全Evidence，精确重开见§5。

### [Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution](https://arxiv.org/html/2602.06413v1)

exact-v1 §3/§4.4–4.5/§5及AppB.1–B.8必要理论审阅；Submitted06:11:06Z/registered02:41:28Z（Feb06/09）。AppB balanced-prior平均Bayes advantage=TV，strict η<1下指数界条件成立；主文posterior不是同统计量，noise/finitecapacity不自动给该strict contraction，B8模型系数留未来。TextWorld cached相同room/actions模型输出而同时改变reset/edge-dedup controller，未測η或分别控制两项，不证明AR必然cliff/DAG必要。6分中心争议，root actual必要proof/实验及owner通过隔离；Ch79现search/currentstate分工不能承载该必然性，不正面Existing/Books。原字段依共同条件包络落窗，完整反侧及精确重开见作者笔记/§5。

### [TrailBlazer: History-Guided Reinforcement Learning for Black-Box LLM Jailbreaking](https://arxiv.org/html/2602.06440v1)

exact-v1 §3/§4.1–4.2 Tables1–6/limits安全必要深入，Submitted07:11:10Z/registered02:42:08Z。K4/5 history features交attention selector，五mutators与Vicuna cosine reward借既有。四指定11–20B target、A6000；测试统一50target queries/GPT4o10/10，但QPS只成功条件，不含失败/离线训练18K–24K秒/helper或judge总cost；transfer有反例，不授生产攻击概率或全防线无效。Ch72“Safety Evaluation 的单位是 Run，不只是 Prompt”实际history/query-budget/paired-confounding分责已核，无此局部attack实证；仅报告而非泛主题Existing，无Book新增。5分root必要安全/OnlyReport通过，原字段依共同条件包络落窗；[作者必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)保留ND及不采用范围。

### [ReBeCA: Unveiling Interpretable Behavior Hierarchy behind the Iterative Self-Reflection of Language Models with Causal Analysis](https://arxiv.org/html/2602.06373v1)

exact-v1 §3–5及必要配置，Submitted04:00:57Z/registered02:40:32Z（Feb06/09）。随机fold的ICP式mean/variance非外部干预/无confounding证明；50 AIME的2×2 prompting joint均值低于baseline，omnibus非所有pair因果。stage-specific行为提案与单项/联合对照接口可采用，不采用causal hierarchy已识别或普遍收益。2 + 2 + 2 = 6，具体gap深入；root原源/owner及Ch80 L64/66正文、邻接与note358实际POST通过。硬件/temp/outputcap/seed ND，未复现。

以上日期依共同条件包络，原字段秒精度保留；必要配置/反侧见[作者笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)，不授实现复现或日级Gate。

### [Difficulty-Estimated Policy Optimization](https://arxiv.org/html/2602.06375v1)

exact-v1 §3.1–3.2/§4.1–4.3/Table2/Fig7，Submitted04:12:23Z/registered02:40:35Z。warmup后的BERT估Avg@k/PPL再pre-rollout过滤，不等未来group真实零variance；Eq9排序方向/threshold不采用。误拒、陈旧、人口覆盖与estimator/PPL更新成本保留，total125.65 vsGRPO121.85秒不授freeoverhead，等steps非等tokens。Qwen2.5 1.5/7B、16/32H100、Verl/vLLM、G8；precision/seed/cap ND。2 + 1 + 2 = 5，owner gap定点深入；root原源/owner及Ch33 L128/130、note2315实际POST通过。

以上日期依共同条件包络，原字段秒精度保留；必要配置/反侧见[作者笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)，不授实现复现或日级Gate。

### [Uniform Spectral Growth and Convergence of Muon in LoRA-Style Matrix Factorization](https://arxiv.org/html/2602.06385v1)

exact-v1 §4.1/Thm5.7/§6.2/Prop6.7与必要限制，Submitted04:47:06Z/registered02:40:49Z。单矩阵平方loss、smallinit、smoothed连续flow与有限active区间的sqrt谱近unit增长，不是原singularvalue恒速或全LLM离散Muon收敛。factor-norm可能发散、boundedness额外、局部rate需distinct target且已收敛；L2另改目标，过多mode有generalization压力。RoBERTa/1B LoRA只是谱观察，硬件/precision/seed ND。2 + 2 + 2 = 6，specific gap深入；root源/owner及Ch30 L115/117正文、邻接与note756实际POST通过。

以上日期依共同条件包络，原字段秒精度保留；必要配置/反侧见[作者笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)，不授实现复现或日级Gate。

### [Action Hallucination in Generative Visual-Language-Action Models](https://arxiv.org/html/2602.06339v1)

exact-v1 III/IV-A Ass3/9–11/Thm12、IV-B Def13/Thm15、D-A与VI；Submitted03:05:30Z/registered02:39:44Z（Feb06/09）。连续totaldecoder/full-support前提、薄tube density与folding额外条件明确，finite Euler/DDIM非当然可逆、二维proxy非真实robot风险证书；感知/partial observation/stochasticenv excluded，硬件/precision/seed数ND。 原字段依共同条件包络落窗；2 + 2 + 2 = 6，具体owner gap定点深入。root必要源/owner与实际Ch26 L176/178正文/邻接/末注POST通过，未核实现/复现，不授日Gate；[完整必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [FlowConsist: Make Your Flow Consistent with Real Trajectory](https://arxiv.org/html/2602.06346v1)

exact-v1 §3–4 Eq7/10–11、§5 CFG/多样性反侧及AppA/B；Submitted03:24:23Z/registered02:39:53Z。Real F diagonal/fake G自产重加噪角色分开，不重复已有方差项。SiT131M/676M、pretrain/REPA与CFG搜索、aux成本分账，高CFG diversity退步；硬件/precision/seed/SLO ND。 原字段依共同条件包络落窗；2 + 2 + 2 = 6，具体owner gap定点深入。root必要源/owner与实际Ch24 L436/438正文/邻接/末注POST通过，未核实现/复现，不授日Gate；[完整必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [Di3PO - Diptych Diffusion DPO for Targeted Improvements in Image Generation](https://arxiv.org/html/2602.06355v1)

exact-v1 §3.1–3.2/4/5.1–5.2；Submitted03:33:17Z/registered02:40:06Z。Eq4/5梯度精确相消不采用，300pairs/SDXL与SD3文字OCR、Table2背景变化DPO/chosenSFT。2000held-out/4生成/1000bootstrap非4trainingseed，8TPUv4/b16/900steps、teacher与选择成本保留；precision/resolution/SLO ND。 原字段依共同条件包络落窗；2 + 1 + 2 = 5，具体owner gap定点深入。root必要源/owner与实际Ch34 L277/279正文/邻接/末注POST通过，未核实现/复现，不授日Gate；[完整必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass](https://arxiv.org/html/2602.06358v1)

exact-v1 §3–5及AppA/B2/B5–6；Submitted03:40:31Z/registered02:40:10Z。MetaLoRA与generatedadapter身份分开，Qwen3-8B/Meta128/generated8/M148/8A100，合成QA非独立gold；ICL69.4>55.6及多轮/长文退步，不把0.3s局部摊销/FLOPs估算当SLO。offline/online成本与ICL/RAG/SFT退路保留，precision/batch/concurrency/seed ND。 原字段依共同条件包络落窗；2 + 2 + 2 = 6，具体owner gap定点深入。root必要源/owner与实际Ch30 L705/707正文/邻接/末注POST通过，未核实现/复现，不授日Gate；[完整必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [Training Data Selection with Gradient Orthogonality for Efficient Domain Adaptation](https://arxiv.org/html/2602.06359v1)

exact-v1 §3.1–3.5/Alg1/§4与A1–4/B2/D3；Submitted03:41:40Z/registered02:40:12Z。abs-cos容微负/高阶/anchor遗漏，cosine非不等norm下dot最优，rank相关非逐点安全；multi-episode与onepass成本不一致，selection GPUhours非总成本。A10080GB/LoRA16/alpha32/400anchor有限，seed/precision/maxlength/episodebudget ND。 原字段依共同条件包络落窗；2 + 2 + 2 = 6，具体owner gap定点深入。root必要源/owner与实际Ch27 L1029/1031正文/邻接/末注POST通过，未核实现/复现，不授日Gate；[完整必要笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems](https://arxiv.org/html/2602.06319v1)

exact-v1 §2.1–2.3/§3.1–3.3及AppE必要标准审阅；SubmittedFeb06 02:36:15Z、registeredFeb09 02:39:15Z依共同包络。固定80nodes/200edges、node-name扩长控制topology却改变lexical representation，不是纯token长度因果；只在已有正确答案response算outcome efficiency、按行为词与judge标注self-verification，没有stop/intervention因果证明。9任务/2700题及固定图三任务各50原图；每题k8但部分模型k4，temp.6/topp.95/minp0/out32768、boxed exactstring，不能直接跨k比较。Ch66的input scale/graph binding难度轴与长度控制只承载一般协议责任，不是这个具体实测命题，因此root5分标准完成、仅报告通过，不借主题授Existing，不采普遍停止规则。硬件/precision/total成本/SLO未披露，未核代码或复现。

### [Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigating Replay and Context-Binding Failures in AP2](https://arxiv.org/html/2602.06345v1)

exact-v1 §3/§4 Algo1、§5.1/5.3–5.5.3/§6.1–6.4受影响安全深入；SubmittedFeb06 03:22:11Z、registeredFeb09 02:39:52Z依共同包络。可信TCB/keys/strongconsistent SetNX下的nonce/context gate仅作者AP2-style mock，不是锁定正式协议版本的漏洞证明。10kTPS试验仅10秒，TTL30/60/300秒的plateau由有限trace封顶，不能推出peak-concurrency bound；持续state随rate×retention，时钟容差/futuretimestamp与downstream effect exactly-once仍未获证。PythonHTTP→mockbackend平均延迟不授生产安全；硬件/cryptoalgorithm/seed/concurrency/SLO未披露。Ch72已具体区分effect-time authorization、nonce/expiry与exactly-once；新增是局部gate模拟，成熟binding原则不重复写。root4分安全深入、仅报告通过，未核实现/复现，不采用100%安全/内存保证。

### [SOCKET: SOft Collision Kernel EsTimator for Sparse Attention](https://arxiv.org/html/2602.06283v1)

exact-v1 §4/Algo1–3、§5必要假设/Lemma5–6、§6及AppD深入selector gap；SubmittedFeb06 00:41:44Z、UpdatedFeb09 01:12:25Z、registered02:38:25Z按共同包络落窗。Key硬bucket、query软概率，对全部N keys概率聚合×value norm再TopK，只采用graded selection接口不授sublinear；角核/random-sampling理论非practicaldeterministicTopK。Algo3 exp(hashscore)与正文subsetexactsoftmax权重冲突，不静默修正、不采用该子命题。AVG排PassageCount、模型口径及推荐baseline非matchedsearch保留；A100/H200单层b1 decode不是完整LLM E2E，precision/output/concurrency/SLO未披露，建表/metadata/prefill另计。root6分gap深入/owner及实际Ch22 L340/342/末注1276 POST通过，衔接trained selector至层次扫描分支。

### [When Agents Say One Thing and Do Another: Validating Elicited Beliefs from LLMs](https://arxiv.org/html/2602.06286v1)

exact-v1 §3.1–3.2/Prop3.3/Remark3.4/IIA、§4–6与A1必要深入。SubmittedFeb06 00:50:33Z、UpdatedFeb09 01:12:38Z、registered02:38:29Z按共同包络落窗。只在u(a,θ)不含context、exogenous noise条件下用A⊥θ|p作decision-sufficiency否证；pass不证明truth、reject不唯一lying，IIA单调性另假设且方向未知。四有限诊断集、200cases×5、CMI/500bootstrap及OOS效应有small deviations，prompt/persona与utility alternative保留；不是医学部署建议。hardware/precision/deploy配置未披露/不适用，无代码/实验复现。root5分gap深入/owner及Ch66 confidence三层后原L4120/4122两段与末注POST通过；不由统计检验授执行权。

### [Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math](https://arxiv.org/html/2602.06291v1)

exact-v1 §3–5、§6–8/C必要反侧深入。SubmittedFeb06 01:10:28Z、UpdatedFeb09 01:12:53Z、registered02:38:36Z按共同包络落窗。fixed(Q,C) ICL在verified邻题上的utility不是原答案truth/oracle；人工邻域构造/compactreference、solver依赖及easy/hard失辨别保留。samebackbone/64rollout的±15%tokens非严格matchedcost，人口425/630/192口径冲突不合成全量结论；selected112 disagreement、consensus gold与8relative64误差都不授真实概率。输出16k、hardware/precision/deploySLO未披露，v接口未核实现；不采science发现或普遍优于judge。root5分gap深入/owner及Ch66 L1078/1080/5386实际POST通过，activejudge→工作假设迁移utility→panel连续。

### [Can Post-Training Transform LLMs into Causal Reasoners?](https://arxiv.org/abs/2602.06337v1)

作者和root各自实际完整AB；CauGym七任务/五test与SFT/DPO/KTO/PPO/GRPO的定向人口配方比较有局部训练增量，未提供新失效条件或可采用的普遍causal保证，4分后仅报告、不改Books。不是领域/小模型排除；reliable/robust标签不正面采用。SubmittedFeb06 03:03Z、UpdatedFeb09 01:16:47Z、registered02:39:41Z按共同包络落窗，无正文深入声明。

### [Cost-Aware Model Selection for Text Classification: Multi-Objective Trade-offs Between Fine-Tuned Encoders and LLM Prompting in Production](https://arxiv.org/abs/2602.06370v1)

作者和root各自实际完整AB；四固定label benchmarks上的fine-tuned encoder与promptLLM性能/latency/cost、现成Pareto/utility是局部model-choice应用，没有新归因/失效边界。4分仅报告，不给成熟成本权衡添Durability分、不采用headline模型普遍优越，亦不因分类领域关闭。SubmittedFeb06 03:54:28Z、UpdatedFeb09 01:19:37Z、registered02:40:28Z按共同包络落窗。

### [The Condensate Theorem: Transformers are O(n), Not O(n²)](https://arxiv.org/html/2602.06317v1)

exact-v1 §2/Theorem1/Cor2–3、§3、§4、§5/Table4、§6必要配置/OOM、§7–8及CodeAvailability直接反证深入；SubmittedFeb06 02:32:42Z、UpdatedFeb09 01:15:17Z、registered02:39:12Z按共同包络落窗。有限GPT2 greedy1500+token匹配和cosine显示1.000不证明attention vectors数学恒等；mass接近也不等零tail。§4每query全QK O(n)扫描未计入总O(n(W+k))、§7删KV后未来query TopK如何恢复未说明，中心exact/固定support保证隔离。RTX4090Laptop16GB/b1/8heads×64、precision与完整E2E未披露，OOM速度外推/proprietary kernel不正面采用；公开reference不授优化核已核。Ch22 exactdense/changed sparse semantics及selector scan原段已实际对照，但不授争议家族Existing或正面Evidence；root已核有限中心冲突终态，无Books写入。

### [DeDPO: Debiased Direct Preference Optimization for Diffusion Models](https://arxiv.org/html/2602.06195v1)

exact-v1 §4 Eq8/Prop1–2/§4.4、§5.1、§6和supp必要假设深入具体owner差额。SubmittedFeb05 21:11Z、UpdatedFeb09 01:07:16Z、registered02:36:22Z/Available2026-02按共同条件包络落窗。只采用固定θ、同目标人口与代表性标注抽样下，全池pseudo criterion加标注true−pseudo loss residual的期望身份，不授优化后policy无偏；human-biased selection、标签稀少增方差、selftraining违反independent nuisance/crossfit条件均限制接口。原Eq5/18 BCE符号与Eq21导数不一致，未静默改式；网络权重收敛/完整bias-free-training子命题不采用并在§5定点隔离。SD1.5/XL、FiFA5K/HPDv2、25%human、局部automaticproxy实测非独立humanalignment；Table3 Qwen/CLIP反侧、额外forward/残差成本与15 test runs非训练seeds保留。2GPU型号/precision、SDXL完整batch未披露；不采免费收益或fully-labelled upperbound。root5分gap深入/owner及实际Ch34 L241/243与L451末注POST通过，保留原clean-anchor分支/普通DPO回退。

### [Self-Improving World Modelling with Latent Actions](https://arxiv.org/html/2602.06130v1)

exact-v1 §3.1–3.3、§4必要评价/4.5、A4/A7与B1深入具体owner gap。SubmittedFeb05 19:04:41Z、UpdatedFeb09 01:02:31Z、registered02:34:51Z/Available2026-02按共同条件包络落窗。PhaseI冻结IDM，用恢复z的logQ奖励FWM生成可辨transition；PhaseII冻结FWM，用actual后态logP奖励IDM提案，分别recoverability/datafidelity。视觉编辑400K监督warmup、LLM前半带action SFT，只有后段RL丢actionlabel；无标签全生命周期不可采用。CMI下界不识别唯一物理action，ELBO需reference/prior及β1，B1部分实际β.1/迭代VLMβ未另披露，GRPO不授exact coordinate/global上升。T6长horizon N随成功/失败filter、重复迭代/共享weights退步；A4 uniqueness/长度/PPL不排共同rewardhack。Liquid/LLM作者评价是judge/BLEU/BERT/ROUGE而非真实actuator；32/8H200和8GH100、input8126或4096/output4096有限配置，precision/deployconcurrency/SLO未披露，不采headline。root6分gap深入及owner通过；Ch25此前只inverse anti-collapse，实际L260/262新增双反馈/后阶段责任、成本和回退，实际POST通过。

### [Learning Rate Scaling across LoRA Ranks and Transfer to Full Finetuning](https://arxiv.org/html/2602.06204v1)

exact-v1 §3–4、§5关键eval/§6、A2–3/A6及B1–3/B6–8深入具体owner gap。SubmittedFeb05 21:28:59Z、UpdatedFeb09 01:07:59Z、registered02:36:35Z/Available2026-02按共同条件包络落窗。W+αBA的effectiveα不是PEFT lora_alpha/r同名参数，B2 s=αr/use_rsloraFalse；Init[A] α1给η∝n^-1/2 r^-1/2、α1/r rankinvariant；Init[B] α1给n^-1，仅与FFT同阶必要条件，不等有限最优常数可直接迁移。fixedT/single-sample/bounded信号/SignSGD代理与Gaussian独立简化不覆盖完整AdamW轨迹。实测AdamW、seed42、log2 grid的finite趋势，RoBERTa FFT最佳略低、head即使固定1e-3仍可耦合；4H200/BF16/TF32，Tulu1024 b32/OpenThoughts8192 b8等task合同分别保留，不采用A6000实测或训练倍数。root5分gap深入及owner通过；Ch30原matchedsearch一般公平段未承载具体scaling/necessarytransfer，实际L111/113窄写并保留独立sweep/回退，实际POST通过。

### [Is my model "mind blurting"? Interpreting the dynamics of reasoning tokens with Recurrence Quantification Analysis (RQA)](https://arxiv.org/abs/2602.06266v1)

完整官方AB与身份已实际核，root独立完整AB关闭校准通过。3600条R1-distill hidden traces的recurrence/laminarity只作complexity诊断，未给可执行stop/budget校准；新增局部proxy3分后不进一步采用，不因模型规模排除。Books仅报告，无长期策略增量；原Submitted23:48:23Z与Feb09 registered02:38:01Z满足下述条件日期包络，精确字段保留原缓存，无正文深入或实验复现声明。

### [RoPE-LIME: RoPE-Space Locality + Sparse-K Sampling for Efficient LLM Attribution](https://arxiv.org/abs/2602.06275v1)

完整官方AB与身份已实际核，root独立完整AB关闭校准通过。固定closed-model output、open surrogate RoPE locality/NLL fitting和SparseK有局部替代，但没有closed-model faithfulness新边界；4分后仅报告、不新增Books，不能把替身表现当closed模型归因真值。Feb06 Submitted00:26:14Z与Feb09 registered02:38:14Z满足下述条件日期包络，字段保留，不称读过完整正文。

### [Accelerating Vision Transformers on Brain Processing Unit](https://arxiv.org/abs/2602.06300v1)

各自完整官方题摘已实际读，root独立完整AB校准通过；身份/原Submitted与registered见[原字段](../_sources/daily-20260210/feb10_all_selected_date_raw.json)，分别为Feb05 23:48:23Z/Feb09 02:38:01Z、Feb06 00:26:14Z/Feb09 02:38:14Z、Feb06 01:48:54Z/Feb09 02:38:48Z，均满足下述条件包络；原题摘位置在[170逐身份筛选](../_sources/daily-20260210/feb10_v3_screening.md)。RQA只是3600条R1-distill traces上的complexity proxy及预测，未建立stop/budget可靠门槛；RoPE-LIME提出替代locality与NLL fitting，但不由open surrogate结果证明closed model因果归因；BPU固定weight的linear/LN→conv体现既有器件lowering，不能从受测数字添加通用编译保证。这些具体增量评分3/4/4后不进一步采用，无未处理安全/纠错信号；不是以小模型、视觉或未测LLM端到端排除，没有宣称全文审阅或否定学术价值。Books均仅报告，局部配方未改变长期owner论点。

以下arXiv采用相同的**条件日期推定**而非精确公开时刻：正常Submitted不早于2026-02-05T19:00:00Z、最早可能公告2026-02-09T01:00:00Z，ID不提前生成、每ID原registered存在上界且无更早同正文公开信号。Available只有月，Updated不独立证明first-public；右端原registered+1秒仅保守包络秒精度上界。[逐ID原字段](../_sources/daily-20260210/feb10_all_selected_date_raw.json)和[官方排程](../_sources/daily-20260210/feb10_policy_monthly_raw.txt)保留，不倒填Submitted为公开。各项完整必要配置/反侧见[作者核心笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)，不代表实现或实验复现。

### [MoSE: Mixture of Slimmable Experts for Efficient and Adaptive Language Models](https://arxiv.org/html/2602.06154v1)

采用exact-v1 §2.2–2.4、§3必要对照/transfer、§5及A1。Submitted19:48:41Z、Updated01:04:34Z、registered02:35:25Z（Feb05/Feb09），Available2026-02。前向全宽+随机宽的双loss使同expert上投影列/下投影行共享prefix；概率幂映射、clip及.05离散后不保证严格总额度。γ对各额度在OWT有限50batch校准后冻结，未充分披露离散切片梯度，不能授实现已核。GPT2 55M/322M/1B、OWT3–15Btokens、4A100 DDP，只支持局部质量—MFLOPs；transfer有退步，不授真实latency、任意posttraining弹性或未来Agent应用。root核5分标准及owner差额，实际Ch21 L257/259把nested prefix与既有异宽group/elasticpath衔接，双forward与欠训练及固定宽回退近正文，实际POST通过。

### [Stop the Flip-Flop: Context-Preserving Verification for Fast Revocable Diffusion Decoding](https://arxiv.org/html/2602.06161v1)

exact-v1 §5.1–5.3、AppB.1–4、§6.1/6.4/6.5必要深入。Submitted19:58:48Z、Updated01:05:00Z、registered02:35:35Z（Feb05/Feb09），Available2026-02。其他query读取前步seed KV，而seed验证恢复自身mask diagonal；AppB固定Q/off-diagonal单row的减旧、加新和renormalize精确，不支持全网causal leave-one-out、零间接leak或AR distribution exactness。keep/replace/remask及seed不连续验证维护不同状态；选择与drift Spearman只是代理。KV消融同时删两机制，remask ratio分母也与其他baseline不同，不能单独归因。LLaDA/Dream、4H200、greedy/temp0、block64、输出256/512有限作者结果，concurrency/SLO未披露，不采用headline速度。root6分必要深入及owner通过；Ch24原Self-revision已有provisional/revision预算却无两视图局部校正，实际L569/571窄写，POST通过。

### [Uncertainty Drives Social Bias Changes in Quantized Large Language Models](https://arxiv.org/html/2602.06181v1)

当前官方exact-v1题名不同于原DataCite旧标题，同ID/作者/Submitted；旧字段不覆盖。Submitted20:37:26Z、Updated01:06:11Z、registered02:36:02Z（Feb05/Feb09），Available2026-02。§3.2–3.4/4.5/A6的安全评价必要深入：十模型五PTQ、13英语datasets，closed length-normalized likelihood/open greedy，paired1000次permutation/bootstrap及FDR.05；aggregate抵消并非逐例/子群无变化。单人盲标400且按detected-change分层，Guard PPV/NPV只该人口，不由paired形式授judge误差全相消。Qwen.5B/selectedBBQ的SimPO/EntropyMax同时改变weights/preferences，非唯一entropy cause。vLLM/L40S或H100、输入4096、输出512或每turn150，batch/concurrency/SLO未披露，不采用吞吐或通用安全bit策略。root核5分必要安全深入；Ch49实际“量化验收不能只看平均分：逐例一致性与分布漂移”已完整承载aggregate→perexample→drift/slice与artifact/evaluator身份，新增实测不提供更强precision策略，具体已有覆盖通过、无Books新写。

### [To 2:4 Sparsity and Beyond: Neuron-level Activation Function to Accelerate LLM Pre-Training](https://arxiv.org/html/2602.06183v1)

exact-v1 §3/Algorithms1–3、§3.2/§4/§5.1–5.2关键表与反侧标准审阅。Submitted20:43:24Z、Updated01:06:30Z、registered02:36:05Z（Feb05/Feb09），Available2026-02。SquaredReLU与weight2:4/activation Venom分工覆盖六FFN GEMM，cluster→tokenrouter→row permutation为物理pattern，不等optimizer拓扑身份；距离文字/伪码差额不授代码已核。LLaMA3-1B/7B、DCLM/H200，dense1000warmup后sparse→dense恢复，model-specific预算且激进sparse退步；最近100步平均loss/无多seed不确定性不授无损。headline只是FLOPs/roofline+微核估算，非实测training E2E，布局成本和假定comm overlap需另计，Blackwell优化未实测。root6分标准及owner通过；Ch28 L289/291把该分支接现有DynamicSparsity后，区分physicalpattern与optimizer-state、恢复和总成本，实际POST通过。

### [Compressing LLMs with MoP: Mixture of Pruners](https://arxiv.org/html/2602.06127v1)

精确v1原日期：Submitted `2026-02-05T19:01:06Z`，Available仅月 `2026-02`，Updated `2026-02-09T01:02:09Z`，registered `2026-02-09T02:34:47Z`。Submitted不等公开；它晚于Thu14EST截止点，官方排程的最早可能公告为SunFeb08 20EST（Feb09 01Z/09BJT）。结合ID不提前生成及原registered存在上界，且当前未见更早同正文公开信号，形成完全落窗的条件范围；右端加1秒只是将原秒精度上界保守包成不含终点范围，不补造公开时刻。[原字段](../_sources/daily-20260210/feb10_all_selected_date_raw.json)与[官方排程raw](../_sources/daily-20260210/feb10_policy_monthly_raw.txt)保留条件及精度。

实际标准审阅[exact-v1缓存](../_sources/daily-20260210/feb10_core_06127_v1.json)§3.2–3.3、§4.1–4.4及关键表/反侧。每步先选一层并重算其当前参数数，width分支匹配相同删除预算；proxy分支可以短LoRA后评分，却丢弃短更新，保留相应剪枝模型，最后才完整恢复。末两层保护及AMP head/neuron评分借自既有方法，不计新增。关键§4.1.1/Table1的PPL60.84与random60.83±0.43相近，后续实际用random；Figure2同pipeline混合胜单轴支持的是联合结构空间，而不是复杂选择器优越。三条seed和跨论文预算不构成稳健性定理或严格matched排名。

LLaMA7B仅校准，文本LLaMA2-7B/3-8B及LLaVA1.5-7B；Alpaca恢复有明确额外预算。§4.3 RTX4090/LLaMA2-7B、12输入/128输出、batch1，20次弃10预热、余10墙钟；precision、concurrency、SLO Not Disclosed。只支持受测压缩档延迟，不采用39%通用承诺；多模态恢复仍有能力下降。未核代码或复现实验，完整条件见[必要审阅笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

Ch49具体稀疏段已有mask目标、保护集与kernel admission，却未承载深宽等参数预算与random≈proxy反侧。root已核必要原文及5分标准/owner差额；实际在“两个稀疏性”之前写两段，区分质量改变的结构压缩与无损图优化、搜索/恢复/执行成本，保留single-axis与dense回退，Review notes同步原源。root实际正文L467–469及前后邻接写后复核通过；这是该家族整合完成，不授全日Books或Gate通过。

### [Kimi CLI 1.10.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.10.0)

官方 release API 原字段 `published_at=2026-02-09T15:03:56Z`，换算北京时间23:03:56，完全落窗。5分标准审阅后因兼容/执行边界定点加深；采用精确 tag1.10.0 的 Changelog，并读相关 PR1039、1065 的实际变更，不是泛审整个版本。原记录：[100 release API](../_sources/daily-20260210/feb10_scope_recovery_0.txt)、[Changelog](../_sources/daily-20260210/feb10_core_initial_1.txt)、[PR1039文件](../_sources/daily-20260210/feb10_date_initial_0.json)、[PR1065文件](../_sources/daily-20260210/feb10_date_core_2.json)。

PR1039 `src/kimi_cli/web/runner/worker.py` 读取全局 MCP JSON，传入 `KimiCLI.create(session,mcp_configs=...)`；JSON 错误记录 warning，MCPConfigError 后回退无显式配置。它修正 Web/CLI 能力配置路径，并可能改变可用工具集合；不是将动作执行权限转移给浏览器，回退也不是验证全部工具安全。

PR1065 `chat-workspace-container.tsx` 仅在前一状态 streaming/submitted/error 转 ready 且队列非空时消费文本。切 selectedSessionId 清队列的 effect 明确先于自动发送 effect；处理中附件不加入队列。`queue-store.ts` 是内存 Zustand FIFO，可编辑/移动/移除，item带UUID；没有持久后端或跨session保留保证。对此不能宣称 durable exactly-once、排队后的授权仍有效或任务完成；这是静态分支核验，未运行浏览器或复现生产流程。

对照具体 owner：[AGENT-MCP，第83章](../../../../books/part-07-agent/83-mcp.md)“协议比较必须拆开五类契约”当前L104–108、“MCP 不等于 Tool Authorization”L167–169已明确 backend 等价性、principal/policy与effect commit分责；[AGENT-PLATFORM，第84章](../../../../books/part-07-agent/84-agent-platform.md)“Serving 结束不等于 Agent 任务结束”当前L88–94已有 runtime/工具真实副作用、Thread/Turn/Item、断线回读与session/run身份区别。本次新增是版本特定的 Web 配置与界面输入状态修正，未证明新的持久任务协议或可靠性条件，因此仅报告、不改 Books。不是把“主题已有”当作准入排除。


### [Latent Structure Emergence in Diffusion Models via Confidence-Based Filtering](https://arxiv.org/html/2602.06155v1)

标准5分审阅，root实际必要原文与Ch24 prior/preview owner核通过，仅报告。[方法及前段评价raw](../_sources/daily-20260210/feb10_decisive_06155_v1.json)、[§5.3/6剩余必要评价](../_sources/daily-20260210/feb10_core_06155_v1_remaining.json)、[AppE必要diversity对象](../_sources/daily-20260210/feb10_core_06155_v1_diversity.json)。确定性DDIM的seed→image先由LeNet h赋label/confidence，再学seed proxy g，在denoise前按目标类别/置信度选seed；这不同于生成后filter，但不是独立语义真值。70k Gaussian seeds经h平衡到35160，fresh5100仍由同LeNet验证；53.42% high-confidence与20.31% unconditional属于不同选择人口，9维监督LDA/UMAP也不证自然可辨语义。DDPM没有同样清晰结构，局部Lipschitz流论证不授有限DDIM普遍可逆；confidence logits/probability文字口径不静默修。AppE每类10张、CFG3视觉比较不证明定量diversity；训练生成/搜索预算、hardware、precision和净latency成本 Not Disclosed，未复现。Ch24现prior steering及低分辨率preview筛seed与此proxy分支不完全相同，故不称泛Existing；局部classifier-defined目标/条件人口尚不足新增长期结论。

原Submitted `2026-02-05T19:48:50Z`、Updated `2026-02-09T01:04:35Z`、registered `2026-02-09T02:35:26Z`；采用正常ID条件排程下界与registered+1s保守上界，Updated不独立证明first-public，非精确公开时刻。

### [Refining the Information Bottleneck via Adversarial Information Separation](https://arxiv.org/html/2602.06549v1)

标准5分审阅，root实际§3.3–3.4、§4.1–4.4与Ch5 owner核通过，仅报告。[通用方法/评价/理想条件raw](../_sources/daily-20260210/feb10_core_06549_v1_generic.json)、[AppC1–4配置](../_sources/daily-20260210/feb10_core_06549_v1_configuration.json)。撤销materials/AI4Science标签排除：这是一般task/noise表示分解与跨层回收机制，不采用科学应用§4.5。无需separation labels不等无target监督；noise仍可含有用微弱信号及spurious项，joint-vs-shuffled WGAN-GP有限critic不授实际严格独立/纯语义分离，strictgain另需首层遗漏、后层capacity与理想优化条件。

十seed局部结果有得有失：CIFAR Joint在N100/200/300为.280/.321/.361，高于InfoR的.262/.320/.357；TwoStage在N200/300也更高，N100相等；只有N500/1000两variant均低于InfoR。此前作者ready笔记“全部低于InfoR”错误已纠正，不沿用该全负侧。AEP70% Joint .597低于VIB .604、Concrete500两variant低于VIB/InfoR及λ>1退步仍保留；不是普适负面或优势。Synthetic是Gaussian s13经随机MLP划分dominant/subtle信号，再随机线性mix，没有独立noise-shift协议；two-stage先40%冻结后层再冻结前层，critic次数/随机KLcoeff也改变recipe，不授唯一机制因果。hardware、precision与完整净成本 Not Disclosed，未核artifact/复现。Ch5目标相关invariance/shift论点不等此局部recipe，但当前证据不足修改长期结论；不以主题记Existing，不强写Ch23或科学路线。

原Submitted `2026-02-06T09:54:47Z`、Updated `2026-02-09T01:33:21Z`、registered `2026-02-09T02:44:41Z`；采用同正常ID条件下界与registered+1s保守秒包络，不倒填精确first-public。

### [Improve Large Language Model Systems with User Logs](https://arxiv.org/html/2602.06470v1)

5分标准起点，因采用具体分流机制定点深入；必要§3.1–3.6、Alg1、§4.1/4.3/5.1–2已审，原源为[规则及gap](../_sources/daily-20260210/feb10_decisive_06470_v1.json)、[分流和checkpoint](../_sources/daily-20260210/feb10_decisive_06470_v1_route.json)、[关键评价与反侧](../_sources/daily-20260210/feb10_core_06470_v1_evaluation.json)。低gap经验尝试Expert DPO+NLL，经预设模拟评价选checkpoint；失败或高gap则训练Critic，由base初答、Critic反馈、base重答，outlier回base。采用的是固化经验失败的反馈者回退分支，不采用noise真值、Bayes普遍保证或安全发布许可；Ward方差增量不是固定cluster直径。LongLong预筛recall为零，减少DPO训练数据不等总成本下降，完整UNO增加调用，不能借UNO-Single输入token图说明全路径省成本。模拟用户日志/base judge三次/BLEU过滤限定评价人口；hardware、precision及全部成本未披露，未核实现或复现。root核必要原源与具体owner后，实际Ch77两段及末注写后复核通过；不是因旧owner未写某配方自动认定长期缺口。

原Submitted `2026-02-06T07:55:26Z`、Updated `2026-02-09T01:28:14Z`、registered `2026-02-09T02:42:50Z`，见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)；公开范围按正常ID排程下界与registered+1s包络，不倒填精确时刻。

### [Provably avoiding over-optimization in Direct Preference Optimization without knowing the data distribution](https://arxiv.org/html/2602.06239v1)

6分标准起点，因采用受限聚合条件定点深入；必要§3/Alg1–2、有限§4/Lem4.2–4、§5/Tables1–2及AppA1.1–2/4–5见[方法](../_sources/daily-20260210/feb10_core_06239_v1_method.json)、[理论条件、实现近似和反侧](../_sources/daily-20260210/feb10_core_06239_v1_necessary.json)。二元BT两方向和为一，不能同时下估；tie mass、disjoint pair subsets及whole-response policy minimum构成受限保守聚合。保证依赖有限support、有界reward/log-ratio、BT人口、ensemble大小与有效tie upper bound，不适用于任意未知生成分布。AppA1.4明确token规则不继承response理论；局部normalize不授whole-trajectory exact tilt。完整response rejection可零接受，16次截断及mean/std变体改变交付目标；共享base仍有多adapter前向，局部1/4时间不是总GPU-hours节省，L>3 toy反退保留。UltraFeedback多generator、AlpacaEval805及Llama70B judge，LoRA16/alpha16/BF16/AdamW1e-5/seed42、GH200与A100；完整端到端成本和生产SLO未披露，未核代码或复现。root核必要原源、具体owner后，实际Ch34两段和末注写后复核通过，不采普遍免overoptimization或token exact保证。

原Submitted `2026-02-05T22:31:07Z`、Updated `2026-02-09T01:09:53Z`、registered `2026-02-09T02:37:24Z`；采用正常ID条件排程下界与registered+1s包络。

### [REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop](https://arxiv.org/html/2602.06248v1)

5分安全必要深入，root实际核§3/4.1–4.2与AppE Sample50后仅报告通过；[方法](../_sources/daily-20260210/feb10_core_06248_v1_method.json)、[评价、预算与误判反侧](../_sources/daily-20260210/feb10_core_06248_v1_evaluation.json)保留。benign proxy与relearning不能排序该局部adaptive recoverability，但known hidden answer、Qwen7B hacker/judge、TOFU1B与WMDP8B人口，以及logits和generation权限限制结论。最多4220候选与Leak1000并非matched budget，AppE未知虚构书本被judge判泄漏，不能将qualitative“noFP”推成总体零误判。hardware、precision、target完整解码、手工审计分母和完整成本未披露，未运行实现。Ch72实际suppression/erasure、有限observer及搜索访问/预算论点与此有限测试共同支持不授擦除证书，但不称该recipe已完整覆盖；未新增防御机制或长期保证，故不改Books。

原Submitted `2026-02-05T22:54:56Z`、registered `2026-02-09T02:37:36Z`；采用正常ID条件下界与registered+1s包络。

### [Steering Safely or Off a Cliff? Rethinking Specificity and Robustness in Inference-Time Interventions](https://arxiv.org/html/2602.06256v1)

6分安全必要深入，root实际§3/5/Table2、§4/6/AppC原源与Ch31 actuator邻接核通过，实际L502/504两段、末注1252写后通过；[方法](../_sources/daily-20260210/feb10_core_06256_v1_method.json)、[控制对照](../_sources/daily-20260210/feb10_core_06256_v1_baselines.json)、[评价与配置](../_sources/daily-20260210/feb10_core_06256_v1_evaluation.json)。只采用target/相关control-ID/同control-shifted三分，不由一般MMLU/fluency回归认证控制稳定。Table2 safety为1−HarmScore，headline相对下降非pp；PCA只是单模型层的关联，不授通用因果。四models/五methods/三runs、256训练/100验证、500test与25静态prefix×100harmful；RTX2080各15GPUh，precision、完整解码及全成本未披露，未运行代码或复现。

### [D-Legion: A Scalable Many-Core Architecture for Accelerating Matrix Multiplication in Quantized LLMs](https://arxiv.org/html/2602.06252v1)

5分标准完成，root实际III/IV/V-A与V-C必要源和同PE反侧核后仅报告；[方法](../_sources/daily-20260210/feb10_core_06252_v1_method.json)、[评价与限制](../_sources/daily-20260210/feb10_core_06252_v1_necessary.json)、[完整已读笔记](../_sources/daily-20260210/feb10_ready_06252_06258.md)。小core沿K分块、spatial psum reducer和KV multicast不取消temporal RMW或生成依赖；大core在attention-score shape反而更快。cycle simulator非silicon测量，headline与较少PE基线资源不等，同PE对照psum流量也非一律更少；面积/功耗、量化质量、全生成延迟与SLO未披露。Ch49 phase×shape可解释但非具体微架构全覆盖；局部simulator不足改长期布局选择，未写Books或复现。

### [GRP-Obliteration: Unaligning LLMs With a Single Unlabeled Prompt](https://arxiv.org/html/2602.06258v1)

5分安全必要深入，root实际§3.1/3.3、AppA/Table1逐能力反侧核后仅报告；[方法](../_sources/daily-20260210/feb10_core_06258_v1_method.json)、[必要评价](../_sources/daily-20260210/feb10_core_06258_v1_necessary.json)。prompt本身故意有害且reward不安全；一个prompt重复rollouts非一条样本或免成本，六benchmark utility平均不保每项能力。15models有限实验、家族特定LR/KL/earlystop与不同judge不能合并为普遍安全退化；外部攻击对照预算未匹配，PCA干预只局部refusal-subspace诊断。hardware、precision、全部训练成本与seed不确定性未披露，未执行不安全训练或复现。Ch72 revision/复验/回退并非该recipe全覆盖，此局部攻击证据无新防御或安全合同，不改Books。

### [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/html/2602.06521v1)

5分标准完成，root核§3.3/Eq10–12与§4/Tables4–7后仅报告；[已读方法](../_sources/daily-20260210/feb10_admission_06521_v1.json)、[动作评价proxy](../_sources/daily-20260210/feb10_admission_06521_refinement_v1.json)，评价本轮直接读官方精确HTML。双BEV分支和simulator监督reward权重action-head，不授想象一致即物理正确。stage3的短时open-loop收益很小，各bench的baseline/reward不同；Table7实际inference加噪而非训练loss删除，不能隔离feature监督因果。8H20两套训练配置与120/93h分开，precision、seed不确定性及全部推理成本未披露。Ch25 transition/score/真实反馈分责不等该recipe全覆盖；局部proxy不足改变长期控制判断，未写Books或复现。

### [AgentCPM-Report: Interleaving Drafting and Deepening for Open-Ended Deep Research](https://arxiv.org/html/2602.06540v1)

5分标准完成，root核§2.3.1/Table1、§3.3.4/Table5、AppA6.1decision与B1必要源后仅报告；[方法与停止监督](../_sources/daily-20260210/feb10_admission_06540_v1.json)，评价本轮直接读官方精确HTML。teacher强制扩展后judge选最高分draft截断并重标Terminate，匹配reference的0/1决策奖励不是客观信息饱和。same-teacher pruned/raw对照支持局部质量收益，监督tokens与完整teacher/search成本不相同；forced15曲线不默改部署cap12。MiniCPM8B/8A100、SFT/atomic/pipeline分阶段训练，precision、重复运行不确定性与净成本未披露。Ch29监督与Ch79预算不能泛称此recipe已有覆盖；局部judge-defined标签不授通用最优停止，不写Books或复现。

### [Code vs Serialized AST Inputs for LLM-Based Code Summarization: An Empirical Study](https://arxiv.org/html/2602.06671v1)

exact-v1 §4.1/§5.1–2/T3–4/§5.4。SubmittedFeb06 12:55:01Z、registeredFeb09 02:47:31Z按共同条件包络，右端秒精度加1s。Python CodeXGLUE清洗30227/2771/3097、Llama3.1-8BInstruct4bit、LoRA16/alpha16/.05、AdamW8bit/lr5e-5、3epochs/window5000、单A6000/beam4。NIT比SBT短且近同quality，但rawCode更短而quality相当，preorder丢lexical最差；同epoch不等总tokens/walltime，pretraining重叠未排除，preprocess/inference/seedCI ND。root实际必要方法与raw/SBT/NIT直接反侧复核通过5标准OnlyReport；局部负侧未形成通用结构规则，不因小模型关闭，也不借Ch74信任结构主题记Existing或造gap。

### [FCDP: Fully Cached Data Parallel for Communication-Avoiding Large-Scale Training](https://arxiv.org/html/2602.06499v1)

exact-v1 IV-C–E/Alg1、V-A–E/T4–7与VI-A；SubmittedFeb06 08:52:06Z、registeredFeb09 02:43:31Z按共同条件。forward inter-AG后host cache，backward本地node shard/intra-AG；trainable更新dirty、frozen clean一次AG，阈值placement/NUMA pinned/stream与gradient RS另计。4node×8A40/48GB、双EPYC/512GB/100GbpsEDR、pairNVLink/PCIe4、DS.16.2/Torch2.3，GPT2XL衍生10–30B/SQuAD，FP16activation/gradient+FP32master。microbatch8与maxbatch、2node LoRA r8分别报告，不混用motivation BF16；seq/quality/全训练及恢复成本、seedCI ND。root实际核关键机制/配置及Ch39 L263–269：per-node完整generation、activeGPU shard、optimizer/gradient ownership/prefetch可见性与DRAM/NUMA/PCIe/coherence代价和同SF/条件已具体承载。6标准Existing通过，不重复加dirty recipe；不授实际HBM恰好W/G或带宽不敏感保证。

### [DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving](https://arxiv.org/html/2602.06502v1)

exact-v1 §2.3/§3.2–3.4/§4.1–4.3、A1.2/A2.1–3/A3；SubmittedFeb06 08:53:29Z、registeredFeb09 02:43:35Z按共同条件。hotness prefix key延伸/合并后固定双候选，SLO约束内保affinity；只将正收益pending请求移到另一候选。A1.2明认nonuniform，重复prefix并非每请求独立uniform PoTC；eviction/动态key不授两miss界。8Ascend910B、FP16、7B32GB/14B64GB、TTFT5s/90%goodput，Mooncake有限trace/scaledarrival与warm500排除；32实例及overhead为Vidur模拟，decodeSLO/seedCI/全控制成本 ND。root实际必要源6标准OnlyReport通过；有限局部router不改变长期状态/SLO合同，不以Ch52 locality主题称具体Existing，不造recipe缺位gap。

### [Revisiting the Shape Convention of Transformer Language Models](https://arxiv.org/html/2602.06471v1)

exact-v1 §3/Eq2–5、T1–5/AppA1.1/A1.4/T7；SubmittedFeb06 07:55:30Z、registeredFeb09 02:42:51Z按共同条件。SwiGLU bottleneck内部残差K不同全层L；T1固定dm/L/attention质量近同，T3/4联合dm/attention/FFN及1B层20vs16非单shape因果，T4 PPL不授所有downstream更优，K5消融增参数67→175M。OLMo2 stage1固定顺序/seed6198、2.5/7/16/21Btokens、RTX6000Ada/B200、AdamW/CE+softmaxaux、seq2048/4096，precision/kernel/latency/全cost/repeatCI ND。root核5标准OnlyReport；Ch16常见expand非必要定理、相同预算与结构参数非速度已有边界不等exact-recipe Existing；局部可选shape未改变通用选择。主文43.19→42.16与T1实际不一致保留，不补造数值。

### [Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning](https://arxiv.org/html/2602.06475v1)

exact-v1 HTML §3.1–3.3/Eq3–8/Th3.1–2、§4/T1与官方10页PDF p5–7/末页实际读；SubmittedFeb06 08:03:11Z、registeredFeb09 02:42:57Z按共同条件。末token latent扰动以answer-distribution与norm稳定造episode reward，surprise加权后组归一/反映射token，仍含outcome监督。稳定高norm不能排除常量/answer-insensitive方向，Th3.2需noncausal tangent/B6却授最优causal收敛；主文B3/B6证明、g_m/F及q操作在两入口均缺，不能自行补假设。4kNumina或919AIME、1.5B/7B/A100/lr1e-6/b256/weights .9/.8；M/扰动/precision/q评估cost/seedCI ND，表内数字不作Evidence。root5分中心Disputed终态通过，不进Books；只重开必要B/F与依赖保证，不无限恢复附件。

### [Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention](https://arxiv.org/html/2602.06478v1)

exact-v1 §2.3–2.7/§3.1–3.6/T2–6及AppC/D/T7/E/T8/G；SubmittedFeb06 08:11:58Z、registeredFeb09 02:43:02Z按共同条件。input各view独立intra、target self/cross各层读取；固定image/pose/weight可复用input KV，新view只自身encode，cross及总latency仍随views增长。REPA teacher训练成本另计。T2 res256质量低于decoder-only，512 PSNR高而LPIPS低；同宽层199vs177M非参数等价，mask86M/MMDiT164M不同容量。scene2+1天/object3+2天64A10080GB、消融2A10010h，precision/latencyhardware/batch/seedCI ND。root6标准OnlyReport通过；局部NVS recipe不建立通用跨模态/真实世界可更新state，非Ch23主题Existing或自动gap。

### [Scaling Speech Tokenizers with Diffusion Autoencoders](https://arxiv.org/html/2602.06602v1)

§2.1–4/3.1–3.4/T1/3–5实际读。mel50Hz/128bin→stack4/12.5Hz、VQ32dim/65536EMA、16层causal encoder/4层CTC/16层noncausalFM decoder、Vocos24KHz；直接CTC transcript监督取代额外ASR语义encoder是局部低rate双用途条件。intro L73作者明确披露2 million hours of speech data；方法另一处省略单位，保留作者申报而非独立数据核验；一epoch约450ksteps/AdamW8e-5/32kwarmup。SeedTTS-test-en whisper/WavLM/UTMOS、DASB与1B ASR/LibriSpeech-testclean，T2baseline部分借外部数不全同训练。去CTC WER33vs4.06，CTC过大也反退、XL重建改善但ASR/SV反侧、6.25Hz collapse与R+D-only decoder WER5.73保留；TokenCFG/WER改善伴SIM下降、额外forward成本，不授普遍兼得。shortcut RTF未披露绑定硬件/precision/batch/全部训练搜索净cost/seedCI，不采用E2Eheadline或全理解生成保证。Ch23 L180–196已有语义约束/重建分账与双路径共存，非SiTok exactExisting；该局部CTC+FM/codec工作点不改变长期表示合同，不因未写此配方造gap，Only。 日期依共同公告包络落窗（右界10:45:56+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Confundo: Learning to Generate Robust Poison for Practical RAG Systems](https://arxiv.org/html/2602.06616v1)

§3–6.3/6.5及T2实际读；只审fragment/query-shift命题，不执行攻击或复制payload。作者假设攻击文档被ingest、不可查询target；Qwen3-.6B/三个surrogate embedding、40token单注入、target bge-small/Qwen3或Llama3-8B、chunk128/top3。训练random split只取prefix/suffix较高reward，不证明每fragment都有效/任意chunk安全；hallucination reward ROUGE阈值与substring target、sentiment classifier不是语义真值。6.2 chunk较大稀释攻击、unseen query83→74与paraphrase88→73反侧保留；T2去Pipeline91retrieval/62vs59ASR、去其它目标同时改语义/流畅度，不唯一归因chunk机制。warmup8sample/temp.7/minmax+GRPO；hardware/precision/全部steps/独立repeatCI/净训练与targetsearch成本ND。具体负侧成立但仅有限测量，不授通用防线失败/无需上传条件，不按Ch72未写此recipe造gap；Only无Books。 日期依共同公告包络落窗（右界10:46:15+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [TrapSuffix: Proactive Defense Against Adversarial Suffixes in Jailbreaking](https://arxiv.org/html/2602.06630v1)

§3–5.3/7、T1–3必要源已读。random-vs-trap hinge排序/线性安全项/gradient attraction及nonrefusal-safe对比是局部训练防线；不从这些loss授成功攻击必含fingerprint。ASR实际定义为harmful AND evade tracing，不能称伤害率<.01%；T2仍124真实jailbreak/109traced，Probe仅1/5 traced，trace≠block。80thpercentile文字与实设α0、GCG25prompt/adaptive100%trap blacklisting产生0WithTraps/0trace且未成功，不证明未来trace必然；FPR是攻击者停止误判，不是benign用户falsealarm。三模型LoRA8/alpha16/dropout.05/q/v/40epochs/lr5e-5/4A4048GB，JBB100和Dolly15k；GPT4o judge>5、utility三benchmark非逐能力/外部安全，precision/seedCI/完整净成本ND。canonical iterative suffix限域、非semantic攻击保证，模型adaptation付成本。只保留有限经验不采inevitable/硬trace保证、不造Ch72配方gap，Only。 日期依共同公告包络落窗（右界10:46:35+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](https://arxiv.org/html/2602.06643v1)

II-A–C/IV-A–D/V/VIII、必要AppE/F实际读。unscaled人类taskpose+IK preview；previous scheduled target锚actionchunk减lag反转、blind pelvis/feet只relative reference displacement防global drift。IV-C换actual EE参照75%(15/20)→40%(4/10)、IV-Dabsolute pelvis75%(15/20)→0/10为具体局部接口反侧，样本量不同、single G1平台/控制器task-specific、追踪依赖texture/light不授所有机器人稳定/安全。高层Diffusion5Hz、controller50Hz，F双224图/20Hz观测/48actionhorizon、200epoch/b256/10denoisestep/lr3e-4；E teacherprivileged→DAgger student25步history/10waypoints2s、reset与speedrandomization额外训练。hardware/precision/独立seedCI/完整sim+示教净成本ND，20有限rollout不授99%生产。Ch26 L106–132已有多时标proposal/controller与body calibration/漂移停机分责，但不是此接口exactExisting。该受限scheduled-vs-observed trade-off是局部替代，尚不支持长期安全或一般参照规则改写；Only，不因robot-free/小scale排除也不自动gap。 日期依共同公告包络落窗（右界10:46:53+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Beyond Static Alignment: Hierarchical Policy Control for LLM Safety via Risk-Aware Chain-of-Thought](https://arxiv.org/html/2602.06650v1)

§3.1–3.3/4.1–4.4/T2–5/Limits及G实际读。self-distill→global先判/earlyexit→user Label2Action为训练出的CoT序列，非法global设置只通过adversarial训练样本映射REJECT，非独立runtime hardgate；原nonoverridable/100%一致性与G+/S .833直接不授全局安全。Qwen3-8B/573435样本、自分类/自响应，CoSApien200去21partial/PACT-test5361内部生成customlabel随机mapping、三judge安全多数/两judge helpfulness非独立真值。GUIDE较REJECT安全下降而helpful升、woCoT也改变reasoning/data，不授唯一因果；Limits明确taxonomy灰区、label/chain injection及串行error，CoTtoken成本尚待优化。G给8H80080GB/lr1e-5/3epoch、temp0/top-p1/top-k1/max5k；precision/seedCI/净总成本ND。局部control经验不改变硬权限/执行责任长期原则，Only无Books。 日期依共同公告包络落窗（右界10:47:02+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Same Answer, Different Representations: Hidden instability in VLMs](https://arxiv.org/html/2602.06652v1)

§3–5/T2–4/7–8/Limits和A system/setup实际读。loglikelihood选option与五末layer probe位置分开，predicted-topmargin不是correctmargin；output不变而drift观察不证明latent“先于flip”或后续fragility因果。semantic/random/box同geometry可分部分overlay因素，R→W/W→R并存；control drift只是随机其他images非语义边界，Dirichlet差与失败相关不认证空间信息丢失。POPE blank近全No，扰动FP减伴recall损，不授去languagebias唯一因果/通用收益。四disjoint3500 subsets不等四seed，A固定seed0；单A10080GB FP16/b4、32B四A100，MMMU表847与3000同split计数不静默统一，净probe/搜索成本ND。局部VLM质量/内部geometry反证支持报告，未建立新可执行robustness验收或修复机制，不冒充Existing/未列配方gap，Only。 日期依共同公告包络落窗（右界10:47:05+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [PrefIx: Understand and Adapt to User Preference in Human-Agent Interaction](https://arxiv.org/abs/2602.06714v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。interaction-as-tool与31偏好的局部交互评价；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:48:32+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling](https://arxiv.org/abs/2602.06795v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。错误trace生成rubric的局部reward实现，20%非总gold/teacher预算；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:50:26+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [RAIGen: Rare Attribute Identification in Text-to-Image Generative Models](https://arxiv.org/abs/2602.06806v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。MSAE频率/distinctiveness的局部rarity score；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:50:41+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing](https://arxiv.org/abs/2602.06862v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。共享parameter centers/input router的局部PEFT替代；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:52:00+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Robustness Beyond Known Groups with Low-rank Adaptation](https://arxiv.org/abs/2602.06924v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。error subspace classifier logits局部鲁棒替代；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:53:24+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay](https://arxiv.org/abs/2602.06942v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。受控corpus/tokenizer的局部资源诊断，固定steps非matchedcompute；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:53:49+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [The Representational Geometry of Number](https://arxiv.org/abs/2602.06843v1)

精确v1身份/完整题摘/Submitted与registered原值见[原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)及[具体关闭依据](../_sources/daily-20260210/feb10_ready_core_notes.md)。数字任务subspace间的局部关系几何测量，非计算因果；1 + 1 + 2 = 4，root独立最低关闭通过。未标准实证完成，不采用headline，不外推通用因果/安全/质量保证；未核artifact/复现，无Books新增。 日期依共同公告包络落窗（右界10:51:34+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/html/2602.06959v1)

§4.1–3/5.1–4/T1–3实际读。20pano-view/VGGT image+camera features加和、resize/project后与noisyvideo/sceneimage concat；需desired camera但不需source显式cam，fixedFoV不推广varyingintrinsics。首context固定、其余shuffle针对ordered-position shortcut；context-vs-VGGTloss给dynamicforeground局部反側，不授隐式3D真值/世界persistentstate。internalT2V/10kstep/b16/lr5e-5、384×672/77frame/50采样步、300heldout/50OOD；samebackbone重实现contextbaselines但不同3D/camera baseline设置。T3ordered matchingpixels4673.67>shuffled4617.51、progressive RotErr2.5757<shuffled2.6825，非所有metric单调；T1CLIP-T弱于FramePack，10.17×速度未绑定硬件/precision/全VGGT成本/CI不采用。原static/dynamic decomposition与生成condition设计是有限配方，不转长期可执行3D一致性或安全机制，Only、不造recipe gap/不复查全附件。 日期依共同公告包络落窗（右界10:54:14+08:00），root已核必要原源/直接反侧或相应最低身份关闭并通过终态，仅报告，无新Books；不授日级Gate。

### [Not All Layers Need Tuning: Selective Layer Restoration Recovers Diversity](https://arxiv.org/html/2602.06665v1)

[exact-v1](https://arxiv.org/html/2602.06665v1) §3.1–3.3/4.1–4.5/Limits/AppA1/T1实际读。共享架构pre/post checkpoint区间整层恢复，CRC单token已知valid set的条件entropy与valid mass分开；20prompt×两类、qmin=.9×post而非任意quality保持。A100不batch搜索30/45/60min，search非零成本；proxy-soup 21个alpha搜索非同搜索数量。三7–9B、固定min-p.1/T1、100writing×32、40QA×128，GSM8K仅各模型greedy失败100题×64，不授全任务推理收益。Gemini2.5Pro judge/canonicalization可能漏未列正确答案，embedding diversity不是正确性。T1多项poem/story与Gemma joke质量下降，Early/Late恢复仅QA对照，不能称所有行为定位同层或安全保留；max4096/QA64，precision/seedCI/全搜索与生成净costND。局部可选checkpoint干预不改变长期posttraining或可靠性合同，不因缺配方造gap、不冒充Existing，Only。 root已实际必要原源与反侧复核通过，仅报告，无新增Books；完整作者证据保留于[必要源笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [Pruning at Initialisation through the lens of Graphon Limit: Convergence, Expressivity, and Generalisation](https://arxiv.org/html/2602.06675v1)

[exact-v1](https://arxiv.org/html/2602.06675v1) §3.2/4.1–4.4/5.1–5.2/6.1–6.4实际读。one-hidden-layer/squared loss/固定label与Gaussian初始化；factorised saliency收敛依d,n共同增长、bounded row profile、neuron CDF、conditional iid edge noise与稳定threshold；SNIP entry影响渐消是近似桥梁，GraSP此处magnitude变体非原signed任意结构。UAT限active k坐标、正measure rectangle/edge floor与αn p^k→∞，不是全ambient能力或算法一定找对任务feature。NTK lazy与λmin>0、i.i.d.S，yᵀK^-1y/路径上界不自动准确率/硬件加速；n4096 binaryCIFAR10代理，高density≥.7 curves接近或反转及过集中spectral collapse保留，hardware/precision/全训练资源ND。条件理论贡献不因非LLM排除，未将宽limit授实际foundation剪枝新保证；有限asymptotic taxonomy/边界可报告，暂无可直接改变长期可执行选择的增量，不自动Books。 root已实际必要原源与反侧复核通过，仅报告，无新增Books；完整作者证据保留于[必要源笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/html/2602.06687v1)

[exact-v1](https://arxiv.org/html/2602.06687v1) §3.1–3.3/4.1–4.5/T3/4/6与必要Limits实际读。rootcause/verdict分账有具体评价增量，但semantic-preserving实为g++编译+三LLM多数非执行等价证明；GPT5 MATCH judge只抽200 MISMATCH（10.9%）人审，3%不能授全池precision/recall。T3 vulnerable要求label+MATCH、patched却将falsepositive+MATCH重归TN，非普通同分母F1。DAG source/intermediate/sink与parent-order/closure是结构规则，final reward仍DeepSeekR1对gold judge，不认证program causal truth；gold生成也给groundtruth，regex/similarity过滤不排leakage。8157 SFT3epochs→2178/4096筛RL2epochs/rollout16，多阶段成本非同预算；8A80040GB，precision/seedCI/完整lr/batch与净成本ND。T4 Claude hinted扰动反更好、T6 DAG-only局部弱于CoT，保留非单调。具体diagnostic/训练替代不足通用可靠审计或proof-carrying执行机制，不新Books、不因安全主题自动gap/全proof。 root已实际必要原源与反侧复核通过，仅报告，无新增Books；完整作者证据保留于[必要源笔记](../_sources/daily-20260210/feb10_ready_core_notes.md)。

### [NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models](https://arxiv.org/html/2602.06694v1)

[exact-v1](https://arxiv.org/html/2602.06694v1) §3.1–3.3/4.1–4.6/T2–7、AppC/E必要配置与反侧实际读。双binary低rank factor与两channel scale；KFAC-diagonal预补偿→ADMM/SVID→STE→冻结binary后全局scale/logits蒸馏，属具体PTQ工作点，不授global optimum。128×2048 WT2校准、各重建8epoch/400ADMM步/seed0/H10080GB，WT2 PPL存在校准任务重叠；QAT结果/训练量引用不同，baseline checkpoint bytes部分由公式估算，不是实装公平资源比较。T3/T4/T6/T7 PPL改善≠zero-shot普保、低成本≠同质量；最低bit大量准确率损失，局部精度/补偿消融非单调。AppE两段packed uint32解码：GEMV FP16/BF16非TensorCore、GEMM走TensorCore，两次factor中间量与rank不免费；128input/512batched-output、batch1 decode/不同batch GEMM、TX2/3050/A100/H100，PyTorch BF16/FP16参照不授任意engine/SLO收益。存储模型含FP16scale假定，训练precision/完整搜索与生产净cost/CI ND；不采ADMM单调到全局最优。Ch49既有binary-factor、inner-rank与执行开销边界不是此PTQ exactExisting；局部训练配方不自动新长期gap，Only。 root已实际必要原源与反侧复核通过，仅报告，无新Books。

### [Explaining Grokking in Transformers through the Lens of Inductive Bias](https://arxiv.org/html/2602.06702v1)

[exact-v1](https://arxiv.org/html/2602.06702v1) §2.1–2.4/3.1–3.2/4/5Limits及AppC必要方法/反侧实际读。mod-add p113、单层128宽/4head/MLP512、fullbatch10kepoch/AdamW lr.001-wd1、5seeds；LN置MLP或QKV有路径差异，10k内未泛化不证明永久失败。readout scale与lr联动调η0/α²后原趋势反转，wd也随η改变；MSE-SGD比例与CE/AdamW近似分开、epsilon及训练阶段条件不授全部LLM相同动力学。MLP scaleSR只是观察，不是反传处理；prelogit ER谱相关、5seed取min聚合压slingshot不当普通平均/唯一因果。hardware型号/precision/CI/完整search成本ND，小模型反证不因toy拒绝，但仅受限优化与评价混杂判断；无新一般LN或可执行可靠合同，Only。 root已实际必要原源与反侧复核通过，仅报告，无新Books。

### [F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare](https://arxiv.org/html/2602.06717v1)

exact-v1 §3.1/Eq9–11、§3.2/4/T3与AppF2/H/I必要源及[详细证据](../_sources/daily-20260210/feb10_ready_core_notes.md)已读。iid二值中mixed有更新信号不等指定rare-correct采到，有限categorical局部更新不授共享θ长期收敛。Focal成功率proxy不认证tail保留；基础NLL选1263轨迹、γ搜索及1024→256 paired重采非独立training repeats，pass1/pass256反侧及16H100/完整净预算限制保留。root实际Ch33原group混合/成功率与curriculum、positive-only及Rare论证：缺的是同题trajectory coverage与题coverage的明确分账，不是缺focal配方。6分只此窄概率/评价命题深入整合，实际Ch33 L332/334及319–347邻接、末注2748已获root非作者POST；36实际POST，锁释放，不授全日Gate。

### [A Unified Framework for LLM Watermarks](https://arxiv.org/html/2602.06754v1)

[exact-v1](https://arxiv.org/html/2602.06754v1) §3–5/6、AppA/C4/D5实际必要读。固定hash/detector的token-level期望score优化，不是联合/sequence最优power；hard约束每g、soft约束对G平均，新增PPL方案的quality只是代理。D5 iid连续score/有限一阶moment/finiteΣ/feasible条件只证明“存在”support1 optimal，不是所有soft方案必然确定；主文措辞更强，隔离不采。重复prompt固定key下diversity与平均无distortion不同；1000ELI5×200token、Llama3.1-8B16bit/temp.7/topk50、Qwen3-30B8bit PPL，100prompt×100重复的trigramSelfBLEU/固定TPR.95及1%FPR有限测量，非semantic diversity/改写抗性保证。C4caption Ministral、method Llama的identity冲突保留，accuracy三任务平均不授每项普保；硬件/净求解hashcost/seedCI ND。Ch72 L1048附近已明确平均key/message不认证条件质量，固定key重复维度是更细评价，但当前未改变实际来源归属或可靠性机制；Only，不叫exactExisting/新Books缺口。 root已实际必要原源与直接反侧复核通过，无新Books。

### ["Tab, Tab, Bug": Security Pitfalls of Next Edit Suggestions in AI-Integrated IDEs](https://arxiv.org/html/2602.06759v1)

[exact-v1](https://arxiv.org/html/2602.06759v1) §2.1–2.4/3.1–3.2/4.1–4.2/6/T2及AppD实际读。新增recent-view/undo仍在editbuffer/LSP依赖和transactional替换缺安全配置的有限failure路径，不执行攻击/不复制payload。CodeQL top1000Java→手工构造410独立cases，Zeta每场景10重复→4100，不当4100独立project；黑盒四IDE120case单次→480，case不matched model/检索/预算、reload只是作者清history非因果控制认证。T2各vector非所有模型更差（Zed编辑历史0、commercial autojump较低）；无suggestion不能认证修复，但debounce与用户低警觉属作者归因/问卷，未分离受控UX因果。blackbox精确IDE/model版本、hardware/precision/fullinput-output/budgetCI ND，不能将Jan2026版本事实外推current或所有NES，亦不据JSD授显著无变化。既有context provenance/effect审核原则不等此实例exactExisting；局部版本测量未建立新runtime enforcement/外部回执契约，Only，不按安全词/owner缺配方造gap。 root已实际必要原源与直接反侧复核通过，无新Books。

### [R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging](https://arxiv.org/html/2602.06763v1)

[exact-v1](https://arxiv.org/html/2602.06763v1) §2–5/T1–5/AppC/D实际读。label-correct∧MetaRM-rationale-aligned是具体诊断/训练分解，gold rationale由Gemini3Pro conditionedlabel或整合人审生成；同teacher产gold又评、GPTOSS120B训练meta选择对GeminiF1，不能认证真实内部causalreason或普遍soundness。AppC只53 HelpSteer3/Qwen14B label-correct样本人审，不授全benchmark可靠率。8/14B RM PPO同hyperparameter声明不等同总teacher/runtime预算；下游Qwen8B、Arena prompts+Step3-VL10B固定reference/+1−1与动态lengthpenalty，净teacher成本/hardware/precision/lrstepsseedCI ND。T4RAlign8 IF26.9低于RLVR30.3/base32、14B coding49.4低于RLVR50.1，且多项base更高，不能称能力保留或所有域赢；§5.3相关含自己训练family，不识别唯一rationale因果/外推保证，§5.2恢复数值与列名文字冲突不采。新增有限evaluator与配方可报告，但未支持长期审计真值机制或比既有critic/trace分账更强权限，Only不造gap。 root已实际必要原源与直接反侧复核通过，无新Books。

## 5. 缺口与下一步

2026-10-08补查可执行待办：无。root已实际通过SOURCE、13个完整题摘准入校准、4项必要日期安全隔离及当前六部分DAY；V3、原135行/原§4/原窗口一致性、151本地引用与限定diff-check通过。扫描/筛选/正文审阅/Books修改/独立复核普通待办为0，不展开月列表/其他日报。下列4项必要日期及未恢复历史入口是外部终态保留，不用于正面Evidence/Books/无遗漏或性能安全保证；定点材料到达后仅重开受影响身份。下方原完成声明与有效证据继续保留，不代替本轮验收。

追加有限Seed恢复发现的[SAGE2602.08354v1](https://arxiv.org/abs/2602.08354v1) 完整题摘已读：longCoT冗余→模型隐含stop时点被sampling遮蔽→新采样SAGE与SAGE-RL混采可能改变停止/训练接口，root实际准入校准确认潜在贡献成立。官方当前列表PublishDate标Feb09而ArticleID/UpdateTime在后月份，arXiv v1 Submitted为Feb09、最早公告已越过本窗，不能把后回填目录日期自动当历史同正文首次公开。未列确定候选/评分/核心审阅/Books；必要首公开日期按第4项外部终态隔离，只接受Feb09该精确正文作者原页快照/同期公开日志或官方事件证明，满足日期后定点核实际采样/停止条件，不扩大版本史。[完整题摘及metadata](../_sources/daily-20260210/supplement-20261008-rss-seed-gap-recovery.json)。

3项必要日期终态保留：[DAVE2602.06613v1](https://arxiv.org/abs/2602.06613v1) 的patch embedding/attention routing梯度结构噪声→稳定局部等变分量分解，可能改变pixel attribution解释；[ABR2602.06328v1](https://arxiv.org/abs/2602.06328v1) 的长期TTA误差轨迹→label-flip变化自适应reset间隔，可能改变持久更新状态与重置选择。两项是既存原筛选身份，root已定点撤销“无机制信号”模板理由，但SubmittedFeb06与旧registry_updated_v1+排程/DataCite推定不是新核验的首次公开日期，当前不得授本窗准入，不改旧ledger/原候选日期，不双计。新增[Does Visual Rendering Bypass Tokenization?2602.06973v1](https://arxiv.org/abs/2602.06973v1) 完整题摘给DualGPT重新接text tokenizer后的四脚本反证：较低OOV/fertility仍不代表chrF++更好，可能改变视觉入口能否绕过tokenizer约束的判断；v1 Submitted为2026-01-12，2602 ID/月列表不能独自确定Feb09首公开。3项均未列确定候选、未评分、未读核心绕日期门、未进入Books/正面Evidence/无遗漏保证。接受官方该精确版本首次公告/公开日期日志或同正文作者首次公开记录，完整公开日期范围落窗后只重开对应身份的日期/准入；不追求时分秒、不补造日期。[DAVE/ABR完整原件](../_sources/daily-20260210/supplement-20261008-abstracts.json)、[pixel/ILA完整原件](../_sources/daily-20260210/supplement-20261008-edge-abstracts.json)。ILA-agent2602.06976v1已按具体贡献不足关闭，不为不影响处置的日期另保留请求。

检索线索中2602.08329v1、08335v1的Submitted为Feb09 UTC，09017v1为Feb09晚UTC，arXiv排程最早公告已越过本补充北京自然日；不能照索引“Feb09”标签归入本窗。未建立更早同正文公开信号，不作当窗候选/已审重复。SpiderSense2602.05386v2仅版本变化不证明本窗重要增量，不展开版本史。四主题搜索空召回、Advanced/API错误、Meta空文本及机构当前目录限制不支持零发布或无遗漏。

可执行待办：无。来源有限入口已停止、135个唯一候选冻结并逐项安全终裁；普通扫描、筛选、审阅、Books修改与独立复核待办均为0。root已通过当前六部分日级Gate，本日完成，不扩150日期身份/170题摘/496库存、不重读有效证据或POST。本日外部终态保留项如下，不用于正面Evidence/Books/无遗漏或性能安全保证；材料到达仅定点重开对应身份或入口，不阻塞本次结束。

本窗外部保留项：

- Steering Identifiability `2602.06801v1` 中心全prompt严格输出分布等价：接受冻结模型下共同非零kernel、非线性精确等价的明确限定假设与有效证明/勘误后，仅重开Prop1及B2/B3依赖命题；局部lexical测量、低effective rank或同时改W不替代。当前不正面采用、不写Books，不请求全部附件。

- GC2PO `2602.06475v1` 中心causal block识别/收敛争议：HTML与官方10页PDF未给B3/B6必要证明、g_m实现F及q(answer|latent)操作。只接受同精确版本必要B/F段、相容artifact或勘误后，定点重开§3.2及依赖稳定/energy→causal与收敛命题；不要求全代码/全版本，不把norm或有限task曲线当因果识别。当前无正面Evidence或Books。

- DiSPO `2602.06462v1` 未采用理论子命题：只接受与同版本经验目标匹配的normalized surrogate、实际branch采样分布、固定state和groupbaseline独立性/条件说明；核清exp(Elog)/πold与tildeπold桥梁后定点重开§4/A1.1及依赖方差/无偏结论。不请求全代码/全proof，经验接口采用不授理论成立。

- PCR `2602.06453v1` 中心更新争议：只接受同版本明确conflict/nonconflict下MLP最终梯度、βgsta保留规则、variance estimator的实际定义及所引必要算法/配置，核清Eq14–16与文字后定点重开§4.4–4.5/Theorem5.1。Scalar Gaussian MMSE不替代LLM稳定/安全证据，当前不正面采用、不写Books；不请求全code/全附件，不静默更正β或错指公式。

- VENOMREC `2602.06409v1` 未采用真实pixel-upload路径/防线与跨骨干安全claim：主文feature-vector编辑不证明原始UGC可构造，HTML/PDF附录A1–A5为空，缺pixel-feasible路径或可核对应artifact、matched-search budget/必要defensivefilter及T5base证据。只接受作者精确补充或对应原版本必要材料后定点重开§4.2–4.3/§5及相应A段；不要求全部code/版本史，当前局部作者事实OnlyReport不授生产安全。
- MOX `2602.06441v1` 中心GD普遍no-collapse/retainKL自动给θfor保持争议：缺一致CE/NPO方向、目标人口/下界及negative-edit最终artifact的保持条件。接受作者精确勘误与对应必要条件/对照后，仅重开§2.3/AppC及依赖安全结论；不要求全代码，不静默更正原loss，不把θmem约束迁移到θfor。局部mem→negative edit作者结果仅作描述，无Books/正面安全Evidence。
- CORE `2602.06446v1` 中心metric/labelmapping争议：只接受同题ID与answerletter→relation映射、SCR原始分母/逐项计数，以及selfreport置信度读取/校准映射；核清实际negativeoption控制及是否存在None/abstain行为后定点重开§4.3/5.1/5.3/AppA，不请求全code/所有版本，不授架构因果或原相关数值。
- AR Stability `2602.06413v1` 中心AR必然cliff/DAG必要性争议：AppB均衡先验平均Bayes的条件收缩界不等主文posterior及真实decoder严格收缩；cached controller同时reset/edge-dedup未核新增信息/分别反侧。只接受一致统计对象、实际decoding收缩条件/系数与reset所需信息或控制机制、必要独立对照后定点重开§3/AppB/§5.3及依赖必要性；不要求全附件，不授无条件AR失败或安全。
- Condensate `2602.06317v1` 中心恒等/总复杂度/未来KV状态争议：缺少满足必要precision/rounding条件的等价证明、把全QK选择计入的复杂度，以及query变化后已删历史TopK如何恢复的状态合同。只接受作者精确勘误/可核证明和必要artifact后重开§2/4/5/7及依赖速度，不以有限greedy匹配替代、不扩版本史；当前无Books及正面Evidence。
- SOCKET `2602.06283v1` 未采用最终weight配方：Algo3 exp(hashscore)与正文subsetexactstandardsoftmax冲突；接受精确勘误或对应version代码及必要数值验证后只重开该接口与依赖精度结论。graded selector/全N扫描的已采用分支不受影响，不授practicalTopK angular-kernel exactness。
- DeDPO `2602.06195v1` 未采用子命题：Eq5/Eq18 BCE符号与Eq21导数不一致，网络权重收敛、bias-free trained policy和fully-labelled upperbound不能由已采用的fixed-θ估计器身份推出。接受作者精确版本勘误/一致公式、与之匹配的独立nuisance/采样条件证明或必要artifact后，仅重开该公式及依赖理论；不阻塞代表性loss residual窄接口，也不自行修原式。
- 早期Submitted的12个日期保留身份：2602.06050、06051、06057、06063、06065、06071、06072、06075、06079、06081、06098、06107。完整原字段见[170身份原日期](../_sources/daily-20260210/feb10_all_selected_date_raw.json)，精确子集见[150正常/12早期](../_sources/daily-20260210/feb10_date_subsets.json)。Available v1仅月，Updated不当first-public，Created/Registered仅存在上界；这12项的Submitted早于2026-02-05T19:00:00Z，不能据排程证明下界已进入本窗。只接受官方首次公告/精确版本首次公开日志，或作者同一正文首公开且完整范围落窗的证据，然后只重开对应身份。正常150项不再一律称日期不可得：Submitted不早于Thu Feb05 14EST截止点，最早可能公告为Sun Feb08 20EST（Feb09 01Z/09BJT）；arXiv ID不提前生成及各原Feb09 registered给存在上界，无更早同正文公开信号时可条件准入。保留秒精度字段，不把Submitted或Updated直接当公开时刻。
- 来源历史切片：上述 Anthropic、Meta、Qwen、DeepSeek、Hunyuan、ZAI、Seed，以及 Google publication、MiMo无日期Blog、MiniMax Agent目录有限限制不支撑完整Coverage。可接受替代为带日期的官方本窗目录/分页、官方历史快照或同机构可核本窗发布事件；只重开相应入口/切片，不重扫机构历年全部研究。
- PersonaPlex 原文/项目在Jan15已有公开，本窗仅arXiv记录不构成新的已证修订；真实归属日恢复线索见[作者原页raw](../_sources/daily-20260210/feb10_scope_B_deeper_2.json)，不顺带处理01/15。

所有日期/历史隔离项和未采用争议子命题不计正面Evidence、不进入Books、不支撑无遗漏、性能或安全保证。材料到达才定点重开；普通未读不写受阻。

## 6. 复核

2026-10-08补查复核：复核者为root（非本日报告作者），已实际独立读PlanViz/DAVE/RAIGen/DiTS/HQP/LAAFD/PointViT/comparIA及ABR/CER完整题摘、DAVE/ABR/PlanViz旧ledger具体理由和pixel/ILA/SAGE三项新身份完整题摘、Seed原始metadata/UpdateTime及两处SOURCE有限恢复。准入校准通过：5个具名代表关闭+PlanViz/ILA贡献不足、RAIGen有效候选复用、DAVE/ABR错误关闭撤销及4项日期安全隔离（含SAGE潜在sampling+RL迁移）；CER未发现新的基础模型/系统机制线索，不因题名hallucination自动准入。SOURCE有限入口与RSS/Seed两处实际恢复已独立通过；root实际核旧候选冻结、原§4、当前§5/6及本轮六部分终处置，结论：通过；DAY已完成，普通待办为0。无新增Books写入，无本轮POST对象；以下原复核有效复用，不重做未变化单项或36项Books POST。

本轮机器校验：V3与限定cached/unstaged diff-check通过；151本地引用0缺。原135候选逐行sha256、原窗口均一致，原§4采用heading后原换行到§5前换行（不trim），91350字符sha256 `7f2ac5c3356c0be02ff226b14d6e766f77684098abc695ff63099a3f9d4d02d8`与运行前一致，root已独立机器复算。补查JSON语法通过，全部写入限定本日README/本日supplement原件，无新增共享Books/LEARNING_STATE/索引/其他日报写入，未stage、commit或push。机器校验不替代上述实际DAY。

复核者：root 与 fresh独立复核者 feb10_finite_review（均非本日报告作者）。
结论：通过

root已实际验收当前六部分与有限停止/冻结、证据/Books终态、外部隔离及新增字段纠正；135单项终裁与36实际POST有效复用。

当前最终范围：root分批复核126个候选的必要原源/关闭依据、全部36项实际Books写入与邻接POST；fresh独立复核者复核最后9项（06771/06825/06850/06854/06871/06887/06909/06911/06914），root已接受其终裁。合计135家族，不是每人无差别重读全部附件。PKA/RFDM从4纠正5并补必要评价反侧；DreamDojo T6 singleH100、AEGPO训练时间/显存、RFDM keyframe周期/反侧与split冲突、Generic clean/leaky量与人口混杂、Tamper BF16均明确修正。source有限停止与135冻结不授无遗漏；15项具名贡献前关闭的具体题摘/决定性依据已获root复核，其余明确范围外按来源/主题/理由的有限样本核验，不称496库存全量验证。早期12日期与历史切片未获正面Coverage/Evidence，均保持终态隔离；旧阶段人数仅过程证据，不控制当前。

### 历史分批复核证据

以下各阶段人数及待冻结/待Gate表述仅保留当时单项证据，不覆盖本节顶部135终裁与当前验收状态。

root实际核170题摘ledger及具名完整AB准入/负侧；准入不授Evidence。正常150条件包络、早期12隔离及06549通用学习纠错/06138/06767修正通过。Kimi/06319/06345/06440/06409/06443/06155/06549必要仅报告、06181/06454具体已有覆盖通过；MoP/MoSE/Venom/COVER/SWIRL/μA/DeDPO/SOCKET/Belief/CBU/VLA几何/FlowConsist/Di3PO/SHINE/OGS/ReBeCA/DEPO/Muon/MuCo/BridgeNav/SureLock/TurningPoint/QA-Token/STA/GCPA/低秩初始化/FoG/paired SAE/MCQ修复/BrokenBind/DiSPO/UNO/PEPO三十三处实际源→owner→POST通过。06266/06275/06300/06337/06370低分关闭与06341/06366/06384/06391/06442/06525贡献前关闭通过；06671/06875的旧排除在本轮同门槛贡献校准中复核，不能只借其成熟子模块关闭全部题摘贡献。06317/06413/06441/06446/06453中心争议隔离。最终候选冻结及六部分日级验收未完成，最终分层抽检数量/未查范围待root记录。

本轮纠偏复核：root独立核五项完整题摘与决定性事实，EvoMAS/TraceCoder贡献前关闭、AST负侧准入成立；另核REBEL、D-Legion、GRP、DriveWorld与AgentCPM的必要源，仅报告终裁通过。Steering实际Ch31两段、邻接与末注POST通过，锁已释放；合计三十四项真实POST。其余有效既有复核不重做，最终候选清单及六部分日级验收仍未完成。

root另实际核AST必要方法/直接raw-SBT-NIT反侧、FCDP IV-C/E/Alg1/V-A/VI-A及Ch39具体正文、DualMap §3.2–3.3/§4.1/A1.2/A3，三个标准终处置通过并同步，未新增Books写入。

root实际核Hourglass T1/T3–4/AppA预算反侧、GC2PO Eq3–4/Th3.1–2与必要B/F缺失、LVSM §2.3–2.7/T2/AppC–E，分别5标准OnlyReport、5中心争议隔离与6标准OnlyReport通过，不撤贡献准入、不借局部recipe造Books差额。

root实际核JADE §3/Eq3/9–12/§5.4人审、UATS §4.2/5/6.1/T2/F1成本与直接反侧、GRASP §6.1/7.2–3/T5，三个Only终处置通过并同步，无新增Books写。

root另实际核World-VLA-Loop/HyPER/LogicSkills/MaliciousSkills/MERGE/SeeUPO对应必要方法、对照与直接反侧，六项Only终处置通过；DREAM必要源/具体owner及Ch76两段、前后邻接与末注实际POST通过，共35实际整合。理论共享参数桥梁与短sandbox漏检分别限定，不授全局/安全保证，未造其余recipe gap。

root另实际打开LIBERO-X III-B/IV-A/B与SPARC §5/6/T2/3，两项6标准仅报告终裁通过；累计扰动/重训/predicate混杂与WBF负侧、SFT epoch冲突、冻结权重非行为守恒均保留。单项通过不授日级Gate。

root实际AgentCPM-Explore §2.4/3.3局部summary消费反侧通过5标准Only；DAIReS方法/Meta/Discussion直接原源安全排除复核通过，不纳候选或评分，未造因果诊断机制/不可用材料请求。

root必要原源已核ThinkProprio/Latent Rethinking/Degradation/Echoes/Overlap，五项Only终裁通过；Degradation/Echoes定点加深仅必要反侧，FairJudge v1 AB/身份4分关闭通过。六项已同步，未新增Books或Existing。单篇通过不授日级Gate。

root另已实际核Confundo/TrapSuffix/PACT/SameAnswer必要安全/设计反側，SiTok/HuMI/CineScene最低标准原源与关键反侧，七项Only通过；SiTok按intro纠正2M hours作者披露。六local4与数字几何最低关闭通过；TaS贡献前排除通过。正式98终处置，不加新Books，单项不是日级Gate。

root实际核SLR §3.1–3.3/4.1/图3、Graphon §3.2/5.1–2/6.2–4、DAGVul §3.1–3.3/4.1–4.5，三项必要源Only终裁通过；正式101终处置，未新增Books，非日级Gate。

root实际核NanoQuant §3/4/T3/T6–7/AppE、Grokking §2/3/AppC必要机制/预算与设计反侧，两项Only通过；F-GRPO §3/4/T3/F2及实际Ch33 L332/334、319–347邻接与末注2748 POST通过，正式104终处置、36实际POST，锁释放。单项通过不授日级Gate。

root实际Watermark §3/5.3/D5、NES §2/3/T2/4.2、R-Align §3/4/T4/AppC必要源核后Only终裁通过，正式107；不新增Books，不授日级Gate。

root实际CodeSSM §3–5/T1、SquaredPO §3/Lemma2/T1反側、FSL §3.1/Th6.3必要源通过三个标准Only；Steering Identifiability B2/B3中心保证缺严格冻结模型桥梁，按Disputed隔离。正式111，36 actualPOST不变，不授日级Gate。

root实际核ScaleEnv/POP/EDS-WDS/CTWA/NanoFLUX对应关键方法、预算与直接反侧，五项限定Only通过，正式116＝96必要core（36actualPOST+3Existing+57Only）+13low+7Disputed；无新Books。NanoFLUX保留§4.5作者约2.5s合计E2E估算与T7 denoise区别，不授matched-measured E2E验收。

root实际核DeVA/ViT plasticity/Prompt Reinjection与Aurora/ESR/Agentic Uncertainty的关键方法、预算和直接反侧，六限定Only终裁通过并正式同步122＝102必要core（36actualPOST+3Existing+63Only）+13low+7Disputed；不授center因果或生产普保，无新Books。此前有效单项/POST复用，不授日级Gate。

机器校验：本轮135行V3、唯一135家族与六部分结构通过；45标准/66深入/17关闭/7争议，36整合/3已有覆盖/89仅报告/7暂缓；147本地引用均存在、日期JSON有效、Markdown无异常，限定cached/unstaged diff-check均0。工具不证明语义验收；既有dirty保持，未stage、commit或push；root整日Gate已通过。
