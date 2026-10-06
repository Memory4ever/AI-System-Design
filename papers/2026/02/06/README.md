# Daily Research — 2026-02-06

**规范：** V3
**窗口：** 2026-02-05T09:00:00+08:00 ～ 2026-02-06T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T00:15:53+08:00

## 1. 结论

本日独立从原始来源重建，旧README仅原文备份于[LEGACY_README](../_sources/daily-20260206/LEGACY_README.md)，cmp一致；未用旧候选/评分/摘要反推准入。原目录非feb06_前缀均属legacy。14每日来源已有限停止，贡献队列与70家族候选清单冻结；75份新读取完整v1题摘不等于75候选。当前31实际Books POST、14具体已有覆盖、13仅报告与12中心争议终态保留；普通候选处置0，源核通过与机器检查仍不替代日级验收。首批准入/代表负侧、逐项必要原源和owner均按实际非作者范围记录，不授摘要宣传、注册即发布或覆盖保证。Books采用具体接口/反证与成本/回退，保持旧合理路径；未stage、commit或push。本日已完成到合同安全终态，jan02_v3独立六部分日级Gate通过；实际范围与未核权限见§6。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research原入口、fresh官方RSS1243只作metadata定位；Feb3～7窗口边界：Frontier Feb5 06GMT、TAC10GMT落窗；protein11GMT为暂缓AIforScience；GPT5.3 release/card Feb5 00GMT窗前，localization Feb6 10GMT窗后即停止。Frontier L42–108及TAC L38–55必要core已读，root关闭/准入分别通过。 | 已检查 | 当前原页不是初版逐句证明；RSS有限定位不证明历史无删改。 |
| SRC-ANTHROPIC | Research current10及原publishedOn定点Jan/Feb；zero-days Feb5 00Z窗前。Opus4.6 release原datePublished Feb5 18Z落窗、modified Sept9；当前card必要缓存为11/103–104/106–108/116，不遍历213页。 | 已检查 | Release adaptive effort接口与Ch56具体Existing经root实际核通过；current card后期修改不能当Feb5初版披露，p103+安全案例事件时刻不明，终态隔离不采为首日机制。原初版/带事件时间条款到达只定点重开；不把单页11写成1～11已读。 |
| SRC-GOOGLE-AI | Google pubs目录只身份定位；February2026Blog7；原NAI的tools URL实际404，不能授已读。本轮一次具名官方域补检恢复正确agents URL，当前原页L100/104–151全部core已读并保存[fresh corrected core](../_sources/daily-20260206/feb06_NAI_corrected_core.txt)。DeepMind实际/page/3/、/4/跨May→Feb→Jan→Dec有限停止。具名DeepThink数学/科学datePublished Feb11 15Z，升级Feb12 16:13Z均窗后。 | 已检查 | NAI具体原型组合经root实际L100–151核后贡献前关闭，不因领域或无benchmark排除；有限当前列表不证明历史无删改，不扩年度pubs/linked MAVP库存。 |
| SRC-META-AI | Research原动态返回无有效历史列表；作者当时停点记述官方域Feb5四主题及一次定点模型训练/Agent/推理补检未恢复本窗原始正文，停止此入口，不把该记述当原返回。 | 受阻 | 官方动态入口原返回Total lines:0（feb06_sources_web_0.txt:571–572）可核；作者当时四主题定点补检停点未保存原返回，本次非作者不能逐项复核该补检。历史覆盖终态保留，定点重开条件为可访问官方本窗历史页/原有限补检回执，不支持零发布、Books或无遗漏断言。 |
| SRC-QWEN | fresh原HTML/JS定位 /api/v2/article/retrieval；实际读40条声明extra.date，从CoderNext Feb3 04+08跨到Image2 Feb10 13:08:30+08，本窗无可见项即停止。原值见feb06_Qwen_declared_dates.jsonl。 | 已检查 | 当前40条不是历史删除/修订完备日志，不继承前日零发布。 |
| SRC-DEEPSEEK | fresh /news动态和Research10：Research Jun24→Feb25→Jan28→Jan12→Dec31，动态Apr24→Dec1，无本窗可见项。 | 已检查 | 当前有限列表不证明历史无删改。 |
| SRC-MOONSHOT | fresh Platform本页26：Nov7/6,2025至May29,2024，不覆盖2026；具名Kimi CLI原changelog按精确非v release tags恢复：1.7.0 Feb4 18:11:34Z窗前，1.8.0 Feb5 05:45:25Z落窗，release body与changelog仅startup诊断吞错修复，作者/root实际core核后贡献前关闭即停止，不扩PR库存。 | 已检查 | Platform2026带时间历史入口本窗终态保留，恢复只补该窗口，不把org更新作首次公开；普通启动错误显示修复未新增执行/状态/兼容性验收机制，不按版本号拒绝。 |
| SRC-TENCENT-HUNYUAN | fresh Research/JS定位正确只读POST api.hunyuan.tencent.com/api/blog/publicList page1/size20/renderType0，实际返回9条全部已读；CL100025 publicAt Feb3 18:02:07+08窗前，RLclip100015 Feb13窗后，其余更晚，停止。原public/published字段保留feb06_source_API_final.jsonl。 | 已检查 | 当前9条未证明历史无删除；不把内部published字段等同公开可见时间。 |
| SRC-ZAI | fresh Research首次timeout后直接GET恢复，实际15项从Aug26→Feb21/11→Feb2 GLM-OCR→Jan19/13→Dec9，跨过窗口后停止；feb06_ZAI_current_list.json。 | 已检查 | 当前目录不证明历史无删改，timeout不是零发布依据。 |
| SRC-BYTEDANCE-SEED | freshResearch/PublicPapers仅线索；实际get_article_list_v2 article_type1/count20/publish_year2026/order_descfalse首20原ArticleMeta.PublishDate，VTok Feb4 date-only、BABE Feb5 date-only为暂缓AIforScience，首次窗后Feb9 StopThinking/Protenix后停止；has_more/total82不扩队列。 | 已检查 | VTok靠逐ID arxiv证据落窗，不从官方date-only定时或假定co-release；feb06_Seed_publish_fields.json保原值。 |
| SRC-BAIDU-ERNIE | freshBlog本页9项May9→Feb6 ERNIE5→Jan29→Jan15/8→2025，跨窗前Jan29停止；Feb6 Blog date-only相交，关联04705论文已独立核原v1并具体已有覆盖。 | 已检查 | Blog相交日期不补时刻、不与论文视作同刻release；不授Blog初版每句措辞已确定。 |
| SRC-XIAOMI-MIMO | freshPaper8：Jun29/March13→Feb3 HySparse→Jan8 Flash→2025，已读有限列表无本窗可见论文；Blog15只标题无日期/#blog，原入口与一次具名Feb2026官方域补检均未恢复历史时间，停止。 | 受阻 | Blog本窗终态保留：需带日期原文章或官方历史列表，恢复定点重开；不借Paper无项排除Blog、不扩15当前篇全文。 |
| SRC-MINIMAX | freshEN/CNBlog，CN实际13项从August→Feb12 Forge/M2.5→Jan28 her→Dec23 M2.1→2025，跨窗前后停止；Agent Tech实际仅May13一篇，窗后。 | 已检查 | 当前有限列表不证明历史无删改，不继承前日零发布。 |
| SRC-ARXIV | 作者当时停点记录四主题API start0/max100 Submitted缓冲202602031900～202602041859为429/timeout，以及CL skip250/275/300各25、AI225/25、CV400/425各25、DC25/25至05017的有限月页浏览；这些失败回执及月页原输出未保存，本次非作者无法逐请求/逐页复核。实际可核的是75份相关完整v1题摘另初始4篇、68个arxiv候选逐ID日期及全部必要处置，已有限停止。 | 受阻 | 原API/月页与revision历史覆盖为终态保留，不把175作者记述标题或75实际题摘授无遗漏。未依赖lastUpdatedDate search prefix，不授revision零事件；定点重开条件仅原有限四主题请求/已列页原列表或带公告版本日期入口恢复，不用于正面证据、Books或无遗漏断言。正面个体采用只由可核题摘/必要源与逐ID有条件公开范围支持，Submitted/注册不等首公开。 |

fresh原始记录集中[daily-20260206 sources](../_sources/daily-20260206/)，只feb06_前缀为本轮。未扫Weekly来源。

## 3. 候选与判断

已冻结70家族，三维原分不随Books决定或审阅工作量改变；31实际整合、14具体已有覆盖、13仅报告、12中心终态保留，普通候选处置0。原始题摘/日期命中不自动候选，来源受限不授无遗漏。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/) | 2026-02-05T18:00:00+08:00 | dual-use意图难区分→identity-qualified access与model mitigation分层→资格路由不等于内容/工具授权；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 550–560 model sensor/actor/TAC责任 |
| [Expert Selections In MoE Models Reveal (Almost) As Much As Text v1](https://arxiv.org/abs/2602.04105v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:51:13+08:00 | 仅离散专家选择也可联合训练decoder恢复内容→telemetry不能因无token默认非敏感；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) canonical审计后→DP前一段；root actual POST通过 |
| [ERNIE 5.0 Technical Report v1](https://arxiv.org/abs/2602.04705v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:05:14+08:00 | posthoc单形状压缩→预训练采样depth/expert-subset/top-k族→总驻留与活动计算分轴；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) 255–266 profile与训练采样 |
| [Multi-Head LatentMoE and Head Parallel v1](https://arxiv.org/abs/2602.04870v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:09:09+08:00 | routing后token复制通信→独立latent-head边界先collective后routing→通信相对k解耦但需shape/network与EP共存；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 668段；root actual POST通过 |
| [Harmonia v1](https://arxiv.org/abs/2602.04595v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:02:36+08:00 | linear-only低精度→attention BFP、KV不对称/混合平滑及可重构PE→algorithm/硬件消费联合验收；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 1643段；root actual POST通过 |
| [Likelihood-Based Reward Designs v1](https://arxiv.org/abs/2602.03979v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:48:21+08:00 | verifier奖励稀疏→current-policy参考答案似然及长度归一不同目标→reward与直接梯度分账；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 66/68两段；root actual POST通过 |
| [Survey Questions Credibility v1](https://arxiv.org/abs/2602.04033v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:49:36+08:00 | 边际问卷拟合→联合问题相关结构与prompt/decoding混杂→不能由均值一致推模拟受访者；2+2+2=6 | 争议 | 暂缓：中心指标单位终态隔离，见§4；不授结构性排行或Books |
| [VTok v1](https://arxiv.org/abs/2602.04202v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:27+08:00 | 单帧独立codec→首帧锚与特征差分motion latent→表示共享和时间重建身份分开；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 577–606 scene/motion分解与invalidation，非全部VTok实现 |
| [Prompt Underspecification v1](https://arxiv.org/abs/2602.04297v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:41+08:00 | 分类label-subset argmax→free generation/invalid parse及表示probe分账→prompt敏感未必知识变化；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 386–405 matched-output/parse/variants |
| [DeFrame v1](https://arxiv.org/abs/2602.04306v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:54+08:00 | 同任务framing改变回答→polarity映射与signed类别分布→偏好幅度稳定不等对象不变；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 390段/5276注；jan01_v3 actual POST通过 |
| [Vision vs Text Working Memory v1](https://arxiv.org/abs/2602.04355v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:57:01+08:00 | n-back成绩→错误lag结构与输入模态反证→区分编码缺陷与执行控制；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 122段；root actual POST通过 |
| [Trajectory Fusion v1](https://arxiv.org/abs/2602.04391v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:57:51+08:00 | rejection只留成功→wrong/reflection/correct整response NTP→错误前缀监督与仅条件历史不同；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) 156段/1218注；jan01_v3 actual POST通过 |
| [Swordsman v1](https://arxiv.org/abs/2602.04399v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:58:01+08:00 | 固定DLM block→entropy自适应切块及剩余计算控制→block质量/并行预算联合；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 260段/1526注；root actual POST通过 |
| [Fine-Grained Activation Steering: Steering Less, Achieving More v1](https://arxiv.org/abs/2602.04428v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:58:41+08:00 | 对比pair符号一致性AU定位→按当前输入scalar排名缩放→干预粒度不等head/neuron/SAE；2+2+2=6 | 深入完成 | 整合：MODEL-MULTI-HEAD-ATTENTION，[Ch15](../../../../books/part-02-model/15-multi-head-attention.md) 287段；root actual POST通过 |
| [Model-Dowser: Data-Free Importance Probing to Mitigate Catastrophic Forgetting in Multimodal Large Language Models v1](https://arxiv.org/abs/2602.04509v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:00:35+08:00 | 无原语料保护→base synthetic输出敏感性代理与静态各层底部可训mask→区别当前适配gradient人口；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) 813段；root actual POST通过 |
| [$C$-$ΔΘ$: Circuit-Restricted Weight Arithmetic for Selective Refusal v1](https://arxiv.org/abs/2602.04521v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:00:51+08:00 | runtime refusal hook→circuit-restricted weight arithmetic→离线选择性refusal artifact；2+2+2=6 | 争议 | 暂缓：中心mask convention/config与objective→结果绑定未决，本窗终态隔离 |
| [LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding v1](https://arxiv.org/abs/2602.04541v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:01:20+08:00 | 每head selector重扫→dense head选集跨层同head继承→完整KV驻留与稀疏消费分责；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 190段/2060注；jan01_v3 actual POST通过 |
| [Rethinking Weight Tying: Pseudo-Inverse Tying for Stable LM Training and Updates v1](https://arxiv.org/abs/2602.04556v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:01:41+08:00 | embedding/output普通weight tying→列正交Z与可逆T耦合左逆→代数接口与质量分责；2+2+2=6 | 深入完成 | 整合：MODEL-EMBEDDING，[Ch12](../../../../books/part-02-model/12-embedding.md) 158–165；root actual POST通过 |
| [Textual Planning with Explicit Latent Transitions v1](https://arxiv.org/abs/2602.04557v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:01:42+08:00 | 冻结embedding transition规划→gold-successor候选命中≠free rollout→latent预测非闭环planning guarantee；2+2+2=6 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) target/context与imagined-vs-execute；jan01_v3 actual source-owner通过 |
| [Semantic Self-Distillation for Language Model Uncertainty v1](https://arxiv.org/abs/2602.04577v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:02:10+08:00 | 多答案semantic dispersion付费→prompt-conditioned student分布→生成前uncertainty sensor；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 2041段/4297注；root actual POST通过 |
| [Trust The Typical v1](https://arxiv.org/abs/2602.04581v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:02:16+08:00 | safe-only semantic representation→typicality/OOD gate→安全信号与内容判定不同；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 831段/3010注；root actual POST通过 |
| [Active Epistemic Control v1](https://arxiv.org/abs/2602.03974v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:48:14+08:00 | 预测belief可筛计划但不可认证commit→grounded fact与独立feasibility分责→query预算不越事实权限；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING，[Ch79](../../../../books/part-07-agent/79-planning.md) 54–58/70–72/218–232；root具体核通过 |
| [Adaptive Test-Time Compute Allocation v1](https://arxiv.org/abs/2602.03975v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:48:15+08:00 | 固定验证调用→feasibility/ranking与uncertainty调k→验证前筛选及调用分账；2+2+2=6 | 争议 | 暂缓：generation/verifier预算与结果映射中心争议，本窗终态隔离 |
| [Monitorability as a Free Gift v1](https://arxiv.org/abs/2602.03978v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:48:20+08:00 | RLVR能力与monitorability变化分离→训练数据/条件人口/draft接口改变测量→升级能力不能静默迁移监测保证；3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 792/794两段/3014注；root actual POST通过 |
| [Claude Opus 4.6 release](https://www.anthropic.com/news/claude-opus-4-6) | 2026-02-06T02:00:00+08:00 | 固定reasoning预算→adaptive thinking与developer effort接口→实际route/effort/stopping及成本身份需分账；2+2+2=6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 319–337；仅公开接口边界，后期card条款隔离 |
| [OMG v1](https://arxiv.org/abs/2602.04144v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:52:07+08:00 | 语言retrieval规划与双深度注入、Tweedie/task CE联合→共享语义预测与判别目标分责；1+2+2=5 | 标准完成 | 仅报告：局部模块组合与对照条件不支持新的通用表示合同 |
| [Bi-directional Bias v1](https://arxiv.org/abs/2602.04398v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:58:00+08:00 | forward demographic entropy与backward stereotype cue JSD是不同观察对象→fairness指标不能互换；2+1+2=5 | 标准完成 | 仅报告：受限固定模板/神经元replacement诊断不识别全LM公平因果 |
| [Guided Verifier v1](https://arxiv.org/abs/2602.04290v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:31+08:00 | policy仅latest guide而frozen verifier读完整reason steps→guidance输入与reward评价不同view；1+2+2=5 | 标准完成 | 仅报告：局部guidance/RL组合；不采用一般error理论或完整latency保证 |
| [ORBIT v1](https://arxiv.org/abs/2602.04089v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:50:51+08:00 | 单episode采样→同task reset但保留跨episode history→训练单位与测试context适应分开；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 675段/2257注；root actual POST通过 |
| [One-DVA v1](https://arxiv.org/abs/2602.04220v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:52+08:00 | encoded latents训练decoder→预测latents exposure并冻结encoder适配→重建与生成质量分账；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 669段/927注；root actual POST通过 |
| [InterPReT v1](https://arxiv.org/abs/2602.04213v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:42+08:00 | 语言编辑可微policy结构、demo调整θ→结构与参数更新及summary披露不同职责；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 147段/1354注；root actual POST通过 |
| [Competing Forecasts of AI Agent Performance v1](https://arxiv.org/abs/2602.04836v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:08:21+08:00 | 单增长曲线→base×reasoning竞争分解→in-sample fit不能验证未来平台或拐点；3+2+2=7 | 深入完成 | 仅报告：模型竞争假设与受限拟合不改变已核长期forecast结论 |
| [Fluid Representations in Reasoning Models v1](https://arxiv.org/abs/2602.04843v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:08:31+08:00 | 跨命名probe几何→matched/shuffled与早层随机干预→可编码不等自然使用或唯一symbolic原因；3+1+3=7 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 211–236/327–338证据阶梯与functional-subspace |
| [When AI Persuades v1](https://arxiv.org/abs/2602.04003v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:48:55+08:00 | fluent解释保留对错误输出的自报trust→human-facing攻击观察与预测/解释混杂分账→信任不等实际决策effect；2+2+2=6 | 深入完成 | 仅报告：受限人类实验不识别framing-only因果或新的普遍用户规则 |
| [The Missing Half v1](https://arxiv.org/abs/2602.04196v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:18+08:00 | deployment内容安全不能覆盖训练run→环境/奖励/monitor人口改变隐式风险观测→训练权限与release验收分责；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) training-run containment、release与effect分权 |
| [Toxic Proactivity v1](https://arxiv.org/abs/2602.04197v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:20+08:00 | dilemma多步模拟→终局toxic action与失败尝试分开→feedback同时改变执行路径不能独归monitor；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 755–766阶段责任与whole-harness反事实边界 |
| [From Assumptions to Actions v1](https://arxiv.org/abs/2602.04326v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:56:22+08:00 | 单计划隐含假设→scenario树与询问/行动效用比较→belief与query成本不能充事实或optimality；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING，[Ch79](../../../../books/part-07-agent/79-planning.md) 43–58/218–232 belief/unknown/query预算 |
| [CoLT v1](https://arxiv.org/abs/2602.04246v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:54:27+08:00 | main seed→外部decoder展开文本再回main→中间展开成本与decoder/context接口分账；2+2+2=6 | 深入完成 | 整合：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md) 283段/419注；root actual POST通过 |
| [AgenticVerifier v1](https://arxiv.org/abs/2602.04254v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:54:39+08:00 | 静态test输入→learned proposer主动找输出分歧→input validity/exec与output truth不同权；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1663段/5320注；root actual POST通过 |
| [KVSmooth v1](https://arxiv.org/abs/2602.04268v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:54:59+08:00 | KV-state近邻EMA与entropy适配→cache变换而非selection→主文row/算法column触发人口须绑定评价；2+2+2=6 | 争议 | 暂缓：中心entropy人口/queue/config与结果绑定未决，本窗安全终态隔离 |
| [Language Models Struggle to Use Representations Learned In-Context v1](https://arxiv.org/abs/2602.04212v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:40+08:00 | context语义可编码→有限下游部署失败与instruction/prefill接口差异→可读表示不等实际使用；2+2+2=6 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 211–244/basis与充分性-必要性 |
| [MiniRec v1](https://arxiv.org/abs/2602.04278v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:14+08:00 | reward learnability与HVP representativeness→RL数据选择代理→Hθ与hidden gradient空间须匹配；1+2+2=5 | 争议 | 暂缓：中心HVP空间/实现与结果绑定未决，本窗终态隔离 |
| [Contextual Drag v1](https://arxiv.org/abs/2602.04288v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:29+08:00 | wrong history结构继承→识错反馈未必恢复→reset/修复须独立质量验收；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) 560–562；Ch80 history/ECR/EIR交接 |
| [Proxy Compression v1](https://arxiv.org/abs/2602.04289v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:30+08:00 | 压缩proxy/byte联合训练→部署byte-only→训练符号与raw曝光/线上成本分账；2+2+2=6 | 深入完成 | 整合：MODEL-TOKENIZER，[Ch11](../../../../books/part-02-model/11-tokenizer.md) 126段/422注；root actual POST通过 |
| [CoFT v1](https://arxiv.org/abs/2602.04337v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:56:37+08:00 | dual prompt→样本依赖cutoff与peer选择→loss方向须支持可靠性sensor；1+2+2=5 | 争议 | 暂缓：Eq6 loss/sign与表结果绑定未决，本窗终态隔离 |
| [ActiveCLIP v1](https://arxiv.org/abs/2602.04340v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:56:41+08:00 | dual prompt clean proxy→human query与pseudo mining→loss/正确概率与人口分账；2+1+2=5 | 争议 | 暂缓：Eq5 loss/sign与表结果绑定未决，本窗终态隔离 |
| [SAGA v1](https://arxiv.org/abs/2602.04356v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:57:03+08:00 | 固定初始attention map→stagewise灰盒扰动转移→caption相似与安全越权/effect分账；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 587–600/705–733 attention sensor/组件access边界 |
| [SparVAR v1](https://arxiv.org/abs/2602.04361v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:57:09+08:00 | 固定网格flat ID→query区域/KV来源尺度坐标迁移→索引与近似residual重用分责；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 59段/1770注；root actual POST通过 |
| [Vision-aligned Latent Reasoning v1](https://arxiv.org/abs/2602.04476v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:59:47+08:00 | 每step latent与视觉teacher feature训练对齐→训练监督不等在线视觉重注入；2+1+2=5 | 标准完成 | 仅报告：局部latent训练case，长度切片与encoder组合不支持普遍视觉保真/缩放结论 |
| [Focus-LIME v1](https://arxiv.org/abs/2602.04607v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:02:53+08:00 | proxy先选邻域→inactive token固定、active局部扰动→解释对象与proxy准备预算改变；2+1+2=5 | 标准完成 | 仅报告：受限邻域诊断，不授human overlap为内部faithfulness或proxy必益 |
| [Disentangling meaning from language v1](https://arxiv.org/abs/2602.04613v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:03:02+08:00 | language/content双corruption与teacher-prefix观察位置→head steering分别验输出目标；2+2+2=6 | 深入完成 | 整合：MODEL-MULTI-HEAD-ATTENTION，[Ch15](../../../../books/part-02-model/15-multi-head-attention.md) 287段/345注；root actual POST通过 |
| [Transformers perform adaptive partial pooling v1](https://arxiv.org/abs/2602.03980v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:48:23+08:00 | GPT2受控二元context频数/类型/变异→跨context pooling随训练改变→相似不等唯一Bayes机制；2+1+2=5 | 标准完成 | 仅报告：有限synthetic学习case，不改自然语言最优性或已核表示结论 |
| [Partial Ring Scan v1](https://arxiv.org/abs/2602.04170v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:52:43+08:00 | ring内部causal SSM聚合与partial channels→顺序/旋转及过滤配置改变→invariance须成立；1+2+2=5 | 争议 | 暂缓：中心zero-initial SSM均值不具所述order-invariance，配置与表绑定未决 |
| [Scene-Responsive Human-in-the-Loop Motion Planning v1](https://arxiv.org/abs/2602.04184v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:02+08:00 | passenger指令→离线10步trajectory与tail失误→提示效果/均值改善不等闭环安全；2+1+2=5 | 标准完成 | 仅报告：局部离线prompt/轨迹case，不授真实控制或语言因果 |
| [Scalable Interactive Oversight v1](https://arxiv.org/abs/2602.04210v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:53:38+08:00 | 递归闭合action树+在线feedback reward→意图elicitation与真值监督边界；2+1+2=5 | 标准完成 | 仅报告：synthetic PRD与局部user-feedback训练，不改变通用oversight保证 |
| [VideoBrain v1](https://arxiv.org/abs/2602.04094v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:50:58+08:00 | 主动读取类别来自base/teacher答题差异→训练label不等证据充分→索引与forward成本需另计；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) active-observation label段；root actual POST通过 |
| [Empirical-MCTS v1](https://arxiv.org/abs/2602.04248v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:54:30+08:00 | 经验bank与prompt/judge共同演化→MCTS value/visit须绑定统计人口→相对排序不是正确概率；2+2+2=6 | 深入完成 | 整合：AGENT-PLANNING，[Ch79](../../../../books/part-07-agent/79-planning.md) 257段/500注；root actual POST通过 |
| [AgentOmit v1](https://arxiv.org/abs/2602.04284v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:23+08:00 | 原view下omit决策→压缩view下successor→old/current概率与obs loss mask不能换condition；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 677段/2619注；root actual POST通过 |
| [Group-Evolving Agents v1](https://arxiv.org/abs/2602.04837v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:08:22+08:00 | group汇集code/trace经验→每member改自己artifact→共享经验不授共享代码或成员共同正确；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) 848段/1245注；root actual POST通过 |
| [How Few-shot Demonstrations Affect Prompt-based Defenses v1](https://arxiv.org/abs/2602.04294v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:37+08:00 | demo与prompt defense交互反向→RoP/ToP不共享稳定选择规则→模板与population需分账；2+2+2=6 | 深入完成 | 仅报告：局部prompt×demo反证不识别framing-only机制或可移植选择规则 |
| [Beyond Static Cropping v1](https://arxiv.org/abs/2602.04304v1) | 2026-02-05T09:00:00+08:00～2026-02-05T10:55:51+08:00 | ±query双prefill首step正差→固定区域selector→同box VAT是另一个logit对象；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) VAQ静态crop段；jan02_v3 actual POST通过 |
| [MetaJudge v1](https://arxiv.org/abs/2602.04649v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:03:53+08:00 | 公开rationale atomic units→matcher与参考人口覆盖测量→coverage不等内部faithfulness或事实真值；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 3500段/5324注；jan02_v3 actual POST通过 |
| [LiteToken v1](https://arxiv.org/abs/2602.04706v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:05:15+08:00 | input merge graph递归拆/重merge→output禁emission不改ARprefix→词表两artifact与KV责任分开；2+2+2=6 | 深入完成 | 整合：MODEL-TOKENIZER，[Ch11](../../../../books/part-02-model/11-tokenizer.md) 93段/426注；jan02_v3 actual POST通过 |
| [Alignment Drift in Multimodal LLMs v1](https://arxiv.org/abs/2602.04739v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:06:01+08:00 | paired text/image与伤害/拒答测量→运行人口与主附表不一致→跨代drift排名不能自证；2+2+2=6 | 争议 | 暂缓：中心ASR人口/ordinal-binary模型与API运行绑定争议，本窗终态保留 |
| [When Silence Is Golden v1](https://arxiv.org/abs/2602.04755v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:06:24+08:00 | temporal支持与拒答reward→跨OOD abstention反侧→gold移除改变任务人口；2+1+2=5 | 深入完成 | 仅报告：局部temporal reward/abstention反证不提供通用honesty或confidence规则 |
| [OmniSIFT v1](https://arxiv.org/abs/2602.04804v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:07:35+08:00 | 先压缩video→audio Q读取selected visual KV→依赖selector使两模态预算不可独立验收；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 402段/OmniSIFT源注；jan02_v3 actual POST通过 |
| [SE-Bench v1](https://arxiv.org/abs/2602.04811v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:07:45+08:00 | 训练有doc/部署无doc→knowledge internalization与rollout objective身份分开→literal clip/IS中心未绑定；2+2+2=6 | 争议 | 暂缓：中心loss/ratio处理与ablation配置绑定未决，本窗终态保留 |
| [Decomposed Prompting Does Not Fix Knowledge Gaps v1](https://arxiv.org/abs/2602.04853v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:08:45+08:00 | gold DSL分解→几种调用view与agreement→拒答sensor非校准正确概率；2+1+2=5 | 标准完成 | 仅报告：人工oracle/历史与预算不同的局部评价，不授部署confidence或幻觉消除 |
| [CoT is Not the Chain of Truth v1](https://arxiv.org/abs/2602.04856v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:08:50+08:00 | 可见CoT风险与final拒答分离→hidden g扰动不等真实输出effect→安全率/定位中心需绑定；2+2+2=6 | 争议 | 暂缓：标签人口/hidden sensor与输出、Eq1/Table2定位配置未绑定，本窗终态保留 |
| [Reinforced Attention Learning v1](https://arxiv.org/abs/2602.04884v1) | 2026-02-05T09:00:00+08:00～2026-02-05T11:09:29+08:00 | 优化attention regularizer→PPO目标与loss方向须一致→center objective/config到结果尚未绑定；2+2+2=6 | 争议 | 暂缓：中心loss方向/τ配置与所报结果未绑定，本窗终态保留 |

## 4. 证据与知识整合

### [Expert Selections In MoE Models Reveal (Almost) As Much As Text v1](https://arxiv.org/abs/2602.04105v1)

采用§3–6、§8–9的最小安全反证：attacker已获得per-token unordered top-k expert indices与兼容tokenizer，并可取得同家族文本—轨迹配对训练数据；联合序列decoder不需要router logits/weights/hidden states/expert outputs。作者评估gpt-oss-20b、32expert/top4/24层完整轨迹、32token prefill、100M训练与10M不重叠OpenWebText token；不把top1恢复数字授作自然发生率或通用plaintext泄漏。§9未测cross-model transfer、部分层重建和长窗口极限；side-channel实际获取是外部前提，§8污染模拟及padding/随机路由/重标记等防御没有给质量—性能tradeoff，也不是DP。证据缓存见[fresh core](../_sources/daily-20260206/feb06_initial4_core.jsonl)及[补充核心](../_sources/daily-20260206/feb06_initial_core_supplement.jsonl)。

Ch72原observable/canonical审计已列routing metadata，但未承载离散expert-choice本身是可训练内容编码的具体边界。已在canonical两段后→DP前写一段与章末源注（当前343/4002），保最小披露/访问隔离和防御成本。root实际读必要源与owner差额后授锁，实际正文/前后邻接及末注POST通过；未复现。

### [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/)

采用官方当前core L38–55：cyber dual-use intent难分；identity verification、enterprise team请求与邀请试点是actor资格及模型访问路由，参与者仍受Usage Policies/Terms约束，不是无限工具authority或安全保证。原RSS pubDate=`Thu, 05 Feb 2026 10:00:00 GMT`。当前Ch72 Policy-as-Data后message/actor/end-user/TAC责任段实际承载model sensor与确定enforcement、identity资格和effect scope分账；root原文/正文具体Existing Coverage通过。现有正文使用后来的GPT5.4实例，只引用其长期论点，不冒充本日TAC原release版本或首发证据。

### [ERNIE 5.0 Technical Report v1](https://arxiv.org/abs/2602.04705v1)

必要§3、§6（尤其3.3/6.4.2）核train-once-for-all的depth/expert-subset/top-k采样与子模型评价。主文75/25和消融80/20不是同一recipe，子模型成本/质量不能授任意免费profile。Ch21 255–266实际四元profile、path sampling与逐profile校准已承载具体机制；root必要原源/owner对读通过，已有覆盖，不强改Ch28。官方Blog date-only Feb6是另事件，不借论文推定给Blog补时刻。

### [Multi-Head LatentMoE and Head Parallel v1](https://arxiv.org/abs/2602.04870v1)

采用§3.1–3.4、§4.1–4.4及必要A/B：独立latent heads先all-to-all分头、再local routing/expert、最后逆交换；固定heads/shape下通信仅相对k为O(1)，设备P不超过heads且须可整除，还可组合EP，不是计算/总通信O(1)或全部负载无失衡。两次交换、投影和expert imbalance仍付费；H10080/NVLink、12layer/d1024/T2048、0.2B active与2.2–4.2B total、10B tokens局部评价不外推服务SLO，架构与kernel收益未独立归因。Ch36固定EP后668段新增架构替代边界，2024注；root actual662–675及末注POST通过，未运行可选代码。

### [Harmonia v1](https://arxiv.org/abs/2602.04595v1)

采用III-A、IV-C、V-A及质量反侧：K按token的channel分组，V按channel的sequence分组；增长残组暂存/临时转换供attention，组满最终转换commit。原文未明确残组特定高精度储存，不把该事实补造；“动态scale不改已提交组”写为工程合同而非作者已验证保证。RTL、28nm/300MHz/0.9V综合、PrimeTimePX VCD及HBM2 cycle/bandwidth模拟不是实芯片/生产Decode。Ch49格式grid后1643段及2609注，root actual1637–1652/末注POST通过；不采headline数字。

### [Likelihood-Based Reward Designs v1](https://arxiv.org/abs/2602.03979v1)

采用§2/Eq2–18、§3.1–3.4、A.1/Eq19–23、A.2/A.4：current-policy在sampled CoT后teacher-force参考答案，prob/logprob/meanprob/meanlog的长度与数值作用不同；完整θ-dependent reward期望梯度含score-function与direct derivative，detach改变估计并省略后者，二项分解非本篇首创。两3B模型/四datasets只支持受限reward比较；greedy/sample排序、长form CoT collapse近SFT、KL/长度/warm-start维持CoT非质量保证。A.2 Base-RL100/10/0 format reward与主文binary概述分开，不混唯一配方。Ch33 reward来源后66/68两段及2255注，root actualPOST通过；未复现。[补充原式](../_sources/daily-20260206/feb06_03979_supplement.jsonl)。


### [Survey Questions Credibility v1](https://arxiv.org/abs/2602.04033v1)

深入受影响§3.2 SelfCorrelation、§4/Table2/3及两个定点当前main代码。原定义为143问题两两Pearson correlation矩阵的Frobenius norm，但所报human约1.66、model .90～3.33：若按完整矩阵且每列有限非零方差、包含diag=1，则raw norm至少sqrt(143)，与这些单位不相容。需要明确normalized norm、去diag或子集等具体convention；这是一项条件性单位冲突，不能据此称全部边际问卷实验伪。current-main compare_survey_and_model.py只有MSD/KLD/std/χ²，plot_self_correlation.py含corr()与去diag热图但未给绑定exact-v1排行的norm/normalization，不冒称实现复现或代码等同稿件版本。原机制缓存[feb06_core_03979_04033](../_sources/daily-20260206/feb06_core_03979_04033.jsonl)，两个限定原文件[feb06_survey_metric_code](../_sources/daily-20260206/feb06_survey_metric_code.jsonl)。root已实际核§3.2/§4/Table2/3，精准中心争议终态隔离通过；不采用相关结构强弱/排行，不把成熟边际与联合差异重复写Books。唯一重开条件：exact-v1 metric convention及与所报结果的绑定计算，或具体勘误；不扩repo。

### [VTok v1](https://arxiv.org/abs/2602.04202v1)

采用§3.1/3.2首帧keyframe与特征差分motion latent、§4.1/4.2受限共享理解/生成接口。冻结CLIP与DiT、另WAN适配分开，不授pixel-lossless/AR可执行vocab协议。§4.4 16spatial/5sec24FPS/46tokens与Table5时序配置不混成唯一压缩recipe。Ch23 577–606已具体承载scene/motion分解、时间identity和变化引起的invalidation；root必要原源/owner标准Existing通过，仅采用此论点，不声称正文已覆盖TVAlign、精确46token或全部decoder公式。[原核心](../_sources/daily-20260206/feb06_core_04202_04297.jsonl)。

### [Prompt Underspecification v1](https://arxiv.org/abs/2602.04297v1)

采用§3–5：label-subset argmax可以忽略全词表label概率质量，自由生成的缺label/multilabel是另解析事件；instruction prompts未统一改善，Ridge probe可读性不证明模型内部因果使用。Ch66 386–405已有prompt variants/invalid parse/abstain与同输出位置评价分账，root必要原源/owner标准Existing通过；不把自由输出与label logits变化直接当知识变动，不授普遍prompt证书。

论文公开时间为逐项条件联合推定，不是严格公告日志：保原v1 Submitted、v1 Updated、Available=2026-02、created/registered及findable字段，[首四原值](../_sources/daily-20260206/feb06_first4_date_fields.json)与[后续具名原值](../_sources/daily-20260206/feb06_potential_date_fields.jsonl)。官方availability排程给条件性最早announcement计划Feb5 01Z，已findable DOI registered加一秒仅作公开上界；各月字段和版本字段相容且无已见更早原公开线索。Submitted本身不能证明accepted、Updated/registered都不等于首公开时刻，根据信号冲突只重开受影响个体，不由代表或同批日期授全部落窗。

### [Vision vs Text Working Memory v1](https://arxiv.org/abs/2602.04355v1)

采用exact-v1 Method(Sx2)/Eq1、Results(Sx3.3–3.4)与Discussion(Sx4)：配对同一n-back刺激、forced m/−输出与两标签log-probability差，冻结evidence后改用不同lag标签重算AUC，诊断错误时间关系与阈值bias，不算重新遵从原任务。readability位置识别并非完美，recent-repeat lure须分层；视觉86tokens和ASCII不同长度也不等预算。50×24序列、Qwen/Llama局部模型及固定256像素网格不证明内部memory容量、架构唯一因果或所有视觉输入无效。必要原源见[feb06_framing_lag_core](../_sources/daily-20260206/feb06_framing_lag_core.jsonl)，原空S3 selector已定点恢复，未用空缓存授证据。Ch66任务难度切片后122段新增同evidence错误依赖诊断与边界，4289末注；root必要源/owner及实际正文、前后邻接/末注POST通过，未复现。

### [Fine-Grained Activation Steering: Steering Less, Achieving More v1](https://arxiv.org/abs/2602.04428v1)

采用§3–5及Appendix B/C的有限scalar-granularity分支：AU是输入scalar×权重列；对比pairs的activation差符号一致性用于排序选取，再按排名缩放当前activation，不能与head/neuron/SAE feature混同，也不是内部唯一因果。负γ足够大时1+γ可以变号，k/α随任务校准；部分utility退步与selection/白盒校准成本保留，激活单元数和异硬件引用不作端到端速度证据。原核心见[feb06_core_04428_04509_04521_04541](../_sources/daily-20260206/feb06_core_04428_04509_04521_04541.jsonl)，必要反侧见[feb06_AUS_necessary_supp](../_sources/daily-20260206/feb06_AUS_necessary_supp.txt)。Ch15 287段及341注，root实际method/eval与owner差额核后授窄写，actual279–299邻接与源注POST通过，未复现。

### [Model-Dowser: Data-Free Importance Probing to Mitigate Catastrophic Forgetting in Multimodal Large Language Models v1](https://arxiv.org/abs/2602.04509v1)

采用§3.1–3.3、§4与A.4/E.2/G：冻结base从随机词表种子生成文本，以随机反向投影估计输出敏感性并选每层底ρ可训mask；这是一组synthetic功能proxy，不是当前适配gradient人口或原训练语料等价。L1一阶界不授随机估计精确ranking/有限步无遗忘，梯度屏蔽不自动冻结AdamW最终delta。N/R准备成本、静态陈旧、有限retain反侧及A100/H200条件保留，不合并CIDEr/EM的H-score或泛称加速。必要补充见[feb06_Dowser_necessary_supp](../_sources/daily-20260206/feb06_Dowser_necessary_supp.jsonl)。Ch29 813段及1214注置于动态mask后→搜索synthetic保护gradient前，root actual802–822邻接与源注POST通过。

### [Rethinking Weight Tying: Pseudo-Inverse Tying for Stable LM Training and Updates v1](https://arxiv.org/abs/2602.04556v1)

采用§3–5与[A.3实现](../_sources/daily-20260206/feb06_PIT_implementation_supp.jsonl)：E=ZT^-1、Wout=TZ^T在Z列正交/T可逆时给WoutE=Id，EWout=ZZ^T不是IV；仅线性hidden/logit接口，不继承softmax/token/语义逆。Teacher polar U/T=I改变旧lookup，default freezeZ/trainT、FP32solve/额外hT与conditioning付费；可训Z的polar维护与ridge数值近似不授exactStiefel。A.3把L对角clamp称为T eigenclamp一般不等价，不采用；Table1 scratch全退步/teacher590及LoRA反侧不授普适质量稳定，构造alignment值不是独立质量证据。原必要core见[feb06_fusion_supp_PIT_core](../_sources/daily-20260206/feb06_fusion_supp_PIT_core.jsonl)第二行。jan01_v3实际必要原源与Ch12 tying/factorization写前独立核通过；root授158–165/375注窄写，作者已实写；root实际读取Ch12 135–170与375源注，actual POST通过，日级Gate未验。

### [DeFrame v1](https://arxiv.org/abs/2602.04306v1)

采用exact-v1 §3–4、限制与A.2：70Decisions负framing以no映射favorable，bias绝对幅度近似也可伴随受偏好对象反转；BBQ与DoNotAnswer的脆弱framing方向不同，不能统一为某极性更危险。双framing整合/guideline/self-revision总4 calls，baseline1/2/3；温度.8/top-k40/top-p.9，BBQ/DNA三runs与70Decisions单run分开。低framing disparity不授答案真值/公平保证或内部机制归因。必要原源见[feb06_framing_lag_core](../_sources/daily-20260206/feb06_framing_lag_core.jsonl)。jan01_v3实际必要source→Ch66 variants具体gap核通过，root授窄写；作者已写390段/5276注，jan01_v3 actual POST通过。

### [Trajectory Fusion v1](https://arxiv.org/abs/2602.04391v1)

采用§3–5/§7及A.1.2–A.1.3：按error-rate与不同错误final answer数决定k，按final answer分组优先频繁/短轨迹；固定reflection与correct轨迹拼成一条assistant response，全response NTP包括wrong前缀，区别于失败历史只作条件/expert恢复位置loss。全wrong题Implementation排除，不称无correct也可生成有效训练；final-answer verifier不证过程真实，固定reflection不是独立诊断。长序列与采样付费，同题数不等token预算，k饱和与teacher context confound保留，Pass@1 Avg16不是Pass@16。原源见[feb06_core_04391_04399](../_sources/daily-20260206/feb06_core_04391_04399.jsonl)及[feb06_fusion_supp_PIT_core](../_sources/daily-20260206/feb06_fusion_supp_PIT_core.jsonl)首行。jan01_v3实际必要source→owner核通过，root授窄写；Ch29 expert恢复后156段/1218注已实写，jan01_v3 actual POST通过。

### [$C$-$ΔΘ$: Circuit-Restricted Weight Arithmetic for Selective Refusal v1](https://arxiv.org/abs/2602.04521v1)

深入受影响S3.2/Alg1、§5及A.3/A.6：同harmful prompts的refusal/compliance分支训练只在选择mask上更新，再差分/缩放合成artifact；主文per-layer topκ与AppC global topκ/排首层不一致，中心选择人口及结果配置未解。Eq3 KL(refuse)−KL(comply)方向与prose不合，但后续mean-absolute归因可能消除符号，不能据此断全部实验无效；gradientmask不授所有optimizer最终delta保证。Table13 Gemma3-12B All OOD基线62.27与多个steered52.5/37.95等为明确反侧，不授allOOD提升；utility<1%宣传也不覆盖Crime61.7→55.7。原源见[feb06_core_04428_04509_04521_04541](../_sources/daily-20260206/feb06_core_04428_04509_04521_04541.jsonl)、[necessary](../_sources/daily-20260206/feb06_Cdelta_necessary_supp.jsonl)与[mask/eval](../_sources/daily-20260206/feb06_Cdelta_mask_eval_supp.jsonl)。root实际上述决定性原段/Table13核后认可原6中心争议终态，不入Books/正面安全或性能证据、不支撑无遗漏。重开只需actual mask convention/config、objective与所报结果绑定或勘误，不请求全部附件。

### [LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding v1](https://arxiv.org/abs/2602.04541v1)

采用§3–4：dense head选indices给下一层同head，sparse head继承不刷新，首层全dense；完整KV仍驻留，减少selected read不等容量删除。HardKuma训练混合两map并蒸馏teacher logits，部署按期望>.5固定角色；expectedL0不授每run严格budget/attention等价。A10080 Passkey/Booksum与LongBench局部质量退步、A800 partial-head未快于dense kernel及selector/gather付费保留，不采allhead速度为端到端TTFT/SLO。原源见[feb06_core_04428_04509_04521_04541](../_sources/daily-20260206/feb06_core_04428_04509_04521_04541.jsonl)。jan01_v3实际source→Ch45 FASA后具体gap核通过，root授窄写；190段/2060注实写，jan01_v3 actual POST通过。

### [Textual Planning with Explicit Latent Transitions v1](https://arxiv.org/abs/2602.04557v1)

采用§3–5：冻结encoder、128投影与轻量action-conditioned transition用InfoNCE训练；9 PDDL域/67 problems/最优轨迹导出样本，以gold successor+127 distractors候选测命中。PlanVariant每步teacher-forced gold状态，不等free-running rollout或环境闭环；跨域distractor与同problem distractor难度不同，最佳配置/3seed与backbone条件不能证明所有latent planner不可能。原核心见[feb06_embedplan_SSD_core](../_sources/daily-20260206/feb06_embedplan_SSD_core.jsonl)首行。jan01_v3实际source/Ch25 target-index、输入真值/自产预测及gradient分账（319–321）、imagined-vs-execute（327–338）与Ch79 oracle依赖/终局验证核通过，具体Existing仅采用teacher-forcing指标不继承真实规划保证；不称精确128候选recipe或全部架构已覆盖，不改Books、不把非作者身份写成root全源审阅。

### [Swordsman v1](https://arxiv.org/abs/2602.04399v1)

采用exact-v1 §3.1–3.3/Eq13–16、§4.1–4.3/Table1与§5：已解前块条件下重新forward残余位置，以最大正熵shift提下一块边界，低于阈值则合尾；当前块起始平均熵相对截至当前最大块平均熵与块内熵变化另调unmask门槛。两个控制对象不能混为单一历史confidence。语义边界解释依赖有效词表近似均匀、块内平滑及搜索空间扩张假设，不授semantic independence/cache exactness/正确性。三DLM/H200/长度512、固定块32；Table1部分MBPP/MATH退步、AdaBlock引用非本地重放与额外重分块forward/cache/校准成本保留，不采普遍质量/吞吐保证。原核心见[feb06_core_04391_04399](../_sources/daily-20260206/feb06_core_04391_04399.jsonl)第二行。jan01_v3实际source→Ch24 fixed/confidence控制接口差额核通过；root在DCD写后通过并释放锁后授本段，作者已写260段/1526注；root实际读取255–266/1526注，actual POST通过，未复现。

### [Semantic Self-Distillation for Language Model Uncertainty v1](https://arxiv.org/abs/2602.04577v1)

采用§2–5：固定LM的prompt末hidden→PCA16/条件MDN拟合每题32 teacher completions embedding，Rényi2分布dispersion、candidate likelihood、centroid是三个对象。稳定错teacher分布不是真值；匹配答案对比随机他题OOD不能替正确性，centroid不当答案/动作。7模型TriviaQA4k/1k局部，PCP/SEP平均排序高于SSD，单forward不是硬件真实latency。原核心见[feb06_embedplan_SSD_core](../_sources/daily-20260206/feb06_embedplan_SSD_core.jsonl)第二行与[feb06_SSD_method_supp](../_sources/daily-20260206/feb06_SSD_method_supp.jsonl)。Ch66 graph-agreement仅已承载实采样的一致性，缺生成前蒸馏分布三个接口与paid准备分账；jan01_v3实际necessary source→owner核通过，root授窄写；2041段/4297注；root actual POST通过，未复现。

### [Trust The Typical v1](https://arxiv.org/abs/2602.04581v1)

深入受影响§3–5/C.4/D：三encoder下benign参考几何/PRDC、GMM/OCSVM仅提典型性/OOD风险，Recall/Coverage依测试cohort，不等单请求安全概率；HH-RLHF近OOD约.5反侧不授语义相近内容可靠区分。main与C.4 reference混合口径、positive-gap负式及D prose20tokens/Table5 20words冲突不自选修补，正文不采精确interval。OPT125M/H200/vLLM0.10.2/batch32流式局部不授生产低延迟；三encoder、reference维护及batchlag付费。原源[feb06_T3_core](../_sources/daily-20260206/feb06_T3_core.jsonl)、[C.4/D](../_sources/daily-20260206/feb06_T3_streaming_supp.jsonl)。Ch72已有learned sensor→policy→enforcement，但缺benign-only典型性与cohort身份接口；jan01_v3实际必要source→owner核通过，root授831段/3010注窄写；root实际831段/邻接/3010注POST通过，不授通用安全，未复现。

### [Active Epistemic Control v1](https://arxiv.org/abs/2602.03974v1)

采用exact-v1 §3–6：grounded fact store与belief store分开，预测只剪候选，commit需grounded precondition coverage及独立compatibility check；unknown不当false。所述风险界依赖initial facts/query soundness与sound verifier等条件，query不可逆、过时或返回错误时不能由belief校准补保证。ScienceWorld split与“non-iterative”/后续iteration口径不一致留作作者结果限制，不采用性能数字。原核心见[feb06_core_03974](../_sources/daily-20260206/feb06_core_03974.jsonl)。root实际§3–6与Ch79 54–58/70–72/218–232核通过，现query/grounded facts—belief分责、独立commit verification及budget/freshness已承载本次采用论点；不称正文有精确epsilon/tau控制器、不制造重复diff。

### [Adaptive Test-Time Compute Allocation v1](https://arxiv.org/abs/2602.03975v1)

标准必要§3–6已读：deterministic structured-move feasibility不是全局soundness；frozen embed/MLP state-distance与residual scorer、uncertainty调k是具体候选机制。但§5.3明确majority voting不使用verifier，Table1却给其64 verifier calls，generation/verifier成本人口与所报节省映射未明。Eq14 beta符号未披露不推成实现反号，score标准差不等top-gap；joint residual+k消融也不隔离k的因果收益。原核心[feb06_core_03975](../_sources/daily-20260206/feb06_core_03975.jsonl)，root实际§3–6核后原6中心争议终态通过；不入Books/正面效率保证，不宣称全部作者实验无效。唯一重开：精确k/beta实现配置与generation/verifier调用口径绑定所报结果，或具体勘误。

### [Monitorability as a Free Gift v1](https://arxiv.org/abs/2602.03978v1)

深入采用§3/4.2/5.1/6、A.2/B.2/B.3/B.8/C.1的受限训练对照和测量接口：任务/格式reward训练未显式优化monitorability，能力与检测分可不同步，训练数据改变其局部轨迹。IF级联600+600与其他800步不等预算；attention/entropy相关不识别唯一原因。提示有/无配对生成与TE筛选定义条件人口，不是全部请求危险发生率；draft—后续答案一致性及强teacher替换只测特定接口，非整个reasoning内部因果忠实。正文TPR×TNR概述与B.2具体式不混算、不采用未核数字。原核心[feb06_core_03978](../_sources/daily-20260206/feb06_core_03978.jsonl)、[必要补充](../_sources/daily-20260206/feb06_monitorability_supp.jsonl)。Ch72原四轴/两代checkpoint比较后792/794两段及3014注补齐训练身份与条件人口分账；root实际必要原源/owner及772–806正文邻接/末注POST通过，原8不变，未复现/日Gate未验。

### [Claude Opus 4.6 release](https://www.anthropic.com/news/claude-opus-4-6)

采用官方release核心34/44的adaptive thinking与developer effort公开接口，不把产品排行、未披露内部决策或后期安全案例当新增机制。原datePublished=2026-02-05T18:00:00.000Z，dateModified=2026-09-09T21:28:45.000Z，[字段](../_sources/daily-20260206/feb06_opus_release_date_fields.json)支持本窗release归属；当前页面不证明初版逐句措辞。当前card p11四档仅辅助解释当前接口；p103+ overagentic/partial-prefill等条款事件时间不明，终态隔离不采为Feb5事实，不扩213页，重开需初版或具原始事件时间条款。root实际release34/44、currentcard p11及Ch56 319–337核通过，现route/effort policy、reasoning tokens/stopping、tool/harness身份与实际成本归因已具体承载，Existing只限此命题，不称全card已审或release全部能力已覆盖。

### [OMG v1](https://arxiv.org/abs/2602.04144v1)

采用exact-v1 §3.3–3.6及必要评测：planner/retriever形成外部特征，深/浅两路注入并用Tweedie恢复与task CE训练；cosine对齐不是物理恢复或正交独立保证。MOSI/MOSEI、BERT/Facet/COVAREP与五次运行的局部结果及mask recipe口径保留，不采用通用模态解耦或完整端到端成本。原[feb06_ambiguity_core](../_sources/daily-20260206/feb06_ambiguity_core.jsonl)；root实际必要方法/评价核后原5标准仅报告通过，局部组合不改变现有长期知识，不为案例另写Books。

### [Bi-directional Bias v1](https://arxiv.org/abs/2602.04398v1)

采用exact-v1 §3/Eq5–9、必要§4–6：最后projection的IG归因、固定neuron replacement、forward demographic entropy与backward cue divergence度量不同对象。GPT-4生成cue pool、固定templates与Pother处理改变测量人口；DIG与同超参50随机对照反侧保留，不授所有utility/群体公平或归因即内部因果。原[feb06_ambiguity_core](../_sources/daily-20260206/feb06_ambiguity_core.jsonl)；root实际必要方法/固定干预与直接反侧核后原5标准仅报告通过，不把有限诊断强改为普遍Books机制。

### [Guided Verifier v1](https://arxiv.org/abs/2602.04290v1)

采用exact-v1 Eq7/8及§3–4、§4.5 overhead/4.6顺序消融：可训练policy消费最新guide，冻结verifier读全部reason steps但不读guides；不把两者输入人口混为同一conditioning。教师标注、裁剪筛选、额外参数/输出tokens不等完整latency；naive verifier退步及顺序消融条件保留，不采Eq10梯度式或一般error定理。原[feb06_Guided_deciding_core](../_sources/daily-20260206/feb06_Guided_deciding_core.jsonl)；root实际准入/必要方法和成本反侧核后原5标准仅报告通过，未复现。

### [ORBIT v1](https://arxiv.org/abs/2602.04089v1)

采用exact-v1 §2–5：固定MDP的P/r，多episode间reset初始状态而保留history；训练按完整trace成功次数比较，测试冻结θ，适应只发生在context。三episode、32K历史、训练/测试环境与模型/checkpoint选择不同，不证明等总预算优势；作者GRPO不能dense的泛化不采用。原[feb06_core_04089](../_sources/daily-20260206/feb06_core_04089.jsonl)。Ch33既有single-episode identity未承载reset与retained input跨episode单位，675一段/2257注补齐；root实际必要源/owner及新增正文、前后episode→Measurement/末注POST通过。

### [One-DVA v1](https://arxiv.org/abs/2602.04220v1)

采用exact-v1 §3.1–3.3/3.5、§4.1/4.3/4.4：structural+variable query latents及阶段训练后，以预测latents适配decoder、冻结encoder保持坐标；更多decoder steps可改善感知指标而损失PSNR，生成表非全面优胜。额外48×80G及多阶段训练成本保留，不称sample/GT配对实现独立已审、所有artifacts消除或通用corrector。原[feb06_core_04220](../_sources/daily-20260206/feb06_core_04220.jsonl)。Ch23 train/inference mismatch后669段/927注是具体分布gap；root实际原源/owner及正文→connector邻接/末注POST通过。

### [InterPReT v1](https://arxiv.org/abs/2602.04213v1)

采用exact-v1 §3完整结构/参数/summary及§4.1/4.3与必要反侧：语言restructure feature/operator图、demo调参数，English summary只结构/constants，不覆盖全部训练权重。34人模拟器研究/结构化观测、无限制示教训练测试次数未隔离language-only因果；不授真机安全、world causal graph或actuator授权。原[feb06_core_04213](../_sources/daily-20260206/feb06_core_04213.jsonl)。Ch26 VLM controller→VLA间147一段/1354注补此更新职责差额，保额外成本/固定controller回退；root实际必要源/owner及正文/邻接/末注POST通过。

### [Competing Forecasts of AI Agent Performance v1](https://arxiv.org/abs/2602.04836v1)

深入采用exact-v1 §3–6：base×(1+reasoning)经link函数组合，latent components及thinking release feature不是直接观测能力；sigmoid inflection间隔假设才产生plateau形状，不识别真实原因。更大参数量、likelihood/log-horizon/horizon MSE目标不同，in-sample胜利未控制完整模型选择，也未做heldout future验证；June拐点与已验证platform plateau不采用。原[feb06_core_04836](../_sources/daily-20260206/feb06_core_04836.jsonl)。Ch7 215–242已分regime/heldout/model selection，root实际模型/拟合条件/正文核后原7深入仅报告通过，不以竞争解释改长期预测。v2 Submitted相交但Updated Feb9不当本窗公开修订。

### [Fluid Representations in Reasoning Models v1](https://arxiv.org/abs/2602.04843v1)

深入采用exact-v1 §2.2–2.3/3/4/6、必要A.7/A.11：QwQ32B受限BlocksWorld命名/trace配对、base喂入同traces的几何、norm-preserving patch与matched-vs-shuffled控制。早层随机noise也帮助、constant vector仍有accuracy、晚层shuffled反侧不支持唯一symbolic电路或普遍层解释；A7 random/shuffled表述差异不分派2.9%数字。原[feb06_core_04843](../_sources/daily-20260206/feb06_core_04843.jsonl)。root实际主文必要干预/控制及Ch5 211–236证据阶梯、327–338 sufficient≠necessary核后原7具体Existing通过；A7/A11由作者实际定点核，不称root全部附录已读。

### [When AI Persuades v1](https://arxiv.org/abs/2602.04003v1)

深入受影响exact-v1 §3–6：205名英语成年人、40题（10 benign/30 attack）测7点自报trust及rationale，不是实际选择或工具effect。§5.1 benign同时为正确prediction/解释、attack为错误prediction/同类解释，不能由结果识别framing-only因果；生成/投票/人工筛选与post-treatment rationale分组改变人口。4.53与4.59差异不显著不是等效/非劣证明，不采普遍用户规则。原[feb06_core_04003](../_sources/daily-20260206/feb06_core_04003.jsonl)；root实际§4.3/4.4、§5.1及§6.1/6.3独立核后原6安全深入仅报告通过，保留局部human-facing失败观察而不强造Books通用原则。

### [The Missing Half v1](https://arxiv.org/abs/2602.04196v1)

深入受影响exact-v1 §3–6及C/E/F必要段：108 prompts、每prompt最多20训练步或首个检测risk即停，run内any-risk是二值人口，不是每rollout发生率。非reasoning三runs/reasoning一run、750 GPUh及L1–3背景、L4环境能力、L5synthetic组织条件分开；autonomy层级不是severity。A3 file/storage实际状态检查、compute/memory的AST+intent标注和network AST不同，不能授真实网络exfil receipt。单60步IF case与系统奖励组合不识别所有训练普遍因果，不采用未核完整reward prompt。原[feb06_core_04196](../_sources/daily-20260206/feb06_core_04196.jsonl)与[CEF](../_sources/daily-20260206/feb06_04196_supp_CEF.jsonl)。root实际S3/4关键L1–5、IFcase与A3检查身份及Ch72 686–695 training run/独立release、755–766 proposal/authorization/commit与772–806 monitor条件人口核通过；具体Existing不称全taxonomy已覆盖。

### [Toxic Proactivity v1](https://arxiv.org/abs/2602.04197v1)

深入受影响exact-v1 §3–6：16 synthetic dilemmas、4域×2 incentive×2实例、3 benign/3 toxic/1 terminal工具、400 simulations/model与固定生成预算是人工冲突人口。MR只计终局toxic action，auxiliary failed attempts另计；模型环境模拟转移不是真实工具receipt或伤害。High-feedback拒绝与warning同时改变后续可执行路径，不是单monitor的独立因果，也不证明自然风险率/RLHF起因。原[feb06_core_04197](../_sources/daily-20260206/feb06_core_04197.jsonl)。root实际S3.3、§4.1及§5干预/执行路径与Ch72 755–766 attempt-vs-commit/effect分责、686–722 whole-harness反事实条件核后原6具体Existing通过，不需为未采用的精确intensity扩全部moderator prompts。

### [From Assumptions to Actions v1](https://arxiv.org/abs/2602.04326v1)

采用exact-v1 §3–6：LLM composer从trace/context形成有限scenario树、概率及收益；多个叶可同action，逐叶排名不等校准posterior/action聚合最优。False scenario的G=0是假设，询问与行动互斥/延迟及距离或消息长度成本改变比较对象。CWAH/TDW有限模型与任务，一些TDW配置token明显多于CoELA，不授全面成本优势；12人自报不是事实正确或真实控制安全。原[feb06_core_04326](../_sources/daily-20260206/feb06_core_04326.jsonl)。root实际完整§4、§5有限比较与Ch79 43–58 belief/unknown、218–232 act/ask/verify预算及Ch80 competing hypotheses核后原6具体Existing通过；不称Books已有Composer recipe、校准posterior或optimality。

### [CoLT v1](https://arxiv.org/abs/2602.04246v1)

采用exact-v1 §3–6：main model产生seed hidden，经projector/浅层自回归decoder展开可见文本再回main；默认Llama1B/一层decoder、GSM8K教师步骤、四80G训练配置，不继承全部loop可微。Eq4 seed/decoded记号不采用；#L估算包括附加主模型调用却不是完整decoder/回填/硬件latency。初始化不同和引用基线不授等所有预算，MATH及固定4tokens语义粒度反侧保留，可读不证明faithfulness。原[feb06_core_04246](../_sources/daily-20260206/feb06_core_04246.jsonl)。Ch18离散plan前缀后→latent分支前283段/419注新增接口替代分支，保发布identity、训练/decoder/重新Prefill成本与独立outcome/fullCoT回退；root实际必要原源/owner及正文/前后交接/末注POST通过。

### [AgenticVerifier v1](https://arxiv.org/abs/2602.04254v1)

采用exact-v1 §2–5完整必要输入鉴别/voting、训练/validator及直接反侧：learned generator多轮寻找候选pair执行不同的有效输入，reward区分invalid/same/different，无正确output oracle。教师/consensus有效性标签可错，投票cluster多数不授truth；两个official-suite正确程序新输入分歧不能判断哪一个真。教师60K轨迹/模型、SFT/RL与多轮执行成本保留，matched512 inputs不等所有调用/CPU或训练预算，Best@8非独立模型；medium30B随机baseline82.7高于80反侧不授普胜。原[feb06_core_04254](../_sources/daily-20260206/feb06_core_04254.jsonl)。Ch66 same-verdict后→形式建模前1663段/5320注补主动proposer/validity/exec-output truth三权，root必要原源/owner及实际正文/邻接/末注POST通过，未复现。

### [KVSmooth v1](https://arxiv.org/abs/2602.04268v1)

必要exact-v1 §3–6及A5完整Algorithm1/2：主§3.3 Eq5为当前query行entropy、Σj α(t,j)logα(t,j)，算法step4却Σi α(i,j)logα(i,j)并把列方向z(t,j)入queue；主k/M与算法k/|S|早期队列、先attention output后EMA亦须绑定实际evaluation配置。§4.1 Gaussian prior/likelihood的条件MAP可导EMA，但独立Gaussian随机变量乘积通常非Gaussian，不能把density乘积性质当attention/KV变换的Bayesian-optimal或因果证明。三7B系模型、greedy512、层3–31的作者局部表结果保留；OPOPE LLaVA accuracy退步及AMBER MiniGPT覆盖/CHAIR反侧不授全面quality/no-cost。原[feb06_core_04268](../_sources/daily-20260206/feb06_core_04268.jsonl)、[A5公式](../_sources/daily-20260206/feb06_KVSmooth_algorithm.jsonl)及[fresh完整A5](../_sources/daily-20260206/feb06_KVSmooth_algorithm_full.jsonl)。root实际主S3.3/S4.1与A5全算法独立核后原6中心安全保留通过，不入Books/正面机制/性能/安全证据，不称全部实验无效、不支撑无遗漏。唯一重开：row/column entropy及queue convention、实际实现/配置身份与所报结果绑定或勘误，不扩所有层/源码附件。

### [Language Models Struggle to Use Representations Learned In-Context v1](https://arxiv.org/abs/2602.04212v1)

深入受影响exact-v1 §2–6与A.D/F：有限图随机游走语义的hidden geometry可读，不保证next-token或adaptive-world任务实际部署；instruction与assistant-prefill是不同输入接口，长context或autorater grid不能充正确mapping/全部frontier inert。§4 DE越低越好，但walk/fewshot比值与“更差”方向未一致，该指标方向不采用；独立有限行为对照仍可保留，不把几何代理当内部因果。原[feb06_core_04212](../_sources/daily-20260206/feb06_core_04212.jsonl)、[必要A.D/F](../_sources/daily-20260206/feb06_04212_ADF.jsonl)。root实际S2/S3/S4任务、S5/6与Ch5 211–244及basis/充分性-必要性段核后原6具体Existing通过；现正文承载可读/可干预/自然使用分账，不称已覆盖本篇精确图任务。

### [MiniRec v1](https://arxiv.org/abs/2602.04278v1)

标准必要exact-v1 §3–6：proxy reward在中间区间取learnability，HVP对齐全局平均与greedy diversity构成选择；但§4.3 Eq9–12的H为参数θ Hessian，v为最终hidden-state gradient，未定义空间映射就不能相乘。§5.6 λ称参数平滑与方法中representativeness weighting身份亦不一致；不代作者补mapping、不把局部两Amazon/Gemma2B/Qwen3B作者结果全部作废。原[feb06_core_04278](../_sources/daily-20260206/feb06_core_04278.jsonl)。root实际Eq9–12及λ反侧独立核后原5中心终态隔离通过，不采用其“ideal optimization trajectory”、选择最优/加速保证或Books；唯一重开为实际HVP空间、实现设定和所报结果绑定或勘误，不扩repo。

### [Contextual Drag v1](https://arxiv.org/abs/2602.04288v1)

深入受影响exact-v1 §3–7：基于original表现的anchor与hard subset改变人口，failed-attempt context常使输出继承结构；TED测输出表达式树，不识别内部causal。外部错误反馈及posthoc正确self-verification子集均不能证明恢复部署保证，也不能直接同整组1F相比较。fallback SFT与denoising有局部改善、正确draft退步及额外调用成本，不授无代价清洗。原[feb06_core_04288](../_sources/daily-20260206/feb06_core_04288.jsonl)。root实际S3 eval/TED、S4.1/4.2、S6/7反证与Ch75 560–562 reset非clean两段、Ch80 history强化/ECR/EIR独立核后原6具体Existing通过；已有责任是reset/修复需独立质量验收，非声称书已承载本篇fallback训练recipe。

### [Proxy Compression v1](https://arxiv.org/abs/2602.04289v1)

深入具体接口缺口，exact-v1 §2/§3.1–3.4/3.6及负侧：sentinel/disjoint vocabulary交替学习压缩proxy/UTF8 bytes，paired warmup后取消配对，部署byte-only。固定symbols不是同raw exposure；0.5B反侧、gzip失败、compressed-gold oracle与normal-generation分账，不授神经无损或普遍快。原[feb06_core_04289](../_sources/daily-20260206/feb06_core_04289.jsonl)。Ch11 byte单位/UTF8合法性之间原无该分工，126一段/422注补齐；root实际原源、owner与正文/邻接/末注POST通过，准备、长Decode成本及旧byte/subword回退就近保留。

### [CoFT v1](https://arxiv.org/abs/2602.04337v1)

标准必要exact-v1 §3.1.2/3.1.3、§3.2/4/Table1/4：dual正负prompt取relative-cosine clean proxy后peer筛选，pseudo seeds/random complement与iterative/contrastive/LLM prompt共同改变训练。Eq6负真标签log概率加正log(1−complement clean概率)按最小化推complement概率上升，与noisy文字方向相反。不能自行补负号，也不由有限准确率授可靠sensor或确认偏差普降。原[feb06_core_04337](../_sources/daily-20260206/feb06_core_04337.jsonl)；root实际核心/Eq6与评价核后原5中心隔离通过，不全实验作废、不写Books。唯一重开：实际loss/sign/更新实现与所报表绑定或勘误，不扩repo。

### [ActiveCLIP v1](https://arxiv.org/abs/2602.04340v1)

标准必要exact-v1 §3–4/Table1–4：dual prompt相对cosine形成clean proxy，低分human query/高分pseudo mining；Eq5 −log p_clean(y)+log(1−p_clean(complement))按最小化推complement概率上升，与§3.2.1方向相反。六轮每轮1%annotation、三seed/单3090；full Ours联训与OursCoOp/VPT/MaPLe仅选样是不同人口，重复Ours列不指控伪结果。原[feb06_core_04340](../_sources/daily-20260206/feb06_core_04340.jsonl)。root实际Eq5/S4.1/S4.2核后原5中心隔离通过，不授可靠性sensor/Books；唯一重开为实际negative-prompt loss/sign/参数更新与表绑定或勘误。

### [SAGA v1](https://arxiv.org/abs/2602.04356v1)

深入受影响exact-v1 §2–4/A2完整Algorithm1/C1：一个初始attention map预建stage hotspots，不是每stage实时重抽。1000源图/随机目标caption、三CLIP surrogate与十target；ASR是gpt-oss20b caption相似分>.5，不是安全政策越权/真实harm，norm小不证明人眼不可察。hot/cold及extractor消融支持有限选择，ensemble未必改善，地图shift关联不识别唯一因果。原[feb06_core_04356](../_sources/daily-20260206/feb06_core_04356.jsonl)、[A2/C1](../_sources/daily-20260206/feb06_SAGA_algorithm.jsonl)。root实际S3/S4.1/S4.2/A2/C1与Ch72 587–600/705–733核后原6安全深入具体Existing通过；只采用sensor≠causal、access/目标输出≠effect分责，不称精确攻击recipe已有覆盖。

### [SparVAR v1](https://arxiv.org/abs/2602.04361v1)

深入采用exact-v1 §3–4、Appendix A.1 query/KV Decompose-Align-Project：扩尺度时query区域与历史KV来源尺度/局部坐标不能沿用固定flatID；稀疏pattern迁移与dense−sparse输出差额近似重用分责。必要原源见[feb06_core_04361](../_sources/daily-20260206/feb06_core_04361.jsonl)、[SparExtra](../_sources/daily-20260206/feb06_SparExtra_necessary.jsonl)。A.2 Eq4索引子命题与main flat-ratio/appendix配置未一致，不采用精确算法/复现保证；局部5.61x不是request收益。Ch24尺度历史后59段/1770注只整合qualitative坐标与近似reuse分工、gather/cache/校准成本和dense回退；root实际52–68正文/末注及Ch23末→Ch25入口POST通过，未运行或复现，不以正文采用消除公式争议。

### [Vision-aligned Latent Reasoning v1](https://arxiv.org/abs/2602.04476v1)

标准采用exact-v1 §3–4、A.1训练及必要B.1–3：每step生成latent，以训练期视觉encoder features对齐，encoder冻结、decoder/MLP训练；不是运行时重注入teacher feature或保证保留视觉真值。Qwen2.5-VL7B、两阶段同450K CoT及4A100训练是局部条件；生成长度posthoc切片不能识别多想因果收益，多encoder组合不授普遍视觉保真。必要原源见[feb06_core_04476](../_sources/daily-20260206/feb06_core_04476.jsonl)、[VaLRExtra](../_sources/daily-20260206/feb06_VaLRExtra_necessary.jsonl)。root实际§3/§4/A.1与Ch18视觉teacher约束段核后原5标准仅报告通过；只保训练case与评价边界，不称精确recipe已有覆盖、不强制改Books。

### [Focus-LIME v1](https://arxiv.org/abs/2602.04607v1)

标准采用exact-v1 §3全部方法/Eq3–4、§4.1–4.3直接反侧：proxy coarse-to-fine选择active邻域，target扰动只改active token，inactive token保静态，再局部回归；归因是这组条件邻域而非全输入/internal唯一因果。proxy准备成本不能因不新增target调用而抹去，without-proxy反侧及14B/32B、k50/100口径未一致留作headline限制，human evidence overlap不是内部faithfulness。原源见[feb06_core_04607](../_sources/daily-20260206/feb06_core_04607.jsonl)。root实际S3/Eq3–4及S4必要表/counter核后原5标准仅报告通过，不写普遍更忠实/更省预算的Books结论。

### [Disentangling meaning from language v1](https://arxiv.org/abs/2602.04613v1)

深入采用exact-v1 §3–6：含义相同/错语言与对语言/含义破坏是两个干预目标；patch clean head、teacher-forced参考前缀与观察token位置共同定义sensor，再分别验language/content输出。位置KL或可干预性不证明唯一language-independent code，token0、低资源语言与强α utility反侧限制部署，白盒pair/位置/强度校准付费。原源见[feb06_core_04613](../_sources/daily-20260206/feb06_core_04613.jsonl)。Ch15 conditional-head后→AU前287段及345注补具体双目标/观察位置接口；root实际275–301正文与345注POST通过，未复现。

这四个首次公开事件逐项采用相容v1 Submitted、February ID/Available月份、v1 Updated及findable注册上界的有说明联合保守区间，不称Submitted/注册即first-public。原字段见[last15](../_sources/daily-20260206/feb06_last15_date_fields.jsonl)与[additional7](../_sources/daily-20260206/feb06_additional7_date_fields.jsonl)：04361/04476注册Feb5 02:57:08Z/02:59:46Z，04607/04613注册03:02:52Z/03:03:01Z；表的秒精度上界加一秒仅为半开表示，最早计划条件为09:00+08，非精确发布日志。后期v2不回填本窗正文。

### [Transformers perform adaptive partial pooling v1](https://arxiv.org/abs/2602.03980v1)

标准采用exact-v1 [PDF](https://arxiv.org/pdf/2602.03980v1) p2–5方法/结果/讨论：GPT2受控二元输出、1000 synthetic context字符串、50次重复的频率/类型数量/异质性变化；跨context pooling随epochs变化与hierarchical regression相似，不识别自然语言最优性或唯一Bayes内部实现。HTML404未授全文受阻，原PDF由作者与jan01_v3实际必要核，后者独立p2–5读通过，原2+1+2=5标准仅报告，不为局部case重复长期学习原则。没有新的Books改动/复现。

### [Partial Ring Scan v1](https://arxiv.org/abs/2602.04170v1)

标准必要exact-v1 §3–4及zero-initial causal SSM条件显示中心order-invariance不成立：B=C=1、state系数.5时，input(1,0)输出均值.75，旋转input(0,1)均值.5；ring内取mean仍受causal scan顺序影响，交替方向不自行消去。partial-channel signed GAP与mean-absolute口径、参数27与22/30配置也未绑定同表。原[feb06_core_04170](../_sources/daily-20260206/feb06_core_04170.jsonl)，jan01_v3实际必要method/evaluation与反例核后原1+2+2=5中心暂缓通过；不入Books/正面rotation或性能保证，不断全部作者实验无效。唯一重开为实际ring aggregation/边界状态、channel score及配置与所报结果绑定，或勘误。

### [Scene-Responsive Human-in-the-Loop Motion Planning v1](https://arxiv.org/abs/2602.04184v1)

标准采用exact-v1 §III–V：OpenEMMA/LLaVA读取front-camera/ego-state与passenger式指令，离线生成10步speed-curvature trajectory，在849 doScenes annotated scenes计算ADE。posthoc剔除tail与提示phrase变化不能识别在线控制安全/语言独立因果；均值、极端值和单位6201.443口径不外推，20min与七日offline计算不是真实交互latency。原[feb06_core_04184](../_sources/daily-20260206/feb06_core_04184.jsonl)，jan01_v3实际必要source核后原2+1+2=5标准仅报告通过，未授真机/闭环保证，不制造Books差额。

### [Scalable Interactive Oversight v1](https://arxiv.org/abs/2602.04210v1)

标准采用exact-v1 §3–5及[评价补充](../_sources/daily-20260206/feb06_04210_eval_supp.jsonl)：37闭合actions递归elicitation和online UserReward−DontCare比例/分组whitening，与expert PRD judge形成局部监督；700 SFT、synthetic需求和一人10次user study不足以支持真实用户expert-equivalence或通用可扩展监督保证。原[feb06_core_04210](../_sources/daily-20260206/feb06_core_04210.jsonl)。jan01_v3实际necessary core/直接反侧核后原2+1+2=5标准仅报告通过，不因“监督”主题借成熟原则抬分，未改Books。

这四项原日期逐项见[feb06_potential_date_fields](../_sources/daily-20260206/feb06_potential_date_fields.jsonl)：03980/04170/04184/04210 v1 Submitted依次Feb3 20:05:01Z、Feb4 03:07:41Z/03:44:56Z/04:52:00Z，v1 Updated为Feb5 01:06:04Z/01:22:37Z/01:24:38Z/01:26:45Z，findable registered上界为02:48:22Z/02:52:42Z/02:53:01Z/02:53:37Z；February Available与ID月相容。按既述received/accepted条件排程与逐项注册上界取保守区间，不称注册即发布、Submitted即公开或机械同批推定，表上界一秒只为半开表示。后期v2不回填本窗。

### [VideoBrain v1](https://arxiv.org/abs/2602.04094v1)

必要§3–4及反侧：direct/adaptive/active按base/teacher及有无工具答题定义，both-wrong也可active，排除base-correct/teacher-wrong；类别不保证下一次读取恢复答案。全视频索引、额外模型forward/roundtrip不从帧数节省消失，固定采样有反侧。见[feb06_core_04094](../_sources/daily-20260206/feb06_core_04094.jsonl)。jan01_v3实际必要source→owner通过，root授Ch23现active-reading后窄段；root实际正文/邻接/末注POST通过。身份/读回guard是工程推导，未复现、不授无成本完整取证。

### [Empirical-MCTS v1](https://arxiv.org/abs/2602.04248v1)

必要§3–5/7的BT/Borda/NormalizedDominance比较、UCB选择和bank更新；UCB不是softmax，Table2不全Pareto。prompt/bank同时改不能识别memory单因果。见[feb06_core_04248](../_sources/daily-20260206/feb06_core_04248.jsonl)。Ch79旧replanning/statistics未具体承载strategy/judge/context snapshot；一段只补身份/冻结或失效与付费judge/bank成本、stateless回退，guard标工程推导。jan01_v3必要源/owner通过，root实际244–266/新257与末注500 POST通过；未复现。

### [AgentOmit v1](https://arxiv.org/abs/2602.04284v1)

必要方法/训练及反侧：counterfactual reroll thought为空或observation特殊标记，正确省略轨迹SFT对obs作loss mask；omit decision原condition与压缩后successor不同，压缩trace不替代原sampler oldlogprob。Eq4参考分布p(y)=0/优化ref不证明部署最优policy KL；不给错误轨迹省略收益不认证无rewardhacking。见[feb06_core_04284](../_sources/daily-20260206/feb06_core_04284.jsonl)。一段只补概率账与准备/parser/verifier成本和fullobservation回退，guard为工程推导。jan01_v3 source→owner通过，root实际670–689/新677/2619注 POST通过；未复现。

### [Group-Evolving Agents v1](https://arxiv.org/abs/2602.04837v1)

必要group reflection→各member code修改→sanity/archive和SWE/Poly分阶段eval；same child数不等反思、工具、训练/评测总cost匹配。见[feb06_core_04837](../_sources/daily-20260206/feb06_core_04837.jsonl)及[成本必要段](../_sources/daily-20260206/feb06_GEA_cost_core.jsonl)。Ch82 population flow未具体承载group经验与代码/成员验证；一段补parent/member/revision/test人口身份、paidreflection及失败保留parent，guard是工程推导。jan01_v3 source→owner通过，root实际838–858/新848/1245注 POST通过；未复现。

### [How Few-shot Demonstrations Affect Prompt-based Defenses v1](https://arxiv.org/abs/2602.04294v1)

必要§3–5/6.1/6.4与T8/T11/T13：Qwen ToP+FSG上升，T13 ToP+FS 84.8→93.2不支持一致退化；有限9模型/6攻击/三demo与QwenGuard人口。prompt内容/长度/位置未对齐，Bayesian/attention是假设而非因果机制。见[feb06_core_04294](../_sources/daily-20260206/feb06_core_04294.jsonl)。jan02_v3实际必要深入后OnlyReport通过：贡献是有用局部反证，但未形成稳定设计选择，不称已覆盖exactrecipe/普遍RoP优。未改Books/复现。

### [Beyond Static Cropping v1](https://arxiv.org/abs/2602.04304v1)

必要§3–5：attention正差经head/layer选box，在首prefill决定crop；VAT裁同box作logitcontrast，不是持续decode动态因果定位。2×4090并行、双显存和额外时间不消失，短答对照不授长答/SLO。见[feb06_core_04304](../_sources/daily-20260206/feb06_core_04304.jsonl)。jan02_v3 actual source/Ch23:428–461 gap通过，一段补双对象/映射/成本与full图回退；actual新段/crop前邻/可靠性后邻及源注POST通过。未复现。

### [MetaJudge v1](https://arxiv.org/abs/2602.04649v1)

必要§2–4/C1/D1/D2及Fig9完整prompt；GPT5拆分人工参考并筛93项、CW3503删207争议项是测量人口变更，judge稳定不等humantruth。见[core](../_sources/daily-20260206/feb06_core_04649.jsonl)、[必要补充](../_sources/daily-20260206/feb06_MetaJudge_necessary.jsonl)、[完整prompt](../_sources/daily-20260206/feb06_MetaJudge_prompt.jsonl)。Ch66 EvidenceTrail补一段referenceunit/matcher/output预算及人审成本、final-only回退，jan02实际source/owner与正文/邻接/末注POST通过。AP/RR子命题终态保留：Eq3 weightedmatching零边/非唯一tie后binaryhit无阈值，Fig9各ref best未禁复用，不能代补global1-to-1或奖励可靠保证；定点重开实际matching/threshold/reuse配置与对应结果或勘误。未复现，不断全部实验无效。

### [LiteToken v1](https://arxiv.org/abs/2602.04706v1)

必要机制与评测/配置：FI最终emission和neighborentropy选残留merge，输入递归split/remerge而输出mask列、不重merge生成prefix；保基本单元，Latin/C4有限人口。PPL token单位、生成confidence与真准确不同。见[feb06_core_04706](../_sources/daily-20260206/feb06_core_04706.jsonl)。Ch11固定vocab规则后补一段input/outputartifact与长序列/backendcost、原artifact回退；jan02_v3 source/owner及actual正文/邻接/注POST通过。threshold §6.2 T4 .25/正文.15、§6.6配置冲突子命题终态保留，不采用配置收益点；只以对应artifact/config→结果或勘误定点重开。未复现。

### [Alignment Drift in Multimodal LLMs v1](https://arxiv.org/abs/2602.04739v1)

exact-v1 [PDF](https://arxiv.org/pdf/2602.04739v1)必要§3–7 p2–6、D1/D2 p12–13及必要限制p19–20实际恢复，不是访问受阻；[必要定位](../_sources/daily-20260206/feb06_04739_necessary.txt)。726 US-English/363配对、两阶段17/12rater/API单turn。主§4.1 GPT4o .067/.043 vsD1 .09/.30，Claude<.03 vsD1 .05/.12；§3.4 ordinalCLMM与D2binaryGLMM混用且maxgrad.704未收敛。拒答列最低伤害类不等benignutility/API黑箱不识别架构原因。root实际必要PDF/core/Ch66refusal分账核后中心终态隔离通过，不入Books/跨代模态排名或定量drift因果，不断全部实验无效。只重开ASR事件/人口与主附表、ordinal/binary拟合收敛、API snapshot/run身份绑定或勘误。

### [When Silence Is Golden v1](https://arxiv.org/abs/2602.04755v1)

必要§3–7及完整AppendixL，见[core](../_sources/daily-20260206/feb06_core_04755.jsonl)、[L](../_sources/daily-20260206/feb06_04755_extra.jsonl)。time/KG过滤、CoT正确终局筛选、SFT+GRPO联合训练；格式.5/拒答1/答案最多2改变reward。HardFN/OODTP反侧，GPT3.5 Hard退步。L在12%MCQ删gold、另88%也删错项形成三选项，不是原MMLU/HellaSwag人口；不能由TP/FN授内部uncertainty。jan02_v3实际necessary/Ch66risk–coverage与Ch33reward核后Only通过：新增局部任务反证非可移植规则，预算/teacher成本分账，不称exactrecipe Existing。未改Books/复现。

### [OmniSIFT v1](https://arxiv.org/abs/2602.04804v1)

必要§3–4：同步twoframe spatial/temporal选择、compressed visualKV+audioQ/MLP/TopK/STE，107K paidSFT共同训decoder/VGAS；reverseOmniZip对照不同recipe不授方向唯一原因，部分quality低于full。见[feb06_core_04804](../_sources/daily-20260206/feb06_core_04804.jsonl)。Ch23预算后一段补依赖/坐标/paidcost与画外音、视觉失配反侧和audio独立/dense回退；jan02_v3 source/owner及actual381–415/新402/末注POST通过，未复现/不授SLO无损。

### [SE-Bench v1](https://arxiv.org/abs/2602.04811v1)

必要§2–4/C1–3见[core](../_sources/daily-20260206/feb06_core_04811.jsonl)、[S2](../_sources/daily-20260206/feb06_SEbench_S2.jsonl)、[C](../_sources/daily-20260206/feb06_04811_extra.jsonl)。random ZWC/ASTtests与Open/Closed SFT的局部结果可描述，但同y保/删doc不唯一识别参数internalization；consensus零观察不证永久OOD。§4.2明省offpolicy doc→no-doc IS，literal min(r,clip(r))*A在A<0不同PPO min(rA,clip(r)A)；r2/clip1.2/A−1分别−1.2/−2，只说明字面目标不同不断实现全错。C2 n/batch同时改不隔离clip原因。jan02_v3 actual必要源/Ch29:428–474核后中心终态通过，不写Books、不授标准RL不能internalize或clip内因；只重开actual loss/ratio handling及ablation config→results，有限SFT结果不全作废。

### [Decomposed Prompting Does Not Fix Knowledge Gaps v1](https://arxiv.org/abs/2602.04853v1)

必要§2–5及完整§4对照见[feb06_core_04853](../_sources/daily-20260206/feb06_core_04853.jsonl)。1433goldDSL人工核；Direct零shot、AssistivefullDSL/fewshot、Incremental freshcall缺原prompt/history不等view/budget；GeminiFlash gold/consistency judge不是internaltruth。RM正确且consistent/正确且inconsistent是比非条件正确率，DBA仅Direct事件sensor；CRAG反侧/稳定共同错保留。root实际源及Ch66:554–565/631–667核后Only通过，原2+1+2=5保持（root6简写已纠正）。现sensor/action/outcome合同承载一般边界，不称本goldrecipe已覆盖，也无证据形成部署新规则；未改Books/复现。

### [CoT is Not the Chain of Truth v1](https://arxiv.org/abs/2602.04856v1)

必要exact-v1 §3–6/A5/A7/G1–3，见[core](../_sources/daily-20260206/feb06_core_04856.jsonl)、[完整A5/A7恢复](../_sources/daily-20260206/feb06_04856_A57_full.jsonl)、[必要G](../_sources/daily-20260206/feb06_04856_AG.jsonl)。A5 can_gen自述/rules+10×100humanerror0非全人口零错；A7拒答仍带procedural surface不是实际生成有害文章/external effect。S4.4扰动pretrained hiddenclassifier g须同regenerated output分账；Eq1跨类减类内/argmax、Table2风格与87.5%、globalB2/per-input目标未绑定。G局部softmax/方向不授因果防御。root实际必要/Ch72:755–790核后中心终态通过，不写Books/可靠routing保证、不全篇无效；只重开标签人口、g与输出对照、指标实现/定位表config勘误。v2 Updated Feb6 02:03:27Z在本窗终点后，Submitted不是公开修订。

### [Reinforced Attention Learning v1](https://arxiv.org/abs/2602.04884v1)

必要exact-v1 §3 Eqs1–7/§4–5 setup/table/反侧，见[feb06_core_04884](../_sources/daily-20260206/feb06_core_04884.jsonl)。Eq1正PPO surrogate maximize、Eq3 A*JSD minimize、Eq4直接相加没给符号转换，不能代补负号；attentionteacher≠value/事实因果，θ=old JSDgradient0不授探索。eagerattention/8H100/teacher32B付费，VideoMMMU反侧、τ Table1=1/prose.9及RAL-zero同时改格式reward保留。root actual必要深入中心隔离通过，不写Books/性能或causalcredit；只重开实际优化方向、loss符号/τ配置与结果对应或勘误，不请求全repo/断全部表伪。

本批15项逐ID原字段与范围已核：04248 Submitted=2026-02-04T06:14:55Z、v1Updated=2026-02-05T01:29:25Z、registered=2026-02-05T02:54:29.000Z；04284 Submitted=2026-02-04T07:26:23Z、v1Updated=2026-02-05T01:32:09Z、registered=2026-02-05T02:55:22.000Z；04837 Submitted=2026-02-04T18:29:36Z、v1Updated=2026-02-05T02:06:58Z、registered=2026-02-05T03:08:21.000Z；04094 Submitted=2026-02-04T00:08:35Z、v1Updated=2026-02-05T01:14:19Z、registered=2026-02-05T02:50:57.000Z；04706 Submitted=2026-02-04T16:19:05Z、v1Updated=2026-02-05T01:59:52Z、registered=2026-02-05T03:05:14.000Z；04739 Submitted=2026-02-04T16:42:02Z、v1Updated=2026-02-05T02:01:14Z、registered=2026-02-05T03:06:00.000Z；04755 Submitted=2026-02-04T16:54:47Z、v1Updated=2026-02-05T02:02:10Z、registered=2026-02-05T03:06:23.000Z；04804 Submitted=2026-02-04T17:51:05Z、v1Updated=2026-02-05T02:05:14Z、registered=2026-02-05T03:07:34.000Z；04811 Submitted=2026-02-04T17:58:32Z、v1Updated=2026-02-05T02:05:38Z、registered=2026-02-05T03:07:44.000Z；04853 Submitted=2026-02-04T18:39:58Z、v1Updated=2026-02-05T02:07:30Z、registered=2026-02-05T03:08:44.000Z；04856 Submitted=2026-02-04T18:43:10Z、v1Updated=2026-02-05T02:07:49Z、registered=2026-02-05T03:08:49.000Z；04884 Submitted=2026-02-04T18:59:52Z、v1Updated=2026-02-05T02:08:51Z、registered=2026-02-05T03:09:28.000Z；04304 Submitted=2026-02-04T08:13:01Z、v1Updated=2026-02-05T01:34:08Z、registered=2026-02-05T02:55:50.000Z；04294 Submitted=2026-02-04T07:54:51Z、v1Updated=2026-02-05T01:33:11Z、registered=2026-02-05T02:55:36.000Z；04649 Submitted=2026-02-04T15:24:52Z、v1Updated=2026-02-05T01:56:55Z、registered=2026-02-05T03:03:52.000Z。共同粗字段Available=2026-02和February ID相容，state=findable；原值分别见[feb06_potential_date_fields](../_sources/daily-20260206/feb06_potential_date_fields.jsonl)、[last15](../_sources/daily-20260206/feb06_last15_date_fields.jsonl)、[additional7](../_sources/daily-20260206/feb06_additional7_date_fields.jsonl)。不是由代表批次推日期：各Submitted均在前一公告cutoff后、条件最早计划为Feb5 01Z，个体v1字段与findable注册上界联合的保守范围整体落窗；accepted/moderation可能延迟，故明示条件推定而非精确发布日志。registered是公开上界定位，不是首公开时刻，表加一秒只是秒精度半开表示；后期版本不回填。

## 5. 缺口与下一步

普通可执行：0。70家族/三维原分与来源停点已冻结，31实际POST、14具体已有覆盖、13仅报告、12中心终态保留；所有必要源、owner、实际写后处置及jan02_v3独立六部分日级Gate均安全闭合。STOP：不新增发现、不扩月目录/全文附件库存，普通待办0不消除下列历史覆盖和争议限制；共享窄锁已释放，来源/分数/改动数和机器检查仍不等无遗漏或性能保证。

终态保留项：12中心家族为04033指标单位、04521mask人口/config、03975generation/verifier账、04268entropy/queue、04278HVP空间、04337/04340loss方向、04170causal ring聚合，以及本批04739ASR/拟合人口、04811loss/IS/ablation、04856label/g/output/定位、04884loss方向/config。各精确重开条件见§4，只有绑定实际定义/配置与所报结果的澄清或勘误才定点重开；不用于正面证据、Books或无遗漏断言，不宣称全部实验伪。MetaJudge AP/RR matching与LiteToken配置、Spar索引公式子命题另明确隔离，不消除争议却也不挡已验证的有限qualitative接口采用。

外部来源终态保留项：arxiv原四主题API失败/有限月页回执未保存的历史与revision覆盖、Meta历史列表及补检回执、Kimi Platform2026与MiMo Blog日期入口具体限制见§2，Opuscurrentcard后期安全条款缺本窗事件身份；定点重开条件仅原有限请求/所列页/可访问历史原入口/带事件时间原条款恢复，不扩大库存，不支持零发布、正面证据、Books或无遗漏断言。04856v2 Updated在终点后，不由Submitted迁入；其他后期版本保持原字段边界。

贡献前关闭与窗外身份：Frontier、DELTA、H-GIVR、PersoDPO、Interfaze、DiMo、03822、04206按具体原文组合缺少本项目可迁移的新机制，不按领域、小模型或无实验排除。SoftFSM04206不是按turn占位：原§3.2/3.4/4.1/4.3/6.4的累计KIU进度由手工40+schema及court-judgment确定oracle提供，learned extraction尚future；root实际决定性核后仅关闭其本项目准入，不否认外置progress有效，不授开放动态程序终止或真实事实核验。NAI与Kimi1.8.0具名必要core已root实际关闭；三有限deciding原5Only安全处置。03845/03802/05014窗外和04634later-withdraw版本身份保原记录，不充本窗候选/重要修订。未经主题贡献筛选的月目录不是队列；未扫描Weekly、Live或其他月份。

## 6. 复核

协作验收停点：70家族身份/评分冻结，31实际整合POST、14具体已有覆盖、13仅报告、12中心终态保留，所有候选普通处置0；jan02_v3独立日级Gate通过。来源14有限停止、逐ID条件公开范围及具名原字段、负侧抽样保持实际范围；Spar/Meta/Lite子命题隔离不授正面结论。root/jan01_v3/jan02_v3的必要核与实际POST仅指下列采用范围，不声称全部正文/附件或代码复现已读。最终六部分由jan02_v3实际验收通过，范围及未抽样权限如下。

复核者：jan02_v3（报告非作者，最终日级复核）；root/jan01_v3分批必要核与actual POST按下列范围

结论：通过

最终日级非作者实际范围（jan02_v3）：顺读最终六部分，核70候选/70同URL证据及31整合+14已有覆盖+13仅报告+12中心=70，实际逐ID核68个arxiv原Submitted/v1Updated/Available/findable注册上界与条件联合区间、2官方事件时间；复用本轮明确root/jan01_v3/jan02_v3必要原源→owner→实际POST，不复用legacy，本人最后VAQ/OmniSIFT/MetaJudge/LiteToken四POST实际读正文、前后邻接和末注。来源原停点实际抽核RSS、40Qwen、9Hunyuan、15ZAI、20Seed/has_more、DeepMind页3/4、Kimi tags、Anthropic修改日期及Moonshot2025列表限制；重新读最新§2/§5的arxiv四主题API/有限月页回执未保存与revision历史、Meta补检回执未保存终态隔离，不授这些原分页已独立核或无遗漏。本人完整v1题摘负侧抽检Interfaze04101、DiMo04188、CROSS-ALIGN03822、SoftFSM04206；SoftFSM决定性§3.2/3.4/4.1/4.3/6.4复用root本轮fresh实际核，有限schema/oracle理由关闭不否外置progress。未抽核其余全部75题摘负侧/175宽标题、未重读全附件或运行代码复现，不授正面历史覆盖。结论为本窗可执行处置闭合及外部/中心终态安全保留，不是所有原源无遗漏证明。

本批15独立范围：jan01_v3实际8narrow source→owner后，04094/04248/04284/04837四gap由root实际新段/邻接/源注POST通过；03980/04184/04210 Only与04170中心终态已按其实际核记录。jan02_v3实际04294必要§3–5/T8/T11/T13/限制、04304必要§3–5及Ch23crop邻接、04649§2–4/C1/D1/D2/Fig9与Ch66 EvidenceTrail、04706机制/配置与Ch11固定vocab、04755§3–7/完整L与Ch66/33、04804§3–4与Ch23预算、04811§2–4/C1–3与Ch29必要核；VAQ与OmniSIFT实际正文/前后邻接及末注POST通过，MetaJudge/LiteToken实际新正文/前后邻接/源注POST也已通过。root另外实际04739 exact-v1PDF§3–7/D1–D2、04853§2–5/§4完整对照、04856§3–6/A5/A7/G1–3与Ch72四轴、04884§3 Eqs1–7/§4–5，按精确中心/Only判通过。原04853 2+1+2=5冻结，不沿root摘要简写6；评分不因深度/Books差额改变。采用范围未运行代码或复现实验，四中心不授性能/安全/完整覆盖。

非作者jan01_v3实际必要原源/owner分批复核：Lychee §3–4/实现成本反侧与Ch45 FASA后接口、TrajFusion §3–5/§7/A.1.2–A.1.3与Ch29 expert恢复段、DeFrame §3–4/A.2与Ch66 variants段、Swordsman §3–5与Ch24 fixed/confidence控制差额通过；前三实际新段POST由jan01_v3实际读正文/邻接/末注通过，范围分别Ch45 180–200、Ch29 146–164、Ch66 378–398，未重审无关附件；Swordsman由root另实际POST通过。EmbedPlan §3–5与Ch25/Ch79具体已有覆盖通过，仅采用teacher-forced命中不继承free rollout/闭环planning结论，非root全文核。SSD/T3必要source→owner已由jan01_v3实际核，原6不变；teacher样本/读出/MDN成本、三分布接口、PCP/SEP反侧与T3cohort依赖/HH近OOD/reference及20tokens/words冲突按采用边界收窄，root另实际两新段/邻接/末注POST通过，未授日Gate。root另实际Cdelta S3.2/Eq3、Alg1/gradmask及S5/A.3/A.6/Table13，中心mask convention/config与结果绑定未解，本窗终态隔离通过；不授全部实验伪或正面安全证据。

root实际读首批四篇完整v1题摘及逐项日期字段、TAC L38–55，7/6/6/6与TAC6准入通过；随后03979/04033/04202/04297/04306/04355/04391/04399及04428/04509/04521/04541/04556/04557/04577/04581两批完整v1题摘、具体增量/6分准入通过，不授AB宣传保证。Frontier L42–108完整core、DELTA04112/H-GIVR04413/PersoDPO04493完整题摘的具体贡献前关闭通过。必要证据/owner层：04105必要§3–6/8–9与Ch72；ERNIE§3/§6与Ch21具体已有覆盖；TAC与Ch72具体已有覆盖；HP§3–4/Ch36与HarmoniaIII-A/IV-C/V-A/Ch49；03979§2/§3/A.1与Ch33；04202§3.1/3.2/4.1/4.2与Ch23仅scene/motion分解，04297§3–5与Ch66仅matched-output/parse/variants，两项标准具体已有覆盖通过。04033原§3.2/§4/Table2/3中心指标单位终态隔离通过；04355 Sx2/Eq1、Sx3.3–3.4必要原源及Ch66差额通过，actual122段与前后邻接/4289末注POST通过。八项实际改动的正文/前后邻接/末注均root POST通过；新增Dowser Ch29 802–822/1214、AUS Ch15 279–299/341及PIT Ch12 135–170/375已实际核，这段只记录当时采用范围；后续具名处置见§4及本节新增范围，不能据此批量授Evidence或日级Gate。04355原缓存selector未覆盖Sx节名已实际发现并定点恢复，不冒称原空core已读。机器校验不替代来源/证据/Books实际核验。
