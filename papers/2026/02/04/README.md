# Daily Research — 2026-02-04

**规范：** V3
**窗口：** 2026-02-03T09:00:00+08:00 ～ 2026-02-04T09:00:00+08:00
**补充窗口：** 2026-02-03 ～ 2026-02-03
**窗口说明：** 用户授权仅补已有日报遗漏；原窗口、17 个既有候选行/公开日期/评分和连续原 §4 冻结。新增按前一北京自然日判断，不沿用旧 9 点门，也不搬移旧材料归属。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T12:38:18+08:00

## 1. 结论

本轮对 14 个每日入口及四组 arXiv 主线主题做有限补查；新增确定家族 1 个 HySparse，评分 6，必要 v1 机制/评价/直接反侧已深入审阅，具体 Books owner 已有覆盖，本轮 Books 新写 0。合并后确定家族 18 个：原 17 个处置不变，加 1 个具体已有覆盖；共 7 整合、10 已有覆盖、1 中心争议隔离。15 个新增潜在家族因首次公开日未证实而隔离，不计候选或完成审阅；另 1 个已撤回家族不采用。Sora feed、GLM-OCR API、ADP-MA 与 Formal Semantic Control 贡献前关闭，不以产品上线、主题或自称 novel 自动纳入。首批准入、HySparse 必要证据与 owner、代表排除及本轮六部分日级复核均由 root 实际独立通过；本轮可执行待办 0，日报补查完成，旧完成声明未用作这次验收。

以下两段及既有明细是原轮有效层的保留记录，不是本轮新增覆盖/完成凭据；逐字运行前基线另保留于[本轮原稿基线](../_sources/daily-20260204/supplement-original-20261008.md)。未复现实验，本轮有限入口不能支持全网无遗漏。

本日独立处理14个每日原入口和具名必要补充，未从旧Daily/Weekly或旧队列反推准入。确定候选17个唯一家族（16论文、1官方博客），完整题摘/博客核心及必要机制、对照、限制均已按采用命题实际审阅；视觉压缩的中心理论与性能冲突仍隔离，不算正面证明。七个更早Submitted家族和三机构日期相交事件未确定落窗，不计候选。

当前7家族已实际整合到6个唯一owner章节，共9段正文及各证据注；9家族具体已有覆盖，1家族中心争议暂缓。7家族实际写后独立通过，9项具体已有覆盖及1项争议终态的必要证据独立核均已完成；root非作者日级来源/日期/负侧/状态验收通过，作者普通待办0，日报完成。未复现实验或运行公开实现，有限发现与原入口历史缺口不支持“全网无遗漏”。

旧README已逐字备份于[LEGACY_README](../_sources/daily-20260204/LEGACY_README.md)。原目录非`feb04_*`的旧inventory/screening/Books queue保持原身份，未用于本轮准入、评分或完成；fresh依据均为`feb04_*`。

## 2. 来源覆盖

原轮来源表完整保存在[原稿基线](../_sources/daily-20260204/supplement-original-20261008.md)；本节唯一覆盖表记录本轮有限查询与停止，不将原轮已检查标签继承为本轮零发布。

原始入口、参数和返回保存在 [本日来源记录](../_sources/daily-20260204/feb04_sources_0.json)、同目录 sources_1/2/3、native_metadata、api_restore、directory_restore、arxiv_metadata/arxiv_fallback、hunyuan_api 等 fresh 文件。失败与替代范围亦保留，不拿失败返回作零命中。对具名官方事件页的Comments/history及当前修订提示作轻量检查，PROBE的v2不作为本窗新贡献；不为证明没有标记遍历全版本史。

本轮补查（仅 Feb 3 自然日）实际停止如下。原始材料集中为同目录 `supplement-*`；[本轮目录/日期恢复](../_sources/daily-20260204/supplement-native-restore-20261008.json)、[边界补查](../_sources/daily-20260204/supplement-native-boundaries-20261008.json)、[机构原件](../_sources/daily-20260204/supplement-native2-20261008.json)及[四主题查询](../_sources/daily-20260204/supplement-arxiv-themes-20261008.json)分别保留实际返回，不把宽目录条数当本日候选量。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 当前页/RSS；本轮 RSS 1255 条元数据，只读 Feb2→Feb3 Sora→Feb4 App Server 邻接。Sora 官方 Feb3 全核心已读并贡献前关闭，停止于边界。 | 已检查 | 当前 RSS 非不可变历史快照；Sora 后加 April26 停用标记不回填本窗。 |
| SRC-ANTHROPIC | Research 当前页与本轮 embedded publishedOn，Jan29 coding skills/Jan28 disempowerment→Feb5 zero-days。日期不是图片 _createdAt；只读取邻接段，停止。 | 已检查 | 当前目录不保证已删除发布召回；窗后安全事件不纳入本日。 |
| SRC-GOOGLE-AI | DeepMind 当前 Research/Blog 与 ?page=4 未恢复目标历史切片；有限官方域 Feb3 补检。Research Feb 月份 7 个日期标题仅定位，唯一 Feb3 virtual-care 在暂缓医疗领域应用，停止，不审整月正文。 | 受阻 | DeepMind 本日历史切片仍缺；Google pubs 年度目录不是全文队列。 |
| SRC-META-AI | Research 动态页 0 行正文；官方域 Feb3 research 有界补检无可用本日原事件，停止。 | 受阻 | 空正文/搜索无命中不证明零发布；需本日官方历史切片或具名事件。 |
| SRC-QWEN | qwenlm 当前首页、qwen.ai/blog 本轮可见正文仅 Qwen；有限官方域 Feb3 补检日历文字不当发布字段，停止。 | 受阻 | 未恢复本日官方历史目录，不授覆盖或零发布。 |
| SRC-DEEPSEEK | 从官网新闻入口实际读取 research 日期邻接 Jan28 OCR2→Feb25 DualPath，两侧均窗外即停止，不展开全年论文。 | 已检查 | 当前有限目录不能保证已删除条目召回。 |
| SRC-MOONSHOT | Platform Blog 本轮可见最近 Nov7 2025；GitHub 官方 org 当前入口只定位，无本日首次发布字段；停止。 | 受阻 | 当前仓库更新时间不等初公开，仍缺本日历史切片，不继承别日报结论。 |
| SRC-TENCENT-HUNYUAN | Research 原入口及本轮 publicList page1/pageSize1000/renderType0，total9/list9 元数据读完；100025 Feb3 与下一项 Feb13 邻接。100025 同既有 CL-bench 家族去重，原必要核心有效复用。 | 已检查 | publicAt 与 display 原字段保留，当前列表不证明初版逐句或删除历史；不重复计 CL。 |
| SRC-ZAI | Research 日期 Jan19→Feb2 GLM-OCR→Feb11/21；Feb3 release notes 与 OCR API guide 核心读，API 只产品提供/普通图文输入合同，没有本次新的执行/权限/兼容差额，贡献前关闭。 | 已检查 | Feb2 research 与 Feb3 API 为同家族不同事件，不反填成 Feb3 新论文。 |
| SRC-BYTEDANCE-SEED | 本轮 type1 publish_year2026/count100/order_desc=false 实际首20/total82，只读邻接 Jan29/31→Feb2 SPARKLING→Feb4 VTok/Feb5 BABE；type2 首9/total23 最早 Feb12，窗后停止。 | 已检查 | [实际 API](../_sources/daily-20260204/supplement-seed-api-20261008.json) has_more 不扩全年队列；VTok 官方 Feb4 窗外，epoch 日期编码不造午夜。 |
| SRC-BAIDU-ERNIE | 本轮中文 Blog 日期邻接 Jan29 PaddleOCR-VL1.5→Feb6 ERNIE5.0，停止，不读两侧窗外正文。 | 已检查 | 当前目录可能删除/重排。 |
| SRC-XIAOMI-MIMO | 本轮官方 Paper/Blog Jan8→Feb3 HySparse→Mar13/Jun29；官方 date-only 完整落新增自然日，精确 v1 题摘/必要核心与当前标记读完。 | 已检查 | 作者官网事件与随后 arXiv 事件分开；Submitted 不作为公开证据，不追时分秒。 |
| SRC-MINIMAX | 本轮英文 Jan27→Feb12、中文跳转 minimax.cn Jan28→Feb12，独立日期邻接停止；Agent Tech Blog 原动态与 .md 880 bytes 只 May13，停止。 | 已检查 | Agent Tech Blog 当前页不能证明历史无条目；英中文日期不同不合并成一个精确时刻。 |
| SRC-ARXIV | model(CL/LG)、multimodal(CV/RO)、system(DC/AR/PL/OS/PF)、agent(AI/IR/MA)四主题；Jan30→Feb3 submittedDate 仅缓冲发现，start0/max100/ascending，本轮 429/超时。有限 CL 请求首100实际可见40标题、AI首25标题读完，DC/CV首25失败；主线明确线索完整 v1 题摘，跨来源/分类去重；官方 daily/advanced 日期恢复失败即停止。 | 受阻 | 月目录不是日公告，未审整个100/月份/分类；Submitted、February ID、DOI注册及当前版本不补首次公开日。15 个新增潜在日期 hold 与撤回项隔离见 §5。 |

## 3. 候选与判断

以下 17 个旧行逐字保留；新增行只有 HySparse。其公开日期来自 MiMo 官方 Paper 目录 Feb3，不是 arXiv Submitted 或旧 9 点条件推定；同家族首次官方事件和随后论文公告不重复评分。

论文公开区间逐ID保守推定：Submitted均晚于Jan30 19Z；winter公告的条件性最早批次与February ID/Available相容，findable DOI registered逐项给13:00前的公开上界，联合范围完整落窗。它不是严格announcement日志，registered也不是首次公开时刻；原字段见[首批](../_sources/daily-20260204/feb04_dates_api.json)与[后续逐项](../_sources/daily-20260204/feb04_selected_dates.json)。若出现实际更早原发布，仅重开受影响项。PROBE v2不是本次采用事件。CL博客与后来论文公告分开。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Localizing and Correcting Errors for LLM-based Planners · 2602.00276v1](https://arxiv.org/html/2602.00276v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | whole-plan 示例隐藏错误位置→first-failure 最小 IO→离线 prompt 修复粒度；2 + 1 + 2 = 5 | 深入完成 | 整合 `AGENT-PLANNING` [章节](../../../../books/part-07-agent/79-planning.md)，正文340 |
| [Do Latent-CoT Models Think Step-by-Step? A Mechanistic Study on Sequential Reasoning Tasks · 2602.00449v1](https://arxiv.org/html/2602.00449v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 完整 latent rollout 的假设→bridge/readout bypass 和任务收缩反证→干预路径再判断；3 + 1 + 2 = 6 | 深入完成 | 整合 `MODEL-DECODER-ONLY` [章节](../../../../books/part-02-model/18-decoder-only.md)，正文294/296 |
| [Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory · 2602.00521v1](https://arxiv.org/html/2602.00521v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 同一 subject 下 prompt 改变仪器→GRM条件分解→稳定与 human alignment 分账；2 + 2 + 2 = 6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，正文261 |
| [Assessing Domain-Level Susceptibility to Emergent Misalignment from Narrow Finetuning · 2602.00298v1](https://arxiv.org/html/2602.00298v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 窄域 FT 风险随domain/base变化→adjusted MIA与raw相关反向→冻结安全probe人口；3 + 1 + 2 = 6 | 深入完成 | 已有覆盖 `PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md)，分布触发行为probe/跨模型sensor边界 |
| [CL-bench 官方博客100025](https://hunyuan.tencent.com/research) | 2026-02-03T18:02:07+08:00 | 长Context检索不等于规则学习→same-task context ablation/rubric contract→依赖与抗污染分账；2 + 2 + 2 = 6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，正文2874/2876 |
| [Training LLMs with Fault Tolerant HSDP on 100,000 GPUs · 2602.00277v1](https://arxiv.org/html/2602.00277v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 全组停顿放大故障→replica故障单元/CPU membership/GPU FTAR与catch-up→按step提交重入；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖 `TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md)，970–978同家族正文 |
| [PROBE: Co-Balancing Computation and Communication in MoE Inference via Real-Time Predictive Prefetching · 2602.00509v1](https://arxiv.org/html/2602.00509v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | reactive热度滞后→下层lookahead+phase-locked weight transfer→复制预算与真实路由分离；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 `INFER-SCHEDULING` [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)，531–535同家族正文 |
| [When Agents "Misremember" Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems · 2602.00428v1](https://arxiv.org/html/2602.00428v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 角色群体与压缩记忆放大错误→真假guidance取舍→共识/authority不可相互替代；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 `AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md)，311–334、1435–1455 |
| [Segment-Level Attribution for Selective Learning of Long Reasoning Traces · 2602.00425v1](https://arxiv.org/html/2602.00425v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 全trace监督重复片段→IG强度/符号一致性选段loss→输入保留与监督选择分权；2 + 1 + 2 = 5 | 深入完成 | 整合 `TRAIN-SFT` [章节](../../../../books/part-04-training-system/29-sft.md)，正文126 |
| [DecompressionLM: Deterministic, Diagnostic, and Zero-Shot Concept Graph Extraction from Language Models · 2602.00377v1](https://arxiv.org/html/2602.00377v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 平均PPL掩盖部分概念可访问性→受控inventory/offset量化反证→量化发布需独立语义切片；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 `INFER-TENSORRT-LLM` [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，1936及2153–2155；inventory方案仅报告 |
| [PolarMem: A Training-Free Polarized Latent Graph Memory for Verifiable Multimodal Agents · 2602.00415v1](https://arxiv.org/html/2602.00415v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 相似检索混淆正/负/未知→极性冲突优先级→否定条件需独立事实验证；2 + 2 + 2 = 6 | 深入完成 | 整合 `AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md)，正文1222 |
| [Cross-Modal Memory Compression for Efficient Multi-Agent Debate · 2602.00454v1](https://arxiv.org/html/2602.00454v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 长text通信→图像codec压缩→质量/恢复/成本条件需分权；2 + 2 + 2 = 6 | 争议 | 暂缓：中心信息论保证及冲突性能点；§5明确重开条件 |
| [Dual Latent Memory for Visual Multi-agent System · 2602.00471v1](https://arxiv.org/html/2602.00471v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 单记忆表征→perception/thinking双库与entropy触发→访问路径/reader兼容/训练费用分权；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 `AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md)，465–482、799–807、1432 |
| [Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs · 2602.00564v1](https://arxiv.org/html/2602.00564v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 答案成功掩盖过程违反→rule/格式/first-error分数→结果与公开过程不互授faithfulness；3 + 1 + 2 = 6 | 深入完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，3442–3452 |
| [Learning Modal-Mixed Chain-of-Thought Reasoning with Latent Embeddings · 2602.00574v1](https://arxiv.org/html/2602.00574v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 外图工具成本→自编码视觉latent+AR条件diffusion head→路由/采样/质量各自核；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 `MULTIMODAL-GENERATIVE-PARADIGMS` [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，373–375；视觉表示交接Ch23 |
| [DIVERGE: Diversity-Enhanced RAG for Open-Ended Information Seeking · 2602.00238v1](https://arxiv.org/html/2602.00238v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 检索多样不保证输出多样→memory/reflection+同query输出测量→输入与claim多样分权；3 + 1 + 2 = 6 | 深入完成 | 整合 `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md)，正文438 |
| [DETOUR: An Interactive Benchmark for Dual-Agent Search and Reasoning · 2602.00352v1](https://arxiv.org/html/2602.00352v1) | 2026-02-03T09:00:00+08:00 ～ 2026-02-03T13:00:00+08:00 | 固定partner仍有推理/模型偏差→joint身份与非均run对照→不以固定Memory宣称独立归因；3 + 1 + 2 = 6 | 深入完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，1330–1382 |
| [HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing · 2602.03560v1](https://arxiv.org/html/2602.03560v1) | 2026-02-03 | 每层 selector/KV 重复成本→full 层 block scores/global KV 跨层复用，独立 layer-local SWA→分别选择全局状态共享与局部表示保留；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 `MODEL-LONG-CONTEXT` [章节](../../../../books/part-02-model/22-long-context.md)，选择器成本/ownership 与独立 local window 正文396–414 |

## 4. 证据与知识整合

原文必要核心保存于[首批精确sections](../_sources/daily-20260204/feb04_necessary_core_sections.json)、[后11核心sections](../_sources/daily-20260204/feb04_second_core_sections.json)、[必要控制附录](../_sources/daily-20260204/feb04_control_appendices.json)及[CL/DETOUR核心](../_sources/daily-20260204/feb04_cl_detour_sections.json)。抓取内容多于实际采用范围；下面只称实际阅读的位置，不以下载等于审阅。

### [Localizing and Correcting Errors for LLM-based Planners · 2602.00276v1](https://arxiv.org/html/2602.00276v1)

§3–4/6：PTP只提供subroutine specification，不是可执行实现；training oracle定位第一违例并给(function,input,correct output)，test不再调用该oracle。离线pool与100test/domain分开，valid≠success≠optimal。Alg1 P0/batch与iterative prose不一致，2k/5k/7k及89%/63%不拼接为统一效率。Ch79原334–338只分解oracle trajectory mismatch，未承载最小IO→离线prompt接口；新增340及末注496，保whole-plan/ledger/终局验证，不授在线自改或约束保证。root必要原源/owner写前通过，root实际写后及邻接通过。

### [Do Latent-CoT Models Think Step-by-Step? A Mechanistic Study on Sequential Reasoning Tasks · 2602.00449v1](https://arxiv.org/html/2602.00449v1)

§3–7及受影响C/D/E/F/G/H/I：3-layer/2-head GPT2-style、固定latent slots、teacher answer-boundary self-distillation；2–3hop存在bridge+final-input readout bypass，长hop部分late-only。probe/patch只在clean-correct样本；线性不可读不证明其他code不存在。prime非零乘子双射/composite收缩是特定任务边界，有压缩可能不等训练必采用；distillation-only与teacher-loss消融不混淆。Ch18必要性干预后新增294/296、末注407，root实际写后及邻接通过。不外推自然语言推理或通用训练因果。

### [Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory · 2602.00521v1](https://arxiv.org/html/2602.00521v1)

§3–6/Tables1–3/6.3：七judge、四benchmark families、四拟保持含义的prompt、OpenRouter temperature0。GRM共享subject latent quality、各prompt discrimination/threshold；估计依赖先验与rating尺度。CV/ρ稳定≠人类正确，aggregate Wasserstein不保证逐sample配对，扰动不保证严格等价。Ch66 hardwin/loss与softprob/Rank之后261新增instrument stability与human alignment分账；源注5236，root实际正文/相邻及写后通过。作者阈值不变成通用发布Gate。

### [Assessing Domain-Level Susceptibility to Emergent Misalignment from Narrow Finetuning · 2602.00298v1](https://arxiv.org/html/2602.00298v1)

§5–8/A/B：主Qwen2.5-Coder7B与GPT4omini subset，不是两模型全11域因子；11训练域仅9完整with-prefix。§5judge<50与§7图<30不合并比例，有限 unrelated prompts/judge有共盲区。raw MIA相关在base-adjusted后反向，adjusted zlib AUC.5不提供通用预测器。§8未分清领域有害输出模仿与genuine broad misalignment。采用局部风险/评价人口边界；Ch72现2218后的分布触发probe、有限触发false-negative/rollback及跨模型sensor限制承载，不把domain相关写成因果先验。root实际§5/8及Ch72 safety sensor/geometry/独立safety regression正文核对，具体已有覆盖通过。

### [CL-bench 官方博客100025](https://hunyuan.tencent.com/research)

API100025 publicAt1770112927=Feb3 18:02:07BJ，内部published/display1770090898=11:54:58，均落窗但不同；当前公开核心不证明初版逐句措辞。原博客及补充2602.03587v1 §3–4/6.3/A1/A5/E必要内容：self-contained rule Context、task dependency、all-rubric二值成功；保逐rubric失败与scorer。1000随机题单GPT5.1 no-context .9%支持局部依赖，不证明零污染；100答案人工审judge rationale与异构agreement>90%不是human baseline。后论文Submitted Feb3 14:37:47Z的公告在窗后，不回填博客co-release。Ch66 longContext配置后新增2874/2876与5238源注，root原核心、补充证据和实际写后通过。

### [Training LLMs with Fault Tolerant HSDP on 100,000 GPUs · 2602.00277v1](https://arxiv.org/html/2602.00277v1)

§4–6及必要§2故障约束：replica内同步/local commit，CPU FTAR membership/retry与GPU copy/reduce分离。恢复在已提交step/state/cursor上catch-up，健康replicas继续；fetch比step慢则仍可能阻塞。exactly-once是batch被接纳一次，不是物理执行一次。98K H100/12replica/4DC的大型作者训练与256H100 MoE精度实验不同；3min包含故障检测/实遇bug，修复后约1.5min为推计未重跑；80%/44%是按18min故障间隔公式，不是测得通用吞吐。Ch36 970–978已有同SF control/data、frontier/cursor、重入与fallback，No Change，不重复改书。

### [PROBE: Co-Balancing Computation and Communication in MoE Inference via Real-Time Predictive Prefetching · 2602.00509v1](https://arxiv.org/html/2602.00509v1)

§3–6：下层router clone/residual predictor只建议placement，真实router仍决定token dispatch；planner受双rank窗口/ingress/egress/slots约束，是heuristic非全局最优。weight transfer在GEMM开始、Combine暂停、Attention恢复，最多3副本double-buffer=6slots。8×Hopper141GB单NVSwitch/BF16、PyTorch2.9/CUDA12.9/NCCL2.27.3/SGLang/DeepEP；500decode steps均值非多节点或SLO。87–94%预测不授零miss，6.5×Combine主要sync-wait差异非网络变快；prefill EPLB OOM排除改变可比集合。Ch56 531–535同SF已承载predictor/planner/buffer/epoch、miss/超窗与静态回退，No Change。

### [When Agents "Misremember" Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems · 2602.00428v1](https://arxiv.org/html/2602.00428v1)

§3–6及D.2：4838 BBH多选、distractor与五角色，错误转换分母是baseline-correct子集。角色对比伴随叙事复杂度；short同会话、long是摘要注入新context，不是模型永久内部记忆。原prose全角色更易受骗与DeepSeek/Llama表局部反向保留；vigilance只是作者假说。Resilience-only会拒真guidance；新增1000cooperative（500纠错/500丰富）与resilience平衡的SFT在4A800/BF16/5epoch局部可缓解。但main CorrectGuidance σC测原本正确→错，不代表原本错→接受真纠正的成功率。Ch77 311–334共识不授truth及双纠错风险、1435–1455consolidation authority/重复观测已有覆盖；不为“Mandela”名称新增memory机制。

### [Segment-Level Attribution for Selective Learning of Long Reasoning Traces · 2602.00425v1](https://arxiv.org/html/2602.00425v1)

§2–4/C/D：绝对IG聚合除sqrt(length)，符号一致性=abs(sum)/sum(abs)，累积强度τ.7和β.8是局部selector；首尾保留，完整CoT teacher forcing，仅选段loss，不把负归因从Context删除。817 LIMO、R1-distill1.5/7B及Qwen、固定数学任务；归因baseline与50步额外前反向约7GPUh、全SFT约8GPUh但硬件不披露，不授总降本。分段keywords/model依赖、attr不是causal necessity。Ch29 loss mask与backward routing间新增126/源注1204；root原源/owner写前通过，root实际写后及邻接通过。

### [DecompressionLM: Deterministic, Diagnostic, and Zero-Shot Concept Graph Extraction from Language Models · 2602.00377v1](https://arxiv.org/html/2602.00377v1)

§3–5/8：Van-der-Corput 1D arithmetic-CDF deterministic decode、领域concept prompt、ASCII/fuzzy过滤与连续概念co-occurrence graph，不是reasoning边的证明。8192条独立生成序列、每条最长16/32 token、Qwen7B/Llama8B BF16/GPTQ/AWQ/BNB，offset8×2048导致inventory交集15–34%、core2–8%；非完整知识库存。AB的PPL近不变不能涵盖GPTQ4（Table2约1e5）；局部BNB4/Int8 concept损失与同配置conditional explanation PPL才相关，后者不是heldout通用PPL。200法律concept单corpus是否有hit不是truth oracle，errors/denominator不外推法律可靠性。Ch49 1936平均PPL掩盖symbolic commitment、2153–2155发布按语言/task切片已覆盖拟采用边界；inventory算法仅报告，不写“丢70%真实知识”。

### [PolarMem: A Training-Free Polarized Latent Graph Memory for Verifiable Multimodal Agents · 2602.00415v1](https://arxiv.org/html/2602.00415v1)

§3–4：VLM概念/Yes概率+image-adaptive Otsu、unknown margin，极性标签不是独立真值。query正/负constraints与lexicographic(-1,0,1)再semantic；Alg1 sortTopK非删除conflict，候选不足仍可返回冲突，不授“categorically suppressed”或hard逻辑执行。8VLM/6benchmark冻结模型，部分backbone/切片退步，training-free≠cost-free。Ch77 verifier metadata后新增1222及源注2008，明确存在/否定/未知、软priority与事实验证分工；root必要原文/owner通过，root实际写后及邻接通过。

### [Cross-Modal Memory Compression for Efficient Multi-Agent Debate · 2602.00454v1](https://arxiv.org/html/2602.00454v1)

§3–5及A/B：3Agent/5round历史render为1024图像、Arial12/SAM+CLIP/256视觉token、约85K数据adapter，frozenMLLM；固定token不证明任意history字迹可恢复。Table1 singleA100/7–12B MATH46.8与resolution表76.3未解释protocol，不合并收益；input token不含output/train，85K数据split不足以排除或认定污染。

理论A4的conditional independence不保证压缩后信息indicator相互独立；eq24对任意aggregation声称MI≥max没有所需条件（constant聚合反例），Step4另加每history≥bottleneck假设；eq41 γ/KΣI不能一般趋零。因此中心恢复保证及冲突性能点争议终态隔离，不用于正面证据或Books。Ch82 258–275现codec/modality/lifecycle/fidelity/可读回退具体承载已支持的表示分工；不借成熟codec原则掩盖新定理争议，不强制改书。

### [Dual Latent Memory for Visual Multi-agent System · 2602.00471v1](https://arxiv.org/html/2602.00471v1)

§3–4/C.1–5/D.1–2：多粒度视觉native encoder/projector perception bank与hidden-state thinking bank；entropy滑窗/λσ+cooldown、learned Gumbel gate、TopK/refine8tokens触发读取。需logits/hidden/native projector，不是black-box普适API。backbone frozen但compressor/router经PPO训练；主文two-stage与C.5三stage冲突保留。D.2 w/oTriggering未明示matched random controller，观察type usage不授因果最优路由；局部accuracy负向及token均值异常不采用headline效率。8H200、五VLM/六topologies局部结论。Ch77 465–482uncertainty/selective展开、799–807hidden-query外bank/预算及1432reader兼容具体承载，No Change。

### [Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs · 2602.00564v1](https://arxiv.org/html/2602.00564v1)

§3–5/7及B/F：150双语题、人工2–10步skeleton，teacherJudge process/format/length/first-error分数分开；所谓lucky guesses含格式惩罚，可能惩罚合法替代/长trace，不证明内部不faithful。Gemini3pro按同benchmark human相关选judge，PRM8B有goldanswer/33Kteacher训练，不等部署未知答案oracle；hazard设计来自同14模型2100trace非独立通用先验。human相关.64/κ.568有限，部分blind/split未披露。Ch66 3442–3452现evidence-trail/公开步骤/最后值/声明分权与独立oracle，不以过程rubric宣称内部因果；具体已有覆盖。

### [Learning Modal-Mixed Chain-of-Thought Reasoning with Latent Embeddings · 2602.00574v1](https://arxiv.org/html/2602.00574v1)

§4–5：START/END切换language head与固定K视觉latent，own vision encoder/connector将图像表征256→32，条件diffusion head逐latent50denoise；CE+噪声MSE（原文velocity/noise词不一致不混说）。71,488 Zebra筛选与VisuLogic1k×500sample；RL不反传latent loss，只更新text策略。SFT26.7→RL25.7、language-only21.6<base22.5保留，不授无遗忘。H100的32text1.03s/32latent3.10s/工具8.36s不是端到端同任务通用速度点。Ch24 373–375已分开AR conditional history/continuous head/采样预算与全pipeline成本，视觉representation交接Ch23 865–870；不为局部new scene复制同机制。

### [DIVERGE: Diversity-Enhanced RAG for Open-Ended Information Seeking · 2602.00238v1](https://arxiv.org/html/2602.00238v1)

§3–7/B/C：历史观点memory、reflection生成new perspective与MMR refinement；same-query10答案/GPT5系T1。主文100query与C.1顺序筛200subset不合并；claim extractor+embedding greedy阈值.75定义的是代理多样性，不是truth/有效观点数量。quality judge用事实/支持/一致/相关五档，1500/25human κ.54不是当前100任务独立事实oracle；query-minmax归一harmonic依赖参照竞争者。GPT5mini质量4.342<baseline4.578，不照录全部配置只微降.04；额外search/calls未matched，ablation不授单组件因果，failure含intent偏离40%等局部样本不能外推。Ch76 setwise utility后438新增输入/输出diversity分权，源注1414；root必要原源/owner通过，root实际写后及邻接通过。

### [DETOUR: An Interactive Benchmark for Dual-Agent Search and Reasoning · 2602.00352v1](https://arxiv.org/html/2602.00352v1)

§4/5.2–5.4/6：固定Memory Gemini2.5Pro prompt偏重facts不构成推理隔离；20prompt/150校准题同Gemini judge的97.5%不授deterministic环境。三full runs对noMemory单run预算非均；部分问题参数知识可答，Memory不是每题必需。撤回最初TOCTOU类比（原文没有）。新增可支持的是partner identity/共同prompt与judge/非均run归因边界，root实际核并确认Ch66 1330–1382 mock规则/状态/prompt/checkpoint/seed与共偏已承载；已有覆盖，不授独立模拟保证。

### [HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing · 2602.03560v1](https://arxiv.org/html/2602.03560v1)

本轮新增。MiMo 官方 Paper Feb3 为首次官方研究事件；v1 Submitted Feb3 只辨身份，不提供公开日；未见撤回/勘误标记。实际读 v1 §3.1–3.3/Eq3–9/Algo1、§4.1/Tables1–4、§4.4/§5；[必要原件](../_sources/daily-20260204/supplement-hysparsecore2-20261008.json)与[限制](../_sources/daily-20260204/supplement-hysparselimit-20261008.json)。full 层给 block-max normalized scores、GQA 组内 max indices；后续 sparse 层以本层 query 读取源 full-layer KV，另保本层 SWA KV，sigmoid 融合。64-token block/1024 selected tokens/128 local window 是作者配置，不是通用最优参数；它是需要训练的混合架构，非任意 checkpoint 无损删层或永久驱逐未选 token。

7B 36 层 1:3、32Q/8KV，1T@8192 后 200B@32768；80B-A3B 49 层 1:11、64Q/4KV，500B@32768，Full MoE 另 gated attention。Table3 的 80B16k HySparse90.6 < Full93.6，Table2 也有退步，不采用摘要 across-all 优势。Table4 仅7B，独立 SWA 相对无 SWA 的 MMLU57.1→56.1 反退；仅共享 SA 比同时共享 SA/SWA 的五项改善，支持全局/局部状态分权，不证明作者表征解释唯一因果。硬件、serving batch/concurrency/SLO与端到端 TTFT/TPOT Not Disclosed，“近10x KV”非部署速度/全系统容量，offload 仅 future work。

算法概率冲突触发深入核查：Algo1 L16 缺 Eq3 必需的 exp，不能当正确 probability 或 kernel 实现证明；同 row 共同正仿射可保排名，不因此证明 GQA 跨 head max 等价。保留冲突，不采用无损、无额外内存或 negligible kernel 保证；必要机制、评价和直接反侧足够 STOP，未全附录/全版本比较或复现实验。

Books 具体比较：`MODEL-LONG-CONTEXT` Ch22「选择器的成本如何摊薄：刷新、复用与地址状态」正文明确少数 full layers 产出 block scores/global KV、后续层共享且 layer-local sliding-window KV 保局部 representation；邻接同时解释刷新/地址 owner、stale selection/head imbalance/index 风险、训练结构与短上下文 dense/full+window 回退。1247 源注仅辅助身份，不替代正文。采用命题已有覆盖，No Change，无共享 Books 新写。root 已实际 fresh 读 v1 §3/Algo1、§4.1/4.3/4.4/§5 及 Ch22 396–414完整邻接，首批准入/评分及 Source/Owner PRE 通过。

## 5. 缺口与下一步

本轮扫描、筛选、候选必要审阅与 Books 判断可执行待办 0；root 日级独立复核已通过。外部保留项不进入确定候选、不评分、不支持正面证据/Books 或无遗漏声明。原轮七项日期 hold 与 DebateOCR 中心争议有效保留；原三机构相交项在补充自然日中分别为 HySparse 已处置、GLM API 贡献前关闭、VTok Feb4 窗外，不再要求发布时分秒。下面新增各项的完整题摘仅供潜在贡献筛选，不算全文审阅完成。

- [UQ00279v1](https://arxiv.org/abs/2602.00279v1)、[Faithful-Patchscopes00300v1](https://arxiv.org/abs/2602.00300v1)、[importance00459v1](https://arxiv.org/abs/2602.00459v1)、[Kanade00594v1](https://arxiv.org/abs/2602.00594v1)：分别是 instruction-tuning 置信极化/ECE盲区、decoder prior 与 paired-logit 校准、摘要中 importance 的局部相关性（不授因果）、acoustic constants 与 phonetic/prosody 单流表示；保留评价/faithfulness/representation 主线潜力，不能因科学 QA 或无因果干预直接关闭。root 实际读四项完整 v1 题摘及标记，潜在贡献与日期隔离通过。
- [LOM00029v1](https://arxiv.org/abs/2602.00029v1)、[PTCBENCH00016v1](https://arxiv.org/abs/2602.00016v1)、[PPoGA00007v1](https://arxiv.org/abs/2602.00007v1)：ontology structural→node grounding→paired curriculum、人格 context 变化牵连 reasoning 的评价盲区、local path 修复与 entire-plan discard/reformulate 分权是潜在差额，不把 staged training/benchmark 或自纠正标签当确认新机制。
- [LAVE00612v1](https://arxiv.org/abs/2602.00612v1)、[Calibration jailbreaking00619v1](https://arxiv.org/abs/2602.00619v1)：parallel distributions lookahead 的 CFG 可续完性、loss-dual Gradient Shift 将 logit arithmetic 扩成 proper-loss family为潜在机制/理论，LAVE v2/v3 只轻标，不替代 v1。
- [SayNext00327v1](https://arxiv.org/abs/2602.00327v1)、[RobustDebias00405v1](https://arxiv.org/abs/2602.00405v1)、[KEPO00400v1](https://arxiv.org/abs/2602.00400v1)、[ToolPoker00528v1](https://arxiv.org/abs/2602.00528v1)：分别涉及 next-utterance multimodal cue/dual-route、FT bias amplification 的 DRO、quality-gated OPD 与 teacher-hint rejection sampling、knowing-doing 反证与 solver 行为接口。KEPO 虽用 medical VQA，摘要明示通用后训练差额，不按医疗标签直接排除；ToolPoker 不仅是游戏胜率。潜在贡献均未经必要全文核实，v2/会议名不推日期。
- [Prefill-Decode control02987v1](https://arxiv.org/abs/2602.02987v1)、[PackInfer06072v1](https://arxiv.org/abs/2602.06072v1)：state-dependent service-rate 的 gate-and-route/asymptotic control 与 compute/I/O-aware packed attention/shared-prefix KV layout 为潜在 inference/system 差额，未采用性能或理论保证。搜索 Feb3 只是 Submitted 线索。

上述 15 个新增潜在家族共同缺首次实际公开日；月目录、Submitted（部分早至2025/Jan）及索引不提供落窗证据。精确题摘/标记原件为 `supplement-ab1/ab2/ab3`、[AI 定点题摘](../_sources/daily-20260204/supplement-ai-selected-20261008.json)、[KEPO/撤回标记](../_sources/daily-20260204/supplement-kepo-withdraw-20261008.json)、[系统定点题摘](../_sources/daily-20260204/supplement-system-selected-20261008.json)。唯一外部请求：逐 ID 官方 announcement 或作者/机构首公开事件的北京公开日期；只重开相应 ID 的日期/准入，不投入全文、不扩月份或其他日报。§2 受阻机构则只请求本日原目录切片或具名官方事件，当前失败不当无发布。

[Replacing Parameters with Preferences00485](https://arxiv.org/abs/2602.00485) 当前明确 Withdrawn，v2 Mar5 原因是 substantial revisions；本轮 exact-v1 获取失败，但当前完整题摘/作者声明与 AI 标题目录标记足够隔离，不采用 reward-routing/GRPO 的设计或效果，不把撤回日搬入 Feb3。若恢复，须具名作者新稿/撤回解除及可信原事件日期，只重开该家族；不是待普通全文。

贡献前关闭的本轮代表：[Sora feed philosophy](https://openai.com/index/sora-feed-philosophy/) 全核心给排名原则/可关闭历史信号、生成 guardrail→分发过滤→人工 report+takedown；明称沿用4o图像哲学，未给本事件新的训练/执行/风险成立条件或评价差额，非因缺 benchmark 排除安全；root 实际核心复核通过。[GLM-OCR API](https://docs.z.ai/release-notes/new-released) 只是同 Feb2 research 家族的 Feb3 API 产品事件，具体差额不足，root 实际校准通过。[ADP-MA00307v1](https://arxiv.org/abs/2602.00307v1) 完整题摘仅 planning/orchestration/monitoring/progressive sampling 的组件命名与 demo，无明确新的调度、监控触发或分区规则差额；[Formal Semantic Control00638v1](https://arxiv.org/abs/2602.00638v1) 完整题摘只 VAE 可解释/可控目标和研究方向，未给本事件新的可核机制或理论命题。后两者具体贡献前关闭，公开日期未核实也不影响此处置，未为其索取日期或全论文本体；不是按无 benchmark 拒绝系统或理论。明确题名领域外如 clinical EHR00009、health conversation00017、municipal extraction00316、Turkish binding00380、French drama00588、brain networks00561只作范围关闭，不逐篇扩队列。普通未展开标题不是已读题摘或全量负侧验收。

下面为原轮隔离/关闭记录（保持其当时身份与原窗口，不充作本轮待办）：

本窗可执行待办0；17家族必要审阅/Books决定、全部实际写后和root日级验收通过。下列外部保留项安全隔离，不等正面Evidence或Coverage通过，不阻塞本窗结束。

本窗外部终态保留项：不支持正面证据、Books采用或无遗漏断言；不评分、不进入确定候选。下列分别给出具名定点重开条件：

- 七潜在：[Mirage2Matter00096](https://arxiv.org/abs/2602.00096v1)、[LLaVA-FA00135](https://arxiv.org/abs/2602.00135v1)、[NGFF00148](https://arxiv.org/abs/2602.00148v1)、[HYPEEDIT00105](https://arxiv.org/abs/2602.00105v1)、[VDEBench00122](https://arxiv.org/abs/2602.00122v1)、[GMem00015](https://arxiv.org/abs/2602.00015v1)、[RDD00150](https://arxiv.org/abs/2602.00150v1)。完整题摘具体机制可能相关；Submitted早于本日缓冲，February ID/v1Updated/DOI registered Feb3只给上界，不能排除Feb2公开。有限原入口未得actual first-public；须该ID官方announcement或完全落窗公开字段才定点重开日期/准入，不扩读全文。
- [VTok](https://seed.bytedance.com/en/public_papers) Feb4、[HySparse](https://mimo.xiaomi.com/) Feb3、[GLM-OCR API release](https://docs.z.ai/release-notes/new-released) Feb3：date-only整日相交，需要该事件官方时刻/完全落窗区间，不以Submitted、另一research发布或epoch显示补午夜。HySparse arXiv最早公告在终点，非本窗论文；终态保留不证明事件不存在。
- §2 DeepMind/Meta/Qwen/Moonshot/arXiv主题接口历史切片限制：现入口/有限补检停止，不以当前空页或search无命中授Coverage；恢复只补具名入口本窗切片。
- [DebateOCR00454v1](https://arxiv.org/html/2602.00454v1)：中心MI恢复证明与MATH两表protocol冲突如§4。需要作者勘误/明确aggregation及条件独立证明、γ随K条件，以及逐表一致模型/数据/分辨率/预算配置；未恢复前不采用恢复保证或冲突性能点，争议不是正面Evidence通过。

窗外恢复线索：SPARKLING官方Feb2日历在起点前；2602.02472v1 Submitted Feb2 18:52:52Z最早公告在终点后，归属不得回填。CL 2602.03587v1是必要窗后证据事件，不新计本日候选。不顺带恢复其他日报。

贡献前具名关闭：Google Feb4 Sequential Attention是2022/2024机制说明，所链修订2023/2025，LLM pruning/inference只futurework，无本事件新机制/适用边界；Feb3 virtual-care与Seed BABE为暂缓领域应用，未借Evaluation回收。00359完整题摘只有A-Evolve/演化compute position，无新增可核设计。这些不是因没有benchmark一律关闭理论、安全或局部反证。

## 6. 复核

复核者：root（非作者，本轮增量）。
结论：通过

已实际独立分批通过：全部新增确定家族 1 个 HySparse 的官方 Feb3/精确 v1完整题摘、贡献链与评分6；v1关键机制/Algo1概率冲突、Tables3/4直接反侧、§5未来工作；Ch22具体正文完整邻接的已有覆盖/No Change。Sora 生成/分发/人工安全分工、GLM API 代表贡献前关闭；ADP-MA00307与Formal Semantic Control00638完整题摘中缺具体增量、withdraw00485作者声明均已独立实际检查。日期 hold 分层实际样本包括 UQ00279/Patchscopes00300/importance00459/Kanade00594、LAVE00612/安全calibration00619、KEPO00400/ToolPoker00528；安全/纠错反证信号已实读，普通 hold 按主题/理由抽核，不声称15个全部准入成立或普通标题全审，也不把摘要读完记正面Evidence通过。

root 本轮实际通读六部分增量、抽核 14 来源真实查询/停止与失败边界、核原17候选/原窗口/连续原§4不变、新1处置和外部终态完整性。发现 §2 残留17与最终15不一致，已按独立要求修正；00307/00638具体贡献关闭，不再索取其日期。修正后本轮 DAY 通过；受阻入口、公开日 hold 与旧中心争议未授全Coverage、正面Evidence/Books或无遗漏保证。新写 Books 0，无需写后改书验收。

本轮完成态 V3 校验、本地 Markdown 引用与限定 diff-check 已检查通过；旧17行、原窗口及连续原§4与运行前基线逐字相同。未stage/commit/push、未写共享Books/LS；未创建别日或Weekly。

原轮复核（下文完整保留，不替代本轮 DAY）：

复核者：root（非作者）。
结论：通过

实际独立检查：全部17项拟入选的完整题摘或官方核心与具体采用命题，首4评分、CL评分6、后11准入及DETOUR受限联合评价反证；Google旧机制/00359负侧。必要原证据为L-ICL§3–4/6、CODI§3–7受影响干预、IRT§3–6、domain safety§5/8；CL官方API9项/博客及补充v1§3.4/4/6.3/A1/A5；segment§2/C.4、Polar§3、DIVERGE§3–5/7；FT§4–6、PROBE§3–5、MAN§3–6、Decomp§3–4/8、Debate§3–5/A1 Eq24/41、Dual§3–5、Math§3–5/7、Mixed§4–5、DETOUR§4/5.2–5.4。这些是采用命题必要范围，不称全文/所有附录独立读完或实验复现。

root实际对读全部具体Books决定：7整合的6章9正文段、各末注及前后交接写后通过；FT Ch36、PROBE Ch56、MAN/Dual Ch77、domain safety Ch72、Decomp/Mixed Ch49/24、Math/DETOUR Ch66的具体已有覆盖通过；Debate中心理论/性能冲突终态隔离通过，不用于Books或正面保证。root日级实际通读六部分，核14原源有限查询/停止与失败恢复边界、24项metadata原字段/注册上界及本窗条件相容推定、17家族完整性、七潜在与三日期相交的终态隔离、具名修订/安全与普通负侧。负侧复用已读Google旧机制/00359/暂缓领域应用分批样本，不称所有原始标题逐项全审；宽目录只定位。修正Decomp序列数/每序列token单位后，通过日级验收。所有争议及历史入口缺口不授正面证据、Books或无遗漏保证。

当前17项版本validator及六Books/README限定diff-check通过，本地Markdown引用存在；格式不替代语义日Gate。未stage/commit/push、未写共享LS；本日Books只获锁窄改上述六文件，保护原有dirty。
